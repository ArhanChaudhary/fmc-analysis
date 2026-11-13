# EO to DR, and scramble to DR

The fourth case study of this repository: the first half of a DR solve. How far a random scramble is from DR (one axis, best of three, with the inverse, with NISS, and through the short EOs a solver writes down), how many EOs a scramble has and how short, and what an EO leaves: how far DR is with the other DR axis, the inverse, the EO's last turn the other way and EO-breaking turns, overall and case by case. Every concrete claim from the FMC solvers Discord on these topics is checked against the numbers.

It builds on Cale's *DR setup stats* (and its version with the last EO move switched), Louis's *DRM/ARM average optimals* and Rodney Kinney's sheet built on it, KrzychXyz's and Evan's sheets, Shota's EO tables, FakeMMAP's and torchlight's EO to DR tables, DougCube's *Tables of Distinct Positions*, Joba's exact NISS EO table, Sebastiano Tronto's EO-solved scrambles, torchlight's exact bad-edge counts, and the DR-xs study's section 6.4. What it adds:

- DR from a scramble over all axes, with the inverse and with NISS, with the odds of a DR in 8, 9, 10 and 11;
- the EO inside the optimal DR, and the best DR through EOs of each length;
- the number of DRs per EO;
- EO counts and shortest EOs per scramble on all axes, and the bad-edge layouts exactly;
- EO to DR with every option you have, including the second DR axis exactly;
- a check of nissy 2.0.8's scrambler, which has a modulo bias in its edge permutation that makes DRs on the inverse of its scrambles shorter.

| Where | What |
|---|---|
| [report/WRITEUP.md](report/WRITEUP.md) | the write-up |
| [report/EXAMPLES.md](report/EXAMPLES.md) | worked examples: 150 scrambles with their shortest DRs and their best DRs through EOs of at most 4 and 5, then 60 EO-solved states by case |
| [report/BUGS.md](report/BUGS.md) | errata: what the numbers show is wrong in things said on the server |
| `research/SPEC.md` | the questions and the model |
| `research/README.md` | every step of the computation: command, input, output, time, and the checks |
| `research/eodrtools/` | the Rust side: scrambles, per-scramble search (DR distances, NISS DR, EOs of up to 6 turns with their DRs), EO to DR tables, EO tables, checks |
| `research/src/` | the Python side: sticker-model checks, nissy cross-checks, analysis, report tables, examples page |
| `research/out/` | the result tables (`SUMMARY.md` states every answer) |
| `lean/` | Lean certificate of the small exact tables (see `lean/EODR/README.md`) |

## How the numbers are made

The cube model and the two exact coset tables (fewest turns to DR with any turns, and keeping an EO; 2,217,093,120 cosets each) are the DR-xs study's (`is-dr-xs-worth-it/research/`), read through rotations for the other axes. Each mapping is checked against nissy 2.0.8 on 1,000 or 2,000 positions; every solution printed anywhere is replayed on a sticker model that reads EO and DR off the stickers. The scrambles are 50,000 uniformly random states drawn by the study (`eodrtools mkscr`); nissy's `scramble` isn't used, because it's biased (appendix B of the write-up). `research/run_all.sh` lists the heavy commands in order (about 50 minutes on four cores, peak memory about 3.5 GB).

Large outputs (`research/out/big/`, the per-scramble tables) are not in the repository; `run_all.sh` regenerates them. The distance tables come from the DR-xs study (2.2 GB each).

## Rebuilding the report

    source /data/fmc/env.sh
    cd eo-to-dr/research
    # the extra examples data (seconds): the first 150 scrambles inverted, and every EO of at most 4 on scrambles 151-450
    eodrtools/target/release/eodrtools scr out/big/ex_inv150.txt 11 6 > out/big/ex_inv150.tsv
    eodrtools/target/release/eodrtools eolist 4 <scrambles 151-450 of out/scrambles.txt> > out/big/ex_eolist.tsv
    cd src
    python xtables.py                              # report/data/*.md and out/report_extra.json
    python xwitness.py                             # out/witness_extra.json, replayed
    python both_eo.py                              # out/both_eo.json: the cases with no edge out of place (seconds)
    python default_listing.py                      # out/default_listing.json: nissy's default EO listing against -a (about a minute)
    python report_build/assemble.py --final        # report/WRITEUP.md (every number is computed; --final fails if one is missing)
    python report_build/assemble.py --bugs --final # report/BUGS.md
    python xexamples.py                            # report/EXAMPLES.md, every move sequence replayed on the sticker model
    python report_build/check_quotes.py            # every quotation against its message or document

The text is `research/src/report_build/writeup.md` with the `sec_*.md` and `app.md` parts next to it, and `bugs.md`: `{{table}}` for a table from `report/data`, `{{PART}}` for another text file of that folder, `{= expression =}` for a computed number (names in `report_build/xenv.py`) and `[[N123]]` for a link to a Discord message.

The reading notes, the register of what was said and the Discord export are not in the repository; the quote check needs them.
