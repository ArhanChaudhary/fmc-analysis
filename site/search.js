// Search over every listed page of the site, section by section (index: search-index.json, written by
// scripts/search-index.py).  A section matches when it holds every word of the query; "quoted words" match as a phrase.
// Matching ignores case.  Results link to the section.
(function () {
  'use strict';
  var box = document.getElementById('q');
  var out = document.getElementById('results');
  var info = document.getElementById('search-info');
  var index = null, loading = null, timer = null;
  var LIMIT = 60;

  function load() {
    if (index) return Promise.resolve(index);
    if (!loading) {
      info.textContent = 'Loading the index…';
      loading = fetch('search-index.json').then(function (r) {
        if (!r.ok) throw new Error(r.status);
        return r.json();
      }).then(function (data) {
        data.forEach(function (e) { e.lt = e.t.toLowerCase(); e.ls = e.s.toLowerCase(); e.lp = e.p.toLowerCase(); });
        index = data;
        return data;
      });
    }
    return loading;
  }

  function terms(q) {
    var m = q.toLowerCase().match(/"[^"]+"|\S+/g) || [];
    return m.map(function (t) { return t.replace(/^"|"$/g, '').trim(); }).filter(function (t) { return t.length > 0; });
  }

  function count(hay, needle) {
    var n = 0, i = hay.indexOf(needle);
    while (i !== -1 && n < 25) { n++; i = hay.indexOf(needle, i + needle.length); }
    return n;
  }

  function esc(s) {
    return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }

  function reEsc(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

  function mark(text, ts) {
    // split on the terms (the capture group keeps them at the odd positions), escape every piece
    var re = new RegExp('(' + ts.map(reEsc).sort(function (a, b) { return b.length - a.length; }).join('|') + ')', 'i');
    return text.split(re).map(function (p, i) { return i % 2 ? '<mark>' + esc(p) + '</mark>' : esc(p); }).join('');
  }

  function snippet(e, ts) {
    var best = -1;
    ts.forEach(function (t) { var i = e.lt.indexOf(t); if (i !== -1 && (best === -1 || i < best)) best = i; });
    if (best === -1) return e.t.slice(0, 220) + (e.t.length > 220 ? ' …' : '');
    var a = Math.max(0, best - 90), b = Math.min(e.t.length, best + 200);
    while (a > 0 && e.t[a - 1] !== ' ') a--;
    while (b < e.t.length && e.t[b] !== ' ') b++;
    return (a > 0 ? '… ' : '') + e.t.slice(a, b) + (b < e.t.length ? ' …' : '');
  }

  function run() {
    var q = box.value.trim();
    var url = q ? '?q=' + encodeURIComponent(q) : location.pathname;
    history.replaceState(null, '', url);
    if (!q) { out.innerHTML = ''; info.textContent = ''; return; }
    load().then(function (data) {
      var ts = terms(q);
      var hits = [];
      data.forEach(function (e) {
        var score = 0;
        for (var k = 0; k < ts.length; k++) {
          var t = ts[k];
          var inText = count(e.lt, t), inHead = e.ls.indexOf(t) !== -1, inPage = e.lp.indexOf(t) !== -1;
          if (!inText && !inHead && !inPage) return;
          score += inText + (inHead ? 15 : 0) + (inPage ? 3 : 0);
        }
        if (e.k === 'Write-up' || e.k === 'Reference table') score += 4;
        hits.push([score, e]);
      });
      hits.sort(function (a, b) { return b[0] - a[0]; });
      info.textContent = hits.length === 0 ? 'No section has all of these words.' :
        hits.length + (hits.length === 1 ? ' section matches' : ' sections match') +
        (hits.length > LIMIT ? '; the first ' + LIMIT + ' are shown.' : '.');
      out.innerHTML = hits.slice(0, LIMIT).map(function (h) {
        var e = h[1];
        return '<li><a href="' + esc(e.u) + '">' + mark(e.s, ts) + '</a>' +
          '<div class="where">' + esc(e.p) + ' · ' + esc(e.k) + '</div>' +
          '<div class="snip">' + mark(snippet(e, ts), ts) + '</div></li>';
      }).join('');
    }).catch(function () { info.textContent = 'The search index could not be loaded.'; });
  }

  box.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(run, 150); });
  var q0 = new URLSearchParams(location.search).get('q');
  if (q0) { box.value = q0; run(); }
  box.focus();
})();
