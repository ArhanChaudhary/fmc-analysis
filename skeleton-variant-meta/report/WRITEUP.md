# The skeleton/variant meta

24 Nov 2026

A meta for finding DR finishes within a certain goal move count, based on [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0).
The meta is based on the extra moves needed on top of a corner skeleton: any algorithm that solves corners, modulo corner swaps and rotations. Its length L is counted after removing any corner swaps.
The extra moves are broken down as in the doc:

 - **P**: Additional moves used to reach 2qt
 - **S**: Additional moves used to set up the 2qt trigger
 - **T**: Additional moves in the trigger
 - **N**: Additional moves after reaching HTR 

With L the length of the skeleton and G the goal, a solution has L+P+S+T+N moves, and G−L is the number of spare moves.

These stats use a goal of 12/13/14 moves for 2qt/3qt/4qt cases, counting the moves from DR to a leave-slice finish.

**What a skeleton looks like.** Between two quarter turns it has a single half turn, an X2 U2 Y2 sequence, or nothing. Before its first quarter turn it has nothing, X2, U2 X2 or X2 U2 Y2, and after its last one nothing, X2, X2 U2 or X2 U2 Y2 (X and Y are side faces on different axes). Whatever else a solution has is extra moves:

- `U R2 F2 U` is a 3-move skeleton with T=1. `R2 F2` is `R2` with a corner swap in it (`R2 F2 R2` then `R2`), so the skeleton is `U R2 U`.
- `U R2 U R2 F2 R2` is also a 3-move skeleton, with N=3.
- On the 4b2 DR `F2 D' L2 R2 U B2 D R2 D U2 L2`, the solution `L2 U B2 U' F2 D' F2 B2 U F2` has the 8-move skeleton `L2 U B2 U' F2 D' U F2` and T=2: the slice `F2 B2` sits between two quarter turns that have nothing between them in the skeleton (a cancelling pair).

Every corner solution of that shape is a skeleton, with its own L, so a DR has many of them (section 2 counts them). Every solution in these stats is read against its own skeleton, section by section (appendix C).

**The inverse reads a solution backwards**, so the values swap places:

| Skeleton | On normal | On inverse |
|---|---|---|
| 2qt | (S, T, N) | (N, T, S) |
| 3qt | (P, S, T, N) | (N, T, S, P) |
| 4qt | (P, P, S, T, N) | (N, T, S, P, P) |
| 5qt | (P, P, P, S, T, N) | (N, T, S, P, P, P) |

For example, on the 2c3 DR `F2 L2 F2 L2 R2 D' F2 D2 U' B2 D' R2`, the solution `B2 R2 U' B2 U R2 L2 F2 D' R2 L2 F2 B2` has a 6-move skeleton and reads (P, S, T, N) = (1, 0, 2, 4). Its inverse, `B2 F2 L2 R2 D F2 L2 R2 U' B2 U R2 B2`, solves the inverse scramble and reads (4, 2, 0, 1).

## 1. The meta

The standard meta, roughly speaking, is to spam HTRs whose length is not too far from the goal, on both normal and inverse.
You don't want too many extra moves early in the skeleton, and block building is of limited value, because preserving blocks is often incompatible
with the approach to HTR.  

Here, we formalize the meta in terms of skeletons and their variants. We quantify "not too far from the goal"
and "too many extra early moves" as follows:

1. **Sort the attempt's DRs by corner case**, shortest skeleton first, in the order of the table below.
2. **Within a DR, find the skeletons on normal and inverse.** Skeletons with two more quarter turns than the DR count too.
3. **For each skeleton, take the variants with P ≤ 1 and P+S+T ≤ 5 whose HTR is at most G−1 moves away.** At G moves there is no move left for a finish.
4. **Leave a variant to the other side when it comes earlier there.** A variant's early extra moves on one side are its late extra moves on the other, so each side only needs the variants with:
    - N ≥ S on a 2qt skeleton
    - N ≥ P on a 3qt skeleton
    - T+N ≥ P on a 4qt skeleton
    - S+T+N ≥ P on a 5qt skeleton
5. **Discard a variant when L+P+S+T+N > G**, where N is the bound's N, or the smallest N step 4 allows if that is larger.
6. **Finish the rest in order of moves to HTR, fewest first**, with the skeletons and the two sides mixed. Among HTRs equally far, take the ones with the most pairs first. Count the corner/edge pairs in the U and D layers right after the variant's last insertion, before the next quarter turn.

For example, a 2qt skeleton of 6 moves has 6 spare moves at goal 12. With step 4, a setup with S=2 can only take a trigger with T ≤ 2, and a setup with S=3 only T=0, whatever the bound says.

The pairs settle which of two HTRs equally far goes first. On the inverse of the 4b2 DR `R2 F2 D F2 R2 D U R2 U R2 B2`, `R2 F2 U L2 F2 D2 R2 U` and `R2 F2 U R2 B2 U2 R2 D'` are variants of the same 5-move skeleton, both with (S, T) = (1, 3), and both reach HTR in 8 moves. There are 8 pairs after `R2 F2 U L2 F2 D2 R2` and 6 after `R2 F2 U R2 B2 U2 R2`, so the first is finished first: `R2 B2` makes it 10 moves. The second can't be finished in fewer than 17.

**A skeleton that ends in HH gets a premove pass as well.** When a skeleton of 3 or more quarter turns ends with its last quarter turn (HH corners), apply that turn as a premove on the other side and NISS. What is left is a one-fewer-qt case with a goal one lower: take its variants with steps 2, 3 and 5. The premove counts as a move to HTR in steps 3 and 6. The skeleton is also checked linearly, as in the steps above. A skeleton that also starts with a quarter turn ends with one on both sides, and gets the pass on both.

Checking a skeleton linearly means going through its variants on the side it is on, with no premove, as in steps 3 to 5. The pass reads the same moves one section later: the last section before 2qt becomes the setup, the setup becomes the trigger, and the trigger becomes the finish. So it gets to solutions that have too many early extra moves on both sides. For example, on the 4b2 DR `U F2 D2 L2 U2 R2 D' L2 D' L2 B2 R2 U'`, the 12-move solution `U R2 B2 L2 U B2 D F2 R2 D2 F2 D` reads (P, P, S, T, N) = (0, 3, 0, 3, 0) on its 4qt skeleton, and the same on inverse: 3 extra moves before 2qt either way. With its last `D` as a premove, what is left reads (P, S, T, N) = (0, 3, 0, 2) on a 3qt skeleton, and steps 3 and 5 let it through.

This is the NISS rule of the Suggested Meta in [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0), with one difference. There the pass takes the place of checking that side linearly. Here the skeleton is still checked linearly as well, because the pass alone loses the solutions that go on after that quarter turn (section 2).

In the **baseline** meta, you do the same without DR Bounding: the only N you have is the one from step 4. The order of step 6 is the same.
Advanced DR Bounding adds a way to compute N. The stats below show the benefit of using it
to discard variants. 

The cap of step 3 was chosen by scoring every combination of up to three caps on S, T, N and their partial sums (appendix B). Step 4 cuts the HTRs to finish by 16%. It loses no within-goal DR of the sample. The best two or three caps together finish 5% fewer HTRs than P+S+T ≤ 5 alone without missing more in any corner case, and caps that include N, like S+T+N or T+N, give up more within-goal finishes than they save in HTRs.

### Corner cases

These stats are based on a random sample of 2qt/3qt/4qt DRs, 2,000 of each (1,960 for 2qt; see appendix C). This table gives the chance that 
a corner case has a within-goal solution, and the chance that the recommended meta will miss it.

| Corner case | Shortest skeleton length | Within-goal DRs | The meta misses a within-goal finish | DRs in the sample |
|---|---|---|---|---|
| 4b2 | 3 | 60.2% | 2.3% | 1,584 |
| 4a2 | 5 | 31.9% | 3.3% | 376 |
| 2c3 | 5 | 86.0% | 2.0% | 1,048 |
| 4c3 | 7 | 60.0% | 0.8% | 851 |
| 2c4 | 7 | 90.3% | 0.4% | 1,243 |
| 0c3 | 9 | 14.9% | 6.7% | 101 |
| 0c4 | 9 | 100.0% | 0.0% | 66 |
| 4c4 | 9 | 57.5% | 0.0% | 691 |

These are the misses with DR Bounding. The baseline misses up to 0.2 points less.
The misses come from the two caps of step 3. Of the 54 within-goal DRs the meta misses in the sample, a second move before 2qt is needed for 23, P+S+T of 6 or more for 21 and both for 0. Section 2 has the rest.
Extra moves before 2qt on normal are extra moves at the end on inverse, 
so a cap loses a DR when its solutions need two moves before 2qt on both sides, or more than 5 extra moves before HTR on both sides.
For example, the 2c3 DR `U L2 U B2 D2 B2 F2 L2 D L2 U F2 U' R2` has a 13-move solution on normal, `L2 U2 F2 L2 U R2 U L2 U' F2 D2 F2 B2`, which reads (P, S, T, N) = (2, 0, 0, 2) on its 9-move skeleton. On inverse, the nearest it gets is `F2 B2 U2 B2 U R2 U' L2 U' R2 B2 D2 L2`, which reads (2, 0, 0, 2) on a 9-move skeleton: 2 extra moves before 2qt again. The meta finds neither, with or without a premove.

## 2. Stats for the recommended meta

Filtering by the DR Bounding lower limit **reduces the number of HTRs to check by 11-18x**, with only a negligible change in missed within-goal finishes.

The stats below use the "corner-case-aware" bound from [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0), without the reflection penalty (which would improve the numbers). See the doc for details.

How to read the columns:

- **HTRs to finish per DR.** The variants the search finishes, as a median over all the case's DRs, within-goal or not.
- **Within goal.** The share of those HTRs whose finish fits the goal.
- **Chance of missing a within-goal finish.** The share of within-goal DRs where none of them does.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal · 10 skeletons and 42 routes to 2qt per DR (median, both searches). The bound finishes 14× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 281 | 1 in 427 | 3.3% |
| **Corner-case-aware** | 20 | 1 in 39 | 3.3% |

**4b2** · 1,584 DRs, 953 within-goal · 24 skeletons and 159 routes to 2qt per DR (median, both searches). The bound finishes 12× fewer HTRs with a chance of missing 0.1 points higher.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 746 | 1 in 379 | 2.2% |
| **Corner-case-aware** | 62 | 1 in 34 | 2.3% |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample) · 4 skeletons and 14 routes to 2qt per DR (median, both searches). The bound finishes 18× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 320 | 1 in 847 | 6.7% |
| **Corner-case-aware** | 18 | 1 in 64 | 6.7% |

**2c3** · 1,048 DRs, 901 within-goal · 53 skeletons and 520 routes to 2qt per DR (median, both searches). The bound finishes 11× fewer HTRs with a chance of missing 0.2 points higher.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 2,224 | 1 in 371 | 1.8% |
| **Corner-case-aware** | 195 | 1 in 36 | 2.0% |

**4c3** · 851 DRs, 511 within-goal · 31 skeletons and 301 routes to 2qt per DR (median, both searches). The bound finishes 15× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 1,645 | 1 in 536 | 0.8% |
| **Corner-case-aware** | 108 | 1 in 43 | 0.8% |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample) · 104 skeletons and 1,426 routes to 2qt per DR (median, both searches). The bound finishes 16× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 7,609 | 1 in 793 | 0.0% |
| **Corner-case-aware** | 490 | 1 in 57 | 0.0% |

**2c4** · 1,243 DRs, 1,123 within-goal · 76 skeletons and 1,078 routes to 2qt per DR (median, both searches). The bound finishes 12× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 4,109 | 1 in 525 | 0.4% |
| **Corner-case-aware** | 338 | 1 in 43 | 0.4% |

**4c4** · 691 DRs, 397 within-goal · 56 skeletons and 667 routes to 2qt per DR (median, both searches). The bound finishes 15× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 1,796 | 1 in 736 | 0.0% |
| **Corner-case-aware** | 117 | 1 in 52 | 0.0% |

### Where the misses come from

Skeletons with two more quarter turns are part of the meta. Without them, 4b2 would miss 36.4% of the time instead of 2.3%, and 4c4 30.7% instead of 0.0%. Skeletons with four more quarter turns would save at most 3 within-goal DRs in any corner case.

Each missed DR is filed under what its nearest within-goal HTR breaks, on the side where it breaks the least, in the premove pass or linearly. Cells are shares of within-goal DRs, and the five columns on the right add up to the meta's chance of missing, up to rounding.

**Error in DR Bound** counts DRs lost because the corner-case-aware table asks +5 for RD or FD corners with 1 bad slice and cs/fr 1/1, where +4 is enough. For example, on the inverse of the 2c3 DR `B2 D' R2 D L2 R2 B2 D R2 D2 B2 R2 U2`, `B2 U' B2 U R2 L2 B2 D` reaches HTR in that case in 8 moves and `R2 U2 F2 L2 D2` finishes in 5, 13 in all. That reads (0, 0, 2, 4) on a 7-move skeleton, but the bound says N ≥ 5, which makes 14.

| Corner case | Missed with only the DR's own quarter turns | Missed | Needs a second pre-2qt move | Needs P+S+T of 6 or more | Needs both | Error in DR Bound | Needs four more quarter turns |
|---|---|---|---|---|---|---|---|
| 4a2 | 21.7% | 3.3% | 0.0% | 0.8% | 0.0% | 0.0% | 2.5% |
| 4b2 | 36.4% | 2.3% | 0.7% | 1.3% | 0.0% | 0.1% | 0.2% |
| 0c3 | 6.7% | 6.7% | 0.0% | 0.0% | 0.0% | 0.0% | 6.7% |
| 2c3 | 10.3% | 2.0% | 1.0% | 0.8% | 0.0% | 0.2% | 0.0% |
| 4c3 | 24.3% | 0.8% | 0.6% | 0.0% | 0.0% | 0.0% | 0.2% |
| 0c4 | 6.1% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| 2c4 | 2.8% | 0.4% | 0.4% | 0.1% | 0.0% | 0.0% | 0.0% |
| 4c4 | 30.7% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### What the cap on the moves to HTR changes

An HTR that is G moves away is within goal only when it solves the DR as it stands. Step 3 leaves those out. That takes 26% to 41% off the HTRs to finish, and loses no within-goal DR of the sample: every DR with such a solution has a nearer within-goal HTR that the meta finishes. Without the premove pass it would lose 151.

This table shows the meta with the corner-case-aware bound, with HTRs at any distance and with the cap.

| Corner case | HTRs to finish per DR, any distance (median) | HTRs to finish per DR, at most G−1 moves (median) | Within-goal DRs lost |
|---|---|---|---|
| 4b2 | 88 | 62 | 0 |
| 4a2 | 34 | 20 | 0 |
| 2c3 | 264 | 195 | 0 |
| 4c3 | 152 | 108 | 0 |
| 2c4 | 483 | 338 | 0 |
| 0c3 | 28 | 18 | 0 |
| 0c4 | 766 | 490 | 0 |
| 4c4 | 178 | 117 | 0 |

### What the premove pass changes

The pass finds within-goal DRs that the linear check misses under the caps: 198 of the sample's 4,086. Without it the meta would miss 252 of them (6.2%), and with it 54 (1.3%). With the pass in place of the linear check of that side, as the doc has it, it would miss 163 (4.0%): 185 gained and 96 lost.

This table shows the chance of missing a within-goal finish in the three versions. Lost and gained count within-goal DRs against the meta with no pass.

| Corner case | Within-goal DRs | Missed, no pass | Missed, pass instead of linear | Lost, pass instead of linear | Gained by the pass | Missed, pass and linear (the meta) |
|---|---|---|---|---|---|---|
| 4b2 | 953 | 8.0% | 4.0% | 14 | 54 | 2.3% |
| 4a2 | 120 | 5.8% | 4.2% | 1 | 3 | 3.3% |
| 2c3 | 901 | 5.2% | 4.4% | 19 | 29 | 2.0% |
| 4c3 | 511 | 5.9% | 8.0% | 37 | 26 | 0.8% |
| 2c4 | 1,123 | 2.9% | 1.7% | 13 | 28 | 0.4% |
| 0c3 | 15 | 13.3% | 13.3% | 1 | 1 | 6.7% |
| 0c4 | 66 | 6.1% | 1.5% | 1 | 4 | 0.0% |
| 4c4 | 397 | 13.4% | 4.3% | 10 | 53 | 0.0% |
| All | 4,086 | 6.2% | 4.0% | 96 | 198 | 1.3% |

**Why the pass alone loses DRs.** What is left after the premove only holds the solutions that end on that quarter turn. A solution that goes on after it, with a slice or a corner swap, is not among them, and on the other side those moves come before 2qt. All 96 lost DRs are of that kind: every within-goal solution the linear check finds for them has 2 to 4 moves after the last quarter turn of a skeleton that ends in HH. For example, on the 4c3 DR `B2 U' R2 B2 D2 F2 D' R2 B2 U' L2 R2`, the only within-goal solution the meta finishes is `B2 U' R2 B2 D2 F2 U' B2 L2 D' R2 L2` on inverse, which reads (P, S, T, N) = (0, 1, 1, 2). Its skeleton ends with the `D'`, and the slice `R2 L2` comes after. On normal it reads (P, S, T, N) = (2, 1, 1, 0): 2 extra moves before 2qt, so it isn't found there. With the `D'` as a premove, what is left has no solution within the goal.

This table shows the work and how soon a finish is found: the HTRs to finish per DR (median), and the chance of a within-goal finish among the first 10 HTRs finished, in the order of the last table of this section.

| Corner case | HTRs to finish, no pass | HTRs to finish, pass instead of linear | HTRs to finish, pass and linear | Within 10, no pass | Within 10, pass instead of linear | Within 10, pass and linear |
|---|---|---|---|---|---|---|
| 4b2 | 42 | 53 | 62 | 71% | 73% | 74% |
| 4a2 | 15 | 17 | 20 | 78% | 77% | 80% |
| 2c3 | 135 | 153 | 195 | 66% | 67% | 69% |
| 4c3 | 78 | 85 | 108 | 55% | 57% | 61% |
| 2c4 | 237 | 268 | 338 | 56% | 63% | 63% |
| 0c3 | 16 | 16 | 18 | 40% | 67% | 73% |
| 0c4 | 325 | 400 | 490 | 34% | 32% | 37% |
| 4c4 | 78 | 95 | 117 | 44% | 47% | 51% |

### Where the skeletons and routes come from

Most of a DR's skeletons have two more quarter turns than the DR, and that is where most routes to 2qt are. Some of those have a cancelling pair: two quarter turns with nothing between them in the skeleton, like the `D' U` of the example at the top. The counts are medians per DR over both sides, before the bound, so the parts don't add up exactly to the totals of the tables above. The routes of the premove pass are counted too, under the quarter turns of the whole skeleton, premove included. A left-over skeleton that again ends with its last quarter turn counts as a cancelling pair, since the premove comes right after that turn. Skeletons are counted in the linear check only.

| Corner case | Skeletons, own quarter turns | Skeletons, two more, no cancelling pair | Skeletons, two more, cancelling pair | Routes to 2qt, own quarter turns | Routes to 2qt, two more, no cancelling pair | Routes to 2qt, two more, cancelling pair | Missed without the cancelling pairs |
|---|---|---|---|---|---|---|---|
| 4a2 | 2 | 0 | 8 | 2 | 0 | 39 | 20.8% |
| 4b2 | 2 | 14 | 9 | 2 | 98 | 54 | 13.3% |
| 0c3 | 2 | 0 | 0 | 8 | 0 | 0 | 6.7% |
| 2c3 | 6 | 31 | 16 | 64 | 292 | 154 | 4.6% |
| 4c3 | 4 | 23 | 4 | 24 | 208 | 64 | 4.9% |
| 0c4 | 22 | 82 | 0 | 392 | 846 | 176 | 0.0% |
| 2c4 | 15 | 49 | 12 | 417 | 507 | 141 | 0.8% |
| 4c4 | 6 | 50 | 0 | 106 | 526 | 10 | 0.5% |

### Found within K finishes

Here are the chances of finding a within-goal solution within the first several HTRs, in the order of step 6: fewest moves to HTR first, and the most pairs first among HTRs equally far.

Compared to the baseline, using DR bounding boosts the chances of success within 10 or 20 finishes by 1.1x-1.8x.

The order is the same in every table of this page, and it is the standard meta's; only what is discarded changes. [HTR search order and limits](STANDARD-META.md) compares it with going through one skeleton at a time, compares the caps of step 3 with a cap on the moves to HTR alone, and looks at what more NISS would add.

| Corner case | Meta, within 5 | Meta, within 10 | Meta, within 20 | Baseline, within 5 | Baseline, within 10 | Baseline, within 20 |
|---|---|---|---|---|---|---|
| 4b2 | 60% | 74% | 86% | 52% | 62% | 72% |
| 4a2 | 55% | 80% | 88% | 43% | 63% | 72% |
| 2c3 | 55% | 69% | 80% | 50% | 61% | 72% |
| 4c3 | 48% | 61% | 78% | 36% | 45% | 57% |
| 2c4 | 46% | 63% | 77% | 40% | 53% | 66% |
| 0c3 | 73% | 73% | 80% | 52% | 60% | 72% |
| 0c4 | 28% | 37% | 55% | 21% | 28% | 38% |
| 4c4 | 35% | 51% | 71% | 21% | 29% | 40% |

## Appendix A. Varying the bound

[*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0) doc 
defines three estimates for the lower bound: simple, corner-case-aware, and comprehensive. We have chosen
the middle one. Each level prunes the HTRs by a factor of roughly 2x, at the cost of more complicated recognition,
but the biggest jump is between using any type of DR Bounding vs. none.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal. Corner-case-aware makes a finished HTR 11.1× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 281 | 1 in 427 | 3.3% |
| Simple | 43 | 1 in 94 | 8.3% |
| **Corner-case-aware** | 20 | 1 in 39 | 3.3% |
| Comprehensive | 11 | 1 in 20 | 3.3% |

**4b2** · 1,584 DRs, 953 within-goal. Corner-case-aware makes a finished HTR 11.1× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 746 | 1 in 379 | 2.2% |
| Simple | 154 | 1 in 82 | 2.3% |
| **Corner-case-aware** | 62 | 1 in 34 | 2.3% |
| Comprehensive | 32 | 1 in 18 | 2.2% |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample). Corner-case-aware makes a finished HTR 13.3× likelier to be within goal than the baseline does; comprehensive adds 2.0× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 320 | 1 in 847 | 6.7% |
| Simple | 64 | 1 in 171 | 6.7% |
| **Corner-case-aware** | 18 | 1 in 64 | 6.7% |
| Comprehensive | 4 | 1 in 32 | 6.7% |

**2c3** · 1,048 DRs, 901 within-goal. Corner-case-aware makes a finished HTR 10.4× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 2,224 | 1 in 371 | 1.8% |
| Simple | 451 | 1 in 81 | 1.9% |
| **Corner-case-aware** | 195 | 1 in 36 | 2.0% |
| Comprehensive | 100 | 1 in 19 | 1.8% |

**4c3** · 851 DRs, 511 within-goal. Corner-case-aware makes a finished HTR 12.5× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 1,645 | 1 in 536 | 0.8% |
| Simple | 286 | 1 in 113 | 1.6% |
| **Corner-case-aware** | 108 | 1 in 43 | 0.8% |
| Comprehensive | 53 | 1 in 22 | 0.8% |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample). Corner-case-aware makes a finished HTR 13.9× likelier to be within goal than the baseline does; comprehensive adds 2.0× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 7,609 | 1 in 793 | 0.0% |
| Simple | 1,402 | 1 in 170 | 0.0% |
| **Corner-case-aware** | 490 | 1 in 57 | 0.0% |
| Comprehensive | 241 | 1 in 29 | 0.0% |

**2c4** · 1,243 DRs, 1,123 within-goal. Corner-case-aware makes a finished HTR 12.2× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 4,109 | 1 in 525 | 0.4% |
| Simple | 864 | 1 in 112 | 0.8% |
| **Corner-case-aware** | 338 | 1 in 43 | 0.4% |
| Comprehensive | 175 | 1 in 22 | 0.4% |

**4c4** · 691 DRs, 397 within-goal. Corner-case-aware makes a finished HTR 14.1× likelier to be within goal than the baseline does; comprehensive adds 2.0× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 1,796 | 1 in 736 | 0.0% |
| Simple | 353 | 1 in 152 | 0.0% |
| **Corner-case-aware** | 117 | 1 in 52 | 0.0% |
| Comprehensive | 59 | 1 in 26 | 0.0% |

## Appendix B. Varying the caps

The cap on P+S+T of step 3 and the rule of step 4 come from a sweep. A rule is P ≤ 1, the goal, at most G−1 moves to HTR, step 4 on or off, and up to three caps taken from S, T, N, P+S, S+T, T+N, P+S+T, S+T+N and P+S+T+N, each set to anything from 0 to 8: 128,468 rules in all. Each one was scored on every corner case with the corner-case-aware bound.

This table compares a few of them with the rule that has no cap and no step 4. HTRs to finish is the mean per DR as a share of that rule's, averaged over the six corner cases with at least 100 within-goal DRs (a geometric mean). Extra misses are points added to the chance of missing a within-goal finish.

| Rule on top of P ≤ 1 and the goal | HTRs to finish, against no cap | Extra misses, average | Extra misses, worst corner case |
|---|---|---|---|
| Step 4 | 81% | +0.0 points | +0.0 points |
| Step 4, P+S+T ≤ 6 | 76% | +0.0 points | +0.1 points (4b2) |
| **Step 4, P+S+T ≤ 5** | 68% | +0.5 points | +1.3 points (4b2) |
| Step 4, P+S+T ≤ 4 | 56% | +1.2 points | +3.1 points (4b2) |
| Step 4, the best two caps that miss no more than the meta in any corner case (S ≤ 3, T ≤ 5) | 65% | +0.5 points | +1.0 points (2c3) |
| Step 4, the best three caps that miss no more than the meta in any corner case (S ≤ 3, T ≤ 5, S+T ≤ 6) | 65% | +0.5 points | +1.0 points (2c3) |
| Step 4, the best single cap that includes N and misses no more than the meta (S+T+N ≤ 7) | 79% | +0.2 points | +1.2 points (4b2) |
| Step 4, S+T+N ≤ 5 | 64% | +3.0 points | +11.1 points (4b2) |
| Step 4, T+N ≤ 4 | 65% | +3.0 points | +11.3 points (4b2) |
| P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 75% | +2.8 points | +10.1 points (4b2) |

What the sweep says:

- **Step 4 costs nothing.** With P+S+T ≤ 5 in place, it loses no within-goal DR of the sample. With no cap it loses no within-goal DR.
- **One cap on P+S+T is enough.** Among the rules that miss no more than the meta in any corner case, the best with two or three caps finishes 5% fewer HTRs than P+S+T ≤ 5 alone (the two rows of the table that name them).
- **Caps that include N don't pay.** N is read off the bound at 2qt for free, and a variant with a big N is already discarded by the goal. S+T+N ≤ 5 and T+N ≤ 4 finish about as many HTRs as P+S+T ≤ 5, and miss 12.2% and 12.4% of the time on 4b2 instead of 2.3%: a short skeleton leaves room for a long finish.
- **Finer caps don't help either.** The sweep's caps are the same for every skeleton. Caps on P+S+T that change with the spare moves, with P, with the skeleton's quarter turns or with the bound's N, and arbitrary sets of (quarter turns, spare moves, P, S, T, N), were fitted on half of the DRs and scored on the other half, over 8 random splits. At the misses of P+S+T ≤ 5, the single cap finishes 84% of the HTRs that step 4 alone does on the held-out half, and the finer rules 84% to 89%.

The tables below show the stats of each corner case with different caps, using the corner-case-aware bound. The meta's row is in bold. Skeletons and routes to 2qt are counted before the bound, so they only change with the caps.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal. P+S+T ≤ 4 misses no more often (3.3%); a second pre-2qt move finds nothing more, for 20 HTRs instead of 20 and 44 routes to 2qt instead of 42.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 11 | 60 | 28 | 1 in 46 | 2.5% |
| P ≤ 1, step 4 | 10 | 42 | 20 | 1 in 40 | 2.5% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 10 | 40 | 16 | 1 in 32 | 9.2% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 10 | 42 | 20 | 1 in 35 | 3.3% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **10** | **42** | **20** | **1 in 39** | **3.3%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 10 | 42 | 20 | 1 in 40 | 2.5% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 11 | 60 | 28 | 1 in 45 | 3.3% |
| P = 0, step 4, P+S+T ≤ 5 | 9 | 37 | 16 | 1 in 37 | 5.0% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 10 | 44 | 20 | 1 in 39 | 3.3% |
| Any P, step 4, P+S+T ≤ 5 | 10 | 44 | 20 | 1 in 39 | 3.3% |
| P ≤ 1, step 4, T+N ≤ 4 | 10 | 42 | 19 | 1 in 36 | 6.7% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 10 | 42 | 20 | 1 in 39 | 4.2% |
| The meta on skeletons with 2 or more spare moves | 10 | 41 | 19 | 1 in 38 | 4.2% |
| The meta with P = 0 on skeletons with two more quarter turns | 9 | 37 | 16 | 1 in 37 | 5.0% |
| The meta without skeletons that have a cancelling pair | 2 | 2 | 8 | 1 in 34 | 20.8% |
| The meta on skeletons with the DR's own quarter turns only | 2 | 2 | 7 | 1 in 34 | 21.7% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 11 | 60 | 28 | 1 in 45 | 3.3% |

**4b2** · 1,584 DRs, 953 within-goal. P+S+T ≤ 4 misses 4.2% of the time instead of 2.3%; a second pre-2qt move takes it to 1.6%, for 67 HTRs instead of 62 and 198 routes to 2qt instead of 159.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 25 | 192 | 103 | 1 in 43 | 1.0% |
| P ≤ 1, step 4 | 24 | 159 | 64 | 1 in 38 | 1.0% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 23 | 130 | 34 | 1 in 28 | 13.5% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 24 | 156 | 52 | 1 in 32 | 4.2% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **24** | **159** | **62** | **1 in 34** | **2.3%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 24 | 159 | 64 | 1 in 35 | 1.2% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 25 | 192 | 81 | 1 in 36 | 2.3% |
| P = 0, step 4, P+S+T ≤ 5 | 23 | 79 | 46 | 1 in 32 | 7.9% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 26 | 198 | 67 | 1 in 35 | 1.6% |
| Any P, step 4, P+S+T ≤ 5 | 26 | 243 | 70 | 1 in 36 | 1.6% |
| P ≤ 1, step 4, T+N ≤ 4 | 24 | 158 | 53 | 1 in 37 | 12.4% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 24 | 159 | 53 | 1 in 37 | 12.2% |
| The meta on skeletons with 2 or more spare moves | 21 | 151 | 60 | 1 in 34 | 2.9% |
| The meta with P = 0 on skeletons with two more quarter turns | 23 | 79 | 46 | 1 in 32 | 7.9% |
| The meta without skeletons that have a cancelling pair | 16 | 99 | 42 | 1 in 29 | 13.3% |
| The meta on skeletons with the DR's own quarter turns only | 2 | 2 | 13 | 1 in 20 | 36.4% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 25 | 192 | 68 | 1 in 38 | 11.1% |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample). P+S+T ≤ 4 misses no more often (6.7%); a second pre-2qt move changes nothing.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 4 | 16 | 24 | 1 in 66 | 6.7% |
| P ≤ 1, step 4 | 4 | 14 | 18 | 1 in 64 | 6.7% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 4 | 14 | 18 | 1 in 63 | 6.7% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 4 | 14 | 18 | 1 in 64 | 6.7% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **4** | **14** | **18** | **1 in 64** | **6.7%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 4 | 14 | 18 | 1 in 64 | 6.7% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 4 | 16 | 24 | 1 in 66 | 6.7% |
| P = 0, step 4, P+S+T ≤ 5 | 4 | 8 | 16 | 1 in 59 | 6.7% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 4 | 14 | 18 | 1 in 64 | 6.7% |
| Any P, step 4, P+S+T ≤ 5 | 4 | 14 | 18 | 1 in 64 | 6.7% |
| P ≤ 1, step 4, T+N ≤ 4 | 4 | 14 | 18 | 1 in 64 | 6.7% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 4 | 14 | 18 | 1 in 64 | 6.7% |
| The meta on skeletons with 2 or more spare moves | 1 | 6 | 0 | 1 in 54 | 13.3% |
| The meta with P = 0 on skeletons with two more quarter turns | 4 | 14 | 18 | 1 in 63 | 6.7% |
| The meta without skeletons that have a cancelling pair | 2 | 8 | 16 | 1 in 62 | 6.7% |
| The meta on skeletons with the DR's own quarter turns only | 2 | 8 | 16 | 1 in 61 | 6.7% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 4 | 16 | 24 | 1 in 66 | 6.7% |

**2c3** · 1,048 DRs, 901 within-goal. P+S+T ≤ 4 misses 4.3% of the time instead of 2.0%; a second pre-2qt move takes it to 1.0%, for 213 HTRs instead of 195 and 696 routes to 2qt instead of 520.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 55 | 590 | 288 | 1 in 44 | 1.2% |
| P ≤ 1, step 4 | 53 | 521 | 266 | 1 in 43 | 1.2% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 51 | 449 | 89 | 1 in 29 | 10.0% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 52 | 515 | 141 | 1 in 32 | 4.3% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **53** | **520** | **195** | **1 in 36** | **2.0%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 53 | 521 | 246 | 1 in 39 | 1.2% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 55 | 590 | 210 | 1 in 37 | 2.0% |
| P = 0, step 4, P+S+T ≤ 5 | 50 | 230 | 138 | 1 in 34 | 8.2% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 58 | 696 | 213 | 1 in 36 | 1.0% |
| Any P, step 4, P+S+T ≤ 5 | 58 | 904 | 231 | 1 in 37 | 1.0% |
| P ≤ 1, step 4, T+N ≤ 4 | 53 | 521 | 226 | 1 in 42 | 2.9% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 53 | 521 | 162 | 1 in 38 | 5.5% |
| The meta on skeletons with 2 or more spare moves | 35 | 454 | 187 | 1 in 35 | 2.2% |
| The meta with P = 0 on skeletons with two more quarter turns | 51 | 275 | 166 | 1 in 33 | 3.6% |
| The meta without skeletons that have a cancelling pair | 37 | 360 | 164 | 1 in 33 | 4.6% |
| The meta on skeletons with the DR's own quarter turns only | 6 | 64 | 124 | 1 in 30 | 10.3% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 55 | 590 | 172 | 1 in 38 | 6.1% |

**4c3** · 851 DRs, 511 within-goal. P+S+T ≤ 4 misses no more often (0.8%); a second pre-2qt move takes it to 0.4%, for 117 HTRs instead of 108 and 351 routes to 2qt instead of 301.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 33 | 339 | 119 | 1 in 44 | 0.8% |
| P ≤ 1, step 4 | 31 | 301 | 108 | 1 in 43 | 0.8% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 31 | 284 | 78 | 1 in 36 | 3.3% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 31 | 300 | 104 | 1 in 40 | 0.8% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **31** | **301** | **108** | **1 in 43** | **0.8%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 31 | 301 | 108 | 1 in 43 | 0.8% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 33 | 339 | 118 | 1 in 44 | 0.8% |
| P = 0, step 4, P+S+T ≤ 5 | 30 | 134 | 78 | 1 in 41 | 9.4% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 32 | 351 | 117 | 1 in 43 | 0.4% |
| Any P, step 4, P+S+T ≤ 5 | 32 | 375 | 118 | 1 in 43 | 0.2% |
| P ≤ 1, step 4, T+N ≤ 4 | 31 | 301 | 107 | 1 in 43 | 1.2% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 31 | 301 | 107 | 1 in 44 | 1.2% |
| The meta on skeletons with 2 or more spare moves | 20 | 266 | 103 | 1 in 42 | 3.3% |
| The meta with P = 0 on skeletons with two more quarter turns | 30 | 149 | 89 | 1 in 41 | 5.3% |
| The meta without skeletons that have a cancelling pair | 26 | 237 | 98 | 1 in 42 | 4.9% |
| The meta on skeletons with the DR's own quarter turns only | 4 | 24 | 62 | 1 in 40 | 24.3% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 33 | 339 | 117 | 1 in 45 | 1.2% |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample). P+S+T ≤ 4 misses no more often (0.0%); a second pre-2qt move finds nothing more, for 535 HTRs instead of 490 and 1,818 routes to 2qt instead of 1,426.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 108 | 1,714 | 529 | 1 in 59 | 0.0% |
| P ≤ 1, step 4 | 104 | 1,426 | 490 | 1 in 57 | 0.0% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 104 | 1,392 | 381 | 1 in 54 | 1.5% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 104 | 1,424 | 490 | 1 in 57 | 0.0% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **104** | **1,426** | **490** | **1 in 57** | **0.0%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 104 | 1,426 | 490 | 1 in 57 | 0.0% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 108 | 1,714 | 529 | 1 in 59 | 0.0% |
| P = 0, step 4, P+S+T ≤ 5 | 99 | 602 | 288 | 1 in 56 | 6.1% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 124 | 1,818 | 535 | 1 in 55 | 0.0% |
| Any P, step 4, P+S+T ≤ 5 | 124 | 2,006 | 578 | 1 in 57 | 0.0% |
| P ≤ 1, step 4, T+N ≤ 4 | 104 | 1,426 | 490 | 1 in 58 | 0.0% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 104 | 1,426 | 490 | 1 in 57 | 0.0% |
| The meta on skeletons with 2 or more spare moves | 38 | 1,081 | 452 | 1 in 56 | 0.0% |
| The meta with P = 0 on skeletons with two more quarter turns | 99 | 859 | 445 | 1 in 57 | 1.5% |
| The meta without skeletons that have a cancelling pair | 104 | 1,234 | 480 | 1 in 58 | 0.0% |
| The meta on skeletons with the DR's own quarter turns only | 22 | 392 | 396 | 1 in 56 | 6.1% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 108 | 1,714 | 529 | 1 in 59 | 0.0% |

**2c4** · 1,243 DRs, 1,123 within-goal. P+S+T ≤ 4 misses 0.7% of the time instead of 0.4%; a second pre-2qt move takes it to 0.1%, for 389 HTRs instead of 338 and 1,434 routes to 2qt instead of 1,078.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 78 | 1,242 | 398 | 1 in 46 | 0.4% |
| P ≤ 1, step 4 | 76 | 1,080 | 374 | 1 in 45 | 0.4% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 76 | 980 | 194 | 1 in 38 | 3.5% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 76 | 1,060 | 271 | 1 in 41 | 0.7% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **76** | **1,078** | **338** | **1 in 43** | **0.4%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 76 | 1,080 | 374 | 1 in 45 | 0.4% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 78 | 1,241 | 358 | 1 in 44 | 0.4% |
| P = 0, step 4, P+S+T ≤ 5 | 74 | 464 | 191 | 1 in 41 | 8.5% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 81 | 1,434 | 389 | 1 in 43 | 0.1% |
| Any P, step 4, P+S+T ≤ 5 | 81 | 1,751 | 423 | 1 in 44 | 0.1% |
| P ≤ 1, step 4, T+N ≤ 4 | 76 | 1,080 | 347 | 1 in 45 | 0.8% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 76 | 1,080 | 338 | 1 in 45 | 0.6% |
| The meta on skeletons with 2 or more spare moves | 37 | 836 | 318 | 1 in 42 | 1.2% |
| The meta with P = 0 on skeletons with two more quarter turns | 74 | 739 | 311 | 1 in 42 | 0.7% |
| The meta without skeletons that have a cancelling pair | 65 | 927 | 319 | 1 in 42 | 0.8% |
| The meta on skeletons with the DR's own quarter turns only | 15 | 417 | 274 | 1 in 40 | 2.8% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 78 | 1,241 | 341 | 1 in 45 | 1.0% |

**4c4** · 691 DRs, 397 within-goal. P+S+T ≤ 4 misses no more often (0.0%); a second pre-2qt move finds nothing more, for 128 HTRs instead of 117 and 796 routes to 2qt instead of 667.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 58 | 774 | 131 | 1 in 53 | 0.0% |
| P ≤ 1, step 4 | 56 | 667 | 117 | 1 in 52 | 0.0% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 56 | 664 | 114 | 1 in 50 | 1.0% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 56 | 667 | 117 | 1 in 52 | 0.0% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **56** | **667** | **117** | **1 in 52** | **0.0%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 56 | 667 | 117 | 1 in 52 | 0.0% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 58 | 774 | 131 | 1 in 53 | 0.0% |
| P = 0, step 4, P+S+T ≤ 5 | 54 | 314 | 70 | 1 in 51 | 10.6% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 59 | 796 | 128 | 1 in 53 | 0.0% |
| Any P, step 4, P+S+T ≤ 5 | 59 | 850 | 133 | 1 in 53 | 0.0% |
| P ≤ 1, step 4, T+N ≤ 4 | 56 | 667 | 117 | 1 in 52 | 0.3% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 56 | 667 | 117 | 1 in 52 | 0.0% |
| The meta on skeletons with 2 or more spare moves | 14 | 383 | 93 | 1 in 51 | 12.8% |
| The meta with P = 0 on skeletons with two more quarter turns | 54 | 375 | 92 | 1 in 52 | 5.5% |
| The meta without skeletons that have a cancelling pair | 56 | 627 | 116 | 1 in 52 | 0.5% |
| The meta on skeletons with the DR's own quarter turns only | 6 | 106 | 68 | 1 in 52 | 30.7% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 58 | 774 | 131 | 1 in 53 | 0.0% |

## Appendix C. Data and method

Every number above comes from an exhaustive search of random DRs, with each HTR's finish taken from an exact table.

- **Sample.** 2,000 uniformly random DR states each with 2, 3 and 4 quarter turns to HTR. 40 of the 2qt states are 0c0 up to a turn of both layers and are dropped, leaving 1,960.
- **Search.** On both sides, every HTR in reach with the DR's quarter turns or two more, up to 6. In reach means the moves to HTR plus the corner moves left after it fit the goal. That's 53,654,751 HTRs, and the premove pass adds 11,378,756. Of those, 31,990,225 are at most G−1 moves away. Every table is counted on these, with its own caps on top.
- **Finish.** The shortest leave-slice finish in half turns from that HTR, from an exact table. An HTR is within goal when its moves plus that finish fit the goal.
- **Reading a solution.** A solution is cut at its quarter turns into sections. The skeleton of a section is the fewest half turns that do the same to the corners, up to a corner swap of the side axes (`R2 F2 R2`), a slice, and a U2 or D2 next to a quarter turn, which only turns that quarter turn the other way. L is the quarter turns plus those moves, and a section's extra moves are its length minus its skeleton's. P is the extra moves of the sections before 2qt, S of the setup at 2qt, T of the trigger and N of the finish. Two HTRs are on the same skeleton when they are in the same corner case at every quarter turn.
- **Checks of that reading.** On 20,965 skeletons (the first 100 DRs of each sample), L is the length of the shortest corner-only path through the same corner cases at each quarter turn. All 2,898 within-goal solutions of those DRs read as mirror images on normal and inverse. Over the whole sample, all but 10 of the 47,122 within-goal HTRs have their mirror image among the other side's HTRs.
- **Step 4 on a 6qt skeleton.** S+T+N ≥ P, not counting an extra move in the skeleton's middle section, which the inverse also reads as its middle.
- **Premove pass.** On each side, a quarter turn is made first on the other side, and every HTR of what is left is listed on skeletons with one quarter turn fewer than the DR or one more, so the whole skeleton, premove included, has the DR's quarter turns or two more. The premove is made all four ways, on the U or the D layer and in either direction. The same paths reach HTR each time, so a path counts as one HTR with the best of its four finishes. P, S, T and N are read on the left-over skeleton, with the cap, the bound and the goal as in steps 3 and 5. L and the solution's length count the premove. Step 4 is not applied, because only one side of what is left is searched. A left-over skeleton that again ends with its last quarter turn is gone through like any other, with no second premove. A left-over path that is solved at its last quarter turn is left out: with the premove it ends on two U/D quarter turns in a row, which is a solution of the skeleton two quarter turns shorter. A skeleton that starts and ends with a quarter turn gets the pass on both sides. A solution that ends on its last quarter turn is reached twice, in the pass and linearly, and counts as an HTR in each.
- **Pairs.** A pair is a corner and an edge next to each other in the U or D layer with both stickers matching, so there are 0 to 16. A variant's pairs are counted right after its last insertion: on the state just before the quarter turn that closes its last section with extra moves, or just before its last quarter turn when it has no extra moves. A quarter turn of U or D keeps the count, and so does turning D where the variant turns U. Every pair count printed on this page was counted again on the stickers.
- **Order of finishing.** By moves to HTR, fewest first, over all the DR's skeletons on both sides and the premove pass, whose premove counts as a move. Among HTRs equally far, the ones with the most pairs go first. Ties are taken in random order, and the found-within-K shares are averages over 20 such orders.
- **Routes to 2qt.** Distinct move sequences, on either side, up to the point where the skeleton has 2 quarter turns left, that lead to at least one HTR the table's limits allow. They're counted before any bound, so they don't depend on it.
- **Skeletons.** Counted the same way: the skeletons with at least one HTR the table's limits allow, before any bound. They are counted in the linear check only: a skeleton of the premove pass is a skeleton of the DR with its last quarter turn made first.

### Changes from the 19 Nov version

- **P is its own number**, as in the doc. Before, the moves before 2qt were counted inside S.
- **Every solution is read against its own skeleton.** Before, extra moves were counted against the shortest corner path with the same quarter turns and the same NISS@1qt corner case, so a solution on a longer corner route looked like a variant with extra moves, often before 2qt. Now that route is a skeleton of its own, with a longer L and fewer spare moves. More solutions fit P ≤ 1 this way, so, before the premove pass and the cap on the moves to HTR, the meta misses less (4b2 4.0% instead of 8.2%, 2c3 3.6% instead of 6.9%) and has more routes to 2qt to go through (4b2 148 instead of 77, 2c3 578 instead of 169).
- **Step 4 is new.**
- **The order of finishing is new.** HTRs are finished by moves to HTR, fewest first, and the most pairs first among HTRs equally far. Before, the skeletons were gone through shortest first and each skeleton's variants by fewest P+S+T, at most 3 per skeleton in a first pass. On the HTRs the meta finishes now, that order finds a within-goal finish within 10 for 61% of 4b2's within-goal DRs and 53% of 2c3's, and the new one for 74% and 69% (69% and 64% without the pairs).
- **The premove pass is new.** With the cap on the moves to HTR in place, it takes the chance of missing from 8.0% to 2.3% on 4b2 and from 5.2% to 2.0% on 2c3, and the HTRs to finish per DR from 42 to 62 and from 135 to 195 (section 2).
- **The cap on the moves to HTR is new.** HTRs G moves away are left out. It takes the HTRs to finish per DR from 88 to 62 on 4b2 and from 264 to 195 on 2c3, and loses no within-goal DR of the sample (section 2).

### Left out of the meta

- **Reflection penalties.** The doc's "+2 per reflected slice" terms aren't tracked here.
- **cs-parity.** Only the comprehensive bound needs it, and checking it during a solve is slow.
