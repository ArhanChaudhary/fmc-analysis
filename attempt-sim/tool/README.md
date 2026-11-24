# The attempt simulator, for the web

The simulator of [*How to spend the hour*](../report/WRITEUP.md) as a library, a command-line program and a web page
that runs it in the browser (live at `/attempt-sim/tool/` on the site). Give it a scramble, change any time cost, human
limit or part of the plan, and it plays the hour: the solution it wrote down, every backup it found, and every step it
took, in order.

It is a port of the research program (`../research/attemptsim`) and gives its results exactly (see *Checks*). The
additions in *Beyond the research program* change no research attempt.

## Layout

| Where | What |
|---|---|
| `sim/` | the simulator, a Rust library with no I/O (crate `attempt-sim`) |
| `cli/` | `attempt-sim`, the command-line program: batch runs in the research program's output format, one attempt as JSON, table checks |
| `wasm/` | the WebAssembly API the page uses (wasm-bindgen) |
| `web/` | the page: `index.html`, `app.js` (form, results, timeline), `worker.js` (runs the simulator off the page's thread), `tool.css`, `scrambles.txt` (1,000 of the write-up's random scrambles), `pkg/` (the built WebAssembly module, committed) |
| `build-web.sh` | rebuilds `web/pkg/` |

Reading order in `sim/src`: `cube.rs` (the whole cube, from the geometry of the turns), `eo.rs` (every EO up to a
length, normal, inverse and NISS), `rzp.rs` (from an EO to DRs: the RZP search of one EO ending and DR axis, with the
solver's blurred reads), `dr.rs` and `htr.rs` (the DR group and its HTR subsets), `prune.rs` (optimal DR finishes),
`routes.rs` and `finish.rs` (the route of a finish, the checklist routes of a subset), `settings.rs` (costs, human
limits, plans), `attempt.rs` (one attempt, step by step), `tables.rs` (everything built once).

## What changed from the research program

- **Optimal finishes by search.** The research program read every DR state's optimal finish from *Judging a DR*'s
  exact table (1.3 GB). A web page can't load that, so `prune.rs` searches (IDA*) with a smaller exact table as the
  bound: the distance of the corners and U/D-layer edges alone, E slice ignored, one entry per corner symmetry class and
  edge permutation (111.6 million entries, 4 bits each, 56 MB; exact up to 13 moves, 14 meaning 14 or more). It takes
  2.3 s to build natively and about 3 s in a desktop browser (longer on a phone); the page keeps it in IndexedDB, so
  later visits load it in a tenth of a second. The bound only cuts branches that can't reach solved within the budget, so the searches find
  the same finishes in the same order as the exact table did.
- **The cube from geometry.** The whole-cube model is built from the turns' geometry instead of the tables of
  `research/data/cubie.txt`; places are numbered as in the DR model, so a DR state reads off directly. A view (the
  cube turned so the EO axis is F/B and the DR axis U/D) is just the scramble with every turn renamed.
- **The same random draws everywhere.** The transcendental functions come from the `libm` crate, so the native program
  and the page give the same attempt to the last millisecond.
- **A record of the attempt.** With `record`, every step keeps what it was (which EO, which RZP moves, the read, which DR,
  which route, the finish), and every full solution keeps its parts and when it was found and written down. The
  simulation itself does not depend on it.
- Left out: the sensitivity knobs `cost.scale_*` and `reserve_scale`, the answer-key commands (`exhaust`, `cmpgaps`,
  `routecurve`, `export`).

## Beyond the research program

Five additions, none of which changes a research attempt (see *Checks*):

- **A cube a few turns from solved is seen** (`human.finish_see`, default 3). At the look, a scramble that leaves the
  cube at most that many turns from solved is seen with its solution; a DR whose finish is that short is finished as it
  goes onto the page. Before this, a one-turn scramble (`R`) found the DR `R'` at 0:44 and kept looking for EOs and DRs
  until the finishing phase (minute 35): the solution `R'` went down at 55:43.
- **Done when it can't matter** (`plan.bank_at` and `plan.stop_at`, default 12 instead of off). A solution of 12 moves
  or fewer is written down at once and ends the attempt. No research attempt comes within 3 moves of that. Writing down
  a solution shorter than 12 moves takes its share (n/12) of `costs.write`, so `R` is written and done at 0:26.
- **More than one DR per line goes on past a DR** (`plan.dr_per_line` over 1). With one DR per line (every research
  plan) a line stops below the first DR it sees, as before. With more, the solver keeps working the states past it and,
  from a state where the DR is seen d turns away, takes the other ways to a DR in d or d + 1 turns, one at a time, in
  the order of turns + the mean optimal finish of the subset they reach. Before this, a DR seen at the glance was the
  only DR its line ever gave, however many DRs per line the plan allowed.
- **A longer HTR may count** (`human.htr_extra`, default 2 = the research value). A route takes an HTR at most this
  many moves over the shortest NISS HTR; at 4, a long HTR with a short finish counts.

The world-record check below is what these were for.

## Build and run

    cargo build --release -p attempt-sim-cli
    target/release/attempt-sim table                               # build the finish table, check its checksum
    target/release/attempt-sim trace --scramble "R' U' F ..."      # one attempt, everything recorded, as JSON
    target/release/attempt-sim run --costs ../research/costs.toml --policies ../research/policies/conclusions.toml \
        --scrambles ../research/data/scrambles_uniform.txt --count 200 --out OUT.tsv [--log LOG --logn 20]
    cargo test -p attempt-sim                                      # model checks and three golden attempts

The page: `./build-web.sh` (needs the `wasm32-unknown-unknown` target and `wasm-bindgen-cli` 0.2.130), then serve the
site (`scripts/build-pages.sh` copies `web/` to `/attempt-sim/tool/`).

## The WebAssembly API

```js
import init, { Simulator } from './pkg/attempt_sim_wasm.js';
await init();
const sim = new Simulator();                       // small tables, under a second
while (sim.build_step(32) < 1) {}                  // the finish table, a slice at a time (progress 0..1)
// or: sim.load_table(bytes) with bytes kept from sim.table_bytes(); Simulator.table_version() names them
const { settings, plans } = JSON.parse(Simulator.defaults());   // settings = {costs, human, plan, seed, attempt}
const report = JSON.parse(sim.simulate(JSON.stringify({ scramble: "R' U' F ...", settings })));
// report = {scramble, outcome, subset, solutions, steps, kinds}
```

`settings` has the keys of `research/costs.toml` (`costs` = `[cost]`, `human` = `[human]`), the plan (the fields of a
`[policy.NAME]` section; `plans.tuned` and `plans.baseline` are the write-up's two), and the random draws: `seed` and
`attempt`. An unknown key is an error. The research runs used seed 1 and the scramble's number in
`research/data/scrambles_uniform.txt` as the attempt number, so those attempts can be replayed exactly.

Each step of `report.steps` has `start` and `ms` (clock in milliseconds), `kind` (one of the 11 kinds of the write-up's
section 3) and, under `type`, what it was. Each solution of `report.solutions` has when its finish was found, its
moves, its EO, DR (normal and inverse moves), subset, route, finish, the DR's optimal finish (computer only) and when
it was written down, if it was.

## Checks

- **Against the research program**, on the same scrambles, plans and costs (the research program with the exact
  table): 73,034 attempts, scrambles 0 to 2,199 of `scrambles_uniform.txt` and the 609 official scrambles, each with
  the 26 plans of `policies/conclusions.toml`. The output files are byte for byte the same (result, solution, clock,
  counts and time per step kind, every column), and so are the step logs of the 520 attempts logged (138,422 steps).
- **Optimal finishes**: on 3,000 random DR states the search gives the exact table's value every time
  (`attempt-sim check-optimal --exact judging-a-dr/research/data/lean_exact_table.u8`).
- `cargo test`: the cube model (move orders, orientation conventions, a superflip, inverses), the cube against the DR
  model on 500 random DR moves, routes read back, settings as JSON, the record adding up (steps follow each other,
  totals per kind, every solution solves the scramble), and three golden attempts from the research program's output.
- **World-record singles.** Every 3x3 FMC world-record single in the WCA results export (2026-11-13) plus Riccardo
  Raciti's 16 at FMC Italy 2026 (2026-11-21), 60 attempts per scramble. The WCA publishes no scrambles for the seven
  records before 2015 (Goljan 29 and 28, Zborowski 28, Razoux Schultz 27, Coll 22, Kocza 22, Okayama 20), so they
  can't be run. *Strong solver* is the research human with `dr_see_glance` [1, 1, 1, 1, 0.9, 0.6, 0.3, 0.1],
  `dr_see_work` [1, 1, 1, 1, 1, 0.95, 0.8, 0.5], `read_sd` 0.7, `route_see` 0.95 and `htr_extra` 4; *wide plan* is
  the tuned plan with `dr_per_line` 3, `rzp_per_eo` 5, `read_max` 11, `htr_per_dr` 6, `fin_min_p` 0 and `t_dr` 1800.
  The DR column is a solution of record length or shorter that a computer finds with the DR method (cubelib, quality
  100,000), if there is one.

  | Record (date, moves, competition) | DR solution exists | Tuned plan, research human: attempts at record or better | Wide plan, strong solver: attempts at record or better |
  |---|---|---|---|
  | 2015-07-10, 20, Michigan 2015 | yes (19) | 16 of 60 | 23 of 60 (best 18) |
  | 2015-10-11, 19, Irvine Fall 2015 | no | 0 | 0 (best 21) |
  | 2016-01-09, 19, Cubelonia 2016 | no | 0 | 0 (best 21) |
  | 2016-08-27, 19, PSU Open 2016 | yes | 0 | 14 of 60 |
  | 2018-04-30, 19, Beijing Open 2018 | yes | 0 | 0 (best 21) |
  | 2018-10-26, 18, GA Cubers Mountain Trip 2018 | no | 0 | 0 (best 20) |
  | 2018-10-26, 19, Polish Championship 2018 | cubelib found none; the simulator did | 3 of 60 | 1 of 60 |
  | 2019-01-19, 17, TGBBO 2019 | yes | 0 | 60 of 60 |
  | 2019-06-08, 17, Mental Breakdown Minnesota 2019 | yes | 0 | 0 (best 18) |
  | 2019-06-15, 16, FMC 2019 | yes | 4 of 60 | 23 of 60 |
  | 2024-06-23, 16, Ashfield Summer Challenge 2024 | no | 0 | 0 (best 20) |
  | 2024-10-26, 16, Rubik's UK Championship FMC 2024 | yes | 0 | 16 of 60 |
  | 2026-11-21, 16, FMC Italy 2026 | yes | 0 | 5 of 60 |

  Beijing 2018 and Minnesota 2019 have DR solutions of record length that the simulated solver doesn't reach.
  Minnesota's starts from one 5-move EO out of 131 on its axis (the 144th EO written down in a ten-hour run), and the
  solver works EOs in the order it wrote them. Beijing's starts from a 5-move EO with moves on both sides,
  `U' R F' (L' F')`, then 2 RZP turns and a 3-turn DR; why the solver misses it is not diagnosed yet. Irvine, Cubelonia, GA Cubers and
  Ashfield have no DR solution of record length at all: those records were not DR solves, and the simulator only plays
  the DR method.
