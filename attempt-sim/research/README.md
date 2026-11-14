# attempt-sim research: the simulator, the runs, the tables

Everything behind `../report/WRITEUP.md`. The simulator is a Rust program (`attemptsim/`); the experiments are policy
files (`policies/`) run on scramble files (`data/`) with one cost file (`costs.toml`); Python scripts (`src/`) turn
the result files into the report's tables.

## Layout

| Where | What |
|---|---|
| `attemptsim/` | the simulator (Rust, one crate). Reading order: `ctx.rs` (cube model and tables), `eo.rs` (EOs), `line.rs` (RZP to DR), `finish.rs` (HTR routes and finishes), `conf.rs` (costs, human limits, policies), `solver.rs` (one attempt), `cmds.rs` (commands). `vendor/` holds copies of other studies' sources: `cubie.rs` (is-dr-xs-worth-it), `core.rs`, `class.rs`, `reduced.rs` (judging-a-dr), `model.rs`, `routes.rs` (htr-routes). |
| `costs.toml` | **the time costs and the human limits**: the numbers to tune, each with a comment saying where it comes from |
| `policies/*.toml` | the plans for the hour. `base.toml` is the baseline; `e1_split` … `e5_curves` are the experiments, `all.toml` is all of them in one file (written by `src/make_policies.py`); `final.toml` the policies reported as recommendations; `cal.toml`, `cal1.toml` the calibration runs |
| `data/` | `scrambles_uniform.txt`: 10,000 uniformly random states written as scrambles (the first 10,000 of the EO-to-DR study's 50,000, `eodrtools mkscr 50000 2026`, by way of the gaps study); `official_scrambles.txt`: the scrambles of the top-10 group's official attempts since 2024 (from the WCA export, `src/wca_top.py`); `checklist.tsv` (htr-routes' main checklist per subset), `dist48.tsv` (htr-routes: optimal finish distribution of all DR states per subset), `cubie.txt` (the cubie model's tables) |
| `jobs/*.txt` | job lists for `remote_batch.sh` (one experiment per line) |
| `src/` | `make_policies.py` (policy files), `simstats.py` (statistics, paired differences), `tables.py` (every table and number of the report), `analyze.py` (quick look at one result file), `wca_extract.py`, `wca_top.py` (real results from the WCA export), `report_build/` (the write-up's sources and `assemble.py`) |
| `out/` | small results: `wca_top_summary.tsv`, `wca_top_attempts.tsv`, the answer key `key_eo5_cap11.tsv`, the Lean export; `out/big/` (not in git) holds every run's result file |
| `run_all.sh` | every run and table, in order |
| `remote_batch.sh`, `run_local.sh` | run a job list on another machine / one job here |

## Build

    source /data/fmc/env.sh                     # cargo
    cd attemptsim
    cargo build --release --target x86_64-unknown-linux-musl     # static binary: runs on the other machines too
    target/x86_64-unknown-linux-musl/release/attemptsim selftest  # model checks (EO-kept distance histogram = Cale's table, DR coordinates, NISS convention)

The simulator needs judging-a-dr's exact optimal-finish table, `judging-a-dr/research/data/lean_exact_table.u8`
(1.3 GB, sha256 `26cc1c0a…5e1fe0`, written by that study's Lean project), passed as `--exact`. It holds it in memory.

## Run

    attemptsim run --costs costs.toml --policies policies/base.toml --scrambles data/scrambles_uniform.txt \
        --first 0 --count 1000 --exact TABLE --out out/big/NAME.tsv [--set cost.rzp=10] [--set human.read_sd=0.5] [--log FILE --logn K]

Every policy of the file plays every scramble. Threads: `RAYON_NUM_THREADS`. Output: one row per policy × scramble
(result, clock, counts and minutes per step kind, the result's DR and when it was found, the scramble's features) and a
summary per policy on stdout. `--log` writes the full step log of the first K scrambles (the Lean sample). Every
solution found is replayed on the cube; the run fails if one doesn't solve the scramble.

Speed: about 10 ms of one modern core per attempt (the route tables of a scramble are shared by all its policies), so
236 policies on 4,000 scrambles is about 2.5 core-hours.

## Change a cost

Edit `costs.toml` (every key is documented there; an unknown key is an error), or override one run with
`--set cost.KEY=VALUE` / `--set human.KEY=VALUE` (arrays as `[a,b,c]`). `cost.scale_eo`, `scale_dr`, `scale_fin`,
`scale_write`, `scale_all` multiply whole groups of costs. Then rerun `run_all.sh` (or the stage you need).

## Add a policy

Add a `[policy.NAME]` section to a file in `policies/` (or to `src/make_policies.py` and rerun it). `base = "OTHER"`
copies another section of the same file first; every key is a field of `Policy` in `attemptsim/src/conf.rs`, with its
meaning in the comment next to it. Times are seconds on the clock of a one-hour attempt; with another `budget` they
scale with it.

## WCA data

The official results and scrambles used here come from the WCA results export (version 2.0.2, 13 November 2026, https://www.worldcubeassociation.org/export/results). This information is based on competition results owned and maintained by the World Cube Association, published at https://worldcubeassociation.org/results as of November 13, 2026.
