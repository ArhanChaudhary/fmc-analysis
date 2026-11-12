# Judging a DR by hand

What a solver can read off a domino reduction (DR) before solving it, how much each read says about the
finish, and which lower bounds hold. Everything is measured on the exact optimal finish of all
19,508,428,800 DR states.

| | |
|---|---|
| [`report/WRITEUP.md`](report/WRITEUP.md) | Judging a DR by hand: what the full BFS says. Start with its section 1, the short version. |
| [`report/EXAMPLES.md`](report/EXAMPLES.md) | Eleven DRs read step by step, with the exact odds after each read and the real optimal. Then 100 random-state scrambles with the DRs you could have on the page: reads, what the prune list says, and the answers folded away. |
| [`report/BUGS.md`](report/BUGS.md) | Errata: what the full search shows is wrong in the docs and sheets involved and in things said on the server. |

## What is in this folder

| Path | What |
|---|---|
| `report/` | The three reports and the tables they include (`data/`). |
| `lean/DRBound/` | Lean 4 proof (no Mathlib): the optimal finish of every DR state, the lower bounds, the 216 half-turn-only values. See its `README.md`. |
| `research/drtools/` | Rust: the search over the DR group, the bound tables, and the passes that count each hand-readable quantity against the optimal. |
| `research/src/` | Python analysis of those counts. `pv.py` gives the share finishing in any number of moves for any combination of reads, `hand_pivots.py` and `report_tables.py` write the tables in `report/data/`, and `report_build/` assembles `report/WRITEUP.md` from its parts (every number in the per-subset guide is computed at build time). |
| `research/tool/` | `drread`: the reads and odds for any DR. `drbound`: the computed lower bounds for any DR. |
| `research/out/` | Result tables (CSV and text), including `out/hand/` (one histogram per read) and `out/witnesses.txt` (an explicit state for every existence claim in the reports). |

Not included: the large generated tables (`research/data/`, about 6 GB): one bit per reduced state and
depth for the exact search, and the bound tables. The commands below rebuild them in a few minutes.

## Reproducing

The code was written on one Linux machine and still assumes its layout: the repository at `/data/fmc`,
with the generated tables under `/data/fmc/judging-a-dr/research/data`. Rust (stable), Lean 4.35.0 via
elan, Python 3 with numpy, and nissy for the cross-checks.

    cd research/drtools && cargo build --release
    ./target/release/drtools bfs ../data/drbfs                 # exact optimal of every DR state
    ./target/release/drtools ladder ../data/drbfs ../data/tables > ../out/lattice.csv
    ./target/release/drtools lsbfs ../data/ls_depth.u8         # optimal leave slice
    ./target/release/drtools hcensus ../data/drbfs ../data/ls_depth.u8 ../out/hand
    ./target/release/drtools hcensus2 ../data/drbfs ../out/hand
    ./target/release/drtools hcensus3 ../data/drbfs ../out/hand                  # pairs, corner cases and HTR lengths together
    ./target/release/drtools ncensus ../data/drbfs ../out/hand
    ./target/release/drtools witness ../data/drbfs ../data/ls_depth.u8 LISTING > ../out/witnesses.txt
    cd ../../lean/DRBound && lake build DRBound.CertifiedExactTable && lake build   # the proof, about half an hour

The reports are then rebuilt from the counts:

    cd ../src && python3 hand_pivots.py && python3 report_tables.py && python3 witness_tables.py
    python3 report_build/corner_section.py && python3 report_build/assemble.py   # writes report/WRITEUP.md
    python3 many_examples.py                                                      # the 100 scrambles in report/EXAMPLES.md (needs cubelib-cli)
    cd ../../.. && scripts/build-pages.sh OUTPUT_DIRECTORY                         # the site

Each pass needs under 3 GB of memory. `LISTING` is FakeMMAP's list of the 216 NISS@1qt cases with a
half-turn scramble each (an attachment on FakeMMAP's Discord post, linked from the write-up).
