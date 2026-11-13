---

## Appendix A: every type and length

The full tables behind section 6: every even skeleton length from 10 to 30, every type, random skeletons. The first column is the cap and what was inserted. Rows at caps 10 and 12, and the comm-plus-alg rows, are **computer only** (every alg of that length); the cap-8 rows are best pairs of 8-movers, which a hand search following the first comms a move worse gets close to (8.4):

- *one comm*: one 3-cycle alg (3c and 3e only);
- *two comms*: two 3-cycle algs, nesting allowed;
- *one alg*: one alg for the whole leftover;
- *best of the two*: the shorter of two comms and one alg on each skeleton, over the skeletons where two comms was run.

A block is left out when nothing of that length exists (no alg of 8 or fewer does a 5c, and so on). The *Skeletons* column is the size of the sample behind each row. *Mean moves added* is over the skeletons where something fits; the *Adds k or less* shares are of all skeletons. Each table below is one leftover, one row per cap, model and skeleton length.

**3c**: one row per cap, model and skeleton length.

{{app_cost_3c}}

**2tc**: one row per cap, model and skeleton length.

{{app_cost_2tc}}

**3tc**: one row per cap, model and skeleton length.

{{app_cost_3tc}}

**Pure 2c2c**: one row per cap, model and skeleton length.

{{app_cost_2c2c-pure}}

**Twisted 2c2c**: one row per cap, model and skeleton length.

{{app_cost_2c2c-twisted}}

**3c1t**: one row per cap, model and skeleton length.

{{app_cost_3c1t}}

**5c**: one row per cap, model and skeleton length.

{{app_cost_5c}}

**3c3c** (two separate corner 3-cycles): one row per cap, model and skeleton length.

{{app_cost_3c3c}}

**3e**: one row per cap, model and skeleton length.

{{app_cost_3e}}

**2fe** (two edges flipped in place): one row per cap, model and skeleton length.

{{app_cost_2f}}

**2e2e** (two swaps, no flip): one row per cap, model and skeleton length.

{{app_cost_2e2e}}

**Flipped 2e2e** (two swaps, each with a flip): one row per cap, model and skeleton length.

{{app_cost_2e2e-flipped}}

**3e1f** (a flipped 3-cycle and one flipped edge): one row per cap, model and skeleton length.

{{app_cost_3e1f}}

**5e**: one row per cap, model and skeleton length.

{{app_cost_5e}}

**3e3e** (two separate edge 3-cycles): one row per cap, model and skeleton length.

{{app_cost_3e3e}}

**Exchange rates at cap 10.** The table of 7.2 with algs up to 10 moves (3c: one comm, {= NSK('3c', L=10) =} skeletons per length; the others: best of two comms and one alg, on {= NSK('2tc', L=10) =} to {= NSK('5c', L=10) =} skeletons per length, the sizes of the cap-10 rows above, so the last digit is soft; every whole length is its own sample):

{{exchange_cap10}}

---

## Appendix B: the 3c and 3e cases

Every corner 3-cycle and every edge 3-cycle, grouped into classes: two cases are in one class when one is the other seen from another side of the cube (the 24 rotations), or its inverse. For each class a shortest alg, which pieces go where, and how many different algs of each length solve it. It's a reference to learn from: looking a case up here is **computer only**, nothing to do in an attempt.

*Pieces* reads `A>B`: the piece from A ends at B. `+1` and `+2` are a clockwise and a counter-clockwise twist of the corner as it arrives (for edges `+1` is a flip).

**Corner 3-cycles: {= STATES('3c') =} cases in {= NCLASS('3c') =} classes.** One row per class, with how many algs of each length it has.

{{classes_3c}}

**Edge 3-cycles: {= STATES('3e') =} cases in {= NCLASS('3e') =} classes.** One row per class, same columns plus 6- and 7-move algs.

{{classes_3e}}

---

## Appendix C: how it was computed, and what checks it

**The model.** One sticker-level cube built from geometry, so no permutation is typed by hand. The search program reads its move tables from it, and every solution that is printed anywhere in this study is replayed on it.

**Leftover types (section 4).** Corner states as a permutation with twists, edge states as a permutation with flips. All products of two 3-cycles and, for corners, of three are formed and sorted by cycle type. Exhaustive.

**Algorithms (section 5, Appendix B).** Every reduced move sequence of 12 moves or fewer that moves corners only or edges only, found by joining all sequences of 6 moves with all sequences of 6 (meet in the middle), then sorted by what it does. *Reduced* means no two moves in a row on one face and a fixed order for two moves on opposite faces, so each alg is counted once. For the 3-cycle families a second, independent depth-first search gives the same lists class by class. The parity (2c2e) lists come from that second search. For torchlight's statement on twisting a corner (section 5) the same join was run over every corner-only sequence of {= TW('checked') =} moves or fewer, whatever it does to the corners.

**One skeleton (everything in sections 6 to 9).** For a skeleton and a leftover I work out the state an insertion has to produce at each spot, then put in every alg within the cap for that state and cancel. For two comms, every first comm at every spot (every 3-cycle that leaves a 3-cycle) gets followed by every second comm at every spot of the result. The program only skips work where a bound proves nothing better can come out, so the minimum is exact for its cap.

**Samples.** A random skeleton is $n$ moves, each uniform among the moves that do not turn the face just turned (and that keep opposite-face pairs in the fixed order), and a leftover drawn uniformly from its type. The sizes are in section 3 and in each table; the odd lengths of section 7 have samples of their own, made the same way. Two standard errors of a mean, one row per sample:

| Leftover | Cap | Skeletons | ± two standard errors, moves |
|---|---:|---:|---:|
| 5c | 8 | 20,000 | {= SE2('5c') =} |
| 5c | 10 | 2,000 | {= SE2('5c', L=10) =} |
| 3c1t | 10 | 500 | {= SE2('3c1t', L=10) =} |
| 2tc | 10 | 200 | {= SE2('2tc', L=10) =} |
| 5c | 12 | 100 | {= SE2('5c', L=12, src='two12') =} |

**Exchange rates (section 7).** The chance of a total of $N$ or less from a skeleton of length $n$ is the share of sampled skeletons of that length whose best insertion adds $N - n$ or less. Every whole length from 10 to 30 is its own sample. The length of equal chance is read off between two whole lengths on the log-odds, and the length of equal expected total between two whole lengths on the mean.

**What checks what.**

- The search program's cube and its cancelling agree with the sticker model on random sequences.
- The sizes of all 15 leftover types come out the same three ways: by construction, among all products of two 3-cycles, and among all corner states.
- One comm: a separate Python program on the sticker model computes the best 8-mover and the best alg of up to 10 at every spot of every 3c skeleton of the samples. Its minimum equals the search program's on all {= CHECK('onepos') =} skeletons, at both caps.
- Two comms: the search agrees with a plain enumeration of every pair on small skeletons for every type, and the Python program, following up every first comm, gives the same total on {= CHECK('greedy_full') =} 5c skeletons of 20 moves.
- {= CHECK('sample_solutions') =} solutions printed in the sample files, every solution for the real skeletons ({= CHECK('real_solutions') =}) and every solution on the examples page were replayed: each solves its scramble with the stated length.
- On the Insertion Finder pages people posted, the search is never worse than Insertion Finder once its cap covers the algs Insertion Finder used (section 9).

**Formally verified.** `lean/Insertions` in the repository is a Lean 4 certificate (no Mathlib, no `sorry`). It recomputes from its own definitions, and states as theorems:

- *the leftover types (section 4)*:
  - `corner_three_cycles`, `edge_three_cycles`: there are {= STATES('3c') =} corner 3-cycles and {= STATES('3e') =} edge 3-cycles, all different, each of order 3, and the inverse of each is in the list.
  - `corner_products_of_two`: every pair of corner 3-cycles multiplied gives {= WITHIN2('corner') =} different states, and by type exactly the 5c, 3c3c, 3c1t, twisted 2c2c, pure 2c2c, 3tc and 2tc counts of section 4, the 3c1t and the 3tc as two types each, one per twist direction (plus the 3-cycles and the solved state). No other type occurs.
  - `corner_no_two_twisted_3_cycles`, `corner_no_two_swaps_with_twist`: two 3-cycles never give two twisted 3-cycles (the mixed 3c3c), nor two swaps with a twisted corner (2c2c1t).
  - `corner_type_sizes`, `corner_two_gives_whole_types`: the number of all corner states of each type, counted over all {= f'{40320 * 2187:,}' =} corner states, equals the number reached, so every state of those seven types is two 3-cycles away.
  - `edge_products_of_two`, `edge_type_sizes`, `edge_two_gives_whole_types`: the same for edges: {= WITHIN2('edge') =} states, the six edge types of section 4, each reached in full.
  - `corner_fewest_up_to_three`, `corner_three_totals`, `corner_three_gives_whole_types`: multiplying by a third 3-cycle, exactly {= THREE('types') =} more types appear (twist directions apart; {= THREE('names') =} by name), {= THREE('states') =} states, each type in full: the second table of section 4.
  - `corner_type_sizes_by_hand`, `edge_type_sizes_by_hand`: the same sizes again as plain arithmetic (which 5 corners, how many cyclic orders, how many twists).
- *first comms per spot* (`first_comms_per_spot`, 6.2): for every state of every type, the 3-cycles that leave a 3-cycle: {= FC('2tc') =} for a 2tc, {= FC('2c2c-pure') =} for either 2c2c, {= FC('3tc') =} for a 3tc, {= FC('3c1t') =} for a 3c1t, {= FC('5c') =} for a 5c.
- *the algs of 8 moves or fewer*, on a sticker cube whose 18 turns equal the Python model's (`moves_agree_with_python`), found by joining every sequence of up to 4 turns with every sequence of up to 4 turns, no pruning:
  - `corner_algs_up_to_8`, `corner_counts` (section 5): {= ALGS('3c', 8) =} corner-only sequences, all 8-move 3-cycles; {= ALGN('3c', 8) =} of the {= STATES('3c') =} 3-cycles have one, {= F8(2) =} of them two; {= FACT('oriented_3c_with_8') =} of the {= FACT('oriented_3c') =} oriented 3-cycles have one; {= FACT('no8_after_any_move_all_3c') =} have none even one move over; Jay's `R' F' R B2 R' F R B2` is one of the oriented ones (`jay_oriented_8_mover`).
  - `edge_counts` (6.6): the edge 3-cycles with an alg of 8 or fewer are {= sum(int(ALGN('3e', k)) for k in (6, 7, 8)) =}, with 6-, 7- and 8-move sequences {= ALGS('3e', 6) =}, {= ALGS('3e', 7) =} and {= ALGS('3e', 8) =}; the {= EO('six', 3) =} with a 6-mover are oriented on all three axes, and exactly that many edge 3-cycles are.
- *the corner algs of 10 moves or fewer* (`ten_facts`, the same join with halves of up to 5 turns): of the corner 3-cycles, {= ALGN('3c', 8) =} have an 8-mover, {= ALGN('3c', 9) =} more a 9-mover and {= ALGN('3c', 10) =} more a 10-mover ({= ALGS('3c', 9) =} and {= ALGS('3c', 10) =} sequences of 9 and 10 moves); a pure 2c2c has a 10-mover in {= ALGN('2c2c-pure', 10) =} cases and nothing shorter; nothing of 10 moves or fewer does a twisted 2c2c, a 3c1t, a 2tc or a 3tc.
- *the examples*: every scramble, skeleton, comm and solution of the corrections page and of [a] to [e] and [g] to [k] replays as printed (lengths, cancels, what the skeleton leaves), and the optima they state are exact over every alg of 8 moves or fewer, and of 10 or fewer where they say so:
  - [a]: 29, 29 and 30;
  - [b]: 26 with 8-movers, 25 with algs up to 10, and no 9-mover better than 26;
  - [c]: 25 at spot 16 only, and nothing better than an 8-1 on the odd spots and the ends;
  - [d]: 19;
  - [e]: 29 nested and 31 without nesting;
  - [g]: 30;
  - [h]: no 8-mover at any spot, 30 with algs up to 10;
  - [i]: 28 with 8-movers, 27 with algs up to 10;
  - [j]: 25 at spot 4 only;
  - [k]: 25 at spot 10 only, no alg under 10 moves for the case at spot 8, and the walk sees nothing better than an 8-1;
  - the 20-move 3c of 6.1 with no 8-mover: 28 with algs up to 10, and the shortest alg at each spot as printed;
  - the 23-move 3c of 9.5: 27 with 8-movers, 23 with algs up to 10.

*Computed, not proved*: the corner alg lists over 10 moves and the edge lists over 8 (cap 12, the 3c1t and 2tc alg counts, twisting in place, 2c2e), the insertion searches on the samples and on the real skeletons, every mean, share and exchange rate (the samples), and examples [f] and [l]. They rest on the cross-checks above. The proofs use `native_decide`, which trusts the Lean compiler. That the edge leftovers needing three comms are 13 types is counted in Python only, and is not used here.

---

## Docs referred to

- Sebastiano Tronto, [Fewest Moves Tutorial](https://fmcsolves.cubing.net/fmc_tutorial_ENG.pdf), version 3 (January 2020), revision 3.04 (August 2023): section 2.4 on insertions, the table in 2.4.10, the solves of Appendix D.
- Yurii Riabov, [Hitchhiker’s Guide to FMC](https://docs.google.com/document/d/16nu10y1JkUmVDC11c1h_ULzAl4Vze7zR), March 2024: which leftovers take how many comms. It links the alg sheet [DR algs with mnemonics](https://docs.google.com/document/d/1TqVjcA5DW3TzZOtxV1uzvHeYBACA4CP-lECrLuD9WAY).
- Cyprian Kalbarczyk, [Blockbuilding example solves](https://docs.google.com/document/d/1oWbbzc375q4FRIuzA5U091yaiGxt0zkFObGPe5P24_I) (solves from late 2019 to October 2022) and [FMC attempt with comments](https://docs.google.com/document/d/1_6hfBXK3cK-xZ1f7VjRH8EtSZ5hpLuV7TNFGT1zkZw8).
- Alexandros Fokianos and Tommaso Raposio, A Domino Reduction Guide, August 2019 ([shared folder](https://drive.google.com/drive/folders/1olTCi3CoDhHoKeikeDb6KFzlqIIi-CXe)).
- [Insertion Finder](https://333.fm/if): the site 333.fm is Baiqiang Dong's and the core was written by Yan Xuan (Baiqiang, [[D3803]]). The result pages people posted from it are linked in section 9.
