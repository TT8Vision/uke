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
  <div class="mobile-menu-header"><span style="font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:700;color:#fff;">UK <em style="font-style:italic;color:var(--gold-light);">Emporium</em></span><button class="mobile-menu-close">✕</button></div>
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

def make_page(filename, title, emoji, products):
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
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'w') as f:
        f.write(html)
    print(f'Written {filename} ({count} products)')

# ── BEERS & ALES ──────────────────────────────────────────────────────────────
beers = [
    ('Abbott Ale', 'R84.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/Abbott-Ale-500ml.jpg?resize=600%2C600&ssl=1', 'Abbott', '500ml'),
    ('Adnams Ghost Ship', 'R74.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Adnams-Ghost-Ship-500ml.pptx.png?resize=600%2C600&ssl=1', 'Adnams', '500ml'),
    ('Angelo Poretti', 'R166.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Angelo-Poretti-4x440ml.pptx.png?resize=600%2C600&ssl=1', 'Angelo Poretti', '4×440ml'),
    ('Badger Tangle Foot Golden Ale', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/Tangle.webp?resize=600%2C600&ssl=1', 'Badger', '500ml'),
    ('Barnstormer Black', 'R34.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Barnstormer-Black-500ml.pptx.png?resize=600%2C600&ssl=1', 'Barnstormer', '500ml'),
    ('Birra Moretti', 'R57.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/birra_moretti.jpg?resize=600%2C600&ssl=1', 'Birra Moretti', '330ml'),
    ('Birra Moretti Lager', 'R219.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/birra.jpg?resize=600%2C600&ssl=1', 'Birra Moretti', '4×440ml'),
    ('Birra Moretti Zero', 'R157.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/Birra-Moretti-Zero-4-Pack-1.png?resize=600%2C600&ssl=1', 'Birra Moretti', '4×330ml'),
    ('Bishops Finger Ale', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/Bishops-Finger-500ml-1.jpg?resize=600%2C600&ssl=1', 'Shepherd Neame', '500ml'),
    ('Black Sheep Ale', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/Black-Sheep-Ale-500ml.jpg?resize=600%2C600&ssl=1', 'Black Sheep', '500ml'),
    ('Boddingtons Draught', 'R45.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/Boddingtons_Draught_Bitter_440ml.webp?resize=600%2C600&ssl=1', 'Boddingtons', '440ml'),
    ('Carlsberg Danish Pilsner', 'R34.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/carlsbergpilsner.jpg?resize=600%2C600&ssl=1', 'Carlsberg', '440ml'),
    ('Carlsberg Export Lager', 'R199.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/Carlsberg-Export-440ml.jpg?resize=600%2C600&ssl=1', 'Carlsberg', '4×440ml'),
    ('Cobra Beer', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/bb-mine-card.pptx-3-1.png?resize=600%2C600&ssl=1', 'Cobra', '620ml'),
    ('Coors Lager', 'R159.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/Coors-4x440ml.png?resize=600%2C600&ssl=1', 'Coors', '4×440ml'),
    ('Desperados Original', 'R249.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Desperados-Original-4pk.pptx.png?resize=600%2C600&ssl=1', 'Desperados', '4×440ml'),
    ('Estrella Damm', 'R25.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/estrella-damm-lager-beer-bottle-24-x-330ml-case-2-56322-p.jpg?resize=600%2C600&ssl=1', 'Estrella Damm', '330ml'),
    ('Estrella Damm', 'R229.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/8410793002204.jpg?resize=600%2C600&ssl=1', 'Estrella Damm', '4×440ml'),
    ("Foster's Shandy", 'R129.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/fosters-lager-shandy-4pk.jpg?resize=600%2C600&ssl=1', "Foster's", '4×440ml'),
    ("Fuller's London Pride Ale", 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/London-Pride.jpg?resize=600%2C600&ssl=1', "Fuller's", '500ml'),
    ('Guinness Draught Zero', 'R239.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/images-1.jpg?resize=600%2C600&ssl=1', 'Guinness', '4×440ml'),
    ('Guinness Original Draught', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/guinness-draught.jpeg?resize=600%2C600&ssl=1', 'Guinness', '4×440ml', 'Irish stout'),
    ('Guinness Original Extra Stout', 'R229.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/Guinness-Original-Stout-1.jpg?resize=600%2C600&ssl=1', 'Guinness', '4×440ml'),
    ('Hobgoblin Gold Beer', 'R86.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/35444thumb.png?resize=600%2C600&ssl=1', 'Hobgoblin', '500ml'),
    ('Hobgoblin Ruby Beer', 'R86.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/bb-Hobgoblin-Ruby-Beer-500ml.pptx.png?resize=600%2C600&ssl=1', 'Hobgoblin', '500ml'),
    ("Inch's Medium Apple Cider", 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Inchs-Medium-Apple-Cider-4pk.pptx.png?resize=600%2C600&ssl=1', "Inch's", '4×440ml'),
    ("Jack Daniel's Coca Cola Cherry", 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Jack-Daniels-Coke-Cherry-330ml.pptx-1.png?resize=600%2C600&ssl=1', "Jack Daniel's", '330ml'),
    ("Jack Daniel's Coca Cola Zero Sugar", 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Jack-Daniels-Coca-Cola-Zero-Sugar-330ml.pptx.png?resize=600%2C600&ssl=1', "Jack Daniel's", '330ml'),
    ('John Smiths Extra Smooth Ale', 'R175.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/John-Smiths-4-pack.jpg?resize=600%2C600&ssl=1', 'John Smiths', '4×440ml'),
    ('Kronenbourg 1664 Lager', 'R219.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/1664-4-pack.jpg?resize=600%2C600&ssl=1', 'Kronenbourg', '4×440ml'),
    ('Leffe Blonde', 'R69.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/bb-Leffe-Blonde-330ml.pptx.png?resize=600%2C600&ssl=1', 'Leffe', '330ml'),
    ('Madri Zero', 'R154.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Madri-Zero-4x330ml.pptx.png?resize=600%2C600&ssl=1', 'Madri', '4×330ml'),
    ('Magners Irish Cider', 'R42.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/magnerscan_jpg.webp?resize=600%2C600&ssl=1', 'Magners', '440ml'),
    ('McEwans Export', 'R216.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/McEwans-Export-4pack.png?resize=600%2C600&ssl=1', 'McEwans', '4×500ml'),
    ("Murphy's Draught Irish Stout", 'R183.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/Murphy_draught_irish_stout.webp?resize=600%2C600&ssl=1', "Murphy's", '4×440ml'),
    ('Newcastle Brown Ale', 'R84.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/Newcastle-Brown-Ale.png?resize=600%2C600&ssl=1', 'Newcastle', '550ml'),
    ('Old Speckled Hen', 'R229.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/Greene_King_Old_Speckled_Hen_Can_-_4_Pack.webp?resize=600%2C600&ssl=1', 'Greene King', '4×440ml'),
    ('Old Speckled Hen', 'R86.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/Old-Speckled-Hen-500ml-e1764233180847.png?resize=600%2C600&ssl=1', 'Greene King', '500ml'),
    ('Peroni Nastro Azzurro', 'R229.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/12/peroni-4pk.webp?resize=600%2C600&ssl=1', 'Peroni', '4×440ml'),
    ('Peroni Nastro Azzurro 0.0%', 'R123.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Peroni-Nastro-Azzurro-0.0-4x330ml-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Peroni', '4×330ml'),
    ('Peroni Nastro Azzurro Gluten Free', 'R57.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Peroni-Nastro-Azzurro-Gluten-Free-330ml-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Peroni', '330ml'),
    ('Red Stripe Lager', 'R150.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/Red-Stripes-4x440ml.jpg?resize=600%2C600&ssl=1', 'Red Stripe', '4×440ml'),
    ('San Miguel 0%', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/San-Miguel-4x330ml-0-2.png?resize=600%2C600&ssl=1', 'San Miguel', '4×330ml'),
    ('San Miguel Especial', 'R43.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/bb-mine-card.pptx-2.png?resize=600%2C600&ssl=1', 'San Miguel', '330ml'),
    ('Scrumpy Jack Cider', 'R229.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/0c0d556a-b240-4023-8eea-e275bc7488e9.png?resize=600%2C600&ssl=1', 'Scrumpy Jack', '4×500ml'),
    ("Sharp's Doom Bar", 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Sharps-Doom-Bar-500ml.pptx.png?resize=600%2C600&ssl=1', "Sharp's", '500ml'),
    ('Singha Thai Lager', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/bb-mine-card.pptx-3.png?resize=600%2C600&ssl=1', 'Singha', '630ml'),
    ('Southern Comfort & Lemonade', 'R63.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Southern-Comfort-Lemonade-330ml.pptx.png?resize=600%2C600&ssl=1', 'Southern Comfort', '330ml'),
    ('Spitfire Ale', 'R86.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/Spitfire-Ale-500ml-3.jpg?resize=600%2C600&ssl=1', 'Shepherd Neame', '500ml'),
    ('Thatchers Gold', 'R145.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Thatchers-Gold-4x440ml.pptx.png?resize=600%2C600&ssl=1', 'Thatchers', '4×440ml'),
    ('Thornbridge 1838', 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Thornbridge-1838-500ml.pptx-1.png?resize=600%2C600&ssl=1', 'Thornbridge', '500ml'),
    ('Thornbridge Bayern', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Thornbridge-Bayern-500ml.pptx.png?resize=600%2C600&ssl=1', 'Thornbridge', '500ml'),
    ('Thornbridge Jaipur', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Thornbridge-Jaipur-500ml.pptx.png?resize=600%2C600&ssl=1', 'Thornbridge', '500ml'),
    ('Thornbridge Lord Marples', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Thornbridge-Lord-Marples-500ml.pptx.png?resize=600%2C600&ssl=1', 'Thornbridge', '500ml'),
    ("Timothy Taylor's Landlord", 'R74.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Timothy-Taylors-500ml-ChatGPT.pptx.png?resize=600%2C600&ssl=1', "Timothy Taylor's", '500ml'),
]
make_page('cat-beers.html', 'Beers & Ales', '🍺', beers)

# ── HOT DRINKS ────────────────────────────────────────────────────────────────
hotdrinks = [
    ('Cadbury Hot Drinking Chocolate', 'R94.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/Cadbury-Drinking-Chocolate-250g.png?resize=600%2C600&ssl=1', 'Cadbury', '250g'),
    ('Cadbury Hot Drinking Chocolate', 'R139.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/Cadbury-Hot-Choc-500g.jpg?resize=600%2C600&ssl=1', 'Cadbury', '500g'),
    ('Caffeluxe Firenze Gourmet', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/Caffeluxe-Firenze-Gourmet.jpg?resize=600%2C600&ssl=1', 'Caffeluxe', '10 Capsule'),
    ('Caffeluxe Italiano Decaf', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/caffeluxe-italiano-Decaf-Snip.jpg?resize=600%2C600&ssl=1', 'Caffeluxe', '10 Capsule'),
    ('Caffeluxe Milano Espresso', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/Caffeluxe-Milano-Espresso.jpg?resize=600%2C600&ssl=1', 'Caffeluxe', '10 Capsule'),
    ('Caffeluxe Napoli Dark Roast', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/Caffeluxe-Napoli-Dark-Roast.jpg?resize=600%2C600&ssl=1', 'Caffeluxe', '10 Capsule'),
    ('Caffeluxe Roma Lungo', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/Caffeluxe-Roma-Lungo-2.jpg?resize=600%2C600&ssl=1', 'Caffeluxe', '10 Capsule'),
    ('Caffeluxe Venezia Ristretto', 'R48.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/03/bb-Caffeluxe-Venezia-Ristretto.pptx.png?resize=600%2C600&ssl=1', 'Caffeluxe', '10 Capsule'),
    ('Galaxy Hot Chocolate', 'R93.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/images-3.jpg?resize=600%2C600&ssl=1', 'Galaxy', '250g'),
    ('Horlicks "Original"', 'R169.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Horlicks-500g.jpg?resize=600%2C600&ssl=1', 'Horlicks', '400g'),
    ('Mars Maltesers Hot Chocolate', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/4481716042589.png?resize=600%2C600&ssl=1', 'Maltesers', '225g'),
    ('Options White Hot Chocolate Sachet', 'R19.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/white-choc.jpg?resize=600%2C600&ssl=1', 'Options', '11g'),
    ('Ovaltine', 'R174.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Ovaltine-300g.jpg?resize=600%2C600&ssl=1', 'Ovaltine', '300g'),
    ('Ovaltine Chocolate', 'R174.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/images-4.jpg?resize=600%2C600&ssl=1', 'Ovaltine', '300g'),
    ('Ovaltine Original Light', 'R174.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/09/Ovaltine-Original-Light-300g.png?resize=600%2C600&ssl=1', 'Ovaltine', '300g'),
    ('Ovaltine Original Malt Drink', 'R398.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/07/ovaltine.jpg?resize=600%2C600&ssl=1', 'Ovaltine', '800g'),
    ('PG Tips Original', 'R102.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-PG-Tips-40s-Original.pptx.png?resize=600%2C600&ssl=1', 'PG Tips', '40 Pyramid Teabags'),
    ('PG Tips Original', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/PG-Tips-80-Teabags.webp?resize=600%2C600&ssl=1', 'PG Tips', '80 Pyramid Teabags', 'Best seller'),
    ('Splenda Zero Calorie Sweetener', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/01/splenda-mini.webp?resize=600%2C600&ssl=1', 'Splenda', '100 Sweet Minis'),
    ('Taylors Yorkshire Tea', 'R299.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/bb-Taylors-Yorkshire-Tea-160s.pptx.png?resize=600%2C600&ssl=1', 'Taylors', '160 Teabags'),
    ('Taylors Yorkshire Tea', 'R102.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Taylors-Yorkshire-Tea-40s.pptx.png?resize=600%2C600&ssl=1', 'Taylors', '40 Teabags'),
    ('Taylors Yorkshire Tea', 'R187.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Taylors-Yorkshire-Tea-80s.pptx.png?resize=600%2C600&ssl=1', 'Taylors', '80 Teabags', 'Best seller'),
    ('Taylors Yorkshire Tea Biscuit Brew', 'R114.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Taylors-Yorksire-Tea-Biscuit-Brew-40s.pptx.png?resize=600%2C600&ssl=1', 'Taylors', '40 Teabags'),
    ('Taylors Yorkshire Tea Decaf', 'R189.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Taylors-Yorkshire-Tea-Decaf-80s.pptx.png?resize=600%2C600&ssl=1', 'Taylors', '80 Teabags'),
    ('Taylors Yorkshire Tea Decaf Bedtime Brew', 'R114.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/bb-Taylors-Yorksire-Tea-Bedtime-Decaf-40s.pptx.png?resize=600%2C600&ssl=1', 'Taylors', '40 Teabags'),
    ('Taylors Yorkshire Tea Gold', 'R199.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Taylors-Yorkshire-Tea-Gold-80s.pptx-2.png?resize=600%2C600&ssl=1', 'Taylors', '80 Teabags'),
    ('Taylors Yorkshire Tea Gold', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/bb-Taylors-Yorkshire-Tea-Gold-40s.pptx.png?resize=600%2C600&ssl=1', 'Taylors', '40 Teabags'),
    ('Tetley Decaf Tea', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/41E6YwbQOxL._SR600315_PIWhiteStripBottomLeft035_PIStarRatingFOURANDHALFBottomLeft360-6_SR600315_ZA409445290400400AmazonEmberBold124005_SCLZZZZZZZ_FMpng_BG255255255_preview_rev_1.png?resize=600%2C600&ssl=1', 'Tetley', '80 Teabags'),
    ('Tetley Original Tea', 'R155.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/07/tetley888_2_1024x_preview_rev_1.png?resize=600%2C600&ssl=1', 'Tetley', '80 Teabags'),
    ('Twinings Assam Loose Tea', 'R125.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/Twinings-Assam-Tea-Loose-125.jpg?resize=600%2C600&ssl=1', 'Twinings', '125g'),
    ('Twinings Assam Tea', 'R125.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Twinings-Assam-Tea-40-Teabags.jpg?resize=600%2C600&ssl=1', 'Twinings', '40 Teabags'),
    ('Twinings Buttermint', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/Buttermint_1600x1600_Compressed.jpg?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Camomile & Orange', 'R119.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/1-Twinings-Camomile-Orange-20-Tea-Bags_540x.webp?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Camomile & Honey', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Twinings-Camomile-Honey-20-Teabags.jpg?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Cherry & Cinnamon', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Twinings-Cherry-Cinnamon-20-Teabags.jpg?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Cranberry & Raspberry', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Twinings-Cranberry-Raspberry-20-Teabags.jpg?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Darjeeling', 'R125.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Twinings-Darjeeling-50-Teabags.jpg?resize=600%2C600&ssl=1', 'Twinings', '40 Teabags'),
    ('Twinings Decaffeinated Earl Grey', 'R155.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/earl-grey-decaf.jpg?resize=600%2C600&ssl=1', 'Twinings', '40 Teabags'),
    ('Twinings Distinctively Smoky', 'R125.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/01/Distinctively-Smoky-40-Tea-Bags-Front.webp?resize=600%2C600&ssl=1', 'Twinings', '40 Teabags'),
    ('Twinings Earl Grey Tea', 'R125.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/earl-grey.jpg?resize=600%2C600&ssl=1', 'Twinings', '40 Teabags'),
    ('Twinings English Breakfast', 'R236.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Twinings-English-Breakfast-80s.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '80 Teabags'),
    ('Twinings English Breakfast Decaf', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/10/download.png?resize=600%2C600&ssl=1', 'Twinings', '40 Teabags'),
    ('Twinings Everyday', 'R142.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Twinings-Everyday-80-Teabags.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '80 Teabags'),
    ('Twinings Jasmine Green Tea', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/0070177103071_1_512x512_20240903.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Jasmine Green Tea', 'R219.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/Jasmine_80_1600x1600_Compressed.webp?resize=600%2C600&ssl=1', 'Twinings', '80 Teabags'),
    ('Twinings Lady Grey', 'R236.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Twinings-Lady-Grey-80-Teabags.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '80 Teabags'),
    ('Twinings Lemon & Ginger', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Twinings-Lemon-Ginger-20-Teabags.jpg?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Peppermint', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Twinings-Peppermint-20-Teabags.jpg?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Pure Camomile', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/01/pure-cam.jpg?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Pure Camomile Tea', 'R219.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/08/Camomile_80_1600x1600_Compressed.jpg?resize=600%2C600&ssl=1', 'Twinings', '80 Teabags'),
    ('Twinings Pure Fennel', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/01/1-Twinings-Pure-Fennel-20-Single-Tea-Bags.webp?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Pure Peppermint', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Twinings-Pure-Peppermint-20-Teabags.jpg?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Soulful Blends Little Lift', 'R144.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Twinings-SB-Little-Lift.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Soulful Blends Pause', 'R144.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Twinings-SB-Pause.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Soulful Blends Peace', 'R144.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Twinings-SB-Peace.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Soulful Blends Quiet Mind', 'R144.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Twinings-SB-Quiet-Mind.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Soulful Blends Reset', 'R144.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Twinings-SB-Reset.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Spiced Ginger', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Twinings-Spiced-Ginger-20-Teabags.jpg?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Strawberry & Raspberry', 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Twinings-Strawberry-Raspberry-20-Teabags.jpg?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Strong English Breakfast', 'R259.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Twinings-Strong-English-Breakfast-80s.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '80 Teabags'),
    ('Twinings Superblends Calm', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Twinings-SB-Calm.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Superblends Detox', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Twinings-SB-Detox.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Superblends Digest', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Twinings-SB-Digest.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Superblends Focus', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Twinings-SB-Focus.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Superblends Glow Tea', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Twinings-SB-Glow.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Superblends Heart Warming', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Twinings-SB-Heart.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Superblends Immune Support', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Twinings-SB-Immune-Support.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Superblends Matcha', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Twinings-SB-Matcha.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Superblends Menopause', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/bb-Twinings-SB-Menopause-.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Superblends Metabolism', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Twinings-SB-Metabolism.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Superblends Sleep', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Twinings-SB-Sleep-.pptx.png?resize=600%2C600&ssl=1', 'Twinings', '20 Teabags'),
    ('Twinings Swiss Chocolate Drink', 'R219.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/twinings-swiss-350.jpg?resize=600%2C600&ssl=1', 'Twinings', '350g'),
]
make_page('cat-hotdrinks.html', 'Hot Drinks', '☕', hotdrinks)

# ── COLD DRINKS ───────────────────────────────────────────────────────────────
colddrinks = [
    ('7 Up Pink Lemonade Zero Sugar Can', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/pink-lemonade.jpg?resize=600%2C600&ssl=1', '7 Up', '330ml'),
    ("Barr's American Cream Soda", 'R22.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/Barr-Cream-Soda-330ml-1.jpg?resize=600%2C600&ssl=1', "Barr's", '330ml'),
    ("Barr's Bubble Gum", 'R22.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/barr-bubblegum-soda.webp?resize=600%2C600&ssl=1', "Barr's", '330ml'),
    ("Barr's Cherryade", 'R22.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/bb-Barr-Cherryade-330ml-.pptx.png?resize=600%2C600&ssl=1', "Barr's", '330ml'),
    ("Barr's Limeade Zero Sugar", 'R22.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/02/barr_limeade_330ml_59p.png?resize=600%2C600&ssl=1', "Barr's", '330ml'),
    ("Barr's Tizer", 'R22.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/330ml-tizer-can-plain.png?resize=600%2C600&ssl=1', "Barr's", '330ml'),
    ('Belvoir Elderflower & Rose Cordial', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Belvoir-Elderflower-Rose-Cordial-500ml.jpg?resize=600%2C600&ssl=1', 'Belvoir', '500ml'),
    ('Belvoir Elderflower Cordial', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Belvoir-Elderflower-Cordial-500ml.jpg?resize=600%2C600&ssl=1', 'Belvoir', '500ml', 'Premium'),
    ('Belvoir Ginger Cordial', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Belvoir-Ginger-Cordial-500ml.jpg?resize=600%2C600&ssl=1', 'Belvoir', '500ml'),
    ('Belvoir Lime & Yuzu Mojito', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Belvoir-Sparkling-Lime-Yuzu-Mojito-750ml.pptx.png?resize=600%2C600&ssl=1', 'Belvoir', '750ml'),
    ('Belvoir Lime Cordial', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/Belvoir-Lime-Cordial-500ml.jpg?resize=600%2C600&ssl=1', 'Belvoir', '500ml'),
    ('Belvoir Raspberry & Lemon Cordial', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Belvoir-Raspberry-Lemon-Cordial-500ml.pptx.png?resize=600%2C600&ssl=1', 'Belvoir', '500ml'),
    ('Belvoir Sicilian Lemon & Lime Cordial NAS', 'R109.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Belvoir-Sicilian-Lemon-Lime-Cordial-500ml.pptx.png?resize=600%2C600&ssl=1', 'Belvoir', '500ml'),
    ('Belvoir Sparkling Elderflower', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Belvoir-Sparkling-Elderflower-275ml.pptx.png?resize=600%2C600&ssl=1', 'Belvoir', '275ml'),
    ('Belvoir Sparkling Elderflower', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Belvoir-Sparkling-Elderflower-750ml.pptx.png?resize=600%2C600&ssl=1', 'Belvoir', '750ml'),
    ('Belvoir Sparkling Elderflower & Rose', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Belvoir-Sparkling-Elderflower-Rose-275ml.pptx.png?resize=600%2C600&ssl=1', 'Belvoir', '275ml'),
    ('Belvoir Sparkling Elderflower & Rose', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Belvoir-Sparkling-Elderflower-Rose-750ml.pptx.png?resize=600%2C600&ssl=1', 'Belvoir', '750ml'),
    ('Belvoir Sparkling Ginger Beer', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Belvoir-Ginger-Beer-275ml.pptx.png?resize=600%2C600&ssl=1', 'Belvoir', '275ml'),
    ('Belvoir Sparkling Ginger Beer', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Belvoir-Sparkling-Ginger-Beer-750ml.pptx.png?resize=600%2C600&ssl=1', 'Belvoir', '750ml'),
    ('Belvoir Sparkling Peach Bellini', 'R61.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Belvoir-Sparkling-Peach-Bellini-750ml.pptx.png?resize=600%2C600&ssl=1', 'Belvoir', '750ml'),
    ('Belvoir Sparkling Raspberry Lemonade', 'R29.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/02/bb-Belvoir-Sparkling-Raspberry-Lemonade-275ml.pptx.png?resize=600%2C600&ssl=1', 'Belvoir', '275ml'),
    ('Ben Shaws Bitter Shandy', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Ben-Shaws-Bitter-Shandy-330ml.jpg?resize=600%2C600&ssl=1', 'Ben Shaws', '330ml'),
    ('Ben Shaws Cloudy Lemonade', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Ben-Shaws-Cloudy-Lemonade-330ml.jpg?resize=600%2C600&ssl=1', 'Ben Shaws', '330ml'),
    ('Ben Shaws Cream Soda', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Ben-Shaws-Cream-Soda-330ml.jpg?resize=600%2C600&ssl=1', 'Ben Shaws', '330ml'),
    ('Ben Shaws Dandelion & Burdock', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Ben-Shaws-Dandelion-Burdock-330ml.jpg?resize=600%2C600&ssl=1', 'Ben Shaws', '330ml'),
    ('Cherry Coke', 'R26.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/Cherry-Coke-330ml.jpg?resize=600%2C600&ssl=1', 'Coca-Cola', '330ml'),
    ('Coke Lemon', 'R26.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/10/lemon-coke.png?resize=600%2C600&ssl=1', 'Coca-Cola', '330ml'),
    ('Coke Lime', 'R26.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/05/5017726447151.jpg?resize=600%2C600&ssl=1', 'Coca-Cola', '330ml'),
    ('Dr Pepper', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/dr-pepper.webp?resize=600%2C600&ssl=1', 'Dr Pepper', '330ml'),
    ('Dr Pepper Zero', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/dr-pepper-zero.jpg?resize=600%2C600&ssl=1', 'Dr Pepper', '330ml'),
    ('Dr Pepper Zero Cherry Crush', 'R22.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/04/bb-Dr-Pepper-Zero-Cherry-Crush-330ml.pptx.png?resize=600%2C600&ssl=1', 'Dr Pepper', '330ml'),
    ('Fanta Fruit Twist', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Fanta-Fruit-Twist-330ml.jpg?resize=600%2C600&ssl=1', 'Fanta', '330ml'),
    ('Fanta Lemon', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Fanta-Lemon-330.jpg?resize=600%2C600&ssl=1', 'Fanta', '330ml'),
    ('Fanta Orange', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/fanta-orange-330ml.jpg?resize=600%2C600&ssl=1', 'Fanta', '330ml'),
    ('Fanta Pineapple & Grapefruit', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/04/fanta-pineapple-grapefruit-330-ml-englische-suesswaren-guenstig-kaufen-1.webp?resize=600%2C600&ssl=1', 'Fanta', '330ml'),
    ('Highland Spring Still Water', 'R24.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/highland-spring-water.jpg?resize=600%2C600&ssl=1', 'Highland Spring', '750ml'),
    ('Irn Bru', 'R49.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/irnbru2L.jpeg?resize=600%2C600&ssl=1', 'Irn Bru', '2L'),
    ('Irn Bru', 'R22.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Irn-Bru-330ml.jpg?resize=600%2C600&ssl=1', 'Irn Bru', '330ml'),
    ('Irn Bru Sugar Free', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/11/irn-bru-sugar-free-2L-1.jpg?resize=600%2C600&ssl=1', 'Irn Bru', '2L Sugar Free'),
    ('Irn Bru Xtra', 'R74.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/irnbruxtra2L.webp?resize=600%2C600&ssl=1', 'Irn Bru', '2L Xtra'),
    ('Irn Bru Xtra', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/09/bcf73cae-b81c-45cf-8c22-01df9e7ef9ef.png?resize=600%2C600&ssl=1', 'Irn Bru', '330ml Xtra'),
    ('Levi Roots Caribbean Crush Can', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/caribbean.jpg?resize=600%2C600&ssl=1', 'Levi Roots', '330ml'),
    ('Nestle Nesquik Banana Powder', 'R129.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/nesquik-banana.webp?resize=600%2C600&ssl=1', 'Nesquik', '300g'),
    ('Nestle Nesquik Chocolate Powder', 'R129.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/06/nesquikchoc.webp?resize=600%2C600&ssl=1', 'Nesquik', '300g'),
    ('Nestle Nesquik Strawberry Powder', 'R129.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/nesquik-straw.jpg?resize=600%2C600&ssl=1', 'Nesquik', '300g'),
    ('Old Jamaica Ginger Beer', 'R25.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Old-Jamaica-Ginger-Beer-330ml-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Old Jamaica', '330ml'),
    ('Pepsi Cream Soda Zero Sugar', 'R19.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/adwhjubckzmc877tgxkp.jpg?resize=600%2C600&ssl=1', 'Pepsi', '330ml'),
    ('Pepsi Max Cherry', 'R7.50', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/cherry-max.jpg?resize=600%2C600&ssl=1', 'Pepsi', '330ml'),
    ('Pepsi Strawberries & Cream Zero Sugar', 'R19.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/pepsi-pepsi-strawberries-cream-330ml.webp?resize=600%2C600&ssl=1', 'Pepsi', '330ml'),
    ('Quick Milk Birthday Cake', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/11/quickmilkbday.jpg?resize=600%2C600&ssl=1', 'Quick Milk', '13pc'),
    ('Quick Milk Chocolate', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/03/36_723c06e8-5464-45fb-9109-0c1228c7cac7.webp?resize=600%2C600&ssl=1', 'Quick Milk', '13pc'),
    ('Quick Milk Strawberry', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/03/37_46404a28-7620-475f-9d39-d356359c867b.webp?resize=600%2C600&ssl=1', 'Quick Milk', '13pc'),
    ('Quick Milk Strawberry, Banana & Forest Fruit', 'R44.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/11/QuickMilkLuckyBoxStrawberry_Banana_ForestFruit78gmGLAMSHOW.webp?resize=600%2C600&ssl=1', 'Quick Milk', '13pc'),
    ('Ribena Blackcurrant Carton', 'R12.50', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ribena-Blackcurrant-RTD-Carton-250mlChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Ribena', '250ml'),
    ('Ribena Blackcurrant Cordial', 'R133.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Ribena-Blackcurrant-Cordial-850ml-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Ribena', '850ml'),
    ('Ribena Strawberry Carton', 'R12.50', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/04/ribena-straw-carton.pptx.jpg?resize=600%2C600&ssl=1', 'Ribena', '250ml'),
    ('Robinsons Real Fruit & Barley Summer Fruits Cordial', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/bb-Robinsons-Summer-Fruits-FB-1L-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Robinsons', '1L'),
    ('Robinsons Real Fruit & Barley Orange Cordial', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Robinsons-Orange-FB-1L-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Robinsons', '1L'),
    ('Robinsons Real Fruit Apple & Blackcurrant Cordial', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Robinsons-Apple-Blackcurrant-1L-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Robinsons', '1L'),
    ('Robinsons Real Fruit Lemon Cordial', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Robinsons-Lemon-1L-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Robinsons', '1L'),
    ('Robinsons Real Fruit Orange Cordial', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/bb-Robinsons-Orange-Cordial-1L-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Robinsons', '1L'),
    ('Robinsons Real Fruit Pink Grapefruit Cordial', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Robinsons-Pink-Grapefruit-FB-Cordial-1L-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Robinsons', '1L'),
    ('Robinsons Real Fruit Summer Fruits Cordial', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Robinsons-Summer-Fruits-Cordial-1L-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Robinsons', '1L'),
    ('Robinsons Summer Fruit NAS Double Strength Cordial', 'R89.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/bb-Robinsons-Summer-Fruits-DC-1L-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Robinsons', '750ml'),
    ('Vimto Fizzy', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Vimto-Original-330ml-.pptx.png?resize=600%2C600&ssl=1', 'Vimto', '330ml'),
    ('Vimto Fizzy Zero', 'R21.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/bb-Vimto-Zero-330ml-.pptx-1.png?resize=600%2C600&ssl=1', 'Vimto', '330ml'),
    ('Vimto Real Fruit Squash', 'R119.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/Vimto-Real-Fruit-Squash-2Lt.jpg?resize=600%2C600&ssl=1', 'Vimto', '2L'),
    ('Vimto Real Fruit Squash Cordial', 'R66.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/Vimto-Real-Fruit-Squash-2Lt.jpg?resize=600%2C600&ssl=1', 'Vimto', '725ml'),
    ('Vimto Real Fruit Squash Cordial NAS', 'R66.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/03/bb-Vimto-Real-Fruit-Squash-Cordial-NAS-725ml-ChatGPT.pptx.png?resize=600%2C600&ssl=1', 'Vimto', '725ml'),
    ('Volvic Mineral Water', 'R34.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Volvic-Mineral-Water-Screw-Cap-1Lt-2.jpg?resize=600%2C600&ssl=1', 'Volvic', '1L'),
    ('Volvic Mineral Water', 'R18.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/09/Volvic-Mineral-Water-500-ml.jpg?resize=600%2C600&ssl=1', 'Volvic', '500ml'),
    ('Voss Plus Still Water', 'R23.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/voss-plus.jpg?resize=600%2C600&ssl=1', 'Voss', '500ml'),
    ('Voss Sparkling Lemon Cucumber Flavoured Water', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Voss-Sprk-Lem-Cuc-Gl-375ml.jpg?resize=600%2C600&ssl=1', 'Voss', '375ml'),
    ('Voss Sparkling Lime Mint Flavoured Water', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Voss-Sprk-Lime-Mint-Gl-375ml.jpg?resize=600%2C600&ssl=1', 'Voss', '375ml'),
    ('Voss Sparkling Tangerine Lemongrass Flavoured Water', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Voss-Sprk-Tang-Lgra-Gl-375ml.jpg?resize=600%2C600&ssl=1', 'Voss', '375ml'),
    ('Voss Sparkling Water', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Voss-Sprk-Water-375-ml-Gl.jpg?resize=600%2C600&ssl=1', 'Voss', '375ml'),
    ('Voss Sparkling Water', 'R76.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Voss-Sprk-Water-800-ml-Gl.jpg?resize=600%2C600&ssl=1', 'Voss', '800ml'),
    ('Voss Still Water', 'R36.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Voss-Still-Water-375-ml-Gl.jpg?resize=600%2C600&ssl=1', 'Voss', '375ml'),
    ('Voss Still Water', 'R76.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Voss-StillWater-800-ml-Gl.jpg?resize=600%2C600&ssl=1', 'Voss', '800ml'),
]
make_page('cat-colddrinks.html', 'Cold Drinks', '🥤', colddrinks)

# ── CEREALS ───────────────────────────────────────────────────────────────────
cereals = [
    ('Jordans Country Crisp Chunky Nuts', 'R169.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/01/Jordans-Country-Crisp-Crunchy-Nut-450g.webp?resize=600%2C600&ssl=1', 'Jordans', '450g'),
    ('Jordans Country Crisp with Crunchy Chunky Nuts', 'R119.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/jordans-400g.jpg?resize=600%2C600&ssl=1', 'Jordans', '450g'),
    ("Kellogg's All Bran Original", 'R99.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/allbranoriginal.png?resize=600%2C600&ssl=1', "Kellogg's", '500g'),
    ("Kellogg's Coco Pops Bars", 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Kelloggs-Coco-Pops-Bars-6x20g.jpg?resize=600%2C600&ssl=1', "Kellogg's", '6 Bars x 20g'),
    ("Kellogg's Crunchy Nut Cornflakes", 'R159.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/11/Kelloggs-C-Nut-500g.jpg?resize=600%2C600&ssl=1', "Kellogg's", '460g'),
    ("Kellogg's Frosties", 'R159.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Kelloggs-Frosties-500.jpg?resize=600%2C600&ssl=1', "Kellogg's", '470g'),
    ("Kellogg's Frosties Bars", 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Kelloggs-Frosties-Bars-6x25g.jpg?resize=600%2C600&ssl=1', "Kellogg's", '6 x 25g'),
    ("Kellogg's Fruit 'n Fibre", 'R156.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/fruit-n-Fibre.png?resize=600%2C600&ssl=1', "Kellogg's", '500g'),
    ("Kellogg's Oaties Original Crunch", 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/oaties.png?resize=600%2C600&ssl=1', "Kellogg's", '500g'),
    ("Kellogg's Pop Tarts Chocotastic", 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Kelloggs-Poptarts-Choc-8pk-2.jpg?resize=600%2C600&ssl=1', "Kellogg's", '8pk'),
    ("Kellogg's Pop Tarts Hot Fudge Sundae", 'R25.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/01/hot-fudge.webp?resize=600%2C600&ssl=1', "Kellogg's", '8pk'),
    ("Kellogg's Pop Tarts Strawberry Sensation", 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Kelloggs-Poptarts-Strawberry-8pk-2.jpg?resize=600%2C600&ssl=1', "Kellogg's", '8pk'),
    ("Kellogg's Rice Krispies", 'R129.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/rice340g.png?resize=600%2C600&ssl=1', "Kellogg's", '310g'),
    ("Kellogg's Rice Krispies Bars", 'R59.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/11/Kelloggs-Rice-Crispies-Bars-6x20g.jpg?resize=600%2C600&ssl=1', "Kellogg's", '6 x 20g'),
    ("Kellogg's Rice Krispies Squares Chewy-Tastic Marshmallow", 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/Rice-Krispies-Marsh-Squares-4-x-36g.jpg?resize=600%2C600&ssl=1', "Kellogg's", '4x28g'),
    ("Kellogg's Rice Krispies Squares Totally Chocolatey", 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/04/Rice-Krispies-Choc-Squares-4-x-36g.jpg?resize=600%2C600&ssl=1', "Kellogg's", '4x36g'),
    ("Kellogg's Special K Red Berries", 'R179.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/09/specialkredberries.png?resize=600%2C600&ssl=1', "Kellogg's", '330g'),
    ("Kellogg's Variety Pack", 'R139.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Kelloggs-Variety-Pack-8pk.jpg?resize=600%2C600&ssl=1', "Kellogg's", '8pk'),
    ("Kellogg's Rice Krispies Squares Caramel & Chocolate", 'R67.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/11/1.png?resize=600%2C600&ssl=1', "Kellogg's", '4 x 36g'),
    ('Nestle Choco Crunch Nesquik Cereal', 'R159.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2026/03/bb-Nestle-Nesquik-Cereal-375g.pptx.png?resize=600%2C600&ssl=1', 'Nestle', '375g'),
    ('Nestle Cookie Crisp', 'R119.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/05/COOKIECRISP500G.png?resize=600%2C600&ssl=1', 'Nestle', '375g'),
    ('Nestle Curiously Cinnamon', 'R134.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Nestle-Curious-Cinnamon-375g.jpg?resize=600%2C600&ssl=1', 'Nestle', '375g'),
    ('Nestle Curiously Cinnamon Churros', 'R159.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/07/Nestle-Churros-360g.jpg?resize=600%2C600&ssl=1', 'Nestle', '360g'),
    ('Nestle KitKat Cereal', 'R55.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/06/cerealbox_3x_0.webp?resize=600%2C600&ssl=1', 'Nestle', '330g'),
    ('Nestle Shredded Wheat', 'R139.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/10/Nestle-Shredded-Wheat-16.jpg?resize=600%2C600&ssl=1', 'Nestle', "16's"),
    ('Nestle Shredded Wheat', 'R189.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2020/11/Nestle-Shredded-Wheat-30.jpg?resize=600%2C600&ssl=1', 'Nestle', "30's"),
    ('Nestle Shredded Wheat Bitesize', 'R189.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2023/04/1-2.webp?resize=600%2C600&ssl=1', 'Nestle', '720g'),
    ('Nestle Shreddies', 'R144.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/02/GYMSUPPLEMENTS.CO_.UK_9_0e6211c7-0ee8-4247-af89-6ed507dddf7b_preview_rev_1.png?resize=600%2C600&ssl=1', 'Nestle', '460g'),
    ('Nestle Shreddies Frosted', 'R119.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/09/shreddiesfrosted.webp?resize=600%2C600&ssl=1', 'Nestle', '500g'),
    ('Nestle Shreddies Honey', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/10/honey-shreddies.jpg?resize=600%2C600&ssl=1', 'Nestle', '460g'),
    ("Oreo O's", 'R213.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2022/09/OreoFeature.jpg-701x394-1.png?resize=600%2C600&ssl=1', 'Oreo', '350g'),
    ('Quaker Porridge Oats', 'R139.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/03/quaker-porridge-oats-new.jpg?resize=600%2C600&ssl=1', 'Quaker', '1kg'),
    ('Ready Brek Cereal', 'R114.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/09/ready-brek.jpg?resize=600%2C600&ssl=1', 'Ready Brek', '450g'),
    ("Scott's Oats", 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/01/Scotts-Oats-1kg.jpg?resize=600%2C600&ssl=1', "Scott's", '1kg'),
    ('Weetabix', 'R97.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2025/06/weetabix.jpg?resize=600%2C600&ssl=1', 'Weetabix', '12pc'),
]
make_page('cat-cereals.html', 'Cereals & Breakfast', '🥣', cereals)

# ── KENT HAIRBRUSHES ──────────────────────────────────────────────────────────
kent = [
    ('10 Pronged Afro Style Comb', 'R79.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-spc86.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'SPC86'),
    ('40mm Small Radial Brush', 'R199.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-pf08.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'PF08'),
    ('Airhedz Maxi-Phat De-Tangle Brush', 'R179.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-pf19.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'PF19'),
    ('Airhedz Maxi-Phine Taming Brush', 'R179.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-pf18.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'PF18'),
    ('Large Beech Wood Quill WoodyHog Brush', 'R209.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-woodyhog.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'KBWOODYHOG', 'Handmade'),
    ('Large Rubber Cushion Brush', 'R244.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-pf07.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'PF07'),
    ('Large Rubber Pad Brush', 'R189.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-pf01.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'PF01'),
    ('Large Synthetic Shaving Brush — Ivory White', 'R359.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/BK8S-scaled.jpg?resize=600%2C600&ssl=1', 'Kent', 'BK8S'),
    ('Medium Bristle Cushion Graphite Brush — White', 'R249.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-ah13w.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'AH13W'),
    ('Medium Phine Pins Cushion Graphite Brush — Black', 'R199.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-ah9g.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'AH9G'),
    ('Medium Synthetic Shaving Brush — Black', 'R359.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/BLK4S-scaled.jpg?resize=600%2C600&ssl=1', 'Kent', 'BLK4S'),
    ('Medium Synthetic Shaving Brush — Ivory White', 'R349.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/BK4S-scaled.jpg?resize=600%2C600&ssl=1', 'Kent', 'BK4S'),
    ('Mini WoodyHog Brush', 'R179.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-mini-woody.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'KBMINIW/HOG'),
    ('Small Handbag Brush', 'R155.00', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-pf10.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'PF10'),
    ('Small Phine Pins Cushion Graphite Brush — Black', 'R149.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-ah11g.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'AH11G'),
    ('Small Radial Brush', 'R199.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2021/02/kent-pf04.pptx.jpg?resize=600%2C600&ssl=1', 'Kent', 'PF04'),
    ('Airhedz AH6W Brush', 'R219.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/kent-ah6w-airhedz.jpg?resize=600%2C600&ssl=1', 'Kent', 'AH6W'),
    ('KS50 Brush', 'R199.90', 'https://i0.wp.com/www.uke.co.za/wp-content/uploads/2024/08/kent-ks50.jpg?resize=600%2C600&ssl=1', 'Kent', 'KS50'),
]
make_page('cat-kent.html', 'Kent Hairbrushes', '💈', kent)

print('All category pages generated successfully.')
