/* Admin editor overlay for the uke storefront.
   Dormant for the public: it only builds UI when a signed-in user is an admin
   (public.is_admin() === true). Real write-protection is RLS; this is UX. */
(function () {
  const sb = window.ukeSupabase;
  if (!sb) { console.error('[admin-editor] no Supabase client'); return; }

  let editMode = false;

  const CATEGORIES = [
    ['cleaning', 'Household Cleaning'], ['groceries', 'Groceries'],
    ['confectionery', 'Confectionery'], ['hotdrinks', 'Hot Drinks'],
    ['colddrinks', 'Cold Drinks'], ['beers', 'Beers & Ales'],
    ['cereals', 'Cereals & Breakfast'], ['personalcare', 'Personal Care & Beauty'],
    ['kent', 'Kent Hairbrushes'],
  ];
  const TAGS = ['None', 'Best seller', 'Popular', 'Specialty', 'New in', 'Handmade', 'Premium', 'Irish stout'];
  const val = (id) => document.getElementById(id);

  function esc(v) {
    return v == null ? '' : String(v)
      .replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function injectStyles() {
    const css = `
      #uke-admin-bar{position:fixed;left:0;right:0;bottom:0;z-index:9999;display:flex;
        gap:.75rem;align-items:center;padding:.6rem 1rem;background:#111;color:#fff;
        font-family:Inter,system-ui,sans-serif;font-size:.9rem}
      #uke-admin-bar .spacer{flex:1}
      #uke-admin-bar button{border:0;border-radius:6px;padding:.45rem .8rem;cursor:pointer;font-size:.9rem}
      #uke-admin-bar .toggle{background:#2563eb;color:#fff}
      #uke-admin-bar .toggle.on{background:#16a34a}
      #uke-admin-bar .ghost{background:#333;color:#fff}
      body.uke-edit-mode .product-card{outline:2px dashed #2563eb;cursor:pointer;position:relative}
      body.uke-edit-mode{padding-bottom:56px}
      .uke-modal-backdrop{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:10000;
        display:flex;align-items:center;justify-content:center;padding:1rem}
      .uke-modal{background:#fff;color:#111;border-radius:12px;max-width:460px;width:100%;
        max-height:90vh;overflow:auto;padding:1.25rem;font-family:Inter,system-ui,sans-serif}
      .uke-modal h2{font-size:1.1rem;margin-bottom:1rem}
      .uke-modal label{display:block;font-size:.8rem;color:#444;margin:.6rem 0 .2rem}
      .uke-modal input[type=text],.uke-modal input[type=number],.uke-modal select{
        width:100%;padding:.5rem;border:1px solid #ccc;border-radius:6px;font-size:.95rem}
      .uke-modal .cats{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.3rem}
      .uke-modal .cats label{display:flex;align-items:center;gap:.3rem;margin:0;font-size:.85rem}
      .uke-modal .row{display:flex;gap:1rem}.uke-modal .row>div{flex:1}
      .uke-modal .flags{display:flex;gap:1.2rem;margin-top:.7rem}
      .uke-modal .flags label{display:flex;align-items:center;gap:.4rem;margin:0}
      .uke-actions{display:flex;gap:.6rem;margin-top:1.2rem}
      .uke-actions .save{background:#16a34a;color:#fff}
      .uke-actions .cancel{background:#eee;color:#111}
      .uke-actions .delete{background:#b3261e;color:#fff;margin-left:auto}
      .uke-actions button{border:0;border-radius:6px;padding:.55rem .9rem;cursor:pointer}
      .uke-modal .err{color:#b3261e;font-size:.85rem;margin-top:.6rem;min-height:1em}`;
    const s = document.createElement('style'); s.textContent = css; document.head.appendChild(s);
  }

  function buildBar() {
    const bar = document.createElement('div');
    bar.id = 'uke-admin-bar';
    bar.innerHTML =
      `<strong>uke admin</strong>` +
      `<button class="toggle" id="uke-edit-toggle">Edit mode: off</button>` +
      `<button class="ghost" id="uke-new">＋ New product</button>` +
      `<span class="spacer"></span>` +
      `<button class="ghost" id="uke-logout">Log out</button>`;
    document.body.appendChild(bar);

    val('uke-edit-toggle').addEventListener('click', (e) => {
      editMode = !editMode;
      document.body.classList.toggle('uke-edit-mode', editMode);
      e.target.classList.toggle('on', editMode);
      e.target.textContent = `Edit mode: ${editMode ? 'on' : 'off'}`;
    });
    val('uke-new').addEventListener('click', () => openEditor(null));
    val('uke-logout').addEventListener('click', async () => {
      await sb.auth.signOut(); location.reload();
    });
  }

  // Click a card while in edit mode -> open its editor.
  function bindCardClicks() {
    document.addEventListener('click', (e) => {
      if (!editMode) return;
      const card = e.target.closest('.product-card');
      if (!card) return;
      e.preventDefault();
      openEditor(card.getAttribute('data-product-id'));
    });
  }

  // camelCase editor state -> snake_case DB columns
  function toRow(p) {
    return {
      brand: p.brand, name: p.name, volume: p.volume || null,
      price: p.price, old_price: p.oldPrice, sku: p.sku || null, image: p.image,
      categories: p.categories, tag: p.tag, in_stock: p.inStock, is_new: p.new,
    };
  }

  // A DB row (from .select()) -> the renderer's shape.
  function mapEditorRow(r) {
    return {
      id: r.id, brand: r.brand, name: r.name, volume: r.volume,
      price: r.price, oldPrice: r.old_price, sku: r.sku, image: r.image,
      categories: r.categories || [], tag: r.tag,
      inStock: r.in_stock, new: r.is_new, dateAdded: r.date_added,
    };
  }

  function openEditor(id) {
    const existing = id ? window.Catalogue.get(id) : null;
    const p = existing || { categories: [], inStock: true, new: false, tag: null };

    const backdrop = document.createElement('div');
    backdrop.className = 'uke-modal-backdrop';
    backdrop.innerHTML = `
      <div class="uke-modal">
        <h2>${existing ? 'Edit product' : 'New product'}</h2>
        <div class="row">
          <div><label>Brand</label><input type="text" id="f-brand" value="${esc(p.brand)}"></div>
          <div><label>Volume / size</label><input type="text" id="f-volume" value="${esc(p.volume)}"></div>
        </div>
        <label>Name</label><input type="text" id="f-name" value="${esc(p.name)}">
        <div class="row">
          <div><label>Price (R)</label><input type="number" step="0.01" min="0" id="f-price" value="${p.price ?? ''}"></div>
          <div><label>Was-price (blank = no sale)</label><input type="number" step="0.01" min="0" id="f-old" value="${p.oldPrice ?? ''}"></div>
        </div>
        <label>Image URL</label><input type="text" id="f-image" value="${esc(p.image)}">
        <label>SKU (optional)</label><input type="text" id="f-sku" value="${esc(p.sku)}">
        <label>Badge</label>
        <select id="f-tag">${TAGS.map(t =>
          `<option ${((p.tag || 'None') === t) ? 'selected' : ''}>${t}</option>`).join('')}</select>
        <label>Categories</label>
        <div class="cats">${CATEGORIES.map(([v, l]) =>
          `<label><input type="checkbox" value="${v}" ${p.categories.includes(v) ? 'checked' : ''}> ${l}</label>`
        ).join('')}</div>
        <div class="flags">
          <label><input type="checkbox" id="f-instock" ${p.inStock ? 'checked' : ''}> In stock</label>
          <label><input type="checkbox" id="f-new" ${p.new ? 'checked' : ''}> New in store</label>
        </div>
        <div class="err" id="f-err"></div>
        <div class="uke-actions">
          <button class="save" id="f-save">Save</button>
          <button class="cancel" id="f-cancel">Cancel</button>
          ${existing ? '<button class="delete" id="f-delete">Delete</button>' : ''}
        </div>
      </div>`;
    document.body.appendChild(backdrop);

    backdrop.addEventListener('click', (e) => { if (e.target === backdrop) backdrop.remove(); });
    val('f-cancel').addEventListener('click', () => backdrop.remove());
    val('f-save').addEventListener('click', () => save(id, backdrop));
    if (existing) val('f-delete').addEventListener('click', () => remove(id, backdrop));
  }

  function readForm() {
    const cats = [...document.querySelectorAll('.uke-modal .cats input:checked')].map(c => c.value);
    const tag = val('f-tag').value;
    const oldRaw = val('f-old').value.trim();
    return {
      brand: val('f-brand').value.trim(),
      name: val('f-name').value.trim(),
      volume: val('f-volume').value.trim() || null,
      price: Number(val('f-price').value),
      oldPrice: oldRaw === '' ? null : Number(oldRaw),
      sku: val('f-sku').value.trim() || null,
      image: val('f-image').value.trim(),
      categories: cats,
      tag: tag === 'None' ? null : tag,
      inStock: val('f-instock').checked,
      new: val('f-new').checked,
    };
  }

  function validate(p) {
    if (!p.brand) return 'Brand is required.';
    if (!p.name) return 'Name is required.';
    if (!p.image) return 'Image URL is required.';
    if (!(p.price >= 0)) return 'Price must be a number ≥ 0.';
    if (!p.categories.length) return 'Pick at least one category.';
    return null;
  }

  async function save(id, backdrop) {
    const p = readForm();
    const err = validate(p);
    const errBox = val('f-err');
    if (err) { errBox.textContent = err; return; }
    val('f-save').disabled = true; errBox.textContent = '';

    if (id) {
      const { data, error } = await sb.from('products').update(toRow(p)).eq('id', id).select().single();
      if (error) { errBox.textContent = error.message; val('f-save').disabled = false; return; }
      window.Catalogue.upsertLocal(mapEditorRow(data));
    } else {
      const row = { ...toRow(p), date_added: new Date().toISOString().slice(0, 10) };
      const { data, error } = await sb.from('products').insert(row).select().single();
      if (error) { errBox.textContent = error.message; val('f-save').disabled = false; return; }
      window.Catalogue.upsertLocal(mapEditorRow(data));
    }
    backdrop.remove();
    window.renderProducts();
  }

  async function remove(id, backdrop) {
    const p = window.Catalogue.get(id);
    const label = p ? `${p.brand} ${p.name}` : id;
    if (!window.confirm(`Delete "${label}"? This cannot be undone.`)) return;
    const errBox = val('f-err'); errBox.textContent = '';
    const { error } = await sb.from('products').delete().eq('id', id);
    if (error) { errBox.textContent = error.message; return; }
    window.Catalogue.removeLocal(id);
    backdrop.remove();
    window.renderProducts();
  }

  async function init() {
    const { data: { session } } = await sb.auth.getSession();
    if (!session) return;
    const { data: isAdmin, error } = await sb.rpc('is_admin');
    if (error) { console.error('[admin-editor] is_admin failed', error); return; }
    if (isAdmin !== true) return;
    injectStyles();
    buildBar();
    bindCardClicks();
  }

  document.addEventListener('DOMContentLoaded', init);
})();
