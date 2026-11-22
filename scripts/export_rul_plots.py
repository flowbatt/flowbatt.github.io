"""Preserve the original one-row paper figure, replacing only its font.

Run with Python and the existing Poppler pdftocairo executable:
    PYTHONDONTWRITEBYTECODE=1 python webpage/scripts/export_rul_plots.py

All generated files stay under webpage/. Original PDFs are read-only. The
camera-ready composite is converted directly to SVG, and all non-text artwork
is retained. Original text runs are replaced by live Source Sans 3 at the same
baseline positions, font sizes, rotations and regular weight. There is no
replotting, new inference, palette substitution, or per-panel rearrangement.
"""
from __future__ import annotations

import hashlib
import json
import copy
import subprocess
import re
import zlib
from decimal import Decimal
from pathlib import Path
import xml.etree.ElementTree as ET

WEBPAGE = Path(__file__).resolve().parents[1]
PROJECT = WEBPAGE.parent
QA = WEBPAGE / ".qa/rul"
QA.mkdir(parents=True, exist_ok=True)
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
NUMBER = r"[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?"
DATASETS = (
    ("MATR-1", "matr-1", 0, 2500, 42),
    ("MATR-2", "matr-2", 500, 2000, 40),
    ("HUST", "hust", 1000, 3000, 22),
    ("MIX-100", "mix-100", 0, 3000, 137),
    ("MIX-20", "mix-20", 0, 2500, 147),
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_stream(path: Path) -> str:
    """Read this known, hash-verified Matplotlib PDF's Flate content stream."""
    candidates = []
    for match in re.finditer(rb"\nstream\r?\n(.*?)\r?\nendstream", path.read_bytes(), re.S):
        try:
            text = zlib.decompress(match.group(1)).decode("latin1")
        except zlib.error:
            continue
        if "/P0 Do" in text:
            candidates.append(text)
    assert len(candidates) == 1, (path, len(candidates))
    return candidates[0]


def extract_panel(dataset: str, slug: str, low: int, high: int, count: int, record: dict) -> dict:
    source = PROJECT / record["source"]
    assert sha(source) == record["source_sha256"], f"Published source changed: {source}"
    stream = text_stream(source)
    clip = re.search(rf"({NUMBER}) ({NUMBER}) ({NUMBER}) ({NUMBER}) re W n", stream)
    assert clip is not None
    left, bottom, width, height = map(Decimal, clip.groups())
    assert width == height
    labels = re.findall(r"\(([^()]*)\) Tj", stream)
    ticks = [int(value) for value in labels[:labels.index("Reference")]]
    assert ticks == [int(value) for value in labels[labels.index("Reference") + 1:labels.index("Prediction")]]
    color_ticks = labels[labels.index(dataset) + 1:labels.index(dataset) + 6]
    assert len(color_ticks) == 5 and all(value.isdigit() for value in color_ticks)

    # The known source uses repeated translation matrices for one circular marker
    # form. Decimal accumulation retains the original PDF operator precision.
    events = re.compile(
        rf"(?P<color>({NUMBER})\s+({NUMBER})\s+({NUMBER})\s+rg)"
        rf"|(?P<point>1 0 0 1 ({NUMBER}) ({NUMBER}) cm /P0 Do)"
    )
    x = y = Decimal(0)
    color = None
    points = []
    span = Decimal(high - low)
    for event in events.finditer(stream):
        if event.group("color"):
            color = [Decimal(value) for value in re.findall(NUMBER, event.group("color"))]
            continue
        numbers = re.findall(NUMBER, event.group("point").split("cm")[0])
        x += Decimal(numbers[-2])
        y += Decimal(numbers[-1])
        assert color is not None and color[2] == 1
        assert abs(color[0] + color[1] - 1) < Decimal("0.000000001")
        color_bin = round(color[0] * 255)
        assert abs(color[0] * 255 - color_bin) < Decimal("0.0000001")
        reference = Decimal(low) + (x - left) / width * span
        prediction = Decimal(low) + (y - bottom) / height * span
        points.append({
            "index": len(points),
            "referenceCycles": float(reference),
            "predictedCycles": float(prediction),
            "referenceCyclesDecimal": str(reference),
            "predictedCyclesDecimal": str(prediction),
            "pdfXDecimal": str(x), "pdfYDecimal": str(y),
            "originalRgbDecimal": [str(value) for value in color],
            "uncertaintyColorBin": color_bin,
        })
    assert len(points) == count == stream.count("/P0 Do")

    # Retain the source identity polyline's complete path, including its endpoints.
    identity = re.search(r"0\.8901960784 0\.4666666667 0\.7607843137 RG\s+(.*?)\nS", stream, re.S)
    assert identity is not None
    identity_pdf = [list(map(Decimal, pair)) for pair in re.findall(rf"({NUMBER}) ({NUMBER}) [ml]", identity.group(1))]
    # Matplotlib simplified the long MIX identity paths to four vertices.
    assert 2 <= len(identity_pdf) <= count
    identity_data = [[float(Decimal(low) + (px-left)/width*span), float(Decimal(low) + (py-bottom)/height*span)] for px, py in identity_pdf]
    # PDF line vertices are rounded to six decimals, unlike marker translations.
    assert max(abs(px-py) for px,py in identity_data) < 0.001

    return {
        "dataset": dataset, "slug": slug, "count": count,
        "svg": "figures/rul/rul-one-row.svg", "viewBox": [0, 0, 396, 72.881054],
        "sourcePdf": record["source"], "sourcePdfSha256": sha(source),
        "contentStreamSha256": hashlib.sha256(stream.encode("latin1")).hexdigest(),
        "sourcePlotBoxPdfDecimal": list(clip.groups()),
        "xRange": [low, high], "yRange": [low, high],
        "xTicks": ticks, "yTicks": ticks,
        "colorbarTickLabels": color_ticks,
        "colorbarTickFractions": [0, 0.25, 0.5, 0.75, 1],
        "colorbarTickPrecision": "Original integer-formatted labels; not exact standard-deviation extrema.",
        "clippedPointCount": sum(not(low <= p["referenceCycles"] <= high and low <= p["predictedCycles"] <= high) for p in points),
        "points": points,
        "identityPolylinePdfDecimal": [[str(x),str(y)] for x,y in identity_pdf],
        "identityPolylineCycles": identity_data,
    }


def extract_text_runs(stream: str) -> list[dict]:
    """Read the limited text operators in these hash-verified Matplotlib PDFs."""
    operations = re.compile(
        rf"(?P<font>/F\d+ ({NUMBER}) Tf)"
        rf"|(?P<matrix>(?:{NUMBER}\s+){{6}}Tm)"
        rf"|(?P<move>{NUMBER}\s+{NUMBER}\s+Td)"
        r"|(?P<show>\([^()]*\)\s+Tj)"
        r"|(?P<array>\[.*?\]\s+TJ)", re.S
    )
    runs = []
    for block in re.findall(r"BT\s+(.*?)\s+ET", stream, re.S):
        size = None
        matrix = [1., 0., 0., 1., 0., 0.]
        for operation in operations.finditer(block):
            if operation.group("font"):
                size = float(re.search(rf"({NUMBER}) Tf", operation.group("font")).group(1))
            elif operation.group("matrix"):
                matrix = list(map(float, re.findall(NUMBER, operation.group("matrix"))))
            elif operation.group("move"):
                tx,ty = map(float,re.findall(NUMBER,operation.group("move")))
                matrix[4] += matrix[0]*tx + matrix[2]*ty
                matrix[5] += matrix[1]*tx + matrix[3]*ty
            else:
                value = operation.group("show") or operation.group("array")
                text = "".join(re.findall(r"\(([^()]*)\)", value)).replace("\x1b", "σ")
                assert size is not None
                assert matrix[:4] in ([1.,0.,0.,1.],[0.,1.,-1.,0.])
                runs.append({"text":text,"fontSizePdf":size,"xPdf":matrix[4],"yPdf":matrix[5],
                             "rotation":-90 if matrix[:4]==[0.,1.,-1.,0.] else 0})
    return runs


def remove_original_glyphs(root: ET.Element) -> int:
    """Remove only font glyph definitions/uses; preserve every other SVG node."""
    removed = 0
    for parent in root.iter():
        for child in list(parent):
            if child.get("id","").startswith("glyph-"):
                parent.remove(child)
            elif child.tag == f"{{{SVG_NS}}}use" and child.get("{http://www.w3.org/1999/xlink}href","").startswith("#glyph-"):
                parent.remove(child)
                removed += 1
    return removed


def namespace_ids(root: ET.Element, prefix: str) -> None:
    identifiers = {e.get("id"):prefix+e.get("id") for e in root.iter() if e.get("id")}
    for element in root.iter():
        for key,value in list(element.attrib.items()):
            if key == "id":
                element.set(key, identifiers[value])
            elif value.startswith("#") and value[1:] in identifiers:
                element.set(key,"#"+identifiers[value[1:]])
            else:
                element.set(key,re.sub(r"url\(#([^)]*)\)",lambda match:f"url(#{identifiers[match.group(1)]})",value))


def render_original_row(records: list[dict], panels: list[dict], paper: Path) -> dict:
    converted = QA / "original-row.svg"
    subprocess.run(["pdftocairo","-svg",str(paper),str(converted)],check=True)
    original = ET.parse(converted).getroot()
    assert original.get("viewBox") == "0 0 396 72.881054"
    removed_glyphs = remove_original_glyphs(original)
    assert removed_glyphs == 272
    # The original converted graphical subtree is copied unchanged into the final
    # asset. ID prefixing is the only serialization change to its graphics.
    graphics_bytes = ET.tostring(original,encoding="utf-8")
    graphics_hash = hashlib.sha256(graphics_bytes).hexdigest()
    output = copy.deepcopy(original)
    prefix = "rul-paper-"
    namespace_ids(output,prefix)
    restored = ET.tostring(output,encoding="unicode").replace(prefix,"")
    assert restored == graphics_bytes.decode()

    text_layer = ET.SubElement(output,f"{{{SVG_NS}}}g",{
        "id":"rul-paper-source-sans-text", "font-family":"Source Sans 3, sans-serif",
        "font-weight":"400", "fill":"#000000", "stroke":"none",
    })
    row_height = 72.881054
    all_runs = []
    for record,panel in zip(records,panels):
        scale,offset = record["uniform_scale"],record["x_offset_pt"]
        runs = extract_text_runs(text_stream(PROJECT/record["source"]))
        for run in runs:
            if run["text"] == "Prediction" and not record["prediction_ylabel"]:
                continue
            x = run["xPdf"]*scale + offset
            y = row_height-run["yPdf"]*scale
            size = run["fontSizePdf"]*scale
            attributes={"x":f"{x:.10f}","y":f"{y:.10f}","font-size":f"{size:.10f}"}
            if run["rotation"]:
                attributes["transform"]=f"rotate({run['rotation']} {x:.10f} {y:.10f})"
            node=ET.SubElement(text_layer,f"{{{SVG_NS}}}text",attributes)
            node.text=run["text"]
            all_runs.append({"dataset":panel["dataset"],**run,"xSvg":x,"ySvg":y,"fontSizeSvg":size})
        panel["paperCompositeScale"]=scale
        panel["paperCompositeXOffset"]=offset
        panel["predictionYLabel"]=record["prediction_ylabel"]
    expected_text=[r["text"] for r in all_runs]
    assert expected_text.count("Reference")==5 and expected_text.count("Prediction")==1
    assert expected_text.count("σ")==5 and expected_text.count("RUL")==5
    output.set("role","img")
    output.set("aria-labelledby","rul-paper-title rul-paper-description")
    title=ET.Element(f"{{{SVG_NS}}}title",{"id":"rul-paper-title"})
    title.text="FlowBatt RUL prediction: original five-panel paper figure"
    desc=ET.Element(f"{{{SVG_NS}}}desc",{"id":"rul-paper-description"})
    desc.text=("Original paper Figure 4 in one row: MATR-1, MATR-2, HUST, MIX-100 and MIX-20. "
               "Prediction versus reference RUL. Cyan-to-magenta color shows the standard deviation of RUL "
               "from ten generated SOH trajectories per sample. Original markers, ranges, grids, ticks, "
               "pink identity lines and individual colorbars are preserved; only the font is Source Sans 3.")
    output.insert(0,title)
    output.insert(1,desc)
    assert not list(output.iter(f"{{{SVG_NS}}}style"))
    ids=[element.get("id") for element in output.iter() if element.get("id")]
    assert len(ids)==len(set(ids))
    for element in output.iter():
        for key,value in element.attrib.items():
            for reference in re.findall(r"url\(#([^)]*)\)",value):
                assert reference in ids
            if key.endswith("href") and value.startswith("#"):
                assert value[1:] in ids
    destination=WEBPAGE/"public/figures/rul/rul-one-row.svg"
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(ET.tostring(output,encoding="unicode")+"\n")
    # Remove only the superseded assets produced by this same exporter.
    for panel in panels:
        obsolete=destination.parent/f"{panel['slug']}.svg"
        if obsolete.exists():
            obsolete.unlink()
    return {"svg":"figures/rul/rul-one-row.svg","viewBox":[0,0,396,72.881054],
            "svgSha256":sha(destination),"svgBytes":destination.stat().st_size,
            "originalNonTextSvgSha256":graphics_hash,
            "nonTextArtworkUnchanged":True,"replacedGlyphUses":removed_glyphs,
            "textRuns":all_runs,"uniqueIdCount":len(ids)}


def main() -> None:
    manifest=PROJECT/"manuscript/figs/rul_one_row.json"
    records=json.loads(manifest.read_text())
    assert [record["dataset"] for record in records]==[dataset[0] for dataset in DATASETS]
    paper=PROJECT/"cameraready/figs/rul_one_row.pdf"
    assert sha(paper)==sha(PROJECT/"manuscript/figs/rul_one_row.pdf")
    panels=[extract_panel(*dataset,record) for dataset,record in zip(DATASETS,records)]
    artwork=render_original_row(records,panels,paper)
    result={
        "schemaVersion":2,
        "source":"Original camera-ready composite PDF converted to SVG; only text font is replaced.",
        "paperFigure":"Figure 4, RUL prediction",
        "paperPdf":str(paper.relative_to(PROJECT)),"paperPdfSha256":sha(paper),
        "compositionManifest":str(manifest.relative_to(PROJECT)),"compositionManifestSha256":sha(manifest),
        "exporter":"webpage/scripts/export_rul_plots.py","exporterSha256":sha(Path(__file__)),
        "font":"Source Sans 3 regular 400 (official static Adobe 3.052R)",
        "fontSha256":sha(WEBPAGE/"public/fonts/source-sans-3-regular.woff2"),
        "palette":{"original":"Matplotlib cool (cyan-to-magenta), unchanged original vector colors and colorbar images","bins":256},
        "presentation":"Original single row, geometry, labels, marker sizes, grid, axes, ticks, pink identity lines and colorbars. Only font substitution.",
        "meanings":{
            "x":"Reference RUL in cycles, as plotted in the paper.",
            "y":"Predicted RUL in cycles, as plotted in the paper; caption does not specify coordinate aggregation.",
            "color":"Standard deviation of scalar RUL extracted from ten generated SOH trajectories per test sample.",
            "errorBars":"None in the source; none introduced.",
        },
        "limitations":[
            "The PDF records exact plotted coordinates and 256 uncertainty color bins, not the ten underlying scalar predictions or raw per-cell standard deviations.",
            "Integer-formatted colorbar labels do not identify exact normalization extrema. No exact sigma values or mean/median aggregation are inferred.",
            "Available seed-2026 uncertainty caches differ from the published figure and are not substituted.",
            "Live text retains original text-run baselines, font sizes and rotation; natural glyph shapes and text advances change with the requested font substitution.",
        ],
        "totalPointCount":sum(panel["count"] for panel in panels),"artwork":artwork,"panels":panels,
    }
    assert result["totalPointCount"]==388
    destination=WEBPAGE/"public/data/rul-paper-scatter.json"
    destination.write_text(json.dumps(result,indent=2)+"\n")
    print(artwork["svg"],artwork["viewBox"],artwork["svgBytes"],"bytes")
    print("Verified unchanged non-text artwork;",artwork["replacedGlyphUses"],"glyph uses replaced by",len(artwork["textRuns"]),"live text runs.")


if __name__=="__main__":
    main()

