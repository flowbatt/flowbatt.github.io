# FlowBatt project webpage: plan, requirements, and checklist

Last updated: 2026-11-22  
Status: the current iteration moves the unchanged original 14px TL;DR into the 700px reading column, reduces university logo display widths to 118.8px/138px, removes the schematic toolbar/header and automatic-loop label without changing its animation, and removes the displayed Limitations section while retaining its source. Add a brief paper-grounded RUL discussion and all five paper Figure 4 scatter panels, restyled with Source Sans 3/navy-magenta while preserving original geometry and separate uncertainty scales. The approved schematic plus this requested RUL figure are now in scope; other demos remain deferred. Current scientific asset review, production build, static integration, and Firefox desktop/900px/390px verification pass. Prior passes below are historical; user review and broader release/accessibility audits remain open. Local only, not deployed.  
Working directory: `webpage/`

This is the working plan for the FlowBatt project page. Update the decisions, checklist, and iteration log as the website develops. Check an item only when its acceptance condition is met; attach a file, preview, or short verification note where useful.

## 1. Purpose and audience

Present **FlowBatt: Flow Matching for Probabilistic Battery Degradation Prediction**, accepted at NeurIPS 2026, as an accessible, scientifically grounded academic project page with the approved animated schematic, requested RUL figure, and traceable paper results.

The main story is:

**Early-life battery measurements → multiple plausible degradation trajectories → lifetime estimates and empirical prediction intervals.**

| Audience | Questions the page should answer |
| --- | --- |
| AI researchers | What is the modeling contribution? How do conditioning, flow matching, and the DiT backbone work? How can I reproduce or extend the results? |
| Battery researchers | What measurements are required? Which cells, chemistries, and benchmark settings were evaluated? What do the trajectories and intervals mean? |
| Industry readers | What can the approach estimate? What would be required to evaluate it on our data? Which capabilities are demonstrated, and which are future applications? |

Opening title: **FlowBatt: Flow Matching for Probabilistic Battery Degradation Prediction.**

The full paper title leads a centered academic banner. Use academic prose throughout, explain unfamiliar battery and modeling terms on first use, and support the narrative with the approved full-width method overview, concise paper-based prose, and the actual benchmark table.

## 2. Decisions and defaults

| Topic | Decision or proposed default | Status |
| --- | --- | --- |
| Framework | Astro | Selected by the user |
| Project location | `webpage/` | Selected by the user |
| Current deliverable | RUL discussion/five-panel figure, TL;DR in 700px column, smaller logos, no visible schematic toolbar/loop label or Limitations section | Scientific/build/static/three-width browser checks pass; user review open; local only |
| Site structure | Academic banner, concise unheaded overview, Methodology, Results and discussion, Conclusions and outlook, resources/citation | Current user-approved concise structure |
| Rendering | Static HTML, semantic results table, and client-side JavaScript for the approved schematic | Existing Astro implementation |
| Template | Small custom Astro layout; borrow selected components only if useful | Proposed |
| Opening layout | Centered conference/title/authors/resources in the hero; original 14px TL;DR and 100-word overview in the 700px reading column | Two desktop TL;DR lines and natural mobile wrapping verified |
| Hosting | GitHub Pages, with a custom domain optional | Proposed; not configured |
| Charts | Approved SVG schematic plus five-panel paper Figure 4 RUL figure; Table 1 remains semantic HTML | RUL figure requested; other charts/explorers deferred |
| Animation | Preserve the approved SVG/CSS/requestAnimationFrame implementation and 2.85-second loop | Unchanged this iteration |
| Demo data | Existing versioned training and matched inference exports | Preserve unchanged; additional explorer exports deferred |
| Visual direction | Navy/black/magenta on white/light-gray; 700px reading column, 16px/1.65 body, left 22px h2/18px h3, justified prose/captions/notes | Current publication-layout requirements |
| Typography | Self-hosted Source Sans 3 regular/semibold/bold across the entire page, table, citation, and schematic | Only active CSS font family; symbols, diagram labels, and layout verified |
| Opening schematic | Preserve open sections, palette, geometry, data, axes, and automatic loop; change only its font to the common Source Sans 3 family | Approved scientific content/layout retained |
| Live inference | Optional later Gradio/Hugging Face Spaces companion | Deferred |

Proposed defaults allow local implementation to proceed without resolving every design preference first. The user has authorized local implementation, concise content, shared typography, and publication preparation, while preserving the schematic's scientific content and geometry. Hosting ownership, the public URL, and publication remain launch decisions; deployment, uploads, purchases, and server experiments are outside the current request.

### Current palette and academic layout requirements

| Role | Color | Use |
| --- | --- | --- |
| Navy | `#17365D` | Heading/link accents and reference curves |
| Black | `#111111` | Body text, observed data, and neutral graphical marks |
| Magenta | `#C2188B` | Generated trajectories and associated illustrative spread |
| Background | White / light gray | Consistent reading surface with restrained section separation |

These tokens replace the earlier cyan/pink preference. Retain labels and line styles so color alone does not carry meaning. Use self-hosted **Source Sans 3** for every visible element, including citation/BibTeX and schematic labels; regular, semibold, and bold support the hierarchy. Figure labels stay lowercase/bold. [Source/version records](public/fonts/SOURCE-SANS-3-SOURCE.txt), the [license](public/fonts/LICENSE-SOURCE-SANS-3.txt), and [font README](public/fonts/README.md) document the current family. STIX and Computer Modern files remain historical assets, not active typography.

Use a **700px** body column, **16px** text with **1.65** line height, left-aligned **22px h2** and **18px h3** headings, and justified paragraphs, figure/table captions, and metric notes. The title banner retains its academic centered arrangement. Final visual checks must include mobile word spacing/overflow and ± rendering.

**Figure 1 palette exception:** the opening schematic retains its original pink curve `#E375C2`, purple DiT blocks, encoder/embedding colors. Enclosing panel frames are replaced by bold navy headings, short magenta rules, and one subtle horizontal divider; axes are black. The real capacity matrix uses the paper's **cool** colormap, with cycle number horizontal and “Voltage grid” vertical. The always-visible reference is dashed black and the fixed observed prefix solid black. Pink/purple tracks, particles, and block highlights replace black connector arrows. Units (Ah), exact matrix range, and palette provenance remain in the downloadable data; the compact paper composition has no added colorbar. The earlier cividis PNG is retained as an alternate asset but is not displayed. This explicit user-requested exception does not change the accepted site palette elsewhere.

Keep all six authors in manuscript order, include affiliation numbers, and make the full affiliations available from the banner. Use the real arXiv paper, FlowBatt repository, and checkpoint-directory URLs; verify reachability without describing them as placeholder release links. Remove the separate branding/navigation bar, duplicated team section, marketing-style headings, and promotional card grids. Use a visible BibTeX block and compact contact footer.

OGAS is the structural reference, not a source of FlowBatt claims or figure data. Retain Astro and the existing scientific scope. All work remains local; no deployment is authorized by this iteration.

### Current schematic grid requirements

- Give all six data plots the same **16 × 11** dimensions in SVG coordinates, including the velocity plot. Top-row plots use `y=14`; bottom-row plots use `y=52.5`.
- Align the state/input column at `x=80` and the velocity/output column at `x=150`.
- Place both DiTs at `x=108` with equal **26.886335 × 13.396257** dimensions, centered at `y=19.5` and `y=58` to match the respective plot rows.
- Increase curve, axis, and connector stroke widths while retaining distinct line styles and clear gaps between connectors and plot/model borders.
- Remove the progress bar. Preserve automatic looping, one displayed test capacity matrix, plain labels, and the absence of equations, MSE, playback controls, and black arrows.
- Preserve every numerical export, data mapping, fixed axis limit, reference cutoff, reduced-motion fallback, geometry, and 2.85-second timing. Apply Source Sans 3 to its text; no scientific or geometric changes are part of this iteration.

## 3. Current release scope and deferred additions

The current page includes:

- The academic title banner, NeurIPS 2026 identification, authors, affiliations, and real resource links.
- The exact original screenshot TL;DR, restored verbatim, and unchanged 100-word overview without an Abstract heading; the lay summary remains removed.
- The approved real-data schematic and brief methodology paragraph. Remove the visible schematic toolbar/header and automatic-loop label; preserve geometry/data/colors/axes/timing and automatic motion.
- Brief protocol and qualitative findings from Section 3.1, with unchanged semantic Table 1 in the 700px reading width. Keep all values and full metric/± notes in source/provenance, but remove the visible metric-note list; no repeated numeric prose.
- A new approximately 80-word paper-grounded RUL-prediction discussion with all five Figure 4 scatter panels, restyled in Source Sans 3/navy-magenta without changing point/axis geometry or their separate uncertainty scales.
- Concise paper-based conclusion and outlook, including competitive trajectory-derived RUL and synthetic SOH improving downstream RUL modeling. Remove the visible Limitations heading/paragraph at the user’s request while retaining the complete source export and caveats in provenance.
- Citation/contact, intact official university logos at 118.8px/138px display widths, then the unchanged exact accepted acknowledgment in justified 13px text. Preserve conditional metadata/social card without deploying.

The approved schematic and newly requested RUL figure are the current figure scope. All other figures and demos remain removed from the displayed page at the user's direction. Separate trajectory/generation explorers, benchmark plots, capacity/XAI views, synthesis galleries, application cards, live inference, and talk/video additions are **deferred, not first-release obligations**. Their former checklist entries are retained as historical/backlog records, not instructions to restore them. User uploads, accounts, arbitrary chemistry/protocol simulation, and a production battery-management interface remain outside scope.

## 4. Page structure and content provenance

| Section | Required content and source |
| --- | --- |
| Academic title banner | Conference, full title, authors, affiliations, and paper/code/checkpoint links |
| Opening | Original screenshot TL;DR unchanged at 14px in the 700px column, targeting two desktop lines; unchanged 100-word unheaded overview |
| Methodology | Unchanged brief paragraph and approved Figure 1; remove visible toolbar/header/automatic-loop label in addition to previously removed caption/timing note; preserve animation/data/provenance |
| Results and discussion | SOH protocol/findings and unchanged six-method/five-dataset Table 1 at 700px, plus new brief RUL discussion and original five-panel Figure 4; retain source definitions and separate uncertainty scales |
| Conclusions and outlook | Concise conclusion/outlook retaining RUL/synthesis findings; remove displayed Limitations section while retaining its export and scientific caveats in source |
| Resources, citation, contact, and acknowledgment | Existing links/citation/email followed by the full accepted camera-ready acknowledgment in small text |

Use the 700px column, Source Sans 3, left-aligned section headings, justified prose/captions/notes, academic tone, and accepted navy/black/magenta palette. Table 1 is a semantic table, not an extra figure image. The paper's quantitative results remain distinct from the curated schematic example's single-cell metrics. The user-requested note removals are presentation changes; retain the complete definitions, timing/selection explanation, provenance, and JSON exports in source. Institutional logo source files remain unchanged; only their proportional display widths shrink to 60%. Source guidance and the NeurIPS text-only decision remain documented under `public/logos/`.

| Editable file | Provenance responsibility |
| --- | --- |
| `src/data/paperContent.ts` | Original TL;DR, exact accepted acknowledgment, unchanged concise/historical prose, full Table 1 caption/notes, and references |
| `scripts/PAPER_CONTENT.md` | Exact source locations, transcription decisions, source differences, and table interpretation |
| `src/data/content.ts` | Author/affiliation metadata and citation |
| `src/pages/index.astro` | Section order, semantic text/table presentation, actual resource URLs, and citation behavior |
| `src/components/RulPlots.astro` | Five-panel RUL figure, responsive layout, and accessible panel descriptions |
| `src/data/overview-example.json`, `src/data/training-example.json` | Approved schematic numerical exports; unchanged |
| `scripts/export_rul_plots.py` | Reproduce the five RUL SVG panels from published PDF vector coordinates and color bins; no replacement inference |
| `public/figures/rul/{matr-1,matr-2,hust,mix-100,mix-20}.svg` | Live Source Sans 3 Figure 4 panels with original points, axes, and separate color scales |
| `public/data/rul-paper-scatter.json` | All 388 original marker coordinates/color bins, converted axes, source/output hashes, and precision limitations |
| `scripts/RUL_PLOTS.md` | RUL extraction, ordering/scales, styling decisions, source uncertainty limitations, and reproduction |
| `scripts/OVERVIEW_DATA.md` | Schematic data, model, timing, selection, and scientific interpretation |
| `astro.config.mjs`, `src/pages/index.astro` | Conditional production origin/base path and canonical/Open Graph/social metadata |
| `public/social-card.png` | Reproducibly generated local 1200 × 630 social card; visually verified |

The public resource targets are [arXiv 2611.03150](https://arxiv.org/abs/2611.03150), [FlowBatt code](https://github.com/HamidrezaEiv/FlowBatt), and [pretrained checkpoints](https://github.com/HamidrezaEiv/FlowBatt/tree/main/checkpoints). Record link verification separately from writing the correct targets. The citation URL points to the paper; no fake/pending publication URL is displayed.

### Publication preparation boundary

Use the actual future public origin from `FLOWBATT_SITE_URL` and optional repository/subdirectory path from `FLOWBATT_BASE_PATH` (default `/`). Canonical and absolute Open Graph/social-image URLs are conditional on that origin; no guessed project URL is embedded. Local builds without the origin and development previews retain `noindex, nofollow`, even though visible local-preview labels are removed. Ordinary local title/description metadata does not claim deployment. Prepare the social card locally and verify default-local and configured-production/base-path output before release. No upload, hosting/domain change, or deployment is authorized by this preparation task.

## 5. Approved animation and deferred interactions

The approved schematic and requested five-panel RUL figure are the current figure scope. The schematic remains the only scientific animation required in this iteration. It automatically loops while visible, pauses offscreen/when hidden, and uses a static final state for reduced motion. Preserve the existing behavior, recorded values, plain labels, absence of visible controls/progress rail, and distinct physical-cycle/flow-time interpretation.

The previous trajectory explorer and separate generation illustration are removed from the page. Their components may remain unused in the repository. Dataset selectors, interval/reference toggles, EOL threshold controls, additional generation scrubbing, benchmark filters, XAI interactions, and synthesis viewers are deferred until explicitly prioritized in a later iteration. Any future restoration needs verified real data, clear selection rules, honest interval/calibration language, and a separate accessibility audit; the current request does not require implementing them.

## 6. Scientific and data requirements

| ID | Requirement |
| --- | --- |
| SCI-01 | Resolve accepted text from revision macros and reconcile manuscript/camera-ready copies before publishing claims or the downloadable PDF. |
| SCI-02 | Describe flow matching as adapted to conditional battery trajectory generation; preserve the paper's contribution scope. |
| SCI-03 | Present conditioning windows as fixed benchmark settings: 20 or 100 cycles. An arbitrary history-length slider requires additional supported model outputs. |
| SCI-04 | Explain the capacity-matrix input and the observed SOH prefix used by the current sampling initialization; audit exactly which inputs each example uses. |
| SCI-05 | Do not imply direct temperature, charging-protocol, cooling, or current-profile controls in the current model. Dataset metadata are distinct from model inputs. |
| SCI-06 | Describe intervals as empirical prediction intervals. State the nominal level, sample count, and measured coverage where relevant; do not imply guaranteed calibration. |
| SCI-07 | Reconcile every benchmark leadership or ranking claim with the authoritative publication, task, metric, and aggregation before displaying it. Keep SOH, RUL, and synthesis claims distinct; do not carry forward unverified all-benchmark or four-of-five wording. |
| SCI-08 | State dataset/split context and the MIX-20 training-set difference when comparing with BatLiNet. Do not equate benchmark diversity with proven generalization to unseen chemistries or protocols. |
| SCI-09 | Use actual numeric outputs for interactive charts. Figure geometry extracted from PDFs is not a substitute for full-precision predictions. |
| SCI-10 | Audit scaling, physical cycle coordinates, resampling, valid observation lengths, EOL handling, and padded tails before export. Padded reference values must not appear as measured future behavior. |
| SCI-11 | Preserve the paper's metric definitions for headline results, including aggregation and the meaning of error bars. Cached demo samples may be from a different evaluation run. |
| SCI-12 | Attach hardware, batch size, sample count, and timing procedure to any runtime comparison. Animation playback is not a speed benchmark. |
| SCI-13 | Present test planning, fleet applications, and second-life assessment as potential applications unless supported by a completed evaluation. Include current limitations near the relevant claims. |

Two issues already identified during planning require explicit reconciliation:

1. `results/generative_uq/summary.csv` contains values that differ from manuscript tables. Do not silently substitute one for the other; identify the run and metric conventions before choosing a source.
2. `manuscript/figs/prepare_interval_one_row.py` documents that some figure assets use simplified vector paths, alternative cached draws, threshold clipping, and padded reference tails. Audit the underlying numeric data before using these assets in an interactive view.

The exporter should produce small, versioned browser assets with:

- Benchmark, cell identifier/index, split, conditioning window, and default EOL threshold.
- Explicit cycle coordinates and SOH units/normalization.
- Reference values plus a validity mask or original observation endpoint.
- Generated trajectories, sample count, median, and interval definition.
- Generation output times and intermediate states for animated examples.
- Source paths, checkpoint identifier/hash, seed information, preprocessing version, and export-script version where available.
- A short record of example selection and any display-only transformations.

Record unknown provenance fields as unresolved rather than inferring them from filenames. Export only the data needed for the page; keep checkpoints and full research outputs outside the site bundle.

### Current overview data contract

The overview uses `github/datasets/MATR-1.npz` test row 9, displayed as **MATR-1 · test cell 10**. This is a deliberately good example: excluding the former row 0, five cached cells have a reference 80% crossing strictly after 1000 cycles; row 9 has the lowest mean individual-draw forecast RMSE among them. The displayed fresh draw is then selected by lowest forecast RMSE among draws whose own 80% crossing also exceeds 1000 cycles. Selection is post hoc, not representative or unbiased. Metrics exclude the ten known prefix coordinates and include the reference's first 80% crossing; cache ranking, fresh results, and source hashes are retained. The archive has no serialized cell ID or raw measured length; these remain unknown. The real input matrix is **100 cycles × 100 voltage points**, with unnormalized discharge-capacity differences in **Ah** relative to cycle 10. The original cycle-11 zeroing and non-finite-value treatment are preserved. Both PNG palettes retain all 10,000 input samples at native resolution, with cycle increasing left to right and highest voltage at the top. The current figure selects the **cool** image through `capacity.paperImage`; the earlier cividis asset remains reproducible. Since physical voltage limits are unavailable, the y-axis says **voltage grid**.

The exporter loads `github/checkpoints/flowbatt/MATR-1.pth` and generates **ten fresh draws on CPU**, with seed 2026 set after model construction. It saves **101 actual dopri5 output states** for selected draw 5 at requested times 0–1, using `atol=rtol=1e-5` and 170 vector-field evaluations. Its final frame equals ensemble draw 5 exactly. The fresh mean per-draw forecast RMSE is 0.928376 SOH percentage points, and displayed draw RMSE is 0.406084; these selected-example metrics are not headline benchmark claims. Output times are not internal adaptive solver steps, and the animation must not interpolate a fictional path toward the reference. Any animation playback duration is independent of inference runtime.

The SOH coordinates are cycles **1, 11, …, 2551**, and the first ten preprocessed SOH values initialize the known prefix. The reference is already causally smoothed and has a 70% padding floor; it is labeled **preprocessed reference** and displayed only through its first 80% crossing, cycle 1031. This display limit avoids showing the padding floor as measured future behavior and is not a recovered raw measurement endpoint. The current inference view shows only **draw 5** with fixed axes of 0–1200 cycles and 80–110% SOH. Its first 80% crossing is cycle 1041. The initial selected state spans approximately 42.196–123.202% and is partly outside the window. The complete modeled horizon through cycle 2551 remains in the export. SVG clipping hides out-of-window noise without clamping numeric values or rescaling. All ten predictions and optional per-draw first-80%-crossing lengths remain in the export for future displays. The retained numerical states and predictions are not clipped, smoothed, or projected by the exporter. The downloadable ensemble is not labeled a calibrated prediction interval.

Training uses the first **train-array row**, its own capacity input, and the same fixed checkpoint. `src/data/training-example.json` and its identical public copy record 101 CondOT positions `x_t=(1−t)x_0+t x_1`, normalized target `u=x_1−x_0`, actual predicted velocity, and mean squared velocity error over all 256 coordinates. This is an objective illustration, **not optimizer history or ODE inference**. Training SOH axes stay at 0–2500 cycles and 80–110%; normalized velocity stays at −4…4 over cycles 1–2551. Only the test matrix is displayed. The provenance explains that the training sweep used its own separate input, retained in the training export; the visible schematic caption is removed in this iteration. Equations and numeric MSE remain in the provenance/data contract, not in the visual schematic.

The current `github/assets/generation.gif` was decoded read-only: 121 frames, 2.85-second infinite loop, 240 ms first/20 ms interior/230 ms last. The shared automatic website sweep uses its 101 real saved positions with first/last holds preserved and 99 intermediate holds of `2380/99` ms. No new numerical states are invented; playback duration is not computation time. The archived 8.55-second timing is historical. All generated assets, caches, and audit files for this work remain under `webpage/`.

The matched data, source SHA-256 hashes, ODE settings, axes, and selection rule are available in `src/data/overview-example.json` and its identical public download. See [the provenance note](scripts/OVERVIEW_DATA.md) for the complete contract and limitations. The separate `GenerationPreview.astro` and `TrajectoryPlot.astro` illustrations are no longer displayed and are deferred. The one-cell export does not substitute for the published Table 1 results.

## 7. Candidate local sources

Paths below are relative to this document. The camera-ready PDF/source govern current paper prose and Table 1. Other research assets remain candidates for future work, not additional current deliverables.

| Source | Intended use |
| --- | --- |
| [Main manuscript](../manuscript/main_rev_HE.tex) | Narrative, methods, results, authors, limitations, and citation details |
| [Camera-ready PDF](../cameraready/cameraready.pdf) and [source](../cameraready/cameraready.tex) | Authoritative current abstract, Section 3.1/Table 1, conclusion, limitations, and outlook |
| [Page content module](src/data/paperContent.ts) and [provenance note](scripts/PAPER_CONTENT.md) | Transcribed page text, table data, and exact source/metric interpretation |
| [Bibliography](../manuscript/cameraready.bib) | Related work and source attribution |
| [Architecture artwork](../manuscript/figs/drawing_artwork.svg) | Adaptable vector diagram; retain applicable attribution |
| [Generation figure](../manuscript/figs/record1d_flowbatt.png) | Storyboard reference for the generation animation |
| [FlowBatt sampler](../codes_data_pretrained_models/nns.py) | Export generation states via `return_records=True` |
| [Model runner](../codes_data_pretrained_models/run_model.py) | Checkpoint loading and sampling configuration |
| [Postprocessing](../codes_data_pretrained_models/pp_utils.py) | Audit scaling, resampling, and threshold conventions |
| [Saved predictions](../results/generative_uq/) | Candidate numeric samples and references for all five benchmark settings |
| [MATR-1 example cache](../results/generative_uq/matr_1_Q/flowbatt_10_samples.npz) | Inspected in initial research: reference shape `(42, 256)` and sample shape `(10, 42, 256)` |
| [Prepared MATR-1 archive](../github/datasets/MATR-1.npz) | Actual overview input and preprocessed reference from selected test row 9 |
| [Released MATR-1 checkpoint](../github/checkpoints/flowbatt/MATR-1.pth) | Strictly loaded pretrained model for the overview's fresh CPU draws |
| [Overview exporter](scripts/export_overview.py) and [provenance](scripts/OVERVIEW_DATA.md) | Reproducible real-data export, numerical checks, axes, settings, and limitations |
| [Interval-figure preparation](../manuscript/figs/prepare_interval_one_row.py) | Identify existing display transformations and reference-tail issues |
| [Figure assets](../manuscript/figs/) | Capacity matrices, heatmaps, and publication plots |
| [Synthetic samples](../results/synthesis/flow_samples_10_per_cell.npz) | Candidate later synthesis gallery; verify the corresponding experiment |
| [Runtime package](../prediction_time_a100/README.md) | Timing methodology and provenance; reconcile with the final reported hardware/run |

## 8. Implementation and design requirements

- Keep application source, exported public data, and data-export scripts under `webpage/`; preserve the research source files.
- Use Astro static output. Add interactive components only where needed; choose one component framework if vanilla TypeScript becomes unwieldy.
- Keep prose and benchmark summaries separate from visualization logic so authors can revise copy without editing chart code.
- Use a reproducible Python export step for scientific data, with explicit source files and output schemas.
- Lazy-load larger example collections and media. Show a useful first plot without downloading every sample.
- Keep a static image or textual result available when JavaScript is disabled or a demo cannot load.
- Support narrow mobile layouts, keyboard operation, visible focus, readable labels, and touch controls. Do not encode reference/prediction identity by color alone.
- Respect reduced-motion preferences. The opening Figure 1 automatically pauses offscreen/when hidden and uses a static final state for reduced motion; its visible playback controls were removed at the user's request.
- Use clear plot axes, units, legends, and definitions for SOH, RUL, EOL, and prediction intervals.
- Include page title/description, social preview image, favicon, citation, and stable section links.
- Preserve required attribution for reused artwork/templates and verify the intended release terms for downloadable assets.
- Check public resource links before launch; omit unavailable buttons rather than linking placeholders.
- Verify the production build at the intended GitHub Pages base path, including nested assets and downloads.

Suggested future layout, to refine during implementation:

```text
webpage/
  PLAN.md
  src/pages/                 # Astro page entry points
  src/components/            # Layout and interactive figures
  src/content/               # Editable narrative and result metadata
  public/data/               # Small validated browser exports
  public/media/              # Optimized images, diagrams, and videos
  scripts/                   # Scientific data exporters and validation
```

The displayed page contains paper-based prose/Table 1 and the approved real-data overview. Legacy illustrative SVG components may remain in the repository but are unused and deferred. `scripts/export_overview.py` generates the matched inference JSON and both capacity PNG palettes; `scripts/export_training.py` generates the separate training JSON, path/velocity/loss arrays, and training capacity PNGs. Each JSON has an identical public download. `scripts/prepare_paper_schematic.py` prepares the original Figure 1 vector background and layout manifest under `public/figures/`, and can regenerate `capacity-matr1-paper-cool.png` without inference. The `capacity.paperImage`, `paperColormap`, and `paperColormapSource` fields select/document the paper-palette asset while preserving the earlier cividis metadata. The static Astro build consumes these saved assets without Python or browser inference. See [README.md](README.md) for the editing map and local commands, and [OVERVIEW_DATA.md](scripts/OVERVIEW_DATA.md) for regeneration and scientific provenance.

## 9. Working checklist

### Milestone 0 — planning baseline

- [x] P-01: Review the manuscript, representative figures, sampling code, and cached outputs.
- [x] P-02: Compare related research pages, templates, and platform options.
- [x] P-03: Record the user's selection of Astro and the `webpage/` location.
- [x] P-04: Create this plan with requirements and an iterative checklist.

### Milestone 1 — content and data audit

- [x] C-01: Select the camera-ready PDF/source as the authority for current paper prose and Table 1; record detailed transcription checks under P-11/P-12.
- [x] C-02: Produce the original local prose draft. Historical completion only; the full-paper replacement was tracked under P-11/P-12, and current concise copy is tracked under P-20/P-21.
- [ ] C-03: Verify authors, order, affiliations, acknowledgments, contact, and citation.
- [x] C-04: Verify every displayed Table 1 value and metric note against camera-ready Section 3.1. Independent paper/content review passes for all 30 values; see P-12. Broader benchmark explorers are deferred.
- [x] D-01: Document the approved overview selection rule: deliberately curated row 9/draw 5, with cached/fresh error selection and >1000-cycle eligibility recorded. Representative/challenging multi-cell demos are deferred.
- [x] D-02: Verify the overview's data/checkpoint provenance, conditioning, coordinates, normalization, masks, and padding; unknown cell ID/raw measured length are explicit. No broader example export is required now.
- [x] D-03: Verify that displayed Table 1 claims use the camera-ready paper, with exact metric notes and all 30 values independently checked. The curated schematic metrics remain separate. Re-running/reconciling a full benchmark is outside this content task.
- [x] D-04: Export and numerically check the overview JSON, capacity PNGs, source hashes, and provenance note. Broader explorer exports are deferred.
- [x] D-05: Export the approved overview's 101 actual ODE states and fixed-checkpoint training evaluations. Replacing the removed separate generation illustration is deferred.


Exit condition: approved-for-implementation copy and a documented numeric data contract. No unresolved ambiguity in the units or meaning of the plotted values.

### Historical milestone 2 — visual direction and Astro shell

The B/R/O/A/G/S/V records below describe their original revisions, including then-open reviews and controls that have since been retired. They do not require restoring removed figures or superseded UI. Current obligations are P-40–P-47 and the applicable release audit; the approved schematic review closes with T-05.

- [x] B-01: Scaffold Astro inside `webpage/` and record setup/build commands. Astro 7.3.8 is pinned; see `README.md`.
- [x] B-02: Establish draft 03 typography, spacing, navy/black/magenta colors, self-hosted Computer Modern figure fonts, and responsive baseline. Desktop and 390px layouts and font rendering inspected in Firefox; the full Q-03 release audit remains pending.
- [x] B-03: Verify the revised local first-screen preview, introduction, and full-width overview figure. Production build passes, loopback HTTP returns 200, and Firefox desktop/390px title, body, and chart layouts were inspected. All scientific placeholders remain labeled.
- [x] B-04: Verify the revised academic section order, compact implementation resources, visible citation, and contact footer. Built HTML has no unresolved internal anchors or duplicate IDs; the overview has a visually hidden h2 for a consistent heading outline. Resource links and final citation metadata remain pending.
- [ ] B-05: Review draft 03 with the user and record feedback. The requested direction is the OGAS academic structure, academic prose, and navy/black/magenta palette.

Historical draft 03 review checklist (old section order and controls are superseded; unresolved accessibility work rolls into the release audit):

- [x] R-01: Confirm the title, authors, affiliations, conference identification, and resource buttons form the academic opening banner. Verified in source and Firefox.
- [x] R-02: Confirm the introduction and overview figure lead into Background, Method, Prediction examples, and Results. Implemented order checked in source and preview.
- [ ] R-03: Review academic wording and definitions for AI, battery, and industry readers. Draft wording has been revised; final editorial and user review remain pending.
- [x] R-04: Check the consistent reading width, centered headings, white/light-gray section treatment, and figure captions. Firefox desktop and 390px layouts inspected.
- [x] R-05: Check the navy/black/magenta mapping and self-hosted Computer Modern figure labels. Color tokens checked in source; local font rendering verified in Firefox.
- [x] R-06: Confirm Practical use and limitations, Implementation, visible BibTeX, and compact contact complete the page without duplicated team or resource cards. Implemented structure checked in source and preview; desktop citation/footer inspected and Copy BibTeX returned “Citation copied.”
- [ ] R-07: Complete interaction, keyboard, and reduced-motion verification. Generation playback, slider Home/Right keys, the Reference toggle (line and endpoint), and citation copying were verified in Firefox. Full keyboard traversal, reduced-motion emulation, and the broader Q-03 release audit remain pending; scientific audits and release checks are unchanged.

Exit condition: a readable, responsive page with a recognizable FlowBatt identity and substantive draft content.

### Previous iteration — real-data schematic overview

- [x] O-01: Define a matched input/reference/output example and selection rule. MATR-1 test-array row 0 was chosen before inference, with unavailable original identity explicitly left unknown.
- [x] O-02: Export the actual 100 × 100 capacity matrix in Ah with cividis, cycle on x, documented voltage-index orientation, native-resolution PNG, and unchanged source preprocessing.
- [x] O-03: Export ten predictions from the identified pretrained checkpoint and 101 actual ODE output states, recording seed, solver, tolerances, source hashes, and the final-frame/sample correspondence.
- [x] O-04: Verify input/reference correspondence, shapes, finite values, known-prefix preservation within float32 roundoff, downloadable-copy equality, and image resolution. Numerical checks are in `scripts/export_overview.py` and documented in `scripts/OVERVIEW_DATA.md`.
- [x] O-05: Document the preprocessed reference, 10-cycle coordinates, observed prefix, 80% display endpoint, unavailable raw length, and the distinction between output times and solver steps.
- [x] O-06: Review the completed model schematic against the camera-ready architecture: capacity/CNN conditioning, time embedding, four DiT blocks, vector-field interpretation, and initialization from the known SOH prefix. Independent scientific review also verified the data/component mapping, final-frame/sample equality, and reference cutoff at the first 80% crossing.
- [ ] O-07: Verify the revised overview in the production build and desktop/mobile browser; check play/pause/replay, scrubbing, keyboard access, reduced motion, static fallback, and readable axes. Partial: the final production build passes; the user's existing loopback preview returns HTTP 200; Firefox desktop and 390px matrix/architecture/plot/controls were inspected. Playback and slider Home/Right/End were verified at times 0/0.01/1, including the 40–140% initial-state axis. Fresh screenshots verify the final DiT-label/mobile-axis-spacing changes. Static output has valid unique IDs, anchors, and image paths; the built download matches its source and retains final-state/draw-0 equality. Reduced-motion emulation, complete keyboard traversal, and a no-JavaScript browser check remain pending.
- [ ] O-08: Review the overview caption, download, and provenance link, and confirm the separate GenerationPreview/TrajectoryPlot figures remain clearly illustrative. Implementation caption/download/provenance and illustrative labeling have been verified; user review remains pending.

These historical checks applied to the opening overview only. They did not close broader scientific/accessibility or publication audits; the separate explorer work is now deferred.

Historical interaction note for the preceding layout: Replay followed by Pause held the state at actual output time `t=0.10`, with slider index 10 stable and the button returning to “Play generation”. The existing preview was refreshed to `t=1` for handoff. Later composition checks are recorded below; these retired controls are not current requirements.

### Previous iteration — animation inside original Figure 1

- [x] A-01: Preserve the original composition: training across the top, conditioning at lower left, inference at lower right. Derive a vector background from the manuscript artwork and reuse camera-ready label positions with Computer Modern.
- [x] A-02: Preserve original Figure 1 model/curve/frame colors and use its cool capacity colormap, explicitly scoped as an exception to the surrounding site's navy/black/magenta palette. Generate a second PNG from the same exact input; preserve all numeric data and the earlier cividis asset.
- [x] A-03: Animate actual recorded draw-0 states inside the original inference output frame, with a real fixed noise initialization at the input, schematic DiT/loop highlights, optional preprocessed reference, and visible flow time. Keep static training/conditioning context and remove the opening's large ensemble plot; all ten final draws remain in the export.
- [x] A-04: Independently review source for artwork/label alignment, input orientation, t=0 initialization, final-state/draw-0 equality, reference cutoff, full modeled sample horizon, and truthful flow-time/runtime language. No blocking source-review issues found; output rescaling is disclosed and layer highlights are labeled schematic.
- [x] A-05: Pass the final production build and retain matching source/public JSON with unique IDs and final-state/draw-0 equality. Background rendering was compared with the camera-ready artwork. Final static audit verified 31 unique IDs, 12 valid asset/link references, identical JSON copies, 101 recorded states, and exact final-frame equality to draw 0.
- [ ] A-06: Inspect the latest full figure and inference-detail view on desktop and narrow screens; verify play/pause/replay, exact slider stepping, reference visibility, horizontal panning, reduced-motion behavior, keyboard access, and static fallback. Partial: Firefox desktop full/inference-detail and 390 × 844 layouts visually pass. Playback was witnessed near t=0.57/0.59 with the original pink flow path and intermediate state; play/pause works. Home/Right/End verify t=0/0.01/1 and the 40–125% initial / 65–100% final scales. Reference off/on synchronizes line and legend, including restored browser state. Narrow controls fit and horizontal keyboard panning reaches the output without page overflow. Full keyboard traversal, reduced-motion emulation, and a JavaScript-disabled browser check remain unverified release checks. Previous-layout checks above remain historical only.
- [ ] A-07: Review Figure 1 faithfulness and animation pace with the user; retain lower-page illustrative labels and leave broader scientific/publication checklists open. Updated caption, README, and provenance notes are ready for review.

Historical handoff state: both full-figure and inference-detail compositions were visually inspected at phone width; switching views reset horizontal pan. The preview was restored to the desktop full figure at the final sample with the reference enabled.

### Previous iteration — animated training and GIF-paced inference

- [x] G-01: Inspect the current `github/assets/generation.gif` and archived source scripts read-only; record decoded timing, fixed axes, time mapping, and representative frames under `webpage/.qa/generation-gif/`. Current GIF is 2.85 seconds, not the archived 8.55 seconds.
- [x] G-02: Export first-row training data, its real capacity matrix, 101 CondOT path states, checkpoint velocities, target velocity, normalized MSE, source hashes, and units. Verify formula/endpoints, prefix zeros, original inputs, unchanged source hashes, matching public JSON, and alignment with inference times.
- [x] G-03: Integrate animated training and inference inside the whole Figure 1; remove full/detail selectors, distinguish Train/Test matrices, retain original pink/purple/cool palette and Computer Modern labels, and label the training sweep as an objective illustration rather than parameter learning.
- [x] G-04: Use a 2.85-second loop (240 ms first, 99 × `2380/99` ms interior, 230 ms last); fixed SOH axes 80–110%, training/test cycle windows 0–2500/0–2000, and normalized velocity −4…4 across all modeled cycles. Clip the viewing region without clamping data; keep manual stepping and reduced-motion behavior.
- [x] G-05: Verify integrated source, final production build, data/asset consistency, desktop/narrow layouts, loop/replay/pause, slider stepping, and optional reference. Final build and independent scientific review pass. Static audit verifies 36 unique IDs, 14 asset/link references, both source/public/built JSON sets, 101 times aligned within 1e-6, and inference endpoint/draw-0 equality. Timing/geometry checks cover all 101 frame boundaries, 240/230 ms holds, the 2.85-second loop, and unclamped out-of-window coordinates. Firefox desktop/390 × 844 views pass: synchronized panel playback, Home/Right/End at 0/0.01/1, test-only reference toggling, explicit play/pause, mobile panning/controls, and visible keyboard focus. Full reduced-motion emulation, JavaScript-disabled browsing, and complete keyboard traversal remain unverified release checks; previous-revision checks above stay historical.
- [ ] G-06: Review the combined animation with the user. Full accessibility/release audits, broader benchmark reconciliation, lower-page real-data replacement, and publication remain open.

### Previous iteration — automatic and simplified Figure 1

- [x] S-01: Automatically loop training/inference while the figure is visible; pause offscreen/hidden and show a static final state for reduced motion. Remove play/pause buttons, the slider, view selectors, and reference checkbox; use only a quiet informational progress rail.
- [x] S-02: Show one real test capacity matrix. Preserve the separate training input in its export and clearly identify it in the caption. Keep reference curves visible and numerical data unchanged.
- [x] S-03: Remove equations, function notation, the MSE readout, and black connector arrows. Use compact input/output plots, short plain labels, faint pink/purple tracks, moving particles, and soft sequential DiT highlights driven by the shared playback clock; preserve the original three-panel composition/colors.
- [ ] S-04: Verify source/build/data consistency, fixed axes/GIF timing, desktop/mobile legibility, visibility-triggered autoplay, offscreen/background pausing, and reduced-motion behavior. Partial: final production build after the caption update and independent scientific/runtime source review pass; numerical data and GIF timing are unchanged. Firefox desktop confirms automatic repeated looping without input and the requested one-matrix/control-free appearance. The 390 × 844 view has clean type/progress/legend wrapping and keyboard panning reaches output/velocity plots without page overflow. Caption provenance is explicit. The built page has 35 unique IDs and five resolving local assets; both built JSON downloads match their sources. Static checks confirm matching source/public data, one capacity plot, no schematic buttons/inputs, and no black fills/strokes in the background artwork. Reduced-motion/offscreen/background logic is source-reviewed; browser emulation, full keyboard, and JavaScript-disabled checks remain open. Prior revision checks stay historical.
- [ ] S-05: User review of the simplified appearance and motion; broader scientific and release audits remain open.

The progress rail mentioned in S-01 and S-04 is historical and was removed by the equal-grid refinement below.

### Previous iteration — equal plots and aligned model grid

- [x] V-01: Give all six plots equal 16 × 11 dimensions and align their rows/columns; give both DiTs equal dimensions and align their centers with the corresponding plot rows. Static geometry checks and Firefox desktop/390 × 844 inspection pass: all six plots match, both DiTs share `x=108` and size, and the input/output columns align.
- [x] V-02: Strengthen curve, axis, and connector strokes with clear endpoint gaps; retain distinguishable reference/prediction styles and readable labels. Firefox desktop/mobile inspection confirms visibly stronger strokes and clear gaps. Independent source review confirms connectors avoid borders/labels after accounting for packet sizes.
- [x] V-03: Remove the progress bar and retain automatic looping, one capacity matrix, plain labels, and unchanged data/axes/timing. Static checks find no progress-bar markup/selectors; source/public/built JSON match. Automatic animation remains active in browser inspection, and source review found no runtime issues.
- [x] V-04: Verify production build, data/asset consistency, desktop/mobile layout, loop behavior, model/connector alignment, and horizontal panning. Final build passes after all component/assets edits (12:09:49); static audit verifies 35 unique IDs and five valid local assets. Firefox desktop/390 × 844 views pass, including keyboard horizontal panning to the output. The existing user preview at port 4321 serves current code. New reduced-motion/background-lifecycle emulation was not performed and remains part of the broader release audit.
- [ ] V-05: Review the more organized figure with the user; leave broader scientific, accessibility, and publication audits open.

### Approved previous iteration — open sections, bold type, and curated example

- [x] T-01: Remove only the enclosing a/b/c panel borders while preserving aligned model/encoder/embedding geometry. Background-only regeneration and strict XML/manifest comparison pass; removed source paths and original extents are recorded.
- [x] T-02: Review open headings/rules, lowercase schematic labels, black axes, and self-hosted STIX Two Text 700 throughout the schematic. Font source/license records, bold/lowercase inheritance, black axes, and embedded/public WOFF2 consistency pass; Firefox desktop/390 × 844 font/layout inspection passes. Other figures retain Computer Modern.
- [x] T-03: Verify deliberately selected row 9/draw 5, matching input/reference, 101 recorded states, exact final-frame/draw-5 equality, selection metrics/hashes, and identical source/public/built exports. Both first 80% crossings exceed 1000 cycles (reference 1031, prediction 1041); recomputed selected-draw RMSE is 0.406084 percentage points. The built payload uses metadata-driven 0–1200 cycles. Training data, 80–110% SOH, and 2.85-second timing remain unchanged.
- [x] T-04: Complete final production build, asset/data checks, desktop/mobile layout/font inspection, automatic-loop behavior, and horizontal panning. Build passes at 12:24:51; static checks verify 35 unique HTML IDs, resolving anchors and six local assets, six equal plots, matching DiTs, and removed panel paths. Independent source review passes. Firefox desktop/390 × 844 confirms bold open sections without overlap/page overflow, advancing states, and mobile keyboard panning to the 1200-cycle output with a wrapping legend. Existing preview 4321 was restored to desktop. Broader reduced-motion/background-lifecycle, full keyboard, and JavaScript-disabled audits remain open; previous layout checks are historical.
- [x] T-05: User approved the schematic and requested it remain unchanged during the surrounding-content revision. Publication and broader accessibility/scientific audits remain open.

### Historical previous iteration — full paper-based page content

- [x] P-10: Record the approved scope: preserve the schematic; replace surrounding draft prose with supplied/paper content; remove all other displayed figures/demos and defer their restoration.
- [x] P-11: Transcribe the user's TL;DR/lay summary and full camera-ready abstract; add the paper's conclusion, limitations, and outlook. Source locations/editorial decisions are recorded in `scripts/PAPER_CONTENT.md`; independent review confirms the exact paper prose.
- [x] P-12: Add camera-ready Section 3.1 SOH results and semantic Table 1 with six methods/five datasets. Independent review confirms all 30 values and exact metric notes; static audit verifies 30 result cells and five underlined second-best values. Table/caption/notes use STIX Two Text 400 with 700 emphasis, and ± glyphs render correctly.
- [x] P-13: Remove other figure/demo imports and rendered blocks, plus superseded background/method/application placeholder prose. Final output contains exactly one figure (the approved schematic) and one semantic results table.
- [x] P-14: Wire the three exact arXiv/repository/checkpoint URLs in the current page and the paper URL in the citation; remove fake/pending resource copy. Static target checks pass and Copy BibTeX returned “Citation copied.” Broader external-link/publication checks remain in the release audit.
- [x] P-15: Preserve the approved schematic components, assets, data, and timing without edits. Source/public/built training and overview JSON are byte-identical; local asset/provenance/download targets resolve. The schematic font remains STIX 700.
- [x] P-16: Final production build passed at 12:43:11 after all source edits. Static audit verifies 25 unique IDs, resolving anchors, and six existing local HTML assets. Firefox desktop/390 × 844 checks cover banner/TL;DR/lay summary/abstract, desktop conclusions/limitations/outlook, mobile abstract/conclusions without page overflow, and correct table glyphs. Mobile table caption wraps outside its scroller; sticky method cells and panning through MIX-100 work. Citation copying passes; existing preview 4321 was returned to the desktop top. Full keyboard, reduced-motion/lifecycle, JavaScript-disabled, and publication audits remain open.
- [ ] P-17: Review the completed surrounding content with the user; keep publication and broader release checks open.

### Historical previous iteration — concise publication layout

- [x] P-20: Supply the exact seven-word TL;DR, 100-word unheaded overview, brief methodology/results, and concise closing prose. Remove lay summary from current copy; keep historical full exports only for provenance. Table values and complete metric/± notes are unchanged.
- [x] P-21: Retain qualitative conclusions on competitive trajectory-derived RUL and synthetic SOH improving downstream RUL, without numerical gains; preserve uncertainty/input/generalization/physics limitations. Document source selections/abridgments and normalize the BatteryML reference to HTTPS.
- [x] P-22: Apply Source Sans 3 throughout the page, citation, and schematic; use 700px/16px/1.65 body, left 22px h2/18px h3, and justified paragraphs/captions/notes. Static review finds only Source Sans 3 active; Firefox desktop/390 × 844 verifies hierarchy, mathematical glyphs, mobile spacing, and diagram labels without overlap. Navy `#17365D`, black `#111111`, and magenta `#C2188B` remain unchanged.
- [x] P-23: Wire Methodology → Results and discussion → Conclusions and outlook, remove lay summary/Abstract heading and visible local-preview labels, and retain one figure/one table. Final audit confirms 30 result values and zero duplicated numeric mean/SD pairs in prose; desktop TL;DR fits one line.
- [x] P-24: Preserve schematic geometry/data/axes/timing after the shared-font update. Source/public/built training and inference replay JSON are byte-identical; assets/downloads resolve. Browser inspection confirms readable diagram labels, advancing loop, and mobile panning through inference. Static/reduced-motion logic is source-reviewed; lifecycle/reduced-motion emulation remains open.
- [x] P-25: Generate and visually check the local 1200 × 630 social card and conditional metadata. The 13:00:57 subpath build in `.astro/qa-subpath` used reserved test-only `https://flowbatt.example` with `/FlowBatt/`: all seven HTML assets and three CSS font paths resolve, canonical/social URLs are correct, and noindex is absent only with configured production site. Default-local output retains noindex and no invented canonical; ScholarlyArticle metadata has six authors. This is preparation/testing only, not deployment.
- [x] P-26: Final root production build passes at 13:03:46. Static audit verifies 24 unique IDs, one figure/table, all anchors/assets, and unchanged scientific exports. Firefox desktop/390 × 844 confirms compact headings/prose, table ±/bold/underlines, sticky method labels while panning through MIX-100, schematic panning, citation wrapping and “Citation copied”, mobile outlook, and the 390px header's 2 × 2 resource buttons. The browser was returned to the desktop top. Existing preview 4321 returns HTTP 200 and was reused; the temporary owned 4323 QA server is stopped. Full keyboard, JavaScript-disabled, and browser-emulated reduced-motion/lifecycle audits remain open.
- [ ] P-27: Review the concise publication layout with the user. Broader accessibility/lifecycle/publication audits and deployment remain open.

### Historical previous iteration — original TL;DR, compact table, and acknowledgment footer

- [x] P-30: Restore `tldr` exactly to `screenshotTldr`, including punctuation. The 17-word original sentence is verified identical; every other concise-copy export and all table values/notes/references remain unchanged.
- [x] P-31: Add the complete accepted camera-ready acknowledgment in justified 13px footer text after the email and university logos. Source and generated HTML match line 415 after TeX conversion: 79 words, preserving CircularLIB, donor/program spelling, `MWK | ZN3678`, and `DS³`. Desktop/mobile footer placement and readability pass.
- [x] P-32: Remove the visible schematic caption, separate timing note, and table metric-note list at the user's request. Generated HTML/browser checks confirm their absence; full source/provenance/JSON and the complete table caption/notes export remain intact.
- [x] P-33: Fit the table to the 700px reading width and set the original TL;DR to 14px within the 1050px hero. Firefox verifies one desktop line and three natural mobile lines, all five table columns fitting desktop, mobile keyboard panning through MIX-20/MIX-100 with fixed method labels, and readable footer text.
- [x] P-34: Complete official-guidance research and add intact proportional official TU Braunschweig/TU Clausthal logos for author affiliations. Asset hashes match their sources; desktop row/mobile stack display correctly. Record provenance and the affiliation-use interpretation in `public/logos/README.md`; keep NeurIPS as ordinary text because permission remains unresolved in `public/logos/NEURIPS-SOURCE.md`. No individualized approval or blanket license is claimed.
- [x] P-35: Preserve other paper copy, all 30 table values/five second-best marks, model geometry/data/timing, Source Sans 3, and exact navy/black/magenta tokens. Source/public/built replay JSON are byte-identical; the automatic schematic still visibly advances. The table's complete caption/notes remain unchanged in source.
- [x] P-36: Final default build passes at 13:21:10 after the acknowledgment justification fix. Reserved-origin `/FlowBatt/` build passes at 13:20:57, verifying seven HTML assets (including logos), three CSS fonts, canonical/social paths, and conditional noindex; default local output is restored. Independent HTML audit verifies 23 unique IDs, resolving anchors/ARIA references, exact TL;DR/acknowledgment, one figure/no figcaption, and all local assets. Firefox desktop/390 × 844 inspection passes for the changed header/table/footer/logos and continued animation; browser returned to desktop footer. Citation copying is unchanged and retains its prior successful verification, not a new click this iteration. Full keyboard, reduced-motion/lifecycle, JavaScript-disabled, actual-origin, and publication audits remain open.
- [ ] P-37: Review the restored TL;DR and compact/footer presentation with the user. Broader accessibility, lifecycle, actual-origin release checks, and deployment remain open.

### Current iteration — RUL figure and compact presentation

- [x] P-40: Remove the visible schematic toolbar/header and automatic-loop label while preserving all recorded data, geometry, axes, 2.85-second timing, and automatic/reduced-motion behavior. Firefox confirms the toolbar/label is absent and the automatic loop still visibly advances.
- [x] P-41: Move the exact original 14px TL;DR into the 700px reading column, with two desktop lines and natural mobile wrapping verified in Firefox. Its wording, size, and body/table widths remain unchanged.
- [x] P-42: Reduce TU Braunschweig/TU Clausthal display widths to 118.8px/138px (60%); keep original SVG bytes, colors, aspect ratios, email/logo/acknowledgment order, and exact 13px acknowledgment unchanged. Desktop/mobile inspection confirms the smaller marks display correctly.
- [x] P-43: Remove the displayed Limitations heading/paragraph at the user’s request; retain `closingLimitations`, original accepted limitations, and scientific provenance without recasting the evidence as calibrated or broadly generalizable. Source retention and browser absence are confirmed.
- [x] P-44: Add an approximately 80-word paper-grounded RUL discussion and all five paper Figure 4 panels. Source/export paths are recorded in `scripts/RUL_PLOTS.md`: all 388 marker centers/color bins, five original panel hashes, axes/ticks/clip/identity lines, and separate scales pass independent asset review. Preserve these values/order and restyle with Source Sans 3/navy-magenta. Smaller marker styling and the retained clipped MATR-2 point are explicit; raw sigma/aggregation are unavailable and must not be invented. Independent scientific/source checks pass; desktop/900px/390px browser integration passes.
- [x] P-45: Arrange RUL panels in three columns above 1050px with the second row centered, two columns from 681–1050px, and one column at 680px and below; cap panel width at 360px. Firefox desktop/900px/390px inspection confirms the 3+2/two-column/single-column layouts and readable axes, colorbars, and text. The browser is returned to the desktop RUL section.
- [x] P-46: Final production build passes at 13:37. Scientific asset review and static integration pass: two figures, six SVG image roles, all 30 SOH result cells, unique IDs/resolving ARIA/internal references, and existing assets. Requested toolbar/Limitations labels are absent, exact TL;DR text remains 14px, and logo widths are 118.8px/138px. Public/built training, inference, and RUL JSON are byte-identical. Firefox desktop/900px/390px verifies changed layouts, readable RUL axes/colorbars/text, smaller logos, TL;DR wrapping, and continued automatic motion; browser returned to desktop RUL. Unchanged citation/subpath behavior retains prior verification rather than an unnecessary retest. Broader release/accessibility audits remain open.
- [ ] P-47: Review the new RUL section and compact presentation with the user. Broader accessibility/lifecycle/release audits and actual deployment remain open.

### Deferred former milestone 3 — separate explorers

These are retained as backlog records at the user's direction, not first-release requirements. Do not restore removed figures merely to close these checkboxes.

- [ ] I-01: Deferred dataset/cell selection and synchronized metadata.
- [ ] I-02: Deferred trajectory, median, interval, and reference visibility controls.
- [ ] I-03: Deferred EOL threshold exploration, reset, and non-crossing behavior.
- [ ] I-04: Deferred separate generation playback/scrubbing; the approved schematic remains automatic and control-free.
- [ ] I-05: Audit accessibility/static fallback if a future explorer is approved; current schematic/page accessibility remains in Q-03.
- [ ] I-06: Scientifically review any future demo before adding it; no additional demo is required in this iteration.

### Milestone 4 — verification and publication preparation

- [ ] Q-01: Compare exported references, trajectories, intervals, and threshold summaries with their Python sources; exercise boundary/non-crossing cases.
- [ ] Q-02: Review claims, units, benchmark comparisons, and error-bar definitions against the final paper.
- [ ] Q-03: Inspect desktop and mobile layouts; verify keyboard navigation, contrast, and reduced motion.
- [ ] Q-04: Check loading behavior and payload sizes on a throttled connection; optimize observed bottlenecks.
- [ ] Q-05: Run the production build and verify the intended deployment base path, media, downloads, and internal links.
- [ ] Q-06: Verify public paper/code/model/contact links, attribution, and downloadable artifact versions.
- [ ] Q-07: Prepare social metadata, favicon, preview image, and citation copy/download.
- [ ] L-01: Record hosting account/repository, domain choice, and deployment workflow.
- [ ] L-02: Present a concrete local preview for final content/design review; record requested changes.
- [ ] L-03: When publication is requested, deploy and verify the public URL and interactive figures.
- [ ] L-04: Record the release URL, source revision, data-manifest version, and maintenance instructions.

Exit condition, when publication is requested: a verified public project page with traceable paper claims, the approved schematic, functioning links, and a documented update process.

### Deferred backlog — revisit only when requested

- [ ] F-01: Add capacity-matrix and encoder-analysis interactions.
- [ ] F-02: Add benchmark filters and downloadable result tables.
- [ ] F-03: Add synthesis examples with downstream experiment context.
- [ ] F-04: Evaluate live inference hosting and add a companion demo if useful.
- [ ] F-05: Add a worked input-data preparation example for external collaborators.
- [ ] F-06: Add talk/poster/video materials when available.

## 10. Iteration process and unresolved choices

For each iteration, choose a small set of checklist IDs, implement them, verify their acceptance conditions, and record the outcome below. Mark partially completed items as unchecked with a short note. Add new requirements to this file when feedback changes the scope.

| Choice | Current working default | When to revisit |
| --- | --- | --- |
| Template versus custom layout | Custom Astro layout using OGAS as the academic structure reference | Draft 03 review |
| Visual palette and opening layout | Navy/black/magenta; original 14px TL;DR joins the 700px body/table column; centered academic hero retained | Two desktop TL;DR lines/mobile wrapping verified; user review open |
| Figure 1 palette and composition | Approved colors/geometry/data/timing, open sections, black axes, aligned plots/models, one curated matrix; shared Source Sans 3 text | Font/layout verified; scientific content preserved |
| Animation pace | Approved automatic 2.85-second Figure 1 loop; no other displayed demos | Preserve unchanged |
| Number of displayed figures | Approved schematic plus requested five-panel RUL figure; Table 1 is HTML | Other figures/explorers remain deferred |
| Public origin/base path | Supply actual `FLOWBATT_SITE_URL` and optional `FLOWBATT_BASE_PATH`; no assumed URL | Before an explicitly authorized deployment |
| Contact/footer | Email, official university logos at 118.8px/138px, then exact camera-ready acknowledgment in justified 13px text | Smaller-logo desktop/mobile display verified; source/content unchanged |
| Institutional logos | Intact official TU Braunschweig/TU Clausthal marks; NeurIPS stays ordinary venue text | Source/usage records in `public/logos/`; source hashes and rendered layout verified |
| Live inference | Deferred | Only if explicitly prioritized later |

| Date | Iteration / checklist IDs | Historical outcome or current next action |
| --- | --- | --- |
| 2026-10-14 | Planning / P-01–P-04 | Astro selected and local plan created. |
| 2026-10-14 | Placeholder draft / C-02, B-01–B-04 | Local draft, illustrative plots, controls, authors, and citation added. Build/HTTP/Safari desktop checks passed; real data and publication links were then pending. |
| 2026-10-14 | Academic banner / B-02–B-05 | Centered full-title banner, author/affiliation details, resource buttons, and paper palette introduced. Build and Safari desktop inspection passed. |
| 2026-11-21 | Academic structure / B/R series | OGAS-inspired section structure, navy/black/magenta, Computer Modern, resource/citation/footer layout added. Build, IDs/anchors, Firefox desktop/390px layouts, then-present controls and citation copying passed. |
| 2026-11-21 | Real-data overview / O series | Former row 0/draw 0, actual 100 × 100 ΔQ matrix, ten CPU predictions, 101 ODE states, hashes and reference cutoff exported. Numeric/independent scientific/build checks and desktop/mobile playback/keyboard inspection passed. |
| 2026-11-21 | Original Figure 1 / A series | Original model artwork/palette with real matrix and ODE curve integrated. Source/artwork/data/build checks and desktop/mobile full/detail, panning, and then-present controls passed. |
| 2026-11-21 | Training and GIF timing / G series | Fixed-checkpoint CondOT training sweep added; 101-frame training/inference alignment, objective/prefix/endpoints, and all timing boundaries verified. Build and synchronized desktop/mobile interaction checks passed. |
| 2026-11-21 | Automatic presentation / S series | One matrix, automatic motion, no visible equations/MSE/controls/black arrows. Build, numeric/runtime source review, desktop repeated looping, mobile panning/layout passed. Lifecycle/reduced-motion logic was source-reviewed, not browser-emulated. |
| 2026-11-22 | Equal grid / V series | Six 16 × 11 plots, equal aligned DiTs, stronger strokes/gaps, no progress bar. Build at 12:09:49, geometry/data/source review and desktop/mobile checks passed. |
| 2026-11-22 | Approved open sections/STIX/example / T series | Open headings/rules, bold lowercase STIX and black axes, curated row 9/draw 5 (>1000-cycle reference/prediction crossings), 0–1200 inference view. Final build at 12:24:51, data/static/scientific and Firefox desktop/390px font/layout/automatic-loop/panning checks passed. The user subsequently approved the schematic. Broader accessibility/lifecycle audits remain open. |
| 2026-11-22 | Paper-based surrounding content / P-10–P-17 | Preserve approved schematic; replace other prose with screenshot TL;DR/lay summary, full camera-ready abstract, Section 3.1/Table 1 and paper closing paragraphs. Use real arXiv/code/checkpoint URLs; remove other displayed figures/demos and defer restoration. Final build at 12:43:11, independent exact-prose/30-value review, static IDs/assets/table/resource checks, and Firefox desktop/390px content/table/citation checks pass. Schematic components/assets/data/timing remain unchanged; new STIX 400 fixes table ± rendering. User content review and broader release audits remain open. |
| 2026-11-22 | Concise publication layout / P-20–P-27 | Short TL;DR, 100-word unheaded overview, brief method/results/closing prose, unchanged table notes/values, and retained qualitative RUL/synthesis conclusions. Source Sans 3 becomes the sole family, including citation/diagram; apply 700px/16px/1.65 body, left headings, justified text. Preserve schematic geometry/data/timing. Prepare conditional real-origin metadata and local social card; remove visible local labels while retaining local noindex. Final root build 13:03:46 and reserved-origin/subpath build 13:00:57 pass; source/static/data checks and Firefox desktop/390px typography, diagram/table panning, glyphs, citation, and loop inspection pass. Social card verified; local noindex retained, conditional metadata/paths checked, no invented public URL. User review and broader accessibility/release audits remain open; not deployed. |
| 2026-11-22 | Original TL;DR/table/footer refinement / P-30–P-37 | Original 14px TL;DR fits one desktop line in a 1050px hero; table matches 700px prose. Visible schematic/timing/table-note text removed while provenance remains. Footer has email, intact official TU Braunschweig/TU Clausthal logos, then exact 79-word acknowledgment at justified 13px. NeurIPS stays text after policy review. Default build 13:21:10 and reserved-origin/subpath build 13:20:57 pass; independent exact-copy/30-value/23-ID/ARIA/asset/JSON checks and Firefox desktop/390px layout, table panning, logos, and continued animation pass. Citation copying retains prior verification; browser returned to desktop footer. P-37 user review and broader release/accessibility audits remain open. No deployment. |

| 2026-11-22 | RUL figure and compact presentation / P-40–P-47 | Add brief paper-grounded RUL discussion and all five Figure 4 panels with original geometry/separate uncertainty scales and Source Sans 3/navy-magenta styling. Remove schematic toolbar/header/loop label while preserving animation; move original 14px TL;DR into 700px column; reduce logo widths to 60%; remove displayed Limitations section while retaining source. Target RUL grid 3+2 desktop, two columns medium, one mobile. Final build 13:37, independent scientific asset review, static integration (two figures, all 30 SOH values, unique/resolving references, matching public/built JSON), and Firefox desktop/900px/390px layout/legibility/continued-motion checks pass. Browser returned to desktop RUL; user review and broader release audits remain open. No deployment. |

## 11. Reference links

Platform and tooling references reviewed during initial research:

- [Astro islands architecture](https://docs.astro.build/en/concepts/islands/) and [GitHub Pages deployment](https://docs.astro.build/en/guides/deploy/github/).
- [AstroWind](https://github.com/arthelokyo/astrowind), an optional source of layout components.
- [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template), a reference for paper resources and citation presentation.
- [D3](https://d3js.org/), [Motion](https://motion.dev/docs/quick-start), and [Plotly.js](https://plotly.com/javascript/) as an alternative charting option.
- [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces-overview) and [embedding a Space](https://huggingface.co/docs/hub/spaces-embed) for a potential later live demo.

Scientific and presentation references:

- [OGAS project page](https://melissa-sa.github.io/ogas/): user-selected structural reference for draft 03, including the academic title banner, figure-led narrative, and compact implementation/citation ending.
- [BatteryML](https://github.com/microsoft/BatteryML): dataset and benchmark transparency.
- [BatLiNet](https://www.nature.com/articles/s42256-024-00972-x): scientific comparison and evaluation context.
- [DiffBatt](https://github.com/HamidrezaEiv/DiffBatt): related generative battery modeling work.
- [DiT project page](https://www.wpeebles.com/DiT): readable technical narrative with visual evidence.
- [Diffusion Explainer](https://poloclub.github.io/diffusion-explainer/): interactive explanation using preset examples.
- [Nerfies](https://nerfies.github.io/): concise introduction, demonstrations, and resource links.

Verify dependency versions and hosting capabilities again when implementing or publishing; this plan does not pin software versions or assume a live-inference pricing tier.
