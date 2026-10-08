# CLAUDE.md — UK Emporium (uke)

Persistent rules for this repo. Read this before every change.

## What this is
A hand-written static storefront for UK Emporium, deployed to Netlify. There is no
database, no authentication, no CMS and no inline editor. The catalogue is JSON files in
the repo; changing a product means editing a file, committing and pushing.

## Stack
- Site: hand-written HTML5 at the repo root + `styles.css` + vanilla JS (`shared.js`,
  `js/render-products.js`). No bundler, no framework. Live Server / `npm run dev`
  compatible.
- Catalogue: `data/products/<id>.json`, one file per product — the source of truth.
  `npm run build:catalogue` stitches them into `data/products.json`, which is what the
  browser fetches. Both are committed.
- Rendering: `js/render-products.js` does `fetch('data/products.json')` and builds the
  product cards into `[data-category]`, `[data-featured]`, `[data-new-strip]` and
  `[data-count]` slots.
- Images: local files under `images/products/`. Catalogue images are
  `images/products/<id>.webp` (max 1600px, q80). Brand and logo art live in
  `images/brands/` and `images/logos/`.
- Promo ticker: `data/settings.json`, read by `shared.js`.
- Cart: client-side only, in `localStorage` (`uke_cart`), re-priced from the catalogue
  on every page load.
- Deploy: Netlify, `publish = "."`, `command = "npm run build:catalogue"`. Push to the
  deploy branch and Netlify rebuilds.

## Data flow
`data/products/*.json` → `npm run build:catalogue` → `data/products.json` → browser.

- `data/products.json` is a generated artifact (its `_comment` key says so). Never edit
  it by hand; edit the per-product file and rebuild. Commit the regenerated file with
  the edit so local serving and the deployed site agree.
- The filename is the id. `build-catalogue.mjs` trusts the filename over the `id` field
  and fails on duplicate ids.
- New products take the next unused `uke-####` id (highest existing + 1).
- `data/featured-shop.json` and `data/featured-index.json` are curated **reference**
  lists — ordered product ids plus presentation-only overrides (tag, gold, image,
  cardClass). A featured entry must never restate a price.

## Conventions
- Audit-first: read the relevant existing files before writing. Prefer small, scoped diffs.
- Pages stay single-file and Live Server-compatible.
- Prices are numbers, formatted for display by `formatPrice` and never parsed back out of
  the DOM. Never add a `data-price` attribute — that is a second copy of price.
- Image paths in product JSON are relative and local. No remote image hosts.
- One concern per commit, with a clear message.
- Scripts are dependency-free ESM. Do not add a runtime dependency without a reason.
- `index.html` and `shop.html` carry inert `data-tt8-edit` / `data-tt8-rich` attributes
  on static copy. Nothing reads them; they are harmless.
- Update this file whenever a rule or convention changes.

## Retired — do not reinstate
- Decap CMS + Netlify Identity (`admin/`). `/admin` and `/admin/*` 301 to `/`.
- The hosted-database catalogue, `login.html` and the inline admin editor. The site
  briefly read products from a database; that layer was removed and the repo is
  authoritative.
- `editor/overlay.js` and any Next.js / Vercel publish pipeline.

## Scripts
- `npm run dev` — serve the site locally on :3000.
- `npm run build:catalogue` — `data/products/*.json` → `data/products.json`.
- `npm run normalise:products` — rewrite product files in canonical key order (values
  untouched), so diffs stay small.

## Test after changes
- `npm run build:catalogue` reports the expected product count with no warnings.
- `npm run dev`, then load `index.html`, `shop.html` and each `cat-*.html`: products
  render, images load, no console errors, no requests to remote catalogue hosts.
- Add to cart, reload: the cart persists and totals are right.
