# CLAUDE.md — TT8 Live Editor

Persistent rules for this repo. Read this before every change. Do not weaken anything
under "Security invariants" unless an instruction explicitly names the rule it's changing.

## What this is
A bounded live-editing product for TT8Vision static client sites. Clients edit **text and
images only** on their own pages; changes are committed back to each site's GitHub repo and
auto-deployed to Hostinger. Clients never touch code, deploy config, secrets, or a database.

## Stack
- Admin app: Next.js (App Router, TypeScript) on Vercel.
- Auth: Supabase email magic-link; server-side session via `@supabase/ssr`.
- Publish: Next.js Route Handler using `@octokit/rest` (GitHub Contents API) + `cheerio`
  (patching) + `jose` (JWT verify).
- Client sites: hand-written HTML5 + Tailwind CDN + vanilla JS, deployed to Hostinger via
  its native Git integration (auto-deploy on push to `main`).
- Registry: `sites.config.json` at repo root — one entry per client site.
- Editor overlay: `public/editor/overlay.js` — ships on client sites, dormant until activated.

## Live shop editing (Supabase) — current model
The shop catalogue's live source of truth is the Supabase `UKE` project
(`public.products`, ref `dyifpssjebmkvpdoiyas`). Public pages read it via
supabase-js (`js/supabase-config.js`, publishable key, RLS public-read). Admins
sign in with a magic link (`login.html`); `public.admins` + `public.is_admin()`
gate all writes, enforced by RLS (only admins may insert/update/delete). Editing
happens inline on the real pages via `js/admin-editor.js`. The service-role key
never reaches the browser. `data/products/*.json` and `data/products.json` are
retained as an offline backup but are no longer on the live read path.

The previous Decap CMS + Netlify Identity + git-publish flow (`admin/`) is
**deprecated** — it no longer feeds the live site and is kept only as a
fallback/reference pending removal.

## Security invariants (do not weaken)
1. The publish route verifies a real Supabase JWT and checks the caller's email against the
   site's `allowedEmails`. Never bypass either check except via the documented
   `ALLOW_DEV_TOKEN` path, which must be off in production.
2. Only elements that already carry `[data-tt8-edit]` may change. Unknown ids are ignored —
   never created.
3. Only pages listed in the site's registry entry may be patched. Never write arbitrary paths.
4. Text is applied as **plain text** by default (`.text()`). Rich text is allowed only on
   elements marked `data-tt8-rich`, and only through the tag allowlist
   (`b i em strong a br span`), sanitised server-side.
5. `GITHUB_TOKEN` and `SUPABASE_JWT_SECRET` are server-only. Never send them to the browser,
   inline them in client code, or log them.
6. `GITHUB_TOKEN` is a fine-grained PAT scoped to client repos only (Contents: read/write).

## Conventions
- Audit-first: read the relevant existing files before writing. Prefer small, scoped diffs.
- Client site HTML stays single-file and Live Server-compatible, with `<!-- EDIT: -->`
  markers at customisation points.
- Keep it Prettier / ESLint clean; no build-pipeline conflicts.
- One concern per commit, with a clear message.
- uke catalogue: `data/products/` (one JSON file per product) is the source of truth — that is
  what the CMS edits. `data/products.json` is **generated** by `npm run build:catalogue` and
  must never be hand-edited; a manual change there is silently overwritten by the next build.
- Update this file whenever a rule or convention changes.

## Env vars
`GITHUB_TOKEN`, `SUPABASE_JWT_SECRET`, `NEXT_PUBLIC_SUPABASE_URL`,
`NEXT_PUBLIC_SUPABASE_ANON_KEY`, `ADMIN_ORIGIN`. Dev-only: `ALLOW_DEV_TOKEN`, `DEV_TOKEN`.

## Test after changes
- `npm run build` passes.
- Publish rejects: no token, wrong email, unknown site, unknown page, unknown id.
- Publish succeeds for an allow-listed editor on a registered page, producing one commit.
