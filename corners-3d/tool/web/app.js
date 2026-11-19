// The lookup page: reads a scramble, shows what the write-up's reads say about it.
import { PLACES, SHOW, KIND_NAME, MOVES, N, buildTables, stateOfScramble, fromIndex, read } from "./corners.js";
import { COUNT } from "./count.js";

const $ = (id) => document.getElementById(id);
let T = null;

function li(html) { const e = document.createElement("li"); e.innerHTML = html; return e; }
function row(cells) {
  const tr = document.createElement("tr");
  for (const c of cells) { const td = document.createElement("td"); td.innerHTML = c; tr.appendChild(td); }
  return tr;
}
const plural = (n, word) => `${n} ${word}${n === 1 ? "" : "s"}`;

function show(state, turned) {
  const r = read(state, T, COUNT);
  $("turned").hidden = !turned;
  $("line").textContent = r.line;
  const body = $("corners").tBodies[0];
  body.replaceChildren(...SHOW.map((p) => row([PLACES[p], PLACES[state.perm[p]], KIND_NAME[r.kinds[p]]])));

  const outText = `${r.out[0]} with R/L oriented, ${r.out[1]} with U/D, ${r.out[2]} with F/B`;
  $("reads").replaceChildren(
    li(`<strong>${plural(r.twisted, "twisted corner")}</strong>, <strong>${plural(r.out[0] + r.out[1] + r.out[2], "out corner")}</strong> (${outText}). Weight ${r.weight}. <em>At a glance.</em>`),
    li(`Out corners: <strong>${r.shape}</strong>. D-colour corners: <strong>${r.dPicture}</strong>. <em>At a glance.</em>`),
    li(`Parity: <strong>${r.parity}</strong>, so the number of quarter turns into HTR is ${r.parity}. <em>Tracing.</em>`),
  );

  const c = r.countRow;
  $("floors").tBodies[0].replaceChildren(
    row(["weight / 4", "", Math.ceil(r.weight / 4), "at a glance"]),
    row(["count table", `${c.moves} (${c.niss} with NISS)`, c.quarter, "at a glance"]),
    row(["types (distance to all good)", r.typesFloor, "", "a search, or this page"]),
    row(["types + parity", r.parityFloor, "", "a search, or this page"]),
  );

  const ends = r.goodWayEnds === 0 ? "real HTR" : `a fake HTR, ${r.goodWayEnds} moves from HTR`;
  const items = [
    li(`<strong>${plural(r.d, "move")}</strong> to HTR on one side, <strong>${plural(r.q, "quarter turn")}</strong> at least.`),
  ];
  if (r.d > 0) {
    items.push(li(`Turns that get closer: <strong>${r.closer.join(", ")}</strong> (${r.closer.length} of 9).`));
    items.push(li(`A shortest way: <code>${r.solution}</code>`));
  }
  if (r.typesFloor > 0) items.push(li(`A shortest way to all good: <code>${r.goodWay}</code>. It ends in ${ends}.`));
  else if (r.d > 0) items.push(li(`Every corner is good and it isn't HTR: a fake HTR.`));
  $("answer").replaceChildren(...items);
  $("result").hidden = false;
}

function lookUp() {
  $("error").hidden = true;
  try {
    const { state, turned } = stateOfScramble($("scramble").value);
    show(state, turned);
    history.replaceState(null, "", "#" + encodeURIComponent($("scramble").value.trim()));
  } catch (e) {
    $("error").textContent = e.message;
    $("error").hidden = false;
    $("result").hidden = true;
  }
}

// A uniformly random state, written as a scramble: solve it into HTR, undo that, and put in front the half turns
// that make the HTR state it ended on.
function randomScramble() {
  const s = Math.floor(Math.random() * N);
  let x = s; const back = [];
  while (T.d[x] > 0) { let m = 0; while (T.d[T.next(x, m)] >= T.d[x]) m++; back.push(m); x = T.next(x, m); }
  // x is an HTR state: the half turns that make it from solved (at most 4)
  const seen = new Map([[0, []]]); const queue = [0];
  while (!seen.has(x)) {
    const y = queue.shift();
    for (const m of [1, 4, 7]) { const z = T.next(y, m); if (!seen.has(z)) { seen.set(z, [...seen.get(y), m]); queue.push(z); } }
  }
  const inverse = (m) => m - (m % 3) + 2 - (m % 3);
  const seq = [...seen.get(x), ...back.reverse().map(inverse)];
  return { state: fromIndex(s), text: seq.map((m) => MOVES[m]).join(" ") };
}

$("form").addEventListener("submit", (e) => { e.preventDefault(); if (T) lookUp(); });
$("random").addEventListener("click", () => {
  const { text } = randomScramble();
  $("scramble").value = text;
  lookUp();
});

setTimeout(() => {
  T = buildTables();
  $("status").classList.add("done");
  $("go").disabled = false;
  $("random").disabled = false;
  if (location.hash.length > 1) $("scramble").value = decodeURIComponent(location.hash.slice(1));
  lookUp();
}, 30);
