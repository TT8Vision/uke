# SNAPSHOT — not the source of truth

The source of truth for the product catalogue is **Supabase**
(project `xwgpaalydysfebyolern`, table `public.products`).

These files are a snapshot of that table, kept in git so the catalogue is
backed up, diffable and reviewable. **Nothing reads them at runtime** — the
site queries Supabase directly via `js/render-products.js`.

Refresh the snapshot with:

```
npm run export:catalogue
```

That rewrites every file here and regenerates `data/products.json`.

## Do not edit these files by hand

An edit here changes nothing on the site, and the next export silently
overwrites it. To change a product, sign in at `/login.html` with an admin
account and edit it inline on the page.

Editing here is also how the catalogue used to get two competing id
allocators. Product ids are minted by Supabase — the `assign_product_id`
trigger draws from `products_id_seq`. Creating a file here with a
hand-picked `uke-####` id would eventually collide with one the sequence
issues.
