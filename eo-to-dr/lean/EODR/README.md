# EODR — a Lean 4 certificate for the small exact tables of "EO → DR and scramble → DR"

Lean 4.35.0, no Mathlib (only the library that ships with Lean). About 1,100 lines written by hand, plus `EODR/Study.lean`, which is generated. No `sorry`.

The case study's exact numbers that fit in a small state space are computed in Rust (`research/eodrtools`: `eo axis`, `eo layouts`, `eodr exact`) and in the research's coset tables. This project does them again in Lean, from its own definitions of the cube and the 18 face turns, and states each number as a theorem. Four of the research's output files are copied verbatim into `EODR/Study.lean`, and the theorems named `…_matches_study` say that Lean's tables equal those files row for row. All of them do. No number had to be changed.

Words: axes 0 = R/L, 1 = U/D, 2 = F/B. Turns are face turns (HTM), named U U2 U' D D2 D' R R2 R' L L2 L' F F2 F' B B2 B' (indices 0 … 17 in that order). An edge is *good* for axis Y when it can go home without quarter turns of the Y faces. `Pieces.lean` reads this off the stickers: each edge place has a reference sticker for Y (its U/D sticker if it has one, else its Y sticker; for Y = U/D, its F/B sticker if it has one, else its U/D sticker), and an edge is good when its own reference sticker sits on the place's reference sticker. A *mask* is the 12 bad-edge bits of a state. *Twist* is the U/D corner orientation. *DR on U/D* with F/B EO solved means every twist is 0 and the four E-slice pieces are in the E slice, as in the research's coset tables.

## What is proved

**A. The model** (`EODR/Model.lean`)

| Theorem | It says |
|---|---|
| `model_size` | 54 stickers, all different; 18 face turns with the names above, each a permutation of the 54 places. |
| `places` | 12 edge places of 2 stickers and 8 corner places of 3, together the 48 non-centre stickers. Each of the M, E and S kinds has four edge places. The E-slice places are the four with no U or D sticker. |
| `turns_permute_pieces` | Each turn sends edge places to edge places and corner places to corner places, one to one. |
| `flip_table` | **The EO rule.** For each axis Y, turn and edge place, a turn changes the goodness of an edge for Y exactly when the turn is a quarter turn of a Y face and the edge is on that face. So every other turn keeps EO on Y, and a Y quarter turn changes 4 edges. |
| `keep_fb_eo` | The turns that keep F/B EO are exactly U, D, R and L turns plus F2 and B2: the 14 turns used in D. |
| `corner_turns_cyclic` | Each turn carries each corner's sticker list (U/D sticker first, then round the corner) onto the destination corner's list, shifted cyclically. So a turn adds a fixed amount mod 3 to the twist, and over the 8 corners these amounts sum to 0 mod 3. |
| `coordinates_follow_stickers` | On every sticker state within 3 turns of solved, and for every turn, the masks on all three axes, the twist number and the E-slice mask after the turn are what the coordinate tables (`EOT`, `coAct`, `maskAct`) compute from those before it. The solved cube has no bad edges and no twist, and its E-slice pieces are in the E-slice places. |

**B. EO on one axis: the 2,048 states** (`EODR/EoTheorems.lean`; the research's `eo axis`)

| Theorem | It says |
|---|---|
| `eo_table_checked` | On each axis, the BFS table passes the independent check `search.ruleHolds` (see Trust), so each entry is the fewest face turns to EO. The masks it reaches are exactly those with an even number of bad edges. |
| `eo_states` | There are 2,048 such masks. |
| `eo_distance_hist` | Fewest turns to EO, the same on all three axes: 0 for 1 state, 1 for 2, 2 for 25, 3 for 202, 4 for 620, 5 for 900, 6 for 285 and 7 for 13. The maximum is 7. |
| `eo_distance_sum`, `eo_mean_digits` | The distances sum to 9439, so the mean is 9439/2048 = 4.60888… (DougCube's 4.609; S-EO-6/9). |
| `eo_by_bad` | By number of bad edges, on every axis. 0 bad (1 state): 0 turns. 2 bad (66): 3:40, 4:22, 5:4. 4 bad (495): 1:2, 2:24, 3:134, 4:276, 5:56, 6:3. 6 bad (924): 3:8, 4:200, 5:556, 6:160. 8 bad (495): 2:1, 3:20, 4:122, 5:284, 6:68. 10 bad (66): 6:54, 7:12. 12 bad (1): 7. This is the "optimal linear EO" column of SUMMARY B5, and every "linear ≤ k" share there follows from it. The 10-bad case has no EO under 6 turns, and 12 of its 66 states need 7 (S-EO-24/25/26). The superflip needs 7 (S-EO-23). Within 4 turns, 8 bad (143/495 = 28.9%) beats 6 bad (208/924 = 22.5%) (S-EO-141). |
| `eo_solution_counts` | Counts of canonical F/B EO solutions, i.e. sequences that reach EO for the first time at their last turn. Canonical as in the research: no two turns of one face in a row, and for opposite faces the U, R or F turn goes first. For lengths 0 … 8 the theorem gives five rows. Sum over the 2,048 states: 1, 4, 54, 720, 9612, 128176, 1710088, 22816024, 304466248. Most for one state: 1, 2, 4, 16, 72, 384, 3920, 43748, 500774. Most of length ≤ r: 1, 2, 4, 20, 92, 476, 4332, 48080, 548854. Sum of those of length ≤ r: 1, 5, 59, 779, 10391, 138567, …. States with none of length ≤ r: 2047, 2045, 2020, 1818, 1198, 298, 13, 0, 0. |
| `eo_le5_mean_digits` | 138567/2048 = 67.6596…, the "≤ 5 mean 67.6597" of B4. The same theorem gives "at most 476" (≤ 5) and "at most 92" (≤ 4). |
| `eo_axis_matches_study` | The whole state-by-state table (bad edges, fewest turns, n₀ … n₈) equals `research/out/eo_axis.tsv`, 2,048 rows. Both sides are sorted, so the research's state numbering does not matter. |

**C. Bad-edge layouts** (`EODR/LayoutTheorems.lean`; the research's `eo layouts`)

| Theorem | It says |
|---|---|
| `badAt_rules` | `badAt Y k p o` asks whether piece p, at place k with F/B orientation o, is bad for Y. It is read off the stickers. Checked over every place, piece and orientation and all three axes: for Y = F/B it equals o; turning a piece over changes its badness on every axis; and it depends on the piece only through its kind (E, M or S). |
| `arrangements_count` | 34,650 ways to put four E, four M and four S pieces on the 12 places; 34,650 × 2,048 = 70,963,200. |
| `layouts_matches_study` | The count runs over those 70,963,200 configurations: each placement of kinds × each of the 2,048 even F/B orientation vectors. Its table of (bad F/B, bad R/L, bad U/D) triples equals `research/out/eo_layouts.tsv` row for row (247 triples). Each configuration stands for 4!³ edge permutations, so count/70,963,200 is the probability over all 12!·2¹¹ edge states. |
| `layout_facts` | Readings of that table. 12/12/12: 1 configuration (S-EO-17). Some axis with 0 bad: **103,741** (torchlight's 103741/70963200, S-EO-67). Every axis in {0, 2, 4, 8}: **9,868,829** (S-EO-44). Sorted triples: 4/6/6 10,465,584; 6/6/6 6,527,128; 6/6/8 10,465,584 (S-EO-41); 0/0/2 48 and 0/0/8 3 (S-EO-43); 2/10/10 1,098 (S-EO-45); 10/10/10 12,602. The full distribution of the sum of the three counts, which peaks at 18 with **16,978,144** (S-EO-39). Two axes never differ by more than 8, and 8 occurs (S-EO-45). 12 bad on one axis leaves at least 4 on each other axis, and 4 occurs (S-EO-46). With 0 bad on one axis, the others have 0, 2, 4, 6 or 8, and each occurs (S-EO-47). |
| `layout_share_digits` | The same as percentages, cut (not rounded) after the last digit shown: 13.906967…%, 0.146189(6)% (the study rounds to 0.146190%), 23.9252(7)% (rounded 23.9253%, torchlight's 23.93%), 14.747903…%, 9.197905…%. |

**D. EO → DR, exact over the 1,082,565 cosets** (`EODR/EodrTheorems.lean`; the research's `eodr exact` and the eo = 0 part of `eo-fb_dr.u8`)

| Theorem | It says |
|---|---|
| `eodr_matches_study` | `run` is a BFS over (twist number 0 … 6560) × (12-bit E-slice mask) with the 14 EO-keeping turns, to DR on U/D. Its table passes `search.ruleHolds`, so each entry is the fewest such turns to DR. The states it reaches are exactly the twist vectors with sum ≡ 0 (mod 3) × the masks with 4 bits, 1,082,565 in all. Its per-case table (corners twisted × misplaced E-slice edges, xcye as in Cale's sheet) for the options "eo" (EO kept), "eo_switchF" and "eo_switchB" (better of the state and the state after F2 / B2: the last EO turn inverted) equals the rows of `research/out/eodr_exact.tsv` for those options (40 cases × 3). |
| `eodr_states` | 2187 × 495 = 1,082,565. |
| `eodr_facts` | Readings. EO kept: **1, 2, 17, 134, 1065, 8190, 54694, 267576, 560568, 187204, 3114** for 0 … 10 turns (Cale's table, S-DR-76), Σ = 8,447,364 (mean 7.8031), ≤ 6 for 64,103. Last turn inverted if better: 1, 4, 29, 228, 1809, 13736, 86726, 365050, 523932, 90098, 952 (F and B the same), Σ = 8,164,226 (mean 7.5416), ≤ 6 for 102,533. 4c4e: 70,560 cosets (EO-DR-22), ≤ 6 for 13,576, with the switch 19,798 (EO-DR-79). The five most common cases are 6c6e 137,984, 5c6e 125,440, 6c4e 103,488, 5c4e 94,080 and 4c6e 94,080, and no case has more than 6c6e (EO-DR-32). |
| `eo0_hist_matches_study` | The research's own histogram of the eo = 0 part of `eo-fb_dr.u8` (`out/eo0_hist_eo-fb_dr.txt`, made from the 2.2 GB table) is the same distribution. |
| `eodr_digits` | 8447364/1082565 = 7.8031…; 8164226/1082565 = 7.541557…; ≤ 6: 5.92% and 9.47%; 4c4e ≤ 6: 19.24% (1 in 5.20) and with the switch 28.058% (1 in 3.56); 4c4e is 1 in 15.34; 10 turns: 0.287% (EO-DR-50); 6c6e 12.746%. |
| `twist_counts` | Over the 2,187 twist vectors with sum ≡ 0 (mod 3), the number with k twisted corners: 0:1, 2:56, 3:112, 4:420, 5:560, 6:616, 7:336, 8:86 (EO-DR-18: 112/2187 and 420/2187). Of the 616 with six twisted, 56 have all six twisted the same way and 560 have three each way (EO-DR-5: 1 in 11). |

## Files

| File | Content |
|---|---|
| `EODR/Cube.lean` | The sticker model: 54 stickers and the 18 face turns built from geometry. Copied unchanged, except for the namespace, from is-dr-xs-worth-it's certificate (`lean/DRXs/DRXs/Cube.lean`). **Read this to convince yourself the model is the cube.** |
| `EODR/Pieces.lean` | Edge and corner places, the EO rule, twist and the E-slice mask read off stickers, and what each turn does to them (`EOT`, `coAct`, `maskAct`). |
| `EODR/Search.lean` | `bfs` and the independent check `ruleHolds`. |
| `EODR/Eo.lean` | B: the one-axis table, the distance readings, and the canonical first-reach counts (the recursion of `eo.rs: eo_counts`). |
| `EODR/Layouts.lean` | C: `badAt`, the placements, the count, and the readings. |
| `EODR/Eodr.lean` | D: the coset BFS, `tally` (per case and option), the readings, and the twist counts. |
| `EODR/Study.lean` | Generated by `gen_study.py`: `eo_axis.tsv`, `eo_layouts.tsv`, `eodr_exact.tsv` and `eo0_hist_eo-fb_dr.txt` from `research/out/`, verbatim. |
| `EODR/Parse.lean` | Reads those files (tab-separated, header dropped). |
| `EODR/Model.lean`, `EoTheorems.lean`, `LayoutTheorems.lean`, `EodrTheorems.lean` | The theorems, A to D. |
| `EODR/Audit.lean` | `#print axioms` for every theorem. |
| `gen_study.py` | Writes `EODR/Study.lean`. Rerun it after the research's outputs change; if a number changed, the build fails. |

## Build

    source /data/fmc/env.sh
    cd /data/fmc/eo-to-dr/lean/EODR
    systemd-run --user --scope -q -p MemoryMax=5G lake build

Measured from a clean tree (`rm -rf .lake/build`) on the 4-core VM: 8 s wall, 18 s CPU, peak memory 0.55 GB (one Lean process). The theorem files take 2–3 s each. D's BFS over 26.9 million slots, 1,082,565 of them reached, takes about 1.5 s with its check. C's count over 70,963,200 configurations takes about 2 s. The last step prints the audit (`Audit.lean`).

`lakefile.toml` sets `precompileModules = true`, as in the two earlier certificates: the definitions are compiled to machine code before the theorem files run them.

Two notes for anyone who edits the code:
- A `let` table written inside a loop's function can be inlined by the compiler into the loop body and recomputed at every step. In `Eodr.run` this redid the whole BFS for every state. Large tables are therefore top-level constants (`POP`, `EVENS`, `CO_OK`, …), and the tally is a separate `@[noinline]` function that receives the BFS table as an argument.
- After changing a definition file, build the whole project (`lake build`). Building one module does not rebuild its shared library, and a stale library makes the theorem files fall back to slow interpreted code.

## Trust

- Every theorem that runs a computation is proved by `native_decide`: Lean compiles the statement, runs it, and accepts the answer `true`. This trusts the Lean compiler and the C compiler, not only Lean's kernel. `Audit.lean` shows one axiom per such theorem, named `<theorem>._native.native_decide.ax_…`, next to Lean's three standard axioms. A wrong number does fail: for example, `(layouts.count 34650).2 = 70963201` and `(eodr.run eodr.N).states = 1082566` are both rejected.
- Proved by `decide`, the kernel alone, with no axioms: `eo_mean_digits`, `eo_le5_mean_digits`, `layout_share_digits`, `eodr_states` and `eodr_digits` (arithmetic on the numbers).
- `search.ruleHolds` does not trust `bfs`. For each state with an entry it checks three things: the entry is 0 exactly at the goal; every turn leads to a state with an entry, and d(x) ≤ d(after the turn) + 1; and a non-goal state has a turn to an entry one lower. The third gives a sequence of d(x) turns to the goal. The second, followed along any sequence of k turns to the goal, gives d(x) ≤ k. So the entries are the true fewest-turn counts (turns applied after the state), whatever `bfs` did.
- What a theorem says is exactly what its Lean statement says about the Lean definitions. That those definitions are the cube and the study's quantities is for the reader to check. A is the evidence: the EO rule's flip table, the cyclic corner lists, and agreement of the coordinate actions with the sticker model.

## Where the Lean differs from the research

- **Coordinates.** The research indexes states by ranks (eo 0 … 2047, co 0 … 2186, sl 0 … 494) and reads its moves from `cubie.txt`. The Lean uses raw masks and Σ twist·3^c, with tables computed from its own sticker model. The comparisons with the research's files are therefore by content: sorted rows (B), the triple table (C), and per-case histograms (D). They never compare by index.
- **EO→DR.** The research reads the eo = 0 part of its 2.2 GB table `eo-fb_dr.u8`. The Lean does its own BFS over the 1,082,565 cosets, so it checks that part of the table independently.
- **Layouts.** Both count placements × even F/B orientation vectors. The Lean reads the per-axis badness from stickers, and `badAt_rules` checks the rule that the research asserts in `layouts_cmd` (badness depends on the piece only through its kind).

## Not proved in Lean

- **Everything sampled**: all of A1–A3 (50,000 scrambles, the 500 of judging-a-dr), B4's per-scramble counts and the NISS and all-axes EO numbers (1,000,000 states: 3.88137, 3.60056, 3.45481, the "≤ 3 on some axis" shares), B5's NISS columns, and every "sampled" row of C6/C7 (inverse, better of normal and inverse, combinations; 10,000,000 states).
- **The exact rows that need the full 2,217,093,120-coset space**: "any turns (EO may break)" (7.7969, torchlight) and its switch variant, and the fixed-axis scramble → DR distribution (9.5245, max 12). These need `all_dr.u8` (2.2 GB) or a BFS over (co, eo, sl). That does not fit a Lean `native_decide` run in 5 GB, and was not attempted.
- **"Better of the two DR axes, EO kept" (7.4008, 11.33%, EO-DR-334)**: exact in the research, but it sums over 8!·3⁷ corner states and 34,650 edge placements, about 3·10¹⁰ steps. Not attempted.
- **That every one of the 12!·2¹¹ edge states, and every coset, occurs on a real cube**, and that each placement of kinds stands for exactly 4!³ permutations: these are the usual facts behind the normalisation by 70,963,200, not proved here. (`flip_table` gives the parity half: a turn changes 0 or 4 edges' goodness. The BFS in B and D shows that every even mask and every (twist vector, slice mask) state is reached.)
- **That the EO-solved cosets are equally likely after a random EO** (README "C's EO-solved states are uniform"): this is what makes the D counts probabilities. It is the study's argument, not proved here.
- The table mappings to other axes through rotations, and the checks against nissy, are research-side checks, not redone here (B and C compute all three axes directly).
