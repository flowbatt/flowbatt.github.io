# Original paper RUL figure, with Source Sans 3

`export_rul_plots.py` converts `cameraready/figs/rul_one_row.pdf` directly to one inline SVG. The only visual change is the requested Source Sans 3 font. The original one-row arrangement, colors, marker sizes, clipping, grid, frames, ticks, pink identity lines, dataset titles, axis labels and individual colorbars remain intact.

- Asset: `public/figures/rul/rul-one-row.svg`; `viewBox="0 0 396 72.881054"`.
- Extracted point/text metadata and hashes: `public/data/rul-paper-scatter.json` (schema 2).
- Inline using an Astro `?raw` import so the page’s self-hosted Source Sans 3 applies. Scale the whole SVG proportionally; do not rearrange panels. IDs are namespaced and no global CSS selectors are introduced.
- Original labels remain “Reference” beneath every panel and “Prediction” at the far left only, with black dataset titles and σ with RUL subscript. Font weight remains regular 400. No cycle-unit text or new legend is inserted into the figure.

| Paper order | Markers | Both axis ranges | Original colorbar tick labels |
| --- | ---: | --- | --- |
| MATR-1 | 42 | 0–2500 | 5, 12, 20, 28, 36 |
| MATR-2 | 40 | 500–2000 | 6, 12, 19, 25, 31 |
| HUST | 22 | 1000–3000 | 5, 31, 57, 82, 108 |
| MIX-100 | 137 | 0–3000 | 3, 53, 102, 151, 200 |
| MIX-20 | 147 | 0–2500 | 5, 73, 141, 209, 277 |

The 388 markers and original cyan-to-magenta `cool` colors are retained directly as vector artwork. The source marker centered at `(1645, 2033.5)` in MATR-2 keeps its original size and clipping above the 2000 y-limit, including its small visible cap. The earlier navy/magenta restyling, smaller markers, explicit unit-bearing axes and separate panel assets are superseded and removed.

## Provenance and fidelity

The individual source PDFs are identified and hash-checked using `manuscript/figs/rul_one_row.json`. Its composition script documents that the original composite changed only the repeated y-axis titles. The combined manuscript and camera-ready PDFs are byte-identical: 990,389 bytes, SHA-256 `7b27aaf5f00bdeb94bea8e19709c1b79ad7ea85e1c2e97e5b2496e6c7817d0bb`.

Poppler converts the actual composite to SVG. The exporter removes only the original glyph definitions and 272 glyph uses, then adds 80 live Source Sans 3 text runs. It reads each run’s original PDF baseline, size and rotation and applies the recorded original composition transform; natural glyph shapes and advances change with the font. Every non-text SVG node is retained unchanged, apart from namespacing IDs/references; full serialized-subtree equality is asserted after reversing that prefix. Original colorbar raster images remain embedded unchanged. The SVG has accessible title/description text without adding visible annotations.

The JSON additionally records original PDF decimal marker coordinates, cycle coordinates, color-bin indices, complete identity paths, source hashes and text-run transformations. These are read directly from the original PDF, not regenerated inference or screenshot digitization. Uncertainty colors represent the standard deviation of scalar RUL from ten generated SOH trajectories per sample; there are no error bars. The PDF does not retain exact raw standard deviations or the ten underlying predictions, and its caption does not identify the plotted coordinate’s aggregation. No exact sigma or mean/median claim is inferred. The available seed-2026 caches differ and are not substituted.

## Reproduce and check

```sh
PYTHONDONTWRITEBYTECODE=1 python webpage/scripts/export_rul_plots.py
```

Requires Python’s standard library and the existing Poppler `pdftocairo` executable. No installations or network access are needed. All writes stay under `webpage/`; intermediate conversion is in `.qa/rul/`. Original source files remain read-only.

Verified automatically: original PDF hashes/composite identity, all 388 marker records, original colors/ticks/ranges, unchanged converted non-text artwork, text-run count/labels, unique IDs and resolved internal references. The original paper was visually inspected from a Poppler PNG. Page integration build passed at 13:47. Desktop browser inspection confirmed the original single-row composition, cool palette, pink identity lines, original marker cap and Source Sans 3 replacement without text overlap. Unrelated accessibility/release checks remain separate.
