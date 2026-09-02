-- Grant admin rights to a staff member.
--
-- Prerequisite: the person already has an auth user. Either they signed up on
-- login.html (Create account tab), or you invited them from the Supabase
-- dashboard (Authentication -> Users -> Add user).
--
-- Run this in the Supabase SQL editor for project xwgpaalydysfebyolern.
-- Safe to re-run; it will not duplicate a row.

insert into public.admins (user_id, email)
select id, email
from auth.users
where lower(email) = lower('jonathantheron34@gmail.com')
on conflict (user_id) do nothing;

-- Verify: should return exactly one row.
select a.user_id, a.email, a.created_at
from public.admins a
where lower(a.email) = lower('jonathantheron34@gmail.com');
