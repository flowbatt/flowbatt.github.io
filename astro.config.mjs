import { defineConfig } from 'astro/config';

export default defineConfig({
  // Organization Pages site; local development remains unindexed in index.astro.
  site: process.env.FLOWBATT_SITE_URL || 'https://flowbatt.github.io',
  base: process.env.FLOWBATT_BASE_PATH || '/',
  output: 'static',
  devToolbar: { enabled: false },
});
