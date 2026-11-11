# Is DR-xs worth it?

The second case study of this repository: what the "DR minus slices" techniques (DR-xs, also called DR-fe; slice EO; DR-1s, DR-2s 8fe) cost and how often they are there, computed exactly where the state space allows it, with every concrete claim from the FMC solvers Discord checked against the numbers.

It builds on tseitsei89's DR-Xs tutorial and trangium's statistics in it. What it adds: odds instead of averages, the exact move counts between DR-3s, DR-2s, DR-1s and DR, how often a slice EO is there and what it leads to, the same 500 scrambles as the first study with every DR-1s and DR-2s 8fe on them, and the claims check.

| Where | What |
|---|---|
| [report/WRITEUP.md](report/WRITEUP.md) | the write-up |
| [report/EXAMPLES.md](report/EXAMPLES.md) | worked examples |
| [report/BUGS.md](report/BUGS.md) | corrections to documents and claims |
| `research/src/` | the Python side: sticker model, kinds of DR-xs, coordinates, exact counts, report tables |
| `research/xstools/` | the Rust side: searches over the 2,217,093,120 cosets of the DR group, finishing DR-1s and DR-2s 8fe states with the first study's exact DR table, real scrambles |
| `lean/DRXs/` | Lean certificate of the small exact tables |

## How the numbers are made

Everything starts from one sticker-level model of the cube built from geometry (`research/src/cube.py`); no permutation is typed by hand anywhere, the Rust tools read tables exported from it.

| Step | Script | Output |
|---|---|---|
| Kinds of DR-xs state, slices and turns to DR | `fe.py`, `fecosets.py`, `festeps.py` | `out/fecosets.pkl`, `out/kinds.tsv` |
| Coordinates and move tables for Rust | `coords.py`, `export_kinds.py`, `export_cubie.py` | `out/tables/`, `out/targets/` |
| Slice-EO skip odds, turns to a slice EO | `seo_skip.py`, `seo_dist.py` | `out/seo_skip.txt` |
| From an edge-orientation pattern to a kind | `patterns.py` | printed table |
| Searches over all cosets, per move rule and target | `run_bfs.sh` (`xstools bfs`) | `out/bfs/*.u8` (2.2 GB each), `*.hist` |
| From a slice-EO skip to the nearest DR-1s / 8fe / DR | `seo_hist.py` | `out/seo_hist.json` |
| Finish of random DR-1s and DR-2s 8fe states | `xstools sample1s`, `sample8fe` | `out/sample1s.tsv`, `out/sample1s_labels.tsv`, `out/sample8fe.tsv` |
| Shortest DR / DR-1s / 8fe / any DR-xs of random scrambles | `xstools nearest` | `out/nearest.tsv` |
| Every DR-1s and DR-2s 8fe on 500 scrambles, with solutions | `xstools attempts`, `verify_attempts.py` | `out/attempts.tsv` |
| The server's worked examples against the classification | `check_examples.py` | printed |
| Example scrambles for the claims | `witness.py` | `out/witness.json` |
| The normal route by EO length on the 500 scrambles | `xeo.py` | `out/eo_run.tsv` |
| Report tables, write-up, errata, examples page | `xtables.py`, `xreal.py`, `report_build/assemble.py` (and `--bugs`), `xexamples.py` | `report/` |

Checks built in: the sticker model solves 100 scramble-and-solution pairs of the first study; the full search to a real DR reproduces the known distribution of DR lengths (1, 4, 50, 592, …, 476); the search to "any DR-xs on one axis" reproduces the distribution trangium posted (1, 4, 50, 586, 6800, …, 84); the Rust finisher agrees with a sticker-level brute force (`check_finish.py`); every solution written by `xstools attempts` is replayed on the scramble by `verify_attempts.py`.

The exact DR table (`judging-a-dr/research/data/lean_exact_table.u8`) and the 500 scrambles (`judging-a-dr/research/out/hand/attempt_scrambles.txt`) come from the first study. `xstools` uses that study's `drtools` sources for the DR group and the table index.

Large outputs (`research/out/bfs/`, build directories) are not in the repository; the scripts above regenerate them (about an hour for the searches on four cores, 55 GB of disk).

## Rebuilding the report

    source /data/fmc/env.sh
    cd is-dr-xs-worth-it/research/src
    python xtables.py && python xreal.py          # report/data/*.md
    python report_build/assemble.py --final       # report/WRITEUP.md (every number is computed; --final fails if one is missing)
    python report_build/assemble.py --bugs        # report/BUGS.md
    python xexamples.py                           # report/EXAMPLES.md, then replays every route and solution on the page

The text is `research/src/report_build/writeup.md` (and `real.md`, `app_c.md`, `bugs.md`), with `{{table}}` for a table from `report/data`, `{= expression =}` for a computed number (names in `report_build/xenv.py`) and `[[T123]]` for a link to a Discord message.

## Lean

    cd is-dr-xs-worth-it/lean/DRXs && lake build      # about a minute

See `lean/DRXs/README.md` for the list of theorems.
