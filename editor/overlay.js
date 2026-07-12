/*
 * TT8 Live Editor — overlay.js
 * One editing layer, two modes. What the client approves in "demo" is exactly
 * what ships in "live" — only the Publish target changes.
 *
 *   mode: "demo"  -> Publish saves to the browser (localStorage). No backend.
 *                    Auto-applies saved edits on load and shows an "Edit this
 *                    page" launcher. Perfect for client walkthroughs.
 *   mode: "live"  -> Publish POSTs to the serverless API, which commits to
 *                    GitHub and auto-deploys to Hostinger. Activated by the
 *                    admin app, which also calls setToken().
 *
 * It only ever touches elements marked [data-tt8-edit]. Everything else on the
 * page is untouchable — that boundary is the whole security model.
 */
(function () {
  "use strict";

  var config = { mode: "live", siteId: null, page: null, publishUrl: null, token: null, storageKey: null };
  var pristine = {};       // id -> true original from the page (text string, or {src, alt})
  var pristineDone = false;
  var originals = {};      // baseline for the dirty check
  var current = {};        // live text values while editing
  var pendingImages = {};  // id -> { name, dataUrl, alt }
  var active = false;
  var bar = null;
  var launcher = null;

  function configure(opts) {
    Object.assign(config, opts || {});
    if (config.mode === "demo") ready(function () { capturePristine(); applySaved(); injectLauncher(); });
  }
  function setToken(t) { config.token = t; }

  function ready(fn) { document.readyState !== "loading" ? fn() : document.addEventListener("DOMContentLoaded", fn); }
  function nodes() { return Array.prototype.slice.call(document.querySelectorAll("[data-tt8-edit]")); }
  function isImg(el) { return el.tagName === "IMG"; }
  function isRich(el) { return el.hasAttribute("data-tt8-rich"); }
  function readText(el) { return (isRich(el) ? el.innerHTML : el.innerText).trim(); }

  // ---- pristine + demo persistence ---------------------------------------
  function capturePristine() {
    if (pristineDone) return;
    nodes().forEach(function (el) {
      var id = el.getAttribute("data-tt8-edit");
      pristine[id] = isImg(el) ? { src: el.getAttribute("src"), alt: el.getAttribute("alt") || "" } : readText(el);
    });
    pristineDone = true;
  }
  function storageKey() { return config.storageKey || ("tt8-demo:" + (config.siteId || "site") + ":" + (config.page || "page")); }
  function readSaved() { try { return JSON.parse(localStorage.getItem(storageKey())) || { text: {}, images: {} }; } catch (e) { return { text: {}, images: {} }; } }
  function writeSaved(d) { try { localStorage.setItem(storageKey(), JSON.stringify(d)); return true; } catch (e) { return false; } }

  function applySaved() {
    var saved = readSaved();
    Object.keys(saved.text || {}).forEach(function (id) {
      var el = document.querySelector('[data-tt8-edit="' + id + '"]');
      if (el && !isImg(el)) isRich(el) ? (el.innerHTML = saved.text[id]) : (el.textContent = saved.text[id]);
    });
    Object.keys(saved.images || {}).forEach(function (id) {
      var el = document.querySelector('img[data-tt8-edit="' + id + '"]');
      if (!el) return;
      if (saved.images[id].src) el.setAttribute("src", saved.images[id].src);
      if (saved.images[id].alt != null) el.setAttribute("alt", saved.images[id].alt);
    });
  }

  // ---- styles -------------------------------------------------------------
  function injectStyles() {
    if (document.getElementById("tt8-editor-styles")) return;
    var css = `
      .tt8-editable{outline:1px dashed transparent;outline-offset:3px;transition:outline-color .12s;cursor:text}
      .tt8-editable:hover{outline-color:#c8842f}
      .tt8-editable:focus{outline:2px solid #c8842f}
      .tt8-dirty{outline-color:#c8842f !important}
      img.tt8-editable{cursor:pointer}
      .tt8-img-wrap{position:relative;display:inline-block}
      .tt8-img-bar{position:absolute;top:8px;left:8px;display:none;gap:6px;z-index:2147483000}
      .tt8-img-bar button{font:500 12px/1 ui-sans-serif,system-ui,sans-serif;padding:6px 10px;border:0;border-radius:999px;background:#12181f;color:#fff;cursor:pointer}
      .tt8-launcher{position:fixed;right:20px;bottom:20px;z-index:2147483600;display:flex;align-items:center;gap:8px;padding:12px 18px;border:0;border-radius:999px;background:#12181f;color:#fff;font:500 14px/1 ui-sans-serif,system-ui,sans-serif;cursor:pointer;box-shadow:0 6px 20px rgba(0,0,0,.25)}
      .tt8-launcher span{color:#c8842f}
      .tt8-bar{position:fixed;top:0;left:0;right:0;z-index:2147483600;display:flex;align-items:center;gap:14px;padding:10px 18px;background:#12181f;color:#fff;font:400 14px/1.4 ui-sans-serif,system-ui,sans-serif}
      .tt8-bar strong{font-weight:600}
      .tt8-bar .tt8-tag{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:#c8842f;border:1px solid rgba(200,132,47,.5);padding:2px 8px;border-radius:999px}
      .tt8-bar .tt8-count{color:#c8842f}
      .tt8-bar .tt8-spacer{flex:1}
      .tt8-bar button{font:500 13px/1 inherit;padding:8px 16px;border-radius:999px;border:0;cursor:pointer}
      .tt8-btn-primary{background:#c8842f;color:#12181f}
      .tt8-btn-primary[disabled]{opacity:.5;cursor:default}
      .tt8-btn-ghost{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.35) !important}
      body.tt8-editing{padding-top:46px}
      .tt8-toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);z-index:2147483600;max-width:88vw;text-align:center;padding:12px 18px;border-radius:10px;color:#fff;font:400 14px ui-sans-serif,system-ui,sans-serif}
      .tt8-toast-ok{background:#1d7a52}.tt8-toast-err{background:#a32d2d}
    `;
    var el = document.createElement("style");
    el.id = "tt8-editor-styles";
    el.textContent = css;
    document.head.appendChild(el);
  }

  // ---- launcher (demo only) ----------------------------------------------
  function injectLauncher() {
    if (launcher || active) return;
    injectStyles();
    launcher = document.createElement("button");
    launcher.className = "tt8-launcher";
    launcher.type = "button";
    launcher.innerHTML = '<span>&#9998;</span> Edit this page';
    launcher.addEventListener("click", activate);
    document.body.appendChild(launcher);
  }
  function removeLauncher() { if (launcher) { launcher.remove(); launcher = null; } }

  // ---- wiring -------------------------------------------------------------
  function markDirty(id, el) { current[id] !== originals[id] ? el.classList.add("tt8-dirty") : el.classList.remove("tt8-dirty"); refreshBar(); }
  function dirtyCount() {
    var n = 0, id;
    for (id in current) if (current[id] !== originals[id]) n++;
    for (id in pendingImages) n++;
    return n;
  }

  function wireText(el, id) {
    originals[id] = readText(el);
    current[id] = originals[id];
    el.classList.add("tt8-editable");
    el.setAttribute("contenteditable", isRich(el) ? "true" : "plaintext-only");
    el.addEventListener("input", function () { current[id] = readText(el); markDirty(id, el); });
  }

  function wireImage(el, id) {
    el.classList.add("tt8-editable");
    var wrap = document.createElement("span");
    wrap.className = "tt8-img-wrap";
    el.parentNode.insertBefore(wrap, el);
    wrap.appendChild(el);
    var barEl = document.createElement("div");
    barEl.className = "tt8-img-bar";
    barEl.innerHTML = '<button type="button" data-act="replace">Replace</button><button type="button" data-act="alt">Alt text</button>';
    wrap.appendChild(barEl);
    wrap.addEventListener("mouseenter", function () { barEl.style.display = "flex"; });
    wrap.addEventListener("mouseleave", function () { barEl.style.display = "none"; });
    var file = document.createElement("input");
    file.type = "file"; file.accept = "image/*"; file.style.display = "none";
    wrap.appendChild(file);
    barEl.querySelector('[data-act="replace"]').addEventListener("click", function () { file.click(); });
    barEl.querySelector('[data-act="alt"]').addEventListener("click", function () {
      var next = window.prompt("Describe the image (alt text):", (pendingImages[id] && pendingImages[id].alt) != null ? pendingImages[id].alt : (pristine[id] ? pristine[id].alt : ""));
      if (next === null) return;
      pendingImages[id] = Object.assign({}, pendingImages[id], { alt: next });
      el.setAttribute("alt", next); el.classList.add("tt8-dirty"); refreshBar();
    });
    file.addEventListener("change", function () {
      var f = file.files[0]; if (!f) return;
      var reader = new FileReader();
      reader.onload = function () {
        el.setAttribute("src", reader.result);
        pendingImages[id] = Object.assign({ alt: (pristine[id] ? pristine[id].alt : "") }, pendingImages[id], { name: f.name, dataUrl: reader.result });
        el.classList.add("tt8-dirty"); refreshBar();
      };
      reader.readAsDataURL(f);
    });
  }

  // ---- toolbar ------------------------------------------------------------
  function buildBar() {
    var demo = config.mode === "demo";
    bar = document.createElement("div");
    bar.className = "tt8-bar";
    bar.innerHTML =
      '<strong>TT8 Live Editor</strong>' +
      (demo ? '<span class="tt8-tag">Demo</span>' : '') +
      '<span>Editing <span class="tt8-page"></span></span>' +
      '<span class="tt8-count"></span>' +
      '<span class="tt8-spacer"></span>' +
      (demo ? '<button type="button" class="tt8-btn-ghost tt8-reset">Reset</button>' : '') +
      '<button type="button" class="tt8-btn-ghost tt8-exit">' + (demo ? 'Done' : 'Discard') + '</button>' +
      '<button type="button" class="tt8-btn-primary tt8-publish">Publish</button>';
    document.body.appendChild(bar);
    bar.querySelector(".tt8-page").textContent = config.page || "this page";
    bar.querySelector(".tt8-publish").addEventListener("click", demo ? publishDemo : publishLive);
    bar.querySelector(".tt8-exit").addEventListener("click", function () { location.reload(); });
    if (demo) bar.querySelector(".tt8-reset").addEventListener("click", resetDemo);
    refreshBar();
  }
  function refreshBar() {
    if (!bar) return;
    var n = dirtyCount();
    bar.querySelector(".tt8-count").textContent = n ? n + " unsaved change" + (n === 1 ? "" : "s") : "No changes yet";
    bar.querySelector(".tt8-publish").disabled = n === 0;
  }
  function toast(msg, ok) {
    var t = document.createElement("div");
    t.className = "tt8-toast " + (ok ? "tt8-toast-ok" : "tt8-toast-err");
    t.textContent = msg; document.body.appendChild(t);
    setTimeout(function () { t.remove(); }, ok ? 3600 : 6000);
  }

  // ---- publish: demo ------------------------------------------------------
  function publishDemo() {
    var data = { text: {}, images: {} };
    nodes().forEach(function (el) {
      var id = el.getAttribute("data-tt8-edit");
      if (isImg(el)) {
        var src = el.getAttribute("src"), alt = el.getAttribute("alt") || "";
        if (src !== pristine[id].src || alt !== (pristine[id].alt || "")) data.images[id] = { src: src, alt: alt };
      } else {
        var val = readText(el);
        if (val !== pristine[id]) data.text[id] = val;
      }
    });
    if (!writeSaved(data)) { toast("That image is a little large for the preview — try a smaller one.", false); return; }
    originals = {}; nodes().forEach(function (el) { if (!isImg(el)) originals[el.getAttribute("data-tt8-edit")] = readText(el); });
    current = Object.assign({}, originals); pendingImages = {};
    document.querySelectorAll(".tt8-dirty").forEach(function (n) { n.classList.remove("tt8-dirty"); });
    refreshBar();
    toast("Published to your preview. Reload the page and your changes are still here.", true);
  }
  function resetDemo() {
    try { localStorage.removeItem(storageKey()); } catch (e) {}
    location.reload();
  }

  // ---- publish: live ------------------------------------------------------
  function buildPayload() {
    var text = {}, id;
    for (id in current) if (current[id] !== originals[id]) text[id] = current[id];
    return { siteId: config.siteId, page: config.page, text: text, images: pendingImages };
  }
  function publishLive() {
    var btn = bar.querySelector(".tt8-publish");
    btn.disabled = true; btn.textContent = "Publishing…";
    fetch(config.publishUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Authorization": "Bearer " + (config.token || "") },
      body: JSON.stringify(buildPayload())
    })
      .then(function (r) { return r.json().then(function (b) { return { ok: r.ok, body: b }; }); })
      .then(function (res) {
        btn.textContent = "Publish";
        if (!res.ok) { toast(res.body.error || "Publish failed.", false); refreshBar(); return; }
        var id; for (id in current) originals[id] = current[id];
        pendingImages = {};
        document.querySelectorAll(".tt8-dirty").forEach(function (n) { n.classList.remove("tt8-dirty"); });
        refreshBar();
        toast("Published. Your site is updating now.", true);
      })
      .catch(function () { btn.textContent = "Publish"; toast("Network error — nothing was published.", false); refreshBar(); });
  }

  // ---- activation ---------------------------------------------------------
  function activate() {
    if (active) return;
    active = true;
    removeLauncher();
    injectStyles();
    capturePristine();
    document.body.classList.add("tt8-editing");
    nodes().forEach(function (el) {
      var id = el.getAttribute("data-tt8-edit");
      isImg(el) ? wireImage(el, id) : wireText(el, id);
    });
    buildBar();
  }

  window.TT8Editor = { configure: configure, setToken: setToken, activate: activate };
})();
