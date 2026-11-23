# HTR cases

An interactive index of every HTR case of a DR, live at <https://fmc.arhan.sh/htr-cases/>:

- 1,446 cases: 1,272 up to rotations, mirrors and the E slice, with every version a picture can hide listed apart;
- grouped by subset, then bad edges, then the optimal (the fewest face turns to HTR, leaving DR on the way or not;
  "6-optimal" on the page);
- each drawn in 3D with only its bad pieces solid, and with its HTRs, DR-breaking ones included, up to 0 to 4 moves
  over its optimal (a slider, 2 by default).

Alongside it, [`web/htr-cases.txt`](web/htr-cases.txt) has a shortest generator of every case, for other programs.

## What a case is

A DR on U/D goes to HTR with the DR moves U, D, R2, L2, F2, B2, or with any face turns, leaving DR on the way. Two
DR states take exactly the same sequences to HTR when they differ by an element of the half-turn group
H = `<U2, D2, R2, L2, F2, B2>` renaming their pieces. So the case of a state g is its coset H·g.

There are 29,400 cosets: 420 corner cosets times 70 patterns of M-slice edges on U/D-layer places. Three things count
as the same case:

- **Rotations and mirrors** that keep the U/D axis: the 16 symmetries, acting by conjugation.
- **The E slice.** Renaming every piece by U D' (which normalises H) turns every bad piece good and every good one bad,
  so 2c3 2e becomes 6c3 6e. In the frame with few bad pieces, where subsets are named, the bad pieces are the same.
  Up to a y rotation, this is the same as turning the E slice. Each case is drawn the way with fewer bad pieces: 2c
  rather than 6c, 0c rather than 8c (with 4 bad corners either way, the fewer bad edges). Case 1 is the exception,
  drawn with every piece bad: HTR with the E slice turned, 2 moves from HTR, whose twin is HTR itself.

What the tests check about the E slice (`cases/tests/checks.rs`):
- with DR moves, the two versions are the same number of moves from HTR, for every case except HTR itself, which a
  turned E slice puts 2 moves away (case 1); and their HTRs are the same, with the last quarter turn moved to the other
  layer (all 405,992 of them, before the dedupe below);
- with every face turn, they are not always: for 25 more classes the two versions' optima differ, by one move (two for
  cases 741 and 807). Mostly 2c4 cases whose 2c version has a DR-breaking shortcut the 6c one lacks (741: 7 moves
  drawn, 9 with the slice turned); for three 0c3 and two 4b5 cases the other way round. The page shows the version
  drawn.

That leaves 1,272 classes.

**The list.** Some pictures are kept by a turn or a mirror of the cube (or, for 4 bad corners and 4 bad edges, by the
E slice) while the class is not: one picture then hides two or four cosets that take different HTRs. 2c3 cases 323
and 324 are one class, mirror images of each other with the same bad pieces, one clockwise and one anticlockwise.
So the page lists every coset with its class's picture (`classes::entries`): 1,446 cases, 174 more than the
classes, in 0c3, 0c4, 2c3, 2c4, 4a3, 4a4 and 4b5. A DR turned to look like a picture is then always one of the cases
shown with it, and its HTRs are listed as written. The lookalikes of a case say which are the same class turned, in a
mirror or with the E slice turned. In 0c3, 2c3 and 2c4 the labels tell them apart (R or F, the direction, the swap
type); in 0c4, 4a3, 4a4 and 4b5 (192 cases) no label does yet.

Every case shares its bad pieces with other cases, its *lookalikes*, which the page lists. The CLI also gives a *corner test*: a shortest sequence that puts its corners in HTR, which leaves any lookalike
in fake HTR. Lookalikes in the same subset also get the label the guides use (`cases/src/labels.rs`):

- **4b2 parity.** Set the corners up for a Q X2 Q trigger with half turns, counting every U2 or D2 done while the bad
  corners split 3/1 between U and D. An even count gives real HTR (no parity); an odd count, parity.
- **2c3 direction.** From the position shown, the quarter turn that brings it to 4b2 with no parity goes either
  clockwise or anticlockwise. U and D are each seen from their own face, and every half turn before it flips the
  direction.
- **0c3 type: U, R or F.** The axis whose quarter turn brings the corners to 4a2 (the other two bring them to 4a4),
  each read with that axis as the DR axis (`cube::DR_VIEW`). A 0c3's corners are twisted right on every axis, and the
  three types are its three corner cosets. R and F are read on the case as drawn: a y rotation swaps them, but turns
  the bad edges with them, so with the edges the letter tells cases apart (cases 292 and 293, both 0c3 4e with the same bad edges, are R and F; 25 pairs of
  lookalikes differ only so).
- **2c4 swap type and good, mid or bad.** Swapping the two bad corners makes a 0c3; the swap type (Swap-U, Swap-R,
  Swap-F) is its type. With the bad corners in opposite layers, good if U brings it to 4b3 (D does the same), bad if
  to 4b5; with both on U (at UFR and UFL), good if U and B2 U both bring it to 2c3, mid if only U does, bad if only
  B2 U does.
- **4a3, good or bad.** A sequence *progresses* when it brings the corners a quarter turn closer to HTR, half turns
  counting nothing (`labels::quarter_turns`; this is the number in the subset's name, for every subset). A 4a3 is good
  when, with its bad corners as bars on U and D, U progresses; all on U, F2 U. Otherwise bad; with its bad corners on
  diagonals, neither. U or U' makes no difference (they are a free U2 apart).

The first two rules come from the *Hitchhiker's Guide to HTR* (Yurii Riabov, 2024) and the server. Computed over every
half-turn route, each gives a single answer on every corner coset. The guide's own examples come out as it says. The
70 pairs of 4b2 lookalikes are each one with parity and one without. The 0c3, 2c4 and 4a3 rules give one answer from
every side that puts the bad corners where a rule wants them (a 2c4 with 6 bad corners, or a 0c3 with 8, is read from
its version with few, as the index draws it), and the same answer on both versions of a case. A good 4a3's turn leads
to 4b2 and a bad one's to 4b4. Over the listed cases: 0c3, 13 each of U, R and F; 2c4, Swap-U 54 good and 42 bad,
Swap-R 11 good, 31 mid and 54 bad, Swap-F 31 good, 11 mid and 54 bad (mid never with Swap-U); 4a3, 50 good, 50 bad and
24 neither.
*Find your case* gives U, R and F on the solver's own axes.

The HTRs listed are canonical sequences of face turns: the DR moves, and quarter turns of R, L, F and B, which leave
DR on the way (`cases/src/allmoves.rs`):
- turns of opposite faces go in the order U D, R L, F B;
- none is in HTR before its end, or in HTR with the E slice turned (the rest would only turn the slice back);
- none has a half turn among its last turns.

So each ends in a quarter turn that can go either way (X and X′ both reach HTR), and only the clockwise one is written.
Then one is kept of each set that is the same up to the E slice, the shortest (`allmoves::modulo_e`): ignoring the E
slice, D is U with the cube turned a quarter, so every D turn is written as a U turn and the faces after it are moved
round (R to F, F to L, L to B, B to R). Case 323's `U R2 U R2 U`, `U R2 D B2 D`, `D B2 U B2 D` and `D B2 D L2 U` are one
HTR. Case 1, HTR up to the E slice, lists only `U D`.

**Breaking DR.** The optimal counts every face turn: for 155 classes (201 listed cases) an HTR that leaves DR on the way is shorter than any
with DR moves. Case 742 (2c4 2e, bad) is 8 moves from HTR with DR moves and 7 with `F U B' U2 F U' B`; case 1017 (4a4
0e), 13 with DR moves, is 10. The search for them runs on the whole cube, pruned by exact distances of projections:
the corners up to H (twists times corner coset, 918,540) and, for each slice, the edges' flips with the places of
that slice's edges (2048 times 495). Within 5 face turns of HTR it knows the moves left exactly (155,000 cosets of H,
by breadth-first search), and back in DR it uses the exact distance of every DR coset to HTR, computed once
(`AllMoves::dr_distances`, kept in `cases/src/all_dist.bin`, written by `htr-cases all-dist`).

How long the lists go is a slider in the case's panel: 0 to 4 moves over its optimal, 2 by default (382,048 HTRs over
all the cases, 178,110 of them leaving DR), but never past 11 moves; a case whose optimal is longer lists its optimal
ones (`Index::longest`). With every face turn, a 7-optimal case has about 100,000 HTRs of 11 moves before the dedupe,
about a second's search; at 12 moves some cases take ten.

**Pairs a U2 apart.** Cases that are one case after U2 (or D2), seen from some side, with a shortest HTR on both that
starts with a quarter turn of that layer: U on one is U′ on the other, so after it they are the same case
(`classes::u2_mates`; 323 and 325 are a pair). 197 pairs and 18 groups of four (a case after U2 can look like two
cases with one picture); the cases of a group always have the same subset, edges and optimal. The page names each
case's others, and a switch shows each group as one entry (1,195 entries).

**The page.** The list of cases on the left; a click opens a case in the panel on its right (over the list, on a
phone, where "Show in list" goes back), and nothing in the list moves: the card is only marked. The panel's title bar
has the case, its subset, its optimal and its label; under the cube are its lookalikes, its pair a U2 apart, the
slider for how far over the optimal and its HTRs. Over the list, a second slider shows only the cases with optimal
that or less. *Find your case* takes one text: the scramble on the first line and the moves to DR after it, or just a
setup (`find::split_attempt`).

## Layout

| Where | What |
|---|---|
| `cases/` | the library (crate `htr-cases`): `cosets.rs` (the cosets, moves, symmetries, E slice, the HTR search), `classes.rs` (the cases, how each is drawn, lookalikes), `labels.rs` (4b2 parity, 2c3 direction, 0c3 type, 2c4 swap type and good, mid or bad, 4a3 good or bad), `allmoves.rs` (the HTRs with every face turn; `all_dist.bin`, the distance of every DR coset), `find.rs` (a solver's own DR from a scramble and NISS moves), `lib.rs` (`Index`, what the page and the text file show) |
| `cases/tests/checks.rs` | the checks (below) |
| `cli/` | `htr-cases text FILE`, `list`, `case N [--turned] [--above K]`, `find SCRAMBLE MOVES [--above K]`, `all-dist FILE` |
| `wasm/` | the WebAssembly API the page uses (wasm-bindgen) |
| `web/` | the page: `index.html`, `app.js`, `cube.js` (the 3D drawing, canvas 2D), `worker.js`, `cases.css`, `pkg/` (the built module, committed), `htr-cases.txt` (generated) |
| `build-web.sh` | rebuilds `web/pkg/` and `web/htr-cases.txt` |

The DR group, the HTR cosets and the whole-cube model come from the attempt simulator's library
(`../attempt-sim/tool/sim`: `dr.rs`, `htr.rs`, `cube.rs`).

## Build and run

    cargo build --release -p htr-cases-cli
    target/release/htr-cases case 142                    # one case and its HTRs, as JSON
    target/release/htr-cases find "R U2 R' U2 L2 F2" ""  # the case of a DR (any axis; NISS moves in brackets)
    cargo test --release -p htr-cases                    # the checks
    ./build-web.sh                                       # the page's module and the text file

`build-web.sh` needs the `wasm32-unknown-unknown` target and `wasm-bindgen-cli` 0.2.130. `scripts/build-pages.sh`
copies `web/` to `/htr-cases/` on the site.

## Checks

`cargo test --release -p htr-cases` replays everything on the whole-cube model of `cube.rs`, which is built from the
geometry of the turns and doesn't use the coset tables:

- 1,272 classes cover the 29,400 cosets; listed as 1,446 cases.
- The list is exhaustive: every DR coset, turned, mirrored or with the E slice turned, is a listed case; and every
  coset with a listed case's bad corners and edges in the same places and its subset is listed itself. The 1,400 such
  lookalike pairs each take different HTRs, checked on the cube (some optimal HTR of one does not solve the other).
  With one case per class, as before, the check fails (a coset looks like case 648 and is not listed).
- With DR moves, every coset of a case is as far from HTR as the others, except HTR itself; with every face turn, the
  symmetric copies are, and the two versions differ for 25 cases (23 by one move, 2 by two). Never further than with
  DR moves; shorter for 155 classes.
- `all_dist.bin` is what the search finds now (computed again, 15 seconds).
- The case of `U' L2 U' F2 U L2 U' L2` is 8 moves from HTR with DR moves and 7 with `F U B' U2 F U' B`.
- Every generator makes its case, as drawn, in as many moves as the case's optimal.
- Every HTR of 8 moves or less (or the optimal ones) of every case and of its E-turned version, before the dedupe
  (537,837, of them 35,748 leaving DR), reaches HTR at its end and not before, not even with the E slice turned. The
  shortest has the case's optimal.
- The dedupe keeps one HTR of each set with the same form up to the E slice. With DR moves, the members of a set end
  with the same corners and U/D-layer edges up to U D' (checked on the DR model); the form with every face turn is
  the DR-move one on DR moves; the four 5-movers of `U' R2 U' R2 U'` are one set.
- The lists are complete: a brute-force search over every sequence of face turns from the cube finds exactly the
  listed ones, up to 6 moves on 23 cases and 7 on 2 (one with a DR-breaking 7-mover); over every DR-move sequence, the
  DR-move ones up to 7 moves on 23 cases, 8 on 3, and case 1.
- The guide's setups have the subsets the guide gives them, and its 4b2 and 2c3 examples have the parity and the
  direction it says.
- NISS moves in brackets count on the inverse; the page's one field reads a scramble with moves, or a setup.
- 0c3, 2c4 and 4a3: every case has its labels but the 4a3s on diagonals, the same on both versions of a case; U and
  Swap-U the same from every side, R and F swapping with a y rotation (which turns the edges too); a 0c3 found on R/L has its letter on R/L's axes.
- The panel's slider: up to 4 over the optimal, not past 11 moves unless the optimal is; case 1 lists only `U D`.
- Cases a U2 apart: 197 pairs and 18 groups of four, each with the same subset, edges and optimal.
- What the page says about the E slice (counted above).
