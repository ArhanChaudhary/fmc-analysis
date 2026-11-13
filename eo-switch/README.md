# When to switch an EO

The sixth case study of this repository: after EO + RZP, when to switch (go to the inverse, keep the EO and look for a short DR there). Its main result is a count: how many turns of the side faces the DR needs when U and D turns are free. A U or D turn never makes or breaks a pair, so a switched case is two rings (the U and D layers up to turning) and the four E-slice places, a half turn swaps a row between the rings, and a quarter turn has a one-line rule. For 4c4e the count is the number of half turns to two bars: 0 or 1 is a certain sub-7, 2 is 72.1%, 3 is 16.0%, 4 or 5 is 1.7%. For every DRM, 2 side turns or fewer is a certain sub-7, and 3 with no extra quarter turn is the switch group. The study also gives a switch card per DRM for a pair trace alone, shows how to read every feature (the rings included) from the normal side, covers what a real RZP changes (the RZP bias, gone after a switch; the last RZP and EO turns; the second DR axis; RZP length), grades every switch rule from the FMC solvers Discord on the same terms, reproduces the published tables, and checks every concrete claim.

It builds on Cale's *DR setup stats*, Louis's *DRM/ARM average optimals*, rodneykinney's corner cases, *DR - 4c4e Theory* (the two-bar target and the half turns that form pairs), *DRM corner variant+pair stats*, *DRM Subsets* and its trees, Evan's *arm/pairs* sheets, Fanti's rule sets, Radek B's and Levi Gibson's tables, wen's pair tracing, torchlight's RZP bias, and the hand rules of Yura Riabov, tseitsei89, wen, Jay, Noah Swor, Lewis Isom, caycala, compLex, Daichi and Zagros. What it adds:

- The two-ring picture, exact for every case: what U/D turns, half turns and quarter turns do to it.
- For 4c4e, half turns to two bars: the bands above, the count as the larger of row swaps and a hole number, how to read it from a pair trace (exact rule for 3 and 4 pairs, a one-swap look for 2), and every ring picture with 2 swaps or fewer.
- For every DRM, side turns: the certain class, quarter turns against half turns, the trigger cases in ring notation, and each card's groups split by them (7c8e with 5-6 pairs: 95.4% against 33.8%).
- For 4c4e by a pair trace alone, a rule that settles about twice as many cases as pairs or ARM: count the paired edges, then look at edge ARM.
- The your-call groups split by the corner case.
- The rings, side pairs and edge ARM read on the normal side.
- Proof that the uniform tables are exact for switched RZPs.
- A grade for every rule on exact cases and on 121.5 million real attempts.
- That Fanti's figures are any-turn numbers.

| Where | What |
|---|---|
| [report/WRITEUP.md](report/WRITEUP.md) | the write-up |
| [report/EXAMPLES.md](report/EXAMPLES.md) | worked examples: 200 real attempts from uniform scrambles, with what to trace, the card's verdict and the optimal DR after the switch, folded away |
| [report/BUGS.md](report/BUGS.md) | errata: the one statement from the server that the numbers go against, with an example |
| `research/SPEC.md` | the questions and the model |
| `research/eoswtools/` | the Rust side: the BFS over all 1,082,565 EO-solved cases, the second-axis completions, the RZP weights, the sampled attempts |
| `research/src/` | the Python side: features (sticker model), the two-ring model and its counts (`rings.py`, `xrings.py`, `xtrace_rings.py`), populations, reproduction, grading, rule search, NISS and tracing checks, claims, witnesses, report tables, examples page |
| `research/out/` | the result tables (`SUMMARY.md` states every answer) |
| `lean/EOSwitch/` | Lean certificate: its own BFS over all cases, the features from stickers, the distance histogram, the per-DRM counts and every cell of the card tables, and that the printed tables match; the two-ring picture and its turn rules on every case, side turns, half turns to two bars as the larger of row swaps and hole number, the band tables, the 3-pair recipe and the list of ring pictures with 2 swaps or fewer |

## How the numbers are made

`research/run_all.sh` regenerates everything in about six minutes on four cores, each heavy step capped at 4 GB. It needs is-dr-xs-worth-it's `out/tables/` and eo-to-dr's `eodrtools` and `out/big/` tables. The distances come from a BFS with the 14 EO-keeping turns. They are checked against eo-to-dr's table on every case and against nissy 2.0.8 on 1,000. The features are defined from stickers and checked against rodneykinney's own code on every case. The real attempts are every EO of up to 6 moves, with every RZP to a total of 4, 5 or 6, on 6,000 uniformly random scrambles.

Large outputs (`research/out/big/`, per-case data and the attempts) are not in the repository. `run_all.sh` regenerates them.

## Rebuilding the report

    source /data/fmc/env.sh
    cd eo-switch/research/src
    python xtrace.py 20000                         # out/checks_trace.tsv: the tracings of section 5 on random cubes (a few minutes)
    python rings.py                                # out/big/rings.npz, out/checks_rings.txt: the ring picture checked on every case, side turns, half turns to two bars
    python xrings.py                               # report/data/ring_*.md, out/rings.json, out/ring_examples.json (every example replayed), out/rings_lean_ref.json
    python xtrace_rings.py 20000                   # out/checks_trace_rings.tsv: the rings read on normal, on random cubes
    python xtables.py                              # report/data/*.md and out/report_extra.json
    python report_build/assemble.py --final        # report/WRITEUP.md (every number is computed; --final fails if one is missing)
    python report_build/assemble.py --bugs --final # report/BUGS.md
    python xexamples.py                            # report/EXAMPLES.md, every move sequence replayed on the sticker model, lengths checked with nissy
    python report_build/check_quotes.py            # every quotation against its message or document

The text is `research/src/report_build/writeup.md`, with the `sec_*.md` and `app.md` parts next to it, and `bugs.md`. `{{table}}` includes a table from `report/data`, `{{PART}}` another text file of that folder, `{= expression =}` a computed number (names in `report_build/xenv.py`), and `[[T123]]` a link to a Discord message.

The reading notes, the register of what was said and the Discord export are not in the repository; the quote check needs them.
