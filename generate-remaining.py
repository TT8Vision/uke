#!/usr/bin/env python3
import os

BASE_DIR = '/Users/dremuthan/uke-redesign'

NAV = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — UK Emporium</title>
  <meta name="description" content="Browse all {title} — authentic British imported goods from UK Emporium, Cape Town." />
  <link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
  <style>
    .products-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem}}
    @media(max-width:1100px){{.products-grid{{grid-template-columns:repeat(3,1fr)}}}}
    @media(max-width:700px){{.products-grid{{grid-template-columns:repeat(2,1fr)}}}}
    @media(max-width:440px){{.products-grid{{grid-template-columns:1fr}}}}
    .cat-page-header{{display:flex;align-items:center;justify-content:space-between;margin-bottom:2rem;flex-wrap:wrap;gap:1rem}}
    .cat-page-count{{font-size:.85rem;color:var(--mid-gray)}}
    .back-link{{font-size:.82rem;font-weight:600;color:var(--gold);text-decoration:underline;text-underline-offset:3px}}
    .back-link:hover{{color:var(--navy)}}
  </style>
</head>
<body>
<div class="ticker-bar"><div class="ticker-track">
  <span class="ticker-item">🇬🇧 Authentic British imports<span>·</span></span>
  <span class="ticker-item">Buy any 5 Astonish triggers — 10% off · Code: <strong>AST10</strong><span>·</span></span>
  <span class="ticker-item">Free delivery over R1,000 · Cape Town &amp; 60km radius<span>·</span></span>
  <span class="ticker-item">🇬🇧 Authentic British imports<span>·</span></span>
  <span class="ticker-item">Buy any 5 Astonish triggers — 10% off · Code: <strong>AST10</strong><span>·</span></span>
  <span class="ticker-item">Free delivery over R1,000 · Cape Town &amp; 60km radius<span>·</span></span>
</div></div>
<nav class="nav"><div class="nav-inner">
  <a href="index.html" class="nav-logo"><span class="nav-logo-main">UK <em>Emporium</em></span><span class="nav-logo-sub">Cape Town · Est. in Britain</span></a>
  <ul class="nav-links">
    <li><a href="index.html">Home</a></li><li><a href="our-brands.html">Our Brands</a></li><li><a href="about.html">About</a></li>
    <li><a href="shop.html" class="active">Shop</a></li><li><a href="wholesale.html">Wholesale</a></li><li><a href="contact.html">Contact</a></li>
  </ul>
  <div class="nav-actions">
    <a href="my-account.html" class="nav-icon-btn" aria-label="Account"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></a>
    <a href="shop.html" class="nav-icon-btn" style="position:relative" aria-label="Cart"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg><span class="cart-badge">0</span></a>
    <button class="nav-hamburger" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</div></nav>
<div class="mobile-menu" id="mobileMenu">
  <div class="mobile-menu-header"><span style="font-family:\'Playfair Display\',serif;font-size:1.3rem;font-weight:700;color:#fff;">UK <em style="font-style:italic;color:var(--gold-light);">Emporium</em></span><button class="mobile-menu-close">✕</button></div>
  <ul class="mobile-menu-links"><li><a href="index.html">Home</a></li><li><a href="our-brands.html">Our Brands</a></li><li><a href="about.html">About</a></li><li><a href="shop.html" class="active">Shop</a></li><li><a href="wholesale.html">Wholesale</a></li><li><a href="contact.html">Contact</a></li><li><a href="my-account.html">My Account</a></li></ul>
</div>
<div class="page-hero">
  <div class="page-hero-content">
    <div class="breadcrumb"><a href="index.html">Home</a><span>/</span><a href="shop.html">Shop</a><span>/</span><span style="color:var(--gold-light);">{title}</span></div>
    <p class="page-hero-label">{emoji} All products</p>
    <h1 class="page-hero-title">{title}</h1>
    <p class="page-hero-sub">Authentic British imports — {count} products</p>
  </div>
</div>
<main>
<section class="section section-cream">
  <div class="container">
    <div class="cat-page-header">
      <p class="cat-page-count">Showing <strong>{count}</strong> products</p>
      <a href="shop.html" class="back-link">← Back to all categories</a>
    </div>
    <div class="wholesale-cta-banner">
      <div class="wcb-text">
        <p class="wcb-label">For businesses</p>
        <p class="wcb-title">Ordering in bulk? Get wholesale pricing.</p>
        <p class="wcb-sub">We supply retailers, delis, restaurants and forecourts across South Africa with exclusive British brands.</p>
      </div>
      <div class="wcb-actions">
        <a href="wholesale.html" class="btn-wcb-primary">Apply for wholesale →</a>
        <a href="tel:+27215511722" class="btn-wcb-ghost">Call 021 551 1722</a>
      </div>
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between;gap:1rem;margin-bottom:2rem;flex-wrap:wrap;">
      <div class="shop-sort">
        <label for="sort-select" style="font-size:.82rem;color:var(--mid-gray);">Sort by:</label>
        <select id="sort-select" style="border:1.5px solid var(--border-light);border-radius:var(--radius-sm);padding:.5rem .9rem;font-family:inherit;font-size:.83rem;color:var(--navy);outline:none;cursor:pointer;background:#fff;">
          <option value="featured">Featured</option>
          <option value="price-asc">Price: Low to High</option>
          <option value="price-desc">Price: High to Low</option>
          <option value="name-asc">Name: A\u2013Z</option>
        </select>
      </div>
    </div>
    <div class="products-grid">
'''

FOOTER = '''    </div>
  </div>
</section>
</main>
<footer class="footer"><div class="container">
  <div class="footer-grid">
    <div><div class="footer-logo-main">UK <em>Emporium</em></div><p class="footer-tagline">Quality imported goods from the UK</p><p class="footer-about">Cape Town&#39;s home of authentic British imports since 2004.</p><div class="social-links"><a href="https://facebook.com/UkEmporiumCpt/" class="social-link" target="_blank" rel="noopener">f</a><a href="https://instagram.com/ukemporium/" class="social-link" target="_blank" rel="noopener">ig</a><a href="https://tiktok.com/@ukemporiumcpt" class="social-link" target="_blank" rel="noopener">tt</a></div></div>
    <div><p class="footer-col-title">Shop</p><ul class="footer-links"><li><a href="cat-beers.html">Beers &amp; Ales</a></li><li><a href="cat-confectionery.html">Confectionery</a></li><li><a href="cat-groceries.html">Groceries</a></li><li><a href="cat-hotdrinks.html">Hot Drinks</a></li><li><a href="cat-colddrinks.html">Cold Drinks</a></li><li><a href="cat-cleaning.html">Household Cleaning</a></li><li><a href="cat-personalcare.html">Personal Care</a></li><li><a href="cat-cereals.html">Cereals &amp; Breakfast</a></li><li><a href="cat-kent.html">Kent Hairbrushes</a></li></ul></div>
    <div><p class="footer-col-title">Company</p><ul class="footer-links"><li><a href="index.html">Home</a></li><li><a href="our-brands.html">Our Brands</a></li><li><a href="about.html">About Us</a></li><li><a href="wholesale.html">Wholesale</a></li><li><a href="contact.html">Contact</a></li><li><a href="my-account.html">My Account</a></li></ul></div>
    <div><p class="footer-col-title">Help</p><ul class="footer-links"><li><a href="contact.html">Delivery Info</a></li><li><a href="wholesale.html">Wholesale</a></li><li><a href="#">Terms</a></li><li><a href="#">Privacy</a></li></ul></div>
  </div>
  <div class="footer-bottom"><p class="footer-copy">Copyright &copy; 2026 UK Emporium. Cape Town branch only.</p><div class="footer-legal"><a href="#">Terms</a><a href="#">Privacy</a><a href="contact.html">Contact</a></div></div>
</div></footer>
<div class="sticky-cart-bar" id="stickyCart"><span class="scb-text">You&#39;re <strong>R1,000</strong> away from free delivery</span><button class="scb-btn" onclick="window.scrollTo(0,0)">Keep shopping</button></div>
<script src="shared.js"></script>
</body>
</html>
'''

def card(name, price, img, brand='', volume='', tag=''):
    tag_html = f'<span class="product-tag">{tag}</span>' if tag else ''
    brand_html = f'<p class="product-brand">{brand}</p>' if brand else ''
    vol_html = f'<p class="product-volume">{volume}</p>' if volume else ''
    img_safe = img.replace('"', '&quot;')
    name_safe = name.replace('&', '&amp;').replace('"', '&quot;')
    return f'<div class="product-card"><div class="product-img-wrap">{tag_html}<button class="product-wishlist">&#9825;</button><img src="{img_safe}" alt="{name_safe}" loading="lazy" /></div><div class="product-body">{brand_html}<h3 class="product-name">{name_safe}</h3>{vol_html}<div class="product-footer"><div><span class="product-price">{price}</span></div><button class="btn-add-cart">Add to cart</button></div></div></div>\n'

def make_page(path, title, emoji, products):
    count = len(products)
    html = NAV.format(title=title, emoji=emoji, count=count)
    for p in products:
        if len(p) == 3:
            html += card(p[0], p[1], p[2])
        elif len(p) == 4:
            html += card(p[0], p[1], p[2], brand=p[3])
        elif len(p) == 5:
            html += card(p[0], p[1], p[2], brand=p[3], volume=p[4])
        elif len(p) == 6:
            html += card(p[0], p[1], p[2], brand=p[3], volume=p[4], tag=p[5])
    html += FOOTER
    with open(path, 'w') as f:
        f.write(html)
    print(f'Written {os.path.basename(path)} ({count} products)')

# ── CONFECTIONERY (200 products) ──────────────────────────────────────────────
confectionery = [
    ('Barratt Dolly Mix', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/04/dolly-mix.pptx.jpg', 'Barratt', '150g'),
    ('Barratt Milk Bottles', 'R55.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/5010511481347.jpg', 'Barratt', '150g'),
    ('Barratt Refreshers Tube', 'R19.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/Refreshers-Tube-34g.jpg', 'Barratt', '30g'),
    ('Barratt Shrimps & Bananas', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/barratt-shrimp.jpg', 'Barratt', '150g'),
    ('Bazooka Juicy Drop Blasts', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/Juicy-Drops-Blasts-140-g.jpg', 'Bazooka', '120g'),
    ('Bazooka Push Pop Dipperz', 'R14.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Bazooka-Push-Pop-Dipperz-12g.jpg', 'Bazooka', '12g'),
    ('Bazooka Ring Pop Blackcurrant', 'R22.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/black-ring-pop.jpg', 'Bazooka', '10g'),
    ('Bazooka Ring Pop Cola', 'R22.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/cola.jpg', 'Bazooka', '10g'),
    ('Bazooka Ring Pop Raspberry', 'R22.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/raspberry.jpg', 'Bazooka', '10g'),
    ('Bazooka Ring Pop Strawberry', 'R22.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/strawberry.jpg', 'Bazooka', '10g'),
    ('Bebeto Fizzy Strawberry Laces', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/Bebeto-Fizzy-Strawberry-Laces-200.jpg', 'Bebeto', '160g'),
    ('Bebeto Fizzy Strawberry Pencils', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/Bebeto-Fizzy-STrawberry-Pencils-160g.jpg', 'Bebeto', '160g'),
    ('Bebeto Twisted Fruity Pencils', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bebeto-twisted-fruity-pencils-new.jpg', 'Bebeto', '160g'),
    ('Beyoglu Dubai Duo Wafer', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/12/Beyoglu-Dubai-Duo-Wafer-36g.webp', 'Beyoglu', '36g'),
    ('Big D Salted Peanuts', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/big-d-salted-peanuts-200g_e5957e67-b5e9-4ef4-bbec-3ae9cb320f52_500x500.webp', 'Big D', '200g'),
    ('Bolands Fig Rolls', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/11/figRols_2__jpg.webp', 'Bolands', '200g'),
    ('Burtons Wagon Wheels', 'R57.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Burtons-Wagon-Wheels-Original-6-Pack.jpg', 'Burtons', '6pk'),
    ('Burtons Wagon Wheels Jammie', 'R57.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Burtons-Wagon-Wheels-Jammie-6-Pack.jpg', 'Burtons', '6pk'),
    ('Cadbury Boost Bar', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/bb-Cadbury-Boost-48.5g-ChatGPT.pptx.png', 'Cadbury', '48.5g'),
    ('Cadbury Bournville Old Jamaica Dark Chocolate Rum & Raisin', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/BournevilleOldJamaica_700x700.webp', 'Cadbury', '100g'),
    ('Cadbury Buttons Pouch', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Buttons-100g-ChatGPT.pptx.png', 'Cadbury', '100g'),
    ('Cadbury Choco Sandwich', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/06/cadchococ_669x669.webp', 'Cadbury', '260g'),
    ('Cadbury Crunchie Rocks Pouch', 'R74.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/Cadbury-Crunchie-Rock-2.png', 'Cadbury', '100g'),
    ('Cadbury Crunchy Melts Chocolate Centre', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Crunchy-Melts-156g-ChatGPT.pptx.png', 'Cadbury', '156g'),
    ('Cadbury Curly Wurly', 'R12.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Curly-Wurly-21.5g-ChatGPT.pptx-1.png', 'Cadbury', '21.5g'),
    ('Cadbury Curly Wurly', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/02/Curly-Wurly-5pk.jpg', 'Cadbury', '5pk'),
    ('Cadbury Curly Wurly Squirlies', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/curlysquirlies.jpg', 'Cadbury', '85g'),
    ('Cadbury Daim Slab', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/Cadbury-Daim-Slab-120g.jpg', 'Cadbury', '120g'),
    ('Cadbury Dairy Milk & More Caramel Nut Crunch', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/bb-Cadbury-Caramel-Nut-Crunch-200g-ChatGPT.pptx.png', 'Cadbury', '200g'),
    ('Cadbury Dairy Milk & More Nutty Praline Crisp', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/bb-Cadbury-Nutty-Praline-Crisp-180g-ChatGPT.pptx.png', 'Cadbury', '180g'),
    ('Cadbury Dairy Milk Crunchie Bits', 'R117.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/cadbury_crunchie_bits.webp', 'Cadbury', '180g'),
    ('Cadbury Darkmilk Buttons', 'R77.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Cadbury-Darkmilk-Buttons-100g-ChatGPT.pptx-1.png', 'Cadbury', '100g'),
    ('Cadbury Delights Hazelnut Caramel Soft Nougat', 'R94.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/07/104719-1.png', 'Cadbury', '110g'),
    ('Cadbury Delights Salted Caramel Soft Nougat', 'R94.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/07/41lQ8sYAbLL._SR600315_PIWhiteStripBottomLeft035_PIStarRatingFOURBottomLeft360-6_SR600315_ZA27445290400400AmazonEmberBold124005_SCLZZZZZZZ_FMpng_BG255255255.png', 'Cadbury', '110g'),
    ('Cadbury Double Decker Bar', 'R10.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Double-Decker-54.5g-ChatGPT.pptx-1.png', 'Cadbury', '54.5g'),
    ('Cadbury Eclairs', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/08/7622210117793.jpg', 'Cadbury', '130g'),
    ('Cadbury Freddo Caramel Bar', 'R12.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Freddo-Caramel-19.5g-ChatGPT.pptx.png', 'Cadbury', '19.5g'),
    ('Cadbury Fudge Bar', 'R13.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Fudge-Bar-22g-ChatGPT.pptx.png', 'Cadbury', '22g'),
    ('Cadbury Fudge Bars', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/fudge-4pk.jpg', 'Cadbury', '4x22g'),
    ('Cadbury Marvellous Creations', 'R15.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/Cadbury-Marvellous-Creations-47g.jpg', 'Cadbury', '47g'),
    ('Cadbury Milk Chocolate Fingers', 'R47.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Dairy-Milk-Fingers-114g-ChatGPT.pptx.png', 'Cadbury', '114g'),
    ('Cadbury Nibbly Fingers', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Cadbury-Nibbly-Fingers-125g.jpg', 'Cadbury', '125g'),
    ('Cadbury Oreo Bites Pouch', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Cadbury-Oreo-Bites.jpg', 'Cadbury', '85g'),
    ('Cadbury Oreo Sandwich', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Oreo-Sandwich-Slab-96g-ChatGPT.pptx.png', 'Cadbury', '96g'),
    ('Cadbury Picnic Bar', 'R38.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/47ef548c-bb4e-4685-8037-c7da31f0f097.png', 'Cadbury', '48.4g'),
    ('Cadbury Starbar', 'R10.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Starbar-49g-ChatGPT.pptx-1.png', 'Cadbury', '49g'),
    ('Cadbury Twirl Bar', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Twirl-43g-ChatGPT.pptx.png', 'Cadbury', '43g'),
    ('Cadbury Twirl Bites Pouch', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Cadbury-Twirl-Bites-Pouch-109g.jpg', 'Cadbury', '85g'),
    ('Cadbury Twirl Orange', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/bb-Cadbury-Twirl-Orange-43g-ChatGPT.pptx.png', 'Cadbury', '43g'),
    ('Cadbury Twirl White Dipped Chocolate', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Cadbury-Twirl-Dipped-White-43g-ChatGPT.pptx.png', 'Cadbury', '43g'),
    ('Cadbury Twirl Xtra', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Twirl-Xtra-54g-ChatGPT.pptx.png', 'Cadbury', '54g'),
    ('Cadbury White Oreo Chocolate', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb-Cadbury-White-Oreo-120g-ChatGPT.pptx.png', 'Cadbury', '120g'),
    ('Cadbury Wispa Bar', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Wispa-36g-ChatGPT.pptx.png', 'Cadbury', '36g'),
    ('Cadbury Wispa Bites', 'R77.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Cadbury-Wipsa-Pouch-100g-ChatGPT.pptx.png', 'Cadbury', '100g'),
    ('Cadbury Wispa Duo', 'R45.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Wispa-Duo-47.4g-ChatGPT.pptx.png', 'Cadbury', '47.4g'),
    ('Cadbury Wispa Gold', 'R31.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Cadbury-Wispa-Gold-48g-ChatGPT.pptx.png', 'Cadbury', '48g'),
    ('Candy Kittens Smittens Sour', 'R45.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Candy-Kittens-Smittens-Sour-130g.pptx.png', 'Candy Kittens', '130g'),
    ('Candy Kittens Smittens Strawberry', 'R45.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Candy-Kittens-Smittens-Strawberry-130g.pptx.png', 'Candy Kittens', '130g'),
    ('Candyland Sherbet Dip Dabs', 'R19.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Candyland-Sherbet-Dip-Dabs-23g.jpg', 'Candyland', '23g'),
    ('Candyland Sherbet Fountains', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Candyland-Sherbet-Fountains-25g.jpg', 'Candyland', '25g'),
    ("Cheetos Twisted Flamin' Hot", 'R14.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/08/CheetosTwistedFlamin_HotSnacksCrisps_1024x1024.webp', 'Cheetos', '30g'),
    ('Chupa Chups Cotton Candy Bubble Gum', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Chupa-Chups-Cotton-Candy-Bubblegum-2.jpg', 'Chupa Chups', '11g'),
    ('Chupa Chups Melody Pops Strawberry', 'R16.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/02/Chup-Melody-12.jpg', 'Chupa Chups', '12g'),
    ('Crawfords Garibaldi', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Crawfords-Garibaldi-100g.jpg', 'Crawfords', '100g'),
    ('Doritos Cool Original', 'R28.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/12/Doritos-Cool-Original-40g.jpg', 'Doritos', '40g'),
    ('Doritos Tangy Cheese', 'R28.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/doritos-tangy-cheese-box-of-32-packets-40g-crisps-769_600x600.webp', 'Doritos', '40g'),
    ("Doritos That's Nuts Chilli Heatwave", 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Doritos-Thats-Nuts-Chilli-Heatwave-160g.pptx.png', 'Doritos', '160g'),
    ("Doritos That's Nuts Flamin' Hot", 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Doritos-Thats-Nuts-Flamin-Hot-160g.pptx.png', 'Doritos', '160g'),
    ('Euroshopper Jaffa Cakes', 'R74.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/images-12.jpeg', 'Euroshopper', '300g'),
    ("Farley's Original Rusks", 'R85.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/FARLEYS-RUSKS-300G.jpg', "Farley's", '150g'),
    ("Farley's Rusks Reduced Sugar", 'R85.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/farleys-reduced.webp', "Farley's", '150g'),
    ('Fini Rainbow Tornadoes', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/Fini-Rainbow-Tornadoes-225g.jpg', 'Fini', '140g'),
    ('Fini Strawberry Tornadoes', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/Fini-Strawberry-Tornadoes-225g.jpg', 'Fini', '140g'),
    ('Fini Tornadoes Smooth Raspberry', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/09/Fini-Tornadoes-Raspberry-200g.jpg', 'Fini', '140g'),
    ("Fisherman's Friend Cherry", 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/Fisherman_sFriendSugarFreeCherryFlavourLozenges25g_bgremoved.webp', "Fisherman's Friend", '25g'),
    ('Fishermans Friend Honey & Lemon', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/Untitled_design_d5fb3dd7-4eb2-4603-9c29-6e6e0085bda4_1024x.webp', "Fisherman's Friend", '25g'),
    ('Fizz Wiz Popping Candy Cherry Flavour', 'R12.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Fizz-Wizz-Cherry-Pop-5g.jpg', 'Fizz Wiz', '5g'),
    ('Fizz Wiz Popping Candy Cola Flavour', 'R12.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Fizz-Wizz-Cola-Pop-5g.jpg', 'Fizz Wiz', '5g'),
    ('Fizz Wiz Popping Candy Strawberry Flavour', 'R12.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Fizz-Wizz-Strawberry-Pop-5g.jpg', 'Fizz Wiz', '5g'),
    ("Fox's Chocolatey Dubai Style Pistachio Shortcake Biscuits", 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Foxs-Chocolatey-Dubai-Style-Pistachio.pptx.png', "Fox's", '130g'),
    ("Fox's Glacier Fruits", 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/fruit.jpg', "Fox's", '100g'),
    ("Fox's Glacier Fruits", 'R64.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/foxs-glacier-fruits-200g.jpg', "Fox's", '200g'),
    ("Fox's Glacier Mints", 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/mints.jpg', "Fox's", '100g'),
    ("Fox's Glacier Mints", 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/foxs-glacier-mints-200g.jpg', "Fox's", '200g'),
    ("Fox's Party Rings", 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/fox-party-ring-single-2.jpg', "Fox's", '125g'),
    ("Fox's Seriously Strong XXX Peppermints", 'R104.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/foxs-xxx-peppermint-extra-strong-mints-5pk.webp', "Fox's", '5pk'),
    ('Frisia Fruit UFO Flying Saucers', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Frisia-Fruit-UFOs-Flying-Saucers-45g.pptx.png', 'Frisia', '45g'),
    ("Fry's Chocolate Cream", 'R25.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/U-2FRY35CC-08_08_2022_17_16_23_1.png', "Fry's", '3x49g'),
    ("Fry's Chocolate Cream Bar", 'R10.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Frys-Chocolate-Cream-Std-49g.jpg', "Fry's", '49g'),
    ("Fry's Orange Cream", 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/Fry-Or-Cr-3pk.jpg', "Fry's", '3x49g'),
    ("Fry's Orange Cream Chocolate Bar", 'R10.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/frys-orange.jpg', "Fry's", '49g'),
    ("Fry's Peppermint Cream", 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/FRYS-PEPPERMINT-CREAM-3-PACK-3X49G-147G.webp', "Fry's", '3x49g'),
    ("Fry's Peppermint Cream Chocolate Bar", 'R24.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Frys-Peppermint-Cream-Std-49g.jpg', "Fry's", '49g'),
    ("Fry's Turkish Delight", 'R15.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Frys-Turk-3.jpg', "Fry's", '3pk'),
    ("Fry's Turkish Delight Mini Bars", 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/FRYS-TURKISH-MINI-BARS.jpg', "Fry's", '7pk'),
    ("Fry's Turkish Delight Single", 'R8.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Frys-Turk-Sing.jpg', "Fry's", '51g'),
    ('Galaxy Minstrels', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Galaxy-Minstrels-42g-ChatGPT.pptx.png', 'Galaxy', '42g'),
    ('Galaxy Minstrels Pouch', 'R92.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/02/Galaxy-Minstrels-125.jpg', 'Galaxy', '125g'),
    ('Galaxy Minstrels Treat Bag', 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/02/Galaxy-Minstrels-80.jpg', 'Galaxy', '80g'),
    ('Galaxy Ripple Bar', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Galaxy-Ripple-30g.pptx.png', 'Galaxy', '30g'),
    # Page 2
    ('Galaxy Ripple Bar', 'R66.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/ripple-3pk.jpg', 'Galaxy', '3x30g'),
    ('Galaxy Smooth Milk Bar', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/5000159470292.jpg', 'Galaxy', '42g'),
    ('Galaxy Smooth Milk Caramel Bar', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/Galaxy-Smooth-Caramel-48g.jpg', 'Galaxy', '48g'),
    ('Galaxy Smooth Milk Chocolate Block', 'R76.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Galaxy-Smth-Milk-110g.jpg', 'Galaxy', '100g'),
    ('Halls Soothers Blackcurrant', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/blackcurrent.jpg', 'Halls', '45g'),
    ('Halls Soothers Cherry', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/halls-soothers-cherry-1-pack-p977-3064_zoom-scaled.png', 'Halls', '45g'),
    ('Halls Soothers Honey & Lemon', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/Halls_Soothers_Honey___Lemon_45g.jpg', 'Halls', '45g'),
    ('Halls Soothers Peach & Raspberry', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/Halls-Soothers-Peach-Raspberry.webp', 'Halls', '45g'),
    ('Halls Soothers Strawberry', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/strawberry-halls.png', 'Halls', '45g'),
    ("Hannah's Jazzles Milk Chocolate", 'R41.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/03/hannah-s-jazzles-milk-chocolate-180g-godteri-38633460859064_1200x1200.webp', "Hannah's", '140g'),
    ('Haribo Balla Bites', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/08/Balla-Bites-160g_VegPM-700x940-1.png', 'Haribo', '154g'),
    ('Haribo Balla Stix Strawberry', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Haribo-Strawberry-Balla-Stix-PM-140g.jpg', 'Haribo', '140g'),
    ('Haribo Chamallows', 'R57.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Haribo-Chamallows-140g.jpg', 'Haribo', '140g'),
    ('Haribo Giant Strawbs', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Haribo-Giant-Strawbs-160g.jpg', 'Haribo', '140g'),
    ('Haribo Gold Bears', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/11/51aat1L8yQL.jpg', 'Haribo', '154g'),
    ('Haribo Happy Cola', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Haribo-Happy-Cola-160-g.jpg', 'Haribo', '154g'),
    ('Haribo Harry Potter', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/12/Haribo-Harry-Potter-160g.jpg', 'Haribo', '160g'),
    ('Haribo Nostalgix', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-Haribo-Nostalgix-140g-.pptx.png', 'Haribo', '140g'),
    ('Haribo Pontefract Cakes', 'R57.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Haribo-Pontefract-Cakes-Bag-140g.jpg', 'Haribo', '160g'),
    ('Haribo Rainbow Strips Z!ng', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Haribo-Rainbow-Strips-Zing-130g.jpg', 'Haribo', '143g'),
    ('Haribo Soda Twist Z!ng', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/08/HARIBO-SODA-TWIST-ZING-160G.png', 'Haribo', '140g'),
    ('Haribo Sour Sparks', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Haribo-Sour-Sparks-160g.jpg', 'Haribo', '140g'),
    ('Haribo Starmix', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Haribo-Starmix-140g.jpg', 'Haribo', '140g'),
    ('Haribo Supermix', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/12/142121-E-Supermix-160g.webp', 'Haribo', '140g'),
    ('Haribo Tangfastics', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Haribo-Tangfastics-Bag-140g.jpg', 'Haribo', '140g'),
    ('Haribo Twin Snakes', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/12/twin_snakes_10.jpg', 'Haribo', '154g'),
    ("Henry Goode's Superbly Soft Liquorice", 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Henry-Goode-Soft-Liquorice-140g.jpg', "Henry Goode's", '200g'),
    ("Hershey's Cookies n Creme Dipped Pretzels", 'R137.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Hersheys-Cookies-n-Creme-Dipped-Pretzels-120g.pptx.png', "Hershey's", '120g'),
    ("Hershey's Cookies 'n Chocolate Bar", 'R9.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Hersheys-Cookies-n-Chocolate-40g.pptx-1.png', "Hershey's", '40g'),
    ("Hershey's Cookies 'n Creme Bar", 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Hersheys-Cookies-n-Creme-40g.pptx.png', "Hershey's", '40g'),
    ('Highland Speciality Shortbread Assortment', 'R57.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/highland-shortbread-assort.webp', 'Highland', '200g'),
    ('Highland Speciality Shortbread Petticoat Tails', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/highland-shortbread-petticoat.webp', 'Highland', '125g'),
    ('Hill Coconut Creams', 'R15.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/hill-coconut.png', 'Hill', '150g'),
    ('Hubba Bubba Original', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Hubba-Bubba-Original-5pk.jpg', 'Hubba Bubba', '5pc'),
    ('Hubba Bubba Strawberry', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Hubba-Bubba-Stawberry-5pk.jpg', 'Hubba Bubba', '5pc'),
    ('Hula Hoops BBQ Beef', 'R26.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Hula-Hoops-BBQ-Beef-34g.pptx.png', 'Hula Hoops', '34g'),
    ('Hula Hoops Cheese & Onion', 'R26.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Hula-Hoops-Cheese-Onion-34g.pptx.png', 'Hula Hoops', '34g'),
    ('Hula Hoops Original', 'R26.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Hula-Hoops-Original-34g.pptx.png', 'Hula Hoops', '34g'),
    ('Hula Hoops Salt & Vinegar', 'R26.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Hula-Hoops-Salt-Vinegar-34g.pptx.png', 'Hula Hoops', '34g'),
    ('Hula Hoops Variety Pack', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Hula-Hoops-Variety-6pk.pptx.png', 'Hula Hoops', '6pk'),
    ("Hunter's Black Truffle", 'R20.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/12/Hunters-Black-Truffle-100g.webp', "Hunter's", '100g'),
    ("Hunter's Black Truffle & Parmesan", 'R20.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/12/Hunters-Black-Truffle-Parmesan-100g.webp', "Hunter's", '100g'),
    ("Hunter's White Truffle & Porcini", 'R15.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/12/Hunters-White-Truffle-Porcini-100g.jpg', "Hunter's", '100g'),
    ('Ice Breakers Strawberry & Mixed Berry Sours', 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Icebreakers-Sours-Strawberry-Mixed-Berry-42g-ChatGPT.pptx.png', 'Ice Breakers', '42g'),
    ('Ice Breakers Watermelon & Green Apple Sours', 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Icebreakers-Sours-Watermelon-Sour-Apple-42g-ChatGPT.pptx.png', 'Ice Breakers', '42g'),
    ("Jack's Bourbon Cream Biscuits", 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Jacks-Bourbon-Cream-Biscuits-400g.pptx.png', "Jack's", '400g'),
    ("Jack's Custard Cream Biscuits", 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Jacks-Custard-Cream-Biscuits-400g.pptx.png', "Jack's", '400g'),
    ("Jack's Malted Milk Biscuits", 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Jacks-Malted-Milk-Biscuits-200g.pptx.png', "Jack's", '200g'),
    ("Jack's Pink Wafers", 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Jacks-Pink-Wafers-100g.pptx.png', "Jack's", '100g'),
    ('Jacobs Twiglets', 'R64.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/11/Twiglets-105g.jpg', 'Jacobs', '105g'),
    ('Jacobs Twiglets', 'R94.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/08/Twiglets-150g-B.jpg', 'Jacobs', '150g'),
    ('Jacobs Twiglets', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/06/Twiglets-45g.jpg', 'Jacobs', '45g'),
    ("Jakeman's Throat & Chest Honey Lemon Lozenges", 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/08/jakeman-honey.jpg', "Jakeman's", '73g'),
    ('Jakemans Blueberry Soothing Menthol Lozenges', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/jakemans-blueberry.png', 'Jakemans', '73g'),
    ('Jakemans Throat & Chest Lozenges', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/08/Jakemans-Throat-and-chest-losinges-100-g.jpg', 'Jakemans', '73g'),
    ('Jolly Ranchers Sour Gummies', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/jolly-rancher-sour-gummies-3.5oz.png', 'Jolly Ranchers', '99g'),
    ("Kellogg's Fruit Winders Strawberry", 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/09/5053827197212.png.webp', "Kellogg's", '5pk'),
    ("Kellogg's Fruit Winders Strawberry Apple", 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/09/November032217_x700.webp', "Kellogg's", '5pk'),
    ("Kellogg's Fruit Winders Strawberry Blackcurrant", 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/09/551921011_0_640x640.jpg', "Kellogg's", '5pk'),
    ('KP Dry Roasted Peanuts', 'R47.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-KP-Dry-Roasted-Peanuts-65g.pptx.png', 'KP', '65g'),
    ('KP Honey Roasted Peanuts', 'R47.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/honeyroast.png', 'KP', '65g'),
    ('KP Original Salted Peanuts', 'R47.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/download-1.jpg', 'KP', '65g'),
    ('KP Thai Chilli Coated Peanuts', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/09/thaichilli.png.jpg', 'KP', '55g'),
    ("Lees' Snowballs", 'R63.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-mine-card.pptx-1.png', "Lees'", '10pk'),
    ("Lees' Jam Teacakes", 'R63.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-mine-card.pptx.png', "Lees'", '10pk'),
    ('Lion Mini Gems', 'R56.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Lion-Midget-Gems-150-g.jpg', 'Lion', '130g'),
    ('Lotus Original Caramelised Biscuits', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Lotus-Biscoff-250g.pptx.png', 'Lotus Biscoff', '250g'),
    ('Lyons Toffypops', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Lyons-Biscuits-Toffypops-240g.pptx.png', 'Lyons', '240g'),
    ('Lyons Viscount Mint Biscuits', 'R76.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/06/lyons-viscount-biscuits-196g-577120_1024x1024-1.webp', 'Lyons', '196g'),
    ('M&S Percy Pig Original', 'R84.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/percy-pig-170g.jpg', 'M&S', '170g'),
    ('M&S Percy Pig Piglets', 'R84.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/percy-pigs-piglets.jpg', 'M&S', '170g'),
    ('M&S Percy Pig Reversy', 'R84.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/percy-pigs-reversy.jpg', 'M&S', '170g'),
    ('M&S Percy Pig Veggie', 'R84.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/percy-pigs-veggie.jpg', 'M&S', '170g'),
    ('Maltesers Big Bag', 'R53.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Malteser-Kingsize-Bag-58.5g.jpg', 'Maltesers', '58.5g'),
    ('Maltesers Box', 'R129.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/03/1-1.webp', 'Maltesers', '110g'),
    ('Maltesers Teaser Bar', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Malteser-Teaser-Bar-35g.jpg', 'Maltesers', '35g'),
    ('Marmite Rice Cakes', 'R28.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Marmite-Rice-Cakes-25.jpg', 'Marmite', '25g'),
    ('Marmite Rice Cakes Tube', 'R66.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Marmite-Rice-Cakes-110.jpg', 'Marmite', '110g'),
    ('Mars Galaxy Counters Treat Bag', 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/counters.png', 'Galaxy', '78g'),
    ('Mars Galaxy Milk Chocolate Digestives', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/galaxydigestives.webp', 'Galaxy', '300g'),
    ('Mars Revels Pouch', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-Mars-Revels-101g.pptx.png', 'Mars', '101g'),
    ('Maryland Chocolate & Hazelnut Biscuits', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Maryland-Chocolate-Hazelnut-Biscuits-200g.pptx.png', 'Maryland', '200g'),
    ('Maryland Double Chocolate Biscuits', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Maryland-Double-Chocolate-Biscuits-200g.pptx.png', 'Maryland', '200g'),
    ("Maynard's Murray Mints", 'R66.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/maynard-bassetts-maynard-bassetts-murray-mints-193.webp', "Maynard's", '193g'),
    ("Maynards Bassett's Liquorice Allsorts", 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/1-1.webp', 'Maynards', '130g'),
    ('Maynards Bassetts Sports Mix', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Maynards-Bassetts-Sports-Mix-130g.pptx.png', 'Maynards', '130g'),
    ('Maynards Sherbet Lemons', 'R68.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/sherbet-lemons-114.webp', 'Maynards', '192g'),
    ("McVitie's Club Mint", 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Mcvities-Club-Mint-7pk.pptx.png', "McVitie's", '7pk'),
    ("McVitie's Club Orange", 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Mcvities-Club-Orange-7pk.pptx.png', "McVitie's", '7pk'),
    ("McVitie's Club Salted Caramel", 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Mcvities-Club-Salted-Caramel-7pk.pptx.png', "McVitie's", '7pk'),
    ("McVitie's Digestives Dark Chocolate", 'R45.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Mcvities-Digestives-Dark-Chocolate.pptx.png', "McVitie's", '266g'),
    ("McVitie's Digestives Original", 'R50.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Mcvities-Digestives-Original.pptx.png', "McVitie's", '360g'),
    ("McVitie's Fruit Shortcake Biscuits", 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Mcvities-Fruit-Shortcake.pptx.png', "McVitie's", '200g'),
    ("McVitie's Ginger Nuts", 'R103.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-Mcvities-Ginger-Nuts-Fiery-One.pptx.png', "McVitie's", '250g'),
    ("Mcvitie's Gold Billions Wafer", 'R24.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Mcvities-Gold-Billions-Wafer-39g.pptx.png', "McVitie's", '39g'),
    ("McVitie's Hobnobs Dark Chocolate", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Mcvities-Hobnobs-Dark-Chocolate.pptx.png', "McVitie's", '262g'),
    ("McVitie's Hobnobs Milk Chocolate", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Mcvities-Hobnobs-Milk-Chocolate.pptx.png', "McVitie's", '262g'),
    ("McVitie's Hobnobs Original", 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Mcvities-Hobnobs-Oaty-One.pptx.png', "McVitie's", '255g'),
    ("McVitie's Iced Gems", 'R64.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/mcv-iced-gems.jpg', "McVitie's", '5pk'),
    ("McVitie's Iced Gems Candy Floss Flavour", 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/Iced-Gems-Candy-floss.jpg', "McVitie's", '5pk'),
]

make_page(os.path.join(BASE_DIR, 'cat-confectionery.html'), 'Confectionery', '🍬', confectionery)

# ── GROCERIES (171 products) ──────────────────────────────────────────────────
groceries = [
    ('Ainsley Harriott Caribbean Inspired Couscous', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/08/bb-Ainsley-Harriott-Caribbean-Inspired-Couscous.pptx.png', 'Ainsley Harriott', '100g'),
    ('Ainsley Harriott Couscous Moroccan Medley', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ainsley-Harriott-Moroccan-Medley-Couscous.pptx.png', 'Ainsley Harriott', '100g'),
    ('Ainsley Harriott Couscous Roasted Vegetable', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ainsley-Harriott-Roasted-Vegetable-Couscous.pptx.png', 'Ainsley Harriott', '100g'),
    ('Ainsley Harriott Couscous Spice Sensation', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ainsley-Harriott-Spice-Sensation-Couscous.pptx.png', 'Ainsley Harriott', '100g'),
    ('Ainsley Harriott Couscous Sundried Tomato & Garlic', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ainsley-Harriott-Sundried-Tomato-Garlic-Couscous.pptx.png', 'Ainsley Harriott', '100g'),
    ('Ainsley Harriott Couscous Tomato & Chilli', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ainsley-Harriott-Tomato-Chilli-Couscous.pptx.png', 'Ainsley Harriott', '100g'),
    ('Ainsley Harriott Couscous Wild Mushroom', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ainsley-Harriott-Wild-Mushroom-Couscous.pptx.png', 'Ainsley Harriott', '100g'),
    ('Ainsley Harriott Cup Soup Aromatic Thai Chicken & Lemongrass', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ainsley-Harriott-Thai-CHicken-Lemongrass-Cup-Soup.pptx.png', 'Ainsley Harriott', '3 sachets'),
    ('Ainsley Harriott Cup Soup Broccoli & Stilton', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ainsley-Harriott-Broccoli-Stilton-Cup-Soup.pptx.png', 'Ainsley Harriott', '3 sachets'),
    ('Ainsley Harriott Cup Soup Cream of Wild Mushroom', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ainsley-Harriott-Cream-of-Wild-Mushroom-Cup-Soup.pptx.png', 'Ainsley Harriott', '3pk'),
    ('Ainsley Harriott Cup Soup Italian Minestrone', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ainsley-Harriott-Italian-Minestrone-Cup-Soup.pptx.png', 'Ainsley Harriott', '3pk'),
    ('Ainsley Harriott Cup Soup Szechuan Hot & Sour', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ainsley-Harriott-Szechuan-Hot-Sour-Cup-Soup.pptx.png', 'Ainsley Harriott', '3pk'),
    ('Ainsley Harriott Cup Soup Scottish Chicken & Leek', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bb-Ainsley-Harriott-Scottish-Style-Chicken-Leek-Cup-Soup.pptx.png', 'Ainsley Harriott', '3pk'),
    ('Ainsley Harriott New England Vegetable Chowder Cup Soup', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/08/bb-Ainsley-Harriott-New-England-Vegetable-Chowder-Cup-Soup.pptx.png', 'Ainsley Harriott', '3pk'),
    ('Ainsley Harriott Sweet & Spicy Caribbean Cup Soup', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/bb-Ainsley-Harriott-Sweet-Spicy-Caribbean-Cup-Soup.pptx.png', 'Ainsley Harriott', '3pk'),
    ('Ambrosia Devon Custard', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/images-7.jpg', 'Ambrosia', '400g'),
    ('Ambrosia Rice Pudding', 'R73.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Ambrosia-Rice-Pud-Orig-400.jpg', 'Ambrosia', '400g'),
    ('Atora Original Beef Suet', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/11/atora.jpg', 'Atora', '200g'),
    ('Atora Vegetable Suet', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/11/atora-shredded-vegetable-suet-200g.png', 'Atora', '200g'),
    ("Aunt Bessie's American Style Pancake Mix", 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/bb-Aunt-Bessies-American-Style-Pancake-Waffle-Mix-200g.pptx.png', "Aunt Bessie's", '200g'),
    ("Aunt Bessie's Gluten Free Sage & Onion Stuffing Mix", 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/AUNTBESSIEGLUTENFREESTUFFINGMIX.webp', "Aunt Bessie's", '140g'),
    ("Aunt Bessie's Gluten Free Yorkshire Pudding Mix", 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Aunt-Bessies-Gluten-Free-Yorkshire-Pudding-Mix-120g.pptx.png', "Aunt Bessie's", '120g'),
    ("Aunt Bessie's Golden Crumble Mix", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/bb-Aunt-Bessies-Crumble-Mix-400g.pptx.png', "Aunt Bessie's", '400g'),
    ("Aunt Bessie's Homely & Hearty Dumpling Mix", 'R23.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bb-Aunt-Bessies-Hearty-Homely-Dumpling-Mix-140g.pptx.png', "Aunt Bessie's", '140g'),
    ("Aunt Bessie's Homestyle Sage & Onion Stuffing Mix", 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/01/AUNT-BESSIES-STUFFING-240G.webp', "Aunt Bessie's", '240g'),
    ("Aunt Bessie's Smooth & Creamy Instant Custard", 'R27.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Aunt-Bessies-Instant-Custard-70g.pptx.png', "Aunt Bessie's", '70g'),
    ("Aunt Bessie's Yorkshire Pudding Mix", 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/Yorkshire-pud.jpg', "Aunt Bessie's", '120g'),
    ("Aunt Bessie's Shortcrust Pastry Mix", 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Aunt-Bessies-Shortcrust-Pastry-Mix-500g.pptx.png', "Aunt Bessie's", '500g'),
    ('Batchelors Bigga Marrowfat Peas', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Batchelors-Marrowfat-Bigga-Peas-300-g.jpg', 'Batchelors', '300g'),
    ('Batchelors Mushy Peas "Chip Shop Style"', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Batchelors-Mushy-Peas-Chip-Shop-300-g.jpg', 'Batchelors', '300g'),
    ('Batchelors Mushy Peas "Original"', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Batchelors-Mushy-Peas-Original-300-g.jpg', 'Batchelors', '300g'),
    ('Baxters Caramelised Onion Chutney', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Baxters-Caramelised-Onion-Chutney-.pptx.png', 'Baxters', '290g'),
    ('Baxters Mint Jelly', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/bb-Baxters-Mint-Sauce.pptx.png', 'Baxters', '210g'),
    ('Baxters Red Currant Jelly', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/bb-Baxters-Redcurrant-Jelly.pptx.png', 'Baxters', '210g'),
    ("Bird's Custard Powder", 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/11/2998-Birds-Custard-Powder-250g.webp', "Bird's", '250g'),
    ('Bisto Curry Sauce Mix', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/d26fc926-f559-49f2-83a4-6d178a204e7d.png', 'Bisto', '185g'),
    ('Bisto Gravy Granules Chicken', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Bisto-Chicken-Granules-190g.pptx.png', 'Bisto', '190g'),
    ('Bisto Gravy Granules Original', 'R139.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Bisto-Beef-Granules-190g.pptx.png', 'Bisto', '190g'),
    ('Bisto Gravy Granules Vegetable', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/Bistoveg2.webp', 'Bisto', '190g'),
    ('Blue Dragon Dark Soy Sauce', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/Blue_Dragon_Dark_Soy_Sauce.png', 'Blue Dragon', '150ml'),
    ('Blue Dragon Light Soy Sauce', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/light-soy.webp', 'Blue Dragon', '150ml'),
    ('Branston Baked Beans', 'R45.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/images-1-1.jpg', 'Branston', '410g'),
    ('Branston Baked Beans', 'R159.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/images-2-1.jpg', 'Branston', '4x410g'),
    ('Branston Original Piccalilli', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/BRANSTON-PICCALILLI-360G.jpeg', 'Branston', '360g'),
    ('Branston Pickle Original', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/bb-Branston-Pickle-Original-360g.pptx.png', 'Branston', '360g'),
    ('Branston Pickle Original', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Branston-Pickle-Original-520g.pptx.png', 'Branston', '520g'),
    ('Branston Pickle Small Chunk', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/bb-Branston-Pickle-Small-Chunk-360g.pptx-1.png', 'Branston', '360g'),
    ('Branston Pickle Small Chunk', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Branston-Pickle-Small-Chunk-520g.pptx.png', 'Branston', '520g'),
    ("Campbell's Cream Of Chicken Condensed Soup", 'R30.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Campbells-Cream-of-Chicken-Soup-295g.pptx.png', "Campbell's", '295g'),
    ("Campbell's Cream Of Mushroom Condensed Soup", 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Campbells-Cream-of-Mushroom-Soup-295g.pptx.png', "Campbell's", '295g'),
    ("Campbell's Cream Of Tomato Condensed Soup", 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Campbells-Cream-of-Tomato-Soup-295g.pptx.png', "Campbell's", '295g'),
    ('Chicken Tonight Creamy Mushroom', 'R85.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/08/creamy-mushroom.jpg', 'Chicken Tonight', '500g'),
    ("Colman's Beef Casserole Mix", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Colmans-Beef-Casserole-40g.pptx.png', "Colman's", '40g'),
    ("Colman's Chicken Casserole", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Colmans-Chicken-Casserole-40g.pptx.png', "Colman's", '40g'),
    ("Colman's Chicken Chasseur Mix", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Colmans-Chicken-Chasseur-43g.pptx.png', "Colman's", '43g'),
    ("Colman's Chilli Con Carne Mix", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Colmans-Chilli-Con-Carne-Mix-50g.pptx.png', "Colman's", '50g'),
    ("Colman's Shepherds Pie Mix", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Colmans-Shepherds-Pie-Mix-50g.pptx.png', "Colman's", '50g'),
    ("Colman's Spaghetti Bolognese Seasoning Mix", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Colmans-Spaghetti-Bolognese-44g.pptx.png', "Colman's", '44g'),
    ("Colman's Apple Sauce", 'R65.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Colmans-Apple-Sauce-155g.pptx.png', "Colman's", '155g'),
    ("Colman's Bread Sauce", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Colmans-Bread-Sauce-40g.pptx.png', "Colman's", '40g'),
    ("Colman's Cottage Pie Mix", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bb-Colmans-Cottage-Pie-Mix-45g.pptx.png', "Colman's", '45g'),
    ("Colman's English Mustard Squeezee", 'R114.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Colmans-Mustard-Banging-On-Bangers-150g.pptx.png', "Colman's", '150g'),
    ("Colman's Horseradish Sauce", 'R65.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/bb-Colmans-Horseradish-Sauce-136g.pptx.png', "Colman's", '136g'),
    ("Colman's Mint Sauce", 'R65.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/09/1804808-8714100536186.png.rendition.274.274.png', "Colman's", '165g'),
    ("Colman's Onion Sauce", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/bb-Colmans-Onion-Sauce-35g.pptx.png', "Colman's", '35g'),
    ("Colman's Parsley Sauce", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/bb-Colmans-Parsley-Sauce-20g.pptx.png', "Colman's", '20g'),
    ("Colman's Pepper Sauce", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/bb-Colmans-Pepper-Sauce-40g.pptx.png', "Colman's", '40g'),
    ("Colman's Tartare Sauce", 'R30.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Colmans-Tartare-Sauce-144g.pptx.png', "Colman's", '144g'),
    ("Colman's White Sauce", 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/bb-Colmans-White-Sauce-25g.pptx.png', "Colman's", '25g'),
    ('Daddies Favourite Brown Sauce', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/02/Daddies-Brown-400.jpg', 'Daddies', '400g'),
    ('Encona Extra Hot Pepper Sauce', 'R42.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/EnconaWestIndianExtraHotPepperSauce-142ml_8e3d74f9-08cf-4612-afca-a9ed05ddb2ad_1024x1024.webp', 'Encona', '142ml'),
    ('Encona Mango Chilli Sauce', 'R42.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/encona_mango_chilli_medium_sauce142ml.webp', 'Encona', '142ml'),
    ('Encona South Carolina Carolina Reaper', 'R42.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/reaper.jpg', 'Encona', '142ml'),
    ('Encona West Ind Hot Pepper Sauce (Original)', 'R42.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Encona-West-Ind-Hot-Pepper-Sauce-142ml.jpg', 'Encona', '142ml'),
    ('Frank Coopers Fine Cut Marmalade', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/images-1-2.jpg', 'Frank Coopers', '454g'),
    ("Frank's Red Hot Buffalo Wings Sauce", 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Franks-Red-Hot-Buffalo-Wings-Sauce-148ml.pptx.png', "Frank's Red Hot", '148ml'),
    ("Frank's Red Hot Original Cayenne Pepper Sauce", 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Franks-Red-Hot-Original-Sauce-148ml.pptx-1.png', "Frank's Red Hot", '148ml'),
    ('Fray Bentos Meaty Puds Steak & Kidney', 'R135.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/Fray-Bentos-Meaty-Puds-Steak-Kidney-200g.png', 'Fray Bentos', '200g'),
    ('Fray Bentos Minced Beef & Onion Pie', 'R159.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/FRAY-BEEF-ONION-1.jpg', 'Fray Bentos', '425g'),
    ('Fray Bentos Steak & Gravy Pie', 'R159.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/FRAY-STEAK-GRAVY.jpg', 'Fray Bentos', '425g'),
    ('Fray Bentos Steak & Kidney Pie', 'R159.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/Fray-Bentos-Steak-Kidney-Pie.png', 'Fray Bentos', '425g'),
    ("French's Classic Yellow Mustard", 'R82.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/e6a8611c-09a6-46c2-8d79-f755f85cf889.png', "French's", '218ml'),
    ('Fry Light Olive Oil Spray', 'R129.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/fry-olive-oil-300x300-1.png', 'Fry Light', '190ml'),
    ('Gia Garlic Puree "In Sunflower Oil"', 'R54.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Gia-Garlic-Puree.jpg', 'Gia', '90g'),
    ('GoldenFry Chip Shop Batter Mix', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Goldenfry-Chip-Shop-Batter-Mix-170g-ChatGPT.pptx.png', 'GoldenFry', '170g'),
    ('Goldenfry Chip Shop Curry Sauce Granules', 'R63.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Goldenfry-Chip-Shop-Curry-Granules-160g-ChatGPT.pptx.png', 'GoldenFry', '160g'),
    ('GoldenFry Farmhouse Style Dumpling Mix', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Goldenfry-Dumpling-Mix-142g-ChatGPT.pptx.png', 'GoldenFry', '142g'),
    ('GoldenFry Yorkshire Pudding & Pancake Mix', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Goldenfry-Yorkshire-Pudding-Pancake-Mix-142gChatGPT.pptx.png', 'GoldenFry', '142g'),
    ("Grant's Premium Haggis", 'R104.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/images-1.jpg', "Grant's", '392g'),
    ('Grey Poupon Dijon Mustard', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/grey-poupon-dijon.png', 'Grey Poupon', '215g'),
    ('Heinz Baked Beans 4x415g', 'R218.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/images-8.jpg', 'Heinz', '4x415g'),
    ('Heinz Beans Richmond Sausages', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/richmond.jpg', 'Heinz', '415g'),
    ('Heinz Chicken & Mushroom Soup', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/chick-and-mushroom.jpg', 'Heinz', '400g'),
    ('Heinz Cream of Chicken Soup', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Heinz-Cream-of-Chicken-Soup-400g.pptx.png', 'Heinz', '400g'),
    ('Heinz Cream of Mushroom Soup', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Heinz-Cream-Of-Mushroom-Soup-400g.pptx.png', 'Heinz', '400g'),
    ('Heinz Cream of Tomato Soup', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Heinz-Cream-Of-Tomato-Soup-400g.pptx.png', 'Heinz', '400g'),
    ('Heinz Salad Cream', 'R102.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-Heinz-Salad-Cream-325g.pptx.png', 'Heinz', '325g'),
    ('Heinz Salad Cream Original', 'R159.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/salad-cream.jpg', 'Heinz', '425g'),
    ('Heinz Sandwich Spread', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Heinz-Sandwich-Spread-300g.jpg', 'Heinz', '300g'),
    ('Heinz Spaghetti Richmond Pork Sausages', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/heinz-spaghetti.jpg', 'Heinz', '400g'),
    # Page 2
    ('Heinz Tomato Ketchup Squeezy Bottle', 'R177.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/tomato-ketchup.jpg', 'Heinz', '460g'),
    ('Heinz Vegetable Soup', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Heinz-Vegetable-Soup-400g.pptx.png', 'Heinz', '400g'),
    ('Heinz Yellow Mustard', 'R20.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/1578388316825_540x540.png', 'Heinz', '240ml'),
    ("Hellmann's Light Mayonnaise", 'R118.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/download-5.jpg', "Hellmann's", '430ml'),
    ("Hellmann's Real Mayonnaise Squeezy Bottle", 'R118.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/hellmann.jpg', "Hellmann's", '404g'),
    ("Henderson's Relish", 'R95.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/03/hendersons-.pptx.jpg', "Henderson's", '284ml'),
    ('HP Original Sauce', 'R199.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/03/HP-600ml.jpg', 'HP', '600g'),
    ('Kikkoman Soy Sauce', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/Kikkoman-Soy-Sauce-148ml.webp', 'Kikkoman', '150ml'),
    ('Knorr Ham Stock Cubes', 'R92.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/knorr-ham.jpg', 'Knorr', '80g'),
    ('Kraft Vegemite', 'R129.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Kraft-Vegemite-220g.jpg', 'Kraft', '220g'),
    ('Lea & Perrins Worcester Sauce', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/Lea_PerrinsWorcestershireSauce150Ml_1600x.webp', 'Lea & Perrins', '150ml'),
    ('Levi Roots Reggae Reggae Jerk BBQ Sauce', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Levi-Roots-Reggae-Reggae-Jerk-BBQ-Sauce-310g.jpg', 'Levi Roots', '290g'),
    ('Lion Dijon Mustard', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/dijon.jpg', 'Lion', '185g'),
    ('Lion Horseradish Sauce', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/Horseradish-_D3_9070-scaled.png', 'Lion', '185g'),
    ('Lo Salt', 'R115.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/images-18.jpg', 'Lo Salt', '350g'),
    ('Lotus Biscoff Crunchy Spread', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Lotus-Biscoff-Crunchy-380g.pptx-1.png', 'Lotus Biscoff', '380g'),
    ('Lotus Biscoff Smooth Spread', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Lotus-Biscoff-Smooth-400g.pptx.png', 'Lotus Biscoff', '400g'),
    ("Lyle's Black Treacle Tin", 'R76.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Lyles-Black-Treacle-454g-Tin.pptx.png', "Lyle's", '454g'),
    ("Lyle's Golden Syrup Maple Squeezy", 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Lyles-Golden-Syrup-Maple-Flavour-Squeezy-454g.jpg', "Lyle's", '454g'),
    ("Lyle's Golden Syrup Tin", 'R76.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Lyles-Golden-Syrup-454g-Tin.pptx.png', "Lyle's", '454g'),
    ("Lyle's Golden Syrup Squeezy", 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Lyles-Golden-Syrup-325g.pptx.png', "Lyle's", '325g'),
    ('Maldon Sea Salt Flakes', 'R118.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/Maldon8oz.webp', 'Maldon', '250g'),
    ('Marmite Yeast Extract', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/marmite-yeast-extract-125g.jpg', 'Marmite', '125g'),
    ('McDougalls Thickening Granules', 'R56.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/McDougalls-Thickening-Granules-170g.jpg', 'McDougalls', '170g'),
    ('Nutini Chocolino Cocoa & Hazelnut Spread', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/nutini_chocolino_cocoa_and_hazelnut_spread_300g_101951_T1.jpg', 'Nutini', '300g'),
    ('Nutini Smooth Caramelised Biscuit Spread', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/NUTINI-CARAMEL-BISCUIT-SPREAD-300G.jpeg', 'Nutini', '300g'),
    ('Opies Pickled Walnuts', 'R232.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-Opies-Pickled-Walnuts-390g.pptx.png', 'Opies', '390g'),
    ('Oxo Beef Cubes', 'R104.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/beef.webp', 'Oxo', '12pk'),
    ('Oxo Chicken Cubes', 'R104.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/chicken.webp', 'Oxo', '12pk'),
    ('Oxo Vegetable Cubes', 'R104.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/vegetable.webp', 'Oxo', '12pk'),
    ("Parson's Pickled Cockles", 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb7c39_c0599c0689124a5f9a270bed3a2fd663mv2.webp', "Parson's", '155g'),
    ("Parson's Pickled Mussels", 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/accord_fileqee35l.jpeg', "Parson's", '162g'),
    ("Patak's Balti Spice Paste", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Pataks-Balti-Spice-Paste-283g.pptx.png', "Patak's", '283g'),
    ("Patak's Butter Chicken Cooking Sauce", 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bb-Pataks-Butter-Chicken-Cooking-Sauce-450g.pptx.png', "Patak's", '450g'),
    ("Patak's Chilli Pickle", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Pataks-Chilli-Pickles-283g.pptx.png', "Patak's", '283g'),
    ("Patak's Garlic Pickle", 'R88.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb-Pataks-Garlic-Pickle-283g.pptx.png', "Patak's", '300g'),
    ("Patak's Hot Lime Pickle", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb-Pataks-Hot-Lime-Pickle-283g.pptx.png', "Patak's", '283g'),
    ("Patak's Korma Cooking Sauce", 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Pataks-Korma-Cooking-Sauce-450g.pptx.png', "Patak's", '450g'),
    ("Patak's Korma Spice Paste", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bb-Pataks-Korma-Spice-Paste-290g.pptx.png', "Patak's", '290g'),
    ("Patak's Lime Pickle", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb-Pataks-Lime-Pickle-283g.pptx.png', "Patak's", '283g'),
    ("Patak's Madras Spice Paste", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bb-Pataks-Madras-Spice-Paste-283g.pptx.png', "Patak's", '283g'),
    ("Patak's Mango Pickle", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Pataks-Mango-Pickle-283g.pptx.png', "Patak's", '283g'),
    ("Patak's Rogan Josh Cooking Sauce", 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Pataks-Rogan-Josh-Cooking-Sauce-450g.pptx.png', "Patak's", '450g'),
    ("Patak's Rogan Josh Spice Paste", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bb-Pataks-Rogan-Josh-Spice-Paste-283g.pptx.png', "Patak's", '283g'),
    ("Patak's Tandoori Marinade Paste", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Pataks-Tandoori-Marinade-Paste-283g.pptx.png', "Patak's", '312g'),
    ("Patak's Tikka Marinade Paste", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb-Pataks-Tikka-Marinade-Paste-283g.pptx.png', "Patak's", '300g'),
    ("Patak's Tikka Masala Cooking Sauce", 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bb-Pataks-Tikka-Masala-Cooking-Sauce-450g.pptx.png', "Patak's", '450g'),
    ("Patak's Vindaloo Cooking Sauce", 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Pataks-Vindaloo-Cooking-Sauce-450g.pptx.png', "Patak's", '450g'),
    ("Patak's Vindaloo Spice Paste", 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bb-Pataks-Vindaloo-Spice-Paste-283g.pptx.png', "Patak's", '283g'),
    ('Paxo Sage & Onion Stuffing Mix', 'R118.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Paxo-Sage-Onion-Stuffing-170g-Seasonal-.jpg', 'Paxo', '170g'),
    ('Paxo Sage & Onion Stuffing Mix', 'R132.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/09/paxo-sage-onion-stuffing-mix-340g.png', 'Paxo', '340g'),
    ('Pot Noodle Beef and Tomato', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Pot-Noodle-Beef-Tomato-90g.pptx.png', 'Pot Noodle', '90g'),
    ('Pot Noodle Bombay Bad Boy', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Pot-Noodle-Bombay-Bad-Boy-90g.pptx.png', 'Pot Noodle', '90g'),
    ('Pot Noodle Chicken & Mushroom', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Pot-Noodle-Chicken-Mushroom-90g.pptx.png', 'Pot Noodle', '90g'),
    ('Pot Noodle Chinese Chow Mein', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Pot-Noodle-Chinese-Chow-Mein-90g.pptx.png', 'Pot Noodle', '90g'),
    ('Pot Noodle Original Curry', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Pot-Noodle-Original-Curry-90g.pptx.png', 'Pot Noodle', '90g'),
    ('Pot Noodle Sticky Rib', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Pot-Noodle-Sticky-Rib-90g.pptx.png', 'Pot Noodle', '90g'),
    ('Pot Noodle Sweet & Sour', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Pot-Noodle-Sweet-Sour-90g.pptx.png', 'Pot Noodle', '90g'),
    ('Princes Corned Beef', 'R169.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb-Princes-Corned-Beef-200g-ChatGPT.pptx.png', 'Princes', '200g'),
    ('Princes Corned Beef', 'R209.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb-Princes-Corned-Beef-340g-ChatGPT.pptx.png', 'Princes', '340g'),
    ('Princes Salmon Paste', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb-Princes-Salmon-Paste-75g-Paste-ChatGPT.pptx.png', 'Princes', '75g'),
    ('Princes Sardine & Tomato Paste', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb-Princes-Sardine-Tomato-75g-Paste-ChatGPT.pptx.png', 'Princes', '75g'),
    ("Rose's Lemon & Lime Marmalade", 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/lemon-lime.jpg', "Rose's", '454g'),
    ("Rose's Lime Marmalade", 'R139.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/lime-marmalade.jpg', "Rose's", '454g'),
    ("Sarson's Browning Colour", 'R58.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/1-4.webp', "Sarson's", '150ml'),
    ("Sarson's Malt Vinegar", 'R65.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/7145a834-372c-48b2-8d24-5375213b228b.png', "Sarson's", '250ml'),
    ("Sarson's Worcester Sauce", 'R66.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/1-2.webp', "Sarson's", '150ml'),
    ('Schwartz Hot Chilli Con Carne', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/chilli.jpg', 'Schwartz', '41g'),
    ("Sharwood's Chutney Green Label Mango", 'R124.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Sharwoods-Mango-Chutney-360.jpg', "Sharwood's", '360g'),
    ('Splenda Low Calorie Sweetener', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/0017702_0.png', 'Splenda', '75g'),
    ('Splenda Zero Calorie Sweetener', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/01/splenda-mini.webp', 'Splenda', '100 Mini\'s'),
]

make_page(os.path.join(BASE_DIR, 'cat-groceries.html'), 'Groceries', '🛒', groceries)

# ── HOUSEHOLD CLEANING (100 products) ────────────────────────────────────────
cleaning = [
    ('Astonish 2-in-1 Hair & Body Wash For Kids', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-2-in-1-For-Kids-Raspberry-Ripple-ChatGPT.pptx.png', 'Astonish', '400ml'),
    ('Astonish 2-in-1 Shower + Shampoo For Men', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-HairBody-2-in-1-ChatGPT.pptx.png', 'Astonish', '400ml'),
    ('Astonish Carpet Care Shampoo', 'R72.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/Astonish-Carpet-Care-Shampoo-1L.webp', 'Astonish', '1L'),
    ('Astonish Conditioner Apple Fresh', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Apple-Conditioner.pptx.png', 'Astonish', '375ml'),
    ('Astonish Conditioner Coconut Bliss', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Coconut-Conditioner.pptx.png', 'Astonish', '375ml'),
    ('Astonish Conditioner Tropical Oasis', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Tropical-Conditioner.pptx.png', 'Astonish', '375ml'),
    ('Astonish Dishwasher Tablets', 'R269.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Dishwasher-Tablets-100s-ChatGPT.pptx.png', 'Astonish', "100's"),
    ('Astonish Dishwasher Tablets', 'R129.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Dishwasher-Tablets-42s-ChatGPT.pptx.png', 'Astonish', "42's"),
    ('Astonish Fabric Refresher Fresh Linen', 'R35.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/03/bb-Astonish-Fabric-Refresher-Fresh-Linen-550ml-ChatGPT.pptx.png', 'Astonish', '550ml'),
    ('Astonish Fabric Refresher Lavender Escape', 'R35.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/03/bb-Astonish-Fabric-Refresher-Lavender-Escape-550ml-ChatGPT.pptx.png', 'Astonish', '550ml'),
    ('Astonish Fizz & Fresh Toilet Bowl Tablets Pink Peony', 'R56.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Fizz-Fresh-Pink-Peony-ChatGPT.pptx.png', 'Astonish', '8 tablets'),
    ('Astonish Fizz & Fresh Toilet Bowl Tablets Eucalyptus Fresh', 'R56.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Fizz-Fresh-Eucalyptus-ChatGPT.pptx.png', 'Astonish', '8 tablets'),
    ('Astonish Fizz & Fresh Toilet Bowl Tablets Lemon Splash', 'R56.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Fizz-Fresh-Lemon-Splash-ChatGPT.pptx-1.png', 'Astonish', '8 tablets'),
    ('Astonish Floor Cleaner Lavender Blossom', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Floor-Cleaner-Lavender-ChatGPT.pptx.png', 'Astonish', '1L'),
    ('Astonish Floor Cleaner Peony Bloom', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Floor-Cleaner-Peony-Bloom.pptx.png', 'Astonish', '1L'),
    ('Astonish Floor Cleaner Zesty Lemon', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bb-Astonish-Floor-Cleaner-Zesty-Lemon.pptx.png', 'Astonish', '1L'),
    ('Astonish Foam And Fresh Eucalyptus', 'R58.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Foam-Fresh-Eucalyptus-ChatGPT.pptx.png', 'Astonish', '3x48g'),
    ('Astonish Foam And Fresh Lemon Splash', 'R58.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Foam-Fresh-Lemon-Splash-ChatGPT.pptx.png', 'Astonish', '3x48g'),
    ('Astonish Foam And Fresh Pink Peony', 'R58.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Foam-Fresh-Pink-Peony-ChatGPT.pptx.png', 'Astonish', '3x48g'),
    ('Astonish Hob Power Cream', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Hob-Power-Cream.pptx.png', 'Astonish', '500ml'),
    ('Astonish Lavender Haze Disinfectant Spray', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/3714937928.png', 'Astonish', '550ml'),
    ('Astonish Linen Fresh Disinfectant Spray', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/08/bb-Astonish-Linen-Fresh-Disinfectant-Trigger-.pptx.png', 'Astonish', '550ml'),
    ('Astonish Morning Dew Pet Fresh Disinfectant Spray', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/bb-Astonish-Morning-Dew-Disinfectant-Trigger-.pptx.png', 'Astonish', '550ml'),
    ('Astonish Morning Dew Pet Fresh Floor Cleaner', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/08/petfloor2.webp', 'Astonish', '1L'),
    ('Astonish Original Cleaning Paste', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb-Astonish-Original-Cleaning-Paste.pptx.png', 'Astonish', '500g'),
    ('Astonish Oxy Active Tub', 'R65.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/astonish-oxy-active.webp', 'Astonish', '625g'),
    ('Astonish Pink Roses Disinfectant Spray', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/bb-Astonish-Pink-Roses-Disinfectant-Trigger-.pptx-1.png', 'Astonish', '550ml'),
    ('Astonish Protect & Care Anti-Bacterial Aloe Vera Handwash', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Aloe-Vera-Handwash-ChatGPT.pptx.png', 'Astonish', '600ml'),
    ('Astonish Protect & Care Anti-Bacterial Original Handwash', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Original-Blue-Handwash-ChatGPT.pptx.png', 'Astonish', '600ml'),
    ('Astonish Protect & Care Anti-Bacterial Vitamin E Handwash', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Vitamin-E-Handwash-ChatGPT.pptx.png', 'Astonish', '600ml'),
    ('Astonish Protect & Care Laundry Cleanser', 'R62.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/bb-Astonish-Protect-Care-Laundry-Cleanser.pptx.png', 'Astonish', '1L'),
    ('Astonish Shake & Fresh Carpet Lemon Sparkle', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/bb-Astonish-Shake-Fresh-Lemon-Sparkle.pptx.png', 'Astonish', '350g'),
    ('Astonish Shake & Fresh Carpet Pink Blossom', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/bb-Astonish-Shake-Fresh-Pink-Blossom.pptx.png', 'Astonish', '350g'),
    ('Astonish Shake & Fresh Winter Spice', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Astonish-Shake-Fresh-Winter-Spice-300g-ChatGPT.pptx.png', 'Astonish', '300g'),
    ('Astonish Shampoo Apple Fresh', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Apple-Shampoo.pptx.png', 'Astonish', '400ml'),
    ('Astonish Shampoo Coconut Bliss', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Coconut-Shampoo.pptx.png', 'Astonish', '400ml'),
    ('Astonish Shampoo Tropical Oasis', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Tropical-Shampoo.pptx.png', 'Astonish', '400ml'),
    ('Astonish Shower Creme Cosy Cashmere', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Shower-Creme-Cosy-Cashmere.pptx.png', 'Astonish', '400ml'),
    ('Astonish Shower Creme Exotic Coconut', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Shower-Creme-Exotic-Coconut.pptx.png', 'Astonish', '400ml'),
    ('Astonish Shower Creme Silky Rose', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Shower-Creme-Silky-Rose.pptx.png', 'Astonish', '400ml'),
    ('Astonish The Good One Paste', 'R62.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Good-One-Paste.pptx.png', 'Astonish', '500g'),
    ('Astonish Toilet Fresh Eucalyptus', 'R32.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/bb-Astonish-Toilet-Fresh-Eucalyptus.pptx.png', 'Astonish', '750ml'),
    ('Astonish Toilet Fresh Lemon', 'R32.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/bb-Astonish-Toilet-Fresh-Lemon.pptx.png', 'Astonish', '750ml'),
    ('Astonish Toilet Fresh Ocean', 'R32.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/bb-Astonish-Toilet-Fresh-Ocean.pptx.png', 'Astonish', '750ml'),
    ('Astonish Toilet Fresh Peony', 'R32.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/bb-Astonish-Toilet-Fresh-Peony.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Air Fryer Cleaner', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/bb-Astonish-Air-Fryer-Cleaner-Trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Antibacterial Surface Cleanser', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Anti-Bac-Trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Bathroom Cleaner White Jasmine & Basil', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Bathroom-Cleaner-Trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Daily Shower Shine & White Lilies', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Daily-Shower-trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Fabric Refresher Cotton Fresh', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Fabric-Refresher-Trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Grease Lifter Spray', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Grease-Lift-trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Kitchen Cleaner', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Kitchen-Cleaner-trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Mold & Mildew Stain Blaster', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Mould-Blast-Trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Multi Purpose Bicarb of Soda', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/12/bb-Astonish-Bicarb-of-Soda-Trigger-.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Multi-Purpose Bleach Cleaner', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/03/bb-Astonish-Bleach-Trigger-ChatGPT.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Multi-Surface Cleaner Orange Grove', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Multi-Surface-Trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Oxy Active', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Oxy-Active-Trigger-ChatGPT.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Oxy Active Carpet Stain Remover', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Oxy-Active-Carpet-trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Pet Fresh Stain Remover', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bb-Astonish-Pet-Fresh-Stain-Remover-Trigger-.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Stainless Steel & Shine', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/12/bb-Astonish-Stainless-Steel-Trigger-.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Ultimate Lime Blast', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Lime-Blast-Trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Trigger Window & Glass Cleaner', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Window-Glass-Trigger.pptx.png', 'Astonish', '750ml'),
    ('Astonish Zesty Lemon Disinfectant Spray', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/bb-Astonish-Zesty-Lemon-Disinfectant-Trigger-.pptx.png', 'Astonish', '550ml'),
    ('Bin Brite Berry Blast Spray', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/bin-brite-spray-pink.webp', 'Bin Brite', '400ml'),
    ('Bin Brite Berry Blast Tub', 'R75.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/bin-brite-tub-pink.jpg', 'Bin Brite', '500g'),
    ('Bin Brite Citronella & Lemongrass Spray', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/cit-spray.jpg', 'Bin Brite', '400ml'),
    ('Bin Brite Citronella & Lemongrass Tub', 'R75.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/bin-brite-tub-cit.jpg', 'Bin Brite', '500g'),
    ('Bin Brite Island Fruit Spray', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/bin-brite-island-spray.pptx.jpg', 'Bin Brite', '400ml'),
    ('Bin Brite Island Fruit Tub', 'R75.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/bin-brite-island-tub.pptx.jpg', 'Bin Brite', '500g'),
    ('Bin Brite Mediterranean Sun Spray', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/bin-brite-med-spray.pptx.jpg', 'Bin Brite', '400ml'),
    ('Bin Brite Mediterranean Sun Tub', 'R75.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/bin-brite-medi-tub.pptx.jpg', 'Bin Brite', '500g'),
    ('Bin Brite Spring Blossom Spray', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/BIN-BRITE-BIN-ODOUR-NEUTRALISER-SPRAY-SPRING-BLOSSOM-400ML.jpeg', 'Bin Brite', '400ml'),
    ('Bin Brite Spring Blossom Tub', 'R75.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/bin-brite-linen-tub.pptx.jpg', 'Bin Brite', '500g'),
    ('Bin Brite Stick On Bin Freshener Citronella & Lemongrass', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/cit-stick-on.jpg', 'Bin Brite', '2pk'),
    ('Bin Brite Stick On Freshener Berry Blast', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/bin-brite-berry.jpg', 'Bin Brite', '2pk'),
    ('Bin Brite Stick On Freshener Island Fruit', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/bin-brite-island-fruit.png', 'Bin Brite', '2pk'),
    ('Bin Brite Stick On Freshener Lost In Paradise', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/bin-brite-lost-in-paradise.webp', 'Bin Brite', '2pk'),
    ('Bin Brite Stick On Freshener Mediterranean Sun', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/bin-brite-meditteranean.png', 'Bin Brite', '2pk'),
    ('Bin Brite Stick On Outdoor Bin Freshener Citronella', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/09/download-2.jpg', 'Bin Brite', '2pk'),
    ('Bold All in 1 Pink Tulips & White Jasmine 36 Washes', 'R289.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bold-pink.pptx.jpg', 'Bold', '698.4g'),
    ('Bold Lavender & Camomile Laundry Liquid', 'R249.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/08006540929940_c1n1_00415908-scaled.webp', 'Bold', '1023ml'),
    ('Bold Lavender & Camomile All in 1 Pods 12 Washes', 'R184.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bold-lav-12w.pptx.jpg', 'Bold', '232.8g'),
    ('Bold Spring Awakening All in 1 Pods 13 Washes', 'R199.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bold-spring-13w.pptx.jpg', 'Bold', '252.2g'),
    ('Bold Spring Awakening Laundry Gel', 'R174.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/04/f30b0cb5-3e0f-46cd-b3a9-664e19cfc3c9.webp', 'Bold', '840ml'),
    ('Bold Spring Awakening Washing Liquid', 'R329.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/04/08006540995051_c1n1_00415907-scaled.webp', 'Bold', '1995ml'),
    ('Brasso Liquid', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/brasso.png', 'Brasso', '175ml'),
    ('Brillo Soap Pads', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/BRILLO-PADS-10s.jpg', 'Brillo', '10pk'),
    ('Brillo Soap Pads', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/brillo5pk.jpg', 'Brillo', "5's"),
    ('Brillo Soap Pads', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/brillo-pads-6pk.webp', 'Brillo', '6pk'),
    ('Comfort Persil Colour And Fibre Care', 'R93.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/03/persil-1.61-.pptx.jpg', 'Comfort', '700g'),
    ('Comfort Creations Apple Blossom', 'R94.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/comfort-apple-blossom.png', 'Comfort', '900ml'),
    ('Comfort Creations Honey & Sandalwood', 'R95.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/comfort-honeysuckle.jpg', 'Comfort', '900ml'),
    ('Comfort Creations Strawberry & Lily', 'R95.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/Comfort-Creations-Strawberry-_-Lily-Fabric-Conditioner-33-Wash-1.165L_grande.webp', 'Comfort', '900ml'),
    ('Comfort Creations Waterlily & Lime', 'R95.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/Comfort-Creations-Waterlily-_-Lime-Fabric-Conditioner-33-Wash-1.165L-BAA_grande.webp', 'Comfort', '900ml'),
    ('Comfort Fabric Conditioner Pure', 'R121.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-Comfort-Pure-Fabric-Conditioner-.pptx.png', 'Comfort', '870ml'),
    ('Comfort Intense "Fresh Sky" Ironing Water', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Comfort-Intense-Ironing-Water-Fresh-Sky-1-Lt.jpg', 'Comfort', '1L'),
    ('Comfort Scent Booster Elixir Heavenly Fresh', 'R174.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/04/51DPYjuxMWL.jpg', 'Comfort', '460ml'),
    ('Comfort Scent Booster Elixir Summer Bouquet', 'R174.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/04/48014-1728052927.png', 'Comfort', '460ml'),
    ('Daz All In One Pods Cherry Blossom 24 Washes', 'R229.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/03/1-9.webp', 'Daz', '24x19.6g'),
    ('Daz Laundry Powder Cherry Blossom 42 Washes', 'R236.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/Daz-Cherry-Blossom-Powder.png', 'Daz', '42w'),
]

make_page(os.path.join(BASE_DIR, 'cat-cleaning.html'), 'Household Cleaning', '🧹', cleaning)

# ── PERSONAL CARE (170 products) ──────────────────────────────────────────────
personalcare = [
    ('Alberto Balsam Coconut & Lychee Conditioner', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Alberto-Balsam-Coconut-Lychee-Conditioner-350ml.jpg.jpg', 'Alberto Balsam', '350ml'),
    ('Alberto Balsam Coconut & Lychee Shampoo', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Alberto-Balsam-Coconut-Lychee-Shampoo-350ml.jpg', 'Alberto Balsam', '350ml'),
    ('Alberto Balsam Juicy Green Apple Conditioner', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Alberto-Balsam-Juicy-Green-Apple-Conditioner-400ml.jpg', 'Alberto Balsam', '350ml'),
    ('Alberto Balsam Juicy Green Apple Shampoo', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Alberto-Balsam-Juicy-Green-Apple-Shampoo-400ml.jpg', 'Alberto Balsam', '350ml'),
    ('Alberto Balsam Limited Edition Strawberries & Cream Conditioner', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/03/389476-alberto-balsam-strawberries-and-cream-conditioner.jpg', 'Alberto Balsam', '350ml'),
    ('Alberto Balsam Limited Edition Strawberries & Cream Shampoo', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/03/8710908705731_T1_1500x1500.webp', 'Alberto Balsam', '350ml'),
    ('Alberto Balsam Sunkissed Raspberry Conditioner', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/11/Alberto-Balsam-Sunkissed-Raspberry-Conditioner-350ml.jpg.jpg', 'Alberto Balsam', '350ml'),
    ('Alberto Balsam Sunkissed Raspberry Shampoo', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Alberto-Balsam-Sunkissed-Raspberry-Shampoo-350ml.jpg', 'Alberto Balsam', '350ml'),
    ('Andrex Summer Fresh Washlets', 'R34.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/ANDREX-SUMMER-FRESH-WASHLETS-5-029053-580395-v2_500x500.webp', 'Andrex', '36pc'),
    ('Andrex Supreme Air Pocket Quilts Toilet Paper', 'R249.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/andrex-9-roll.png', 'Andrex', '9 Rolls'),
    ('Aquafresh Fresh Minty Mouthwash', 'R64.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Aquafresh-Minty-Mouthwash-500ml-.jpg', 'Aquafresh', '500ml'),
    ('Arm & Hammer Advanced Whitening Toothpaste', 'R95.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/06/download-2.jpg', 'Arm & Hammer', '75ml'),
    ('Astonish 2-in-1 Hair & Body Wash For Kids', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-2-in-1-For-Kids-Raspberry-Ripple-ChatGPT.pptx.png', 'Astonish', '400ml'),
    ('Astonish 2-in-1 Shower + Shampoo For Men', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-HairBody-2-in-1-ChatGPT.pptx.png', 'Astonish', '400ml'),
    ('Astonish Conditioner Apple Fresh', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Apple-Conditioner.pptx.png', 'Astonish', '375ml'),
    ('Astonish Conditioner Coconut Bliss', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Coconut-Conditioner.pptx.png', 'Astonish', '375ml'),
    ('Astonish Conditioner Tropical Oasis', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Tropical-Conditioner.pptx.png', 'Astonish', '375ml'),
    ('Astonish Protect & Care Anti-Bacterial Aloe Vera Handwash', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Aloe-Vera-Handwash-ChatGPT.pptx.png', 'Astonish', '600ml'),
    ('Astonish Protect & Care Anti-Bacterial Original Handwash', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Original-Blue-Handwash-ChatGPT.pptx.png', 'Astonish', '600ml'),
    ('Astonish Protect & Care Anti-Bacterial Vitamin E Handwash', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Astonish-Vitamin-E-Handwash-ChatGPT.pptx.png', 'Astonish', '600ml'),
    ('Astonish Shampoo Apple Fresh', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Apple-Shampoo.pptx.png', 'Astonish', '400ml'),
    ('Astonish Shampoo Coconut Bliss', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Coconut-Shampoo.pptx.png', 'Astonish', '400ml'),
    ('Astonish Shampoo Tropical Oasis', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Tropical-Shampoo.pptx.png', 'Astonish', '400ml'),
    ('Astonish Shower Creme Cosy Cashmere', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Shower-Creme-Cosy-Cashmere.pptx.png', 'Astonish', '400ml'),
    ('Astonish Shower Creme Exotic Coconut', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Shower-Creme-Exotic-Coconut.pptx.png', 'Astonish', '400ml'),
    ('Astonish Shower Creme Silky Rose', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Astonish-Shower-Creme-Silky-Rose.pptx.png', 'Astonish', '400ml'),
    ('Aussie Deep Treatment 3 Minute Miracle Reconstructor', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Aussie-3min-20-ml.jpg', 'Aussie', '20ml'),
    ('Baylis & Harding Goodness Rose & Geranium Handwash', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/Baylis-Harding-Goodness-Rose-Geranium-500ml.webp', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Elements Fresh Lemon & Mint Handwash', 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/BH-Fresh-Lemon-Mint.jpg', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Elements Oud Wood & Bergamot', 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/BH-Oud-Wood-Bergamot-500ml.jpg', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Elements White Tea & Neroli Handwash', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/BH-White-Tea-Neroli-500ml.jpg', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Goodness Oud, Cedar & Amber Handwash', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/oudcederamber.jpg', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Goodness Sea Kelp & Peppermint Handwash', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/BH-Goodness-Sea-Kel-Pep-500.jpg', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Jojoba, Vanilla & Almond Oil Handwash', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/BH-Jojoba-Vanilla-and-Almond-Oil-500ml.jpg', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Black Pepper & Ginseng Handwash', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Baylis-Harding-Black-Pepper-Ginseng-500ml.pptx.png', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Dark Amber & Fig Handwash', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/darkamberfig-1.jpg', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Jasmine & Apple Blossom Anti-Bacterial Handwash', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Baylis-Harding-Jasmine-Apple-Blossom-Anti-Bacterial-Hand-Wash-500ml.jpg', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Limited Edition Tropical Fruit Cocktail Handwash', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/rainbow.jpg', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Pink Blossom & Lotus Flower Handwash', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/Baylis-Harding-Pink-Blossom-Lotus-Flower-500ml-png.jpg', 'Baylis & Harding', '500ml'),
    ('Baylis & Harding Sweet Mandarin & Grapefruit Handwash', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Baylis-Harding-Sweet-Mandarin-Grapefruit-Hand-Wash-500ml.jpg', 'Baylis & Harding', '500ml'),
    ('Chapstick Original SPF10', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/02/Chap-Original.jpg', 'Chapstick', 'SPF10'),
    ('Colgate Cool Stripe Toothpaste Pump', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/GT-2023-01-19T212105.517.webp', 'Colgate', '100ml'),
    ('Colgate Max Whitening Toothpaste Pump', 'R94.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/colgate.webp', 'Colgate', '100ml'),
    ('Colgate Toothpaste Pump', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Colgate-Toothpaste-Pump-100ml.jpg', 'Colgate', '100ml'),
    ('Colgate Total Care Whitening Paste Pump', 'R137.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/03/ff.png', 'Colgate', '100ml'),
    ('Colgate Total Care Whitening Paste Tube', 'R74.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/03/MAT_7200786_PCE_LV.webp', 'Colgate', '75ml'),
    ('Dalton House Sea Breeze Handwash', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/dalton-house-sea-breeze-handwash.webp', 'Dalton House', '500ml'),
    ('Dalton House Sweet Rose Handwash', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/dalton-house-sweet-rose-handwash.webp', 'Dalton House', '500ml'),
    ('Dentiplus Universal Toothbrush Heads', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/03/bb-Dentiplus-Universal-Toothbrush-Heads-2pk.pptx.png', 'Dentiplus', '2pk'),
    ('Eight Triple Eight Colour Protect Conditioner', 'R88.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/ColourProtectConditioner.webp', 'Eight Triple Eight', '1L'),
    ('Eight Triple Eight Colour Protect Shampoo', 'R88.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/ColourProtectShampoo.webp', 'Eight Triple Eight', '1L'),
    ('Eight Triple Eight Hemp Oil Shampoo', 'R88.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Eitht-Triple-Eight-Henp-Oil-Sh-1lt.jpg', 'Eight Triple Eight', '1L'),
    ('Elysium 100% Essential Oil Eucalyptus', 'R38.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Elysium-Oil-Eucalyptus.jpg', 'Elysium', '10ml'),
    ('Elysium Epsom Salts Eucalyptus', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Elysium-Salt-Euca-450.jpg', 'Elysium', '450g'),
    ('Elysium Epsom Salts Lavender', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Elysium-Salt-Lav-450.jpg', 'Elysium', '450g'),
    ('Elysium Epsom Salts Original', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Elysium-Salt-Original-450.jpg', 'Elysium', '450g'),
    ('Elysium Epsom Salts Eucalyptus', 'R63.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/elysium-epsom-salts-euclayptus-1kg.jpg', 'Elysium', '1kg'),
    ('Elysium Muscle & Back Soak Bath Salts with Hemp Oil', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/medicines-2u-elysium-muscle-back-soak-hemp-1737375436ELYSIUM-SOAK-HEMP-X-1.png', 'Elysium', '450g'),
    ('Elysium Muscle & Back Soak Bath Salts With Menthol', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/elysium-bath-soak.webp', 'Elysium', '450g'),
    ('Elysium Spa Mermaid Bath Dust Blueberry', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/mermaid-dust.jpg', 'Elysium', '400g'),
    ('Elysium Spa Unicorn Bath Dust Bubblegum', 'R33.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/bubblegum-dust.jpg', 'Elysium', '400g'),
    ('Enliven Coconut & Vanilla Conditioner', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/enliven-naturals-conditioner-coconut-vanilla-500ml-AH5234-18126.webp', 'Enliven', '500ml'),
    ('Enliven Coconut & Vanilla Shampoo', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/Enliven-Coconut-Vanilla-Shampoo-500ml.jpg', 'Enliven', '500ml'),
    ('Enliven Coconut & Vanilla Conditioner', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Enliven-Coconut-Vanilla-Conditioner-400ml.jpg', 'Enliven', '400ml'),
    ('Enliven Coconut & Vanilla Shampoo', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Enliven-Coconut-Vanilla-Shampoo-400ml.jpg', 'Enliven', '400ml'),
    ('Enliven Cucumber & Garden Mint Hand Gel', 'R54.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Enliven-Cucumber-Garden-Mint-Hand-gel-500.jpg', 'Enliven', '500ml'),
    ('Enliven Dry Shampoo "Original" Sweet Blossom Hair Refresh', 'R59.90', 'https://www.uke.co.za/wp-content/uploads/2024/05/enliven-dry-shap-3.avif', 'Enliven', '300ml'),
    ('Enliven Dry Shampoo Hair Refresh Tropical', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/ENLIVEN-DRY-SHAMPOO-HAIR-REFRESH-TROPICAL-300ML.jpg', 'Enliven', '300ml'),
    ('Enliven Hair Gel Extreme', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Enliven-Gel-Extreme-250.jpg', 'Enliven', '250ml'),
    ('Enliven Hair Gel Extreme', 'R45.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Enliven-Gel-Extreme-500.jpg', 'Enliven', '500ml'),
    ('Enliven Hair Gel Firm', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Enliven-Gel-Firm-250.jpg', 'Enliven', '250ml'),
    ('Enliven Hair Gel Firm', 'R45.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Enliven-Gel-Firm-500.jpg', 'Enliven', '500ml'),
    ('Enliven Hair Gel Ultimate', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Enliven-Gel-Ultimate-250.jpg', 'Enliven', '250ml'),
    ('Enliven Hair Gel Ultimate', 'R45.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Enliven-Gel-Ultimate-500.jpg', 'Enliven', '500ml'),
    ('Enliven Hair Gel Wet', 'R45.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Enliven-Gel-Wet-500.jpg', 'Enliven', '500ml'),
    ('Enliven Hair Mousse Ultra Hold Volume & Curl', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/Enliven-Hair-Mousse-300ml.jpg', 'Enliven', '300ml'),
    ('Enliven Hairspray Ultra Hold', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/enliven-hairspray.jpg', 'Enliven', '300ml'),
    ('Enliven Hydrating Banana & Coconut Conditioner', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/09/C005742_Enliven_Fruits_Conditioner_Banana_Coconut_Visual.webp', 'Enliven', '350ml'),
    ('Enliven Hydrating Banana & Coconut Shampoo', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/09/C005735_Enliven_Fruits_Shampoo_Banana_Coconut_Visual-1.webp', 'Enliven', '350ml'),
    ('Enliven Hydrating Coconut & Macadamia Conditioner', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/09/C005736_Enliven_Fruits_Conditioner_Coconut_Macadamia_visual.webp', 'Enliven', '350ml'),
    ('Enliven Hydrating Coconut & Macadamia Shampoo', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/09/C005738_Enliven_Fruits_Shampoo_Coconut_Macadamia_visual.webp', 'Enliven', '350ml'),
    ('Enliven Hydrating Watermelon & Pomegranate Conditioner', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/09/C005739_Enliven_Fruits_Conditioner_Watermelon_Pomegranate_Visual.webp', 'Enliven', '350ml'),
    ('Enliven Hydrating Watermelon & Pomegranate Shampoo', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/09/C005741_Enliven_Fruits_Shampoo_Watermelon_Pomegranate_Visual.webp', 'Enliven', '350ml'),
    ('Enliven Mouth Wash Cool Mint', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Enliven-Mouth-Wash-Coolmint-500-ml.jpg', 'Enliven', '500ml'),
    ('Enliven Mouth Wash Fresh Mint', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Enliven-Mouth-Wash-Fresh-Mint-500ml.jpg', 'Enliven', '500ml'),
    ('Enliven Mouth Wash Total Care', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Enliven-Mouth-Wash-Total-Care-500ml.jpg', 'Enliven', '500ml'),
    ('Enliven Naturals Shower Gel Coconut/Vanilla', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/grocerapp-enliven-shower-gel-coconut-6454ef78c9e37.webp', 'Enliven', '500ml'),
    ('Enliven Naturals Shower Gel Raspberry/Red Apple', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/61k9A-vIbpL._SL1500_.jpg', 'Enliven', '500ml'),
    ('Enliven Raspberry & Red Apple Conditioner', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/Enliven-Raspberry-Red-Apple-Conditioner-500ml.jpg', 'Enliven', '500ml'),
    ('Enliven Raspberry & Red Apple Shampoo', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/Enliven-Raspberry-Red-Apple-Shampoo-500ml.webp', 'Enliven', '500ml'),
    ('Enliven Raspberry & Red Apple Conditioner', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Enliven-Raspberry-Red-Apple-Conditioner-400ml.jpg', 'Enliven', '400ml'),
    ('Enliven Raspberry & Red Apple Shampoo', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Enliven-Raspberry-Red-Apple-Shampoo-400ml.jpg', 'Enliven', '400ml'),
    ('Enliven Refreshing 3-in-1 Watermelon & Pomegranate Hair Mask', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/09/C005740_Enliven_Fruits_Mask_Watermelon_Pomegranate_Visual.webp', 'Enliven', '350ml'),
    ('Enliven Softening 3-in-1 Banana & Coconut Hair Mask', 'R76.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/09/C005743_Enliven_Fruits_Mask_Banana_Coconut_Visual.webp', 'Enliven', '350ml'),
    ('Enliven Softening 3-in-1 Coconut & Macadamia Hair Mask', 'R76.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/09/C005737_Enliven_Fruits_Mask_Coconut_Macadamia_Visual.webp', 'Enliven', '350ml'),
    ('Enliven Whitening Mouthwash', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/enliven-mouthwash.webp', 'Enliven', '500ml'),
    ('Euthymol Original Toothpaste', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/05/Euthymol-75-ml.jpg', 'Euthymol', '75ml'),
    ('Gillette Blue 2 Blade', 'R74.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/10132917EA-checkers515Wx515H.png', 'Gillette', '5 Pack'),
    ('Gillette Shave Foam Regular', 'R66.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Gillette-Shave-Foam-Regular-200ml.jpg', 'Gillette', '200ml'),
    ('Gillette Shave Foam Sensitive', 'R66.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/eng_pl_Gillette-Shaving-Foam-Sensitive-Skin-200ml-35842_1.png', 'Gillette', '200ml'),
    # Page 2
    ('Gillette Shave Gel Regular', 'R76.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/7702018980901-removebg-preview_1024x1024.webp', 'Gillette', '200ml'),
    ('Gillette Shave Gel Sensitive', 'R76.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/7702018980918-115879_711x711.webp', 'Gillette', '200ml'),
    ('Huggies Extra Care Sensitive', 'R39.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/huggies.jpeg', 'Huggies', '56 Wipes'),
    ('Huggies Wipes All Over Clean', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/09/huggies-all-over-clean-wipes.webp', 'Huggies', '56pk'),
    ('Huggies Wipes Natural Care', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/09/huggiesnaturalcarealoe.png', 'Huggies', '56pk'),
    ('Huggies Wipes Pure', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Huggies-Pure-56.jpg', 'Huggies', '56pk'),
    ('Imperial Leather Original Soap Bars', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/imperialleather2bars.webp', 'Imperial Leather', '2x90g'),
    ('Imperial Leather Original Soap Bars', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/05/imperialleather4bars.webp', 'Imperial Leather', '4x90g'),
    ('Imperial Leather Bergamot & Sea Salt', 'R84.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/IL_New_Curve_Bottle_Energising_250ml_1_v1.jpg', 'Imperial Leather', '500ml'),
    ('Imperial Leather Blue Cypress & Eucalyptus', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/Blue-Cypress-and-Eucalyptus-Packshot-2-scaled-1.jpg', 'Imperial Leather', '500ml'),
    ('Imperial Leather Cotton Clouds & White Cashmere Handwash', 'R35.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-nestle-damak-Baklava.pptx.png', 'Imperial Leather', '300ml'),
    ('Imperial Leather Cotton Flower & Vanilla Bodywash', 'R84.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/5000101513978-IL_New_Curve_Bottle_Moisturising_250ml_1_v1.jpg', 'Imperial Leather', '500ml'),
    ('Imperial Leather Cotton Flower & Vanilla Orchid Handwash', 'R66.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/imperial-leather-moist-hand-wash-500ml.jpg', 'Imperial Leather', '500ml'),
    ('Imperial Leather Energising Foamburst Bergamot & Sea Minerals', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/il-foam-energ.png', 'Imperial Leather', '200ml'),
    ('Imperial Leather Mallow & Rose Milk Body Wash', 'R84.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/289587011_289587011_1_1709744842000_1280x1280.jpg', 'Imperial Leather', '500ml'),
    ('Imperial Leather Mandarin & Neroli Bodywash', 'R84.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/5000101514012-IL_New_Curve_Bottle_Refreshing_250ml_1_v1.jpg', 'Imperial Leather', '500ml'),
    ('Imperial Leather Meadow Honey & Shea Butter Handwash', 'R35.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-Imperial-Leather-Meadow-Honey-Shea-Butter-Hand-Wash-300ml.pptx.png', 'Imperial Leather', '300ml'),
    ('Imperial Leather Moisturising Foamburst Jasmine & Vanilla Orchid', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/il-foam-moisture.png', 'Imperial Leather', '200ml'),
    ('Imperial Leather Nourishing Foamburst Lychee & Lotus Flower', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/il-foam-nourish.png', 'Imperial Leather', '200ml'),
    ('Imperial Leather Original Classic Handwash', 'R34.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/imperial-leather-handwash.jpg', 'Imperial Leather', '300ml'),
    ('Imperial Leather Oud & Frankincense Handwash', 'R66.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/01/imperial-leather-indulg-hand-wah-500ml.jpg', 'Imperial Leather', '500ml'),
    ('Imperial Leather Pampering Foamburst Mallow & Cherry Blossom', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/foamburst.jpg', 'Imperial Leather', '200ml'),
    ('Imperial Leather Relaxing Foamburst Plum Blossom & Cashmere Musk', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/il-relaxing-foam.png', 'Imperial Leather', '200ml'),
    ("Johnson's Baby Bath", 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Johnsons-Baby-Bath-500.jpg', "Johnson's", '500ml'),
    ('Jolly Good Beard Oil Cedarwood', 'R35.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/Jolly-Good-Beard-Oil-30ml.jpg', 'Jolly Good', '30ml'),
    ('Lenor Tumble Dryer Sheets Pink Blossom', 'R116.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/bb-Lenor-Tumble-Dryer-Sheets-Pink-Blossom-34-Sheets-ChatGPT.pptx.png', 'Lenor', '34 Sheets'),
    ('Lenor Tumble Dryer Sheets Spring Awakening', 'R116.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/Lenor_Sheets_Carton_Spring_Awakening_34_UK__1_.png', 'Lenor', '34 Sheets'),
    ('Lenor Tumble Dryer Sheets Summer Breeze', 'R116.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/Tumbledryersheets-summer_500x_510b51b3-63e6-46e4-9de7-debcf9d7d3d7_grande.webp', 'Lenor', '34 Sheets'),
    ('Malibu Aloe Vera After Sun Gel', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-Malibu-Aloe-Vera-After-Sun-Gel-200ml.pptx.png', 'Malibu', '200ml'),
    ('Malibu Ice Blue After Sun Gel', 'R28.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-Malibu-Ice-Blue-After-Sun-Gel-100ml.pptx.png', 'Malibu', '100ml'),
    ('My Little Pony Battery Operated Toothbrush', 'R71.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/mlp-toothbrush.pptx.jpg', 'My Little Pony', ''),
    ('Nuage Tattoo Moisturiser', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/08/Nuage-TAT-150ml.jpg', 'Nuage', '150ml'),
    ('Nuage Make-Up Remover Wipes With Aloe', 'R37.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Nuage-Makeup-rem-wipes-25.jpg', 'Nuage', '25 Wipes'),
    ('Nuage Make-Up Removing Cloth', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Nuage-makeup-Cloth-3pk.jpg', 'Nuage', '3pk'),
    ('Oral B Complete Mouth Wash', 'R41.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Oral-B-Complete-Mouth-Wash-250-ml.jpg', 'Oral B', '250ml'),
    ('Oral B Deep Clean Floss', 'R132.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/Beers-27_01_25.pptx-1.png', 'Oral B', '50m'),
    ('Oral B Deep Healthy Gums', 'R145.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/0005170_oral-b-pro-expert-advanced-healthy-gums-floss-50m_510.png', 'Oral B', '50m'),
    ('Oral B Essential Unwaxed Floss', 'R55.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Oral-B-Waxed-Floss-50-meters.jpg', 'Oral B', '50m'),
    ('Oral B Essential Waxed Floss', 'R55.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/05/Oral-B-Ess-Floss-Waxed.jpg', 'Oral B', '50m'),
    ('Oral B Satin Mint Floss', 'R57.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Oral-B-Satin-Tape-Mint-Floss-25-meter-.jpg', 'Oral B', '25m'),
    ('Oral B Satin Tape', 'R55.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Oral-B-Satin-Tape-25-meter.jpg', 'Oral B', '25m'),
    ('Oral B Superfloss Threader', 'R136.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/oral-b_super-floss_50m_power-image-scaled.webp', 'Oral B', '50 Pre Cut Strands'),
    ('Pears Pure & Gentle With Lemon Flower Extracts Soap', 'R52.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Pears-Soap-Lemon-100-g.jpg', 'Pears', '125g'),
    ('Pears Pure & Gentle With Mint Extracts Soap', 'R52.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/unnamed.jpg', 'Pears', '125g'),
    ('Pears Pure & Gentle With Natural Oils Soap', 'R56.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/709381124-Pears-Transparent-Bar-Soap-with-Natural-Oils-125G.png', 'Pears', '125g'),
    ('Sensodyne Soft Bristle 3 Pack Toothbrushes', 'R148.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Sensodyne-3pk-Soft.jpg', 'Sensodyne', '3pk'),
    ('Simple Moisturising Handwash', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/04/8712561847247_1389e34d-7d1a-4a82-a1cd-9a1bdc3c9dfc_1080x.webp', 'Simple', '250ml'),
    ('Swirl Jewellery Cleaner', 'R46.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/04/bb-Swirl-Jewellery-Cleaner-ChatGPT.pptx.png', 'Swirl', '145ml'),
    ('Venus Satin Care Sensitive Aloe Vera Glide Gel', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/satin-care.jpg', 'Venus', '200ml'),
    ("Wright's Traditional Soap w/Coal Tar Fragrance", 'R144.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-Wrights-Traditional-Soap-4pk-w_coal-fragrance.pptx.png', "Wright's", '4pk'),
    ('XHC Argan Oil Conditioner', 'R42.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/08/conditioner.webp', 'XHC', '300ml'),
    ('XHC Silver Conditioner', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/xhc-condi.pptx.jpg', 'XHC', '400ml'),
    ('XHC Silver Shampoo', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/xhc-shampoo.pptx.jpg', 'XHC', '400ml'),
]

make_page(os.path.join(BASE_DIR, 'cat-personalcare.html'), 'Personal Care & Beauty', '💄', personalcare)

print(f'Written cat-confectionery.html ({len(confectionery)} products)')
print(f'Written cat-groceries.html ({len(groceries)} products)')
print(f'Written cat-cleaning.html ({len(cleaning)} products)')
print(f'Written cat-personalcare.html ({len(personalcare)} products)')
print('All done.')
