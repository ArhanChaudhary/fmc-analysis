# Which HTR routes to try from a DR

The fifth case study here: from a DR to HTR. For each of the 48 subsets (corner subset × bad edges): which routes to HTR find the optimal finish, in what order to try them, and how long their HTRs are. Also linear against NISS HTR and which HTR the optimal uses, DR bounding measured per subset with the number of reductions, FakeMMAP's reduction-length bound tested, hand checklists graded, and every concrete claim from the FMC solvers Discord on these topics checked against the numbers.

It builds on Daichi's cheat sheet, Levi Gibson's *allcases*, *Extra Quarter-Turn Stats* and *DR Bounding*, Aedan Bryant's *HTR Subset Stats*, Joba's exact optimal distribution, DougCube's HTR-state table, rodneykinney's *DR Finish Move Counts*, normal forms and *Advanced DR Bounding*, FakeMMAP's reduction bound, JTuu's 2c3 2e simulation, and the hand orders of Zagros, Yura Riabov, rogo, Adri, Lewis Isom, Jay and rodneykinney. What it adds: a checklist per subset × edges with the share of DRs each prefix finds (optimal and +1) under an HTR budget; which letter each sheet gives 4b2 and 4a2 (the server had it for *allcases*; the *Extra Quarter-Turn Stats* sheet uses the opposite letters); HTR lengths against the optimal; bounding effectiveness and reduction counts; the test FakeMMAP asked for, with a correction to the multi-qt lower bound.

| Where | What |
|---|---|
| [report/WRITEUP.md](report/WRITEUP.md) | the write-up |
| [report/EXAMPLES.md](report/EXAMPLES.md) | worked examples: 200 DR states from the 20 most common subset × edges, with the checklist routes that find each optimal written out and the shortest bounding reduction |
| [report/BUGS.md](report/BUGS.md) | errata: what the numbers show is wrong in things said on the server |
| `research/SPEC.md` | the questions and the model |
| `research/README.md` | every step of the computation: command, input, output, time, memory, and the checks |
| `research/htrtools/` | the Rust side: sampling per subset, every optimal and +1 finish with every NISS reading, shortest HTRs, reductions and their counts, bound data |
| `research/src/` | the Python side: sticker-model checks, nissy cross-checks, analysis, claims, witnesses, report tables, examples page |
| `research/out/` | the result tables (`SUMMARY.md` states every answer) |
| `lean/HTRRoutes/` | Lean certificate of the small exact tables (HTR group, corner subsets and qt counts, shortest linear HTR per coset, α per corner path, 2qt labels) |

## How the numbers are made

Finish lengths come from the first study's exact table of the optimal finish of all 19,508,428,800 DR states (`judging-a-dr/research/data`, Lean-proved there). `htrtools` draws 25,000 uniform states per subset × edges and enumerates every optimal and +1 finish (both orders of commuting moves), every NISS reading, the same for the DR with its last move turned the other way, the shortest HTR on each side and with NISS, and every reduction to 1q / 2q. An independent sticker model re-reads every finish of 1,240 states, nissy 2.0.8 lists the same optimal finishes, and every move sequence printed in the reports is replayed. `research/run_all.sh` lists the heavy commands in order (about an hour on four cores, at most 5 GB per job).

Large outputs (`research/out/big/`, per-state data) are not in the repository; `run_all.sh` regenerates them.

## Rebuilding the report

    source /data/fmc/env.sh
    cd htr-routes/research/src
    python xchecklist.py                           # out/q2_same_classes_p1.tsv: the checklists read at +1 (about 2 minutes, 2 GB)
    python xwitness.py                             # out/witness_extra.json: four extra examples, replayed (nissy -N takes a few minutes)
    python xlbdist.py                              # out/q9_lb_values.tsv: typical value of FakeMMAP's multi-qt lower bounds (a few minutes, 4 GB cap)
    python xtables.py                              # report/data/*.md and out/report_extra.json (reads Aedan Bryant's sheet from the kb through sheet15.py)
    python report_build/assemble.py --final        # report/WRITEUP.md (every number is computed; --final fails if one is missing)
    python report_build/assemble.py --bugs --final # report/BUGS.md
    python xexamples.py                            # report/EXAMPLES.md, every move sequence replayed on the sticker model
    python report_build/check_quotes.py            # every quotation against its message or document

The text is `research/src/report_build/writeup.md` with the `sec_*.md` and `app.md` parts next to it, and `bugs.md`: `{{table}}` for a table from `report/data`, `{{PART}}` for another text file of that folder, `{= expression =}` for a computed number (names in `report_build/xenv.py`) and `[[T123]]` for a link to a Discord message.

`out/checks/lsdist48.tsv` (leave-slice optimum per subset, every DR state) is made by `htrtools lsdist ls_depth.u8` (it histograms the leave-slice table by subset, like `dist`).

The reading notes, the register of what was said and the Discord export are not in the repository; the quote check needs them.
