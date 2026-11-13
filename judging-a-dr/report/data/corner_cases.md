
**0c0**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 0c0-1 | none bad | 0–5 | nothing, needs a setup |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 0c0-1 | `R2 U' F2 R2 D L2 B2 R2 U L2 U R2` | 12 | none needed |

How each case finishes: its share of 0c0, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 0c0-1 | 100.0% | 12.28 | 6.1% | 21% | 54% | 90% |

**4a1**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 4a1-1 | 4-0 | 1–4 | 0c0 |  |
| 4a1-2 | 2-2, pairs on opposite sides | 2–5 | nothing, needs a setup |  |
| 4a1-3 | 2-2, pairs stacked | 3–6 | nothing, needs a setup |  |
| 4a1-4 | 2-2, diagonal over diagonal | 4–7 | nothing, needs a setup |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 4a1-1 | `U2 F2 R2 B2 U B2 U2 B2 U2 R2 F2 U2` | 12 | `D` |
| 4a1-2 | `B2 U' F2 D F2 L2 U2 B2 D2 B2 U' L2` | 12 | `D B2` |
| 4a1-3 | `R2 U' B2 L2 D2 B2 D2 B2 D B2 U' F2 U2` | 13 | `D B2 D2` |
| 4a1-4 | `D2 B2 U L2 D' B2 R2 B2 D' L2 D' U' F2` | 13 | `D' R2 D2 F2` |

How each case finishes: its share of 4a1, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4a1-1 | 16.7% | 12.30 | 5.6% | 19% | 52% | 91% |
| 4a1-2 | 33.3% | 12.36 | 4.8% | 17% | 50% | 91% |
| 4a1-3 | 33.3% | 12.48 | 3.8% | 14% | 45% | 88% |
| 4a1-4 | 16.7% | 12.54 | 3.5% | 14% | 42% | 86% |

4a1, corner case on both sides. Each row is a pair of cases, one on normal and one on inverse, in either order:

| Cases on the two sides | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4a1-1 and 4a1-3 | 11.1% | 12.29 | 5.6% | 20% | 53% | 92% |
| 4a1-1 and 4a1-2 | 11.1% | 12.29 | 5.6% | 19% | 53% | 91% |
| 4a1-1 and 4a1-4 | 5.6% | 12.31 | 5.6% | 19% | 52% | 90% |
| 4a1-1 and 4a1-1 | 2.8% | 12.32 | 5.7% | 19% | 52% | 89% |
| 4a1-2 and 4a1-2 | 11.1% | 12.34 | 4.9% | 18% | 51% | 91% |
| 4a1-2 and 4a1-3 | 22.2% | 12.38 | 4.3% | 16% | 49% | 91% |
| 4a1-2 and 4a1-4 | 11.1% | 12.42 | 4.3% | 16% | 47% | 90% |
| 4a1-3 and 4a1-3 | 11.1% | 12.59 | 3.0% | 12% | 40% | 86% |
| 4a1-3 and 4a1-4 | 11.1% | 12.66 | 2.5% | 11% | 37% | 83% |
| 4a1-4 and 4a1-4 | 2.8% | 12.78 | 1.9% | 8.6% | 33% | 78% |

**4a2**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 4a2-1 | 2-2, diagonal over diagonal | 5–8 | 4a1 |  |
| 4a2-2 | 2-2, pairs stacked | 6–9 | nothing, needs a setup |  |
| 4a2-3 | 2-2, pairs on opposite sides | 7–10 | nothing, needs a setup |  |
| 4a2-4 | 4-0 | 8–11 | nothing, needs a setup |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 4a2-1 | `F2 R2 U B2 F2 U' L2 R2 U' R2 D2 F2 U` | 13 | `U R2 U2 F2 U` |
| 4a2-2 | `B2 L2 D' L2 D2 B2 D F2 R2 U2 R2 F2 D2` | 13 | `D' B2 D2 R2 U R2` |
| 4a2-3 | `D R2 U2 L2 R2 B2 U' B2 R2 U B2 U2 R2 U'` | 14 | `U' R2 U2 F2 U R2 U2` |
| 4a2-4 | `B2 R2 U2 R2 U' B2 R2 U2 R2 D B2 L2 U2 L2` | 14 | `D R2 U2 F2 U F2 U2 R2` |

How each case finishes: its share of 4a2, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4a2-1 | 16.7% | 12.86 | 2.4% | 9.3% | 31% | 72% |
| 4a2-2 | 33.3% | 13.14 | 1.4% | 6.1% | 22% | 60% |
| 4a2-3 | 33.3% | 13.58 | 0.50% | 2.7% | 12% | 42% |
| 4a2-4 | 16.7% | 13.80 | 0.32% | 1.9% | 9.3% | 33% |

4a2, corner case on both sides. Each row is a pair of cases, one on normal and one on inverse, in either order:

| Cases on the two sides | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4a2-1 and 4a2-1 | 2.8% | 12.54 | 4.4% | 14% | 43% | 83% |
| 4a2-2 and 4a2-1 | 11.1% | 12.71 | 3.1% | 12% | 35% | 79% |
| 4a2-2 and 4a2-2 | 11.1% | 12.97 | 1.8% | 7.7% | 27% | 68% |
| 4a2-3 and 4a2-1 | 11.1% | 13.02 | 1.3% | 6.6% | 25% | 66% |
| 4a2-4 and 4a2-1 | 5.6% | 13.16 | 1.0% | 4.8% | 21% | 61% |
| 4a2-2 and 4a2-3 | 22.2% | 13.33 | 0.68% | 3.5% | 16% | 53% |
| 4a2-4 and 4a2-2 | 11.1% | 13.52 | 0.42% | 2.7% | 12% | 43% |
| 4a2-3 and 4a2-3 | 11.1% | 13.85 | 0.15% | 1.1% | 6.3% | 29% |
| 4a2-4 and 4a2-3 | 11.1% | 14.09 | 0.04% | 0.59% | 4.2% | 20% |
| 4a2-4 and 4a2-4 | 2.8% | 14.42 | 0 | 0.16% | 2.3% | 13% |

**4b2**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 4b2-1 | 2-2, pairs sharing one column | 3–6 | 4a1 |  |
| 4b2-2 | 3-1 | 4–7 | nothing, needs a setup | looks the same as the 3-1 case with L 5–8. Only the corner solution separates them: L = 4 is this one |
| 4b2-3 | 3-1 | 5–8 | nothing, needs a setup | looks the same as the 3-1 case with L 4–7. Only the corner solution separates them: L = 8 is this one |
| 4b2-4 | 2-2, pairs sharing one column | 6–9 | nothing, needs a setup |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 4b2-1 | `U' L2 D' L2 U' F2 U L2 U2 R2 D' R2 U'` | 13 | `U R2 U'` |
| 4b2-2 | `U' L2 D' L2 U B2 D2 B2 U' L2 U B2 D'` | 13 | `D' F2 U' F2` |
| 4b2-3 | `R2 U L2 R2 D L2 U' B2 F2 R2 D' R2 D2` | 13 | `U' L2 U' F2 U2` |
| 4b2-4 | `B2 D2 L2 D R2 F2 D' L2 B2 F2 D' U' L2` | 13 | `D F2 U R2 U2 F2` |

How each case finishes: its share of 4b2, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4b2-1 | 16.7% | 12.50 | 3.4% | 14% | 44% | 88% |
| 4b2-2 | 33.3% | 12.61 | 2.5% | 11% | 40% | 86% |
| 4b2-3 | 33.3% | 12.76 | 1.7% | 8.4% | 33% | 81% |
| 4b2-4 | 16.7% | 12.85 | 1.3% | 7.0% | 30% | 78% |

4b2, corner case on both sides. Each row is a pair of cases, one on normal and one on inverse, in either order:

| Cases on the two sides | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4b2-1 and 4b2-1 | 2.8% | 12.36 | 4.8% | 17% | 50% | 91% |
| 4b2-2 and 4b2-1 | 11.1% | 12.44 | 3.8% | 15% | 47% | 90% |
| 4b2-2 and 4b2-2 | 11.1% | 12.55 | 2.9% | 12% | 42% | 87% |
| 4b2-3 and 4b2-1 | 11.1% | 12.56 | 2.8% | 12% | 41% | 87% |
| 4b2-4 and 4b2-1 | 5.6% | 12.63 | 2.5% | 11% | 38% | 85% |
| 4b2-3 and 4b2-2 | 22.2% | 12.67 | 2.1% | 9.7% | 36% | 84% |
| 4b2-2 and 4b2-4 | 11.1% | 12.75 | 1.6% | 8.2% | 33% | 82% |
| 4b2-3 and 4b2-3 | 11.1% | 12.85 | 1.2% | 6.8% | 29% | 78% |
| 4b2-3 and 4b2-4 | 11.1% | 12.95 | 0.87% | 5.3% | 26% | 74% |
| 4b2-4 and 4b2-4 | 2.8% | 13.06 | 0.61% | 4.2% | 21% | 69% |

**0c3**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 0c3-1 | none bad | 9–12 | 4a2 |  |
| 0c3-2 | none bad | 10–12 | nothing, needs a setup |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 0c3-1 | `R2 U F2 U2 L2 D' L2 U B2 U2 L2 U' F2 U'` | 14 | `D' R2 D2 F2 U F2 U2 R2 U` |
| 0c3-2 | `L2 B2 D L2 F2 U2 F2 D L2 U2 B2 U' L2 B2 U2` | 15 | `U L2 D2 F2 U F2 U2 R2 U R2` |

How each case finishes: its share of 0c3, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 0c3-1 | 33.3% | 14.29 | 0.09% | 0.70% | 4.0% | 18% |
| 0c3-2 | 66.7% | 14.54 | 0.01% | 0.22% | 1.9% | 11% |

0c3, corner case on both sides. Each row is a pair of cases, one on normal and one on inverse, in either order:

| Cases on the two sides | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 0c3-1 and 0c3-1 | 11.1% | 14.22 | 0.20% | 1.1% | 5.4% | 23% |
| 0c3-1 and 0c3-2 | 44.4% | 14.33 | 0.04% | 0.51% | 3.3% | 15% |
| 0c3-2 and 0c3-2 | 44.4% | 14.65 | 0 | 0.08% | 1.2% | 9.0% |

**2c3**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 2c3-1 | 1 up 1 down, stacked | 5–8 | 4b2 |  |
| 2c3-2 | 1 up 1 down, opposite | 5–8 | 4b2 |  |
| 2c3-3 | both on one layer, adjacent | 6–9 | nothing, needs a setup |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 2c3-1 | `R2 D' F2 D' R2 D2 F2 R2 U F2 D' L2 U'` | 13 | `D' F2 D' L2 U'` |
| 2c3-2 | `L2 D2 B2 D R2 D' B2 L2 D R2 U B2 U'` | 13 | `U' R2 U' R2 U` |
| 2c3-3 | `L2 B2 F2 D' R2 F2 D' F2 D2 U' F2 L2 D2` | 13 | `U R2 U' F2 U F2` |

How each case finishes: its share of 2c3, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 2c3-1 | 25.0% | 12.68 | 2.1% | 9.9% | 37% | 83% |
| 2c3-2 | 25.0% | 12.87 | 1.5% | 7.2% | 29% | 75% |
| 2c3-3 | 50.0% | 13.08 | 0.89% | 4.9% | 22% | 66% |

2c3, corner case on both sides. Each row is a pair of cases, one on normal and one on inverse, in either order:

| Cases on the two sides | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 2c3-1 and 2c3-1 | 6.3% | 12.49 | 3.1% | 14% | 45% | 88% |
| 2c3-2 and 2c3-1 | 12.5% | 12.64 | 2.3% | 10% | 38% | 85% |
| 2c3-3 and 2c3-1 | 25.0% | 12.78 | 1.5% | 7.7% | 32% | 80% |
| 2c3-2 and 2c3-2 | 6.3% | 12.84 | 1.6% | 7.7% | 30% | 77% |
| 2c3-3 and 2c3-2 | 25.0% | 13.01 | 1.0% | 5.4% | 24% | 70% |
| 2c3-3 and 2c3-3 | 25.0% | 13.25 | 0.53% | 3.3% | 16% | 57% |

**4c3**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 4c3-1 | 2-2, pairs on opposite sides | 7–9 | 4b2 |  |
| 4c3-2 | 2-2, pairs stacked | 7–9 | 4b2 |  |
| 4c3-3 | 4-0 | 8–9 | nothing, needs a setup | looks the same as the 4-0 case with L 9–10. Only the corner solution separates them: L = 8 is this one |
| 4c3-4 | 2-2, pairs sharing one column | 7–10 | 4a2 |  |
| 4c3-5 | 3-1 | 8–11 | nothing, needs a setup |  |
| 4c3-6 | 2-2, diagonal over diagonal | 8–10 | nothing, needs a setup |  |
| 4c3-7 | 2-2, pairs stacked | 8–10 | nothing, needs a setup |  |
| 4c3-8 | 4-0 | 9–10 | nothing, needs a setup | looks the same as the 4-0 case with L 8–9. Only the corner solution separates them: L = 10 is this one |
| 4c3-9 | 2-2, pairs on opposite sides | 9–11 | nothing, needs a setup |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 4c3-1 | `D R2 D' F2 D' B2 R2 B2 U L2 D2 U' R2` | 13 | `D B2 U F2 U2 R2 U` |
| 4c3-2 | `R2 U' F2 U R2 B2 D L2 U2 R2 U' R2 U'` | 13 | `D' R2 D' B2 U2 R2 U` |
| 4c3-3 | `D2 B2 D' B2 U' B2 D2 L2 U' L2 U' F2 U'` | 13 | `D' R2 U B2 U2 R2 U R2` |
| 4c3-4 | `R2 D2 R2 U L2 U' B2 R2 B2 U L2 D F2 U'` | 14 | `D' B2 U2 R2 U F2 U` |
| 4c3-5 | `R2 F2 U' B2 D' B2 R2 D' R2 D R2 U2 L2 U'` | 14 | `D B2 D2 R2 U F2 U' R2` |
| 4c3-6 | `B2 F2 U' F2 L2 U R2 U2 L2 R2 B2 D' F2 L2` | 14 | `U' F2 U' R2 U2 F2 U F2` |
| 4c3-7 | `D' L2 U' F2 D' F2 L2 D' L2 U B2 U2 R2 U2` | 14 | `U' L2 U' R2 U2 F2 U F2` |
| 4c3-8 | `D' F2 U L2 D' L2 R2 U' B2 U R2 D F2 U'` | 14 | `U' F2 D R2 U2 F2 U R2 U2` |
| 4c3-9 | `D' L2 U F2 D' B2 L2 U' R2 U L2 D F2 U'` | 14 | `D' B2 U' F2 U2 R2 U F2 U2` |

How each case finishes: its share of 4c3, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4c3-1 | 8.3% | 13.06 | 0.75% | 4.5% | 22% | 68% |
| 4c3-2 | 8.3% | 13.21 | 0.62% | 3.6% | 18% | 60% |
| 4c3-3 | 4.2% | 13.27 | 0.40% | 2.8% | 15% | 57% |
| 4c3-4 | 16.7% | 13.45 | 0.50% | 2.8% | 13% | 47% |
| 4c3-5 | 33.3% | 13.51 | 0.29% | 2.0% | 11% | 45% |
| 4c3-6 | 8.3% | 13.52 | 0.26% | 1.8% | 10% | 43% |
| 4c3-7 | 8.3% | 13.59 | 0.23% | 1.6% | 9.4% | 40% |
| 4c3-8 | 4.2% | 13.83 | 0.07% | 0.68% | 5.1% | 28% |
| 4c3-9 | 8.3% | 14.00 | 0.05% | 0.47% | 3.6% | 22% |

4c3, corner case on both sides. Each row is a pair of cases, one on normal and one on inverse, in either order:

| Cases on the two sides | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4c3-4 and 4c3-1 | 5.6% | 13.04 | 0.95% | 5.3% | 23% | 68% |
| 4c3-5 and 4c3-1 | 11.1% | 13.07 | 0.65% | 4.1% | 21% | 68% |
| 4c3-4 and 4c3-2 | 5.6% | 13.19 | 0.78% | 4.4% | 19% | 59% |
| 4c3-5 and 4c3-2 | 11.1% | 13.22 | 0.54% | 3.3% | 17% | 60% |
| 4c3-3 and 4c3-4 | 2.8% | 13.24 | 0.60% | 3.2% | 17% | 58% |
| 4c3-3 and 4c3-5 | 5.6% | 13.28 | 0.31% | 2.5% | 15% | 57% |
| 4c3-4 and 4c3-6 | 5.6% | 13.47 | 0.41% | 2.3% | 12% | 46% |
| 4c3-4 and 4c3-7 | 5.6% | 13.54 | 0.35% | 2.1% | 11% | 42% |
| 4c3-5 and 4c3-6 | 11.1% | 13.54 | 0.19% | 1.6% | 9.5% | 42% |
| 4c3-5 and 4c3-7 | 11.1% | 13.61 | 0.17% | 1.4% | 8.5% | 39% |
| 4c3-8 and 4c3-4 | 2.8% | 13.79 | 0.16% | 1.0% | 5.8% | 30% |
| 4c3-8 and 4c3-5 | 5.6% | 13.84 | 0.03% | 0.51% | 4.8% | 28% |
| 4c3-4 and 4c3-9 | 5.6% | 13.95 | 0.11% | 0.84% | 4.8% | 24% |
| 4c3-5 and 4c3-9 | 11.1% | 14.03 | 0.01% | 0.29% | 3.0% | 20% |

**0c4**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 0c4-1 | none bad | 9–10 | 4a3 |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 0c4-1 | `B2 U R2 B2 U' L2 B2 D2 B2 U B2 R2 D2 U'` | 14 | `U' F2 D L2 U2 F2 U F2 U'` |

How each case finishes: its share of 0c4, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 0c4-1 | 100.0% | 13.67 | 0.08% | 0.87% | 6.7% | 36% |

**2c4**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 2c4-1 | both on one layer, adjacent | 7–10 | 2c3 | the two diagonals of the back face agree (see the note under the table) |
| 2c4-2 | 1 up 1 down, opposite | 8–10 | 4b3 |  |
| 2c4-3 | both on one layer, adjacent | 7–10 | 2c3 | the two diagonals of the back face differ (see the note under the table) |
| 2c4-4 | both on one layer, adjacent | 8–11 | nothing, needs a setup |  |
| 2c4-5 | 1 up 1 down, stacked | 9–11 | 4b3 |  |
| 2c4-6 | 1 up 1 down, opposite | 8–11 | nothing, needs a setup |  |
| 2c4-7 | 1 up 1 down, stacked | 9–12 | nothing, needs a setup |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 2c4-1 | `R2 D' B2 F2 L2 D' B2 U B2 D' B2 F2 U2` | 13 | `U F2 U L2 U' F2 U'` |
| 2c4-2 | `R2 B2 F2 U' L2 D2 B2 U' F2 L2 U' L2 U'` | 13 | `U' F2 U' L2 U R2 U F2` |
| 2c4-3 | `F2 U' B2 D' L2 D' L2 U B2 R2 U L2 F2 U'` | 14 | `D F2 U' F2 U R2 U'` |
| 2c4-4 | `B2 D2 R2 U F2 U L2 U' R2 D2 R2 F2 U' R2` | 14 | `U' R2 U' R2 U F2 U' F2` |
| 2c4-5 | `B2 U B2 U2 B2 F2 R2 D B2 L2 U' B2 R2 U'` | 14 | `D F2 U2 R2 U F2 U' F2 U` |
| 2c4-6 | `U' L2 D B2 U2 B2 L2 F2 U' L2 B2 D2 U' R2` | 14 | `U' R2 U F2 U' R2 U R2` |
| 2c4-7 | `U F2 U' L2 F2 D B2 R2 F2 D2 B2 U' F2 U2` | 14 | `U F2 D' L2 U F2 U' F2 U2` |

How each case finishes: its share of 2c4, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 2c4-1 | 16.7% | 13.27 | 0.48% | 3.1% | 16% | 57% |
| 2c4-2 | 8.3% | 13.39 | 0.31% | 2.3% | 13% | 51% |
| 2c4-3 | 16.7% | 13.45 | 0.38% | 2.4% | 13% | 47% |
| 2c4-4 | 16.7% | 13.77 | 0.15% | 1.1% | 7.0% | 33% |
| 2c4-5 | 8.3% | 13.77 | 0.13% | 1.1% | 7.0% | 33% |
| 2c4-6 | 16.7% | 13.80 | 0.13% | 0.99% | 6.4% | 31% |
| 2c4-7 | 16.7% | 14.01 | 0.04% | 0.52% | 4.1% | 23% |

**Telling the two look-alike 2c4 cases apart.** Hold the cube so the two bad corners are on the front edge of one layer (if you see six bad corners, turn both layers, U D', and you will see two). The four corners of the back face are then all good. Take each diagonal of the back face. Its two corners share exactly one colour: their sticker on the back face, their U/D sticker, or their sticker on the side. If both diagonals share the same kind of sticker, the diagonals agree; otherwise they differ.

2c4, corner case on both sides. Each row is a pair of cases, one on normal and one on inverse, in either order:

| Cases on the two sides | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 2c4-1 and 2c4-1 | 2.8% | 12.93 | 0.92% | 5.6% | 26% | 75% |
| 2c4-1 and 2c4-2 | 2.8% | 13.01 | 0.68% | 4.4% | 23% | 72% |
| 2c4-3 and 2c4-1 | 5.6% | 13.11 | 0.72% | 4.3% | 20% | 65% |
| 2c4-2 and 2c4-2 | 0.7% | 13.15 | 0.37% | 3.2% | 18% | 65% |
| 2c4-3 and 2c4-2 | 2.8% | 13.17 | 0.56% | 3.5% | 18% | 62% |
| 2c4-3 and 2c4-3 | 2.8% | 13.32 | 0.55% | 3.1% | 15% | 54% |
| 2c4-1 and 2c4-5 | 2.8% | 13.32 | 0.32% | 2.3% | 14% | 54% |
| 2c4-4 and 2c4-1 | 5.6% | 13.40 | 0.32% | 2.2% | 12% | 50% |
| 2c4-1 and 2c4-6 | 5.6% | 13.44 | 0.28% | 1.9% | 12% | 48% |
| 2c4-3 and 2c4-5 | 2.8% | 13.47 | 0.29% | 1.9% | 11% | 46% |
| 2c4-4 and 2c4-2 | 2.8% | 13.49 | 0.19% | 1.7% | 10% | 45% |
| 2c4-5 and 2c4-2 | 1.4% | 13.53 | 0.09% | 1.3% | 9.1% | 43% |
| 2c4-6 and 2c4-2 | 2.8% | 13.54 | 0.17% | 1.4% | 9.1% | 42% |
| 2c4-1 and 2c4-7 | 5.6% | 13.59 | 0.12% | 1.2% | 8.4% | 40% |
| 2c4-4 and 2c4-3 | 5.6% | 13.60 | 0.26% | 1.6% | 9.3% | 40% |
| 2c4-3 and 2c4-6 | 5.6% | 13.63 | 0.21% | 1.5% | 8.7% | 38% |
| 2c4-3 and 2c4-7 | 5.6% | 13.73 | 0.11% | 1.1% | 6.8% | 33% |
| 2c4-7 and 2c4-2 | 2.8% | 13.78 | 0.02% | 0.49% | 5.1% | 30% |
| 2c4-4 and 2c4-5 | 2.8% | 13.82 | 0.05% | 0.75% | 5.4% | 29% |
| 2c4-6 and 2c4-5 | 2.8% | 13.87 | 0.05% | 0.69% | 4.9% | 27% |
| 2c4-4 and 2c4-4 | 2.8% | 13.90 | 0.09% | 0.77% | 5.0% | 26% |
| 2c4-4 and 2c4-6 | 5.6% | 13.95 | 0.08% | 0.64% | 4.4% | 24% |
| 2c4-6 and 2c4-6 | 2.8% | 13.98 | 0.07% | 0.55% | 3.9% | 23% |
| 2c4-4 and 2c4-7 | 5.6% | 14.09 | <0.01% | 0.26% | 2.8% | 19% |
| 2c4-6 and 2c4-7 | 5.6% | 14.11 | <0.01% | 0.25% | 2.7% | 18% |
| 2c4-5 and 2c4-5 | 0.7% | 14.13 | 0 | 0.18% | 2.5% | 18% |
| 2c4-7 and 2c4-5 | 2.8% | 14.33 | 0 | 0.07% | 1.3% | 12% |
| 2c4-7 and 2c4-7 | 2.8% | 14.49 | 0 | 0.03% | 0.63% | 7.5% |

**4c4**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 4c4-1 | 2-2, diagonal over diagonal | 9–10 | 4a3 |  |
| 4c4-2 | 2-2, pairs sharing one column | 9–11 | 4a3 |  |
| 4c4-3 | 2-2, pairs stacked | 10–11 | nothing, needs a setup |  |
| 4c4-4 | 3-1 | 10–12 | nothing, needs a setup |  |
| 4c4-5 | 2-2, pairs on opposite sides | 11–12 | nothing, needs a setup |  |
| 4c4-6 | 4-0 | 11–12 | 0c3 |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 4c4-1 | `L2 B2 D2 B2 D' L2 B2 D B2 U2 R2 U' R2 U'` | 14 | `U' R2 U' R2 U2 F2 U R2 U` |
| 4c4-2 | `F2 U B2 R2 U' R2 D2 F2 D' B2 R2 U2 R2 U'` | 14 | `U' R2 U' F2 U2 R2 U R2 U` |
| 4c4-3 | `B2 L2 F2 U' R2 U F2 U' L2 D L2 U L2 D` | 14 | `U L2 D' B2 U2 R2 U F2 U' R2` |
| 4c4-4 | `U' F2 D' L2 B2 D2 F2 U F2 R2 U2 R2 U F2 R2` | 15 | `D' R2 D' B2 U2 R2 U R2 U' R2` |
| 4c4-5 | `R2 B2 D R2 U' B2 U' F2 D F2 U' F2 U L2 U2` | 15 | `D B2 U' L2 U2 F2 U R2 U' R2 U2` |
| 4c4-6 | `B2 U R2 F2 D2 F2 D' F2 R2 D2 R2 D' F2 R2 U'` | 15 | `D F2 U2 R2 U F2 U2 R2 U F2 U` |

How each case finishes: its share of 4c4, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4c4-1 | 8.3% | 13.97 | 0.08% | 0.63% | 4.3% | 23% |
| 4c4-2 | 16.7% | 14.25 | 0.04% | 0.33% | 2.5% | 15% |
| 4c4-3 | 16.7% | 14.27 | 0.01% | 0.20% | 1.9% | 13% |
| 4c4-4 | 33.3% | 14.48 | <0.01% | 0.11% | 1.2% | 9.3% |
| 4c4-5 | 16.7% | 14.60 | 0 | 0.03% | 0.59% | 6.0% |
| 4c4-6 | 8.3% | 14.71 | 0 | 0.03% | 0.57% | 5.6% |

4c4, corner case on both sides. Each row is a pair of cases, one on normal and one on inverse, in either order:

| Cases on the two sides | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4c4-2 and 4c4-1 | 5.6% | 13.87 | 0.17% | 0.92% | 5.6% | 28% |
| 4c4-4 and 4c4-1 | 11.1% | 14.01 | 0.03% | 0.49% | 3.7% | 21% |
| 4c4-2 and 4c4-3 | 11.1% | 14.14 | 0.03% | 0.43% | 2.9% | 17% |
| 4c4-4 and 4c4-3 | 22.2% | 14.33 | 0 | 0.08% | 1.3% | 11% |
| 4c4-5 and 4c4-2 | 11.1% | 14.43 | 0 | 0.07% | 1.1% | 9.4% |
| 4c4-6 and 4c4-2 | 5.6% | 14.50 | 0 | 0.08% | 1.3% | 9.5% |
| 4c4-4 and 4c4-5 | 22.2% | 14.69 | 0 | 0.01% | 0.33% | 4.3% |
| 4c4-6 and 4c4-4 | 11.1% | 14.81 | 0 | 0 | 0.20% | 3.7% |

**2c5**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 2c5-1 | both on one layer, adjacent | 9–12 | 2c4 |  |
| 2c5-2 | 1 up 1 down, opposite | 10–13 | 4b4 |  |
| 2c5-3 | 1 up 1 down, stacked | 11–13 | 4b4 |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 2c5-1 | `D' R2 D R2 U2 L2 D' F2 U' R2 U F2 L2 U2` | 14 | `U R2 U F2 U' F2 U R2 U` |
| 2c5-2 | `B2 D U2 F2 U L2 U R2 U2 L2 U' F2 U' R2` | 14 | `D B2 U' R2 U F2 U' R2 U R2` |
| 2c5-3 | `B2 D' B2 D' B2 R2 D2 L2 U' F2 D F2 L2 U R2` | 15 | `D F2 U' F2 U F2 U' F2 U R2 U2` |

How each case finishes: its share of 2c5, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 2c5-1 | 50.0% | 14.12 | 0.05% | 0.45% | 3.4% | 19% |
| 2c5-2 | 25.0% | 14.34 | 0.01% | 0.20% | 1.9% | 13% |
| 2c5-3 | 25.0% | 14.72 | 0 | 0.03% | 0.62% | 6.0% |

2c5, corner case on both sides. Each row is a pair of cases, one on normal and one on inverse, in either order:

| Cases on the two sides | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 2c5-1 and 2c5-1 | 25.0% | 13.95 | 0.08% | 0.69% | 4.7% | 25% |
| 2c5-1 and 2c5-2 | 25.0% | 14.15 | 0.02% | 0.35% | 2.9% | 18% |
| 2c5-2 and 2c5-2 | 6.3% | 14.38 | 0 | 0.09% | 1.4% | 11% |
| 2c5-1 and 2c5-3 | 25.0% | 14.44 | 0 | 0.06% | 1.1% | 9.5% |
| 2c5-2 and 2c5-3 | 12.5% | 14.69 | 0 | 0 | 0.24% | 4.5% |
| 2c5-3 and 2c5-3 | 6.3% | 15.31 | 0 | 0 | 0 | 0.64% |

**4b5**. Each row is one corner case: what it looks like.

| Case | Bad corners | L | A qt takes it straight to | Told apart from a look-alike by |
|---|---|---|---|---|
| 4b5-1 | 3-1 | 9–12 | 2c4 |  |
| 4b5-2 | 2-2, pairs sharing one column | 10–12 | 4a4 |  |

The same cases with a typical DR and the shortest setup of their corners:

| Case | A typical DR | Its optimal, moves | Shortest setup of these corners |
|---|---|---:|---|
| 4b5-1 | `D' L2 F2 U' B2 D B2 L2 D B2 F2 R2 D' U2` | 14 | `U' L2 D F2 U' R2 U F2 U` |
| 4b5-2 | `R2 D' L2 U L2 U' B2 U L2 F2 U' L2 B2 D2` | 14 | `D F2 U R2 U' R2 U R2 U F2` |

How each case finishes: its share of 4b5, its average optimal, and the share finishing in 10, 11, 12 and 13 or less.

| Case | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4b5-1 | 66.7% | 14.23 | 0.02% | 0.25% | 2.2% | 15% |
| 4b5-2 | 33.3% | 14.37 | <0.01% | 0.12% | 1.3% | 11% |

4b5, corner case on both sides. Each row is a pair of cases, one on normal and one on inverse, in either order:

| Cases on the two sides | Share of the subset | Average optimal, moves | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 4b5-1 and 4b5-1 | 44.4% | 14.19 | 0.03% | 0.30% | 2.6% | 17% |
| 4b5-1 and 4b5-2 | 44.4% | 14.31 | <0.01% | 0.16% | 1.6% | 12% |
| 4b5-2 and 4b5-2 | 11.1% | 14.48 | 0 | 0.03% | 0.75% | 7.9% |
