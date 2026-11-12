# Insertion cost by skeleton type

The third case study of this repository: what an insertion costs. For every kind of leftover that one or two 3-cycle insertions solve (3c, 5c, 2c2c, 3c1t, twisted corners, and the same for edges), how many moves the best insertion adds, by skeleton length and by how long an inserted alg may be, with every concrete claim from the FMC solvers Discord about insertions checked against the numbers.

It builds on the table in Sebastiano Tronto's tutorial ("Move count (an estimate)"), on the estimates, exchange rates and counts people posted, and it uses Insertion Finder's result pages (333.fm, by Baiqiang Dong, core by Yan Xuan) as a reference. What it adds is the measured version: odds instead of one number per type, the effect of the alg list (8, 10 and 12 moves), exchange rates between types, where the best insertion sits and what shorter searches lose, the exact list of leftovers that two or three comms solve, the shortest alg of every case that has one of 12 moves or fewer, and worked examples from real solves searched the same way.

| Where | What |
|---|---|
| [report/WRITEUP.md](report/WRITEUP.md) | the write-up |
| [report/EXAMPLES.md](report/EXAMPLES.md) | worked examples: examples from the tutorial and the server redone, then 200 skeletons to play along with |
| [report/BUGS.md](report/BUGS.md) | errata: what the numbers show is wrong in things said on the server |
| `research/SPEC.md` | the model: skeleton, leftover, insertion, cost, the cap on alg length, the models `one`, `two`, `direct`, `mixed` |
| `research/instools/` | the Rust side: all algs up to 12 moves for every leftover, the exact best insertion(s) of a skeleton, samplers |
| `research/src/` | the Python side: sticker model, leftover types, checks, real skeletons, report tables, examples page |
| `lean/Insertions/` | Lean certificate of which leftovers one, two or three 3-cycles make |

## How the numbers are made

Everything starts from one sticker-level model of the cube built from geometry (`research/src/cube.py`); no permutation is typed by hand anywhere, and the Rust tool reads tables exported from it. `research/src/run_all.sh` lists the heavy commands in order.

| Step | Script | Output (under `research/out/`) |
|---|---|---|
| Leftover types and how many 3-cycles each needs | `leftover_types.py` (and `lean/Insertions`) | `types.json` |
| Move tables for Rust | `export_tables.py` | tables read by `instools` |
| All algs up to 8, 10, 12 moves for every type | `instools algs <L>` | `algs_L*.bin`, `algs_L*_summary.txt`, `cases_<type>_L*.tsv` |
| Corner-only sequences of up to 12 moves that leave a corner twisted in place, whatever their type | `instools twistmin 12` | `twistmin_L12.txt` |
| Random skeletons: best insertion under every model and cap | `instools runs`, `run_base_odd.sh` | `sample_<type>_n<n>.tsv` (even lengths), `base_*` (odd lengths), `mixed_*`, `two12_*` |
| Histograms of the samples | `histograms.py` | `hist.json` |
| One comm, spot by spot, in Python (also a check of the tool) | `py3.py`, `xone.py` | `algs3c_L*.json`, `onepos_3c_n<n>.tsv` |
| Two comms the way people do them (best first comm, then the best second) | `xgreedy.py`, `xgreedy_sum.py` | `greedy_*.tsv`, `greedy.json` |
| Small exact facts about the 3-cycle algs, and the quoted algs on the sticker model | `facts.py` | `facts.json` |
| A 3c on modelled 17-move skeletons: random moves, moves that keep EO, DR moves | `xdr.py` | `dr17.json` |
| Every check again, with its output | `checks.py`, `checks.py --report` | `checks.txt`, `checks_report.txt`, `checks.json` |
| Real skeletons: the server's worked examples and Kalbarczyk's solves | `corpus_cyprian.py`, `replay.py`, `real_cases.py`, `real_run.py`, `xreal.py` | `real_cases.tsv`, `real_meta.json`, `real_best.txt`, `real.json`, `corpus_real_*.tsv` |
| Insertion Finder pages | `instools best --file`, `if_table.py` | `if_cases.tsv`, `if_best.txt`, `if_compare.tsv` |
| Example scrambles for the claims | `exlib.py`, `witness.py` | `witness.json`, `report_build/wit_*.md` |
| Report tables | `xtables.py`, `xgreedy_sum.py`, `xreal.py` | `report/data/*.md` |
| How people are named in the pages | `names.py` | |
| Write-up and errata | `report_build/assemble.py` (and `--bugs`) | `report/WRITEUP.md`, `report/BUGS.md` |
| Examples page | `xexamples.py --cases`, then `xexamples.py` | `examples_cases.json`, `report/EXAMPLES.md` |

Checks built in:

- `instools selftest` and `count`: the Rust cube and its cancelling against `cube.py`; the sizes of the 15 types three ways.
- `instools algs --check`: the meet-in-the-middle lists against an independent search, class by class.
- `instools bf1`, `bf2`: one and two insertions against plain enumeration on small skeletons.
- `xone.py`: the best one-comm insertion of every sampled 3c skeleton recomputed in Python on the sticker model; `xgreedy.py --full`: the same for two comms on 5c skeletons.
- `check_solutions.py`: every solution printed by the tool replayed on the sticker model.
- `real_cases.py`, `xreal.py`: every real example put on the sticker model before it is counted; the author's own solution replayed where it is written out.
- `witness.py --verify`, `xexamples.py --verify`: every scramble, skeleton and solution printed in the reports read back from the text and replayed.
- `report_build/check_quotes.py`: every quotation against the message or document it is cited from.

Large outputs (`research/out/sample_*.tsv`, `base_*.tsv`, `algs_L*.bin`, `onepos_*.tsv`, `corpus_real_*`, `real_cache.json`, build directories) are not in the repository; `run_all.sh` regenerates them (about two hours on four cores, most of it the real skeletons at cap 12 and the greedy runs; about 1.2 GB of disk).

The reading notes and the 389 worked examples come from the Discord export, which is not in the repository; `real_cases.py` needs them.

## Rebuilding the report

    source /data/fmc/env.sh
    cd insertion-cost/research/src
    python histograms.py && python xone.py 10,12,14,16,18,20,22,24,26,28,30 && python facts.py && python xdr.py
    python real_cases.py && python real_run.py && python xreal.py --corpus && python xreal.py
    ./run_greedy.sh && python xtables.py && python witness.py && python checks.py
    python report_build/assemble.py --final       # report/WRITEUP.md (every number is computed; --final fails if one is missing)
    python report_build/assemble.py --bugs        # report/BUGS.md
    python xexamples.py                           # report/EXAMPLES.md, then replays everything on the page
    python checks.py --report                     # witness blocks, examples page and quotations once more, with the output kept

The text is `research/src/report_build/writeup.md` and the `sec_*.md`, `app.md` and `bugs.md` files next to it, with `{{table}}` for a table from `report/data`, `{{PART}}` for another text file of that folder, `{= expression =}` for a computed number (names in `report_build/xenv.py`) and `[[N123]]` for a link to a Discord message.

## Lean

    cd insertion-cost/lean/Insertions && lake build      # about three minutes

See `lean/Insertions/README.md` for the list of theorems.
