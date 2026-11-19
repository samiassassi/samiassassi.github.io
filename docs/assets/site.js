(function () {
  "use strict";
  var root = document.documentElement, body = document.body;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* theme */
  var themeBtn = $(".theme-btn");
  if (themeBtn) themeBtn.addEventListener("click", function () {
    var cur = root.getAttribute("data-theme");
    if (!cur) cur = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    var next = cur === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("sa-theme", next); } catch (e) {}
  });

  /* mobile menu */
  var menuBtn = $(".menu-btn");
  if (menuBtn) {
    menuBtn.addEventListener("click", function () {
      var open = body.classList.toggle("nav-open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    $$(".nav a").forEach(function (a) { a.addEventListener("click", function () { body.classList.remove("nav-open"); menuBtn.setAttribute("aria-expanded", "false"); }); });
  }

  /* toast */
  var toastEl = $(".toast"), toastT;
  function toast(msg) {
    if (!toastEl) return;
    toastEl.textContent = msg; toastEl.classList.add("show");
    clearTimeout(toastT); toastT = setTimeout(function () { toastEl.classList.remove("show"); }, 1800);
  }

  /* value-chain explorer (tabs) */
  $$(".chain").forEach(function (ch) {
    var tabs = $$(".node", ch);
    function select(i, focus) {
      tabs.forEach(function (t, j) {
        var on = i === j;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
        var p = document.getElementById(t.getAttribute("aria-controls"));
        if (p) p.hidden = !on;
      });
      if (focus) tabs[i].focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(i); });
      t.addEventListener("keydown", function (ev) {
        var rtl = root.dir === "rtl", n = tabs.length, k = ev.key;
        var fwd = rtl ? "ArrowLeft" : "ArrowRight", back = rtl ? "ArrowRight" : "ArrowLeft";
        if (k === fwd) { ev.preventDefault(); select((i + 1) % n, true); }
        else if (k === back) { ev.preventDefault(); select((i - 1 + n) % n, true); }
        else if (k === "Home") { ev.preventDefault(); select(0, true); }
        else if (k === "End") { ev.preventDefault(); select(n - 1, true); }
      });
    });
  });

  /* publication filters */
  var chips = $$(".chip");
  if (chips.length) {
    var pubs = $$(".plist .pub"), groups = $$(".pgroup"), countEl = $(".count span");
    chips.forEach(function (c) {
      c.addEventListener("click", function () {
        var f = c.getAttribute("data-f"), n = 0;
        chips.forEach(function (o) { o.setAttribute("aria-pressed", o === c ? "true" : "false"); });
        pubs.forEach(function (p) {
          var show = f === "all" || (" " + p.getAttribute("data-th") + " ").indexOf(" " + f + " ") > -1;
          p.hidden = !show; if (show) n++;
        });
        groups.forEach(function (g) { g.hidden = !$$(".pub", g).some(function (p) { return !p.hidden; }); });
        if (countEl) countEl.textContent = n;
      });
    });
    /* highlight a publication reached by anchor */
    if (location.hash) {
      var target = document.getElementById(location.hash.slice(1));
      if (target && target.classList.contains("pub")) { target.style.transition = "background .6s"; target.style.background = "color-mix(in srgb, var(--wheat) 18%, transparent)"; setTimeout(function () { target.style.background = ""; }, 2200); }
    }
  }

  /* copy citation */
  $$(".copy").forEach(function (b) {
    b.addEventListener("click", function () {
      var txt = b.getAttribute("data-cite"), lang = root.lang;
      var msg = { en: "Citation copied", fr: "Référence copiée", ar: "تم نسخ المرجع" }[lang] || "Copied";
      function done() { toast(msg); }
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(txt).then(done, fallback);
      else fallback();
      function fallback() {
        var ta = document.createElement("textarea"); ta.value = txt; ta.style.position = "fixed"; ta.style.opacity = "0";
        document.body.appendChild(ta); ta.select();
        try { document.execCommand("copy"); done(); } catch (e) {}
        document.body.removeChild(ta);
      }
    });
  });

  /* fieldwork map */
  $$(".map-box").forEach(function (box) {
    var map = $(".dz-map", box), tip = $(".map-tip", box);
    if (!map || !tip) return;
    var grid = box.closest(".map-grid");
    var items = grid ? $$(".site-list li", grid) : [];
    function hl(w, on) {
      $$('[data-w="' + w + '"]', map).forEach(function (p) { p.classList.toggle("hl", on); });
      items.forEach(function (li) { if (li.getAttribute("data-w") === w) li.classList.toggle("hl", on); });
    }
    function show(p, x, y) {
      tip.innerHTML = "";
      var s = document.createElement("strong"); s.textContent = p.getAttribute("data-name");
      tip.appendChild(s); tip.appendChild(document.createTextNode(p.getAttribute("data-desc")));
      tip.hidden = false;
      var bw = box.clientWidth, tw = tip.offsetWidth;
      var left = Math.min(Math.max(8, x - tw / 2), bw - tw - 8);
      tip.style.left = left + "px"; tip.style.top = Math.max(8, y - tip.offsetHeight - 14) + "px";
      hl(p.getAttribute("data-w"), true);
    }
    function hide(p) { tip.hidden = true; if (p) hl(p.getAttribute("data-w"), false); }
    $$(".w.on", map).forEach(function (p) {
      p.addEventListener("mousemove", function (ev) { var r = box.getBoundingClientRect(); show(p, ev.clientX - r.left, ev.clientY - r.top); });
      p.addEventListener("mouseleave", function () { hide(p); });
      p.addEventListener("focus", function () { var r = box.getBoundingClientRect(), b = p.getBoundingClientRect(); show(p, b.left - r.left + b.width / 2, b.top - r.top + b.height / 2); });
      p.addEventListener("blur", function () { hide(p); });
      p.addEventListener("click", function (ev) { var r = box.getBoundingClientRect(); show(p, ev.clientX - r.left, ev.clientY - r.top); });
    });
    items.forEach(function (li) {
      var w = li.getAttribute("data-w");
      li.addEventListener("mouseenter", function () { hl(w, true); });
      li.addEventListener("mouseleave", function () { hl(w, false); });
    });
  });

  /* print CV */
  var pb = $(".print-btn");
  if (pb) pb.addEventListener("click", function () { window.print(); });

  /* reveal on scroll */
  var rev = $$(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -6% 0px" });
    rev.forEach(function (r) { io.observe(r); });
  } else rev.forEach(function (r) { r.classList.add("in"); });
})();
