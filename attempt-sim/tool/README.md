# The attempt simulator, for the web

The simulator of [*How to spend the hour*](../report/WRITEUP.md) as a library, a command-line program and a web page
that runs it in the browser (live at `/attempt-sim/tool/` on the site). Give it a scramble, change any time cost, human
limit or part of the plan, and it plays the hour: the solution it wrote down, every backup it found, and every step it
took, in order.

It is a port of the research program (`../research/attemptsim`) and gives its results exactly (see *Checks*).

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
