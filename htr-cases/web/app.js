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
const optimal = (moves) => `${moves}-optimal`;
const LABEL_TEXT = { clockwise: '↻ clockwise', anticlockwise: '↺ anticlockwise' };

function tag(label) {
  return label ? el('span', { class: 'tag', title: label }, LABEL_TEXT[label] ?? label) : null;
}
const tags = (labels) => labels.map(tag);

// settings kept in this browser only (each a convenience: the page works without them)
const load = (key) => { try { return localStorage.getItem(key); } catch { return null; } };
const save = (key, value) => { try { localStorage.setItem(key, value); } catch { /* storage may be off */ } };
const STORE = 'htr-cases-find';
const MERGE = 'htr-cases-merge';
const OPTIMAL = 'htr-cases-optimal';
const ABOVE = 'htr-cases-above';

let cases = [];
const byNumber = new Map();
let merge = false; // pairs a U2 apart as one entry
let maxOptimal = 13; // the list shows cases with optimal this or less
let above = 2; // the panel lists HTRs up to this many moves over the optimal
const LONGEST = 11; // ... but not past this many (htr_cases::LONGEST)

const debounce = (f, ms = 120) => {
  let timer = null;
  return (...args) => { clearTimeout(timer); timer = setTimeout(() => f(...args), ms); };
};

// ---- the list of HTRs -------------------------------------------------------------------------------------------

const SHOW_FIRST = 400;

// The HTRs listed, one fold per length (the shortest open).
function htrList(list) {
  const byLength = new Map();
  for (const s of list) {
    const n = s.split(' ').length;
    if (!byLength.has(n)) byLength.set(n, []);
    byLength.get(n).push(s);
  }
  const lengths = [...byLength.keys()].sort((a, b) => a - b);
  return lengths.map((n) => {
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
    return d;
  });
}

// "156 HTRs of 7 moves or less", and why the list stops short of the slider when it does
function countText(n, longest, moves, onlyTheSlice) {
  const short = !onlyTheSlice && longest < moves + above
    ? (moves >= LONGEST ? ` (past ${LONGEST} moves, only the optimal ones)` : ` (${LONGEST} moves at most)`)
    : '';
  return `${plural(n, 'HTR')} of ${plural(longest, 'move')} or less, up to the E slice${short}`;
}

// ---- the side panel --------------------------------------------------------------------------------------------
// The list never moves when a case is opened: the case opens in the panel beside it (over it, on a phone), and the
// card is only marked.  "Show in list" scrolls the list to the card (on a phone, it goes back to the list).

const side = {};
let sideCube = null;
let selection = null; // { n }: a case of the index; { found, text }: a solver's own DR
let selectedCard = null;
let renderToken = 0;
const narrow = () => matchMedia('(max-width: 44rem)').matches;

const caseLink = (n, text = `#${n}`) => el('a', { href: `#case-${n}`, onclick: (e) => { e.preventDefault(); selectCase(n); } }, text);

function lookalikeLinks(c) {
  const out = el('span', { class: 'lookalikes' });
  const same = new Map(c.siblings); // the same case seen another way: how
  c.lookalikes.forEach((n, i) => {
    const o = byNumber.get(n);
    const how = same.has(n) ? [`this one ${same.get(n)}`] : [];
    out.append(i ? ' · ' : '', el('span', {}, `${o.subset} ${o.edges}e `, caseLink(n), ` (${[optimal(o.moves), ...o.labels, ...how].join(', ')})`));
  });
  return out;
}

// the pair of a case a U2 away (see the page's notes): in the merged index both are one card
function pairRow(c) {
  if (!c.u2_mates.length) return [];
  const pick = merge
    ? el('span', { class: 'switch' }, ...[c.number, ...c.u2_group].sort((a, b) => a - b).map((n) =>
        el('label', {}, el('input', { type: 'radio', name: 'pair', checked: n === c.number, onchange: () => selectCase(n) }),
          ` #${n}${byNumber.get(n).labels.length ? ` (${byNumber.get(n).labels.join(', ')})` : ''}`)))
    : el('span', {}, ...c.u2_mates.flatMap((n, i) => [i ? ' · ' : '', caseLink(n)]));
  return [el('span', { class: 'k' }, 'A U2 away'), pick];
}

function markCard(n) {
  selectedCard?.classList.remove('selected');
  selectedCard?.querySelector('.thumb')?.removeAttribute('aria-current');
  selectedCard = n ? document.getElementById(`case-${merge ? leaderOf(n) : n}`) : null;
  selectedCard?.classList.add('selected');
  selectedCard?.querySelector('.thumb')?.setAttribute('aria-current', 'true');
  if (selection) side.locate.hidden = !selectedCard && !narrow();
}

// the title bar: the case, its subset and edges, its optimal and its label
function title(name, c) {
  side.name.replaceChildren(el('b', {}, name), el('span', { class: 'sub' }, `${c.subset} ${c.edges}e · ${optimal(c.moves)}`), ...tags(c.labels));
}

function showSide(fresh) {
  side.locate.hidden = !selectedCard && !narrow();
  side.over.hidden = false;
  side.panel.classList.add('active');
  if (fresh) side.panel.scrollTop = 0;
}

// scroll the list to the open case's card (the only time the list moves); on a phone, back to the list
function locate(instant = false) {
  if (narrow()) side.panel.classList.remove('active');
  if (!selectedCard) return;
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
  title(`Case ${c.number}`, c);
  side.viewHint.textContent = 'Drag to rotate · double-click to reset';
  if (fresh) sideCube.view = { ...DEFAULT_VIEW };
  sideCube.set({ corners: c.bad_corners, edges: c.bad_edges });
  side.facts.replaceChildren(el('span', { class: 'k' }, 'Lookalikes'), el('span', {}, lookalikeLinks(c)), ...pairRow(c));
  side.count.textContent = 'Listing the HTRs…';
  if (fresh) side.htrs.replaceChildren();
  showSide(fresh);
  try {
    const { longest, htrs } = await call('solutions', c.number, false, above);
    if (token !== renderToken) return;
    side.count.textContent = countText(htrs.length, longest, c.moves, c.number === 1);
    side.htrs.replaceChildren(...htrList(htrs));
  } catch (err) {
    if (token === renderToken) side.htrs.replaceChildren(el('p', { class: 'error' }, err.message));
  }
}

function renderFound(f, text, fresh = true) {
  renderToken++;
  selection = { found: f, text };
  markCard(f.number);
  history.replaceState(null, '', location.pathname + location.search);
  title('Your DR', f);
  side.viewHint.textContent = 'Your cube as you hold it · drag to rotate';
  if (fresh) sideCube.view = { ...DEFAULT_VIEW };
  sideCube.set({ corners: f.corners, edges: f.edge_pieces });
  side.facts.replaceChildren(
    el('span', { class: 'k' }, 'DR axis'), el('span', {}, f.axis),
    el('span', { class: 'k' }, 'In the index'), el('span', {},
      caseLink(f.number, `case ${f.number}`),
      el('span', { class: 'hint' }, f.turned
        ? ' with the slice between your DR faces turned: its bad pieces are your good ones'
        : ' (drawn with the DR on U/D, maybe rotated or mirrored)')),
  );
  side.count.textContent = countText(f.solutions.length, f.longest, f.moves, f.number === 1);
  side.htrs.replaceChildren(...htrList(f.solutions));
  showSide(fresh);
}

// the panel's slider: how many moves over the optimal the HTRs listed go
const redrawSide = debounce(() => {
  if (selection?.n) renderCase(byNumber.get(selection.n), false);
  else if (selection?.found) find(null, selection.text, false);
});

function setAbove(value, redraw = true) {
  above = value;
  $('#above').value = String(above);
  $('#above-value').textContent = `+${above}`;
  save(ABOVE, String(above));
  if (redraw) redrawSide();
}

// ---- the index --------------------------------------------------------------------------------------------------

let observer = null;
const leaderOf = (n) => Math.min(n, ...byNumber.get(n).u2_group);
const membersOf = (c) => (merge ? [c.number, ...c.u2_group].sort((a, b) => a - b) : [c.number]);

function buildIndex() {
  const root = $('#cases');
  const nav = $('#subset-nav');
  root.replaceChildren();
  nav.replaceChildren();
  observer?.disconnect();
  selectedCard = null;
  // subsets where some case has a label: there every card has a row for them, so the cubes line up
  const labelled = new Set(cases.filter((c) => c.labels.length).map((c) => c.subset));
  const groups = new Map();
  for (const c of cases) {
    if (merge && leaderOf(c.number) !== c.number) continue;
    if (c.moves > maxOptimal) continue; // (the two cases of a pair have the same optimal)
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
          const labels = [...new Set(members.flatMap((n) => byNumber.get(n).labels))];
          // a card already open (in the merged index, either case of it) stays as it is; on a phone it opens the panel again
          const open = () => (selection?.n && members.includes(selection.n) ? showSide(false) : selectCase(c.number));
          const thumb = el('button', { type: 'button', class: 'thumb', title: `Case ${members.join(' and ')}: ${c.subset} ${c.edges}e, ${optimal(c.moves)}`, onclick: open },
            labelled.has(subset) ? el('div', { class: 'tags' }, ...labels.map(tag)) : null,
            canvas, el('div', { class: 'cap' }, el('b', {}, members.map((n) => `#${n}`).join(' · '))));
          grid.append(el('div', { class: 'case', id: `case-${c.number}` }, thumb));
          draw.observe(canvas);
        }
        groupsBox.append(el('div', { class: 'moves' }, el('h4', {}, optimal(moves), el('span', { class: 'n' }, ` · ${fmt(list.length)}`)), grid));
      }
      section.append(block);
    }
    root.append(section);
  }
  if (!groups.size) root.append(el('p', { class: 'hint' }, 'No case is that short.'));
}

// the list's filter and merge switch: rebuild the list, and mark the open case's card again
function rebuild() {
  buildIndex();
  if (selection?.n) markCard(selection.n);
  else if (selection?.found) markCard(selection.found.number);
}
const rebuildSoon = debounce(rebuild);

function setOptimal(value, redraw = true) {
  maxOptimal = value;
  $('#optimal').value = String(maxOptimal);
  $('#optimal-value').textContent = String(maxOptimal);
  save(OPTIMAL, String(maxOptimal));
  if (redraw) rebuildSoon();
}

// ---- find your case ---------------------------------------------------------------------------------------------

async function find(e, text = $('#find-text').value, fresh = true) {
  e?.preventDefault();
  save(STORE, JSON.stringify({ text }));
  const error = $('#find-error');
  try {
    renderFound(await call('find', text, above), text, fresh);
    error.hidden = true;
  } catch (err) {
    error.textContent = err.message;
    error.hidden = false;
  }
}

// ---- start ------------------------------------------------------------------------------------------------------

async function start() {
  const status = $('#status');
  try {
    const saved = JSON.parse(load(STORE) || 'null');
    if (saved) $('#find-text').value = saved.text ?? [saved.scramble, saved.moves].filter(Boolean).join('\n');
  } catch { /* an old or broken entry */ }
  try {
    cases = await call('cases');
  } catch (err) {
    status.textContent = `The cases could not be loaded: ${err.message}`;
    status.classList.add('failed');
    return;
  }
  for (const c of cases) byNumber.set(c.number, c);
  call('prepare').catch(() => {}); // the search's tables, built while the list is looked at
  Object.assign(side, {
    panel: $('#side'), name: $('#side-name'), locate: $('#side-locate'), viewHint: $('#side-view-hint'),
    facts: $('#side-facts'), over: $('#side-over'), count: $('#side-count'), htrs: $('#side-htrs'),
  });
  sideCube = new CubeView($('#side-canvas'), { interactive: true });
  new ResizeObserver(() => sideCube.draw()).observe($('#side-canvas'));
  side.locate.addEventListener('click', () => locate());

  // the two sliders and the merge switch, as this browser last left them
  const within = (input, value) => (value >= Number(input.min) && value <= Number(input.max) ? value : null);
  const optimalInput = $('#optimal');
  const longestOptimal = Math.max(...cases.map((c) => c.moves));
  optimalInput.max = String(longestOptimal);
  setOptimal(within(optimalInput, Number(load(OPTIMAL) ?? NaN)) ?? longestOptimal, false);
  optimalInput.addEventListener('input', () => setOptimal(Number(optimalInput.value)));
  const aboveInput = $('#above');
  setAbove(within(aboveInput, Number(load(ABOVE) ?? NaN)) ?? 2, false);
  aboveInput.addEventListener('input', () => setAbove(Number(aboveInput.value)));
  const box = $('#merge');
  merge = load(MERGE) === '1';
  box.checked = merge;
  box.addEventListener('change', () => {
    merge = box.checked;
    save(MERGE, merge ? '1' : '0');
    rebuild();
    if (selection?.n) renderCase(byNumber.get(selection.n), false); // its pair is shown one way or the other
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
