# Judging a DR by hand: worked examples

*Eleven DRs, read the way the write-up says to read them, with what the exact tables say at each step and then the real optimal.*

November 2026. Goes with "Judging a DR by hand: what the full BFS says" but reads on its own.

---

## How to read these

Every example is a DR state given as a scramble in DR moves on the U/D axis, like the random scrambles in Rodney's Advanced DR Bounding doc. Do the scramble on a solved cube and you're looking at the DR.

The reads, in the order of what they cost you:

1. **Subset**, the way you already name it (2c4 4e and so on).
2. **True pairs**: a corner and an edge next to each other in the U or D layer with both touching stickers matching. 16 places to look.
3. **Corner case on both sides**: where the bad corners sit on normal and on inverse (counted up to turning a layer, so "all four on U plus two on D" is two bad corners on D), and whether a U or D quarter turn drops the corner qt count right away.
4. **Shortest HTR on both sides.**
5. **Corner solution and E-slice parity**: the optimal corner solution, length L. The number of side half turns (R2 L2 F2 B2) in any finish is even if the E-slice is an even permutation and odd if it's odd. If your corner solution has the wrong count you need the best one of the other parity, and no finish is shorter than that. That part is a true bound, proven in Lean.

After each read I give the share of all DR states *with that same read* that finish in 12 or less and in 13 or less. Those numbers are exact counts over all 19,508,428,800 DR states. "Everything together" means subset + pairs + both HTR lengths + L + parity fit as one class.

Then the truth: the optimal finish in DR moves, from the full table.

**How the examples were picked.** 1, 2 and 3 are the DRs in Rodney's and Levi's docs. 11 is the 1qt case from the write-up where a finish with three quarter turns is shorter than the 1qt bound. 4 to 10 are each "the first DR my random generator produced with this read", from a fixed seed. They were picked by the read, never by the outcome, so some of them go against the odds. That's on purpose.

Corner cases are named by where the bad corners are. When it matters which of two look-alike cases it is, I give the range of optimal corner solution lengths the case can have (L 7–10 and so on), which is how they're told apart in the write-up's corner case appendix.

---

## 1. Rodney's first random scramble: a decent 2c3

    U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2   // 2c3 6e

**Subset.** 2c3 6e: 17% finish in 12, 61% in 13. Average optimal 13.20.

**Pairs.** One (UBR + UR). With one pair: 15% / 58%. Slightly worse than the subset.

**Corners.** On normal the bad corners are UBR and DBR, one above the other. On inverse they're UBL and DFR, opposite corners of the cube. Both are the good kind of 2c3, where a quarter turn takes you straight to 4b2 and L is 5–8. For that pair of cases: 38% / 85%. Much better than the subset.

**HTR.** 9 on normal, 7 on inverse:

    U' R2 L2 B2 R2 U F2 R2 U     // HTR, normal (9)
    (U' L2 U F2 R2 L2 D)         // HTR, inverse (7)

For 2c3 6e with 7 and 9: 21% / 70%.

**Corner solution and parity.**

    U' R2 U' R2 U           // corners, L = 5, two side turns

The E-slice is odd, so the finish needs an odd number of side turns and this one has two. The best with an odd count:

    U R2 U2 R2 U R2 U       // corners, 7 moves, three side turns

So nothing under 7 here, and nothing under 9 because of the HTR on normal. For 2c3 6e with L = 5 and the parity costing +2: 24% / 71%.

**Everything together**: 15% / 65%.

**Verdict before solving.** Good for a 13, and a 12 is somewhere between 15% and 38% depending on which read you believe. The reads don't agree with each other, and that's normal: this is what "an sd of 0.8 moves is left" looks like on one DR.

**Truth.** 13.

    R2 B2 D' B2 R2 U B2 R2 U F2 L2 U2 F2   // 13, optimal

Only one of the ten moves starts an optimal finish (R2). Rodney finds a 13 in his doc after bounding his way through three skeletons, and it is optimal. If this DR's last move could be turned the other way and that amounted to an R2 here, the finish would be 12.

---

## 2. Rodney's 4a4: the reads say no, and it's a 13

    U R2 L2 F2 U' B2 D2 F2 D L2 U B2 R2 U' F2 U   // 4c4 4e (4a4 on normal, 4b4 on inverse)

**Subset.** 4c4 4e: 1.8% in 12, 12% in 13. Average 14.38.

**Pairs.** One. 1.1% / 8.7%.

**Corners.** Four bad on both sides, 2-2. The case on normal is one of the two worst 4a4s (L 11–12). For this pair of cases: 1.1% / 9.4%.

**HTR.** 11 on normal, 10 on inverse. 1.3% / 10%.

**Corner solution and parity.** L = 11 and it already has an odd number of side turns, which is what the odd E-slice wants:

    U2 R2 U' R2 U F2 U2 R2 U' F2 U'   // corners, 11, five side turns

So no finish under 11. With L = 11 and the parity for free: 0.7% / 14%.

**Everything together**: 0.3% / 10%.

**Verdict before solving.** Toss it unless the DR was very short.

**Truth.** 13.

    U2 F2 L2 D B2 U' F2 D2 R2 U B2 L2 U'   // 13, optimal

This is the one in ten. Rodney gets there by writing down the four ways to 2qt and bounding each, which is real work on one DR. Nothing you can read off the DR would have told you this one was worth it. That's the limit of triage by reads.

---

## 3. Levi's DR, and why you read both versions of the last move

    Scramble: R' U' F B2 R' F2 L' U2 R2 F2 D2 L2 U2 R' B2 U' F L' F L D F' L2 F2 R' U' F
    (D2 B' L' B U' F2 D L U2 R)   // 10-move DR, 4c3 4e

The DR ends in R on inverse. R' gives a DR too, a different state. Read both.

| | Ending in R (as written) | Ending in R' |
|---|---|---|
| pairs | 2 | 2 |
| corners, normal / inverse | 3-1 / all four on one layer (L 9–10) | 3-1 / 2-2 (L 9–11) |
| for those corners | 4.8% in 12, 28% in 13 | 3.0% / 20% |
| HTR, normal / inverse | 9 / 10 | 9 / 9 |
| for those HTRs | 5.6% / 34% | 11% / 48% |
| L, and with the right parity | 10, 10 | 10, 11 |
| for that | 7.5% / 25% | 3.6% / 32% |
| everything together | 3.5% / 21% | 2.9% / 40% |
| **optimal finish** | **15** | **14** |

**Verdict before solving.** Both are 9+ to HTR on both sides, which is where Zagros throws a 4c3 away, and the corner cases on inverse are the two worst 4a3s. A 13-move finish would need luck (20–40%), a 12 isn't happening.

**Truth.** 15 as written, 14 with R'. Levi's doc says "14-move optimal finish, giving a 24", and that's the R' one. The reads pointed the same way for 13 (21% against 40%) but not for 12. An invertible last move is worth a third of a move on average. Here it's worth a whole one.

---

## 4. A 2c5 with the corners stacked on both sides: dead

    D2 B2 U' R2 D R2 B2 R2 F2 U2 R2 D F2 U R2 U'   // 2c5 2e

**Subset.** 2c5 2e: 2.5% in 12, 16% in 13. Average 14.28.

**Pairs.** Three. 2.3% / 17%. Nothing unusual.

**Corners.** UBL over DBL on normal. UBL over DBL on inverse too. Stacked on both sides: **0.0% in 12, 0.6% in 13**, average 15.31.

You can stop here. For the record:

**HTR.** 11 and 11. For 2c5 2e: 0.0% / 2.0%.

**Corner solution and parity.** L = 13 with an even number of side turns. The E-slice is odd, and the best odd corner solution is 14. So no finish under 14, guaranteed.

**Truth.** 16. Nine of the ten moves start an optimal finish, which is typical for a long one: it's wide and all of it is bad.

---

## 5. A 2c4 with the best corners on both sides

    D' L2 D R2 B2 F2 U2 B2 R2 U L2 U'   // 2c4 4e

**Subset.** 2c4 4e: 9.1% in 12, 38% in 13. Average 13.66.

**Pairs.** One (DFL + DL). 5.8% / 31%. A bad sign.

**Corners.** On normal all four U corners are bad plus DFR and DFL, so turn the U layer in your head: two bad corners, next to each other on D. On inverse it's the same thing on U (UBL and UBR). On both sides a quarter turn goes straight to 2c3. That's the best 2c4 layout: **26% in 12, 75% in 13**, average 12.93.

**HTR.** 9 on normal, 7 on inverse:

    U R2 U B2 L2 U R2 B2 U     // HTR, normal (9)
    (U' F2 U' L2 U B2 U)       // HTR, inverse (7)

For 2c4 4e with 7 and 9: 20% / 64%.

**Corner solution and parity.**

    U R2 U R2 U' L2 B2 D           // corners, L = 8, four side turns
    U' R2 U' R2 F2 U' L2 D' B2     // corners, 9, five side turns

The E-slice is odd, so it's the 9. With L = 8 and +1 for parity: 20% / 55%.

**Everything together**: 17% / 52%.

**Verdict before solving.** Solve it. For a 2c4 this is as good as they come, about a coin flip for 13 and one in five or six for 12, against one in eleven for the subset.

**Truth.** 12.

    U L2 U' R2 B2 U2 F2 B2 R2 D' L2 D   // 12, optimal

Two optimal first moves (U and L2). With an L2 available from the last DR move it would be 11.

---

## 6. A 2c4 with a double stack

    U B2 U' F2 U B2 D2 L2 U' R2 U R2 U' L2 U2   // 2c4 4e

**Subset.** 2c4 4e again: 9.1% / 38%.

**Pairs.** Two. 8.1% / 37%. Average for the subset.

**Corners.** Three of four bad on U and three of four on D, so after turning both layers in your head: UBL over DBL. On inverse: UFR over DFR. Stacked on both sides, and on neither side does a quarter turn lower the qt count without a setup. **0.6% in 12, 7.5% in 13**, average 14.49.

**HTR.** 10 and 10. For 2c4 4e: 0.9% / 11%.

**Corner solution and parity.** L = 12 with an even number of side turns, the E-slice is odd, the best odd one is 13. No finish under 13, guaranteed. So the 12 is ruled out for certain, and for this class 12% reach 13.

**Truth.** 15.

Same subset as example 5, same number of bad pieces, roughly the same pairs. One has a 12 and the other a 15, and the corners on both sides told you which was which in a few seconds.

---

## 7. A 4c3 that's 9+ to HTR on both sides

    R2 U B2 D' F2 U' B2 R2 D F2 U' R2 D' R2 U'   // 4c3 4e

**Subset.** 4c3 4e: 12% in 12, 45% in 13. Average 13.50.

**Pairs.** None. 6.7% / 34%.

**Corners.** 2-2 on both sides. On normal it's a 4b3 where a quarter turn goes straight to 4a2, on inverse a 4a3 with L 8–10. Middle of the pack: 11% / 42%.

**HTR.** 10 on normal, 9 on inverse. This is Zagros's "9+ on both sides, throw away". For 9 and 10: 5.6% / 34%.

**Corner solution and parity.** L = 10 with an odd number of side turns, E-slice even, so 11. With L = 10 and +1: 3.6% / 32%.

**Everything together**: 0.7% / 19%.

**Verdict before solving.** No 12 here. A 13 one time in five. Toss unless the DR is short enough that a 14 helps.

**Truth.** 15.

---

## 8. A 4c3 that's short to HTR on both sides

    R2 U' L2 D2 B2 D' B2 R2 D' F2 U2 F2   // 4c3 4e

**Subset.** 4c3 4e: 12% / 45%.

**Pairs.** Four. 19% / 58%.

**Corners.** 3-1 on normal (a 4b3). On inverse the best 4a3 there is: 2-2, L 7–9, a quarter turn straight to 4b2. For that pair: 21% / 68%.

**HTR.** 8 on normal, 7 on inverse:

    L2 U F2 U F2 U2 R2 U       // HTR, normal (8)
    (U L2 U2 F2 U L2 U)        // HTR, inverse (7)

For 4c3 4e with 7 and 8: **43% in 12, 85% in 13**.

**Corner solution and parity.** L = 8 with an even count, E-slice odd, so 9. 19% / 60%.

**Everything together**: 63% / 95%.

**Verdict before solving.** Every read says yes. This is the DR you spend your time on.

**Truth.** 12.

    F2 U2 F2 D R2 B2 D B2 D2 L2 U R2   // 12, optimal

And 11 if the last DR move gives you an F2 or a B2.

Examples 7 and 8 are the same subset. This is the spread Zagros's rule is cutting through: 0.7% against 63% for a 12 once everything is read.

---

## 9. A blocky 4c4

    R2 U F2 U' L2 U R2 D' B2 U' F2 D   // 4c4 4e

**Subset.** 4c4 4e: 1.8% in 12, 12% in 13. Average 14.38. Normally a toss.

**Pairs.** Six. With six or more: **6.1% in 12, 28% in 13**, average 13.88. Only 0.1% of all DRs are a 4c4 4e this blocky.

**Corners.** 3-1 on normal, 2-2 on inverse. 1.3% / 11%. No help.

**HTR.** 11 and 10. 1.3% / 10%. No help.

**Corner solution and parity.** L = 11 and the parity fits. 0.7% / 14%.

**Everything together**: 2.8% / 29%.

**Verdict before solving.** The only read that likes it is the pairs, and pairs take it from a 12% shot at 13 to 28–29%. Worth a look with a short DR, with low hopes for 12.

**Truth.** 12.

    D' F2 U B2 D R2 U' L2 U F2 U' R2   // 12, optimal

One optimal first move. That's the 3-in-100 outcome, so don't read it as "blocky 4c4s are good". Read it as: pairs were the only thing pointing the right way, and HTR length and corners, which usually carry more, saw nothing.

---

## 10. A 4b2 where everything says 12 and it's a 13

    U2 F2 R2 B2 U2 L2 F2 D' L2 F2 L2 R2 U   // 4b2 4e

**Subset.** 4b2 4e: 34% in 12, 82% in 13. Average 12.73.

**Pairs.** None. 20% / 69%.

**Corners.** 2-2 with L 3–6 on normal, the best 4b2 case (a quarter turn straight to 4a1). 3-1 with L 4–7 on inverse, the second best. 47% / 90%.

**HTR.** 4 on normal, 8 on inverse:

    U' F2 R2 D                    // HTR, normal (4): the trigger is right there
    (F2 R2 U' R2 B2 U2 L2 U)      // HTR, inverse (8)

For 4b2 4e with 4 and 8: **85% in 12**, 99.6% in 13.

**Corner solution and parity.** L = 5 and the parity fits. 47% / 90%.

**Everything together**: 76% / 97%.

**Verdict before solving.** A 4-move HTR on a 4b2 4e. Of course you solve it, and you expect a 12.

**Truth.** 13.

    U' R2 L2 F2 L2 D F2 L2 U2 B2 R2 F2 U2   // 13, optimal

The optimal here takes six moves to get to HTR and seven half turns after it. No read is ever certain: this one sat in the 15% of its HTR cell and the 24% of its full class that don't get to 12. Pricing the part after HTR before you execute it is what Rodney's NISS@1qt tracing is for.

---

## 11. A 1qt case where a 3qt finish beats the 1qt bound

    U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2   // 4a1 4e

**HTR.** 6 on normal, 5 on inverse:

    F2 R2 F2 R2 F2 U     // HTR, normal (6)
    (U2 F2 R2 B2 U)      // HTR, inverse (5)

**Levi's formula.** 6 + 5 − 1 = 10. So the best finish with one quarter turn is 10 moves.

**Truth.** 7.

    U B2 L2 F2 D F2 D   // 7, three quarter turns

The formula is exact for finishes with one quarter turn, which is what it's for, and says nothing about finishes with three. Over all 4a1 4e, a 3qt finish is shorter than the formula 11.7% of the time. The other reads here: five pairs (81% in 12 for 4a1 4e with five pairs), L = 3 with the parity for free, and 90% in 12 with everything together. So when a 4a1 4e is this blocky and the bound still says 10, it's worth a minute on the 3qt finishes before you believe it.

---

## What the examples show

- **Corners on both sides are the best quick read at 4–5qt.** Examples 4, 5 and 6 are decided by them in seconds: 0.0%, 26% and 0.6% for a 12.
- **HTR on both sides is the best read once you have it.** Examples 7 and 8: 5.6% against 43%.
- **Pairs are free and sometimes the only read that's right** (example 9), and sometimes wrong (example 5 had one pair and a 12).
- **The parity bound is the only certainty.** In examples 4 and 6 it rules out the target outright: no finish under 14, no finish under 13.
- **Odds are odds.** Example 2 was a 10% shot at 13 and came in. Example 10 was a 76% shot at 12 and didn't. Over many DRs the reads roughly double your hit rate. On one DR they can't promise anything, and for that you still need to bound per skeleton the way Rodney does.
