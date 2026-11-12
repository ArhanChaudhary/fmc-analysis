# Which HTR routes to try from a DR: results

Fifth case study. Everything below is computed on the DR group <U, D, R2, L2, F2, B2> with the first study's exact optimal-finish table (all 19,508,428,800 DR states). Route questions use **25,000 uniform states per subset x edge count (48 x 25,000 = 1,200,000 states)**, each solved exactly: every optimal finish and every optimal + 1 finish (all orders of commuting moves), every NISS reading of each (split after any move, either side first), plus the same for the DR with its last move turned the other way (X R2). Exact over all DR states where stated. Finishes stay in the DR group (no DR-breaking moves); E slice solved unless "leave slice".

Labels: study 1 / Mallard subsets ("4b2 4e"); the corner letter of 3- and 4-qt subsets is the side's own (4a3 / 4b3, 4a4 / 4b4). Where docs disagree: doc 15 and doc 171 call 4b2 "2qt(a)" and 4a2 "2qt(b)"; doc 66 the reverse (its own examples prove it, out/name_map.tsv); Joba's 4c5 = 4b5.

Route notation: `4b2 > 2c3 > (4b2 > 4a1 > 0c0) | ht` = the corner subset at the start and after each quarter turn until HTR, the part in brackets done on the other side after a NISS switch, `| ht` = the rest of the finish is half turns (`| qt` = HTR-breaking finish).

**One fact governs every route question**: a NISS reading of a finish is also a finish read linearly, so "some optimal follows route X" cannot tell linear from NISS routes. What NISS changes is the length of the HTR the solver must find. Checklists below therefore carry an **HTR budget**: a class counts only if its HTR is at most the state's shortest NISS HTR + 2 (budget 2); "no limit" rows are the plain class.

Samples: route questions 25,000 uniform states per subset x edges (seed 20261112); Q8 shares and reduction counts the first 4,000 of them; "one optimal at random" numbers (docs 171 comparison, C01-C06, C41, C42) 5,000 other uniform states per subset x edges (htrtools tie / tiels, seed 7); the docs 396/410 reading-rule comparison 5,000 per subset x edges (htrtools docpaths, seed 11).

## Checks (all passed before any number was used)

- total states 19508428800
- (1a) vs first study census.csv: 473 (subset, depth) cells, 0 differ
- (1b) vs Joba doc 580 (4c5 read as 4b5): 473 cells, 0 differ []
- (2) DougCube HTR Finish: 663552 states, mean 10.13432557; ours half-turn-only: 663552 states, mean 10.13432557; all depth counts equal: True
-     the same 663,552 HTR states with any DR move allowed (HTR-breaking finishes): mean 9.88708, 663552 states; max 13 vs 15
- (3) Joba doc 566 (DR->HTR length per subset, with edges): 48 of 48 subsets agree to 1e-4 %; differ: []
- Independent sticker model (sticker.py, built from cube geometry only) on 1240 (1000 random-move scrambles + 5 per subset from the main sample) states: finish replayed: 18631; finish replay ok: 18631; finish read: 16140; H key sets equal: 16140; F key sets equal: 16140; HTR lengths equal: 16140; nissy states: 1240; nissy optimal length equal: 1240; nissy finish sets equal: 1240; nissy count == nopt_canon: 1240; failures: 0.
- redcount2 (coset-table count of reductions to 1q / 2q, r <= 5) vs redcount (brute-force enumeration of every pair), first 100 states of every subset x edges: 4800 states, 4800 identical in every (q, r) cell. alpha for 4a3 > 4b2 > 4a1 > HTR = 0,3,1,0 (FakeMMAP T11501: alpha_1 = 3 for 4a3 2e).
- redcount2 vs brute force for every length r <= 7 (q = 1 and 2): 40 states, the first 10 of 4 subsets (0c0 0e, 0c0 2e, 0c0 4e, 0c0 6e); 40 identical in every (q, r) cell. The brute-force run was stopped after 6 hours (about 70 hours for all 48 subsets); r = 6 and 7 are not checked on the other 44 subsets.
- Every finish printed in this file and in witness.json is replayed on the sticker model (witness.json, `replayed_ok`).

## Q2. The checklist per subset (main deliverable)

Greedy order of route classes (corner chain + switch), counting a class only with an HTR at most 2 over the shortest NISS HTR. At +1 a class counts if any of its finishes within optimal + 1 has such an HTR (it may be shorter than on the optimal finishes). Ties (classes covering exactly the same states) are broken the same way everywhere: linear first, then the normal-first reading of a mirror pair (a split of a finish read starting on normal or on inverse is the same pair of moves; such mirror pairs of classes are in out/route_aliases_C.tsv and each chosen class's mirror is in q2_checklist_budget.tsv; as classes they do not cover the same states, since each also collects other finishes: C-level mirror pairs checked over all 48 subsets: 21552; identical state sets: 646.), then the name. Cumulative share of states where the classes so far find an optimal finish; last column: the same three classes at optimal + 1. Edge counts pooled by their exact sizes; 25,000 states per subset x edges. Per subset x edges, all budgets (0, 1, 2, none) and up to 8 classes: out/q2_checklist_budget.tsv. Without a budget the first one or two classes reach 90-99% (out/q2_checklist.tsv, out/q2_best.tsv: greedy is within 0.5 points of the best possible set of the same size (k = 1-4, best set searched among the top 25-40 classes) in 2,192 of 2,208 cases, at most 1.8 points off).

| subset | 1st class | 2nd | 3rd | after 1 / 2 / 3 | +1 after 3 |
|---|---|---|---|---|---|
| 0c0 | `0c0 > 4a1 > 0c0` | `0c0 > 4a1 > (0c0)` | `0c0 > 4a1 > 0c0 > 4a1 > (0c0)` | 42.3% / 55.9% / 60.9% | 86.4% |
| 2c5 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 72.8% / 85.5% / 91.4% | 98.9% |
| 2c4 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 66.0% / 83.5% / 88.4% | 98.7% |
| 0c3 | `0c3 > 4a2 > (4a1 > 0c0)` | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | `0c3 > 4a2 > 4b3 > (4b2 > 4a1 > 0c0)` | 74.4% / 88.8% / 89.3% | 99.2% |
| 4a2 | `4a2 > 4a1 > (0c0)` | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 41.6% / 64.1% / 73.2% | 91.8% |
| 4a1 | `4a1 > 4b2 > 4a1 > 0c0` | `4a1 > 0c0 > (4a1 > 0c0)` | `4a1 > 0c0` | 29.3% / 44.8% / 58.0% | 84.3% |
| 2c3 | `2c3 > 4b2 > 4a1 > 0c0` | `2c3 > 4b2 > (4a1 > 0c0)` | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 53.5% / 75.7% / 78.0% | 96.1% |
| 0c4 | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | `0c4 > 4a3 > (4a2 > 4a1 > 0c0)` | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 83.8% / 85.1% / 86.3% | 97.6% |
| 4c3 | `4a3 > 4b2 > (4a1 > 0c0)` | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 64.3% / 71.3% / 75.0% | 94.2% |
| 4c4 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 68.1% / 75.0% / 78.4% | 96.1% |
| 4b2 | `4b2 > 4a1 > 0c0` | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 37.6% / 53.3% / 62.6% | 88.0% |
| 4b5 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 64.7% / 87.4% / 93.7% | 99.6% |

Per subset x edges (budget 2, optimal; first class and cumulative after 1/2/3):

| subset | first class | 1 / 2 / 3 | +1 after 3 |
|---|---|---|---|
| 0c0 0e | `0c0 > 4a1 > 0c0` | 42.5% / 84.4% / 92.6% | 98.3% |
| 0c0 2e | `0c0 > 4a1 > 0c0` | 60.5% / 65.7% / 70.2% | 92.3% |
| 0c0 4e | `0c0 > 4a1 > 0c0` | 44.9% / 57.8% / 61.5% | 88.1% |
| 0c0 6e | `0c0 > 4a1 > (0c0)` | 40.8% / 53.7% / 60.2% | 88.1% |
| 0c0 8e | `0c0 > 4a1 > (0c0)` | 53.5% / 70.1% / 77.1% | 95.0% |
| 2c5 0e | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 77.8% / 86.5% / 89.6% | 98.7% |
| 2c5 2e | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.8% / 86.2% / 91.0% | 98.7% |
| 2c5 4e | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 71.5% / 86.0% / 91.9% | 99.0% |
| 2c5 6e | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.0% / 84.1% / 90.6% | 98.7% |
| 2c5 8e | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 77.6% / 86.0% / 91.0% | 98.9% |
| 2c4 0e | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 70.1% / 85.9% / 88.6% | 98.7% |
| 2c4 2e | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 67.7% / 86.3% / 89.9% | 98.9% |
| 2c4 4e | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 62.0% / 82.0% / 87.6% | 98.7% |
| 2c4 6e | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.8% / 84.1% / 88.5% | 98.6% |
| 2c4 8e | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 77.7% / 89.5% / 91.5% | 99.4% |
| 0c3 0e | `0c3 > 4a2 > (4a1 > 0c0)` | 85.5% / 94.2% / 96.6% | 99.8% |
| 0c3 2e | `0c3 > 4a2 > (4a1 > 0c0)` | 80.8% / 91.3% / 92.1% | 99.5% |
| 0c3 4e | `0c3 > 4a2 > (4a1 > 0c0)` | 67.2% / 85.1% / 85.8% | 98.9% |
| 0c3 6e | `0c3 > 4a2 > (4a1 > 0c0)` | 82.6% / 93.9% / 94.6% | 99.7% |
| 0c3 8e | `0c3 > 4a2 > (4a1 > 0c0)` | 87.3% / 94.8% / 96.1% | 99.8% |
| 4a2 0e | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 29.1% / 40.4% / 44.4% | 68.4% |
| 4a2 2e | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 42.2% / 67.8% / 76.8% | 95.7% |
| 4a2 4e | `4a2 > 4a1 > 0c0` | 60.9% / 72.2% / 79.1% | 93.6% |
| 4a1 0e | `4a1 > 0c0 > (4a1 > 0c0)` | 33.5% / 46.5% / 54.6% | 84.2% |
| 4a1 2e | `4a1 > 4b2 > 4a1 > 0c0` | 38.8% / 58.8% / 70.5% | 92.7% |
| 4a1 4e | `4a1 > 0c0` | 33.6% / 50.3% / 60.6% | 86.9% |
| 2c3 0e | `2c3 > 4b2 > (4a1 > 0c0)` | 46.3% / 67.0% / 75.1% | 96.1% |
| 2c3 2e | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% / 79.6% / 80.2% | 96.6% |
| 2c3 4e | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% / 76.6% / 78.1% | 96.1% |
| 2c3 6e | `2c3 > 4b2 > (4a1 > 0c0)` | 66.1% / 73.3% / 76.7% | 95.8% |
| 2c3 8e | `2c3 > 4b2 > (4a1 > 0c0)` | 46.3% / 67.2% / 74.5% | 95.7% |
| 0c4 0e | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | 83.2% / 86.8% / 87.6% | 97.5% |
| 0c4 2e | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | 86.5% / 88.0% / 89.1% | 98.1% |
| 0c4 4e | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | 83.5% / 85.1% / 86.1% | 97.5% |
| 0c4 6e | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | 81.8% / 83.7% / 85.4% | 97.8% |
| 0c4 8e | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | 80.3% / 86.2% / 87.1% | 98.3% |
| 4c3 0e | `4a3 > 4b2 > (4a1 > 0c0)` | 70.8% / 78.4% / 83.3% | 97.2% |
| 4c3 2e | `4a3 > 4b2 > (4a1 > 0c0)` | 66.2% / 72.0% / 75.1% | 94.6% |
| 4c3 4e | `4a3 > 4b2 > (4a1 > 0c0)` | 62.3% / 70.2% / 74.4% | 93.9% |
| 4c4 0e | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 65.2% / 72.4% / 76.7% | 96.3% |
| 4c4 2e | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 67.9% / 75.4% / 78.7% | 96.4% |
| 4c4 4e | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 68.4% / 74.8% / 78.2% | 95.9% |
| 4b2 0e | `4b2 > 4a1 > 0c0` | 36.5% / 51.1% / 61.0% | 85.8% |
| 4b2 2e | `4b2 > 4a1 > 0c0` | 45.9% / 53.7% / 59.0% | 86.3% |
| 4b2 4e | `4b2 > 4a1 > 0c0` | 30.3% / 53.3% / 66.8% | 90.1% |
| 4b5 0e | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 60.8% / 84.2% / 92.6% | 99.4% |
| 4b5 2e | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 62.6% / 85.1% / 93.6% | 99.6% |
| 4b5 4e | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 67.0% / 89.6% / 93.9% | 99.6% |

Cheap vs marginal classes: with budget 0 (only shortest HTRs) the best single class finds the optimal in 13-48% of states per corner subset, with budget 2 in 29-84%, with no limit in 51-98% (out/q2_checklist_budget.tsv). After the third class each further class adds at most 8 points, usually under 3: these pay only at the margin. The cost proxy (mean shortest HTR of the class where it works) is in out/q1_routes.tsv and out/q2_checklist.tsv. Striking findings:
- NEW: on 4c3 the single class `4a3 > 4b2 > (4a1 > 0c0)` (one qt to 4b2 from the a side, switch) finds the optimal in 64.3% of states with a near-shortest HTR; three classes 75.0% (witness W01). KNOWN in spirit: Daichi's sheet "always switch after 4b2 4e"; doc 396 lists this as the top 4c3 path.
- NEW: on 2c4, `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` alone gives 66.0%, three classes 88.4% (witness W02). KNOWN as advice (Daichi D18331).
- NEW: on 4b2 the linear 2qt route comes first (37.6%) but three classes only reach 62.6%: 4b2 needs the 4qt regressions through 2c3 (witness W03).

## Q1. How often each route class works

Per subset x edges, share of states where a class finds an optimal / within +1 / with the last DR move inverted: out/q1_routes.tsv (levels C corner chain, H with edges, Q quarter-turn shape, F the full-finish chain of docs 396/410). Cell-by-cell with docs 396/410: out/compare_docs_396_410_cells.tsv.
- KNOWN + NEW (method found): docs 396/410 are reproduced when each optimal finish is read only with its shortest-HTR NISS readings: doc 410 (7,007 paths) mean |difference| 0.008, correlation 0.965, 97.2% of paths within 5 points; every reading: 0.044; linear only: 0.025. Doc 396 (768 paths, sub-13 states, ~1000 per tab) 0.034. So 396/410 count, per state, every distinct shortest-NISS-HTR path of every optimal finish (D19661). Their 0c0 0e tab holds HTR states only (96% "no quarter turn"), while the 0c0 0e subset is half HTR, half U D' times HTR.
- KNOWN + CORRECTS: doc 171 (allcases) is reproduced by one leave-slice optimal per state with a random tie-break (1895 paths: mean |difference| 0.0029, correlation 0.991; full finish 0.0057 / 0.974), with its tie-break slightly favouring the fewest-qt path (~5 points). Its "2qt(b)" is 4a2: mrauo's "only 1/3 of 2q 4b2e use 2qt" (D9450) read the 4a2 2e row; Zagros's "a and b flipped" (D9451) is right for doc 66 vs doc 171.
- Doc 15 (1000 states per subset): solution means within 0.06 of exact; its "Linear HTR" is the normal side only (ours 6.156 vs 6.213 for 4b2 2e), its NISS HTR mean matches ours to 0.05 (out/compare_doc15.tsv).

## Q3. Shortest HTR vs optimal

All DRs (25,000 per subset, weighted): shortest NISS HTR 7.80, shortest linear (better side) 8.38, normal side 8.80. Some optimal uses a shortest NISS HTR in 32.9% of states; the best HTR an optimal uses is +1 in 31.8%, +2 in 22.5%, +3 or more in 12.8%; post-HTR part of that optimal 4.59 moves. Per subset: out/q3_htr.tsv, by HTR length out/q3_htr_by_length.tsv.
- NEW (T624 answered): linear and NISS shortest HTRs are equal in 55.8% of DRs, NISS 1 shorter in 32.3%, 2+ shorter in 11.9%; 0c3: 2+ shorter in 52.4%, 0c4 40.5%.
- NEW (C12 stays open): in 65.2% of all DRs every optimal finish needs an HTR of 9+ moves; given a shortest HTR of L moves, an optimal uses an L-move HTR in about a third of states for every L from 6 to 9 (witness W05). "9-move HTRs rarely give an optimal" is about each 9-move HTR a solver writes, which this does not measure.
- NEW: two thirds of DRs (67.2%) have no optimal finish through any shortest HTR (T554, T4167, T10409).
- CORRECTS "DR > slice ~ DR > solved - 1" (C23): optimal minus optimal leave-slice is 0.290 moves on average; ~0.7 only for 0c0 / 4a1. KNOWN from doc 15's own No-E column.

## Q4. Extra quarter turns

Share of states where every optimal uses more qts than the corner subset's count / where some optimal does (full finish), and every leave-slice optimal (doc 66's reading):

| subset | every optimal | some optimal | every leave-slice optimal |
|---|---|---|---|
| 0c0 | 99.4% | 99.6% | 99.3% |
| 2c5 | 3.2% | 17.5% | 3.0% |
| 2c4 | 5.8% | 33.2% | 4.8% |
| 0c3 | 24.0% | 43.2% | 24.4% |
| 4a2 | 49.4% | 73.3% | 43.3% |
| 4a1 | 82.5% | 92.7% | 73.8% |
| 2c3 | 17.5% | 53.6% | 11.2% |
| 0c4 | 10.0% | 43.6% | 9.3% |
| 4c3 | 27.4% | 64.1% | 25.3% |
| 4c4 | 27.1% | 65.1% | 27.4% |
| 4b2 | 55.0% | 82.5% | 40.9% |
| 4b5 | 1.9% | 13.2% | 1.4% |

- KNOWN: doc 66 "% with extra qts" = every leave-slice optimal uses extra qts; all 47 comparable rows agree within sampling error (out/compare_doc66.tsv). Its 0qt 0c0e row is HTR states only.
- NEW: the two readings explain the quoted numbers: rodney's 57% (2qt subsets, T539) is the "every optimal" reading (every optimal uses 4+ qt 53.9%), Lichi's >60% for 4b2 4e (nissy's first optimal) matches a random optimal (77.6%).
- AGREES (Kai T5573): 2c3 2e, some optimal has <2 half turns before its first qt on one of the two sides in 82.7% (85% claimed); normal side alone 62.0%.
- Doc 9: its corner-QT shares (17.1/27.5/32.9/22.5%) match neither the fewest quarter turns to solve corners (exact 17.6/28.1/35.2/19.1%) nor that count among move-optimal corner solutions; its "+0/+2" extra-qt shares sit between our fewest-qt and most-qt optimal readings (out/compare_doc9.tsv).

## Q5. Inverting the last DR move

- CORRECTS Yura (T4606, 1/6): X R2 is one move shorter in 32.5% of DRs (exact over all DR states 32.47%), never more; mean gain 0.325 move (witness W06). A qt break costs 0.68 moves on average (trangium ~0.5).
- With the variation allowed, route-class shares rise by about the same amount for every class (out/q1_routes.tsv columns share_vopt / share_vp1, checklists target vopt / vp1 in out/q2_checklist.tsv); it adds no new class to any checklist.

## Q6. Hand checklists graded

Cumulative share of states where the checklist finds an optimal (budget 2 HTRs; no-limit in brackets), out/q6_grading.tsv:

- Zagros 4b2 order (D15884): S1+S2 linear 2qt 4b2 > 4a1 > HTR (normal or inverse): 37.6% (45.0%); S3 linear 4qt HTR of <= 8 moves: 45.4% (54.3%); S4 reduce to 4a1, switch (4b2 > 4a1 > (HTR)): 50.8% (54.3%); S5 regress to 2c3, switch (4b2 > 2c3 > (...)): 64.2% (95.5%); S8 2+2: any 4qt route switching after the 2nd qt: 71.3% (100.0%)
- Yura 4b2 4e order (D6409-D6416): ~S1 linear 2qt trigger with <= 2 setup moves (HTR <= 6): 8.6% (8.6%); S2 regress to 2c3 (2e or 4e), then 2c3 linear or switch (4qt): 62.3% (82.2%); S3 reduce to 4a1 and switch: 72.9% (93.1%)
- rogo/Adri 4b2 4e order (D6422-D6424): ~S1 linear 2qt trigger with <= 2 setup moves (HTR <= 6): 8.6% (8.6%); S3 reduce to 4a1 and switch: 26.1% (36.2%)
- Lewis 4a2 0e/2e list (T6743): S1 linear 2qt 4a2 > 4a1 4e > HTR: 13.3% (32.4%); S2 reduce to 4a1 4e, switch: 32.2% (32.4%); S3 4qt linear through 4a2 4e again (qt, slice, qt): 37.7% (73.0%); S4 regress to 4b3 (2e/4e), switch, 4a3 > 4b2 > 4a1: 52.7% (73.6%); S5 regress to 0c3, then 0c3 > 4a2 > 4a1 (linear or NISS): 53.4% (73.6%)
- Jay/rodney 2c3 0e checks (T328-T344): ~2c3 0e: one qt to 4b2 4e, switch, 4a1 > HTR (Jay T328 / rodney T331-T344, prefix not restricted): 46.3% (46.9%)
- Fanti 4b2 4e split (D10034), cumulative: 2qt (4b2 > 4a1 > HTR, any switch): 35.5% (36.2%); 4qt via 2c3: 77.8% (93.1%); 4qt via 4a1 > 0c0: 80.2% (97.6%)
- Daichi's cheat sheet (D18340): 0c0 0e 84.5%, 0c0 2e 71.5%, 0c0 4e 65.1%, 0c0 6e 61.2%, 0c0 8e 70.1%, 2c5 0e 81.6%, 2c5 2e 86.1%, 2c5 4e 85.7%, 2c5 6e 83.7%, 2c5 8e 83.0%, 2c4 0e 88.4%, 2c4 2e 89.7%, 2c4 4e 87.3%, 2c4 6e 88.0%, 2c4 8e 89.5%, 0c3 0e 92.6%, 0c3 2e 85.6%, 0c3 4e 72.6%, 0c3 6e 87.9%, 0c3 8e 92.9%, 4a2 0e 37.6%, 4a2 2e 76.8%, 4a2 4e 65.9%, 4a1 0e 70.1%, 4a1 2e 76.5%, 4a1 4e 69.4%, 2c3 0e 87.8%, 2c3 2e 79.6%, 2c3 4e 76.6%, 2c3 6e 73.3%, 2c3 8e 85.9%, 0c4 0e 83.6%, 0c4 2e 89.2%, 0c4 4e 84.5%, 0c4 6e 83.4%, 0c4 8e 80.7%, 4c3 0e 74.8%, 4c3 2e 72.4%, 4c3 4e 67.8%, 4c4 0e 66.9%, 4c4 2e 70.6%, 4c4 4e 70.7%, 4b2 0e 74.9%, 4b2 2e 67.2%, 4b2 4e 77.8%, 4b5 0e 74.6%, 4b5 2e 78.8%, 4b5 4e 77.4%.
- KNOWN: Zagros's "optimal in 15 minutes like 80% of the time" fits: his eight steps reach 71% optimal / 91% within +1 with near-shortest HTRs. NEW: Yura's 4b2 4e order (regress to 2c3) finds about twice as many optimals as rogo/Adri's (trigger, then 4a1 switch).

## Q7. Claims

125 claims from the reading notes (out/claims.tsv): NOT CHECKED 66, AGREES 27, ANSWERED 15, CORRECTS 8, PARTLY 7, OPEN 2. Corrections with a witness: C15 (W06), C56 (W07), C51 (W08), C53 (W09). The SPEC's quoted numbers:

- C01 rodneykinney (57%): **PARTLY**. 2qt corner cases (4a2+4b2, all edges, weighted by size): every optimal uses 4+ qt 53.9%; some optimal does 80.7%; one optimal picked at random 69.0% (leave-slice 56.3%). 57% fits only the 'every optimal' reading. 25,000 states per subset.
- C02 Lichi Fang (>60%): **AGREES**. 4b2 4e: one optimal at random uses 4+ qt 77.6% (leave-slice 66.5%); every optimal 63.7%; some optimal 86.9%.
- C03 Lichi Fang / beef beans (~25%): **AGREES**. 4c3: every leave-slice optimal uses 5+ qt 25.3%; full finish 27.4%; by edges 0e/2e/4e (leave slice) 23.4%, 23.5%, 27.0%.
- C04 Evan (4%): **PARTLY**. 4b2 0e: one leave-slice optimal at random passes 4c3: 6.1% (full finish 7.4%); doc 171's tie-break favours fewer qts (see its comparison), which lowers 4qt paths like this one.
- C05 beef beans / Fanti / Zagros (3-4% (beef); 6.10% (Fanti, summed); ~6% (Zagros)): **PARTLY**. Depends on the reading. 4a1 4e: every optimal uses 5+ qt: leave slice 3.6%, full finish 10.2%; one optimal at random has 5+ qt 9.6% (leave slice). beef's 3-4% fits 'every leave-slice optimal'; Fanti's 6.10% is the sum of the allcases 5qt rows; full finishes give 10%.
- C06 Fanti (40% / 45% / ~8%): **AGREES**. 4b2 4e, one leave-slice optimal at random: 2qt 33.5%, 4qt via 2c3 46.8%, 4qt via 4a1 > 0c0 9.9% (Fanti: 40/45/8 from doc 171); full finish 22.4% / 51.1% / 11.6%.
- C07 zakimoshi (5/6): **AGREES**. Corner permutations with no bad corner (DR on all three axes): 576; of these 96 are 0c0 (HTR corners or U D' of them), so 480/576 = 0.8333 are fake (0c3, 0c4). Exact.
- C08 Jay (vibing) (8 (<=5); 11 (<=6); 4 (<=4)): **CORRECTS**. Shortest linear (normal-side) HTR per subset, exact over HTR cosets: 5 subsets <= 4, 9 <= 5, 12 <= 6. <=5: 0c0 0e, 0c0 2e, 0c0 4e, 4a2 4e, 4a1 4e, 2c3 2e, 2c3 4e, 4b2 2e, 4b2 4e.
- C09 Jay (vibing) (7 cases; 0c3 worse than 2c4): **AGREES**. Corner subsets with at most 3 qt: 0c0 4a1 4a2 4b2 0c3 2c3 4c3 (7). Mean optimal 0c3 14.460 vs 2c4 13.647 (exact): 0c3 is worse.
- C10 rodneykinney (2/3 (63%) of 3qt; 1/6 (16%) of 4qt; 4qt ~2x as common as 2qt): **PARTLY**. Corners, exact over the 40320 permutations: a bare quarter turn (no setup) on normal or on inverse takes a 3qt case to 2qt in 66.1% (rodney: 2/3, agrees). A 4qt case cannot reach 2qt with one quarter turn (0.0%); rodney's 1/6 for 4qt counted something else (his corner_h_sections column on the optimal corner solution, T507).
- C12 tseitsei89 (low chance): **OPEN**. The claim is about each 9-move HTR a solver writes, which is not measured here. What is measured: all DR states: every optimal finish needs an HTR of 9+ moves (its shortest HTR over all NISS readings) in 65.2% of states; 2c3 2e 21.4%, 4b2 4e 37.2%, 4c3 59.7%, 2c4 71.6%. Among states whose shortest NISS HTR is 9, an optimal uses a 9-move HTR in 0.3256 (about the same as for 6-8 moves). So 9-move HTRs are often the only way to an optimal, but the share of written 9-move HTRs that extend to an optimal is not computed.
- C14 Kai Cui (85% need <2 ht; 4 is rare): **AGREES**. 2c3 2e: some optimal has <2 half turns before its first quarter turn, read on normal or inverse: 82.7%; normal side only 62.0%; 3+ needed 5.2%.
- C15 Yura Riabov (1/6 move mean improvement (or 1/6 of DRs)): **CORRECTS**. Turning the DR's last move the other way (X -> X*R2): shorter by one move in 32.5% of states (exact over all DR states from the first study's h8 table: 32.47%), never by more; mean gain 0.325 move. Neither 1/6 move nor 1/6 of DRs: about 1/3.
- C26 JTuu (Kai Cui prompt; Tzak defs) (64.65% (L7,B4) ... 86.05% (L8,B5)): **OPEN**. Same definitions as JTuu (linear HTR within L moves, or a reduction of at most B moves to 4a1 4e followed by one quarter turn), uniform 2c3 2e, 25,000 states: an optimal is found by linear HTRs <= 7 or 1q reductions <= 4 in 55.3% (linear alone 38.1%, bounding alone 44.7%); <= 8 / <= 5: 80.3% (63.4%, 71.3%). JTuu's sim: 64.65% / 86.05%, 6-9 points more; his states were probably drawn differently (e.g. with the last DR move inverted).
- C27 Zagros (~80% optimal): **AGREES**. Zagros's 4b2 order on 4b2 (0/2/4e, weighted), only HTRs at most 2 moves over the shortest NISS HTR: step 1 37.6% (+1: 67.2%); step 2 45.4% (+1: 75.7%); step 3 50.8% (+1: 80.8%); step 4 64.2% (+1: 90.4%); step 5 71.3% (+1: 93.4%); with no HTR limit: step 1 45.0% (+1: 74.8%); step 2 54.3% (+1: 83.0%); step 3 54.3% (+1: 83.0%); step 4 95.5% (+1: 99.4%); step 5 100.0% (+1: 100.0%). ~71% optimal (91% within +1) with realistic HTRs, close to his 80%.
- C48 wen / Lichi Fang (hardly ever 2q switch 2q): **CORRECTS**. 2c4: share of states where an optimal is reached through each route shape using an HTR at most 2 moves over the shortest NISS HTR: 1+(3) | ht 66.5%, 3+(1) | ht 66.5%, 4 | ht 54.0%, 2+(2) | ht 30.8%, 4+(2) | ht 3.3%, 2+(4) | ht 3.3%, 1+(5) | ht 3.0%. (Without an HTR limit every shape that a finish can be read in ties, ~94%.)

## Q8. DR bounding as a route

The method as stated: some reduction to 1q (reach 4a1 4e; or to 2q) of at most R moves, on normal, on inverse or split by NISS, followed by the optimal finish of the reduced state (any number of quarter turns), gives an optimal finish (or one within +1, or of at most M = 10, 11, 12). Exact search on reductions (htrtools bound4: along each side, length + optimum never decreases, so the search is cut at the target), first 4,000 states of every subset x edges (the states of the main pass). Reductions counted as a solver writes them: pairs (moves on normal, moves on inverse), each empty or ending in a quarter turn, counted exactly with coset tables for r <= 6 (checked against brute force on 4,800 states for r <= 5 and on 40 states of 0c0 0e/2e/4e/6e for r <= 7; reduction counts for R = 7 are not reported: the brute-force check of them was stopped after 6 hours). The R <= 7 column gives the share found only. out/q8_bounding_stated.tsv has every subset x edges, R = 0-7, every target, with standard errors.

| subset | R<=3: found / reductions | R<=4 | R<=5 | R<=6 | R<=7 | +1 at R<=4 | <=12 at R<=5 | 2q R<=3 |
|---|---|---|---|---|---|---|---|---|
| 0c0 | 86.0% / 156 | 91.5% / 1238 | 93.9% / 8763 | 96.9% / 63868 | 99.1% | 98.9% | 51.0% | 100.0% / 384 |
| 2c5 | 0.0% / 0 | 0.0% / 0 | 0.0% / 0 | 10.9% / 237 | 45.8% | 0.0% | 0.0% | 0.0% / 0 |
| 2c4 | 0.0% / 0 | 3.5% / 11 | 25.7% / 228 | 59.5% / 2503 | 84.6% | 8.5% | 3.7% | 46.5% / 71 |
| 0c3 | 12.7% / 5 | 35.0% / 38 | 65.5% / 399 | 81.7% / 3628 | 85.3% | 52.1% | 2.6% | 98.4% / 101 |
| 4a2 | 64.3% / 26 | 76.6% / 207 | 80.0% / 1463 | 85.2% / 10942 | 92.3% | 93.6% | 15.9% | 100.0% / 181 |
| 4a1 | 62.3% / 80 | 75.6% / 623 | 88.6% / 4901 | 95.4% / 36474 | 98.0% | 89.2% | 43.6% | 98.9% / 304 |
| 2c3 | 20.5% / 16 | 48.1% / 140 | 71.1% / 1080 | 86.2% / 9111 | 94.2% | 78.8% | 21.1% | 95.7% / 152 |
| 0c4 | 0.0% / 0 | 10.2% / 22 | 37.0% / 330 | 63.5% / 3075 | 84.3% | 19.0% | 3.4% | 77.9% / 123 |
| 4c3 | 15.7% / 8 | 37.5% / 66 | 60.1% / 559 | 75.1% / 4959 | 86.8% | 66.1% | 8.4% | 93.4% / 102 |
| 4c4 | 0.0% / 0 | 3.7% / 6 | 17.6% / 83 | 38.8% / 800 | 58.2% | 6.4% | 0.6% | 41.6% / 36 |
| 4b2 | 43.7% / 26 | 58.0% / 233 | 74.1% / 1978 | 88.8% / 16087 | 97.6% | 84.5% | 28.0% | 100.0% / 248 |
| 4b5 | 0.0% / 0 | 0.0% / 0 | 0.0% / 0 | 10.3% / 229 | 48.1% | 0.0% | 0.0% | 0.0% / 0 |

Standard errors: shares at most 0.8 points per corner subset (4,000-20,000 states). A stricter reading, the reduction followed by a finish with exactly one quarter turn (what JTuu's T5744 sim measured, out/q8_bounding_v2.tsv), finds less: 2c3 at R <= 4 / 5: 39.8% / 63.8% against 48.1% / 71.1% as stated; 4b2 42.4% / 63.6% against 58.0% / 74.1%.

Bounding against the route checklist of Q2: smallest R reaching 80% optimal and the reductions it takes, against the classes the budget-2 checklist needs for 80%:

| subset | bounding: R for 80% (reductions) | checklist: classes for 80% (budget 2) | checklist, no HTR limit |
|---|---|---|---|
| 0c0 | 3 (156) | > 8 (69.4%) | 2 |
| 2c5 | > 7 (45.8% at 7) | 2 | 1 |
| 2c4 | 7 (count not reported) | 2 | 1 |
| 0c3 | 6 (3628) | 2 | 2 |
| 4a2 | 5 (1463) | 5 | 3 |
| 4a1 | 5 (4901) | > 8 (74.6%) | 2 |
| 2c3 | 6 (9111) | 5 | 1 |
| 0c4 | 7 (count not reported) | 1 | 1 |
| 4c3 | 7 (count not reported) | 5 | 2 |
| 4c4 | > 7 (58.2% at 7) | 4 | 2 |
| 4b2 | 6 (16087) | > 8 (75.0%) | 2 |
| 4b5 | > 7 (48.1% at 7) | 2 | 1 |

- CORRECTS beef beans / Levi ("all reductions <= 4 find optimal about 75-80% on 2c3", D9086): 48.1% (+- 0.4) at <= 4 moves (140 reductions), 71.1% at <= 5 (1080 reductions); within +1 at <= 4: 78.8%.
- JTuu's T5744 sim (linear HTRs <= 7 + 1q reductions <= 4: 64.65%) uses the stricter one-quarter-turn finish; on that reading: Same definitions as JTuu (linear HTR within L moves, or a reduction of at most B moves to 4a1 4e followed by one quarter turn), uniform 2c3 2e, 25,000 states: an optimal is found by linear HTRs <= 7 or 1q reductions <= 4 in 55.3% (linear alone 38.1%, bounding alone 44.7%); <= 8 / <= 5: 80.3% (63.4%, 71.3%). JTuu's sim: 64.65% / 86.05%, 6-9 points more; his states were probably drawn differently (e.g. with the last DR move inverted).
- NEW: reducing to 2q needs far shorter reductions: 2q reductions of <= 3 moves reach an optimal in 60.4% of all DRs vs 14.1% for 1q.
- NEW: bounding reaches 80% optimal with reductions of <= 5 moves on 0c0, 4a2, 4a1; elsewhere it needs 6 (thousands to tens of thousands of reductions) or 7, or does not get there by 7. The budget-2 route checklist reaches 80% with a handful of classes on most subsets (table). A class and a reduction are not the same amount of work; the comparison is only in kind.

## Q9. FakeMMAP's reduction-length bound (T11501-T11504), with the section bounds

alpha_i computed per corner path (corners only, over every permutation following the path; 4a3 > 4b2 > 4a1 gives alpha = 0,3,1,0, FakeMMAP's example; out/q9_alpha.tsv). Sum of alpha over i with i and i+1 in S, as written. Per (state, path of a finish of length <= M) the reduction that finish needs against R. 25,000 states per subset; targets optimal, +1 and fixed M = 10, 11, 12 (out/q9_v2.tsv, counterexamples out/q9_v2_counterexamples.tsv).

- target opt: insufficient: literal 0.0%, without term 1 0.0%, exact model with C = shortest linear HTR of the subset 0.1%, with C = the state's shortest NISS HTR 0.0%. Mean R: literal 12.14, without term 1 11.14, exact 8.90; needed 6.96.
- target p1: insufficient: literal 0.0%, without term 1 0.0%, exact model with C = shortest linear HTR of the subset 0.0%, with C = the state's shortest NISS HTR 0.0%. Mean R: literal 13.59, without term 1 12.83, exact 10.37; needed 8.17.
- Not knowing the path (R = max over the subset's paths, with the state's own A and B): mean R without term 1 12.40, exact 10.57; insufficient 0.0% / 0.0%. Pruning: the longest reduction any optimal needed is 11.2 moves on average over subsets (25,000 states each), so R from the formula (12.4) asks for longer reductions than the empirical maximum and prunes nothing against it; the exact R (10.6) is about the empirical maximum. Against the reductions a solver can actually write (R <= 6-7), neither prunes: every extra move multiplies the reductions by about 7.5 (out/q8_bounding_v2.tsv).
- CORRECTS T11503 as written: with alpha summed over i with i and i+1 in S, the lower bound is wrong in 923 of 1,914,809 (state, path) cases (0.05%; 0c4, 4c4, 4b2, 4c3; out/q9_t11503_examples.tsv; witness W13). Summing the section shared by windows i and i+1 (alpha_(i+1)) instead makes every lower bound valid and keeps R sufficient (0 violations): that is probably what was meant.
- T11503 lower bounds as written (after every reduction shorter than the one the optimal needs failed): valid in 99.9%; better than the trivial M >= A + alpha_N, B + alpha_0 in 75.3% (exact model 88.7%); reach the optimum itself in 5.3%.
- C as "the shortest HTR in the subset" must be the shortest NISS HTR, not linear: a linear C makes the model wrong (W10: 0c0 2e, optimal 7 with a 4-move NISS HTR, below the subset's linear minimum 5).

rodneykinney's table (T11512), "reduce to 1q in at most R moves", per subset x edges and target M, worst case over the subset's paths with A = B = the subset's shortest linear HTR (nothing read off the DR), formula without term 1 (C = shortest linear HTR, as FakeMMAP defined it) / exact model (C = shortest NISS HTR seen in the subset); then the mean with the DR's own A, B; and what was actually needed (90th percentile / max). Full table: out/q9_rodney_table.tsv. M = 12 rows:

| subset | R (formula) | R (exact) | mean R, own A/B (formula / exact) | needed p90 / max |
|---|---|---|---|---|
| 0c0 0e | 13 | 10 | 13.00 / 10.00 | 1 / 8 |
| 0c0 2e | 11 | 10 | 11.00 / 10.00 | 6 / 9 |
| 0c0 4e | 11 | 9 | 11.00 / 9.00 | 7 / 9 |
| 0c0 6e | 10 | 9 | 10.00 / 9.00 | 7 / 9 |
| 0c0 8e | 11 | 9 | 11.00 / 9.00 | 4 / 7 |
| 2c5 0e | 10 | 9 | 10.00 / 9.00 | 8 / 8 |
| 2c5 2e | 10 | 9 | 10.00 / 9.00 | 8 / 8 |
| 2c5 4e | 10 | 9 | 10.00 / 9.00 | 8 / 8 |
| 2c5 6e | 10 | 9 | 10.00 / 9.00 | 8 / 8 |
| 2c5 8e | 10 | 9 | 10.00 / 9.00 | 8 / 8 |
| 2c4 0e | 10 | 9 | 10.00 / 9.00 | 7 / 9 |
| 2c4 2e | 10 | 9 | 10.00 / 9.00 | 7 / 9 |
| 2c4 4e | 10 | 9 | 10.00 / 9.00 | 7 / 9 |
| 2c4 6e | 10 | 9 | 10.00 / 9.00 | 7 / 9 |
| 2c4 8e | 10 | 9 | 10.00 / 9.00 | 7 / 8 |
| 0c3 0e | 10 | 9 | 10.00 / 9.00 | 4 / 4 |
| 0c3 2e | 10 | 9 | 10.00 / 9.00 | 5 / 7 |
| 0c3 4e | 10 | 9 | 10.00 / 9.00 | 4 / 7 |
| 0c3 6e | 10 | 9 | 10.00 / 9.00 | 5 / 7 |
| 0c3 8e | 10 | 9 | 10.00 / 9.00 | 4 / 4 |
| 4a2 0e | 10 | 9 | 10.00 / 9.00 | 7 / 8 |
| 4a2 2e | 10 | 9 | 10.00 / 9.00 | 7 / 9 |
| 4a2 4e | 11 | 10 | 11.00 / 10.00 | 6 / 9 |
| 4a1 0e | 11 | 9 | 11.00 / 9.00 | 8 / 9 |
| 4a1 2e | 11 | 9 | 11.00 / 9.00 | 6 / 8 |
| 4a1 4e | 13 | 9 | 13.00 / 9.00 | 6 / 8 |
| 2c3 0e | 10 | 9 | 10.00 / 9.00 | 8 / 8 |
| 2c3 2e | 11 | 9 | 11.00 / 9.00 | 6 / 8 |
| 2c3 4e | 11 | 9 | 11.00 / 9.00 | 7 / 8 |
| 2c3 6e | 11 | 9 | 11.00 / 9.00 | 7 / 8 |
| 2c3 8e | 10 | 9 | 10.00 / 9.00 | 8 / 8 |
| 0c4 0e | 10 | 9 | 10.00 / 9.00 | 7 / 9 |
| 0c4 2e | 10 | 9 | 10.00 / 9.00 | 7 / 9 |
| 0c4 4e | 10 | 9 | 10.00 / 9.00 | 7 / 9 |
| 0c4 6e | 10 | 9 | 10.00 / 9.00 | 8 / 9 |
| 0c4 8e | 9 | 9 | 9.00 / 9.00 | 5 / 8 |
| 4c3 0e | 10 | 9 | 10.00 / 9.00 | 7 / 8 |
| 4c3 2e | 11 | 9 | 11.00 / 9.00 | 7 / 8 |
| 4c3 4e | 11 | 9 | 11.00 / 9.00 | 7 / 8 |
| 4c4 0e | 10 | 9 | 9.51 / 9.00 | 8 / 8 |
| 4c4 2e | 10 | 9 | 10.00 / 9.00 | 8 / 9 |
| 4c4 4e | 10 | 9 | 10.00 / 9.00 | 8 / 9 |
| 4b2 0e | 11 | 9 | 11.00 / 9.00 | 7 / 9 |
| 4b2 2e | 12 | 9 | 12.00 / 9.00 | 6 / 9 |
| 4b2 4e | 11 | 9 | 11.00 / 9.00 | 7 / 9 |
| 4b5 0e | 10 | 9 | 10.00 / 9.00 | 8 / 8 |
| 4b5 2e | 10 | 9 | 10.00 / 9.00 | 8 / 8 |
| 4b5 4e | 10 | 9 | 10.00 / 9.00 | 8 / 8 |

## Half turns between quarter turns (C11, C13)

- C11: **PARTLY**. 2c4: some optimal ends with an R U2 R'-shape trigger (last two qts on one face, opposite directions, one half turn between) 41.4%, at either end 60.0%, a random optimal 13.8%; any qt-half turn-qt ending 73.7% (random optimal 50.8%); 2c3: some optimal ends with an R U2 R'-shape trigger (last two qts on one face, opposite directions, one half turn between) 34.8%, at either end 52.4%, a random optimal 11.7%; any qt-half turn-qt ending 69.5% (random optimal 46.2%). Either end with qt-half turn-qt: 2c4 91.1%, 2c3 89.1%. beef beans' 94.9% (2c4) / 72.5% (2c3) sit near the loose readings (any qt-half turn-qt), far above the strict R U2 R' shape (41% / 35% some optimal, 14% / 12% a random optimal); 25,000 states per subset.
- C13: **CORRECTS**. All DRs: the shortest-HTR optimal readings all need a switch after more than 2 moves in 28.2% of states (after more than 3: 12.5%); with HTRs up to 2 over the shortest allowed: 26.1% / 17.9%. Per subset in c11_c13.tsv.

## Witnesses

- W01 (4c3 4e): 4c3 checklist, first class: 4a3 > 4b2, switch, 4a1 > HTR finds the optimal (here with an HTR within 2 of the shortest). Scramble `L2 U2 F2 L2 D' F2 R2 D' L2 B2 U2 B2 D' R2`, optimal 14: `R2 D B2 U2 B2 L2 D R2 F2 D L2 F2 U2 L2`; route reading: `B2 R2 D' B2 R2 U2 R2 U' L2 D F2 U2 L2 F2` (normal first, normal `B2 R2 D'`, inverse `F2 L2 U2 F2 D' L2 U R2 U2 R2 B2`, HTR 10); replayed ok.
- W02 (2c4 4e): 2c4 checklist, first class: one qt to 2c3, switch, then 4b2 > 4a1 > HTR on the other side. Scramble `R2 F2 R2 D2 F2 D F2 D R2 U' L2 D F2 U2`, optimal 14: `U2 F2 D' L2 U R2 D' F2 D' F2 D2 R2 F2 R2`; route reading: `U2 F2 D' L2 U R2 D' F2 D' F2 D2 R2 F2 R2` (inverse first, normal `U2 F2 D' L2 U R2 D' F2`, inverse `R2 F2 R2 D2 F2 D`, HTR 13); replayed ok.
- W03 (4b2 4e): 4b2 4e: regress to 2c3, switch (Yura's step 2 / Zagros step 5). Scramble `B2 L2 U F2 D' R2 U L2 B2 L2 D2 B2 R2 D'`, optimal 14: `D R2 B2 D2 L2 B2 L2 U' R2 D F2 U' L2 B2`; route reading: `D R2 B2 D2 L2 B2 L2 U' R2 D F2 U' L2 B2` (normal first, normal `D`, inverse `B2 L2 U F2 D' R2 U L2 B2 L2 D2 B2 R2`, HTR 8); replayed ok.
- W04 (4b2 4e): 4b2 4e where no optimal finish uses 2 quarter turns (63.7% of 4b2 4e): the 2qt route 4b2 4e > 4a1 4e > HTR only gives optimal + 1 or worse. Scramble `F2 D F2 D L2 D2 L2 F2 L2 D L2 U`, optimal 12: `U' L2 D' L2 F2 L2 D2 L2 D' F2 D' F2`; replayed ok.
- W05 (2c3 2e): a 2c3 2e whose every optimal finish needs an HTR of 9+ moves in every NISS reading (65% of all DRs are like this; context for C12). Scramble `U2 L2 U F2 L2 R2 U' B2 R2 U' L2 U2 B2`, optimal 13: `B2 U2 L2 U R2 B2 U R2 L2 F2 U' L2 U2`; replayed ok.
- W06 (4b2 2e): Last DR move turned the other way (X -> X R2) gives a finish one move shorter (32.5% of DRs; Yura said 1/6). Scramble `R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U`, optimal 13: `U' B2 D2 R2 B2 D' L2 D' R2 F2 R2 D' R2`; replayed ok.
- W07 (4a1 4e): 4a1 4e can need 17 moves (C56 said 15); exact count 32 of 286,654,464 4a1 4e states. Scramble `B2 R2 U B2 F2 R2 B2 F2 R2 U F2 R2 D' U' F2 R2 D'`, optimal 17: `D R2 F2 U D R2 F2 U' R2 F2 B2 R2 F2 B2 U' R2 B2`; replayed ok.
- W08 (4c4 0e): 4c4 0e has linear HTRs of 10 moves (C51 said the minimum is 11). Scramble `D F2 R2 U2 B2 U' F2 U' F2 U L2 B2 U' R2 U'`, optimal 15: `U R2 U B2 L2 U' F2 U F2 U B2 U2 R2 F2 D'`; replayed ok.
- W09 (0c3 4e): The longest shortest linear HTR is 13 moves (Daichi T11594 right, Lewis T4100's 12 wrong). Scramble `B2 D L2 B2 U' L2 D F2 D' F2 U' L2 D R2 U`, optimal 15: `U' R2 D' L2 U F2 D F2 D' L2 U B2 L2 D' B2`; replayed ok.
- W10 (0c0 2e): FakeMMAP's C (shortest HTR in the subset) is not a bound on NISS HTRs: this 0c0 2e state (shortest linear HTR in 0c0 2e: 5) has an optimal 7-move finish whose NISS reading reaches HTR in 4. Scramble `F2 U' B2 R2 B2 U R2`, optimal 7: `R2 U' B2 R2 B2 U F2`; replayed ok.
- W11 (4b2 0e): 4b2 0e whose optimal goes through 4c3 (C04: 4%; ours 6% with a random optimal). Scramble `U' B2 D2 F2 U' B2 F2 L2 B2 U2 F2 U' L2 U'`, optimal 14: `U L2 U F2 U2 B2 L2 F2 B2 U F2 D2 B2 U`; route reading: `U L2 U F2 U2 B2 L2 F2 B2 U F2 D2 B2 U` (normal first, normal `U`, inverse `U' B2 D2 F2 U' B2 F2 L2 B2 U2 F2 U' L2`, HTR 13); replayed ok.
- W12 (2c3 2e): C13 corrected: a 2c3 2e whose shortest HTR among all readings of all optimal finishes needs a NISS switch after 4+ moves (28% of DRs need a switch after more than 2 moves for their shortest optimal HTR). Scramble `F2 U' L2 U' F2 R2 F2 L2 U F2 D2 B2`, optimal 12: `B2 D2 F2 U' L2 F2 R2 F2 U L2 U F2`; replayed ok.
- W13 (0c4 0e): T11503 lower bound as written (alpha_i summed over i with i, i+1 in S) is invalid here: this 0c4 0e has optimal 14 with a finish on 0c4 > 4a3 > 4b2 > 4a1 > HTR, sections 2,1,3,1,3, shortest 1q reduction 9, while the bound with R' = 9 gives M >= 15 (S = {0,2,3} adds alpha_2 = 3); summing the shared section alpha_(i+1) instead gives 14. Scramble `D2 F2 L2 U' B2 U' L2 U2 B2 U' L2 D R2 D2`, optimal 14: `D2 R2 D' L2 U B2 U2 L2 U B2 U L2 F2 D2`; replayed ok.

## Run times and memory

See research/README.md.

