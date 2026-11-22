# FlowBatt on GitHub Pages

- Repository: https://github.com/flowbatt/flowbatt.github.io
- Website: https://flowbatt.github.io/
- The contents of this `webpage/` directory form the website repository root.
- Publishing source: repository **Settings → Pages → GitHub Actions**.

The workflow in `.github/workflows/deploy.yml` builds the Astro site with
Node.js 24 and npm, then deploys the generated static files. It runs on pushes
to `main` and can also be run manually from the Actions tab. No custom domain,
`CNAME` file, or repository subpath is needed.

## Local development

```sh
npm ci
npm run dev
```

Production verification:

```sh
npm run build
npm run preview
```

The default production origin is `https://flowbatt.github.io`, with base `/`.
`FLOWBATT_SITE_URL` and `FLOWBATT_BASE_PATH` remain available for other preview
targets. The development server retains `noindex, nofollow`; production emits
the canonical URL and absolute social-preview URLs for the configured origin.

## Publishing updates

Commit the desired website changes and push `main` to `origin`. Check the
**Deploy FlowBatt to GitHub Pages** workflow in the repository's Actions tab.
Once both jobs pass, verify the public page and its figures. Publishing does
not require uploading `node_modules/`, local caches, or generated `dist/`.

The website build uses only committed files in this repository. The historical
data/figure export scripts under `scripts/` document how the bundled scientific
assets were prepared; rerunning those exporters requires the separate research
workspace and is not part of deployment.
