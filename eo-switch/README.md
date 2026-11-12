# When to switch an EO

The sixth case study of this repository: after EO + RZP, when to switch (go to the inverse, keep the EO and look for a short DR there). It gives a switch card per DRM, a rule a solver can check by tracing, with the sub-7 share of each verdict (switch, your call, discard) and how much of the DRM it settles. It shows how to read every feature of the cards from the normal side, including two new tracings (side pairs and edge ARM on the inverse). It also covers what a real RZP changes (the RZP bias, gone after a switch; the last RZP and EO turns; the second DR axis; RZP length), grades every switch rule from the FMC solvers Discord on the same terms, reproduces the published tables, and checks every concrete claim.

It builds on Cale's *DR setup stats*, Louis's *DRM/ARM average optimals*, rodneykinney's corner cases, *DRM corner variant+pair stats*, *DRM Subsets* and its trees, Evan's *arm/pairs* sheets, Fanti's rule sets, Radek B's and Levi Gibson's tables, wen's pair tracing, torchlight's RZP bias, and the hand rules of Yura Riabov, tseitsei89, wen, Jay, Noah Swor, Lewis Isom, caycala, compLex, Daichi and Zagros. What it adds:

- For 4c4e, a rule that settles about twice as many cases as pairs or ARM: count the paired edges, then look at edge ARM.
- The your-call groups split by the corner case.
- Side pairs and edge ARM read on the normal side.
- Proof that the uniform tables are exact for switched RZPs.
- A grade for every rule on exact cases and on 121.5 million real attempts.
- That Fanti's figures are any-turn numbers.

| Where | What |
|---|---|
| [report/WRITEUP.md](report/WRITEUP.md) | the write-up |
| [report/EXAMPLES.md](report/EXAMPLES.md) | worked examples: 200 real attempts from uniform scrambles, with what to trace, the card's verdict and the optimal DR after the switch, folded away |
| [report/BUGS.md](report/BUGS.md) | errata: what the numbers show is wrong in things said on the server |
| `research/SPEC.md` | the questions and the model |
| `research/eoswtools/` | the Rust side: the BFS over all 1,082,565 EO-solved cases, the second-axis completions, the RZP weights, the sampled attempts |
| `research/src/` | the Python side: features (sticker model), populations, reproduction, grading, rule search, NISS and tracing checks, claims, witnesses, report tables, examples page |
| `research/out/` | the result tables (`SUMMARY.md` states every answer) |
| `lean/EOSwitch/` | Lean certificate: its own BFS over all cases, the features from stickers, the distance histogram, the per-DRM counts and every cell of the card tables, and that the printed tables match |

## How the numbers are made

`research/run_all.sh` regenerates everything in about six minutes on four cores, each heavy step capped at 4 GB. It needs is-dr-xs-worth-it's `out/tables/` and eo-to-dr's `eodrtools` and `out/big/` tables. The distances come from a BFS with the 14 EO-keeping turns. They are checked against eo-to-dr's table on every case and against nissy 2.0.8 on 1,000. The features are defined from stickers and checked against rodneykinney's own code on every case. The real attempts are every EO of up to 6 moves, with every RZP to a total of 4, 5 or 6, on 6,000 uniformly random scrambles.

Large outputs (`research/out/big/`, per-case data and the attempts) are not in the repository. `run_all.sh` regenerates them.

## Rebuilding the report

    source /data/fmc/env.sh
    cd eo-switch/research/src
    python xtrace.py 20000                         # out/checks_trace.tsv: the tracings of section 5 on random cubes (a few minutes)
    python xtables.py                              # report/data/*.md and out/report_extra.json
    python report_build/assemble.py --final        # report/WRITEUP.md (every number is computed; --final fails if one is missing)
    python report_build/assemble.py --bugs --final # report/BUGS.md
    python xexamples.py                            # report/EXAMPLES.md, every move sequence replayed on the sticker model, lengths checked with nissy
    python report_build/check_quotes.py            # every quotation against its message or document

The text is `research/src/report_build/writeup.md`, with the `sec_*.md` and `app.md` parts next to it, and `bugs.md`. `{{table}}` includes a table from `report/data`, `{{PART}}` another text file of that folder, `{= expression =}` a computed number (names in `report_build/xenv.py`), and `[[T123]]` a link to a Discord message.

The reading notes, the register of what was said and the Discord export are not in the repository; the quote check needs them.
