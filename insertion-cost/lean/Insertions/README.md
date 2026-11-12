# Insertions — a Lean 4 certificate for what one, two or three 3-cycles can make

Lean 4.35.0, no Mathlib (only the library that ships with Lean, `Std.HashMap` and `Std.HashSet` included). About 700 lines, no `sorry`.

The case study "Insertion cost by skeleton type" needs, as exact facts, which kinds of leftover one or two inserted 3-cycles can solve. They are computed in Python by `research/src/leftover_types.py` (output in `research/out/types.json`). This project does the computation again in Lean, from its own definitions, and states each resulting number as a theorem. Every number below that the Python prints is the number the Python prints; none had to be changed.

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

## Files

| File | Content |
|---|---|
| `Insertions/LeftoverTypes.lean` | `leftover_types.py`: `mul`, `ident`, `three_cycles`, `ctype`, `name`, `run`, with the Python's names. **Read this next to the Python.** |
| `Insertions/Products.lean` | What B to D are stated with: `products_of_two` (the set of all products, as a list), `by_type`, `count_distinct`, `count_in`, `cycles`, `twisted_cycles`. |
| `Insertions/AllStates.lean` | The full count: `permutations`, `twists`, `type_sizes` (go through every state), `type_size_by_places` (the shortcut for edges), and the positions `perm_index`, `twist_index`. |
| `Insertions/Three.lean` | `fewest_by_type`: the Python's loop run a third time, with the set of seen states kept as a table of 88,179,840 bytes. |
| `Insertions/Theorems.lean`, `Insertions/ThreeTheorems.lean` | The theorems. |
| `Insertions/Audit.lean` | `#print axioms` for every theorem. |
| `check_by_classes.py` | Not part of the build: a second count of the same tables in Python by another method (one state per type and a formula for the size of a type). It prints the tables of B, D and E, and the edge types that need three. |

Each definition file starts with a "Python -> Lean" note.

## Build

    source /data/fmc/env.sh
    cd /data/fmc/insertion-cost/lean/Insertions
    systemd-run --user --scope -q -p MemoryMax=2G lake build

From a clean tree this took 3 minutes on the 4-core VM (measured: 181 s wall, 164 s of CPU) while other jobs were using most of the cores. Nearly all of it is two steps that run one after the other: `Theorems` (62 s, of which about 40 s is the count over all 88,179,840 corner states in `corner_type_sizes`) and `ThreeTheorems` (114 s: the 217 million products of `corner_fewest_up_to_three`). Everything else takes a few seconds. A whole build on a quiet machine was not timed; single runs on the quiet machine took 37 s for that count and 100 s for those products (the latter before a small speed-up). With all four cores busy elsewhere the same build has taken 8 and a half minutes. The last step prints the audit (`Audit.lean`).

Memory: the build's own peak was 0.53 GB (the control group that `MemoryMax=2G` limits); the largest single process showed 1.0 GB resident, which counts the Lean toolchain's files mapped into it.

`lakefile.toml` sets `precompileModules = true`, as in the earlier studies: the definitions are compiled to machine code before the theorem files run them. Without it they would run in the interpreter (the two calls of `run` then take 2 minutes instead of 5 seconds).

## Trust

- Every theorem that runs a computation is proved by `native_decide`: Lean compiles the statement, runs it, and accepts the answer `true`. This trusts the Lean compiler and the C compiler, not only Lean's kernel. `Audit.lean` shows it as one axiom per such theorem, named `<theorem>._native.native_decide.ax_…`, next to Lean's three standard axioms. The kernel does not replay these computations.
- Checked by the kernel alone, no such axiom: `corner_type_sizes_by_hand` and `edge_type_sizes_by_hand` (`decide`, plain arithmetic).
- Read off earlier theorems by the kernel, so depending on their runs and no new one: `corner_two_gives_whole_types` (from `corner_products_of_two` and `corner_type_sizes`), `edge_two_gives_whole_types` (from `edge_products_of_two` and `edge_type_sizes`), `corner_three_totals` (from `corner_fewest_up_to_three`), `corner_three_gives_whole_types` (from `corner_fewest_up_to_three` and `corner_type_sizes`).
- What a theorem says is exactly what its Lean statement says about the Lean definitions. That those definitions are the Python's is for the reader to check; `LeftoverTypes.lean` is about 150 lines and follows the Python line by line, and `corner_run`, `edge_run` reproduce its output.
- The model is the Python's (permutation and twist of each kind of piece on its own). Nothing here ties it to face turns; the study does that elsewhere.

## Where the Lean differs from the Python

- **`three_cycles`** returns a list in the order the loops make it; the Python collects a set and sorts it. `(-oi - oj) % m` is written `(2 * m - oi - oj) % m` because Lean's natural numbers have no negatives. `itertools.permutations(range(n), 3)` is three loops that skip equal indices.
- **`mul`** fills the two tuples in one loop instead of two generator expressions.
- **`run`** returns the types sorted as the Python prints them (fewest 3-cycles, then most states). Where two types have equally many states (2e2e and 2e2e-flipped) the Lean puts them in alphabetical order; the Python prints them in the order its set happened to give (2e2e-flipped first). It prints nothing and writes no file.
- **More than the Python:** the products as a list of states counted by exact type (`products_of_two`, `by_type`: the Python's names merge `[(3, 2), (1, 1)]` with `[(3, 1), (1, 2)]` and the two kinds of three twisted corners); the full sizes of the types (`AllStates.lean`); the third round (`Three.lean`).
- **`fewest_by_type`** (E) keeps the states it has met in a byte table indexed by the position of the state in the list of all states, not in a set. This is the only encoding in the project; `every_state_once` checks the two position functions against the lists themselves.

## Not proved in Lean

- That a state of one of these types is a conjugate of every other state of the type (which is why whole types come out). The certificate does not use it: the `…_whole_types` theorems compare counts. `check_by_classes.py` does use it, and agrees.
- The full sizes of the edge types rest on the step "choose the k places, then count on k places" (`type_size_by_places`), checked against the full count for corners only.
- Anything about four or more 3-cycles, or about three edge 3-cycles (by the count of `check_by_classes.py`, not certified, 13 edge types need three and 172,074,266 edge states are within three).
