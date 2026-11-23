# The standard meta against the skeleton/variant meta

23 Nov 2026

Which within-goal solutions can each meta reach? The DRs are those of [the skeleton/variant meta page](WRITEUP.md): uniformly random 2qt, 3qt and 4qt DRs, 2,000 of each (1,960 for 2qt), with a goal of 12/13/14 moves from DR to a leave-slice finish. A DR is within-goal when it has such a solution at all.

Only reach is compared. How many HTRs the standard meta has to finish to get there is not counted, so nothing here says which meta is faster.

**The two metas**

- **Skeleton/variant**, as on the page: skeletons with the DR's quarter turns or two more, variants with P ≤ 1 and P+S+T ≤ 5, each side leaving to the other what comes earlier there (step 4), and HTRs discarded by the corner-case-aware bound.
- **Standard**: a cap on the moves to HTR. Every HTR within the cap is finished. The moves are made on normal, on inverse, or with one NISS after 1–2 moves: a quarter turn, alone or with one half turn before it, on one side, and the rest of the way to HTR on the other. No bound, and any number of quarter turns.

**Reach.** A meta reaches a solution when it finishes an HTR on it: the solution is the moves the meta makes to that HTR, plus half turns only. A solution counts once, however its half-turn stretches are written and whichever of U and D is turned.

**The cap.** The cap looked at closely is median L + 2, where median L is the median, over the corner case's DRs, of the DR's shortest skeleton on either side. That is 8 for 4b2, 10 for 4a2, 9 for 2c3, 11 for 4c3, 11 for 2c4, 13 for 0c3, 12 for 0c4, 13 for 4c4. The first table has every cap from 8 to 13. For 0c3 that is the goal itself, so no cap at all.

The moves to HTR are counted to the HTR itself, which is the last quarter turn made. L+P+S+T is that plus the skeleton's moves after the last quarter turn (the X2, X2 U2 or X2 U2 Y2 that a skeleton can end on), so it is 0 to 3 moves more. Section 1 has both readings of the cap; the rest uses the moves to the HTR itself.

## Short version

- **Where median L + 2 is the usual 8 or 9 (4b2 and 2c3), the standard meta reaches less.** It has a within-goal solution in reach on 76.8% and 86.5% of the within-goal DRs; the skeleton/variant meta on 96.0% and 96.4%. One more move of cap brings it to 92.4% and 95.0%; it gets past the skeleton/variant meta at cap 10 and cap 11.
- **On the corner cases with longer skeletons (4a2, 4c3, 2c4, 4c4), median L + 2 is 10 to 13, only 1 to 3 short of the goal, and the two are close**: 98.3% against 96.7% on 4a2, 96.7% against 98.6% on 4c3, 95.7% against 98.8% on 2c4, 100.0% against 98.5% on 4c4.
- **If the cap is on L+P+S+T, the standard meta reaches 52.4% on 4b2 and 61.0% on 2c3** at the same caps. L+P+S+T also counts the skeleton's moves after the last quarter turn, so that cap is tighter by up to 3 moves.
- **The NISS is worth 7 to 11 points to the standard meta** at median L + 2. On normal and inverse alone it reaches 66.7% on 4b2 and 75.4% on 2c3.
- **What only the skeleton/variant meta reaches** (4,076 solutions, against 13,584 both reach): solutions whose HTR comes after the cap whichever way the standard meta goes. For 71% of them it comes one move after. 52% of them are on skeletons with two more quarter turns than the DR, which are the longer ones.
- **What only the standard meta reaches** (2,839 solutions): 65% of them need the NISS. With a NISS, the stretch of half turns that finishes the HTR sits between two quarter turns of the solution, and the skeleton/variant meta reads it as extra moves before HTR. 45% of the 2,839 have P+S+T ≥ 6 on the side that comes closer and 53% have P ≥ 2; the bound discards 1%, and 2 are on a skeleton with more than two extra quarter turns.

## 1. Within-goal DRs with a solution in reach

Each cell is the share of the corner case's within-goal DRs on which the meta reaches at least one within-goal solution. The standard meta is shown at caps 8 to 13, with the cap of median L + 2 in bold.

| Corner case | Within-goal DRs | Median L | Skeleton/variant | Standard, cap 8 | Standard, cap 9 | Standard, cap 10 | Standard, cap 11 | Standard, cap 12 | Standard, cap 13 |
|---|---|---|---|---|---|---|---|---|---|
| 4b2 | 953 | 6 | 96.0% | **76.8%** | 92.4% | 99.7% | 100.0% | 100.0% | 100.0% |
| 4a2 | 120 | 8 | 96.7% | 80.0% | 90.8% | **98.3%** | 100.0% | 100.0% | 100.0% |
| 2c3 | 901 | 7 | 96.4% | 70.7% | **86.5%** | 95.0% | 99.7% | 100.0% | 100.0% |
| 4c3 | 511 | 9 | 98.6% | 42.9% | 67.9% | 85.7% | **96.7%** | 100.0% | 100.0% |
| 2c4 | 1,123 | 9 | 98.8% | 36.4% | 65.2% | 87.5% | **95.7%** | 99.5% | 100.0% |
| 0c3 | 15 | 11 | 93.3% | 33.3% | 93.3% | 93.3% | 93.3% | 100.0% | **100.0%** |
| 0c4 | 66 | 10 | 100.0% | 4.5% | 18.2% | 53.0% | 81.8% | **100.0%** | 100.0% |
| 4c4 | 397 | 11 | 98.5% | 2.0% | 8.8% | 35.5% | 64.7% | 95.2% | **100.0%** |

A cap at or over the goal (12 for 4b2 and 4a2, 13 for 2c3, 4c3 and 0c3) is the same as no cap. 0c3 and 0c4 have 15 and 66 within-goal DRs, so their percentages are coarse.

The same with the cap on L+P+S+T, so that the skeleton's moves after the last quarter turn count against the cap too. For a solution with a NISS that is the moves made on both sides plus the corner moves of the HTR's finish.

| Corner case | Skeleton/variant | Standard, L+P+S+T ≤ 8 | Standard, L+P+S+T ≤ 9 | Standard, L+P+S+T ≤ 10 | Standard, L+P+S+T ≤ 11 | Standard, L+P+S+T ≤ 12 | Standard, L+P+S+T ≤ 13 |
|---|---|---|---|---|---|---|---|
| 4b2 | 96.0% | **52.4%** | 78.3% | 88.6% | 97.9% | 100.0% | 100.0% |
| 4a2 | 96.7% | 39.2% | 65.8% | **85.0%** | 95.8% | 100.0% | 100.0% |
| 2c3 | 96.4% | 33.0% | **61.0%** | 82.6% | 92.2% | 98.8% | 100.0% |
| 4c3 | 98.6% | 8.2% | 23.1% | 58.3% | **78.9%** | 95.5% | 100.0% |
| 2c4 | 98.8% | 6.3% | 20.3% | 49.2% | **74.7%** | 88.5% | 98.4% |
| 0c3 | 93.3% | 0.0% | 13.3% | 40.0% | 46.7% | 93.3% | **100.0%** |
| 0c4 | 100.0% | 0.0% | 3.0% | 22.7% | 53.0% | **78.8%** | 100.0% |
| 4c4 | 98.5% | 0.0% | 1.3% | 6.0% | 28.5% | 50.6% | **88.4%** |

## 2. What the NISS adds to the standard meta

The standard meta at median L + 2 with and without the NISS after 1–2 moves, as the share of within-goal DRs with a solution in reach.

| Corner case | Cap | With the NISS | Normal and inverse only |
|---|---|---|---|
| 4b2 | 8 | 76.8% | 66.7% |
| 4a2 | 10 | 98.3% | 91.7% |
| 2c3 | 9 | 86.5% | 75.4% |
| 4c3 | 11 | 96.7% | 88.6% |
| 2c4 | 11 | 95.7% | 88.7% |
| 0c3 | 13 | 100.0% | 100.0% |
| 0c4 | 12 | 100.0% | 89.4% |
| 4c4 | 13 | 100.0% | 92.7% |

## 3. The same DRs under both metas

Within-goal DRs by which meta has a within-goal solution in reach, with the standard meta at median L + 2.

| Corner case | Cap | Both | Only skeleton/variant | Only standard | Neither |
|---|---|---|---|---|---|
| 4b2 | 8 | 717 | 198 | 15 | 23 |
| 4a2 | 10 | 116 | 0 | 2 | 2 |
| 2c3 | 9 | 759 | 110 | 20 | 12 |
| 4c3 | 11 | 488 | 16 | 6 | 1 |
| 2c4 | 11 | 1,066 | 44 | 9 | 4 |
| 0c3 | 13 | 14 | 0 | 1 | 0 |
| 0c4 | 12 | 66 | 0 | 0 | 0 |
| 4c4 | 13 | 391 | 0 | 6 | 0 |

## 4. Solutions only one meta reaches

Within-goal solutions over all the within-goal DRs of the corner case, with the standard meta at median L + 2. The last column is the part of the "only standard" solutions that the standard meta reaches through the NISS and not on normal or inverse alone.

| Corner case | Cap | Both reach | Only skeleton/variant | Only standard | Only standard, needs the NISS |
|---|---|---|---|---|---|
| 4b2 | 8 | 1,714 | 783 | 211 | 197 |
| 4a2 | 10 | 318 | 1 | 7 | 5 |
| 2c3 | 9 | 2,671 | 1,479 | 685 | 436 |
| 4c3 | 11 | 1,579 | 63 | 110 | 71 |
| 2c4 | 11 | 5,735 | 1,733 | 1,734 | 1,086 |
| 0c3 | 13 | 36 | 0 | 1 | 0 |
| 0c4 | 12 | 328 | 17 | 31 | 18 |
| 4c4 | 13 | 1,203 | 0 | 60 | 26 |

**Why the standard meta doesn't reach the "only skeleton/variant" solutions.** Their HTR comes after the cap in every way the standard meta has: on normal, on inverse, and with a NISS from either side. The table has the fewest moves over the cap.

| Corner case | Cap | 1 move over | 2 moves over | 3 or more over |
|---|---|---|---|---|
| 4b2 | 8 | 468 | 285 | 30 |
| 4a2 | 10 | 1 | 0 | 0 |
| 2c3 | 9 | 824 | 555 | 100 |
| 4c3 | 11 | 63 | 0 | 0 |
| 2c4 | 11 | 1,507 | 226 | 0 |
| 0c3 | 13 | 0 | 0 | 0 |
| 0c4 | 12 | 17 | 0 | 0 |
| 4c4 | 13 | 0 | 0 | 0 |

**Why the skeleton/variant meta doesn't reach the "only standard" solutions.** Each solution is filed under what stops it on the side that comes closer.

| Corner case | P+S+T ≥ 6 | P ≥ 2 | Skeleton with more than two extra quarter turns | Discarded by the bound | Other |
|---|---|---|---|---|---|
| 4b2 | 171 | 35 | 0 | 5 | 0 |
| 4a2 | 4 | 0 | 1 | 2 | 0 |
| 2c3 | 428 | 245 | 0 | 12 | 0 |
| 4c3 | 61 | 49 | 0 | 0 | 0 |
| 2c4 | 626 | 1,091 | 0 | 17 | 0 |
| 0c3 | 0 | 0 | 1 | 0 | 0 |
| 0c4 | 0 | 31 | 0 | 0 | 0 |
| 4c4 | 0 | 58 | 0 | 2 | 0 |

Most of these are NISS solutions. With one quarter turn on one side, alone or after a half turn, and the rest on the other, the stretch of half turns that finishes the HTR ends up between the first two quarter turns of the solution, or between the last two. Read as a variant of a skeleton, that stretch is a section before HTR with about as many extra moves as the finish is long, and it stays between the same two quarter turns on inverse. On a 2qt or 3qt skeleton it is the trigger or the setup and breaks P+S+T ≤ 5. On a skeleton with four or more quarter turns it can also be a section before 2qt, where it breaks P ≤ 1.

## 5. Examples

For each corner case, solutions only one of the two metas reaches, with the standard meta at median L + 2. Where it says so, the other meta has no within-goal solution in reach for that DR at all.

### 4b2 (goal 12, standard cap 8)

Only the skeleton/variant meta:

- DR `U' L2 D L2 R2 F2 D' U2 R2 U B2` (optimal 10). Solution `B2 U' R2 U' L2 F2 B2 U' L2 U` (10 moves).
    - Skeleton/variant: on normal L = 8, (P, S, T, N) = (0, 2, 0, 0).
    - Standard: HTR after 10 moves on normal and 9 on inverse; 9 with a NISS from either side. The standard meta has no within-goal solution in reach for this DR.
- DR `U2 R2 U' R2 B2 D' U' L2 F2 D' R2 B2` (optimal 11). Solution `B2 R2 U L2 B2 U2 F2 L2 U L2 D2` (11 moves).
    - Skeleton/variant: on normal L = 6, (S, T, N) = (1, 4, 0).
    - Standard: HTR after 9 moves on normal and 9 on inverse; no NISS after 1–2 moves, since it starts and ends with two or more half turns. The standard meta has no within-goal solution in reach for this DR.

Only the standard meta:

- DR `L2 U' R2 D L2 D F2 D R2 U B2 L2 U'` (optimal 12). Solution `B2 L2 U' L2 B2 L2 U2 R2 L2 F2 D R2` (12 moves).
    - Standard: `R2 D'` on inverse, then `B2 L2 U'` on normal: HTR after 5 moves; finish `L2 B2 L2 U2 R2 L2 F2`.
    - Skeleton/variant: on normal L = 5, (S, T, N) = (1, 6, 0): P+S+T = 7; on inverse L = 5, (S, T, N) = (0, 6, 1): P+S+T = 6. The skeleton/variant meta has no within-goal solution in reach for this DR.
- DR `D' B2 D2 F2 L2 B2 U' B2 D2 L2 F2 U2` (optimal 12). Solution `U2 F2 L2 U2 F2 U F2 R2 B2 U2 B2 D` (12 moves).
    - Standard: `D' B2 U2 B2 R2 F2 U'` on inverse: HTR after 7 moves; finish `F2 U2 L2 F2 U2`, on inverse.
    - Skeleton/variant: on normal L = 4, (S, T, N) = (4, 4, 0): P+S+T = 8; on inverse L = 4, (S, T, N) = (0, 4, 4): the bound gives N = 5, which makes 13 moves. The skeleton/variant meta has no within-goal solution in reach for this DR.

### 4a2 (goal 12, standard cap 10)

Only the skeleton/variant meta:

- DR `R2 U' R2 D B2 F2 L2 F2 L2 U' L2 D2 U` (optimal 12). Solution `U R2 U R2 B2 R2 F2 B2 U' F2 D R2` (12 moves).
    - Skeleton/variant: on normal L = 7, (P, S, T, N) = (0, 5, 0, 0).
    - Standard: HTR after 11 moves on normal and 12 on inverse; 11 with a NISS from either side. The standard meta reaches another solution of this DR, a 12.

Only the standard meta:

- DR `L2 U L2 D' U' L2 B2 D2 L2 F2 U2 R2 U'` (optimal 12). Solution `U R2 U2 F2 L2 U2 F2 R2 U2 F2 D' L2` (12 moves).
    - Standard: `U` on normal, then `L2 D` on inverse: HTR after 3 moves; finish `F2 U2 R2 F2 U2 L2 F2 U2 R2`, on inverse.
    - Skeleton/variant: L = 6, (S, T, N) = (0, 6, 0) on both sides: P+S+T = 6. The skeleton/variant meta has no within-goal solution in reach for this DR.
- DR `U' F2 D2 B2 F2 L2 U' L2 U2 F2 R2 D2` (optimal 12). Solution `U2 L2 B2 U2 R2 U R2 F2 B2 U2 F2 U` (12 moves).
    - Standard: `U' F2 U2 B2 F2 R2 U'` on inverse: HTR after 7 moves; finish `R2 U2 B2 L2 U2`, on inverse.
    - Skeleton/variant: on normal L = 6, (S, T, N) = (4, 2, 0): P+S+T = 6; on inverse L = 6, (S, T, N) = (0, 2, 4): the bound gives N = 5, which makes 13 moves. The skeleton/variant meta reaches another solution of this DR, a 12.

### 2c3 (goal 13, standard cap 9)

Only the skeleton/variant meta:

- DR `L2 D' B2 L2 U R2 B2 L2 U2 F2 D' L2 U2` (optimal 12). Solution `B2 L2 U F2 U' B2 L2 F2 B2 D' L2 U2` (12 moves).
    - Skeleton/variant: on normal L = 8, (P, S, T, N) = (1, 0, 3, 0).
    - Standard: HTR after 10 moves on normal and 10 on inverse; no NISS after 1–2 moves, since it starts and ends with two or more half turns. The standard meta has no within-goal solution in reach for this DR.
- DR `U F2 U' B2 L2 U' R2 U' L2 D R2 F2` (optimal 12). Solution `F2 R2 U' F2 U B2 U F2 L2 U R2 D'` (12 moves).
    - Skeleton/variant: on normal L = 10, (P, S, T, N) = (1, 1, 0, 0).
    - Standard: HTR after 12 moves on normal and 10 on inverse; with a NISS, 11 from a start on inverse. The standard meta has no within-goal solution in reach for this DR.

Only the standard meta:

- DR `R2 D' L2 F2 D U B2 F2 L2 F2 D F2 U'` (optimal 12). Solution `U F2 U' L2 B2 R2 L2 U2 B2 R2 D R2` (12 moves).
    - Standard: `R2 D'` on inverse, then `U F2 U'` on normal: HTR after 5 moves; finish `L2 B2 R2 L2 U2 B2 R2`.
    - Skeleton/variant: on normal L = 6, (P, S, T, N) = (0, 0, 6, 0): P+S+T = 6; on inverse L = 6, (P, S, T, N) = (0, 6, 0, 0): P+S+T = 6. The skeleton/variant meta has no within-goal solution in reach for this DR.
- DR `B2 R2 U2 B2 L2 R2 U' F2 U R2 U B2 F2 U2` (optimal 13). Solution `F2 B2 U L2 U' B2 U B2 U2 F2 L2 B2 R2` (13 moves).
    - Standard: `F2 B2 U L2 U' B2 U` on normal: HTR after 7 moves; finish `B2 U2 F2 L2 B2 R2`.
    - Skeleton/variant: on normal L = 7, (P, S, T, N) = (2, 0, 0, 4): P = 2; on inverse L = 7, (P, S, T, N) = (4, 0, 0, 2): P = 4. The skeleton/variant meta has no within-goal solution in reach for this DR.

### 4c3 (goal 13, standard cap 11)

Only the skeleton/variant meta:

- DR `U F2 R2 D R2 D B2 R2 D B2 U' B2 L2 U2` (optimal 13). Solution `B2 U F2 U' R2 F2 U' F2 B2 L2 U' R2 U'` (13 moves).
    - Skeleton/variant: on normal L = 10, (P, S, T, N) = (1, 2, 0, 0).
    - Standard: HTR after 13 moves on normal and 12 on inverse; 12 with a NISS from either side. The standard meta has no within-goal solution in reach for this DR.
- DR `L2 D' F2 U' B2 R2 D' F2 L2 U L2 D B2` (optimal 13). Solution `B2 U' F2 U' F2 R2 U R2 B2 U F2 D L2` (13 moves).
    - Skeleton/variant: on normal L = 11, (P, S, T, N) = (1, 1, 0, 0).
    - Standard: HTR after 12 moves on normal and 12 on inverse; 12 with a NISS from either side. The standard meta has no within-goal solution in reach for this DR.

Only the standard meta:

- DR `B2 F2 U F2 D2 U' L2 D2 B2 D' L2 B2 R2` (optimal 12). Solution `R2 B2 L2 U R2 D2 B2 U' R2 D' F2 B2` (12 moves).
    - Standard: `B2 F2 D R2 U B2 D2 R2 U'` on inverse: HTR after 9 moves; finish `L2 B2 R2`, on inverse.
    - Skeleton/variant: on normal L = 7, (P, S, T, N) = (3, 0, 0, 2): P = 3; on inverse L = 7, (P, S, T, N) = (2, 0, 0, 3): P = 2. The skeleton/variant meta has no within-goal solution in reach for this DR.
- DR `D2 B2 F2 D B2 D2 R2 D' R2 D L2 R2 U2` (optimal 13). Solution `U B2 R2 F2 B2 U' R2 B2 L2 F2 D2 R2 D` (13 moves).
    - Standard: `D'` on inverse, then `U B2 R2 F2 B2 U'` on normal: HTR after 7 moves; finish `R2 B2 L2 F2 D2 R2`.
    - Skeleton/variant: L = 7, (P, S, T, N) = (0, 3, 3, 0) on both sides: P+S+T = 6. The skeleton/variant meta has no within-goal solution in reach for this DR.

### 2c4 (goal 14, standard cap 11)

Only the skeleton/variant meta:

- DR `D' B2 U F2 L2 R2 D' B2 U2 B2 L2 U' R2 B2` (optimal 14). Solution `B2 R2 U L2 B2 U2 B2 D R2 L2 F2 U' B2 D` (14 moves).
    - Skeleton/variant: on inverse L = 10, (P, S, T, N) = (0, 2, 1, 1).
    - Standard: HTR after 14 moves on normal and 12 on inverse; with a NISS, 13 from a start on inverse. The standard meta has no within-goal solution in reach for this DR.

Only the standard meta:

- DR `U' B2 L2 F2 L2 D' F2 U' L2 D U R2 B2 U'` (optimal 13). Solution `U B2 R2 U2 F2 U R2 U L2 F2 L2 B2 U` (13 moves).
    - Standard: `U` on normal, then `U' B2 L2 F2 L2 U' R2 U'` on inverse: HTR after 9 moves; finish `F2 U2 R2 B2`, on inverse.
    - Skeleton/variant: L = 7, (P, S, T, N) = (3, 0, 3, 0) on both sides: P = 3. The skeleton/variant meta has no within-goal solution in reach for this DR.
- DR `U' R2 D2 R2 B2 R2 D B2 R2 D' F2 L2 U' B2` (optimal 14). Solution `B2 U L2 F2 U F2 R2 U' R2 B2 R2 D2 R2 U` (14 moves).
    - Standard: `U'` on inverse, then `B2 U L2 F2 U F2 R2 U'` on normal: HTR after 9 moves; finish `R2 B2 R2 D2 R2`.
    - Skeleton/variant: on normal L = 8, (P, S, T, N) = (1, 1, 4, 0): P+S+T = 6; on inverse L = 8, (P, S, T, N) = (4, 1, 1, 0): P = 4. The skeleton/variant meta has no within-goal solution in reach for this DR.

### 0c3 (goal 13, standard cap 13)

Only the skeleton/variant meta: no such solution in the sample.

Only the standard meta:

- DR `D' B2 U' F2 D B2 U F2 U' L2 U L2 U'` (optimal 13). Solution `U L2 U' L2 U F2 U' B2 U' R2 U L2 U` (13 moves).
    - Standard: `U` on normal, then `U' L2 U' R2 U B2 U F2 U' L2 U` on inverse: HTR after 12 moves; finish `L2`, on inverse.
    - Skeleton/variant: L = 13, (P, S, T, N) = (0, 0, 0, 0) on both sides: its skeleton has 7 quarter turns, more than two over the DR's. The skeleton/variant meta has no within-goal solution in reach for this DR.

### 0c4 (goal 14, standard cap 12)

Only the skeleton/variant meta:

- DR `B2 U L2 U B2 F2 R2 F2 U2 B2 U' R2 U B2` (optimal 14). Solution `B2 U' R2 U B2 U2 F2 R2 F2 B2 U' L2 U' B2` (14 moves).
    - Skeleton/variant: on normal L = 11, (P, S, T, N) = (0, 3, 0, 0).
    - Standard: HTR after 13 moves on normal and 13 on inverse; 13 with a NISS from either side. The standard meta reaches another solution of this DR, a 14.
- DR `D L2 U' L2 F2 L2 F2 U2 F2 R2 U' F2 U' F2` (optimal 14). Solution `F2 U F2 U L2 B2 U2 F2 L2 B2 R2 D B2 U'` (14 moves).
    - Skeleton/variant: on normal L = 10, (P, S, T, N) = (0, 4, 0, 0).
    - Standard: HTR after 14 moves on normal and 13 on inverse; 13 with a NISS from either side. The standard meta reaches another solution of this DR, a 14.

Only the standard meta:

- DR `D' R2 D B2 R2 D2 L2 U' B2 D F2 U2 R2 F2` (optimal 13). Solution `B2 U R2 L2 F2 U B2 U2 R2 U' F2 U2 F2 D'` (14 moves).
    - Standard: `B2 U` on normal, then `D F2 U2 F2 U R2 U2 B2 U'` on inverse: HTR after 11 moves; finish `F2 L2 R2`, on inverse.
    - Skeleton/variant: L = 10, (P, S, T, N) = (2, 0, 2, 0) on both sides: P = 2. The skeleton/variant meta reaches another solution of this DR, a 13.
- DR `L2 R2 D B2 U L2 F2 U2 B2 D' L2 U' B2` (optimal 13). Solution `B2 U' R2 U2 L2 U R2 U2 B2 U' R2 U' R2 L2` (14 moves).
    - Standard: `B2 U'` on normal, then `L2 R2 U R2 U B2 U2 R2 U'` on inverse: HTR after 11 moves; finish `L2 U2 R2`, on inverse.
    - Skeleton/variant: on normal L = 10, (P, S, T, N) = (2, 0, 0, 2): P = 2; on inverse L = 10, (P, S, T, N) = (2, 0, 2, 0): P = 2. The skeleton/variant meta reaches another solution of this DR, a 13.

### 4c4 (goal 14, standard cap 13)

Only the skeleton/variant meta: no such solution in the sample.

Only the standard meta:

- DR `D' R2 D' U2 L2 U' F2 L2 R2 D R2 U' L2 U'` (optimal 13). Solution `U L2 U R2 U' F2 B2 R2 U F2 U' R2 D` (13 moves).
    - Standard: `U` on normal, then `D' R2 U F2 U' R2 B2 F2 U R2 U'` on inverse: HTR after 12 moves; finish `L2`, on inverse.
    - Skeleton/variant: L = 11, (P, S, T, N) = (2, 0, 0, 0) on both sides: P = 2. The skeleton/variant meta has no within-goal solution in reach for this DR.
- DR `D L2 B2 L2 D2 R2 F2 D R2 U2 B2 D' L2 U'` (optimal 14). Solution `U B2 R2 U F2 U F2 R2 B2 D' B2 U B2 U` (14 moves).
    - Standard: `U` on normal, then `U' B2 U' B2 D B2 R2 F2 U' F2 U'` on inverse: HTR after 12 moves; finish `R2 B2`, on inverse.
    - Skeleton/variant: on normal L = 10, (P, S, T, N) = (4, 0, 0, 0): P = 4; on inverse L = 10, (P, S, T, N) = (3, 0, 1, 0): P = 3. The skeleton/variant meta reaches another solution of this DR, a 14.

## How it was counted

- **Sample.** The 5,960 DRs of the page (4,086 within-goal), each searched on normal and on inverse.
- **Skeleton/variant side.** The same HTRs as the page: for every DR, the number of HTRs finished and the number of those within the goal equal the page's records.
- **Standard side.** Every way to an HTR within the goal: from the DR on normal, from the DR on inverse, and from each start of one quarter turn, alone or after one half turn of a side face, on either side, with the rest on the other side. A start of a lone half turn, a start with the half turn after the quarter turn, and a start whose half turn is U2 or D2 reach the same HTRs as a start without that half turn, one move sooner, so they add nothing. A way stops at the first HTR it comes to, as on the page.
- **Finish.** The shortest half-turn finish of the HTR to a leave-slice solution, for both metas.
- **Solutions.** Section 4 counts the within-goal solutions either meta has a way to: the page's HTRs on both sides, finished or not, and the standard meta's HTRs at any cap, each with its shortest finish. Two that differ only in how a stretch of half turns is written, or in which of U and D is turned, are one solution. Whether a meta reaches a solution is then read off the solution itself: the HTRs on it are the ones before its first quarter turn (on inverse), after its last (on normal), and after a NISS start at either end.
- **Checks.** On normal and inverse, the standard meta's best solution within each cap is never worse than the best among the page's HTRs with that many moves to HTR. For every DR and every cap, "the meta reaches a within-goal solution" comes out the same from the HTRs and from the list of solutions. The moves to HTR of every solution in each of the four ways, recounted from its stretches of half turns alone, are the tool's for 21,407 of the 21,432 solutions in sight; the other 25 come through an earlier HTR on one of the ways, or have a shorter way of writing the same moves. Every example is one where the two agree, and was replayed on a separate sticker model on normal and on inverse, with its (L; P, S, T, N) read again from the solution's own moves on both sides.
- **Not covered.** The work of either meta. The standard meta as a person runs it also drops HTRs by feel or by a bound; here it finishes everything within the cap, so its reach is an upper limit.
