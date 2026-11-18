// The simulator page: settings form, running an attempt in the worker, and showing what it did.

const KINDS = ['look', 'eo_scan', 'eo_write', 'eo_eval', 'rzp', 'switch', 'dr_find', 'dr_read', 'htr', 'tail', 'write'];
const KIND_LABEL = {
  look: 'Look', eo_scan: 'EO search', eo_write: 'EO written', eo_eval: 'EO glance', rzp: 'RZP', switch: 'Switch',
  dr_find: 'DR found', dr_read: 'DR read', htr: 'HTR route', tail: 'Finish', write: 'Write down',
};
const KIND_LONG = {
  look: 'counting bad edges', eo_scan: 'searching for EOs', eo_write: 'writing EOs down', eo_eval: 'glancing at EOs',
  rzp: 'working RZP states', switch: 'switching to the other side', dr_find: 'writing DRs down', dr_read: 'reading DRs',
  htr: 'trying HTR routes', tail: 'writing out finishes', write: 'writing the solution down',
};

// ------------------------------------------------------------------------------------------------ settings form

const S = 'seconds';
const SCHEMA = {
  costs: [
    { k: 'budget', label: 'Length of the attempt', unit: S, help: '3600 is an hour. The plan\'s clock times scale with it.' },
    { k: 'look', label: 'Counting bad edges', unit: S, help: 'On the three axes, before anything else.' },
    { k: 'eo_scan', label: 'Searching one axis for EOs one move longer', unit: S, arr: 'EO length',
      help: 'Both sides. Cumulative per axis: 20 s to length 4, 50 s to length 5; a pass over the six axis-sides takes under 2 minutes.' },
    { k: 'eo_niss_factor', label: 'NISS factor for the EO search', unit: '×', help: 'The same search when EOs with moves on both sides are looked for too.' },
    { k: 'eo_write', label: 'Writing an EO down', unit: S, help: '7 to 20 s per EO all in.' },
    { k: 'eo_eval', label: 'Glancing at an EO', unit: S, help: 'Bad corners and bad edges on its two DR axes, both endings (3 to 5 s to throw away a 4-mover).' },
    { k: 'rzp', label: 'Working an RZP state', unit: S, help: '10 to 30 s per RZP.' },
    { k: 'switch', label: 'Working a state on the other side', unit: S, help: 'Setting the inverse up first (20 to 30 s per switch).' },
    { k: 'dr_find', label: 'Writing down a DR that was seen', unit: S, arr: 'moves away', help: 'Index: how many moves away the DR was when it was seen.' },
    { k: 'dr_read', label: 'Reading a DR', unit: S, help: 'Corner case and bad edges, for the last turn either way.' },
    { k: 'htr', label: 'Trying one route to HTR', unit: S },
    { k: 'tail', label: 'Writing out the finish a route gave', unit: S },
    { k: 'write', label: 'Writing the solution down and checking it', unit: S },
    { k: 'noise_sigma', label: 'Spread of one step\'s time', help: 'Log-normal spread of a step\'s real time around its nominal time (fixed per scramble and thing looked at).' },
    { k: 'attempt_sigma', label: 'Spread of the solver\'s pace', help: 'From one attempt to the next: a log-normal factor on every step. 0.15 gives the top 5\'s DNF rate.' },
  ],
  human: [
    { k: 'eo_see_lin', label: 'Chance to find an EO, moves on one side', arr: 'EO length', chance: true, help: 'When its axis is searched to that length.' },
    { k: 'eo_see_niss', label: 'Chance to find an EO with moves on both sides', arr: 'EO length', chance: true },
    { k: 'dr_see_glance', label: 'Chance to see the DR at the glance', arr: 'moves away', chance: true,
      help: 'From the EO\'s own state, when the DR is that many EO-keeping moves away.' },
    { k: 'dr_see_work', label: 'Chance to see the DR from a worked RZP state', arr: 'moves away', chance: true },
    { k: 'route_see', label: 'Chance to find a route\'s finish', chance: true, help: 'That a route which has a short finish is finished that well when it is tried.' },
    { k: 'read_sd', label: 'Reading error', unit: 'moves',
      help: 'How well the solver judges how far the DR is (DRM, pairs, ARM): the true distance plus a normal error with this spread. 1 is about the EO-switch cards; 0 is a solver who knows.' },
    { k: 'rzp_depth_weight', label: 'Depth weight of RZP states', help: 'RZP states are worked in the order of this × moves so far + their read.' },
    { k: 'form_sigma', label: 'Spread of the solver\'s form', help: 'Day to day: on a good day every miss is rarer and the reads sharper. 0 = the same solver every attempt.' },
  ],
  plan: [
    { h: 'EOs' },
    { k: 'eo_len', label: 'EO length searched', unit: 'moves', int: true, help: 'Look for EOs of up to this many moves on every axis.' },
    { k: 'eo_niss', label: 'Look for EOs with moves on both sides', bool: true },
    { k: 'eo_cap', label: 'Most EOs written down', int: true },
    { k: 't_eo', label: 'Stop collecting EOs at', unit: S },
    { k: 'eo_len_poor', label: 'Poor scramble: search EOs up to', unit: 'moves', int: true, help: 'If fewer than the number below were found (0 = off).' },
    { k: 'poor_n', label: '… when fewer EOs than this were found', int: true },
    { k: 'eager_eo', label: 'Take EOs this short straight to DR', unit: 'moves', int: true, help: '0 = off: EOs first, then DRs.' },
    { h: 'RZP and DR' },
    { k: 'rzp_per_eo', label: 'RZP states worked per EO', int: true, help: 'After the glance, most promising first (switches included).' },
    { k: 'rzp_short', label: '… for EOs of at most', unit: 'moves', int: true },
    { k: 'rzp_per_eo_long', label: 'RZP states worked per longer EO', int: true },
    { k: 'read_max', label: 'Work an RZP state only if EO + RZP + read is at most', unit: 'moves' },
    { k: 'rzp_more', label: 'More RZP states per EO on each extra pass', int: true, help: 'When nothing is left to look at: go over the EOs again with this many more each, and the read limit one higher.' },
    { k: 'rzp_depth', label: 'Most RZP moves', int: true },
    { k: 'switch_pen', label: 'Switch penalty', unit: 'moves', help: 'How much worse a state on the other side is ranked. 50 or more: never switch.' },
    { k: 'dr_cap', label: 'Longest DR written down', unit: 'moves', int: true },
    { k: 'dr_per_line', label: 'DRs taken per line', int: true, help: 'A line is one EO ending with one DR axis.' },
    { k: 'read_on_find', label: 'Read a DR\'s subset when writing it down', bool: true, help: 'Otherwise only when it is its turn to be finished.' },
    { k: 't_dr', label: 'Stop looking for DRs at', unit: S },
    { k: 't_dr_rich', label: '… or at this time with many EOs', unit: S, help: 'If at least the number below of EOs were written (0 = off).' },
    { k: 'rich_n', label: '… many EOs means at least', int: true },
    { k: 't_dr_late', label: '… or at this time with no good DR', unit: S, help: 'If no DR of at most the length below is on the page at the stop time (0 = off).' },
    { k: 'late_len', label: '… a good DR is at most', unit: 'moves', int: true },
    { k: 't_dr_backup', label: '… or at this time with a backup', unit: S, help: 'If a solution of at most the length below is written down (0 = off).' },
    { k: 'backup_len', label: '… a backup is at most', unit: 'moves', int: true },
    { k: 'dr_enough', label: 'Stop once this many short DRs are on the page', int: true, help: '0 = off.' },
    { k: 'dr_enough_len', label: '… short means at most', unit: 'moves', int: true },
    { h: 'Finishing' },
    { k: 'htr_per_dr', label: 'Routes to HTR tried per DR', int: true },
    { k: 'fin_min_p', label: 'Skip a DR whose chance to beat the best is below', chance: true, help: 'By subset, from the optimal-finish distribution.' },
    { k: 'fin_max', label: 'Most DRs taken to a finish', int: true },
    { k: 'eager_finish', label: 'Finish a DR at once if its expected total is at most', unit: 'moves', help: '0 = off.' },
    { k: 'eager_routes', label: '… with this many routes', int: true },
    { h: 'Safety' },
    { k: 'reserve', label: 'Time kept to write the solution down', unit: S },
    { k: 'reserve_rewrite', label: '… once a solution is on the sheet', unit: S, nullable: true, help: 'Empty = the same as above. A rewrite that runs over leaves the old solution standing.' },
    { k: 'backup_time', label: 'No solution yet at this time: finish the best DR', unit: S, help: '0 = off.' },
    { k: 'bank_first', label: 'Write the first solution down at once', bool: true },
    { k: 'bank_always', label: 'Write every improvement down at once', bool: true },
    { k: 'bank_at', label: 'Write a solution down at once if at most', unit: 'moves', int: true, help: '0 = off.' },
    { k: 'stop_at', label: 'Stop once a solution of at most this is written', unit: 'moves', int: true, help: '0 = off.' },
  ],
};

let defaults = null; // {settings, plans}
let settings = null; // the current settings
let preset = 'tuned';
let ready = false;
let runId = 0;
let report = null;

const $ = (id) => document.getElementById(id);
const clone = (x) => JSON.parse(JSON.stringify(x));
const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

function baseFor(group) {
  return group === 'plan' ? defaults.plans[preset === 'custom' ? 'tuned' : preset] : defaults.settings[group];
}

function buildForm() {
  for (const group of ['costs', 'human', 'plan']) {
    const box = document.querySelector(`.fields[data-group="${group}"]`);
    box.innerHTML = '';
    for (const f of SCHEMA[group]) {
      if (f.h) {
        const h = document.createElement('h3');
        h.textContent = f.h;
        box.appendChild(h);
        continue;
      }
      const div = document.createElement('div');
      div.className = 'f' + (f.arr ? ' wide' : '');
      div.dataset.key = f.k;
      const id = `${group}-${f.k}`;
      let html = `<label for="${id}${f.arr ? '-0' : ''}">${esc(f.label)}${f.unit ? ` <span class="help">(${esc(f.unit)})</span>` : ''}</label>`;
      const step = f.int ? '1' : f.chance ? '0.01' : 'any';
      if (f.arr) {
        html += '<div class="arr">';
        for (let i = 0; i < 8; i++) {
          html += `<div><span>${i}</span><input type="number" id="${id}-${i}" data-group="${group}" data-key="${f.k}" data-index="${i}" step="${step}" min="0"${f.chance ? ' max="1"' : ''}></div>`;
        }
        html += '</div>';
        html += `<span class="help">Index: ${esc(f.arr)}. ${esc(f.help || '')}</span>`;
      } else if (f.bool) {
        html = `<label><input type="checkbox" id="${id}" data-group="${group}" data-key="${f.k}"> ${esc(f.label)}</label>`;
        if (f.help) html += `<span class="help">${esc(f.help)}</span>`;
      } else {
        html += `<input type="number" id="${id}" data-group="${group}" data-key="${f.k}" step="${step}" min="0"${f.chance ? ' max="1"' : ''}${f.nullable ? ' placeholder="same"' : ''}>`;
        if (f.help) html += `<span class="help">${esc(f.help)}</span>`;
      }
      div.innerHTML = html;
      box.appendChild(div);
    }
  }
  document.querySelectorAll('.fields input').forEach((inp) => inp.addEventListener('input', onFieldInput));
}

function fillForm() {
  document.querySelectorAll('.fields input').forEach((inp) => {
    const { group, key, index } = inp.dataset;
    const v = settings[group][key];
    if (inp.type === 'checkbox') inp.checked = !!v;
    else if (index !== undefined) inp.value = v[+index];
    else inp.value = v === null || v === undefined ? '' : v;
  });
  $('preset').value = preset;
  markChanged();
}

function onFieldInput(ev) {
  const inp = ev.target;
  const { group, key, index } = inp.dataset;
  const f = SCHEMA[group].find((x) => x.k === key);
  let v;
  if (inp.type === 'checkbox') v = inp.checked;
  else if (inp.value === '' && f.nullable) v = null;
  else {
    v = Number(inp.value);
    if (inp.value === '' || !Number.isFinite(v)) return; // keep the last good value while typing
    if (f.int) v = Math.round(v);
  }
  if (index !== undefined) settings[group][key][+index] = v;
  else settings[group][key] = v;
  if (group === 'plan') {
    preset = same(settings.plan, defaults.plans.tuned) ? 'tuned' : same(settings.plan, defaults.plans.baseline) ? 'baseline' : 'custom';
    $('preset').value = preset;
  }
  markChanged();
  save();
}

function markChanged() {
  for (const group of ['costs', 'human', 'plan']) {
    const base = baseFor(group);
    document.querySelectorAll(`.fields[data-group="${group}"] .f[data-key]`).forEach((div) => {
      div.classList.toggle('changed', !same(settings[group][div.dataset.key], base[div.dataset.key]));
    });
  }
}

// ------------------------------------------------------------------------------------------------ keeping and sharing

const STORE_KEY = 'attempt-sim:v1';

function diff(cur, base) {
  const o = {};
  for (const k of Object.keys(cur)) if (!same(cur[k], base[k])) o[k] = cur[k];
  return o;
}

function snapshot() {
  return {
    s: $('scramble').value.trim(),
    a: Number($('attempt').value) || 0,
    p: preset,
    o: { costs: diff(settings.costs, defaults.settings.costs), human: diff(settings.human, defaults.settings.human), plan: diff(settings.plan, baseFor('plan')) },
  };
}

function restore(snap) {
  if (!snap) return;
  if (typeof snap.s === 'string') $('scramble').value = snap.s;
  if (Number.isFinite(snap.a)) $('attempt').value = snap.a;
  preset = ['tuned', 'baseline', 'custom'].includes(snap.p) ? snap.p : 'tuned';
  settings = clone(defaults.settings);
  settings.plan = clone(baseFor('plan'));
  const o = snap.o || {};
  for (const group of ['costs', 'human', 'plan']) {
    for (const [k, v] of Object.entries(o[group] || {})) {
      if (k in settings[group] && typeof v === typeof settings[group][k] || (k === 'reserve_rewrite')) settings[group][k] = v;
    }
  }
}

function save() {
  try {
    localStorage.setItem(STORE_KEY, JSON.stringify(snapshot()));
  } catch {
    // storage blocked: nothing kept between visits
  }
}

function loadSaved() {
  if (location.hash.length > 1) {
    try {
      return JSON.parse(decodeURIComponent(location.hash.slice(1)));
    } catch {
      // not ours
    }
  }
  try {
    return JSON.parse(localStorage.getItem(STORE_KEY));
  } catch {
    return null;
  }
}

// ------------------------------------------------------------------------------------------------ the worker

const worker = new Worker(new URL('./worker.js', import.meta.url), { type: 'module' });
const statusBox = $('status');

function setStatus(text, progress) {
  statusBox.querySelector('.status-text').textContent = text;
  if (progress !== undefined) statusBox.querySelector('.fill').style.width = `${Math.round(progress * 100)}%`;
}

worker.onmessage = (ev) => {
  const m = ev.data;
  if (m.type === 'defaults') {
    defaults = m.defaults;
    buildForm();
    restore(loadSaved() || { p: 'tuned' });
    fillForm();
  } else if (m.type === 'progress') {
    setStatus(m.loading ? 'Loading the finish table kept from your last visit…'
      : `Building the finish table (once; the browser keeps it for next time): ${Math.round(m.value * 100)}%`, m.value);
  } else if (m.type === 'ready') {
    ready = true;
    statusBox.classList.add('done');
    setStatus('Ready.');
    $('run').disabled = false;
    if ($('scramble').value.trim()) run();
  } else if (m.type === 'fatal') {
    setStatus(`The simulator could not start in this browser: ${m.message}`);
  } else if (m.type === 'result' && m.id === runId) {
    $('run').disabled = false;
    setStatus(`Done: the attempt took ${(m.ms / 1000).toFixed(2)} s to simulate.`);
    report = m.report;
    render();
  } else if (m.type === 'error' && m.id === runId) {
    $('run').disabled = false;
    showError(m.message);
    setStatus('Ready.');
  }
};
worker.postMessage({ type: 'init' });

function showError(msg) {
  const e = $('error');
  e.textContent = msg;
  e.hidden = !msg;
}

function run() {
  if (!ready) return;
  const scramble = $('scramble').value.trim();
  if (!scramble) {
    showError('Type a scramble first (or take a random one).');
    return;
  }
  showError('');
  settings.attempt = Math.max(0, Math.round(Number($('attempt').value) || 0));
  settings.seed = 1;
  save();
  runId += 1;
  $('run').disabled = true;
  setStatus('Running the attempt…');
  worker.postMessage({ type: 'simulate', id: runId, request: { scramble, settings } });
}

// ------------------------------------------------------------------------------------------------ showing the attempt

function clock(ms) {
  const s = Math.floor(ms / 1000);
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
}
function secs(ms) {
  return ms >= 10000 ? `${Math.round(ms / 1000)} s` : `${(ms / 1000).toFixed(1)} s`;
}
const code = (m) => `<code>${esc(m)}</code>`;
const co = '<span class="co">computer only</span>';
const plural = (n, w) => `${n} ${w}${n === 1 ? '' : 's'}`;
const eoName = (eo) => `EO ${eo.number} ${code(eo.text)}`;
const drName = (dr) => `DR ${dr.number} ${code(dr.text)}`;

// the RZP moves of a state: on the EO's side, then (after a switch) on the other side
function rzpMoves(n) {
  const first = n.moves ? code(n.moves) : '';
  if (!n.switched) return first || 'the EO as it is';
  return `${first ? `${first}, then ` : ''}switch, then ${n.moves_after_switch ? code(n.moves_after_switch) : 'nothing'}`;
}

function describe(s) {
  switch (s.type) {
    case 'look':
      return `Counted the bad edges: R/L ${s.bad_edges[0]}, U/D ${s.bad_edges[1]}, F/B ${s.bad_edges[2]}.`;
    case 'eo_scan': {
      const where = s.niss ? 'normal, inverse and NISS' : 'normal and inverse';
      const found = s.spotted.length ? `spotted ${s.spotted.map(code).join(', ')}` : 'nothing new';
      return `Searched ${s.axis} for EOs of ${plural(s.length, 'move')} (${where}): ${found}.`;
    }
    case 'eo_write':
      return `Wrote down ${eoName(s.eo)}: ${s.eo.axis}, ${plural(s.eo.len, 'move')}${s.eo.kind === 'NISS' ? ', NISS' : s.eo.kind === 'inverse' ? ', on inverse' : ''}.`;
    case 'eo_glance': {
      const best = s.lines.filter((l) => Number.isFinite(l.read_total)).reduce((a, l) => (a && a.read_total <= l.read_total ? a : l), null);
      const drms = [...new Set(s.lines.map((l) => `${l.dr_axis} ${l.drm}`))].join(', ');
      return `Glanced at ${eoName(s.eo)}: ${drms}${best ? `; best read: a DR of about ${best.read_total.toFixed(1)} in all, on ${best.dr_axis}` : ''}.`;
    }
    case 'rzp':
      return `RZP on ${eoName(s.eo)} for DR on ${s.dr_axis}: ${rzpMoves(s.node)} (${s.node.drm}); reads as a DR of about ${s.node.read_total.toFixed(1)} in all.`;
    case 'switch':
      return `Switched ${eoName(s.eo)} to the other side for DR on ${s.dr_axis}, ${s.node.moves ? `after ${code(s.node.moves)}` : 'right after the EO'} (${s.node.drm}); reads as a DR of about ${s.node.read_total.toFixed(1)} in all.`;
    case 'dr_find':
      if (s.outcome === 'the same DR again') return `Saw ${drName(s.dr)} again: it is already on the page.`;
      return `Wrote down ${drName(s.dr)}: ${plural(s.dr.len, 'move')}, DR on ${s.dr.axis}, from EO ${s.eo.number}${s.outcome !== 'new' ? ' (a shorter way to a DR already found)' : ''}.`;
    case 'dr_read':
      return `Read DR ${s.dr.number}: ${s.subsets.length > 1 ? `${s.subsets[0]}, or ${s.subsets[1]} with the last turn the other way` : s.subsets[0]}.`;
    case 'htr': {
      const a = s.attempt;
      const res = a.finish_len !== null && a.finish_len !== undefined
        ? `a finish of ${a.finish_len} → ${a.total} in all`
        : a.missed ? 'missed the finish it had' : 'nothing within two moves of the optimum';
      return `Tried route ${code(a.route)} on DR ${s.dr.number} (${a.subset}): ${res}.`;
    }
    case 'tail':
      return `Wrote out the finish: a solution of ${s.len}${s.best_so_far ? ', the best so far' : ', no better than the best'}.`;
    case 'write':
      return `Wrote the solution down and checked it: ${s.len} moves${s.in_time ? '' : '. This ran past the end of the attempt: it doesn\'t count'}.`;
    default:
      return s.type;
  }
}

function details(s) {
  switch (s.type) {
    case 'eo_glance':
      return `<div class="tablewrap"><table><tr><th>Ending</th><th>DR axis</th><th>DRM</th><th>Read: DR in all</th><th>True distance to DR ${co}</th></tr>${s.lines
        .map((l) => `<tr><td>${code(l.ending)}</td><td>${l.dr_axis}</td><td>${l.drm}</td><td>${Number.isFinite(l.read_total) ? l.read_total.toFixed(1) : '–'}</td><td>${l.true_distance}</td></tr>`)
        .join('')}</table></div>`;
    case 'rzp':
    case 'switch':
      return `EO ${code(s.eo.text)} (it ends on ${s.side}). RZP moves after it: ${rzpMoves(s.node)}. DRM ${s.node.drm}. The read says a DR of ${s.node.read_total.toFixed(2)} in all; the DR is really ${plural(s.node.true_distance, 'move')} away ${co}.`;
    case 'dr_find':
      return `${code(s.dr.text)}: ${plural(s.dr.len, 'move')} from ${eoName(s.eo)}; seen ${plural(s.seen_from, 'move')} away after ${plural(s.rzp_moves, 'RZP move')}${s.switched ? ', on the other side' : ''}.`;
    case 'htr': {
      const a = s.attempt;
      return `Route ${code(a.route)} on the ending in ${a.subset}. ${a.finish ? `Finish: ${code(a.finish)}.` : ''} The DR's optimal finish is ${a.optimal} ${co}.`;
    }
    case 'tail':
      return code(s.solution);
    case 'write':
      return code(s.solution);
    case 'eo_scan':
      return s.spotted.length ? s.spotted.map(code).join(' · ') : 'No EO of that length was spotted on this axis.';
    default:
      return '';
  }
}

function isKey(s) {
  return (s.type === 'dr_find' && s.outcome !== 'the same DR again') || s.type === 'tail' || s.type === 'write';
}

function render() {
  const r = report;
  const o = r.outcome;
  $('results').hidden = false;
  // the result
  const res = $('result-card');
  const written = r.solutions.filter((x) => x.written_at !== null && x.written_at !== undefined);
  const final = o.len > 0 ? written.find((x) => x.moves === o.moves.join(' ') && x.len === o.len) : null;
  let html;
  if (o.len > 0) {
    html = `<div class="headline">${o.len} moves</div><div class="moves">${esc(o.moves.join(' '))}</div>`;
  } else {
    html = `<div class="headline dnf">DNF</div><div>${o.best_found ? `Found a ${o.best_found} but didn't get it written down in time.` : 'No full solution was found.'}</div>`;
  }
  html += '<div class="facts">';
  if (final) html += `<span>Finish found at <b>${clock(final.found_at)}</b>, written down at <b>${clock(final.written_at)}</b></span>`;
  html += `<span>Attempt ended at <b>${clock(o.t_end)}</b> of ${clock(o.budget_ms)}</span>`;
  const n = (k, w) => `<b>${k}</b> ${w}${k === 1 ? '' : 's'}`;
  html += `<span>${n(o.eos_found, 'EO')} written</span><span>${n(o.drs_found, 'DR')} written${o.best_dr ? `, best <b>${o.best_dr}</b>` : ''}</span>`;
  html += `<span>${n(o.drs_finished, 'DR')} taken to a finish</span><span>${n(r.solutions.length, 'solution')} found</span>`;
  if (o.oracle_page) html += `<span>Best DR + optimal finish on the page: <b>${o.oracle_page}</b> ${co}</span>`;
  html += '</div>';
  if (final) {
    html += `<div class="skeleton">
      <span class="k">EO</span><span>${code(final.eo)} (${plural(final.eo_len, 'move')})</span>
      <span class="k">DR</span><span>${code(final.dr_normal || '–')} on normal, ${code(final.dr_inverse || '–')} on inverse (${final.dr_len} in all, DR on ${final.dr_axis})</span>
      <span class="k">Subset</span><span>${esc(final.subset)}</span>
      <span class="k">Finish</span><span>${code(final.finish)} (${final.finish_len}) by the route ${code(final.route)}; the optimal finish is ${final.optimal_finish} ${co}</span>
      <span class="k">Solution</span><span>DR on normal + finish + the inverse of the DR's inverse moves, cancelled: ${o.len}</span>
    </div>`;
  }
  res.innerHTML = html;

  // every solution
  const t = $('solutions');
  if (!r.solutions.length) {
    t.innerHTML = '<tr><td>No full solution was found in this attempt.</td></tr>';
  } else {
    t.innerHTML = `<tr><th class="num">Found at</th><th class="num">Moves</th><th class="num">Written down</th><th class="num">DR</th><th>Subset</th><th>Route</th><th class="num">Finish</th><th class="num">Optimal finish ${co}</th><th>Solution</th></tr>${r.solutions
      .map((x) => {
        const isFinal = final && x === final;
        return `<tr class="${isFinal ? 'result' : ''}"><td class="num">${clock(x.found_at)}</td><td class="num">${x.len}</td><td class="num">${x.written_at !== null && x.written_at !== undefined ? clock(x.written_at) : '–'}</td><td class="num">${x.dr_len}</td><td>${esc(x.subset)}</td><td>${code(x.route)}</td><td class="num">${x.finish_len}</td><td class="num">${x.optimal_finish}</td><td class="moves-cell"><details><summary>show</summary>${code(x.moves)}<br>EO ${code(x.eo)} · DR ${code(x.dr_normal || '–')} (${code(x.dr_inverse || '–')}) · finish ${code(x.finish)}</details></td></tr>`;
      })
      .join('')}`;
  }

  renderHour();
  renderTimeline();
}

function renderHour() {
  const r = report;
  const o = r.outcome;
  const total = Math.max(o.budget_ms, o.t_end);
  const bar = $('hour-bar');
  let html = '';
  for (const s of r.steps) {
    const left = (100 * s.start) / total;
    const width = Math.max((100 * s.ms) / total, 0.08);
    html += `<div class="seg" style="left:${left}%;width:${width}%;background:var(--k-${s.kind})"></div>`;
  }
  if (o.t_end < o.budget_ms) html += `<div class="end" style="left:${(100 * o.t_end) / total}%" title="unused"></div>`;
  for (const w of o.writes) html += `<div class="mark" style="left:${(100 * w[0]) / total}%" title="${w[1]} written down at ${clock(w[0])}"></div>`;
  bar.innerHTML = html;
  bar.onclick = (ev) => {
    const rect = bar.getBoundingClientRect();
    jumpTo(((ev.clientX - rect.left) / rect.width) * total);
  };
  const axis = $('hour-axis');
  const stepMin = total > 2 * 3600000 ? 20 : total > 3600000 ? 10 : 5;
  let ticks = '';
  for (let m = 0; m * 60000 <= total; m += stepMin) ticks += `<span style="left:${(100 * m * 60000) / total}%">${m}</span>`;
  axis.innerHTML = ticks;
  $('legend').innerHTML = KINDS.map((k, i) => (o.count[i] ? `<span><i class="sw" style="background:var(--k-${k})"></i>${KIND_LABEL[k]}: ${(o.time[i] / 60000).toFixed(1)} min (${o.count[i]})</span>` : ''))
    .join('') + '<span>Minutes on the axis; black lines: solution written down</span>';
}

function renderTimeline() {
  const list = $('timeline');
  const r = report;
  let html = '';
  let nextMinute = 5;
  r.steps.forEach((s, i) => {
    while (s.start >= nextMinute * 60000) {
      html += `<li class="minute" data-minute="${nextMinute}">${nextMinute} minutes</li>`;
      nextMinute += 5;
    }
    html += `<li data-i="${i}" data-kind="${s.kind}" class="${isKey(s) ? 'key' : ''}">
      <span class="t">${clock(s.start)}</span><span class="dur">${secs(s.ms)}</span>
      <span class="kind"><i class="sw" style="background:var(--k-${s.kind})"></i>${KIND_LABEL[s.kind]}</span>
      <span class="what">${describe(s)}</span>
      <div class="more">${details(s)}</div></li>`;
  });
  list.innerHTML = html;
  list.onclick = (ev) => {
    const li = ev.target.closest('li[data-i]');
    if (li && !ev.target.closest('.more')) li.classList.toggle('open');
  };
  // filters
  const chips = $('kind-filters');
  chips.innerHTML = KINDS.filter((k, i) => r.outcome.count[i]).map((k) => `<label><input type="checkbox" data-kind="${k}" checked><i class="sw" style="background:var(--k-${k})"></i>${KIND_LABEL[k]}</label>`).join('');
  chips.onchange = applyFilters;
  $('key-only').onchange = applyFilters;
  applyFilters();
}

function applyFilters() {
  const shown = new Set([...document.querySelectorAll('#kind-filters input:checked')].map((x) => x.dataset.kind));
  const keyOnly = $('key-only').checked;
  document.querySelectorAll('#timeline li[data-i]').forEach((li) => {
    const s = report.steps[+li.dataset.i];
    li.hidden = !shown.has(s.kind) || (keyOnly && !isKey(s));
  });
}

function jumpTo(ms) {
  const steps = report.steps;
  let i = steps.findIndex((s) => s.start + s.ms > ms);
  if (i < 0) i = steps.length - 1;
  const li = document.querySelector(`#timeline li[data-i="${i}"]`);
  if (!li) return;
  if (li.hidden) {
    $('key-only').checked = false;
    document.querySelectorAll('#kind-filters input').forEach((x) => (x.checked = true));
    applyFilters();
  }
  li.scrollIntoView({ block: 'center', behavior: 'smooth' });
  li.classList.remove('flash');
  void li.offsetWidth;
  li.classList.add('flash');
}

// ------------------------------------------------------------------------------------------------ the controls

let scrambles = null;

$('run-form').addEventListener('submit', (ev) => {
  ev.preventDefault();
  run();
});
$('random-scramble').addEventListener('click', async () => {
  try {
    if (!scrambles) {
      const text = await (await fetch('scrambles.txt')).text();
      scrambles = text.split('\n').filter((l) => l && !l.startsWith('#')).map((l) => l.split('\t'));
    }
    const [k, scr] = scrambles[Math.floor(Math.random() * scrambles.length)];
    $('scramble').value = scr;
    $('attempt').value = k;
    save();
    run();
  } catch (e) {
    showError(`Could not load the scramble list: ${e.message}`);
  }
});
$('next-attempt').addEventListener('click', () => {
  $('attempt').value = (Number($('attempt').value) || 0) + 1;
  run();
});
$('attempt').addEventListener('change', save);
$('scramble').addEventListener('change', save);
$('preset').addEventListener('change', () => {
  preset = $('preset').value;
  if (preset !== 'custom') settings.plan = clone(defaults.plans[preset]);
  fillForm();
  save();
});
$('reset').addEventListener('click', () => {
  preset = 'tuned';
  settings = clone(defaults.settings);
  settings.plan = clone(defaults.plans.tuned);
  fillForm();
  save();
});
$('copy-link').addEventListener('click', async () => {
  const url = `${location.origin}${location.pathname}#${encodeURIComponent(JSON.stringify(snapshot()))}`;
  try {
    await navigator.clipboard.writeText(url);
    $('copied').hidden = false;
    setTimeout(() => ($('copied').hidden = true), 1500);
  } catch {
    history.replaceState(null, '', url);
  }
});
