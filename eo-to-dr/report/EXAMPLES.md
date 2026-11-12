# Worked examples: EO to DR, and scramble to DR

Examples to play along with the write-up ([WRITEUP.md](WRITEUP.md)). Try a scramble, then open the answers.

**Part 1** is 150 uniformly random scrambles, the first 150 of the study's 50,000 (made by the study itself, not by nissy's `scramble`; see the write-up, appendix B). For each one: the bad edges on each axis, how many EOs of at most 4 and at most 5 turns it has, and, folded away, its shortest DR (normal, inverse, best of six, NISS) and the best DR through an EO of at most 4 and of at most 5 turns. **Part 2** is 60 EO-solved states by case: a scramble and an EO, then how far DR is on each of the two DR axes, on the inverse, and with the EO's last turn the other way.

How to read it. Turns are face turns (HTM). *Normal* means turns after the scramble, *inverse* turns after the inverse scramble, written in brackets as usual for NISS: `R U (F D)` is `R U` on the normal side and `F D` on the inverse. A *route through an EO* is the EO, then turns that keep it (no quarter turns of the EO's axis) to DR on one of the two other axes, on the same side. "EOs of at most 4 turns" counts every move sequence that solves EO for the first time at its last turn, both directions of the last turn counted, as nissy's `-a` lists them (nissy's default listing shows about half of these). A *NISS EO* has turns on both sides. A case like 4c4e names the bad corners and the edges out of place for that DR axis (slice edges outside the slice, and as many other edges inside it), as in Cale's "DR setup stats" sheet.

Every answer is exact: a shortest DR is the fewest turns there are (from exact distance tables), and a "best DR through an EO" is the best over every EO of that length or shorter. "For example" gives one of the shortest; there are usually several.

**Replay check.** Every move sequence on this page was replayed on the sticker model before the page was written: 2,242 checks (each EO is an EO on its axis, each DR is a DR on its axis with the stated number of turns, DR turns after an EO keep it, each case and bad-edge count is read off the stickers), 0 mismatches.

In these 150: best of six 8.75 on average, NISS 8.47 (the 50,000 give 8.76 and 8.46).

## Part 1. 150 scrambles

### Scramble 1

`U2 R2 D L2 R2 D' R2 U' L2 D R2 U F2 R' D' F2 L' D R D' B' R2 D'`

Bad edges on R/L, U/D, F/B: 6, 10, 4. EOs of at most 4 turns (all three axes): 26 normal, 24 inverse, 4 NISS with turns on both sides; of at most 5: 180, 172, 184.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `R' D B L' R U' R F2 D` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(L U' B U2 L' F2 R B2 U' L)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `R' D B L' R U' R F2 D` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `D' L2 U2 F'` on F/B, then `R' U D' L D` to DR on R/L; through an inverse EO: 10, `(L U' B)` on F/B, then `(U2 L' F2 R B2 U' L)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `D' L2 U2 F'` on F/B, then `R' U D' L D` to DR on R/L; through an inverse EO: 10, `(L U' B)` on F/B, then `(U2 L' F2 R B2 U' L)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 2

`B2 L2 R2 U R2 D2 B2 L2 R2 U F2 U R2 D2 B' R' U B' L' U R2 B D2`

Bad edges on R/L, U/D, F/B: 8, 6, 6. EOs of at most 4 turns (all three axes): 0 normal, 4 inverse, 0 NISS with turns on both sides; of at most 5: 58, 100, 92.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 9, F/B 11), for example `F' D R' B2 U B' L2 D` (DR on R/L).
- On the inverse: 8 (per axis: R/L 9, U/D 10, F/B 8), for example `(L U' B2 D R' U' B' L)` (DR on F/B).
- Best of the six: 8. With NISS: 8, for example `F' D R' B2 U B' L2 D` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; through an inverse EO: 11, `(U D L' U')` on U/D, then `(L2 F R B L2 F' R)` to DR on F/B; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U2 F' R D' L` on R/L, then `F2 D' B2 U B` to DR on U/D; through an inverse EO: 10, `(L2 D' B2 R' U')` on U/D, then `(L' U2 R2 F L)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 3

`L2 D2 U' F2 L2 U' L2 B2 U' R2 B2 L2 R' D L F' D F2 D' F2`

Bad edges on R/L, U/D, F/B: 8, 4, 4. EOs of at most 4 turns (all three axes): 64 normal, 48 inverse, 12 NISS with turns on both sides; of at most 5: 650, 380, 276.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 9, U/D 8, F/B 10), for example `F2 D F2 D' F L' D' R` (DR on U/D).
- On the inverse: 8 (per axis: R/L 9, U/D 8, F/B 10), for example `(R' D R2 L' D B2 U' B)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `F2 D F2 D' F L' D' R` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `F L D' R` on R/L, then `L2 D' F' D' F` to DR on U/D; through an inverse EO: 8, `(R' D R2 L')` on R/L, then `(D B2 U' B)` to DR on U/D; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 8, EO `F2 D F2 D' F` on F/B, then `L' D' R` to DR on U/D; through an inverse EO: 8, `(R' D R2 L')` on R/L, then `(D B2 U' B)` to DR on U/D; with NISS EOs too: 8.

</details>

### Scramble 4

`U R2 F2 R2 F2 U B2 U2 R2 D' F2 L2 U' R' U' F' U' R2 B' F2 D' R`

Bad edges on R/L, U/D, F/B: 6, 4, 6. EOs of at most 4 turns (all three axes): 12 normal, 24 inverse, 36 NISS with turns on both sides; of at most 5: 190, 284, 316.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `B R D B' D2 L' F2 U2 F` (DR on U/D).
- On the inverse: 8 (per axis: R/L 8, U/D 9, F/B 10), for example `(L' F2 L F' R B2 U' B)` (DR on R/L).
- Best of the six: 8. With NISS: 8, for example `(L' F2 L F' R B2 U' B)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `R' F' L' D'` on U/D, then `R2 B' L R F2 R B` to DR on R/L; through an inverse EO: 10, `(U R2 F2 D)` on U/D, then `(B' D2 F U2 L B)` to DR on R/L; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `R D2 R2 B' L'` on R/L, then `U2 D B' R2 B` to DR on U/D; through an inverse EO: 9, `(U R' F R' D)` on U/D, then `(R2 B D2 B)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 5

`D2 R2 F2 L2 U' L2 R2 U' B2 D B2 R2 U2 B' L2 F' R U2 B L2 F L' U'`

Bad edges on R/L, U/D, F/B: 6, 6, 8. EOs of at most 4 turns (all three axes): 12 normal, 0 inverse, 12 NISS with turns on both sides; of at most 5: 190, 88, 228.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 10, F/B 10), for example `F2 U D L' F' R' B D` (DR on R/L).
- On the inverse: 8 (per axis: R/L 10, U/D 8, F/B 10), for example `(L' B' U' R F R' U2 L)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `F2 U D L' F' R' B D` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `R F R L` on R/L, then `F' D F' L2 U' D2 F` to DR on U/D; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `R F D2 R' L` on R/L, then `U F2 L2 F D` to DR on F/B; through an inverse EO: 8, `(L' B' U' R F)` on F/B, then `(R' U2 L)` to DR on U/D; with NISS EOs too: 8.

</details>

### Scramble 6

`B2 U L2 F2 R2 D2 R2 U F2 U2 B2 U R2 L' B' F2 R' D F2 U' F' D2`

Bad edges on R/L, U/D, F/B: 6, 4, 8. EOs of at most 4 turns (all three axes): 2 normal, 32 inverse, 24 NISS with turns on both sides; of at most 5: 66, 244, 284.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `D2 F U F2 D' R F2 B L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(F D F2 D L F D2 R D)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `D2 F U F2 D' R F2 B L` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `L F' B D` on U/D, then `L R B L2 D2 R B` to DR on R/L; through an inverse EO: 10, `(R2 B' R' D)` on U/D, then `(F B2 L' B' U2 L)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L' B L F' D'` on U/D, then `L F' U2 R' F` to DR on R/L; through an inverse EO: 10, `(R2 B' R' D)` on U/D, then `(F B2 L' B' U2 L)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 7

`B2 F2 U2 B2 L2 U' B2 U' B2 U L2 U' B2 F' D2 U L D2 B' U' L U'`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 18 normal, 14 inverse, 24 NISS with turns on both sides; of at most 5: 256, 238, 248.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `U L' U B D2 L' U' D2 F` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `(F B2 U' F2 D' R2 U2 F' L)` (DR on F/B).
- Best of the six: 9. With NISS: 8, for example `F U' R' B2 D' R B (U)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U D2 F' L'` on R/L, then `F' R2 D' B U L2 D` to DR on F/B; through an inverse EO: 11, `(D' L' F U)` on U/D, then `(B2 L' B' R2 F' D2 L)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U F U2 B2 R` on R/L, then `D' B F' U F` to DR on U/D; through an inverse EO: 9, `(F B2 U' F2 D')` on U/D, then `(R2 U2 F' L)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 8

`B2 U2 L2 R2 D B2 D F2 U2 L2 U' R2 U' R2 U' B' D2 R' B2 F' R2 U F2 L R'`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 4 normal, 2 inverse, 0 NISS with turns on both sides; of at most 5: 54, 60, 116.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 11, U/D 10, F/B 10), for example `R L' F2 U' R2 F B2 R D2 B` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `(F2 R' D F' B2 U' R' U2 L)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `(U R2 D' L U2 B R' L2 F)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `R' F U2 L'` on R/L, then `F D2 F' B' U F2 D` to DR on F/B; through an inverse EO: 11, `(U R2 F D)` on U/D, then `(F' L' B' R' D2 B R)` to DR on F/B; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `R2 F R U2 L'` on R/L, then `D R2 F U' D F` to DR on U/D; through an inverse EO: 11, `(U R2 F D)` on U/D, then `(F' L' B' R' D2 B R)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 9

`F2 L2 R2 U2 L2 U' F2 D' B2 R2 D' F2 U R U L2 B L F' D F R' U'`

Bad edges on R/L, U/D, F/B: 8, 8, 6. EOs of at most 4 turns (all three axes): 0 normal, 16 inverse, 40 NISS with turns on both sides; of at most 5: 52, 116, 236.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `D L' D2 B' R2 L2 U' R D` (DR on F/B).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(L' D F' U R' F R2 B2 L' B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `D L' D2 B' R2 L2 U' R D` (DR on F/B).
- EOs of at most 4 turns, best DR: no normal EO; through an inverse EO: 10, `(L' D F' U)` on U/D, then `(R' F R2 B2 L' B)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `F2 D L B' R'` on R/L, then `F R2 B' L2 U F` to DR on U/D; through an inverse EO: 10, `(L' D F' U)` on U/D, then `(R' F R2 B2 L' B)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 10

`D2 L2 U2 L2 U' L2 D F2 U' B2 D B2 U L2 U2 B' D' F R' B' D B2 F2 L2 U2`

Bad edges on R/L, U/D, F/B: 4, 6, 6. EOs of at most 4 turns (all three axes): 14 normal, 14 inverse, 32 NISS with turns on both sides; of at most 5: 230, 150, 316.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `F2 L F U2 L' U R2 F D U` (DR on F/B).
- On the inverse: 8 (per axis: R/L 9, U/D 10, F/B 8), for example `(L2 B D' B' D F U R)` (DR on F/B).
- Best of the six: 8. With NISS: 8, for example `(L2 B D' B' D F U R)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `L F' U2 L'` on R/L, then `U B' U D2 B U D` to DR on F/B; through an inverse EO: 9, `(F U R)` on R/L, then `(F' U2 D' B R2 D)` to DR on F/B; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F2 L F U2 L'` on R/L, then `U R2 F U D` to DR on F/B; through an inverse EO: 9, `(F U R)` on R/L, then `(F' U2 D' B R2 D)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 11

`U' B2 U' B2 U L2 D2 B2 R2 F2 R2 D F2 R2 U2 R' U L B F R2 U' B R D2`

Bad edges on R/L, U/D, F/B: 8, 6, 6. EOs of at most 4 turns (all three axes): 10 normal, 28 inverse, 4 NISS with turns on both sides; of at most 5: 144, 180, 228.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `F U' L2 F B' U' D R D` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(U2 R D U L' B D' U' L)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `F U' L2 F B' U' D R D` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U' B2 R D` on U/D, then `F' L' F U2 D2 R F` to DR on R/L; through an inverse EO: 10, `(R U' L')` on R/L, then `(B2 U' B L2 U D2 B)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `F U' R2 F' B` on F/B, then `U' D L U` to DR on R/L; through an inverse EO: 10, `(R U' L')` on R/L, then `(B2 U' B L2 U D2 B)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 12

`R2 F2 L2 B2 D F2 L2 D2 L2 U F2 D B2 U' L' F' U B L D R B' L2 U'`

Bad edges on R/L, U/D, F/B: 6, 6, 10. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 8 NISS with turns on both sides; of at most 5: 0, 26, 180.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 11, U/D 10, F/B 10), for example `F D2 L' D' F2 U' L' D L2 U` (DR on F/B).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(D' B' L' U' F2 R' F U2 D B)` (DR on U/D).
- Best of the six: 10. With NISS: 9, for example `F B R' D' L' B (D F2 R)` (DR on U/D).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: no normal EO; through an inverse EO: 11, `(L D F' B L')` on R/L, then `(B2 U2 B' D2 B D)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 13

`D F2 U' L2 D' F2 U' R2 U' B2 U B2 R2 U L' D' U' F R D2 R D' B D`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 4 normal, 4 inverse, 8 NISS with turns on both sides; of at most 5: 62, 96, 228.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `R' L D' B2 U L' D' B' R` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(R2 U' B R' U' B2 L D' F)` (DR on R/L).
- Best of the six: 9. With NISS: 8, for example `L (D' B' U2 D R' B L)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `B' D R2 F'` on F/B, then `D2 L U L2 R U` to DR on R/L; through an inverse EO: 11, `(F B R F)` on F/B, then `(L B2 R' D' R' F2 L)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L U' B2 L' D'` on U/D, then `R' D2 L2 F R` to DR on F/B; through an inverse EO: 10, `(F R' B R' F)` on F/B, then `(L R' U B2 D)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 14

`L2 R2 U2 F2 U L2 U F2 L2 D' F2 R2 U F' L' D2 R' B2 U B' F' L2`

Bad edges on R/L, U/D, F/B: 6, 6, 10. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 0 NISS with turns on both sides; of at most 5: 28, 28, 112.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `R' D F B R2 D F' R' F` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(F R2 U' R D U B2 L2 B' L)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `R' D F B R2 D F' R' F` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; no EO at all.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `R U' B U' D'` on U/D, then `L2 B R' L' B' R` to DR on F/B; through an inverse EO: 11, `(U' R U F' D')` on U/D, then `(U2 B' L B2 R' F)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 15

`R2 B2 U2 B2 U' F2 D F2 U2 F2 R2 D2 U' R2 L' B D' U F2 R' B F2 L`

Bad edges on R/L, U/D, F/B: 4, 8, 4. EOs of at most 4 turns (all three axes): 10 normal, 6 inverse, 12 NISS with turns on both sides; of at most 5: 174, 152, 180.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `R F D' R' U' R U2 F' L` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(R D R U B' U B2 R U)` (DR on R/L).
- Best of the six: 9. With NISS: 8, for example `F' R B2 D (R2 F' U B)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D' L' U' B` on F/B, then `L D' L F2 L U` to DR on R/L; through an inverse EO: 10, `(L2 U2 B' L)` on R/L, then `(F2 L2 D F B' U)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `R F D' R' U'` on U/D, then `R U2 F' L` to DR on F/B; through an inverse EO: 9, `(R D R U B')` on F/B, then `(U B2 R U)` to DR on R/L; with NISS EOs too: 8.

</details>

### Scramble 16

`D R2 U B2 L2 U L2 B2 D2 L2 F2 U' L2 U' B' D2 F' L' R D' U' R' U2`

Bad edges on R/L, U/D, F/B: 8, 8, 6. EOs of at most 4 turns (all three axes): 16 normal, 20 inverse, 16 NISS with turns on both sides; of at most 5: 260, 310, 332.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `U2 R U D R' L F D2 B` (DR on U/D).
- On the inverse: 10 (per axis: R/L 10, U/D 11, F/B 11), for example `(U' B U2 D R F L U' F D)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `U2 R U D R' L F D2 B` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U D R L` on R/L, then `F L2 U F' L2 D` to DR on F/B; through an inverse EO: 11, `(B' R2 D F)` on F/B, then `(R D2 L U' R2 D L)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U D R L` on R/L, then `F L2 U F' L2 D` to DR on F/B; through an inverse EO: 11, `(U R L' U D')` on U/D, then `(L2 R D2 B U2 F)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 17

`U2 F2 D' L2 B2 D' R2 F2 D F2 L2 B2 U2 B' U R F2 U F U2 R2 U'`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 40 normal, 6 inverse, 8 NISS with turns on both sides; of at most 5: 352, 170, 228.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `B U' F' L U2 D' L U' L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `(U F' R2 D' R U' B' D2 R)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `U R2 U2 F' U' F2 R' U' B` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `B U' F'` on F/B, then `L U2 D' L U' L` to DR on U/D; through an inverse EO: 11, `(R2 D F2 R')` on R/L, then `(F2 D' B2 D' L2 F U)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `R' U R' F B` on F/B, then `D' L U' L` to DR on U/D; through an inverse EO: 11, `(U2 R2 D F2 R')` on R/L, then `(L2 D' L2 F U' B)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 18

`D' R2 U2 F2 L2 R2 U' L2 U' L2 U' B2 L B' U' R B U2 F' R' F' R'`

Bad edges on R/L, U/D, F/B: 6, 4, 4. EOs of at most 4 turns (all three axes): 24 normal, 24 inverse, 44 NISS with turns on both sides; of at most 5: 340, 278, 524.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `U' B L' D R F R' F' D` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(R B U L' F2 R F2 U' B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `U L' F' U' R U2 R' U L` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `R' U L2 F'` on F/B, then `U L U2 L2 R U` to DR on R/L; through an inverse EO: 10, `(L2 D2 B' U')` on U/D, then `(F2 B2 R D2 B' L)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `B R' L' F' R'` on R/L, then `D2 R2 U' L2 B` to DR on U/D; through an inverse EO: 10, `(L B' R U' R')` on R/L, then `(U F' U' L2 U)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 19

`D L2 U' F2 R2 U B2 R2 D' R2 U2 L2 B' L2 D' L B' D2 F D B R' U'`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 6 normal, 6 inverse, 16 NISS with turns on both sides; of at most 5: 176, 130, 412.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 11, F/B 10), for example `U R F R B' R2 B' D` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(F' L2 D B U2 B2 L' F2 D R)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `U R F R B' R2 B' D` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `R' L U L'` on R/L, then `B2 D F2 L2 F' D` to DR on F/B; through an inverse EO: 10, `(F' L2 D B)` on F/B, then `(U2 B2 L' F2 D R)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `R' L U L'` on R/L, then `B2 D F2 L2 F' D` to DR on F/B; through an inverse EO: 10, `(F' L2 D B)` on F/B, then `(U2 B2 L' F2 D R)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 20

`R2 U' L2 D' F2 U2 B2 R2 B2 U F2 D F2 U2 F' L' B U F' D' B U2 R2`

Bad edges on R/L, U/D, F/B: 4, 8, 6. EOs of at most 4 turns (all three axes): 28 normal, 4 inverse, 8 NISS with turns on both sides; of at most 5: 236, 152, 200.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `R2 B U D' B' R F' B2 R` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(B2 R2 D2 B' U2 F' U D' B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `R2 U2 B' D F U' B' L F` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U2 F2 L'` on R/L, then `F B U2 D F B' U` to DR on F/B; through an inverse EO: 11, `(B2 D' F R')` on R/L, then `(U2 D' B2 F L2 D F)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U2 F2 L'` on R/L, then `F B U2 D F B' U` to DR on F/B; through an inverse EO: 10, `(R2 F B' U R)` on R/L, then `(F2 R2 U2 F' D)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 21

`D B2 D2 F2 D R2 B2 F2 U R2 B2 L2 U' B' D2 L D' L D L F' L2 U'`

Bad edges on R/L, U/D, F/B: 2, 8, 8. EOs of at most 4 turns (all three axes): 16 normal, 24 inverse, 20 NISS with turns on both sides; of at most 5: 244, 296, 220.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `U' B D F' U R F2 R F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `(B2 U F' U2 D' L F' L' B)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `U' B D F' U R F2 R F` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U L F L'` on R/L, then `U2 B D2 B U2 D B` to DR on U/D; through an inverse EO: 11, `(R2 L' B' L')` on R/L, then `(F R2 F2 U B' D' F)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `U' B D F' U` on U/D, then `R F2 R F` to DR on R/L; through an inverse EO: 10, `(U B' R D F)` on F/B, then `(U' L F2 R' U)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 22

`L2 D' F2 U L2 F2 D' B2 D2 R2 B2 U R2 F' U2 L B' R2 F' U' R F' U`

Bad edges on R/L, U/D, F/B: 8, 8, 8. EOs of at most 4 turns (all three axes): 4 normal, 0 inverse, 20 NISS with turns on both sides; of at most 5: 100, 84, 228.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `R2 D L B' U' F D' R' B` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(L D' U' R2 F B D' F L)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `L' U2 L' F' U L' B' D' F` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U R B L'` on R/L, then `U' D2 L2 F' U' L2 F` to DR on U/D; no inverse EO; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `B' R U' D F'` on F/B, then `L U' D R' U` to DR on R/L; through an inverse EO: 10, `(R2 L' F U' D)` on U/D, then `(F2 U2 F2 B R)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 23

`D' R2 F2 U L2 U R2 U' R2 U L2 U B2 D B U R2 D R' F' U' B F2 U2`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 24 normal, 22 inverse, 16 NISS with turns on both sides; of at most 5: 236, 290, 228.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `D F D F2 L' B2 U2 L2 U B` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(F' U' L U' D' R2 U F' L)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `(F' U' L U' D' R2 U F' L)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U' F B2 R` on R/L, then `U F' R2 F R2 F' D` to DR on F/B; through an inverse EO: 10, `(F D L B)` on F/B, then `(U R2 F2 U R2 U)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D F D F2 L'` on R/L, then `B2 U2 L2 U B` to DR on U/D; through an inverse EO: 10, `(U R2 B' D2 L)` on R/L, then `(U2 B' D F U)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 24

`U2 R2 U' F2 U' B2 F2 D' R2 U B2 U2 R2 D B2 U' R' B' U B' D R' D L R2 U'`

Bad edges on R/L, U/D, F/B: 6, 8, 2. EOs of at most 4 turns (all three axes): 40 normal, 36 inverse, 4 NISS with turns on both sides; of at most 5: 530, 428, 232.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 11), for example `L' B R' U' B U2 D2 R2 B2 R` (DR on U/D).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(B' U' B U2 L U2 D L' B2 D)` (DR on R/L).
- Best of the six: 10. With NISS: 8, for example `L' B R' U' B (U2 R2 U)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `D' F' R2 F'` on F/B, then `U2 R' B2 D' L' R U` to DR on R/L; through an inverse EO: 10, `(U L' F' D)` on U/D, then `(B2 R' F2 R' U2 L)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F L' F' R L'` on R/L, then `U D R2 U' B` to DR on U/D; through an inverse EO: 10, `(U L' F' D)` on U/D, then `(B2 R' F2 R' U2 L)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 25

`F2 D B2 R2 B2 L2 U2 B2 U R2 U' B2 U F2 B' D L2 R' U R2 B F2 R' D'`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 24 NISS with turns on both sides; of at most 5: 26, 52, 312.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `L U' F2 B' D R D2 F U2 R` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(F D' F B2 R' U B2 L F)` (DR on R/L).
- Best of the six: 9. With NISS: 8, for example `D R B D2 L (U L' D)` (DR on F/B).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U F' B2 L' D` on U/D, then `F U2 F D2 L` to DR on F/B; through an inverse EO: 11, `(D L' B R' D)` on U/D, then `(B' U2 L B U2 L)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 26

`D2 B2 R2 D F2 U' B2 L2 B2 L2 D2 F2 D' R' B' F2 R F2 L B' D' F U`

Bad edges on R/L, U/D, F/B: 8, 8, 6. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 4 NISS with turns on both sides; of at most 5: 72, 48, 64.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `F D' F' L U B' R B' R F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(L U R F' D' R2 B' R B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `(L U R F' D' R2 B' R B)` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F D L F' U'` on U/D, then `L2 F' U2 F' L` to DR on F/B; through an inverse EO: 9, `(L U R F' D')` on U/D, then `(R2 B' R B)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 27

`D' F2 D L2 F2 U' F2 L2 D L2 U' L2 B2 F' R F D R' U' F R U'`

Bad edges on R/L, U/D, F/B: 4, 6, 4. EOs of at most 4 turns (all three axes): 18 normal, 34 inverse, 16 NISS with turns on both sides; of at most 5: 306, 332, 324.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `D' F D2 B U2 R2 U L' B` (DR on R/L).
- On the inverse: 8 (per axis: R/L 9, U/D 9, F/B 8), for example `(F L2 B' L' U' B R2 D)` (DR on F/B).
- Best of the six: 8. With NISS: 8, for example `(F L2 B' L' U' B R2 D)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U D' F' R` on R/L, then `B D2 B R2 L2 F` to DR on U/D; through an inverse EO: 8, `(F L2 B' L')` on R/L, then `(U' B R2 D)` to DR on F/B; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U D' F' R` on R/L, then `B D2 B R2 L2 F` to DR on U/D; through an inverse EO: 8, `(F L2 B' L')` on R/L, then `(U' B R2 D)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 28

`U2 L2 U B2 D2 L2 D' R2 U' F2 D' B2 R2 B2 L' F D' U' F2 D2 B2 R2 F`

Bad edges on R/L, U/D, F/B: 4, 8, 6. EOs of at most 4 turns (all three axes): 4 normal, 16 inverse, 4 NISS with turns on both sides; of at most 5: 206, 226, 132.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 10, U/D 9, F/B 8), for example `U2 R2 U B' L D' F' L` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `(B' U D L' B' U R B2 R)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `U2 R2 U B' L D' F' L` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U' D2 B' L` on R/L, then `U2 F2 U' F2 D L2 F` to DR on U/D; through an inverse EO: 10, `(D' F2 U' R)` on R/L, then `(U2 B' D' L2 U' F)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U F' B' D B` on F/B, then `R2 D F2 R D` to DR on R/L; through an inverse EO: 9, `(B' U D L' B')` on F/B, then `(U R B2 R)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 29

`L2 U' R2 U' R2 F2 L2 D L2 D F2 U2 L2 U R' B2 F R D F' L2 F' L' R'`

Bad edges on R/L, U/D, F/B: 8, 2, 4. EOs of at most 4 turns (all three axes): 42 normal, 42 inverse, 16 NISS with turns on both sides; of at most 5: 528, 556, 264.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `L' D B' L' D L2 B' U2 L` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `(F' R' U F L F U2 D2 F)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `R2 U D' F R2 D F R' U` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `L2 D' R D` on U/D, then `L B2 R F' B' R` to DR on F/B; through an inverse EO: 10, `(R U B' U)` on U/D, then `(F' R2 L2 U2 F' R)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `L' D B' L' D` on U/D, then `L2 B' U2 L` to DR on F/B; through an inverse EO: 9, `(F' R' U F L)` on R/L, then `(B R2 L2 B)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 30

`R2 D' B2 D L2 B2 F2 D B2 L2 R2 D U F' L' U2 B2 D B' R' B' F' U'`

Bad edges on R/L, U/D, F/B: 6, 8, 6. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 12 NISS with turns on both sides; of at most 5: 20, 52, 216.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `D' F L' U' F D2 L F' D` (DR on F/B).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(D2 L D B U L' F2 B' R' B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `D' F L' U' F D2 L F' D` (DR on F/B).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `F L' U2 D' F` on F/B, then `R2 U2 R' L U R` to DR on U/D; through an inverse EO: 10, `(D2 L D B U)` on U/D, then `(L' B' F2 R' B)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 31

`B2 R2 U F2 U' L2 F2 U B2 L2 U' L2 D2 R' D' R2 F' L B' R U' L U'`

Bad edges on R/L, U/D, F/B: 6, 6, 8. EOs of at most 4 turns (all three axes): 8 normal, 8 inverse, 8 NISS with turns on both sides; of at most 5: 78, 120, 164.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `F' B' L' R' U2 B R' U R2 D` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(F2 B2 R B R' U R2 D' L)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `(F2 B2 R B R' U R2 D' L)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U2 R F B` on F/B, then `U D R F2 U' D' L` to DR on U/D; through an inverse EO: 11, `(U' B' R D)` on U/D, then `(F R2 L2 D2 F2 B R)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `R' F U B R` on R/L, then `F D F D' R2 F` to DR on U/D; through an inverse EO: 11, `(U R D2 F2 D')` on U/D, then `(B L F' D2 B2 L)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 32

`R2 U' F2 U' F2 R2 B2 D B2 D' R2 F2 U' L' D' R U' L' B' L`

Bad edges on R/L, U/D, F/B: 8, 8, 4. EOs of at most 4 turns (all three axes): 36 normal, 36 inverse, 16 NISS with turns on both sides; of at most 5: 518, 400, 368.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 7 (per axis: R/L 8, U/D 7, F/B 9), for example `L' B L U R' D L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(R U2 B2 U' L D R' U F)` (DR on R/L).
- Best of the six: 7. With NISS: 7, for example `L' B L U R' D L` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 7, EO `L' B` on F/B, then `L U R' D L` to DR on U/D; through an inverse EO: 11, `(L U' R D)` on U/D, then `(R2 B2 D2 L F B2 R)` to DR on F/B; with NISS EOs too: 7.
- EOs of at most 5 turns, best DR: through a normal EO: 7, EO `L' B` on F/B, then `L U R' D L` to DR on U/D; through an inverse EO: 10, `(D' L U R D)` on U/D, then `(L' B2 L B' L)` to DR on F/B; with NISS EOs too: 7.

</details>

### Scramble 33

`B2 U B2 F2 R2 U' R2 B2 U' L2 U F2 L2 U2 F' L' D' U' B' D' L F2 D U'`

Bad edges on R/L, U/D, F/B: 4, 4, 8. EOs of at most 4 turns (all three axes): 40 normal, 22 inverse, 4 NISS with turns on both sides; of at most 5: 424, 244, 256.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `D2 F2 L' B' L2 D B L2 D` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(U' F U' B L R2 B D' B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `D2 F2 L' B' L2 D B L2 D` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `D2 F2 L'` on R/L, then `B' L2 D B L2 D` to DR on F/B; through an inverse EO: 10, `(F' B D2 R)` on R/L, then `(U' F B' U' F2 U)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `D2 F2 L'` on R/L, then `B' L2 D B L2 D` to DR on F/B; through an inverse EO: 10, `(F' B D2 R)` on R/L, then `(U' F B' U' F2 U)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 34

`B2 L2 U' B2 F2 D F2 U2 B2 L2 F2 L2 U F' D B2 F2 R' B2 D' B' D L'`

Bad edges on R/L, U/D, F/B: 8, 6, 6. EOs of at most 4 turns (all three axes): 24 normal, 8 inverse, 20 NISS with turns on both sides; of at most 5: 170, 108, 244.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `L U' R' B' L2 D2 R' F U` (DR on F/B).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(U' B' U' R2 D F L B2 L B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `R D2 U' R' L U' B' R D` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D2 L' B' R'` on R/L, then `F B D F U D` to DR on F/B; through an inverse EO: 11, `(B' U' R2 D')` on U/D, then `(L B' U2 B' L' R F)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D2 L' B' R'` on R/L, then `F B D F U D` to DR on F/B; through an inverse EO: 10, `(U' B' U' R2 D)` on U/D, then `(F L B2 L B)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 35

`F2 U L2 U' B2 D F2 L2 R2 F2 U B2 D' F' L B U2 F2 L U' L' R2 D2`

Bad edges on R/L, U/D, F/B: 6, 8, 8. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 4 NISS with turns on both sides; of at most 5: 92, 32, 112.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `L2 F L' F2 U' B R' D' B` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(U' F' B2 U R' U2 B' R2 U)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `L2 F L' F2 U' B R' D' B` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F' U' R' B D'` on U/D, then `B D2 R2 B2 L` to DR on F/B; through an inverse EO: 10, `(F' L' U' D B')` on F/B, then `(U F2 U2 D L)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 36

`R2 U2 B2 L2 U' F2 U' R2 B2 R2 D R2 F' U L' U' R D2 F' R B2 D2`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 4 normal, 8 inverse, 8 NISS with turns on both sides; of at most 5: 144, 104, 240.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 11, U/D 10, F/B 10), for example `B L' F2 R' U' F L' F2 B2 U` (DR on F/B).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(D R2 B L' D' L2 D2 U2 B' L)` (DR on F/B).
- Best of the six: 10. With NISS: 8, for example `D B' L U' D B (R2 F)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `F B' R' F` on F/B, then `L2 D F2 D2 R2 F2 R` to DR on U/D; through an inverse EO: 11, `(D L F2 U)` on U/D, then `(L' B' F2 U2 L R F)` to DR on R/L; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `D L' D B U` on U/D, then `L' F' L' B D2 R` to DR on F/B; through an inverse EO: 10, `(D R2 B L' D')` on U/D, then `(L2 D2 U2 B' L)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 37

`D F2 L2 U' F2 U L2 B2 U L2 B2 L2 D U' L' F R B2 U L U2 L2 F`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 0 normal, 2 inverse, 16 NISS with turns on both sides; of at most 5: 92, 90, 232.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 11, U/D 9, F/B 10), for example `F' L2 U2 L' U' B2 R' F' L` (DR on U/D).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(U2 R B U' R L B R2 D' B)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `F' L2 U2 L' U' B2 R' F' L` (DR on U/D).
- EOs of at most 4 turns, best DR: no normal EO; through an inverse EO: 11, `(D F2 R U')` on U/D, then `(R B' L F2 L F' L)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `R' F D' B L` on R/L, then `U' B U R2 F D` to DR on F/B; through an inverse EO: 11, `(U B R' B2 L)` on R/L, then `(U' B2 D R2 U' F)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 38

`L2 D F2 U F2 D B2 L2 D R2 B2 F2 D F2 R' F' R U R' D F2 R D'`

Bad edges on R/L, U/D, F/B: 6, 4, 4. EOs of at most 4 turns (all three axes): 22 normal, 18 inverse, 12 NISS with turns on both sides; of at most 5: 246, 198, 248.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `F' U L' F' B D' L' D B` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(B L' F2 L U' D2 L2 F' U)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `F' U L' F' B D' L' D B` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `F2 L' F U'` on U/D, then `D2 R B' D2 R' F` to DR on R/L; through an inverse EO: 10, `(U L B)` on F/B, then `(U2 L2 B2 D' L2 R' U)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U' R2 F2 B' D` on U/D, then `R' F2 L' F' L` to DR on F/B; through an inverse EO: 10, `(U L B)` on F/B, then `(U2 L2 B2 D' L2 R' U)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 39

`B2 F2 D2 U' B2 R2 F2 U' R2 U L2 F2 D' U' L' R' U' F2 L B D F2 D'`

Bad edges on R/L, U/D, F/B: 6, 6, 4. EOs of at most 4 turns (all three axes): 52 normal, 18 inverse, 8 NISS with turns on both sides; of at most 5: 402, 268, 264.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 9, F/B 9), for example `B' U F2 B2 D R' F2 D` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(F2 R' U' R2 L' F2 D2 U' L)` (DR on F/B).
- Best of the six: 8. With NISS: 6, for example `B (R' L D F2 R)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 8, EO `B'` on F/B, then `U F2 B2 D R' F2 D` to DR on R/L; through an inverse EO: 10, `(L' D B2 R)` on R/L, then `(U D2 B' U2 D B)` to DR on U/D; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 8, EO `B'` on F/B, then `U F2 B2 D R' F2 D` to DR on R/L; through an inverse EO: 10, `(L' D B2 R)` on R/L, then `(U D2 B' U2 D B)` to DR on U/D; with NISS EOs too: 8.

</details>

### Scramble 40

`D2 R2 D' F2 L2 B2 D2 R2 D2 U B2 R2 U2 L' D2 U F R B L' F L U2`

Bad edges on R/L, U/D, F/B: 8, 4, 8. EOs of at most 4 turns (all three axes): 28 normal, 64 inverse, 16 NISS with turns on both sides; of at most 5: 376, 426, 228.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `F' D2 F2 B' U' F' R U2 D2 B` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(F D B2 D' R' L' F' U R)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `(F D B2 D' R' L' F' U R)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `B2 R' F' U'` on U/D, then `F' B' R' F L F R` to DR on F/B; through an inverse EO: 10, `(R2 B L' D')` on U/D, then `(R B L' U2 F' R)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F' D2 F2 B' U'` on U/D, then `F' R U2 D2 B` to DR on R/L; through an inverse EO: 10, `(F' D2 R' F' L')` on R/L, then `(U2 F L2 U' F)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 41

`B2 F2 R2 D B2 U' B2 D2 U' F2 U B2 L2 U' L' D U2 B2 F R D F R'`

Bad edges on R/L, U/D, F/B: 4, 4, 4. EOs of at most 4 turns (all three axes): 42 normal, 22 inverse, 24 NISS with turns on both sides; of at most 5: 364, 282, 472.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 9, F/B 9), for example `B2 U L2 U2 L' U' L' F` (DR on R/L).
- On the inverse: 8 (per axis: R/L 8, U/D 8, F/B 8), for example `(B R' F2 D' F R' D2 B)` (DR on R/L).
- Best of the six: 8. With NISS: 8, for example `R' U' R' D L2 F2 D B` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `R' F2 R2 D'` on U/D, then `L R2 D2 L' D2 F` to DR on R/L; through an inverse EO: 8, `(B R' F2 D')` on U/D, then `(F R' D2 B)` to DR on R/L; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `R F' D' R' F'` on F/B, then `B2 U2 D' L` to DR on U/D; through an inverse EO: 8, `(B R' F2 D')` on U/D, then `(F R' D2 B)` to DR on R/L; with NISS EOs too: 8.

</details>

### Scramble 42

`B2 D R2 D' B2 R2 B2 F2 U' R2 U F2 U R' F R B2 U2 L' U F D' B'`

Bad edges on R/L, U/D, F/B: 4, 8, 6. EOs of at most 4 turns (all three axes): 0 normal, 10 inverse, 8 NISS with turns on both sides; of at most 5: 12, 192, 232.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `D F B D' U2 B' U' R D` (DR on F/B).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(F L U D' B U2 F2 B2 R)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `D F B D' U2 B' U' R D` (DR on F/B).
- EOs of at most 4 turns, best DR: no normal EO; through an inverse EO: 11, `(L B' D' L')` on R/L, then `(D' F2 L2 B' R2 U F)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 12, EO `U2 B U' D L` on R/L, then `U F2 B2 L2 U' R2 D` to DR on F/B; through an inverse EO: 9, `(F L U D' B)` on F/B, then `(U2 F2 B2 R)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 43

`F2 D' R2 B2 D L2 U2 L2 F2 D' R2 U2 F2 U' F' U' R' D' B R' F D' U'`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 22 normal, 36 inverse, 20 NISS with turns on both sides; of at most 5: 198, 280, 320.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `U R B U L' F D R U` (DR on R/L).
- On the inverse: 8 (per axis: R/L 9, U/D 8, F/B 10), for example `(U B' U D' F' B' U' L)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `(U B' U D' F' B' U' L)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U2 F2 D R` on R/L, then `B2 D L2 F D B` to DR on U/D; through an inverse EO: 9, `(D' R2 F B)` on F/B, then `(U L2 U' R' U)` to DR on R/L; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U2 F2 D R` on R/L, then `B2 D L2 F D B` to DR on U/D; through an inverse EO: 9, `(D' R2 F B)` on F/B, then `(U L2 U' R' U)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 44

`U F2 U' L2 F2 D L2 B2 D R2 B2 R2 U B' D2 U R' B L D R' U' F`

Bad edges on R/L, U/D, F/B: 8, 6, 6. EOs of at most 4 turns (all three axes): 0 normal, 4 inverse, 4 NISS with turns on both sides; of at most 5: 40, 90, 88.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `R F' D L' R2 B' D2 B2 R U` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(D R' B D' L B R2 F2 B2 D)` (DR on F/B).
- Best of the six: 10. With NISS: 9, for example `F (R F' R2 B D F L' U)` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; through an inverse EO: 12, `(F R2 D' B)` on F/B, then `(L F2 D R B2 L F2 D)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `U' F2 D' R L` on R/L, then `F' U R2 U L2 D` to DR on F/B; through an inverse EO: 10, `(D R' B D' L)` on R/L, then `(B R2 F2 B2 D)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 45

`B2 U2 B2 D F2 D' R2 F2 U' B2 L2 D' R2 U' L' D F' U' R2 U' B' F2 L' R'`

Bad edges on R/L, U/D, F/B: 10, 6, 6. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 4 NISS with turns on both sides; of at most 5: 10, 38, 136.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `L D B D2 L F R' F' U` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(B2 D' F' L F' B D' R' F2 U)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `L D B D2 L F R' F' U` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `L' U R L2 D'` on U/D, then `B2 L2 F L2 B' R` to DR on F/B; through an inverse EO: 11, `(B2 L' F D2 B)` on F/B, then `(U' L2 U L D R)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 46

`D F2 U L2 D L2 U B2 R2 U' R2 D2 L2 D F' R F2 L U2 B' D' U' F' U`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 16 NISS with turns on both sides; of at most 5: 54, 32, 308.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `D R' D' F' U2 D' F2 B' L' F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(F2 L U' R U R F U R)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `(F2 L U' R U R F U R)` (DR on F/B).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D R' D' F' D'` on U/D, then `U2 B' F2 L' F` to DR on R/L; through an inverse EO: 11, `(B U2 D R' F')` on F/B, then `(L U' R2 U' B2 L)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 47

`U R2 D2 R2 U2 F2 L2 R2 U' L2 R2 L' U L R2 B D2 L' U2 R`

Bad edges on R/L, U/D, F/B: 6, 4, 4. EOs of at most 4 turns (all three axes): 20 normal, 16 inverse, 0 NISS with turns on both sides; of at most 5: 272, 262, 176.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `R' U2 L D2 B' R2 L' U' L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(R' U F2 L2 D R D2 R' F)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `R' U2 L D2 B' R2 L' U' L` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D2 L2 B' D` on U/D, then `R2 B2 L B' D2 F` to DR on R/L; through an inverse EO: 11, `(U R B2 U)` on U/D, then `(L2 F' L R2 B2 L F)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `R' U2 L D2 B'` on F/B, then `R2 L' U' L` to DR on U/D; through an inverse EO: 9, `(R' U F2 L2 D)` on U/D, then `(R D2 R' F)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 48

`F2 D2 R2 D' L2 U2 B2 L2 B2 L2 D F2 U2 R2 U' R' D L2 B L' B2 R2 D2 F' L2 U'`

Bad edges on R/L, U/D, F/B: 8, 6, 6. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 12 NISS with turns on both sides; of at most 5: 68, 64, 188.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 11, F/B 10), for example `U2 F U F' R' D2 B L F2 U` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(F R' F' L D R D B U)` (DR on F/B).
- Best of the six: 9. With NISS: 8, for example `F R' U' B R2 F' U (L)` (DR on F/B).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `D2 R B' U L` on R/L, then `F2 U2 B' U2 D' B` to DR on U/D; through an inverse EO: 10, `(R' F' L' D R)` on R/L, then `(B U F B2 D)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 49

`F2 D2 R2 U L2 U B2 D' R2 B2 F2 D F2 R' B2 D' L B U R2 F L' B`

Bad edges on R/L, U/D, F/B: 6, 6, 8. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 0 NISS with turns on both sides; of at most 5: 42, 22, 132.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `B' L F' R2 U' B' L' D B2 R` (DR on U/D).
- On the inverse: 10 (per axis: R/L 10, U/D 11, F/B 10), for example `(R' D F D2 L' B' U F2 R F)` (DR on R/L).
- Best of the six: 10. With NISS: 9, for example `F R' U2 B' D R' F (R' D)` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; no EO at all.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `D B2 L' F B` on F/B, then `L D L' U F2 U` to DR on R/L; through an inverse EO: 11, `(L' B U' D' F)` on F/B, then `(L' U' R L' D' R)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 50

`F2 L2 F2 D U2 L2 F2 D' F2 L2 R2 U2 L2 F' U' B L B U2 B2 F' R U'`

Bad edges on R/L, U/D, F/B: 6, 4, 6. EOs of at most 4 turns (all three axes): 20 normal, 6 inverse, 4 NISS with turns on both sides; of at most 5: 200, 174, 132.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `F2 R U' F2 R' F2 R2 F' B L` (DR on F/B).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(B' L2 B' R U2 F' B' D' R)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `(B' L2 B' R U2 F' B' D' R)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `F2 R U'` on U/D, then `F2 R' F2 R2 F' B L` to DR on F/B; through an inverse EO: 10, `(D2 R' F D)` on U/D, then `(F' R' L U2 B L)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L F' B2 R' D'` on U/D, then `R D2 L2 R2 F` to DR on R/L; through an inverse EO: 10, `(D2 R' F D)` on U/D, then `(F' R' L U2 B L)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 51

`L2 D2 R2 B2 D F2 D' L2 F2 R2 U2 F2 U2 F' R' U2 L B D' L' F2 D' U2`

Bad edges on R/L, U/D, F/B: 8, 4, 6. EOs of at most 4 turns (all three axes): 14 normal, 8 inverse, 12 NISS with turns on both sides; of at most 5: 226, 154, 208.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `B2 D' F' R' D R2 U L2 F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `(F2 L F B D R' F U2 F)` (DR on U/D).
- Best of the six: 9. With NISS: 8, for example `D B (D R2 U' F R U)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U R B2 U` on U/D, then `L F' R' D2 L' B` to DR on R/L; through an inverse EO: 10, `(L B D R)` on R/L, then `(B' U B R2 F2 D)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U R B2 U` on U/D, then `L F' R' D2 L' B` to DR on R/L; through an inverse EO: 10, `(D L' D B R)` on R/L, then `(B' U' R2 F U)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 52

`D R2 F2 D' L2 F2 U2 R2 F2 U' F2 D' R D' B L' F2 D2 R' D' U`

Bad edges on R/L, U/D, F/B: 6, 8, 4. EOs of at most 4 turns (all three axes): 4 normal, 12 inverse, 16 NISS with turns on both sides; of at most 5: 162, 192, 260.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `U' D R D2 F2 L B' D R` (DR on U/D).
- On the inverse: 8 (per axis: R/L 9, U/D 8, F/B 9), for example `(L U2 B2 D B2 D B' L)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `(L U2 B2 D B2 D B' L)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U2 D' L' B` on F/B, then `D2 B2 R' U' F2 R` to DR on U/D; through an inverse EO: 10, `(D R' F U)` on U/D, then `(D2 B F U2 R B)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L F B2 D' R'` on R/L, then `B R2 D B F` to DR on U/D; through an inverse EO: 10, `(D R F R2 U)` on U/D, then `(B R' U2 R B)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 53

`B2 D' L2 U R2 F2 U' R2 D2 F2 R2 D' R2 D2 R' D L2 F R2 D' F2 U' L U`

Bad edges on R/L, U/D, F/B: 4, 8, 4. EOs of at most 4 turns (all three axes): 8 normal, 14 inverse, 36 NISS with turns on both sides; of at most 5: 174, 204, 332.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `D2 B U L' F' U2 D F2 D' F` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `(U2 R' U R2 D' L2 F2 B U)` (DR on R/L).
- Best of the six: 9. With NISS: 8, for example `R' U R L F L (U' L)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D2 B U L'` on R/L, then `F' U2 D F2 D' F` to DR on U/D; through an inverse EO: 11, `(B' U D' R)` on R/L, then `(U' D' B L2 U' F2 D)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D2 B U L'` on R/L, then `F' U2 D F2 D' F` to DR on U/D; through an inverse EO: 10, `(D' B' U D' R')` on R/L, then `(D2 F2 R2 F' D)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 54

`F2 U2 F2 D' L2 D B2 U' B2 U' L2 D2 B' L F' R B U F L' R' D'`

Bad edges on R/L, U/D, F/B: 6, 4, 6. EOs of at most 4 turns (all three axes): 28 normal, 20 inverse, 28 NISS with turns on both sides; of at most 5: 412, 224, 420.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `L' D L' U2 L' F U2 L' B` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(R U2 F' L U2 F U F L)` (DR on F/B).
- Best of the six: 9. With NISS: 8, for example `D2 B (R L U2 F U L)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `L' D` on U/D, then `L' U2 L' F U2 L' B` to DR on R/L; through an inverse EO: 10, `(B' R F' U)` on U/D, then `(F2 R2 F U2 R' B)` to DR on R/L; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `R2 F2 L B2 U'` on U/D, then `B F' L' F` to DR on R/L; through an inverse EO: 10, `(U2 R' F D' L)` on R/L, then `(F D L2 B' D)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 55

`D2 L2 F2 L2 D' R2 B2 F2 U' F2 D' R2 U B' D U2 F U' L' R' U F2 U2`

Bad edges on R/L, U/D, F/B: 8, 6, 6. EOs of at most 4 turns (all three axes): 4 normal, 0 inverse, 16 NISS with turns on both sides; of at most 5: 142, 100, 212.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `U' R F U L' F R2 F D` (DR on F/B).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(F2 R D' L2 U' R U2 R B L)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `F D' B2 R' U' L D R' D` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `F' B L B'` on F/B, then `L R2 B2 U' B2 D` to DR on R/L; no inverse EO; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `U' R F U L'` on R/L, then `F R2 F D` to DR on F/B; through an inverse EO: 10, `(F2 R D' L2 U')` on U/D, then `(R U2 R B L)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 56

`F2 D B2 D' R2 D' F2 L2 D2 B2 L2 D2 U' B2 R' D U2 B' F2 L F' L2 D'`

Bad edges on R/L, U/D, F/B: 2, 6, 8. EOs of at most 4 turns (all three axes): 50 normal, 10 inverse, 12 NISS with turns on both sides; of at most 5: 492, 218, 276.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `D L2 F L' F2 B U2 D' R` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `(B' R L2 F D R' F U B)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `D L2 F L' F2 B U2 D' R` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U' R F2 R` on R/L, then `D2 F2 D' B U2 B2 U` to DR on F/B; through an inverse EO: 10, `(F R U R')` on R/L, then `(D' F' D' F D B)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `D L2 F L' B` on F/B, then `F2 U2 D' R` to DR on U/D; through an inverse EO: 10, `(F D' R U R)` on R/L, then `(U F' U' R2 B)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 57

`R2 D2 L2 B2 D' F2 D' F2 R2 F2 U2 B2 D R' D2 F U' B L' B2 D F D`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 8 normal, 14 inverse, 4 NISS with turns on both sides; of at most 5: 120, 230, 204.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `F D B2 L U R2 F' U R2 B` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `(D' F' B' R B U2 B2 U' B)` (DR on U/D).
- Best of the six: 9. With NISS: 8, for example `F' R F2 B' R2 D L (D)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `F D B2 L` on R/L, then `U B F2 U' L2 F` to DR on U/D; through an inverse EO: 9, `(D' F' B' R)` on R/L, then `(B U2 B2 U' B)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F D B2 L` on R/L, then `U B F2 U' L2 F` to DR on U/D; through an inverse EO: 9, `(D' F' B' R)` on R/L, then `(B U2 B2 U' B)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 58

`L2 B2 U' F2 D L2 F2 U L2 U' B2 R2 F2 B' L2 R' B' D' R D2 R B'`

Bad edges on R/L, U/D, F/B: 6, 4, 6. EOs of at most 4 turns (all three axes): 2 normal, 14 inverse, 0 NISS with turns on both sides; of at most 5: 136, 234, 128.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `B R' D2 R' D B R L2 B` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(B2 R B L' F B2 R2 D' R)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `B R' D2 R' D B R L2 B` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 12, EO `B L F D` on U/D, then `F2 R L' F' L' B D2 R` to DR on F/B; through an inverse EO: 10, `(U2 L2 F D)` on U/D, then `(U2 F' L B2 R B)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `D2 R' F' B D'` on U/D, then `L2 U2 L' U2 L B` to DR on R/L; through an inverse EO: 10, `(U2 L2 U2 F D')` on U/D, then `(R2 B F' R' B)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 59

`B2 F2 D2 L2 D R2 U F2 L2 D F2 D L2 B2 U2 F' D2 L' D' U2 F R2 B D2 U`

Bad edges on R/L, U/D, F/B: 4, 6, 6. EOs of at most 4 turns (all three axes): 22 normal, 18 inverse, 16 NISS with turns on both sides; of at most 5: 290, 212, 236.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `F2 L' F' B2 L' F2 U2 B' D' B` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(R2 B2 L' U2 B' U L B2 D)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `(R2 B2 L' U2 B' U L B2 D)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U2 F' D2 R` on R/L, then `F B2 U' F R2 B' U` to DR on F/B; through an inverse EO: 11, `(D B L)` on R/L, then `(D B D' B2 F2 L2 U' F)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F2 L' F' B2 L'` on R/L, then `F2 U2 B' D' B` to DR on U/D; through an inverse EO: 10, `(U D' F2 B' R')` on R/L, then `(U' B L2 D' F)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 60

`U2 L2 D' L2 D F2 L2 D R2 U' L2 D' R2 F2 U L' D R2 F R F' L' F`

Bad edges on R/L, U/D, F/B: 6, 6, 4. EOs of at most 4 turns (all three axes): 20 normal, 22 inverse, 12 NISS with turns on both sides; of at most 5: 430, 296, 260.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 9, U/D 8, F/B 8), for example `F' L F R' F' R2 D' L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(D L U2 L U' B R2 U2 R)` (DR on F/B).
- Best of the six: 8. With NISS: 8, for example `F' L F R' F' R2 D' L` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U' R' U2 F` on F/B, then `U2 R2 U2 R' U' R` to DR on U/D; through an inverse EO: 10, `(D' R2 L U')` on U/D, then `(R' L' B' R F' R)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 8, EO `F2 R L D' L` on R/L, then `B' R2 D` to DR on F/B; through an inverse EO: 9, `(D L U2 L U')` on U/D, then `(B R2 U2 R)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 61

`U' B2 D F2 D' B2 D' B2 F2 D2 R2 B2 D2 R2 B' D R B' D2 U' R U2 B2 U2`

Bad edges on R/L, U/D, F/B: 6, 4, 4. EOs of at most 4 turns (all three axes): 30 normal, 16 inverse, 36 NISS with turns on both sides; of at most 5: 296, 350, 336.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `B2 R' D R2 F2 L2 D2 R' F` (DR on R/L).
- On the inverse: 8 (per axis: R/L 9, U/D 8, F/B 10), for example `(R2 L' F2 L' D2 F' D R)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `(R2 L' F2 L' D2 F' D R)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `B2 R' D` on U/D, then `R2 F2 L2 D2 R' F` to DR on R/L; through an inverse EO: 11, `(D' R B D)` on U/D, then `(B' R2 B' U2 B' D2 B)` to DR on R/L; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `B2 R' D` on U/D, then `R2 F2 L2 D2 R' F` to DR on R/L; through an inverse EO: 10, `(D2 R' F2 U L')` on R/L, then `(F L2 F' U B)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 62

`U2 F2 U L2 U F2 L2 U F2 U' L2 U L2 U2 L' D U2 B D' L' B R U'`

Bad edges on R/L, U/D, F/B: 4, 6, 4. EOs of at most 4 turns (all three axes): 6 normal, 10 inverse, 20 NISS with turns on both sides; of at most 5: 230, 210, 236.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `U B2 D' R F2 U' L' R B` (DR on R/L).
- On the inverse: 8 (per axis: R/L 10, U/D 9, F/B 8), for example `(R2 B U' B2 D' R2 F' L)` (DR on F/B).
- Best of the six: 8. With NISS: 8, for example `(R2 B U' B2 D' R2 F' L)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D' F2 L' U'` on U/D, then `F R U2 B' U2 F` to DR on R/L; through an inverse EO: 9, `(B' D' F2 L')` on R/L, then `(F R2 B U F)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D F U' B' L'` on R/L, then `B L2 U' R2 B` to DR on U/D; through an inverse EO: 8, `(R2 B U' B2 D')` on U/D, then `(R2 F' L)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 63

`D2 B2 U F2 L2 R2 D R2 F2 U R2 D' B L' B2 F' L2 D F U R`

Bad edges on R/L, U/D, F/B: 4, 8, 6. EOs of at most 4 turns (all three axes): 16 normal, 0 inverse, 8 NISS with turns on both sides; of at most 5: 248, 58, 288.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `F2 B R2 U R D' R B2 R` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(F R B2 D' B' U' F R2 B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `R' U' F' D' L2 F B2 L B` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U' B2 D L` on R/L, then `F' B U' F2 L2 U` to DR on F/B; no inverse EO; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U' B2 D L` on R/L, then `F' B U' F2 L2 U` to DR on F/B; through an inverse EO: 10, `(D2 F U F L)` on R/L, then `(U B' D B U)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 64

`B2 D F2 D2 B2 D' B2 D' R2 D' F2 U' R2 U' L' D' F' R' B L U B F' R2`

Bad edges on R/L, U/D, F/B: 10, 6, 8. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 16 NISS with turns on both sides; of at most 5: 54, 24, 128.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `L' F2 U L2 F L R' B' U` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(B2 D2 R U' F' B2 R' B L)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `L' F2 U L2 F L R' B' U` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F' U D R D'` on U/D, then `R' F' L B F` to DR on R/L; through an inverse EO: 11, `(U F D' R B)` on F/B, then `(R2 L U R' D R)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 65

`R2 D R2 F2 D F2 U' B2 L2 D B2 D2 F2 U R' U2 F' R2 B2 D' U' L' F L'`

Bad edges on R/L, U/D, F/B: 6, 10, 6. EOs of at most 4 turns (all three axes): 8 normal, 0 inverse, 8 NISS with turns on both sides; of at most 5: 68, 46, 232.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 11, U/D 10, F/B 10), for example `L F' L U D B2 R2 F U2 R` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(R' B D2 F U B U2 D R)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `(R' B D2 F U B U2 D R)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `B' U F B'` on F/B, then `U2 D L' B2 R B2 U` to DR on R/L; no inverse EO; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `U D2 F' R2 B` on F/B, then `R D2 L' F2 D R` to DR on U/D; through an inverse EO: 11, `(R F B U B)` on F/B, then `(F2 D R U2 R U)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 66

`F2 D' R2 B2 U' R2 U' F2 D2 B2 R2 U' F2 R2 D2 F' R B2 R F' L D U' F U2`

Bad edges on R/L, U/D, F/B: 4, 8, 6. EOs of at most 4 turns (all three axes): 26 normal, 24 inverse, 8 NISS with turns on both sides; of at most 5: 290, 312, 248.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `F' D B2 R2 B' R2 U' D2 F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `(R' B D' B' U' F L' D' L)` (DR on U/D).
- Best of the six: 9. With NISS: 8, for example `B U B' U' D L F (F)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `L2 U' D L` on R/L, then `F D' F' R2 U' F` to DR on U/D; through an inverse EO: 10, `(U R2 D2 R)` on R/L, then `(F' B' U F' R2 U)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L2 U' D L` on R/L, then `F D' F' R2 U' F` to DR on U/D; through an inverse EO: 10, `(U R2 D2 R)` on R/L, then `(F' B' U F' R2 U)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 67

`D' B2 D2 L2 D F2 L2 U2 F2 R2 U' R2 B2 U B' D' B' F L' F R B' R2 U'`

Bad edges on R/L, U/D, F/B: 8, 8, 8. EOs of at most 4 turns (all three axes): 4 normal, 16 inverse, 0 NISS with turns on both sides; of at most 5: 116, 200, 72.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `U R2 B R' F' L F' B D B` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(L' F U' D' B' U R' B' L)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `(L' F U' D' B' U R' B' L)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U' R L' D` on U/D, then `F' R2 B R' L' B' R` to DR on F/B; through an inverse EO: 10, `(L F R B)` on F/B, then `(U2 F2 U' L R' D)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `R2 B R' F' L` on R/L, then `U' F D F2 U' B` to DR on U/D; through an inverse EO: 10, `(L' F D R' L')` on R/L, then `(F D' R2 B U)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 68

`B2 L2 D' R2 F2 D' F2 D B2 D R2 D2 B2 L2 U' F' L D U' R B2 U L' B2`

Bad edges on R/L, U/D, F/B: 6, 6, 4. EOs of at most 4 turns (all three axes): 18 normal, 24 inverse, 4 NISS with turns on both sides; of at most 5: 368, 288, 212.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 9, F/B 9), for example `L' F' L' U2 R' U' B2 D` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `(B2 R' L2 F2 B' L B U' B)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `L' F' L' U2 R' U' B2 D` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 8, EO `L' F'` on F/B, then `L' U2 R' U' B2 D` to DR on R/L; through an inverse EO: 10, `(B D L2 B)` on F/B, then `(R L D' F2 B2 L)` to DR on U/D; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 8, EO `L' F'` on F/B, then `L' U2 R' U' B2 D` to DR on R/L; through an inverse EO: 10, `(B L' B U2 R)` on R/L, then `(D2 F2 R2 D F)` to DR on U/D; with NISS EOs too: 8.

</details>

### Scramble 69

`R2 B2 F2 D2 L2 B2 D' R2 D L2 R2 D R2 U' B' R2 D' R' F U L D2 F' D2`

Bad edges on R/L, U/D, F/B: 8, 6, 8. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 20 NISS with turns on both sides; of at most 5: 68, 4, 120.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `L F2 D F' U' B' D L2 D' L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(B' U2 F' D' L' B2 U B2 R)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `(B' U2 F' D' L' B2 U B2 R)` (DR on F/B).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `B2 L U F' R` on R/L, then `F2 D B R2 U2 F` to DR on U/D; through an inverse EO: 12, `(F2 D F L B')` on F/B, then `(D L2 R' B2 R F2 D)` to DR on R/L; with NISS EOs too: 11.

</details>

### Scramble 70

`R2 B2 U2 B2 U L2 U2 R2 U2 B2 L2 U' B' D2 L' F D2 R F' U2`

Bad edges on R/L, U/D, F/B: 6, 2, 6. EOs of at most 4 turns (all three axes): 48 normal, 60 inverse, 8 NISS with turns on both sides; of at most 5: 524, 572, 356.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 8, F/B 9), for example `L' U' L2 U' F' L2 R' B` (DR on R/L).
- On the inverse: 8 (per axis: R/L 8, U/D 9, F/B 10), for example `(U2 R2 U B' R2 U' F' U)` (DR on R/L).
- Best of the six: 8. With NISS: 8, for example `L' U' L2 U' F' L2 R' B` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 8, EO `L' U' L2 U'` on U/D, then `F' L2 R' B` to DR on R/L; through an inverse EO: 9, `(D' F2 D)` on U/D, then `(F L B2 L' R2 B)` to DR on R/L; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 8, EO `L' U' L2 U'` on U/D, then `F' L2 R' B` to DR on R/L; through an inverse EO: 9, `(D' F2 D)` on U/D, then `(F L B2 L' R2 B)` to DR on R/L; with NISS EOs too: 8.

</details>

### Scramble 71

`B2 L2 U' L2 U' F2 D R2 B2 D R2 U' F2 D2 R' F' D L' B2 R2 B D2 U'`

Bad edges on R/L, U/D, F/B: 8, 4, 6. EOs of at most 4 turns (all three axes): 2 normal, 16 inverse, 0 NISS with turns on both sides; of at most 5: 64, 326, 80.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `U D2 B' R2 B2 L D' F R` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(R2 L F U' R D2 L2 U' L)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `U D2 B' R2 B2 L D' F R` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `B' R' L2 F` on F/B, then `U B2 D' R' L' U L` to DR on U/D; through an inverse EO: 10, `(R U)` on U/D, then `(R' U2 B' D2 F2 L2 R B)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `U2 B R L' D` on U/D, then `R' B' L' B U2 B` to DR on R/L; through an inverse EO: 10, `(D R2 U R D)` on U/D, then `(L B' R' F R)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 72

`D' F2 R2 U2 R2 U B2 U F2 U R2 U2 L2 U2 B' F' D' L B R U' L2 F' R2`

Bad edges on R/L, U/D, F/B: 8, 8, 6. EOs of at most 4 turns (all three axes): 0 normal, 16 inverse, 0 NISS with turns on both sides; of at most 5: 44, 92, 80.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `R2 F L2 U R' B' L' D F B` (DR on U/D).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(R2 F' D2 R' L2 D' F' B' U' L)` (DR on U/D).
- Best of the six: 10. With NISS: 8, for example `R' L F R (D R2 B R)` (DR on U/D).
- EOs of at most 4 turns, best DR: no normal EO; through an inverse EO: 11, `(R D B' U')` on U/D, then `(D2 R B F D2 R B)` to DR on R/L; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `U2 F U L' D'` on U/D, then `B' L U2 R D2 B` to DR on R/L; through an inverse EO: 11, `(R D B' U')` on U/D, then `(D2 R B F D2 R B)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 73

`D' R2 U2 B2 F2 U F2 U' B2 L2 R2 U2 R' B' D L2 U R2 B' D2`

Bad edges on R/L, U/D, F/B: 4, 8, 6. EOs of at most 4 turns (all three axes): 4 normal, 14 inverse, 20 NISS with turns on both sides; of at most 5: 122, 162, 232.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 9, U/D 8, F/B 10), for example `D2 B R2 U' L2 D' B R` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(R' B2 D' B' L' U L2 D2 B)` (DR on R/L).
- Best of the six: 8. With NISS: 8, for example `D2 B R2 U' L2 D' B R` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `F D' R2 B` on F/B, then `D' B2 D R2 B2 U' L` to DR on U/D; through an inverse EO: 10, `(U D R)` on R/L, then `(B2 F D' B2 U' R2 B)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `U D' R2 F2 L'` on R/L, then `D' R2 F' L2 U' B` to DR on U/D; through an inverse EO: 10, `(U D R)` on R/L, then `(B2 F D' B2 U' R2 B)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 74

`D F2 U R2 U' F2 L2 D' F2 D2 L2 B2 D' L' U2 B' R U F L2 D' B R'`

Bad edges on R/L, U/D, F/B: 6, 6, 10. EOs of at most 4 turns (all three axes): 8 normal, 0 inverse, 4 NISS with turns on both sides; of at most 5: 82, 20, 112.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `F L' D' B' U B2 U F2 L F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `(L2 F L' B' U D R' D2 F)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `(B' L' F U' D2 R F2 D' B)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `F L' D2 R'` on R/L, then `U' F2 D' B U' D2 F` to DR on U/D; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `R' F L U2 R` on R/L, then `U2 B' U L2 D' F` to DR on U/D; through an inverse EO: 12, `(L2 D' F' U D')` on U/D, then `(R U2 L B R2 B R)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 75

`D' F2 U' R2 B2 L2 R2 D' R2 U2 B2 F2 U' R' D B L F' D2 B L R2 U'`

Bad edges on R/L, U/D, F/B: 8, 4, 6. EOs of at most 4 turns (all three axes): 26 normal, 10 inverse, 8 NISS with turns on both sides; of at most 5: 278, 198, 136.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 7 (per axis: R/L 10, U/D 10, F/B 7), for example `B R L2 B' L' B' U` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(U2 B R2 U R' F' L2 D2 B)` (DR on R/L).
- Best of the six: 7. With NISS: 7, for example `B R L2 B' L' B' U` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `R L2 U'` on U/D, then `B F2 U2 B D2 L B` to DR on R/L; through an inverse EO: 9, `(U2 B R2 U)` on U/D, then `(R' B' U2 L2 F)` to DR on R/L; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 7, EO `B R L2 B' L'` on R/L, then `B' U` to DR on F/B; through an inverse EO: 9, `(U2 B R2 U)` on U/D, then `(R' B' U2 L2 F)` to DR on R/L; with NISS EOs too: 7.

</details>

### Scramble 76

`U' B2 U' F2 D L2 R2 D F2 U' F2 U' R2 U F' L R2 B' D L F2 U' F' R U'`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 8 normal, 12 inverse, 24 NISS with turns on both sides; of at most 5: 108, 122, 340.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 11, F/B 10), for example `U' F' R' F R2 B' D R2 B` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(R' D2 B L F' L2 F' U' D B)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `U' F' R' F R2 B' D R2 B` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U' R D2 L'` on R/L, then `D F' B D F' L2 U` to DR on F/B; through an inverse EO: 10, `(R' D2 B L)` on R/L, then `(F' L2 F' U' D B)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `U' R D2 L'` on R/L, then `D F' B D F' L2 U` to DR on F/B; through an inverse EO: 10, `(R' D2 B L)` on R/L, then `(F' L2 F' U' D B)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 77

`U2 F2 D B2 L2 D B2 L2 D L2 U' B2 D2 L2 U' L' F U' L2 B F2 L' D2 U2`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 12 normal, 0 inverse, 24 NISS with turns on both sides; of at most 5: 174, 96, 304.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 11), for example `D2 B' R' L' F' D2 R' D B` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(U' F L D2 F' D F B L)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `D2 F' D' L' R2 D B' D F` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `R D B' L` on R/L, then `U2 L2 B' R2 U2 B` to DR on U/D; no inverse EO; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D B R' B2 L'` on R/L, then `F' U L2 U F` to DR on U/D; through an inverse EO: 11, `(D2 L B R L')` on R/L, then `(B2 U R2 U' B' U)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 78

`B2 U' R2 U' B2 L2 D2 B2 L2 U2 B2 L2 U' R2 B' D' U F R' B' R U B'`

Bad edges on R/L, U/D, F/B: 2, 6, 8. EOs of at most 4 turns (all three axes): 46 normal, 32 inverse, 12 NISS with turns on both sides; of at most 5: 454, 392, 272.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `B U' R' B R F' U' D B` (DR on U/D).
- On the inverse: 7 (per axis: R/L 9, U/D 7, F/B 10), for example `(L U' L F B2 U B)` (DR on U/D).
- Best of the six: 7. With NISS: 7, for example `(L U' L F B2 U B)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `R' B2 R` on R/L, then `F B U B R2 F2 U` to DR on F/B; through an inverse EO: 7, `(L U' L)` on R/L, then `(B2 F U B)` to DR on U/D; with NISS EOs too: 7.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `B U' R' B R` on R/L, then `F' U' D B` to DR on U/D; through an inverse EO: 7, `(L U' L)` on R/L, then `(B2 F U B)` to DR on U/D; with NISS EOs too: 7.

</details>

### Scramble 79

`R2 D' F2 R2 D' B2 L2 R2 U F2 D B2 D' F' U2 L B U2 L2 R F2 R'`

Bad edges on R/L, U/D, F/B: 6, 4, 6. EOs of at most 4 turns (all three axes): 14 normal, 28 inverse, 12 NISS with turns on both sides; of at most 5: 216, 302, 252.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `R F2 R' L2 U2 B' L' U2 F` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(D F B' L F' R' U L U)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `R F2 R' L2 U2 B' L' U2 F` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `L' F2 B R'` on R/L, then `L2 D F D B L2 D` to DR on F/B; through an inverse EO: 10, `(U D L2 U)` on U/D, then `(B2 L' U2 R F' L)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F2 R D2 F L` on R/L, then `B L2 B' L2 U` to DR on F/B; through an inverse EO: 9, `(D F B' L F')` on F/B, then `(R' U L U)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 80

`B2 D R2 U' R2 F2 L2 R2 U' F2 U' R2 U2 B2 U' B' R' D2 F2 U2 F2 U2 F' U'`

Bad edges on R/L, U/D, F/B: 4, 4, 4. EOs of at most 4 turns (all three axes): 64 normal, 82 inverse, 20 NISS with turns on both sides; of at most 5: 636, 780, 484.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `R' U2 L2 F' R2 U L' R U` (DR on R/L).
- On the inverse: 7 (per axis: R/L 8, U/D 7, F/B 9), for example `(F' D' B' L' U2 L2 B)` (DR on U/D).
- Best of the six: 7. With NISS: 7, for example `(F' D' B' L' U2 L2 B)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `R' U2 L2 F'` on F/B, then `R2 U L' R U` to DR on R/L; through an inverse EO: 7, `(F' D' B' L')` on R/L, then `(U2 L2 B)` to DR on U/D; with NISS EOs too: 7.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `U L2 U R2 U` on U/D, then `R' U2 R' F` to DR on R/L; through an inverse EO: 7, `(F' D' B' L')` on R/L, then `(U2 L2 B)` to DR on U/D; with NISS EOs too: 7.

</details>

### Scramble 81

`U' F2 U F2 L2 U F2 L2 D L2 U2 F2 R2 F2 U2 F' R' B R' D B2 L' U' L2 D2`

Bad edges on R/L, U/D, F/B: 6, 8, 8. EOs of at most 4 turns (all three axes): 32 normal, 0 inverse, 4 NISS with turns on both sides; of at most 5: 190, 10, 224.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `B U' D' L R F B R F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(R U' D R' F L R' U B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `F2 B' U D' B' U2 L R B` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `F2 B' U D'` on U/D, then `B' U2 L R B` to DR on R/L; no inverse EO; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `F2 B' U D'` on U/D, then `B' U2 L R B` to DR on R/L; through an inverse EO: 11, `(B' L F B2 R)` on R/L, then `(U B2 R2 L2 F' U)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 82

`D B2 U2 F2 R2 F2 D' R2 B2 U' B2 D F2 B' L' U R2 D2 U' B R2`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 20 normal, 8 inverse, 8 NISS with turns on both sides; of at most 5: 210, 170, 200.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 10, U/D 8, F/B 10), for example `R2 B' U D2 R2 U' L B` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `(U2 B' L2 D' U R2 L B D)` (DR on F/B).
- Best of the six: 8. With NISS: 8, for example `R2 B' U D2 R2 U' L B` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `B U L' F'` on F/B, then `L U D F2 R` to DR on U/D; through an inverse EO: 10, `(U' R2 F D')` on U/D, then `(B' R2 D2 R U2 B)` to DR on R/L; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `B U L' F'` on F/B, then `L U D F2 R` to DR on U/D; through an inverse EO: 10, `(U' B D' B2 L')` on R/L, then `(R2 F R2 U F)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 83

`U B2 L2 F2 L2 D L2 U2 F2 L2 R2 D L2 U' F' U' B D' L' B' F L2 U2`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 16 normal, 4 inverse, 4 NISS with turns on both sides; of at most 5: 152, 152, 172.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `U2 L2 F' B L D B' U F` (DR on U/D).
- On the inverse: 8 (per axis: R/L 9, U/D 8, F/B 10), for example `(R' F' B2 D' B' L' D' L)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `(R' F' B2 D' B' L' D' L)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U2 F' B L` on R/L, then `U' B R2 U F' D` to DR on F/B; through an inverse EO: 10, `(D F' D' R)` on R/L, then `(B2 D B' L2 D' F)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `U2 L2 F' B L` on R/L, then `D B' U F` to DR on U/D; through an inverse EO: 8, `(R' F' B2 D' B')` on F/B, then `(L' D' L)` to DR on U/D; with NISS EOs too: 8.

</details>

### Scramble 84

`U' F2 D B2 L2 D2 R2 F2 U' B2 F2 R2 B' L2 R' F R U2 L' R2 D'`

Bad edges on R/L, U/D, F/B: 4, 4, 6. EOs of at most 4 turns (all three axes): 52 normal, 16 inverse, 20 NISS with turns on both sides; of at most 5: 606, 248, 372.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `B' L U2 F' U' B U' D' F` (DR on U/D).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(R F D' R F' U2 F' L2 F U)` (DR on F/B).
- Best of the six: 9. With NISS: 8, for example `B' L (D B2 L2 F' U B)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `L2 D F L` on R/L, then `U' R2 B' L2 B` to DR on U/D; through an inverse EO: 10, `(R F D' R)` on R/L, then `(F' U2 F' L2 F U)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `D F U B L'` on R/L, then `U B R2 D` to DR on F/B; through an inverse EO: 10, `(R F D' R)` on R/L, then `(F' U2 F' L2 F U)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 85

`F2 R2 F2 R2 D L2 U2 R2 D2 U' B2 U2 R2 L' U' L F' U L U2 B R`

Bad edges on R/L, U/D, F/B: 6, 6, 8. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 20 NISS with turns on both sides; of at most 5: 94, 42, 280.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `R' B' U2 L' U' F L' U L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 11, U/D 9, F/B 10), for example `(L D R D L U' F' B' R)` (DR on U/D).
- Best of the six: 9. With NISS: 8, for example `D F' D' R F B (F2 D)` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `R' F' B D R'` on R/L, then `U L2 B D2 B` to DR on U/D; through an inverse EO: 11, `(D' L' F' R' L)` on R/L, then `(B D' B U F2 U)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 86

`L2 F2 U R2 F2 U2 L2 U B2 U B2 U' R2 D' L' U L2 B2 F' U' L' F2 D2`

Bad edges on R/L, U/D, F/B: 8, 4, 4. EOs of at most 4 turns (all three axes): 26 normal, 16 inverse, 12 NISS with turns on both sides; of at most 5: 400, 270, 328.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 9, F/B 10), for example `F2 D B2 L U B2 D' F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `(D2 B2 L' U2 B U' R2 U' R)` (DR on U/D).
- Best of the six: 8. With NISS: 7, for example `F (R' B D' L D' B)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `R2 D2 R D'` on U/D, then `B2 U2 B2 D2 R' F` to DR on R/L; through an inverse EO: 10, `(R' D' B L')` on R/L, then `(D R2 B' U2 R2 B)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `D2 F2 L U F` on F/B, then `B2 L2 U' L` to DR on U/D; through an inverse EO: 9, `(R B2 L B' D')` on U/D, then `(U2 F' U2 L)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 87

`D' L2 D' R2 D' R2 D2 B2 U' R2 D' B2 U2 B2 U' L' B F' D' L F R2 D2 R`

Bad edges on R/L, U/D, F/B: 4, 4, 8. EOs of at most 4 turns (all three axes): 8 normal, 24 inverse, 4 NISS with turns on both sides; of at most 5: 130, 250, 180.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 10, U/D 9, F/B 8), for example `L2 D' B D F' R' B2 D` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `(D F2 R F' B D B2 U' F)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `L2 D' B D F' R' B2 D` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `R L' B D'` on U/D, then `L' B U2 F B2 L` to DR on F/B; through an inverse EO: 9, `(D F2 R)` on R/L, then `(B F' D B2 U' F)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L2 D F' B R` on R/L, then `D' F' U R2 U` to DR on F/B; through an inverse EO: 9, `(D F2 R)` on R/L, then `(B F' D B2 U' F)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 88

`L2 U B2 R2 D' L2 D2 F2 D L2 D' B2 U' B' U' R2 B2 R' F L2 D2 F2`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 20 normal, 14 inverse, 28 NISS with turns on both sides; of at most 5: 238, 248, 260.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `F2 D2 L2 F' R B2 R2 U B` (DR on U/D).
- On the inverse: 8 (per axis: R/L 8, U/D 10, F/B 9), for example `(R F U' B' R' D2 R' D)` (DR on R/L).
- Best of the six: 8. With NISS: 8, for example `(R F U' B' R' D2 R' D)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D2 L2 F' R` on R/L, then `L2 B' D2 B2 D' F` to DR on U/D; through an inverse EO: 8, `(R F U' B')` on F/B, then `(R' D2 R' D)` to DR on R/L; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `F2 D2 L2 F' R` on R/L, then `B2 R2 U B` to DR on U/D; through an inverse EO: 8, `(R F U' B')` on F/B, then `(R' D2 R' D)` to DR on R/L; with NISS EOs too: 8.

</details>

### Scramble 89

`U L2 B2 D R2 F2 U B2 D' B2 L2 B2 F2 U2 R' U2 R2 F' R2 D' B' L F`

Bad edges on R/L, U/D, F/B: 6, 4, 8. EOs of at most 4 turns (all three axes): 6 normal, 10 inverse, 0 NISS with turns on both sides; of at most 5: 160, 226, 124.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 10, U/D 9, F/B 8), for example `R F R' D2 L B U' R` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(U2 R D2 R' B D F' L' B)` (DR on R/L).
- Best of the six: 8. With NISS: 8, for example `R F R' D2 L B U' R` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `F L B U'` on U/D, then `F U2 L B' D2 B` to DR on R/L; through an inverse EO: 11, `(D2 R B D')` on U/D, then `(F2 U2 L' B' D2 B' L)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F L B U'` on U/D, then `F U2 L B' D2 B` to DR on R/L; through an inverse EO: 10, `(F R L' F D)` on U/D, then `(R2 L2 B U2 L)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 90

`U' B2 L2 D' B2 U2 L2 U B2 F2 L2 D B2 R2 U' L' B2 R' B' U2 L2 B L2 U2`

Bad edges on R/L, U/D, F/B: 6, 2, 4. EOs of at most 4 turns (all three axes): 62 normal, 36 inverse, 20 NISS with turns on both sides; of at most 5: 672, 542, 412.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `D L' D B2 U2 F' D2 R' F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(D' R' L D' L D2 U2 R D)` (DR on F/B).
- Best of the six: 9. With NISS: 8, for example `R' D' F2 R' D B (F2 D)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `D L' D` on U/D, then `B2 U2 F' D2 R' F` to DR on R/L; through an inverse EO: 10, `(L2 U' F2 U)` on U/D, then `(L2 F U2 B L B)` to DR on R/L; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `D L' D` on U/D, then `B2 U2 F' D2 R' F` to DR on R/L; through an inverse EO: 10, `(U2 F2 D F2 D)` on U/D, then `(B' R U2 R2 B)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 91

`L2 D2 B2 R2 D' L2 D R2 B2 D' R2 F2 D2 R' F U' F2 U' L' B2 D' F2`

Bad edges on R/L, U/D, F/B: 6, 6, 4. EOs of at most 4 turns (all three axes): 2 normal, 20 inverse, 28 NISS with turns on both sides; of at most 5: 114, 182, 364.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `F2 D B2 L U F2 U F' R` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `(U L2 U' F2 D' L F D2 R)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `F2 D B2 L U F2 U F' R` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 12, EO `D' R' U' F` on F/B, then `U L' D' F2 D R D2 L` to DR on U/D; through an inverse EO: 10, `(D R' U B')` on F/B, then `(F2 U' L2 D' R' D)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D' R U' R2 F'` on F/B, then `U' F2 U B2 R` to DR on U/D; through an inverse EO: 10, `(D R' U F2 B')` on F/B, then `(U' L2 D' R' D)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 92

`R2 U2 R2 B2 D L2 B2 L2 D2 B2 U B2 U' F' U B2 L B D L2 R' D2 F'`

Bad edges on R/L, U/D, F/B: 8, 6, 10. EOs of at most 4 turns (all three axes): 8 normal, 0 inverse, 8 NISS with turns on both sides; of at most 5: 84, 64, 144.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `D2 U F L U R U2 F' D` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(U2 B' L' U F B L' D' B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `D2 U F L U R U2 F' D` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `D2 F R L` on R/L, then `F2 D F' B' U B2 U` to DR on F/B; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F R' L2 B' L'` on R/L, then `F' U B' D2 F` to DR on U/D; through an inverse EO: 11, `(D' L U B R)` on R/L, then `(U' F R2 U' L2 D)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 93

`F2 R2 D B2 R2 D' B2 D2 U' R2 U' R2 F2 U' R2 B' D L' D2 F2 R2 F' D' U2 R'`

Bad edges on R/L, U/D, F/B: 4, 6, 6. EOs of at most 4 turns (all three axes): 24 normal, 8 inverse, 0 NISS with turns on both sides; of at most 5: 290, 164, 164.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `D F L' D B2 L U' B' D` (DR on F/B).
- On the inverse: 8 (per axis: R/L 8, U/D 10, F/B 9), for example `(L2 R2 U' B' D' L2 U F)` (DR on R/L).
- Best of the six: 8. With NISS: 8, for example `(L2 R2 U' B' D' L2 U F)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `L' U2 F2 R` on R/L, then `U' B L2 U2 F2 D` to DR on F/B; through an inverse EO: 11, `(D' F U D')` on U/D, then `(B R F B2 R F R)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L' U2 F2 R` on R/L, then `U' B L2 U2 F2 D` to DR on F/B; through an inverse EO: 9, `(L2 U2 F B' R')` on R/L, then `(D' R2 F' U)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 94

`B2 R2 D' L2 U2 B2 U2 F2 R2 U' L2 F2 U' F' U' L' B2 U R D' F D2 U'`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 4 NISS with turns on both sides; of at most 5: 12, 90, 280.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `R' U B D2 B2 U F B2 R U` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(R L F' L2 U B U R' D L)` (DR on U/D).
- Best of the six: 10. With NISS: 9, for example `F U' R' B' L R2 F D (B)` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `U R' B D2 F` on F/B, then `B2 U L2 D' R' D` to DR on R/L; through an inverse EO: 11, `(R F R' D L)` on R/L, then `(D2 L2 F U L2 F)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 95

`U L2 D F2 U2 L2 B2 U R2 U L2 R2 F2 U' F' U B L' U' B' L B2 D`

Bad edges on R/L, U/D, F/B: 4, 6, 6. EOs of at most 4 turns (all three axes): 32 normal, 0 inverse, 4 NISS with turns on both sides; of at most 5: 286, 22, 208.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `D' B2 L' B U L B' U' F` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(R2 B L U R' B2 R' F U)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `F' L' F2 L2 B U F2 D B` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `L2 F' L` on R/L, then `B U F' R2 B' U F` to DR on U/D; no inverse EO; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L2 D' F' D L'` on R/L, then `D' B R2 F2 U` to DR on F/B; through an inverse EO: 11, `(U F D F R)` on R/L, then `(F2 B2 D2 B R2 U)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 96

`F2 L2 F2 D B2 U' F2 D2 L2 D B2 L2 U B2 R' U' L2 R' B D R2 U2 B' U'`

Bad edges on R/L, U/D, F/B: 2, 8, 6. EOs of at most 4 turns (all three axes): 24 normal, 22 inverse, 16 NISS with turns on both sides; of at most 5: 332, 326, 312.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `D L' F' L' B U' L' F' L` (DR on F/B).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(D2 R' U' R' B' R2 F' D B)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `D L' F' L' B U' L' F' L` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `L' B' L'` on R/L, then `F2 U' B2 F' R2 U B` to DR on U/D; through an inverse EO: 9, `(D2 R' U' R')` on R/L, then `(B' R2 F' D B)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L' B' L'` on R/L, then `F2 U' B2 F' R2 U B` to DR on U/D; through an inverse EO: 9, `(D2 R' U' R')` on R/L, then `(B' R2 F' D B)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 97

`D2 R2 U' F2 U' B2 F2 D' L2 D L2 U R2 U' L' U' L' D' B' D2 R D' B' D2`

Bad edges on R/L, U/D, F/B: 6, 6, 4. EOs of at most 4 turns (all three axes): 32 normal, 30 inverse, 36 NISS with turns on both sides; of at most 5: 380, 306, 396.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `R F D U' L2 U2 B2 R U` (DR on F/B).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(F' R2 B' U2 F' R' U2 L F)` (DR on U/D).
- Best of the six: 9. With NISS: 8, for example `B' L (U2 L' U' D B' R)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `B2 D2 L B` on F/B, then `D' R D R2 U L` to DR on U/D; through an inverse EO: 10, `(U L' B')` on F/B, then `(D R2 U R F2 D2 L)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `R B U' D R` on R/L, then `F' L2 U F' D` to DR on F/B; through an inverse EO: 10, `(U L' B')` on F/B, then `(D R2 U R F2 D2 L)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 98

`D2 L2 B2 D' L2 U2 L2 F2 D' R2 U2 F2 U' R2 U2 L' U' L' F U' R B F2`

Bad edges on R/L, U/D, F/B: 4, 6, 6. EOs of at most 4 turns (all three axes): 8 normal, 16 inverse, 0 NISS with turns on both sides; of at most 5: 152, 200, 136.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 9, U/D 8, F/B 9), for example `F2 B' R' U F' L U L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(B2 L' D B L2 F2 L' U F)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `F2 B' R' U F' L U L` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `F2 U B R` on R/L, then `F D' B D' B` to DR on U/D; through an inverse EO: 10, `(U2 R2 U' R)` on R/L, then `(B2 U2 B U2 F U)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 8, EO `F2 B' R' U F'` on F/B, then `L U L` to DR on U/D; through an inverse EO: 10, `(U2 R2 U' R)` on R/L, then `(B2 U2 B U2 F U)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 99

`U' R2 D F2 U2 L2 U' R2 U F2 L2 B2 F U2 R B' F' U' F' L2 R U'`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 4 normal, 20 inverse, 40 NISS with turns on both sides; of at most 5: 210, 196, 348.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `B2 U' F' D B' L D2 F U` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(F D F2 L2 D' R F B U)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `B L' B' U D2 B R2 F U` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D2 F B L'` on R/L, then `U B F U2 D B` to DR on U/D; through an inverse EO: 10, `(F U2 F2 R')` on R/L, then `(F' D2 B U D B)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U' F B U2 R'` on R/L, then `F' U2 F' D F` to DR on U/D; through an inverse EO: 10, `(D' B2 R2 F L')` on R/L, then `(D' F D R2 B)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 100

`B2 D2 R2 U2 L2 B2 R2 D' L2 B2 D' L2 U2 L' U2 B' R' D L2 U' L F2 U2`

Bad edges on R/L, U/D, F/B: 6, 8, 4. EOs of at most 4 turns (all three axes): 16 normal, 4 inverse, 12 NISS with turns on both sides; of at most 5: 354, 148, 204.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `B2 L' F' R D' L' R U B2 D` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(F L' F U L2 B2 U2 R' B)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `(F L' F U L2 B2 U2 R' B)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D' L' D2 F` on F/B, then `U R D B2 R D` to DR on R/L; through an inverse EO: 12, `(U' L D B)` on F/B, then `(U D' L' F2 U R' B2 L)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F2 R2 F U D'` on U/D, then `L B' D2 U2 L` to DR on F/B; through an inverse EO: 11, `(D2 B R B2 L)` on R/L, then `(D R2 B F' U' F)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 101

`F2 R2 U' F2 L2 F2 L2 U F2 D R2 D2 L2 U' R' U2 B D R' B F U B L2 U2`

Bad edges on R/L, U/D, F/B: 6, 10, 10. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 8 NISS with turns on both sides; of at most 5: 0, 4, 76.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 11, F/B 10), for example `B' L' B' U' F B D L' R2 U` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(B L' U B L2 F D B' D2 R)` (DR on U/D).
- Best of the six: 10. With NISS: 10, for example `L F R' D B2 L' B' U F D` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: no normal EO; through an inverse EO: 11, `(B' L F2 D' R)` on R/L, then `(U' B U2 R2 U' F)` to DR on U/D; with NISS EOs too: 11.

</details>

### Scramble 102

`L2 R2 D' R2 F2 U R2 D B2 U' F2 D' B' R D' U B2 R D R2 F' U'`

Bad edges on R/L, U/D, F/B: 6, 4, 6. EOs of at most 4 turns (all three axes): 22 normal, 2 inverse, 12 NISS with turns on both sides; of at most 5: 238, 174, 296.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `B U2 F2 R' U2 D' R U2 F` (DR on R/L).
- On the inverse: 8 (per axis: R/L 9, U/D 9, F/B 8), for example `(R2 U R' D U' L D' R)` (DR on F/B).
- Best of the six: 8. With NISS: 8, for example `(R2 U R' D U' L D' R)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D2 F' L2 B` on F/B, then `F2 U' L B2 D' R` to DR on U/D; through an inverse EO: 11, `(L B2 U R)` on R/L, then `(U R2 B2 R2 U' L2 U)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `B U2 F2 R' D'` on U/D, then `U2 R U2 F` to DR on R/L; through an inverse EO: 10, `(L U' B2 U R')` on R/L, then `(U L2 U F2 D)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 103

`U2 L2 U' F2 D' L2 U2 F2 D B2 U B2 U' F2 U' F' U' L2 D' L' U L R2 F U'`

Bad edges on R/L, U/D, F/B: 2, 6, 6. EOs of at most 4 turns (all three axes): 0 normal, 22 inverse, 32 NISS with turns on both sides; of at most 5: 78, 240, 344.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `U F' L' U2 L D' B L' U` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(U R' D' R D' F' R2 U2 D2 F)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `U F' L' U2 L D' B L' U` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; through an inverse EO: 10, `(U R' D' R)` on R/L, then `(D' B' D2 R2 L2 B)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `U' B' R' U' R'` on R/L, then `F' U' D' F2 B' U` to DR on F/B; through an inverse EO: 10, `(U R' D' R)` on R/L, then `(D' B' D2 R2 L2 B)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 104

`U L2 U2 L2 U' F2 D' R2 D R2 U2 B2 F L F' D2 F2 R U' L2 B' U'`

Bad edges on R/L, U/D, F/B: 6, 4, 4. EOs of at most 4 turns (all three axes): 18 normal, 40 inverse, 28 NISS with turns on both sides; of at most 5: 350, 426, 416.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `U B2 R2 B D' L F2 R' D` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(R' F' D2 F D F' U R2 U)` (DR on R/L).
- Best of the six: 9. With NISS: 7, for example `R D (U L D F' D)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `U B2 R2 B` on F/B, then `D' L F2 R' D` to DR on R/L; through an inverse EO: 10, `(R' L U' L)` on R/L, then `(D' F L2 F2 U F)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `U B2 R2 B` on F/B, then `D' L F2 R' D` to DR on R/L; through an inverse EO: 10, `(D2 R U' F2 L)` on R/L, then `(U2 D2 L2 F D)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 105

`U B2 D R2 U' L2 D2 L2 R2 U' F2 U B2 U' R' D' L' B U R B2 D U2`

Bad edges on R/L, U/D, F/B: 8, 6, 4. EOs of at most 4 turns (all three axes): 34 normal, 6 inverse, 12 NISS with turns on both sides; of at most 5: 328, 118, 200.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `U2 B L2 F2 U L U' R2 D` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `(R2 F2 L' D' R2 U R2 U2 R)` (DR on F/B).
- Best of the six: 9. With NISS: 8, for example `U2 B D2 L' U (R2 L' D)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `U2 B` on F/B, then `L2 F2 U L U' R2 D` to DR on R/L; through an inverse EO: 11, `(L U D R)` on R/L, then `(U' F U' F D' R2 B)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `U2 B` on F/B, then `L2 F2 U L U' R2 D` to DR on R/L; through an inverse EO: 10, `(B2 D' R L' B)` on F/B, then `(U B2 R B2 R)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 106

`D' B2 U2 F2 D L2 U B2 R2 U B' R2 U L F' D' R' U' L U`

Bad edges on R/L, U/D, F/B: 8, 6, 6. EOs of at most 4 turns (all three axes): 28 normal, 2 inverse, 0 NISS with turns on both sides; of at most 5: 224, 116, 112.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `R B' L B' D2 U L2 F2 B U` (DR on F/B).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(D L2 U R L' B D F' R2 U)` (DR on F/B).
- Best of the six: 10. With NISS: 8, for example `R' L2 D' F2 D2 F L (F)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `R B' L` on R/L, then `B' U D2 L2 F2 B U` to DR on F/B; through an inverse EO: 11, `(F D2 R' B)` on F/B, then `(L2 R B2 U D L' D)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `R B' L` on R/L, then `B' U D2 L2 F2 B U` to DR on F/B; through an inverse EO: 10, `(U B2 D R L')` on R/L, then `(B D F' R2 U)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 107

`B2 D' B2 R2 D' B2 U2 L2 U2 R2 U B2 F2 U' L' F L2 U' R F' D2 F' R U'`

Bad edges on R/L, U/D, F/B: 6, 2, 6. EOs of at most 4 turns (all three axes): 42 normal, 18 inverse, 20 NISS with turns on both sides; of at most 5: 440, 278, 400.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `F2 R' U F' L' U F' B' L` (DR on F/B).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(F' L F R2 B' U2 R' B2 L)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `L2 B U F' D2 L' F' L U` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D R2 D` on U/D, then `R F R B L' R' F` to DR on R/L; through an inverse EO: 10, `(L U2 F R)` on R/L, then `(F2 D' F' U2 F' D)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U L2 F2 L2 U'` on U/D, then `B' D2 R U2 L` to DR on F/B; through an inverse EO: 9, `(F' L F R2 B')` on F/B, then `(U2 R' B2 L)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 108

`F2 D F2 U' B2 F2 R2 F2 D F2 U2 B2 D' R F' L' U' B D' R' D2 R U'`

Bad edges on R/L, U/D, F/B: 10, 8, 8. EOs of at most 4 turns (all three axes): 0 normal, 8 inverse, 0 NISS with turns on both sides; of at most 5: 64, 88, 72.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 10, F/B 10), for example `F2 D2 L U R D F B` (DR on R/L).
- On the inverse: 8 (per axis: R/L 10, U/D 8, F/B 10), for example `(R' F2 B D' L' U' R' F)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `F2 D2 L U R D F B` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; through an inverse EO: 9, `(F2 R' F' B)` on F/B, then `(D' B2 L' U' R)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U2 R' U L' D` on U/D, then `F' R' F2 R B` to DR on R/L; through an inverse EO: 9, `(F2 R' F' B)` on F/B, then `(D' B2 L' U' R)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 109

`B2 R2 D2 B2 D L2 R2 U' B2 U2 F2 U' F' R F L F2 D' L2 D B`

Bad edges on R/L, U/D, F/B: 8, 4, 6. EOs of at most 4 turns (all three axes): 20 normal, 28 inverse, 4 NISS with turns on both sides; of at most 5: 312, 354, 144.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `F' D2 R2 B R2 U' L' B' R` (DR on F/B).
- On the inverse: 8 (per axis: R/L 10, U/D 10, F/B 8), for example `(F D F L2 U2 L D' R)` (DR on F/B).
- Best of the six: 8. With NISS: 7, for example `F L2 B R' F' D (D)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `F2 L' B' U` on U/D, then `F R F L' R2 F` to DR on R/L; through an inverse EO: 10, `(R2 L' B R)` on R/L, then `(L2 U B' U2 R2 U)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F2 L' B' U` on U/D, then `F R F L' R2 F` to DR on R/L; through an inverse EO: 9, `(L' F2 D' F' R')` on R/L, then `(B2 U' R2 U)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 110

`L2 U F2 D L2 B2 U2 R2 B2 R2 B2 D' L2 U' R2 B' L' D2 R' F R2 U' L B L`

Bad edges on R/L, U/D, F/B: 6, 6, 8. EOs of at most 4 turns (all three axes): 0 normal, 16 inverse, 16 NISS with turns on both sides; of at most 5: 26, 92, 276.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `F' R' U' R2 F L F2 B D` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(D' R F' B' R F2 L B2 U' L)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `F' R' U' R2 F L F2 B D` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; through an inverse EO: 10, `(D' R F' B')` on F/B, then `(R F2 L B2 U' L)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `U' F' R B2 D'` on U/D, then `F' D2 R' D2 B' R` to DR on F/B; through an inverse EO: 10, `(D' R F' B')` on F/B, then `(R F2 L B2 U' L)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 111

`F2 D2 L2 U F2 L2 R2 D L2 F2 U F2 D' F2 U' R' D' F' L2 B2 R B F' D'`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 12 normal, 0 inverse, 12 NISS with turns on both sides; of at most 5: 204, 108, 180.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `D F B' R' B2 L2 F D R` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `(D R U F B' R' F D2 F)` (DR on U/D).
- Best of the six: 9. With NISS: 8, for example `D2 B (U2 D' R' D' F' D)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D2 B' U L` on R/L, then `R2 D' F2 U L2 F` to DR on U/D; no inverse EO; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D2 R2 B' U L` on R/L, then `D' B F' D B` to DR on U/D; through an inverse EO: 10, `(U D F B' R)` on R/L, then `(U' B R2 F2 U)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 112

`R2 D B2 D' B2 U2 R2 B2 L2 F2 D2 U F2 L' D F R2 D U2 B' R'`

Bad edges on R/L, U/D, F/B: 4, 6, 4. EOs of at most 4 turns (all three axes): 24 normal, 18 inverse, 16 NISS with turns on both sides; of at most 5: 252, 360, 348.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 10, U/D 8, F/B 9), for example `R B U2 D' R2 F' D' L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `(U F R F2 U R' U2 B2 D)` (DR on R/L).
- Best of the six: 8. With NISS: 8, for example `R B U2 D' R2 F' D' L` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U F2 R` on R/L, then `D' R2 B D' R2 F D` to DR on F/B; through an inverse EO: 9, `(U F)` on F/B, then `(R F2 U R' U2 B2 D)` to DR on R/L; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U F2 R` on R/L, then `D' R2 B D' R2 F D` to DR on F/B; through an inverse EO: 9, `(F L' U D' L)` on R/L, then `(F U2 F' D)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 113

`B2 L2 F2 L2 D R2 U' B2 U2 B2 L2 U' R2 U L2 U F' U' R F' R2 U' L' B' U'`

Bad edges on R/L, U/D, F/B: 8, 6, 8. EOs of at most 4 turns (all three axes): 12 normal, 8 inverse, 28 NISS with turns on both sides; of at most 5: 116, 124, 212.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `U B L U R2 F R' U F` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(R F' U' L D B L2 D F)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `U B L U R2 F R' U F` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U R B L` on R/L, then `F' U' L2 D R2 B` to DR on U/D; through an inverse EO: 9, `(R F' U' L)` on R/L, then `(D B L2 D F)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U R B L` on R/L, then `F' U' L2 D R2 B` to DR on U/D; through an inverse EO: 9, `(R F' U' L)` on R/L, then `(D B L2 D F)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 114

`L2 F2 R2 U2 L2 F2 U' L2 D B2 R2 U B2 U2 L' F' U2 L U L2 R' U2 B D`

Bad edges on R/L, U/D, F/B: 8, 8, 8. EOs of at most 4 turns (all three axes): 8 normal, 0 inverse, 4 NISS with turns on both sides; of at most 5: 72, 96, 84.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `B R B' L2 B L U F' B' D` (DR on F/B).
- On the inverse: 10 (per axis: R/L 11, U/D 11, F/B 10), for example `(D' B' U B' R L2 B L' F' U)` (DR on F/B).
- Best of the six: 10. With NISS: 10, for example `R F2 U' F2 L' D B L' U' F` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `L2 B R L` on R/L, then `U B' D' B' D F' D` to DR on F/B; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `L2 B R L` on R/L, then `U B' D' B' D F' D` to DR on F/B; through an inverse EO: 11, `(F2 L2 B' U D)` on U/D, then `(B L' F' L2 B R)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 115

`L2 U F2 U2 B2 U F2 L2 F2 U' F2 R2 F' L' D2 B2 U2 F' D' F D2 U'`

Bad edges on R/L, U/D, F/B: 4, 8, 6. EOs of at most 4 turns (all three axes): 20 normal, 22 inverse, 0 NISS with turns on both sides; of at most 5: 202, 218, 192.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `R' D' L2 D' B U' F D F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `(U2 F' L' F' D' U' F' B U)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `R' D' L2 D' B U' F D F` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `F' U F' R` on R/L, then `B' D B' U' R2 B` to DR on U/D; through an inverse EO: 9, `(U2 F' L')` on R/L, then `(F' U' D' F' B U)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L2 U L2 F2 R'` on R/L, then `U F' D L2 B` to DR on U/D; through an inverse EO: 9, `(U2 F' L')` on R/L, then `(F' U' D' F' B U)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 116

`U R2 B2 D' B2 D F2 D L2 B2 D2 B2 U B' D L D2 B D2 F' U L' D'`

Bad edges on R/L, U/D, F/B: 6, 8, 6. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 8 NISS with turns on both sides; of at most 5: 44, 60, 192.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `L' D L F2 B L B' D R2 F` (DR on U/D).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(F U' D R2 L' B U2 R B2 L)` (DR on U/D).
- Best of the six: 10. With NISS: 8, for example `U' L2 B2 L D' F' U (R)` (DR on F/B).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `L U B D2 R` on R/L, then `F' U2 L2 D B' U` to DR on F/B; through an inverse EO: 11, `(U' R B2 D' L)` on R/L, then `(F' B' U F' B2 D)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 117

`U B2 F2 D B2 F2 U' R2 D' U' R2 B2 U R' B2 D F' D' R2 B' U' F' U`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 14 normal, 22 inverse, 8 NISS with turns on both sides; of at most 5: 204, 230, 212.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `L2 F' D' B' D F2 R' F2 U` (DR on F/B).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(B' R' U' F R U' D' F' U2 B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `L2 F' D' B' D F2 R' F2 U` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `R F B' R` on R/L, then `U B' D' L2 U R2 B` to DR on U/D; through an inverse EO: 11, `(D' F2 D' L)` on R/L, then `(U2 B F U L2 D B)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L2 F L2 B' R` on R/L, then `D B' U' F U` to DR on F/B; through an inverse EO: 11, `(U L F2 U' L)` on R/L, then `(U2 F' U' F2 D B)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 118

`B2 U' B2 R2 B2 U B2 D' U2 B2 U F2 R' F L2 D' B D' B D'`

Bad edges on R/L, U/D, F/B: 4, 4, 2. EOs of at most 4 turns (all three axes): 46 normal, 90 inverse, 44 NISS with turns on both sides; of at most 5: 676, 872, 504.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 10, U/D 8, F/B 9), for example `D B' D B' D L2 F' R` (DR on U/D).
- On the inverse: 8 (per axis: R/L 8, U/D 9, F/B 9), for example `(B D2 R' F2 L2 R' F D)` (DR on R/L).
- Best of the six: 8. With NISS: 8, for example `D B' D B' D L2 F' R` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `B R L2 D'` on U/D, then `F2 B D2 U2 L` to DR on F/B; through an inverse EO: 9, `(L F' R' D)` on U/D, then `(R' D2 B2 L2 F)` to DR on R/L; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `R2 B2 L2 U R` on R/L, then `U B L2 B` to DR on U/D; through an inverse EO: 9, `(L F' R' D)` on U/D, then `(R' D2 B2 L2 F)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 119

`D L2 D U2 F2 D B2 U' L2 U L2 B2 R F D2 L' B' F' D' R' U2`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 4 normal, 0 inverse, 20 NISS with turns on both sides; of at most 5: 66, 42, 168.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `D2 B' L' D B' R' F R2 D` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(F B' R B2 U R2 L D2 B U)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `D2 B' L' D B' R' F R2 D` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D' L F2 U'` on U/D, then `F' B' R' L B L` to DR on F/B; no inverse EO; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D2 R' F R' L'` on R/L, then `F' R2 U D B` to DR on U/D; through an inverse EO: 11, `(U L F' B' D)` on U/D, then `(B R' B' L' B' L)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 120

`B2 D B2 D F2 L2 F2 R2 D L2 B2 D2 F2 U2 R' B2 F2 D U' B L' D' F2 U2`

Bad edges on R/L, U/D, F/B: 4, 6, 4. EOs of at most 4 turns (all three axes): 24 normal, 24 inverse, 28 NISS with turns on both sides; of at most 5: 340, 260, 400.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `F' R' D2 F' U L' D' F' D` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(L2 U F2 U D2 L' U' L' F)` (DR on R/L).
- Best of the six: 9. With NISS: 8, for example `R' U B' D (L' D' B' L)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `R D2 L' F` on F/B, then `L U R F2 L D` to DR on R/L; through an inverse EO: 11, `(U2 B R)` on R/L, then `(B2 L2 B' U F R2 F' D)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `R2 D' R F' U` on U/D, then `F B2 R' U2 R` to DR on F/B; through an inverse EO: 11, `(U2 B R)` on R/L, then `(B2 L2 B' U F R2 F' D)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 121

`F2 U' B2 U2 B2 L2 U' L2 U F2 L2 R2 U' F2 U F' U' L F2 D L2 F L B' U2`

Bad edges on R/L, U/D, F/B: 4, 6, 8. EOs of at most 4 turns (all three axes): 20 normal, 8 inverse, 4 NISS with turns on both sides; of at most 5: 174, 124, 100.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `B R' L F' B2 R' U L' D' L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(F' D' B' U2 R B2 U2 R' F)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `(F' D' B' U2 R B2 U2 R' F)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `F' D B' R` on R/L, then `B' L2 F U R2 D` to DR on F/B; through an inverse EO: 10, `(L U' L2 D')` on U/D, then `(L F' R B2 L B)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `F' D B' R` on R/L, then `B' L2 F U R2 D` to DR on F/B; through an inverse EO: 10, `(L U' L2 D')` on U/D, then `(L F' R B2 L B)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 122

`D2 F2 U B2 R2 D2 L2 D R2 U L2 R2 L' D R2 B F D B' F2 R2 U'`

Bad edges on R/L, U/D, F/B: 4, 6, 6. EOs of at most 4 turns (all three axes): 8 normal, 28 inverse, 28 NISS with turns on both sides; of at most 5: 168, 240, 248.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `R2 U B R2 F' D2 U2 R D` (DR on F/B).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(D R F U L2 D' L D2 B)` (DR on R/L).
- Best of the six: 9. With NISS: 8, for example `D (F2 B D' U' B L D)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U' D F' R` on R/L, then `U B D B U' F' U` to DR on F/B; through an inverse EO: 10, `(D' R2 U' R)` on R/L, then `(D' F2 U2 B R2 U)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D F2 U' F' R'` on R/L, then `F2 U2 B U D` to DR on F/B; through an inverse EO: 10, `(D' R2 U' R)` on R/L, then `(D' F2 U2 B R2 U)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 123

`D L2 F2 U B2 D' F2 R2 B2 F2 U2 R2 U' R2 U' B' D L' R2 F L D' F' U' L`

Bad edges on R/L, U/D, F/B: 4, 4, 6. EOs of at most 4 turns (all three axes): 34 normal, 10 inverse, 8 NISS with turns on both sides; of at most 5: 554, 288, 272.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `D L B D' F2 U2 F B' D` (DR on F/B).
- On the inverse: 7 (per axis: R/L 9, U/D 9, F/B 7), for example `(R' D2 L2 B U' B' R)` (DR on F/B).
- Best of the six: 7. With NISS: 7, for example `(R' D2 L2 B U' B' R)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `D L` on R/L, then `B D' F2 U2 F B' D` to DR on F/B; through an inverse EO: 10, `(R2 F D2 R)` on R/L, then `(D' B R2 F B2 D)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `D L` on R/L, then `B D' F2 U2 F B' D` to DR on F/B; through an inverse EO: 7, `(R' D2 L2 B U')` on U/D, then `(B' R)` to DR on F/B; with NISS EOs too: 7.

</details>

### Scramble 124

`B2 U' R2 D L2 B2 R2 F2 U F2 U' R2 U L2 U' F' L2 R2 D2 F R' B L D R'`

Bad edges on R/L, U/D, F/B: 8, 4, 6. EOs of at most 4 turns (all three axes): 22 normal, 4 inverse, 12 NISS with turns on both sides; of at most 5: 322, 162, 180.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `L' B' L2 F D F2 R F2 U L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `(F' B U2 L' B R2 B2 D R)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `(B' L D2 R' B D2 L F U)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `L' B' L2 F` on F/B, then `D F2 R F2 U L` to DR on U/D; through an inverse EO: 11, `(U' L B' R)` on R/L, then `(U2 D2 B D' L2 F U)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `R D' L' B' R` on R/L, then `B' L2 U2 D2 B` to DR on U/D; through an inverse EO: 9, `(F' B U2 L' B)` on F/B, then `(R2 B2 D R)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 125

`R2 F2 D2 L2 D2 R2 B2 U L2 R2 F2 R2 U2 B' L' D U2 L R2 D2 F D2`

Bad edges on R/L, U/D, F/B: 4, 6, 4. EOs of at most 4 turns (all three axes): 32 normal, 42 inverse, 8 NISS with turns on both sides; of at most 5: 366, 366, 188.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `B2 L' F R2 L F L2 D R` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `(B U F U F' L B' L2 D)` (DR on F/B).
- Best of the six: 9. With NISS: 8, for example `L2 B2 R' B2 R' F' R (L)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `U F D2 L` on R/L, then `F2 D' F U' D' F` to DR on U/D; through an inverse EO: 10, `(U D2 F2 R')` on R/L, then `(F' R2 U' F' R2 D)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U F D2 L` on R/L, then `F2 D' F U' D' F` to DR on U/D; through an inverse EO: 10, `(U D2 F2 R')` on R/L, then `(F' R2 U' F' R2 D)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 126

`D F2 U F2 L2 B2 U' R2 B2 R2 D L2 U' L' D B2 D R' B' U' R'`

Bad edges on R/L, U/D, F/B: 4, 8, 4. EOs of at most 4 turns (all three axes): 26 normal, 24 inverse, 24 NISS with turns on both sides; of at most 5: 306, 482, 244.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 9, U/D 8, F/B 10), for example `R U B R D' B2 D' L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `(B2 D R' U F B2 U' F2 L)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `R U B R D' B2 D' L` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 8, EO `R U B` on F/B, then `R D' B2 D' L` to DR on U/D; through an inverse EO: 10, `(U R2 F R)` on R/L, then `(B' U2 B D2 B D)` to DR on F/B; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 8, EO `R U B` on F/B, then `R D' B2 D' L` to DR on U/D; through an inverse EO: 9, `(B2 D R' U F)` on F/B, then `(B2 U' F2 L)` to DR on U/D; with NISS EOs too: 8.

</details>

### Scramble 127

`B2 D B2 D' L2 B2 F2 D R2 B2 F2 U2 B2 U' L' D2 U' B2 D' F L' D' B' U'`

Bad edges on R/L, U/D, F/B: 6, 6, 8. EOs of at most 4 turns (all three axes): 8 normal, 12 inverse, 8 NISS with turns on both sides; of at most 5: 126, 154, 252.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 11), for example `U B D L F' D B2 U D2 L` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(F' D' R2 L U' L2 F B' L)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `(F' D' R2 L U' L2 F B' L)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `D' L B2 R'` on R/L, then `U' F' U' R2 F2 B U` to DR on F/B; through an inverse EO: 11, `(R' L B' R)` on R/L, then `(F2 D' R2 F' R2 U B)` to DR on U/D; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U B D L F'` on F/B, then `D B2 U D2 L` to DR on U/D; through an inverse EO: 9, `(F' D' R2 L U')` on U/D, then `(L2 F B' L)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 128

`U' B2 U' R2 D F2 U2 L2 B2 L2 D F2 D2 R2 F' U' R2 B' R' F2 L B F' U2`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 8 normal, 2 inverse, 4 NISS with turns on both sides; of at most 5: 136, 102, 100.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `L F L B R F' L2 F' U' B` (DR on U/D).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(R' L' F D2 B' R' L2 B2 U' L)` (DR on U/D).
- Best of the six: 10. With NISS: 9, for example `B' L F (U2 B2 U F2 B' D)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U R' F2 D` on U/D, then `R U2 R' B' L F R` to DR on F/B; through an inverse EO: 11, `(D' L2 F U)` on U/D, then `(B U2 F L' F' D2 R)` to DR on F/B; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `L F L B R` on R/L, then `F' L2 F' U' B` to DR on U/D; through an inverse EO: 10, `(R' L' F D2 B')` on F/B, then `(R' L2 B2 U' L)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 129

`B2 L2 D' B2 U' F2 U B2 F2 L2 F2 D2 B' D R U' L' B D U' R D' U'`

Bad edges on R/L, U/D, F/B: 10, 8, 6. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 24 NISS with turns on both sides; of at most 5: 30, 16, 264.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 11, F/B 10), for example `B2 R' F U L' R2 F' R2 D` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 11, F/B 10), for example `(U' L2 R B U' L B2 D F U)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `B2 R' F U L' R2 F' R2 D` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `D F' U2 R' B'` on F/B, then `U' R L' U' D R` to DR on U/D; through an inverse EO: 11, `(F2 R U' B D)` on U/D, then `(R2 L D2 F2 B' L)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 130

`D' F2 D' F2 R2 U' F2 U F2 U' B2 L2 U2 R B' D R' U L' D L' R' U'`

Bad edges on R/L, U/D, F/B: 6, 6, 4. EOs of at most 4 turns (all three axes): 28 normal, 22 inverse, 12 NISS with turns on both sides; of at most 5: 252, 194, 232.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `F2 R' F' U2 B2 D' R F2 U` (DR on R/L).
- On the inverse: 8 (per axis: R/L 8, U/D 9, F/B 10), for example `(L U B2 D F2 L' U2 B)` (DR on R/L).
- Best of the six: 8. With NISS: 8, for example `(L R2 U B2 D' L' U2 B)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `F2 R' F'` on F/B, then `U2 B2 D' R F2 U` to DR on R/L; through an inverse EO: 8, `(L U B2 D)` on U/D, then `(F2 L' U2 B)` to DR on R/L; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `F2 R' F'` on F/B, then `U2 B2 D' R F2 U` to DR on R/L; through an inverse EO: 8, `(R2 L U B2 D')` on U/D, then `(L' U2 B)` to DR on R/L; with NISS EOs too: 8.

</details>

### Scramble 131

`B2 D' R2 D2 B2 D F2 U2 R2 U' B2 R2 U2 L' U' R' F' D' F2 L B' D2 L`

Bad edges on R/L, U/D, F/B: 8, 6, 6. EOs of at most 4 turns (all three axes): 0 normal, 4 inverse, 8 NISS with turns on both sides; of at most 5: 0, 108, 184.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `B U B L2 R U R' F2 R F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(L F R' L2 F D' L' U2 B)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `(L F R' L2 F D' L' U2 B)` (DR on U/D).
- EOs of at most 4 turns, best DR: no normal EO; through an inverse EO: 10, `(F' L U' R)` on R/L, then `(D' B U2 B' L2 D)` to DR on F/B; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: no normal EO; through an inverse EO: 10, `(F' L U' R)` on R/L, then `(D' B U2 B' L2 D)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 132

`B2 D' R2 U R2 U R2 B2 U2 L2 U R2 U' R2 U' B' D L2 D' L F L D' L`

Bad edges on R/L, U/D, F/B: 6, 4, 6. EOs of at most 4 turns (all three axes): 6 normal, 4 inverse, 32 NISS with turns on both sides; of at most 5: 178, 184, 388.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 9), for example `F' B' U' F' L U R' D R` (DR on U/D).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `(B R' F' D' B2 U' F2 B R)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `L' D L' F' L' D L2 D' B` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `F' B' U' F'` on F/B, then `L U R' D R` to DR on U/D; through an inverse EO: 11, `(R2 L' F D)` on U/D, then `(R' F B' L F2 B L)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `L' D L' F' L'` on R/L, then `D L2 D' B` to DR on U/D; through an inverse EO: 10, `(U' R L' D L')` on R/L, then `(B' R2 U' D2 B)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 133

`F2 U R2 B2 R2 F2 D' L2 U' L2 U' R2 L' B' R' U' L' F' U2 B2 R U2`

Bad edges on R/L, U/D, F/B: 8, 6, 8. EOs of at most 4 turns (all three axes): 0 normal, 4 inverse, 40 NISS with turns on both sides; of at most 5: 116, 166, 408.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `U2 B U' L' R B U' F U` (DR on R/L).
- On the inverse: 8 (per axis: R/L 8, U/D 10, F/B 10), for example `(D F B2 L' B' D' R' D)` (DR on R/L).
- Best of the six: 8. With NISS: 8, for example `(D F B2 L' B' D' R' D)` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; through an inverse EO: 9, `(U D L U')` on U/D, then `(L' B2 F L' B)` to DR on R/L; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `R' L U B R` on R/L, then `F' D' B R2 L2 D` to DR on F/B; through an inverse EO: 8, `(D F B2 L' B')` on F/B, then `(D' R' D)` to DR on R/L; with NISS EOs too: 8.

</details>

### Scramble 134

`D R2 B2 U' L2 U B2 U' R2 D R2 B2 F2 L' F D' B U L' R2 F' R' D2 U2`

Bad edges on R/L, U/D, F/B: 10, 10, 8. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 0 NISS with turns on both sides; of at most 5: 24, 32, 8.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 11, F/B 10), for example `B' R' U L' F D' L' B' U` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `(D2 L' D R' F B U' L' D)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `B' R' U L' F D' L' B' U` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; no EO at all.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `R' U F' D' B` on F/B, then `R U' D L U L` to DR on U/D; through an inverse EO: 12, `(D' R B L F)` on F/B, then `(R' D R D' L D L)` to DR on U/D; with NISS EOs too: 11.

</details>

### Scramble 135

`U2 R2 U L2 F2 U B2 U' B2 U L2 D R2 U2 R' U B' L U L' B2 F L' D2`

Bad edges on R/L, U/D, F/B: 8, 4, 8. EOs of at most 4 turns (all three axes): 6 normal, 14 inverse, 12 NISS with turns on both sides; of at most 5: 172, 268, 156.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `F2 D' L B2 R' F' U' L B` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(F2 D' L' F B' L R' B2 U)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `F2 D' L B2 R' F' U' L B` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `D2 R2 B D'` on U/D, then `L' U2 F2 D2 F B2 L` to DR on F/B; through an inverse EO: 10, `(B' R' F L')` on R/L, then `(D2 B' U F' D' F)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `D2 R2 B D'` on U/D, then `L' U2 F2 D2 F B2 L` to DR on F/B; through an inverse EO: 9, `(F2 D' L' F B')` on F/B, then `(L R' B2 U)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 136

`B2 L2 D L2 F2 U L2 U2 B2 D2 U' F' U R' D B L' R2 B F U'`

Bad edges on R/L, U/D, F/B: 8, 4, 8. EOs of at most 4 turns (all three axes): 32 normal, 28 inverse, 16 NISS with turns on both sides; of at most 5: 384, 430, 284.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `F L' B R' D U2 L2 B D` (DR on F/B).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(R' F' R D R' B' L R D2 B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `F L' B R' D U2 L2 B D` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `F L' B R'` on R/L, then `U2 D L2 B D` to DR on F/B; through an inverse EO: 10, `(R' F' R D)` on U/D, then `(R' B' L R D2 B)` to DR on R/L; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `F L' B R'` on R/L, then `U2 D L2 B D` to DR on F/B; through an inverse EO: 10, `(R' F' R D)` on U/D, then `(R' B' L R D2 B)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 137

`L2 D B2 L2 U L2 U2 F2 L2 B2 L2 R2 B' L' R2 F L' F' U B' L`

Bad edges on R/L, U/D, F/B: 4, 6, 4. EOs of at most 4 turns (all three axes): 28 normal, 24 inverse, 44 NISS with turns on both sides; of at most 5: 356, 280, 408.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `U' B U' B2 D L F2 U2 F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(B' U B2 R' U D' F' R U)` (DR on R/L).
- Best of the six: 9. With NISS: 8, for example `U (D2 F L U F R2 D)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `B' D B L` on R/L, then `F B U D2 F' U` to DR on F/B; through an inverse EO: 10, `(D2 F L)` on R/L, then `(U2 L2 D R2 F' B U)` to DR on F/B; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 9, EO `U' B U' B2 D` on U/D, then `L B2 D2 F` to DR on R/L; through an inverse EO: 10, `(D B' U' F' L')` on R/L, then `(D F2 L2 F' D)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 138

`B2 F2 L2 F2 D2 F2 U L2 U F2 R2 U F2 R' F' U' B' L U F2 U' B`

Bad edges on R/L, U/D, F/B: 8, 4, 6. EOs of at most 4 turns (all three axes): 12 normal, 16 inverse, 28 NISS with turns on both sides; of at most 5: 142, 256, 332.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `L2 D2 L' F' R' F B2 D' B` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 10), for example `(F L2 F' B2 R' D L D2 B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `L2 D2 L' F' R' F B2 D' B` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `D2 L' F2 U` on U/D, then `B' R2 U2 L' B R` to DR on F/B; through an inverse EO: 10, `(R U2 B' U)` on U/D, then `(B2 F' U2 L2 R' F)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D2 L' F2 U` on U/D, then `B' R2 U2 L' B R` to DR on F/B; through an inverse EO: 10, `(R U2 B' U)` on U/D, then `(B2 F' U2 L2 R' F)` to DR on R/L; with NISS EOs too: 9.

</details>

### Scramble 139

`D U2 B2 U' L2 U B2 U' B2 D' R2 U L' F' R' U' L' R F D2 L U'`

Bad edges on R/L, U/D, F/B: 4, 6, 4. EOs of at most 4 turns (all three axes): 2 normal, 4 inverse, 8 NISS with turns on both sides; of at most 5: 84, 90, 240.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 11, U/D 10, F/B 10), for example `U2 D2 F D2 R D' B2 R' U' F` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(R F U' F2 R2 L U F2 L)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `(R F U' F2 R2 L U F2 L)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `R' U D' F` on F/B, then `U D2 F2 B2 L2 R' U` to DR on R/L; through an inverse EO: 12, `(B' U D' R)` on R/L, then `(B U D' R2 B2 F2 D' F)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `F R2 F D' L'` on R/L, then `F' U2 D' F L2 U` to DR on F/B; through an inverse EO: 11, `(B U B D' R)` on R/L, then `(D2 F L2 U' L2 F)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 140

`F2 U' R2 F2 D' R2 D' R2 B2 D' L2 U B2 R2 U L' B' F D L' U' R2 B L2 U'`

Bad edges on R/L, U/D, F/B: 6, 4, 10. EOs of at most 4 turns (all three axes): 24 normal, 0 inverse, 8 NISS with turns on both sides; of at most 5: 208, 96, 152.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 7 (per axis: R/L 7, U/D 10, F/B 9), for example `R B D' F B R B` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(B D F L2 D' L' B R' D2 B)` (DR on R/L).
- Best of the six: 7. With NISS: 7, for example `R B D' F B R B` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 7, EO `R B D'` on U/D, then `B F R B` to DR on R/L; no inverse EO; with NISS EOs too: 7.
- EOs of at most 5 turns, best DR: through a normal EO: 7, EO `R B D'` on U/D, then `B F R B` to DR on R/L; through an inverse EO: 10, `(B D F L2 D')` on U/D, then `(L' B R' D2 B)` to DR on R/L; with NISS EOs too: 7.

</details>

### Scramble 141

`B2 D' L2 U F2 D L2 U2 F2 D2 B2 R D' F R2 U B L U' L`

Bad edges on R/L, U/D, F/B: 6, 6, 6. EOs of at most 4 turns (all three axes): 2 normal, 0 inverse, 4 NISS with turns on both sides; of at most 5: 66, 90, 148.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 9, F/B 9), for example `L' F' L2 U L' B' U' R' D` (DR on R/L).
- On the inverse: 8 (per axis: R/L 10, U/D 8, F/B 9), for example `(L U' F B D R' D F)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `(L U' F B D R' D F)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 12, EO `B' R2 L' F` on F/B, then `L' D2 R U' L D R' D` to DR on R/L; no inverse EO; with NISS EOs too: 12.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U2 F B L' F` on F/B, then `L' D L U D` to DR on R/L; through an inverse EO: 10, `(L' U' B D2 R')` on R/L, then `(D B R2 U' B)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 142

`F2 U R2 U R2 D' F2 U B2 D B2 L2 D' L2 R' U2 F' D' F' R2 F' D2 F2 D'`

Bad edges on R/L, U/D, F/B: 4, 4, 6. EOs of at most 4 turns (all three axes): 8 normal, 18 inverse, 16 NISS with turns on both sides; of at most 5: 156, 254, 288.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 10, F/B 10), for example `B L2 R U' R' B R F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `(F' R D2 U' R D' U F D)` (DR on F/B).
- Best of the six: 8. With NISS: 8, for example `F' R F D' F2 D2 F' D` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 8, EO `B R L2 U'` on U/D, then `R' B R F` to DR on R/L; through an inverse EO: 10, `(F2 B2 U L)` on R/L, then `(D2 F U' F2 B D)` to DR on F/B; with NISS EOs too: 8.
- EOs of at most 5 turns, best DR: through a normal EO: 8, EO `B R L2 U'` on U/D, then `R' B R F` to DR on R/L; through an inverse EO: 9, `(F' R U' D2 R)` on R/L, then `(U D' F D)` to DR on F/B; with NISS EOs too: 8.

</details>

### Scramble 143

`B2 L2 F2 U L2 D2 B2 L2 D R2 D B2 F' R2 U B D2 L' F D2 B`

Bad edges on R/L, U/D, F/B: 4, 8, 6. EOs of at most 4 turns (all three axes): 16 normal, 40 inverse, 12 NISS with turns on both sides; of at most 5: 188, 462, 200.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 9, F/B 9), for example `B' U F B D' B2 L F` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(B' R U' D' B2 L2 F L2 D B)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `B' U F B D' B2 L F` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 9, EO `B' D2 F' L` on R/L, then `D2 B' U' R2 F` to DR on U/D; through an inverse EO: 10, `(U' B' U2 R)` on R/L, then `(B2 D' B' F D' F)` to DR on U/D; with NISS EOs too: 9.
- EOs of at most 5 turns, best DR: through a normal EO: 8, EO `B' U F B D'` on U/D, then `B2 L F` to DR on R/L; through an inverse EO: 10, `(U' B' U2 R)` on R/L, then `(B2 D' B' F D' F)` to DR on U/D; with NISS EOs too: 8.

</details>

### Scramble 144

`L2 U F2 D R2 B2 L2 F2 U' B2 U2 L2 B2 F' D' B2 R' D U' F' R B2 U'`

Bad edges on R/L, U/D, F/B: 6, 8, 4. EOs of at most 4 turns (all three axes): 8 normal, 18 inverse, 12 NISS with turns on both sides; of at most 5: 140, 276, 180.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 8 (per axis: R/L 8, U/D 10, F/B 10), for example `L U F L D' B2 L B` (DR on R/L).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(F R D2 R2 U2 B' U R L)` (DR on U/D).
- Best of the six: 8. With NISS: 8, for example `L U F L D' B2 L B` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `F2 L U D'` on U/D, then `F L U2 F' L' F` to DR on R/L; through an inverse EO: 10, `(R L2 F')` on F/B, then `(U' F2 L2 F2 L2 R' D)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 8, EO `L U F L D'` on U/D, then `B2 L B` to DR on R/L; through an inverse EO: 10, `(R L2 F')` on F/B, then `(U' F2 L2 F2 L2 R' D)` to DR on R/L; with NISS EOs too: 8.

</details>

### Scramble 145

`B2 L2 B2 D' B2 U L2 U2 F2 U' B2 U' F2 R2 L' D F D U B U' R2 D L'`

Bad edges on R/L, U/D, F/B: 2, 10, 8. EOs of at most 4 turns (all three axes): 24 normal, 38 inverse, 0 NISS with turns on both sides; of at most 5: 280, 396, 152.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `L' F2 D' L U B D F B2 D` (DR on R/L).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(R U' R D R2 B' U2 B2 U F)` (DR on U/D).
- Best of the six: 10. With NISS: 9, for example `L' D B R2 U D B L (F)` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `D2 L U L` on R/L, then `F D F' B' U B2 U` to DR on F/B; through an inverse EO: 10, `(U R U2 R)` on R/L, then `(U F2 D B U F)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `U' D2 R B2 R'` on R/L, then `D' R2 F' U' D B` to DR on U/D; through an inverse EO: 10, `(U R U2 R)` on R/L, then `(U F2 D B U F)` to DR on U/D; with NISS EOs too: 10.

</details>

### Scramble 146

`F2 R2 D' L2 B2 D2 F2 U R2 F2 U L2 R2 U2 B' U F' L' F L R D U' L`

Bad edges on R/L, U/D, F/B: 10, 6, 6. EOs of at most 4 turns (all three axes): 0 normal, 0 inverse, 16 NISS with turns on both sides; of at most 5: 38, 16, 208.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 9, U/D 10, F/B 9), for example `L B' L2 R' D L2 U F U` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 10, F/B 11), for example `(L U R' D' R' F B' D' B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `L B' L2 R' D L2 U F U` (DR on R/L).
- EOs of at most 4 turns, best DR: no normal EO; no inverse EO; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `R' U L' B D` on U/D, then `L' B2 R' D2 F L` to DR on F/B; through an inverse EO: 11, `(L U' B' U2 F)` on F/B, then `(R2 F2 R' F2 R D)` to DR on R/L; with NISS EOs too: 10.

</details>

### Scramble 147

`D L2 U2 L2 B2 D2 F2 U F2 U L2 U' B' L F L2 F2 L2 U R F U'`

Bad edges on R/L, U/D, F/B: 6, 6, 8. EOs of at most 4 turns (all three axes): 4 normal, 4 inverse, 4 NISS with turns on both sides; of at most 5: 86, 128, 128.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 10, F/B 9), for example `F' B2 L' F2 D B' L2 U L` (DR on F/B).
- On the inverse: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `(R' L U' F R' L2 F' D F U)` (DR on F/B).
- Best of the six: 9. With NISS: 9, for example `F' B2 L' F2 D B' L2 U L` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 12, EO `L U2 F' R` on R/L, then `B U2 D' L2 F L2 D' F` to DR on U/D; through an inverse EO: 12, `(L' D2 F R)` on R/L, then `(U2 F U B2 R2 B' D F)` to DR on U/D; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `D' F' D B U'` on U/D, then `F' L U2 B' R` to DR on F/B; through an inverse EO: 10, `(R' L U' F R')` on R/L, then `(L2 F' D F U)` to DR on F/B; with NISS EOs too: 10.

</details>

### Scramble 148

`R2 F2 L2 D' B2 D F2 D2 R2 D R2 F2 U2 B2 U2 R' U' L2 B U L' U F2 U2`

Bad edges on R/L, U/D, F/B: 6, 6, 4. EOs of at most 4 turns (all three axes): 14 normal, 22 inverse, 8 NISS with turns on both sides; of at most 5: 200, 228, 232.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `U2 F2 U' L U' B' L2 U R` (DR on U/D).
- On the inverse: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `(R2 L D L' B' R U2 D2 R)` (DR on U/D).
- Best of the six: 9. With NISS: 9, for example `U2 F2 U' L U' B' L2 U R` (DR on U/D).
- EOs of at most 4 turns, best DR: through a normal EO: 10, EO `F2 U2 L B'` on F/B, then `F2 U2 L' U R L` to DR on U/D; through an inverse EO: 10, `(R2 D F2 B)` on F/B, then `(R U' B2 R U L)` to DR on U/D; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 10, EO `U F2 U2 L B'` on F/B, then `L B2 R' D L` to DR on U/D; through an inverse EO: 9, `(R2 L D L' B')` on F/B, then `(R U2 D2 R)` to DR on U/D; with NISS EOs too: 9.

</details>

### Scramble 149

`D R2 B2 U L2 U2 L2 D' B2 U2 L' B' D' R B2 U' B F' R2 D'`

Bad edges on R/L, U/D, F/B: 8, 8, 6. EOs of at most 4 turns (all three axes): 12 normal, 12 inverse, 8 NISS with turns on both sides; of at most 5: 180, 132, 196.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 10 (per axis: R/L 10, U/D 10, F/B 10), for example `B R D' L' B U B U2 L' F` (DR on R/L).
- On the inverse: 9 (per axis: R/L 9, U/D 9, F/B 10), for example `(F R2 D R B U' F' L' B)` (DR on R/L).
- Best of the six: 9. With NISS: 9, for example `(U2 L B' L' F U D R F)` (DR on R/L).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `U2 L B' R` on R/L, then `B' U D' F B R2 U` to DR on F/B; through an inverse EO: 10, `(F' D B U)` on U/D, then `(D2 L D2 B' U2 F)` to DR on R/L; with NISS EOs too: 10.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `U2 L B' R` on R/L, then `B' U D' F B R2 U` to DR on F/B; through an inverse EO: 10, `(U2 F D B U)` on U/D, then `(F B R' B' L)` to DR on F/B; with NISS EOs too: 9.

</details>

### Scramble 150

`R2 D2 B2 R2 U' F2 D L2 U' R2 F2 U' B2 U' L' F' R' F2 D' B' U L F`

Bad edges on R/L, U/D, F/B: 6, 8, 6. EOs of at most 4 turns (all three axes): 8 normal, 0 inverse, 0 NISS with turns on both sides; of at most 5: 104, 28, 64.

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

- Shortest DR on the normal side: 9 (per axis: R/L 10, U/D 9, F/B 10), for example `F' L' U' B D F2 R F L` (DR on U/D).
- On the inverse: 8 (per axis: R/L 10, U/D 10, F/B 8), for example `(D' L' F' U' R D' F' L)` (DR on F/B).
- Best of the six: 8. With NISS: 8, for example `(R F L2 B2 L' D U' L)` (DR on F/B).
- EOs of at most 4 turns, best DR: through a normal EO: 11, EO `F' U F B` on F/B, then `U R2 L' U L D' R` to DR on U/D; no inverse EO; with NISS EOs too: 11.
- EOs of at most 5 turns, best DR: through a normal EO: 11, EO `R' L F U D` on U/D, then `L F U2 F2 B2 L` to DR on F/B; through an inverse EO: 11, `(R' F2 U' D L')` on R/L, then `(D' R2 U B D2 F)` to DR on U/D; with NISS EOs too: 11.

</details>

## Part 2. EO to DR, 60 states by case

Each is a scramble from the study's sample and one of its EOs of at most 4 turns. The cases are in order of how often they come up after an EO (most common first). The summary line under each gives the case on each DR axis; the table gives the turns to DR each way, all with the EO kept unless the row says otherwise.

### 6c6e

**6c6e, example 1.** Scramble `L2 U2 F2 U R2 U' B2 D B2 U B2 U' B2 U R' U R2 F' L' F2 L2 B' R U'`, EO `U R' B2 D` on U/D (4 turns). After it, the case is 6c6e for DR on F/B and 5c6e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (6c6e), EO kept | 8 | `F' B' R' F' U2 R2 F2 R` |
| DR on F/B on the inverse (6c6e there), EO kept | 7 | `(B U2 L' F' R F2 R)` |
| DR on F/B, last EO turn the other way (`U R' B2 D'`) | 7 | `B' L' F D2 R2 B R` |
| DR on R/L (5c6e), EO kept | 7 | `B L' U2 L' D2 L B` |
| DR on R/L on the inverse (5c6e there), EO kept | 8 | `(L U2 L B' D2 F' R B)` |
| DR on R/L, last EO turn the other way (`U R' B2 D'`) | 8 | `D2 B L' U2 L' D2 L B` |

</details>

**6c6e, example 2.** Scramble `U2 F2 U' F2 U L2 B2 D B2 D' L2 R2 B2 U' R' U F' R D L D B' F' U'`, EO `U R2 L D` on U/D (4 turns). After it, the case is 6c6e for DR on R/L and 4c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (6c6e), EO kept | 7 | `F' U2 L F U2 R' B` |
| DR on R/L on the inverse (6c6e there), EO kept | 8 | `(R2 D2 F L' B2 R' D2 F)` |
| DR on R/L, last EO turn the other way (`U R2 L D'`) | 8 | `L B D2 B F D2 R F` |
| DR on F/B (4c6e), EO kept | 6 | `B' U2 F' R U2 L` |
| DR on F/B on the inverse (4c6e there), EO kept | 8 | `(F R2 F' R2 B' R' D2 L)` |
| DR on F/B, last EO turn the other way (`U R2 L D'`) | 7 | `F' B L B R2 D2 R` |

</details>

**6c6e, example 3.** Scramble `B2 F2 D' B2 F2 L2 D' B2 D' F2 U F2 U' F2 B' F' R' D' R2 U2 L' F U`, EO `L U F' R` on R/L (4 turns). After it, the case is 6c6e for DR on U/D and 6c4e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (6c6e), EO kept | 7 | `B U2 D' B' R2 D' B` |
| DR on U/D on the inverse (6c6e there), EO kept | 8 | `(F2 U' F D L2 B2 U' B)` |
| DR on U/D, last EO turn the other way (`L U F' R'`) | 7 | `B U2 D' B' R2 D' B` |
| DR on F/B (6c4e), EO kept | 7 | `B' D' F' U2 L2 F' U` |
| DR on F/B on the inverse (6c4e there), EO kept | 8 | `(F2 U F' R2 B R2 F' U)` |
| DR on F/B, last EO turn the other way (`L U F' R'`) | 8 | `F U F2 U F2 L2 B U` |

</details>

### 5c6e

**5c6e, example 1.** Scramble `U B2 R2 U' R2 U B2 D' F2 R2 U L2 F2 L' U' R' F2 D F' R B R U'`, EO `U B R F` on F/B (4 turns). After it, the case is 5c6e for DR on R/L and 7c4e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (5c6e), EO kept | 8 | `R2 F2 R U L2 D' R D` |
| DR on R/L on the inverse (5c6e there), EO kept | 6 | `(U L' D2 F2 L D)` |
| DR on R/L, last EO turn the other way (`U B R F'`) | 7 | `U' L2 R D2 F2 L' U` |
| DR on U/D (7c4e), EO kept | 8 | `U' R2 B2 U2 L' U2 D' L` |
| DR on U/D on the inverse (7c4e there), EO kept | 9 | `(U L D2 R U' R F2 B2 R)` |
| DR on U/D, last EO turn the other way (`U B R F'`) | 8 | `R U' R' B2 U2 R' F2 R` |

</details>

**5c6e, example 2.** Scramble `U2 F2 U2 F2 L2 U' B2 D' F2 U' R2 U2 F2 R2 U2 R' U2 F' L2 D' L R D' F' L2 U'`, EO `U D2 L D` on U/D (4 turns). After it, the case is 5c6e for DR on R/L and 4c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (5c6e), EO kept | 8 | `F L D2 L F' L R' F` |
| DR on R/L on the inverse (5c6e there), EO kept | 8 | `(L2 B' R U2 B L R B)` |
| DR on R/L, last EO turn the other way (`U D2 L D'`) | 8 | `L R F L' U2 F2 L' B` |
| DR on F/B (4c6e), EO kept | 8 | `U2 B' D2 F' D2 R' F2 L` |
| DR on F/B on the inverse (4c6e there), EO kept | 9 | `(F R B' R U2 R F2 B' L)` |
| DR on F/B, last EO turn the other way (`U D2 L D'`) | 9 | `F R2 F' R F' D2 R2 F2 R` |

</details>

**5c6e, example 3.** Scramble `D' L2 R2 B2 D' F2 L2 U B2 L2 D2 L2 U' L' F D2 U' F' D2 L2 B' D' U'`, EO `L' B U L'` on R/L (4 turns). After it, the case is 5c6e for DR on U/D and 5c8e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (5c6e), EO kept | 9 | `U F2 R2 U B2 F' R2 D B` |
| DR on U/D on the inverse (5c6e there), EO kept | 8 | `(U' B U B2 D' B L2 F)` |
| DR on U/D, last EO turn the other way (`L' B U L`) | 8 | `B' F2 U R2 F U D F` |
| DR on F/B (5c8e), EO kept | 8 | `F2 U2 D' L2 U' F B' D` |
| DR on F/B on the inverse (5c8e there), EO kept | 8 | `(L2 F' U L2 D F' B U)` |
| DR on F/B, last EO turn the other way (`L' B U L`) | 9 | `U B R2 F U' F R2 F2 D` |

</details>

### 6c4e

**6c4e, example 1.** Scramble `F2 R2 D B2 U R2 B2 F2 D2 F2 D' F2 U' B2 U2 L' D' B2 U2 L2 R' B' R`, EO `U' D R' U` on U/D (4 turns). After it, the case is 6c4e for DR on R/L and 7c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (6c4e), EO kept | 9 | `L2 B L B' U2 D2 B2 R F` |
| DR on R/L on the inverse (6c4e there), EO kept | 8 | `(R F U2 L R' D2 R B)` |
| DR on R/L, last EO turn the other way (`U' D R' U'`) | 8 | `F R U2 D2 B R U2 F` |
| DR on F/B (7c6e), EO kept | 8 | `F B R' L2 B' D2 B2 L` |
| DR on F/B on the inverse (7c6e there), EO kept | 6 | `(R' L B' U2 B L)` |
| DR on F/B, last EO turn the other way (`U' D R' U'`) | 8 | `F B R' D2 U2 R2 F R` |

</details>

**6c4e, example 2.** Scramble `F2 L2 F2 L2 U2 L2 D L2 D L2 F2 D2 L' U' F2 U' F' D R' B2 F`, EO `F2 D' L2 F` on F/B (4 turns). After it, the case is 6c4e for DR on R/L and 5c6e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (6c4e), EO kept | 8 | `U R' U F2 U B2 L D` |
| DR on R/L on the inverse (6c4e there), EO kept | 8 | `(R2 U D L2 U' L' R D)` |
| DR on R/L, last EO turn the other way (`F2 D' L2 F'`) | 9 | `L U' D R B2 U F2 R' D` |
| DR on U/D (5c6e), EO kept | 8 | `U2 R' F2 U' L' F2 D R` |
| DR on U/D on the inverse (5c6e there), EO kept | 7 | `(L2 D2 R D F2 U L)` |
| DR on U/D, last EO turn the other way (`F2 D' L2 F'`) | 7 | `R U D' R L U' R` |

</details>

**6c4e, example 3.** Scramble `L2 B2 D' R2 F2 U' B2 D B2 U F2 L2 F2 D' U' R' B L' D' B U B U2 R U'`, EO `U2 D' R L` on R/L (4 turns). After it, the case is 6c4e for DR on U/D and 5c8e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (6c4e), EO kept | 9 | `D F U R2 D L2 B2 U2 B` |
| DR on U/D on the inverse (6c4e there), EO kept | 8 | `(U' D' B' D B2 D R2 F)` |
| DR on U/D, last EO turn the other way (`U2 D' R L'`) | 9 | `U2 F R2 U2 D' B F U F` |
| DR on F/B (5c8e), EO kept | 8 | `F D' R2 U' F' D B' D` |
| DR on F/B on the inverse (5c8e there), EO kept | 8 | `(U' L2 F2 B' U' D' F D)` |
| DR on F/B, last EO turn the other way (`U2 D' R L'`) | 7 | `U' F' B2 D F2 B' D` |

</details>

### 4c6e

**4c6e, example 1.** Scramble `U2 B2 U' R2 U F2 U2 R2 B2 F2 R2 B2 U2 L' B D' U' L' R' F' L2 F'`, EO `D L B R` on R/L (4 turns). After it, the case is 4c6e for DR on U/D and 2c8e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (4c6e), EO kept | 7 | `B U' L2 D' B2 R2 F` |
| DR on U/D on the inverse (4c6e there), EO kept | 9 | `(D B2 D2 R2 B' L2 B2 D F)` |
| DR on U/D, last EO turn the other way (`D L B R'`) | 7 | `U R2 L2 D2 B R2 F` |
| DR on F/B (2c8e), EO kept | 9 | `U' F U F' U' B' U B2 D` |
| DR on F/B on the inverse (2c8e there), EO kept | 9 | `(F D B' U' R2 D L2 B D)` |
| DR on F/B, last EO turn the other way (`D L B R'`) | 9 | `U F2 U F' B' U F' B2 D` |

</details>

**4c6e, example 2.** Scramble `U B2 U' B2 U F2 D' F2 U' F2 D2 L2 U' L2 B' U L' B D F' D R' U`, EO `D B' U' R'` on R/L (4 turns). After it, the case is 4c6e for DR on U/D and 4c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (4c6e), EO kept | 7 | `B' F2 U F U2 D B` |
| DR on U/D on the inverse (4c6e there), EO kept | 7 | `(U' D2 F2 U' B' D2 F)` |
| DR on U/D, last EO turn the other way (`D B' U' R`) | 6 | `B' U' B' U D' F` |
| DR on F/B (4c6e), EO kept | 6 | `U L2 B U2 B' D` |
| DR on F/B on the inverse (4c6e there), EO kept | 8 | `(F' D2 B U L2 F2 B2 U)` |
| DR on F/B, last EO turn the other way (`D B' U' R`) | 6 | `U L2 B U2 B' D` |

</details>

**4c6e, example 3.** Scramble `F2 R2 B2 D F2 R2 D' B2 U F2 L2 U' F' U' B' L2 F' D R' F' R U'`, EO `U R' F R'` on R/L (4 turns). After it, the case is 4c6e for DR on U/D and 6c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (4c6e), EO kept | 7 | `R2 D' B D2 F U F` |
| DR on U/D on the inverse (4c6e there), EO kept | 8 | `(D L2 B' D' L2 B2 D2 B)` |
| DR on U/D, last EO turn the other way (`U R' F R`) | 6 | `D' B D2 F U F` |
| DR on F/B (6c6e), EO kept | 8 | `F U' B U D B L2 U` |
| DR on F/B on the inverse (6c6e there), EO kept | 8 | `(F' R2 U D R2 L2 B' D)` |
| DR on F/B, last EO turn the other way (`U R' F R`) | 8 | `F' D2 B U' D L2 B U` |

</details>

### 5c4e

**5c4e, example 1.** Scramble `B2 U R2 U' F2 D2 R2 B2 U' F2 D' F2 U' F2 U B' R D L D R B F2 D2`, EO `U' D R U` on U/D (4 turns). After it, the case is 5c4e for DR on F/B and 6c4e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (5c4e), EO kept | 8 | `L2 F D2 U2 L' F D2 L` |
| DR on F/B on the inverse (5c4e there), EO kept | 9 | `(F R F2 R2 L' U2 F2 B' L)` |
| DR on F/B, last EO turn the other way (`U' D R U'`) | 8 | `F2 R2 B L U2 L' F R` |
| DR on R/L (6c4e), EO kept | 8 | `R' F2 R' B F2 L' R B` |
| DR on R/L on the inverse (6c4e there), EO kept | 8 | `(L B' U2 B L B R B)` |
| DR on R/L, last EO turn the other way (`U' D R U'`) | 7 | `R D2 F R' F R' F` |

</details>

**5c4e, example 2.** Scramble `R2 U L2 D F2 D2 R2 F2 U B2 R2 U B2 L' B F2 L2 U2 L2 U' R B'`, EO `U B' D B` on F/B (4 turns). After it, the case is 5c4e for DR on R/L and 6c6e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (5c4e), EO kept | 8 | `U2 B2 L D F2 L2 R' U` |
| DR on R/L on the inverse (5c4e there), EO kept | 8 | `(U L2 D L U L2 R2 U)` |
| DR on R/L, last EO turn the other way (`U B' D B'`) | 7 | `D2 R' D' R' B2 R' D` |
| DR on U/D (6c6e), EO kept | 8 | `R L D' R' U' R' D' R` |
| DR on U/D on the inverse (6c6e there), EO kept | 7 | `(D' R' U R2 L U' L)` |
| DR on U/D, last EO turn the other way (`U B' D B'`) | 8 | `R D R D' L U D2 R` |

</details>

**5c4e, example 3.** Scramble `R2 D F2 D' B2 L2 R2 D L2 U' R2 U L2 U B' R2 D' U' L' B2 D' B D R'`, EO `R B2 D L` on R/L (4 turns). After it, the case is 5c4e for DR on U/D and 7c2e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (5c4e), EO kept | 8 | `B2 U B2 L2 F' U R2 F` |
| DR on U/D on the inverse (5c4e there), EO kept | 7 | `(D B' D' B2 D' R2 F)` |
| DR on U/D, last EO turn the other way (`R B2 D L'`) | 7 | `B2 U B2 F' U R2 F` |
| DR on F/B (7c2e), EO kept | 8 | `D R2 F U' B L2 B' U` |
| DR on F/B on the inverse (7c2e there), EO kept | 8 | `(U D' B R2 D' B' R2 U)` |
| DR on F/B, last EO turn the other way (`R B2 D L'`) | 8 | `D F' B2 D' F2 D F' D` |

</details>

### 7c6e

**7c6e, example 1.** Scramble `D2 B2 U F2 R2 F2 U' B2 L2 R2 D R2 F' L2 U L' D R B' U2 R' U'`, EO `U D' B2 U` on U/D (4 turns). After it, the case is 7c6e for DR on R/L and 8c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (7c6e), EO kept | 7 | `L' R' F R' U2 L F` |
| DR on R/L on the inverse (7c6e there), EO kept | 8 | `(R F' R' B F' L B F)` |
| DR on R/L, last EO turn the other way (`U D' B2 U'`) | 8 | `L' B R' B2 F R D2 B` |
| DR on F/B (8c6e), EO kept | 9 | `F' R D2 F2 U2 R F' B' L` |
| DR on F/B on the inverse (8c6e there), EO kept | 8 | `(R2 L F R B' D2 U2 R)` |
| DR on F/B, last EO turn the other way (`U D' B2 U'`) | 8 | `B2 R B L' F' R U2 L` |

</details>

**7c6e, example 2.** Scramble `F2 L2 D' B2 D F2 D' F2 R2 D2 U' B2 U' L2 F' D L2 F2 D' U R' B F2 D`, EO `U' D B L` on R/L (4 turns). After it, the case is 7c6e for DR on F/B and 5c6e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (7c6e), EO kept | 9 | `F B2 U' B2 U B R2 F U` |
| DR on F/B on the inverse (7c6e there), EO kept | 9 | `(F R2 B' D' B U' F' R2 U)` |
| DR on F/B, last EO turn the other way (`U' D B L'`) | 8 | `F2 U F' U2 B R2 L2 U` |
| DR on U/D (5c6e), EO kept | 7 | `F U L2 B' D' L2 F` |
| DR on U/D on the inverse (5c6e there), EO kept | 9 | `(D' B' U2 F' R2 D B' D2 B)` |
| DR on U/D, last EO turn the other way (`U' D B L'`) | 8 | `R2 B D L2 F' U' L2 B` |

</details>

**7c6e, example 3.** Scramble `B2 D' R2 U B2 F2 D F2 D2 U' R2 U' L2 F' D' L U B D B2 L2 R' D'`, EO `L' U2 D R` on R/L (4 turns). After it, the case is 7c6e for DR on U/D and 5c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (7c6e), EO kept | 9 | `U2 F' L2 B U' L2 B2 D2 F` |
| DR on U/D on the inverse (7c6e there), EO kept | 8 | `(U' D B' F U' L2 U' F)` |
| DR on U/D, last EO turn the other way (`L' U2 D R'`) | 8 | `D' B F U' F' R2 U' B` |
| DR on F/B (5c6e), EO kept | 8 | `F U L2 U' F L2 B D` |
| DR on F/B on the inverse (5c6e there), EO kept | 9 | `(F2 B2 D' R2 B R2 U' F2 D)` |
| DR on F/B, last EO turn the other way (`L' U2 D R'`) | 7 | `F2 L2 B U' R2 B' D` |

</details>

### 4c4e

**4c4e, example 1.** Scramble `L2 U L2 D R2 B2 U L2 U' B2 R2 D' R2 U' B' U' F L' B R2 U B R U'`, EO `R B2 L' F` on F/B (4 turns). After it, the case is 4c4e for DR on U/D and 3c6e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (4c4e), EO kept | 8 | `U D2 F2 U R2 D F2 L` |
| DR on U/D on the inverse (4c4e there), EO kept | 7 | `(B2 U L2 D' R2 F2 L)` |
| DR on U/D, last EO turn the other way (`R B2 L' F'`) | 8 | `U R2 F2 B2 D B2 D L` |
| DR on R/L (3c6e), EO kept | 8 | `L2 U2 D' R D R B2 D` |
| DR on R/L on the inverse (3c6e there), EO kept | 8 | `(U L' U2 L' D2 L' B2 U)` |
| DR on R/L, last EO turn the other way (`R B2 L' F'`) | 7 | `U2 D' R' F2 D2 L' U` |

</details>

**4c4e, example 2.** Scramble `B2 R2 U2 B2 D L2 D2 L2 F2 U' R2 U2 L2 U2 L' D' B' R D2 B' F2 U2 F`, EO `D2 F R' B` on F/B (4 turns). After it, the case is 4c4e for DR on U/D and 4c6e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (4c4e), EO kept | 7 | `L2 U2 R2 U2 F2 U L` |
| DR on U/D on the inverse (4c4e there), EO kept | 8 | `(U2 D F2 D' L2 U F2 R)` |
| DR on U/D, last EO turn the other way (`D2 F R' B'`) | 7 | `R2 B2 U D F2 U R` |
| DR on R/L (4c6e), EO kept | 7 | `D' F2 L' U2 D2 R U` |
| DR on R/L on the inverse (4c6e there), EO kept | 8 | `(L2 U L' R U2 B2 L' U)` |
| DR on R/L, last EO turn the other way (`D2 F R' B'`) | 7 | `D L' U' L2 U' B2 U` |

</details>

**4c4e, example 3.** Scramble `B2 U2 R2 D' L2 U2 B2 R2 F2 L2 U F2 D2 F2 R2 U2 R' F L2 U' L' R' F L2 D2`, EO `D L F` on F/B (3 turns). After it, the case is 4c4e for DR on R/L and 3c4e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (4c4e), EO kept | 6 | `F2 L U2 F2 L' D` |
| DR on R/L on the inverse (4c4e there), EO kept | 7 | `(L B2 R D2 L' B2 D)` |
| DR on R/L, last EO turn the other way (`D L F'`) | 5 | `L U2 F2 L' D` |
| DR on U/D (3c4e), EO kept | 8 | `R L U R D R2 U' L` |
| DR on U/D on the inverse (3c4e there), EO kept | 7 | `(R' U D F2 R' D' R)` |
| DR on U/D, last EO turn the other way (`D L F'`) | 8 | `R L D L U L2 D' R` |

</details>

### 7c4e

**7c4e, example 1.** Scramble `D' R2 D F2 D' B2 F2 L2 U B2 R2 D2 U' R U' L' U B' U F2 R2 D2`, EO `U2 R' U2 D` on U/D (4 turns). After it, the case is 7c4e for DR on R/L and 6c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (7c4e), EO kept | 9 | `L R' F L2 F L' U2 L2 B` |
| DR on R/L on the inverse (7c4e there), EO kept | 9 | `(R B' F R B2 R B L2 F)` |
| DR on R/L, last EO turn the other way (`U2 R' U2 D'`) | 9 | `L R' F R2 B U2 D2 R B` |
| DR on F/B (6c6e), EO kept | 8 | `B R F' R2 D2 R2 B R` |
| DR on F/B on the inverse (6c6e there), EO kept | 8 | `(B L' F' R B U2 F L)` |
| DR on F/B, last EO turn the other way (`U2 R' U2 D'`) | 8 | `L' B2 R' F B' R D2 R` |

</details>

**7c4e, example 2.** Scramble `B2 U B2 L2 F2 R2 D2 B2 D U2 R2 B2 R' F2 D' L R2 D B' F' R D'`, EO `D R F B` on F/B (4 turns). After it, the case is 7c4e for DR on R/L and 5c6e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (7c4e), EO kept | 7 | `U R' U R' F2 R2 D` |
| DR on R/L on the inverse (7c4e there), EO kept | 9 | `(L U' L' B2 L D' L R2 D)` |
| DR on R/L, last EO turn the other way (`D R F B'`) | 7 | `U R' U R' F2 R2 D` |
| DR on U/D (5c6e), EO kept | 7 | `D' R U' L U D2 L` |
| DR on U/D on the inverse (5c6e there), EO kept | 9 | `(U2 R' U R L U' F2 U2 R)` |
| DR on U/D, last EO turn the other way (`D R F B'`) | 8 | `U2 R2 U R' L2 F2 U' L` |

</details>

**7c4e, example 3.** Scramble `B2 R2 D2 L2 D B2 D2 F2 D' R2 U2 L2 B2 L' D2 F D' R2 B L2 U F'`, EO `U2 B D2 R'` on R/L (4 turns). After it, the case is 7c4e for DR on U/D and 6c4e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (7c4e), EO kept | 9 | `U R2 D' R2 U F U2 D' F` |
| DR on U/D on the inverse (7c4e there), EO kept | 8 | `(B U' D2 B' U R2 U' F)` |
| DR on U/D, last EO turn the other way (`U2 B D2 R`) | 8 | `L2 U' R2 L2 F' U2 D' F` |
| DR on F/B (6c4e), EO kept | 8 | `D2 B D F U' D B' U` |
| DR on F/B on the inverse (6c4e there), EO kept | 8 | `(R2 B2 U' F2 B' U' F U)` |
| DR on F/B, last EO turn the other way (`U2 B D2 R`) | 8 | `U2 F' U B U D' F' D` |

</details>

### 6c8e

**6c8e, example 1.** Scramble `U B2 R2 U R2 D F2 D' L2 F2 D' R2 F2 D2 F' D2 L' D U' B' L' D U2 L2`, EO `L' F' D' B` on F/B (4 turns). After it, the case is 6c8e for DR on R/L and 4c6e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (6c8e), EO kept | 8 | `R' D' R U2 L' U' F2 D` |
| DR on R/L on the inverse (6c8e there), EO kept | 8 | `(U D R' F2 U' F2 L2 D)` |
| DR on R/L, last EO turn the other way (`L' F' D' B'`) | 7 | `R' U' L' B2 L' B2 D` |
| DR on U/D (4c6e), EO kept | 8 | `L2 F2 U' F2 D R' U2 L` |
| DR on U/D on the inverse (4c6e there), EO kept | 8 | `(D L D B2 R' L D' R)` |
| DR on U/D, last EO turn the other way (`L' F' D' B'`) | 8 | `D' R U' R L U2 D' R` |

</details>

**6c8e, example 2.** Scramble `D2 F2 D' B2 L2 U2 B2 D2 F2 L' U' L' U' B' L2 R U2 F' D'`, EO `U D' B L` on R/L (4 turns). After it, the case is 6c8e for DR on U/D and 6c8e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (6c8e), EO kept | 8 | `U' R2 F' D2 B U D2 B` |
| DR on U/D on the inverse (6c8e there), EO kept | 7 | `(B D' B2 F' L2 D' B)` |
| DR on U/D, last EO turn the other way (`U D' B L'`) | 9 | `U F U2 B' D F' R2 U' F` |
| DR on F/B (6c8e), EO kept | 8 | `F' U' B' D' B U' F U` |
| DR on F/B on the inverse (6c8e there), EO kept | 8 | `(F2 D' B R2 U D B D)` |
| DR on F/B, last EO turn the other way (`U D' B L'`) | 8 | `D' F B D' F2 D2 F U` |

</details>

**6c8e, example 3.** Scramble `F2 L2 D U2 B2 D L2 D' R2 D2 U' B2 L' F' D' B' D2 R D' B' L U2`, EO `D F R L` on R/L (4 turns). After it, the case is 6c8e for DR on U/D and 6c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (6c8e), EO kept | 9 | `U B F' D' B F' U B F` |
| DR on U/D on the inverse (6c8e there), EO kept | 8 | `(B F R2 U L2 D R2 B)` |
| DR on U/D, last EO turn the other way (`D F R L'`) | 8 | `B' D B2 U B F' U B` |
| DR on F/B (6c6e), EO kept | 9 | `F D' F' U2 D2 F' U R2 D` |
| DR on F/B on the inverse (6c6e there), EO kept | 8 | `(F' B' U B' U2 R2 B' D)` |
| DR on F/B, last EO turn the other way (`D F R L'`) | 8 | `B U D F' B' D2 B' U` |

</details>

### 5c8e

**5c8e, example 1.** Scramble `R2 D R2 U' F2 U2 R2 U' L2 U2 B2 U B2 U F2 L' D2 B' R2 F D2 U' B R2 U2`, EO `U F B2 R` on R/L (4 turns). After it, the case is 5c8e for DR on F/B and 8c4e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (5c8e), EO kept | 7 | `D' F' U' B2 D B' D` |
| DR on F/B on the inverse (5c8e there), EO kept | 8 | `(F' U' L2 F' U D B' U)` |
| DR on F/B, last EO turn the other way (`U F B2 R'`) | 8 | `U' B2 R2 B U D F' U` |
| DR on U/D (8c4e), EO kept | 9 | `U F' D B F' D R2 L2 B` |
| DR on U/D on the inverse (8c4e there), EO kept | 9 | `(U2 F D' R2 B' L2 U2 D B)` |
| DR on U/D, last EO turn the other way (`U F B2 R'`) | 9 | `B' U D2 B2 D B U2 D' B` |

</details>

**5c8e, example 2.** Scramble `L2 B2 D L2 D B2 L2 R2 U B2 U2 L2 D' R2 U' B' L B2 U2 L' U' R2 F L U'`, EO `D2 B' D2 L` on R/L (4 turns). After it, the case is 5c8e for DR on U/D and 4c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (5c8e), EO kept | 9 | `B R2 F' L2 D' F U' D2 B` |
| DR on U/D on the inverse (5c8e there), EO kept | 9 | `(U D' B U' D' F L2 U' B)` |
| DR on U/D, last EO turn the other way (`D2 B' D2 L'`) | 8 | `B2 F' L2 B D L2 U' B` |
| DR on F/B (4c6e), EO kept | 8 | `F' B' R2 U B2 U2 F D` |
| DR on F/B on the inverse (4c6e there), EO kept | 8 | `(U2 R2 F2 U2 B' U L2 D)` |
| DR on F/B, last EO turn the other way (`D2 B' D2 L'`) | 9 | `F2 U2 B' D' F' U2 D' F U` |

</details>

**5c8e, example 3.** Scramble `B2 U' R2 D2 L2 U B2 L2 U' L2 D2 L2 R2 U' B' U L' F R2 D' R' B2 F' D' U'`, EO `U B2 R D'` on U/D (4 turns). After it, the case is 5c8e for DR on F/B and 6c6e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (5c8e), EO kept | 8 | `F L' F R' L2 F U2 L` |
| DR on F/B on the inverse (5c8e there), EO kept | 8 | `(F' R2 L D2 R' F' B L)` |
| DR on F/B, last EO turn the other way (`U B2 R D`) | 8 | `F' R2 D2 L F L2 B R` |
| DR on R/L (6c6e), EO kept | 7 | `L U2 B D2 L U2 B` |
| DR on R/L on the inverse (6c6e there), EO kept | 7 | `(U2 B2 F L D2 L B)` |
| DR on R/L, last EO turn the other way (`U B2 R D`) | 8 | `B L U2 L B L' R' B` |

</details>

### 4c8e

**4c8e, example 1.** Scramble `L2 D B2 R2 U R2 D R2 B2 U2 B2 R2 U' R2 U2 L' D F L R' F L D F'`, EO `F U2 R' B` on F/B (4 turns). After it, the case is 4c8e for DR on R/L and 6c6e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (4c8e), EO kept | 9 | `L D' L2 R D B2 D' L U` |
| DR on R/L on the inverse (4c8e there), EO kept | 9 | `(R F2 U F2 U B2 D L' U)` |
| DR on R/L, last EO turn the other way (`F U2 R' B'`) | 8 | `L F2 U' L U D' L U` |
| DR on U/D (6c6e), EO kept | 9 | `U L' U' B2 D' L U D' R` |
| DR on U/D on the inverse (6c6e there), EO kept | 6 | `(L D' F2 L' D R)` |
| DR on U/D, last EO turn the other way (`F U2 R' B'`) | 8 | `D' R' L2 B2 D L D R` |

</details>

**4c8e, example 2.** Scramble `D' L2 U' F2 L2 R2 U2 L2 U' F2 U2 L2 R2 U' F' L' B2 L2 U' B2 D' F' U L2`, EO `B' U' D L` on R/L (4 turns). After it, the case is 4c8e for DR on F/B and 6c6e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (4c8e), EO kept | 8 | `F U' L2 D B D2 F U` |
| DR on F/B on the inverse (4c8e there), EO kept | 8 | `(R2 D F U2 B U2 B2 U)` |
| DR on F/B, last EO turn the other way (`B' U' D L'`) | 9 | `F' U2 D B2 U2 R2 L2 F' D` |
| DR on U/D (6c6e), EO kept | 9 | `U F U2 D F U' B' U' F` |
| DR on U/D on the inverse (6c6e there), EO kept | 8 | `(U R2 U' B U D R2 F)` |
| DR on U/D, last EO turn the other way (`B' U' D L'`) | 8 | `U2 B U' F D' R2 U F` |

</details>

**4c8e, example 3.** Scramble `D L2 F2 U' R2 U F2 R2 U R2 U' R2 U L D2 B' D' U' F' L' B R' D2`, EO `R L D L` on R/L (4 turns). After it, the case is 4c8e for DR on U/D and 2c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (4c8e), EO kept | 9 | `D' B' R2 F2 U' D2 B D2 F` |
| DR on U/D on the inverse (4c8e there), EO kept | 9 | `(D' F U D2 B2 F' U2 D B)` |
| DR on U/D, last EO turn the other way (`R L D L'`) | 9 | `D' B' R2 F U' L2 B2 U2 B` |
| DR on F/B (2c6e), EO kept | 8 | `D F B2 D' R2 U' B D` |
| DR on F/B on the inverse (2c6e there), EO kept | 7 | `(F U F B2 D2 B D)` |
| DR on F/B, last EO turn the other way (`R L D L'`) | 8 | `B U R2 B D' B' L2 D` |

</details>

### 3c6e

**3c6e, example 1.** Scramble `U2 L2 B2 D' B2 U' B2 U R2 U' B2 R2 B' U B' F' L B R2 F L U`, EO `U' F' B' L` on R/L (4 turns). After it, the case is 3c6e for DR on U/D and 3c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (3c6e), EO kept | 9 | `U F D L2 B R2 B2 D' B` |
| DR on U/D on the inverse (3c6e there), EO kept | 7 | `(L2 D B2 F' U' D2 B)` |
| DR on U/D, last EO turn the other way (`U' F' B' L'`) | 9 | `U F' U F2 U2 B' L2 D' F` |
| DR on F/B (3c6e), EO kept | 7 | `U2 F U2 D F2 B U` |
| DR on F/B on the inverse (3c6e there), EO kept | 8 | `(B2 U' D' B U F' B U)` |
| DR on F/B, last EO turn the other way (`U' F' B' L'`) | 8 | `U2 F U2 L2 D F2 B U` |

</details>

**3c6e, example 2.** Scramble `B2 F2 L2 F2 D L2 D' F2 L2 D' B2 U B' D' F L R' U' L B2 F'`, EO `L B U D` on U/D (4 turns). After it, the case is 3c6e for DR on R/L and 4c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (3c6e), EO kept | 7 | `U2 L' R' F' L R2 B` |
| DR on R/L on the inverse (3c6e there), EO kept | 5 | `(L2 B' L2 R' F)` |
| DR on R/L, last EO turn the other way (`L B U D'`) | 8 | `L' R' B' L2 B2 F2 L F` |
| DR on F/B (4c6e), EO kept | 8 | `L B R L2 B U2 F' L` |
| DR on F/B on the inverse (4c6e there), EO kept | 8 | `(F' B2 U2 R F2 L' B' L)` |
| DR on F/B, last EO turn the other way (`L B U D'`) | 8 | `F2 R2 U2 R F2 R2 B L` |

</details>

**3c6e, example 3.** Scramble `B2 L2 U' B2 U2 B2 L2 U' L2 F2 U2 F2 U L2 U R' F' R D L R2 F' R2 U R'`, EO `U R L D` on U/D (4 turns). After it, the case is 3c6e for DR on R/L and 4c2e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (3c6e), EO kept | 8 | `D2 B2 U2 R2 F L R2 B` |
| DR on R/L on the inverse (3c6e there), EO kept | 8 | `(R' D2 F R' B2 D2 L' B)` |
| DR on R/L, last EO turn the other way (`U R L D'`) | 7 | `B2 U2 R2 F L R2 B` |
| DR on F/B (4c2e), EO kept | 8 | `F2 B' R' L2 B' R2 F' R` |
| DR on F/B on the inverse (4c2e there), EO kept | 7 | `(B2 R D2 R' F' B2 L)` |
| DR on F/B, last EO turn the other way (`U R L D'`) | 8 | `R2 B' R F R' L' F L` |

</details>

### 7c8e

**7c8e, example 1.** Scramble `R2 D2 B2 F2 D' R2 D' R2 B2 L2 R2 U' B2 U' L' D' R' B' R' U' R B2 U'`, EO `U L' F2 B` on F/B (4 turns). After it, the case is 7c8e for DR on U/D and 6c6e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (7c8e), EO kept | 9 | `U R2 F2 B2 R D' R2 U L` |
| DR on U/D on the inverse (7c8e there), EO kept | 8 | `(U R D' F2 B2 L2 U R)` |
| DR on U/D, last EO turn the other way (`U L' F2 B'`) | 8 | `R2 D L D' R L D' L` |
| DR on R/L (6c6e), EO kept | 7 | `R D' L' U L2 R2 U` |
| DR on R/L on the inverse (6c6e there), EO kept | 8 | `(D2 L U' F2 L' U L' U)` |
| DR on R/L, last EO turn the other way (`U L' F2 B'`) | 8 | `R B2 U' D R F2 B2 D` |

</details>

**7c8e, example 2.** Scramble `U' L2 U' L2 U2 F2 U R2 B2 F2 D' L2 F2 U R' F L' B2 R2 D L B F U'`, EO `B' R2 U F` on F/B (4 turns). After it, the case is 7c8e for DR on R/L and 5c6e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (7c8e), EO kept | 7 | `L2 U2 L U2 D R U` |
| DR on R/L on the inverse (7c8e there), EO kept | 6 | `(L D2 F2 D R' U)` |
| DR on R/L, last EO turn the other way (`B' R2 U F'`) | 7 | `L B2 U2 B2 D' L U` |
| DR on U/D (5c6e), EO kept | 7 | `D2 R U R2 D R L` |
| DR on U/D on the inverse (5c6e there), EO kept | 8 | `(U F2 L' U2 R F2 D L)` |
| DR on U/D, last EO turn the other way (`B' R2 U F'`) | 7 | `D2 R U R2 D R L` |

</details>

**7c8e, example 3.** Scramble `L2 U2 L2 R2 D F2 R2 D R2 D' L2 B2 R' B' R2 D R F' D L' U R'`, EO `L' F B' D` on U/D (4 turns). After it, the case is 7c8e for DR on F/B and 8c2e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (7c8e), EO kept | 7 | `U2 R L B R' U2 R` |
| DR on F/B on the inverse (7c8e there), EO kept | 8 | `(B D2 L' B' R L' F L)` |
| DR on F/B, last EO turn the other way (`L' F B' D'`) | 8 | `F' L2 F U2 R L2 F L` |
| DR on R/L (8c2e), EO kept | 9 | `B L' R B L' R2 U2 D2 F` |
| DR on R/L on the inverse (8c2e there), EO kept | 9 | `(B' L F' R2 B U2 L2 R B)` |
| DR on R/L, last EO turn the other way (`L' F B' D'`) | 10 | `L B L' R B' R B2 L' U2 F` |

</details>

### 6c2e

**6c2e, example 1.** Scramble `B2 L2 F2 L2 D' L2 D R2 D' F2 U2 F2 R' B' R' B' D2 R B2 F2 D2`, EO `U B2 U L` on R/L (4 turns). After it, the case is 6c2e for DR on U/D and 5c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (6c2e), EO kept | 8 | `U2 B' D2 B' U B' U B` |
| DR on U/D on the inverse (6c2e there), EO kept | 9 | `(U D F' R2 U B' U D2 B)` |
| DR on U/D, last EO turn the other way (`U B2 U L'`) | 9 | `U B' L2 U' R2 U' F2 U' F` |
| DR on F/B (5c6e), EO kept | 7 | `D' F R2 L2 U2 F D` |
| DR on F/B on the inverse (5c6e there), EO kept | 8 | `(B U D B' R2 F B2 D)` |
| DR on F/B, last EO turn the other way (`U B2 U L'`) | 8 | `F2 B2 R2 U B D2 B D` |

</details>

**6c2e, example 2.** Scramble `B2 L2 U L2 D2 U' L2 B2 D' B2 U R2 B' U' F' L2 U2 R B F2 U2 R U'`, EO `U F R' D` on U/D (4 turns). After it, the case is 6c2e for DR on F/B and 6c6e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (6c2e), EO kept | 8 | `L' F R2 B L' F' B L` |
| DR on F/B on the inverse (6c2e there), EO kept | 8 | `(R' D2 F L' F' R' F' L)` |
| DR on F/B, last EO turn the other way (`U F R' D'`) | 8 | `F' L' F R2 B L' F' L` |
| DR on R/L (6c6e), EO kept | 8 | `R F L' B U2 L R2 F` |
| DR on R/L on the inverse (6c6e there), EO kept | 7 | `(L2 U2 B' R B' D2 B)` |
| DR on R/L, last EO turn the other way (`U F R' D'`) | 9 | `L U2 F' R' B R' F2 L B` |

</details>

**6c2e, example 3.** Scramble `F2 U' L2 F2 U' B2 D' B2 L2 D' L2 B2 U' L' B2 R' F' R D' F' L B' F2`, EO `R2 D2 L U'` on U/D (4 turns). After it, the case is 6c2e for DR on F/B and 6c6e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (6c2e), EO kept | 9 | `F L F' L D2 L' B' D2 L` |
| DR on F/B on the inverse (6c2e there), EO kept | 9 | `(F2 B2 R F B R F' B2 R)` |
| DR on F/B, last EO turn the other way (`R2 D2 L U`) | 8 | `L F B2 L' F R' D2 R` |
| DR on R/L (6c6e), EO kept | 8 | `L' R' F2 L' B F' R' B` |
| DR on R/L on the inverse (6c6e there), EO kept | 8 | `(L F L U2 L F' L B)` |
| DR on R/L, last EO turn the other way (`R2 D2 L U`) | 8 | `L2 U2 L F L R U2 B` |

</details>

### 8c6e

**8c6e, example 1.** Scramble `B2 D' F2 L2 B2 F2 D B2 L2 D L2 U F2 D' L' F' R U F L U2 R'`, EO `U2 R F U` on U/D (4 turns). After it, the case is 8c6e for DR on F/B and 7c2e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (8c6e), EO kept | 8 | `F R F L2 D2 R2 F R` |
| DR on F/B on the inverse (8c6e there), EO kept | 9 | `(B2 R' B R2 B' R L B R)` |
| DR on F/B, last EO turn the other way (`U2 R F U'`) | 8 | `R2 B L' D2 R' U2 B' L` |
| DR on R/L (7c2e), EO kept | 9 | `L2 R F D2 L2 U2 L' R2 B` |
| DR on R/L on the inverse (7c2e there), EO kept | 9 | `(L B' R B L R U2 L' F)` |
| DR on R/L, last EO turn the other way (`U2 R F U'`) | 10 | `L R F U2 R U2 R' B2 L F` |

</details>

**8c6e, example 2.** Scramble `U2 F2 R2 U' L2 U' B2 R2 B2 L2 U' L2 F2 D F' D' B2 L' B D2 L U' B2 D'`, EO `U F B2 L'` on R/L (4 turns). After it, the case is 8c6e for DR on U/D and 6c4e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (8c6e), EO kept | 8 | `U2 F' U B L2 B2 D F` |
| DR on U/D on the inverse (8c6e there), EO kept | 8 | `(D' B U R2 L2 B' U F)` |
| DR on U/D, last EO turn the other way (`U F B2 L`) | 8 | `D2 B L2 U R2 U L2 F` |
| DR on F/B (6c4e), EO kept | 7 | `B U F' B2 U' F2 U` |
| DR on F/B on the inverse (6c4e there), EO kept | 8 | `(B U L2 U' R2 D2 B' U)` |
| DR on F/B, last EO turn the other way (`U F B2 L`) | 8 | `B D' F R2 D' F' B2 D` |

</details>

**8c6e, example 3.** Scramble `D L2 U F2 U2 L2 B2 U R2 F2 R2 F2 U L' F L' R F L' U' R' B F`, EO `F2 U2 R2 F` on F/B (4 turns). After it, the case is 8c6e for DR on U/D and 5c8e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (8c6e), EO kept | 9 | `L D R' U D2 F2 R' B2 L` |
| DR on U/D on the inverse (8c6e there), EO kept | 8 | `(R' F2 L U2 L U' D' L)` |
| DR on U/D, last EO turn the other way (`F2 U2 R2 F'`) | 9 | `U' L U R U2 F2 B2 U L` |
| DR on R/L (5c8e), EO kept | 7 | `D' L2 U' L R' B2 U` |
| DR on R/L on the inverse (5c8e there), EO kept | 9 | `(U D2 L2 D R B2 U2 L2 D)` |
| DR on R/L, last EO turn the other way (`F2 U2 R2 F'`) | 8 | `F2 D' L2 U' L R' B2 U` |

</details>

### 3c4e

**3c4e, example 1.** Scramble `U R2 D' L2 B2 D' F2 D' L2 R2 D' B2 U2 F' R F D' B U2 B2 F L2`, EO `D F D' L` on R/L (4 turns). After it, the case is 3c4e for DR on F/B and 4c6e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (3c4e), EO kept | 8 | `F2 D2 F U' R2 L2 F' D` |
| DR on F/B on the inverse (3c4e there), EO kept | 5 | `(U F U' B U)` |
| DR on F/B, last EO turn the other way (`D F D' L'`) | 8 | `F L2 U' R2 F2 U B U` |
| DR on U/D (4c6e), EO kept | 8 | `U' D2 B U2 B2 L2 U' B` |
| DR on U/D on the inverse (4c6e there), EO kept | 8 | `(D B' U2 D F U' L2 F)` |
| DR on U/D, last EO turn the other way (`D F D' L'`) | 7 | `B' U' L2 F U' L2 F` |

</details>

**3c4e, example 2.** Scramble `U' R2 F2 R2 F2 U R2 U2 L2 D' R2 B2 F2 B' L D2 L F' D2 L' D' L'`, EO `U L' U' L` on R/L (4 turns). After it, the case is 3c4e for DR on U/D and 5c8e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (3c4e), EO kept | 7 | `B D' B2 U2 B' U' B` |
| DR on U/D on the inverse (3c4e there), EO kept | 8 | `(U' B2 U2 B' D' R2 U2 F)` |
| DR on U/D, last EO turn the other way (`U L' U' L'`) | 8 | `U2 B2 D F U B D2 B` |
| DR on F/B (5c8e), EO kept | 8 | `L2 D B D R2 D' F U` |
| DR on F/B on the inverse (5c8e there), EO kept | 9 | `(F B U F L2 B U' B' D)` |
| DR on F/B, last EO turn the other way (`U L' U' L'`) | 7 | `D B D R2 D' F U` |

</details>

**3c4e, example 3.** Scramble `L2 B2 L2 F2 U R2 D' F2 U2 F2 L2 U F2 D B' U L2 R2 B D R F D2`, EO `D2 F' R'` on R/L (3 turns). After it, the case is 3c4e for DR on F/B and 7c6e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (3c4e), EO kept | 6 | `R2 U F2 U B D` |
| DR on F/B on the inverse (3c4e there), EO kept | 7 | `(F' U' D2 F R2 L2 D)` |
| DR on F/B, last EO turn the other way (`D2 F' R`) | 5 | `U F2 U B D` |
| DR on U/D (7c6e), EO kept | 6 | `D' B' R2 L2 U' B` |
| DR on U/D on the inverse (7c6e there), EO kept | 8 | `(B D F' U' B2 R2 U B)` |
| DR on U/D, last EO turn the other way (`D2 F' R`) | 7 | `R2 D' B' R2 L2 U' B` |

</details>

### 2c4e

**2c4e, example 1.** Scramble `U' B2 D' L2 B2 F2 U R2 U2 L2 F2 D L2 U' L2 F' R B' L F' D R D' F D'`, EO `D L' B R` on R/L (4 turns). After it, the case is 2c4e for DR on F/B and 5c2e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (2c4e), EO kept | 7 | `D' R2 B R2 B R2 D` |
| DR on F/B on the inverse (2c4e there), EO kept | 8 | `(B U2 F2 U' F2 U' L2 U)` |
| DR on F/B, last EO turn the other way (`D L' B R'`) | 8 | `F' D F' B U2 D B D` |
| DR on U/D (5c2e), EO kept | 9 | `U D' B U' B F2 U' L2 F` |
| DR on U/D on the inverse (5c2e there), EO kept | 8 | `(U2 B F' D F' D R2 B)` |
| DR on U/D, last EO turn the other way (`D L' B R'`) | 8 | `U' F U B2 D' B2 D F` |

</details>

**2c4e, example 2.** Scramble `U2 B2 D' R2 U F2 R2 B2 D' R2 D F2 D2 L2 F' R' B' D F L2 B U' L U'`, EO `F' L' D R'` on R/L (4 turns). After it, the case is 2c4e for DR on F/B and 4c6e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (2c4e), EO kept | 8 | `U B U' F' L2 U' F2 U` |
| DR on F/B on the inverse (2c4e there), EO kept | 8 | `(F D' R2 D F' U' F2 D)` |
| DR on F/B, last EO turn the other way (`F' L' D R`) | 7 | `U' B D F' D' B' U` |
| DR on U/D (4c6e), EO kept | 8 | `D B' F2 D' B' U' D F` |
| DR on U/D on the inverse (4c6e there), EO kept | 7 | `(U' F2 D' R2 B L2 F)` |
| DR on U/D, last EO turn the other way (`F' L' D R`) | 7 | `U2 B' U' R2 L2 D' B` |

</details>

**2c4e, example 3.** Scramble `L2 U R2 D2 F2 L2 U' L2 D B2 L2 U2 R' D' R' U2 F D L' B2 D`, EO `L' F2 B' U` on U/D (4 turns). After it, the case is 2c4e for DR on R/L and 7c4e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (2c4e), EO kept | 8 | `R' B2 F' R2 F U2 R F` |
| DR on R/L on the inverse (2c4e there), EO kept | 7 | `(F D2 L F2 R' U2 F)` |
| DR on R/L, last EO turn the other way (`L' F2 B' U'`) | 8 | `L' B2 F' U2 F D2 R B` |
| DR on F/B (7c4e), EO kept | 7 | `R B' D2 B2 D2 U2 R` |
| DR on F/B on the inverse (7c4e there), EO kept | 8 | `(B L' U2 L' F B D2 R)` |
| DR on F/B, last EO turn the other way (`L' F2 B' U'`) | 7 | `R B' D2 B2 D2 U2 R` |

</details>

### 4c2e

**4c2e, example 1.** Scramble `D2 F2 D R2 D' B2 D R2 D2 B2 U' B2 U B' R F2 R' B2 U2 B D`, EO `U L D L` on R/L (4 turns). After it, the case is 4c2e for DR on U/D and 7c4e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (4c2e), EO kept | 7 | `D B' U2 D2 B' R2 F` |
| DR on U/D on the inverse (4c2e there), EO kept | 7 | `(U F D B' F' D B)` |
| DR on U/D, last EO turn the other way (`U L D L'`) | 7 | `D' B' D2 B U D2 B` |
| DR on F/B (7c4e), EO kept | 7 | `U R2 F' D F L2 U` |
| DR on F/B on the inverse (7c4e there), EO kept | 8 | `(F D2 R2 B' U' F' B2 U)` |
| DR on F/B, last EO turn the other way (`U L D L'`) | 8 | `L2 U R2 F' D F L2 U` |

</details>

**4c2e, example 2.** Scramble `R2 U2 L2 U R2 D' R2 U2 L2 D R2 U B2 D' R' B' L2 D' U F2 L U' L R'`, EO `D L' B' U` on U/D (4 turns). After it, the case is 4c2e for DR on R/L and 4c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (4c2e), EO kept | 8 | `L2 U2 B' F2 R' B2 L' B` |
| DR on R/L on the inverse (4c2e there), EO kept | 8 | `(L R' F R' F R U2 F)` |
| DR on R/L, last EO turn the other way (`D L' B' U'`) | 8 | `R F' L F' R2 B L B` |
| DR on F/B (4c6e), EO kept | 7 | `L2 D2 L F2 R2 F' R` |
| DR on F/B on the inverse (4c6e there), EO kept | 7 | `(F2 B2 R' F L B' L)` |
| DR on F/B, last EO turn the other way (`D L' B' U'`) | 7 | `R2 U2 L B2 L2 F R` |

</details>

**4c2e, example 3.** Scramble `D' L2 U' R2 U' B2 R2 D2 L2 U B2 L2 U2 F2 R' D' U2 B2 F D' U F D2`, EO `U' D2 F D` on U/D (4 turns). After it, the case is 4c2e for DR on R/L and 4c4e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (4c2e), EO kept | 8 | `L' F U2 F' U2 F2 L F` |
| DR on R/L on the inverse (4c2e there), EO kept | 6 | `(L' F D2 R' D2 F)` |
| DR on R/L, last EO turn the other way (`U' D2 F D'`) | 8 | `L F2 R2 B D2 R' D2 B` |
| DR on F/B (4c4e), EO kept | 7 | `U2 F' D2 R D2 F2 L` |
| DR on F/B on the inverse (4c4e there), EO kept | 8 | `(U2 F R2 D2 B2 D2 U2 R)` |
| DR on F/B, last EO turn the other way (`U' D2 F D'`) | 7 | `R' U2 F2 R' D2 F L` |

</details>

### 3c2e

**3c2e, example 1.** Scramble `B2 D2 R2 B2 F2 D B2 D2 U L2 B2 F2 R' B' R' D' L U B' F'`, EO `F' R B U` on U/D (4 turns). After it, the case is 3c2e for DR on R/L and 6c4e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (3c2e), EO kept | 7 | `L2 R F2 R2 F R F` |
| DR on R/L on the inverse (3c2e there), EO kept | 5 | `(B2 L2 B' R' B)` |
| DR on R/L, last EO turn the other way (`F' R B U'`) | 7 | `L B2 R' B2 F' R F` |
| DR on F/B (6c4e), EO kept | 8 | `R2 U2 L D2 R2 U2 B' L` |
| DR on F/B on the inverse (6c4e there), EO kept | 8 | `(R F2 R' U2 F L' F L)` |
| DR on F/B, last EO turn the other way (`F' R B U'`) | 7 | `F2 R' U2 R' L2 B L` |

</details>

**3c2e, example 2.** Scramble `L2 U F2 L2 U' L2 R2 D L2 U' L2 U F2 R2 U' F' R B2 U B D' U' F D U'`, EO `R' B R' F` on F/B (4 turns). After it, the case is 3c2e for DR on U/D and 5c6e for DR on R/L.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (3c2e), EO kept | 7 | `F2 U R2 U L' D' L` |
| DR on U/D on the inverse (3c2e there), EO kept | 7 | `(U F2 U2 R2 L' U L)` |
| DR on U/D, last EO turn the other way (`R' B R' F'`) | 6 | `U R2 U L' D' L` |
| DR on R/L (5c6e), EO kept | 7 | `L2 B2 R D R B2 U` |
| DR on R/L on the inverse (5c6e there), EO kept | 8 | `(L D L' U B2 L2 R' D)` |
| DR on R/L, last EO turn the other way (`R' B R' F'`) | 7 | `L2 B2 R' D R' B2 U` |

</details>

**3c2e, example 3.** Scramble `R2 U R2 B2 U' B2 D F2 R2 U B2 U' B2 R' D' R2 U B2`, EO `B2 R2 D R` on R/L (4 turns). After it, the case is 3c2e for DR on F/B and 2c0e for DR on U/D.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on F/B (3c2e), EO kept | 7 | `R2 B L2 F' D' F' D` |
| DR on F/B on the inverse (3c2e there), EO kept | 6 | `(F B U' D2 F U)` |
| DR on F/B, last EO turn the other way (`B2 R2 D R'`) | 6 | `B L2 F' D' F' D` |
| DR on U/D (2c0e), EO kept | 5 | `B' U' F2 U B` |
| DR on U/D on the inverse (2c0e there), EO kept | 6 | `(U' B' U F2 U' B)` |
| DR on U/D, last EO turn the other way (`B2 R2 D R'`) | 6 | `U2 B D' F2 D B` |

</details>

### 8c8e

**8c8e, example 1.** Scramble `L2 F2 L2 B2 D' L2 F2 U' L2 F2 U' B2 L2 U2 F' R' B U F' U2 R2 F L' D'`, EO `L2 F2 B2 D` on U/D (4 turns). After it, the case is 8c8e for DR on R/L and 5c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (8c8e), EO kept | 7 | `R' F L' B L2 R' B` |
| DR on R/L on the inverse (8c8e there), EO kept | 7 | `(R B F2 L F' R' B)` |
| DR on R/L, last EO turn the other way (`L2 F2 B2 D'`) | 6 | `B F' R B2 R2 B` |
| DR on F/B (5c6e), EO kept | 7 | `B D2 L B' R U2 L` |
| DR on F/B on the inverse (5c6e there), EO kept | 8 | `(F2 U2 L' B R' U2 F' R)` |
| DR on F/B, last EO turn the other way (`L2 F2 B2 D'`) | 8 | `F L B' L F R2 B R` |

</details>

**8c8e, example 2.** Scramble `D2 U' B2 L2 D L2 D' L2 U' F2 U' L2 R2 F' U' B R B F2 R F' U R'`, EO `U' F' B' R` on R/L (4 turns). After it, the case is 8c8e for DR on U/D and 5c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on U/D (8c8e), EO kept | 8 | `B D L2 F' L2 F2 D' F` |
| DR on U/D on the inverse (8c8e there), EO kept | 8 | `(U L2 D' B F U D' B)` |
| DR on U/D, last EO turn the other way (`U' F' B' R'`) | 8 | `B D L2 F' L2 F2 D' F` |
| DR on F/B (5c6e), EO kept | 8 | `D2 F' R2 B2 D B L2 U` |
| DR on F/B on the inverse (5c6e there), EO kept | 9 | `(F R2 U F2 L2 D R2 F' U)` |
| DR on F/B, last EO turn the other way (`U' F' B' R'`) | 8 | `U2 D' F D2 B' U F2 D` |

</details>

**8c8e, example 3.** Scramble `L2 U' B2 D B2 U' F2 U' B2 L2 U2 B2 L2 U2 R' F' L' B' F L' F' L2`, EO `U L' B2 U'` on U/D (4 turns). After it, the case is 8c8e for DR on R/L and 4c6e for DR on F/B.

<details><summary>Turns to DR each way</summary>

| After the EO | Turns to DR | One way |
|---|---:|---|
| DR on R/L (8c8e), EO kept | 8 | `L2 B' F L' R B L2 B` |
| DR on R/L on the inverse (8c8e there), EO kept | 7 | `(L U2 B F L R F)` |
| DR on R/L, last EO turn the other way (`U L' B2 U`) | 7 | `B F' L R B' D2 B` |
| DR on F/B (4c6e), EO kept | 10 | `F B' L' U2 B D2 L' B' D2 R` |
| DR on F/B on the inverse (4c6e there), EO kept | 7 | `(D2 B L U2 R' B' L)` |
| DR on F/B, last EO turn the other way (`U L' B2 U`) | 9 | `B D2 R F2 R' U2 L F' R` |

</details>
