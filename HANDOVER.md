# UK Emporium website

A static website: plain HTML, CSS and JavaScript. No database, no logins, no build
framework. The product catalogue is a set of JSON files in this folder.

## Run it locally
Requires [Node.js](https://nodejs.org) 20 or newer.

```
npm run build:catalogue   # rebuild data/products.json from data/products/
npm run dev               # serve at http://localhost:3000
```

Opening the HTML files straight from disk will not load products; use a local server.

## How products work
- Each product is one file: `data/products/uke-0001.json`, `uke-0002.json`, …
  Field meanings are in `data/products/README.md`.
- `npm run build:catalogue` combines them into `data/products.json`, which the pages
  read. Never edit `data/products.json` by hand.
- Product images live in `images/products/`, named after the product id.
- Prices are plain numbers in rand (`84.9`, not `"R84.90"`).

## Edit a product
1. Open its file in `data/products/` and change the fields (price, name, `inStock`…).
2. Run `npm run build:catalogue`.
3. Check it with `npm run dev`.
4. Commit both changed files and push:
   ```
   git add data/products
   git add data/products.json
   git commit -m "Update price of Abbott Ale"
   git push
   ```
5. Netlify rebuilds and the live site updates within a couple of minutes.

To remove a product, delete its file, rebuild, commit and push.

## Add a product
1. Find the highest existing id in `data/products/` (e.g. `uke-0868`) and use the next
   one (`uke-0869`).
2. Copy an existing file to `data/products/uke-0869.json` and edit every field. The `id`
   field must match the filename.
3. Add the image as `images/products/uke-0869.webp` (square, about 600–1600px; JPG or
   PNG work too if you use that extension in the `image` field).
4. Rebuild, check locally, commit and push as above.

## Homepage and shop highlights
`data/featured-index.json` and `data/featured-shop.json` list which product ids appear
in the curated sections, in order. They never contain prices. The promo message in the
top ticker is in `data/settings.json`.

## Hosting
Netlify settings are in `netlify.toml`: publish directory `.`, build command
`npm run build:catalogue`, plus security headers and a redirect from `/admin`.

To move to another host: any static host works (Cloudflare Pages, GitHub Pages, an
ordinary web server). Run `npm run build:catalogue`, then upload the whole folder except
`node_modules/` and `.git/`. If the host can run a build command, set it to
`npm run build:catalogue` and the publish directory to the project root. Recreate the
headers and `/admin` redirect in the new host's own config format, then point the
domain's DNS at the new host.
