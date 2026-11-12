# EO → DR and scramble → DR: what to compute

Fourth case study for fmc.arhan.sh, suggested by a top solver: "try asking things about EO->DR and scrambled->DR".
The questions come from the server's register, `/data/fmc/kb/reread/eodr_register.md` (top tables: Prior work,
Open questions, Disputed claims; entry ids like S-DR-6 below refer to it), its examples
`/data/fmc/kb/reread/eodr_examples.jsonl` (416), and the docs digest `/data/fmc/kb/reread/eodr_docs.md`.

## What already exists (credit it; do not present it as new)
- EO→DR for one DR axis, EO-preserving moves, linear: exact for every case (Cale doc 6: 1,082,565 states, mean 7.80,
  max 10; Louis doc 108 by DRM × ARM; KrzychXyz doc 136; Evan doc 363; Rodney doc 274). With EO-breaking moves:
  torchlight T2600 (7.797 against 7.803). FakeMMAP T2598 the same distribution.
- Scramble→DR on one fixed axis, linear: DougCube doc 218 (mean 9.5245, max 12); Kociemba phase 1.
- Scramble→EO: fixed axis 4.609; best NISS EO over all axes 3.455 (doc 218, Joba T9374).
- Our own DR-xs study, section 6.4: shortest DR over 3 axes × normal/inverse, linear, any moves: 8.76 on 2,000,000
  scrambles, 92% ≤ 9. Its exact coset tables are reusable (below).

## Model and tools to reuse
- Coset space for one DR colour: (co 2187, eo 2048 for the F/B axis, sl 495 E-slice places) = 2,217,093,120 cosets,
  index `(co*2048+eo)*495+sl`, coordinates from `/data/fmc/is-dr-xs-worth-it/research/src/coords.py`, Rust model in
  `is-dr-xs-worth-it/research/xstools/src/cubie.rs` (Cubie, Model::coords, conj for rotations).
- Exact distance tables (u8 per coset, 2.2 GB each, `is-dr-xs-worth-it/research/out/bfs/`):
  `all_dr.u8` (any face turn → DR on U/D colour), `eo-fb_dr.u8` (moves that keep F/B EO, i.e. no F/B quarter turns →
  DR on U/D colour). Other DR colours and EO axes by conjugating with a rotation (check every mapping on samples
  against a direct BFS/brute force before trusting it). `attempt.rs` packs a table to 4 bits in RAM (1.1 GB): use
  that; never mmap several tables at once (the machine has 7.7 GB, no swap; one heavy job at a time, memory capped
  with `systemd-run --user --scope -p MemoryMax=…`).
- EO distance: 2048 states per axis, trivial BFS; with NISS: pre-moves.
- Sticker model `/data/fmc/is-dr-xs-worth-it/research/src/cube.py` for independent checks; every printed solution is
  replayed on it.
- nissy and cubelib-cli are installed (`source /data/fmc/env.sh`) for cross-checks.

## Definitions
- A *DR on axis X* = corners oriented and E-slice-for-X edges in their slice for the colour of X (centres as usual).
  Three axes. *Linear*: moves after the scramble only. *Inverse*: moves after the inverse scramble. *NISS*: moves
  on both sides, total length |A|+|B| where B·S·A is a DR (B on the inverse side, read in the usual NISS way). The
  NISS length of S = min over pre-move sequences B of |B| + d(B·S); exact by enumerating B up to the depth where it
  cannot beat the linear value.
- An *EO on axis Y* (F/B, R/L, U/D) = all edges good for Y. EO length: linear, inverse, NISS as above.
- *Through an EO*: route = EO sequence E on some side, then moves that keep that EO (no quarter turns of Y's faces)
  to a DR on one of the two axes ≠ Y: on the normal side for a normal EO, on the inverse side for an inverse EO, and
  for a NISS EO (turns on both sides) on the better of the two sides (as computed, `eodrtools/src/scr.rs`).
- *Last-move inversion*: the EO's last move is a quarter turn of Y; the alternative is the same EO with that move
  turned the other way (state · Y2).
- Case names: xCyE / DRM as on the server (bad corners, bad edges for the DR axis after EO; doc 6 conventions).

## Questions (each answer exact or a stated sample size; random-state scrambles, 20,000+ unless stated)
A. Scramble → DR as a whole
 1. Shortest DR length distribution: fixed axis (exact, known), best of 3 axes linear, best of 6 (3 × normal/inverse),
    and with NISS (S-DR-6, D20015–D20023: "is the distribution known", "sub-10 on most scrambles?", superflip and
    the worst case). Give odds of ≤8, ≤9, ≤10, the mean, and how many DR solutions of each length a scramble has.
 2. Optimal DR against the best DR through an EO: for k = 3, 4, 5, 6, the best DR reachable through an EO of ≤k
    (linear on one side; then with NISS EOs), against the optimal DR (S-DR-47, S-DR-46, S-DR-26). How often the
    optimal DR goes through some short EO; the average loss; how often an EO-breaking route is needed.
 3. Number of DRs: for each scramble, the number of (EO, DR axis) pairs with an EO of ≤k and a DR total ≤N, for
    k = 4, 5 and N = 9, 10, 11, 12 (S-DR-251; "25 4-move EOs or 200 5-move EOs"); the gain in the best DR from
    adding the 5-move EOs to the 4-move ones; from adding the other axes.
B. Scramble → EO
 4. Number of EOs of each length per scramble, one axis and all axes, linear / with inverse / NISS (S-EO-82,
    S-EO-85/86 how rare 3-move EOs are, S-EO-87 N-move but no N+1, S-EO-91 fewest ≤5-move EOs, S-EO-174 max per axis).
 5. Bad-edge layouts: exact probabilities of each (count on the three axes) triple (S-EO-37, S-EO-17), and the
    chance of a ≤k-move EO by bad-edge count (S-EO-136/137/140). Exact over 12!·2^11 edge states where possible
    (an EO depends only on the edge state: count over 2048 orientations × slice positions).
C. EO → DR
 6. The exact per-case table exists (credit). New: the same with (a) the better of the two DR axes of one EO
    (EO-DR-334, T3226–T3329 "dropped as infeasible"), (b) the better of normal and inverse (EO-DR-336; correlation
    between normal and inverse, EO-DR-113, Jay vs Tom Nelson), (c) last-move inversion (EO-DR-73–77: "DR-4e4c in 6
    is 1 in 5.2, or 1 in 3.6 if you can switch the last move"; Lichi Fang's 3 of 27; Cale's re-test), (d) any moves
    against EO-preserving moves (credit torchlight), each by case (DRM) and overall. Exact where the state space
    allows (a, d exact over cosets; b, c by sampling EO'd states uniformly with exact table lookups).
 7. "Typical EO→DR" (Zagros D12300, EO-DR-102/109/110): one table that says what a solver gets after an EO with
    each of the options above.
D. Claims: every disputed or checkable claim in the register's "Disputed claims" table and B-kind entries on these
   themes that the computations above can settle, with an example scramble for every correction.

## Checks
- Table lookups against a direct search (nissy or own IDA*) on 1,000 random positions per table and per mapping.
- The fixed-axis distributions must reproduce the known ones (all_dr: 1, 4, 50, 592, …, 476; EO→DR: Cale's 1,082,565
  states with mean 7.80; EO fixed axis mean 4.609; best NISS EO mean 3.455).
- Every DR or EO solution printed anywhere is replayed on the sticker model.

## Output layout
`research/src` (Python), `research/eodrtools` (Rust, one crate; reuse xstools sources by `#[path]` like xstools did
with drtools), `research/out` (small outputs committed; big ones git-ignored), `lean/` later (small exact tables:
bad-edge layout counts, EO distance distribution), `report/` later.
