/* ── Product renderer ──────────────────────────────────────────────
   Builds .product-card markup identical to the hand-written cards, so styling
   is untouched. Two kinds of container:

     <div class="products-grid" data-category="beers">        every product in a category
     <div class="products-grid-4" data-featured="shop:beers"> a curated, ordered id list

   Featured lists (data/featured-shop.json, data/featured-index.json) are
   REFERENCES, never product data. An entry may carry presentation-only
   overrides — tag, gold, image, cardClass — and nothing else.

   Pricing rule: products.json is the ONLY source of price. A featured entry may
   NOT override price (enforced below). Cards render price as display text
   derived from the JSON number; nothing ever reads that text back. The cart
   resolves price/name from the catalogue by data-product-id.
   Never add a data-price attribute — that would be a second copy of price.
   ────────────────────────────────────────────────────────────────── */

const Catalogue = {
  products: [],
  byId: new Map(),
  loaded: false,

  async load() {
    if (this.loaded) return this.products;
    const res = await fetch('data/products.json');
    if (!res.ok) throw new Error(`products.json: ${res.status} ${res.statusText}`);
    const data = await res.json();
    // Decap's file collections require an object at the root, so the catalogue is
    // stored as { products: [...] }. A bare array is still accepted.
    this.products = Array.isArray(data) ? data : (data.products || []);
    this.byId = new Map(this.products.map(p => [p.id, p]));
    this.loaded = true;
    return this.products;
  },

  get(id) {
    return this.byId.get(id) || null;
  },

  byCategory(category) {
    return this.products.filter(p => Array.isArray(p.categories) && p.categories.includes(category));
  },

  categories() {
    return [...new Set(this.products.flatMap(p => p.categories))];
  },

  // Products flagged new, newest first; ties broken by id descending so the
  // order is stable while every migrated product shares the baseline date.
  newest(limit = 8) {
    return this.products
      .filter(p => p.new === true)
      .sort((a, b) =>
        String(b.dateAdded ?? '').localeCompare(String(a.dateAdded ?? '')) ||
        String(b.id).localeCompare(String(a.id)))
      .slice(0, limit);
  },
};

// Curated id lists, loaded on demand: "shop" -> data/featured-shop.json
const Featured = {
  lists: {},

  async load(source) {
    if (!this.lists[source]) {
      const res = await fetch(`data/featured-${source}.json`);
      if (!res.ok) throw new Error(`featured-${source}.json: ${res.status}`);
      this.lists[source] = await res.json();
    }
    return this.lists[source];
  },

  // "shop:beers" -> that section's array; "index" -> the whole array
  async entries(spec) {
    const [source, key] = spec.split(':');
    const list = await this.load(source);
    const entries = key ? list[key] : list;
    if (!Array.isArray(entries)) throw new Error(`featured list "${spec}" not found`);
    return entries;
  },
};

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

/* Mirrors the existing hand-written card exactly.
   - volume: null  -> the <p class="product-volume"> element is omitted entirely
   - tag:    null  -> the <span class="product-tag"> badge is omitted entirely
   `extra` carries presentation-only overrides from a featured entry. */
function productCardHTML(p, extra = {}) {
  // A featured entry owns its badge outright: if it passes `tag` (even as null)
  // that wins, so a curated card shows no badge just because the catalogue
  // record happens to carry one. Category pages pass no `tag` and use p.tag.
  const tagText = 'tag' in extra ? extra.tag : p.tag;
  const image = extra.image || p.image;
  const cardClass = extra.cardClass ? ` ${extra.cardClass}` : '';
  const alt = escapeHtml(p.name);

  const tag = tagText
    ? `<span class="product-tag${extra.gold ? ' gold-tag' : ''}">${escapeHtml(tagText)}</span>`
    : '';
  const volume = p.volume
    ? `<p class="product-volume">${escapeHtml(p.volume)}</p>`
    : '';
  const oldPrice = p.oldPrice != null
    ? `<span class="product-price-old">${formatPrice(p.oldPrice)}</span>`
    : '';

  return `<div class="product-card${cardClass}" data-product-id="${escapeHtml(p.id)}">` +
    `<div class="product-img-wrap">${tag}` +
      `<button class="product-wishlist">&#9825;</button>` +
      `<img src="${escapeHtml(image)}" alt="${alt}" loading="lazy" />` +
    `</div>` +
    `<div class="product-body">` +
      `<p class="product-brand">${escapeHtml(p.brand)}</p>` +
      `<h3 class="product-name">${escapeHtml(p.name)}</h3>` +
      volume +
      `<div class="product-footer">` +
        `<div>${oldPrice}<span class="product-price">${formatPrice(p.price)}</span></div>` +
        `<button class="btn-add-cart">Add to cart</button>` +
      `</div>` +
    `</div>` +
  `</div>`;
}

/* Every count on the site is derived from the catalogue, never hardcoded.
   Mark a slot with data-count and the renderer fills in the number:

     data-count="total"           868  — products in the catalogue
     data-count="categories"        9  — distinct categories
     data-count="cat:colddrinks"   78  — products in one category

   Only the number is written; the surrounding wording is untouched. */
function syncCounts() {
  document.querySelectorAll('[data-count]').forEach(el => {
    const spec = el.getAttribute('data-count');
    let n;
    if (spec === 'total') n = Catalogue.products.length;
    else if (spec === 'categories') n = Catalogue.categories().length;
    else if (spec.startsWith('cat:')) n = Catalogue.byCategory(spec.slice(4)).length;
    else { console.error(`[render-products] unknown data-count "${spec}"`); return; }
    el.textContent = n;
  });
}

// Curated homepage strip of the newest products. Hides the whole section when
// nothing is flagged — no empty grid, no orphaned heading.
function renderNewStrip() {
  const grid = document.querySelector('[data-new-strip]');
  if (!grid) return;

  const limit = Number(grid.getAttribute('data-new-strip')) || 8;
  const items = Catalogue.newest(limit);
  const section = grid.closest('section') || grid.parentElement;

  if (!items.length) {
    if (section) section.hidden = true;
    grid.innerHTML = '';
    return;
  }

  grid.innerHTML = items.map(p => productCardHTML(p, { cardClass: 'reveal' })).join('');
  if (section) section.hidden = false;
}

function showError(grid) {
  grid.innerHTML = `<p class="products-error">Products could not be loaded. Please refresh the page.</p>`;
}

async function renderProducts() {
  const categoryGrids = document.querySelectorAll('[data-category]');
  const featuredGrids = document.querySelectorAll('[data-featured]');
  const newStrip = document.querySelector('[data-new-strip]');
  const countSlots = document.querySelectorAll('[data-count]');
  if (!categoryGrids.length && !featuredGrids.length && !newStrip && !countSlots.length) return;

  try {
    await Catalogue.load();
  } catch (err) {
    console.error('[render-products] could not load catalogue:', err);
    [...categoryGrids, ...featuredGrids].forEach(showError);
    if (newStrip) (newStrip.closest('section') || newStrip).hidden = true;
    return;
  }

  syncCounts();
  renderNewStrip();

  // Category pages: every product in the category, catalogue order.
  categoryGrids.forEach(grid => {
    const items = Catalogue.byCategory(grid.getAttribute('data-category'));
    grid.innerHTML = items.map(p => productCardHTML(p)).join('');
  });

  // Curated pages: an explicit ordered list of ids.
  for (const grid of featuredGrids) {
    const spec = grid.getAttribute('data-featured');
    let entries;
    try {
      entries = await Featured.entries(spec);
    } catch (err) {
      console.error(`[render-products] featured list "${spec}":`, err);
      showError(grid);
      continue;
    }

    grid.innerHTML = entries.map(entry => {
      const p = Catalogue.get(entry.id);
      if (!p) {
        console.error(`[render-products] featured list "${spec}" references unknown id ${entry.id} — skipped`);
        return '';
      }
      if ('price' in entry || 'oldPrice' in entry) {
        // A featured list must never restate a price; products.json owns it.
        console.error(`[render-products] featured entry ${entry.id} tried to override price — ignored`);
      }
      return productCardHTML(p, {
        tag: entry.tag ?? null,        // always explicit: absent in the list => no badge
        gold: entry.gold,
        image: entry.image,
        cardClass: entry.cardClass,
      });
    }).join('');
  }

  // Cart items already in localStorage are re-priced from the JSON we just
  // loaded, so a price edit reaches even a cart saved before the change.
  if (window.Cart?.repriceFromCatalogue) Cart.repriceFromCatalogue();

  document.dispatchEvent(new CustomEvent('products:rendered'));
}

// `const` at the top level of a classic script is NOT a property of window, so
// expose it explicitly — shared.js resolves cart prices via window.Catalogue.
window.Catalogue = Catalogue;
window.Featured = Featured;

document.addEventListener('DOMContentLoaded', renderProducts);
