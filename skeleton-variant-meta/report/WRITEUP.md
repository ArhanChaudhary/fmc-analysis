# The skeleton/variant meta

19 Nov 2026

A meta for finding DR finishes within a certain goal move count, based on [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0).
The meta is based on the extra moves needed on top of a corner skeleton (minimum moves to solve corners up to a corner-swap/rotation). 
The extra moves are broken down by:

 - **S**: Additional moves used to set up the 2qt trigger, counting any extra moves before reaching 2qt
 - **T**: Additional moves in the trigger
 - **N**: Additional moves after reaching HTR 

These stats use a goal of 12/13/14 moves for 2qt/3qt/4qt cases, counting the moves from DR to a leave-slice finish.

## 1. The meta

The standard meta, roughly speaking, is to spam HTRs whose length is not too far from the goal, on both normal and inverse.
You don't want too many extra moves early in the skeleton, and block building is of limited value, because preserving blocks is often incompatible
with the approach to HTR.  

Here, we formalize the meta in terms of skeletons and their variants. We quantify "not too far from the goal"
and "too many extra early moves" as follows:

1. **Sort the attempt's DRs by corner case**, shortest skeleton first, in the order of the table below.
2. **Within a DR, sort skeletons by length**, normal and inverse mixed. Skeletons with two more quarter turns than the DR count too, and sort in by length with the rest.
3. **For each skeleton, generate the variants with S+T ≤ 5**, with at most 1 of those extra moves before 2qt.
4. **Discard a variant when S+T+N+L > G**, where L is the skeleton length, and G is the goal. Finish the rest, fewest extra moves first.

In the **baseline** meta, you check every variant with S+T ≤ 5 and S+T+L ≤ G, the equivalent of N=0.
Advanced DR Bounding adds a way to compute N. The stats below show the benefit of using it
to discard variants. 

### Corner cases

These stats are based on a random sample of 2qt/3qt/4qt DRs, 2,000 of each (1,960 for 2qt; see appendix C). This table gives the chance that 
a corner case has a within-goal solution, and the chance that the recommended meta will miss it.

| Corner case | Shortest skeleton length | Within-goal DRs | The meta misses a within-goal finish | DRs in the sample |
|---|---|---|---|---|
| 4b2 | 3 | 60.2% | 8.2% | 1,584 |
| 4a2 | 5 | 31.9% | 4.2% | 376 |
| 2c3 | 5 | 86.0% | 6.9% | 1,048 |
| 4c3 | 7 | 60.0% | 2.2% | 851 |
| 2c4 | 7 | 90.3% | 4.5% | 1,243 |
| 0c3 | 9 | 14.9% | 6.7% | 101 |
| 0c4 | 9 | 100.0% | 1.5% | 66 |
| 4c4 | 9 | 57.5% | 4.5% | 691 |

As we'll see below, the miss percentages do not depend on whether you use DR Bounding to prune the search.
Instead, they mostly come from the restriction to not add too many extra moves at the beginning of the skeleton.
Pre-2qt moves on normal become post-2qt moves on inverse, so a DR is missed when its solutions need early extra moves on both sides.
For example, the 2c3 DR `D2 F2 D2 U F2 U R2 D L2 U L2 R2 U'` has a 12-move solution on normal, `U R2 L2 U' L2 U' B2 U' R2 D F2 D2`,
but on its 5qt skeleton both extra moves come before 2qt. Its best solution on inverse, `U2 B2 U' F2 U R2 U B2 D R2 L2 U'`,
also needs 2 extra moves before 2qt. The meta finds neither.

## 2. Stats for the recommended meta

Filtering by the DR Bounding lower limit **reduces the number of HTRs to check by 11-27x**, with only a negligible increase in missed within-goal finishes.

The stats below use the "corner-case-aware" bound from [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0), without the reflection penalty (which would improve the numbers). See the doc for details.

How to read the columns:

- **HTRs to finish per DR.** The variants the search finishes, as a median over all the case's DRs, within-goal or not.
- **Within goal.** The share of those HTRs whose finish fits the goal.
- **Chance of missing a within-goal finish.** The share of within-goal DRs where none of them does.
- **Found within K finishes.** The share of within-goal DRs where one of the first K HTRs finished, in the meta's order, is within goal.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal · 76 routes to 2qt per DR (median, both searches). The bound finishes 27× fewer HTRs with no change in the chance of missing. It finds a within-goal finish in the first 10 for 62% of within-goal DRs against 39%.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 878 | 1 in 738 | 4.2% | 25% | 39% |
| **Corner-case-aware** | 32 | 1 in 54 | 4.2% | 40% | 62% |

**4b2** · 1,584 DRs, 953 within-goal · 77 routes to 2qt per DR (median, both searches). The bound finishes 12× fewer HTRs with a chance of missing 0.2 points higher. It finds a within-goal finish in the first 10 for 58% of within-goal DRs against 49%.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 756 | 1 in 388 | 8.0% | 40% | 49% |
| **Corner-case-aware** | 64 | 1 in 36 | 8.2% | 49% | 58% |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample) · 27 routes to 2qt per DR (median, both searches). The bound finishes 24× fewer HTRs with no change in the chance of missing. It finds a within-goal finish in the first 10 for 21% of within-goal DRs against 6%.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 760 | 1 in 1,940 | 6.7% | 4% | 6% |
| **Corner-case-aware** | 32 | 1 in 112 | 6.7% | 15% | 21% |

**2c3** · 1,048 DRs, 901 within-goal · 169 routes to 2qt per DR (median, both searches). The bound finishes 11× fewer HTRs with a chance of missing 0.2 points higher. It finds a within-goal finish in the first 10 for 47% of within-goal DRs against 36%.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 1,602 | 1 in 411 | 6.7% | 28% | 36% |
| **Corner-case-aware** | 143 | 1 in 37 | 6.9% | 36% | 47% |

**4c3** · 851 DRs, 511 within-goal · 236 routes to 2qt per DR (median, both searches). The bound finishes 16× fewer HTRs with no change in the chance of missing. It finds a within-goal finish in the first 10 for 40% of within-goal DRs against 22%.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 1,948 | 1 in 891 | 2.2% | 15% | 22% |
| **Corner-case-aware** | 122 | 1 in 60 | 2.2% | 26% | 40% |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample) · 755 routes to 2qt per DR (median, both searches). The bound finishes 16× fewer HTRs with no change in the chance of missing. It finds a within-goal finish in the first 10 for 23% of within-goal DRs against 11%.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 8,444 | 1 in 1,252 | 1.5% | 8% | 11% |
| **Corner-case-aware** | 538 | 1 in 82 | 1.5% | 16% | 23% |

**2c4** · 1,243 DRs, 1,123 within-goal · 428 routes to 2qt per DR (median, both searches). The bound finishes 13× fewer HTRs with no change in the chance of missing. It finds a within-goal finish in the first 10 for 40% of within-goal DRs against 27%.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 2,569 | 1 in 680 | 4.5% | 18% | 27% |
| **Corner-case-aware** | 203 | 1 in 51 | 4.5% | 28% | 40% |

**4c4** · 691 DRs, 397 within-goal · 505 routes to 2qt per DR (median, both searches). The bound finishes 17× fewer HTRs with no change in the chance of missing. It finds a within-goal finish in the first 10 for 27% of within-goal DRs against 10%.

| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 2,081 | 1 in 1,217 | 4.5% | 7% | 10% |
| **Corner-case-aware** | 126 | 1 in 76 | 4.5% | 17% | 27% |

### Where the misses come from

Skeletons with two more quarter turns are part of the meta. Without them, 4b2 would miss 36.4% of the time instead of 8.2%, and 4c3 25.0% instead of 2.2%. What's left is mostly DRs that need a second pre-2qt move. Skeletons with four more quarter turns would save at most 3 DRs in any case.

Each missed DR the bound didn't lose is filed under its cheapest within-goal HTR anywhere in the data: fewest S+T, then fewest pre-2qt moves. Cells are shares of within-goal DRs, and the five columns on the right add up to the meta's chance of missing, up to rounding.

**Error in DR Bound** counts DRs lost because the corner-case-aware table asks +5 for RD or FD corners with 1 bad slice and cs/fr 1/1, where +4 is enough. For example, on the 2c3 DR `U L2 U2 B2 D2 F2 L2 U' B2 D' R2 U2`, `R2 U' R2 B2 U' R2 B2 U'` reaches HTR in that case in 8 moves and `B2 U2 L2 F2 D2` finishes in 5, 13 in all, but the bound says 8 + 1 + 5 = 14.

| Corner case | Missed | Needs 1 more S+T | Needs a second pre-2qt move | Needs 2 or more S+T beyond the limit | Error in DR Bound | Needs four more quarter turns |
|---|---|---|---|---|---|---|
| 4a2 | 4.2% | 0.8% | 0.8% | 0.0% | 0.0% | 2.5% |
| 4b2 | 8.2% | 1.9% | 5.7% | 0.2% | 0.2% | 0.2% |
| 0c3 | 6.7% | 0.0% | 0.0% | 0.0% | 0.0% | 6.7% |
| 2c3 | 6.9% | 1.6% | 4.8% | 0.3% | 0.2% | 0.0% |
| 4c3 | 2.2% | 0.2% | 1.8% | 0.0% | 0.0% | 0.2% |
| 0c4 | 1.5% | 0.0% | 1.5% | 0.0% | 0.0% | 0.0% |
| 2c4 | 4.5% | 0.4% | 4.1% | 0.0% | 0.0% | 0.0% |
| 4c4 | 4.5% | 0.0% | 4.5% | 0.0% | 0.0% | 0.0% |

## Appendix A. Varying the bound

[*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0) doc 
defines three estimates for the lower bound: simple, corner-case-aware, and comprehensive. We have chosen
the middle one. Each level prunes the HTRs by a factor of roughly 2x, at the cost of more complicated recognition,
but the biggest jump is between using any type of DR Bounding vs. none.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal. Corner-case-aware makes a finished HTR 13.6× likelier to be within goal than the baseline does; comprehensive adds 2.0× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 878 | 1 in 738 | 4.2% | 25% | 39% |
| Simple | 80 | 1 in 140 | 4.2% | 32% | 49% |
| **Corner-case-aware** | 32 | 1 in 54 | 4.2% | 40% | 62% |
| Comprehensive | 16 | 1 in 27 | 4.2% | 49% | 73% |

**4b2** · 1,584 DRs, 953 within-goal. Corner-case-aware makes a finished HTR 10.8× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 756 | 1 in 388 | 8.0% | 40% | 49% |
| Simple | 141 | 1 in 79 | 8.0% | 44% | 54% |
| **Corner-case-aware** | 64 | 1 in 36 | 8.2% | 49% | 58% |
| Comprehensive | 33 | 1 in 19 | 8.0% | 54% | 68% |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample). Corner-case-aware makes a finished HTR 17.3× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 760 | 1 in 1,940 | 6.7% | 4% | 6% |
| Simple | 96 | 1 in 282 | 6.7% | 10% | 15% |
| **Corner-case-aware** | 32 | 1 in 112 | 6.7% | 15% | 21% |
| Comprehensive | 8 | 1 in 58 | 6.7% | 24% | 36% |

**2c3** · 1,048 DRs, 901 within-goal. Corner-case-aware makes a finished HTR 11.0× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 1,602 | 1 in 411 | 6.7% | 28% | 36% |
| Simple | 325 | 1 in 82 | 6.9% | 31% | 41% |
| **Corner-case-aware** | 143 | 1 in 37 | 6.9% | 36% | 47% |
| Comprehensive | 75 | 1 in 20 | 6.7% | 41% | 57% |

**4c3** · 851 DRs, 511 within-goal. Corner-case-aware makes a finished HTR 14.9× likelier to be within goal than the baseline does; comprehensive adds 2.0× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 1,948 | 1 in 891 | 2.2% | 15% | 22% |
| Simple | 302 | 1 in 149 | 3.3% | 20% | 30% |
| **Corner-case-aware** | 122 | 1 in 60 | 2.2% | 26% | 40% |
| Comprehensive | 58 | 1 in 30 | 2.2% | 34% | 51% |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample). Corner-case-aware makes a finished HTR 15.2× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 8,444 | 1 in 1,252 | 1.5% | 8% | 11% |
| Simple | 1,266 | 1 in 205 | 1.5% | 11% | 16% |
| **Corner-case-aware** | 538 | 1 in 82 | 1.5% | 16% | 23% |
| Comprehensive | 260 | 1 in 43 | 1.5% | 22% | 32% |

**2c4** · 1,243 DRs, 1,123 within-goal. Corner-case-aware makes a finished HTR 13.4× likelier to be within goal than the baseline does; comprehensive adds 1.9× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 2,569 | 1 in 680 | 4.5% | 18% | 27% |
| Simple | 492 | 1 in 123 | 5.2% | 22% | 32% |
| **Corner-case-aware** | 203 | 1 in 51 | 4.5% | 28% | 40% |
| Comprehensive | 105 | 1 in 26 | 4.5% | 34% | 50% |

**4c4** · 691 DRs, 397 within-goal. Corner-case-aware makes a finished HTR 16.1× likelier to be within goal than the baseline does; comprehensive adds 2.0× on top.

| Bound | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |
|---|---|---|---|---|---|
| Baseline (no DR Bounding) | 2,081 | 1 in 1,217 | 4.5% | 7% | 10% |
| Simple | 338 | 1 in 186 | 4.5% | 11% | 18% |
| **Corner-case-aware** | 126 | 1 in 76 | 4.5% | 17% | 27% |
| Comprehensive | 60 | 1 in 38 | 4.5% | 27% | 43% |

## Appendix B. Varying S+T and the pre-2qt moves

We can prune our HTRs further by reducing the limit on S+T. However, this significantly
increases our chance of missing a within-goal solution. 

Similarly, we can increase our chances of finding a within-goal solution by allowing
more moves before 2qt. It cuts the misses to below 5%, but doubles the number of routes to 2qt.

The tables below show the stats with different S+T and pre-2qt limits, using the corner-case-aware bound. The meta's row (S+T ≤ 5, at most 1 pre-2qt move) is in bold.

### 2qt DRs (goal 12)

**4a2** · 376 DRs, 120 within-goal. S+T ≤ 4 misses no more often (4.2%); a second pre-2qt move takes it to 3.3%, for 36 HTRs instead of 32 and 80 routes to 2qt instead of 76.

| S+T at most | Pre-2qt moves at most | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| 2 | 0 | 8 | 2 | 1 in 25 | 35.8% |
| 2 | 1 | 10 | 4 | 1 in 26 | 35.8% |
| 2 | no limit | 11 | 4 | 1 in 27 | 35.8% |
| 3 | 0 | 30 | 14 | 1 in 33 | 12.5% |
| 3 | 1 | 42 | 17 | 1 in 34 | 11.7% |
| 3 | 2 | 46 | 18 | 1 in 35 | 10.8% |
| 3 | no limit | 50 | 19 | 1 in 35 | 10.8% |
| 4 | 0 | 38 | 22 | 1 in 41 | 6.7% |
| 4 | 1 | 76 | 29 | 1 in 43 | 4.2% |
| 4 | 2 | 80 | 33 | 1 in 44 | 3.3% |
| 4 | no limit | 85 | 37 | 1 in 45 | 3.3% |
| 5 | 0 | 38 | 24 | 1 in 52 | 6.7% |
| **5** | **1** | **76** | **32** | **1 in 54** | **4.2%** |
| 5 | 2 | 80 | 36 | 1 in 55 | 3.3% |
| 5 | no limit | 85 | 42 | 1 in 56 | 3.3% |

**4b2** · 1,584 DRs, 953 within-goal. S+T ≤ 4 misses 12.8% of the time instead of 8.2%; a second pre-2qt move takes it to 3.1%, for 79 HTRs instead of 64 and 181 routes to 2qt instead of 77.

| S+T at most | Pre-2qt moves at most | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| 2 | 0 | 9 | 5 | 1 in 15 | 53.7% |
| 2 | 1 | 24 | 7 | 1 in 18 | 47.4% |
| 2 | no limit | 35 | 9 | 1 in 19 | 44.9% |
| 3 | 0 | 16 | 13 | 1 in 20 | 34.2% |
| 3 | 1 | 47 | 19 | 1 in 23 | 26.5% |
| 3 | 2 | 85 | 23 | 1 in 25 | 22.4% |
| 3 | no limit | 133 | 27 | 1 in 27 | 21.1% |
| 4 | 0 | 18 | 28 | 1 in 25 | 22.7% |
| 4 | 1 | 72 | 41 | 1 in 30 | 12.8% |
| 4 | 2 | 142 | 48 | 1 in 32 | 8.8% |
| 4 | no limit | 363 | 64 | 1 in 37 | 7.3% |
| 5 | 0 | 19 | 46 | 1 in 31 | 19.3% |
| **5** | **1** | **77** | **64** | **1 in 36** | **8.2%** |
| 5 | 2 | 181 | 79 | 1 in 39 | 3.1% |
| 5 | no limit | 591 | 111 | 1 in 46 | 2.4% |

### 3qt DRs (goal 13)

**0c3** · 101 DRs, 15 within-goal (a small sample). S+T ≤ 4 misses no more often (6.7%); a second pre-2qt move changes nothing.

| S+T at most | Pre-2qt moves at most | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| 2 | 0 | 8 | 16 | 1 in 100 | 33.3% |
| 2 | 1 | 27 | 24 | 1 in 113 | 33.3% |
| 2 | no limit | 28 | 32 | 1 in 121 | 33.3% |
| 3 | 0 | 8 | 16 | 1 in 100 | 13.3% |
| 3 | 1 | 27 | 32 | 1 in 111 | 13.3% |
| 3 | 2 | 28 | 32 | 1 in 121 | 13.3% |
| 3 | no limit | 28 | 40 | 1 in 118 | 13.3% |
| 4 | 0 | 8 | 16 | 1 in 104 | 6.7% |
| 4 | 1 | 27 | 32 | 1 in 112 | 6.7% |
| 4 | 2 | 28 | 32 | 1 in 123 | 6.7% |
| 4 | no limit | 28 | 40 | 1 in 122 | 6.7% |
| 5 | 0 | 8 | 16 | 1 in 104 | 6.7% |
| **5** | **1** | **27** | **32** | **1 in 112** | **6.7%** |
| 5 | 2 | 28 | 32 | 1 in 123 | 6.7% |
| 5 | no limit | 28 | 40 | 1 in 122 | 6.7% |

**2c3** · 1,048 DRs, 901 within-goal. S+T ≤ 4 misses 11.7% of the time instead of 6.9%; a second pre-2qt move takes it to 2.9%, for 200 HTRs instead of 143 and 502 routes to 2qt instead of 169.

| S+T at most | Pre-2qt moves at most | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| 2 | 0 | 10 | 5 | 1 in 11 | 53.8% |
| 2 | 1 | 36 | 13 | 1 in 15 | 40.2% |
| 2 | no limit | 72 | 18 | 1 in 17 | 37.3% |
| 3 | 0 | 22 | 18 | 1 in 18 | 39.3% |
| 3 | 1 | 91 | 35 | 1 in 22 | 23.1% |
| 3 | 2 | 206 | 49 | 1 in 25 | 19.5% |
| 3 | no limit | 349 | 63 | 1 in 27 | 17.8% |
| 4 | 0 | 25 | 39 | 1 in 24 | 28.9% |
| 4 | 1 | 153 | 83 | 1 in 29 | 11.7% |
| 4 | 2 | 369 | 114 | 1 in 32 | 7.9% |
| 4 | no limit | 1,086 | 172 | 1 in 38 | 6.8% |
| 5 | 0 | 27 | 66 | 1 in 32 | 22.8% |
| **5** | **1** | **169** | **143** | **1 in 37** | **6.9%** |
| 5 | 2 | 502 | 200 | 1 in 42 | 2.9% |
| 5 | no limit | 2,380 | 343 | 1 in 51 | 2.0% |

**4c3** · 851 DRs, 511 within-goal. S+T ≤ 4 misses 2.9% of the time instead of 2.2%; a second pre-2qt move takes it to 0.8%, for 156 HTRs instead of 122 and 502 routes to 2qt instead of 236.

| S+T at most | Pre-2qt moves at most | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| 2 | 0 | 40 | 19 | 1 in 28 | 36.6% |
| 2 | 1 | 135 | 38 | 1 in 35 | 24.5% |
| 2 | no limit | 226 | 46 | 1 in 37 | 22.1% |
| 3 | 0 | 64 | 37 | 1 in 36 | 24.1% |
| 3 | 1 | 214 | 66 | 1 in 43 | 9.4% |
| 3 | 2 | 415 | 90 | 1 in 46 | 7.2% |
| 3 | no limit | 626 | 103 | 1 in 48 | 6.1% |
| 4 | 0 | 67 | 57 | 1 in 45 | 17.4% |
| 4 | 1 | 233 | 103 | 1 in 52 | 2.9% |
| 4 | 2 | 477 | 133 | 1 in 56 | 1.4% |
| 4 | no limit | 863 | 174 | 1 in 61 | 1.0% |
| 5 | 0 | 68 | 65 | 1 in 53 | 16.2% |
| **5** | **1** | **236** | **122** | **1 in 60** | **2.2%** |
| 5 | 2 | 502 | 156 | 1 in 63 | 0.8% |
| 5 | no limit | 1,002 | 225 | 1 in 68 | 0.4% |

### 4qt DRs (goal 14)

**0c4** · 66 DRs, 66 within-goal (a small sample). S+T ≤ 4 misses no more often (1.5%); a second pre-2qt move takes it to 0.0%, for 735 HTRs instead of 538 and 2,064 routes to 2qt instead of 755.

| S+T at most | Pre-2qt moves at most | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| 2 | 0 | 134 | 70 | 1 in 40 | 24.2% |
| 2 | 1 | 562 | 151 | 1 in 46 | 15.2% |
| 2 | no limit | 1,150 | 194 | 1 in 51 | 13.6% |
| 3 | 0 | 150 | 130 | 1 in 54 | 19.7% |
| 3 | 1 | 738 | 270 | 1 in 59 | 6.1% |
| 3 | 2 | 1,937 | 398 | 1 in 66 | 4.5% |
| 3 | no limit | 3,465 | 486 | 1 in 72 | 4.5% |
| 4 | 0 | 151 | 220 | 1 in 73 | 13.6% |
| 4 | 1 | 755 | 420 | 1 in 78 | 1.5% |
| 4 | 2 | 2,060 | 586 | 1 in 83 | 0.0% |
| 4 | no limit | 5,773 | 841 | 1 in 94 | 0.0% |
| 5 | 0 | 151 | 264 | 1 in 81 | 12.1% |
| **5** | **1** | **755** | **538** | **1 in 82** | **1.5%** |
| 5 | 2 | 2,064 | 735 | 1 in 86 | 0.0% |
| 5 | no limit | 6,222 | 1,184 | 1 in 95 | 0.0% |

**2c4** · 1,243 DRs, 1,123 within-goal. S+T ≤ 4 misses 6.6% of the time instead of 4.5%; a second pre-2qt move takes it to 0.8%, for 327 HTRs instead of 203 and 1,254 routes to 2qt instead of 428.

| S+T at most | Pre-2qt moves at most | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| 2 | 0 | 41 | 14 | 1 in 22 | 55.3% |
| 2 | 1 | 201 | 43 | 1 in 27 | 27.5% |
| 2 | no limit | 407 | 64 | 1 in 30 | 21.9% |
| 3 | 0 | 64 | 30 | 1 in 30 | 43.4% |
| 3 | 1 | 341 | 82 | 1 in 34 | 15.2% |
| 3 | 2 | 865 | 137 | 1 in 39 | 8.5% |
| 3 | no limit | 1,469 | 183 | 1 in 43 | 6.1% |
| 4 | 0 | 68 | 52 | 1 in 39 | 34.6% |
| 4 | 1 | 416 | 145 | 1 in 43 | 6.6% |
| 4 | 2 | 1,168 | 233 | 1 in 48 | 2.1% |
| 4 | no limit | 3,282 | 404 | 1 in 54 | 1.2% |
| 5 | 0 | 68 | 73 | 1 in 47 | 31.1% |
| **5** | **1** | **428** | **203** | **1 in 51** | **4.5%** |
| 5 | 2 | 1,254 | 327 | 1 in 55 | 0.8% |
| 5 | no limit | 4,950 | 640 | 1 in 63 | 0.4% |

**4c4** · 691 DRs, 397 within-goal. S+T ≤ 4 misses 5.5% of the time instead of 4.5%; a second pre-2qt move takes it to 0.5%, for 195 HTRs instead of 126 and 1,149 routes to 2qt instead of 505.

| S+T at most | Pre-2qt moves at most | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |
|---|---|---|---|---|---|
| 2 | 0 | 104 | 27 | 1 in 50 | 48.4% |
| 2 | 1 | 410 | 64 | 1 in 57 | 24.4% |
| 2 | no limit | 758 | 89 | 1 in 62 | 20.4% |
| 3 | 0 | 115 | 43 | 1 in 59 | 36.0% |
| 3 | 1 | 501 | 100 | 1 in 66 | 10.3% |
| 3 | 2 | 1,147 | 156 | 1 in 73 | 6.0% |
| 3 | no limit | 1,829 | 200 | 1 in 78 | 5.8% |
| 4 | 0 | 115 | 51 | 1 in 66 | 30.2% |
| 4 | 1 | 505 | 123 | 1 in 71 | 5.5% |
| 4 | 2 | 1,149 | 188 | 1 in 78 | 1.5% |
| 4 | no limit | 1,973 | 235 | 1 in 83 | 1.0% |
| 5 | 0 | 115 | 52 | 1 in 72 | 29.2% |
| **5** | **1** | **505** | **126** | **1 in 76** | **4.5%** |
| 5 | 2 | 1,149 | 195 | 1 in 81 | 0.5% |
| 5 | no limit | 1,973 | 238 | 1 in 87 | 0.0% |

## Appendix C. Data and method

Every number above comes from an exhaustive search of random DRs, with each HTR's finish taken from an exact table.

- **Sample.** 2,000 uniformly random DR states each with 2, 3 and 4 quarter turns to HTR. 40 of the 2qt states are 0c0 up to a turn of both layers and are dropped, leaving 1,960.
- **Search.** On both sides, every HTR in reach of every skeleton with the DR's quarter turns or two more, up to 6. In reach means S+T+L ≤ G. The S+T and pre-2qt limits of each table are applied on top.
- **Finish.** The shortest leave-slice finish in DR moves from that HTR, from an exact table. An HTR is within goal when its moves plus that finish fit the goal.
- **Order of finishing.** Shortest skeleton first, then fewest extra moves. Ties are taken in random order, and the found-within-K shares are expected values over that order.
- **Routes to 2qt.** Distinct move sequences, on either side, up to the point where the skeleton has 2 quarter turns left, that lead to at least one HTR the table's limits allow. They're counted before any bound, so they don't depend on it.

### Left out of the meta

- **Reflection penalties.** The doc's "+2 per reflected slice" terms aren't tracked here.
- **cs-parity.** Only the comprehensive bound needs it, and checking it during a solve is slow.
- **Pair count at the trigger.** The number of pairs at the quarter turn from 2qt to 1qt was looked at as a further sort for 2c3 DRs with RD corners. It's kept as a note, not part of the meta.
