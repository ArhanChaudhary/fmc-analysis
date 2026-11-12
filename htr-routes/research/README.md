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
| 7 | `htrtools docpaths ... 5000 11` | exact table | `out/big/docpaths.tsv` (docs 396/410 chains under three reading rules) | 21 s | 1.3 GB |
| 8 | `src/check_sticker.py 1000 60` | `htrtools trace`, sticker model, nissy | `out/checks/check_sticker.txt` | 90 s | 1.3 GB |
| 9 | `src/map_names.py` | docs 15 / 66 examples, `htrtools nisshtr` | `out/name_map.tsv` | 2 s | 1.3 GB |
| 10 | `src/stats_analysis.py` | step 3 states | `out/q3_htr.tsv`, `q3_htr_by_length.tsv`, `q4_qt.tsv`, `q5_states.tsv`, `compare_doc15.tsv`, `compare_doc66.tsv`, `compare_doc9.tsv` | 25 s | 0.5 GB |
| 11 | `src/routes_analysis.py` | step 3 | `out/q1_routes.tsv`, `q2_checklist.tsv`, `q2_best.tsv` | 25 min | 2.0 GB |
| 12 | `src/checklist_cost.py` | step 3 | `out/q2_checklist_budget.tsv` (the main checklist, with HTR budgets) | 72 s | 1.3 GB |
| 13 | `src/compare_docs.py`, `compare_docs.py doc171`, `compare_docpaths.py` | steps 3, 4, 7, docs 396/410/171 CSVs | `out/compare_docs_396_410*.tsv`, `compare_docs_reading_rules.tsv`, `compare_doc171*.tsv` | 35 s | 1.0 GB |
| 14 | `src/bounding.py` | steps 3, 5, 6 | `out/q8_bounding.tsv`, `q8_reduction_counts.tsv`, `q9_fakemmap.tsv`, `q9_counterexamples.tsv`, `q9_tables.tsv` | 4 min | 2.1 GB |
| 14b | `htrtools redcount2 ... 4000 20261112 7` | exact table | `out/big/redcount2.tsv` (reductions to 1q / 2q of each length <= 7, first 4,000 states per subset; B counted by coset tables, identical to brute force on 4,800 states: `out/checks/check_redcount2.txt`) | 27 min 41 s | 1.4 GB |
| 14c | `htrtools bound2 ... 25000 20261112` | exact table | `out/big/bound2.tsv` (per state: finishes up to max(opt+1, min(opt+2, 12)) by corner path, sections, reductions; trigger and switch data for C11 / C13) | 5 min 19 s | 1.3 GB |
| 14d | `src/bounding2.py` (calls `htrtools alpha`) | 14b, 14c | `out/q8_bounding_v2.tsv`, `q9_alpha.tsv`, `q9_v2.tsv`, `q9_v2_counterexamples.tsv`, `q9_rodney_table.tsv`, `c11_c13.tsv` (supersede the Q9 part of step 14) | 3 min 47 s | 3.9 GB |
| 14e | `src/t11503_cex.py` | 14c | `out/q9_t11503_examples.tsv` (923 cases where the T11503 bound as written exceeds the optimum) | 49 s | 3.0 GB |
| 14f | `htrtools bound4 ... 4000 20261112`, `src/q8_stated.py` | exact table, redcount2 | `out/big/bound4.tsv`, `out/q8_bounding_stated.tsv` (Q8 as the method states it: reduction to 1q / 2q, then the optimal finish of the reduced state; exact search) | 1 min / 10 s | 1.4 GB |
| 14g | `htrtools redcount ... 10 20261112 7`, `src/check_redcount7.py` | exact table | `out/checks/check_redcount7.txt` (brute force vs coset counts, r <= 7, 480 states) | ~10 min | 1.4 GB |
| 15 | `src/grade.py` | step 3 | `out/q6_grading.tsv` | 70 s | 2.2 GB |
| 16 | `src/claims.py` | all of the above, `out/claims_raw.tsv` | `out/claims.tsv` | 3 min | 2 GB |
| 17 | `src/summary.py specs`, `src/witness.py`, `src/summary.py` | all of the above, `htrtools explain / trace`, nissy, sticker model | `out/witness_specs.json`, `out/witness.json`, `out/SUMMARY.md` | 10 s | 1.3 GB |

`out/claims_raw.tsv` (125 claims with quotes and message ids) was extracted by hand-checked reading of
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
  switch, and whether the post-HTR part has a quarter turn; `F:` = labels over the whole finish (docs 396/410).
* HTR length of a reading: moves done (both sides) until the current side's state is in HTR.
* Shortest NISS HTR: min |A| + |B| with (X A)^-1 B in HTR (exact IDA*, corner-only and edge-only bounds).
* X R2: the DR's last move turned the other way.

## Not covered / caveats

* Route membership at optimal + 1 uses the same enumeration and reading code as at the optimum; the optimum level
  is checked against the sticker model and nissy (1,240 states), the +1 level is not checked independently.
* Samples, not exact, for route questions (25,000 per subset x edges); reduction counts on 4,000 states per subset x edges (step 14b; the first pass, step 6, used 100).
* Route keys do not record half-turn counts between quarter turns; checklist steps that depend on setup lengths
  are graded as their whole class (marked "~" in `q6_grading.tsv`). Sections (half turns between quarter turns)
  are recorded per finish in `bound2` (C11, C13, Q9), not checked on the sticker model.
* Q8 / Q9 for fixed targets M = 10-12 use finishes up to max(opt + 1, min(opt + 2, 12)) moves; for states with an
  optimum of 9 or less a longer target is not covered and their needed reduction is an upper bound.
