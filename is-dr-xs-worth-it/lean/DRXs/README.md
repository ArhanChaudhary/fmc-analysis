# DRXs — a Lean 4 certificate for the kinds of DR-xs state and for the slice-EO skip count

Lean 4.35.0, no Mathlib (only the library that ships with Lean, `Std.HashMap` included). About 900 lines, no `sorry`.

The case study "Is DR-xs worth it?" rests on a few exact computations done in Python (`research/src/cube.py`, `fe.py`, `fecosets.py`, `festeps.py`, `seo_skip.py`). This project does them again in Lean, from its own definitions, and states each resulting number as a theorem. Every number below is also the number the Python prints; none had to be changed.

Words: a *kind* is a signature (face axis the corners are oriented on, 8 flip bits, 4 slice bits) with the U/D colours as the colour axis. A *group* is one allowed turn or pair of turns about one axis (`fe.gens`: any turns of the two oriented faces, half turns of the others, and the slice turns R L, R L', R' L, R' L' and their F/B or U/D likes); two groups in a row are never about the same axis. *Slices* of a kind = fewest slice groups to a real DR. Turns are face turns (R L' counts 2).

## What is proved

**A. The model is a cube** (`DRXs/Theorems.lean`)

| Theorem | It says |
|---|---|
| `model_size` | There are 54 stickers, all different, and 18 face turns named U U2 U' … B B2 B'. |
| `moves_are_permutations` | Each of the 18 face-turn maps is a permutation of the 54 places. |
| `quarter_turn_four_times` | U⁴ = F⁴ = R⁴ = identity. |
| `turns_of_a_face` | Each of U D R L F B has order exactly 4, X2 is X done twice and X' is X done three times. |
| `sexy_move_order` | R U R' U' has order 6. |
| `RU_order` | R U has order 105. |
| `order_1260` | R U2 D' B D' has order 1260. |
| `turn_directions` | U carries the U-sticker of UFR to UFL, R carries it to UBR facing B, F carries it to DFR facing R (clockwise turns). |
| `moves_agree_with_python` | The 18 permutations built in Lean from geometry are, number for number, the ones `cube.py` builds. |

**B. Kinds**

| Theorem | It says |
|---|---|
| `gens_well_formed` | For each face axis there are 29 allowed groups, written with the 18 move names only. |
| `explore_asserts_hold` | No assert of the walk fails (the Python's spot check included, 20000 comparisons). |
| `kinds_count` | Starting from the solved cube and closing under the allowed groups, exactly 768 signatures are reached. |
| `kinds_closed` | Each of the 768 has its 29 groups and every one of them leads to one of the 768. |
| `kinds_by_face_axis` | 256 kinds for each face axis. |
| `one_real_dr` | The walk starts at the real DR (U/D axis, no flips, slice bits 1111), and that is the only real DR among the 768. |
| `moves_keep_corners_and_edges` | A face turn carries the 24 corner places to corner places and the 24 edge places to edge places. |
| `signature_is_complete_invariant` | Over all 210 reachable (face axis, colours at the corner places) and all 53,760 reachable (face axis, colours at the edge places): the state has a signature, it is one of the 768, and each group leads to the signature recorded for that kind. So the 768-kind table speaks for every reachable state, not only for one state per kind (argument in `DRXs/Invariant.lean`). |
| `slices_hist` | Slices: 1 kind needs 0, 140 need 1, 383 need 2, 244 need 3. |

**C. DR-1s to DR**

| Theorem | It says |
|---|---|
| `dr1s_turns_hist` | Over the 140 kinds with slices = 1, the fewest turns to a real DR are 2 for 2 kinds, 3 for 4, 4 for 18, 5 for 60, 6 for 56. |
| `dr1s_turns_le_6` | No kind with slices = 1 needs more than 6 turns. |

**D. DR-2s and DR-3s to DR**

| Theorem | It says |
|---|---|
| `dr2s_turns_hist` | Over the 383 kinds with slices = 2: 4 turns for 2 kinds, 5 for 32, 6 for 99, 7 for 172, 8 for 54, 9 for 24. |
| `dr3s_turns_hist` | Over the 244 kinds with slices = 3: 6 turns for 2 kinds, 7 for 14, 8 for 118, 9 for 80, 10 for 30. |

**E. Steps**

| Theorem | It says |
|---|---|
| `dr3s_to_2s_hist` | From each of the 244 kinds with slices = 3, a kind with slices ≤ 2 is reached in exactly 2 turns. |
| `dr2s_to_1s_hist` | From the 383 kinds with slices = 2, a kind with slices ≤ 1 is reached in 2 turns (209 kinds), 3 (102) or 4 (72). |
| `tables_satisfy_rule` | Each of the four tables (slices, turns to DR, turns to ≤ 1 slice, turns to ≤ 2 slices) satisfies its rule in every entry: 0 on the target, else the least weight + entry of the next kind over the groups about an axis other than the previous one. |
| `to0_is_dmv` | `festeps`' table "to the kinds with 0 slices" is `fecosets`' table "to a real DR". |

In C, D, E the previous axis is "none" (counted from scratch).

**F. Slice-EO skips** (`DRXs/SeoTheorems.lean`)

| Theorem | It says |
|---|---|
| `seo_skip_counts` | Over all 70,963,200 configurations (which kind of piece is at each edge place × 2,048 orientation vectors): the number with exactly k slice-EO skips, for every k, on normal and on normal and inverse together. Same two tables as `research/out/seo_skip.txt`. |
| `seo_no_skip` | 22,143,888 of the 70,963,200 have no skip on normal; 14,678,928 have none on normal or inverse. |
| `seo_configurations` | 34,650 × 2,048 = 70,963,200. |
| `seo_share_normal`, `seo_share_both` | So the share with at least one skip is 68.7953 % on normal and 79.3147 % on normal or inverse, to four places. |

## Files

| File | Content |
|---|---|
| `DRXs/Cube.lean` | `cube.py`: stickers from geometry, the 18 face turns, `apply`, `do_`, `order`. **Read this to convince yourself the model is the cube.** |
| `DRXs/Fe.lean` | `fe.py`: `look`, `is_dr`, `gens`. |
| `DRXs/Fecosets.lean` | `fecosets.py`: `explore`, `dijkstra` (as `shortest`, see below), and the run: `kinds`, `dsl`, `dmv`. |
| `DRXs/Festeps.lean` | `festeps.py`'s `to_set` and the tables `to1`, `to2`, `to0`. |
| `DRXs/Invariant.lean` | The complete check that the signature decides what every group does, with the argument why two small walks are enough. Not in the Python. |
| `DRXs/SeoSkip.lean` | `seo_skip.py`'s counting loop. |
| `DRXs/Theorems.lean`, `DRXs/SeoTheorems.lean` | The theorems. |
| `DRXs/PyMoves.lean` | Generated by `gen_moves.py` from `cube.py`: Python's 18 permutations, used only by `moves_agree_with_python`. |
| `DRXs/Audit.lean` | `#print axioms` for every theorem. |
| `gen_moves.py` | Writes `DRXs/PyMoves.lean`. |

`Cube`, `Fe`, `Fecosets` and `SeoSkip` each start with a "Python -> Lean" note. Names are the Python's, except: no leading underscore (`rot`, `layer_move`, `build`, `stickers`), `do_` for `do`, and `cube.ST` written with its prefix (plain `ST` means something else in Lean).

## Build

    source /data/fmc/env.sh
    cd /data/fmc/is-dr-xs-worth-it/lean/DRXs
    systemd-run --user --scope -q -p MemoryMax=2G lake build

From a clean tree this takes about 1 minute on the 4-core VM (measured: 51 s wall, 72 s of CPU, peak memory 0.7 GB): 41 s for F's run (`SeoTheorems`), 17 s for `Theorems`, a few seconds for everything else. With other jobs hammering the disk the wall time has been several times longer for the same CPU time. The last step prints the audit (`Audit.lean`).

`lakefile.toml` sets `precompileModules = true`, as in the first study: the definitions are compiled to machine code before the theorem files run them. Without it they would run in the interpreter and F would not finish in reasonable time.

To regenerate `DRXs/PyMoves.lean`: `/data/fmc/venv/bin/python gen_moves.py` (it must come out unchanged).

## Trust

- Every theorem that runs a computation is proved by `native_decide`: Lean compiles the statement, runs it, and accepts the answer `true`. This trusts the Lean compiler and the C compiler, not only Lean's kernel. `Audit.lean` shows it as one axiom per such theorem, named `<theorem>._native.native_decide.ax_…`, next to Lean's three standard axioms. The kernel does not replay these computations (`explore`, `shortest` and `walk` use `while` loops, which only compiled code can run).
- Checked by the kernel alone, no axioms: `seo_configurations`, `seo_share_normal`, `seo_share_both` (`decide`, plain arithmetic). `seo_no_skip` is read off `seo_skip_counts` by the kernel (`rw`, `decide`) and so depends on that one run.
- What a theorem says is exactly what its Lean statement says about the Lean definitions. That those definitions are the cube and the Python's procedures is for the reader to check; the files are short and follow the Python line by line, and section A is the evidence for the cube.
- `tables_satisfy_rule` is a second look at the four tables that does not depend on how they were filled in. For the three tables counted in turns (every group costs 1 or 2) the rule has only one solution, so the theorem pins them down by itself. For the slices table (groups cost 0 or 1) it does not; there the minimum rests on how `shortest` works (entries only ever take the cost of an actual sequence of groups, and the loop stops when the rule holds everywhere).

## Where the Lean differs from the Python

- **`dijkstra` / `to_set`.** The Python runs Dijkstra's algorithm with a heap on the reversed graph. The Lean repeats the rule from the Python's own comment over all entries until nothing changes (`fecosets.shortest`). Same table.
- **Asserts** are counted (`failed`) instead of stopping the run; `explore_asserts_hold` says the count is 0.
- **More than the Python:** `Invariant.lean` (the complete invariance check), `kinds_closed`, `tables_satisfy_rule`, `turns_of_a_face`, `moves_keep_corners_and_edges`.
- **Less than the Python:** no slice turns, wide turns or rotations in the cube model (nothing here needs them); no `best_move` / `path`; no `after_quarter` in `festeps`; in `seo_skip`, no `check_rule`, no per-event counts and no "oriented only" tables.
- **Move sequences** are strings whose names must be separated by spaces (`"R U R' U'"`); the Python also accepts them run together.
- **`seo_skip`**: numpy handles the 2,048 orientation vectors of a placement at once; the Lean loops over them.

## Not proved in Lean

- The slice-EO rule itself (`b ^ g_e(place kind) ^ g_e(piece kind)`): F counts with the rule as given. The Python tries the rule against the sticker model on 200 random states (`seo_skip.check_rule`).
- That the two walks of `Invariant.lean` cover every reachable state: this is the short argument at the top of that file. It uses three things read off the code of `fe.look` (it reads a state only through the colour axes of its stickers; its corner loop reads corner places only; its edge loop reads edge places only) and `moves_keep_corners_and_edges`.
- That the DR-xs move set and the cost count (one group = its face turns, no two groups in a row about one axis) are the right model of solving; that is the study's business, not the certificate's.
