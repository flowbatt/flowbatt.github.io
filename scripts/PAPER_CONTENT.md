# Paper text used by the project page

## XAI subsection update

Results and discussion ends with a short **XAI-guided encoder design** subsection,
immediately after RUL prediction. The table labels are shortened to **RF** and
**MLP**, removing “(BatteryML)” without changing numerical values or references.
`xaiDiscussion` condenses the CNN encoder paragraph and appendix Grad-CAM
analysis in `cameraready/cameraready.tex` (lines 193 and 602–660). It identifies
the scalar-RUL diagnostic task, blank attribution maps, and the LeakyReLU
encoder adopted in FlowBatt. `xaiCaption` identifies the 42 matching test cells
and the per-cell relative-attribution scale. No seed-performance chart or
newer reproduction results are added.

The three original paper grids are displayed in one row at the text width,
with Source Sans 3 labels and a stacked layout below 600px. Asset provenance
and unchanged SHA-256 hashes are documented in `public/figures/xai/README.md`.
Production build, asset identity, subsection placement, unique IDs, and ARIA
references pass. The local server serves the new image with HTTP 200. Browser
preview controls were unresponsive, so desktop/mobile rendering is not newly
visually verified. The historical verification records below predate this
additional figure.

`src/data/paperContent.ts` contains the current concise page copy, the unchanged
published Table 1, the new brief RUL discussion/caption, and historical full-text exports retained as provenance.
The page restores the original 17-word screenshot TL;DR and retains a 100-word introductory overview without
an “Abstract” heading. The former lay summary is no longer current page copy.
Methodology, Results and discussion, and Conclusions and outlook organize the
remaining text. Shortened passages use selected complete paper sentences where
possible; other edits are explicitly documented abridgments, not verbatim
paragraph reproductions. New RUL copy draws only on the accepted paper; no novel scientific claim or table value is added. The visible Limitations heading/paragraph is removed at the user’s request, while its source export and caveats remain intact.

## Current concise exports

All current prose exports are plain strings. The table and references retain
their existing structured schemas.

| Export | Words | Source and editorial treatment |
| --- | ---: | --- |
| `tldr` | 17 | Exactly restored original screenshot wording, identical to `screenshotTldr`: “We introduce FlowBatt, a use-inspired conditional generative framework that adapts flow matching to probabilistic battery degradation modeling.” |
| `overview` | 100 | Abstract (line 109), introduction (lines 125–128), and conclusion (line 405). Keeps the battery-aging problem, early-cycle conditioning, multiple plausible trajectories/empirical intervals, five-setting evaluation, and unified tasks. Expands SOH on first use. Omits numeric rankings and architectural details reserved for later sections. Render as unheaded introductory prose, not a full abstract. |
| `methodology` | 55 | Flow-matching description (lines 137, 154–170) and architecture (lines 186–195). The cycle-by-voltage/baseline-subtracted capacity definition is a complete source sentence; the CNN/time-embedding/DiT and vector-field/ODE descriptions are condensed. It describes flow-matching training accurately and does not reuse the paper's diffusion-specific Figure 1 training sentence at line 176. |
| `resultsIntro` | 67 | SOH protocol/baselines (lines 229, 232) and shared split context. Preserves evaluation up to EOL, final-value padding, averaging across test samples, percentage units, and adaptation of RF/MLP/BatLiNet for trajectories. Expands EOL and random forest (RF); links RF and MLP to BatteryML [51] and BatLiNet to [52]. |
| `resultsFindings` | 44 | Two complete accepted sentences from lines 255 and 253, reordered to lead with FlowBatt. Retains the lowest-mean-RMSE and DiffBatt/Transformer comparison without repeating per-dataset values from the table. |
| `rulDiscussion` | 77 | Camera-ready Section 3.2: line 302 defines trajectory-derived RUL and ten generated trajectories per input; lines 339/341 establish competitive downstream RUL performance, the HUST result, and top-three RMSE rankings; line 353 describes the tendency for larger error to accompany larger variability. Condenses these findings without numerical gains or a calibrated-uncertainty/generalization claim. |
| `rulCaption` | 40 | Figure 4 caption (line 348) and discussion (line 353), with the EOL thresholds from the benchmark protocol (line 209). Identifies reference/predicted axes, perfect-agreement diagonal, per-cell standard deviation across ten trajectories, separate dataset scales, and the 90% MIX-20 versus 80% other-dataset threshold. Original PDF coordinates/color bins, panel axes/ticks/scales, and source hashes pass independent asset review; final desktop/900px/390px browser integration passes. |
| `closingConclusion` | 77 | Camera-ready conclusion (line 405): excerpts the clause beginning “FlowBatt learns,” the final accepted benchmark sentence, the complete sentence on empirical prediction intervals, and the opening clause on synthetic trajectories improving downstream RUL modeling. Omits numerical gains, the baseline comparison, and the BatLiNet citation; ends the selected synthesis clause with a period. |
| `closingLimitations` (retained, unrendered) | 58 | Removed from visible page at the user’s request; the unchanged source remains. Line 407. The first sentence is shortened to preserve empirical-interval undercoverage on MATR-2/HUST; the remaining complete sentences retain fixed 20/100-cycle inputs, missing operating/environmental variables, unestablished unseen-chemistry/protocol generalization, and absent physical constraints. |
| `acknowledgments` | 79 | Complete accepted camera-ready acknowledgment at line 415. Only TeX conversion: `\textbar{}` → `\|`, `\textsuperscript{3}` → `³`. Preserve CircularLIB, donor/program spelling, `MWK \| ZN3678`, and `DS³`. Render in justified 13px footer text after the email and official university logos. |
| `closingOutlook` | 70 | Two verbatim sentences from Broader impacts (line 963) on sustainable energy, battery lifetimes, reliability, waste, and resource consumption, followed by the final outlook sentence (line 409) on broader datasets and foundation models. Retains “can” and “may” for potential future impacts. |

The conclusion now foregrounds the contribution and sustainability implications at the author's request. Closing wording is excerpted from the camera-ready source, with the benchmark sentence taken from the final revision branch and the synthesis sentence shortened before its numerical-gain clause. The retained, unrendered limitations and full outlook exports preserve the original scope discussion. Neither the shortened RUL discussion nor the scatter plot establishes calibrated intervals or generalization beyond the benchmark splits. The schematic legend and its unused styles are removed; the animation and numerical data are unchanged. Verification records below describe earlier iterations.

## Sources and conversion

- Primary source: `cameraready/cameraready.tex`, SHA-256
  `8ce5b336642513d58e15ae787d45cd900c471ba69034f73731fb41fbcebe18ac`.
- Comparison source: `manuscript/main_rev_HE.tex`. Its abstract hyphenates
  “state-of-health” and “remaining-useful-life”; the camera-ready uses “state of
  health” and “remaining useful life”. The camera-ready wording is retained.
  The main trajectory-results table is identical in both sources, as are the
  accepted conclusion/outlook paragraphs.
- Camera-ready final mode defines `\revdd{old}{accepted}` as its second argument,
  retains `\newtext`/`\rev`, and hides `\revd`/`\highlight`. The export resolves
  those macros before extracting prose; deleted claims are not exported.
- For the historical full-text exports, typographic TeX wrappers are removed; `\%` becomes `%`, `\pm` becomes `±`, math delimiters are removed, and whitespace is normalized while retaining word boundaries across macro groups (including “constraints and descriptions”). Their wording and complete paragraph boundaries are preserved. Current concise exports use the documented selection/abridgment above.
- Historical `screenshotTldr` and `laySummary` preserve the earlier screenshot transcription. The current `tldr` restores the exact original screenshot wording at the user's request; it duplicates `screenshotTldr` literally. The lay summary remains omitted from the page.

## Retained full-text provenance and unchanged table

| Export | Source and scope |
| --- | --- |
| `screenshotTldr`, `laySummary` | Original screenshot transcription; `tldr` now exactly repeats `screenshotTldr`, while `laySummary` remains historical and unrendered |
| `abstract` | Historical complete abstract, camera-ready line 109; the current page uses `overview` |
| `sohResults` | Historical five complete SOH-prediction paragraphs, lines 227, 229, 232, 253, 255; current page uses `resultsIntro`/`resultsFindings` |
| `sohTable` | Table 1, `tab:soh-trajectorywise`, lines 234–251; six methods × five datasets, all 30 mean/SD pairs retained |
| `conclusions` | Historical complete conclusion and limitations, lines 405 and 407; current page renders `closingConclusion` but omits `closingLimitations` at the user’s request |
| `outlook` | Historical complete outlook paragraph, line 409; current page uses `closingOutlook` |
| `paperReferences` | The two citations appearing in these excerpts, numbered from the camera-ready `.aux` and titled/linked from its `.bbl` |

`sohTable.columns` are dataset names in paper order: MATR-1, MATR-2, HUST,
MIX-20, MIX-100. Each row has `method`, five exact formatted `values`, and
`emphasis` (`best`, `second`, or `none`). All five FlowBatt values are best;
all five DiffBatt values are second-best. In the retained source data, `caption` is the first complete caption sentence and `notes` contains every remaining caption sentence, without omission or paraphrase. The visible metric-note list is removed at the user's request; the complete definitions remain here and in the paper. Render best values bold and second-best values
underlined to honor the caption.

The ± terms are standard deviations across ten generative draws from one
trained checkpoint for FlowBatt/DiffBatt, and ten training initializations
for other models. They are not confidence intervals or across-cell spread.
The table is trajectory-wise SOH RMSE (%) up to EOL, not cycle-wise error or
RUL error. The source's metric wording is preserved in `sohTable.caption` and `sohTable.notes`, even when the note list is not rendered on the page.

## RUL figure and uncertainty provenance

The new RUL subsection renders `rulDiscussion` and `rulCaption` with all five Figure 4 panels in paper order: MATR-1, MATR-2, HUST, MIX-100, MIX-20. `scripts/export_rul_plots.py` reads the published panel PDFs’ vector operators, retaining all 388 marker centers and their exact 256-bin color assignments. Its SVG assets live under `public/figures/rul/`; `public/data/rul-paper-scatter.json` records original coordinates/colors, converted cycle positions, source/output hashes, and precision limits. Full reproduction and original independent axis/color scales are recorded in [`RUL_PLOTS.md`](RUL_PLOTS.md).

The combined manuscript/camera-ready Figure 4 files are byte-identical. The web plots preserve original point centers, axes, clipping, identity lines, and separate colorbar labels, with Source Sans 3 text and navy-to-magenta bin remapping. Marker size is a presentation change: the original MATR-2 point `(1645, 2033.5)` remains above the published y-limit and clipped; the smaller webpage marker no longer exposes the paper marker’s tiny cap.

Color represents the per-cell standard deviation of scalar RUL values extracted separately from ten generated trajectories. The PDF contains color bins and integer-formatted colorbar labels, not exact raw standard deviations or their exact normalization extrema. It also does not establish whether the plotted predicted coordinate is a mean, median, or individual draw. Do not add such claims, infer confidence intervals, compare colors across dataset scales as a common absolute scale, or substitute the different cached predictions. The source/geometry/color/ID checks pass independently; final page integration, build/static, and desktop/900px/390px browser checks pass.

## Reference targets retained for page rendering

The retained table notes and historical full-text exports retain reference labels. `PaperText.astro` can wrap them in links without changing their wording. Current shortened prose need not display every historical target:

- `table 1`: link to the displayed results table (`#soh-results-table`). It is
  Table 1 on PDF page 7 according to `cameraready/cameraready.aux`.
- `appendix A.5`: the paper's additional SOH results, PDF page 20.
- `appendix A.5.3`: the cycle-wise SOH protocol, PDF page 22.
- `[51]`: BatteryML, Zhang et al., ICLR 2024; the local bibliography records
  `http://arxiv.org/abs/2310.14714`; the page normalizes this target to `https://arxiv.org/abs/2310.14714` after review.
- `[52]`: BatLiNet, Zhang et al., Nature Machine Intelligence 2025; the local
  bibliography records DOI `10.1038/s42256-024-00972-x`.

Numbers and pages are taken from the local compiled auxiliary file. Keep the
paper's numbering when linking these excerpts; do not silently renumber them
as a new independent bibliography.

## Selection and omissions

Current prose omits the lay summary, long background discussion, repeated
per-dataset numerical results, the extended baseline rationale, and RUL/synthesis
performance numbers from prose; the requested RUL figure retains the original graphical values and scales. Qualitative conclusions on competitive trajectory-derived RUL and synthetic SOH improving downstream RUL modeling remain. The page retains a brief method paragraph and a brief protocol plus qualitative result interpretation. The source Table 1 export still contains all 30 exact mean/SD pairs, its full caption, and every essential metric/± note. No table
value, dataset order, emphasis flag, or note changed during this abridgment.

The visible schematic caption, separate animation timing note, and table metric-note list remain removed at the user's request. The current iteration also removes the schematic toolbar/header and automatic-loop label while preserving animation, and removes the visible Limitations heading/paragraph while preserving its export. Their underlying scientific interpretation, timing, selection metadata, JSON exports, and complete table caption/notes remain in the source and provenance files. This changes presentation only; it does not relabel the curated sample as representative, alter any trajectory/table value, or change the meaning of ±. The complete accepted acknowledgment paragraph is added as justified 13px footer text after the contact email and official university logos. Logo sources/usage interpretation are recorded in `public/logos/README.md`; NeurIPS remains venue text for the reasons documented in `public/logos/NEURIPS-SOURCE.md`.

The earlier full paragraphs remain exported for provenance and possible editorial
comparison, but are not current page copy. The new closing strings contain no
“Limitations.” or “Outlook.” prefix, so page headings do not need to strip one.
The approved schematic's geometry, numerical data, and timing remain unchanged and separate from Table 1's aggregate benchmark; the publication layout applies the common Source Sans 3 family to its labels. Its selected-example error must not replace the published
metric or be represented as using the same aggregation protocol.

## Verification

For the concise-content revision, the overview is verified at 100 whitespace-
separated words. The seven original concise body strings remain 408 words in source; the 58-word limitations string is no longer rendered and a 77-word RUL discussion is added (427 words across the currently intended main body strings, excluding the new 40-word RUL caption). The restored TL;DR is 17 words and the new acknowledgment is 79 words. Table 1/caption/notes are excluded from these counts. Equality with the original screenshot TL;DR and direct accepted-source acknowledgment conversion are verified in source and generated HTML. All other copy, table values/caption/notes, and references are unchanged.
The table block, including its complete caption and notes, remains byte-identical (SHA-256 `bde3aa15c5653872b8f292f04606d9ee86e7e2be5ee405ee9bf9fa1fb7c80647`). The only reference change is BatteryML's HTTP-to-HTTPS target normalization; no reference title or scientific content changes.

**Current RUL/presentation verification:** the RUL discussion and caption are 77 and 40 whitespace-separated words, respectively. Their accepted-paper source locations and intended uncertainty meaning are recorded above. Independent asset review passes the five source hashes, composite identity, all 388 original centers/color bins, axes/ticks/scales, output mapping/IDs, and rendered contact sheet. Final production build passes at 13:37. Static integration verifies two figures/six SVG image roles, all 30 table values, unique IDs/resolved ARIA/internal links, existing assets, absent toolbar/Limitations labels, unchanged exact 14px TL;DR, 118.8px/138px logos, and byte-identical public/built training/inference/RUL JSON. Firefox desktop/900px/390px verifies the 3+2/two-column/single-column RUL layouts, readable axes/colorbars/text, two-line desktop TL;DR/natural mobile wrapping, smaller logos, and continued schematic motion. The browser was returned to the desktop RUL section. Citation/subpath checks retain prior evidence; user review and broader release/accessibility audits remain open. The current figure scope is the approved automatic schematic plus the requested five-panel Figure 4 adaptation; all other figures/demos remain deferred. TL;DR wording/14px size, table values, replay data/timing, and acknowledgment source are unchanged.

**Historical original-TL;DR/table/footer verification:** final default build passes at 13:21:10 after the acknowledgment justification fix. Independent static checks verify all 30 table values, five second-best marks, 23 unique IDs, resolving anchors/ARIA references, seven local HTML assets including both hash-matched official logos, one figure/no figcaption, and absence of the visible timing/table-note list. Source/public/built replay JSON are byte-identical. The reserved-origin/subpath build passes at 13:20:57 with all HTML/logo/font paths and canonical/social URLs correct; the default local build is restored with noindex and no invented public origin.

Firefox desktop and 390 × 844 inspection verifies the original 14px TL;DR on one desktop line and three natural mobile lines; the 700px table aligns with prose, and mobile keyboard panning reaches MIX-20/MIX-100 with fixed method labels. Official logos display intact in a desktop row/mobile stack, followed by the exact acknowledgment in readable justified 13px text. The automatic schematic still advances. The browser was returned to the desktop footer. Citation copying was verified in the previous iteration and is unchanged, not newly clicked here. User review and broader accessibility/release checks remain open; no publishing occurred.

**Historical concise/publication-layout verification, before the TL;DR/footer/note-removal revision:**

This prose refinement changes no numerical exports or schematic geometry/timing. The publication-layout font update is separate. Final root build passed at 13:03:46; the reserved-origin/subpath configuration build passed at 13:00:57. Source/static review confirms one displayed figure, one table with all 30 values, no duplicated numeric mean/SD pairs in prose, 24 unique IDs, resolving anchors/assets, and byte-identical source/public/built training and inference replay JSON.

Firefox desktop and 390 × 844 inspection verifies the concise justified layout, single-line desktop TL;DR, Source Sans 3 throughout (including diagram/citation), no overlapping diagram labels, correct ±/bold/underlines, mobile table/diagram panning, citation wrapping/copying, mobile outlook, and 390px header resource buttons in a 2 × 2 layout. The loop visibly advances, and the browser was returned to the desktop top. The local 1200 × 630 social card and conditional canonical/social/subpath metadata were checked; no publishing occurred. Static/reduced-motion logic is source-reviewed, not browser-emulated. User review, full keyboard/JavaScript-disabled/lifecycle checks, and actual deployment remain open.

**Historical full-text revision, before this abridgment:**

The extraction resolves balanced TeX groups, checks for unconverted commands,
and compares every exported prose block with direct final-branch conversion
of its source paragraph. An independent source review confirms all 30 table
values, dataset ordering, best/second-best styles, abstract wording, and
standard-deviation semantics. The final production build passed on 2026-11-22
at 12:43:11. Integration checks confirm one displayed figure, one semantic
results table with 30 values, 25 unique HTML IDs, resolving local anchors and
assets, and the three supplied resource URLs. The training and test JSON
copies in source, public, and built output are byte-identical.

Firefox desktop and 390 × 844 inspection confirms readable prose, table
caption wrapping, horizontal table scrolling with fixed method labels, and
successful BibTeX copying. Table text uses self-hosted STIX Two Text 400/700
so mathematical symbols, including ±, render correctly. The approved
schematic and its existing bold font remain unchanged.
