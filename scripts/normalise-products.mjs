/* Rewrite every data/products/<id>.json with keys in the canonical order.
 *
 * Decap writes an entry's keys in whatever order its form state happens to hold, so a
 * CMS save reorders the file and git shows a whole-file diff for a one-price change.
 * This rewrites the same data in a fixed key order, so diffs stay honest: only the
 * fields that actually changed show up.
 *
 * Safe to run any time — it is data-preserving. It changes key ORDER and formatting
 * only, never values. build-catalogue.mjs does not depend on key order (it keys by
 * id and reorders on output), so this is purely for readable diffs.
 *
 *   npm run normalise:products
 */
import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';

const DIR = 'data/products';

// Same 13 fields, same order as split-products.mjs and build-catalogue.mjs.
const FIELDS = ['id', 'brand', 'name', 'volume', 'price', 'oldPrice', 'sku',
  'image', 'categories', 'tag', 'inStock', 'new', 'dateAdded'];

const files = (await readdir(DIR)).filter(f => f.endsWith('.json'));

let rewritten = 0;
for (const f of files) {
  const full = path.join(DIR, f);
  const before = await readFile(full, 'utf8');
  const p = JSON.parse(before);

  // The filename is the id — build-catalogue.mjs treats it as authoritative, so keep
  // the field in step with it rather than letting the two drift apart.
  const idFromName = path.basename(f, '.json');
  if (p.id !== idFromName) {
    console.warn(`[normalise] ${f}: id field "${p.id}" != filename — using filename`);
    p.id = idFromName;
  }

  const ordered = {};
  for (const field of FIELDS) ordered[field] = field in p ? p[field] : null;

  // A key the schema does not know about would be silently dropped by the rewrite —
  // and by the build. Fail loudly instead of eating data.
  const extra = Object.keys(p).filter(k => !FIELDS.includes(k));
  if (extra.length) {
    console.error(`[normalise] ${f} has unexpected fields: ${extra.join(', ')}`);
    process.exit(1);
  }

  const after = JSON.stringify(ordered, null, 2) + '\n';
  if (after !== before) {
    await writeFile(full, after);
    rewritten += 1;
  }
}

console.log(`files scanned  : ${files.length}`);
console.log(`files rewritten: ${rewritten}`);
console.log(rewritten ? '(key order normalised)' : '(all files already canonical)');
