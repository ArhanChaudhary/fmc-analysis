# Half turns before the first qt: which visible reads predict it (working notes)

Status, 2026-11-13, final: everything below is now on the reference page `tables/half-turns-before-first-qt.md`
(sections *What you can see that predicts it*, *A finish within one move of the optimal*, *If U2 and D2 don't count*),
rendered by `tables/src/half_turns_before_first_qt.py` from `out/ht_first_extra.json` (`src/xhtfirst.py`) and
`out/ht_first_witness.json`. The page is the reference; these notes are the trail.

Checked: the counts (first qt after 0 / 1 / 2 / 3+ half turns per DR and side) by a second exact search
(`research/htfirst`), equal to the `ht_first_n` / `ht_first_i` columns on all 1,200,000 sampled states, and by an
independent enumeration in Python on 12,000 states (the +1 level on 2,000; 18,852 optimal finishes replayed on the
sticker model; `out/checks/check_ht_first.txt`). The reads (ready side, corner setup count, corner case): the setup
count recomputed on the sticker model for 2,880 states and the corner cases by the first study's `drread` for 440,
no difference (`out/checks/check_ht_first_reads.txt`).

"Needs k+" = on both normal and inverse every optimal finish has at least k half turns before its first qt (the better
side, picked with hindsight). All six half turns count, U2 and D2 too. 25,000 sampled DRs per subset × edges;
standard error of a share of n DRs at most 50 / sqrt(n) points (0.3 for 25,000, 1 for 2,500, 3.5 for 200).
The pooled figures equal the published ones (optimal ≤ 13: 61.5 / 25.9 / 8.8 / 3.8%; ≤ 12: 56.9 / 27.2 / 10.5 / 5.4%;
4a1 4e ≤ 12: 44.9 / 24.5 / 12.0 / 18.6%), with the page's convention that a 0c0 0e DR with no quarter turn in any
optimal finish (29.6% of that row) counts as 3 or more.

## 1. The read that works for "needs a half turn first": is a side trigger-ready?

**Trigger-ready** = on that side some U or D quarter turn, done right now, takes the corners to a subset with one qt
less (the "A qt takes it straight to" column of judging-a-dr, Appendix E). How to see it: recognise the corner case on
normal and on inverse. Ready cases: 2c4 the four that go straight to 2c3 or 4b3 (each bad-corner layout has a ready and
a not-ready case, so the layout alone does not tell); 2c3 the two bad corners 1 up 1 down; 4a2 2-2 diagonal over
diagonal; 4a1 4-0; 4b2 the 2-2 case that goes straight to 4a1; 0c3 the case that goes straight to 4a2.

Corner subsets pooled over edges, DRs with optimal ≤ 13:

| Subset | Neither side ready | Needs 1+ if neither side is ready | Needs 1+ if a side is ready | Needs 2+ if neither | Needs 2+ if a side is ready |
|---|---:|---:|---:|---:|---:|
| 2c4 | 12.5% | 88.6% | 27.7% | 17.9% | 6.5% |
| 0c3 | 30.3% | 98.7% | 7.4% | 5.2% | 1.1% |
| 4a2 | 57.4% | 74.9% | 16.9% | 29.9% | 10.9% |
| 4a1 | 69.0% | 48.5% | 28.4% | 20.1% | 13.1% |
| 2c3 | 19.7% | 79.2% | 33.6% | 26.0% | 12.9% |
| 4c3 | 34.8% | 70.9% | 22.9% | 15.5% | 6.9% |
| 4c4 | 31.2% | 58.9% | 5.2% | 4.3% | 0.6% |
| 4b2 | 67.6% | 48.0% | 27.9% | 19.2% | 13.5% |

The rows asked about:

| Subset × edges | DRs counted | Neither side ready | n | Needs 1+ | Needs 2+ | A side ready: n | Needs 1+ | Needs 2+ |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 2c4 2e | optimal ≤ 13 (43.5% of the row) | 13.6% | 1,481 | 88.0% | 18.2% | 9,404 | 29.2% | 7.5% |
| 2c4 2e | optimal ≤ 12 (11.3%) | 10.0% | 281 | 91.5% | 13.9% | 2,533 | 27.8% | 5.6% |
| 2c4 2e | all | 24.5% | 6,133 | 68.2% | 12.4% | 18,867 | 23.7% | 6.1% |
| 4a2 4e | optimal ≤ 13 (63.5%) | 61.8% | 9,812 | 81.0% | 38.0% | 6,067 | 23.5% | 16.8% |
| 4a2 4e | all | 69.5% | 17,385 | 67.8% | 33.2% | 7,615 | 20.1% | 14.3% |
| 4a1 4e | optimal ≤ 13 (91.2%) | 69.3% | 15,806 | 52.9% | 25.8% | 7,004 | 33.1% | 17.8% |
| 4a1 4e | all | 69.6% | 17,410 | 49.3% | 23.6% | 7,590 | 31.1% | 16.6% |
| 4b2 2e | optimal ≤ 13 (84.5%) | 67.3% | 14,207 | 52.1% | 24.2% | 6,913 | 30.8% | 17.7% |
| 4b2 2e | all | 69.1% | 17,287 | 45.3% | 20.5% | 7,713 | 28.1% | 16.1% |
| 2c3 2e | optimal ≤ 13 (87.9%) | 22.4% | 4,918 | 82.9% | 29.3% | 17,045 | 38.4% | 16.4% |
| 2c3 2e | all | 25.1% | 6,265 | 75.2% | 24.1% | 18,735 | 35.5% | 15.0% |

Good for 1+ on 2c4, 2c3, 4a2, 0c3, 4c3, 4c4; weak on 4a1 and 4b2; and it says little about 2+. The read is sharper on
optimal ≤ 13 than on all DRs.

Per side it is cleaner still. 2c4 2e with optimal ≤ 13, each side on its own (a side = normal or inverse of one DR):

| Case on that side | Bad corners | A qt takes it straight to | Sides | First qt after 0 half turns | After 1 | After 2 | After 3+ |
|---|---|---|---:|---:|---:|---:|---:|
| 2c4-1 | both on one layer, adjacent | 2c3 | 5,098 | 60.7% | 23.5% | 10.0% | 5.7% |
| 2c4-2 | 1 up 1 down, opposite | 4b3 | 2,327 | 31.7% | 49.3% | 14.2% | 4.8% |
| 2c4-3 | both on one layer, adjacent | 2c3 | 4,506 | 74.4% | 0.9% | 11.2% | 13.6% |
| 2c4-4 | both on one layer, adjacent | nothing, needs a setup | 3,129 | 7.8% | 50.6% | 26.2% | 15.3% |
| 2c4-5 | 1 up 1 down, stacked | 4b3 | 1,573 | 50.7% | 1.9% | 24.2% | 23.3% |
| 2c4-6 | 1 up 1 down, opposite | nothing, needs a setup | 2,956 | 4.4% | 56.8% | 18.4% | 20.4% |
| 2c4-7 | 1 up 1 down, stacked | nothing, needs a setup | 2,181 | 8.1% | 26.0% | 27.3% | 38.6% |

A side that needs a setup starts its optimal with a qt in 4 to 8%. On 2c4-3 and 2c4-5 it is a qt at once or two half
turns, almost never exactly one.

## 2. Needing 2+: 4a2 has a rule, the rest only slopes

Count on each side the half turns the corners need before a qt can lower them (0 = trigger-ready; 4a2: diagonal over
diagonal 0, pairs stacked 1, pairs on opposite sides 2, 4-0 3; 4a1: 4-0 0, pairs on opposite sides 1, pairs stacked 2,
diagonal over diagonal 3), take the smaller side. "2 or 3" = on both sides the corners need two or more.

| Subset × edges | DRs counted | Both sides need 2 or 3: share | n | Needs 2+ | Needs 3+ | Otherwise: n | Needs 2+ | Needs 3+ |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 4a2 4e | optimal ≤ 13 | 13.9% | 2,200 | 77.7% | 36.7% | 13,679 | 22.2% | 5.8% |
| 4a2 4e | optimal ≤ 12 | 7.6% | 496 | 86.3% | 30.4% | 6,049 | 23.3% | 4.5% |
| 4a2 4e | all | 24.9% | 6,227 | 54.7% | 28.4% | 18,773 | 18.4% | 5.1% |
| 4a2 2e | optimal ≤ 13 | 6.1% | 600 | 38.7% | 0.0% | 9,303 | 6.1% | 0.0% |
| 4b2 0e | optimal ≤ 13 | 21.2% | 3,942 | 23.4% | 7.9% | 14,625 | 5.7% | 0.4% |
| 4a1 4e | optimal ≤ 13 | 24.1% | 5,489 | 32.8% | 21.1% | 17,321 | 20.3% | 11.5% |
| 4b2 2e | optimal ≤ 13 | 22.7% | 4,796 | 31.9% | 20.3% | 16,324 | 19.2% | 8.8% |
| 4a1 2e | optimal ≤ 13 | 22.8% | 5,004 | 20.7% | 5.4% | 16,953 | 9.9% | 1.8% |
| 4b2 4e | optimal ≤ 13 | 23.2% | 4,753 | 20.6% | 9.1% | 15,737 | 11.2% | 3.2% |

4a2 4e by the exact count (optimal ≤ 13; first qt after 0 / 1 / 2 / 3+): count 0 (n = 6,067) 76.5 / 6.8 / 9.0 / 7.7%;
count 1 (7,612) 19.0 / 54.5 / 22.4 / 4.2%; count 2 (2,020) 20.4 / 2.8 / 44.7 / 32.1%; count 3 (180) 0.6 / 11.7 / 0.0 / 87.8%.

## 3. Needing 2+ on 2c4 2e: nothing visible predicts it well

Base rate 8.9% at optimal ≤ 13 (7.6% of all 2c4 2e, 6.5% at ≤ 12). On optimal ≤ 13:

- Trigger-ready or not: 18.2% against 7.5%.
- Bad corners 1 up 1 down stacked on both sides (1.9% of those DRs, n = 204): 38.2% against 8.4% (on all 2c4 2e: 6.1%
  of the row, 18.0% against 7.0%). Stacked on at least one side (33%): 14.7% against 6.1%.
- The exact pair of corner cases (28 pairs): from 1.8% (2c4-1 with 2c4-2, n = 509) to 42% (2c4-5 with 2c4-7, n = 104).
  Picking the worst and best pair with 100+ DRs on half the sample and reading them on the other half: 28.7%
  (2c4-4 with 2c4-7, n = 174) and 4.2% (2c4-1 on both sides, n = 262).
- Share of the uncertainty about "needs 2+" a read removes (mutual information over entropy, chance level taken off):
  trigger-ready 2.3%, layout on both sides 4.2%, corner case on both sides 7.6%, plus both HTR lengths 8.9%;
  true pairs, slice pairs, E-slice edges solved, E-slice parity 0.0% each. For "needs 1+": trigger-ready 13.4%, corner
  cases 24.1%.
- Where the bad edges sit adds almost nothing: per side, every bad corner and bad edge known explains 10.8% of "2+" on
  that side against 8.8% for the corner case alone.
- Needs the HTR: shorter HTR of 9 (25.5% of those DRs): 15.2% against 6.8%.

## 4. Reads that need the HTR (optimal ≤ 13)

- 4b2 2e with a 3- or 4-move HTR on a side (11.8%, n = 2,488): 2+ in 3.3%, against 24.6% (n = 18,632).
- 4a1 4e: shorter HTR 1–2 (4.9%): 5.9%; 3–4 (26.9%): 38.2%; 5 or more (68.2%): 18.7%.

## 5. Why so little shows (computer only)

The need tracks the number of optimal finishes of the DR, which nobody can see. 2c4 2e, optimal ≤ 13: one optimal
finish 13.3% need 2+, 2–3 11.7%, 4–7 5.8%, 8–15 2.8%, 16 or more 1.2%. All DRs with optimal ≤ 13: 17.4 / 16.1 / 11.9 /
7.1 / 3.5%.

## 6. Within +1 of optimal

A finish one move over the optimum almost never needs 2+ half turns first. All DRs: 0.6% (94.2% have one that starts
with a qt on a side); optimal ≤ 13: 1.4% (89.1%); optimal ≤ 12: 3.3% (82.1%). By corner subset at optimal ≤ 13 the worst
are 4a2 2.6%, 4a1 2.4%, 0c0 2.3% (with its no-qt finishes counted as 3 or more), 4b2 2.1%.
