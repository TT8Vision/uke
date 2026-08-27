# Supabase-Backed Admin Shop Editor — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the Supabase `UKE` project the live source of truth for the shop catalogue, with invite-only admins editing products inline on the real site and RLS enforcing admin-only writes.

**Architecture:** A `public.products` table (mirroring today's 868 JSON products) is read live by every page via supabase-js. Admins sign in with a magic link; `is_admin()` + RLS gate all writes. An inline editor overlay (`js/admin-editor.js`) appears only for admins and does create/edit/delete straight against the table. Because all pages read from the one table, edits show everywhere on next load.

**Tech Stack:** Static HTML + Tailwind CDN + vanilla JS · supabase-js v2 (CDN) · Supabase Postgres + Auth + RLS · Node (ESM) for the one-time seed.

**Reference:** spec at `docs/superpowers/specs/2026-08-27-supabase-admin-shop-editor-design.md`.

**Project facts (already fetched):**
- Project ref / id: `dyifpssjebmkvpdoiyas`
- API URL: `https://dyifpssjebmkvpdoiyas.supabase.co`
- Publishable (browser-safe) key: `sb_publishable_hdC7VIEduIiPQ_Q81EZB0Q_mSYrIgtz`

**Testing note:** this repo has no unit-test runner (vitest belongs to a different project). Verification is therefore behavior-based: SQL checks via the Supabase MCP (`execute_sql`), `curl`/browser checks against `http://localhost:3000` (`npx serve . --listen 3000`), and console inspection. Each task lists the exact check and expected result.

---

## File Structure

**New files**
- `js/supabase-config.js` — creates the browser Supabase client (`window.ukeSupabase`).
- `js/admin-editor.js` — admin session detection, admin bar, inline create/edit/delete overlay. Dormant unless an admin session is present.
- `login.html` — staff-only magic-link login page.
- `scripts/build-seed-sql.mjs` — reads `data/products/*.json`, emits `scripts/seed-products.sql`.
- `scripts/seed-products.sql` — generated seed (git-ignored build artifact; regenerate any time).
- Supabase migration `create_shop_schema` (applied via MCP `apply_migration`).

**Modified files**
- `js/render-products.js` — `Catalogue.load()` reads Supabase instead of `products.json`; add `mapRow`, `Catalogue.upsertLocal`, `Catalogue.removeLocal`.
- 11 product pages (`index.html`, `shop.html`, `cat-*.html`) — add supabase-js CDN + `supabase-config.js` + `admin-editor.js` script tags.
- `.gitignore` — ignore `scripts/seed-products.sql`.
- `CLAUDE.md` — document the Supabase live-editing architecture; mark Decap deprecated.

**Unchanged (explicitly out of scope):** `data/products/*.json` (kept as backup), `data/featured-*.json`, `data/settings.json`, `admin/` (Decap), `editor/overlay.js`, `netlify.toml`.

---

## Phase 1 — Supabase schema & data

### Task 1: Create the schema (products, admins, is_admin, RLS)

**Files:**
- Supabase migration: `create_shop_schema` (via MCP `apply_migration`, project `dyifpssjebmkvpdoiyas`)

- [ ] **Step 1: Apply the migration**

Call the Supabase MCP tool `apply_migration` with `project_id="dyifpssjebmkvpdoiyas"`, `name="create_shop_schema"`, and this SQL:

```sql
create extension if not exists moddatetime schema extensions;

create sequence if not exists public.products_id_seq;

create table if not exists public.products (
  id          text primary key,
  brand       text not null,
  name        text not null,
  volume      text,
  price       numeric(10,2) not null check (price >= 0),
  old_price   numeric(10,2) check (old_price >= 0),
  sku         text,
  image       text not null,
  categories  text[] not null default '{}',
  tag         text,
  in_stock    boolean not null default true,
  is_new      boolean not null default false,
  date_added  date,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);

-- Assign uke-XXXX ids on insert when the client supplies none
create or replace function public.assign_product_id()
returns trigger language plpgsql as $$
begin
  if new.id is null or new.id = '' then
    new.id := 'uke-' || lpad(nextval('public.products_id_seq')::text, 4, '0');
  end if;
  return new;
end;
$$;

create trigger products_assign_id
  before insert on public.products
  for each row execute function public.assign_product_id();

create trigger products_set_updated_at
  before update on public.products
  for each row execute function extensions.moddatetime(updated_at);

create table if not exists public.admins (
  user_id    uuid primary key references auth.users(id) on delete cascade,
  email      text,
  created_at timestamptz not null default now()
);

-- SECURITY DEFINER bypasses RLS on admins, so no policy recursion
create or replace function public.is_admin()
returns boolean language sql security definer set search_path = public stable as $$
  select exists (select 1 from public.admins where user_id = auth.uid());
$$;

alter table public.products enable row level security;
alter table public.admins   enable row level security;

create policy products_public_read on public.products
  for select using (true);
create policy products_admin_insert on public.products
  for insert with check (public.is_admin());
create policy products_admin_update on public.products
  for update using (public.is_admin()) with check (public.is_admin());
create policy products_admin_delete on public.products
  for delete using (public.is_admin());

create policy admins_read_self on public.admins
  for select using (user_id = auth.uid());

grant execute on function public.is_admin() to anon, authenticated;
```

- [ ] **Step 2: Verify schema + RLS**

Call MCP `execute_sql` with `project_id="dyifpssjebmkvpdoiyas"`:

```sql
select
  (select count(*) from information_schema.tables
     where table_schema='public' and table_name in ('products','admins')) as tables,
  (select count(*) from pg_policies where schemaname='public') as policies,
  (select relrowsecurity from pg_class where oid='public.products'::regclass) as products_rls,
  (select relrowsecurity from pg_class where oid='public.admins'::regclass)   as admins_rls;
```

Expected: `tables=2`, `policies=5`, `products_rls=true`, `admins_rls=true`.

- [ ] **Step 3: Verify anon cannot write, public can read (RLS smoke test)**

Call MCP `execute_sql`:

```sql
set local role anon;
select public.is_admin() as is_admin;                 -- expect false
select count(*) from public.products;                 -- expect 0 (allowed, empty)
insert into public.products (brand,name,price,image)
  values ('x','x',1,'x');                              -- expect: permission denied / RLS violation
reset role;
```

Expected: `is_admin=false`, count returns `0`, and the INSERT raises a row-level-security error. (If the whole statement errors on the insert, that is the pass condition.)

---

### Task 2: Seed the 868 products

**Files:**
- Create: `scripts/build-seed-sql.mjs`
- Create (generated): `scripts/seed-products.sql`
- Modify: `.gitignore`

- [ ] **Step 1: Write the seed generator**

Create `scripts/build-seed-sql.mjs`:

```js
// Reads every data/products/*.json and emits scripts/seed-products.sql:
// chunked multi-row INSERTs plus a setval so auto-ids continue after the max.
// Field mapping: oldPrice->old_price, new->is_new, inStock->in_stock, dateAdded->date_added.
import { readdir, readFile, writeFile } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const dir = join(root, 'data', 'products');
const out = join(root, 'scripts', 'seed-products.sql');
const CHUNK = 200;

const q = (v) => v == null ? 'null' : `'${String(v).replace(/'/g, "''")}'`;
const num = (v) => (v == null || v === '') ? 'null' : Number(v);
const bool = (v) => v === true ? 'true' : 'false';
const arr = (v) => Array.isArray(v) && v.length
  ? `array[${v.map(q).join(',')}]::text[]` : `'{}'::text[]`;

const files = (await readdir(dir)).filter(f => f.endsWith('.json')).sort();
const rows = [];
for (const f of files) {
  const p = JSON.parse(await readFile(join(dir, f), 'utf8'));
  rows.push(`(${q(p.id)},${q(p.brand)},${q(p.name)},${q(p.volume)},${num(p.price)},` +
    `${num(p.oldPrice)},${q(p.sku)},${q(p.image)},${arr(p.categories)},${q(p.tag)},` +
    `${bool(p.inStock)},${bool(p.new)},${q(p.dateAdded)})`);
}

const cols = '(id,brand,name,volume,price,old_price,sku,image,categories,tag,in_stock,is_new,date_added)';
let sql = '-- generated by scripts/build-seed-sql.mjs — do not edit by hand\nbegin;\n';
for (let i = 0; i < rows.length; i += CHUNK) {
  sql += `insert into public.products ${cols} values\n` +
    rows.slice(i, i + CHUNK).join(',\n') +
    '\non conflict (id) do nothing;\n';
}
sql += `select setval('public.products_id_seq',` +
  ` (select coalesce(max((regexp_replace(id,'\\D','','g'))::int),0) from public.products));\n`;
sql += 'commit;\n';

await writeFile(out, sql, 'utf8');
console.log(`Wrote ${out} with ${rows.length} products`);
```

- [ ] **Step 2: Generate the SQL and confirm the count**

Run:
```bash
cd "C:/Users/Jonathan D Theron/uke" && node scripts/build-seed-sql.mjs
```
Expected stdout: `Wrote .../scripts/seed-products.sql with 868 products`.

- [ ] **Step 3: Ignore the generated file**

Add to `.gitignore` (new line):
```
scripts/seed-products.sql
```

- [ ] **Step 4: Apply the seed**

Read `scripts/seed-products.sql` and apply it via the Supabase MCP `execute_sql` (`project_id="dyifpssjebmkvpdoiyas"`). If the file is too large for one call, apply each `insert ... ;` chunk in sequence, then run the final `setval` statement.

_(Alternative for a human executor with the DB password: `psql "postgresql://postgres:PASSWORD@db.dyifpssjebmkvpdoiyas.supabase.co:5432/postgres" -f scripts/seed-products.sql`.)_

- [ ] **Step 5: Verify the seed**

Call MCP `execute_sql`:
```sql
select count(*) as total,
       count(*) filter (where old_price is not null) as on_sale,
       (select currval('public.products_id_seq')) as seq
  from public.products;
select id, brand, name, price, old_price, is_new, in_stock, categories
  from public.products where id = 'uke-0001';
```
Expected: `total=868`; `seq=868`; row `uke-0001` = Abbott / Abbott Ale / `84.90` / `null` / `false` / `true` / `{beers}`.

- [ ] **Step 6: Commit**

```bash
git add scripts/build-seed-sql.mjs .gitignore
git commit -m "feat(db): schema + seed generator for Supabase product catalogue"
```

---

## Phase 2 — Public pages read live from Supabase

### Task 3: Add the browser Supabase client

**Files:**
- Create: `js/supabase-config.js`

- [ ] **Step 1: Write the config**

Create `js/supabase-config.js`:

```js
/* Public Supabase client for the uke storefront.
   The publishable key is designed to ship in the browser; RLS enforces that
   only admins (public.is_admin()) can write. No service-role key here, ever. */
(function () {
  const URL = 'https://dyifpssjebmkvpdoiyas.supabase.co';
  const KEY = 'sb_publishable_hdC7VIEduIiPQ_Q81EZB0Q_mSYrIgtz';
  if (!window.supabase || !window.supabase.createClient) {
    console.error('[supabase-config] supabase-js not loaded before this script');
    return;
  }
  window.ukeSupabase = window.supabase.createClient(URL, KEY, {
    auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true },
  });
})();
```

- [ ] **Step 2: Commit**

```bash
git add js/supabase-config.js
git commit -m "feat: browser Supabase client config"
```

---

### Task 4: Read the catalogue from Supabase

**Files:**
- Modify: `js/render-products.js` (`Catalogue` object)
- Modify: `index.html`, `shop.html`, `cat-beers.html`, `cat-cereals.html`, `cat-cleaning.html`, `cat-colddrinks.html`, `cat-confectionery.html`, `cat-groceries.html`, `cat-hotdrinks.html`, `cat-kent.html`, `cat-personalcare.html`

- [ ] **Step 1: Replace `Catalogue.load` and add helpers in `js/render-products.js`**

Replace the whole `async load() { … }` method (currently lines ~24-37) with:

```js
  async load() {
    if (this.loaded) return this.products;
    const { data, error } = await window.ukeSupabase
      .from('products')
      .select('*')
      .order('id', { ascending: true });
    if (error) throw new Error(`products: ${error.message}`);
    this.products = (data || []).map(mapRow);
    this.byId = new Map(this.products.map(p => [p.id, p]));
    this.loaded = true;
    return this.products;
  },

  // Apply a local insert/update without refetching, so the editor can re-render.
  upsertLocal(p) {
    const i = this.products.findIndex(x => x.id === p.id);
    if (i === -1) this.products.push(p); else this.products[i] = p;
    this.products.sort((a, b) => String(a.id).localeCompare(String(b.id)));
    this.byId.set(p.id, p);
  },

  removeLocal(id) {
    this.products = this.products.filter(p => p.id !== id);
    this.byId.delete(id);
  },
```

Then add this helper just above `const Catalogue = {` (top of file, after the header comment):

```js
/* Map a Supabase row (snake_case) to the shape the renderer expects. */
function mapRow(r) {
  return {
    id: r.id, brand: r.brand, name: r.name, volume: r.volume,
    price: r.price, oldPrice: r.old_price, sku: r.sku, image: r.image,
    categories: r.categories || [], tag: r.tag,
    inStock: r.in_stock, new: r.is_new, dateAdded: r.date_added,
  };
}
```

_(No other part of `render-products.js` changes — every consumer already reads through `Catalogue`.)_

- [ ] **Step 2: Add the supabase-js CDN + config before `render-products.js` on all 11 product pages**

On each of the 11 files, find the line `<script src="js/render-products.js"></script>` and insert these two lines **immediately before** it:

```html
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="js/supabase-config.js"></script>
```

- [ ] **Step 3: Start the site and verify products load from Supabase**

Run:
```bash
cd "C:/Users/Jonathan D Theron/uke" && npx serve . --listen 3000 --no-clipboard
```
Open `http://localhost:3000/cat-beers.html` in the browser. Expected: beer product cards render as before. In DevTools Network, confirm a request to `dyifpssjebmkvpdoiyas.supabase.co/rest/v1/products` (200) and **no** request to `data/products.json`. Console has no errors.

- [ ] **Step 4: Verify counts still work on the homepage**

Open `http://localhost:3000/index.html`. Expected: any `data-count="total"` slot shows `868`; category strips render. Console clean.

- [ ] **Step 5: Commit**

```bash
git add js/render-products.js index.html shop.html cat-*.html
git commit -m "feat: read shop catalogue live from Supabase"
```

---

## Phase 3 — Admin auth

### Task 5: Staff magic-link login page + Supabase Auth config

**Files:**
- Create: `login.html`
- Manual: Supabase dashboard Auth settings

- [ ] **Step 1: Configure allowed redirect URLs (manual, Supabase dashboard)**

In the Supabase dashboard → **Authentication → URL Configuration**:
- **Site URL:** the production Netlify URL (e.g. `https://<your-site>.netlify.app`).
- **Redirect URLs — add:** `http://localhost:3000/**` and `https://<your-site>.netlify.app/**`.

Confirm **Authentication → Providers → Email** is enabled (default) with "Email OTP / magic link" allowed.

- [ ] **Step 2: Create `login.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="noindex" />
  <title>Staff login · uke</title>
  <link rel="stylesheet" href="styles.css" />
  <style>
    .login-wrap{max-width:420px;margin:12vh auto;padding:2rem;font-family:Inter,system-ui,sans-serif}
    .login-wrap h1{font-size:1.4rem;margin-bottom:.25rem}
    .login-wrap p{color:#555;margin-bottom:1.5rem}
    .login-wrap input{width:100%;padding:.75rem;border:1px solid #ccc;border-radius:8px;margin-bottom:1rem;font-size:1rem}
    .login-wrap button{width:100%;padding:.75rem;border:0;border-radius:8px;background:#111;color:#fff;font-size:1rem;cursor:pointer}
    .login-wrap button:disabled{opacity:.6;cursor:default}
    .login-msg{margin-top:1rem;font-size:.95rem}
    .login-msg.ok{color:#137a3c}.login-msg.err{color:#b3261e}
  </style>
</head>
<body>
  <div class="login-wrap">
    <h1>Staff login</h1>
    <p>Enter your email and we'll send you a one-time login link.</p>
    <form id="login-form">
      <input id="login-email" type="email" placeholder="you@uke.co.za" required autocomplete="email" />
      <button id="login-btn" type="submit">Send login link</button>
    </form>
    <div id="login-msg" class="login-msg" role="status"></div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <script src="js/supabase-config.js"></script>
  <script>
    const form = document.getElementById('login-form');
    const btn = document.getElementById('login-btn');
    const msg = document.getElementById('login-msg');
    // If arriving back from a magic link, a session now exists — go to the shop.
    window.ukeSupabase.auth.getSession().then(({ data }) => {
      if (data.session) window.location.replace('shop.html');
    });
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      btn.disabled = true; msg.className = 'login-msg'; msg.textContent = 'Sending…';
      const email = document.getElementById('login-email').value.trim();
      const { error } = await window.ukeSupabase.auth.signInWithOtp({
        email,
        options: { emailRedirectTo: location.origin + '/shop.html' },
      });
      if (error) { msg.className = 'login-msg err'; msg.textContent = error.message; btn.disabled = false; }
      else { msg.className = 'login-msg ok'; msg.textContent = 'Check your inbox for the login link.'; }
    });
  </script>
</body>
</html>
```

- [ ] **Step 3: Verify the link sends**

Open `http://localhost:3000/login.html`, enter your email, submit. Expected: "Check your inbox for the login link." and an email arrives. **Do not click it yet** — Task 6 seeds your admin row first (a non-admin login still works but shows no admin bar, which is the correct behavior to also verify).

- [ ] **Step 4: Commit**

```bash
git add login.html
git commit -m "feat: staff magic-link login page"
```

---

### Task 6: Admin bar (session + is_admin gate)

**Files:**
- Create: `js/admin-editor.js`
- Modify: the 11 product pages (add `<script src="js/admin-editor.js"></script>` after `render-products.js`)
- Manual: seed one admin row

- [ ] **Step 1: Create `js/admin-editor.js` (bar only for now)**

```js
/* Admin editor overlay for the uke storefront.
   Dormant for the public: it only builds UI when a signed-in user is an admin
   (public.is_admin() === true). Real write-protection is RLS; this is UX. */
(function () {
  const sb = window.ukeSupabase;
  if (!sb) { console.error('[admin-editor] no Supabase client'); return; }

  let editMode = false;

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

    document.getElementById('uke-edit-toggle').addEventListener('click', (e) => {
      editMode = !editMode;
      document.body.classList.toggle('uke-edit-mode', editMode);
      e.target.classList.toggle('on', editMode);
      e.target.textContent = `Edit mode: ${editMode ? 'on' : 'off'}`;
    });
    document.getElementById('uke-new').addEventListener('click', () => openEditor(null));
    document.getElementById('uke-logout').addEventListener('click', async () => {
      await sb.auth.signOut(); location.reload();
    });
  }

  // Click a card while in edit mode -> open its editor. (Editor form: Task 7.)
  function bindCardClicks() {
    document.addEventListener('click', (e) => {
      if (!editMode) return;
      const card = e.target.closest('.product-card');
      if (!card) return;
      e.preventDefault();
      openEditor(card.getAttribute('data-product-id'));
    });
  }

  // Placeholder until Task 7 replaces it.
  function openEditor(id) { console.log('[admin-editor] openEditor', id); }
  window.__ukeOpenEditor = openEditor; // reassigned in Task 7

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
```

- [ ] **Step 2: Add the script to the 11 product pages**

On each of the 11 files, insert immediately **after** `<script src="js/render-products.js"></script>`:

```html
<script src="js/admin-editor.js"></script>
```

- [ ] **Step 3: Verify a NON-admin sees no bar**

Click the magic link from Task 5 Step 3 (you are authenticated but not yet an admin). You land on `shop.html`. Expected: **no admin bar**; site looks normal. Confirms the `is_admin` gate.

- [ ] **Step 4: Seed your admin row (manual)**

Call MCP `execute_sql` (`project_id="dyifpssjebmkvpdoiyas"`), replacing the email with yours:
```sql
insert into public.admins (user_id, email)
select id, email from auth.users where email = 'jonathantheron34@gmail.com'
on conflict (user_id) do nothing;
select user_id, email from public.admins;
```
Expected: one row returned.

- [ ] **Step 5: Verify an ADMIN sees the bar**

Reload `http://localhost:3000/shop.html`. Expected: the dark **uke admin** bar appears at the bottom with "Edit mode: off", "＋ New product", "Log out". Toggling Edit mode outlines the product cards with a dashed border. Clicking a card logs `openEditor <id>` in the console.

- [ ] **Step 6: Commit**

```bash
git add js/admin-editor.js index.html shop.html cat-*.html
git commit -m "feat: admin bar gated by Supabase session + is_admin()"
```

---

## Phase 4 — Inline create / edit / delete

### Task 7: Edit an existing product

**Files:**
- Modify: `js/admin-editor.js` (replace the placeholder `openEditor` + add the form, save, re-render)

- [ ] **Step 1: Replace the placeholder editor with the real one**

In `js/admin-editor.js`, delete the two placeholder lines:
```js
  function openEditor(id) { console.log('[admin-editor] openEditor', id); }
  window.__ukeOpenEditor = openEditor; // reassigned in Task 7
```
and replace them with:

```js
  const CATEGORIES = [
    ['cleaning','Household Cleaning'],['groceries','Groceries'],
    ['confectionery','Confectionery'],['hotdrinks','Hot Drinks'],
    ['colddrinks','Cold Drinks'],['beers','Beers & Ales'],
    ['cereals','Cereals & Breakfast'],['personalcare','Personal Care & Beauty'],
    ['kent','Kent Hairbrushes'],
  ];
  const TAGS = ['None','Best seller','Popular','Specialty','New in','Handmade','Premium','Irish stout'];
  const val = (id) => document.getElementById(id);

  function toRow(p) {
    // camelCase editor state -> snake_case DB columns
    return {
      brand: p.brand, name: p.name, volume: p.volume || null,
      price: p.price, old_price: p.oldPrice, sku: p.sku || null, image: p.image,
      categories: p.categories, tag: p.tag, in_stock: p.inStock, is_new: p.new,
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
          `<option ${((p.tag||'None')===t)?'selected':''}>${t}</option>`).join('')}</select>
        <label>Categories</label>
        <div class="cats">${CATEGORIES.map(([v,l]) =>
          `<label><input type="checkbox" value="${v}" ${p.categories.includes(v)?'checked':''}> ${l}</label>`
        ).join('')}</div>
        <div class="flags">
          <label><input type="checkbox" id="f-instock" ${p.inStock?'checked':''}> In stock</label>
          <label><input type="checkbox" id="f-new" ${p.new?'checked':''}> New in store</label>
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

  // The insert/update .select() returns a DB row; reuse the public mapper.
  function mapEditorRow(r) {
    return {
      id: r.id, brand: r.brand, name: r.name, volume: r.volume,
      price: r.price, oldPrice: r.old_price, sku: r.sku, image: r.image,
      categories: r.categories || [], tag: r.tag,
      inStock: r.in_stock, new: r.is_new, dateAdded: r.date_added,
    };
  }

  function esc(v) {
    return v == null ? '' : String(v)
      .replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  }

  async function remove(id, backdrop) { /* implemented in Task 9 */ }
```

- [ ] **Step 2: Verify an edit persists and propagates**

With the admin bar up (`http://localhost:3000/cat-beers.html`), turn Edit mode on, click **Abbott Ale**, change price to `90.00`, Save. Expected: the card updates immediately to R90.00. Reload the page — still R90.00. Open `http://localhost:3000/shop.html` — if Abbott Ale appears in any strip there, it shows R90.00 too.

- [ ] **Step 3: Verify the write hit the DB**

Call MCP `execute_sql`:
```sql
select id, price, updated_at from public.products where id = 'uke-0001';
```
Expected: `price=90.00` and `updated_at` just now. (Reset it to `84.90` afterward if you like.)

- [ ] **Step 4: Commit**

```bash
git add js/admin-editor.js
git commit -m "feat: inline edit form writes product changes to Supabase"
```

---

### Task 8: Add a new product

**Files:**
- `js/admin-editor.js` (already wired — `＋ New product` calls `openEditor(null)`, and `save` handles the insert branch)

- [ ] **Step 1: Verify create**

Click **＋ New product**. Fill: Brand `Test`, Name `Test Product`, Price `12.50`, Image `https://via.placeholder.com/300`, tick category **Groceries**, In stock. Save. Expected: modal closes; the new card appears on `cat-groceries.html`.

- [ ] **Step 2: Verify the id was auto-assigned**

Call MCP `execute_sql`:
```sql
select id, brand, name, price, date_added from public.products
  where brand = 'Test' order by id desc limit 1;
```
Expected: one row with an id like `uke-0869` (max+1) and today's `date_added`.

- [ ] **Step 3: Verify the sequence advanced correctly**

Add a second test product the same way; expect its id to be `uke-0870`. Then delete both test products in the next task's flow (or via SQL) to keep the catalogue clean.

- [ ] **Step 4: Commit (docs only — behavior already covered by Task 7 code)**

```bash
git commit --allow-empty -m "test: verify new-product insert assigns uke-XXXX id"
```

---

### Task 9: Delete a product

**Files:**
- Modify: `js/admin-editor.js` (implement the `remove` stub)

- [ ] **Step 1: Implement `remove`**

Replace the stub:
```js
  async function remove(id, backdrop) { /* implemented in Task 9 */ }
```
with:
```js
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
```

- [ ] **Step 2: Verify delete**

Edit the `Test Product` from Task 8, click **Delete**, confirm. Expected: the card disappears from `cat-groceries.html`. Delete the second test product too.

- [ ] **Step 3: Verify the DB and that featured lists are unharmed**

Call MCP `execute_sql`:
```sql
select count(*) as total from public.products;                -- expect 868 again
select id from public.products where brand = 'Test';          -- expect 0 rows
```
Open `http://localhost:3000/index.html` and `shop.html` — featured strips still render with no console errors (the renderer skips any unknown featured id by design).

- [ ] **Step 4: Commit**

```bash
git add js/admin-editor.js
git commit -m "feat: inline delete with confirmation"
```

---

## Phase 5 — Documentation

### Task 10: Update CLAUDE.md and mark Decap deprecated

**Files:**
- Modify: `CLAUDE.md`
- Modify: `admin/config.yml` (top-of-file deprecation comment)

- [ ] **Step 1: Add an architecture note to `CLAUDE.md`**

Under the `## Stack` section, append:

```markdown
## Live shop editing (Supabase) — current model

The shop catalogue's live source of truth is the Supabase `UKE` project
(`public.products`). Public pages read it via supabase-js (publishable key,
RLS public-read). Admins sign in with a magic link; `public.admins` +
`public.is_admin()` gate all writes, enforced by RLS (only admins may
insert/update/delete). Editing happens inline on the real pages via
`js/admin-editor.js`. The service-role key never reaches the browser.

The previous Decap CMS + Netlify Identity + git-publish flow (`admin/`) is
**deprecated** — it no longer feeds the live site and is kept only as a
fallback/reference pending removal.
```

- [ ] **Step 2: Mark Decap deprecated**

At the very top of `admin/config.yml`, add:
```yaml
# DEPRECATED (2026-08-27): the live shop is now edited via Supabase
# (js/admin-editor.js). This Decap CMS no longer feeds the site. Kept for
# reference only. See CLAUDE.md "Live shop editing (Supabase)".
```

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md admin/config.yml
git commit -m "docs: document Supabase live-editing model; deprecate Decap CMS"
```

---

## Self-Review

**Spec coverage:**
- Live source of truth → Task 4 (public read). ✓
- Supabase `products` model + `admins` + `is_admin()` → Task 1. ✓
- Migrate 868 products → Task 2. ✓
- RLS (public read, admin-only write) → Task 1 (Steps 1-3). ✓
- Invite-only admins, no public signup → no signup UI; admins seeded via SQL (Task 6 Step 4). ✓
- Magic-link login → Task 5. ✓
- Inline editing of all card fields → Task 7 (all fields incl. price/old_price/brand/name/volume/image/tag/in_stock/is_new + sku). ✓
- Add / delete → Tasks 8, 9. ✓
- Propagation everywhere → Task 4 (single `Catalogue` source) + re-render via `window.renderProducts()`. ✓
- Decap deprecated, CLAUDE.md updated → Task 10. ✓
- Featured/promo stay static → untouched; verified unharmed in Task 9 Step 3. ✓

**Placeholder scan:** the only intentional stub (`remove`) is created in Task 7 and implemented in Task 9, explicitly flagged. No TBDs.

**Type consistency:** editor state is camelCase (`oldPrice`, `inStock`, `new`); `toRow()` converts to snake_case for the DB; `mapRow`/`mapEditorRow` convert DB rows back. `Catalogue.upsertLocal`/`removeLocal`/`get` and `window.renderProducts()` are all defined in Task 4 / already exist in `render-products.js`. `window.__ukeOpenEditor` from Task 6 is superseded by the real `openEditor` (same closure) in Task 7 — the placeholder line is deleted, not left dangling.
