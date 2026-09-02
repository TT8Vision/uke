# CLAUDE.md — UK Emporium (uke)

Persistent rules for this repo. Read this before every change. Do not weaken anything
under "Security invariants" unless an instruction explicitly names the rule it's changing.

## What this is
A hand-written static storefront for UK Emporium, deployed to Netlify. The product
catalogue lives in Supabase and is read at runtime by the browser. Staff sign in on the
live site and edit products inline; there is no CMS, no build step, and no server of our
own.

## Stack
- Site: hand-written HTML5 at the repo root + `styles.css` + vanilla JS. No bundler,
  no framework, no build step. Live Server / `npm run dev` compatible.
- Data: Supabase project **`uke`** (ref `xwgpaalydysfebyolern`), table `public.products`.
- Reads: `js/supabase-config.js` creates a supabase-js client with the **publishable**
  key; `js/render-products.js` queries `public.products` directly and builds the cards.
- Auth: Supabase email/password, magic link, self-serve sign-up and password reset, all
  on `login.html`.
- Editing: `js/admin-editor.js` — injects an admin bar and inline product editor, but
  only for a signed-in user for whom `public.is_admin()` returns true.
- Images: Supabase Storage, public bucket `product-images`.
- Deploy: Netlify, `publish = "."`, static, no build command.

## How editing actually works
1. A staff member clicks **Staff login** in the site footer and lands on `login.html`.
2. They sign in (password or magic link). `login.html` then calls the `is_admin` RPC.
   - Admin → redirected to `shop.html`.
   - Not an admin → told plainly that the editor stays hidden, and to ask the owner.
3. On every page, `js/admin-editor.js` runs on `DOMContentLoaded`. It calls
   `getSession()`, returns silently if there is no session, calls `is_admin()`, and
   returns silently unless it is `true`. Only then does it inject styles, the bottom
   admin bar, and the click handlers on product cards.
4. Edits write straight to `public.products` via supabase-js. RLS decides whether the
   write lands. The page updates in place; there is no publish step and no commit.

Creating an account grants **no** editing rights. Admin rights are granted separately by
inserting into `public.admins` — see `scripts/grant-admin.sql`. There is no client-side
INSERT policy on that table, so nobody can self-elevate.

## Security invariants (do not weaken)
1. **The publishable key is public by design.** It ships in `js/supabase-config.js` and
   is meant to. It is not a secret and must never be treated as one — do not try to hide
   it, proxy it, or move it to an env var. It grants exactly what RLS allows.
2. **RLS is the gate, not the UI.** `public.products` allows public SELECT and restricts
   INSERT / UPDATE / DELETE to `public.is_admin()`. Every access decision must be
   enforceable by a policy in the database. Never rely on hiding UI for protection.
3. **`is_admin()` gates the editor, and is advisory only.** `js/admin-editor.js` checks
   it to decide whether to render. That check is UX — a user who forces the bar to appear
   still cannot write, because RLS refuses. Never move an authorisation decision into the
   client.
4. **Admin rights come only from `public.admins`.** That table has no client-side INSERT
   policy. Adding an admin is a deliberate SQL action by the owner.
5. **The service-role key never enters this repo or the browser.** Not in client code,
   not in a script's source, not in a commit. `scripts/migrate-images.mjs` will use one
   from the environment if offered, but its documented path is an admin sign-in.
6. **Storage mirrors the table's rules.** Bucket `product-images` is public-read;
   insert/update/delete are gated on `public.is_admin()` — see `scripts/storage-bucket.sql`.

## Source of truth
Supabase is authoritative for the catalogue. Everything in the repo is downstream of it.

- `data/products/*.json` and `data/products.json` are a **snapshot**, refreshed by
  `npm run export:catalogue`. Nothing reads them at runtime. Do not hand-edit them; the
  next export overwrites the change. See `data/products/README.md`.
- `data/featured-shop.json` and `data/featured-index.json` are curated **reference**
  lists — ordered product ids plus presentation-only overrides (tag, gold, image,
  cardClass). A featured entry must never restate a price.
- Product ids are minted by Postgres alone: the `assign_product_id` trigger draws from
  `products_id_seq` when a client inserts without an id. **Never introduce a second
  allocator.** The retired Decap CMS was one, and two allocators sharing the `uke-####`
  namespace collide on the primary key.

## Retired — do not reinstate
- **Decap CMS + Netlify Identity + git-publish** (`admin/`). Deleted. It no longer fed
  the live site, and left reachable it let staff save edits that went nowhere. `/admin`
  and `/admin/*` 301 to `/`.
- **`editor/overlay.js`** (the TT8Editor demo/live overlay). Deleted. Its "demo" mode had
  a Publish button that wrote to `localStorage` and claimed the change was published; its
  "live" mode posted to a serverless API that does not exist here.
- **A Next.js / Vercel / Octokit publish pipeline.** Earlier revisions of this file
  described one. It was never built in this repo. There is no admin app, no route
  handler, no `GITHUB_TOKEN` and no `sites.config.json`.

`index.html` and `shop.html` still carry `data-tt8-edit` / `data-tt8-rich` attributes
(86 and 13 respectively) on their static copy. They are **inert**: the only code that
ever read them was `editor/overlay.js`, which is deleted. They are harmless markup and
are left in place as anchors should a copy editor be built later — but nothing reads
them today, and no invariant depends on them. `js/admin-editor.js` edits products, not
page copy, and ignores these attributes entirely.

## Conventions
- Audit-first: read the relevant existing files before writing. Prefer small, scoped diffs.
- Pages stay single-file and Live Server-compatible.
- Prices are numbers, formatted for display by `formatPrice` and never parsed back out of
  the DOM. Never add a `data-price` attribute — that is a second copy of price.
- One concern per commit, with a clear message.
- Scripts are dependency-free ESM using built-in `fetch`. Do not add a runtime dependency
  without a reason.
- Update this file whenever a rule or convention changes.

## Scripts
- `npm run dev` — serve the site locally on :3000.
- `npm run export:catalogue` — Supabase → `data/products/*.json` + `data/products.json`.
- `npm run build:catalogue` — the reverse, `data/products/*.json` → `data/products.json`.
  Retained because the export reuses its shape; not part of any deploy.
- `node scripts/migrate-images.mjs <download|upload|rewrite>` — move product images to
  Supabase Storage.
- `node scripts/build-seed-sql.mjs` — regenerate `scripts/seed-products.sql` (gitignored)
  from the snapshot, for loading the catalogue in the Supabase SQL editor.
- `scripts/grant-admin.sql`, `scripts/storage-bucket.sql` — run in the SQL editor.

## Test after changes
- `npm run dev`, then load `index.html` and `shop.html`: products render, no console errors.
- Signed out: no admin bar anywhere, and product cards are not clickable.
- Signed in as a non-admin: still no admin bar; `login.html` says so explicitly.
- Signed in as an admin: bar appears, edit mode outlines cards, a save persists across
  reload, and a delete removes the product.
- A non-admin write must be refused by RLS, not merely hidden.
