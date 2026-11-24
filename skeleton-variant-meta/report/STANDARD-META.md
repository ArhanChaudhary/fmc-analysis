# HTR search order and limits

24 Nov 2026

Three choices in a search for DR finishes, measured on the DRs of the [skeleton/variant meta](WRITEUP.md): the order the HTRs are finished in (section 1), which HTRs are finished at all (section 2), and how much NISS to use (section 3).

The goal is 12/13/14 moves from DR to a leave-slice finish for 2qt/3qt/4qt DRs. The sample is the page's: 2,000 random DRs of each kind (1,960 for 2qt). P, S and T are the extra moves before 2qt, in the setup and in the trigger, counted on the HTR's own skeleton, and L is the skeleton's length, as on the page. Nothing here uses a lower bound for N, so the page's steps 4 and 5 are left out. Every HTR is at most G−1 moves away, as in the page's step 3: at G moves there is no move left for a finish.

## Short version

- **By hand, two passes cost little on the first solution and more on the tail.** Going through one skeleton at a time puts the first solution 3x to 27x later than finishing by HTR length. With a first pass of 5 HTRs per skeleton it comes 1.4x to 2.4x later, and getting to 95% of within-goal DRs takes 2.0x to 3.6x as many HTRs (section 1).
- **Neither cap wins alone, and together they need the fewest HTRs.** At 95% reach, the cap on the extra moves needs fewer HTRs than the cap on the moves in 4 of the 6 corner cases with at least 100 within-goal DRs, and more in 1. Where the cap on the moves can also go under G−1 (4b2, 4a2, 2c3 and 2c4), the pair keeps 56% to 85% of the HTRs of the better single cap (section 2).
- **More NISS adds HTRs, not earlier solutions.** A NISS after 1 move is the premove pass without its conditions. One after up to 3 moves keeps 1.2x to 1.6x the HTRs under the page's cap, and moves the median place by 1 at most (section 3).

## 1. Order: by HTR length, or one skeleton at a time

Finishing the nearest HTR first should find a solution soonest. But that order mixes the skeletons, and by hand it is easier to go through one skeleton at a time. This section measures what that costs.

The HTRs are the same in every order: the ones with P ≤ 1 and P+S+T ≤ 5, on normal, on inverse and in the page's premove pass, whose premove counts as a move. The orders:

- **By HTR length.** All the DR's HTRs by moves to HTR, fewest first, with the skeletons and the two sides mixed.
- **One skeleton at a time.** Skeletons shortest first, by L, with the two sides mixed. All of a skeleton's HTRs are finished before the next skeleton: those of its premove pass first, then the linear ones, the nearest first in each.
- **Two passes, k per skeleton.** The same walk, but the first pass finishes at most k HTRs of each skeleton, premove pass and linear together. The second pass goes through the skeletons again, one at a time, for the rest. k runs from 2 to 10.

In every order, HTRs equally far are taken with the most pairs first, and skeletons of one length in random order. What is still tied is taken at random; the numbers are over 20 such orders. An HTR of the premove pass belongs to the skeleton whose last quarter turn is its premove.

How to read the columns:

- **Median place.** How many HTRs are finished up to the first one within goal, as a median over within-goal DRs.
- **HTRs to finish for 95%.** How many HTRs have to be finished per DR before 95% of within-goal DRs have a within-goal finish. A dash means the HTRs kept don't reach 95% of them.

**One skeleton at a time costs a lot.** In the corner cases with at least 100 within-goal DRs, the first solution comes 3x to 27x later (median place), and 95% of within-goal DRs take 4x to 10x as many HTRs.

**Two passes get the median back, and part of the 95%.** What the first pass doesn't find is left to the second pass, which is one skeleton at a time again. So a larger first pass brings the 95% point in and pushes the median out. This table shows each first-pass size against the order by HTR length, over the same corner cases: how much later the first solution comes, and how many more HTRs it takes for 95%.

| First pass | Median place, against by HTR length | HTRs for 95%, against by HTR length |
|---|---|---|
| 2 per skeleton | 1.8x to 3.4x | 2.9x to 5.1x |
| 3 per skeleton | 1.4x to 2.7x | 2.6x to 4.5x |
| 4 per skeleton | 1.6x to 2.3x | 2.3x to 4.2x |
| 5 per skeleton | 1.4x to 2.4x | 2.0x to 3.6x |
| 6 per skeleton | 1.4x to 2.6x | 1.7x to 3.2x |
| 8 per skeleton | 1.6x to 3.4x | 0.9x to 2.9x |
| 10 per skeleton | 1.7x to 4.0x | 0.9x to 2.7x |
| One skeleton at a time | 2.7x to 27.0x | 3.8x to 10.5x |

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal · at most 11 moves to HTR · 560 HTRs and 12 skeletons per DR (median) · reach 96.7%. One skeleton at a time puts the first solution at place 19 instead of 7. Of the two-pass orders, 5 per skeleton has the best median place (10), and 10 per skeleton needs the fewest HTRs for 95% (197, against 216 by HTR length).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| By HTR length | 7 | 216 |
| One skeleton at a time | 19 | 2,261 |
| Two passes, 2 per skeleton | 24 | 833 |
| Two passes, 3 per skeleton | 19 | 843 |
| Two passes, 4 per skeleton | 16 | 825 |
| Two passes, 5 per skeleton | 10 | 432 |
| Two passes, 6 per skeleton | 10 | 370 |
| Two passes, 8 per skeleton | 11 | 203 |
| Two passes, 10 per skeleton | 12 | 197 |

**4b2** · 1,584 DRs, 953 within-goal · at most 11 moves to HTR · 982 HTRs and 26 skeletons per DR (median) · reach 97.8%. One skeleton at a time puts the first solution at place 28 instead of 5. Of the two-pass orders, 3 per skeleton has the best median place (7), and 10 per skeleton needs the fewest HTRs for 95% (351, against 205 by HTR length).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| By HTR length | 5 | 205 |
| One skeleton at a time | 28 | 994 |
| Two passes, 2 per skeleton | 9 | 674 |
| Two passes, 3 per skeleton | 7 | 615 |
| Two passes, 4 per skeleton | 8 | 587 |
| Two passes, 5 per skeleton | 8 | 481 |
| Two passes, 6 per skeleton | 8 | 459 |
| Two passes, 8 per skeleton | 10 | 368 |
| Two passes, 10 per skeleton | 12 | 351 |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample) · at most 12 moves to HTR · 512 HTRs and 4 skeletons per DR (median) · reach 93.3%. One skeleton at a time puts the first solution at place 17 instead of 5. Of the two-pass orders, 3 per skeleton has the best median place (4).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| By HTR length | 5 | — |
| One skeleton at a time | 17 | — |
| Two passes, 2 per skeleton | 15 | — |
| Two passes, 3 per skeleton | 4 | — |
| Two passes, 4 per skeleton | 5 | — |
| Two passes, 5 per skeleton | 6 | — |
| Two passes, 6 per skeleton | 7 | — |
| Two passes, 8 per skeleton | 9 | — |
| Two passes, 10 per skeleton | 11 | — |

**2c3** · 1,048 DRs, 901 within-goal · at most 12 moves to HTR · 2,486.5 HTRs and 63 skeletons per DR (median) · reach 98.2%. One skeleton at a time puts the first solution at place 68 instead of 5. Of the two-pass orders, 2 per skeleton has the best median place (10), and 10 per skeleton needs the fewest HTRs for 95% (675, against 427 by HTR length).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| By HTR length | 5 | 427 |
| One skeleton at a time | 68 | 1,799 |
| Two passes, 2 per skeleton | 10 | 1,275 |
| Two passes, 3 per skeleton | 10 | 1,109 |
| Two passes, 4 per skeleton | 11 | 992 |
| Two passes, 5 per skeleton | 12 | 908 |
| Two passes, 6 per skeleton | 13 | 869 |
| Two passes, 8 per skeleton | 17 | 855 |
| Two passes, 10 per skeleton | 20 | 675 |

**4c3** · 851 DRs, 511 within-goal · at most 12 moves to HTR · 1,846 HTRs and 37 skeletons per DR (median) · reach 99.2%. One skeleton at a time puts the first solution at place 123 instead of 14. Of the two-pass orders, 3 per skeleton has the best median place (31), and 10 per skeleton needs the fewest HTRs for 95% (1,136, against 565 by HTR length).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| By HTR length | 14 | 565 |
| One skeleton at a time | 123 | 2,386 |
| Two passes, 2 per skeleton | 35 | 1,724 |
| Two passes, 3 per skeleton | 31 | 1,515 |
| Two passes, 4 per skeleton | 31 | 1,387 |
| Two passes, 5 per skeleton | 31 | 1,342 |
| Two passes, 6 per skeleton | 32 | 1,231 |
| Two passes, 8 per skeleton | 37 | 1,221 |
| Two passes, 10 per skeleton | 41 | 1,136 |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample) · at most 13 moves to HTR · 8,235 HTRs and 134 skeletons per DR (median) · reach 100.0%. One skeleton at a time puts the first solution at place 961 instead of 39. Of the two-pass orders, 2 per skeleton has the best median place (71), and 5 per skeleton needs the fewest HTRs for 95% (2,824, against 606 by HTR length).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| By HTR length | 39 | 606 |
| One skeleton at a time | 961 | 4,955 |
| Two passes, 2 per skeleton | 71 | 3,260 |
| Two passes, 3 per skeleton | 76 | 3,134 |
| Two passes, 4 per skeleton | 85 | 3,092 |
| Two passes, 5 per skeleton | 88 | 2,824 |
| Two passes, 6 per skeleton | 91 | 2,855 |
| Two passes, 8 per skeleton | 96 | 3,007 |
| Two passes, 10 per skeleton | 99 | 3,144 |

**2c4** · 1,243 DRs, 1,123 within-goal · at most 13 moves to HTR · 4,431 HTRs and 98 skeletons per DR (median) · reach 99.6%. One skeleton at a time puts the first solution at place 243 instead of 9. Of the two-pass orders, 2 per skeleton has the best median place (16), and 10 per skeleton needs the fewest HTRs for 95% (938, against 350 by HTR length).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| By HTR length | 9 | 350 |
| One skeleton at a time | 243 | 2,596 |
| Two passes, 2 per skeleton | 16 | 1,791 |
| Two passes, 3 per skeleton | 16 | 1,578 |
| Two passes, 4 per skeleton | 18 | 1,474 |
| Two passes, 5 per skeleton | 20 | 1,267 |
| Two passes, 6 per skeleton | 21 | 1,137 |
| Two passes, 8 per skeleton | 25 | 1,015 |
| Two passes, 10 per skeleton | 29 | 938 |

**4c4** · 691 DRs, 397 within-goal · at most 13 moves to HTR · 2,022 HTRs and 73 skeletons per DR (median) · reach 100.0%. One skeleton at a time puts the first solution at place 245 instead of 39. Of the two-pass orders, 3 per skeleton has the best median place (67), and 10 per skeleton needs the fewest HTRs for 95% (1,120, against 585 by HTR length).

| Order | Median place | HTRs to finish for 95% |
|---|---|---|
| By HTR length | 39 | 585 |
| One skeleton at a time | 245 | 2,236 |
| Two passes, 2 per skeleton | 69 | 1,695 |
| Two passes, 3 per skeleton | 67 | 1,536 |
| Two passes, 4 per skeleton | 78 | 1,491 |
| Two passes, 5 per skeleton | 84 | 1,374 |
| Two passes, 6 per skeleton | 90 | 1,344 |
| Two passes, 8 per skeleton | 97 | 1,142 |
| Two passes, 10 per skeleton | 102 | 1,120 |

## 2. Which HTRs: the choice of cap

This section compares three kinds of cap. All of them leave out the HTRs G moves away.

- **A cap on the moves.** Every HTR at most c moves away, whatever its extra moves. This is the standard meta's cap.
- **A cap on the extra moves.** Every HTR with P ≤ 1 and P+S+T ≤ k. The page uses k = 5.
- **Both.** P ≤ 1 and P+S+T ≤ k, and at most c moves away, for c under G−1.

The HTRs come from normal, inverse and the premove pass, as in section 1. How to read the columns:

- **HTRs per DR.** The HTRs the cap keeps, as a median over all the corner case's DRs, within-goal or not. It is what gets finished on a DR where nothing fits the goal.
- **Reach.** The share of within-goal DRs where at least one kept HTR has a finish within the goal.
- **Median place.** As in section 1, with the order chosen there: one skeleton at a time, two passes, 5 per skeleton in the first. A dash means fewer than half of the within-goal DRs are reached.

In each table the rows in bold are, for each kind of cap, the one with the fewest HTRs per DR that still reaches 95% of within-goal DRs. This table collects them.

| Corner case | Cap on the moves | Its HTRs per DR | Its reach | Cap on the extra moves | Its HTRs per DR | Its reach | Both | Their HTRs per DR | Their reach |
|---|---|---|---|---|---|---|---|---|---|
| 4b2 | 10 moves | 675 | 97.4% | P ≤ 1, P+S+T ≤ 4 | 674.5 | 95.9% | P ≤ 1, P+S+T ≤ 5, 10 moves | 404 | 95.0% |
| 4a2 | 10 moves | 280 | 95.0% | P ≤ 1, P+S+T ≤ 4 | 472 | 96.7% | P ≤ 1, P+S+T ≤ 4, 10 moves | 238 | 95.0% |
| 2c3 | 11 moves | 1,927 | 98.1% | P ≤ 1, P+S+T ≤ 4 | 1,612 | 95.9% | P ≤ 1, P+S+T ≤ 5, 11 moves | 1,080 | 96.2% |
| 4c3 | 12 moves | 2,560 | 99.8% | P ≤ 1, P+S+T ≤ 3 | 983 | 96.7% | — | — | — |
| 2c4 | 12 moves | 2,573 | 98.6% | P ≤ 1, P+S+T ≤ 3 | 2,351 | 96.5% | P ≤ 1, P+S+T ≤ 4, 12 moves | 1,328 | 97.8% |
| 0c3 | — | — | — | — | — | — | — | — | — |
| 0c4 | 12 moves | 2,708 | 98.5% | P ≤ 1, P+S+T ≤ 3 | 5,502 | 98.5% | P ≤ 1, P+S+T ≤ 3, 12 moves | 2,118.5 | 98.5% |
| 4c4 | 13 moves | 2,677 | 100.0% | P ≤ 1, P+S+T ≤ 3 | 1,887 | 99.0% | — | — | — |

A dash means no cap of that kind reaches 95%.

**Alone, neither cap wins everywhere.** At 95% reach, the cap on the extra moves needs fewer HTRs than the cap on the moves in 4 of the 6 corner cases with at least 100 within-goal DRs (2c3, 4c3, 2c4 and 4c4), and more in 1 (4a2): 38% to 169% as many.

**Together they need the fewest HTRs.** In 4 of those corner cases (4b2, 4a2, 2c3 and 2c4) the cap on the moves can go under G−1 with the cap on the extra moves in place and still leave 95% reach. The pair then keeps 56% to 85% of the HTRs of the better single cap. On 4c3 and 4c4 it cannot: G−2 moves reaches under 95% whatever the extra moves.

**The cap moves the first solution little.** Between the bold rows of a corner case, the median place differs by 10 at most (0c4: 78 to 88).

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal. The tightest caps with 95% reach: at most 10 moves (280 HTRs per DR); P ≤ 1, P+S+T ≤ 4 (472); and P ≤ 1, P+S+T ≤ 4 with at most 10 moves (238).

| Cap | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| At most 7 moves | 0 | 36.7% | — |
| At most 8 moves | 8 | 69.2% | 11 |
| At most 9 moves | 70 | 86.7% | 11 |
| **At most 10 moves** | **280** | **95.0%** | **10** |
| At most 11 moves | 610 | 97.5% | 10 |
| P ≤ 1, P+S+T ≤ 3 | 228.5 | 90.8% | 10 |
| **P ≤ 1, P+S+T ≤ 4** | **472** | **96.7%** | **10** |
| P ≤ 1, P+S+T ≤ 5 | 560 | 96.7% | 10 |
| P ≤ 1, P+S+T ≤ 6 | 560 | 97.5% | 10 |
| P ≤ 1 | 560 | 97.5% | 10 |
| **P ≤ 1, P+S+T ≤ 4, at most 10 moves** | **238** | **95.0%** | **10** |
| P ≤ 1, P+S+T ≤ 5, at most 10 moves | 272 | 95.0% | 10 |
| P ≤ 1, P+S+T ≤ 6, at most 10 moves | 272 | 95.0% | 10 |

**4b2** · 1,584 DRs, 953 within-goal. The tightest caps with 95% reach: at most 10 moves (675 HTRs per DR); P ≤ 1, P+S+T ≤ 4 (674.5); and P ≤ 1, P+S+T ≤ 5 with at most 10 moves (404).

| Cap | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| At most 7 moves | 6 | 55.0% | 7 |
| At most 8 moves | 33 | 71.5% | 7 |
| At most 9 moves | 159 | 88.4% | 8 |
| **At most 10 moves** | **675** | **97.4%** | **8** |
| At most 11 moves | 2,013 | 99.8% | 8 |
| P ≤ 1, P+S+T ≤ 3 | 375 | 86.5% | 9 |
| **P ≤ 1, P+S+T ≤ 4** | **674.5** | **95.9%** | **8** |
| P ≤ 1, P+S+T ≤ 5 | 982 | 97.8% | 8 |
| P ≤ 1, P+S+T ≤ 6 | 1,407.5 | 99.0% | 8 |
| P ≤ 1 | 1,604 | 99.1% | 8 |
| P ≤ 1, P+S+T ≤ 4, at most 10 moves | 279 | 93.3% | 8 |
| **P ≤ 1, P+S+T ≤ 5, at most 10 moves** | **404** | **95.0%** | **8** |
| P ≤ 1, P+S+T ≤ 6, at most 10 moves | 527 | 96.2% | 8 |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample). No cap reaches 95% of the within-goal DRs here, so no row is in bold.

| Cap | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| At most 8 moves | 0 | 33.3% | — |
| At most 9 moves | 0 | 66.7% | 6 |
| At most 10 moves | 32 | 66.7% | 6 |
| At most 11 moves | 188 | 80.0% | 6 |
| At most 12 moves | 512 | 93.3% | 6 |
| P ≤ 1, P+S+T ≤ 3 | 512 | 93.3% | 6 |
| P ≤ 1, P+S+T ≤ 4 | 512 | 93.3% | 6 |
| P ≤ 1, P+S+T ≤ 5 | 512 | 93.3% | 6 |
| P ≤ 1, P+S+T ≤ 6 | 512 | 93.3% | 6 |
| P ≤ 1 | 512 | 93.3% | 6 |
| P ≤ 1, P+S+T ≤ 4, at most 11 moves | 188 | 80.0% | 6 |
| P ≤ 1, P+S+T ≤ 5, at most 11 moves | 188 | 80.0% | 6 |
| P ≤ 1, P+S+T ≤ 6, at most 11 moves | 188 | 80.0% | 6 |

**2c3** · 1,048 DRs, 901 within-goal. The tightest caps with 95% reach: at most 11 moves (1,927 HTRs per DR); P ≤ 1, P+S+T ≤ 4 (1,612); and P ≤ 1, P+S+T ≤ 5 with at most 11 moves (1,080).

| Cap | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| At most 8 moves | 15 | 63.6% | 9 |
| At most 9 moves | 87 | 80.8% | 11 |
| At most 10 moves | 451 | 91.7% | 11 |
| **At most 11 moves** | **1,927** | **98.1%** | **11** |
| At most 12 moves | 6,584.5 | 100.0% | 11 |
| P ≤ 1, P+S+T ≤ 3 | 952 | 90.2% | 11 |
| **P ≤ 1, P+S+T ≤ 4** | **1,612** | **95.9%** | **12** |
| P ≤ 1, P+S+T ≤ 5 | 2,486.5 | 98.2% | 12 |
| P ≤ 1, P+S+T ≤ 6 | 3,396 | 99.0% | 12 |
| P ≤ 1 | 4,376 | 99.0% | 12 |
| P ≤ 1, P+S+T ≤ 4, at most 11 moves | 644 | 93.6% | 12 |
| **P ≤ 1, P+S+T ≤ 5, at most 11 moves** | **1,080** | **96.2%** | **12** |
| P ≤ 1, P+S+T ≤ 6, at most 11 moves | 1,356 | 96.6% | 12 |

**4c3** · 851 DRs, 511 within-goal. The tightest caps with 95% reach: at most 12 moves (2,560 HTRs per DR); and P ≤ 1, P+S+T ≤ 3 (983). With at most 11 moves no cap reaches 95%.

| Cap | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| At most 8 moves | 2 | 32.3% | — |
| At most 9 moves | 24 | 56.6% | 20 |
| At most 10 moves | 150 | 79.1% | 20 |
| At most 11 moves | 696 | 93.0% | 27 |
| **At most 12 moves** | **2,560** | **99.8%** | **29** |
| **P ≤ 1, P+S+T ≤ 3** | **983** | **96.7%** | **31** |
| P ≤ 1, P+S+T ≤ 4 | 1,659 | 99.2% | 31 |
| P ≤ 1, P+S+T ≤ 5 | 1,846 | 99.2% | 31 |
| P ≤ 1, P+S+T ≤ 6 | 1,846 | 99.2% | 31 |
| P ≤ 1 | 1,846 | 99.2% | 31 |
| P ≤ 1, P+S+T ≤ 4, at most 11 moves | 565 | 91.8% | 28 |
| P ≤ 1, P+S+T ≤ 5, at most 11 moves | 566 | 91.8% | 27 |
| P ≤ 1, P+S+T ≤ 6, at most 11 moves | 569 | 91.8% | 27 |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample). The tightest caps with 95% reach: at most 12 moves (2,708 HTRs per DR); P ≤ 1, P+S+T ≤ 3 (5,502); and P ≤ 1, P+S+T ≤ 3 with at most 12 moves (2,118.5).

| Cap | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| At most 9 moves | 6 | 18.2% | — |
| At most 10 moves | 70 | 51.5% | 75 |
| At most 11 moves | 501.5 | 77.3% | 65 |
| **At most 12 moves** | **2,708** | **98.5%** | **88** |
| At most 13 moves | 11,927 | 100.0% | 99 |
| **P ≤ 1, P+S+T ≤ 3** | **5,502** | **98.5%** | **86** |
| P ≤ 1, P+S+T ≤ 4 | 7,724 | 100.0% | 87 |
| P ≤ 1, P+S+T ≤ 5 | 8,235 | 100.0% | 87 |
| P ≤ 1, P+S+T ≤ 6 | 8,235 | 100.0% | 87 |
| P ≤ 1 | 8,235 | 100.0% | 87 |
| **P ≤ 1, P+S+T ≤ 3, at most 12 moves** | **2,118.5** | **98.5%** | **78** |
| P ≤ 1, P+S+T ≤ 4, at most 12 moves | 2,204.5 | 98.5% | 83 |
| P ≤ 1, P+S+T ≤ 5, at most 12 moves | 2,204.5 | 98.5% | 83 |
| P ≤ 1, P+S+T ≤ 6, at most 12 moves | 2,204.5 | 98.5% | 83 |

**2c4** · 1,243 DRs, 1,123 within-goal. The tightest caps with 95% reach: at most 12 moves (2,573 HTRs per DR); P ≤ 1, P+S+T ≤ 3 (2,351); and P ≤ 1, P+S+T ≤ 4 with at most 12 moves (1,328).

| Cap | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| At most 9 moves | 11 | 55.0% | 15 |
| At most 10 moves | 86 | 79.2% | 16 |
| At most 11 moves | 541 | 92.3% | 18 |
| **At most 12 moves** | **2,573** | **98.6%** | **19** |
| At most 13 moves | 9,810 | 100.0% | 20 |
| **P ≤ 1, P+S+T ≤ 3** | **2,351** | **96.5%** | **20** |
| P ≤ 1, P+S+T ≤ 4 | 3,521 | 99.3% | 21 |
| P ≤ 1, P+S+T ≤ 5 | 4,431 | 99.6% | 21 |
| P ≤ 1, P+S+T ≤ 6 | 5,325 | 99.6% | 21 |
| P ≤ 1 | 5,327 | 99.6% | 21 |
| **P ≤ 1, P+S+T ≤ 4, at most 12 moves** | **1,328** | **97.8%** | **20** |
| P ≤ 1, P+S+T ≤ 5, at most 12 moves | 1,609 | 97.9% | 20 |
| P ≤ 1, P+S+T ≤ 6, at most 12 moves | 1,612 | 97.9% | 20 |

**4c4** · 691 DRs, 397 within-goal. The tightest caps with 95% reach: at most 13 moves (2,677 HTRs per DR); and P ≤ 1, P+S+T ≤ 3 (1,887). With at most 12 moves no cap reaches 95%.

| Cap | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|
| At most 9 moves | 0 | 7.1% | — |
| At most 10 moves | 8 | 30.0% | — |
| At most 11 moves | 88 | 57.4% | 77 |
| At most 12 moves | 568 | 87.2% | 80 |
| **At most 13 moves** | **2,677** | **100.0%** | **84** |
| **P ≤ 1, P+S+T ≤ 3** | **1,887** | **99.0%** | **84** |
| P ≤ 1, P+S+T ≤ 4 | 2,022 | 100.0% | 83 |
| P ≤ 1, P+S+T ≤ 5 | 2,022 | 100.0% | 83 |
| P ≤ 1, P+S+T ≤ 6 | 2,022 | 100.0% | 83 |
| P ≤ 1 | 2,022 | 100.0% | 83 |
| P ≤ 1, P+S+T ≤ 4, at most 12 moves | 503 | 86.9% | 82 |
| P ≤ 1, P+S+T ≤ 5, at most 12 moves | 503 | 86.9% | 82 |
| P ≤ 1, P+S+T ≤ 6, at most 12 moves | 503 | 86.9% | 82 |

## 3. NISS

The HTRs above come from normal, inverse and the page's premove pass. The standard meta has a NISS of its own: one NISS after a start of 1 to 3 moves (a quarter turn; a side half turn and a quarter turn; a U-layer move, a side half turn and a quarter turn). This section counts what each adds, in the order of section 2: one skeleton at a time, two passes, 5 per skeleton in the first.

Where a NISS HTR goes in that order:

- **Its skeleton** is the one its whole solution is on when written on one side: the path, the finish, then the start undone. After a start, P, S and T are read on the skeleton of what is left, as in the premove pass, and the start's moves count in the moves to HTR.
- **After a single quarter turn**, the start is a premove: the HTR comes before the linear HTRs of its skeleton. The premove pass is this NISS on skeletons with 3 or more quarter turns, leaving out what the premove alone solves.
- **After a longer start**, the HTR comes after all the linear HTRs of its skeleton, and never in the first pass: the first pass is for the 5 nearest HTRs of the premove and the linear check.

### With the cap on the moves alone

This table has every HTR at most G−1 moves away, whatever its extra moves.

| Corner case | NISS | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|---|
| 4b2 | none | 1,661 | 98.7% | 8 |
| 4b2 | the premove pass | 2,013 | 99.8% | 8 |
| 4b2 | after 1 move | 2,074 | 99.8% | 8 |
| 4b2 | after up to 2 moves | 2,513 | 99.8% | 8 |
| 4b2 | after up to 3 moves | 2,762 | 99.8% | 8 |
| 4a2 | none | 500 | 95.8% | 10 |
| 4a2 | the premove pass | 610 | 97.5% | 10 |
| 4a2 | after 1 move | 616 | 97.5% | 9 |
| 4a2 | after up to 2 moves | 663 | 97.5% | 9 |
| 4a2 | after up to 3 moves | 745.5 | 97.5% | 9 |
| 2c3 | none | 4,947.5 | 99.2% | 18 |
| 2c3 | the premove pass | 6,584.5 | 100.0% | 11 |
| 2c3 | after 1 move | 6,584.5 | 100.0% | 11 |
| 2c3 | after up to 2 moves | 8,090 | 100.0% | 11 |
| 2c3 | after up to 3 moves | 9,024 | 100.0% | 11 |
| 4c3 | none | 1,994 | 97.8% | 58 |
| 4c3 | the premove pass | 2,560 | 99.8% | 29 |
| 4c3 | after 1 move | 2,560 | 99.8% | 29 |
| 4c3 | after up to 2 moves | 3,032 | 99.8% | 29 |
| 4c3 | after up to 3 moves | 3,403 | 99.8% | 29 |
| 2c4 | none | 7,052 | 99.3% | 26 |
| 2c4 | the premove pass | 9,810 | 100.0% | 19 |
| 2c4 | after 1 move | 9,810 | 100.0% | 19 |
| 2c4 | after up to 2 moves | 11,748 | 100.0% | 19 |
| 2c4 | after up to 3 moves | 13,705 | 100.0% | 19 |
| 0c3 | none | 512 | 86.7% | 134 |
| 0c3 | the premove pass | 512 | 93.3% | 6 |
| 0c3 | after 1 move | 512 | 93.3% | 6 |
| 0c3 | after up to 2 moves | 528 | 93.3% | 6 |
| 0c3 | after up to 3 moves | 548 | 93.3% | 6 |
| 0c4 | none | 7,974 | 100.0% | 156 |
| 0c4 | the premove pass | 11,927 | 100.0% | 98 |
| 0c4 | after 1 move | 11,927 | 100.0% | 98 |
| 0c4 | after up to 2 moves | 15,115 | 100.0% | 98 |
| 0c4 | after up to 3 moves | 16,791 | 100.0% | 98 |
| 4c4 | none | 1,889 | 92.7% | 148 |
| 4c4 | the premove pass | 2,677 | 100.0% | 85 |
| 4c4 | after 1 move | 2,677 | 100.0% | 85 |
| 4c4 | after up to 2 moves | 3,575 | 100.0% | 85 |
| 4c4 | after up to 3 moves | 4,039 | 100.0% | 85 |

### With the page's cap on the extra moves

This table has the HTRs with P ≤ 1 and P+S+T ≤ 5 that are at most G−1 moves away.

| Corner case | NISS | HTRs per DR (median) | Reach | Median place |
|---|---|---|---|---|
| 4b2 | none | 684.5 | 92.7% | 8 |
| 4b2 | the premove pass | 982 | 97.8% | 8 |
| 4b2 | after 1 move | 990.5 | 98.0% | 8 |
| 4b2 | after up to 2 moves | 1,258 | 98.5% | 8 |
| 4b2 | after up to 3 moves | 1,480.5 | 98.5% | 8 |
| 4a2 | none | 464 | 94.2% | 10 |
| 4a2 | the premove pass | 560 | 96.7% | 10 |
| 4a2 | after 1 move | 573 | 97.5% | 9 |
| 4a2 | after up to 2 moves | 607 | 97.5% | 9 |
| 4a2 | after up to 3 moves | 689 | 97.5% | 9 |
| 2c3 | none | 1,785 | 95.0% | 17 |
| 2c3 | the premove pass | 2,486.5 | 98.2% | 12 |
| 2c3 | after 1 move | 2,486.5 | 98.2% | 12 |
| 2c3 | after up to 2 moves | 3,164 | 98.7% | 12 |
| 2c3 | after up to 3 moves | 3,874 | 99.0% | 12 |
| 4c3 | none | 1,403 | 94.3% | 53 |
| 4c3 | the premove pass | 1,846 | 99.2% | 30 |
| 4c3 | after 1 move | 1,846 | 99.2% | 30 |
| 4c3 | after up to 2 moves | 2,226 | 99.2% | 30 |
| 4c3 | after up to 3 moves | 2,542 | 99.2% | 30 |
| 2c4 | none | 3,185 | 97.1% | 26 |
| 2c4 | the premove pass | 4,431 | 99.6% | 20 |
| 2c4 | after 1 move | 4,431 | 99.6% | 20 |
| 2c4 | after up to 2 moves | 5,478 | 99.6% | 20 |
| 2c4 | after up to 3 moves | 6,771 | 99.7% | 20 |
| 0c3 | none | 512 | 86.7% | 134 |
| 0c3 | the premove pass | 512 | 93.3% | 6 |
| 0c3 | after 1 move | 512 | 93.3% | 6 |
| 0c3 | after up to 2 moves | 528 | 93.3% | 6 |
| 0c3 | after up to 3 moves | 542 | 93.3% | 6 |
| 0c4 | none | 5,312 | 95.5% | 120 |
| 0c4 | the premove pass | 8,235 | 100.0% | 88 |
| 0c4 | after 1 move | 8,235 | 100.0% | 88 |
| 0c4 | after up to 2 moves | 10,631.5 | 100.0% | 88 |
| 0c4 | after up to 3 moves | 11,908 | 100.0% | 88 |
| 4c4 | none | 1,469 | 88.2% | 163 |
| 4c4 | the premove pass | 2,022 | 100.0% | 83 |
| 4c4 | after 1 move | 2,022 | 100.0% | 83 |
| 4c4 | after up to 2 moves | 2,774 | 100.0% | 83 |
| 4c4 | after up to 3 moves | 3,187 | 100.0% | 83 |

**A NISS after 1 move is the premove pass without its conditions.** Under the page's cap it keeps 1.00x to 1.02x the HTRs of the pass in the corner cases with at least 100 within-goal DRs, and moves the median place by 1 at most.

**A longer start adds HTRs and leaves the first solution where it is.** A NISS after up to 3 moves keeps 1.2x to 1.6x the HTRs of the premove pass under the page's cap, and 1.2x to 1.5x under the cap on the moves alone. The median place moves by 1 at most, since those HTRs come in the second pass. If they were let into the first pass of a skeleton with fewer than 5 other HTRs, the first solution would come later: on 0c4 at place 99 instead of 88.

## How it was counted

- **HTRs.** On both sides of every DR, every HTR in reach on a skeleton with the DR's quarter turns or two more; the HTRs of the premove pass; and in section 3 the HTRs after each NISS start, with the whole path on the DR's quarter turns or two more. In reach means the moves to HTR plus the corner moves left after it fit the goal. An HTR is one path up to how its U and D layer turns are written, with the best finish among those. Only the HTRs at most G−1 moves away are used.
- **The same HTRs as the page.** They are read from a list that also has, for each HTR, the skeleton of its whole solution. The list is checked against the page's records DR by DR: on normal and inverse it has the same HTRs, and its premove pass is the page's.
- **Moves to HTR.** The length of the path, a premove or the start before a NISS included.
- **Skeletons.** Two HTRs are on the same skeleton when they are on the same side and in the same corner case at every quarter turn. After a premove or another start, the corner cases are those of the whole solution written on the side of the path, which ends with the start undone. L is the skeleton's length.
- **Ties.** HTRs equally far go most pairs first, the pairs counted right after the last insertion as on the page. Skeletons of one length, and HTRs still tied, are taken in random order; every place is taken over 20 such orders.
- **Median place and HTRs for 95%.** The number of HTRs finished by which 50% and 95% of within-goal DRs have a within-goal finish, over the DRs and the random orders.
- **Finish.** The shortest leave-slice finish in half turns from the HTR, from an exact table.

