**The model.** One sticker-level cube with centers, built from geometry, so no permutation is typed in by hand. Everything else (the Rust tools' move tables, the Lean model) is generated from it or checked against it.

**Kinds and move counts (sections 3 and 4).** A kind is read off the stickers. I walk every kind reachable from a DR with DR-xs moves (768 per colour), and a shortest-path search over them with the cancelling rule gives the slices and turns. Exhaustive.

**Searches over cosets (6.2, 6.3).** For one colour, a cube's distance from a DR depends only on the corner twists, the edge orientations and where the E-slice pieces are: 2,217,093,120 cosets. For each target (real DR, DR-1s, DR-2s 8fe, any DR-xs) and each move rule (any turn; no quarter turns of one axis; quarter turns of that axis only when they miss the slice pieces) a BFS gives the distance from every coset. The numbers by kind of skip are counts over all cosets with that skip. Exhaustive.

**Slice-EO skips (6.1).** A count over all 70,963,200 arrangements of edge kinds and orientations. Exhaustive.

**Shortest routes on random scrambles (6.4).** A sample of {= NEARN() =} uniformly random cube states, each looked up in the coset tables for three colours and both sides.

**Finishes (section 5).** Random states, uniform over DR-1s ({= N1() =}) and over DR-2s 8fe ({= N8() =}). For each, I find the shortest solution of the method's form exactly, by trying every setup from both ends and looking up the optimal finish of the resulting DR in the first study's table. The averages carry a standard error of {= SE1() =} (DR-1s) and {= SE8() =} (8fe); the search per state is exact for its form.

**Real scrambles (section 7).** The first study's 500 scrambles: uniformly random states drawn with the EO → DR study's generator, not nissy's scrambler, which isn't uniform ([EO → DR study, appendix B](https://fmc.arhan.sh/eo-to-dr/#appendix-b-how-it-was-computed-and-what-checks-it)). Normal DRs: every DR up to 12 moves through an EO of 5 moves or less, from cubelib-cli (it lists no longer EOs), each finished optimally (first study). For 7.4 the same lists restricted to EOs of 4 or less. DR-xs: every DR-1s up to 8 moves and DR-2s 8fe up to 9 that starts from a slice-EO skip or a one-move slice EO and then keeps the EO of that axis, plus every DR-2s 8fe after an EO of at most 4 moves, each finished as in section 5 (the 8fe with setups of at most 3 moves from either end) and written out as a solution.

**What checks what.**

- The sticker model solves 100 scramble-and-solution pairs from the first study's examples page.
- The search to a real DR reproduces the known counts by distance (1, 4, 50, 592, …, 476).
- The search to any DR-xs on one colour and axis reproduces the distribution trangium posted (1, 4, 50, 586, …, 84).
- The 43 labelled DR-xs states in the server's worked examples are all classified as labelled.
- The finisher agrees with a separate sticker-level brute force on test states, and every solution it writes is replayed: {= RL('n1s', f='{:,}') =} DR-1s solutions and every 8fe solution of the 500 scrambles solve their scramble in the stated number of moves.
- The DR finish table is the Lean-certified one of the first study.

**Formally verified.** `lean/DRXs` in the repository is a Lean 4 certificate (no Mathlib, no `sorry`) that builds its own sticker cube and proves, by evaluating its own definitions:

- *the model is a cube*: every turn is a permutation, its moves equal the Python model's, and the orders of `U` and of these come out right:

  ```
  R U R' U'    // order 6
  R U          // order 105
  R U2 D' B D' // order 1260
  ```

- *the kinds (sections 3 and 4)*: exactly 768 kinds per colour (checked for the U/D and the F/B colours), and the kind of a state decides where every move takes it; 1, 140, 383 and 244 kinds need 0, 1, 2 and 3 slices; DR-1s to DR in 2 to 6 turns (1, 2, 9, 30, 28 of the 70 layouts on each pair of faces, 5.17 on average), the DR-2s and DR-3s rows of 4.1 and their averages; DR-3s to DR-2s in 2 turns for all 244 and free after a trigger; DR-2s to DR-1s in 2, 3 or 4 turns, free after a trigger for 209 of 383 and 3 for the rest (the whole after-trigger table of 4.3); Simon's 1, 4, 13, 36, 16;
- *the slice-EO rule*, for every way an edge can sit and each axis, on normal and on inverse, from the stickers. So the slice-EO count of 6.1 is exact for the cube: of 70,963,200 arrangements, 22,143,888 have no skip on normal and 14,678,928 none on either side, 2.25 skips per scramble over both sides (exactly 18/8);
- *turns to a slice EO for one slice* (6.1): all four rows of that table, over the 7,920 placements;
- *6.3 from a full EO*: the renaming turns each face turn into a face turn and an 8fe into a real DR, and over all 1,082,565 positions with a full EO, with moves that keep it, the distance to the 8fe equals the distance of the renamed position to the DR, position by position, so the two columns of the 6.3 table are the same (7.80 on average; the DR column also matches the separate Lean search of [*When to switch an EO*](../eo-switch/));
- *printed examples*, each with the stated kind, flipped edges, slices and fewest turns, and its printed fix reaching DR in the printed number of turns:
  - the 12-bad scramble of the errata and of section 8 (theorem `errata_B1`);
  - the wrong-slice example of 5.4 (theorems `errata_B3` and `errata_B3_nissy`), with the shortest DRs on any axis by brute force, 4 on normal and 6 on the inverse;
  - the 6-turn layout `UB UF BR FR` of Appendix A, its scramble and its fix (theorem `errata_B2_six`);
  - Simon's thirteen rows (theorems `simon_count`, `simon13_rows_U`, `simon13_rows_D`).

*Computed, not proved*: the searches over 2.2 billion cosets (6.2, 6.4, the rest of 6.3, including "with any moves" and the twelve targets), the finish samples (section 5), the 500 real scrambles (section 7), Appendix A's other rows, Appendix B, and two scrambles of section 8 with nissy's shortest DRs: the DR-1s that is 6 turns from a DR from either side, and the one for the ninth case of Rodney's restatement. They rest on the cross-checks above. The proofs use `native_decide`, which trusts the Lean compiler.
