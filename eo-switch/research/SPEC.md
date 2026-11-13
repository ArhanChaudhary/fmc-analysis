# When to switch on an EO: what to compute (study 6)

Request (professional solver, 2026-11-12): "find better guidelines than we have already (arm, drm, pairs, maybe
rodney's corner orbit thing) for when to switch an eo, closer to 100% vs 0% chance of sub7 to dr. Guidelines that
humans can quickly check."

On the server "switch" means: after EO (+ RZP), go to the inverse (NISS) and keep the EO, because the case predicts a
short DR there; the rules are keep/switch/discard rules. Evidence, definitions, rules and tables:
`/data/fmc/kb/reread/eoswitch_notes.md` (read it all; definitions from LouisSart and rodneykinney DRM-ARM-stats code;
fix the corner-index convention with its test states before trusting any feature).

## State and target
F/B EO, U/D DR. State = (co of 8 corners, positions of the 4 E-edges) : 3^7 * C(12,4) = 1,082,565. Target: optimal
EO-kept DR length <= 6 (also <= 5, <= 7, and <= 11 - L for an RZP of length L). Also with the last EO/RZP turn free
(min over the state and the state with that turn reversed) and with both DR axes. Exact over all states.

## Populations (report every rule on each)
1. Uniform EO-solved states (what all existing tables use).
2. States as reached by an RZP: weight each state by the number of ways an RZP of each length reaches it from
   uniform EO-solved states / from uniform scrambles' EOs (torchlight's bias, T4250), exact by counting.
3. Sampled real attempts: uniform scrambles (eodrtools mkscr, NOT nissy's scrambler), every EO <= 4/5, every RZP to
   each DRM the server names, at total length 5 and 6.

## Features
The 19 candidates in the notes' final list (DRM, corner/edge ARM, orbit case 4a-4d + suffix, twist split, pairs, fake
pairs, side pairs, unpaired corners, split pairs, AR pairs/bars, layer layouts, corner-only optimal, distance to
trigger families, special corner states, 7c8e patterns, 8c8e checks, free options, RZP length). Each with a stated
by-hand reading and a rough cost to check.

## Questions
1. Reproduce: Cale's/Louis's DRM tables, Louis/Evan ARM/pairs tables, Rodney's corner-variant+pair stats
   (exact where they are exact; within error where sampled).
2. Grade every existing rule in the notes (per DRM): share of states it keeps, precision (sub-7 among kept), recall,
   sub-7 states discarded; on each population.
3. Search rules of 1-3 features (decision lists / small trees over human-readable features) maximizing separation:
   mass in the < 10% and > 50% bands, the in-between mass left; Pareto front of rule size vs separation; per DRM.
   Report a rule only if it holds out-of-sample on populations 2 and 3.
4. Which feature adds most to DRM; to DRM+ARM; whether the corner orbit case beats pairs; bars vs separate pairs.
5. Every checkable claim with verdict and an example (EO + state) for each correction.

## Checks
Exact distances from a BFS over the 1,082,565 cosets, matched against eo-to-dr's table and nissy on 1,000 states;
every feature implementation unit-tested on hand-made states from the notes' examples; every printed line replayed on
`is-dr-xs-worth-it/research/src/cube.py`. Lean certificate for the per-feature tables.

## Addendum (2026-11-13): counts with U and D turns free
U and D turns keep every pair, so a case reduces to two rings (the U and D layers up to turning: 4 edge places and 4
corners each, a bad corner pointing at the edge place it would pair with) and the four E-slice places. Definitions,
turn rules and exhaustive checks: `src/rings.py` (out/big/rings.npz, out/checks_rings.txt).
- sigma: fewest side turns (R, L quarter or half, F2, B2) of any DR, U/D free; (q, h): quarter and half turns of the
  side-turn-optimal setups (fewest quarter turns on ties); Q[q][h]: fewest moves of a DR with exactly that make-up.
- 4c4e: hbar = fewest half turns before one R/L quarter turn finishes = max(row swaps on the ring pair, hole number).
- Tables, examples (replayed on stickers) and the integer cells the Lean certificate asserts: `src/xrings.py`
  (report/data/ring_*.md, out/rings.json, out/ring_examples.json, out/rings_lean_ref.json).
- Reading the rings on the normal side, checked on random cubes: `src/xtrace_rings.py`.
