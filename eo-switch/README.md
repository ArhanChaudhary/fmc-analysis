# When to switch an EO

The sixth case study of this repository: after EO + RZP, when to switch (go to the inverse, keep the EO and look for a short DR there).

The question is whether there is a better policy than the one in use (the number of pairs on the inverse, with ARM or the corner case for some cases) that a solver can still run in a few seconds. Every policy is graded by what it misses: how much it switches, and which share of the cases with a DR in 4 or less, in 5 and in 6 it does not switch, because a missed 4-mover costs more than a missed 5-mover and both cost more than a wasted switch. The answer is a switch card per DRM: pairs first, then one more look that depends on the pair count. On 4c4e, 4c2e, 3c2e and 7c8e together it switches a little less than the pairs rule and misses less at every length. ARM, the fast read, is asked for on every 1-pair 4c4e case; the slower reads (the corners, the side pairs) on a minority. Most of each card is reads the server already had (caycala, Evan, Fanti, wen, Daichi, Jay, rodneykinney), credited where they are used. The study also judges the half-turns-to-two-bars count (the main rule of the page's earlier version) as a switch test, lists what did not help, and gives the ceilings: how far any rule on the quick reads could go.

It builds on rodneykinney's *DRM Subsets Meta*, *DRM Subsets*, *DR - 4c4e Theory*, *Domino Setup Theory* and *DRM corner variant+pair stats*, Louis's *DRM/ARM average optimals*, Cale's *DR setup stats*, Evan's *arm/pairs*, Fanti's rule sets, and the rules and reads of tseitsei89, wen, Jay, Daichi, caycala, Yura Riabov, bpaul, Radek B, compLex and Zagros.

| Where | What |
|---|---|
| [report/WRITEUP.md](report/WRITEUP.md) | the write-up |
| [report/EXAMPLES.md](report/EXAMPLES.md) | worked examples: 201 real attempts from uniform scrambles, with what you see before switching, the reads, the card's verdict next to the pairs rule's and the optimal DR after the switch, folded away |
| [report/BUGS.md](report/BUGS.md) | errata: the one statement from the server that the numbers go against, with an example |
| `research/v2/` | this version's analysis (below) |
| `research/src/`, `research/eoswtools/` | the earlier version's code, still used: the BFS over all 1,082,565 EO-solved cases, the features defined from stickers, the server's rules as code (`rules.py`), the real attempts, the two-ring model behind the half-turn count |
| `report/data/`, `research/out/SUMMARY.md` | tables of the earlier version (the ring pictures and the half-turn count among them), kept because section 7 of the write-up and parts E and F of the Lean project refer to that count |
| `lean/EOSwitch/` | Lean certificate: its own BFS over all cases, the features from stickers, and (part G) every group of every card and every current policy recounted, by DR length |

## The v2 analysis (`research/v2/`)

| File | What it does |
|---|---|
| `lib.py` | the yardstick: the prices of a miss, the grade of a policy (switched, missed 4-or-less / 5 / 6, cost per case), the best rule on a set of reads |
| `feat2.py` | extra reads per case (where the pairs are, the holes, the layers, …) → `out/feat2.npz` |
| `cards.py` | **the cards** (`CARDS`) and the current policies they are compared with (`BASE`); `python cards.py` prints every card with its exact numbers |
| `induce.py`, `tree.py`, `fastsearch.py`, `linfit.py`, `relfeat.py` | the searches: greedy rule lists, small trees, the best rule per set of reads, weighted sums, every relation between two bad pieces |
| `nextrows.py` | after the 4c4e card: the best single rows left to add when the pair trace and ARM are read on every case and the slower reads are priced by how often they are needed → `out/nextrows.json` |
| `trace2.py` | every read done on the normal side by colour, checked against the inverse on random cubes → `out/checks_trace2.tsv` |
| `results.py` | everything the report prints → `out/results.json` |
| `witness2.py` | the example cases of the write-up, replayed → `out/witness2.json` |
| `xexamples2.py` | the examples page |
| `report/` | the write-up's text (`writeup.md`), its numbers and tables (`env2.py`), the builder (`assemble2.py`), the decision-cards entry (`decision_card.py`) |

## Rebuilding

    source /data/fmc/env.sh
    cd eo-switch/research/v2
    python feat2.py && python cards.py          # needs ../out/big (run ../run_all.sh first: about six minutes)
    python trace2.py 5000                       # the reads on normal, 65,000 random cubes
    python results.py && python witness2.py && python nextrows.py
    python xexamples2.py                        # report/EXAMPLES.md
    python report/assemble2.py                  # report/WRITEUP.md
    python report/decision_card.py              # the switch card of cards/decision-cards.md
    python ../src/report_build/check_quotes.py report/writeup.md

Large outputs (`research/out/big/`, `research/v2/out/*.npz`, `*.npy`) are not in the repository. The reading notes, the register of what was said and the Discord export are not in the repository either; the quote check needs them.
