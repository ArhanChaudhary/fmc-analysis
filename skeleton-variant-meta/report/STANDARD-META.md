# The standard meta against the skeleton/variant meta

23 Nov 2026

Which within-goal solutions can each meta reach? The DRs are those of [the skeleton/variant meta page](WRITEUP.md): uniformly random 2qt, 3qt and 4qt DRs, 2,000 of each (1,960 for 2qt), with a goal of 12/13/14 moves from DR to a leave-slice finish. A DR is within-goal when it has such a solution at all.

Only reach is compared. How many HTRs the standard meta has to finish to get there is not counted, so nothing here says which meta is faster.

**The two metas**

- **Skeleton/variant**, as on the page: skeletons with the DR's quarter turns or two more, variants with P ≤ 1 and P+S+T ≤ 5, each side leaving to the other what comes earlier there (step 4), and HTRs discarded by the corner-case-aware bound.
- **Standard**: a cap on the moves to HTR. Every HTR within the cap is finished. The moves are made on normal, on inverse, or with one NISS after 1–3 moves: the first moves on one side, the rest of the way to HTR on the other. No bound, and any number of quarter turns. The moves before the NISS are:
    - 1 move: a quarter turn, as in `U`;
    - 2 moves: a half turn and a quarter turn, as in `R2 U`;
    - 3 moves, only when the first is a U or a U2 (a D or a D2 counts the same): that move, a half turn and a quarter turn, as in `U R2 U'` and `U2 R2 U`.

**Reach.** A meta reaches a solution when it finishes an HTR on it: the solution is the moves the meta makes to that HTR, plus half turns only. A solution counts once, however its half-turn stretches are written and whichever of U and D is turned.

**The cap.** The moves to HTR are counted to the HTR itself, which is the last quarter turn made; with a NISS they are the moves on both sides. The cap looked at closely is median L + 2, where median L is the median, over the corner case's DRs, of the DR's shortest skeleton on either side. That is 8 for 4b2, 10 for 4a2, 9 for 2c3, 11 for 4c3, 11 for 2c4, 13 for 0c3, 12 for 0c4, 13 for 4c4. Sections 1 and 2 have every cap from 8 to 13. For 0c3 that is the goal itself, so no cap at all.

## Short version

- **Where median L + 2 is the usual 8 or 9 (4b2 and 2c3), the standard meta reaches less.** It has a within-goal solution in reach on 80.8% and 88.9% of the within-goal DRs; the skeleton/variant meta on 96.0% and 96.4%. One more move of cap brings it to 94.6% and 96.4%. Against the skeleton/variant meta it gets ahead at cap 10 on 4b2, and draws level at cap 10 on 2c3.
- **On the corner cases with longer skeletons (4a2, 4c3, 2c4, 4c4), median L + 2 is 10 to 13, only 1 to 3 short of the goal, and the two are close**: 99.2% against 96.7% on 4a2, 97.8% against 98.6% on 4c3, 97.2% against 98.8% on 2c4, 100.0% against 98.5% on 4c4.
- **By the moves before the NISS**, at median L + 2: with no NISS the standard meta reaches 66.7% on 4b2 and 75.4% on 2c3; with a NISS after 1 move 72.0% and 80.8%; after up to 2 moves 76.8% and 86.5%; after up to 3 moves 80.8% and 88.9%. Over the corner cases with 100 or more within-goal DRs, the first move before the NISS is worth 3.6 to 7.3 points, the second 0.0 to 5.7 and the third 0.0 to 4.0.
- **The NISS after 3 moves** brings 987 more solutions inside the cap, next to the 16,423 the standard meta reaches without it, and a within-goal solution on 84 more DRs. 630 of the 987 have a start like `U R2 U'`, 317 one like `U2 R2 U`, and 40 one of each, on the two sides.
- **What only the skeleton/variant meta reaches** (3,289 solutions, against 14,371 both reach): solutions whose HTR comes after the cap whichever way the standard meta goes. For 75% of them it comes one move after. 56% of them are on skeletons with two more quarter turns than the DR, which are the longer ones.
- **What only the standard meta reaches** (3,039 solutions): 67% of them need a NISS (1,354 after 1 move, 485 after 2, 200 after 3). With a NISS, the stretch of half turns that finishes the HTR sits between two quarter turns of the solution, and the skeleton/variant meta reads it as extra moves before HTR. 48% of the 3,039 have P+S+T ≥ 6 on the side that comes closer and 51% have P ≥ 2; the bound discards 1%, and 3 are on a skeleton with more than two extra quarter turns.

## 1. Within-goal DRs with a solution in reach

Each cell is the share of the corner case's within-goal DRs on which the meta reaches at least one within-goal solution. The standard meta, with the NISS after up to 3 moves, is shown at caps 8 to 13, with the cap of median L + 2 in bold.

| Corner case | Within-goal DRs | Median L | Skeleton/variant | Standard, cap 8 | Standard, cap 9 | Standard, cap 10 | Standard, cap 11 | Standard, cap 12 | Standard, cap 13 |
|---|---|---|---|---|---|---|---|---|---|
| 4b2 | 953 | 6 | 96.0% | **80.8%** | 94.6% | 100.0% | 100.0% | 100.0% | 100.0% |
| 4a2 | 120 | 8 | 96.7% | 80.8% | 92.5% | **99.2%** | 100.0% | 100.0% | 100.0% |
| 2c3 | 901 | 7 | 96.4% | 74.3% | **88.9%** | 96.4% | 100.0% | 100.0% | 100.0% |
| 4c3 | 511 | 9 | 98.6% | 50.1% | 74.4% | 89.4% | **97.8%** | 100.0% | 100.0% |
| 2c4 | 1,123 | 9 | 98.8% | 40.2% | 69.9% | 90.9% | **97.2%** | 99.6% | 100.0% |
| 0c3 | 15 | 11 | 93.3% | 33.3% | 93.3% | 93.3% | 93.3% | 100.0% | **100.0%** |
| 0c4 | 66 | 10 | 100.0% | 24.2% | 48.5% | 72.7% | 86.4% | **100.0%** | 100.0% |
| 4c4 | 397 | 11 | 98.5% | 13.9% | 23.7% | 46.6% | 71.5% | 97.0% | **100.0%** |

A cap at or over the goal (12 for 4b2 and 4a2, 13 for 2c3, 4c3 and 0c3) is the same as no cap. 0c3 and 0c4 have 15 and 66 within-goal DRs, so their percentages are coarse.

## 2. By the moves before the NISS

The standard meta at median L + 2, with the NISS allowed after more and more moves. Each cell is the share of within-goal DRs with a within-goal solution in reach; each column includes the ones to its left.

| Corner case | Cap | No NISS | NISS after 1 move | NISS after up to 2 moves | NISS after up to 3 moves | Skeleton/variant |
|---|---|---|---|---|---|---|
| 4b2 | 8 | 66.7% | 72.0% | 76.8% | 80.8% | 96.0% |
| 4a2 | 10 | 91.7% | 96.7% | 98.3% | 99.2% | 96.7% |
| 2c3 | 9 | 75.4% | 80.8% | 86.5% | 88.9% | 96.4% |
| 4c3 | 11 | 88.6% | 93.0% | 96.7% | 97.8% | 98.6% |
| 2c4 | 11 | 88.7% | 92.3% | 95.7% | 97.2% | 98.8% |
| 0c3 | 13 | 100.0% | 100.0% | 100.0% | 100.0% | 93.3% |
| 0c4 | 12 | 89.4% | 98.5% | 100.0% | 100.0% | 100.0% |
| 4c4 | 13 | 92.7% | 100.0% | 100.0% | 100.0% | 98.5% |

The same DRs counted once each, under the fewest moves before the NISS that put a within-goal solution in reach.

| Corner case | Cap | No NISS needed | Needs a NISS after 1 move | Needs a NISS after 2 moves | Needs a NISS after 3 moves | Not in reach |
|---|---|---|---|---|---|---|
| 4b2 | 8 | 636 | 50 | 46 | 38 | 183 |
| 4a2 | 10 | 110 | 6 | 2 | 1 | 1 |
| 2c3 | 9 | 679 | 49 | 51 | 22 | 100 |
| 4c3 | 11 | 453 | 22 | 19 | 6 | 11 |
| 2c4 | 11 | 996 | 40 | 39 | 17 | 31 |
| 0c3 | 13 | 15 | 0 | 0 | 0 | 0 |
| 0c4 | 12 | 59 | 6 | 1 | 0 | 0 |
| 4c4 | 13 | 368 | 29 | 0 | 0 | 0 |

The shares at every cap from 8 to 13, with the cap of median L + 2 in bold.

| Corner case | Moves before the NISS | Cap 8 | Cap 9 | Cap 10 | Cap 11 | Cap 12 | Cap 13 |
|---|---|---|---|---|---|---|---|
| 4b2 | none | **66.7%** | 81.7% | 92.5% | 98.8% | 100.0% | 100.0% |
| 4b2 | up to 1 | **72.0%** | 88.4% | 97.6% | 100.0% | 100.0% | 100.0% |
| 4b2 | up to 2 | **76.8%** | 92.4% | 99.7% | 100.0% | 100.0% | 100.0% |
| 4b2 | up to 3 | **80.8%** | 94.6% | 100.0% | 100.0% | 100.0% | 100.0% |
| 4a2 | none | 65.8% | 81.7% | **91.7%** | 96.7% | 100.0% | 100.0% |
| 4a2 | up to 1 | 70.8% | 87.5% | **96.7%** | 100.0% | 100.0% | 100.0% |
| 4a2 | up to 2 | 80.0% | 90.8% | **98.3%** | 100.0% | 100.0% | 100.0% |
| 4a2 | up to 3 | 80.8% | 92.5% | **99.2%** | 100.0% | 100.0% | 100.0% |
| 2c3 | none | 54.9% | **75.4%** | 88.0% | 96.0% | 99.2% | 100.0% |
| 2c3 | up to 1 | 63.6% | **80.8%** | 91.7% | 98.1% | 100.0% | 100.0% |
| 2c3 | up to 2 | 70.7% | **86.5%** | 95.0% | 99.7% | 100.0% | 100.0% |
| 2c3 | up to 3 | 74.3% | **88.9%** | 96.4% | 100.0% | 100.0% | 100.0% |
| 4c3 | none | 18.8% | 44.0% | 71.0% | **88.6%** | 97.8% | 100.0% |
| 4c3 | up to 1 | 32.3% | 56.6% | 79.1% | **93.0%** | 100.0% | 100.0% |
| 4c3 | up to 2 | 42.9% | 67.9% | 85.7% | **96.7%** | 100.0% | 100.0% |
| 4c3 | up to 3 | 50.1% | 74.4% | 89.4% | **97.8%** | 100.0% | 100.0% |
| 2c4 | none | 18.9% | 44.0% | 71.4% | **88.7%** | 96.3% | 99.3% |
| 2c4 | up to 1 | 27.3% | 55.0% | 79.2% | **92.3%** | 98.6% | 100.0% |
| 2c4 | up to 2 | 36.4% | 65.2% | 87.5% | **95.7%** | 99.5% | 100.0% |
| 2c4 | up to 3 | 40.2% | 69.9% | 90.9% | **97.2%** | 99.6% | 100.0% |
| 0c3 | none | 0.0% | 6.7% | 20.0% | 53.3% | 86.7% | **100.0%** |
| 0c3 | up to 1 | 33.3% | 66.7% | 66.7% | 80.0% | 100.0% | **100.0%** |
| 0c3 | up to 2 | 33.3% | 93.3% | 93.3% | 93.3% | 100.0% | **100.0%** |
| 0c3 | up to 3 | 33.3% | 93.3% | 93.3% | 93.3% | 100.0% | **100.0%** |
| 0c4 | none | 0.0% | 7.6% | 39.4% | 62.1% | **89.4%** | 100.0% |
| 0c4 | up to 1 | 4.5% | 18.2% | 51.5% | 77.3% | **98.5%** | 100.0% |
| 0c4 | up to 2 | 4.5% | 18.2% | 53.0% | 81.8% | **100.0%** | 100.0% |
| 0c4 | up to 3 | 24.2% | 48.5% | 72.7% | 86.4% | **100.0%** | 100.0% |
| 4c4 | none | 0.0% | 3.3% | 16.9% | 40.6% | 70.0% | **92.7%** |
| 4c4 | up to 1 | 2.0% | 7.1% | 30.0% | 57.4% | 87.2% | **100.0%** |
| 4c4 | up to 2 | 2.0% | 8.8% | 35.5% | 64.7% | 95.2% | **100.0%** |
| 4c4 | up to 3 | 13.9% | 23.7% | 46.6% | 71.5% | 97.0% | **100.0%** |

## 3. The same DRs under both metas

Within-goal DRs by which meta has a within-goal solution in reach, with the standard meta at median L + 2 and the NISS after up to that many moves.

| Corner case | Cap | Moves before the NISS | Both | Only skeleton/variant | Only standard | Neither |
|---|---|---|---|---|---|---|
| 4b2 | 8 | none | 634 | 281 | 2 | 36 |
| 4b2 | 8 | up to 1 | 676 | 239 | 10 | 28 |
| 4b2 | 8 | up to 2 | 717 | 198 | 15 | 23 |
| 4b2 | 8 | up to 3 | 753 | 162 | 17 | 21 |
| 4a2 | 10 | none | 110 | 6 | 0 | 4 |
| 4a2 | 10 | up to 1 | 114 | 2 | 2 | 2 |
| 4a2 | 10 | up to 2 | 116 | 0 | 2 | 2 |
| 4a2 | 10 | up to 3 | 116 | 0 | 3 | 1 |
| 2c3 | 9 | none | 671 | 198 | 8 | 24 |
| 2c3 | 9 | up to 1 | 712 | 157 | 16 | 16 |
| 2c3 | 9 | up to 2 | 759 | 110 | 20 | 12 |
| 2c3 | 9 | up to 3 | 777 | 92 | 24 | 8 |
| 4c3 | 11 | none | 448 | 56 | 5 | 2 |
| 4c3 | 11 | up to 1 | 469 | 35 | 6 | 1 |
| 4c3 | 11 | up to 2 | 488 | 16 | 6 | 1 |
| 4c3 | 11 | up to 3 | 494 | 10 | 6 | 1 |
| 2c4 | 11 | none | 993 | 117 | 3 | 10 |
| 2c4 | 11 | up to 1 | 1,028 | 82 | 8 | 5 |
| 2c4 | 11 | up to 2 | 1,066 | 44 | 9 | 4 |
| 2c4 | 11 | up to 3 | 1,081 | 29 | 11 | 2 |
| 0c3 | 13 | none | 14 | 0 | 1 | 0 |
| 0c3 | 13 | up to 1 | 14 | 0 | 1 | 0 |
| 0c3 | 13 | up to 2 | 14 | 0 | 1 | 0 |
| 0c3 | 13 | up to 3 | 14 | 0 | 1 | 0 |
| 0c4 | 12 | none | 59 | 7 | 0 | 0 |
| 0c4 | 12 | up to 1 | 65 | 1 | 0 | 0 |
| 0c4 | 12 | up to 2 | 66 | 0 | 0 | 0 |
| 0c4 | 12 | up to 3 | 66 | 0 | 0 | 0 |
| 4c4 | 13 | none | 364 | 27 | 4 | 2 |
| 4c4 | 13 | up to 1 | 391 | 0 | 6 | 0 |
| 4c4 | 13 | up to 2 | 391 | 0 | 6 | 0 |
| 4c4 | 13 | up to 3 | 391 | 0 | 6 | 0 |

## 4. Solutions only one meta reaches

Within-goal solutions over all the within-goal DRs of the corner case, with the standard meta at median L + 2 and the NISS after up to 3 moves.

| Corner case | Cap | Both reach | Only skeleton/variant | Only standard |
|---|---|---|---|---|
| 4b2 | 8 | 1,844 | 653 | 223 |
| 4a2 | 10 | 319 | 0 | 8 |
| 2c3 | 9 | 2,852 | 1,298 | 745 |
| 4c3 | 11 | 1,612 | 30 | 117 |
| 2c4 | 11 | 6,165 | 1,303 | 1,847 |
| 0c3 | 13 | 36 | 0 | 1 |
| 0c4 | 12 | 340 | 5 | 38 |
| 4c4 | 13 | 1,203 | 0 | 60 |

The solutions the standard meta reaches (the "both" and "only standard" columns together), each under the fewest moves before the NISS that bring its HTR inside the cap.

| Corner case | Cap | No NISS needed | Needs a NISS after 1 move | Needs a NISS after 2 moves | Needs a NISS after 3 moves |
|---|---|---|---|---|---|
| 4b2 | 8 | 1,499 | 232 | 194 | 142 |
| 4a2 | 10 | 294 | 20 | 11 | 2 |
| 2c3 | 9 | 2,338 | 524 | 494 | 241 |
| 4c3 | 11 | 1,336 | 268 | 85 | 40 |
| 2c4 | 11 | 4,507 | 1,759 | 1,203 | 543 |
| 0c3 | 13 | 37 | 0 | 0 | 0 |
| 0c4 | 12 | 250 | 88 | 21 | 19 |
| 4c4 | 13 | 1,076 | 187 | 0 | 0 |

The same for the "only standard" solutions alone.

| Corner case | Cap | No NISS needed | Needs a NISS after 1 move | Needs a NISS after 2 moves | Needs a NISS after 3 moves |
|---|---|---|---|---|---|
| 4b2 | 8 | 14 | 144 | 53 | 12 |
| 4a2 | 10 | 2 | 5 | 0 | 1 |
| 2c3 | 9 | 249 | 294 | 142 | 60 |
| 4c3 | 11 | 39 | 70 | 1 | 7 |
| 2c4 | 11 | 648 | 797 | 289 | 113 |
| 0c3 | 13 | 1 | 0 | 0 | 0 |
| 0c4 | 12 | 13 | 18 | 0 | 7 |
| 4c4 | 13 | 34 | 26 | 0 | 0 |

Of the 987 solutions that need the NISS after 3 moves, 630 have a start like `U R2 U'`, 317 one like `U2 R2 U`, and 40 one of each, on the two sides. Of the 200 among them that only the standard meta reaches, it is 156, 28 and 16.

**Why the standard meta doesn't reach the "only skeleton/variant" solutions.** Their HTR comes after the cap in every way the standard meta has: on normal, on inverse, and with a NISS after 1, 2 or 3 moves on either side. The table has the fewest moves over the cap.

| Corner case | Cap | 1 move over | 2 moves over | 3 or more over |
|---|---|---|---|---|
| 4b2 | 8 | 454 | 190 | 9 |
| 4a2 | 10 | 0 | 0 | 0 |
| 2c3 | 9 | 798 | 452 | 48 |
| 4c3 | 11 | 30 | 0 | 0 |
| 2c4 | 11 | 1,181 | 122 | 0 |
| 0c3 | 13 | 0 | 0 | 0 |
| 0c4 | 12 | 5 | 0 | 0 |
| 4c4 | 13 | 0 | 0 | 0 |

**Why the skeleton/variant meta doesn't reach the "only standard" solutions.** Each solution is filed under what stops it on the side that comes closer.

| Corner case | P+S+T ≥ 6 | P ≥ 2 | Skeleton with more than two extra quarter turns | Discarded by the bound | Other |
|---|---|---|---|---|---|
| 4b2 | 183 | 35 | 0 | 5 | 0 |
| 4a2 | 4 | 0 | 2 | 2 | 0 |
| 2c3 | 485 | 248 | 0 | 12 | 0 |
| 4c3 | 61 | 56 | 0 | 0 | 0 |
| 2c4 | 717 | 1,113 | 0 | 17 | 0 |
| 0c3 | 0 | 0 | 1 | 0 | 0 |
| 0c4 | 0 | 38 | 0 | 0 | 0 |
| 4c4 | 0 | 58 | 0 | 2 | 0 |

The same over all corner cases, by the fewest moves before the NISS that the solution needs.

| Moves before the NISS | P+S+T ≥ 6 | P ≥ 2 | Skeleton with more than two extra quarter turns | Discarded by the bound | Other |
|---|---|---|---|---|---|
| No NISS needed | 0 | 961 | 1 | 38 | 0 |
| NISS after 1 move | 917 | 436 | 1 | 0 | 0 |
| NISS after 2 moves | 373 | 112 | 0 | 0 | 0 |
| NISS after 3 moves | 160 | 39 | 1 | 0 | 0 |

The 1,000 that need no NISS are nearly all P ≥ 2 (961): two or more extra moves before 2qt, on a skeleton the standard meta gets through inside its cap. The bound discards 38 more.

The rest are NISS solutions. With a NISS, the stretch of half turns that finishes the HTR is not at the end of the solution but between two of its quarter turns: the first two (or the last two) after `U`, `R2 U` or `U2 R2 U`, and the second and third (or the third- and second-to-last) after `U R2 U'`. Read as a variant of a skeleton, that stretch is a section before HTR with about as many extra moves as the finish is long, and it stays between the same two quarter turns on inverse. On a 2qt or 3qt skeleton it is the trigger or the setup and breaks P+S+T ≤ 5. On a skeleton with four or more quarter turns it can also be a section before 2qt, where it breaks P ≤ 1.

## 5. Examples

For each corner case, solutions only one of the two metas reaches, with the standard meta at median L + 2. For the standard meta, one that needs the NISS after 3 moves comes first where there is one. Where it says so, the other meta has no within-goal solution in reach for that DR at all.

### 4b2 (goal 12, standard cap 8)

Only the skeleton/variant meta:

- DR `R2 U' F2 L2 U L2 D' U2 L2 U' L2 B2` (optimal 11). Solution `B2 L2 U L2 U' B2 U' B2 L2 D R2` (11 moves).
    - Skeleton/variant: on normal L = 9, (P, S, T, N) = (1, 0, 1, 0).
    - Standard: HTR after 10 moves on normal and 9 on inverse; with a NISS, 9 after 2 moves on inverse. The standard meta has no within-goal solution in reach for this DR.
- DR `F2 L2 U B2 U2 F2 L2 B2 U F2 D2 U2 F2` (optimal 11). Solution `F2 B2 U' F2 R2 B2 D2 B2 U' L2 F2` (11 moves).
    - Skeleton/variant: on inverse L = 4, (S, T, N) = (1, 4, 2).
    - Standard: HTR after 9 moves on normal and 9 on inverse; none of the NISS starts fits its first or last moves. The standard meta has no within-goal solution in reach for this DR.

Only the standard meta:

- DR `D R2 F2 R2 U L2 R2 F2 R2 D F2 D'` (optimal 12). Solution `U L2 U' R2 F2 R2 L2 U' R2 F2 R2 D'` (12 moves).
    - Standard: `U L2 U'` on normal, then `D R2 F2 R2 U` on inverse: HTR after 8 moves; finish `L2 R2 F2 R2`, on inverse.
    - Skeleton/variant: on normal L = 6, (P, S, T, N) = (0, 3, 3, 0): P+S+T = 6; on inverse L = 6, (P, S, T, N) = (3, 3, 0, 0): P = 3. The skeleton/variant meta has no within-goal solution in reach for this DR.
- DR `D' L2 B2 L2 R2 U' L2 D' L2 R2 D' F2` (optimal 12). Solution `F2 U F2 B2 D B2 D R2 L2 B2 L2 D` (12 moves).
    - Standard: `D'` on inverse, then `F2 U B2 F2 D B2 D` on normal: HTR after 8 moves; finish `L2 R2 B2 L2`.
    - Skeleton/variant: on normal L = 7, (P, S, T, N) = (2, 0, 3, 0): P = 2; on inverse L = 7, (P, S, T, N) = (3, 0, 2, 0): P = 3. The skeleton/variant meta has no within-goal solution in reach for this DR.

### 4a2 (goal 12, standard cap 10)

Only the skeleton/variant meta: no such solution in the sample.

Only the standard meta:

- DR `U' L2 D B2 R2 U L2 D L2 U F2 U` (optimal 12). Solution `U' F2 U' L2 U' F2 D' R2 B2 D' L2 U` (12 moves).
    - Standard: `U' L2 D` on inverse, then `U' F2 U' L2 U' F2 D'` on normal: HTR after 10 moves; finish `R2 B2`.
    - Skeleton/variant: on normal L = 11, (P, S, T, N) = (0, 1, 0, 0) and on inverse L = 11, (P, S, T, N) = (1, 0, 0, 0); its skeleton has 6 quarter turns, more than two over the DR's. The skeleton/variant meta has no within-goal solution in reach for this DR.
- DR `L2 U L2 D' U' L2 B2 D2 L2 F2 U2 R2 U'` (optimal 12). Solution `U R2 U2 F2 L2 U2 F2 R2 U2 F2 D' L2` (12 moves).
    - Standard: `U` on normal, then `L2 D` on inverse: HTR after 3 moves; finish `F2 U2 R2 F2 U2 L2 F2 U2 R2`, on inverse.
    - Skeleton/variant: L = 6, (S, T, N) = (0, 6, 0) on both sides: P+S+T = 6. The skeleton/variant meta has no within-goal solution in reach for this DR.

### 2c3 (goal 13, standard cap 9)

Only the skeleton/variant meta:

- DR `B2 L2 U L2 U2 L2 R2 U F2 L2 D' F2 R2` (optimal 12). Solution `B2 U' B2 L2 U' L2 F2 L2 F2 U' R2 B2` (12 moves).
    - Skeleton/variant: on normal L = 7, (P, S, T, N) = (0, 1, 3, 1).
    - Standard: HTR after 10 moves on normal and 11 on inverse; with a NISS, 10 after 2 moves on normal. The standard meta has no within-goal solution in reach for this DR.
- DR `U F2 U' B2 L2 U' R2 U' L2 D R2 F2` (optimal 12). Solution `F2 R2 U' F2 U B2 U F2 L2 U R2 D'` (12 moves).
    - Skeleton/variant: on normal L = 10, (P, S, T, N) = (1, 1, 0, 0).
    - Standard: HTR after 12 moves on normal and 10 on inverse; with a NISS, 11 after 1 move on inverse, 10 after 3 moves on inverse. The standard meta has no within-goal solution in reach for this DR.

Only the standard meta:

- DR `D2 L2 U' F2 R2 B2 R2 U2 L2 D' U2 B2 R2 U'` (optimal 13). Solution `U R2 B2 U' B2 U2 F2 R2 F2 L2 D L2 D2` (13 moves).
    - Standard: `D2 L2 D'` on inverse, then `U R2 B2 U'` on normal: HTR after 7 moves; finish `B2 U2 F2 R2 F2 L2`.
    - Skeleton/variant: on normal L = 7, (P, S, T, N) = (0, 1, 5, 0) and on inverse L = 7, (P, S, T, N) = (0, 5, 1, 0); P+S+T = 6. The skeleton/variant meta has no within-goal solution in reach for this DR.
- DR `D U F2 U' R2 D' F2 L2 F2 R2 D'` (optimal 10). Solution `U F2 B2 U L2 U B2 U L2 B2 L2 B2 D` (13 moves).
    - Standard: `D'` on inverse, then `U B2 F2 U L2 U B2 U` on normal: HTR after 9 moves; finish `L2 B2 L2 B2`.
    - Skeleton/variant: on normal L = 8, (P, S, T, N) = (2, 0, 3, 0): P = 2; on inverse L = 8, (P, S, T, N) = (3, 0, 2, 0): P = 3. The skeleton/variant meta reaches another solution of this DR, a 10.

### 4c3 (goal 13, standard cap 11)

Only the skeleton/variant meta:

- DR `L2 D' F2 U' B2 R2 D' F2 L2 U L2 D B2` (optimal 13). Solution `B2 U' F2 U' F2 R2 U R2 B2 U F2 D L2` (13 moves).
    - Skeleton/variant: on normal L = 11, (P, S, T, N) = (1, 1, 0, 0).
    - Standard: HTR after 12 moves on normal and 12 on inverse; with a NISS, 12 after 2 moves on normal, 12 after 2 moves on inverse. The standard meta has no within-goal solution in reach for this DR.
- DR `L2 D' F2 U' B2 F2 R2 D' L2 U L2 D' F2` (optimal 13). Solution `F2 U B2 U' B2 D F2 R2 L2 D F2 D L2` (13 moves).
    - Skeleton/variant: on normal L = 11, (P, S, T, N) = (0, 2, 0, 0).
    - Standard: HTR after 12 moves on normal and 12 on inverse; with a NISS, 12 after 2 moves on normal, 12 after 2 moves on inverse. The standard meta has no within-goal solution in reach for this DR.

Only the standard meta:

- DR `D R2 D F2 U2 F2 D L2 R2 U' L2 U R2` (optimal 13). Solution `R2 U' L2 U R2 L2 U' R2 D2 L2 U' R2 D'` (13 moves).
    - Standard: `D R2 U` on inverse, then `R2 U' L2 U L2 R2 U'` on normal: HTR after 10 moves; finish `R2 D2 L2`.
    - Skeleton/variant: L = 9, (P, S, T, N) = (2, 2, 0, 0) on both sides: P = 2. The skeleton/variant meta reaches another solution of this DR, a 13.
- DR `D2 B2 F2 D B2 D2 R2 D' R2 D L2 R2 U2` (optimal 13). Solution `U B2 R2 F2 B2 U' R2 B2 L2 F2 D2 R2 D` (13 moves).
    - Standard: `D'` on inverse, then `U B2 R2 B2 F2 U'` on normal: HTR after 7 moves; finish `R2 B2 L2 F2 D2 R2`.
    - Skeleton/variant: L = 7, (P, S, T, N) = (0, 3, 3, 0) on both sides: P+S+T = 6. The skeleton/variant meta has no within-goal solution in reach for this DR.

### 2c4 (goal 14, standard cap 11)

Only the skeleton/variant meta:

- DR `R2 U R2 D2 B2 U' L2 U' L2 U L2 U' L2 R2 D'` (optimal 14). Solution `B2 R2 U' F2 D R2 F2 R2 F2 D L2 B2 D L2` (14 moves).
    - Skeleton/variant: on normal L = 9, (P, S, T, N) = (1, 3, 1, 0).
    - Standard: HTR after 13 moves on normal and 12 on inverse; with a NISS, 12 after 2 moves on inverse. The standard meta has no within-goal solution in reach for this DR.

Only the standard meta:

- DR `U2 R2 U' L2 B2 R2 F2 U R2 D' L2 D' B2 F2` (optimal 14). Solution `F2 B2 U B2 U L2 U' B2 L2 F2 R2 U L2 D2` (14 moves).
    - Standard: `D2 L2 U'` on inverse, then `B2 F2 U B2 U L2 U'` on normal: HTR after 10 moves; finish `B2 L2 F2 R2`.
    - Skeleton/variant: on normal L = 9, (P, S, T, N) = (2, 0, 3, 0): P = 2; on inverse L = 9, (P, S, T, N) = (3, 0, 0, 2): P = 3. The skeleton/variant meta has no within-goal solution in reach for this DR.
- DR `U' R2 D2 R2 B2 R2 D B2 R2 D' F2 L2 U' B2` (optimal 14). Solution `B2 U L2 F2 U F2 R2 U' R2 B2 R2 D2 R2 U` (14 moves).
    - Standard: `U'` on inverse, then `B2 U L2 F2 U F2 R2 U'` on normal: HTR after 9 moves; finish `R2 B2 R2 D2 R2`.
    - Skeleton/variant: on normal L = 8, (P, S, T, N) = (1, 1, 4, 0): P+S+T = 6; on inverse L = 8, (P, S, T, N) = (4, 1, 1, 0): P = 4. The skeleton/variant meta has no within-goal solution in reach for this DR.

### 0c3 (goal 13, standard cap 13)

Only the skeleton/variant meta: no such solution in the sample.

Only the standard meta:

- DR `D' B2 U' F2 D B2 U F2 U' L2 U L2 U'` (optimal 13). Solution `U L2 U' L2 U F2 U' B2 U' R2 U L2 U` (13 moves).
    - Standard: `U L2 U' L2 U F2 U' B2 U' R2 U L2 U` on normal: HTR after 13 moves; nothing left to finish.
    - Skeleton/variant: L = 13, (P, S, T, N) = (0, 0, 0, 0) on both sides: its skeleton has 7 quarter turns, more than two over the DR's. The skeleton/variant meta has no within-goal solution in reach for this DR.

### 0c4 (goal 14, standard cap 12)

Only the skeleton/variant meta:

- DR `B2 U L2 U B2 F2 R2 F2 U2 B2 U' R2 U B2` (optimal 14). Solution `B2 U' R2 U B2 U2 F2 R2 F2 B2 U' L2 U' B2` (14 moves).
    - Skeleton/variant: on normal L = 11, (P, S, T, N) = (0, 3, 0, 0).
    - Standard: HTR after 13 moves on normal and 13 on inverse; with a NISS, 13 after 2 moves on normal, 13 after 2 moves on inverse. The standard meta reaches another solution of this DR, a 14.
- DR `D2 R2 U L2 D' R2 B2 D2 B2 U L2 D F2` (optimal 13). Solution `F2 U' R2 U' F2 U2 F2 R2 F2 B2 U R2 D F2` (14 moves).
    - Skeleton/variant: on normal L = 11, (P, S, T, N) = (0, 3, 0, 0).
    - Standard: HTR after 13 moves on normal and 13 on inverse; with a NISS, 13 after 2 moves on normal, 13 after 2 moves on inverse. The standard meta reaches another solution of this DR, a 13.

Only the standard meta:

- DR `B2 D2 R2 B2 U L2 D F2 L2 U2 L2 D' L2 U'` (optimal 13). Solution `U B2 U' R2 F2 U' R2 L2 D' F2 U R2 U R2` (14 moves).
    - Standard: `U B2 U'` on normal, then `R2 U' R2 U' F2 D L2 R2 U` on inverse: HTR after 12 moves; finish `F2 R2`, on inverse.
    - Skeleton/variant: on normal L = 11, (P, S, T, N) = (3, 0, 0, 0): P = 3; on inverse L = 11, (P, S, T, N) = (2, 1, 0, 0): P = 2. The skeleton/variant meta reaches another solution of this DR, a 13.
- DR `D' R2 D B2 R2 D2 L2 U' B2 D F2 U2 R2 F2` (optimal 13). Solution `B2 U R2 L2 F2 U B2 U2 R2 U' F2 U2 F2 D'` (14 moves).
    - Standard: `D` on inverse, then `B2 U L2 R2 F2 U B2 U2 R2 U'` on normal: HTR after 11 moves; finish `F2 U2 F2`.
    - Skeleton/variant: L = 10, (P, S, T, N) = (2, 0, 2, 0) on both sides: P = 2. The skeleton/variant meta reaches another solution of this DR, a 13.

### 4c4 (goal 14, standard cap 13)

Only the skeleton/variant meta: no such solution in the sample.

Only the standard meta:

- DR `D' R2 D' U2 L2 U' F2 L2 R2 D R2 U' L2 U'` (optimal 13). Solution `U L2 U R2 U' F2 B2 R2 U F2 U' R2 D` (13 moves).
    - Standard: `U L2 U R2 U' F2 B2 R2 U F2 U' R2 D` on normal: HTR after 13 moves; nothing left to finish.
    - Skeleton/variant: L = 11, (P, S, T, N) = (2, 0, 0, 0) on both sides: P = 2. The skeleton/variant meta has no within-goal solution in reach for this DR.
- DR `D' F2 U R2 U' R2 B2 L2 D F2 R2 D' R2 D'` (optimal 14). Solution `U F2 U L2 B2 U' B2 R2 F2 D R2 U' F2 D` (14 moves).
    - Standard: `U` on normal, then `D' F2 U R2 D' F2 R2 B2 U B2 L2 U'` on inverse: HTR after 13 moves; finish `F2`, on inverse.
    - Skeleton/variant: on normal L = 10, (P, S, T, N) = (4, 0, 0, 0): P = 4; on inverse L = 10, (P, S, T, N) = (3, 1, 0, 0): P = 3. The skeleton/variant meta has no within-goal solution in reach for this DR.

## How it was counted

- **Sample.** The 5,960 DRs of the page (4,086 within-goal), each searched on normal and on inverse.
- **Skeleton/variant side.** The same HTRs as the page: for every DR, the number of HTRs finished and the number of those within the goal equal the page's records.
- **Standard side.** Every way to an HTR within the goal: from the DR on normal, from the DR on inverse, and from each start on either side with the rest on the other side. The starts are a quarter turn; a half turn of a side face and a quarter turn; and a turn of the U or D layer (a quarter turn or U2/D2), a half turn of a side face and a quarter turn. A way stops at the first HTR it comes to, as on the page.
- **Other starts.** A start that ends on a half turn reaches the same HTRs as the start without that half turn, one move sooner. So does a start with U2 or D2 right before its quarter turn, since the two commute. A start with nothing but half turns reaches what the other side reaches without a NISS. `U D` or `U D'` in front is a U2 or nothing as far as a leave-slice finish goes. So no other start of up to 3 moves adds anything; as a check, every other three-move start that begins on the U or D layer was run as well on the first 128 DRs of each sample, and the best solution within every cap stayed the same on all 384 of them.
- **Finish.** The shortest half-turn finish of the HTR to a leave-slice solution, for both metas.
- **Solutions.** Section 4 counts the within-goal solutions either meta has a way to: the page's HTRs on both sides, finished or not, and the standard meta's HTRs at any cap, each with its shortest finish. Two that differ only in how a stretch of half turns is written, or in which of U and D is turned, are one solution. Whether a meta reaches a solution is then read off the solution itself: the HTRs on it are the ones before its first quarter turn (on inverse), after its last (on normal), and after a NISS start at either end.
- **Checks.** On normal and inverse, the standard meta's best solution within each cap is never worse than the best among the page's HTRs with that many moves to HTR. For every DR, every cap and every number of moves before the NISS, "the meta reaches a within-goal solution" comes out the same from the HTRs and from the list of solutions. The moves to HTR of every solution in each of the eight ways (normal, inverse, and a NISS after 1, 2 or 3 moves on either side), recounted from its stretches of half turns alone, are the tool's for 21,405 of the 21,432 solutions in sight. Of the other 27, 20 have a way that comes through an earlier HTR, where the meta stops, and 7 have a U-layer and a D-layer move side by side, as in `U D2`, which the tool counts as the one move they make for a leave-slice finish; each was checked to be one of the two. Every example is one where the two agree, and was replayed on a separate sticker model on normal and on inverse, with its (L; P, S, T, N) read again from the solution's own moves on both sides.
- **Not covered.** The work of either meta. The standard meta as a person runs it also drops HTRs by feel or by a bound; here it finishes everything within the cap, so its reach is an upper limit.
