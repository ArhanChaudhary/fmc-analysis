**The model.** One sticker-level cube with centers, built from geometry, so no permutation is typed by hand. Everything else (the Rust tools' move tables, the Lean model) is generated from it or checked against it.

**Kinds and move counts (sections 3 and 4).** A kind is read off the stickers. All kinds reachable from a DR with DR-xs moves are walked (768 per colour), and a shortest-path search over them with the cancelling rule gives the slices and turns. Exhaustive.

**Searches over cosets (6.2, 6.3).** For one colour, a cube's distance from a DR depends only on the corner twists, the edge orientations and where the E-slice pieces are: 2,217,093,120 cosets. For each target (real DR, DR-1s, DR-2s 8fe, any DR-xs) and each move rule (any turn; no quarter turns of one axis; quarter turns of that axis only when they miss the slice pieces) a breadth-first search gives the distance from every coset. The numbers by kind of skip are counts over all cosets with that skip. Exhaustive.

**Slice-EO skips (6.1).** A count over all 70,963,200 arrangements of edge kinds and orientations. Exhaustive.

**Shortest routes on random scrambles (6.4).** A sample of {= NEARN() =} uniformly random cube states, each looked up in the coset tables for three colours and both sides.

**Finishes (section 5).** Random states, uniform over DR-1s ({= N1() =}) and over DR-2s 8fe ({= N8() =}). For each, the shortest solution of the method's form is found exactly, by trying every setup from both ends and looking up the optimal finish of the DR that results in the first study's table. The averages carry a standard error of {= SE1() =} (DR-1s) and {= SE8() =} (8fe); the search per state is exact for its form.

**Real scrambles (section 7).** The first study's 500 scrambles: uniformly random states drawn with the EO → DR study's generator. An earlier version of this page used nissy's scrambler, which is not uniform ([EO → DR study, appendix B](https://fmc.arhan.sh/eo-to-dr/#appendix-b-how-it-was-computed-and-what-checks-it)). Normal DRs: every DR up to 12 moves through an EO of 5 moves or less, from cubelib-cli (it lists no longer EOs), each finished optimally (first study). For 7.4 the same lists restricted to EOs of 4 or less. DR-xs: every DR-1s up to 8 moves and DR-2s 8fe up to 9 that starts from a slice-EO skip or a one-move slice EO and then keeps the EO of that axis, plus every DR-2s 8fe after an EO of at most 4 moves, each finished as in section 5 (the 8fe with setups of at most 3 moves from either end) and written out as a solution.

**What checks what.**

- The sticker model solves 100 scramble-and-solution pairs from the first study's examples page.
- The search to a real DR reproduces the known counts by distance (1, 4, 50, 592, …, 476).
- The search to any DR-xs on one colour and axis reproduces the distribution trangium posted (1, 4, 50, 586, …, 84).
- The 43 labelled DR-xs states in the server's worked examples are all classified as labelled.
- The finisher agrees with a separate sticker-level brute force on test states, and every solution it writes is replayed: {= RL('n1s', f='{:,}') =} DR-1s solutions and every 8fe solution of the 500 scrambles solve their scramble in the stated number of moves.
- The DR finish table is the Lean-certified one of the first study.

**Lean.** `lean/DRXs` in the repository proves, by evaluation of its own definitions (no Mathlib):

- the model is a cube: every turn is a permutation, the orders of `U`, `R U R' U'` (6), `R U` (105) and `R U2 D' B D'` (1260), and that its moves equal the Python model's;
- exactly 768 kinds are reached, 256 per pair of faces, and the kind of a state decides where every move takes it (checked over all reachable corner and edge colourings, not just one state per kind);
- the slices: 1, 140, 383 and 244 kinds need 0, 1, 2 and 3;
- the turns to DR: 2, 4, 18, 60, 56 kinds of DR-1s at 2 to 6 turns and none above; the DR-2s and DR-3s rows of 4.1; DR-3s to DR-2s in 2 turns for all 244; DR-2s to DR-1s in 2, 3 or 4 turns for 209, 102 and 72;
- the slice-EO count: of 70,963,200 arrangements, 22,143,888 have no skip on normal and 14,678,928 none on either side.

The proofs use `native_decide`, which trusts the Lean compiler. The searches over 2.2 billion cosets, the finish samples and the real scrambles are not in Lean; they rest on the cross-checks above.
