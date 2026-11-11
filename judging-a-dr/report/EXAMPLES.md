# Judging a DR by hand: worked examples

*Eleven DRs, read the way the write-up says to read them, with what the exact tables say at each step and then the real optimal. Then 300 more at random, in tables.*

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

The first three you get by looking. The last two you have to solve for, and the numbers assume you found the shortest HTR and the optimal corner solution.

After each read I give four numbers, **a / b / c / d**: the share of all DR states *with that same read* whose optimal finish is 10 or less / 11 or less / 12 or less / 13 or less. They are exact counts over all 19,508,428,800 DR states. 0 means no state at all gets there, <0.01% means a few do.

Which of the four is yours depends on the DR. A 9- or 10-move DR gets finished whatever it looks like, and a 12 or a 13 from it is a result. The DRs you want to prune are the 11-movers, and those need a 10 or an 11 (one more if the first move of the finish merges with the last move of the DR). The examples are DR states with no DR length attached, so each verdict says what you'd do with it at 9 or 10 moves and at 11.

What each line counts:

- **Subset**: every DR of that subset (2c3 6e).
- **Pairs**: the ones of that subset with that many true pairs.
- **Corners**: every DR of that corner subset with that pair of corner cases, all edge counts together.
- **Without solving**: subset + pairs + corner case on both sides, as one class. This is where you stand before you pick up a pen.
- **HTR**: the ones of that subset with those two HTR lengths.
- **Corner solution and parity**: the ones of that subset with that L and that cost for the right parity.
- **Everything together**: subset + pairs + both HTR lengths + L + parity fit, as one class.

Then the truth: the optimal finish in DR moves, from the full table.

**How the examples were picked.** 1, 2 and 3 are the DRs in Rodney's and Levi's docs. 11 is the 1qt case from the write-up where a finish with three quarter turns is shorter than the 1qt bound. 4 to 10 are each "the first DR my random generator produced with this read", from a fixed seed. They were picked by the read, never by the outcome, so some of them go against the odds. That's on purpose. (That generator made each state with 30 random moves, which leans towards states with short finishes, so don't tally the outcomes of these seven. The 300 at the end are uniformly random.)

Corner cases are named by where the bad corners are. When it matters which of two look-alike cases it is, I give the range of optimal corner solution lengths the case can have (L 7–10 and so on), which is how they're told apart in the write-up's corner case appendix.

---

## 1. Rodney's first random scramble: a decent 2c3

    U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2   // 2c3 6e

**Subset.** 2c3 6e: 0.47% / 3.2% / 17% / 61% finish in 10 / 11 / 12 / 13. Average optimal 13.20.

**Pairs.** One (UBR + UR). With one pair: 0.32% / 2.4% / 15% / 58%. Slightly worse than the subset.

**Corners.** On normal the bad corners are UBR and DBR, one above the other. On inverse they're UBL and DFR, opposite corners of the cube. Both are the good kind of 2c3, where a quarter turn takes you straight to 4b2 and L is 5–8. For that pair of cases: 2.3% / 10% / 38% / 85%. Much better than the subset.

**Without solving.** 2c3 6e, one pair, those corners: 0.58% / 4.1% / 23% / 74%. (Lower than the corners line because that one pools every 2c3, and 6e is the bad end of 2c3.)

**HTR.** 9 on normal, 7 on inverse:

    U' R2 L2 B2 R2 U F2 R2 U     // HTR, normal (9)
    (U' L2 U F2 R2 L2 D)         // HTR, inverse (7)

For 2c3 6e with 7 and 9: 0.57% / 3.9% / 21% / 69%.

**Corner solution and parity.**

    U' R2 U' R2 U           // corners, L = 5, two side turns

The E-slice is odd, so the finish needs an odd number of side turns and this one has two. The best with an odd count:

    U R2 U2 R2 U R2 U       // corners, 7 moves, three side turns

So nothing under 7 here, and nothing under 9 because of the HTR on normal. For 2c3 6e with L = 5 and the parity costing +2: 0.58% / 4.3% / 24% / 71%.

**Everything together**: 0 / 2.5% / 15% / 65%.

**Verdict before solving.** At 9 or 10 moves you solve it: good for a 13, and a 12 is somewhere between 15% and 38% depending on which read you believe. At 11 moves it's a pass: an 11 is 2–4% on every line that knows about the six bad edges, and a 10 is half a percent at best. The reads don't agree with each other, and that's normal: this is what "an sd of 0.8 moves is left" looks like on one DR.

**Truth.** 13.

    R2 B2 D' B2 R2 U B2 R2 U F2 L2 U2 F2   // 13, optimal

Only one of the ten moves starts an optimal finish (R2). Rodney finds a 13 in his doc after bounding his way through three skeletons, and it is optimal. If this DR's last move could be turned the other way and that amounted to an R2 here, the finish would be 12.

---

## 2. Rodney's 4a4: the reads say no, and it's a 13

    U R2 L2 F2 U' B2 D2 F2 D L2 U B2 R2 U' F2 U   // 4c4 4e (4a4 on normal, 4b4 on inverse)

**Subset.** 4c4 4e: 0.02% / 0.21% / 1.8% / 12% finish in 10 / 11 / 12 / 13. Average optimal 14.38.

**Pairs.** One. <0.01% / 0.10% / 1.1% / 8.7%.

**Corners.** Four bad on both sides, 2-2. The case on normal is one of the two worst 4a4s (L 11–12). For this pair of cases: 0 / 0.07% / 1.1% / 9.4%.

**Without solving.** 4c4 4e, one pair, those corners: 0 / 0 / 0.47% / 6.3%.

**HTR.** 11 on normal, 10 on inverse. 0 / 0.07% / 1.3% / 10%.

**Corner solution and parity.** L = 11 and it already has an odd number of side turns, which is what the odd E-slice wants:

    U2 R2 U' R2 U F2 U2 R2 U' F2 U'   // corners, 11, five side turns

So no finish under 11. With L = 11 and the parity for free: 0 / 0.12% / 0.73% / 14%.

**Everything together**: 0 / 0.02% / 0.29% / 10%.

**Verdict before solving.** Toss it unless the DR was very short. At 11 moves it's gone before you solve anything: no 4c4 4e with one pair and these corners finishes in 11 at all. Even at 10 moves a 12 is about 1% on any single read and under half a percent with them together. What's left is a one-in-ten 13.

**Truth.** 13.

    U2 F2 L2 D B2 U' F2 D2 R2 U B2 L2 U'   // 13, optimal

This is the one in ten. Rodney gets there by writing down the four ways to 2qt and bounding each, which is real work on one DR. Nothing you can read off the DR would have told you this one was worth it. That's the limit of triage by reads.

---

## 3. Levi's DR, and why you read both versions of the last move

    Scramble: R' U' F B2 R' F2 L' U2 R2 F2 D2 L2 U2 R' B2 U' F L' F L D F' L2 F2 R' U' F
    (D2 B' L' B U' F2 D L U2 R)   // 10-move DR, 4c3 4e

The DR ends in R on inverse. R' gives a DR too, a different state. Read both. Every row of four numbers is the share finishing in 10 / 11 / 12 / 13.

| | Ending in R (as written) | Ending in R' |
|---|---|---|
| subset | 4c3 4e: 0.35% / 2.3% / 12% / 45% | 4c3 4e: 0.35% / 2.3% / 12% / 45% |
| pairs | 2 | 2 |
| for those pairs | 0.30% / 2.1% / 11% / 45% | 0.30% / 2.1% / 11% / 45% |
| corners, normal / inverse | 3-1 / all four on one layer (L 9–10) | 3-1 / 2-2 (L 9–11) |
| for those corners | 0.03% / 0.51% / 4.8% / 28% | 0.01% / 0.29% / 3.0% / 20% |
| without solving | <0.01% / 0.29% / 3.9% / 25% | 0.02% / 0.31% / 2.7% / 19% |
| HTR, normal / inverse | 9 / 10 | 9 / 9 |
| for those HTRs | 0.02% / 0.51% / 5.6% / 34% | 0.15% / 1.6% / 11% / 48% |
| L, and with the right parity | 10, 10 | 10, 11 |
| for that | 0.09% / 0.23% / 7.5% / 25% | 0 / 1.3% / 3.6% / 32% |
| everything together | <0.01% / 0.02% / 3.5% / 21% | 0 / 1.0% / 2.9% / 40% |
| **optimal finish** | **15** | **14** |

**Verdict before solving.** It's a 10-move DR, so it gets solved either way. Both versions are 9+ to HTR on both sides, which is where Zagros throws a 4c3 away, and the corner cases on inverse are the two worst 4a3s. A 13-move finish would need luck (20–40%), a 12 isn't happening (3%), and an 11 is somewhere between 0.02% and 1.6% depending on the line. With R' a 10 is ruled out for certain, because the corner solution of the right parity is 11. One move longer and this DR would have been a toss on sight.

**Truth.** 15 as written, 14 with R'. Levi's doc says "14-move optimal finish, giving a 24", and that's the R' one. The reads pointed the same way for 13 (21% against 40%) but not for 12 (3.5% against 2.9%). An invertible last move is worth a third of a move on average. Here it's worth a whole one.

---

## 4. A 2c5 with the corners stacked on both sides: dead

    D2 B2 U' R2 D R2 B2 R2 F2 U2 R2 D F2 U R2 U'   // 2c5 2e

**Subset.** 2c5 2e: 0.03% / 0.30% / 2.5% / 16% finish in 10 / 11 / 12 / 13. Average optimal 14.28.

**Pairs.** Three. <0.01% / 0.22% / 2.3% / 17%. Nothing unusual.

**Corners.** UBL over DBL on normal. UBL over DBL on inverse too. Stacked on both sides: **0 / 0 / 0 / 0.64%**, average 15.31. Not one of them finishes in 12.

**Without solving.** 2c5 2e, three pairs, stacked on both sides: 0 / 0 / 0 / 0.65%.

You can stop here, whatever the length of the DR. For the record:

**HTR.** 11 and 11. For 2c5 2e: 0 / 0 / 0.02% / 2.0%.

**Corner solution and parity.** L = 13 with an even number of side turns. The E-slice is odd, and the best odd corner solution is 14. So no finish under 14, guaranteed.

**Everything together**: 0 / 0 / 0 / 0.

**Verdict before solving.** Dead at any DR length, and you knew it after the corners.

**Truth.** 16. Nine of the ten moves start an optimal finish, which is typical for a long one: it's wide and all of it is bad.

---

## 5. A 2c4 with the best corners on both sides

    D' L2 D R2 B2 F2 U2 B2 R2 U L2 U'   // 2c4 4e

**Subset.** 2c4 4e: 0.23% / 1.6% / 9.1% / 38% finish in 10 / 11 / 12 / 13. Average optimal 13.66.

**Pairs.** One (DFL + DL). 0.07% / 0.74% / 5.8% / 31%. A bad sign.

**Corners.** On normal all four U corners are bad plus DFR and DFL, so turn the U layer in your head: two bad corners, next to each other on D. On inverse it's the same thing on U (UBL and UBR). On both sides a quarter turn goes straight to 2c3. That's the best 2c4 layout: **0.92% / 5.6% / 26% / 75%**, average 12.93.

**Without solving.** 2c4 4e, one pair, the best corners on both sides: 0.33% / 2.9% / 18% / 67%.

**HTR.** 9 on normal, 7 on inverse:

    U R2 U B2 L2 U R2 B2 U     // HTR, normal (9)
    (U' F2 U' L2 U B2 U)       // HTR, inverse (7)

For 2c4 4e with 7 and 9: 0.75% / 4.3% / 20% / 64%.

**Corner solution and parity.**

    U R2 U R2 U' L2 B2 D           // corners, L = 8, four side turns
    U' R2 U' R2 F2 U' L2 D' B2     // corners, 9, five side turns

The E-slice is odd, so it's the 9. With L = 8 and +1 for parity: 0.55% / 2.6% / 20% / 55%.

**Everything together**: 0.19% / 1.5% / 17% / 52%.

**Verdict before solving.** At 9 or 10 moves, solve it. For a 2c4 this is as good as they come, about a coin flip for 13 and one in five or six for 12, against one in eleven for the subset. At 11 moves it's a long shot even so: the best corners there are take an 11 from 1.6% to 5.6%, the single pair pulls that back to about 3%, and with everything read it's 1.5%. A 10 is under 1% on every line. That's what 4qt looks like at this target.

**Truth.** 12.

    U L2 U' R2 B2 U2 F2 B2 R2 D' L2 D   // 12, optimal

Two optimal first moves (U and L2). With an L2 available from the last DR move it would be 11.

---

## 6. A 2c4 with a double stack

    U B2 U' F2 U B2 D2 L2 U' R2 U R2 U' L2 U2   // 2c4 4e

**Subset.** 2c4 4e again: 0.23% / 1.6% / 9.1% / 38% finish in 10 / 11 / 12 / 13. Average optimal 13.66.

**Pairs.** Two. 0.14% / 1.2% / 8.1% / 37%. Average for the subset.

**Corners.** Three of four bad on U and three of four on D, so after turning both layers in your head: UBL over DBL. On inverse: UFR over DFR. Stacked on both sides, and on neither side does a quarter turn lower the qt count without a setup. **0 / 0.03% / 0.63% / 7.5%**, average 14.49.

**Without solving.** 2c4 4e, two pairs, that double stack: 0 / 0.02% / 0.68% / 6.9%.

**HTR.** 10 and 10. For 2c4 4e: <0.01% / 0.04% / 0.89% / 11%.

**Corner solution and parity.** L = 12 with an even number of side turns, the E-slice is odd, the best odd one is 13. No finish under 13, guaranteed. So the 12 is ruled out for certain, and for this class 12% reach 13: 0 / 0 / 0 / 12%.

**Everything together**: 0 / 0 / 0 / 9.8%.

**Verdict before solving.** A toss at any DR length, in the few seconds it takes to see the two stacks. A 13 one time in ten is all there is.

**Truth.** 15.

Same subset as example 5, same number of bad pieces, roughly the same pairs. One has a 12 and the other a 15, and the corners on both sides told you which was which in a few seconds.

---

## 7. A 4c3 that's 9+ to HTR on both sides

    R2 U B2 D' F2 U' B2 R2 D F2 U' R2 D' R2 U'   // 4c3 4e

**Subset.** 4c3 4e: 0.35% / 2.3% / 12% / 45% finish in 10 / 11 / 12 / 13. Average optimal 13.50.

**Pairs.** None. 0.08% / 0.87% / 6.7% / 33%.

**Corners.** 2-2 on both sides. On normal it's a 4b3 where a quarter turn goes straight to 4a2, on inverse a 4a3 with L 8–10. Middle of the pack: 0.35% / 2.1% / 11% / 42%.

**Without solving.** 4c3 4e, no pairs, those corners: 0.11% / 1.1% / 7.7% / 34%.

**HTR.** 10 on normal, 9 on inverse. This is Zagros's "9+ on both sides, throw away". For 9 and 10: 0.02% / 0.51% / 5.6% / 34%.

**Corner solution and parity.** L = 10 with an odd number of side turns, E-slice even, so 11. With L = 10 and +1: 0 / 1.3% / 3.6% / 32%.

**Everything together**: 0 / 0.05% / 0.68% / 19%.

**Verdict before solving.** No 12 here. A 13 one time in five. Toss unless the DR is short enough that a 14 helps. At 11 moves there's nothing to think about: the corner solution of the right parity is 11, so a 10 is ruled out for certain, and an 11 is one in 2,000 with everything read.

**Truth.** 15.

---

## 8. A 4c3 that's short to HTR on both sides

    R2 U' L2 D2 B2 D' B2 R2 D' F2 U2 F2   // 4c3 4e

**Subset.** 4c3 4e: 0.35% / 2.3% / 12% / 45% finish in 10 / 11 / 12 / 13. Average optimal 13.50.

**Pairs.** Four. 0.78% / 4.1% / 18% / 58%.

**Corners.** 3-1 on normal (a 4b3). On inverse the best 4a3 there is: 2-2, L 7–9, a quarter turn straight to 4b2. For that pair: 0.65% / 4.1% / 21% / 68%.

**Without solving.** 4c3 4e, four pairs, those corners: 1.2% / 7.3% / 32% / 82%.

**HTR.** 8 on normal, 7 on inverse:

    L2 U F2 U F2 U2 R2 U       // HTR, normal (8)
    (U L2 U2 F2 U L2 U)        // HTR, inverse (7)

For 4c3 4e with 7 and 8: **3.4% / 14% / 43% / 85%**.

**Corner solution and parity.** L = 8 with an even count, E-slice odd, so 9. 0.60% / 4.1% / 19% / 60%.

**Everything together**: 6.6% / 20% / 63% / 95%.

**Verdict before solving.** Every read says yes. This is the DR you spend your time on, and it's the kind of 4c3 you keep at 11 moves too: one in five for an 11 with everything read, against one in 43 for the subset.

**Truth.** 12.

    F2 U2 F2 D R2 B2 D B2 D2 L2 U R2   // 12, optimal

And 11 if the last DR move gives you an F2 or a B2.

Examples 7 and 8 are the same subset. This is the spread Zagros's rule is cutting through: once everything is read, 0.68% against 63% for a 12 and 0.05% against 20% for an 11.

---

## 9. A blocky 4c4

    R2 U F2 U' L2 U R2 D' B2 U' F2 D   // 4c4 4e

**Subset.** 4c4 4e: 0.02% / 0.21% / 1.8% / 12% finish in 10 / 11 / 12 / 13. Average optimal 14.38. Normally a toss.

**Pairs.** Six. With six or more: **0.12% / 0.93% / 6.1% / 28%**, average 13.88. Only 0.1% of all DRs are a 4c4 4e this blocky.

**Corners.** 3-1 on normal, 2-2 on inverse. 0 / 0.08% / 1.3% / 11%. No help.

**Without solving.** 4c4 4e, five or more pairs, those corners: 0 / 0.37% / 4.7% / 28%.

**HTR.** 11 and 10. 0 / 0.07% / 1.3% / 10%. No help.

**Corner solution and parity.** L = 11 and the parity fits. 0 / 0.12% / 0.73% / 14%.

**Everything together**: 0 / 0.43% / 2.8% / 29%.

**Verdict before solving.** The only read that likes it is the pairs, and pairs take it from a 12% shot at 13 to 28–29%. Worth a look with a short DR, with low hopes for 12. At 11 moves, no: 11 to HTR on normal means no 10 for certain, and even six pairs leave an 11 under 1%.

**Truth.** 12.

    D' F2 U B2 D R2 U' L2 U F2 U' R2   // 12, optimal

One optimal first move. That's the 3-in-100 outcome, so don't read it as "blocky 4c4s are good". Read it as: pairs were the only thing pointing the right way, and HTR length and corners, which usually carry more, saw nothing.

---

## 10. A 4b2 where everything says 12 and it's a 13

    U2 F2 R2 B2 U2 L2 F2 D' L2 F2 L2 R2 U   // 4b2 4e

**Subset.** 4b2 4e: 1.8% / 8.8% / 34% / 82% finish in 10 / 11 / 12 / 13. Average optimal 12.73.

**Pairs.** None. 0.41% / 3.4% / 20% / 69%.

**Corners.** 2-2 with L 3–6 on normal, the best 4b2 case (a quarter turn straight to 4a1). 3-1 with L 4–7 on inverse, the second best. 3.8% / 15% / 47% / 90%.

**Without solving.** 4b2 4e, no pairs, those corners: 0.81% / 5.4% / 28% / 78%.

**HTR.** 4 on normal, 8 on inverse:

    U' F2 R2 D                    // HTR, normal (4): the trigger is right there
    (F2 R2 U' R2 B2 U2 L2 U)      // HTR, inverse (8)

For 4b2 4e with 4 and 8: **13% / 41% / 84% / 99.6%**.

**Corner solution and parity.** L = 5 and the parity fits. 3.4% / 15% / 47% / 90%.

**Everything together**: 4.2% / 18% / 76% / 97%.

**Verdict before solving.** A 4-move HTR on a 4b2 4e. Of course you solve it, at any DR length, and you expect a 12. At 11 moves it's the HTR that keeps it alive: before you found it this was a 5% shot at an 11, with it 41% (18% with everything read).

**Truth.** 13.

    U' R2 L2 F2 L2 D F2 L2 U2 B2 R2 F2 U2   // 13, optimal

The optimal here takes six moves to get to HTR and seven half turns after it. No read is ever certain: this one sat in the 16% of its HTR cell and the 24% of its full class that don't get to 12. Pricing the part after HTR before you execute it is what Rodney's NISS@1qt tracing is for.

---

## 11. A 1qt case where a 3qt finish beats the 1qt bound

    U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2   // 4a1 4e

**HTR.** 6 on normal, 5 on inverse:

    F2 R2 F2 R2 F2 U     // HTR, normal (6)
    (U2 F2 R2 B2 U)      // HTR, inverse (5)

**Levi's formula.** 6 + 5 − 1 = 10. So the best finish with one quarter turn is 10 moves.

**Truth.** 7.

    U B2 L2 F2 D F2 D   // 7, three quarter turns

The formula is exact for finishes with one quarter turn, which is what it's for, and says nothing about finishes with three. Over all 4a1 4e, a 3qt finish is shorter than the formula 11.7% of the time. The other reads here: five pairs (15% / 43% / 81% / 99% in 10 / 11 / 12 / 13 for 4a1 4e with five pairs), L = 3 with the parity for free, and 12% / 45% / 90% / 100% with everything together. So when a 4a1 4e is this blocky and the bound still says 10, it's worth a minute on the 3qt finishes before you believe it. On an 11-move DR a bound of 10 reads as "a 21 at best", and here there was an 18 under it.

---

## What the examples show

- **Corners on both sides are the best quick read at 4–5qt.** Examples 4, 5 and 6 are decided by them in seconds: 0, 26% and 0.63% for a 12, and 0, 5.6% and 0.03% for an 11.
- **HTR on both sides is the best read once you have it.** Examples 7 and 8: 5.6% against 43% for a 12, 0.51% against 14% for an 11.
- **Pairs are free and sometimes the only read that's right** (example 9), and sometimes wrong (example 5 had one pair and a 12).
- **The target changes the verdict.** Examples 1 and 5 are DRs you solve at 9 or 10 moves and pass on at 11: a 12 is about one in five, an 11 is a few percent. Example 8 is the one you keep at 11 moves.
- **The parity bound is the only certainty, and it bites more the lower your target.** In examples 4 and 6 it rules out a 12 outright: no finish under 14, no finish under 13. In examples 2, 7 and 9 the corner solution of the right parity is 11, which is no use against a 12 and rules out a 10.
- **Odds are odds.** Example 2 was a 10% shot at 13 and came in. Example 10 was a 76% shot at 12 and didn't. Over many DRs the reads roughly double your hit rate for a 12, and do more than that for a 10 or an 11. On one DR they can't promise anything, and for that you still need to bound per skeleton the way Rodney does.

---

<!-- many-examples:start -->

## 300 more, at random

Three hundred more DR states for fun, 25 for each of the 12 corner subsets, so you can hold your own reads against the table. They are the first 25 of each subset in a run of uniformly random DR states (200 random DR moves each, from a fixed seed). Nothing was picked for how it came out, and 0c0 or 0c3 get as many rows as 2c4 even though they come up far less often.

Each state is given by a shortest scramble, the inverse of an optimal finish. So the scramble is exactly as long as the optimal and undoing it is the solution: the answer is visible on purpose. What is worth looking at is how the reads line up with it.

The columns, the same in every table:

- **Scramble**: do it on a solved cube and you are looking at the DR.
- **Edges**: the number of bad edges, so with the heading it gives the subset (2c4 with 4e is 2c4 4e).
- **True pairs**: counted as in the reads above.
- **Corner case, normal / inverse**: the case names of the write-up's corner case appendix. The cases that show up are listed above each table with where their bad corners sit.
- **Shortest HTR, normal / inverse**: the true shortest on each side.
- **DRs that read the same**: the share finishing in 10 / 11 / 12 or less among all DR states with the same subset, the same number of pairs (five or more count as one), the same two corner cases and the same two HTR lengths. 0 means no such state gets there.
- **Optimal**: the optimal finish in DR moves.

### 0c0

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 0c0-1 | none bad | 0–5 | nothing, needs a setup |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `U2 L2 U B2 R2 F2 D2 B2 R2 F2 U' L2 U2` | 2e | 3 | 0c0-1 / 0c0-1 | 6 / 6 | 8.6% / 33% / 78% | 13 |
| 2 | `B2 D2 R2 B2 D U2 B2 F2 L2 R2 U' R2` | 8e | 0 | 0c0-1 / 0c0-1 | 6 / 6 | 3.0% / 13% / 39% | 12 |
| 3 | `L2 F2 R2 U2 L2 U2 F2 R2 U B2 F2 D` | 4e | 3 | 0c0-1 / 0c0-1 | 4 / 5 | 15% / 35% / 74% | 12 |
| 4 | `U2 F2 D' L2 R2 U' F2 U2 R2 D L2 R2 U'` | 4e | 2 | 0c0-1 / 0c0-1 | 7 / 5 | 5.0% / 20% / 57% | 13 |
| 5 | `F2 D2 B2 D R2 F2 L2 D2 L2 R2 U'` | 2e | 5 | 0c0-1 / 0c0-1 | 5 / 6 | 16% / 44% / 84% | 11 |
| 6 | `U2 L2 B2 U' B2 D2 B2 R2 F2 D' U' B2 U'` | 4e | 0 | 0c0-1 / 0c0-1 | 7 / 5 | 2.3% / 15% / 45% | 13 |
| 7 | `F2 L2 F2 D2 U' B2 D' L2 F2 R2 D' B2 U'` | 6e | 0 | 0c0-1 / 0c0-1 | 8 / 8 | 0.21% / 2.6% / 17% | 13 |
| 8 | `D' B2 F2 D' F2 U' L2 F2 R2 U B2 U2` | 2e | 3 | 0c0-1 / 0c0-1 | 6 / 5 | 12% / 38% / 81% | 12 |
| 9 | `L2 U2 F2 L2 D B2 F2 D' B2 R2 B2` | 4e | 5 | 0c0-1 / 0c0-1 | 5 / 7 | 16% / 40% / 79% | 11 |
| 10 | `B2 U F2 L2 F2 D L2 U' B2 F2 D' R2 D2` | 4e | 4 | 0c0-1 / 0c0-1 | 7 / 6 | 6.0% / 23% / 66% | 13 |
| 11 | `L2 R2 D L2 D2 B2 R2 U2 F2 U' L2 R2` | 4e | 4 | 0c0-1 / 0c0-1 | 7 / 7 | 5.4% / 21% / 59% | 12 |
| 12 | `R2 U R2 F2 R2 U' F2 D2 L2 U2 R2 U2` | 2e | 3 | 0c0-1 / 0c0-1 | 6 / 6 | 8.6% / 33% / 78% | 12 |
| 13 | `B2 F2 D L2 D R2 F2 R2 D B2 U L2 U2` | 4e | 1 | 0c0-1 / 0c0-1 | 7 / 7 | 0.78% / 8.3% / 40% | 13 |
| 14 | `B2 U B2 F2 D' F2 D' U F2 U2` | 4e | 2 | 0c0-1 / 0c0-1 | 7 / 5 | 5.0% / 20% / 57% | 10 |
| 15 | `B2 U' L2 R2 U R2 D' B2 L2 F2 L2 R2 D2 U'` | 6e | 2 | 0c0-1 / 0c0-1 | 8 / 8 | 1.1% / 7.4% / 32% | 14 |
| 16 | `D' L2 R2 D' U2 B2 R2 F2 L2 F2 D2` | 4e | 3 | 0c0-1 / 0c0-1 | 6 / 4 | 13% / 37% / 77% | 11 |
| 17 | `R2 D' B2 U B2 L2 F2 U F2 U'` | 2e | 2 | 0c0-1 / 0c0-1 | 6 / 5 | 9.4% / 36% / 80% | 10 |
| 18 | `F2 U' F2 D L2 R2 D' R2 U R2 F2 R2` | 2e | 3 | 0c0-1 / 0c0-1 | 5 / 5 | 14% / 44% / 84% | 12 |
| 19 | `L2 F2 U' F2 R2 F2 D' B2 R2 U2 R2 U2 R2` | 2e | 3 | 0c0-1 / 0c0-1 | 5 / 6 | 12% / 38% / 81% | 13 |
| 20 | `D F2 D2 F2 R2 F2 D' U' F2 U' R2 U2` | 4e | 3 | 0c0-1 / 0c0-1 | 6 / 7 | 3.8% / 20% / 59% | 12 |
| 21 | `D2 L2 F2 D L2 U R2 B2 L2 U F2 R2 U` | 6e | 2 | 0c0-1 / 0c0-1 | 7 / 7 | 2.6% / 10% / 36% | 13 |
| 22 | `F2 D L2 D L2 R2 U' R2 U' L2 D2 R2 U2` | 4e | 2 | 0c0-1 / 0c0-1 | 6 / 4 | 10% / 36% / 70% | 13 |
| 23 | `D L2 R2 U' L2 U R2 U2 B2 R2 D2 F2 U'` | 6e | 1 | 0c0-1 / 0c0-1 | 8 / 8 | 0.58% / 4.7% / 27% | 13 |
| 24 | `D U L2 D B2 L2 B2 D' B2 U2 B2 L2 U2` | 2e | 4 | 0c0-1 / 0c0-1 | 6 / 6 | 8.7% / 34% / 77% | 13 |
| 25 | `R2 B2 U F2 D R2 B2 R2 U R2 F2 D` | 4e | 4 | 0c0-1 / 0c0-1 | 6 / 5 | 8.8% / 24% / 61% | 12 |

How the 25 came out: 2 in 10 or less, 5 in 11 or less, 13 in 12 or less, 24 in 13 or less. All of 0c0 is 6.1% / 21% / 54% / 90% (in 10 / 11 / 12 / 13), which for 25 DRs is about 1.5, 5.1, 13.4 and 22.5.

### 4a1

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 4a1-1 | 4-0 | 1–4 | 0c0 |
| 4a1-2 | 2-2, pairs on opposite sides | 2–5 | nothing, needs a setup |
| 4a1-3 | 2-2, pairs stacked | 3–6 | nothing, needs a setup |
| 4a1-4 | 2-2, diagonal over diagonal | 4–7 | nothing, needs a setup |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `D L2 U R2 D B2 L2 F2 U B2 U L2` | 2e | 1 | 4a1-2 / 4a1-1 | 7 / 6 | 1.1% / 7.4% / 37% | 12 |
| 2 | `R2 U' F2 R2 B2 U B2 D2 L2 U' F2 L2 U2 R2` | 2e | 2 | 4a1-4 / 4a1-3 | 8 / 7 | 0.38% / 3.5% / 23% | 14 |
| 3 | `F2 L2 R2 D' F2 L2 U R2 F2 R2 D'` | 2e | 1 | 4a1-3 / 4a1-2 | 8 / 7 | 0.49% / 4.5% / 27% | 11 |
| 4 | `R2 B2 L2 R2 U' R2 F2 D2 U2 L2 F2 U2` | 4e | 1 | 4a1-3 / 4a1-2 | 6 / 5 | 2.3% / 16% / 60% | 12 |
| 5 | `U' F2 R2 B2 D R2 U2 L2 B2 R2 F2 D'` | 4e | 3 | 4a1-1 / 4a1-2 | 4 / 7 | 10% / 36% / 83% | 12 |
| 6 | `U2 F2 D' F2 U2 B2 L2 U L2 F2 R2 U` | 2e | 2 | 4a1-4 / 4a1-3 | 7 / 6 | 0.89% / 8.4% / 41% | 12 |
| 7 | `U B2 D F2 L2 D' L2 R2 B2 U' B2 R2 D'` | 2e | 2 | 4a1-3 / 4a1-2 | 7 / 7 | 0.99% / 7.9% / 37% | 13 |
| 8 | `B2 U2 L2 D R2 F2 L2 U F2 U' F2 D2 F2` | 4e | 2 | 4a1-3 / 4a1-2 | 7 / 7 | 1.4% / 10% / 41% | 13 |
| 9 | `D' L2 D' B2 U' L2 D F2 L2 R2 D2 B2 U'` | 4e | 2 | 4a1-3 / 4a1-2 | 6 / 8 | 0.58% / 4.6% / 23% | 13 |
| 10 | `D B2 F2 D' F2 R2 B2 L2 R2 U' B2 D2 R2` | 2e | 0 | 4a1-4 / 4a1-1 | 8 / 8 | 0 / 1.3% / 13% | 13 |
| 11 | `B2 D2 F2 D L2 R2 D2 U' F2 L2 U2 L2 U` | 4e | 1 | 4a1-1 / 4a1-2 | 7 / 6 | 1.2% / 7.1% / 34% | 13 |
| 12 | `D' R2 U2 B2 U L2 B2 R2 D' F2 U2` | 4e | 3 | 4a1-2 / 4a1-1 | 6 / 5 | 4.1% / 23% / 71% | 11 |
| 13 | `U' F2 L2 F2 U' F2 D' R2 D' B2 F2 U'` | 2e | 1 | 4a1-3 / 4a1-2 | 8 / 7 | 0.49% / 4.5% / 27% | 12 |
| 14 | `U R2 F2 U B2 R2 D' F2 U' R2 U L2 B2` | 4e | 1 | 4a1-3 / 4a1-3 | 7 / 7 | 0.42% / 4.4% / 26% | 13 |
| 15 | `B2 L2 D2 R2 F2 D' L2 B2 R2 F2 U2 R2` | 4e | 1 | 4a1-4 / 4a1-3 | 7 / 4 | 2.2% / 15% / 54% | 12 |
| 16 | `U2 F2 D2 F2 R2 F2 L2 U' B2 R2 F2 R2 U2` | 4e | 2 | 4a1-3 / 4a1-2 | 6 / 6 | 0.83% / 9.7% / 47% | 13 |
| 17 | `R2 U L2 D' L2 D' L2 U' L2 F2 D' U2` | 2e | 2 | 4a1-2 / 4a1-4 | 7 / 8 | 0.85% / 6.6% / 33% | 12 |
| 18 | `F2 L2 R2 D' U2 B2 D' B2 F2 U' F2 L2 F2` | 2e | 2 | 4a1-3 / 4a1-2 | 7 / 7 | 0.99% / 7.9% / 37% | 13 |
| 19 | `D' B2 U' L2 R2 U' L2 U2 L2 U2 B2 R2 U2` | 2e | 4 | 4a1-3 / 4a1-1 | 7 / 6 | 5.5% / 24% / 67% | 13 |
| 20 | `F2 L2 U2 R2 D F2 R2 B2 D L2 D2 U'` | 2e | 2 | 4a1-1 / 4a1-2 | 7 / 7 | 4.7% / 22% / 66% | 12 |
| 21 | `L2 U' L2 D' F2 L2 F2 U' R2 D2 L2 R2 F2` | 2e | 1 | 4a1-2 / 4a1-2 | 7 / 6 | 2.2% / 13% / 47% | 13 |
| 22 | `L2 U2 F2 D2 U R2 B2 U' B2 L2 B2 D R2` | 2e | 1 | 4a1-3 / 4a1-4 | 7 / 7 | 0.63% / 4.6% / 24% | 13 |
| 23 | `L2 F2 D2 R2 U2 R2 F2 D L2 U L2 F2 L2 D'` | 4e | 2 | 4a1-3 / 4a1-3 | 7 / 7 | 1.1% / 5.9% / 31% | 14 |
| 24 | `F2 L2 D' F2 D2 U2 F2 R2 U2 R2` | 4e | 1 | 4a1-3 / 4a1-2 | 5 / 3 | 36% / 63% / 93% | 10 |
| 25 | `B2 D2 B2 U L2 R2 U' L2 F2 D' F2` | 4e | 3 | 4a1-2 / 4a1-4 | 6 / 4 | 12% / 40% / 88% | 11 |

How the 25 came out: 1 in 10 or less, 4 in 11 or less, 12 in 12 or less, 23 in 13 or less. All of 4a1 is 4.4% / 16% / 47% / 89% (in 10 / 11 / 12 / 13), which for 25 DRs is about 1.1, 4.0, 11.8 and 22.3.

### 4a2

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 4a2-1 | 2-2, diagonal over diagonal | 5–8 | 4a1 |
| 4a2-2 | 2-2, pairs stacked | 6–9 | nothing, needs a setup |
| 4a2-3 | 2-2, pairs on opposite sides | 7–10 | nothing, needs a setup |
| 4a2-4 | 4-0 | 8–11 | nothing, needs a setup |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `F2 U2 R2 U' F2 R2 F2 R2 U2 B2 D B2 L2 D2` | 2e | 0 | 4a2-3 / 4a2-4 | 10 / 11 | 0 / 0 / 0.09% | 14 |
| 2 | `D' L2 R2 U' L2 D' B2 D2 R2 U R2 F2 U2 L2` | 2e | 2 | 4a2-3 / 4a2-3 | 10 / 10 | 0 / 0.06% / 1.4% | 14 |
| 3 | `L2 B2 U2 F2 D R2 U2 F2 R2 F2 R2 U' F2 U2` | 2e | 0 | 4a2-3 / 4a2-4 | 10 / 11 | 0 / 0 / 0.09% | 14 |
| 4 | `U' L2 U2 B2 U R2 U B2 U2 L2 U' R2 B2 U2` | 4e | 1 | 4a2-4 / 4a2-3 | 9 / 7 | 0 / 2.7% / 12% | 14 |
| 5 | `U R2 U' L2 U' L2 B2 U F2 D' F2 D' L2` | 4e | 2 | 4a2-2 / 4a2-3 | 6 / 8 | 4.4% / 20% / 53% | 13 |
| 6 | `R2 F2 D2 U R2 B2 U2 B2 D R2 B2 U2 F2` | 4e | 2 | 4a2-4 / 4a2-2 | 10 / 7 | 0 / 0 / 20% | 13 |
| 7 | `B2 D L2 B2 D2 L2 B2 U' R2 D R2 B2 R2 U'` | 2e | 2 | 4a2-3 / 4a2-2 | 10 / 9 | 0 / 0.61% / 7.0% | 14 |
| 8 | `U2 L2 R2 B2 R2 U F2 L2 D' U' F2 U L2` | 4e | 1 | 4a2-2 / 4a2-3 | 7 / 7 | 1.5% / 12% / 39% | 13 |
| 9 | `U2 L2 B2 U' F2 U2 R2 U' R2 F2 L2 F2 D' U'` | 4e | 4 | 4a2-3 / 4a2-3 | 10 / 8 | 0 / 0.37% / 3.2% | 14 |
| 10 | `D' F2 L2 U2 R2 D' F2 L2 R2 U F2 U2 L2 U'` | 2e | 1 | 4a2-3 / 4a2-3 | 10 / 10 | 0 / 0.01% / 0.84% | 14 |
| 11 | `B2 F2 D2 F2 R2 B2 L2 D B2 U2 R2 U L2 D' U'` | 4e | 1 | 4a2-3 / 4a2-3 | 7 / 10 | 0 / 0 / 4.5% | 15 |
| 12 | `D2 R2 D2 U' F2 L2 U' L2 R2 U' L2 F2 U' L2 U2` | 4e | 1 | 4a2-3 / 4a2-3 | 10 / 8 | 0 / 0 / 0.32% | 15 |
| 13 | `R2 D2 F2 U L2 D2 L2 B2 D' L2 D' L2 R2 U` | 2e | 0 | 4a2-2 / 4a2-4 | 9 / 11 | 0 / 0 / 1.7% | 14 |
| 14 | `F2 U2 L2 U L2 B2 U2 B2 D' L2 F2 R2 F2 U2` | 4e | 3 | 4a2-3 / 4a2-4 | 9 / 8 | 0 / 0 / 10% | 14 |
| 15 | `F2 U' R2 D L2 U B2 U L2 D' L2 U L2` | 4e | 2 | 4a2-2 / 4a2-4 | 9 / 8 | 0 / 0 / 8.4% | 13 |
| 16 | `U F2 D' R2 U F2 D L2 B2 U F2 U R2 U2` | 4e | 1 | 4a2-3 / 4a2-3 | 10 / 8 | 0 / 0 / 0.32% | 14 |
| 17 | `B2 L2 D F2 D2 R2 U' F2 U2 R2 U B2 F2 U'` | 2e | 1 | 4a2-4 / 4a2-2 | 11 / 9 | 0 / 0 / 2.0% | 14 |
| 18 | `B2 F2 U R2 D2 B2 U R2 D B2 R2 B2 U` | 2e | 1 | 4a2-2 / 4a2-1 | 9 / 8 | 0.56% / 3.7% / 19% | 13 |
| 19 | `F2 L2 F2 U F2 D2 B2 L2 D' B2 U2 R2 U2` | 4e | 1 | 4a2-4 / 4a2-1 | 8 / 8 | 0 / 2.2% / 15% | 13 |
| 20 | `D2 B2 L2 F2 U L2 R2 B2 U2 R2 U` | 4e | 4 | 4a2-1 / 4a2-1 | 5 / 8 | 15% / 51% / 87% | 11 |
| 21 | `U2 F2 D2 U F2 U2 R2 U' F2 R2 U L2 F2 R2 U` | 4e | 1 | 4a2-2 / 4a2-3 | 7 / 8 | 1.2% / 7.0% / 33% | 15 |
| 22 | `D R2 U' L2 B2 D' B2 U' F2 U F2 U` | 2e | 2 | 4a2-2 / 4a2-3 | 9 / 10 | 0 / 0.61% / 7.0% | 12 |
| 23 | `F2 L2 U2 F2 R2 U' L2 F2 U2 F2 U' L2 B2` | 4e | 3 | 4a2-2 / 4a2-4 | 8 / 10 | 0 / 0 / 0.76% | 13 |
| 24 | `R2 B2 U' R2 U B2 L2 D B2 R2 D' R2 U F2 U'` | 2e | 1 | 4a2-3 / 4a2-4 | 10 / 11 | 0 / 0 / 0.09% | 15 |
| 25 | `D2 L2 B2 U B2 L2 F2 L2 U2 B2 D' F2 D' U'` | 2e | 4 | 4a2-3 / 4a2-3 | 10 / 10 | 0 / 0.09% / 2.5% | 14 |

How the 25 came out: 0 in 10 or less, 1 in 11 or less, 2 in 12 or less, 9 in 13 or less. All of 4a2 is 1.1% / 4.8% / 18% / 52% (in 10 / 11 / 12 / 13), which for 25 DRs is about 0.3, 1.2, 4.6 and 12.9.

### 4b2

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 4b2-1 | 2-2, pairs sharing one column | 3–6 | 4a1 |
| 4b2-2 | 3-1 | 4–7 | nothing, needs a setup |
| 4b2-3 | 3-1 | 5–8 | nothing, needs a setup |
| 4b2-4 | 2-2, pairs sharing one column | 6–9 | nothing, needs a setup |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `L2 D2 R2 D2 R2 B2 R2 B2 U' R2 D' U2` | 2e | 1 | 4b2-1 / 4b2-1 | 3 / 5 | 12% / 47% / 87% | 12 |
| 2 | `D2 L2 R2 U R2 D B2 D B2 L2 D' B2` | 4e | 3 | 4b2-2 / 4b2-3 | 5 / 9 | 3.3% / 22% / 68% | 12 |
| 3 | `U' F2 D2 L2 B2 U B2 R2 D L2 B2 L2 U'` | 4e | 2 | 4b2-3 / 4b2-1 | 8 / 6 | 1.6% / 10% / 43% | 13 |
| 4 | `D' R2 D R2 B2 F2 U F2 D' L2 D2 R2 D2` | 4e | 1 | 4b2-2 / 4b2-3 | 7 / 8 | 0.33% / 3.9% / 24% | 13 |
| 5 | `D R2 B2 F2 D' L2 R2 F2 U' L2 D L2 D2` | 2e | 0 | 4b2-4 / 4b2-3 | 8 / 7 | 0.01% / 0.45% / 7.9% | 13 |
| 6 | `R2 F2 D2 L2 B2 D L2 D' L2 R2 U F2 U` | 4e | 3 | 4b2-1 / 4b2-4 | 7 / 7 | 2.2% / 16% / 53% | 13 |
| 7 | `U2 R2 D2 U L2 B2 R2 B2 R2 D' F2 L2 U2` | 2e | 1 | 4b2-3 / 4b2-3 | 7 / 6 | 0.36% / 3.8% / 23% | 13 |
| 8 | `F2 D B2 U' L2 R2 D' F2 L2 B2 D' L2` | 2e | 2 | 4b2-2 / 4b2-2 | 6 / 6 | 1.5% / 8.1% / 32% | 12 |
| 9 | `U2 B2 R2 D' B2 L2 D B2 F2 U2 L2 F2` | 4e | 1 | 4b2-2 / 4b2-3 | 6 / 7 | 1.9% / 11% / 41% | 12 |
| 10 | `B2 U' L2 R2 F2 U' B2 L2 U F2 R2 B2 U` | 2e | 1 | 4b2-2 / 4b2-2 | 5 / 4 | 4.2% / 18% / 59% | 13 |
| 11 | `F2 D2 L2 F2 U2 L2 F2 U' R2 D B2 D' U'` | 2e | 1 | 4b2-3 / 4b2-3 | 5 / 7 | 1.6% / 9.8% / 39% | 13 |
| 12 | `B2 L2 B2 F2 U2 L2 D L2 U R2 F2 U2` | 2e | 2 | 4b2-3 / 4b2-4 | 6 / 6 | 1.8% / 8.8% / 36% | 12 |
| 13 | `B2 D F2 L2 B2 R2 D' R2 U2 F2 D2 B2 L2` | 0e | 1 | 4b2-3 / 4b2-2 | 8 / 7 | 0.70% / 4.6% / 22% | 13 |
| 14 | `B2 F2 L2 B2 U B2 L2 U B2 R2 D U` | 4e | 3 | 4b2-3 / 4b2-2 | 7 / 5 | 7.9% / 27% / 69% | 12 |
| 15 | `F2 U2 F2 L2 D2 F2 L2 D' F2 L2 B2 R2 U` | 0e | 3 | 4b2-1 / 4b2-3 | 6 / 8 | 3.5% / 14% / 42% | 13 |
| 16 | `L2 D2 B2 F2 D B2 D' L2 F2 L2 B2 D2 U2` | 2e | 1 | 4b2-2 / 4b2-2 | 7 / 5 | 1.7% / 8.9% / 38% | 13 |
| 17 | `B2 R2 D' L2 B2 D' R2 U' R2 B2 D F2 U2` | 4e | 2 | 4b2-3 / 4b2-4 | 8 / 8 | 0.26% / 2.1% / 17% | 13 |
| 18 | `R2 D' L2 F2 D L2 D F2 U2 B2 F2 U` | 4e | 1 | 4b2-3 / 4b2-1 | 6 / 8 | 0.87% / 7.1% / 35% | 12 |
| 19 | `D B2 R2 D U R2 D F2 L2 F2 L2 R2` | 4e | 1 | 4b2-1 / 4b2-1 | 7 / 6 | 1.9% / 11% / 39% | 12 |
| 20 | `L2 F2 U' L2 B2 U F2 L2 U2 R2 D' F2 U` | 2e | 3 | 4b2-4 / 4b2-3 | 7 / 6 | 0.63% / 6.4% / 32% | 13 |
| 21 | `U L2 U' B2 F2 L2 D2 L2 U' B2 U L2 B2` | 2e | 1 | 4b2-1 / 4b2-2 | 6 / 6 | 1.3% / 8.0% / 35% | 13 |
| 22 | `D2 L2 F2 D2 U' B2 R2 D F2 L2 B2` | 4e | 3 | 4b2-1 / 4b2-3 | 7 / 7 | 1.9% / 11% / 48% | 11 |
| 23 | `L2 U' B2 L2 U' B2 D2 R2 B2 U B2 D L2` | 2e | 1 | 4b2-4 / 4b2-1 | 8 / 6 | 0.16% / 3.3% / 23% | 13 |
| 24 | `U' F2 U B2 U' B2 L2 F2 D B2 L2 U2` | 4e | 2 | 4b2-2 / 4b2-1 | 7 / 4 | 8.9% / 34% / 77% | 12 |
| 25 | `B2 F2 L2 D R2 D F2 L2 B2 D B2 U2 R2 U'` | 4e | 3 | 4b2-1 / 4b2-2 | 7 / 8 | 1.7% / 12% / 46% | 14 |

How the 25 came out: 0 in 10 or less, 1 in 11 or less, 10 in 12 or less, 24 in 13 or less. All of 4b2 is 2.2% / 10% / 36% / 83% (in 10 / 11 / 12 / 13), which for 25 DRs is about 0.6, 2.5, 9.1 and 20.8.

### 2c3

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 2c3-1 | 1 up 1 down, stacked | 5–8 | 4b2 |
| 2c3-2 | 1 up 1 down, opposite | 5–8 | 4b2 |
| 2c3-3 | both on one layer, adjacent | 6–9 | nothing, needs a setup |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `L2 D2 R2 F2 D L2 U2 L2 D L2 D' F2 L2` | 4e | 0 | 2c3-1 / 2c3-3 | 7 / 8 | 0.22% / 2.5% / 18% | 13 |
| 2 | `D2 L2 U2 R2 F2 R2 U B2 F2 L2 U F2 D` | 6e | 1 | 2c3-1 / 2c3-3 | 7 / 9 | 0.31% / 3.0% / 19% | 13 |
| 3 | `R2 D B2 U' L2 F2 D L2 D B2 D2 L2 U` | 4e | 2 | 2c3-1 / 2c3-2 | 7 / 8 | 0.99% / 6.7% / 31% | 13 |
| 4 | `B2 F2 U L2 U' L2 B2 R2 U2 B2 D F2 L2` | 4e | 1 | 2c3-3 / 2c3-1 | 7 / 7 | 0.57% / 4.4% / 24% | 13 |
| 5 | `D' L2 U' L2 F2 R2 F2 R2 U' R2 U2 L2 F2 U2` | 6e | 1 | 2c3-3 / 2c3-1 | 8 / 8 | 0.32% / 2.5% / 17% | 14 |
| 6 | `U2 B2 D' B2 U' F2 D' F2 U F2 U' L2 R2` | 2e | 4 | 2c3-2 / 2c3-3 | 6 / 7 | 2.8% / 13% / 46% | 13 |
| 7 | `B2 D2 B2 U L2 D F2 U' B2 U L2 F2 R2 U'` | 0e | 1 | 2c3-3 / 2c3-3 | 10 / 10 | 0 / 0.10% / 1.3% | 14 |
| 8 | `B2 U' B2 D' R2 F2 D F2 R2 U F2 R2 U` | 4e | 3 | 2c3-2 / 2c3-2 | 8 / 6 | 2.1% / 11% / 40% | 13 |
| 9 | `B2 U' B2 D F2 L2 B2 R2 D' L2 D2 F2 L2 U2` | 4e | 1 | 2c3-3 / 2c3-3 | 7 / 8 | 0.17% / 1.7% / 11% | 14 |
| 10 | `F2 L2 F2 D2 B2 R2 D' R2 B2 D' B2 U'` | 2e | 5 | 2c3-1 / 2c3-3 | 6 / 6 | 9.2% / 30% / 72% | 12 |
| 11 | `L2 F2 D F2 U' B2 R2 D2 L2 F2 D B2` | 4e | 3 | 2c3-3 / 2c3-1 | 6 / 8 | 2.3% / 11% / 42% | 12 |
| 12 | `F2 D L2 B2 L2 F2 D B2 U F2 D2` | 6e | 1 | 2c3-2 / 2c3-3 | 7 / 8 | 0.41% / 2.9% / 16% | 11 |
| 13 | `D2 F2 U L2 R2 D L2 B2 U' F2 D B2 R2 U'` | 4e | 5 | 2c3-1 / 2c3-1 | 7 / 7 | 6.8% / 25% / 64% | 14 |
| 14 | `F2 U R2 U' B2 D2 L2 B2 U' L2 R2 D2` | 4e | 4 | 2c3-1 / 2c3-1 | 6 / 6 | 8.0% / 27% / 67% | 12 |
| 15 | `R2 U' R2 U2 R2 U F2 D L2 D B2 U' B2` | 2e | 3 | 2c3-3 / 2c3-3 | 7 / 7 | 0.97% / 5.7% / 28% | 13 |
| 16 | `F2 R2 B2 R2 D2 U F2 L2 D L2 B2 U'` | 6e | 3 | 2c3-1 / 2c3-1 | 7 / 8 | 3.9% / 16% / 53% | 12 |
| 17 | `D' R2 U F2 L2 R2 U' L2 R2 F2 U' L2 D2 U'` | 4e | 1 | 2c3-3 / 2c3-2 | 8 / 7 | 0.24% / 2.2% / 15% | 14 |
| 18 | `D' F2 D2 F2 R2 B2 D B2 U' L2 U2 L2 D2` | 2e | 3 | 2c3-3 / 2c3-2 | 7 / 6 | 1.9% / 9.9% / 40% | 13 |
| 19 | `L2 D' B2 D' B2 L2 B2 F2 D2 L2 F2 L2 D'` | 4e | 2 | 2c3-2 / 2c3-1 | 7 / 6 | 1.9% / 10% / 40% | 13 |
| 20 | `F2 L2 F2 U' L2 D2 F2 D2 F2 D L2 U F2` | 4e | 1 | 2c3-3 / 2c3-2 | 8 / 8 | 0.12% / 1.7% / 13% | 13 |
| 21 | `L2 U' B2 L2 R2 U B2 U L2 D' U L2` | 4e | 1 | 2c3-1 / 2c3-3 | 7 / 8 | 0.37% / 3.3% / 21% | 12 |
| 22 | `R2 U2 F2 D' F2 L2 D' L2 B2 U' R2` | 2e | 2 | 2c3-3 / 2c3-3 | 7 / 7 | 0.55% / 4.3% / 24% | 11 |
| 23 | `U2 F2 L2 D L2 F2 D' B2 L2 R2 U B2 R2` | 6e | 2 | 2c3-3 / 2c3-2 | 8 / 7 | 0.65% / 3.7% / 19% | 13 |
| 24 | `F2 U R2 U' B2 U F2 D2 R2 U B2 L2 F2 D'` | 4e | 0 | 2c3-3 / 2c3-3 | 8 / 8 | 0.03% / 0.58% / 6.0% | 14 |
| 25 | `U2 B2 U2 B2 R2 U B2 D B2 F2 L2 F2 D'` | 4e | 1 | 2c3-1 / 2c3-3 | 7 / 8 | 0.37% / 3.3% / 21% | 13 |

How the 25 came out: 0 in 10 or less, 2 in 11 or less, 7 in 12 or less, 19 in 13 or less. All of 2c3 is 1.3% / 6.7% / 28% / 73% (in 10 / 11 / 12 / 13), which for 25 DRs is about 0.3, 1.7, 6.9 and 18.2.

### 4c3

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 4c3-1 (4a3) | 2-2, pairs on opposite sides | 7–9 | 4b2 |
| 4c3-2 (4a3) | 2-2, pairs stacked | 7–9 | 4b2 |
| 4c3-3 (4a3) | 4-0 | 8–9 | nothing, needs a setup |
| 4c3-4 (4b3) | 2-2, pairs sharing one column | 7–10 | 4a2 |
| 4c3-5 (4b3) | 3-1 | 8–11 | nothing, needs a setup |
| 4c3-6 (4a3) | 2-2, diagonal over diagonal | 8–10 | nothing, needs a setup |
| 4c3-7 (4a3) | 2-2, pairs stacked | 8–10 | nothing, needs a setup |
| 4c3-8 (4a3) | 4-0 | 9–10 | nothing, needs a setup |
| 4c3-9 (4a3) | 2-2, pairs on opposite sides | 9–11 | nothing, needs a setup |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `D' R2 F2 D' R2 U R2 U2 R2 B2 U' L2 U F2` | 2e | 1 | 4c3-4 / 4c3-8 | 7 / 9 | 0 / 1.4% / 11% | 14 |
| 2 | `D2 U' F2 U2 F2 R2 U' L2 U' L2 B2 F2` | 2e | 3 | 4c3-5 / 4c3-1 | 9 / 7 | 0.92% / 6.5% / 30% | 12 |
| 3 | `D' L2 D2 B2 R2 B2 L2 D' B2 U B2 U2` | 4e | 1 | 4c3-5 / 4c3-2 | 10 / 7 | 0.39% / 2.6% / 15% | 12 |
| 4 | `U2 L2 D' B2 D L2 R2 U R2 D L2 B2 F2 U` | 4e | 0 | 4c3-4 / 4c3-9 | 10 / 11 | 0 / 0 / 0 | 14 |
| 5 | `L2 D' R2 U F2 L2 U' L2 U R2 U' F2 L2` | 4e | 2 | 4c3-6 / 4c3-4 | 8 / 10 | 0.06% / 1.4% / 9.9% | 13 |
| 6 | `D2 F2 D' L2 B2 U F2 L2 D2 B2 L2 U R2` | 2e | 1 | 4c3-3 / 4c3-5 | 8 / 9 | 0.07% / 1.5% / 11% | 13 |
| 7 | `D2 R2 D' L2 B2 U' F2 D' R2 D L2 U' F2 R2` | 2e | 0 | 4c3-7 / 4c3-5 | 9 / 9 | 0.01% / 0.43% / 4.7% | 14 |
| 8 | `R2 U' F2 U F2 R2 F2 L2 F2 D' B2 U' B2 U` | 2e | 1 | 4c3-5 / 4c3-6 | 9 / 8 | 0.05% / 0.69% / 6.2% | 14 |
| 9 | `L2 U R2 F2 D2 L2 D' F2 D2 L2 D' R2` | 4e | 2 | 4c3-6 / 4c3-5 | 9 / 9 | 0.06% / 1.1% / 8.1% | 12 |
| 10 | `D2 F2 D' B2 U F2 R2 D L2 F2 U' L2 U'` | 4e | 1 | 4c3-5 / 4c3-6 | 9 / 9 | 0.07% / 0.94% / 6.3% | 13 |
| 11 | `R2 F2 U L2 U L2 U2 R2 F2 D L2 B2 D2 L2` | 2e | 2 | 4c3-8 / 4c3-5 | 10 / 9 | 0 / 0.08% / 2.2% | 14 |
| 12 | `F2 D2 B2 D B2 D' B2 U' F2 D B2 D' R2 U2` | 4e | 1 | 4c3-9 / 4c3-5 | 10 / 10 | 0 / 0 / 0.18% | 14 |
| 13 | `R2 D B2 U R2 D L2 U2 L2 U R2 U` | 2e | 2 | 4c3-5 / 4c3-3 | 9 / 9 | 0.06% / 1.2% / 11% | 12 |
| 14 | `U L2 B2 U2 B2 U B2 D' R2 B2 U2 F2 R2 B2` | 2e | 2 | 4c3-5 / 4c3-2 | 9 / 7 | 0.77% / 3.9% / 19% | 14 |
| 15 | `B2 D2 B2 U' F2 D R2 D2 F2 U B2 U2 L2 R2` | 4e | 0 | 4c3-8 / 4c3-5 | 11 / 9 | 0 / 0 / 0.58% | 14 |
| 16 | `F2 L2 U F2 U' B2 D2 F2 L2 D U2 B2 R2 U2` | 4e | 0 | 4c3-9 / 4c3-5 | 10 / 9 | 0 / 0.05% / 1.3% | 14 |
| 17 | `U B2 L2 R2 U' L2 B2 U2 L2 B2 U L2 B2` | 2e | 0 | 4c3-7 / 4c3-4 | 9 / 8 | 0.19% / 1.8% / 10% | 13 |
| 18 | `U' L2 F2 U2 R2 U B2 R2 U2 R2 U R2 U2` | 4e | 2 | 4c3-2 / 4c3-4 | 9 / 10 | 0.10% / 1.3% / 9.2% | 13 |
| 19 | `U' L2 R2 D2 F2 D' L2 D2 L2 R2 F2 U' B2` | 2e | 0 | 4c3-3 / 4c3-4 | 8 / 7 | 0 / 1.3% / 16% | 13 |
| 20 | `F2 D' L2 D' R2 F2 U' F2 L2 U F2 U B2 D2` | 4e | 2 | 4c3-4 / 4c3-3 | 10 / 9 | 0 / 1.1% / 10% | 14 |
| 21 | `U' B2 U2 F2 U R2 U F2 L2 R2 D F2 U'` | 4e | 0 | 4c3-5 / 4c3-2 | 10 / 9 | 0 / 0.37% / 4.8% | 13 |
| 22 | `F2 D R2 U2 L2 B2 L2 F2 U' L2 D2 B2 D` | 4e | 1 | 4c3-1 / 4c3-5 | 7 / 8 | 1.5% / 8.7% / 35% | 13 |
| 23 | `F2 R2 F2 D' R2 U B2 L2 D2 R2 U' L2 D' U'` | 4e | 0 | 4c3-2 / 4c3-4 | 8 / 10 | 0 / 0.93% / 7.8% | 14 |
| 24 | `F2 U' L2 F2 U' B2 D' L2 R2 B2 U2 R2 D' B2 U'` | 4e | 0 | 4c3-5 / 4c3-9 | 9 / 10 | 0 / 0.05% / 1.3% | 15 |
| 25 | `F2 U' L2 U F2 D2 L2 U' F2 U2 F2 L2 U2` | 4e | 3 | 4c3-7 / 4c3-5 | 10 / 8 | 0 / 1.2% / 12% | 13 |

How the 25 came out: 0 in 10 or less, 0 in 11 or less, 4 in 12 or less, 13 in 13 or less. All of 4c3 is 0.36% / 2.3% / 12% / 46% (in 10 / 11 / 12 / 13), which for 25 DRs is about 0.1, 0.6, 3.0 and 11.5.

### 0c3

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 0c3-1 | none bad | 9–12 | 4a2 |
| 0c3-2 | none bad | 10–12 | nothing, needs a setup |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `L2 U2 R2 U' B2 D2 F2 R2 U L2 U2 F2 U' R2` | 6e | 2 | 0c3-2 / 0c3-2 | 10 / 10 | 0 / 0.34% / 3.4% | 14 |
| 2 | `U L2 U' L2 R2 U' B2 R2 U R2 D2 F2 U' R2` | 4e | 3 | 0c3-2 / 0c3-1 | 12 / 11 | 0 / 0 / 0 | 14 |
| 3 | `R2 U B2 D B2 D2 R2 U' L2 D F2 D2 R2 U'` | 6e | 0 | 0c3-2 / 0c3-2 | 10 / 10 | 0 / 0.07% / 1.3% | 14 |
| 4 | `D2 B2 D' R2 U2 L2 B2 U' R2 U2 B2 U B2 U2` | 2e | 6 | 0c3-2 / 0c3-2 | 10 / 10 | 0 / 0.57% / 4.4% | 14 |
| 5 | `D' R2 U2 B2 D' R2 F2 R2 B2 D2 R2 U` | 4e | 2 | 0c3-1 / 0c3-1 | 11 / 12 | 0 / 0 / 7.1% | 12 |
| 6 | `F2 D2 B2 U B2 R2 U2 R2 D L2 F2 U2 B2 U B2` | 4e | 2 | 0c3-2 / 0c3-2 | 12 / 11 | 0 / 0 / 0 | 15 |
| 7 | `U' L2 U2 B2 D B2 D' B2 U2 R2 U R2 F2 U` | 4e | 2 | 0c3-1 / 0c3-2 | 10 / 12 | 0 / 0 / 5.8% | 14 |
| 8 | `F2 D' U' L2 U R2 U2 R2 F2 U F2 U2 F2 L2 U'` | 4e | 2 | 0c3-1 / 0c3-2 | 10 / 12 | 0 / 0 / 5.8% | 15 |
| 9 | `F2 U B2 D2 L2 D R2 U2 B2 R2 B2 R2 U' F2 R2` | 6e | 1 | 0c3-2 / 0c3-2 | 10 / 10 | 0 / 0.13% / 1.9% | 15 |
| 10 | `U F2 D' U' L2 B2 U B2 R2 U2 R2 U' R2` | 6e | 1 | 0c3-2 / 0c3-1 | 10 / 9 | 0.19% / 1.8% / 8.1% | 13 |
| 11 | `L2 D B2 U' F2 D B2 D2 L2 U' L2 U' B2 U R2 U` | 6e | 0 | 0c3-2 / 0c3-2 | 10 / 10 | 0 / 0.07% / 1.3% | 16 |
| 12 | `U' R2 D' R2 F2 R2 U B2 U B2 D2 F2 L2 D' R2` | 2e | 2 | 0c3-2 / 0c3-1 | 10 / 11 | 0 / 0 / 0.18% | 15 |
| 13 | `U' F2 U L2 F2 R2 D' F2 D' L2 D2 B2 U'` | 4e | 3 | 0c3-1 / 0c3-1 | 12 / 12 | 0 / 0 / 0.32% | 13 |
| 14 | `B2 D R2 D2 F2 U' F2 U2 R2 U' R2 B2 L2 B2 R2 U2` | 6e | 1 | 0c3-2 / 0c3-2 | 10 / 10 | 0 / 0.13% / 1.9% | 16 |
| 15 | `F2 D L2 D2 R2 B2 U L2 F2 U2 B2 D L2 U2` | 6e | 1 | 0c3-2 / 0c3-2 | 10 / 10 | 0 / 0.13% / 1.9% | 14 |
| 16 | `D' B2 L2 D2 L2 D' L2 B2 U2 F2 D F2 R2 U2` | 4e | 4 | 0c3-2 / 0c3-1 | 11 / 10 | 0 / 2.0% / 6.9% | 14 |
| 17 | `R2 U F2 R2 D2 L2 D B2 R2 U2 L2 D' R2 U2` | 4e | 1 | 0c3-2 / 0c3-2 | 11 / 11 | 0 / 0 / 2.5% | 14 |
| 18 | `U' B2 U2 R2 U L2 U F2 L2 F2 U' R2 U' F2 U2` | 4e | 4 | 0c3-2 / 0c3-1 | 12 / 10 | 0 / 0 / 7.8% | 15 |
| 19 | `L2 B2 D2 L2 U R2 U2 F2 D R2 U2 F2 U R2` | 6e | 1 | 0c3-2 / 0c3-2 | 10 / 10 | 0 / 0.13% / 1.9% | 14 |
| 20 | `D R2 B2 U2 F2 U B2 L2 R2 U2 R2 U' R2 U2` | 4e | 1 | 0c3-2 / 0c3-1 | 12 / 10 | 0 / 0 / 5.4% | 14 |
| 21 | `U' B2 R2 D F2 D B2 D2 R2 U' F2 U' L2 U F2 U'` | 4e | 2 | 0c3-2 / 0c3-2 | 13 / 11 | 0 / 0 / 0 | 16 |
| 22 | `D2 L2 F2 L2 F2 U' R2 D2 F2 D B2 L2 U2 R2 U'` | 6e | 2 | 0c3-1 / 0c3-2 | 9 / 10 | 0.22% / 2.2% / 9.6% | 15 |
| 23 | `D2 R2 U' R2 U2 R2 F2 U' R2 F2 D2 F2 U' F2 R2 U2` | 2e | 3 | 0c3-2 / 0c3-2 | 10 / 10 | 0 / 0.07% / 1.9% | 16 |
| 24 | `U' L2 U' B2 R2 D L2 U' B2 U L2 U B2 U2 R2 U'` | 6e | 1 | 0c3-2 / 0c3-2 | 10 / 10 | 0 / 0.13% / 1.9% | 16 |
| 25 | `R2 D' R2 U L2 U' R2 D' F2 U R2 D' L2 F2 D'` | 2e | 5 | 0c3-1 / 0c3-2 | 11 / 10 | 0 / 0 / 0.81% | 15 |

How the 25 came out: 0 in 10 or less, 0 in 11 or less, 1 in 12 or less, 3 in 13 or less. All of 0c3 is 0.04% / 0.38% / 2.6% / 13% (in 10 / 11 / 12 / 13), which for 25 DRs is about 0.0, 0.1, 0.6 and 3.3.

### 2c4

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 2c4-1 | both on one layer, adjacent; back-face diagonals agree | 7–10 | 2c3 |
| 2c4-2 | 1 up 1 down, opposite | 8–10 | 4b3 |
| 2c4-3 | both on one layer, adjacent; back-face diagonals differ | 7–10 | 2c3 |
| 2c4-4 | both on one layer, adjacent | 8–11 | nothing, needs a setup |
| 2c4-6 | 1 up 1 down, opposite | 8–11 | nothing, needs a setup |
| 2c4-7 | 1 up 1 down, stacked | 9–12 | nothing, needs a setup |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `R2 F2 L2 R2 D' B2 U B2 U' R2 U L2 D2` | 4e | 2 | 2c4-7 / 2c4-6 | 9 / 8 | 0.07% / 0.69% / 3.9% | 13 |
| 2 | `U' F2 U F2 D2 R2 U' B2 R2 D R2 F2 U L2 U'` | 4e | 3 | 2c4-7 / 2c4-6 | 9 / 9 | 0 / 0.23% / 2.3% | 15 |
| 3 | `U L2 U R2 B2 U' F2 U2 B2 U' R2 F2 R2` | 6e | 4 | 2c4-1 / 2c4-1 | 9 / 8 | 0.45% / 5.0% / 28% | 13 |
| 4 | `L2 F2 L2 U' F2 L2 D L2 D' R2 D F2 U2` | 6e | 4 | 2c4-7 / 2c4-1 | 10 / 8 | 0.37% / 3.9% / 20% | 13 |
| 5 | `D' F2 R2 D F2 U B2 R2 F2 D2 B2 D'` | 4e | 3 | 2c4-3 / 2c4-1 | 7 / 7 | 0.82% / 5.8% / 30% | 12 |
| 6 | `R2 D' F2 D B2 U' B2 F2 L2 D2 F2 D' L2` | 6e | 1 | 2c4-2 / 2c4-7 | 9 / 10 | 0 / 0.10% / 2.7% | 13 |
| 7 | `L2 B2 R2 U B2 U' B2 D' F2 U2 F2 U` | 2e | 3 | 2c4-3 / 2c4-3 | 8 / 8 | 0.96% / 4.3% / 20% | 12 |
| 8 | `U' L2 U B2 L2 B2 L2 U F2 D B2 F2` | 4e | 4 | 2c4-1 / 2c4-3 | 8 / 8 | 2.3% / 8.2% / 32% | 12 |
| 9 | `R2 B2 R2 U' L2 U B2 U2 L2 R2 U R2 U` | 4e | 2 | 2c4-3 / 2c4-3 | 8 / 8 | 0.53% / 3.1% / 15% | 13 |
| 10 | `D F2 D' R2 D' F2 U' F2 L2 U' L2 U B2` | 4e | 3 | 2c4-4 / 2c4-3 | 8 / 9 | 0.24% / 1.8% / 11% | 13 |
| 11 | `R2 U' R2 U2 R2 U' L2 D' B2 U2 B2 R2 U' R2` | 4e | 2 | 2c4-4 / 2c4-1 | 8 / 8 | 0.26% / 2.3% / 15% | 14 |
| 12 | `R2 U R2 B2 U' B2 D' B2 F2 U2 R2 F2 U'` | 0e | 2 | 2c4-1 / 2c4-1 | 7 / 7 | 1.0% / 7.6% / 36% | 13 |
| 13 | `D L2 U R2 F2 L2 B2 D F2 U R2 U2 R2` | 4e | 2 | 2c4-7 / 2c4-1 | 10 / 8 | 0.03% / 0.70% / 7.9% | 13 |
| 14 | `F2 U L2 U' F2 U B2 R2 U L2 D R2 U2 B2 D'` | 2e | 2 | 2c4-7 / 2c4-4 | 10 / 9 | 0 / 0.05% / 1.5% | 15 |
| 15 | `D' R2 F2 U R2 B2 F2 U' B2 R2 F2 R2 U' L2` | 6e | 0 | 2c4-4 / 2c4-1 | 9 / 9 | 0.03% / 0.43% / 4.4% | 14 |
| 16 | `R2 U' L2 D R2 U' B2 U R2 D2 B2 U2 B2` | 4e | 3 | 2c4-7 / 2c4-4 | 10 / 8 | 0 / 0.82% / 6.2% | 13 |
| 17 | `L2 B2 D F2 U' L2 U L2 D2 R2 B2 U F2 L2` | 4e | 2 | 2c4-6 / 2c4-7 | 8 / 10 | 0 / 0.44% / 2.9% | 14 |
| 18 | `B2 U2 R2 U B2 R2 D F2 U' B2 R2 D2 B2 R2 U'` | 4e | 1 | 2c4-1 / 2c4-4 | 9 / 9 | 0.02% / 0.47% / 5.4% | 15 |
| 19 | `L2 B2 U L2 D' R2 F2 D' R2 D' U2 B2 L2 U2 R2` | 6e | 2 | 2c4-7 / 2c4-4 | 10 / 9 | 0 / 0.15% / 2.3% | 15 |
| 20 | `B2 U B2 F2 U2 F2 U R2 U' B2 U R2 U2` | 2e | 3 | 2c4-4 / 2c4-6 | 8 / 9 | 0.08% / 0.88% / 7.8% | 13 |
| 21 | `R2 D' R2 B2 U' F2 D F2 L2 D2 L2 D L2 F2` | 2e | 3 | 2c4-4 / 2c4-7 | 9 / 9 | 0 / 0.13% / 2.5% | 14 |
| 22 | `F2 D' B2 R2 D2 L2 U' F2 L2 U' L2 U B2 D2` | 2e | 1 | 2c4-6 / 2c4-6 | 8 / 8 | 0.42% / 2.0% / 7.4% | 14 |
| 23 | `D2 L2 D F2 U' L2 D' F2 R2 U2 L2 D2 U' L2` | 6e | 3 | 2c4-2 / 2c4-6 | 9 / 9 | 0.20% / 2.6% / 14% | 14 |
| 24 | `U' B2 U B2 U L2 R2 U' B2 U R2 D' B2 U2` | 2e | 1 | 2c4-4 / 2c4-3 | 9 / 8 | 0.13% / 0.92% / 6.8% | 14 |
| 25 | `U B2 U' L2 B2 U2 B2 D' L2 D B2 U R2 U` | 6e | 5 | 2c4-6 / 2c4-3 | 10 / 8 | 0 / 1.4% / 13% | 14 |

How the 25 came out: 0 in 10 or less, 0 in 11 or less, 3 in 12 or less, 13 in 13 or less. All of 2c4 is 0.23% / 1.6% / 9.4% / 39% (in 10 / 11 / 12 / 13), which for 25 DRs is about 0.1, 0.4, 2.3 and 9.7.

### 0c4

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 0c4-1 | none bad | 9–10 | 4a3 |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `D2 B2 L2 R2 D' B2 D F2 L2 U2 L2 U' R2 U` | 6e | 2 | 0c4-1 / 0c4-1 | 10 / 10 | 0.09% / 0.66% / 5.1% | 14 |
| 2 | `L2 R2 B2 D B2 U F2 R2 U' B2 U R2 D R2 U'` | 2e | 6 | 0c4-1 / 0c4-1 | 10 / 9 | 0.37% / 3.0% / 18% | 15 |
| 3 | `B2 L2 U' F2 R2 U F2 R2 U2 B2 L2 D F2 U` | 4e | 0 | 0c4-1 / 0c4-1 | 9 / 10 | 0 / 0.12% / 2.6% | 14 |
| 4 | `U B2 U' F2 D2 L2 F2 R2 B2 U F2 U' F2` | 4e | 4 | 0c4-1 / 0c4-1 | 10 / 9 | 0.21% / 1.4% / 12% | 13 |
| 5 | `R2 B2 D B2 F2 L2 D' R2 D2 F2 D' R2 U` | 6e | 1 | 0c4-1 / 0c4-1 | 10 / 10 | 0 / 0.35% / 3.8% | 13 |
| 6 | `B2 D B2 L2 U' L2 D2 L2 B2 U R2 U R2 U2` | 4e | 4 | 0c4-1 / 0c4-1 | 10 / 10 | 0 / 1.3% / 7.5% | 14 |
| 7 | `U R2 D F2 D B2 U' F2 U' L2 U B2 F2` | 6e | 2 | 0c4-1 / 0c4-1 | 10 / 10 | 0.09% / 0.66% / 5.1% | 13 |
| 8 | `U F2 D L2 D2 F2 D F2 R2 F2 L2 U' R2 B2` | 4e | 4 | 0c4-1 / 0c4-1 | 9 / 10 | 0.21% / 1.4% / 12% | 14 |
| 9 | `U B2 F2 L2 F2 U L2 U2 F2 U B2 U F2 L2` | 2e | 2 | 0c4-1 / 0c4-1 | 10 / 10 | 0.17% / 0.66% / 6.0% | 14 |
| 10 | `F2 R2 B2 U2 F2 U F2 U F2 U2 R2 U L2 U` | 4e | 1 | 0c4-1 / 0c4-1 | 9 / 10 | 0.01% / 0.51% / 4.9% | 14 |
| 11 | `R2 U F2 U R2 U2 L2 B2 U' B2 U2 B2 F2 U'` | 6e | 1 | 0c4-1 / 0c4-1 | 10 / 10 | 0 / 0.35% / 3.8% | 14 |
| 12 | `U' R2 U' L2 D2 R2 B2 U F2 D2 B2 F2 U' L2` | 6e | 1 | 0c4-1 / 0c4-1 | 10 / 10 | 0 / 0.35% / 3.8% | 14 |
| 13 | `D2 L2 U' F2 D' B2 R2 U2 L2 D R2 F2 D'` | 2e | 4 | 0c4-1 / 0c4-1 | 9 / 9 | 0.23% / 1.4% / 10% | 13 |
| 14 | `R2 D L2 U' R2 B2 D2 R2 B2 U' B2 F2 L2 D'` | 2e | 2 | 0c4-1 / 0c4-1 | 9 / 10 | 0 / 0.77% / 7.1% | 14 |
| 15 | `L2 D B2 L2 D' B2 D2 L2 U' F2 U B2 U2` | 2e | 4 | 0c4-1 / 0c4-1 | 9 / 9 | 0.23% / 1.4% / 10% | 13 |
| 16 | `F2 D' L2 U F2 R2 U2 B2 R2 D' U2 B2 U' R2` | 8e | 0 | 0c4-1 / 0c4-1 | 11 / 11 | 0 / 0.11% / 1.9% | 14 |
| 17 | `R2 B2 L2 B2 D' L2 U B2 R2 U2 L2 U' F2 U'` | 2e | 3 | 0c4-1 / 0c4-1 | 10 / 10 | 0 / 0.70% / 7.2% | 14 |
| 18 | `D2 L2 B2 D' R2 U' B2 L2 U2 R2 D L2 D` | 6e | 0 | 0c4-1 / 0c4-1 | 10 / 10 | 0.01% / 0.11% / 1.9% | 13 |
| 19 | `D' L2 D B2 R2 U2 B2 L2 U F2 U' R2 F2 R2` | 8e | 0 | 0c4-1 / 0c4-1 | 11 / 11 | 0 / 0.11% / 1.9% | 14 |
| 20 | `R2 U' L2 D U2 B2 L2 D2 R2 D L2 U' B2` | 2e | 2 | 0c4-1 / 0c4-1 | 10 / 9 | 0 / 0.77% / 7.1% | 13 |
| 21 | `F2 R2 U F2 D L2 F2 U2 R2 F2 U L2 D B2` | 2e | 7 | 0c4-1 / 0c4-1 | 9 / 9 | 0.40% / 3.2% / 17% | 14 |
| 22 | `D' B2 D R2 B2 F2 D2 L2 F2 U L2 U2 R2 U'` | 8e | 0 | 0c4-1 / 0c4-1 | 11 / 11 | 0 / 0.11% / 1.9% | 14 |
| 23 | `D F2 D R2 D2 B2 U R2 D' L2 D2 F2 L2 R2` | 4e | 3 | 0c4-1 / 0c4-1 | 9 / 9 | 0.22% / 1.8% / 9.9% | 14 |
| 24 | `U' R2 U' B2 L2 D2 F2 R2 D L2 R2 D2 F2 R2 U'` | 4e | 2 | 0c4-1 / 0c4-1 | 10 / 9 | 0.11% / 0.80% / 6.7% | 15 |
| 25 | `U L2 B2 F2 D F2 L2 D2 F2 L2 D F2 R2 U'` | 2e | 1 | 0c4-1 / 0c4-1 | 9 / 9 | 0 / 0.28% / 4.0% | 14 |

How the 25 came out: 0 in 10 or less, 0 in 11 or less, 0 in 12 or less, 7 in 13 or less. All of 0c4 is 0.08% / 0.87% / 6.7% / 36% (in 10 / 11 / 12 / 13), which for 25 DRs is about 0.0, 0.2, 1.7 and 9.0.

### 4c4

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 4c4-1 (4a4) | 2-2, diagonal over diagonal | 9–10 | 4a3 |
| 4c4-2 (4b4) | 2-2, pairs sharing one column | 9–11 | 4a3 |
| 4c4-3 (4a4) | 2-2, pairs stacked | 10–11 | nothing, needs a setup |
| 4c4-4 (4b4) | 3-1 | 10–12 | nothing, needs a setup |
| 4c4-5 (4a4) | 2-2, pairs on opposite sides | 11–12 | nothing, needs a setup |
| 4c4-6 (4a4) | 4-0 | 11–12 | 0c3 |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `R2 F2 D L2 D' F2 L2 D2 R2 U' L2 B2 U'` | 4e | 3 | 4c4-1 / 4c4-4 | 9 / 11 | 0 / 0.66% / 4.6% | 13 |
| 2 | `L2 D' F2 U2 L2 D L2 B2 D2 R2 F2 U' L2 U' L2` | 4e | 2 | 4c4-5 / 4c4-4 | 11 / 10 | 0 / 0.01% / 0.28% | 15 |
| 3 | `F2 D' B2 R2 D R2 B2 D2 F2 D F2 U F2 L2 U2` | 2e | 4 | 4c4-5 / 4c4-4 | 11 / 10 | 0 / 0.09% / 1.1% | 15 |
| 4 | `D B2 U F2 D R2 D' L2 U L2 U' R2 F2 D2` | 4e | 3 | 4c4-4 / 4c4-3 | 10 / 10 | 0 / 0.25% / 2.1% | 14 |
| 5 | `U2 L2 D L2 U' L2 D2 L2 B2 U' F2 L2 U2 R2 U'` | 2e | 2 | 4c4-2 / 4c4-3 | 11 / 10 | 0 / 0.07% / 1.5% | 15 |
| 6 | `R2 F2 D L2 U' F2 U B2 L2 D R2 B2 U R2 U'` | 2e | 3 | 4c4-4 / 4c4-5 | 10 / 11 | 0 / 0.03% / 0.57% | 15 |
| 7 | `U' B2 D B2 L2 D' L2 R2 F2 D L2 U' L2 D` | 4e | 3 | 4c4-2 / 4c4-5 | 9 / 12 | 0 / 0 / 1.3% | 14 |
| 8 | `L2 U' L2 U' B2 F2 D F2 U L2 U2 B2 U' R2 U'` | 2e | 1 | 4c4-2 / 4c4-3 | 9 / 10 | 0.10% / 0.47% / 2.5% | 15 |
| 9 | `L2 D L2 D R2 U' B2 R2 U' B2 U' B2 L2 U` | 4e | 0 | 4c4-3 / 4c4-4 | 10 / 11 | 0 / 0 / 0.66% | 14 |
| 10 | `L2 D' L2 D' B2 F2 R2 U L2 U' F2 D' B2 U'` | 2e | 3 | 4c4-4 / 4c4-3 | 10 / 11 | 0 / 0.01% / 1.1% | 14 |
| 11 | `D' B2 D B2 D2 R2 U R2 U2 F2 U' R2 B2 U2` | 4e | 4 | 4c4-4 / 4c4-6 | 11 / 11 | 0 / 0 / 0.35% | 14 |
| 12 | `R2 U L2 U' R2 U B2 L2 U2 R2 D B2 D' R2 U'` | 4e | 1 | 4c4-3 / 4c4-4 | 10 / 11 | 0 / 0 / 0.82% | 15 |
| 13 | `U' B2 D R2 B2 R2 B2 U' F2 D R2 U' L2 U'` | 2e | 0 | 4c4-1 / 4c4-4 | 10 / 11 | 0 / 0.08% / 1.0% | 14 |
| 14 | `R2 D B2 U' L2 D' U2 R2 U' B2 U' L2 R2 B2 U'` | 4e | 1 | 4c4-4 / 4c4-3 | 11 / 10 | 0 / 0 / 0.82% | 15 |
| 15 | `R2 F2 D B2 L2 U' R2 D F2 U' R2 D' R2 U` | 4e | 6 | 4c4-5 / 4c4-4 | 11 / 10 | 0 / 0.14% / 1.7% | 14 |
| 16 | `R2 U2 L2 D B2 R2 U L2 F2 U2 F2 D F2 D' R2` | 4e | 2 | 4c4-4 / 4c4-5 | 11 / 11 | 0 / <0.01% / 0.15% | 15 |
| 17 | `D2 L2 U' R2 D F2 R2 D2 R2 D L2 U' F2 R2 U2` | 4e | 1 | 4c4-4 / 4c4-5 | 11 / 11 | 0 / 0 / 0.06% | 15 |
| 18 | `F2 D F2 D' L2 D F2 U' L2 F2 D' L2 D2 U'` | 2e | 3 | 4c4-4 / 4c4-6 | 11 / 12 | 0 / 0 / 0 | 14 |
| 19 | `D' B2 R2 D' L2 D' L2 B2 U2 R2 D' B2 U L2 U` | 4e | 1 | 4c4-3 / 4c4-2 | 10 / 9 | 0 / 0.11% / 2.4% | 15 |
| 20 | `B2 U' R2 F2 D B2 D2 B2 R2 U R2 U L2 B2 U2` | 4e | 1 | 4c4-5 / 4c4-4 | 11 / 10 | 0 / 0 / 0.13% | 15 |
| 21 | `B2 F2 L2 D' L2 R2 B2 D' R2 U2 F2 U L2 U'` | 2e | 0 | 4c4-1 / 4c4-4 | 9 / 11 | 0 / 0.14% / 2.3% | 14 |
| 22 | `U R2 U R2 D' B2 F2 R2 U R2 U' B2 U'` | 4e | 2 | 4c4-4 / 4c4-3 | 10 / 10 | 0 / 0.17% / 1.4% | 13 |
| 23 | `U' R2 F2 D' B2 L2 U2 R2 U' F2 U2 F2 R2 U' R2` | 2e | 1 | 4c4-4 / 4c4-6 | 11 / 11 | 0 / 0 / 0.34% | 15 |
| 24 | `U2 F2 L2 F2 U R2 U' B2 L2 U2 R2 D' L2 U' R2` | 4e | 0 | 4c4-4 / 4c4-1 | 11 / 10 | 0 / 0.22% / 2.5% | 15 |
| 25 | `B2 D' B2 L2 D' F2 L2 U2 L2 U' B2 U' L2` | 4e | 2 | 4c4-4 / 4c4-3 | 10 / 10 | 0 / 0.17% / 1.4% | 13 |

How the 25 came out: 0 in 10 or less, 0 in 11 or less, 0 in 12 or less, 3 in 13 or less. All of 4c4 is 0.02% / 0.19% / 1.6% / 11% (in 10 / 11 / 12 / 13), which for 25 DRs is about 0.0, 0.0, 0.4 and 2.8.

### 2c5

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 2c5-1 | both on one layer, adjacent | 9–12 | 2c4 |
| 2c5-2 | 1 up 1 down, opposite | 10–13 | 4b4 |
| 2c5-3 | 1 up 1 down, stacked | 11–13 | 4b4 |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `U2 R2 U B2 F2 R2 U' F2 D F2 U' L2 U' F2 U2` | 6e | 0 | 2c5-3 / 2c5-3 | 12 / 11 | 0 / 0 / 0 | 15 |
| 2 | `D' L2 U L2 F2 U' R2 U2 B2 L2 R2 D F2 U` | 2e | 3 | 2c5-1 / 2c5-3 | 10 / 11 | 0 / 0.05% / 0.97% | 14 |
| 3 | `U2 F2 U L2 F2 D' R2 D2 L2 B2 U' F2 U R2 U` | 4e | 1 | 2c5-2 / 2c5-1 | 11 / 10 | 0 / 0.04% / 0.98% | 15 |
| 4 | `B2 U2 F2 D' L2 B2 U B2 D' R2 U L2 B2 U` | 2e | 1 | 2c5-1 / 2c5-3 | 10 / 11 | 0 / 0 / 0.16% | 14 |
| 5 | `R2 D' B2 D R2 U F2 D2 B2 R2 D B2 D' F2 U2` | 4e | 1 | 2c5-1 / 2c5-3 | 10 / 11 | 0 / <0.01% / 0.31% | 15 |
| 6 | `D L2 B2 D' R2 D B2 R2 B2 L2 D2 U' R2 U'` | 6e | 2 | 2c5-1 / 2c5-1 | 10 / 10 | 0.02% / 0.41% / 3.8% | 14 |
| 7 | `F2 U2 B2 D' L2 F2 U L2 D' B2 U F2 U B2` | 4e | 3 | 2c5-2 / 2c5-3 | 10 / 11 | 0 / 0 / 0.54% | 14 |
| 8 | `D2 F2 L2 R2 D L2 D' B2 D F2 D' B2 U' L2 U2` | 4e | 4 | 2c5-3 / 2c5-3 | 11 / 12 | 0 / 0 / 0 | 15 |
| 9 | `R2 U L2 D L2 F2 L2 R2 U2 B2 U R2 D R2 U` | 2e | 3 | 2c5-2 / 2c5-2 | 11 / 10 | 0 / 0 / 1.6% | 15 |
| 10 | `B2 F2 D2 R2 B2 U' B2 U F2 U' R2 U R2 U' R2` | 4e | 2 | 2c5-2 / 2c5-3 | 10 / 11 | 0 / 0 / 0.49% | 15 |
| 11 | `F2 R2 U2 F2 R2 D' R2 D' F2 U B2 R2 U L2 D'` | 4e | 2 | 2c5-1 / 2c5-3 | 10 / 11 | 0 / 0.01% / 0.62% | 15 |
| 12 | `L2 D' L2 D B2 L2 R2 D B2 U2 R2 D' F2 R2 U` | 4e | 0 | 2c5-1 / 2c5-3 | 10 / 12 | 0 / 0 / 0.17% | 15 |
| 13 | `D' R2 U R2 U' F2 D' R2 B2 U2 F2 R2 U L2` | 4e | 1 | 2c5-1 / 2c5-1 | 10 / 10 | <0.01% / 0.13% / 1.9% | 14 |
| 14 | `B2 D R2 D L2 B2 F2 U' L2 D L2 D F2 D' U'` | 4e | 1 | 2c5-1 / 2c5-1 | 10 / 9 | 0 / 0.35% / 3.7% | 15 |
| 15 | `U2 L2 D' L2 U2 R2 D' R2 D' L2 B2 D' B2 U` | 6e | 2 | 2c5-1 / 2c5-3 | 10 / 11 | 0 / 0.05% / 0.96% | 14 |
| 16 | `D L2 B2 D R2 D2 B2 U' F2 D' L2 F2 U2 L2 U` | 4e | 1 | 2c5-2 / 2c5-1 | 10 / 11 | 0 / 0.04% / 0.98% | 15 |
| 17 | `B2 R2 D' B2 D' U2 B2 D' B2 L2 U' B2 U' R2` | 6e | 1 | 2c5-2 / 2c5-1 | 11 / 10 | 0 / 0.16% / 1.4% | 14 |
| 18 | `R2 B2 U' R2 B2 D B2 D' L2 B2 U' L2 D L2` | 2e | 1 | 2c5-1 / 2c5-1 | 10 / 10 | 0 / 0.22% / 2.4% | 14 |
| 19 | `B2 L2 D L2 U' B2 U L2 U B2 L2 D2 R2 F2 U'` | 4e | 1 | 2c5-1 / 2c5-1 | 9 / 10 | 0 / 0.35% / 3.7% | 15 |
| 20 | `B2 F2 U2 F2 U B2 D' F2 D L2 D' L2 B2 D' R2` | 2e | 3 | 2c5-2 / 2c5-3 | 10 / 11 | 0 / 0 / 0.36% | 15 |
| 21 | `L2 F2 L2 F2 U' B2 D L2 D2 F2 U' L2 D R2 U'` | 2e | 2 | 2c5-3 / 2c5-1 | 11 / 10 | 0 / 0.02% / 0.56% | 15 |
| 22 | `F2 D F2 U L2 D' L2 D2 L2 F2 L2 D B2 U'` | 4e | 1 | 2c5-1 / 2c5-1 | 10 / 10 | <0.01% / 0.13% / 1.9% | 14 |
| 23 | `B2 D2 L2 U F2 D B2 L2 U L2 U2 B2 U' L2 U'` | 2e | 2 | 2c5-1 / 2c5-1 | 10 / 10 | 0.02% / 0.32% / 3.2% | 15 |
| 24 | `D B2 R2 U' L2 U R2 D' F2 U R2 B2 L2 D2` | 6e | 0 | 2c5-1 / 2c5-1 | 9 / 10 | 0 / 0.26% / 2.6% | 14 |
| 25 | `D2 L2 D B2 U R2 D' L2 U R2 U' F2 U2 R2` | 4e | 4 | 2c5-3 / 2c5-3 | 11 / 11 | 0 / 0 / 0 | 14 |

How the 25 came out: 0 in 10 or less, 0 in 11 or less, 0 in 12 or less, 0 in 13 or less. All of 2c5 is 0.03% / 0.28% / 2.3% / 14% (in 10 / 11 / 12 / 13), which for 25 DRs is about 0.0, 0.1, 0.6 and 3.6.

### 4b5

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 4b5-1 | 3-1 | 9–12 | 2c4 |
| 4b5-2 | 2-2, pairs sharing one column | 10–12 | 4a4 |

| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |
|---:|---|---|---:|---|---|---|---:|
| 1 | `D2 F2 L2 F2 U' B2 L2 D2 U' R2 U' F2 U R2 U'` | 4e | 1 | 4b5-1 / 4b5-1 | 10 / 10 | <0.01% / 0.11% / 1.3% | 15 |
| 2 | `L2 D B2 U' R2 U B2 R2 U L2 F2 U2 B2 U` | 2e | 1 | 4b5-1 / 4b5-1 | 10 / 9 | <0.01% / 0.11% / 1.3% | 14 |
| 3 | `L2 B2 D' L2 U B2 D' L2 U' F2 U2 B2 R2 U'` | 4e | 2 | 4b5-1 / 4b5-1 | 10 / 10 | <0.01% / 0.12% / 1.9% | 14 |
| 4 | `D' F2 D L2 D F2 D' B2 U R2 U' L2 B2 U` | 4e | 1 | 4b5-2 / 4b5-1 | 11 / 10 | 0 / 0.04% / 0.68% | 14 |
| 5 | `L2 F2 U' L2 U' B2 U2 F2 L2 U' L2 U' B2 D'` | 2e | 1 | 4b5-2 / 4b5-1 | 10 / 9 | 0 / 0.08% / 1.1% | 14 |
| 6 | `U F2 L2 D R2 U' R2 U F2 U2 L2 U' B2 U2` | 4e | 4 | 4b5-2 / 4b5-1 | 11 / 10 | 0 / 0.22% / 2.8% | 14 |
| 7 | `B2 D' L2 U L2 D2 B2 L2 D L2 D' F2 U2 R2 U'` | 2e | 3 | 4b5-1 / 4b5-2 | 9 / 10 | 0.04% / 0.43% / 3.0% | 15 |
| 8 | `D' L2 D' B2 D2 L2 B2 L2 F2 D' L2 U R2 U` | 2e | 1 | 4b5-2 / 4b5-1 | 10 / 10 | 0 / 0.03% / 0.63% | 14 |
| 9 | `U B2 D B2 U' F2 U F2 U F2 D' B2 U F2 U2` | 4e | 1 | 4b5-1 / 4b5-1 | 9 / 10 | 0 / 0.06% / 1.3% | 15 |
| 10 | `U2 L2 B2 D R2 U' R2 D B2 L2 U F2 U B2` | 4e | 2 | 4b5-1 / 4b5-2 | 10 / 11 | 0 / 0.08% / 1.0% | 14 |
| 11 | `F2 U' L2 B2 D' B2 D R2 U F2 U2 L2 U' L2` | 2e | 3 | 4b5-1 / 4b5-2 | 10 / 10 | 0 / 0.18% / 2.2% | 14 |
| 12 | `B2 U L2 U2 B2 F2 U B2 U F2 U' R2 U F2 U2` | 2e | 1 | 4b5-1 / 4b5-1 | 10 / 9 | <0.01% / 0.11% / 1.3% | 15 |
| 13 | `R2 U L2 R2 B2 U L2 U' B2 F2 R2 D L2 U'` | 4e | 1 | 4b5-1 / 4b5-2 | 10 / 11 | 0 / 0.04% / 0.68% | 14 |
| 14 | `L2 F2 U L2 D' B2 D' F2 U2 R2 B2 D' B2 U'` | 4e | 5 | 4b5-1 / 4b5-1 | 10 / 10 | 0.17% / 1.4% / 9.1% | 14 |
| 15 | `F2 L2 D B2 D R2 F2 U F2 L2 D F2 D' R2 U2` | 4e | 1 | 4b5-2 / 4b5-1 | 11 / 10 | 0 / 0.04% / 0.68% | 15 |
| 16 | `L2 U B2 R2 B2 L2 D' F2 U L2 D' R2 U' B2 R2` | 0e | 1 | 4b5-1 / 4b5-2 | 9 / 10 | 0 / 0 / 0.47% | 15 |
| 17 | `D B2 U2 L2 R2 U L2 U F2 U F2 U2 F2 R2 U` | 4e | 1 | 4b5-1 / 4b5-1 | 11 / 10 | 0 / 0.07% / 0.98% | 15 |
| 18 | `D2 B2 U L2 D' B2 F2 R2 U F2 U' R2 U'` | 4e | 3 | 4b5-1 / 4b5-1 | 10 / 11 | 0 / 0.13% / 2.8% | 13 |
| 19 | `F2 D2 B2 D L2 D' B2 U L2 U' R2 D L2` | 2e | 1 | 4b5-1 / 4b5-2 | 9 / 10 | 0 / 0.08% / 1.1% | 13 |
| 20 | `D' F2 U2 R2 D F2 U' R2 U' B2 U2 F2 U R2` | 4e | 2 | 4b5-2 / 4b5-1 | 10 / 10 | 0 / 0.10% / 1.2% | 14 |
| 21 | `D L2 U2 F2 U' R2 U R2 B2 U L2 F2 U` | 2e | 2 | 4b5-1 / 4b5-1 | 9 / 10 | 0.03% / 0.29% / 2.5% | 13 |
| 22 | `U' B2 U' B2 F2 U2 R2 D' B2 D F2 L2 U'` | 4e | 4 | 4b5-1 / 4b5-1 | 10 / 10 | 0.08% / 0.65% / 5.7% | 13 |
| 23 | `R2 U B2 U' F2 R2 B2 R2 D' L2 D R2 U B2 U2` | 2e | 2 | 4b5-2 / 4b5-1 | 10 / 9 | 0.03% / 0.23% / 1.7% | 15 |
| 24 | `L2 U L2 D F2 D' B2 R2 U F2 U2 F2 R2 U` | 4e | 1 | 4b5-1 / 4b5-1 | 10 / 10 | <0.01% / 0.11% / 1.3% | 14 |
| 25 | `U' R2 D' B2 D F2 R2 B2 L2 U L2 D2 B2 U'` | 4e | 2 | 4b5-1 / 4b5-1 | 10 / 11 | 0 / 0.09% / 1.7% | 14 |

How the 25 came out: 0 in 10 or less, 0 in 11 or less, 0 in 12 or less, 4 in 13 or less. All of 4b5 is 0.02% / 0.21% / 1.9% / 14% (in 10 / 11 / 12 / 13), which for 25 DRs is about 0.0, 0.1, 0.5 and 3.4.

### All 300 against the odds

Add up the odds quoted for each of the 300 DRs and you get the number of finishes the tables expect. Against what happened:

| Finish | Expected from the subset alone | Expected from the full read (last-but-one column) | Happened |
|---|---:|---:|---:|
| 10 or less | 3.9 | 4.2 | 3 |
| 11 or less | 16.3 | 17.3 | 13 |
| 12 or less | 55.9 | 56.9 | 52 |

The reads don't change how many short finishes there are in a pile of DRs. They change which DRs you expect them in:

The 13 DRs that finished in 11 or less had been given 29% on average by the full read and 18% by their subset. The 52 DRs that finished in 12 or less had been given 51% on average by the full read and 40% by their subset.

<!-- many-examples:end -->
