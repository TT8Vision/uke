// Move the product catalogue's images off the legacy uke.co.za WordPress site and
// into Supabase Storage, so the catalogue no longer depends on a host that is
// being decommissioned.
//
// Three stages, run in order. Each is idempotent and resumable — re-running skips
// work already done, so a partial run can simply be repeated.
//
//   node scripts/migrate-images.mjs download   remote/local image -> .cache/product-images/
//   node scripts/migrate-images.mjs upload     .cache/product-images/ -> Supabase Storage
//   node scripts/migrate-images.mjs rewrite    data/products/*.json image -> storage URL
//
// `download` needs no credentials. `upload` needs an admin identity, because the
// bucket's RLS gates writes on public.is_admin() (see scripts/storage-bucket.sql,
// which must be applied first). Supply either:
//
//   UKE_ADMIN_EMAIL + UKE_ADMIN_PASSWORD   an account listed in public.admins
//   SUPABASE_SERVICE_ROLE_KEY              bypasses RLS; never commit or ship this
//
// After `rewrite`, regenerate the seed: node scripts/build-seed-sql.mjs

import { readdir, readFile, writeFile, mkdir, stat } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const SUPABASE_URL = 'https://xwgpaalydysfebyolern.supabase.co';
const PUBLISHABLE_KEY = 'sb_publishable_bO3j0H1obZi7Db8AAHUKfA_H-g_EXa9';
const BUCKET = 'product-images';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const productsDir = join(root, 'data', 'products');
const cacheDir = join(root, '.cache', 'product-images');
const manifestPath = join(cacheDir, 'manifest.json');
const failuresPath = join(cacheDir, 'failures.json');

// Concurrency is deliberately modest: the legacy host is a small WordPress box,
// and Node's fetch has been unstable here at higher fan-out.
const DOWNLOAD_CONCURRENCY = 8;
const UPLOAD_CONCURRENCY = 6;
const TIMEOUT_MS = 30000;
const RETRIES = 3;

const EXT_BY_MIME = {
  'image/jpeg': 'jpg',
  'image/png': 'png',
  'image/webp': 'webp',
  'image/avif': 'avif',
  'image/gif': 'gif',
};
const MIME_BY_EXT = {
  jpg: 'image/jpeg',
  jpeg: 'image/jpeg',
  png: 'image/png',
  webp: 'image/webp',
  avif: 'image/avif',
  gif: 'image/gif',
};

const publicUrl = (object) =>
  `${SUPABASE_URL}/storage/v1/object/public/${BUCKET}/${object}`;

/* ── shared helpers ─────────────────────────────────────────────── */

async function readProducts() {
  const files = (await readdir(productsDir)).filter((f) => f.endsWith('.json')).sort();
  const products = [];
  for (const file of files) {
    const path = join(productsDir, file);
    products.push({ file, path, data: JSON.parse(await readFile(path, 'utf8')) });
  }
  return products;
}

async function readJsonIfPresent(path, fallback) {
  try {
    return JSON.parse(await readFile(path, 'utf8'));
  } catch (err) {
    if (err.code === 'ENOENT') return fallback;
    throw err;
  }
}

function extFromUrl(url) {
  const match = url.split('?')[0].match(/\.([a-zA-Z0-9]+)$/);
  if (!match) return null;
  const ext = match[1].toLowerCase();
  return ext === 'jpeg' ? 'jpg' : ext;
}

// A bounded worker pool. Returns once every task has settled.
async function pool(items, concurrency, handler) {
  let cursor = 0;
  const workers = Array.from({ length: Math.min(concurrency, items.length) }, async () => {
    while (cursor < items.length) {
      const index = cursor++;
      await handler(items[index], index);
    }
  });
  await Promise.all(workers);
}

// fetch with an explicit timeout. AbortSignal.timeout leaks timers badly enough
// on Node 24 to crash the process at scale, so the timer is cleared by hand.
async function fetchWithTimeout(url, options = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);
  try {
    return await fetch(url, { ...options, signal: controller.signal });
  } finally {
    clearTimeout(timer);
  }
}

async function withRetries(label, fn) {
  let lastError;
  for (let attempt = 1; attempt <= RETRIES; attempt++) {
    try {
      return await fn(attempt);
    } catch (err) {
      lastError = err;
      if (attempt < RETRIES) {
        await new Promise((r) => setTimeout(r, 400 * 2 ** (attempt - 1)));
      }
    }
  }
  throw new Error(`${label}: ${lastError?.message || lastError}`);
}

class Progress {
  constructor(total, label) {
    this.total = total;
    this.label = label;
    this.done = 0;
    this.failed = 0;
  }
  tick(ok) {
    this.done++;
    if (!ok) this.failed++;
    if (this.done % 25 === 0 || this.done === this.total) {
      const failed = this.failed ? `, ${this.failed} failed` : '';
      console.log(`  ${this.label} ${this.done}/${this.total}${failed}`);
    }
  }
}

/* ── stage: download ────────────────────────────────────────────── */

async function download() {
  await mkdir(cacheDir, { recursive: true });
  const products = await readProducts();
  const manifest = await readJsonIfPresent(manifestPath, {});
  const failures = [];

  // Anything already in the manifest with a file on disk is done.
  const pending = [];
  for (const { data } of products) {
    const source = data.image;
    if (!source) {
      failures.push({ id: data.id, source: null, error: 'product has no image field' });
      continue;
    }
    const entry = manifest[data.id];
    if (entry && entry.source === source) {
      try {
        await stat(join(cacheDir, entry.object));
        continue; // cached and current
      } catch {
        /* file vanished — fall through and re-fetch */
      }
    }
    pending.push({ id: data.id, source });
  }

  const cached = products.length - pending.length - failures.length;
  console.log(`download: ${products.length} products, ${cached} already cached, ${pending.length} to fetch`);
  const progress = new Progress(pending.length, 'fetched');

  await pool(pending, DOWNLOAD_CONCURRENCY, async ({ id, source }) => {
    try {
      let bytes;
      let contentType = null;

      if (/^https?:\/\//i.test(source)) {
        const res = await withRetries(`${id} ${source}`, async () => {
          const r = await fetchWithTimeout(source, { redirect: 'follow' });
          if (!r.ok) throw new Error(`HTTP ${r.status}`);
          return r;
        });
        contentType = (res.headers.get('content-type') || '').split(';')[0].trim() || null;
        bytes = Buffer.from(await res.arrayBuffer());
      } else {
        // A repo-relative path, e.g. images/products/foo.png
        bytes = await readFile(join(root, source));
      }

      if (!bytes.length) throw new Error('empty response body');

      // Prefer the server's content-type; fall back to the URL's extension.
      let ext = EXT_BY_MIME[contentType] || extFromUrl(source);
      if (!ext) throw new Error(`cannot determine image type (content-type: ${contentType})`);
      if (!MIME_BY_EXT[ext]) throw new Error(`unsupported image type: ${ext}`);

      const object = `${id}.${ext}`;
      await writeFile(join(cacheDir, object), bytes);
      manifest[id] = {
        object,
        source,
        bytes: bytes.length,
        contentType: MIME_BY_EXT[ext],
        uploaded: false,
      };
      progress.tick(true);
    } catch (err) {
      failures.push({ id, source, error: String(err.message || err) });
      progress.tick(false);
    }
  });

  await writeFile(manifestPath, JSON.stringify(manifest, null, 2) + '\n');
  await writeFile(failuresPath, JSON.stringify(failures, null, 2) + '\n');

  const total = Object.values(manifest).reduce((sum, e) => sum + e.bytes, 0);
  console.log(`\ndownload complete: ${Object.keys(manifest).length} cached (${(total / 1048576).toFixed(1)} MB)`);
  if (failures.length) {
    console.log(`${failures.length} FAILED — see ${failuresPath}`);
    for (const f of failures.slice(0, 20)) console.log(`  ${f.id}  ${f.error}  ${f.source ?? ''}`);
    if (failures.length > 20) console.log(`  ...and ${failures.length - 20} more`);
    process.exitCode = 1;
  }
}

/* ── stage: upload ──────────────────────────────────────────────── */

// Returns the headers that authorise a storage write.
async function storageAuth() {
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (serviceKey) {
    console.log('auth: SUPABASE_SERVICE_ROLE_KEY (bypasses RLS)');
    return { apikey: serviceKey, Authorization: `Bearer ${serviceKey}` };
  }

  const email = process.env.UKE_ADMIN_EMAIL;
  const password = process.env.UKE_ADMIN_PASSWORD;
  if (!email || !password) {
    throw new Error(
      'no credentials: set UKE_ADMIN_EMAIL and UKE_ADMIN_PASSWORD (an account in ' +
        'public.admins), or SUPABASE_SERVICE_ROLE_KEY',
    );
  }

  const res = await fetchWithTimeout(`${SUPABASE_URL}/auth/v1/token?grant_type=password`, {
    method: 'POST',
    headers: { apikey: PUBLISHABLE_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  });
  if (!res.ok) throw new Error(`sign-in failed: HTTP ${res.status} ${await res.text()}`);
  const { access_token: token } = await res.json();
  if (!token) throw new Error('sign-in returned no access token');

  // Fail loudly now rather than on 867 individual 403s.
  const check = await fetchWithTimeout(`${SUPABASE_URL}/rest/v1/rpc/is_admin`, {
    method: 'POST',
    headers: {
      apikey: PUBLISHABLE_KEY,
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: '{}',
  });
  if ((await check.text()).trim() !== 'true') {
    throw new Error(`${email} signed in but is not in public.admins — grant admin first`);
  }
  console.log(`auth: signed in as ${email} (admin confirmed)`);
  return { apikey: PUBLISHABLE_KEY, Authorization: `Bearer ${token}` };
}

async function upload() {
  const manifest = await readJsonIfPresent(manifestPath, null);
  if (!manifest) throw new Error(`no manifest at ${manifestPath} — run the download stage first`);

  const auth = await storageAuth();
  const entries = Object.entries(manifest);
  const pending = entries.filter(([, e]) => !e.uploaded);
  console.log(`upload: ${entries.length} images, ${entries.length - pending.length} already uploaded, ${pending.length} to send`);

  const progress = new Progress(pending.length, 'uploaded');
  const failures = [];

  await pool(pending, UPLOAD_CONCURRENCY, async ([id, entry]) => {
    try {
      const body = await readFile(join(cacheDir, entry.object));
      await withRetries(`${id} upload`, async () => {
        const res = await fetchWithTimeout(
          `${SUPABASE_URL}/storage/v1/object/${BUCKET}/${entry.object}`,
          {
            method: 'POST',
            headers: {
              ...auth,
              'Content-Type': entry.contentType,
              'Cache-Control': 'public, max-age=31536000, immutable',
              'x-upsert': 'true',
            },
            body,
          },
        );
        if (!res.ok) throw new Error(`HTTP ${res.status} ${(await res.text()).slice(0, 200)}`);
      });
      entry.uploaded = true;
      progress.tick(true);
    } catch (err) {
      failures.push({ id, object: entry.object, error: String(err.message || err) });
      progress.tick(false);
    }
  });

  await writeFile(manifestPath, JSON.stringify(manifest, null, 2) + '\n');
  const uploaded = entries.filter(([, e]) => e.uploaded).length;
  console.log(`\nupload complete: ${uploaded}/${entries.length} objects in ${BUCKET}`);
  if (failures.length) {
    console.log(`${failures.length} FAILED:`);
    for (const f of failures.slice(0, 20)) console.log(`  ${f.id}  ${f.error}`);
    process.exitCode = 1;
  }
}

/* ── stage: rewrite ─────────────────────────────────────────────── */

async function rewrite() {
  const manifest = await readJsonIfPresent(manifestPath, null);
  if (!manifest) throw new Error(`no manifest at ${manifestPath} — run the download stage first`);

  const notUploaded = Object.entries(manifest).filter(([, e]) => !e.uploaded);
  if (notUploaded.length) {
    throw new Error(
      `${notUploaded.length} images are cached but not uploaded — run the upload stage first, ` +
        'or the rewritten URLs would 404',
    );
  }

  const products = await readProducts();
  const missing = [];
  let changed = 0;

  for (const { path, data } of products) {
    const entry = manifest[data.id];
    if (!entry) {
      missing.push(data.id);
      continue;
    }
    const url = publicUrl(entry.object);
    if (data.image === url) continue;
    data.image = url;
    // JSON.stringify preserves the parsed key order, so each file keeps its own.
    await writeFile(path, JSON.stringify(data, null, 2) + '\n');
    changed++;
  }

  console.log(`rewrite complete: ${changed} product files updated, ${products.length - changed} already current`);
  if (missing.length) {
    console.log(`${missing.length} products have no cached image and were left untouched:`);
    for (const id of missing.slice(0, 20)) console.log(`  ${id}`);
    process.exitCode = 1;
  } else {
    console.log('\nNext: node scripts/build-seed-sql.mjs');
  }
}

/* ── entry point ────────────────────────────────────────────────── */

const stages = { download, upload, rewrite };
const stage = process.argv[2];
if (!stages[stage]) {
  console.error(`usage: node scripts/migrate-images.mjs <${Object.keys(stages).join('|')}>`);
  process.exit(2);
}
await stages[stage]();
