# Paper XAI heatmaps

The three PNGs are byte-for-byte copies from `cameraready/figs/`:

| File | Paper panel | SHA-256 |
| --- | --- | --- |
| `heatmaps_test_data.png` | `fig:qmatrix_b`: MATR-1 test capacity matrices | `ecdfa66ad7935833f3453ae19278747cadd384edc52633e060621f7e088b276b` |
| `heatmaps_bml_cnn_3.png` | `fig:cnngradcam`, right: CNN Grad-CAM example | `fd2e49a4a7eaf1607ca95bb55743ee7986e843ee6e753a6c1440a55a4d01163f` |
| `heatmaps_cnn_3.png` | `fig:xcnngradcam`, right: XAI-CNN Grad-CAM example | `07e4d6e32af44b2f60fac5872e4f7fbf0800f30c6f4641c65a8742ce60e73e6d` |

`src/components/XaiHeatmaps.astro` aligns these three original 42-cell grids.
It adds Source Sans 3 panel labels outside the raster images. The SVG viewport
`20 20 833 710` removes only surrounding blank margins from the original
873 × 868 canvases. Heatmap pixels, colormap, tile order, borders, and spacing
are unchanged. The grids stack on narrow screens.

The images contain no embedded text. No numerical axes or colorbar are added;
the original plotting code uses cycle number horizontally and voltage
vertically. The archived Grad-CAM workflow normalizes per cell, and its plotting
code also autoscales each tile. Colors must not be interpreted as a shared
absolute attribution scale across cells or models, or as confidence.

These are the original paper examples for standalone scalar-RUL CNNs, not
attributions of FlowBatt's generated trajectories. Historical file suffixes
are not exposed as checkpoint or best/worst labels. The archived ReLU and
LeakyReLU branches also differ in preprocessing; the displayed image comparison
alone is not a controlled activation-only ablation. No newer reproduction
outputs, inferred sample IDs, or performance metrics are substituted.

The short subsection text condenses the camera-ready CNN encoder paragraph
(line 193) and appendix Grad-CAM discussion (lines 602–660). The displayed text
describes blank attribution maps; a blank rectified Grad-CAM image alone does
not establish a zero gradient.
