# fmc-analysis

Rubik's cube FMC (fewest moves) theory, checked against every state.

The first study is about judging a domino reduction (DR) before you solve it: what a solver can read off a
DR by hand, how much each read says about the finish, and which lower bounds hold. Everything is measured
on the exact optimal finish of all 19,508,428,800 DR states.

**Read it at [fmc.arhan.sh](https://fmc.arhan.sh).**

| | |
|---|---|
| [`report/WRITEUP.md`](report/WRITEUP.md) | Judging a DR by hand: what the full BFS says. Start with its "Start here" block. |
| [`report/EXAMPLES.md`](report/EXAMPLES.md) | Eleven DRs read step by step, with the exact odds after each read and the real optimal. |
| [`report/BUGS.md`](report/BUGS.md) | Errata for the docs and sheets involved, and claims from the server that the full search settles. |

## What is in the repository

| Path | What |
|---|---|
| `report/` | The three reports and the tables they include (`data/`). |
| `lean/DRBound/` | Lean 4 proof (no Mathlib): the optimal finish of every DR state, the lower bounds, the 216 half-turn-only values. See its `README.md`. |
| `research/drtools/` | Rust: the search over the DR group, the bound tables, and the passes that count each hand-readable quantity against the optimal. |
| `research/src/` | Python analysis of those counts. `report_build/` assembles `report/WRITEUP.md` from its parts. |
| `research/tool/` | `drread`: the reads and odds for any DR. `drbound`: the computed lower bounds for any DR. |
| `research/out/` | Result tables (CSV and text), including `out/hand/` (one histogram per read) and `out/witnesses.txt` (an explicit state for every existence claim in the reports). |
| `scripts/build-pages.sh`, `site/` | The website: the three reports as pages with a table of contents each. Needs pandoc. |

## What is not here

- The Discord export the reports quote from, and the knowledge base built from it. They are other people's
  messages and documents. The reports link to each message they cite.
- The large generated tables (`research/data/`, about 6 GB): one bit per reduced state and depth for the
  exact search, and the bound tables. `drtools bfs`, `drtools ladder` and `drtools lsbfs` rebuild them in
  a few minutes.

## Reproducing

The code was written on one Linux machine and still assumes its layout: this repository at `/data/fmc`,
with the generated tables under `/data/fmc/research/data`. Rust (stable), Lean 4.35.0 via elan, Python 3
with numpy, and nissy for the cross-checks.

    cd research/drtools && cargo build --release
    ./target/release/drtools bfs ../data/drbfs                 # exact optimal of every DR state
    ./target/release/drtools ladder ../data/drbfs ../data/tables > ../out/lattice.csv
    ./target/release/drtools lsbfs ../data/ls_depth.u8         # optimal leave slice
    ./target/release/drtools hcensus ../data/drbfs ../data/ls_depth.u8 ../out/hand
    ./target/release/drtools hcensus2 ../data/drbfs ../out/hand
    ./target/release/drtools ncensus ../data/drbfs ../out/hand
    cd ../../lean/DRBound && lake build DRBound.CertifiedExactTable && lake build   # the proof, about half an hour

Each pass needs under 3 GB of memory.

## The website

    scripts/build-pages.sh /tmp/fmc-site      # needs pandoc

`.github/workflows/pages.yml` runs the same script on every push to `main` and deploys the result to
GitHub Pages.
