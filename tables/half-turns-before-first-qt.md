# Half turns before the first quarter turn

From a DR, how many half turns does an optimal finish make before its first quarter turn, if you start on the better side? Per subset × edges, for all DRs and for the DRs that matter in an attempt: those with an optimal of 13 or less, or 12 or less.

**How it's counted.** Take every optimal finish of the DR (U, D, R2, L2, F2, B2) and count the moves before its first U or D quarter turn. They're all half turns; U2 and D2 count. Any optimal finish counts, including one with more quarter turns than the corners need, so the first quarter turn doesn't have to make progress: on a 2qt case it can be the first of four ([when it has to](#when-the-first-quarter-turn-has-to-make-progress)). Read each finish from its first move (normal) and from its last move (inverse) and keep the smaller number: that's *the better side*, chosen with hindsight. The *normal side alone* columns keep only the first reading. Sampled: 25,000 uniformly random DRs per subset × edges, each with every optimal finish from the exact table of all DR states, so a share is good to about ±0.3 points, more on the rows with few DRs (the tables give the count). November 2026.

**The short answer.**

- Over all DRs, 69.9% need no half turn first, 22.2% need one, and 8.0% need two or more. Among DRs with an optimal of 13 or less it's 12.6% that need two or more, and with 12 or less 15.9%.
- It depends on the subset and on the edge count. With an optimal of 12 or less, two or more half turns first are needed on 30.6% of 4a1 4e, 28.1% of 4a2 4e, 27.5% of 4b2 2e and 21.5% of 2c3 2e, and on none of the sampled DRs of 2c5, 0c3, 0c4, 4c4 or 4b5.
- Checking both sides matters: on the normal side alone, 23.6% of all DRs need two or more, against 8.0% on the better side.
- On the 2qt subsets the high *0 half turns* shares are 4qt optimals. A quarter turn at once belongs to a 2qt optimal on 5.7% of 4b2 and 7.3% of 4a2; on 57.9% and 49.9% only an optimal with four or more quarter turns starts that way. Those are common: every optimal of a 4b2 has four or more quarter turns on 55.0% of its DRs, and some optimal on 82.6% ([when the first quarter turn has to make progress](#when-the-first-quarter-turn-has-to-make-progress); [*Which HTR routes to try from a DR*](../htr-routes/#7-extra-quarter-turns-and-the-last-dr-move), section 7).
- What you can see: the corner case says whether to expect **one** half turn first. Call a side ready when a quarter turn takes its corners straight down a quarter turn. A 2c4 2e with an optimal of 13 or less needs a half turn first on 88.0% if neither side is ready, against 29.2% if one is. Needing **two or more** barely shows: only 4a2 has a usable sign, the bad-corner layout on both sides (77.7% against 22.2% on 4a2 4e). Pairs and the E slice say nothing, the bad edges next to nothing ([what you can see](#what-you-can-see-that-predicts-it)).
- One move over the optimal it nearly stops mattering: with an optimal of 13 or less, 1.4% of DRs have no finish within one move of the optimal that reaches its first quarter turn after 0 or 1 half turns ([within one move](#a-finish-within-one-move-of-the-optimal)).

The same question for 2c4 2e. Each row is a group of its DRs; each cell is the share needing exactly that many half turns first, on the better side:

| 2c4 2e | 0 half turns | 1 half turn | 2 half turns | 3 or more |
|---|---|---|---|---|
| all its DRs | 65.4% | 27.0% | 6.6% | 1.0% |
| optimal ≤ 13 (43.5% of 2c4 2e) | 62.8% | 28.2% | 8.5% | 0.5% |
| optimal ≤ 12 (11.3% of 2c4 2e) | 65.9% | 27.6% | 6.5% | 0% |

**What existed.** Kai Cui asked for these ([27 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1300060647719043174): "Are there stats on how many ht before first qt including niss for Dr finishes?"), got no answer, and measured 2c3 2e on 540 generated states ([5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457154635665448)): 60.0% with 0 half turns, 24.8% with 1, 10.9% with 2 and 4.3% with 3. Kai Cui's summary ([5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457432898633840)): "baically 85 percent chance that you dont need to check 2 ht before first qt". This sample gives 54.6% / 28.1% / 12.1% / 5.2% for uniform 2c3 2e, so 82.7% with 0 or 1 on the better side. Nothing else on the server has it per subset. [*Which HTR routes to try from a DR*](../htr-routes/) (section 7) has that row and the all-DRs figure. The tables below give every subset × edges.

**One row reads differently.** Half of 0c0 0e is already in HTR. On 29.6% of the sampled row no optimal finish has a quarter turn at all, and those DRs count as 3 or more.

## Optimal of 13 or less

Each row is a subset × edges, restricted to its DRs with an optimal finish of at most 13. *Share of its DRs that short* is how much of the subset × edges that is. The next four cells are the shares needing exactly 0, 1, 2, or 3 or more half turns before the first quarter turn on the better side; the last four are the same on the normal side alone.

| Subset × edges | Share of its DRs that short | DRs in the sample | 0 half turns | 1 half turn | 2 half turns | 3 or more | Normal side alone: 0 | Normal side alone: 1 | Normal side alone: 2 | Normal side alone: 3 or more |
|---|---|---|---|---|---|---|---|---|---|---|
| 0c0 0e | 100.0% | 25,000 | 38.3% | 18.7% | 8.3% | 34.8% | 25.2% | 17.3% | 10.3% | 47.2% |
| 0c0 2e | 98.8% | 24,701 | 57.9% | 28.3% | 10.6% | 3.1% | 39.2% | 27.0% | 14.9% | 19.0% |
| 0c0 4e | 92.3% | 23,082 | 59.9% | 23.9% | 9.9% | 6.3% | 40.5% | 25.0% | 13.5% | 21.0% |
| 0c0 6e | 75.2% | 18,805 | 72.4% | 22.6% | 4.5% | 0.5% | 48.8% | 27.5% | 12.8% | 10.9% |
| 0c0 8e | 77.6% | 19,407 | 61.4% | 26.1% | 9.9% | 2.6% | 40.2% | 25.9% | 15.3% | 18.5% |
| 2c5 0e | 11.2% | 2,798 | 89.3% | 10.7% | 0% | 0% | 61.2% | 27.7% | 9.2% | 1.9% |
| 2c5 2e | 15.4% | 3,845 | 81.0% | 17.8% | 1.1% | 0% | 53.7% | 29.4% | 11.7% | 5.3% |
| 2c5 4e | 15.1% | 3,780 | 78.5% | 19.6% | 1.9% | 0% | 51.6% | 28.3% | 12.6% | 7.4% |
| 2c5 6e | 11.6% | 2,907 | 82.2% | 17.2% | 0.6% | 0% | 54.1% | 27.9% | 12.0% | 6.1% |
| 2c5 8e | 10.8% | 2,698 | 86.5% | 13.5% | 0% | 0% | 59.8% | 27.5% | 7.6% | 5.1% |
| 2c4 0e | 58.0% | 14,488 | 59.2% | 30.9% | 9.0% | 0.9% | 35.7% | 28.3% | 16.5% | 19.5% |
| 2c4 2e | 43.5% | 10,885 | 62.8% | 28.2% | 8.5% | 0.5% | 39.8% | 28.5% | 16.9% | 14.8% |
| 2c4 4e | 38.0% | 9,489 | 64.0% | 27.1% | 7.9% | 1.0% | 39.4% | 29.3% | 16.2% | 15.2% |
| 2c4 6e | 35.0% | 8,742 | 68.4% | 27.0% | 4.5% | 0% | 42.7% | 30.4% | 16.2% | 10.7% |
| 2c4 8e | 24.0% | 6,003 | 76.5% | 21.8% | 1.7% | 0% | 47.5% | 30.6% | 14.4% | 7.6% |
| 0c3 0e | 26.1% | 6,517 | 71.4% | 28.6% | 0% | 0% | 40.8% | 37.1% | 18.7% | 3.3% |
| 0c3 2e | 17.4% | 4,348 | 60.6% | 35.8% | 3.6% | 0% | 35.4% | 35.7% | 19.9% | 9.0% |
| 0c3 4e | 9.2% | 2,312 | 72.6% | 27.4% | 0% | 0% | 45.1% | 35.0% | 16.7% | 3.2% |
| 0c3 6e | 17.4% | 4,360 | 59.0% | 36.7% | 4.3% | 0% | 33.8% | 35.4% | 20.8% | 10.0% |
| 0c3 8e | 25.1% | 6,276 | 71.5% | 28.5% | 0% | 0% | 42.1% | 37.9% | 17.6% | 2.4% |
| 4a2 0e | 28.5% | 7,116 | 75.6% | 22.0% | 2.5% | 0% | 48.7% | 31.4% | 12.2% | 7.7% |
| 4a2 2e | 39.6% | 9,903 | 64.7% | 27.3% | 8.1% | 0% | 41.7% | 29.2% | 15.3% | 13.8% |
| 4a2 4e | 63.5% | 15,879 | 40.9% | 29.2% | 19.9% | 10.0% | 25.4% | 24.0% | 17.7% | 32.9% |
| 4a1 0e | 70.2% | 17,562 | 76.3% | 20.2% | 3.2% | 0.3% | 51.6% | 27.1% | 11.7% | 9.5% |
| 4a1 2e | 87.8% | 21,957 | 62.0% | 25.6% | 9.8% | 2.6% | 40.2% | 27.0% | 14.4% | 18.4% |
| 4a1 4e | 91.2% | 22,810 | 53.2% | 23.5% | 9.5% | 13.8% | 34.6% | 23.6% | 13.7% | 28.1% |
| 2c3 0e | 51.8% | 12,942 | 82.9% | 16.2% | 0.9% | 0% | 56.5% | 27.3% | 11.4% | 4.8% |
| 2c3 2e | 87.9% | 21,963 | 51.6% | 29.1% | 13.4% | 5.8% | 32.3% | 25.9% | 16.4% | 25.5% |
| 2c3 4e | 72.3% | 18,078 | 56.8% | 26.6% | 11.1% | 5.5% | 36.1% | 26.1% | 14.9% | 22.9% |
| 2c3 6e | 60.6% | 15,147 | 65.3% | 26.2% | 7.8% | 0.7% | 42.2% | 27.8% | 15.9% | 14.2% |
| 2c3 8e | 44.6% | 11,162 | 80.3% | 18.5% | 1.3% | 0% | 53.5% | 27.8% | 12.3% | 6.4% |
| 0c4 0e | 60.3% | 15,079 | 78.4% | 19.7% | 1.9% | 0% | 51.8% | 26.5% | 14.2% | 7.6% |
| 0c4 2e | 44.1% | 11,036 | 78.1% | 21.0% | 1.0% | 0% | 51.0% | 29.0% | 14.0% | 6.0% |
| 0c4 4e | 37.5% | 9,365 | 77.4% | 21.0% | 1.7% | 0% | 50.5% | 29.2% | 14.2% | 6.1% |
| 0c4 6e | 24.4% | 6,104 | 84.1% | 15.9% | 0% | 0% | 56.3% | 28.4% | 11.7% | 3.7% |
| 0c4 8e | 15.4% | 3,848 | 92.0% | 8.0% | 0% | 0% | 63.2% | 28.1% | 8.7% | 0% |
| 4c3 0e | 54.3% | 13,568 | 65.0% | 29.6% | 5.4% | 0% | 40.2% | 29.1% | 15.8% | 14.9% |
| 4c3 2e | 45.7% | 11,415 | 59.7% | 29.7% | 9.8% | 0.8% | 36.4% | 29.0% | 17.5% | 17.0% |
| 4c3 4e | 45.3% | 11,327 | 60.7% | 29.7% | 9.0% | 0.6% | 37.2% | 29.8% | 17.6% | 15.4% |
| 4c4 0e | 8.6% | 2,152 | 81.6% | 18.4% | 0% | 0% | 54.3% | 27.4% | 12.3% | 6.0% |
| 4c4 2e | 10.6% | 2,649 | 79.3% | 18.6% | 2.1% | 0% | 50.9% | 30.3% | 13.1% | 5.7% |
| 4c4 4e | 11.7% | 2,937 | 76.9% | 21.5% | 1.6% | 0% | 49.6% | 31.2% | 14.2% | 5.0% |
| 4b2 0e | 74.3% | 18,567 | 66.2% | 24.3% | 7.5% | 2.0% | 42.7% | 26.7% | 14.2% | 16.4% |
| 4b2 2e | 84.5% | 21,120 | 54.8% | 23.1% | 10.7% | 11.4% | 35.2% | 24.3% | 14.8% | 25.7% |
| 4b2 4e | 82.0% | 20,490 | 61.5% | 25.1% | 8.8% | 4.6% | 39.4% | 26.7% | 15.1% | 18.8% |
| 4b5 0e | 13.1% | 3,272 | 80.5% | 16.6% | 3.0% | 0% | 52.8% | 28.3% | 11.9% | 7.0% |
| 4b5 2e | 13.6% | 3,401 | 78.9% | 19.3% | 1.8% | 0% | 52.1% | 27.8% | 12.5% | 7.6% |
| 4b5 4e | 12.9% | 3,236 | 84.2% | 15.3% | 0.5% | 0% | 55.7% | 28.8% | 11.1% | 4.4% |

The same, edge counts pooled by their exact sizes. Each row is a corner subset:

| Corner subset | Share of its DRs that short | DRs in the sample | 0 half turns | 1 half turn | 2 half turns | 3 or more | Normal side alone: 0 | Normal side alone: 1 | Normal side alone: 2 | Normal side alone: 3 or more |
|---|---|---|---|---|---|---|---|---|---|---|
| 0c0 | 89.8% | 110,995 | 61.5% | 24.7% | 9.0% | 4.8% | 41.5% | 25.9% | 13.7% | 18.9% |
| 2c5 | 14.3% | 16,028 | 80.0% | 18.6% | 1.4% | 0% | 52.8% | 28.5% | 12.2% | 6.6% |
| 2c4 | 38.6% | 49,607 | 64.6% | 27.4% | 7.3% | 0.6% | 40.2% | 29.3% | 16.4% | 14.2% |
| 0c3 | 13.4% | 23,813 | 64.9% | 32.7% | 2.3% | 0% | 38.7% | 35.5% | 19.0% | 6.9% |
| 4a2 | 51.6% | 32,898 | 49.8% | 28.4% | 15.4% | 6.4% | 31.5% | 26.0% | 16.8% | 25.8% |
| 4a1 | 89.1% | 62,329 | 57.7% | 24.4% | 9.5% | 8.5% | 37.5% | 25.2% | 13.9% | 23.3% |
| 2c3 | 72.5% | 79,292 | 57.5% | 27.1% | 10.9% | 4.6% | 36.6% | 26.4% | 15.4% | 21.6% |
| 0c4 | 36.0% | 45,432 | 78.7% | 20.1% | 1.2% | 0% | 51.7% | 28.9% | 13.7% | 5.7% |
| 4c3 | 45.7% | 36,310 | 60.4% | 29.7% | 9.2% | 0.7% | 36.9% | 29.4% | 17.5% | 16.1% |
| 4c4 | 11.1% | 7,738 | 78.1% | 20.1% | 1.8% | 0% | 50.3% | 30.7% | 13.7% | 5.3% |
| 4b2 | 82.9% | 60,177 | 58.5% | 24.1% | 9.6% | 7.7% | 37.5% | 25.6% | 15.0% | 22.0% |
| 4b5 | 13.2% | 9,909 | 81.6% | 17.2% | 1.2% | 0% | 53.9% | 28.3% | 11.7% | 6.0% |
| all DRs | 43.4% | 534,528 | 61.5% | 25.9% | 8.8% | 3.8% | 39.0% | 27.4% | 15.4% | 18.1% |

## Optimal of 12 or less

Same columns, DRs with an optimal finish of at most 12. The high-qt rows rest on a few hundred DRs each.

| Subset × edges | Share of its DRs that short | DRs in the sample | 0 half turns | 1 half turn | 2 half turns | 3 or more | Normal side alone: 0 | Normal side alone: 1 | Normal side alone: 2 | Normal side alone: 3 or more |
|---|---|---|---|---|---|---|---|---|---|---|
| 0c0 0e | 99.3% | 24,814 | 37.9% | 18.8% | 8.3% | 35.0% | 24.7% | 17.3% | 10.4% | 47.6% |
| 0c0 2e | 79.9% | 19,978 | 53.5% | 31.0% | 11.9% | 3.5% | 34.4% | 27.5% | 16.4% | 21.8% |
| 0c0 4e | 53.0% | 13,252 | 52.4% | 27.0% | 12.8% | 7.9% | 32.8% | 25.2% | 15.3% | 26.7% |
| 0c0 6e | 27.1% | 6,780 | 70.8% | 24.2% | 5.0% | 0% | 45.1% | 28.8% | 14.4% | 11.7% |
| 0c0 8e | 38.4% | 9,598 | 57.6% | 29.2% | 11.3% | 1.9% | 35.3% | 26.9% | 16.8% | 21.0% |
| 2c5 0e | 1.5% | 373 | 94.9% | 5.1% | 0% | 0% | 70.8% | 24.1% | 5.1% | 0% |
| 2c5 2e | 2.6% | 658 | 87.1% | 12.9% | 0% | 0% | 58.7% | 29.3% | 10.5% | 1.5% |
| 2c5 4e | 2.6% | 645 | 83.1% | 16.9% | 0% | 0% | 55.0% | 29.8% | 11.9% | 3.3% |
| 2c5 6e | 1.7% | 415 | 88.0% | 12.0% | 0% | 0% | 59.0% | 27.5% | 11.8% | 1.7% |
| 2c5 8e | 1.5% | 367 | 86.6% | 13.4% | 0% | 0% | 68.7% | 21.3% | 10.1% | 0% |
| 2c4 0e | 19.9% | 4,963 | 62.3% | 30.6% | 7.1% | 0% | 35.6% | 27.2% | 17.8% | 19.3% |
| 2c4 2e | 11.3% | 2,814 | 65.9% | 27.6% | 6.5% | 0% | 41.1% | 29.6% | 16.3% | 13.0% |
| 2c4 4e | 9.1% | 2,282 | 66.2% | 27.1% | 6.7% | 0% | 38.7% | 30.5% | 16.3% | 14.5% |
| 2c4 6e | 7.7% | 1,914 | 75.3% | 22.2% | 2.5% | 0% | 47.4% | 28.9% | 16.4% | 7.3% |
| 2c4 8e | 4.4% | 1,091 | 83.6% | 16.4% | 0% | 0% | 52.0% | 31.3% | 12.2% | 4.6% |
| 0c3 0e | 5.5% | 1,381 | 89.6% | 10.4% | 0% | 0% | 54.8% | 36.1% | 9.1% | 0% |
| 0c3 2e | 3.7% | 915 | 74.1% | 25.9% | 0% | 0% | 45.7% | 32.8% | 17.6% | 3.9% |
| 0c3 4e | 1.5% | 378 | 84.1% | 15.9% | 0% | 0% | 52.1% | 38.4% | 9.5% | 0% |
| 0c3 6e | 3.7% | 921 | 74.0% | 26.0% | 0% | 0% | 45.1% | 33.3% | 17.7% | 3.9% |
| 0c3 8e | 5.6% | 1,396 | 90.2% | 9.8% | 0% | 0% | 53.9% | 37.0% | 9.1% | 0% |
| 4a2 0e | 6.1% | 1,526 | 79.9% | 20.1% | 0% | 0% | 54.7% | 29.7% | 10.4% | 5.3% |
| 4a2 2e | 10.5% | 2,615 | 66.6% | 29.9% | 3.5% | 0% | 42.3% | 28.3% | 16.1% | 13.3% |
| 4a2 4e | 26.2% | 6,545 | 39.5% | 32.4% | 21.6% | 6.4% | 23.3% | 23.2% | 18.7% | 34.8% |
| 4a1 0e | 24.1% | 6,031 | 74.9% | 21.8% | 3.3% | 0% | 48.3% | 27.2% | 14.1% | 10.4% |
| 4a1 2e | 42.9% | 10,726 | 57.4% | 28.6% | 11.9% | 2.0% | 34.8% | 26.8% | 16.4% | 22.0% |
| 4a1 4e | 53.1% | 13,263 | 44.9% | 24.5% | 12.0% | 18.6% | 27.5% | 22.1% | 15.1% | 35.2% |
| 2c3 0e | 11.7% | 2,933 | 85.3% | 14.7% | 0% | 0% | 57.1% | 28.8% | 12.4% | 1.7% |
| 2c3 2e | 42.2% | 10,562 | 47.3% | 31.2% | 15.7% | 5.8% | 27.8% | 24.6% | 17.7% | 29.8% |
| 2c3 4e | 27.0% | 6,741 | 52.3% | 29.3% | 13.5% | 4.8% | 31.5% | 26.2% | 16.5% | 25.8% |
| 2c3 6e | 17.0% | 4,246 | 66.5% | 27.0% | 6.5% | 0% | 41.9% | 27.4% | 17.3% | 13.4% |
| 2c3 8e | 9.4% | 2,341 | 85.7% | 14.3% | 0% | 0% | 56.3% | 28.1% | 13.2% | 2.4% |
| 0c4 0e | 17.7% | 4,428 | 79.0% | 21.0% | 0% | 0% | 51.0% | 30.5% | 13.3% | 5.2% |
| 0c4 2e | 9.1% | 2,277 | 84.2% | 15.8% | 0% | 0% | 54.5% | 29.6% | 13.6% | 2.2% |
| 0c4 4e | 7.2% | 1,801 | 84.3% | 15.7% | 0% | 0% | 55.9% | 29.2% | 12.2% | 2.7% |
| 0c4 6e | 3.7% | 913 | 89.9% | 10.1% | 0% | 0% | 63.3% | 26.8% | 9.9% | 0% |
| 0c4 8e | 1.9% | 466 | 100.0% | 0% | 0% | 0% | 79.6% | 20.4% | 0% | 0% |
| 4c3 0e | 17.1% | 4,283 | 68.5% | 28.0% | 3.5% | 0% | 41.8% | 28.0% | 17.0% | 13.1% |
| 4c3 2e | 12.0% | 2,992 | 62.2% | 30.2% | 7.6% | 0% | 36.5% | 29.3% | 18.4% | 15.8% |
| 4c3 4e | 11.8% | 2,954 | 63.4% | 30.0% | 6.5% | 0% | 39.5% | 29.5% | 18.3% | 12.6% |
| 4c4 0e | 1.3% | 317 | 86.4% | 13.6% | 0% | 0% | 60.3% | 28.4% | 11.4% | 0% |
| 4c4 2e | 1.6% | 397 | 86.4% | 13.6% | 0% | 0% | 53.7% | 30.7% | 12.8% | 2.8% |
| 4c4 4e | 1.9% | 474 | 87.1% | 12.9% | 0% | 0% | 55.5% | 30.2% | 11.6% | 2.7% |
| 4b2 0e | 28.5% | 7,113 | 62.4% | 27.4% | 8.4% | 1.9% | 38.4% | 27.3% | 16.1% | 18.2% |
| 4b2 2e | 39.3% | 9,831 | 47.4% | 25.1% | 13.6% | 13.9% | 28.9% | 23.1% | 15.9% | 32.1% |
| 4b2 4e | 34.4% | 8,610 | 56.5% | 27.2% | 10.4% | 5.9% | 33.9% | 26.5% | 17.1% | 22.5% |
| 4b5 0e | 1.9% | 474 | 83.1% | 16.9% | 0% | 0% | 55.9% | 28.1% | 11.0% | 5.1% |
| 4b5 2e | 2.0% | 508 | 82.5% | 17.5% | 0% | 0% | 55.3% | 29.7% | 11.6% | 3.3% |
| 4b5 4e | 1.8% | 440 | 90.2% | 9.8% | 0% | 0% | 62.5% | 27.0% | 8.6% | 1.8% |

Edge counts pooled. Each row is a corner subset:

| Corner subset | Share of its DRs that short | DRs in the sample | 0 half turns | 1 half turn | 2 half turns | 3 or more | Normal side alone: 0 | Normal side alone: 1 | Normal side alone: 2 | Normal side alone: 3 or more |
|---|---|---|---|---|---|---|---|---|---|---|
| 0c0 | 53.7% | 74,422 | 54.6% | 27.8% | 11.4% | 6.1% | 34.6% | 26.2% | 15.5% | 23.8% |
| 2c5 | 2.4% | 2,458 | 85.0% | 15.0% | 0% | 0% | 56.9% | 29.2% | 11.5% | 2.5% |
| 2c4 | 9.4% | 13,064 | 67.8% | 26.4% | 5.8% | 0% | 41.0% | 29.9% | 16.3% | 12.8% |
| 0c3 | 2.6% | 4,991 | 78.0% | 22.0% | 0% | 0% | 47.9% | 34.9% | 14.7% | 2.5% |
| 4a2 | 18.4% | 10,686 | 46.9% | 31.6% | 16.7% | 4.7% | 28.5% | 24.6% | 17.9% | 28.9% |
| 4a1 | 47.6% | 30,020 | 50.5% | 26.1% | 11.8% | 11.5% | 30.8% | 24.1% | 15.6% | 29.4% |
| 2c3 | 27.7% | 26,823 | 52.9% | 29.5% | 13.1% | 4.4% | 32.0% | 25.9% | 17.0% | 25.2% |
| 0c4 | 6.9% | 9,885 | 84.8% | 15.2% | 0% | 0% | 56.3% | 29.1% | 12.3% | 2.3% |
| 4c3 | 12.0% | 10,229 | 63.1% | 30.0% | 6.9% | 0% | 38.2% | 29.3% | 18.3% | 14.1% |
| 4c4 | 1.7% | 1,188 | 86.8% | 13.2% | 0% | 0% | 54.8% | 30.4% | 12.1% | 2.7% |
| 4b2 | 36.5% | 25,554 | 52.2% | 26.2% | 11.9% | 9.8% | 31.6% | 24.8% | 16.5% | 27.1% |
| 4b5 | 1.9% | 1,422 | 86.2% | 13.8% | 0% | 0% | 58.8% | 28.4% | 10.2% | 2.7% |
| all DRs | 14.7% | 210,742 | 56.9% | 27.2% | 10.5% | 5.4% | 34.7% | 26.5% | 16.5% | 22.3% |

## All DRs

Same columns, every DR of the subset × edges (25,000 sampled each).

| Subset × edges | 0 half turns | 1 half turn | 2 half turns | 3 or more | Normal side alone: 0 | Normal side alone: 1 | Normal side alone: 2 | Normal side alone: 3 or more |
|---|---|---|---|---|---|---|---|---|
| 0c0 0e | 38.3% | 18.7% | 8.3% | 34.8% | 25.2% | 17.3% | 10.3% | 47.2% |
| 0c0 2e | 58.3% | 28.1% | 10.5% | 3.1% | 39.7% | 26.9% | 14.7% | 18.7% |
| 0c0 4e | 62.3% | 22.6% | 9.2% | 5.8% | 43.6% | 24.2% | 12.7% | 19.5% |
| 0c0 6e | 77.0% | 18.9% | 3.7% | 0.4% | 56.2% | 24.6% | 10.5% | 8.6% |
| 0c0 8e | 66.3% | 22.9% | 8.5% | 2.3% | 46.4% | 24.5% | 13.6% | 15.5% |
| 2c5 0e | 88.4% | 11.1% | 0.5% | 0% | 67.4% | 23.0% | 7.0% | 2.7% |
| 2c5 2e | 83.2% | 15.1% | 1.7% | <0.1% | 61.7% | 25.7% | 8.2% | 4.3% |
| 2c5 4e | 82.0% | 15.4% | 2.5% | 0.1% | 60.3% | 25.1% | 9.2% | 5.5% |
| 2c5 6e | 83.1% | 15.0% | 1.9% | <0.1% | 61.8% | 25.1% | 8.6% | 4.6% |
| 2c5 8e | 86.6% | 12.1% | 1.3% | 0% | 65.6% | 23.7% | 7.6% | 3.2% |
| 2c4 0e | 59.9% | 30.0% | 8.8% | 1.3% | 38.2% | 29.8% | 15.4% | 16.6% |
| 2c4 2e | 65.4% | 27.0% | 6.6% | 1.0% | 43.6% | 31.2% | 13.6% | 11.6% |
| 2c4 4e | 65.7% | 26.5% | 6.4% | 1.4% | 43.9% | 31.7% | 13.1% | 11.3% |
| 2c4 6e | 68.4% | 26.7% | 4.5% | 0.3% | 45.7% | 32.9% | 12.9% | 8.6% |
| 2c4 8e | 72.4% | 24.9% | 2.7% | 0.1% | 48.7% | 32.7% | 11.8% | 6.8% |
| 0c3 0e | 64.8% | 34.0% | 1.2% | 0% | 43.8% | 37.6% | 14.1% | 4.5% |
| 0c3 2e | 60.3% | 34.7% | 4.8% | 0.1% | 41.0% | 37.5% | 13.7% | 7.8% |
| 0c3 4e | 69.5% | 26.9% | 3.6% | 0% | 50.0% | 32.2% | 12.7% | 5.1% |
| 0c3 6e | 57.0% | 37.2% | 5.6% | 0.1% | 37.2% | 38.9% | 15.2% | 8.7% |
| 0c3 8e | 64.2% | 34.7% | 1.1% | 0% | 42.0% | 40.9% | 13.2% | 3.9% |
| 4a2 0e | 75.7% | 22.0% | 2.3% | <0.1% | 51.8% | 32.1% | 10.4% | 5.8% |
| 4a2 2e | 67.9% | 24.0% | 7.0% | 1.2% | 46.0% | 30.7% | 12.2% | 11.1% |
| 4a2 4e | 46.7% | 25.8% | 16.5% | 10.9% | 30.5% | 24.7% | 16.1% | 28.7% |
| 4a1 0e | 79.2% | 17.8% | 2.8% | 0.3% | 57.1% | 25.9% | 9.5% | 7.4% |
| 4a1 2e | 65.5% | 23.5% | 8.6% | 2.3% | 44.5% | 26.2% | 13.0% | 16.4% |
| 4a1 4e | 56.2% | 22.3% | 8.8% | 12.7% | 37.8% | 23.4% | 12.8% | 26.0% |
| 2c3 0e | 85.2% | 14.0% | 0.8% | 0% | 63.5% | 24.6% | 8.2% | 3.7% |
| 2c3 2e | 54.6% | 28.1% | 12.1% | 5.2% | 35.2% | 26.8% | 15.2% | 22.8% |
| 2c3 4e | 61.5% | 24.9% | 9.1% | 4.5% | 41.2% | 26.9% | 13.3% | 18.6% |
| 2c3 6e | 69.8% | 23.4% | 6.1% | 0.7% | 48.3% | 27.9% | 12.9% | 10.9% |
| 2c3 8e | 83.2% | 15.4% | 1.3% | <0.1% | 61.3% | 24.8% | 8.9% | 5.0% |
| 0c4 0e | 83.3% | 15.1% | 1.5% | <0.1% | 62.4% | 21.5% | 10.3% | 5.7% |
| 0c4 2e | 83.8% | 15.1% | 1.1% | 0% | 62.1% | 23.9% | 9.6% | 4.4% |
| 0c4 4e | 83.6% | 14.9% | 1.6% | 0% | 62.3% | 23.3% | 9.5% | 4.8% |
| 0c4 6e | 87.7% | 11.7% | 0.6% | 0% | 67.3% | 21.6% | 7.9% | 3.2% |
| 0c4 8e | 90.3% | 9.7% | <0.1% | 0% | 72.1% | 20.6% | 6.0% | 1.3% |
| 4c3 0e | 69.4% | 25.6% | 4.8% | 0.2% | 44.8% | 29.2% | 13.2% | 12.8% |
| 4c3 2e | 64.1% | 26.3% | 8.4% | 1.2% | 42.1% | 29.1% | 15.0% | 13.8% |
| 4c3 4e | 65.8% | 25.5% | 7.5% | 1.2% | 43.0% | 29.6% | 14.8% | 12.7% |
| 4c4 0e | 83.3% | 14.6% | 2.1% | 0% | 62.6% | 24.4% | 8.4% | 4.6% |
| 4c4 2e | 79.9% | 18.0% | 2.1% | <0.1% | 58.3% | 28.2% | 9.4% | 4.2% |
| 4c4 4e | 78.6% | 19.0% | 2.3% | <0.1% | 57.4% | 27.9% | 9.8% | 4.8% |
| 4b2 0e | 72.0% | 20.5% | 6.0% | 1.6% | 50.1% | 25.0% | 12.0% | 12.9% |
| 4b2 2e | 60.0% | 20.9% | 9.2% | 9.9% | 40.6% | 23.8% | 13.3% | 22.3% |
| 4b2 4e | 66.3% | 22.4% | 7.5% | 3.9% | 45.1% | 25.7% | 13.2% | 16.0% |
| 4b5 0e | 85.2% | 13.0% | 1.8% | <0.1% | 64.6% | 22.7% | 8.1% | 4.6% |
| 4b5 2e | 84.0% | 13.8% | 2.1% | <0.1% | 62.6% | 24.2% | 8.4% | 4.9% |
| 4b5 4e | 85.9% | 13.0% | 1.1% | <0.1% | 64.3% | 24.3% | 8.0% | 3.3% |

Edge counts pooled. Each row is a corner subset:

| Corner subset | 0 half turns | 1 half turn | 2 half turns | 3 or more | Normal side alone: 0 | Normal side alone: 1 | Normal side alone: 2 | Normal side alone: 3 or more |
|---|---|---|---|---|---|---|---|---|
| 0c0 | 64.5% | 23.0% | 8.2% | 4.3% | 45.3% | 24.8% | 12.6% | 17.2% |
| 2c5 | 82.7% | 15.1% | 2.1% | 0.1% | 61.1% | 25.2% | 8.8% | 4.9% |
| 2c4 | 66.3% | 26.7% | 6.0% | 1.0% | 44.2% | 31.8% | 13.2% | 10.8% |
| 0c3 | 64.4% | 31.3% | 4.3% | 0.1% | 44.8% | 35.2% | 13.5% | 6.5% |
| 4a2 | 57.2% | 24.9% | 11.8% | 6.1% | 38.2% | 27.7% | 14.1% | 20.0% |
| 4a1 | 61.1% | 22.7% | 8.6% | 7.6% | 41.4% | 24.7% | 12.8% | 21.0% |
| 2c3 | 62.5% | 25.0% | 8.9% | 3.6% | 42.1% | 27.1% | 13.5% | 17.4% |
| 0c4 | 84.6% | 14.1% | 1.2% | <0.1% | 63.6% | 23.0% | 9.1% | 4.3% |
| 4c3 | 65.2% | 25.8% | 7.9% | 1.2% | 42.6% | 29.4% | 14.8% | 13.2% |
| 4c4 | 79.3% | 18.4% | 2.2% | <0.1% | 58.0% | 27.9% | 9.6% | 4.5% |
| 4b2 | 63.6% | 21.6% | 8.2% | 6.5% | 43.2% | 24.8% | 13.2% | 18.8% |
| 4b5 | 85.0% | 13.4% | 1.6% | <0.1% | 63.5% | 24.2% | 8.2% | 4.1% |
| all DRs | 69.9% | 22.2% | 5.9% | 2.1% | 48.6% | 27.8% | 12.1% | 11.5% |

## When the first quarter turn has to make progress

The tables above count any optimal finish. On a 2qt subset that includes the optimal finishes with four quarter turns, and those are what fills its *0 half turns* column: on a 4b2 whose corners need a half turn first (4b2 parity) no quarter turn makes progress, and an optimal still starts with one, the first of four. This section counts only the finishes that don't do that.

**No extra quarter turn.** Every DR has a fewest number of quarter turns that any finish of it can have. It's the corners' count (2 on 4b2 and 4a2, 3 on 2c3, and so on) on every subset but two: on 4a1 0e and 4a1 2e one quarter turn can't fix the edges and it's 3, and on 0c0 outside HTR it's 2. A finish with exactly that many has *no extra quarter turn*; on 4b2 or 4a2 that's a 2qt finish, which is what not using 4q means. Half turns never change the number and a quarter turn changes it by exactly one, so on such a finish every quarter turn lowers it. If the finish starts with a quarter turn, that turn makes progress, and on every row where the number is the corners' count it lowers the corners' count: the side was ready, in the words of the next section.

**How common the extra quarter turns are** was measured on the server before. rodneykinney ([13 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1063355084697784371)): "How often does the optimal DR finish use more QT than the optimal corner finish? Surprisingly often! For example, 57% of the time, the optimal solution uses 4QT for a 2QT corner case." Lichi Fang ([6 Aug 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1137835695721939094)): "I shockingly discovered that over 60% the optimal solution for htr subset 2qt(a) 4c4e (the R U2 F2 R' case) use 4qt rather than 2qt. How are they possibly findable?" [*Which HTR routes to try from a DR*](../htr-routes/#7-extra-quarter-turns-and-the-last-dr-move) (section 7) checks both: on 4a2 and 4b2 together every optimal uses 4 or more quarter turns on 53.9% of DRs and some optimal does on 80.7%; on 4b2 4e it's 63.7% and 86.9%. Its verdict is that both quotes fit: the 57% read as every optimal, or as one leave-slice optimal picked at random (56.3%), and the over 60% as every optimal of 4b2 4e.

The two 2qt subsets. Each row is a subset × edges and a group of its DRs. The first two cells are the shares where every optimal, and where some optimal, has 4 or more quarter turns. Then the *0 half turns* share of the main tables, split in two: a 2qt optimal starts with the quarter turn on one of the sides, or only an optimal with 4 or more quarter turns does. Sampled, 25,000 per subset × edges:

| Subset | DRs counted | Every optimal has 4 or more quarter turns | Some optimal has 4 or more | 0 half turns, as in the main table | A 2qt optimal starts with the quarter turn | Only an optimal with 4 or more quarter turns does |
|---|---|---|---|---|---|---|
| 4b2 0e | All DRs | 55.0% | 80.8% | 72.0% | 13.6% | 58.4% |
| 4b2 0e | Optimal ≤ 13 | 57.5% | 74.9% | 66.2% | 14.3% | 51.9% |
| 4b2 2e | All DRs | 45.2% | 77.7% | 60.0% | 5.7% | 54.3% |
| 4b2 2e | Optimal ≤ 13 | 48.6% | 74.0% | 54.8% | 6.0% | 48.8% |
| 4b2 4e | All DRs | 63.7% | 86.9% | 66.3% | 5.2% | 61.1% |
| 4b2 4e | Optimal ≤ 13 | 66.1% | 84.3% | 61.5% | 5.6% | 55.9% |
| 4b2, edge counts pooled | All DRs | 55.0% | 82.6% | 63.6% | 5.7% | 57.9% |
| 4b2, edge counts pooled | Optimal ≤ 13 | 57.7% | 79.2% | 58.5% | 6.0% | 52.5% |
| 4a2 0e | All DRs | 96.0% | 99.5% | 75.7% | 1.8% | 73.8% |
| 4a2 0e | Optimal ≤ 13 | 97.3% | 98.8% | 75.6% | 2.2% | 73.4% |
| 4a2 2e | All DRs | 65.8% | 86.6% | 67.9% | 6.4% | 61.5% |
| 4a2 2e | Optimal ≤ 13 | 67.3% | 77.1% | 64.7% | 10.7% | 54.0% |
| 4a2 4e | All DRs | 32.1% | 60.0% | 46.7% | 8.5% | 38.3% |
| 4a2 4e | Optimal ≤ 13 | 31.2% | 49.1% | 40.9% | 12.2% | 28.7% |
| 4a2, edge counts pooled | All DRs | 49.4% | 73.3% | 57.2% | 7.3% | 49.9% |
| 4a2, edge counts pooled | Optimal ≤ 13 | 44.9% | 59.7% | 49.8% | 11.5% | 38.3% |

So on 4b2 a quarter turn at once belongs to a 2qt optimal on 5.7% of DRs, and the other 57.9% of its 63.6% are 4qt optimals. They're not rare finishes: every optimal of a 4b2 has 4 or more quarter turns on 55.0% of its DRs.

A 4b2 2e like that, replayed. Neither side is ready (4b2-3 on normal, 4b2-3 on inverse: the corners need 2 half turns before a quarter turn lowers them, on either side). Its optimal starts with a quarter turn all the same, and both optimal finishes have 4 quarter turns:

```
L2 D2 F2 L2 U B2 D' L2 D' L2 R2 U' // 4b2 2e, 12 optimal; corners 4b2-3 on normal, 4b2-3 on inverse
U R2 L2 D L2 D B2 U' L2 F2 D2 L2 // optimal finish, 4 quarter turns: 0 half turns before the first qt on normal, 4 on inverse
U L2 R2 D L2 D B2 U' L2 F2 D2 L2 // the other optimal finish, 4 quarter turns: 0 half turns before the first qt on normal, 4 on inverse
```

The same split for every corner subset, edge counts pooled. Each row is a corner subset; the first three cells are over all its DRs, the last three over those with an optimal of 13 or less:

| Corner subset | All DRs: 0 half turns, as in the main table | All DRs: a finish with no extra quarter turn starts with the quarter turn | All DRs: only finishes with extra quarter turns do | Optimal ≤ 13: 0 half turns, as in the main table | Optimal ≤ 13: a finish with no extra quarter turn starts with the quarter turn | Optimal ≤ 13: only finishes with extra quarter turns do |
|---|---|---|---|---|---|---|
| 0c0 | 64.5% | 17.2% | 47.2% | 61.5% | 17.0% | 44.5% |
| 2c5 | 82.7% | 77.8% | 4.9% | 80.0% | 79.0% | 1.0% |
| 2c4 | 66.3% | 51.6% | 14.7% | 64.6% | 57.6% | 7.1% |
| 0c3 | 64.4% | 32.4% | 32.1% | 64.9% | 58.3% | 6.6% |
| 4a2 | 57.2% | 7.3% | 49.9% | 49.8% | 11.5% | 38.3% |
| 4a1 | 61.1% | 20.8% | 40.3% | 57.7% | 19.3% | 38.4% |
| 2c3 | 62.5% | 32.5% | 30.0% | 57.5% | 32.6% | 24.9% |
| 0c4 | 84.6% | 71.1% | 13.6% | 78.7% | 65.4% | 13.3% |
| 4c3 | 65.2% | 26.7% | 38.5% | 60.4% | 30.7% | 29.7% |
| 4c4 | 79.3% | 38.6% | 40.7% | 78.1% | 51.1% | 27.0% |
| 4b2 | 63.6% | 5.7% | 57.9% | 58.5% | 6.0% | 52.5% |
| 4b5 | 85.0% | 81.9% | 3.1% | 81.6% | 80.6% | 1.0% |
| all DRs | 69.9% | 42.2% | 27.7% | 61.5% | 33.7% | 27.8% |

On 2c5 and 4b5 a quarter turn at once nearly always makes progress, and on 2c4 and 0c4 mostly. On 4a2, 4b2, 0c0 and 4a1 it mostly doesn't, and on 2c3, 0c3, 4c3 and 4c4 it's about half and half.

Every subset × edges, all DRs:

| Subset × edges | 0 half turns, as in the main table | A finish with no extra quarter turn starts with the quarter turn | Only finishes with extra quarter turns do |
|---|---|---|---|
| 0c0 0e | 38.3% | 22.9% | 15.3% |
| 0c0 2e | 58.3% | 22.6% | 35.7% |
| 0c0 4e | 62.3% | 14.0% | 48.3% |
| 0c0 6e | 77.0% | 17.5% | 59.5% |
| 0c0 8e | 66.3% | 37.0% | 29.2% |
| 2c5 0e | 88.4% | 82.6% | 5.9% |
| 2c5 2e | 83.2% | 77.9% | 5.3% |
| 2c5 4e | 82.0% | 77.3% | 4.7% |
| 2c5 6e | 83.1% | 78.1% | 5.0% |
| 2c5 8e | 86.6% | 81.7% | 4.9% |
| 2c4 0e | 59.9% | 49.1% | 10.8% |
| 2c4 2e | 65.4% | 51.5% | 13.9% |
| 2c4 4e | 65.7% | 50.4% | 15.4% |
| 2c4 6e | 68.4% | 54.0% | 14.4% |
| 2c4 8e | 72.4% | 58.9% | 13.5% |
| 0c3 0e | 64.8% | 45.2% | 19.5% |
| 0c3 2e | 60.3% | 34.0% | 26.3% |
| 0c3 4e | 69.5% | 30.0% | 39.6% |
| 0c3 6e | 57.0% | 34.3% | 22.7% |
| 0c3 8e | 64.2% | 46.9% | 17.3% |
| 4a2 0e | 75.7% | 1.8% | 73.8% |
| 4a2 2e | 67.9% | 6.4% | 61.5% |
| 4a2 4e | 46.7% | 8.5% | 38.3% |
| 4a1 0e | 79.2% | 29.5% | 49.6% |
| 4a1 2e | 65.5% | 43.0% | 22.5% |
| 4a1 4e | 56.2% | 0.6% | 55.7% |
| 2c3 0e | 85.2% | 27.1% | 58.0% |
| 2c3 2e | 54.6% | 33.2% | 21.4% |
| 2c3 4e | 61.5% | 31.7% | 29.8% |
| 2c3 6e | 69.8% | 34.4% | 35.4% |
| 2c3 8e | 83.2% | 25.4% | 57.8% |
| 0c4 0e | 83.3% | 75.4% | 7.9% |
| 0c4 2e | 83.8% | 72.1% | 11.7% |
| 0c4 4e | 83.6% | 69.9% | 13.6% |
| 0c4 6e | 87.7% | 71.6% | 16.1% |
| 0c4 8e | 90.3% | 81.2% | 9.1% |
| 4c3 0e | 69.4% | 35.7% | 33.7% |
| 4c3 2e | 64.1% | 26.6% | 37.5% |
| 4c3 4e | 65.8% | 26.3% | 39.6% |
| 4c4 0e | 83.3% | 36.4% | 47.0% |
| 4c4 2e | 79.9% | 38.3% | 41.5% |
| 4c4 4e | 78.6% | 39.0% | 39.6% |
| 4b2 0e | 72.0% | 13.6% | 58.4% |
| 4b2 2e | 60.0% | 5.7% | 54.3% |
| 4b2 4e | 66.3% | 5.2% | 61.1% |
| 4b5 0e | 85.2% | 82.0% | 3.2% |
| 4b5 2e | 84.0% | 80.8% | 3.3% |
| 4b5 4e | 85.9% | 82.9% | 3.0% |

### Counting only finishes with no extra quarter turn

The main tables again, counting only the optimal finishes with no extra quarter turn. A DR whose every optimal has extra quarter turns has no such finish and can't be 0, 1, 2 or 3 or more, so it gets its own column, and the five shares add up to all the DRs of the row. *Quarter turns in such a finish* is the fewest any finish can have. Better side, chosen with hindsight, as above.

Optimal of 13 or less. Each row is a subset × edges:

| Subset × edges | Share of its DRs that short | DRs in the sample | Quarter turns in such a finish | No optimal without extra quarter turns | 0 half turns | 1 half turn | 2 half turns | 3 or more |
|---|---|---|---|---|---|---|---|---|
| 0c0 0e | 100.0% | 25,000 | 0 or 2 | 8.8% | 22.9% | 13.8% | 7.5% | 47.0% |
| 0c0 2e | 98.8% | 24,701 | 2 | 30.1% | 22.4% | 26.9% | 14.9% | 5.7% |
| 0c0 4e | 92.3% | 23,082 | 2 | 41.2% | 13.8% | 20.2% | 13.5% | 11.3% |
| 0c0 6e | 75.2% | 18,805 | 2 | 58.5% | 17.0% | 16.1% | 7.3% | 1.0% |
| 0c0 8e | 77.6% | 19,407 | 2 | 23.1% | 35.3% | 25.5% | 12.4% | 3.6% |
| 2c5 0e | 11.2% | 2,798 | 5 | 1.2% | 88.1% | 10.7% | 0% | 0% |
| 2c5 2e | 15.4% | 3,845 | 5 | 1.1% | 79.8% | 18.0% | 1.1% | 0% |
| 2c5 4e | 15.1% | 3,780 | 5 | 0.8% | 77.6% | 19.7% | 1.9% | 0% |
| 2c5 6e | 11.6% | 2,907 | 5 | 0.9% | 81.3% | 17.3% | 0.6% | 0% |
| 2c5 8e | 10.8% | 2,698 | 5 | 1.1% | 85.4% | 13.5% | 0% | 0% |
| 2c4 0e | 58.0% | 14,488 | 4 | 3.8% | 53.8% | 32.0% | 9.4% | 0.9% |
| 2c4 2e | 43.5% | 10,885 | 4 | 5.5% | 55.7% | 29.3% | 9.0% | 0.5% |
| 2c4 4e | 38.0% | 9,489 | 4 | 6.2% | 56.6% | 27.6% | 8.5% | 1.1% |
| 2c4 6e | 35.0% | 8,742 | 4 | 5.5% | 61.9% | 27.9% | 4.8% | 0% |
| 2c4 8e | 24.0% | 6,003 | 4 | 3.3% | 72.8% | 22.2% | 1.7% | 0% |
| 0c3 0e | 26.1% | 6,517 | 3 | 1.7% | 69.7% | 28.6% | 0% | 0% |
| 0c3 2e | 17.4% | 4,348 | 3 | 5.0% | 55.4% | 35.9% | 3.7% | 0% |
| 0c3 4e | 9.2% | 2,312 | 3 | 10.5% | 61.9% | 27.6% | 0% | 0% |
| 0c3 6e | 17.4% | 4,360 | 3 | 4.2% | 54.7% | 36.8% | 4.3% | 0% |
| 0c3 8e | 25.1% | 6,276 | 3 | 1.2% | 70.3% | 28.5% | 0% | 0% |
| 4a2 0e | 28.5% | 7,116 | 2 | 97.3% | 2.2% | 0.4% | 0% | 0% |
| 4a2 2e | 39.6% | 9,903 | 2 | 67.3% | 10.7% | 14.6% | 7.5% | 0% |
| 4a2 4e | 63.5% | 15,879 | 2 | 31.2% | 12.2% | 22.0% | 22.2% | 12.4% |
| 4a1 0e | 70.2% | 17,562 | 3 | 51.4% | 28.8% | 15.1% | 4.2% | 0.5% |
| 4a1 2e | 87.8% | 21,957 | 3 | 14.7% | 40.7% | 28.1% | 12.9% | 3.6% |
| 4a1 4e | 91.2% | 22,810 | 1 | 66.3% | 0.6% | 2.0% | 4.4% | 26.8% |
| 2c3 0e | 51.8% | 12,942 | 3 | 56.3% | 29.1% | 13.3% | 1.3% | 0% |
| 2c3 2e | 87.9% | 21,963 | 3 | 11.3% | 32.6% | 30.6% | 17.6% | 7.9% |
| 2c3 4e | 72.3% | 18,078 | 3 | 19.3% | 31.7% | 27.2% | 14.6% | 7.2% |
| 2c3 6e | 60.6% | 15,147 | 3 | 26.3% | 35.5% | 27.2% | 10.1% | 1.0% |
| 2c3 8e | 44.6% | 11,162 | 3 | 59.6% | 26.2% | 12.5% | 1.7% | 0% |
| 0c4 0e | 60.3% | 15,079 | 4 | 7.8% | 69.2% | 21.0% | 2.0% | 0% |
| 0c4 2e | 44.1% | 11,036 | 4 | 11.0% | 66.4% | 21.6% | 1.1% | 0% |
| 0c4 4e | 37.5% | 9,365 | 4 | 13.6% | 63.7% | 21.0% | 1.7% | 0% |
| 0c4 6e | 24.4% | 6,104 | 4 | 16.1% | 68.2% | 15.7% | 0% | 0% |
| 0c4 8e | 15.4% | 3,848 | 4 | 7.6% | 84.5% | 8.0% | 0% | 0% |
| 4c3 0e | 54.3% | 13,568 | 3 | 25.2% | 39.6% | 28.6% | 6.6% | 0% |
| 4c3 2e | 45.7% | 11,415 | 3 | 29.8% | 31.0% | 26.7% | 11.4% | 1.1% |
| 4c3 4e | 45.3% | 11,327 | 3 | 33.5% | 29.9% | 25.5% | 10.4% | 0.7% |
| 4c4 0e | 8.6% | 2,152 | 4 | 27.5% | 53.6% | 18.9% | 0% | 0% |
| 4c4 2e | 10.6% | 2,649 | 4 | 30.2% | 50.8% | 16.9% | 2.2% | 0% |
| 4c4 4e | 11.7% | 2,937 | 4 | 26.2% | 51.3% | 20.8% | 1.7% | 0% |
| 4b2 0e | 74.3% | 18,567 | 2 | 57.5% | 14.3% | 14.8% | 9.7% | 3.6% |
| 4b2 2e | 84.5% | 21,120 | 2 | 48.6% | 6.0% | 10.8% | 13.1% | 21.5% |
| 4b2 4e | 82.0% | 20,490 | 2 | 66.1% | 5.6% | 9.4% | 9.2% | 9.7% |
| 4b5 0e | 13.1% | 3,272 | 5 | 1.0% | 79.1% | 16.9% | 3.0% | 0% |
| 4b5 2e | 13.6% | 3,401 | 5 | 1.0% | 77.8% | 19.4% | 1.8% | 0% |
| 4b5 4e | 12.9% | 3,236 | 5 | 0.8% | 83.3% | 15.3% | 0.5% | 0% |

Edge counts pooled. Each row is a corner subset:

| Corner subset | Share of its DRs that short | DRs in the sample | Quarter turns in such a finish | No optimal without extra quarter turns | 0 half turns | 1 half turn | 2 half turns | 3 or more |
|---|---|---|---|---|---|---|---|---|
| 0c0 | 89.8% | 110,995 | 0 or 2 | 41.0% | 17.0% | 21.1% | 12.6% | 8.4% |
| 2c5 | 14.3% | 16,028 | 5 | 0.9% | 79.0% | 18.7% | 1.4% | 0% |
| 2c4 | 38.6% | 49,607 | 4 | 5.8% | 57.6% | 28.1% | 7.8% | 0.7% |
| 0c3 | 13.4% | 23,813 | 3 | 6.5% | 58.3% | 32.8% | 2.4% | 0% |
| 4a2 | 51.6% | 32,898 | 2 | 44.9% | 11.5% | 19.1% | 16.7% | 7.9% |
| 4a1 | 89.1% | 62,329 | 1 or 3 | 42.7% | 19.3% | 14.0% | 8.2% | 15.7% |
| 2c3 | 72.5% | 79,292 | 3 | 19.2% | 32.6% | 27.9% | 14.3% | 6.1% |
| 0c4 | 36.0% | 45,432 | 4 | 13.1% | 65.4% | 20.3% | 1.3% | 0% |
| 4c3 | 45.7% | 36,310 | 3 | 31.5% | 30.7% | 26.2% | 10.7% | 0.9% |
| 4c4 | 11.1% | 7,738 | 4 | 28.0% | 51.1% | 19.1% | 1.9% | 0% |
| 4b2 | 82.9% | 60,177 | 2 | 57.7% | 6.0% | 10.2% | 11.0% | 15.1% |
| 4b5 | 13.2% | 9,909 | 5 | 0.9% | 80.6% | 17.3% | 1.2% | 0% |
| all DRs | 43.4% | 534,528 | 0 to 5 | 27.9% | 33.7% | 21.8% | 10.3% | 6.3% |

Optimal of 12 or less:

| Subset × edges | Share of its DRs that short | DRs in the sample | Quarter turns in such a finish | No optimal without extra quarter turns | 0 half turns | 1 half turn | 2 half turns | 3 or more |
|---|---|---|---|---|---|---|---|---|
| 0c0 0e | 99.3% | 24,814 | 0 or 2 | 8.8% | 22.6% | 13.9% | 7.5% | 47.2% |
| 0c0 2e | 79.9% | 19,978 | 2 | 32.1% | 21.6% | 26.2% | 14.9% | 5.3% |
| 0c0 4e | 53.0% | 13,252 | 2 | 42.3% | 15.1% | 19.3% | 13.1% | 10.2% |
| 0c0 6e | 27.1% | 6,780 | 2 | 56.8% | 21.1% | 16.1% | 6.0% | 0% |
| 0c0 8e | 38.4% | 9,598 | 2 | 22.4% | 37.0% | 26.5% | 12.0% | 2.1% |
| 2c5 0e | 1.5% | 373 | 5 | 0% | 94.9% | 5.1% | 0% | 0% |
| 2c5 2e | 2.6% | 658 | 5 | 0% | 87.1% | 12.9% | 0% | 0% |
| 2c5 4e | 2.6% | 645 | 5 | 0% | 83.1% | 16.9% | 0% | 0% |
| 2c5 6e | 1.7% | 415 | 5 | 0% | 88.0% | 12.0% | 0% | 0% |
| 2c5 8e | 1.5% | 367 | 5 | 0% | 86.6% | 13.4% | 0% | 0% |
| 2c4 0e | 19.9% | 4,963 | 4 | 2.0% | 59.5% | 31.3% | 7.2% | 0% |
| 2c4 2e | 11.3% | 2,814 | 4 | 3.6% | 61.6% | 28.2% | 6.6% | 0% |
| 2c4 4e | 9.1% | 2,282 | 4 | 2.8% | 62.9% | 27.3% | 6.9% | 0% |
| 2c4 6e | 7.7% | 1,914 | 4 | 3.4% | 71.6% | 22.4% | 2.6% | 0% |
| 2c4 8e | 4.4% | 1,091 | 4 | 0.8% | 82.8% | 16.4% | 0% | 0% |
| 0c3 0e | 5.5% | 1,381 | 3 | 0% | 89.6% | 10.4% | 0% | 0% |
| 0c3 2e | 3.7% | 915 | 3 | 0.8% | 73.3% | 25.9% | 0% | 0% |
| 0c3 4e | 1.5% | 378 | 3 | 1.3% | 82.8% | 15.9% | 0% | 0% |
| 0c3 6e | 3.7% | 921 | 3 | 0.5% | 73.5% | 26.0% | 0% | 0% |
| 0c3 8e | 5.6% | 1,396 | 3 | 0% | 90.2% | 9.8% | 0% | 0% |
| 4a2 0e | 6.1% | 1,526 | 2 | 98.0% | 2.0% | 0% | 0% | 0% |
| 4a2 2e | 10.5% | 2,615 | 2 | 61.3% | 17.7% | 18.1% | 2.9% | 0% |
| 4a2 4e | 26.2% | 6,545 | 2 | 25.8% | 18.6% | 26.4% | 22.3% | 6.8% |
| 4a1 0e | 24.1% | 6,031 | 3 | 47.8% | 32.2% | 16.3% | 3.7% | 0% |
| 4a1 2e | 42.9% | 10,726 | 3 | 14.9% | 41.2% | 28.3% | 13.5% | 2.2% |
| 4a1 4e | 53.1% | 13,263 | 1 | 63.0% | 1.1% | 3.2% | 6.5% | 26.3% |
| 2c3 0e | 11.7% | 2,933 | 3 | 52.2% | 36.8% | 11.0% | 0% | 0% |
| 2c3 2e | 42.2% | 10,562 | 3 | 11.7% | 33.4% | 30.4% | 18.0% | 6.5% |
| 2c3 4e | 27.0% | 6,741 | 3 | 16.4% | 34.9% | 28.3% | 15.1% | 5.3% |
| 2c3 6e | 17.0% | 4,246 | 3 | 22.3% | 44.4% | 26.4% | 6.9% | 0% |
| 2c3 8e | 9.4% | 2,341 | 3 | 57.3% | 32.7% | 10.0% | 0% | 0% |
| 0c4 0e | 17.7% | 4,428 | 4 | 8.6% | 69.7% | 21.6% | 0% | 0% |
| 0c4 2e | 9.1% | 2,277 | 4 | 8.0% | 76.2% | 15.8% | 0% | 0% |
| 0c4 4e | 7.2% | 1,801 | 4 | 9.8% | 74.5% | 15.7% | 0% | 0% |
| 0c4 6e | 3.7% | 913 | 4 | 12.3% | 77.7% | 10.1% | 0% | 0% |
| 0c4 8e | 1.9% | 466 | 4 | 5.2% | 94.8% | 0% | 0% | 0% |
| 4c3 0e | 17.1% | 4,283 | 3 | 21.8% | 48.5% | 25.9% | 3.8% | 0% |
| 4c3 2e | 12.0% | 2,992 | 3 | 25.5% | 39.2% | 27.4% | 8.0% | 0% |
| 4c3 4e | 11.8% | 2,954 | 3 | 28.9% | 37.5% | 26.6% | 7.0% | 0% |
| 4c4 0e | 1.3% | 317 | 4 | 13.9% | 72.6% | 13.6% | 0% | 0% |
| 4c4 2e | 1.6% | 397 | 4 | 22.7% | 63.7% | 13.6% | 0% | 0% |
| 4c4 4e | 1.9% | 474 | 4 | 20.7% | 66.5% | 12.9% | 0% | 0% |
| 4b2 0e | 28.5% | 7,113 | 2 | 52.6% | 18.7% | 17.2% | 9.3% | 2.3% |
| 4b2 2e | 39.3% | 9,831 | 2 | 48.1% | 7.8% | 12.5% | 13.5% | 18.1% |
| 4b2 4e | 34.4% | 8,610 | 2 | 63.6% | 7.9% | 11.4% | 9.5% | 7.6% |
| 4b5 0e | 1.9% | 474 | 5 | 0% | 83.1% | 16.9% | 0% | 0% |
| 4b5 2e | 2.0% | 508 | 5 | 0% | 82.5% | 17.5% | 0% | 0% |
| 4b5 4e | 1.8% | 440 | 5 | 0% | 90.2% | 9.8% | 0% | 0% |

Edge counts pooled:

| Corner subset | Share of its DRs that short | DRs in the sample | Quarter turns in such a finish | No optimal without extra quarter turns | 0 half turns | 1 half turn | 2 half turns | 3 or more |
|---|---|---|---|---|---|---|---|---|
| 0c0 | 53.7% | 74,422 | 0 or 2 | 39.4% | 18.4% | 21.2% | 12.7% | 8.3% |
| 2c5 | 2.4% | 2,458 | 5 | 0% | 85.0% | 15.0% | 0% | 0% |
| 2c4 | 9.4% | 13,064 | 4 | 3.1% | 64.2% | 26.7% | 6.0% | 0% |
| 0c3 | 2.6% | 4,991 | 3 | 0.8% | 77.2% | 22.0% | 0% | 0% |
| 4a2 | 18.4% | 10,686 | 2 | 35.7% | 18.2% | 24.0% | 17.1% | 5.0% |
| 4a1 | 47.6% | 30,020 | 1 or 3 | 42.9% | 18.0% | 13.7% | 9.3% | 15.9% |
| 2c3 | 27.7% | 26,823 | 3 | 16.0% | 35.7% | 28.6% | 14.8% | 4.9% |
| 0c4 | 6.9% | 9,885 | 4 | 9.5% | 75.3% | 15.2% | 0% | 0% |
| 4c3 | 12.0% | 10,229 | 3 | 27.1% | 38.7% | 26.9% | 7.3% | 0% |
| 4c4 | 1.7% | 1,188 | 4 | 21.4% | 65.4% | 13.2% | 0% | 0% |
| 4b2 | 36.5% | 25,554 | 2 | 55.7% | 8.1% | 12.1% | 11.5% | 12.7% |
| 4b5 | 1.9% | 1,422 | 5 | 0% | 86.2% | 13.8% | 0% | 0% |
| all DRs | 14.7% | 210,742 | 0 to 5 | 29.6% | 31.8% | 21.2% | 10.7% | 6.8% |

All DRs:

| Subset × edges | Quarter turns in such a finish | No optimal without extra quarter turns | 0 half turns | 1 half turn | 2 half turns | 3 or more |
|---|---|---|---|---|---|---|
| 0c0 0e | 0 or 2 | 8.8% | 22.9% | 13.8% | 7.5% | 47.0% |
| 0c0 2e | 2 | 29.9% | 22.6% | 26.9% | 14.9% | 5.7% |
| 0c0 4e | 2 | 39.5% | 14.0% | 21.0% | 13.9% | 11.6% |
| 0c0 6e | 2 | 55.1% | 17.5% | 17.9% | 8.0% | 1.6% |
| 0c0 8e | 2 | 22.1% | 37.0% | 25.0% | 11.8% | 4.2% |
| 2c5 0e | 5 | 4.5% | 82.6% | 12.2% | 0.6% | 0% |
| 2c5 2e | 5 | 3.6% | 77.9% | 16.5% | 2.0% | <0.1% |
| 2c5 4e | 5 | 2.9% | 77.3% | 16.7% | 3.0% | 0.1% |
| 2c5 6e | 5 | 3.2% | 78.1% | 16.4% | 2.3% | 0.1% |
| 2c5 8e | 5 | 3.5% | 81.7% | 13.3% | 1.5% | 0% |
| 2c4 0e | 4 | 3.8% | 49.1% | 35.0% | 10.6% | 1.5% |
| 2c4 2e | 4 | 5.1% | 51.5% | 33.7% | 8.3% | 1.4% |
| 2c4 4e | 4 | 6.2% | 50.4% | 33.4% | 8.2% | 1.7% |
| 2c4 6e | 4 | 5.7% | 54.0% | 33.8% | 5.9% | 0.5% |
| 2c4 8e | 4 | 4.8% | 58.9% | 32.5% | 3.7% | 0.1% |
| 0c3 0e | 3 | 14.4% | 45.2% | 38.1% | 2.2% | 0% |
| 0c3 2e | 3 | 16.9% | 34.0% | 42.1% | 6.6% | 0.4% |
| 0c3 4e | 3 | 31.6% | 30.0% | 33.4% | 5.0% | 0.1% |
| 0c3 6e | 3 | 15.2% | 34.3% | 43.2% | 7.0% | 0.4% |
| 0c3 8e | 3 | 12.7% | 46.9% | 38.8% | 1.7% | 0% |
| 4a2 0e | 2 | 96.0% | 1.8% | 1.8% | 0.3% | 0% |
| 4a2 2e | 2 | 65.8% | 6.4% | 12.8% | 11.6% | 3.4% |
| 4a2 4e | 2 | 32.1% | 8.5% | 17.0% | 22.3% | 20.0% |
| 4a1 0e | 3 | 48.1% | 29.5% | 16.1% | 5.4% | 0.9% |
| 4a1 2e | 3 | 13.5% | 43.0% | 28.0% | 12.0% | 3.4% |
| 4a1 4e | 1 | 66.0% | 0.6% | 1.8% | 4.0% | 27.6% |
| 2c3 0e | 3 | 53.1% | 27.1% | 16.6% | 3.1% | 0.1% |
| 2c3 2e | 3 | 10.2% | 33.2% | 32.1% | 17.1% | 7.4% |
| 2c3 4e | 3 | 16.8% | 31.7% | 29.5% | 14.6% | 7.3% |
| 2c3 6e | 3 | 21.9% | 34.4% | 30.7% | 11.3% | 1.7% |
| 2c3 8e | 3 | 52.8% | 25.4% | 17.3% | 4.5% | 0.1% |
| 0c4 0e | 4 | 5.6% | 75.4% | 17.2% | 1.8% | <0.1% |
| 0c4 2e | 4 | 8.0% | 72.1% | 18.2% | 1.7% | 0% |
| 0c4 4e | 4 | 9.9% | 69.9% | 17.8% | 2.4% | <0.1% |
| 0c4 6e | 4 | 12.9% | 71.6% | 14.5% | 1.0% | 0% |
| 0c4 8e | 4 | 6.9% | 81.2% | 11.8% | 0.1% | 0% |
| 4c3 0e | 3 | 23.5% | 35.7% | 31.8% | 8.4% | 0.6% |
| 4c3 2e | 3 | 25.4% | 26.6% | 30.5% | 14.6% | 2.9% |
| 4c3 4e | 3 | 29.3% | 26.3% | 28.3% | 13.1% | 3.0% |
| 4c4 0e | 4 | 32.3% | 36.4% | 25.0% | 6.2% | 0.1% |
| 4c4 2e | 4 | 27.9% | 38.3% | 28.5% | 5.0% | 0.3% |
| 4c4 4e | 4 | 26.2% | 39.0% | 29.2% | 5.4% | 0.2% |
| 4b2 0e | 2 | 55.0% | 13.6% | 15.5% | 10.9% | 5.1% |
| 4b2 2e | 2 | 45.2% | 5.7% | 10.9% | 13.7% | 24.4% |
| 4b2 4e | 2 | 63.7% | 5.2% | 9.2% | 9.9% | 11.9% |
| 4b5 0e | 5 | 1.9% | 82.0% | 14.1% | 2.0% | <0.1% |
| 4b5 2e | 5 | 2.0% | 80.8% | 14.9% | 2.3% | <0.1% |
| 4b5 4e | 5 | 1.9% | 82.9% | 14.0% | 1.2% | <0.1% |

Edge counts pooled:

| Corner subset | Quarter turns in such a finish | No optimal without extra quarter turns | 0 half turns | 1 half turn | 2 half turns | 3 or more |
|---|---|---|---|---|---|---|
| 0c0 | 0 or 2 | 40.2% | 17.2% | 21.6% | 12.7% | 8.4% |
| 2c5 | 5 | 3.2% | 77.8% | 16.4% | 2.5% | 0.1% |
| 2c4 | 4 | 5.8% | 51.6% | 33.6% | 7.7% | 1.3% |
| 0c3 | 3 | 24.0% | 32.4% | 37.7% | 5.7% | 0.2% |
| 4a2 | 2 | 49.4% | 7.3% | 14.7% | 16.8% | 11.8% |
| 4a1 | 1 or 3 | 41.5% | 20.8% | 14.2% | 7.7% | 15.8% |
| 2c3 | 3 | 17.5% | 32.5% | 30.0% | 14.1% | 5.8% |
| 0c4 | 4 | 10.0% | 71.1% | 17.0% | 1.9% | <0.1% |
| 4c3 | 3 | 27.4% | 26.7% | 29.4% | 13.7% | 2.9% |
| 4c4 | 4 | 27.1% | 38.6% | 28.7% | 5.2% | 0.3% |
| 4b2 | 2 | 55.0% | 5.7% | 10.2% | 11.7% | 17.4% |
| 4b5 | 5 | 1.9% | 81.9% | 14.4% | 1.8% | <0.1% |
| all DRs | 0 to 5 | 20.2% | 42.2% | 24.6% | 8.7% | 4.4% |

On 4a1 4e a finish with no extra quarter turn has one quarter turn, so it's half turns, the quarter turn, half turns, and it almost never starts within two half turns of either end. On 0c0 0e the HTR states solved by half turns alone have a finish with no quarter turn at all, and count as 3 or more as before.

## What you can see that predicts it

Before you solve anything you can read the corner case on normal and on inverse, where the bad edges sit, the pairs and the E slice. Measured against the tables above: the corner case tells you a lot about needing **one** half turn first, the bad-corner layout gives one usable rule for **two or more** (on 4a2), the pairs and the E slice tell you nothing, and where the bad edges sit next to nothing. Jay suggested the split in 2023 ([3 Nov 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1169972245620342794)): "4qt 2cxe could be divided into a bunch of mini cases ranging from needing 0 half turns on both sides of the scramble to make ideal qt progress, all the way to needing 2 half turns before you can do that ideal qt".

Below, *needs 1+* means that on both sides every optimal finish has at least one half turn before its first quarter turn, and *needs 2+* at least two. DRs with an optimal of 13 or less come first, all DRs after. The corner case names (2c4-3 and so on) and the column *A qt takes it straight to* are those of [*Judging a DR by hand*](../judging-a-dr/), appendix E.

**How far to look, whatever you see.** With an optimal of 13 or less, starting the first quarter turn after 0 or 1 half turns finds an optimal on 87.4% of DRs if you get the side right, and 0 to 2 half turns on 96.2%. Noah Swor's rule ([2 Oct 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1158302491075690507): "also idk if this is a good rule but I only usually write at most 2 moves before the first quarter turn") loses the optimal on the other 3.8%; that's 13.8% of 4a1 4e, 11.4% of 4b2 2e and 10.0% of 4a2 4e, and at most 1.0% on every row of 2c5, 2c4, 0c3, 0c4, 4c3, 4c4 and 4b5.

### A ready side

Call a side **ready** when some U or D quarter turn, done right away, takes the corners to a subset with one quarter turn less: 2c4 to 2c3 or 4b3, 2c3 to 4b2, 4a2 to 4a1, 4a1 to 0c0. You see it by recognising the corner case on that side; the table [per corner case](#every-corner-case-one-side-at-a-time) says which cases are ready. On 2c4 the bad-corner layout alone doesn't tell you, because each of its three layouts has a ready case and one that needs a setup. 2c5, 0c4 and 4b5 are always ready and 0c0 has nothing to lower, so the read exists on eight corner subsets.

**Rule 1: if neither side is ready, expect a half turn before the first quarter turn.** DRs with an optimal of 13 or less, edge counts pooled. Each row is a corner subset. *Neither side ready* is the share of those DRs with the sign; the other cells are the shares needing 1+ and 2+, with the sign and without it:

| Corner subset | Neither side ready | Needs 1+, neither side ready | Needs 1+, a side ready | Needs 2+, neither side ready | Needs 2+, a side ready |
|---|---|---|---|---|---|
| 2c4 | 12.5% | 88.6% | 27.7% | 17.9% | 6.5% |
| 0c3 | 30.3% | 98.7% | 7.4% | 5.2% | 1.1% |
| 4a2 | 57.4% | 74.9% | 16.9% | 29.9% | 10.9% |
| 4a1 | 69.0% | 48.5% | 28.4% | 20.1% | 13.1% |
| 2c3 | 19.7% | 79.2% | 33.6% | 26.0% | 12.9% |
| 4c3 | 34.8% | 70.9% | 22.9% | 15.5% | 6.9% |
| 4c4 | 31.2% | 58.9% | 5.2% | 4.3% | 0.6% |
| 4b2 | 67.6% | 48.0% | 27.9% | 19.2% | 13.5% |

On 2c4, 0c3, 4a2, 2c3, 4c3 and 4c4 the sign separates well for 1+: 59% to 99% with it against 5% to 34% without. On 4a1 and 4b2 it's weak (48.5% against 28.4%, 48.0% against 27.9%): every optimal finish takes extra quarter turns on 82.5% of 4a1 and 55.0% of 4b2 ([*Which HTR routes to try from a DR*](../htr-routes/), section 7), so the finish often doesn't start where the corners say. For 2+ the sign is worth much less: 17.9% against 6.5% on 2c4.

2c4 2e. Each row is a group of its DRs:

| 2c4 2e | Neither side ready | Needs 1+, neither side ready | Needs 1+, a side ready | Needs 2+, neither side ready | Needs 2+, a side ready |
|---|---|---|---|---|---|
| optimal ≤ 13 (10,885 sampled) | 13.6% | 88.0% | 29.2% | 18.2% | 7.5% |
| optimal ≤ 12 (2,814 sampled) | 10.0% | 91.5% | 27.8% | 13.9% | 5.6% |
| all DRs (25,000 sampled) | 24.5% | 68.2% | 23.7% | 12.4% | 6.1% |

So on a 2c4 2e with an optimal of 13 or less: if neither side is ready, expect to need a half turn first, 88.0% against 29.2%.

The same on all DRs, where the sign is duller. It's a read about the DRs you'd keep:

| Corner subset | Neither side ready | Needs 1+, neither side ready | Needs 1+, a side ready | Needs 2+, neither side ready | Needs 2+, a side ready |
|---|---|---|---|---|---|
| 2c4 | 24.9% | 67.2% | 22.6% | 11.4% | 5.6% |
| 0c3 | 44.1% | 67.7% | 10.3% | 5.6% | 3.3% |
| 4a2 | 69.2% | 55.9% | 13.3% | 22.0% | 8.6% |
| 4a1 | 69.7% | 44.2% | 26.5% | 18.0% | 12.0% |
| 2c3 | 25.1% | 65.5% | 28.2% | 18.2% | 10.6% |
| 4c3 | 44.2% | 52.8% | 20.6% | 12.0% | 6.7% |
| 4c4 | 44.5% | 36.5% | 8.0% | 3.7% | 1.1% |
| 4b2 | 69.4% | 41.4% | 25.2% | 16.0% | 12.1% |

A 2c4 2e where neither side is ready, replayed. Both optimal finishes need half turns first on both sides:

```
L2 U' F2 U B2 D' B2 L2 D' R2 U2 R2 F2 // 2c4 2e, 13 optimal; corners 2c4-7 on normal, 2c4-4 on inverse
F2 R2 U2 R2 D L2 B2 D B2 U' F2 U L2 // optimal finish: 4 half turns before the first qt on normal, 1 on inverse
F2 R2 D2 L2 U F2 L2 U B2 D' L2 D L2 // the other optimal finish: 4 half turns before the first qt on normal, 1 on inverse
```

And one that's ready on normal only: there any U or D quarter turn takes the corners from 2c4 to 2c3, and both optimal finishes start with one.

```
F2 L2 D' F2 R2 U' F2 D F2 L2 D2 L2 U // 2c4 2e, 13 optimal; corners 2c4-3 on normal, 2c4-7 on inverse
U' L2 D2 L2 F2 D' F2 U R2 F2 D L2 F2 // optimal finish: 0 half turns before the first qt on normal, 2 on inverse
D' B2 D2 B2 L2 D' L2 D R2 F2 D L2 F2 // the other optimal finish: 0 half turns before the first qt on normal, 2 on inverse
```

### Rule 1 when the quarter turn has to make progress

Count only the optimal finishes with no extra quarter turn ([above](#when-the-first-quarter-turn-has-to-make-progress)), on the rows where that means the corners' count. Then rule 1 is exact one way: if neither side is ready, no such finish starts with a quarter turn, on any DR. That's what solvers call 4b2 parity: with it a quarter turn at once makes no progress. More generally the first quarter turn of such a finish can't come before the half turns the corners need on that side. It's logic, and it holds on every sampled DR.

The other way it stays odds. The 2qt rows and 4a1 4e, DRs with an optimal of 13 or less. Each row is a subset × edges. *Has an optimal with no extra quarter turn* is a share of those DRs, the next cell is how many that is in the sample, and the rest are shares of the DRs that have one: neither side ready; such a finish starting with the quarter turn, without the sign and with a side ready; needing 2+ on such finishes; and the first quarter turn coming exactly as early as the corners allow on the better side:

| Subset × edges | Has an optimal with no extra quarter turn | DRs in the sample that have one | Of those: neither side ready | 0 half turns, neither side ready | 0 half turns, a side ready | Needs 2+, neither side ready | Needs 2+, a side ready | First quarter turn as early as the corners allow |
|---|---|---|---|---|---|---|---|---|
| 4b2 0e | 42.5% | 7,882 | 62.0% | 0% | 88.7% | 46.3% | 7.3% | 78.0% |
| 4b2 2e | 51.4% | 10,856 | 67.8% | 0% | 36.2% | 73.1% | 55.5% | 37.1% |
| 4b2 4e | 33.9% | 6,946 | 66.4% | 0% | 49.1% | 62.6% | 42.3% | 49.4% |
| 4a2 0e | 2.7% | 189 | 16.9% | 0% | 100.0% | 0% | 0% | 100.0% |
| 4a2 2e | 32.7% | 3,240 | 55.0% | 0% | 72.6% | 29.6% | 14.4% | 76.9% |
| 4a2 4e | 68.8% | 10,926 | 66.8% | 0% | 53.4% | 56.7% | 37.4% | 56.9% |
| 4a1 4e | 33.7% | 7,693 | 75.5% | 0% | 7.5% | 93.5% | 88.7% | 10.7% |

So on a 4b2 2e with a 2qt optimal and a ready side, a 2qt optimal starts with that quarter turn on 36.2%, against 69.2% of ready 4b2 2e in the main count, where the 4qt optimals come in. For 2+ the sign is still weak (73.1% against 55.5%). On 4a1 4e being ready hardly helps: the single quarter turn also has to fix all four bad edges.

The corner subsets, edge counts pooled (4a1 is left out because of 4a1 0e and 2e), optimal of 13 or less:

| Corner subset | Has an optimal with no extra quarter turn | DRs in the sample that have one | Of those: neither side ready | 0 half turns, neither side ready | 0 half turns, a side ready | Needs 2+, neither side ready | Needs 2+, a side ready | First quarter turn as early as the corners allow |
|---|---|---|---|---|---|---|---|---|
| 2c4 | 94.2% | 47,196 | 12.1% | 0% | 69.5% | 20.9% | 7.4% | 70.7% |
| 0c3 | 93.5% | 22,981 | 32.1% | 0% | 91.8% | 5.3% | 1.2% | 92.7% |
| 4a2 | 55.1% | 14,355 | 64.3% | 0% | 58.5% | 51.9% | 31.3% | 61.1% |
| 2c3 | 80.8% | 55,399 | 20.0% | 0% | 50.4% | 39.5% | 21.7% | 52.4% |
| 4c3 | 68.5% | 25,693 | 34.6% | 0% | 68.6% | 25.5% | 12.3% | 70.7% |
| 4c4 | 72.0% | 5,578 | 25.0% | 0% | 94.6% | 7.9% | 0.8% | 94.0% |
| 4b2 | 42.3% | 25,684 | 67.1% | 0% | 43.2% | 68.2% | 48.6% | 43.2% |

All DRs:

| Subset × edges | Has an optimal with no extra quarter turn | DRs in the sample that have one | Of those: neither side ready | 0 half turns, neither side ready | 0 half turns, a side ready | Needs 2+, neither side ready | Needs 2+, a side ready | First quarter turn as early as the corners allow |
|---|---|---|---|---|---|---|---|---|
| 4b2 0e | 45.0% | 11,262 | 66.2% | 0% | 89.3% | 50.1% | 6.8% | 76.6% |
| 4b2 2e | 54.8% | 13,689 | 70.2% | 0% | 35.0% | 74.9% | 57.2% | 35.9% |
| 4b2 4e | 36.3% | 9,063 | 68.8% | 0% | 45.9% | 66.6% | 46.1% | 46.0% |
| 4a2 0e | 4.0% | 996 | 53.1% | 0% | 97.9% | 15.1% | 0% | 94.1% |
| 4a2 2e | 34.2% | 8,541 | 72.5% | 0% | 67.8% | 51.8% | 22.7% | 72.8% |
| 4a2 4e | 67.9% | 16,963 | 73.6% | 0% | 47.4% | 69.2% | 43.5% | 50.4% |
| 4a1 4e | 34.0% | 8,502 | 75.4% | 0% | 6.8% | 94.1% | 89.9% | 9.8% |

### One side at a time

The same read per side, which is how you'd use it: look at a side, know its odds. Each row is a corner case on one side of a 2c4 2e with an optimal of 13 or less (a DR gives two sides). The last four cells are the shares of such sides on which the optimal finishes, read from that side, reach their first quarter turn after exactly that many half turns:

| Corner case on that side | Bad corners | A qt takes it straight to | Sides in the sample | 0 half turns | 1 half turn | 2 half turns | 3 or more |
|---|---|---|---|---|---|---|---|
| 2c4-1 | both on one layer, adjacent | 2c3 | 5,098 | 60.7% | 23.5% | 10.0% | 5.7% |
| 2c4-2 | 1 up 1 down, opposite | 4b3 | 2,327 | 31.7% | 49.3% | 14.2% | 4.8% |
| 2c4-3 | both on one layer, adjacent | 2c3 | 4,506 | 74.4% | 0.9% | 11.2% | 13.6% |
| 2c4-4 | both on one layer, adjacent | nothing, needs a setup | 3,129 | 7.8% | 50.6% | 26.2% | 15.3% |
| 2c4-5 | 1 up 1 down, stacked | 4b3 | 1,573 | 50.7% | 1.9% | 24.2% | 23.3% |
| 2c4-6 | 1 up 1 down, opposite | nothing, needs a setup | 2,956 | 4.4% | 56.8% | 18.4% | 20.4% |
| 2c4-7 | 1 up 1 down, stacked | nothing, needs a setup | 2,181 | 8.1% | 26.0% | 27.3% | 38.6% |

A side that needs a setup starts with a quarter turn on 4% to 8% (finishes that go up a quarter turn first). A ready side starts with one on 51% to 74% (2c4-1, 2c4-3, 2c4-5), and on 31.7% for 2c4-2. On 2c4-3 and 2c4-5 it's a quarter turn at once or at least two half turns, almost never exactly one (0.9% and 1.9%).

### Two or more: the 4a2 rule

On 4a2, 4a1 and 4b2 the corners can need up to three half turns before any quarter turn lowers them. On 4a2 the layout gives the count (2-2 with a diagonal over a diagonal: 0; 2-2 with the pairs stacked: 1; 2-2 with the pairs on opposite sides: 2; 4-0: 3). Take the side that needs fewer.

4a2 4e with an optimal of 13 or less. Each row is that count; the last four cells are the shares of those DRs needing exactly that many half turns before the first quarter turn on the better side:

| Half turns the corners need, smaller side | Bad corners on that side | DRs in the sample | Share of those DRs | 0 half turns | 1 half turn | 2 half turns | 3 or more |
|---|---|---|---|---|---|---|---|
| 0 | 2-2, diagonal over diagonal | 6,067 | 38.2% | 76.5% | 6.8% | 9.0% | 7.7% |
| 1 | 2-2, pairs stacked | 7,612 | 47.9% | 19.0% | 54.5% | 22.4% | 4.2% |
| 2 | 2-2, pairs on opposite sides | 2,020 | 12.7% | 20.4% | 2.8% | 44.7% | 32.1% |
| 3 | 4-0 | 180 | 1.1% | 0.6% | 11.7% | 0% | 87.8% |

**Rule 2: on 4a2 4e, if on both sides the bad corners are 4-0 or 2-2 with the pairs on opposite sides, expect two or more half turns first: 77.7% against 22.2%.** That's with an optimal of 13 or less, where 13.9% have the sign (2,200 DRs in the sample). With 12 or less it's 86.3% against 23.3% (496 DRs with the sign), and on all 4a2 4e 54.7% against 18.4%, with the sign on 24.9%.

The same sign, the corners needing 2 or 3 half turns on both sides, on every row where it exists. Optimal of 13 or less:

| Subset × edges | Corners need 2 or 3 half turns on both sides | DRs in the sample with that | Needs 2+, with that | Needs 2+, without | Needs 3+, with that | Needs 3+, without |
|---|---|---|---|---|---|---|
| 4a2 4e | 13.9% | 2,200 | 77.7% | 22.2% | 36.7% | 5.8% |
| 4a2 2e | 6.1% | 600 | 38.7% | 6.1% | 0% | 0% |
| 4a2 0e | 6.6% | 468 | 6.4% | 2.2% | 0% | 0% |
| 4b2 0e | 21.2% | 3,942 | 23.4% | 5.7% | 7.9% | 0.4% |
| 4a1 4e | 24.1% | 5,489 | 32.8% | 20.3% | 21.1% | 11.5% |
| 4b2 2e | 22.7% | 4,796 | 31.9% | 19.2% | 20.3% | 8.8% |
| 4a1 2e | 22.8% | 5,004 | 20.7% | 9.9% | 5.4% | 1.8% |
| 4b2 4e | 23.2% | 4,753 | 20.6% | 11.2% | 9.1% | 3.2% |
| 4a1 0e | 19.8% | 3,486 | 8.3% | 2.2% | 1.1% | 0.1% |

It carries over to 4a2 2e and 4b2 0e. On the other rows it's a slope, not a rule. For 4a1 the count is 4-0: 0; 2-2 with the pairs on opposite sides: 1; 2-2 with the pairs stacked: 2; 2-2 with a diagonal over a diagonal: 3. On 4b2 the layout isn't enough (3-1 is 1 or 2, pairs sharing one column 0 or 3), so there it takes the corner case.

All DRs:

| Subset × edges | Corners need 2 or 3 half turns on both sides | DRs in the sample with that | Needs 2+, with that | Needs 2+, without | Needs 3+, with that | Needs 3+, without |
|---|---|---|---|---|---|---|
| 4a2 4e | 24.9% | 6,227 | 54.7% | 18.4% | 28.4% | 5.1% |
| 4a2 2e | 24.8% | 6,210 | 19.4% | 4.4% | 4.4% | 0.1% |
| 4a2 0e | 24.4% | 6,096 | 4.8% | 1.5% | 0.1% | 0% |
| 4b2 0e | 25.2% | 6,308 | 16.2% | 4.7% | 5.4% | 0.3% |
| 4a1 4e | 25.0% | 6,249 | 29.3% | 18.9% | 18.7% | 10.7% |
| 4b2 2e | 25.0% | 6,248 | 25.5% | 17.0% | 16.1% | 7.8% |
| 4a1 2e | 24.7% | 6,174 | 17.0% | 9.0% | 4.5% | 1.6% |
| 4b2 4e | 25.4% | 6,356 | 16.2% | 9.7% | 7.1% | 2.8% |
| 4a1 0e | 24.8% | 6,201 | 6.9% | 1.8% | 1.0% | 0.1% |

A 4a2 4e with the pairs on opposite sides on both sides, replayed:

```
R2 D2 F2 L2 U F2 U2 L2 D B2 D2 // 4a2 4e, 11 optimal; corners 4a2-3 on normal, 4a2-3 on inverse
D2 B2 D' L2 U2 F2 U' L2 F2 D2 R2 // optimal finish: 2 half turns before the first qt on normal, 4 on inverse
D2 B2 D' L2 D2 B2 U' R2 B2 U2 R2 // the other optimal finish: 2 half turns before the first qt on normal, 4 on inverse
```

And one with 4-0 on both sides:

```
R2 D2 B2 U' L2 D2 L2 F2 U' B2 U2 F2 L2 // 4a2 4e, 13 optimal; corners 4a2-4 on normal, 4a2-4 on inverse
L2 F2 U2 B2 U F2 L2 D2 L2 U B2 D2 R2 // optimal finish: 4 half turns before the first qt on normal, 3 on inverse
F2 D2 L2 U' L2 B2 U2 L2 F2 D B2 D2 L2 // the other optimal finish: 3 half turns before the first qt on normal, 3 on inverse
```

### Two or more on 2c4 2e: nothing you can see

8.9% of 2c4 2e with an optimal of 13 or less need 2+. What moves that number:

- A ready side or not (rule 1): 18.2% against 7.5%.
- The two bad corners stacked, one above the other, on both sides: 38.2% against 8.4%, but only 1.9% of them look like that (204 DRs in the sample). Stacked on at least one side (32.6%): 14.7% against 6.1%.
- The exact pair of corner cases (28 pairs): from 1.8% (2c4-1 and 2c4-2, 509 DRs) to 42.3% (2c4-5 and 2c4-7, 104 DRs). Picking the worst and the best pair on half the sample and reading them on the other half gives 28.7% (2c4-4 and 2c4-7, 174 DRs) and 4.2% (2c4-1 on both sides, 262 DRs).
- True pairs, slice pairs, the E slice: nothing measurable. Where the bad edges sit: next to nothing (second table below).

So the best a read does on 2c4 2e is single out one DR in fifty where the odds of 2+ are about two in five, and leave the rest near the base rate.

*Computer only*, to put a number on it: the share of the uncertainty about *needs 2+* that each read removes (mutual information as a share of the entropy, with the chance level of a read with that many values taken off), DRs with an optimal of 13 or less. Each column is a subset × edges:

| Read | 2c4 2e | 2c3 2e | 4a2 4e | 4a1 4e | 4b2 2e |
|---|---|---|---|---|---|
| a side ready or not | 2.3% | 1.8% | 4.4% | 0.7% | 0.5% |
| bad-corner layout on both sides | 4.2% | 3.3% | 15.9% | 2.0% | <0.1% |
| corner case on both sides | 7.6% | 3.3% | 15.9% | 2.0% | 2.1% |
| corner cases and both HTR lengths (needs the HTRs) | 8.9% | 4.2% | 21.8% | 11.5% | 5.9% |
| both HTR lengths (needs the HTRs) | 2.9% | 1.9% | 8.4% | 8.2% | 3.9% |
| true pairs on both sides | <0.1% | 0.1% | 0.2% | 0.2% | 0.2% |
| slice pairs on both sides | 0% | <0.1% | <0.1% | <0.1% | <0.1% |
| E-slice edges solved | 0% | 0% | 0.1% | 0% | 0.1% |
| E-slice parity | <0.1% | 0% | 0.2% | 0% | 0.2% |
| optimal length (not a read) | 0.9% | 0.5% | 0.7% | 4.7% | 1.5% |
| number of optimal finishes (not a read) | 4.2% | 8.2% | 4.0% | 6.0% | 6.4% |

Only 4a2 4e gets anywhere, through rule 2. The bad edges, *computer only* again: the same share for one side at a time (does this side need 2+), knowing its corner case, and knowing on top of that where every bad edge sits:

| Known about one side | 2c4 2e | 2c3 2e | 4a2 4e | 4a1 4e | 4b2 2e |
|---|---|---|---|---|---|
| its corner case | 8.8% | 4.1% | 14.6% | 1.8% | 2.3% |
| its corner case and where every bad edge sits | 10.8% | 5.4% | 19.4% | 5.6% | 5.4% |

That's 1 to 5 points more, most on 4a2 4e and 4a1 4e, and it would take a table of hundreds of layouts to use. The last row of the first table shows why so little is visible: what decides it is mostly how many optimal finishes the DR has, and that can't be seen. *Computer only*, the share needing 2+ by the number of optimal finishes:

| Optimal finishes of the DR | 2c4 2e, optimal ≤ 13: share of those DRs | 2c4 2e, optimal ≤ 13: needs 2+ | 2c4 2e, all: needs 2+ | Every subset, optimal ≤ 13: needs 2+ | Every subset, all DRs: needs 2+ |
|---|---|---|---|---|---|
| 1 | 24.2% | 13.3% | 16.7% | 17.4% | 16.4% |
| 2 or 3 | 33.3% | 11.7% | 14.1% | 16.1% | 14.3% |
| 4 to 7 | 24.2% | 5.8% | 7.1% | 11.9% | 9.0% |
| 8 to 15 | 12.7% | 2.8% | 2.8% | 7.1% | 4.2% |
| 16 or more | 5.6% | 1.2% | 0.6% | 3.5% | 1.0% |

A 2c4 2e that's ready on both sides and still needs two half turns first on both, replayed. Its two optimal finishes differ only in the order of the first two moves:

```
R2 F2 D' B2 D2 R2 U' R2 D' L2 U B2 F2 // 2c4 2e, 13 optimal; corners 2c4-5 on normal, 2c4-1 on inverse
F2 B2 U' L2 D R2 U R2 D2 B2 D F2 R2 // optimal finish: 2 half turns before the first qt on normal, 2 on inverse
B2 F2 U' L2 D R2 U R2 D2 B2 D F2 R2 // the other optimal finish: 2 half turns before the first qt on normal, 2 on inverse
```

### If you already have the HTRs

Not a read of a few seconds, but you find these anyway. Each row is a subset × edges and the length of the shorter of its two shortest HTRs (normal, inverse), among DRs with an optimal of 13 or less:

| Subset × edges | Shorter of the two HTRs, moves | DRs in the sample | Share of those DRs | Needs 1+ | Needs 2+ |
|---|---|---|---|---|---|
| 4b2 2e | 3 | 517 | 2.4% | 5.6% | 1.4% |
| 4b2 2e | 4 | 1,971 | 9.3% | 52.4% | 3.9% |
| 4b2 2e | 5 | 6,194 | 29.3% | 43.7% | 26.2% |
| 4b2 2e | 6 | 9,920 | 47.0% | 46.3% | 24.0% |
| 4b2 2e | 7 | 2,493 | 11.8% | 46.6% | 22.8% |
| 4a1 4e | 1 | 224 | 1.0% | 2.2% | 1.8% |
| 4a1 4e | 2 | 887 | 3.9% | 72.6% | 7.0% |
| 4a1 4e | 3 | 2,137 | 9.4% | 60.7% | 42.9% |
| 4a1 4e | 4 | 4,003 | 17.5% | 51.6% | 35.7% |
| 4a1 4e | 5 | 5,498 | 24.1% | 48.9% | 26.0% |
| 4a1 4e | 6 | 6,271 | 27.5% | 42.0% | 17.2% |
| 4a1 4e | 7 | 3,716 | 16.3% | 35.6% | 10.6% |
| 2c4 2e | 7 | 1,514 | 13.9% | 15.4% | 5.0% |
| 2c4 2e | 8 | 6,600 | 60.6% | 33.5% | 7.2% |
| 2c4 2e | 9 | 2,697 | 24.8% | 58.2% | 14.9% |

A 4b2 2e with a 3- or 4-move HTR on a side almost never needs 2+: 3.3% against 24.6% (11.8% of them have one). On 4a1 4e it's the other way round: with a 3- or 4-move HTR 38.2% need 2+, against 18.7% from 5 moves up and 5.9% with 1 or 2. On 2c4 2e a 9-move shorter HTR means 15.2% against 6.8%.

### Every corner case, one side at a time

Each row is a corner case on one side, edge counts pooled, DRs with an optimal of 13 or less. The last four cells are the shares of such sides on which the optimal finishes, read from that side, reach their first quarter turn after exactly that many half turns. A case with an entry under *A qt takes it straight to* is ready.

| Corner case on that side | Bad corners | A qt takes it straight to | Share of the sides of its subset | Sides in the sample | 0 half turns | 1 half turn | 2 half turns | 3 or more |
|---|---|---|---|---|---|---|---|---|
| 2c5-1 | both on one layer, adjacent | 2c4 | 66.9% | 21,734 | 68.1% | 18.9% | 9.1% | 3.9% |
| 2c5-2 | 1 up 1 down, opposite | 4b4 | 22.3% | 6,934 | 15.5% | 66.1% | 13.2% | 5.2% |
| 2c5-3 | 1 up 1 down, stacked | 4b4 | 10.8% | 3,388 | 34.7% | 12.9% | 28.6% | 23.8% |
| 2c4-1 | both on one layer, adjacent | 2c3 | 24.4% | 23,939 | 60.1% | 24.6% | 9.4% | 5.8% |
| 2c4-2 | 1 up 1 down, opposite | 4b3 | 10.9% | 10,474 | 32.4% | 49.2% | 13.2% | 5.1% |
| 2c4-3 | both on one layer, adjacent | 2c3 | 20.6% | 20,666 | 76.3% | 0.8% | 10.8% | 12.1% |
| 2c4-4 | both on one layer, adjacent | nothing, needs a setup | 14.0% | 14,388 | 7.2% | 52.8% | 25.1% | 14.9% |
| 2c4-5 | 1 up 1 down, stacked | 4b3 | 7.1% | 6,758 | 53.9% | 1.3% | 23.8% | 21.0% |
| 2c4-6 | 1 up 1 down, opposite | nothing, needs a setup | 13.0% | 13,256 | 4.4% | 56.4% | 20.1% | 19.2% |
| 2c4-7 | 1 up 1 down, stacked | nothing, needs a setup | 9.9% | 9,733 | 6.8% | 29.6% | 26.6% | 37.0% |
| 0c3-1 | none bad | 4a2 | 44.4% | 20,483 | 86.0% | <0.1% | 5.0% | 9.0% |
| 0c3-2 | none bad | nothing, needs a setup | 55.6% | 27,143 | 2.0% | 62.7% | 29.8% | 5.5% |
| 4a2-1 | 2-2, diagonal over diagonal | 4a1 | 23.7% | 16,280 | 78.3% | 2.3% | 6.2% | 13.2% |
| 4a2-2 | 2-2, pairs stacked | nothing, needs a setup | 38.8% | 25,809 | 14.0% | 55.5% | 18.8% | 11.7% |
| 4a2-3 | 2-2, pairs on opposite sides | nothing, needs a setup | 26.7% | 17,143 | 26.8% | 6.4% | 28.1% | 38.7% |
| 4a2-4 | 4-0 | nothing, needs a setup | 10.9% | 6,564 | 2.5% | 20.5% | 5.0% | 72.0% |
| 4a1-1 | 4-0 | 0c0 | 16.9% | 21,602 | 59.1% | 14.3% | 10.3% | 16.4% |
| 4a1-2 | 2-2, pairs on opposite sides | nothing, needs a setup | 34.2% | 42,808 | 34.3% | 34.9% | 14.1% | 16.7% |
| 4a1-3 | 2-2, pairs stacked | nothing, needs a setup | 32.7% | 40,877 | 39.4% | 17.3% | 15.7% | 27.6% |
| 4a1-4 | 2-2, diagonal over diagonal | nothing, needs a setup | 16.2% | 19,371 | 18.2% | 31.8% | 14.2% | 35.9% |
| 2c3-1 | 1 up 1 down, stacked | 4b2 | 28.6% | 46,964 | 48.5% | 30.1% | 11.8% | 9.6% |
| 2c3-2 | 1 up 1 down, opposite | 4b2 | 25.9% | 41,713 | 60.4% | 3.9% | 13.8% | 21.8% |
| 2c3-3 | both on one layer, adjacent | nothing, needs a setup | 45.5% | 69,907 | 15.1% | 36.8% | 19.0% | 29.2% |
| 0c4-1 | none bad | 4a3 | 100.0% | 90,864 | 51.3% | 28.9% | 13.9% | 5.8% |
| 4c3-1 | 2-2, pairs on opposite sides | 4b2 | 12.4% | 8,868 | 63.3% | 20.9% | 9.0% | 6.8% |
| 4c3-2 | 2-2, pairs stacked | 4b2 | 10.6% | 7,705 | 77.3% | 0.1% | 10.7% | 11.9% |
| 4c3-3 | 4-0 | nothing, needs a setup | 5.4% | 3,849 | 10.8% | 66.9% | 16.4% | 5.8% |
| 4c3-4 | 2-2, pairs sharing one column | 4a2 | 17.3% | 12,711 | 59.0% | 12.7% | 9.4% | 18.9% |
| 4c3-5 | 3-1 | nothing, needs a setup | 32.7% | 23,599 | 28.1% | 36.4% | 21.9% | 13.5% |
| 4c3-6 | 2-2, diagonal over diagonal | nothing, needs a setup | 7.9% | 5,636 | 2.3% | 53.8% | 29.2% | 14.7% |
| 4c3-7 | 2-2, pairs stacked | nothing, needs a setup | 7.3% | 5,334 | 1.0% | 60.8% | 18.4% | 19.8% |
| 4c3-8 | 4-0 | nothing, needs a setup | 2.6% | 1,922 | 25.9% | 0.4% | 37.7% | 36.0% |
| 4c3-9 | 2-2, pairs on opposite sides | nothing, needs a setup | 3.9% | 2,996 | 4.1% | 9.4% | 28.8% | 57.7% |
| 4c4-1 | 2-2, diagonal over diagonal | 4a3 | 17.8% | 2,858 | 87.5% | 3.0% | 4.7% | 4.8% |
| 4c4-2 | 2-2, pairs sharing one column | 4a3 | 22.0% | 3,369 | 84.7% | 4.6% | 4.5% | 6.2% |
| 4c4-3 | 2-2, pairs stacked | nothing, needs a setup | 19.5% | 3,042 | 17.8% | 61.7% | 17.9% | 2.6% |
| 4c4-4 | 3-1 | nothing, needs a setup | 28.0% | 4,369 | 23.4% | 51.0% | 20.6% | 4.9% |
| 4c4-5 | 2-2, pairs on opposite sides | nothing, needs a setup | 8.8% | 1,301 | 41.9% | 22.8% | 25.2% | 10.0% |
| 4c4-6 | 4-0 | 0c3 | 3.9% | 537 | 67.7% | 15.5% | 4.5% | 12.3% |
| 4b2-1 | 2-2, pairs sharing one column | 4a1 | 17.7% | 21,622 | 59.8% | 13.4% | 10.4% | 16.4% |
| 4b2-2 | 3-1 | nothing, needs a setup | 34.1% | 40,992 | 33.1% | 36.9% | 15.4% | 14.7% |
| 4b2-3 | 3-1 | nothing, needs a setup | 32.4% | 38,895 | 40.2% | 16.3% | 16.8% | 26.7% |
| 4b2-4 | 2-2, pairs sharing one column | nothing, needs a setup | 15.8% | 18,845 | 16.6% | 33.8% | 15.4% | 34.3% |
| 4b5-1 | 3-1 | 2c4 | 73.9% | 14,572 | 66.1% | 19.4% | 8.9% | 5.6% |
| 4b5-2 | 2-2, pairs sharing one column | 4a4 | 26.1% | 5,246 | 19.4% | 54.7% | 19.1% | 6.8% |

All DRs:

| Corner case on that side | Bad corners | A qt takes it straight to | Share of the sides of its subset | Sides in the sample | 0 half turns | 1 half turn | 2 half turns | 3 or more |
|---|---|---|---|---|---|---|---|---|
| 2c5-1 | both on one layer, adjacent | 2c4 | 49.7% | 124,387 | 77.5% | 13.5% | 6.0% | 2.9% |
| 2c5-2 | 1 up 1 down, opposite | 4b4 | 24.9% | 62,373 | 32.3% | 56.0% | 8.0% | 3.8% |
| 2c5-3 | 1 up 1 down, stacked | 4b4 | 25.4% | 63,240 | 57.0% | 18.1% | 14.6% | 10.3% |
| 2c4-1 | both on one layer, adjacent | 2c3 | 16.7% | 41,504 | 68.4% | 20.2% | 7.1% | 4.3% |
| 2c4-2 | 1 up 1 down, opposite | 4b3 | 8.3% | 21,066 | 43.6% | 43.8% | 9.1% | 3.5% |
| 2c4-3 | both on one layer, adjacent | 2c3 | 16.8% | 41,864 | 82.1% | 0.9% | 8.4% | 8.7% |
| 2c4-4 | both on one layer, adjacent | nothing, needs a setup | 16.7% | 41,595 | 18.2% | 54.2% | 17.5% | 10.1% |
| 2c4-5 | 1 up 1 down, stacked | 4b3 | 8.3% | 20,741 | 67.1% | 2.2% | 17.5% | 13.2% |
| 2c4-6 | 1 up 1 down, opposite | nothing, needs a setup | 16.6% | 41,555 | 17.2% | 56.4% | 13.9% | 12.5% |
| 2c4-7 | 1 up 1 down, stacked | nothing, needs a setup | 16.6% | 41,675 | 22.9% | 35.8% | 20.0% | 21.4% |
| 0c3-1 | none bad | 4a2 | 33.6% | 83,860 | 84.3% | 1.4% | 4.2% | 10.0% |
| 0c3-2 | none bad | nothing, needs a setup | 66.4% | 166,140 | 25.1% | 52.0% | 18.2% | 4.7% |
| 4a2-1 | 2-2, diagonal over diagonal | 4a1 | 16.8% | 25,154 | 82.7% | 2.0% | 5.1% | 10.2% |
| 4a2-2 | 2-2, pairs stacked | nothing, needs a setup | 33.1% | 50,000 | 24.7% | 53.3% | 13.8% | 8.1% |
| 4a2-3 | 2-2, pairs on opposite sides | nothing, needs a setup | 33.3% | 49,814 | 44.4% | 9.2% | 22.5% | 23.9% |
| 4a2-4 | 4-0 | nothing, needs a setup | 16.7% | 25,032 | 7.4% | 40.0% | 7.6% | 44.9% |
| 4a1-1 | 4-0 | 0c0 | 16.5% | 24,935 | 61.4% | 14.0% | 9.6% | 15.1% |
| 4a1-2 | 2-2, pairs on opposite sides | nothing, needs a setup | 33.6% | 50,173 | 38.7% | 33.0% | 13.0% | 15.3% |
| 4a1-3 | 2-2, pairs stacked | nothing, needs a setup | 33.1% | 49,805 | 44.4% | 16.7% | 14.3% | 24.7% |
| 4a1-4 | 2-2, diagonal over diagonal | nothing, needs a setup | 16.8% | 25,087 | 21.3% | 34.1% | 13.2% | 31.4% |
| 2c3-1 | 1 up 1 down, stacked | 4b2 | 24.9% | 62,443 | 54.3% | 27.4% | 10.1% | 8.1% |
| 2c3-2 | 1 up 1 down, opposite | 4b2 | 25.0% | 62,597 | 66.8% | 3.7% | 11.8% | 17.6% |
| 2c3-3 | both on one layer, adjacent | nothing, needs a setup | 50.2% | 124,960 | 23.5% | 38.4% | 16.2% | 21.9% |
| 0c4-1 | none bad | 4a3 | 100.0% | 250,000 | 63.4% | 23.0% | 9.3% | 4.3% |
| 4c3-1 | 2-2, pairs on opposite sides | 4b2 | 8.3% | 12,449 | 70.3% | 17.8% | 6.9% | 5.0% |
| 4c3-2 | 2-2, pairs stacked | 4b2 | 8.4% | 12,511 | 82.8% | 0.2% | 8.3% | 8.7% |
| 4c3-3 | 4-0 | nothing, needs a setup | 4.2% | 6,397 | 21.3% | 62.9% | 11.8% | 4.0% |
| 4c3-4 | 2-2, pairs sharing one column | 4a2 | 16.8% | 25,155 | 63.7% | 13.3% | 8.5% | 14.5% |
| 4c3-5 | 3-1 | nothing, needs a setup | 33.2% | 49,845 | 42.5% | 32.0% | 16.0% | 9.5% |
| 4c3-6 | 2-2, diagonal over diagonal | nothing, needs a setup | 8.3% | 12,370 | 8.6% | 59.2% | 21.8% | 10.5% |
| 4c3-7 | 2-2, pairs stacked | nothing, needs a setup | 8.3% | 12,485 | 5.5% | 65.4% | 13.9% | 15.2% |
| 4c3-8 | 4-0 | nothing, needs a setup | 4.2% | 6,258 | 46.6% | 1.3% | 28.4% | 23.8% |
| 4c3-9 | 2-2, pairs on opposite sides | nothing, needs a setup | 8.4% | 12,530 | 13.9% | 22.6% | 24.9% | 38.5% |
| 4c4-1 | 2-2, diagonal over diagonal | 4a3 | 8.4% | 12,653 | 89.6% | 2.8% | 3.4% | 4.2% |
| 4c4-2 | 2-2, pairs sharing one column | 4a3 | 16.6% | 24,780 | 88.2% | 4.3% | 3.1% | 4.4% |
| 4c4-3 | 2-2, pairs stacked | nothing, needs a setup | 16.8% | 24,975 | 40.6% | 46.0% | 11.1% | 2.3% |
| 4c4-4 | 3-1 | nothing, needs a setup | 33.4% | 50,220 | 41.6% | 42.6% | 12.1% | 3.7% |
| 4c4-5 | 2-2, pairs on opposite sides | nothing, needs a setup | 16.6% | 24,997 | 58.2% | 20.9% | 14.1% | 6.8% |
| 4c4-6 | 4-0 | 0c3 | 8.3% | 12,375 | 64.5% | 19.8% | 6.1% | 9.7% |
| 4b2-1 | 2-2, pairs sharing one column | 4a1 | 16.7% | 24,937 | 63.4% | 12.5% | 9.5% | 14.7% |
| 4b2-2 | 3-1 | nothing, needs a setup | 33.1% | 49,603 | 38.9% | 34.7% | 13.6% | 12.8% |
| 4b2-3 | 3-1 | nothing, needs a setup | 33.4% | 50,254 | 47.2% | 16.0% | 14.6% | 22.2% |
| 4b2-4 | 2-2, pairs sharing one column | nothing, needs a setup | 16.8% | 25,206 | 23.7% | 35.0% | 13.5% | 27.8% |
| 4b5-1 | 3-1 | 2c4 | 66.4% | 99,559 | 74.5% | 15.1% | 6.3% | 4.1% |
| 4b5-2 | 2-2, pairs sharing one column | 4a4 | 33.6% | 50,441 | 41.5% | 42.5% | 11.9% | 4.1% |

### Rule 1 on every subset × edges

Optimal of 13 or less. Same columns as the rule 1 table:

| Subset × edges | Neither side ready | Needs 1+, neither side ready | Needs 1+, a side ready | Needs 2+, neither side ready | Needs 2+, a side ready |
|---|---|---|---|---|---|
| 2c4 0e | 16.3% | 90.9% | 31.0% | 19.2% | 8.1% |
| 2c4 2e | 13.6% | 88.0% | 29.2% | 18.2% | 7.5% |
| 2c4 4e | 12.5% | 88.5% | 28.5% | 20.2% | 7.2% |
| 2c4 6e | 11.1% | 89.3% | 24.3% | 11.4% | 3.7% |
| 2c4 8e | 8.4% | 90.9% | 17.2% | 6.9% | 1.2% |
| 0c3 0e | 28.8% | 98.4% | 0.3% | 0% | 0% |
| 0c3 2e | 31.9% | 99.1% | 11.5% | 7.4% | 1.9% |
| 0c3 4e | 26.8% | 97.9% | 1.7% | 0% | 0% |
| 0c3 6e | 33.1% | 99.2% | 12.2% | 9.0% | 2.0% |
| 0c3 8e | 28.3% | 99.3% | 0.6% | 0% | 0% |
| 4a2 0e | 48.6% | 45.7% | 4.3% | 4.0% | 1.0% |
| 4a2 2e | 49.9% | 62.4% | 8.5% | 12.8% | 3.3% |
| 4a2 4e | 61.8% | 81.0% | 23.5% | 38.0% | 16.8% |
| 4a1 0e | 65.8% | 30.0% | 11.5% | 4.7% | 1.1% |
| 4a1 2e | 68.9% | 44.3% | 24.0% | 14.2% | 8.2% |
| 4a1 4e | 69.3% | 52.9% | 33.1% | 25.8% | 17.8% |
| 2c3 0e | 14.6% | 45.1% | 12.3% | 2.3% | 0.7% |
| 2c3 2e | 22.4% | 82.9% | 38.4% | 29.3% | 16.4% |
| 2c3 4e | 19.4% | 79.7% | 34.4% | 28.0% | 13.8% |
| 2c3 6e | 16.9% | 73.0% | 26.9% | 15.4% | 7.0% |
| 2c3 8e | 13.6% | 49.3% | 15.1% | 2.1% | 1.1% |
| 4c3 0e | 34.7% | 71.1% | 15.7% | 11.0% | 2.5% |
| 4c3 2e | 34.8% | 72.2% | 23.3% | 16.4% | 7.5% |
| 4c3 4e | 34.8% | 69.7% | 23.0% | 14.9% | 6.7% |
| 4c4 0e | 32.1% | 55.1% | 1.0% | 0% | 0% |
| 4c4 2e | 29.9% | 55.6% | 5.8% | 5.5% | 0.6% |
| 4c4 4e | 32.1% | 61.5% | 4.9% | 3.6% | 0.6% |
| 4b2 0e | 65.8% | 45.5% | 11.4% | 13.1% | 2.4% |
| 4b2 2e | 67.3% | 52.1% | 30.8% | 24.2% | 17.7% |
| 4b2 4e | 68.0% | 44.3% | 26.1% | 14.9% | 10.2% |

All DRs:

| Subset × edges | Neither side ready | Needs 1+, neither side ready | Needs 1+, a side ready | Needs 2+, neither side ready | Needs 2+, a side ready |
|---|---|---|---|---|---|
| 2c4 0e | 25.1% | 75.8% | 28.1% | 17.1% | 7.7% |
| 2c4 2e | 24.5% | 68.2% | 23.7% | 12.4% | 6.1% |
| 2c4 4e | 25.0% | 67.0% | 23.4% | 12.3% | 6.3% |
| 2c4 6e | 24.9% | 66.6% | 20.0% | 8.7% | 3.6% |
| 2c4 8e | 24.8% | 62.9% | 16.0% | 5.2% | 1.9% |
| 0c3 0e | 44.2% | 76.5% | 2.6% | 2.7% | <0.1% |
| 0c3 2e | 44.1% | 72.6% | 13.7% | 5.8% | 4.2% |
| 0c3 4e | 44.0% | 60.4% | 7.0% | 5.2% | 2.3% |
| 0c3 6e | 44.3% | 77.9% | 15.2% | 6.5% | 5.2% |
| 0c3 8e | 44.1% | 78.3% | 2.2% | 2.5% | 0% |
| 4a2 0e | 69.2% | 33.8% | 3.0% | 3.1% | 0.6% |
| 4a2 2e | 68.9% | 43.7% | 6.4% | 10.5% | 2.7% |
| 4a2 4e | 69.5% | 67.8% | 20.1% | 33.2% | 14.3% |
| 4a1 0e | 69.2% | 25.7% | 10.0% | 4.0% | 0.9% |
| 4a1 2e | 69.9% | 39.7% | 22.4% | 12.4% | 7.5% |
| 4a1 4e | 69.6% | 49.3% | 31.1% | 23.6% | 16.6% |
| 2c3 0e | 24.6% | 32.2% | 9.1% | 1.8% | 0.5% |
| 2c3 2e | 25.1% | 75.2% | 35.5% | 24.1% | 15.0% |
| 2c3 4e | 25.0% | 66.8% | 29.0% | 20.0% | 11.5% |
| 2c3 6e | 25.2% | 57.0% | 21.2% | 10.4% | 5.6% |
| 2c3 8e | 25.0% | 33.6% | 11.2% | 2.5% | 1.0% |
| 4c3 0e | 44.5% | 53.0% | 12.7% | 8.4% | 2.2% |
| 4c3 2e | 44.4% | 54.2% | 21.2% | 12.6% | 7.3% |
| 4c3 4e | 44.0% | 51.6% | 20.5% | 11.6% | 6.4% |
| 4c4 0e | 44.8% | 28.5% | 7.1% | 3.6% | 0.9% |
| 4c4 2e | 44.8% | 35.8% | 7.4% | 3.5% | 1.0% |
| 4c4 4e | 44.2% | 37.7% | 8.5% | 3.9% | 1.2% |
| 4b2 0e | 69.6% | 36.0% | 9.9% | 10.0% | 2.0% |
| 4b2 2e | 69.1% | 45.3% | 28.1% | 20.5% | 16.1% |
| 4b2 4e | 69.6% | 38.2% | 23.4% | 12.4% | 9.0% |

## A finish within one move of the optimal

If a finish one move over the optimal will do, the half turns mostly stop mattering. Each row is a corner subset; each cell is the share of its DRs whose best start among all finishes of at most optimal + 1 moves has that many half turns before the first quarter turn, on the better side:

| Corner subset | Optimal ≤ 13: 0 half turns | Optimal ≤ 13: 1 | Optimal ≤ 13: 2 or more | Optimal ≤ 12: 0 half turns | Optimal ≤ 12: 1 | Optimal ≤ 12: 2 or more | All DRs: 0 half turns | All DRs: 1 | All DRs: 2 or more |
|---|---|---|---|---|---|---|---|---|---|
| 0c0 | 90.4% | 7.2% | 2.3% | 84.8% | 11.3% | 3.8% | 91.4% | 6.5% | 2.1% |
| 2c5 | 92.9% | 6.9% | 0.2% | 90.8% | 9.2% | 0% | 98.1% | 1.9% | <0.1% |
| 2c4 | 87.7% | 11.5% | 0.8% | 83.3% | 15.3% | 1.3% | 92.9% | 6.8% | 0.3% |
| 0c3 | 75.1% | 24.2% | 0.6% | 80.3% | 19.7% | 0% | 90.4% | 9.4% | 0.2% |
| 4a2 | 82.2% | 15.2% | 2.6% | 73.1% | 22.1% | 4.9% | 89.3% | 9.3% | 1.4% |
| 4a1 | 89.6% | 7.9% | 2.4% | 82.1% | 13.4% | 4.5% | 90.7% | 7.1% | 2.2% |
| 2c3 | 89.4% | 9.1% | 1.5% | 81.3% | 15.3% | 3.4% | 92.2% | 6.7% | 1.1% |
| 0c4 | 95.8% | 4.2% | 0.1% | 91.2% | 8.8% | 0% | 98.5% | 1.5% | <0.1% |
| 4c3 | 87.5% | 11.5% | 1.0% | 80.4% | 17.7% | 1.9% | 93.7% | 5.9% | 0.5% |
| 4c4 | 89.2% | 10.3% | 0.5% | 89.8% | 10.2% | 0% | 97.3% | 2.6% | 0.1% |
| 4b2 | 90.9% | 7.0% | 2.1% | 82.3% | 13.1% | 4.6% | 92.5% | 5.8% | 1.7% |
| 4b5 | 92.8% | 7.1% | 0.1% | 91.8% | 8.2% | 0% | 98.3% | 1.7% | <0.1% |
| all DRs | 89.1% | 9.5% | 1.4% | 82.1% | 14.6% | 3.3% | 94.2% | 5.2% | 0.6% |

With an optimal of 13 or less, 1.4% of DRs have no such finish starting its first quarter turn after 0 or 1 half turns, against 12.6% for the optimal itself. Every subset × edges:

| Subset × edges | Optimal ≤ 13: 0 half turns | Optimal ≤ 13: 1 | Optimal ≤ 13: 2 or more | Optimal ≤ 12: 0 half turns | Optimal ≤ 12: 1 | Optimal ≤ 12: 2 or more | All DRs: 0 half turns | All DRs: 1 | All DRs: 2 or more |
|---|---|---|---|---|---|---|---|---|---|
| 0c0 0e | 66.6% | 10.5% | 22.9% | 66.4% | 10.6% | 23.1% | 66.6% | 10.5% | 22.9% |
| 0c0 2e | 88.2% | 9.4% | 2.4% | 85.6% | 11.4% | 3.0% | 88.3% | 9.3% | 2.4% |
| 0c0 4e | 90.7% | 7.0% | 2.3% | 84.6% | 11.4% | 4.0% | 91.4% | 6.5% | 2.1% |
| 0c0 6e | 94.9% | 4.6% | 0.5% | 88.3% | 10.3% | 1.3% | 96.1% | 3.5% | 0.4% |
| 0c0 8e | 87.4% | 9.2% | 3.4% | 79.0% | 15.2% | 5.8% | 90.1% | 7.2% | 2.6% |
| 2c5 0e | 95.5% | 4.5% | 0% | 98.1% | 1.9% | 0% | 99.0% | 1.0% | 0% |
| 2c5 2e | 93.9% | 6.0% | 0.1% | 93.2% | 6.8% | 0% | 98.4% | 1.6% | <0.1% |
| 2c5 4e | 92.5% | 7.2% | 0.3% | 89.9% | 10.1% | 0% | 97.8% | 2.1% | 0.1% |
| 2c5 6e | 92.4% | 7.6% | 0.1% | 89.9% | 10.1% | 0% | 98.2% | 1.8% | <0.1% |
| 2c5 8e | 95.5% | 4.5% | 0% | 89.6% | 10.4% | 0% | 98.7% | 1.3% | <0.1% |
| 2c4 0e | 86.6% | 12.9% | 0.5% | 83.7% | 15.8% | 0.6% | 90.4% | 9.3% | 0.3% |
| 2c4 2e | 88.1% | 11.2% | 0.8% | 82.8% | 15.4% | 1.7% | 92.9% | 6.7% | 0.4% |
| 2c4 4e | 87.0% | 12.1% | 0.9% | 82.4% | 16.2% | 1.4% | 92.7% | 7.0% | 0.4% |
| 2c4 6e | 88.9% | 10.7% | 0.4% | 86.3% | 13.1% | 0.6% | 93.6% | 6.2% | 0.2% |
| 2c4 8e | 90.5% | 9.3% | 0.2% | 90.6% | 9.4% | 0% | 94.8% | 5.1% | 0.1% |
| 0c3 0e | 78.1% | 21.9% | 0% | 89.6% | 10.4% | 0% | 88.1% | 11.8% | 0.1% |
| 0c3 2e | 75.1% | 24.0% | 0.9% | 77.6% | 22.4% | 0% | 89.2% | 10.5% | 0.3% |
| 0c3 4e | 76.5% | 23.5% | 0% | 84.1% | 15.9% | 0% | 92.1% | 7.7% | 0.2% |
| 0c3 6e | 72.9% | 25.9% | 1.2% | 77.5% | 22.5% | 0% | 88.1% | 11.6% | 0.3% |
| 0c3 8e | 78.7% | 21.3% | 0% | 90.2% | 9.8% | 0% | 87.8% | 12.1% | 0.1% |
| 4a2 0e | 93.1% | 6.8% | 0.1% | 90.0% | 10.0% | 0% | 96.6% | 3.4% | <0.1% |
| 4a2 2e | 88.1% | 11.2% | 0.7% | 82.3% | 16.6% | 1.1% | 93.9% | 5.8% | 0.3% |
| 4a2 4e | 78.7% | 17.6% | 3.8% | 69.5% | 24.2% | 6.3% | 84.8% | 12.8% | 2.4% |
| 4a1 0e | 94.9% | 4.7% | 0.4% | 89.7% | 9.1% | 1.2% | 96.0% | 3.7% | 0.3% |
| 4a1 2e | 92.2% | 6.8% | 1.0% | 85.7% | 12.3% | 2.0% | 93.1% | 6.0% | 0.9% |
| 4a1 4e | 87.3% | 9.0% | 3.8% | 79.4% | 14.2% | 6.4% | 88.4% | 8.2% | 3.4% |
| 2c3 0e | 97.4% | 2.6% | <0.1% | 93.7% | 6.3% | 0% | 98.6% | 1.4% | <0.1% |
| 2c3 2e | 88.0% | 10.1% | 1.9% | 80.8% | 15.4% | 3.8% | 89.4% | 8.9% | 1.7% |
| 2c3 4e | 89.2% | 9.3% | 1.6% | 80.4% | 15.9% | 3.7% | 92.1% | 6.8% | 1.1% |
| 2c3 6e | 91.5% | 7.9% | 0.6% | 84.9% | 13.7% | 1.4% | 94.7% | 5.0% | 0.4% |
| 2c3 8e | 97.0% | 3.0% | <0.1% | 93.2% | 6.8% | 0% | 98.5% | 1.5% | <0.1% |
| 0c4 0e | 97.5% | 2.5% | 0% | 93.7% | 6.3% | 0% | 98.5% | 1.5% | 0% |
| 0c4 2e | 96.3% | 3.7% | <0.1% | 92.3% | 7.7% | 0% | 98.4% | 1.6% | <0.1% |
| 0c4 4e | 95.4% | 4.5% | 0.1% | 90.2% | 9.8% | 0% | 98.3% | 1.7% | <0.1% |
| 0c4 6e | 95.8% | 4.2% | 0% | 91.8% | 8.2% | 0% | 98.9% | 1.1% | 0% |
| 0c4 8e | 95.9% | 4.1% | 0% | 100.0% | 0% | 0% | 99.3% | 0.7% | 0% |
| 4c3 0e | 90.1% | 9.6% | 0.3% | 85.5% | 13.8% | 0.7% | 94.5% | 5.4% | 0.1% |
| 4c3 2e | 87.0% | 12.0% | 1.0% | 79.7% | 18.5% | 1.8% | 93.5% | 6.1% | 0.5% |
| 4c3 4e | 87.8% | 11.2% | 1.1% | 80.7% | 17.2% | 2.1% | 93.8% | 5.7% | 0.5% |
| 4c4 0e | 90.3% | 9.7% | 0% | 87.1% | 12.9% | 0% | 98.0% | 2.0% | <0.1% |
| 4c4 2e | 89.2% | 10.2% | 0.6% | 89.7% | 10.3% | 0% | 97.4% | 2.5% | 0.1% |
| 4c4 4e | 89.2% | 10.5% | 0.4% | 90.1% | 9.9% | 0% | 97.1% | 2.8% | 0.1% |
| 4b2 0e | 93.0% | 6.1% | 0.9% | 85.3% | 12.6% | 2.1% | 94.8% | 4.6% | 0.6% |
| 4b2 2e | 89.6% | 7.4% | 2.9% | 80.3% | 13.6% | 6.1% | 91.2% | 6.3% | 2.5% |
| 4b2 4e | 92.0% | 6.6% | 1.4% | 84.2% | 12.6% | 3.2% | 93.5% | 5.4% | 1.1% |
| 4b5 0e | 90.6% | 8.9% | 0.6% | 91.1% | 8.9% | 0% | 97.9% | 2.0% | 0.1% |
| 4b5 2e | 91.9% | 7.8% | 0.2% | 90.0% | 10.0% | 0% | 98.2% | 1.7% | <0.1% |
| 4b5 4e | 93.6% | 6.3% | <0.1% | 93.6% | 6.4% | 0% | 98.4% | 1.6% | <0.1% |

0c0 0e reads differently here too: its finishes with no quarter turn count as 3 or more.

## If U2 and D2 don't count

Count only R2, L2, F2 and B2 before the first quarter turn, so that `U2 R2 U` has one and not two. That changes the number on 7.0% of DRs with an optimal of 13 or less (4.6% of all DRs). The 0 column can't change. Over all subsets, each row is a group of DRs, with the shares needing exactly that many under each count:

| DRs counted | Every half turn counted: 0 | Every half turn counted: 1 | Every half turn counted: 2 | Every half turn counted: 3 or more | U2 and D2 not counted: 0 | U2 and D2 not counted: 1 | U2 and D2 not counted: 2 | U2 and D2 not counted: 3 or more |
|---|---|---|---|---|---|---|---|---|
| Optimal ≤ 13 | 61.5% | 25.9% | 8.8% | 3.8% | 61.5% | 29.9% | 6.9% | 1.7% |
| Optimal ≤ 12 | 56.9% | 27.2% | 10.5% | 5.4% | 56.9% | 31.7% | 8.9% | 2.4% |
| All DRs | 69.9% | 22.2% | 5.9% | 2.1% | 69.9% | 25.1% | 4.2% | 0.8% |

So about a third of the *2 or more* moves down a column, and the picture stays: the rows that need the most are the same four, 4a2 4e, 4a1 4e, 4b2 2e and 2c3 2e. The tables on this page count every half turn, because that's the number of moves you write before the quarter turn. Both counts for every row are in `htr-routes/research/out/ht_first.tsv` in the repository.

## How it was computed

The sample is the one behind [*Which HTR routes to try from a DR*](../htr-routes/): 25,000 uniformly random DR states for each of the 48 subset × edges. For each state every optimal finish is enumerated against the exact optimal-finish table of all 19,508,428,800 DR states ([*Judging a DR by hand*](../judging-a-dr/)), and the fewest moves before the first quarter turn is kept for each reading direction. Pooled rows weight each subset × edges by its exact number of DR states (with a cut on the optimal, by that number times the share that qualifies). The script is `tables/src/half_turns_before_first_qt.py` in the repository.

**Checked.** A second program (`htr-routes/research/htfirst`: a search over half-turn starts against the same exact table, with the first program's cube model but none of its enumeration) gives the same number on all 1,200,000 sampled DRs, on both sides. A third count in Python, with its own move tables, agrees on 12,000 DRs (the first 3,000 of 2c4 2e, 4a1 4e, 2c3 2e and 0c0 0e) and replays every optimal finish of 800 of them on a 54-sticker cube (18,852 finishes, all solve). The within-one-move numbers come from the second program and agree with the third count on 2,000 DRs. The reads: the half turns the corners need on each side were recomputed on the sticker cube for 2,880 DRs (60 of every subset × edges) and the corner case names by the first study's reader for 440, with no difference. The counts over finishes with no extra quarter turn come from the second program too; the third count agrees on 30,000 DRs (those above and the first 3,000 of 4b2 0e, 4b2 2e, 4b2 4e, 4a2 4e, 4a2 2e and 4a1 2e), with the fewest quarter turns of any finish recomputed by its own search over all 2,822,400 pairs of a corner arrangement and an edge pattern, and the fewest and most quarter turns of the optimal finishes equal to the first program's. Every example on this page is replayed on the sticker cube and re-read by that reader. Scripts: `htr-routes/research/src/ht_first.py`, `xhtfirst.py`, `check_ht_first.py`, `ht_first_witness.py`.

**Checked in Lean** (`htr-routes/lean`, HTRRoutes part F and FakeBound/HTFirst; no `sorry`). Over all 29,400 HTR cosets: the fewest quarter turns of a finish into HTR is exact (no sequence of DR moves does it with fewer, and some sequence does it with exactly that many); a half turn never changes it and a quarter turn changes it by exactly one; and in a finish with no extra quarter turn every quarter turn lowers it. Per corner subset: which corner cases are ready (2c5, 0c4 and 4b5 always; 0c0 has nothing to lower; the other eight have both kinds), how many half turns the corners can need before a lowering quarter turn, and where a lowering quarter turn leads. For the worked DRs of this page: each stated optimal is exact and the printed finishes are all of its optimal finishes, and the numbers of the first 200 sampled 2c4 2e DRs are recomputed from the list of all their optimal finishes. The sampled shares in the tables are not proved in Lean.
