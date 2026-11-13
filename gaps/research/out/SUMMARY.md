# Two data gaps in the DR studies: real DRs, and finishes that break DR

The published studies state two limits themselves (judging-a-dr WRITEUP section 13; htr-routes WRITEUP, "Not covered"):
every per-subset number weights DR states uniformly, and "optimal" means the best finish in DR moves (U, D, R2, L2, F2,
B2). This folder measures both. Code in `research/src`, the steps in `research/run_all.sh`, every table behind this
page in `research/out`. Built by `src/summary.py`.

## 1. The short version

- **The DRs you actually reach behave like uniform DRs.** 10,000 uniformly random scrambles; every EO-first DR of
  at most 11 moves, listed exactly the way judging-a-dr's examples page lists them (cubelib-cli, EO of at most 5 on
  normal, inverse or with NISS, then DR on either side): 6,840,923 DRs. Corner-subset shares are within 0.4 points
  of uniform, and each corner subset's mean optimal finish is within 0.05 moves of the exact uniform mean.
- **Every htr-routes headline survives.** Run through htr-routes' own code on these DRs, the checklist shares,
  hand-checklist grades, bounding shares, linear vs NISS HTR and "optimal through a shortest HTR" all move by under
  1 point per corner subset. The exceptions: 0c0 (0.5% of DRs), whose first checklist class finds 39-40% instead
  of 42.3%, and, with each DR counted once, 0c3's "NISS HTR 2+ shorter than linear" (50.1 ± 0.8% against 52.4%;
  52.0 ± 0.6% with each scramble once). Same first class on every corner subset, same first three in the same order on 11 of 12, same subsets for
  bounding. **No recommendation changes.**
- **Why** (section 2.1): given what the EO and DR search looks at, the rest of the cube is uniformly random, so each
  DR found is uniform inside the class of states that information allows. What does shift is the mix of bad-edge
  counts inside a corner subset: weighting each scramble once, 0e cells are 10-40% rarer than uniform and 6e cells
  up to 15% more common. Those cells are small, so pooled numbers hardly move.
- **This corrects two sentences**: judging-a-dr's "Real DRs aren't uniform across subsets" and htr-routes' "Real
  DRs come from EOs and triggers and are not uniform within a subset". Uniform numbers, including the "all DRs" ones,
  are good numbers for real DRs (section 4).
- **Breaking DR rarely pays.** On 48,000 uniform DR states (1,000 per subset x edges) solved optimally with all 18
  face turns by nissy, a finish shorter than the DR-move optimum exists on 4.3% ± 0.1% of DRs, by one move in 90% of those cases (weighted by subset size; 83.5% of the unweighted sample, where 0e cells are oversampled);
  mean gain 0.048 moves. For DRs whose DR-move optimum is 12 or less (the ones a solver finishes) it is
  1.1%; it climbs only for long finishes (9% at 15, 36% at 16). Exceptions by cell: 0c3 0e (36%), 0c4 0e (26%),
  0c0 0e (21%, up to 4 moves: `R L F2 B2 R' L' D2` solves a DR whose DR-move optimum is 11). On the real population the share is 4.2% ± 0.2% with each DR once and 3.9% ± 0.4% with each scramble once (uniform 4.3%).

## 2. Gap 1: the DRs solvers actually reach

### 2.0 Population, weightings, sample sizes

- **Scrambles**: the first 10,000 states of eo-to-dr's `out/scrambles.txt` (`eodrtools mkscr 50000 2026`:
  uniformly random states; adjacent turns of one face merged with eo-to-dr's `canon.py`). Not nissy's `scramble`,
  which is biased (eo-to-dr README).
- **DRs**: `cubelib-cli solve -s "EO[niss=always;max=5] > DR[niss=before;max=11]" -q 0 -M 11 -f detailed`, the route
  definition of judging-a-dr's examples page (`many_examples.py`): an EO on any axis with NISS anywhere in it, then DR
  on normal or on inverse without breaking that EO, on either of the other two axes. cubelib lists no EO longer than 5
  moves (with `max=8`, as the examples page wrote it, the lists are identical: checked on 20 scrambles), so this is
  exactly what that page used. Each DR is the state as written, the quarter turns among each side's last moves made
  clockwise (the page's convention: of a DR ending `F` and its twin ending `F'` only one is kept), turned so its axis
  is U/D, and deduplicated per scramble by state (the first listing, shortest first, gives the moves).
- **Which side**: the DR state on the side the DR step is written on. DR step on normal: I^-1 S N (the state as
  written); on inverse: N^-1 S^-1 I (computed separately on stickers and checked to be the inverse permutation).
  50.4% of the DRs end on inverse.
- **Size**: 6,840,923 DRs of at most 11 moves: 684 per scramble on average, median 320, one scramble 98,536.
  704,669 of at most 10 moves (9,850 scrambles have one). By length: 4: 1, 5: 5, 6: 71, 7: 682, 8: 6,616,
  9: 64,470, 10: 632,824, 11: 6,136,254.
- **Weightings**, each reported:
  - `dr11` / `dr10`: every DR found counts once (a scramble with 3,000 DRs weighs 3,000 times one with one DR);
  - `scr11` / `scr10`: every scramble counts once, split equally over its DRs of at most 11 (10) moves.
  A few scrambles hold most DRs, so the two differ in precision more than in value. `scr` is the better model of
  "the DR a solver gets", `dr` of "a DR someone wrote down".
- **Standard errors** are clustered by scramble (DRs of one scramble are not independent): linearised ratio
  estimator with a K/(K-1) correction. Uniform SEs: each state its own cluster. A greedy class choice is taken as
  fixed when its share's SE is computed.
- **Checks**: 1,000 random DRs of the population: the coordinates read back by judging-a-dr's `drtools read --quick`
  give the same subset and optimum as the gaps `htrtools label`, and the first optimal finish, turned back to the
  cube's frame, solves the scramble on stickers in the stated number of moves, on both sides: 0 failures
  (`src/check_pop.py`).

Part (a) uses every DR. Part (b) runs htr-routes' code on a sample: per subset x edges up to 25,000 DRs drawn
uniformly from that cell's pooled DRs (878,048 in all; all of them in the 13 cells with fewer), each carrying the
Horvitz-Thompson weight of every population (population weight x cell pool / cell sample). The states go through a
fork of `htrtools` whose only change is that states come from a list (`GAPS_STATES`; checked: 80 states give
identical route sets, key by key, from the list and from the uniform draw), then through htr-routes' own
`common.py`, `checklist_cost.py` (`member`, `greedy`) and `grade.py` (`checklists`, `P`), imported from their
folder, with one weight per state in place of `SIZE[s] / n`. The same code on htr-routes' uniform states reproduces
its published checklist, grade, bounding and Q3 numbers to the last digit (rows `uniform` in out/b_*.tsv).

### 2.1 Why the population is so close to uniform

Fix the coordinates of a scramble that the EO and DR search can see: edge and corner orientation for each axis, and
which slice each edge sits in for each axis. cubelib's list of EOs, DRs and NISS splits depends on nothing else,
and given those coordinates the scramble's remaining permutation is uniformly random. For a fixed move sequence the
map from scramble to DR state is a bijection, so each DR found is uniform over the DR states compatible with what
the search saw. Counting a scramble's DRs, deduplicating, choosing the side and weighting by scramble also use only
that information. That information does fix part of the HTR structure (which tetrad each corner is in, which edges
belong to the M or S slice for the other axes), so the bad-edge mix and similar classes can differ from uniform;
inside such a class every DR state is equally likely. This is an argument, not a proof (nothing here is in Lean);
the measurements agree with it.

### 2.2 (a) Subset shares and the optimal finish

Corner subsets: share of the population (± SE) and mean optimal DR finish. Uniform = exact over all
19,508,428,800 DR states.

| corner subset | share: uniform | dr11 | scr11 | dr10 | scr10 | mean optimal: uniform | dr11 | scr11 | dr10 | scr10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0c0 | 0.48% | 0.51 ± 0.03 | 0.48 ± 0.01 | 0.53 ± 0.06 | 0.47 ± 0.03 | 12.278 | 12.293 ± 0.040 | 12.327 ± 0.016 | 12.281 ± 0.081 | 12.406 ± 0.058 |
| 2c5 | 7.62% | 7.50 ± 0.11 | 7.49 ± 0.05 | 7.50 ± 0.20 | 7.52 ± 0.11 | 14.327 | 14.317 ± 0.005 | 14.332 ± 0.003 | 14.307 ± 0.010 | 14.334 ± 0.010 |
| 2c4 | 22.86% | 22.73 ± 0.16 | 22.98 ± 0.08 | 22.60 ± 0.31 | 23.15 ± 0.18 | 13.647 | 13.647 ± 0.003 | 13.660 ± 0.002 | 13.645 ± 0.006 | 13.656 ± 0.006 |
| 0c3 | 1.43% | 1.43 ± 0.05 | 1.46 ± 0.03 | 1.47 ± 0.08 | 1.50 ± 0.06 | 14.460 | 14.470 ± 0.009 | 14.460 ± 0.009 | 14.480 ± 0.018 | 14.443 ± 0.033 |
| 4a2 | 2.86% | 2.88 ± 0.07 | 2.82 ± 0.03 | 2.90 ± 0.12 | 2.89 ± 0.07 | 13.348 | 13.335 ± 0.013 | 13.355 ± 0.008 | 13.312 ± 0.026 | 13.347 ± 0.023 |
| 4a1 | 2.86% | 2.96 ± 0.08 | 2.90 ± 0.03 | 3.03 ± 0.15 | 3.03 ± 0.08 | 12.419 | 12.404 ± 0.009 | 12.435 ± 0.007 | 12.398 ± 0.018 | 12.466 ± 0.021 |
| 2c3 | 15.24% | 15.41 ± 0.19 | 15.24 ± 0.07 | 15.37 ± 0.37 | 15.03 ± 0.15 | 12.925 | 12.913 ± 0.004 | 12.930 ± 0.003 | 12.906 ± 0.006 | 12.927 ± 0.008 |
| 0c4 | 0.95% | 0.93 ± 0.03 | 0.96 ± 0.02 | 0.94 ± 0.07 | 1.00 ± 0.04 | 13.674 | 13.679 ± 0.008 | 13.679 ± 0.008 | 13.692 ± 0.021 | 13.709 ± 0.033 |
| 4c3 | 11.43% | 11.27 ± 0.11 | 11.40 ± 0.06 | 11.14 ± 0.20 | 11.41 ± 0.14 | 13.487 | 13.483 ± 0.003 | 13.488 ± 0.003 | 13.481 ± 0.007 | 13.494 ± 0.009 |
| 4c4 | 11.43% | 11.24 ± 0.11 | 11.39 ± 0.06 | 11.13 ± 0.20 | 11.30 ± 0.13 | 14.403 | 14.405 ± 0.002 | 14.411 ± 0.002 | 14.403 ± 0.005 | 14.412 ± 0.007 |
| 4b2 | 11.43% | 11.84 ± 0.18 | 11.44 ± 0.06 | 12.19 ± 0.38 | 11.37 ± 0.13 | 12.680 | 12.676 ± 0.006 | 12.693 ± 0.003 | 12.671 ± 0.013 | 12.688 ± 0.009 |
| 4b5 | 11.43% | 11.29 ± 0.12 | 11.44 ± 0.06 | 11.20 ± 0.22 | 11.33 ± 0.13 | 14.279 | 14.280 ± 0.002 | 14.284 ± 0.002 | 14.285 ± 0.004 | 14.302 ± 0.007 |

Edge mix inside each corner subset: share of the corner subset's DRs with each bad-edge count (uniform exact,
real ± SE):

| subset | uniform | dr11 | scr11 | dr10 | scr10 |
|---|---|---|---|---|---|
| 0c0 0e | 1.5 | 2.2 ± 1.0 | 0.8 ± 0.2 | 3.2 ± 2.1 | 1.3 ± 0.6 |
| 0c0 2e | 22.9 | 20.0 ± 1.0 | 21.4 ± 1.1 | 16.1 ± 1.5 | 19.2 ± 2.7 |
| 0c0 4e | 51.5 | 49.6 ± 2.7 | 49.6 ± 1.5 | 49.4 ± 5.2 | 49.7 ± 4.2 |
| 0c0 6e | 22.9 | 26.9 ± 4.1 | 26.7 ± 1.5 | 29.8 ± 8.1 | 28.8 ± 3.8 |
| 0c0 8e | 1.5 | 1.4 ± 0.2 | 1.5 ± 0.2 | 1.5 ± 0.4 | 1.1 ± 0.4 |
| 2c5 0e | 1.4 | 1.6 ± 0.2 | 1.3 ± 0.1 | 1.6 ± 0.4 | 1.6 ± 0.2 |
| 2c5 2e | 22.9 | 23.0 ± 0.5 | 22.4 ± 0.3 | 23.0 ± 0.9 | 21.9 ± 0.7 |
| 2c5 4e | 51.4 | 51.5 ± 1.0 | 51.3 ± 0.4 | 52.1 ± 2.0 | 52.1 ± 1.1 |
| 2c5 6e | 22.9 | 22.4 ± 0.4 | 23.5 ± 0.3 | 21.7 ± 0.7 | 22.9 ± 0.7 |
| 2c5 8e | 1.4 | 1.5 ± 0.1 | 1.6 ± 0.1 | 1.6 ± 0.2 | 1.5 ± 0.2 |
| 2c4 0e | 1.4 | 1.5 ± 0.1 | 1.2 ± 0.0 | 1.5 ± 0.2 | 1.1 ± 0.1 |
| 2c4 2e | 22.9 | 22.2 ± 0.3 | 21.8 ± 0.2 | 21.7 ± 0.5 | 21.4 ± 0.4 |
| 2c4 4e | 51.4 | 51.7 ± 0.5 | 51.8 ± 0.3 | 51.9 ± 1.0 | 52.0 ± 0.6 |
| 2c4 6e | 22.9 | 23.1 ± 0.4 | 23.7 ± 0.2 | 23.5 ± 0.7 | 23.8 ± 0.4 |
| 2c4 8e | 1.4 | 1.4 ± 0.1 | 1.5 ± 0.1 | 1.5 ± 0.2 | 1.7 ± 0.1 |
| 0c3 0e | 1.4 | 1.3 ± 0.1 | 1.0 ± 0.1 | 1.4 ± 0.2 | 1.0 ± 0.3 |
| 0c3 2e | 22.9 | 23.4 ± 1.7 | 21.4 ± 0.8 | 24.4 ± 3.5 | 21.7 ± 1.7 |
| 0c3 4e | 51.4 | 48.7 ± 1.3 | 51.0 ± 1.1 | 47.0 ± 2.2 | 53.0 ± 2.7 |
| 0c3 6e | 22.9 | 25.2 ± 1.9 | 25.3 ± 0.8 | 25.9 ± 3.1 | 22.7 ± 1.7 |
| 0c3 8e | 1.4 | 1.3 ± 0.3 | 1.4 ± 0.1 | 1.3 ± 0.4 | 1.6 ± 0.5 |
| 4a2 0e | 2.9 | 2.7 ± 0.2 | 2.6 ± 0.1 | 2.7 ± 0.3 | 2.4 ± 0.3 |
| 4a2 2e | 45.7 | 45.4 ± 1.2 | 45.6 ± 0.7 | 45.2 ± 2.3 | 45.5 ± 1.6 |
| 4a2 4e | 51.4 | 51.9 ± 1.6 | 51.8 ± 0.7 | 52.1 ± 3.0 | 52.1 ± 1.8 |
| 4a1 0e | 2.9 | 2.7 ± 0.2 | 2.7 ± 0.1 | 2.5 ± 0.4 | 2.7 ± 0.4 |
| 4a1 2e | 45.7 | 46.6 ± 1.9 | 46.6 ± 0.7 | 48.0 ± 3.9 | 48.3 ± 1.9 |
| 4a1 4e | 51.4 | 50.6 ± 1.2 | 50.8 ± 0.8 | 49.5 ± 2.0 | 49.0 ± 1.7 |
| 2c3 0e | 1.4 | 1.3 ± 0.0 | 1.2 ± 0.0 | 1.2 ± 0.1 | 1.1 ± 0.1 |
| 2c3 2e | 22.9 | 23.0 ± 0.4 | 22.3 ± 0.2 | 22.8 ± 0.7 | 22.0 ± 0.5 |
| 2c3 4e | 51.4 | 52.3 ± 1.2 | 51.6 ± 0.3 | 53.4 ± 2.4 | 52.7 ± 0.8 |
| 2c3 6e | 22.9 | 22.1 ± 0.3 | 23.4 ± 0.2 | 21.3 ± 0.6 | 22.6 ± 0.5 |
| 2c3 8e | 1.4 | 1.4 ± 0.0 | 1.5 ± 0.1 | 1.3 ± 0.1 | 1.6 ± 0.1 |
| 0c4 0e | 1.5 | 1.4 ± 0.2 | 0.9 ± 0.1 | 1.2 ± 0.4 | 0.4 ± 0.1 |
| 0c4 2e | 22.9 | 22.8 ± 1.6 | 21.1 ± 0.8 | 23.6 ± 3.5 | 19.9 ± 1.6 |
| 0c4 4e | 51.5 | 49.7 ± 1.6 | 51.8 ± 1.4 | 49.1 ± 3.2 | 51.0 ± 3.3 |
| 0c4 6e | 22.9 | 24.8 ± 2.4 | 24.6 ± 0.8 | 25.2 ± 4.9 | 27.4 ± 2.5 |
| 0c4 8e | 1.5 | 1.3 ± 0.1 | 1.6 ± 0.1 | 0.9 ± 0.2 | 1.2 ± 0.4 |
| 4c3 0e | 2.9 | 2.8 ± 0.1 | 2.8 ± 0.1 | 2.7 ± 0.2 | 2.6 ± 0.2 |
| 4c3 2e | 45.7 | 45.3 ± 0.6 | 45.5 ± 0.3 | 44.9 ± 1.1 | 45.8 ± 0.8 |
| 4c3 4e | 51.4 | 51.9 ± 0.7 | 51.7 ± 0.4 | 52.4 ± 1.2 | 51.6 ± 0.9 |
| 4c4 0e | 2.9 | 2.8 ± 0.1 | 2.8 ± 0.1 | 2.7 ± 0.2 | 2.6 ± 0.2 |
| 4c4 2e | 45.7 | 45.6 ± 0.6 | 45.8 ± 0.3 | 45.5 ± 1.1 | 45.1 ± 0.7 |
| 4c4 4e | 51.4 | 51.7 ± 0.6 | 51.4 ± 0.4 | 51.8 ± 1.0 | 52.4 ± 0.8 |
| 4b2 0e | 2.9 | 2.6 ± 0.1 | 2.8 ± 0.1 | 2.3 ± 0.1 | 2.9 ± 0.2 |
| 4b2 2e | 45.7 | 46.1 ± 1.1 | 45.6 ± 0.3 | 46.5 ± 2.4 | 45.6 ± 0.8 |
| 4b2 4e | 51.4 | 51.3 ± 0.8 | 51.6 ± 0.4 | 51.2 ± 1.5 | 51.6 ± 0.8 |
| 4b5 0e | 2.9 | 2.9 ± 0.1 | 2.9 ± 0.1 | 2.8 ± 0.2 | 2.7 ± 0.2 |
| 4b5 2e | 45.7 | 45.9 ± 0.6 | 45.2 ± 0.3 | 46.0 ± 1.2 | 44.4 ± 0.8 |
| 4b5 4e | 51.4 | 51.3 ± 0.7 | 51.9 ± 0.4 | 51.2 ± 1.2 | 52.9 ± 0.9 |

- Per subset x edges (out/a_subsets.tsv, out/cmp_subsets.tsv): the mean optimal is within 0.05 moves of uniform in
  every cell with more than 1,000 DRs. The one large gap is 0c0 0e with each DR once (755 DRs from a few
  scrambles): 9.47 ± 0.12 against 9.95; with each scramble once 9.88 ± 0.11.
- The whole optimal-finish distribution per corner subset (out/a_depth.tsv) is within 0.5 points of uniform in
  every length, except 0c0 (1.1 points with each DR once, 2.0 with each scramble once).
- Shares finishing in 10 / 11 / 12 or less per subset: out/a_subsets.tsv. The largest corner-subset gap is 0c0 in
  at most 11: 19.3 ± 0.6% (each scramble once) against 20.6%.

### 2.3 (b) htr-routes' headline outputs, uniform vs real

Same class definitions, same HTR budget (at most 2 over the state's shortest NISS HTR), same code. Uniform =
htr-routes' 25,000 states per subset x edges (bounding: its first 4,000). Every cell, with SEs and flags
(> 2 points, > 2 combined SE), is in out/cmp_checklist.tsv, cmp_grades.tsv, cmp_bounding.tsv, cmp_q3.tsv,
cmp_subsets.tsv.

**Checklists (htr-routes Q2), budget 2, greedy on each population.** Cumulative share finding an optimal after 1 / 2
/ 3 classes, then the same three classes within +1 (± SE):

| subset | after 1 / 2 / 3, +1 after 3: uniform | real, each DR once (dr11) | real, each scramble once (scr11) | same 3 classes in order (dr11 / scr11) |
|---|---|---|---|---|
| 0c0 | 42.3 ± 0.2 / 55.9 ± 0.2 / 60.9 ± 0.2 / 86.4 ± 0.1 | 39.1 ± 1.2 / 53.6 ± 0.8 / 59.0 ± 0.6 / 85.3 ± 0.8 | 40.2 ± 0.7 / 54.8 ± 0.7 / 60.1 ± 0.6 / 86.6 ± 0.4 | yes / yes |
| 2c5 | 72.8 ± 0.2 / 85.5 ± 0.1 / 91.4 ± 0.1 / 98.9 ± 0.0 | 73.1 ± 0.2 / 85.7 ± 0.1 / 91.6 ± 0.1 / 99.0 ± 0.0 | 73.1 ± 0.4 / 85.4 ± 0.3 / 91.3 ± 0.2 / 99.1 ± 0.1 | yes / yes |
| 2c4 | 66.0 ± 0.2 / 83.5 ± 0.1 / 88.4 ± 0.1 / 98.7 ± 0.0 | 65.9 ± 0.2 / 83.8 ± 0.1 / 88.5 ± 0.1 / 98.7 ± 0.1 | 66.1 ± 0.4 / 83.6 ± 0.3 / 88.4 ± 0.2 / 98.7 ± 0.1 | yes / yes |
| 0c3 | 74.4 ± 0.2 / 88.8 ± 0.1 / 89.3 ± 0.1 / 99.1 ± 0.0 | 75.3 ± 0.3 / 89.2 ± 0.2 / 89.7 ± 0.1 / 99.1 ± 0.0 | 74.8 ± 0.4 / 89.3 ± 0.3 / 89.8 ± 0.3 / 98.9 ± 0.2 | yes / yes |
| 4a2 | 41.6 ± 0.2 / 64.1 ± 0.2 / 73.2 ± 0.2 / 90.8 ± 0.1 | 41.2 ± 0.3 / 63.8 ± 0.3 / 72.7 ± 0.3 / 90.6 ± 0.2 | 41.6 ± 0.5 / 64.1 ± 0.5 / 73.0 ± 0.4 / 91.0 ± 0.2 | yes / yes |
| 4a1 | 29.3 ± 0.2 / 44.8 ± 0.2 / 58.0 ± 0.2 / 84.3 ± 0.2 | 29.4 ± 0.4 / 44.6 ± 0.3 / 58.0 ± 0.4 / 84.1 ± 0.3 | 29.7 ± 0.4 / 45.0 ± 0.5 / 58.0 ± 0.5 / 84.6 ± 0.3 | yes / yes |
| 2c3 | 53.5 ± 0.2 / 75.7 ± 0.2 / 78.0 ± 0.2 / 96.1 ± 0.1 | 53.7 ± 0.2 / 75.5 ± 0.2 / 77.7 ± 0.2 / 96.0 ± 0.1 | 53.8 ± 0.4 / 75.4 ± 0.4 / 77.8 ± 0.3 / 96.1 ± 0.1 | yes / yes |
| 0c4 | 83.8 ± 0.1 / 85.1 ± 0.1 / 86.3 ± 0.1 / 97.6 ± 0.1 | 83.2 ± 0.2 / 84.6 ± 0.2 / 85.8 ± 0.2 / 97.5 ± 0.1 | 83.9 ± 0.3 / 85.2 ± 0.3 / 86.4 ± 0.3 / 97.5 ± 0.1 | 1st same / 1st same |
| 4c3 | 64.3 ± 0.2 / 71.3 ± 0.2 / 75.0 ± 0.2 / 94.2 ± 0.1 | 64.4 ± 0.2 / 71.5 ± 0.2 / 75.0 ± 0.2 / 94.3 ± 0.1 | 63.9 ± 0.4 / 71.0 ± 0.4 / 74.8 ± 0.4 / 94.5 ± 0.2 | yes / yes |
| 4c4 | 68.1 ± 0.2 / 75.0 ± 0.2 / 78.4 ± 0.2 / 96.1 ± 0.1 | 68.2 ± 0.2 / 74.9 ± 0.2 / 78.2 ± 0.2 / 95.9 ± 0.1 | 68.2 ± 0.4 / 74.8 ± 0.4 / 78.2 ± 0.4 / 95.8 ± 0.2 | yes / yes |
| 4b2 | 37.6 ± 0.2 / 53.3 ± 0.2 / 62.6 ± 0.2 / 88.0 ± 0.1 | 37.8 ± 0.3 / 53.6 ± 0.2 / 62.8 ± 0.2 / 88.4 ± 0.2 | 37.9 ± 0.5 / 54.2 ± 0.5 / 63.2 ± 0.5 / 88.6 ± 0.3 | yes / yes |
| 4b5 | 64.7 ± 0.2 / 87.4 ± 0.1 / 93.7 ± 0.1 / 99.6 ± 0.0 | 64.7 ± 0.2 / 87.3 ± 0.1 / 93.8 ± 0.1 / 99.6 ± 0.0 | 64.4 ± 0.4 / 87.2 ± 0.3 / 93.7 ± 0.2 / 99.5 ± 0.1 | yes / yes |

- Flags over the 48 subset x edges and 12 corner subsets (4 numbers each, 240 per population): > 2 SE in 10.4%
  (dr11) and 4.2% (scr11) of cells, about chance once the heavy-tailed clusters are allowed for. > 2 points and
  > 2 SE together: 4 cells for dr11, 4 for scr11: 0c0 8e (first class 47.5 ± 2.7% against 53.5%, each DR once),
  0c3 0e (87.9 ± 1.1 against 85.5, each DR once), 2c3 0e (each scramble once: 43.4 ± 0.9 / 64.7 ± 0.9 / 73.1 ± 0.8
  against 46.3 / 67.0 / 75.1), and the 0c0 corner row.
- The uniform checklist's own three classes evaluated on the real states (rows "uniform classes" in
  out/b_checklist.tsv) stay within the same margins.
- Class order per subset x edges: the first class is the same on 46 of 48 cells for each 11-move weighting; the two
  changes are near-ties in tiny cells (0c0 0e, each DR once: `0c0 | ht` first instead of `0c0 > 4a1 > 0c0 | ht`;
  0c0 8e, each scramble once: `0c0 > 4a1 > 0c0` before `0c0 > 4a1 > (0c0)`). Second and third classes swap only
  where they were within about a point (out/cmp_checklist.tsv, column real_classes).
- Side finding: htr-routes' research summary (research/out/SUMMARY.md, Q2 table) labels its last column "the same
  three classes at optimal + 1", but prints the greedy checklist built *at* +1 (`summary.py` reads
  `checklist(g, '2', 'p1')`). The report's WRITEUP uses the same three classes (4a2 90.8%) and is right; the
  research summary's 4a2 91.8% and 0c3 99.2% are the +1 checklist (same three classes: 90.8%, 99.1%); its per-cell
  rows differ similarly (4a2 0e 68.4% printed, 68.2% for the same classes).

**Hand checklists (htr-routes Q6), budget 2, optimal**, cumulative per step (no limit and +1: out/b_grades.tsv):

| checklist | step | uniform | dr11 | scr11 | dr10 | scr10 |
|---|---|---|---|---|---|---|
| Zagros 4b2 order (D15884) | 1. S1+S2 linear 2qt 4b2 > 4a1 > HTR (normal or inverse) | 37.6 ± 0.2 | 37.8 ± 0.3 | 37.9 ± 0.5 | 38.5 ± 1.0 | 37.3 ± 1.8 |
| Zagros 4b2 order (D15884) | 2. S3 linear 4qt HTR of <= 8 moves | 45.4 ± 0.2 | 45.6 ± 0.3 | 45.4 ± 0.5 | 46.3 ± 0.9 | 45.7 ± 1.9 |
| Zagros 4b2 order (D15884) | 3. S4 reduce to 4a1, switch (4b2 > 4a1 > (HTR)) | 50.8 ± 0.2 | 51.0 ± 0.3 | 50.7 ± 0.5 | 51.7 ± 0.9 | 53.0 ± 1.9 |
| Zagros 4b2 order (D15884) | 4. S5 regress to 2c3, switch (4b2 > 2c3 > (...)) | 64.2 ± 0.2 | 64.3 ± 0.2 | 64.5 ± 0.4 | 65.0 ± 0.8 | 67.5 ± 1.6 |
| Zagros 4b2 order (D15884) | 5. S8 2+2: any 4qt route switching after the 2nd qt | 71.3 ± 0.2 | 71.3 ± 0.2 | 71.5 ± 0.4 | 71.6 ± 0.7 | 73.0 ± 1.5 |
| Zagros 4b2 order (D15884), 4b2 4e only | 1. S1+S2 linear 2qt 4b2 > 4a1 > HTR (normal or inverse) | 30.3 ± 0.3 | 30.1 ± 0.3 | 30.9 ± 0.8 | 30.2 ± 1.0 | 28.9 ± 2.5 |
| Zagros 4b2 order (D15884), 4b2 4e only | 2. S3 linear 4qt HTR of <= 8 moves | 40.8 ± 0.3 | 40.8 ± 0.3 | 41.1 ± 0.8 | 40.8 ± 1.0 | 41.7 ± 3.1 |
| Zagros 4b2 order (D15884), 4b2 4e only | 3. S4 reduce to 4a1, switch (4b2 > 4a1 > (HTR)) | 45.7 ± 0.3 | 45.6 ± 0.4 | 45.7 ± 0.8 | 45.9 ± 1.0 | 47.4 ± 3.0 |
| Zagros 4b2 order (D15884), 4b2 4e only | 4. S5 regress to 2c3, switch (4b2 > 2c3 > (...)) | 65.3 ± 0.3 | 65.3 ± 0.4 | 65.9 ± 0.7 | 66.0 ± 1.0 | 69.5 ± 2.3 |
| Zagros 4b2 order (D15884), 4b2 4e only | 5. S8 2+2: any 4qt route switching after the 2nd qt | 74.5 ± 0.3 | 74.4 ± 0.3 | 74.6 ± 0.6 | 75.1 ± 0.9 | 77.1 ± 1.9 |
| Yura 4b2 4e order (D6409-D6416) | 1. ~S1 linear 2qt trigger with <= 2 setup moves (HTR <= 6) | 8.6 ± 0.2 | 8.7 ± 0.2 | 8.8 ± 0.4 | 9.9 ± 0.7 | 8.7 ± 1.4 |
| Yura 4b2 4e order (D6409-D6416) | 2. S2 regress to 2c3 (2e or 4e), then 2c3 linear or switch (4qt) | 62.3 ± 0.3 | 62.4 ± 0.3 | 63.6 ± 0.7 | 64.0 ± 0.9 | 68.8 ± 2.3 |
| Yura 4b2 4e order (D6409-D6416) | 3. S3 reduce to 4a1 and switch | 72.9 ± 0.3 | 73.1 ± 0.3 | 73.8 ± 0.6 | 74.5 ± 0.9 | 78.1 ± 1.8 |
| rogo/Adri 4b2 4e order (D6422-D6424) | 1. ~S1 linear 2qt trigger with <= 2 setup moves (HTR <= 6) | 8.6 ± 0.2 | 8.7 ± 0.2 | 8.8 ± 0.4 | 9.9 ± 0.7 | 8.7 ± 1.4 |
| rogo/Adri 4b2 4e order (D6422-D6424) | 2. S3 reduce to 4a1 and switch | 26.1 ± 0.3 | 26.2 ± 0.3 | 25.7 ± 0.6 | 27.3 ± 1.0 | 25.6 ± 2.3 |
| Lewis 4a2 0e/2e list (T6743) | 1. S1 linear 2qt 4a2 > 4a1 4e > HTR | 13.3 ± 0.2 | 13.1 ± 0.2 | 12.7 ± 0.4 | 13.0 ± 0.7 | 13.6 ± 1.6 |
| Lewis 4a2 0e/2e list (T6743) | 2. S2 reduce to 4a1 4e, switch | 32.2 ± 0.3 | 31.7 ± 0.3 | 31.4 ± 0.6 | 31.7 ± 1.0 | 30.3 ± 2.0 |
| Lewis 4a2 0e/2e list (T6743) | 3. S3 4qt linear through 4a2 4e again (qt, slice, qt) | 37.7 ± 0.3 | 37.1 ± 0.4 | 36.8 ± 0.6 | 37.6 ± 1.1 | 38.3 ± 2.2 |
| Lewis 4a2 0e/2e list (T6743) | 4. S4 regress to 4b3 (2e/4e), switch, 4a3 > 4b2 > 4a1 | 52.7 ± 0.3 | 52.5 ± 0.4 | 52.5 ± 0.6 | 53.7 ± 1.1 | 52.9 ± 2.2 |
| Lewis 4a2 0e/2e list (T6743) | 5. S5 regress to 0c3, then 0c3 > 4a2 > 4a1 (linear or NISS) | 53.4 ± 0.3 | 53.1 ± 0.4 | 53.2 ± 0.6 | 54.4 ± 1.1 | 53.7 ± 2.2 |
| Jay/rodney 2c3 0e checks (T328-T344) | 1. ~2c3 0e: one qt to 4b2 4e, switch, 4a1 > HTR (Jay T328 / rodney T331-T344, prefix not restricted) | 46.3 ± 0.3 | 45.7 ± 0.5 | 43.4 ± 0.9 | 42.5 ± 1.5 | 42.2 ± 3.0 |
| Fanti 4b2 4e split (D10034), cumulative | 1. 2qt (4b2 > 4a1 > HTR, any switch) | 35.5 ± 0.3 | 35.2 ± 0.4 | 35.8 ± 0.8 | 35.7 ± 1.0 | 34.7 ± 2.8 |
| Fanti 4b2 4e split (D10034), cumulative | 2. 4qt via 2c3 | 77.8 ± 0.3 | 77.7 ± 0.3 | 78.4 ± 0.6 | 78.5 ± 0.9 | 80.9 ± 1.7 |
| Fanti 4b2 4e split (D10034), cumulative | 3. 4qt via 4a1 > 0c0 | 80.2 ± 0.2 | 80.3 ± 0.3 | 81.0 ± 0.5 | 81.2 ± 0.9 | 84.0 ± 1.5 |

Daichi's cheat sheet per subset x edges (budget 2): every cell within 1.3 points of uniform for the 11-move
weightings except 0c0 8e (each scramble once 75.0 ± 3.4% against 70.1%) and 4a2 0e (35.3 ± 1.5 against 37.6).
Out/cmp_grades.tsv has every cell.

**Bounding as stated (htr-routes Q8)**: share where some reduction to 1q / 2q of at most R moves, followed by the
optimal finish of the reduced state, gives an optimal finish (uniform / each DR once / each scramble once, ± SE):

| subset | q | R <= 3: uniform / dr11 / scr11 | R <= 4 | R <= 5 |
|---|---|---|---|---|
| 0c0 | 1q | 86.0 ± 0.3 / 86.0 ± 0.4 / 86.3 ± 0.4 | 91.5 ± 0.3 / 91.6 ± 0.4 / 91.5 ± 0.3 | 93.9 ± 0.2 / 93.8 ± 0.2 / 93.4 ± 0.3 |
| 0c0 | 2q | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 |
| 2c5 | 1q | 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 ± 0.0 | 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 ± 0.0 | 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 ± 0.0 |
| 2c5 | 2q | 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 ± 0.0 | 17.9 ± 0.4 / 18.4 ± 0.3 / 18.5 ± 0.3 | 67.9 ± 0.4 / 68.1 ± 0.2 / 68.2 ± 0.4 |
| 2c4 | 1q | 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 ± 0.0 | 3.5 ± 0.2 / 3.6 ± 0.1 / 3.5 ± 0.1 | 25.7 ± 0.4 / 26.2 ± 0.2 / 25.7 ± 0.3 |
| 2c4 | 2q | 46.5 ± 0.5 / 46.6 ± 0.2 / 46.4 ± 0.4 | 80.8 ± 0.4 / 80.3 ± 0.2 / 80.5 ± 0.3 | 94.8 ± 0.2 / 94.7 ± 0.1 / 94.9 ± 0.2 |
| 0c3 | 1q | 12.7 ± 0.3 / 12.0 ± 0.4 / 13.0 ± 0.4 | 35.0 ± 0.5 / 34.2 ± 0.6 / 35.2 ± 0.5 | 65.5 ± 0.5 / 65.3 ± 0.5 / 66.1 ± 0.4 |
| 0c3 | 2q | 98.4 ± 0.1 / 98.5 ± 0.1 / 98.6 ± 0.1 | 98.5 ± 0.1 / 98.5 ± 0.1 / 98.6 ± 0.1 | 98.5 ± 0.1 / 98.5 ± 0.1 / 98.6 ± 0.1 |
| 4a2 | 1q | 64.3 ± 0.5 / 64.3 ± 0.4 / 63.5 ± 0.5 | 76.6 ± 0.5 / 77.3 ± 0.3 / 76.8 ± 0.4 | 80.0 ± 0.4 / 80.3 ± 0.3 / 79.6 ± 0.4 |
| 4a2 | 2q | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 |
| 4a1 | 1q | 62.3 ± 0.5 / 61.9 ± 0.5 / 61.6 ± 0.6 | 75.6 ± 0.4 / 75.6 ± 0.4 / 75.0 ± 0.5 | 88.6 ± 0.3 / 88.3 ± 0.2 / 88.2 ± 0.3 |
| 4a1 | 2q | 98.9 ± 0.1 / 99.0 ± 0.1 / 99.1 ± 0.1 | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 |
| 2c3 | 1q | 20.5 ± 0.4 / 20.8 ± 0.2 / 20.1 ± 0.3 | 48.1 ± 0.5 / 48.4 ± 0.2 / 47.8 ± 0.4 | 71.1 ± 0.4 / 70.9 ± 0.2 / 70.8 ± 0.4 |
| 2c3 | 2q | 95.7 ± 0.2 / 95.6 ± 0.1 / 95.7 ± 0.2 | 99.5 ± 0.1 / 99.5 ± 0.0 / 99.4 ± 0.1 | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 |
| 0c4 | 1q | 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 ± 0.0 | 10.2 ± 0.3 / 9.9 ± 0.2 / 10.0 ± 0.3 | 37.0 ± 0.5 / 36.6 ± 0.3 / 36.3 ± 0.4 |
| 0c4 | 2q | 77.9 ± 0.4 / 77.2 ± 0.2 / 77.3 ± 0.4 | 97.7 ± 0.1 / 97.4 ± 0.1 / 97.4 ± 0.1 | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 |
| 4c3 | 1q | 15.7 ± 0.4 / 15.2 ± 0.2 / 15.1 ± 0.3 | 37.5 ± 0.5 / 37.9 ± 0.2 / 37.9 ± 0.4 | 60.1 ± 0.5 / 59.6 ± 0.2 / 59.8 ± 0.4 |
| 4c3 | 2q | 93.4 ± 0.3 / 93.5 ± 0.1 / 93.5 ± 0.2 | 97.5 ± 0.2 / 97.6 ± 0.1 / 97.7 ± 0.1 | 99.6 ± 0.1 / 99.5 ± 0.0 / 99.6 ± 0.1 |
| 4c4 | 1q | 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 ± 0.0 | 3.7 ± 0.2 / 3.8 ± 0.1 / 3.7 ± 0.2 | 17.6 ± 0.4 / 17.3 ± 0.2 / 17.3 ± 0.3 |
| 4c4 | 2q | 41.6 ± 0.5 / 41.3 ± 0.4 / 41.1 ± 0.5 | 76.9 ± 0.5 / 76.7 ± 0.2 / 76.3 ± 0.4 | 88.2 ± 0.4 / 88.1 ± 0.2 / 88.1 ± 0.3 |
| 4b2 | 1q | 43.7 ± 0.5 / 44.2 ± 0.4 / 43.7 ± 0.5 | 58.0 ± 0.5 / 58.7 ± 0.3 / 58.6 ± 0.5 | 74.1 ± 0.5 / 74.5 ± 0.3 / 74.2 ± 0.4 |
| 4b2 | 2q | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 | 100.0 ± 0.0 / 100.0 ± 0.0 / 100.0 ± 0.0 |
| 4b5 | 1q | 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 ± 0.0 | 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 ± 0.0 | 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 ± 0.0 |
| 4b5 | 2q | 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 ± 0.0 | 19.3 ± 0.4 / 19.3 ± 0.2 / 19.3 ± 0.4 | 68.7 ± 0.5 / 69.6 ± 0.2 / 69.5 ± 0.4 |
| all | 1q | 14.1 ± 0.1 / 14.4 ± 0.2 / 14.0 ± 0.1 | 24.9 ± 0.1 / 25.4 ± 0.2 / 25.0 ± 0.1 | 40.6 ± 0.2 / 41.0 ± 0.2 / 40.6 ± 0.2 |
| all | 2q | 60.4 ± 0.2 / 60.8 ± 0.2 / 60.4 ± 0.2 | 77.1 ± 0.1 / 77.3 ± 0.2 / 77.1 ± 0.1 | 91.4 ± 0.1 / 91.6 ± 0.1 / 91.5 ± 0.1 |

**Q3 headlines, all DRs** (uniform pooled by exact subset size, real by population weight; shares in %):

| all DRs | uniform | dr11 | scr11 | dr10 | scr10 |
|---|---|---|---|---|---|
| mean_htr_niss | 7.798 ± 0.002 | 7.776 ± 0.009 | 7.804 ± 0.005 | 7.759 ± 0.017 | 7.794 ± 0.015 |
| mean_htr_linear_best_side | 8.383 ± 0.002 | 8.356 ± 0.010 | 8.388 ± 0.005 | 8.332 ± 0.020 | 8.372 ± 0.017 |
| mean_htr_normal | 8.801 ± 0.002 | 8.775 ± 0.009 | 8.802 ± 0.005 | 8.759 ± 0.017 | 8.792 ± 0.017 |
| niss_eq_linear | 55.8 ± 0.1 | 56.2 ± 0.2 | 55.8 ± 0.2 | 56.7 ± 0.3 | 56.5 ± 0.6 |
| niss_shorter_by_1 | 32.3 ± 0.1 | 32.0 ± 0.1 | 32.3 ± 0.1 | 31.7 ± 0.3 | 31.9 ± 0.5 |
| niss_shorter_by_2plus | 11.9 ± 0.1 | 11.8 ± 0.1 | 11.9 ± 0.1 | 11.7 ± 0.2 | 11.7 ± 0.3 |
| opt_uses_shortest_niss | 32.9 ± 0.1 | 32.9 ± 0.1 | 32.7 ± 0.1 | 32.9 ± 0.2 | 32.5 ± 0.5 |
| no_opt_through_shortest_niss | 67.2 ± 0.1 | 67.1 ± 0.1 | 67.3 ± 0.1 | 67.1 ± 0.2 | 67.5 ± 0.5 |
| every_opt_htr_ge9 | 65.2 ± 0.1 | 64.9 ± 0.2 | 65.5 ± 0.2 | 64.4 ± 0.4 | 64.8 ± 0.6 |
| mean_opt_minus_leave_slice | 0.290 ± 0.001 | 0.293 ± 0.001 | 0.290 ± 0.002 | 0.294 ± 0.003 | 0.298 ± 0.006 |
| xr2_one_shorter | 32.5 ± 0.1 | 32.5 ± 0.1 | 32.6 ± 0.1 | 32.2 ± 0.2 | 31.6 ± 0.5 |
| 0c3: niss_shorter_by_2plus | 52.4 ± 0.2 | 50.1 ± 0.8 | 52.0 ± 0.6 | 48.4 ± 1.5 | 52.4 ± 2.0 |
| 0c4: niss_shorter_by_2plus | 40.5 ± 0.2 | 41.0 ± 0.7 | 41.0 ± 0.6 | 40.9 ± 1.3 | 39.8 ± 1.9 |

### 2.4 (c) Does any recommendation change?

No.
- **Checklist order**: same first class on every corner subset for the 11-move weightings (and for dr10; with each
  scramble once over 10-move DRs, 4b5's first two classes, the same route switched one quarter turn apart, trade
  places); the three-class lists are identical except 0c4 (a tie: on real DRs `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` takes the slot of
  the uniform third class `0c4 > 4a3 > 4b2 > 4a1 > 0c0`; the uniform three find 0.05 and 0.16 points less on real DRs) and per-cell swaps of 2nd and 3rd classes that were within about a point.
- **Best route**: the first class per corner subset, the route to try first, is unchanged.
- **Bounding**: the subsets where reductions of at most 5 moves reach 80% optimal are still 0c0, 4a1 and 4a2. 4a2
  sits on the line in every population (uniform 80.0 ± 0.4%, each DR once 80.3 ± 0.3%, each scramble once 79.6 ±
  0.4%), so "4a2 reaches 80% at R <= 5" is better read as "about 80%". At R <= 4 (what a solver can write) nothing
  moves by more than 0.7 points.
- **DRs of at most 10 moves** (dr10, scr10) give the same picture with 2-4 times larger SEs; their > 2-point flags
  sit mostly in 0e and 8e cells holding a few hundred DRs (out/cmp_*.tsv).

## 3. Gap 2: finishes that break DR

### 3.0 Method

- **Exact solver**: nissy 2.0.8 `solve optimal` (IDA* with its 2.47 GB `pt_nxopt31` table; 3.1 GB resident, so it
  ran on the second machine, one session for all states). For each state: the DR-move optimum d from judging-a-dr's
  exact table; one optimal DR finish F from htrtools `trace`; the state is written as F^-1 (DR moves only, applied to
  a solved cube); `solve optimal -M d-1 -n 1` returns the shortest solution of at most d - 1 moves if one exists
  (any of the 18 face turns), and if none exists the any-move optimum is d (F is a solution). Cost: 5,367 s for
  48,000 states on 8 threads.
- **Uniform sample**: the first 1,000 states of each of htr-routes' 48 uniform samples (48,000 states; corner
  subsets and "all" pooled by exact subset size).
- **Real sample**: 500 per subset x edges of the Gap 1 route sample (23,976 states; all of them in cells with
  fewer), weighted by that sample's population weights, SE clustered by scramble.
- **Leave slice**: the DR-move optimum to solve corners and U/D edges with the E slice as it falls (judging-a-dr's
  `ls_depth.u8`), for comparison.
- **Examples**: for 8 states with a shorter finish (the largest gain, then the first per corner subset in the
  sample), every optimal solution nissy lists (`solve optimal -o -a`), each replayed on is-dr-xs-worth-it's sticker
  model (`research/src/cube.py`): 27 solutions, all replay to solved with the stated length and all break DR;
  the DR-optimal finish of each replays too; failures: 0 (out/g2_examples.json).

### 3.1 Results

Per corner subset and all DRs (uniform; real where computed): share where some any-move finish is shorter than the
DR-move optimum, by how much, mean gain, mean DR-move / any-move / leave-slice optimum, and the share where the
any-move optimum is even below the leave-slice optimum:

| subset | pop | n | true optimum < DR optimum | by 1 / by 2+ | mean gain (moves) | mean DR opt / true opt / leave-slice | true < leave slice |
|---|---|---|---|---|---|---|---|
| 0c0 | uniform | 5000 | 7.6 ± 0.5% | 6.4 / 1.1 | 0.088 ± 0.006 | 12.271 / 12.183 / 11.581 | 3.2% |
| 0c0 | dr11 | 2476 | 8.5 ± 0.8% | 7.0 / 1.5 | 0.100 ± 0.011 | 12.257 / 12.157 / 11.527 | 3.3% |
| 0c0 | scr11 | 2476 | 7.0 ± 1.2% | 5.4 / 1.5 | 0.085 ± 0.016 | 12.329 / 12.244 / 11.625 | 3.4% |
| 2c5 | uniform | 5000 | 6.3 ± 0.5% | 5.5 / 0.8 | 0.071 ± 0.005 | 14.339 / 14.268 / 14.195 | 5.6% |
| 2c5 | dr11 | 2500 | 6.0 ± 0.7% | 5.3 / 0.7 | 0.068 ± 0.008 | 14.308 / 14.240 / 14.176 | 5.1% |
| 2c5 | scr11 | 2500 | 5.3 ± 1.0% | 4.3 / 1.1 | 0.064 ± 0.014 | 14.342 / 14.278 / 14.180 | 4.6% |
| 2c4 | uniform | 5000 | 3.0 ± 0.3% | 2.8 / 0.3 | 0.033 ± 0.004 | 13.643 / 13.610 / 13.398 | 2.0% |
| 2c4 | dr11 | 2500 | 3.4 ± 0.5% | 3.0 / 0.4 | 0.038 ± 0.006 | 13.637 / 13.599 / 13.348 | 2.5% |
| 2c4 | scr11 | 2500 | 4.0 ± 1.2% | 3.0 / 1.0 | 0.051 ± 0.018 | 13.719 / 13.668 / 13.415 | 3.6% |
| 0c3 | uniform | 5000 | 7.5 ± 0.5% | 6.8 / 0.7 | 0.084 ± 0.006 | 14.415 / 14.331 / 14.366 | 7.0% |
| 0c3 | dr11 | 2500 | 8.4 ± 0.8% | 7.3 / 1.1 | 0.095 ± 0.009 | 14.484 / 14.389 / 14.431 | 7.9% |
| 0c3 | scr11 | 2500 | 7.0 ± 1.2% | 6.3 / 0.7 | 0.077 ± 0.013 | 14.403 / 14.326 / 14.338 | 6.8% |
| 4a2 | uniform | 3000 | 4.2 ± 0.4% | 4.0 / 0.2 | 0.044 ± 0.004 | 13.368 / 13.324 / 13.019 | 2.2% |
| 4a2 | dr11 | 1500 | 4.8 ± 0.7% | 4.3 / 0.5 | 0.053 ± 0.008 | 13.286 / 13.233 / 12.930 | 2.9% |
| 4a2 | scr11 | 1500 | 4.2 ± 0.9% | 3.9 / 0.3 | 0.044 ± 0.009 | 13.286 / 13.241 / 12.965 | 2.2% |
| 4a1 | uniform | 3000 | 6.0 ± 0.5% | 5.2 / 0.8 | 0.068 ± 0.006 | 12.445 / 12.377 / 11.803 | 2.2% |
| 4a1 | dr11 | 1500 | 6.2 ± 0.8% | 5.2 / 1.0 | 0.072 ± 0.009 | 12.408 / 12.336 / 11.797 | 2.3% |
| 4a1 | scr11 | 1500 | 6.0 ± 1.4% | 5.7 / 0.3 | 0.064 ± 0.014 | 12.433 / 12.370 / 11.803 | 2.2% |
| 2c3 | uniform | 5000 | 3.4 ± 0.4% | 3.1 / 0.3 | 0.037 ± 0.004 | 12.942 / 12.905 / 12.491 | 1.3% |
| 2c3 | dr11 | 2500 | 3.0 ± 0.5% | 2.6 / 0.4 | 0.034 ± 0.005 | 12.896 / 12.862 / 12.428 | 1.4% |
| 2c3 | scr11 | 2500 | 1.9 ± 0.4% | 1.7 / 0.1 | 0.020 ± 0.004 | 12.913 / 12.893 / 12.459 | 0.8% |
| 0c4 | uniform | 5000 | 1.7 ± 0.2% | 1.7 / 0.1 | 0.018 ± 0.002 | 13.678 / 13.660 / 13.452 | 1.0% |
| 0c4 | dr11 | 2500 | 1.6 ± 0.3% | 1.4 / 0.2 | 0.018 ± 0.004 | 13.701 / 13.682 / 13.470 | 1.0% |
| 0c4 | scr11 | 2500 | 1.0 ± 0.2% | 0.8 / 0.2 | 0.012 ± 0.004 | 13.731 / 13.718 / 13.512 | 0.6% |
| 4c3 | uniform | 3000 | 2.8 ± 0.4% | 2.6 / 0.2 | 0.031 ± 0.004 | 13.488 / 13.457 / 13.233 | 1.8% |
| 4c3 | dr11 | 1500 | 3.3 ± 0.6% | 3.2 / 0.1 | 0.034 ± 0.006 | 13.562 / 13.528 / 13.290 | 2.0% |
| 4c3 | scr11 | 1500 | 1.7 ± 0.4% | 1.6 / 0.1 | 0.017 ± 0.005 | 13.494 / 13.477 / 13.242 | 0.9% |
| 4c4 | uniform | 3000 | 6.6 ± 0.5% | 5.8 / 0.8 | 0.075 ± 0.006 | 14.396 / 14.321 / 14.284 | 5.6% |
| 4c4 | dr11 | 1500 | 6.5 ± 0.7% | 5.9 / 0.6 | 0.072 ± 0.009 | 14.356 / 14.284 / 14.252 | 5.8% |
| 4c4 | scr11 | 1500 | 6.6 ± 1.3% | 6.3 / 0.3 | 0.070 ± 0.014 | 14.333 / 14.263 / 14.238 | 5.8% |
| 4b2 | uniform | 3000 | 3.5 ± 0.4% | 3.4 / 0.1 | 0.036 ± 0.004 | 12.684 / 12.648 / 12.192 | 1.5% |
| 4b2 | dr11 | 1500 | 2.3 ± 0.4% | 2.1 / 0.2 | 0.026 ± 0.005 | 12.691 / 12.665 / 12.161 | 0.6% |
| 4b2 | scr11 | 1500 | 1.8 ± 0.5% | 1.7 / 0.1 | 0.019 ± 0.005 | 12.670 / 12.651 / 12.166 | 0.3% |
| 4b5 | uniform | 3000 | 5.9 ± 0.5% | 5.1 / 0.8 | 0.067 ± 0.006 | 14.285 / 14.218 / 14.145 | 4.9% |
| 4b5 | dr11 | 1500 | 5.9 ± 0.7% | 5.1 / 0.8 | 0.067 ± 0.009 | 14.284 / 14.217 / 14.135 | 5.3% |
| 4b5 | scr11 | 1500 | 6.0 ± 1.2% | 4.7 / 1.4 | 0.074 ± 0.015 | 14.304 / 14.230 / 14.127 | 4.9% |
| all | uniform | 48000 | 4.3 ± 0.1% | 3.9 / 0.4 | 0.048 ± 0.002 | 13.584 / 13.537 / 13.300 | 2.9% |
| all | dr11 | 23976 | 4.2 ± 0.2% | 3.8 / 0.5 | 0.047 ± 0.002 | 13.566 / 13.518 / 13.261 | 3.0% |
| all | scr11 | 23976 | 3.9 ± 0.4% | 3.4 / 0.6 | 0.045 ± 0.005 | 13.596 / 13.551 / 13.296 | 2.9% |

By the DR-move optimum (uniform, weighted by exact subset size):

| DR optimum | states solved | share of all DR states | a shorter any-move finish exists |
|---|---|---|---|
| 8 | 95 | 0.02% | 0.1% |
| 9 | 269 | 0.10% | 0.1% |
| 10 | 701 | 0.55% | 0.3% |
| 11 | 1,805 | 2.72% | 0.7% |
| 12 | 5,578 | 11.27% | 1.3% |
| 13 | 12,904 | 28.73% | 2.0% |
| 14 | 16,697 | 37.13% | 3.8% |
| 15 | 9,055 | 18.34% | 9.4% |
| 16 | 841 | 1.14% | 35.7% |
| 17 | 13 | 0.01% | 43.1% |

Gains over the 48,000 uniform states (DR-move optimum minus any-move optimum, unweighted counts): 0: 45,001, 1: 2,505, 2: 421, 3: 62, 4: 11.

Per subset x edges (uniform: share shorter ± SE, share shorter by 2+, mean gain):

| subset x edges | uniform: shorter, by 2+, mean gain |
|---|---|
| 0c0 0e | 20.9 ± 1.3%, 6.7%, 0.301 |
| 0c0 2e | 6.2 ± 0.8%, 0.9%, 0.071 |
| 0c0 4e | 6.7 ± 0.8%, 1.0%, 0.079 |
| 0c0 6e | 9.8 ± 0.9%, 1.3%, 0.111 |
| 0c0 8e | 11.4 ± 1.0%, 1.5%, 0.130 |
| 2c5 0e | 8.4 ± 0.9%, 0.9%, 0.096 |
| 2c5 2e | 9.7 ± 0.9%, 1.3%, 0.110 |
| 2c5 4e | 6.0 ± 0.8%, 0.7%, 0.068 |
| 2c5 6e | 3.7 ± 0.6%, 0.4%, 0.041 |
| 2c5 8e | 3.3 ± 0.6%, 0.5%, 0.038 |
| 2c4 0e | 9.9 ± 0.9%, 2.2%, 0.124 |
| 2c4 2e | 3.8 ± 0.6%, 0.4%, 0.043 |
| 2c4 4e | 3.1 ± 0.5%, 0.2%, 0.033 |
| 2c4 6e | 1.7 ± 0.4%, 0.2%, 0.019 |
| 2c4 8e | 2.7 ± 0.5%, 0.5%, 0.033 |
| 0c3 0e | 36.3 ± 1.5%, 13.3%, 0.529 |
| 0c3 2e | 7.4 ± 0.8%, 0.5%, 0.082 |
| 0c3 4e | 9.2 ± 0.9%, 0.8%, 0.100 |
| 0c3 6e | 2.5 ± 0.5%, 0.0%, 0.025 |
| 0c3 8e | 1.2 ± 0.3%, 0.0%, 0.012 |
| 4a2 0e | 9.6 ± 0.9%, 1.2%, 0.109 |
| 4a2 2e | 4.8 ± 0.7%, 0.1%, 0.049 |
| 4a2 4e | 3.4 ± 0.6%, 0.2%, 0.036 |
| 4a1 0e | 4.0 ± 0.6%, 0.6%, 0.046 |
| 4a1 2e | 3.1 ± 0.5%, 0.2%, 0.033 |
| 4a1 4e | 8.7 ± 0.9%, 1.4%, 0.101 |
| 2c3 0e | 6.8 ± 0.8%, 0.6%, 0.074 |
| 2c3 2e | 2.2 ± 0.5%, 0.0%, 0.022 |
| 2c3 4e | 3.9 ± 0.6%, 0.4%, 0.043 |
| 2c3 6e | 3.4 ± 0.6%, 0.5%, 0.039 |
| 2c3 8e | 0.6 ± 0.2%, 0.0%, 0.006 |
| 0c4 0e | 25.6 ± 1.4%, 4.9%, 0.313 |
| 0c4 2e | 1.8 ± 0.4%, 0.0%, 0.018 |
| 0c4 4e | 1.5 ± 0.4%, 0.0%, 0.015 |
| 0c4 6e | 0.8 ± 0.3%, 0.0%, 0.008 |
| 0c4 8e | 0.6 ± 0.2%, 0.0%, 0.006 |
| 4c3 0e | 1.1 ± 0.3%, 0.0%, 0.011 |
| 4c3 2e | 3.0 ± 0.5%, 0.1%, 0.031 |
| 4c3 4e | 2.8 ± 0.5%, 0.4%, 0.032 |
| 4c4 0e | 7.8 ± 0.9%, 0.9%, 0.088 |
| 4c4 2e | 6.2 ± 0.8%, 1.1%, 0.074 |
| 4c4 4e | 6.9 ± 0.8%, 0.6%, 0.075 |
| 4b2 0e | 5.7 ± 0.7%, 1.0%, 0.067 |
| 4b2 2e | 3.9 ± 0.6%, 0.1%, 0.040 |
| 4b2 4e | 3.0 ± 0.5%, 0.1%, 0.031 |
| 4b5 0e | 3.1 ± 0.5%, 0.2%, 0.033 |
| 4b5 2e | 3.8 ± 0.6%, 0.2%, 0.040 |
| 4b5 4e | 7.9 ± 0.9%, 1.3%, 0.092 |

- For finishes a solver actually writes (DR-move optimum of 12 or less) a DR-breaking finish is shorter in
  1.1% of DRs. It matters for long finishes: 9.4% at 15, 36% at 16, 6 of 13 sampled 17s.
- The cells where it matters are the 0e cells with few bad edges and an awkward corner case: 0c3 0e (36%, 13% by
  2+), 0c4 0e (26%), 0c0 0e (21%, 7% by 2+; the U D' x HTR states, solved by slice-like `R L F2 B2 R' L'` shapes).
- Mean gain over all DRs: 0.048 moves. For comparison, optimal minus leave-slice optimum is 0.29 moves on
  average (htr-routes Q3), so leaving the slice is the bigger lever, but the two are different: the any-move
  optimum is a full solve.

### 3.2 Examples (every optimal solution, replayed)

- **0c0 0e**, DR optimum 11, any-move optimum 7 (leave slice 9). State: `B2 L2 R2 F2 R2 U2 L2 R2 U2 R2 U2` applied to a solved cube (DR moves only). DR-optimal finish `U2 R2 U2 R2 L2 U2 R2 F2 R2 L2 B2`. Every optimal solution nissy lists (8): `D2 F' B' R2 L2 F B`, `D2 F B R2 L2 F' B'`, `U2 R' L' F2 B2 R L`, `U2 R L F2 B2 R' L'`, `F B R2 L2 F' B' U2`, `F' B' R2 L2 F B U2`, `R L F2 B2 R' L' D2`, `R' L' F2 B2 R L D2`.
- **0c0 0e**, DR optimum 11, any-move optimum 10 (leave slice 9). State: `R2 F2 D' U' B2 R2 F2 L2 F2 D2 U2` applied to a solved cube (DR moves only). DR-optimal finish `U2 D2 F2 L2 F2 R2 B2 U D F2 R2`. Every optimal solution nissy lists (1): `R L' F2 R' L' B2 U D L2 D2`.
- **0c3 0e**, DR optimum 15, any-move optimum 14 (leave slice 15). State: `L2 B2 D' F2 D2 B2 R2 D' R2 U2 L2 B2 U' L2 U2` applied to a solved cube (DR moves only). DR-optimal finish `U2 L2 U B2 L2 U2 R2 D R2 B2 D2 F2 D B2 L2`. Every optimal solution nissy lists (12): `L2 U D L B2 U2 R2 U2 L U2 B2 R2 F2 R`, `R D2 F2 R2 D2 B2 R B2 R2 U2 L U D R2`, `R D2 F2 R2 D2 B2 L' B2 L2 U2 R' U D R2`, `L B2 L2 F2 D2 R D2 L2 D2 F2 R U D R2`, `U' D' L' U2 F2 R2 D2 B2 R D2 B2 L2 F2 R'`, `L2 U D R D2 L2 F2 L F2 U2 L2 B2 U2 L`, `L2 U D L' D2 R2 F2 R' F2 U2 L2 B2 U2 L`, `R' B2 L2 F2 D2 L D2 L2 D2 B2 R' U' D' L2`, `U' D' R' F2 L2 B2 U2 L F2 D2 L2 B2 D2 L'`, `R2 U' D' L' F2 U2 R2 U2 R U2 B2 R2 F2 L'`, `R' U2 F2 R2 U2 B2 R D2 F2 R2 B2 L' D' U'`, `L' B2 R2 F2 U2 L F2 U2 L2 B2 D2 R' D' U'`.
- **0c4 0e**, DR optimum 14, any-move optimum 13 (leave slice 14). State: `L2 U' R2 D' L2 U' B2 U L2 U F2 U' B2 U2` applied to a solved cube (DR moves only). DR-optimal finish `U2 B2 U F2 U' L2 U' B2 U L2 D R2 U L2`. Every optimal solution nissy lists (2): `B U2 F' U2 L2 B2 L2 B U2 F' U D R2`, `B2 U' D' L D2 R' F2 R2 F2 D2 L D2 R'`.
- **2c3 0e**, DR optimum 14, any-move optimum 13 (leave slice 14). State: `D F2 U B2 L2 R2 U L2 B2 D B2 D B2 U2` applied to a solved cube (DR moves only). DR-optimal finish `U2 B2 D' B2 D' B2 L2 U' R2 L2 B2 U' F2 D'`. Every optimal solution nissy lists (1): `F2 U2 B2 R2 B D B' L2 F U' F R2 U`.
- **2c4 0e**, DR optimum 13, any-move optimum 12 (leave slice 13). State: `U R2 B2 D B2 D R2 D2 F2 L2 D B2 L2` applied to a solved cube (DR moves only). DR-optimal finish `L2 B2 D' L2 F2 D2 R2 D' B2 D' B2 R2 U'`. Every optimal solution nissy lists (1): `D2 R2 D2 R2 L F' L B2 L' F L' F2`.
- **2c5 0e**, DR optimum 15, any-move optimum 14 (leave slice 15). State: `F2 L2 D F2 D' L2 U2 B2 U R2 B2 U F2 L2 U'` applied to a solved cube (DR moves only). DR-optimal finish `U L2 F2 U' B2 R2 U' B2 U2 L2 D F2 D' L2 F2`. Every optimal solution nissy lists (1): `F' U' F R2 B' D F2 B' L2 F2 U' B2 U2 L2`.
- **4a1 0e**, DR optimum 13, any-move optimum 12 (leave slice 13). State: `D' F2 R2 U B2 U2 L2 F2 U2 R2 U' B2 U2` applied to a solved cube (DR moves only). DR-optimal finish `U2 B2 U R2 U2 F2 L2 U2 B2 U' R2 F2 D`. Every optimal solution nissy lists (1): `F2 L2 D' F2 B2 D' F B' U2 B' F U'`.

## 4. What changes in the published studies

**judging-a-dr** (report/WRITEUP.md)
- Section 4, "The data", bullet "**Every count treats each DR state as equally likely.** Real DRs aren't uniform
  across subsets, so read everything per subset." Wrong as a reason: real EO-first DRs (up to 11 moves) are spread
  over the 12 corner subsets within 0.4 points of the uniform shares (section 2.2 table), and within a subset their
  optimal finish matches uniform within 0.05 moves. New wording: every count treats each DR state as equally likely;
  that is also how the DRs you reach from a scramble are spread, up to a slightly different mix of bad-edge counts.
- Section 13, "**Uniform states.** ... The DRs you actually reach are spread differently over the subsets, so use the
  per-subset numbers, not the 'all DRs' ones, for a decision." Same correction; the "all DRs" numbers hold for real
  DRs (htr-routes' all-DR Q3 headlines move by at most 0.4 points on 11-move DRs, 0.9 on 10-move DRs).
- Section 13, "**DR moves only.** ... DR-breaking finishes can be shorter: at the HTR level that's 66 of the 216
  cases." Add the measured size: over all DR states 4.3% ± 0.1% have a shorter any-move finish (mean gain 0.048
  moves; by one move in 90% of those, weighted by subset size); 1.1% among DRs with a DR-move optimum of 12 or less; most in 0c3 0e (36%), 0c4 0e
  (26%), 0c0 0e (21%).
- Appendix A ("Longest" = "God's number for the subset", "In 9 ... In 13" columns) and section 6 ("The longest: 18
  for 0c0 8e, ..."): these are DR-move optima; say so in the column note. For 0c3 0e, 0c4 0e and 0c0 0e the any-move
  finish is shorter on a fifth to a third of states (section 3.1 cell table); the "In N" shares there are lower bounds.
  The 18-move states themselves were not solved with all moves here.

**htr-routes** (report/WRITEUP.md and research/out/SUMMARY.md)
- WRITEUP "Not covered": "**The DR itself.** Uniform DR states. Real DRs come from EOs and triggers and are not
  uniform within a subset (Kai Cui's and JTuu's generated states show how much that can matter, section 8)."
  Replace: real DRs from uniform scrambles (every EO-first DR up to 11 moves on 10,000 scrambles) give the same
  checklists, grades and bounding shares within about 1 point per corner subset (0c0: first class 39-40% against
  42.3%); generated sets like Kai Cui's half-turn-around-a-trigger states are what is not uniform.
- WRITEUP "Not covered": "**DR-breaking and HTR-breaking finishes** ... are not routes here". Add: a DR-breaking
  finish beats the DR-move optimum on 4.3% ± 0.1% of DRs (by one move in 90% of those, weighted by subset size), so "optimal" in every route share means
  DR-move optimal, and on 0c3 0e / 0c4 0e / 0c0 0e that differs on a fifth to a third of states.
- WRITEUP section 8 ("Against the checklists"): "Bounding gets to 80% with short reductions on 0c0 (3), 4a2 and 4a1
  (5)". 4a2 at R <= 5 is 80.0% uniform and 79.6-80.3% on real DRs: write "about 80%".
- research/out/SUMMARY.md, Q2: the "+1 after 3" column is labelled "the same three classes at optimal + 1" but holds
  the greedy +1 checklist: 4a2 91.8% (same classes 90.8%, as the WRITEUP prints), 0c3 99.2% (99.1%), 4a2 0e 68.4%
  (68.2%); other corner subsets agree to 0.1. Fix the label or the numbers.
- Every other table (Q2 checklists, Q6 grades, Q8 bounding, Q3 headlines): no number moves by more than its stated
  SE plus about a point; nothing to change beyond a line saying real DRs were checked.

**eo-switch**: nothing changes. Its own result (switched RZP states are uniform within their class) is the same
mechanism as section 2.1. Its tables count DR in EO-keeping moves, not finishes.

**eo-to-dr**: nothing changes (its DR lengths are to reach DR, not finishes).

## 5. Limits and uncertainty

- **The population is cubelib's list.** EO-first DRs only (no CO-first or direct DR), EO of at most 5 (cubelib's
  limit), DR of at most 11. Of a DR ending in `F` and `F'` only the clockwise one is kept, as on judging-a-dr's
  examples page; by mirror symmetry the other has the same distribution, but this is not measured.
- **Each DR counts, not each DR a solver would pick.** A solver who keeps a DR because of what it looks like (a good
  subset, short HTR) selects on the state; inside the chosen subset the state is still uniform by section 2.1, but
  any selection on features inside a subset (pairs, corner case) is not modelled.
- **SEs**: clustered by scramble, with heavy-tailed cluster sizes for `dr` weightings (one scramble holds 98,536
  DRs), so `dr` SEs in tiny cells are rough; flags at 2 SE fire on 4-10% of cells, about chance. Greedy selection
  uncertainty is not in the SEs.
- **Section 2.1 is an argument**, checked by the measurements, not proved.
- **Gap 2 sample**: 1,000 uniform states per subset x edges (SE about 0.5-1.5 points per cell, 0.1 overall); 500 per
  cell on the real population. nissy is trusted as the exact solver; every solution it printed for the examples was
  replayed, but "no shorter solution" rests on nissy's search being exact (an IDA* with an admissible table; every
  solution it returned was shorter than the DR-move optimum, as it must be under `-M d-1`). The rare 18-move DR states were not solved with all moves.
- **Runs**: population 10,000 scrambles ~60 min on 4 cores; labelling 45 s, routes 8.5 min and bound4 1.5 min on 8
  cores (second machine); analysis ~40 min; nissy 89 min for the 48,000 uniform states and 41 min for the 23,976 real ones, on 8 threads.
