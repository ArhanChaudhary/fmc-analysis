# Insertions — a Lean 4 certificate for what one, two or three 3-cycles can make, the algs of 8 moves or fewer, and the printed examples

Lean 4.35.0, no Mathlib (only the library that ships with Lean, `Std.HashMap` and `Std.HashSet` included). About 1,800 lines, no `sorry`.

The case study "Insertion cost by skeleton type" needs, as exact facts, which kinds of leftover one or two inserted 3-cycles can solve. They are computed in Python by `research/src/leftover_types.py` (output in `research/out/types.json`). This project does the computation again in Lean, from its own definitions, and states each resulting number as a theorem. Every number below that the Python prints is the number the Python prints; none had to be changed.

Since November 2026 it also holds (parts F, G and H): the number of first comms per spot for each leftover type, every corner-only and edge-only alg of 8 moves or fewer and every corner-only alg of 10 or fewer on a sticker cube with face turns, and a replay of the examples printed on the corrections page and in the write-up, with their best insertions (8-movers, and algs up to 10 where the page gives them) recomputed by brute force. Those parts share no code with the study's Rust and Python.

Words: a *state* is (perm, twist): the piece `perm[i]` sits at place i with `twist[i]`, twists mod 3 for the 8 corners, flips mod 2 for the 12 edges. A *3-cycle* moves three pieces around, with any twists that add up to 0, and touches nothing else (1008 for corners, 1760 for edges). The *type* of a state is its list of cycles as (length, twist sum), largest first, leaving out the pieces that are in place and untwisted: `[(3, 1), (1, 2)]` is a 3-cycle whose twists add up to 1 plus one corner twisted by 2 in place; the solved state is `[]`. In the function calls, `8 3` means corners and `12 2` edges.

## What is proved

**A. The 3-cycles** (`Insertions/Theorems.lean`)

| Theorem | It says |
|---|---|
| `corner_three_cycles` | The list has 1008 corner 3-cycles, all different; each is one 3-cycle with twist sum 0 and nothing else touched; each has order 3 (it is not solved, done three times it is); the inverse of each, which is the 3-cycle done twice, is in the list. |
| `edge_three_cycles` | The same for the 1760 edge 3-cycles. |

That 1008 and 1760 are *all* such states is in `corner_type_sizes` and `edge_type_sizes` (type `[(3, 0)]`).

**B. Corners, two 3-cycles**

| Theorem | It says |
|---|---|
| `corner_products_of_two` | Multiplying every ordered pair of corner 3-cycles gives 216,511 different states, the solved state and all 1008 3-cycles among them. By type: `[(5, 0)]` 108,864; `[(3, 0), (3, 0)]` 90,720; `[(3, 2), (1, 1)]` 5,040; `[(3, 1), (1, 2)]` 5,040; `[(2, 2), (2, 1)]` 3,780; `[(2, 0), (2, 0)]` 1,890; `[(3, 0)]` 1,008; `[(1, 2), (1, 2), (1, 2)]` 56; `[(1, 2), (1, 1)]` 56; `[(1, 1), (1, 1), (1, 1)]` 56; `[]` 1. No other type occurs. |
| `corner_run` | `run "corner"` returns what the Python prints: 1008 3-cycles; with two 3-cycles 5c 108,864, 3c3c 90,720, 3c1t 10,080, 2c2c-twisted 3,780, 2c2c-pure 1,890, 3tc 112, 2tc 56; 216,511 states within two. |

**C. Corners: what two 3-cycles cannot make, and what they make in full**

| Theorem | It says |
|---|---|
| `corner_no_two_twisted_3_cycles` | No product of two corner 3-cycles is a pair of 3-cycles that both have a twist sum other than 0 (type `[(3, 2), (3, 1)]`), nor holds such a pair next to anything else. |
| `corner_no_two_swaps_with_twist` | No product of two corner 3-cycles holds two swaps together with a corner twisted in place. |
| `every_state_once` | The two lists that the full count walks through are complete, for up to 8 pieces and twists mod 2 or 3: n! permutations and m^(n-1) twist vectors with total 0, each entry valid and at its own position. |
| `corner_type_sizes` | The full size of 33 corner types (the 11 of B and the 22 of E), counted by going through all 8! × 3^7 = 88,179,840 corner states and taking the type of each. |
| `corner_two_gives_whole_types` | For each of the 11 types of B, the number of all corner states of that type equals the number of products of that type. The products are different states, so every state of the type is a product of two 3-cycles. |
| `corner_type_sizes_by_hand` | The same sizes (solved state aside) as arithmetic, with the count explained line by line; for example a 5-cycle with twist sum 0: which 5 corners, 4! cyclic orders, 3^4 twists, C(8,5) · 4! · 81 = 108,864. |

**D. Edges, two 3-cycles**

| Theorem | It says |
|---|---|
| `edge_products_of_two` | Multiplying every ordered pair of edge 3-cycles gives 925,035 different states, the solved state and all 1760 3-cycles among them. By type: `[(3, 0), (3, 0)]` 591,360; `[(5, 0)]` 304,128; `[(3, 1), (1, 1)]` 15,840; `[(2, 1), (2, 1)]` 5,940; `[(2, 0), (2, 0)]` 5,940; `[(3, 0)]` 1,760; `[(1, 1), (1, 1)]` 66; `[]` 1. No other type occurs. |
| `edge_run` | `run "edge"` returns what the Python prints: 1760 3-cycles; with two 3-cycles 3e3e 591,360, 5e 304,128, 3e1f 15,840, 2e2e 5,940, 2e2e-flipped 5,940, 2f 66; 925,035 states within two. |
| `edge_type_sizes` | The full size of each of the 8 edge types of `edge_products_of_two`. The 12! × 2^11 edge states are too many to go through, so the size is (12 choose k) × the number of states of that type on k places, k being the number of places the type touches, and only that second number is counted by going through all states (on k ≤ 6 places). |
| `corner_type_sizes_by_places` | That shortcut gives the right sizes for 32 of the 33 corner types of `corner_type_sizes` (the last one touches all 8 places, so there the shortcut is the full count). |
| `edge_two_gives_whole_types` | For each of the 8 types, the full size equals the number of products of that type: every state of the type is a product of two 3-cycles. |
| `edge_type_sizes_by_hand` | The same sizes (solved state aside) as arithmetic, explained line by line; for example an unflipped 5-cycle: C(12,5) · 4! · 2^4 = 304,128. |

**E. Corners, three 3-cycles** (`Insertions/ThreeTheorems.lean`; not in the Python)

| Theorem | It says |
|---|---|
| `corner_fewest_up_to_three` | Multiplying on by every 3-cycle a third time: the number of states of each type that are a product of k 3-cycles and of no fewer, for k = 0, 1, 2, 3. k ≤ 2 repeats B. Exactly three are needed by 22 types: `[(7, 0)]` 4,199,040; `[(5, 0), (3, 0)]` 1,959,552; `[(3, 2), (3, 0), (1, 1)]` 362,880; `[(3, 1), (3, 0), (1, 2)]` 362,880; `[(5, 2), (1, 1)]` 326,592; `[(5, 1), (1, 2)]` 326,592; `[(3, 0), (2, 2), (2, 1)]` 272,160; `[(4, 2), (2, 1)]` 204,120; `[(4, 1), (2, 2)]` 204,120; `[(4, 0), (2, 0)]` 204,120; `[(3, 2), (3, 1)]` 181,440; `[(3, 0), (2, 0), (2, 0)]` 136,080; `[(3, 0), (1, 2), (1, 1)]` 20,160; `[(2, 2), (2, 0), (1, 1)]` 15,120; `[(2, 1), (2, 0), (1, 2)]` 15,120; `[(3, 2), (1, 2), (1, 2)]` 10,080; `[(3, 1), (1, 1), (1, 1)]` 10,080; `[(3, 0), (1, 2), (1, 2), (1, 2)]` 10,080; `[(3, 0), (1, 1), (1, 1), (1, 1)]` 10,080; `[(2, 2), (2, 2), (1, 2)]` 7,560; `[(2, 1), (2, 1), (1, 1)]` 7,560; `[(1, 2), (1, 2), (1, 1), (1, 1)]` 420. |
| `corner_three_totals` | That is 22 types and 8,845,836 states; 9,062,347 corner states are a product of at most three 3-cycles, of the 44,089,920 that 3-cycles reach at all. |
| `corner_three_gives_whole_types` | For each of the 22 types, the number found equals the full size of the type (`corner_type_sizes`): every state of the type needs exactly three. |

The two types asked about in C are both in this list: two 3-cycles with twist sums 2 and 1, and two swaps plus a twisted corner (`[(2, 2), (2, 0), (1, 1)]`, `[(2, 1), (2, 0), (1, 2)]`, `[(2, 2), (2, 2), (1, 2)]`, `[(2, 1), (2, 1), (1, 1)]`), need three 3-cycles.

**F. First comms per spot** (`Insertions/FirstComms.lean`, `Insertions/FirstCommsTheorem.lean`)

| Theorem | It says |
|---|---|
| `first_comms_per_spot` | For every state x of every type two corner 3-cycles make, the number of corner 3-cycles c with c⁻¹x a 3-cycle (the first comms that leave a 3c at a spot): 5c 5, 3c3c 2, 3c1t 9, twisted and pure 2c2c 24, 3c 54, 3tc 18, 2tc 108. One value per type, so it holds at every spot of every skeleton. |

**G. Face turns: the algs of 8 moves or fewer and the printed examples** (`Insertions/ErrataTheorems.lean`, `Insertions/WitnessTheorems.lean`)

The sticker cube is `Cube.lean`, copied from `is-dr-xs-worth-it/lean/DRXs` (the study's `cube.py` is byte-identical to that study's). `Replay.lean` adds, written for this check and not ported from the study's code: cancelling as the normal form of a word (turns of one face add mod 4, turns of opposite faces commute), inserting, what a state leaves on the corners in the words the pages use (with "clockwise" defined by a 120-degree rotation about the corner), and `checkBlock`, which replays a printed block (skeleton line with marks, `* = alg // (8-3/25)` lines, an optional second skeleton line, the `Solution:` line) from the text itself. `Search.lean` lists every alg of at most 8 moves that touches only corners (or only edges) by joining every sequence of at most 4 turns (all 111,151, cancelling or not) with every such sequence, and finds best insertions by brute force with no pruning (one comm per spot; two comms, the second anywhere in the cancelled result, nesting included).

| Theorem | It says |
|---|---|
| `moves_agree_with_python` | The 18 turns built from geometry are the ones cube.py builds. |
| `corner_algs_up_to_8` | 864 corner-only sequences of at most 8 moves, all of 8 moves, all corner 3-cycles; they do 528 different things, 192 with one sequence and 336 with two. |
| `corner_counts` | On the sticker cube: 1008 corner 3-cycles, 112 of them leaving all three corners oriented, 32 of those with an 8-mover; the 8-movers and their one-move conjugates reach 896 3-cycles, so 112 have no 8-mover even one move over. |
| `jay_oriented_8_mover` | `R' F' R B2 R' F R B2` (Jay's answer to "There arent 8 movers if they're oriented") is an 8-move corner 3-cycle that leaves all three corners oriented. |
| `edge_counts` | 168 edge 3-cycles have an alg of at most 8 moves (24, 48, 96 by shortest length 6, 7, 8), with 96, 240 and 2,496 sequences of 6, 7 and 8 moves; the 24 with a 6-mover are oriented on all three axes (the usual EO rule and its two rotations), and exactly 24 edge 3-cycles are. |
| `A1_blocks_replay`, `A1_best_two` | Corrections page A1: the three typical skeletons replay as printed (20 moves, the printed leftovers and types, the printed cancels and lengths, solutions that solve), and 29, 29, 30 are the best with two algs of at most 8 moves, at any spots, nested or not. |
| `A2_example`, `A2_pair_swapped` | A2: the block replays; the best 8-mover insertion is 25, at spot 16 only and by one alg only; the odd spots and both ends give at best 27; spot 14 also gives at best 27; with `F' B` written `B F'` the alg moved one move over gives 25 between the two and replays to the same solution. |
| `A3_example` | A3: the 19-move 5c replays and 30 is its best with two algs of at most 8 moves. |
| `example_d_negative`, `example_e_nested`, `example_j_third`, `examples_no_8_mover` | Write-up examples [d] (19, below the skeleton's 20), [e] (29 with nesting; 31 with both comms put into the skeleton itself), [j] (25 at spot 4 only; every third spot from the start and the end give at best 27), [h] and the 20-move 3c of section 3 (no 8-mover at any spot; their 9- and 10-move blocks replay). |

**H. The corner algs of 10 moves or fewer, and the cap-10 parts of the examples** (`Insertions/TenTheorems.lean`)

`Search10.lean` is the join of G with halves of up to 5 turns (2,000,719 of them), matched by a 64-bit mix of the stickers; every sequence kept is checked on the cube. `Ten.lean` makes the list once and reads everything off it.

| Theorem | It says |
|---|---|
| `ten_facts` | Every corner-only alg of at most 10 moves, by type: 3-cycles with shortest alg 8, 9, 10: 528, 336, 80 states (864, 1,728, 11,856 sequences); pure 2c2c: 132 states with a 10-mover, nothing shorter (1,296 sequences); 5-cycles 1,152 and pairs of 3-cycles 704 at 10 moves; no twisted 2c2c, 3c1t, 2tc or 3tc; the other types are a 4-cycle with a swap (24 states at 9 moves, 432 at 10), four swaps (3) and two 4-cycles (18), which need three comms. Examples: [b] 26 / 26 / 25 with algs up to 8 / 9 / 10; [i] 28 and 27; [k] the 8-mover results spot by spot (25 at spot 10 only), 8-movers for the cases at spots 0, 2, 4, 6 and nothing under 10 moves at spot 8, the printed 10-mover right for spot 8; [h] 30; the 20-move 3c with no 8-mover: 28, and the shortest alg at each spot; the 23-move 3c of 9.5: 27 and 23. |
| `ten_blocks_replay` | The printed blocks of [b], [i], [k] and of the 23-move 3c replay, and the 22-move solution found by hand there solves the scramble. |

## Files

| File | Content |
|---|---|
| `Insertions/LeftoverTypes.lean` | `leftover_types.py`: `mul`, `ident`, `three_cycles`, `ctype`, `name`, `run`, with the Python's names. **Read this next to the Python.** |
| `Insertions/Products.lean` | What B to D are stated with: `products_of_two` (the set of all products, as a list), `by_type`, `count_distinct`, `count_in`, `cycles`, `twisted_cycles`. |
| `Insertions/AllStates.lean` | The full count: `permutations`, `twists`, `type_sizes` (go through every state), `type_size_by_places` (the shortcut for edges), and the positions `perm_index`, `twist_index`. |
| `Insertions/Three.lean` | `fewest_by_type`: the Python's loop run a third time, with the set of seen states kept as a table of 88,179,840 bytes. |
| `Insertions/Theorems.lean`, `Insertions/ThreeTheorems.lean` | The theorems. |
| `Insertions/FirstComms.lean`, `Insertions/FirstCommsTheorem.lean` | F: `first_comms`, `first_comms_by_type`; the theorem. |
| `Insertions/Cube.lean`, `Insertions/PyMoves.lean` | The sticker cube and cube.py's 18 turns, copied from `is-dr-xs-worth-it/lean/DRXs`. |
| `Insertions/Replay.lean` | Words, cancelling, inserting, the leftover in words, `checkBlock`. |
| `Insertions/Search.lean` | The algs of at most 8 moves (`joined`, `cornerAlgs`, `edgeAlgs`), `perSpot`, `best2`, `cornerType`. |
| `Insertions/Counts.lean` | Definitions for the counts and for [e]: `bestFlat`, `cyclePlacements`, `cornerOriented`, `edgeOrientedOn`, `cornerCovered`. |
| `Insertions/ErrataTheorems.lean`, `Insertions/WitnessTheorems.lean` | G. The block strings are copied from `research/src/report_build/wit_*.md`. |
| `Insertions/Search10.lean`, `Insertions/Ten.lean`, `Insertions/TenTheorems.lean` | H: `joinedUpTo`, `summary`; `tenFacts` and the block strings; the theorems. |
| `Insertions/Audit.lean` | `#print axioms` for every theorem. |
| `check_by_classes.py` | Not part of the build: a second count of the same tables in Python by another method (one state per type and a formula for the size of a type). It prints the tables of B, D and E, and the edge types that need three. |

Each definition file starts with a "Python -> Lean" note.

## Build

    source /data/fmc/env.sh
    cd /data/fmc/insertion-cost/lean/Insertions
    systemd-run --user --scope -q -p MemoryMax=3G lake build

From a clean tree, with F and G in (2026-11-13): 9 min 18 s wall and 6 min 32 s of CPU on the 4-core VM while other jobs kept all four cores busy (load 7 to 9); on a quiet machine expect less than the CPU time, since the theorem files run side by side. By step, as lake reported them under that load: `ThreeTheorems` 304 s (the 217 million products of `corner_fewest_up_to_three`), `Theorems` 214 s (mostly the count over all 88,179,840 corner states in `corner_type_sizes`), `FirstCommsTheorem` 152 s (218 million products), `ErrataTheorems` 30 s, `WitnessTheorems` 30 s, `Counts` 22 s, `Audit` 19 s; everything else a second or two. Before F and G were added the same build took 181 s wall (164 s of CPU) under lighter load. H was added after that measurement and built on its own: `TenTheorems` 327 s wall, 4 min 30 s of CPU, so a clean build is now about 11 minutes of CPU. The last step prints the audit (`Audit.lean`).

Memory: the build's own peak was 0.95 GB without H (the control group that `MemoryMax` limits; three theorem files run at once); the largest single process showed 0.73 GB resident. `TenTheorems` alone takes 0.8 GB resident, so with it running next to the others allow 2 GB; the limit above is 3 GB.

In G every file that imports `Search.lean` computes the two alg lists once when it is loaded (about 10 s), which is why the theorem files share them. Definitions sit in files of their own (`Search`, `Counts`, `FirstComms`) so that the theorem files run them compiled.

`lakefile.toml` sets `precompileModules = true`, as in the earlier studies: the definitions are compiled to machine code before the theorem files run them. Without it they would run in the interpreter (the two calls of `run` then take 2 minutes instead of 5 seconds).

## Trust

- Every theorem that runs a computation is proved by `native_decide`: Lean compiles the statement, runs it, and accepts the answer `true`. This trusts the Lean compiler and the C compiler, not only Lean's kernel. `Audit.lean` shows it as one axiom per such theorem, named `<theorem>._native.native_decide.ax_…`, next to Lean's three standard axioms. The kernel does not replay these computations.
- Checked by the kernel alone, no such axiom: `corner_type_sizes_by_hand` and `edge_type_sizes_by_hand` (`decide`, plain arithmetic).
- Read off earlier theorems by the kernel, so depending on their runs and no new one: `corner_two_gives_whole_types` (from `corner_products_of_two` and `corner_type_sizes`), `edge_two_gives_whole_types` (from `edge_products_of_two` and `edge_type_sizes`), `corner_three_totals` (from `corner_fewest_up_to_three`), `corner_three_gives_whole_types` (from `corner_fewest_up_to_three` and `corner_type_sizes`).
- What a theorem says is exactly what its Lean statement says about the Lean definitions. That those definitions are the Python's is for the reader to check; `LeftoverTypes.lean` is about 150 lines and follows the Python line by line, and `corner_run`, `edge_run` reproduce its output.
- A to F use the Python's model (permutation and twist of each kind of piece on its own), with no face turns. G works on the sticker cube with face turns; it does not use A to F, except that the page reads its counts next to them.
- G's and H's lists of algs rest on one fact that is not proved in Lean: a sequence `a ++ b` leaves the edges home exactly when the edge stickers of `b`'s state equal those of the state of `a` reversed (a property of permutations). It is what makes the list complete. Every alg that is listed is replayed on the cube, so the list holds nothing wrong.
- In G a state's "need" at a spot is computed by doing the sequence `inv(s[:i]) ++ inv(z) ++ inv(s[i:])` on the cube, not by composing states, and every printed solution is checked by doing it.

## Where the Lean differs from the Python

- **`three_cycles`** returns a list in the order the loops make it; the Python collects a set and sorts it. `(-oi - oj) % m` is written `(2 * m - oi - oj) % m` because Lean's natural numbers have no negatives. `itertools.permutations(range(n), 3)` is three loops that skip equal indices.
- **`mul`** fills the two tuples in one loop instead of two generator expressions.
- **`run`** returns the types sorted as the Python prints them (fewest 3-cycles, then most states). Where two types have equally many states (2e2e and 2e2e-flipped) the Lean puts them in alphabetical order; the Python prints them in the order its set happened to give (2e2e-flipped first). It prints nothing and writes no file.
- **More than the Python:** the products as a list of states counted by exact type (`products_of_two`, `by_type`: the Python's names merge `[(3, 2), (1, 1)]` with `[(3, 1), (1, 2)]` and the two kinds of three twisted corners); the full sizes of the types (`AllStates.lean`); the third round (`Three.lean`).
- **`fewest_by_type`** (E) keeps the states it has met in a byte table indexed by the position of the state in the list of all states, not in a set. This is the only encoding in the project; `every_state_once` checks the two position functions against the lists themselves.

## Not proved in Lean

- That a state of one of these types is a conjugate of every other state of the type (which is why whole types come out). The certificate does not use it: the `…_whole_types` theorems compare counts. `check_by_classes.py` does use it, and agrees.
- The full sizes of the edge types rest on the step "choose the k places, then count on k places" (`type_size_by_places`), checked against the full count for corners only.
- The corner algs of more than 10 moves and the edge algs of more than 8 (so nothing about cap 12, the 3c1t and 2tc alg counts, twisting in place or 2c2e); no insertion search on the samples or on the real skeletons; examples [f] and [l] (the greedy rule).
- Anything about four or more 3-cycles, or about three edge 3-cycles (by the count of `check_by_classes.py`, not certified, 13 edge types need three and 172,074,266 edge states are within three).
