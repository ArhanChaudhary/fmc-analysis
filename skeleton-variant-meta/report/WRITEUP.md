# The skeleton/variant meta

23 Nov 2026

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
2. **Within a DR, sort skeletons by length**, normal and inverse mixed. Skeletons with two more quarter turns than the DR count too, and sort in by length with the rest.
3. **For each skeleton, go through the variants with P ≤ 1 and P+S+T ≤ 5**, fewest P+S+T first, and in increasing order of (P, S, T, N) among those.
4. **Leave a variant to the other side when it comes earlier there.** A variant's early extra moves on one side are its late extra moves on the other, so each side only needs the variants with:
    - N ≥ S on a 2qt skeleton
    - N ≥ P on a 3qt skeleton
    - T+N ≥ P on a 4qt skeleton
    - S+T+N ≥ P on a 5qt skeleton
5. **Discard a variant when L+P+S+T+N > G**, where N is the bound's N, or the smallest N step 4 allows if that is larger. Finish the rest.

For example, a 2qt skeleton of 6 moves has 6 spare moves at goal 12. With step 4, a setup with S=2 can only take a trigger with T ≤ 2, and a setup with S=3 only T=0, whatever the bound says.

In the **baseline** meta, you do the same without DR Bounding: the only N you have is the one from step 4.
Advanced DR Bounding adds a way to compute N. The stats below show the benefit of using it
to discard variants. 

The cap of step 3 was chosen by scoring every combination of up to three caps on S, T, N and their partial sums (appendix B). Step 4 is free: with P+S+T ≤ 5 in place it loses no within-goal DR of the sample, and it cuts the HTRs to finish by 22%. No two or three caps together do better than P+S+T ≤ 5 alone without missing more in some corner case, and caps that include N, like S+T+N or T+N, give up more within-goal finishes than they save in HTRs.

### Corner cases

These stats are based on a random sample of 2qt/3qt/4qt DRs, 2,000 of each (1,960 for 2qt; see appendix C). This table gives the chance that 
a corner case has a within-goal solution, and the chance that the recommended meta will miss it.

| Corner case | Shortest skeleton length | Within-goal DRs | The meta misses a within-goal finish | DRs in the sample |
|---|---|---|---|---|
| 4b2 | 3 | 60.2% | 4.0% | 1,584 |
| 4a2 | 5 | 31.9% | 3.3% | 376 |
| 2c3 | 5 | 86.0% | 3.6% | 1,048 |
| 4c3 | 7 | 60.0% | 1.4% | 851 |
| 2c4 | 7 | 90.3% | 1.2% | 1,243 |
| 0c3 | 9 | 14.9% | 6.7% | 101 |
| 0c4 | 9 | 100.0% | 0.0% | 66 |
| 4c4 | 9 | 57.5% | 1.5% | 691 |

As we'll see below, the miss percentages do not depend on whether you use DR Bounding to prune the search.
Instead, they come from the two caps of step 3, in about equal parts. Extra moves before 2qt on normal are extra moves at the end on inverse, 
so a DR is missed when its solutions need two of them on both sides, or more than 5 extra moves before HTR on both sides.
For example, the 2c3 DR `U' B2 F2 U B2 D R2 F2 U F2 R2 D2 U'` has a 12-move solution on normal, `U' L2 B2 U' B2 L2 U' R2 U' R2 L2 D`, which reads (P, S, T, N) = (2, 0, 2, 0) on its 8-move skeleton. On inverse, the nearest it gets is `U' F2 B2 U B2 D R2 F2 D R2 B2 D`, which reads (2, 1, 1, 0) on an 8-move skeleton: 2 extra moves before 2qt again. The meta finds neither.

## 2. Stats for the recommended meta

Filtering by the DR Bounding lower limit **reduces the number of HTRs to check by 13-21x**, with only a negligible increase in missed within-goal finishes.

The stats below use the "corner-case-aware" bound from [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0), without the reflection penalty (which would improve the numbers). See the doc for details.

How to read the columns:

- **HTRs to finish per DR.** The variants the search finishes, as a median over all the case's DRs, within-goal or not.
- **Within goal.** The share of those HTRs whose finish fits the goal.
- **Chance of missing a within-goal finish.** The share of within-goal DRs where none of them does.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal · 11 skeletons and 58 routes to 2qt per DR (median, both searches). The bound finishes 16× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 355 | 1 in 518 | 3.3% |
| **Corner-case-aware** | 22 | 1 in 43 | 3.3% |

**4b2** · 1,584 DRs, 953 within-goal · 25 skeletons and 148 routes to 2qt per DR (median, both searches). The bound finishes 13× fewer HTRs with a chance of missing 0.1 points higher.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 784 | 1 in 469 | 3.9% |
| **Corner-case-aware** | 60 | 1 in 38 | 4.0% |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample) · 4 skeletons and 16 routes to 2qt per DR (median, both searches). The bound finishes 21× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 512 | 1 in 1,899 | 6.7% |
| **Corner-case-aware** | 24 | 1 in 110 | 6.7% |

**2c3** · 1,048 DRs, 901 within-goal · 58 skeletons and 578 routes to 2qt per DR (median, both searches). The bound finishes 13× fewer HTRs with a chance of missing 0.2 points higher.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 2,359 | 1 in 506 | 3.3% |
| **Corner-case-aware** | 179 | 1 in 42 | 3.6% |

**4c3** · 851 DRs, 511 within-goal · 33 skeletons and 310 routes to 2qt per DR (median, both searches). The bound finishes 16× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 1,826 | 1 in 861 | 1.4% |
| **Corner-case-aware** | 113 | 1 in 59 | 1.4% |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample) · 116 skeletons and 1,423 routes to 2qt per DR (median, both searches). The bound finishes 16× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 9,008 | 1 in 1,307 | 0.0% |
| **Corner-case-aware** | 554 | 1 in 85 | 0.0% |

**2c4** · 1,243 DRs, 1,123 within-goal · 95 skeletons and 1,230 routes to 2qt per DR (median, both searches). The bound finishes 14× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 5,104 | 1 in 825 | 1.2% |
| **Corner-case-aware** | 356 | 1 in 58 | 1.2% |

**4c4** · 691 DRs, 397 within-goal · 71 skeletons and 777 routes to 2qt per DR (median, both searches). The bound finishes 16× fewer HTRs with no change in the chance of missing.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 2,257 | 1 in 1,275 | 1.5% |
| **Corner-case-aware** | 138 | 1 in 79 | 1.5% |

### Where the misses come from

Skeletons with two more quarter turns are part of the meta. Without them, 4b2 would miss 36.4% of the time instead of 4.0%, and 4c4 30.7% instead of 1.5%. Skeletons with four more quarter turns would save at most 3 DRs in any case.

Each missed DR is filed under what its nearest within-goal HTR breaks, on the side where it breaks the least. Cells are shares of within-goal DRs, and the five columns on the right add up to the meta's chance of missing, up to rounding.

**Error in DR Bound** counts DRs lost because the corner-case-aware table asks +5 for RD or FD corners with 1 bad slice and cs/fr 1/1, where +4 is enough. For example, on the inverse of the 2c3 DR `B2 D' R2 D L2 R2 B2 D R2 D2 B2 R2 U2`, `B2 U' B2 U R2 L2 B2 D` reaches HTR in that case in 8 moves and `R2 U2 F2 L2 D2` finishes in 5, 13 in all. That reads (0, 0, 2, 4) on a 7-move skeleton, but the bound says N ≥ 5, which makes 14.

| Corner case | Missed with only the DR's own quarter turns | Missed | Needs a second pre-2qt move | Needs P+S+T of 6 or more | Needs both | Error in DR Bound | Needs four more quarter turns |
|---|---|---|---|---|---|---|---|
| 4a2 | 21.7% | 3.3% | 0.0% | 0.8% | 0.0% | 0.0% | 2.5% |
| 4b2 | 36.4% | 4.0% | 2.0% | 1.6% | 0.1% | 0.1% | 0.2% |
| 0c3 | 6.7% | 6.7% | 0.0% | 0.0% | 0.0% | 0.0% | 6.7% |
| 2c3 | 12.3% | 3.6% | 1.4% | 1.9% | 0.0% | 0.2% | 0.0% |
| 4c3 | 25.0% | 1.4% | 0.6% | 0.6% | 0.0% | 0.0% | 0.2% |
| 0c4 | 6.1% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| 2c4 | 3.3% | 1.2% | 0.7% | 0.4% | 0.0% | 0.0% | 0.0% |
| 4c4 | 30.7% | 1.5% | 1.5% | 0.0% | 0.0% | 0.0% | 0.0% |

### Where the skeletons and routes come from

Most of a DR's skeletons have two more quarter turns than the DR, and that is where most routes to 2qt are. Some of those have a cancelling pair: two quarter turns with nothing between them in the skeleton, like the `D' U` of the example at the top. The counts are medians per DR over both sides, before the bound, so the parts don't add up exactly to the totals of the tables above.

| Corner case | Skeletons, own quarter turns | Skeletons, two more, no cancelling pair | Skeletons, two more, cancelling pair | Routes to 2qt, own quarter turns | Routes to 2qt, two more, no cancelling pair | Routes to 2qt, two more, cancelling pair | Missed without the cancelling pairs |
|---|---|---|---|---|---|---|---|
| 4a2 | 2 | 0 | 9 | 2 | 0 | 54 | 20.8% |
| 4b2 | 2 | 14 | 10 | 2 | 97 | 44 | 13.4% |
| 0c3 | 2 | 0 | 0 | 8 | 0 | 0 | 6.7% |
| 2c3 | 6 | 33 | 19 | 63 | 337 | 151 | 6.2% |
| 4c3 | 4 | 24 | 6 | 24 | 238 | 60 | 5.5% |
| 0c4 | 22 | 92 | 3 | 410 | 992 | 18 | 0.0% |
| 2c4 | 15 | 63 | 17 | 436 | 630 | 144 | 1.5% |
| 4c4 | 6 | 65 | 0 | 109 | 661 | 0 | 1.5% |

### Found within K finishes

Here are the chances of finding a within-goal solution within the first several HTRs. The order of HTRs is by skeleton length first, then fewest P+S+T, then (P, S, T, N), checking up to 3 HTRs per skeleton in a first pass, then looping back through the skeletons until the limit is reached.

Compared to the baseline, using DR bounding boosts the chances of success within 10 or 20 finishes by 1.3x-4.0x.

| Corner case | Meta, within 5 | Meta, within 10 | Meta, within 20 | Baseline, within 5 | Baseline, within 10 | Baseline, within 20 |
|---|---|---|---|---|---|---|
| 4b2 | 48% | 59% | 73% | 41% | 47% | 52% |
| 4a2 | 40% | 55% | 76% | 23% | 29% | 36% |
| 2c3 | 33% | 49% | 63% | 26% | 39% | 48% |
| 4c3 | 25% | 38% | 53% | 13% | 18% | 24% |
| 2c4 | 24% | 40% | 60% | 16% | 27% | 40% |
| 0c3 | 17% | 22% | 32% | 6% | 7% | 8% |
| 0c4 | 18% | 27% | 36% | 8% | 13% | 16% |
| 4c4 | 17% | 28% | 42% | 6% | 10% | 14% |

## Appendix A. Varying the bound

[*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0) doc 
defines three estimates for the lower bound: simple, corner-case-aware, and comprehensive. We have chosen
the middle one. Each level prunes the HTRs by a factor of roughly 2x, at the cost of more complicated recognition,
but the biggest jump is between using any type of DR Bounding vs. none.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal. Corner-case-aware makes a finished HTR 12.2× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 355 | 1 in 518 | 3.3% |
| Simple | 46 | 1 in 101 | 8.3% |
| **Corner-case-aware** | 22 | 1 in 43 | 3.3% |
| Comprehensive | 10 | 1 in 22 | 3.3% |

**4b2** · 1,584 DRs, 953 within-goal. Corner-case-aware makes a finished HTR 12.2× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 784 | 1 in 469 | 3.9% |
| Simple | 137 | 1 in 84 | 4.0% |
| **Corner-case-aware** | 60 | 1 in 38 | 4.0% |
| Comprehensive | 32 | 1 in 21 | 3.9% |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample). Corner-case-aware makes a finished HTR 17.2× likelier to be within goal than the baseline does; comprehensive adds 2.0× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 512 | 1 in 1,899 | 6.7% |
| Simple | 80 | 1 in 271 | 6.7% |
| **Corner-case-aware** | 24 | 1 in 110 | 6.7% |
| Comprehensive | 4 | 1 in 55 | 6.7% |

**2c3** · 1,048 DRs, 901 within-goal. Corner-case-aware makes a finished HTR 12.0× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 2,359 | 1 in 506 | 3.3% |
| Simple | 394 | 1 in 91 | 3.4% |
| **Corner-case-aware** | 179 | 1 in 42 | 3.6% |
| Comprehensive | 91 | 1 in 22 | 3.3% |

**4c3** · 851 DRs, 511 within-goal. Corner-case-aware makes a finished HTR 14.7× likelier to be within goal than the baseline does; comprehensive adds 2.0× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 1,826 | 1 in 861 | 1.4% |
| Simple | 269 | 1 in 144 | 2.5% |
| **Corner-case-aware** | 113 | 1 in 59 | 1.4% |
| Comprehensive | 55 | 1 in 30 | 1.4% |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample). Corner-case-aware makes a finished HTR 15.4× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 9,008 | 1 in 1,307 | 0.0% |
| Simple | 1,321 | 1 in 208 | 0.0% |
| **Corner-case-aware** | 554 | 1 in 85 | 0.0% |
| Comprehensive | 274 | 1 in 44 | 0.0% |

**2c4** · 1,243 DRs, 1,123 within-goal. Corner-case-aware makes a finished HTR 14.3× likelier to be within goal than the baseline does; comprehensive adds 2.0× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 5,104 | 1 in 825 | 1.2% |
| Simple | 817 | 1 in 138 | 1.5% |
| **Corner-case-aware** | 356 | 1 in 58 | 1.2% |
| Comprehensive | 180 | 1 in 29 | 1.2% |

**4c4** · 691 DRs, 397 within-goal. Corner-case-aware makes a finished HTR 16.2× likelier to be within goal than the baseline does; comprehensive adds 2.0× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|
| Baseline (no DR Bounding) | 2,257 | 1 in 1,275 | 1.5% |
| Simple | 358 | 1 in 188 | 1.5% |
| **Corner-case-aware** | 138 | 1 in 79 | 1.5% |
| Comprehensive | 67 | 1 in 39 | 1.5% |

## Appendix B. Varying the caps

The cap of step 3 and the rule of step 4 come from a sweep. A rule is P ≤ 1, the goal, step 4 on or off, and up to three caps taken from S, T, N, P+S, S+T, T+N, P+S+T, S+T+N and P+S+T+N, each set to anything from 0 to 8: 128,468 rules in all. Each one was scored on every corner case with the corner-case-aware bound.

This table compares a few of them with the rule that has no cap and no step 4. HTRs to finish is the mean per DR as a share of that rule's, averaged over the six corner cases with at least 100 within-goal DRs (a geometric mean). Extra misses are points added to the chance of missing a within-goal finish.

| Rule on top of P ≤ 1 and the goal | HTRs to finish, against no cap | Extra misses, average | Extra misses, worst corner case |
|---|---|---|---|
| Step 4 | 73% | +0.0 points | +0.1 points (4b2) |
| Step 4, P+S+T ≤ 6 | 64% | +0.1 points | +0.3 points (2c3) |
| **Step 4, P+S+T ≤ 5** | 55% | +0.9 points | +1.9 points (2c3) |
| Step 4, P+S+T ≤ 4 | 42% | +2.5 points | +5.4 points (4b2) |
| Step 4, the best single cap that includes N and misses no more than the meta (S+T+N ≤ 7) | 68% | +0.2 points | +1.3 points (4b2) |
| Step 4, S+T+N ≤ 5 | 52% | +3.5 points | +11.2 points (4b2) |
| Step 4, T+N ≤ 4 | 55% | +3.2 points | +11.5 points (4b2) |
| P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 66% | +3.4 points | +10.3 points (4b2) |

What the sweep says:

- **Step 4 costs nothing.** With P+S+T ≤ 5 it loses no within-goal DR of the sample. With no cap it loses 1 of the sample's 4,086 within-goal DRs: a 4b2 whose mirror image runs into the bound's too-strict cell (section 2).
- **One cap on P+S+T is enough.** Among the rules that miss no more than the meta in any corner case, none with two or three caps finishes fewer HTRs than P+S+T ≤ 5 alone.
- **Caps that include N don't pay.** N is read off the bound at 2qt for free, and a variant with a big N is already discarded by the goal. S+T+N ≤ 5 and T+N ≤ 4 finish about as many HTRs as P+S+T ≤ 5, and miss 13.5% and 13.9% of the time on 4b2 instead of 4.0%: a short skeleton leaves room for a long finish.
- **Finer caps don't help either.** The sweep's caps are the same for every skeleton. Caps on P+S+T that change with the spare moves, with P, with the skeleton's quarter turns or with the bound's N, and arbitrary sets of (quarter turns, spare moves, P, S, T, N), were fitted on half of the DRs and scored on the other half, over 8 random splits. At the misses of P+S+T ≤ 5, the single cap finishes 75% of the HTRs that step 4 alone does on the held-out half, and the finer rules 79% to 85%.

The tables below show the stats of each corner case with different caps, using the corner-case-aware bound. The meta's row is in bold. Routes to 2qt are counted before the bound, so they only change with the caps.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal. P+S+T ≤ 4 misses no more often (3.3%); a second pre-2qt move changes nothing.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 12 | 78 | 33 | 1 in 59 | 2.5% |
| P ≤ 1, step 4 | 11 | 58 | 22 | 1 in 46 | 2.5% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 10 | 42 | 15 | 1 in 32 | 10.8% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 11 | 58 | 20 | 1 in 37 | 3.3% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **11** | **58** | **22** | **1 in 43** | **3.3%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 11 | 58 | 22 | 1 in 46 | 2.5% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 12 | 78 | 33 | 1 in 55 | 3.3% |
| P = 0, step 4, P+S+T ≤ 5 | 10 | 42 | 18 | 1 in 40 | 5.8% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 11 | 58 | 22 | 1 in 43 | 3.3% |
| Any P, step 4, P+S+T ≤ 5 | 11 | 58 | 22 | 1 in 43 | 3.3% |
| P ≤ 1, step 4, T+N ≤ 4 | 11 | 58 | 20 | 1 in 40 | 6.7% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 11 | 58 | 22 | 1 in 43 | 4.2% |
| The meta on skeletons with 2 or more spare moves | 10 | 56 | 20 | 1 in 42 | 4.2% |
| The meta with P = 0 on skeletons with two more quarter turns | 10 | 42 | 18 | 1 in 40 | 5.8% |
| The meta without skeletons that have a cancelling pair | 2 | 2 | 8 | 1 in 37 | 20.8% |
| The meta on skeletons with the DR's own quarter turns only | 2 | 2 | 7 | 1 in 35 | 21.7% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 12 | 78 | 33 | 1 in 55 | 3.3% |

**4b2** · 1,584 DRs, 953 within-goal. P+S+T ≤ 4 misses 7.7% of the time instead of 4.0%; a second pre-2qt move takes it to 2.0%, for 66 HTRs instead of 60 and 179 routes to 2qt instead of 148.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 26 | 206 | 119 | 1 in 58 | 2.3% |
| P ≤ 1, step 4 | 25 | 148 | 64 | 1 in 48 | 2.4% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 24 | 117 | 29 | 1 in 29 | 20.6% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 24 | 144 | 48 | 1 in 35 | 7.7% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **25** | **148** | **60** | **1 in 38** | **4.0%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 25 | 148 | 64 | 1 in 40 | 2.5% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 26 | 206 | 83 | 1 in 40 | 4.0% |
| P = 0, step 4, P+S+T ≤ 5 | 24 | 74 | 44 | 1 in 34 | 11.4% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 27 | 179 | 66 | 1 in 40 | 2.0% |
| Any P, step 4, P+S+T ≤ 5 | 27 | 181 | 66 | 1 in 40 | 1.9% |
| P ≤ 1, step 4, T+N ≤ 4 | 25 | 147 | 53 | 1 in 44 | 13.9% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 25 | 148 | 53 | 1 in 43 | 13.5% |
| The meta on skeletons with 2 or more spare moves | 21 | 137 | 60 | 1 in 38 | 4.6% |
| The meta with P = 0 on skeletons with two more quarter turns | 24 | 74 | 44 | 1 in 34 | 11.4% |
| The meta without skeletons that have a cancelling pair | 16 | 99 | 44 | 1 in 33 | 13.4% |
| The meta on skeletons with the DR's own quarter turns only | 2 | 2 | 13 | 1 in 20 | 36.4% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 26 | 206 | 69 | 1 in 44 | 12.6% |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample). P+S+T ≤ 4 misses no more often (6.7%); a second pre-2qt move changes nothing.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 4 | 28 | 32 | 1 in 113 | 6.7% |
| P ≤ 1, step 4 | 4 | 16 | 24 | 1 in 110 | 6.7% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 4 | 16 | 24 | 1 in 108 | 13.3% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 4 | 16 | 24 | 1 in 110 | 6.7% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **4** | **16** | **24** | **1 in 110** | **6.7%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 4 | 16 | 24 | 1 in 110 | 6.7% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 4 | 28 | 32 | 1 in 113 | 6.7% |
| P = 0, step 4, P+S+T ≤ 5 | 4 | 10 | 16 | 1 in 105 | 6.7% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 4 | 16 | 24 | 1 in 110 | 6.7% |
| Any P, step 4, P+S+T ≤ 5 | 4 | 16 | 24 | 1 in 110 | 6.7% |
| P ≤ 1, step 4, T+N ≤ 4 | 4 | 16 | 24 | 1 in 110 | 6.7% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 4 | 16 | 24 | 1 in 110 | 6.7% |
| The meta on skeletons with 2 or more spare moves | 1 | 5 | 0 | 1 in 99 | 13.3% |
| The meta with P = 0 on skeletons with two more quarter turns | 4 | 16 | 24 | 1 in 109 | 6.7% |
| The meta without skeletons that have a cancelling pair | 3 | 12 | 20 | 1 in 107 | 6.7% |
| The meta on skeletons with the DR's own quarter turns only | 2 | 8 | 20 | 1 in 106 | 6.7% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 4 | 28 | 32 | 1 in 113 | 6.7% |

**2c3** · 1,048 DRs, 901 within-goal. P+S+T ≤ 4 misses 7.0% of the time instead of 3.6%; a second pre-2qt move takes it to 2.1%, for 201 HTRs instead of 179 and 730 routes to 2qt instead of 578.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 60 | 698 | 326 | 1 in 60 | 1.7% |
| P ≤ 1, step 4 | 58 | 579 | 266 | 1 in 57 | 1.7% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 57 | 454 | 80 | 1 in 34 | 15.5% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 58 | 568 | 129 | 1 in 38 | 7.0% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **58** | **578** | **179** | **1 in 42** | **3.6%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 58 | 579 | 231 | 1 in 46 | 2.0% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 60 | 693 | 202 | 1 in 44 | 3.6% |
| P = 0, step 4, P+S+T ≤ 5 | 56 | 237 | 121 | 1 in 39 | 11.4% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 64 | 730 | 201 | 1 in 43 | 2.1% |
| Any P, step 4, P+S+T ≤ 5 | 64 | 740 | 204 | 1 in 42 | 2.1% |
| P ≤ 1, step 4, T+N ≤ 4 | 58 | 578 | 224 | 1 in 56 | 3.8% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 58 | 579 | 160 | 1 in 46 | 7.5% |
| The meta on skeletons with 2 or more spare moves | 39 | 510 | 173 | 1 in 42 | 3.8% |
| The meta with P = 0 on skeletons with two more quarter turns | 56 | 282 | 145 | 1 in 37 | 6.2% |
| The meta without skeletons that have a cancelling pair | 39 | 398 | 150 | 1 in 38 | 6.2% |
| The meta on skeletons with the DR's own quarter turns only | 6 | 63 | 104 | 1 in 31 | 12.3% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 60 | 693 | 178 | 1 in 47 | 8.2% |

**4c3** · 851 DRs, 511 within-goal. P+S+T ≤ 4 misses 2.0% of the time instead of 1.4%; a second pre-2qt move takes it to 0.8%, for 116 HTRs instead of 113 and 332 routes to 2qt instead of 310.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 35 | 388 | 142 | 1 in 63 | 0.8% |
| P ≤ 1, step 4 | 33 | 310 | 113 | 1 in 60 | 0.8% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 33 | 300 | 72 | 1 in 45 | 7.6% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 33 | 310 | 104 | 1 in 53 | 2.0% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **33** | **310** | **113** | **1 in 59** | **1.4%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 33 | 310 | 113 | 1 in 60 | 0.8% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 35 | 388 | 139 | 1 in 62 | 1.4% |
| P = 0, step 4, P+S+T ≤ 5 | 33 | 145 | 78 | 1 in 57 | 12.9% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 35 | 332 | 116 | 1 in 59 | 0.8% |
| Any P, step 4, P+S+T ≤ 5 | 35 | 332 | 116 | 1 in 59 | 0.4% |
| P ≤ 1, step 4, T+N ≤ 4 | 33 | 310 | 113 | 1 in 60 | 1.4% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 33 | 310 | 111 | 1 in 59 | 2.3% |
| The meta on skeletons with 2 or more spare moves | 21 | 274 | 108 | 1 in 58 | 3.9% |
| The meta with P = 0 on skeletons with two more quarter turns | 33 | 161 | 88 | 1 in 56 | 8.8% |
| The meta without skeletons that have a cancelling pair | 27 | 264 | 101 | 1 in 57 | 5.5% |
| The meta on skeletons with the DR's own quarter turns only | 4 | 24 | 63 | 1 in 53 | 25.0% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 35 | 388 | 137 | 1 in 63 | 2.3% |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample). P+S+T ≤ 4 misses no more often (0.0%); a second pre-2qt move finds nothing more, for 608 HTRs instead of 554 and 1,798 routes to 2qt instead of 1,423.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 120 | 1,775 | 658 | 1 in 87 | 0.0% |
| P ≤ 1, step 4 | 116 | 1,423 | 554 | 1 in 85 | 0.0% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 116 | 1,399 | 346 | 1 in 68 | 4.5% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 116 | 1,423 | 470 | 1 in 81 | 0.0% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **116** | **1,423** | **554** | **1 in 85** | **0.0%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 116 | 1,423 | 554 | 1 in 85 | 0.0% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 120 | 1,775 | 658 | 1 in 87 | 0.0% |
| P = 0, step 4, P+S+T ≤ 5 | 113 | 558 | 324 | 1 in 90 | 10.6% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 140 | 1,798 | 608 | 1 in 84 | 0.0% |
| Any P, step 4, P+S+T ≤ 5 | 140 | 2,089 | 625 | 1 in 83 | 0.0% |
| P ≤ 1, step 4, T+N ≤ 4 | 116 | 1,423 | 551 | 1 in 86 | 0.0% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 116 | 1,423 | 554 | 1 in 85 | 0.0% |
| The meta on skeletons with 2 or more spare moves | 42 | 1,069 | 526 | 1 in 84 | 0.0% |
| The meta with P = 0 on skeletons with two more quarter turns | 113 | 838 | 510 | 1 in 85 | 4.5% |
| The meta without skeletons that have a cancelling pair | 114 | 1,407 | 549 | 1 in 85 | 0.0% |
| The meta on skeletons with the DR's own quarter turns only | 22 | 410 | 458 | 1 in 82 | 6.1% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 120 | 1,775 | 658 | 1 in 87 | 0.0% |

**2c4** · 1,243 DRs, 1,123 within-goal. P+S+T ≤ 4 misses 2.0% of the time instead of 1.2%; a second pre-2qt move takes it to 0.5%, for 405 HTRs instead of 356 and 1,505 routes to 2qt instead of 1,230.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 97 | 1,561 | 462 | 1 in 66 | 0.7% |
| P ≤ 1, step 4 | 95 | 1,231 | 406 | 1 in 64 | 0.7% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 95 | 1,081 | 190 | 1 in 47 | 6.1% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 95 | 1,202 | 278 | 1 in 53 | 2.0% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **95** | **1,230** | **356** | **1 in 58** | **1.2%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 95 | 1,231 | 402 | 1 in 62 | 0.8% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 97 | 1,559 | 399 | 1 in 60 | 1.2% |
| P = 0, step 4, P+S+T ≤ 5 | 93 | 529 | 189 | 1 in 56 | 12.5% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 102 | 1,505 | 405 | 1 in 58 | 0.5% |
| Any P, step 4, P+S+T ≤ 5 | 102 | 1,562 | 412 | 1 in 57 | 0.4% |
| P ≤ 1, step 4, T+N ≤ 4 | 95 | 1,231 | 380 | 1 in 63 | 1.2% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 95 | 1,231 | 372 | 1 in 61 | 1.2% |
| The meta on skeletons with 2 or more spare moves | 43 | 933 | 330 | 1 in 57 | 1.9% |
| The meta with P = 0 on skeletons with two more quarter turns | 93 | 825 | 322 | 1 in 55 | 1.8% |
| The meta without skeletons that have a cancelling pair | 78 | 1,072 | 334 | 1 in 56 | 1.5% |
| The meta on skeletons with the DR's own quarter turns only | 15 | 436 | 280 | 1 in 53 | 3.3% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 97 | 1,559 | 390 | 1 in 61 | 1.6% |

**4c4** · 691 DRs, 397 within-goal. P+S+T ≤ 4 misses 2.5% of the time instead of 1.5%; a second pre-2qt move takes it to 0.5%, for 146 HTRs instead of 138 and 893 routes to 2qt instead of 777.

| Rule | Skeletons per DR (median) | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| P ≤ 1 | 73 | 1,008 | 168 | 1 in 80 | 1.5% |
| P ≤ 1, step 4 | 71 | 777 | 138 | 1 in 79 | 1.5% |
| P ≤ 1, step 4, P+S+T ≤ 3 | 71 | 775 | 123 | 1 in 72 | 7.1% |
| P ≤ 1, step 4, P+S+T ≤ 4 | 71 | 777 | 137 | 1 in 75 | 2.5% |
| **P ≤ 1, step 4, P+S+T ≤ 5** | **71** | **777** | **138** | **1 in 79** | **1.5%** |
| P ≤ 1, step 4, P+S+T ≤ 6 | 71 | 777 | 138 | 1 in 79 | 1.5% |
| P ≤ 1, P+S+T ≤ 5, without step 4 | 73 | 1,008 | 168 | 1 in 80 | 1.5% |
| P = 0, step 4, P+S+T ≤ 5 | 69 | 366 | 82 | 1 in 76 | 17.6% |
| P ≤ 2, step 4, P+S+T ≤ 5 | 75 | 893 | 146 | 1 in 80 | 0.5% |
| Any P, step 4, P+S+T ≤ 5 | 75 | 943 | 149 | 1 in 80 | 0.0% |
| P ≤ 1, step 4, T+N ≤ 4 | 71 | 777 | 138 | 1 in 79 | 1.8% |
| P ≤ 1, step 4, S+T+N ≤ 5 | 71 | 777 | 138 | 1 in 79 | 1.5% |
| The meta on skeletons with 2 or more spare moves | 16 | 446 | 107 | 1 in 78 | 14.4% |
| The meta with P = 0 on skeletons with two more quarter turns | 69 | 443 | 108 | 1 in 78 | 10.8% |
| The meta without skeletons that have a cancelling pair | 71 | 773 | 138 | 1 in 79 | 1.5% |
| The meta on skeletons with the DR's own quarter turns only | 6 | 109 | 77 | 1 in 78 | 30.7% |
| P ≤ 1, P+S+T+N ≤ 5, without step 4 (the doc's S+T+N ≤ min(G−L, 5) − P) | 73 | 1,008 | 168 | 1 in 80 | 1.5% |

## Appendix C. Data and method

Every number above comes from an exhaustive search of random DRs, with each HTR's finish taken from an exact table.

- **Sample.** 2,000 uniformly random DR states each with 2, 3 and 4 quarter turns to HTR. 40 of the 2qt states are 0c0 up to a turn of both layers and are dropped, leaving 1,960.
- **Search.** On both sides, every HTR in reach with the DR's quarter turns or two more, up to 6. In reach means the moves to HTR plus the corner moves left after it fit the goal. That's 53,654,751 HTRs. The caps of each table are applied on top.
- **Finish.** The shortest leave-slice finish in half turns from that HTR, from an exact table. An HTR is within goal when its moves plus that finish fit the goal.
- **Reading a solution.** A solution is cut at its quarter turns into sections. The skeleton of a section is the fewest half turns that do the same to the corners, up to a corner swap of the side axes (`R2 F2 R2`), a slice, and a U2 or D2 next to a quarter turn, which only turns that quarter turn the other way. L is the quarter turns plus those moves, and a section's extra moves are its length minus its skeleton's. P is the extra moves of the sections before 2qt, S of the setup at 2qt, T of the trigger and N of the finish. Two HTRs are on the same skeleton when they are in the same corner case at every quarter turn.
- **Checks of that reading.** On 20,965 skeletons (the first 100 DRs of each sample), L is the length of the shortest corner-only path through the same corner cases at each quarter turn. All 2,898 within-goal solutions of those DRs read as mirror images on normal and inverse. Over the whole sample, all but 10 of the 47,122 within-goal HTRs have their mirror image among the other side's HTRs.
- **Step 4 on a 6qt skeleton.** S+T+N ≥ P, not counting an extra move in the skeleton's middle section, which the inverse also reads as its middle.
- **Order of finishing.** Skeletons shortest first, each skeleton's variants with the fewest P+S+T first and in increasing order of (P, S, T, N) among those. A first pass finishes at most 3 variants per skeleton, then the rest follow in the same order. Ties are taken in random order, and the found-within-K shares are averages over 20 such orders. Plain (P, S, T, N) order, which takes every trigger of one setup before the next setup, finds later: on 4b2, 68% within 20 instead of 73%.
- **Routes to 2qt.** Distinct move sequences, on either side, up to the point where the skeleton has 2 quarter turns left, that lead to at least one HTR the table's limits allow. They're counted before any bound, so they don't depend on it.
- **Skeletons.** Counted the same way: the skeletons with at least one HTR the table's limits allow, before any bound.

### Changes from the 19 Nov version

- **P is its own number**, as in the doc. Before, the moves before 2qt were counted inside S.
- **Every solution is read against its own skeleton.** Before, extra moves were counted against the shortest corner path with the same quarter turns and the same NISS@1qt corner case, so a solution on a longer corner route looked like a variant with extra moves, often before 2qt. Now that route is a skeleton of its own, with a longer L and fewer spare moves. More solutions fit P ≤ 1 this way, so the meta misses less (4b2 4.0% instead of 8.2%, 2c3 3.6% instead of 6.9%) and has more routes to 2qt to go through (4b2 148 instead of 77, 2c3 578 instead of 169).
- **Step 4 is new.**

### Left out of the meta

- **Reflection penalties.** The doc's "+2 per reflected slice" terms aren't tracked here.
- **cs-parity.** Only the comprehensive bound needs it, and checking it during a solve is slow.
- **Pair count at the trigger.** The number of pairs at the quarter turn from 2qt to 1qt was looked at as a further sort for 2c3 DRs with RD corners. It's kept as a note, not part of the meta.
