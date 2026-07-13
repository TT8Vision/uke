/* One-time migration: data/products.json -> data/products/<id>.json (one file per product).
 *
 * This runs ONCE, to seed the folder collection from the trusted single source. After
 * this, the per-product files become the source of truth and build-catalogue.mjs
 * regenerates products.json from them. Re-running this would overwrite per-product
 * edits with whatever is in products.json, so it is deliberately not an npm script.
 *
 *   node scripts/split-products.mjs
 */
import { readFile, writeFile, mkdir, readdir } from 'node:fs/promises';
import path from 'node:path';

const SRC = 'data/products.json';
const OUT = 'data/products';

// Canonical field order — every emitted file writes these 13 keys in this order, so a
// file is diffable and Decap round-trips it without reshuffling.
const FIELDS = ['id', 'brand', 'name', 'volume', 'price', 'oldPrice', 'sku',
  'image', 'categories', 'tag', 'inStock', 'new', 'dateAdded'];

const raw = JSON.parse(await readFile(SRC, 'utf8'));
const products = Array.isArray(raw) ? raw : raw.products;

await mkdir(OUT, { recursive: true });

let written = 0;
for (const p of products) {
  if (!/^uke-\d{4}$/.test(p.id ?? '')) throw new Error(`bad id: ${JSON.stringify(p.id)}`);

  const ordered = {};
  for (const f of FIELDS) {
    if (!(f in p)) throw new Error(`${p.id} is missing field "${f}"`);
    ordered[f] = p[f];
  }
  const extra = Object.keys(p).filter(k => !FIELDS.includes(k));
  if (extra.length) throw new Error(`${p.id} has unexpected fields: ${extra.join(', ')}`);

  await writeFile(path.join(OUT, `${p.id}.json`), JSON.stringify(ordered, null, 2) + '\n');
  written += 1;
}

const onDisk = (await readdir(OUT)).filter(f => f.endsWith('.json'));
console.log(`source records : ${products.length}`);
console.log(`files written  : ${written}`);
console.log(`files on disk  : ${onDisk.length}`);
if (written !== products.length || onDisk.length !== products.length) {
  console.error('MISMATCH — file count does not equal source record count');
  process.exit(1);
}
