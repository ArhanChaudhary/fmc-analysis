# HTRRoutes: a Lean 4 certificate for the small exact tables of "Which HTR routes to try from a DR"

Lean 4.35.0, no Mathlib (only the library that ships with Lean). About 1,050 lines written by hand, plus `Cube.lean` (copied) and `HTRRoutes/Study.lean` (generated). No `sorry`.

Most of the case study is about DR states (19.5 billion, or samples of them). The parts that live in a small space are the corners (40,320 arrangements), the HTR cosets (29,400) and the HTR group (663,552 states). The research computes these in Rust (`research/htrtools`, and `class.rs` of the first study's drtools) and in Python (`research/src/sticker.py`, `claims.py`). This project computes them again in Lean, from its own definitions of the cube and the ten DR moves, and states each number as a theorem. Four of the research's output files and three rows of `out/claims.tsv` are copied verbatim into `HTRRoutes/Study.lean`. The theorems named `…_matches_study` say that Lean's tables equal those files row for row; `…_as_study` say that the claims rows print the same numbers. All of them do. No number had to be changed.

Words: DR moves are U U2 U' D D2 D' R2 L2 F2 B2 (0 … 9); half turns U2 D2 R2 L2 F2 B2; quarter turns U U' D D'. A corner *arrangement* says which corner sits in each corner place. The *tetrads* are the two sets of four corner places that half turns keep apart. A *bad corner* sits in a place of the other tetrad. *M places* are UF UB DF DB, *S places* UL UR DL DR; *bad edges* are M pieces in S places plus S pieces in M places. *HTR corners* are the 96 arrangements reached from solved by half turns. The *qt count* of an arrangement is the fewest quarter turns of any DR sequence that brings its corners into HTR or into U D' of HTR (half turns free). The 14 *corner subsets* come from (bad corners, qt count, shape): 8 bad corners count as 0 and 6 as 2; with 4 bad corners the letter is *a* when half turns can bring the four bad places onto one face, else *b*. As in the study, 4a3/4b3 and 4a4/4b4 carry the side's own letter, and Mallard's 48 subsets merge them as 4c3 and 4c4. A *corner coset* is an arrangement up to renaming its pieces by an HTR element; an *HTR coset* is a corner coset with the set of places holding M pieces (the *edge pattern*). All of these are the research's definitions (`class.rs`, `sticker.py`), rebuilt here.

## What is proved

**A. The model** (`HTRRoutes/Model.lean`)

| Theorem | It says |
|---|---|
| `model_size` | 54 stickers, all different; the ten DR moves are permutations of the 54 places. |
| `places` | 8 corner places of 3 stickers, 8 U/D-layer edge places and 4 E-slice places of 2. Each tetrad has 4 corner places (UFR UBL DFL DBR is the one with x·y·z > 0). There are 4 M places and 4 S places, and together they are the 8 U/D edge places. |
| `dr_keeps_axes` | Every DR move sends a sticker on a U/D face to a U/D face, and keeps each E-slice edge sticker on a face of the same axis. So DR moves never twist or flip a piece relative to U/D, and a DR state is given by its three arrangements (corners, U/D edges, E slice). |
| `arrangements_follow_stickers` | On every sticker state within 3 DR moves of solved, and for every DR move, the three arrangements after the move are the ones before it composed with the move's arrangement (`amul`). The move arrangements are permutations, and solved is the identity. |
| `half_turns_keep_parts` | Half turns keep each corner in its tetrad and M places among M places. A quarter turn of U or D makes 4 bad corners and 4 bad edges, and U D' makes all 8 corners bad. |
| `ranks` | `unrank 8` lists the 40,320 permutations of eight, each once, with the identity at rank 0. The same holds for the 24 permutations of four. |

**B. The HTR group** (`HTRRoutes/HtrTheorems.lean`; the research's `out/checks/htr_states.tsv`, check (2) of SUMMARY)

| Theorem | It says |
|---|---|
| `htr_coordinate_ok` | The HTR coordinate (two tetrads, M, S and E-slice pieces, 576 · 24³ = 7,962,624 slots) is one to one, and slot 0 is solved. For every value of every part and every half turn, the part table gives exactly the arrangement the move gives. |
| `htr_group_matches_study` | A BFS from solved with the six half turns passes `search.ruleHolds`, so each entry is the fewest half turns that solve the state. It reaches **663,552** states, and its histogram equals the half_turn_optimal column of `htr_states.tsv`, which is DougCube's table. |
| `htr_hist` | Half turns 0 … 15 solve **1, 6, 27, 120, 519, 1932, 6484, 20310, 55034, 113892, 178495, 179196, 89728, 16176, 1488, 144** states. The distances sum to 6,724,652. |
| `htr_parts` | The reached states use 96 corner values and 6,912 edge values (half of 24³). Since 96 · 6,912 = 663,552, every corner value occurs with every edge value. |
| `htr_mean_digits` | 6724652 / 663552 = 10.1343255690…, which rounds to the **10.13432557** of the research and DougCube. |

**C. Corner cases** (`HTRRoutes/CornerTheorems.lean`)

| Theorem | It says |
|---|---|
| `htr_corners` | Half turns reach 96 corner arrangements from solved. Adding U D' gives 192, the targets of the qt count. |
| `qt_checked` | The qt table passes the independent check `qtRule` (see Trust), so each entry is the true fewest quarter turns. Over the 40,320 arrangements, 0 … 5 qt occur 192, 1152, 5760, 11328, 14208, 7680 times. No corner case needs more than 5 qt. |
| `subsets_well_defined` | Every arrangement gets one of the 14 subsets: no (bad corners, qt, shape) falls outside the naming table. The subset is the same across a coset and does not change under half turns. There are **420** corner cosets of 96 arrangements each. |
| `subset_table` | Per subset: cosets, the qt count of every arrangement in it (the minimum quarter turns of the corner case), and the bad corners. **0c0 2** (qt 0), **4a1 12** (1), **4a2 12** (2), **4b2 48** (2), **0c3 6** (3), **2c3 64** (3), **4a3 24** (3), **4b3 24** (3), **0c4 4** (4), **2c4 96** (4), **4a4 24** (4), **4b4 24** (4), **2c5 32** (5), **4b5 48** (5). The sum is 420. The 0c0, 0c3 and 0c4 cosets have 0 or 8 bad corners, the 2cX cosets 2 or 6, and the 4xX cosets 4. |
| `inverse_subsets` | The inverse arrangement (the corners of the inverse scramble) is in the same subset, except that 4a3 ↔ 4b3 and 4a4 ↔ 4b4 swap. So the 2qt letters a/b are the same on both sides, and the 3qt and 4qt letters are a property of the side. |
| `fake_htr` | **"5/6 of HTRs are fake"** (claim C07), in the study's reading: of the **576** corner arrangements with no bad corner, exactly **96** are 0c0, and these are the HTR corners. **288** are 0c3 and **192** are 0c4. |
| `fake_htr_as_study` | 480 / 576 = 5/6. The research's C07 row prints "576; of these 96 are 0c0" and "480/576 = 0.8333". |
| `bare_quarter_turns` | Claim C10. Of the 11,328 arrangements with qt 3, one bare U, U', D or D' on the arrangement or on its inverse gives qt 2 for **7,488** (66.10…%). Of the 14,208 with qt 4, it does for **none**. |
| `bare_quarter_turns_as_study` | 7488/11328 = 0.661…. The C10 row prints "66.1%" and "(0.0%)". |
| `ht_checked` | For each of the 14 subsets t, the table HT[t] (fewest half turns to a place from which a quarter turn lands in t) passes `search.ruleHolds`. |
| `alpha_example` | FakeMMAP's example (T11501): on the corner path 4a3 > 4b2 > 4a1 > HTR, the sections need at least **0, 3, 1, 0** half turns. |
| `alpha_matches_study` | **α for every corner path the study uses.** `out/q9_alpha.tsv` has 1,060 paths of 1 to 10 subsets. For each one, Lean's α_0 … α_N equal the file's, and some arrangement follows the path. α_i is computed as in `htrtools alpha`: R_0 = the arrangements in s_0, R_{i+1} = (half-turn closure of R_i) then a quarter turn into s_{i+1}, and α_i = min over R_i of HT[s_{i+1}]. |

**D. HTR cosets, the 48 subsets, and the 2qt a/b labels** (`HTRRoutes/CosetTheorems.lean`)

| Theorem | It says |
|---|---|
| `htr48_matches_study` | The move action on (corner coset, edge pattern) does not depend on the representative. A BFS over the HTR cosets with the ten DR moves passes `search.ruleHolds`, so each entry is the shortest linear DR → HTR of the coset. It reaches **29,400** = 420 × 70 cosets, and its (48-subset, shortest HTR, cosets) table equals `out/checks/htr48.tsv`, all 161 rows. |
| `htr48_facts` | There are 48 subset names. The shortest linear HTR of a subset is ≤ 4 for **5** subsets, ≤ 5 for **9** and ≤ 6 for **12** (claim C08: Jay's "8 cases in ≤ 5" is 9). The 9 are 0c0 0e/2e/4e, 2c3 2e/4e, 4a1 4e, 4a2 4e and 4b2 2e/4e, and the C08 row says the same. |
| `name_map_matches_study` | All 95 example scrambles of docs 15 and 66 (`out/name_map.tsv`), done on the sticker model, give the research's 48-subset, label, and label of the inverse. |
| `two_qt_letters` | **2qt a/b.** Doc 15's "2qt (a)" examples are 4b2 0e/2e/4e and its "2qt (b)" examples 4a2. Doc 66 has the letters the other way round: "2qt(a)" is 4a2 and "2qt(b)" is 4b2. (`name_map.tsv` has no examples from doc 171, so nothing about doc 171's labels is proved here.) |

**E. One and two quarter turns from HTR** (`HTRRoutes/QtCosetTheorems.lean`; the study's reductions to 1q and 2q)

| Theorem | It says |
|---|---|
| `qt1_is_4a1_4e` | The HTR cosets reached from HTR by one quarter turn and then any half turns are **432**, the set is closed under half turns, and a coset is in it exactly when its label is **4a1 4e**. So 4a1 4e is exactly the set of DR states that one quarter turn and half turns finish (the study's "reduction to 1q"), and on any finish the state before the last quarter turn is 4a1 4e ("the 4a1 before HTR is 4a1 4e"). |
| `qt2_cosets` | The cosets two quarter turns from HTR and no closer: all of 4a2 (24, 384, 432 cosets with 0, 2, 4 bad edges), all of 4b2 (96, 1536, 1728), 0c0 with bad edges (32, 72, 32, 2 with 2, 4, 6, 8) and **one** of the two 0c0 0e cosets; the other 0c0 0e coset is HTR itself. So "2q" is 4a2, 4b2 and every 0c0 that is not HTR. |

## Files

| File | Content |
|---|---|
| `HTRRoutes/Cube.lean` | The sticker model: 54 stickers and the 18 face turns built from geometry. Copied from eo-to-dr's certificate, changing only the namespace and the header. **Read this to convince yourself the model is the cube.** |
| `HTRRoutes/Pieces.lean` | Corner, U/D-edge and E-slice places and arrangements read off stickers, the ten DR moves as arrangements, tetrads, M/S, bad pieces, masks, and permutation ranks. |
| `HTRRoutes/Search.lean` | `bfs` from a set of goals, and the independent check `ruleHolds`. |
| `HTRRoutes/HtrGroup.lean` | B: the HTR coordinate, the part tables, the BFS. |
| `HTRRoutes/Corners.lean` | C: corner move tables on ranks, HTR corners, the qt count and `qtRule`, the 14 subsets, cosets, `HT`, `alphaOf`, fake HTRs and `bareQt`. |
| `HTRRoutes/Cosets.lean` | D: the HTR coset BFS, `label`, `label48`, and the labels of a scramble (`scrambleLabels`). |
| `HTRRoutes/Study.lean` | Generated by `gen_study.py`. It holds `research/out/checks/htr_states.tsv`, `checks/htr48.tsv`, `q9_alpha.tsv`, `name_map.tsv` and the rows C07, C08, C10 of `claims.tsv`, verbatim. |
| `HTRRoutes/Parse.lean` | Reads those files (tab-separated, header dropped). |
| `HTRRoutes/QtCosets.lean` | E: the half-turn closure on HTR cosets (`closure`, checked by `closedUnderHalf`), the sets one and two quarter turns from HTR, and their tally by label. |
| `HTRRoutes/Model.lean`, `HtrTheorems.lean`, `CornerTheorems.lean`, `CosetTheorems.lean`, `QtCosetTheorems.lean` | The theorems, A to E. |
| `HTRRoutes/Audit.lean` | `#print axioms` for every theorem. |
| `gen_study.py` | Writes `HTRRoutes/Study.lean`. Rerun it after the research's outputs change: if a number changed, the build fails. |

## Build

    source /data/fmc/env.sh
    cd /data/fmc/htr-routes/lean/HTRRoutes
    systemd-run --user --scope -q -p MemoryMax=5G lake build

From a clean tree (`rm -rf .lake/build`) on the 4-core VM, this took 39 s wall time, 73 s CPU and 0.53 GB peak memory (one Lean process). The slowest file is `CornerTheorems.lean` (22 s), which includes α for the 1,060 paths. `Model.lean` takes 10 s, `Cosets.lean` and `CosetTheorems.lean` about 9 s each, and `HtrTheorems.lean` 1.4 s. That last one includes the BFS over 7,962,624 slots and its check. The last step prints the audit (`Audit.lean`).

With part E added (13 Nov 2026), a clean build took 95 s CPU and 0.54 GB peak memory (1 min 52 s wall time on a busy machine). `QtCosets.lean` takes 10 to 30 s and `QtCosetTheorems.lean` 14 to 17 s, depending on the load. The definitions of part E are in their own file because a statement run by `native_decide` in the file that defines what it runs is interpreted, not compiled: with both in one file the same two theorems had not finished after 24 minutes.

`lakefile.toml` sets `precompileModules = true`, as in the earlier certificates, so the definitions are compiled to machine code before the theorem files run them. EODR's two notes apply here too. Large tables are top-level constants, not `let`s inside loops, which the compiler can inline and recompute at every step; the tally functions are `@[noinline]`. After editing a definition file, build the whole project.

## Trust

- Every theorem that runs a computation is proved by `native_decide`. Lean compiles the statement, runs it, and accepts the answer `true`. This trusts the Lean compiler and the C compiler, not only Lean's kernel. `Audit.lean` shows one axiom per such theorem, named `<theorem>._native.native_decide.ax_…`, next to Lean's standard axioms. A wrong number does fail: for example, `alphaOf HT (parsePath "4a3 > 4b2 > 4a1 > 0c0") = ([0, 3, 2, 0], true)` and `htr.run = ⟨true, 663553, parse.htrHalfHist⟩` are both rejected.
- `htr_mean_digits` (arithmetic) is proved by `decide`, the kernel alone, with no axioms.
- `search.ruleHolds` does not trust `bfs`. For every state with an entry, it checks three things: the entry is 0 exactly at a goal; every move leads to a state with an entry, with d(x) ≤ d(after the move) + 1; and a non-goal state has a move to an entry one lower. So the entries are the true fewest-move counts, whatever `bfs` did. The argument is in the file header; it is not a Lean theorem.
- Part E's `closure` is `search.bfs` with the six half turns. `closedUnderHalf` checks that the set it marks is closed under the half turns, and `bfs` only ever marks a start or a move of something already marked, so the set is exactly the half-turn closure of the starts. That argument is informal too.
- `qtRule` does not trust the qt computation. It checks the following: qt = 0 exactly on the 192 targets; a half turn keeps qt; a quarter turn lowers it by at most 1; and from every arrangement with qt = k > 0, some HTR element h (a product of half turns) followed by a quarter turn reaches qt = k − 1. The last two give, as for `ruleHolds`, that qt is the fewest quarter turns. That argument is likewise informal.
- What a theorem says is exactly what its Lean statement says about the Lean definitions. That those definitions are the cube and the study's quantities is for the reader to check. A is the evidence: the arrangements follow the sticker model, and DR moves keep the axes. Two steps are argued, not proved in Lean. The first is that a DR state is its three arrangements. `dr_keeps_axes` checks that the U/D and E-slice stickers keep their axes, and the step from there to fixed orientation is the usual one. The second is that composing arrangements (`amul`) is associative.

## Where the Lean differs from the research

- **Coordinates.** The research indexes corners and edges by its own ranks (`core.rs`) and labels cosets by first appearance. The Lean reads arrangements off its own sticker model, ranks them with its own Lehmer code, and names a coset by its smallest rank. So the comparisons are by content and never by index: the sorted (subset, length, count) rows of `htr48.tsv`, the histogram of `htr_states.tsv`, α per path name, and labels per scramble.
- **The qt count** is computed per arrangement, as in `sticker.py`, rather than per coset as in `class.rs`. `subsets_well_defined` shows that the subset is constant on cosets, so the two agree.
- **The 48 subsets** are grouped by name (`label48`), not by the research's union-find over half turns, U D' and inversion. The table equals the research's, so the grouping is the same.
- **The HTR group** is searched directly, with half turns on a coordinate of 7,962,624 slots. The research reads it off its 19.5-billion-state exact table, and DougCube made his table independently.

## Not proved in Lean

- **Everything sampled.** That covers all of Q1–Q6 and Q8 (25,000 states per subset × edge count, the route classes, the checklists, the grading of hand checklists), Q9's per-state numbers (R sufficient, pruning, the T11503 counterexamples) and C11/C13. It also covers every claim whose evidence is a share of sampled states (C01–C06, C12, C14, C26, C27, C48 and the others in `claims.tsv`), and the witnesses.
- **Exact numbers that need the first study's 19.5-billion-state table.** These are the per-subset optimal distributions (`dist48.tsv`, check (1)), DR → HTR per subset weighted by states (check (3)), the 32.47% for inverting the last DR move (C15), the 0c3 vs 2c4 means of C09, and the dr_optimal column of `htr_states.tsv`: the 663,552 HTR states solved with any DR move (mean 9.88708, max 13). That last one needs distances in the whole DR group, not just the HTR group, and was not attempted. The first study's own certificate (`judging-a-dr/lean/DRBound`) proves its exact table.
- **C09's "7 cases".** That is a count of names (subsets with at most 3 qt: 0c0 4a1 4a2 4b2 0c3 2c3 4c3). It can be read off `subset_table`, but it is not stated as a theorem.
- **That every corner arrangement occurs in DR** is argued, not stated: `qt_checked` gives every one of the 40,320 a DR sequence into the HTR corners or U D' of them, and reversing it reaches the arrangement from solved. The HTR states and the HTR cosets are reached from solved by their BFS, so they do occur.
- The research's checks against the sticker model and nissy, and its comparisons with docs 15, 66, 171, 396, 410, are research-side checks and are not redone here. Doc 218 (DougCube) is compared only through the research's `htr_states.tsv`, whose half_turn_optimal column the research checked against doc 218 count by count.
