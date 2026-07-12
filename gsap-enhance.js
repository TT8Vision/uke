/* ────────────────────────────────────────────────────────────────
   gsap-enhance.js — Premium GSAP motion layer (progressive enhancement)
   Loads AFTER shared.js. If GSAP fails to load (CDN blocked), this file
   no-ops and shared.js's CSS reveal fallback stays active — no flash,
   no missing content. Fully respects prefers-reduced-motion.
   ──────────────────────────────────────────────────────────────── */
(function () {
  // Bail cleanly if the GSAP CDN didn't load — CSS/IntersectionObserver fallback stands in.
  if (!window.gsap || !window.ScrollTrigger) return;

  gsap.registerPlugin(ScrollTrigger);

  // Tell shared.js's initReveal() to stand down — this layer owns the reveals.
  // Set synchronously at parse time, before shared.js's DOMContentLoaded handler runs.
  window.__gsapReveals = true;

  // Kills the CSS transition on .reveal so GSAP's per-frame writes aren't double-eased.
  document.documentElement.classList.add('gsap-active');

  gsap.defaults({ ease: 'power3.out', duration: 0.8 });

  const mm = gsap.matchMedia();

  mm.add(
    {
      reduce: '(prefers-reduced-motion: reduce)',
    },
    (ctx) => {
      // Reduced motion: reveal everything instantly, no movement, no parallax.
      if (ctx.conditions.reduce) {
        gsap.set('.reveal', { opacity: 1, y: 0, clearProps: 'transform' });
        return;
      }
      buildHero();
      buildSectionReveals();
      buildHeroParallax();
    }
  );

  // ── Hero entrance choreography ──────────────────────────────────
  function buildHero() {
    const hero = document.querySelector('.hero');
    if (!hero) return;

    // The .reveal wrappers themselves become visible; their children are choreographed.
    gsap.set(hero.querySelectorAll('.reveal'), { opacity: 1, y: 0 });

    const tl = gsap.timeline({ delay: 0.15 });
    tl.from('.hero-label', { y: 20, autoAlpha: 0, duration: 0.6 })
      .from('.hero-headline', { y: 30, autoAlpha: 0, duration: 0.9 }, '-=0.35')
      .from('.hero-sub', { y: 20, autoAlpha: 0, duration: 0.7 }, '-=0.55')
      .from('.hero-actions > *', { y: 16, autoAlpha: 0, stagger: 0.1, duration: 0.6 }, '-=0.4')
      .from('.hero-trust .trust-item', { y: 12, autoAlpha: 0, stagger: 0.12, duration: 0.5 }, '-=0.3')
      // Card stack settles in with a soft overshoot.
      .from('.hero-visual', { y: 44, autoAlpha: 0, scale: 0.96, duration: 1, ease: 'back.out(1.4)' }, '-=0.95')
      // Float badges: fade only (autoAlpha leaves transform alone so the CSS float keeps running).
      .from('.float-badge', { autoAlpha: 0, stagger: 0.15, duration: 0.6 }, '-=0.55');
  }

  // ── Scroll-driven section reveals (staggered, eased) ────────────
  function buildSectionReveals() {
    const hero = document.querySelector('.hero');
    const rest = gsap.utils
      .toArray('.reveal')
      .filter((el) => !hero || !hero.contains(el));

    gsap.set(rest, { opacity: 0, y: 26 });

    ScrollTrigger.batch(rest, {
      start: 'top 88%',
      once: true,
      onEnter: (batch) =>
        gsap.to(batch, {
          opacity: 1,
          y: 0,
          duration: 0.85,
          stagger: 0.12,
          overwrite: true,
        }),
    });
  }

  // ── Subtle scroll parallax on the hero card stack ───────────────
  function buildHeroParallax() {
    if (!document.querySelector('.hero-card-stack')) return;
    gsap.to('.hero-card-stack', {
      yPercent: -10,
      ease: 'none',
      scrollTrigger: {
        trigger: '.hero',
        start: 'top top',
        end: 'bottom top',
        scrub: 1,
      },
    });
  }

  // Recalculate trigger positions once lazy images have loaded (layout shift).
  window.addEventListener('load', () => ScrollTrigger.refresh());
})();
