# research: which HTR routes to try from a DR

Computation behind the fifth case study (questions in `SPEC.md`, answers in `out/SUMMARY.md`).
Everything is rebuilt by `run_all.sh` (about 50 minutes on the 4-core, 7.7 GB VM; one heavy job at a time,
each under `systemd-run --user --scope -p MemoryMax=5G`).

Inputs from the first study (`/data/fmc/judging-a-dr`, read only): `research/data/lean_exact_table.u8` (optimal
finish of every DR state, Lean-checked, 1.34 GB), `research/data/ls_depth.u8` (optimal leave-slice), and the model
sources `research/drtools/src/{core,class,reduced}.rs`, included into `htrtools` by `#[path]`. The sticker model for
the checks is `/data/fmc/is-dr-xs-worth-it/research/src/cube.py`. nissy 2.0.8 for cross-checks.

## Layout

| Path | What |
|---|---|
| `htrtools/` | Rust (rayon). `model.rs`: depth lookup, labels, uniform sampler per subset, exact shortest NISS HTR (IDA*). `routes.rs`: enumeration of every optimal and +1 finish, every NISS reading, route keys. `cmds.rs`: the subcommands. |
| `src/` | Python (numpy). Checks, analysis, claims, witnesses, SUMMARY. |
| `out/` | Small results (TSV / JSON / SUMMARY.md); `out/checks/` the checks; `out/big/` (git-ignored) the per-state data. |

## Steps (input -> output; wall time; peak memory)

| # | Command | Input | Output | Time | Peak RSS |
|---|---|---|---|---|---|
| 1 | `htrtools dist` | exact table | `out/checks/dist48.tsv`, `htr_states.tsv`, `htr48.tsv` (per-subset optimal over all DR states; the 663,552 HTR states; DR->HTR per subset) | 2 s | 1.3 GB |
| 2 | `src/check_dist.py` | step 1, first study census, Joba docs 580/566, DougCube doc 218 | `out/checks/check_dist.txt` | 1 s | small |
| 3 | `htrtools routes ... 25000 20261112` | exact + leave-slice tables | `out/big/run1/states_<subset>.tsv` (per state: optimum, HTR lengths, qt counts, leave slice, X R2), `routes_<subset>.bin` (u64 per route and state: id, shortest HTR at the route's shortest finishes, shortest HTR over every finish within +1, finish length minus optimum), `route_keys.tsv`, `route_aliases.tsv` (mirror pairs) | 18 min 25 s | 1.6 GB |
| 4 | `htrtools tie / tiels ... 5000 7` | exact (+ ls) table | `out/big/tie.tsv`, `tiels.tsv` (one optimal per state, random tie-break, linear chain) | 7 s / 15 s | 1.4 GB |
| 5 | `htrtools bound ... 25000 20261112` | exact table | `out/big/bound.tsv` (shortest 1q / 2q reduction per state, length, qt count; same states as step 3) | 4 min 22 s | 1.3 GB |
| 6 | `htrtools redcount ... 100 20261112 5` | exact table | `out/big/redcount.tsv` (reductions a solver writes, r <= 5) | 8 min 14 s | 1.3 GB |
| 7 | `src/check_sticker.py 1000 60` | `htrtools trace`, sticker model, nissy | `out/checks/check_sticker.txt` | 90 s | 1.3 GB |
| 7b | `src/check_c_invariance.py 3000` | sticker model | `out/checks/check_c_invariance.txt` (a half turn after or before a DR never changes its subset × edges label, so FakeMMAP's C bounds the middle block of a finish) | 1 min | 0.1 GB |
| 8 | `src/map_names.py` | docs 15 / 66 examples, `htrtools nisshtr` | `out/name_map.tsv` | 2 s | 1.3 GB |
| 9 | `src/stats_analysis.py` | step 3 states | `out/q3_htr.tsv`, `q3_htr_by_length.tsv`, `q4_qt.tsv`, `q5_states.tsv`, `compare_doc15.tsv`, `compare_doc66.tsv`, `compare_doc9.tsv` | 25 s | 0.5 GB |
| 10 | `src/routes_analysis.py` | step 3 | `out/q1_routes.tsv`, `q2_checklist.tsv`, `q2_best.tsv` | 25 min | 2.0 GB |
| 11 | `src/checklist_cost.py` | step 3 | `out/q2_checklist_budget.tsv` (the main checklist, with HTR budgets) | 72 s | 1.3 GB |
| 11b | `src/edge_gain.py` | step 3, step 11 | `out/q2_edge_gain.tsv` (budget 2: own subset × edges checklist against the pooled corner checklist on the same group, after 1/2/3/5 routes; first route, rank of the pooled first route) | 1 min 38 s | 1.3 GB |
| 11c | `src/edge_steps.py` | step 3, step 11 | `out/q2_edge_steps_checklist.tsv` (budget-2 checklists over routes with the bad-edge count at every step, the H keys, against corner-only), `q2_edge_steps_via.tsv` (share of states whose budget-2 routes pass each intermediate subset × edges), `out/checks/check_edge_steps.txt` (labels carry the group's edge count; corner-only greedy reproduces step 12) | 3 min 31 s | 2.1 GB |
| 12 | `src/compare_docs.py doc171` | step 4, doc 171 CSV | `out/compare_doc171*.tsv` | 35 s | 1.0 GB |
| 13 | `src/bounding.py` | steps 3, 5, 6 | `out/q8_bounding.tsv`, `q8_reduction_counts.tsv`, `q9_fakemmap.tsv`, `q9_counterexamples.tsv`, `q9_tables.tsv` | 4 min | 2.1 GB |
| 13b | `htrtools redcount2 ... 4000 20261112 7` | exact table | `out/big/redcount2.tsv` (reductions to 1q / 2q of each length <= 7, first 4,000 states per subset; B counted by coset tables, identical to brute force on 4,800 states: `out/checks/check_redcount2.txt`) | 27 min 41 s | 1.4 GB |
| 13c | `htrtools bound2 ... 25000 20261112` | exact table | `out/big/bound2.tsv` (per state: finishes up to max(opt+1, min(opt+2, 12)) by corner path, sections, reductions; trigger and switch data for C11 / C13) | 5 min 19 s | 1.3 GB |
| 13d | `src/bounding2.py` (calls `htrtools alpha`) | 13b, 13c | `out/q8_bounding_v2.tsv`, `q9_alpha.tsv`, `q9_v2.tsv`, `q9_v2_counterexamples.tsv`, `q9_rodney_table.tsv`, `c11_c13.tsv` (supersede the Q9 part of step 14; model and derivation in `notes/fakemmap_C.md`; streams `bound2.tsv` one subset at a time) | about 7 min | 0.9 GB |
| 13e | `src/t11503_cex.py`, `src/xlbdist.py` | 13c | `out/q9_t11503_examples.tsv` (cases where the T11503 bound as written exceeds the optimum), `out/checks/t11503_counts.txt` (as written and with α_(i+1)), `out/q9_lb_values.tsv` (typical corrected bound) | 53 s + about 1 min | 0.2 GB (both stream `bound2.tsv`) |
| 13f | `htrtools bound4 ... 4000 20261112`, `src/q8_stated.py` | exact table, redcount2 | `out/big/bound4.tsv`, `out/q8_bounding_stated.tsv` (Q8 as the method states it: reduction to 1q / 2q, then the optimal finish of the reduced state; exact search) | 1 min / 10 s | 1.4 GB |
| 13g | `htrtools redcount ... 10 20261112 7`, `src/check_redcount7.py` | exact table | `out/checks/check_redcount7.txt` (brute force vs coset counts, r <= 7, 40 states: the first 10 of 0c0 0e / 2e / 4e / 6e, all identical; r = 6 and 7 are not checked on the other 44 subsets) | brute force stopped after 6 h (about 70 h for all 48 subsets) | 1.4 GB |
| 14 | `src/grade.py` | step 3 | `out/q6_grading.tsv` | 70 s | 2.2 GB |
| 15 | `src/claims.py` | all of the above, `out/claims_raw.tsv` | `out/claims.tsv` | 3 min | 2 GB |
| 16 | `src/summary.py specs`, `src/witness.py`, `src/summary.py` | all of the above, `htrtools explain / trace`, nissy, sticker model | `out/witness_specs.json`, `out/witness.json`, `out/SUMMARY.md` | 10 s | 1.3 GB |

`out/claims_raw.tsv` (124 claims with quotes and message ids) was extracted by hand-checked reading of
`kb/reread/htr_theory_*.md`, `htr_discussion_*.md` and `htr_docs.md` Part B.

## Definitions in the code

* Finish: a canonical sequence of DR moves solving the state (no two moves on one face in a row, at most two moves in
  a row on one axis, both orders of commuting moves kept). All optimal and all optimal + 1 finishes are enumerated
  with the exact table as an admissible-and-exact bound.
* Reading of a finish S at split k: normal first (S[0..k] on normal, then the inverse of S[k..n] on inverse) or inverse
  first; the states seen are computed as permutations of segments of S (routes.rs header). Every reading is
  re-simulated move by move on the sticker model in the checks.
* Label: corner subset of the state's own corner coset (study 1's names; 4a3/4b3 and 4a4/4b4 by side) and bad edges
  in the frame with <= 4 bad corners. Route key `H:` = labels at the start and after each quarter turn up to HTR, the
  switch, and whether the post-HTR part has a quarter turn; `F:` = labels over the whole finish.
* HTR length of a reading: moves done (both sides) until the current side's state is in HTR.
* Shortest NISS HTR: min |A| + |B| with (X A)^-1 B in HTR (exact IDA*, corner-only and edge-only bounds).
* X R2: the DR's last move turned the other way.

## Not covered / caveats

* Route membership at optimal + 1 uses the same enumeration and reading code as at the optimum; the optimum level
  is checked against the sticker model and nissy (1,240 states), the +1 level is not checked independently.
* Samples, not exact, for route questions (25,000 per subset x edges); reduction counts on 4,000 states per subset x edges (step 13b; the first pass, step 6, used 100).
* Route keys do not record half-turn counts between quarter turns; checklist steps that depend on setup lengths
  are graded as their whole class (marked "~" in `q6_grading.tsv`). Sections (half turns between quarter turns)
  are recorded per finish in `bound2` (C11, C13, Q9), not checked on the sticker model.
* Q8 / Q9 for fixed targets M = 10-12 use finishes up to max(opt + 1, min(opt + 2, 12)) moves; for states with an
  optimum of 9 or less a longer target is not covered and their needed reduction is an upper bound.
