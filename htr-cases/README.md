# HTR cases

An interactive index of every HTR case of a DR, live at <https://fmc.arhan.sh/htr-cases/>:

- 1,272 cases, up to rotations, mirrors and the E slice;
- grouped by subset, then bad edges, then the fewest moves to HTR;
- each drawn in 3D with only its bad pieces solid, and with every HTR of 8 moves or less (or the shortest ones, when
  none is that short).

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
  Up to a y rotation, this is the same as turning the E slice.

What the tests check about the E slice (`cases/tests/checks.rs`):
- the two versions are the same number of moves from HTR, for every case except HTR itself, which a turned E slice
  puts 2 moves away (case 1);
- their shortest HTRs are the same, with the last quarter turn moved to the other layer;
- so are 405,992 of the 414,848 HTRs listed.

That leaves 1,272 cases. Every one shares its bad pieces with 3 to 5 other cases. Every case lists its *lookalikes* and
has a *corner test*: a shortest sequence that puts its corners in HTR. The same sequence leaves any lookalike in fake
HTR. Lookalikes in the same subset also get the label the guides use (`cases/src/labels.rs`):

- **4b2 parity.** Set the corners up for a Q X2 Q trigger with half turns, counting every U2 or D2 done while the bad
  corners split 3/1 between U and D. An even count gives real HTR (no parity); an odd count, parity.
- **2c3 direction.** From the position shown, the quarter turn that brings it to 4b2 with no parity goes either
  clockwise or anticlockwise. U and D are each seen from their own face, and every half turn before it flips the
  direction.

Both rules come from the *Hitchhiker's Guide to HTR* (Yurii Riabov, 2024) and the server. Computed over every half-turn
route, each gives a single answer on every corner coset. The guide's own examples come out as it says. The 70 pairs of
4b2 lookalikes are each one with parity and one without.

The HTRs listed are canonical DR-move sequences:
- turns of opposite faces go in the order U D, R L, F B;
- none is in HTR before its end;
- none has a half turn among its last turns.

So each ends in a quarter turn that can go either way, and only the clockwise one is written. 782 cases have no HTR of
8 moves or less (most need 9 to 11; two need 13), and for those the page lists the shortest ones.

## Layout

| Where | What |
|---|---|
| `cases/` | the library (crate `htr-cases`): `cosets.rs` (the cosets, moves, symmetries, E slice, the HTR search), `classes.rs` (the cases, how each is drawn, lookalikes), `labels.rs` (4b2 parity, 2c3 direction), `find.rs` (a solver's own DR from a scramble and NISS moves), `lib.rs` (`Index`, what the page and the text file show) |
| `cases/tests/checks.rs` | the checks (below) |
| `cli/` | `htr-cases text FILE`, `list`, `case N [--turned]`, `find SCRAMBLE MOVES` |
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
- Every listed HTR of every case and of its E-turned version (more than 800,000) reaches HTR at its end and not before.
  The shortest has the case's length.
- The lists are complete: a brute-force search over every DR-move sequence from the cube finds exactly the listed ones,
  up to 7 moves on 24 cases and 8 moves on 3.
- The guide's setups have the subsets the guide gives them, and its 4b2 and 2c3 examples have the parity and the
  direction it says.
- NISS moves in brackets count on the inverse.
- What the page says about the E slice (counted above).
