# FlowBatt project page

Academic project website for **FlowBatt: Flow Matching for Probabilistic Battery Degradation Prediction** (NeurIPS 2026).

[Website](https://flowbatt.github.io/) · [Paper](https://arxiv.org/abs/2611.03150) · [Research code and pretrained models](https://github.com/HamidrezaEiv/FlowBatt)

The static Astro site includes the animated flow-matching schematic, SOH and RUL results, the paper's XAI heatmaps, and the citation. Figures and animations use bundled data; viewing the website does not run a model or require a backend.

## Develop locally

Use Node.js 24 or a compatible newer release, then run these commands from the repository root:

```sh
npm ci
npm run dev
```

## Build and deploy

```sh
npm run build
npm run preview
```

GitHub Actions builds and publishes pushes to `main` at **https://flowbatt.github.io/**. The repository's Pages publishing source must be **GitHub Actions**. See [DEPLOYMENT.md](DEPLOYMENT.md) for the workflow and configuration.

## Scientific assets and provenance

Paper text and figure provenance are recorded under `scripts/` and alongside the corresponding files in `public/`. The original heatmaps and RUL artwork are preserved, with the website's typography applied to figure labels. Font and institutional-logo source notices remain bundled with their assets.

The data-export scripts require the separate FlowBatt research workspace. They are not needed to build this site. [PLAN.md](PLAN.md) and [LOCAL_DEVELOPMENT.md](LOCAL_DEVELOPMENT.md) preserve the local development checklist and historical verification notes.
