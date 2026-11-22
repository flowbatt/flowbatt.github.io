"""Prepare the paper's vector Figure 1 for the interactive web overlay.

No manuscript files are modified. The background preserves the original
Q-encoder, embeddings, DiT styling, and model frames. Both DiTs
reuse the original training artwork at equal size in aligned columns. Original
encoder and embedding shapes are translated onto the same centerline. All original
plot content/frames, static connectors, and enclosing panel borders are removed
so the web overlay can provide equal-size plots, a single capacity matrix,
animated colored links, and open panel headings/rules.
Labels are separately typeset with the self-hosted Source Sans 3 font.

Use --background-only to prepare just the SVG and layout manifest without
reading or rewriting capacity images or numerical example exports.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)


def save_paper_capacity(capacity: np.ndarray, minimum: float, maximum: float) -> str:
    """Original Figure 1 uses Matplotlib cool; input array is cycles × voltage."""
    import numpy as np
    from matplotlib import colormaps
    from PIL import Image

    lookup = colormaps["cool"](np.linspace(0, 1, 256), bytes=True)[:, :3]
    indices = np.clip(np.round((capacity.T - minimum) / (maximum - minimum) * 255), 0, 255).astype(np.uint8)
    relative = "figures/capacity-matr1-paper-cool.png"
    output = ROOT / "webpage/public" / relative
    output.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(lookup[indices]).save(output, optimize=True)
    return relative


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--background-only", action="store_true",
                        help="Write only the SVG background and layout manifest.")
    args = parser.parse_args()
    source = ROOT / "manuscript/figs/drawing_artwork.svg"
    tree = ET.parse(source)
    root = tree.getroot()
    by_id = {element.get("id"): element for element in root.iter()}
    parents = {child: parent for parent in root.iter() for child in parent}
    training_stacks = {
        "data": "g51346", "noise": "g51471-7",
        "interpolant": "g51497", "velocity": "g51471",
    }
    inference_plots = {"input": "g52133", "output": "g52142"}
    panel_borders = {"training": "path1227", "conditioning": "path1235", "inference": "path1231"}
    original_panel_paths = {name: by_id[ident].get("d") for name, ident in panel_borders.items()}
    static_connectors = {
        "capacityEncoder": ["path1351", "path1349"],
        "trainingConditioning": ["g9465"],
        "inferenceConditioning": ["g9465-9"],
        "inferenceInput": ["path4183", "path4185"],
        "inferenceOutput": ["path4189", "path4191"],
        "inferenceFeedback": ["path3673", "path3675"],
    }
    removed_ids = list(inference_plots.values())
    removed_ids += list(training_stacks.values())
    removed_ids += ["g2593", "path2597", "g2709", "path2713", "path2715", "g67648"]
    removed_ids += [ident for group in static_connectors.values() for ident in group]
    removed_ids += list(panel_borders.values())
    for ident in removed_ids:
        parents[by_id[ident]].remove(by_id[ident])

    # Bounds exclude strokes and are expressed in the root viewBox. Retain
    # source geometry separately from the aligned web presentation.
    original_training_dit = [103.0117075337, 11.1938315862, 26.8863352649, 13.3962571267]
    original_inference_dit = [113.4517761694, 50.5356974022, 23.1669482045, 11.5430530762]
    original_training_blocks = [
        [104.5027614054, 11.9779321194, 5.2044445093, 11.8280551954],
        [110.7360224095, 11.9779321194, 5.2044445093, 11.8280551954],
        [116.9692830667, 11.9779321194, 5.2044445093, 11.8280551954],
        [123.2025443309, 11.9779321194, 5.2044445093, 11.8280551954],
    ]
    original_inference_blocks = [
        [114.736561, 51.211327, 4.484475, 10.191792],
        [120.107529, 51.211327, 4.484475, 10.191792],
        [125.478496, 51.211327, 4.484475, 10.191792],
        [130.849464, 51.211327, 4.484475, 10.191792],
    ]
    original_encoder = [32.5839375671, 51.6736120187, 12.3081804327, 10.9779632433]
    original_embedding = [53.5322549514, 54.0557778064, 10.4920955289, 6.2136468238]
    training_shift = [108 - original_training_dit[0], 12.8018715 - original_training_dit[1]]
    inference_shift = [108 - original_training_dit[0], 51.3018715 - original_training_dit[1]]
    encoder_shift = [0, 58 - original_encoder[1] - original_encoder[3] / 2]
    embedding_shift = [0, 58 - original_embedding[1] - original_embedding[3] / 2]

    def translated_box(box: list[float], shift: list[float]) -> list[float]:
        return [round(box[0] + shift[0], 10), round(box[1] + shift[1], 10), *box[2:]]

    def translate(element: ET.Element, shift: list[float]) -> None:
        parent = parents[element]
        index = list(parent).index(element)
        wrapper = ET.Element(f"{{{SVG}}}g", {
            "id": f"{element.get('id')}-web-alignment",
            "transform": f"translate({shift[0]:.10f},{shift[1]:.10f})",
        })
        parent.remove(element)
        wrapper.append(element)
        parent.insert(index, wrapper)

    # Clone before wrapping so both copies retain exactly the same original
    # geometry, stroke widths, fills, and opacity. Rename all cloned IDs.
    training_art = by_id["g13024"]
    inference_art = copy.deepcopy(training_art)
    for element in inference_art.iter():
        if element.get("id"):
            element.set("id", f"{element.get('id')}-web-inference")
    inference_art.set("transform", f"translate({inference_shift[0]:.10f},{inference_shift[1]:.10f})")
    old_inference = by_id["g13024-7"]
    inference_parent = parents[old_inference]
    inference_index = list(inference_parent).index(old_inference)
    inference_parent.remove(old_inference)
    inference_parent.insert(inference_index, inference_art)
    translate(training_art, training_shift)
    translate(by_id["g62414"], encoder_shift)
    translate(by_id["g3131"], embedding_shift)

    # Remove editor-only metadata and unreferenced definitions. This does not
    # rewrite the preserved source shapes, appearance, or opacity.
    for parent in list(root.iter()):
        for element in list(parent):
            if not element.tag.startswith(f"{{{SVG}}}"):
                parent.remove(element)
        for attribute in list(parent.attrib):
            if attribute.startswith("{"):
                del parent.attrib[attribute]
    defs = root.find(f"{{{SVG}}}defs")
    if defs is not None:
        root.remove(defs)
        references = set(re.findall(r"url\(#([^)]*)\)", ET.tostring(root, encoding="unicode")))
        definitions = {element.get("id"): element for element in defs.iter()}
        retained = ET.Element(f"{{{SVG}}}defs")
        while references:
            ident = references.pop()
            if any(element.get("id") == ident for element in retained):
                continue
            element = copy.deepcopy(definitions[ident])
            retained.append(element)
            references.update(re.findall(r"url\(#([^)]*)\)", ET.tostring(element, encoding="unicode")))
        root.insert(0, retained)
    root.set("width", "178.02093")
    root.set("height", "72.192085")
    root.set("role", "img")
    root.set("aria-label", "FlowBatt Figure 1 artwork, with capacity, flow-matching training, and inference curves supplied by the interactive overlay")
    target = ROOT / "webpage/public/figures/figure1-background.svg"
    target.parent.mkdir(parents=True, exist_ok=True)
    tree.write(target, encoding="utf-8", xml_declaration=True)

    manifest = {
        "source": "manuscript/figs/drawing_artwork.svg",
        "labels": "cameraready/figs/drawing_latex.tex",
        "viewBox": [0, 0, 178.02093, 72.192085],
        "panelViewBoxes": {
            "training": [0, 0, 178.02093, 36.4],
            "conditioning": [0, 38.55, 70.4, 33.642085],
            "inference": [71.15, 38.55, 106.87093, 33.642085],
        },
        "panelStructure": {
            "enclosingBordersRemoved": True,
            "removedPathIds": panel_borders,
            "originalPathData": original_panel_paths,
            "originalPathTransform": "translate(-12.0463, -63.417)",
            "layout": "Original panel extents are retained in panelViewBoxes for provenance. The overlay supplies open headings and short rules instead of enclosing panel boxes; model geometry and alignment are unchanged.",
        },
        "boxes": {
            "capacity": [15.5, 52.5, 11, 11],
            "input": [80, 52.5, 16, 11],
            "output": [150, 52.5, 16, 11],
            "originalCapacityFrame": [11.372319, 49.542807, 12.564400, 15.299809],
            "originalInputFrame": [76.691693, 50.836013, 16.117589, 14.493984],
            "originalOutputFrame": [156.302147, 50.836024, 16.117589, 14.493986],
            "inferenceDiT": [108, 51.3018715, 26.886335, 13.396257],
            "inferenceBlocks": [translated_box(box, inference_shift) for box in original_training_blocks],
            "trainingData": [43, 14, 16, 11],
            "trainingNoise": [13, 14, 16, 11],
            "trainingInterpolant": [80, 14, 16, 11],
            "trainingVelocity": [150, 14, 16, 11],
            "originalTrainingDataFrames": [
                [26.440632, 9.886334, 14.338141, 12.893792],
                [34.369016, 7.170276, 14.338141, 12.893792],
                [30.313174, 12.955900, 14.338141, 12.893792],
            ],
            "originalTrainingNoiseFrames": [
                [59.213715, 11.547055, 5.518868, 4.962925],
                [62.243781, 10.175165, 5.518868, 4.962926],
                [61.118178, 12.691972, 5.518868, 4.962926],
            ],
            "originalTrainingInterpolantFrames": [
                [80.258820, 14.759600, 10.783024, 9.696044],
                [85.026162, 12.079131, 10.783024, 9.696044],
                [82.330881, 17.440064, 10.783024, 9.696044],
            ],
            "originalTrainingVelocityFrames": [
                [135.745648, 14.980951, 10.783024, 9.696797],
                [141.665935, 12.300488, 10.783024, 9.696799],
                [139.466677, 17.217944, 10.783024, 9.696799],
            ],
            "trainingDiT": [108, 12.8018715, 26.886335, 13.396257],
            "trainingBlocks": [translated_box(box, training_shift) for box in original_training_blocks],
            "encoder": translated_box(original_encoder, encoder_shift),
            "embedding": translated_box(original_embedding, embedding_shift),
            "originalTrainingDiT": original_training_dit,
            "originalInferenceDiT": original_inference_dit,
            "originalTrainingBlocks": original_training_blocks,
            "originalInferenceBlocks": original_inference_blocks,
            "originalEncoder": original_encoder,
            "originalEmbedding": original_embedding,
        },
        "artworkAlignment": {
            "bounds": "Geometric path/rectangle bounds in root viewBox coordinates, excluding strokes. Leave at least 0.25 units of connector clearance around encoder/embedding shapes.",
            "training": {"sourceGroup": "g13024", "translation": training_shift},
            "inference": {"sourceGroup": "g13024", "replacedGroup": "g13024-7", "translation": inference_shift},
            "encoder": {"sourceGroup": "g62414", "translation": encoder_shift, "strokePadding": 0.17058},
            "embedding": {"sourceGroup": "g3131", "translation": embedding_shift},
            "layout": "Six equal 16-by-11 plots; both identical DiTs at x=108; training and inference centerlines at y=19.5 and y=58. Encoder and embedding share y=58. Original DiT dimensions/styles are reused without scaling; their recorded display dimensions are rounded to six decimals.",
        },
        "training": {
            "layout": "The overlay supplies equal-size plots and animated colored links. The original training DiT artwork is translated onto the shared model column, preserving its styling. Enclosing panel borders are removed in favor of open overlay headings/rules.",
            "originalStackOrder": "Original painter order, with the final card in each original frame array foremost.",
            "state": "x_t = (1-t) x_0 + t x_1",
            "target": "u = x_1 - x_0",
            "prediction": "v_theta(x_t, t, c)",
            "loss": "mean squared error between predicted and target velocity",
            "lossLabelArea": [69, 2.2, 76, 6],
            "removedPlotStackGroups": training_stacks,
            "removedInputArrowIds": ["g2593", "path2597"],
            "removedDiffusionLossIds": ["g2709", "path2713", "path2715"],
        },
        "conditioning": {
            "removedPlotGroup": "g67648",
            "capacityFrameRemoved": True,
            "layout": "The overlay supplies one capacity matrix and animated colored connections. Original Q-encoder and embedding shapes are translated vertically onto the inference centerline without scaling.",
        },
        "inference": {
            "removedPlotGroups": inference_plots,
            "inputOutputFramesRemoved": True,
            "originalFrameBounds": "boxes.originalInputFrame and boxes.originalOutputFrame retain source-art bounds; boxes.input and boxes.output define equal-size displayed plots. The original training DiT artwork is cloned at the inference centerline so both networks have identical size and styling.",
        },
        "connectors": {
            "staticConnectorsRemoved": True,
            "removedGroups": static_connectors,
            "layout": "All original static connectors and arrowheads are removed; animated colored links are supplied by the overlay.",
        },
        "originalFeedbackPath": "M138.86637 57.26675 h2.42958 v-11.76302 h-34.95111 v7.15892",
        "colors": {
            "curve": "#e375c2", "ditFill": "#ad5db5", "ditFillOpacity": 0.733333,
            "ditStroke": "#9137a3", "ditOuterFill": "#eaaedd", "ditOuterFillOpacity": 0.470588,
            "ditOuterStroke": "#a02c89", "encoderFill": "#ffd5e5", "encoderStroke": "#ff5599",
            "panelStroke": "#7e9fb6", "panelStrokeOpacity": 0.796078, "capacityColormap": "cool",
        },
        "removed": [
            "path1227/path1235/path1231 (enclosing borders of the training, conditioning, and inference panels)",
            "g52133/g52142 (complete inference input/output plots: curves, backing, and frames)",
            "g51346/g51471-7/g51497/g51471 (complete original training plot stacks, including frames and curves)",
            "g2593/path2597 (original training input connector and arrowhead)",
            "g2709/path2713/path2715 (diffusion-specific loss connector and arrowheads)",
            "g67648 (capacity contours, backing, frame, and ticks)",
            "g9465/g9465-9 (training and inference conditioning arrows/arrowheads)",
            "path3673/path3675 (inference feedback connector and arrowhead)",
            "path4183/path4185/path4189/path4191 (inference input/output connectors and arrowheads)",
            "path1349/path1351 (lavender capacity/encoder/embedding connectors)",
        ],
        "removedIds": removed_ids,
    }
    (target.parent / "figure1-layout.json").write_text(json.dumps(manifest, indent=2) + "\n")

    if args.background_only:
        print(f"Wrote {target.relative_to(ROOT)} ({target.stat().st_size:,} bytes) and layout manifest.")
        return

    # Existing export retains all numeric values. Recreate only its companion
    # paper-palette image without rerunning inference or changing any arrays.
    import numpy as np

    example_path = ROOT / "webpage/src/data/overview-example.json"
    example = json.loads(example_path.read_text())
    with np.load(ROOT / example["metadata"]["sourceDataset"], allow_pickle=False) as archive:
        matrix = archive["x_test"][example["metadata"]["testIndex"]]
    assert np.allclose(matrix[:, ::-1].T, example["capacity"]["values"], atol=5e-10, rtol=0)
    paper_image = save_paper_capacity(matrix, example["capacity"]["minimum"], example["capacity"]["maximum"])
    example["capacity"]["paperColormap"] = "cool"
    example["capacity"]["paperImage"] = paper_image
    example["capacity"]["paperColormapSource"] = "Original Figure 1 capacity contours in manuscript/figs/drawing_artwork.svg use the Matplotlib cool palette."
    example_path.write_text(json.dumps(example, separators=(",", ":"), allow_nan=False) + "\n")
    (ROOT / "webpage/public/data/overview-example.json").write_bytes(example_path.read_bytes())
    print(f"Wrote {target.relative_to(ROOT)} ({target.stat().st_size:,} bytes), layout manifest, and matched cool-palette capacity image.")


if __name__ == "__main__":
    main()
