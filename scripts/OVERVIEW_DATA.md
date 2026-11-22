# Real-data overview figure

The schematic uses a matched input matrix, early SOH observations, reference
trajectory, and model outputs for **MATR-1 test-array row 9**, displayed as
“MATR-1 · test cell 10”, with **draw 5** (the sixth of ten fresh draws).
This is a deliberately selected good example with both reference and prediction
reaching 80% SOH after 1000 cycles. Selection is post hoc, not an unbiased or
aggregate performance estimate; the exact screening rule is recorded below.

The schematic preserves the **whole original Figure 1 composition** while
animating both a training-objective example and inference. Training uses
**MATR-1 train row 0**; inference uses **test row 9**. Only the test capacity matrix is displayed; the training sweep uses its own
separate capacity input, recorded in the training export and caption. Soft
model highlights and pink/purple particles indicate schematic information
flow, not recorded activations. The whole figure automatically loops while
visible, without view/play/slider/reference controls, equations, an MSE
readout, or a progress bar. The current presentation uses open a/b/c sections, short magenta rules, bold
navy headings, and one subtle horizontal divider. All visible schematic labels
are lowercase STIX Two Text Bold (700), with black axes. Equal plot/model
sizes and 2.85-second timing remain; the inference example is selected
for close agreement and a lifetime beyond 1000 cycles. Lower-page illustrative
figures remain unchanged. Final data/source, build, and desktop/mobile checks pass; user review and
broader release audits remain open. Earlier checks below are historical.

## Sources and identity

- Input and reference: `github/datasets/MATR-1.npz`, `x_test[9]` and
  `y_test_physical[9]` (with the same fitted inverse transform used by inference).
- Trained model: `github/checkpoints/flowbatt/MATR-1.pth`, loaded strictly through
  the repository's `flowbatt.inference.load_flowbatt`.
- SHA-256 hashes of both source files are embedded in the exported JSON.
- The reference was checked to be exactly equal to test row 9 in the cached
  `results/generative_uq/matr_1_Q/flowbatt_10_samples.npz` reference array. The
  website predictions are fresh reproducible draws, not copies of that cache.
- The numeric archive has no serialized cell IDs. “Test cell 10” is the
  one-based array row, not an inferred original battery identifier.

## Deliberate example selection

`select_overview_example.py` screens the existing ten-draw cache, excluding the
former test row 0 and requiring the reference's first 80% crossing to occur
strictly after cycle 1000. Five rows qualify. Ranking uses the mean of all ten
individual forecast RMSEs, excluding known indices 0–9 and including the first
reference crossing. Row 9 ranks first, with cached mean RMSE **1.080956 SOH
percentage points**. Cached results select the cell; they are not reused as
the website's predictions.

Ten fresh CPU draws are evaluated with the actual checkpoint. Among draws
whose own first 80% crossing exceeds 1000 cycles, draw 5 has the lowest forecast
RMSE (**0.406084 percentage points**); the ten-draw mean is **0.928376**.
Metrics cover 94 forecast coordinates, cycles 101–1031. Reference and selected
prediction first reach 80% at **1031** and **1041** cycles; all ten fresh
predictions cross at 1021–1071. Crossings use the first sampled value at or
below 80% on the ten-cycle grid, without interpolation. These post-hoc metrics
illustrate a good prediction and do not support a claim of typical accuracy.

The download records the five-row ranking, eligibility criteria, fresh metrics,
selected index, and source/cache/checkpoint/export/selection-script hashes.
Fresh draws use a seed reset after checkpoint loading and need not match the
cached multi-cell noise batch.

## Capacity matrix and orientation

The actual input is an unnormalized **100 cycle × 100 voltage** float32 matrix.
Values are discharge-capacity differences in **Ah** relative to cycle 10. The
preprocessing sets cycle 11 to zero and replaces non-finite values with zero;
the baseline cycle 10 is also zero. These are preserved rather than visually
filled or reconstructed.

The original extractor stores voltage columns from high to low. The lossless
100 × 100 PNG therefore uses `x_test[9].T`: cycles increase left to right,
highest voltage is at the top. The JSON `capacity.values` rows are reversed
into low-to-high voltage order, with `voltageIndices` 1–100 reindexed in that
order. Its grid-index 1 is at the bottom. No physical voltage limits were
retained in the numeric archive, so the axis says “voltage grid”, not volts.
No numerical input samples are downsampled or spatially smoothed.

The current figure uses the original Figure 1 **cool** palette, sampled at 256
entries with linear scaling over the complete matrix minimum/maximum (no
percentile clipping). The companion image is selected by `capacity.paperImage`
(`figures/capacity-matr1-paper-cool.png`), with `paperColormap: "cool"` and
`paperColormapSource` recording provenance. The original SVG's capacity contour
colors follow the same cool palette. The figure preserves the paper's compact
composition without adding a colorbar; Ah units and the exact range are in
the download and this note.

The earlier **cividis** image and its exact lookup remain in `capacity.image`,
`colormap`, and `colormapStops` for reproducibility, but are not displayed in
the current schematic. Both PNGs quantize only color. JSON numeric capacity
values are rounded to 9 decimal places (less than 0.0000000005 Ah error); the
model receives the original float32 data.

## SOH reference and time axes

The prepared SOH reference is already causally smoothed, and its fixed-length
sequence has a 70% padding floor. It must be called a **preprocessed reference**,
not raw measurements. Exact unsmoothed values and raw measured length are not
recoverable from this archive. See the preserved conversion manifest at
`repository_archive/pre_cleanup/datasets/manifest.json` and the original
`codes_data_pretrained_models/batlinet/data/databundle.py` preprocessing.

The trajectory samples correspond to cycles **1, 11, …, 2551**, a 10-cycle
stride. The first **10** preprocessed SOH points (cycles 1–91) initialize the
observed prefix, alongside the first 100 cycles' capacity matrix conditioning.
The vector field masks those prefix coordinates; float32 dense-output
interpolation can introduce sub-micro-unit normalized roundoff, which is
checked and recorded, not overwritten in the export.

The reference display ends at its first **80% SOH crossing**, cycle
1031, including that sample (`referenceDisplayLength: 104`). This avoids
presenting the later 70% padded floor as measurements. The current inference viewing window is fixed at cycles 0–1200 and
80–110% SOH, while the export retains the full horizon through cycle 2551. The export additionally records optional individual prediction
display lengths through each curve's first 80% crossing; the current figure
uses fixed SVG viewing windows rather than those lengths to truncate predictions. The JSON retains full
numerical curves without clipping, smoothing, or projection.

## Actual model animation

Ten independent Gaussian noise draws are generated in one CPU batch, with
`torch.manual_seed(2026)` set after model construction. The actual model has
four DiT blocks, hidden width 16, condition-dropout probability 0, and guidance
scale 1. The export caches the real 16-component CNN conditioning embedding
and uses the repository's cached-condition vector-field evaluator.

The adaptive **dopri5** ODE solve uses `atol=rtol=1e-5`. It returned 101 actual
solution outputs at requested times `t = 0, 0.01, …, 1`; the recorded run made
170 vector-field evaluations. These output frames **are not the adaptive
solver's internal steps** and must not be labeled as such. They are not a
linear visual morph from noise to reference. Plotting adjacent coordinates
as line segments is a normal presentation of the sampled trajectory.

Animation frames follow draw 5; its final frame equals `trajectories.samples[5]`
exactly in the JSON. The opening figure now shows only this one sample; the
previous large ensemble plot has been removed. The other nine final curves
remain in the download and are genuine independent draws from the same
checkpoint, battery input, and solve. They are a sample ensemble, not a
calibrated uncertainty interval. The initial draw ranges
from 42.196% to 123.202% when expressed in inverse-transformed SOH coordinates;
early generative states extend beyond the fixed visible window and are not
physical predictions.
Display a distinct “flow state” label before `t=1`.

The SOH state plots keep the GIF's **80–110%** window. Compact plots
show major ticks at 80/100/110 and endpoint cycle labels. Training uses cycles **0–2500** (its target reaches 80% at
cycle 2161); inference uses **0–1200** (sample/reference crossings 1041/1031).
The archived GIF's MATR-1 x window of 0–900 belongs to a different cell, test
row 14, so it is not copied onto this example. SVG clipping hides out-of-view
values without numerical clamping or autoscaling. Early noise spans about
42.196–123.202% and is deliberately partly outside this fixed view. The original
pink/purple/cool palette remains confined to Figure 1; reference and fixed
prefix marks remain black with distinct line styles.

## Training-objective export

`export_training.py` reads `x_train[0]` and the corresponding normalized and
physical training labels from `github/datasets/MATR-1.npz`. It uses the same
MATR-1 checkpoint as inference. Seed 2026 is set after loading the checkpoint;
the first ten initial coordinates are copied from the training trajectory.
No cell identity or raw measured endpoint is inferred from the archive.

At 101 requested time positions, `AffineProbPath(CondOTScheduler())` evaluates
`x_t = (1−t)x_0 + t x_1`, with alpha `t`, sigma `1−t`, and terminal noise
coefficient zero. The target normalized velocity is `u_t = x_1−x_0`. The fixed
checkpoint in evaluation mode predicts `v_theta(x_t,t,Q)` directly. The
exported per-time loss is `mean((v_theta−u_t)^2)` over **all 256 normalized
coordinates**, including the prepared trajectory's padding. Target and
predicted velocities are exactly zero over the ten known coordinates.

This deterministic time sweep illustrates the training objective; actual
training samples time uniformly. It performs **no optimization, parameter
updates, or inference ODE solve**, and its loss profile is not training
progress or expected to decrease. SOH state plots inverse-transform states;
velocity stays in normalized units and uses **−4 to 4** across all 256 cycle
coordinates (1–2551). An affine state offset must never be added to velocity.
The export records the appropriate multiplicative conversion separately.

`src/data/training-example.json` and its identical `public/data` copy contain
`training.times`, `cycles`, `statesNormalized`, `x0Normalized`, `x1Normalized`,
`targetVelocityNormalized`, `predictedVelocityNormalized`, `loss`, and
`observedCount`; `normalization` supplies units and conversions. Metadata
records source/checkpoint/code hashes, seed, split, selection, and meaning.
Training capacity PNGs are `data/capacity-matr1-training-cool.png` and
`data/capacity-matr1-training-cividis.png`, selected by `capacity.paperImage`
and `capacity.image` respectively. They preserve the same orientation and
100 × 100 native resolution as the test input.
Each matrix uses its own recorded minimum/maximum for color mapping; equal
colors across the train/test pair do not necessarily mean equal Ah values.

Checks cover original input/target equality before rounding, exact path
endpoints and affine formula, target equality, finite values, prefix velocity
zeros, MSE equivalence, unchanged dataset/checkpoint hashes, and identical
public/source copies. Training and inference time arrays agree within
3.6e-8 float32 roundoff. Training values use six-decimal presentation copies;
capacity uses nine decimals. These checks do not establish aggregate accuracy.

## GIF timing reference

`github/assets/generation.gif` was inspected read-only. It has 121 frames,
1650 × 376 pixels, and infinite looping. Its **current decoded duration is
2.85 seconds**: 240 ms on frame 0, 119 interior frames at 20 ms, and 230 ms on
frame 120. Frames correspond to 121 requested ODE output times from 0 to 1.
Representative frames are pixel-identical to the archived original; only the
timing differs. The old render script's 8.55-second export (600/50/2000 ms)
is therefore not the current speed reference.

The webpage's 101 saved frame positions use 240 ms initially, `2380/99` ms
for each of 99 interior holds, and 230 ms at the end: the same 2.85-second
cycle, with no synthetic intermediate states. Training and inference share
the same automatic playback clock but retain their different mathematical meanings. Playback timing
is independent of training/inference computation time. Motion pauses when
the figure is offscreen or the document hidden. Reduced-motion mode keeps the
final state still. No manual scrubber or reference toggle appears in this
simplified schematic; the reference remains visible. Audit metadata and
extracted frames are under `webpage/.qa/generation-gif/`; scripts were read
from `repository_archive/workspaces/figure3_generation_20261023/` without
running them or writing outside `webpage/`.

## Figure 1 artwork

`scripts/prepare_paper_schematic.py` derives
`public/figures/figure1-background.svg` from the label-free
`manuscript/figs/drawing_artwork.svg`. Its plot curves and capacity colors are
replaced by matched real-data overlays. The Q-encoder, embedding stacks, DiT
blocks, and original model styles supply the visual vocabulary; black arrows
are removed and model positions/sizes are adapted to the webpage grid.
The original camera-ready label layout is recorded in
`cameraready/figs/drawing_latex.tex`; the website repositions and simplifies its
labels. Current schematic typography is lowercase **STIX Two Text Bold 700**,
self-hosted with the unmodified official WOFF2; source/version/hash records are
in `public/fonts/STIX-SOURCE.txt` and redistribution terms in
`public/fonts/LICENSE-STIX.txt` (SIL OFL 1.1). Other figures retain Computer
Modern. The website uses flow-integration terminology, identifies the voltage
grid without unsupported volts, and keeps one whole-figure view.

The current grid specification uses six equal **16 × 11** SVG plot frames:
top-row `y=14`, bottom-row `y=52.5`, state/input column `x=80`, and
velocity/output column `x=150`. Both DiTs use `x=108` and dimensions
**26.886335 × 13.396257**, vertically centered at `y=19.5` and `y=58`.
Stronger curve/axis/connector strokes and clear endpoint gaps improve
legibility; axes are black. The progress bar remains absent. Enclosing panel
paths `path1227`, `path1235`, and `path1231` are removed; open navy headings,
short magenta rules, and one subtle horizontal divider organize a/b/c instead.
A strict XML comparison confirms that removing these borders changes no
remaining artwork geometry, and all aligned manifest bounds remain identical.
Final source/static checks, production build, and Firefox desktop/390 × 844
inspection verify the open layout, bold type, and retained alignment.

`public/figures/figure1-layout.json` records the original viewBox, panel crops,
overlay bounds, DiT block coordinates, feedback path, source color values
and opacities, and removed panel paths with their original coordinates/transform. No manuscript source is edited by this preparation step.

## Regeneration and checks

Use the existing ML environment, not the Astro Node environment:

```bash
PYTHONDONTWRITEBYTECODE=1 MPLCONFIGDIR="$PWD/webpage/.cache/matplotlib" python webpage/scripts/export_overview.py
PYTHONDONTWRITEBYTECODE=1 MPLCONFIGDIR="$PWD/webpage/.cache/matplotlib" python webpage/scripts/export_training.py
PYTHONDONTWRITEBYTECODE=1 MPLCONFIGDIR="$PWD/webpage/.cache/matplotlib" python webpage/scripts/prepare_paper_schematic.py
```

The inference exporter performs no training. It
writes `src/data/overview-example.json`, an identical downloadable copy at
`public/data/overview-example.json`, and both the cividis and cool capacity
PNGs. The training exporter writes its separate JSON and capacity assets. The final
command prepares the SVG and layout manifest and regenerates
the cool PNG from the original numeric archive without rerunning inference;
only the paper-palette metadata is added to existing JSON. For artwork-only
changes, pass `--background-only` to avoid touching capacity PNGs or data JSON.
No source model,
training data, manuscript, or benchmark result is changed.

Export checks include original input/reference equality, agreement with the
cached benchmark reference, finite values and expected dimensions, observed
prefix preservation within float32 solver roundoff, and equality of the final
animation frame to selected ensemble draw 5. JSON SOH values are rounded to six decimal
places (less than 0.0000005 percentage-point error). The matrix is intended to
be rendered from the compact PNG; do not serialize all 10,000 numeric entries
into the interactive browser payload when they are only needed for download.

Historical checks of the preceding inference-only revision confirmed original Figure 1 placement, matched input and
recorded states, final-state/sample equality, reference cutoff, full sample
horizon, and truthful animation-time labels. The final production build and
static audit pass: 31 unique IDs, 12 valid asset/link references, matching JSON
copies, 101 states, and exact final-state/draw-0 equality.

Firefox desktop full/inference-detail views and the 390 × 844 layout were
inspected. Playback, pause, reference curve/legend synchronization, slider
Home/Right/End at times 0/0.01/1, and narrow-screen horizontal keyboard panning
were verified. Full-figure/detail views work at phone width and switching views
resets horizontal pan. Initial/final displayed scales are 40–125% and 65–100%.
Full keyboard traversal, reduced-motion emulation, and a JavaScript-disabled
browser check remain unverified release checks. Earlier-layout checks remain
historical in `PLAN.md`; user design review is still open.

Historical combined training/inference revision before visual simplification:
numerical checks, independent
scientific review, and final production build pass. Static checks verify 36
unique IDs, 14 valid asset/link references, matching source/public/built JSON
for both examples, 101 time positions aligned within 1e-6, and exact inference
endpoint/draw-0 equality. An independent timing/geometry check passes all 101
frame boundaries, 240/230 ms endpoint holds, the 2.85-second loop, and unchanged
out-of-window coordinates.

Firefox desktop and 390 × 844 views were inspected. Both panels animate in
sync; Home/Right/End select times 0/0.01/1; play/pause works; the reference
control changes only the test curve and its legend. Narrow controls fit,
horizontal panning reaches predictions, and keyboard focus is visible. Full
reduced-motion emulation, JavaScript-disabled browsing, complete keyboard
traversal, and user review remain open. No files outside `webpage/` changed.

Historical presentation revision before the equal-grid refinement: compact I/O plots, one displayed test matrix,
plain labels without equations/MSE, no black connector arrows or controls,
and an automatic loop with shared-clock particles/block highlights. Source
data, fixed plot windows, and timing values are unchanged. The revised
component build and independent scientific/runtime source review pass.
Firefox desktop confirms automatic repeated looping without input and the
intended one-matrix/control-free presentation. At 390 × 844, typography,
progress, and legend wrap cleanly; keyboard panning reaches output/velocity
plots without page overflow. The caption distinguishes the test matrix from
the separately matched training input and identifies the fixed-checkpoint
sweep and schematic particles. The final production build after the caption
update passes (22:20), with 35 unique IDs, five resolving local assets, and
both built JSON downloads matching their sources. Static checks confirm matching source/public data, one
capacity plot, no schematic buttons/inputs, and no black fills/strokes in the
background artwork.
Reduced-motion/offscreen/background behavior was source-reviewed, not browser
emulated; full keyboard and JavaScript-disabled audits remain open.

Historical equal-grid refinement (2026-11-22), before the current open-panel/
typography/example revision: equal data-plot dimensions, matching
DiT dimensions and alignment, stronger strokes with clear connector gaps,
and removal of the progress bar. Real exports, one displayed test matrix,
101-frame mapping, fixed axes, and 2.85-second loop are unchanged. The final
production build passes at 12:09:49 after all component/assets edits. Static
checks verify all six 16 × 11 plots, matching DiT size and `x=108` placement,
common input/output columns, absent progress-bar markup/selectors, matching
source/public/built JSON, 35 unique IDs, and five valid local assets.
Independent source review found no runtime/layout issues; connectors clear
borders and labels after accounting for packet sizes. Firefox desktop and
390 × 844 inspection confirms aligned models/plots, stronger strokes, clear
gaps, no progress bar, continued automatic motion, and keyboard horizontal
panning to the output. The existing user preview at port 4321 serves the
current code. No new reduced-motion/background-lifecycle emulation was
performed; those broader audits and user appearance review remain open.
All writes for this iteration are under `webpage/`.

Current revision: remove enclosing panel boxes, use lowercase STIX Two Text
Bold 700 throughout the schematic, black axes, open headings/rules, and an
explicitly selected good prediction with lifetime beyond 1000 cycles. Equal
plot/model dimensions, training data, 80–110% SOH, and the 2.85-second loop
remain. Border-only XML/geometry checks pass. Final build passes at 12:24:51;
source/public/built JSON are identical for both examples, all 101 states end
exactly at draw 5, and independently recomputed RMSE is 0.406084. Static checks
verify metadata-driven 0–1200 cycles, six equal plots/aligned DiTs, 35 unique
HTML IDs, resolving anchors and six local assets, removed panel paths, and
matching embedded/public STIX bytes.
Independent source review and Firefox desktop/390 × 844 inspection pass:
bold open sections have no overlap/page overflow, automatic states advance,
and mobile keyboard panning reaches the output with clean legend wrapping.
Final data audit verifies source/checkpoint/cache/script hashes, input/reference
rounding fidelity, exact PNG lookup/orientation, and matching source/public
exports (430,298 bytes; SHA-256
`3e2158efcc44f7f4c461505854acad388b48630cabb68752166b409b7f597272`).
Known-prefix drift is at most 0.000031 SOH percentage points from float32
dense-output roundoff; training/inference times agree within 3.6e-8.
The existing port-4321 preview is restored to desktop. User review remains open.
Reduced-motion/background-lifecycle emulation, complete keyboard traversal,
and JavaScript-disabled testing remain unperformed release checks.
