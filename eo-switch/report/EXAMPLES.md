# Worked examples: when to switch an EO

Examples to play along with the write-up ([WRITEUP.md](WRITEUP.md)). Do the EO and RZP, trace the inverse as the card says, decide, then open the answer.

These are 200 real attempts from the study's uniformly random scrambles: an EO and an RZP that reach the DRM at a total of 5 moves, so the target after the switch is a DR in 6 (sub-7). They're spread over the cells of the switch cards (more where the cards have more to say, 4c4e most) and picked at random within each cell. Nothing is hand-picked, so within each cell about as many reach a sub-7 as the cell's rate says.

**How to read it.**

- Every attempt is turned so that its EO is on F/B and its DR on U/D, the frame of the write-up: the scramble printed is the generated one with the faces renamed, which is the same scramble held in another orientation.
- An EO and RZP in brackets were found on the inverse scramble; the DR is then done on the other side, as usual with NISS.
- Colours are named by their home face (the *F/B colour* is the EO axis's colour, green or blue with green front).
- *Traced before switching* is what section 5 of the write-up reads on the side where the EO and RZP were done, from the cube after them: how many of the U/D-coloured edges in the E slice find a misoriented corner showing their colours on its side stickers (paired edges on the inverse), how many of them have an F/B-colour sticker (edge ARM on the inverse), the R/L stickers on the U/D faces (corner ARM on the inverse), the pairs and the side pairs.
- The answer gives the card's verdict with the sub-7 rate of that group (exact, every case once), the switched case, and one optimal DR on the inverse with the EO kept.

**Replay check.** Every move sequence on this page was replayed on the sticker model before the page was written: 2,600 checks (the turned scramble is the generated one after a rotation; EO + RZP solves the F/B EO and gives the stated DRM; the switched case is the attempt's; every value traced on normal equals the feature of the inverse; the DR solves the inverse to DR on U/D with the EO kept, in the table's optimal number of moves, and nissy 2.0.8 finds the same length), 0 mismatches.

**In these 200**, a DR in 6 or less exists after the switch in 33 of the 54 *switch*, 16 of the 64 *your call*, 5 of the 82 *discard* attempts.

## 4c4e

**4c4e, example 1.** `L2 R2 B' U2 F2 U2 L2 F' U2 B2 U2 R2 F B2 R2 U' B2 L B R U B L' D L'`

EO `(D2 F D' B)`, RZP `(R)`, on the inverse scramble: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 3 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 21, 3 pair(s) on 2 edge(s), 1 fake, 1 side pair(s), corners 4b-2.

Optimal DR on the normal side: `L2 U' F2 D2 R` (5 moves, sub-7). The whole attempt: `(D2 F D' B R) L2 U' F2 D2 R`, 10 moves to DR.

</details>

**4c4e, example 2.** `B2 D' L2 F2 U' F2 D2 B2 R2 D' L2 F2 U R2 U L' B2 U' B F2 L F2 R`

EO `R' F2 L' F2 B`, no RZP needed: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 3 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 31, 3 pair(s) on 2 edge(s), 0 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U2 B2 U' L2 U' L` (6 moves, sub-7). The whole attempt: `R' F2 L' F2 B (U2 B2 U' L2 U' L)`, 11 moves to DR.

</details>

**4c4e, example 3.** `B2 F2 L D2 R D2 R B2 D2 F2 U2 L U' R U B' L' D' L' R' U R'`

EO `F2 B2 R' U2 F'`, no RZP needed: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 3 (R/L stickers on U/D), 3 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 32, 3 pair(s) on 2 edge(s), 0 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U L2 D' B2 U R` (6 moves, sub-7). The whole attempt: `F2 B2 R' U2 F' (U L2 D' B2 U R)`, 11 moves to DR.

</details>

**4c4e, example 4.** `U2 L2 F R2 F D2 B D2 B' D2 R2 F' D2 U' R' F' L D R' U2 L2 U2`

EO `R' L F'`, RZP `D L'`: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 3 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 11, 3 pair(s) on 2 edge(s), 0 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U D F2 U L2 U' L` (7 moves, not sub-7). The whole attempt: `R' L F' D L' (U D F2 U L2 U' L)`, 12 moves to DR.

</details>

**4c4e, example 5.** `R2 D2 B2 D' B2 U' R2 F2 D' R2 F2 U' B2 R2 D' B' L' F' L D' U R B2 D'`

EO `L U' F L' B'`, no RZP needed: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 3 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 11, 3 pair(s) on 2 edge(s), 0 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U D' B2 U R2 U R` (7 moves, not sub-7). The whole attempt: `L U' F L' B' (U D' B2 U R2 U R)`, 12 moves to DR.

</details>

**4c4e, example 6.** `L2 U2 B2 U2 F2 R' F2 D2 R2 F2 R' D2 R B' L D' U2 R' D L U2 R'`

EO `U2 L D' R' F'`, no RZP needed: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 31, 2 pair(s) on 2 edge(s), 1 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U2 D' L2 B2 U R` (6 moves, sub-7). The whole attempt: `U2 L D' R' F' (U2 D' L2 B2 U R)`, 11 moves to DR.

</details>

**4c4e, example 7.** `D2 F D2 F' R2 B' L2 F2 R2 L2 F' R2 B' L' D' R2 L2 B' D L F2 U`

EO `(U' D L' U' F')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 21, 2 pair(s) on 2 edge(s), 2 fake, 0 side pair(s), corners 4b-2.

Optimal DR on the normal side: `R2 U' D' L2 D' L` (6 moves, sub-7). The whole attempt: `(U' D L' U' F') R2 U' D' L2 D' L`, 11 moves to DR.

</details>

**4c4e, example 8.** `F R2 B2 U2 L2 R2 B L2 F' U2 B R2 U2 L2 B' R' B' R' D L' F2 R D' B2`

EO `R U' D2 B'`, RZP `L`: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 10, 2 pair(s) on 2 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U L2 F2 U2 D R` (6 moves, sub-7). The whole attempt: `R U' D2 B' L (U L2 F2 U2 D R)`, 11 moves to DR.

</details>

**4c4e, example 9.** `F2 U2 R F2 D2 F2 U2 L' F2 L2 R D2 U' R D R2 D F R2 F R`

EO `R D2 B R2 B'`, no RZP needed: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 11, 2 pair(s) on 2 edge(s), 0 fake, 3 side pair(s), corners 4c-1.

Optimal DR on the inverse: `L U' R U2 L` (5 moves, sub-7). The whole attempt: `R D2 B R2 B' (L U' R U2 L)`, 10 moves to DR.

</details>

**4c4e, example 10.** `U2 R2 F L2 F R2 D2 F R2 F' L2 D2 B U2 F' R' D' R' L2 U B' R' F D F'`

EO `R2 B U' R F'`, no RZP needed: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 11, 2 pair(s) on 2 edge(s), 0 fake, 2 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U R' B2 R D2 R U2 L` (8 moves, not sub-7). The whole attempt: `R2 B U' R F' (U R' B2 R D2 R U2 L)`, 13 moves to DR.

</details>

**4c4e, example 11.** `D2 R D2 F2 U2 R' F2 L2 B2 F2 L B2 R2 D' L2 R F L R F R2 D`

EO `(F2 D2 R B')`, RZP `(L)`, on the inverse scramble: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 11, 2 pair(s) on 2 edge(s), 0 fake, 2 side pair(s), corners 4c-1.

Optimal DR on the normal side: `L' B2 D' R' U D' R` (7 moves, not sub-7). The whole attempt: `(F2 D2 R B' L) L' B2 D' R' U D' R`, 12 moves to DR.

</details>

**4c4e, example 12.** `U2 R2 F' B2 L2 B' U2 F L2 B' L2 D2 L2 R2 U' L F2 D' U R U' F`

EO `(L2 B L F')`, RZP `(R')`, on the inverse scramble: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 3 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 11, 3 pair(s) on 2 edge(s), 1 fake, 2 side pair(s), corners 4c-1.

Optimal DR on the normal side: `U L2 D' F2 D2 L` (6 moves, sub-7). The whole attempt: `(L2 B L F' R') U L2 D' F2 D2 L`, 11 moves to DR.

</details>

**4c4e, example 13.** `B2 L2 D2 B2 L F2 D2 L' U2 L U2 B2 L F2 R D' F' L' B2 U L2 B L2 F L'`

EO `(B D2 F)`, RZP `(U' L)`, on the inverse scramble: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 2 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 22, 2 pair(s) on 2 edge(s), 0 fake, 0 side pair(s), corners 4a-2.

Optimal DR on the normal side: `U D2 R2 U2 F2 D' R` (7 moves, not sub-7). The whole attempt: `(B D2 F U' L) U D2 R2 U2 F2 D' R`, 12 moves to DR.

</details>

**4c4e, example 14.** `L2 D2 F2 U B2 R2 U B2 F2 D R2 U2 R2 R' F' U B U2 L' F' R' B'`

EO `(L' F B)`, RZP `(U R)`, on the inverse scramble: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 11, 2 pair(s) on 2 edge(s), 0 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `U2 F2 U' F2 R2 D' L` (7 moves, not sub-7). The whole attempt: `(L' F B U R) U2 F2 U' F2 R2 D' L`, 12 moves to DR.

</details>

**4c4e, example 15.** `U2 F2 U2 B2 L2 B2 L2 R' B2 L' B2 D2 L' B' U' F2 L D2 B' U F' L2 R2`

EO `D2 F' D' R2 B'`, no RZP needed: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 21, 2 pair(s) on 2 edge(s), 1 fake, 0 side pair(s), corners 4a-2.

Optimal DR on the inverse: `U F2 U2 L2 U L` (6 moves, sub-7). The whole attempt: `D2 F' D' R2 B' (U F2 U2 L2 U L)`, 11 moves to DR.

</details>

**4c4e, example 16.** `U2 L D2 F2 D2 U2 R' U2 R2 B2 R B2 R F2 L' U' R F D' B2 R' B' R' U R2`

EO `(D2 R' B' U' F')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (both bad U/D edges paired: 15.5% of 4c4e, 59.9% sub-7).

Switched case: 4c4e, ARM 11, 2 pair(s) on 2 edge(s), 1 fake, 2 side pair(s), corners 4c-1.

Optimal DR on the normal side: `U L2 D' R2 D R` (6 moves, sub-7). The whole attempt: `(D2 R' B' U' F') U L2 D' R2 D R`, 11 moves to DR.

</details>

**4c4e, example 17.** `L2 D2 F2 U B2 R2 U B2 F2 D R2 U2 R2 R' F' U B U2 L' F' R' B'`

EO `(L' F B)`, RZP `(R L)`, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 2 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 21, 2 pair(s) on 1 edge(s), 0 fake, 2 side pair(s), corners 4b-2.

Optimal DR on the normal side: `L2 U2 L2 U R` (5 moves, sub-7). The whole attempt: `(L' F B R L) L2 U2 L2 U R`, 10 moves to DR.

</details>

**4c4e, example 18.** `U2 R' B2 R D2 L' U2 L U2 F2 U2 B2 R' D2 R2 U' F R D' L U' D2 R2 F U R'`

EO `(L2 U L F' B')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 2 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 21, 2 pair(s) on 1 edge(s), 0 fake, 2 side pair(s), corners 4b-2.

Optimal DR on the normal side: `F2 B2 U2 B2 D' R` (6 moves, sub-7). The whole attempt: `(L2 U L F' B') F2 B2 U2 B2 D' R`, 11 moves to DR.

</details>

**4c4e, example 19.** `L2 D2 B' F2 U2 F' L2 B U2 F' U2 R2 U2 D2 L' U B2 R' L D L' B`

EO `(D2 L2 B U F)`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 21, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4b-2.

Optimal DR on the normal side: `U2 L2 F2 U D F2 U R` (8 moves, not sub-7). The whole attempt: `(D2 L2 B U F) U2 L2 F2 U D F2 U R`, 13 moves to DR.

</details>

**4c4e, example 20.** `U2 R F2 L B2 U2 L D2 R D2 L2 B2 R' B' D' B' R' F' L' D R2 D' B'`

EO `(L' F R' U' B')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 21, 1 pair(s) on 1 edge(s), 1 fake, 2 side pair(s), corners 4b-2.

Optimal DR on the normal side: `U' R2 U' F2 D' B2 R` (7 moves, not sub-7). The whole attempt: `(L' F R' U' B') U' R2 U' F2 D' B2 R`, 12 moves to DR.

</details>

**4c4e, example 21.** `R2 L2 D F2 U F2 U R2 F2 L2 B2 D B' U B R' D' F' D' U' B U'`

EO `(B D2 F L2 B')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 31, 2 pair(s) on 1 edge(s), 1 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the normal side: `B2 U2 B2 D B2 D' R` (7 moves, not sub-7). The whole attempt: `(B D2 F L2 B') B2 U2 B2 D B2 D' R`, 12 moves to DR.

</details>

**4c4e, example 22.** `D2 B' R2 D2 B R2 B D2 B' D2 B U2 F' R2 R' B D B2 U' R F D F B2`

EO `L' U2 D2 F'`, RZP `L'`: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 4 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 41, 2 pair(s) on 1 edge(s), 2 fake, 0 side pair(s), corners 4a-4.

Optimal DR on the inverse: `B2 U F2 B2 U L` (6 moves, sub-7). The whole attempt: `L' U2 D2 F' L' (B2 U F2 B2 U L)`, 11 moves to DR.

</details>

**4c4e, example 23.** `L2 F2 U R2 U' B2 D U2 F2 R2 U B2 F2 U' F' L' B2 F2 U' L D2 L' D U2`

EO `(U2 R L2 D B')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 21, 1 pair(s) on 1 edge(s), 1 fake, 0 side pair(s), corners 4a-2.

Optimal DR on the normal side: `U F2 U2 B2 U' F2 L` (7 moves, not sub-7). The whole attempt: `(U2 R L2 D B') U F2 U2 B2 U' F2 L`, 12 moves to DR.

</details>

**4c4e, example 24.** `U2 R2 D' F2 R2 U2 R2 U' B2 R2 U2 R2 U F2 U' F' D F2 L2 U' R D F2 R'`

EO `(D L2 U2 D2 B')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 31, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the normal side: `D R2 U2 L' D F2 U L` (8 moves, not sub-7). The whole attempt: `(D L2 U2 D2 B') D R2 U2 L' D F2 U L`, 13 moves to DR.

</details>

**4c4e, example 25.** `D R2 D2 R2 F2 D R2 D L2 F2 R2 U' R2 U' F2 L' U2 L2 B F2 L' F R' L'`

EO `B' R F L' B`, no RZP needed: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 11, 1 pair(s) on 1 edge(s), 3 fake, 2 side pair(s), corners 4c-1.

Optimal DR on the inverse: `R2 L' U' F2 L U L` (7 moves, not sub-7). The whole attempt: `B' R F L' B (R2 L' U' F2 L U L)`, 12 moves to DR.

</details>

**4c4e, example 26.** `R2 U R2 F2 L2 U' F2 D2 B2 F2 D B2 U2 R' D2 U F D U F U2 R`

EO `(B' D2 R2 U' F')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 31, 1 pair(s) on 1 edge(s), 2 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `U D' L2 D' R2 F2 D' L` (8 moves, not sub-7). The whole attempt: `(B' D2 R2 U' F') U D' L2 D' R2 F2 D' L`, 13 moves to DR.

</details>

**4c4e, example 27.** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `L B`, RZP `U D2 L`: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 11, 2 pair(s) on 1 edge(s), 0 fake, 2 side pair(s), corners 4c-1.

Optimal DR on the inverse: `F2 R2 U' F2 L2 D R` (7 moves, not sub-7). The whole attempt: `L B U D2 L (F2 R2 U' F2 L2 D R)`, 12 moves to DR.

</details>

**4c4e, example 28.** `L2 D R2 F2 R2 L2 U' L2 U2 B2 U B2 U F2 D' L' U F R' B2 U' B' U' L U2`

EO `R' F' U' L B`, no RZP needed: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 21, 1 pair(s) on 1 edge(s), 2 fake, 1 side pair(s), corners 4a-2.

Optimal DR on the inverse: `L U2 B2 R' F2 D R` (7 moves, not sub-7). The whole attempt: `R' F' U' L B (L U2 B2 R' F2 D R)`, 12 moves to DR.

</details>

**4c4e, example 29.** `L2 U' B2 U' R2 D' B2 F2 D2 R2 F2 U B2 L2 R' D L' B F' U L' D2 F'`

EO `U' B' R F'`, RZP `L'`: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 21, 1 pair(s) on 1 edge(s), 2 fake, 1 side pair(s), corners 4a-2.

Optimal DR on the inverse: `R' D2 L F2 R D' L` (7 moves, not sub-7). The whole attempt: `U' B' R F' L' (R' D2 L F2 R D' L)`, 12 moves to DR.

</details>

**4c4e, example 30.** `L2 U2 B D2 B R2 F R2 F' R2 D2 B' R2 L' D' B' U R D' L2 U2 L2`

EO `(R U2 L' U B)`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 11, 2 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `D2 L U R U' L` (6 moves, sub-7). The whole attempt: `(R U2 L' U B) D2 L U R U' L`, 11 moves to DR.

</details>

**4c4e, example 31.** `D2 F2 R' F2 R U2 L F2 L' R2 U2 B' D R F' U2 B' U D' L B`

EO `(F' B D' L F)`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 11, 1 pair(s) on 1 edge(s), 1 fake, 2 side pair(s), corners 4c-1.

Optimal DR on the normal side: `D L' U' B2 U F2 R` (7 moves, not sub-7). The whole attempt: `(F' B D' L F) D L' U' B2 U F2 R`, 12 moves to DR.

</details>

**4c4e, example 32.** `R D2 R' F2 R B2 U2 R' U2 R F2 L B' R' D L' U L' D2 B D2 L`

EO `(D2 B R D F)`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 31, 1 pair(s) on 1 edge(s), 1 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the normal side: `U2 F2 L2 D F2 R2 D' L` (8 moves, not sub-7). The whole attempt: `(D2 B R D F) U2 F2 L2 D F2 R2 D' L`, 13 moves to DR.

</details>

**4c4e, example 33.** `U' L2 U' R2 D L2 D' F2 D L2 U L2 U' B2 U' L' B' D U2 R U B' L' D'`

EO `B' R2 U F'`, RZP `L`: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 31, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the inverse: `F2 D R2 D F2 U' L` (7 moves, not sub-7). The whole attempt: `B' R2 U F' L (F2 D R2 D F2 U' L)`, 12 moves to DR.

</details>

**4c4e, example 34.** `B2 L2 U2 F L2 F' L2 B' R2 B R2 U2 R' D2 B D2 F L U' L' D'`

EO `(D2 F' R' L' F)`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 21, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4b-2.

Optimal DR on the normal side: `U2 R2 F2 U2 B2 U R` (7 moves, not sub-7). The whole attempt: `(D2 F' R' L' F) U2 R2 F2 U2 B2 U R`, 12 moves to DR.

</details>

**4c4e, example 35.** `B2 D2 R2 B2 D F2 R2 D' L2 D L2 B2 D F2 U R' F' D' B2 L D2 B D2 F D'`

EO `(F D2 B)`, RZP `(D R)`, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 0 (R/L stickers on U/D), 2 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 01, 2 pair(s) on 1 edge(s), 1 fake, 3 side pair(s), corners 4b-0.

Optimal DR on the normal side: `U R2 U2 L2 D' B2 U R` (8 moves, not sub-7). The whole attempt: `(F D2 B D R) U R2 U2 L2 D' B2 U R`, 13 moves to DR.

</details>

**4c4e, example 36.** `U2 F2 U2 B2 L2 B2 L2 R' B2 L' B2 D2 L' B' U' F2 L D2 B' U F' L2 R2`

EO `L2 D F' R2 B`, no RZP needed: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (one paired, edge ARM 1: 32.5% of 4c4e, 20.0% sub-7).

Switched case: 4c4e, ARM 21, 1 pair(s) on 1 edge(s), 0 fake, 1 side pair(s), corners 4a-2.

Optimal DR on the inverse: `R2 U' L2 U B2 L` (6 moves, sub-7). The whole attempt: `L2 D F' R2 B (R2 U' L2 U B2 L)`, 11 moves to DR.

</details>

**4c4e, example 37.** `B D2 F2 L2 U2 D2 F U2 B' L2 F D2 L2 U2 F' D' F' D' R U' B2 D R' F2`

EO `(D L F2 L2 B)`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 31, 0 pair(s) on 0 edge(s), 2 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `L2 B2 D F2 D L2 U' L` (8 moves, not sub-7). The whole attempt: `(D L F2 L2 B) L2 B2 D F2 D L2 U' L`, 13 moves to DR.

</details>

**4c4e, example 38.** `U2 R2 D' F2 R2 U2 R2 U' B2 R2 U2 R2 U F2 U' F' D F2 L2 U' R D F2 R'`

EO `(R' D' R' D2 F')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 21, 0 pair(s) on 0 edge(s), 2 fake, 0 side pair(s), corners 4a-2.

Optimal DR on the normal side: `U' R D' L' U' R' U' L` (8 moves, not sub-7). The whole attempt: `(R' D' R' D2 F') U' R D' L' U' R' U' L`, 13 moves to DR.

</details>

**4c4e, example 39.** `D2 L2 B' R2 B2 D2 B' U2 F D2 B2 F' L2 U' D' F' R' U L F' U'`

EO `R F L' D F'`, no RZP needed: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (one paired, edge ARM 0 or 2: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 12, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U R F2 L2 U2 D L` (7 moves, not sub-7). The whole attempt: `R F L' D F' (U R F2 L2 U2 D L)`, 12 moves to DR.

</details>

**4c4e, example 40.** `U2 R2 F D2 F' R2 B L2 U2 F D2 B' R2 B' L2 R' U' F D' F U' F L2 F2 B2`

EO `U F' L' D2 B`, no RZP needed: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 11, 0 pair(s) on 0 edge(s), 0 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U' L2 U F2 U2 F2 B2 L` (8 moves, not sub-7). The whole attempt: `U F' L' D2 B (U' L2 U F2 U2 F2 B2 L)`, 13 moves to DR.

</details>

**4c4e, example 41.** `L2 B R2 D2 R2 L2 F' L2 F2 U2 F U2 F D2 B' L' F D R' U2 F' U' F' L F2`

EO `(R U' F')`, RZP `(U L)`, on the inverse scramble: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 31, 0 pair(s) on 0 edge(s), 3 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `L' D L' D' R D' R` (7 moves, not sub-7). The whole attempt: `(R U' F' U L) L' D L' D' R D' R`, 12 moves to DR.

</details>

**4c4e, example 42.** `F2 U F2 U' R2 D' L2 U2 R2 L2 U' R2 D' L' F' R2 L2 D' F L U2 B`

EO `(F' U F2 U2 F)`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (one paired, edge ARM 0 or 2: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 10, 1 pair(s) on 1 edge(s), 0 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `U2 B2 R2 D' F2 D L` (7 moves, not sub-7). The whole attempt: `(F' U F2 U2 F) U2 B2 R2 D' F2 D L`, 12 moves to DR.

</details>

**4c4e, example 43.** `F2 R2 U L2 D2 F2 U R2 U' R2 U B2 R2 R' B D B R' D B' R' F' D'`

EO `(F L F' D B')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 21, 0 pair(s) on 0 edge(s), 2 fake, 2 side pair(s), corners 4d-2.

Optimal DR on the normal side: `R2 L2 F2 B2 D F2 R` (7 moves, not sub-7). The whole attempt: `(F L F' D B') R2 L2 F2 B2 D F2 R`, 12 moves to DR.

</details>

**4c4e, example 44.** `D2 F2 L2 F2 R2 U' R2 B2 U2 R2 U' B2 U L' D B' F2 U' B D F2 U'`

EO `B' L2 U2 L2 B'`, no RZP needed: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 10, 0 pair(s) on 0 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U' L' U R2 U2 F2 B2 R` (8 moves, not sub-7). The whole attempt: `B' L2 U2 L2 B' (U' L' U R2 U2 F2 B2 R)`, 13 moves to DR.

</details>

**4c4e, example 45.** `L2 U' B2 U R2 D' L2 D L2 F2 L2 B2 U' R2 U2 L' F U R' D L' R2 U2 F L U'`

EO `(L D F' B)`, RZP `(L')`, on the inverse scramble: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 21, 0 pair(s) on 0 edge(s), 0 fake, 2 side pair(s), corners 4b-2.

Optimal DR on the normal side: `D2 L2 D' F2 B2 L` (6 moves, sub-7). The whole attempt: `(L D F' B L') D2 L2 D' F2 B2 L`, 11 moves to DR.

</details>

**4c4e, example 46.** `B2 D' L2 F2 U' F2 D2 B2 R2 D' L2 F2 U R2 U L' B2 U' B F2 L F2 R`

EO `U' R D2 L F'`, no RZP needed: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 0, corner ARM 3 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 30, 0 pair(s) on 0 edge(s), 2 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U2 F2 D R2 D' R2 B2 L` (8 moves, not sub-7). The whole attempt: `U' R D2 L F' (U2 F2 D R2 D' R2 B2 L)`, 13 moves to DR.

</details>

**4c4e, example 47.** `U2 L2 F2 R B2 D2 R B2 F2 L D2 R2 D2 D' F' R B R2 U' F' D' B'`

EO `(U F B)`, RZP `(D R)`, on the inverse scramble: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 21, 0 pair(s) on 0 edge(s), 2 fake, 1 side pair(s), corners 4a-2.

Optimal DR on the normal side: `U L2 F2 B2 D F2 R` (7 moves, not sub-7). The whole attempt: `(U F B D R) U L2 F2 B2 D F2 R`, 12 moves to DR.

</details>

**4c4e, example 48.** `L2 F2 L2 B2 D2 B2 D2 U' B2 D' B2 R2 D' B' L' F2 D R2 B' L F' D2 U2`

EO `F B R D2 B`, no RZP needed: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 21, 0 pair(s) on 0 edge(s), 1 fake, 2 side pair(s), corners 4a-2.

Optimal DR on the inverse: `D R' L2 D F2 L' D' R` (8 moves, not sub-7). The whole attempt: `F B R D2 B (D R' L2 D F2 L' D' R)`, 13 moves to DR.

</details>

**4c4e, example 49.** `U2 R2 F' B2 L2 B' U2 F L2 B' L2 D2 L2 R2 U' L F2 D' U R U' F`

EO `(D2 F' D L B')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (one paired, edge ARM 0 or 2: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 10, 1 pair(s) on 1 edge(s), 0 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `F2 R2 D' F2 U2 D L` (7 moves, not sub-7). The whole attempt: `(D2 F' D L B') F2 R2 D' F2 U2 D L`, 12 moves to DR.

</details>

**4c4e, example 50.** `B2 U' L2 U2 B2 R2 L2 U' F2 U2 R2 U' L2 F2 U' L' B' U' R L' U2 F' U L'`

EO `(R' B' U' D F)`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (one paired, edge ARM 0 or 2: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 20, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4b-2.

Optimal DR on the normal side: `D2 R' B2 U' R U' R` (7 moves, not sub-7). The whole attempt: `(R' B' U' D F) D2 R' B2 U' R U' R`, 12 moves to DR.

</details>

**4c4e, example 51.** `R2 F' D2 R2 F D2 F R2 F' R2 F L2 B' D2 D' F R F2 L' D B R B F2`

EO `D2 R U R2 F`, no RZP needed: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (one paired, edge ARM 0 or 2: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 10, 1 pair(s) on 1 edge(s), 1 fake, 2 side pair(s), corners 4c-1.

Optimal DR on the inverse: `D R B2 U R2 L2 D R` (8 moves, not sub-7). The whole attempt: `D2 R U R2 F (D R B2 U R2 L2 D R)`, 13 moves to DR.

</details>

**4c4e, example 52.** `L2 B U2 F D2 L2 F R2 B R2 F2 D2 B' D' R' D' B' U' F' R B2 R' D'`

EO `(R2 F L U' B')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (one paired, edge ARM 0 or 2: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 22, 1 pair(s) on 1 edge(s), 2 fake, 0 side pair(s), corners 4b-2.

Optimal DR on the normal side: `D' B2 D' L2 D' R2 D R` (8 moves, not sub-7). The whole attempt: `(R2 F L U' B') D' B2 D' L2 D' R2 D R`, 13 moves to DR.

</details>

**4c4e, example 53.** `R2 U R2 F2 L2 U' F2 D2 B2 F2 D B2 U2 R' D2 U F D U F U2 R`

EO `(U' D2 F2 L2 F')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 0 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 11, 0 pair(s) on 0 edge(s), 3 fake, 2 side pair(s), corners 4c-1.

Optimal DR on the normal side: `U2 L D R' U' B2 U' R` (8 moves, not sub-7). The whole attempt: `(U' D2 F2 L2 F') U2 L D R' U' B2 U' R`, 13 moves to DR.

</details>

**4c4e, example 54.** `U2 R' B2 R' D2 L' B2 F2 L2 D2 F2 R B2 U2 D' L U' B F' R U' L2 F'`

EO `R2 D' R' F' B`, no RZP needed: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 31, 0 pair(s) on 0 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `R2 L2 D B2 U F2 B2 R` (8 moves, not sub-7). The whole attempt: `R2 D' R' F' B (R2 L2 D B2 U F2 B2 R)`, 13 moves to DR.

</details>

**4c4e, example 55.** `D R2 D2 R2 F2 D R2 D L2 F2 R2 U' R2 U' F2 L' U2 L2 B F2 L' F R' L'`

EO `R' F' L' F2 B`, no RZP needed: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (one paired, edge ARM 0 or 2: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 20, 1 pair(s) on 1 edge(s), 1 fake, 2 side pair(s), corners 4a-2.

Optimal DR on the inverse: `R U2 B2 R U' R U' R` (8 moves, not sub-7). The whole attempt: `R' F' L' F2 B (R U2 B2 R U' R U' R)`, 13 moves to DR.

</details>

**4c4e, example 56.** `B2 U2 R F2 R' D2 L R2 U2 F2 R D2 U2 R' U' B' D2 U2 R' B L2 B' L R2`

EO `L' F R' D2 B'`, no RZP needed: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 0, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 20, 0 pair(s) on 0 edge(s), 2 fake, 1 side pair(s), corners 4a-2.

Optimal DR on the inverse: `U2 B2 U' F2 R' U2 F2 L` (8 moves, not sub-7). The whole attempt: `L' F R' D2 B' (U2 B2 U' F2 R' U2 F2 L)`, 13 moves to DR.

</details>

**4c4e, example 57.** `L' B2 R' F2 R B2 U2 R F2 L' B2 R B2 R D' B F' L' F' U' B' D2 F2`

EO `B' L' D R' B`, no RZP needed: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (one paired, edge ARM 0 or 2: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 22, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4a-2.

Optimal DR on the inverse: `D2 F2 D' R' B2 L2 U' R` (8 moves, not sub-7). The whole attempt: `B' L' D R' B (D2 F2 D' R' B2 L2 U' R)`, 13 moves to DR.

</details>

**4c4e, example 58.** `L2 U2 B D2 B R2 F R2 F' R2 D2 B' R2 L' D' B' U R D' L2 U2 L2`

EO `U D' B`, RZP `R' L`: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 21, 0 pair(s) on 0 edge(s), 0 fake, 0 side pair(s), corners 4b-2.

Optimal DR on the inverse: `U2 R2 L2 B2 L2 F2 D' R` (8 moves, not sub-7). The whole attempt: `U D' B R' L (U2 R2 L2 B2 L2 F2 D' R)`, 13 moves to DR.

</details>

**4c4e, example 59.** `L2 U2 B2 R U2 R' U2 L' D2 L D2 B2 D' F2 L F2 R U B' U' F'`

EO `R2 D2 F' U B`, no RZP needed: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 2 (R/L stickers on U/D), 2 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (one paired, edge ARM 0 or 2: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 22, 2 pair(s) on 1 edge(s), 1 fake, 2 side pair(s), corners 4b-2.

Optimal DR on the inverse: `F2 U' L' D L' D R` (7 moves, not sub-7). The whole attempt: `R2 D2 F' U B (F2 U' L' D L' D R)`, 12 moves to DR.

</details>

**4c4e, example 60.** `B2 F2 L D2 R D2 R B2 D2 F2 U2 L U' R U B' L' D' L' R' U R'`

EO `L' U2 R2 L' B'`, no RZP needed: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (one paired, edge ARM 0 or 2: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 32, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `D' F2 R2 L2 D R` (6 moves, sub-7). The whole attempt: `L' U2 R2 L' B' (D' F2 R2 L2 D R)`, 11 moves to DR.

</details>

**4c4e, example 61.** `D2 F2 R' F2 R U2 L F2 L' R2 U2 B' D R F' U2 B' U D' L B`

EO `(F' B L D' F')`, no RZP needed, on the inverse scramble: 4c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (one paired, edge ARM 0 or 2: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 12, 1 pair(s) on 1 edge(s), 1 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the normal side: `U' L2 D2 B2 U F2 D R` (8 moves, not sub-7). The whole attempt: `(F' B L D' F') U' L2 D2 B2 U F2 D R`, 13 moves to DR.

</details>

**4c4e, example 62.** `R2 B2 D2 R2 B L2 D2 B' U2 B U2 R2 B L2 F D' L' B' R2 U B2 R B2 L B'`

EO `B' D L' U B`, no RZP needed: 4c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 0, corner ARM 3 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no bad edge paired: 52.0% of 4c4e, 6.7% sub-7).

Switched case: 4c4e, ARM 30, 0 pair(s) on 0 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U2 R2 D' B2 D' F2 B2 L` (8 moves, not sub-7). The whole attempt: `B' D L' U B (U2 R2 D' B2 D' F2 B2 L)`, 13 moves to DR.

</details>

## 4c2e

**4c2e, example 1.** `L D2 L2 D2 F2 L D2 L U2 F2 D2 R' D2 R' F2 U' R2 U2 B F2 U' F D' U'`

EO `(B D' F' U' B)`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (pairs + side pairs/2 is 1.5 or more: 22.3% of 4c2e, 57.0% sub-7).

Switched case: 4c2e, ARM 21, 1 pair(s) on 1 edge(s), 1 fake, 2 side pair(s), corners 4a-2.

Optimal DR on the normal side: `R U2 L2 U R` (5 moves, sub-7). The whole attempt: `(B D' F' U' B) R U2 L2 U R`, 10 moves to DR.

</details>

**4c2e, example 2.** `F2 R F2 R' D2 L' U2 R2 D2 U2 R' D2 L' U' F' D2 U2 L' F U R2 B`

EO `(F R' F2 R2 F')`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (pairs + side pairs/2 is 1.5 or more: 22.3% of 4c2e, 57.0% sub-7).

Switched case: 4c2e, ARM 31, 2 pair(s) on 1 edge(s), 0 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `F2 U' R' U2 R` (5 moves, sub-7). The whole attempt: `(F R' F2 R2 F') F2 U' R' U2 R`, 10 moves to DR.

</details>

**4c2e, example 3.** `U2 R2 F' B2 L2 B' U2 F L2 B' L2 D2 L2 R2 U' L F2 D' U R U' F`

EO `(R2 F L B')`, RZP `(R)`, on the inverse scramble: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (pairs + side pairs/2 is 1.5 or more: 22.3% of 4c2e, 57.0% sub-7).

Switched case: 4c2e, ARM 10, 2 pair(s) on 1 edge(s), 0 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `R2 U D2 R F2 R` (6 moves, sub-7). The whole attempt: `(R2 F L B' R) R2 U D2 R F2 R`, 11 moves to DR.

</details>

**4c2e, example 4.** `B2 F2 R' U2 L2 U2 B2 L' U2 R2 U2 F2 L R2 F2 U' R2 B R F U R B' D B'`

EO `(R' L F' U' B)`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (pairs + side pairs/2 is 1.5 or more: 22.3% of 4c2e, 57.0% sub-7).

Switched case: 4c2e, ARM 10, 1 pair(s) on 1 edge(s), 0 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `R D L2 F2 D' R` (6 moves, sub-7). The whole attempt: `(R' L F' U' B) R D L2 F2 D' R`, 11 moves to DR.

</details>

**4c2e, example 5.** `U2 R2 F D2 F' R2 B L2 U2 F D2 B' R2 B' L2 R' U' F D' F U' F L2 F2 B2`

EO `L F B U' B'`, no RZP needed: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 4 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (pairs + side pairs/2 is 1.5 or more: 22.3% of 4c2e, 57.0% sub-7).

Switched case: 4c2e, ARM 41, 2 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4a-4.

Optimal DR on the inverse: `U D R' F2 B2 R B2 R` (8 moves, not sub-7). The whole attempt: `L F B U' B' (U D R' F2 B2 R B2 R)`, 13 moves to DR.

</details>

**4c2e, example 6.** `F2 U2 L2 U2 R2 B' R2 D2 B2 R2 B' D2 B L' F D' U2 B' D F U2 B'`

EO `(F2 L' F R2 B')`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (pairs + side pairs/2 is 1.5 or more: 22.3% of 4c2e, 57.0% sub-7).

Switched case: 4c2e, ARM 31, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `L2 U R' F2 R` (5 moves, sub-7). The whole attempt: `(F2 L' F R2 B') L2 U R' F2 R`, 10 moves to DR.

</details>

**4c2e, example 7.** `L' D2 R' U2 R D2 B2 R U2 L' D2 R D2 R F' D U' L' U' B' D' F2 U2`

EO `F D R' B'`, RZP `L`: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (pairs + side pairs/2 is 1.5 or more: 22.3% of 4c2e, 57.0% sub-7).

Switched case: 4c2e, ARM 10, 2 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U2 R2 U' R' D2 R` (6 moves, sub-7). The whole attempt: `F D R' B' L (U2 R2 U' R' D2 R)`, 11 moves to DR.

</details>

**4c2e, example 8.** `F2 U F2 L2 B2 U' L2 D2 R2 L2 D R2 U2 F' D2 U L D U L U2 F`

EO `R U' R D' B`, no RZP needed: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 4 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (pairs + side pairs/2 is 1.5 or more: 22.3% of 4c2e, 57.0% sub-7).

Switched case: 4c2e, ARM 41, 2 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4b-0.

Optimal DR on the inverse: `U D R B2 R` (5 moves, sub-7). The whole attempt: `R U' R D' B (U D R B2 R)`, 10 moves to DR.

</details>

**4c2e, example 9.** `B D2 F2 L2 U2 D2 F U2 B' L2 F D2 L2 U2 F' D' F' D' R U' B2 D R' F2`

EO `U2 L B`, RZP `U R`: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (pairs + side pairs/2 is 1.5 or more: 22.3% of 4c2e, 57.0% sub-7).

Switched case: 4c2e, ARM 20, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4a-2.

Optimal DR on the inverse: `D' L2 D' B2 R F2 R` (7 moves, not sub-7). The whole attempt: `U2 L B U R (D' L2 D' B2 R F2 R)`, 12 moves to DR.

</details>

**4c2e, example 10.** `D2 F2 L2 U F2 U' F2 D' B2 D B2 L2 B' R2 D R2 U F L' F' R'`

EO `(R' L U' R2 F')`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 0 (R/L stickers on U/D), 2 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (pairs + side pairs/2 is 1.5 or more: 22.3% of 4c2e, 57.0% sub-7).

Switched case: 4c2e, ARM 00, 2 pair(s) on 1 edge(s), 0 fake, 2 side pair(s), corners 4b-0, JZP.

Optimal DR on the normal side: `R' F2 R` (3 moves, sub-7). The whole attempt: `(R' L U' R2 F') R' F2 R`, 8 moves to DR.

</details>

**4c2e, example 11.** `F' R2 F' D2 B2 U2 R2 B' U2 F' U2 L2 U2 F' L' D F' L2 U F' D' R D`

EO `F' B2 U L' B'`, no RZP needed: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (pairs + side pairs/2 is exactly 1: 24.6% of 4c2e, 15.7% sub-7).

Switched case: 4c2e, ARM 10, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the inverse: `L D' F2 R2 U2 D' R` (7 moves, not sub-7). The whole attempt: `F' B2 U L' B' (L D' F2 R2 U2 D' R)`, 12 moves to DR.

</details>

**4c2e, example 12.** `R2 B R2 B' D2 F' U2 B2 D2 U2 B' D2 F' U' R' D2 U2 F' R U B2 L`

EO `(F2 B R L2 B)`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (pairs + side pairs/2 is exactly 1: 24.6% of 4c2e, 15.7% sub-7).

Switched case: 4c2e, ARM 21, 0 pair(s) on 0 edge(s), 1 fake, 2 side pair(s), corners 4b-2.

Optimal DR on the normal side: `R D2 R' F2 R' U' R` (7 moves, not sub-7). The whole attempt: `(F2 B R L2 B) R D2 R' F2 R' U' R`, 12 moves to DR.

</details>

**4c2e, example 13.** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `L B`, RZP `R U' R'`: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (pairs + side pairs/2 is exactly 1: 24.6% of 4c2e, 15.7% sub-7).

Switched case: 4c2e, ARM 21, 1 pair(s) on 1 edge(s), 1 fake, 0 side pair(s), corners 4b-2.

Optimal DR on the inverse: `D R' D2 R' B2 U L` (7 moves, not sub-7). The whole attempt: `L B R U' R' (D R' D2 R' B2 U L)`, 12 moves to DR.

</details>

**4c2e, example 14.** `L2 F2 U2 F2 D2 R' D2 B2 R2 D2 R' B2 R U' L B' F2 R' B L F2 R'`

EO `F' U2 F`, RZP `D2 R'`: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (pairs + side pairs/2 is exactly 1: 24.6% of 4c2e, 15.7% sub-7).

Switched case: 4c2e, ARM 31, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U R U L F2 L' U R` (8 moves, not sub-7). The whole attempt: `F' U2 F D2 R' (U R U L F2 L' U R)`, 13 moves to DR.

</details>

**4c2e, example 15.** `B2 R' D2 B2 R D2 R B2 R' B2 R F2 L' D2 D' R B R2 F' D L B L R2`

EO `(B' R2 F)`, RZP `(U R')`, on the inverse scramble: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 4 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (pairs + side pairs/2 is exactly 1: 24.6% of 4c2e, 15.7% sub-7).

Switched case: 4c2e, ARM 41, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4a-4.

Optimal DR on the normal side: `U' L' D L B2 D R` (7 moves, not sub-7). The whole attempt: `(B' R2 F U R') U' L' D L B2 D R`, 12 moves to DR.

</details>

**4c2e, example 16.** `L2 U2 B D2 B R2 F R2 F' R2 D2 B' R2 L' D' B' U R D' L2 U2 L2`

EO `B' U D' B'`, RZP `L`: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (pairs + side pairs/2 is exactly 1: 24.6% of 4c2e, 15.7% sub-7).

Switched case: 4c2e, ARM 31, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U2 D L D R2 D L` (7 moves, not sub-7). The whole attempt: `B' U D' B' L (U2 D L D R2 D L)`, 12 moves to DR.

</details>

**4c2e, example 17.** `D2 R D2 F2 U2 R' F2 L2 B2 F2 L B2 R2 D' L2 R F L R F R2 D`

EO `D' F R L' F'`, no RZP needed: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 4 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (pairs + side pairs/2 is exactly 1: 24.6% of 4c2e, 15.7% sub-7).

Switched case: 4c2e, ARM 41, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4a-4.

Optimal DR on the inverse: `U R2 D2 L F2 U F2 L` (8 moves, not sub-7). The whole attempt: `D' F R L' F' (U R2 D2 L F2 U F2 L)`, 13 moves to DR.

</details>

**4c2e, example 18.** `L D2 L2 D2 F2 L D2 L U2 F2 D2 R' D2 R' F2 U' R2 U2 B F2 U' F D' U'`

EO `(B D F' U' B)`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 0 (R/L stickers on U/D), 0 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (pairs + side pairs/2 is exactly 1: 24.6% of 4c2e, 15.7% sub-7).

Switched case: 4c2e, ARM 01, 0 pair(s) on 0 edge(s), 2 fake, 2 side pair(s), corners 4a-0.

Optimal DR on the normal side: `R' D' L2 D' R2 U' R` (7 moves, not sub-7). The whole attempt: `(B D F' U' B) R' D' L2 D' R2 U' R`, 12 moves to DR.

</details>

**4c2e, example 19.** `D2 L2 B2 U L2 U' L2 D' R2 D R2 B2 R' F2 D F2 U L B' L' F'`

EO `(B L' F)`, RZP `(D' L')`, on the inverse scramble: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 0 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (pairs + side pairs/2 is exactly 1: 24.6% of 4c2e, 15.7% sub-7).

Switched case: 4c2e, ARM 00, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4b-0, JZP.

Optimal DR on the normal side: `U2 D2 B2 R F2 R` (6 moves, sub-7). The whole attempt: `(B L' F D' L') U2 D2 B2 R F2 R`, 11 moves to DR.

</details>

**4c2e, example 20.** `L2 U F2 D B2 L2 D R2 U R2 D2 B2 U' B' R' B' U' F' D' R U2 R' B'`

EO `(D F U' L' B')`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (pairs + side pairs/2 is exactly 1: 24.6% of 4c2e, 15.7% sub-7).

Switched case: 4c2e, ARM 10, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the normal side: `U R2 U' D2 R U2 R` (7 moves, not sub-7). The whole attempt: `(D F U' L' B') U R2 U' D2 R U2 R`, 12 moves to DR.

</details>

**4c2e, example 21.** `L2 F2 U2 F2 D2 R' D2 B2 R2 D2 R' B2 R U' L B' F2 R' B L F2 R'`

EO `B L B2 R2 B'`, no RZP needed: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 4 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (pairs + side pairs/2 is 0 or 0.5: 53.2% of 4c2e, 4.0% sub-7).

Switched case: 4c2e, ARM 41, 0 pair(s) on 0 edge(s), 0 fake, 0 side pair(s), corners 4b-0.

Optimal DR on the inverse: `L2 U' D' B2 R U2 R` (7 moves, not sub-7). The whole attempt: `B L B2 R2 B' (L2 U' D' B2 R U2 R)`, 12 moves to DR.

</details>

**4c2e, example 22.** `B2 U' R2 B2 U R2 U B2 U' B2 U F2 D' R2 R' U B U2 F' R D B D U2`

EO `(B' U2 F)`, RZP `(U L')`, on the inverse scramble: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 0, corner ARM 4 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (pairs + side pairs/2 is 0 or 0.5: 53.2% of 4c2e, 4.0% sub-7).

Switched case: 4c2e, ARM 40, 0 pair(s) on 0 edge(s), 1 fake, 0 side pair(s), corners 4b-0.

Optimal DR on the normal side: `B2 D' F2 B2 D R U2 R` (8 moves, not sub-7). The whole attempt: `(B' U2 F U L') B2 D' F2 B2 D R U2 R`, 13 moves to DR.

</details>

**4c2e, example 23.** `F' D2 B' U2 B D2 L2 B U2 F' D2 B D2 B R' D U' F' U' L' D' R2 U2`

EO `(L F2 U' F B)`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (pairs + side pairs/2 is 0 or 0.5: 53.2% of 4c2e, 4.0% sub-7).

Switched case: 4c2e, ARM 21, 0 pair(s) on 0 edge(s), 1 fake, 0 side pair(s), corners 4b-2.

Optimal DR on the normal side: `R D2 R' D2 R2 D' R` (7 moves, not sub-7). The whole attempt: `(L F2 U' F B) R D2 R' D2 R2 D' R`, 12 moves to DR.

</details>

**4c2e, example 24.** `F2 D2 L' R2 U2 R' F2 L U2 R' U2 B2 U2 D2 F' U L2 B' F D F' L`

EO `(B L D' B')`, RZP `(R)`, on the inverse scramble: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (pairs + side pairs/2 is 0 or 0.5: 53.2% of 4c2e, 4.0% sub-7).

Switched case: 4c2e, ARM 21, 0 pair(s) on 0 edge(s), 1 fake, 1 side pair(s), corners 4a-2.

Optimal DR on the normal side: `U' R' D' B2 L U2 D' L` (8 moves, not sub-7). The whole attempt: `(B L D' B' R) U' R' D' B2 L U2 D' L`, 13 moves to DR.

</details>

**4c2e, example 25.** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `L F2 B`, RZP `D L`: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 0, corner ARM 3 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (pairs + side pairs/2 is 0 or 0.5: 53.2% of 4c2e, 4.0% sub-7).

Switched case: 4c2e, ARM 30, 0 pair(s) on 0 edge(s), 2 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U2 R' U' R U2 R' U R` (8 moves, not sub-7). The whole attempt: `L F2 B D L (U2 R' U' R U2 R' U R)`, 13 moves to DR.

</details>

**4c2e, example 26.** `R2 U R2 U' B2 D' F2 U2 B2 F2 U' B2 D' F' R' B2 F2 D' R F U2 L`

EO `B D2 L2 B'`, RZP `L'`: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 0, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (pairs + side pairs/2 is 0 or 0.5: 53.2% of 4c2e, 4.0% sub-7).

Switched case: 4c2e, ARM 20, 0 pair(s) on 0 edge(s), 0 fake, 1 side pair(s), corners 4b-2.

Optimal DR on the inverse: `U2 R' U R F2 D F2 R` (8 moves, not sub-7). The whole attempt: `B D2 L2 B' L' (U2 R' U R F2 D F2 R)`, 13 moves to DR.

</details>

**4c2e, example 27.** `F2 D2 R2 U L2 B2 U L2 R2 D B2 U2 B2 B' R' U L U2 F' R' B' L'`

EO `(L' F' R D' B)`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (pairs + side pairs/2 is 0 or 0.5: 53.2% of 4c2e, 4.0% sub-7).

Switched case: 4c2e, ARM 31, 0 pair(s) on 0 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the normal side: `R2 L2 D R' B2 R` (6 moves, sub-7). The whole attempt: `(L' F' R D' B) R2 L2 D R' B2 R`, 11 moves to DR.

</details>

**4c2e, example 28.** `F2 U F2 L2 B2 U' L2 D2 R2 L2 D R2 U2 F' D2 U L D U L U2 F`

EO `U D L U' F`, no RZP needed: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 0, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (pairs + side pairs/2 is 0 or 0.5: 53.2% of 4c2e, 4.0% sub-7).

Switched case: 4c2e, ARM 20, 0 pair(s) on 0 edge(s), 1 fake, 0 side pair(s), corners 4b-2.

Optimal DR on the inverse: `R D' F2 D R' F2 R` (7 moves, not sub-7). The whole attempt: `U D L U' F (R D' F2 D R' F2 R)`, 12 moves to DR.

</details>

**4c2e, example 29.** `U2 R' F2 R2 U2 B2 F2 R' D2 R2 B2 R' F2 D2 R' F' U' R' B F' R2 D' R F'`

EO `(B' U R' L2 B')`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (pairs + side pairs/2 is 0 or 0.5: 53.2% of 4c2e, 4.0% sub-7).

Switched case: 4c2e, ARM 11, 0 pair(s) on 0 edge(s), 1 fake, 0 side pair(s), corners 4c-1.

Optimal DR on the normal side: `F2 L U2 D L' B2 D R` (8 moves, not sub-7). The whole attempt: `(B' U R' L2 B') F2 L U2 D L' B2 D R`, 13 moves to DR.

</details>

**4c2e, example 30.** `L D2 L2 D2 F2 L D2 L U2 F2 D2 R' D2 R' F2 U' R2 U2 B F2 U' F D' U'`

EO `(R2 D F' U' B')`, no RZP needed, on the inverse scramble: 4c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 0 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (pairs + side pairs/2 is 0 or 0.5: 53.2% of 4c2e, 4.0% sub-7).

Switched case: 4c2e, ARM 01, 0 pair(s) on 0 edge(s), 1 fake, 0 side pair(s), corners 4b-0.

Optimal DR on the normal side: `U' D2 R U D R' D' R` (8 moves, not sub-7). The whole attempt: `(R2 D F' U' B') U' D2 R U D R' D' R`, 13 moves to DR.

</details>

## 3c2e

**3c2e, example 1.** `L2 U2 B2 R U2 R' U2 L' D2 L D2 B2 D' F2 L F2 R U B' U' F'`

EO `(B U' F')`, RZP `(D R)`, on the inverse scramble: 3c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (always: 100.0% of 3c2e, 61.6% sub-7).

Switched case: 3c2e, ARM 11, 0 pair(s) on 0 edge(s), 1 fake, 0 side pair(s).

Optimal DR on the normal side: `U' F2 B2 U R' U R` (7 moves, not sub-7). The whole attempt: `(B U' F' D R) U' F2 B2 U R' U R`, 12 moves to DR.

</details>

**3c2e, example 2.** `D2 L2 B2 L2 F2 U' F2 R2 U2 F2 U' R2 U B' D R' L2 U' R D L2 U'`

EO `(L2 F R2 U2 F')`, no RZP needed, on the inverse scramble: 3c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (always: 100.0% of 3c2e, 61.6% sub-7).

Switched case: 3c2e, ARM 10, 0 pair(s) on 0 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the normal side: `U D F2 R' L2 U R` (7 moves, not sub-7). The whole attempt: `(L2 F R2 U2 F') U D F2 R' L2 U R`, 12 moves to DR.

</details>

**3c2e, example 3.** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `(D2 R B2 U2 B')`, no RZP needed, on the inverse scramble: 3c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (always: 100.0% of 3c2e, 61.6% sub-7).

Switched case: 3c2e, ARM 11, 0 pair(s) on 0 edge(s), 0 fake, 1 side pair(s).

Optimal DR on the normal side: `U' B2 U R L2 U R` (7 moves, not sub-7). The whole attempt: `(D2 R B2 U2 B') U' B2 U R L2 U R`, 12 moves to DR.

</details>

**3c2e, example 4.** `L2 R2 B' U2 F2 U2 L2 F' U2 B2 U2 R2 F B2 R2 U' B2 L B R U B L' D L'`

EO `(B D' F)`, RZP `(R L)`, on the inverse scramble: 3c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 0, corner ARM 0 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (always: 100.0% of 3c2e, 61.6% sub-7).

Switched case: 3c2e, ARM 00, 0 pair(s) on 0 edge(s), 0 fake, 1 side pair(s).

Optimal DR on the normal side: `F2 B2 D L' D' L` (6 moves, sub-7). The whole attempt: `(B D' F R L) F2 B2 D L' D' L`, 11 moves to DR.

</details>

**3c2e, example 5.** `D2 B' R2 D2 B R2 B D2 B' D2 B U2 F' R2 R' B D B2 U' R F D F B2`

EO `R2 L B`, RZP `D2 R'`: 3c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (always: 100.0% of 3c2e, 61.6% sub-7).

Switched case: 3c2e, ARM 11, 0 pair(s) on 0 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the inverse: `U' R U2 D' R U2 R` (7 moves, not sub-7). The whole attempt: `R2 L B D2 R' (U' R U2 D' R U2 R)`, 12 moves to DR.

</details>

**3c2e, example 6.** `U2 L2 F2 R B2 D2 R B2 F2 L D2 R2 D2 D' F' R B R2 U' F' D' B'`

EO `(U' F' B')`, RZP `(U' L')`, on the inverse scramble: 3c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (always: 100.0% of 3c2e, 61.6% sub-7).

Switched case: 3c2e, ARM 10, 1 pair(s) on 1 edge(s), 1 fake, 0 side pair(s).

Optimal DR on the normal side: `U' F2 D2 R D' R` (6 moves, sub-7). The whole attempt: `(U' F' B' U' L') U' F2 D2 R D' R`, 11 moves to DR.

</details>

**3c2e, example 7.** `L2 D2 B' F2 U2 F' L2 B U2 F' U2 R2 U2 D2 L' U B2 R' L D L' B`

EO `(B U F)`, RZP `(D R')`, on the inverse scramble: 3c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (always: 100.0% of 3c2e, 61.6% sub-7).

Switched case: 3c2e, ARM 21, 0 pair(s) on 0 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the normal side: `R2 U2 D2 R D R` (6 moves, sub-7). The whole attempt: `(B U F D R') R2 U2 D2 R D R`, 11 moves to DR.

</details>

**3c2e, example 8.** `R2 D' B2 L2 U' L2 D2 R2 F2 D' B2 L2 U F2 U B' R2 U' R L2 B L2 F`

EO `U F' R F2 B'`, no RZP needed: 3c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (always: 100.0% of 3c2e, 61.6% sub-7).

Switched case: 3c2e, ARM 11, 1 pair(s) on 1 edge(s), 1 fake, 0 side pair(s).

Optimal DR on the inverse: `U2 D R U' R` (5 moves, sub-7). The whole attempt: `U F' R F2 B' (U2 D R U' R)`, 10 moves to DR.

</details>

**3c2e, example 9.** `R F2 R' U2 R D2 B2 R' B2 R U2 L D' R' F L' B L' F2 D F2 L`

EO `(D' L F R B')`, no RZP needed, on the inverse scramble: 3c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (always: 100.0% of 3c2e, 61.6% sub-7).

Switched case: 3c2e, ARM 11, 0 pair(s) on 0 edge(s), 1 fake, 0 side pair(s).

Optimal DR on the normal side: `R2 U2 D' R' U R` (6 moves, sub-7). The whole attempt: `(D' L F R B') R2 U2 D' R' U R`, 11 moves to DR.

</details>

**3c2e, example 10.** `L D2 L2 D2 F2 L D2 L U2 F2 D2 R' D2 R' F2 U' R2 U2 B F2 U' F D' U'`

EO `(D' F' U' F2 B')`, no RZP needed, on the inverse scramble: 3c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (always: 100.0% of 3c2e, 61.6% sub-7).

Switched case: 3c2e, ARM 11, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the normal side: `U' R D R' D' R` (6 moves, sub-7). The whole attempt: `(D' F' U' F2 B') U' R D R' D' R`, 11 moves to DR.

</details>

## 7c8e

**7c8e, example 1.** `F2 U2 L2 B U2 B' U2 F' D2 F D2 L2 D' R2 F R2 B U L' U' R'`

EO `(D2 R2 U' D' B')`, no RZP needed, on the inverse scramble: 7c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 5 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (5 or 6 pairs: 16.3% of 7c8e, 59.0% sub-7).

Switched case: 7c8e, ARM 31, 5 pair(s) on 4 edge(s), 2 fake, 4 side pair(s).

Optimal DR on the normal side: `B2 R2 U L' U' R` (6 moves, sub-7). The whole attempt: `(D2 R2 U' D' B') B2 R2 U L' U' R`, 11 moves to DR.

</details>

**7c8e, example 2.** `L2 F2 D R2 D' F2 U B2 L2 D R2 U' F2 U' B2 F' L' D R' D L' D B2 D2 U2`

EO `D B`, RZP `R U2 L`: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 5 pair(s), 5 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (5 or 6 pairs: 16.3% of 7c8e, 59.0% sub-7).

Switched case: 7c8e, ARM 21, 5 pair(s) on 3 edge(s), 3 fake, 5 side pair(s).

Optimal DR on the inverse: `U2 R2 L D R` (5 moves, sub-7). The whole attempt: `D B R U2 L (U2 R2 L D R)`, 10 moves to DR.

</details>

**7c8e, example 3.** `L2 B R2 D2 R2 L2 F' L2 F2 U2 F U2 F D2 B' L' F D R' U2 F' U' F' L F2`

EO `(U' R F')`, RZP `(U R)`, on the inverse scramble: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 3, corner ARM 5 (R/L stickers on U/D), 5 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (5 or 6 pairs: 16.3% of 7c8e, 59.0% sub-7).

Switched case: 7c8e, ARM 53, 5 pair(s) on 3 edge(s), 1 fake, 2 side pair(s).

Optimal DR on the normal side: `U D R2 B2 R U L` (7 moves, not sub-7). The whole attempt: `(U' R F' U R) U D R2 B2 R U L`, 12 moves to DR.

</details>

**7c8e, example 4.** `L2 D2 F2 U B2 R2 U B2 F2 D R2 U2 R2 R' F' U B U2 L' F' R' B'`

EO `(D' L B' D' F')`, no RZP needed, on the inverse scramble: 7c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 5 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (5 or 6 pairs: 16.3% of 7c8e, 59.0% sub-7).

Switched case: 7c8e, ARM 42, 5 pair(s) on 4 edge(s), 1 fake, 3 side pair(s).

Optimal DR on the normal side: `D R2 L2 F2 R U' L` (7 moves, not sub-7). The whole attempt: `(D' L B' D' F') D R2 L2 F2 R U' L`, 12 moves to DR.

</details>

**7c8e, example 5.** `U2 L2 U2 R2 B2 R2 B2 F' R2 B' R2 D2 B' R' U' L2 B D2 R' U L' B2 F2`

EO `(B U' L2 B')`, RZP `(L')`, on the inverse scramble: 7c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 5 pair(s), 5 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (5 or 6 pairs: 16.3% of 7c8e, 59.0% sub-7).

Switched case: 7c8e, ARM 21, 5 pair(s) on 4 edge(s), 1 fake, 5 side pair(s).

Optimal DR on the normal side: `U2 R2 L2 B2 L' D R` (7 moves, not sub-7). The whole attempt: `(B U' L2 B' L') U2 R2 L2 B2 L' D R`, 12 moves to DR.

</details>

**7c8e, example 6.** `U2 R' B2 R' D2 L' B2 F2 L2 D2 F2 R B2 U2 D' L U' B F' R U' L2 F'`

EO `(L2 U' B R' F')`, no RZP needed, on the inverse scramble: 7c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 3, corner ARM 3 (R/L stickers on U/D), 5 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (5 or 6 pairs: 16.3% of 7c8e, 59.0% sub-7).

Switched case: 7c8e, ARM 33, 5 pair(s) on 4 edge(s), 2 fake, 4 side pair(s).

Optimal DR on the normal side: `U B2 R D' L` (5 moves, sub-7). The whole attempt: `(L2 U' B R' F') U B2 R D' L`, 10 moves to DR.

</details>

**7c8e, example 7.** `R2 F2 D' B2 D2 R2 D' L2 U R2 D2 U' F2 L' R' U' B' L F U' L'`

EO `(B' R' F U B')`, no RZP needed, on the inverse scramble: 7c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 2, corner ARM 5 (R/L stickers on U/D), 5 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (5 or 6 pairs: 16.3% of 7c8e, 59.0% sub-7).

Switched case: 7c8e, ARM 52, 5 pair(s) on 4 edge(s), 3 fake, 2 side pair(s).

Optimal DR on the normal side: `U' B2 U L D R` (6 moves, sub-7). The whole attempt: `(B' R' F U B') U' B2 U L D R`, 11 moves to DR.

</details>

**7c8e, example 8.** `D2 R2 F L2 B2 D2 F R2 F' R2 F U2 R2 R' U B U R' B U' R' D' B'`

EO `F' U' L U B`, no RZP needed: 7c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 5 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (5 or 6 pairs: 16.3% of 7c8e, 59.0% sub-7).

Switched case: 7c8e, ARM 31, 5 pair(s) on 4 edge(s), 1 fake, 4 side pair(s).

Optimal DR on the inverse: `D R2 F2 R' D L` (6 moves, sub-7). The whole attempt: `F' U' L U B (D R2 F2 R' D L)`, 11 moves to DR.

</details>

**7c8e, example 9.** `U2 F U2 B D2 B2 R2 F R2 U2 L2 B' U' R2 L B2 U' D2 F' D L U`

EO `L' F R2 L B`, no RZP needed: 7c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 3, corner ARM 4 (R/L stickers on U/D), 5 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (5 or 6 pairs: 16.3% of 7c8e, 59.0% sub-7).

Switched case: 7c8e, ARM 43, 5 pair(s) on 4 edge(s), 2 fake, 3 side pair(s).

Optimal DR on the inverse: `U2 F2 R2 D L U R` (7 moves, not sub-7). The whole attempt: `L' F R2 L B (U2 F2 R2 D L U R)`, 12 moves to DR.

</details>

**7c8e, example 10.** `F D2 F2 D2 R2 F D2 F U2 R2 D2 B' D2 B' R2 U' B2 U2 L R2 U' R D' U'`

EO `(U2 D2 B R2 B')`, no RZP needed, on the inverse scramble: 7c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 3, corner ARM 5 (R/L stickers on U/D), 5 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (5 or 6 pairs: 16.3% of 7c8e, 59.0% sub-7).

Switched case: 7c8e, ARM 53, 5 pair(s) on 4 edge(s), 1 fake, 2 side pair(s).

Optimal DR on the normal side: `U D' R2 B2 R' U L` (7 moves, not sub-7). The whole attempt: `(U2 D2 B R2 B') U D' R2 B2 R' U L`, 12 moves to DR.

</details>

**7c8e, example 11.** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `D L2 D2 L' B'`, no RZP needed: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 2, corner ARM 6 (R/L stickers on U/D), 4 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 33.7% of 7c8e, 15.9% sub-7).

Switched case: 7c8e, ARM 62, 4 pair(s) on 3 edge(s), 3 fake, 1 side pair(s).

Optimal DR on the inverse: `U R2 D F2 R D' L` (7 moves, not sub-7). The whole attempt: `D L2 D2 L' B' (U R2 D F2 R D' L)`, 12 moves to DR.

</details>

**7c8e, example 12.** `F D2 F2 D2 R2 F D2 F U2 R2 D2 B' D2 B' R2 U' B2 U2 L R2 U' R D' U'`

EO `L2 U F R2 F`, no RZP needed: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 3, corner ARM 3 (R/L stickers on U/D), 4 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 33.7% of 7c8e, 15.9% sub-7).

Switched case: 7c8e, ARM 33, 4 pair(s) on 3 edge(s), 2 fake, 4 side pair(s).

Optimal DR on the inverse: `U F2 L2 D R' U L` (7 moves, not sub-7). The whole attempt: `L2 U F R2 F (U F2 L2 D R' U L)`, 12 moves to DR.

</details>

**7c8e, example 13.** `U2 D2 F' L2 B2 L2 U2 B' L2 F2 L2 D2 B F2 D2 L' F2 U F D L F U' R U'`

EO `(U2 F R' B')`, RZP `(L')`, on the inverse scramble: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 3, corner ARM 3 (R/L stickers on U/D), 4 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 33.7% of 7c8e, 15.9% sub-7).

Switched case: 7c8e, ARM 33, 4 pair(s) on 3 edge(s), 4 fake, 4 side pair(s).

Optimal DR on the normal side: `F2 U' B2 D R U' L` (7 moves, not sub-7). The whole attempt: `(U2 F R' B' L') F2 U' B2 D R U' L`, 12 moves to DR.

</details>

**7c8e, example 14.** `R2 D2 B U2 F2 R2 B D2 B' D2 B L2 D2 D' L F L D' F L' D' R' F'`

EO `B U L F`, RZP `R'`: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 2, corner ARM 2 (R/L stickers on U/D), 4 pair(s), 5 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 33.7% of 7c8e, 15.9% sub-7).

Switched case: 7c8e, ARM 22, 4 pair(s) on 3 edge(s), 4 fake, 5 side pair(s).

Optimal DR on the inverse: `U' B2 R D' L U F2 R` (8 moves, not sub-7). The whole attempt: `B U L F R' (U' B2 R D' L U F2 R)`, 13 moves to DR.

</details>

**7c8e, example 15.** `L2 F2 U2 F2 D2 R' D2 B2 R2 D2 R' B2 R U' L B' F2 R' B L F2 R'`

EO `D' F' U2 F`, RZP `L`: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 2, corner ARM 6 (R/L stickers on U/D), 4 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 33.7% of 7c8e, 15.9% sub-7).

Switched case: 7c8e, ARM 62, 4 pair(s) on 3 edge(s), 3 fake, 1 side pair(s).

Optimal DR on the inverse: `U2 L2 U' R2 U' R' D' L` (8 moves, not sub-7). The whole attempt: `D' F' U2 F L (U2 L2 U' R2 U' R' D' L)`, 13 moves to DR.

</details>

**7c8e, example 16.** `D2 L2 U2 R2 B' L2 B D2 F2 R2 D2 B' F2 L' U' D2 B U D R U' B' F'`

EO `U' F' U' L B`, no RZP needed: 7c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 3, corner ARM 4 (R/L stickers on U/D), 4 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 33.7% of 7c8e, 15.9% sub-7).

Switched case: 7c8e, ARM 43, 4 pair(s) on 4 edge(s), 3 fake, 3 side pair(s).

Optimal DR on the inverse: `U2 F2 R2 U L' D' R` (7 moves, not sub-7). The whole attempt: `U' F' U' L B (U2 F2 R2 U L' D' R)`, 12 moves to DR.

</details>

**7c8e, example 17.** `L2 U2 B R2 B' D2 F B2 U2 R2 B D2 U2 B' U' L' D2 U2 B' L F2 L' F B2`

EO `(L' F R F B')`, no RZP needed, on the inverse scramble: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 4 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 33.7% of 7c8e, 15.9% sub-7).

Switched case: 7c8e, ARM 31, 4 pair(s) on 3 edge(s), 4 fake, 4 side pair(s).

Optimal DR on the normal side: `R2 L2 D' L D R` (6 moves, sub-7). The whole attempt: `(L' F R F B') R2 L2 D' L D R`, 11 moves to DR.

</details>

**7c8e, example 18.** `D2 L2 B' R2 B2 D2 B' U2 F D2 B2 F' L2 U' D' F' R' U L F' U'`

EO `U2 R L2 U' F`, no RZP needed: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 3, corner ARM 3 (R/L stickers on U/D), 4 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 33.7% of 7c8e, 15.9% sub-7).

Switched case: 7c8e, ARM 33, 4 pair(s) on 3 edge(s), 3 fake, 4 side pair(s).

Optimal DR on the inverse: `U L2 D' F2 R U' L` (7 moves, not sub-7). The whole attempt: `U2 R L2 U' F (U L2 D' F2 R U' L)`, 12 moves to DR.

</details>

**7c8e, example 19.** `U2 L2 F2 R B2 D2 R B2 F2 L D2 R2 D2 D' F' R B R2 U' F' D' B'`

EO `(U R2 F' B)`, RZP `(R)`, on the inverse scramble: 7c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 2, corner ARM 3 (R/L stickers on U/D), 4 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 33.7% of 7c8e, 15.9% sub-7).

Switched case: 7c8e, ARM 32, 4 pair(s) on 4 edge(s), 4 fake, 4 side pair(s).

Optimal DR on the normal side: `R' L' U' R' F2 U2 R` (7 moves, not sub-7). The whole attempt: `(U R2 F' B R) R' L' U' R' F2 U2 R`, 12 moves to DR.

</details>

**7c8e, example 20.** `L2 U' B2 U' R2 D' B2 F2 D2 R2 F2 U B2 L2 R' D L' B F' U L' D2 F'`

EO `U' R F' R' B'`, no RZP needed: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 2, corner ARM 2 (R/L stickers on U/D), 4 pair(s), 5 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 33.7% of 7c8e, 15.9% sub-7).

Switched case: 7c8e, ARM 22, 4 pair(s) on 3 edge(s), 3 fake, 5 side pair(s).

Optimal DR on the inverse: `U R2 L2 D' B2 R' U L` (8 moves, not sub-7). The whole attempt: `U' R F' R' B' (U R2 L2 D' B2 R' U L)`, 13 moves to DR.

</details>

**7c8e, example 21.** `R2 F2 D' B2 D2 R2 D' L2 U R2 D2 U' F2 L' R' U' B' L F U' L'`

EO `(B' U' R' F B')`, no RZP needed, on the inverse scramble: 7c8e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 4 (R/L stickers on U/D), 2 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 50.0% of 7c8e, 2.9% sub-7).

Switched case: 7c8e, ARM 41, 2 pair(s) on 2 edge(s), 5 fake, 3 side pair(s).

Optimal DR on the normal side: `R L2 D L U R' D R` (8 moves, not sub-7). The whole attempt: `(B' U' R' F B') R L2 D L U R' D R`, 13 moves to DR.

</details>

**7c8e, example 22.** `L2 U2 B R2 B' D2 F B2 U2 R2 B D2 U2 B' U' L' D2 U2 B' L F2 L' F B2`

EO `(F R F' L' B')`, no RZP needed, on the inverse scramble: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 1, corner ARM 5 (R/L stickers on U/D), 3 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 50.0% of 7c8e, 2.9% sub-7).

Switched case: 7c8e, ARM 51, 3 pair(s) on 3 edge(s), 5 fake, 2 side pair(s).

Optimal DR on the normal side: `U R' U' L' D B2 R` (7 moves, not sub-7). The whole attempt: `(F R F' L' B') U R' U' L' D B2 R`, 12 moves to DR.

</details>

**7c8e, example 23.** `D2 L2 B2 L2 F2 U' F2 R2 U2 F2 U' R2 U B' D R' L2 U' R D L2 U'`

EO `(B2 U2 B')`, RZP `(R' L')`, on the inverse scramble: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 3, corner ARM 4 (R/L stickers on U/D), 3 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 50.0% of 7c8e, 2.9% sub-7).

Switched case: 7c8e, ARM 43, 3 pair(s) on 3 edge(s), 5 fake, 3 side pair(s).

Optimal DR on the normal side: `U D R' L D R' D2 R` (8 moves, not sub-7). The whole attempt: `(B2 U2 B' R' L') U D R' L D R' D2 R`, 13 moves to DR.

</details>

**7c8e, example 24.** `L2 U2 B D2 B R2 F R2 F' R2 D2 B' R2 L' D' B' U R D' L2 U2 L2`

EO `(R U D2 R2 F)`, no RZP needed, on the inverse scramble: 7c8e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 2 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 50.0% of 7c8e, 2.9% sub-7).

Switched case: 7c8e, ARM 42, 2 pair(s) on 2 edge(s), 4 fake, 3 side pair(s).

Optimal DR on the normal side: `F2 L' D' R' U D2 R` (7 moves, not sub-7). The whole attempt: `(R U D2 R2 F) F2 L' D' R' U D2 R`, 12 moves to DR.

</details>

**7c8e, example 25.** `F2 D2 L' R2 U2 R' F2 L U2 R' U2 B2 U2 D2 F' U L2 B' F D F' L`

EO `F2 U2 B2 U' B'`, no RZP needed: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 3 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 50.0% of 7c8e, 2.9% sub-7).

Switched case: 7c8e, ARM 31, 3 pair(s) on 3 edge(s), 4 fake, 4 side pair(s).

Optimal DR on the inverse: `R2 F2 B2 D' R D L` (7 moves, not sub-7). The whole attempt: `F2 U2 B2 U' B' (R2 F2 B2 D' R D L)`, 12 moves to DR.

</details>

**7c8e, example 26.** `F2 U F2 L2 B2 U' L2 D2 R2 L2 D R2 U2 F' D2 U L D U L U2 F`

EO `D L2 F'`, RZP `U R`: 7c8e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 50.0% of 7c8e, 2.9% sub-7).

Switched case: 7c8e, ARM 32, 1 pair(s) on 1 edge(s), 5 fake, 4 side pair(s).

Optimal DR on the inverse: `R L U F2 U' R2 U R` (8 moves, not sub-7). The whole attempt: `D L2 F' U R (R L U F2 U' R2 U R)`, 13 moves to DR.

</details>

**7c8e, example 27.** `D2 R D2 R' B2 L' F2 R2 B2 F2 R' B2 L' F' D' B2 F2 L' D F R2 U`

EO `R' B2 D2 R' F'`, no RZP needed: 7c8e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 2 (R/L stickers on U/D), 3 pair(s), 5 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 50.0% of 7c8e, 2.9% sub-7).

Switched case: 7c8e, ARM 22, 3 pair(s) on 2 edge(s), 4 fake, 5 side pair(s).

Optimal DR on the inverse: `R L2 D' L U2 R2 D' R` (8 moves, not sub-7). The whole attempt: `R' B2 D2 R' F' (R L2 D' L U2 R2 D' R)`, 13 moves to DR.

</details>

**7c8e, example 28.** `L2 D2 F2 U B2 R2 U B2 F2 D R2 U2 R2 R' F' U B U2 L' F' R' B'`

EO `(L F B')`, RZP `(U' L)`, on the inverse scramble: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 3 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 50.0% of 7c8e, 2.9% sub-7).

Switched case: 7c8e, ARM 31, 3 pair(s) on 3 edge(s), 3 fake, 4 side pair(s).

Optimal DR on the normal side: `R2 L2 F2 U' L U R` (7 moves, not sub-7). The whole attempt: `(L F B' U' L) R2 L2 F2 U' L U R`, 12 moves to DR.

</details>

**7c8e, example 29.** `F D2 F2 D2 R2 F D2 F U2 R2 D2 B' D2 B' R2 U' B2 U2 L R2 U' R D' U'`

EO `(F2 L2 B' U2 B')`, no RZP needed, on the inverse scramble: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 3, corner ARM 3 (R/L stickers on U/D), 3 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 50.0% of 7c8e, 2.9% sub-7).

Switched case: 7c8e, ARM 33, 3 pair(s) on 3 edge(s), 3 fake, 4 side pair(s).

Optimal DR on the normal side: `D' R D L D' R2 U' L` (8 moves, not sub-7). The whole attempt: `(F2 L2 B' U2 B') D' R D L D' R2 U' L`, 13 moves to DR.

</details>

**7c8e, example 30.** `L2 B U2 F D2 L2 F R2 B R2 F2 D2 B' D' R' D' B' U' F' R B2 R' D'`

EO `R D' B R' F'`, no RZP needed: 7c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 3 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 50.0% of 7c8e, 2.9% sub-7).

Switched case: 7c8e, ARM 42, 3 pair(s) on 3 edge(s), 4 fake, 3 side pair(s).

Optimal DR on the inverse: `L' B2 U R F2 D' L` (7 moves, not sub-7). The whole attempt: `R D' B R' F' (L' B2 U R F2 D' L)`, 12 moves to DR.

</details>

## 8c8e

**8c8e, example 1.** `L2 R2 B' U2 F2 U2 L2 F' U2 B2 U2 R2 F B2 R2 U' B2 L B R U B L' D L'`

EO `(R2 F2 B U F')`, no RZP needed, on the inverse scramble: 8c8e in 5. Traced before switching: 2 paired edge(s), edge ARM 3, corner ARM 4 (R/L stickers on U/D), 4 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (corner ARM 0, 4 or 8: 44.2% of 8c8e, 20.5% sub-7).

Switched case: 8c8e, ARM 43, 4 pair(s) on 2 edge(s), 4 fake, 4 side pair(s).

Optimal DR on the normal side: `U R2 U R' L U' D L` (8 moves, not sub-7). The whole attempt: `(R2 F2 B U F') U R2 U R' L U' D L`, 13 moves to DR.

</details>

**8c8e, example 2.** `L2 U' B2 U' R2 D' B2 F2 D2 R2 F2 U B2 L2 R' D L' B F' U L' D2 F'`

EO `U B' R F'`, RZP `R'`: 8c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 4 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (corner ARM 0, 4 or 8: 44.2% of 8c8e, 20.5% sub-7).

Switched case: 8c8e, ARM 42, 4 pair(s) on 4 edge(s), 4 fake, 4 side pair(s).

Optimal DR on the inverse: `R' L' D R2 U2 L` (6 moves, sub-7). The whole attempt: `U B' R F' R' (R' L' D R2 U2 L)`, 11 moves to DR.

</details>

**8c8e, example 3.** `F D2 F2 D2 R2 F D2 F U2 R2 D2 B' D2 B' R2 U' B2 U2 L R2 U' R D' U'`

EO `U F2 B' D2 B`, no RZP needed: 8c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 3, corner ARM 4 (R/L stickers on U/D), 4 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (corner ARM 0, 4 or 8: 44.2% of 8c8e, 20.5% sub-7).

Switched case: 8c8e, ARM 43, 4 pair(s) on 3 edge(s), 4 fake, 4 side pair(s).

Optimal DR on the inverse: `R' D' L U' F2 U2 R` (7 moves, not sub-7). The whole attempt: `U F2 B' D2 B (R' D' L U' F2 U2 R)`, 12 moves to DR.

</details>

**8c8e, example 4.** `B2 R' D2 B2 R D2 R B2 R' B2 R F2 L' D2 D' R B R2 F' D L B L R2`

EO `(F B2 D2 B)`, RZP `(L)`, on the inverse scramble: 8c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 5 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (corner ARM 0, 4 or 8: 44.2% of 8c8e, 20.5% sub-7).

Switched case: 8c8e, ARM 42, 5 pair(s) on 4 edge(s), 3 fake, 4 side pair(s).

Optimal DR on the normal side: `U R B2 L B2 D L` (7 moves, not sub-7). The whole attempt: `(F B2 D2 B L) U R B2 L B2 D L`, 12 moves to DR.

</details>

**8c8e, example 5.** `U2 F2 R2 B L2 D2 B L2 R2 F D2 B2 D2 D' R' B L B2 U' R' D' L'`

EO `D B' L2 F`, RZP `R`: 8c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 1, corner ARM 0 (R/L stickers on U/D), 6 pair(s), 8 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (corner ARM 0, 4 or 8: 44.2% of 8c8e, 20.5% sub-7).

Switched case: 8c8e, ARM 01, 6 pair(s) on 3 edge(s), 2 fake, 8 side pair(s).

Optimal DR on the inverse: `R U' R2 L2 D L` (6 moves, sub-7). The whole attempt: `D B' L2 F R (R U' R2 L2 D L)`, 11 moves to DR.

</details>

**8c8e, example 6.** `L2 U2 L2 D2 F2 D2 F2 B' D2 F' D2 R2 F' D' L' U2 F R2 D' L U' F2 B2`

EO `R L F2 B`, RZP `R`: 8c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 4 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (corner ARM 0, 4 or 8: 44.2% of 8c8e, 20.5% sub-7).

Switched case: 8c8e, ARM 42, 4 pair(s) on 3 edge(s), 4 fake, 4 side pair(s).

Optimal DR on the inverse: `R L U' D L` (5 moves, sub-7). The whole attempt: `R L F2 B R (R L U' D L)`, 10 moves to DR.

</details>

**8c8e, example 7.** `L2 U2 B D2 B R2 F R2 F' R2 D2 B' R2 L' D' B' U R D' L2 U2 L2`

EO `(R L U' L B)`, no RZP needed, on the inverse scramble: 8c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 1, corner ARM 4 (R/L stickers on U/D), 3 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (corner ARM 0, 4 or 8: 44.2% of 8c8e, 20.5% sub-7).

Switched case: 8c8e, ARM 41, 3 pair(s) on 3 edge(s), 5 fake, 4 side pair(s).

Optimal DR on the normal side: `R' U' R U L U R` (7 moves, not sub-7). The whole attempt: `(R L U' L B) R' U' R U L U R`, 12 moves to DR.

</details>

**8c8e, example 8.** `D R2 U2 F2 L2 R2 U L2 D' F2 U R2 F2 L2 U' R' U' R' B L' D2 R B' U2`

EO `F U2 F2 R' B'`, no RZP needed: 8c8e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 4 pair(s), 4 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (corner ARM 0, 4 or 8: 44.2% of 8c8e, 20.5% sub-7).

Switched case: 8c8e, ARM 42, 4 pair(s) on 2 edge(s), 4 fake, 4 side pair(s).

Optimal DR on the inverse: `L' U' R D' F2 U2 R` (7 moves, not sub-7). The whole attempt: `F U2 F2 R' B' (L' U' R D' F2 U2 R)`, 12 moves to DR.

</details>

**8c8e, example 9.** `F D2 F2 D2 R2 F D2 F U2 R2 D2 B' D2 B' R2 U' B2 U2 L R2 U' R D' U'`

EO `(U2 R2 F' R2 F)`, no RZP needed, on the inverse scramble: 8c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 3, corner ARM 5 (R/L stickers on U/D), 5 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (corner ARM 2, 3, 5 or 6: 55.8% of 8c8e, 9.8% sub-7).

Switched case: 8c8e, ARM 53, 5 pair(s) on 4 edge(s), 3 fake, 3 side pair(s).

Optimal DR on the normal side: `L' U D' R U L` (6 moves, sub-7). The whole attempt: `(U2 R2 F' R2 F) L' U D' R U L`, 11 moves to DR.

</details>

**8c8e, example 10.** `U2 L2 F2 R B2 D2 R B2 F2 L D2 R2 D2 D' F' R B R2 U' F' D' B'`

EO `(U' F' B')`, RZP `(D R')`, on the inverse scramble: 8c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 2, corner ARM 3 (R/L stickers on U/D), 4 pair(s), 5 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (corner ARM 2, 3, 5 or 6: 55.8% of 8c8e, 9.8% sub-7).

Switched case: 8c8e, ARM 32, 4 pair(s) on 4 edge(s), 4 fake, 5 side pair(s).

Optimal DR on the normal side: `U D R U R L' D R` (8 moves, not sub-7). The whole attempt: `(U' F' B' D R') U D R U R L' D R`, 13 moves to DR.

</details>

**8c8e, example 11.** `U2 F' R2 F D2 B' U2 B U2 L2 U2 R2 F' D2 F2 U' L F D' B U' D2 F2 L U F'`

EO `(D' B' R2 U' F')`, no RZP needed, on the inverse scramble: 8c8e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 6 (R/L stickers on U/D), 3 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (corner ARM 2, 3, 5 or 6: 55.8% of 8c8e, 9.8% sub-7).

Switched case: 8c8e, ARM 62, 3 pair(s) on 2 edge(s), 5 fake, 2 side pair(s).

Optimal DR on the normal side: `D' L' U' R' U2 D' R` (7 moves, not sub-7). The whole attempt: `(D' B' R2 U' F') D' L' U' R' U2 D' R`, 12 moves to DR.

</details>

**8c8e, example 12.** `D2 F2 L2 U F2 U' F2 D' B2 D B2 L2 B' R2 D R2 U F L' F' R'`

EO `U' B2 L' D2 F'`, no RZP needed: 8c8e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 2 (R/L stickers on U/D), 3 pair(s), 6 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (corner ARM 2, 3, 5 or 6: 55.8% of 8c8e, 9.8% sub-7).

Switched case: 8c8e, ARM 22, 3 pair(s) on 2 edge(s), 5 fake, 6 side pair(s).

Optimal DR on the inverse: `U R' U' L U2 D' L` (7 moves, not sub-7). The whole attempt: `U' B2 L' D2 F' (U R' U' L U2 D' L)`, 12 moves to DR.

</details>

**8c8e, example 13.** `R2 D' B2 L2 U' L2 D2 R2 F2 D' B2 L2 U F2 U B' R2 U' R L2 B L2 F`

EO `B2 U' F' L' B'`, no RZP needed: 8c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 3, corner ARM 5 (R/L stickers on U/D), 4 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (corner ARM 2, 3, 5 or 6: 55.8% of 8c8e, 9.8% sub-7).

Switched case: 8c8e, ARM 53, 4 pair(s) on 3 edge(s), 4 fake, 3 side pair(s).

Optimal DR on the inverse: `B2 L' U L D R L` (7 moves, not sub-7). The whole attempt: `B2 U' F' L' B' (B2 L' U L D R L)`, 12 moves to DR.

</details>

**8c8e, example 14.** `D2 L2 B2 L' B2 R' D2 F2 L' D2 F2 R' B2 D2 L' B' U' F' U L' R D B2 L'`

EO `R' U F U' B`, no RZP needed: 8c8e in 5. Traced before switching: 3 paired edge(s), edge ARM 2, corner ARM 6 (R/L stickers on U/D), 5 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (corner ARM 2, 3, 5 or 6: 55.8% of 8c8e, 9.8% sub-7).

Switched case: 8c8e, ARM 62, 5 pair(s) on 3 edge(s), 3 fake, 2 side pair(s).

Optimal DR on the inverse: `F2 R U' L' U2 D' L` (7 moves, not sub-7). The whole attempt: `R' U F U' B (F2 R U' L' U2 D' L)`, 12 moves to DR.

</details>

**8c8e, example 15.** `U2 F2 R D2 R' B2 L R2 F2 D2 R B2 F2 R' F' U' B2 F2 R' U L2 U' L R2`

EO `(R U2 L' B)`, RZP `(R')`, on the inverse scramble: 8c8e in 5. Traced before switching: 4 paired edge(s), edge ARM 3, corner ARM 3 (R/L stickers on U/D), 4 pair(s), 5 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (corner ARM 2, 3, 5 or 6: 55.8% of 8c8e, 9.8% sub-7).

Switched case: 8c8e, ARM 33, 4 pair(s) on 4 edge(s), 4 fake, 5 side pair(s).

Optimal DR on the normal side: `U D L D' R' U' D R` (8 moves, not sub-7). The whole attempt: `(R U2 L' B R') U D L D' R' U' D R`, 13 moves to DR.

</details>

**8c8e, example 16.** `U2 L2 F R2 F D2 B D2 B' D2 R2 F' D2 U' R' F' L D R' U2 L2 U2`

EO `R' L2 B2 L' F'`, no RZP needed: 8c8e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 6 (R/L stickers on U/D), 1 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (corner ARM 2, 3, 5 or 6: 55.8% of 8c8e, 9.8% sub-7).

Switched case: 8c8e, ARM 61, 1 pair(s) on 1 edge(s), 7 fake, 2 side pair(s).

Optimal DR on the inverse: `R U L D R' U F2 R` (8 moves, not sub-7). The whole attempt: `R' L2 B2 L' F' (R U L D R' U F2 R)`, 13 moves to DR.

</details>

## 2c2e

**2c2e, example 1.** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `B2 R2 B2 L B'`, no RZP needed: 2c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (a bad U/D edge with a pair: 23.2% of 2c2e, 59.6% sub-7).

Switched case: 2c2e, ARM 11, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the inverse: `U R F2 R' F2 U2 R` (7 moves, not sub-7). The whole attempt: `B2 R2 B2 L B' (U R F2 R' F2 U2 R)`, 12 moves to DR.

</details>

**2c2e, example 2.** `D B2 D2 B2 R2 D B2 D F2 R2 B2 U' B2 U' R2 F' U2 F2 L R2 F' R B' F'`

EO `R B' L' F`, RZP `R`: 2c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (a bad U/D edge with a pair: 23.2% of 2c2e, 59.6% sub-7).

Switched case: 2c2e, ARM 21, 2 pair(s) on 1 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the inverse: `D F2 R U2 R' F2 L` (7 moves, not sub-7). The whole attempt: `R B' L' F R (D F2 R U2 R' F2 L)`, 12 moves to DR.

</details>

**2c2e, example 3.** `D2 L2 B2 L2 F2 U' F2 R2 U2 F2 U' R2 U B' D R' L2 U' R D L2 U'`

EO `(R2 L2 B2 D2 F)`, no RZP needed, on the inverse scramble: 2c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (a bad U/D edge with a pair: 23.2% of 2c2e, 59.6% sub-7).

Switched case: 2c2e, ARM 10, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the normal side: `L' U' B2 U L` (5 moves, sub-7). The whole attempt: `(R2 L2 B2 D2 F) L' U' B2 U L`, 10 moves to DR.

</details>

**2c2e, example 4.** `D2 R D2 R' B2 L' F2 R2 B2 F2 R' B2 L' F' D' B2 F2 L' D F R2 U`

EO `B U L' U B'`, no RZP needed: 2c2e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (a bad U/D edge with a pair: 23.2% of 2c2e, 59.6% sub-7).

Switched case: 2c2e, ARM 21, 1 pair(s) on 1 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the inverse: `U' R' U' R U D' R` (7 moves, not sub-7). The whole attempt: `B U L' U B' (U' R' U' R U D' R)`, 12 moves to DR.

</details>

**2c2e, example 5.** `F2 R F2 R' D2 L' U2 R2 D2 U2 R' D2 L' U' F' D2 U2 L' F U R2 B`

EO `(F2 R' F2 R2 F')`, no RZP needed, on the inverse scramble: 2c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no pair, not JZP: 68.8% of 2c2e, 9.7% sub-7).

Switched case: 2c2e, ARM 21, 0 pair(s) on 0 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the normal side: `L' D L' D2 R D' R` (7 moves, not sub-7). The whole attempt: `(F2 R' F2 R2 F') L' D L' D2 R D' R`, 12 moves to DR.

</details>

**2c2e, example 6.** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `L B'`, RZP `L F2 L'`: 2c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 0 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no pair, not JZP: 68.8% of 2c2e, 9.7% sub-7).

Switched case: 2c2e, ARM 01, 0 pair(s) on 0 edge(s), 2 fake, 0 side pair(s).

Optimal DR on the inverse: `U L U L2 U2 F2 D R` (8 moves, not sub-7). The whole attempt: `L B' L F2 L' (U L U L2 U2 F2 D R)`, 13 moves to DR.

</details>

**2c2e, example 7.** `U2 B2 R F2 R B2 D2 R B2 R' F2 D2 L U2 R' B' D' B' F2 U L' B' R D R'`

EO `R B L' U2 F`, no RZP needed: 2c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no pair, not JZP: 68.8% of 2c2e, 9.7% sub-7).

Switched case: 2c2e, ARM 21, 0 pair(s) on 0 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the inverse: `R' F2 R F2 D R` (6 moves, sub-7). The whole attempt: `R B L' U2 F (R' F2 R F2 D R)`, 11 moves to DR.

</details>

**2c2e, example 8.** `L2 U2 B2 R U2 R' U2 L' D2 L D2 B2 D' F2 L F2 R U B' U' F'`

EO `(B' U' F)`, RZP `(U L)`, on the inverse scramble: 2c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 0, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no pair, not JZP: 68.8% of 2c2e, 9.7% sub-7).

Switched case: 2c2e, ARM 20, 0 pair(s) on 0 edge(s), 1 fake, 0 side pair(s).

Optimal DR on the normal side: `U' R' L U R' U L` (7 moves, not sub-7). The whole attempt: `(B' U' F U L) U' R' L U R' U L`, 12 moves to DR.

</details>

**2c2e, example 9.** `B2 D' L2 F2 U' F2 D2 B2 R2 D' L2 F2 U R2 U L' B2 U' B F2 L F2 R`

EO `B R' L' B'`, RZP `R'`: 2c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no pair, not JZP: 68.8% of 2c2e, 9.7% sub-7).

Switched case: 2c2e, ARM 21, 0 pair(s) on 0 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the inverse: `R2 U L' U L2 D' L` (7 moves, not sub-7). The whole attempt: `B R' L' B' R' (R2 U L' U L2 D' L)`, 12 moves to DR.

</details>

**2c2e, example 10.** `L2 U2 L2 D2 F2 D2 F2 B' D2 F' D2 R2 F' D' L' U2 F R2 D' L U' F2 B2`

EO `U L' D2 R' F'`, no RZP needed: 2c2e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (no pair, not JZP: 68.8% of 2c2e, 9.7% sub-7).

Switched case: 2c2e, ARM 21, 0 pair(s) on 0 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the inverse: `U D R U2 F2 R' U2 R` (8 moves, not sub-7). The whole attempt: `U L' D2 R' F' (U D R U2 F2 R' U2 R)`, 13 moves to DR.

</details>

## 4c6e

**4c6e, example 1.** `U2 R2 D' F2 R2 U2 R2 U' B2 R2 U2 R2 U F2 U' F' D F2 L2 U' R D F2 R'`

EO `(R2 D F)`, RZP `(D2 L)`, on the inverse scramble: 4c6e in 5. Traced before switching: 2 paired edge(s), edge ARM 0, corner ARM 0 (R/L stickers on U/D), 3 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (JZP: 0.61% of 4c6e, 61.1% sub-7).

Switched case: 4c6e, ARM 00, 3 pair(s) on 2 edge(s), 0 fake, 2 side pair(s), corners 4b-0, JZP.

Optimal DR on the normal side: `U2 F2 D2 R B2 L` (6 moves, sub-7). The whole attempt: `(R2 D F D2 L) U2 F2 D2 R B2 L`, 11 moves to DR.

</details>

**4c6e, example 2.** `R2 F' D2 R2 F D2 F R2 F' R2 F L2 B' D2 D' F R F2 L' D B R B F2`

EO `D' B2 U D' F'`, no RZP needed: 4c6e in 5. Traced before switching: 2 paired edge(s), edge ARM 0, corner ARM 0 (R/L stickers on U/D), 3 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (JZP: 0.61% of 4c6e, 61.1% sub-7).

Switched case: 4c6e, ARM 00, 3 pair(s) on 2 edge(s), 0 fake, 3 side pair(s), corners 4b-0, JZP.

Optimal DR on the inverse: `U2 F2 B2 R U2 L` (6 moves, sub-7). The whole attempt: `D' B2 U D' F' (U2 F2 B2 R U2 L)`, 11 moves to DR.

</details>

**4c6e, example 3.** `F R2 B2 U2 L2 R2 B L2 F' U2 B R2 U2 L2 B' R' B' R' D L' F2 R D' B2`

EO `U' L2 U2 F`, RZP `L'`: 4c6e in 5. Traced before switching: 2 paired edge(s), edge ARM 0, corner ARM 0 (R/L stickers on U/D), 3 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (JZP: 0.61% of 4c6e, 61.1% sub-7).

Switched case: 4c6e, ARM 00, 3 pair(s) on 2 edge(s), 0 fake, 3 side pair(s), corners 4b-0, JZP.

Optimal DR on the inverse: `U2 B2 R U2 L` (5 moves, sub-7). The whole attempt: `U' L2 U2 F L' (U2 B2 R U2 L)`, 10 moves to DR.

</details>

**4c6e, example 4.** `U2 F D2 R2 D2 U2 B' U2 B2 L2 B L2 B R2 F' U' B R D' L2 B' L' B' U B2`

EO `B R L B'`, RZP `R`: 4c6e in 5. Traced before switching: 1 paired edge(s), edge ARM 0, corner ARM 0 (R/L stickers on U/D), 2 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (JZP: 0.61% of 4c6e, 61.1% sub-7).

Switched case: 4c6e, ARM 00, 2 pair(s) on 1 edge(s), 0 fake, 3 side pair(s), corners 4a-0, JZP.

Optimal DR on the inverse: `R F2 U2 B2 R' D2 R` (7 moves, not sub-7). The whole attempt: `B R L B' R (R F2 U2 B2 R' D2 R)`, 12 moves to DR.

</details>

**4c6e, example 5.** `L' D2 R' U2 R D2 B2 R U2 L' D2 R D2 R F' D U' L' U' B' D' F2 U2`

EO `D B' D' R F`, no RZP needed: 4c6e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 4 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 1.2% of 4c6e, 47.9% sub-7).

Switched case: 4c6e, ARM 42, 4 pair(s) on 2 edge(s), 1 fake, 0 side pair(s), corners 4a-4.

Optimal DR on the inverse: `U R U2 D2 L' D' L` (7 moves, not sub-7). The whole attempt: `D B' D' R F (U R U2 D2 L' D' L)`, 12 moves to DR.

</details>

**4c6e, example 6.** `U2 R2 F' B2 L2 B' U2 F L2 B' L2 D2 L2 R2 U' L F2 D' U R U' F`

EO `(F L B)`, RZP `(U' L')`, on the inverse scramble: 4c6e in 5. Traced before switching: 3 paired edge(s), edge ARM 3, corner ARM 4 (R/L stickers on U/D), 4 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 1.2% of 4c6e, 47.9% sub-7).

Switched case: 4c6e, ARM 43, 4 pair(s) on 3 edge(s), 0 fake, 0 side pair(s), corners 4b-0.

Optimal DR on the normal side: `U' D R U2 L` (5 moves, sub-7). The whole attempt: `(F L B U' L') U' D R U2 L`, 10 moves to DR.

</details>

**4c6e, example 7.** `R2 B R2 U2 L2 B' U2 F2 D2 U2 F D2 B2 R' F2 B U F B U B2 R`

EO `R' F' U B`, RZP `R'`: 4c6e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 0 (R/L stickers on U/D), 4 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 1.2% of 4c6e, 47.9% sub-7).

Switched case: 4c6e, ARM 01, 4 pair(s) on 2 edge(s), 1 fake, 3 side pair(s), corners 4a-0.

Optimal DR on the inverse: `U2 R' U' R U2 D2 L` (7 moves, not sub-7). The whole attempt: `R' F' U B R' (U2 R' U' R U2 D2 L)`, 12 moves to DR.

</details>

**4c6e, example 8.** `L2 U2 L2 D2 F2 D2 F2 B' D2 F' D2 R2 F' D' L' U2 F R2 D' L U' F2 B2`

EO `R L B`, RZP `D2 R'`: 4c6e in 5. Traced before switching: 3 paired edge(s), edge ARM 2, corner ARM 2 (R/L stickers on U/D), 4 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 1.2% of 4c6e, 47.9% sub-7).

Switched case: 4c6e, ARM 22, 4 pair(s) on 3 edge(s), 0 fake, 1 side pair(s), corners 4a-2.

Optimal DR on the inverse: `U D2 B2 R' B2 L` (6 moves, sub-7). The whole attempt: `R L B D2 R' (U D2 B2 R' B2 L)`, 11 moves to DR.

</details>

**4c6e, example 9.** `D2 R D2 R' B2 L' F2 R2 B2 F2 R' B2 L' F' D' B2 F2 L' D F R2 U`

EO `B R D' R F`, no RZP needed: 4c6e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 2 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (anything else: 98.2% of 4c6e, 3.7% sub-7).

Switched case: 4c6e, ARM 22, 2 pair(s) on 2 edge(s), 3 fake, 1 side pair(s), corners 4b-2.

Optimal DR on the inverse: `U D2 R' F2 U L' D L` (8 moves, not sub-7). The whole attempt: `B R D' R F (U D2 R' F2 U L' D L)`, 13 moves to DR.

</details>

**4c6e, example 10.** `U2 R2 F' B2 L2 B' U2 F L2 B' L2 D2 L2 R2 U' L F2 D' U R U' F`

EO `F R' F2 L2 B`, no RZP needed: 4c6e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (anything else: 98.2% of 4c6e, 3.7% sub-7).

Switched case: 4c6e, ARM 32, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U R U2 D R2 B2 R` (7 moves, not sub-7). The whole attempt: `F R' F2 L2 B (U R U2 D R2 B2 R)`, 12 moves to DR.

</details>

**4c6e, example 11.** `U2 L2 U2 R2 B2 R2 B2 F' R2 B' R2 D2 B' R' U' L2 B D2 R' U L' B2 F2`

EO `D2 F2 U D' F`, no RZP needed: 4c6e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (anything else: 98.2% of 4c6e, 3.7% sub-7).

Switched case: 4c6e, ARM 31, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `L' F2 U' D L' F2 U' L` (8 moves, not sub-7). The whole attempt: `D2 F2 U D' F (L' F2 U' D L' F2 U' L)`, 13 moves to DR.

</details>

**4c6e, example 12.** `B2 D2 R2 B2 D F2 R2 D' L2 D L2 B2 D F2 U R' F' D' B2 L D2 B D2 F D'`

EO `(F R2 L2 U2 F')`, no RZP needed, on the inverse scramble: 4c6e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 2 (R/L stickers on U/D), 2 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (anything else: 98.2% of 4c6e, 3.7% sub-7).

Switched case: 4c6e, ARM 22, 2 pair(s) on 2 edge(s), 0 fake, 2 side pair(s), corners 4b-2.

Optimal DR on the normal side: `U F2 D' R F2 U2 D2 R` (8 moves, not sub-7). The whole attempt: `(F R2 L2 U2 F') U F2 D' R F2 U2 D2 R`, 13 moves to DR.

</details>

**4c6e, example 13.** `R2 F2 L' U2 F2 R2 F2 R' D2 F2 R2 F2 R U2 R' U' L U2 B2 R' F L U2 F'`

EO `L2 B L' D2 B'`, no RZP needed: 4c6e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (anything else: 98.2% of 4c6e, 3.7% sub-7).

Switched case: 4c6e, ARM 11, 1 pair(s) on 1 edge(s), 2 fake, 2 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U F2 L U' B2 R2 D2 L` (8 moves, not sub-7). The whole attempt: `L2 B L' D2 B' (U F2 L U' B2 R2 D2 L)`, 13 moves to DR.

</details>

**4c6e, example 14.** `F2 U2 R F2 D2 F2 U2 L' F2 L2 R D2 U' R D R2 D F R2 F R`

EO `D' F L' F'`, RZP `R`: 4c6e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 3 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (anything else: 98.2% of 4c6e, 3.7% sub-7).

Switched case: 4c6e, ARM 32, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s), corners 4c-1.

Optimal DR on the inverse: `U D' L' D R' L U2 D' R` (9 moves, not sub-7). The whole attempt: `D' F L' F' R (U D' L' D R' L U2 D' R)`, 14 moves to DR.

</details>

## 3c4e

**3c4e, example 1.** `R2 L2 D F2 U F2 U R2 F2 L2 B2 D B' U B R' D' F' D' U' B U'`

EO `(F' L' B L B)`, no RZP needed, on the inverse scramble: 3c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (2 pairs: 10.7% of 3c4e, 33.7% sub-7).

Switched case: 3c4e, ARM 21, 2 pair(s) on 2 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the normal side: `R' U2 F2 D' L` (5 moves, sub-7). The whole attempt: `(F' L' B L B) R' U2 F2 D' L`, 10 moves to DR.

</details>

**3c4e, example 2.** `R2 D2 B U2 F2 R2 B D2 B' D2 B L2 D2 D' L F L D' F L' D' R' F'`

EO `B U L F`, RZP `L'`: 3c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 3 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (2 pairs: 10.7% of 3c4e, 33.7% sub-7).

Switched case: 3c4e, ARM 32, 2 pair(s) on 2 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the inverse: `L F2 L D R U F2 R` (8 moves, not sub-7). The whole attempt: `B U L F L' (L F2 L D R U F2 R)`, 13 moves to DR.

</details>

**3c4e, example 3.** `D2 B L2 B2 F D2 F2 D2 L2 D2 B' D2 F R' D2 B' U' F' R2 U' R D`

EO `B2 D' B R' F'`, no RZP needed: 3c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (2 pairs: 10.7% of 3c4e, 33.7% sub-7).

Switched case: 3c4e, ARM 21, 2 pair(s) on 2 edge(s), 1 fake, 0 side pair(s).

Optimal DR on the inverse: `R' U2 B2 U' R` (5 moves, sub-7). The whole attempt: `B2 D' B R' F' (R' U2 B2 U' R)`, 10 moves to DR.

</details>

**3c4e, example 4.** `U2 F2 U2 B2 L2 B2 L2 R' B2 L' B2 D2 L' B' U' F2 L D2 B' U F' L2 R2`

EO `D F2 B U2 F`, no RZP needed: 3c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (2 pairs: 10.7% of 3c4e, 33.7% sub-7).

Switched case: 3c4e, ARM 11, 2 pair(s) on 2 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the inverse: `R2 U R U2 F2 D' L` (7 moves, not sub-7). The whole attempt: `D F2 B U2 F (R2 U R U2 F2 D' L)`, 12 moves to DR.

</details>

**3c4e, example 5.** `D2 F2 L2 F2 R2 U' R2 B2 U2 R2 U' B2 U L' D B' F2 U' B D F2 U'`

EO `B' U2 B`, RZP `U L`: 3c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (2 pairs: 10.7% of 3c4e, 33.7% sub-7).

Switched case: 3c4e, ARM 11, 2 pair(s) on 2 edge(s), 0 fake, 1 side pair(s).

Optimal DR on the inverse: `U' D2 L D' L' D' L` (7 moves, not sub-7). The whole attempt: `B' U2 B U L (U' D2 L D' L' D' L)`, 12 moves to DR.

</details>

**3c4e, example 6.** `D2 R D2 R' B2 L' F2 R2 B2 F2 R' B2 L' F' D' B2 F2 L' D F R2 U`

EO `U2 B R2 D2 F`, no RZP needed: 3c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (0 or 1 pair: 89.3% of 3c4e, 7.1% sub-7).

Switched case: 3c4e, ARM 11, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the inverse: `U' L D' L U2 D' R` (7 moves, not sub-7). The whole attempt: `U2 B R2 D2 F (U' L D' L U2 D' R)`, 12 moves to DR.

</details>

**3c4e, example 7.** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `L B`, RZP `R2 B2 L'`: 3c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (0 or 1 pair: 89.3% of 3c4e, 7.1% sub-7).

Switched case: 3c4e, ARM 21, 1 pair(s) on 1 edge(s), 2 fake, 1 side pair(s).

Optimal DR on the inverse: `L2 D2 R F2 B2 D' L` (7 moves, not sub-7). The whole attempt: `L B R2 B2 L' (L2 D2 R F2 B2 D' L)`, 12 moves to DR.

</details>

**3c4e, example 8.** `U2 R2 D' F2 R2 U2 R2 U' B2 R2 U2 R2 U F2 U' F' D F2 L2 U' R D F2 R'`

EO `(U' D R' U F)`, no RZP needed, on the inverse scramble: 3c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (0 or 1 pair: 89.3% of 3c4e, 7.1% sub-7).

Switched case: 3c4e, ARM 21, 0 pair(s) on 0 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the normal side: `U2 L2 D2 L' F2 B2 U' R` (8 moves, not sub-7). The whole attempt: `(U' D R' U F) U2 L2 D2 L' F2 B2 U' R`, 13 moves to DR.

</details>

**3c4e, example 9.** `L2 U2 B2 R U2 R' U2 L' D2 L D2 B2 D' F2 L F2 R U B' U' F'`

EO `(U2 L2 F' U' B)`, no RZP needed, on the inverse scramble: 3c4e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 0 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (0 or 1 pair: 89.3% of 3c4e, 7.1% sub-7).

Switched case: 3c4e, ARM 11, 0 pair(s) on 0 edge(s), 0 fake, 1 side pair(s).

Optimal DR on the normal side: `D2 L' U' B2 R2 U D2 L` (8 moves, not sub-7). The whole attempt: `(U2 L2 F' U' B) D2 L' U' B2 R2 U D2 L`, 13 moves to DR.

</details>

**3c4e, example 10.** `U2 L2 U2 R2 B2 R2 B2 F' R2 B' R2 D2 B' R' U' L2 B D2 R' U L' B2 F2`

EO `R' L' U' D' F`, no RZP needed: 3c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 1 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (0 or 1 pair: 89.3% of 3c4e, 7.1% sub-7).

Switched case: 3c4e, ARM 21, 1 pair(s) on 1 edge(s), 1 fake, 0 side pair(s).

Optimal DR on the inverse: `R2 D2 R' F2 L' U' L` (7 moves, not sub-7). The whole attempt: `R' L' U' D' F (R2 D2 R' F2 L' U' L)`, 12 moves to DR.

</details>

## 3c6e

**3c6e, example 1.** `B D2 F2 L2 U2 D2 F U2 B' L2 F D2 L2 U2 F' D' F' D' R U' B2 D R' F2`

EO `(L F2 L2 D B)`, no RZP needed, on the inverse scramble: 3c6e in 5. Traced before switching: 0 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 0 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (always: 100.0% of 3c6e, 4.8% sub-7).

Switched case: 3c6e, ARM 11, 0 pair(s) on 0 edge(s), 1 fake, 2 side pair(s).

Optimal DR on the normal side: `D2 R F2 D R U' L2 D R` (9 moves, not sub-7). The whole attempt: `(L F2 L2 D B) D2 R F2 D R U' L2 D R`, 14 moves to DR.

</details>

**3c6e, example 2.** `L2 U2 L2 D2 F2 D2 F2 B' D2 F' D2 R2 F' D' L' U2 F R2 D' L U' F2 B2`

EO `R2 B' R' L B`, no RZP needed: 3c6e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (always: 100.0% of 3c6e, 4.8% sub-7).

Switched case: 3c6e, ARM 11, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the inverse: `U R D' R2 F2 R2 B2 D' L` (9 moves, not sub-7). The whole attempt: `R2 B' R' L B (U R D' R2 F2 R2 B2 D' L)`, 14 moves to DR.

</details>

**3c6e, example 3.** `B2 F2 D R2 U R2 U B2 R2 F2 L2 D L' U L B' D' R' D' U' L U'`

EO `U2 B L2 U' B`, no RZP needed: 3c6e in 5. Traced before switching: 2 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 2 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (always: 100.0% of 3c6e, 4.8% sub-7).

Switched case: 3c6e, ARM 10, 2 pair(s) on 2 edge(s), 1 fake, 2 side pair(s).

Optimal DR on the inverse: `U2 R' F2 L U F2 U' L` (8 moves, not sub-7). The whole attempt: `U2 B L2 U' B (U2 R' F2 L U F2 U' L)`, 13 moves to DR.

</details>

**3c6e, example 4.** `U2 R' B2 R D2 L' U2 L U2 F2 U2 B2 R' D2 R2 U' F R D' L U' D2 R2 F U R'`

EO `F' U D B'`, RZP `L'`: 3c6e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 1 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (always: 100.0% of 3c6e, 4.8% sub-7).

Switched case: 3c6e, ARM 12, 1 pair(s) on 1 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the inverse: `U2 D2 B2 D' B2 L' U2 D' R` (9 moves, not sub-7). The whole attempt: `F' U D B' L' (U2 D2 B2 D' B2 L' U2 D' R)`, 14 moves to DR.

</details>

## 5c4e

**5c4e, example 1.** `D2 R D2 F2 U2 R' F2 L2 B2 F2 L B2 R2 D' L2 R F L R F R2 D`

EO `(F2 R' L2 U2 F)`, no RZP needed, on the inverse scramble: 5c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 3 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (3 pairs: 6.1% of 5c4e, 27.6% sub-7).

Switched case: 5c4e, ARM 42, 3 pair(s) on 2 edge(s), 0 fake, 1 side pair(s).

Optimal DR on the normal side: `U D L U' D R' U' R` (8 moves, not sub-7). The whole attempt: `(F2 R' L2 U2 F) U D L U' D R' U' R`, 13 moves to DR.

</details>

**5c4e, example 2.** `L B2 L2 B2 D2 L B2 L F2 D2 B2 R' B2 R' D2 F' R2 F2 U D2 F' D B' F'`

EO `D' B U' F'`, RZP `R`: 5c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 3 (R/L stickers on U/D), 3 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (3 pairs: 6.1% of 5c4e, 27.6% sub-7).

Switched case: 5c4e, ARM 32, 3 pair(s) on 2 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the inverse: `D R U R F2 D' L` (7 moves, not sub-7). The whole attempt: `D' B U' F' R (D R U R F2 D' L)`, 12 moves to DR.

</details>

**5c4e, example 3.** `D2 F2 L2 F2 R2 U' R2 B2 U2 R2 U' B2 U L' D B' F2 U' B D F2 U'`

EO `F2 L F L F'`, no RZP needed: 5c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 0, corner ARM 1 (R/L stickers on U/D), 3 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (3 pairs: 6.1% of 5c4e, 27.6% sub-7).

Switched case: 5c4e, ARM 10, 3 pair(s) on 2 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the inverse: `U2 L U' L' U' D2 L` (7 moves, not sub-7). The whole attempt: `F2 L F L F' (U2 L U' L' U' D2 L)`, 12 moves to DR.

</details>

**5c4e, example 4.** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `U2 L U2 B'`, RZP `R'`: 5c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 4 (R/L stickers on U/D), 1 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (2 pairs or fewer: 93.9% of 5c4e, 5.9% sub-7).

Switched case: 5c4e, ARM 41, 1 pair(s) on 1 edge(s), 3 fake, 1 side pair(s).

Optimal DR on the inverse: `U R2 D' B2 R' D' B2 R` (8 moves, not sub-7). The whole attempt: `U2 L U2 B' R' (U R2 D' B2 R' D' B2 R)`, 13 moves to DR.

</details>

**5c4e, example 5.** `F2 R F2 U2 B2 R' U2 L2 D2 U2 L D2 R2 F' L2 R U L R U R2 F`

EO `L U2 F`, RZP `U2 R'`: 5c4e in 5. Traced before switching: 1 paired edge(s), edge ARM 1, corner ARM 4 (R/L stickers on U/D), 2 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (2 pairs or fewer: 93.9% of 5c4e, 5.9% sub-7).

Switched case: 5c4e, ARM 41, 2 pair(s) on 1 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the inverse: `B2 U2 B2 D L' U B2 L` (8 moves, not sub-7). The whole attempt: `L U2 F U2 R' (B2 U2 B2 D L' U B2 L)`, 13 moves to DR.

</details>

**5c4e, example 6.** `U2 L2 F2 R B2 D2 R B2 F2 L D2 R2 D2 D' F' R B R2 U' F' D' B'`

EO `(U' D2 F B')`, RZP `(R')`, on the inverse scramble: 5c4e in 5. Traced before switching: 2 paired edge(s), edge ARM 1, corner ARM 4 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (2 pairs or fewer: 93.9% of 5c4e, 5.9% sub-7).

Switched case: 5c4e, ARM 41, 2 pair(s) on 2 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the normal side: `U2 F2 D B2 L' D' F2 L` (8 moves, not sub-7). The whole attempt: `(U' D2 F B' R') U2 F2 D B2 L' D' F2 L`, 13 moves to DR.

</details>

## 5c6e

**5c6e, example 1.** `R2 D2 L' F2 D2 R2 D2 R' B2 D2 R2 D2 R F2 R' F' L F2 U2 R' D L F2 D'`

EO `(B2 L F2 U2 F')`, no RZP needed, on the inverse scramble: 5c6e in 5. Traced before switching: 3 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 4 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 3.1% of 5c6e, 37.9% sub-7).

Switched case: 5c6e, ARM 42, 4 pair(s) on 3 edge(s), 2 fake, 1 side pair(s).

Optimal DR on the normal side: `U' D' L U R' U L` (7 moves, not sub-7). The whole attempt: `(B2 L F2 U2 F') U' D' L U R' U L`, 12 moves to DR.

</details>

**5c6e, example 2.** `D' R2 U' L2 U R2 B2 U L2 D' R2 U R2 U F' R L' D' L' B' R' F2 L2`

EO `F U D2 L2 F`, no RZP needed: 5c6e in 5. Traced before switching: 3 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 4 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (4 pairs: 3.1% of 5c6e, 37.9% sub-7).

Switched case: 5c6e, ARM 42, 4 pair(s) on 3 edge(s), 2 fake, 0 side pair(s).

Optimal DR on the inverse: `D' R' U R' D2 L` (6 moves, sub-7). The whole attempt: `F U D2 L2 F (D' R' U R' D2 L)`, 11 moves to DR.

</details>

**5c6e, example 3.** `B2 L2 U2 F L2 F' L2 B' R2 B R2 U2 R' D2 B D2 F L U' L' D'`

EO `(U' R F2 L2 B)`, no RZP needed, on the inverse scramble: 5c6e in 5. Traced before switching: 2 paired edge(s), edge ARM 2, corner ARM 4 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 96.9% of 5c6e, 5.1% sub-7).

Switched case: 5c6e, ARM 42, 2 pair(s) on 2 edge(s), 2 fake, 1 side pair(s).

Optimal DR on the normal side: `U B2 D R B2 D' L` (7 moves, not sub-7). The whole attempt: `(U' R F2 L2 B) U B2 D R B2 D' L`, 12 moves to DR.

</details>

**5c6e, example 4.** `R2 U R2 U' B2 D' F2 U2 B2 F2 U' B2 D' F' R' B2 F2 D' R F U2 L`

EO `B R' U R' F'`, no RZP needed: 5c6e in 5. Traced before switching: 1 paired edge(s), edge ARM 3, corner ARM 3 (R/L stickers on U/D), 2 pair(s), 1 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (3 pairs or fewer: 96.9% of 5c6e, 5.1% sub-7).

Switched case: 5c6e, ARM 33, 2 pair(s) on 1 edge(s), 1 fake, 1 side pair(s).

Optimal DR on the inverse: `R D R L U R' B2 L` (8 moves, not sub-7). The whole attempt: `B R' U R' F' (R D R L U R' B2 L)`, 13 moves to DR.

</details>

## 6c6e

**6c6e, example 1.** `D2 F2 L2 F2 R2 U' R2 B2 U2 R2 U' B2 U L' D B' F2 U' B D F2 U'`

EO `F' L2 F'`, RZP `R2 L`: 6c6e in 5. Traced before switching: 3 paired edge(s), edge ARM 1, corner ARM 2 (R/L stickers on U/D), 5 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (JZP, or 5 or 6 pairs: 1.3% of 6c6e, 39.0% sub-7).

Switched case: 6c6e, ARM 21, 5 pair(s) on 3 edge(s), 1 fake, 3 side pair(s).

Optimal DR on the inverse: `R F2 R' F2 L2 U' L` (7 moves, not sub-7). The whole attempt: `F' L2 F' R2 L (R F2 R' F2 L2 U' L)`, 12 moves to DR.

</details>

**6c6e, example 2.** `B2 U L2 D R2 B2 D F2 U F2 D2 R2 U' R' F' R' U' L' D' F U2 F' R'`

EO `F R2 D' L' B'`, no RZP needed: 6c6e in 5. Traced before switching: 3 paired edge(s), edge ARM 3, corner ARM 6 (R/L stickers on U/D), 6 pair(s), 0 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **your call** (JZP, or 5 or 6 pairs: 1.3% of 6c6e, 39.0% sub-7).

Switched case: 6c6e, ARM 63, 6 pair(s) on 3 edge(s), 0 fake, 0 side pair(s).

Optimal DR on the inverse: `R U R D' L` (5 moves, sub-7). The whole attempt: `F R2 D' L' B' (R U R D' L)`, 10 moves to DR.

</details>

**6c6e, example 3.** `R2 F2 L' U2 F2 R2 F2 R' D2 F2 R2 F2 R U2 R' U' L U2 B2 R' F L U2 F'`

EO `L2 U R D2 B'`, no RZP needed: 6c6e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 3 (R/L stickers on U/D), 2 pair(s), 3 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (anything else: 98.7% of 6c6e, 5.2% sub-7).

Switched case: 6c6e, ARM 32, 2 pair(s) on 1 edge(s), 2 fake, 3 side pair(s).

Optimal DR on the inverse: `U L' B2 L' F2 U R L` (8 moves, not sub-7). The whole attempt: `L2 U R D2 B' (U L' B2 L' F2 U R L)`, 13 moves to DR.

</details>

**6c6e, example 4.** `U2 R' B2 R D2 L' U2 L U2 F2 U2 B2 R' D2 R2 U' F R D' L U' D2 R2 F U R'`

EO `(L U F' U B)`, no RZP needed, on the inverse scramble: 6c6e in 5. Traced before switching: 1 paired edge(s), edge ARM 2, corner ARM 3 (R/L stickers on U/D), 2 pair(s), 2 side pair(s).

<details><summary>Verdict and the DR after the switch</summary>

Card: **discard** (anything else: 98.7% of 6c6e, 5.2% sub-7).

Switched case: 6c6e, ARM 32, 2 pair(s) on 1 edge(s), 2 fake, 2 side pair(s).

Optimal DR on the normal side: `R D' L F2 B2 U2 D' L` (8 moves, not sub-7). The whole attempt: `(L U F' U B) R D' L F2 B2 U2 D' L`, 13 moves to DR.

</details>
