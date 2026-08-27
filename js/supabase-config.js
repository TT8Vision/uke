/* Public Supabase client for the uke storefront.
   The publishable key is designed to ship in the browser; RLS enforces that
   only admins (public.is_admin()) can write. No service-role key here, ever. */
(function () {
  const URL = 'https://dyifpssjebmkvpdoiyas.supabase.co';
  const KEY = 'sb_publishable_hdC7VIEduIiPQ_Q81EZB0Q_mSYrIgtz';
  if (!window.supabase || !window.supabase.createClient) {
    console.error('[supabase-config] supabase-js not loaded before this script');
    return;
  }
  window.ukeSupabase = window.supabase.createClient(URL, KEY, {
    auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true },
  });
})();
