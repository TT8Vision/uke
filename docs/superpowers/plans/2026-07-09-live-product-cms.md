# Live Product CMS Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let the client edit products (price, add/edit/remove, stock, "New in store") through a branded `/admin` panel with no code, by making the catalog render from a single `data/products.json` that Decap CMS edits.

**Architecture:** Products move from hardcoded HTML into `data/products.json`. A vanilla-JS renderer (`render-products.js`) fetches that JSON at page load and builds the existing `.product-card` markup into each category grid. Decap CMS (`/admin`, GitHub login) commits edits to `products.json`; Netlify redeploys (~1 min) and the change is live. No build step, no framework.

**Tech Stack:** HTML5, Tailwind CDN, vanilla JS, Decap CMS (CDN), GitHub OAuth, Netlify hosting. Node (already present via `npx`) is used only for the one-time throwaway seed script.

## Global Constraints

- No build tools, no npm dependencies in the shipped site, no bundler, no framework (CLAUDE.md). Node is allowed only for the throwaway seed script.
- Tailwind via CDN only. Branding via CSS custom properties already in the pages.
- Site must still run under VS Code Live Server / static hosting with no compile step.
- Preserve existing `.product-card` markup and CSS exactly so visuals are unchanged.
- Categories (slugs) are fixed: `beers, cereals, cleaning, colddrinks, confectionery, groceries, hotdrinks, kent, personalcare`.
- Prices are South African Rand, displayed as `R39.90` (two decimals, tabular nums).
- Product object shape (used by every task):
  ```
  { id: string, name: string, brand: string, volume: string,
    category: string, price: number, oldPrice: number|null,
    stock: "in-stock"|"low-stock"|"out-of-stock",
    tag: "none"|"bestseller"|"popular"|"specialty"|"sale",
    isNew: boolean, image: string, order: number }
  ```

---

### Task 1: Seed `data/products.json` from existing HTML

Extract the ~880 hardcoded product cards into `data/products.json`. The seed script is a **throwaway** Node script (deleted after use); the generated JSON is the deliverable.

**Files:**
- Create: `scripts/seed-products.mjs` (throwaway)
- Create: `data/products.json` (generated)
- Read: `cat-beers.html`, `cat-cereals.html`, `cat-cleaning.html`, `cat-colddrinks.html`, `cat-confectionery.html`, `cat-groceries.html`, `cat-hotdrinks.html`, `cat-kent.html`, `cat-personalcare.html`

**Interfaces:**
- Produces: `data/products.json` — an array of product objects (shape in Global Constraints), which every later task consumes.

- [ ] **Step 1: Record the expected counts (verification baseline)**

Run:
```bash
grep -c "product-card" cat-*.html
```
Expected (record these): beers 55, cereals 35, cleaning 100, colddrinks 79, confectionery 200, groceries 171, hotdrinks 72, kent 18, personalcare 153. Total 883.

- [ ] **Step 2: Write the seed script**

The cards are machine-generated with regular markup, so regex extraction is safe. `id` = image basename (stable); `order` = index within page; `stock` defaults to `in-stock`; `isNew` defaults `false`; `tag` mapped from the badge text.

Create `scripts/seed-products.mjs`:
```js
import { readFileSync, writeFileSync } from 'node:fs';

const CATS = ['beers','cereals','cleaning','colddrinks','confectionery',
  'groceries','hotdrinks','kent','personalcare'];

const TAG_MAP = { 'best seller':'bestseller', 'popular':'popular',
  'specialty':'specialty', 'sale':'sale' };

const CARD_RE = /<div class="product-card[^"]*">([\s\S]*?)<\/div>\s*<\/div>\s*<\/div>/g;
const grab = (html, re) => (html.match(re)?.[1] ?? '').trim();
const price = (s) => { const n = parseFloat(String(s).replace(/[^0-9.]/g, '')); return Number.isFinite(n) ? n : null; };

const all = [];
for (const cat of CATS) {
  const html = readFileSync(`cat-${cat}.html`, 'utf8');
  let m, i = 0;
  while ((m = CARD_RE.exec(html))) {
    const c = m[1];
    const img = grab(c, /<img[^>]*src="([^"]+)"/);
    const alt = grab(c, /<img[^>]*alt="([^"]*)"/);
    const tagText = grab(c, /<span class="product-tag[^"]*">([^<]*)<\/span>/).toLowerCase();
    const brand = grab(c, /<p class="product-brand">([^<]*)<\/p>/);
    const name = grab(c, /<h3 class="product-name">([^<]*)<\/h3>/);
    const volume = grab(c, /<p class="product-volume">([^<]*)<\/p>/);
    const oldP = grab(c, /<span class="product-price-old">([^<]*)<\/span>/);
    const newP = grab(c, /<span class="product-price">([^<]*)<\/span>/);
    const id = (img.split('/').pop() || `${cat}-${i}`).replace(/\.[a-z]+$/i, '');
    all.push({
      id, name, brand, volume, category: cat,
      price: price(newP), oldPrice: oldP ? price(oldP) : null,
      stock: 'in-stock', tag: TAG_MAP[tagText] || 'none',
      isNew: false, image: img, order: i,
      _alt: alt, // kept only for spot-checking; removed in step 4
    });
    i++;
  }
  console.log(`${cat}: ${i}`);
}
writeFileSync('data/products.json', JSON.stringify(all, null, 2));
console.log(`TOTAL: ${all.length}`);
```

- [ ] **Step 3: Run the seed script and verify counts match the baseline**

Run:
```bash
mkdir -p data && node scripts/seed-products.mjs
```
Expected: per-category counts and `TOTAL: 883` matching Step 1. If any category is off, fix the regex (a card whose markup varies) before continuing — do not proceed with lossy data.

- [ ] **Step 4: Spot-check and drop the temporary field**

Run:
```bash
node -e "const p=require('./data/products.json'); console.log(p.filter(x=>x.price==null).length+' null prices'); console.log(JSON.stringify(p[0],null,2));"
```
Expected: `0 null prices` and a well-formed first product. Then remove the `_alt` helper line from `scripts/seed-products.mjs`, re-run Step 3 so `products.json` has no `_alt`, and confirm again.

- [ ] **Step 5: Commit**

```bash
git add data/products.json scripts/seed-products.mjs
git commit -m "feat: seed data/products.json from existing catalog HTML"
```

---

### Task 2: `render-products.js` renderer + wire into one category page

Build the renderer and prove it on the smallest page (`cat-kent.html`, 18 products) before touching the rest. Also make Add-to-cart survive dynamic rendering.

**Files:**
- Create: `render-products.js`
- Modify: `shared.js` (add-to-cart delegation + reveal rescan)
- Modify: `cat-kent.html` (replace hardcoded grid with container + script)

**Interfaces:**
- Consumes: `data/products.json` (Task 1).
- Produces:
  - Global `window.UKEProducts` = `{ load(): Promise<Product[]>, cardHTML(p): string, renderGrid(container): Promise<void> }`.
  - A `products:rendered` DOM event dispatched on `document` after cards inject.
  - `shared.js` binds `.btn-add-cart` via delegation on `document` (works for injected cards).

- [ ] **Step 1: Add the renderer**

Create `render-products.js`. `cardHTML` reproduces the existing `.product-card` markup exactly, plus stock/new states.
```js
(function () {
  const TAGS = {
    bestseller: { label: 'Best seller', cls: '' },
    popular:    { label: 'Popular',     cls: '' },
    specialty:  { label: 'Specialty',   cls: ' gold-tag' },
    sale:       { label: 'Sale',        cls: '' },
  };
  const rand = (v) => 'R' + Number(v).toFixed(2);

  let cache = null;
  async function load() {
    if (cache) return cache;
    const res = await fetch('data/products.json', { cache: 'no-store' });
    if (!res.ok) throw new Error('products fetch failed: ' + res.status);
    cache = await res.json();
    return cache;
  }

  function badge(p) {
    if (p.stock === 'out-of-stock') return '<span class="product-tag oos-tag">Out of stock</span>';
    if (p.isNew) return '<span class="product-tag new-tag">New</span>';
    const t = TAGS[p.tag];
    if (p.stock === 'low-stock') return '<span class="product-tag low-tag">Low stock</span>';
    return t ? `<span class="product-tag${t.cls}">${t.label}</span>` : '';
  }

  function cardHTML(p) {
    const oos = p.stock === 'out-of-stock';
    const oldP = p.oldPrice ? `<span class="product-price-old">${rand(p.oldPrice)}</span>` : '<span class="product-price-old"></span>';
    const btn = oos
      ? '<button class="btn-add-cart" disabled aria-disabled="true">Out of stock</button>'
      : '<button class="btn-add-cart">Add to cart</button>';
    return `<div class="product-card reveal${oos ? ' is-oos' : ''}" data-id="${p.id}">`
      + `<div class="product-img-wrap">${badge(p)}<button class="product-wishlist">♡</button>`
      + `<img src="${p.image}" alt="${p.brand} ${p.name} ${p.volume}" loading="lazy" onerror="this.src='images/placeholder.png'" /></div>`
      + `<div class="product-body"><p class="product-brand">${p.brand}</p>`
      + `<h3 class="product-name">${p.name}</h3><p class="product-volume">${p.volume}</p>`
      + `<div class="product-footer"><div>${oldP}<span class="product-price">${rand(p.price)}</span></div>`
      + `${btn}</div></div></div>`;
  }

  async function renderGrid(container) {
    const cat = container.getAttribute('data-category');
    try {
      const products = (await load())
        .filter((p) => (cat ? p.category === cat : true))
        .sort((a, b) => a.order - b.order);
      container.innerHTML = products.map(cardHTML).join('');
    } catch (e) {
      console.error(e);
      container.innerHTML = '<p class="grid-error">Products temporarily unavailable. Please refresh.</p>';
      return;
    }
    document.dispatchEvent(new CustomEvent('products:rendered', { detail: { container } }));
  }

  window.UKEProducts = { load, cardHTML, renderGrid };

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-product-grid]').forEach(renderGrid);
  });
})();
```

- [ ] **Step 2: Make Add-to-cart work for injected cards (event delegation)**

In `shared.js`, find the block at ~line 243:
```js
  document.querySelectorAll('.btn-add-cart').forEach(btn => {
    btn.addEventListener('click', function(e) {
```
Replace that per-element binding with one delegated listener on `document` so cards added later still work. New code:
```js
  // Delegated so dynamically-rendered product cards work too.
  document.addEventListener('click', function (e) {
    const btn = e.target.closest('.btn-add-cart');
    if (!btn || btn.disabled) return;
    const card = btn.closest('.product-card');
    const name = card?.querySelector('.product-name')?.textContent?.trim() || 'Product';
    const price = card?.querySelector('.product-price')?.textContent?.trim() || 'R0.00';
    const img = card?.querySelector('img')?.getAttribute('src') || '';
    Cart.add(name, price, img);
  });
```
Keep whatever extra behavior the original handler had (e.g. brand/volume in the name) — fold it into this delegated version so cart items read identically.

- [ ] **Step 3: Re-scan reveals after render**

The reveal observer at ~line 213 only sees `.reveal` present at load. Refactor it into a rescan-able function and call it on `products:rendered`. In `shared.js`, wrap the observer setup so `.reveal` elements can be (re)observed:
```js
  const revealObs = new IntersectionObserver((entries) => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('visible'); revealObs.unobserve(en.target); } });
  }, { threshold: 0.1 });
  function scanReveals(root = document) { root.querySelectorAll('.reveal:not(.visible)').forEach(el => revealObs.observe(el)); }
  scanReveals();
  document.addEventListener('products:rendered', (e) => scanReveals(e.detail.container));
```
(Match the existing `visible` class name the CSS uses — verify with `grep "reveal" styles.css`; if it uses a different class, use that.)

- [ ] **Step 4: Convert `cat-kent.html` to render dynamically**

In `cat-kent.html`, replace the block of hardcoded `.product-card` divs inside the products grid with an empty container carrying the category, and ensure the scripts load. The grid wrapper currently looks like `<div class="products-grid...">...cards...</div>`. Change to:
```html
<div class="products-grid" data-product-grid data-category="kent"></div>
```
Before `</body>` (after `shared.js`), add:
```html
<script src="render-products.js"></script>
```
Add a minimal placeholder image if none exists: create `images/placeholder.png` (any small neutral image) so `onerror` never breaks.

- [ ] **Step 5: Verify in the browser**

Run the dev server (`npm run dev`) and open `http://localhost:3000/cat-kent.html`. Verify:
- 18 product cards render, visually identical to before.
- In the browser console: `document.querySelectorAll('.product-card').length` → `18`.
- Clicking **Add to cart** on a card opens the drawer with the right name/price.
- Temporarily set one product's `stock` to `"out-of-stock"` in `data/products.json`, reload: it shows the "Out of stock" badge and a disabled button. Revert the edit.

- [ ] **Step 6: Commit**

```bash
git add render-products.js shared.js cat-kent.html images/placeholder.png
git commit -m "feat: data-driven product rendering (renderer + cat-kent)"
```

---

### Task 3: Migrate the remaining 8 category pages

Apply the same swap to every other `cat-*.html`, then retire the Python generators.

**Files:**
- Modify: `cat-beers.html`, `cat-cereals.html`, `cat-cleaning.html`, `cat-colddrinks.html`, `cat-confectionery.html`, `cat-groceries.html`, `cat-hotdrinks.html`, `cat-personalcare.html`
- Delete: `generate-categories.py`, `generate-remaining.py`, `category-header.html`

**Interfaces:**
- Consumes: `window.UKEProducts`, `data/products.json`, `render-products.js` (Task 2).

- [ ] **Step 1: For each of the 8 pages, replace the hardcoded grid with a container**

In each `cat-<slug>.html`, replace the inner `.product-card` blocks of the products grid with:
```html
<div class="products-grid" data-product-grid data-category="<slug>"></div>
```
using that file's slug. **Preserve** the grid's existing class list (it may be `products-grid`, `products-grid-3`, or `products-grid-4` — keep whichever the page used) and any surrounding filter/sort UI. Add `<script src="render-products.js"></script>` before `</body>` if not already present.

- [ ] **Step 2: Verify each page's count**

For each page, with `npm run dev` running, open it and check the console count equals the Task 1 baseline for that category (e.g. confectionery → 200). Quick loop:
```bash
for c in beers cereals cleaning colddrinks confectionery groceries hotdrinks personalcare; do
  echo -n "$c expected "; grep -c product-card <(git show HEAD:cat-$c.html);
done
```
Compare each to the rendered `.product-card` count in the browser console on that page.

- [ ] **Step 3: Confirm sort dropdown still works**

On a page with the sort control (e.g. `cat-groceries.html`), change the sort dropdown; cards should reorder. (The handler at `shared.js:284` re-queries `.product-card` at change time, so it works post-render — just confirm.)

- [ ] **Step 4: Retire the generators**

```bash
git rm generate-categories.py generate-remaining.py category-header.html
```

- [ ] **Step 5: Commit**

```bash
git add cat-*.html
git commit -m "feat: migrate all category pages to data-driven rendering; retire generators"
```

---

### Task 4: Homepage featured + "New in store" strip

The homepage shows a small featured set and needs a "New in store" strip driven by `isNew`.

**Files:**
- Modify: `index.html`
- Modify: `render-products.js` (add `renderNew` helper)
- Modify: `styles.css` (only if a new-strip layout class is needed; reuse existing grid classes first)

**Interfaces:**
- Consumes: `window.UKEProducts.load`, `cardHTML`.
- Produces: `window.UKEProducts.renderNew(container, limit)` rendering `isNew` products.

- [ ] **Step 1: Add `renderNew` to `render-products.js`**

Inside the IIFE, before the `window.UKEProducts =` line:
```js
  async function renderNew(container, limit = 8) {
    try {
      const products = (await load()).filter((p) => p.isNew).slice(0, limit);
      if (!products.length) { container.closest('[data-new-section]')?.remove(); return; }
      container.innerHTML = products.map(cardHTML).join('');
    } catch (e) {
      console.error(e); container.closest('[data-new-section]')?.remove(); return;
    }
    document.dispatchEvent(new CustomEvent('products:rendered', { detail: { container } }));
  }
```
Add `renderNew` to the exported object, and in the `DOMContentLoaded` handler:
```js
    document.querySelectorAll('[data-new-grid]').forEach((el) => renderNew(el));
```

- [ ] **Step 2: Add the "New in store" section to `index.html`**

Place near the existing featured products section:
```html
<!-- EDIT: New in store — populated automatically from products flagged "New" in /admin -->
<section class="new-in-store" data-new-section>
  <div class="section-inner">
    <h2 class="section-title">New in store</h2>
    <div class="products-grid-4" data-new-grid></div>
  </div>
</section>
```
Match the section wrapper/classes used by the adjacent featured section so spacing is consistent. Ensure `render-products.js` is loaded on `index.html`.

- [ ] **Step 3: Verify**

Set `isNew: true` on 3–4 products in `data/products.json` across categories, reload `index.html`:
- The "New in store" strip shows those products with a "New" badge.
- Set all `isNew` back to `false`, reload: the whole `data-new-section` is removed (no empty strip).

- [ ] **Step 4: Commit**

```bash
git add index.html render-products.js styles.css
git commit -m "feat: New in store strip on homepage driven by isNew flag"
```

> **Known scope choice:** the homepage's existing hand-picked *featured* product cards (near the top of `index.html`) stay static in phase 1, so their prices are NOT CMS-editable. If the client wants those live too, the clean extension is a `featured` boolean on the product model + a `data-featured-grid` container rendered the same way as `renderNew` — small, additive, do it as a follow-up rather than bloating this task.

---

### Task 5: Editable site text (`data/site.json`)

Move hero copy, ticker lines, and delivery numbers into editable data so the client can change wording without code.

**Files:**
- Create: `data/site.json`
- Create: `render-site.js`
- Modify: `index.html` (mark editable text nodes with `data-site` keys + include script)

**Interfaces:**
- Consumes: `data/site.json`.
- Produces: nothing other tasks depend on (leaf feature).

- [ ] **Step 1: Create `data/site.json`**

Seed with the current copy (read the real strings from `index.html` first — hero headline/subcopy, the two ticker lines, delivery threshold/fee/radius):
```json
{
  "heroHeadline": "<current headline text>",
  "heroSubcopy": "<current subcopy text>",
  "tickerLines": ["Free delivery on orders over R1,000 in Cape Town"],
  "freeDeliveryOver": 1000,
  "flatFee": 99,
  "radiusKm": 60
}
```

- [ ] **Step 2: Add `render-site.js`**

```js
(function () {
  document.addEventListener('DOMContentLoaded', async () => {
    let data;
    try { data = await (await fetch('data/site.json', { cache: 'no-store' })).json(); }
    catch (e) { console.error('site.json load failed', e); return; }
    document.querySelectorAll('[data-site]').forEach((el) => {
      const key = el.getAttribute('data-site');
      if (data[key] != null) el.textContent = data[key];
    });
  });
})();
```

- [ ] **Step 3: Tag the editable nodes in `index.html`**

Add `data-site="heroHeadline"` etc. to the matching elements (do not remove the existing text — it stays as the fallback). Include `<script src="render-site.js"></script>` before `</body>`.

- [ ] **Step 4: Verify**

Edit `heroHeadline` in `data/site.json`, reload `index.html`: the hero headline updates to the new text.

- [ ] **Step 5: Commit**

```bash
git add data/site.json render-site.js index.html
git commit -m "feat: editable site text via data/site.json"
```

---

### Task 6: Decap CMS admin (local backend first)

Add the `/admin` panel and its config, verified with Decap's local backend before any auth is wired.

**Files:**
- Create: `admin/index.html`
- Create: `admin/config.yml`

**Interfaces:**
- Consumes: `data/products.json`, `data/site.json`, `images/products/`.
- Produces: a working editor that writes those files.

- [ ] **Step 1: Create `admin/index.html`**

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>UK Emporium — Product Admin</title>
</head>
<body>
  <script src="https://unpkg.com/decap-cms@^3.0.0/dist/decap-cms.js"></script>
</body>
</html>
```

- [ ] **Step 2: Create `admin/config.yml`**

Products as a `files`-backed list editing the single `products.json` array; site text as a single file.
```yaml
backend:
  name: git-gateway   # replaced with github backend in Task 7
  branch: main

local_backend: true   # for local testing; remove/ignore in production
media_folder: "images/products"
public_folder: "images/products"

collections:
  - name: catalog
    label: "Catalog"
    files:
      - name: products
        label: "Products"
        file: "data/products.json"
        format: json
        fields:
          - name: products
            label: "Products"
            widget: list
            summary: "{{fields.brand}} {{fields.name}} — R{{fields.price}} ({{fields.stock}})"
            fields:
              - { name: id, label: "ID (unique)", widget: string }
              - { name: name, label: "Name", widget: string }
              - { name: brand, label: "Brand", widget: string }
              - { name: volume, label: "Size / volume", widget: string, required: false }
              - name: category
                label: "Category"
                widget: select
                options: [beers, cereals, cleaning, colddrinks, confectionery, groceries, hotdrinks, kent, personalcare]
              - { name: price, label: "Price (R)", widget: number, value_type: float, min: 0 }
              - { name: oldPrice, label: "Old price (R) — optional", widget: number, value_type: float, required: false }
              - name: stock
                label: "Stock"
                widget: select
                default: in-stock
                options:
                  - { label: "In stock", value: in-stock }
                  - { label: "Low stock", value: low-stock }
                  - { label: "Out of stock", value: out-of-stock }
              - name: tag
                label: "Badge"
                widget: select
                default: none
                options: [none, bestseller, popular, specialty, sale]
              - { name: isNew, label: "New in store", widget: boolean, default: false }
              - { name: image, label: "Image", widget: image }
              - { name: order, label: "Sort order", widget: number, value_type: int, default: 999 }
      - name: site
        label: "Site text"
        file: "data/site.json"
        format: json
        fields:
          - { name: heroHeadline, label: "Hero headline", widget: string }
          - { name: heroSubcopy, label: "Hero subcopy", widget: text }
          - { name: tickerLines, label: "Ticker lines", widget: list, field: { name: line, widget: string } }
          - { name: freeDeliveryOver, label: "Free delivery over (R)", widget: number, value_type: int }
          - { name: flatFee, label: "Flat delivery fee (R)", widget: number, value_type: int }
          - { name: radiusKm, label: "Delivery radius (km)", widget: number, value_type: int }
```

- [ ] **Step 3: Verify with the local backend**

Decap's local backend lets you edit real files without auth. Run it (uses `npx`, no install):
```bash
npx decap-server
```
In a second shell keep `npm run dev` running, then open `http://localhost:3000/admin/`. Verify:
- Both collections load ("Products" and "Site text").
- Editing a product's price and clicking **Publish** changes `data/products.json` on disk (`git diff data/products.json` shows it).
- Reloading the matching category page shows the new price.
- Adding a product via the list adds an entry and it appears on its category page.

- [ ] **Step 4: Commit**

```bash
git add admin/index.html admin/config.yml
git commit -m "feat: Decap CMS admin for products and site text (local backend)"
```

---

### Task 7: Production auth — GitHub login + go-live

Wire GitHub OAuth so the client can log in at the live `/admin`. This task involves Netlify/GitHub dashboard steps that the plan documents but a person performs.

**Files:**
- Modify: `admin/config.yml`

**Interfaces:**
- Consumes: everything above.

- [ ] **Step 1: Register a GitHub OAuth app**

In GitHub → Settings → Developer settings → OAuth Apps → New OAuth App:
- Homepage URL: the live site URL.
- Authorization callback URL: the OAuth provider callback (Step 2 decides the exact value).
Record the Client ID and Client Secret.

- [ ] **Step 2: Provide an OAuth handler**

Decap's GitHub backend needs an OAuth provider to exchange the code for a token. Use one of (no build step either way):
- **Netlify + a serverless OAuth relay** (deploy an OAuth provider function to this Netlify site), or
- **A hosted OAuth relay** (e.g. an existing community Netlify OAuth provider deployment you control).
Set the GitHub OAuth app callback URL to the chosen handler's `/callback`.

- [ ] **Step 3: Point Decap at the GitHub backend**

In `admin/config.yml`, replace the `backend:` block:
```yaml
backend:
  name: github
  repo: TT8Vision/<repo-name>
  branch: main
  base_url: https://<your-oauth-handler-domain>
```
Remove or leave `local_backend: true` (it is ignored in production; keep it so local testing still works).

- [ ] **Step 4: Deploy and verify end-to-end**

Push to `main`, let Netlify deploy, then:
- Open the live `/admin`, click **Log in with GitHub**, authorize.
- Edit a product price, **Publish**.
- Confirm a commit lands on `main`, Netlify redeploys, and the live page shows the new price within ~1–2 minutes.
- Confirm a non-authorized GitHub account cannot log in (repo collaborator gating).

- [ ] **Step 5: Commit**

```bash
git add admin/config.yml
git commit -m "feat: GitHub OAuth login for production admin"
```

---

## Notes for the implementer

- **Do not push** without the client's say-so — pushing triggers the live FTP/Netlify deploy (CLAUDE.md). Tasks 1–6 are safe to build and commit locally; Task 7 is the go-live step and needs sign-off.
- Keep `.product-card` markup byte-compatible with the originals so `styles.css` needs no changes for the core cards. New states (`oos-tag`, `low-tag`, `new-tag`, `is-oos`) may need a few small style rules — add them to `styles.css` near the existing `.product-tag` rules.
- The seed script (`scripts/seed-products.mjs`) is throwaway; it can be deleted after Task 1 if preferred, but committing it documents how the data was produced.
