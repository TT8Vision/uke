-- Product image storage for the uke catalogue.
-- Apply once in the Supabase SQL editor (project xwgpaalydysfebyolern).
--
-- Read is public: the storefront is anonymous, and a public bucket serves images
-- straight from the CDN without a token. Writes are gated by public.is_admin() —
-- the same predicate that gates public.products — so the only people who can add,
-- replace or remove a product image are the same people who can edit a product.
-- No service-role key is needed by anything that ships to a browser.

insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values (
  'product-images',
  'product-images',
  true,
  10485760, -- 10 MB; catalogue images are 600x600 and come in far under this
  array['image/jpeg', 'image/png', 'image/webp', 'image/avif', 'image/gif']
)
on conflict (id) do update
  set public            = excluded.public,
      file_size_limit   = excluded.file_size_limit,
      allowed_mime_types = excluded.allowed_mime_types;

-- Anyone may read an object in this bucket.
drop policy if exists product_images_public_read on storage.objects;
create policy product_images_public_read on storage.objects
  for select
  using (bucket_id = 'product-images');

-- Only admins may create, replace or delete one.
drop policy if exists product_images_admin_insert on storage.objects;
create policy product_images_admin_insert on storage.objects
  for insert
  with check (bucket_id = 'product-images' and public.is_admin());

drop policy if exists product_images_admin_update on storage.objects;
create policy product_images_admin_update on storage.objects
  for update
  using (bucket_id = 'product-images' and public.is_admin())
  with check (bucket_id = 'product-images' and public.is_admin());

drop policy if exists product_images_admin_delete on storage.objects;
create policy product_images_admin_delete on storage.objects
  for delete
  using (bucket_id = 'product-images' and public.is_admin());
