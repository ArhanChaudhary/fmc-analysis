This is what Daichi, JTuu and wen asked for. There are 46 corner cases once you merge rotations, mirrors and turning a layer. Inside a corner subset they are *not* equally good, and since the corner case on inverse is a different one, there are two reads.

How to read the tables:

- "A qt takes it straight to" means some U or D quarter turn lowers the corner qt count right away, with no setup.
- L is the range of optimal corner solution lengths the case can have.
- Each subset gets three tables: what the cases look like, how they finish, and a typical DR of each case (a state whose optimal is the median for that case).
- "Both sides together" tables: each row is a combination of the cases on normal and on inverse, with its share of the subset and how it finishes.

**2c4** (wen's stacks). Seven cases. Two of them have the same bad corners and are told apart by the back face, as explained under the tables. One case per row:

| Bad corners | L | A qt takes it straight to | Share of the subset |
|---|---|---|---:|
| both on one layer, adjacent; back-face diagonals agree | 7–10 | 2c3 | 17% |
| 1 up 1 down, opposite | 8–10 | 4b3 | 8% |
| both on one layer, adjacent; back-face diagonals differ | 7–10 | 2c3 | 17% |
| both on one layer, adjacent | 8–11 | nothing, needs a setup | 17% |
| 1 up 1 down, stacked | 9–11 | 4b3 | 8% |
| 1 up 1 down, opposite | 8–11 | nothing, needs a setup | 17% |
| 1 up 1 down, stacked | 9–12 | nothing, needs a setup | 17% |

How each case finishes, same rows: the share of its DRs finishing in 10, 11, 12 and 13 or less.

| Bad corners | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|
| both on one layer, adjacent; back-face diagonals agree | 0.48% | 3.1% | 16% | 57% |
| 1 up 1 down, opposite | 0.31% | 2.3% | 13% | 51% |
| both on one layer, adjacent; back-face diagonals differ | 0.38% | 2.4% | 13% | 47% |
| both on one layer, adjacent | 0.15% | 1.1% | 7.0% | 33% |
| 1 up 1 down, stacked | 0.13% | 1.1% | 7.0% | 33% |
| 1 up 1 down, opposite | 0.13% | 0.99% | 6.4% | 31% |
| 1 up 1 down, stacked | 0.04% | 0.52% | 4.1% | 23% |

A typical DR of each case, with its optimal finish:

| Bad corners | A typical DR | Its optimal, moves |
|---|---|---:|
| both on one layer, adjacent; back-face diagonals agree | `R2 D' B2 F2 L2 D' B2 U B2 D' B2 F2 U2` | 13 |
| 1 up 1 down, opposite | `R2 B2 F2 U' L2 D2 B2 U' F2 L2 U' L2 U'` | 13 |
| both on one layer, adjacent; back-face diagonals differ | `F2 U' B2 D' L2 D' L2 U B2 R2 U L2 F2 U'` | 14 |
| both on one layer, adjacent | `B2 D2 R2 U F2 U L2 U' R2 D2 R2 F2 U' R2` | 14 |
| 1 up 1 down, stacked | `B2 U B2 U2 B2 F2 R2 D B2 L2 U' B2 R2 U'` | 14 |
| 1 up 1 down, opposite | `U' L2 D B2 U2 B2 L2 F2 U' L2 B2 D2 U' R2` | 14 |
| 1 up 1 down, stacked | `U F2 U' L2 F2 D B2 R2 F2 D2 B2 U' F2 U2` | 14 |

**Telling the two look-alike 2c4 cases apart.** Hold the cube so the two bad corners are on the front edge of one layer (if you see six bad corners, turn both layers, U D', and you will see two). The four corners of the back face are then all good. Take each diagonal of the back face. Its two corners share exactly one colour: their sticker on the back face, their U/D sticker, or their sticker on the side. If both diagonals share the same kind of sticker, the diagonals agree; otherwise they differ.

Both sides together, one row per combination of the cases on normal and on inverse:

| Normal and inverse | Share of the subset | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|
| the best case on both sides (adjacent, a qt straight to 2c3, first row) | 2.8% | 0.92% | 5.6% | 26% | 75% |
| no stack on either side, and a qt goes straight to 2c3 or 4b3 on both | 17.4% | 0.68% | 4.2% | 21% | 66% |
| a stack on one side only | 37.5% | 0.10% | 0.92% | 6.4% | 32% |
| a stack on both sides | 6.2% | 0 | 0.06% | 1.1% | 11% |

So a double stack is as dead as a 5qt at every target, and the best layout on both sides is as good as the last row. Each row is a kind of DR, with the share finishing in 10, 11, 12 and 13 or less:

| DRs | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|
| a stack on both sides | 0 | 0.06% | 1.1% | 11% |
| all 5qt DRs | 0.02% | 0.24% | 2.1% | 14% |
| an average 2c3 4e | 1.3% | 6.4% | 27% | 73% |

    U2 L2 D' F2 U' R2 U F2 D L2 U2   // the fastest any double-stacked 2c4 finishes: 11

**2c5.** Three cases, one per row:

| Bad corners | L | A qt takes it straight to | Share of the subset |
|---|---|---|---:|
| both on one layer, adjacent | 9–12 | 2c4 | 50% |
| 1 up 1 down, opposite | 10–13 | 4b4 | 25% |
| 1 up 1 down, stacked | 11–13 | 4b4 | 25% |

How each case finishes, same rows: the share of its DRs finishing in 10, 11, 12 and 13 or less.

| Bad corners | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|
| both on one layer, adjacent | 0.05% | 0.45% | 3.4% | 19% |
| 1 up 1 down, opposite | 0.01% | 0.20% | 1.9% | 13% |
| 1 up 1 down, stacked | 0 | 0.03% | 0.62% | 6.0% |

A typical DR of each case, with its optimal finish:

| Bad corners | A typical DR | Its optimal, moves |
|---|---|---:|
| both on one layer, adjacent | `D' R2 D R2 U2 L2 D' F2 U' R2 U F2 L2 U2` | 14 |
| 1 up 1 down, opposite | `B2 D U2 F2 U L2 U R2 U2 L2 U' F2 U' R2` | 14 |
| 1 up 1 down, stacked | `B2 D' B2 D' B2 R2 D2 L2 U' F2 D F2 L2 U R2` | 15 |

Both sides together, one row per combination of the cases on normal and on inverse:

| Normal and inverse | Share of the subset | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|
| adjacent on both sides | 25.0% | 0.08% | 0.69% | 4.7% | 25% |
| adjacent and opposite | 25.0% | 0.02% | 0.35% | 2.9% | 18% |
| opposite on both sides | 6.2% | 0 | 0.09% | 1.4% | 11% |
| adjacent and stacked | 25.0% | 0 | 0.06% | 1.1% | 9.5% |
| opposite and stacked | 12.5% | 0 | 0 | 0.24% | 4.5% |
| stacked on both sides | 6.2% | 0 | 0 | 0 | 0.64% |

The last two rows are 19% of all 2c5, and you can drop them on sight whatever your target: a 2c5 that is stacked on both sides never finishes in 12, and stacked on one side with opposite on the other never finishes in 11 and is 0.24% for a 12.

    U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2   // the fastest any double-stacked 2c5 finishes: 13

**4c3** (JTuu's question). Nine cases, seven of them 4a3 and two 4b3. Eight rows, because two of the 4a3 cases look the same:

| Bad corners | Subset | L | A qt takes it straight to | Share of the subset |
|---|---|---|---|---:|
| 2-2, pairs on opposite sides | 4a3 | 7–9 | 4b2 | 8% |
| 2-2, pairs stacked | 4a3 | 7–9 | 4b2 | 8% |
| 2-2, pairs sharing one column | 4b3 | 7–10 | 4a2 | 17% |
| 3-1 | 4b3 | 8–11 | nothing, needs a setup | 33% |
| 2-2, diagonal over diagonal | 4a3 | 8–10 | nothing, needs a setup | 8% |
| 4-0 (two cases that look the same) | 4a3 | 8–10 | nothing, needs a setup | 8% |
| 2-2, pairs stacked | 4a3 | 8–10 | nothing, needs a setup | 8% |
| 2-2, pairs on opposite sides | 4a3 | 9–11 | nothing, needs a setup | 8% |

How each case finishes, same rows: the share of its DRs finishing in 10, 11, 12 and 13 or less.

| Bad corners | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|
| 2-2, pairs on opposite sides | 0.75% | 4.5% | 22% | 68% |
| 2-2, pairs stacked | 0.62% | 3.6% | 18% | 60% |
| 2-2, pairs sharing one column | 0.50% | 2.8% | 13% | 47% |
| 3-1 | 0.29% | 2.0% | 11% | 45% |
| 2-2, diagonal over diagonal | 0.26% | 1.8% | 10% | 43% |
| 4-0 (two cases that look the same) | 0.24% | 1.7% | 10% | 43% |
| 2-2, pairs stacked | 0.23% | 1.6% | 9.4% | 40% |
| 2-2, pairs on opposite sides | 0.05% | 0.47% | 3.6% | 22% |

A typical DR of each case, with its optimal finish:

| Bad corners | A typical DR | Its optimal, moves |
|---|---|---:|
| 2-2, pairs on opposite sides | `D R2 D' F2 D' B2 R2 B2 U L2 D2 U' R2` | 13 |
| 2-2, pairs stacked | `R2 U' F2 U R2 B2 D L2 U2 R2 U' R2 U'` | 13 |
| 2-2, pairs sharing one column | `R2 D2 R2 U L2 U' B2 R2 B2 U L2 D F2 U'` | 14 |
| 3-1 | `R2 F2 U' B2 D' B2 R2 D' R2 D R2 U2 L2 U'` | 14 |
| 2-2, diagonal over diagonal | `B2 F2 U' F2 L2 U R2 U2 L2 R2 B2 D' F2 L2` | 14 |
| 4-0 (two cases that look the same), one | `D2 B2 D' B2 U' B2 D2 L2 U' L2 U' F2 U'` | 13 |
| 4-0 (two cases that look the same), the other | `D' F2 U L2 D' L2 R2 U' B2 U R2 D F2 U'` | 14 |
| 2-2, pairs stacked | `D' L2 U' F2 D' F2 L2 D' L2 U B2 U2 R2 U2` | 14 |
| 2-2, pairs on opposite sides | `D' L2 U F2 D' B2 L2 U' R2 U L2 D F2 U'` | 14 |

The row marked "two cases that look the same" is two corner cases with the same bad corners and no quarter turn that lowers the count. I have not found a visible test that separates them, so the row gives their odds together. Apart, they are 0.40% / 2.8% / 15% / 57% and 0.07% / 0.68% / 5.1% / 28% (in 10 / 11 / 12 / 13), and only the optimal corner solution tells you which: 8 moves is the better one, 10 the worse one, and with 9 it can be either.

Both sides together, one row per combination of the cases on normal and on inverse:

| Normal and inverse | Share of the subset | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|
| the best pair of cases | 5.6% | 0.95% | 5.3% | 23% | 68% |
| the worst pair of cases | 11.1% | 0.01% | 0.29% | 3.0% | 20% |

**4b2** (Daichi's four: 2-2 and 3-1, each with good and bad parity). Three rows, because the two 3-1 cases look the same:

| Bad corners | L | A qt takes it straight to | Share of the subset |
|---|---|---|---:|
| 2-2, pairs sharing one column | 3–6 | 4a1 | 17% |
| 3-1 (two cases that look the same) | 4–8 | nothing, needs a setup | 67% |
| 2-2, pairs sharing one column | 6–9 | nothing, needs a setup | 17% |

How each case finishes, same rows: the share of its DRs finishing in 10, 11, 12 and 13 or less.

| Bad corners | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|
| 2-2, pairs sharing one column | 3.4% | 14% | 44% | 88% |
| 3-1 (two cases that look the same) | 2.1% | 9.8% | 36% | 83% |
| 2-2, pairs sharing one column | 1.3% | 7.0% | 30% | 78% |

A typical DR of each case, with its optimal finish:

| Bad corners | A typical DR | Its optimal, moves |
|---|---|---:|
| 2-2, pairs sharing one column | `U' L2 D' L2 U' F2 U L2 U2 R2 D' R2 U'` | 13 |
| 3-1 (two cases that look the same), one | `U' L2 D' L2 U B2 D2 B2 U' L2 U B2 D'` | 13 |
| 3-1 (two cases that look the same), the other | `R2 U L2 R2 D L2 U' B2 F2 R2 D' R2 D2` | 13 |
| 2-2, pairs sharing one column | `B2 D2 L2 D R2 F2 D' L2 B2 F2 D' U' L2` | 13 |

The 3-1 row is two corner cases that look the same (Daichi's "3-1 good parity" and "3-1 bad parity"). I have not found a visible test that separates them, so the row gives their odds together. Apart, they are 2.5% / 11% / 40% / 86% and 1.7% / 8.4% / 33% / 81% (in 10 / 11 / 12 / 13), and only the optimal corner solution tells you which: 4 moves is the better one, 8 the worse one, and with 5 to 7 it can be either.

Both sides together, one row per combination of the cases on normal and on inverse:

| Normal and inverse | Share of the subset | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|
| the best pair of cases | 2.8% | 4.8% | 17% | 50% | 91% |
| the worst pair of cases | 2.8% | 0.61% | 4.2% | 21% | 69% |

**4a2.** The widest spread of the low-qt subsets. One case per row:

| Bad corners | L | A qt takes it straight to | Share of the subset |
|---|---|---|---:|
| 2-2, diagonal over diagonal | 5–8 | 4a1 | 17% |
| 2-2, pairs stacked | 6–9 | nothing, needs a setup | 33% |
| 2-2, pairs on opposite sides | 7–10 | nothing, needs a setup | 33% |
| 4-0 | 8–11 | nothing, needs a setup | 17% |

How each case finishes, same rows: the share of its DRs finishing in 10, 11, 12 and 13 or less.

| Bad corners | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|
| 2-2, diagonal over diagonal | 2.4% | 9.3% | 31% | 72% |
| 2-2, pairs stacked | 1.4% | 6.1% | 22% | 60% |
| 2-2, pairs on opposite sides | 0.50% | 2.7% | 12% | 42% |
| 4-0 | 0.32% | 1.9% | 9.3% | 33% |

A typical DR of each case, with its optimal finish:

| Bad corners | A typical DR | Its optimal, moves |
|---|---|---:|
| 2-2, diagonal over diagonal | `F2 R2 U B2 F2 U' L2 R2 U' R2 D2 F2 U` | 13 |
| 2-2, pairs stacked | `B2 L2 D' L2 D2 B2 D F2 R2 U2 R2 F2 D2` | 13 |
| 2-2, pairs on opposite sides | `D R2 U2 L2 R2 B2 U' B2 R2 U B2 U2 R2 U'` | 14 |
| 4-0 | `B2 R2 U2 R2 U' B2 R2 U2 R2 D B2 L2 U2 L2` | 14 |

Both sides together, one row per combination of the cases on normal and on inverse:

| Normal and inverse | Share of the subset | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|
| the best pair of cases | 2.8% | 4.4% | 14% | 43% | 83% |
| the worst pair of cases | 2.8% | 0 | 0.16% | 2.3% | 13% |

**4c4** and **4b5** are too rare at 10 and 11 for the case to matter (under 1% in 11 for every case). For a 12, 4c4 runs from 0.57% to 4.3% by case and 4b5 from 1.3% to 2.2%.

Appendix E lists all 46 cases with a typical DR and the shortest setup for each, the L range (which is what Evan asked for), and the full both-sides tables.
