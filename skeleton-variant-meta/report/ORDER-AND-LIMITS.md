# HTR search order and limits

24 Nov 2026

This is an analysis of different metas for prioritizing HTRs when searching for a DR finish.
The key decisions that the meta needs to make are:
 - **Breadth vs depth**: how many HTRs to check on a skeleton before moving to another skeleton
 - **Length restriction**: limits on the HTRs to check
 - **NISS strategy**: when to use NISS

The analysis is based on a sample of 2,000 random DRs for each 2qt/3qt/4qt corner case. The goal is
to find leave-slice in 12/13/14 for 2qt/3qt/4qt.

The analysis uses the following definitions:
 - **G** goal total move count to leave-slice: 12, 13, or 14
 - **L** length of the corner skeleton
 - **E** extra moves that must be added to the corner skeleton to reach HTR
 - **H** total moves to reach HTR

See [Advanced DR Bounding](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0/edit?usp=sharing) for definition of a corner skeleton, its length, and extra moves. In that doc's notation, E=P+S+T

## Conclusions

- **Shallow first pass** Check up to 5 HTRs on each skeleton before moving to the next one. Then make a second depth-first pass
- **Both relative and absolute cap on HTR length** Restrict to E ≤ 5 and H ≤ G−2, with ≤ 1 extra move before 2qt
- **NISS after a single QT is enough for all but 0c3, 4c3, and 4c4**

## 1. Breadth vs Depth

Finishing the shortest HTR first should find a solution soonest. But that order mixes the skeletons, and by hand it is easier to go through one skeleton at a time.
This section measures what that costs by comparing three strategies:

- **Breadth first** Strict ordering by H, mixing together all skeletons on both sides. The a-priori optimal ordering
- **Depth first** Order skeletons by L, then check all of a skeleton's HTRs before moving to the next
- **Two pass** Order skeletons by L, then check up to k HTRs per skeleton. Finish with a depth-first second pass through the skeletons

The HTRs found include linear in both directions, plus NISS after an initial U move.

For all DRs that have a within-goal solution, we compute

- **Median place.** How many HTRs must be checked to find the first within-goal finish, median over all DRs
- **HTRs to finish for 95%.** How many HTRs have to be finished to have a 95% chance of finding a within-goal finish. 0c3 never reaches 95%.

Across all corner cases, a two-pass strategy works best, but the depth matters. Too deep is wasteful,
while too shallow falls back to overall depth-first. Trying 5 HTRs per skeleton gives the best trade-off, roughly doubling both numbers compared to the optimal.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal · E ≤ 5, H ≤ 11 · 573 HTRs and 12 skeletons per DR (median) · reach 97.5%. Depth first puts the first solution at place 13 instead of 7. Of the two-pass orders, 4 per skeleton has the best median place (9), and 8 per skeleton needs the fewest HTRs for 95% (203, against 188 breadth first).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| Breadth first | 7 | 188 |
| Depth first | 13 | 1,250 |
| Two pass, 2 per skeleton | 19 | 637 |
| Two pass, 3 per skeleton | 13 | 649 |
| Two pass, 4 per skeleton | 9 | 340 |
| Two pass, 5 per skeleton | 9 | 269 |
| Two pass, 6 per skeleton | 9 | 267 |
| Two pass, 8 per skeleton | 10 | 203 |
| Two pass, 10 per skeleton | 11 | 207 |

**4b2** · 1,584 DRs, 953 within-goal · E ≤ 5, H ≤ 11 · 990.5 HTRs and 26 skeletons per DR (median) · reach 98.0%. Depth first puts the first solution at place 23 instead of 4. Of the two-pass orders, 3 per skeleton has the best median place (7), and 10 per skeleton needs the fewest HTRs for 95% (332, against 206 breadth first).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| Breadth first | 4 | 206 |
| Depth first | 23 | 1,002 |
| Two pass, 2 per skeleton | 8 | 664 |
| Two pass, 3 per skeleton | 7 | 600 |
| Two pass, 4 per skeleton | 7 | 559 |
| Two pass, 5 per skeleton | 8 | 448 |
| Two pass, 6 per skeleton | 8 | 428 |
| Two pass, 8 per skeleton | 10 | 336 |
| Two pass, 10 per skeleton | 11 | 332 |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample) · E ≤ 5, H ≤ 12 · 512 HTRs and 4 skeletons per DR (median) · reach 93.3%. Depth first puts the first solution at place 17 instead of 5. Of the two-pass orders, 3 per skeleton has the best median place (4).

The analysis only extends skeletons to 2 extra qt, and 1 of the 15 within-goal DRs needs more, so the success rate stops at 93.3% and 95% is never reached.

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| Breadth first | 5 | — |
| Depth first | 17 | — |
| Two pass, 2 per skeleton | 15 | — |
| Two pass, 3 per skeleton | 4 | — |
| Two pass, 4 per skeleton | 5 | — |
| Two pass, 5 per skeleton | 6 | — |
| Two pass, 6 per skeleton | 7 | — |
| Two pass, 8 per skeleton | 9 | — |
| Two pass, 10 per skeleton | 11 | — |

**2c3** · 1,048 DRs, 901 within-goal · E ≤ 5, H ≤ 12 · 2,486.5 HTRs and 63 skeletons per DR (median) · reach 98.2%. Depth first puts the first solution at place 69 instead of 6. Of the two-pass orders, 2 per skeleton has the best median place (10), and 10 per skeleton needs the fewest HTRs for 95% (685, against 427 breadth first).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| Breadth first | 6 | 427 |
| Depth first | 69 | 1,804 |
| Two pass, 2 per skeleton | 10 | 1,289 |
| Two pass, 3 per skeleton | 10 | 1,056 |
| Two pass, 4 per skeleton | 11 | 990 |
| Two pass, 5 per skeleton | 12 | 926 |
| Two pass, 6 per skeleton | 14 | 861 |
| Two pass, 8 per skeleton | 17 | 858 |
| Two pass, 10 per skeleton | 20 | 685 |

**4c3** · 851 DRs, 511 within-goal · E ≤ 5, H ≤ 12 · 1,846 HTRs and 37 skeletons per DR (median) · reach 99.2%. Depth first puts the first solution at place 118 instead of 15. Of the two-pass orders, 4 per skeleton has the best median place (30), and 10 per skeleton needs the fewest HTRs for 95% (1,142, against 565 breadth first).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| Breadth first | 15 | 565 |
| Depth first | 118 | 2,383 |
| Two pass, 2 per skeleton | 33 | 1,731 |
| Two pass, 3 per skeleton | 31 | 1,523 |
| Two pass, 4 per skeleton | 30 | 1,428 |
| Two pass, 5 per skeleton | 31 | 1,256 |
| Two pass, 6 per skeleton | 32 | 1,229 |
| Two pass, 8 per skeleton | 35 | 1,221 |
| Two pass, 10 per skeleton | 41 | 1,142 |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample) · E ≤ 5, H ≤ 13 · 8,235 HTRs and 134 skeletons per DR (median) · reach 100.0%. Depth first puts the first solution at place 894 instead of 40. Of the two-pass orders, 2 per skeleton has the best median place (72), and 5 per skeleton needs the fewest HTRs for 95% (2,790, against 600 breadth first).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| Breadth first | 40 | 600 |
| Depth first | 894 | 4,984 |
| Two pass, 2 per skeleton | 72 | 3,510 |
| Two pass, 3 per skeleton | 76 | 3,356 |
| Two pass, 4 per skeleton | 88 | 3,236 |
| Two pass, 5 per skeleton | 86 | 2,790 |
| Two pass, 6 per skeleton | 85 | 2,855 |
| Two pass, 8 per skeleton | 98 | 3,022 |
| Two pass, 10 per skeleton | 96 | 3,162 |

**2c4** · 1,243 DRs, 1,123 within-goal · E ≤ 5, H ≤ 13 · 4,431 HTRs and 98 skeletons per DR (median) · reach 99.6%. Depth first puts the first solution at place 241 instead of 9. Of the two-pass orders, 2 per skeleton has the best median place (16), and 10 per skeleton needs the fewest HTRs for 95% (950, against 350 breadth first).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| Breadth first | 9 | 350 |
| Depth first | 241 | 2,605 |
| Two pass, 2 per skeleton | 16 | 1,815 |
| Two pass, 3 per skeleton | 16 | 1,587 |
| Two pass, 4 per skeleton | 18 | 1,470 |
| Two pass, 5 per skeleton | 20 | 1,268 |
| Two pass, 6 per skeleton | 21 | 1,164 |
| Two pass, 8 per skeleton | 25 | 1,013 |
| Two pass, 10 per skeleton | 29 | 950 |

**4c4** · 691 DRs, 397 within-goal · E ≤ 5, H ≤ 13 · 2,022 HTRs and 73 skeletons per DR (median) · reach 100.0%. Depth first puts the first solution at place 236 instead of 39. Of the two-pass orders, 3 per skeleton has the best median place (67), and 10 per skeleton needs the fewest HTRs for 95% (1,128, against 584 breadth first).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| Breadth first | 39 | 584 |
| Depth first | 236 | 2,242 |
| Two pass, 2 per skeleton | 70 | 1,696 |
| Two pass, 3 per skeleton | 67 | 1,593 |
| Two pass, 4 per skeleton | 77 | 1,539 |
| Two pass, 5 per skeleton | 81 | 1,406 |
| Two pass, 6 per skeleton | 91 | 1,406 |
| Two pass, 8 per skeleton | 97 | 1,163 |
| Two pass, 10 per skeleton | 102 | 1,128 |

## 2. Length Restrictions

An HTR too close to the goal has a very small chance of hitting the goal. We enforce these limits always, including for the analysis in Section 1:
 - **H < G** Must reach HTR with at least one move to spare
 - **≤ 1 extra move before 2qt** Usually unnecessary because we are checking both directions

We use the k=5, two-pass strategy from section 1 and consider three kinds of additional restrictions

- **H** Cap on the total moves to reach HTR
- **E** Cap on the extra moves to reach HTR
- **Combined** Cap both separately

For each corner case, the tables below show

- **HTRs per DR.** The median number of HTRs that satisfy the restriction. As before, ratios are most important
- **Reach.** The fraction of within-goal finishes that satisfy the restriction
- **Median place.** How many HTRs must be checked to find the first within-goal finish. A dash means fewer than half of the within-goal DRs are reached

The rows in bold are, the loosest restriction that still has 95% reach.

Across corner cases, a combined restriction gives the best tradeoff: E ≤ 5, H ≤ G−2, which trims the HTR count
by 2x-4x while keeping reach above 95%.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal. The tightest restrictions with 95% reach: H ≤ 10 (272 HTRs per DR); E ≤ 4 (476); and E ≤ 4 with H ≤ 10 (239).

| Restriction | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| H ≤ 7 | 0 | 42.5% | — |
| H ≤ 8 | 8 | 70.8% | 11 |
| H ≤ 9 | 72 | 87.5% | 10 |
| **H ≤ 10** | **272** | **95.8%** | **9** |
| H ≤ 11 | 573 | 97.5% | 9 |
| E ≤ 3 | 228.5 | 92.5% | 9 |
| **E ≤ 4** | **476** | **97.5%** | **9** |
| E ≤ 5 | 573 | 97.5% | 9 |
| E ≤ 6 | 573 | 97.5% | 9 |
| **E ≤ 4, H ≤ 10** | **239** | **95.8%** | **9** |
| E ≤ 5, H ≤ 10 | 272 | 95.8% | 9 |
| E ≤ 6, H ≤ 10 | 272 | 95.8% | 9 |

**4b2** · 1,584 DRs, 953 within-goal. The tightest restrictions with 95% reach: H ≤ 10 (600 HTRs per DR); E ≤ 4 (675.5); and E ≤ 5 with H ≤ 10 (411).

| Restriction | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| H ≤ 7 | 7 | 56.0% | 6 |
| H ≤ 8 | 33 | 71.7% | 7 |
| H ≤ 9 | 151 | 87.2% | 8 |
| **H ≤ 10** | **600** | **96.2%** | **8** |
| H ≤ 11 | 1,650.5 | 99.1% | 8 |
| E ≤ 3 | 376 | 87.9% | 8 |
| **E ≤ 4** | **675.5** | **96.3%** | **7** |
| E ≤ 5 | 990.5 | 98.0% | 8 |
| E ≤ 6 | 1,435 | 99.0% | 8 |
| E ≤ 4, H ≤ 10 | 280.5 | 93.7% | 7 |
| **E ≤ 5, H ≤ 10** | **411** | **95.2%** | **8** |
| E ≤ 6, H ≤ 10 | 555 | 96.2% | 8 |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample). No restriction reaches 95% of the within-goal DRs here, so no row is in bold.

| Restriction | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| H ≤ 8 | 0 | 33.3% | — |
| H ≤ 9 | 0 | 66.7% | 6 |
| H ≤ 10 | 32 | 66.7% | 7 |
| H ≤ 11 | 188 | 80.0% | 6 |
| H ≤ 12 | 512 | 93.3% | 6 |
| E ≤ 3 | 512 | 93.3% | 6 |
| E ≤ 4 | 512 | 93.3% | 6 |
| E ≤ 5 | 512 | 93.3% | 6 |
| E ≤ 6 | 512 | 93.3% | 6 |
| E ≤ 4, H ≤ 11 | 188 | 80.0% | 6 |
| E ≤ 5, H ≤ 11 | 188 | 80.0% | 6 |
| E ≤ 6, H ≤ 11 | 188 | 80.0% | 6 |

**2c3** · 1,048 DRs, 901 within-goal. The tightest restrictions with 95% reach: H ≤ 11 (1,364.5 HTRs per DR); E ≤ 4 (1,612.5); and E ≤ 5 with H ≤ 11 (1,080).

| Restriction | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| H ≤ 8 | 14 | 61.9% | 10 |
| H ≤ 9 | 74 | 78.6% | 11 |
| H ≤ 10 | 340.5 | 89.9% | 12 |
| **H ≤ 11** | **1,364.5** | **96.6%** | **12** |
| H ≤ 12 | 4,376 | 99.0% | 12 |
| E ≤ 3 | 952 | 90.2% | 12 |
| **E ≤ 4** | **1,612.5** | **95.9%** | **12** |
| E ≤ 5 | 2,486.5 | 98.2% | 12 |
| E ≤ 6 | 3,396 | 99.0% | 12 |
| E ≤ 4, H ≤ 11 | 644 | 93.6% | 12 |
| **E ≤ 5, H ≤ 11** | **1,080** | **96.2%** | **12** |
| E ≤ 6, H ≤ 11 | 1,356 | 96.6% | 12 |

**4c3** · 851 DRs, 511 within-goal. The tightest restrictions with 95% reach: H ≤ 12 (1,846 HTRs per DR); and E ≤ 3 (983). With H ≤ 11 nothing reaches 95%.

| Restriction | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| H ≤ 8 | 2 | 32.3% | — |
| H ≤ 9 | 23 | 55.6% | 22 |
| H ≤ 10 | 137 | 77.5% | 20 |
| H ≤ 11 | 569 | 91.8% | 27 |
| **H ≤ 12** | **1,846** | **99.2%** | **31** |
| **E ≤ 3** | **983** | **96.7%** | **31** |
| E ≤ 4 | 1,659 | 99.2% | 31 |
| E ≤ 5 | 1,846 | 99.2% | 30 |
| E ≤ 6 | 1,846 | 99.2% | 31 |
| E ≤ 4, H ≤ 11 | 565 | 91.8% | 27 |
| E ≤ 5, H ≤ 11 | 566 | 91.8% | 27 |
| E ≤ 6, H ≤ 11 | 569 | 91.8% | 27 |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample). The tightest restrictions with 95% reach: H ≤ 12 (2,204.5 HTRs per DR); E ≤ 3 (5,502); and E ≤ 3 with H ≤ 12 (2,118.5).

| Restriction | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| H ≤ 9 | 6 | 18.2% | — |
| H ≤ 10 | 70 | 51.5% | 79 |
| H ≤ 11 | 461.5 | 75.8% | 64 |
| **H ≤ 12** | **2,204.5** | **98.5%** | **85** |
| H ≤ 13 | 8,235 | 100.0% | 86 |
| **E ≤ 3** | **5,502** | **98.5%** | **86** |
| E ≤ 4 | 7,724 | 100.0% | 86 |
| E ≤ 5 | 8,235 | 100.0% | 86 |
| E ≤ 6 | 8,235 | 100.0% | 86 |
| **E ≤ 3, H ≤ 12** | **2,118.5** | **98.5%** | **79** |
| E ≤ 4, H ≤ 12 | 2,204.5 | 98.5% | 85 |
| E ≤ 5, H ≤ 12 | 2,204.5 | 98.5% | 85 |
| E ≤ 6, H ≤ 12 | 2,204.5 | 98.5% | 85 |

**2c4** · 1,243 DRs, 1,123 within-goal. The tightest restrictions with 95% reach: H ≤ 12 (1,612 HTRs per DR); E ≤ 3 (2,351); and E ≤ 4 with H ≤ 12 (1,328).

| Restriction | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| H ≤ 9 | 11 | 54.2% | 16 |
| H ≤ 10 | 71 | 76.9% | 16 |
| H ≤ 11 | 385 | 90.0% | 19 |
| **H ≤ 12** | **1,612** | **97.9%** | **20** |
| H ≤ 13 | 5,327 | 99.6% | 21 |
| **E ≤ 3** | **2,351** | **96.5%** | **20** |
| E ≤ 4 | 3,521 | 99.3% | 21 |
| E ≤ 5 | 4,431 | 99.6% | 21 |
| E ≤ 6 | 5,325 | 99.6% | 21 |
| **E ≤ 4, H ≤ 12** | **1,328** | **97.8%** | **20** |
| E ≤ 5, H ≤ 12 | 1,609 | 97.9% | 20 |
| E ≤ 6, H ≤ 12 | 1,612 | 97.9% | 20 |

**4c4** · 691 DRs, 397 within-goal. The tightest restrictions with 95% reach: H ≤ 13 (2,022 HTRs per DR); and E ≤ 3 (1,887). With H ≤ 12 nothing reaches 95%.

| Restriction | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| H ≤ 9 | 0 | 7.1% | — |
| H ≤ 10 | 8 | 30.0% | — |
| H ≤ 11 | 84 | 56.7% | 75 |
| H ≤ 12 | 503 | 86.9% | 80 |
| **H ≤ 13** | **2,022** | **100.0%** | **81** |
| **E ≤ 3** | **1,887** | **99.0%** | **82** |
| E ≤ 4 | 2,022 | 100.0% | 81 |
| E ≤ 5 | 2,022 | 100.0% | 81 |
| E ≤ 6 | 2,022 | 100.0% | 81 |
| E ≤ 4, H ≤ 12 | 503 | 86.9% | 80 |
| E ≤ 5, H ≤ 12 | 503 | 86.9% | 80 |
| E ≤ 6, H ≤ 12 | 503 | 86.9% | 80 |

## 3. NISS Strategy

The search strategy used above always uses linear search on both normal and inverse, and also checks NISS for skeletons that begin or end with a qt.
This section shows the effect of different NISS strategies:

- **None** No NISS on any skeleton
- **After 1 move** NISS only after a single qt (as in Sections 1 and 2)
- **After 1-2 moves** Also NISS after `X2 U`
- **After 1-3 moves** Also NISS after `U X2 U`

The statistics use the ordering of Section 1 and the restrictions of Section 2. 
Within each skeleton, the order is: 1) after-1 NISS 2) linear 3) after-2 NISS 4) after-3 NISS 

A NISS after 1 move is important. For most corner cases, it's enough to get the reach above 95%.
The exceptions are 0c3, 4c3, and 4c4, which get another boost at 1-2 moves.

| Corner case | NISS | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|---|
| 4b2 | None | 338 | 87.5% | 8 |
| 4b2 | After 1 move | 411 | 95.2% | 8 |
| 4b2 | After 1-2 moves | 499 | 98.3% | 8 |
| 4b2 | After 1-3 moves | 554 | 98.5% | 8 |
| 4a2 | None | 252 | 91.7% | 10 |
| 4a2 | After 1 move | 272 | 95.8% | 9 |
| 4a2 | After 1-2 moves | 306 | 97.5% | 9 |
| 4a2 | After 1-3 moves | 313 | 97.5% | 9 |
| 2c3 | None | 872.5 | 92.8% | 16 |
| 2c3 | After 1 move | 1,080 | 96.2% | 12 |
| 2c3 | After 1-2 moves | 1,267.5 | 98.1% | 12 |
| 2c3 | After 1-3 moves | 1,462.5 | 98.9% | 12 |
| 4c3 | None | 478 | 86.1% | 46 |
| 4c3 | After 1 move | 566 | 91.8% | 27 |
| 4c3 | After 1-2 moves | 687 | 95.9% | 27 |
| 4c3 | After 1-3 moves | 742 | 97.3% | 27 |
| 2c4 | None | 1,268 | 94.3% | 24 |
| 2c4 | After 1 move | 1,609 | 97.9% | 20 |
| 2c4 | After 1-2 moves | 1,945 | 99.2% | 20 |
| 2c4 | After 1-3 moves | 2,267 | 99.4% | 20 |
| 0c3 | None | 128 | 53.3% | 257 |
| 0c3 | After 1 move | 188 | 80.0% | 7 |
| 0c3 | After 1-2 moves | 192 | 93.3% | 7 |
| 0c3 | After 1-3 moves | 202 | 93.3% | 7 |
| 0c4 | None | 1,660 | 87.9% | 126 |
| 0c4 | After 1 move | 2,204.5 | 98.5% | 84 |
| 0c4 | After 1-2 moves | 2,808 | 100.0% | 84 |
| 0c4 | After 1-3 moves | 3,084.5 | 100.0% | 84 |
| 4c4 | None | 382 | 69.3% | 124 |
| 4c4 | After 1 move | 503 | 86.9% | 80 |
| 4c4 | After 1-2 moves | 638 | 95.0% | 80 |
| 4c4 | After 1-3 moves | 734 | 97.0% | 79 |
