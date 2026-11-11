This is what Daichi, JTuu and wen asked for. There are 46 corner cases once you merge rotations, mirrors and turning a layer. Inside a corner subset they are *not* equally good, and since the corner case on inverse is a different one, there are two reads.

How to read the tables:

- "A qt takes it straight to" means some U or D quarter turn lowers the corner qt count right away, with no setup.
- L is the range of optimal corner solution lengths the case can have.
- The last column is a typical DR of the case: a state whose optimal is the median for that case, with that optimal in brackets.

**2c4** (wen's stacks). Seven cases. Two of them have the same bad corners and are told apart by the back face, as explained under the table:

| Bad corners | L | A qt takes it straight to | Share | In 12 | In 13 | A typical DR (its optimal) |
|---|---|---|---:|---:|---:|---|
| both on one layer, adjacent; back-face diagonals agree | 7–10 | 2c3 | 17% | 16.2% | 57% | `R2 D' B2 F2 L2 D' B2 U B2 D' B2 F2 U2` (13) |
| 1 up 1 down, opposite | 8–10 | 4b3 | 8% | 13.2% | 51% | `R2 B2 F2 U' L2 D2 B2 U' F2 L2 U' L2 U'` (13) |
| both on one layer, adjacent; back-face diagonals differ | 7–10 | 2c3 | 17% | 12.5% | 47% | `F2 U' B2 D' L2 D' L2 U B2 R2 U L2 F2 U'` (14) |
| both on one layer, adjacent | 8–11 | nothing, needs a setup | 17% | 7.0% | 33% | `B2 D2 R2 U F2 U L2 U' R2 D2 R2 F2 U' R2` (14) |
| 1 up 1 down, stacked | 9–11 | 4b3 | 8% | 7.0% | 33% | `B2 U B2 U2 B2 F2 R2 D B2 L2 U' B2 R2 U'` (14) |
| 1 up 1 down, opposite | 8–11 | nothing, needs a setup | 17% | 6.4% | 31% | `U' L2 D B2 U2 B2 L2 F2 U' L2 B2 D2 U' R2` (14) |
| 1 up 1 down, stacked | 9–12 | nothing, needs a setup | 17% | 4.1% | 23% | `U F2 U' L2 F2 D B2 R2 F2 D2 B2 U' F2 U2` (14) |

**Telling the two look-alike 2c4 cases apart.** Hold the cube so the two bad corners are on the front edge of one layer (if you see six bad corners, turn both layers, U D', and you will see two). The four corners of the back face are then all good. Take each diagonal of the back face. Its two corners share exactly one colour: their sticker on the back face, their U/D sticker, or their sticker on the side. If both diagonals share the same kind of sticker, the diagonals agree; otherwise they differ.

Both sides together:

| Normal and inverse | Share | In 12 | In 13 |
|---|---:|---:|---:|
| the best case on both sides (adjacent, a qt straight to 2c3, first row) | 2.8% | 26.3% | 74.7% |
| a qt goes straight to 2c3 or 4b3 on both sides | 17.4% | 20.5% | 65.5% |
| a stack on one side only | 37.5% | 6.4% | 31.6% |
| a stack on both sides | 6.2% | 1.1% | 10.5% |

So a double stack is as dead as a 5qt, and the best layout on both sides is as good as an average 2c3 4e (27% in 12).

    U2 L2 D' F2 U' R2 U F2 D L2 U2   // the fastest any double-stacked 2c4 finishes: 11

**2c5.** Three cases:

| Bad corners | L | A qt takes it straight to | Share | In 12 | In 13 | A typical DR (its optimal) |
|---|---|---|---:|---:|---:|---|
| both on one layer, adjacent | 9–12 | 2c4 | 50% | 3.4% | 19% | `D' R2 D R2 U2 L2 D' F2 U' R2 U F2 L2 U2` (14) |
| 1 up 1 down, opposite | 10–13 | 4b4 | 25% | 1.9% | 13% | `B2 D U2 F2 U L2 U R2 U2 L2 U' F2 U' R2` (14) |
| 1 up 1 down, stacked | 11–13 | 4b4 | 25% | 0.6% | 6% | `B2 D' B2 D' B2 R2 D2 L2 U' F2 D F2 L2 U R2` (15) |

Both sides together:

| Normal and inverse | Share | In 12 | In 13 |
|---|---:|---:|---:|
| adjacent on both sides | 25.0% | 4.7% | 25.1% |
| adjacent and opposite | 25.0% | 2.9% | 17.8% |
| opposite on both sides | 6.2% | 1.4% | 11.4% |
| adjacent and stacked | 25.0% | 1.1% | 9.5% |
| opposite and stacked | 12.5% | 0.2% | 4.5% |
| stacked on both sides | 6.2% | 0.0% | 0.6% |

The last two rows are 19% of all 2c5, and you can drop them on sight: a 2c5 that is stacked on both sides never finishes in 12.

    U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2   // the fastest any double-stacked 2c5 finishes: 13

**4c3** (JTuu's question). Nine cases, seven of them 4a3 and two 4b3. Eight rows, because two of the 4a3 cases look the same:

| Bad corners | Subset | L | A qt takes it straight to | Share | In 12 | In 13 | A typical DR (its optimal) |
|---|---|---|---|---:|---:|---:|---|
| 2-2, pairs on opposite sides | 4a3 | 7–9 | 4b2 | 8% | 21.6% | 68% | `D R2 D' F2 D' B2 R2 B2 U L2 D2 U' R2` (13) |
| 2-2, pairs stacked | 4a3 | 7–9 | 4b2 | 8% | 17.6% | 60% | `R2 U' F2 U R2 B2 D L2 U2 R2 U' R2 U'` (13) |
| 2-2, pairs sharing one column | 4b3 | 7–10 | 4a2 | 17% | 13.5% | 47% | `R2 D2 R2 U L2 U' B2 R2 B2 U L2 D F2 U'` (14) |
| 3-1 | 4b3 | 8–11 | nothing, needs a setup | 33% | 11.4% | 45% | `R2 F2 U' B2 D' B2 R2 D' R2 D R2 U2 L2 U'` (14) |
| 2-2, diagonal over diagonal | 4a3 | 8–10 | nothing, needs a setup | 8% | 10.3% | 43% | `B2 F2 U' F2 L2 U R2 U2 L2 R2 B2 D' F2 L2` (14) |
| 4-0 (two cases that look the same) | 4a3 | 8–10 | nothing, needs a setup | 8% | 10.2% | 43% | `D2 B2 D' B2 U' B2 D2 L2 U' L2 U' F2 U'` (13) or `D' F2 U L2 D' L2 R2 U' B2 U R2 D F2 U'` (14) |
| 2-2, pairs stacked | 4a3 | 8–10 | nothing, needs a setup | 8% | 9.4% | 40% | `D' L2 U' F2 D' F2 L2 D' L2 U B2 U2 R2 U2` (14) |
| 2-2, pairs on opposite sides | 4a3 | 9–11 | nothing, needs a setup | 8% | 3.6% | 22% | `D' L2 U F2 D' B2 L2 U' R2 U L2 D F2 U'` (14) |

The row marked "two cases that look the same" is two corner cases with the same bad corners and no quarter turn that lowers the count. I have not found a visible test that separates them, so the row gives their odds together. Apart, they are 15% in 12 (57% in 13) and 5% in 12 (28% in 13), and only the optimal corner solution tells you which: 8 moves is the better one, 10 the worse one, and with 9 it can be either.

Both sides together:

| Normal and inverse | Share | In 12 | In 13 |
|---|---:|---:|---:|
| the best pair of cases | 5.6% | 23.1% | 67.8% |
| the worst pair of cases | 11.1% | 3.0% | 20.3% |

**4b2** (Daichi's four: 2-2 and 3-1, each with good and bad parity). Three rows, because the two 3-1 cases look the same:

| Bad corners | L | A qt takes it straight to | Share | In 12 | In 13 | A typical DR (its optimal) |
|---|---|---|---:|---:|---:|---|
| 2-2, pairs sharing one column | 3–6 | 4a1 | 17% | 43.9% | 88% | `U' L2 D' L2 U' F2 U L2 U2 R2 D' R2 U'` (13) |
| 3-1 (two cases that look the same) | 4–8 | nothing, needs a setup | 67% | 36.4% | 83% | `U' L2 D' L2 U B2 D2 B2 U' L2 U B2 D'` (13) or `R2 U L2 R2 D L2 U' B2 F2 R2 D' R2 D2` (13) |
| 2-2, pairs sharing one column | 6–9 | nothing, needs a setup | 17% | 29.6% | 78% | `B2 D2 L2 D R2 F2 D' L2 B2 F2 D' U' L2` (13) |

The 3-1 row is two corner cases that look the same (Daichi's "3-1 good parity" and "3-1 bad parity"). I have not found a visible test that separates them, so the row gives their odds together. Apart, they are 40% in 12 and 33% in 12, and only the optimal corner solution tells you which: 4 moves is the better one, 8 the worse one, and with 5 to 7 it can be either.

Both sides together:

| Normal and inverse | Share | In 12 | In 13 |
|---|---:|---:|---:|
| the best pair of cases | 2.8% | 49.7% | 90.7% |
| the worst pair of cases | 2.8% | 21.2% | 68.9% |

**4a2.** The widest spread of the low-qt subsets:

| Bad corners | L | A qt takes it straight to | Share | In 12 | In 13 | A typical DR (its optimal) |
|---|---|---|---:|---:|---:|---|
| 2-2, diagonal over diagonal | 5–8 | 4a1 | 17% | 31.0% | 72% | `F2 R2 U B2 F2 U' L2 R2 U' R2 D2 F2 U` (13) |
| 2-2, pairs stacked | 6–9 | nothing, needs a setup | 33% | 22.4% | 60% | `B2 L2 D' L2 D2 B2 D F2 R2 U2 R2 F2 D2` (13) |
| 2-2, pairs on opposite sides | 7–10 | nothing, needs a setup | 33% | 12.4% | 42% | `D R2 U2 L2 R2 B2 U' B2 R2 U B2 U2 R2 U'` (14) |
| 4-0 | 8–11 | nothing, needs a setup | 17% | 9.3% | 33% | `B2 R2 U2 R2 U' B2 R2 U2 R2 D B2 L2 U2 L2` (14) |

Both sides together:

| Normal and inverse | Share | In 12 | In 13 |
|---|---:|---:|---:|
| the best pair of cases | 2.8% | 43.4% | 83.0% |
| the worst pair of cases | 2.8% | 2.3% | 13.1% |

**4c4** runs from 0.6% to 4.3% in 12 by case, and **4b5** from 1.3% to 2.2%. Nothing to see there.

Appendix E lists all 46 cases with a typical DR and the shortest setup for each, the L range (which is what Evan asked for), and the full both-sides tables.
