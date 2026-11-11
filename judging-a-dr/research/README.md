# research — exhaustive computations behind the DR-bounding report

| Path | What |
|---|---|
| `drtools/` | Rust crate (rayon only, `#![forbid(unsafe_code)]`). `cargo build --release`, then `target/release/drtools <cmd>`: `selftest`, `bfs`, `ladder`, `census`, `census2`, `sharp`, `parity`, `query`, `genlean`. |
| `tool/drbound` | Command-line lookup: scramble + moves to DR (NISS in brackets) -> subset, every bound on both sides, exact optimum, verdict against a target. Uses `tool/fmccube.py` (a small cube simulator) and `drtools query`. |
| `src/*.py` | Analyses and cross-checks: `check_joba.py`, `check_nissy.py`, `allmoves216.py`, `compare216.py`, `check_rodney_sheet2.py`, `check_oblpp_cells.py`, `an*.py`, `mk_tables.py`. |
| `data/drbfs/` | Exact optimum of all 19,508,428,800 DR states: one bitset per depth over the symmetry-reduced index (3.2 GB). |
| `data/tables/` | The ladder tables `T_<rung>.u8` (one byte per class). |
| `out/` | Census CSVs, logs of every check quoted in `report/`. |
| `legacy_c/` | The first C implementation, superseded by `drtools` (byte-identical outputs); kept as a second implementation only. |

Memory: every command here runs in under 1 GB except `drtools ladder` (about 0.9 GB) and `allmoves216.py` (about 3 GB);
on this VM wrap heavy runs in `systemd-run --user --scope -q -p MemoryMax=2500M …` and run one at a time.
