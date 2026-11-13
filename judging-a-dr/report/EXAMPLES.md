# Judging a DR by hand: worked examples

*Eleven DRs, read the way the write-up says to read them, with what the exact tables say at each step and then the real optimal. Then 100 random-state scrambles with the DRs on the page, to judge yourself before you open the answers.*

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

After each read I give four numbers, **a / b / c / d**: the share of all DR states *with that same read* whose optimal finish is 10 or less / 11 or less / 12 or less / 13 or less. They are exact counts over all 19,508,428,800 DR states. 0 means no state at all gets there, <0.01% means a few do. These numbers are **computer only**: a lookup per DR in the full table, and for the combined lines (without solving, everything together) a class out of thousands. They're here to show what the reads are worth on one DR. In an attempt you have the odds of the write-up's guide per subset and its drop rules, which go by one read at a time.

Which of the four is yours depends on the DR. A 9- or 10-move DR gets finished whatever it looks like, and a 12 or a 13 from it is a result. The DRs you want to prune are the 11-movers, and those need a 10 or an 11 (one more if the first move of the finish merges with the last move of the DR). The examples are DR states with no DR length attached, so each verdict says what you'd do with it at 9 or 10 moves and at 11.

What each line counts:

- **Subset**: every DR of that subset (2c3 6e).
- **Pairs**: the ones of that subset with that many true pairs.
- **Corners**: every DR of that corner subset with that pair of corner cases, all edge counts together.
- **Without solving**: subset + pairs + corner case on both sides, as one class. This is where you stand before you pick up a pen.
- **HTR**: the ones of that subset with those two HTR lengths.
- **Corner solution and parity**: the ones of that subset with that L and that cost for the right parity.
- **Everything together**: subset + pairs + both HTR lengths + L + parity fit, as one class.

Then the truth: the optimal finish in DR moves, from the full table. That's the answer key, **computer only**.

**How the examples were picked.** Each row is a group of examples and where they come from:

| Examples | Where they're from |
|---|---|
| 1, 2 and 3 | the DRs in Rodney's and Levi's docs |
| 4 to 10 | each one is "the first DR my random generator produced with this read", from a fixed seed |
| 11 | the 1qt case from the write-up where a finish with three quarter turns is shorter than the 1qt bound |

They were picked by the read, never by the outcome, so some of them go against the odds. That's on purpose. The generator made each state with 30 random moves, which leans towards states with short finishes, so don't tally the outcomes of these seven. The DRs of the 100 scrambles at the end come from random-state scrambles and are tallied there.

Corner cases are named by where the bad corners are. When it matters which of two look-alike cases it is, I give the range of optimal corner solution lengths the case can have (L 7–10 and so on), which is how they're told apart in the write-up's corner case appendix.

---

## Eleven worked examples

### 1. Rodney's first random scramble: a decent 2c3

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

**Verdict before solving.**

- **At 9 or 10 moves** you solve it: good for a 13, and a 12 is somewhere between 15% and 38% depending on which read you believe.
- **At 11 moves** it's a pass: an 11 is 2–4% on every line that knows about the six bad edges, and a 10 is half a percent at best.

The reads don't agree with each other, and that's normal: this is what "an sd of 0.8 moves is left" looks like on one DR.

**Truth.** 13.

    R2 B2 D' B2 R2 U B2 R2 U F2 L2 U2 F2   // 13, optimal

Only one of the ten moves starts an optimal finish (R2). Rodney's doc finds a 13 after bounding its way through three skeletons, and it is optimal. If this DR's last move could be turned the other way and that amounted to an R2 here, the finish would be 12.

---

### 2. Rodney's 4a4: the reads say no, and it's a 13

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

**Verdict before solving.** Toss it unless the DR was very short.

- **At 11 moves** it's gone before you solve anything: no 4c4 4e with one pair and these corners finishes in 11 at all.
- **At 10 moves** a 12 is about 1% on any single read and under half a percent with them together. What's left is a one-in-ten 13.

**Truth.** 13.

    U2 F2 L2 D B2 U' F2 D2 R2 U B2 L2 U'   // 13, optimal

This is the one in ten. Rodney gets there by writing down the four ways to 2qt and bounding each, which is real work on one DR. Nothing you can read off the DR would have told you this one was worth it. That's the limit of triage by reads.

---

### 3. Levi's DR, and why you read both versions of the last move

    Scramble: R' U' F B2 R' F2 L' U2 R2 F2 D2 L2 U2 R' B2 U' F L' F L D F' L2 F2 R' U' F
    (D2 B' L' B U' F2 D L U2 R)   // 10-move DR, 4c3 4e

The DR ends in R on inverse. R' gives a DR too, a different state. Read both. First what each version shows, one read per row:

| Read | Ending in R (as written) | Ending in R' |
|---|---|---|
| subset | 4c3 4e | 4c3 4e |
| pairs | 2 | 2 |
| corners, normal | 3-1 | 3-1 |
| corners, inverse | all four on one layer (L 9–10) | 2-2 (L 9–11) |
| shortest HTR, normal | 9 | 9 |
| shortest HTR, inverse | 10 | 9 |
| L | 10 | 10 |
| L with the right parity | 10 | 11 |
| **optimal finish** | **15** | **14** |

Then the odds after each read for the DR as written. Each row is the class of DR states that share the reads so far; the columns are the share finishing in 10, 11, 12 and 13 or less:

| Ending in R, after reading | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|
| subset | 0.35% | 2.3% | 12% | 45% |
| pairs | 0.30% | 2.1% | 11% | 45% |
| corners | 0.03% | 0.51% | 4.8% | 28% |
| without solving | <0.01% | 0.29% | 3.9% | 25% |
| HTR | 0.02% | 0.51% | 5.6% | 34% |
| corner solution and parity | 0.09% | 0.23% | 7.5% | 25% |
| everything together | <0.01% | 0.02% | 3.5% | 21% |

The same for R':

| Ending in R', after reading | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|
| subset | 0.35% | 2.3% | 12% | 45% |
| pairs | 0.30% | 2.1% | 11% | 45% |
| corners | 0.01% | 0.29% | 3.0% | 20% |
| without solving | 0.02% | 0.31% | 2.7% | 19% |
| HTR | 0.15% | 1.6% | 11% | 48% |
| corner solution and parity | 0 | 1.3% | 3.6% | 32% |
| everything together | 0 | 1.0% | 2.9% | 40% |

**Verdict before solving.** It's a 10-move DR, so it gets solved either way. Both versions are 9+ to HTR on both sides, which is where Zagros throws a 4c3 away, and the corner cases on inverse are the two worst 4a3s. So:

- a 13-move finish would need luck (20–40%),
- a 12 isn't happening (3%),
- an 11 is somewhere between 0.02% and 1.6% depending on the line,
- with R' a 10 is ruled out for certain, because the corner solution of the right parity is 11.

One move longer and this DR would have been a toss on sight.

**Truth.** 15 as written, 14 with R'. Levi's doc says "14-move optimal finish, giving a 24". The 14 is the R' one, and the 24 holds either way: as written, a finish that starts with R2 merges with the R. With everything read, the two versions compare like this. Each row is a target; the last column says whether the odds picked the better version:

| Finish in, moves or less | Ending in R | Ending in R' | Pointed the right way? |
|---|---:|---:|---|
| 13 | 21% | 40% | yes |
| 12 | 3.5% | 2.9% | no |

An invertible last move is worth a third of a move on average. Here it's worth a whole one.

---

### 4. A 2c5 with the corners stacked on both sides: dead

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

### 5. A 2c4 with the best corners on both sides

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

**Verdict before solving.**

- **At 9 or 10 moves**, solve it. For a 2c4 this is as good as they come: about a coin flip for 13 and one in five or six for 12, against one in eleven for the subset.
- **At 11 moves** it's a long shot even so. The best corners there are take an 11 from 1.6% to 5.6%, the single pair pulls that back to about 3%, and with everything read it's 1.5%. A 10 is under 1% on every line.

That's what 4qt looks like at this target.

**Truth.** 12.

    U L2 U' R2 B2 U2 F2 B2 R2 D' L2 D   // 12, optimal

Two optimal first moves (U and L2). With an L2 available from the last DR move it would be 11.

---

### 6. A 2c4 with a double stack

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

### 7. A 4c3 that's 9+ to HTR on both sides

    R2 U B2 D' F2 U' B2 R2 D F2 U' R2 D' R2 U'   // 4c3 4e

**Subset.** 4c3 4e: 0.35% / 2.3% / 12% / 45% finish in 10 / 11 / 12 / 13. Average optimal 13.50.

**Pairs.** None. 0.08% / 0.87% / 6.7% / 33%.

**Corners.** 2-2 on both sides. On normal it's a 4b3 where a quarter turn goes straight to 4a2, on inverse a 4a3 with L 8–10. Middle of the pack: 0.35% / 2.1% / 11% / 42%.

**Without solving.** 4c3 4e, no pairs, those corners: 0.11% / 1.1% / 7.7% / 34%.

**HTR.** 10 on normal, 9 on inverse. This is Zagros's rule (9+ on both sides, throw it away). For 9 and 10: 0.02% / 0.51% / 5.6% / 34%.

**Corner solution and parity.** L = 10 with an odd number of side turns, E-slice even, so 11. With L = 10 and +1: 0 / 1.3% / 3.6% / 32%.

**Everything together**: 0 / 0.05% / 0.68% / 19%.

**Verdict before solving.** No 12 here, and a 13 one time in five.

- **With a short DR**: toss it unless the DR is short enough that a 14 helps.
- **At 11 moves** there's nothing to think about: the corner solution of the right parity is 11, so a 10 is ruled out for certain, and an 11 is one in 2,000 with everything read.

**Truth.** 15.

---

### 8. A 4c3 that's short to HTR on both sides

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

### 9. A blocky 4c4

    R2 U F2 U' L2 U R2 D' B2 U' F2 D   // 4c4 4e

**Subset.** 4c4 4e: 0.02% / 0.21% / 1.8% / 12% finish in 10 / 11 / 12 / 13. Average optimal 14.38. Normally a toss.

**Pairs.** Six. With six or more: **0.12% / 0.93% / 6.1% / 28%**, average 13.88. Only 0.1% of all DRs are a 4c4 4e this blocky.

**Corners.** 3-1 on normal, 2-2 on inverse. 0 / 0.08% / 1.3% / 11%. No help.

**Without solving.** 4c4 4e, five or more pairs (this lookup counts five and up as one), those corners: 0 / 0.37% / 4.7% / 28%.

**HTR.** 11 and 10. 0 / 0.07% / 1.3% / 10%. No help.

**Corner solution and parity.** L = 11 and the parity fits. 0 / 0.12% / 0.73% / 14%.

**Everything together**: 0 / 0.43% / 2.8% / 29%.

**Verdict before solving.** The only read that likes it is the pairs, and pairs take it from a 12% shot at 13 to 28–29%.

- **With a short DR** it's worth a look, with low hopes for 12.
- **At 11 moves**, no: 11 to HTR on normal means no 10 for certain, and even six pairs leave an 11 under 1%.

**Truth.** 12.

    D' F2 U B2 D R2 U' L2 U F2 U' R2   // 12, optimal

One optimal first move. That's the 3-in-100 outcome, so don't read it as "blocky 4c4s are good". Read it as: pairs were the only thing pointing the right way, and HTR length and corners, which usually carry more, saw nothing.

---

### 10. A 4b2 where everything says 12 and it's a 13

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

### 11. A 1qt case where a 3qt finish beats the 1qt bound

    U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2   // 4a1 4e

**HTR.** 6 on normal, 5 on inverse:

    F2 R2 F2 R2 F2 U     // HTR, normal (6)
    (U2 F2 R2 B2 U)      // HTR, inverse (5)

**Levi's formula.** $6 + 5 - 1 = 10$. So the best finish with one quarter turn is 10 moves.

**Truth.** 7.

    U B2 L2 F2 D F2 D   // 7, three quarter turns

The formula is exact for finishes with one quarter turn, which is what it's for, and says nothing about finishes with three. Over all 4a1 4e, a 3qt finish is shorter than the formula 11.7% of the time. The other reads here: the corner solution is L = 3 with the parity for free, and the odds, one read per row, as the share finishing in 10, 11, 12 and 13 or less:

| Read | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|
| five pairs (for 4a1 4e with five pairs) | 15% | 43% | 81% | 99% |
| everything together | 12% | 45% | 90% | 100% |

So when a 4a1 4e is this blocky and the bound still says 10, it's worth a minute on the 3qt finishes before you believe it. On an 11-move DR a bound of 10 reads as "a 21 at best", and here there was an 18 under it.

---

## What the examples show

The examples where a single read did the deciding. Each row is an example and the read; the last two columns are the share of DR states with that read finishing in 12 or less, and in 11 or less:

| Example | Read | For a 12 | For an 11 |
|---|---|---:|---:|
| 4 | corners on both sides | 0 | 0 |
| 5 | corners on both sides | 26% | 5.6% |
| 6 | corners on both sides | 0.63% | 0.03% |
| 7 | HTR on both sides | 5.6% | 0.51% |
| 8 | HTR on both sides | 43% | 14% |

- **Corners on both sides are the best quick read at 4–5qt.** They settle the first three of those in seconds.
- **HTR on both sides is the best read once you have it.** The last two are the same subset, and the HTR lengths alone split them, for a 12 and for an 11.
- **Pairs are free and sometimes the only read that's right** (example 9), and sometimes wrong (example 5 had one pair and a 12).
- **The target changes the verdict.** Examples 1 and 5 are DRs you solve at 9 or 10 moves and pass on at 11: a 12 is about one in five, an 11 is a few percent. Example 8 is the one you keep at 11 moves.
- **The parity bound is the only certainty, and it bites more the lower your target.** In examples 4 and 6 it rules out a 12 outright: no finish under 14, and no finish under 13. In examples 2, 7 and 9 the corner solution of the right parity is 11. That's no use against a 12, but it rules out a 10.
- **Odds are odds.** Example 2 was a 10% shot at 13 and came in. Example 10 was a 76% shot at 12 and didn't. Over many DRs the reads roughly double your hit rate for a 12, and do more than that for a 10 or an 11. On one DR they can't promise anything, and for that you still need to bound per skeleton the way Rodney does.

---

<!-- many-examples:start -->

## 100 scrambles: which DRs would you finish?

A hundred random-state scrambles, written the way FMC scrambles are, and for each one some of the DRs you could have on your page. What you can read off each DR without solving is in the two tables. The answers are folded away under them: pick the DRs you'd finish, then open them.

**Where the DRs come from.** cubelib-cli (the solver behind Mallard) lists every DR that goes EO first (EOs of up to 5 moves; it doesn't list longer ones), with NISS, and then DR on normal or on inverse without breaking the EO, on all three axes. A scramble has far more of those than anyone writes down: 721 up to 11 moves on average over the 500 scrambles of the tally at the end. Each scramble shows at most 8 of them: up to 4 of 10 moves or less, shortest first, then 11-movers, drawn at random where there are more. Nothing was picked by how it finishes.

**What you're testing.** You finish a DR of 10 moves or less whatever it looks like. The 11-movers are where you need a quick way to say no, and that's what the short list in the write-up's guide is for. It needs no solving:

- **2c5, 4b5, 4c4, 0c3, 0c4**: drop it.
- **2c4**: keep it only if on both sides the bad corners are not stacked and a quarter turn takes them straight to 2c3 or 4b3, or if it has four or more pairs.
- **4c3**: keep it only if its 4a3 side is 2-2 with a quarter turn straight to 4b2, or if it has four or more pairs.
- **4a2**: with 4e, keep it if on at least one side the bad corners are 2-2 with the two pairs stacked or each on a diagonal. With 2e or 0e, keep it only if one side has each layer's pair on a diagonal (a quarter turn straight to 4a1).
- **4a1, 4b2, 2c3, 0c0**: keep.

**The answers are the answer key**, **computer only**, not what a person finds in an hour: the true shortest HTR on each side, the optimal finish in DR moves, and the shortest solution through that DR.

### How to read the tables

- **Moves to DR**: brackets are moves on inverse. The last move on each side is written clockwise, and the row is about that DR exactly as written.
- **Length**: the number of moves to DR. **Axis**: the axis the DR is on.
- **Subset**: corner subset and number of bad edges, the way you already name it.
- **True pairs**: a corner and an edge next to each other in one of the two layers of the DR axis, both touching stickers matching.
- **Corner case, normal** and **inverse**: where the bad corners sit on each side, by the names in the table below (the same names as in the write-up's corner case appendix). Normal is the cube after the scramble and the unbracketed moves, with the bracketed ones as premoves the usual way. Inverse is the other side.
- **The list says**: `keep` or `drop` for a DR of 11 moves or more. A DR of 10 moves or less says `look anyway`.
- **Same reads: in 10, in 11, in 12**: of all DR states with that subset, that many true pairs (five or more count as one) and those two corner cases, the share whose optimal finish is 10 or less, 11 or less, 12 or less. 0 means none. An 11-move DR needs one of the first two. These are **computer only**, a lookup in a table of every subset, pair count and pair of corner cases. In an attempt the column to go by is **The list says**, with the guide per subset for the odds.
- **Shortest HTR, normal** and **inverse** (answers): the true shortest on each side.
- **Optimal finish** (answers): the optimal finish in DR moves of the DR as written.
- **Solution** (answers): the shortest solution through that DR, which is DR + finish less whatever cancels where the finish meets the DR. R then R2 is R', so a last move that is better turned the other way saves a move.

### The corner cases

"A qt takes it straight to" is the subset you are in after the right quarter turn of a layer, when one lowers the corner qt count with no setup. L is the range of optimal corner solution lengths. Each row is one corner case:

| Corner case | Bad corners | L | A qt takes it straight to |
|---|---|---|---|
| 0c0-1 | none bad | 0–5 | nothing, needs a setup |
| 4a1-1 | 4-0 | 1–4 | 0c0 |
| 4a1-2 | 2-2, pairs on opposite sides | 2–5 | nothing, needs a setup |
| 4a1-3 | 2-2, pairs stacked | 3–6 | nothing, needs a setup |
| 4a1-4 | 2-2, diagonal over diagonal | 4–7 | nothing, needs a setup |
| 4a2-1 | 2-2, diagonal over diagonal | 5–8 | 4a1 |
| 4a2-2 | 2-2, pairs stacked | 6–9 | nothing, needs a setup |
| 4a2-3 | 2-2, pairs on opposite sides | 7–10 | nothing, needs a setup |
| 4a2-4 | 4-0 | 8–11 | nothing, needs a setup |
| 4b2-1 | 2-2, pairs sharing one column | 3–6 | 4a1 |
| 4b2-2 | 3-1 | 4–7 | nothing, needs a setup |
| 4b2-3 | 3-1 | 5–8 | nothing, needs a setup |
| 4b2-4 | 2-2, pairs sharing one column | 6–9 | nothing, needs a setup |
| 2c3-1 | 1 up 1 down, stacked | 5–8 | 4b2 |
| 2c3-2 | 1 up 1 down, opposite | 5–8 | 4b2 |
| 2c3-3 | both on one layer, adjacent | 6–9 | nothing, needs a setup |
| 4c3-1 (4a3) | 2-2, pairs on opposite sides | 7–9 | 4b2 |
| 4c3-2 (4a3) | 2-2, pairs stacked | 7–9 | 4b2 |
| 4c3-3 (4a3) | 4-0 | 8–9 | nothing, needs a setup |
| 4c3-4 (4b3) | 2-2, pairs sharing one column | 7–10 | 4a2 |
| 4c3-5 (4b3) | 3-1 | 8–11 | nothing, needs a setup |
| 4c3-6 (4a3) | 2-2, diagonal over diagonal | 8–10 | nothing, needs a setup |
| 4c3-7 (4a3) | 2-2, pairs stacked | 8–10 | nothing, needs a setup |
| 4c3-8 (4a3) | 4-0 | 9–10 | nothing, needs a setup |
| 4c3-9 (4a3) | 2-2, pairs on opposite sides | 9–11 | nothing, needs a setup |
| 0c3-1 | none bad | 9–12 | 4a2 |
| 0c3-2 | none bad | 10–12 | nothing, needs a setup |
| 2c4-1 | both on one layer, adjacent; back-face diagonals agree | 7–10 | 2c3 |
| 2c4-2 | 1 up 1 down, opposite | 8–10 | 4b3 |
| 2c4-3 | both on one layer, adjacent; back-face diagonals differ | 7–10 | 2c3 |
| 2c4-4 | both on one layer, adjacent | 8–11 | nothing, needs a setup |
| 2c4-5 | 1 up 1 down, stacked | 9–11 | 4b3 |
| 2c4-6 | 1 up 1 down, opposite | 8–11 | nothing, needs a setup |
| 2c4-7 | 1 up 1 down, stacked | 9–12 | nothing, needs a setup |
| 0c4-1 | none bad | 9–10 | 4a3 |
| 4c4-1 (4a4) | 2-2, diagonal over diagonal | 9–10 | 4a3 |
| 4c4-2 (4b4) | 2-2, pairs sharing one column | 9–11 | 4a3 |
| 4c4-3 (4a4) | 2-2, pairs stacked | 10–11 | nothing, needs a setup |
| 4c4-4 (4b4) | 3-1 | 10–12 | nothing, needs a setup |
| 4c4-5 (4a4) | 2-2, pairs on opposite sides | 11–12 | nothing, needs a setup |
| 4c4-6 (4a4) | 4-0 | 11–12 | 0c3 |
| 2c5-1 | both on one layer, adjacent | 9–12 | 2c4 |
| 2c5-2 | 1 up 1 down, opposite | 10–13 | 4b4 |
| 2c5-3 | 1 up 1 down, stacked | 11–13 | 4b4 |
| 4b5-1 | 3-1 | 9–12 | 2c4 |
| 4b5-2 | 2-2, pairs sharing one column | 10–12 | 4a4 |

### The scrambles

#### Scramble 1

```
R' U' F L2 D' L2 F2 U' L2 D R2 U R2 B' R2 U R F U2 R' F R D' R U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(U' B' U' D' F' R2 F L' R2 B)` | 10 | R/L | 2c4 2e | 3 |
| 2 | `L2 U2 R' F L' F2 L2 D F B` | 10 | U/D | 4c4 2e | 2 |
| 3 | `(F U' R' U L D' B L2 D' F)` | 10 | U/D | 4b5 4e | 2 |
| 4 | `L2 U2 R' F L' B2 R2 U F B` | 10 | U/D | 4c4 2e | 2 |
| 5 | `L2 R' B2 R2 U D F U (L2 D' L)` | 11 | F/B | 4b5 4e | 0 |
| 6 | `(F U2 R' U' L' B U D F U2 F)` | 11 | U/D | 4b5 4e | 3 |
| 7 | `L2 U2 R' F L R2 F2 R2 D F B` | 11 | U/D | 4c4 2e | 2 |
| 8 | `(U' B U' D' F L2 U2 F L2 R' B)` | 11 | R/L | 2c4 2e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-6 | 2c4-5 | look anyway | 0.02% | 0.85% | 6.3% |
| 2 | 4c4-4 | 4c4-3 | look anyway | 0 | 0.05% | 0.96% |
| 3 | 4b5-2 | 4b5-1 | look anyway | 0 | 0.07% | 1.0% |
| 4 | 4c4-4 | 4c4-3 | look anyway | 0 | 0.05% | 0.96% |
| 5 | 4b5-2 | 4b5-2 | drop | 0 | 0 | 0.11% |
| 6 | 4b5-2 | 4b5-2 | drop | 0 | 0.01% | 0.79% |
| 7 | 4c4-4 | 4c4-3 | drop | 0 | 0.05% | 0.96% |
| 8 | 2c4-6 | 2c4-5 | drop | 0 | 0.41% | 4.2% |

Shown: 8 of the 194 DRs up to 11 moves (10 moves: 4 of 13; 11 moves: 4 of 181).

<details>
<summary>Answers for scramble 1</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 10 | 15 | 24 |
| 2 | 11 | 10 | 15 | 24 |
| 3 | 11 | 10 | 15 | 25 |
| 4 | 11 | 10 | 14 | 24 |
| 5 | 10 | 10 | 15 | 26 |
| 6 | 11 | 11 | 14 | 24 |
| 7 | 11 | 10 | 15 | 25 |
| 8 | 9 | 10 | 15 | 25 |

Best on the page: **24 moves**, from DR 1 (DRs 2, 4 and 6 tie it): `R' D2 L' U2 F2 R' U2 L D2 R' F2 D2 L' U2 B R2 L F' R2 F D U B U`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 2

```
R' U' F L2 U L2 F2 D2 R2 B2 F2 D U' L' F2 R' F2 U B' D' L2 D2 F' U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U L (B' L2 R' D' F B U)` | 9 | F/B | 4c4 4e | 0 |
| 2 | `U L (B' L2 R' D F B U)` | 9 | F/B | 4c4 4e | 2 |
| 3 | `U R' D' F L U L2 F2 D2 R` | 10 | U/D | 2c5 4e | 1 |
| 4 | `(D2 R2 U' D F' U' L R' U L)` | 10 | U/D | 4c4 2e | 3 |
| 5 | `(L' U F2 D B' L' R' D L R2 U)` | 11 | R/L | 4a1 4e | 2 |
| 6 | `U R' D' F' U2 B2 R U D' F2 L` | 11 | U/D | 2c4 2e | 1 |
| 7 | `U L (B' L2 R' D L2 R2 F B D)` | 11 | F/B | 4c4 4e | 0 |
| 8 | `(L2 D' F2 U2 B U L R U2 B2 U)` | 11 | R/L | 4a2 2e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-4 | 4c4-5 | look anyway | 0 | 0 | 0.06% |
| 2 | 4c4-4 | 4c4-3 | look anyway | 0 | 0.06% | 1.2% |
| 3 | 2c5-3 | 2c5-1 | look anyway | 0 | <0.01% | 0.37% |
| 4 | 4c4-6 | 4c4-2 | look anyway | 0 | 0.13% | 1.6% |
| 5 | 4a1-3 | 4a1-2 | keep | 5.5% | 19% | 54% |
| 6 | 2c4-1 | 2c4-3 | keep | 0.14% | 2.0% | 14% |
| 7 | 4c4-4 | 4c4-3 | drop | 0 | 0.02% | 0.67% |
| 8 | 4a2-2 | 4a2-4 | drop | 0 | 0 | 2.0% |

Shown: 8 of the 303 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 18; 11 moves: 4 of 283).

<details>
<summary>Answers for scramble 2</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 11 | 14 | 23 |
| 2 | 11 | 11 | 15 | 23 |
| 3 | 11 | 10 | 15 | 25 |
| 4 | 12 | 9 | 15 | 25 |
| 5 | 7 | 6 | 13 | 23 |
| 6 | 8 | 8 | 13 | 24 |
| 7 | 11 | 11 | 15 | 24 |
| 8 | 9 | 11 | 14 | 24 |

Best on the page: **23 moves**, from DR 1 (DRs 2 and 5 tie it): `U L F L2 F R2 D2 F D2 B' U2 L2 F' R2 F2 B' U' B' F' D R L2 B`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 3

```
R' U' F L2 D2 L2 U2 R2 B2 R2 D F2 D' R' U' F' U2 L' U' B R U2 L2 U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F' U B L U2 F R' B` | 8 | R/L | 0c3 6e | 1 |
| 2 | `F2 D2 F U' R U2 L F B` | 9 | R/L | 2c4 4e | 0 |
| 3 | `F' U B D2 L U2 F R' B` | 9 | R/L | 2c3 6e | 2 |
| 4 | `F' U B L U2 R2 B R' F` | 9 | R/L | 2c5 6e | 1 |
| 5 | `F2 D2 F U' L' B2 R2 B2 R F B` | 11 | R/L | 2c4 4e | 2 |
| 6 | `F' U (R' F2 B' L R F' U2 B' L)` | 11 | F/B | 4b5 2e | 1 |
| 7 | `F2 D2 F U' L F2 R F2 L2 F B` | 11 | R/L | 2c4 4e | 1 |
| 8 | `(R2 U2 D2 B U F' R U2 D2 F2 R)` | 11 | F/B | 2c5 6e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 0c3-1 | 0c3-2 | look anyway | 0.10% | 0.89% | 4.3% |
| 2 | 2c4-4 | 2c4-3 | look anyway | 0.03% | 0.44% | 3.9% |
| 3 | 2c3-2 | 2c3-1 | look anyway | 1.0% | 6.4% | 30% |
| 4 | 2c5-1 | 2c5-2 | look anyway | 0 | 0.16% | 1.5% |
| 5 | 2c4-4 | 2c4-3 | drop | 0.13% | 1.1% | 7.8% |
| 6 | 4b5-2 | 4b5-1 | drop | 0 | 0.05% | 0.78% |
| 7 | 2c4-6 | 2c4-3 | drop | 0.06% | 0.65% | 5.1% |
| 8 | 2c5-3 | 2c5-2 | drop | 0 | 0 | 0.07% |

Shown: 8 of the 1,255 DRs up to 11 moves (8 moves: 1 of 1; 9 moves: 3 of 15; 10 moves: 0 of 120; 11 moves: 4 of 1,119).

<details>
<summary>Answers for scramble 3</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 15 | 23 |
| 2 | 8 | 9 | 13 | 22 |
| 3 | 8 | 7 | 14 | 22 |
| 4 | 10 | 11 | 15 | 24 |
| 5 | 9 | 9 | 15 | 25 |
| 6 | 10 | 10 | 15 | 25 |
| 7 | 8 | 9 | 14 | 24 |
| 8 | 11 | 11 | 15 | 26 |

Best on the page: **22 moves**, from DR 2 (DR 3 ties it): `F2 D2 F U' R U2 L F B D2 R2 F2 R' U2 R' B2 D2 L' B2 R2 U2 L`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 4

```
R' U' F R2 B2 U2 F2 D U2 B2 D' L2 D' L B D U' L U' B2 F2 R2 F2 U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `R' U' L' U L (F' U' B U)` | 9 | F/B | 2c3 4e | 2 |
| 2 | `U' L' F' U' F D2 L' F R` | 9 | F/B | 4b2 2e | 4 |
| 3 | `U' L D2 L F B D B (R)` | 9 | U/D | 4c4 4e | 1 |
| 4 | `U' L' F' U' F' B2 U2 R' F L` | 10 | F/B | 4b2 4e | 4 |
| 5 | `D2 R F U L B2 D2 F B' D2 L` | 11 | F/B | 4b5 4e | 6 |
| 6 | `L B2 R' F' D' B2 D2 F L' B2 L` | 11 | F/B | 4c3 4e | 0 |
| 7 | `R (D2 L U2 L' D' B U2 D' B U)` | 11 | F/B | 2c4 4e | 1 |
| 8 | `D' L' U F2 U' L2 D (B U R2 F)` | 11 | R/L | 2c4 6e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-2 | 2c3-3 | look anyway | 0.66% | 4.2% | 22% |
| 2 | 4b2-3 | 4b2-2 | look anyway | 5.0% | 19% | 58% |
| 3 | 4c4-4 | 4c4-3 | look anyway | 0 | 0.02% | 0.78% |
| 4 | 4b2-3 | 4b2-2 | look anyway | 3.5% | 16% | 51% |
| 5 | 4b5-1 | 4b5-2 | drop | 0.07% | 1.0% | 6.9% |
| 6 | 4c3-2 | 4c3-5 | keep | 0.06% | 1.0% | 8.8% |
| 7 | 2c4-1 | 2c4-6 | drop | 0.09% | 0.94% | 7.2% |
| 8 | 2c4-1 | 2c4-6 | drop | 0.10% | 1.4% | 10% |

Shown: 8 of the 555 DRs up to 11 moves (9 moves: 3 of 3; 10 moves: 1 of 44; 11 moves: 4 of 508).

<details>
<summary>Answers for scramble 4</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 12 | 20 |
| 2 | 7 | 4 | 13 | 22 |
| 3 | 11 | 10 | 15 | 23 |
| 4 | 8 | 8 | 13 | 23 |
| 5 | 10 | 11 | 14 | 25 |
| 6 | 9 | 10 | 13 | 24 |
| 7 | 9 | 9 | 13 | 23 |
| 8 | 9 | 9 | 14 | 24 |

Best on the page: **20 moves**, from DR 1: `R' U' L' U L F' R2 L2 B' L2 B' U2 L2 F L2 F' U B' U F`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 5

```
R' U' F U' L2 B2 R2 D R2 F2 D2 L2 R2 F' R2 D' F L U B' L' B L2 U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(U2 D' L B U' R D R U' R)` | 10 | U/D | 4c4 4e | 1 |
| 2 | `U R' B (R2 U L' R' U L U)` | 10 | R/L | 2c4 6e | 1 |
| 3 | `U' L2 D' R F (L R D' B2 L)` | 10 | U/D | 2c5 6e | 2 |
| 4 | `D R2 D R U (F2 U2 B' D2 R)` | 10 | F/B | 4a1 4e | 3 |
| 5 | `(F2 D F' R2 U' B2 R2 B' D2 L B)` | 11 | R/L | 2c3 4e | 5 |
| 6 | `R' U B (R U2 F2 L' U D2 F2 U)` | 11 | R/L | 2c4 2e | 0 |
| 7 | `U R' B' L B2 U' R' U' R U' L` | 11 | U/D | 2c5 6e | 1 |
| 8 | `U' R' U2 B' L2 D2 R D L F2 L` | 11 | U/D | 4b2 4e | 5 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-6 | 4c4-2 | look anyway | 0 | 0.07% | 0.97% |
| 2 | 2c4-3 | 2c4-6 | look anyway | 0.04% | 0.51% | 4.6% |
| 3 | 2c5-3 | 2c5-3 | look anyway | 0 | 0 | 0 |
| 4 | 4a1-3 | 4a1-3 | look anyway | 6.1% | 20% | 54% |
| 5 | 2c3-1 | 2c3-3 | keep | 5.9% | 21% | 58% |
| 6 | 2c4-3 | 2c4-7 | drop | 0 | 0.12% | 2.2% |
| 7 | 2c5-2 | 2c5-1 | drop | 0 | 0.16% | 1.5% |
| 8 | 4b2-1 | 4b2-1 | keep | 16% | 39% | 77% |

Shown: 8 of the 665 DRs up to 11 moves (10 moves: 4 of 44; 11 moves: 4 of 621).

<details>
<summary>Answers for scramble 5</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 14 | 24 |
| 2 | 9 | 9 | 15 | 24 |
| 3 | 12 | 12 | 15 | 25 |
| 4 | 3 | 7 | 10 | 20 |
| 5 | 7 | 7 | 12 | 23 |
| 6 | 8 | 10 | 14 | 24 |
| 7 | 11 | 10 | 15 | 25 |
| 8 | 8 | 6 | 13 | 24 |

Best on the page: **20 moves**, from DR 4: `D R2 D R U B2 L2 F2 B' U2 R2 U2 L2 F2 L2 R' D2 B U2 F2`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 6

```
R' U' F U R D2 L2 F' U R' F L' D2 B' R2 D2 R2 D F2 B2 D R2 U B2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(U2 L' R F U' D2 F B2 D)` | 9 | F/B | 4c3 2e | 0 |
| 2 | `(L R' U D2 F B2 D B' D)` | 9 | F/B | 2c4 6e | 0 |
| 3 | `(L R' U' D2 F B2 D B' D)` | 9 | F/B | 4c4 4e | 0 |
| 4 | `U B D F2 L2 U' D' B (L R)` | 10 | U/D | 2c5 6e | 1 |
| 5 | `L2 F' B U' F2 B U' B2 D (L R)` | 11 | F/B | 4c3 4e | 0 |
| 6 | `D L2 B D F D L2 B2 U (L R)` | 11 | F/B | 2c5 6e | 1 |
| 7 | `(L R U' B' L2 F2 L2 B2 D2 B D)` | 11 | F/B | 2c3 4e | 1 |
| 8 | `U2 D' F D' B D F2 B2 U (L R)` | 11 | F/B | 2c5 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c3-2 | 4c3-4 | look anyway | 0.09% | 1.4% | 10% |
| 2 | 2c4-5 | 2c4-3 | look anyway | 0 | 0.44% | 4.8% |
| 3 | 4c4-2 | 4c4-3 | look anyway | 0 | 0.16% | 1.9% |
| 4 | 2c5-2 | 2c5-2 | look anyway | 0 | 0 | 0.83% |
| 5 | 4c3-6 | 4c3-4 | drop | 0.11% | 1.2% | 8.4% |
| 6 | 2c5-1 | 2c5-2 | drop | 0 | 0.16% | 1.5% |
| 7 | 2c3-3 | 2c3-1 | keep | 0.62% | 4.5% | 24% |
| 8 | 2c5-1 | 2c5-1 | drop | 0.10% | 0.85% | 6.2% |

Shown: 8 of the 1,274 DRs up to 11 moves (9 moves: 3 of 3; 10 moves: 1 of 95; 11 moves: 4 of 1,176).

<details>
<summary>Answers for scramble 6</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 10 | 14 | 23 |
| 2 | 10 | 9 | 15 | 23 |
| 3 | 10 | 10 | 14 | 22 |
| 4 | 11 | 10 | 15 | 24 |
| 5 | 9 | 10 | 12 | 22 |
| 6 | 9 | 11 | 14 | 25 |
| 7 | 9 | 6 | 14 | 25 |
| 8 | 10 | 10 | 15 | 25 |

Best on the page: **22 moves**, from DR 3 (DR 5 ties it): `D2 F R2 B D2 F L2 D2 F U2 B' L2 B D B D' B2 F' D2 U R L'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 7

```
R' U' F L2 U2 R2 U F2 U' L2 D' F2 D' F' L B' U' B2 L' D R' D F U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U (B' U L' D F L2 B)` | 8 | R/L | 2c3 2e | 1 |
| 2 | `U (B' U L' D B D2 F)` | 8 | R/L | 2c3 2e | 1 |
| 3 | `U (B' U L' D F2 B' U2 F)` | 9 | R/L | 2c3 2e | 1 |
| 4 | `(R' U B' L' D L' B' D2 L)` | 9 | F/B | 4c4 2e | 3 |
| 5 | `U (B' U L' D' F2 B2 U2 F R2 B)` | 11 | R/L | 2c3 2e | 3 |
| 6 | `U (B' U L' D B U2 F2 U2 D2 F)` | 11 | R/L | 2c3 2e | 2 |
| 7 | `U (B' U L' D F' R2 F' B' U2 F)` | 11 | R/L | 2c3 2e | 2 |
| 8 | `(U B' L' D' F D2 R' D2 L B2 R)` | 11 | U/D | 2c4 6e | 4 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-3 | look anyway | 0.44% | 3.7% | 22% |
| 2 | 2c3-3 | 2c3-3 | look anyway | 0.44% | 3.7% | 22% |
| 3 | 2c3-3 | 2c3-3 | look anyway | 0.44% | 3.7% | 22% |
| 4 | 4c4-3 | 4c4-4 | look anyway | 0 | 0.09% | 1.5% |
| 5 | 2c3-3 | 2c3-3 | keep | 1.0% | 6.1% | 29% |
| 6 | 2c3-3 | 2c3-2 | keep | 1.2% | 7.3% | 33% |
| 7 | 2c3-3 | 2c3-2 | keep | 1.2% | 7.3% | 33% |
| 8 | 2c4-1 | 2c4-3 | keep | 1.4% | 7.7% | 32% |

Shown: 8 of the 209 DRs up to 11 moves (8 moves: 2 of 2; 9 moves: 2 of 3; 10 moves: 0 of 24; 11 moves: 4 of 180).

<details>
<summary>Answers for scramble 7</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 14 | 21 |
| 2 | 7 | 7 | 14 | 21 |
| 3 | 7 | 6 | 14 | 22 |
| 4 | 10 | 11 | 14 | 22 |
| 5 | 7 | 6 | 13 | 23 |
| 6 | 7 | 8 | 12 | 22 |
| 7 | 7 | 7 | 13 | 24 |
| 8 | 8 | 8 | 12 | 22 |

Best on the page: **21 moves**, from DR 1 (DR 2 ties it): `U' R2 F2 L2 F2 D2 R B2 L U2 R' B2 R2 D2 B' L2 F' D' L U' B`. The list drops 0 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 8

```
R' U' F D2 F2 L2 U2 F2 R2 D' F2 U L2 F L2 R' U B R2 F' U' R D2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `D2 B' U' F U2 B (B2 U)` | 8 | R/L | 4c4 4e | 3 |
| 2 | `D2 B' U' B L2 F (B2 U)` | 8 | R/L | 4c4 4e | 2 |
| 3 | `U' R2 U2 B D2 L2 B2 D' L` | 9 | U/D | 4b5 2e | 2 |
| 4 | `U' L2 D2 F U2 L2 F2 U' L` | 9 | U/D | 4b5 2e | 2 |
| 5 | `F' D L (L2 U L2 F' D B' L2 U)` | 11 | F/B | 4a1 2e | 0 |
| 6 | `R2 U F2 B' U L' B2 L' F2 D' R` | 11 | U/D | 0c4 6e | 2 |
| 7 | `F' D L (F2 B2 D2 F R2 U D F)` | 11 | U/D | 4c4 4e | 1 |
| 8 | `U' R2 U2 B' U' B2 D2 R' U R' U` | 11 | R/L | 4c4 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-1 | 4c4-2 | look anyway | 0.18% | 1.2% | 6.7% |
| 2 | 4c4-1 | 4c4-2 | look anyway | 0.09% | 0.84% | 5.2% |
| 3 | 4b5-1 | 4b5-2 | look anyway | 0.01% | 0.14% | 1.4% |
| 4 | 4b5-1 | 4b5-2 | look anyway | 0.01% | 0.14% | 1.4% |
| 5 | 4a1-1 | 4a1-2 | keep | 0.98% | 6.4% | 31% |
| 6 | 0c4-1 | 0c4-1 | drop | 0.09% | 0.66% | 5.1% |
| 7 | 4c4-1 | 4c4-4 | drop | <0.01% | 0.24% | 2.5% |
| 8 | 4c4-4 | 4c4-3 | drop | 0 | 0.08% | 1.9% |

Shown: 8 of the 1,070 DRs up to 11 moves (8 moves: 2 of 2; 9 moves: 2 of 10; 10 moves: 0 of 98; 11 moves: 4 of 960).

<details>
<summary>Answers for scramble 8</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 12 | 20 |
| 2 | 10 | 9 | 15 | 22 |
| 3 | 10 | 10 | 15 | 23 |
| 4 | 10 | 10 | 15 | 24 |
| 5 | 6 | 7 | 13 | 23 |
| 6 | 10 | 10 | 13 | 23 |
| 7 | 9 | 11 | 14 | 25 |
| 8 | 10 | 10 | 14 | 25 |

Best on the page: **20 moves**, from DR 1: `D2 B' U' F U2 B U2 F2 U2 R D2 R U2 L2 F2 L' F2 R U' B2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 9

```
R' U' F D2 B2 R2 F2 U L2 B2 D2 B2 U B R U R2 B' D2 L2 B' F' L' U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `D2 F' R D2 R (D B L' U)` | 9 | F/B | 4b5 4e | 3 |
| 2 | `(D B L' U B' L B' R2 B)` | 9 | R/L | 4c4 2e | 4 |
| 3 | `D L2 U B (B D F' D' L)` | 9 | U/D | 4b2 4e | 2 |
| 4 | `(L' B U L' B2 L2 D2 F' D)` | 9 | F/B | 2c4 2e | 2 |
| 5 | `(F' B D' L U' F D R2 F B' D)` | 11 | F/B | 4c4 2e | 1 |
| 6 | `L' D2 F' L2 R2 D B (L' U D' L)` | 11 | U/D | 2c4 2e | 0 |
| 7 | `F B L2 U B D (L2 F U' F2 L)` | 11 | F/B | 2c4 4e | 2 |
| 8 | `L2 B L R2 B L (D B D2 L' U)` | 11 | F/B | 2c4 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b5-2 | 4b5-1 | look anyway | <0.01% | 0.13% | 1.8% |
| 2 | 4c4-3 | 4c4-4 | look anyway | 0 | 0.27% | 2.6% |
| 3 | 4b2-3 | 4b2-3 | look anyway | 0.64% | 5.0% | 27% |
| 4 | 2c4-3 | 2c4-5 | look anyway | 0.08% | 1.1% | 8.9% |
| 5 | 4c4-4 | 4c4-5 | drop | 0 | 0 | 0.09% |
| 6 | 2c4-6 | 2c4-7 | drop | 0 | 0.08% | 0.95% |
| 7 | 2c4-7 | 2c4-1 | drop | 0.08% | 0.85% | 7.2% |
| 8 | 2c4-1 | 2c4-4 | drop | 0.10% | 1.0% | 8.2% |

Shown: 8 of the 772 DRs up to 11 moves (9 moves: 4 of 16; 10 moves: 0 of 80; 11 moves: 4 of 676).

<details>
<summary>Answers for scramble 9</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 9 | 14 | 23 |
| 2 | 11 | 10 | 12 | 21 |
| 3 | 8 | 7 | 14 | 22 |
| 4 | 8 | 10 | 14 | 23 |
| 5 | 11 | 11 | 15 | 26 |
| 6 | 8 | 10 | 14 | 25 |
| 7 | 9 | 8 | 14 | 24 |
| 8 | 9 | 8 | 14 | 24 |

Best on the page: **21 moves**, from DR 2: `B2 R D2 L D2 F2 L2 B2 R F2 L' D2 B' R2 B L' B U' L B' D'`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 10

```
R' U' F D B2 D L2 D B2 D2 U' F2 R D B R2 U' R D2 U2 B2 R D' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' F2 D2 R F (R' D2 L)` | 8 | U/D | 4b2 4e | 2 |
| 2 | `U' F2 D2 R F (L' F2 R)` | 8 | U/D | 4b2 4e | 2 |
| 3 | `U (R' D2 L U' F R2 D2 F)` | 9 | R/L | 4c3 4e | 2 |
| 4 | `U' F2 D2 R F (L R2 B2 R)` | 9 | U/D | 4b2 4e | 2 |
| 5 | `(U' R' D2 B U F2 U' D L' R' D)` | 11 | R/L | 2c4 0e | 2 |
| 6 | `B2 D (R2 B2 U R F R' F R2 F)` | 11 | R/L | 2c4 4e | 1 |
| 7 | `U' F2 D2 R F (R U2 L R B2 R)` | 11 | U/D | 4b2 4e | 4 |
| 8 | `L' U' F2 D2 F' U2 L2 R U2 L' U` | 11 | R/L | 4c3 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-2 | 4b2-2 | look anyway | 1.9% | 10% | 40% |
| 2 | 4b2-2 | 4b2-2 | look anyway | 1.9% | 10% | 40% |
| 3 | 4c3-5 | 4c3-7 | look anyway | 0.17% | 1.3% | 7.9% |
| 4 | 4b2-2 | 4b2-2 | look anyway | 1.9% | 10% | 40% |
| 5 | 2c4-6 | 2c4-5 | drop | 0 | 0.49% | 6.4% |
| 6 | 2c4-6 | 2c4-2 | drop | 0.06% | 0.69% | 6.0% |
| 7 | 4b2-2 | 4b2-2 | keep | 4.9% | 19% | 56% |
| 8 | 4c3-6 | 4c3-5 | drop | 0.23% | 1.9% | 11% |

Shown: 8 of the 512 DRs up to 11 moves (8 moves: 2 of 2; 9 moves: 2 of 7; 10 moves: 0 of 40; 11 moves: 4 of 463).

<details>
<summary>Answers for scramble 10</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 12 | 20 |
| 2 | 8 | 7 | 14 | 20 |
| 3 | 9 | 10 | 13 | 21 |
| 4 | 8 | 7 | 10 | 18 |
| 5 | 8 | 9 | 14 | 25 |
| 6 | 8 | 9 | 14 | 24 |
| 7 | 8 | 7 | 11 | 21 |
| 8 | 10 | 9 | 14 | 25 |

Best on the page: **18 moves**, from DR 4: `U' F2 D2 R F' B2 L2 U' B2 U' B2 U' B2 U' R' B2 R2 L'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 11

```
R' U' F R2 D2 R2 U' B2 F2 D' L2 F2 R2 F' D2 L B2 U R' B' L2 B F U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `D F U (L' F' L U2 D2 R' F)` | 10 | R/L | 2c4 6e | 0 |
| 2 | `D F U (L2 U2 B2 U2 L' F B)` | 10 | R/L | 2c4 4e | 1 |
| 3 | `(B U2 D F D2 L2 D L B2 R)` | 10 | U/D | 2c4 4e | 3 |
| 4 | `D F U (L2 D2 F2 U2 R F B)` | 10 | R/L | 2c4 4e | 1 |
| 5 | `D F U (L' R2 B' L' U2 D2 R B)` | 11 | R/L | 2c4 6e | 0 |
| 6 | `F2 B2 U F D (U2 D2 L2 R F B)` | 11 | R/L | 2c4 4e | 2 |
| 7 | `D F U D2 F' L B' R' U2 R2 F` | 11 | R/L | 4b2 4e | 2 |
| 8 | `D F U (L U2 F R' F2 B2 L B)` | 11 | R/L | 2c4 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-4 | 2c4-7 | look anyway | 0 | 0.06% | 1.0% |
| 2 | 2c4-4 | 2c4-6 | look anyway | 0.02% | 0.28% | 2.4% |
| 3 | 2c4-1 | 2c4-7 | look anyway | 0.13% | 1.4% | 10% |
| 4 | 2c4-4 | 2c4-6 | look anyway | 0.02% | 0.28% | 2.4% |
| 5 | 2c4-4 | 2c4-5 | drop | 0.03% | 0.27% | 2.7% |
| 6 | 2c4-4 | 2c4-7 | drop | 0.01% | 0.19% | 2.1% |
| 7 | 4b2-3 | 4b2-3 | keep | 0.64% | 5.0% | 27% |
| 8 | 2c4-4 | 2c4-1 | drop | 0.10% | 1.0% | 8.2% |

Shown: 8 of the 276 DRs up to 11 moves (10 moves: 4 of 34; 11 moves: 4 of 242).

<details>
<summary>Answers for scramble 11</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 10 | 15 | 24 |
| 2 | 9 | 8 | 14 | 23 |
| 3 | 8 | 9 | 13 | 23 |
| 4 | 9 | 9 | 15 | 23 |
| 5 | 9 | 10 | 15 | 25 |
| 6 | 9 | 10 | 14 | 25 |
| 7 | 9 | 7 | 13 | 24 |
| 8 | 8 | 9 | 14 | 24 |

Best on the page: **23 moves**, from DR 2 (DRs 3 and 4 tie it): `D F U R' U2 R F2 R L2 U2 R D2 B2 L D2 L' B' F L U2 B2 U2 L2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 12

```
R' U' F R2 U' L2 U L B R' U D B D' L2 D B2 L2 B2 D' B2 D F2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' B U (D' F' L B2 R2 U2 F)` | 10 | R/L | 2c3 2e | 3 |
| 2 | `U' B U (D' F' L F2 L2 D2 F)` | 10 | R/L | 2c3 2e | 2 |
| 3 | `U' B U (D' F' L F2 R2 U2 B)` | 10 | R/L | 2c3 2e | 1 |
| 4 | `U' B U (D' F' L B2 L2 D2 B)` | 10 | R/L | 2c3 2e | 2 |
| 5 | `U' B U (D' F' L' B' L2 B2 D2 B)` | 11 | R/L | 2c4 2e | 2 |
| 6 | `U' D2 B U (D' L' D2 F' R2 B' L)` | 11 | F/B | 4c4 2e | 3 |
| 7 | `(D F' D R2 D' B' L R U2 R F)` | 11 | R/L | 2c3 4e | 1 |
| 8 | `L' F L D2 L F L2 U F U B` | 11 | U/D | 4b5 4e | 0 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-2 | look anyway | 1.9% | 10% | 40% |
| 2 | 2c3-3 | 2c3-2 | look anyway | 1.2% | 7.3% | 33% |
| 3 | 2c3-3 | 2c3-2 | look anyway | 0.77% | 5.6% | 29% |
| 4 | 2c3-3 | 2c3-2 | look anyway | 1.2% | 7.3% | 33% |
| 5 | 2c4-3 | 2c4-5 | drop | 0.08% | 1.1% | 8.9% |
| 6 | 4c4-4 | 4c4-5 | drop | 0 | 0.02% | 0.45% |
| 7 | 2c3-1 | 2c3-1 | keep | 1.4% | 8.6% | 37% |
| 8 | 4b5-1 | 4b5-2 | drop | 0 | <0.01% | 0.32% |

Shown: 8 of the 148 DRs up to 11 moves (10 moves: 4 of 16; 11 moves: 4 of 132).

<details>
<summary>Answers for scramble 12</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 6 | 6 | 14 | 23 |
| 2 | 6 | 5 | 12 | 22 |
| 3 | 6 | 5 | 11 | 21 |
| 4 | 6 | 6 | 13 | 22 |
| 5 | 8 | 10 | 12 | 23 |
| 6 | 10 | 11 | 15 | 24 |
| 7 | 8 | 5 | 13 | 23 |
| 8 | 10 | 10 | 15 | 26 |

Best on the page: **21 moves**, from DR 3: `U' B U L2 U2 L2 B2 D2 U2 R' U2 R B2 L' B' U2 R2 F2 L' F D`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 13

```
R' U' F R2 D2 F2 U2 B2 L2 D U B2 U F L2 R2 D F' L' D' L U' L D' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `R (R2 F' D L' U F' D2 B U)` | 10 | F/B | 2c4 6e | 1 |
| 2 | `R D L2 D' R2 F U (D F' L)` | 10 | F/B | 2c4 4e | 2 |
| 3 | `B' D2 F U' L (L2 D R2 B' D)` | 10 | F/B | 4b5 4e | 3 |
| 4 | `R' B2 U R (D F' D' L2 D' B)` | 10 | U/D | 4c4 4e | 1 |
| 5 | `R' B2 U R' B' U' F' L2 U D2 F` | 11 | U/D | 4c4 2e | 3 |
| 6 | `R U2 D B2 D L2 B U (D F' L)` | 11 | F/B | 2c4 2e | 4 |
| 7 | `B2 L2 U F2 R B D2 B' D' B U` | 11 | F/B | 2c5 6e | 2 |
| 8 | `U' R2 D' B2 R U2 B2 U F R2 B` | 11 | U/D | 2c4 6e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-4 | 2c4-7 | look anyway | 0 | 0.05% | 1.3% |
| 2 | 2c4-7 | 2c4-6 | look anyway | 0.01% | 0.28% | 2.3% |
| 3 | 4b5-1 | 4b5-1 | look anyway | 0.02% | 0.27% | 2.9% |
| 4 | 4c4-2 | 4c4-3 | look anyway | 0 | 0.21% | 2.2% |
| 5 | 4c4-4 | 4c4-6 | drop | 0 | 0 | 0.12% |
| 6 | 2c4-1 | 2c4-2 | keep | 1.5% | 8.6% | 38% |
| 7 | 2c5-3 | 2c5-3 | drop | 0 | 0 | 0 |
| 8 | 2c4-3 | 2c4-7 | drop | 0.01% | 0.44% | 4.0% |

Shown: 8 of the 206 DRs up to 11 moves (10 moves: 4 of 17; 11 moves: 4 of 189).

<details>
<summary>Answers for scramble 13</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 10 | 14 | 24 |
| 2 | 10 | 8 | 14 | 24 |
| 3 | 10 | 10 | 14 | 24 |
| 4 | 11 | 10 | 15 | 24 |
| 5 | 11 | 12 | 15 | 26 |
| 6 | 8 | 9 | 12 | 23 |
| 7 | 11 | 11 | 15 | 26 |
| 8 | 9 | 10 | 13 | 24 |

Best on the page: **23 moves**, from DR 6: `R U2 D B2 D L2 B U R2 D2 R2 F' R2 F' D2 F D2 R2 B' U2 L' F D'`. The list drops 3 of the 4 DRs of 11 moves or more, and keeps the best one.

</details>

#### Scramble 14

```
R' U' F R2 F' R U R2 B' D2 L' F U' R U D' R2 L2 F2 R2 B2 D F2 B2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `R' U D L (L2 R U' D' F D)` | 10 | F/B | 2c4 2e | 4 |
| 2 | `(U R U2 L' D' F2 R' F B R)` | 10 | F/B | 4b5 4e | 3 |
| 3 | `R U D L (R' U' D' F2 B' D)` | 10 | F/B | 2c4 2e | 2 |
| 4 | `R' U D L (R' U' D' F2 B' D)` | 10 | F/B | 2c4 2e | 5 |
| 5 | `B D F R' U (B R2 B U2 R2 B)` | 11 | R/L | 4c3 4e | 1 |
| 6 | `(U' L' R D L R B R' U2 L' F)` | 11 | R/L | 2c3 4e | 0 |
| 7 | `B D F R' U (F D2 F U2 R2 F)` | 11 | R/L | 4c3 4e | 1 |
| 8 | `B D F R' U (F U2 F R2 U2 F)` | 11 | R/L | 4c3 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-7 | 2c4-3 | look anyway | 0.20% | 2.3% | 14% |
| 2 | 4b5-1 | 4b5-1 | look anyway | 0.02% | 0.27% | 2.9% |
| 3 | 2c4-1 | 2c4-3 | look anyway | 0.37% | 3.1% | 19% |
| 4 | 2c4-7 | 2c4-3 | look anyway | 0.83% | 5.5% | 22% |
| 5 | 4c3-5 | 4c3-8 | drop | <0.01% | 0.29% | 3.1% |
| 6 | 2c3-3 | 2c3-3 | keep | 0.09% | 1.0% | 8.0% |
| 7 | 4c3-5 | 4c3-8 | drop | <0.01% | 0.29% | 3.1% |
| 8 | 4c3-5 | 4c3-8 | drop | <0.01% | 0.29% | 3.1% |

Shown: 8 of the 187 DRs up to 11 moves (10 moves: 4 of 11; 11 moves: 4 of 176).

<details>
<summary>Answers for scramble 14</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 8 | 14 | 23 |
| 2 | 10 | 10 | 15 | 25 |
| 3 | 8 | 8 | 13 | 23 |
| 4 | 10 | 8 | 14 | 23 |
| 5 | 8 | 10 | 14 | 24 |
| 6 | 7 | 9 | 12 | 22 |
| 7 | 8 | 9 | 14 | 24 |
| 8 | 8 | 11 | 14 | 24 |

Best on the page: **22 moves**, from DR 6: `B2 L' D2 U2 B2 L B2 L' F2 B2 D2 F L U2 R B' R' L' D' R' L U`. The list drops 3 of the 4 DRs of 11 moves or more, and keeps the best one.

</details>

#### Scramble 15

```
R' U' F U' B2 D' B2 U' B2 R2 B2 F2 D L U F' D2 L' D2 U' F' D' B2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `B2 D R' F' L (U' D2 B' L2 B)` | 10 | U/D | 4b2 2e | 3 |
| 2 | `B2 R' D (U L' R2 U2 L2 F' R)` | 10 | F/B | 4c3 4e | 1 |
| 3 | `D R' U2 F D' L2 B2 R' D (F)` | 10 | R/L | 4c4 4e | 4 |
| 4 | `B2 R' D' F R2 U2 D2 R F (U)` | 10 | R/L | 4c3 2e | 3 |
| 5 | `F' L' R' D2 F R' B2 D R B2 U` | 11 | R/L | 2c3 6e | 1 |
| 6 | `F2 U R B2 D (R2 D2 F' L' B R)` | 11 | F/B | 4c4 4e | 1 |
| 7 | `U' D R F2 D (B' U2 B U2 B' R)` | 11 | F/B | 0c3 4e | 4 |
| 8 | `U B' R D' R2 F2 L D2 F' R B` | 11 | R/L | 4b5 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-3 | 4b2-1 | look anyway | 4.4% | 17% | 52% |
| 2 | 4c3-5 | 4c3-8 | look anyway | <0.01% | 0.29% | 3.1% |
| 3 | 4c4-2 | 4c4-3 | look anyway | 0.11% | 0.91% | 5.0% |
| 4 | 4c3-2 | 4c3-4 | look anyway | 0.82% | 5.3% | 22% |
| 5 | 2c3-3 | 2c3-1 | keep | 0.33% | 2.7% | 17% |
| 6 | 4c4-3 | 4c4-4 | drop | 0 | 0.02% | 0.78% |
| 7 | 0c3-2 | 0c3-2 | drop | 0 | 0 | 0.75% |
| 8 | 4b5-2 | 4b5-2 | drop | 0 | <0.01% | 0.41% |

Shown: 8 of the 127 DRs up to 11 moves (10 moves: 4 of 9; 11 moves: 4 of 118).

<details>
<summary>Answers for scramble 15</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 6 | 6 | 12 | 22 |
| 2 | 9 | 10 | 14 | 24 |
| 3 | 9 | 11 | 14 | 23 |
| 4 | 8 | 10 | 12 | 22 |
| 5 | 9 | 7 | 14 | 24 |
| 6 | 10 | 11 | 14 | 25 |
| 7 | 12 | 12 | 14 | 25 |
| 8 | 11 | 10 | 14 | 25 |

Best on the page: **22 moves**, from DR 1 (DR 4 ties it): `B2 D R' F' L U' F2 L2 F2 U L2 B2 D L2 B2 U2 D' B' L2 B D2 U`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 16

```
R' U' F R2 B' R2 U2 B2 D2 F' L2 D2 R2 D' L2 R F2 L' R F' U F2 U' F2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U D R U' B (L' D' L)` | 8 | U/D | 4c3 4e | 0 |
| 2 | `R D B' R' D R2 B2 D' B` | 9 | U/D | 2c4 8e | 2 |
| 3 | `R D B' R B2 D' B2 U' B` | 9 | U/D | 4b2 2e | 4 |
| 4 | `D R2 B (U' F2 D' F2 B2 R)` | 9 | U/D | 2c4 6e | 1 |
| 5 | `R D B' R B2 U' L2 D R2 U2 F` | 11 | U/D | 4b2 2e | 6 |
| 6 | `F U' B2 D L F' R2 F U' B' D` | 11 | F/B | 4c4 2e | 6 |
| 7 | `B2 U' F2 U' L2 D' B (B U' D' R)` | 11 | U/D | 4b5 4e | 2 |
| 8 | `R2 F2 B2 U' B' R' U' L U' D2 L` | 11 | U/D | 2c4 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c3-6 | 4c3-5 | look anyway | 0.04% | 0.58% | 5.3% |
| 2 | 2c4-4 | 2c4-7 | look anyway | 0 | 0 | 0.24% |
| 3 | 4b2-3 | 4b2-3 | look anyway | 3.2% | 15% | 49% |
| 4 | 2c4-4 | 2c4-3 | look anyway | 0.07% | 0.66% | 5.4% |
| 5 | 4b2-3 | 4b2-3 | keep | 8.7% | 26% | 63% |
| 6 | 4c4-4 | 4c4-3 | drop | 0 | 0.48% | 4.7% |
| 7 | 4b5-1 | 4b5-1 | drop | <0.01% | 0.13% | 1.9% |
| 8 | 2c4-3 | 2c4-7 | drop | 0.13% | 1.2% | 8.1% |

Shown: 8 of the 551 DRs up to 11 moves (8 moves: 1 of 1; 9 moves: 3 of 4; 10 moves: 0 of 37; 11 moves: 4 of 509).

<details>
<summary>Answers for scramble 16</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 8 | 13 | 19 |
| 2 | 10 | 11 | 14 | 22 |
| 3 | 7 | 5 | 13 | 21 |
| 4 | 9 | 9 | 15 | 23 |
| 5 | 6 | 5 | 12 | 23 |
| 6 | 10 | 10 | 13 | 24 |
| 7 | 10 | 10 | 14 | 25 |
| 8 | 8 | 10 | 13 | 24 |

Best on the page: **19 moves**, from DR 1: `U D R U' B' D' L2 D2 B2 U2 D' F2 R2 F2 L2 D' L D L`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 17

```
R' U' F L2 D2 L2 B2 D' B2 L2 R2 D2 U2 F U2 L' F2 D' F R D' B L' D R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L D' L2 R U (B R U' L2 F)` | 10 | R/L | 4b2 2e | 1 |
| 2 | `U R' D F2 R (B D R' U B)` | 10 | U/D | 4b5 4e | 2 |
| 3 | `L R2 U F D L2 U' F (F2 U' R)` | 11 | U/D | 4a2 2e | 2 |
| 4 | `B' L F' U2 B' U' D B' U (F2 R)` | 11 | F/B | 2c5 2e | 2 |
| 5 | `D2 L2 D' R F2 L (B L R U' F)` | 11 | U/D | 4b2 0e | 2 |
| 6 | `D' R2 D2 R' U2 L (B' L R2 U F)` | 11 | U/D | 4b5 4e | 1 |
| 7 | `(B' U D2 L B L2 R B2 R2 U' R)` | 11 | U/D | 2c3 4e | 1 |
| 8 | `D' R2 D2 L' B2 R (B' L R2 U F)` | 11 | U/D | 4b5 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-2 | 4b2-1 | look anyway | 1.9% | 9.9% | 40% |
| 2 | 4b5-1 | 4b5-1 | look anyway | <0.01% | 0.13% | 1.9% |
| 3 | 4a2-4 | 4a2-2 | drop | 0 | 0 | 2.3% |
| 4 | 2c5-1 | 2c5-2 | drop | 0 | 0.06% | 1.8% |
| 5 | 4b2-4 | 4b2-2 | keep | 0.51% | 5.1% | 27% |
| 6 | 4b5-2 | 4b5-1 | drop | 0 | 0.03% | 0.64% |
| 7 | 2c3-1 | 2c3-1 | keep | 1.4% | 8.6% | 37% |
| 8 | 4b5-2 | 4b5-1 | drop | 0 | 0.03% | 0.64% |

Shown: 8 of the 33 DRs up to 11 moves (10 moves: 2 of 2; 11 moves: 6 of 31).

<details>
<summary>Answers for scramble 17</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 6 | 6 | 13 | 22 |
| 2 | 10 | 10 | 15 | 24 |
| 3 | 11 | 9 | 14 | 25 |
| 4 | 10 | 11 | 14 | 25 |
| 5 | 9 | 7 | 13 | 23 |
| 6 | 11 | 11 | 14 | 25 |
| 7 | 7 | 7 | 12 | 23 |
| 8 | 11 | 11 | 15 | 25 |

Best on the page: **22 moves**, from DR 1: `L D' L2 R U' R B2 D2 B2 R2 L' U2 F2 R U2 F2 R F' L2 U R' B'`. The list drops 4 of the 6 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 18

```
R' U' F L2 F2 L U2 B2 R D2 F2 L2 R U' D R' F' D' R2 U D2 F D R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L2 B L F L U' L D` | 8 | R/L | 2c4 4e | 1 |
| 2 | `L2 B L F L' D' L U` | 8 | R/L | 2c4 6e | 1 |
| 3 | `L2 B L F L R2 U' L D` | 9 | R/L | 2c4 4e | 4 |
| 4 | `L2 B L F L' R2 D' L U` | 9 | R/L | 2c4 6e | 4 |
| 5 | `F U B' D L' D2 B' D2 B' R B` | 11 | R/L | 4c4 4e | 1 |
| 6 | `F U' B' D (D2 L' D2 R2 B2 U2 B)` | 11 | R/L | 4c3 4e | 0 |
| 7 | `U2 F L B' R' U2 D L R2 U R` | 11 | U/D | 2c3 2e | 3 |
| 8 | `F L F2 B' D' R' D L F2 U L` | 11 | U/D | 2c4 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-4 | 2c4-5 | look anyway | 0 | 0.27% | 3.0% |
| 2 | 2c4-7 | 2c4-3 | look anyway | 0.01% | 0.44% | 4.0% |
| 3 | 2c4-7 | 2c4-3 | look anyway | 0.27% | 2.2% | 13% |
| 4 | 2c4-4 | 2c4-5 | look anyway | 0.35% | 2.3% | 11% |
| 5 | 4c4-4 | 4c4-6 | drop | 0 | 0 | 0.13% |
| 6 | 4c3-5 | 4c3-1 | keep | 0.07% | 1.2% | 10% |
| 7 | 2c3-1 | 2c3-2 | keep | 4.0% | 18% | 57% |
| 8 | 2c4-2 | 2c4-3 | keep | 0.38% | 2.8% | 17% |

Shown: 8 of the 624 DRs up to 11 moves (8 moves: 2 of 2; 9 moves: 2 of 5; 10 moves: 0 of 45; 11 moves: 4 of 572).

<details>
<summary>Answers for scramble 18</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 10 | 14 | 22 |
| 2 | 10 | 9 | 14 | 22 |
| 3 | 9 | 8 | 13 | 21 |
| 4 | 9 | 9 | 13 | 22 |
| 5 | 11 | 11 | 14 | 25 |
| 6 | 8 | 10 | 14 | 24 |
| 7 | 8 | 7 | 13 | 23 |
| 8 | 9 | 10 | 12 | 23 |

Best on the page: **21 moves**, from DR 3: `L2 B L F L R2 U' L D' R2 B2 L U2 L' D2 F2 L B2 R2 F2 L'`. The list drops 1 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 19

```
R' U' F D2 F2 L2 F D2 F L2 F2 D2 F L R' B2 D R' D B2 R' B' D' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F' B L' R B (F2 U L' D)` | 9 | R/L | 4c3 2e | 2 |
| 2 | `(F' L F' U D' F' U2 F R)` | 9 | F/B | 2c3 2e | 3 |
| 3 | `(U' L' D R' F R B' L R2 B)` | 10 | R/L | 4b2 4e | 1 |
| 4 | `(F' L F U D' L2 F' U2 F R)` | 10 | F/B | 2c3 4e | 5 |
| 5 | `F (U2 R F2 B U' L' R' U' R2 D)` | 11 | R/L | 2c5 4e | 1 |
| 6 | `B2 U (D L2 U B R U2 F' L R)` | 11 | F/B | 4c3 2e | 2 |
| 7 | `L2 F' D2 F' L' R B' L (U L' D)` | 11 | F/B | 2c4 6e | 2 |
| 8 | `L R' B L F2 R2 D2 R (U' L' D)` | 11 | F/B | 4a1 0e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c3-5 | 4c3-2 | look anyway | 0.38% | 2.6% | 15% |
| 2 | 2c3-2 | 2c3-3 | look anyway | 1.9% | 10% | 40% |
| 3 | 4b2-2 | 4b2-3 | look anyway | 0.68% | 5.1% | 26% |
| 4 | 2c3-2 | 2c3-3 | look anyway | 4.5% | 16% | 49% |
| 5 | 2c5-1 | 2c5-1 | drop | <0.01% | 0.23% | 2.7% |
| 6 | 4c3-5 | 4c3-8 | drop | 0.03% | 0.40% | 4.3% |
| 7 | 2c4-4 | 2c4-3 | drop | 0.17% | 1.2% | 8.1% |
| 8 | 4a1-1 | 4a1-4 | keep | 1.0% | 8.3% | 40% |

Shown: 8 of the 254 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 13; 11 moves: 4 of 239).

<details>
<summary>Answers for scramble 19</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 14 | 22 |
| 2 | 7 | 7 | 13 | 22 |
| 3 | 8 | 7 | 12 | 22 |
| 4 | 5 | 6 | 13 | 22 |
| 5 | 11 | 10 | 13 | 24 |
| 6 | 9 | 10 | 14 | 24 |
| 7 | 9 | 8 | 13 | 23 |
| 8 | 7 | 10 | 13 | 22 |

Best on the page: **22 moves**, from DR 1 (DRs 2, 3, 4 and 8 tie it): `F' B L' R B' F2 L' U2 F2 R U2 R F2 U2 R D2 R L2 D' L U' F2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 20

```
R' U' F R2 D2 U R2 D2 U' B2 F2 L2 B2 L B2 F2 R B U B D' L F2 U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `D' B (B' D F U' R' U F2 L)` | 10 | U/D | 2c3 0e | 6 |
| 2 | `D B L F (B' U' L' R' D' L)` | 10 | U/D | 4c4 2e | 3 |
| 3 | `D B (B L' F L2 U' B2 R F2 L)` | 11 | U/D | 2c4 2e | 5 |
| 4 | `L' U (F' U D R B' R' U2 D2 B)` | 11 | R/L | 4b5 4e | 1 |
| 5 | `F U L' D2 R' B D F B' D' B` | 11 | U/D | 2c4 4e | 2 |
| 6 | `B U D' F2 L' R B U2 R (B' D)` | 11 | F/B | 4b5 4e | 4 |
| 7 | `B' U D' L' B2 L2 B D2 L (B' D)` | 11 | F/B | 2c4 4e | 5 |
| 8 | `L' D F' B U' D2 L' R' D R (B)` | 11 | U/D | 4b2 4e | 5 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-3 | look anyway | 0 | 0.97% | 9.2% |
| 2 | 4c4-2 | 4c4-5 | look anyway | 0 | 0.06% | 1.3% |
| 3 | 2c4-3 | 2c4-1 | keep | 4.3% | 17% | 51% |
| 4 | 4b5-1 | 4b5-2 | drop | 0 | 0.03% | 0.64% |
| 5 | 2c4-3 | 2c4-4 | drop | 0.13% | 1.1% | 7.8% |
| 6 | 4b5-2 | 4b5-2 | drop | 0 | 0.04% | 1.3% |
| 7 | 2c4-3 | 2c4-5 | keep | 1.6% | 7.0% | 28% |
| 8 | 4b2-2 | 4b2-3 | keep | 6.8% | 25% | 64% |

Shown: 8 of the 18 DRs up to 11 moves (10 moves: 2 of 2; 11 moves: 6 of 16).

<details>
<summary>Answers for scramble 20</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 10 | 13 | 22 |
| 2 | 11 | 11 | 15 | 25 |
| 3 | 8 | 8 | 13 | 24 |
| 4 | 11 | 11 | 14 | 25 |
| 5 | 8 | 9 | 13 | 24 |
| 6 | 11 | 11 | 15 | 25 |
| 7 | 7 | 9 | 13 | 24 |
| 8 | 5 | 7 | 11 | 21 |

Best on the page: **21 moves**, from DR 8: `L' D F' B U' D2 L' R' D R' F2 U L2 F2 R2 L2 D L2 U2 L2 B'`. The list drops 3 of the 6 DRs of 11 moves or more, and keeps the best one.

</details>

#### Scramble 21

```
R' U' F U2 L2 D2 R2 U' L2 D L2 B2 D' L' D L' B' U' F' U L' D L2 U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `R2 B (F D2 F' D L U)` | 8 | R/L | 4c3 4e | 1 |
| 2 | `R2 B (B R2 B' D L U)` | 8 | R/L | 4c3 4e | 1 |
| 3 | `L' R U' L' F' D2 F D (L)` | 9 | F/B | 2c3 4e | 1 |
| 4 | `R D2 R D' B (U' R2 F2 D2 L)` | 10 | U/D | 4b5 2e | 1 |
| 5 | `R2 B (F D2 F' L2 U2 R2 U L D)` | 11 | R/L | 4b5 4e | 2 |
| 6 | `L' D (D R U' L' U2 B' L' U2 L)` | 11 | F/B | 4b2 4e | 0 |
| 7 | `B U F U2 L U' R U2 R (U2 B)` | 11 | U/D | 4c3 2e | 3 |
| 8 | `R2 B (B R2 B' D L D' R2 U D)` | 11 | R/L | 4c3 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c3-4 | 4c3-8 | look anyway | 0.02% | 0.43% | 3.4% |
| 2 | 4c3-4 | 4c3-8 | look anyway | 0.02% | 0.43% | 3.4% |
| 3 | 2c3-2 | 2c3-2 | look anyway | 0.49% | 3.9% | 21% |
| 4 | 4b5-2 | 4b5-2 | look anyway | 0 | 0.01% | 0.38% |
| 5 | 4b5-1 | 4b5-1 | drop | <0.01% | 0.13% | 1.9% |
| 6 | 4b2-3 | 4b2-3 | keep | 0.15% | 1.8% | 14% |
| 7 | 4c3-5 | 4c3-7 | drop | 0.14% | 1.6% | 9.5% |
| 8 | 4c3-4 | 4c3-8 | drop | 0.17% | 1.2% | 6.0% |

Shown: 8 of the 303 DRs up to 11 moves (8 moves: 2 of 2; 9 moves: 1 of 1; 10 moves: 1 of 31; 11 moves: 4 of 269).

<details>
<summary>Answers for scramble 21</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 10 | 14 | 22 |
| 2 | 8 | 10 | 13 | 21 |
| 3 | 7 | 8 | 14 | 22 |
| 4 | 10 | 10 | 15 | 25 |
| 5 | 10 | 11 | 14 | 25 |
| 6 | 8 | 7 | 13 | 24 |
| 7 | 9 | 8 | 14 | 23 |
| 8 | 8 | 9 | 13 | 24 |

Best on the page: **21 moves**, from DR 2: `R2 B R F2 U2 L2 B2 L' F2 U2 R2 U2 L' B2 R2 U' L' D' B R2 B'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 22

```
R' U' F D2 F' R2 D2 B U2 B L2 B' L2 R B U2 L2 B' D' R' U' F U B2 F' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(L' U B' R D R' U2 B L)` | 9 | F/B | 4a1 4e | 0 |
| 2 | `L2 F U2 R' F R U' D F2 L` | 10 | U/D | 4c4 2e | 3 |
| 3 | `L' F' U' D L F' R2 F' D' F` | 10 | U/D | 4b2 2e | 1 |
| 4 | `(L' R F2 D' F2 B' L2 D2 R D)` | 10 | R/L | 2c3 2e | 3 |
| 5 | `D' L R' B (F2 B' R2 D R' D L)` | 11 | U/D | 4c4 4e | 1 |
| 6 | `L (F2 U2 F R' U F' R2 F2 B' U)` | 11 | F/B | 2c4 4e | 1 |
| 7 | `(L' D' R B' L D R' D R' U2 R)` | 11 | U/D | 2c3 4e | 3 |
| 8 | `(R F2 L' D' B U2 F2 L U' F2 L)` | 11 | U/D | 4a2 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4a1-3 | 4a1-3 | look anyway | 1.6% | 8.5% | 33% |
| 2 | 4c4-1 | 4c4-4 | look anyway | 0.02% | 0.48% | 3.8% |
| 3 | 4b2-2 | 4b2-3 | look anyway | 1.2% | 7.0% | 31% |
| 4 | 2c3-3 | 2c3-3 | look anyway | 1.0% | 6.1% | 29% |
| 5 | 4c4-1 | 4c4-4 | drop | <0.01% | 0.24% | 2.5% |
| 6 | 2c4-7 | 2c4-2 | drop | 0 | 0.20% | 2.9% |
| 7 | 2c3-3 | 2c3-1 | keep | 1.8% | 9.3% | 37% |
| 8 | 4a2-3 | 4a2-3 | drop | 0.06% | 1.1% | 8.2% |

Shown: 8 of the 286 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 20; 11 moves: 4 of 265).

<details>
<summary>Answers for scramble 22</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 5 | 14 | 22 |
| 2 | 9 | 11 | 14 | 24 |
| 3 | 5 | 6 | 12 | 22 |
| 4 | 7 | 7 | 12 | 22 |
| 5 | 9 | 11 | 14 | 24 |
| 6 | 10 | 8 | 14 | 24 |
| 7 | 6 | 7 | 14 | 24 |
| 8 | 10 | 7 | 15 | 25 |

Best on the page: **22 moves**, from DR 1 (DRs 3 and 4 tie it): `F2 L2 D2 U2 F2 R2 U2 L2 B' R2 F2 R2 D2 L B' U2 R D' R' B U' L`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 23

```
R' U' F R2 D2 U' B2 U' R2 U' R2 L2 D R L2 D2 B L D' R' U2 F D' B2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L U' F2 B' L U' B D' B` | 9 | U/D | 2c3 2e | 2 |
| 2 | `(R' D2 L U B U2 B2 D' L2 U)` | 10 | F/B | 4c3 4e | 0 |
| 3 | `L U' F2 B' L U' R2 B D' B` | 10 | U/D | 4c3 4e | 1 |
| 4 | `L2 F' U F B' L' R2 U F2 U` | 10 | R/L | 4b2 2e | 2 |
| 5 | `D L2 F' U (L2 F L' R D2 R2 F)` | 11 | R/L | 2c4 4e | 4 |
| 6 | `F2 L (L U2 L U2 L2 F' D L2 U)` | 11 | F/B | 2c5 4e | 1 |
| 7 | `B2 D' R (R' B' D L2 R2 F2 B' U)` | 11 | F/B | 4c4 2e | 1 |
| 8 | `F2 L (L U2 L U' B' U R2 B U)` | 11 | F/B | 2c5 2e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-2 | look anyway | 1.2% | 7.3% | 33% |
| 2 | 4c3-3 | 4c3-4 | look anyway | 0.21% | 1.6% | 10% |
| 3 | 4c3-8 | 4c3-4 | look anyway | 0.02% | 0.43% | 3.4% |
| 4 | 4b2-3 | 4b2-2 | look anyway | 2.0% | 9.6% | 38% |
| 5 | 2c4-7 | 2c4-2 | keep | 0.06% | 1.0% | 9.1% |
| 6 | 2c5-3 | 2c5-1 | drop | 0 | <0.01% | 0.37% |
| 7 | 4c4-6 | 4c4-2 | drop | 0 | 0.08% | 1.2% |
| 8 | 2c5-1 | 2c5-2 | drop | 0 | 0.06% | 1.8% |

Shown: 8 of the 300 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 21; 11 moves: 4 of 278).

<details>
<summary>Answers for scramble 23</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 13 | 21 |
| 2 | 8 | 10 | 13 | 23 |
| 3 | 9 | 9 | 13 | 23 |
| 4 | 6 | 5 | 13 | 22 |
| 5 | 9 | 9 | 11 | 22 |
| 6 | 11 | 10 | 15 | 25 |
| 7 | 12 | 10 | 15 | 26 |
| 8 | 10 | 10 | 13 | 24 |

Best on the page: **21 moves**, from DR 1: `L U' F2 B' L U' B D' B' R2 L2 D2 B2 R2 U B2 R2 U' B2 R2 U'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 24

```
R' U' F U' B2 U2 F2 U R2 F2 U' B2 U2 F L D' B L U L2 R' B' F' U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F D2 B L (R2 F2 B' L U)` | 9 | F/B | 4c3 4e | 1 |
| 2 | `R' F' B' L2 U2 R (F' L' F D)` | 10 | F/B | 4c3 4e | 1 |
| 3 | `(U2 L' D F' B' R F L D2 F)` | 10 | R/L | 2c3 6e | 2 |
| 4 | `(R' D2 B' D F L' U' R D' R)` | 10 | U/D | 4b2 4e | 2 |
| 5 | `(U2 L' D' F L R' F2 B L U2 F)` | 11 | R/L | 4a1 4e | 4 |
| 6 | `(L' D' F R2 F B' L' U2 L2 F' R)` | 11 | F/B | 2c3 6e | 2 |
| 7 | `(L' D' R' U2 D2 R F U2 R2 B2 L)` | 11 | F/B | 4b5 2e | 2 |
| 8 | `(F D R B' L D L U2 L' U2 R)` | 11 | U/D | 4b2 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c3-8 | 4c3-4 | look anyway | 0.02% | 0.43% | 3.4% |
| 2 | 4c3-5 | 4c3-3 | look anyway | 0.18% | 1.6% | 10% |
| 3 | 2c3-3 | 2c3-1 | look anyway | 0.47% | 3.6% | 22% |
| 4 | 4b2-4 | 4b2-2 | look anyway | 0.97% | 6.2% | 30% |
| 5 | 4a1-2 | 4a1-4 | keep | 15% | 38% | 73% |
| 6 | 2c3-3 | 2c3-1 | keep | 0.47% | 3.6% | 22% |
| 7 | 4b5-1 | 4b5-1 | drop | 0.02% | 0.24% | 2.3% |
| 8 | 4b2-3 | 4b2-3 | keep | 1.2% | 7.9% | 35% |

Shown: 8 of the 296 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 11; 11 moves: 4 of 284).

<details>
<summary>Answers for scramble 24</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 14 | 22 |
| 2 | 10 | 9 | 14 | 23 |
| 3 | 8 | 7 | 13 | 23 |
| 4 | 8 | 7 | 14 | 24 |
| 5 | 2 | 7 | 10 | 21 |
| 6 | 8 | 7 | 12 | 23 |
| 7 | 9 | 10 | 14 | 24 |
| 8 | 9 | 9 | 10 | 21 |

Best on the page: **21 moves**, from DR 5 (DR 8 ties it): `B2 L U2 F2 U2 R2 F2 R2 B2 U2 F' U2 L' B' F2 R L' F' D L U2`. The list drops 1 of the 4 DRs of 11 moves or more, and keeps the best one.

</details>

#### Scramble 25

```
R' U' F L2 U' R D2 F' D2 R' B' L' R F' D' B2 D L2 R2 B2 U B2 L2 D' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F R F (B D2 R2 F' D)` | 8 | R/L | 4c4 2e | 4 |
| 2 | `L' R F2 U2 D F' R2 U F` | 9 | U/D | 2c4 4e | 2 |
| 3 | `(F2 U2 F' L R' U' L' R' U)` | 9 | R/L | 2c5 4e | 1 |
| 4 | `L R D R2 D F' U' L2 F` | 9 | U/D | 4b5 4e | 2 |
| 5 | `F2 L D2 R' U (L' D2 L' U2 F2 R)` | 11 | F/B | 4c4 4e | 1 |
| 6 | `D2 L' R U2 L2 R2 U B' R2 D B` | 11 | U/D | 2c4 4e | 2 |
| 7 | `F2 L D2 R' U (R' B2 R' U2 F2 L)` | 11 | F/B | 4c4 4e | 0 |
| 8 | `L' B2 R' D F' B2 L R D B2 D` | 11 | R/L | 0c4 2e | 4 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-5 | 4c4-4 | look anyway | 0 | 0.06% | 0.87% |
| 2 | 2c4-7 | 2c4-3 | look anyway | 0.07% | 0.72% | 5.7% |
| 3 | 2c5-3 | 2c5-1 | look anyway | 0 | <0.01% | 0.37% |
| 4 | 4b5-1 | 4b5-1 | look anyway | <0.01% | 0.13% | 1.9% |
| 5 | 4c4-3 | 4c4-2 | drop | 0 | 0.21% | 2.2% |
| 6 | 2c4-7 | 2c4-3 | drop | 0.07% | 0.72% | 5.7% |
| 7 | 4c4-3 | 4c4-2 | drop | 0 | 0.16% | 1.9% |
| 8 | 0c4-1 | 0c4-1 | drop | 0.15% | 1.2% | 8.6% |

Shown: 8 of the 1,591 DRs up to 11 moves (8 moves: 1 of 1; 9 moves: 3 of 7; 10 moves: 0 of 103; 11 moves: 4 of 1,480).

<details>
<summary>Answers for scramble 25</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 15 | 22 |
| 2 | 10 | 10 | 14 | 23 |
| 3 | 11 | 10 | 15 | 23 |
| 4 | 10 | 10 | 15 | 24 |
| 5 | 11 | 10 | 15 | 26 |
| 6 | 9 | 9 | 14 | 25 |
| 7 | 11 | 9 | 15 | 25 |
| 8 | 9 | 9 | 14 | 25 |

Best on the page: **22 moves**, from DR 1: `F R F L2 D2 F2 L' B2 R' B2 R2 U2 L D2 L F2 U2 D F R2 D2 B'`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 26

```
R' U' F R' F2 R2 L F2 D2 R' D2 F' U' L' U' B2 U' F2 U' B2 L2 U2 R2 D' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' F' D F2 U B2 L F` | 8 | R/L | 4c4 2e | 1 |
| 2 | `L F' D R F D2 F' L2 F` | 9 | R/L | 4c3 4e | 3 |
| 3 | `F2 R2 F B U' B (F' B2 R)` | 9 | U/D | 4b2 2e | 1 |
| 4 | `B' R2 U' F L B2 U2 F U` | 9 | F/B | 4c4 4e | 2 |
| 5 | `L F' D R' B2 L2 B L2 B' R2 F` | 11 | R/L | 4b5 4e | 1 |
| 6 | `F R2 B2 U F' L2 R' F D2 B2 L` | 11 | F/B | 0c0 4e | 3 |
| 7 | `R F2 L' F (D2 L D' R B2 R U)` | 11 | R/L | 2c4 4e | 1 |
| 8 | `L F' D' R D2 R B R2 B' L2 F` | 11 | R/L | 2c4 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-1 | 4c4-2 | look anyway | 0.03% | 0.36% | 3.6% |
| 2 | 4c3-2 | 4c3-4 | look anyway | 0.74% | 4.9% | 22% |
| 3 | 4b2-4 | 4b2-1 | look anyway | 1.4% | 7.6% | 32% |
| 4 | 4c4-6 | 4c4-2 | look anyway | 0 | 0.04% | 0.87% |
| 5 | 4b5-1 | 4b5-2 | drop | 0 | 0.03% | 0.64% |
| 6 | 0c0-1 | 0c0-1 | keep | 5.7% | 22% | 61% |
| 7 | 2c4-5 | 2c4-5 | drop | 0 | 0.08% | 1.4% |
| 8 | 2c4-7 | 2c4-2 | drop | 0.04% | 0.74% | 6.2% |

Shown: 8 of the 2,483 DRs up to 11 moves (8 moves: 1 of 1; 9 moves: 3 of 18; 10 moves: 0 of 208; 11 moves: 4 of 2,256).

<details>
<summary>Answers for scramble 26</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 10 | 15 | 23 |
| 2 | 9 | 10 | 14 | 23 |
| 3 | 6 | 6 | 11 | 19 |
| 4 | 12 | 10 | 15 | 24 |
| 5 | 10 | 11 | 15 | 26 |
| 6 | 7 | 4 | 12 | 23 |
| 7 | 10 | 9 | 15 | 25 |
| 8 | 10 | 8 | 14 | 25 |

Best on the page: **19 moves**, from DR 3: `F2 R2 F B U' B R2 U' R2 L2 U' L2 U' R2 U' L2 R B2 F`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 27

```
R' U' F D' R2 D L2 U' R2 D' B2 D' U' R U' F2 D2 B' F2 U F2 R' U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' D' L2 D2 B' D (F' R' B' U L)` | 11 | F/B | 2c3 2e | 5 |
| 2 | `B' U F L (R' D R2 D L2 U F)` | 11 | U/D | 2c3 6e | 0 |
| 3 | `L (B R F' L' F2 B' D F2 B U)` | 11 | F/B | 4c3 4e | 2 |
| 4 | `L (B R F' L' D2 R2 U' F B2 D)` | 11 | F/B | 4b2 2e | 3 |
| 5 | `L R2 D (F D' B' R' U2 F2 R2 F)` | 11 | R/L | 2c3 4e | 0 |
| 6 | `(R B' U F L R2 D F D2 F U)` | 11 | F/B | 4b5 4e | 3 |
| 7 | `B' U F L (R' D L2 U L2 D B)` | 11 | U/D | 2c3 4e | 2 |
| 8 | `B' U F L (R' U D2 F D' B' D)` | 11 | F/B | 0c4 2e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-1 | keep | 8.2% | 27% | 69% |
| 2 | 2c3-1 | 2c3-3 | keep | 0.21% | 2.1% | 14% |
| 3 | 4c3-1 | 4c3-4 | keep | 0.97% | 5.3% | 22% |
| 4 | 4b2-4 | 4b2-3 | keep | 1.4% | 8.1% | 35% |
| 5 | 2c3-3 | 2c3-3 | keep | 0.09% | 1.0% | 8.0% |
| 6 | 4b5-2 | 4b5-1 | drop | <0.01% | 0.13% | 1.8% |
| 7 | 2c3-1 | 2c3-3 | keep | 1.0% | 6.4% | 30% |
| 8 | 0c4-1 | 0c4-1 | drop | 0.04% | 0.70% | 6.5% |

Shown: 8 of the 11 DRs up to 11 moves (11 moves: 8 of 11).

<details>
<summary>Answers for scramble 27</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 6 | 7 | 9 | 20 |
| 2 | 8 | 8 | 12 | 23 |
| 3 | 9 | 10 | 14 | 24 |
| 4 | 6 | 7 | 13 | 22 |
| 5 | 9 | 8 | 12 | 22 |
| 6 | 11 | 11 | 15 | 26 |
| 7 | 6 | 7 | 13 | 23 |
| 8 | 10 | 10 | 13 | 24 |

Best on the page: **20 moves**, from DR 1: `U' D' L2 D2 B' D B' L2 F' D2 F' D2 B U2 B L' U' B R F`. The list drops 2 of the 8 DRs of 11 moves or more, and keeps the best one.

</details>

#### Scramble 28

```
R' U' F U2 R2 D2 B2 R2 D' L2 D2 U' R2 B U' B' R F D2 F2 D' F L U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F' D' R F' D B U2 R U2 B` | 10 | R/L | 2c5 6e | 1 |
| 2 | `(F' L' D R F2 D F' U' F2 U)` | 10 | F/B | 2c3 4e | 2 |
| 3 | `R2 F (L2 F' D B2 D R D L)` | 10 | U/D | 4b2 2e | 3 |
| 4 | `R' B2 L U' L2 B L' B R2 F` | 10 | R/L | 2c4 6e | 3 |
| 5 | `F2 B' L' D L B' U2 F' U2 L F` | 11 | R/L | 4c3 2e | 2 |
| 6 | `R F2 L D' L2 F' L U2 R2 B2 R` | 11 | F/B | 2c5 4e | 2 |
| 7 | `F2 D B2 L (L U2 D2 F D B' D)` | 11 | F/B | 4b2 4e | 2 |
| 8 | `U D2 R D' L2 F2 R' F2 B L (D)` | 11 | F/B | 4c4 2e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c5-2 | 2c5-2 | look anyway | 0 | 0 | 0.83% |
| 2 | 2c3-3 | 2c3-2 | look anyway | 0.66% | 4.2% | 22% |
| 3 | 4b2-2 | 4b2-1 | look anyway | 6.0% | 21% | 58% |
| 4 | 2c4-5 | 2c4-7 | look anyway | 0 | 0 | 2.3% |
| 5 | 4c3-6 | 4c3-5 | drop | 0.12% | 1.2% | 8.1% |
| 6 | 2c5-2 | 2c5-1 | drop | 0.02% | 0.23% | 2.4% |
| 7 | 4b2-3 | 4b2-4 | keep | 0.46% | 3.8% | 23% |
| 8 | 4c4-4 | 4c4-1 | drop | 0.04% | 0.38% | 2.8% |

Shown: 8 of the 508 DRs up to 11 moves (10 moves: 4 of 41; 11 moves: 4 of 467).

<details>
<summary>Answers for scramble 28</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 14 | 23 |
| 2 | 8 | 8 | 13 | 23 |
| 3 | 5 | 7 | 13 | 22 |
| 4 | 10 | 10 | 13 | 23 |
| 5 | 8 | 8 | 14 | 25 |
| 6 | 11 | 9 | 14 | 24 |
| 7 | 6 | 8 | 13 | 24 |
| 8 | 10 | 11 | 14 | 24 |

Best on the page: **22 moves**, from DR 3: `R2 F B2 L2 U L2 D F2 D2 B2 L2 F2 L2 U2 L D' R' D' B2 D' F L2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 29

```
R' U' F U' F2 U2 B2 R2 B2 L2 F2 R2 U R B2 F U' L2 F' U B D' L U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(D2 B2 R' U L' F2 L B)` | 8 | R/L | 2c4 6e | 2 |
| 2 | `(D' L' B' R' U R' U B2 R D)` | 10 | R/L | 4c4 4e | 2 |
| 3 | `(D' L' B U L2 B2 L U L D)` | 10 | R/L | 2c3 4e | 2 |
| 4 | `(D2 B2 R' U L2 U2 L U2 L B)` | 10 | R/L | 4b2 4e | 1 |
| 5 | `L' B2 R (F' L' D2 B2 R2 F' B U)` | 11 | F/B | 2c4 6e | 2 |
| 6 | `F' L R2 D2 B (F2 B2 U' F2 R' U)` | 11 | R/L | 4c3 4e | 5 |
| 7 | `R' U2 L (F' L' U2 L2 F' D2 B2 U)` | 11 | F/B | 4b5 4e | 4 |
| 8 | `L' B L B L' D2 F (U2 L F2 U)` | 11 | R/L | 4b5 2e | 5 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-2 | 2c4-1 | look anyway | 0.54% | 4.0% | 23% |
| 2 | 4c4-4 | 4c4-3 | look anyway | 0 | 0.06% | 1.2% |
| 3 | 2c3-3 | 2c3-1 | look anyway | 1.0% | 6.4% | 30% |
| 4 | 4b2-1 | 4b2-2 | look anyway | 1.7% | 9.1% | 36% |
| 5 | 2c4-3 | 2c4-4 | drop | 0.17% | 1.2% | 8.1% |
| 6 | 4c3-9 | 4c3-5 | keep | 0.11% | 1.4% | 10% |
| 7 | 4b5-1 | 4b5-2 | drop | 0.01% | 0.31% | 3.2% |
| 8 | 4b5-1 | 4b5-1 | drop | 0.25% | 1.8% | 9.5% |

Shown: 8 of the 708 DRs up to 11 moves (8 moves: 1 of 1; 10 moves: 3 of 68; 11 moves: 4 of 639).

<details>
<summary>Answers for scramble 29</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 8 | 14 | 21 |
| 2 | 10 | 11 | 14 | 24 |
| 3 | 8 | 7 | 15 | 24 |
| 4 | 8 | 9 | 13 | 23 |
| 5 | 9 | 9 | 14 | 24 |
| 6 | 10 | 9 | 14 | 25 |
| 7 | 11 | 10 | 15 | 25 |
| 8 | 9 | 10 | 14 | 24 |

Best on the page: **21 moves**, from DR 1: `R' D2 F2 L B2 R F2 L2 F2 U2 R' F2 U2 B L' F2 L U' R B2 D2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 30

```
R' U' F U2 L2 D' F2 U L2 R2 B2 U L2 F' U2 L' B' F2 D B U F2 U' R' U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F L B2 R U' F' D' B D (R)` | 10 | F/B | 2c5 4e | 1 |
| 2 | `L' D R' B2 U' L2 B' L F2 B' R` | 11 | F/B | 2c4 4e | 1 |
| 3 | `R D R' U' R U2 L (B' U2 L F)` | 11 | U/D | 2c5 2e | 2 |
| 4 | `(D' R B U L' U2 B D' F2 D' F)` | 11 | U/D | 0c3 4e | 3 |
| 5 | `F' R D2 L (R' U2 R2 U' B L2 F)` | 11 | U/D | 4c3 2e | 3 |
| 6 | `F R2 F U D2 F (U' D' R' B L)` | 11 | U/D | 4c3 4e | 1 |
| 7 | `D (D R U D' L F L2 B' U2 L)` | 11 | F/B | 2c5 4e | 1 |
| 8 | `(R U F B2 D' L R2 F' D2 B L)` | 11 | F/B | 2c4 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c5-2 | 2c5-3 | look anyway | 0 | 0 | 0.14% |
| 2 | 2c4-4 | 2c4-7 | drop | 0 | 0.08% | 1.5% |
| 3 | 2c5-3 | 2c5-2 | drop | 0 | 0 | 0.16% |
| 4 | 0c3-2 | 0c3-2 | drop | 0 | 0 | 0.53% |
| 5 | 4c3-5 | 4c3-3 | drop | 0.44% | 3.3% | 19% |
| 6 | 4c3-5 | 4c3-9 | drop | 0 | 0.10% | 1.9% |
| 7 | 2c5-2 | 2c5-1 | drop | 0 | 0.05% | 1.2% |
| 8 | 2c4-6 | 2c4-3 | drop | 0.06% | 0.65% | 5.1% |

Shown: 8 of the 52 DRs up to 11 moves (10 moves: 1 of 1; 11 moves: 7 of 51).

<details>
<summary>Answers for scramble 30</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 11 | 15 | 25 |
| 2 | 9 | 9 | 14 | 25 |
| 3 | 11 | 11 | 15 | 25 |
| 4 | 11 | 13 | 15 | 25 |
| 5 | 8 | 8 | 12 | 23 |
| 6 | 9 | 10 | 14 | 24 |
| 7 | 11 | 10 | 14 | 25 |
| 8 | 8 | 9 | 14 | 25 |

Best on the page: **23 moves**, from DR 5: `F' R D2 L U2 B2 U' R2 U R2 B2 D2 B2 U' F2 R2 F' L2 B' U R2 U2 R`. The list drops 7 of the 7 DRs of 11 moves or more, the best one among them. What's left gives 25 (DR 1), 2 moves more.

</details>

#### Scramble 31

```
R' U' F D' F2 U L2 U L2 B2 R2 U2 R2 B F' D' B' U2 R F D' F2 U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(F U' D' R B D' L2 B2 R)` | 9 | U/D | 4b2 4e | 1 |
| 2 | `U' D B' R (D2 B2 L2 D B)` | 9 | U/D | 4b5 2e | 2 |
| 3 | `(F U' D' R B' R2 F2 U R)` | 9 | U/D | 4b2 4e | 2 |
| 4 | `R F2 D2 F U D (L2 D R)` | 9 | F/B | 2c3 4e | 2 |
| 5 | `U' D B' R (D2 B2 U2 D2 R2 D F)` | 11 | U/D | 4b5 2e | 2 |
| 6 | `R (D R' D' F' U R2 F2 D' B D)` | 11 | F/B | 4c4 4e | 3 |
| 7 | `R D2 F2 D2 F B2 U D (L2 D R)` | 11 | F/B | 2c3 4e | 3 |
| 8 | `L' R2 U B R2 B2 D (U L F' R)` | 11 | F/B | 4b5 2e | 5 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-1 | 4b2-2 | look anyway | 1.7% | 9.1% | 36% |
| 2 | 4b5-2 | 4b5-2 | look anyway | 0 | 0.06% | 0.88% |
| 3 | 4b2-1 | 4b2-2 | look anyway | 2.4% | 12% | 43% |
| 4 | 2c3-2 | 2c3-2 | look anyway | 1.0% | 6.3% | 27% |
| 5 | 4b5-2 | 4b5-2 | drop | 0 | 0.06% | 0.88% |
| 6 | 4c4-6 | 4c4-4 | drop | 0 | 0 | 0.10% |
| 7 | 2c3-2 | 2c3-2 | keep | 1.9% | 9.7% | 36% |
| 8 | 4b5-1 | 4b5-2 | drop | 0.06% | 0.73% | 5.8% |

Shown: 8 of the 491 DRs up to 11 moves (9 moves: 4 of 9; 10 moves: 0 of 64; 11 moves: 4 of 418).

<details>
<summary>Answers for scramble 31</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 12 | 21 |
| 2 | 10 | 10 | 15 | 23 |
| 3 | 8 | 7 | 11 | 20 |
| 4 | 7 | 7 | 13 | 21 |
| 5 | 10 | 10 | 15 | 25 |
| 6 | 12 | 10 | 15 | 25 |
| 7 | 8 | 7 | 11 | 22 |
| 8 | 9 | 10 | 13 | 24 |

Best on the page: **20 moves**, from DR 3: `U2 F2 R2 B2 U L2 D2 F2 R2 D' B2 R' U' F2 R2 B R' D U F'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 32

```
R' U' F U2 R' B' R L2 U2 B L D' B U2 F B2 R2 D2 R2 L2 U L2 D' L2 D R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L U' R F' D R2 F' D2 B` | 9 | R/L | 4b2 4e | 4 |
| 2 | `L U' R F' D R2 B' L2 F` | 9 | R/L | 4b2 4e | 2 |
| 3 | `D2 F2 B' U (D' B2 R' B L' F)` | 10 | R/L | 4c4 4e | 0 |
| 4 | `(D F B U' F' D2 B' U2 R F)` | 10 | R/L | 4c3 4e | 1 |
| 5 | `(L B D L' R' D2 R2 U B R2 U)` | 11 | F/B | 4b5 2e | 1 |
| 6 | `F' L (D R' B' U2 L2 B U2 D F)` | 11 | U/D | 4b5 4e | 3 |
| 7 | `B' U' B (L B R D' R' U2 L D)` | 11 | R/L | 2c5 2e | 5 |
| 8 | `B2 U (L B D F2 L2 R B U2 B)` | 11 | R/L | 4b2 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-2 | 4b2-4 | look anyway | 2.7% | 13% | 46% |
| 2 | 4b2-2 | 4b2-4 | look anyway | 0.97% | 6.2% | 30% |
| 3 | 4c4-3 | 4c4-4 | look anyway | 0 | 0.02% | 0.67% |
| 4 | 4c3-5 | 4c3-8 | look anyway | <0.01% | 0.29% | 3.1% |
| 5 | 4b5-2 | 4b5-2 | drop | 0 | 0.01% | 0.38% |
| 6 | 4b5-1 | 4b5-2 | drop | <0.01% | 0.13% | 1.8% |
| 7 | 2c5-1 | 2c5-1 | drop | 0.67% | 3.5% | 16% |
| 8 | 4b2-3 | 4b2-2 | keep | 0.68% | 5.1% | 26% |

Shown: 8 of the 180 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 12; 11 moves: 4 of 166).

<details>
<summary>Answers for scramble 32</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 9 | 13 | 21 |
| 2 | 7 | 9 | 12 | 21 |
| 3 | 11 | 10 | 14 | 23 |
| 4 | 8 | 9 | 14 | 24 |
| 5 | 10 | 10 | 14 | 25 |
| 6 | 10 | 10 | 15 | 25 |
| 7 | 10 | 9 | 13 | 23 |
| 8 | 7 | 7 | 13 | 22 |

Best on the page: **21 moves**, from DR 1 (DR 2 ties it): `L U' R F' D R2 F' D2 B' R' F2 D2 L' D2 U2 R U2 L' D2 L2 F2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 33

```
R' U' F U2 R2 U' L2 F2 D F2 D' R2 U2 L' F2 R2 F' R B' F2 D R D U2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F D' B' L D2 R' U2 B' L` | 9 | F/B | 4b5 2e | 2 |
| 2 | `F D' B' L' F U2 F L F` | 9 | R/L | 4c4 4e | 2 |
| 3 | `F D B' L D2 R' U2 B' L` | 9 | F/B | 2c5 4e | 1 |
| 4 | `F D B' R F2 L' D2 F' L` | 9 | F/B | 2c5 6e | 2 |
| 5 | `F D F D2 R B' L' F U2 D2 L` | 11 | F/B | 4c4 2e | 3 |
| 6 | `F D' B R2 B2 L' B' R2 F R B` | 11 | R/L | 2c4 4e | 0 |
| 7 | `U2 F D' B' U2 L F R U2 B L` | 11 | F/B | 2c4 4e | 0 |
| 8 | `F D B D2 B' L B' D2 L' B2 R` | 11 | F/B | 0c4 2e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b5-2 | 4b5-2 | look anyway | 0 | 0.06% | 0.88% |
| 2 | 4c4-5 | 4c4-4 | look anyway | 0 | <0.01% | 0.20% |
| 3 | 2c5-1 | 2c5-1 | look anyway | <0.01% | 0.23% | 2.7% |
| 4 | 2c5-1 | 2c5-1 | look anyway | 0.02% | 0.38% | 3.8% |
| 5 | 4c4-5 | 4c4-2 | drop | 0 | 0.06% | 1.3% |
| 6 | 2c4-6 | 2c4-1 | drop | 0.05% | 0.55% | 5.2% |
| 7 | 2c4-7 | 2c4-4 | drop | 0 | 0.02% | 0.95% |
| 8 | 0c4-1 | 0c4-1 | drop | 0.11% | 1.0% | 8.5% |

Shown: 8 of the 860 DRs up to 11 moves (9 moves: 4 of 6; 10 moves: 0 of 72; 11 moves: 4 of 782).

<details>
<summary>Answers for scramble 33</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 14 | 23 |
| 2 | 11 | 10 | 15 | 24 |
| 3 | 10 | 9 | 14 | 23 |
| 4 | 10 | 10 | 14 | 23 |
| 5 | 11 | 10 | 15 | 25 |
| 6 | 8 | 9 | 13 | 23 |
| 7 | 9 | 9 | 15 | 26 |
| 8 | 10 | 9 | 14 | 25 |

Best on the page: **23 moves**, from DR 1 (DRs 3, 4 and 6 tie it): `F D' B' L D2 R' U2 B' L F' U2 B U2 B' U2 R2 F2 U2 R2 F L2 B' R2`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 34

```
R' U' F U' B D L F D2 B2 L' B' L B' R2 D L2 F2 L2 F2 U2 D' F2 D' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(D L' B' L R B2 R2 F' U)` | 9 | F/B | 4a1 4e | 3 |
| 2 | `(D L' B' L R F2 L2 F' D)` | 9 | F/B | 4a1 4e | 4 |
| 3 | `B' R2 U' L' R2 D (U D B)` | 9 | R/L | 2c3 8e | 2 |
| 4 | `B2 D (B' D' L2 U2 R' F B2 L)` | 10 | F/B | 4b2 4e | 3 |
| 5 | `R F' R U (D R F' U2 F B2 R)` | 11 | F/B | 4c3 2e | 3 |
| 6 | `(D' L F2 R' U F R' B2 D2 L F)` | 11 | R/L | 2c4 2e | 2 |
| 7 | `F' U2 R F B' R' U2 L' D' L R` | 11 | U/D | 4b5 4e | 2 |
| 8 | `F2 U2 F' B' R F (D' L' B' R D)` | 11 | R/L | 4b5 4e | 4 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4a1-2 | 4a1-4 | look anyway | 7.3% | 24% | 61% |
| 2 | 4a1-2 | 4a1-4 | look anyway | 15% | 38% | 73% |
| 3 | 2c3-2 | 2c3-3 | look anyway | 0.15% | 1.6% | 11% |
| 4 | 4b2-1 | 4b2-3 | look anyway | 3.1% | 13% | 48% |
| 5 | 4c3-4 | 4c3-9 | drop | 0.11% | 0.92% | 5.5% |
| 6 | 2c4-7 | 2c4-5 | drop | 0 | 0 | 0.81% |
| 7 | 4b5-1 | 4b5-1 | drop | <0.01% | 0.13% | 1.9% |
| 8 | 4b5-1 | 4b5-2 | drop | 0.01% | 0.31% | 3.2% |

Shown: 8 of the 280 DRs up to 11 moves (9 moves: 3 of 3; 10 moves: 1 of 26; 11 moves: 4 of 251).

<details>
<summary>Answers for scramble 34</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 3 | 4 | 12 | 21 |
| 2 | 3 | 4 | 12 | 20 |
| 3 | 9 | 10 | 14 | 21 |
| 4 | 7 | 8 | 13 | 23 |
| 5 | 10 | 9 | 15 | 25 |
| 6 | 10 | 9 | 15 | 25 |
| 7 | 10 | 10 | 15 | 25 |
| 8 | 10 | 10 | 14 | 25 |

Best on the page: **20 moves**, from DR 2: `F2 R2 B' R2 L2 F' D2 L2 B L2 F2 D F L2 F2 R' L' B L D'`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 35

```
R' U' F U B L2 U' L F2 D2 U' R B L D2 B2 R2 L2 B L2 B R2 D2 F' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `D R B L U (F D2 L F)` | 9 | R/L | 2c3 4e | 2 |
| 2 | `F' L' F' U' L R' D R (L B)` | 10 | U/D | 2c5 6e | 0 |
| 3 | `R2 U2 D R' U (B L2 R' F L)` | 10 | F/B | 4c4 2e | 2 |
| 4 | `D' L U2 R U B' R B' L2 U2 F` | 11 | R/L | 2c3 8e | 1 |
| 5 | `F' L' F' U' L B2 R' D R (L B)` | 11 | U/D | 2c3 4e | 2 |
| 6 | `U2 R2 U R D B' U2 L U2 R' F` | 11 | R/L | 4c4 2e | 3 |
| 7 | `U2 D R U' R2 U2 F' R F' B' L` | 11 | F/B | 2c3 2e | 0 |
| 8 | `F D L' F' U L2 F2 L' B R F` | 11 | R/L | 2c4 2e | 4 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-3 | look anyway | 0.35% | 2.6% | 15% |
| 2 | 2c5-3 | 2c5-1 | look anyway | 0 | 0.02% | 0.32% |
| 3 | 4c4-3 | 4c4-2 | look anyway | <0.01% | 0.19% | 2.1% |
| 4 | 2c3-1 | 2c3-3 | keep | 0.09% | 1.1% | 10% |
| 5 | 2c3-3 | 2c3-2 | keep | 0.66% | 4.2% | 22% |
| 6 | 4c4-2 | 4c4-5 | drop | 0 | 0.06% | 1.3% |
| 7 | 2c3-3 | 2c3-3 | keep | 0.35% | 3.1% | 19% |
| 8 | 2c4-4 | 2c4-7 | keep | 0.02% | 0.48% | 5.3% |

Shown: 8 of the 119 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 2 of 2; 11 moves: 5 of 116).

<details>
<summary>Answers for scramble 35</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 9 | 13 | 21 |
| 2 | 12 | 10 | 15 | 24 |
| 3 | 10 | 9 | 14 | 24 |
| 4 | 9 | 10 | 14 | 24 |
| 5 | 8 | 8 | 14 | 23 |
| 6 | 9 | 11 | 15 | 26 |
| 7 | 7 | 6 | 13 | 23 |
| 8 | 9 | 10 | 14 | 25 |

Best on the page: **21 moves**, from DR 1: `D R B L U' F2 D2 U2 R' U2 R' L2 U2 R' B2 D2 B2 F L' D2 F'`. The list drops 1 of the 5 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 36

```
R' U' F D B2 R2 U' L2 B2 U F2 R2 F R' B' F' U L B2 D2 R' B U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(L R' D2 B' L2 R U R U)` | 9 | R/L | 4c3 4e | 1 |
| 2 | `(R' D' F2 L B' D2 L2 R U)` | 9 | R/L | 4b2 2e | 1 |
| 3 | `D' L' D R D (L D R' B)` | 9 | R/L | 4b5 2e | 6 |
| 4 | `R2 B D' B D L F B2 L` | 9 | F/B | 2c3 4e | 2 |
| 5 | `(R' D2 L2 B2 R B' U2 B' D' F D)` | 11 | F/B | 2c3 6e | 2 |
| 6 | `L' F R' D2 R' B L (B' D F' D)` | 11 | F/B | 2c4 4e | 1 |
| 7 | `(L D2 R2 B2 L' D2 F U' D2 B U)` | 11 | F/B | 4c4 4e | 2 |
| 8 | `(D F' D' L2 R F' R B2 R2 D2 L)` | 11 | F/B | 0c3 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c3-9 | 4c3-5 | look anyway | 0 | 0.10% | 1.9% |
| 2 | 4b2-4 | 4b2-1 | look anyway | 1.4% | 7.6% | 32% |
| 3 | 4b5-1 | 4b5-2 | look anyway | 0.06% | 0.73% | 5.8% |
| 4 | 2c3-3 | 2c3-2 | look anyway | 0.66% | 4.2% | 22% |
| 5 | 2c3-3 | 2c3-3 | keep | 0.09% | 1.0% | 8.2% |
| 6 | 2c4-5 | 2c4-6 | drop | 0.01% | 0.31% | 2.9% |
| 7 | 4c4-4 | 4c4-3 | drop | 0 | 0.06% | 1.2% |
| 8 | 0c3-1 | 0c3-1 | drop | 0.19% | 0.83% | 4.3% |

Shown: 8 of the 1,760 DRs up to 11 moves (9 moves: 4 of 11; 10 moves: 0 of 153; 11 moves: 4 of 1,596).

<details>
<summary>Answers for scramble 36</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 9 | 13 | 22 |
| 2 | 7 | 6 | 13 | 22 |
| 3 | 10 | 10 | 14 | 22 |
| 4 | 8 | 8 | 14 | 22 |
| 5 | 8 | 8 | 14 | 24 |
| 6 | 9 | 10 | 14 | 24 |
| 7 | 10 | 10 | 14 | 25 |
| 8 | 12 | 12 | 16 | 26 |

Best on the page: **22 moves**, from DR 1 (DRs 2, 3 and 4 tie it): `F2 R2 F2 D2 R B2 D2 R2 U2 L' F2 L D2 U' R' U' R' L2 B D2 R L'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 37

```
R' U' F U2 B2 D2 R2 D' L2 D B2 U' L' B' D' U' B' D2 R D R' U2 F' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' L2 B U' B' D2 B' L` | 8 | F/B | 4b2 4e | 2 |
| 2 | `L F2 U (U' R2 D2 R2 B)` | 8 | R/L | 2c4 6e | 2 |
| 3 | `L F2 U (L D2 L' U' B)` | 8 | R/L | 2c4 2e | 2 |
| 4 | `L F2 U (U' L2 D2 L2 B)` | 8 | R/L | 2c4 6e | 3 |
| 5 | `D2 L B2 U' L (D2 F U' B' U F)` | 11 | U/D | 4b2 2e | 1 |
| 6 | `L F2 U (U R B' R2 F R U2 B)` | 11 | R/L | 4a2 4e | 5 |
| 7 | `L F2 U (U' F U2 B' U2 R2 D2 B)` | 11 | R/L | 2c4 6e | 1 |
| 8 | `D2 R2 F2 U' L2 D L (B2 U' D2 B)` | 11 | U/D | 4c3 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-3 | 4b2-1 | look anyway | 1.6% | 8.8% | 38% |
| 2 | 2c4-4 | 2c4-3 | look anyway | 0.17% | 1.2% | 8.1% |
| 3 | 2c4-4 | 2c4-1 | look anyway | 0.19% | 1.7% | 12% |
| 4 | 2c4-4 | 2c4-3 | look anyway | 0.25% | 1.8% | 10% |
| 5 | 4b2-2 | 4b2-1 | keep | 1.9% | 9.9% | 40% |
| 6 | 4a2-2 | 4a2-1 | keep | 12% | 32% | 68% |
| 7 | 2c4-4 | 2c4-3 | drop | 0.07% | 0.66% | 5.4% |
| 8 | 4c3-4 | 4c3-9 | drop | 0.05% | 0.54% | 3.8% |

Shown: 8 of the 1,382 DRs up to 11 moves (8 moves: 4 of 6; 9 moves: 0 of 11; 10 moves: 0 of 134; 11 moves: 4 of 1,231).

<details>
<summary>Answers for scramble 37</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 6 | 7 | 14 | 21 |
| 2 | 9 | 8 | 15 | 22 |
| 3 | 9 | 8 | 13 | 20 |
| 4 | 9 | 8 | 14 | 21 |
| 5 | 6 | 6 | 13 | 23 |
| 6 | 7 | 8 | 14 | 24 |
| 7 | 9 | 8 | 14 | 24 |
| 8 | 9 | 10 | 14 | 23 |

Best on the page: **20 moves**, from DR 3: `L F2 U' L2 U2 R' D2 L' D2 L B2 U2 B2 U2 L' B' U L D2 L'`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 38

```
R' U' F D B2 D2 L2 U L2 B2 U' L2 D2 F' R D' U2 F B' D' L B2 D2 B' U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `R' F' R' U' L R2 F2 B R2 U' F` | 11 | U/D | 4c4 4e | 2 |
| 2 | `F L' B2 D' L2 R F2 B L2 D' F` | 11 | U/D | 4b5 2e | 2 |
| 3 | `R' F' R' U' L (F' D F R2 F' U)` | 11 | F/B | 4b2 4e | 1 |
| 4 | `D F' L' B (B' D R2 U D' L D)` | 11 | R/L | 4c4 2e | 5 |
| 5 | `R' F' R' U' L (R2 U' B2 L2 F' U)` | 11 | F/B | 4b2 4e | 3 |
| 6 | `R' F R' U' L (B' D R2 U' F' U)` | 11 | F/B | 4b2 2e | 2 |
| 7 | `F L' B2 D' R (B2 U' R2 U F' D)` | 11 | F/B | 2c4 6e | 1 |
| 8 | `L U (F U D F' L F R' F2 R)` | 11 | F/B | 2c4 2e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-2 | 4c4-3 | drop | 0.05% | 0.51% | 2.9% |
| 2 | 4b5-1 | 4b5-1 | drop | 0.02% | 0.24% | 2.3% |
| 3 | 4b2-2 | 4b2-3 | keep | 0.68% | 5.1% | 26% |
| 4 | 4c4-1 | 4c4-2 | drop | 0.80% | 3.3% | 16% |
| 5 | 4b2-3 | 4b2-3 | keep | 1.2% | 7.9% | 35% |
| 6 | 4b2-4 | 4b2-2 | keep | 1.7% | 8.7% | 35% |
| 7 | 2c4-7 | 2c4-1 | drop | 0.01% | 0.47% | 5.0% |
| 8 | 2c4-2 | 2c4-6 | drop | 0.22% | 1.9% | 11% |

Shown: 8 of the 23 DRs up to 11 moves (11 moves: 8 of 23).

<details>
<summary>Answers for scramble 38</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 11 | 13 | 24 |
| 2 | 10 | 10 | 15 | 26 |
| 3 | 7 | 7 | 12 | 22 |
| 4 | 11 | 9 | 13 | 24 |
| 5 | 7 | 7 | 11 | 22 |
| 6 | 7 | 7 | 13 | 23 |
| 7 | 10 | 8 | 13 | 24 |
| 8 | 9 | 9 | 13 | 23 |

Best on the page: **22 moves**, from DR 3 (DR 5 ties it): `R' F' R' U' L' B' U2 R2 D2 U2 B R2 F2 U2 F2 D2 U' F R2 F' D' F`. The list drops 5 of the 8 DRs of 11 moves or more, and keeps the best one.

</details>

#### Scramble 39

```
R' U' F D2 F2 D F2 U R2 F2 D R2 U2 B' D' L D2 F2 D' F2 U2 R D U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F B R (L' U F2 D' B' L2 U)` | 10 | F/B | 2c4 6e | 2 |
| 2 | `D' B' R U' F2 D2 R B' R' F` | 10 | R/L | 4c4 4e | 1 |
| 3 | `B' R' F' U2 D2 L (L' D B' U)` | 10 | F/B | 2c4 6e | 2 |
| 4 | `F B R (L D R2 U' F R2 U)` | 10 | F/B | 4c4 2e | 2 |
| 5 | `D' B' R U' F2 D2 L2 R' F' R' B` | 11 | R/L | 4c4 4e | 1 |
| 6 | `L2 B' R' F' U2 D2 L (L' D B' U)` | 11 | F/B | 4c4 2e | 1 |
| 7 | `D' B' R U' R2 B2 U2 R F' R' B` | 11 | R/L | 4c4 2e | 2 |
| 8 | `R2 F B R (L D R2 U' F R2 U)` | 11 | F/B | 4c4 2e | 4 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-5 | 2c4-3 | look anyway | 0.25% | 1.7% | 11% |
| 2 | 4c4-2 | 4c4-1 | look anyway | 0.12% | 0.66% | 4.3% |
| 3 | 2c4-7 | 2c4-7 | look anyway | 0 | 0.01% | 0.40% |
| 4 | 4c4-3 | 4c4-4 | look anyway | 0 | 0.05% | 0.96% |
| 5 | 4c4-2 | 4c4-1 | drop | 0.12% | 0.66% | 4.3% |
| 6 | 4c4-4 | 4c4-3 | drop | 0 | 0.03% | 0.54% |
| 7 | 4c4-2 | 4c4-1 | drop | 0.09% | 0.93% | 5.2% |
| 8 | 4c4-3 | 4c4-4 | drop | 0 | 0.27% | 2.6% |

Shown: 8 of the 106 DRs up to 11 moves (10 moves: 4 of 4; 11 moves: 4 of 102).

<details>
<summary>Answers for scramble 39</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 14 | 23 |
| 2 | 10 | 9 | 14 | 24 |
| 3 | 10 | 10 | 14 | 24 |
| 4 | 10 | 10 | 15 | 24 |
| 5 | 9 | 10 | 14 | 25 |
| 6 | 11 | 10 | 14 | 25 |
| 7 | 9 | 9 | 15 | 26 |
| 8 | 11 | 10 | 14 | 24 |

Best on the page: **23 moves**, from DR 1: `F B R F' R2 B D2 F' D2 F2 R2 F' R2 B2 D2 R2 U L2 B D F2 U' L`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 40

```
R' U' F U2 B2 R2 B2 U R2 U F2 D' U2 R F' U' R' D2 L2 B' U2 B' R' F' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `B' L D L2 B U F (F2 B2 L)` | 10 | U/D | 2c4 6e | 1 |
| 2 | `B R (F2 R' D2 L2 D' B U' F)` | 10 | U/D | 4c4 4e | 2 |
| 3 | `R' B R U' B R2 D R2 F (R)` | 10 | U/D | 4b5 2e | 1 |
| 4 | `R' B R U' B' R2 D R2 F (R)` | 10 | U/D | 4b5 2e | 2 |
| 5 | `U' L' U2 R' D R (U' F' L R' B)` | 11 | U/D | 4b5 2e | 0 |
| 6 | `D' L2 B2 L2 B2 U (R U L' F L)` | 11 | F/B | 4b2 4e | 2 |
| 7 | `U' F2 L2 F2 L2 D (R U' L' F L)` | 11 | F/B | 2c4 4e | 4 |
| 8 | `B R (F2 R' D2 L2 U2 D' F U' B)` | 11 | U/D | 4a2 2e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-2 | 2c4-2 | look anyway | 0.05% | 1.8% | 13% |
| 2 | 4c4-4 | 4c4-1 | look anyway | <0.01% | 0.35% | 3.3% |
| 3 | 4b5-1 | 4b5-1 | look anyway | <0.01% | 0.08% | 1.2% |
| 4 | 4b5-1 | 4b5-1 | look anyway | 0.02% | 0.24% | 2.3% |
| 5 | 4b5-2 | 4b5-2 | drop | 0 | 0.02% | 0.31% |
| 6 | 4b2-2 | 4b2-3 | keep | 1.2% | 7.6% | 34% |
| 7 | 2c4-3 | 2c4-1 | keep | 1.5% | 7.8% | 32% |
| 8 | 4a2-1 | 4a2-1 | keep | 1.7% | 7.9% | 31% |

Shown: 8 of the 175 DRs up to 11 moves (10 moves: 4 of 10; 11 moves: 4 of 165).

<details>
<summary>Answers for scramble 40</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 14 | 22 |
| 2 | 11 | 10 | 13 | 23 |
| 3 | 10 | 10 | 14 | 24 |
| 4 | 10 | 9 | 12 | 21 |
| 5 | 10 | 10 | 15 | 25 |
| 6 | 8 | 7 | 13 | 23 |
| 7 | 8 | 7 | 13 | 24 |
| 8 | 8 | 9 | 12 | 23 |

Best on the page: **21 moves**, from DR 4: `R' B R U' B' R2 D R2 F' B2 D' F2 L2 U F2 U' F2 D B2 D' R'`. The list drops 1 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 41

```
R' U' F D2 R2 U R2 B2 D U2 F2 U L' R2 F' L2 U' R' B U' L2 R' U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L R (U' R F2 R2 B' L2 U)` | 9 | F/B | 2c5 6e | 1 |
| 2 | `(B' R D' R' U' D2 R F' U2 B)` | 10 | R/L | 2c3 4e | 4 |
| 3 | `(U' D' L' B' D' F R U2 B2 R)` | 10 | F/B | 2c3 0e | 3 |
| 4 | `(U2 B' U' R D' L2 B L D2 R)` | 10 | F/B | 2c4 2e | 3 |
| 5 | `U2 L R (U' R F2 D2 R2 B' L2 U)` | 11 | F/B | 2c5 4e | 1 |
| 6 | `(U' R B D B' R' F2 U2 L U2 F)` | 11 | R/L | 4c3 4e | 4 |
| 7 | `(U' D' L' B' D R' D2 F R F2 L)` | 11 | F/B | 2c4 6e | 2 |
| 8 | `L R (U' R' F2 R2 F' D2 F' B D)` | 11 | F/B | 2c5 6e | 5 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c5-2 | 2c5-1 | look anyway | 0 | 0.16% | 1.5% |
| 2 | 2c3-3 | 2c3-3 | look anyway | 1.2% | 6.2% | 26% |
| 3 | 2c3-1 | 2c3-1 | look anyway | 0.15% | 2.7% | 25% |
| 4 | 2c4-4 | 2c4-5 | look anyway | 0.02% | 0.81% | 7.2% |
| 5 | 2c5-2 | 2c5-1 | drop | 0 | 0.05% | 1.2% |
| 6 | 4c3-4 | 4c3-7 | keep | 0.81% | 3.4% | 16% |
| 7 | 2c4-4 | 2c4-5 | drop | 0.03% | 0.73% | 5.4% |
| 8 | 2c5-2 | 2c5-2 | drop | 0 | 0 | 0.65% |

Shown: 8 of the 186 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 24; 11 moves: 4 of 161).

<details>
<summary>Answers for scramble 41</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 14 | 23 |
| 2 | 7 | 8 | 13 | 23 |
| 3 | 9 | 9 | 12 | 22 |
| 4 | 9 | 9 | 14 | 23 |
| 5 | 11 | 9 | 15 | 24 |
| 6 | 10 | 10 | 14 | 25 |
| 7 | 9 | 9 | 15 | 25 |
| 8 | 11 | 10 | 14 | 25 |

Best on the page: **22 moves**, from DR 3: `L2 B' D2 B' D2 F D2 F2 U2 F R2 F' R' B2 U2 R' F' D B L D U`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 42

```
R' U' F D2 U' B2 U R2 D' R2 B2 U' R' B2 D2 B2 F' U R2 D' R' B' L' U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `B L' D' F2 D' B L D2 R B` | 10 | R/L | 2c4 2e | 4 |
| 2 | `U' R2 U (F2 L2 B' R' U2 D2 B)` | 10 | R/L | 4c3 4e | 0 |
| 3 | `U' B2 R2 B2 U (F B2 U2 R' B)` | 10 | R/L | 2c3 2e | 2 |
| 4 | `L2 U' R2 U' F' L' F' R' U2 B` | 10 | R/L | 2c3 6e | 1 |
| 5 | `B2 U' R2 U R2 B2 R' B2 D2 B' L` | 11 | F/B | 4b5 4e | 4 |
| 6 | `(L2 F' D2 L B' U2 R2 B2 D' L' D)` | 11 | R/L | 2c4 4e | 1 |
| 7 | `D' F2 D (L2 U2 F B2 R U2 R2 B)` | 11 | R/L | 4b5 4e | 2 |
| 8 | `B' L' D' F2 D' B L' R2 U2 R F` | 11 | R/L | 2c4 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-7 | 2c4-5 | look anyway | 0 | 0.08% | 2.1% |
| 2 | 4c3-4 | 4c3-1 | look anyway | 0.31% | 2.3% | 13% |
| 3 | 2c3-2 | 2c3-2 | look anyway | 1.6% | 9.2% | 39% |
| 4 | 2c3-2 | 2c3-1 | look anyway | 0.58% | 4.1% | 23% |
| 5 | 4b5-1 | 4b5-1 | drop | 0.06% | 0.66% | 5.8% |
| 6 | 2c4-5 | 2c4-1 | drop | 0.05% | 0.84% | 7.6% |
| 7 | 4b5-1 | 4b5-2 | drop | 0 | 0.07% | 1.0% |
| 8 | 2c4-7 | 2c4-2 | drop | 0.03% | 0.45% | 4.4% |

Shown: 8 of the 603 DRs up to 11 moves (10 moves: 4 of 42; 11 moves: 4 of 561).

<details>
<summary>Answers for scramble 42</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 9 | 14 | 24 |
| 2 | 10 | 9 | 14 | 23 |
| 3 | 7 | 7 | 14 | 23 |
| 4 | 9 | 8 | 12 | 22 |
| 5 | 10 | 9 | 12 | 23 |
| 6 | 10 | 9 | 14 | 25 |
| 7 | 11 | 10 | 14 | 25 |
| 8 | 9 | 9 | 13 | 24 |

Best on the page: **22 moves**, from DR 4: `L2 U' R2 U' F' L' F' R' U2 B R U2 L' B2 R' U2 B2 R F2 R D2 B2`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 43

```
R' U' F U B2 R2 F2 U' L2 D B2 U B2 R D2 F' L F' U2 F' D2 U F' U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(F U' R D2 F D R2 U' L)` | 9 | U/D | 2c3 6e | 2 |
| 2 | `(R' U D L F2 B L2 F' U' F)` | 10 | U/D | 4b2 2e | 3 |
| 3 | `U B R (B2 R U F U R2 F)` | 10 | U/D | 2c4 4e | 1 |
| 4 | `U F2 B' D L' D' R (U D2 F)` | 10 | U/D | 4b2 4e | 2 |
| 5 | `R U' B' D2 F R U L D2 R U` | 11 | R/L | 4b5 2e | 2 |
| 6 | `(R U D L' B2 D F D R2 U' F)` | 11 | U/D | 2c3 4e | 0 |
| 7 | `U B U2 R (R D2 L2 U' F2 B D)` | 11 | F/B | 4a1 2e | 2 |
| 8 | `U B U2 R (R' D2 L2 U F2 B D)` | 11 | F/B | 4a1 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-1 | 2c3-3 | look anyway | 0.47% | 3.6% | 22% |
| 2 | 4b2-1 | 4b2-4 | look anyway | 3.5% | 15% | 48% |
| 3 | 2c4-6 | 2c4-1 | look anyway | 0.09% | 0.94% | 7.2% |
| 4 | 4b2-4 | 4b2-3 | look anyway | 0.46% | 3.8% | 23% |
| 5 | 4b5-1 | 4b5-1 | drop | 0.02% | 0.24% | 2.3% |
| 6 | 2c3-1 | 2c3-1 | keep | 1.0% | 6.6% | 31% |
| 7 | 4a1-3 | 4a1-4 | keep | 0.59% | 5.0% | 27% |
| 8 | 4a1-3 | 4a1-4 | keep | 3.7% | 17% | 51% |

Shown: 8 of the 172 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 18; 11 moves: 4 of 153).

<details>
<summary>Answers for scramble 43</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 12 | 21 |
| 2 | 6 | 6 | 13 | 22 |
| 3 | 10 | 8 | 14 | 24 |
| 4 | 7 | 8 | 13 | 22 |
| 5 | 10 | 10 | 15 | 25 |
| 6 | 7 | 8 | 14 | 24 |
| 7 | 7 | 7 | 12 | 23 |
| 8 | 7 | 4 | 14 | 24 |

Best on the page: **21 moves**, from DR 1: `D2 F2 B2 D' L2 B2 D' R2 F2 B2 D F2 L' U R2 D' F' D2 R' U F'`. The list drops 1 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 44

```
R' U' F D' B2 U B2 D' F2 U2 B2 R' B2 R' B U F L' F' R2 B F' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' D' L U2 R' B' L (R U D)` | 10 | F/B | 2c5 4e | 2 |
| 2 | `R U F' B' D F (D2 L D' L)` | 10 | U/D | 4b5 2e | 2 |
| 3 | `U' D' L U2 R' B' L (R' U D)` | 10 | F/B | 2c5 4e | 2 |
| 4 | `(B2 L2 B U' D L2 B L B2 R)` | 10 | F/B | 2c4 4e | 1 |
| 5 | `(B' U' L B D R2 F L2 B' U2 B)` | 11 | R/L | 2c4 2e | 1 |
| 6 | `(B U2 D F U' R' U2 F' L2 B' R)` | 11 | F/B | 2c4 2e | 1 |
| 7 | `L R (L U F B' U' D F' D' F)` | 11 | U/D | 0c3 6e | 1 |
| 8 | `B2 U' L2 B (B R' D R F2 D R)` | 11 | U/D | 2c4 4e | 0 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c5-1 | 2c5-2 | look anyway | 0.02% | 0.23% | 2.4% |
| 2 | 4b5-1 | 4b5-2 | look anyway | 0.01% | 0.14% | 1.4% |
| 3 | 2c5-1 | 2c5-2 | look anyway | 0.02% | 0.23% | 2.4% |
| 4 | 2c4-1 | 2c4-7 | look anyway | 0.02% | 0.48% | 4.7% |
| 5 | 2c4-3 | 2c4-3 | keep | 0.07% | 1.4% | 9.3% |
| 6 | 2c4-1 | 2c4-2 | keep | 0.16% | 2.0% | 16% |
| 7 | 0c3-1 | 0c3-2 | drop | 0.10% | 0.89% | 4.3% |
| 8 | 2c4-2 | 2c4-6 | drop | 0.05% | 0.62% | 5.1% |

Shown: 8 of the 127 DRs up to 11 moves (10 moves: 4 of 12; 11 moves: 4 of 115).

<details>
<summary>Answers for scramble 44</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 10 | 12 | 22 |
| 2 | 9 | 10 | 15 | 25 |
| 3 | 10 | 10 | 14 | 23 |
| 4 | 9 | 10 | 15 | 25 |
| 5 | 10 | 8 | 15 | 26 |
| 6 | 9 | 9 | 14 | 25 |
| 7 | 11 | 10 | 14 | 24 |
| 8 | 8 | 8 | 12 | 23 |

Best on the page: **22 moves**, from DR 1: `U' D' L U2 R' B' L D2 B' U2 L2 B' D2 F L2 F' U2 F L2 D' U' R'`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 45

```
R' U' F U2 R2 F2 U' B2 D' R2 D' L2 U2 L' U B U B R U2 F' D' U F' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `D' L R2 F D (B' L F R' F)` | 10 | R/L | 4c4 4e | 0 |
| 2 | `U2 L' D2 B R' F2 U F2 D' B` | 10 | U/D | 4b5 2e | 2 |
| 3 | `L (B D2 F R F2 B' U D2 B)` | 10 | U/D | 4b2 4e | 1 |
| 4 | `B' U' L2 F' D (L R' U' F2 R)` | 10 | F/B | 4b5 2e | 4 |
| 5 | `U2 F2 D' L2 U' F (L R' F U' R)` | 11 | U/D | 4b5 2e | 1 |
| 6 | `D' B R' B2 L (F D L2 D' B U)` | 11 | F/B | 2c4 4e | 0 |
| 7 | `F' D F' U2 R B D2 L (U2 F U)` | 11 | F/B | 2c3 6e | 0 |
| 8 | `D' L' D' B' U' F2 D' B (U2 B' L)` | 11 | U/D | 2c4 6e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-4 | 4c4-3 | look anyway | 0 | 0.02% | 0.67% |
| 2 | 4b5-1 | 4b5-2 | look anyway | 0.01% | 0.14% | 1.4% |
| 3 | 4b2-3 | 4b2-1 | look anyway | 1.1% | 6.6% | 31% |
| 4 | 4b5-1 | 4b5-1 | look anyway | 0.11% | 0.72% | 5.4% |
| 5 | 4b5-2 | 4b5-1 | drop | 0 | 0.05% | 0.78% |
| 6 | 2c4-7 | 2c4-7 | drop | 0 | 0 | 0.21% |
| 7 | 2c3-2 | 2c3-3 | keep | 0.14% | 1.3% | 9.5% |
| 8 | 2c4-3 | 2c4-4 | drop | 0.07% | 0.66% | 5.4% |

Shown: 8 of the 85 DRs up to 11 moves (10 moves: 4 of 7; 11 moves: 4 of 78).

<details>
<summary>Answers for scramble 45</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 15 | 25 |
| 2 | 10 | 11 | 14 | 24 |
| 3 | 8 | 7 | 12 | 21 |
| 4 | 10 | 9 | 12 | 22 |
| 5 | 10 | 9 | 15 | 25 |
| 6 | 10 | 9 | 15 | 25 |
| 7 | 7 | 8 | 15 | 25 |
| 8 | 8 | 9 | 14 | 25 |

Best on the page: **21 moves**, from DR 3: `L' B2 R2 U2 B2 D' F2 B2 R2 B2 D F2 B D2 U' B F2 R' F' D2 B'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 46

```
R' U' F U R L U R2 D2 B U R U2 L F B2 U' B2 D' F2 U' R2 F2 U' B2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `D2 R2 B2 U D2 R B' D2 L` | 9 | F/B | 4b5 4e | 1 |
| 2 | `U2 L2 F2 U D2 L F' D2 R` | 9 | F/B | 4b5 2e | 0 |
| 3 | `D L F' B' L (U2 L' F' U)` | 9 | F/B | 4a1 4e | 1 |
| 4 | `R' U B' L2 U R' D R' D` | 9 | R/L | 2c3 4e | 0 |
| 5 | `R2 U2 F2 L2 U (R' F2 L F' D2 R)` | 11 | F/B | 2c4 6e | 1 |
| 6 | `R' U B R' B2 L2 R' D' L2 F2 D` | 11 | R/L | 4b2 2e | 2 |
| 7 | `R2 D2 B2 R2 U (R' F2 L F' D2 R)` | 11 | F/B | 2c4 6e | 2 |
| 8 | `D2 B2 R2 U B2 L2 R2 B' L' D2 B` | 11 | R/L | 2c5 6e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b5-1 | 4b5-1 | look anyway | <0.01% | 0.08% | 1.1% |
| 2 | 4b5-1 | 4b5-1 | look anyway | 0 | 0.06% | 0.76% |
| 3 | 4a1-2 | 4a1-2 | look anyway | 3.6% | 14% | 46% |
| 4 | 2c3-2 | 2c3-1 | look anyway | 0.59% | 4.4% | 24% |
| 5 | 2c4-2 | 2c4-7 | drop | 0 | 0.07% | 2.2% |
| 6 | 4b2-3 | 4b2-1 | keep | 2.7% | 12% | 42% |
| 7 | 2c4-2 | 2c4-7 | drop | 0 | 0.24% | 4.5% |
| 8 | 2c5-1 | 2c5-1 | drop | 0.05% | 0.29% | 2.5% |

Shown: 8 of the 1,013 DRs up to 11 moves (9 moves: 4 of 6; 10 moves: 0 of 77; 11 moves: 4 of 930).

<details>
<summary>Answers for scramble 46</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 14 | 23 |
| 2 | 10 | 9 | 15 | 23 |
| 3 | 6 | 6 | 12 | 21 |
| 4 | 8 | 7 | 13 | 22 |
| 5 | 9 | 10 | 13 | 24 |
| 6 | 7 | 6 | 13 | 24 |
| 7 | 9 | 10 | 14 | 24 |
| 8 | 10 | 10 | 14 | 25 |

Best on the page: **21 moves**, from DR 3: `D L F' B' L F2 U2 F2 D2 B2 R2 F' L2 U2 R2 B2 D2 U' F L U2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 47

```
R' U' F U B2 D R2 U2 R2 B2 R2 F2 D F' R D R2 D L2 B' D' F' B' D2 U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `B' R B L R2 F' B2 D` | 8 | F/B | 4b2 2e | 2 |
| 2 | `L' B' R' D2 F' R2 U' D2 F` | 9 | U/D | 4c4 2e | 1 |
| 3 | `L' B' L2 R' U2 B L2 U' F` | 9 | U/D | 4c4 4e | 2 |
| 4 | `L' B' R (U2 D2 R2 F2 B' D)` | 9 | F/B | 2c3 6e | 0 |
| 5 | `L' U2 F2 D2 F B' U (B R2 F' L)` | 11 | F/B | 2c3 4e | 2 |
| 6 | `B' R' B L (U F' B D L2 R2 B)` | 11 | U/D | 4c3 2e | 2 |
| 7 | `B2 R B' L' R2 F' B U' R2 D' F` | 11 | U/D | 4c4 2e | 0 |
| 8 | `L' B' R' F' B2 D B2 U2 L2 U' B` | 11 | U/D | 2c5 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-1 | 4b2-1 | look anyway | 5.0% | 20% | 55% |
| 2 | 4c4-1 | 4c4-4 | look anyway | 0 | 0.14% | 1.8% |
| 3 | 4c4-1 | 4c4-4 | look anyway | <0.01% | 0.35% | 3.3% |
| 4 | 2c3-3 | 2c3-2 | look anyway | 0.14% | 1.3% | 9.5% |
| 5 | 2c3-3 | 2c3-3 | keep | 0.35% | 2.6% | 15% |
| 6 | 4c3-9 | 4c3-5 | drop | <0.01% | 0.21% | 2.6% |
| 7 | 4c4-1 | 4c4-4 | drop | 0 | 0.07% | 1.3% |
| 8 | 2c5-2 | 2c5-1 | drop | 0.02% | 0.23% | 2.4% |

Shown: 8 of the 1,074 DRs up to 11 moves (8 moves: 1 of 1; 9 moves: 3 of 4; 10 moves: 0 of 84; 11 moves: 4 of 985).

<details>
<summary>Answers for scramble 47</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 3 | 13 | 21 |
| 2 | 11 | 11 | 14 | 23 |
| 3 | 9 | 11 | 15 | 24 |
| 4 | 8 | 9 | 13 | 22 |
| 5 | 8 | 8 | 15 | 25 |
| 6 | 10 | 9 | 13 | 24 |
| 7 | 9 | 11 | 14 | 25 |
| 8 | 10 | 10 | 15 | 25 |

Best on the page: **21 moves**, from DR 1: `B' R B L R2 F' B2 D F D2 F2 D2 F U2 B' U2 L2 U2 F' L2 U2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 48

```
R' U' F U L2 B2 D B2 D F2 D2 B2 R2 F' R' B' D' U R U B2 U L2 F' U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(B2 U2 L' B2 L B' U' D' F)` | 9 | U/D | 2c5 4e | 1 |
| 2 | `(B2 U2 L' B2 L B U' D' F)` | 9 | U/D | 2c5 4e | 2 |
| 3 | `(R B2 R F' U' F B D' F)` | 9 | U/D | 2c3 4e | 1 |
| 4 | `(R B2 R U2 B' U' B2 D' F)` | 9 | U/D | 4c3 2e | 1 |
| 5 | `(L U2 L' B2 L2 D2 F' D' F2 U' B)` | 11 | U/D | 4b5 4e | 0 |
| 6 | `(F' R B2 R' B2 D F2 L2 U' B U)` | 11 | F/B | 2c4 6e | 0 |
| 7 | `(R B2 L2 R' U2 F2 B' D' B2 U' F)` | 11 | U/D | 4c3 4e | 1 |
| 8 | `R F' B R' B' R (D' L2 F B' U)` | 11 | F/B | 4c3 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c5-1 | 2c5-1 | look anyway | <0.01% | 0.23% | 2.7% |
| 2 | 2c5-1 | 2c5-2 | look anyway | 0.02% | 0.23% | 2.4% |
| 3 | 2c3-1 | 2c3-3 | look anyway | 0.62% | 4.5% | 24% |
| 4 | 4c3-4 | 4c3-9 | look anyway | 0.06% | 0.56% | 3.7% |
| 5 | 4b5-1 | 4b5-2 | drop | 0 | <0.01% | 0.32% |
| 6 | 2c4-5 | 2c4-4 | drop | 0.03% | 0.27% | 2.7% |
| 7 | 4c3-5 | 4c3-9 | drop | 0 | 0.10% | 1.9% |
| 8 | 4c3-2 | 4c3-4 | keep | 0.74% | 4.9% | 22% |

Shown: 8 of the 958 DRs up to 11 moves (9 moves: 4 of 7; 10 moves: 0 of 97; 11 moves: 4 of 854).

<details>
<summary>Answers for scramble 48</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 10 | 15 | 23 |
| 2 | 10 | 11 | 13 | 22 |
| 3 | 8 | 7 | 14 | 22 |
| 4 | 8 | 10 | 14 | 23 |
| 5 | 10 | 10 | 15 | 26 |
| 6 | 10 | 9 | 14 | 25 |
| 7 | 9 | 10 | 14 | 25 |
| 8 | 8 | 8 | 13 | 24 |

Best on the page: **22 moves**, from DR 2 (DR 3 ties it): `D' L2 U F2 L2 F2 R2 U B2 D' R2 U L2 F' D U B' L' B2 L U2 B2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 49

```
R' U' F L' D' R L' U2 L2 F' U2 D' B L' U F2 D' B2 L2 F2 U2 R2 D2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' L2 R' U F' B2 D' F2 L` | 9 | U/D | 4c4 4e | 3 |
| 2 | `(U F' L D' L' D' F2 D' L)` | 9 | U/D | 0c0 2e | 3 |
| 3 | `(U F B2 D L2 U R' F2 L)` | 9 | U/D | 4a2 4e | 1 |
| 4 | `B' L2 R2 F (D R U D2 L)` | 9 | U/D | 4c4 2e | 1 |
| 5 | `U' L2 R' U F' L2 F2 U' D2 F2 R` | 11 | U/D | 4c4 4e | 6 |
| 6 | `(U F D' L' D' R' U F2 B2 D' L)` | 11 | U/D | 4b5 4e | 0 |
| 7 | `B2 D B2 R B2 D (F2 U L D F)` | 11 | R/L | 2c3 6e | 2 |
| 8 | `U' R2 B2 U' R' F2 D (R' F2 D' F)` | 11 | R/L | 2c3 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-4 | 4c4-5 | look anyway | 0 | <0.01% | 0.44% |
| 2 | 0c0-1 | 0c0-1 | look anyway | 12% | 38% | 81% |
| 3 | 4a2-3 | 4a2-3 | look anyway | 0.06% | 1.1% | 8.2% |
| 4 | 4c4-2 | 4c4-6 | look anyway | 0 | 0.08% | 1.2% |
| 5 | 4c4-2 | 4c4-5 | drop | 0 | 0.31% | 4.8% |
| 6 | 4b5-1 | 4b5-2 | drop | 0 | <0.01% | 0.32% |
| 7 | 2c3-2 | 2c3-3 | keep | 0.33% | 2.5% | 15% |
| 8 | 2c3-3 | 2c3-3 | keep | 0.19% | 1.6% | 11% |

Shown: 8 of the 1,843 DRs up to 11 moves (9 moves: 4 of 16; 10 moves: 0 of 163; 11 moves: 4 of 1,664).

<details>
<summary>Answers for scramble 49</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 11 | 14 | 23 |
| 2 | 6 | 5 | 12 | 20 |
| 3 | 7 | 8 | 12 | 20 |
| 4 | 11 | 11 | 13 | 22 |
| 5 | 9 | 11 | 14 | 25 |
| 6 | 11 | 10 | 15 | 26 |
| 7 | 7 | 9 | 13 | 24 |
| 8 | 8 | 9 | 15 | 25 |

Best on the page: **20 moves**, from DR 2 (DR 3 ties it): `F2 U L2 F2 L2 U F2 D2 R2 B2 D2 L D F2 D L D L' F U'`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 50

```
R' U' F L B' D' B2 R2 B2 R D R2 F' R F2 U' F2 U R2 B2 D' B2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U F B L' B2 R (U' D2 F' D)` | 10 | F/B | 4b2 2e | 2 |
| 2 | `F U (D' R2 U' F' L F R2 B)` | 10 | R/L | 4c4 4e | 3 |
| 3 | `(U' L' F' L' D B' R' B2 L' F)` | 10 | R/L | 2c3 4e | 1 |
| 4 | `D' F R2 F2 L U R (L F B)` | 10 | U/D | 4b2 4e | 2 |
| 5 | `(U' L' F' L' D F2 B L' B2 R' F)` | 11 | R/L | 2c3 4e | 1 |
| 6 | `U' L2 F B' R B2 L (U' D2 F' D)` | 11 | F/B | 4c4 2e | 3 |
| 7 | `U' D2 F B L' U2 R (U' D2 F' D)` | 11 | F/B | 4b2 2e | 1 |
| 8 | `U' L2 F B' L U2 R (U' D2 F' D)` | 11 | F/B | 4c4 2e | 5 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-2 | 4b2-3 | look anyway | 2.0% | 9.6% | 38% |
| 2 | 4c4-2 | 4c4-1 | look anyway | 0.18% | 1.2% | 6.7% |
| 3 | 2c3-2 | 2c3-2 | look anyway | 0.49% | 3.9% | 21% |
| 4 | 4b2-3 | 4b2-2 | look anyway | 1.2% | 7.6% | 34% |
| 5 | 2c3-2 | 2c3-2 | keep | 0.49% | 3.9% | 21% |
| 6 | 4c4-1 | 4c4-4 | drop | 0.02% | 0.48% | 3.8% |
| 7 | 4b2-2 | 4b2-3 | keep | 1.2% | 7.0% | 31% |
| 8 | 4c4-1 | 4c4-4 | drop | 0.17% | 2.0% | 12% |

Shown: 8 of the 60 DRs up to 11 moves (10 moves: 4 of 9; 11 moves: 4 of 51).

<details>
<summary>Answers for scramble 50</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 14 | 23 |
| 2 | 10 | 10 | 14 | 23 |
| 3 | 6 | 7 | 13 | 23 |
| 4 | 9 | 8 | 14 | 23 |
| 5 | 8 | 7 | 13 | 23 |
| 6 | 10 | 11 | 14 | 25 |
| 7 | 7 | 7 | 14 | 23 |
| 8 | 11 | 11 | 14 | 25 |

Best on the page: **23 moves**, from DR 1 (DRs 2, 3, 4, 5 and 7 tie it): `U F B L' B2 R L2 D2 F' L2 U2 F2 L2 F U2 R2 F L2 F' D F D2 U`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 51

```
R' U' F U F2 L2 U R2 B2 F2 U' F2 U' R' B' U' B R D2 B L2 F' U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(F2 L U2 D' R U D' B D)` | 9 | F/B | 2c3 4e | 2 |
| 2 | `B' L2 D B (D B2 L R' D R)` | 10 | U/D | 2c4 4e | 2 |
| 3 | `B' U L' U R2 D (U' R D' B)` | 10 | R/L | 4c3 2e | 1 |
| 4 | `(F2 L U2 D' R' U D' F2 B D)` | 10 | F/B | 2c3 4e | 2 |
| 5 | `R U' R (B2 L' D B U' D2 F U)` | 11 | F/B | 4b5 2e | 4 |
| 6 | `R D' F U2 R' B' U' B U D B` | 11 | U/D | 2c4 2e | 3 |
| 7 | `U2 R2 U' R' B2 U2 R D2 F (L D)` | 11 | R/L | 2c4 8e | 1 |
| 8 | `U2 R' U B' D F R F2 U2 D2 L` | 11 | F/B | 2c3 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-2 | look anyway | 0.66% | 4.2% | 22% |
| 2 | 2c4-6 | 2c4-2 | look anyway | 0.17% | 1.2% | 8.1% |
| 3 | 4c3-1 | 4c3-5 | look anyway | 0.23% | 2.1% | 15% |
| 4 | 2c3-3 | 2c3-2 | look anyway | 0.66% | 4.2% | 22% |
| 5 | 4b5-1 | 4b5-1 | drop | 0.11% | 0.72% | 5.4% |
| 6 | 2c4-1 | 2c4-3 | keep | 0.84% | 5.5% | 25% |
| 7 | 2c4-2 | 2c4-1 | keep | 0.06% | 1.9% | 14% |
| 8 | 2c3-3 | 2c3-3 | keep | 0.19% | 1.6% | 11% |

Shown: 8 of the 301 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 30; 11 moves: 4 of 270).

<details>
<summary>Answers for scramble 51</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 6 | 8 | 13 | 21 |
| 2 | 9 | 8 | 15 | 24 |
| 3 | 9 | 9 | 13 | 22 |
| 4 | 7 | 7 | 12 | 22 |
| 5 | 10 | 9 | 15 | 25 |
| 6 | 9 | 8 | 12 | 23 |
| 7 | 10 | 9 | 14 | 24 |
| 8 | 8 | 7 | 14 | 25 |

Best on the page: **21 moves**, from DR 1: `F2 R2 B' L2 B R2 B' R2 B2 R2 U2 B2 D B' D U' R' D U2 L' F2`. The list drops 1 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 52

```
R' U' F R2 D' F2 R2 U2 B2 L2 U2 B2 F2 L F R F' R2 U' L2 F2 R' U2 B2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(B R D' B U' L' D2 B)` | 8 | R/L | 2c4 4e | 2 |
| 2 | `F' D' F (L2 D B2 L2 D2 L)` | 9 | U/D | 4c4 2e | 1 |
| 3 | `(B R D' B U' L R2 U2 F)` | 9 | R/L | 2c4 4e | 2 |
| 4 | `(R B' U' B L D L' R D)` | 9 | R/L | 2c4 4e | 2 |
| 5 | `D L' B (B' U2 L2 F2 D2 F2 L D)` | 11 | R/L | 4c3 2e | 4 |
| 6 | `D (D L' R2 D' F2 B2 L' B L B)` | 11 | R/L | 4b5 4e | 3 |
| 7 | `F' B2 D' F' L' U L2 U' F2 R2 U` | 11 | F/B | 2c4 8e | 2 |
| 8 | `F' D' F (L2 F2 B2 U B2 L2 D2 R)` | 11 | U/D | 4c4 2e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-1 | 2c4-5 | look anyway | 0.18% | 1.7% | 12% |
| 2 | 4c4-3 | 4c4-4 | look anyway | 0 | 0.03% | 0.54% |
| 3 | 2c4-1 | 2c4-5 | look anyway | 0.18% | 1.7% | 12% |
| 4 | 2c4-5 | 2c4-6 | look anyway | 0.06% | 0.59% | 4.3% |
| 5 | 4c3-7 | 4c3-4 | keep | 0.75% | 3.3% | 14% |
| 6 | 4b5-2 | 4b5-2 | drop | 0 | 0.01% | 0.79% |
| 7 | 2c4-3 | 2c4-6 | drop | 0.07% | 1.3% | 7.1% |
| 8 | 4c4-3 | 4c4-4 | drop | 0 | 0.03% | 0.54% |

Shown: 8 of the 748 DRs up to 11 moves (8 moves: 1 of 1; 9 moves: 3 of 8; 10 moves: 0 of 88; 11 moves: 4 of 651).

<details>
<summary>Answers for scramble 52</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 9 | 14 | 21 |
| 2 | 10 | 11 | 14 | 23 |
| 3 | 7 | 9 | 13 | 22 |
| 4 | 10 | 10 | 14 | 22 |
| 5 | 9 | 10 | 14 | 24 |
| 6 | 11 | 10 | 14 | 24 |
| 7 | 9 | 10 | 14 | 25 |
| 8 | 10 | 11 | 15 | 26 |

Best on the page: **21 moves**, from DR 1: `L B2 R F2 U2 R U2 R B2 D2 L2 B2 D2 B D2 L U B' D R' B'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 53

```
R' U' F U L2 U B2 R2 U F2 L2 U R' B2 D' U L' F' R2 F' D' B2 F R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `R (R' D2 L' U2 F B D F)` | 9 | U/D | 4b5 4e | 0 |
| 2 | `B D (B2 D F2 B2 R F D2 L)` | 10 | F/B | 4c4 2e | 1 |
| 3 | `R' B' D' R2 U' F' L' U2 B R` | 10 | F/B | 2c4 4e | 2 |
| 4 | `R (R' D2 L' F B' R2 B2 D F)` | 10 | U/D | 4b5 2e | 2 |
| 5 | `(L D' F' U2 L' B2 R2 D2 F2 D F)` | 11 | U/D | 2c4 6e | 3 |
| 6 | `R (L R2 B2 R F' U' L2 F R2 F)` | 11 | U/D | 2c5 8e | 0 |
| 7 | `F B R (L U' F' U2 D' R2 B' U)` | 11 | F/B | 2c5 2e | 5 |
| 8 | `R F B D F U' L2 D (L' F2 R)` | 11 | F/B | 2c3 2e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b5-1 | 4b5-1 | look anyway | 0 | 0.03% | 0.58% |
| 2 | 4c4-1 | 4c4-2 | look anyway | 0.03% | 0.36% | 3.6% |
| 3 | 2c4-4 | 2c4-7 | look anyway | 0.01% | 0.19% | 2.1% |
| 4 | 4b5-1 | 4b5-1 | look anyway | 0.02% | 0.24% | 2.3% |
| 5 | 2c4-7 | 2c4-4 | drop | 0 | 0.18% | 3.1% |
| 6 | 2c5-2 | 2c5-3 | drop | 0 | 0 | 0 |
| 7 | 2c5-1 | 2c5-2 | drop | 0.12% | 1.9% | 10% |
| 8 | 2c3-1 | 2c3-3 | keep | 2.8% | 14% | 51% |

Shown: 8 of the 135 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 12; 11 moves: 4 of 122).

<details>
<summary>Answers for scramble 53</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 10 | 14 | 23 |
| 2 | 9 | 10 | 12 | 22 |
| 3 | 9 | 9 | 14 | 24 |
| 4 | 10 | 10 | 13 | 23 |
| 5 | 10 | 9 | 15 | 25 |
| 6 | 11 | 12 | 16 | 26 |
| 7 | 9 | 10 | 13 | 22 |
| 8 | 8 | 7 | 11 | 21 |

Best on the page: **21 moves**, from DR 8: `R F B D F U' L2 D' L2 B L2 D2 U2 F R2 F' D2 F2 R' F2 L`. The list drops 3 of the 4 DRs of 11 moves or more, and keeps the best one.

</details>

#### Scramble 54

```
R' U' F U' L2 U2 F2 U' L2 R2 U B2 U R D' L' R B L U2 L2 F U L2 U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(R2 B R D' F' L2 F2 D2 R)` | 9 | U/D | 4b2 4e | 4 |
| 2 | `(R2 B R D' F' R2 F2 D2 L)` | 9 | U/D | 4b2 4e | 5 |
| 3 | `L2 U2 B U' L F' L' R B` | 9 | R/L | 4b2 4e | 4 |
| 4 | `(R2 B R D' F' R2 B2 U2 R)` | 9 | U/D | 4b2 4e | 5 |
| 5 | `(L D2 F2 U F2 B2 R' U2 F' B R)` | 11 | F/B | 2c5 4e | 1 |
| 6 | `(F' R2 D B' D' B2 L' U2 F2 D R)` | 11 | U/D | 2c4 8e | 0 |
| 7 | `R' F' L2 U L2 D2 F' D2 R2 B2 R` | 11 | F/B | 4c4 2e | 2 |
| 8 | `D' L2 R' U' B2 D2 L (F' R2 D B)` | 11 | U/D | 2c4 6e | 0 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-3 | 4b2-3 | look anyway | 2.2% | 12% | 44% |
| 2 | 4b2-3 | 4b2-3 | look anyway | 5.2% | 20% | 57% |
| 3 | 4b2-1 | 4b2-2 | look anyway | 6.0% | 24% | 62% |
| 4 | 4b2-3 | 4b2-3 | look anyway | 5.2% | 20% | 57% |
| 5 | 2c5-1 | 2c5-2 | drop | 0 | 0.05% | 1.2% |
| 6 | 2c4-2 | 2c4-2 | keep | 0 | 0.32% | 4.1% |
| 7 | 4c4-4 | 4c4-3 | drop | 0 | 0.05% | 0.96% |
| 8 | 2c4-4 | 2c4-5 | drop | 0.03% | 0.27% | 2.7% |

Shown: 8 of the 719 DRs up to 11 moves (9 moves: 4 of 6; 10 moves: 0 of 84; 11 moves: 4 of 629).

<details>
<summary>Answers for scramble 54</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 13 | 22 |
| 2 | 8 | 9 | 14 | 23 |
| 3 | 7 | 8 | 11 | 20 |
| 4 | 8 | 8 | 12 | 21 |
| 5 | 10 | 10 | 14 | 24 |
| 6 | 10 | 10 | 14 | 24 |
| 7 | 10 | 10 | 15 | 25 |
| 8 | 9 | 9 | 13 | 24 |

Best on the page: **20 moves**, from DR 3: `L2 U2 B U' L F' L' R B R' D2 R F2 U2 B2 R D2 B2 L U2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 55

```
R' U' F D' F2 U2 L2 D F2 U F2 B2 U F B2 D B U F R U2 F D' R' U2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L' U L2 D B L' B2 L D` | 9 | R/L | 2c4 2e | 0 |
| 2 | `U F2 L' F D2 R D' R (B)` | 9 | U/D | 4c4 2e | 1 |
| 3 | `F' D R' F' U' R' D2 F2 D (B)` | 10 | R/L | 2c5 4e | 1 |
| 4 | `B2 U2 L (B' R B2 D2 L2 U B)` | 10 | U/D | 4b2 4e | 2 |
| 5 | `R2 F' U D F (U2 L R' D' F2 L)` | 11 | U/D | 4c3 4e | 0 |
| 6 | `R2 U' B2 D2 F' D (U2 R D' B2 L)` | 11 | F/B | 2c3 6e | 0 |
| 7 | `L' D' R2 U2 B2 U F D (L2 U2 R)` | 11 | F/B | 2c5 0e | 3 |
| 8 | `U F2 L' F' D2 F2 D2 R D' R (B)` | 11 | U/D | 2c4 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-2 | 2c4-1 | look anyway | 0.09% | 1.2% | 11% |
| 2 | 4c4-4 | 4c4-5 | look anyway | 0 | 0 | 0.09% |
| 3 | 2c5-3 | 2c5-1 | look anyway | 0 | <0.01% | 0.37% |
| 4 | 4b2-2 | 4b2-2 | look anyway | 1.9% | 10% | 40% |
| 5 | 4c3-7 | 4c3-5 | drop | 0.04% | 0.56% | 5.1% |
| 6 | 2c3-1 | 2c3-3 | keep | 0.21% | 2.1% | 14% |
| 7 | 2c5-1 | 2c5-1 | drop | 0 | 0.54% | 3.2% |
| 8 | 2c4-7 | 2c4-4 | drop | <0.01% | 0.35% | 3.5% |

Shown: 8 of the 272 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 25; 11 moves: 4 of 245).

<details>
<summary>Answers for scramble 55</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 13 | 22 |
| 2 | 11 | 11 | 16 | 24 |
| 3 | 11 | 10 | 15 | 24 |
| 4 | 7 | 5 | 12 | 22 |
| 5 | 9 | 10 | 14 | 24 |
| 6 | 8 | 9 | 13 | 23 |
| 7 | 10 | 10 | 14 | 25 |
| 8 | 10 | 9 | 15 | 25 |

Best on the page: **22 moves**, from DR 1 (DR 4 ties it): `L' U L2 D B L' B2 L D U2 R' F2 U2 R2 D2 F2 R' F2 U2 L D2 L`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 56

```
R' U' F L2 R2 B2 D2 U' L2 U F2 U L2 F' L U' B D' R B F L' R' B' U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F' U R' B2 L (R B L' F)` | 9 | U/D | 4a1 2e | 1 |
| 2 | `U2 B' L' R B' U' B L2 D` | 9 | F/B | 4a2 2e | 1 |
| 3 | `F' U L' D2 R (R B L' F)` | 9 | U/D | 4a1 2e | 2 |
| 4 | `B' D R2 U' F D' R U L D` | 10 | R/L | 4c4 2e | 2 |
| 5 | `U D F2 D F' D2 B (D' R U' L)` | 11 | U/D | 4c4 4e | 2 |
| 6 | `F (R' B' L' F U L2 D2 F2 R U)` | 11 | R/L | 4c3 2e | 1 |
| 7 | `U2 B' L' R' U' F D2 R2 F U2 F` | 11 | U/D | 2c4 4e | 1 |
| 8 | `B' L' D R D2 F2 L2 U R2 D (L)` | 11 | F/B | 2c4 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4a1-2 | 4a1-3 | look anyway | 0.85% | 6.8% | 35% |
| 2 | 4a2-2 | 4a2-3 | look anyway | 0 | 0.31% | 4.5% |
| 3 | 4a1-2 | 4a1-3 | look anyway | 1.4% | 10% | 43% |
| 4 | 4c4-4 | 4c4-3 | look anyway | 0 | 0.05% | 0.96% |
| 5 | 4c4-6 | 4c4-2 | drop | 0 | 0.04% | 0.87% |
| 6 | 4c3-5 | 4c3-9 | drop | <0.01% | 0.10% | 1.6% |
| 7 | 2c4-5 | 2c4-1 | drop | 0.05% | 0.84% | 7.6% |
| 8 | 2c4-1 | 2c4-1 | keep | 0.52% | 4.3% | 24% |

Shown: 8 of the 205 DRs up to 11 moves (9 moves: 3 of 3; 10 moves: 1 of 14; 11 moves: 4 of 188).

<details>
<summary>Answers for scramble 56</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 6 | 7 | 12 | 21 |
| 2 | 9 | 10 | 13 | 21 |
| 3 | 6 | 7 | 13 | 21 |
| 4 | 11 | 10 | 14 | 24 |
| 5 | 12 | 10 | 14 | 25 |
| 6 | 9 | 10 | 13 | 24 |
| 7 | 9 | 7 | 13 | 24 |
| 8 | 8 | 8 | 13 | 23 |

Best on the page: **21 moves**, from DR 1 (DRs 2 and 3 tie it): `F' U R' B2 L U2 B2 U2 R2 F2 D' R2 D' L2 F2 L2 D F' L B' R'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 57

```
R' U' F L2 U' F2 B2 U2 F2 R2 D R2 U2 F' U2 R' F' U2 B D B2 L' U2 R2 U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(F' D' R B2 R B' U R2 B)` | 9 | U/D | 2c4 4e | 2 |
| 2 | `L U' F' L' D B D2 R2 U` | 9 | F/B | 2c4 2e | 2 |
| 3 | `L U' F' L' D B U2 L2 U` | 9 | F/B | 2c4 2e | 3 |
| 4 | `L U' F' L' D' R2 U2 F' U` | 9 | F/B | 2c4 4e | 1 |
| 5 | `F' R2 U' F U' D' R2 U (L U2 L)` | 11 | F/B | 4a1 2e | 3 |
| 6 | `L2 F L B L' U D L2 D F D` | 11 | F/B | 2c4 4e | 3 |
| 7 | `L U' F' L' D B' D2 R2 U2 F2 U` | 11 | F/B | 2c4 2e | 1 |
| 8 | `(F2 D2 L U2 L' B' U D L2 R2 B)` | 11 | U/D | 4b5 2e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-1 | 2c4-1 | look anyway | 0.52% | 4.3% | 24% |
| 2 | 2c4-1 | 2c4-7 | look anyway | 0.03% | 0.77% | 7.0% |
| 3 | 2c4-1 | 2c4-7 | look anyway | 0.09% | 1.3% | 9.9% |
| 4 | 2c4-1 | 2c4-7 | look anyway | 0.02% | 0.48% | 4.7% |
| 5 | 4a1-3 | 4a1-2 | keep | 3.2% | 16% | 54% |
| 6 | 2c4-1 | 2c4-7 | drop | 0.13% | 1.4% | 10% |
| 7 | 2c4-1 | 2c4-7 | drop | <0.01% | 0.40% | 4.8% |
| 8 | 4b5-1 | 4b5-2 | drop | 0.01% | 0.14% | 1.4% |

Shown: 8 of the 635 DRs up to 11 moves (9 moves: 4 of 5; 10 moves: 0 of 74; 11 moves: 4 of 556).

<details>
<summary>Answers for scramble 57</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 14 | 23 |
| 2 | 8 | 9 | 14 | 23 |
| 3 | 8 | 9 | 14 | 23 |
| 4 | 9 | 10 | 14 | 23 |
| 5 | 6 | 7 | 12 | 23 |
| 6 | 7 | 9 | 14 | 25 |
| 7 | 9 | 9 | 13 | 24 |
| 8 | 9 | 10 | 15 | 26 |

Best on the page: **23 moves**, from DR 1 (DRs 2, 3, 4 and 5 tie it): `U' R2 U' F2 R2 F2 D F2 R2 U' F2 D' B2 U' B' R2 U' B R' B2 R' D F`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 58

```
R' U' F D2 L2 D B2 U' F2 R2 U' B2 U R' D' L F' U2 F U R2 B' R F2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L2 R F2 D B (L' R2 B' R)` | 9 | U/D | 4c4 4e | 0 |
| 2 | `(L' F' D R' B2 D' B U D)` | 9 | F/B | 4c4 4e | 2 |
| 3 | `(L' F' D R' B2 D' B' U D)` | 9 | F/B | 4c4 4e | 1 |
| 4 | `(D B2 L' F2 R' F B U F)` | 9 | U/D | 4b5 4e | 3 |
| 5 | `(D L' F2 R' F' U2 L2 B' D F U)` | 11 | F/B | 2c4 2e | 4 |
| 6 | `(L' D2 F2 D' R U F R2 B' U D)` | 11 | F/B | 2c4 6e | 3 |
| 7 | `(L' F' D R' U' L2 F U L2 B U)` | 11 | F/B | 4c3 2e | 2 |
| 8 | `(L' F' D R' B2 D' B D2 L2 U D)` | 11 | F/B | 4c4 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-2 | 4c4-6 | look anyway | 0 | 0 | 0.81% |
| 2 | 4c4-4 | 4c4-5 | look anyway | 0 | <0.01% | 0.20% |
| 3 | 4c4-4 | 4c4-5 | look anyway | 0 | 0 | 0.08% |
| 4 | 4b5-2 | 4b5-2 | look anyway | 0 | 0.01% | 0.79% |
| 5 | 2c4-2 | 2c4-2 | keep | 0.60% | 6.0% | 28% |
| 6 | 2c4-4 | 2c4-3 | drop | 0.25% | 1.8% | 10% |
| 7 | 4c3-9 | 4c3-5 | drop | <0.01% | 0.21% | 2.6% |
| 8 | 4c4-4 | 4c4-1 | drop | <0.01% | 0.24% | 2.5% |

Shown: 8 of the 202 DRs up to 11 moves (9 moves: 4 of 4; 10 moves: 0 of 15; 11 moves: 4 of 183).

<details>
<summary>Answers for scramble 58</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 11 | 15 | 23 |
| 2 | 11 | 11 | 14 | 22 |
| 3 | 11 | 11 | 15 | 23 |
| 4 | 11 | 11 | 15 | 23 |
| 5 | 9 | 9 | 13 | 24 |
| 6 | 9 | 8 | 15 | 24 |
| 7 | 9 | 8 | 14 | 25 |
| 8 | 11 | 10 | 14 | 25 |

Best on the page: **22 moves**, from DR 2: `R2 F' D2 B' U2 B R2 U2 F R2 F' U2 F D U' B' D B2 R D' F L`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 59

```
R' U' F L D' F' R B L U F' R2 F2 R D' L2 U L2 D2 R2 L2 U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L' U2 L2 U' B' D (F U2 D R)` | 10 | F/B | 4c3 2e | 5 |
| 2 | `L U2 L2 U B' D (F U2 D R)` | 10 | F/B | 4c3 4e | 3 |
| 3 | `(R B' D' L' U' R' B' U2 F' L)` | 10 | F/B | 4c3 4e | 2 |
| 4 | `L' B2 D2 R2 D' B' U (F U2 D R)` | 11 | F/B | 2c5 2e | 4 |
| 5 | `U' F (U2 B' L2 F2 L' U D B2 L)` | 11 | U/D | 2c3 4e | 2 |
| 6 | `L (F U2 D R' F U' D' R2 D' B)` | 11 | U/D | 2c3 4e | 4 |
| 7 | `(R B' D' L' U' R' F2 B D2 F' R)` | 11 | F/B | 4c3 4e | 1 |
| 8 | `(R B' D' L' U' R' U2 F' L2 B' L)` | 11 | F/B | 4c3 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c3-2 | 4c3-5 | look anyway | 2.6% | 11% | 36% |
| 2 | 4c3-2 | 4c3-5 | look anyway | 0.78% | 4.2% | 22% |
| 3 | 4c3-5 | 4c3-6 | look anyway | 0.15% | 1.4% | 8.7% |
| 4 | 2c5-1 | 2c5-1 | drop | 0.05% | 0.82% | 6.4% |
| 5 | 2c3-2 | 2c3-1 | keep | 1.6% | 8.8% | 36% |
| 6 | 2c3-1 | 2c3-3 | keep | 2.9% | 13% | 45% |
| 7 | 4c3-5 | 4c3-6 | drop | 0.08% | 0.96% | 7.0% |
| 8 | 4c3-6 | 4c3-5 | drop | 0.15% | 1.4% | 8.7% |

Shown: 8 of the 43 DRs up to 11 moves (10 moves: 3 of 3; 11 moves: 5 of 40).

<details>
<summary>Answers for scramble 59</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 13 | 23 |
| 2 | 8 | 9 | 13 | 23 |
| 3 | 9 | 9 | 14 | 24 |
| 4 | 10 | 9 | 15 | 25 |
| 5 | 7 | 7 | 13 | 24 |
| 6 | 6 | 6 | 13 | 24 |
| 7 | 9 | 9 | 15 | 25 |
| 8 | 9 | 10 | 15 | 26 |

Best on the page: **23 moves**, from DR 1 (DR 2 ties it): `L' U2 L2 U' B' D F2 U2 F U2 B R2 U2 B U2 F R2 D2 F' R' D' U2 F'`. The list drops 3 of the 5 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 60

```
R' U' F L2 B2 L2 B2 U2 R2 D F2 D' U2 R U2 B2 D' R' U2 B D' U' F R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `B L' U F B2 U L D` | 8 | R/L | 2c4 4e | 1 |
| 2 | `F L B' D' L U F2 U' F` | 9 | U/D | 4a1 4e | 2 |
| 3 | `B U L' F (D L' U2 L U)` | 9 | R/L | 4a1 4e | 0 |
| 4 | `B L' U F L2 R2 F2 D L U` | 10 | R/L | 2c4 4e | 0 |
| 5 | `R2 F' U2 F' D2 B' D (R2 D B' L)` | 11 | F/B | 0c4 4e | 3 |
| 6 | `(L' B' U2 L' B2 L2 U' F' B' D F)` | 11 | U/D | 4b5 2e | 1 |
| 7 | `B U L' F (R2 D2 L' R2 U' L' D)` | 11 | R/L | 2c3 4e | 1 |
| 8 | `(L' B' U2 L R2 D2 F' D' F R2 B)` | 11 | U/D | 2c4 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-5 | 2c4-6 | look anyway | 0.01% | 0.31% | 2.9% |
| 2 | 4a1-4 | 4a1-2 | look anyway | 6.7% | 21% | 54% |
| 3 | 4a1-2 | 4a1-1 | look anyway | 2.3% | 10% | 36% |
| 4 | 2c4-5 | 2c4-6 | look anyway | 0.01% | 0.21% | 2.4% |
| 5 | 0c4-1 | 0c4-1 | drop | 0.14% | 1.3% | 8.9% |
| 6 | 4b5-1 | 4b5-1 | drop | <0.01% | 0.08% | 1.2% |
| 7 | 2c3-2 | 2c3-2 | keep | 0.49% | 3.9% | 21% |
| 8 | 2c4-7 | 2c4-4 | drop | <0.01% | 0.35% | 3.5% |

Shown: 8 of the 406 DRs up to 11 moves (8 moves: 1 of 1; 9 moves: 2 of 2; 10 moves: 1 of 42; 11 moves: 4 of 361).

<details>
<summary>Answers for scramble 60</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 9 | 15 | 22 |
| 2 | 4 | 7 | 13 | 22 |
| 3 | 5 | 3 | 13 | 21 |
| 4 | 10 | 9 | 15 | 25 |
| 5 | 9 | 10 | 15 | 25 |
| 6 | 10 | 10 | 13 | 24 |
| 7 | 7 | 6 | 13 | 24 |
| 8 | 9 | 8 | 14 | 25 |

Best on the page: **21 moves**, from DR 3: `B U L' F' D2 F2 R2 B2 D2 R2 D2 R2 B2 L F2 B2 U' L' U2 L D'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 61

```
R' U' F L2 B2 D' F' R2 U D' L' D2 F L2 D2 B2 D R2 U B2 D L2 D2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U2 F D L U R2 U D2 L` | 9 | U/D | 2c3 4e | 1 |
| 2 | `R2 F' L F U2 D L' D2 L` | 9 | F/B | 0c3 2e | 4 |
| 3 | `R2 F' L F U2 D R' B2 R` | 9 | F/B | 0c3 2e | 3 |
| 4 | `U D F' U' F2 D (B2 D' L)` | 9 | F/B | 2c4 4e | 1 |
| 5 | `U2 F R F2 B2 U' B2 U2 R B2 U` | 11 | R/L | 0c4 6e | 0 |
| 6 | `(R D2 F2 D' F' R F' U2 L R2 F)` | 11 | R/L | 2c4 4e | 4 |
| 7 | `(D2 F2 B' L' D' B' D2 B' R2 B2 L)` | 11 | F/B | 4b5 2e | 1 |
| 8 | `U F L2 U' L' D' R2 U B U' B` | 11 | U/D | 2c4 6e | 4 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-2 | 2c3-1 | look anyway | 0.88% | 6.1% | 29% |
| 2 | 0c3-1 | 0c3-1 | look anyway | 0.83% | 3.0% | 9.1% |
| 3 | 0c3-1 | 0c3-1 | look anyway | 0 | 0.37% | 11% |
| 4 | 2c4-7 | 2c4-4 | look anyway | 0 | 0.08% | 1.5% |
| 5 | 0c4-1 | 0c4-1 | drop | 0.01% | 0.11% | 1.9% |
| 6 | 2c4-3 | 2c4-1 | keep | 1.5% | 7.8% | 32% |
| 7 | 4b5-1 | 4b5-1 | drop | <0.01% | 0.08% | 1.2% |
| 8 | 2c4-6 | 2c4-1 | keep | 0.67% | 4.0% | 21% |

Shown: 8 of the 1,316 DRs up to 11 moves (9 moves: 4 of 8; 10 moves: 0 of 88; 11 moves: 4 of 1,220).

<details>
<summary>Answers for scramble 61</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 9 | 18 |
| 2 | 11 | 9 | 13 | 22 |
| 3 | 9 | 9 | 13 | 22 |
| 4 | 9 | 9 | 14 | 23 |
| 5 | 10 | 10 | 14 | 25 |
| 6 | 8 | 8 | 13 | 23 |
| 7 | 9 | 10 | 14 | 25 |
| 8 | 9 | 8 | 13 | 23 |

Best on the page: **18 moves**, from DR 1: `U2 F D L U R2 U D2 L D' F2 R2 D' R2 B2 L2 F2 U`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 62

```
R' U' F U' R2 U2 R2 U' L2 U' F2 R2 U' B' U F R2 F2 U R2 D R' F2 L' U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L U D2 F' D R2 B' U2 D2 R` | 10 | F/B | 4c4 4e | 3 |
| 2 | `U B2 D2 R' D (L F B D' F)` | 10 | R/L | 2c4 4e | 2 |
| 3 | `D' L' U' B2 U2 R2 F' L (F2 D)` | 10 | F/B | 4c4 2e | 3 |
| 4 | `B' U' B' L D (F B L' D2 F)` | 10 | R/L | 2c5 4e | 3 |
| 5 | `F' L (B' R' B' U2 B' U2 D' B' U)` | 11 | F/B | 2c3 6e | 1 |
| 6 | `L U D2 F' D R2 B' R2 U2 D2 R` | 11 | F/B | 4c4 4e | 1 |
| 7 | `L U D2 F' D (B R2 U2 D2 F L)` | 11 | F/B | 2c3 2e | 3 |
| 8 | `L U' D F R' F2 D B U2 D' B` | 11 | U/D | 4c3 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-2 | 4c4-5 | look anyway | 0 | 0.04% | 1.4% |
| 2 | 2c4-6 | 2c4-7 | look anyway | 0.01% | 0.28% | 2.3% |
| 3 | 4c4-3 | 4c4-4 | look anyway | 0 | 0.09% | 1.5% |
| 4 | 2c5-1 | 2c5-1 | look anyway | 0.10% | 0.85% | 6.2% |
| 5 | 2c3-3 | 2c3-2 | keep | 0.22% | 1.8% | 12% |
| 6 | 4c4-4 | 4c4-5 | drop | 0 | 0 | 0.08% |
| 7 | 2c3-3 | 2c3-3 | keep | 1.0% | 6.1% | 29% |
| 8 | 4c3-7 | 4c3-5 | drop | 0.17% | 1.3% | 7.9% |

Shown: 8 of the 90 DRs up to 11 moves (10 moves: 4 of 6; 11 moves: 4 of 84).

<details>
<summary>Answers for scramble 62</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 11 | 13 | 23 |
| 2 | 9 | 9 | 14 | 23 |
| 3 | 10 | 10 | 15 | 24 |
| 4 | 9 | 9 | 14 | 23 |
| 5 | 8 | 8 | 14 | 24 |
| 6 | 10 | 11 | 16 | 26 |
| 7 | 6 | 7 | 13 | 23 |
| 8 | 9 | 9 | 12 | 23 |

Best on the page: **23 moves**, from DR 1 (DRs 2, 4, 7 and 8 tie it): `L U D2 F' D R2 B' U2 D2 R F D2 F' R2 D2 B2 U2 F' D2 F R2 D2 B2`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 63

```
R' U' F D2 B U2 D2 F L2 D2 F R2 F L' F' D L U L' B2 F U' R' U2 F' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(R2 F' B' R' U L U' L U)` | 9 | R/L | 2c4 6e | 1 |
| 2 | `R' D F2 R F' U D2 F U` | 9 | F/B | 2c5 4e | 3 |
| 3 | `(F' B R' U B2 L F2 R U' L)` | 10 | U/D | 2c4 2e | 1 |
| 4 | `R' F' D R' D2 B' R2 F2 U2 B` | 10 | U/D | 4b2 2e | 5 |
| 5 | `U F (F U' R' U' R' U D F2 L)` | 11 | U/D | 2c4 4e | 0 |
| 6 | `R' D F2 R F' U2 D2 R2 U' F U` | 11 | F/B | 0c3 2e | 2 |
| 7 | `R2 D' L2 R D L2 D' L D (F B)` | 11 | R/L | 2c4 8e | 0 |
| 8 | `(F' B' L2 D2 B2 L' D' R' D' L' D)` | 11 | R/L | 4c4 2e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-4 | 2c4-4 | look anyway | 0.02% | 0.26% | 2.5% |
| 2 | 2c5-2 | 2c5-3 | look anyway | 0 | 0 | 0.33% |
| 3 | 2c4-2 | 2c4-2 | look anyway | 0.21% | 2.2% | 16% |
| 4 | 4b2-4 | 4b2-2 | look anyway | 8.7% | 26% | 65% |
| 5 | 2c4-1 | 2c4-7 | drop | 0 | 0.25% | 3.2% |
| 6 | 0c3-2 | 0c3-2 | drop | 0 | 0.02% | 0.96% |
| 7 | 2c4-7 | 2c4-4 | drop | 0 | 0 | 0.17% |
| 8 | 4c4-4 | 4c4-5 | drop | 0 | <0.01% | 0.22% |

Shown: 8 of the 1,140 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 57; 11 moves: 4 of 1,081).

<details>
<summary>Answers for scramble 63</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 14 | 23 |
| 2 | 11 | 12 | 15 | 24 |
| 3 | 9 | 9 | 13 | 22 |
| 4 | 6 | 7 | 13 | 22 |
| 5 | 9 | 9 | 14 | 24 |
| 6 | 10 | 10 | 14 | 25 |
| 7 | 11 | 10 | 14 | 24 |
| 8 | 10 | 11 | 14 | 25 |

Best on the page: **22 moves**, from DR 3 (DR 4 ties it): `D L2 U F2 D R2 B2 U2 L2 F2 D B2 L U R' F2 L' B2 U' R B' F`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 64

```
R' U' F D B2 R2 B2 R2 D' F2 L2 F2 U2 R D2 B' F2 D U R B U B2 R2 U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U R D B L2 F D' B (L)` | 9 | U/D | 2c4 6e | 1 |
| 2 | `U2 F U2 F' L2 U (L' F R)` | 9 | F/B | 0c0 4e | 2 |
| 3 | `U R (L' B U D B U' F B)` | 10 | U/D | 4a2 2e | 1 |
| 4 | `F D2 B2 D' L2 B2 U (L' F R)` | 10 | F/B | 2c4 4e | 0 |
| 5 | `D' B2 D F' U F2 U (F' L' F' R)` | 11 | F/B | 2c3 4e | 1 |
| 6 | `F' B2 R2 D L' F' U2 B' D2 L' B` | 11 | R/L | 2c3 6e | 3 |
| 7 | `D B D F' U' B U D (L' F R)` | 11 | F/B | 4c3 4e | 4 |
| 8 | `L2 U R (L' B' U2 R2 F' D' B' D)` | 11 | F/B | 4b2 4e | 0 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-7 | 2c4-3 | look anyway | 0.01% | 0.44% | 4.0% |
| 2 | 0c0-1 | 0c0-1 | look anyway | 4.6% | 17% | 52% |
| 3 | 4a2-2 | 4a2-3 | look anyway | 0 | 0.31% | 4.5% |
| 4 | 2c4-6 | 2c4-4 | look anyway | 0 | 0.13% | 1.5% |
| 5 | 2c3-2 | 2c3-3 | keep | 0.38% | 2.8% | 17% |
| 6 | 2c3-1 | 2c3-1 | keep | 3.0% | 14% | 49% |
| 7 | 4c3-5 | 4c3-1 | keep | 1.2% | 7.3% | 32% |
| 8 | 4b2-1 | 4b2-2 | keep | 0.81% | 5.4% | 28% |

Shown: 8 of the 833 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 67; 11 moves: 4 of 764).

<details>
<summary>Answers for scramble 64</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 8 | 15 | 23 |
| 2 | 6 | 7 | 12 | 21 |
| 3 | 9 | 10 | 14 | 23 |
| 4 | 9 | 10 | 14 | 24 |
| 5 | 8 | 8 | 13 | 24 |
| 6 | 8 | 7 | 13 | 24 |
| 7 | 9 | 9 | 13 | 23 |
| 8 | 8 | 7 | 12 | 23 |

Best on the page: **21 moves**, from DR 2: `U2 F U2 F' L2 U F2 R2 F2 B D2 U2 B R2 D2 U2 F2 D2 R' F' L`. The list drops 0 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 65

```
R' U' F U' B2 R2 U' L2 U' F2 U2 B2 F2 R' D2 B2 F' U R B' D R U2 F R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U B L' U' B U2 B D (U2 R)` | 10 | F/B | 2c3 4e | 3 |
| 2 | `F' D2 R F D2 F D F (F L)` | 10 | U/D | 4b5 2e | 0 |
| 3 | `F' D2 R B R2 B U F (F L)` | 10 | U/D | 4b5 0e | 1 |
| 4 | `U B L' U D2 F U2 F D (U2 R)` | 11 | F/B | 2c3 6e | 3 |
| 5 | `(L' B L R F' R' U F2 L2 U2 L)` | 11 | U/D | 4b5 4e | 1 |
| 6 | `(L' B' L R F L D R2 D2 B2 R)` | 11 | U/D | 4b5 2e | 5 |
| 7 | `F' L U2 D' R' U R2 U2 B' U' F` | 11 | U/D | 2c5 4e | 2 |
| 8 | `U B L' U' L2 F R2 F U (U2 R)` | 11 | F/B | 2c3 4e | 4 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-1 | 2c3-3 | look anyway | 1.8% | 9.3% | 37% |
| 2 | 4b5-1 | 4b5-1 | look anyway | 0 | 0.06% | 0.76% |
| 3 | 4b5-1 | 4b5-1 | look anyway | 0 | 0.15% | 1.9% |
| 4 | 2c3-1 | 2c3-3 | keep | 0.73% | 5.3% | 28% |
| 5 | 4b5-1 | 4b5-1 | drop | <0.01% | 0.08% | 1.1% |
| 6 | 4b5-1 | 4b5-1 | drop | 0.25% | 1.8% | 9.5% |
| 7 | 2c5-1 | 2c5-2 | drop | 0.02% | 0.23% | 2.4% |
| 8 | 2c3-1 | 2c3-1 | keep | 5.9% | 23% | 61% |

Shown: 8 of the 46 DRs up to 11 moves (10 moves: 3 of 3; 11 moves: 5 of 43).

<details>
<summary>Answers for scramble 65</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 14 | 22 |
| 2 | 10 | 9 | 14 | 23 |
| 3 | 9 | 9 | 15 | 24 |
| 4 | 8 | 9 | 14 | 24 |
| 5 | 10 | 10 | 13 | 24 |
| 6 | 10 | 9 | 13 | 24 |
| 7 | 9 | 10 | 13 | 24 |
| 8 | 6 | 8 | 12 | 23 |

Best on the page: **22 moves**, from DR 1: `U B L' U' B U2 B D' B2 D2 F D2 B U2 B D2 B' U2 L2 B' R U2`. The list drops 3 of the 5 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 66

```
R' U' F U2 R2 B2 U2 B2 R' B2 R' U2 R' F R' U2 R2 D2 F U D2 L R' D2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `D2 F' U' D2 F L (F2 U)` | 8 | F/B | 4b2 4e | 1 |
| 2 | `F' U' F2 L U R2 B2 D B` | 9 | U/D | 2c3 4e | 1 |
| 3 | `F' U' F2 L U F2 U' B2 L2 B` | 10 | U/D | 2c3 4e | 4 |
| 4 | `D' F' D' F U' B' R' B2 R' B` | 10 | R/L | 2c4 2e | 4 |
| 5 | `F U' L B2 L2 B R2 D' B' D B` | 11 | U/D | 0c3 6e | 3 |
| 6 | `U' R2 U2 D2 F' D (U2 L2 D B' L)` | 11 | F/B | 4b5 4e | 5 |
| 7 | `(D2 F R2 U2 L R2 U2 B' D' L2 F)` | 11 | U/D | 4b2 2e | 4 |
| 8 | `(R2 B D2 F' R' F2 B L2 B D F)` | 11 | U/D | 2c4 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-1 | 4b2-2 | look anyway | 1.7% | 9.1% | 36% |
| 2 | 2c3-2 | 2c3-2 | look anyway | 0.49% | 3.9% | 21% |
| 3 | 2c3-3 | 2c3-2 | look anyway | 2.1% | 9.7% | 36% |
| 4 | 2c4-7 | 2c4-3 | look anyway | 0.20% | 2.3% | 14% |
| 5 | 0c3-1 | 0c3-2 | drop | 0.34% | 2.3% | 8.8% |
| 6 | 4b5-1 | 4b5-1 | drop | 0.27% | 2.0% | 11% |
| 7 | 4b2-3 | 4b2-3 | keep | 3.2% | 15% | 49% |
| 8 | 2c4-3 | 2c4-7 | drop | 0.02% | 0.40% | 3.7% |

Shown: 8 of the 562 DRs up to 11 moves (8 moves: 1 of 1; 9 moves: 1 of 1; 10 moves: 2 of 52; 11 moves: 4 of 508).

<details>
<summary>Answers for scramble 66</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 6 | 7 | 12 | 20 |
| 2 | 6 | 8 | 11 | 20 |
| 3 | 7 | 6 | 13 | 22 |
| 4 | 10 | 7 | 13 | 23 |
| 5 | 9 | 10 | 14 | 25 |
| 6 | 9 | 10 | 14 | 25 |
| 7 | 5 | 6 | 11 | 22 |
| 8 | 9 | 10 | 14 | 25 |

Best on the page: **20 moves**, from DR 1 (DR 2 ties it): `D2 F' U' D2 F L B' R2 D2 B' U2 F' R2 L2 D2 R2 U2 B' U' F2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 67

```
R' U' F U2 B2 D F2 L2 F2 R2 U' B2 L2 B' U' F' D' L2 B L F2 R F2 U2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L' B D (B2 U2 R F2 L B)` | 9 | R/L | 2c3 6e | 4 |
| 2 | `D' F' D B (L2 R F B2 L)` | 9 | U/D | 4c4 4e | 3 |
| 3 | `L' B D (B2 D2 L B2 R F)` | 9 | R/L | 2c3 4e | 4 |
| 4 | `B2 D2 R F D2 R (R B D)` | 9 | F/B | 4b5 2e | 0 |
| 5 | `D2 L' R B L2 U2 B (R2 B R' D)` | 11 | R/L | 4c4 4e | 5 |
| 6 | `F' B R U (D B' D2 L' U2 L2 B)` | 11 | R/L | 4b5 2e | 1 |
| 7 | `(R D2 L' F' U2 D R' B2 R2 F B)` | 11 | R/L | 2c4 4e | 2 |
| 8 | `L' B U2 D L' U2 R' D2 L R' F` | 11 | R/L | 2c3 2e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-3 | look anyway | 0.14% | 1.8% | 13% |
| 2 | 4c4-3 | 4c4-2 | look anyway | 0.01% | 0.55% | 3.9% |
| 3 | 2c3-3 | 2c3-3 | look anyway | 1.2% | 6.2% | 26% |
| 4 | 4b5-1 | 4b5-1 | look anyway | 0 | 0.06% | 0.76% |
| 5 | 4c4-1 | 4c4-4 | drop | 0.26% | 2.6% | 14% |
| 6 | 4b5-2 | 4b5-1 | drop | 0 | 0.05% | 0.78% |
| 7 | 2c4-6 | 2c4-2 | drop | 0.17% | 1.2% | 8.1% |
| 8 | 2c3-3 | 2c3-3 | keep | 0.44% | 3.7% | 22% |

Shown: 8 of the 1,074 DRs up to 11 moves (9 moves: 4 of 15; 10 moves: 0 of 116; 11 moves: 4 of 943).

<details>
<summary>Answers for scramble 67</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 9 | 13 | 22 |
| 2 | 10 | 10 | 14 | 22 |
| 3 | 7 | 8 | 13 | 21 |
| 4 | 10 | 10 | 15 | 23 |
| 5 | 9 | 11 | 14 | 25 |
| 6 | 10 | 9 | 14 | 25 |
| 7 | 10 | 8 | 14 | 24 |
| 8 | 7 | 7 | 11 | 22 |

Best on the page: **21 moves**, from DR 3: `L' B D U2 R2 L D2 R F2 D2 R B2 D2 L2 B2 F R' B2 L' D2 B2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 68

```
R' U' F L2 B2 U L2 B2 U' B2 U L2 D' L U' F' R U' F L D2 F D B' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F L2 D' L2 U (R2 F R B' L)` | 10 | F/B | 2c3 4e | 4 |
| 2 | `F L2 U' F2 D (R2 F' R B' L)` | 10 | F/B | 4b5 4e | 2 |
| 3 | `L B R' D' L (U2 L2 F U D)` | 10 | F/B | 2c4 2e | 6 |
| 4 | `F L2 U' F2 D (R2 F R B' L)` | 10 | F/B | 2c3 4e | 2 |
| 5 | `F L2 D' L2 U (D2 R2 F' R B' L)` | 11 | F/B | 2c3 4e | 0 |
| 6 | `F' D2 B2 D' F2 U (R2 F R B' L)` | 11 | F/B | 2c3 4e | 2 |
| 7 | `L B R' D' L (D2 R2 F2 B' U D)` | 11 | F/B | 2c4 2e | 1 |
| 8 | `B R' F U L U2 L2 D R2 F D` | 11 | F/B | 2c4 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-1 | look anyway | 2.9% | 13% | 45% |
| 2 | 4b5-2 | 4b5-1 | look anyway | 0 | 0.07% | 1.0% |
| 3 | 2c4-1 | 2c4-1 | look anyway | 5.2% | 20% | 58% |
| 4 | 2c3-3 | 2c3-1 | look anyway | 1.0% | 6.4% | 30% |
| 5 | 2c3-3 | 2c3-3 | keep | 0.09% | 1.0% | 8.0% |
| 6 | 2c3-3 | 2c3-1 | keep | 1.0% | 6.4% | 30% |
| 7 | 2c4-1 | 2c4-1 | keep | 0.24% | 2.7% | 19% |
| 8 | 2c4-1 | 2c4-3 | keep | 0.41% | 3.2% | 18% |

Shown: 8 of the 135 DRs up to 11 moves (10 moves: 4 of 15; 11 moves: 4 of 120).

<details>
<summary>Answers for scramble 68</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 7 | 12 | 21 |
| 2 | 11 | 10 | 15 | 24 |
| 3 | 8 | 8 | 13 | 21 |
| 4 | 9 | 7 | 12 | 22 |
| 5 | 7 | 9 | 14 | 24 |
| 6 | 8 | 7 | 14 | 24 |
| 7 | 8 | 8 | 12 | 22 |
| 8 | 8 | 10 | 12 | 23 |

Best on the page: **21 moves**, from DR 1 (DR 3 ties it): `F L2 D' L2 U' L2 F L2 B2 L2 F' U2 L2 B' U2 R2 L' B R' F' R2`. The list drops 0 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 69

```
R' U' F D L2 D' U2 B2 D2 R2 F2 L2 U F B2 R B' D L' B L2 D' R2 U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' B (U L B2 U2 D' R' U)` | 9 | R/L | 4c4 4e | 3 |
| 2 | `U' B R' U2 R' U B2 R' D` | 9 | R/L | 4b2 4e | 2 |
| 3 | `U' B R U' D' R' B2 L' D` | 9 | R/L | 4b5 4e | 3 |
| 4 | `U D' R U R (B' R2 D' B)` | 9 | U/D | 4c3 4e | 1 |
| 5 | `F L2 F U' B' L2 R2 F2 U' F2 D` | 11 | R/L | 4b5 2e | 1 |
| 6 | `R2 B L' B L (F' U2 F U B2 D)` | 11 | F/B | 2c5 4e | 1 |
| 7 | `(B2 L' U2 L' U' F U2 D F' D F)` | 11 | U/D | 2c5 4e | 1 |
| 8 | `(R2 U R F2 R U2 F B' D F B)` | 11 | U/D | 2c3 6e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-2 | 4c4-5 | look anyway | 0 | 0.04% | 1.4% |
| 2 | 4b2-3 | 4b2-1 | look anyway | 1.6% | 8.8% | 38% |
| 3 | 4b5-1 | 4b5-2 | look anyway | <0.01% | 0.13% | 1.8% |
| 4 | 4c3-6 | 4c3-5 | look anyway | 0.08% | 0.96% | 7.0% |
| 5 | 4b5-1 | 4b5-2 | drop | 0 | 0.05% | 0.78% |
| 6 | 2c5-1 | 2c5-1 | drop | <0.01% | 0.23% | 2.7% |
| 7 | 2c5-3 | 2c5-2 | drop | 0 | 0 | 0.14% |
| 8 | 2c3-2 | 2c3-3 | keep | 0.33% | 2.5% | 15% |

Shown: 8 of the 1,752 DRs up to 11 moves (9 moves: 4 of 6; 10 moves: 0 of 127; 11 moves: 4 of 1,619).

<details>
<summary>Answers for scramble 69</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 11 | 15 | 24 |
| 2 | 9 | 7 | 12 | 20 |
| 3 | 11 | 11 | 13 | 22 |
| 4 | 9 | 9 | 14 | 23 |
| 5 | 9 | 10 | 14 | 25 |
| 6 | 10 | 9 | 13 | 24 |
| 7 | 11 | 11 | 15 | 25 |
| 8 | 8 | 8 | 12 | 22 |

Best on the page: **20 moves**, from DR 2: `U' B R' U2 R' U B2 R' D' B2 R B2 U2 B2 L' U2 R2 L D2 L`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 70

```
R' U' F U2 L2 B2 L2 U B2 R2 D' R2 U B' D' L' F R2 F2 L2 R D B' F' U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' L' U B R (B' U F D)` | 9 | F/B | 2c3 4e | 4 |
| 2 | `B' R U' L' B2 L2 F U B` | 9 | U/D | 2c5 6e | 2 |
| 3 | `B' U' L' U R U' D' B D F` | 10 | U/D | 2c4 2e | 1 |
| 4 | `B' R U' L' F' D L2 U2 R2 F` | 10 | U/D | 2c3 4e | 6 |
| 5 | `B2 R U' B' L' U F D2 F' U' F` | 11 | U/D | 4c3 2e | 1 |
| 6 | `B2 U' D2 F D F B (F R U' L)` | 11 | U/D | 2c3 2e | 3 |
| 7 | `U' D' F2 B' U F U (F R U' L)` | 11 | F/B | 4b2 4e | 2 |
| 8 | `B' U' L U R B' U R2 F D2 B` | 11 | U/D | 2c3 4e | 4 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-3 | look anyway | 1.2% | 6.2% | 26% |
| 2 | 2c5-1 | 2c5-2 | look anyway | 0.01% | 0.22% | 2.2% |
| 3 | 2c4-4 | 2c4-6 | look anyway | 0.02% | 0.27% | 2.4% |
| 4 | 2c3-1 | 2c3-1 | look anyway | 12% | 35% | 74% |
| 5 | 4c3-9 | 4c3-4 | drop | 0.06% | 0.56% | 3.7% |
| 6 | 2c3-3 | 2c3-1 | keep | 2.8% | 14% | 51% |
| 7 | 4b2-3 | 4b2-2 | keep | 1.2% | 7.6% | 34% |
| 8 | 2c3-1 | 2c3-1 | keep | 5.9% | 23% | 61% |

Shown: 8 of the 201 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 18; 11 moves: 4 of 181).

<details>
<summary>Answers for scramble 70</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 7 | 13 | 22 |
| 2 | 10 | 11 | 13 | 22 |
| 3 | 9 | 9 | 14 | 23 |
| 4 | 7 | 5 | 13 | 23 |
| 5 | 10 | 10 | 14 | 25 |
| 6 | 6 | 7 | 12 | 22 |
| 7 | 7 | 8 | 13 | 23 |
| 8 | 6 | 7 | 12 | 23 |

Best on the page: **22 moves**, from DR 1 (DRs 2 and 6 tie it): `U' L' U B R F B2 D2 B D2 L2 F' D2 L2 B' U2 F L2 D' F' U' B`. The list drops 1 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 71

```
R' U' F U R2 F2 R' B' L F2 L2 D2 R B U' F2 U D L2 F2 R2 B2 U' B2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F U' L2 B R2 F' U (U' L)` | 9 | F/B | 4b5 2e | 1 |
| 2 | `(R U' L U R F' L2 B U)` | 9 | F/B | 2c4 2e | 1 |
| 3 | `R (U2 F2 L F D' B' D' F)` | 9 | U/D | 2c3 4e | 0 |
| 4 | `B U' L2 F' B' D F2 U (U' L)` | 10 | F/B | 2c4 2e | 0 |
| 5 | `F U D R (D2 F2 L2 B R2 B' D)` | 11 | F/B | 2c3 4e | 2 |
| 6 | `(R2 U' L' U' B' R2 D B' L2 F' D)` | 11 | F/B | 2c4 4e | 3 |
| 7 | `D F L2 B2 U' B D2 L2 B (U' L)` | 11 | U/D | 2c3 2e | 3 |
| 8 | `L2 B' L2 F2 U F (B U' L2 D L)` | 11 | U/D | 4c3 4e | 0 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b5-1 | 4b5-1 | look anyway | <0.01% | 0.08% | 1.2% |
| 2 | 2c4-7 | 2c4-6 | look anyway | 0 | 0.10% | 1.6% |
| 3 | 2c3-1 | 2c3-2 | look anyway | 0.59% | 4.4% | 24% |
| 4 | 2c4-1 | 2c4-2 | look anyway | 0.09% | 1.2% | 11% |
| 5 | 2c3-3 | 2c3-1 | keep | 1.0% | 6.4% | 30% |
| 6 | 2c4-3 | 2c4-5 | drop | 0.41% | 2.4% | 14% |
| 7 | 2c3-1 | 2c3-1 | keep | 5.6% | 22% | 62% |
| 8 | 4c3-2 | 4c3-5 | keep | 0.06% | 1.0% | 8.8% |

Shown: 8 of the 889 DRs up to 11 moves (9 moves: 3 of 3; 10 moves: 1 of 57; 11 moves: 4 of 829).

<details>
<summary>Answers for scramble 71</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 9 | 13 | 21 |
| 2 | 10 | 9 | 15 | 23 |
| 3 | 6 | 7 | 12 | 20 |
| 4 | 9 | 9 | 14 | 23 |
| 5 | 8 | 6 | 13 | 23 |
| 6 | 9 | 9 | 13 | 24 |
| 7 | 8 | 7 | 13 | 23 |
| 8 | 8 | 8 | 14 | 24 |

Best on the page: **20 moves**, from DR 3: `R F2 L2 D' F2 D' F2 L2 U' B2 R2 D2 F D B D F' L' F2 U2`. The list drops 1 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 72

```
R' U' F D F2 D' F2 L2 D2 U R2 B2 U2 L B2 F L U2 B2 F2 R2 U B2 F' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(D' B D' R U D2 L B R)` | 9 | F/B | 4a2 4e | 4 |
| 2 | `D' L' U D (L R' U2 F R B)` | 10 | R/L | 2c5 4e | 0 |
| 3 | `D' L' U D' F B U2 L' F' R` | 10 | F/B | 2c3 4e | 1 |
| 4 | `U' F2 B' L' F R D' L D' L` | 10 | U/D | 4c3 2e | 2 |
| 5 | `L U B R2 F' R' F' L (D F2 D)` | 11 | F/B | 2c3 4e | 4 |
| 6 | `L U F' U' L2 F2 U (R' U B L)` | 11 | F/B | 2c3 4e | 0 |
| 7 | `D' L' U D (B R' F2 L' F2 B L)` | 11 | F/B | 4b5 2e | 2 |
| 8 | `L U D2 F' B' R F' L (U L2 U)` | 11 | F/B | 4c3 2e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4a2-4 | 4a2-2 | look anyway | 0.87% | 5.2% | 22% |
| 2 | 2c5-3 | 2c5-2 | look anyway | 0 | 0 | 0.10% |
| 3 | 2c3-1 | 2c3-1 | look anyway | 1.4% | 8.6% | 37% |
| 4 | 4c3-9 | 4c3-5 | look anyway | <0.01% | 0.21% | 2.6% |
| 5 | 2c3-1 | 2c3-3 | keep | 2.9% | 13% | 45% |
| 6 | 2c3-3 | 2c3-3 | keep | 0.09% | 1.0% | 8.0% |
| 7 | 4b5-1 | 4b5-1 | drop | 0.02% | 0.24% | 2.3% |
| 8 | 4c3-5 | 4c3-2 | keep | 0.18% | 1.6% | 11% |

Shown: 8 of the 303 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 24; 11 moves: 4 of 278).

<details>
<summary>Answers for scramble 72</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 7 | 11 | 20 |
| 2 | 11 | 11 | 15 | 24 |
| 3 | 7 | 8 | 12 | 21 |
| 4 | 9 | 8 | 15 | 24 |
| 5 | 7 | 8 | 13 | 23 |
| 6 | 8 | 8 | 15 | 24 |
| 7 | 9 | 10 | 13 | 23 |
| 8 | 9 | 7 | 14 | 24 |

Best on the page: **20 moves**, from DR 1: `L2 F2 R2 U2 F' U2 L2 B2 R2 F' D2 R' B' L' D2 U' R' D B' D`. The list drops 1 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 73

```
R' U' F U2 R2 D' L2 B2 U2 F2 R2 U' R' U L2 B' U B2 D U' R' B' U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F2 D2 F' L' D' L' U' D2 R` | 9 | U/D | 2c5 6e | 0 |
| 2 | `B2 U2 F' D' L' R2 U' B2 R` | 9 | U/D | 4c4 4e | 1 |
| 3 | `B2 R U R' F (U L2 D B2 R)` | 10 | U/D | 2c4 6e | 2 |
| 4 | `F2 D2 F (L2 D B2 R' F2 D L)` | 10 | U/D | 4c4 2e | 2 |
| 5 | `F' U' F' D2 F (U B2 L' B2 D R)` | 11 | U/D | 4c3 4e | 1 |
| 6 | `F2 D2 F' L D F2 U' R U2 D' L` | 11 | U/D | 2c4 4e | 2 |
| 7 | `R2 B' R2 U2 F (U L' R F2 U L)` | 11 | U/D | 2c4 6e | 0 |
| 8 | `U D2 F2 D2 F (U2 R B2 U' L D)` | 11 | R/L | 2c3 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c5-3 | 2c5-2 | look anyway | 0 | 0 | 0.13% |
| 2 | 4c4-2 | 4c4-5 | look anyway | 0 | 0 | 0.47% |
| 3 | 2c4-1 | 2c4-6 | look anyway | 0.10% | 1.4% | 10% |
| 4 | 4c4-4 | 4c4-5 | look anyway | 0 | <0.01% | 0.22% |
| 5 | 4c3-5 | 4c3-6 | drop | 0.08% | 0.96% | 7.0% |
| 6 | 2c4-4 | 2c4-4 | drop | 0.03% | 0.45% | 3.8% |
| 7 | 2c4-7 | 2c4-4 | drop | 0 | 0.06% | 1.0% |
| 8 | 2c3-3 | 2c3-3 | keep | 0.35% | 2.6% | 15% |

Shown: 8 of the 482 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 38; 11 moves: 4 of 442).

<details>
<summary>Answers for scramble 73</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 15 | 24 |
| 2 | 10 | 11 | 14 | 23 |
| 3 | 8 | 10 | 13 | 22 |
| 4 | 11 | 11 | 15 | 24 |
| 5 | 9 | 9 | 14 | 25 |
| 6 | 9 | 10 | 15 | 25 |
| 7 | 10 | 9 | 15 | 25 |
| 8 | 8 | 8 | 13 | 24 |

Best on the page: **22 moves**, from DR 3: `B2 R U R' F' U D2 F2 L2 B2 R2 U L2 D' B2 D F2 R' B2 D' L2 U'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 74

```
R' U' F L2 U2 F2 L2 D L2 F2 D L2 U2 F' D' U B U R D U2 L F' R2 U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(F R' B' L' F' L2 U' D2 L)` | 9 | U/D | 0c3 4e | 2 |
| 2 | `(R' B L' F B2 L U F2 R)` | 9 | U/D | 2c3 4e | 2 |
| 3 | `U L' D L B' R D2 F B2 R` | 10 | F/B | 2c4 4e | 6 |
| 4 | `(B' L2 D' F U' L F L2 B' R)` | 10 | F/B | 0c0 0e | 2 |
| 5 | `(F R' B' L' F' U2 R2 U2 L2 U' L)` | 11 | U/D | 0c3 4e | 1 |
| 6 | `U2 F B R' B' L (B' L2 D F U)` | 11 | F/B | 2c3 2e | 1 |
| 7 | `(B D R' F' U F2 R B U2 R' B)` | 11 | R/L | 4b5 2e | 2 |
| 8 | `(F R' B' L' F' L2 D' R2 U' D' L)` | 11 | U/D | 0c3 4e | 6 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 0c3-2 | 0c3-2 | look anyway | 0 | 0 | 0.37% |
| 2 | 2c3-3 | 2c3-3 | look anyway | 0.35% | 2.6% | 15% |
| 3 | 2c4-3 | 2c4-7 | look anyway | 0.79% | 4.8% | 19% |
| 4 | 0c0-1 | 0c0-1 | look anyway | 62% | 90% | 99.5% |
| 5 | 0c3-2 | 0c3-2 | drop | 0 | 0 | 0.28% |
| 6 | 2c3-3 | 2c3-2 | keep | 0.77% | 5.6% | 29% |
| 7 | 4b5-2 | 4b5-1 | drop | 0.01% | 0.14% | 1.4% |
| 8 | 0c3-2 | 0c3-2 | drop | 0 | 0 | 0.70% |

Shown: 8 of the 186 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 14; 11 moves: 4 of 170).

<details>
<summary>Answers for scramble 74</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 12 | 12 | 16 | 24 |
| 2 | 7 | 9 | 14 | 22 |
| 3 | 7 | 9 | 14 | 24 |
| 4 | 2 | 2 | 8 | 18 |
| 5 | 12 | 12 | 14 | 25 |
| 6 | 6 | 6 | 13 | 23 |
| 7 | 10 | 9 | 14 | 25 |
| 8 | 12 | 12 | 15 | 26 |

Best on the page: **18 moves**, from DR 4: `D2 F2 D2 U2 R2 F' B' U2 R' B L2 F' L' U F' D L2 B`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 75

```
R' U' F U2 L2 B' D2 B' F' L2 U2 L2 F2 R U L2 B D' B' L' F' L B' U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' B' U2 L' B R2 F (D' B' U)` | 10 | R/L | 2c3 4e | 0 |
| 2 | `U (F2 D B' U' L2 F B L' F)` | 10 | R/L | 4c3 2e | 4 |
| 3 | `D R' U2 R U (U F R D F)` | 10 | R/L | 2c4 4e | 3 |
| 4 | `L' U L' U' F2 B U2 D L' U` | 10 | R/L | 4c3 4e | 3 |
| 5 | `U' F2 B D2 R' F U2 B (D' B' U)` | 11 | R/L | 2c3 4e | 0 |
| 6 | `U L' U' B' D2 B' R2 B D (U L)` | 11 | F/B | 4c4 2e | 4 |
| 7 | `L' U L' U' F2 B' U2 R2 D L' U` | 11 | R/L | 4b5 2e | 0 |
| 8 | `(F' L D' F2 R B U2 F B' L2 U)` | 11 | F/B | 2c3 2e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-2 | look anyway | 0.19% | 1.9% | 13% |
| 2 | 4c3-7 | 4c3-5 | look anyway | 0.49% | 2.4% | 13% |
| 3 | 2c4-7 | 2c4-6 | look anyway | <0.01% | 0.30% | 3.1% |
| 4 | 4c3-1 | 4c3-5 | look anyway | 0.89% | 5.0% | 25% |
| 5 | 2c3-3 | 2c3-2 | keep | 0.19% | 1.9% | 13% |
| 6 | 4c4-4 | 4c4-6 | drop | 0 | 0 | 0.38% |
| 7 | 4b5-2 | 4b5-2 | drop | 0 | 0.02% | 0.31% |
| 8 | 2c3-2 | 2c3-1 | keep | 4.0% | 18% | 57% |

Shown: 8 of the 137 DRs up to 11 moves (10 moves: 4 of 11; 11 moves: 4 of 126).

<details>
<summary>Answers for scramble 75</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 7 | 13 | 22 |
| 2 | 8 | 9 | 13 | 23 |
| 3 | 10 | 8 | 15 | 23 |
| 4 | 8 | 9 | 12 | 22 |
| 5 | 8 | 7 | 13 | 23 |
| 6 | 10 | 11 | 15 | 25 |
| 7 | 10 | 10 | 14 | 25 |
| 8 | 6 | 7 | 11 | 22 |

Best on the page: **22 moves**, from DR 1 (DRs 4 and 8 tie it): `U' B' U2 L' B R2 F' U2 L' D2 B2 R F2 L2 B2 L' B2 D2 B2 U' B D`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 76

```
R' U' F U F2 R F2 B2 L U L' B' R F L2 U2 B2 D B2 U F2 B2 R2 U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L' B (L' F' L' U R F2 L)` | 9 | U/D | 4b5 0e | 0 |
| 2 | `L' B (L' F' L' U L D2 R)` | 9 | U/D | 4b5 0e | 2 |
| 3 | `(L' F' D B R U L U' F2 U)` | 10 | R/L | 4c4 4e | 1 |
| 4 | `F2 R' U (R' D' F2 L B' R' F)` | 10 | R/L | 2c5 4e | 1 |
| 5 | `L' B (L' F' L' U L' D L2 D2 R)` | 11 | U/D | 2c4 4e | 2 |
| 6 | `R B2 D' R' B2 L2 D2 B' R F (D)` | 11 | R/L | 4b2 2e | 2 |
| 7 | `B2 R D (B' D' F' L' R' F B L)` | 11 | F/B | 4c3 4e | 3 |
| 8 | `L' B (L' F' L' U R U2 D2 B2 R)` | 11 | U/D | 4b5 0e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b5-1 | 4b5-2 | look anyway | 0 | 0.06% | 1.1% |
| 2 | 4b5-1 | 4b5-2 | look anyway | 0.03% | 0.24% | 1.7% |
| 3 | 4c4-2 | 4c4-1 | look anyway | 0.12% | 0.66% | 4.3% |
| 4 | 2c5-3 | 2c5-2 | look anyway | 0 | 0 | 0.14% |
| 5 | 2c4-6 | 2c4-6 | drop | 0.08% | 0.53% | 3.7% |
| 6 | 4b2-3 | 4b2-4 | keep | 0.77% | 5.2% | 27% |
| 7 | 4c3-5 | 4c3-9 | drop | 0.02% | 0.39% | 3.8% |
| 8 | 4b5-1 | 4b5-2 | drop | 0 | 0 | 0.47% |

Shown: 8 of the 122 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 13; 11 moves: 4 of 107).

<details>
<summary>Answers for scramble 76</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 10 | 15 | 23 |
| 2 | 9 | 10 | 14 | 22 |
| 3 | 10 | 9 | 15 | 25 |
| 4 | 11 | 11 | 15 | 24 |
| 5 | 8 | 8 | 15 | 25 |
| 6 | 7 | 8 | 14 | 23 |
| 7 | 10 | 10 | 14 | 24 |
| 8 | 9 | 10 | 15 | 26 |

Best on the page: **22 moves**, from DR 2: `L' B U B2 U' L2 U F2 B2 L2 D' F2 D' B2 L2 R D2 L' U' L F L`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 77

```
R' U' F D2 B2 U2 L2 B2 L2 B2 U F2 U B' L' U2 B D2 U F U2 R' B2 D2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(U' R' U' B R U2 B2 L D)` | 9 | R/L | 2c3 6e | 0 |
| 2 | `(F2 R' U' B' L' D2 L2 F2 L2 D)` | 10 | R/L | 2c3 2e | 2 |
| 3 | `L (B' L' R D' F L2 D F D)` | 10 | F/B | 0c3 2e | 3 |
| 4 | `(U F2 R' U' B' D2 L B2 R' U)` | 10 | R/L | 4a1 4e | 0 |
| 5 | `(B2 D B U2 R' D' L U R2 D R)` | 11 | U/D | 4c4 2e | 1 |
| 6 | `U (L2 D R D' R2 F' R U2 L2 B)` | 11 | R/L | 4a1 4e | 1 |
| 7 | `F2 B' U L' R2 B U2 L2 F (L D)` | 11 | R/L | 2c5 6e | 1 |
| 8 | `R' F B (F' U' R2 D2 R D' L' U)` | 11 | R/L | 2c3 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-1 | 2c3-2 | look anyway | 0.40% | 3.1% | 18% |
| 2 | 2c3-3 | 2c3-3 | look anyway | 0.65% | 4.7% | 25% |
| 3 | 0c3-1 | 0c3-2 | look anyway | 0.09% | 0.68% | 4.2% |
| 4 | 4a1-3 | 4a1-2 | look anyway | 2.6% | 11% | 40% |
| 5 | 4c4-4 | 4c4-3 | drop | 0 | 0.03% | 0.54% |
| 6 | 4a1-2 | 4a1-3 | keep | 3.3% | 14% | 46% |
| 7 | 2c5-3 | 2c5-1 | drop | 0 | 0 | 0.49% |
| 8 | 2c3-3 | 2c3-2 | keep | 0.66% | 4.2% | 22% |

Shown: 8 of the 950 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 65; 11 moves: 4 of 884).

<details>
<summary>Answers for scramble 77</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 9 | 13 | 22 |
| 2 | 7 | 7 | 13 | 23 |
| 3 | 11 | 10 | 15 | 24 |
| 4 | 6 | 8 | 13 | 23 |
| 5 | 10 | 10 | 13 | 24 |
| 6 | 7 | 7 | 11 | 20 |
| 7 | 12 | 10 | 15 | 25 |
| 8 | 9 | 8 | 14 | 24 |

Best on the page: **20 moves**, from DR 6: `U' L' F2 B2 R U2 B2 R F2 R2 B L2 U2 R' F R2 D R' D' L2`. The list drops 2 of the 4 DRs of 11 moves or more, and keeps the best one.

</details>

#### Scramble 78

```
R' U' F R2 D' L2 D' L2 B2 D' F2 L2 U' B R U F2 D B2 U L' U2 R U2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `B2 U' R (R B2 D' R2 F' D)` | 9 | F/B | 4c3 4e | 1 |
| 2 | `F2 R' U L B2 R (F B' U' B)` | 10 | U/D | 4b5 2e | 2 |
| 3 | `U (R U F U F U2 F' D2 B)` | 10 | R/L | 2c3 4e | 2 |
| 4 | `R F' R2 F (F' L' D R' D2 L)` | 10 | U/D | 4c3 2e | 2 |
| 5 | `F' R' F D' B2 R2 U D2 R' D (F)` | 11 | R/L | 4b5 2e | 3 |
| 6 | `U' B2 R (R' F B2 L2 B2 D' F2 D)` | 11 | F/B | 4c3 2e | 2 |
| 7 | `F' R' F' U' D L' R D2 L D (F)` | 11 | R/L | 2c3 4e | 1 |
| 8 | `B2 U' R (R B2 U' B2 U D' F' D)` | 11 | F/B | 4c3 2e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c3-5 | 4c3-7 | look anyway | 0.06% | 0.79% | 6.0% |
| 2 | 4b5-1 | 4b5-1 | look anyway | 0.02% | 0.24% | 2.3% |
| 3 | 2c3-3 | 2c3-3 | look anyway | 0.35% | 2.6% | 15% |
| 4 | 4c3-5 | 4c3-6 | look anyway | 0.12% | 1.2% | 8.1% |
| 5 | 4b5-1 | 4b5-1 | drop | 0.04% | 0.38% | 3.3% |
| 6 | 4c3-5 | 4c3-2 | keep | 0.38% | 2.6% | 15% |
| 7 | 2c3-2 | 2c3-1 | keep | 0.88% | 6.1% | 29% |
| 8 | 4c3-5 | 4c3-7 | drop | 0.11% | 1.1% | 7.6% |

Shown: 8 of the 278 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 21; 11 moves: 4 of 256).

<details>
<summary>Answers for scramble 78</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 8 | 13 | 21 |
| 2 | 10 | 9 | 15 | 24 |
| 3 | 9 | 9 | 14 | 22 |
| 4 | 9 | 9 | 14 | 24 |
| 5 | 10 | 10 | 13 | 23 |
| 6 | 9 | 9 | 14 | 24 |
| 7 | 8 | 7 | 12 | 22 |
| 8 | 9 | 8 | 14 | 25 |

Best on the page: **21 moves**, from DR 1: `B2 U' R' U2 B2 R2 B R2 F L2 F2 R2 U2 F R2 D F R2 D B2 R'`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 79

```
R' U' F L2 U B2 L2 B2 D2 U' F2 D' B' U' L U B2 D L' B U' L2 R U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L R F' L R (L B' R' D)` | 9 | F/B | 2c4 4e | 1 |
| 2 | `L R F L R (L B' R' D)` | 9 | F/B | 2c4 4e | 2 |
| 3 | `(D L2 F' D B' L' D L R U)` | 10 | R/L | 4c4 2e | 5 |
| 4 | `F2 L R F L R (L B' R' D)` | 10 | F/B | 2c4 4e | 2 |
| 5 | `B (R' F' R B D' F2 L D' L2 U)` | 11 | R/L | 2c4 2e | 3 |
| 6 | `L F2 U' D' L2 R' F D2 L2 B' D` | 11 | F/B | 4b2 4e | 2 |
| 7 | `(D F D B' L U' R' U2 L2 B2 U)` | 11 | R/L | 2c3 4e | 1 |
| 8 | `F2 L R F D2 L R (L B' R' D)` | 11 | F/B | 2c4 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-4 | 2c4-3 | look anyway | 0.08% | 0.76% | 5.9% |
| 2 | 2c4-4 | 2c4-3 | look anyway | 0.13% | 1.1% | 7.8% |
| 3 | 4c4-3 | 4c4-4 | look anyway | 0 | 0.48% | 4.7% |
| 4 | 2c4-4 | 2c4-3 | look anyway | 0.13% | 1.1% | 7.8% |
| 5 | 2c4-4 | 2c4-2 | drop | 0.19% | 2.2% | 14% |
| 6 | 4b2-4 | 4b2-1 | keep | 1.9% | 8.9% | 35% |
| 7 | 2c3-3 | 2c3-3 | keep | 0.19% | 1.6% | 11% |
| 8 | 2c4-7 | 2c4-3 | drop | 0.07% | 0.72% | 5.7% |

Shown: 8 of the 388 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 39; 11 moves: 4 of 347).

<details>
<summary>Answers for scramble 79</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 10 | 14 | 22 |
| 2 | 8 | 10 | 14 | 22 |
| 3 | 10 | 10 | 15 | 25 |
| 4 | 9 | 10 | 14 | 23 |
| 5 | 9 | 9 | 14 | 23 |
| 6 | 9 | 7 | 13 | 24 |
| 7 | 7 | 7 | 13 | 24 |
| 8 | 10 | 10 | 14 | 24 |

Best on the page: **22 moves**, from DR 1 (DR 2 ties it): `L R F' L R U2 F D2 F B2 L2 D2 L2 U2 B' D2 F U2 D R B L'`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 80

```
R' U' F U L D R' U2 F B L2 D' B2 R L2 B L2 D2 B L2 B2 R2 B U2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `B R F (D' R' B2 U R2 U)` | 9 | R/L | 2c4 4e | 1 |
| 2 | `B R F (D' R' B2 D B2 D)` | 9 | R/L | 2c4 4e | 0 |
| 3 | `(B' D R' B D F2 R2 U2 R)` | 9 | F/B | 4b5 2e | 1 |
| 4 | `B D L F R F' B' L B` | 9 | R/L | 4b2 4e | 0 |
| 5 | `U2 B D' R2 D2 L2 B R' B2 U2 B` | 11 | R/L | 2c4 2e | 2 |
| 6 | `B D' F2 R' F L R2 F2 D2 F R` | 11 | F/B | 4c4 2e | 2 |
| 7 | `B' R F' U2 F2 U2 B2 D L' F2 R` | 11 | U/D | 4c3 4e | 2 |
| 8 | `U2 L' D2 B' L' B' R (L2 D2 R' D)` | 11 | F/B | 4b2 2e | 5 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-4 | 2c4-1 | look anyway | 0.10% | 1.0% | 8.2% |
| 2 | 2c4-4 | 2c4-1 | look anyway | 0.05% | 0.65% | 5.9% |
| 3 | 4b5-1 | 4b5-1 | look anyway | <0.01% | 0.08% | 1.2% |
| 4 | 4b2-2 | 4b2-3 | look anyway | 0.34% | 3.2% | 20% |
| 5 | 2c4-6 | 2c4-5 | drop | 0 | 0.41% | 4.2% |
| 6 | 4c4-3 | 4c4-4 | drop | 0 | 0.05% | 0.96% |
| 7 | 4c3-4 | 4c3-3 | drop | 0.65% | 3.5% | 17% |
| 8 | 4b2-1 | 4b2-3 | keep | 13% | 35% | 75% |

Shown: 8 of the 1,690 DRs up to 11 moves (9 moves: 4 of 11; 10 moves: 0 of 161; 11 moves: 4 of 1,518).

<details>
<summary>Answers for scramble 80</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 8 | 14 | 22 |
| 2 | 9 | 8 | 14 | 22 |
| 3 | 9 | 10 | 15 | 23 |
| 4 | 7 | 7 | 13 | 22 |
| 5 | 9 | 10 | 14 | 24 |
| 6 | 10 | 10 | 15 | 25 |
| 7 | 8 | 10 | 11 | 22 |
| 8 | 5 | 5 | 12 | 23 |

Best on the page: **22 moves**, from DR 1 (DRs 2, 4 and 7 tie it): `B R F' U2 R F2 R' U2 R' L2 F2 L' F2 D2 F2 R2 U' R2 U' B2 R D`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 81

```
R' U' F D2 R' F2 B2 U F B' U D2 L F D' F2 D' L2 D L2 U B2 D' F2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(F' U B' U F L F2 U R)` | 9 | U/D | 0c4 6e | 0 |
| 2 | `(L B2 U B' R' U D2 F2 D F)` | 10 | U/D | 4c3 2e | 0 |
| 3 | `(B D2 R B2 L' B2 D' B U' B)` | 10 | U/D | 2c3 6e | 0 |
| 4 | `U' F' U' F (B R U' B2 U L)` | 10 | U/D | 4a1 2e | 4 |
| 5 | `(F' B U' F L R' U D' L' U' L)` | 11 | U/D | 2c5 2e | 2 |
| 6 | `R2 D2 R F D (L B' L' D2 L F)` | 11 | R/L | 4c4 4e | 2 |
| 7 | `(B' L2 F D F U2 D2 L' D B2 R)` | 11 | U/D | 2c3 2e | 3 |
| 8 | `L F (L2 D' B L' R2 B2 D' L R)` | 11 | U/D | 4c4 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 0c4-1 | 0c4-1 | look anyway | 0.01% | 0.11% | 1.9% |
| 2 | 4c3-4 | 4c3-2 | look anyway | 0.09% | 1.4% | 10% |
| 3 | 2c3-2 | 2c3-3 | look anyway | 0.14% | 1.3% | 9.5% |
| 4 | 4a1-4 | 4a1-2 | look anyway | 3.7% | 18% | 57% |
| 5 | 2c5-1 | 2c5-1 | drop | 0.01% | 0.32% | 3.4% |
| 6 | 4c4-5 | 4c4-4 | drop | 0 | <0.01% | 0.20% |
| 7 | 2c3-3 | 2c3-1 | keep | 2.8% | 14% | 51% |
| 8 | 4c4-4 | 4c4-3 | drop | 0 | 0.02% | 0.78% |

Shown: 8 of the 487 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 41; 11 moves: 4 of 445).

<details>
<summary>Answers for scramble 81</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 10 | 15 | 23 |
| 2 | 9 | 8 | 13 | 22 |
| 3 | 9 | 8 | 14 | 24 |
| 4 | 7 | 7 | 13 | 22 |
| 5 | 10 | 10 | 15 | 25 |
| 6 | 11 | 11 | 14 | 24 |
| 7 | 7 | 6 | 13 | 24 |
| 8 | 10 | 10 | 14 | 24 |

Best on the page: **22 moves**, from DR 2 (DR 4 ties it): `U2 L2 D B2 U' R2 D' F2 D R2 D' B2 F D' F2 D2 U' R B U' B2 L'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 82

```
R' U' F R2 D' U' L2 D L2 R2 U' B2 L2 F U F2 L U2 L2 B F L R2 U2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `B2 L2 F' D (D' R' B' U' R)` | 9 | F/B | 2c3 2e | 1 |
| 2 | `(B' L2 F R' D B2 U F2 L)` | 9 | U/D | 4b2 4e | 5 |
| 3 | `(F' D2 B L' U B2 D F2 R)` | 9 | U/D | 4b2 4e | 5 |
| 4 | `F2 R2 F' U (D' R' B' U' R)` | 9 | F/B | 2c3 2e | 1 |
| 5 | `U L2 D2 L (D' F2 D2 F2 B R2 U)` | 11 | F/B | 2c5 2e | 1 |
| 6 | `(F2 B R2 F L' U L B2 D F2 R)` | 11 | U/D | 2c3 6e | 4 |
| 7 | `(F' D2 B U' L2 B2 D F2 L2 U' R)` | 11 | U/D | 2c4 6e | 2 |
| 8 | `L2 D2 L' U' B' D F R2 B2 D2 B` | 11 | U/D | 2c4 6e | 0 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-3 | look anyway | 0.44% | 3.7% | 22% |
| 2 | 4b2-3 | 4b2-3 | look anyway | 5.2% | 20% | 57% |
| 3 | 4b2-3 | 4b2-3 | look anyway | 5.2% | 20% | 57% |
| 4 | 2c3-3 | 2c3-3 | look anyway | 0.44% | 3.7% | 22% |
| 5 | 2c5-1 | 2c5-1 | drop | 0 | 0.16% | 2.2% |
| 6 | 2c3-2 | 2c3-1 | keep | 2.7% | 13% | 46% |
| 7 | 2c4-5 | 2c4-4 | drop | 0.03% | 0.73% | 5.4% |
| 8 | 2c4-4 | 2c4-7 | drop | 0 | 0.06% | 1.0% |

Shown: 8 of the 856 DRs up to 11 moves (9 moves: 4 of 4; 10 moves: 0 of 66; 11 moves: 4 of 786).

<details>
<summary>Answers for scramble 82</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 6 | 7 | 14 | 21 |
| 2 | 8 | 7 | 12 | 21 |
| 3 | 7 | 7 | 13 | 22 |
| 4 | 6 | 7 | 14 | 22 |
| 5 | 10 | 10 | 14 | 25 |
| 6 | 8 | 8 | 14 | 24 |
| 7 | 10 | 9 | 15 | 25 |
| 8 | 9 | 10 | 15 | 25 |

Best on the page: **21 moves**, from DR 1 (DR 2 ties it): `B2 L2 F' D' R2 F B2 R2 F2 R2 F D2 R2 B' U2 L2 R U B R D`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 83

```
R' U' F U R B2 R' F2 D' L U' B' R L2 F2 D B2 U2 F2 R2 U' D' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(F U' R' B' U D2 L' F2 D)` | 9 | R/L | 4b2 2e | 4 |
| 2 | `L2 U' F (R F' R D F2 B2 L)` | 10 | U/D | 2c4 4e | 0 |
| 3 | `B D' L' D2 R F2 L2 D R2 D` | 10 | F/B | 4c3 2e | 1 |
| 4 | `(F U' R' B R2 B2 U' R' B2 D)` | 10 | R/L | 4c4 2e | 3 |
| 5 | `R' F' R (U2 R F' U' D' F2 B' U)` | 11 | F/B | 4c4 4e | 0 |
| 6 | `B (B U2 F R' D2 F2 D R' D2 R)` | 11 | U/D | 2c4 4e | 1 |
| 7 | `(F U' R' B D' R2 B2 U' R F2 U)` | 11 | R/L | 2c3 2e | 3 |
| 8 | `B D' L' D2 R' B2 R2 F2 D R2 D` | 11 | F/B | 4c3 2e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-3 | 4b2-3 | look anyway | 3.2% | 15% | 49% |
| 2 | 2c4-1 | 2c4-6 | look anyway | 0.05% | 0.55% | 5.2% |
| 3 | 4c3-5 | 4c3-9 | look anyway | <0.01% | 0.10% | 1.6% |
| 4 | 4c4-3 | 4c4-4 | look anyway | 0 | 0.09% | 1.5% |
| 5 | 4c4-4 | 4c4-5 | drop | 0 | 0 | 0.06% |
| 6 | 2c4-6 | 2c4-7 | drop | 0 | 0.07% | 1.5% |
| 7 | 2c3-1 | 2c3-2 | keep | 4.0% | 18% | 57% |
| 8 | 4c3-5 | 4c3-9 | drop | <0.01% | 0.21% | 2.6% |

Shown: 8 of the 180 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 13; 11 moves: 4 of 166).

<details>
<summary>Answers for scramble 83</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 6 | 6 | 13 | 22 |
| 2 | 8 | 8 | 14 | 24 |
| 3 | 9 | 10 | 14 | 23 |
| 4 | 10 | 11 | 14 | 24 |
| 5 | 11 | 11 | 14 | 24 |
| 6 | 8 | 9 | 11 | 21 |
| 7 | 6 | 6 | 12 | 23 |
| 8 | 9 | 10 | 15 | 25 |

Best on the page: **21 moves**, from DR 6: `B' U' R2 D R2 D' B2 D' F2 D2 F2 R' D2 R D' F2 D2 R F' U2 B'`. The list drops 3 of the 4 DRs of 11 moves or more, the best one among them. What's left gives 22 (DR 1), 1 move more.

</details>

#### Scramble 84

```
R' U' F U L D' L2 B2 D2 B D F2 B2 R' D F2 B2 U' F2 U D2 B2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L (U2 F' U R B U2 F)` | 8 | U/D | 4c3 4e | 1 |
| 2 | `L (U2 F' U R F R2 B)` | 8 | U/D | 4c3 4e | 2 |
| 3 | `L (U2 F' U R F2 B' D2 F)` | 9 | U/D | 4c3 4e | 3 |
| 4 | `L (U2 F' U R F' B2 L2 B)` | 9 | U/D | 4c3 4e | 3 |
| 5 | `L (U2 F' U R U2 F2 R2 B' R2 F)` | 11 | U/D | 4b5 4e | 2 |
| 6 | `L (U2 F' U R F R2 F R2 F B)` | 11 | U/D | 4c3 4e | 3 |
| 7 | `R (D R' U2 L' D F' U2 D' R2 U)` | 11 | F/B | 2c5 4e | 4 |
| 8 | `L (U2 F' U R F R2 F' R2 F B)` | 11 | U/D | 4c3 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c3-5 | 4c3-1 | look anyway | 0.22% | 2.1% | 14% |
| 2 | 4c3-5 | 4c3-1 | look anyway | 0.41% | 3.3% | 19% |
| 3 | 4c3-5 | 4c3-1 | look anyway | 0.89% | 5.0% | 25% |
| 4 | 4c3-5 | 4c3-1 | look anyway | 0.89% | 5.0% | 25% |
| 5 | 4b5-1 | 4b5-2 | drop | 0 | 0.07% | 1.0% |
| 6 | 4c3-5 | 4c3-7 | drop | 0.24% | 1.8% | 11% |
| 7 | 2c5-2 | 2c5-3 | drop | 0 | 0 | 0.69% |
| 8 | 4c3-5 | 4c3-9 | drop | 0.02% | 0.31% | 2.7% |

Shown: 8 of the 245 DRs up to 11 moves (8 moves: 2 of 2; 9 moves: 2 of 3; 10 moves: 0 of 26; 11 moves: 4 of 214).

<details>
<summary>Answers for scramble 84</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 8 | 13 | 21 |
| 2 | 9 | 8 | 12 | 20 |
| 3 | 9 | 8 | 13 | 22 |
| 4 | 9 | 8 | 13 | 22 |
| 5 | 10 | 10 | 14 | 25 |
| 6 | 9 | 9 | 14 | 24 |
| 7 | 10 | 11 | 15 | 25 |
| 8 | 9 | 9 | 13 | 24 |

Best on the page: **20 moves**, from DR 2: `L U2 B2 R2 D R2 D L2 B2 D2 B2 D' R2 B' R2 F' R' U' F U2`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 85

```
R' U' F D L2 R2 U B2 L2 B2 L2 R2 U L' D R D L2 F B U2 L' R B' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(U R2 B' U' R2 F2 B2 R' B)` | 9 | R/L | 2c3 2e | 1 |
| 2 | `D B' D L' U' D2 L U (B)` | 9 | R/L | 4c4 2e | 1 |
| 3 | `B D B2 L2 D (R2 F2 B2 L' B)` | 10 | R/L | 4c3 2e | 1 |
| 4 | `(B' R2 F' U F L' B R' B2 R)` | 10 | F/B | 4c4 4e | 2 |
| 5 | `D B' L2 D2 R D' R U' D2 L (B)` | 11 | U/D | 4c4 2e | 2 |
| 6 | `B (B2 L' B' U2 L' D L2 U' R2 U)` | 11 | R/L | 2c5 2e | 2 |
| 7 | `R' F2 U F2 L' U2 F2 D2 F' L (U)` | 11 | F/B | 4b2 4e | 3 |
| 8 | `D B' U2 R' D F2 D L R D (B)` | 11 | R/L | 2c3 2e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-2 | 2c3-1 | look anyway | 1.6% | 10% | 43% |
| 2 | 4c4-1 | 4c4-4 | look anyway | 0 | 0.14% | 1.8% |
| 3 | 4c3-4 | 4c3-9 | look anyway | 0.06% | 0.56% | 3.7% |
| 4 | 4c4-4 | 4c4-3 | look anyway | 0 | 0.06% | 1.2% |
| 5 | 4c4-1 | 4c4-4 | drop | 0.04% | 0.38% | 2.8% |
| 6 | 2c5-2 | 2c5-2 | drop | 0 | 0.05% | 0.90% |
| 7 | 4b2-3 | 4b2-1 | keep | 3.1% | 13% | 48% |
| 8 | 2c3-1 | 2c3-1 | keep | 2.5% | 14% | 50% |

Shown: 8 of the 575 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 59; 11 moves: 4 of 514).

<details>
<summary>Answers for scramble 85</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 6 | 6 | 13 | 22 |
| 2 | 9 | 11 | 14 | 23 |
| 3 | 9 | 10 | 14 | 23 |
| 4 | 11 | 10 | 14 | 24 |
| 5 | 11 | 10 | 14 | 25 |
| 6 | 10 | 10 | 15 | 25 |
| 7 | 7 | 7 | 12 | 22 |
| 8 | 6 | 6 | 13 | 23 |

Best on the page: **22 moves**, from DR 1 (DR 7 ties it): `R2 D2 F2 L2 U2 F2 U2 R D2 R' U2 B2 L B' R B2 F2 R2 U B R2 U'`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 86

```
R' U' F R2 D' R2 U B2 D U2 B2 L2 U' L B' L D2 F2 R' U L2 B D R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L2 D L' F (B2 R2 D L)` | 8 | U/D | 4c4 2e | 1 |
| 2 | `L' D2 L' U D R' U (L2 F)` | 9 | R/L | 4b2 2e | 3 |
| 3 | `L2 D L' F (L2 U' L2 B2 L)` | 9 | U/D | 4c4 2e | 0 |
| 4 | `L2 D L' F (L2 U' R2 F2 L)` | 9 | U/D | 4c4 2e | 1 |
| 5 | `(L2 F' L2 U' D R' B2 L' U B2 D)` | 11 | R/L | 2c4 6e | 1 |
| 6 | `L' F2 U R2 B2 R' D' L2 U (L2 F)` | 11 | R/L | 2c5 2e | 3 |
| 7 | `(L2 F L' R D R B2 R' B2 U' L)` | 11 | U/D | 2c5 4e | 1 |
| 8 | `(L2 F' D' L2 R' F2 R2 B2 U L D)` | 11 | R/L | 0c3 6e | 0 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-4 | 4c4-5 | look anyway | 0 | 0 | 0.09% |
| 2 | 4b2-1 | 4b2-1 | look anyway | 4.4% | 22% | 61% |
| 3 | 4c4-4 | 4c4-6 | look anyway | 0 | 0 | 0.12% |
| 4 | 4c4-4 | 4c4-6 | look anyway | 0 | 0 | 0.14% |
| 5 | 2c4-7 | 2c4-2 | drop | 0 | 0.07% | 2.2% |
| 6 | 2c5-3 | 2c5-2 | drop | 0 | 0 | 0.28% |
| 7 | 2c5-3 | 2c5-1 | drop | 0 | <0.01% | 0.37% |
| 8 | 0c3-1 | 0c3-2 | drop | 0 | 0.28% | 3.0% |

Shown: 8 of the 1,117 DRs up to 11 moves (8 moves: 1 of 1; 9 moves: 3 of 4; 10 moves: 0 of 83; 11 moves: 4 of 1,029).

<details>
<summary>Answers for scramble 86</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 11 | 16 | 23 |
| 2 | 6 | 6 | 10 | 19 |
| 3 | 11 | 11 | 15 | 23 |
| 4 | 11 | 11 | 15 | 23 |
| 5 | 10 | 10 | 14 | 25 |
| 6 | 11 | 10 | 14 | 24 |
| 7 | 12 | 10 | 16 | 26 |
| 8 | 11 | 10 | 14 | 25 |

Best on the page: **19 moves**, from DR 2: `L' D2 L' U D R' U L B2 R L2 F2 D2 F2 L B2 L' F' L2`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 87

```
R' U' F R2 U2 F2 D2 U L2 U2 B2 U' L2 F L2 U' F' R' U' B2 F L' B' U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `D' F2 L U' D' B' R2 F U2 R` | 10 | F/B | 2c4 2e | 3 |
| 2 | `R2 D2 B L' F2 B2 D' B2 R (F)` | 10 | U/D | 2c4 4e | 1 |
| 3 | `L2 U2 F L' F2 B2 U' F2 R (F)` | 10 | U/D | 2c4 6e | 2 |
| 4 | `L2 U2 F (F R' B2 D R' F2 L)` | 10 | U/D | 0c3 6e | 2 |
| 5 | `F2 D' L U D R' F L2 B U2 L` | 11 | F/B | 4c3 4e | 1 |
| 6 | `U' R2 B2 D' L D2 R (F D2 L B)` | 11 | U/D | 2c4 2e | 1 |
| 7 | `L2 U2 F' R' D2 R B2 U' F2 R (F)` | 11 | U/D | 2c3 4e | 1 |
| 8 | `D L F2 L U D (D' F D' L B)` | 11 | R/L | 2c3 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-6 | 2c4-6 | look anyway | 0.09% | 0.57% | 5.0% |
| 2 | 2c4-7 | 2c4-7 | look anyway | 0 | 0 | 0.22% |
| 3 | 2c4-7 | 2c4-7 | look anyway | 0 | 0.01% | 0.40% |
| 4 | 0c3-2 | 0c3-2 | look anyway | 0 | 0.34% | 3.4% |
| 5 | 4c3-3 | 4c3-5 | drop | 0.18% | 1.6% | 10% |
| 6 | 2c4-4 | 2c4-1 | drop | 0.11% | 1.1% | 9.4% |
| 7 | 2c3-3 | 2c3-3 | keep | 0.19% | 1.6% | 11% |
| 8 | 2c3-3 | 2c3-2 | keep | 1.3% | 6.5% | 29% |

Shown: 8 of the 148 DRs up to 11 moves (10 moves: 4 of 7; 11 moves: 4 of 141).

<details>
<summary>Answers for scramble 87</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 9 | 14 | 23 |
| 2 | 10 | 9 | 15 | 24 |
| 3 | 10 | 10 | 13 | 23 |
| 4 | 10 | 10 | 15 | 24 |
| 5 | 9 | 9 | 13 | 24 |
| 6 | 9 | 7 | 14 | 24 |
| 7 | 8 | 7 | 13 | 22 |
| 8 | 8 | 6 | 10 | 21 |

Best on the page: **21 moves**, from DR 8: `D L F2 L U D F2 R2 B2 L' F2 L' D2 L' B2 L2 B' L' D F' D`. The list drops 2 of the 4 DRs of 11 moves or more, and keeps the best one.

</details>

#### Scramble 88

```
R' U' F D R2 U2 L2 D R2 F2 U' R2 F2 B' R F' B L U' L2 R' B2 U' R' U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(L2 B2 R' U R' F L B)` | 8 | R/L | 0c3 2e | 4 |
| 2 | `L F U' R U2 F2 B' R' F` | 9 | R/L | 2c4 4e | 0 |
| 3 | `F L F U (L' U2 F' R B)` | 9 | R/L | 4b5 4e | 1 |
| 4 | `R B' L' F' R F2 U2 D L` | 9 | U/D | 2c4 4e | 3 |
| 5 | `(L2 B2 R' U R' F L F R2 F B)` | 11 | R/L | 0c3 2e | 5 |
| 6 | `L F U' R U2 F2 B2 R2 F R' B` | 11 | R/L | 2c4 2e | 2 |
| 7 | `(F2 U2 R' D' F L2 B2 L R B' L)` | 11 | F/B | 4c4 4e | 3 |
| 8 | `(F B L' F2 R D2 L2 B' U2 B' U)` | 11 | F/B | 4c4 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 0c3-1 | 0c3-1 | look anyway | 0.83% | 3.0% | 9.1% |
| 2 | 2c4-2 | 2c4-1 | look anyway | 0.10% | 1.5% | 12% |
| 3 | 4b5-1 | 4b5-1 | look anyway | <0.01% | 0.08% | 1.1% |
| 4 | 2c4-7 | 2c4-6 | look anyway | <0.01% | 0.30% | 3.1% |
| 5 | 0c3-1 | 0c3-2 | drop | 0.23% | 1.8% | 7.0% |
| 6 | 2c4-7 | 2c4-6 | drop | 0 | 0.12% | 2.3% |
| 7 | 4c4-3 | 4c4-4 | drop | 0 | 0.08% | 1.9% |
| 8 | 4c4-4 | 4c4-6 | drop | 0 | 0 | 0.10% |

Shown: 8 of the 901 DRs up to 11 moves (8 moves: 1 of 1; 9 moves: 3 of 4; 10 moves: 0 of 81; 11 moves: 4 of 815).

<details>
<summary>Answers for scramble 88</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 11 | 13 | 21 |
| 2 | 8 | 9 | 13 | 21 |
| 3 | 10 | 11 | 15 | 24 |
| 4 | 10 | 9 | 14 | 23 |
| 5 | 9 | 10 | 14 | 25 |
| 6 | 10 | 9 | 14 | 25 |
| 7 | 10 | 11 | 15 | 26 |
| 8 | 10 | 11 | 14 | 25 |

Best on the page: **21 moves**, from DR 1 (DR 2 ties it): `R' D2 B2 U2 B2 D2 R2 U2 L' F2 R2 U2 L B' L' F' R U' R B2 L2`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 8 moves long, so you'd finish it anyway.

</details>

#### Scramble 89

```
R' U' F D' L2 U' B2 U2 B2 U' F2 D' U' R' D2 U F R B' R' B2 R D L2 U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F D' B' U' F' D (U2 B2 U R)` | 10 | F/B | 4b2 4e | 5 |
| 2 | `(R' D' B2 R' B' U L2 B' L2 F)` | 10 | U/D | 2c5 6e | 2 |
| 3 | `D' F2 R (U B' D' L2 U L2 F)` | 10 | U/D | 4a1 2e | 2 |
| 4 | `(R' D' B2 R' B' U L2 F' D2 B)` | 10 | U/D | 2c5 6e | 1 |
| 5 | `(B' U B2 R D F D' F' U D2 F)` | 11 | U/D | 4c3 2e | 3 |
| 6 | `(B2 U R' D' B L2 U2 R2 D2 B' U)` | 11 | F/B | 4c4 4e | 2 |
| 7 | `D' F2 R (U B' D' F2 R2 D' R2 F)` | 11 | U/D | 4a1 2e | 2 |
| 8 | `F2 D' R (F U B' L2 B D B' U)` | 11 | F/B | 2c3 2e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b2-3 | 4b2-3 | look anyway | 5.2% | 20% | 57% |
| 2 | 2c5-1 | 2c5-1 | look anyway | 0.02% | 0.38% | 3.8% |
| 3 | 4a1-4 | 4a1-2 | look anyway | 1.5% | 9.3% | 40% |
| 4 | 2c5-1 | 2c5-1 | look anyway | 0.05% | 0.29% | 2.5% |
| 5 | 4c3-5 | 4c3-6 | drop | 0.15% | 1.6% | 11% |
| 6 | 4c4-5 | 4c4-2 | drop | 0 | 0.07% | 1.1% |
| 7 | 4a1-4 | 4a1-2 | keep | 1.5% | 9.3% | 40% |
| 8 | 2c3-2 | 2c3-2 | keep | 2.7% | 13% | 48% |

Shown: 8 of the 371 DRs up to 11 moves (10 moves: 4 of 22; 11 moves: 4 of 349).

<details>
<summary>Answers for scramble 89</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 8 | 13 | 22 |
| 2 | 9 | 10 | 14 | 24 |
| 3 | 8 | 7 | 13 | 22 |
| 4 | 9 | 10 | 15 | 24 |
| 5 | 8 | 8 | 14 | 25 |
| 6 | 11 | 9 | 14 | 24 |
| 7 | 8 | 7 | 12 | 23 |
| 8 | 6 | 7 | 13 | 23 |

Best on the page: **22 moves**, from DR 1 (DR 3 ties it): `F D' B' U' F' D B U2 B2 R2 L2 B R2 F' L2 U2 F' D2 R U' B2 U2`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 90

```
R' U' F U' B2 D' L2 B2 D' B2 U B2 U' L U F2 U L U' B' R' D L U2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F' U L R2 F U2 D L U` | 9 | R/L | 2c3 6e | 2 |
| 2 | `(R B' D' B2 L' B R2 U B)` | 9 | U/D | 2c3 4e | 3 |
| 3 | `F' D2 R2 D2 F (B' R' B' D' L)` | 10 | U/D | 2c3 4e | 1 |
| 4 | `R2 D2 L' D2 F (F2 L2 R2 U R)` | 10 | U/D | 2c4 6e | 0 |
| 5 | `U L R2 F B2 L2 U2 D' L' U2 R` | 11 | U/D | 4c4 2e | 2 |
| 6 | `R2 D' F R F L2 F' L (F L' U)` | 11 | F/B | 2c3 4e | 4 |
| 7 | `F2 U2 L' D2 B' D L' D' L2 B2 D` | 11 | R/L | 2c4 4e | 7 |
| 8 | `(D L2 R B U L' F2 R2 D F2 L)` | 11 | U/D | 2c3 8e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-1 | 2c3-2 | look anyway | 1.0% | 6.4% | 30% |
| 2 | 2c3-2 | 2c3-2 | look anyway | 1.9% | 9.7% | 36% |
| 3 | 2c3-2 | 2c3-2 | look anyway | 0.49% | 3.9% | 21% |
| 4 | 2c4-1 | 2c4-7 | look anyway | 0 | 0.18% | 2.7% |
| 5 | 4c4-5 | 4c4-4 | drop | 0 | <0.01% | 0.22% |
| 6 | 2c3-1 | 2c3-2 | keep | 4.6% | 18% | 55% |
| 7 | 2c4-2 | 2c4-4 | keep | 1.2% | 6.5% | 27% |
| 8 | 2c3-3 | 2c3-1 | keep | 0.09% | 1.1% | 10% |

Shown: 8 of the 397 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 39; 11 moves: 4 of 356).

<details>
<summary>Answers for scramble 90</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 7 | 9 | 13 | 22 |
| 2 | 7 | 8 | 11 | 20 |
| 3 | 7 | 7 | 13 | 23 |
| 4 | 8 | 10 | 14 | 23 |
| 5 | 11 | 11 | 15 | 26 |
| 6 | 6 | 6 | 13 | 23 |
| 7 | 8 | 9 | 13 | 23 |
| 8 | 10 | 9 | 13 | 23 |

Best on the page: **20 moves**, from DR 2: `U2 R2 B2 U L2 F2 U' B2 U' L2 U2 B' U' R2 B' L B2 D B R'`. The list drops 1 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 91

```
R' U' F R' F R' U B' U2 F D' F2 B L' U D L2 B2 R2 D2 F2 U' R2 B2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `R' B2 R U' F D2 F L (U)` | 9 | F/B | 4b5 4e | 3 |
| 2 | `F' L2 U' L (R F R2 B' D)` | 9 | F/B | 2c3 0e | 1 |
| 3 | `R' B2 R U' F' B2 U2 F R (U)` | 10 | F/B | 4b5 4e | 4 |
| 4 | `D L2 U2 R' B2 D' B L2 F (L)` | 10 | U/D | 2c4 4e | 2 |
| 5 | `F' D L B L' D' F' D F B2 U` | 11 | F/B | 2c4 4e | 2 |
| 6 | `D' R (D F L B2 D F2 U D2 F)` | 11 | U/D | 2c4 6e | 2 |
| 7 | `B2 U' F2 L2 B U2 F' R D2 R (U)` | 11 | F/B | 2c4 4e | 3 |
| 8 | `D' R U F R' U F2 D B2 U F` | 11 | U/D | 4b5 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b5-1 | 4b5-1 | look anyway | 0.02% | 0.27% | 2.9% |
| 2 | 2c3-3 | 2c3-1 | look anyway | 0 | 0.23% | 5.1% |
| 3 | 4b5-1 | 4b5-1 | look anyway | 0.06% | 0.66% | 5.8% |
| 4 | 2c4-7 | 2c4-7 | look anyway | 0 | 0.02% | 0.68% |
| 5 | 2c4-6 | 2c4-5 | drop | 0.06% | 0.59% | 4.3% |
| 6 | 2c4-6 | 2c4-4 | drop | 0.03% | 0.37% | 3.3% |
| 7 | 2c4-3 | 2c4-7 | drop | 0.13% | 1.2% | 8.1% |
| 8 | 4b5-2 | 4b5-2 | drop | 0 | <0.01% | 0.41% |

Shown: 8 of the 249 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 14; 11 moves: 4 of 233).

<details>
<summary>Answers for scramble 91</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 9 | 15 | 23 |
| 2 | 10 | 9 | 14 | 22 |
| 3 | 10 | 9 | 14 | 24 |
| 4 | 10 | 10 | 14 | 23 |
| 5 | 8 | 9 | 14 | 25 |
| 6 | 9 | 9 | 14 | 24 |
| 7 | 9 | 10 | 13 | 24 |
| 8 | 10 | 10 | 15 | 26 |

Best on the page: **22 moves**, from DR 2: `F' L2 U' L' F2 U2 B' L2 U2 F' U2 B2 U2 R2 U2 F' L2 D' B R2 F' R'`. The list drops 4 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 92

```
R' U' F D2 L2 R2 D L2 D2 R2 F2 R2 U' F D' R U R' U2 L D U2 B F2 U' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F L' R2 F' D (U' B' L)` | 8 | F/B | 4c4 4e | 3 |
| 2 | `L' R2 F' D (U F' U2 B' L)` | 9 | F/B | 4c4 4e | 4 |
| 3 | `U' F (D' B R2 D F2 U' L)` | 9 | U/D | 4c4 4e | 3 |
| 4 | `(L B U' L' D2 F' R2 F L2 B)` | 10 | U/D | 4b2 4e | 2 |
| 5 | `B R D (L' U' R' B2 R' B' R2 F)` | 11 | R/L | 2c4 6e | 2 |
| 6 | `(L B U' L' U2 B R2 U2 F R2 B)` | 11 | U/D | 4b2 4e | 3 |
| 7 | `(L2 B' D B2 L F2 U B2 L2 D' F)` | 11 | U/D | 4b5 4e | 3 |
| 8 | `(F R2 U' F2 L' D L2 R2 D2 F D)` | 11 | F/B | 4b5 2e | 0 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c4-2 | 4c4-6 | look anyway | 0 | 0.12% | 1.6% |
| 2 | 4c4-2 | 4c4-5 | look anyway | 0 | 0.16% | 2.1% |
| 3 | 4c4-2 | 4c4-6 | look anyway | 0 | 0.12% | 1.6% |
| 4 | 4b2-1 | 4b2-4 | look anyway | 1.9% | 8.9% | 35% |
| 5 | 2c4-1 | 2c4-5 | drop | 0.27% | 2.1% | 13% |
| 6 | 4b2-4 | 4b2-2 | keep | 1.6% | 8.9% | 38% |
| 7 | 4b5-2 | 4b5-1 | drop | <0.01% | 0.13% | 1.8% |
| 8 | 4b5-1 | 4b5-2 | drop | <0.01% | 0.03% | 0.58% |

Shown: 8 of the 627 DRs up to 11 moves (8 moves: 1 of 1; 9 moves: 2 of 2; 10 moves: 1 of 64; 11 moves: 4 of 560).

<details>
<summary>Answers for scramble 92</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 11 | 16 | 23 |
| 2 | 10 | 11 | 14 | 23 |
| 3 | 10 | 12 | 15 | 24 |
| 4 | 6 | 8 | 12 | 22 |
| 5 | 9 | 10 | 14 | 24 |
| 6 | 8 | 7 | 13 | 23 |
| 7 | 11 | 10 | 14 | 25 |
| 8 | 9 | 10 | 13 | 24 |

Best on the page: **22 moves**, from DR 4: `U' R2 B2 D2 L2 F2 R2 U' L2 U2 L2 F2 B' L2 F' R2 F D2 L U B' L'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 93

```
R' U' F L2 F2 L2 U2 B2 D2 B2 D F2 U' L F2 U' B L' B' R2 U' F' R B' U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' F' L2 F' R' U F2 B2 R (F)` | 10 | U/D | 4c3 4e | 1 |
| 2 | `F R (R' B' R' F D' L2 U B)` | 10 | U/D | 4a1 2e | 2 |
| 3 | `R D L' B' U' B2 D' B (F L)` | 10 | U/D | 4c3 4e | 3 |
| 4 | `L R F' L' D F2 U R2 B' U` | 10 | F/B | 2c4 2e | 3 |
| 5 | `(L' F B L' B R U D L2 B2 L)` | 11 | U/D | 4c3 4e | 1 |
| 6 | `L R' F' L' U2 F2 D B' U2 B' U` | 11 | F/B | 2c4 4e | 2 |
| 7 | `B2 D L2 D R2 U (L' F U L R)` | 11 | F/B | 2c4 6e | 0 |
| 8 | `R U L' B L (D F' L2 U' B2 D)` | 11 | F/B | 4b5 2e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c3-3 | 4c3-4 | look anyway | 0.22% | 1.7% | 12% |
| 2 | 4a1-3 | 4a1-4 | look anyway | 0.59% | 5.0% | 27% |
| 3 | 4c3-2 | 4c3-5 | look anyway | 0.78% | 4.2% | 22% |
| 4 | 2c4-2 | 2c4-4 | look anyway | 0.19% | 2.2% | 14% |
| 5 | 4c3-7 | 4c3-4 | drop | 0.17% | 1.5% | 9.0% |
| 6 | 2c4-4 | 2c4-1 | drop | 0.16% | 1.5% | 11% |
| 7 | 2c4-1 | 2c4-3 | keep | 0.06% | 1.2% | 9.5% |
| 8 | 4b5-1 | 4b5-2 | drop | 0 | 0.05% | 0.78% |

Shown: 8 of the 139 DRs up to 11 moves (10 moves: 4 of 9; 11 moves: 4 of 130).

<details>
<summary>Answers for scramble 93</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 10 | 13 | 22 |
| 2 | 7 | 7 | 13 | 23 |
| 3 | 9 | 9 | 13 | 22 |
| 4 | 9 | 8 | 12 | 22 |
| 5 | 9 | 10 | 14 | 24 |
| 6 | 10 | 9 | 13 | 24 |
| 7 | 9 | 8 | 13 | 24 |
| 8 | 10 | 10 | 15 | 25 |

Best on the page: **22 moves**, from DR 1 (DRs 3 and 4 tie it): `U' F' L2 F' R' U F2 B2 R' U L2 B2 D2 B2 U D2 B2 L2 B2 L2 U F'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 94

```
R' U' F U' B2 D F2 D' L2 D L2 F2 U' B' D2 L B2 U' L' U' B' R' D' R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `D (F2 U2 R D F' B2 L F2 L)` | 10 | F/B | 4b5 4e | 2 |
| 2 | `L' F' L2 D F2 U' R (B2 L' F)` | 10 | U/D | 4a2 4e | 2 |
| 3 | `D' L2 U2 L' F D2 L (R F2 D)` | 10 | F/B | 4c3 2e | 2 |
| 4 | `D R2 D2 L F D2 L (R F2 D)` | 10 | F/B | 4c3 4e | 1 |
| 5 | `L' F (L' F' L2 R D2 R' D' F2 R)` | 11 | U/D | 2c3 4e | 2 |
| 6 | `L2 B2 D F D' F (L' D F' D' R)` | 11 | U/D | 2c4 4e | 3 |
| 7 | `L' F (L' F' L' B2 L' U2 D' B2 L)` | 11 | U/D | 2c3 6e | 4 |
| 8 | `F2 D (R D' B' L' F' B' R' F' R)` | 11 | F/B | 2c3 6e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b5-1 | 4b5-1 | look anyway | <0.01% | 0.13% | 1.9% |
| 2 | 4a2-3 | 4a2-2 | look anyway | 1.3% | 6.4% | 24% |
| 3 | 4c3-5 | 4c3-6 | look anyway | 0.12% | 1.2% | 8.1% |
| 4 | 4c3-5 | 4c3-6 | look anyway | 0.08% | 0.96% | 7.0% |
| 5 | 2c3-3 | 2c3-3 | keep | 0.35% | 2.6% | 15% |
| 6 | 2c4-2 | 2c4-1 | keep | 0.91% | 5.7% | 28% |
| 7 | 2c3-3 | 2c3-1 | keep | 1.1% | 7.6% | 34% |
| 8 | 2c3-2 | 2c3-3 | keep | 0.51% | 3.6% | 20% |

Shown: 8 of the 196 DRs up to 11 moves (10 moves: 4 of 13; 11 moves: 4 of 183).

<details>
<summary>Answers for scramble 94</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 14 | 23 |
| 2 | 7 | 10 | 13 | 23 |
| 3 | 9 | 9 | 14 | 23 |
| 4 | 9 | 10 | 13 | 22 |
| 5 | 7 | 8 | 14 | 24 |
| 6 | 8 | 7 | 12 | 22 |
| 7 | 8 | 9 | 13 | 24 |
| 8 | 7 | 9 | 13 | 24 |

Best on the page: **22 moves**, from DR 4 (DR 6 ties it): `D R2 D2 L F D2 L D2 R2 F' D2 B U2 L2 B2 D2 L2 B' R2 D F2 R'`. The list drops 0 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 95

```
R' U' F R2 U2 R2 B2 U' B2 L2 D R2 U' F D R' D L R F2 U' B' D2 U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `L B R F (B U B L D)` | 9 | R/L | 4c3 4e | 2 |
| 2 | `L' R2 F R B (B U B L D)` | 10 | R/L | 4c3 4e | 1 |
| 3 | `(U L B' D' F' R2 B L' R B)` | 10 | R/L | 4a1 4e | 1 |
| 4 | `D2 L B R F (B U B L D)` | 10 | R/L | 4c3 2e | 1 |
| 5 | `(F2 U F' R' B U2 L2 D F2 B2 D)` | 11 | R/L | 2c4 4e | 3 |
| 6 | `L B2 R2 F' R B (B U B L D)` | 11 | R/L | 2c3 2e | 2 |
| 7 | `U2 B2 D (F2 U F2 L2 F' L U2 R)` | 11 | F/B | 2c3 4e | 5 |
| 8 | `(F2 U F' R' B D2 R2 U L2 R2 U)` | 11 | R/L | 2c4 4e | 1 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4c3-6 | 4c3-5 | look anyway | 0.15% | 1.4% | 8.7% |
| 2 | 4c3-6 | 4c3-5 | look anyway | 0.08% | 0.96% | 7.0% |
| 3 | 4a1-4 | 4a1-3 | look anyway | 2.0% | 11% | 37% |
| 4 | 4c3-2 | 4c3-5 | look anyway | 0.18% | 1.6% | 11% |
| 5 | 2c4-7 | 2c4-5 | drop | 0 | 0.09% | 1.7% |
| 6 | 2c3-3 | 2c3-3 | keep | 0.65% | 4.7% | 25% |
| 7 | 2c3-2 | 2c3-2 | keep | 8.1% | 25% | 62% |
| 8 | 2c4-7 | 2c4-5 | drop | 0 | 0.01% | 0.63% |

Shown: 8 of the 119 DRs up to 11 moves (9 moves: 1 of 1; 10 moves: 3 of 9; 11 moves: 4 of 109).

<details>
<summary>Answers for scramble 95</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 8 | 14 | 23 |
| 2 | 8 | 9 | 14 | 24 |
| 3 | 7 | 7 | 14 | 24 |
| 4 | 9 | 9 | 13 | 23 |
| 5 | 10 | 9 | 14 | 25 |
| 6 | 7 | 7 | 13 | 23 |
| 7 | 8 | 8 | 12 | 23 |
| 8 | 10 | 9 | 13 | 24 |

Best on the page: **23 moves**, from DR 1 (DRs 4, 6 and 7 tie it): `L B R F L2 U2 F2 B2 L D2 R' U2 L F2 R B2 D2 L' D' L' B' U' B'`. The list drops 2 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 96

```
R' U' F U2 L2 D B2 F2 R2 D' F2 U F2 L' U2 L2 D' R2 U2 F U2 B' D' F2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `B R2 D (B' D' L F' R' F R)` | 10 | F/B | 2c3 4e | 1 |
| 2 | `(B D' L' D2 R D2 B L2 U F)` | 10 | U/D | 2c5 4e | 4 |
| 3 | `R' D' B2 D2 F' L2 U B (B R)` | 10 | U/D | 4c3 4e | 0 |
| 4 | `L U2 F D2 B' U (D L' F' R)` | 10 | F/B | 4c4 2e | 0 |
| 5 | `R' U B' U2 R2 U B D2 F (B R)` | 11 | U/D | 4b2 2e | 3 |
| 6 | `U F B2 L B (D' F2 D L B2 R)` | 11 | U/D | 4b2 2e | 1 |
| 7 | `R' U B' U2 R2 U F L2 B (B R)` | 11 | U/D | 4b2 2e | 2 |
| 8 | `R' F L2 F2 B D L2 R2 B (B R)` | 11 | U/D | 4b5 4e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-2 | look anyway | 0.38% | 2.8% | 17% |
| 2 | 2c5-1 | 2c5-2 | look anyway | 0.09% | 1.2% | 7.5% |
| 3 | 4c3-7 | 4c3-5 | look anyway | 0.04% | 0.56% | 5.1% |
| 4 | 4c4-3 | 4c4-4 | look anyway | 0 | 0.02% | 0.48% |
| 5 | 4b2-4 | 4b2-1 | keep | 3.5% | 15% | 48% |
| 6 | 4b2-4 | 4b2-1 | keep | 1.4% | 7.6% | 32% |
| 7 | 4b2-4 | 4b2-1 | keep | 2.6% | 11% | 40% |
| 8 | 4b5-1 | 4b5-2 | drop | 0 | 0.07% | 1.0% |

Shown: 8 of the 111 DRs up to 11 moves (10 moves: 4 of 6; 11 moves: 4 of 105).

<details>
<summary>Answers for scramble 96</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 11 | 21 |
| 2 | 10 | 11 | 13 | 23 |
| 3 | 9 | 8 | 12 | 22 |
| 4 | 10 | 11 | 14 | 23 |
| 5 | 7 | 6 | 12 | 22 |
| 6 | 8 | 5 | 14 | 24 |
| 7 | 7 | 6 | 12 | 23 |
| 8 | 9 | 11 | 14 | 25 |

Best on the page: **21 moves**, from DR 1: `B R2 D R2 L2 U2 F' U2 L2 F' D2 U2 R2 F R' F' R F L' D B`. The list drops 1 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 97

```
R' U' F R2 U' R' U' L' D F R' F' U2 F U D' F2 U F2 R2 U' R2 B2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `U' L D2 L2 D (R' F2 B2 R' F)` | 10 | R/L | 4b5 4e | 2 |
| 2 | `D2 F2 U' B U' R' U' D2 R' D` | 10 | R/L | 4b2 4e | 4 |
| 3 | `L' B2 U R D L R F B2 L` | 10 | F/B | 4b5 2e | 2 |
| 4 | `(R2 F2 R F U L F2 D' R' U)` | 10 | R/L | 4b2 2e | 0 |
| 5 | `R' D' B2 R U' L D (R' F2 R' F)` | 11 | R/L | 2c4 4e | 1 |
| 6 | `(R2 D2 L' D2 F' D F2 L U' L R)` | 11 | U/D | 2c4 4e | 5 |
| 7 | `L R2 U2 L' U' L D (R' F2 R' F)` | 11 | R/L | 2c5 4e | 3 |
| 8 | `(R' F2 R' F R2 U2 L R U' R' D)` | 11 | R/L | 2c3 2e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b5-1 | 4b5-2 | look anyway | 0 | 0.07% | 1.0% |
| 2 | 4b2-3 | 4b2-4 | look anyway | 1.6% | 9.8% | 39% |
| 3 | 4b5-2 | 4b5-2 | look anyway | 0 | 0.06% | 0.88% |
| 4 | 4b2-3 | 4b2-4 | look anyway | 0.19% | 2.5% | 17% |
| 5 | 2c4-6 | 2c4-1 | drop | 0.09% | 0.94% | 7.2% |
| 6 | 2c4-6 | 2c4-3 | keep | 1.3% | 5.4% | 22% |
| 7 | 2c5-1 | 2c5-1 | drop | 0.10% | 0.85% | 6.2% |
| 8 | 2c3-1 | 2c3-1 | keep | 5.6% | 22% | 62% |

Shown: 8 of the 547 DRs up to 11 moves (10 moves: 4 of 42; 11 moves: 4 of 505).

<details>
<summary>Answers for scramble 97</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 11 | 10 | 15 | 24 |
| 2 | 7 | 7 | 13 | 23 |
| 3 | 10 | 10 | 14 | 24 |
| 4 | 7 | 8 | 14 | 24 |
| 5 | 10 | 9 | 14 | 24 |
| 6 | 9 | 9 | 14 | 25 |
| 7 | 10 | 9 | 13 | 24 |
| 8 | 5 | 6 | 12 | 22 |

Best on the page: **22 moves**, from DR 8: `U2 B2 R' L2 D2 L B2 D2 B2 U2 R' D R U R' L' U2 R2 F' R F2 R`. The list drops 2 of the 4 DRs of 11 moves or more, and keeps the best one.

</details>

#### Scramble 98

```
R' U' F D2 B2 R2 D' R2 D' L2 D R' B D' F L B2 R2 B2 D R2 D2 U2 R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `F' L D' R' F' L2 D2 B2 D2 L` | 10 | U/D | 2c3 4e | 1 |
| 2 | `F' D (F2 D' R' B2 R U2 R2 F)` | 10 | R/L | 2c3 4e | 3 |
| 3 | `R F B U B' U' R U R' D` | 10 | R/L | 2c3 6e | 2 |
| 4 | `F' L D' F' L F B2 R' F (D)` | 10 | R/L | 4b2 4e | 1 |
| 5 | `F' L D' F' L' B2 U2 B L' B (D)` | 11 | R/L | 4c4 4e | 3 |
| 6 | `L' R U2 L F' B L (D B' R U)` | 11 | F/B | 2c5 2e | 2 |
| 7 | `U2 R2 F U' D' R2 B L' B' R2 F` | 11 | R/L | 4a2 4e | 6 |
| 8 | `L' F2 L2 D (D' R' F2 R' B' R2 F)` | 11 | R/L | 2c4 4e | 0 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c3-3 | 2c3-2 | look anyway | 0.38% | 2.8% | 17% |
| 2 | 2c3-2 | 2c3-2 | look anyway | 1.9% | 9.7% | 36% |
| 3 | 2c3-3 | 2c3-2 | look anyway | 0.33% | 2.5% | 15% |
| 4 | 4b2-2 | 4b2-2 | look anyway | 1.2% | 7.0% | 32% |
| 5 | 4c4-4 | 4c4-6 | drop | 0 | 0 | 0.10% |
| 6 | 2c5-1 | 2c5-3 | drop | 0 | 0.01% | 0.57% |
| 7 | 4a2-3 | 4a2-2 | keep | 4.2% | 15% | 40% |
| 8 | 2c4-4 | 2c4-3 | drop | 0.03% | 0.44% | 3.9% |

Shown: 8 of the 213 DRs up to 11 moves (10 moves: 4 of 31; 11 moves: 4 of 182).

<details>
<summary>Answers for scramble 98</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 9 | 8 | 14 | 24 |
| 2 | 8 | 7 | 14 | 23 |
| 3 | 8 | 7 | 14 | 23 |
| 4 | 8 | 8 | 13 | 23 |
| 5 | 11 | 12 | 15 | 26 |
| 6 | 10 | 11 | 15 | 25 |
| 7 | 9 | 9 | 13 | 24 |
| 8 | 9 | 7 | 14 | 24 |

Best on the page: **23 moves**, from DR 2 (DRs 3 and 4 tie it): `F' D R L2 D2 R B2 L D2 R D2 F2 R F2 R2 F R2 U2 R' B2 R D F2`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 10 moves long, so you'd finish it anyway.

</details>

#### Scramble 99

```
R' U' F D2 B' R2 B' R2 U2 D2 B F L2 U' F R2 U2 L' F R' B D' L F R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `(D L U B' R' B L2 R2 U)` | 9 | F/B | 2c4 4e | 0 |
| 2 | `D' F L' F' R (F' U' L' D)` | 9 | F/B | 2c4 4e | 4 |
| 3 | `(D L U B' R' B U2 L2 R2 U)` | 10 | F/B | 2c4 4e | 2 |
| 4 | `F2 D' L' B2 U (L2 F D' R2 B)` | 10 | R/L | 4b5 2e | 2 |
| 5 | `F2 R D' L' R' U B D2 R2 D2 F` | 11 | U/D | 2c4 4e | 3 |
| 6 | `(D L U B' R' B U' D' F2 B2 D)` | 11 | F/B | 2c4 4e | 1 |
| 7 | `D' F' R2 B2 R' F' L (F' U' L' D)` | 11 | F/B | 2c4 2e | 3 |
| 8 | `(U' F' B' U B L' D R2 U2 L' U)` | 11 | R/L | 2c4 2e | 2 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 2c4-7 | 2c4-4 | look anyway | 0 | 0.02% | 0.95% |
| 2 | 2c4-7 | 2c4-7 | look anyway | 0 | 0.18% | 1.5% |
| 3 | 2c4-7 | 2c4-6 | look anyway | 0.01% | 0.28% | 2.3% |
| 4 | 4b5-1 | 4b5-1 | look anyway | 0.02% | 0.24% | 2.3% |
| 5 | 2c4-6 | 2c4-2 | drop | 0.22% | 1.8% | 11% |
| 6 | 2c4-7 | 2c4-6 | drop | 0 | 0.07% | 1.5% |
| 7 | 2c4-2 | 2c4-3 | keep | 0.58% | 4.5% | 24% |
| 8 | 2c4-3 | 2c4-7 | drop | 0.03% | 0.68% | 5.6% |

Shown: 8 of the 105 DRs up to 11 moves (9 moves: 2 of 2; 10 moves: 2 of 8; 11 moves: 4 of 95).

<details>
<summary>Answers for scramble 99</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 9 | 15 | 23 |
| 2 | 10 | 10 | 14 | 22 |
| 3 | 10 | 8 | 14 | 24 |
| 4 | 9 | 10 | 14 | 23 |
| 5 | 9 | 9 | 13 | 24 |
| 6 | 10 | 8 | 14 | 25 |
| 7 | 9 | 8 | 14 | 24 |
| 8 | 8 | 9 | 14 | 25 |

Best on the page: **22 moves**, from DR 2: `D' F L' F' R' D2 B2 D2 B' U2 L2 F2 L2 F' D2 B U2 F' D L U F`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

#### Scramble 100

```
R' U' F U R2 B2 L2 D2 F2 D F2 U2 F2 B' L' D L F' R' U B D' R2 U R' U' F // scramble
```

Each row is one DR you could have on the page:

| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |
|---:|---|---:|---|---|---:|
| 1 | `B (L' R F U2 R' F2 R U)` | 9 | R/L | 4b5 4e | 1 |
| 2 | `F L2 F' R (R F D2 R2 F)` | 9 | U/D | 4b2 4e | 3 |
| 3 | `D2 F' R D2 R (B2 R' B' D)` | 9 | F/B | 4b2 4e | 1 |
| 4 | `L2 U B (F D' L' D B2 R)` | 9 | U/D | 4b5 2e | 2 |
| 5 | `R (R' U2 B' U L2 D' B' D2 B U)` | 11 | F/B | 4c4 4e | 1 |
| 6 | `(R' B' D B' L R2 D2 L B U2 B)` | 11 | R/L | 2c4 4e | 0 |
| 7 | `R' F D2 F' U L2 R2 F L2 U (R)` | 11 | F/B | 2c3 4e | 2 |
| 8 | `(R' B' D' F B R' F' U2 R2 F2 L)` | 11 | F/B | 4c4 4e | 3 |

The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:

| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |
|---:|---|---|---|---:|---:|---:|
| 1 | 4b5-1 | 4b5-1 | look anyway | <0.01% | 0.08% | 1.1% |
| 2 | 4b2-4 | 4b2-2 | look anyway | 1.6% | 8.9% | 38% |
| 3 | 4b2-2 | 4b2-2 | look anyway | 1.2% | 7.0% | 32% |
| 4 | 4b5-2 | 4b5-2 | look anyway | 0 | 0.06% | 0.88% |
| 5 | 4c4-6 | 4c4-2 | drop | 0 | 0.07% | 0.97% |
| 6 | 2c4-5 | 2c4-4 | drop | 0 | 0.20% | 2.3% |
| 7 | 2c3-2 | 2c3-1 | keep | 1.6% | 8.8% | 36% |
| 8 | 4c4-1 | 4c4-4 | drop | 0.02% | 0.61% | 5.0% |

Shown: 8 of the 2,200 DRs up to 11 moves (9 moves: 4 of 21; 10 moves: 0 of 176; 11 moves: 4 of 2,003).

<details>
<summary>Answers for scramble 100</summary>

Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:

| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |
|---:|---:|---:|---:|---:|
| 1 | 10 | 10 | 14 | 23 |
| 2 | 8 | 8 | 13 | 20 |
| 3 | 8 | 7 | 13 | 22 |
| 4 | 10 | 10 | 13 | 22 |
| 5 | 12 | 10 | 15 | 26 |
| 6 | 9 | 9 | 15 | 26 |
| 7 | 8 | 7 | 13 | 23 |
| 8 | 9 | 11 | 14 | 25 |

Best on the page: **20 moves**, from DR 2: `F L2 F' R' D2 L2 F2 U D2 F2 R2 U' L2 B2 R2 F R2 D2 F' R'`. The list drops 3 of the 4 DRs of 11 moves or more, and the best one is 9 moves long, so you'd finish it anyway.

</details>

### The tally

First the rows printed above, with every DR finished optimally. Each row is one count over the 100 scrambles:

| What | On the page |
|---|---:|
| Scrambles | 100 |
| DRs shown | 800 |
| of 10 moves or less (you'd finish these anyway) | 382 |
| of 11 moves or more | 418 |
| of those, dropped by the list | 268 (64%) |
| DRs to finish per scramble, without the list | 8.0 |
| DRs to finish per scramble, with the list | 5.3 |
| Best solution on the page, average, finishing every DR shown | 21.29 |
| Best solution on the page, average, finishing what the list leaves | 21.32 |
| Scrambles where the list drops the page's best solution | 2 of 100 |
| Moves lost on those, average | 1.50 |

The page shows a handful of DRs per scramble. The same count over every DR up to 12 moves, for 500 scrambles (the 100 above are the first of them), says what there is to find and what the list does to it. Nobody finishes hundreds of DRs in an hour, so read the second column as the size of the haystack. "The best there is" is the shortest solution over all of a scramble's DRs up to 12 moves, each finished optimally; the list is used on DRs of 11 moves and up only.

9 of the 500 scrambles have no DR of 10 moves or less of this kind. This table leaves them out, so every row is about the same 491 scrambles. Each row is a set of DRs you finish, with how many that is and the best solution it gives.

| You finish | DRs to finish per scramble | Best solution, average moves | Scrambles where that is the best there is |
|---|---:|---:|---:|
| every DR of 10 moves or less | 71 | 20.62 | 35% |
| those, and the 11-movers the list keeps | 353 | 20.05 | 62% |
| those, and every 11-mover | 733 | 20.04 | 63% |
| every DR of 10 moves or less, and the 11- and 12-movers the list keeps | 3,137 | 19.57 | 99.4% |
| every DR up to 12 moves | 7,244 | 19.56 | 100% |

So the list on the 11-movers takes the DRs to finish from 733 to 353 per scramble and the average result from 20.04 to 20.05. On the 12-movers as well it takes 7,244 to 3,137, and 19.56 to 19.57.

And by the length of the DR, over all 500 scrambles. "Reaches the best" means its solution is as short as the best one over all of that scramble's DRs up to 12 moves. The list is meant for 11 moves and up; the first two rows show what it would do if you used it on shorter DRs too. Each row is a DR length:

| DR length | DRs per scramble | Scrambles where one of them reaches the best | The list drops | Kept DRs that reach the best | Dropped DRs that reach the best |
|---|---:|---:|---:|---:|---:|
| 9 or less | 6.1 | 12% | 57% | 4.8% | 0.68% |
| 10 | 63.6 | 26% | 57% | 1.1% | 0.08% |
| 11 | 651.0 | 44% | 57% | 0.23% | <0.01% |
| 12 | 6,400.7 | 74% | 57% | 0.06% | <0.01% |

In counts: of the 342 11-movers that reach their scramble's best solution the list keeps 325, and of the 794 12-movers it keeps 778.

Over all DR states the list drops 57% and loses 7.8% of the finishes in 11 or less (write-up, guide). Every finish here is the optimal one: the answer key, not what you find by hand.

<!-- many-examples:end -->
