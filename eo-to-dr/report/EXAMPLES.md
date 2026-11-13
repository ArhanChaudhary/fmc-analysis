# Worked examples: EO to DR, and scramble to DR

Examples to play along with [the write-up](index.html). Try a scramble, then open the answers.

**Part 1** is 150 uniformly random scrambles, the first 150 of the study's 50,000 (drawn by the study itself, not by nissy's `scramble`; see the write-up, appendix B). For each one: the bad edges on each axis, how many EOs of at most 4 and at most 5 turns it has, and, folded away, its shortest DR (normal, inverse, best of six, NISS) and the best DR through an EO of at most 4 and of at most 5 turns. **Part 2** is 60 EO-solved states by case: a scramble and an EO, then how far DR is on each of the two DR axes, on the inverse, and with the EO's last turn the other way.

How to read it:

- Turns are face turns (HTM). *Normal* means turns after the scramble, *inverse* turns after the inverse scramble, written in brackets as usual for NISS: `R U (F D)` is `R U` on the normal side and `F D` on the inverse. A *NISS EO* has turns on both sides.
- A *route through an EO* is the EO, then turns that keep it (no quarter turns of the EO's axis) to DR on one of the two other axes, on the same side.
- "EOs of at most 4 turns" counts every move sequence that solves EO for the first time at its last turn, both directions of the last turn counted, as nissy's `-a` lists them. nissy's default listing keeps one of the EOs that differ only in the directions of their last turns: on these 150 scrambles it lists 47% of the normal EOs of at most 5, 47% of the inverse ones and 38%, about two fifths, of the NISS column.
- A case like 4c4e names the bad corners and the edges out of place for that DR axis (slice edges outside the slice, and as many other edges inside it), the counts of Cale's "DR setup stats" sheet (which writes the edges first, 4e4c).

Every answer is exact: a shortest DR is the fewest turns there are (from exact distance tables), and a "best DR through an EO" is the best over every EO of that length or shorter. "For example" gives one of the shortest; there are usually several. These are computer only, the answer key: try the scramble the way you would in an attempt, then compare.

**Replay check.** Every move sequence on this page was replayed on the sticker model before the page was written: 2,242 checks (each EO is an EO on its axis, each DR is a DR on its axis with the stated number of turns, DR turns after an EO keep it, each case and bad-edge count is read off the stickers), 0 mismatches.

In these 150: best of six 8.75 on average, NISS 8.47 (the 50,000 give 8.76 and 8.46).

## Part 1. 150 scrambles

### Scramble 1

```
U2 R2 D L2 R2 D' R2 U' L2 D R2 U F2 R' D' F2 L' D R D' B' R2 D'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 10, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 26 | 24 | 4 |
| At most 5 | 180 | 172 | 184 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
R' D B L' R U' R F2 D        // normal, DR on R/L
(L U' B U2 L' F2 R B2 U' L)  // inverse, DR on U/D
R' D B L' R U' R F2 D        // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
D' L2 U2 F'           // normal EO on F/B
R' U D' L D           // then DR on R/L
(L U' B)              // inverse EO on F/B
(U2 L' F2 R B2 U' L)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
D' L2 U2 F'           // normal EO on F/B
R' U D' L D           // then DR on R/L
(L U' B)              // inverse EO on F/B
(U2 L' F2 R B2 U' L)  // then DR on U/D
```


</details>

### Scramble 2

```
B2 L2 R2 U R2 D2 B2 L2 R2 U F2 U R2 D2 B' R' U B' L' U R2 B D2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 4 | 0 |
| At most 5 | 58 | 100 | 92 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 9 | 11 |
| Inverse | 8 | 9 | 10 | 8 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
F' D R' B2 U B' L2 D    // normal, DR on R/L
(L U' B2 D R' U' B' L)  // inverse, DR on F/B
F' D R' B2 U B' L2 D    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; through an inverse EO: 11; with NISS EOs too: 11.

```
(U D L' U')         // inverse EO on U/D
(L2 F R B L2 F' R)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
U2 F' R D' L      // normal EO on R/L
F2 D' B2 U B      // then DR on U/D
(L2 D' B2 R' U')  // inverse EO on U/D
(L' U2 R2 F L)    // then DR on F/B
```


</details>

### Scramble 3

```
L2 D2 U' F2 L2 U' L2 B2 U' R2 B2 L2 R' D L F' D F2 D' F2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 4, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 64 | 48 | 12 |
| At most 5 | 650 | 380 | 276 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 9 | 8 | 10 |
| Inverse | 8 | 9 | 8 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
F2 D F2 D' F L' D' R    // normal, DR on U/D
(R' D R2 L' D B2 U' B)  // inverse, DR on U/D
F2 D F2 D' F L' D' R    // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 8; with NISS EOs too: 8.

```
F L D' R       // normal EO on R/L
L2 D' F' D' F  // then DR on U/D
(R' D R2 L')   // inverse EO on R/L
(D B2 U' B)    // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 8; through an inverse EO: 8; with NISS EOs too: 8.

```
F2 D F2 D' F  // normal EO on F/B
L' D' R       // then DR on U/D
(R' D R2 L')  // inverse EO on R/L
(D B2 U' B)   // then DR on U/D
```


</details>

### Scramble 4

```
U R2 F2 R2 F2 U B2 U2 R2 D' F2 L2 U' R' U' F' U' R2 B' F2 D' R  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 12 | 24 | 36 |
| At most 5 | 190 | 284 | 316 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 8 | 8 | 9 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
B R D B' D2 L' F2 U2 F  // normal, DR on U/D
(L' F2 L F' R B2 U' B)  // inverse, DR on R/L
(L' F2 L F' R B2 U' B)  // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 9.

```
R' F' L' D'       // normal EO on U/D
R2 B' L R F2 R B  // then DR on R/L
(U R2 F2 D)       // inverse EO on U/D
(B' D2 F U2 L B)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
R D2 R2 B' L'  // normal EO on R/L
U2 D B' R2 B   // then DR on U/D
(U R' F R' D)  // inverse EO on U/D
(R2 B D2 B)    // then DR on R/L
```


</details>

### Scramble 5

```
D2 R2 F2 L2 U' L2 R2 U' B2 D B2 R2 U2 B' L2 F' R U2 B L2 F L' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 12 | 0 | 12 |
| At most 5 | 190 | 88 | 228 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 10 | 10 |
| Inverse | 8 | 10 | 8 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
F2 U D L' F' R' B D     // normal, DR on R/L
(L' B' U' R F R' U2 L)  // inverse, DR on U/D
F2 U D L' F' R' B D     // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; no inverse EO; with NISS EOs too: 11.

```
R F R L             // normal EO on R/L
F' D F' L2 U' D2 F  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 8; with NISS EOs too: 8.

```
R F D2 R' L     // normal EO on R/L
U F2 L2 F D     // then DR on F/B
(L' B' U' R F)  // inverse EO on F/B
(R' U2 L)       // then DR on U/D
```


</details>

### Scramble 6

```
B2 U L2 F2 R2 D2 R2 U F2 U2 B2 U R2 L' B' F2 R' D F2 U' F' D2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 2 | 32 | 24 |
| At most 5 | 66 | 244 | 284 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 10 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D2 F U F2 D' R F2 B L   // normal, DR on U/D
(F D F2 D L F D2 R D)   // inverse, DR on F/B
D2 F U F2 D' R F2 B L   // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 9.

```
L F' B D           // normal EO on U/D
L R B L2 D2 R B    // then DR on R/L
(R2 B' R' D)       // inverse EO on U/D
(F B2 L' B' U2 L)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
L' B L F' D'       // normal EO on U/D
L F' U2 R' F       // then DR on R/L
(R2 B' R' D)       // inverse EO on U/D
(F B2 L' B' U2 L)  // then DR on F/B
```


</details>

### Scramble 7

```
B2 F2 U2 B2 L2 U' B2 U' B2 U L2 U' B2 F' D2 U L D2 B' U' L U'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 18 | 14 | 24 |
| At most 5 | 256 | 238 | 248 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 10 |
| Inverse | 9 | 10 | 9 | 9 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
U L' U B D2 L' U' D2 F      // normal, DR on U/D
(F B2 U' F2 D' R2 U2 F' L)  // inverse, DR on F/B
F U' R' B2 D' R B (U)       // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 9.

```
U D2 F' L'             // normal EO on R/L
F' R2 D' B U L2 D      // then DR on F/B
(D' L' F U)            // inverse EO on U/D
(B2 L' B' R2 F' D2 L)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
U F U2 B2 R      // normal EO on R/L
D' B F' U F      // then DR on U/D
(F B2 U' F2 D')  // inverse EO on U/D
(R2 U2 F' L)     // then DR on F/B
```


</details>

### Scramble 8

```
B2 U2 L2 R2 D B2 D F2 U2 L2 U' R2 U' R2 U' B' D2 R' B2 F' R2 U F2 L R'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 2 | 0 |
| At most 5 | 54 | 60 | 116 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 11 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
R L' F2 U' R2 F B2 R D2 B   // normal, DR on U/D
(F2 R' D F' B2 U' R' U2 L)  // inverse, DR on F/B
(U R2 D' L U2 B R' L2 F)    // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 11.

```
R' F U2 L'            // normal EO on R/L
F D2 F' B' U F2 D     // then DR on F/B
(U R2 F D)            // inverse EO on U/D
(F' L' B' R' D2 B R)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 9.

```
R2 F R U2 L'          // normal EO on R/L
D R2 F U' D F         // then DR on U/D
(U R2 F D)            // inverse EO on U/D
(F' L' B' R' D2 B R)  // then DR on F/B
```


</details>

### Scramble 9

```
F2 L2 R2 U2 L2 U' F2 D' B2 R2 D' F2 U R U L2 B L F' D F R' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 16 | 40 |
| At most 5 | 52 | 116 | 236 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D L' D2 B' R2 L2 U' R D      // normal, DR on F/B
(L' D F' U R' F R2 B2 L' B)  // inverse, DR on R/L
D L' D2 B' R2 L2 U' R D      // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: no normal EO; through an inverse EO: 10; with NISS EOs too: 10.

```
(L' D F' U)        // inverse EO on U/D
(R' F R2 B2 L' B)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
F2 D L B' R'       // normal EO on R/L
F R2 B' L2 U F     // then DR on U/D
(L' D F' U)        // inverse EO on U/D
(R' F R2 B2 L' B)  // then DR on R/L
```


</details>

### Scramble 10

```
D2 L2 U2 L2 U' L2 D F2 U' B2 D B2 U L2 U2 B' D' F R' B' D B2 F2 L2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 14 | 14 | 32 |
| At most 5 | 230 | 150 | 316 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 8 | 9 | 10 | 8 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
F2 L F U2 L' U R2 F D U  // normal, DR on F/B
(L2 B D' B' D F U R)     // inverse, DR on F/B
(L2 B D' B' D F U R)     // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 9; with NISS EOs too: 8.

```
L F' U2 L'         // normal EO on R/L
U B' U D2 B U D    // then DR on F/B
(F U R)            // inverse EO on R/L
(F' U2 D' B R2 D)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 8.

```
F2 L F U2 L'       // normal EO on R/L
U R2 F U D         // then DR on F/B
(F U R)            // inverse EO on R/L
(F' U2 D' B R2 D)  // then DR on F/B
```


</details>

### Scramble 11

```
U' B2 U' B2 U L2 D2 B2 R2 F2 R2 D F2 R2 U2 R' U L B F R2 U' B R D2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 10 | 28 | 4 |
| At most 5 | 144 | 180 | 228 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F U' L2 F B' U' D R D    // normal, DR on R/L
(U2 R D U L' B D' U' L)  // inverse, DR on F/B
F U' L2 F B' U' D R D    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
U' B2 R D            // normal EO on U/D
F' L' F U2 D2 R F    // then DR on R/L
(R U' L')            // inverse EO on R/L
(B2 U' B L2 U D2 B)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
F U' R2 F' B         // normal EO on F/B
U' D L U             // then DR on R/L
(R U' L')            // inverse EO on R/L
(B2 U' B L2 U D2 B)  // then DR on U/D
```


</details>

### Scramble 12

```
R2 F2 L2 B2 D F2 L2 D2 L2 U F2 D B2 U' L' F' U B L D R B' L2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 10.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 8 |
| At most 5 | 0 | 26 | 180 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 11 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 10 | | | |
| NISS | 9 | | | |

For example:

```
F D2 L' D' F2 U' L' D L2 U    // normal, DR on F/B
(D' B' L' U' F2 R' F U2 D B)  // inverse, DR on U/D
F B R' D' L' B (D F2 R)       // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 10.

**EOs of at most 5 turns**, best DR: no normal EO; through an inverse EO: 11; with NISS EOs too: 10.

```
(L D F' B L')      // inverse EO on R/L
(B2 U2 B' D2 B D)  // then DR on F/B
```


</details>

### Scramble 13

```
D F2 U' L2 D' F2 U' R2 U' B2 U B2 R2 U L' D' U' F R D2 R D' B D  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 4 | 8 |
| At most 5 | 62 | 96 | 228 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
R' L D' B2 U L' D' B' R    // normal, DR on F/B
(R2 U' B R' U' B2 L D' F)  // inverse, DR on R/L
L (D' B' U2 D R' B L)      // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
B' D R2 F'            // normal EO on F/B
D2 L U L2 R U         // then DR on R/L
(F B R F)             // inverse EO on F/B
(L B2 R' D' R' F2 L)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
L U' B2 L' D'  // normal EO on U/D
R' D2 L2 F R   // then DR on F/B
(F R' B R' F)  // inverse EO on F/B
(L R' U B2 D)  // then DR on R/L
```


</details>

### Scramble 14

```
L2 R2 U2 F2 U L2 U F2 L2 D' F2 R2 U F' L' D2 R' B2 U B' F' L2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 10.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 0 |
| At most 5 | 28 | 28 | 112 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
R' D F B R2 D F' R' F       // normal, DR on R/L
(F R2 U' R D U B2 L2 B' L)  // inverse, DR on F/B
R' D F B R2 D F' R' F       // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; no EO at all.

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
R U' B U' D'       // normal EO on U/D
L2 B R' L' B' R    // then DR on F/B
(U' R U F' D')     // inverse EO on U/D
(U2 B' L B2 R' F)  // then DR on R/L
```


</details>

### Scramble 15

```
R2 B2 U2 B2 U' F2 D F2 U2 F2 R2 D2 U' R2 L' B D' U F2 R' B F2 L  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 8, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 10 | 6 | 12 |
| At most 5 | 174 | 152 | 180 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
R F D' R' U' R U2 F' L  // normal, DR on F/B
(R D R U B' U B2 R U)   // inverse, DR on R/L
F' R B2 D (R2 F' U B)   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
D' L' U' B        // normal EO on F/B
L D' L F2 L U     // then DR on R/L
(L2 U2 B' L)      // inverse EO on R/L
(F2 L2 D F B' U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 9; with NISS EOs too: 8.

```
R F D' R' U'  // normal EO on U/D
R U2 F' L     // then DR on F/B
(R D R U B')  // inverse EO on F/B
(U B2 R U)    // then DR on R/L
```


</details>

### Scramble 16

```
D R2 U B2 L2 U L2 B2 D2 L2 F2 U' L2 U' B' D2 F' L' R D' U' R' U2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 16 | 20 | 16 |
| At most 5 | 260 | 310 | 332 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 10 |
| Inverse | 10 | 10 | 11 | 11 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U2 R U D R' L F D2 B      // normal, DR on U/D
(U' B U2 D R F L U' F D)  // inverse, DR on R/L
U2 R U D R' L F D2 B      // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
U D R L             // normal EO on R/L
F L2 U F' L2 D      // then DR on F/B
(B' R2 D F)         // inverse EO on F/B
(R D2 L U' R2 D L)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
U D R L           // normal EO on R/L
F L2 U F' L2 D    // then DR on F/B
(U R L' U D')     // inverse EO on U/D
(L2 R D2 B U2 F)  // then DR on R/L
```


</details>

### Scramble 17

```
U2 F2 D' L2 B2 D' R2 F2 D F2 L2 B2 U2 B' U R F2 U F U2 R2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 40 | 6 | 8 |
| At most 5 | 352 | 170 | 228 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 9 | 10 | 9 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
B U' F' L U2 D' L U' L     // normal, DR on U/D
(U F' R2 D' R U' B' D2 R)  // inverse, DR on U/D
U R2 U2 F' U' F2 R' U' B   // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 11; with NISS EOs too: 9.

```
B U' F'               // normal EO on F/B
L U2 D' L U' L        // then DR on U/D
(R2 D F2 R')          // inverse EO on R/L
(F2 D' B2 D' L2 F U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 11; with NISS EOs too: 9.

```
R' U R' F B        // normal EO on F/B
D' L U' L          // then DR on U/D
(U2 R2 D F2 R')    // inverse EO on R/L
(L2 D' L2 F U' B)  // then DR on U/D
```


</details>

### Scramble 18

```
D' R2 U2 F2 L2 R2 U' L2 U' L2 U' B2 L B' U' R B U2 F' R' F' R'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 24 | 24 | 44 |
| At most 5 | 340 | 278 | 524 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U' B L' D R F R' F' D    // normal, DR on F/B
(R B U L' F2 R F2 U' B)  // inverse, DR on R/L
U L' F' U' R U2 R' U L   // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
R' U L2 F'         // normal EO on F/B
U L U2 L2 R U      // then DR on R/L
(L2 D2 B' U')      // inverse EO on U/D
(F2 B2 R D2 B' L)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
B R' L' F' R'   // normal EO on R/L
D2 R2 U' L2 B   // then DR on U/D
(L B' R U' R')  // inverse EO on R/L
(U F' U' L2 U)  // then DR on F/B
```


</details>

### Scramble 19

```
D L2 U' F2 R2 U B2 R2 D' R2 U2 L2 B' L2 D' L B' D2 F D B R' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 6 | 6 | 16 |
| At most 5 | 176 | 130 | 412 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 11 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
U R F R B' R2 B' D           // normal, DR on R/L
(F' L2 D B U2 B2 L' F2 D R)  // inverse, DR on U/D
U R F R B' R2 B' D           // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
R' L U L'          // normal EO on R/L
B2 D F2 L2 F' D    // then DR on F/B
(F' L2 D B)        // inverse EO on F/B
(U2 B2 L' F2 D R)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
R' L U L'          // normal EO on R/L
B2 D F2 L2 F' D    // then DR on F/B
(F' L2 D B)        // inverse EO on F/B
(U2 B2 L' F2 D R)  // then DR on U/D
```


</details>

### Scramble 20

```
R2 U' L2 D' F2 U2 B2 R2 B2 U F2 D F2 U2 F' L' B U F' D' B U2 R2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 28 | 4 | 8 |
| At most 5 | 236 | 152 | 200 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
R2 B U D' B' R F' B2 R      // normal, DR on U/D
(B2 R2 D2 B' U2 F' U D' B)  // inverse, DR on R/L
R2 U2 B' D F U' B' L F      // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 9.

```
U2 F2 L'             // normal EO on R/L
F B U2 D F B' U      // then DR on F/B
(B2 D' F R')         // inverse EO on R/L
(U2 D' B2 F L2 D F)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
U2 F2 L'         // normal EO on R/L
F B U2 D F B' U  // then DR on F/B
(R2 F B' U R)    // inverse EO on R/L
(F2 R2 U2 F' D)  // then DR on F/B
```


</details>

### Scramble 21

```
D B2 D2 F2 D R2 B2 F2 U R2 B2 L2 U' B' D2 L D' L D L F' L2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 2, 8, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 16 | 24 | 20 |
| At most 5 | 244 | 296 | 220 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U' B D F' U R F2 R F       // normal, DR on R/L
(B2 U F' U2 D' L F' L' B)  // inverse, DR on U/D
U' B D F' U R F2 R F       // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
U L F L'             // normal EO on R/L
U2 B D2 B U2 D B     // then DR on U/D
(R2 L' B' L')        // inverse EO on R/L
(F R2 F2 U B' D' F)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
U' B D F' U     // normal EO on U/D
R F2 R F        // then DR on R/L
(U B' R D F)    // inverse EO on F/B
(U' L F2 R' U)  // then DR on R/L
```


</details>

### Scramble 22

```
L2 D' F2 U L2 F2 D' B2 D2 R2 B2 U R2 F' U2 L B' R2 F' U' R F' U  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 8, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 0 | 20 |
| At most 5 | 100 | 84 | 228 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
R2 D L B' U' F D' R' B     // normal, DR on R/L
(L D' U' R2 F B D' F L)    // inverse, DR on F/B
L' U2 L' F' U L' B' D' F   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; no inverse EO; with NISS EOs too: 10.

```
U R B L'             // normal EO on R/L
U' D2 L2 F' U' L2 F  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
B' R U' D F'    // normal EO on F/B
L U' D R' U     // then DR on R/L
(R2 L' F U' D)  // inverse EO on U/D
(F2 U2 F2 B R)  // then DR on F/B
```


</details>

### Scramble 23

```
D' R2 F2 U L2 U R2 U' R2 U L2 U B2 D B U R2 D R' F' U' B F2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 24 | 22 | 16 |
| At most 5 | 236 | 290 | 228 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D F D F2 L' B2 U2 L2 U B   // normal, DR on U/D
(F' U' L U' D' R2 U F' L)  // inverse, DR on U/D
(F' U' L U' D' R2 U F' L)  // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
U' F B2 R          // normal EO on R/L
U F' R2 F R2 F' D  // then DR on F/B
(F D L B)          // inverse EO on F/B
(U R2 F2 U R2 U)   // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
D F D F2 L'     // normal EO on R/L
B2 U2 L2 U B    // then DR on U/D
(U R2 B' D2 L)  // inverse EO on R/L
(U2 B' D F U)   // then DR on F/B
```


</details>

### Scramble 24

```
U2 R2 U' F2 U' B2 F2 D' R2 U B2 U2 R2 D B2 U' R' B' U B' D R' D L R2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 8, 2.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 40 | 36 | 4 |
| At most 5 | 530 | 428 | 232 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 11 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 10 | | | |
| NISS | 8 | | | |

For example:

```
L' B R' U' B U2 D2 R2 B2 R   // normal, DR on U/D
(B' U' B U2 L U2 D L' B2 D)  // inverse, DR on R/L
L' B R' U' B (U2 R2 U)       // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
D' F' R2 F'         // normal EO on F/B
U2 R' B2 D' L' R U  // then DR on R/L
(U L' F' D)         // inverse EO on U/D
(B2 R' F2 R' U2 L)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
F L' F' R L'        // normal EO on R/L
U D R2 U' B         // then DR on U/D
(U L' F' D)         // inverse EO on U/D
(B2 R' F2 R' U2 L)  // then DR on F/B
```


</details>

### Scramble 25

```
F2 D B2 R2 B2 L2 U2 B2 U R2 U' B2 U F2 B' D L2 R' U R2 B F2 R' D'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 24 |
| At most 5 | 26 | 52 | 312 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
L U' F2 B' D R D2 F U2 R  // normal, DR on F/B
(F D' F B2 R' U B2 L F)   // inverse, DR on R/L
D R B D2 L (U L' D)       // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 8.

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 8.

```
U F' B2 L' D      // normal EO on U/D
F U2 F D2 L       // then DR on F/B
(D L' B R' D)     // inverse EO on U/D
(B' U2 L B U2 L)  // then DR on F/B
```


</details>

### Scramble 26

```
D2 B2 R2 D F2 U' B2 L2 B2 L2 D2 F2 D' R' B' F2 R F2 L B' D' F U  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 4 |
| At most 5 | 72 | 48 | 64 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F D' F' L U B' R B' R F  // normal, DR on R/L
(L U R F' D' R2 B' R B)  // inverse, DR on R/L
(L U R F' D' R2 B' R B)  // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
F D L F' U'    // normal EO on U/D
L2 F' U2 F' L  // then DR on F/B
(L U R F' D')  // inverse EO on U/D
(R2 B' R B)    // then DR on R/L
```


</details>

### Scramble 27

```
D' F2 D L2 F2 U' F2 L2 D L2 U' L2 B2 F' R F D R' U' F R U'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 18 | 34 | 16 |
| At most 5 | 306 | 332 | 324 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 8 | 9 | 9 | 8 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
D' F D2 B U2 R2 U L' B  // normal, DR on R/L
(F L2 B' L' U' B R2 D)  // inverse, DR on F/B
(F L2 B' L' U' B R2 D)  // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 8; with NISS EOs too: 8.

```
U D' F' R       // normal EO on R/L
B D2 B R2 L2 F  // then DR on U/D
(F L2 B' L')    // inverse EO on R/L
(U' B R2 D)     // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 8; with NISS EOs too: 8.

```
U D' F' R       // normal EO on R/L
B D2 B R2 L2 F  // then DR on U/D
(F L2 B' L')    // inverse EO on R/L
(U' B R2 D)     // then DR on F/B
```


</details>

### Scramble 28

```
U2 L2 U B2 D2 L2 D' R2 U' F2 D' B2 R2 B2 L' F D' U' F2 D2 B2 R2 F  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 16 | 4 |
| At most 5 | 206 | 226 | 132 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 10 | 9 | 8 |
| Inverse | 9 | 9 | 9 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
U2 R2 U B' L D' F' L     // normal, DR on F/B
(B' U D L' B' U R B2 R)  // inverse, DR on U/D
U2 R2 U B' L D' F' L     // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
U' D2 B' L          // normal EO on R/L
U2 F2 U' F2 D L2 F  // then DR on U/D
(D' F2 U' R)        // inverse EO on R/L
(U2 B' D' L2 U' F)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
U F' B' D B     // normal EO on F/B
R2 D F2 R D     // then DR on R/L
(B' U D L' B')  // inverse EO on F/B
(U R B2 R)      // then DR on U/D
```


</details>

### Scramble 29

```
L2 U' R2 U' R2 F2 L2 D L2 D F2 U2 L2 U R' B2 F R D F' L2 F' L' R'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 2, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 42 | 42 | 16 |
| At most 5 | 528 | 556 | 264 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 9 | 9 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
L' D B' L' D L2 B' U2 L  // normal, DR on F/B
(F' R' U F L F U2 D2 F)  // inverse, DR on U/D
R2 U D' F R2 D F R' U    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
L2 D' R D           // normal EO on U/D
L B2 R F' B' R      // then DR on F/B
(R U B' U)          // inverse EO on U/D
(F' R2 L2 U2 F' R)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 9; with NISS EOs too: 9.

```
L' D B' L' D   // normal EO on U/D
L2 B' U2 L     // then DR on F/B
(F' R' U F L)  // inverse EO on R/L
(B R2 L2 B)    // then DR on U/D
```


</details>

### Scramble 30

```
R2 D' B2 D L2 B2 F2 D B2 L2 R2 D U F' L' U2 B2 D B' R' B' F' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 12 |
| At most 5 | 20 | 52 | 216 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D' F L' U' F D2 L F' D      // normal, DR on F/B
(D2 L D B U L' F2 B' R' B)  // inverse, DR on R/L
D' F L' U' F D2 L F' D      // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 10.

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 9.

```
F L' U2 D' F     // normal EO on F/B
R2 U2 R' L U R   // then DR on U/D
(D2 L D B U)     // inverse EO on U/D
(L' B' F2 R' B)  // then DR on R/L
```


</details>

### Scramble 31

```
B2 R2 U F2 U' L2 F2 U B2 L2 U' L2 D2 R' D' R2 F' L B' R U' L U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 8 | 8 |
| At most 5 | 78 | 120 | 164 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F' B' L' R' U2 B R' U R2 D  // normal, DR on R/L
(F2 B2 R B R' U R2 D' L)    // inverse, DR on F/B
(F2 B2 R B R' U R2 D' L)    // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
U2 R F B             // normal EO on F/B
U D R F2 U' D' L     // then DR on U/D
(U' B' R D)          // inverse EO on U/D
(F R2 L2 D2 F2 B R)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
R' F U B R        // normal EO on R/L
F D F D' R2 F     // then DR on U/D
(U R D2 F2 D')    // inverse EO on U/D
(B L F' D2 B2 L)  // then DR on F/B
```


</details>

### Scramble 32

```
R2 U' F2 U' F2 R2 B2 D B2 D' R2 F2 U' L' D' R U' L' B' L  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 8, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 36 | 36 | 16 |
| At most 5 | 518 | 400 | 368 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 7 | 8 | 7 | 9 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 7 | | | |
| NISS | 7 | | | |

For example:

```
L' B L U R' D L          // normal, DR on U/D
(R U2 B2 U' L D R' U F)  // inverse, DR on R/L
L' B L U R' D L          // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 7; through an inverse EO: 11; with NISS EOs too: 7.

```
L' B                 // normal EO on F/B
L U R' D L           // then DR on U/D
(L U' R D)           // inverse EO on U/D
(R2 B2 D2 L F B2 R)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 7; through an inverse EO: 10; with NISS EOs too: 7.

```
L' B            // normal EO on F/B
L U R' D L      // then DR on U/D
(D' L U R D)    // inverse EO on U/D
(L' B2 L B' L)  // then DR on F/B
```


</details>

### Scramble 33

```
B2 U B2 F2 R2 U' R2 B2 U' L2 U F2 L2 U2 F' L' D' U' B' D' L F2 D U'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 4, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 40 | 22 | 4 |
| At most 5 | 424 | 244 | 256 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D2 F2 L' B' L2 D B L2 D   // normal, DR on F/B
(U' F U' B L R2 B D' B)   // inverse, DR on R/L
D2 F2 L' B' L2 D B L2 D   // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
D2 F2 L'           // normal EO on R/L
B' L2 D B L2 D     // then DR on F/B
(F' B D2 R)        // inverse EO on R/L
(U' F B' U' F2 U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
D2 F2 L'           // normal EO on R/L
B' L2 D B L2 D     // then DR on F/B
(F' B D2 R)        // inverse EO on R/L
(U' F B' U' F2 U)  // then DR on F/B
```


</details>

### Scramble 34

```
B2 L2 U' B2 F2 D F2 U2 B2 L2 F2 L2 U F' D B2 F2 R' B2 D' B' D L'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 24 | 8 | 20 |
| At most 5 | 170 | 108 | 244 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
L U' R' B' L2 D2 R' F U     // normal, DR on F/B
(U' B' U' R2 D F L B2 L B)  // inverse, DR on R/L
R D2 U' R' L U' B' R D      // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
D2 L' B' R'          // normal EO on R/L
F B D F U D          // then DR on F/B
(B' U' R2 D')        // inverse EO on U/D
(L B' U2 B' L' R F)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
D2 L' B' R'      // normal EO on R/L
F B D F U D      // then DR on F/B
(U' B' U' R2 D)  // inverse EO on U/D
(F L B2 L B)     // then DR on R/L
```


</details>

### Scramble 35

```
F2 U L2 U' B2 D F2 L2 R2 F2 U B2 D' F' L B U2 F2 L U' L' R2 D2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 8, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 4 |
| At most 5 | 92 | 32 | 112 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 10 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
L2 F L' F2 U' B R' D' B     // normal, DR on R/L
(U' F' B2 U R' U2 B' R2 U)  // inverse, DR on R/L
L2 F L' F2 U' B R' D' B     // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 9.

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
F' U' R' B D'    // normal EO on U/D
B D2 R2 B2 L     // then DR on F/B
(F' L' U' D B')  // inverse EO on F/B
(U F2 U2 D L)    // then DR on U/D
```


</details>

### Scramble 36

```
R2 U2 B2 L2 U' F2 U' R2 B2 R2 D R2 F' U L' U' R D2 F' R B2 D2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 8 | 8 |
| At most 5 | 144 | 104 | 240 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 11 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 10 | | | |
| NISS | 8 | | | |

For example:

```
B L' F2 R' U' F L' F2 B2 U    // normal, DR on F/B
(D R2 B L' D' L2 D2 U2 B' L)  // inverse, DR on F/B
D B' L U' D B (R2 F)          // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 8.

```
F B' R' F            // normal EO on F/B
L2 D F2 D2 R2 F2 R   // then DR on U/D
(D L F2 U)           // inverse EO on U/D
(L' B' F2 U2 L R F)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 8.

```
D L' D B U       // normal EO on U/D
L' F' L' B D2 R  // then DR on F/B
(D R2 B L' D')   // inverse EO on U/D
(L2 D2 U2 B' L)  // then DR on F/B
```


</details>

### Scramble 37

```
D F2 L2 U' F2 U L2 B2 U L2 B2 L2 D U' L' F R B2 U L U2 L2 F  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 2 | 16 |
| At most 5 | 92 | 90 | 232 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 11 | 9 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F' L2 U2 L' U' B2 R' F' L   // normal, DR on U/D
(U2 R B U' R L B R2 D' B)   // inverse, DR on U/D
F' L2 U2 L' U' B2 R' F' L   // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: no normal EO; through an inverse EO: 11; with NISS EOs too: 10.

```
(D F2 R U')         // inverse EO on U/D
(R B' L F2 L F' L)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
R' F D' B L        // normal EO on R/L
U' B U R2 F D      // then DR on F/B
(U B R' B2 L)      // inverse EO on R/L
(U' B2 D R2 U' F)  // then DR on U/D
```


</details>

### Scramble 38

```
L2 D F2 U F2 D B2 L2 D R2 B2 F2 D F2 R' F' R U R' D F2 R D'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 22 | 18 | 12 |
| At most 5 | 246 | 198 | 248 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F' U L' F' B D' L' D B     // normal, DR on R/L
(B L' F2 L U' D2 L2 F' U)  // inverse, DR on R/L
F' U L' F' B D' L' D B     // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
F2 L' F U'             // normal EO on U/D
D2 R B' D2 R' F        // then DR on R/L
(U L B)                // inverse EO on F/B
(U2 L2 B2 D' L2 R' U)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
U' R2 F2 B' D          // normal EO on U/D
R' F2 L' F' L          // then DR on F/B
(U L B)                // inverse EO on F/B
(U2 L2 B2 D' L2 R' U)  // then DR on R/L
```


</details>

### Scramble 39

```
B2 F2 D2 U' B2 R2 F2 U' R2 U L2 F2 D' U' L' R' U' F2 L B D F2 D'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 52 | 18 | 8 |
| At most 5 | 402 | 268 | 264 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 9 | 9 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 8 | | | |
| NISS | 6 | | | |

For example:

```
B' U F2 B2 D R' F2 D         // normal, DR on R/L
(F2 R' U' R2 L' F2 D2 U' L)  // inverse, DR on F/B
B (R' L D F2 R)              // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 8; through an inverse EO: 10; with NISS EOs too: 8.

```
B'                 // normal EO on F/B
U F2 B2 D R' F2 D  // then DR on R/L
(L' D B2 R)        // inverse EO on R/L
(U D2 B' U2 D B)   // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 8; through an inverse EO: 10; with NISS EOs too: 8.

```
B'                 // normal EO on F/B
U F2 B2 D R' F2 D  // then DR on R/L
(L' D B2 R)        // inverse EO on R/L
(U D2 B' U2 D B)   // then DR on U/D
```


</details>

### Scramble 40

```
D2 R2 D' F2 L2 B2 D2 R2 D2 U B2 R2 U2 L' D2 U F R B L' F L U2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 4, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 28 | 64 | 16 |
| At most 5 | 376 | 426 | 228 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F' D2 F2 B' U' F' R U2 D2 B  // normal, DR on R/L
(F D B2 D' R' L' F' U R)     // inverse, DR on F/B
(F D B2 D' R' L' F' U R)     // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
B2 R' F' U'       // normal EO on U/D
F' B' R' F L F R  // then DR on F/B
(R2 B L' D')      // inverse EO on U/D
(R B L' U2 F' R)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
F' D2 F2 B' U'    // normal EO on U/D
F' R U2 D2 B      // then DR on R/L
(F' D2 R' F' L')  // inverse EO on R/L
(U2 F L2 U' F)    // then DR on U/D
```


</details>

### Scramble 41

```
B2 F2 R2 D B2 U' B2 D2 U' F2 U B2 L2 U' L' D U2 B2 F R D F R'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 4, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 42 | 22 | 24 |
| At most 5 | 364 | 282 | 472 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 9 | 9 |
| Inverse | 8 | 8 | 8 | 8 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
B2 U L2 U2 L' U' L' F   // normal, DR on R/L
(B R' F2 D' F R' D2 B)  // inverse, DR on R/L
R' U' R' D L2 F2 D B    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 8; with NISS EOs too: 8.

```
R' F2 R2 D'      // normal EO on U/D
L R2 D2 L' D2 F  // then DR on R/L
(B R' F2 D')     // inverse EO on U/D
(F R' D2 B)      // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 8; with NISS EOs too: 8.

```
R F' D' R' F'  // normal EO on F/B
B2 U2 D' L     // then DR on U/D
(B R' F2 D')   // inverse EO on U/D
(F R' D2 B)    // then DR on R/L
```


</details>

### Scramble 42

```
B2 D R2 D' B2 R2 B2 F2 U' R2 U F2 U R' F R B2 U2 L' U F D' B'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 10 | 8 |
| At most 5 | 12 | 192 | 232 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D F B D' U2 B' U' R D    // normal, DR on F/B
(F L U D' B U2 F2 B2 R)  // inverse, DR on U/D
D F B D' U2 B' U' R D    // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: no normal EO; through an inverse EO: 11; with NISS EOs too: 10.

```
(L B' D' L')          // inverse EO on R/L
(D' F2 L2 B' R2 U F)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 12; through an inverse EO: 9; with NISS EOs too: 9.

```
U2 B U' D L         // normal EO on R/L
U F2 B2 L2 U' R2 D  // then DR on F/B
(F L U D' B)        // inverse EO on F/B
(U2 F2 B2 R)        // then DR on U/D
```


</details>

### Scramble 43

```
F2 D' R2 B2 D L2 U2 L2 F2 D' R2 U2 F2 U' F' U' R' D' B R' F D' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 22 | 36 | 20 |
| At most 5 | 198 | 280 | 320 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 8 | 9 | 8 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
U R B U L' F D R U      // normal, DR on R/L
(U B' U D' F' B' U' L)  // inverse, DR on U/D
(U B' U D' F' B' U' L)  // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
U2 F2 D R       // normal EO on R/L
B2 D L2 F D B   // then DR on U/D
(D' R2 F B)     // inverse EO on F/B
(U L2 U' R' U)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
U2 F2 D R       // normal EO on R/L
B2 D L2 F D B   // then DR on U/D
(D' R2 F B)     // inverse EO on F/B
(U L2 U' R' U)  // then DR on R/L
```


</details>

### Scramble 44

```
U F2 U' L2 F2 D L2 B2 D R2 B2 R2 U B' D2 U R' B L D R' U' F  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 4 | 4 |
| At most 5 | 40 | 90 | 88 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 10 | | | |
| NISS | 9 | | | |

For example:

```
R F' D L' R2 B' D2 B2 R U   // normal, DR on R/L
(D R' B D' L B R2 F2 B2 D)  // inverse, DR on F/B
F (R F' R2 B D F L' U)      // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; through an inverse EO: 12; with NISS EOs too: 10.

```
(F R2 D' B)           // inverse EO on F/B
(L F2 D R B2 L F2 D)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
U' F2 D' R L    // normal EO on R/L
F' U R2 U L2 D  // then DR on F/B
(D R' B D' L)   // inverse EO on R/L
(B R2 F2 B2 D)  // then DR on F/B
```


</details>

### Scramble 45

```
B2 U2 B2 D F2 D' R2 F2 U' B2 L2 D' R2 U' L' D F' U' R2 U' B' F2 L' R'  // scramble
```

Bad edges on R/L, U/D, F/B: 10, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 4 |
| At most 5 | 10 | 38 | 136 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
L D B D2 L F R' F' U          // normal, DR on R/L
(B2 D' F' L F' B D' R' F2 U)  // inverse, DR on R/L
L D B D2 L F R' F' U          // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
L' U R L2 D'     // normal EO on U/D
B2 L2 F L2 B' R  // then DR on F/B
(B2 L' F D2 B)   // inverse EO on F/B
(U' L2 U L D R)  // then DR on U/D
```


</details>

### Scramble 46

```
D F2 U L2 D L2 U B2 R2 U' R2 D2 L2 D F' R F2 L U2 B' D' U' F' U  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 16 |
| At most 5 | 54 | 32 | 308 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D R' D' F' U2 D' F2 B' L' F  // normal, DR on R/L
(F2 L U' R U R F U R)        // inverse, DR on F/B
(F2 L U' R U R F U R)        // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 10.

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
D R' D' F' D'      // normal EO on U/D
U2 B' F2 L' F      // then DR on R/L
(B U2 D R' F')     // inverse EO on F/B
(L U' R2 U' B2 L)  // then DR on U/D
```


</details>

### Scramble 47

```
U R2 D2 R2 U2 F2 L2 R2 U' L2 R2 L' U L R2 B D2 L' U2 R  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 20 | 16 | 0 |
| At most 5 | 272 | 262 | 176 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
R' U2 L D2 B' R2 L' U' L   // normal, DR on U/D
(R' U F2 L2 D R D2 R' F)   // inverse, DR on R/L
R' U2 L D2 B' R2 L' U' L   // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
D2 L2 B' D           // normal EO on U/D
R2 B2 L B' D2 F      // then DR on R/L
(U R B2 U)           // inverse EO on U/D
(L2 F' L R2 B2 L F)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 9; with NISS EOs too: 9.

```
R' U2 L D2 B'   // normal EO on F/B
R2 L' U' L      // then DR on U/D
(R' U F2 L2 D)  // inverse EO on U/D
(R D2 R' F)     // then DR on R/L
```


</details>

### Scramble 48

```
F2 D2 R2 D' L2 U2 B2 L2 B2 L2 D F2 U2 R2 U' R' D L2 B L' B2 R2 D2 F' L2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 12 |
| At most 5 | 68 | 64 | 188 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 11 | 10 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
U2 F U F' R' D2 B L F2 U  // normal, DR on R/L
(F R' F' L D R D B U)     // inverse, DR on F/B
F R' U' B R2 F' U (L)     // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 8.

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 8.

```
D2 R B' U L       // normal EO on R/L
F2 U2 B' U2 D' B  // then DR on U/D
(R' F' L' D R)    // inverse EO on R/L
(B U F B2 D)      // then DR on F/B
```


</details>

### Scramble 49

```
F2 D2 R2 U L2 U B2 D' R2 B2 F2 D F2 R' B2 D' L B U R2 F L' B  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 0 |
| At most 5 | 42 | 22 | 132 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 10 | 10 | 11 | 10 |
| Best of the six | 10 | | | |
| NISS | 9 | | | |

For example:

```
B' L F' R2 U' B' L' D B2 R  // normal, DR on U/D
(R' D F D2 L' B' U F2 R F)  // inverse, DR on R/L
F R' U2 B' D R' F (R' D)    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; no EO at all.

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
D B2 L' F B        // normal EO on F/B
L D L' U F2 U      // then DR on R/L
(L' B U' D' F)     // inverse EO on F/B
(L' U' R L' D' R)  // then DR on U/D
```


</details>

### Scramble 50

```
F2 L2 F2 D U2 L2 F2 D' F2 L2 R2 U2 L2 F' U' B L B U2 B2 F' R U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 20 | 6 | 4 |
| At most 5 | 200 | 174 | 132 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F2 R U' F2 R' F2 R2 F' B L  // normal, DR on F/B
(B' L2 B' R U2 F' B' D' R)  // inverse, DR on U/D
(B' L2 B' R U2 F' B' D' R)  // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
F2 R U'             // normal EO on U/D
F2 R' F2 R2 F' B L  // then DR on F/B
(D2 R' F D)         // inverse EO on U/D
(F' R' L U2 B L)    // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
L F' B2 R' D'     // normal EO on U/D
R D2 L2 R2 F      // then DR on R/L
(D2 R' F D)       // inverse EO on U/D
(F' R' L U2 B L)  // then DR on F/B
```


</details>

### Scramble 51

```
L2 D2 R2 B2 D F2 D' L2 F2 R2 U2 F2 U2 F' R' U2 L B D' L' F2 D' U2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 14 | 8 | 12 |
| At most 5 | 226 | 154 | 208 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 9 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
B2 D' F' R' D R2 U L2 F  // normal, DR on R/L
(F2 L F B D R' F U2 F)   // inverse, DR on U/D
D B (D R2 U' F R U)      // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
U R B2 U          // normal EO on U/D
L F' R' D2 L' B   // then DR on R/L
(L B D R)         // inverse EO on R/L
(B' U B R2 F2 D)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
U R B2 U         // normal EO on U/D
L F' R' D2 L' B  // then DR on R/L
(D L' D B R)     // inverse EO on R/L
(B' U' R2 F U)   // then DR on F/B
```


</details>

### Scramble 52

```
D R2 F2 D' L2 F2 U2 R2 F2 U' F2 D' R D' B L' F2 D2 R' D' U  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 8, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 12 | 16 |
| At most 5 | 162 | 192 | 260 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 8 | 9 | 8 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
U' D R D2 F2 L B' D R  // normal, DR on U/D
(L U2 B2 D B2 D B' L)  // inverse, DR on U/D
(L U2 B2 D B2 D B' L)  // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
U2 D' L' B        // normal EO on F/B
D2 B2 R' U' F2 R  // then DR on U/D
(D R' F U)        // inverse EO on U/D
(D2 B F U2 R B)   // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
L F B2 D' R'   // normal EO on R/L
B R2 D B F     // then DR on U/D
(D R F R2 U)   // inverse EO on U/D
(B R' U2 R B)  // then DR on R/L
```


</details>

### Scramble 53

```
B2 D' L2 U R2 F2 U' R2 D2 F2 R2 D' R2 D2 R' D L2 F R2 D' F2 U' L U  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 8, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 14 | 36 |
| At most 5 | 174 | 204 | 332 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 9 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
D2 B U L' F' U2 D F2 D' F  // normal, DR on U/D
(U2 R' U R2 D' L2 F2 B U)  // inverse, DR on R/L
R' U R L F L (U' L)        // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 9.

```
D2 B U L'             // normal EO on R/L
F' U2 D F2 D' F       // then DR on U/D
(B' U D' R)           // inverse EO on R/L
(U' D' B L2 U' F2 D)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
D2 B U L'        // normal EO on R/L
F' U2 D F2 D' F  // then DR on U/D
(D' B' U D' R')  // inverse EO on R/L
(D2 F2 R2 F' D)  // then DR on F/B
```


</details>

### Scramble 54

```
F2 U2 F2 D' L2 D B2 U' B2 U' L2 D2 B' L F' R B U F L' R' D'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 28 | 20 | 28 |
| At most 5 | 412 | 224 | 420 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 10 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
L' D L' U2 L' F U2 L' B  // normal, DR on R/L
(R U2 F' L U2 F U F L)   // inverse, DR on F/B
D2 B (R L U2 F U L)      // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
L' D                // normal EO on U/D
L' U2 L' F U2 L' B  // then DR on R/L
(B' R F' U)         // inverse EO on U/D
(F2 R2 F U2 R' B)   // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
R2 F2 L B2 U'   // normal EO on U/D
B F' L' F       // then DR on R/L
(U2 R' F D' L)  // inverse EO on R/L
(F D L2 B' D)   // then DR on F/B
```


</details>

### Scramble 55

```
D2 L2 F2 L2 D' R2 B2 F2 U' F2 D' R2 U B' D U2 F U' L' R' U F2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 0 | 16 |
| At most 5 | 142 | 100 | 212 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U' R F U L' F R2 F D        // normal, DR on F/B
(F2 R D' L2 U' R U2 R B L)  // inverse, DR on F/B
F D' B2 R' U' L D R' D      // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; no inverse EO; with NISS EOs too: 10.

```
F' B L B'        // normal EO on F/B
L R2 B2 U' B2 D  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
U' R F U L'      // normal EO on R/L
F R2 F D         // then DR on F/B
(F2 R D' L2 U')  // inverse EO on U/D
(R U2 R B L)     // then DR on F/B
```


</details>

### Scramble 56

```
F2 D B2 D' R2 D' F2 L2 D2 B2 L2 D2 U' B2 R' D U2 B' F2 L F' L2 D'  // scramble
```

Bad edges on R/L, U/D, F/B: 2, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 50 | 10 | 12 |
| At most 5 | 492 | 218 | 276 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 10 |
| Inverse | 9 | 9 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D L2 F L' F2 B U2 D' R   // normal, DR on U/D
(B' R L2 F D R' F U B)   // inverse, DR on U/D
D L2 F L' F2 B U2 D' R   // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
U' R F2 R           // normal EO on R/L
D2 F2 D' B U2 B2 U  // then DR on F/B
(F R U R')          // inverse EO on R/L
(D' F' D' F D B)    // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
D L2 F L' B     // normal EO on F/B
F2 U2 D' R      // then DR on U/D
(F D' R U R)    // inverse EO on R/L
(U F' U' R2 B)  // then DR on U/D
```


</details>

### Scramble 57

```
R2 D2 L2 B2 D' F2 D' F2 R2 F2 U2 B2 D R' D2 F U' B L' B2 D F D  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 14 | 4 |
| At most 5 | 120 | 230 | 204 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 9 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
F D B2 L U R2 F' U R2 B    // normal, DR on U/D
(D' F' B' R B U2 B2 U' B)  // inverse, DR on U/D
F' R F2 B' R2 D L (D)      // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
F D B2 L        // normal EO on R/L
U B F2 U' L2 F  // then DR on U/D
(D' F' B' R)    // inverse EO on R/L
(B U2 B2 U' B)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
F D B2 L        // normal EO on R/L
U B F2 U' L2 F  // then DR on U/D
(D' F' B' R)    // inverse EO on R/L
(B U2 B2 U' B)  // then DR on U/D
```


</details>

### Scramble 58

```
L2 B2 U' F2 D L2 F2 U L2 U' B2 R2 F2 B' L2 R' B' D' R D2 R B'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 2 | 14 | 0 |
| At most 5 | 136 | 234 | 128 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
B R' D2 R' D B R L2 B     // normal, DR on U/D
(B2 R B L' F B2 R2 D' R)  // inverse, DR on F/B
B R' D2 R' D B R L2 B     // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 12; through an inverse EO: 10; with NISS EOs too: 10.

```
B L F D               // normal EO on U/D
F2 R L' F' L' B D2 R  // then DR on F/B
(U2 L2 F D)           // inverse EO on U/D
(U2 F' L B2 R B)      // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
D2 R' F' B D'    // normal EO on U/D
L2 U2 L' U2 L B  // then DR on R/L
(U2 L2 U2 F D')  // inverse EO on U/D
(R2 B F' R' B)   // then DR on R/L
```


</details>

### Scramble 59

```
B2 F2 D2 L2 D R2 U F2 L2 D F2 D L2 B2 U2 F' D2 L' D' U2 F R2 B D2 U  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 22 | 18 | 16 |
| At most 5 | 290 | 212 | 236 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F2 L' F' B2 L' F2 U2 B' D' B  // normal, DR on U/D
(R2 B2 L' U2 B' U L B2 D)     // inverse, DR on F/B
(R2 B2 L' U2 B' U L B2 D)     // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
U2 F' D2 R              // normal EO on R/L
F B2 U' F R2 B' U       // then DR on F/B
(D B L)                 // inverse EO on R/L
(D B D' B2 F2 L2 U' F)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
F2 L' F' B2 L'   // normal EO on R/L
F2 U2 B' D' B    // then DR on U/D
(U D' F2 B' R')  // inverse EO on R/L
(U' B L2 D' F)   // then DR on U/D
```


</details>

### Scramble 60

```
U2 L2 D' L2 D F2 L2 D R2 U' L2 D' R2 F2 U L' D R2 F R F' L' F  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 20 | 22 | 12 |
| At most 5 | 430 | 296 | 260 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 9 | 8 | 8 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
F' L F R' F' R2 D' L     // normal, DR on U/D
(D L U2 L U' B R2 U2 R)  // inverse, DR on F/B
F' L F R' F' R2 D' L     // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
U' R' U2 F         // normal EO on F/B
U2 R2 U2 R' U' R   // then DR on U/D
(D' R2 L U')       // inverse EO on U/D
(R' L' B' R F' R)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 8; through an inverse EO: 9; with NISS EOs too: 8.

```
F2 R L D' L    // normal EO on R/L
B' R2 D        // then DR on F/B
(D L U2 L U')  // inverse EO on U/D
(B R2 U2 R)    // then DR on F/B
```


</details>

### Scramble 61

```
U' B2 D F2 D' B2 D' B2 F2 D2 R2 B2 D2 R2 B' D R B' D2 U' R U2 B2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 30 | 16 | 36 |
| At most 5 | 296 | 350 | 336 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 8 | 9 | 8 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
B2 R' D R2 F2 L2 D2 R' F  // normal, DR on R/L
(R2 L' F2 L' D2 F' D R)   // inverse, DR on U/D
(R2 L' F2 L' D2 F' D R)   // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 11; with NISS EOs too: 9.

```
B2 R' D                // normal EO on U/D
R2 F2 L2 D2 R' F       // then DR on R/L
(D' R B D)             // inverse EO on U/D
(B' R2 B' U2 B' D2 B)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
B2 R' D           // normal EO on U/D
R2 F2 L2 D2 R' F  // then DR on R/L
(D2 R' F2 U L')   // inverse EO on R/L
(F L2 F' U B)     // then DR on U/D
```


</details>

### Scramble 62

```
U2 F2 U L2 U F2 L2 U F2 U' L2 U L2 U2 L' D U2 B D' L' B R U'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 6 | 10 | 20 |
| At most 5 | 230 | 210 | 236 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 10 |
| Inverse | 8 | 10 | 9 | 8 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
U B2 D' R F2 U' L' R B   // normal, DR on R/L
(R2 B U' B2 D' R2 F' L)  // inverse, DR on F/B
(R2 B U' B2 D' R2 F' L)  // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
D' F2 L' U'     // normal EO on U/D
F R U2 B' U2 F  // then DR on R/L
(B' D' F2 L')   // inverse EO on R/L
(F R2 B U F)    // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 8; with NISS EOs too: 8.

```
D F U' B' L'     // normal EO on R/L
B L2 U' R2 B     // then DR on U/D
(R2 B U' B2 D')  // inverse EO on U/D
(R2 F' L)        // then DR on F/B
```


</details>

### Scramble 63

```
D2 B2 U F2 L2 R2 D R2 F2 U R2 D' B L' B2 F' L2 D F U R  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 16 | 0 | 8 |
| At most 5 | 248 | 58 | 288 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F2 B R2 U R D' R B2 R     // normal, DR on F/B
(F R B2 D' B' U' F R2 B)  // inverse, DR on R/L
R' U' F' D' L2 F B2 L B   // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; no inverse EO; with NISS EOs too: 10.

```
U' B2 D L        // normal EO on R/L
F' B U' F2 L2 U  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
U' B2 D L        // normal EO on R/L
F' B U' F2 L2 U  // then DR on F/B
(D2 F U F L)     // inverse EO on R/L
(U B' D B U)     // then DR on F/B
```


</details>

### Scramble 64

```
B2 D F2 D2 B2 D' B2 D' R2 D' F2 U' R2 U' L' D' F' R' B L U B F' R2  // scramble
```

Bad edges on R/L, U/D, F/B: 10, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 16 |
| At most 5 | 54 | 24 | 128 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
L' F2 U L2 F L R' B' U     // normal, DR on R/L
(B2 D2 R U' F' B2 R' B L)  // inverse, DR on U/D
L' F2 U L2 F L R' B' U     // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 9.

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 9.

```
F' U D R D'      // normal EO on U/D
R' F' L B F      // then DR on R/L
(U F D' R B)     // inverse EO on F/B
(R2 L U R' D R)  // then DR on U/D
```


</details>

### Scramble 65

```
R2 D R2 F2 D F2 U' B2 L2 D B2 D2 F2 U R' U2 F' R2 B2 D' U' L' F L'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 10, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 0 | 8 |
| At most 5 | 68 | 46 | 232 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 11 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
L F' L U D B2 R2 F U2 R  // normal, DR on U/D
(R' B D2 F U B U2 D R)   // inverse, DR on U/D
(R' B D2 F U B U2 D R)   // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; no inverse EO; with NISS EOs too: 9.

```
B' U F B'          // normal EO on F/B
U2 D L' B2 R B2 U  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 9.

```
U D2 F' R2 B     // normal EO on F/B
R D2 L' F2 D R   // then DR on U/D
(R F B U B)      // inverse EO on F/B
(F2 D R U2 R U)  // then DR on R/L
```


</details>

### Scramble 66

```
F2 D' R2 B2 U' R2 U' F2 D2 B2 R2 U' F2 R2 D2 F' R B2 R F' L D U' F U2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 26 | 24 | 8 |
| At most 5 | 290 | 312 | 248 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 9 | 9 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
F' D B2 R2 B' R2 U' D2 F   // normal, DR on R/L
(R' B D' B' U' F L' D' L)  // inverse, DR on U/D
B U B' U' D L F (F)        // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
L2 U' D L          // normal EO on R/L
F D' F' R2 U' F    // then DR on U/D
(U R2 D2 R)        // inverse EO on R/L
(F' B' U F' R2 U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
L2 U' D L          // normal EO on R/L
F D' F' R2 U' F    // then DR on U/D
(U R2 D2 R)        // inverse EO on R/L
(F' B' U F' R2 U)  // then DR on F/B
```


</details>

### Scramble 67

```
D' B2 D2 L2 D F2 L2 U2 F2 R2 U' R2 B2 U B' D' B' F L' F R B' R2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 8, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 16 | 0 |
| At most 5 | 116 | 200 | 72 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U R2 B R' F' L F' B D B    // normal, DR on U/D
(L' F U' D' B' U R' B' L)  // inverse, DR on U/D
(L' F U' D' B' U R' B' L)  // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
U' R L' D           // normal EO on U/D
F' R2 B R' L' B' R  // then DR on F/B
(L F R B)           // inverse EO on F/B
(U2 F2 U' L R' D)   // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
R2 B R' F' L    // normal EO on R/L
U' F D F2 U' B  // then DR on U/D
(L' F D R' L')  // inverse EO on R/L
(F D' R2 B U)   // then DR on F/B
```


</details>

### Scramble 68

```
B2 L2 D' R2 F2 D' F2 D B2 D R2 D2 B2 L2 U' F' L D U' R B2 U L' B2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 18 | 24 | 4 |
| At most 5 | 368 | 288 | 212 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 9 | 9 |
| Inverse | 9 | 9 | 9 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
L' F' L' U2 R' U' B2 D     // normal, DR on R/L
(B2 R' L2 F2 B' L B U' B)  // inverse, DR on U/D
L' F' L' U2 R' U' B2 D     // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 8; through an inverse EO: 10; with NISS EOs too: 8.

```
L' F'             // normal EO on F/B
L' U2 R' U' B2 D  // then DR on R/L
(B D L2 B)        // inverse EO on F/B
(R L D' F2 B2 L)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 8; through an inverse EO: 10; with NISS EOs too: 8.

```
L' F'             // normal EO on F/B
L' U2 R' U' B2 D  // then DR on R/L
(B L' B U2 R)     // inverse EO on R/L
(D2 F2 R2 D F)    // then DR on U/D
```


</details>

### Scramble 69

```
R2 B2 F2 D2 L2 B2 D' R2 D L2 R2 D R2 U' B' R2 D' R' F U L D2 F' D2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 20 |
| At most 5 | 68 | 4 | 120 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
L F2 D F' U' B' D L2 D' L   // normal, DR on U/D
(B' U2 F' D' L' B2 U B2 R)  // inverse, DR on F/B
(B' U2 F' D' L' B2 U B2 R)  // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 12; with NISS EOs too: 11.

```
B2 L U F' R          // normal EO on R/L
F2 D B R2 U2 F       // then DR on U/D
(F2 D F L B')        // inverse EO on F/B
(D L2 R' B2 R F2 D)  // then DR on R/L
```


</details>

### Scramble 70

```
R2 B2 U2 B2 U L2 U2 R2 U2 B2 L2 U' B' D2 L' F D2 R F' U2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 2, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 48 | 60 | 8 |
| At most 5 | 524 | 572 | 356 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 8 | 9 |
| Inverse | 8 | 8 | 9 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
L' U' L2 U' F' L2 R' B   // normal, DR on R/L
(U2 R2 U B' R2 U' F' U)  // inverse, DR on R/L
L' U' L2 U' F' L2 R' B   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 8; through an inverse EO: 9; with NISS EOs too: 8.

```
L' U' L2 U'       // normal EO on U/D
F' L2 R' B        // then DR on R/L
(D' F2 D)         // inverse EO on U/D
(F L B2 L' R2 B)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 8; through an inverse EO: 9; with NISS EOs too: 8.

```
L' U' L2 U'       // normal EO on U/D
F' L2 R' B        // then DR on R/L
(D' F2 D)         // inverse EO on U/D
(F L B2 L' R2 B)  // then DR on R/L
```


</details>

### Scramble 71

```
B2 L2 U' L2 U' F2 D R2 B2 D R2 U' F2 D2 R' F' D L' B2 R2 B D2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 2 | 16 | 0 |
| At most 5 | 64 | 326 | 80 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U D2 B' R2 B2 L D' F R    // normal, DR on U/D
(R2 L F U' R D2 L2 U' L)  // inverse, DR on F/B
U D2 B' R2 B2 L D' F R    // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
B' R' L2 F               // normal EO on F/B
U B2 D' R' L' U L        // then DR on U/D
(R U)                    // inverse EO on U/D
(R' U2 B' D2 F2 L2 R B)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
U2 B R L' D      // normal EO on U/D
R' B' L' B U2 B  // then DR on R/L
(D R2 U R D)     // inverse EO on U/D
(L B' R' F R)    // then DR on F/B
```


</details>

### Scramble 72

```
D' F2 R2 U2 R2 U B2 U F2 U R2 U2 L2 U2 B' F' D' L B R U' L2 F' R2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 16 | 0 |
| At most 5 | 44 | 92 | 80 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 10 | | | |
| NISS | 8 | | | |

For example:

```
R2 F L2 U R' B' L' D F B        // normal, DR on U/D
(R2 F' D2 R' L2 D' F' B' U' L)  // inverse, DR on U/D
R' L F R (D R2 B R)             // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: no normal EO; through an inverse EO: 11; with NISS EOs too: 11.

```
(R D B' U')        // inverse EO on U/D
(D2 R B F D2 R B)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
U2 F U L' D'       // normal EO on U/D
B' L U2 R D2 B     // then DR on R/L
(R D B' U')        // inverse EO on U/D
(D2 R B F D2 R B)  // then DR on R/L
```


</details>

### Scramble 73

```
D' R2 U2 B2 F2 U F2 U' B2 L2 R2 U2 R' B' D L2 U R2 B' D2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 14 | 20 |
| At most 5 | 122 | 162 | 232 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 9 | 8 | 10 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
D2 B R2 U' L2 D' B R        // normal, DR on U/D
(R' B2 D' B' L' U L2 D2 B)  // inverse, DR on R/L
D2 B R2 U' L2 D' B R        // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
F D' R2 B             // normal EO on F/B
D' B2 D R2 B2 U' L    // then DR on U/D
(U D R)               // inverse EO on R/L
(B2 F D' B2 U' R2 B)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 9.

```
U D' R2 F2 L'         // normal EO on R/L
D' R2 F' L2 U' B      // then DR on U/D
(U D R)               // inverse EO on R/L
(B2 F D' B2 U' R2 B)  // then DR on U/D
```


</details>

### Scramble 74

```
D F2 U R2 U' F2 L2 D' F2 D2 L2 B2 D' L' U2 B' R U F L2 D' B R'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 10.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 0 | 4 |
| At most 5 | 82 | 20 | 112 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 9 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F L' D' B' U B2 U F2 L F   // normal, DR on R/L
(L2 F L' B' U D R' D2 F)   // inverse, DR on U/D
(B' L' F U' D2 R F2 D' B)  // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; no inverse EO; with NISS EOs too: 11.

```
F L' D2 R'          // normal EO on R/L
U' F2 D' B U' D2 F  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 12; with NISS EOs too: 9.

```
R' F L U2 R        // normal EO on R/L
U2 B' U L2 D' F    // then DR on U/D
(L2 D' F' U D')    // inverse EO on U/D
(R U2 L B R2 B R)  // then DR on F/B
```


</details>

### Scramble 75

```
D' F2 U' R2 B2 L2 R2 D' R2 U2 B2 F2 U' R' D B L F' D2 B L R2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 26 | 10 | 8 |
| At most 5 | 278 | 198 | 136 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 7 | 10 | 10 | 7 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 7 | | | |
| NISS | 7 | | | |

For example:

```
B R L2 B' L' B' U          // normal, DR on F/B
(U2 B R2 U R' F' L2 D2 B)  // inverse, DR on R/L
B R L2 B' L' B' U          // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
R L2 U'           // normal EO on U/D
B F2 U2 B D2 L B  // then DR on R/L
(U2 B R2 U)       // inverse EO on U/D
(R' B' U2 L2 F)   // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 7; through an inverse EO: 9; with NISS EOs too: 7.

```
B R L2 B' L'     // normal EO on R/L
B' U             // then DR on F/B
(U2 B R2 U)      // inverse EO on U/D
(R' B' U2 L2 F)  // then DR on R/L
```


</details>

### Scramble 76

```
U' B2 U' F2 D L2 R2 D F2 U' F2 U' R2 U F' L R2 B' D L F2 U' F' R U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 12 | 24 |
| At most 5 | 108 | 122 | 340 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 11 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U' F' R' F R2 B' D R2 B      // normal, DR on R/L
(R' D2 B L F' L2 F' U' D B)  // inverse, DR on U/D
U' F' R' F R2 B' D R2 B      // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 9.

```
U' R D2 L'         // normal EO on R/L
D F' B D F' L2 U   // then DR on F/B
(R' D2 B L)        // inverse EO on R/L
(F' L2 F' U' D B)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 9.

```
U' R D2 L'         // normal EO on R/L
D F' B D F' L2 U   // then DR on F/B
(R' D2 B L)        // inverse EO on R/L
(F' L2 F' U' D B)  // then DR on U/D
```


</details>

### Scramble 77

```
U2 F2 D B2 L2 D B2 L2 D L2 U' B2 D2 L2 U' L' F U' L2 B F2 L' D2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 12 | 0 | 24 |
| At most 5 | 174 | 96 | 304 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 11 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D2 B' R' L' F' D2 R' D B  // normal, DR on U/D
(U' F L D2 F' D F B L)    // inverse, DR on F/B
D2 F' D' L' R2 D B' D F   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; no inverse EO; with NISS EOs too: 9.

```
R D B' L          // normal EO on R/L
U2 L2 B' R2 U2 B  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 9.

```
D B R' B2 L'       // normal EO on R/L
F' U L2 U F        // then DR on U/D
(D2 L B R L')      // inverse EO on R/L
(B2 U R2 U' B' U)  // then DR on F/B
```


</details>

### Scramble 78

```
B2 U' R2 U' B2 L2 D2 B2 L2 U2 B2 L2 U' R2 B' D' U F R' B' R U B'  // scramble
```

Bad edges on R/L, U/D, F/B: 2, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 46 | 32 | 12 |
| At most 5 | 454 | 392 | 272 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 7 | 9 | 7 | 10 |
| Best of the six | 7 | | | |
| NISS | 7 | | | |

For example:

```
B U' R' B R F' U' D B  // normal, DR on U/D
(L U' L F B2 U B)      // inverse, DR on U/D
(L U' L F B2 U B)      // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 7; with NISS EOs too: 7.

```
R' B2 R          // normal EO on R/L
F B U B R2 F2 U  // then DR on F/B
(L U' L)         // inverse EO on R/L
(B2 F U B)       // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 7; with NISS EOs too: 7.

```
B U' R' B R  // normal EO on R/L
F' U' D B    // then DR on U/D
(L U' L)     // inverse EO on R/L
(B2 F U B)   // then DR on U/D
```


</details>

### Scramble 79

```
R2 D' F2 R2 D' B2 L2 R2 U F2 D B2 D' F' U2 L B U2 L2 R F2 R'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 14 | 28 | 12 |
| At most 5 | 216 | 302 | 252 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
R F2 R' L2 U2 B' L' U2 F   // normal, DR on U/D
(D F B' L F' R' U L U)     // inverse, DR on R/L
R F2 R' L2 U2 B' L' U2 F   // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
L' F2 B R'         // normal EO on R/L
L2 D F D B L2 D    // then DR on F/B
(U D L2 U)         // inverse EO on U/D
(B2 L' U2 R F' L)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
F2 R D2 F L    // normal EO on R/L
B L2 B' L2 U   // then DR on F/B
(D F B' L F')  // inverse EO on F/B
(R' U L U)     // then DR on R/L
```


</details>

### Scramble 80

```
B2 D R2 U' R2 F2 L2 R2 U' F2 U' R2 U2 B2 U' B' R' D2 F2 U2 F2 U2 F' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 4, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 64 | 82 | 20 |
| At most 5 | 636 | 780 | 484 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 10 |
| Inverse | 7 | 8 | 7 | 9 |
| Best of the six | 7 | | | |
| NISS | 7 | | | |

For example:

```
R' U2 L2 F' R2 U L' R U  // normal, DR on R/L
(F' D' B' L' U2 L2 B)    // inverse, DR on U/D
(F' D' B' L' U2 L2 B)    // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 7; with NISS EOs too: 7.

```
R' U2 L2 F'    // normal EO on F/B
R2 U L' R U    // then DR on R/L
(F' D' B' L')  // inverse EO on R/L
(U2 L2 B)      // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 7; with NISS EOs too: 7.

```
U L2 U R2 U    // normal EO on U/D
R' U2 R' F     // then DR on R/L
(F' D' B' L')  // inverse EO on R/L
(U2 L2 B)      // then DR on U/D
```


</details>

### Scramble 81

```
U' F2 U F2 L2 U F2 L2 D L2 U2 F2 R2 F2 U2 F' R' B R' D B2 L' U' L2 D2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 8, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 32 | 0 | 4 |
| At most 5 | 190 | 10 | 224 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 10 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
B U' D' L R F B R F      // normal, DR on R/L
(R U' D R' F L R' U B)   // inverse, DR on R/L
F2 B' U D' B' U2 L R B   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; no inverse EO; with NISS EOs too: 9.

```
F2 B' U D'   // normal EO on U/D
B' U2 L R B  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 11; with NISS EOs too: 9.

```
F2 B' U D'         // normal EO on U/D
B' U2 L R B        // then DR on R/L
(B' L F B2 R)      // inverse EO on R/L
(U B2 R2 L2 F' U)  // then DR on F/B
```


</details>

### Scramble 82

```
D B2 U2 F2 R2 F2 D' R2 B2 U' B2 D F2 B' L' U R2 D2 U' B R2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 20 | 8 | 8 |
| At most 5 | 210 | 170 | 200 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 10 | 8 | 10 |
| Inverse | 9 | 10 | 9 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
R2 B' U D2 R2 U' L B      // normal, DR on U/D
(U2 B' L2 D' U R2 L B D)  // inverse, DR on F/B
R2 B' U D2 R2 U' L B      // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
B U L' F'          // normal EO on F/B
L U D F2 R         // then DR on U/D
(U' R2 F D')       // inverse EO on U/D
(B' R2 D2 R U2 B)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
B U L' F'        // normal EO on F/B
L U D F2 R       // then DR on U/D
(U' B D' B2 L')  // inverse EO on R/L
(R2 F R2 U F)    // then DR on U/D
```


</details>

### Scramble 83

```
U B2 L2 F2 L2 D L2 U2 F2 L2 R2 D L2 U' F' U' B D' L' B' F L2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 16 | 4 | 4 |
| At most 5 | 152 | 152 | 172 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 8 | 9 | 8 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
U2 L2 F' B L D B' U F     // normal, DR on U/D
(R' F' B2 D' B' L' D' L)  // inverse, DR on U/D
(R' F' B2 D' B' L' D' L)  // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
U2 F' B L          // normal EO on R/L
U' B R2 U F' D     // then DR on F/B
(D F' D' R)        // inverse EO on R/L
(B2 D B' L2 D' F)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 8; with NISS EOs too: 8.

```
U2 L2 F' B L      // normal EO on R/L
D B' U F          // then DR on U/D
(R' F' B2 D' B')  // inverse EO on F/B
(L' D' L)         // then DR on U/D
```


</details>

### Scramble 84

```
U' F2 D B2 L2 D2 R2 F2 U' B2 F2 R2 B' L2 R' F R U2 L' R2 D'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 52 | 16 | 20 |
| At most 5 | 606 | 248 | 372 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
B' L U2 F' U' B U' D' F     // normal, DR on U/D
(R F D' R F' U2 F' L2 F U)  // inverse, DR on F/B
B' L (D B2 L2 F' U B)       // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
L2 D F L           // normal EO on R/L
U' R2 B' L2 B      // then DR on U/D
(R F D' R)         // inverse EO on R/L
(F' U2 F' L2 F U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
D F U B L'         // normal EO on R/L
U B R2 D           // then DR on F/B
(R F D' R)         // inverse EO on R/L
(F' U2 F' L2 F U)  // then DR on F/B
```


</details>

### Scramble 85

```
F2 R2 F2 R2 D L2 U2 R2 D2 U' B2 U2 R2 L' U' L F' U L U2 B R  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 20 |
| At most 5 | 94 | 42 | 280 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 9 | 11 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
R' B' U2 L' U' F L' U L  // normal, DR on U/D
(L D R D L U' F' B' R)   // inverse, DR on U/D
D F' D' R F B (F2 D)     // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 8.

```
R' F' B D R'     // normal EO on R/L
U L2 B D2 B      // then DR on U/D
(D' L' F' R' L)  // inverse EO on R/L
(B D' B U F2 U)  // then DR on F/B
```


</details>

### Scramble 86

```
L2 F2 U R2 F2 U2 L2 U B2 U B2 U' R2 D' L' U L2 B2 F' U' L' F2 D2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 4, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 26 | 16 | 12 |
| At most 5 | 400 | 270 | 328 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 9 | 10 |
| Inverse | 9 | 9 | 9 | 9 |
| Best of the six | 8 | | | |
| NISS | 7 | | | |

For example:

```
F2 D B2 L U B2 D' F         // normal, DR on R/L
(D2 B2 L' U2 B U' R2 U' R)  // inverse, DR on U/D
F (R' B D' L D' B)          // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
R2 D2 R D'         // normal EO on U/D
B2 U2 B2 D2 R' F   // then DR on R/L
(R' D' B L')       // inverse EO on R/L
(D R2 B' U2 R2 B)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 9; with NISS EOs too: 9.

```
D2 F2 L U F     // normal EO on F/B
B2 L2 U' L      // then DR on U/D
(R B2 L B' D')  // inverse EO on U/D
(U2 F' U2 L)    // then DR on F/B
```


</details>

### Scramble 87

```
D' L2 D' R2 D' R2 D2 B2 U' R2 D' B2 U2 B2 U' L' B F' D' L F R2 D2 R  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 4, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 24 | 4 |
| At most 5 | 130 | 250 | 180 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 10 | 9 | 8 |
| Inverse | 9 | 9 | 9 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
L2 D' B D F' R' B2 D     // normal, DR on F/B
(D F2 R F' B D B2 U' F)  // inverse, DR on U/D
L2 D' B D F' R' B2 D     // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
R L' B D'         // normal EO on U/D
L' B U2 F B2 L    // then DR on F/B
(D F2 R)          // inverse EO on R/L
(B F' D B2 U' F)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
L2 D F' B R       // normal EO on R/L
D' F' U R2 U      // then DR on F/B
(D F2 R)          // inverse EO on R/L
(B F' D B2 U' F)  // then DR on U/D
```


</details>

### Scramble 88

```
L2 U B2 R2 D' L2 D2 F2 D L2 D' B2 U' B' U' R2 B2 R' F L2 D2 F2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 20 | 14 | 28 |
| At most 5 | 238 | 248 | 260 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 10 |
| Inverse | 8 | 8 | 10 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
F2 D2 L2 F' R B2 R2 U B  // normal, DR on U/D
(R F U' B' R' D2 R' D)   // inverse, DR on R/L
(R F U' B' R' D2 R' D)   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 8; with NISS EOs too: 8.

```
D2 L2 F' R        // normal EO on R/L
L2 B' D2 B2 D' F  // then DR on U/D
(R F U' B')       // inverse EO on F/B
(R' D2 R' D)      // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 8; with NISS EOs too: 8.

```
F2 D2 L2 F' R  // normal EO on R/L
B2 R2 U B      // then DR on U/D
(R F U' B')    // inverse EO on F/B
(R' D2 R' D)   // then DR on R/L
```


</details>

### Scramble 89

```
U L2 B2 D R2 F2 U B2 D' B2 L2 B2 F2 U2 R' U2 R2 F' R2 D' B' L F  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 6 | 10 | 0 |
| At most 5 | 160 | 226 | 124 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 10 | 9 | 8 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
R F R' D2 L B U' R        // normal, DR on F/B
(U2 R D2 R' B D F' L' B)  // inverse, DR on R/L
R F R' D2 L B U' R        // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
F L B U'               // normal EO on U/D
F U2 L B' D2 B         // then DR on R/L
(D2 R B D')            // inverse EO on U/D
(F2 U2 L' B' D2 B' L)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
F L B U'        // normal EO on U/D
F U2 L B' D2 B  // then DR on R/L
(F R L' F D)    // inverse EO on U/D
(R2 L2 B U2 L)  // then DR on F/B
```


</details>

### Scramble 90

```
U' B2 L2 D' B2 U2 L2 U B2 F2 L2 D B2 R2 U' L' B2 R' B' U2 L2 B L2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 2, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 62 | 36 | 20 |
| At most 5 | 672 | 542 | 412 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
D L' D B2 U2 F' D2 R' F   // normal, DR on R/L
(D' R' L D' L D2 U2 R D)  // inverse, DR on F/B
R' D' F2 R' D B (F2 D)    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
D L' D            // normal EO on U/D
B2 U2 F' D2 R' F  // then DR on R/L
(L2 U' F2 U)      // inverse EO on U/D
(L2 F U2 B L B)   // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
D L' D            // normal EO on U/D
B2 U2 F' D2 R' F  // then DR on R/L
(U2 F2 D F2 D)    // inverse EO on U/D
(B' R U2 R2 B)    // then DR on R/L
```


</details>

### Scramble 91

```
L2 D2 B2 R2 D' L2 D R2 B2 D' R2 F2 D2 R' F U' F2 U' L' B2 D' F2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 2 | 20 | 28 |
| At most 5 | 114 | 182 | 364 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 10 |
| Inverse | 9 | 10 | 9 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F2 D B2 L U F2 U F' R     // normal, DR on U/D
(U L2 U' F2 D' L F D2 R)  // inverse, DR on U/D
F2 D B2 L U F2 U F' R     // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 12; through an inverse EO: 10; with NISS EOs too: 10.

```
D' R' U' F           // normal EO on F/B
U L' D' F2 D R D2 L  // then DR on U/D
(D R' U B')          // inverse EO on F/B
(F2 U' L2 D' R' D)   // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
D' R U' R2 F'    // normal EO on F/B
U' F2 U B2 R     // then DR on U/D
(D R' U F2 B')   // inverse EO on F/B
(U' L2 D' R' D)  // then DR on R/L
```


</details>

### Scramble 92

```
R2 U2 R2 B2 D L2 B2 L2 D2 B2 U B2 U' F' U B2 L B D L2 R' D2 F'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 10.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 0 | 8 |
| At most 5 | 84 | 64 | 144 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D2 U F L U R U2 F' D      // normal, DR on F/B
(U2 B' L' U F B L' D' B)  // inverse, DR on R/L
D2 U F L U R U2 F' D      // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; no inverse EO; with NISS EOs too: 11.

```
D2 F R L           // normal EO on R/L
F2 D F' B' U B2 U  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
F R' L2 B' L'      // normal EO on R/L
F' U B' D2 F       // then DR on U/D
(D' L U B R)       // inverse EO on R/L
(U' F R2 U' L2 D)  // then DR on F/B
```


</details>

### Scramble 93

```
F2 R2 D B2 R2 D' B2 D2 U' R2 U' R2 F2 U' R2 B' D L' D2 F2 R2 F' D' U2 R'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 24 | 8 | 0 |
| At most 5 | 290 | 164 | 164 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 8 | 8 | 10 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
D F L' D B2 L U' B' D    // normal, DR on F/B
(L2 R2 U' B' D' L2 U F)  // inverse, DR on R/L
(L2 R2 U' B' D' L2 U F)  // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
L' U2 F2 R        // normal EO on R/L
U' B L2 U2 F2 D   // then DR on F/B
(D' F U D')       // inverse EO on U/D
(B R F B2 R F R)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
L' U2 F2 R       // normal EO on R/L
U' B L2 U2 F2 D  // then DR on F/B
(L2 U2 F B' R')  // inverse EO on R/L
(D' R2 F' U)     // then DR on F/B
```


</details>

### Scramble 94

```
B2 R2 D' L2 U2 B2 U2 F2 R2 U' L2 F2 U' F' U' L' B2 U R D' F D2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 4 |
| At most 5 | 12 | 90 | 280 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 10 | | | |
| NISS | 9 | | | |

For example:

```
R' U B D2 B2 U F B2 R U   // normal, DR on R/L
(R L F' L2 U B U R' D L)  // inverse, DR on U/D
F U' R' B' L R2 F D (B)   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
U R' B D2 F       // normal EO on F/B
B2 U L2 D' R' D   // then DR on R/L
(R F R' D L)      // inverse EO on R/L
(D2 L2 F U L2 F)  // then DR on U/D
```


</details>

### Scramble 95

```
U L2 D F2 U2 L2 B2 U R2 U L2 R2 F2 U' F' U B L' U' B' L B2 D  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 32 | 0 | 4 |
| At most 5 | 286 | 22 | 208 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 10 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D' B2 L' B U L B' U' F   // normal, DR on U/D
(R2 B L U R' B2 R' F U)  // inverse, DR on R/L
F' L' F2 L2 B U F2 D B   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; no inverse EO; with NISS EOs too: 10.

```
L2 F' L           // normal EO on R/L
B U F' R2 B' U F  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
L2 D' F' D L'      // normal EO on R/L
D' B R2 F2 U       // then DR on F/B
(U F D F R)        // inverse EO on R/L
(F2 B2 D2 B R2 U)  // then DR on F/B
```


</details>

### Scramble 96

```
F2 L2 F2 D B2 U' F2 D2 L2 D B2 L2 U B2 R' U' L2 R' B D R2 U2 B' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 2, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 24 | 22 | 16 |
| At most 5 | 332 | 326 | 312 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D L' F' L' B U' L' F' L     // normal, DR on F/B
(D2 R' U' R' B' R2 F' D B)  // inverse, DR on U/D
D L' F' L' B U' L' F' L     // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
L' B' L'            // normal EO on R/L
F2 U' B2 F' R2 U B  // then DR on U/D
(D2 R' U' R')       // inverse EO on R/L
(B' R2 F' D B)      // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
L' B' L'            // normal EO on R/L
F2 U' B2 F' R2 U B  // then DR on U/D
(D2 R' U' R')       // inverse EO on R/L
(B' R2 F' D B)      // then DR on U/D
```


</details>

### Scramble 97

```
D2 R2 U' F2 U' B2 F2 D' L2 D L2 U R2 U' L' U' L' D' B' D2 R D' B' D2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 32 | 30 | 36 |
| At most 5 | 380 | 306 | 396 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
R F D U' L2 U2 B2 R U       // normal, DR on F/B
(F' R2 B' U2 F' R' U2 L F)  // inverse, DR on U/D
B' L (U2 L' U' D B' R)      // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
B2 D2 L B           // normal EO on F/B
D' R D R2 U L       // then DR on U/D
(U L' B')           // inverse EO on F/B
(D R2 U R F2 D2 L)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
R B U' D R          // normal EO on R/L
F' L2 U F' D        // then DR on F/B
(U L' B')           // inverse EO on F/B
(D R2 U R F2 D2 L)  // then DR on U/D
```


</details>

### Scramble 98

```
D2 L2 B2 D' L2 U2 L2 F2 D' R2 U2 F2 U' R2 U2 L' U' L' F U' R B F2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 16 | 0 |
| At most 5 | 152 | 200 | 136 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 9 | 8 | 9 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
F2 B' R' U F' L U L       // normal, DR on U/D
(B2 L' D B L2 F2 L' U F)  // inverse, DR on U/D
F2 B' R' U F' L U L       // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
F2 U B R          // normal EO on R/L
F D' B D' B       // then DR on U/D
(U2 R2 U' R)      // inverse EO on R/L
(B2 U2 B U2 F U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 8; through an inverse EO: 10; with NISS EOs too: 8.

```
F2 B' R' U F'     // normal EO on F/B
L U L             // then DR on U/D
(U2 R2 U' R)      // inverse EO on R/L
(B2 U2 B U2 F U)  // then DR on F/B
```


</details>

### Scramble 99

```
U' R2 D F2 U2 L2 U' R2 U F2 L2 B2 F U2 R B' F' U' F' L2 R U'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 20 | 40 |
| At most 5 | 210 | 196 | 348 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
B2 U' F' D B' L D2 F U  // normal, DR on F/B
(F D F2 L2 D' R F B U)  // inverse, DR on R/L
B L' B' U D2 B R2 F U   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
D2 F B L'        // normal EO on R/L
U B F U2 D B     // then DR on U/D
(F U2 F2 R')     // inverse EO on R/L
(F' D2 B U D B)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
U' F B U2 R'     // normal EO on R/L
F' U2 F' D F     // then DR on U/D
(D' B2 R2 F L')  // inverse EO on R/L
(D' F D R2 B)    // then DR on U/D
```


</details>

### Scramble 100

```
B2 D2 R2 U2 L2 B2 R2 D' L2 B2 D' L2 U2 L' U2 B' R' D L2 U' L F2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 8, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 16 | 4 | 12 |
| At most 5 | 354 | 148 | 204 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
B2 L' F' R D' L' R U B2 D  // normal, DR on R/L
(F L' F U L2 B2 U2 R' B)   // inverse, DR on U/D
(F L' F U L2 B2 U2 R' B)   // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 12; with NISS EOs too: 10.

```
D' L' D2 F              // normal EO on F/B
U R D B2 R D            // then DR on R/L
(U' L D B)              // inverse EO on F/B
(U D' L' F2 U R' B2 L)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
F2 R2 F U D'      // normal EO on U/D
L B' D2 U2 L      // then DR on F/B
(D2 B R B2 L)     // inverse EO on R/L
(D R2 B F' U' F)  // then DR on U/D
```


</details>

### Scramble 101

```
F2 R2 U' F2 L2 F2 L2 U F2 D R2 D2 L2 U' R' U2 B D R' B F U B L2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 10, 10.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 8 |
| At most 5 | 0 | 4 | 76 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 11 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 10 | | | |
| NISS | 10 | | | |

For example:

```
B' L' B' U' F B D L' R2 U  // normal, DR on R/L
(B L' U B L2 F D B' D2 R)  // inverse, DR on U/D
L F R' D B2 L' B' U F D    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.

**EOs of at most 5 turns**, best DR: no normal EO; through an inverse EO: 11; with NISS EOs too: 11.

```
(B' L F2 D' R)     // inverse EO on R/L
(U' B U2 R2 U' F)  // then DR on U/D
```


</details>

### Scramble 102

```
L2 R2 D' R2 F2 U R2 D B2 U' F2 D' B' R D' U B2 R D R2 F' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 22 | 2 | 12 |
| At most 5 | 238 | 174 | 296 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 8 | 9 | 9 | 8 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
B U2 F2 R' U2 D' R U2 F  // normal, DR on R/L
(R2 U R' D U' L D' R)    // inverse, DR on F/B
(R2 U R' D U' L D' R)    // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
D2 F' L2 B            // normal EO on F/B
F2 U' L B2 D' R       // then DR on U/D
(L B2 U R)            // inverse EO on R/L
(U R2 B2 R2 U' L2 U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
B U2 F2 R' D'   // normal EO on U/D
U2 R U2 F       // then DR on R/L
(L U' B2 U R')  // inverse EO on R/L
(U L2 U F2 D)   // then DR on F/B
```


</details>

### Scramble 103

```
U2 L2 U' F2 D' L2 U2 F2 D B2 U B2 U' F2 U' F' U' L2 D' L' U L R2 F U'  // scramble
```

Bad edges on R/L, U/D, F/B: 2, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 22 | 32 |
| At most 5 | 78 | 240 | 344 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U F' L' U2 L D' B L' U        // normal, DR on R/L
(U R' D' R D' F' R2 U2 D2 F)  // inverse, DR on U/D
U F' L' U2 L D' B L' U        // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; through an inverse EO: 10; with NISS EOs too: 10.

```
(U R' D' R)         // inverse EO on R/L
(D' B' D2 R2 L2 B)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
U' B' R' U' R'      // normal EO on R/L
F' U' D' F2 B' U    // then DR on F/B
(U R' D' R)         // inverse EO on R/L
(D' B' D2 R2 L2 B)  // then DR on U/D
```


</details>

### Scramble 104

```
U L2 U2 L2 U' F2 D' R2 D R2 U2 B2 F L F' D2 F2 R U' L2 B' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 18 | 40 | 28 |
| At most 5 | 350 | 426 | 416 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 7 | | | |

For example:

```
U B2 R2 B D' L F2 R' D    // normal, DR on R/L
(R' F' D2 F D F' U R2 U)  // inverse, DR on R/L
R D (U L D F' D)          // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
U B2 R2 B         // normal EO on F/B
D' L F2 R' D      // then DR on R/L
(R' L U' L)       // inverse EO on R/L
(D' F L2 F2 U F)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
U B2 R2 B       // normal EO on F/B
D' L F2 R' D    // then DR on R/L
(D2 R U' F2 L)  // inverse EO on R/L
(U2 D2 L2 F D)  // then DR on F/B
```


</details>

### Scramble 105

```
U B2 D R2 U' L2 D2 L2 R2 U' F2 U B2 U' R' D' L' B U R B2 D U2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 34 | 6 | 12 |
| At most 5 | 328 | 118 | 200 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 9 | 10 | 9 | 9 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
U2 B L2 F2 U L U' R2 D      // normal, DR on R/L
(R2 F2 L' D' R2 U R2 U2 R)  // inverse, DR on F/B
U2 B D2 L' U (R2 L' D)      // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 11; with NISS EOs too: 9.

```
U2 B                 // normal EO on F/B
L2 F2 U L U' R2 D    // then DR on R/L
(L U D R)            // inverse EO on R/L
(U' F U' F D' R2 B)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
U2 B               // normal EO on F/B
L2 F2 U L U' R2 D  // then DR on R/L
(B2 D' R L' B)     // inverse EO on F/B
(U B2 R B2 R)      // then DR on U/D
```


</details>

### Scramble 106

```
D' B2 U2 F2 D L2 U B2 R2 U B' R2 U L F' D' R' U' L U  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 28 | 2 | 0 |
| At most 5 | 224 | 116 | 112 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 10 | | | |
| NISS | 8 | | | |

For example:

```
R B' L B' D2 U L2 F2 B U   // normal, DR on F/B
(D L2 U R L' B D F' R2 U)  // inverse, DR on F/B
R' L2 D' F2 D2 F L (F)     // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
R B' L              // normal EO on R/L
B' U D2 L2 F2 B U   // then DR on F/B
(F D2 R' B)         // inverse EO on F/B
(L2 R B2 U D L' D)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
R B' L             // normal EO on R/L
B' U D2 L2 F2 B U  // then DR on F/B
(U B2 D R L')      // inverse EO on R/L
(B D F' R2 U)      // then DR on F/B
```


</details>

### Scramble 107

```
B2 D' B2 R2 D' B2 U2 L2 U2 R2 U B2 F2 U' L' F L2 U' R F' D2 F' R U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 2, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 42 | 18 | 20 |
| At most 5 | 440 | 278 | 400 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F2 R' U F' L' U F' B' L    // normal, DR on F/B
(F' L F R2 B' U2 R' B2 L)  // inverse, DR on U/D
L2 B U F' D2 L' F' L U     // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
D R2 D              // normal EO on U/D
R F R B L' R' F     // then DR on R/L
(L U2 F R)          // inverse EO on R/L
(F2 D' F' U2 F' D)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
U L2 F2 L2 U'   // normal EO on U/D
B' D2 R U2 L    // then DR on F/B
(F' L F R2 B')  // inverse EO on F/B
(U2 R' B2 L)    // then DR on U/D
```


</details>

### Scramble 108

```
F2 D F2 U' B2 F2 R2 F2 D F2 U2 B2 D' R F' L' U' B D' R' D2 R U'  // scramble
```

Bad edges on R/L, U/D, F/B: 10, 8, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 8 | 0 |
| At most 5 | 64 | 88 | 72 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 10 | 10 |
| Inverse | 8 | 10 | 8 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
F2 D2 L U R D F B        // normal, DR on R/L
(R' F2 B D' L' U' R' F)  // inverse, DR on U/D
F2 D2 L U R D F B        // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; through an inverse EO: 9; with NISS EOs too: 9.

```
(F2 R' F' B)     // inverse EO on F/B
(D' B2 L' U' R)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
U2 R' U L' D     // normal EO on U/D
F' R' F2 R B     // then DR on R/L
(F2 R' F' B)     // inverse EO on F/B
(D' B2 L' U' R)  // then DR on U/D
```


</details>

### Scramble 109

```
B2 R2 D2 B2 D L2 R2 U' B2 U2 F2 U' F' R F L F2 D' L2 D B  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 20 | 28 | 4 |
| At most 5 | 312 | 354 | 144 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 8 | 10 | 10 | 8 |
| Best of the six | 8 | | | |
| NISS | 7 | | | |

For example:

```
F' D2 R2 B R2 U' L' B' R  // normal, DR on F/B
(F D F L2 U2 L D' R)      // inverse, DR on F/B
F L2 B R' F' D (D)        // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
F2 L' B' U         // normal EO on U/D
F R F L' R2 F      // then DR on R/L
(R2 L' B R)        // inverse EO on R/L
(L2 U B' U2 R2 U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
F2 L' B' U        // normal EO on U/D
F R F L' R2 F     // then DR on R/L
(L' F2 D' F' R')  // inverse EO on R/L
(B2 U' R2 U)      // then DR on F/B
```


</details>

### Scramble 110

```
L2 U F2 D L2 B2 U2 R2 B2 R2 B2 D' L2 U' R2 B' L' D2 R' F R2 U' L B L  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 16 | 16 |
| At most 5 | 26 | 92 | 276 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F' R' U' R2 F L F2 B D       // normal, DR on R/L
(D' R F' B' R F2 L B2 U' L)  // inverse, DR on U/D
F' R' U' R2 F L F2 B D       // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; through an inverse EO: 10; with NISS EOs too: 10.

```
(D' R F' B')      // inverse EO on F/B
(R F2 L B2 U' L)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 9.

```
U' F' R B2 D'     // normal EO on U/D
F' D2 R' D2 B' R  // then DR on F/B
(D' R F' B')      // inverse EO on F/B
(R F2 L B2 U' L)  // then DR on U/D
```


</details>

### Scramble 111

```
F2 D2 L2 U F2 L2 R2 D L2 F2 U F2 D' F2 U' R' D' F' L2 B2 R B F' D'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 12 | 0 | 12 |
| At most 5 | 204 | 108 | 180 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 9 | 9 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
D F B' R' B2 L2 F D R    // normal, DR on U/D
(D R U F B' R' F D2 F)   // inverse, DR on U/D
D2 B (U2 D' R' D' F' D)  // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; no inverse EO; with NISS EOs too: 10.

```
D2 B' U L        // normal EO on R/L
R2 D' F2 U L2 F  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
D2 R2 B' U L    // normal EO on R/L
D' B F' D B     // then DR on U/D
(U D F B' R)    // inverse EO on R/L
(U' B R2 F2 U)  // then DR on F/B
```


</details>

### Scramble 112

```
R2 D B2 D' B2 U2 R2 B2 L2 F2 D2 U F2 L' D F R2 D U2 B' R'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 24 | 18 | 16 |
| At most 5 | 252 | 360 | 348 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 10 | 8 | 9 |
| Inverse | 9 | 9 | 9 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
R B U2 D' R2 F' D' L     // normal, DR on U/D
(U F R F2 U R' U2 B2 D)  // inverse, DR on R/L
R B U2 D' R2 F' D' L     // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 8.

```
U F2 R               // normal EO on R/L
D' R2 B D' R2 F D    // then DR on F/B
(U F)                // inverse EO on F/B
(R F2 U R' U2 B2 D)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 8.

```
U F2 R             // normal EO on R/L
D' R2 B D' R2 F D  // then DR on F/B
(F L' U D' L)      // inverse EO on R/L
(F U2 F' D)        // then DR on F/B
```


</details>

### Scramble 113

```
B2 L2 F2 L2 D R2 U' B2 U2 B2 L2 U' R2 U L2 U F' U' R F' R2 U' L' B' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 12 | 8 | 28 |
| At most 5 | 116 | 124 | 212 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 10 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U B L U R2 F R' U F     // normal, DR on U/D
(R F' U' L D B L2 D F)  // inverse, DR on U/D
U B L U R2 F R' U F     // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
U R B L          // normal EO on R/L
F' U' L2 D R2 B  // then DR on U/D
(R F' U' L)      // inverse EO on R/L
(D B L2 D F)     // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
U R B L          // normal EO on R/L
F' U' L2 D R2 B  // then DR on U/D
(R F' U' L)      // inverse EO on R/L
(D B L2 D F)     // then DR on U/D
```


</details>

### Scramble 114

```
L2 F2 R2 U2 L2 F2 U' L2 D B2 R2 U B2 U2 L' F' U2 L U L2 R' U2 B D  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 8, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 0 | 4 |
| At most 5 | 72 | 96 | 84 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 10 | 11 | 11 | 10 |
| Best of the six | 10 | | | |
| NISS | 10 | | | |

For example:

```
B R B' L2 B L U F' B' D      // normal, DR on F/B
(D' B' U B' R L2 B L' F' U)  // inverse, DR on F/B
R F2 U' F2 L' D B L' U' F    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; no inverse EO; with NISS EOs too: 11.

```
L2 B R L           // normal EO on R/L
U B' D' B' D F' D  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
L2 B R L           // normal EO on R/L
U B' D' B' D F' D  // then DR on F/B
(F2 L2 B' U D)     // inverse EO on U/D
(B L' F' L2 B R)   // then DR on F/B
```


</details>

### Scramble 115

```
L2 U F2 U2 B2 U F2 L2 F2 U' F2 R2 F' L' D2 B2 U2 F' D' F D2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 20 | 22 | 0 |
| At most 5 | 202 | 218 | 192 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 10 |
| Inverse | 9 | 9 | 9 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
R' D' L2 D' B U' F D F      // normal, DR on R/L
(U2 F' L' F' D' U' F' B U)  // inverse, DR on F/B
R' D' L2 D' B U' F D F      // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
F' U F' R          // normal EO on R/L
B' D B' U' R2 B    // then DR on U/D
(U2 F' L')         // inverse EO on R/L
(F' U' D' F' B U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
L2 U L2 F2 R'      // normal EO on R/L
U F' D L2 B        // then DR on U/D
(U2 F' L')         // inverse EO on R/L
(F' U' D' F' B U)  // then DR on F/B
```


</details>

### Scramble 116

```
U R2 B2 D' B2 D F2 D L2 B2 D2 B2 U B' D L D2 B D2 F' U L' D'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 8 |
| At most 5 | 44 | 60 | 192 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 10 | | | |
| NISS | 8 | | | |

For example:

```
L' D L F2 B L B' D R2 F     // normal, DR on U/D
(F U' D R2 L' B U2 R B2 L)  // inverse, DR on U/D
U' L2 B2 L D' F' U (R)      // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 11.

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 8.

```
L U B D2 R         // normal EO on R/L
F' U2 L2 D B' U    // then DR on F/B
(U' R B2 D' L)     // inverse EO on R/L
(F' B' U F' B2 D)  // then DR on F/B
```


</details>

### Scramble 117

```
U B2 F2 D B2 F2 U' R2 D' U' R2 B2 U R' B2 D F' D' R2 B' U' F' U  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 14 | 22 | 8 |
| At most 5 | 204 | 230 | 212 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
L2 F' D' B' D F2 R' F2 U      // normal, DR on F/B
(B' R' U' F R U' D' F' U2 B)  // inverse, DR on R/L
L2 F' D' B' D F2 R' F2 U      // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
R F B' R           // normal EO on R/L
U B' D' L2 U R2 B  // then DR on U/D
(D' F2 D' L)       // inverse EO on R/L
(U2 B F U L2 D B)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
L2 F L2 B' R       // normal EO on R/L
D B' U' F U        // then DR on F/B
(U L F2 U' L)      // inverse EO on R/L
(U2 F' U' F2 D B)  // then DR on U/D
```


</details>

### Scramble 118

```
B2 U' B2 R2 B2 U B2 D' U2 B2 U F2 R' F L2 D' B D' B D'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 4, 2.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 46 | 90 | 44 |
| At most 5 | 676 | 872 | 504 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 10 | 8 | 9 |
| Inverse | 8 | 8 | 9 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
D B' D B' D L2 F' R     // normal, DR on U/D
(B D2 R' F2 L2 R' F D)  // inverse, DR on R/L
D B' D B' D L2 F' R     // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 9; with NISS EOs too: 9.

```
B R L2 D'        // normal EO on U/D
F2 B D2 U2 L     // then DR on F/B
(L F' R' D)      // inverse EO on U/D
(R' D2 B2 L2 F)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 9; with NISS EOs too: 9.

```
R2 B2 L2 U R     // normal EO on R/L
U B L2 B         // then DR on U/D
(L F' R' D)      // inverse EO on U/D
(R' D2 B2 L2 F)  // then DR on R/L
```


</details>

### Scramble 119

```
D L2 D U2 F2 D B2 U' L2 U L2 B2 R F D2 L' B' F' D' R' U2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 0 | 20 |
| At most 5 | 66 | 42 | 168 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
D2 B' L' D B' R' F R2 D    // normal, DR on R/L
(F B' R B2 U R2 L D2 B U)  // inverse, DR on F/B
D2 B' L' D B' R' F R2 D    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; no inverse EO; with NISS EOs too: 10.

```
D' L F2 U'      // normal EO on U/D
F' B' R' L B L  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
D2 R' F R' L'      // normal EO on R/L
F' R2 U D B        // then DR on U/D
(U L F' B' D)      // inverse EO on U/D
(B R' B' L' B' L)  // then DR on F/B
```


</details>

### Scramble 120

```
B2 D B2 D F2 L2 F2 R2 D L2 B2 D2 F2 U2 R' B2 F2 D U' B L' D' F2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 24 | 24 | 28 |
| At most 5 | 340 | 260 | 400 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
F' R' D2 F' U L' D' F' D   // normal, DR on F/B
(L2 U F2 U D2 L' U' L' F)  // inverse, DR on R/L
R' U B' D (L' D' B' L)     // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
R D2 L' F               // normal EO on F/B
L U R F2 L D            // then DR on R/L
(U2 B R)                // inverse EO on R/L
(B2 L2 B' U F R2 F' D)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 8.

```
R2 D' R F' U            // normal EO on U/D
F B2 R' U2 R            // then DR on F/B
(U2 B R)                // inverse EO on R/L
(B2 L2 B' U F R2 F' D)  // then DR on F/B
```


</details>

### Scramble 121

```
F2 U' B2 U2 B2 L2 U' L2 U F2 L2 R2 U' F2 U F' U' L F2 D L2 F L B' U2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 20 | 8 | 4 |
| At most 5 | 174 | 124 | 100 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
B R' L F' B2 R' U L' D' L   // normal, DR on U/D
(F' D' B' U2 R B2 U2 R' F)  // inverse, DR on U/D
(F' D' B' U2 R B2 U2 R' F)  // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
F' D B' R        // normal EO on R/L
B' L2 F U R2 D   // then DR on F/B
(L U' L2 D')     // inverse EO on U/D
(L F' R B2 L B)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
F' D B' R        // normal EO on R/L
B' L2 F U R2 D   // then DR on F/B
(L U' L2 D')     // inverse EO on U/D
(L F' R B2 L B)  // then DR on R/L
```


</details>

### Scramble 122

```
D2 F2 U B2 R2 D2 L2 D R2 U L2 R2 L' D R2 B F D B' F2 R2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 28 | 28 |
| At most 5 | 168 | 240 | 248 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
R2 U B R2 F' D2 U2 R D  // normal, DR on F/B
(D R F U L2 D' L D2 B)  // inverse, DR on R/L
D (F2 B D' U' B L D)    // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 9.

```
U' D F' R          // normal EO on R/L
U B D B U' F' U    // then DR on F/B
(D' R2 U' R)       // inverse EO on R/L
(D' F2 U2 B R2 U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
D F2 U' F' R'      // normal EO on R/L
F2 U2 B U D        // then DR on F/B
(D' R2 U' R)       // inverse EO on R/L
(D' F2 U2 B R2 U)  // then DR on F/B
```


</details>

### Scramble 123

```
D L2 F2 U B2 D' F2 R2 B2 F2 U2 R2 U' R2 U' B' D L' R2 F L D' F' U' L  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 34 | 10 | 8 |
| At most 5 | 554 | 288 | 272 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 7 | 9 | 9 | 7 |
| Best of the six | 7 | | | |
| NISS | 7 | | | |

For example:

```
D L B D' F2 U2 F B' D  // normal, DR on F/B
(R' D2 L2 B U' B' R)   // inverse, DR on F/B
(R' D2 L2 B U' B' R)   // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
D L                // normal EO on R/L
B D' F2 U2 F B' D  // then DR on F/B
(R2 F D2 R)        // inverse EO on R/L
(D' B R2 F B2 D)   // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 7; with NISS EOs too: 7.

```
D L                // normal EO on R/L
B D' F2 U2 F B' D  // then DR on F/B
(R' D2 L2 B U')    // inverse EO on U/D
(B' R)             // then DR on F/B
```


</details>

### Scramble 124

```
B2 U' R2 D L2 B2 R2 F2 U F2 U' R2 U L2 U' F' L2 R2 D2 F R' B L D R'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 22 | 4 | 12 |
| At most 5 | 322 | 162 | 180 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 9 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
L' B' L2 F D F2 R F2 U L  // normal, DR on U/D
(F' B U2 L' B R2 B2 D R)  // inverse, DR on U/D
(B' L D2 R' B D2 L F U)   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 11; with NISS EOs too: 10.

```
L' B' L2 F           // normal EO on F/B
D F2 R F2 U L        // then DR on U/D
(U' L B' R)          // inverse EO on R/L
(U2 D2 B D' L2 F U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
R D' L' B' R    // normal EO on R/L
B' L2 U2 D2 B   // then DR on U/D
(F' B U2 L' B)  // inverse EO on F/B
(R2 B2 D R)     // then DR on U/D
```


</details>

### Scramble 125

```
R2 F2 D2 L2 D2 R2 B2 U L2 R2 F2 R2 U2 B' L' D U2 L R2 D2 F D2  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 32 | 42 | 8 |
| At most 5 | 366 | 366 | 188 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 9 | 10 | 9 | 9 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
B2 L' F R2 L F L2 D R    // normal, DR on U/D
(B U F U F' L B' L2 D)   // inverse, DR on F/B
L2 B2 R' B2 R' F' R (L)  // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
U F D2 L            // normal EO on R/L
F2 D' F U' D' F     // then DR on U/D
(U D2 F2 R')        // inverse EO on R/L
(F' R2 U' F' R2 D)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
U F D2 L            // normal EO on R/L
F2 D' F U' D' F     // then DR on U/D
(U D2 F2 R')        // inverse EO on R/L
(F' R2 U' F' R2 D)  // then DR on F/B
```


</details>

### Scramble 126

```
D F2 U F2 L2 B2 U' R2 B2 R2 D L2 U' L' D B2 D R' B' U' R'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 8, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 26 | 24 | 24 |
| At most 5 | 306 | 482 | 244 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 9 | 8 | 10 |
| Inverse | 9 | 9 | 9 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
R U B R D' B2 D' L        // normal, DR on U/D
(B2 D R' U F B2 U' F2 L)  // inverse, DR on U/D
R U B R D' B2 D' L        // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 8; through an inverse EO: 10; with NISS EOs too: 8.

```
R U B             // normal EO on F/B
R D' B2 D' L      // then DR on U/D
(U R2 F R)        // inverse EO on R/L
(B' U2 B D2 B D)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 8; through an inverse EO: 9; with NISS EOs too: 8.

```
R U B          // normal EO on F/B
R D' B2 D' L   // then DR on U/D
(B2 D R' U F)  // inverse EO on F/B
(B2 U' F2 L)   // then DR on U/D
```


</details>

### Scramble 127

```
B2 D B2 D' L2 B2 F2 D R2 B2 F2 U2 B2 U' L' D2 U' B2 D' F L' D' B' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 12 | 8 |
| At most 5 | 126 | 154 | 252 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 11 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U B D L F' D B2 U D2 L     // normal, DR on U/D
(F' D' R2 L U' L2 F B' L)  // inverse, DR on F/B
(F' D' R2 L U' L2 F B' L)  // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 11.

```
D' L B2 R'            // normal EO on R/L
U' F' U' R2 F2 B U    // then DR on F/B
(R' L B' R)           // inverse EO on R/L
(F2 D' R2 F' R2 U B)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
U B D L F'       // normal EO on F/B
D B2 U D2 L      // then DR on U/D
(F' D' R2 L U')  // inverse EO on U/D
(L2 F B' L)      // then DR on F/B
```


</details>

### Scramble 128

```
U' B2 U' R2 D F2 U2 L2 B2 L2 D F2 D2 R2 F' U' R2 B' R' F2 L B F' U2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 2 | 4 |
| At most 5 | 136 | 102 | 100 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 10 | | | |
| NISS | 9 | | | |

For example:

```
L F L B R F' L2 F' U' B        // normal, DR on U/D
(R' L' F D2 B' R' L2 B2 U' L)  // inverse, DR on U/D
B' L F (U2 B2 U F2 B' D)       // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 11.

```
U R' F2 D            // normal EO on U/D
R U2 R' B' L F R     // then DR on F/B
(D' L2 F U)          // inverse EO on U/D
(B U2 F L' F' D2 R)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
L F L B R        // normal EO on R/L
F' L2 F' U' B    // then DR on U/D
(R' L' F D2 B')  // inverse EO on F/B
(R' L2 B2 U' L)  // then DR on U/D
```


</details>

### Scramble 129

```
B2 L2 D' B2 U' F2 U B2 F2 L2 F2 D2 B' D R U' L' B D U' R D' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 10, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 24 |
| At most 5 | 30 | 16 | 264 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 11 | 10 |
| Inverse | 10 | 10 | 11 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
B2 R' F U L' R2 F' R2 D    // normal, DR on R/L
(U' L2 R B U' L B2 D F U)  // inverse, DR on R/L
B2 R' F U L' R2 F' R2 D    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 10.

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
D F' U2 R' B'      // normal EO on F/B
U' R L' U' D R     // then DR on U/D
(F2 R U' B D)      // inverse EO on U/D
(R2 L D2 F2 B' L)  // then DR on F/B
```


</details>

### Scramble 130

```
D' F2 D' F2 R2 U' F2 U F2 U' B2 L2 U2 R B' D R' U L' D L' R' U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 28 | 22 | 12 |
| At most 5 | 252 | 194 | 232 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 8 | 8 | 9 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
F2 R' F' U2 B2 D' R F2 U  // normal, DR on R/L
(L U B2 D F2 L' U2 B)     // inverse, DR on R/L
(L R2 U B2 D' L' U2 B)    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 8; with NISS EOs too: 8.

```
F2 R' F'         // normal EO on F/B
U2 B2 D' R F2 U  // then DR on R/L
(L U B2 D)       // inverse EO on U/D
(F2 L' U2 B)     // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 8; with NISS EOs too: 8.

```
F2 R' F'         // normal EO on F/B
U2 B2 D' R F2 U  // then DR on R/L
(R2 L U B2 D')   // inverse EO on U/D
(L' U2 B)        // then DR on R/L
```


</details>

### Scramble 131

```
B2 D' R2 D2 B2 D F2 U2 R2 U' B2 R2 U2 L' U' R' F' D' F2 L B' D2 L  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 4 | 8 |
| At most 5 | 0 | 108 | 184 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
B U B L2 R U R' F2 R F    // normal, DR on R/L
(L F R' L2 F D' L' U2 B)  // inverse, DR on U/D
(L F R' L2 F D' L' U2 B)  // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: no normal EO; through an inverse EO: 10; with NISS EOs too: 10.

```
(F' L U' R)        // inverse EO on R/L
(D' B U2 B' L2 D)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: no normal EO; through an inverse EO: 10; with NISS EOs too: 9.

```
(F' L U' R)        // inverse EO on R/L
(D' B U2 B' L2 D)  // then DR on F/B
```


</details>

### Scramble 132

```
B2 D' R2 U R2 U R2 B2 U2 L2 U R2 U' R2 U' B' D L2 D' L F L D' L  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 6 | 4 | 32 |
| At most 5 | 178 | 184 | 388 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 9 |
| Inverse | 9 | 9 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F' B' U' F' L U R' D R     // normal, DR on U/D
(B R' F' D' B2 U' F2 B R)  // inverse, DR on U/D
L' D L' F' L' D L2 D' B    // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 11; with NISS EOs too: 9.

```
F' B' U' F'         // normal EO on F/B
L U R' D R          // then DR on U/D
(R2 L' F D)         // inverse EO on U/D
(R' F B' L F2 B L)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
L' D L' F' L'    // normal EO on R/L
D L2 D' B        // then DR on U/D
(U' R L' D L')   // inverse EO on R/L
(B' R2 U' D2 B)  // then DR on U/D
```


</details>

### Scramble 133

```
F2 U R2 B2 R2 F2 D' L2 U' L2 U' R2 L' B' R' U' L' F' U2 B2 R U2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 4 | 40 |
| At most 5 | 116 | 166 | 408 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 10 |
| Inverse | 8 | 8 | 10 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
U2 B U' L' R B U' F U   // normal, DR on R/L
(D F B2 L' B' D' R' D)  // inverse, DR on R/L
(D F B2 L' B' D' R' D)  // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; through an inverse EO: 9; with NISS EOs too: 9.

```
(U D L U')      // inverse EO on U/D
(L' B2 F L' B)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 8; with NISS EOs too: 8.

```
R' L U B R       // normal EO on R/L
F' D' B R2 L2 D  // then DR on F/B
(D F B2 L' B')   // inverse EO on F/B
(D' R' D)        // then DR on R/L
```


</details>

### Scramble 134

```
D R2 B2 U' L2 U B2 U' R2 D R2 B2 F2 L' F D' B U L' R2 F' R' D2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 10, 10, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 0 |
| At most 5 | 24 | 32 | 8 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 11 | 10 |
| Inverse | 9 | 9 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
B' R' U L' F D' L' B' U   // normal, DR on R/L
(D2 L' D R' F B U' L' D)  // inverse, DR on R/L
B' R' U L' F D' L' B' U   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; no EO at all.

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 12; with NISS EOs too: 11.

```
R' U F' D' B       // normal EO on F/B
R U' D L U L       // then DR on U/D
(D' R B L F)       // inverse EO on F/B
(R' D R D' L D L)  // then DR on U/D
```


</details>

### Scramble 135

```
U2 R2 U L2 F2 U B2 U' B2 U L2 D R2 U2 R' U B' L U L' B2 F L' D2  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 4, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 6 | 14 | 12 |
| At most 5 | 172 | 268 | 156 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F2 D' L B2 R' F' U' L B    // normal, DR on R/L
(F2 D' L' F B' L R' B2 U)  // inverse, DR on R/L
F2 D' L B2 R' F' U' L B    // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
D2 R2 B D'          // normal EO on U/D
L' U2 F2 D2 F B2 L  // then DR on F/B
(B' R' F L')        // inverse EO on R/L
(D2 B' U F' D' F)   // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 9; with NISS EOs too: 9.

```
D2 R2 B D'          // normal EO on U/D
L' U2 F2 D2 F B2 L  // then DR on F/B
(F2 D' L' F B')     // inverse EO on F/B
(L R' B2 U)         // then DR on R/L
```


</details>

### Scramble 136

```
B2 L2 D L2 F2 U L2 U2 B2 D2 U' F' U R' D B L' R2 B F U'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 4, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 32 | 28 | 16 |
| At most 5 | 384 | 430 | 284 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F L' B R' D U2 L2 B D       // normal, DR on F/B
(R' F' R D R' B' L R D2 B)  // inverse, DR on R/L
F L' B R' D U2 L2 B D       // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
F L' B R'         // normal EO on R/L
U2 D L2 B D       // then DR on F/B
(R' F' R D)       // inverse EO on U/D
(R' B' L R D2 B)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
F L' B R'         // normal EO on R/L
U2 D L2 B D       // then DR on F/B
(R' F' R D)       // inverse EO on U/D
(R' B' L R D2 B)  // then DR on R/L
```


</details>

### Scramble 137

```
L2 D B2 L2 U L2 U2 F2 L2 B2 L2 R2 B' L' R2 F L' F' U B' L  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 28 | 24 | 44 |
| At most 5 | 356 | 280 | 408 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 8 | | | |

For example:

```
U' B U' B2 D L F2 U2 F    // normal, DR on R/L
(B' U B2 R' U D' F' R U)  // inverse, DR on R/L
U (D2 F L U F R2 D)       // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
B' D B L             // normal EO on R/L
F B U D2 F' U        // then DR on F/B
(D2 F L)             // inverse EO on R/L
(U2 L2 D R2 F' B U)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
U' B U' B2 D     // normal EO on U/D
L B2 D2 F        // then DR on R/L
(D B' U' F' L')  // inverse EO on R/L
(D F2 L2 F' D)   // then DR on F/B
```


</details>

### Scramble 138

```
B2 F2 L2 F2 D2 F2 U L2 U F2 R2 U F2 R' F' U' B' L U F2 U' B  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 12 | 16 | 28 |
| At most 5 | 142 | 256 | 332 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 10 |
| Inverse | 9 | 9 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
L2 D2 L' F' R' F B2 D' B   // normal, DR on R/L
(F L2 F' B2 R' D L D2 B)   // inverse, DR on R/L
L2 D2 L' F' R' F B2 D' B   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
D2 L' F2 U          // normal EO on U/D
B' R2 U2 L' B R     // then DR on F/B
(R U2 B' U)         // inverse EO on U/D
(B2 F' U2 L2 R' F)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 9.

```
D2 L' F2 U          // normal EO on U/D
B' R2 U2 L' B R     // then DR on F/B
(R U2 B' U)         // inverse EO on U/D
(B2 F' U2 L2 R' F)  // then DR on R/L
```


</details>

### Scramble 139

```
D U2 B2 U' L2 U B2 U' B2 D' R2 U L' F' R' U' L' R F D2 L U'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 2 | 4 | 8 |
| At most 5 | 84 | 90 | 240 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 11 | 10 | 10 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U2 D2 F D2 R D' B2 R' U' F  // normal, DR on U/D
(R F U' F2 R2 L U F2 L)     // inverse, DR on F/B
(R F U' F2 R2 L U F2 L)     // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 12; with NISS EOs too: 10.

```
R' U D' F               // normal EO on F/B
U D2 F2 B2 L2 R' U      // then DR on R/L
(B' U D' R)             // inverse EO on R/L
(B U D' R2 B2 F2 D' F)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
F R2 F D' L'       // normal EO on R/L
F' U2 D' F L2 U    // then DR on F/B
(B U B D' R)       // inverse EO on R/L
(D2 F L2 U' L2 F)  // then DR on U/D
```


</details>

### Scramble 140

```
F2 U' R2 F2 D' R2 D' R2 B2 D' L2 U B2 R2 U L' B' F D L' U' R2 B L2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 4, 10.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 24 | 0 | 8 |
| At most 5 | 208 | 96 | 152 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 7 | 7 | 10 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 7 | | | |
| NISS | 7 | | | |

For example:

```
R B D' F B R B              // normal, DR on R/L
(B D F L2 D' L' B R' D2 B)  // inverse, DR on R/L
R B D' F B R B              // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 7; no inverse EO; with NISS EOs too: 7.

```
R B D'   // normal EO on U/D
B F R B  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 7; through an inverse EO: 10; with NISS EOs too: 7.

```
R B D'          // normal EO on U/D
B F R B         // then DR on R/L
(B D F L2 D')   // inverse EO on U/D
(L' B R' D2 B)  // then DR on R/L
```


</details>

### Scramble 141

```
B2 D' L2 U F2 D L2 U2 F2 D2 B2 R D' F R2 U B L U' L  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 2 | 0 | 4 |
| At most 5 | 66 | 90 | 148 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 9 | 9 |
| Inverse | 8 | 10 | 8 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
L' F' L2 U L' B' U' R' D  // normal, DR on R/L
(L U' F B D R' D F)       // inverse, DR on U/D
(L U' F B D R' D F)       // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 12; no inverse EO; with NISS EOs too: 12.

```
B' R2 L' F           // normal EO on F/B
L' D2 R U' L D R' D  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
U2 F B L' F      // normal EO on F/B
L' D L U D       // then DR on R/L
(L' U' B D2 R')  // inverse EO on R/L
(D B R2 U' B)    // then DR on U/D
```


</details>

### Scramble 142

```
F2 U R2 U R2 D' F2 U B2 D B2 L2 D' L2 R' U2 F' D' F' R2 F' D2 F2 D'  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 4, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 18 | 16 |
| At most 5 | 156 | 254 | 288 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 10 | 10 |
| Inverse | 9 | 10 | 10 | 9 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
B L2 R U' R' B R F       // normal, DR on R/L
(F' R D2 U' R D' U F D)  // inverse, DR on F/B
F' R F D' F2 D2 F' D     // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 8; through an inverse EO: 10; with NISS EOs too: 8.

```
B R L2 U'         // normal EO on U/D
R' B R F          // then DR on R/L
(F2 B2 U L)       // inverse EO on R/L
(D2 F U' F2 B D)  // then DR on F/B
```

**EOs of at most 5 turns**, best DR: through a normal EO: 8; through an inverse EO: 9; with NISS EOs too: 8.

```
B R L2 U'       // normal EO on U/D
R' B R F        // then DR on R/L
(F' R U' D2 R)  // inverse EO on R/L
(U D' F D)      // then DR on F/B
```


</details>

### Scramble 143

```
B2 L2 F2 U L2 D2 B2 L2 D R2 D B2 F' R2 U B D2 L' F D2 B  // scramble
```

Bad edges on R/L, U/D, F/B: 4, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 16 | 40 | 12 |
| At most 5 | 188 | 462 | 200 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 9 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
B' U F B D' B2 L F           // normal, DR on R/L
(B' R U' D' B2 L2 F L2 D B)  // inverse, DR on U/D
B' U F B D' B2 L F           // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 9; through an inverse EO: 10; with NISS EOs too: 9.

```
B' D2 F' L         // normal EO on R/L
D2 B' U' R2 F      // then DR on U/D
(U' B' U2 R)       // inverse EO on R/L
(B2 D' B' F D' F)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 8; through an inverse EO: 10; with NISS EOs too: 8.

```
B' U F B D'        // normal EO on U/D
B2 L F             // then DR on R/L
(U' B' U2 R)       // inverse EO on R/L
(B2 D' B' F D' F)  // then DR on U/D
```


</details>

### Scramble 144

```
L2 U F2 D R2 B2 L2 F2 U' B2 U2 L2 B2 F' D' B2 R' D U' F' R B2 U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 8, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 18 | 12 |
| At most 5 | 140 | 276 | 180 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 8 | 8 | 10 | 10 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
L U F L D' B2 L B        // normal, DR on R/L
(F R D2 R2 U2 B' U R L)  // inverse, DR on U/D
L U F L D' B2 L B        // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
F2 L U D'              // normal EO on U/D
F L U2 F' L' F         // then DR on R/L
(R L2 F')              // inverse EO on F/B
(U' F2 L2 F2 L2 R' D)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 8; through an inverse EO: 10; with NISS EOs too: 8.

```
L U F L D'             // normal EO on U/D
B2 L B                 // then DR on R/L
(R L2 F')              // inverse EO on F/B
(U' F2 L2 F2 L2 R' D)  // then DR on R/L
```


</details>

### Scramble 145

```
B2 L2 B2 D' B2 U L2 U2 F2 U' B2 U' F2 R2 L' D F D U B U' R2 D L'  // scramble
```

Bad edges on R/L, U/D, F/B: 2, 10, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 24 | 38 | 0 |
| At most 5 | 280 | 396 | 152 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 10 | | | |
| NISS | 9 | | | |

For example:

```
L' F2 D' L U B D F B2 D     // normal, DR on R/L
(R U' R D R2 B' U2 B2 U F)  // inverse, DR on U/D
L' D B R2 U D B L (F)       // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
D2 L U L          // normal EO on R/L
F D F' B' U B2 U  // then DR on F/B
(U R U2 R)        // inverse EO on R/L
(U F2 D B U F)    // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
U' D2 R B2 R'    // normal EO on R/L
D' R2 F' U' D B  // then DR on U/D
(U R U2 R)       // inverse EO on R/L
(U F2 D B U F)   // then DR on U/D
```


</details>

### Scramble 146

```
F2 R2 D' L2 B2 D2 F2 U R2 F2 U L2 R2 U2 B' U F' L' F L R D U' L  // scramble
```

Bad edges on R/L, U/D, F/B: 10, 6, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 0 | 0 | 16 |
| At most 5 | 38 | 16 | 208 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 9 | 10 | 9 |
| Inverse | 9 | 9 | 10 | 11 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
L B' L2 R' D L2 U F U     // normal, DR on R/L
(L U R' D' R' F B' D' B)  // inverse, DR on R/L
L B' L2 R' D L2 U F U     // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: no normal EO; no inverse EO; with NISS EOs too: 10.

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 10.

```
R' U L' B D        // normal EO on U/D
L' B2 R' D2 F L    // then DR on F/B
(L U' B' U2 F)     // inverse EO on F/B
(R2 F2 R' F2 R D)  // then DR on R/L
```


</details>

### Scramble 147

```
D L2 U2 L2 B2 D2 F2 U F2 U L2 U' B' L F L2 F2 L2 U R F U'  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 8.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 4 | 4 | 4 |
| At most 5 | 86 | 128 | 128 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 10 | 9 |
| Inverse | 10 | 10 | 10 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
F' B2 L' F2 D B' L2 U L     // normal, DR on F/B
(R' L U' F R' L2 F' D F U)  // inverse, DR on F/B
F' B2 L' F2 D B' L2 U L     // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 12; through an inverse EO: 12; with NISS EOs too: 11.

```
L U2 F' R              // normal EO on R/L
B U2 D' L2 F L2 D' F   // then DR on U/D
(L' D2 F R)            // inverse EO on R/L
(U2 F U B2 R2 B' D F)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
D' F' D B U'    // normal EO on U/D
F' L U2 B' R    // then DR on F/B
(R' L U' F R')  // inverse EO on R/L
(L2 F' D F U)   // then DR on F/B
```


</details>

### Scramble 148

```
R2 F2 L2 D' B2 D F2 D2 R2 D R2 F2 U2 B2 U2 R' U' L2 B U L' U F2 U2  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 6, 4.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 14 | 22 | 8 |
| At most 5 | 200 | 228 | 232 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 10 |
| Inverse | 9 | 10 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
U2 F2 U' L U' B' L2 U R   // normal, DR on U/D
(R2 L D L' B' R U2 D2 R)  // inverse, DR on U/D
U2 F2 U' L U' B' L2 U R   // NISS, DR on U/D
```

**EOs of at most 4 turns**, best DR: through a normal EO: 10; through an inverse EO: 10; with NISS EOs too: 10.

```
F2 U2 L B'       // normal EO on F/B
F2 U2 L' U R L   // then DR on U/D
(R2 D F2 B)      // inverse EO on F/B
(R U' B2 R U L)  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 10; through an inverse EO: 9; with NISS EOs too: 9.

```
U F2 U2 L B'    // normal EO on F/B
L B2 R' D L     // then DR on U/D
(R2 L D L' B')  // inverse EO on F/B
(R U2 D2 R)     // then DR on U/D
```


</details>

### Scramble 149

```
D R2 B2 U L2 U2 L2 D' B2 U2 L' B' D' R B2 U' B F' R2 D'  // scramble
```

Bad edges on R/L, U/D, F/B: 8, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 12 | 12 | 8 |
| At most 5 | 180 | 132 | 196 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 10 | 10 | 10 | 10 |
| Inverse | 9 | 9 | 9 | 10 |
| Best of the six | 9 | | | |
| NISS | 9 | | | |

For example:

```
B R D' L' B U B U2 L' F  // normal, DR on R/L
(F R2 D R B U' F' L' B)  // inverse, DR on R/L
(U2 L B' L' F U D R F)   // NISS, DR on R/L
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 10.

```
U2 L B' R          // normal EO on R/L
B' U D' F B R2 U   // then DR on F/B
(F' D B U)         // inverse EO on U/D
(D2 L D2 B' U2 F)  // then DR on R/L
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 10; with NISS EOs too: 9.

```
U2 L B' R         // normal EO on R/L
B' U D' F B R2 U  // then DR on F/B
(U2 F D B U)      // inverse EO on U/D
(F B R' B' L)     // then DR on F/B
```


</details>

### Scramble 150

```
R2 D2 B2 R2 U' F2 D L2 U' R2 F2 U' B2 U' L' F' R' F2 D' B' U L F  // scramble
```

Bad edges on R/L, U/D, F/B: 6, 8, 6.

How many EOs the scramble has on all three axes, by length, on each side:

| Number of EOs | Normal | Inverse | NISS, turns on both sides |
|---|---:|---:|---:|
| At most 4 turns | 8 | 0 | 0 |
| At most 5 | 104 | 28 | 64 |

<details><summary>Shortest DRs and the best DRs through short EOs</summary>

Fewest turns to DR from the scramble: the best axis, then each axis.

| Shortest DR | Best axis, turns | R/L, turns | U/D, turns | F/B, turns |
|---|---:|---:|---:|---:|
| Normal side | 9 | 10 | 9 | 10 |
| Inverse | 8 | 10 | 10 | 8 |
| Best of the six | 8 | | | |
| NISS | 8 | | | |

For example:

```
F' L' U' B D F2 R F L    // normal, DR on U/D
(D' L' F' U' R D' F' L)  // inverse, DR on F/B
(R F L2 B2 L' D U' L)    // NISS, DR on F/B
```

**EOs of at most 4 turns**, best DR: through a normal EO: 11; no inverse EO; with NISS EOs too: 11.

```
F' U F B          // normal EO on F/B
U R2 L' U L D' R  // then DR on U/D
```

**EOs of at most 5 turns**, best DR: through a normal EO: 11; through an inverse EO: 11; with NISS EOs too: 11.

```
R' L F U D        // normal EO on U/D
L F U2 F2 B2 L    // then DR on F/B
(R' F2 U' D L')   // inverse EO on R/L
(D' R2 U B D2 F)  // then DR on U/D
```


</details>

## Part 2. EO to DR, 60 states by case

Each is a scramble from the study's sample and one of its EOs of at most 4 turns. The cases are the 16 most common after an EO, most common first, then four rarer ones (2c4e, 4c2e, 3c2e and 8c8e). The line on top gives the case on each DR axis; the table gives the turns to DR each way, all with the EO kept unless the row says otherwise.

### Case 6c6e: examples 1–3

**6c6e, example 1.** After the EO the case is 6c6e for DR on F/B and 5c6e for DR on R/L.

```
L2 U2 F2 U R2 U' B2 D B2 U B2 U' B2 U R' U R2 F' L' F2 L2 B' R U'  // scramble
U R' B2 D                                                          // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (6c6e), EO kept | 8 | `F' B' R' F' U2 R2 F2 R` |
| DR on F/B on the inverse (6c6e there), EO kept | 7 | `(B U2 L' F' R F2 R)` |
| DR on F/B, last EO turn the other way (`U R' B2 D'`) | 7 | `B' L' F D2 R2 B R` |
| DR on R/L (5c6e), EO kept | 7 | `B L' U2 L' D2 L B` |
| DR on R/L on the inverse (5c6e there), EO kept | 8 | `(L U2 L B' D2 F' R B)` |
| DR on R/L, last EO turn the other way (`U R' B2 D'`) | 8 | `D2 B L' U2 L' D2 L B` |

</details>

**6c6e, example 2.** After the EO the case is 6c6e for DR on R/L and 4c6e for DR on F/B.

```
U2 F2 U' F2 U L2 B2 D B2 D' L2 R2 B2 U' R' U F' R D L D B' F' U'  // scramble
U R2 L D                                                          // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (6c6e), EO kept | 7 | `F' U2 L F U2 R' B` |
| DR on R/L on the inverse (6c6e there), EO kept | 8 | `(R2 D2 F L' B2 R' D2 F)` |
| DR on R/L, last EO turn the other way (`U R2 L D'`) | 8 | `L B D2 B F D2 R F` |
| DR on F/B (4c6e), EO kept | 6 | `B' U2 F' R U2 L` |
| DR on F/B on the inverse (4c6e there), EO kept | 8 | `(F R2 F' R2 B' R' D2 L)` |
| DR on F/B, last EO turn the other way (`U R2 L D'`) | 7 | `F' B L B R2 D2 R` |

</details>

**6c6e, example 3.** After the EO the case is 6c6e for DR on U/D and 6c4e for DR on F/B.

```
B2 F2 D' B2 F2 L2 D' B2 D' F2 U F2 U' F2 B' F' R' D' R2 U2 L' F U  // scramble
L U F' R                                                           // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (6c6e), EO kept | 7 | `B U2 D' B' R2 D' B` |
| DR on U/D on the inverse (6c6e there), EO kept | 8 | `(F2 U' F D L2 B2 U' B)` |
| DR on U/D, last EO turn the other way (`L U F' R'`) | 7 | `B U2 D' B' R2 D' B` |
| DR on F/B (6c4e), EO kept | 7 | `B' D' F' U2 L2 F' U` |
| DR on F/B on the inverse (6c4e there), EO kept | 8 | `(F2 U F' R2 B R2 F' U)` |
| DR on F/B, last EO turn the other way (`L U F' R'`) | 8 | `F U F2 U F2 L2 B U` |

</details>

### Case 5c6e: examples 1–3

**5c6e, example 1.** After the EO the case is 5c6e for DR on R/L and 7c4e for DR on U/D.

```
U B2 R2 U' R2 U B2 D' F2 R2 U L2 F2 L' U' R' F2 D F' R B R U'  // scramble
U B R F                                                        // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (5c6e), EO kept | 8 | `R2 F2 R U L2 D' R D` |
| DR on R/L on the inverse (5c6e there), EO kept | 6 | `(U L' D2 F2 L D)` |
| DR on R/L, last EO turn the other way (`U B R F'`) | 7 | `U' L2 R D2 F2 L' U` |
| DR on U/D (7c4e), EO kept | 8 | `U' R2 B2 U2 L' U2 D' L` |
| DR on U/D on the inverse (7c4e there), EO kept | 9 | `(U L D2 R U' R F2 B2 R)` |
| DR on U/D, last EO turn the other way (`U B R F'`) | 8 | `R U' R' B2 U2 R' F2 R` |

</details>

**5c6e, example 2.** After the EO the case is 5c6e for DR on R/L and 4c6e for DR on F/B.

```
U2 F2 U2 F2 L2 U' B2 D' F2 U' R2 U2 F2 R2 U2 R' U2 F' L2 D' L R D' F' L2 U'  // scramble
U D2 L D                                                                     // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (5c6e), EO kept | 8 | `F L D2 L F' L R' F` |
| DR on R/L on the inverse (5c6e there), EO kept | 8 | `(L2 B' R U2 B L R B)` |
| DR on R/L, last EO turn the other way (`U D2 L D'`) | 8 | `L R F L' U2 F2 L' B` |
| DR on F/B (4c6e), EO kept | 8 | `U2 B' D2 F' D2 R' F2 L` |
| DR on F/B on the inverse (4c6e there), EO kept | 9 | `(F R B' R U2 R F2 B' L)` |
| DR on F/B, last EO turn the other way (`U D2 L D'`) | 9 | `F R2 F' R F' D2 R2 F2 R` |

</details>

**5c6e, example 3.** After the EO the case is 5c6e for DR on U/D and 5c8e for DR on F/B.

```
D' L2 R2 B2 D' F2 L2 U B2 L2 D2 L2 U' L' F D2 U' F' D2 L2 B' D' U'  // scramble
L' B U L'                                                           // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (5c6e), EO kept | 9 | `U F2 R2 U B2 F' R2 D B` |
| DR on U/D on the inverse (5c6e there), EO kept | 8 | `(U' B U B2 D' B L2 F)` |
| DR on U/D, last EO turn the other way (`L' B U L`) | 8 | `B' F2 U R2 F U D F` |
| DR on F/B (5c8e), EO kept | 8 | `F2 U2 D' L2 U' F B' D` |
| DR on F/B on the inverse (5c8e there), EO kept | 8 | `(L2 F' U L2 D F' B U)` |
| DR on F/B, last EO turn the other way (`L' B U L`) | 9 | `U B R2 F U' F R2 F2 D` |

</details>

### Case 6c4e: examples 1–3

**6c4e, example 1.** After the EO the case is 6c4e for DR on R/L and 7c6e for DR on F/B.

```
F2 R2 D B2 U R2 B2 F2 D2 F2 D' F2 U' B2 U2 L' D' B2 U2 L2 R' B' R  // scramble
U' D R' U                                                          // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (6c4e), EO kept | 9 | `L2 B L B' U2 D2 B2 R F` |
| DR on R/L on the inverse (6c4e there), EO kept | 8 | `(R F U2 L R' D2 R B)` |
| DR on R/L, last EO turn the other way (`U' D R' U'`) | 8 | `F R U2 D2 B R U2 F` |
| DR on F/B (7c6e), EO kept | 8 | `F B R' L2 B' D2 B2 L` |
| DR on F/B on the inverse (7c6e there), EO kept | 6 | `(R' L B' U2 B L)` |
| DR on F/B, last EO turn the other way (`U' D R' U'`) | 8 | `F B R' D2 U2 R2 F R` |

</details>

**6c4e, example 2.** After the EO the case is 6c4e for DR on R/L and 5c6e for DR on U/D.

```
F2 L2 F2 L2 U2 L2 D L2 D L2 F2 D2 L' U' F2 U' F' D R' B2 F  // scramble
F2 D' L2 F                                                  // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (6c4e), EO kept | 8 | `U R' U F2 U B2 L D` |
| DR on R/L on the inverse (6c4e there), EO kept | 8 | `(R2 U D L2 U' L' R D)` |
| DR on R/L, last EO turn the other way (`F2 D' L2 F'`) | 9 | `L U' D R B2 U F2 R' D` |
| DR on U/D (5c6e), EO kept | 8 | `U2 R' F2 U' L' F2 D R` |
| DR on U/D on the inverse (5c6e there), EO kept | 7 | `(L2 D2 R D F2 U L)` |
| DR on U/D, last EO turn the other way (`F2 D' L2 F'`) | 7 | `R U D' R L U' R` |

</details>

**6c4e, example 3.** After the EO the case is 6c4e for DR on U/D and 5c8e for DR on F/B.

```
L2 B2 D' R2 F2 U' B2 D B2 U F2 L2 F2 D' U' R' B L' D' B U B U2 R U'  // scramble
U2 D' R L                                                            // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (6c4e), EO kept | 9 | `D F U R2 D L2 B2 U2 B` |
| DR on U/D on the inverse (6c4e there), EO kept | 8 | `(U' D' B' D B2 D R2 F)` |
| DR on U/D, last EO turn the other way (`U2 D' R L'`) | 9 | `U2 F R2 U2 D' B F U F` |
| DR on F/B (5c8e), EO kept | 8 | `F D' R2 U' F' D B' D` |
| DR on F/B on the inverse (5c8e there), EO kept | 8 | `(U' L2 F2 B' U' D' F D)` |
| DR on F/B, last EO turn the other way (`U2 D' R L'`) | 7 | `U' F' B2 D F2 B' D` |

</details>

### Case 4c6e: examples 1–3

**4c6e, example 1.** After the EO the case is 4c6e for DR on U/D and 2c8e for DR on F/B.

```
U2 B2 U' R2 U F2 U2 R2 B2 F2 R2 B2 U2 L' B D' U' L' R' F' L2 F'  // scramble
D L B R                                                          // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (4c6e), EO kept | 7 | `B U' L2 D' B2 R2 F` |
| DR on U/D on the inverse (4c6e there), EO kept | 9 | `(D B2 D2 R2 B' L2 B2 D F)` |
| DR on U/D, last EO turn the other way (`D L B R'`) | 7 | `U R2 L2 D2 B R2 F` |
| DR on F/B (2c8e), EO kept | 9 | `U' F U F' U' B' U B2 D` |
| DR on F/B on the inverse (2c8e there), EO kept | 9 | `(F D B' U' R2 D L2 B D)` |
| DR on F/B, last EO turn the other way (`D L B R'`) | 9 | `U F2 U F' B' U F' B2 D` |

</details>

**4c6e, example 2.** After the EO the case is 4c6e for DR on U/D and 4c6e for DR on F/B.

```
U B2 U' B2 U F2 D' F2 U' F2 D2 L2 U' L2 B' U L' B D F' D R' U  // scramble
D B' U' R'                                                     // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (4c6e), EO kept | 7 | `B' F2 U F U2 D B` |
| DR on U/D on the inverse (4c6e there), EO kept | 7 | `(U' D2 F2 U' B' D2 F)` |
| DR on U/D, last EO turn the other way (`D B' U' R`) | 6 | `B' U' B' U D' F` |
| DR on F/B (4c6e), EO kept | 6 | `U L2 B U2 B' D` |
| DR on F/B on the inverse (4c6e there), EO kept | 8 | `(F' D2 B U L2 F2 B2 U)` |
| DR on F/B, last EO turn the other way (`D B' U' R`) | 6 | `U L2 B U2 B' D` |

</details>

**4c6e, example 3.** After the EO the case is 4c6e for DR on U/D and 6c6e for DR on F/B.

```
F2 R2 B2 D F2 R2 D' B2 U F2 L2 U' F' U' B' L2 F' D R' F' R U'  // scramble
U R' F R'                                                      // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (4c6e), EO kept | 7 | `R2 D' B D2 F U F` |
| DR on U/D on the inverse (4c6e there), EO kept | 8 | `(D L2 B' D' L2 B2 D2 B)` |
| DR on U/D, last EO turn the other way (`U R' F R`) | 6 | `D' B D2 F U F` |
| DR on F/B (6c6e), EO kept | 8 | `F U' B U D B L2 U` |
| DR on F/B on the inverse (6c6e there), EO kept | 8 | `(F' R2 U D R2 L2 B' D)` |
| DR on F/B, last EO turn the other way (`U R' F R`) | 8 | `F' D2 B U' D L2 B U` |

</details>

### Case 5c4e: examples 1–3

**5c4e, example 1.** After the EO the case is 5c4e for DR on F/B and 6c4e for DR on R/L.

```
B2 U R2 U' F2 D2 R2 B2 U' F2 D' F2 U' F2 U B' R D L D R B F2 D2  // scramble
U' D R U                                                         // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (5c4e), EO kept | 8 | `L2 F D2 U2 L' F D2 L` |
| DR on F/B on the inverse (5c4e there), EO kept | 9 | `(F R F2 R2 L' U2 F2 B' L)` |
| DR on F/B, last EO turn the other way (`U' D R U'`) | 8 | `F2 R2 B L U2 L' F R` |
| DR on R/L (6c4e), EO kept | 8 | `R' F2 R' B F2 L' R B` |
| DR on R/L on the inverse (6c4e there), EO kept | 8 | `(L B' U2 B L B R B)` |
| DR on R/L, last EO turn the other way (`U' D R U'`) | 7 | `R D2 F R' F R' F` |

</details>

**5c4e, example 2.** After the EO the case is 5c4e for DR on R/L and 6c6e for DR on U/D.

```
R2 U L2 D F2 D2 R2 F2 U B2 R2 U B2 L' B F2 L2 U2 L2 U' R B'  // scramble
U B' D B                                                     // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (5c4e), EO kept | 8 | `U2 B2 L D F2 L2 R' U` |
| DR on R/L on the inverse (5c4e there), EO kept | 8 | `(U L2 D L U L2 R2 U)` |
| DR on R/L, last EO turn the other way (`U B' D B'`) | 7 | `D2 R' D' R' B2 R' D` |
| DR on U/D (6c6e), EO kept | 8 | `R L D' R' U' R' D' R` |
| DR on U/D on the inverse (6c6e there), EO kept | 7 | `(D' R' U R2 L U' L)` |
| DR on U/D, last EO turn the other way (`U B' D B'`) | 8 | `R D R D' L U D2 R` |

</details>

**5c4e, example 3.** After the EO the case is 5c4e for DR on U/D and 7c2e for DR on F/B.

```
R2 D F2 D' B2 L2 R2 D L2 U' R2 U L2 U B' R2 D' U' L' B2 D' B D R'  // scramble
R B2 D L                                                           // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (5c4e), EO kept | 8 | `B2 U B2 L2 F' U R2 F` |
| DR on U/D on the inverse (5c4e there), EO kept | 7 | `(D B' D' B2 D' R2 F)` |
| DR on U/D, last EO turn the other way (`R B2 D L'`) | 7 | `B2 U B2 F' U R2 F` |
| DR on F/B (7c2e), EO kept | 8 | `D R2 F U' B L2 B' U` |
| DR on F/B on the inverse (7c2e there), EO kept | 8 | `(U D' B R2 D' B' R2 U)` |
| DR on F/B, last EO turn the other way (`R B2 D L'`) | 8 | `D F' B2 D' F2 D F' D` |

</details>

### Case 7c6e: examples 1–3

**7c6e, example 1.** After the EO the case is 7c6e for DR on R/L and 8c6e for DR on F/B.

```
D2 B2 U F2 R2 F2 U' B2 L2 R2 D R2 F' L2 U L' D R B' U2 R' U'  // scramble
U D' B2 U                                                     // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (7c6e), EO kept | 7 | `L' R' F R' U2 L F` |
| DR on R/L on the inverse (7c6e there), EO kept | 8 | `(R F' R' B F' L B F)` |
| DR on R/L, last EO turn the other way (`U D' B2 U'`) | 8 | `L' B R' B2 F R D2 B` |
| DR on F/B (8c6e), EO kept | 9 | `F' R D2 F2 U2 R F' B' L` |
| DR on F/B on the inverse (8c6e there), EO kept | 8 | `(R2 L F R B' D2 U2 R)` |
| DR on F/B, last EO turn the other way (`U D' B2 U'`) | 8 | `B2 R B L' F' R U2 L` |

</details>

**7c6e, example 2.** After the EO the case is 7c6e for DR on F/B and 5c6e for DR on U/D.

```
F2 L2 D' B2 D F2 D' F2 R2 D2 U' B2 U' L2 F' D L2 F2 D' U R' B F2 D  // scramble
U' D B L                                                            // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (7c6e), EO kept | 9 | `F B2 U' B2 U B R2 F U` |
| DR on F/B on the inverse (7c6e there), EO kept | 9 | `(F R2 B' D' B U' F' R2 U)` |
| DR on F/B, last EO turn the other way (`U' D B L'`) | 8 | `F2 U F' U2 B R2 L2 U` |
| DR on U/D (5c6e), EO kept | 7 | `F U L2 B' D' L2 F` |
| DR on U/D on the inverse (5c6e there), EO kept | 9 | `(D' B' U2 F' R2 D B' D2 B)` |
| DR on U/D, last EO turn the other way (`U' D B L'`) | 8 | `R2 B D L2 F' U' L2 B` |

</details>

**7c6e, example 3.** After the EO the case is 7c6e for DR on U/D and 5c6e for DR on F/B.

```
B2 D' R2 U B2 F2 D F2 D2 U' R2 U' L2 F' D' L U B D B2 L2 R' D'  // scramble
L' U2 D R                                                       // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (7c6e), EO kept | 9 | `U2 F' L2 B U' L2 B2 D2 F` |
| DR on U/D on the inverse (7c6e there), EO kept | 8 | `(U' D B' F U' L2 U' F)` |
| DR on U/D, last EO turn the other way (`L' U2 D R'`) | 8 | `D' B F U' F' R2 U' B` |
| DR on F/B (5c6e), EO kept | 8 | `F U L2 U' F L2 B D` |
| DR on F/B on the inverse (5c6e there), EO kept | 9 | `(F2 B2 D' R2 B R2 U' F2 D)` |
| DR on F/B, last EO turn the other way (`L' U2 D R'`) | 7 | `F2 L2 B U' R2 B' D` |

</details>

### Case 4c4e: examples 1–3

**4c4e, example 1.** After the EO the case is 4c4e for DR on U/D and 3c6e for DR on R/L.

```
L2 U L2 D R2 B2 U L2 U' B2 R2 D' R2 U' B' U' F L' B R2 U B R U'  // scramble
R B2 L' F                                                        // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (4c4e), EO kept | 8 | `U D2 F2 U R2 D F2 L` |
| DR on U/D on the inverse (4c4e there), EO kept | 7 | `(B2 U L2 D' R2 F2 L)` |
| DR on U/D, last EO turn the other way (`R B2 L' F'`) | 8 | `U R2 F2 B2 D B2 D L` |
| DR on R/L (3c6e), EO kept | 8 | `L2 U2 D' R D R B2 D` |
| DR on R/L on the inverse (3c6e there), EO kept | 8 | `(U L' U2 L' D2 L' B2 U)` |
| DR on R/L, last EO turn the other way (`R B2 L' F'`) | 7 | `U2 D' R' F2 D2 L' U` |

</details>

**4c4e, example 2.** After the EO the case is 4c4e for DR on U/D and 4c6e for DR on R/L.

```
B2 R2 U2 B2 D L2 D2 L2 F2 U' R2 U2 L2 U2 L' D' B' R D2 B' F2 U2 F  // scramble
D2 F R' B                                                          // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (4c4e), EO kept | 7 | `L2 U2 R2 U2 F2 U L` |
| DR on U/D on the inverse (4c4e there), EO kept | 8 | `(U2 D F2 D' L2 U F2 R)` |
| DR on U/D, last EO turn the other way (`D2 F R' B'`) | 7 | `R2 B2 U D F2 U R` |
| DR on R/L (4c6e), EO kept | 7 | `D' F2 L' U2 D2 R U` |
| DR on R/L on the inverse (4c6e there), EO kept | 8 | `(L2 U L' R U2 B2 L' U)` |
| DR on R/L, last EO turn the other way (`D2 F R' B'`) | 7 | `D L' U' L2 U' B2 U` |

</details>

**4c4e, example 3.** After the EO the case is 4c4e for DR on R/L and 3c4e for DR on U/D.

```
B2 U2 R2 D' L2 U2 B2 R2 F2 L2 U F2 D2 F2 R2 U2 R' F L2 U' L' R' F L2 D2  // scramble
D L F                                                                    // EO on F/B (3 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (4c4e), EO kept | 6 | `F2 L U2 F2 L' D` |
| DR on R/L on the inverse (4c4e there), EO kept | 7 | `(L B2 R D2 L' B2 D)` |
| DR on R/L, last EO turn the other way (`D L F'`) | 5 | `L U2 F2 L' D` |
| DR on U/D (3c4e), EO kept | 8 | `R L U R D R2 U' L` |
| DR on U/D on the inverse (3c4e there), EO kept | 7 | `(R' U D F2 R' D' R)` |
| DR on U/D, last EO turn the other way (`D L F'`) | 8 | `R L D L U L2 D' R` |

</details>

### Case 7c4e: examples 1–3

**7c4e, example 1.** After the EO the case is 7c4e for DR on R/L and 6c6e for DR on F/B.

```
D' R2 D F2 D' B2 F2 L2 U B2 R2 D2 U' R U' L' U B' U F2 R2 D2  // scramble
U2 R' U2 D                                                    // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (7c4e), EO kept | 9 | `L R' F L2 F L' U2 L2 B` |
| DR on R/L on the inverse (7c4e there), EO kept | 9 | `(R B' F R B2 R B L2 F)` |
| DR on R/L, last EO turn the other way (`U2 R' U2 D'`) | 9 | `L R' F R2 B U2 D2 R B` |
| DR on F/B (6c6e), EO kept | 8 | `B R F' R2 D2 R2 B R` |
| DR on F/B on the inverse (6c6e there), EO kept | 8 | `(B L' F' R B U2 F L)` |
| DR on F/B, last EO turn the other way (`U2 R' U2 D'`) | 8 | `L' B2 R' F B' R D2 R` |

</details>

**7c4e, example 2.** After the EO the case is 7c4e for DR on R/L and 5c6e for DR on U/D.

```
B2 U B2 L2 F2 R2 D2 B2 D U2 R2 B2 R' F2 D' L R2 D B' F' R D'  // scramble
D R F B                                                       // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (7c4e), EO kept | 7 | `U R' U R' F2 R2 D` |
| DR on R/L on the inverse (7c4e there), EO kept | 9 | `(L U' L' B2 L D' L R2 D)` |
| DR on R/L, last EO turn the other way (`D R F B'`) | 7 | `U R' U R' F2 R2 D` |
| DR on U/D (5c6e), EO kept | 7 | `D' R U' L U D2 L` |
| DR on U/D on the inverse (5c6e there), EO kept | 9 | `(U2 R' U R L U' F2 U2 R)` |
| DR on U/D, last EO turn the other way (`D R F B'`) | 8 | `U2 R2 U R' L2 F2 U' L` |

</details>

**7c4e, example 3.** After the EO the case is 7c4e for DR on U/D and 6c4e for DR on F/B.

```
B2 R2 D2 L2 D B2 D2 F2 D' R2 U2 L2 B2 L' D2 F D' R2 B L2 U F'  // scramble
U2 B D2 R'                                                     // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (7c4e), EO kept | 9 | `U R2 D' R2 U F U2 D' F` |
| DR on U/D on the inverse (7c4e there), EO kept | 8 | `(B U' D2 B' U R2 U' F)` |
| DR on U/D, last EO turn the other way (`U2 B D2 R`) | 8 | `L2 U' R2 L2 F' U2 D' F` |
| DR on F/B (6c4e), EO kept | 8 | `D2 B D F U' D B' U` |
| DR on F/B on the inverse (6c4e there), EO kept | 8 | `(R2 B2 U' F2 B' U' F U)` |
| DR on F/B, last EO turn the other way (`U2 B D2 R`) | 8 | `U2 F' U B U D' F' D` |

</details>

### Case 6c8e: examples 1–3

**6c8e, example 1.** After the EO the case is 6c8e for DR on R/L and 4c6e for DR on U/D.

```
U B2 R2 U R2 D F2 D' L2 F2 D' R2 F2 D2 F' D2 L' D U' B' L' D U2 L2  // scramble
L' F' D' B                                                          // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (6c8e), EO kept | 8 | `R' D' R U2 L' U' F2 D` |
| DR on R/L on the inverse (6c8e there), EO kept | 8 | `(U D R' F2 U' F2 L2 D)` |
| DR on R/L, last EO turn the other way (`L' F' D' B'`) | 7 | `R' U' L' B2 L' B2 D` |
| DR on U/D (4c6e), EO kept | 8 | `L2 F2 U' F2 D R' U2 L` |
| DR on U/D on the inverse (4c6e there), EO kept | 8 | `(D L D B2 R' L D' R)` |
| DR on U/D, last EO turn the other way (`L' F' D' B'`) | 8 | `D' R U' R L U2 D' R` |

</details>

**6c8e, example 2.** After the EO the case is 6c8e for DR on U/D and 6c8e for DR on F/B.

```
D2 F2 D' B2 L2 U2 B2 D2 F2 L' U' L' U' B' L2 R U2 F' D'  // scramble
U D' B L                                                 // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (6c8e), EO kept | 8 | `U' R2 F' D2 B U D2 B` |
| DR on U/D on the inverse (6c8e there), EO kept | 7 | `(B D' B2 F' L2 D' B)` |
| DR on U/D, last EO turn the other way (`U D' B L'`) | 9 | `U F U2 B' D F' R2 U' F` |
| DR on F/B (6c8e), EO kept | 8 | `F' U' B' D' B U' F U` |
| DR on F/B on the inverse (6c8e there), EO kept | 8 | `(F2 D' B R2 U D B D)` |
| DR on F/B, last EO turn the other way (`U D' B L'`) | 8 | `D' F B D' F2 D2 F U` |

</details>

**6c8e, example 3.** After the EO the case is 6c8e for DR on U/D and 6c6e for DR on F/B.

```
F2 L2 D U2 B2 D L2 D' R2 D2 U' B2 L' F' D' B' D2 R D' B' L U2  // scramble
D F R L                                                        // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (6c8e), EO kept | 9 | `U B F' D' B F' U B F` |
| DR on U/D on the inverse (6c8e there), EO kept | 8 | `(B F R2 U L2 D R2 B)` |
| DR on U/D, last EO turn the other way (`D F R L'`) | 8 | `B' D B2 U B F' U B` |
| DR on F/B (6c6e), EO kept | 9 | `F D' F' U2 D2 F' U R2 D` |
| DR on F/B on the inverse (6c6e there), EO kept | 8 | `(F' B' U B' U2 R2 B' D)` |
| DR on F/B, last EO turn the other way (`D F R L'`) | 8 | `B U D F' B' D2 B' U` |

</details>

### Case 5c8e: examples 1–3

**5c8e, example 1.** After the EO the case is 5c8e for DR on F/B and 8c4e for DR on U/D.

```
R2 D R2 U' F2 U2 R2 U' L2 U2 B2 U B2 U F2 L' D2 B' R2 F D2 U' B R2 U2  // scramble
U F B2 R                                                               // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (5c8e), EO kept | 7 | `D' F' U' B2 D B' D` |
| DR on F/B on the inverse (5c8e there), EO kept | 8 | `(F' U' L2 F' U D B' U)` |
| DR on F/B, last EO turn the other way (`U F B2 R'`) | 8 | `U' B2 R2 B U D F' U` |
| DR on U/D (8c4e), EO kept | 9 | `U F' D B F' D R2 L2 B` |
| DR on U/D on the inverse (8c4e there), EO kept | 9 | `(U2 F D' R2 B' L2 U2 D B)` |
| DR on U/D, last EO turn the other way (`U F B2 R'`) | 9 | `B' U D2 B2 D B U2 D' B` |

</details>

**5c8e, example 2.** After the EO the case is 5c8e for DR on U/D and 4c6e for DR on F/B.

```
L2 B2 D L2 D B2 L2 R2 U B2 U2 L2 D' R2 U' B' L B2 U2 L' U' R2 F L U'  // scramble
D2 B' D2 L                                                            // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (5c8e), EO kept | 9 | `B R2 F' L2 D' F U' D2 B` |
| DR on U/D on the inverse (5c8e there), EO kept | 9 | `(U D' B U' D' F L2 U' B)` |
| DR on U/D, last EO turn the other way (`D2 B' D2 L'`) | 8 | `B2 F' L2 B D L2 U' B` |
| DR on F/B (4c6e), EO kept | 8 | `F' B' R2 U B2 U2 F D` |
| DR on F/B on the inverse (4c6e there), EO kept | 8 | `(U2 R2 F2 U2 B' U L2 D)` |
| DR on F/B, last EO turn the other way (`D2 B' D2 L'`) | 9 | `F2 U2 B' D' F' U2 D' F U` |

</details>

**5c8e, example 3.** After the EO the case is 5c8e for DR on F/B and 6c6e for DR on R/L.

```
B2 U' R2 D2 L2 U B2 L2 U' L2 D2 L2 R2 U' B' U L' F R2 D' R' B2 F' D' U'  // scramble
U B2 R D'                                                                // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (5c8e), EO kept | 8 | `F L' F R' L2 F U2 L` |
| DR on F/B on the inverse (5c8e there), EO kept | 8 | `(F' R2 L D2 R' F' B L)` |
| DR on F/B, last EO turn the other way (`U B2 R D`) | 8 | `F' R2 D2 L F L2 B R` |
| DR on R/L (6c6e), EO kept | 7 | `L U2 B D2 L U2 B` |
| DR on R/L on the inverse (6c6e there), EO kept | 7 | `(U2 B2 F L D2 L B)` |
| DR on R/L, last EO turn the other way (`U B2 R D`) | 8 | `B L U2 L B L' R' B` |

</details>

### Case 4c8e: examples 1–3

**4c8e, example 1.** After the EO the case is 4c8e for DR on R/L and 6c6e for DR on U/D.

```
L2 D B2 R2 U R2 D R2 B2 U2 B2 R2 U' R2 U2 L' D F L R' F L D F'  // scramble
F U2 R' B                                                       // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (4c8e), EO kept | 9 | `L D' L2 R D B2 D' L U` |
| DR on R/L on the inverse (4c8e there), EO kept | 9 | `(R F2 U F2 U B2 D L' U)` |
| DR on R/L, last EO turn the other way (`F U2 R' B'`) | 8 | `L F2 U' L U D' L U` |
| DR on U/D (6c6e), EO kept | 9 | `U L' U' B2 D' L U D' R` |
| DR on U/D on the inverse (6c6e there), EO kept | 6 | `(L D' F2 L' D R)` |
| DR on U/D, last EO turn the other way (`F U2 R' B'`) | 8 | `D' R' L2 B2 D L D R` |

</details>

**4c8e, example 2.** After the EO the case is 4c8e for DR on F/B and 6c6e for DR on U/D.

```
D' L2 U' F2 L2 R2 U2 L2 U' F2 U2 L2 R2 U' F' L' B2 L2 U' B2 D' F' U L2  // scramble
B' U' D L                                                               // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (4c8e), EO kept | 8 | `F U' L2 D B D2 F U` |
| DR on F/B on the inverse (4c8e there), EO kept | 8 | `(R2 D F U2 B U2 B2 U)` |
| DR on F/B, last EO turn the other way (`B' U' D L'`) | 9 | `F' U2 D B2 U2 R2 L2 F' D` |
| DR on U/D (6c6e), EO kept | 9 | `U F U2 D F U' B' U' F` |
| DR on U/D on the inverse (6c6e there), EO kept | 8 | `(U R2 U' B U D R2 F)` |
| DR on U/D, last EO turn the other way (`B' U' D L'`) | 8 | `U2 B U' F D' R2 U F` |

</details>

**4c8e, example 3.** After the EO the case is 4c8e for DR on U/D and 2c6e for DR on F/B.

```
D L2 F2 U' R2 U F2 R2 U R2 U' R2 U L D2 B' D' U' F' L' B R' D2  // scramble
R L D L                                                         // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (4c8e), EO kept | 9 | `D' B' R2 F2 U' D2 B D2 F` |
| DR on U/D on the inverse (4c8e there), EO kept | 9 | `(D' F U D2 B2 F' U2 D B)` |
| DR on U/D, last EO turn the other way (`R L D L'`) | 9 | `D' B' R2 F U' L2 B2 U2 B` |
| DR on F/B (2c6e), EO kept | 8 | `D F B2 D' R2 U' B D` |
| DR on F/B on the inverse (2c6e there), EO kept | 7 | `(F U F B2 D2 B D)` |
| DR on F/B, last EO turn the other way (`R L D L'`) | 8 | `B U R2 B D' B' L2 D` |

</details>

### Case 3c6e: examples 1–3

**3c6e, example 1.** After the EO the case is 3c6e for DR on U/D and 3c6e for DR on F/B.

```
U2 L2 B2 D' B2 U' B2 U R2 U' B2 R2 B' U B' F' L B R2 F L U  // scramble
U' F' B' L                                                  // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (3c6e), EO kept | 9 | `U F D L2 B R2 B2 D' B` |
| DR on U/D on the inverse (3c6e there), EO kept | 7 | `(L2 D B2 F' U' D2 B)` |
| DR on U/D, last EO turn the other way (`U' F' B' L'`) | 9 | `U F' U F2 U2 B' L2 D' F` |
| DR on F/B (3c6e), EO kept | 7 | `U2 F U2 D F2 B U` |
| DR on F/B on the inverse (3c6e there), EO kept | 8 | `(B2 U' D' B U F' B U)` |
| DR on F/B, last EO turn the other way (`U' F' B' L'`) | 8 | `U2 F U2 L2 D F2 B U` |

</details>

**3c6e, example 2.** After the EO the case is 3c6e for DR on R/L and 4c6e for DR on F/B.

```
B2 F2 L2 F2 D L2 D' F2 L2 D' B2 U B' D' F L R' U' L B2 F'  // scramble
L B U D                                                    // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (3c6e), EO kept | 7 | `U2 L' R' F' L R2 B` |
| DR on R/L on the inverse (3c6e there), EO kept | 5 | `(L2 B' L2 R' F)` |
| DR on R/L, last EO turn the other way (`L B U D'`) | 8 | `L' R' B' L2 B2 F2 L F` |
| DR on F/B (4c6e), EO kept | 8 | `L B R L2 B U2 F' L` |
| DR on F/B on the inverse (4c6e there), EO kept | 8 | `(F' B2 U2 R F2 L' B' L)` |
| DR on F/B, last EO turn the other way (`L B U D'`) | 8 | `F2 R2 U2 R F2 R2 B L` |

</details>

**3c6e, example 3.** After the EO the case is 3c6e for DR on R/L and 4c2e for DR on F/B.

```
B2 L2 U' B2 U2 B2 L2 U' L2 F2 U2 F2 U L2 U R' F' R D L R2 F' R2 U R'  // scramble
U R L D                                                               // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (3c6e), EO kept | 8 | `D2 B2 U2 R2 F L R2 B` |
| DR on R/L on the inverse (3c6e there), EO kept | 8 | `(R' D2 F R' B2 D2 L' B)` |
| DR on R/L, last EO turn the other way (`U R L D'`) | 7 | `B2 U2 R2 F L R2 B` |
| DR on F/B (4c2e), EO kept | 8 | `F2 B' R' L2 B' R2 F' R` |
| DR on F/B on the inverse (4c2e there), EO kept | 7 | `(B2 R D2 R' F' B2 L)` |
| DR on F/B, last EO turn the other way (`U R L D'`) | 8 | `R2 B' R F R' L' F L` |

</details>

### Case 7c8e: examples 1–3

**7c8e, example 1.** After the EO the case is 7c8e for DR on U/D and 6c6e for DR on R/L.

```
R2 D2 B2 F2 D' R2 D' R2 B2 L2 R2 U' B2 U' L' D' R' B' R' U' R B2 U'  // scramble
U L' F2 B                                                            // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (7c8e), EO kept | 9 | `U R2 F2 B2 R D' R2 U L` |
| DR on U/D on the inverse (7c8e there), EO kept | 8 | `(U R D' F2 B2 L2 U R)` |
| DR on U/D, last EO turn the other way (`U L' F2 B'`) | 8 | `R2 D L D' R L D' L` |
| DR on R/L (6c6e), EO kept | 7 | `R D' L' U L2 R2 U` |
| DR on R/L on the inverse (6c6e there), EO kept | 8 | `(D2 L U' F2 L' U L' U)` |
| DR on R/L, last EO turn the other way (`U L' F2 B'`) | 8 | `R B2 U' D R F2 B2 D` |

</details>

**7c8e, example 2.** After the EO the case is 7c8e for DR on R/L and 5c6e for DR on U/D.

```
U' L2 U' L2 U2 F2 U R2 B2 F2 D' L2 F2 U R' F L' B2 R2 D L B F U'  // scramble
B' R2 U F                                                         // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (7c8e), EO kept | 7 | `L2 U2 L U2 D R U` |
| DR on R/L on the inverse (7c8e there), EO kept | 6 | `(L D2 F2 D R' U)` |
| DR on R/L, last EO turn the other way (`B' R2 U F'`) | 7 | `L B2 U2 B2 D' L U` |
| DR on U/D (5c6e), EO kept | 7 | `D2 R U R2 D R L` |
| DR on U/D on the inverse (5c6e there), EO kept | 8 | `(U F2 L' U2 R F2 D L)` |
| DR on U/D, last EO turn the other way (`B' R2 U F'`) | 7 | `D2 R U R2 D R L` |

</details>

**7c8e, example 3.** After the EO the case is 7c8e for DR on F/B and 8c2e for DR on R/L.

```
L2 U2 L2 R2 D F2 R2 D R2 D' L2 B2 R' B' R2 D R F' D L' U R'  // scramble
L' F B' D                                                    // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (7c8e), EO kept | 7 | `U2 R L B R' U2 R` |
| DR on F/B on the inverse (7c8e there), EO kept | 8 | `(B D2 L' B' R L' F L)` |
| DR on F/B, last EO turn the other way (`L' F B' D'`) | 8 | `F' L2 F U2 R L2 F L` |
| DR on R/L (8c2e), EO kept | 9 | `B L' R B L' R2 U2 D2 F` |
| DR on R/L on the inverse (8c2e there), EO kept | 9 | `(B' L F' R2 B U2 L2 R B)` |
| DR on R/L, last EO turn the other way (`L' F B' D'`) | 10 | `L B L' R B' R B2 L' U2 F` |

</details>

### Case 6c2e: examples 1–3

**6c2e, example 1.** After the EO the case is 6c2e for DR on U/D and 5c6e for DR on F/B.

```
B2 L2 F2 L2 D' L2 D R2 D' F2 U2 F2 R' B' R' B' D2 R B2 F2 D2  // scramble
U B2 U L                                                      // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (6c2e), EO kept | 8 | `U2 B' D2 B' U B' U B` |
| DR on U/D on the inverse (6c2e there), EO kept | 9 | `(U D F' R2 U B' U D2 B)` |
| DR on U/D, last EO turn the other way (`U B2 U L'`) | 9 | `U B' L2 U' R2 U' F2 U' F` |
| DR on F/B (5c6e), EO kept | 7 | `D' F R2 L2 U2 F D` |
| DR on F/B on the inverse (5c6e there), EO kept | 8 | `(B U D B' R2 F B2 D)` |
| DR on F/B, last EO turn the other way (`U B2 U L'`) | 8 | `F2 B2 R2 U B D2 B D` |

</details>

**6c2e, example 2.** After the EO the case is 6c2e for DR on F/B and 6c6e for DR on R/L.

```
B2 L2 U L2 D2 U' L2 B2 D' B2 U R2 B' U' F' L2 U2 R B F2 U2 R U'  // scramble
U F R' D                                                         // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (6c2e), EO kept | 8 | `L' F R2 B L' F' B L` |
| DR on F/B on the inverse (6c2e there), EO kept | 8 | `(R' D2 F L' F' R' F' L)` |
| DR on F/B, last EO turn the other way (`U F R' D'`) | 8 | `F' L' F R2 B L' F' L` |
| DR on R/L (6c6e), EO kept | 8 | `R F L' B U2 L R2 F` |
| DR on R/L on the inverse (6c6e there), EO kept | 7 | `(L2 U2 B' R B' D2 B)` |
| DR on R/L, last EO turn the other way (`U F R' D'`) | 9 | `L U2 F' R' B R' F2 L B` |

</details>

**6c2e, example 3.** After the EO the case is 6c2e for DR on F/B and 6c6e for DR on R/L.

```
F2 U' L2 F2 U' B2 D' B2 L2 D' L2 B2 U' L' B2 R' F' R D' F' L B' F2  // scramble
R2 D2 L U'                                                          // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (6c2e), EO kept | 9 | `F L F' L D2 L' B' D2 L` |
| DR on F/B on the inverse (6c2e there), EO kept | 9 | `(F2 B2 R F B R F' B2 R)` |
| DR on F/B, last EO turn the other way (`R2 D2 L U`) | 8 | `L F B2 L' F R' D2 R` |
| DR on R/L (6c6e), EO kept | 8 | `L' R' F2 L' B F' R' B` |
| DR on R/L on the inverse (6c6e there), EO kept | 8 | `(L F L U2 L F' L B)` |
| DR on R/L, last EO turn the other way (`R2 D2 L U`) | 8 | `L2 U2 L F L R U2 B` |

</details>

### Case 8c6e: examples 1–3

**8c6e, example 1.** After the EO the case is 8c6e for DR on F/B and 7c2e for DR on R/L.

```
B2 D' F2 L2 B2 F2 D B2 L2 D L2 U F2 D' L' F' R U F L U2 R'  // scramble
U2 R F U                                                    // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (8c6e), EO kept | 8 | `F R F L2 D2 R2 F R` |
| DR on F/B on the inverse (8c6e there), EO kept | 9 | `(B2 R' B R2 B' R L B R)` |
| DR on F/B, last EO turn the other way (`U2 R F U'`) | 8 | `R2 B L' D2 R' U2 B' L` |
| DR on R/L (7c2e), EO kept | 9 | `L2 R F D2 L2 U2 L' R2 B` |
| DR on R/L on the inverse (7c2e there), EO kept | 9 | `(L B' R B L R U2 L' F)` |
| DR on R/L, last EO turn the other way (`U2 R F U'`) | 10 | `L R F U2 R U2 R' B2 L F` |

</details>

**8c6e, example 2.** After the EO the case is 8c6e for DR on U/D and 6c4e for DR on F/B.

```
U2 F2 R2 U' L2 U' B2 R2 B2 L2 U' L2 F2 D F' D' B2 L' B D2 L U' B2 D'  // scramble
U F B2 L'                                                             // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (8c6e), EO kept | 8 | `U2 F' U B L2 B2 D F` |
| DR on U/D on the inverse (8c6e there), EO kept | 8 | `(D' B U R2 L2 B' U F)` |
| DR on U/D, last EO turn the other way (`U F B2 L`) | 8 | `D2 B L2 U R2 U L2 F` |
| DR on F/B (6c4e), EO kept | 7 | `B U F' B2 U' F2 U` |
| DR on F/B on the inverse (6c4e there), EO kept | 8 | `(B U L2 U' R2 D2 B' U)` |
| DR on F/B, last EO turn the other way (`U F B2 L`) | 8 | `B D' F R2 D' F' B2 D` |

</details>

**8c6e, example 3.** After the EO the case is 8c6e for DR on U/D and 5c8e for DR on R/L.

```
D L2 U F2 U2 L2 B2 U R2 F2 R2 F2 U L' F L' R F L' U' R' B F  // scramble
F2 U2 R2 F                                                   // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (8c6e), EO kept | 9 | `L D R' U D2 F2 R' B2 L` |
| DR on U/D on the inverse (8c6e there), EO kept | 8 | `(R' F2 L U2 L U' D' L)` |
| DR on U/D, last EO turn the other way (`F2 U2 R2 F'`) | 9 | `U' L U R U2 F2 B2 U L` |
| DR on R/L (5c8e), EO kept | 7 | `D' L2 U' L R' B2 U` |
| DR on R/L on the inverse (5c8e there), EO kept | 9 | `(U D2 L2 D R B2 U2 L2 D)` |
| DR on R/L, last EO turn the other way (`F2 U2 R2 F'`) | 8 | `F2 D' L2 U' L R' B2 U` |

</details>

### Case 3c4e: examples 1–3

**3c4e, example 1.** After the EO the case is 3c4e for DR on F/B and 4c6e for DR on U/D.

```
U R2 D' L2 B2 D' F2 D' L2 R2 D' B2 U2 F' R F D' B U2 B2 F L2  // scramble
D F D' L                                                      // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (3c4e), EO kept | 8 | `F2 D2 F U' R2 L2 F' D` |
| DR on F/B on the inverse (3c4e there), EO kept | 5 | `(U F U' B U)` |
| DR on F/B, last EO turn the other way (`D F D' L'`) | 8 | `F L2 U' R2 F2 U B U` |
| DR on U/D (4c6e), EO kept | 8 | `U' D2 B U2 B2 L2 U' B` |
| DR on U/D on the inverse (4c6e there), EO kept | 8 | `(D B' U2 D F U' L2 F)` |
| DR on U/D, last EO turn the other way (`D F D' L'`) | 7 | `B' U' L2 F U' L2 F` |

</details>

**3c4e, example 2.** After the EO the case is 3c4e for DR on U/D and 5c8e for DR on F/B.

```
U' R2 F2 R2 F2 U R2 U2 L2 D' R2 B2 F2 B' L D2 L F' D2 L' D' L'  // scramble
U L' U' L                                                       // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (3c4e), EO kept | 7 | `B D' B2 U2 B' U' B` |
| DR on U/D on the inverse (3c4e there), EO kept | 8 | `(U' B2 U2 B' D' R2 U2 F)` |
| DR on U/D, last EO turn the other way (`U L' U' L'`) | 8 | `U2 B2 D F U B D2 B` |
| DR on F/B (5c8e), EO kept | 8 | `L2 D B D R2 D' F U` |
| DR on F/B on the inverse (5c8e there), EO kept | 9 | `(F B U F L2 B U' B' D)` |
| DR on F/B, last EO turn the other way (`U L' U' L'`) | 7 | `D B D R2 D' F U` |

</details>

**3c4e, example 3.** After the EO the case is 3c4e for DR on F/B and 7c6e for DR on U/D.

```
L2 B2 L2 F2 U R2 D' F2 U2 F2 L2 U F2 D B' U L2 R2 B D R F D2  // scramble
D2 F' R'                                                      // EO on R/L (3 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (3c4e), EO kept | 6 | `R2 U F2 U B D` |
| DR on F/B on the inverse (3c4e there), EO kept | 7 | `(F' U' D2 F R2 L2 D)` |
| DR on F/B, last EO turn the other way (`D2 F' R`) | 5 | `U F2 U B D` |
| DR on U/D (7c6e), EO kept | 6 | `D' B' R2 L2 U' B` |
| DR on U/D on the inverse (7c6e there), EO kept | 8 | `(B D F' U' B2 R2 U B)` |
| DR on U/D, last EO turn the other way (`D2 F' R`) | 7 | `R2 D' B' R2 L2 U' B` |

</details>

### Case 2c4e: examples 1–3

**2c4e, example 1.** After the EO the case is 2c4e for DR on F/B and 5c2e for DR on U/D.

```
U' B2 D' L2 B2 F2 U R2 U2 L2 F2 D L2 U' L2 F' R B' L F' D R D' F D'  // scramble
D L' B R                                                             // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (2c4e), EO kept | 7 | `D' R2 B R2 B R2 D` |
| DR on F/B on the inverse (2c4e there), EO kept | 8 | `(B U2 F2 U' F2 U' L2 U)` |
| DR on F/B, last EO turn the other way (`D L' B R'`) | 8 | `F' D F' B U2 D B D` |
| DR on U/D (5c2e), EO kept | 9 | `U D' B U' B F2 U' L2 F` |
| DR on U/D on the inverse (5c2e there), EO kept | 8 | `(U2 B F' D F' D R2 B)` |
| DR on U/D, last EO turn the other way (`D L' B R'`) | 8 | `U' F U B2 D' B2 D F` |

</details>

**2c4e, example 2.** After the EO the case is 2c4e for DR on F/B and 4c6e for DR on U/D.

```
U2 B2 D' R2 U F2 R2 B2 D' R2 D F2 D2 L2 F' R' B' D F L2 B U' L U'  // scramble
F' L' D R'                                                         // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (2c4e), EO kept | 8 | `U B U' F' L2 U' F2 U` |
| DR on F/B on the inverse (2c4e there), EO kept | 8 | `(F D' R2 D F' U' F2 D)` |
| DR on F/B, last EO turn the other way (`F' L' D R`) | 7 | `U' B D F' D' B' U` |
| DR on U/D (4c6e), EO kept | 8 | `D B' F2 D' B' U' D F` |
| DR on U/D on the inverse (4c6e there), EO kept | 7 | `(U' F2 D' R2 B L2 F)` |
| DR on U/D, last EO turn the other way (`F' L' D R`) | 7 | `U2 B' U' R2 L2 D' B` |

</details>

**2c4e, example 3.** After the EO the case is 2c4e for DR on R/L and 7c4e for DR on F/B.

```
L2 U R2 D2 F2 L2 U' L2 D B2 L2 U2 R' D' R' U2 F D L' B2 D  // scramble
L' F2 B' U                                                 // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (2c4e), EO kept | 8 | `R' B2 F' R2 F U2 R F` |
| DR on R/L on the inverse (2c4e there), EO kept | 7 | `(F D2 L F2 R' U2 F)` |
| DR on R/L, last EO turn the other way (`L' F2 B' U'`) | 8 | `L' B2 F' U2 F D2 R B` |
| DR on F/B (7c4e), EO kept | 7 | `R B' D2 B2 D2 U2 R` |
| DR on F/B on the inverse (7c4e there), EO kept | 8 | `(B L' U2 L' F B D2 R)` |
| DR on F/B, last EO turn the other way (`L' F2 B' U'`) | 7 | `R B' D2 B2 D2 U2 R` |

</details>

### Case 4c2e: examples 1–3

**4c2e, example 1.** After the EO the case is 4c2e for DR on U/D and 7c4e for DR on F/B.

```
D2 F2 D R2 D' B2 D R2 D2 B2 U' B2 U B' R F2 R' B2 U2 B D  // scramble
U L D L                                                   // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (4c2e), EO kept | 7 | `D B' U2 D2 B' R2 F` |
| DR on U/D on the inverse (4c2e there), EO kept | 7 | `(U F D B' F' D B)` |
| DR on U/D, last EO turn the other way (`U L D L'`) | 7 | `D' B' D2 B U D2 B` |
| DR on F/B (7c4e), EO kept | 7 | `U R2 F' D F L2 U` |
| DR on F/B on the inverse (7c4e there), EO kept | 8 | `(F D2 R2 B' U' F' B2 U)` |
| DR on F/B, last EO turn the other way (`U L D L'`) | 8 | `L2 U R2 F' D F L2 U` |

</details>

**4c2e, example 2.** After the EO the case is 4c2e for DR on R/L and 4c6e for DR on F/B.

```
R2 U2 L2 U R2 D' R2 U2 L2 D R2 U B2 D' R' B' L2 D' U F2 L U' L R'  // scramble
D L' B' U                                                          // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (4c2e), EO kept | 8 | `L2 U2 B' F2 R' B2 L' B` |
| DR on R/L on the inverse (4c2e there), EO kept | 8 | `(L R' F R' F R U2 F)` |
| DR on R/L, last EO turn the other way (`D L' B' U'`) | 8 | `R F' L F' R2 B L B` |
| DR on F/B (4c6e), EO kept | 7 | `L2 D2 L F2 R2 F' R` |
| DR on F/B on the inverse (4c6e there), EO kept | 7 | `(F2 B2 R' F L B' L)` |
| DR on F/B, last EO turn the other way (`D L' B' U'`) | 7 | `R2 U2 L B2 L2 F R` |

</details>

**4c2e, example 3.** After the EO the case is 4c2e for DR on R/L and 4c4e for DR on F/B.

```
D' L2 U' R2 U' B2 R2 D2 L2 U B2 L2 U2 F2 R' D' U2 B2 F D' U F D2  // scramble
U' D2 F D                                                         // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (4c2e), EO kept | 8 | `L' F U2 F' U2 F2 L F` |
| DR on R/L on the inverse (4c2e there), EO kept | 6 | `(L' F D2 R' D2 F)` |
| DR on R/L, last EO turn the other way (`U' D2 F D'`) | 8 | `L F2 R2 B D2 R' D2 B` |
| DR on F/B (4c4e), EO kept | 7 | `U2 F' D2 R D2 F2 L` |
| DR on F/B on the inverse (4c4e there), EO kept | 8 | `(U2 F R2 D2 B2 D2 U2 R)` |
| DR on F/B, last EO turn the other way (`U' D2 F D'`) | 7 | `R' U2 F2 R' D2 F L` |

</details>

### Case 3c2e: examples 1–3

**3c2e, example 1.** After the EO the case is 3c2e for DR on R/L and 6c4e for DR on F/B.

```
B2 D2 R2 B2 F2 D B2 D2 U L2 B2 F2 R' B' R' D' L U B' F'  // scramble
F' R B U                                                 // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (3c2e), EO kept | 7 | `L2 R F2 R2 F R F` |
| DR on R/L on the inverse (3c2e there), EO kept | 5 | `(B2 L2 B' R' B)` |
| DR on R/L, last EO turn the other way (`F' R B U'`) | 7 | `L B2 R' B2 F' R F` |
| DR on F/B (6c4e), EO kept | 8 | `R2 U2 L D2 R2 U2 B' L` |
| DR on F/B on the inverse (6c4e there), EO kept | 8 | `(R F2 R' U2 F L' F L)` |
| DR on F/B, last EO turn the other way (`F' R B U'`) | 7 | `F2 R' U2 R' L2 B L` |

</details>

**3c2e, example 2.** After the EO the case is 3c2e for DR on U/D and 5c6e for DR on R/L.

```
L2 U F2 L2 U' L2 R2 D L2 U' L2 U F2 R2 U' F' R B2 U B D' U' F D U'  // scramble
R' B R' F                                                           // EO on F/B (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (3c2e), EO kept | 7 | `F2 U R2 U L' D' L` |
| DR on U/D on the inverse (3c2e there), EO kept | 7 | `(U F2 U2 R2 L' U L)` |
| DR on U/D, last EO turn the other way (`R' B R' F'`) | 6 | `U R2 U L' D' L` |
| DR on R/L (5c6e), EO kept | 7 | `L2 B2 R D R B2 U` |
| DR on R/L on the inverse (5c6e there), EO kept | 8 | `(L D L' U B2 L2 R' D)` |
| DR on R/L, last EO turn the other way (`R' B R' F'`) | 7 | `L2 B2 R' D R' B2 U` |

</details>

**3c2e, example 3.** After the EO the case is 3c2e for DR on F/B and 2c0e for DR on U/D.

```
R2 U R2 B2 U' B2 D F2 R2 U B2 U' B2 R' D' R2 U B2  // scramble
B2 R2 D R                                          // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on F/B (3c2e), EO kept | 7 | `R2 B L2 F' D' F' D` |
| DR on F/B on the inverse (3c2e there), EO kept | 6 | `(F B U' D2 F U)` |
| DR on F/B, last EO turn the other way (`B2 R2 D R'`) | 6 | `B L2 F' D' F' D` |
| DR on U/D (2c0e), EO kept | 5 | `B' U' F2 U B` |
| DR on U/D on the inverse (2c0e there), EO kept | 6 | `(U' B' U F2 U' B)` |
| DR on U/D, last EO turn the other way (`B2 R2 D R'`) | 6 | `U2 B D' F2 D B` |

</details>

### Case 8c8e: examples 1–3

**8c8e, example 1.** After the EO the case is 8c8e for DR on R/L and 5c6e for DR on F/B.

```
L2 F2 L2 B2 D' L2 F2 U' L2 F2 U' B2 L2 U2 F' R' B U F' U2 R2 F L' D'  // scramble
L2 F2 B2 D                                                            // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (8c8e), EO kept | 7 | `R' F L' B L2 R' B` |
| DR on R/L on the inverse (8c8e there), EO kept | 7 | `(R B F2 L F' R' B)` |
| DR on R/L, last EO turn the other way (`L2 F2 B2 D'`) | 6 | `B F' R B2 R2 B` |
| DR on F/B (5c6e), EO kept | 7 | `B D2 L B' R U2 L` |
| DR on F/B on the inverse (5c6e there), EO kept | 8 | `(F2 U2 L' B R' U2 F' R)` |
| DR on F/B, last EO turn the other way (`L2 F2 B2 D'`) | 8 | `F L B' L F R2 B R` |

</details>

**8c8e, example 2.** After the EO the case is 8c8e for DR on U/D and 5c6e for DR on F/B.

```
D2 U' B2 L2 D L2 D' L2 U' F2 U' L2 R2 F' U' B R B F2 R F' U R'  // scramble
U' F' B' R                                                      // EO on R/L (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on U/D (8c8e), EO kept | 8 | `B D L2 F' L2 F2 D' F` |
| DR on U/D on the inverse (8c8e there), EO kept | 8 | `(U L2 D' B F U D' B)` |
| DR on U/D, last EO turn the other way (`U' F' B' R'`) | 8 | `B D L2 F' L2 F2 D' F` |
| DR on F/B (5c6e), EO kept | 8 | `D2 F' R2 B2 D B L2 U` |
| DR on F/B on the inverse (5c6e there), EO kept | 9 | `(F R2 U F2 L2 D R2 F' U)` |
| DR on F/B, last EO turn the other way (`U' F' B' R'`) | 8 | `U2 D' F D2 B' U F2 D` |

</details>

**8c8e, example 3.** After the EO the case is 8c8e for DR on R/L and 4c6e for DR on F/B.

```
L2 U' B2 D B2 U' F2 U' B2 L2 U2 B2 L2 U2 R' F' L' B' F L' F' L2  // scramble
U L' B2 U'                                                       // EO on U/D (4 turns)
```

<details><summary>Turns to DR each way</summary>

Each row is one way to finish: the DR axis and the option, the fewest turns to DR that way, and one DR of that length.

| After the EO | Turns to DR | One shortest DR |
|---|---:|---|
| DR on R/L (8c8e), EO kept | 8 | `L2 B' F L' R B L2 B` |
| DR on R/L on the inverse (8c8e there), EO kept | 7 | `(L U2 B F L R F)` |
| DR on R/L, last EO turn the other way (`U L' B2 U`) | 7 | `B F' L R B' D2 B` |
| DR on F/B (4c6e), EO kept | 10 | `F B' L' U2 B D2 L' B' D2 R` |
| DR on F/B on the inverse (4c6e there), EO kept | 7 | `(D2 B L U2 R' B' L)` |
| DR on F/B, last EO turn the other way (`U L' B2 U`) | 9 | `B D2 R F2 R' U2 L F' R` |

</details>
