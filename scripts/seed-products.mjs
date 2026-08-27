// One-time seed: load data/products/*.json into Supabase public.products via the
// REST API in batches. Field mapping: oldPrice->old_price, new->is_new,
// inStock->in_stock, dateAdded->date_added. Uses the publishable key; run only
// while RLS is temporarily disabled on products (see the plan), then re-enable.
import { readdir, readFile } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const URL = 'https://dyifpssjebmkvpdoiyas.supabase.co';
const KEY = 'sb_publishable_hdC7VIEduIiPQ_Q81EZB0Q_mSYrIgtz';
const BATCH = 500;

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const dir = join(root, 'data', 'products');

const files = (await readdir(dir)).filter(f => f.endsWith('.json')).sort();
const rows = [];
for (const f of files) {
  const p = JSON.parse(await readFile(join(dir, f), 'utf8'));
  rows.push({
    id: p.id, brand: p.brand, name: p.name, volume: p.volume ?? null,
    price: p.price, old_price: p.oldPrice ?? null, sku: p.sku ?? null,
    image: p.image, categories: Array.isArray(p.categories) ? p.categories : [],
    tag: p.tag ?? null, in_stock: p.inStock !== false, is_new: p.new === true,
    date_added: p.dateAdded ?? null,
  });
}

let done = 0;
for (let i = 0; i < rows.length; i += BATCH) {
  const batch = rows.slice(i, i + BATCH);
  const res = await fetch(`${URL}/rest/v1/products`, {
    method: 'POST',
    headers: {
      apikey: KEY,
      Authorization: `Bearer ${KEY}`,
      'Content-Type': 'application/json',
      Prefer: 'return=minimal,resolution=ignore-duplicates',
    },
    body: JSON.stringify(batch),
  });
  if (!res.ok) {
    console.error(`Batch ${i}-${i + batch.length} failed: ${res.status} ${await res.text()}`);
    process.exit(1);
  }
  done += batch.length;
  console.log(`inserted ${done}/${rows.length}`);
}
console.log(`Done: ${done} products.`);
