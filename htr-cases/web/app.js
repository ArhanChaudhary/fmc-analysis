// The HTR case index: the list of cases from the WebAssembly module (worker.js), drawn with cube.js.
import { CubeView } from './cube.js';

// ---- the worker -------------------------------------------------------------------------------------------------

const worker = new Worker(new URL('./worker.js', import.meta.url), { type: 'module' });
const pending = new Map();
let nextId = 1;
worker.onmessage = (e) => {
  const { id, ok, value, error } = e.data;
  const p = pending.get(id);
  pending.delete(id);
  if (ok) p.resolve(value);
  else p.reject(new Error(error));
};
const call = (op, ...args) =>
  new Promise((resolve, reject) => {
    const id = nextId++;
    pending.set(id, { resolve, reject });
    worker.postMessage({ id, op, args });
  });

// ---- helpers ----------------------------------------------------------------------------------------------------

const $ = (sel, root = document) => root.querySelector(sel);

function el(tag, attrs = {}, ...children) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === 'class') e.className = v;
    else if (k.startsWith('on')) e.addEventListener(k.slice(2), v);
    else if (v !== false && v != null) e.setAttribute(k, v === true ? '' : v);
  }
  for (const c of children.flat()) if (c != null && c !== false) e.append(c);
  return e;
}

const fmt = (n) => n.toLocaleString('en');
const plural = (n, one, many = one + 's') => `${fmt(n)} ${n === 1 ? one : many}`;
const CORNERS = ['UFR', 'UFL', 'UBL', 'UBR', 'DFR', 'DFL', 'DBL', 'DBR'];
const EDGES = ['UF', 'UL', 'UB', 'UR', 'DF', 'DL', 'DB', 'DR'];
const LABEL_TEXT = { 'no parity': 'no parity', parity: 'parity', clockwise: '↻ clockwise', anticlockwise: '↺ anticlockwise' };

function tag(label) {
  return label ? el('span', { class: 'tag', title: label }, LABEL_TEXT[label]) : null;
}

function code(text) {
  return text ? el('code', {}, text) : el('span', { class: 'hint' }, 'nothing');
}

let cases = [];
const byNumber = new Map();

// ---- the list of HTRs -------------------------------------------------------------------------------------------

const SHOW_FIRST = 400;

function htrList(list, moves, max, faces = ['U', 'D']) {
  const box = el('div', { class: 'htrs' });
  if (moves === 0) {
    box.append(el('p', {}, 'This is HTR.'));
    return box;
  }
  const byLength = new Map();
  for (const s of list) {
    const n = s.split(' ').length;
    if (!byLength.has(n)) byLength.set(n, []);
    byLength.get(n).push(s);
  }
  box.append(
    el('p', {},
      moves <= max
        ? `${plural(list.length, 'HTR')} of ${max} moves or less. `
        : `No HTR of ${max} moves or less. The shortest are ${moves} moves: ${fmt(list.length)} of them. `,
      el('span', { class: 'hint' }, `Each ends in a quarter turn that can go either way (${faces[0]} or ${faces[0]}′, ${faces[1]} or ${faces[1]}′); only the clockwise one is written.`)),
  );
  const lengths = [...byLength.keys()].sort((a, b) => a - b);
  for (const n of lengths) {
    const seqs = byLength.get(n);
    const ol = el('ol');
    const fill = (all) => {
      ol.replaceChildren(...seqs.slice(0, all ? seqs.length : SHOW_FIRST).map((s) => el('li', {}, el('code', {}, s))));
      if (!all && seqs.length > SHOW_FIRST) {
        ol.after(el('div', { class: 'more' }, el('button', { type: 'button', onclick: (e) => { e.target.parentElement.remove(); fill(true); } }, `Show all ${fmt(seqs.length)}`)));
      }
    };
    const d = el('details', {}, el('summary', {}, `${n} moves`, el('span', { class: 'n' }, fmt(seqs.length))), ol);
    let filled = false;
    d.addEventListener('toggle', () => {
      if (d.open && !filled) {
        filled = true;
        fill(false);
      }
    });
    d.open = n === lengths[0] || list.length <= 60;
    box.append(d);
  }
  return box;
}

// ---- one case, opened -------------------------------------------------------------------------------------------

function piecesText(corners, edges) {
  const part = (list, what) => (list.length ? `${list.join(' ')}` : `no bad ${what}`);
  return `${part(corners, 'corners')} · ${part(edges, 'edges')}`;
}

function complement(list, all) {
  return all.filter((p) => !list.includes(p));
}

function lookalikeLinks(c) {
  const items = c.lookalikes.map((n) => {
    const o = byNumber.get(n);
    return el('span', {}, `${o.subset} ${o.edges}e `, el('a', { href: `#case-${n}`, onclick: (e) => { e.preventDefault(); openCase(n); } }, `#${n}`),
      ` (${o.moves}${o.label ? ', ' + o.label : ''})`);
  });
  const out = el('span', { class: 'lookalikes' });
  items.forEach((it, i) => out.append(i ? ' · ' : '', it));
  return out;
}

function renderDetail(c, card, startTurned = false) {
  const special = c.number === 1; // HTR with the E slice turned
  const canvas = el('canvas', { width: 300, height: 300, 'aria-label': `Case ${c.number}, bad pieces` });
  const view = el('div', { class: 'view' }, canvas, el('div', { class: 'hint' }, 'Drag to turn · double-click to reset'));
  const facts = el('div', { class: 'facts' });
  const htrs = el('div', { class: 'htrs' }, el('p', { class: 'hint' }, 'Listing the HTRs…'));
  const title = el('h3', {});
  const info = el('div', { class: 'info' }, title, facts);
  const detail = el('div', { class: 'detail' }, view, info, htrs);
  card.append(detail);
  const cube = new CubeView(canvas, { interactive: true });

  let turned = startTurned && c.number !== 1;
  const show = async () => {
    const v = turned ? c.turned : c;
    const corners = turned ? complement(c.bad_corners, CORNERS) : c.bad_corners;
    const edges = turned ? complement(c.bad_edges, EDGES) : c.bad_edges;
    const moves = turned ? c.turned.moves : c.moves;
    cube.set({ corners, edges });
    title.replaceChildren(
      ...[`Case ${c.number} · ${c.subset} ${c.edges}e · ${plural(moves, 'move')} `, tag(v.label),
        el('button', { type: 'button', class: 'close', onclick: () => closeCase(card) }, 'Close')].filter(Boolean));
    const switcher = special
      ? el('span', {}, 'Every corner and edge is bad: HTR with the E slice a quarter turn off. With it turned back, this is HTR itself.')
      : el('span', { class: 'switch' },
          ...[false, true].map((t) =>
            el('label', {},
              el('input', { type: 'radio', name: `turn-${c.number}`, checked: t === turned, onchange: () => { turned = t; show(); } }),
              t ? ` every other piece (${c.turned.corners}c ${c.turned.edges}e: the E slice turned)`
                : ` the solid ones (${c.bad_corners.length}c ${c.bad_edges.length}e)`)));
    const lookText = special
      ? [el('span', { class: 'hint' }, 'Nothing is bad in the frame with few bad pieces, as in these fake HTRs: '), lookalikeLinks(c)]
      : [lookalikeLinks(c), el('div', { class: 'hint' }, 'Same bad pieces, other cases. The corner test tells them apart.')];
    facts.replaceChildren(
      el('span', { class: 'k' }, 'Bad pieces'), el('span', {}, piecesText(corners, edges)),
      el('span', { class: 'k' }, 'Which are bad'), switcher,
      el('span', { class: 'k' }, 'Make it'), el('span', {}, code(v.generator), el('span', { class: 'hint' }, ' from solved')),
      el('span', { class: 'k' }, 'Corner test'), el('span', {}, code(v.corner_test),
        el('span', { class: 'hint' }, special ? ' puts the corners in HTR' : ' puts these corners in HTR; on a lookalike it leaves fake HTR')),
      el('span', { class: 'k' }, 'Lookalikes'), el('span', {}, ...lookText),
    );
    htrs.replaceChildren(el('p', { class: 'hint' }, 'Listing the HTRs…'));
    const shown = turned;
    try {
      const list = await call('solutions', c.number, turned);
      if (shown === turned) htrs.replaceChildren(...htrList(list, moves, 8).childNodes);
    } catch (err) {
      htrs.replaceChildren(el('p', { class: 'error' }, err.message));
    }
  };
  show();
}

// ---- opening and closing ----------------------------------------------------------------------------------------

let openCard = null;

function closeCase(card) {
  card.classList.remove('open');
  card.querySelector('.detail')?.remove();
  if (openCard === card) openCard = null;
  history.replaceState(null, '', location.pathname + location.search);
}

function openCase(n, turned = false) {
  const card = document.getElementById(`case-${n}`);
  if (!card) return;
  if (openCard) closeCase(openCard);
  card.classList.add('open');
  renderDetail(byNumber.get(n), card, turned);
  openCard = card;
  history.replaceState(null, '', `#case-${n}`);
  card.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ---- the index --------------------------------------------------------------------------------------------------

function buildIndex() {
  const root = $('#cases');
  const nav = $('#subset-nav');
  const groups = new Map();
  for (const c of cases) {
    if (!groups.has(c.subset)) groups.set(c.subset, new Map());
    const g = groups.get(c.subset);
    if (!g.has(c.edges)) g.set(c.edges, new Map());
    const h = g.get(c.edges);
    if (!h.has(c.moves)) h.set(c.moves, []);
    h.get(c.moves).push(c);
  }
  const draw = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (!e.isIntersecting) continue;
      draw.unobserve(e.target);
      const c = byNumber.get(Number(e.target.dataset.n));
      new CubeView(e.target).set({ corners: c.bad_corners, edges: c.bad_edges });
    }
  }, { rootMargin: '300px' });

  for (const [subset, byEdges] of groups) {
    const count = [...byEdges.values()].reduce((s, m) => s + [...m.values()].reduce((t, l) => t + l.length, 0), 0);
    nav.append(el('a', { href: `#subset-${subset}` }, subset, el('span', { class: 'n' }, fmt(count))));
    const section = el('section', { class: 'subset', id: `subset-${subset}` }, el('h2', {}, subset, el('span', { class: 'n' }, plural(count, 'case'))));
    for (const [edges, byMoves] of byEdges) {
      const n = [...byMoves.values()].reduce((t, l) => t + l.length, 0);
      const groupsBox = el('div', { class: 'groups' });
      const block = el('div', { class: 'edges' }, el('h3', {}, `${subset} ${edges}e`, el('span', { class: 'n' }, plural(n, 'case'))), groupsBox);
      for (const [moves, list] of byMoves) {
        const grid = el('div', { class: 'grid' });
        for (const c of list) {
          const canvas = el('canvas', { 'data-n': c.number, 'aria-hidden': 'true' });
          const thumb = el('button', { type: 'button', class: 'thumb', title: `Case ${c.number}: ${c.subset} ${c.edges}e, ${plural(c.moves, 'move')}`, onclick: () => openCase(c.number) },
            canvas, el('div', { class: 'cap' }, el('b', {}, `#${c.number}`), tag(c.label)));
          grid.append(el('div', { class: 'case', id: `case-${c.number}` }, thumb));
          draw.observe(canvas);
        }
        groupsBox.append(el('div', { class: 'moves' }, el('h4', {}, `${plural(moves, 'move')} to HTR`, el('span', { class: 'n' }, ` · ${fmt(list.length)}`)), grid));
      }
      section.append(block);
    }
    root.append(section);
  }
}

// ---- find your case ---------------------------------------------------------------------------------------------

const STORE = 'htr-cases-find';

async function find(e) {
  e?.preventDefault();
  const scramble = $('#find-scramble').value;
  const moves = $('#find-moves').value;
  try { localStorage.setItem(STORE, JSON.stringify({ scramble, moves })); } catch { /* storage may be off */ }
  const out = $('#find-result');
  out.replaceChildren(el('p', { class: 'hint' }, 'Looking…'));
  let f;
  try {
    f = await call('find', scramble, moves);
  } catch (err) {
    out.replaceChildren(el('p', { class: 'error' }, err.message));
    return;
  }
  const canvas = el('canvas', { width: 300, height: 300, 'aria-label': 'Your DR, bad pieces' });
  const which = f.highlighted_are_bad
    ? `the solid ones (${f.bad[0]}c ${f.bad[1]}e)`
    : `every piece but the solid ones (${f.bad[0]}c ${f.bad[1]}e: the slice between your DR faces is a quarter turn off)`;
  const facts = el('div', { class: 'facts' },
    el('span', { class: 'k' }, 'DR axis'), el('span', {}, f.axis),
    el('span', { class: 'k' }, 'Which are bad'), el('span', {}, which),
    el('span', { class: 'k' }, 'Corner test'), el('span', {}, code(f.corner_test), el('span', { class: 'hint' }, ' puts your corners in HTR')),
    el('span', { class: 'k' }, 'In the index'), el('span', {}, el('a', { href: `#case-${f.number}`, onclick: (ev) => { ev.preventDefault(); openCase(f.number, f.turned); } }, `case ${f.number}`),
      el('span', { class: 'hint' }, f.turned
        ? ' with the slice between your DR faces turned: its bad pieces are your good ones (the case\'s switch shows yours)'
        : ' (drawn with the DR on U/D, maybe turned or mirrored)')),
  );
  const detail = el('div', { class: 'detail' },
    el('div', { class: 'view' }, canvas, el('div', { class: 'hint' }, 'Your cube as you hold it · drag to turn')),
    el('div', { class: 'info' }, el('h3', {}, `${f.subset} ${f.edges}e · ${plural(f.moves, 'move')} to HTR `, tag(f.label)), facts),
    htrList(f.solutions, f.moves, 8, { 'R/L': ['R', 'L'], 'U/D': ['U', 'D'], 'F/B': ['F', 'B'] }[f.axis]));
  out.replaceChildren(el('div', { class: 'case open' }, detail));
  new CubeView(canvas, { interactive: true }).set({ corners: f.corners, edges: f.edge_pieces });
}

// ---- start ------------------------------------------------------------------------------------------------------

async function start() {
  const status = $('#status');
  try {
    const saved = JSON.parse(localStorage.getItem(STORE) || 'null');
    if (saved) {
      $('#find-scramble').value = saved.scramble || '';
      $('#find-moves').value = saved.moves || '';
    }
  } catch { /* storage may be off */ }
  try {
    cases = await call('cases');
  } catch (err) {
    status.textContent = `The cases could not be loaded: ${err.message}`;
    status.classList.add('failed');
    return;
  }
  for (const c of cases) byNumber.set(c.number, c);
  buildIndex();
  status.classList.add('done');
  $('#find-form').addEventListener('submit', find);
  $('#find-form button[type=submit]').disabled = false;
  const m = location.hash.match(/^#case-(\d+)$/);
  if (m) openCase(Number(m[1]));
}

start();
