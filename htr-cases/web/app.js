// The HTR case index: the list of cases from the WebAssembly module (worker.js), drawn with cube.js.
import { CubeView, DEFAULT_VIEW } from './cube.js';

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
const LABEL_TEXT = { 'no parity': 'no parity', parity: 'parity', clockwise: '↻ clockwise', anticlockwise: '↺ anticlockwise', good: 'good', bad: 'bad' };

function tag(label) {
  return label ? el('span', { class: 'tag', title: label }, LABEL_TEXT[label]) : null;
}

let cases = [];
const byNumber = new Map();

// ---- the list of HTRs -------------------------------------------------------------------------------------------

const SHOW_FIRST = 400;
const ABOVE_SHORTEST = 4; // a case lists HTRs at most this many moves over its shortest (as htr_cases::ABOVE_SHORTEST)

// The HTRs of a case, `moves` from HTR, listed up to `max` moves (see the slider; at most ABOVE_SHORTEST over the
// shortest, and the shortest when none is that short).
function htrList(list, moves, max) {
  const box = el('div', { class: 'htrs' });
  if (moves === 0) {
    box.append(el('p', {}, 'This is HTR.'));
    return box;
  }
  const longest = Math.min(max, moves + ABOVE_SHORTEST);
  const byLength = new Map();
  for (const s of list) {
    const n = s.split(' ').length;
    if (!byLength.has(n)) byLength.set(n, []);
    byLength.get(n).push(s);
  }
  box.append(
    el('p', {},
      moves > max
        ? `No HTR of ${plural(max, 'move')} or less. The shortest are ${moves} moves: ${fmt(list.length)} of them, up to the E slice.`
        : `${plural(list.length, 'HTR')} of ${plural(longest, 'move')} or less${longest < max ? ` (${ABOVE_SHORTEST} over the shortest)` : ''}, up to the E slice.`),
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

// ---- the side panel --------------------------------------------------------------------------------------------
// The list never moves when a case is opened: the case opens in the panel beside it (over it, on a phone), and the
// card is only marked.  "Show in list" scrolls the list to the card.

const side = {};
let sideCube = null;
let selection = null; // { n }: a case of the index; { found }: a solver's own DR
let selectedCard = null;
let renderToken = 0;
const narrow = () => matchMedia('(max-width: 44rem)').matches;

const caseLink = (n, text = `#${n}`) => el('a', { href: `#case-${n}`, onclick: (e) => { e.preventDefault(); selectCase(n); } }, text);

function lookalikeLinks(c) {
  const out = el('span', { class: 'lookalikes' });
  c.lookalikes.forEach((n, i) => {
    const o = byNumber.get(n);
    out.append(i ? ' · ' : '', el('span', {}, `${o.subset} ${o.edges}e `, caseLink(n), ` (${o.moves}${o.label ? ', ' + o.label : ''})`));
  });
  return out;
}

// the pair of a case a U2 away (see the page's notes): in the merged index both are one card
function pairRow(c) {
  if (!c.u2_mates.length) return [];
  const pick = merge
    ? el('span', { class: 'switch' }, ...[c.number, ...c.u2_mates].sort((a, b) => a - b).map((n) =>
        el('label', {}, el('input', { type: 'radio', name: 'pair', checked: n === c.number, onchange: () => selectCase(n) }),
          ` #${n}${byNumber.get(n).label ? ` (${byNumber.get(n).label})` : ''}`)))
    : el('span', {}, ...c.u2_mates.flatMap((n, i) => [i ? ' · ' : '', caseLink(n)]));
  return [el('span', { class: 'k' }, 'A U2 away'), el('span', {}, pick,
    el('div', { class: 'hint' }, 'The other is this one after U2, seen from some side; a shortest HTR of each starts with a quarter turn of that layer, U on one and U′ on the other, and after it they are the same case.'))];
}

function markCard(n) {
  selectedCard?.classList.remove('selected');
  selectedCard?.querySelector('.thumb')?.removeAttribute('aria-current');
  selectedCard = n ? document.getElementById(`case-${merge ? leaderOf(n) : n}`) : null;
  selectedCard?.classList.add('selected');
  selectedCard?.querySelector('.thumb')?.setAttribute('aria-current', 'true');
}

function showSide(fresh) {
  side.locate.hidden = !selectedCard;
  side.close.hidden = false;
  side.panel.classList.add('active');
  if (fresh) side.panel.scrollTop = 0;
}

function closeSide() {
  renderToken++;
  selection = null;
  markCard(null);
  side.name.textContent = 'No case open';
  side.locate.hidden = side.close.hidden = true;
  side.viewHint.textContent = 'Drag to turn · double-click to reset';
  sideCube.reset();
  sideCube.set({ corners: [], edges: [] });
  side.heading.replaceChildren();
  side.facts.replaceChildren();
  side.htrs.replaceChildren(side.emptyText);
  side.panel.classList.remove('active');
  side.panel.scrollTop = 0;
  history.replaceState(null, '', location.pathname + location.search);
}

// scroll the list to the open case's card (the only time the list moves)
function locate(instant = false) {
  if (!selectedCard) return;
  if (narrow()) side.panel.classList.remove('active');
  selectedCard.scrollIntoView({ behavior: instant ? 'instant' : 'smooth', block: 'center' });
  selectedCard.querySelector('.thumb').focus({ preventScroll: true });
}

function selectCase(n) {
  const fresh = selection?.n !== n;
  selection = { n };
  markCard(n);
  history.replaceState(null, '', `#case-${n}`);
  renderCase(byNumber.get(n), fresh);
}

async function renderCase(c, fresh) {
  const token = ++renderToken;
  side.name.textContent = `Case ${c.number}`;
  side.viewHint.textContent = 'Drag to turn · double-click to reset';
  if (fresh) sideCube.view = { ...DEFAULT_VIEW };
  sideCube.set({ corners: c.bad_corners, edges: c.bad_edges });
  side.heading.replaceChildren(`${c.subset} ${c.edges}e · ${plural(c.moves, 'move')} to HTR `, ...[tag(c.label)].filter(Boolean));
  side.facts.replaceChildren(
    el('span', { class: 'k' }, 'Lookalikes'), el('span', {}, lookalikeLinks(c)),
    ...pairRow(c),
  );
  side.htrs.replaceChildren(el('p', { class: 'hint' }, 'Listing the HTRs…'));
  showSide(fresh);
  try {
    const list = await call('solutions', c.number, false, cap);
    // (case 1, HTR up to the E slice, lists only its shortest: the E slice itself)
    if (token === renderToken) side.htrs.replaceChildren(...htrList(list, c.moves, c.number === 1 ? c.moves : cap).childNodes);
  } catch (err) {
    if (token === renderToken) side.htrs.replaceChildren(el('p', { class: 'error' }, err.message));
  }
}

function renderFound(f, text, fresh = true) {
  renderToken++;
  selection = { found: f, text };
  markCard(f.number);
  history.replaceState(null, '', location.pathname + location.search);
  side.name.textContent = 'Your DR';
  side.viewHint.textContent = 'Your cube as you hold it · drag to turn';
  if (fresh) sideCube.view = { ...DEFAULT_VIEW };
  sideCube.set({ corners: f.corners, edges: f.edge_pieces });
  side.heading.replaceChildren(`${f.subset} ${f.edges}e · ${plural(f.moves, 'move')} to HTR `, ...[tag(f.label)].filter(Boolean));
  side.facts.replaceChildren(
    el('span', { class: 'k' }, 'DR axis'), el('span', {}, f.axis),
    el('span', { class: 'k' }, 'In the index'), el('span', {},
      caseLink(f.number, `case ${f.number}`),
      el('span', { class: 'hint' }, f.turned
        ? ' with the slice between your DR faces turned: its bad pieces are your good ones'
        : ' (drawn with the DR on U/D, maybe turned or mirrored)')),
  );
  side.htrs.replaceChildren(...htrList(f.solutions, f.moves, f.number === 1 ? f.moves : cap).childNodes);
  showSide(fresh);
}

// ---- the index --------------------------------------------------------------------------------------------------

let merge = false;
let observer = null;
const leaderOf = (n) => Math.min(n, ...byNumber.get(n).u2_mates);
const membersOf = (c) => (merge ? [c.number, ...c.u2_mates].sort((a, b) => a - b) : [c.number]);

function buildIndex() {
  const root = $('#cases');
  const nav = $('#subset-nav');
  root.replaceChildren();
  nav.replaceChildren();
  observer?.disconnect();
  selectedCard = null;
  const groups = new Map();
  for (const c of cases) {
    if (merge && leaderOf(c.number) !== c.number) continue;
    if (!groups.has(c.subset)) groups.set(c.subset, new Map());
    const g = groups.get(c.subset);
    if (!g.has(c.edges)) g.set(c.edges, new Map());
    const h = g.get(c.edges);
    if (!h.has(c.moves)) h.set(c.moves, []);
    h.get(c.moves).push(c);
  }
  const draw = (observer = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (!e.isIntersecting) continue;
      draw.unobserve(e.target);
      const c = byNumber.get(Number(e.target.dataset.n));
      new CubeView(e.target).set({ corners: c.bad_corners, edges: c.bad_edges });
    }
  }, { root: $('#list'), rootMargin: '300px' }));
  const casesIn = (list) => list.reduce((t, c) => t + membersOf(c).length, 0);
  const counted = (list) => (merge ? `${plural(casesIn(list), 'case')} · ${fmt(list.length)} entries` : plural(list.length, 'case'));

  for (const [subset, byEdges] of groups) {
    const all = [...byEdges.values()].flatMap((m) => [...m.values()].flat());
    nav.append(el('a', { href: `#subset-${subset}` }, subset, el('span', { class: 'n' }, fmt(all.length))));
    const section = el('section', { class: 'subset', id: `subset-${subset}` }, el('h2', {}, subset, el('span', { class: 'n' }, counted(all))));
    for (const [edges, byMoves] of byEdges) {
      const groupsBox = el('div', { class: 'groups' });
      const block = el('div', { class: 'edges' }, el('h3', {}, `${subset} ${edges}e`, el('span', { class: 'n' }, counted([...byMoves.values()].flat()))), groupsBox);
      for (const [moves, list] of byMoves) {
        const grid = el('div', { class: 'grid' });
        for (const c of list) {
          const canvas = el('canvas', { 'data-n': c.number, 'aria-hidden': 'true' });
          const members = membersOf(c);
          const labels = [...new Set(members.map((n) => byNumber.get(n).label).filter(Boolean))];
          // a card already open (in the merged index, either case of it) stays as it is; on a phone it opens the panel again
          const open = () => (selection?.n && members.includes(selection.n) ? showSide(false) : selectCase(c.number));
          const thumb = el('button', { type: 'button', class: 'thumb', title: `Case ${members.join(' and ')}: ${c.subset} ${c.edges}e, ${plural(c.moves, 'move')}`, onclick: open },
            canvas, el('div', { class: 'cap' }, el('b', {}, members.map((n) => `#${n}`).join(' · ')), ...labels.map(tag)));
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
const MERGE = 'htr-cases-merge';

async function find(e, text = $('#find-text').value, fresh = true) {
  e?.preventDefault();
  try { localStorage.setItem(STORE, JSON.stringify({ text })); } catch { /* storage may be off */ }
  const error = $('#find-error');
  try {
    renderFound(await call('find', text, cap), text, fresh);
    error.hidden = true;
  } catch (err) {
    error.textContent = err.message;
    error.hidden = false;
  }
}

// ---- the length HTRs are listed to ------------------------------------------------------------------------------

const CAP = 'htr-cases-cap';
let cap = 8;
let capTimer = null;

function setCap(value, { redraw = true } = {}) {
  cap = value;
  $('#cap').value = String(cap);
  $('#cap-value').textContent = String(cap);
  try { localStorage.setItem(CAP, String(cap)); } catch { /* storage may be off */ }
  if (!redraw) return;
  // the open case or DR again, at the new length (after the slider rests a moment)
  clearTimeout(capTimer);
  capTimer = setTimeout(() => {
    if (selection?.n) renderCase(byNumber.get(selection.n), false);
    else if (selection?.found) find(null, selection.text, false);
  }, 150);
}

// ---- start ------------------------------------------------------------------------------------------------------

async function start() {
  const status = $('#status');
  try {
    const saved = JSON.parse(localStorage.getItem(STORE) || 'null');
    if (saved) $('#find-text').value = saved.text ?? [saved.scramble, saved.moves].filter(Boolean).join('\n');
  } catch { /* storage may be off */ }
  try {
    cases = await call('cases');
  } catch (err) {
    status.textContent = `The cases could not be loaded: ${err.message}`;
    status.classList.add('failed');
    return;
  }
  for (const c of cases) byNumber.set(c.number, c);
  Object.assign(side, {
    panel: $('#side'), name: $('#side-name'), locate: $('#side-locate'), close: $('#side-close'), viewHint: $('#side-view-hint'),
    heading: $('#side-heading'), facts: $('#side-facts'), htrs: $('#side-htrs'),
  });
  side.emptyText = side.htrs.firstElementChild;
  sideCube = new CubeView($('#side-canvas'), { interactive: true });
  new ResizeObserver(() => sideCube.draw()).observe($('#side-canvas'));
  side.locate.addEventListener('click', () => locate());
  side.close.addEventListener('click', closeSide);
  let savedCap = NaN;
  try { savedCap = Number(localStorage.getItem(CAP)); } catch { /* storage may be off */ }
  const slider = $('#cap');
  setCap(savedCap >= Number(slider.min) && savedCap <= Number(slider.max) ? savedCap : 8, { redraw: false });
  slider.addEventListener('input', () => setCap(Number(slider.value)));
  const box = $('#merge');
  try { merge = localStorage.getItem(MERGE) === '1'; } catch { /* storage may be off */ }
  box.checked = merge;
  box.addEventListener('change', () => {
    merge = box.checked;
    try { localStorage.setItem(MERGE, merge ? '1' : '0'); } catch { /* storage may be off */ }
    buildIndex();
    if (selection?.n) {
      markCard(selection.n);
      renderCase(byNumber.get(selection.n), false); // its pair is shown one way or the other
    } else if (selection?.found) markCard(selection.found.number);
  });
  buildIndex();
  status.classList.add('done');
  $('#find-form').addEventListener('submit', find);
  $('#find-form button[type=submit]').disabled = false;
  const m = location.hash.match(/^#case-(\d+)$/);
  if (m && byNumber.has(Number(m[1]))) {
    selectCase(Number(m[1]));
    if (!narrow()) locate(true); // opened from a link: the list starts at its card
  }
}

start();
