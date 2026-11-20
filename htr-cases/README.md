# HTR cases

An interactive index of every HTR case of a DR, live at <https://fmc.arhan.sh/htr-cases/>:

- 1,272 cases, up to rotations, mirrors and the E slice;
- grouped by subset, then bad edges, then the optimal (the fewest moves to HTR; "6-optimal" on the page);
- each drawn in 3D with only its bad pieces solid, and with its HTRs up to 0 to 4 moves over its optimal (a slider, 2
  by default).

Alongside it, [`web/htr-cases.txt`](web/htr-cases.txt) has a shortest generator of every case, for other programs.

## What a case is

A DR on U/D goes to HTR with the DR moves U, D, R2, L2, F2, B2. Two DR states take exactly the same sequences to HTR
when they differ by an element of the half-turn group H = `<U2, D2, R2, L2, F2, B2>` renaming their pieces. So the
case of a state g is its coset H·g.

There are 29,400 cosets: 420 corner cosets times 70 patterns of M-slice edges on U/D-layer places. Three things count
as the same case:

- **Rotations and mirrors** that keep the U/D axis: the 16 symmetries, acting by conjugation.
- **The E slice.** Renaming every piece by U D' (which normalises H) turns every bad piece good and every good one bad,
  so 2c3 2e becomes 6c3 6e. In the frame with few bad pieces, where subsets are named, the bad pieces are the same.
  Up to a y rotation, this is the same as turning the E slice. Each case is drawn the way with fewer bad pieces: 2c
  rather than 6c, 0c rather than 8c (with 4 bad corners either way, the fewer bad edges). Case 1 is the exception,
  drawn with every piece bad: HTR with the E slice turned, 2 moves from HTR, whose twin is HTR itself.

What the tests check about the E slice (`cases/tests/checks.rs`):
- the two versions are the same number of moves from HTR, for every case except HTR itself, which a turned E slice
  puts 2 moves away (case 1);
- their HTRs are the same, with the last quarter turn moved to the other layer (all 405,992 of them, before the
  dedupe below).

That leaves 1,272 cases. Every one shares its bad pieces with 3 to 5 other cases, its *lookalikes*, which the page
lists. The CLI also gives a *corner test*: a shortest sequence that puts its corners in HTR, which leaves any lookalike
in fake HTR. Lookalikes in the same subset also get the label the guides use (`cases/src/labels.rs`):

- **4b2 parity.** Set the corners up for a Q X2 Q trigger with half turns, counting every U2 or D2 done while the bad
  corners split 3/1 between U and D. An even count gives real HTR (no parity); an odd count, parity.
- **2c3 direction.** From the position shown, the quarter turn that brings it to 4b2 with no parity goes either
  clockwise or anticlockwise. U and D are each seen from their own face, and every half turn before it flips the
  direction.
- **2c4 and 4a3, good or bad.** A sequence *progresses* when it brings the corners a quarter turn closer to HTR, half
  turns counting nothing (`labels::quarter_turns`; this is the number in the subset's name, for every subset). A 2c4
  is good when, with its bad corners on UFR and UFL, U and B2 U both progress; on UBL and DFR, F2 U and R2 U; stacked
  on UFR and DFR, U2 R2 U and U2 F2 U. A 4a3 is good when, with its bad corners as bars on U and D, U progresses; all
  on U, F2 U. Otherwise bad; a 4a3 with its bad corners on diagonals is neither. U or U' makes no difference (they are
  a free U2 apart).

The first two rules come from the *Hitchhiker's Guide to HTR* (Yurii Riabov, 2024) and the server. Computed over every
half-turn route, each gives a single answer on every corner coset. The guide's own examples come out as it says. The
70 pairs of 4b2 lookalikes are each one with parity and one without. Good and bad give one answer from every side
that puts the bad corners where a rule wants them (a 2c4 with 6 bad corners is read from its 2, as the index draws
it), and the same answer on both versions of a case. What they come to: on a good 2c4 both sequences lead to 2c3, and
on a bad one, one leads to 2c3 and the other to 2c5. A good 4a3's turn leads to 4b2 and a bad one's to 4b4. Over the
cases: 96 good and 160 bad 2c4, 50 good, 50 bad and 15 neither 4a3.

The HTRs listed are canonical DR-move sequences:
- turns of opposite faces go in the order U D, R L, F B;
- none is in HTR before its end, or in HTR with the E slice turned (the rest would only turn the slice back);
- none has a half turn among its last turns.

So each ends in a single quarter turn that can go either way, and only the clockwise one is written. Then one is kept
of each set that is the same up to the E slice, the shortest (`cosets::modulo_e`): ignoring the E slice, D is U with
the cube turned a quarter, so every D turn is written as a U turn and the faces after it are moved round (R to F, F to
L, L to B, B to R). Case 310's `U R2 U R2 U`, `U R2 D B2 D`, `D B2 U B2 D` and `D B2 D L2 U` are one HTR. Of the HTRs
of 8 moves or less (or the optimal ones, for the 782 cases with none that short), that keeps 27,888 of about 406,000.
Case 1, HTR up to the E slice, lists only `U D`.

How long the lists go is a slider in the case's panel: 0 to 4 moves over its optimal, 2 by default (418,657 HTRs over
all the cases), but never past 12 moves; a case whose optimal is longer lists its optimal ones (`Index::longest`). At
optimal + 4, a 10-optimal case would have about 5.8 million HTRs before the dedupe. With the bound, the most any case
lists is about 375,000 before the dedupe (18,472 after), a quarter of a second in the browser.

**Pairs a U2 apart.** 192 pairs of cases are one case after U2 (or D2), with a shortest HTR on both that starts with a
quarter turn of that layer: U on one is U′ on the other, so after it they are the same case (`classes::u2_mates`; 310
and 311 are one pair). Both cases of a pair always have the same subset, edges and length. The page names each case's
pair, and a switch shows each pair as one entry (1,080 entries).

**The page.** The list of cases on the left; a click opens a case in the panel on its right (over the list, on a
phone, where "Show in list" goes back), and nothing in the list moves: the card is only marked. The panel's title bar
has the case, its subset, its optimal and its label; under the cube are its lookalikes, its pair a U2 apart, the
slider for how far over the optimal and its HTRs. Over the list, a second slider shows only the cases with optimal
that or less. *Find your case* takes one text: the scramble on the first line and the moves to DR after it, or just a
setup (`find::split_attempt`).

## Layout

| Where | What |
|---|---|
| `cases/` | the library (crate `htr-cases`): `cosets.rs` (the cosets, moves, symmetries, E slice, the HTR search), `classes.rs` (the cases, how each is drawn, lookalikes), `labels.rs` (4b2 parity, 2c3 direction, 2c4 and 4a3 good or bad), `find.rs` (a solver's own DR from a scramble and NISS moves), `lib.rs` (`Index`, what the page and the text file show) |
| `cases/tests/checks.rs` | the checks (below) |
| `cli/` | `htr-cases text FILE`, `list`, `case N [--turned] [--above K]`, `find SCRAMBLE MOVES [--above K]` |
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

- 1,272 cases cover the 29,400 cosets.
- Every coset of a case is as far from HTR as the others, except HTR itself.
- Every generator makes its case, as drawn, in as many moves as the case's distance.
- Every HTR of 8 moves or less (or the optimal ones) of every case and of its E-turned version, before the dedupe
  (811,985), reaches HTR at its end and not
  before, not even with the E slice turned. The shortest has the case's length.
- The dedupe keeps one HTR of each set with the same form up to the E slice. The members of a set end with the same
  corners and U/D-layer edges up to U D' (checked on the DR model), and case 310's four 5-movers are one set.
- The lists are complete: a brute-force search over every DR-move sequence from the cube finds exactly the listed ones,
  up to 7 moves on 23 cases, 8 moves on 3, and case 1.
- The guide's setups have the subsets the guide gives them, and its 4b2 and 2c3 examples have the parity and the
  direction it says.
- NISS moves in brackets count on the inverse; the page's one field reads a scramble with moves, or a setup.
- 2c4 and 4a3: every case has its label but the 4a3s on diagonals, the same on both versions of a case.
- The panel's slider: up to 4 over the optimal, not past 12 moves unless the optimal is; case 1 lists only `U D`.
- What the page says about the E slice (counted above).
