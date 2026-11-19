# Corners in 3D: how far from HTR, and which turn gets closer

The corners of any state, not just a DR, with DBL held and only R, U, F turns (3,674,160 states). What a solver can
see on them, what can be proved from it about the distance to HTR, and whether it gives the turn that gets closer.

Live at https://fmc.arhan.sh/corners-3d/ ([examples](https://fmc.arhan.sh/corners-3d/examples.html),
[errata](https://fmc.arhan.sh/corners-3d/errata.html)).

## What is in the folder

| Path | What |
|---|---|
| `report/WRITEUP.md`, `EXAMPLES.md`, `BUGS.md` | The pages. Generated: edit the sources in `research/src/report_build/` and run `assemble.py`. |
| `research/c3d/` | Rust: the corner model built from rotations (no table typed in), the turn tables, the kinds of every state and the distance tables. `c3d tables OUTDIR`, `c3d show "R U2 F'"`. |
| `research/src/c3.py`, `core.py` | Loaders for those tables and the shared helpers (types line, scramble of a state, a shortest way down a table). |
| `research/src/derive.py` | Parity, inverse, the type picture, colour pictures, the placement-only tables, DR-only tables per axis, the staged route, the six symmetries. |
| `research/src/analysis.py` | Every number of the write-up: `research/out/numbers.json`. |
| `research/src/extra.py`, `fullcorners.py` | NISS, the server's claims, and the checks that need all eight corners and D, L, B turns: `research/out/extra.json`. |
| `research/src/figures.py` | The mazes and the flow chart as inline SVG, drawn from the tables: `research/out/figures.json`, `figdata.json`, `figures/*.svg`. |
| `research/src/examples.py` | The catalogue, the 200 random states and the DR cases: `research/out/examples.json`. |
| `research/src/lean_witness.py` | Writes `lean/Corners3D/Corners3D/Pages.lean`: every scramble the pages print, for Lean to check. |
| `research/src/verify_pages.py` | Replays every scramble, solution and types line the pages print on a second model that shares no code with the tables. |
| `research/src/report_build/` | Page sources (`writeup.md`, `examples.md`, `bugs.md`), the numbers they may use (`env.py`), `assemble.py`, and `check_quotes.py` (every quotation against the cited message or document). |
| `lean/Corners3D/` | The Lean certificate. Its README lists the theorems. |
| `tool/web/` | The lookup page served at `/corners-3d/tool/`: plain JavaScript, no build step. It builds the tables in the browser (`corners.js`), and `tool/test/test.mjs` checks them against the study's (`node tool/test/test.mjs`). `count.js` and the test cases are written by `research/src/tool_data.py`. |

## Reproduce

    source /data/fmc/env.sh
    cd research/c3d && cargo test --release && cargo run --release -- tables ../out/big    # 8 s, 300 MB of tables
    cd ../src && python derive.py && python analysis.py && python extra.py && python figures.py && python examples.py
    python verify_pages.py && python tool_data.py && node ../../tool/test/test.mjs
    python lean_witness.py                                 # lean/Corners3D/Corners3D/Pages.lean
    cd report_build && python check_quotes.py && python assemble.py
    cd ../../../lean/Corners3D && lake build

`research/out/big/` (the tables) is not in the repository; the first two lines rebuild it.

## Conventions

- Places are printed in the order UFR UFL UBL UBR DFR DFL DBR. A types line uses `.` good, `+` `-` twisted
  clockwise / counter-clockwise, `r` `u` `f` out with only the R/L, U/D or F/B sticker oriented.
- *Solved* means HTR: the 24 states R2, U2, F2 reach. *Moves* are HTM. *Quarter turns* are counted with half turns free.
- A printed scramble of a state is a shortest R, U, F sequence that makes it from solved.
- The 200 random states are drawn uniformly from the 3,674,160 with a fixed seed (`examples.py`).
