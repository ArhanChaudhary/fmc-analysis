# Implied EOs

A case study of this repository: when one EO on a scramble guarantees another one.

The known case is F B (F B), which comes with R L (R L) and U D (U D). The study lists every case where an EO of 5 moves or less (normal + inverse) implies another EO of 5 moves or less: 691 sets of scrambles, in seven kinds, all produced by one dictionary between axes. It gives the exact test for any two EOs (same two EO cases after a fixed change between axes), shows that up to 5 moves nothing but the F B R L trick is behind them, finds the other source (a superflip on both sides, from 6 moves on), and measures how often a scramble has such a pair (26.9%). It also covers the sub-6 EOs that are implied by a longer EO you would never write but can see on the cube, like F B (F U2 B) from U D (D U2 F U): one trace after F B gives every EO that starts with R L or U D on that side too, with all 230 patterns listed. Everything but the percentages is exact and proved in Lean for every scramble.

It builds on Cale's observation and proof, torchlight's axis-free orientation, fabio, wen's adding and cancelling, the derived EOs found by Jay, trig0n, Cale, Zagros, bpaul and FakeMMAP, Shota's count rule, and trig0n's request for a full list.

| Where | What |
|---|---|
| [report/WRITEUP.md](report/WRITEUP.md) | the write-up |
| [report/EXAMPLES.md](report/EXAMPLES.md) | the full list: all 691 sets, and the 230 patterns after F B, each with a random scramble that has its EOs |
| `research/` | the analysis (below) |
| `lean/ImpliedEO/` | the Lean project: the theorems for every scramble, the exhaustive check up to 5 moves, the 691 sets |

There is no errata page: every statement found on the server checks out.

## The analysis (`research/`)

| File | What it does |
|---|---|
| `eomodel.py` | the edge model from geometry: 24 stickers, face turns as rotations, EO on each axis from stickers |
| `census.py` | the EO cases of each length, the two facts everything rests on checked on random scrambles, every EO of 5 moves or less grouped by the scrambles it holds on → `out/classes5.json` |
| `families.py` | the sets up to the 48 symmetries of the cube and swapping normal with inverse → `out/families5.json` |
| `kinds.py` | which change of cases links two EOs, and how short each kind of link can be |
| `study.py` | the sets by kind, the dictionary between axes, how often (2,000,000 uniformly random edge states) → `out/study.json` |
| `beyond.py` | the first implied EOs that are not the trick (6 moves between two axes, 7 on one axis) → `out/beyond.json` |
| `longer.py` | sub-6 EOs implied by a longer EO: the counts by how short the applied side is, the 230 patterns after F B, the shape Jay and wen use, how often (1,000,000 uniformly random edge states) → `out/longer.json` |
| `claims.py` | every implication stated on the server, checked → `out/claims.json` |
| `randscr.py` | ordinary random-move scrambles for every set, each checked by turning stickers → `out/scrambles.json` |
| `report_build/` | the write-up's text (`writeup.md`), the full list (`examples.md`), numbers, tables and checked examples (`env.py`), the builder (`assemble.py`) |

## Rebuilding

    source /data/fmc/env.sh
    cd implied-eo/research
    python census.py && python families.py && python kinds.py
    python study.py 2000000 && python beyond.py && python longer.py 1000000 && python claims.py && python randscr.py
    python report_build/assemble.py
    python ../../eo-switch/research/src/report_build/check_quotes.py report_build/writeup.md
    cd ../lean/ImpliedEO && python3 gen_sets.py && lake build      # under a minute

The quote check and the links to Discord messages need the knowledge base, which is not in the repository.
