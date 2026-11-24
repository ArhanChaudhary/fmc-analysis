# Pruning the search for a DR solution

A study of this repository: which HTRs are worth finishing when you look for a leave-slice solution from a DR within a goal (12 from a 2qt DR, 13 from a 3qt, 14 from a 4qt).

The rule bound of Rodney Kinney's Advanced DR Bounding removes 96–97% of the HTRs in reach of the goal and never a within-goal one. A pair count at HTR does the same job again: with n moves left for the finish an HTR needs at least 16 − 4n true corner-edge pairs, which is proved in Lean. Together they leave a few dozen HTRs per DR out of thousands. The study also gives the order to finish them in (most pairs first), what pairs say at 2qt, at 1qt and at HTR, what HTR-equivalent pairs (true pairs and pseudo-pairs) say with 2 and 3 quarter turns left on normal and on inverse, which skeleton to start with, what NISS adds, and when to abandon a DR, all in precision and recall terms.

It builds on Levi Gibson's DR Bounding, Rodney Kinney's Advanced DR Bounding (doc and sheet, with Lorenzo Mauro's optimal algs for the 216 cases) and DRM Subsets, Levi Gibson's Pairs in DR sheet, and the exact table of [Judging a DR by hand](../judging-a-dr/).

| Where | What |
|---|---|
| [report/WRITEUP.md](report/WRITEUP.md) | the write-up ([on the site](https://fmc.arhan.sh/dr-variants/)) |
| `research/drvar/` | the search tool, in Rust |
| `research/meta/` | the analysis scripts and the page builder |
| `research/data/cases216.tsv` | the 216 NISS@1qt cases of the sheet as HTR states, with the rule's value for each (written by `research/gen_labels.py`) |
| `research/out/meta/` | the result tables the page is built from |
| `lean/PairFloor/` | the Lean project: the pair floor, and the floor on moves to HTR by HTR-equivalent pairs |

There is no errata page: nothing checked here turned out wrong.

## The tool (`research/drvar`)

`drvar` needs two tables of [Judging a DR by hand](../judging-a-dr/) that are not in the repository: the exact optimal finish of every DR state (`judging-a-dr/research/data/lean_exact_table.u8`, 1.3 GB) and the leave-slice depths (`ls_depth.u8`). That study's README says how to rebuild them.

| Command | What it does |
|---|---|
| `drvar metarun N SEED M OUT niss` | every HTR in reach of the goal on both sides for N random M-qt DRs: one 40-byte record per HTR (`OUT.rec`), a second 32-byte record with what can be read 1, 2 and 3 quarter turns before it (`OUT.ext`), and one line per DR (`OUT.tsv`) |
| `drvar metastates N SEED M OUT` | for the same DRs, every state with 2 or 3 quarter turns left on a route with at most 1 extra move so far: pairs, HTR-equivalent pairs on the state and on its inverse, fewest moves to HTR on both sides, subset |
| `drvar metahtable` | HTR-equivalent pairs against the fewest moves to HTR, exactly, over all 29,400 classes of DR states |
| `drvar metahcheck N SEED` | checks of the HTR-equivalent pair count on all HTR states and on N random DR states |
| `drvar metaniss N SEED M OUT.tsv` | the mid-skeleton NISS candidates of the same DRs |
| `drvar metacheck N SEED M` | the cross-check: a second search pruned with the exact leave-slice table must find the same within-goal HTRs |
| `drvar metax "SCRAMBLE"` | every HTR of one DR, one line each, with the within-goal solutions a NISS finds |
| `drvar metabase N SEED` | optimal leave-slice length by quarter-turn count over N random DR states |
| `drvar metacases` | the 216 cases: the rule's value against the finishes of each case's 3,072 states |
| `drvar metahtrpairs` | pairs against the finish over all 663,552 HTR states |
| `drvar metawit` | the HTR-state examples printed on the page |

A route stops at the first HTR it reaches (an HTR up to a turn of both layers together): what follows it is that HTR's finish, not a new HTR.

The module is `src/meta.rs`. The other subcommands of `drvar` (`crisp`, `crisp3`, `lsb`, `diag` and the rest of `main.rs`) are from an earlier check of the doc's zero-bad-slice strategy and are not used by this page; `diag` needs a file that is not in the repository.

## The analysis (`research/meta`)

| File | What it does |
|---|---|
| `load.py`, `common.py` | the record format, the per-HTR table with S+T, slack and M, the order evaluation (expected finishes to the first within-goal HTR, ties handled exactly) |
| `check.py` | the bounds are ordered, and the best HTR of each side equals the DR's optimal leave-slice length |
| `compute.py M` | the funnel, the levels, the card, pairs along the route, skeletons, abandon signals → `out/meta/resM.json` |
| `compute2.py M` | mutual info by level, bad slices, the staged meta → `out/meta/resMb.json` |
| `niss.py M` | what NISS adds and costs → `out/meta/nissM.json` |
| `orders.py` | the orders of finishing at a fixed reach, with the pairs-aware baseline → `out/meta/orders.json` |
| `pairs.py M` | pairs before HTR: true pairs at 2qt once the rule is passed, HTR-equivalent pairs with 2 and 3 quarter turns left on both sides → `out/meta/pairsM.json` |
| `pairtabs.py` | the tables of those two sections, for `mkreport.py` |
| `pick.py M` | candidate example DRs |
| `exview.py`, `exmd.py` | one DR the way the page shows it; every printed solution is replayed on an independent sticker model, and the pair counts are read off its stickers as a check |
| `mkreport.py` | writes `report/WRITEUP.md`; every number on the page is read from the result tables |

## Rebuilding

    source /data/fmc/env.sh
    cd dr-variants/research/drvar && cargo build --release && cd ../meta
    D=../drvar/target/release/drvar
    for m in 2 3 4; do
      $D metarun 2000 $((20261117+m)) $m ../out/meta/run$m niss      # 4.4 GB of records in all
      $D metastates 2000 $((20261117+m)) $m ../out/meta/states$m.bin
      $D metaniss 2000 $((20261117+m)) $m ../out/meta/niss$m.tsv
      $D metacheck 150 4711 $m > ../out/meta/metacheck$m.log
    done
    $D metabase 20000000 777 > ../out/meta/base.tsv
    $D metacases > ../out/meta/cases.tsv
    $D metahtrpairs > ../out/meta/htrpairs.tsv
    $D metahtable > ../out/meta/htable.tsv
    $D metahcheck 300000 99 > ../out/meta/hcheck.log
    python check.py > ../out/meta/check.log
    for m in 2 3 4; do python compute.py $m; python compute2.py $m; python niss.py $m; python pairs.py $m; done
    python orders.py
    python mkreport.py
    python check_quotes.py
    cd ../../lean/PairFloor && lake build      # under a minute once DRBound.Cube is built

The records (`out/meta/run*.rec`, `run*.ext`, `run*.tsv`, `states*.bin`, `niss*.tsv`) are not in the repository. The links to Discord messages and the 216 cases come from the knowledge base, which is not in the repository either.

## The skeleton/variant meta page (`skeleton-variant-meta/`)

The page [The skeleton/variant meta](../skeleton-variant-meta/report/WRITEUP.md) is written from the same samples, with every solution read against its own corner skeleton as (L; P, S, T, N), the numbers of Advanced DR Bounding (version of 23 Nov 2026).

| File | What it does |
|---|---|
| `research/drvar/src/tuple.rs` | the reading: a solution is cut at its quarter turns, each section's skeleton is the fewest half turns with the same corner action up to corner swaps, slices and the direction of the quarter turns beside it. `drvar metatuple N SEED M RULES OUT` writes one 50-byte record per HTR and runs two checks (L against the shortest corner path through the same corner cases; within-goal solutions against their inverses). The record's last two bytes are the pairs right after the variant's last insertion (true pairs and HTR-equivalent pairs in the U and D layers, on the state just before the quarter turn that closes the last section with extra moves; `annot::pairs_after_insertion`). `drvar metaread "SCRAMBLE" "SOLUTION" [inverse]` reads one solution, `drvar metax2 RULES "SCRAMBLE"` every HTR of one DR (the best path with its reading, and what the record holds: the shortest member's reading, its N and its pairs), `drvar metaskel "SCRAMBLE"` writes out the DR's skeletons, `drvar metasec` the shapes a skeleton section can have (before the first quarter turn nothing, X2, U2 X2 or X2 U2 Y2; between quarter turns nothing, X2 or X2 U2 Y2; after the last nothing, X2, X2 U2 or X2 U2 Y2). The premove pass: `drvar metarest N SEED M RULES OUT` writes, for the same DRs, one record of the same kind per HTR of the left-over DRs (a U quarter turn made first on the other side, either way, and what is left listed on skeletons with one quarter turn fewer than the DR or one more; q and the sections are the left-over skeleton's, L and the lengths count the premove; a left-over path solved at its last quarter turn is left out, since with the premove it is a solution of the skeleton two quarter turns shorter). `drvar metarest1 RULES "SCRAMBLE"` does one DR and writes out the within-goal solutions |
| `research/meta/rule_bounds_1123.py` | the doc's three bounds as an N per NISS@1qt case → `out/meta/rules_1123.tsv` |
| `research/meta/tcommon.py`, `tmeta.py` | the records as arrays; the meta as a rule (P cap, caps on partial sums, the mirror floor: `Rule.admit`), and the most-pairs step on top (`most_pairs`, `Rule.finish`): among the HTRs the rule lets through on one skeleton with the same (P, S, T, N), only the ones with the most pairs are finished |
| `research/meta/tcells.py`, `teval.py`, `topt.py`, `tpareto.py` | the cap sweep: HTRs counted by (skeleton quarter turns, spare moves, P, S, T, N, and whether they pass the most-pairs step), every rule with up to three caps scored on every corner case |
| `research/meta/torder.py` | found within K finishes in the page's order of finishing: by moves to HTR, fewest first, most pairs first among HTRs equally far, ties at random (`places`; one sort serves every rule). The skeleton-by-skeleton order of the 19 Nov page is kept for the list of changes (`first_positions`) |
| `research/meta/tgreedy.py` | finer rules (caps by spare moves, P, quarter turns, the bound's N; arbitrary cells) fitted on half of the DRs and scored on the other half → `out/meta/greedy_frontier.json` |
| `research/meta/tsplit.py` | skeletons and routes by quarter turns and by cancelling pair → `out/meta/tsplit.json` |
| `research/meta/tfinal.py M` | every per-corner-case number of the page → `out/meta/tfinal{M}.json`. `BASELINE_PAIRS` (or `SVM_BASELINE_PAIRS=0` for one run) says whether the baseline without DR Bounding takes the most-pairs step too |
| `research/meta/trule.py M` | the premove pass in its versions (no pass; the pass in place of the full search of that side, as in the doc; the pass, then the full search, as in the meta): misses, DRs lost and gained, HTRs to finish, found within K → `out/meta/trule{M}.json` |
| `research/meta/tmirror.py` | the mirror check over the whole sample and the check counts → `out/meta/mirror.json` |
| `research/meta/tex.py`, `texamples.py` | the page's examples, each replayed on an independent sticker model, with every printed pair count counted on the stickers → `out/meta/texamples.json` |
| `research/meta/mkpage_svm.py OUT.md` | writes the page |

    D=../drvar/target/release/drvar
    python rule_bounds_1123.py
    for m in 2 3 4; do $D metatuple 2000 $((20261117+m)) $m ../out/meta/rules_1123.tsv ../out/meta/tup$m.t50 100 > ../out/meta/tup$m.log; $D metarest 2000 $((20261117+m)) $m ../out/meta/rules_1123.tsv ../out/meta/rest$m.t50 > ../out/meta/rest$m.log; python tcells.py $m; done
    python topt.py 3; python tpareto.py 3
    for m in 2 3 4; do python tfinal.py $m; python trule.py $m; done
    python tsplit.py; python tgreedy.py; python tmirror.py; python texamples.py
    python mkpage_svm.py ../../../skeleton-variant-meta/report/WRITEUP.md

Three switches, read by every script of a run. `SVM_UNISS` says what the premove pass does: `add` (the default, and the page) makes the pass and then goes through every skeleton in full as well; `1` lets the pass take the place of the full search of the skeletons it comes from (the doc's NISS rule as written, which loses the solutions that go on after the skeleton's last quarter turn); `0` leaves it out. The left-over DR is gone through with the cap, the bound and a goal one lower, without step 4 (`SVM_REST_FLOOR=1` applies it), and a left-over skeleton that again ends with its last quarter turn is kept (`SVM_REST_HH=drop` leaves those out). A skeleton that starts and ends with a quarter turn gets the pass on both sides; `SVM_REST_BOTH=0` makes it on inverse only (its first quarter turn is the premove, made on normal), and `drvar metastd` reads that switch too. The other two are also read by `drvar metastd`: `SVM_PAIRS` says what the pairs do: `first` (the default, and the page) drops nothing and takes the variants with the most pairs first among those with the same (P, S, T, N); `drop` finishes only those (a variation that was looked at and not taken); `SVM_BASELINE_PAIRS=0` leaves the pairs out of the baseline without DR Bounding.

A run on part of the sample, for testing: `SVM_SUFFIX=p SVM_NDRS=200` makes every script read `tup{M}p.t50` and the first 200 DRs and write its files with the same suffix (`cells{M}p.npz`, `tfinal{M}p.json`, ...).

### HTR search order and limits

The report next to the page (`skeleton-variant-meta/report/ORDER-AND-LIMITS.md`, `STANDARD-META.md` until 24 Nov): how many HTRs to check on a skeleton before moving on, which HTRs to check, and when to NISS, with nothing that needs a lower bound for N. Its notation: E = P+S+T, the extra moves, and H = the moves at which HTR is reached (the moves made before a NISS counted, a skeleton's moves after its last quarter turn not). Always enforced: H ≤ G−1 (`tcommon.py` `HCAP`, on by default: the records that are G moves away are dropped when a file is read; `SVM_HCAP=0` or `T(..., hcap=False)` keeps them) and at most 1 extra move before 2qt.

| File | What it does |
|---|---|
| `research/meta/tlimits.py` | the three sections, all counted on the list below. Section 1, breadth vs depth: the HTRs with E ≤ 5 (normal, inverse, NISS after a single quarter turn) by H, one skeleton at a time (skeletons by L; a skeleton's NISS HTRs before its linear ones), and in two passes with 2 to 10 HTRs per skeleton in the first; the place of the first solution for 50% and 95% of within-goal DRs. Section 2, length restrictions: every pair of a cap on E (3..6 or none) and a cap on H (G−5..G−1), with HTRs per DR, reach and the place of the first solution in the two-pass order (`FIRST` per skeleton). Section 3, NISS, under E ≤ 5 and H ≤ G−2: none, after 1 move, after 1-2, after 1-3; an HTR after a single quarter turn comes before the linear HTRs of its skeleton, one after a longer start after all of them and never in the first pass. Checks, DR by DR, that the list on normal and inverse is the page's records and that its premove pass is the records' → `out/meta/tlimits.json` |
| `research/meta/mklimits.py OUT.md` | writes the report |
| `research/meta/torder.py` | the orders: `places` (by HTR length) and `tier_places` (one skeleton at a time, with or without a first pass, NISS in its place) for the report; `skeleton_places`, `skeleton_places_multi` (the same on the page's records, the premove pass as skeletons of its own) and `first_positions` (the 19 Nov page's order) are kept for reference |
| `research/drvar/src/stdord.rs` | `drvar metastdlist N SEED M CAPMAX OUT.r40`: for every DR of `metatuple N SEED M`, every HTR within CAPMAX moves on normal, on inverse, or with one NISS after a start of 1 to 3 moves (a quarter turn; a half turn of a side face and a quarter turn; a turn of the U or D layer, a half turn of a side face and a quarter turn), within goal or not, 40 bytes each: way, moves before the NISS, start, moves, best total, pairs at the HTR, quarter turns, corner moves left; the path read on its own skeleton (`tuple::read_any`: L with the start counted, P, S, T, pairs right after the last insertion, the corner cases at the quarter turns after one fixed spelling of the start); and the linear skeleton of the whole solution (the path, a finish, the start undone, read on the side of the path): its length and corner cases. One HTR is a class of paths, as in the records. `STDORD_CHECK=1` checks the list against the starts on the U layer alone and that the shortest spellings of a path read the same; `STDORD_CAPS="4a2=12"` sets another cap for a corner case; `OUT` `-` prints counts by cap |

    for m in 2 3 4; do $D metastdlist 2000 $((20261117+m)) $m $((9+m)) ../out/meta/stdn$m.r40; done
    python tlimits.py; python mklimits.py OUT.md

The earlier form of this report (24 Nov, the standard meta's cap against the skeleton/variant meta's at similar numbers of HTRs, commit `d468cfd` of the draft branch) was written by `tord.py`, `tstd.py` and `mkstd.py` from `drvar metastd` (`stdcmp.rs`) and the 12-byte lists `stdl{m}.r12`. They are still in the folder and need `SVM_HCAP=0`.
