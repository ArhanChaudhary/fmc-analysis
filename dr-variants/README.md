# Pruning the search for a DR solution

A study of this repository: which HTRs are worth finishing when you look for a leave-slice solution from a DR within a goal (12 from a 2qt DR, 13 from a 3qt, 14 from a 4qt).

The rule bound of Rodney Kinney's Advanced DR Bounding removes 96–97% of the HTRs in reach of the goal and never a within-goal one. A pair count at HTR does the same job again: with n moves left for the finish an HTR needs at least 16 − 4n true corner-edge pairs, which is proved in Lean. Together they leave a few dozen HTRs per DR out of thousands. The study also gives the order to finish them in (most pairs first), what pairs say at 2qt, at 1qt and at HTR, which skeleton to start with, what NISS adds, and when to abandon a DR, all in precision and recall terms.

It builds on Levi Gibson's DR Bounding, Rodney Kinney's Advanced DR Bounding (doc and sheet, with Lorenzo Mauro's optimal algs for the 216 cases) and DRM Subsets, Levi Gibson's Pairs in DR sheet, and the exact table of [Judging a DR by hand](../judging-a-dr/).

| Where | What |
|---|---|
| [report/WRITEUP.md](report/WRITEUP.md) | the write-up ([on the site](https://fmc.arhan.sh/dr-variants/)) |
| `research/drvar/` | the search tool, in Rust |
| `research/meta/` | the analysis scripts and the page builder |
| `research/data/cases216.tsv` | the 216 NISS@1qt cases of the sheet as HTR states, with the rule's value for each (written by `research/gen_labels.py`) |
| `research/out/meta/` | the result tables the page is built from |
| `lean/PairFloor/` | the Lean project: the pair floor |

There is no errata page: nothing checked here turned out wrong.

## The tool (`research/drvar`)

`drvar` needs two tables of [Judging a DR by hand](../judging-a-dr/) that are not in the repository: the exact optimal finish of every DR state (`judging-a-dr/research/data/lean_exact_table.u8`, 1.3 GB) and the leave-slice depths (`ls_depth.u8`). That study's README says how to rebuild them.

| Command | What it does |
|---|---|
| `drvar metarun N SEED M OUT niss` | every HTR in reach of the goal on both sides for N random M-qt DRs: one 40-byte record per HTR (`OUT.rec`) and one line per DR (`OUT.tsv`) |
| `drvar metaniss N SEED M OUT.tsv` | the mid-skeleton NISS candidates of the same DRs |
| `drvar metacheck N SEED M` | the cross-check: a second search pruned with the exact leave-slice table must find the same within-goal HTRs |
| `drvar metax "SCRAMBLE"` | every HTR of one DR, one line each, with the within-goal solutions a NISS finds |
| `drvar metabase N SEED` | optimal leave-slice length by quarter-turn count over N random DR states |
| `drvar metacases` | the 216 cases: the rule's value against the finishes of each case's 3,072 states |
| `drvar metahtrpairs` | pairs against the finish over all 663,552 HTR states |
| `drvar metawit` | the HTR-state examples printed on the page |

The module is `src/meta.rs`. The other subcommands of `drvar` (`crisp`, `crisp3`, `lsb`, `diag` and the rest of `main.rs`) are from an earlier check of the doc's zero-bad-slice strategy and are not used by this page; `diag` needs a file that is not in the repository.

## The analysis (`research/meta`)

| File | What it does |
|---|---|
| `load.py`, `common.py` | the record format, the per-HTR table with S+T, slack and M, the order evaluation (expected finishes to the first within-goal HTR, ties handled exactly) |
| `check.py` | the bounds are ordered, and the best HTR of each side equals the DR's optimal leave-slice length |
| `compute.py M` | the funnel, the levels, the card, pairs along the route, skeletons, abandon signals → `out/meta/resM.json` |
| `compute2.py M` | mutual info by level, bad slices, the staged meta → `out/meta/resMb.json` |
| `niss.py M` | what NISS adds and costs → `out/meta/nissM.json` |
| `orders.py` | the orders of finishing at a fixed reach → `out/meta/orders.json` |
| `pick.py M` | candidate example DRs |
| `exview.py`, `exmd.py` | one DR the way the page shows it; every printed solution is replayed on an independent sticker model |
| `mkreport.py` | writes `report/WRITEUP.md`; every number on the page is read from the result tables |

## Rebuilding

    source /data/fmc/env.sh
    cd dr-variants/research/drvar && cargo build --release && cd ../meta
    D=../drvar/target/release/drvar
    for m in 2 3 4; do
      $D metarun 2000 $((20261117+m)) $m ../out/meta/run$m niss      # 2.6 GB of records in all
      $D metaniss 2000 $((20261117+m)) $m ../out/meta/niss$m.tsv
      $D metacheck 150 4711 $m
    done
    $D metabase 20000000 777 > ../out/meta/base.tsv
    $D metacases > ../out/meta/cases.tsv
    $D metahtrpairs > ../out/meta/htrpairs.tsv
    python check.py
    for m in 2 3 4; do python compute.py $m; python compute2.py $m; python niss.py $m; done
    python orders.py
    python mkreport.py
    cd ../../lean/PairFloor && lake build      # about half a minute once DRBound.Cube is built

The records (`out/meta/run*.rec`, `run*.tsv`, `niss*.tsv`) are not in the repository. The links to Discord messages and the 216 cases come from the knowledge base, which is not in the repository either.
