# Corners in 3D: worked examples

Examples for [the write-up](./). Corners only, DBL held, R U F turns, and *solved* means HTR.

Types are seven characters in the order UFR UFL UBL UBR DFR DFL DBR: `.` good (3 stickers oriented), `+` `-` twisted clockwise / counter-clockwise (0 oriented), `r` `u` `f` out (only the R/L, U/D or F/B sticker oriented). A scramble here is a shortest sequence that makes the state from solved, so you can put it on a cube in a few turns.

## 1. Twelve states, read step by step

**1. One face.**

```
R                         // types r . . r r . r
```

Four out corners, all with the R/L sticker oriented, all on R. The count table row (0 twisted, out 4) says at least 1. A quarter turn of R turns `r` corners on R into good ones (rule of 4.2), so R or R' makes everything good. Check the end: after R' the D-colour corners are the whole D face, a 4a picture, and one quarter turn from an odd state leaves even parity. HTR. 1 move.

**2. Two faces.**

```
R U                       // types + - u u r . r
```

Two twisted corners where R and U overlap (UFR, UFL after the U), `u` corners on the rest of U, `r` corners on the rest of R. A U turn fixes the `u` ones and turns the twisted ones into `r`. Then R finishes. U' R: 2 moves, and the types floor is 2, so that's optimal.

**3. Bars.**

```
U R2 U'                   // types . . u u u . u
```

Four `u` corners in a 4b shape: no half turns bring them onto one face. That's 4b2 on a DR. U R2 U, 3 moves and 2 quarter turns.

**4. A face that isn't 1 qt.**

```
R' U2 R2 F2 R'            // types . . r r r r .
```

Four `r` corners in a 4a shape again, so it looks like example 1 after a setup: the types floor is 4 moves and 1 quarter turn. But parity is even, so the number of quarter turns has to be even. One quarter turn can't be it. With parity the floor is 5, and that's the answer: R U2 R2 F2 R, 5 moves, 2 quarter turns. This is 4a2. The 1-qt way, U2 R2 F2 R, makes every corner good and lands in a fake HTR.

**5. A fake HTR.**

```
U R2 U F2 U2 R2 U F2 U    // types . . . . . . .
```

Every corner good. The D-colour corners: with DBL they sit 2 and 2 by tetrad, but the two pairs are on neighbouring faces. That's 4b, not 4a, so it isn't HTR, whatever the parity (here even). It's 9 moves from HTR like every fake HTR, 4 quarter turns, 6 moves with NISS.

**6. Two twisted corners.**

```
U F R F R' U' R'          // types . . . . + - .
```

It looks like almost nothing. The count table row (2 twisted, out 0) says at least 7 moves and 5 quarter turns, and this state meets it: R U R F' R' F' U. A twisted corner needs two quarter turns on different axes, and there's no way to give two corners that without dragging others along.

**7. Four twisted corners.**

```
U F2 U2 F'                // types + - . . - + .
```

Twice as many twisted corners and it's 4 moves: F U2 F2 U. All four sit on one face, a half turn setup puts the same four on another face, and two quarter turns on different axes do the job. The row (4 twisted, out 0) has floor 4.

**8. A typical state.**

```
U R' F U F2 R' F' R2 F     // types r r - u f f f
```

1 twisted, out 2 + 1 + 3 by axis. Count table: at least 5. The types floor is 6: `F' R2 U' F2 U F` makes every corner good. But it ends in a fake HTR. Parity is odd, and with parity the floor is 7. The truth is 8: `U2 R U' F R' F' R F`. Only 2 of the nine turns get closer (U2, F2), and nothing you can read off the types says which.

**9. One where the types are enough.**

```
R2 U F2 R' U F     // types . - u . u - -
```

Types floor 5, and it's 5 from HTR: `F' U' R F2 U`. Closer turns: F'.

**10. NISS beats the one-sided floor.**

```
F R2 F2 U2                // types . f f . f . f
```

Four `f` corners, in a 4a shape but not on F: on one side you need the three half turns back, so the types floor is 4 and the state is 4 from HTR. On the inverse the same four corners are on F, and (F) is HTR: 1 with NISS. The quarter-turn count is 1 either way.

**11. Eight quarter turns.**

```
R' U' F U' F U F2 U R'     // types . . + . . + +
```

One of the 384 states that need 8 quarter turns. It's 9 moves from HTR, and the subset number of its placement is only 0: the twist costs 8.

**12. A 5-qt DR case, both ways.**

```
R2 U' R2 U F2 U' F2 U R2 U' R2     // a 2c5, types . u . . . . u
R2 U R2 U F2 U' R2 U F2 U     // 10 moves staying in DR
R F R' F2 R U' R U     // 8 moves with off-axis turns
```

The fewest quarter turns is 5 either way, but the 8-mover isn't a 5-qt solution: it spends 7 quarter turns and 1 half turn, against 5 and 5 for the DR one. Off-axis you trade half turns for quarter turns.

## 2. Every pattern within 3 moves of all good

If the types of your state, up to the symmetries that keep DBL, aren't in this table and aren't all good, the types floor is at least 4. There are 117 such patterns; one row stands for the ones that are alike by turning the cube about the DBL-UFR diagonal or mirroring through it. *Quarter turns in them* is how many of the moves are quarter turns.

| Moves to all good | Quarter turns in them | Types | What you count | Patterns alike by symmetry | A scramble | A way to all good |
|---:|---:|---|---|---:|---|---|
| 1 | 1 | `u u u u . . .` | 4 out (4a) | 3 | `U'` | `U` |
| 2 | 1 | `. r r . r . r` | 4 out (4a) | 6 | `R U2` | `U2 R` |
| 2 | 2 | `- + . r f f r` | 2 + 2 out, 2 twisted (4b) | 6 | `R' F'` | `F R` |
| 2 | 2 | `u u + - r . r` | 2 + 2 out, 2 twisted (4b) | 6 | `R' U'` | `U R` |
| 3 | 1 | `f . . f f . f` | 4 out (4a) | 6 | `F' R2 F2` | `F2 R2 F` |
| 3 | 2 | `. . . f f f f` | 4 out (4b) | 6 | `F' R2 F` | `F' R2 F` |
| 3 | 2 | `r r r . r . .` | 4 out (4b) | 6 | `R U2 R'` | `R U2 R` |
| 3 | 2 | `+ . f r r f +` | 2 + 2 out, 2 twisted (4a) | 6 | `F U2 R` | `R U2 F` |
| 3 | 2 | `. r - + f f r` | 2 + 2 out, 2 twisted (4b) | 6 | `R F' U2` | `U2 F R` |
| 3 | 2 | `. r f f + - r` | 2 + 2 out, 2 twisted (4b) | 6 | `R F U2` | `U2 F' R` |
| 3 | 2 | `u + r u r . -` | 2 + 2 out, 2 twisted (4b) | 6 | `U R U2` | `U2 R' U` |
| 3 | 2 | `u u + f - f .` | 2 + 2 out, 2 twisted (4b) | 6 | `U F U2` | `U2 F' U` |
| 3 | 3 | `+ u u u r f u` | 4 + 1 + 1 out, 1 twisted | 6 | `F U' R` | `R' U F` |
| 3 | 3 | `r r - u r f r` | 4 + 1 + 1 out, 1 twisted | 6 | `F R U` | `U' R' F` |
| 3 | 3 | `+ . u + r . .` | 1 + 1 out, 2 twisted | 6 | `F' U' F` | `F' U F` |
| 3 | 3 | `. . . - u - r` | 1 + 1 out, 2 twisted | 6 | `F' R F` | `F' R' F` |
| 3 | 3 | `. . f - r . -` | 1 + 1 out, 2 twisted | 6 | `U R U'` | `U R' U` |
| 3 | 3 | `r . . + f + .` | 1 + 1 out, 2 twisted | 6 | `U' F' U'` | `U F U` |
| 3 | 3 | `- + - r + f +` | 1 + 1 out, 5 twisted | 6 | `F U R'` | `R U' F` |
| 3 | 3 | `- - + - f + r` | 1 + 1 out, 5 twisted | 6 | `R' U' F'` | `F U R` |

By floor, the number of type patterns: 1 at 0, 3 at 1, 18 at 2, 96 at 3, 561 at 4, 2,630 at 5, 9,062 at 6, 11,752 at 7, 1,376 at 8, 16 at 9.

## 3. 200 random states

Uniformly random over the 3,674,160 states. For each one: the scramble, what you can read, and the floors. The answer is folded: moves and quarter turns to HTR, which turns get closer, a shortest way, and where the first shortest way to all good ends.

In this sample the types floor is the true distance for 74 of the 200 and types + parity for 119. The first shortest way to all good ends in real HTR for 47. Over all states it's exactly 1 in 6, so about 33 was to be expected: this draw is on the lucky side (that many or more comes up 0.8% of the time). The 200 are a plain uniform draw with a fixed seed, and every entry is checked.

**1.** `U R' F U F2 R' F' R2 F`

Types `r r - u f f f`. 1 twisted, out 2 on R/L, 1 on U/D, 3 on F/B. Out corners 6c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: U2, F2. One of 4 shortest ways: `U2 R U' F R' F' R F`. The first shortest way to all good, `F' R2 U' F2 U F`, ends in a fake HTR, 9 from HTR.

</details>

**2.** `U2 F R2 F U2 F' R F`

Types `. f . r + u r`. 1 twisted, out 2 on R/L, 1 on U/D, 1 on F/B. Out corners 4a, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: F'. One of 2 shortest ways: `F' R' F U2 F' R2 F`. The first shortest way to all good, `R F2 R' F' R F`, ends in a fake HTR, 9 from HTR.

</details>

**3.** `R F' R' F' R' U2 R' F U'`

Types `f - u u u - +`. 3 twisted, out 0 on R/L, 3 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: F2. One of 2 shortest ways: `F2 R' F U R F2 U' R`. The first shortest way to all good, `R2 U R U F' U R`, ends in a fake HTR, 9 from HTR.

</details>

**4.** `F' R2 F' U' F2 R U2 R2`

Types `u r - - . - -`. 4 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 4 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (6 moves with NISS). Closer turns: R2, R', U', F, F2. One of 22 shortest ways: `R2 U2 R' F2 U F R2 F`. The first shortest way to all good, `R U' R' F' U R' U`, ends in a fake HTR, 9 from HTR.

</details>

**5.** `F' U' F' U' R F' U R' F2`

Types `f u f u f u -`. 1 twisted, out 0 on R/L, 3 on U/D, 3 on F/B. Out corners 6c, D-colour corners 4c, parity even.

Floors: count table 4 moves (3 qt), types 7, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (7 moves with NISS). Closer turns: U, U', F. One of 6 shortest ways: `U F2 U2 R2 U' F' U2 F`. The first shortest way to all good, `R2 U2 F2 U F' R2 F`, ends in a fake HTR, 9 from HTR.

</details>

**6.** `R U R' F2 R' U R' F2 R'`

Types `f f - r u r f`. 1 twisted, out 2 on R/L, 1 on U/D, 3 on F/B. Out corners 6c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: F. One of 4 shortest ways: `F U2 R' U F2 U F2 R`. The first shortest way to all good, `R U F U' F2 U' F`, ends in a fake HTR, 9 from HTR.

</details>

**7.** `U R2 F R' F' R F' R U2`

Types `u r + r + r .`. 2 twisted, out 3 on R/L, 1 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: U, U2. One of 6 shortest ways: `U F2 U R' U2 F2 R' F`. The first shortest way to all good, `U' R U2 F' R U`, ends in a fake HTR, 9 from HTR.

</details>

**8.** `F U' F2 R' F R`

Types `f r u r u u .`. 0 twisted, out 2 on R/L, 3 on U/D, 1 on F/B. Out corners 6c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

6 moves, 5 quarter turns (5 moves with NISS). Closer turns: R'. One of 2 shortest ways: `R' F' R F2 U F`. The first shortest way to all good, `R' F' R F2 U F`, ends in HTR.

</details>

**9.** `U' F2 U' F' U' R U' F2 R`

Types `- r u - r . u`. 2 twisted, out 2 on R/L, 2 on U/D, 0 on F/B. Out corners 4a, D-colour corners 4b, parity odd.

Floors: count table 2 moves (2 qt), types 5, types + parity 8. Subset number of the placement: 1.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R', U', F2. One of 12 shortest ways: `R' F2 U2 R' F' R' F2 R`. The first shortest way to all good, `F R' F2 U F`, ends in a fake HTR, 9 from HTR.

</details>

**10.** `U F' R' F' U2 R F' R`

Types `f r u r r - u`. 1 twisted, out 3 on R/L, 2 on U/D, 1 on F/B. Out corners 6c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R', F. One of 6 shortest ways: `R' F R' F R F U`. The first shortest way to all good, `R2 F' R2 F' R F2 U`, ends in a fake HTR, 9 from HTR.

</details>

**11.** `F' U2 F2 R2 U' F U R'`

Types `r - - - r . .`. 3 twisted, out 2 on R/L, 0 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 5.

<details><summary>Answer</summary>

6 moves, 5 quarter turns (5 moves with NISS). Closer turns: F. One of 2 shortest ways: `F U' F' R U2 R`. The first shortest way to all good, `F U' F' R U2 R`, ends in HTR.

</details>

**12.** `U' F' U2 F2 U' F2 R' U R2`

Types `u u . + - - +`. 4 twisted, out 0 on R/L, 2 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R. One of 8 shortest ways: `R U R2 F R2 F2 R' F`. The first shortest way to all good, `R F2 U2 R2 U' F`, ends in a fake HTR, 9 from HTR.

</details>

**13.** `R2 U' F' U' R' F2 R2`

Types `+ . . . r u +`. 2 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 3 moves (3 qt), types 5, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (4 moves with NISS). Closer turns: R2. One of 2 shortest ways: `R2 F2 R U F U`. The first shortest way to all good, `R U F U' R`, ends in a fake HTR, 9 from HTR.

</details>

**14.** `R F R F' R U' F2 U`

Types `. u + - u r f`. 2 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 4 moves (3 qt), types 7, types + parity 8. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: U', F, F'. One of 8 shortest ways: `U' F2 U R' F R' F' R`. The first shortest way to all good, `U' R' U2 R' F U' F`, ends in a fake HTR, 9 from HTR.

</details>

**15.** `R U F2 U F' R U2 F' R`

Types `- u - - . r +`. 4 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 4 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: U'. One of 2 shortest ways: `U' R' U' R F U' F`. The first shortest way to all good, `U' R' U' R F U' F`, ends in HTR.

</details>

**16.** `R U' F' R U2 F2 U' R'`

Types `. r r - + + -`. 4 twisted, out 2 on R/L, 0 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 5 moves (3 qt), types 8, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (6 moves with NISS). Closer turns: R, U'. One of 8 shortest ways: `R U F2 U2 R' F U R`. The first shortest way to all good, `R U F2 U2 R' F U R`, ends in HTR.

</details>

**17.** `F2 U' R F2 U F2 U F' U' R'`

Types `. u + u . u r`. 1 twisted, out 1 on R/L, 3 on U/D, 0 on F/B. Out corners 4a, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

9 moves, 5 quarter turns (8 moves with NISS). Closer turns: R, R2, R', U, U2, U', F, F2, F'. One of 44 shortest ways: `R U F U' F2 U' F2 R' U`. The first shortest way to all good, `R' U2 R' F' U' F' U`, ends in a fake HTR, 9 from HTR.

</details>

**18.** `F' U R2 F2 R' F U2 R' U'`

Types `f r f r u u -`. 1 twisted, out 2 on R/L, 2 on U/D, 2 on F/B. Out corners 6c, D-colour corners 4a, parity even.

Floors: count table 6 moves (5 qt), types 8, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: U'. One of 2 shortest ways: `U' F2 R U2 R' F R' U`. The first shortest way to all good, `R2 F' R F2 U' R2 F R`, ends in a fake HTR, 9 from HTR.

</details>

**19.** `R U' F R U R' F U'`

Types `+ f r - f + r`. 3 twisted, out 2 on R/L, 0 on U/D, 2 on F/B. Out corners 4a, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 8, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: R', U. One of 8 shortest ways: `R' U' R2 F' R2 F U' R`. The first shortest way to all good, `R U2 R' U' F U R' F`, ends in a fake HTR, 9 from HTR.

</details>

**20.** `F' U' F2 U' R' F R' U' R'`

Types `- + . - f + f`. 4 twisted, out 0 on R/L, 0 on U/D, 2 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 5 moves (3 qt), types 6, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

9 moves, 4 quarter turns (8 moves with NISS). Closer turns: R, R2, U', F. One of 24 shortest ways: `R U R F' R U F2 U F`. The first shortest way to all good, `U2 F U F2 R2 F`, ends in a fake HTR, 9 from HTR.

</details>

**21.** `U R2 F2 R' F2 U' R F2 R'`

Types `+ u f u . - r`. 2 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity odd.

Floors: count table 4 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R. One of 2 shortest ways: `R F2 R' U F2 R' U`. The first shortest way to all good, `R F2 R' U F2 R' U`, ends in HTR.

</details>

**22.** `R2 U F2 R' U F' R U'`

Types `. . . + u . r`. 1 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 5 moves (5 qt), types 6, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (7 moves with NISS). Closer turns: R', U. One of 10 shortest ways: `R' F2 U' R' F U' R`. The first shortest way to all good, `F2 U' F U' F R`, ends in a fake HTR, 9 from HTR.

</details>

**23.** `F R U' R U F' U R2`

Types `. + - . u + r`. 3 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 4 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R2, U2. One of 4 shortest ways: `R2 U' F U' R' U R' F`. The first shortest way to all good, `U' F' R F R' F' U`, ends in a fake HTR, 9 from HTR.

</details>

**24.** `F R' U2 F R2 F R' U R'`

Types `f r r u r . f`. 0 twisted, out 3 on R/L, 1 on U/D, 2 on F/B. Out corners 6c, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 5.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R'. One of 2 shortest ways: `R' U' R F2 U2 R F`. The first shortest way to all good, `F R F' U2 R' U`, ends in a fake HTR, 9 from HTR.

</details>

**25.** `U' R U' R2 F R F2 U2 R'`

Types `. - u r - . +`. 3 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4a, parity even.

Floors: count table 4 moves (3 qt), types 5, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (6 moves with NISS). Closer turns: U, U', F, F'. One of 8 shortest ways: `U F2 U2 R2 U F2 U' R`. The first shortest way to all good, `R2 U R U2 R`, ends in a fake HTR, 9 from HTR.

</details>

**26.** `R2 F' R' U2 F U R2 U R2`

Types `- r - - . u -`. 4 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 4 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: F. One of 2 shortest ways: `F U R2 F' R' U2 R`. The first shortest way to all good, `F U R2 F' R' U2 R`, ends in HTR.

</details>

**27.** `F2 R F' R2 U2 F' R2 F U`

Types `u u - - r r -`. 3 twisted, out 2 on R/L, 2 on U/D, 0 on F/B. Out corners 4a, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 1.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, R', U, U', F'. One of 20 shortest ways: `R F' R' U F' R2 U' F`. The first shortest way to all good, `R2 F R U' F2 U' F`, ends in a fake HTR, 9 from HTR.

</details>

**28.** `U F2 R2 U' R' F2 R' F2 U R'`

Types `- f f . r . u`. 1 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4a, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: U, U2. One of 6 shortest ways: `U F R2 U' F' R U2 R`. The first shortest way to all good, `U R U F2 R2 U' F`, ends in a fake HTR, 9 from HTR.

</details>

**29.** `R2 U F2 R' U F`

Types `. - u . u - -`. 3 twisted, out 0 on R/L, 2 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 5, types + parity 5. Subset number of the placement: 4.

<details><summary>Answer</summary>

5 moves, 4 quarter turns (5 moves with NISS). Closer turns: F'. One of 4 shortest ways: `F' U' R F2 U`. The first shortest way to all good, `F' U' R F2 U`, ends in HTR.

</details>

**30.** `F U' F2 U F' U' R`

Types `. f u + r r .`. 1 twisted, out 2 on R/L, 1 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (6 moves with NISS). Closer turns: R', F. One of 6 shortest ways: `R' U F U' F2 U F`. The first shortest way to all good, `R F2 R' U2 F R F`, ends in a fake HTR, 9 from HTR.

</details>

**31.** `F U' R2 F R2 F U2 F2 U' R'`

Types `- + f f f u +`. 3 twisted, out 0 on R/L, 1 on U/D, 3 on F/B. Out corners 4a, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: R2, R'. One of 4 shortest ways: `R2 U' F R' U2 F R' F`. The first shortest way to all good, `U2 F2 U' R U' F R`, ends in a fake HTR, 9 from HTR.

</details>

**32.** `F R F2 U F' R2 F' R F'`

Types `- - + f + r -`. 5 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 3 moves (3 qt), types 7, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

9 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, R2, R', U2, U', F, F2, F'. One of 48 shortest ways: `R F U2 F R2 U' F' R F`. The first shortest way to all good, `R F U' R F2 R' F`, ends in a fake HTR, 9 from HTR.

</details>

**33.** `R' F2 U R F2 U' F U F2 R2`

Types `- - f f f r +`. 3 twisted, out 1 on R/L, 0 on U/D, 3 on F/B. Out corners 4a, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: R, F. One of 6 shortest ways: `R U R F R2 U2 R' U`. The first shortest way to all good, `R F2 R U' F R' U`, ends in a fake HTR, 9 from HTR.

</details>

**34.** `R2 U F2 U' R F2 R' F2 R`

Types `. + . u . u -`. 2 twisted, out 0 on R/L, 2 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 8, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: R'. One of 2 shortest ways: `R' F2 R F2 R' U F2 U`. The first shortest way to all good, `R U2 R' U2 R U' F2 U`, ends in a fake HTR, 9 from HTR.

</details>

**35.** `R' F U2 R' F2 R' F' U F2`

Types `- u f + r f .`. 2 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 4 moves (3 qt), types 6, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: F. One of 2 shortest ways: `F U' R F R2 U2 F' R`. The first shortest way to all good, `R' U' F2 R U R`, ends in a fake HTR, 9 from HTR.

</details>

**36.** `F2 R2 F' R U' F2 R U2 R`

Types `r - - . r - .`. 3 twisted, out 2 on R/L, 0 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R'. One of 2 shortest ways: `R' U2 R' F2 U R' F`. The first shortest way to all good, `F2 R F2 U' R' F`, ends in a fake HTR, 9 from HTR.

</details>

**37.** `F U2 F' U2 R F2 R' U R2`

Types `+ + + - u r -`. 5 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 3 moves (3 qt), types 6, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, R', U2, U', F. One of 16 shortest ways: `R U F U R' U2 F U`. The first shortest way to all good, `U' F2 R2 U R' F`, ends in a fake HTR, 9 from HTR.

</details>

**38.** `U2 R U2 F' R F U' F2 R`

Types `f u . - . + -`. 3 twisted, out 0 on R/L, 1 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 4 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (7 moves with NISS). Closer turns: U2. One of 2 shortest ways: `U2 F R2 U' R2 U' F`. The first shortest way to all good, `U2 F R2 U' R2 U' F`, ends in HTR.

</details>

**39.** `U R F2 U' F U' R2 F' R'`

Types `- r . - . r -`. 3 twisted, out 2 on R/L, 0 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R. One of 2 shortest ways: `R F2 R' U2 F U' F`. The first shortest way to all good, `R F2 R' U2 F U' F`, ends in HTR.

</details>

**40.** `F' U F' R F' R U' R2 U'`

Types `- u . u . u f`. 1 twisted, out 0 on R/L, 3 on U/D, 1 on F/B. Out corners 4a, D-colour corners 4d, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: R. One of 2 shortest ways: `R U F2 U' R2 F R' F`. The first shortest way to all good, `R F U F2 U2 R' U`, ends in a fake HTR, 9 from HTR.

</details>

**41.** `F U' F U' R F' U' R2`

Types `. + f f f f -`. 2 twisted, out 0 on R/L, 0 on U/D, 4 on F/B. Out corners 4a, D-colour corners 4b, parity odd.

Floors: count table 4 moves (4 qt), types 6, types + parity 8. Subset number of the placement: 1.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R2, U, U', F, F'. One of 16 shortest ways: `R2 U F R' U F' U F`. The first shortest way to all good, `R F2 R U2 F U`, ends in a fake HTR, 9 from HTR.

</details>

**42.** `F U' F U2 R2 U' F U2 F'`

Types `f u - f . + u`. 2 twisted, out 0 on R/L, 2 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4c, parity even.

Floors: count table 2 moves (2 qt), types 7, types + parity 8. Subset number of the placement: 2.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: R', F'. One of 6 shortest ways: `R' U R F2 R F' R2 F`. The first shortest way to all good, `U R2 F R2 F R' F`, ends in a fake HTR, 9 from HTR.

</details>

**43.** `F' R' U R F2 R2 U R' U' R2`

Types `+ f r . r f -`. 2 twisted, out 2 on R/L, 0 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 2 moves (2 qt), types 5, types + parity 5. Subset number of the placement: 3.

<details><summary>Answer</summary>

9 moves, 5 quarter turns (8 moves with NISS). Closer turns: R, R', F2, F'. One of 14 shortest ways: `R U2 R2 F' U F U' F R`. The first shortest way to all good, `F' U' R' U' R`, ends in a fake HTR, 9 from HTR.

</details>

**44.** `U2 F U2 R U' F2 U' R2`

Types `+ r + + + u +`. 5 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 3 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (7 moves with NISS). Closer turns: R2. One of 4 shortest ways: `R2 U F2 U R U2 F`. The first shortest way to all good, `U F2 U R U2 F`, ends in a fake HTR, 9 from HTR.

</details>

**45.** `R U' R2 U' R2 U' F' U2 R'`

Types `- . u r . - +`. 3 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4a, parity even.

Floors: count table 4 moves (3 qt), types 7, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (7 moves with NISS). Closer turns: R2, R', F. One of 14 shortest ways: `R2 F U R F2 U F' R`. The first shortest way to all good, `R U R2 U2 R' F' R`, ends in a fake HTR, 9 from HTR.

</details>

**46.** `U2 R2 F' U' F' R F U' F'`

Types `r f + f r f u`. 1 twisted, out 2 on R/L, 1 on U/D, 3 on F/B. Out corners 6c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: F. One of 2 shortest ways: `F U F' R' F U F`. The first shortest way to all good, `U F' R2 U2 R F2 U`, ends in a fake HTR, 9 from HTR.

</details>

**47.** `R' F R2 F2 U' R' U F2`

Types `r f . + r r +`. 2 twisted, out 3 on R/L, 0 on U/D, 1 on F/B. Out corners 4a, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (6 moves with NISS). Closer turns: R2, F2. One of 6 shortest ways: `R2 F' R' U R2 U' R2 U`. The first shortest way to all good, `R F2 R U' R U`, ends in a fake HTR, 9 from HTR.

</details>

**48.** `F' R F' U F2 R' U R' U`

Types `- f - . + r .`. 3 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 4 moves (3 qt), types 6, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (7 moves with NISS). Closer turns: F, F2. One of 8 shortest ways: `F R' U F U2 F2 U F`. The first shortest way to all good, `R2 U2 F R2 F R`, ends in a fake HTR, 9 from HTR.

</details>

**49.** `U2 F' R' U2 R' U' F2 U R`

Types `f + + f - + +`. 5 twisted, out 0 on R/L, 0 on U/D, 2 on F/B. Out corners 2c, D-colour corners 4a, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: R', F. One of 6 shortest ways: `R' U' F2 U R U2 R F`. The first shortest way to all good, `U' F2 U' R' F U2 F`, ends in a fake HTR, 9 from HTR.

</details>

**50.** `R U2 R' F' U2 R2 F' R'`

Types `+ f - . . f .`. 2 twisted, out 0 on R/L, 0 on U/D, 2 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (6 moves with NISS). Closer turns: R, F'. One of 6 shortest ways: `R U F' U F U2 R' F`. The first shortest way to all good, `R F U2 F R F2 R`, ends in a fake HTR, 9 from HTR.

</details>

**51.** `U' F' U2 F2 U' R' F2 R`

Types `u u r + u . .`. 1 twisted, out 1 on R/L, 3 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (6 moves with NISS). Closer turns: R'. One of 4 shortest ways: `R' F2 R U F2 U2 F U`. The first shortest way to all good, `R U2 R' U F2 U2 F`, ends in a fake HTR, 9 from HTR.

</details>

**52.** `R2 U R2 U' F U2 R' F2 R`

Types `- + f f f + u`. 3 twisted, out 0 on R/L, 1 on U/D, 3 on F/B. Out corners 4b, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: R'. One of 2 shortest ways: `R' F2 R U2 F' U R2 U`. The first shortest way to all good, `F R2 F R F2 U2 F`, ends in a fake HTR, 9 from HTR.

</details>

**53.** `R2 F2 U2 F' R2 F R' U R2`

Types `+ r u r u f r`. 1 twisted, out 3 on R/L, 2 on U/D, 1 on F/B. Out corners 6c, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: R2. One of 2 shortest ways: `R2 U' R F' R2 F`. The first shortest way to all good, `R2 U' R F' R2 F`, ends in HTR.

</details>

**54.** `F' R U2 R' F U' F R2 F2`

Types `+ . u - r . -`. 3 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 4 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: R2, R', U. One of 6 shortest ways: `R2 U' R' F' R2 U F R`. The first shortest way to all good, `U F R F' U' R`, ends in a fake HTR, 9 from HTR.

</details>

**55.** `R2 U2 R F R2 F R2 F R' U2`

Types `. r u r u r r`. 0 twisted, out 4 on R/L, 2 on U/D, 0 on F/B. Out corners 6c, D-colour corners 4a, parity odd.

Floors: count table 6 moves (4 qt), types 6, types + parity 8. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: U2. One of 4 shortest ways: `U2 R F' R2 F' R2 F' R`. The first shortest way to all good, `R U F' R U R`, ends in a fake HTR, 9 from HTR.

</details>

**56.** `U' R' U' R F' R U' F2`

Types `f f r r r r .`. 0 twisted, out 4 on R/L, 0 on U/D, 2 on F/B. Out corners 6c, D-colour corners 4c, parity odd.

Floors: count table 6 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: F2. One of 4 shortest ways: `F2 U R U' R U' F' U`. The first shortest way to all good, `F2 R F' U R' F' R`, ends in a fake HTR, 9 from HTR.

</details>

**57.** `F2 U R U R F R2 F`

Types `. u . f + u u`. 1 twisted, out 0 on R/L, 3 on U/D, 1 on F/B. Out corners 4a, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (7 moves with NISS). Closer turns: F'. One of 6 shortest ways: `F' R2 F' R' U' R' U`. The first shortest way to all good, `R' F' U F' U2 R2 U`, ends in a fake HTR, 9 from HTR.

</details>

**58.** `U' F' U F2 R U' R' U2 R`

Types `- . r u r . f`. 1 twisted, out 2 on R/L, 1 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: U2. One of 4 shortest ways: `U2 R' F U R2 U2 F R`. The first shortest way to all good, `R U2 R2 F R' F`, ends in a fake HTR, 9 from HTR.

</details>

**59.** `R2 U' F2 U F2 U R2 F' R2`

Types `u f . f u f f`. 0 twisted, out 0 on R/L, 2 on U/D, 4 on F/B. Out corners 6c, D-colour corners 4c, parity even.

Floors: count table 6 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (7 moves with NISS). Closer turns: R2. One of 4 shortest ways: `R2 F U F2 U R2 U`. The first shortest way to all good, `R2 F U F2 U R2 U`, ends in HTR.

</details>

**60.** `F' U F2 U' R U R' F`

Types `f - - + r - .`. 4 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 4 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: F, F'. One of 4 shortest ways: `F U' F' U2 R U R' U`. The first shortest way to all good, `F U2 R' F2 R U`, ends in a fake HTR, 9 from HTR.

</details>

**61.** `U2 R F R2 U' R2 U' R F'`

Types `+ . + r r r u`. 2 twisted, out 3 on R/L, 1 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: F. One of 2 shortest ways: `F R' U R2 U R2 F' R`. The first shortest way to all good, `U F2 R' F U F`, ends in a fake HTR, 9 from HTR.

</details>

**62.** `F U2 F U2 R2 F U R2 F'`

Types `r . - f . + -`. 3 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 4 moves (3 qt), types 7, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: F, F'. One of 8 shortest ways: `F R U' R F' R' U2 R`. The first shortest way to all good, `F2 R' U2 R U F2 R`, ends in a fake HTR, 9 from HTR.

</details>

**63.** `R2 F2 R F' U2 R' F2`

Types `f r - . r u +`. 2 twisted, out 2 on R/L, 1 on U/D, 1 on F/B. Out corners 4a, D-colour corners 4c, parity odd.

Floors: count table 4 moves (3 qt), types 5, types + parity 5. Subset number of the placement: 3.

<details><summary>Answer</summary>

5 moves, 3 quarter turns (5 moves with NISS). Closer turns: F2. One of 2 shortest ways: `F2 R U2 F R`. The first shortest way to all good, `F2 R U2 F R`, ends in HTR.

</details>

**64.** `F U' R U R U' F2 U' F2 U`

Types `f r . u r f r`. 0 twisted, out 3 on R/L, 1 on U/D, 2 on F/B. Out corners 6c, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

9 moves, 6 quarter turns (8 moves with NISS). Closer turns: R, R2, R', U, U', F, F'. One of 24 shortest ways: `R U2 R F U2 R2 F U F`. The first shortest way to all good, `F R' U F' U' R`, ends in a fake HTR, 9 from HTR.

</details>

**65.** `R U' F2 R' U R' F2 R U2`

Types `+ + u + r . -`. 4 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4a, parity even.

Floors: count table 4 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: F'. One of 2 shortest ways: `F' U2 F R' U' F R2 F`. The first shortest way to all good, `R2 F R2 F' R U`, ends in a fake HTR, 9 from HTR.

</details>

**66.** `F U R2 F2 U F R2 U2 R'`

Types `+ r u . r r +`. 2 twisted, out 3 on R/L, 1 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

9 moves, 5 quarter turns (6 moves with NISS). Closer turns: R, R2, R', U2, U', F, F2, F'. One of 44 shortest ways: `R U2 R2 F' U' F2 R2 U' F`. The first shortest way to all good, `R U R U F2 R`, ends in a fake HTR, 9 from HTR.

</details>

**67.** `F U2 F U R2 F2 U R2 U2`

Types `f + - u . . -`. 3 twisted, out 0 on R/L, 1 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 4 moves (3 qt), types 5, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (6 moves with NISS). Closer turns: F. One of 2 shortest ways: `F U' F R2 U F' U`. The first shortest way to all good, `F2 U R2 U F`, ends in a fake HTR, 9 from HTR.

</details>

**68.** `R' U' R' U' R2 F R`

Types `+ f u u r r u`. 1 twisted, out 2 on R/L, 3 on U/D, 1 on F/B. Out corners 6c, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: R', U. One of 4 shortest ways: `R' F' U R U R`. The first shortest way to all good, `R' F' U R U R`, ends in HTR.

</details>

**69.** `U F R' F2 R F2 U F'`

Types `. + r . u . .`. 1 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 5 moves (5 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (6 moves with NISS). Closer turns: F'. One of 2 shortest ways: `F' R F2 U F U R`. The first shortest way to all good, `R U R U2 F R2 F`, ends in a fake HTR, 9 from HTR.

</details>

**70.** `R2 U' R U' F' U F2 U R'`

Types `+ + - u - r +`. 5 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 3 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R. One of 6 shortest ways: `R U' F2 U R' U' R F`. The first shortest way to all good, `U R F2 R' F U2 F`, ends in a fake HTR, 9 from HTR.

</details>

**71.** `U2 F R' U' R U' F' U2`

Types `. + . f . - f`. 2 twisted, out 0 on R/L, 0 on U/D, 2 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (7 moves with NISS). Closer turns: R2, U2. One of 8 shortest ways: `R2 F R' U2 R' U2 R`. The first shortest way to all good, `R2 F R F2 R F2 R`, ends in a fake HTR, 9 from HTR.

</details>

**72.** `R U R' U R2 F' U F2 R'`

Types `f f - + r - u`. 3 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 4 moves (3 qt), types 7, types + parity 8. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: R', F. One of 4 shortest ways: `R' U2 F2 U F' R U2 R`. The first shortest way to all good, `U R2 U' R F' U R`, ends in a fake HTR, 9 from HTR.

</details>

**73.** `U' R2 U' R' F R' U' F' R2`

Types `. r . r . f u`. 0 twisted, out 2 on R/L, 1 on U/D, 1 on F/B. Out corners 4a, D-colour corners 4b, parity odd.

Floors: count table 4 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 1.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R'. One of 2 shortest ways: `R' F R2 F' R2 F R`. The first shortest way to all good, `F R' U2 R F R`, ends in a fake HTR, 9 from HTR.

</details>

**74.** `F2 R2 U F' R' F U' R'`

Types `r . + f r u .`. 1 twisted, out 2 on R/L, 1 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 2.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: R. One of 2 shortest ways: `R U F' R F U`. The first shortest way to all good, `R U F' R F U`, ends in HTR.

</details>

**75.** `R2 U R2 F U' F' U R2`

Types `u u + u . f +`. 2 twisted, out 0 on R/L, 3 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 5.

<details><summary>Answer</summary>

6 moves, 5 quarter turns (6 moves with NISS). Closer turns: F. One of 2 shortest ways: `F U2 R U F R`. The first shortest way to all good, `F R' U R F' U`, ends in a fake HTR, 9 from HTR.

</details>

**76.** `F2 U R' F U' F R2 U' R'`

Types `f r + - - - .`. 4 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 4 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R. One of 2 shortest ways: `R F2 U' R U2 R F`. The first shortest way to all good, `R' F R' F2 U R`, ends in a fake HTR, 9 from HTR.

</details>

**77.** `F' R' F2 U' R F U R'`

Types `. r f + + . -`. 3 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 4 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, R', F2. One of 6 shortest ways: `R U' F' R' U F2 R F`. The first shortest way to all good, `R2 F' R2 U2 F' R`, ends in a fake HTR, 9 from HTR.

</details>

**78.** `F2 R2 F R2 F' R' U' R2`

Types `r u r - r . -`. 2 twisted, out 3 on R/L, 1 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 2.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: R2. One of 4 shortest ways: `R2 U R F R2 F`. The first shortest way to all good, `R2 U R F R2 F`, ends in HTR.

</details>

**79.** `U2 R2 F2 U R2 U' F' U R2`

Types `u r - f . f .`. 1 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 2.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: R2. One of 2 shortest ways: `R2 U' F U R2 U`. The first shortest way to all good, `R2 U' F U R2 U`, ends in HTR.

</details>

**80.** `F' R U' R' U' F U R2 U`

Types `- u u . . + .`. 2 twisted, out 0 on R/L, 2 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: F'. One of 2 shortest ways: `F' R2 U R2 U' F U F`. The first shortest way to all good, `R U2 F2 U F2 U R`, ends in a fake HTR, 9 from HTR.

</details>

**81.** `R' F2 R U2 R U F2 U'`

Types `+ r r - - + .`. 4 twisted, out 2 on R/L, 0 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (3 qt), types 6, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R', U, F. One of 8 shortest ways: `R' U2 R' F2 R' F' U2 F`. The first shortest way to all good, `R F2 R U2 R F`, ends in a fake HTR, 9 from HTR.

</details>

**82.** `R2 U R2 F U' R2 F R' U' R'`

Types `. . . - r - f`. 2 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 3 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: R2, F'. One of 6 shortest ways: `R2 F U2 F2 U F' U F`. The first shortest way to all good, `R F2 R2 U' R' U`, ends in a fake HTR, 9 from HTR.

</details>

**83.** `F' R2 F2 U' R' U2 R2 F`

Types `u f u + u + -`. 3 twisted, out 0 on R/L, 3 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4a, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (6 moves with NISS). Closer turns: F. One of 4 shortest ways: `F R2 F U R2 F2 R`. The first shortest way to all good, `F R2 F U R2 F2 R`, ends in HTR.

</details>

**84.** `U2 R' F2 R' F U2 F U'`

Types `+ f f + f . r`. 2 twisted, out 1 on R/L, 0 on U/D, 3 on F/B. Out corners 4a, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 1.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (5 moves with NISS). Closer turns: U. One of 2 shortest ways: `U F' U2 F' R F2 R`. The first shortest way to all good, `U F' U2 F' R F2 R`, ends in HTR.

</details>

**85.** `U R2 F' U2 F R' F2 R U2`

Types `+ r - - - + u`. 5 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 3 moves (3 qt), types 5, types + parity 5. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: U', F, F'. One of 6 shortest ways: `U' R F U' F U' F`. The first shortest way to all good, `R2 U2 R F U`, ends in a fake HTR, 9 from HTR.

</details>

**86.** `U F U F' R2 U`

Types `u u - f . - u`. 2 twisted, out 0 on R/L, 3 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 5.

<details><summary>Answer</summary>

6 moves, 5 quarter turns (5 moves with NISS). Closer turns: U'. One of 2 shortest ways: `U' R2 F U' F' U`. The first shortest way to all good, `U' R2 F U' F' U`, ends in HTR.

</details>

**87.** `U F R F U2 R2 F2 R' F'`

Types `+ + . + r f +`. 4 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 4 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (6 moves with NISS). Closer turns: F. One of 6 shortest ways: `F R F2 R2 F' U' R' U`. The first shortest way to all good, `R U' F2 U R2 U' F`, ends in a fake HTR, 9 from HTR.

</details>

**88.** `U R2 F U' R2 F2 U' R'`

Types `. . - u f u r`. 1 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (6 moves with NISS). Closer turns: R, F. One of 16 shortest ways: `R U F2 R2 U F R2 U`. The first shortest way to all good, `F2 U' R U' F R' F`, ends in a fake HTR, 9 from HTR.

</details>

**89.** `U2 R' F2 R' U' R2`

Types `r u u r u r +`. 1 twisted, out 3 on R/L, 3 on U/D, 0 on F/B. Out corners 6c, D-colour corners 4c, parity odd.

Floors: count table 4 moves (3 qt), types 5, types + parity 5. Subset number of the placement: 3.

<details><summary>Answer</summary>

5 moves, 3 quarter turns (5 moves with NISS). Closer turns: R2. One of 2 shortest ways: `R2 U R F2 R`. The first shortest way to all good, `R2 U R F2 R`, ends in HTR.

</details>

**90.** `F R2 F' U2 F' U' F2 R'`

Types `u f - - r - u`. 3 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 4 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: U. One of 2 shortest ways: `U F2 U' F R2 U' F`. The first shortest way to all good, `U F2 U' F R2 U' F`, ends in HTR.

</details>

**91.** `U F2 R2 U' R' U' F`

Types `+ - + f - r -`. 5 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 3 moves (3 qt), types 5, types + parity 5. Subset number of the placement: 3.

<details><summary>Answer</summary>

5 moves, 3 quarter turns (5 moves with NISS). Closer turns: F2. One of 2 shortest ways: `F2 R2 F U R`. The first shortest way to all good, `F2 R2 F U R`, ends in HTR.

</details>

**92.** `R2 U' F' U' F2 R' F2 R U'`

Types `- u u r . u .`. 1 twisted, out 1 on R/L, 3 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4d, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (7 moves with NISS). Closer turns: U2. One of 4 shortest ways: `U2 R' F R F U' F`. The first shortest way to all good, `R U' R' F' U F' U`, ends in a fake HTR, 9 from HTR.

</details>

**93.** `R2 U2 F' U' R2 F2 U' R F' R`

Types `+ r - f + f f`. 3 twisted, out 1 on R/L, 0 on U/D, 3 on F/B. Out corners 4a, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: R', U'. One of 6 shortest ways: `R' F R' U F2 R2 U F`. The first shortest way to all good, `R2 U F2 U R U' F`, ends in a fake HTR, 9 from HTR.

</details>

**94.** `R F' R2 F U' R F R2 U2 R'`

Types `. - f f u + u`. 2 twisted, out 0 on R/L, 2 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 2 moves (2 qt), types 6, types + parity 8. Subset number of the placement: 5.

<details><summary>Answer</summary>

9 moves, 5 quarter turns (8 moves with NISS). Closer turns: R2, R', F, F2, F'. One of 22 shortest ways: `R2 U R' U R2 F' R U F`. The first shortest way to all good, `F U2 F' U R2 U`, ends in a fake HTR, 9 from HTR.

</details>

**95.** `R U R' F' U R2 F R'`

Types `+ - + + f f +`. 5 twisted, out 0 on R/L, 0 on U/D, 2 on F/B. Out corners 2c, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 5, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, R', U. One of 8 shortest ways: `R F' R2 U R' F' R F`. The first shortest way to all good, `U R' U2 R F`, ends in a fake HTR, 9 from HTR.

</details>

**96.** `U R2 U' F2 U' R F' R' U2`

Types `. u . + . f +`. 2 twisted, out 0 on R/L, 1 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 3 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

9 moves, 6 quarter turns (8 moves with NISS). Closer turns: R2, R', U, U2, U', F, F'. One of 32 shortest ways: `R2 U R2 U' R2 U' R F R`. The first shortest way to all good, `R U F U2 R2 U`, ends in a fake HTR, 9 from HTR.

</details>

**97.** `U R' U' F U2 F' R2 F' U'`

Types `f + f u f + .`. 2 twisted, out 0 on R/L, 1 on U/D, 3 on F/B. Out corners 4b, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: R', U2. One of 6 shortest ways: `R' U2 F2 U' R' F U2 F`. The first shortest way to all good, `F2 R U2 R' F' U`, ends in a fake HTR, 9 from HTR.

</details>

**98.** `R' U R' F R2 U' F' R2 F R'`

Types `+ . + - u + f`. 4 twisted, out 0 on R/L, 1 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 4 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: R', U, F, F2. One of 14 shortest ways: `R' U F R F2 U' F2 U`. The first shortest way to all good, `F2 U2 R' F U R`, ends in a fake HTR, 9 from HTR.

</details>

**99.** `F' R U2 F2 R F R2 U2 R'`

Types `+ . + u f f f`. 2 twisted, out 0 on R/L, 1 on U/D, 3 on F/B. Out corners 4b, D-colour corners 4d, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

9 moves, 5 quarter turns (6 moves with NISS). Closer turns: R, R2, R', U, U2, U', F2, F'. One of 44 shortest ways: `R U2 R2 F' R' F2 U2 R' F`. The first shortest way to all good, `R U F R F2 U`, ends in a fake HTR, 9 from HTR.

</details>

**100.** `R' U2 F' U2 F R F2 U2 R`

Types `. - . u f u r`. 1 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: U, F2. One of 4 shortest ways: `U F2 R F U2 R2 F R`. The first shortest way to all good, `F U' F U' R U`, ends in a fake HTR, 9 from HTR.

</details>

**101.** `F2 R F2 R' U F' R U' F`

Types `- u . . + f -`. 3 twisted, out 0 on R/L, 1 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 4 moves (3 qt), types 4, types + parity 4. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R', F'. One of 4 shortest ways: `R' F R' U F' U R2 U`. The first shortest way to all good, `U' R2 U F`, ends in a fake HTR, 9 from HTR.

</details>

**102.** `U F R F2 R F' U R' U2`

Types `. f r r . - r`. 1 twisted, out 3 on R/L, 0 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: F2. One of 4 shortest ways: `F2 U R U' R F' U' F`. The first shortest way to all good, `F' R' F' U' R U' R`, ends in a fake HTR, 9 from HTR.

</details>

**103.** `U' R2 F R' U' R' F U'`

Types `. + - + . + +`. 5 twisted, out 0 on R/L, 0 on U/D, 0 on F/B. Out corners 0c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 8, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R', U. One of 10 shortest ways: `R' U R F2 U' F R F`. The first shortest way to all good, `R' U R F2 U' F R F`, ends in HTR.

</details>

**104.** `U F U2 R' U2 F' R F2 R2`

Types `- - + u . r -`. 4 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 4 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R. One of 2 shortest ways: `R U2 F2 R U' R2 F U`. The first shortest way to all good, `R F2 R U' F2 R' U`, ends in a fake HTR, 9 from HTR.

</details>

**105.** `F R2 F U2 R2 F R' U`

Types `+ r u u r f r`. 1 twisted, out 3 on R/L, 2 on U/D, 1 on F/B. Out corners 6c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (6 moves with NISS). Closer turns: R', U'. One of 4 shortest ways: `R' F U F' R U' R`. The first shortest way to all good, `U2 R U2 R' F R`, ends in a fake HTR, 9 from HTR.

</details>

**106.** `R2 U R U' F U R' F2`

Types `- . - u + u +`. 4 twisted, out 0 on R/L, 2 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 5 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (7 moves with NISS). Closer turns: F2. One of 2 shortest ways: `F2 R U' F' U R' U`. The first shortest way to all good, `U2 R U2 F U' R`, ends in a fake HTR, 9 from HTR.

</details>

**107.** `U R2 F U R2 U F`

Types `f u + f r f u`. 1 twisted, out 1 on R/L, 2 on U/D, 3 on F/B. Out corners 6c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (6 moves with NISS). Closer turns: U, F'. One of 6 shortest ways: `U R F' U F U' F`. The first shortest way to all good, `U R' F U F U`, ends in a fake HTR, 9 from HTR.

</details>

**108.** `R F' R U2 F U R2 U R2`

Types `f u + r . f -`. 2 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 4 moves (3 qt), types 6, types + parity 8. Subset number of the placement: 2.

<details><summary>Answer</summary>

9 moves, 6 quarter turns (7 moves with NISS). Closer turns: R2, U, U', F. One of 22 shortest ways: `R2 U' R U' R' U R F' U`. The first shortest way to all good, `R2 U2 F' U R2 F`, ends in a fake HTR, 9 from HTR.

</details>

**109.** `R2 F U R' U2 F U F2 R' U'`

Types `+ . - r . f +`. 3 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4a, parity odd.

Floors: count table 4 moves (3 qt), types 6, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: U'. One of 2 shortest ways: `U' F2 U F R2 U' R`. The first shortest way to all good, `F R2 F' U R2 F`, ends in a fake HTR, 9 from HTR.

</details>

**110.** `R F' R2 F' U2 F U' F R'`

Types `- . f u r . r`. 1 twisted, out 2 on R/L, 1 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: F. One of 2 shortest ways: `F R' F U2 F' U F' U`. The first shortest way to all good, `U R' F' R U' R`, ends in a fake HTR, 9 from HTR.

</details>

**111.** `R2 U' R F' U R' F2 R'`

Types `- - f f f r +`. 3 twisted, out 1 on R/L, 0 on U/D, 3 on F/B. Out corners 4a, D-colour corners 4a, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (7 moves with NISS). Closer turns: R. One of 2 shortest ways: `R F2 R U' F R' U`. The first shortest way to all good, `R F2 R U' F R' U`, ends in HTR.

</details>

**112.** `R' F R' F R' U' F' R2`

Types `+ u f - - + -`. 5 twisted, out 0 on R/L, 1 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 3 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R2, U2, F, F'. One of 14 shortest ways: `R2 F U R F' R F' R`. The first shortest way to all good, `R2 U2 F2 U' R F`, ends in a fake HTR, 9 from HTR.

</details>

**113.** `R2 F U' F2 R2 U F'`

Types `r f - . r + f`. 2 twisted, out 2 on R/L, 0 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4c, parity even.

Floors: count table 2 moves (2 qt), types 6, types + parity 6. Subset number of the placement: 2.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (5 moves with NISS). Closer turns: F. One of 2 shortest ways: `F U' R2 F2 U F`. The first shortest way to all good, `F U' R2 F2 U F`, ends in HTR.

</details>

**114.** `R' F2 R' U R F' R2 F' U R'`

Types `. - + - - . -`. 5 twisted, out 0 on R/L, 0 on U/D, 0 on F/B. Out corners 0c, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: U', F2. One of 8 shortest ways: `U' F R U2 R2 F U' R`. The first shortest way to all good, `R F' R F' U2 F' U`, ends in a fake HTR, 9 from HTR.

</details>

**115.** `R2 F R F' U2 F2 U' R'`

Types `- f . . + . f`. 2 twisted, out 0 on R/L, 0 on U/D, 2 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (6 moves with NISS). Closer turns: R, F'. One of 8 shortest ways: `R U F2 U2 F R' F`. The first shortest way to all good, `R U F2 U2 F R' F`, ends in HTR.

</details>

**116.** `R F U' F' R U2 F' R U`

Types `r f . u + f .`. 1 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 2.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: R2, F. One of 4 shortest ways: `R2 F2 U F U' F R' F`. The first shortest way to all good, `R' F U R' U F`, ends in a fake HTR, 9 from HTR.

</details>

**117.** `F R' U' F' U F2 U F2`

Types `r . u r r + +`. 2 twisted, out 3 on R/L, 1 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: R, F2, F'. One of 20 shortest ways: `R U' F' U R U R' F`. The first shortest way to all good, `U R2 F R U F`, ends in a fake HTR, 9 from HTR.

</details>

**118.** `F2 R' F R' F R2 F R2`

Types `. - . - f f -`. 3 twisted, out 0 on R/L, 0 on U/D, 2 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R2. One of 2 shortest ways: `R2 F' R2 F' R F' R`. The first shortest way to all good, `R2 F' R2 F' R F' R`, ends in HTR.

</details>

**119.** `U R2 F2 U' R U' F'`

Types `r - + f f f -`. 3 twisted, out 1 on R/L, 0 on U/D, 3 on F/B. Out corners 4b, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

6 moves, 5 quarter turns (5 moves with NISS). Closer turns: F. One of 2 shortest ways: `F U R' U R2 U`. The first shortest way to all good, `R2 U F' R' U2 R`, ends in a fake HTR, 9 from HTR.

</details>

**120.** `R' F2 U F' U2 R2 F2 U' F R'`

Types `. + f f . + +`. 3 twisted, out 0 on R/L, 0 on U/D, 2 on F/B. Out corners 2c, D-colour corners 4a, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: R2. One of 2 shortest ways: `R2 U2 R U R' F U F`. The first shortest way to all good, `R2 F R2 F U' F R`, ends in a fake HTR, 9 from HTR.

</details>

**121.** `F' U2 F' U R F2 U' F2 R'`

Types `u u . + . + +`. 3 twisted, out 0 on R/L, 2 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: U, F2. One of 4 shortest ways: `U F2 U' F R' F' R2 F`. The first shortest way to all good, `R U F R2 U' R2 U`, ends in a fake HTR, 9 from HTR.

</details>

**122.** `U' F2 R F' R2 F R2 F' R2`

Types `- r u r r f u`. 1 twisted, out 3 on R/L, 2 on U/D, 1 on F/B. Out corners 6c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, U, U'. One of 10 shortest ways: `R U R2 U2 R' F R`. The first shortest way to all good, `R U R2 U2 R' F R`, ends in HTR.

</details>

**123.** `F R2 F' R' F R2 U2 R' U R'`

Types `f r . - f u .`. 1 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4a, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: F2. One of 2 shortest ways: `F2 R2 F U2 F' R F' R`. The first shortest way to all good, `F2 U F' U F U2 F`, ends in a fake HTR, 9 from HTR.

</details>

**124.** `R' U F2 U R' U R U'`

Types `r u f u - + .`. 2 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4a, D-colour corners 4a, parity odd.

Floors: count table 4 moves (3 qt), types 6, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: F, F'. One of 4 shortest ways: `F U2 F U' R' F2 R`. The first shortest way to all good, `R' U2 F U R2 F`, ends in a fake HTR, 9 from HTR.

</details>

**125.** `F2 U R' F U2 R2 F R2`

Types `u + + + r . -`. 4 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 4 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (6 moves with NISS). Closer turns: R2, U2. One of 4 shortest ways: `R2 F' R2 U2 F' R U`. The first shortest way to all good, `R2 F' R2 U2 F' R U`, ends in HTR.

</details>

**126.** `F' R2 U2 R' U2 F' R' U2`

Types `+ . + f u u r`. 2 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 4 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: U2. One of 2 shortest ways: `U2 R F U2 R' F`. The first shortest way to all good, `U2 R F U2 R' F`, ends in HTR.

</details>

**127.** `U2 F U2 F U F R U2 F' R'`

Types `+ - . + u f +`. 4 twisted, out 0 on R/L, 1 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 4 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 5.

<details><summary>Answer</summary>

9 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, R2, F, F2, F'. One of 24 shortest ways: `R F U2 R' U F2 U' F' U`. The first shortest way to all good, `R' U R' U R2 F' U`, ends in a fake HTR, 9 from HTR.

</details>

**128.** `R2 U2 F' U' F2 R U`

Types `r f - . r - u`. 2 twisted, out 2 on R/L, 1 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 4 moves (3 qt), types 5, types + parity 5. Subset number of the placement: 4.

<details><summary>Answer</summary>

5 moves, 4 quarter turns (5 moves with NISS). Closer turns: U'. One of 2 shortest ways: `U' R' F2 U F`. The first shortest way to all good, `U' R' F2 U F`, ends in HTR.

</details>

**129.** `U2 F U' R2 F2 U R' F`

Types `r f f u + + -`. 3 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4a, D-colour corners 4c, parity odd.

Floors: count table 4 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (6 moves with NISS). Closer turns: F, F'. One of 4 shortest ways: `F U' R U2 F2 R' U`. The first shortest way to all good, `U R' F U' R F' R`, ends in a fake HTR, 9 from HTR.

</details>

**130.** `R2 U2 R F' U R' F' U R'`

Types `u u + f + . r`. 2 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4a, parity odd.

Floors: count table 4 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R. One of 2 shortest ways: `R U' F R U' F R`. The first shortest way to all good, `R U' F R U' F R`, ends in HTR.

</details>

**131.** `U' F R2 F' U R2 F2 U' R2`

Types `r f u r u + u`. 1 twisted, out 2 on R/L, 3 on U/D, 1 on F/B. Out corners 6c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: F'. One of 2 shortest ways: `F' R2 U F' R U' F R`. The first shortest way to all good, `U F' R2 F U' R F`, ends in a fake HTR, 9 from HTR.

</details>

**132.** `F R2 U2 F' R U' R F2 U2`

Types `r u . f u f f`. 0 twisted, out 1 on R/L, 2 on U/D, 3 on F/B. Out corners 6c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: F. One of 2 shortest ways: `F R2 F' U2 R F R`. The first shortest way to all good, `U' R' U R2 F R`, ends in a fake HTR, 9 from HTR.

</details>

**133.** `F2 R2 F R F U F U R2`

Types `r r + + . + .`. 3 twisted, out 2 on R/L, 0 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: R2. One of 4 shortest ways: `R2 F R U F2 R`. The first shortest way to all good, `R2 F R U F2 R`, ends in HTR.

</details>

**134.** `F U F' R2 F' R2 F U2 R`

Types `+ + . u f f f`. 2 twisted, out 0 on R/L, 1 on U/D, 3 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: R2, R', F. One of 14 shortest ways: `R2 U' F R F' R2 U' F`. The first shortest way to all good, `R2 U2 R' U2 R' F' U`, ends in a fake HTR, 9 from HTR.

</details>

**135.** `U2 F R' U' F R2 F2 U2`

Types `+ r u - . + +`. 4 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 4 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (5 moves with NISS). Closer turns: F2. One of 2 shortest ways: `F2 R2 F' R U F`. The first shortest way to all good, `R2 U' F' R U F`, ends in a fake HTR, 9 from HTR.

</details>

**136.** `R2 U R2 U' F U' R F U2`

Types `. u f u u r u`. 0 twisted, out 1 on R/L, 4 on U/D, 1 on F/B. Out corners 6c, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: R', U2. One of 4 shortest ways: `R' F2 R F' R U2 F' R`. The first shortest way to all good, `R U F' R U' R2 U`, ends in a fake HTR, 9 from HTR.

</details>

**137.** `U' R U2 R' F' R2 F U2 R'`

Types `u f - . . + +`. 3 twisted, out 0 on R/L, 1 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 4 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (7 moves with NISS). Closer turns: R2. One of 4 shortest ways: `R2 U R2 U' F R2 U`. The first shortest way to all good, `R F2 R F R2 U' F`, ends in a fake HTR, 9 from HTR.

</details>

**138.** `F2 R' F' R' U2 F U' R' U2`

Types `f f u u + + +`. 3 twisted, out 0 on R/L, 2 on U/D, 2 on F/B. Out corners 4a, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: U2. One of 2 shortest ways: `U2 R U F' U2 R F R`. The first shortest way to all good, `F' R' F R' F' U`, ends in a fake HTR, 9 from HTR.

</details>

**139.** `U' F U' R U R' U2 F`

Types `- . - + - - .`. 5 twisted, out 0 on R/L, 0 on U/D, 0 on F/B. Out corners 0c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R'. One of 2 shortest ways: `R' U2 F R F2 U' R`. The first shortest way to all good, `R U2 F R U2 F' R`, ends in a fake HTR, 9 from HTR.

</details>

**140.** `F2 R' F' R F' U2 F' R'`

Types `- f f r - + u`. 3 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4c, parity even.

Floors: count table 4 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (7 moves with NISS). Closer turns: R. One of 2 shortest ways: `R F U2 F R' F R`. The first shortest way to all good, `R F U2 F R' F R`, ends in HTR.

</details>

**141.** `R2 F2 U2 R' U' R U' F U'`

Types `- + . f f f f`. 2 twisted, out 0 on R/L, 0 on U/D, 4 on F/B. Out corners 4b, D-colour corners 4c, parity even.

Floors: count table 4 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 2.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: U. One of 2 shortest ways: `U F' U R' U R`. The first shortest way to all good, `U F' U R' U R`, ends in HTR.

</details>

**142.** `R' F' R U' R U' R2`

Types `. u r r - f .`. 1 twisted, out 2 on R/L, 1 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (6 moves with NISS). Closer turns: R2. One of 2 shortest ways: `R2 U R' U R' F R`. The first shortest way to all good, `R U F' U2 F U' F`, ends in a fake HTR, 9 from HTR.

</details>

**143.** `F' U2 F' R F' U' R'`

Types `+ + + f - . r`. 4 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 4 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (6 moves with NISS). Closer turns: R, F2. One of 6 shortest ways: `R U F R' F U2 F`. The first shortest way to all good, `R U F R' F U2 F`, ends in HTR.

</details>

**144.** `U2 R' U2 R U R2 U' F2`

Types `. - u - r . +`. 3 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4a, parity even.

Floors: count table 4 moves (3 qt), types 6, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (7 moves with NISS). Closer turns: F2. One of 2 shortest ways: `F2 U R2 U' R' U2 R`. The first shortest way to all good, `U2 R2 U' R2 U R`, ends in a fake HTR, 9 from HTR.

</details>

**145.** `R2 F2 R F' U' F R' U2 R'`

Types `r . + . f . +`. 2 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 3 moves (3 qt), types 5, types + parity 5. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (7 moves with NISS). Closer turns: R. One of 2 shortest ways: `R U2 R F' U F R`. The first shortest way to all good, `R2 F' U F R`, ends in a fake HTR, 9 from HTR.

</details>

**146.** `U2 F' R F U2 R' U R`

Types `. - r + u - -`. 4 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 4 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (7 moves with NISS). Closer turns: R'. One of 2 shortest ways: `R' U' R U2 F' R' F`. The first shortest way to all good, `R F U2 R' F U F`, ends in a fake HTR, 9 from HTR.

</details>

**147.** `U' F2 R U' R F2 R' F R'`

Types `+ f + . f r f`. 2 twisted, out 1 on R/L, 0 on U/D, 3 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R2, U', F. One of 12 shortest ways: `R2 F U F R U2 F`. The first shortest way to all good, `R2 F U F R U2 F`, ends in HTR.

</details>

**148.** `F' R' F U2 F' U2 R F' R`

Types `. . r r f f .`. 0 twisted, out 2 on R/L, 0 on U/D, 2 on F/B. Out corners 4a, D-colour corners 4c, parity odd.

Floors: count table 6 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

9 moves, 5 quarter turns (8 moves with NISS). Closer turns: R, R', F2. One of 12 shortest ways: `R U' R U2 F' U2 F U' F`. The first shortest way to all good, `U R2 F' R2 F R2 U`, ends in a fake HTR, 9 from HTR.

</details>

**149.** `F R' F U' F2 R F' U' R2`

Types `- r f - u r +`. 3 twisted, out 2 on R/L, 1 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity odd.

Floors: count table 4 moves (3 qt), types 6, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: F'. One of 2 shortest ways: `F' R U2 F2 R F' U`. The first shortest way to all good, `U F2 U F2 R F`, ends in a fake HTR, 9 from HTR.

</details>

**150.** `R U F R2 U2 F U' F' R2`

Types `u u - u r u u`. 1 twisted, out 1 on R/L, 5 on U/D, 0 on F/B. Out corners 6c, D-colour corners 4b, parity even.

Floors: count table 5 moves (5 qt), types 5, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: F2, F'. One of 4 shortest ways: `F2 R' U2 F R' F U' F`. The first shortest way to all good, `U R F' R F`, ends in a fake HTR, 9 from HTR.

</details>

**151.** `F' U2 R U' R2 U2 F2 U' F' R'`

Types `u u f + u - -`. 3 twisted, out 0 on R/L, 3 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: U', F2, F'. One of 10 shortest ways: `U' R F' U F' U F' R`. The first shortest way to all good, `R' U2 R F' R' F U`, ends in a fake HTR, 9 from HTR.

</details>

**152.** `R' U F2 U R' U R' U`

Types `r u r u + + .`. 2 twisted, out 2 on R/L, 2 on U/D, 0 on F/B. Out corners 4a, D-colour corners 4c, parity odd.

Floors: count table 2 moves (2 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, R', U', F2. One of 10 shortest ways: `R F' R F' U F2 U R`. The first shortest way to all good, `R2 F U F2 R' F`, ends in a fake HTR, 9 from HTR.

</details>

**153.** `U R' U2 F' R' U' F2 R F' U2`

Types `u u . u + f +`. 2 twisted, out 0 on R/L, 3 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: R', U. One of 6 shortest ways: `R' U' R2 U R2 F' R2 F`. The first shortest way to all good, `R2 U2 R' U2 R' U' F`, ends in a fake HTR, 9 from HTR.

</details>

**154.** `R' F2 R' F R' F2 U' F R'`

Types `+ + u f f r +`. 3 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4a, D-colour corners 4c, parity odd.

Floors: count table 4 moves (3 qt), types 8, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: U, U'. One of 4 shortest ways: `U R' F' U' F2 R U' F`. The first shortest way to all good, `U R U2 R U R' F2 R`, ends in a fake HTR, 9 from HTR.

</details>

**155.** `F' R' U F' R' F2 R2 F'`

Types `. + - u r r u`. 2 twisted, out 2 on R/L, 2 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4a, parity even.

Floors: count table 2 moves (2 qt), types 7, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (6 moves with NISS). Closer turns: R2, U, U2, F, F2, F'. One of 14 shortest ways: `R2 U2 R' F2 R U' F2 U`. The first shortest way to all good, `F2 R U2 R' U R2 U`, ends in a fake HTR, 9 from HTR.

</details>

**156.** `F2 R F R2 F U' R2 U R'`

Types `u + . f - - -`. 4 twisted, out 0 on R/L, 1 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 4 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: R, F. One of 8 shortest ways: `R U F2 R' U' R2 U' F`. The first shortest way to all good, `R' F' R' U2 F U' F`, ends in a fake HTR, 9 from HTR.

</details>

**157.** `R2 U R F' R2 U F2`

Types `+ + f . f - -`. 4 twisted, out 0 on R/L, 0 on U/D, 2 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 5 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: F2. One of 2 shortest ways: `F2 U' R2 F R' U`. The first shortest way to all good, `F2 U' R2 F R' U`, ends in HTR.

</details>

**158.** `U2 F' R F' R U F' R' U`

Types `r f - u - u +`. 3 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 4 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: U, U'. One of 4 shortest ways: `U F' U2 R' F R2 F U`. The first shortest way to all good, `U F U F' U2 R F`, ends in a fake HTR, 9 from HTR.

</details>

**159.** `R' U R F2 U2 F' U F U2`

Types `r u f f - . -`. 2 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4a, D-colour corners 4d, parity even.

Floors: count table 4 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (7 moves with NISS). Closer turns: R2. One of 8 shortest ways: `R2 F R F2 R2 F' U2 F`. The first shortest way to all good, `R U' F R F R2 U`, ends in a fake HTR, 9 from HTR.

</details>

**160.** `R' U F U2 F2 R2 F' U R'`

Types `r u f u r + f`. 1 twisted, out 2 on R/L, 2 on U/D, 2 on F/B. Out corners 6c, D-colour corners 4a, parity even.

Floors: count table 6 moves (5 qt), types 6, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (6 moves with NISS). Closer turns: U', F2. One of 4 shortest ways: `U' R' F' U2 R2 F U' F`. The first shortest way to all good, `R' U' R2 U' F U`, ends in a fake HTR, 9 from HTR.

</details>

**161.** `F2 R' F' R U' R U2 F' R'`

Types `- f r r u u r`. 1 twisted, out 3 on R/L, 2 on U/D, 1 on F/B. Out corners 6c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, U2, U'. One of 8 shortest ways: `R F U2 R' U R' F R`. The first shortest way to all good, `R U F2 U2 R U' R`, ends in a fake HTR, 9 from HTR.

</details>

**162.** `F R2 U2 F' R' F R2 F2`

Types `u - . u f r .`. 1 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (6 moves with NISS). Closer turns: R2, F2. One of 4 shortest ways: `R2 F2 R F2 R F R`. The first shortest way to all good, `R2 U' R' F R' U' F`, ends in a fake HTR, 9 from HTR.

</details>

**163.** `U' F2 R2 F' U2 R2 F U'`

Types `u r r r f . u`. 0 twisted, out 3 on R/L, 2 on U/D, 1 on F/B. Out corners 6c, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (5 moves with NISS). Closer turns: U. One of 2 shortest ways: `U F' R2 U2 F' U`. The first shortest way to all good, `U F' R2 U2 F' U`, ends in HTR.

</details>

**164.** `F2 R' F' R2 F2 U' F' R U2`

Types `- . u u u + u`. 2 twisted, out 0 on R/L, 4 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4c, parity odd.

Floors: count table 4 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: F. One of 4 shortest ways: `F U R2 U2 F U F`. The first shortest way to all good, `R2 F2 R' F U' R`, ends in a fake HTR, 9 from HTR.

</details>

**165.** `F2 R U F R2 U' R2 F' R2`

Types `- - . r u f u`. 2 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 4 moves (3 qt), types 8, types + parity 8. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R2, U, U', F'. One of 12 shortest ways: `R2 F R2 U R2 F' U' R`. The first shortest way to all good, `R U' F U R2 F2 R' U`, ends in a fake HTR, 9 from HTR.

</details>

**166.** `F' U F R' U' F' R`

Types `+ - + - - . +`. 6 twisted, out 0 on R/L, 0 on U/D, 0 on F/B. Out corners 0c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, R', F, F'. One of 12 shortest ways: `R F U R F' U' F`. The first shortest way to all good, `R F U R F' U' F`, ends in HTR.

</details>

**167.** `F2 U' F R' U R2 U' F2`

Types `f . - + f - +`. 4 twisted, out 0 on R/L, 0 on U/D, 2 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: F2. One of 2 shortest ways: `F2 U R2 U' R F' U`. The first shortest way to all good, `F U2 F R' F U2 F`, ends in a fake HTR, 9 from HTR.

</details>

**168.** `F' U F R' U F2 U R2 U'`

Types `. . - + . + -`. 4 twisted, out 0 on R/L, 0 on U/D, 0 on F/B. Out corners 0c, D-colour corners 4b, parity odd.

Floors: count table 4 moves (2 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: R2, U, U2. One of 8 shortest ways: `R2 U' F2 R' F R2 U' R`. The first shortest way to all good, `R' F' U2 R U R2 F`, ends in a fake HTR, 9 from HTR.

</details>

**169.** `U2 F U' R U2 R2 U'`

Types `. r + . u f u`. 1 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 2.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (5 moves with NISS). Closer turns: R, U, U'. One of 6 shortest ways: `R F U F' R U`. The first shortest way to all good, `R F U F' R U`, ends in HTR.

</details>

**170.** `R2 U2 F' R2 F' U' F2 U2 R`

Types `- + . u - - r`. 4 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 4 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (7 moves with NISS). Closer turns: R'. One of 2 shortest ways: `R' U2 F2 U F R2 F`. The first shortest way to all good, `R' U2 F2 U F R2 F`, ends in HTR.

</details>

**171.** `R' F2 R U R' F U' R'`

Types `r r + . - . .`. 2 twisted, out 2 on R/L, 0 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, U2, U', F2. One of 20 shortest ways: `R U F' R U' R' F2 R`. The first shortest way to all good, `U R2 F2 U R2 U R`, ends in a fake HTR, 9 from HTR.

</details>

**172.** `R' U F' R' U' F2 R U R'`

Types `r - . f - . +`. 3 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 4 moves (3 qt), types 5, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (8 moves with NISS). Closer turns: R2, F2. One of 4 shortest ways: `R2 U2 R' U2 R' F' U2 F`. The first shortest way to all good, `F2 R F2 R F`, ends in a fake HTR, 9 from HTR.

</details>

**173.** `F U2 R2 U F U2 R' F`

Types `r f + r + r .`. 2 twisted, out 3 on R/L, 0 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 5.

<details><summary>Answer</summary>

6 moves, 5 quarter turns (6 moves with NISS). Closer turns: F'. One of 2 shortest ways: `F' R U2 F' U F`. The first shortest way to all good, `F' R U2 F' U F`, ends in HTR.

</details>

**174.** `R2 U R2 U R' F' R2`

Types `- + . f + + r`. 4 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 4 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: R2. One of 2 shortest ways: `R2 F R U' R2 U`. The first shortest way to all good, `R2 F R U' R2 U`, ends in HTR.

</details>

**175.** `R2 U2 R' F2 R U R2 F' R'`

Types `r f + f f u u`. 1 twisted, out 1 on R/L, 2 on U/D, 3 on F/B. Out corners 6c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R. One of 2 shortest ways: `R F R2 U' R' F2 R`. The first shortest way to all good, `R F R2 U' R' F2 R`, ends in HTR.

</details>

**176.** `U' F' U2 F' U R2 U F2 U2`

Types `. - + + u . r`. 3 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 4 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R2, U2. One of 4 shortest ways: `R2 U F2 U F' U2 F U`. The first shortest way to all good, `R' U' F R F' U' R`, ends in a fake HTR, 9 from HTR.

</details>

**177.** `F2 R2 U2 R' F U' F2 R F2`

Types `- . + u + - u`. 4 twisted, out 0 on R/L, 2 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 5 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: F2. One of 2 shortest ways: `F2 R' F2 U F' R`. The first shortest way to all good, `F2 R' F2 U F' R`, ends in HTR.

</details>

**178.** `F' U R' F' R2 F' R2 F R2`

Types `- r - + + f +`. 5 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4b, parity even.

Floors: count table 3 moves (3 qt), types 4, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (7 moves with NISS). Closer turns: R, R2, F2. One of 8 shortest ways: `R U' F' U R2 U' R2 U`. The first shortest way to all good, `U2 R U' F`, ends in a fake HTR, 9 from HTR.

</details>

**179.** `U' F2 R2 U F R2 U' R' U2 R`

Types `r f - u . + r`. 2 twisted, out 2 on R/L, 1 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 4 moves (3 qt), types 6, types + parity 8. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (8 moves with NISS). Closer turns: F. One of 2 shortest ways: `F R' U2 R U R2 U F`. The first shortest way to all good, `F2 U2 R U F2 R`, ends in a fake HTR, 9 from HTR.

</details>

**180.** `R F R2 U2 F R U2 F U`

Types `+ + + r + u +`. 5 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4a, parity even.

Floors: count table 3 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (7 moves with NISS). Closer turns: U2, F'. One of 6 shortest ways: `U2 R2 U F2 U R U2 F`. The first shortest way to all good, `U' F2 U R U2 F`, ends in a fake HTR, 9 from HTR.

</details>

**181.** `R2 U2 R F' R F' U2 F R2`

Types `. + f f u f +`. 2 twisted, out 0 on R/L, 1 on U/D, 3 on F/B. Out corners 4a, D-colour corners 4c, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R2, U. One of 4 shortest ways: `R2 F' U2 F R' F R`. The first shortest way to all good, `R U R2 U' R U' F`, ends in a fake HTR, 9 from HTR.

</details>

**182.** `U2 R' U2 R2 U' R F' R`

Types `+ + + u - u +`. 5 twisted, out 0 on R/L, 2 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4b, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (6 moves with NISS). Closer turns: R'. One of 4 shortest ways: `R' F R' U R2 U2 R`. The first shortest way to all good, `R F R' U R' U2 R`, ends in a fake HTR, 9 from HTR.

</details>

**183.** `F U2 R' U' F2 U' F R2 F' U'`

Types `. r . - + u -`. 3 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 4 moves (3 qt), types 7, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: R, R'. One of 4 shortest ways: `R U2 R2 U' R2 F' R F`. The first shortest way to all good, `R F R F' U F2 U`, ends in a fake HTR, 9 from HTR.

</details>

**184.** `R F' U F' U' F2 R' F2 R'`

Types `r r . + r - r`. 2 twisted, out 4 on R/L, 0 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4c, parity odd.

Floors: count table 4 moves (4 qt), types 6, types + parity 8. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: R2, F. One of 4 shortest ways: `R2 F U' R2 U F2 R F`. The first shortest way to all good, `R U R' U F' R`, ends in a fake HTR, 9 from HTR.

</details>

**185.** `F U2 F U2 F' U F U' R'`

Types `. . f r u . f`. 0 twisted, out 1 on R/L, 1 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4c, parity odd.

Floors: count table 4 moves (4 qt), types 4, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (7 moves with NISS). Closer turns: F2. One of 4 shortest ways: `F2 U' F R2 F2 U F R`. The first shortest way to all good, `R' U R' U`, ends in a fake HTR, 9 from HTR.

</details>

**186.** `U' F' U F U2 R' U R2 U2`

Types `u . + f - . +`. 3 twisted, out 0 on R/L, 1 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4a, parity even.

Floors: count table 4 moves (3 qt), types 6, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 4 quarter turns (7 moves with NISS). Closer turns: F'. One of 2 shortest ways: `F' R U R' U2 R F`. The first shortest way to all good, `R2 F' R2 U2 F' U`, ends in a fake HTR, 9 from HTR.

</details>

**187.** `R U2 F' R2 F2 R' U' F2 U2`

Types `. r r u - u +`. 2 twisted, out 2 on R/L, 2 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4c, parity even.

Floors: count table 2 moves (2 qt), types 7, types + parity 8. Subset number of the placement: 2.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (7 moves with NISS). Closer turns: U'. One of 2 shortest ways: `U' R U' R' F U' R F`. The first shortest way to all good, `U F' R F R' U R`, ends in a fake HTR, 9 from HTR.

</details>

**188.** `F R U R' U R F2 R F' R2`

Types `u u + + - - .`. 4 twisted, out 0 on R/L, 2 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4a, parity even.

Floors: count table 5 moves (3 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 4 quarter turns (7 moves with NISS). Closer turns: R'. One of 2 shortest ways: `R' U R U2 F2 R U' R`. The first shortest way to all good, `U R U R2 F2 R U`, ends in a fake HTR, 9 from HTR.

</details>

**189.** `U2 R F U2 R2 F2 R' U2 R'`

Types `+ r u r - r -`. 3 twisted, out 3 on R/L, 1 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4c, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 6. Subset number of the placement: 2.

<details><summary>Answer</summary>

6 moves, 4 quarter turns (6 moves with NISS). Closer turns: R'. One of 4 shortest ways: `R' F U' F2 R2 F`. The first shortest way to all good, `R' F U' F2 R2 F`, ends in HTR.

</details>

**190.** `U2 F' R' U R' U2 F R U'`

Types `u f + u - . f`. 2 twisted, out 0 on R/L, 2 on U/D, 2 on F/B. Out corners 4b, D-colour corners 4b, parity odd.

Floors: count table 2 moves (2 qt), types 5, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 3 quarter turns (7 moves with NISS). Closer turns: U. One of 12 shortest ways: `U R U2 R2 F2 U R' U`. The first shortest way to all good, `U2 F2 R2 F U`, ends in a fake HTR, 9 from HTR.

</details>

**191.** `R' U R U F2 U R' U' F2`

Types `- + . + . . -`. 4 twisted, out 0 on R/L, 0 on U/D, 0 on F/B. Out corners 0c, D-colour corners 4b, parity odd.

Floors: count table 4 moves (2 qt), types 6, types + parity 8. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 7 quarter turns (8 moves with NISS). Closer turns: R'. One of 8 shortest ways: `R' U R' U2 R' F' U' F`. The first shortest way to all good, `R' U F' U' F R`, ends in a fake HTR, 9 from HTR.

</details>

**192.** `R2 F R2 F U2 R' U' F R2`

Types `+ . r r - - +`. 4 twisted, out 2 on R/L, 0 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4c, parity odd.

Floors: count table 5 moves (3 qt), types 6, types + parity 6. Subset number of the placement: 3.

<details><summary>Answer</summary>

8 moves, 5 quarter turns (8 moves with NISS). Closer turns: R2, F'. One of 8 shortest ways: `R2 F' U R U2 F' R2 F`. The first shortest way to all good, `F' U R F' R2 F`, ends in a fake HTR, 9 from HTR.

</details>

**193.** `F' R' U2 R U R' U2 F`

Types `. . f + u . +`. 2 twisted, out 0 on R/L, 1 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 3 moves (3 qt), types 5, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: R, F'. One of 8 shortest ways: `R F2 U' R' F2 U F' R`. The first shortest way to all good, `R2 U2 R U R`, ends in a fake HTR, 9 from HTR.

</details>

**194.** `U' R U' F2 U' R U F2 R`

Types `f u f r u - f`. 1 twisted, out 1 on R/L, 2 on U/D, 3 on F/B. Out corners 6c, D-colour corners 4a, parity odd.

Floors: count table 5 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

9 moves, 5 quarter turns (7 moves with NISS). Closer turns: R', U, U2, U', F, F2, F'. One of 38 shortest ways: `R' F2 U' R' U F2 U R' U`. The first shortest way to all good, `R2 U R2 F R' F2 R`, ends in a fake HTR, 9 from HTR.

</details>

**195.** `F R U' R' F2 U F' U2 F R'`

Types `f + + r + . +`. 4 twisted, out 1 on R/L, 0 on U/D, 1 on F/B. Out corners 2c, D-colour corners 4c, parity even.

Floors: count table 4 moves (4 qt), types 7, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (7 moves with NISS). Closer turns: F'. One of 2 shortest ways: `F' R' U2 F R F R`. The first shortest way to all good, `R F' U2 R' F2 R F`, ends in a fake HTR, 9 from HTR.

</details>

**196.** `F U2 R F2 U' R F R'`

Types `+ u + + . . u`. 3 twisted, out 0 on R/L, 2 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4a, parity even.

Floors: count table 5 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 4.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (7 moves with NISS). Closer turns: R2. One of 2 shortest ways: `R2 F R F' U R U`. The first shortest way to all good, `U F2 U R' U F`, ends in a fake HTR, 9 from HTR.

</details>

**197.** `U' R U' R' U R F' R2`

Types `u f u f r r -`. 1 twisted, out 2 on R/L, 2 on U/D, 2 on F/B. Out corners 6c, D-colour corners 4b, parity odd.

Floors: count table 6 moves (5 qt), types 7, types + parity 7. Subset number of the placement: 3.

<details><summary>Answer</summary>

7 moves, 5 quarter turns (7 moves with NISS). Closer turns: R. One of 2 shortest ways: `R U' R2 U F2 R' U`. The first shortest way to all good, `R U F2 U' R2 F' U`, ends in a fake HTR, 9 from HTR.

</details>

**198.** `F' U' R2 U2 R' F' R2 F U'`

Types `- u u f - + r`. 3 twisted, out 1 on R/L, 2 on U/D, 1 on F/B. Out corners 4b, D-colour corners 4c, parity even.

Floors: count table 4 moves (3 qt), types 8, types + parity 8. Subset number of the placement: 2.

<details><summary>Answer</summary>

8 moves, 6 quarter turns (7 moves with NISS). Closer turns: U, U2. One of 6 shortest ways: `U R' F R U2 F2 U' R`. The first shortest way to all good, `R2 U' R' F' U R2 F' U`, ends in a fake HTR, 9 from HTR.

</details>

**199.** `F2 U2 R' U2 R' F' U F' U'`

Types `r + r u r . .`. 1 twisted, out 3 on R/L, 1 on U/D, 0 on F/B. Out corners 4b, D-colour corners 4b, parity even.

Floors: count table 5 moves (4 qt), types 5, types + parity 7. Subset number of the placement: 2.

<details><summary>Answer</summary>

7 moves, 6 quarter turns (7 moves with NISS). Closer turns: U. One of 2 shortest ways: `U F U' F R U2 R`. The first shortest way to all good, `U' F R' F' R`, ends in a fake HTR, 9 from HTR.

</details>

**200.** `U R2 F' U' F2 U' F R2 F' R'`

Types `. - + - u - r`. 4 twisted, out 1 on R/L, 1 on U/D, 0 on F/B. Out corners 2c, D-colour corners 4a, parity odd.

Floors: count table 4 moves (4 qt), types 6, types + parity 7. Subset number of the placement: 5.

<details><summary>Answer</summary>

9 moves, 5 quarter turns (8 moves with NISS). Closer turns: U, U', F, F2. One of 22 shortest ways: `U R' F2 U2 R' U R' U' R`. The first shortest way to all good, `U R U R' F' R`, ends in a fake HTR, 9 from HTR.

</details>

## 4. DR corner cases, in DR turns and with all turns

One or two cases per subset, scrambled with U, R2 and F2 only. Where leaving DR helps, the first row of the subset is a case where it helps most.

| Subset | Scramble | DR turns | A shortest way in DR turns | All turns | A shortest way | With NISS |
|---|---|---:|---|---:|---|---:|
| 0c3 | `R2 U' F2 U2 R2 U' F2 U2 R2 U' R2` | 10 | `R2 U R2 U2 F2 U R2 U2 F2 U` | 9 | `F R2 F2 U2 F R2 F2 U2 F` | 6 |
| 0c3 | `U R2 U2 F2 U' F2 U2 R2 U'` | 9 | `U R2 U2 F2 U R2 U2 F2 U` | 9 | `U R2 U2 F2 U R2 U2 F2 U` | 6 |
| 0c4 | `F2 U R2 U' R2 U2 F2 U' F2 U` | 9 | `U' R2 U R2 U2 F2 U R2 U` | 9 | `R' U2 R U2 R2 F2 R F2 R` | 6 |
| 2c3 | `U' R2 U' R2 U` | 5 | `U' R2 U R2 U` | 5 | `U' R2 U R2 U` | 4 |
| 2c4 | `F2 U' F2 U R2 U' F2 U F2` | 8 | `F2 U F2 U' R2 U R2 U` | 7 | `R U' R F2 R' U R` | 6 |
| 2c4 | `U R2 U F2 U' R2 U'` | 7 | `U R2 U F2 U' R2 U` | 7 | `U R2 U F2 U' R2 U` | 6 |
| 2c5 | `R2 U' R2 U F2 U' F2 U R2 U' R2` | 10 | `R2 U R2 U F2 U' R2 U F2 U` | 8 | `R F R' F2 R U' R U` | 7 |
| 4a1 | `U'` | 1 | `U` | 1 | `U` | 1 |
| 4a2 | `U' F2 U2 R2 U'` | 5 | `U R2 U2 F2 U` | 5 | `U R2 U2 F2 U` | 2 |
| 4a3 | `U R2 U R2 U2 F2 U'` | 7 | `U R2 U2 F2 U' F2 U` | 7 | `U R2 U2 F2 U' F2 U` | 4 |
| 4a4 | `U' R2 U F2 U' R2 U R2 U R2 U'` | 11 | `U R2 U' R2 U R2 U' R2 U F2 U` | 9 | `U R F' U F2 U' F R U` | 8 |
| 4a4 | `U F2 U R2 U2 F2 U' R2 U` | 9 | `U R2 U R2 U2 F2 U' R2 U` | 9 | `U R2 U R2 U2 F2 U' R2 U` | 6 |
| 4b2 | `U R2 U'` | 3 | `U R2 U` | 3 | `U R2 U` | 2 |
| 4b3 | `U R2 U2 F2 U' F2 U'` | 7 | `U F2 U R2 U2 F2 U` | 7 | `U F2 U R2 U2 F2 U` | 4 |
| 4b4 | `F2 U' F2 U F2 U' F2 U F2 U' R2 U'` | 10 | `R2 U' F2 U R2 U2 F2 U' R2 U` | 9 | `R' U' R' U' F2 U' R U R` | 8 |
| 4b4 | `U2 R2 U R2 U R2 U2 F2 U' R2 U` | 9 | `U' R2 U R2 U2 F2 U' F2 U` | 9 | `R U' R U R' F2 R' U' R` | 8 |
| 4b5 | `R2 U R2 U' R2 U F2 U' R2 U' R2` | 10 | `R2 U R2 U F2 U' R2 U R2 U` | 8 | `R' U F' R2 F R' F' U` | 7 |
