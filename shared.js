/* ── Shared JS for UK Emporium redesign ── */

// ── Cart Manager ──────────────────────────────────────────────────
const Cart = {
  items: [],

  load() {
    try { this.items = JSON.parse(localStorage.getItem('uke_cart') || '[]'); }
    catch { this.items = []; }
  },

  save() {
    localStorage.setItem('uke_cart', JSON.stringify(this.items));
  },

  add(name, price, img) {
    const existing = this.items.find(i => i.name === name);
    if (existing) {
      existing.qty++;
    } else {
      this.items.push({ name, price, img, qty: 1 });
    }
    this.save();
    this.updateBadge();
    this.renderDrawer();
    this.openDrawer();
  },

  remove(name) {
    this.items = this.items.filter(i => i.name !== name);
    this.save();
    this.updateBadge();
    this.renderDrawer();
  },

  setQty(name, qty) {
    const item = this.items.find(i => i.name === name);
    if (!item) return;
    if (qty <= 0) { this.remove(name); return; }
    item.qty = qty;
    this.save();
    this.updateBadge();
    this.renderDrawer();
  },

  total() {
    return this.items.reduce((sum, i) => {
      return sum + (parseFloat(String(i.price).replace(/[^0-9.]/g, '')) * i.qty);
    }, 0);
  },

  count() {
    return this.items.reduce((sum, i) => sum + i.qty, 0);
  },

  updateBadge() {
    const count = this.count();
    document.querySelectorAll('.cart-badge').forEach(b => {
      b.textContent = count > 99 ? '99+' : count;
      b.style.display = count > 0 ? 'flex' : 'none';
    });
    // Update sticky cart bar
    const bar = document.getElementById('stickyCart');
    if (bar) {
      const textEl = bar.querySelector('.scb-text');
      if (textEl && count > 0) {
        const total = this.total();
        const toFree = Math.max(0, 1000 - total);
        if (toFree > 0) {
          textEl.innerHTML = `${count} item${count !== 1 ? 's' : ''} in cart · <strong>R${toFree.toFixed(2)}</strong> from free delivery`;
        } else {
          textEl.innerHTML = `${count} item${count !== 1 ? 's' : ''} · <strong style="color:var(--gold-light)">Free delivery unlocked</strong>`;
        }
      } else if (textEl) {
        textEl.innerHTML = `You're <strong>R1,000</strong> away from free delivery`;
      }
      // Only show sticky bar when items in cart and scrolled down
      if (count === 0) bar.classList.remove('visible');
    }
  },

  renderDrawer() {
    const body = document.getElementById('cartDrawerBody');
    const footer = document.getElementById('cartDrawerFooter');
    const countEl = document.getElementById('cartDrawerCount');
    const n = this.count();

    if (countEl) countEl.textContent = `${n} item${n !== 1 ? 's' : ''}`;

    if (!body) return;

    if (this.items.length === 0) {
      body.innerHTML = `
        <div class="cart-empty">
          <div class="cart-empty-icon">🛒</div>
          <p class="cart-empty-title">Your cart is empty</p>
          <p class="cart-empty-sub">Browse our authentic British imports and add products to get started.</p>
          <a href="shop.html" class="btn-primary" style="margin-top:1.5rem;justify-content:center;display:flex;">Browse the shop →</a>
        </div>`;
      if (footer) footer.style.display = 'none';
      return;
    }

    body.innerHTML = this.items.map(item => {
      const safeName = item.name.replace(/'/g, '&#39;').replace(/"/g, '&quot;');
      return `
        <div class="cart-item">
          <div class="cart-item-img">
            <img src="${item.img}" alt="${safeName}" />
          </div>
          <div class="cart-item-info">
            <p class="cart-item-name">${item.name}</p>
            <p class="cart-item-price">${item.price}</p>
            <div class="cart-item-qty">
              <button class="qty-btn" data-action="dec" data-name="${safeName}">−</button>
              <span class="qty-val">${item.qty}</span>
              <button class="qty-btn" data-action="inc" data-name="${safeName}">+</button>
            </div>
          </div>
          <button class="cart-item-remove" data-action="remove" data-name="${safeName}" aria-label="Remove ${safeName}">✕</button>
        </div>`;
    }).join('');

    // Wire up qty and remove buttons
    body.querySelectorAll('[data-action]').forEach(btn => {
      btn.addEventListener('click', () => {
        const rawName = btn.getAttribute('data-name');
        const item = this.items.find(i => i.name.replace(/'/g, '&#39;').replace(/"/g, '&quot;') === rawName || i.name === rawName);
        if (!item) return;
        const action = btn.getAttribute('data-action');
        if (action === 'remove') this.remove(item.name);
        else if (action === 'inc') this.setQty(item.name, item.qty + 1);
        else if (action === 'dec') this.setQty(item.name, item.qty - 1);
      });
    });

    if (footer) {
      footer.style.display = 'flex';
      const totalEl = footer.querySelector('.cart-subtotal-amount');
      if (totalEl) totalEl.textContent = `R${this.total().toFixed(2)}`;
    }
  },

  openDrawer() {
    const drawer = document.getElementById('cartDrawer');
    const overlay = document.getElementById('cartOverlay');
    if (drawer) drawer.classList.add('open');
    if (overlay) overlay.classList.add('visible');
    document.body.style.overflow = 'hidden';
  },

  closeDrawer() {
    const drawer = document.getElementById('cartDrawer');
    const overlay = document.getElementById('cartOverlay');
    if (drawer) drawer.classList.remove('open');
    if (overlay) overlay.classList.remove('visible');
    document.body.style.overflow = '';
  }
};

// ── Inject cart drawer HTML ────────────────────────────────────────
function injectCartDrawer() {
  if (document.getElementById('cartDrawer')) return;

  const overlay = document.createElement('div');
  overlay.id = 'cartOverlay';
  overlay.className = 'cart-overlay';
  overlay.addEventListener('click', () => Cart.closeDrawer());

  const drawer = document.createElement('aside');
  drawer.id = 'cartDrawer';
  drawer.className = 'cart-drawer';
  drawer.setAttribute('aria-label', 'Shopping cart');
  drawer.innerHTML = `
    <div class="cart-drawer-header">
      <div>
        <h2 class="cart-drawer-title">Your cart</h2>
        <p class="cart-drawer-sub" id="cartDrawerCount">0 items</p>
      </div>
      <button class="cart-drawer-close" aria-label="Close cart">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>
    <div class="cart-drawer-body" id="cartDrawerBody"></div>
    <div class="cart-drawer-footer" id="cartDrawerFooter" style="display:none;">
      <div class="cart-subtotal">
        <span>Subtotal</span>
        <span class="cart-subtotal-amount">R0.00</span>
      </div>
      <p class="cart-delivery-note">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;margin-right:4px"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
        Free delivery on orders over R1,000 in Cape Town
      </p>
      <a href="contact.html" class="btn-primary cart-checkout-btn">Request a quote →</a>
      <div class="cart-wholesale-upsell">
        <p>Ordering for your business?</p>
        <a href="wholesale.html">Get wholesale pricing →</a>
      </div>
    </div>`;

  document.body.appendChild(overlay);
  document.body.appendChild(drawer);

  drawer.querySelector('.cart-drawer-close').addEventListener('click', () => Cart.closeDrawer());
  drawer.querySelector('.cart-checkout-btn')?.addEventListener('click', () => Cart.closeDrawer());
  drawer.querySelector('.cart-wholesale-upsell a')?.addEventListener('click', () => Cart.closeDrawer());
}

// ── Reveal on scroll ───────────────────────────────────────────────
function initReveal() {
  // gsap-enhance.js takes ownership of reveals when GSAP is present.
  if (window.__gsapReveals) return;
  const els = document.querySelectorAll('.reveal');
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });
  els.forEach(el => obs.observe(el));
}

// ── Sticky cart bar ────────────────────────────────────────────────
function initStickyCart() {
  const bar = document.getElementById('stickyCart');
  if (!bar) return;
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const show = window.scrollY > 400 && Cart.count() > 0;
        bar.classList.toggle('visible', show);
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
  const btn = bar.querySelector('.scb-btn');
  if (btn) btn.addEventListener('click', () => Cart.openDrawer());
}

// ── Add to cart buttons ────────────────────────────────────────────
function initCartButtons() {
  document.querySelectorAll('.btn-add-cart').forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      const card = this.closest('.product-card');
      const name = card?.querySelector('.product-name')?.textContent?.trim() || 'Product';
      const price = card?.querySelector('.product-price')?.textContent?.trim() || 'R0.00';
      const img = card?.querySelector('img')?.src || '';

      Cart.add(name, price, img);

      const orig = this.textContent;
      this.textContent = 'Added ✓';
      this.classList.add('added');
      setTimeout(() => {
        this.textContent = orig;
        this.classList.remove('added');
      }, 1600);
    });
  });

  // Hero card add button — open cart drawer
  document.querySelectorAll('.pch-add').forEach(btn => {
    btn.addEventListener('click', () => Cart.openDrawer());
  });
}

// ── Wire cart icon to open drawer ─────────────────────────────────
function initCartIcon() {
  document.querySelectorAll('[aria-label="Cart"]').forEach(el => {
    el.addEventListener('click', function(e) {
      e.preventDefault();
      Cart.openDrawer();
    });
  });
}

// ── Sort products ─────────────────────────────────────────────────
function initSort() {
  const select = document.querySelector('.shop-sort select');
  if (!select) return;
  select.addEventListener('change', function() {
    document.querySelectorAll('.products-grid, .products-grid-3, .products-grid-4').forEach(grid => {
      const cards = Array.from(grid.querySelectorAll('.product-card'));
      if (!cards.length) return;
      cards.sort((a, b) => {
        const pA = parseFloat(a.querySelector('.product-price')?.textContent?.replace(/[^0-9.]/g, '') || 0);
        const pB = parseFloat(b.querySelector('.product-price')?.textContent?.replace(/[^0-9.]/g, '') || 0);
        const nA = a.querySelector('.product-name')?.textContent || '';
        const nB = b.querySelector('.product-name')?.textContent || '';
        if (this.value === 'price-asc') return pA - pB;
        if (this.value === 'price-desc') return pB - pA;
        if (this.value === 'name-asc') return nA.localeCompare(nB);
        return 0;
      });
      cards.forEach(card => grid.appendChild(card));
    });
  });
}

// ── Mobile menu ───────────────────────────────────────────────────
function initMobileMenu() {
  const hamburger = document.querySelector('.nav-hamburger');
  const menu = document.getElementById('mobileMenu');
  const close = document.querySelector('.mobile-menu-close');
  if (!hamburger || !menu) return;
  hamburger.addEventListener('click', () => menu.classList.add('open'));
  close?.addEventListener('click', () => menu.classList.remove('open'));
  menu.addEventListener('click', e => { if (e.target === menu) menu.classList.remove('open'); });
}

// ── Newsletter form ───────────────────────────────────────────────
function initNewsletterForm() {
  const form = document.querySelector('.nl-form');
  if (!form) return;
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    const input = this.querySelector('input[type="email"]');
    const btn = this.querySelector('button[type="submit"]');
    if (!input?.value || !input.validity.valid) {
      input.style.borderColor = '#CF142B';
      input.focus();
      return;
    }
    if (btn) { btn.textContent = 'Subscribed ✓'; btn.style.background = '#136567'; }
    if (input) { input.disabled = true; }
    if (btn) btn.disabled = true;
  });
}

// ── Contact / wholesale form ──────────────────────────────────────
function initContactForm() {
  const form = document.querySelector('.contact-form');
  if (!form) return;
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    let valid = true;
    this.querySelectorAll('[required]').forEach(field => {
      if (!field.value.trim()) {
        field.classList.add('error');
        valid = false;
      } else {
        field.classList.remove('error');
      }
    });
    if (!valid) return;
    const btn = this.querySelector('button[type="submit"]');
    const orig = btn.textContent;
    btn.textContent = 'Message sent ✓';
    btn.style.background = '#136567';
    btn.disabled = true;
    setTimeout(() => {
      btn.textContent = orig;
      btn.style.background = '';
      btn.disabled = false;
      form.reset();
    }, 3000);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  Cart.load();
  injectCartDrawer();
  Cart.updateBadge();
  Cart.renderDrawer();
  initReveal();
  initStickyCart();
  initCartButtons();
  initCartIcon();
  initMobileMenu();
  initNewsletterForm();
  initContactForm();
  initSort();
});
