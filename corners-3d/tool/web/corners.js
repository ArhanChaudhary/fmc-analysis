// Corners with DBL held and R, U, F turns: the model and the tables of the study, built in the browser.
// A corner place is (x, y, z) with x = +1 on R, y = +1 on U, z = +1 on F.  A face turn is a rotation of space; the
// place map and the twist it applies are worked out from the rotation, as in the study's Rust crate.

export const PLACES = ["UFR", "UFL", "UBR", "DFR", "UBL", "DFL", "DBR"];
export const XYZ = [[1, 1, 1], [-1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, -1], [-1, -1, 1], [1, -1, -1]];
export const MOVES = ["R", "R2", "R'", "U", "U2", "U'", "F", "F2", "F'"];
export const SHOW = [0, 1, 4, 2, 3, 5, 6]; // UFR UFL UBL UBR DFR DFL DBR
export const LETTER = [".", "+", "-", "r", "u", "f"];
export const KIND_NAME = ["good", "twisted clockwise", "twisted counter-clockwise", "out, only R/L oriented",
  "out, only U/D oriented", "out, only F/B oriented"];
export const N = 5040 * 729;

const tetrad = (v) => v[0] * v[1] * v[2] < 0;
const TET = XYZ.map(tetrad);
// clockwise seen from the + side of the axis: R: UFR -> UBR.  U: UFR -> UFL.  F: UFR -> DFR.
const rot = (axis, v) => (axis === 0 ? [v[0], v[2], -v[1]] : axis === 1 ? [-v[2], v[1], v[0]] : [v[1], -v[0], v[2]]);
const rotFacing = (axis, f) => (f === axis ? f : 3 - axis - f);
// the faces round a place clockwise from the U/D face
const clockwise = (v) => (tetrad(v) ? [1, 2, 0] : [1, 0, 2]);
const placeIndex = (v) => XYZ.findIndex((w) => w[0] === v[0] && w[1] === v[1] && w[2] === v[2]);

// for each quarter turn (R, U, F): where each place goes and the new twist for each old one
const QUARTER = [0, 1, 2].map((axis) => {
  const to = [], twist = [];
  for (let p = 0; p < 7; p++) {
    if (XYZ[p][axis] < 0) { to.push(p); twist.push([0, 1, 2]); continue; }
    const q = placeIndex(rot(axis, XYZ[p]));
    to.push(q);
    twist.push([0, 1, 2].map((o) => clockwise(XYZ[q]).indexOf(rotFacing(axis, clockwise(XYZ[p])[o]))));
  }
  return { to, twist };
});

export function applyMove(state, m) {
  let { perm, ori } = state;
  const q = QUARTER[Math.floor(m / 3)];
  for (let k = 0; k <= m % 3; k++) {
    const np = new Array(7), no = new Array(7);
    for (let p = 0; p < 7; p++) { np[q.to[p]] = perm[p]; no[q.to[p]] = q.twist[p][ori[p]]; }
    perm = np; ori = no;
  }
  return { perm, ori };
}

export const solved = () => ({ perm: [0, 1, 2, 3, 4, 5, 6], ori: [0, 0, 0, 0, 0, 0, 0] });

function permRank(perm) {
  let rank = 0;
  for (let i = 0; i < 7; i++) {
    let smaller = 0;
    for (let j = i + 1; j < 7; j++) if (perm[j] < perm[i]) smaller++;
    rank = rank * (7 - i) + smaller;
  }
  return rank;
}
function permUnrank(rank) {
  const digits = new Array(7);
  for (let i = 6; i >= 0; i--) { digits[i] = rank % (7 - i); rank = Math.floor(rank / (7 - i)); }
  const left = [0, 1, 2, 3, 4, 5, 6], perm = [];
  for (let i = 0; i < 7; i++) perm.push(left.splice(digits[i], 1)[0]);
  return perm;
}
const twistRank = (ori) => ori.slice(0, 6).reduce((a, o) => a * 3 + o, 0);
function twistUnrank(t) {
  const ori = new Array(7); let sum = 0;
  for (let i = 5; i >= 0; i--) { ori[i] = t % 3; sum += ori[i]; t = Math.floor(t / 3); }
  ori[6] = (3 - (sum % 3)) % 3;
  return ori;
}
export const index = (s) => permRank(s.perm) * 729 + twistRank(s.ori);
export const fromIndex = (i) => ({ perm: permUnrank(Math.floor(i / 729)), ori: twistUnrank(i % 729) });

export function kind(state, p) {
  const home = state.perm[p], o = state.ori[p];
  if (TET[p] === TET[home]) return o; // 0 good, 1 twisted cw, 2 twisted ccw
  const f = clockwise(XYZ[p])[o]; // the axis the U/D sticker faces
  return f === 1 ? 4 : f === 0 ? 5 : 3;
}
export const kinds = (state) => [0, 1, 2, 3, 4, 5, 6].map((p) => kind(state, p));
export const kindsLine = (state) => SHOW.map((p) => LETTER[kind(state, p)]).join(" ");
export function parity(state) {
  let inv = 0;
  for (let i = 0; i < 7; i++) for (let j = i + 1; j < 7; j++) if (state.perm[i] > state.perm[j]) inv++;
  return inv % 2;
}

// ---------- tables ----------

export function buildTables(progress = () => {}) {
  const T = {};
  // turn tables on the two coordinates
  const pm = [], tm = [];
  for (let m = 0; m < 9; m++) {
    const a = new Uint16Array(5040), b = new Uint16Array(729);
    for (let i = 0; i < 5040; i++) a[i] = permRank(applyMove({ perm: permUnrank(i), ori: [0, 0, 0, 0, 0, 0, 0] }, m).perm);
    for (let i = 0; i < 729; i++) b[i] = twistRank(applyMove({ perm: [0, 1, 2, 3, 4, 5, 6], ori: twistUnrank(i) }, m).ori);
    pm.push(a); tm.push(b);
  }
  T.next = (s, m) => pm[m][(s / 729) | 0] * 729 + tm[m][s % 729];
  progress("turn tables");

  const bfs = (sources) => {
    const dist = new Int8Array(N).fill(-1);
    let frontier = new Uint32Array(sources);
    for (const s of sources) dist[s] = 0;
    let level = 0;
    while (frontier.length) {
      const nextF = [];
      for (let k = 0; k < frontier.length; k++) {
        const s = frontier[k], pr = (s / 729) | 0, tr = s % 729;
        for (let m = 0; m < 9; m++) {
          const t = pm[m][pr] * 729 + tm[m][tr];
          if (dist[t] < 0) { dist[t] = level + 1; nextF.push(t); }
        }
      }
      frontier = Uint32Array.from(nextF);
      level++;
    }
    return dist;
  };

  // HTR: what half turns reach
  const htr = new Set([0]);
  const stack = [0];
  while (stack.length) {
    const s = stack.pop();
    for (const m of [1, 4, 7]) { const t = T.next(s, m); if (!htr.has(t)) { htr.add(t); stack.push(t); } }
  }
  T.htr = htr;
  T.d = bfs([...htr]);
  progress("moves to HTR");

  // all good: twists 0 and every corner in its tetrad
  const good = [], goodEven = [];
  for (let pr = 0; pr < 5040; pr++) {
    const perm = permUnrank(pr);
    if (perm.every((h, p) => TET[h] === TET[p])) {
      good.push(pr * 729);
      if (parity({ perm }) === 0) goodEven.push(pr * 729);
    }
  }
  T.dg = bfs(good);
  T.de = bfs(goodEven);
  progress("the floors");

  // quarter turns with half turns free: close each level under half turns, then step out with quarter turns
  const q = new Int8Array(N).fill(-1);
  let level = [...htr];
  for (const s of level) q[s] = 0;
  for (let k = 0; level.length; k++) {
    const nextL = [];
    for (let i = 0; i < level.length; i++) {
      const s = level[i];
      for (const m of [1, 4, 7]) { const t = T.next(s, m); if (q[t] < 0) { q[t] = k; level.push(t); } }
    }
    for (let i = 0; i < level.length; i++) {
      const s = level[i];
      for (const m of [0, 2, 3, 5, 6, 8]) { const t = T.next(s, m); if (q[t] < 0) { q[t] = k + 1; nextL.push(t); } }
    }
    level = nextL;
  }
  T.q = q;
  progress("quarter turns");

  // the six pictures of the D-colour corners that HTR shows
  T.six = new Set([...htr].map((s) => dPicture(fromIndex(s))));
  return T;
}

// which places hold a corner with the D colour (home y = -1), as 7 bits
export function dPicture(state) {
  let bits = 0;
  for (let p = 0; p < 7; p++) if (XYZ[state.perm[p]][1] < 0) bits |= 1 << p;
  return bits;
}
export function dPictureName(state, T) {
  const bits = dPicture(state);
  let inA = 1; // DBL
  for (let p = 0; p < 7; p++) if ((bits >> p) & 1 && TET[p]) inA++;
  return inA === 4 ? "4d" : inA === 2 ? (T.six.has(bits) ? "4a" : "4b") : "4c";
}

// the shape of the out corners: 0c, 2c, 4a, 4b, 6c.  Four out corners are 4a when half turns can carry them onto
// 6 different sets of places, 4b when onto 12.
const HALF_PLACE = [0, 1, 2].map((axis) => QUARTER[axis].to.map((p) => QUARTER[axis].to[p]));
export function outShape(state) {
  let mask = 0;
  for (let p = 0; p < 7; p++) if (kind(state, p) >= 3) mask |= 1 << p;
  const n = mask.toString(2).split("1").length - 1;
  if (n !== 4) return n + "c";
  const seen = new Set([mask]), stack = [mask];
  while (stack.length) {
    const m = stack.pop();
    for (const h of HALF_PLACE) {
      let t = 0;
      for (let p = 0; p < 7; p++) if ((m >> p) & 1) t |= 1 << h[p];
      if (!seen.has(t)) { seen.add(t); stack.push(t); }
    }
  }
  return seen.size === 6 ? "4a" : "4b";
}

// ---------- scrambles ----------

// R, U, F sequences directly; anything with L, D or B (or rotations) goes through all eight corners.
const FACE = { R: [0, 1], L: [0, -1], U: [1, 1], D: [1, -1], F: [2, 1], B: [2, -1] };
const ALL8 = [];
for (const x of [1, -1]) for (const y of [1, -1]) for (const z of [1, -1]) ALL8.push([x, y, z]);
// a quarter turn of the face on the `sign` side of `axis`, clockwise seen from outside that face
function rotSigned(axis, v, sign) {
  let w = rot(axis, v);
  if (sign < 0) { w = rot(axis, rot(axis, w)); }
  return w;
}

export function parseScramble(text) {
  const tokens = text.replace(/[’‘`]/g, "'").replace(/[()]/g, " ").trim().split(/\s+/).filter(Boolean);
  const out = [];
  for (const t of tokens) {
    const m = /^([RLUDFBxyz])(2|'|2'|)$/.exec(t);
    if (!m) throw new Error(`I can't read "${t}" as a turn`);
    out.push([m[1], m[2] === "" ? 1 : m[2] === "'" ? 3 : 2]);
  }
  return out;
}

// The state a scramble makes, in the frame where the DBL corner is home.  Returns the state and whether the
// cube had to be turned as a whole to put DBL home.
export function stateOfScramble(text) {
  const turns = parseScramble(text);
  // every piece: where it is and where its three stickers face
  let pieces = ALL8.map((v) => ({ home: v, at: v, facing: [[v[0], 0, 0], [0, v[1], 0], [0, 0, v[2]]] }));
  const spin = (axis, sign, layer) => {
    pieces = pieces.map((pc) => (layer(pc.at) ? { home: pc.home, at: rotSigned(axis, pc.at, sign), facing: pc.facing.map((f) => rotSigned(axis, f, sign)) } : pc));
  };
  for (const [name, times] of turns) {
    for (let k = 0; k < times; k++) {
      if ("xyz".includes(name)) spin("xyz".indexOf(name), 1, () => true);
      else { const [axis, sign] = FACE[name]; spin(axis, sign, (v) => v[axis] === sign); }
    }
  }
  // turn the whole cube so that the DBL piece is home: try the 24 rotations
  const dbl = pieces.find((pc) => pc.home.every((c) => c === -1));
  const turned = !(dbl.at.every((c) => c === -1) && dbl.facing[0][0] === -1 && dbl.facing[1][1] === -1);
  if (turned) {
    const seqs = [[]];
    const seen = new Set();
    let found = null;
    while (seqs.length && !found) {
      const seq = seqs.shift();
      let at = dbl.at, facing = dbl.facing;
      for (const a of seq) { at = rot(a, at); facing = facing.map((f) => rot(a, f)); }
      const key = at.join() + "|" + facing.map((f) => f.join()).join("|");
      if (seen.has(key)) continue;
      seen.add(key);
      if (at.every((c) => c === -1) && facing[0][0] === -1 && facing[1][1] === -1 && facing[2][2] === -1) { found = seq; break; }
      for (const a of [0, 1, 2]) seqs.push([...seq, a]);
    }
    for (const a of found) spin(a, 1, () => true);
  }
  const state = { perm: new Array(7), ori: new Array(7) };
  for (const pc of pieces) {
    const p = placeIndex(pc.at);
    if (p < 0) continue; // DBL
    state.perm[p] = placeIndex(pc.home);
    const udAxis = pc.facing[1].findIndex((c) => c !== 0);
    state.ori[p] = clockwise(pc.at).indexOf(udAxis);
  }
  return { state, turned };
}

// ---------- reading a state ----------

export function read(state, T, countTable) {
  const s = index(state);
  const ks = kinds(state);
  const twisted = ks.filter((k) => k === 1 || k === 2).length;
  const out = [3, 4, 5].map((k) => ks.filter((x) => x === k).length);
  const sorted = [...out].sort((a, b) => b - a);
  const row = countTable ? countTable[`${twisted}|${sorted.join(",")}`] : null;
  const closer = [];
  for (let m = 0; m < 9; m++) if (T.d[T.next(s, m)] < T.d[s]) closer.push(MOVES[m]);
  const descend = (table) => {
    const seq = []; let x = s;
    while (table[x] > 0) {
      let m = 0;
      while (table[T.next(x, m)] >= table[x]) m++;
      seq.push(MOVES[m]); x = T.next(x, m);
    }
    return { seq: seq.join(" "), end: x };
  };
  const way = descend(T.d), goodWay = descend(T.dg);
  return {
    index: s, kinds: ks, line: kindsLine(state), twisted, out, parity: parity(state) ? "odd" : "even",
    shape: outShape(state), dPicture: dPictureName(state, T), d: T.d[s], q: T.q[s], typesFloor: T.dg[s],
    parityFloor: T.de[s], countRow: row, closer, solution: way.seq, goodWay: goodWay.seq,
    goodWayEnds: T.d[goodWay.end], weight: out.reduce((a, b) => a + b, 0) + 2 * twisted,
  };
}
