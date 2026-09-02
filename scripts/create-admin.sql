-- Create a staff account and grant it admin rights, in one step.
--
-- Run this in the Supabase SQL editor for project xwgpaalydysfebyolern.
--
-- EDIT THE TWO VALUES ON THE MARKED LINES BELOW, then run the whole file.
-- Keep the single quotes. Do not wrap the password in angle brackets or any
-- other punctuation — whatever is between the quotes becomes the password,
-- character for character.
--
-- Safe to re-run. If the account already exists this resets its password and
-- leaves everything else alone, so it doubles as a password reset.
--
-- Admin rights are what public.is_admin() checks, and RLS on public.products
-- and the product-images bucket is what enforces them. Granting admin here
-- gives the account full write access to the catalogue — do not hand it out
-- casually, and give it a long, random password.

do $$
declare
  v_email    text := lower('EDIT-ME@example.com');  -- <<< the account's email
  v_password text := 'EDIT-ME-a-long-random-password'; -- <<< the account's password
  v_id       uuid;
begin
  if v_email like 'edit-me@%' or v_password like 'EDIT-ME-%' then
    raise exception 'Set v_email and v_password at the top of this script first.';
  end if;

  select id into v_id from auth.users where lower(email) = v_email;

  if v_id is null then
    v_id := gen_random_uuid();

    -- Shape mirrors what GoTrue itself writes for an email signup: a confirmed
    -- account on the email provider, with a bcrypt password hash.
    --
    -- The token columns must be '' and never NULL. GoTrue scans them into a
    -- non-nullable Go string, so a NULL makes every sign-in fail with
    -- HTTP 500 "Database error querying schema" — which looks like a server
    -- fault, not a bad row. They are set explicitly for that reason.
    insert into auth.users (
      instance_id, id, aud, role, email, encrypted_password,
      email_confirmed_at, raw_app_meta_data, raw_user_meta_data,
      confirmation_token, recovery_token, email_change,
      email_change_token_new, email_change_token_current,
      phone_change, phone_change_token, reauthentication_token,
      created_at, updated_at
    ) values (
      '00000000-0000-0000-0000-000000000000',
      v_id,
      'authenticated',
      'authenticated',
      v_email,
      extensions.crypt(v_password, extensions.gen_salt('bf')),
      now(),
      '{"provider": "email", "providers": ["email"]}'::jsonb,
      '{}'::jsonb,
      '', '', '', '', '', '', '', '',
      now(), now()
    );

    insert into auth.identities (
      id, user_id, provider_id, identity_data, provider,
      last_sign_in_at, created_at, updated_at
    ) values (
      gen_random_uuid(),
      v_id,
      v_id::text,
      jsonb_build_object('sub', v_id::text, 'email', v_email, 'email_verified', true),
      'email',
      null,
      now(), now()
    );

    raise notice 'Created auth user %', v_email;
  else
    update auth.users
      set encrypted_password = extensions.crypt(v_password, extensions.gen_salt('bf')),
          email_confirmed_at = coalesce(email_confirmed_at, now()),
          -- Repair a row created before the NULL-token problem was understood.
          confirmation_token         = coalesce(confirmation_token, ''),
          recovery_token             = coalesce(recovery_token, ''),
          email_change               = coalesce(email_change, ''),
          email_change_token_new     = coalesce(email_change_token_new, ''),
          email_change_token_current = coalesce(email_change_token_current, ''),
          phone_change               = coalesce(phone_change, ''),
          phone_change_token         = coalesce(phone_change_token, ''),
          reauthentication_token     = coalesce(reauthentication_token, ''),
          updated_at         = now()
      where id = v_id;

    raise notice 'User % already existed — password reset', v_email;
  end if;

  -- public.admins has no client-side INSERT policy, so this is the only way in.
  insert into public.admins (user_id, email)
  values (v_id, v_email)
  on conflict (user_id) do nothing;
end $$;

-- Verify: every admin, and whether each can sign in with a password.
select a.email,
       u.email_confirmed_at is not null as email_confirmed,
       u.encrypted_password is not null as has_password,
       u.last_sign_in_at
from public.admins a
join auth.users u on u.id = a.user_id
order by a.created_at;
