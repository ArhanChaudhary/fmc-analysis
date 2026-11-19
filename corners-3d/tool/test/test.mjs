// Checks the page's model and tables against the study's: the 200 random states of the examples page, and a few
// scrambles with L, D, B turns.   usage: node tool/test/test.mjs
import { readFileSync } from "node:fs";
import { buildTables, stateOfScramble, read, index, N } from "../web/corners.js";
import { COUNT } from "../web/count.js";

const cases = JSON.parse(readFileSync(new URL("./cases.json", import.meta.url)));
const t0 = Date.now();
const T = buildTables();
console.log(`tables built in ${((Date.now() - t0) / 1000).toFixed(1)} s`);

const hist = (a) => { const h = []; for (let i = 0; i < N; i++) h[a[i]] = (h[a[i]] || 0) + 1; return h.join(" "); };
const expect = (name, got, want) => { if (String(got) !== String(want)) { console.error(`FAIL ${name}: got ${got}, want ${want}`); process.exitCode = 1; } };
expect("moves to HTR", hist(T.d), "24 72 432 2304 13464 65496 296400 1077072 1813680 401472 3744");
expect("quarter turns", hist(T.q), "24 432 6768 86184 780048 1708416 1049856 42048 384");
expect("types floor", hist(T.dg), "144 432 2592 13824 80784 378720 1304928 1692288 198144 2304");
expect("types + parity floor", hist(T.de), "72 216 1296 6912 40392 193032 751824 1793520 856008 30888");

let n = 0;
for (const c of cases) {
  const { state, turned } = stateOfScramble(c.scramble);
  const r = read(state, T, COUNT);
  expect(`${c.scramble} turned`, turned, false);
  expect(`${c.scramble} types`, r.line, c.kinds);
  expect(`${c.scramble} d`, r.d, c.d);
  expect(`${c.scramble} q`, r.q, c.q);
  expect(`${c.scramble} types floor`, r.typesFloor, c.floor_types);
  expect(`${c.scramble} parity floor`, r.parityFloor, c.floor_par);
  expect(`${c.scramble} closer`, r.closer.join(","), c.closer.join(","));
  expect(`${c.scramble} shape`, r.shape, c.shape);
  expect(`${c.scramble} D picture`, r.dPicture, c.colour);
  expect(`${c.scramble} parity`, r.parity, c.parity);
  expect(`${c.scramble} count floor`, r.countRow.moves, c.floor_count);
  expect(`${c.scramble} count floor qt`, r.countRow.quarter, c.floor_count_q);
  expect(`${c.scramble} out`, r.out.join(","), c.out.join(","));
  expect(`${c.scramble} way to all good ends`, r.goodWayEnds, c.types_solution_ends);
  n++;
}
// turns of the other three faces are the same corner state as R, U, F with the cube held differently
const same = (a, b) => expect(`${a} = ${b}`, index(stateOfScramble(a).state), index(stateOfScramble(b).state));
same("L", "R"); same("D", "U"); same("B", "F"); same("U D'", ""); same("L2 R2", ""); same("x y z", "");
same("L U B' D2 y", "L U B' D2"); same("L U B' D2 x2 z'", "L U B' D2"); same("D R", "U y' R");
console.log(`${n} states checked` + (process.exitCode ? " WITH FAILURES" : ", all the same as the study's tables"));
