<!-- Historical local development notes, preserved before GitHub Pages setup. -->

# FlowBatt webpage — local academic project page

A static Astro project page with concise paper-based content, the approved animated FlowBatt schematic, and the newly requested RUL-prediction figure from paper Figure 4. The current refinement restores the exact original screenshot TL;DR and retains the 100-word introduction without an Abstract heading and three main sections: Methodology, Results and discussion, and Conclusions and outlook. The lay summary is removed. Table 1 values remain unchanged; its complete metric/± notes are retained in source/provenance while the visible note list is removed. The schematic caption and separate timing note are also removed from the page at the user's request. Per-dataset numbers are not repeated in the prose. Qualitative RUL and synthesis conclusions are retained. The displayed Limitations heading/paragraph is removed at the user’s request; its exact source export and scientific caveats remain in provenance. The footer places the contact email first, intact official university logos second, and the exact camera-ready acknowledgment in justified 13px text third.

Source Sans 3 is the single typeface, including the diagram and citation. The approved schematic's geometry, data, colors, fixed axes, and 2.85-second loop remain intact. It uses deliberately selected MATR-1 row 9/draw 5 over 0–1200 cycles; this curated example is not an aggregate performance estimate. The current RUL/presentation iteration passes scientific asset review, production build, static integration, and desktop/900px/390px browser checks; prior iteration records below remain historical. User review and broader release audits remain open. This is publication preparation only: the page has not been deployed.

## Run locally

Use a supported even-numbered Node.js release, version 22.12.0 or newer (the draft was built with Node 26 and Astro 7.3.8).

```bash
cd webpage
npm ci
npm run dev
```

Open the local URL printed by Astro, normally `http://127.0.0.1:4321/`.

```bash
npm run build      # Generate the static site in dist/
npm run preview    # Preview that production build locally
npm run dev:status # Check the Astro 7 background dev server
npm run dev:stop   # Stop that dev server
```

The dev server binds to loopback only. No hosting account, public deployment, or live-inference service is configured.

If npm reports `UNABLE_TO_GET_ISSUER_CERT_LOCALLY` on this Mac, use the existing system CA bundle for that install command: `NODE_EXTRA_CA_CERTS=/etc/ssl/cert.pem npm ci`. This resolved the local installation issue while retaining TLS verification.

## What to review

- The original TL;DR: “We introduce FlowBatt, a use-inspired conditional generative framework that adapts flow matching to probabilistic battery degradation modeling.” Its unchanged 14px text now belongs to the 700px reading column, with two desktop lines and natural mobile wrapping verified in Firefox.
- The unheaded 100-word introduction, brief methodology, compact protocol/findings, and closing conclusion/outlook; no visible lay summary, long abstract block, or Limitations section. The limitations source remains intact.
- The 700px reading column, 16px body text at 1.65 line height, left-aligned 22px h2/18px h3 headings, and justified paragraphs/captions/notes.
- Source Sans 3 throughout the page, table, citation, and diagram, with legible mathematical symbols.
- The approved schematic's unchanged geometry/data/timing, with its visible toolbar/header, automatic-loop label, caption, and separate timing note removed while animation, provenance, and JSON remain intact.
- Table 1's six methods × five datasets, exact values, 700px width matching the body column, mobile panning, and best/second-best styles. Full metric/± notes remain in source/provenance rather than a visible list.
- The new RUL-prediction subsection: approximately 80 paper-grounded words and all five Figure 4 scatter panels, with exact original point/axis geometry, Source Sans 3 labels, navy/magenta styling, and each panel’s original separate uncertainty scale. Layout: three columns above 1050px (centered second row of two), two columns from 681–1050px, and one column at 680px and below; each panel is at most 360px wide.
- The footer sequence: email, official TU Braunschweig/TU Clausthal logos, then the complete acknowledgment in justified 13px text. Logo display widths become 118.8px/138px (60% of the prior widths); source SVGs remain intact and proportional; NeurIPS stays ordinary venue text. Review publication metadata, social preview, citation copying, and desktop/mobile overflow before release.

## Content sources and scope

| Content | Authoritative source and editable record |
| --- | --- |
| TL;DR | Original screenshot sentence, exactly restored in `tldr` and identical to `screenshotTldr` |
| Concise overview/methodology | Camera-ready abstract/introduction/method passages, selected and abridged with source locations in `scripts/PAPER_CONTENT.md` |
| SOH results and Table 1 | Brief protocol/findings and unchanged values; full published caption/metric notes remain in source/provenance while the visible note list is removed |
| RUL results and figure | Approximately 80 words grounded in the paper’s RUL section and all five original Figure 4 panels; preserve exact geometry and separate uncertainty scales while restyling fonts/colors |
| Conclusion and outlook | Concise paper-based passages retaining competitive trajectory-derived RUL, synthesis benefits, and future work; the unrendered limitations export retains undercoverage/input/generalization/physics caveats |
| Acknowledgments | Complete accepted camera-ready paragraph at line 415, exported as `acknowledgments`, with `MWK \| ZN3678`, `DS³`, and exact donor/program spelling |
| Text/table provenance | `scripts/PAPER_CONTENT.md`, including source locations and editorial/transcription decisions |
| Schematic data and interpretation | Existing JSON exports and `scripts/OVERVIEW_DATA.md`; geometry, data, and timing unchanged; typography follows the new common family |

Use the published table for paper claims. The schematic's selected one-cell metrics and the separate cached evaluation summary are not substitutes for Table 1. Keep the table as semantic HTML, not a figure image. Preserve the exact uncertainty/aggregation definitions in `sohTable.notes` and `scripts/PAPER_CONTENT.md` even though the note list is not rendered. The underlying scientific data and definitions are unchanged.

Resource targets are [the paper](https://arxiv.org/abs/2611.03150), [the FlowBatt repository](https://github.com/HamidrezaEiv/FlowBatt), and [pretrained checkpoints](https://github.com/HamidrezaEiv/FlowBatt/tree/main/checkpoints). The citation links to the paper rather than a placeholder. The existing resource targets and copy handler are unchanged; citation copying was verified in the previous iteration. Public reachability and final author/publication metadata remain release-audit items, not “pending release” copy on the page.

`GenerationPreview.astro` and `TrajectoryPlot.astro` are legacy illustrative components if retained in the repository; they are not displayed. Separate trajectory/generation explorers, additional benchmark charts, capacity/XAI views, and synthesis additions remain deferred. The current authorized figures are the approved overview and the requested five-panel RUL figure; this does not reopen other deferred demos. The site remains local; local/development builds retain indexing restrictions even though visible local-preview labels are removed.

## Paper RUL figure

The RUL section uses the five original Figure 4 panels in paper order: MATR-1, MATR-2, HUST, MIX-100, MIX-20. The export preserves all 388 PDF marker centers and original color-bin assignments, each panel’s axes, clipping, identity line, and separate colorbar labels. It restyles live text in Source Sans 3 and maps the same color bins from navy to magenta; it does not substitute cached predictions or rerun inference. The color scales differ by dataset and cannot be read as one common absolute scale.

The source PDF does not expose exact per-cell standard deviations, the underlying ten scalar predictions, or whether the plotted prediction is a mean, median, or individual draw. The page therefore says “predicted RUL” and makes no invented aggregation/precision claim. One original MATR-2 point has its center above the published upper limit; it remains in the export and clipped. Smaller webpage markers hide the tiny cap visible with the paper’s larger marker. [RUL provenance](scripts/RUL_PLOTS.md) and [the extracted coordinate record](public/data/rul-paper-scatter.json) document these limits. Independent asset/source geometry checks and final desktop/900px/390px browser integration pass.

## Publication preparation

The implementation uses `FLOWBATT_SITE_URL` for the actual future public origin and `FLOWBATT_BASE_PATH` for an optional repository/subdirectory path (default `/`). Do not guess or embed a publication URL. Production canonical and absolute Open Graph/social-image URLs are conditional on the supplied real origin; local builds without it have no canonical/public URL claim and retain `noindex, nofollow`. Development previews remain unindexed. Ordinary title/description metadata may exist locally without implying publication.

The local 1200 × 630 social preview card at `public/social-card.png` was generated reproducibly and visually checked; configured production metadata resolves it through the base path. The favicon, resource links, and citation remain local build assets/content. No hosting account, upload, domain configuration, or deployment is performed by this iteration. Both default-local and configured-production/subpath builds have been checked. Repeat the deployment-specific check when the actual public origin/path is chosen; no public origin has been assumed.

## Verification status

**Current RUL/presentation iteration:** the final production build passes at **13:37**. Independent scientific review verifies all five original panel hashes, identical published composite, all 388 marker centers/color bins, original axes/ticks/clipping/identity lines, and separate uncertainty scales. The static page audit confirms two figures, six SVGs with image roles, all 30 SOH result cells, unique IDs, resolving ARIA/internal links, and existing local assets. Toolbar/automatic-loop and Limitations labels are absent; the original TL;DR sentence and 14px size are unchanged; logo widths are 118.8px/138px. Public/built training, inference, and RUL JSON are byte-identical.

Firefox desktop, 900px, and 390px inspection verifies the RUL grid at 3+2, two columns, and one column, with readable axes, colorbars, and text. The original TL;DR wraps to two desktop lines in the 700px reading column and naturally on mobile. Smaller logos display correctly on desktop/mobile; the schematic loop still visibly advances without its removed toolbar. The Limitations section is absent while its source is retained. The browser was returned to the desktop RUL section. Unchanged citation copying and reserved-origin/subpath behavior retain earlier checks; they were not rerun without a new concern. P-40–P-46 pass; P-47 user review and broader accessibility/release audits remain open. No deployment occurred.

**Historical TL;DR/table/footer refinement:** the final default build passes at **13:21:10**, after the last acknowledgment-justification change. Independent generated-HTML checks confirm the exact original 17-word TL;DR and 79-word accepted acknowledgment, all 30 table values and five second-best marks, 23 unique IDs, resolving anchors/ARIA references, one figure, no figcaption, and no visible timing/table-note list. All seven local HTML assets resolve; both university logos match their official-source hashes. Source/public/built training and inference replay JSON are byte-identical. Other copy, table values/full notes, references, and schematic geometry/timing are unchanged.

The reserved-origin/subpath build passes at **13:20:57** with the test-only origin `https://flowbatt.example` and `/FlowBatt/`: all seven HTML asset paths, including both logos, and three CSS font paths resolve; canonical/social URLs are correct and production noindex is absent only when a site is configured. The default local build was restored and retains noindex without an invented public origin.

Firefox desktop and 390 × 844 inspection verifies the 14px original TL;DR on one desktop line and three natural mobile lines; the 700px table aligns with prose and fits all five desktop columns. Mobile keyboard panning reaches MIX-20/MIX-100 while method labels stay fixed. The automatic schematic still advances; removed visible notes remain absent. Official logos display intact in a desktop row and mobile stack; the exact acknowledgment is readable and justified at 13px after the email/logos. The browser was returned to the desktop footer. Citation copying is unchanged and was verified in the preceding iteration, not newly clicked here. P-30–P-36 pass; P-37 user review and broader release/accessibility checks remain open.

Logo provenance and usage interpretation are recorded in [the university-logo source record](public/logos/README.md). The page uses the intact official TU Braunschweig and TU Clausthal marks for author affiliations; this records institutional guidance, not individualized approval or a general third-party license. NeurIPS remains ordinary venue text because the reviewed policy/media kit did not resolve permission for this page; see [the source review](public/logos/NEURIPS-SOURCE.md). No deployment or external publishing occurred.

**Historical concise/Source Sans 3/publication-layout revision:** the final root production build passed at **13:03:46**. Source/static review confirms the 100-word overview, compact paper-based prose, unchanged 30 Table 1 values and complete notes, restored qualitative RUL/synthesis conclusions, no duplicated numeric mean/SD pairs in prose, 24 unique IDs, one figure, one table, resolving anchors/assets, and Source Sans 3 as the only active CSS font family. Source/public/built training and inference replay JSON are byte-identical. Local output retains noindex without an invented canonical URL; valid ScholarlyArticle metadata lists all six authors.

A separate subpath build passed at **13:00:57** in `.astro/qa-subpath`, using reserved test-only origin `https://flowbatt.example` and `/FlowBatt/`. All seven HTML asset paths and three CSS font paths resolve; canonical/social URLs use the test origin and path correctly. Noindex is absent only for the configured production-site build. This is a local configuration test, not a published site or proposed public URL.

Firefox desktop and 390 × 844 inspection verifies the narrow justified text, smaller left-aligned headings, desktop single-line TL;DR, Source Sans 3 diagram labels without overlap, table ±/bold/underlines, mobile table panning through MIX-100 with fixed method labels, and mobile schematic panning through inference. The 390px header resource buttons form a verified 2 × 2 layout. Citation wrapping/copying and mobile outlook pass; “Citation copied” appears after copying. The schematic loop visibly advances. The social card was visually checked at 1200 × 630. Source review confirms static/reduced-motion logic, but reduced-motion/lifecycle behavior was not browser-emulated. Full keyboard and JavaScript-disabled audits remain open.

The browser was returned to the desktop top. The existing loopback preview at port 4321 was reused and returns HTTP 200; the temporary owned QA server at 4323 is stopped. No external publishing occurred. P-22–P-26 passed for that prior revision. Current final appearance review is tracked by P-47 in [PLAN.md](PLAN.md).

**Historical full-text content revision:** final build at 12:43:11, independent exact-prose/all-30-value review, and static IDs/anchors/assets/table/resource checks passed. Firefox desktop and 390 × 844 inspection verified the then-present lay summary/full abstract, concluding sections, STIX table ± glyphs, wrapping caption, sticky method column/panning through MIX-100, no page overflow, and successful BibTeX copying. The schematic and data were unchanged in that earlier iteration. Its 25-ID/six-asset counts and STIX typography are historical, not current-layout assertions.

**Historical schematic verification, preserved without rerunning inference:**

| Revision | Completed evidence |
| --- | --- |
| Academic shell and illustrative draft | Production build, loopback HTTP, desktop/390px layouts, font rendering, then-present controls, citation copying, IDs, and anchors checked |
| First real-data overview | Matching input/reference, real 101-state ODE export, ten samples, prefix/endpoint checks, independent scientific review, build and desktop/mobile control checks passed for former row 0/draw 0 |
| Original Figure 1 integration | Original artwork mapping, recorded states, reference cutoff, full/detail layouts, panning, and then-present controls reviewed |
| Training plus inference | 101 CondOT evaluations and real ODE frames, source hashes, normalized objective, timing boundaries, endpoint equality, synchronized desktop/mobile playback verified |
| Automatic/equal-grid presentation | One displayed test matrix, no equations or controls, six equal plots, aligned DiTs, stronger strokes/gaps, no progress bar, automatic loop and keyboard panning verified |
| Approved open-panel/STIX/curated example | Final build at 12:24:51, source/data checks, Firefox desktop and 390 × 844 views passed. Row 9/draw 5, identical source/public/built JSON, exact final-frame correspondence, EOL 1031/1041, RMSE 0.406084 percentage points, and the 1200-cycle view were independently verified |

The user approved the schematic content and layout; preserve its geometry, data, and timing while applying the new shared font family. Broader reduced-motion/background-lifecycle emulation, complete keyboard traversal, JavaScript-disabled browsing, deployment/base-path checks, and publication remain open. Detailed historical records and the current checklist are in [PLAN.md](PLAN.md).

## Real-data schematic overview

The Figure 1 arrangement remains: training above, conditioning at lower left, inference at lower right. Enclosing panel boxes are replaced by bold navy a/b/c headings, short magenta rules, and one subtle horizontal divider. All visible schematic labels remain lowercase and bold, now using the shared Source Sans 3 family; axes are black. Training and inference start automatically while visible and share the same playback clock. Soft DiT highlights and pink/purple particles replace black arrows. The current layout specification uses six **16 × 11** plot frames in SVG coordinates, with top-row plots at `y=14` and bottom-row plots at `y=52.5`. The state/input column starts at `x=80`, and the velocity/output column at `x=150`. Both DiTs start at `x=108`, measure **26.886335 × 13.396257**, and center vertically at `y=19.5` and `y=58`, matching their plot rows. Curves, axes, and connectors gain stronger strokes with clear gaps at connected elements. The progress bar is removed. Labels use words, and equations/MSE/play/slider/reference controls remain absent. Motion pauses offscreen or when the document is hidden. Reduced-motion mode displays the final state without automatic motion. Narrow screens can pan across the diagram.

**Training** uses the first MATR-1 training row, selected before checkpoint evaluation, and its actual capacity matrix. At a fixed pretrained checkpoint, the animation sweeps the conditional flow-matching path `x_t = (1−t)x_0 + t x_1`, compares predicted velocity with `u = x_1−x_0`, with mean squared velocity error across all 256 normalized coordinates retained in the download. The numerical loss and equations are not shown in the schematic. These are 101 evaluated path positions, **not optimizer history, parameter updates, or inference ODE states**. Loss need not decrease along this sweep. The first ten SOH coordinates are fixed; their target and predicted velocities are zero.

**Inference** uses MATR-1 test row 9 (“test cell 10”) and draw 5, the sixth of ten fresh seed-2026 predictions. Excluding the former row 0, five cached cells have a reference 80% crossing after cycle 1000; this cell has the lowest mean per-draw forecast RMSE among them. The displayed draw has the lowest fresh forecast RMSE among draws whose own crossing also exceeds 1000 cycles. This is a deliberately good example, not an unbiased sample or benchmark result. Its 101 actual dopri5 states end exactly at `trajectories.samples[5]`; all ten final samples and selection metrics remain downloadable. The reference stays visible, is preprocessed, and ends at its first 80% crossing. Original cell IDs and raw measured lengths are unavailable. Only the **test example's capacity matrix** is displayed. The training example was evaluated with its own separate input, retained in its export and documented in provenance; the single displayed matrix is not its conditioning data. Both exported matrices preserve all 100 × 100 input samples. The visible matrix uses the original cool colormap with cycle number horizontally. “voltage grid” avoids claiming absent physical voltage bounds; units and ranges are in the downloads.

Axes stay fixed, following the GIF's denoising presentation: **80–110% SOH** for state plots, **0–2500 cycles** for training and **0–1200 cycles** for inference; the reference and selected prediction first reach 80% at cycles 1031 and 1041 respectively. The normalized training-velocity plot uses **−4 to 4** over the complete modeled horizon, cycles 1–2551. SVG windows hide out-of-range values without clamping or changing numerical data; early noise extends outside the SOH window. These display limits replace the preceding frame-by-frame rescaling.

The current [generation GIF](../github/assets/generation.gif) has 121 frames and a **2.85-second loop**: 240 ms initially, 119 interior frames at 20 ms, and 230 ms at the end. The website automatically preserves that loop duration with its 101 real frames: 240 ms first, 99 interior holds of `2380/99` ms, and 230 ms last. Playback speed does not measure inference or training runtime. The archived render script's 8.55-second duration differs from the current GIF and is not used.

The [provenance note](scripts/OVERVIEW_DATA.md) documents the data, objective, timing audit, and limitations. Downloadable [inference](public/data/overview-example.json) and [training](public/data/training-example.json) JSON include numeric values and source hashes. The approved schematic and newly requested five-panel RUL figure are the current figure scope; former illustrative demos remain deferred.

Regenerate from the repository root with the existing ML Python environment; all generated files and caches stay under `webpage/`:

```bash
PYTHONDONTWRITEBYTECODE=1 MPLCONFIGDIR="$PWD/webpage/.cache/matplotlib" python webpage/scripts/export_overview.py
PYTHONDONTWRITEBYTECODE=1 MPLCONFIGDIR="$PWD/webpage/.cache/matplotlib" python webpage/scripts/export_training.py
PYTHONDONTWRITEBYTECODE=1 MPLCONFIGDIR="$PWD/webpage/.cache/matplotlib" python webpage/scripts/prepare_paper_schematic.py
```

The Astro build consumes saved assets; it does not load checkpoint weights or perform model inference in the browser. Numerical training checks cover exact source correspondence, path endpoints/formula, target and predicted prefix zeros, MSE definition, and matching public JSON. The earlier example-selection revision changed the matched inference data and cycle window; training data, the 80–110% state window, and 2.85-second timing remain unchanged. Those source/data checks apply to the approved schematic revision. Prior presentation checks confirmed unchanged replay exports and advancing animation. The current toolbar/header removal and new RUL figure pass scoped scientific/build/static/browser verification; broader release checks stay open.

## Current visual direction

Use navy `#17365D`, black `#111111`, and magenta `#C2188B` on white/light-gray backgrounds. Navy identifies page accents; magenta provides restrained emphasis. The approved schematic retains its documented paper-palette exception. Retain labels and line styles alongside color. These tokens replace draft 02's cyan/pink preference.

**Figure 1 exception:** the opening schematic retains the original pink curve `#E375C2`, purple DiT blocks, encoder and embedding colors, and **cool** capacity colormap. Panel frames are removed; navy headings and short magenta rules organize the open sections, and plot axes are black. Its always-visible reference is dashed black and its fixed observed prefix is solid black. Black connector arrows are removed; faint pink/purple tracks, particles, and soft block highlights share the animation clock. Exact original colors/opacities and overlay geometry are recorded in `public/figures/figure1-layout.json`; the rest of the page retains the accepted site palette.

Use self-hosted **Source Sans 3** throughout: regular, semibold, and bold for prose, headings, table, captions, notes, resource rows, citation, and all schematic labels. Its [source/version record](public/fonts/SOURCE-SANS-3-SOURCE.txt), [SIL Open Font License](public/fonts/LICENSE-SOURCE-SANS-3.txt), and [font README](public/fonts/README.md) document provenance. STIX and Computer Modern assets may remain as historical files, but are not active page typography. Shared tokens live in `src/styles/global.css`; font declarations live in `src/styles/figure-fonts.css`.

The text and table columns are 700px wide, with 16px body text and 1.65 line height. Section headings are left aligned (h2 22px, h3 18px). Prose, the table caption, and the 13px acknowledgment are justified. The academic banner remains centered in a 1050px hero, while the original 14px TL;DR moves into the 700px reading column for two desktop lines. University logo display widths become 118.8px and 138px. The current RUL figure uses three columns above 1050px with the second row centered, two columns from 681–1050px, and one at 680px and below; panels are at most 360px wide. Desktop/900px/390px layout validation passes; user appearance review remains open.

## Editing map

| File | Purpose |
| --- | --- |
| `src/pages/index.astro` | Paper-based page sections, approved overview, semantic results table, resource rows, and citation interaction |
| `src/styles/global.css` | Shared visual design and responsive layout |
| `src/styles/figure-fonts.css` | Active self-hosted Source Sans 3 regular/semibold/bold declarations |
| `src/data/content.ts` | Authors, affiliations, shared metadata, and citation |
| `src/data/paperContent.ts` | Restored original TL;DR, exact acknowledgments, concise/full historical prose, unchanged Table 1/notes, and references |
| `scripts/PAPER_CONTENT.md` | Source locations and transcription/provenance decisions for the page text and table |
| `src/components/MethodOverview.astro` | Automatically looping open-panel Figure 1 with equal plot frames, aligned models, curated test input, and reduced-motion fallback |
| `src/components/RulPlots.astro` | Responsive five-panel paper RUL figure, dataset labels, caption, and accessible panel descriptions |
| `src/components/SchematicPlot.astro` | Fixed-axis SVG plot frames, ticks, and data clipping for schematic subplots |
| `src/components/FlowSignal.astro` | Pink/purple connector tracks and schematic motion packets |
| `src/data/overview-example.json` | Build-time matched MATR-1 example, real predictions, ODE states, and metadata |
| `public/data/overview-example.json` | Identical downloadable inference export and source hashes |
| `src/data/training-example.json`, `public/data/training-example.json` | Matched training input, 101 path/velocity evaluations, loss, normalization, and provenance |
| `public/data/capacity-matr1-training-{cool,cividis}.png` | Actual training-row capacity matrix in both palettes |
| `scripts/export_training.py` | Fixed-checkpoint training-objective export; no optimizer or ODE solve |
| `public/data/capacity-matr1-example.png` | Retained full-resolution 100 × 100 cividis capacity matrix from the preceding iteration |
| `public/figures/capacity-matr1-paper-cool.png` | Same real matrix in Figure 1's cool palette; selected by `capacity.paperImage` |
| `public/figures/figure1-background.svg` | Aligned original model artwork without enclosing panel boxes, data curves, or capacity pixels |
| `public/figures/figure1-layout.json` | Original colors and panel provenance, aligned plot/model bounds, and removed panel paths |
| `scripts/prepare_paper_schematic.py` | Reproducible Figure 1 artwork/manifest and paper-palette capacity export; no inference |
| `scripts/select_overview_example.py` | Reproducible cached-row screening and explicit forecast-error selection |
| `scripts/export_overview.py` | Reproducible CPU inference, fresh-draw selection, data/image exports, and numerical checks |
| `scripts/export_rul_plots.py` | Reproduce the five RUL SVG panels from published PDF vector coordinates and color bins; no replacement inference |
| `public/figures/rul/{matr-1,matr-2,hust,mix-100,mix-20}.svg` | Live Source Sans 3 Figure 4 panels with original points, axes, and separate color scales |
| `public/data/rul-paper-scatter.json` | All 388 original marker coordinates/color bins, converted axes, source/output hashes, and precision limitations |
| `scripts/RUL_PLOTS.md` | RUL extraction, ordering/scales, styling decisions, source uncertainty limitations, and reproduction |
| `scripts/OVERVIEW_DATA.md` | Scientific provenance, schema meaning, limitations, and regeneration instructions |
| `src/components/TrajectoryPlot.astro` | Legacy illustrative component; not displayed, deferred |
| `src/components/GenerationPreview.astro` | Legacy illustrative animation; not displayed, deferred |
| `public/fonts/` | Source Sans 3 assets/license/source record and retained historical font files |
| `public/logos/` | Intact official university SVGs, source hashes/usage guidance, and the documented NeurIPS text-only decision |
| `astro.config.mjs` | Conditional future public origin and base path; static build settings |
| `public/social-card.png` | Reproducibly generated, visually checked 1200 × 630 card for conditional production metadata |
| `public/favicon.svg` | Small FlowBatt mark |
| `PLAN.md` | Requirements, decisions, checklist, and iteration log |

Follow the current paper-content checks and remaining release audit in [PLAN.md](PLAN.md). Preserve the approved schematic and the distinction between physical cycles and flow time. Future figures require renewed scope approval and their own scientific-data audit; they are not prerequisites for this page.

No research code, manuscript, model checkpoint, or existing result file is modified by this site.
