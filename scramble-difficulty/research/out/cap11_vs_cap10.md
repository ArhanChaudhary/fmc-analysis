# Scramble difficulty: DRs of at most 11 against at most 10 (2026-11-14)

Same 23,879 scrambles (10,000 uniform, 8,108 official, 5,771 generated), analysis.py --cap 10 / --cap 11
(analysis_c10.*, analysis_c11.*). The cap-10 rerun reproduces the published analysis.txt: of 2,803 decimal values,
about 20 differ in the 3rd decimal (3 scrambles have 1-2 near-cap DRs more or fewer in the new lists).

| What | cap 10 | cap 11 |
|---|---|---|
| DRs per scramble, median (uniform) | 28 | 320 |
| best DR + finish, mean | 21.19 | 20.53 |
| easy (best <= 19) | 9.7% | 16.5% |
| hard | best >= 23 or none: 13.9% | best >= 22 or none: 18.0% |
| fewest bad edges vs number of DRs, Spearman | -0.649 | -0.699 |
| misoriented corners vs number of DRs | 0.004 to 0.010 | 0.003 to 0.008 |
| GBM held-out R^2, number of DRs | 0.715 | 0.828 |
| GBM held-out R^2, best DR + finish | 0.364 | 0.348 |
| AUC easy, GBM | 0.781 | 0.766 |

Conclusions unchanged: edges decide the number of DRs, corners don't; the best single result is mostly luck (even
more so at cap 11); the two-number EO score and the bad-edge classes keep their order. To do when the page moves to
cap 11: every typed number of section 1 and the class table (median DRs, easy/hard shares), and the definitions of
easy/hard (the hard cut moves from 23 to 22).
