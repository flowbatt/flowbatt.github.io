# Self-hosted page fonts

The current page uses **Source Sans 3** as its single typeface family, including
prose, paper results, captions, and schematic labels. The upright 400, 600, and
700 WOFF2 faces are unmodified assets from Adobe's pinned 3.052R release.
The schematic retains its bold 700 weight; changing the family does not alter
its plot/model geometry, colors, data, or timing.

- [Source/version/hash and glyph checks](SOURCE-SANS-3-SOURCE.txt)
- [SIL Open Font License 1.1](LICENSE-SOURCE-SANS-3.txt)
- [Official Adobe release](https://github.com/adobe-fonts/source-sans/releases/tag/3.052R)

CSS is in `src/styles/figure-fonts.css`. Fonts are served locally without an
external font service; all active `@font-face` declarations use Source Sans 3.
The supplied files support ±, mathematical minus, Greek letters, and the
Latin typography used on the page.

## Historical assets

Earlier font files and licenses are retained for provenance, but are no longer
registered by the active stylesheet:

- Computer Modern: `computer-modern-roman.ttf` and `computer-modern-bold.ttf`,
  unmodified renamed `cmr10.ttf`/`cmb10.ttf` from Matplotlib 3.10.8. The original
  TrueType conversion is by Basil K. Malyshev (1994–1995); see
  [the BaKoMa license](LICENSE-BAKOMA.txt) and
  [original collection](https://ctan.org/tex-archive/fonts/cm/ps-type1/bakoma).
- STIX Two Text: previous Regular/Bold assets from official release 2.13 b171;
  see [source records](STIX-SOURCE.txt) and [SIL OFL license](LICENSE-STIX.txt).
