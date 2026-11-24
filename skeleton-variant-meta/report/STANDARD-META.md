# The standard meta against the skeleton/variant meta

24 Nov 2026

The [skeleton/variant meta](WRITEUP.md) finishes HTRs in the standard meta's order: fewest moves to HTR first, and the most pairs first among HTRs equally far. So the two metas differ only in which HTRs they finish at all. This report compares the two caps on the same HTRs, in that order:

- **The standard cap.** Finish every HTR at most c moves away, whatever its extra moves.
- **The skeleton/variant cap.** Finish every HTR with P ≤ 1 and P+S+T ≤ 5, however far it is. P, S and T are the extra moves before 2qt, in the setup and in the trigger, counted on the HTR's own skeleton as on the page.

Neither cap needs a lower bound for N, and nothing here uses one: the page's steps 4 and 5 are left out. An HTR is left out only when its moves plus the corner moves left after it are over the goal, under both caps. Both metas look in the same places: every skeleton on normal and on inverse, and the page's premove pass, where the premove counts as a move to HTR. The standard meta's usual NISS, in place of that pass, is in section 8.

The goal is 12/13/14 moves from DR to a leave-slice finish for 2qt/3qt/4qt DRs. The sample is the page's: 2,000 random DRs of each kind (1,960 for 2qt).

How to read the columns:

- **HTRs per DR.** The HTRs the cap keeps, as a median over all the corner case's DRs, within-goal or not. It is what gets finished on a DR where nothing fits the goal.
- **Reach.** The share of within-goal DRs where at least one kept HTR has a finish within the goal.
- **Within 5 / 10 / 20.** The share of within-goal DRs with a within-goal finish among the first 5 / 10 / 20 HTRs finished.
- **Place of the first solution.** How many HTRs are finished up to the first one within goal, as a median over within-goal DRs. A dash means fewer than half of them have one.

## Short version

- **The cap doesn't change how soon a solution is found.** In the same order both metas start with the same HTRs. On 4b2, a within-goal finish is among the first 10 HTRs for 62% of within-goal DRs under the skeleton/variant cap and 62% under a cap of 11 moves, and the first one comes at place 5 under both. No corner case differs by more than 1.5 points (section 1).
- **Alone, the skeleton/variant cap usually needs more HTRs for the same reach.** In 5 of the 8 corner cases a standard cap reaches at least as many within-goal DRs with fewer HTRs per DR. In the other 3 it sits between two standard caps: on 4b2 it keeps 1,540 HTRs per DR and reaches 97.8%, a cap of 10 moves keeps 675 and reaches 97.4%, and a cap of 11 moves 2,013 and 99.8% (section 1).
- **That is because it keeps HTRs that are too far.** Past a cap one move under the goal are 36% to 46% of its HTRs, and one of them is within goal 1 in 2,807 times, against 1 in 526 for an HTR both caps keep: the goal leaves it no move for a finish, so it has to solve the DR as it stands (section 2).
- **The two caps cut different HTRs and work together.** With a cap one move under the goal on top, the skeleton/variant cap reaches the same within-goal DRs in every corner case with 46% to 64% of the HTRs. On 4b2 that is 982 HTRs per DR and 97.8%, against 2,013 and 99.8% for the cap of 11 moves alone. Over the sample, the two together give up 44 of 4,086 within-goal DRs next to that cap alone (section 3).
- **The premove pass is worth as much to the standard cap.** It adds 64 within-goal DRs to the standard cap's reach and 47 to the skeleton/variant cap's, out of 4,086 (section 5).
- **On the page, the bound does what a cap on the moves does here, and more.** With the corner-case-aware bound and step 4, the page's meta finishes 88 HTRs per DR on 4b2, reaches 97.7% and finds a within-goal finish within 10 for 74% (section 7).
- **The standard meta's usual NISS goes further than the premove pass.** A NISS after 1 move gives what the pass gives. One after up to 3 moves keeps 1.2x to 1.5x the HTRs at the same cap, and on 4b2 finds a within-goal finish within 10 for 69% of within-goal DRs instead of 63%. The caps don't account for that difference (section 8).

## 1. The two caps at similar numbers of HTRs

This table puts the skeleton/variant cap between the two standard caps with the nearest numbers of HTRs per DR. The corner cases are in the page's order, shortest skeleton first.

| Corner case | Cap | HTRs per DR (median) | Reach | Within 5 | Within 10 | Within 20 | Place of the first solution (median) |
|---|---|---|---|---|---|---|---|
| 4b2 | At most 10 moves | 675 | 97.4% | 53% | 62% | 70% | 5 |
| 4b2 | **P ≤ 1, P+S+T ≤ 5** | **1,540** | **97.8%** | **53%** | **62%** | **70%** | **5** |
| 4b2 | At most 11 moves | 2,013 | 99.8% | 53% | 62% | 70% | 5 |
| 4a2 | At most 11 moves | 610 | 97.5% | 43% | 62% | 72% | 7 |
| 4a2 | **P ≤ 1, P+S+T ≤ 5** | **1,222** | **96.7%** | **43%** | **62%** | **72%** | **7** |
| 4a2 | At most 12 moves (every HTR in reach) | 1,293 | 97.5% | 43% | 62% | 72% | 7 |
| 2c3 | At most 11 moves | 1,927 | 98.1% | 51% | 62% | 72% | 5 |
| 2c3 | **P ≤ 1, P+S+T ≤ 5** | **4,028** | **98.2%** | **50%** | **61%** | **71%** | **5** |
| 2c3 | At most 12 moves | 6,584.5 | 100.0% | 51% | 62% | 72% | 5 |
| 4c3 | At most 12 moves | 2,560 | 99.8% | 36% | 46% | 57% | 14 |
| 4c3 | **P ≤ 1, P+S+T ≤ 5** | **2,961** | **99.2%** | **35%** | **45%** | **57%** | **15** |
| 4c3 | At most 13 moves (every HTR in reach) | 4,602 | 99.8% | 36% | 46% | 57% | 14 |
| 2c4 | At most 12 moves | 2,573 | 98.6% | 41% | 53% | 66% | 9 |
| 2c4 | **P ≤ 1, P+S+T ≤ 5** | **7,668** | **99.6%** | **40%** | **53%** | **66%** | **9** |
| 2c4 | At most 13 moves | 9,810 | 100.0% | 41% | 53% | 66% | 9 |
| 0c3 | At most 12 moves | 512 | 93.3% | 50% | 60% | 73% | 5 |
| 0c3 | **P ≤ 1, P+S+T ≤ 5** | **840** | **93.3%** | **50%** | **60%** | **73%** | **5** |
| 0c3 | At most 13 moves (every HTR in reach) | 916 | 93.3% | 50% | 60% | 73% | 5 |
| 0c4 | At most 13 moves | 11,927 | 100.0% | 22% | 27% | 38% | 40 |
| 0c4 | **P ≤ 1, P+S+T ≤ 5** | **14,068** | **100.0%** | **22%** | **28%** | **38%** | **40** |
| 0c4 | At most 14 moves (every HTR in reach) | 24,217.5 | 100.0% | 22% | 27% | 38% | 40 |
| 4c4 | At most 13 moves | 2,677 | 100.0% | 20% | 29% | 40% | 39 |
| 4c4 | **P ≤ 1, P+S+T ≤ 5** | **3,398** | **100.0%** | **21%** | **29%** | **40%** | **38** |
| 4c4 | At most 14 moves (every HTR in reach) | 4,718 | 100.0% | 20% | 29% | 40% | 39 |

**How soon a solution is found is the same.** Both metas start with the same HTRs, so the cap only matters once it is reached. At the standard cap closest in HTRs, found within 5, 10 and 20 are within 1.5 points of the skeleton/variant cap's in every corner case.

**The caps trade reach for HTRs to finish.** In 5 of the 8 corner cases (4a2, 4c3, 0c3, 0c4 and 4c4) a standard cap reaches at least as many within-goal DRs as the skeleton/variant cap with fewer HTRs per DR. In the other 3 (4b2, 2c3 and 2c4) it sits between two standard caps: the one below reaches 0.1 to 1.0 points less with 34% to 48% of the HTRs, and the one above 0.4 to 2.0 points more with 128% to 163%.

## 2. What each cap keeps that the other doesn't

This section takes the standard cap closest to the skeleton/variant cap in HTRs per DR, and splits the HTRs by which cap keeps them. Per DR is a mean over the corner case's DRs. Within goal is how often such an HTR has a finish within the goal.

| Corner case | Standard cap | Kept by both, per DR | Kept by both, within goal | Only the standard cap, per DR | Only the standard cap, within goal | Only the skeleton/variant cap, per DR | Only the skeleton/variant cap, within goal |
|---|---|---|---|---|---|---|---|
| 4b2 | 11 moves | 1,007 | 1 in 395 | 1,354 | 1 in 957 | 570 | 1 in 2,981 |
| 4a2 | 12 moves | 1,502 | 1 in 847 | 626 | 1 in 1,344 | 0 | — |
| 2c3 | 12 moves | 2,462 | 1 in 398 | 4,772 | 1 in 964 | 1,482 | 1 in 3,391 |
| 4c3 | 12 moves | 2,105 | 1 in 563 | 850 | 1 in 866 | 1,407 | 1 in 2,778 |
| 2c4 | 13 moves | 5,114 | 1 in 547 | 6,689 | 1 in 891 | 3,360 | 1 in 2,809 |
| 0c3 | 13 moves | 1,368 | 1 in 1,502 | 242 | 1 in 4,080 | 0 | — |
| 0c4 | 13 moves | 8,363 | 1 in 830 | 3,844 | 1 in 1,250 | 5,913 | 1 in 2,439 |
| 4c4 | 13 moves | 2,367 | 1 in 753 | 826 | 1 in 1,024 | 2,020 | 1 in 2,378 |

**Past the standard cap, the skeleton/variant cap keeps HTRs that are too far.** They are 36% to 46% of its HTRs where the standard cap is under the goal, and one of them is within goal 1 in 2,807 times, against 1 in 526 for an HTR both caps keep: the goal leaves it no move for a finish, so it has to solve the DR as it stands.

**Within the standard cap, what the skeleton/variant cap drops is worth about half of what it keeps.** An HTR that only the standard cap keeps is within goal 1 in 931 times: 1 in 825 when it has P ≥ 2, 1 in 1,037 when it has P+S+T ≥ 6, and 1 in 1,271 with both.

The same split for within-goal DRs: reached by both caps, by one only, or by neither. The last columns say what the nearest within-goal HTR of a DR that only the standard cap reaches has against the skeleton/variant cap.

| Corner case | Standard cap | Within-goal DRs | Reached by both | Only the standard cap | Only the skeleton/variant cap | Neither | Only the standard cap: needs P ≥ 2 | Only the standard cap: needs P+S+T ≥ 6 | Only the standard cap: needs both |
|---|---|---|---|---|---|---|---|---|---|
| 4b2 | 11 moves | 953 | 932 | 19 | 0 | 2 | 7 | 12 | 0 |
| 4a2 | 12 moves | 120 | 116 | 1 | 0 | 3 | 0 | 1 | 0 |
| 2c3 | 12 moves | 901 | 885 | 16 | 0 | 0 | 9 | 7 | 0 |
| 4c3 | 12 moves | 511 | 507 | 3 | 0 | 1 | 3 | 0 | 0 |
| 2c4 | 13 moves | 1,123 | 1,118 | 5 | 0 | 0 | 4 | 1 | 0 |
| 0c3 | 13 moves | 15 | 14 | 0 | 0 | 1 | 0 | 0 | 0 |
| 0c4 | 13 moves | 66 | 66 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4c4 | 13 moves | 397 | 397 | 0 | 0 | 0 | 0 | 0 | 0 |
| All | | 4,086 | 4,035 | 44 | 0 | 7 | 23 | 21 | 0 |

No within-goal DR is reached by the skeleton/variant cap only: whenever a within-goal HTR passes it past the standard cap, another one is within the cap. The DRs neither cap reaches have their within-goal solutions on skeletons with four more quarter turns than the DR, which the HTRs of this report leave out (see the end).

One example per corner case, where there is one. In each, the other cap reaches no within-goal HTR of the DR.

**Only the standard cap:**

- 4b2, at most 11 moves. `D L2 R2 U' B2 U' B2 U F2 R2 B2 F2`: `F2 B2 R2 F2 U' B2 U B2 U R2 L2 D'` solves it in 12 moves, with HTR after 8 moves on inverse. It reads (P, S, T, N) = (3, 0, 2, 0) on a 7-move skeleton on normal (P = 3) and (P, S, T, N) = (2, 0, 0, 3) on a 7-move skeleton on inverse (P = 2); with its last `D'` on normal as a premove, (P, S, T, N) = (3, 0, 0, 2) with L = 7 (P = 3).
- 4a2, at most 12 moves. `L2 U L2 D' U' L2 B2 D2 L2 F2 U2 R2 U'`: `U R2 U2 F2 L2 U2 F2 R2 U2 F2 D' L2` solves it in 12 moves, with HTR after 11 moves on normal. It reads (S, T, N) = (0, 6, 0) on a 6-move skeleton on both sides: P+S+T = 6.
- 2c3, at most 12 moves. `B2 R2 U2 B2 L2 R2 U' F2 U R2 U B2 F2 U2`: `F2 B2 U L2 U' B2 U B2 U2 F2 L2 B2 R2` solves it in 13 moves, with HTR after 7 moves on normal. It reads (P, S, T, N) = (2, 0, 0, 4) on a 7-move skeleton on normal (P = 2) and (P, S, T, N) = (4, 0, 0, 2) on a 7-move skeleton on inverse (P = 4).
- 4c3, at most 12 moves. `B2 F2 U F2 D2 U' L2 D2 B2 D' L2 B2 R2`: `R2 B2 L2 U R2 D2 B2 U' R2 D' F2 B2` solves it in 12 moves, with HTR after 9 moves on inverse. It reads (P, S, T, N) = (3, 0, 0, 2) on a 7-move skeleton on normal (P = 3) and (P, S, T, N) = (2, 0, 0, 3) on a 7-move skeleton on inverse (P = 2).
- 2c4, at most 13 moves. `D L2 B2 U' F2 L2 U' F2 U F2 L2 U' L2 F2 D'`: `L2 U2 B2 L2 U L2 U B2 U' F2 D B2 L2 F2` solves it in 14 moves, with HTR after 11 moves on normal. It reads (P, S, T, N) = (2, 0, 0, 3) on a 9-move skeleton on normal (P = 2) and (P, S, T, N) = (3, 0, 0, 2) on a 9-move skeleton on inverse (P = 3).

## 3. The two caps together

The two caps cut different HTRs, so they can be used together: P ≤ 1, P+S+T ≤ 5, and at most c moves to HTR. This table takes c one move under the goal, where the standard cap alone still reaches everything it can.

| Corner case | Cap on the moves | Standard cap alone, HTRs per DR (median) | Standard cap alone, reach | Skeleton/variant cap alone, HTRs per DR (median) | Skeleton/variant cap alone, reach | Both, HTRs per DR (median) | Both, reach |
|---|---|---|---|---|---|---|---|
| 4b2 | 11 moves | 2,013 | 99.8% | 1,540 | 97.8% | 982 | 97.8% |
| 4a2 | 11 moves | 610 | 97.5% | 1,222 | 96.7% | 560 | 96.7% |
| 2c3 | 12 moves | 6,584.5 | 100.0% | 4,028 | 98.2% | 2,486.5 | 98.2% |
| 4c3 | 12 moves | 2,560 | 99.8% | 2,961 | 99.2% | 1,846 | 99.2% |
| 2c4 | 13 moves | 9,810 | 100.0% | 7,668 | 99.6% | 4,431 | 99.6% |
| 0c3 | 12 moves | 512 | 93.3% | 840 | 93.3% | 512 | 93.3% |
| 0c4 | 13 moves | 11,927 | 100.0% | 14,068 | 100.0% | 8,235 | 100.0% |
| 4c4 | 13 moves | 2,677 | 100.0% | 3,398 | 100.0% | 2,022 | 100.0% |

**The cap on the moves costs the skeleton/variant cap nothing.** In every corner case it reaches the same within-goal DRs with 46% to 64% of the HTRs. **The skeleton/variant cap costs the standard cap a little.** On top of it, it keeps 38% to 100% of the HTRs and gives up 44 of the sample's 4,086 within-goal DRs, the ones that need P ≥ 2 or P+S+T ≥ 6 on both sides.

## 4. Every cap, corner case by corner case

Each table has the standard cap at six values, the skeleton/variant cap with P+S+T ≤ 3 to 6 and with P ≤ 1 alone, and the two caps together. The page's cap is in bold. The largest standard cap is the goal itself, which keeps every HTR in reach.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal. P ≤ 1, P+S+T ≤ 5 keeps 1,222 HTRs per DR and reaches 96.7%; at most 11 moves keeps 610 and reaches 97.5%, and at most 12 moves keeps 1,293 and reaches 97.5%.

| Cap | HTRs per DR (median) | Reach | Within 5 | Within 10 | Within 20 | Place of the first solution (median) |
|---|---|---|---|---|---|---|
| At most 7 moves | 0 | 36.7% | 20% | 33% | 37% | — |
| At most 8 moves | 8 | 69.2% | 36% | 54% | 62% | 9 |
| At most 9 moves | 70 | 86.7% | 42% | 61% | 72% | 7 |
| At most 10 moves | 280 | 95.0% | 43% | 62% | 72% | 7 |
| At most 11 moves | 610 | 97.5% | 43% | 62% | 72% | 7 |
| At most 12 moves (every HTR in reach) | 1,293 | 97.5% | 43% | 62% | 72% | 7 |
| P ≤ 1, P+S+T ≤ 3 | 368 | 90.8% | 43% | 62% | 72% | 7 |
| P ≤ 1, P+S+T ≤ 4 | 881 | 96.7% | 43% | 62% | 72% | 7 |
| **P ≤ 1, P+S+T ≤ 5** | **1,222** | **96.7%** | **43%** | **62%** | **72%** | **7** |
| P ≤ 1, P+S+T ≤ 6 | 1,235 | 97.5% | 43% | 62% | 72% | 7 |
| P ≤ 1 | 1,235 | 97.5% | 43% | 62% | 72% | 7 |
| P ≤ 1, P+S+T ≤ 5, at most 9 moves | 70 | 86.7% | 42% | 61% | 72% | 7 |
| P ≤ 1, P+S+T ≤ 5, at most 10 moves | 272 | 95.0% | 43% | 62% | 72% | 7 |
| P ≤ 1, P+S+T ≤ 5, at most 11 moves | 560 | 96.7% | 43% | 62% | 72% | 7 |

**4b2** · 1,584 DRs, 953 within-goal. P ≤ 1, P+S+T ≤ 5 keeps 1,540 HTRs per DR and reaches 97.8%; at most 10 moves keeps 675 and reaches 97.4%, and at most 11 moves keeps 2,013 and reaches 99.8%.

| Cap | HTRs per DR (median) | Reach | Within 5 | Within 10 | Within 20 | Place of the first solution (median) |
|---|---|---|---|---|---|---|
| At most 7 moves | 6 | 55.0% | 50% | 54% | 55% | 6 |
| At most 8 moves | 33 | 71.5% | 53% | 61% | 68% | 5 |
| At most 9 moves | 159 | 88.4% | 53% | 62% | 70% | 5 |
| At most 10 moves | 675 | 97.4% | 53% | 62% | 70% | 5 |
| At most 11 moves | 2,013 | 99.8% | 53% | 62% | 70% | 5 |
| At most 12 moves (every HTR in reach) | 3,760.5 | 99.8% | 53% | 62% | 70% | 5 |
| P ≤ 1, P+S+T ≤ 3 | 484 | 86.5% | 50% | 61% | 69% | 6 |
| P ≤ 1, P+S+T ≤ 4 | 1,004 | 96.0% | 53% | 62% | 71% | 5 |
| **P ≤ 1, P+S+T ≤ 5** | **1,540** | **97.8%** | **53%** | **62%** | **70%** | **5** |
| P ≤ 1, P+S+T ≤ 6 | 2,215.5 | 99.0% | 53% | 62% | 70% | 5 |
| P ≤ 1 | 2,594.5 | 99.1% | 53% | 62% | 70% | 5 |
| P ≤ 1, P+S+T ≤ 5, at most 9 moves | 133 | 86.6% | 53% | 62% | 70% | 5 |
| P ≤ 1, P+S+T ≤ 5, at most 10 moves | 404 | 95.0% | 53% | 62% | 70% | 5 |
| P ≤ 1, P+S+T ≤ 5, at most 11 moves | 982 | 97.8% | 53% | 62% | 70% | 5 |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample). P ≤ 1, P+S+T ≤ 5 keeps 840 HTRs per DR and reaches 93.3%; at most 12 moves keeps 512 and reaches 93.3%, and at most 13 moves keeps 916 and reaches 93.3%.

| Cap | HTRs per DR (median) | Reach | Within 5 | Within 10 | Within 20 | Place of the first solution (median) |
|---|---|---|---|---|---|---|
| At most 8 moves | 0 | 33.3% | 31% | 33% | 33% | — |
| At most 9 moves | 0 | 66.7% | 46% | 53% | 66% | 6.5 |
| At most 10 moves | 32 | 66.7% | 46% | 53% | 66% | 6.5 |
| At most 11 moves | 188 | 80.0% | 50% | 60% | 73% | 5 |
| At most 12 moves | 512 | 93.3% | 50% | 60% | 73% | 5 |
| At most 13 moves (every HTR in reach) | 916 | 93.3% | 50% | 60% | 73% | 5 |
| P ≤ 1, P+S+T ≤ 3 | 840 | 93.3% | 50% | 60% | 73% | 5 |
| P ≤ 1, P+S+T ≤ 4 | 840 | 93.3% | 50% | 60% | 73% | 5 |
| **P ≤ 1, P+S+T ≤ 5** | **840** | **93.3%** | **50%** | **60%** | **73%** | **5** |
| P ≤ 1, P+S+T ≤ 6 | 840 | 93.3% | 50% | 60% | 73% | 5 |
| P ≤ 1 | 840 | 93.3% | 50% | 60% | 73% | 5 |
| P ≤ 1, P+S+T ≤ 5, at most 10 moves | 32 | 66.7% | 46% | 53% | 66% | 6.5 |
| P ≤ 1, P+S+T ≤ 5, at most 11 moves | 188 | 80.0% | 50% | 60% | 73% | 5 |
| P ≤ 1, P+S+T ≤ 5, at most 12 moves | 512 | 93.3% | 50% | 60% | 73% | 5 |

**2c3** · 1,048 DRs, 901 within-goal. P ≤ 1, P+S+T ≤ 5 keeps 4,028 HTRs per DR and reaches 98.2%; at most 11 moves keeps 1,927 and reaches 98.1%, and at most 12 moves keeps 6,584.5 and reaches 100.0%.

| Cap | HTRs per DR (median) | Reach | Within 5 | Within 10 | Within 20 | Place of the first solution (median) |
|---|---|---|---|---|---|---|
| At most 8 moves | 15 | 63.6% | 49% | 57% | 62% | 6 |
| At most 9 moves | 87 | 80.8% | 50% | 61% | 72% | 5 |
| At most 10 moves | 451 | 91.7% | 51% | 62% | 72% | 5 |
| At most 11 moves | 1,927 | 98.1% | 51% | 62% | 72% | 5 |
| At most 12 moves | 6,584.5 | 100.0% | 51% | 62% | 72% | 5 |
| At most 13 moves (every HTR in reach) | 12,872.5 | 100.0% | 51% | 62% | 72% | 5 |
| P ≤ 1, P+S+T ≤ 3 | 1,506 | 90.2% | 50% | 61% | 70% | 6 |
| P ≤ 1, P+S+T ≤ 4 | 2,577.5 | 95.9% | 50% | 61% | 72% | 5 |
| **P ≤ 1, P+S+T ≤ 5** | **4,028** | **98.2%** | **50%** | **61%** | **71%** | **5** |
| P ≤ 1, P+S+T ≤ 6 | 5,357.5 | 99.0% | 50% | 61% | 71% | 5 |
| P ≤ 1 | 7,390 | 99.0% | 50% | 61% | 71% | 5 |
| P ≤ 1, P+S+T ≤ 5, at most 10 moves | 339.5 | 89.9% | 50% | 61% | 71% | 5 |
| P ≤ 1, P+S+T ≤ 5, at most 11 moves | 1,080 | 96.2% | 50% | 61% | 71% | 5 |
| P ≤ 1, P+S+T ≤ 5, at most 12 moves | 2,486.5 | 98.2% | 50% | 61% | 71% | 5 |

**4c3** · 851 DRs, 511 within-goal. P ≤ 1, P+S+T ≤ 5 keeps 2,961 HTRs per DR and reaches 99.2%; at most 12 moves keeps 2,560 and reaches 99.8%, and at most 13 moves keeps 4,602 and reaches 99.8%.

| Cap | HTRs per DR (median) | Reach | Within 5 | Within 10 | Within 20 | Place of the first solution (median) |
|---|---|---|---|---|---|---|
| At most 8 moves | 2 | 32.3% | 28% | 31% | 32% | — |
| At most 9 moves | 24 | 56.6% | 35% | 43% | 51% | 19 |
| At most 10 moves | 150 | 79.1% | 36% | 46% | 57% | 14 |
| At most 11 moves | 696 | 93.0% | 36% | 46% | 57% | 14 |
| At most 12 moves | 2,560 | 99.8% | 36% | 46% | 57% | 14 |
| At most 13 moves (every HTR in reach) | 4,602 | 99.8% | 36% | 46% | 57% | 14 |
| P ≤ 1, P+S+T ≤ 3 | 1,448 | 96.7% | 35% | 46% | 57% | 14 |
| P ≤ 1, P+S+T ≤ 4 | 2,392 | 99.2% | 35% | 45% | 57% | 15 |
| **P ≤ 1, P+S+T ≤ 5** | **2,961** | **99.2%** | **35%** | **45%** | **57%** | **15** |
| P ≤ 1, P+S+T ≤ 6 | 2,976 | 99.2% | 35% | 45% | 57% | 15 |
| P ≤ 1 | 2,976 | 99.2% | 35% | 45% | 57% | 15 |
| P ≤ 1, P+S+T ≤ 5, at most 10 moves | 136 | 77.5% | 35% | 45% | 57% | 15 |
| P ≤ 1, P+S+T ≤ 5, at most 11 moves | 566 | 91.8% | 35% | 45% | 57% | 15 |
| P ≤ 1, P+S+T ≤ 5, at most 12 moves | 1,846 | 99.2% | 35% | 45% | 57% | 15 |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample). P ≤ 1, P+S+T ≤ 5 keeps 14,068 HTRs per DR and reaches 100.0%; at most 13 moves keeps 11,927 and reaches 100.0%, and at most 14 moves keeps 24,217.5 and reaches 100.0%.

| Cap | HTRs per DR (median) | Reach | Within 5 | Within 10 | Within 20 | Place of the first solution (median) |
|---|---|---|---|---|---|---|
| At most 9 moves | 6 | 18.2% | 17% | 18% | 18% | — |
| At most 10 moves | 70 | 51.5% | 22% | 27% | 36% | 59.5 |
| At most 11 moves | 501.5 | 77.3% | 22% | 27% | 38% | 40 |
| At most 12 moves | 2,708 | 98.5% | 22% | 27% | 38% | 40 |
| At most 13 moves | 11,927 | 100.0% | 22% | 27% | 38% | 40 |
| At most 14 moves (every HTR in reach) | 24,217.5 | 100.0% | 22% | 27% | 38% | 40 |
| P ≤ 1, P+S+T ≤ 3 | 7,677.5 | 98.5% | 22% | 28% | 38% | 40 |
| P ≤ 1, P+S+T ≤ 4 | 11,525 | 100.0% | 22% | 28% | 38% | 40 |
| **P ≤ 1, P+S+T ≤ 5** | **14,068** | **100.0%** | **22%** | **28%** | **38%** | **40** |
| P ≤ 1, P+S+T ≤ 6 | 14,068 | 100.0% | 22% | 28% | 38% | 40 |
| P ≤ 1 | 14,068 | 100.0% | 22% | 28% | 38% | 40 |
| P ≤ 1, P+S+T ≤ 5, at most 11 moves | 461.5 | 75.8% | 22% | 28% | 38% | 40 |
| P ≤ 1, P+S+T ≤ 5, at most 12 moves | 2,204.5 | 98.5% | 22% | 28% | 38% | 40 |
| P ≤ 1, P+S+T ≤ 5, at most 13 moves | 8,235 | 100.0% | 22% | 28% | 38% | 40 |

**2c4** · 1,243 DRs, 1,123 within-goal. P ≤ 1, P+S+T ≤ 5 keeps 7,668 HTRs per DR and reaches 99.6%; at most 12 moves keeps 2,573 and reaches 98.6%, and at most 13 moves keeps 9,810 and reaches 100.0%.

| Cap | HTRs per DR (median) | Reach | Within 5 | Within 10 | Within 20 | Place of the first solution (median) |
|---|---|---|---|---|---|---|
| At most 9 moves | 11 | 55.0% | 39% | 48% | 53% | 12 |
| At most 10 moves | 86 | 79.2% | 41% | 53% | 66% | 9 |
| At most 11 moves | 541 | 92.3% | 41% | 53% | 66% | 9 |
| At most 12 moves | 2,573 | 98.6% | 41% | 53% | 66% | 9 |
| At most 13 moves | 9,810 | 100.0% | 41% | 53% | 66% | 9 |
| At most 14 moves (every HTR in reach) | 18,955 | 100.0% | 41% | 53% | 66% | 9 |
| P ≤ 1, P+S+T ≤ 3 | 3,815 | 96.5% | 40% | 53% | 66% | 9 |
| P ≤ 1, P+S+T ≤ 4 | 6,010 | 99.3% | 40% | 53% | 66% | 9 |
| **P ≤ 1, P+S+T ≤ 5** | **7,668** | **99.6%** | **40%** | **53%** | **66%** | **9** |
| P ≤ 1, P+S+T ≤ 6 | 9,496 | 99.6% | 40% | 53% | 66% | 9 |
| P ≤ 1 | 9,517 | 99.6% | 40% | 53% | 66% | 9 |
| P ≤ 1, P+S+T ≤ 5, at most 11 moves | 385 | 90.0% | 40% | 53% | 66% | 9 |
| P ≤ 1, P+S+T ≤ 5, at most 12 moves | 1,609 | 97.9% | 40% | 53% | 66% | 9 |
| P ≤ 1, P+S+T ≤ 5, at most 13 moves | 4,431 | 99.6% | 40% | 53% | 66% | 9 |

**4c4** · 691 DRs, 397 within-goal. P ≤ 1, P+S+T ≤ 5 keeps 3,398 HTRs per DR and reaches 100.0%; at most 13 moves keeps 2,677 and reaches 100.0%, and at most 14 moves keeps 4,718 and reaches 100.0%.

| Cap | HTRs per DR (median) | Reach | Within 5 | Within 10 | Within 20 | Place of the first solution (median) |
|---|---|---|---|---|---|---|
| At most 9 moves | 0 | 7.1% | 6% | 7% | 7% | — |
| At most 10 moves | 8 | 30.0% | 17% | 22% | 27% | — |
| At most 11 moves | 88 | 57.4% | 20% | 29% | 39% | 47 |
| At most 12 moves | 568 | 87.2% | 20% | 29% | 40% | 39 |
| At most 13 moves | 2,677 | 100.0% | 20% | 29% | 40% | 39 |
| At most 14 moves (every HTR in reach) | 4,718 | 100.0% | 20% | 29% | 40% | 39 |
| P ≤ 1, P+S+T ≤ 3 | 3,121 | 99.0% | 21% | 29% | 40% | 38 |
| P ≤ 1, P+S+T ≤ 4 | 3,398 | 100.0% | 21% | 29% | 40% | 38 |
| **P ≤ 1, P+S+T ≤ 5** | **3,398** | **100.0%** | **21%** | **29%** | **40%** | **38** |
| P ≤ 1, P+S+T ≤ 6 | 3,398 | 100.0% | 21% | 29% | 40% | 38 |
| P ≤ 1 | 3,398 | 100.0% | 21% | 29% | 40% | 38 |
| P ≤ 1, P+S+T ≤ 5, at most 11 moves | 84 | 56.7% | 20% | 29% | 39% | 48 |
| P ≤ 1, P+S+T ≤ 5, at most 12 moves | 503 | 86.9% | 21% | 29% | 40% | 38 |
| P ≤ 1, P+S+T ≤ 5, at most 13 moves | 2,022 | 100.0% | 21% | 29% | 40% | 38 |

## 5. The premove pass under both caps

The premove pass is part of the skeleton/variant meta, and the tables above give it to the standard cap as well. This table shows each cap on normal and inverse alone, and with the pass. The standard cap is the one of section 2.

| Corner case | Standard cap | Standard cap, HTRs per DR, no pass | Standard cap, HTRs per DR, with the pass | Standard cap, reach, no pass | Standard cap, reach, with the pass | Skeleton/variant cap, HTRs per DR, no pass | Skeleton/variant cap, HTRs per DR, with the pass | Skeleton/variant cap, reach, no pass | Skeleton/variant cap, reach, with the pass |
|---|---|---|---|---|---|---|---|---|---|
| 4b2 | 11 moves | 1,661 | 2,013 | 98.7% | 99.8% | 1,101 | 1,540 | 96.1% | 97.8% |
| 4a2 | 12 moves | 1,012 | 1,293 | 97.5% | 97.5% | 912 | 1,222 | 96.7% | 96.7% |
| 2c3 | 12 moves | 4,947.5 | 6,584.5 | 99.2% | 100.0% | 2,762 | 4,028 | 96.7% | 98.2% |
| 4c3 | 12 moves | 1,994 | 2,560 | 97.8% | 99.8% | 2,244 | 2,961 | 98.6% | 99.2% |
| 2c4 | 13 moves | 7,052 | 9,810 | 99.3% | 100.0% | 5,845 | 7,668 | 98.8% | 99.6% |
| 0c3 | 13 moves | 896 | 916 | 93.3% | 93.3% | 760 | 840 | 93.3% | 93.3% |
| 0c4 | 13 moves | 7,974 | 11,927 | 100.0% | 100.0% | 10,546 | 14,068 | 100.0% | 100.0% |
| 4c4 | 13 moves | 1,889 | 2,677 | 92.7% | 100.0% | 2,748 | 3,398 | 98.5% | 100.0% |

Over the sample's 4,086 within-goal DRs, the pass adds 64 to the standard cap's reach and 47 to the skeleton/variant cap's. Its HTRs come early in the order: with the last quarter turn made first, the trigger becomes part of the finish, so the HTR is that many moves nearer.

## 6. The pairs in the order

This table shows the skeleton/variant cap with the order as it is, most pairs first among HTRs equally far, and with those HTRs taken in random order. The standard cap of section 2 gives the same numbers to within 0.7 points.

| Corner case | Within 5, most pairs first | Within 5, random | Within 10, most pairs first | Within 10, random | Within 20, most pairs first | Within 20, random | Place of the first solution, most pairs first | Place of the first solution, random |
|---|---|---|---|---|---|---|---|---|
| 4b2 | 53% | 49% | 62% | 58% | 70% | 66% | 5 | 6 |
| 4a2 | 43% | 28% | 62% | 46% | 72% | 66% | 7 | 12 |
| 2c3 | 50% | 46% | 61% | 57% | 71% | 66% | 5 | 7 |
| 4c3 | 35% | 30% | 45% | 40% | 57% | 50% | 15 | 21 |
| 2c4 | 40% | 37% | 53% | 49% | 66% | 60% | 9 | 11 |
| 0c3 | 50% | 37% | 60% | 53% | 73% | 67% | 5 | 8.5 |
| 0c4 | 22% | 14% | 28% | 21% | 38% | 33% | 40 | 56 |
| 4c4 | 21% | 15% | 29% | 21% | 40% | 30% | 38 | 71 |

## 7. For scale: the page's meta, with the bound

On the [page](WRITEUP.md) the skeleton/variant cap doesn't work alone: step 5 discards a variant when its extra moves plus the bound's N don't fit the goal, and step 4 leaves a variant to the side where it comes earlier. This table puts the page's meta, with the corner-case-aware bound, next to the two caps of this report. The order is the same in all three.

| Corner case | Standard cap | Standard cap, HTRs per DR | Skeleton/variant cap, HTRs per DR | Page's meta, HTRs per DR | Standard cap, reach | Skeleton/variant cap, reach | Page's meta, reach | Standard cap, within 10 | Skeleton/variant cap, within 10 | Page's meta, within 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 4b2 | 11 moves | 2,013 | 1,540 | 88 | 99.8% | 97.8% | 97.7% | 62% | 62% | 74% |
| 4a2 | 12 moves | 1,293 | 1,222 | 34 | 97.5% | 96.7% | 96.7% | 62% | 62% | 80% |
| 2c3 | 12 moves | 6,584.5 | 4,028 | 264.5 | 100.0% | 98.2% | 98.0% | 62% | 61% | 69% |
| 4c3 | 12 moves | 2,560 | 2,961 | 152 | 99.8% | 99.2% | 99.2% | 46% | 45% | 61% |
| 2c4 | 13 moves | 9,810 | 7,668 | 483 | 100.0% | 99.6% | 99.6% | 53% | 53% | 63% |
| 0c3 | 13 moves | 916 | 840 | 28 | 93.3% | 93.3% | 93.3% | 60% | 60% | 73% |
| 0c4 | 13 moves | 11,927 | 14,068 | 766.5 | 100.0% | 100.0% | 100.0% | 27% | 28% | 37% |
| 4c4 | 13 moves | 2,677 | 3,398 | 178 | 100.0% | 100.0% | 100.0% | 29% | 29% | 51% |

The bound and step 4 take the skeleton/variant cap's HTRs per DR down by 15x to 36x in the corner cases with at least 100 within-goal DRs, and what they take out is mostly not within goal, so a solution also comes sooner.

## 8. The standard cap with the standard meta's usual NISS

The tables above give both caps the same places to look, the premove pass included. The standard meta has a NISS of its own: one NISS after a start of 1 to 3 moves (a quarter turn; a side half turn and a quarter turn; a U-layer move, a side half turn and a quarter turn). This table shows the standard cap of section 2 with no NISS and with that NISS, by how long the start may be. It is counted on a list of the standard meta's own (see below), in the same order, so it also has the few HTRs on skeletons with four more quarter turns.

| Corner case | Standard cap | NISS | HTRs per DR (median) | Reach | Within 5 | Within 10 | Within 20 | Place of the first solution (median) |
|---|---|---|---|---|---|---|---|---|
| 4b2 | 11 moves | none | 1,666 | 98.8% | 51% | 60% | 68% | 5 |
| 4b2 | 11 moves | after 1 move | 2,099 | 100.0% | 54% | 63% | 72% | 4 |
| 4b2 | 11 moves | after up to 2 moves | 2,543.5 | 100.0% | 59% | 67% | 75% | 3 |
| 4b2 | 11 moves | after up to 3 moves | 2,814.5 | 100.0% | 61% | 69% | 78% | 3 |
| 4a2 | 12 moves | none | 1,036 | 100.0% | 41% | 56% | 69% | 8 |
| 4a2 | 12 moves | after 1 move | 1,362.5 | 100.0% | 45% | 61% | 74% | 7 |
| 4a2 | 12 moves | after up to 2 moves | 1,558 | 100.0% | 53% | 71% | 81% | 5 |
| 4a2 | 12 moves | after up to 3 moves | 1,615 | 100.0% | 52% | 70% | 84% | 5 |
| 2c3 | 12 moves | none | 4,947.5 | 99.2% | 45% | 56% | 68% | 8 |
| 2c3 | 12 moves | after 1 move | 6,594.5 | 100.0% | 51% | 62% | 73% | 5 |
| 2c3 | 12 moves | after up to 2 moves | 8,099 | 100.0% | 55% | 66% | 77% | 4 |
| 2c3 | 12 moves | after up to 3 moves | 9,059 | 100.0% | 56% | 68% | 79% | 4 |
| 4c3 | 12 moves | none | 1,994 | 97.8% | 28% | 37% | 51% | 20 |
| 4c3 | 12 moves | after 1 move | 2,576 | 100.0% | 37% | 47% | 59% | 12 |
| 4c3 | 12 moves | after up to 2 moves | 3,038 | 100.0% | 45% | 56% | 67% | 7 |
| 4c3 | 12 moves | after up to 3 moves | 3,421 | 100.0% | 51% | 61% | 71% | 5 |
| 2c4 | 13 moves | none | 7,052 | 99.3% | 36% | 48% | 59% | 12 |
| 2c4 | 13 moves | after 1 move | 9,810 | 100.0% | 42% | 55% | 67% | 8 |
| 2c4 | 13 moves | after up to 2 moves | 11,748 | 100.0% | 49% | 63% | 75% | 6 |
| 2c4 | 13 moves | after up to 3 moves | 13,705 | 100.0% | 51% | 66% | 78% | 5 |
| 0c3 | 13 moves | none | 899 | 100.0% | 18% | 20% | 27% | 129 |
| 0c3 | 13 moves | after 1 move | 925 | 100.0% | 53% | 71% | 73% | 5 |
| 0c3 | 13 moves | after up to 2 moves | 1,013 | 100.0% | 69% | 91% | 93% | 2 |
| 0c3 | 13 moves | after up to 3 moves | 1,094 | 100.0% | 68% | 90% | 93% | 2 |
| 0c4 | 13 moves | none | 7,974 | 100.0% | 15% | 24% | 33% | 54 |
| 0c4 | 13 moves | after 1 move | 11,927 | 100.0% | 23% | 28% | 38% | 37 |
| 0c4 | 13 moves | after up to 2 moves | 15,115 | 100.0% | 22% | 27% | 35% | 39 |
| 0c4 | 13 moves | after up to 3 moves | 16,791 | 100.0% | 42% | 49% | 60% | 12 |
| 4c4 | 13 moves | none | 1,889 | 92.7% | 17% | 24% | 31% | 61 |
| 4c4 | 13 moves | after 1 move | 2,677 | 100.0% | 21% | 30% | 41% | 37 |
| 4c4 | 13 moves | after up to 2 moves | 3,575 | 100.0% | 23% | 33% | 45% | 29 |
| 4c4 | 13 moves | after up to 3 moves | 4,039 | 100.0% | 32% | 44% | 54% | 16 |

**A NISS after 1 move is the premove pass without its conditions** (3 or more quarter turns, a skeleton that ends in HH). It gives the numbers of the tables above: found within 10 is within 2 points of the standard cap's with the pass in every corner case with at least 100 within-goal DRs.

**A NISS after up to 3 moves finds a solution sooner.** At the same cap it keeps 1.2x to 1.5x the HTRs of a NISS after 1 move, and found within 10 goes up by 6 points on 2c3 and by 14 on 4c3, the two ends among those corner cases. This is a difference between the two metas that the caps don't account for: the skeleton/variant meta has no NISS but the premove pass.

## How it was counted

- **HTRs.** The page's records: on both sides of every DR, every HTR in reach on a skeleton with the DR's quarter turns or two more, and the HTRs of the premove pass. In reach means the moves to HTR plus the corner moves left after it fit the goal. An HTR is one path up to how its U and D layer turns are written, with the best finish among those.
- **Moves to HTR.** The length of the path, premove included. On its own skeleton that is L+P+S+T less the skeleton's moves after HTR.
- **Caps.** The standard cap is on the moves to HTR. The skeleton/variant cap is P ≤ 1 and P+S+T ≤ 5 on the HTR's own skeleton; in the premove pass, on the skeleton of what is left. No bound, no step 4.
- **Order.** By moves to HTR, fewest first, then most pairs, counted as on the page. Ties are taken in random order, and found within K and the place of the first solution are taken over 20 such orders.
- **Finish.** The shortest leave-slice finish in half turns from the HTR, from an exact table.

The standard cap doesn't need skeletons, so it was also counted on a list of its own: every HTR within the cap on normal, on inverse and with the NISS of section 8, with any number of quarter turns, the pairs counted at the HTR. This table compares the two counts on normal and inverse alone, at the standard cap closest to the skeleton/variant cap there.

| Corner case | Standard cap | HTRs per DR, records | HTRs per DR, own list | Reach, records | Reach, own list | Within 10, records | Within 10, own list | Place of the first solution, records | Place of the first solution, own list |
|---|---|---|---|---|---|---|---|---|---|
| 4b2 | 11 moves | 1,661 | 1,666 | 98.7% | 98.8% | 60% | 60% | 5 | 5 |
| 4a2 | 12 moves | 1,012 | 1,036 | 97.5% | 100.0% | 58% | 56% | 8 | 8 |
| 2c3 | 11 moves | 1,588 | 1,588 | 96.0% | 96.0% | 56% | 56% | 8 | 8 |
| 4c3 | 12 moves | 1,994 | 1,994 | 97.8% | 97.8% | 35% | 37% | 22 | 20 |
| 2c4 | 13 moves | 7,052 | 7,052 | 99.3% | 99.3% | 45% | 48% | 13 | 12 |
| 0c3 | 13 moves | 896 | 899 | 93.3% | 100.0% | 20% | 20% | 130.5 | 129 |
| 0c4 | 13 moves | 7,974 | 7,974 | 100.0% | 100.0% | 17% | 24% | 67 | 54 |
| 4c4 | 13 moves | 1,889 | 1,889 | 92.7% | 92.7% | 23% | 24% | 65 | 61 |

The own list has the HTRs on skeletons with four or more quarter turns over the DR's, which the records leave out: 0.1% of its HTRs at those caps. With no cap at all, on normal and inverse they hold the only within-goal solutions of 7 of the sample's 4,086 within-goal DRs. For example, the 4a2 DR `U L2 B2 U B2 D' L2 D' R2 D F2 U'` is solved by `U F2 U' B2 U L2 D B2 U' B2 L2 U'` in 12 moves, with 6 quarter turns. The two counts also differ in the pairs: the own list counts them at the HTR, the records right after the last insertion, which comes before the trigger when the trigger has no extra move. That is where found within 10 and the place of the first solution differ in the table.

Checks:

- The own list against a separate search for within-goal solutions: for every DR, cap and NISS depth, the best within-goal total is the same (145,108 comparisons).
- The same search against the records: under P ≤ 1 and P+S+T ≤ 5 it finds a within-goal solution for the same DRs, with the same best length.
- On the own list the chances are worked out exactly for random ties; 40 random orders of the list itself give the same found within 5, 10 and 20 to within 0.4 points.
- Every example was replayed on an independent sticker model, read again on both sides and after its premove, and its moves to HTR recounted from its own moves.
