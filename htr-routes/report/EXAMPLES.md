# Worked examples: which HTR routes to try from a DR

Examples to play along with the write-up ([WRITEUP.md](WRITEUP.md)). Find the finish yourself, then open the answer.

These are 200 DR states, the first 10 of the study's uniform sample in each of the 20 most common subsets with their edge counts (together 93% of all DR states). Nothing is picked by hand, so they are as hard or as easy as real DRs of that subset. Each scramble is a random DR followed by DR moves to the state, so it doesn't give the finish away.

**How to read it.** Finishes stay in DR (U, D, R2, L2, F2, B2); optimal means the shortest such finish, E slice solved. A route class like `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` is the corner subset at the start and after each quarter turn until HTR, in the first study's names (4a3 and 4b3 by side: they swap on inverse); the part in brackets is done on the other side after a NISS switch. A class ending in `| qt` has a quarter turn after HTR (an HTR-breaking finish); every other class finishes in half turns from HTR. The checklist of each subset is the one in the write-up (greedy order, HTR budget 2, target optimal), with the share of the subset's 25,000 sampled states it covers after each class. A class *finds an optimal here* if some optimal finish can be read in that class with an HTR at most 2 moves longer than this DR's shortest NISS HTR (first answer), or with any HTR (second). The HTR length counts the moves on both sides until HTR. NISS is written as usual: `R2 U (D F2)` is `R2 U` on normal and `D F2` on the inverse; "normal first" says which side you start on. The finish "as read on normal" is the same finish written linearly.

The bounding lines give the shortest reduction that keeps an optimal finish: moves on normal and (on inverse), each empty or ending in a quarter turn, after which the DR is one quarter turn from HTR (4a1 4e) or two (4a2, 4b2, or a 0c0 with bad edges), and the rest of the optimal finish from there, with exactly that many quarter turns. This is the one-quarter-turn reading of the write-up's bounding section (what JTuu's simulation measured); the method as the bounding docs state it, finishing the reduced state optimally with any number of quarter turns, can occasionally do it with a shorter reduction.

**Replay check.** Every move sequence on this page was replayed on the sticker model before the page was written: 3,829 checks (each scramble gives the state and its labels on both sides, every optimal finish solves it in the stated length, each printed reading has the stated class and HTR length when re-simulated move by move, each reduction leads to a state of the stated kind that the rest solves; the classes found agree with the main run on every state, and the 1q reduction length with the bounding run's one-quarter-turn reading), 0 mismatches.

**In these 200**, the subset's checklist finds an optimal finish (HTR within 2) after its first k classes on: 1: 124 (62%), 2: 155 (78%), 3: 162 (81%), 4: 169 (84%), 5: 171 (86%) states. With any HTR: 1: 151, 2: 182, 3: 189, 4: 192, 5: 192.

## 2c5

### 2c5 2e

1.74% of all DR states.

**2c5 2e, example 1.** `F2 D R2 D B2 U2 D R2 D L2 U F2 U' L2 D F2 D B2 U F2 U L2 D`

Read as 2c5 2e on normal, 2c5 2e on inverse. Shortest HTR: 9 on normal, 12 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (23 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.8% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.2% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.0% | no / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / yes |
| 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.9% | no / no |

- Class 1: normal first: `U L2 U`, then on inverse `(B2 U B2 D' B2 D' L2 U2 R2 B2 L2 R2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U L2 U R2 L2 B2 R2 U2 L2 D B2 D B2 U' B2`.
- Class 2: linear on normal: `U R2 U' F2 D L2 U' B2 R2 U' R2 L2 B2 U2 R2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U R2 U' F2 D L2 U' B2 R2 U' R2 L2 B2 U2 R2`.
- Class 3: normal first: `U`, then on inverse `(L2 D2 B2 D F2 U' F2 D B2 F2 L2 U' R2 F2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U F2 R2 U L2 F2 B2 D' F2 U F2 D' B2 D2 L2`.
- Class 4: inverse first: `(B2 U B2 U')`, then on normal `U L2 U' R2 F2 U2 F2 D' R2 F2 B2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U L2 U' R2 F2 U2 F2 D' R2 F2 B2 U B2 U' B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U R2 U' F2 D L2 U'`; the reduced state is then solved by `B2 R2 U' R2 L2 B2 U2 R2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 5 moves, `U R2 U' F2 D`; the reduced state is then solved by `L2 U' B2 R2 U' R2 L2 B2 U2 R2` (10 moves, 2 quarter turns).

</details>

**2c5 2e, example 2.** `U' L2 F2 D R2 L2 U F2 D2 F2 D2 F2 U' R2 U' R2 L2 U2 L2 U' F2 U'`

Read as 2c5 2e on normal, 2c5 2e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (37 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.8% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.2% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.0% | no / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / yes |
| 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.9% | no / no |

- Class 1: inverse first: `(D' B2 L2 D)`, then on normal `R2 U' B2 D' F2 U' D2 R2 L2 B2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `R2 U' B2 D' F2 U' D2 R2 L2 B2 D' L2 B2 D`.
- Class 2: linear on the inverse: `(R2 U' L2 D B2 D' F2 D L2 B2 U' L2 D2 R2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 D2 L2 U B2 L2 D' F2 D B2 D' L2 U R2`.
- Class 3: normal first: `U'`, then on inverse `(U' R2 B2 U' R2 B2 F2 U L2 U B2 D2 F2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' F2 D2 B2 U' L2 U' F2 B2 R2 U B2 R2 U`.
- Class 4: normal first: `R2 B2 U R2 U`, then on inverse `(U' B2 D R2 B2 U2 B2 D R2)`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U R2 U R2 D' B2 U2 B2 R2 D' B2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `R2 U' B2 D' F2 U (D)`; the reduced state is then solved by `R2 L2 F2 D' R2 F2 U2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `U' (U' R2 B2 U')`; the reduced state is then solved by `F2 D2 B2 U' L2 U' F2 B2 R2` (9 moves, 2 quarter turns).

</details>

**2c5 2e, example 3.** `F2 U2 D F2 U B2 D' R2 B2 U' R2 D' L2 F2 D' F2 B2 L2 F2 U'`

Read as 2c5 2e on normal, 2c5 2e on inverse. Shortest HTR: 11 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (5 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.8% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.2% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.0% | no / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / yes |
| 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.9% | no / no |

- Class 1: inverse first: `(D R2 D')`, then on normal `B2 D F2 U' F2 U' R2 B2 D2 R2 F2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `B2 D F2 U' F2 U' R2 B2 D2 R2 F2 D R2 D'`.
- Class 2: linear on the inverse: `(D' R2 D B2 D' R2 D F2 D B2 R2 U2 F2 L2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `L2 F2 U2 R2 B2 D' F2 D' R2 D B2 D' R2 D`.
- Class 3: normal first: `D2 F2 U`, then on inverse `(D' B2 R2 D B2 L2 D L2 U' F2 R2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D2 F2 U R2 F2 U L2 D' L2 B2 D' R2 B2 D`.
- Class 4: normal first: `D R2 U'`, then on inverse `(L2 F2 U' F2 U' F2 R2 D2 L2 U' F2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D R2 U' F2 U L2 D2 R2 F2 U F2 U F2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `(D' R2 D B2 D' R2 D)`; the reduced state is then solved by `L2 F2 U2 R2 B2 D' F2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `D R2 U' F2 U`; the reduced state is then solved by `L2 D2 R2 F2 U F2 U F2 L2` (9 moves, 2 quarter turns).

</details>

**2c5 2e, example 4.** `U D2 R2 U' D2 R2 U2 D F2 B2 R2 D R2 D' L2 U R2 U2 B2 R2 F2 D' B2`

Read as 2c5 2e on normal, 2c5 2e on inverse. Shortest HTR: 11 on normal, 11 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (16 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.8% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.2% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.0% | no / no |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | yes / yes |
| 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.9% | no / no |

- Class 1: normal first: `U2 R2 F2 U' B2 U'`, then on inverse `(U R2 D' L2 U F2 R2 U2 L2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U2 R2 F2 U' B2 U' L2 U2 R2 F2 U' L2 D R2 U'`.
- Class 2: linear on normal: `U2 R2 F2 U' B2 U' L2 U2 R2 F2 U' L2 D R2 U'`. HTR after 15 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U2 R2 F2 U' B2 U' L2 U2 R2 F2 U' L2 D R2 U'`.
- Class 4: normal first: `L2 U' L2 U'`, then on inverse `(U L2 D F2 D2 R2 D' R2 U2 R2 B2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `L2 U' L2 U' B2 R2 U2 R2 D R2 D2 F2 D' L2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `L2 U' L2 U (U L2 U)`; the reduced state is then solved by `R2 U2 B2 U' F2 D2 B2 L2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `(U R2 D' L2 U)`; the reduced state is then solved by `U2 R2 F2 U' B2 U' L2 U2 R2 F2` (10 moves, 2 quarter turns).

</details>

**2c5 2e, example 5.** `D' B2 R2 U' D2 F2 D B2 R2 U2 F2 U B2 U F2 B2 U' L2 F2 U2 D'`

Read as 2c5 2e on normal, 2c5 2e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.8% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.2% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.0% | no / no |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / yes |
| 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.9% | no / no |

- Class 1: inverse first: `(F2 D B2 D)`, then on normal `B2 U F2 U B2 U R2 D2 B2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `B2 U F2 U B2 U R2 D2 B2 D' B2 D' F2`.
- Class 2: linear on the inverse: `(F2 D B2 D B2 D2 R2 U' B2 U' F2 U' B2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U F2 U B2 U R2 D2 B2 D' B2 D' F2`.
- Class 4: normal first: `B2 U F2 U`, then on inverse `(F2 D B2 D B2 D2 R2 U' B2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U F2 U B2 U R2 D2 B2 D' B2 D' F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `B2 U F2 U (F2 D B2 D)`; the reduced state is then solved by `B2 U R2 D2 B2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `B2 U (F2 D B2 D)`; the reduced state is then solved by `F2 U B2 U R2 D2 B2` (7 moves, 2 quarter turns).

</details>

**2c5 2e, example 6.** `L2 U R2 U' D2 F2 U2 R2 U' D2 R2 F2 U L2 U' R2 B2 U F2 D'`

Read as 2c5 2e on normal, 2c5 2e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (14 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.8% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.2% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.0% | yes / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / no |
| 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.9% | no / no |

- Class 1: normal first: `R2 F2 U B2 U'`, then on inverse `(R2 D B2 R2 U L2 U D2 F2)`. HTR after 12 moves (within the budget); the whole finish, as read on normal: `R2 F2 U B2 U' F2 D2 U' L2 U' R2 B2 D' R2`.
- Class 2: linear on the inverse: `(R2 U R2 F2 D L2 U' B2 D R2 D U2 F2 R2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `R2 F2 U2 D' R2 D' B2 U L2 D' F2 R2 U' R2`.
- Class 3: inverse first: `(R2 U)`, then on normal `R2 F2 U B2 D' L2 U F2 U D2 F2 R2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `R2 F2 U B2 D' L2 U F2 U D2 F2 R2 U' R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `R2 F2 U B2 U' F2 U' (R2 D)`; the reduced state is then solved by `D2 L2 U' R2 B2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 7 moves, `R2 F2 U B2 U' (R2 D)`; the reduced state is then solved by `F2 U' D2 L2 U' R2 B2` (7 moves, 2 quarter turns).

</details>

**2c5 2e, example 7.** `U' D L2 U' F2 U' F2 U2 D B2 U F2 R2 D2 L2 D F2 R2 D' L2 U' R2`

Read as 2c5 2e on normal, 2c5 2e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (97 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.8% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.2% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.0% | yes / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / yes |
| 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.9% | no / no |

- Class 1: normal first: `U B2 D'`, then on inverse `(R2 U R2 U B2 U B2 D2 B2 L2 B2 F2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U B2 D' F2 B2 L2 B2 D2 B2 U' B2 U' R2 U' R2`.
- Class 2: linear on normal: `R2 U' R2 U' R2 B2 D' B2 D R2 D B2 R2 F2 D2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `R2 U' R2 U' R2 B2 D' B2 D R2 D B2 R2 F2 D2`.
- Class 3: normal first: `U`, then on inverse `(F2 D' R2 B2 D L2 D' F2 D L2 F2 L2 F2 D2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U D2 F2 L2 F2 L2 D' F2 D L2 D' B2 R2 D F2`.
- Class 4: inverse first: `(R2 D B2 U)`, then on normal `U B2 D F2 L2 U2 L2 U R2 F2 B2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 D F2 L2 U2 L2 U R2 F2 B2 U' B2 D' R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U (F2 D' F2 U' B2 D)`; the reduced state is then solved by `D2 L2 B2 U' F2 B2 L2 F2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 4 moves, `U B2 U (U)`; the reduced state is then solved by `B2 L2 D F2 R2 U' R2 L2 F2 U2 B2` (11 moves, 2 quarter turns).

</details>

**2c5 2e, example 8.** `D2 L2 U' D' R2 U L2 D F2 U' F2 D B2 L2 D L2 D' L2 F2 U F2 R2 F2`

Read as 2c5 2e on normal, 2c5 2e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (25 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.8% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.2% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.0% | yes / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / no |
| 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.9% | no / no |

- Class 1: inverse first: `(D F2 L2 U')`, then on normal `F2 D F2 L2 U L2 D F2 L2 U2 F2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `F2 D F2 L2 U L2 D F2 L2 U2 F2 U L2 F2 D'`.
- Class 2: linear on the inverse: `(U B2 U F2 D' B2 R2 D' B2 D' B2 F2 L2 U2 B2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `B2 U2 L2 F2 B2 D B2 D R2 B2 D F2 U' B2 U'`.
- Class 3: normal first: `L2 B2 U`, then on inverse `(D R2 D' B2 R2 U' R2 U' B2 R2 D2 B2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `L2 B2 U B2 D2 R2 B2 U R2 U R2 B2 D R2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `R2 F2 D B2 U' R2 U (D)`; the reduced state is then solved by `B2 R2 D' F2 D2 R2 F2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `(U B2 U F2 D')`; the reduced state is then solved by `B2 U2 L2 F2 B2 D B2 D R2 B2` (10 moves, 2 quarter turns).

</details>

**2c5 2e, example 9.** `U F2 U2 D' R2 L2 B2 D2 F2 B2 D' F2 L2 D B2 U B2 U2 F2 R2 U F2 L2 D'`

Read as 2c5 2e on normal, 2c5 2e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.8% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.2% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.0% | no / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / no |
| 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.9% | no / no |

- Class 1: normal first: `D2 R2 D R2 U'`, then on inverse `(R2 B2 D R2 U' F2 U R2 B2)`. HTR after 12 moves (within the budget); the whole finish, as read on normal: `D2 R2 D R2 U' B2 R2 U' F2 U R2 D' B2 R2`.
- Class 2: linear on normal: `D2 F2 D' B2 D F2 U' R2 U F2 U' R2 B2 R2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `D2 F2 D' B2 D F2 U' R2 U F2 U' R2 B2 R2`.
- Class 3: normal first: `D2 R2 D`, then on inverse `(R2 B2 D R2 U' F2 U R2 B2 U R2)`. HTR after 13 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D2 R2 D R2 U' B2 R2 U' F2 U R2 D' B2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `D2 F2 D' B2 D F2 U' R2 U`; the reduced state is then solved by `F2 U' R2 B2 R2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 7 moves, `(R2 B2 D R2 U' F2 U)`; the reduced state is then solved by `D2 R2 D R2 U' B2 R2` (7 moves, 2 quarter turns).

</details>

**2c5 2e, example 10.** `U L2 U' D L2 D2 F2 U' D' B2 U2 R2 L2 U F2 U2 D' L2 U' F2 U B2 R2`

Read as 2c5 2e on normal, 2c5 2e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.8% | no / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.2% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.0% | no / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / no |
| 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.9% | no / no |

- Class 1: normal first: `B2 U' F2 L2 U`, then on inverse `(F2 L2 R2 D' R2 U' L2 D R2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U' F2 L2 U R2 D' L2 U R2 D R2 L2 F2`.
- Class 2: linear on normal: `B2 U' F2 L2 U R2 D' L2 U R2 D R2 L2 F2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `B2 U' F2 L2 U R2 D' L2 U R2 D R2 L2 F2`.
- Class 3: normal first: `B2 U'`, then on inverse `(F2 L2 R2 D' R2 U' L2 D R2 U' L2 F2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U' F2 L2 U R2 D' L2 U R2 D R2 L2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `B2 U' F2 L2 U R2 D' L2 U`; the reduced state is then solved by `R2 D R2 L2 F2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 7 moves, `B2 U' F2 L2 U R2 D'`; the reduced state is then solved by `L2 U R2 D R2 L2 F2` (7 moves, 2 quarter turns).

</details>

### 2c5 4e

3.92% of all DR states.

**2c5 4e, example 1.** `B2 L2 D2 F2 U' B2 U L2 U' B2 D' F2 L2 B2 D' R2 U2 D' B2 U B2 R2`

Read as 2c5 4e on normal, 2c5 4e on inverse. Shortest HTR: 11 on normal, 11 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (10 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 71.5% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.0% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.9% | no / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 93.2% | no / yes |
| 5 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 93.4% | no / no |

- Class 1: normal first: `R2 D' L2 F2 D'`, then on inverse `(L2 U' F2 U L2 U R2 D2 L2 F2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `R2 D' L2 F2 D' F2 L2 D2 R2 U' L2 U' F2 U L2`.
- Class 2: linear on normal: `F2 R2 U L2 F2 D' L2 D R2 D' R2 B2 D' L2 D2`. HTR after 13 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 R2 U L2 F2 D' L2 D R2 D' R2 B2 D' L2 D2`.
- Class 3: normal first: `F2 R2 U`, then on inverse `(D2 L2 D B2 R2 D R2 D' L2 D F2 L2)`. HTR after 13 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 R2 U L2 F2 D' L2 D R2 D' R2 B2 D' L2 D2`.
- Class 4: inverse first: `(D R2 U')`, then on normal `B2 U' L2 F2 B2 U' L2 U2 F2 D R2 F2`. HTR after 13 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U' L2 F2 B2 U' L2 U2 F2 D R2 F2 U R2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `B2 U (D' F2 U R2 U')`; the reduced state is then solved by `R2 F2 B2 U F2 U2 F2 R2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `(D' F2 U R2 U')`; the reduced state is then solved by `B2 U R2 F2 B2 U F2 U2 F2 R2` (10 moves, 2 quarter turns).

</details>

**2c5 4e, example 2.** `D R2 L2 D' B2 D' F2 D2 F2 U F2 U R2 B2 D2 F2 U F2 U L2 F2 U' D' F2`

Read as 2c5 4e on normal, 2c5 4e on inverse. Shortest HTR: 12 on normal, 11 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (10 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 71.5% | no / no |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.0% | no / no |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.9% | no / no |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 93.2% | yes / yes |
| 5 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 93.4% | no / no |

- Class 4: inverse first: `(U F2 D)`, then on normal `U L2 D R2 U2 B2 D' L2 F2 U2 B2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U L2 D R2 U2 B2 D' L2 F2 U2 B2 D' F2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `U L2 D (U F2 D)`; the reduced state is then solved by `R2 U2 B2 D' L2 F2 U2 B2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 4 moves, `U (U F2 D)`; the reduced state is then solved by `L2 D R2 U2 B2 D' L2 F2 U2 B2` (10 moves, 2 quarter turns).

</details>

**2c5 4e, example 3.** `U' D2 B2 U D' F2 U2 D R2 D F2 D2 B2 R2 D F2 L2 D' B2 D L2 U R2`

Read as 2c5 4e on normal, 2c5 4e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (10 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 71.5% | no / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.0% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.9% | yes / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 93.2% | no / no |
| 5 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 93.4% | no / no |

- Class 1: normal first: `L2 B2 U' R2 L2 B2 U`, then on inverse `(U L2 B2 D' F2 D F2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 U' R2 L2 B2 U F2 D' F2 D B2 L2 U'`.
- Class 2: linear on the inverse: `(U L2 B2 D' F2 D F2 U' B2 L2 R2 U B2 L2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 U' R2 L2 B2 U F2 D' F2 D B2 L2 U'`.
- Class 3: normal first: `L2 B2 U'`, then on inverse `(U L2 B2 D' F2 D F2 U' B2 L2 R2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `L2 B2 U' R2 L2 B2 U F2 D' F2 D B2 L2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `(U L2 B2 D' F2 D F2 U')`; the reduced state is then solved by `L2 B2 U' R2 L2 B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `(U L2 B2 D' F2 D)`; the reduced state is then solved by `L2 B2 U' R2 L2 B2 U F2` (8 moves, 2 quarter turns).

</details>

**2c5 4e, example 4.** `L2 U2 D R2 B2 L2 U L2 U F2 U' B2 U2 F2 R2 D' B2 D L2 D R2 U L2 U'`

Read as 2c5 4e on normal, 2c5 4e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 71.5% | no / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.0% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.9% | yes / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 93.2% | no / no |
| 5 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 93.4% | no / no |

- Class 1: normal first: `F2 U L2 F2 D'`, then on inverse `(R2 U L2 F2 U' F2 U' B2 U2 B2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U L2 F2 D' B2 U2 B2 U F2 U F2 L2 U' R2`.
- Class 2: linear on normal: `U' R2 B2 D2 R2 U B2 R2 D' L2 F2 U' B2 D B2`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U' R2 B2 D2 R2 U B2 R2 D' L2 F2 U' B2 D B2`.
- Class 3: normal first: `U'`, then on inverse `(B2 D' B2 U F2 L2 D R2 B2 U' R2 D2 B2 R2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U' R2 B2 D2 R2 U B2 R2 D' L2 F2 U' B2 D B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `U' (B2 D' B2 U F2 L2 D)`; the reduced state is then solved by `R2 B2 D2 R2 U B2 R2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 5 moves, `U' (B2 D' B2 U)`; the reduced state is then solved by `R2 B2 D2 R2 U B2 R2 D' L2 F2` (10 moves, 2 quarter turns).

</details>

**2c5 4e, example 5.** `U' L2 U L2 U' D' L2 U B2 D' F2 D L2 U R2 B2 D' B2 L2 F2 U2`

Read as 2c5 4e on normal, 2c5 4e on inverse. Shortest HTR: 10 on normal, 11 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 71.5% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.0% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.9% | no / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 93.2% | no / no |
| 5 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 93.4% | no / no |

- Class 1: normal first: `U B2 U'`, then on inverse `(D2 L2 D' B2 D R2 D L2 F2 D2 R2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U B2 U' R2 D2 F2 L2 D' R2 D' B2 D L2 D2`.
- Class 2: linear on normal: `U B2 U' R2 D2 F2 L2 D' R2 D' B2 D L2 D2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 U' R2 D2 F2 L2 D' R2 D' B2 D L2 D2`.
- Class 3: normal first: `U`, then on inverse `(D2 L2 D' B2 D R2 D L2 F2 D2 R2 U B2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 U' R2 D2 F2 L2 D' R2 D' B2 D L2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `U (D2 L2 D' B2 D R2 D)`; the reduced state is then solved by `B2 U' R2 D2 F2 L2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 6 moves, `U (D2 L2 D' B2 D)`; the reduced state is then solved by `B2 U' R2 D2 F2 L2 D' R2` (8 moves, 2 quarter turns).

</details>

**2c5 4e, example 6.** `L2 U2 L2 F2 U2 L2 D' L2 B2 D' F2 B2 L2 F2 D' F2 U F2 U L2`

Read as 2c5 4e on normal, 2c5 4e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (10 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 71.5% | no / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.0% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.9% | yes / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 93.2% | no / no |
| 5 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 93.4% | no / no |

- Class 1: inverse first: `(L2 U' R2 B2 D)`, then on normal `R2 U F2 L2 D L2 D' R2 F2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U F2 L2 D L2 D' R2 F2 D' B2 R2 U L2`.
- Class 2: linear on normal: `R2 U' R2 U' L2 D B2 U' R2 D F2 D2 B2 U2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `R2 U' R2 U' L2 D B2 U' R2 D F2 D2 B2 U2`.
- Class 3: inverse first: `(B2 D)`, then on normal `R2 F2 U F2 U R2 U' F2 D F2 B2 R2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `R2 F2 U F2 U R2 U' F2 D F2 B2 R2 D' B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `R2 U' R2 U' L2 D B2 U'`; the reduced state is then solved by `R2 D F2 D2 B2 U2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `R2 U' R2 U' L2 D`; the reduced state is then solved by `B2 U' R2 D F2 D2 B2 U2` (8 moves, 2 quarter turns).

</details>

**2c5 4e, example 7.** `D' F2 U D F2 U' D' B2 D' R2 U2 R2 F2 B2 R2 U' F2 U' B2 D B2 D B2 U'`

Read as 2c5 4e on normal, 2c5 4e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (4 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 71.5% | no / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.0% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.9% | no / no |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 93.2% | no / yes |
| 5 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 93.4% | no / no |

- Class 1: normal first: `D' R2 U`, then on inverse `(B2 U2 B2 U F2 D F2 L2 U R2 U2 F2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D' R2 U F2 U2 R2 U' L2 F2 D' F2 U' B2 U2 B2`.
- Class 2: linear on normal: `D' R2 U F2 U2 R2 U' L2 F2 D' F2 U' B2 U2 B2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D' R2 U F2 U2 R2 U' L2 F2 D' F2 U' B2 U2 B2`.
- Class 4: inverse first: `(B2 U2 B2 U F2 D)`, then on normal `D' R2 U F2 U2 R2 U' L2 F2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D' R2 U F2 U2 R2 U' L2 F2 D' F2 U' B2 U2 B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `D' R2 U (B2 U2 B2 U F2 D)`; the reduced state is then solved by `F2 U2 R2 U' L2 F2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 7 moves, `D' (B2 U2 B2 U F2 D)`; the reduced state is then solved by `R2 U F2 U2 R2 U' L2 F2` (8 moves, 2 quarter turns).

</details>

**2c5 4e, example 8.** `B2 U' D L2 U' F2 D L2 F2 L2 U R2 D' L2 F2 U F2 U2 F2 L2 U R2 U' R2`

Read as 2c5 4e on normal, 2c5 4e on inverse. Shortest HTR: 9 on normal, 11 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (12 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 71.5% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.0% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.9% | yes / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 93.2% | no / no |
| 5 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 93.4% | no / no |

- Class 1: normal first: `L2 U F2 D`, then on inverse `(B2 U L2 B2 D' F2 U L2 F2 U2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `L2 U F2 D U2 F2 L2 U' F2 D B2 L2 U' B2`.
- Class 2: linear on normal: `U' F2 D' B2 U B2 D' B2 D' L2 B2 R2 U2 R2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U' F2 D' B2 U B2 D' B2 D' L2 B2 R2 U2 R2`.
- Class 3: inverse first: `(R2 U)`, then on normal `U F2 U B2 U' B2 U B2 D2 F2 L2 B2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U F2 U B2 U' B2 U B2 D2 F2 L2 B2 U' R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U F2 U B2 U' (R2 U)`; the reduced state is then solved by `B2 U B2 D2 F2 L2 B2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `U F2 U (R2 U)`; the reduced state is then solved by `B2 U' B2 U B2 D2 F2 L2 B2` (9 moves, 2 quarter turns).

</details>

**2c5 4e, example 9.** `R2 D R2 U D2 R2 U2 D2 B2 R2 L2 D2 B2 U' R2 B2 U2 B2 U' D2 F2 U L2`

Read as 2c5 4e on normal, 2c5 4e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 71.5% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.0% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.9% | no / no |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 93.2% | no / yes |
| 5 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 93.4% | no / no |

- Class 1: inverse first: `(U B2 U')`, then on normal `F2 D F2 D' R2 F2 U L2 D2 R2 B2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `F2 D F2 D' R2 F2 U L2 D2 R2 B2 U B2 U'`.
- Class 2: linear on the inverse: `(U B2 U' B2 R2 D2 L2 U' F2 R2 D F2 D' F2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 D F2 D' R2 F2 U L2 D2 R2 B2 U B2 U'`.
- Class 4: normal first: `F2 D F2 D'`, then on inverse `(U B2 U' B2 R2 D2 L2 U' F2 R2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 D F2 D' R2 F2 U L2 D2 R2 B2 U B2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `F2 D F2 D' (U B2 U')`; the reduced state is then solved by `R2 F2 U L2 D2 R2 B2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 5 moves, `F2 D (U B2 U')`; the reduced state is then solved by `F2 D' R2 F2 U L2 D2 R2 B2` (9 moves, 2 quarter turns).

</details>

**2c5 4e, example 10.** `U F2 U D' R2 B2 D R2 U' D2 F2 R2 F2 D' R2 D B2 U B2 U' F2 U D`

Read as 2c5 4e on normal, 2c5 4e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (15 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 71.5% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.0% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 91.9% | yes / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 93.2% | no / no |
| 5 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 93.4% | no / no |

- Class 1: normal first: `F2 R2 D F2 U`, then on inverse `(U L2 U L2 U B2 L2 U2 R2 F2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `F2 R2 D F2 U F2 R2 U2 L2 B2 U' L2 U' L2 U'`.
- Class 2: linear on normal: `F2 R2 U R2 U2 R2 U' B2 U' B2 D F2 U R2 L2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 R2 U R2 U2 R2 U' B2 U' B2 D F2 U R2 L2`.
- Class 3: normal first: `F2 L2 U`, then on inverse `(U' F2 R2 D F2 D' L2 D' R2 U2 F2 R2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `F2 L2 U R2 F2 U2 R2 D L2 D F2 D' R2 F2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `F2 R2 U' L2 U L2 U' (U)`; the reduced state is then solved by `L2 B2 U L2 F2 D2 L2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `(U L2 U L2 U)`; the reduced state is then solved by `F2 R2 D F2 U F2 R2 U2 L2 B2` (10 moves, 2 quarter turns).

</details>

### 2c5 6e

1.74% of all DR states.

**2c5 6e, example 1.** `U2 L2 D2 B2 U D R2 U D2 F2 U' R2 D R2 F2 B2 U' L2 U' B2 R2 U2`

Read as 2c5 6e on normal, 2c5 6e on inverse. Shortest HTR: 10 on normal, 11 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (20 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.0% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.6% | no / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | yes / yes |
| 5 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.7% | no / no |

- Class 1: normal first: `U' R2 U`, then on inverse `(D' R2 D R2 B2 U' R2 D2 B2 F2 L2 B2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U' R2 U B2 L2 F2 B2 D2 R2 U B2 R2 D' R2 D`.
- Class 2: linear on normal: `D B2 U F2 R2 U F2 L2 D F2 U' B2 D2 L2 F2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `D B2 U F2 R2 U F2 L2 D F2 U' B2 D2 L2 F2`.
- Class 3: inverse first: `(D2 F2 D')`, then on normal `R2 L2 U' F2 D R2 D' L2 F2 D' L2 F2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 L2 U' F2 D R2 D' L2 F2 D' L2 F2 D F2 D2`.
- Class 4: inverse first: `(U' B2 D)`, then on normal `D' F2 D F2 L2 D2 R2 D R2 B2 R2 L2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `D' F2 D F2 L2 D2 R2 D R2 B2 R2 L2 D' B2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `U' R2 U (D' R2 D)`; the reduced state is then solved by `B2 L2 F2 B2 D2 R2 U B2 R2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 4 moves, `U' (D' R2 D)`; the reduced state is then solved by `R2 U B2 L2 F2 B2 D2 R2 U B2 R2` (11 moves, 2 quarter turns).

</details>

**2c5 6e, example 2.** `L2 B2 R2 U' D2 R2 L2 U' R2 U2 L2 F2 U F2 D' B2 R2 U' R2 D L2 D R2 U2`

Read as 2c5 6e on normal, 2c5 6e on inverse. Shortest HTR: 11 on normal, 12 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (55 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.0% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.6% | no / no |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | yes / yes |
| 5 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.7% | no / no |

- Class 1: inverse first: `(U2 R2 U' B2 U)`, then on normal `B2 U F2 U' F2 U' F2 D2 F2 L2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `B2 U F2 U' F2 U' F2 D2 F2 L2 U' B2 U R2 U2`.
- Class 2: linear on the inverse: `(U2 R2 U' B2 U L2 F2 D2 F2 U F2 U F2 U' B2)`. HTR after 14 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U F2 U' F2 U' F2 D2 F2 L2 U' B2 U R2 U2`.
- Class 4: normal first: `U F2 U'`, then on inverse `(D R2 U R2 D2 B2 D B2 F2 R2 U2 F2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U F2 U' F2 U2 R2 F2 B2 D' B2 D2 R2 U' R2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `U F2 U (D R2 U')`; the reduced state is then solved by `R2 B2 U2 B2 D' L2 D2 L2 F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 4 moves, `U (D R2 U')`; the reduced state is then solved by `F2 U R2 B2 U2 B2 D' L2 D2 L2 F2` (11 moves, 2 quarter turns).

</details>

**2c5 6e, example 3.** `D2 R2 U D' F2 D' R2 D R2 B2 D' R2 U F2 U2 L2 F2 L2 D' B2 D' L2 U`

Read as 2c5 6e on normal, 2c5 6e on inverse. Shortest HTR: 12 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.0% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.6% | no / no |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / yes |
| 5 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.7% | no / no |

- Class 1: inverse first: `(F2 D' R2 F2 U)`, then on normal `U' R2 U B2 U' L2 B2 U2 F2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U' R2 U B2 U' L2 B2 U2 F2 U' F2 R2 D F2`.
- Class 2: linear on the inverse: `(F2 D' R2 F2 U F2 U2 B2 L2 U B2 U' R2 U)`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U' R2 U B2 U' L2 B2 U2 F2 U' F2 R2 D F2`.
- Class 4: normal first: `U' R2 U`, then on inverse `(F2 D' R2 F2 U F2 U2 B2 L2 U B2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U' R2 U B2 U' L2 B2 U2 F2 U' F2 R2 D F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U' R2 U B2 U' (F2 D')`; the reduced state is then solved by `L2 B2 U2 F2 U' F2 R2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 5 moves, `U' R2 U (F2 D')`; the reduced state is then solved by `B2 U' L2 B2 U2 F2 U' F2 R2` (9 moves, 2 quarter turns).

</details>

**2c5 6e, example 4.** `U' L2 B2 U R2 U D L2 F2 B2 L2 U L2 D L2 D' B2 U B2 R2 U2 L2 U'`

Read as 2c5 6e on normal, 2c5 6e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.0% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.6% | yes / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / no |
| 5 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.7% | no / no |

- Class 1: normal first: `L2 U' L2 D'`, then on inverse `(L2 F2 D' B2 L2 D' F2 U R2 F2)`. HTR after 12 moves (within the budget); the whole finish, as read on normal: `L2 U' L2 D' F2 R2 U' F2 D L2 B2 D F2 L2`.
- Class 2: linear on normal: `R2 F2 U B2 U' R2 D R2 D' L2 U' L2 F2 R2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `R2 F2 U B2 U' R2 D R2 D' L2 U' L2 F2 R2`.
- Class 3: inverse first: `(L2 F2 D')`, then on normal `L2 U' L2 D' F2 R2 U' F2 D L2 B2`. HTR after 12 moves (within the budget); the whole finish, as read on normal: `L2 U' L2 D' F2 R2 U' F2 D L2 B2 D F2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `R2 F2 U B2 U' R2 D R2 D'`; the reduced state is then solved by `L2 U' L2 F2 R2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 7 moves, `R2 F2 U B2 U' R2 D`; the reduced state is then solved by `R2 D' L2 U' L2 F2 R2` (7 moves, 2 quarter turns).

</details>

**2c5 6e, example 5.** `U' R2 U D' L2 F2 U2 D' F2 D2 L2 D' L2 D L2 D' R2 F2 U' R2 U' L2 B2`

Read as 2c5 6e on normal, 2c5 6e on inverse. Shortest HTR: 10 on normal, 11 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (13 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.0% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.6% | no / no |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | yes / yes |
| 5 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.7% | no / no |

- Class 1: inverse first: `(B2 D2 L2 D R2 U')`, then on normal `U' L2 F2 D R2 U' B2 U2 R2`. HTR after 12 moves (within the budget); the whole finish, as read on normal: `U' L2 F2 D R2 U' B2 U2 R2 U R2 D' L2 D2 B2`.
- Class 2: linear on the inverse: `(B2 D2 L2 D R2 U' R2 U2 B2 U R2 D' F2 L2 U)`. HTR after 15 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U' L2 F2 D R2 U' B2 U2 R2 U R2 D' L2 D2 B2`.
- Class 4: inverse first: `(U F2 U')`, then on normal `U F2 R2 D L2 U2 F2 D' B2 R2 U2 R2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U F2 R2 D L2 U2 F2 D' B2 R2 U2 R2 U F2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U F2 R2 D (U F2 U')`; the reduced state is then solved by `L2 U2 F2 D' B2 R2 U2 R2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 4 moves, `U (U F2 U')`; the reduced state is then solved by `F2 R2 D L2 U2 F2 D' B2 R2 U2 R2` (11 moves, 2 quarter turns).

</details>

**2c5 6e, example 6.** `R2 U D L2 U D' L2 U D F2 D F2 U' R2 B2 U R2 D2 B2 U' F2 U' R2 L2`

Read as 2c5 6e on normal, 2c5 6e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.0% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.6% | no / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / no |
| 5 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.7% | no / no |

- Class 1: inverse first: `(L2 F2 D R2 D)`, then on normal `U R2 U' B2 U' R2 D2 B2 R2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U R2 U' B2 U' R2 D2 B2 R2 D' R2 D' F2 L2`.
- Class 2: linear on normal: `U R2 U' B2 U' R2 D2 B2 R2 D' R2 D' F2 L2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U R2 U' B2 U' R2 D2 B2 R2 D' R2 D' F2 L2`.
- Class 3: normal first: `D`, then on inverse `(F2 U' R2 D' R2 U2 B2 L2 D' R2 U' F2 L2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D L2 F2 U R2 D L2 B2 U2 R2 D R2 U F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `U R2 U' (L2 F2 D R2 D)`; the reduced state is then solved by `B2 U' R2 D2 B2 R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `U R2 U' B2 U'`; the reduced state is then solved by `R2 D2 B2 R2 D' R2 D' F2 L2` (9 moves, 2 quarter turns).

</details>

**2c5 6e, example 7.** `F2 U R2 U' F2 R2 D2 L2 F2 D' R2 D' B2 D F2 D R2 F2 L2 D2 L2 D'`

Read as 2c5 6e on normal, 2c5 6e on inverse. Shortest HTR: 12 on normal, 10 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (11 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.0% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.6% | no / no |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / yes |
| 5 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.7% | no / no |

- Class 1: inverse first: `(R2 U' B2 D)`, then on normal `U' B2 L2 U' R2 U L2 F2 U2 L2 B2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U' B2 L2 U' R2 U L2 F2 U2 L2 B2 D' B2 U R2`.
- Class 2: linear on the inverse: `(D B2 L2 D F2 U2 B2 L2 U F2 U' F2 L2 U' F2)`. HTR after 14 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U L2 F2 U F2 U' L2 B2 U2 F2 D' L2 B2 D'`.
- Class 4: normal first: `U' R2 D`, then on inverse `(B2 L2 D R2 U' F2 U2 F2 L2 U' F2 L2)`. HTR after 13 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' R2 D L2 F2 U L2 F2 U2 F2 U R2 D' L2 B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `B2 D' L2 U B2 U' (U')`; the reduced state is then solved by `L2 U2 F2 U R2 F2 L2 B2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `U' (R2 U' B2 D)`; the reduced state is then solved by `B2 L2 U' R2 U L2 F2 U2 L2 B2` (10 moves, 2 quarter turns).

</details>

**2c5 6e, example 8.** `U2 D' F2 L2 B2 U' D' B2 D' B2 U' R2 D2 R2 B2 U2 D R2 L2 B2 U B2`

Read as 2c5 6e on normal, 2c5 6e on inverse. Shortest HTR: 10 on normal, 11 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (15 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.0% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.6% | no / no |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | yes / yes |
| 5 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.7% | no / no |

- Class 1: inverse first: `(D2 F2 U R2 F2 U)`, then on normal `D' L2 D' L2 D' F2 R2 U2 R2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `D' L2 D' L2 D' F2 R2 U2 R2 U' F2 R2 U' F2 D2`.
- Class 2: linear on the inverse: `(D2 F2 U R2 F2 U R2 U2 R2 F2 D L2 D L2 D)`. HTR after 15 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `D' L2 D' L2 D' F2 R2 U2 R2 U' F2 R2 U' F2 D2`.
- Class 4: normal first: `U R2 U'`, then on inverse `(L2 D B2 R2 U' R2 U2 F2 U R2 U2 B2)`. HTR after 12 moves (within the budget); the whole finish, as read on normal: `U R2 U' B2 U2 R2 U' F2 U2 R2 U R2 B2 D' L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `U R2 U' (L2 D B2 R2 U')`; the reduced state is then solved by `B2 U2 R2 U' F2 U2 R2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 5 moves, `U R2 U' (L2 D)`; the reduced state is then solved by `B2 U2 R2 U' F2 U2 R2 U R2 B2` (10 moves, 2 quarter turns).

</details>

**2c5 6e, example 9.** `R2 B2 R2 L2 B2 U2 R2 L2 D F2 U' F2 D' B2 U F2 L2 U R2 U L2 F2 D L2`

Read as 2c5 6e on normal, 2c5 6e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (4 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.0% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.6% | yes / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / no |
| 5 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.7% | no / no |

- Class 1: inverse first: `(U F2 L2 D')`, then on normal `U L2 B2 D R2 D R2 B2 U2 L2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U L2 B2 D R2 D R2 B2 U2 L2 D L2 F2 U'`.
- Class 2: linear on normal: `L2 D' L2 U B2 U' R2 D' F2 U2 R2 F2 U' B2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 D' L2 U B2 U' R2 D' F2 U2 R2 F2 U' B2`.
- Class 3: inverse first: `(B2 U)`, then on normal `L2 D' L2 U B2 U' R2 D' F2 U2 R2 F2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `L2 D' L2 U B2 U' R2 D' F2 U2 R2 F2 U' B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U L2 B2 D R2 D (U)`; the reduced state is then solved by `R2 B2 U2 L2 D L2 F2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `U (U F2 L2 D')`; the reduced state is then solved by `L2 B2 D R2 D R2 B2 U2 L2` (9 moves, 2 quarter turns).

</details>

**2c5 6e, example 10.** `F2 L2 D F2 U D2 B2 D' F2 B2 D B2 D B2 D2 L2 U L2 U' B2 U R2 U'`

Read as 2c5 6e on normal, 2c5 6e on inverse. Shortest HTR: 10 on normal, 11 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.0% | yes / yes |
| 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | yes / yes |
| 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.6% | no / yes |
| 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` | 92.4% | no / no |
| 5 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 92.7% | no / no |

- Class 1: normal first: `R2 U B2 R2 D'`, then on inverse `(F2 D' F2 U' F2 D' L2 D2 R2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `R2 U B2 R2 D' R2 D2 L2 D F2 U F2 D F2`.
- Class 2: linear on normal: `U F2 R2 U F2 U' R2 B2 D' L2 U' F2 U2 L2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U F2 R2 U F2 U' R2 B2 D' L2 U' F2 U2 L2`.
- Class 3: normal first: `U`, then on inverse `(L2 U2 F2 U L2 D B2 R2 U F2 U' R2 F2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U F2 R2 U F2 U' R2 B2 D' L2 U' F2 U2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `R2 U (F2 D' F2 U' F2 D')`; the reduced state is then solved by `B2 R2 D' R2 D2 L2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `U F2 R2 U F2 U'`; the reduced state is then solved by `R2 B2 D' L2 U' F2 U2 L2` (8 moves, 2 quarter turns).

</details>

## 2c4

### 2c4 2e

5.22% of all DR states.

**2c4 2e, example 1.** `U D F2 R2 F2 U' B2 U D' B2 R2 L2 U' L2 U L2 U L2 F2 U2 R2 B2 D2`

Read as 2c4 2e on normal, 2c4 2e on inverse. Shortest HTR: 9 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (4 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 67.7% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 89.9% | yes / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 90.5% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.8% | no / no |

- Class 1: inverse first: `(U)`, then on normal `L2 U2 R2 F2 U' F2 U' F2 U' L2 D2 R2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `L2 U2 R2 F2 U' F2 U' F2 U' L2 D2 R2 U'`.
- Class 2: linear on the inverse: `(U R2 D2 L2 U F2 U F2 U F2 R2 U2 L2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `L2 U2 R2 F2 U' F2 U' F2 U' L2 D2 R2 U'`.
- Class 3: normal first: `L2 U2 R2 F2 D' L2 U`, then on inverse `(U' R2 D L2 U2 L2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `L2 U2 R2 F2 D' L2 U L2 U2 L2 D' R2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `(U R2 D2 L2 U F2 U)`; the reduced state is then solved by `L2 U2 R2 F2 U' F2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `(U' R2 D)`; the reduced state is then solved by `L2 U2 R2 F2 D' L2 U L2 U2 L2` (10 moves, 2 quarter turns).

</details>

**2c4 2e, example 2.** `D B2 U2 B2 D' F2 B2 D2 R2 U L2 U L2 F2 U D2 L2 D2 L2 F2 L2 U'`

Read as 2c4 2e on normal, 2c4 2e on inverse. Shortest HTR: 9 on normal, 8 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (4 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 67.7% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | no / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 89.9% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 90.5% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.8% | no / no |

- Class 1: inverse first: `(U)`, then on normal `B2 U F2 D L2 D' R2 D2 B2 D2 B2`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `B2 U F2 D L2 D' R2 D2 B2 D2 B2 U'`.
- Class 2: linear on the inverse: `(U B2 D2 B2 D2 R2 D L2 D' F2 U' B2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U F2 D L2 D' R2 D2 B2 D2 B2 U'`.
- Class 3: normal first: `B2 U F2 D`, then on inverse `(U B2 D2 B2 D2 R2 D L2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U F2 D L2 D' R2 D2 B2 D2 B2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `B2 U F2 D (U)`; the reduced state is then solved by `L2 D' R2 D2 B2 D2 B2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `B2 U (U)`; the reduced state is then solved by `F2 D L2 D' R2 D2 B2 D2 B2` (9 moves, 2 quarter turns).

</details>

**2c4 2e, example 3.** `B2 L2 U R2 U B2 D L2 U2 L2 F2 U' B2 U2 B2 L2 U' R2 D2 F2 D' B2 U2`

Read as 2c4 2e on normal, 2c4 2e on inverse. Shortest HTR: 8 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 67.7% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | no / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 89.9% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 90.5% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.8% | no / no |

- Class 1: normal first: `L2 U`, then on inverse `(B2 R2 D L2 D' L2 F2 U F2 R2 D2 L2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `L2 U L2 D2 R2 F2 U' F2 L2 D L2 D' R2 B2`.
- Class 2: linear on normal: `U L2 U B2 R2 U L2 F2 L2 F2 D' R2 U2 L2`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U L2 U B2 R2 U L2 F2 L2 F2 D' R2 U2 L2`.
- Class 3: normal first: `U L2 U`, then on inverse `(L2 U2 R2 D F2 L2 F2 L2 U' R2 B2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U L2 U B2 R2 U L2 F2 L2 F2 D' R2 U2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `U L2 U B2 R2 U`; the reduced state is then solved by `L2 F2 L2 F2 D' R2 U2 L2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 0e here) on an optimal path: 3 moves, `U L2 U`; the reduced state is then solved by `B2 R2 U L2 F2 L2 F2 D' R2 U2 L2` (11 moves, 2 quarter turns).

</details>

**2c4 2e, example 4.** `U' F2 D2 F2 U F2 U D2 L2 U' B2 D' R2 F2 D2 R2 L2 F2 D' L2 U' F2 U`

Read as 2c4 2e on normal, 2c4 2e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 67.7% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 89.9% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 90.5% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.8% | no / no |

- Class 1: normal first: `U2 F2 U`, then on inverse `(B2 R2 D B2 U' L2 F2 U F2 U2 R2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U2 F2 U R2 U2 F2 U' F2 L2 U B2 D' R2 B2`.
- Class 2: linear on normal: `B2 U2 R2 D B2 U R2 D' R2 U L2 F2 B2 U2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `B2 U2 R2 D B2 U R2 D' R2 U L2 F2 B2 U2`.
- Class 3: normal first: `U2 F2 U R2 U2 F2 U'`, then on inverse `(B2 R2 D B2 U' L2 F2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U2 F2 U R2 U2 F2 U' F2 L2 U B2 D' R2 B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `(B2 R2 D B2 U' L2 F2 U)`; the reduced state is then solved by `U2 F2 U R2 U2 F2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 5 moves, `(B2 R2 D B2 U')`; the reduced state is then solved by `U2 F2 U R2 U2 F2 U' F2 L2` (9 moves, 2 quarter turns).

</details>

**2c4 2e, example 5.** `U' D' L2 D B2 U D' L2 U2 D2 R2 D2 L2 F2 L2 U' R2 U2 R2 U' R2 U'`

Read as 2c4 2e on normal, 2c4 2e on inverse. Shortest HTR: 8 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 11 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 67.7% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | no / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 89.9% | yes / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 90.5% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.8% | no / no |

- Class 1: normal first: `U'`, then on inverse `(U L2 F2 U B2 R2 U' F2 U2 L2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `U' L2 U2 F2 U R2 B2 U' F2 L2 U'`.
- Class 2: linear on normal: `U' L2 U2 F2 U R2 B2 U' F2 L2 U'`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' L2 U2 F2 U R2 B2 U' F2 L2 U'`.
- Class 3: normal first: `U' L2 U2 F2 U`, then on inverse `(U L2 F2 U B2 R2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U' L2 U2 F2 U R2 B2 U' F2 L2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `U' (U L2 F2 U)`; the reduced state is then solved by `L2 U2 F2 U R2 B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 2 moves, `U' (U)`; the reduced state is then solved by `L2 U2 F2 U R2 B2 U' F2 L2` (9 moves, 2 quarter turns).

</details>

**2c4 2e, example 6.** `U2 D F2 D R2 B2 U D L2 U2 R2 D R2 U' L2 U L2 U2 R2 L2 U F2 L2 U2`

Read as 2c4 2e on normal, 2c4 2e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (5 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 67.7% | no / no |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | no / no |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 89.9% | no / no |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 90.5% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.8% | no / no |

- None of these classes finds an optimal finish on this DR.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `(U' R2 D R2 U F2 D R2 U')`; the reduced state is then solved by `R2 U2 F2 D R2 F2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 7 moves, `(U' R2 D R2 U F2 D)`; the reduced state is then solved by `R2 U2 F2 D R2 F2 U R2` (8 moves, 2 quarter turns).

</details>

**2c4 2e, example 7.** `U D2 R2 U R2 U R2 U2 F2 D B2 D F2 D2 R2 D' F2 L2 U' F2 R2 L2 U`

Read as 2c4 2e on normal, 2c4 2e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 67.7% | no / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | no / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 89.9% | yes / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 90.5% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.8% | no / no |

- Class 1: inverse first: `(F2 R2 D')`, then on normal `F2 U' B2 U R2 B2 R2 L2 D L2 F2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' B2 U R2 B2 R2 L2 D L2 F2 D R2 F2`.
- Class 2: linear on normal: `F2 U' B2 U R2 B2 R2 L2 D L2 F2 D R2 F2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' B2 U R2 B2 R2 L2 D L2 F2 D R2 F2`.
- Class 3: normal first: `F2 U' B2 U`, then on inverse `(F2 R2 D' F2 L2 D' L2 R2 B2 R2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `F2 U' B2 U R2 B2 R2 L2 D L2 F2 D R2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `F2 U' B2 U (F2 R2 D')`; the reduced state is then solved by `R2 B2 R2 L2 D L2 F2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 4 moves, `F2 U' B2 U`; the reduced state is then solved by `R2 B2 R2 L2 D L2 F2 D R2 F2` (10 moves, 2 quarter turns).

</details>

**2c4 2e, example 8.** `U2 D2 L2 B2 R2 D2 R2 U2 F2 L2 U2 F2 D' L2 U B2 U' F2 R2 U' B2 R2 U2`

Read as 2c4 2e on normal, 2c4 2e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 67.7% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | no / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 89.9% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 90.5% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.8% | no / no |

- Class 1: inverse first: `(B2 F2 D)`, then on normal `F2 U L2 D' R2 U B2 U2 R2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `F2 U L2 D' R2 U B2 U2 R2 D' F2 B2`.
- Class 2: linear on the inverse: `(B2 F2 D R2 U2 B2 U' R2 D L2 U' F2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U L2 D' R2 U B2 U2 R2 D' F2 B2`.
- Class 3: inverse first: `(B2 F2 D R2 U2 B2 U')`, then on normal `F2 U L2 D' R2`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U L2 D' R2 U B2 U2 R2 D' F2 B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `F2 U L2 D' R2 U`; the reduced state is then solved by `B2 U2 R2 D' F2 B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 4 moves, `F2 U L2 D'`; the reduced state is then solved by `R2 U B2 U2 R2 D' F2 B2` (8 moves, 2 quarter turns).

</details>

**2c4 2e, example 9.** `U' D' F2 L2 F2 B2 U2 D B2 R2 U L2 D' F2 U2 R2 L2 B2 D B2 U L2 B2 U`

Read as 2c4 2e on normal, 2c4 2e on inverse. Shortest HTR: 8 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 67.7% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 89.9% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 90.5% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.8% | no / no |

- Class 1: normal first: `R2 U`, then on inverse `(B2 R2 U' B2 R2 U' F2 U' F2 D2 F2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `R2 U F2 D2 F2 U F2 U R2 B2 U R2 B2`.
- Class 2: linear on the inverse: `(R2 U' B2 D B2 U' F2 R2 U' D2 F2 L2 F2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `F2 L2 F2 D2 U R2 F2 U B2 D' B2 U R2`.
- Class 3: normal first: `R2 U F2 D2 F2 U`, then on inverse `(B2 R2 U' B2 R2 U' F2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U F2 D2 F2 U F2 U R2 B2 U R2 B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `(R2 U' B2 D B2 U')`; the reduced state is then solved by `F2 L2 F2 U D2 R2 F2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 4 moves, `(R2 U' B2 D)`; the reduced state is then solved by `F2 L2 F2 U D2 R2 F2 U B2` (9 moves, 2 quarter turns).

</details>

**2c4 2e, example 10.** `F2 U D F2 D' R2 U D2 B2 D' L2 F2 D2 B2 U2 F2 L2 D'`

Read as 2c4 2e on normal, 2c4 2e on inverse. Shortest HTR: 8 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (33 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 67.7% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 89.9% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 90.5% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 90.8% | no / no |

- Class 1: normal first: `U`, then on inverse `(B2 U2 F2 R2 U B2 D R2 U' L2 U2 B2 L2 B2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U B2 L2 B2 U2 L2 U R2 D' B2 U' R2 F2 U2 B2`.
- Class 2: linear on normal: `D L2 U2 R2 D L2 U F2 R2 D L2 B2 D2 R2 F2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `D L2 U2 R2 D L2 U F2 R2 D L2 B2 D2 R2 F2`.
- Class 3: normal first: `R2 U B2 L2 D`, then on inverse `(R2 U2 B2 D R2 D' R2 D2 B2 F2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U B2 L2 D F2 B2 D2 R2 D R2 D' B2 U2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `D L2 U2 R2 D L2 U`; the reduced state is then solved by `F2 R2 D L2 B2 D2 R2 F2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 4 moves, `F2 D B2 D`; the reduced state is then solved by `L2 F2 U' B2 U2 F2 L2 U' F2 U2 L2` (11 moves, 2 quarter turns).

</details>

### 2c4 4e

11.76% of all DR states.

**2c4 4e, example 1.** `F2 U D' R2 F2 U' D2 B2 L2 U2 B2 U' B2 D' L2 D' R2 B2 D L2 U'`

Read as 2c4 4e on normal, 2c4 4e on inverse. Shortest HTR: 9 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 62.0% | no / no |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.0% | no / no |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 87.6% | no / no |
| 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 88.1% | no / no |
| 5 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 88.4% | no / no |

- None of these classes finds an optimal finish on this DR.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `U' F2 U (R2 U L2 D L2 D')`; the reduced state is then solved by `R2 D' L2 F2` (4 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 7 moves, `U' (R2 U L2 D L2 D')`; the reduced state is then solved by `F2 U R2 D' L2 F2` (6 moves, 2 quarter turns).

</details>

**2c4 4e, example 2.** `U' B2 U2 D2 L2 D' L2 D2 F2 D' F2 D F2 D' L2 U L2 D' F2 D R2`

Read as 2c4 4e on normal, 2c4 4e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (29 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 62.0% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.0% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 87.6% | yes / yes |
| 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 88.1% | no / no |
| 5 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 88.4% | no / no |

- Class 1: normal first: `F2 L2 U`, then on inverse `(R2 D' R2 U R2 B2 D' F2 D2 B2 D2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `F2 L2 U D2 B2 D2 F2 D B2 R2 U' R2 D R2`.
- Class 2: linear on the inverse: `(R2 U' B2 U B2 L2 D L2 D L2 F2 U2 L2 U2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U2 L2 U2 F2 L2 D' L2 D' L2 B2 U' B2 U R2`.
- Class 3: normal first: `F2 L2 U F2 U`, then on inverse `(R2 U' B2 U B2 D2 R2 U2 R2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `F2 L2 U F2 U R2 U2 R2 D2 B2 U' B2 U R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `(R2 U' B2 U B2 L2 D)`; the reduced state is then solved by `U2 L2 U2 F2 L2 D' L2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `(R2 U' B2 U)`; the reduced state is then solved by `U2 L2 U2 F2 L2 D' L2 D' L2 B2` (10 moves, 2 quarter turns).

</details>

**2c4 4e, example 3.** `U F2 B2 U' L2 D' B2 U' D' R2 L2 B2 D B2 D L2 U D2 B2 R2 U' L2 U'`

Read as 2c4 4e on normal, 2c4 4e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (5 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 62.0% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.0% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 87.6% | no / yes |
| 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 88.1% | no / no |
| 5 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 88.4% | no / no |

- Class 1: inverse first: `(U2 R2 U')`, then on normal `B2 U F2 L2 D B2 U' B2 D2 F2 R2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `B2 U F2 L2 D B2 U' B2 D2 F2 R2 U R2 U2`.
- Class 2: linear on normal: `U2 F2 D' L2 U R2 D' F2 D' F2 D2 R2 F2 R2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U2 F2 D' L2 U R2 D' F2 D' F2 D2 R2 F2 R2`.
- Class 3: normal first: `U2 F2 D' L2 U`, then on inverse `(R2 F2 R2 D2 F2 D F2 D R2)`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U2 F2 D' L2 U R2 D' F2 D' F2 D2 R2 F2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U2 F2 D' L2 U R2 D'`; the reduced state is then solved by `F2 D' F2 D2 R2 F2 R2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `U2 F2 D' L2 U`; the reduced state is then solved by `R2 D' F2 D' F2 D2 R2 F2 R2` (9 moves, 2 quarter turns).

</details>

**2c4 4e, example 4.** `U2 D' B2 R2 D2 F2 U R2 U' F2 U' F2 L2 U' F2 B2 D2 R2 U' L2 B2 U' F2 U'`

Read as 2c4 4e on normal, 2c4 4e on inverse. Shortest HTR: 8 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 62.0% | no / no |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.0% | no / no |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 87.6% | no / no |
| 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 88.1% | no / yes |
| 5 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 88.4% | no / no |

- Class 4: inverse first: `(D' B2 D')`, then on normal `U' F2 U' L2 U L2 B2 D B2 U2 R2`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' F2 U' L2 U L2 B2 D B2 U2 R2 D B2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `U' F2 U' L2 U (D' B2 D')`; the reduced state is then solved by `L2 B2 D B2 U2 R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 6 moves, `U' F2 U' (D' B2 D')`; the reduced state is then solved by `L2 U L2 B2 D B2 U2 R2` (8 moves, 2 quarter turns).

</details>

**2c4 4e, example 5.** `U' D R2 L2 U' D' R2 U D F2 U2 R2 U' L2 D L2 U' R2 L2 F2 D' F2 L2`

Read as 2c4 4e on normal, 2c4 4e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (15 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 62.0% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.0% | no / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 87.6% | yes / yes |
| 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 88.1% | no / no |
| 5 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 88.4% | no / no |

- Class 1: inverse first: `(L2 F2 D')`, then on normal `U F2 D F2 L2 D' U2 B2 U2 B2 L2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U F2 D F2 L2 D' U2 B2 U2 B2 L2 D F2 L2`.
- Class 2: linear on normal: `L2 D' R2 L2 F2 L2 U R2 F2 D L2 D' F2 R2`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 D' R2 L2 F2 L2 U R2 F2 D L2 D' F2 R2`.
- Class 3: normal first: `L2 D' F2 R2 U`, then on inverse `(R2 F2 D L2 D' L2 R2 F2 L2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `L2 D' F2 R2 U L2 F2 R2 L2 D L2 D' F2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `U F2 D (L2 F2 D')`; the reduced state is then solved by `F2 L2 U2 D' B2 U2 B2 L2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 3 moves, `U F2 D`; the reduced state is then solved by `F2 L2 U2 D' B2 U2 B2 L2 D F2 L2` (11 moves, 2 quarter turns).

</details>

**2c4 4e, example 6.** `D F2 U' D L2 F2 D L2 D' R2 D' B2 L2 F2 U2 L2`

Read as 2c4 4e on normal, 2c4 4e on inverse. Shortest HTR: 9 on normal, 7 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (7 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 62.0% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.0% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 87.6% | no / yes |
| 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 88.1% | no / no |
| 5 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 88.4% | no / no |

- Class 1: inverse first: `(U)`, then on normal `R2 U L2 D' F2 D' B2 L2 B2 U2 R2 L2 F2`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `R2 U L2 D' F2 D' B2 L2 B2 U2 R2 L2 F2 U'`.
- Class 2: linear on the inverse: `(R2 U B2 D R2 U' R2 U' B2 L2 B2 F2 U2 L2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `L2 U2 F2 B2 L2 B2 U R2 U R2 D' B2 U' R2`.
- Class 3: normal first: `B2 R2 U' B2 U`, then on inverse `(U F2 D2 F2 L2 F2 U R2 B2)`. HTR after 12 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `B2 R2 U' B2 U B2 R2 U' F2 L2 F2 D2 F2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `R2 U L2 D' (U)`; the reduced state is then solved by `F2 D' B2 L2 B2 U2 R2 L2 F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `R2 U (U)`; the reduced state is then solved by `L2 D' F2 D' B2 L2 B2 U2 R2 L2 F2` (11 moves, 2 quarter turns).

</details>

**2c4 4e, example 7.** `R2 D F2 R2 L2 U2 D' B2 D' R2 F2 D F2 R2 U F2 D' F2 D2 L2 U R2 D`

Read as 2c4 4e on normal, 2c4 4e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 62.0% | no / no |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.0% | no / no |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 87.6% | no / no |
| 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 88.1% | no / yes |
| 5 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 88.4% | no / yes |

- Class 4: inverse first: `(U' L2 D')`, then on normal `L2 B2 U' B2 U L2 U' L2 U R2`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 U' B2 U L2 U' L2 U R2 D L2 U`.
- Class 5: inverse first: `(U')`, then on normal `L2 B2 U' B2 U L2 U' L2 U R2 D L2`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 U' B2 U L2 U' L2 U R2 D L2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `(U' L2 D' R2 U' L2 U L2 U')`; the reduced state is then solved by `L2 B2 U' B2` (4 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 7 moves, `(U' L2 D' R2 U' L2 U)`; the reduced state is then solved by `L2 B2 U' B2 U L2` (6 moves, 2 quarter turns).

</details>

**2c4 4e, example 8.** `L2 D B2 D2 L2 U R2 L2 U2 L2 D' R2 F2 D' R2 D B2 U2 R2 D' B2 L2 F2`

Read as 2c4 4e on normal, 2c4 4e on inverse. Shortest HTR: 8 on normal, 7 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 62.0% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.0% | no / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 87.6% | no / yes |
| 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 88.1% | no / no |
| 5 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 88.4% | no / no |

- Class 1: inverse first: `(D)`, then on normal `L2 B2 D' B2 U B2 L2 D F2 B2 R2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `L2 B2 D' B2 U B2 L2 D F2 B2 R2 D'`.
- Class 2: linear on the inverse: `(D R2 B2 F2 D' L2 B2 U' B2 D B2 L2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 D' B2 U B2 L2 D F2 B2 R2 D'`.
- Class 3: normal first: `L2 B2 D' B2 U`, then on inverse `(D R2 B2 F2 D' L2 B2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 D' B2 U B2 L2 D F2 B2 R2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `L2 B2 D' B2 U (D)`; the reduced state is then solved by `B2 L2 D F2 B2 R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 4 moves, `L2 B2 D' (D)`; the reduced state is then solved by `B2 U B2 L2 D F2 B2 R2` (8 moves, 2 quarter turns).

</details>

**2c4 4e, example 9.** `D' L2 U' B2 U2 D2 R2 D F2 U R2 D' R2 D2 F2 U' F2 L2 D2 F2 L2 U' L2 U'`

Read as 2c4 4e on normal, 2c4 4e on inverse. Shortest HTR: 10 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (21 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 62.0% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.0% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 87.6% | no / yes |
| 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 88.1% | no / yes |
| 5 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 88.4% | no / yes |

- Class 1: inverse first: `(F2 D')`, then on normal `L2 U' F2 D B2 R2 U L2 U2 F2 L2 F2 R2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `L2 U' F2 D B2 R2 U L2 U2 F2 L2 F2 R2 D F2`.
- Class 2: linear on the inverse: `(F2 U' R2 D L2 D' L2 D F2 U2 B2 F2 R2 F2 R2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `R2 F2 R2 F2 B2 U2 F2 D' L2 D L2 D' R2 U F2`.
- Class 3: inverse first: `(F2 D' R2 F2 L2 F2 U2 L2 U')`, then on normal `L2 U' F2 D B2 R2`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U' F2 D B2 R2 U L2 U2 F2 L2 F2 R2 D F2`.
- Class 4: normal first: `F2 U' R2 D'`, then on inverse `(U' R2 F2 D L2 U' F2 D' L2 U2 R2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' R2 D' R2 U2 L2 D F2 U L2 D' F2 R2 U`.
- Class 5: inverse first: `(D')`, then on normal `F2 U' R2 D R2 D B2 U2 F2 U' R2 U' L2 F2`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' R2 D R2 D B2 U2 F2 U' R2 U' L2 F2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `(F2 U' R2 D L2 D')`; the reduced state is then solved by `R2 F2 R2 F2 B2 U2 F2 D' L2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `R2 D' (B2 U')`; the reduced state is then solved by `F2 L2 F2 R2 U' F2 U L2 U2 R2 F2` (11 moves, 2 quarter turns).

</details>

**2c4 4e, example 10.** `F2 B2 U F2 D' F2 L2 F2 B2 D2 L2 D' L2 U F2 D B2 L2 U2 R2 U'`

Read as 2c4 4e on normal, 2c4 4e on inverse. Shortest HTR: 8 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (49 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 62.0% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.0% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 87.6% | no / yes |
| 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 88.1% | no / no |
| 5 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 88.4% | no / no |

- Class 1: normal first: `B2 U'`, then on inverse `(B2 U2 R2 U' R2 U' R2 U' R2 F2 D2 R2 B2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `B2 U' B2 R2 D2 F2 R2 U R2 U R2 U R2 U2 B2`.
- Class 2: linear on normal: `B2 U' L2 U F2 D' L2 D R2 B2 D2 F2 D2 L2 B2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `B2 U' L2 U F2 D' L2 D R2 B2 D2 F2 D2 L2 B2`.
- Class 3: normal first: `R2 L2 D2 B2 U' B2 U'`, then on inverse `(R2 B2 U' B2 D' B2 D2 F2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 L2 D2 B2 U' B2 U' F2 D2 B2 D B2 U B2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `B2 U' L2 U F2 D'`; the reduced state is then solved by `L2 D R2 B2 D2 F2 D2 L2 B2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `B2 U' L2 U`; the reduced state is then solved by `F2 D' L2 D R2 B2 D2 F2 D2 L2 B2` (11 moves, 2 quarter turns).

</details>

### 2c4 6e

5.22% of all DR states.

**2c4 6e, example 1.** `U2 F2 U2 D B2 U2 R2 U2 D' F2 U' F2 U' R2 U B2 U' B2 L2 D F2 B2 R2 D`

Read as 2c4 6e on normal, 2c4 6e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (35 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.8% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 88.5% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 89.2% | no / yes |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 89.6% | no / yes |

- Class 1: inverse first: `(U2 R2 D)`, then on normal `R2 U' F2 U B2 R2 U F2 R2 B2 L2 F2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `R2 U' F2 U B2 R2 U F2 R2 B2 L2 F2 D' R2 U2`.
- Class 2: linear on normal: `R2 D' R2 D L2 B2 D L2 F2 U B2 D2 R2 F2 L2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `R2 D' R2 D L2 B2 D L2 F2 U B2 D2 R2 F2 L2`.
- Class 3: normal first: `R2 U' F2 U`, then on inverse `(U2 R2 D F2 L2 B2 R2 F2 U' R2 B2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U' F2 U B2 R2 U F2 R2 B2 L2 F2 D' R2 U2`.
- Class 4: inverse first: `(D')`, then on normal `U B2 R2 U' B2 D2 R2 U R2 U' F2 D L2 F2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 R2 U' B2 D2 R2 U R2 U' F2 D L2 F2 D`.
- Class 5: normal first: `U B2 R2 U'`, then on inverse `(D' F2 L2 D' F2 U R2 U' R2 D2 B2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 R2 U' B2 D2 R2 U R2 U' F2 D L2 F2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `R2 U' F2 U (U2 R2 D)`; the reduced state is then solved by `B2 R2 U F2 R2 B2 L2 F2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `R2 U' F2 U`; the reduced state is then solved by `B2 R2 U F2 R2 B2 L2 F2 D' R2 U2` (11 moves, 2 quarter turns).

</details>

**2c4 6e, example 2.** `D R2 D2 R2 U' F2 U B2 L2 U2 D' F2 U' L2 D' B2 R2 D2 R2`

Read as 2c4 6e on normal, 2c4 6e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (10 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.8% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 88.5% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 89.2% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 89.6% | no / no |

- Class 1: inverse first: `(B2 D')`, then on normal `F2 U2 R2 U F2 U B2 U B2 R2 U2 B2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `F2 U2 R2 U F2 U B2 U B2 R2 U2 B2 D B2`.
- Class 2: linear on the inverse: `(B2 D L2 F2 U F2 U' B2 U' D2 F2 L2 D2 L2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `L2 D2 L2 F2 D2 U B2 U F2 U' F2 L2 D' B2`.
- Class 3: normal first: `L2 D2 L2 F2 U' F2 U`, then on inverse `(B2 D L2 F2 U' D2 B2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 D2 L2 F2 U' F2 U B2 D2 U F2 L2 D' B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `(B2 D L2 F2 U F2 U')`; the reduced state is then solved by `L2 D2 L2 F2 U D2 B2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `(B2 D L2 F2 U)`; the reduced state is then solved by `L2 D2 L2 F2 U D2 B2 U F2` (9 moves, 2 quarter turns).

</details>

**2c4 6e, example 3.** `U2 D F2 U D R2 L2 U2 D2 R2 L2 D B2 U2 R2 U B2 U' F2 D F2 L2 U'`

Read as 2c4 6e on normal, 2c4 6e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (9 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.8% | no / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 88.5% | yes / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 89.2% | no / yes |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 89.6% | yes / yes |

- Class 1: normal first: `B2 L2 D'`, then on inverse `(B2 U R2 U B2 R2 B2 D2 L2 D' F2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 L2 D' F2 D L2 D2 B2 R2 B2 U' R2 U' B2`.
- Class 2: linear on the inverse: `(B2 U R2 U B2 R2 B2 D2 L2 D' F2 D L2 B2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 L2 D' F2 D L2 D2 B2 R2 B2 U' R2 U' B2`.
- Class 3: normal first: `B2 L2 D' F2 D`, then on inverse `(B2 U R2 U B2 R2 B2 D2 L2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `B2 L2 D' F2 D L2 D2 B2 R2 B2 U' R2 U' B2`.
- Class 4: normal first: `U`, then on inverse `(U' L2 D R2 D2 F2 U' F2 D' R2 U F2 L2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U L2 F2 U' R2 D F2 U F2 D2 R2 D' L2 U`.
- Class 5: inverse first: `(U' L2 D)`, then on normal `U L2 F2 U' R2 D F2 U F2 D2 R2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U L2 F2 U' R2 D F2 U F2 D2 R2 D' L2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `B2 L2 D' (B2 U R2 U)`; the reduced state is then solved by `F2 D L2 D2 B2 R2 B2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `(B2 U R2 U)`; the reduced state is then solved by `B2 L2 D' F2 D L2 D2 B2 R2 B2` (10 moves, 2 quarter turns).

</details>

**2c4 6e, example 4.** `U2 D2 F2 B2 D L2 D' B2 L2 U F2 L2 D' B2 U L2 U' B2 U2 L2`

Read as 2c4 6e on normal, 2c4 6e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.8% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 88.5% | yes / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 89.2% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 89.6% | no / no |

- Class 1: normal first: `U2 F2 U'`, then on inverse `(D' B2 D' B2 L2 D2 B2 D R2 D2 B2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U2 F2 U' B2 D2 R2 D' B2 D2 L2 B2 D B2 D`.
- Class 2: linear on normal: `U2 F2 U' B2 D2 R2 D' B2 D2 L2 B2 D B2 D`. HTR after 14 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U2 F2 U' B2 D2 R2 D' B2 D2 L2 B2 D B2 D`.
- Class 3: normal first: `U2 F2 U' B2 D2 R2 D'`, then on inverse `(D' B2 D' B2 L2 D2 B2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U2 F2 U' B2 D2 R2 D' B2 D2 L2 B2 D B2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `U2 F2 U' (D' B2 D')`; the reduced state is then solved by `B2 D2 R2 D' B2 D2 L2 B2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 3 moves, `(D' B2 D')`; the reduced state is then solved by `U2 F2 U' B2 D2 R2 D' B2 D2 L2 B2` (11 moves, 2 quarter turns).

</details>

**2c4 6e, example 5.** `U' D' L2 U F2 U2 D B2 R2 F2 R2 F2 L2 U L2 B2 U L2 U F2 U2 R2 D' R2 U2`

Read as 2c4 6e on normal, 2c4 6e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.8% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 88.5% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 89.2% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 89.6% | no / no |

- Class 1: normal first: `D2 B2 L2 U'`, then on inverse `(U F2 R2 D L2 D B2 F2 D2 R2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `D2 B2 L2 U' R2 D2 F2 B2 D' L2 D' R2 F2 U'`.
- Class 2: linear on the inverse: `(U F2 R2 D L2 D B2 F2 D2 R2 U L2 B2 D2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `D2 B2 L2 U' R2 D2 F2 B2 D' L2 D' R2 F2 U'`.
- Class 3: normal first: `D2 B2 L2 U' R2 D2 F2 B2 D'`, then on inverse `(U F2 R2 D L2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D2 B2 L2 U' R2 D2 F2 B2 D' L2 D' R2 F2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `(U F2 R2 D L2 D)`; the reduced state is then solved by `D2 B2 L2 U' R2 D2 F2 B2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `(U F2 R2 D)`; the reduced state is then solved by `D2 B2 L2 U' R2 D2 F2 B2 D' L2` (10 moves, 2 quarter turns).

</details>

**2c4 6e, example 6.** `U R2 U' D F2 D2 R2 U2 D L2 D L2 U2 F2 L2 U' F2 B2 L2 U L2 D2 F2 U'`

Read as 2c4 6e on normal, 2c4 6e on inverse. Shortest HTR: 8 on normal, 8 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.8% | no / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 88.5% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 89.2% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 89.6% | no / no |

- Class 1: inverse first: `(D')`, then on normal `F2 D2 L2 B2 U' B2 D L2 D' F2 L2 D2 R2`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 D2 L2 B2 U' B2 D L2 D' F2 L2 D2 R2 D`.
- Class 2: linear on the inverse: `(D' R2 D2 L2 F2 D L2 D' B2 U B2 L2 D2 F2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 D2 L2 B2 U' B2 D L2 D' F2 L2 D2 R2 D`.
- Class 3: inverse first: `(D' R2 D2 L2 F2 D)`, then on normal `F2 D2 L2 B2 U' B2 D L2`. HTR after 13 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `F2 D2 L2 B2 U' B2 D L2 D' F2 L2 D2 R2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `(D' R2 D2 L2 F2 D L2 D')`; the reduced state is then solved by `F2 D2 L2 B2 U' B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `B2 U2 B2 D (U)`; the reduced state is then solved by `F2 R2 U L2 D R2 U2 R2 B2` (9 moves, 2 quarter turns).

</details>

**2c4 6e, example 7.** `L2 U' D R2 F2 B2 R2 U2 D' B2 L2 B2 D R2 D' F2 R2 D2 L2 U' B2 U L2 U'`

Read as 2c4 6e on normal, 2c4 6e on inverse. Shortest HTR: 9 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.8% | no / no |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / no |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 88.5% | no / no |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 89.2% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 89.6% | no / no |

- None of these classes finds an optimal finish on this DR.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `U B2 D' F2 U' L2 D' (U')`; the reduced state is then solved by `R2 U F2 L2 B2 R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `U B2 D' F2 U' (U')`; the reduced state is then solved by `L2 D' R2 U F2 L2 B2 R2` (8 moves, 2 quarter turns).

</details>

**2c4 6e, example 8.** `F2 D R2 U' D B2 U D' L2 U' B2 D R2 F2 R2 L2 U2 D' R2 U' B2 U B2 U2`

Read as 2c4 6e on normal, 2c4 6e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (35 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.8% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | no / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 88.5% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 89.2% | no / yes |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 89.6% | no / yes |

- Class 1: inverse first: `(U)`, then on normal `B2 L2 D F2 L2 D R2 F2 D B2 U2 R2 F2 B2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `B2 L2 D F2 L2 D R2 F2 D B2 U2 R2 F2 B2 U'`.
- Class 2: linear on the inverse: `(U2 F2 D' L2 D' B2 D' B2 F2 U2 L2 D' L2 U2 F2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U2 L2 D L2 U2 F2 B2 D B2 D L2 D F2 U2`.
- Class 3: inverse first: `(L2 F2 L2 D' L2 D2 R2 B2 D')`, then on normal `L2 D' B2 U B2 R2`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `L2 D' B2 U B2 R2 D B2 R2 D2 L2 D L2 F2 L2`.
- Class 4: normal first: `U'`, then on inverse `(U L2 D2 B2 U' B2 L2 U' B2 U R2 D' B2 F2)`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U' F2 B2 D R2 U' B2 U L2 B2 U B2 D2 L2 U'`.
- Class 5: normal first: `F2 U' R2 U'`, then on inverse `(D L2 U R2 U' F2 L2 U B2 U2 R2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' R2 U' R2 U2 B2 U' L2 F2 U R2 U' L2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `L2 D' B2 U B2 R2 D`; the reduced state is then solved by `B2 R2 D2 L2 D L2 F2 L2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 4 moves, `L2 D' B2 U`; the reduced state is then solved by `B2 R2 D B2 R2 D2 L2 D L2 F2 L2` (11 moves, 2 quarter turns).

</details>

**2c4 6e, example 9.** `F2 L2 U' R2 D L2 F2 B2 U' R2 L2 U R2 U' L2 D2 R2 F2 U2 D F2 L2 B2`

Read as 2c4 6e on normal, 2c4 6e on inverse. Shortest HTR: 8 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (5 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.8% | no / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 88.5% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 89.2% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 89.6% | no / no |

- Class 1: normal first: `L2 B2 R2 U'`, then on inverse `(R2 U R2 D' R2 B2 U' F2 D2 L2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 R2 U' L2 D2 F2 U B2 R2 D R2 U' R2`.
- Class 2: linear on normal: `D' L2 U R2 F2 U F2 B2 L2 D R2 D2 L2 F2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `D' L2 U R2 F2 U F2 B2 L2 D R2 D2 L2 F2`.
- Class 3: normal first: `D' L2 U`, then on inverse `(F2 L2 D2 R2 D' L2 B2 F2 U' F2 R2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D' L2 U R2 F2 U F2 B2 L2 D R2 D2 L2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `D' L2 U R2 F2 U`; the reduced state is then solved by `F2 B2 L2 D R2 D2 L2 F2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `D' L2 U`; the reduced state is then solved by `R2 F2 U F2 B2 L2 D R2 D2 L2 F2` (11 moves, 2 quarter turns).

</details>

**2c4 6e, example 10.** `U2 F2 R2 F2 U' D' L2 U2 L2 D R2 B2 U2 F2 R2 U' R2 D' F2 D R2`

Read as 2c4 6e on normal, 2c4 6e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 73.8% | yes / yes |
| 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | yes / yes |
| 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 88.5% | no / yes |
| 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 89.2% | no / no |
| 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 89.6% | no / no |

- Class 1: inverse first: `(D2 R2 U')`, then on normal `F2 B2 R2 U' R2 U B2 D' B2 L2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `F2 B2 R2 U' R2 U B2 D' B2 L2 U R2 D2`.
- Class 2: linear on the inverse: `(D2 R2 U' L2 B2 D B2 U' R2 U R2 B2 F2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `F2 B2 R2 U' R2 U B2 D' B2 L2 U R2 D2`.
- Class 3: normal first: `F2 B2 R2 U' R2 U`, then on inverse `(D2 R2 U' L2 B2 D B2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 R2 U' R2 U B2 D' B2 L2 U R2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `(D2 R2 U' L2 B2 D B2 U')`; the reduced state is then solved by `F2 B2 R2 U' R2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `(D2 R2 U' L2 B2 D)`; the reduced state is then solved by `F2 B2 R2 U' R2 U B2` (7 moves, 2 quarter turns).

</details>

## 4a2

### 4a2 2e

1.31% of all DR states.

**4a2 2e, example 1.** `R2 U2 L2 U B2 U D R2 D2 L2 D B2 U2 R2 F2 R2 F2 U' L2 B2 U2 B2 U'`

Read as 4a2 2e on normal, 4a2 2e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 42.2% | yes / yes |
| 2 | `4a2 > 4a1 > (0c0)` | 67.8% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 76.8% | no / no |
| 4 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 79.6% | no / no |
| 5 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 81.4% | no / no |

- Class 1: inverse first: `(U' B2 L2 B2 D' B2 U')`, then on normal `D F2 U2 F2 R2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `D F2 U2 F2 R2 U B2 D B2 L2 B2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `D (U' B2 L2 B2 D')`; the reduced state is then solved by `F2 U2 F2 R2 U B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 2 moves, `D (U')`; the reduced state is then solved by `F2 U2 F2 R2 U B2 D B2 L2 B2` (10 moves, 2 quarter turns).

</details>

**4a2 2e, example 2.** `D2 R2 U2 D2 F2 U D F2 U F2 D2 R2 D B2 R2 D' L2 F2 L2 D B2 U2`

Read as 4a2 2e on normal, 4a2 2e on inverse. Shortest HTR: 11 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 42.2% | yes / yes |
| 2 | `4a2 > 4a1 > (0c0)` | 67.8% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 76.8% | no / no |
| 4 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 79.6% | no / no |
| 5 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 81.4% | no / no |

- Class 1: normal first: `F2 U' F2 B2 U' B2 D`, then on inverse `(F2 U B2 U2 L2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `F2 U' F2 B2 U' B2 D L2 U2 B2 U' F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `F2 U' F2 B2 U' (F2 U)`; the reduced state is then solved by `B2 D L2 U2 B2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `F2 U' (F2 U)`; the reduced state is then solved by `F2 B2 U' B2 D L2 U2 B2` (8 moves, 2 quarter turns).

</details>

**4a2 2e, example 3.** `U L2 F2 L2 U2 D2 F2 U' D' F2 R2 L2 D' B2 R2 U2 L2 F2 D2 R2 B2 U2`

Read as 4a2 2e on normal, 4a2 2e on inverse. Shortest HTR: 10 on normal, 8 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (22 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 42.2% | no / yes |
| 2 | `4a2 > 4a1 > (0c0)` | 67.8% | yes / yes |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 76.8% | no / yes |
| 4 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 79.6% | no / yes |
| 5 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 81.4% | no / yes |

- Class 1: normal first: `U B2 R2 F2 D' B2 R2 U`, then on inverse `(L2 R2 U R2 D2 B2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 R2 F2 D' B2 R2 U B2 D2 R2 U' R2 L2`.
- Class 2: normal first: `U2 B2 R2 F2 L2 U`, then on inverse `(U D2 L2 U2 B2 R2 B2 L2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `U2 B2 R2 F2 L2 U L2 B2 R2 B2 U2 L2 D2 U'`.
- Class 3: linear on normal: `U2 F2 D B2 D F2 B2 U F2 R2 D B2 L2 B2`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U2 F2 D B2 D F2 B2 U F2 R2 D B2 L2 B2`.
- Class 4: inverse first: `(D)`, then on normal `U2 B2 U F2 D' F2 L2 B2 U F2 L2 B2 L2`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U2 B2 U F2 D' F2 L2 B2 U F2 L2 B2 L2 D'`.
- Class 5: normal first: `U2 B2 U F2 D'`, then on inverse `(D L2 B2 L2 F2 U' B2 L2 F2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U2 B2 U F2 D' F2 L2 B2 U F2 L2 B2 L2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 1 move, `(U)`; the reduced state is then solved by `U2 B2 R2 F2 L2 U L2 B2 R2 B2 U2 L2 D2` (13 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 2e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `U2 B2 R2 F2 L2 U L2 B2 R2 B2 U2 L2 U' D2` (14 moves, 2 quarter turns).

</details>

**4a2 2e, example 4.** `U R2 B2 U2 B2 L2 U D' R2 D2 L2 D' F2 D2 F2 R2 B2 U L2 D2 F2 D F2 R2`

Read as 4a2 2e on normal, 4a2 2e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 42.2% | yes / yes |
| 2 | `4a2 > 4a1 > (0c0)` | 67.8% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 76.8% | no / no |
| 4 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 79.6% | no / no |
| 5 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 81.4% | no / no |

- Class 1: inverse first: `(F2 U' B2 F2 U F2 U')`, then on normal `B2 D F2 D2 F2 R2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `B2 D F2 D2 F2 R2 U F2 U' F2 B2 U F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `(F2 U' B2 F2 U F2 U')`; the reduced state is then solved by `B2 D F2 D2 F2 R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `B2 D (F2 U')`; the reduced state is then solved by `F2 D2 F2 R2 U F2 U' F2 B2` (9 moves, 2 quarter turns).

</details>

**4a2 2e, example 5.** `D2 L2 U2 D' R2 U D' F2 B2 D2 R2 F2 R2 F2 U' F2 U B2 R2 U D' L2 U'`

Read as 4a2 2e on normal, 4a2 2e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 42.2% | yes / yes |
| 2 | `4a2 > 4a1 > (0c0)` | 67.8% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 76.8% | no / no |
| 4 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 79.6% | no / no |
| 5 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 81.4% | no / no |

- Class 1: normal first: `U' F2 D2 F2 R2 U' F2 L2 U'`, then on inverse `(U R2 B2 U2 B2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U' F2 D2 F2 R2 U' F2 L2 U' B2 U2 B2 R2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U' (U R2 B2 U2 B2 U)`; the reduced state is then solved by `F2 D2 F2 R2 U' F2 L2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 2 moves, `U' (U)`; the reduced state is then solved by `F2 D2 F2 R2 U' F2 L2 U' B2 U2 B2 R2` (12 moves, 2 quarter turns).

</details>

**4a2 2e, example 6.** `D2 F2 D' F2 L2 U' L2 U2 D R2 U' R2 B2 L2 F2 R2 D F2 U R2 U2`

Read as 4a2 2e on normal, 4a2 2e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (11 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 42.2% | no / yes |
| 2 | `4a2 > 4a1 > (0c0)` | 67.8% | yes / yes |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 76.8% | no / no |
| 4 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 79.6% | no / no |
| 5 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 81.4% | no / no |

- Class 1: inverse first: `(L2 D B2 L2 F2 U R2 U')`, then on normal `U2 R2 U' L2 D2 F2`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U2 R2 U' L2 D2 F2 U R2 U' F2 L2 B2 D' L2`.
- Class 2: normal first: `B2 L2 U2 F2 D'`, then on inverse `(F2 D F2 L2 F2 R2 F2 U2 B2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `B2 L2 U2 F2 D' B2 U2 F2 R2 F2 L2 F2 D' F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 2 moves, `(F2 D)`; the reduced state is then solved by `B2 L2 U2 F2 D' B2 U2 F2 R2 F2 L2 F2` (12 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 2e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `B2 L2 U2 F2 D' B2 U2 F2 R2 F2 L2 F2 D' F2` (14 moves, 2 quarter turns).

</details>

**4a2 2e, example 7.** `F2 B2 U' D2 F2 U' L2 B2 D F2 B2 U2 F2 D' F2 U L2 F2 U R2 U2`

Read as 4a2 2e on normal, 4a2 2e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (4 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 42.2% | no / no |
| 2 | `4a2 > 4a1 > (0c0)` | 67.8% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 76.8% | no / no |
| 4 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 79.6% | no / no |
| 5 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 81.4% | no / no |

- None of these classes finds an optimal finish on this DR.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 10 moves, `B2 U' B2 D B2 U' (R2 U' L2 D)`; the reduced state is then solved by `R2 U' R2 F2` (4 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 8 moves, `B2 U' B2 D (R2 U' L2 D)`; the reduced state is then solved by `B2 U' R2 U' R2 F2` (6 moves, 2 quarter turns).

</details>

**4a2 2e, example 8.** `U D2 L2 D' B2 D2 R2 U' L2 F2 L2 B2 D' R2 D' L2 D L2 U' F2 U`

Read as 4a2 2e on normal, 4a2 2e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 42.2% | no / no |
| 2 | `4a2 > 4a1 > (0c0)` | 67.8% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 76.8% | no / no |
| 4 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 79.6% | no / no |
| 5 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 81.4% | no / no |

- None of these classes finds an optimal finish on this DR.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `U' (U B2 U' R2 U' F2 D')`; the reduced state is then solved by `L2 D2 F2 B2 D R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `U' (U B2 U' R2 U')`; the reduced state is then solved by `L2 D2 F2 B2 D R2 D F2` (8 moves, 2 quarter turns).

</details>

**4a2 2e, example 9.** `R2 F2 R2 D R2 F2 U R2 U D F2 R2 L2 U' L2 D R2 B2 R2 F2 U B2 D`

Read as 4a2 2e on normal, 4a2 2e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (8 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 42.2% | no / no |
| 2 | `4a2 > 4a1 > (0c0)` | 67.8% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 76.8% | no / yes |
| 4 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 79.6% | yes / yes |
| 5 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 81.4% | no / yes |

- Class 3: linear on normal: `L2 U' B2 D L2 F2 R2 U' F2 D' R2 L2 D2 R2`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U' B2 D L2 F2 R2 U' F2 D' R2 L2 D2 R2`.
- Class 4: normal first: `R2 D`, then on inverse `(L2 D' F2 U B2 F2 D L2 D2 B2 R2 F2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `R2 D F2 R2 B2 D2 L2 D' F2 B2 U' F2 D L2`.
- Class 5: normal first: `L2 U' B2 D`, then on inverse `(R2 D2 L2 R2 D F2 U R2 F2 L2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U' B2 D L2 F2 R2 U' F2 D' R2 L2 D2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `R2 D (L2 D' F2 U)`; the reduced state is then solved by `F2 R2 B2 D2 L2 D' F2 B2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `(L2 D' F2 U)`; the reduced state is then solved by `R2 D F2 R2 B2 D2 L2 D' F2 B2` (10 moves, 2 quarter turns).

</details>

**4a2 2e, example 10.** `L2 U F2 U2 R2 D' L2 D' R2 D2 B2 D L2 B2 U2 F2 D R2 B2 U2 B2 U R2`

Read as 4a2 2e on normal, 4a2 2e on inverse. Shortest HTR: 8 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (79 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 42.2% | yes / yes |
| 2 | `4a2 > 4a1 > (0c0)` | 67.8% | yes / yes |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 76.8% | no / yes |
| 4 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 79.6% | yes / yes |
| 5 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 81.4% | yes / yes |

- Class 1: normal first: `R2 F2 U' F2 R2 F2 U' F2 D`, then on inverse `(U' L2 D2 R2 B2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `R2 F2 U' F2 R2 F2 U' F2 D B2 R2 D2 L2 U`.
- Class 2: normal first: `D`, then on inverse `(R2 U2 B2 L2 U2 F2 U F2 R2 F2 R2 U2 B2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `D B2 U2 R2 F2 R2 F2 U' F2 U2 L2 B2 U2 R2`.
- Class 3: linear on normal: `D R2 U D2 L2 F2 L2 U F2 L2 U' L2 F2 L2`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D R2 U D2 L2 F2 L2 U F2 L2 U' L2 F2 L2`.
- Class 4: normal first: `U`, then on inverse `(U' L2 B2 D B2 F2 D' B2 R2 U2 L2 R2 F2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `U F2 R2 L2 U2 R2 B2 D F2 B2 D' B2 L2 U`.
- Class 5: normal first: `D R2 U`, then on inverse `(L2 F2 L2 U L2 F2 U' L2 F2 L2 D2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `D R2 U D2 L2 F2 L2 U F2 L2 U' L2 F2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 1 move, `D`; the reduced state is then solved by `B2 U2 R2 F2 R2 F2 U' F2 U2 L2 B2 U2 R2` (13 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 2e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `D B2 U2 R2 F2 R2 F2 U' F2 U2 L2 B2 U2 R2` (14 moves, 2 quarter turns).

</details>

### 4a2 4e

1.47% of all DR states.

**4a2 4e, example 1.** `L2 B2 U' D2 R2 U2 D2 B2 U2 F2 U' L2 U' B2 L2 B2 R2 U2 B2 U' F2 R2 U2`

Read as 4a2 4e on normal, 4a2 4e on inverse. Shortest HTR: 9 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4a1 > 0c0` | 60.9% | yes / yes |
| 2 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 72.2% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 79.1% | no / no |
| 4 | `4a2 > 4a1 > (0c0)` | 83.7% | yes / yes |
| 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 85.3% | no / no |

- Class 1: linear on normal: `B2 U2 R2 D' R2 B2 D2 L2 F2 U' L2 F2 L2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `B2 U2 R2 D' R2 B2 D2 L2 F2 U' L2 F2 L2`.
- Class 4: normal first: `B2 U2 R2 D'`, then on inverse `(L2 F2 L2 U F2 L2 D2 B2 R2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `B2 U2 R2 D' R2 B2 D2 L2 F2 U' L2 F2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `(L2 F2 L2 U)`; the reduced state is then solved by `B2 U2 R2 D' R2 B2 D2 L2 F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `B2 U2 R2 D' R2 B2 D2 L2 F2 U' L2 F2 L2` (13 moves, 2 quarter turns).

</details>

**4a2 4e, example 2.** `D L2 F2 B2 U' F2 U B2 D B2 U2 R2 D' R2 D' F2 U B2 U R2 D2 R2 F2`

Read as 4a2 4e on normal, 4a2 4e on inverse. Shortest HTR: 8 on normal, 10 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (34 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4a1 > 0c0` | 60.9% | no / no |
| 2 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 72.2% | yes / yes |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 79.1% | yes / yes |
| 4 | `4a2 > 4a1 > (0c0)` | 83.7% | no / no |
| 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 85.3% | yes / yes |

- Class 2: inverse first: `(D' B2 F2 D F2 U')`, then on normal `D F2 L2 B2 R2 F2 U2 F2`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `D F2 L2 B2 R2 F2 U2 F2 U F2 D' F2 B2 D`.
- Class 3: linear on normal: `D' B2 U F2 L2 B2 U' R2 U' B2 R2 F2 D2 R2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `D' B2 U F2 L2 B2 U' R2 U' B2 R2 F2 D2 R2`.
- Class 5: normal first: `U`, then on inverse `(F2 L2 D R2 D' L2 R2 D L2 B2 R2 U2 B2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U B2 U2 R2 B2 L2 D' R2 L2 D R2 D' L2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `D (D' B2 F2 D)`; the reduced state is then solved by `F2 L2 B2 R2 F2 U2 F2 U F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 2 moves, `D (D')`; the reduced state is then solved by `F2 L2 B2 R2 F2 U2 F2 U F2 D' F2 B2` (12 moves, 2 quarter turns).

</details>

**4a2 4e, example 3.** `D F2 D2 B2 D2 L2 B2 R2 F2 D2 R2 F2 U L2 D' F2 L2 D2 B2 L2 U`

Read as 4a2 4e on normal, 4a2 4e on inverse. Shortest HTR: 7 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4a1 > 0c0` | 60.9% | yes / yes |
| 2 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 72.2% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 79.1% | no / no |
| 4 | `4a2 > 4a1 > (0c0)` | 83.7% | no / yes |
| 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 85.3% | no / no |

- Class 1: linear on the inverse: `(R2 U B2 L2 U2 R2 D L2 F2 R2 F2 U2 B2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `B2 U2 F2 R2 F2 L2 D' R2 U2 L2 B2 U' R2`.
- Class 4: normal first: `B2 U2 F2 R2 F2 L2 D'`, then on inverse `(R2 U B2 L2 U2 R2)`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U2 F2 R2 F2 L2 D' R2 U2 L2 B2 U' R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 2 moves, `(R2 U)`; the reduced state is then solved by `B2 U2 F2 R2 F2 L2 D' R2 U2 L2 B2` (11 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `B2 U2 F2 R2 F2 L2 D' R2 U2 L2 B2 U' R2` (13 moves, 2 quarter turns).

</details>

**4a2 4e, example 4.** `R2 U' D2 R2 F2 D R2 B2 D2 F2 D' B2 R2 U' B2 D F2 D' B2 D' F2 U B2`

Read as 4a2 4e on normal, 4a2 4e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (92 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4a1 > 0c0` | 60.9% | yes / yes |
| 2 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 72.2% | yes / yes |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 79.1% | yes / yes |
| 4 | `4a2 > 4a1 > (0c0)` | 83.7% | yes / yes |
| 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 85.3% | no / yes |

- Class 1: linear on normal: `U2 R2 B2 U R2 U2 R2 F2 D B2 U2 B2 L2 U2 R2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U2 R2 B2 U R2 U2 R2 F2 D B2 U2 B2 L2 U2 R2`.
- Class 2: inverse first: `(L2 F2 D U B2 U')`, then on normal `D2 R2 B2 U' R2 B2 D2 L2 F2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `D2 R2 B2 U' R2 B2 D2 L2 F2 U B2 U' D' F2 L2`.
- Class 3: linear on the inverse: `(D2 B2 D F2 U' R2 F2 R2 U B2 D L2 D2 B2 L2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `L2 B2 D2 L2 D' B2 U' R2 F2 R2 U F2 D' B2 D2`.
- Class 4: normal first: `U2 R2 B2 D`, then on inverse `(R2 B2 U2 L2 U' D2 L2 F2 D2 R2 B2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U2 R2 B2 D B2 R2 D2 F2 L2 D2 U L2 U2 B2 R2`.
- Class 5: normal first: `U2 B2 U'`, then on inverse `(U2 L2 F2 U F2 D B2 F2 D L2 R2 B2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U2 B2 U' B2 R2 L2 D' F2 B2 D' F2 U' F2 L2 U2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `U2 R2 B2 U`; the reduced state is then solved by `R2 U2 R2 F2 D B2 U2 B2 L2 U2 R2` (11 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `U2 R2 B2 U R2 U2 R2 F2 D B2 U2 B2 L2 U2 R2` (15 moves, 2 quarter turns).

</details>

**4a2 4e, example 5.** `F2 U F2 R2 B2 L2 D2 L2 F2 U L2 B2 U' L2 B2 U F2 B2 U R2 U'`

Read as 4a2 4e on normal, 4a2 4e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (28 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4a1 > 0c0` | 60.9% | no / no |
| 2 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 72.2% | yes / yes |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 79.1% | no / no |
| 4 | `4a2 > 4a1 > (0c0)` | 83.7% | no / no |
| 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 85.3% | no / no |

- Class 2: normal first: `U R2 U2 L2 B2 U R2 U`, then on inverse `(F2 D L2 D2 L2 B2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U R2 U2 L2 B2 U R2 U B2 L2 D2 L2 D' F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `(D' B2 F2 D B2 D')`; the reduced state is then solved by `U2 B2 R2 U' F2 R2 D2 R2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `U (F2 D)`; the reduced state is then solved by `R2 U2 L2 B2 U R2 U B2 L2 D2 L2` (11 moves, 2 quarter turns).

</details>

**4a2 4e, example 6.** `F2 D B2 U2 D F2 U' D' R2 D' R2 D F2 B2 L2 D' B2 R2 D' R2 L2 U2`

Read as 4a2 4e on normal, 4a2 4e on inverse. Shortest HTR: 8 on normal, 5 on inverse, 5 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (40 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4a1 > 0c0` | 60.9% | yes / yes |
| 2 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 72.2% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 79.1% | no / no |
| 4 | `4a2 > 4a1 > (0c0)` | 83.7% | yes / yes |
| 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 85.3% | no / yes |

- Class 1: linear on the inverse: `(D F2 L2 U2 L2 D' B2 D2 B2 R2 F2 U2 R2)`. HTR after 6 moves (within the budget); the whole finish, as read on normal: `R2 U2 F2 R2 B2 D2 B2 D L2 U2 L2 F2 D'`.
- Class 4: normal first: `F2 R2 F2 U'`, then on inverse `(L2 R2 D' F2 L2 U2 B2 F2 L2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `F2 R2 F2 U' L2 F2 B2 U2 L2 F2 D R2 L2`.
- Class 5: normal first: `D'`, then on inverse `(D F2 R2 B2 U' L2 R2 D R2 F2 U2 B2)`. HTR after 9 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D' B2 U2 F2 R2 D' R2 L2 U B2 R2 F2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 1 move, `(D)`; the reduced state is then solved by `R2 U2 F2 R2 B2 D2 B2 D L2 U2 L2 F2` (12 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `R2 U2 F2 R2 B2 D2 B2 D L2 U2 L2 F2 D'` (13 moves, 2 quarter turns).

</details>

**4a2 4e, example 7.** `U' D' B2 D R2 U2 B2 L2 U2 F2 U' L2 F2 U2 B2 D F2 U2 B2 L2 D F2 R2 F2 U2`

Read as 4a2 4e on normal, 4a2 4e on inverse. Shortest HTR: 6 on normal, 6 on inverse, 5 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 10 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4a1 > 0c0` | 60.9% | yes / yes |
| 2 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 72.2% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 79.1% | no / no |
| 4 | `4a2 > 4a1 > (0c0)` | 83.7% | yes / yes |
| 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 85.3% | no / no |

- Class 1: linear on the inverse: `(F2 U' R2 F2 D2 F2 U' B2 F2 D2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `D2 F2 B2 U F2 D2 F2 R2 U F2`.
- Class 4: normal first: `D2 F2 B2 U`, then on inverse `(F2 U' R2 F2 D2 F2)`. HTR after 6 moves (within the budget); the whole finish, as read on normal: `D2 F2 B2 U F2 D2 F2 R2 U F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 2 moves, `(F2 U')`; the reduced state is then solved by `D2 F2 B2 U F2 D2 F2 R2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `D2 F2 B2 U F2 D2 F2 R2 U F2` (10 moves, 2 quarter turns).

</details>

**4a2 4e, example 8.** `D R2 B2 U' L2 U2 F2 U2 D2 B2 D' R2 F2 R2 L2 U' R2 F2 B2 D B2 L2 U F2`

Read as 4a2 4e on normal, 4a2 4e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4a1 > 0c0` | 60.9% | yes / yes |
| 2 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 72.2% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 79.1% | no / no |
| 4 | `4a2 > 4a1 > (0c0)` | 83.7% | yes / yes |
| 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 85.3% | no / no |

- Class 1: linear on normal: `R2 D2 B2 D' L2 U2 L2 F2 D' R2 B2 R2 F2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `R2 D2 B2 D' L2 U2 L2 F2 D' R2 B2 R2 F2`.
- Class 4: normal first: `R2 D2 B2 D'`, then on inverse `(F2 R2 B2 R2 D F2 L2 U2 L2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `R2 D2 B2 D' L2 U2 L2 F2 D' R2 B2 R2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `R2 D2 B2 D'`; the reduced state is then solved by `L2 U2 L2 F2 D' R2 B2 R2 F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `R2 D2 B2 D' L2 U2 L2 F2 D' R2 B2 R2 F2` (13 moves, 2 quarter turns).

</details>

**4a2 4e, example 9.** `R2 U D F2 U' B2 L2 D' B2 U F2 R2 D F2 B2 D F2 U' F2 U' L2 B2 U'`

Read as 4a2 4e on normal, 4a2 4e on inverse. Shortest HTR: 7 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (4 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4a1 > 0c0` | 60.9% | yes / yes |
| 2 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 72.2% | no / no |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 79.1% | no / no |
| 4 | `4a2 > 4a1 > (0c0)` | 83.7% | yes / yes |
| 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 85.3% | no / no |

- Class 1: linear on the inverse: `(U' B2 U2 B2 L2 D R2 B2 R2 U2 L2 U2)`. HTR after 6 moves (within the budget); the whole finish, as read on normal: `U2 L2 U2 R2 B2 R2 D' L2 B2 U2 B2 U`.
- Class 4: normal first: `U2 R2 U'`, then on inverse `(D2 L2 B2 R2 D' L2 D2 R2 F2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `U2 R2 U' F2 R2 D2 L2 D R2 B2 L2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 1 move, `(U')`; the reduced state is then solved by `U2 L2 U2 R2 B2 R2 D' L2 B2 U2 B2` (11 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `U2 R2 U' F2 R2 D2 L2 D R2 B2 L2 D2` (12 moves, 2 quarter turns).

</details>

**4a2 4e, example 10.** `U' D' F2 B2 U' D' R2 L2 U' F2 L2 F2 D F2 U' F2 D2 B2 R2 U L2 B2`

Read as 4a2 4e on normal, 4a2 4e on inverse. Shortest HTR: 10 on normal, 8 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (12 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a2 > 4a1 > 0c0` | 60.9% | no / no |
| 2 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` | 72.2% | yes / yes |
| 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 79.1% | no / no |
| 4 | `4a2 > 4a1 > (0c0)` | 83.7% | no / no |
| 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 85.3% | no / no |

- Class 2: inverse first: `(D' L2 R2 D' R2 D')`, then on normal `F2 L2 D L2 F2 D2 L2 F2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `F2 L2 D L2 F2 D2 L2 F2 D R2 D R2 L2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `(D' U' R2 U')`; the reduced state is then solved by `F2 L2 B2 L2 F2 U' B2 L2 U2 L2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 2 moves, `(D' U')`; the reduced state is then solved by `F2 L2 B2 L2 F2 U' B2 L2 U2 L2 U R2` (12 moves, 2 quarter turns).

</details>

## 4a1

### 4a1 4e

1.47% of all DR states.

**4a1 4e, example 1.** `U D' R2 F2 B2 R2 B2 U2 R2 D2 F2 R2 U L2 D R2 F2 L2 U'`

Read as 4a1 4e on normal, 4a1 4e on inverse. Shortest HTR: 6 on normal, 5 on inverse, 5 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 11 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a1 > 0c0` | 33.6% | no / no |
| 2 | `4a1 > 4b2 > 4a1 > 0c0` | 50.3% | no / no |
| 3 | `4a1 > 0c0 > (4a1 > 0c0)` | 60.6% | no / no |
| 4 | `4a1 > 0c0 > 4a1 > (0c0)` | 66.6% | no / no |
| 5 | `4a1 > 0c0 > 4a1 > 0c0` | 69.5% | no / no |

- None of these classes finds an optimal finish on this DR.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `F2 U (U' L2 U' R2 U')`; the reduced state is then solved by `R2 U' L2 F2` (4 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `(U' L2 U' R2 U')`; the reduced state is then solved by `F2 U R2 U' L2 F2` (6 moves, 2 quarter turns).

</details>

**4a1 4e, example 2.** `F2 B2 L2 U2 D' F2 U' R2 F2 L2 D' L2 D' B2 R2 F2 L2 U2 B2 U' R2 U2 F2 R2 L2`

Read as 4a1 4e on normal, 4a1 4e on inverse. Shortest HTR: 7 on normal, 7 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (19 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a1 > 0c0` | 33.6% | no / no |
| 2 | `4a1 > 4b2 > 4a1 > 0c0` | 50.3% | yes / yes |
| 3 | `4a1 > 0c0 > (4a1 > 0c0)` | 60.6% | no / yes |
| 4 | `4a1 > 0c0 > 4a1 > (0c0)` | 66.6% | no / yes |
| 5 | `4a1 > 0c0 > 4a1 > 0c0` | 69.5% | no / yes |

- Class 2: linear on the inverse: `(U' B2 L2 B2 U R2 U' B2 U2 L2 D2 R2 B2 L2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `L2 B2 R2 D2 L2 U2 B2 U R2 U' B2 L2 B2 U`.
- Class 3: normal first: `D2 B2 U2 F2 L2 D`, then on inverse `(D' F2 L2 F2 D B2 F2 L2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D2 B2 U2 F2 L2 D L2 F2 B2 D' F2 L2 F2 D`.
- Class 4: normal first: `L2 B2 R2 F2 U2 R2 D' B2 U`, then on inverse `(D' R2 B2 R2 D2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 R2 F2 U2 R2 D' B2 U D2 R2 B2 R2 D`.
- Class 5: linear on the inverse: `(D2 L2 B2 D B2 L2 D' B2 F2 D R2 B2 D2 L2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 D2 B2 R2 D' F2 B2 D L2 B2 D' B2 L2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `(D' F2 L2 F2 D)`; the reduced state is then solved by `D2 B2 U2 F2 L2 D L2 F2 B2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 1 move, `(D')`; the reduced state is then solved by `D2 B2 U2 F2 L2 D L2 F2 B2 D' F2 L2 F2` (13 moves, 2 quarter turns).

</details>

**4a1 4e, example 3.** `F2 R2 F2 D2 R2 L2 B2 R2 U2 R2 D L2 U2 R2 L2 F2 U F2 B2 U`

Read as 4a1 4e on normal, 4a1 4e on inverse. Shortest HTR: 4 on normal, 7 on inverse, 4 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (24 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a1 > 0c0` | 33.6% | yes / yes |
| 2 | `4a1 > 4b2 > 4a1 > 0c0` | 50.3% | no / yes |
| 3 | `4a1 > 0c0 > (4a1 > 0c0)` | 60.6% | no / yes |
| 4 | `4a1 > 0c0 > 4a1 > (0c0)` | 66.6% | no / yes |
| 5 | `4a1 > 0c0 > 4a1 > 0c0` | 69.5% | no / yes |

- Class 1: linear on normal: `R2 U2 B2 U D2 R2 B2 R2 B2 R2 U2 L2 U2`. HTR after 4 moves (within the budget); the whole finish, as read on normal: `R2 U2 B2 U D2 R2 B2 R2 B2 R2 U2 L2 U2`.
- Class 2: linear on the inverse: `(L2 D2 B2 L2 D U' L2 B2 D' B2 U2 B2 R2)`. HTR after 9 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U2 B2 D B2 L2 U D' L2 B2 D2 L2`.
- Class 3: inverse first: `(L2 D2 B2 L2 B2 R2 D')`, then on normal `U D' F2 R2 U2 R2`. HTR after 9 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U D' F2 R2 U2 R2 D R2 B2 L2 B2 D2 L2`.
- Class 4: normal first: `R2 B2 U2 B2 D B2 L2 U`, then on inverse `(L2 D2 B2 L2 D)`. HTR after 13 moves (9 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U2 B2 D B2 L2 U D' L2 B2 D2 L2`.
- Class 5: linear on normal: `R2 B2 U2 B2 D B2 L2 U D' L2 B2 D2 L2`. HTR after 9 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U2 B2 D B2 L2 U D' L2 B2 D2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `D2 F2 R2 U2 L2 U D2 R2 B2 R2 B2 D2 R2` (13 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 1 move, `U`; the reduced state is then solved by `D' F2 R2 U2 R2 D R2 B2 L2 B2 D2 L2` (12 moves, 2 quarter turns).

</details>

**4a1 4e, example 4.** `U2 D2 L2 U' D L2 D R2 L2 F2 U2 F2 D L2 U F2 B2 U2 B2 U' R2 U'`

Read as 4a1 4e on normal, 4a1 4e on inverse. Shortest HTR: 8 on normal, 7 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (15 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a1 > 0c0` | 33.6% | no / no |
| 2 | `4a1 > 4b2 > 4a1 > 0c0` | 50.3% | no / yes |
| 3 | `4a1 > 0c0 > (4a1 > 0c0)` | 60.6% | no / yes |
| 4 | `4a1 > 0c0 > 4a1 > (0c0)` | 66.6% | yes / yes |
| 5 | `4a1 > 0c0 > 4a1 > 0c0` | 69.5% | no / yes |

- Class 2: linear on the inverse: `(L2 U F2 L2 F2 L2 R2 U' R2 D2 R2 U' F2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U R2 D2 R2 U R2 L2 F2 L2 F2 U' L2`.
- Class 3: normal first: `F2 U`, then on inverse `(L2 U F2 L2 F2 L2 R2 U' R2 D2 R2)`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U R2 D2 R2 U R2 L2 F2 L2 F2 U' L2`.
- Class 4: normal first: `F2 U R2 D2 R2 U`, then on inverse `(L2 U F2 L2 F2 L2 R2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `F2 U R2 D2 R2 U R2 L2 F2 L2 F2 U' L2`.
- Class 5: linear on normal: `F2 U R2 D2 R2 U R2 L2 F2 L2 F2 U' L2`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U R2 D2 R2 U R2 L2 F2 L2 F2 U' L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `F2 U (L2 U)`; the reduced state is then solved by `R2 D2 R2 U R2 L2 F2 L2 F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 2 moves, `(L2 U)`; the reduced state is then solved by `F2 U R2 D2 R2 U R2 L2 F2 L2 F2` (11 moves, 2 quarter turns).

</details>

**4a1 4e, example 5.** `F2 U R2 U2 L2 U2 D2 B2 D R2 B2 U' F2 D2 B2 L2 D R2 B2 D' R2`

Read as 4a1 4e on normal, 4a1 4e on inverse. Shortest HTR: 5 on normal, 5 on inverse, 5 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 11 moves (20 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a1 > 0c0` | 33.6% | yes / yes |
| 2 | `4a1 > 4b2 > 4a1 > 0c0` | 50.3% | yes / yes |
| 3 | `4a1 > 0c0 > (4a1 > 0c0)` | 60.6% | no / yes |
| 4 | `4a1 > 0c0 > 4a1 > (0c0)` | 66.6% | no / yes |
| 5 | `4a1 > 0c0 > 4a1 > 0c0` | 69.5% | no / yes |

- Class 1: linear on the inverse: `(D2 F2 L2 R2 D' U2 B2 U2 L2 U2 R2)`. HTR after 5 moves (within the budget); the whole finish, as read on normal: `R2 U2 L2 U2 B2 U2 D R2 L2 F2 D2`.
- Class 2: linear on the inverse: `(D2 F2 R2 D' U B2 U' L2 U2 B2 R2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `R2 B2 U2 L2 U B2 U' D R2 F2 D2`.
- Class 3: normal first: `R2 B2 U2 L2 U`, then on inverse `(D2 F2 R2 D' U B2)`. HTR after 10 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U2 L2 U B2 U' D R2 F2 D2`.
- Class 4: normal first: `R2 B2 U2 L2 U B2 U'`, then on inverse `(D2 F2 R2 D')`. HTR after 11 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U2 L2 U B2 U' D R2 F2 D2`.
- Class 5: linear on normal: `R2 B2 U2 L2 U B2 U' D R2 F2 D2`. HTR after 8 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U2 L2 U B2 U' D R2 F2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `R2 U2 L2 U2 B2 U2 D R2 L2 F2 D2` (11 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `(D2 F2 R2 D')`; the reduced state is then solved by `R2 B2 U2 L2 U B2 U'` (7 moves, 2 quarter turns).

</details>

**4a1 4e, example 6.** `R2 U' D' F2 U' D2 F2 D2 R2 L2 F2 U' D' B2 R2 D' B2 U R2 D2 R2 U2`

Read as 4a1 4e on normal, 4a1 4e on inverse. Shortest HTR: 6 on normal, 2 on inverse, 2 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 11 moves (32 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a1 > 0c0` | 33.6% | yes / yes |
| 2 | `4a1 > 4b2 > 4a1 > 0c0` | 50.3% | no / no |
| 3 | `4a1 > 0c0 > (4a1 > 0c0)` | 60.6% | no / no |
| 4 | `4a1 > 0c0 > 4a1 > (0c0)` | 66.6% | no / no |
| 5 | `4a1 > 0c0 > 4a1 > 0c0` | 69.5% | no / no |

- Class 1: linear on the inverse: `(L2 D F2 L2 B2 D2 B2 F2 L2 D2 U2)`. HTR after 2 moves (within the budget); the whole finish, as read on normal: `U2 D2 L2 F2 B2 D2 B2 L2 F2 D' L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `U2 D2 L2 F2 B2 D2 B2 L2 F2 D' L2` (11 moves, 1 quarter turn).
- No optimal finish has a stretch with exactly 2 quarter turns and half turns around it.

</details>

**4a1 4e, example 7.** `U2 D' R2 U D2 L2 U D' F2 B2 D2 R2 D' L2 U' B2 L2 D2 R2 U' F2`

Read as 4a1 4e on normal, 4a1 4e on inverse. Shortest HTR: 7 on normal, 4 on inverse, 4 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (25 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a1 > 0c0` | 33.6% | yes / yes |
| 2 | `4a1 > 4b2 > 4a1 > 0c0` | 50.3% | no / yes |
| 3 | `4a1 > 0c0 > (4a1 > 0c0)` | 60.6% | no / yes |
| 4 | `4a1 > 0c0 > 4a1 > (0c0)` | 66.6% | no / yes |
| 5 | `4a1 > 0c0 > 4a1 > 0c0` | 69.5% | no / yes |

- Class 1: linear on the inverse: `(R2 U2 L2 R2 F2 U' D2 B2 L2 U2 R2 U2 R2)`. HTR after 6 moves (within the budget); the whole finish, as read on normal: `R2 U2 R2 U2 L2 B2 D2 U F2 R2 L2 U2 R2`.
- Class 2: linear on normal: `R2 U2 R2 B2 U D B2 R2 U' B2 U2 F2 R2`. HTR after 9 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U2 R2 B2 U D B2 R2 U' B2 U2 F2 R2`.
- Class 3: inverse first: `(R2 F2 U2 B2 U)`, then on normal `R2 U2 R2 B2 U D B2 R2`. HTR after 11 moves (7 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U2 R2 B2 U D B2 R2 U' B2 U2 F2 R2`.
- Class 4: inverse first: `(R2 F2 U2 B2 U R2 B2 D')`, then on normal `R2 U2 R2 B2 U`. HTR after 13 moves (9 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U2 R2 B2 U D B2 R2 U' B2 U2 F2 R2`.
- Class 5: linear on the inverse: `(R2 F2 U2 B2 U R2 B2 D' U' B2 R2 U2 R2)`. HTR after 9 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U2 R2 B2 U D B2 R2 U' B2 U2 F2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `R2 U2 R2 U2 L2 B2 U D2 F2 R2 L2 U2 R2` (13 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `D L2 U' (B2 D)`; the reduced state is then solved by `R2 D' L2 U' F2 L2 F2 L2` (8 moves, 2 quarter turns).

</details>

**4a1 4e, example 8.** `U D' B2 U D2 F2 B2 D' R2 B2 U2 F2 D' F2 L2 D2 R2 F2 U2 R2`

Read as 4a1 4e on normal, 4a1 4e on inverse. Shortest HTR: 7 on normal, 5 on inverse, 5 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (32 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a1 > 0c0` | 33.6% | yes / yes |
| 2 | `4a1 > 4b2 > 4a1 > 0c0` | 50.3% | no / yes |
| 3 | `4a1 > 0c0 > (4a1 > 0c0)` | 60.6% | no / yes |
| 4 | `4a1 > 0c0 > 4a1 > (0c0)` | 66.6% | no / yes |
| 5 | `4a1 > 0c0 > 4a1 > 0c0` | 69.5% | no / yes |

- Class 1: linear on the inverse: `(L2 B2 U2 L2 U' L2 U2 F2 R2 U2 B2 L2 R2)`. HTR after 5 moves (within the budget); the whole finish, as read on normal: `R2 L2 B2 U2 R2 F2 U2 L2 U L2 U2 B2 L2`.
- Class 2: linear on normal: `R2 D B2 L2 B2 D B2 U L2 U2 B2 L2 F2`. HTR after 8 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 D B2 L2 B2 D B2 U L2 U2 B2 L2 F2`.
- Class 3: normal first: `R2 B2 R2 D`, then on inverse `(L2 D L2 R2 U' F2 R2 D2 L2)`. HTR after 9 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 R2 D L2 D2 R2 F2 U R2 L2 D' L2`.
- Class 4: inverse first: `(F2 L2 B2 U2 L2 U' B2 D')`, then on normal `R2 D B2 L2 B2`. HTR after 10 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 D B2 L2 B2 D B2 U L2 U2 B2 L2 F2`.
- Class 5: linear on normal: `R2 B2 R2 D L2 D2 R2 F2 U R2 L2 D' L2`. HTR after 12 moves (7 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 R2 D L2 D2 R2 F2 U R2 L2 D' L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `R2 L2 B2 U2 R2 F2 U2 L2 U L2 U2 B2 L2` (13 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 2 moves, `R2 D`; the reduced state is then solved by `B2 L2 B2 D B2 U L2 U2 B2 L2 F2` (11 moves, 2 quarter turns).

</details>

**4a1 4e, example 9.** `U' D' R2 U F2 U B2 L2 D F2 U2 F2 U' R2 B2 R2 B2 D2 B2 D F2 U' D'`

Read as 4a1 4e on normal, 4a1 4e on inverse. Shortest HTR: 7 on normal, 8 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (5 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a1 > 0c0` | 33.6% | no / no |
| 2 | `4a1 > 4b2 > 4a1 > 0c0` | 50.3% | yes / yes |
| 3 | `4a1 > 0c0 > (4a1 > 0c0)` | 60.6% | yes / yes |
| 4 | `4a1 > 0c0 > 4a1 > (0c0)` | 66.6% | no / yes |
| 5 | `4a1 > 0c0 > 4a1 > 0c0` | 69.5% | no / yes |

- Class 2: linear on normal: `U2 R2 U' B2 L2 F2 D L2 D' L2 B2 L2 D2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U2 R2 U' B2 L2 F2 D L2 D' L2 B2 L2 D2`.
- Class 3: inverse first: `(D)`, then on normal `U2 F2 L2 D F2 B2 U' F2 R2 B2 D2 B2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `U2 F2 L2 D F2 B2 U' F2 R2 B2 D2 B2 D'`.
- Class 4: inverse first: `(D2 L2 B2 L2 D L2 D')`, then on normal `U2 R2 U' B2 L2 F2`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U2 R2 U' B2 L2 F2 D L2 D' L2 B2 L2 D2`.
- Class 5: linear on the inverse: `(D B2 D2 B2 R2 F2 U B2 F2 D' L2 F2 U2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U2 F2 L2 D F2 B2 U' F2 R2 B2 D2 B2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `U2 F2 L2 D (D)`; the reduced state is then solved by `F2 B2 U' F2 R2 B2 D2 B2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (0c0 4e here) on an optimal path: 1 move, `(D)`; the reduced state is then solved by `U2 F2 L2 D F2 B2 U' F2 R2 B2 D2 B2` (12 moves, 2 quarter turns).

</details>

**4a1 4e, example 10.** `B2 U' D' F2 R2 F2 D L2 U' F2 R2 D R2 D L2 B2 U' F2 R2 U2 R2`

Read as 4a1 4e on normal, 4a1 4e on inverse. Shortest HTR: 7 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (14 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a1 > 0c0` | 33.6% | no / no |
| 2 | `4a1 > 4b2 > 4a1 > 0c0` | 50.3% | no / yes |
| 3 | `4a1 > 0c0 > (4a1 > 0c0)` | 60.6% | no / yes |
| 4 | `4a1 > 0c0 > 4a1 > (0c0)` | 66.6% | no / yes |
| 5 | `4a1 > 0c0 > 4a1 > 0c0` | 69.5% | yes / yes |

- Class 2: linear on normal: `D' L2 F2 L2 D' F2 U2 F2 B2 U' F2 B2 R2`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D' L2 F2 L2 D' F2 U2 F2 B2 U' F2 B2 R2`.
- Class 3: inverse first: `(R2 B2 F2 U)`, then on normal `D' L2 F2 L2 D' F2 U2 F2 B2`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D' L2 F2 L2 D' F2 U2 F2 B2 U' F2 B2 R2`.
- Class 4: inverse first: `(R2 B2 F2 U B2 F2 U2 F2 D)`, then on normal `D' L2 F2 L2`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D' L2 F2 L2 D' F2 U2 F2 B2 U' F2 B2 R2`.
- Class 5: linear on the inverse: `(R2 D R2 U R2 B2 R2 U L2 R2 F2 D2 R2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `R2 D2 F2 R2 L2 U' R2 B2 R2 U' R2 D' R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `(R2 D R2 U)`; the reduced state is then solved by `R2 D2 F2 R2 L2 U' R2 B2 R2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 1 move, `D'`; the reduced state is then solved by `L2 F2 L2 D' F2 U2 F2 B2 U' F2 B2 R2` (12 moves, 2 quarter turns).

</details>

## 2c3

### 2c3 2e

3.48% of all DR states.

**2c3 2e, example 1.** `U' R2 F2 U' D2 R2 U2 R2 F2 B2 U B2 R2 B2 L2 D' L2 F2 U' D' R2 U`

Read as 2c3 2e on normal, 2c3 2e on inverse. Shortest HTR: 7 on normal, 7 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 79.6% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.6% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.8% | no / no |

- Class 1: linear on normal: `B2 U F2 L2 U' R2 D' U2 B2 D2 B2 R2`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `B2 U F2 L2 U' R2 D' U2 B2 D2 B2 R2`.
- Class 2: normal first: `B2 U`, then on inverse `(R2 B2 D2 B2 D U2 R2 U L2 F2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U F2 L2 U' R2 U2 D' B2 D2 B2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `B2 U F2 L2 U'`; the reduced state is then solved by `R2 U2 D' B2 D2 B2 R2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 2 moves, `B2 U`; the reduced state is then solved by `F2 L2 U' R2 U2 D' B2 D2 B2 R2` (10 moves, 2 quarter turns).

</details>

**2c3 2e, example 2.** `F2 D' B2 D2 R2 D2 R2 F2 D B2 L2 D R2 F2 B2 U' R2 U' F2 L2 U2 F2 U2`

Read as 2c3 2e on normal, 2c3 2e on inverse. Shortest HTR: 7 on normal, 7 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 79.6% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.6% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.8% | no / no |

- Class 1: linear on the inverse: `(F2 R2 D' L2 D F2 U F2 L2 F2 D2 B2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `B2 D2 F2 L2 F2 U' F2 D' L2 D R2 F2`.
- Class 2: normal first: `B2 D2 F2 L2 F2 U'`, then on inverse `(F2 R2 D' L2 D F2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 D2 F2 L2 F2 U' F2 D' L2 D R2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `(F2 R2 D' L2 D)`; the reduced state is then solved by `B2 D2 F2 L2 F2 U' F2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `(F2 R2 D')`; the reduced state is then solved by `B2 D2 F2 L2 F2 U' F2 D' L2` (9 moves, 2 quarter turns).

</details>

**2c3 2e, example 3.** `L2 U2 D' F2 B2 U' D R2 F2 U B2 R2 B2 D R2 U2 F2 D B2 D' R2`

Read as 2c3 2e on normal, 2c3 2e on inverse. Shortest HTR: 7 on normal, 7 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% | no / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 79.6% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.6% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.8% | no / no |

- Class 1: linear on the inverse: `(U2 L2 U F2 L2 R2 U' B2 R2 U' L2 U2 B2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U2 L2 U R2 B2 U R2 L2 F2 U' L2 U2`.
- Class 2: inverse first: `(U2 L2 U)`, then on normal `B2 U2 L2 U R2 B2 U R2 L2 F2`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U2 L2 U R2 B2 U R2 L2 F2 U' L2 U2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `(U2 L2 U F2 L2 R2 U')`; the reduced state is then solved by `B2 U2 L2 U R2 B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 3 moves, `(U2 L2 U)`; the reduced state is then solved by `B2 U2 L2 U R2 B2 U R2 L2 F2` (10 moves, 2 quarter turns).

</details>

**2c3 2e, example 4.** `F2 U D R2 U D' B2 U2 L2 U2 L2 U' F2 R2 B2 U2 B2 U R2 U' R2`

Read as 2c3 2e on normal, 2c3 2e on inverse. Shortest HTR: 6 on normal, 7 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (34 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 79.6% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / yes |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.6% | no / yes |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.8% | no / yes |

- Class 1: linear on the inverse: `(D2 F2 U R2 U' R2 U B2 F2 U2 L2 D2 R2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `R2 D2 L2 U2 F2 B2 U' R2 U R2 U' F2 D2`.
- Class 2: inverse first: `(D2 F2 U')`, then on normal `U2 R2 F2 B2 U' L2 U' R2 U2 L2`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U2 R2 F2 B2 U' L2 U' R2 U2 L2 U F2 D2`.
- Class 3: normal first: `R2 F2 B2 D2 L2 D`, then on inverse `(D' U' R2 D L2 D' B2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `R2 F2 B2 D2 L2 D B2 D L2 D' R2 U D`.
- Class 4: normal first: `R2 F2 B2 U' D'`, then on inverse `(U2 B2 U L2 D' B2 U' F2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `R2 F2 B2 U' D' F2 U B2 D L2 U' B2 U2`.
- Class 5: normal first: `U' L2 B2 U`, then on inverse `(F2 D2 L2 U F2 D R2 U' R2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `U' L2 B2 U R2 U R2 D' F2 U' L2 D2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `(F2 D' F2 U)`; the reduced state is then solved by `L2 B2 R2 L2 D2 B2 D' R2 F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 2 moves, `(F2 D')`; the reduced state is then solved by `L2 B2 R2 L2 D2 B2 D' R2 F2 U' F2` (11 moves, 2 quarter turns).

</details>

**2c3 2e, example 5.** `R2 L2 F2 B2 U' L2 U D L2 F2 R2 D B2 L2 U R2 U L2 D R2 U2 R2`

Read as 2c3 2e on normal, 2c3 2e on inverse. Shortest HTR: 7 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (11 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 79.6% | yes / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.6% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.8% | no / no |

- Class 1: linear on the inverse: `(U' F2 D B2 R2 D F2 R2 F2 U2 F2 D2 R2)`. HTR after 6 moves (within the budget); the whole finish, as read on normal: `R2 D2 F2 U2 F2 R2 F2 D' R2 B2 D' F2 U`.
- Class 2: inverse first: `(U2 F2 D)`, then on normal `B2 L2 U L2 U' F2 R2 B2 R2 U2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `B2 L2 U L2 U' F2 R2 B2 R2 U2 D' F2 U2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 3 moves, `(U' F2 D)`; the reduced state is then solved by `R2 D2 F2 U2 F2 R2 F2 D' R2 B2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 1 move, `(U')`; the reduced state is then solved by `R2 D2 F2 U2 F2 R2 F2 D' R2 B2 D' F2` (12 moves, 2 quarter turns).

</details>

**2c3 2e, example 6.** `U B2 R2 U2 D2 L2 F2 B2 U2 D2 F2 U' F2 L2 D2 F2 L2 U' R2 U R2 U`

Read as 2c3 2e on normal, 2c3 2e on inverse. Shortest HTR: 5 on normal, 7 on inverse, 5 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 11 moves (12 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 79.6% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.6% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.8% | no / no |

- Class 1: linear on normal: `U' R2 U' R2 U' D2 R2 B2 U2 L2 F2`. HTR after 5 moves (within the budget); the whole finish, as read on normal: `U' R2 U' R2 U' D2 R2 B2 U2 L2 F2`.
- Class 2: normal first: `D`, then on inverse `(F2 D2 F2 L2 D F2 U' B2 U2 F2)`. HTR after 8 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D F2 U2 B2 U F2 D' L2 F2 D2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 3 moves, `U' R2 U'`; the reduced state is then solved by `R2 U' D2 R2 B2 U2 L2 F2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 1 move, `U`; the reduced state is then solved by `D2 L2 U' L2 U R2 B2 U2 L2 F2` (10 moves, 2 quarter turns).

</details>

**2c3 2e, example 7.** `D R2 L2 U2 D2 F2 D' R2 D' B2 D' B2 D B2 R2 D B2 U' L2 U' R2 F2 D2 R2 U'`

Read as 2c3 2e on normal, 2c3 2e on inverse. Shortest HTR: 6 on normal, 8 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 79.6% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.6% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.8% | no / no |

- Class 1: linear on normal: `U R2 U' L2 B2 U B2 U2 R2 F2 R2 D2`. HTR after 6 moves (within the budget); the whole finish, as read on normal: `U R2 U' L2 B2 U B2 U2 R2 F2 R2 D2`.
- Class 2: inverse first: `(D2 R2 F2 R2 U2 B2 U')`, then on normal `U R2 U' L2 B2`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U R2 U' L2 B2 U B2 U2 R2 F2 R2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 3 moves, `U R2 U'`; the reduced state is then solved by `L2 B2 U B2 U2 R2 F2 R2 D2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 1 move, `U`; the reduced state is then solved by `R2 U' L2 B2 U B2 U2 R2 F2 R2 D2` (11 moves, 2 quarter turns).

</details>

**2c3 2e, example 8.** `L2 B2 U' D2 R2 U D2 R2 L2 B2 R2 D R2 U R2 U2 B2 D' R2 L2 B2 L2 U2`

Read as 2c3 2e on normal, 2c3 2e on inverse. Shortest HTR: 6 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (5 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 79.6% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / yes |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.6% | no / yes |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.8% | no / no |

- Class 1: linear on the inverse: `(D R2 F2 U L2 U' L2 B2 F2 U2 R2 F2 D2)`. HTR after 6 moves (within the budget); the whole finish, as read on normal: `D2 F2 R2 U2 F2 B2 L2 U L2 U' F2 R2 D'`.
- Class 2: inverse first: `(D)`, then on normal `D2 F2 R2 U2 F2 B2 L2 U L2 U' F2 R2`. HTR after 11 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `D2 F2 R2 U2 F2 B2 L2 U L2 U' F2 R2 D'`.
- Class 3: normal first: `B2 U`, then on inverse `(D R2 U' R2 F2 L2 B2 D L2 U L2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U L2 U' L2 D' B2 L2 F2 R2 U R2 D'`.
- Class 4: inverse first: `(D R2 U')`, then on normal `B2 U L2 U' L2 D' B2 L2 F2 R2`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U L2 U' L2 D' B2 L2 F2 R2 U R2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `(D R2 F2 U)`; the reduced state is then solved by `D2 F2 R2 U2 F2 B2 L2 U L2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 1 move, `(D)`; the reduced state is then solved by `D2 F2 R2 U2 F2 B2 L2 U L2 U' F2 R2` (12 moves, 2 quarter turns).

</details>

**2c3 2e, example 9.** `L2 B2 U B2 L2 U2 R2 L2 U D' R2 F2 U' D2 F2 R2 L2 D' F2 U' B2 L2 U'`

Read as 2c3 2e on normal, 2c3 2e on inverse. Shortest HTR: 7 on normal, 5 on inverse, 5 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (16 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 79.6% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / yes |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.6% | no / yes |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.8% | no / no |

- Class 1: linear on the inverse: `(U F2 D R2 D' B2 L2 B2 U2 B2 U2 F2 L2)`. HTR after 5 moves (within the budget); the whole finish, as read on normal: `L2 F2 U2 B2 U2 B2 L2 B2 D R2 D' F2 U'`.
- Class 2: inverse first: `(U')`, then on normal `R2 B2 U2 F2 D B2 D R2 L2 F2 R2 D2`. HTR after 8 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U2 F2 D B2 D R2 L2 F2 R2 D2 U`.
- Class 3: inverse first: `(D)`, then on normal `L2 B2 D F2 D' L2 F2 U F2 D R2 L2`. HTR after 11 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 D F2 D' L2 F2 U F2 D R2 L2 D'`.
- Class 4: normal first: `F2 B2 R2 B2 U' D'`, then on inverse `(B2 D' B2 D' R2 D' B2)`. HTR after 12 moves (7 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 R2 B2 U' D' B2 D R2 D B2 D B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 3 moves, `(U F2 D)`; the reduced state is then solved by `L2 F2 U2 B2 U2 B2 L2 B2 D R2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 1 move, `(U')`; the reduced state is then solved by `R2 B2 U2 F2 D B2 D R2 L2 F2 R2 D2` (12 moves, 2 quarter turns).

</details>

**2c3 2e, example 10.** `U' F2 U F2 U' R2 L2 D2 L2 U B2 U B2 D' F2 D' F2 U F2 U' F2`

Read as 2c3 2e on normal, 2c3 2e on inverse. Shortest HTR: 7 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (4 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 79.6% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.6% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 80.8% | no / no |

- Class 1: linear on the inverse: `(R2 U' F2 D2 B2 U' B2 U B2 F2 U2 B2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `B2 U2 F2 B2 U' B2 U B2 D2 F2 U R2`.
- Class 2: inverse first: `(R2 U')`, then on normal `B2 U2 F2 B2 U' B2 U B2 D2 F2`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U2 F2 B2 U' B2 U B2 D2 F2 U R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `(R2 U' F2 D2 B2 U')`; the reduced state is then solved by `B2 U2 F2 B2 U' B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 2 moves, `(R2 U')`; the reduced state is then solved by `B2 U2 F2 B2 U' B2 U B2 D2 F2` (10 moves, 2 quarter turns).

</details>

### 2c3 4e

7.84% of all DR states.

**2c3 4e, example 1.** `L2 U2 D2 L2 U2 R2 U2 D2 R2 D2 F2 U B2 D' B2 L2 U' L2 U' L2 U`

Read as 2c3 4e on normal, 2c3 4e on inverse. Shortest HTR: 8 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% | no / no |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 76.6% | no / no |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 78.1% | no / yes |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.1% | no / yes |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.9% | no / yes |

- Class 3: normal first: `B2 U'`, then on inverse `(D2 F2 R2 F2 U F2 D L2 U R2 U' B2)`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U' B2 U R2 U' L2 D' F2 U' F2 R2 F2 D2`.
- Class 4: normal first: `B2 U' B2 U`, then on inverse `(D2 F2 R2 F2 U F2 D L2 U R2)`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U' B2 U R2 U' L2 D' F2 U' F2 R2 F2 D2`.
- Class 5: inverse first: `(D2 F2 R2 F2 U F2 D)`, then on normal `B2 U' B2 U R2 U' L2`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U' B2 U R2 U' L2 D' F2 U' F2 R2 F2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `B2 U' B2 U R2 U' L2 D'`; the reduced state is then solved by `F2 U' F2 R2 F2 D2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `B2 U' B2 U R2 U'`; the reduced state is then solved by `L2 D' F2 U' F2 R2 F2 D2` (8 moves, 2 quarter turns).

</details>

**2c3 4e, example 2.** `F2 U' D' B2 D2 F2 D2 F2 R2 B2 U R2 B2 L2 F2 R2 D F2 D2 R2 L2 F2 U'`

Read as 2c3 4e on normal, 2c3 4e on inverse. Shortest HTR: 7 on normal, 8 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 76.6% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 78.1% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.1% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.9% | no / no |

- Class 1: linear on the inverse: `(U2 L2 U' B2 L2 D' B2 U L2 B2 U2 L2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `L2 U2 B2 L2 U' B2 D L2 B2 U L2 U2`.
- Class 2: inverse first: `(U2 L2 U')`, then on normal `L2 U2 B2 L2 U' B2 D L2 B2`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U2 B2 L2 U' B2 D L2 B2 U L2 U2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `(U2 L2 U' B2 L2 D')`; the reduced state is then solved by `L2 U2 B2 L2 U' B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `(U2 L2 U')`; the reduced state is then solved by `L2 U2 B2 L2 U' B2 D L2 B2` (9 moves, 2 quarter turns).

</details>

**2c3 4e, example 3.** `U2 D B2 U' F2 U2 R2 U R2 L2 D' F2 R2 F2 D2 R2 D R2 U L2 D'`

Read as 2c3 4e on normal, 2c3 4e on inverse. Shortest HTR: 8 on normal, 8 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (41 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 76.6% | yes / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 78.1% | no / yes |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.1% | no / yes |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.9% | no / no |

- Class 1: linear on normal: `D' R2 F2 B2 D L2 F2 U' R2 U2 R2 F2 B2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `D' R2 F2 B2 D L2 F2 U' R2 U2 R2 F2 B2`.
- Class 2: inverse first: `(U2 L2 D')`, then on normal `D L2 U2 R2 U F2 L2 B2 D2 F2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `D L2 U2 R2 U F2 L2 B2 D2 F2 D L2 U2`.
- Class 3: normal first: `D'`, then on inverse `(R2 D B2 F2 U L2 D L2 D' U2 L2 B2)`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D' B2 L2 U2 D L2 D' L2 U' F2 B2 D' R2`.
- Class 4: inverse first: `(R2 U L2 R2 U')`, then on normal `U' L2 F2 U' L2 U' F2 D2`. HTR after 11 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U' L2 F2 U' L2 U' F2 D2 U R2 L2 U' R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `D (U2 L2 D')`; the reduced state is then solved by `L2 U2 R2 U F2 L2 B2 D2 F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 1 move, `D`; the reduced state is then solved by `L2 U2 R2 U F2 L2 B2 D2 F2 D L2 U2` (12 moves, 2 quarter turns).

</details>

**2c3 4e, example 4.** `B2 R2 U F2 R2 U' D2 F2 D F2 D2 L2 B2 L2 U L2 U F2 D' L2 U B2 L2 D2`

Read as 2c3 4e on normal, 2c3 4e on inverse. Shortest HTR: 7 on normal, 8 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (28 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% | no / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 76.6% | yes / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 78.1% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.1% | no / yes |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.9% | no / no |

- Class 1: linear on the inverse: `(B2 D L2 D R2 B2 L2 U2 L2 U B2 F2 D2)`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D2 F2 B2 U' L2 U2 L2 B2 R2 D' L2 D' B2`.
- Class 2: normal first: `D'`, then on inverse `(R2 F2 D' R2 U' F2 D2 F2 R2 D2 F2 L2)`. HTR after 6 moves (within the budget); the whole finish, as read on normal: `D' L2 F2 D2 R2 F2 D2 F2 U R2 D F2 R2`.
- Class 4: inverse first: `(B2 D R2 F2 D)`, then on normal `U B2 U' F2 D' L2 F2 R2`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 U' F2 D' L2 F2 R2 D' F2 R2 D' B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 3 moves, `U F2 D`; the reduced state is then solved by `R2 F2 U2 R2 B2 D2 F2 U' B2 L2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 1 move, `U`; the reduced state is then solved by `F2 D R2 F2 U2 R2 B2 D2 F2 U' B2 L2` (12 moves, 2 quarter turns).

</details>

**2c3 4e, example 5.** `F2 D' F2 B2 R2 L2 F2 B2 D' F2 B2 L2 F2 U' F2 U B2 R2 F2 L2 D'`

Read as 2c3 4e on normal, 2c3 4e on inverse. Shortest HTR: 7 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% | no / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 76.6% | yes / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 78.1% | no / yes |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.1% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.9% | no / yes |

- Class 1: linear on normal: `F2 U D2 B2 L2 F2 R2 U B2 D' R2 F2 U2`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U D2 B2 L2 F2 R2 U B2 D' R2 F2 U2`.
- Class 2: normal first: `F2 U`, then on inverse `(U2 F2 R2 D B2 U' R2 F2 L2 B2 D2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `F2 U D2 B2 L2 F2 R2 U B2 D' R2 F2 U2`.
- Class 3: normal first: `D`, then on inverse `(L2 B2 U R2 F2 R2 D' F2 U R2 U' R2)`. HTR after 12 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `D R2 U R2 U' F2 D R2 F2 R2 U' B2 L2`.
- Class 5: inverse first: `(L2 B2 U R2 F2 R2 D')`, then on normal `D R2 U R2 U' F2`. HTR after 12 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `D R2 U R2 U' F2 D R2 F2 R2 U' B2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `(U2 F2 R2 D B2 U')`; the reduced state is then solved by `F2 U D2 B2 L2 F2 R2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 2 moves, `F2 U`; the reduced state is then solved by `D2 B2 L2 F2 R2 U B2 D' R2 F2 U2` (11 moves, 2 quarter turns).

</details>

**2c3 4e, example 6.** `U2 D R2 D2 R2 L2 U D' B2 U' F2 L2 D' R2 D' R2 F2 B2 U`

Read as 2c3 4e on normal, 2c3 4e on inverse. Shortest HTR: 8 on normal, 7 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 11 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 76.6% | yes / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 78.1% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.1% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.9% | no / no |

- Class 1: linear on the inverse: `(F2 D2 U R2 D' L2 B2 D' R2 D2 R2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `R2 D2 R2 D B2 L2 D R2 U' D2 F2`.
- Class 2: normal first: `R2 D2 R2 D`, then on inverse `(F2 D2 U R2 D' L2 B2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `R2 D2 R2 D B2 L2 D R2 U' D2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `(F2 D2 U R2 D')`; the reduced state is then solved by `R2 D2 R2 D B2 L2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 2 moves, `(F2 U)`; the reduced state is then solved by `R2 D2 R2 D B2 L2 D R2 D2` (9 moves, 2 quarter turns).

</details>

**2c3 4e, example 7.** `D' F2 D2 L2 D2 R2 U2 D2 F2 B2 D2 F2 B2 D' L2 D' F2 D2 R2`

Read as 2c3 4e on normal, 2c3 4e on inverse. Shortest HTR: 6 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% | yes / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 76.6% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 78.1% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.1% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.9% | no / no |

- Class 1: linear on normal: `B2 L2 U' R2 U B2 L2 D F2 D2 L2 F2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `B2 L2 U' R2 U B2 L2 D F2 D2 L2 F2`.
- Class 2: inverse first: `(F2 L2 D2 F2 D')`, then on normal `B2 L2 U' R2 U B2 L2`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 L2 U' R2 U B2 L2 D F2 D2 L2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `B2 L2 U' R2 U`; the reduced state is then solved by `B2 L2 D F2 D2 L2 F2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 3 moves, `B2 L2 U'`; the reduced state is then solved by `R2 U B2 L2 D F2 D2 L2 F2` (9 moves, 2 quarter turns).

</details>

**2c3 4e, example 8.** `U' D' R2 U2 D R2 U D' B2 R2 L2 D F2 U2 L2 D L2 U L2 F2 L2 U2 B2 U'`

Read as 2c3 4e on normal, 2c3 4e on inverse. Shortest HTR: 7 on normal, 8 on inverse, 5 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (21 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% | no / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 76.6% | yes / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 78.1% | no / no |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.1% | no / yes |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.9% | no / no |

- Class 1: linear on normal: `U' F2 D2 F2 R2 B2 L2 U B2 U2 B2 U R2`. HTR after 12 moves (7 over the shortest NISS HTR); the whole finish, as read on normal: `U' F2 D2 F2 R2 B2 L2 U B2 U2 B2 U R2`.
- Class 2: normal first: `U'`, then on inverse `(R2 U' B2 U2 B2 U' L2 B2 R2 F2 D2 F2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `U' F2 D2 F2 R2 B2 L2 U B2 U2 B2 U R2`.
- Class 4: normal first: `D F2 U'`, then on inverse `(L2 D L2 F2 U F2 U F2 L2 F2)`. HTR after 10 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `D F2 U' F2 L2 F2 U' F2 U' F2 L2 D' L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 3 moves, `U' (R2 U')`; the reduced state is then solved by `F2 D2 F2 R2 B2 L2 U B2 U2 B2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 1 move, `U'`; the reduced state is then solved by `F2 D2 F2 R2 B2 L2 U B2 U2 B2 U R2` (12 moves, 2 quarter turns).

</details>

**2c3 4e, example 9.** `U2 L2 U2 R2 L2 U' L2 U2 L2 F2 D2 B2 D B2 U2 L2 F2 L2 U2 F2 D F2`

Read as 2c3 4e on normal, 2c3 4e on inverse. Shortest HTR: 7 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (38 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% | no / yes |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 76.6% | yes / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 78.1% | no / yes |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.1% | no / no |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.9% | no / yes |

- Class 1: linear on the inverse: `(R2 D F2 U' L2 F2 R2 F2 R2 U' L2 U2 B2 U2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U2 B2 U2 L2 U R2 F2 R2 F2 L2 U F2 D' R2`.
- Class 2: inverse first: `(R2 D')`, then on normal `R2 U2 F2 D' R2 D R2 L2 F2 U2 F2 B2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `R2 U2 F2 D' R2 D R2 L2 F2 U2 F2 B2 D R2`.
- Class 3: inverse first: `(B2 F2 R2 U)`, then on normal `R2 U' R2 L2 U' L2 U' B2 U L2`. HTR after 13 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U' R2 L2 U' L2 U' B2 U L2 U' R2 F2 B2`.
- Class 5: normal first: `R2 U' R2 L2 U'`, then on inverse `(B2 F2 R2 U L2 U' B2 U L2)`. HTR after 13 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U' R2 L2 U' L2 U' B2 U L2 U' R2 F2 B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `(R2 D F2 U')`; the reduced state is then solved by `U2 B2 U2 L2 U R2 F2 R2 F2 L2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 2 moves, `(R2 D)`; the reduced state is then solved by `U2 B2 U2 L2 U R2 F2 R2 F2 L2 U F2` (12 moves, 2 quarter turns).

</details>

**2c3 4e, example 10.** `U D B2 D2 R2 L2 B2 L2 D2 F2 B2 U F2 U B2 U2 F2 B2 L2 F2 U R2 L2`

Read as 2c3 4e on normal, 2c3 4e on inverse. Shortest HTR: 6 on normal, 8 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% | no / no |
| 2 | `2c3 > 4b2 > (4a1 > 0c0)` | 76.6% | no / no |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 78.1% | no / yes |
| 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.1% | no / yes |
| 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.9% | no / no |

- Class 3: inverse first: `(R2 D')`, then on normal `D B2 U' B2 U' B2 U R2 L2 D2 R2`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D B2 U' B2 U' B2 U R2 L2 D2 R2 D R2`.
- Class 4: normal first: `D B2 U'`, then on inverse `(R2 D' R2 D2 L2 R2 U' B2 U B2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `D B2 U' B2 U' B2 U R2 L2 D2 R2 D R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `D B2 U' B2 U' (R2 D')`; the reduced state is then solved by `B2 U R2 L2 D2 R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `D B2 U' (R2 D')`; the reduced state is then solved by `B2 U' B2 U R2 L2 D2 R2` (8 moves, 2 quarter turns).

</details>

### 2c3 6e

3.48% of all DR states.

**2c3 6e, example 1.** `B2 U F2 B2 U L2 D2 R2 D' L2 B2 D B2 L2 D2 F2 B2 D' F2 R2 L2 D2`

Read as 2c3 6e on normal, 2c3 6e on inverse. Shortest HTR: 8 on normal, 7 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > (4a1 > 0c0)` | 66.1% | yes / yes |
| 2 | `2c3 > 4b2 > 4a1 > 0c0` | 73.3% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 76.7% | no / no |
| 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.3% | no / no |
| 5 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.8% | no / no |

- Class 1: normal first: `L2 F2 U'`, then on inverse `(U2 F2 U L2 D B2 R2 B2 F2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `L2 F2 U' F2 B2 R2 B2 D' L2 U' F2 U2`.
- Class 2: linear on normal: `L2 F2 U' F2 B2 R2 B2 D' L2 U' F2 U2`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 F2 U' F2 B2 R2 B2 D' L2 U' F2 U2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `(U2 F2 U L2 D)`; the reduced state is then solved by `L2 F2 U' F2 B2 R2 B2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 3 moves, `(U2 F2 U)`; the reduced state is then solved by `L2 F2 U' F2 B2 R2 B2 D' L2` (9 moves, 2 quarter turns).

</details>

**2c3 6e, example 2.** `U' R2 F2 U' F2 U F2 B2 D B2 R2 F2 L2 B2 D' F2 D R2 D2 B2 U' B2 U F2 U'`

Read as 2c3 6e on normal, 2c3 6e on inverse. Shortest HTR: 8 on normal, 8 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (13 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > (4a1 > 0c0)` | 66.1% | no / no |
| 2 | `2c3 > 4b2 > 4a1 > 0c0` | 73.3% | no / no |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 76.7% | no / yes |
| 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.3% | no / yes |
| 5 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.8% | no / yes |

- Class 3: normal first: `F2 L2 U`, then on inverse `(U L2 D F2 D L2 B2 D R2 D2)`. HTR after 11 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 U D2 R2 D' B2 L2 D' F2 D' L2 U'`.
- Class 4: inverse first: `(U L2 D)`, then on normal `U' R2 U' F2 L2 D L2 F2 D2 F2`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' R2 U' F2 L2 D L2 F2 D2 F2 D' L2 U'`.
- Class 5: normal first: `F2 L2 U' L2 D'`, then on inverse `(U L2 D F2 D' U2 R2 F2)`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 U' L2 D' F2 R2 U2 D F2 D' L2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `U' R2 U' (U L2 D)`; the reduced state is then solved by `F2 L2 D L2 F2 D2 F2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 4 moves, `U' (U L2 D)`; the reduced state is then solved by `R2 U' F2 L2 D L2 F2 D2 F2` (9 moves, 2 quarter turns).

</details>

**2c3 6e, example 3.** `U' F2 U D' B2 U B2 D2 R2 U L2 U R2 F2 R2 D2 F2 U' R2 B2`

Read as 2c3 6e on normal, 2c3 6e on inverse. Shortest HTR: 8 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (15 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > (4a1 > 0c0)` | 66.1% | yes / yes |
| 2 | `2c3 > 4b2 > 4a1 > 0c0` | 73.3% | yes / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 76.7% | no / yes |
| 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.3% | no / yes |
| 5 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.8% | no / yes |

- Class 1: inverse first: `(L2 U)`, then on normal `B2 L2 D2 B2 U' L2 D U2 B2 R2 B2 L2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `B2 L2 D2 B2 U' L2 D U2 B2 R2 B2 L2 U' L2`.
- Class 2: linear on the inverse: `(L2 U L2 B2 R2 B2 U F2 D' R2 D2 F2 U2 B2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `B2 U2 F2 D2 R2 D F2 U' B2 R2 B2 L2 U' L2`.
- Class 3: normal first: `L2 D`, then on inverse `(D2 F2 U' F2 U L2 U B2 U R2 U2 F2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 D F2 U2 R2 U' B2 U' L2 U' F2 U F2 D2`.
- Class 4: normal first: `U' R2 D`, then on inverse `(B2 F2 L2 U' B2 R2 U' B2 R2 D' R2)`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U' R2 D R2 D R2 B2 U R2 B2 U L2 F2 B2`.
- Class 5: inverse first: `(B2 F2 L2 U' B2 R2 U')`, then on normal `U' R2 D R2 D R2 B2`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U' R2 D R2 D R2 B2 U R2 B2 U L2 F2 B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `B2 L2 D' B2 L2 U`; the reduced state is then solved by `D2 B2 L2 U F2 L2 D2 R2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 2 moves, `(L2 U)`; the reduced state is then solved by `B2 U2 F2 D2 R2 D F2 U' B2 R2 B2 L2` (12 moves, 2 quarter turns).

</details>

**2c3 6e, example 4.** `L2 D2 B2 R2 U' D' L2 U2 B2 D F2 R2 D2 R2 U' R2 U L2 F2 U' B2 D`

Read as 2c3 6e on normal, 2c3 6e on inverse. Shortest HTR: 9 on normal, 7 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > (4a1 > 0c0)` | 66.1% | yes / yes |
| 2 | `2c3 > 4b2 > 4a1 > 0c0` | 73.3% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 76.7% | no / yes |
| 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.3% | no / yes |
| 5 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.8% | no / yes |

- Class 1: inverse first: `(U')`, then on normal `F2 R2 D2 R2 D' F2 D U2 L2 F2 R2 F2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `F2 R2 D2 R2 D' F2 D U2 L2 F2 R2 F2 U`.
- Class 2: linear on the inverse: `(U' F2 R2 F2 L2 D' U2 F2 D R2 D2 R2 F2)`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 R2 D2 R2 D' F2 U2 D L2 F2 R2 F2 U`.
- Class 3: normal first: `F2 B2 L2 U`, then on inverse `(B2 D B2 D B2 D R2 U B2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 L2 U B2 U' R2 D' B2 D' B2 D' B2`.
- Class 4: normal first: `F2 B2 U' B2 R2 D'`, then on inverse `(B2 D' L2 U' L2 U F2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 U' B2 R2 D' F2 U' L2 U L2 D B2`.
- Class 5: normal first: `F2 B2 L2 U B2 U'`, then on inverse `(B2 D B2 D B2 D R2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 L2 U B2 U' R2 D' B2 D' B2 D' B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `(U' F2 R2 F2 L2 D')`; the reduced state is then solved by `F2 R2 D2 R2 D' F2 U2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 1 move, `(U')`; the reduced state is then solved by `F2 R2 D2 R2 D' F2 U2 D L2 F2 R2 F2` (12 moves, 2 quarter turns).

</details>

**2c3 6e, example 5.** `L2 D2 L2 U' D2 F2 L2 U F2 B2 U2 F2 D' L2 U' B2 L2 B2 L2 U2 L2 U' R2`

Read as 2c3 6e on normal, 2c3 6e on inverse. Shortest HTR: 8 on normal, 7 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (28 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > (4a1 > 0c0)` | 66.1% | no / yes |
| 2 | `2c3 > 4b2 > 4a1 > 0c0` | 73.3% | yes / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 76.7% | no / yes |
| 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.3% | no / no |
| 5 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.8% | no / yes |

- Class 1: normal first: `L2 U`, then on inverse `(B2 L2 D U2 L2 B2 U R2 F2 L2 B2 R2)`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U R2 B2 L2 F2 R2 U' B2 L2 U2 D' L2 B2`.
- Class 2: linear on the inverse: `(D' L2 R2 B2 U' R2 U' B2 L2 B2 R2 F2 U2 L2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `L2 U2 F2 R2 B2 L2 B2 U R2 U B2 R2 L2 D`.
- Class 3: normal first: `L2 D`, then on inverse `(B2 D' L2 R2 D B2 D' F2 L2 D' U2 L2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `L2 D L2 U2 D L2 F2 D B2 D' R2 L2 D B2`.
- Class 5: inverse first: `(B2 D' L2 R2 U)`, then on normal `L2 U B2 D' F2 R2 D' U2 R2`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U B2 D' F2 R2 D' U2 R2 U' R2 L2 D B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `L2 U (B2 L2 D)`; the reduced state is then solved by `R2 B2 L2 F2 R2 U' B2 L2 U2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 1 move, `(D')`; the reduced state is then solved by `L2 U2 F2 R2 B2 L2 B2 U R2 U B2 R2 L2` (13 moves, 2 quarter turns).

</details>

**2c3 6e, example 6.** `U B2 U' L2 D R2 L2 F2 L2 B2 D2 L2 B2 D' R2 F2 R2 B2 U2 R2 D R2 U2 B2 U2`

Read as 2c3 6e on normal, 2c3 6e on inverse. Shortest HTR: 8 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > (4a1 > 0c0)` | 66.1% | no / yes |
| 2 | `2c3 > 4b2 > 4a1 > 0c0` | 73.3% | yes / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 76.7% | no / no |
| 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.3% | no / no |
| 5 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.8% | no / no |

- Class 1: normal first: `B2 D'`, then on inverse `(D2 F2 L2 D2 R2 U' B2 D' L2 B2 F2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 D' F2 B2 L2 D B2 U R2 D2 L2 F2 D2`.
- Class 2: linear on normal: `B2 D' F2 B2 L2 D B2 U R2 D2 L2 F2 D2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `B2 D' F2 B2 L2 D B2 U R2 D2 L2 F2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `B2 D' F2 B2 L2 D`; the reduced state is then solved by `B2 U R2 D2 L2 F2 D2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 2 moves, `B2 D'`; the reduced state is then solved by `F2 B2 L2 D B2 U R2 D2 L2 F2 D2` (11 moves, 2 quarter turns).

</details>

**2c3 6e, example 7.** `F2 B2 R2 B2 R2 U' R2 D2 L2 F2 B2 U' F2 U' R2 F2 B2 D2 R2 U R2 U'`

Read as 2c3 6e on normal, 2c3 6e on inverse. Shortest HTR: 7 on normal, 9 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > (4a1 > 0c0)` | 66.1% | yes / yes |
| 2 | `2c3 > 4b2 > 4a1 > 0c0` | 73.3% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 76.7% | no / no |
| 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.3% | no / no |
| 5 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.8% | no / no |

- Class 1: inverse first: `(B2 R2 U)`, then on normal `D' F2 U' B2 R2 U2 L2 U2 L2`. HTR after 6 moves (within the budget); the whole finish, as read on normal: `D' F2 U' B2 R2 U2 L2 U2 L2 U' R2 B2`.
- Class 2: linear on normal: `D' F2 U' B2 R2 U2 L2 U2 L2 U' R2 B2`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D' F2 U' B2 R2 U2 L2 U2 L2 U' R2 B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 3 moves, `D' F2 U'`; the reduced state is then solved by `B2 R2 U2 L2 U2 L2 U' R2 B2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 1 move, `D'`; the reduced state is then solved by `F2 U' B2 R2 U2 L2 U2 L2 U' R2 B2` (11 moves, 2 quarter turns).

</details>

**2c3 6e, example 8.** `B2 D' L2 U L2 D' R2 L2 U' B2 R2 B2 U2 F2 R2 U' B2 U' F2 L2 D2 R2 D R2`

Read as 2c3 6e on normal, 2c3 6e on inverse. Shortest HTR: 8 on normal, 8 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (89 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > (4a1 > 0c0)` | 66.1% | yes / yes |
| 2 | `2c3 > 4b2 > 4a1 > 0c0` | 73.3% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 76.7% | no / yes |
| 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.3% | no / yes |
| 5 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.8% | no / yes |

- Class 1: normal first: `U2 R2 L2 U`, then on inverse `(F2 L2 U R2 U B2 F2 D2 B2 L2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U2 R2 L2 U L2 B2 D2 F2 B2 U' R2 U' L2 F2`.
- Class 2: linear on normal: `U' F2 B2 R2 D' L2 F2 R2 F2 D' B2 R2 F2 R2`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' F2 B2 R2 D' L2 F2 R2 F2 D' B2 R2 F2 R2`.
- Class 3: normal first: `R2 B2 U'`, then on inverse `(R2 U' F2 D L2 F2 U' F2 D' F2 L2)`. HTR after 12 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U' L2 F2 D F2 U F2 L2 D' F2 U R2`.
- Class 4: inverse first: `(D B2 F2 L2 D')`, then on normal `B2 U' F2 D' B2 R2 D' R2 F2`. HTR after 12 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U' F2 D' B2 R2 D' R2 F2 D L2 F2 B2 D'`.
- Class 5: normal first: `R2 U' B2 U'`, then on inverse `(F2 D' B2 L2 D' L2 D' F2 L2 R2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U' B2 U' R2 L2 F2 D L2 D L2 B2 D F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `B2 U F2 D`; the reduced state is then solved by `B2 L2 D2 F2 B2 U F2 D2 R2 F2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 1 move, `U'`; the reduced state is then solved by `F2 B2 R2 D' L2 F2 R2 F2 D' B2 R2 F2 R2` (13 moves, 2 quarter turns).

</details>

**2c3 6e, example 9.** `U2 F2 B2 U D' L2 U2 L2 U2 D2 L2 D R2 F2 B2 U' D2 B2 R2 F2 R2 U F2 D2`

Read as 2c3 6e on normal, 2c3 6e on inverse. Shortest HTR: 8 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > (4a1 > 0c0)` | 66.1% | no / no |
| 2 | `2c3 > 4b2 > 4a1 > 0c0` | 73.3% | no / no |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 76.7% | no / yes |
| 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.3% | no / yes |
| 5 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.8% | no / yes |

- Class 3: normal first: `F2 U'`, then on inverse `(U' B2 D L2 U2 L2 U R2 D B2 R2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' R2 B2 D' R2 U' L2 U2 L2 D' B2 U`.
- Class 4: inverse first: `(U' B2 D)`, then on normal `F2 U' R2 B2 D' R2 U' L2 U2 L2`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' R2 B2 D' R2 U' L2 U2 L2 D' B2 U`.
- Class 5: normal first: `F2 U' R2 B2 D'`, then on inverse `(U' B2 D L2 U2 L2 U R2)`. HTR after 12 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' R2 B2 D' R2 U' L2 U2 L2 D' B2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `F2 U' R2 B2 D' (U' B2 D)`; the reduced state is then solved by `R2 U' L2 U2 L2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `F2 U' (U' B2 D)`; the reduced state is then solved by `R2 B2 D' R2 U' L2 U2 L2` (8 moves, 2 quarter turns).

</details>

**2c3 6e, example 10.** `L2 B2 U D F2 B2 R2 F2 D2 F2 U' F2 R2 D' L2 F2 U' D2 R2`

Read as 2c3 6e on normal, 2c3 6e on inverse. Shortest HTR: 8 on normal, 8 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (48 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `2c3 > 4b2 > (4a1 > 0c0)` | 66.1% | yes / yes |
| 2 | `2c3 > 4b2 > 4a1 > 0c0` | 73.3% | no / yes |
| 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 76.7% | yes / yes |
| 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.3% | yes / yes |
| 5 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 79.8% | no / yes |

- Class 1: normal first: `L2 D`, then on inverse `(U2 L2 U B2 U' B2 L2 U2 F2 R2 D2 F2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `L2 D F2 D2 R2 F2 U2 L2 B2 U B2 U' L2 U2`.
- Class 2: linear on normal: `L2 U' B2 U2 L2 F2 L2 D F2 U2 B2 U R2 D2`. HTR after 12 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U' B2 U2 L2 F2 L2 D F2 U2 B2 U R2 D2`.
- Class 3: normal first: `U`, then on inverse `(U' B2 F2 U B2 U' L2 D' U2 L2 R2 F2 L2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U L2 F2 R2 L2 U2 D L2 U B2 U' F2 B2 U`.
- Class 4: inverse first: `(U' B2 F2 D)`, then on normal `D L2 U B2 D U2 F2 R2 B2 R2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `D L2 U B2 D U2 F2 R2 B2 R2 D' F2 B2 U`.
- Class 5: normal first: `R2 U R2 U`, then on inverse `(D2 L2 U R2 U B2 U R2 B2 R2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U R2 U R2 B2 R2 U' B2 U' R2 U' L2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `L2 U' (D2 R2 U')`; the reduced state is then solved by `B2 U2 L2 F2 L2 D F2 U2 B2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 2 moves, `L2 U'`; the reduced state is then solved by `B2 U2 L2 F2 L2 D F2 U2 B2 U R2 D2` (12 moves, 2 quarter turns).

</details>

## 4c3

### 4c3 2e

5.22% of all DR states.

**4c3 2e, example 1.** `D F2 U' D F2 R2 D R2 D L2 U2 F2 R2 B2 D L2 B2 U2 B2 U B2 U2 R2`

Read as 4a3 2e on normal, 4b3 2e on inverse. Shortest HTR: 10 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (39 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 66.2% | yes / yes |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 72.0% | no / yes |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 75.1% | no / yes |
| 4 | `4b3 > 4a2 > 4a1 > 0c0` | 77.9% | yes / yes |
| 5 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 80.1% | no / yes |

- Class 1: normal first: `U2 L2 D'`, then on inverse `(D2 F2 U B2 L2 D B2 U2 L2 F2 R2 B2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U2 L2 D' B2 R2 F2 L2 U2 B2 D' L2 B2 U' F2 D2`.
- Class 2: inverse first: `(B2 D' B2 D')`, then on normal `R2 D' B2 L2 U' R2 D' R2 D2 R2 F2`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 D' B2 L2 U' R2 D' R2 D2 R2 F2 D B2 D B2`.
- Class 3: normal first: `F2 D2 R2 U L2 U'`, then on inverse `(L2 D' B2 L2 D R2 U B2 F2)`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 D2 R2 U L2 U' F2 B2 U' R2 D' L2 B2 D L2`.
- Class 4: linear on the inverse: `(L2 D' L2 U' L2 U2 F2 D' B2 R2 U2 B2 F2 L2 U2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `U2 L2 F2 B2 U2 R2 B2 D F2 U2 L2 U L2 D L2`.
- Class 5: linear on the inverse: `(U F2 D R2 D2 B2 U L2 D R2 U' F2 R2 B2 R2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 R2 F2 U R2 D' L2 U' B2 D2 R2 D' F2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `(L2 D' L2 U')`; the reduced state is then solved by `U2 L2 F2 B2 U2 R2 B2 D F2 U2 L2` (11 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 2 moves, `(L2 D')`; the reduced state is then solved by `U2 L2 F2 B2 U2 R2 B2 D F2 U2 L2 U L2` (13 moves, 2 quarter turns).

</details>

**4c3 2e, example 2.** `U2 D B2 R2 U' R2 B2 D' B2 U2 B2 U R2 U' L2 F2 L2 U' R2 U L2 U2 R2`

Read as 4a3 2e on normal, 4b3 2e on inverse. Shortest HTR: 9 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (19 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 66.2% | no / yes |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 72.0% | yes / yes |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 75.1% | no / yes |
| 4 | `4b3 > 4a2 > 4a1 > 0c0` | 77.9% | yes / yes |
| 5 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 80.1% | no / yes |

- Class 1: normal first: `U2 F2 U2 R2 F2 L2 D'`, then on inverse `(R2 U F2 U L2 F2 U2 B2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U2 F2 U2 R2 F2 L2 D' B2 U2 F2 L2 U' F2 U' R2`.
- Class 2: inverse first: `(D' F2 R2 U)`, then on normal `D L2 U' R2 U R2 B2 R2 L2 D2 B2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `D L2 U' R2 U R2 B2 R2 L2 D2 B2 U' R2 F2 D`.
- Class 3: normal first: `U2 F2 U' R2 U`, then on inverse `(F2 L2 U' F2 U' B2 U F2 R2 B2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U2 F2 U' R2 U B2 R2 F2 U' B2 U F2 U L2 F2`.
- Class 4: linear on the inverse: `(R2 U F2 U' B2 U2 L2 D' R2 B2 D2 R2 F2 U2 R2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `R2 U2 F2 R2 D2 B2 R2 D L2 U2 B2 U F2 U' R2`.
- Class 5: linear on the inverse: `(L2 B2 U' L2 U F2 L2 D2 B2 R2 D R2 U' F2 U)`. HTR after 15 moves (7 over the shortest NISS HTR); the whole finish, as read on normal: `U' F2 U R2 D' R2 B2 D2 L2 F2 U' L2 U B2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `(R2 U F2 U)`; the reduced state is then solved by `U2 F2 U2 R2 F2 L2 D' B2 U2 F2 L2` (11 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 2 moves, `(R2 U)`; the reduced state is then solved by `U2 F2 U2 R2 F2 L2 D' B2 U2 F2 L2 U' F2` (13 moves, 2 quarter turns).

</details>

**4c3 2e, example 3.** `U' B2 U' D' R2 L2 U D R2 D2 F2 D F2 U' L2 F2 L2 U F2 U' R2 U' D'`

Read as 4a3 2e on normal, 4b3 2e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (8 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 66.2% | no / no |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 72.0% | no / yes |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 75.1% | no / yes |
| 4 | `4b3 > 4a2 > 4a1 > 0c0` | 77.9% | no / no |
| 5 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 80.1% | yes / yes |

- Class 2: inverse first: `(L2 U' B2 R2 D)`, then on normal `U2 B2 U' F2 U F2 D' F2`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U2 B2 U' F2 U F2 D' F2 D' R2 B2 U L2`.
- Class 3: normal first: `U2 B2 U' F2 U`, then on inverse `(L2 U' B2 R2 D F2 D F2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U2 B2 U' F2 U F2 D' F2 D' R2 B2 U L2`.
- Class 5: linear on the inverse: `(L2 U' B2 D F2 D F2 U' F2 U B2 U2 L2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `L2 U2 B2 U' F2 U F2 D' F2 D' B2 U L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `(L2 U' B2 D F2 D F2 U')`; the reduced state is then solved by `L2 U2 B2 U' F2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `(L2 U' B2 D F2 D)`; the reduced state is then solved by `L2 U2 B2 U' F2 U F2` (7 moves, 2 quarter turns).

</details>

**4c3 2e, example 4.** `U R2 U2 D2 R2 D2 F2 U D F2 R2 U' B2 L2 D' B2 R2 L2 F2 L2 D B2 U`

Read as 4a3 2e on normal, 4b3 2e on inverse. Shortest HTR: 8 on normal, 8 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 66.2% | yes / yes |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 72.0% | no / no |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 75.1% | no / no |
| 4 | `4b3 > 4a2 > 4a1 > 0c0` | 77.9% | no / yes |
| 5 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 80.1% | no / no |

- Class 1: normal first: `U`, then on inverse `(U2 R2 U R2 D R2 F2 D2 L2 R2 F2)`. HTR after 6 moves (within the budget); the whole finish, as read on normal: `U F2 R2 L2 D2 F2 R2 D' R2 U' R2 U2`.
- Class 4: linear on the inverse: `(U2 R2 U R2 D R2 F2 D2 L2 R2 F2 U')`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `U F2 R2 L2 D2 F2 R2 D' R2 U' R2 U2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `U (U2 R2 U)`; the reduced state is then solved by `F2 R2 L2 D2 F2 R2 D' R2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 1 move, `U`; the reduced state is then solved by `F2 R2 L2 D2 F2 R2 D' R2 U' R2 U2` (11 moves, 2 quarter turns).

</details>

**4c3 2e, example 5.** `U2 L2 D R2 U' B2 R2 D2 F2 D' F2 R2 U2 L2 D' B2 U' L2 U R2 U2 F2 U'`

Read as 4b3 2e on normal, 4a3 2e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 66.2% | yes / yes |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 72.0% | no / no |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 75.1% | no / no |
| 4 | `4b3 > 4a2 > 4a1 > 0c0` | 77.9% | no / yes |
| 5 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 80.1% | no / no |

- Class 1: inverse first: `(U2 F2 D')`, then on normal `D' F2 U2 F2 L2 B2 U' B2 R2 D2 R2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `D' F2 U2 F2 L2 B2 U' B2 R2 D2 R2 D F2 U2`.
- Class 4: linear on normal: `U' R2 U2 R2 F2 L2 U F2 U2 L2 U' B2 D2 B2`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' R2 U2 R2 F2 L2 U F2 U2 L2 U' B2 D2 B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `D' (U2 F2 D')`; the reduced state is then solved by `F2 U2 F2 L2 B2 U' B2 R2 D2 R2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 1 move, `U'`; the reduced state is then solved by `R2 U2 R2 F2 L2 U F2 U2 L2 U' B2 D2 B2` (13 moves, 2 quarter turns).

</details>

**4c3 2e, example 6.** `D L2 U2 D2 R2 L2 U D2 F2 U R2 U' L2 B2 U2 B2 D' B2 D B2 U' F2`

Read as 4a3 2e on normal, 4b3 2e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (87 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 66.2% | yes / yes |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 72.0% | yes / yes |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 75.1% | yes / yes |
| 4 | `4b3 > 4a2 > 4a1 > 0c0` | 77.9% | yes / yes |
| 5 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 80.1% | yes / yes |

- Class 1: normal first: `D'`, then on inverse `(B2 R2 U L2 D2 L2 U2 F2 U' B2 R2 U2 F2 L2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `D' L2 F2 U2 R2 B2 U F2 U2 L2 D2 L2 U' R2 B2`.
- Class 2: inverse first: `(B2 U B2 D')`, then on normal `U' F2 D F2 D' F2 R2 U2 B2 L2 F2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U' F2 D F2 D' F2 R2 U2 B2 L2 F2 D B2 U' B2`.
- Class 3: normal first: `U B2 U`, then on inverse `(B2 D F2 U B2 U' L2 U2 L2 R2 B2 R2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U B2 U R2 B2 R2 L2 U2 L2 U B2 U' F2 D' B2`.
- Class 4: linear on the inverse: `(R2 U R2 U R2 F2 U2 L2 B2 D' B2 F2 L2 B2 L2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `L2 B2 L2 F2 B2 D B2 L2 U2 F2 R2 U' R2 U' R2`.
- Class 5: linear on the inverse: `(D' L2 B2 D' L2 U' F2 D B2 R2 D' F2 D2 B2 F2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `F2 B2 D2 F2 D R2 B2 D' F2 U L2 D B2 L2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `D' (B2 R2 U)`; the reduced state is then solved by `L2 F2 U2 R2 B2 U F2 U2 L2 D2 L2` (11 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 1 move, `D'`; the reduced state is then solved by `L2 F2 U2 R2 B2 U F2 U2 L2 D2 L2 U' R2 B2` (14 moves, 2 quarter turns).

</details>

**4c3 2e, example 7.** `F2 B2 U L2 F2 L2 D2 R2 D R2 L2 B2 L2 D2 F2 D' L2 U L2 D' R2 U B2 R2 U`

Read as 4b3 2e on normal, 4a3 2e on inverse. Shortest HTR: 10 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (11 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 66.2% | no / no |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 72.0% | no / yes |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 75.1% | no / yes |
| 4 | `4b3 > 4a2 > 4a1 > 0c0` | 77.9% | no / no |
| 5 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 80.1% | no / yes |

- Class 2: normal first: `R2 U R2 U`, then on inverse `(B2 D F2 U' B2 L2 D' B2 L2 D2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U R2 U D2 L2 B2 D L2 B2 U F2 D' B2`.
- Class 3: inverse first: `(B2 D F2 U')`, then on normal `R2 U R2 U D2 L2 B2 D L2 B2`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U R2 U D2 L2 B2 D L2 B2 U F2 D' B2`.
- Class 5: linear on normal: `U2 L2 F2 D F2 U' B2 U' F2 D R2 U' B2 R2`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U2 L2 F2 D F2 U' B2 U' F2 D R2 U' B2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `R2 U R2 U (B2 D F2 U')`; the reduced state is then solved by `D2 L2 B2 D L2 B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 6 moves, `R2 U (B2 D F2 U')`; the reduced state is then solved by `R2 U D2 L2 B2 D L2 B2` (8 moves, 2 quarter turns).

</details>

**4c3 2e, example 8.** `D2 B2 U' R2 U' D' R2 U' F2 R2 U' R2 U' D2 B2 U' B2 R2 U' F2 D B2`

Read as 4a3 2e on normal, 4b3 2e on inverse. Shortest HTR: 8 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 66.2% | no / no |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 72.0% | yes / yes |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 75.1% | no / yes |
| 4 | `4b3 > 4a2 > 4a1 > 0c0` | 77.9% | no / no |
| 5 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 80.1% | no / yes |

- Class 2: inverse first: `(L2 U' B2 D')`, then on normal `L2 U' B2 D R2 D' R2 F2 R2 F2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `L2 U' B2 D R2 D' R2 F2 R2 F2 D B2 U L2`.
- Class 3: normal first: `L2 U' B2 D`, then on inverse `(L2 U' B2 D' F2 R2 F2 R2 D R2)`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U' B2 D R2 D' R2 F2 R2 F2 D B2 U L2`.
- Class 5: linear on the inverse: `(L2 U' B2 D' F2 R2 F2 R2 D R2 D' B2 U L2)`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U' B2 D R2 D' R2 F2 R2 F2 D B2 U L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `L2 U' B2 D (L2 U' B2 D')`; the reduced state is then solved by `R2 D' R2 F2 R2 F2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `L2 U' (L2 U' B2 D')`; the reduced state is then solved by `B2 D R2 D' R2 F2 R2 F2` (8 moves, 2 quarter turns).

</details>

**4c3 2e, example 9.** `U' F2 L2 U2 D2 R2 D2 R2 L2 D2 F2 L2 D R2 U2 B2 R2 B2 L2 U L2 U' D' R2`

Read as 4a3 2e on normal, 4b3 2e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 66.2% | yes / yes |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 72.0% | no / no |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 75.1% | no / no |
| 4 | `4b3 > 4a2 > 4a1 > 0c0` | 77.9% | no / yes |
| 5 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 80.1% | no / no |

- Class 1: normal first: `R2 U2 B2 U'`, then on inverse `(D' B2 U B2 U2 R2 F2 L2 B2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `R2 U2 B2 U' B2 L2 F2 R2 U2 B2 U' B2 D`.
- Class 4: linear on the inverse: `(D' B2 U B2 U2 R2 F2 L2 B2 U B2 U2 R2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U2 B2 U' B2 L2 F2 R2 U2 B2 U' B2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 3 moves, `(D' B2 U)`; the reduced state is then solved by `R2 U2 B2 U' B2 L2 F2 R2 U2 B2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 2e here) on an optimal path: 1 move, `(D')`; the reduced state is then solved by `R2 U2 B2 U' B2 L2 F2 R2 U2 B2 U' B2` (12 moves, 2 quarter turns).

</details>

**4c3 2e, example 10.** `U L2 U F2 L2 U D' R2 L2 U' R2 D' L2 D' F2 B2 U' B2 R2 U' R2 U2`

Read as 4a3 2e on normal, 4b3 2e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 66.2% | no / no |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 72.0% | no / no |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 75.1% | no / yes |
| 4 | `4b3 > 4a2 > 4a1 > 0c0` | 77.9% | no / no |
| 5 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 80.1% | no / no |

- Class 3: normal first: `U2 F2 L2 U' F2 D`, then on inverse `(F2 U' B2 U' R2 U' B2 F2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U2 F2 L2 U' F2 D F2 B2 U R2 U B2 U F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `(F2 U' B2 U' R2 U' B2 F2 D')`; the reduced state is then solved by `U2 F2 L2 U' F2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `(F2 U' B2 U' R2 U')`; the reduced state is then solved by `U2 F2 L2 U' F2 D F2 B2` (8 moves, 2 quarter turns).

</details>

### 4c3 4e

5.88% of all DR states.

**4c3 4e, example 1.** `D' L2 D2 R2 L2 F2 B2 U' D B2 D' L2 D B2 U2 L2 U F2 R2 U L2 U2`

Read as 4b3 4e on normal, 4a3 4e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 62.3% | no / no |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 70.2% | no / yes |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.4% | yes / yes |
| 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% | no / yes |
| 5 | `4a3 > 4b2 > 4a1 > 0c0` | 79.6% | no / no |

- Class 2: normal first: `L2 B2 U' B2 U`, then on inverse `(R2 U' R2 U' R2 F2 D' F2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 U' B2 U F2 D F2 R2 U R2 U R2`.
- Class 3: inverse first: `(R2 F2 D L2 U')`, then on normal `L2 U F2 U' R2 U R2 L2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `L2 U F2 U' R2 U R2 L2 U L2 D' F2 R2`.
- Class 4: linear on normal: `L2 B2 U' B2 U F2 D F2 R2 U R2 U R2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 U' B2 U F2 D F2 R2 U R2 U R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `L2 U F2 U' (R2 F2 D L2 U')`; the reduced state is then solved by `R2 U R2 L2` (4 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `L2 U F2 U' R2 U`; the reduced state is then solved by `R2 L2 U L2 D' F2 R2` (7 moves, 2 quarter turns).

</details>

**4c3 4e, example 2.** `U' D B2 U F2 R2 D2 L2 U' R2 F2 U B2 D2 F2 L2 D R2 F2 U' F2 D2`

Read as 4b3 4e on normal, 4a3 4e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (4 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 62.3% | no / yes |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 70.2% | no / no |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.4% | no / no |
| 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% | no / no |
| 5 | `4a3 > 4b2 > 4a1 > 0c0` | 79.6% | no / yes |

- Class 1: inverse first: `(D2 L2 B2 D)`, then on normal `F2 L2 D' F2 R2 U' B2 U2 R2`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 D' F2 R2 U' B2 U2 R2 D' B2 L2 D2`.
- Class 5: linear on the inverse: `(D2 L2 B2 D R2 U2 B2 U R2 F2 D L2 F2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 D' F2 R2 U' B2 U2 R2 D' B2 L2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `F2 L2 D' F2 R2 U'`; the reduced state is then solved by `B2 U2 R2 D' B2 L2 D2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 3 moves, `F2 L2 D'`; the reduced state is then solved by `F2 R2 U' B2 U2 R2 D' B2 L2 D2` (10 moves, 2 quarter turns).

</details>

**4c3 4e, example 3.** `F2 U D' L2 U2 R2 B2 U2 D2 L2 D' B2 R2 D L2 U2 R2 B2 R2 F2 R2 U'`

Read as 4a3 4e on normal, 4b3 4e on inverse. Shortest HTR: 9 on normal, 8 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 11 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 62.3% | yes / yes |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 70.2% | no / no |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.4% | no / no |
| 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% | no / no |
| 5 | `4a3 > 4b2 > 4a1 > 0c0` | 79.6% | no / yes |

- Class 1: normal first: `R2 L2 U`, then on inverse `(U' L2 F2 U' F2 L2 D2 L2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `R2 L2 U L2 D2 L2 F2 U F2 L2 U`.
- Class 5: linear on normal: `R2 L2 U L2 D2 L2 F2 U F2 L2 U`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 L2 U L2 D2 L2 F2 U F2 L2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `(U' L2 F2 U')`; the reduced state is then solved by `R2 L2 U L2 D2 L2 F2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 1 move, `(U')`; the reduced state is then solved by `R2 L2 U L2 D2 L2 F2 U F2 L2` (10 moves, 2 quarter turns).

</details>

**4c3 4e, example 4.** `U' F2 U L2 D2 B2 U2 F2 B2 U' F2 L2 F2 R2 D' B2 D' R2 F2 U2 L2`

Read as 4a3 4e on normal, 4b3 4e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (27 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 62.3% | yes / yes |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 70.2% | no / yes |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.4% | no / yes |
| 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% | yes / yes |
| 5 | `4a3 > 4b2 > 4a1 > 0c0` | 79.6% | yes / yes |

- Class 1: normal first: `B2 L2 U`, then on inverse `(D2 B2 L2 U L2 D R2 F2 U2 L2 B2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `B2 L2 U B2 L2 U2 F2 R2 D' L2 U' L2 B2 D2`.
- Class 2: inverse first: `(D' B2 R2 U')`, then on normal `L2 D' L2 U R2 F2 U B2 R2 L2`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 D' L2 U R2 F2 U B2 R2 L2 U R2 B2 D`.
- Class 3: normal first: `L2 D' L2 U`, then on inverse `(D' B2 R2 U' L2 R2 B2 U' F2 R2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 D' L2 U R2 F2 U B2 R2 L2 U R2 B2 D`.
- Class 4: linear on the inverse: `(U' R2 D' L2 D' F2 D F2 D' U2 L2 D2 R2 F2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `F2 R2 D2 L2 U2 D F2 D' F2 D L2 D R2 U`.
- Class 5: linear on normal: `R2 D B2 U2 B2 L2 D R2 F2 D L2 F2 U2 L2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `R2 D B2 U2 B2 L2 D R2 F2 D L2 F2 U2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `(D2 B2 L2 U L2 D)`; the reduced state is then solved by `B2 L2 U B2 L2 U2 F2 R2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 2 moves, `R2 D`; the reduced state is then solved by `B2 U2 B2 L2 D R2 F2 D L2 F2 U2 L2` (12 moves, 2 quarter turns).

</details>

**4c3 4e, example 5.** `U D2 L2 D L2 U2 D R2 L2 U2 B2 U' R2 U2 L2 D' R2 D' B2 D2 F2 R2 U'`

Read as 4a3 4e on normal, 4b3 4e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (8 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 62.3% | no / no |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 70.2% | yes / yes |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.4% | no / yes |
| 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% | no / yes |
| 5 | `4a3 > 4b2 > 4a1 > 0c0` | 79.6% | no / no |

- Class 2: inverse first: `(L2 D B2 L2 U')`, then on normal `U B2 U' L2 D F2 L2 D2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U B2 U' L2 D F2 L2 D2 U L2 B2 D' L2`.
- Class 3: normal first: `U B2 U`, then on inverse `(L2 U R2 B2 U F2 R2 U' R2 D2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 U D2 R2 U R2 F2 U' B2 R2 U' L2`.
- Class 4: linear on the inverse: `(L2 U R2 B2 U F2 R2 U' R2 D2 U' B2 U')`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 U D2 R2 U R2 F2 U' B2 R2 U' L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U B2 U' L2 D (L2 D)`; the reduced state is then solved by `F2 L2 U D2 L2 B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 5 moves, `U B2 U (L2 U)`; the reduced state is then solved by `D2 R2 U R2 F2 U' B2 R2` (8 moves, 2 quarter turns).

</details>

**4c3 4e, example 6.** `U2 D' L2 U' F2 D' F2 U2 D' R2 B2 U F2 D R2 D' F2 D F2 R2 U' F2 L2 D2 L2`

Read as 4b3 4e on normal, 4a3 4e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (5 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 62.3% | yes / yes |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 70.2% | no / no |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.4% | no / no |
| 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% | no / no |
| 5 | `4a3 > 4b2 > 4a1 > 0c0` | 79.6% | no / yes |

- Class 1: inverse first: `(F2 U')`, then on normal `L2 F2 U' L2 F2 U L2 D2 F2 R2 L2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `L2 F2 U' L2 F2 U L2 D2 F2 R2 L2 U F2`.
- Class 5: linear on the inverse: `(B2 U F2 D2 R2 D R2 B2 L2 B2 D B2 R2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 D' B2 L2 B2 R2 D' R2 D2 F2 U' B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `R2 B2 D' (B2 U)`; the reduced state is then solved by `B2 L2 B2 R2 D' R2 D2 F2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 2 moves, `(B2 U)`; the reduced state is then solved by `R2 B2 D' B2 L2 B2 R2 D' R2 D2 F2` (11 moves, 2 quarter turns).

</details>

**4c3 4e, example 7.** `L2 U' D2 R2 U2 D L2 D' L2 U2 B2 D' F2 R2 U' R2 F2 D' B2 L2 U' L2`

Read as 4a3 4e on normal, 4b3 4e on inverse. Shortest HTR: 9 on normal, 8 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 62.3% | no / no |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 70.2% | no / no |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.4% | no / yes |
| 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% | no / no |
| 5 | `4a3 > 4b2 > 4a1 > 0c0` | 79.6% | no / no |

- Class 3: normal first: `B2 D' F2 D'`, then on inverse `(F2 U' R2 D' L2 B2 U B2 F2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 D' F2 D' F2 B2 U' B2 L2 D R2 U F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `B2 D' F2 D' (F2 U' R2 D')`; the reduced state is then solved by `F2 B2 U' B2 L2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (0c0 4e here) on an optimal path: 6 moves, `B2 D' (F2 U' R2 D')`; the reduced state is then solved by `F2 D' F2 B2 U' B2 L2` (7 moves, 2 quarter turns).

</details>

**4c3 4e, example 8.** `U2 F2 U F2 B2 D F2 U' D L2 D2 B2 U B2 U2 B2 U' L2 D F2 B2 D L2 U`

Read as 4a3 4e on normal, 4b3 4e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 62.3% | no / no |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 70.2% | no / yes |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.4% | no / yes |
| 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% | no / yes |
| 5 | `4a3 > 4b2 > 4a1 > 0c0` | 79.6% | no / no |

- Class 2: inverse first: `(U B2 U')`, then on normal `D' L2 D2 F2 L2 U B2 U F2`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D' L2 D2 F2 L2 U B2 U F2 U B2 U'`.
- Class 3: normal first: `D' L2 D2 F2 L2 U`, then on inverse `(U B2 U' F2 U' B2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D' L2 D2 F2 L2 U B2 U F2 U B2 U'`.
- Class 4: linear on the inverse: `(U B2 U' F2 U' B2 U' L2 F2 D2 L2 D)`. HTR after 12 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `D' L2 D2 F2 L2 U B2 U F2 U B2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `D' (U B2 U' F2 U')`; the reduced state is then solved by `L2 D2 F2 L2 U B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `D' (U B2 U')`; the reduced state is then solved by `L2 D2 F2 L2 U B2 U F2` (8 moves, 2 quarter turns).

</details>

**4c3 4e, example 9.** `U' D' R2 U D F2 U2 D L2 D2 F2 D2 L2 B2 D' L2 U' F2 D' F2 U' R2`

Read as 4b3 4e on normal, 4a3 4e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (12 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 62.3% | no / no |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 70.2% | yes / yes |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.4% | no / yes |
| 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% | yes / yes |
| 5 | `4a3 > 4b2 > 4a1 > 0c0` | 79.6% | no / no |

- Class 2: normal first: `L2 U R2 F2 U`, then on inverse `(U R2 U B2 R2 U' F2 D2 R2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `L2 U R2 F2 U R2 D2 F2 U R2 B2 U' R2 U'`.
- Class 3: inverse first: `(L2 F2 D F2 U2 F2 U')`, then on normal `D' R2 U F2 U' F2 B2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D' R2 U F2 U' F2 B2 U F2 U2 F2 D' F2 L2`.
- Class 4: linear on normal: `R2 D R2 U F2 D F2 U' B2 D F2 B2 D2 B2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `R2 D R2 U F2 D F2 U' B2 D F2 B2 D2 B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `L2 D R2 U' (U R2 D)`; the reduced state is then solved by `L2 D2 F2 U' B2 R2 L2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `D' R2 U F2 U'`; the reduced state is then solved by `F2 B2 U F2 U2 F2 D' F2 L2` (9 moves, 2 quarter turns).

</details>

**4c3 4e, example 10.** `U2 L2 U2 D' R2 U2 F2 B2 U' R2 D B2 U2 F2 D L2 F2 B2 U' L2 F2 R2 U2`

Read as 4b3 4e on normal, 4a3 4e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4a3 > 4b2 > (4a1 > 0c0)` | 62.3% | yes / yes |
| 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 70.2% | no / no |
| 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 74.4% | no / no |
| 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% | no / no |
| 5 | `4a3 > 4b2 > 4a1 > 0c0` | 79.6% | no / yes |

- Class 1: inverse first: `(L2 R2 D')`, then on normal `L2 B2 D L2 B2 D F2 L2 U2 R2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `L2 B2 D L2 B2 D F2 L2 U2 R2 D R2 L2`.
- Class 5: linear on the inverse: `(L2 R2 D' R2 U2 L2 F2 D' B2 L2 D' B2 L2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 D L2 B2 D F2 L2 U2 R2 D R2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `L2 B2 D (L2 R2 D')`; the reduced state is then solved by `L2 B2 D F2 L2 U2 R2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 3 moves, `(L2 R2 D')`; the reduced state is then solved by `L2 B2 D L2 B2 D F2 L2 U2 R2` (10 moves, 2 quarter turns).

</details>

## 4c4

### 4c4 2e

5.22% of all DR states.

**4c4 2e, example 1.** `U F2 U2 R2 L2 U R2 D F2 B2 R2 U' F2 D' B2 U2 L2 B2 U2 F2 U'`

Read as 4b4 2e on normal, 4a4 2e on inverse. Shortest HTR: 10 on normal, 11 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (12 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 67.9% | no / no |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 75.4% | no / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.7% | no / yes |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.8% | no / yes |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 82.1% | no / yes |

- Class 2: inverse first: `(D L2 D')`, then on normal `D2 F2 R2 U' F2 U' B2 U L2 D' L2 F2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D2 F2 R2 U' F2 U' B2 U L2 D' L2 F2 D L2 D'`.
- Class 3: inverse first: `(F2 U B2 U' L2 U)`, then on normal `U F2 U' L2 B2 U2 R2 U' R2`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U F2 U' L2 B2 U2 R2 U' R2 U' L2 U B2 U' F2`.
- Class 4: normal first: `D'`, then on inverse `(F2 U R2 F2 D B2 U' B2 U B2 U R2 U2 L2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D' L2 U2 R2 U' B2 U' B2 U B2 D' F2 R2 U' F2`.
- Class 5: normal first: `D2 F2 R2 U'`, then on inverse `(D L2 D' F2 L2 D L2 U' B2 U F2)`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `D2 F2 R2 U' F2 U' B2 U L2 D' L2 F2 D L2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `U (F2 U B2 U' L2 U R2 U)`; the reduced state is then solved by `F2 U' L2 B2 U2 R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 7 moves, `U (F2 U B2 U' L2 U)`; the reduced state is then solved by `F2 U' L2 B2 U2 R2 U' R2` (8 moves, 2 quarter turns).

</details>

**4c4 2e, example 2.** `D L2 U2 D2 F2 D F2 U2 R2 U L2 B2 L2 B2 D F2 U2 L2 D' R2 D`

Read as 4b4 2e on normal, 4a4 2e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (58 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 67.9% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 75.4% | no / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.7% | no / yes |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.8% | no / yes |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 82.1% | no / no |

- Class 1: normal first: `U B2 U`, then on inverse `(U' L2 F2 D2 R2 U L2 R2 F2 R2 U2 R2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U B2 U R2 U2 R2 F2 R2 L2 U' R2 D2 F2 L2 U`.
- Class 2: inverse first: `(R2 D' B2 U')`, then on normal `R2 D' B2 U' R2 B2 U' L2 U B2 L2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 D' B2 U' R2 B2 U' L2 U B2 L2 U B2 D R2`.
- Class 3: inverse first: `(R2 D' B2 U' L2 B2 U')`, then on normal `R2 D' B2 U' R2 B2 U' L2`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 D' B2 U' R2 B2 U' L2 U B2 L2 U B2 D R2`.
- Class 4: normal first: `R2 D'`, then on inverse `(R2 D' B2 U' L2 B2 U' L2 U B2 R2 U B2)`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 D' B2 U' R2 B2 U' L2 U B2 L2 U B2 D R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `U B2 U (U')`; the reduced state is then solved by `R2 U2 R2 F2 R2 L2 U' R2 D2 F2 L2` (11 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 2 moves, `U (U')`; the reduced state is then solved by `R2 L2 F2 U' L2 U2 R2 F2 D L2 U2 F2 L2` (13 moves, 2 quarter turns).

</details>

**4c4 2e, example 3.** `L2 U' D2 R2 B2 D' F2 B2 D' R2 D L2 U' R2 B2 U2 R2 D' R2 F2 U B2 U`

Read as 4a4 2e on normal, 4b4 2e on inverse. Shortest HTR: 11 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (22 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 67.9% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 75.4% | no / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.7% | no / yes |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.8% | no / no |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 82.1% | no / yes |

- Class 1: inverse first: `(D' L2 D2 F2 U)`, then on normal `B2 U' L2 B2 D B2 L2 U2 F2 L2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `B2 U' L2 B2 D B2 L2 U2 F2 L2 U' F2 D2 L2 D`.
- Class 2: normal first: `F2 B2 D F2 D'`, then on inverse `(D F2 D B2 D' L2 F2 U' R2 F2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 D F2 D' F2 R2 U F2 L2 D B2 D' F2 D'`.
- Class 3: normal first: `F2 B2 D F2 D' F2 R2 U`, then on inverse `(D F2 D B2 D' L2 F2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 D F2 D' F2 R2 U F2 L2 D B2 D' F2 D'`.
- Class 5: inverse first: `(D)`, then on normal `F2 B2 D F2 D' F2 R2 U F2 L2 D B2 D' F2`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 D F2 D' F2 R2 U F2 L2 D B2 D' F2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `B2 U' R2 F2 U' (D)`; the reduced state is then solved by `L2 U2 L2 F2 U' R2 U2 L2 F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `(U L2 D')`; the reduced state is then solved by `R2 F2 L2 D2 F2 U' B2 U B2 D2 B2 R2` (12 moves, 2 quarter turns).

</details>

**4c4 2e, example 4.** `R2 U D' B2 U2 R2 U2 B2 L2 U' R2 L2 U2 B2 D' B2 U2 R2 U L2 U'`

Read as 4a4 2e on normal, 4b4 2e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (20 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 67.9% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 75.4% | no / no |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.7% | no / no |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.8% | no / yes |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 82.1% | no / no |

- Class 1: inverse first: `(D2 F2 R2 U L2 D)`, then on normal `U' F2 L2 U B2 L2 U2 B2 L2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U' F2 L2 U B2 L2 U2 B2 L2 D' L2 U' R2 F2 D2`.
- Class 4: inverse first: `(D')`, then on normal `U L2 U L2 U' L2 B2 D' F2 R2 D B2 R2 L2`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U L2 U L2 U' L2 B2 D' F2 R2 D B2 R2 L2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `D' (L2 F2 U' R2 U')`; the reduced state is then solved by `L2 F2 D2 L2 D' R2 F2 U2 B2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 3 moves, `U' R2 U'`; the reduced state is then solved by `B2 D2 F2 L2 D' L2 F2 U R2 F2 D2 R2` (12 moves, 2 quarter turns).

</details>

**4c4 2e, example 5.** `U R2 U B2 U D R2 D2 R2 F2 R2 U' F2 B2 R2 U F2 U D2 R2 D R2`

Read as 4b4 2e on normal, 4a4 2e on inverse. Shortest HTR: 11 on normal, 11 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 67.9% | no / no |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 75.4% | no / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.7% | no / yes |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.8% | no / no |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 82.1% | no / yes |

- Class 2: inverse first: `(U' B2 F2 L2 D)`, then on normal `D R2 U F2 U' R2 U B2 R2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D R2 U F2 U' R2 U B2 R2 D' L2 F2 B2 U`.
- Class 3: inverse first: `(U' B2 F2 L2 D R2 B2 U')`, then on normal `D R2 U F2 U' R2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D R2 U F2 U' R2 U B2 R2 D' L2 F2 B2 U`.
- Class 5: normal first: `D`, then on inverse `(U' B2 F2 L2 D R2 B2 U' R2 U F2 U' R2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D R2 U F2 U' R2 U B2 R2 D' L2 F2 B2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `D R2 U F2 U' R2 U (U')`; the reduced state is then solved by `B2 R2 D' L2 F2 B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 6 moves, `D R2 U F2 U' (U')`; the reduced state is then solved by `R2 U B2 R2 D' L2 F2 B2` (8 moves, 2 quarter turns).

</details>

**4c4 2e, example 6.** `R2 L2 U2 B2 D' F2 D F2 R2 L2 U' R2 U' F2 R2 D2 F2 L2 D' B2 R2 D'`

Read as 4a4 2e on normal, 4b4 2e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 67.9% | no / no |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 75.4% | no / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.7% | no / yes |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.8% | no / yes |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 82.1% | no / no |

- Class 2: normal first: `U F2 U`, then on inverse `(U L2 B2 U L2 D' F2 U L2 R2 F2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U F2 U F2 R2 L2 U' F2 D L2 U' B2 L2 U'`.
- Class 3: normal first: `U F2 U F2 R2 L2 U'`, then on inverse `(U L2 B2 U L2 D' F2)`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U F2 U F2 R2 L2 U' F2 D L2 U' B2 L2 U'`.
- Class 4: inverse first: `(U)`, then on normal `U F2 U F2 R2 L2 U' F2 D L2 U' B2 L2`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U F2 U F2 R2 L2 U' F2 D L2 U' B2 L2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `U (U L2 B2 U L2 D' F2 U)`; the reduced state is then solved by `F2 U F2 R2 L2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 7 moves, `U (U L2 B2 U L2 D')`; the reduced state is then solved by `F2 U F2 R2 L2 U' F2` (7 moves, 2 quarter turns).

</details>

**4c4 2e, example 7.** `D R2 L2 B2 D F2 U2 D2 F2 R2 L2 U R2 F2 D B2 U2 B2 R2 U R2 U'`

Read as 4a4 2e on normal, 4b4 2e on inverse. Shortest HTR: 11 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 67.9% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 75.4% | no / no |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.7% | no / no |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.8% | no / no |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 82.1% | no / no |

- Class 1: inverse first: `(U F2 D)`, then on normal `F2 U2 L2 U' R2 U' L2 F2 U2 F2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `F2 U2 L2 U' R2 U' L2 F2 U2 F2 D' F2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `F2 U2 L2 U' (U F2 D)`; the reduced state is then solved by `R2 U' L2 F2 U2 F2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `(U F2 D)`; the reduced state is then solved by `F2 U2 L2 U' R2 U' L2 F2 U2 F2` (10 moves, 2 quarter turns).

</details>

**4c4 2e, example 8.** `U B2 U2 D2 F2 D F2 U2 L2 B2 U R2 D' F2 D' L2 F2 U' F2 U B2 U L2`

Read as 4b4 2e on normal, 4a4 2e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (42 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 67.9% | no / no |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 75.4% | no / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.7% | no / yes |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.8% | yes / yes |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 82.1% | no / yes |

- Class 2: inverse first: `(D F2 D)`, then on normal `F2 U2 F2 U' B2 U L2 D' R2 D F2 L2`. HTR after 13 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U2 F2 U' B2 U L2 D' R2 D F2 L2 D' F2 D'`.
- Class 3: inverse first: `(D F2 D L2 F2 D')`, then on normal `F2 U2 F2 U' B2 U L2 D' R2`. HTR after 14 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U2 F2 U' B2 U L2 D' R2 D F2 L2 D' F2 D'`.
- Class 4: normal first: `U'`, then on inverse `(F2 U' L2 D L2 B2 U L2 D' B2 D' R2 F2 D2)`. HTR after 12 moves (within the budget); the whole finish, as read on normal: `U' D2 F2 R2 D B2 D L2 U' B2 L2 D' L2 U F2`.
- Class 5: normal first: `F2 U2 F2 U'`, then on inverse `(D F2 D L2 F2 D' R2 D L2 U' B2)`. HTR after 14 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U2 F2 U' B2 U L2 D' R2 D F2 L2 D' F2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 10 moves, `U L2 U (B2 U B2 U' F2 R2 D')`; the reduced state is then solved by `L2 F2 U D2 F2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 7 moves, `U L2 U (B2 U B2 U')`; the reduced state is then solved by `L2 F2 U D2 F2 D R2 F2` (8 moves, 2 quarter turns).

</details>

**4c4 2e, example 9.** `R2 F2 U' D2 L2 U' D2 B2 R2 B2 R2 B2 U' B2 U F2 R2 D2 L2 D R2 U'`

Read as 4a4 2e on normal, 4b4 2e on inverse. Shortest HTR: 10 on normal, 11 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 16 moves (222 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 67.9% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 75.4% | yes / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.7% | yes / yes |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.8% | yes / yes |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 82.1% | yes / yes |

- Class 1: inverse first: `(B2 R2 U' B2 D')`, then on normal `L2 U' R2 F2 U R2 U2 F2 R2 F2 L2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `L2 U' R2 F2 U R2 U2 F2 R2 F2 L2 D B2 U R2 B2`.
- Class 2: normal first: `U R2 U`, then on inverse `(B2 D' F2 D' R2 B2 U' B2 U' R2 U2 L2 F2)`. HTR after 12 moves (within the budget); the whole finish, as read on normal: `U R2 U F2 L2 U2 R2 U B2 U B2 R2 D F2 D B2`.
- Class 3: normal first: `U R2 D F2 U'`, then on inverse `(D' B2 D' R2 F2 U' F2 R2 D2 F2 L2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U R2 D F2 U' L2 F2 D2 R2 F2 U F2 R2 D B2 D`.
- Class 4: inverse first: `(B2 D)`, then on normal `U' R2 D F2 U' L2 D R2 U L2 U2 R2 L2 F2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U' R2 D F2 U' L2 D R2 U L2 U2 R2 L2 F2 D' B2`.
- Class 5: inverse first: `(R2 D')`, then on normal `U L2 U' F2 D' R2 B2 U' F2 D' F2 D2 B2 L2`. HTR after 12 moves (within the budget); the whole finish, as read on normal: `U L2 U' F2 D' R2 B2 U' F2 D' F2 D2 B2 L2 D R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `R2 U' B2 R2 U' (R2 D)`; the reduced state is then solved by `L2 U2 L2 F2 U' L2 B2 L2 F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `R2 U' L2 U'`; the reduced state is then solved by `R2 U2 B2 D F2 U F2 D2 R2 B2 D2 F2` (12 moves, 2 quarter turns).

</details>

**4c4 2e, example 10.** `L2 U2 F2 B2 D2 L2 U D L2 F2 D' B2 D' F2 D2 R2 U B2 U2 F2 R2 U' F2`

Read as 4b4 2e on normal, 4a4 2e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 67.9% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 75.4% | no / no |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.7% | no / no |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.8% | no / no |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 82.1% | no / no |

- Class 1: normal first: `L2 F2 U B2 D`, then on inverse `(B2 D' F2 R2 U' B2 U2 B2 L2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `L2 F2 U B2 D L2 B2 U2 B2 U R2 F2 D B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `L2 F2 U B2 D (B2 D')`; the reduced state is then solved by `L2 B2 U2 B2 U R2 F2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `(B2 D' F2 R2 U')`; the reduced state is then solved by `L2 F2 U B2 D L2 B2 U2 B2` (9 moves, 2 quarter turns).

</details>

### 4c4 4e

5.88% of all DR states.

**4c4 4e, example 1.** `R2 U' D2 F2 U R2 U' D' L2 U' F2 L2 U F2 L2 F2 U' F2 D B2 U2 L2 D2`

Read as 4b4 4e on normal, 4a4 4e on inverse. Shortest HTR: 9 on normal, 11 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (14 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 68.4% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 74.8% | no / no |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.2% | no / no |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 81.5% | no / no |

- Class 1: normal first: `U L2 U`, then on inverse `(F2 L2 R2 D2 B2 U' L2 D B2 U2 L2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U L2 U L2 U2 B2 D' L2 U B2 D2 R2 L2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `U (F2 L2 U L2 U')`; the reduced state is then solved by `L2 U2 R2 B2 U R2 U2 B2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `U L2 U`; the reduced state is then solved by `L2 U2 B2 D' L2 U B2 D2 R2 L2 F2` (11 moves, 2 quarter turns).

</details>

**4c4 4e, example 2.** `U D L2 B2 U D' R2 F2 R2 D B2 D2 B2 L2 U' L2 D2 R2 B2 D' F2 U' L2`

Read as 4a4 4e on normal, 4b4 4e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (10 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 68.4% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 74.8% | no / no |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.2% | no / no |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 81.5% | no / no |

- Class 1: inverse first: `(B2 D' B2 U)`, then on normal `R2 F2 U2 R2 U F2 D' R2 F2 U2 F2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `R2 F2 U2 R2 U F2 D' R2 F2 U2 F2 U' B2 D B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `(B2 D' B2 U F2 U2 F2 R2 D)`; the reduced state is then solved by `R2 F2 U2 R2 U F2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `(B2 D' B2 U)`; the reduced state is then solved by `R2 F2 U2 R2 U F2 D' R2 F2 U2 F2` (11 moves, 2 quarter turns).

</details>

**4c4 4e, example 3.** `U D2 F2 B2 L2 U D F2 D F2 B2 L2 D' R2 U B2 D' R2 U F2`

Read as 4a4 4e on normal, 4b4 4e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (4 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 68.4% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 74.8% | no / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.2% | no / no |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | yes / yes |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 81.5% | no / no |

- Class 1: inverse first: `(L2 D' L2 B2 D')`, then on normal `R2 B2 D' F2 D B2 D2 F2 L2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `R2 B2 D' F2 D B2 D2 F2 L2 D B2 L2 D L2`.
- Class 2: normal first: `U' B2 U`, then on inverse `(D L2 U2 B2 U L2 U B2 R2 U B2)`. HTR after 13 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' B2 U B2 U' R2 B2 U' L2 U' B2 U2 L2 D'`.
- Class 4: inverse first: `(D)`, then on normal `U' B2 U B2 U' R2 B2 U' L2 U' B2 U2 L2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U' B2 U B2 U' R2 B2 U' L2 U' B2 U2 L2 D'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `R2 B2 D' F2 D (L2 D')`; the reduced state is then solved by `B2 D2 F2 L2 D B2 L2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `(L2 D' L2 B2 D')`; the reduced state is then solved by `R2 B2 D' F2 D B2 D2 F2 L2` (9 moves, 2 quarter turns).

</details>

**4c4 4e, example 4.** `U2 D B2 R2 F2 D' L2 F2 D2 L2 U2 R2 B2 U' L2 U' F2 L2 D2 L2 U' B2 U'`

Read as 4a4 4e on normal, 4b4 4e on inverse. Shortest HTR: 9 on normal, 11 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (26 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 68.4% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 74.8% | no / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.2% | no / yes |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / yes |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 81.5% | no / no |

- Class 1: inverse first: `(L2 B2 U' B2 D')`, then on normal `U L2 F2 U2 R2 D' F2 D2 B2 R2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U L2 F2 U2 R2 D' F2 D2 B2 R2 D B2 U B2 L2`.
- Class 2: normal first: `B2 R2 U' B2 U'`, then on inverse `(U' B2 D' R2 F2 U' L2 B2 U' L2)`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `B2 R2 U' B2 U' L2 U B2 L2 U F2 R2 D B2 U`.
- Class 3: normal first: `B2 R2 U' B2 U' L2 U`, then on inverse `(U' B2 D' R2 F2 U' L2 B2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 R2 U' B2 U' L2 U B2 L2 U F2 R2 D B2 U`.
- Class 4: inverse first: `(U')`, then on normal `U L2 F2 R2 L2 U F2 U' L2 D B2 D L2 B2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U L2 F2 R2 L2 U F2 U' L2 D B2 D L2 B2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `U (L2 B2 U' B2 D')`; the reduced state is then solved by `L2 F2 U2 R2 D' F2 D2 B2 R2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 3 moves, `U B2 D`; the reduced state is then solved by `F2 R2 U2 L2 D L2 B2 D F2 B2 R2 U2` (12 moves, 2 quarter turns).

</details>

**4c4 4e, example 5.** `D2 F2 D B2 U D B2 L2 U2 D2 R2 D' F2 D2 L2 U B2 R2 U B2 R2 U2 R2`

Read as 4a4 4e on normal, 4b4 4e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (29 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 68.4% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 74.8% | no / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.2% | no / yes |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / yes |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 81.5% | no / yes |

- Class 1: inverse first: `(L2 U' B2 F2 L2 D)`, then on normal `U R2 U' R2 B2 R2 B2 D2 L2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U R2 U' R2 B2 R2 B2 D2 L2 D' L2 F2 B2 U L2`.
- Class 2: normal first: `U2 R2 U L2 U`, then on inverse `(L2 D' F2 U L2 F2 D B2 U' B2)`. HTR after 14 moves (7 over the shortest NISS HTR); the whole finish, as read on normal: `U2 R2 U L2 U B2 U B2 D' F2 L2 U' F2 D L2`.
- Class 3: normal first: `U2 R2 U L2 U B2 U`, then on inverse `(L2 D' F2 U L2 F2 D B2)`. HTR after 14 moves (7 over the shortest NISS HTR); the whole finish, as read on normal: `U2 R2 U L2 U B2 U B2 D' F2 L2 U' F2 D L2`.
- Class 4: inverse first: `(U2 L2 D)`, then on normal `D' B2 U' F2 L2 U' B2 U L2 F2 D' F2`. HTR after 14 moves (7 over the shortest NISS HTR); the whole finish, as read on normal: `D' B2 U' F2 L2 U' B2 U L2 F2 D' F2 D' L2 U2`.
- Class 5: inverse first: `(L2 D')`, then on normal `U2 R2 U L2 U B2 U B2 D' F2 L2 U' F2`. HTR after 14 moves (7 over the shortest NISS HTR); the whole finish, as read on normal: `U2 R2 U L2 U B2 U B2 D' F2 L2 U' F2 D L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `U R2 U' (L2 U')`; the reduced state is then solved by `R2 B2 R2 B2 D2 L2 D' L2 F2 B2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 2e here) on an optimal path: 3 moves, `U (L2 U')`; the reduced state is then solved by `R2 U' R2 B2 R2 B2 D2 L2 D' L2 F2 B2` (12 moves, 2 quarter turns).

</details>

**4c4 4e, example 6.** `L2 U D F2 U2 D2 B2 U F2 U R2 D2 R2 B2 U L2 B2 L2 F2 D' R2`

Read as 4b4 4e on normal, 4a4 4e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (24 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 68.4% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 74.8% | yes / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.2% | no / yes |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / yes |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 81.5% | no / yes |

- Class 1: normal first: `R2 F2 L2 B2 U' L2 U'`, then on inverse `(R2 U' B2 D R2 D2 L2 F2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `R2 F2 L2 B2 U' L2 U' F2 L2 D2 R2 D' B2 U R2`.
- Class 2: inverse first: `(U R2 U')`, then on normal `U' L2 U' B2 U B2 R2 U F2 U2 F2 B2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U' L2 U' B2 U B2 R2 U F2 U2 F2 B2 U R2 U'`.
- Class 3: inverse first: `(U R2 U' B2 F2 U2 F2 U')`, then on normal `U' L2 U' B2 U B2 R2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U' L2 U' B2 U B2 R2 U F2 U2 F2 B2 U R2 U'`.
- Class 4: normal first: `U'`, then on inverse `(U R2 U' B2 F2 U2 F2 U' R2 B2 U' B2 U L2)`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U' L2 U' B2 U B2 R2 U F2 U2 F2 B2 U R2 U'`.
- Class 5: normal first: `D2 L2 B2 U`, then on inverse `(D' L2 D' F2 U' B2 D R2 U' F2 R2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D2 L2 B2 U R2 F2 U R2 D' B2 U F2 D L2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `U' L2 U' B2 U (U R2 U')`; the reduced state is then solved by `B2 R2 U F2 U2 F2 B2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `(R2 U' B2 D)`; the reduced state is then solved by `R2 F2 L2 B2 U' L2 U' F2 L2 D2 R2` (11 moves, 2 quarter turns).

</details>

**4c4 4e, example 7.** `U2 F2 D' R2 U2 L2 U2 B2 U L2 F2 U' L2 B2 D' L2 U F2 L2 U R2 B2`

Read as 4b4 4e on normal, 4a4 4e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (19 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 68.4% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 74.8% | no / yes |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.2% | no / yes |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 81.5% | no / yes |

- Class 1: normal first: `U2 F2 D' B2 U'`, then on inverse `(F2 U F2 R2 D' F2 L2 D2 F2 L2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U2 F2 D' B2 U' L2 F2 D2 L2 F2 D R2 F2 U' F2`.
- Class 2: inverse first: `(U F2 L2 U')`, then on normal `F2 R2 U' F2 U' F2 U F2 D' R2 F2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 R2 U' F2 U' F2 U F2 D' R2 F2 U L2 F2 U'`.
- Class 3: inverse first: `(U F2 L2 U' F2 R2 D)`, then on normal `F2 R2 U' F2 U' F2 U F2`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 R2 U' F2 U' F2 U F2 D' R2 F2 U L2 F2 U'`.
- Class 5: normal first: `F2 R2 U'`, then on inverse `(U F2 L2 U' F2 R2 D F2 U' F2 U F2)`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 R2 U' F2 U' F2 U F2 D' R2 F2 U L2 F2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U2 F2 D' B2 U' (F2 U)`; the reduced state is then solved by `L2 F2 D2 L2 F2 D R2 F2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `(B2 U' B2 U')`; the reduced state is then solved by `R2 B2 L2 B2 U' F2 U D2 B2 U2 R2` (11 moves, 2 quarter turns).

</details>

**4c4 4e, example 8.** `U D2 F2 U' B2 U2 D2 L2 F2 R2 D' B2 U R2 U F2 D' L2 D' B2 D'`

Read as 4a4 4e on normal, 4b4 4e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 68.4% | no / no |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 74.8% | no / no |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.2% | no / no |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 81.5% | no / no |

- None of these classes finds an optimal finish on this DR.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `U R2 F2 D' B2 D (U B2 U)`; the reduced state is then solved by `F2 B2 U B2 L2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 7 moves, `U (U B2 U L2 B2 U')`; the reduced state is then solved by `R2 F2 D' B2 D F2 B2` (7 moves, 2 quarter turns).

</details>

**4c4 4e, example 9.** `F2 R2 U2 L2 B2 D B2 U D2 B2 D' L2 B2 U2 L2 D' L2 U L2 B2 U`

Read as 4b4 4e on normal, 4a4 4e on inverse. Shortest HTR: 10 on normal, 11 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 16 moves (27 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 68.4% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 74.8% | no / no |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.2% | no / no |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 81.5% | no / no |

- Class 1: normal first: `R2 U L2 U'`, then on inverse `(U2 B2 R2 D' F2 L2 R2 U R2 D2 L2 B2)`. HTR after 12 moves (within the budget); the whole finish, as read on normal: `R2 U L2 U' B2 L2 D2 R2 U' R2 L2 F2 D R2 B2 U2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `L2 D L2 U' (D2 R2 D)`; the reduced state is then solved by `B2 U2 F2 L2 U' R2 F2 L2 F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `R2 U L2 U'`; the reduced state is then solved by `B2 L2 D2 R2 U' R2 L2 F2 D R2 B2 U2` (12 moves, 2 quarter turns).

</details>

**4c4 4e, example 10.** `U' D' B2 U2 R2 L2 U D' F2 D2 F2 L2 D' R2 U R2 D2 L2 F2 D F2 D' R2`

Read as 4b4 4e on normal, 4a4 4e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (9 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` | 68.4% | yes / yes |
| 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 74.8% | no / no |
| 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 78.2% | no / no |
| 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 80.2% | no / no |
| 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 81.5% | no / no |

- Class 1: normal first: `R2 U R2 D'`, then on inverse `(F2 D' F2 U' L2 F2 L2 R2 U2 L2 F2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `R2 U R2 D' F2 L2 U2 R2 L2 F2 L2 U F2 D F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `R2 U (F2 D' F2 U')`; the reduced state is then solved by `R2 D' F2 L2 U2 R2 L2 F2 L2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `(F2 D' F2 U')`; the reduced state is then solved by `R2 U R2 D' F2 L2 U2 R2 L2 F2 L2` (11 moves, 2 quarter turns).

</details>

## 4b2

### 4b2 2e

5.22% of all DR states.

**4b2 2e, example 1.** `U' F2 U' R2 F2 B2 U' D2 R2 L2 F2 D R2 D' L2 F2 D' F2 U' D' L2`

Read as 4b2 2e on normal, 4b2 2e on inverse. Shortest HTR: 6 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 45.9% | no / no |
| 2 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` | 53.7% | no / yes |
| 3 | `4b2 > 4a1 > (0c0)` | 59.0% | no / no |
| 4 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 63.3% | no / yes |
| 5 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 66.3% | no / yes |

- Class 2: inverse first: `(R2 D R2 F2 R2 D L2 D)`, then on normal `U' B2 D2 R2 B2`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' B2 D2 R2 B2 D' L2 D' R2 F2 R2 D' R2`.
- Class 4: linear on normal: `R2 B2 U' R2 L2 D L2 U L2 U2 R2 U' F2`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U' R2 L2 D L2 U L2 U2 R2 U' F2`.
- Class 5: normal first: `R2 B2 U' R2 L2 D`, then on inverse `(F2 U R2 U2 L2 U' L2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U' R2 L2 D L2 U L2 U2 R2 U' F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U' (R2 D R2 F2 R2 D)`; the reduced state is then solved by `B2 D2 R2 B2 D' L2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `U' (R2 D)`; the reduced state is then solved by `B2 D2 R2 B2 D' L2 D' R2 F2 R2` (10 moves, 2 quarter turns).

</details>

**4b2 2e, example 2.** `F2 B2 D L2 D B2 L2 F2 U B2 D2 L2 U F2 L2 B2 U2 F2 U B2 U'`

Read as 4b2 2e on normal, 4b2 2e on inverse. Shortest HTR: 7 on normal, 7 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (45 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 45.9% | yes / yes |
| 2 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` | 53.7% | yes / yes |
| 3 | `4b2 > 4a1 > (0c0)` | 59.0% | yes / yes |
| 4 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 63.3% | no / yes |
| 5 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 66.3% | yes / yes |

- Class 1: linear on normal: `U2 L2 B2 U' L2 F2 B2 D B2 R2 F2 D2 F2 D2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `U2 L2 B2 U' L2 F2 B2 D B2 R2 F2 D2 F2 D2`.
- Class 2: normal first: `U F2 U' F2 B2 R2 U`, then on inverse `(D' B2 R2 D2 R2 F2 R2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `U F2 U' F2 B2 R2 U R2 F2 R2 D2 R2 B2 D`.
- Class 3: normal first: `F2 U2 B2 D`, then on inverse `(D2 R2 F2 D' F2 D2 B2 L2 F2 L2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `F2 U2 B2 D L2 F2 L2 B2 D2 F2 D F2 R2 D2`.
- Class 4: linear on normal: `F2 U L2 U2 R2 U' R2 U L2 U B2 D2 B2 U2`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U L2 U2 R2 U' R2 U L2 U B2 D2 B2 U2`.
- Class 5: normal first: `D F2 L2 U'`, then on inverse `(U' F2 U L2 D2 F2 R2 B2 L2 R2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `D F2 L2 U' R2 L2 B2 R2 F2 D2 L2 U' F2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `U F2 U' (D')`; the reduced state is then solved by `F2 B2 R2 U R2 F2 R2 D2 R2 B2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `U2 L2 B2 U' L2 F2 B2 D B2 R2 F2 D2 F2 D2` (14 moves, 2 quarter turns).

</details>

**4b2 2e, example 3.** `D2 L2 U2 D2 R2 L2 B2 L2 B2 R2 B2 D R2 U R2 D2 F2 L2 B2 L2 U D`

Read as 4b2 2e on normal, 4b2 2e on inverse. Shortest HTR: 7 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 45.9% | no / no |
| 2 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` | 53.7% | no / yes |
| 3 | `4b2 > 4a1 > (0c0)` | 59.0% | no / no |
| 4 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 63.3% | no / yes |
| 5 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 66.3% | no / yes |

- Class 2: normal first: `R2 B2 D F2 U' B2 U'`, then on inverse `(F2 U2 L2 F2 D' B2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 D F2 U' B2 U' B2 D F2 L2 U2 F2`.
- Class 4: linear on normal: `R2 B2 D F2 U' B2 U' B2 D F2 L2 U2 F2`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 D F2 U' B2 U' B2 D F2 L2 U2 F2`.
- Class 5: normal first: `R2 B2 D F2 U'`, then on inverse `(F2 U2 L2 F2 D' B2 U B2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 D F2 U' B2 U' B2 D F2 L2 U2 F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `R2 B2 D F2 U' B2 U'`; the reduced state is then solved by `B2 D F2 L2 U2 F2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `(D' F2 U')`; the reduced state is then solved by `B2 R2 U2 L2 D F2 U B2 L2 B2` (10 moves, 2 quarter turns).

</details>

**4b2 2e, example 4.** `L2 U' F2 D' L2 U2 D2 B2 U2 D' L2 B2 D F2 D2 F2 D B2 R2 U2 R2 U F2`

Read as 4b2 2e on normal, 4b2 2e on inverse. Shortest HTR: 6 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (60 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 45.9% | yes / yes |
| 2 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` | 53.7% | no / yes |
| 3 | `4b2 > 4a1 > (0c0)` | 59.0% | yes / yes |
| 4 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 63.3% | no / yes |
| 5 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 66.3% | no / yes |

- Class 1: linear on the inverse: `(F2 D B2 U2 L2 R2 U F2 U2 L2 U2 L2 B2 U2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `U2 B2 L2 U2 L2 U2 F2 U' R2 L2 U2 B2 D' F2`.
- Class 2: normal first: `U D L2 F2 R2 D2 B2 U`, then on inverse `(F2 U R2 U2 B2 F2)`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U D L2 F2 R2 D2 B2 U F2 B2 U2 R2 U' F2`.
- Class 3: normal first: `F2 L2 F2 R2 D`, then on inverse `(L2 B2 U L2 B2 U2 B2 D2 L2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `F2 L2 F2 R2 D L2 D2 B2 U2 B2 L2 U' B2 L2`.
- Class 4: linear on the inverse: `(L2 U R2 B2 R2 F2 D' R2 U' L2 D' R2 F2 R2)`. HTR after 11 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 F2 R2 D L2 U R2 D F2 R2 B2 R2 U' L2`.
- Class 5: normal first: `U D`, then on inverse `(F2 U R2 U2 B2 F2 U' B2 D2 R2 F2 L2)`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U D L2 F2 R2 D2 B2 U F2 B2 U2 R2 U' F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 2 moves, `(F2 D)`; the reduced state is then solved by `U2 B2 L2 U2 L2 U2 F2 U' R2 L2 U2 B2` (12 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `U2 B2 L2 U2 L2 U2 F2 U' R2 L2 U2 B2 D' F2` (14 moves, 2 quarter turns).

</details>

**4b2 2e, example 5.** `F2 U2 D R2 F2 D L2 U2 D B2 L2 D2 F2 D' B2 U B2 U' R2 F2 R2 F2 R2 U R2 U'`

Read as 4b2 2e on normal, 4b2 2e on inverse. Shortest HTR: 6 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 45.9% | yes / yes |
| 2 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` | 53.7% | no / yes |
| 3 | `4b2 > 4a1 > (0c0)` | 59.0% | no / yes |
| 4 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 63.3% | no / yes |
| 5 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 66.3% | no / yes |

- Class 1: linear on normal: `L2 B2 L2 U R2 L2 B2 U' F2 U2 R2 U2 B2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `L2 B2 L2 U R2 L2 B2 U' F2 U2 R2 U2 B2`.
- Class 2: normal first: `F2 U F2 D R2 L2 B2 U`, then on inverse `(L2 B2 L2 U L2)`. HTR after 12 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U F2 D R2 L2 B2 U L2 U' L2 B2 L2`.
- Class 3: normal first: `L2 B2 L2 U`, then on inverse `(B2 U2 R2 U2 F2 U B2 L2 R2)`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 B2 L2 U R2 L2 B2 U' F2 U2 R2 U2 B2`.
- Class 4: linear on normal: `F2 U F2 D R2 L2 B2 U L2 U' L2 B2 L2`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U F2 D R2 L2 B2 U L2 U' L2 B2 L2`.
- Class 5: normal first: `F2 U F2 D`, then on inverse `(L2 B2 L2 U L2 U' B2 L2 R2)`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U F2 D R2 L2 B2 U L2 U' L2 B2 L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `L2 B2 L2 U`; the reduced state is then solved by `R2 L2 B2 U' F2 U2 R2 U2 B2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `L2 B2 L2 U R2 L2 B2 U' F2 U2 R2 U2 B2` (13 moves, 2 quarter turns).

</details>

**4b2 2e, example 6.** `R2 L2 U D' B2 R2 L2 U D' R2 U2 B2 D' B2 U F2 D2 R2 L2 B2 R2 D2`

Read as 4b2 2e on normal, 4b2 2e on inverse. Shortest HTR: 7 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (8 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 45.9% | yes / yes |
| 2 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` | 53.7% | no / yes |
| 3 | `4b2 > 4a1 > (0c0)` | 59.0% | no / yes |
| 4 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 63.3% | yes / yes |
| 5 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 66.3% | no / yes |

- Class 1: linear on the inverse: `(B2 U2 B2 D B2 F2 R2 D B2 F2 R2 U2 B2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `B2 U2 R2 F2 B2 D' R2 F2 B2 D' B2 U2 B2`.
- Class 2: normal first: `F2 U' L2 U L2 B2 L2 B2 D'`, then on inverse `(F2 D L2 F2)`. HTR after 11 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' L2 U L2 B2 L2 B2 D' F2 L2 D' F2`.
- Class 3: normal first: `B2 U2 R2 F2 B2 D'`, then on inverse `(B2 U2 B2 D B2 F2 R2)`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U2 R2 F2 B2 D' R2 F2 B2 D' B2 U2 B2`.
- Class 4: linear on the inverse: `(B2 U F2 U' R2 U' R2 D L2 B2 L2 B2 R2)`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `R2 B2 L2 B2 L2 D' R2 U R2 U F2 U' B2`.
- Class 5: normal first: `F2 U' L2 U`, then on inverse `(F2 D L2 F2 D B2 L2 B2 L2)`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' L2 U L2 B2 L2 B2 D' F2 L2 D' F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `(B2 U2 B2 D)`; the reduced state is then solved by `B2 U2 R2 F2 B2 D' R2 F2 B2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `B2 U2 R2 F2 B2 D' R2 F2 B2 D' B2 U2 B2` (13 moves, 2 quarter turns).

</details>

**4b2 2e, example 7.** `D' B2 U B2 U' D R2 D2 R2 B2 L2 D L2 F2 U2 F2 B2 R2 D`

Read as 4b2 2e on normal, 4b2 2e on inverse. Shortest HTR: 6 on normal, 6 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 45.9% | no / no |
| 2 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` | 53.7% | no / no |
| 3 | `4b2 > 4a1 > (0c0)` | 59.0% | no / no |
| 4 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 63.3% | no / no |
| 5 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 66.3% | no / no |

- None of these classes finds an optimal finish on this DR.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `U' B2 D (U')`; the reduced state is then solved by `L2 F2 R2 U' F2 R2 D2 L2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (0c0 2e here) on an optimal path: 2 moves, `U' (U')`; the reduced state is then solved by `B2 D L2 F2 R2 U' F2 R2 D2 L2` (10 moves, 2 quarter turns).

</details>

**4b2 2e, example 8.** `U D' B2 U' D F2 B2 R2 U' D B2 U R2 D R2 U' L2 B2 L2 D`

Read as 4b2 2e on normal, 4b2 2e on inverse. Shortest HTR: 6 on normal, 4 on inverse, 4 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 45.9% | yes / yes |
| 2 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` | 53.7% | no / no |
| 3 | `4b2 > 4a1 > (0c0)` | 59.0% | no / yes |
| 4 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 63.3% | no / no |
| 5 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 66.3% | no / no |

- Class 1: linear on the inverse: `(L2 U L2 D' F2 R2 D2 F2 L2 U2 B2 R2)`. HTR after 4 moves (within the budget); the whole finish, as read on normal: `R2 B2 U2 L2 F2 D2 R2 F2 D L2 U' L2`.
- Class 3: normal first: `R2 B2 U2 L2 F2 D2 R2 F2 D`, then on inverse `(L2 U L2)`. HTR after 11 moves (7 over the shortest NISS HTR); the whole finish, as read on normal: `R2 B2 U2 L2 F2 D2 R2 F2 D L2 U' L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 2 moves, `(L2 U)`; the reduced state is then solved by `R2 B2 U2 L2 F2 D2 R2 F2 D L2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `R2 B2 U2 L2 F2 D2 R2 F2 D L2 U' L2` (12 moves, 2 quarter turns).

</details>

**4b2 2e, example 9.** `D' R2 U' B2 R2 F2 U' D' L2 U' L2 F2 U R2 U B2 R2 L2 D L2`

Read as 4b2 2e on normal, 4b2 2e on inverse. Shortest HTR: 6 on normal, 5 on inverse, 5 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 11 moves (8 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 45.9% | no / no |
| 2 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` | 53.7% | yes / yes |
| 3 | `4b2 > 4a1 > (0c0)` | 59.0% | no / no |
| 4 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 63.3% | no / yes |
| 5 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 66.3% | no / yes |

- Class 2: inverse first: `(U' R2 D B2 U')`, then on normal `L2 U' F2 R2 L2 D2`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `L2 U' F2 R2 L2 D2 U B2 D' R2 U`.
- Class 4: linear on the inverse: `(U' R2 D B2 D2 U' L2 R2 F2 U L2)`. HTR after 10 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U' F2 R2 L2 U D2 B2 D' R2 U`.
- Class 5: normal first: `L2 U' F2 R2 L2 U`, then on inverse `(U' R2 D B2 D2)`. HTR after 9 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U' F2 R2 L2 U D2 B2 D' R2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `L2 U' (U' R2 D)`; the reduced state is then solved by `F2 R2 L2 U D2 B2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `(U' R2 D)`; the reduced state is then solved by `L2 U' F2 R2 L2 U D2 B2` (8 moves, 2 quarter turns).

</details>

**4b2 2e, example 10.** `B2 U' B2 U2 F2 B2 U' R2 U2 F2 L2 D2 L2 F2 U2 F2 U B2 R2 B2 D'`

Read as 4b2 2e on normal, 4b2 2e on inverse. Shortest HTR: 7 on normal, 4 on inverse, 4 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 11 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 45.9% | yes / yes |
| 2 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` | 53.7% | no / no |
| 3 | `4b2 > 4a1 > (0c0)` | 59.0% | no / yes |
| 4 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 63.3% | no / no |
| 5 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 66.3% | no / no |

- Class 1: linear on the inverse: `(F2 D' F2 U L2 F2 D2 R2 B2 D2 L2)`. HTR after 4 moves (within the budget); the whole finish, as read on normal: `L2 D2 B2 R2 D2 F2 L2 U' F2 D F2`.
- Class 3: normal first: `L2 D2 B2 R2 D2 F2 L2 U'`, then on inverse `(F2 D' F2)`. HTR after 10 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `L2 D2 B2 R2 D2 F2 L2 U' F2 D F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 2 moves, `(F2 D')`; the reduced state is then solved by `L2 D2 B2 R2 D2 F2 L2 U' F2` (9 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `L2 D2 B2 R2 D2 F2 L2 U' F2 D F2` (11 moves, 2 quarter turns).

</details>

### 4b2 4e

5.88% of all DR states.

**4b2 4e, example 1.** `U' D2 R2 U2 D' R2 U R2 U2 L2 D F2 D' B2 D' F2 U L2 D R2 D2`

Read as 4b2 4e on normal, 4b2 4e on inverse. Shortest HTR: 6 on normal, 8 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 30.3% | no / no |
| 2 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 53.3% | no / yes |
| 3 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 66.8% | no / yes |
| 4 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 71.7% | yes / yes |
| 5 | `4b2 > 4a1 > (0c0)` | 76.0% | no / no |

- Class 2: normal first: `U'`, then on inverse `(F2 D F2 D L2 D2 L2 F2 L2 D L2)`. HTR after 11 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U' L2 D' L2 F2 L2 D2 L2 D' F2 D' F2`.
- Class 3: linear on normal: `U' L2 D' L2 F2 L2 D2 L2 D' F2 D' F2`. HTR after 11 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U' L2 D' L2 F2 L2 D2 L2 D' F2 D' F2`.
- Class 4: normal first: `U' L2 D'`, then on inverse `(F2 D F2 D L2 D2 L2 F2 L2)`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `U' L2 D' L2 F2 L2 D2 L2 D' F2 D' F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `U' (F2 D F2 D)`; the reduced state is then solved by `L2 D' L2 F2 L2 D2 L2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 3 moves, `U' (F2 D)`; the reduced state is then solved by `L2 D' L2 F2 L2 D2 L2 D' F2` (9 moves, 2 quarter turns).

</details>

**4b2 4e, example 2.** `U' D B2 U2 F2 U D2 L2 F2 B2 D B2 U F2 R2 B2 D' R2 F2 R2 B2 U2`

Read as 4b2 4e on normal, 4b2 4e on inverse. Shortest HTR: 8 on normal, 7 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 30.3% | no / no |
| 2 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 53.3% | yes / yes |
| 3 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 66.8% | yes / yes |
| 4 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 71.7% | no / yes |
| 5 | `4b2 > 4a1 > (0c0)` | 76.0% | no / no |

- Class 2: normal first: `D`, then on inverse `(B2 F2 L2 U' R2 D R2 U' R2 U2 L2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `D L2 U2 R2 U R2 D' R2 U L2 F2 B2`.
- Class 3: linear on normal: `D L2 U2 R2 U R2 D' R2 U L2 F2 B2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `D L2 U2 R2 U R2 D' R2 U L2 F2 B2`.
- Class 4: normal first: `D L2 U2 R2 U`, then on inverse `(B2 F2 L2 U' R2 D R2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D L2 U2 R2 U R2 D' R2 U L2 F2 B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `D (B2 F2 L2 U' R2 D)`; the reduced state is then solved by `L2 U2 R2 U R2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `D (B2 F2 L2 U')`; the reduced state is then solved by `L2 U2 R2 U R2 D' R2` (7 moves, 2 quarter turns).

</details>

**4b2 4e, example 3.** `F2 U' B2 R2 D' B2 L2 D' R2 D F2 D2 B2 U' B2 L2 D2 R2 L2 U'`

Read as 4b2 4e on normal, 4b2 4e on inverse. Shortest HTR: 8 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 30.3% | no / no |
| 2 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 53.3% | no / yes |
| 3 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 66.8% | no / yes |
| 4 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 71.7% | yes / yes |
| 5 | `4b2 > 4a1 > (0c0)` | 76.0% | no / no |

- Class 2: normal first: `F2 U`, then on inverse `(D' R2 D B2 L2 B2 L2 D F2 U2 F2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U F2 U2 F2 D' L2 B2 L2 B2 D' R2 D`.
- Class 3: linear on the inverse: `(D' R2 D B2 L2 B2 L2 D F2 U2 F2 U' F2)`. HTR after 12 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U F2 U2 F2 D' L2 B2 L2 B2 D' R2 D`.
- Class 4: normal first: `F2 U F2 U2 F2 D'`, then on inverse `(D' R2 D B2 L2 B2 L2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `F2 U F2 U2 F2 D' L2 B2 L2 B2 D' R2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `F2 U (D' R2 D)`; the reduced state is then solved by `F2 U2 F2 D' L2 B2 L2 B2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 3 moves, `(D' R2 D)`; the reduced state is then solved by `F2 U F2 U2 F2 D' L2 B2 L2 B2` (10 moves, 2 quarter turns).

</details>

**4b2 4e, example 4.** `R2 F2 U' D2 B2 U' B2 U D L2 F2 U L2 U2 L2 F2 R2 U F2 R2 U2 F2 U2`

Read as 4b2 4e on normal, 4b2 4e on inverse. Shortest HTR: 9 on normal, 7 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 30.3% | no / no |
| 2 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 53.3% | yes / yes |
| 3 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 66.8% | no / yes |
| 4 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 71.7% | no / yes |
| 5 | `4b2 > 4a1 > (0c0)` | 76.0% | no / no |

- Class 2: inverse first: `(U')`, then on normal `D' F2 U F2 R2 D' F2 U2 R2 B2 L2`. HTR after 7 moves (within the budget); the whole finish, as read on normal: `D' F2 U F2 R2 D' F2 U2 R2 B2 L2 U`.
- Class 3: linear on normal: `D' F2 U F2 R2 D' F2 U2 R2 B2 L2 U`. HTR after 12 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `D' F2 U F2 R2 D' F2 U2 R2 B2 L2 U`.
- Class 4: normal first: `D' F2 U`, then on inverse `(U' L2 B2 R2 U2 F2 D R2 F2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D' F2 U F2 R2 D' F2 U2 R2 B2 L2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 4 moves, `D' F2 U (U')`; the reduced state is then solved by `F2 R2 D' F2 U2 R2 B2 L2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 2 moves, `D' (U')`; the reduced state is then solved by `F2 U F2 R2 D' F2 U2 R2 B2 L2` (10 moves, 2 quarter turns).

</details>

**4b2 4e, example 5.** `D B2 U D2 R2 D2 R2 D2 L2 U L2 F2 D2 L2 U' B2 L2 U' B2 L2 U' B2`

Read as 4b2 4e on normal, 4b2 4e on inverse. Shortest HTR: 9 on normal, 5 on inverse, 5 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (3 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 30.3% | yes / yes |
| 2 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 53.3% | no / yes |
| 3 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 66.8% | no / yes |
| 4 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 71.7% | no / yes |
| 5 | `4b2 > 4a1 > (0c0)` | 76.0% | no / yes |

- Class 1: linear on the inverse: `(L2 U' L2 B2 D' L2 D2 B2 D2 B2 L2 F2)`. HTR after 5 moves (within the budget); the whole finish, as read on normal: `F2 L2 B2 D2 B2 D2 L2 D B2 L2 U L2`.
- Class 2: normal first: `F2 L2 B2 L2 U`, then on inverse `(L2 D' B2 R2 D R2 D')`. HTR after 12 moves (7 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 B2 L2 U D R2 D' R2 B2 D L2`.
- Class 3: linear on normal: `F2 L2 B2 L2 U D R2 D' R2 B2 D L2`. HTR after 11 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 B2 L2 U D R2 D' R2 B2 D L2`.
- Class 4: normal first: `F2 L2 B2 L2 U D`, then on inverse `(L2 D' B2 R2 D R2)`. HTR after 11 moves (6 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 B2 L2 U D R2 D' R2 B2 D L2`.
- Class 5: normal first: `F2 L2 B2 D2 B2 D2 L2 D`, then on inverse `(L2 U' L2 B2)`. HTR after 10 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 B2 D2 B2 D2 L2 D B2 L2 U L2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 2 moves, `(L2 U')`; the reduced state is then solved by `F2 L2 B2 D2 B2 D2 L2 D B2 L2` (10 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `F2 L2 B2 D2 B2 D2 L2 D B2 L2 U L2` (12 moves, 2 quarter turns).

</details>

**4b2 4e, example 6.** `R2 L2 B2 U' D' L2 U B2 L2 F2 D L2 U' L2 D R2 U B2 L2 D R2`

Read as 4b2 4e on normal, 4b2 4e on inverse. Shortest HTR: 9 on normal, 8 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 12 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 30.3% | no / no |
| 2 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 53.3% | no / yes |
| 3 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 66.8% | yes / yes |
| 4 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 71.7% | no / yes |
| 5 | `4b2 > 4a1 > (0c0)` | 76.0% | no / no |

- Class 2: inverse first: `(D2 F2 R2 U')`, then on normal `R2 D' L2 U B2 U F2 L2`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 D' L2 U B2 U F2 L2 U R2 F2 D2`.
- Class 3: linear on normal: `R2 D' L2 U B2 U F2 L2 U R2 F2 D2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `R2 D' L2 U B2 U F2 L2 U R2 F2 D2`.
- Class 4: normal first: `R2 D' L2 U`, then on inverse `(D2 F2 R2 U' L2 F2 U' B2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 D' L2 U B2 U F2 L2 U R2 F2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `R2 D' L2 U B2 U`; the reduced state is then solved by `F2 L2 U R2 F2 D2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 4 moves, `R2 D' L2 U`; the reduced state is then solved by `B2 U F2 L2 U R2 F2 D2` (8 moves, 2 quarter turns).

</details>

**4b2 4e, example 7.** `D R2 D F2 U R2 U L2 U' D' L2 D F2 R2 U F2 U' L2 D F2 L2 U2 L2`

Read as 4b2 4e on normal, 4b2 4e on inverse. Shortest HTR: 8 on normal, 8 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (4 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 30.3% | yes / yes |
| 2 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 53.3% | no / no |
| 3 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 66.8% | no / no |
| 4 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 71.7% | no / no |
| 5 | `4b2 > 4a1 > (0c0)` | 76.0% | yes / yes |

- Class 1: linear on normal: `B2 U2 F2 L2 D B2 R2 D' U2 R2 L2 B2 U2`. HTR after 8 moves (within the budget); the whole finish, as read on normal: `B2 U2 F2 L2 D B2 R2 D' U2 R2 L2 B2 U2`.
- Class 5: normal first: `B2 U2 F2 L2 D`, then on inverse `(U2 B2 L2 R2 D U2 R2 B2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `B2 U2 F2 L2 D B2 R2 U2 D' R2 L2 B2 U2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 5 moves, `(U2 B2 L2 R2 D)`; the reduced state is then solved by `B2 U2 F2 L2 D B2 R2 U2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `B2 U2 F2 L2 D B2 R2 U2 D' R2 L2 B2 U2` (13 moves, 2 quarter turns).

</details>

**4b2 4e, example 8.** `D' F2 R2 U2 D L2 D' F2 U D' R2 F2 D L2 U2 F2 U' R2 D R2 U' F2 R2 U'`

Read as 4b2 4e on normal, 4b2 4e on inverse. Shortest HTR: 8 on normal, 7 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 30.3% | no / no |
| 2 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 53.3% | no / yes |
| 3 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 66.8% | no / yes |
| 4 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 71.7% | yes / yes |
| 5 | `4b2 > 4a1 > (0c0)` | 76.0% | no / no |

- Class 2: inverse first: `(U)`, then on normal `B2 R2 U' F2 D' R2 L2 D2 R2 D L2 B2`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 R2 U' F2 D' R2 L2 D2 R2 D L2 B2 U'`.
- Class 3: linear on the inverse: `(U B2 L2 D' R2 D2 L2 R2 D F2 U R2 B2)`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 R2 U' F2 D' R2 L2 D2 R2 D L2 B2 U'`.
- Class 4: normal first: `B2 R2 U' F2 D'`, then on inverse `(U B2 L2 D' R2 D2 L2 R2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `B2 R2 U' F2 D' R2 L2 D2 R2 D L2 B2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `B2 R2 U' F2 D' (U)`; the reduced state is then solved by `R2 L2 D2 R2 D L2 B2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `(U B2 L2 D')`; the reduced state is then solved by `B2 R2 U' F2 D' R2 L2 D2 R2` (9 moves, 2 quarter turns).

</details>

**4b2 4e, example 9.** `F2 B2 R2 U D F2 R2 D2 R2 F2 B2 D L2 F2 L2 U F2 L2 D B2 D'`

Read as 4b2 4e on normal, 4b2 4e on inverse. Shortest HTR: 6 on normal, 8 on inverse, 6 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (68 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 30.3% | yes / yes |
| 2 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 53.3% | no / yes |
| 3 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 66.8% | no / yes |
| 4 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 71.7% | no / yes |
| 5 | `4b2 > 4a1 > (0c0)` | 76.0% | no / yes |

- Class 1: linear on normal: `D B2 L2 B2 R2 U R2 U2 R2 F2 L2 F2 R2 D2`. HTR after 6 moves (within the budget); the whole finish, as read on normal: `D B2 L2 B2 R2 U R2 U2 R2 F2 L2 F2 R2 D2`.
- Class 2: inverse first: `(F2 D')`, then on normal `U2 L2 U B2 D R2 U' F2 R2 D2 L2 F2`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U2 L2 U B2 D R2 U' F2 R2 D2 L2 F2 D F2`.
- Class 3: linear on normal: `R2 D' R2 D' B2 D' B2 L2 U' D2 R2 F2 U2 R2`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 D' R2 D' B2 D' B2 L2 U' D2 R2 F2 U2 R2`.
- Class 4: inverse first: `(F2 D' B2 F2 D')`, then on normal `D L2 B2 U' B2 U2 B2 U2 L2`. HTR after 9 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D L2 B2 U' B2 U2 B2 U2 L2 D F2 B2 D F2`.
- Class 5: normal first: `D`, then on inverse `(D2 R2 F2 L2 F2 R2 U2 R2 U' R2 B2 L2 B2)`. HTR after 10 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D B2 L2 B2 R2 U R2 U2 R2 F2 L2 F2 R2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 1 move, `D`; the reduced state is then solved by `B2 L2 B2 R2 U R2 U2 R2 F2 L2 F2 R2 D2` (13 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 0 moves (the DR is already there); the reduced state is then solved by `D B2 L2 B2 R2 U R2 U2 R2 F2 L2 F2 R2 D2` (14 moves, 2 quarter turns).

</details>

**4b2 4e, example 10.** `U' R2 U' D2 L2 F2 U D' R2 L2 U' R2 B2 D' B2 U2 L2 D' F2 B2 R2 U'`

Read as 4b2 4e on normal, 4b2 4e on inverse. Shortest HTR: 9 on normal, 9 on inverse, 7 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b2 > 4a1 > 0c0` | 30.3% | no / no |
| 2 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 53.3% | no / yes |
| 3 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 66.8% | no / yes |
| 4 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` | 71.7% | no / yes |
| 5 | `4b2 > 4a1 > (0c0)` | 76.0% | no / no |

- Class 2: normal first: `R2 F2 D`, then on inverse `(D2 B2 D' F2 D F2 L2 R2 D B2)`. HTR after 12 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `R2 F2 D B2 D' R2 L2 F2 D' F2 D B2 D2`.
- Class 3: linear on normal: `R2 F2 D B2 D' R2 L2 F2 D' F2 D B2 D2`. HTR after 11 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 F2 D B2 D' R2 L2 F2 D' F2 D B2 D2`.
- Class 4: normal first: `R2 F2 D B2 D'`, then on inverse `(D2 B2 D' F2 D F2 L2 R2)`. HTR after 10 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `R2 F2 D B2 D' R2 L2 F2 D' F2 D B2 D2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `R2 F2 D (D2 B2 D' F2 D)`; the reduced state is then solved by `B2 D' R2 L2 F2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `(D2 B2 D' F2 D)`; the reduced state is then solved by `R2 F2 D B2 D' R2 L2 F2` (8 moves, 2 quarter turns).

</details>

## 4b5

### 4b5 2e

5.22% of all DR states.

**4b5 2e, example 1.** `L2 F2 U D R2 F2 U' D2 B2 D2 B2 L2 F2 U' R2 U' F2 U F2 D B2`

Read as 4b5 2e on normal, 4b5 2e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (12 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 62.6% | no / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 85.1% | no / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 93.7% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 93.8% | no / no |

- Class 1: inverse first: `(R2 B2 U')`, then on normal `F2 B2 U B2 U' F2 D R2 D U2 L2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 U B2 U' F2 D R2 D U2 L2 U B2 R2`.
- Class 2: normal first: `F2 B2 U B2 D'`, then on inverse `(R2 B2 D' B2 U R2 U D2 L2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 U B2 D' L2 D2 U' R2 U' B2 D B2 R2`.
- Class 3: linear on normal: `F2 B2 U B2 U' F2 D R2 U2 D L2 U B2 R2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 U B2 U' F2 D R2 U2 D L2 U B2 R2`.
- Class 4: normal first: `F2 B2 U B2 U' F2 D`, then on inverse `(R2 B2 U' L2 D' U2 R2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 B2 U B2 U' F2 D R2 U2 D L2 U B2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `F2 B2 U B2 U' F2 D R2 D`; the reduced state is then solved by `U2 L2 U B2 R2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 7 moves, `F2 B2 U B2 U' F2 D`; the reduced state is then solved by `R2 U2 D L2 U B2 R2` (7 moves, 2 quarter turns).

</details>

**4b5 2e, example 2.** `R2 D' F2 B2 U' D' L2 U' D' L2 F2 R2 F2 U B2 U B2 U' B2 R2 L2 U F2`

Read as 4b5 2e on normal, 4b5 2e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 62.6% | no / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 85.1% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% | yes / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 93.7% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 93.8% | no / yes |

- Class 1: normal first: `D'`, then on inverse `(F2 U2 R2 D L2 U B2 U' L2 F2 U' R2 F2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D' F2 R2 U F2 L2 U B2 U' L2 D' R2 U2 F2`.
- Class 2: normal first: `U' R2 B2 D`, then on inverse `(F2 U R2 D' R2 U' B2 L2 D2 L2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U' R2 B2 D L2 D2 L2 B2 U R2 D R2 U' F2`.
- Class 3: linear on normal: `D' F2 R2 U F2 L2 U B2 U' L2 D' R2 U2 F2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `D' F2 R2 U F2 L2 U B2 U' L2 D' R2 U2 F2`.
- Class 4: normal first: `U' B2 D L2 U2 R2 F2 U`, then on inverse `(F2 D B2 U' B2 L2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' B2 D L2 U2 R2 F2 U L2 B2 U B2 D' F2`.
- Class 5: normal first: `U'`, then on inverse `(F2 U R2 D' R2 U' B2 L2 D2 L2 D' B2 R2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' R2 B2 D L2 D2 L2 B2 U R2 D R2 U' F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U' (F2 U R2 D' R2 U')`; the reduced state is then solved by `R2 B2 D L2 D2 L2 B2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 5 moves, `U' (F2 U R2 D')`; the reduced state is then solved by `R2 B2 D L2 D2 L2 B2 U R2` (9 moves, 2 quarter turns).

</details>

**4b5 2e, example 3.** `D' F2 L2 D B2 U D2 B2 U' D2 R2 B2 U' F2 U' R2 B2 D R2 U2`

Read as 4b5 2e on normal, 4b5 2e on inverse. Shortest HTR: 11 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 62.6% | no / no |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 85.1% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 93.7% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 93.8% | no / yes |

- Class 2: normal first: `F2 U B2 U`, then on inverse `(U2 F2 U' R2 D F2 D' R2 F2 D2 B2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `F2 U B2 U B2 D2 F2 R2 D F2 D' R2 U F2 U2`.
- Class 3: linear on normal: `F2 U B2 U B2 D2 F2 R2 D F2 D' R2 U F2 U2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U B2 U B2 D2 F2 R2 D F2 D' R2 U F2 U2`.
- Class 4: normal first: `F2 U B2 U B2 D2 F2 R2 D`, then on inverse `(U2 F2 U' R2 D F2)`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U B2 U B2 D2 F2 R2 D F2 D' R2 U F2 U2`.
- Class 5: normal first: `F2 U`, then on inverse `(U2 F2 U' R2 D F2 D' R2 F2 D2 B2 U' B2)`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U B2 U B2 D2 F2 R2 D F2 D' R2 U F2 U2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `F2 U (U2 F2 U' R2 D F2 D')`; the reduced state is then solved by `B2 U B2 D2 F2 R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 7 moves, `(U2 F2 U' R2 D F2 D')`; the reduced state is then solved by `F2 U B2 U B2 D2 F2 R2` (8 moves, 2 quarter turns).

</details>

**4b5 2e, example 4.** `U D' L2 U2 D2 F2 R2 U' D2 L2 B2 U R2 U L2 F2 D2 L2 D B2 D F2 U F2 U'`

Read as 4b5 2e on normal, 4b5 2e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 62.6% | yes / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 85.1% | no / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 93.7% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 93.8% | no / no |

- Class 1: inverse first: `(R2 F2 D')`, then on normal `U' B2 R2 U B2 U' L2 U' L2 U2 F2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `U' B2 R2 U B2 U' L2 U' L2 U2 F2 D F2 R2`.
- Class 2: inverse first: `(R2 F2 D' F2 U2 L2 U)`, then on normal `U' B2 R2 U B2 U' L2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U' B2 R2 U B2 U' L2 U' L2 U2 F2 D F2 R2`.
- Class 3: linear on the inverse: `(B2 D' B2 D2 L2 U' F2 U' B2 U B2 L2 D' B2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 D L2 B2 U' B2 U F2 U L2 D2 B2 D B2`.
- Class 4: inverse first: `(R2 F2 D' F2 U2 L2 U L2 U)`, then on normal `U' B2 R2 U B2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U' B2 R2 U B2 U' L2 U' L2 U2 F2 D F2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `U' B2 R2 U B2 U' L2 U'`; the reduced state is then solved by `L2 U2 F2 D F2 R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 6 moves, `U' B2 R2 U B2 U'`; the reduced state is then solved by `L2 U' L2 U2 F2 D F2 R2` (8 moves, 2 quarter turns).

</details>

**4b5 2e, example 5.** `U D2 R2 U D' B2 R2 F2 B2 U2 F2 L2 U F2 U R2 U' B2 R2 U' F2 R2 L2`

Read as 4b5 2e on normal, 4b5 2e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 62.6% | yes / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 85.1% | no / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 93.7% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 93.8% | no / no |

- Class 1: inverse first: `(U')`, then on normal `B2 U' B2 L2 D' B2 U F2 U' F2 R2 U2 R2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `B2 U' B2 L2 D' B2 U F2 U' F2 R2 U2 R2 U`.
- Class 2: inverse first: `(U' R2 U2 R2 F2 U)`, then on normal `B2 U' B2 L2 D' B2 U F2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U' B2 L2 D' B2 U F2 U' F2 R2 U2 R2 U`.
- Class 3: linear on the inverse: `(U' R2 U2 R2 F2 U F2 U' B2 D L2 B2 U B2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U' B2 L2 D' B2 U F2 U' F2 R2 U2 R2 U`.
- Class 4: inverse first: `(U' R2 U2 R2 F2 U F2 U')`, then on normal `B2 U' B2 L2 D' B2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U' B2 L2 D' B2 U F2 U' F2 R2 U2 R2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `B2 U' B2 L2 D' B2 U (U')`; the reduced state is then solved by `F2 U' F2 R2 U2 R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `B2 U' B2 L2 D' (U')`; the reduced state is then solved by `B2 U F2 U' F2 R2 U2 R2` (8 moves, 2 quarter turns).

</details>

**4b5 2e, example 6.** `F2 U L2 U' L2 U2 F2 B2 U' B2 D' L2 D' B2 L2 D' L2 D' B2 D2 F2 R2 L2`

Read as 4b5 2e on normal, 4b5 2e on inverse. Shortest HTR: 10 on normal, 9 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 62.6% | no / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 85.1% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% | yes / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 93.7% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 93.8% | no / yes |

- Class 1: normal first: `F2 L2 U2 R2 B2 D'`, then on inverse `(U' R2 U B2 U' L2 U R2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 U2 R2 B2 D' R2 U' L2 U B2 U' R2 U`.
- Class 2: inverse first: `(D' L2 F2 U)`, then on normal `L2 U' L2 D B2 D' R2 U2 L2 F2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `L2 U' L2 D B2 D' R2 U2 L2 F2 U' F2 L2 D`.
- Class 3: linear on the inverse: `(U' R2 U B2 U' L2 U R2 D B2 R2 U2 L2 F2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `F2 L2 U2 R2 B2 D' R2 U' L2 U B2 U' R2 U`.
- Class 4: normal first: `F2 L2 U2 R2 B2 D' R2 U' L2 U`, then on inverse `(U' R2 U B2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 U2 R2 B2 D' R2 U' L2 U B2 U' R2 U`.
- Class 5: inverse first: `(D')`, then on normal `L2 U' L2 D B2 D' R2 U2 L2 F2 U' F2 L2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U' L2 D B2 D' R2 U2 L2 F2 U' F2 L2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `L2 U' L2 D B2 D' (D')`; the reduced state is then solved by `R2 U2 L2 F2 U' F2 L2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 5 moves, `L2 U' L2 D (D')`; the reduced state is then solved by `B2 D' R2 U2 L2 F2 U' F2 L2` (9 moves, 2 quarter turns).

</details>

**4b5 2e, example 7.** `U2 D2 R2 D2 R2 L2 U' R2 F2 U L2 B2 U L2 U' B2 L2 U' D2 R2 F2`

Read as 4b5 2e on normal, 4b5 2e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 62.6% | no / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 85.1% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% | yes / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 93.7% | yes / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 93.8% | no / no |

- Class 1: normal first: `D'`, then on inverse `(R2 B2 U' L2 U' F2 L2 U' B2 R2 D' B2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D' B2 D R2 B2 U L2 F2 U L2 U B2 R2`.
- Class 2: normal first: `D' B2 D`, then on inverse `(R2 B2 U' L2 U' F2 L2 U' B2 R2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `D' B2 D R2 B2 U L2 F2 U L2 U B2 R2`.
- Class 3: linear on normal: `D' B2 D R2 B2 U L2 F2 U L2 U B2 R2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `D' B2 D R2 B2 U L2 F2 U L2 U B2 R2`.
- Class 4: normal first: `D' B2 D R2 B2 U`, then on inverse `(R2 B2 U' L2 U' F2 L2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `D' B2 D R2 B2 U L2 F2 U L2 U B2 R2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `D' B2 D (R2 B2 U' L2 U')`; the reduced state is then solved by `R2 B2 U L2 F2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 6 moves, `D' (R2 B2 U' L2 U')`; the reduced state is then solved by `B2 D R2 B2 U L2 F2` (7 moves, 2 quarter turns).

</details>

**4b5 2e, example 8.** `U' F2 L2 U D2 L2 U' D R2 L2 F2 B2 U2 B2 D B2 U R2 D' F2 R2 F2 U2`

Read as 4b5 2e on normal, 4b5 2e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 62.6% | yes / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 85.1% | no / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 93.7% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 93.8% | no / no |

- Class 1: inverse first: `(D')`, then on normal `U' F2 L2 U R2 D' B2 U' B2 D2 B2 R2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U' F2 L2 U R2 D' B2 U' B2 D2 B2 R2 D`.
- Class 2: inverse first: `(D' R2 B2 D2 B2 U)`, then on normal `U' F2 L2 U R2 D' B2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' F2 L2 U R2 D' B2 U' B2 D2 B2 R2 D`.
- Class 3: linear on the inverse: `(D' R2 B2 D2 B2 U B2 D R2 U' L2 F2 U)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U' F2 L2 U R2 D' B2 U' B2 D2 B2 R2 D`.
- Class 4: inverse first: `(D' R2 B2 D2 B2 U B2 D)`, then on normal `U' F2 L2 U R2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U' F2 L2 U R2 D' B2 U' B2 D2 B2 R2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U' F2 L2 U R2 D' (D')`; the reduced state is then solved by `B2 U' B2 D2 B2 R2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `U' F2 L2 U (D')`; the reduced state is then solved by `R2 D' B2 U' B2 D2 B2 R2` (8 moves, 2 quarter turns).

</details>

**4b5 2e, example 9.** `B2 D B2 U R2 U2 D' B2 U2 F2 U' F2 L2 B2 U' R2 D' F2 U' B2 U2`

Read as 4b5 2e on normal, 4b5 2e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (18 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 62.6% | yes / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 85.1% | no / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% | yes / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 93.7% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 93.8% | no / yes |

- Class 1: inverse first: `(U)`, then on normal `B2 U' B2 D R2 U' L2 B2 D R2 U2 F2 B2 R2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `B2 U' B2 D R2 U' L2 B2 D R2 U2 F2 B2 R2 U'`.
- Class 2: normal first: `B2 L2 D L2 U`, then on inverse `(F2 U R2 B2 D F2 U L2 D2 B2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 L2 D L2 U B2 D2 L2 U' F2 D' B2 R2 U' F2`.
- Class 3: linear on the inverse: `(F2 R2 U' F2 D R2 D' R2 D L2 U' B2 U2 L2 B2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `B2 L2 U2 B2 U L2 D' R2 D R2 D' F2 U R2 F2`.
- Class 4: normal first: `F2 U' L2 U' B2 D`, then on inverse `(U2 L2 B2 D F2 D F2 L2 R2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' L2 U' B2 D R2 L2 F2 D' F2 D' B2 L2 U2`.
- Class 5: normal first: `B2 L2 D`, then on inverse `(F2 U R2 B2 D F2 U L2 D2 B2 U' L2)`. HTR after 14 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `B2 L2 D L2 U B2 D2 L2 U' F2 D' B2 R2 U' F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `B2 U' B2 D R2 U' (U)`; the reduced state is then solved by `L2 B2 D R2 U2 F2 B2 R2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 5 moves, `B2 U' B2 D (U)`; the reduced state is then solved by `R2 U' L2 B2 D R2 U2 F2 B2 R2` (10 moves, 2 quarter turns).

</details>

**4b5 2e, example 10.** `U2 R2 U2 B2 U' D B2 U' D2 B2 U' D' L2 B2 D' R2 F2 U R2 U' R2 U`

Read as 4b5 2e on normal, 4b5 2e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (14 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 62.6% | yes / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 85.1% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% | yes / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 93.7% | yes / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 93.8% | no / no |

- Class 1: normal first: `U'`, then on inverse `(L2 U' L2 U R2 U' F2 U' L2 B2 D2 L2 F2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U' F2 L2 D2 B2 L2 U F2 U R2 U' L2 U L2`.
- Class 2: inverse first: `(U2 R2 D' R2 D)`, then on normal `U R2 D B2 U' L2 F2 L2 B2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U R2 D B2 U' L2 F2 L2 B2 D' R2 D R2 U2`.
- Class 3: linear on normal: `U R2 D B2 U' R2 D B2 D' B2 L2 F2 L2 U2`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U R2 D B2 U' R2 D B2 D' B2 L2 F2 L2 U2`.
- Class 4: normal first: `U R2 D B2 U'`, then on inverse `(U2 R2 D' R2 D B2 L2 F2 L2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U R2 D B2 U' L2 F2 L2 B2 D' R2 D R2 U2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U R2 D B2 U' R2 D`; the reduced state is then solved by `B2 D' B2 L2 F2 L2 U2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `U R2 D B2 U'`; the reduced state is then solved by `R2 D B2 D' B2 L2 F2 L2 U2` (9 moves, 2 quarter turns).

</details>

### 4b5 4e

5.88% of all DR states.

**4b5 4e, example 1.** `F2 B2 D' B2 U2 D' F2 D2 F2 U R2 U' B2 D R2 U' F2 U2 F2 R2 F2 U`

Read as 4b5 4e on normal, 4b5 4e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (16 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 67.0% | yes / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 89.6% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.9% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 94.0% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 94.0% | no / yes |

- Class 1: normal first: `D`, then on inverse `(R2 D' F2 R2 U L2 U' R2 U F2 L2 U2 R2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `D R2 U2 L2 F2 U' R2 U L2 U' R2 F2 D R2`.
- Class 2: normal first: `U R2 U'`, then on inverse `(D' F2 L2 R2 U' B2 D F2 R2 D2 R2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U R2 U' R2 D2 R2 F2 D' B2 U R2 L2 F2 D`.
- Class 3: linear on normal: `B2 U F2 D2 L2 U F2 U' F2 D R2 D' L2 F2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `B2 U F2 D2 L2 U F2 U' F2 D R2 D' L2 F2`.
- Class 4: normal first: `F2 D L2 U2 L2 D F2 U`, then on inverse `(R2 D L2 D' F2 R2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 D L2 U2 L2 D F2 U R2 F2 D L2 D' R2`.
- Class 5: normal first: `U`, then on inverse `(D' F2 L2 R2 U' B2 D F2 R2 D2 R2 U R2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U R2 U' R2 D2 R2 F2 D' B2 U R2 L2 F2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `U (D' F2 L2 R2 U' B2 D)`; the reduced state is then solved by `R2 U' R2 D2 R2 F2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `U R2 U' (D')`; the reduced state is then solved by `R2 D2 R2 F2 D' B2 U R2 L2 F2` (10 moves, 2 quarter turns).

</details>

**4b5 4e, example 2.** `F2 R2 U2 D' B2 R2 F2 B2 R2 D F2 U2 F2 D' F2 U2 R2 B2 L2 F2 U' F2 U2 L2 U'`

Read as 4b5 4e on normal, 4b5 4e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (5 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 67.0% | no / no |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 89.6% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.9% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 94.0% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 94.0% | yes / yes |

- Class 2: inverse first: `(U' R2 U2 F2 D)`, then on normal `F2 U' B2 U L2 D B2 L2 D2 L2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `F2 U' B2 U L2 D B2 L2 D2 L2 D' F2 U2 R2 U`.
- Class 3: linear on the inverse: `(U' R2 U2 F2 D L2 D2 L2 B2 D' L2 U' B2 U F2)`. HTR after 14 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' B2 U L2 D B2 L2 D2 L2 D' F2 U2 R2 U`.
- Class 4: inverse first: `(U' R2 U2 F2 D L2 D2 L2 B2 D')`, then on normal `F2 U' B2 U L2`. HTR after 14 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' B2 U L2 D B2 L2 D2 L2 D' F2 U2 R2 U`.
- Class 5: inverse first: `(U')`, then on normal `F2 U' B2 D F2 U B2 U2 R2 D' B2 D2 B2 R2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `F2 U' B2 D F2 U B2 U2 R2 D' B2 D2 B2 R2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `F2 U' B2 U L2 D (U')`; the reduced state is then solved by `B2 L2 D2 L2 D' F2 U2 R2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 5 moves, `F2 U' B2 U (U')`; the reduced state is then solved by `L2 D B2 L2 D2 L2 D' F2 U2 R2` (10 moves, 2 quarter turns).

</details>

**4b5 4e, example 3.** `D R2 U' L2 F2 U R2 L2 U2 F2 R2 D' L2 B2 U R2 U' R2 F2 U L2 B2 D2 R2`

Read as 4b5 4e on normal, 4b5 4e on inverse. Shortest HTR: 11 on normal, 11 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 15 moves (19 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 67.0% | yes / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 89.6% | no / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.9% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 94.0% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 94.0% | no / no |

- Class 1: normal first: `L2 U`, then on inverse `(D' B2 R2 U' L2 B2 U' F2 U' L2 D2 B2 R2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `L2 U R2 B2 D2 L2 U F2 U B2 L2 U R2 B2 D`.
- Class 2: normal first: `L2 U' F2 U2 B2 L2 D'`, then on inverse `(U R2 B2 U B2 D' F2 R2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U' F2 U2 B2 L2 D' R2 F2 D B2 U' B2 R2 U'`.
- Class 3: linear on normal: `R2 U F2 D2 R2 D' B2 U L2 D' L2 F2 U' R2 L2`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `R2 U F2 D2 R2 D' B2 U L2 D' L2 F2 U' R2 L2`.
- Class 4: normal first: `L2 U R2 B2 D2 L2 U F2 U`, then on inverse `(D' B2 R2 U' L2 B2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `L2 U R2 B2 D2 L2 U F2 U B2 L2 U R2 B2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `(U B2 D' F2 D L2 U)`; the reduced state is then solved by `F2 R2 F2 B2 D B2 U2 R2` (8 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 5 moves, `(U B2 D' F2 D)`; the reduced state is then solved by `F2 R2 F2 B2 D B2 U2 R2 U' L2` (10 moves, 2 quarter turns).

</details>

**4b5 4e, example 4.** `F2 D F2 B2 U' B2 U2 F2 B2 U' L2 D' F2 D R2 U R2 D2 R2 B2 D' R2 F2`

Read as 4b5 4e on normal, 4b5 4e on inverse. Shortest HTR: 9 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (21 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 67.0% | yes / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 89.6% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.9% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 94.0% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 94.0% | no / yes |

- Class 1: normal first: `U'`, then on inverse `(U B2 U R2 B2 U B2 D L2 U2 B2 L2 R2)`. HTR after 9 moves (within the budget); the whole finish, as read on normal: `U' R2 L2 B2 U2 L2 D' B2 U' B2 R2 U' B2 U'`.
- Class 2: inverse first: `(U' F2 D)`, then on normal `F2 U' B2 U' F2 L2 D' L2 B2 D2 B2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `F2 U' B2 U' F2 L2 D' L2 B2 D2 B2 D' F2 U`.
- Class 3: linear on normal: `U B2 U R2 U2 B2 U' L2 F2 U L2 F2 U' B2`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 U R2 U2 B2 U' L2 F2 U L2 F2 U' B2`.
- Class 4: normal first: `U B2 U R2 U2 B2 U'`, then on inverse `(B2 U F2 L2 U' F2 L2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 U R2 U2 B2 U' L2 F2 U L2 F2 U' B2`.
- Class 5: normal first: `U`, then on inverse `(B2 U F2 L2 U' F2 L2 U B2 U2 R2 U' B2)`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U B2 U R2 U2 B2 U' L2 F2 U L2 F2 U' B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U B2 U F2 R2 D (U')`; the reduced state is then solved by `B2 U L2 B2 R2 U2 F2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 4 moves, `U B2 U (U')`; the reduced state is then solved by `F2 R2 D B2 U L2 B2 R2 U2 F2` (10 moves, 2 quarter turns).

</details>

**4b5 4e, example 5.** `L2 U2 D' F2 U D' R2 D2 L2 U2 F2 U' L2 B2 R2 L2 D' R2 U R2 U`

Read as 4b5 4e on normal, 4b5 4e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 67.0% | no / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 89.6% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.9% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 94.0% | yes / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 94.0% | no / no |

- Class 1: normal first: `U`, then on inverse `(F2 U' F2 D' R2 D' F2 D2 B2 D R2 F2)`. HTR after 11 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `U F2 R2 D' B2 D2 F2 D R2 D F2 U F2`.
- Class 2: normal first: `U F2 R2 D'`, then on inverse `(F2 U' F2 D' R2 D' F2 D2 B2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U F2 R2 D' B2 D2 F2 D R2 D F2 U F2`.
- Class 3: linear on normal: `U F2 R2 D' B2 D2 F2 D R2 D F2 U F2`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U F2 R2 D' B2 D2 F2 D R2 D F2 U F2`.
- Class 4: inverse first: `(F2 U' F2 D' R2 D')`, then on normal `U F2 R2 D' B2 D2 F2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U F2 R2 D' B2 D2 F2 D R2 D F2 U F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `U (F2 U' F2 D' R2 D')`; the reduced state is then solved by `F2 R2 D' B2 D2 F2` (6 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 5 moves, `U (F2 U' F2 D')`; the reduced state is then solved by `F2 R2 D' B2 D2 F2 D R2` (8 moves, 2 quarter turns).

</details>

**4b5 4e, example 6.** `D' R2 U D2 R2 U' D' B2 U L2 F2 U2 B2 U' R2 D' F2 B2 D' L2 U' B2`

Read as 4b5 4e on normal, 4b5 4e on inverse. Shortest HTR: 10 on normal, 11 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (4 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 67.0% | no / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 89.6% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.9% | yes / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 94.0% | yes / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 94.0% | no / no |

- Class 1: normal first: `D`, then on inverse `(R2 F2 U R2 D' L2 U L2 R2 F2 U' F2 R2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D R2 F2 U F2 R2 L2 U' L2 D R2 U' F2 R2`.
- Class 2: normal first: `D B2 D'`, then on inverse `(B2 D' F2 U R2 F2 U B2 R2 F2 R2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `D B2 D' R2 F2 R2 B2 U' F2 R2 U' F2 D B2`.
- Class 3: linear on the inverse: `(B2 D' B2 D R2 B2 U F2 D' L2 U F2 L2 B2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `B2 L2 F2 U' L2 D F2 U' B2 R2 D' B2 D B2`.
- Class 4: inverse first: `(B2 D' F2 U R2 F2 U)`, then on normal `D B2 D' R2 F2 R2 B2`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `D B2 D' R2 F2 R2 B2 U' F2 R2 U' F2 D B2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `D B2 D' (B2 D' F2 U)`; the reduced state is then solved by `R2 F2 R2 B2 U' F2 R2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 5 moves, `D (B2 D' F2 U)`; the reduced state is then solved by `B2 D' R2 F2 R2 B2 U' F2 R2` (9 moves, 2 quarter turns).

</details>

**4b5 4e, example 7.** `D2 F2 D B2 U2 D2 B2 D' R2 D' R2 U' R2 U' L2 F2 U2 F2 D' R2 F2 D`

Read as 4b5 4e on normal, 4b5 4e on inverse. Shortest HTR: 10 on normal, 10 on inverse, 8 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (6 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 67.0% | no / no |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 89.6% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.9% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 94.0% | yes / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 94.0% | no / yes |

- Class 2: normal first: `U' F2 U`, then on inverse `(U B2 D' L2 R2 F2 U B2 U2 R2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U' F2 U R2 U2 B2 U' F2 R2 L2 D B2 U'`.
- Class 3: linear on normal: `U' F2 U R2 U2 B2 U' F2 R2 L2 D B2 U'`. HTR after 13 moves (5 over the shortest NISS HTR); the whole finish, as read on normal: `U' F2 U R2 U2 B2 U' F2 R2 L2 D B2 U'`.
- Class 4: normal first: `U' F2 U R2 U2 B2 U'`, then on inverse `(U B2 D' L2 R2 F2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `U' F2 U R2 U2 B2 U' F2 R2 L2 D B2 U'`.
- Class 5: normal first: `U'`, then on inverse `(U B2 D' L2 R2 F2 U B2 U2 R2 U' F2)`. HTR after 12 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `U' F2 U R2 U2 B2 U' F2 R2 L2 D B2 U'`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 6 moves, `U' F2 U (U B2 D')`; the reduced state is then solved by `R2 U2 B2 U' F2 R2 L2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 4 moves, `U' (U B2 D')`; the reduced state is then solved by `F2 U R2 U2 B2 U' F2 R2 L2` (9 moves, 2 quarter turns).

</details>

**4b5 4e, example 8.** `D' R2 U R2 L2 F2 U' L2 U D B2 U' F2 U L2 U' L2 B2 D' R2 U' B2 U'`

Read as 4b5 4e on normal, 4b5 4e on inverse. Shortest HTR: 11 on normal, 10 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 13 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 67.0% | yes / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 89.6% | yes / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.9% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 94.0% | yes / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 94.0% | no / no |

- Class 1: normal first: `F2 U'`, then on inverse `(D' R2 B2 U B2 U' F2 R2 U' B2 R2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `F2 U' R2 B2 U R2 F2 U B2 U' B2 R2 D`.
- Class 2: normal first: `F2 U' R2 B2 U`, then on inverse `(D' R2 B2 U B2 U' F2 R2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `F2 U' R2 B2 U R2 F2 U B2 U' B2 R2 D`.
- Class 3: linear on the inverse: `(D' R2 B2 U B2 U' F2 R2 U' B2 R2 U F2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 U' R2 B2 U R2 F2 U B2 U' B2 R2 D`.
- Class 4: inverse first: `(D' R2 B2 U B2 U')`, then on normal `F2 U' R2 B2 U R2 F2`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `F2 U' R2 B2 U R2 F2 U B2 U' B2 R2 D`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 8 moves, `F2 U' (D' R2 B2 U B2 U')`; the reduced state is then solved by `R2 B2 U R2 F2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 4e here) on an optimal path: 6 moves, `(D' R2 B2 U B2 U')`; the reduced state is then solved by `F2 U' R2 B2 U R2 F2` (7 moves, 2 quarter turns).

</details>

**4b5 4e, example 9.** `U2 F2 U' D2 F2 B2 D2 F2 U B2 L2 U2 R2 D R2 B2 U B2 L2 D B2`

Read as 4b5 4e on normal, 4b5 4e on inverse. Shortest HTR: 10 on normal, 11 on inverse, 9 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (2 optimal finishes, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 67.0% | no / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 89.6% | no / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.9% | yes / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 94.0% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 94.0% | no / no |

- Class 1: normal first: `D2 L2 F2 U'`, then on inverse `(F2 D R2 U' L2 D B2 L2 D B2)`. HTR after 13 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `D2 L2 F2 U' B2 D' L2 B2 D' L2 U R2 D' F2`.
- Class 2: normal first: `D2 L2 F2 U' B2 D'`, then on inverse `(F2 D R2 U' L2 D B2 L2)`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D2 L2 F2 U' B2 D' L2 B2 D' L2 U R2 D' F2`.
- Class 3: linear on the inverse: `(F2 D R2 U' L2 D B2 L2 D B2 U F2 L2 D2)`. HTR after 11 moves (within the budget); the whole finish, as read on normal: `D2 L2 F2 U' B2 D' L2 B2 D' L2 U R2 D' F2`.
- Class 4: inverse first: `(F2 D R2 U' L2 D)`, then on normal `D2 L2 F2 U' B2 D' L2 B2`. HTR after 12 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `D2 L2 F2 U' B2 D' L2 B2 D' L2 U R2 D' F2`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 9 moves, `(F2 D R2 U' L2 D B2 L2 D)`; the reduced state is then solved by `D2 L2 F2 U' B2` (5 moves, 1 quarter turn).
- Shortest reduction to 2q (4b2 2e here) on an optimal path: 6 moves, `(F2 D R2 U' L2 D)`; the reduced state is then solved by `D2 L2 F2 U' B2 D' L2 B2` (8 moves, 2 quarter turns).

</details>

**4b5 4e, example 10.** `R2 U L2 U D' R2 U' R2 B2 U' R2 B2 U' L2 B2 U2 F2 U R2 U2 B2`

Read as 4b5 4e on normal, 4b5 4e on inverse. Shortest HTR: 10 on normal, 11 on inverse, 10 with NISS.

<details><summary>Optimal finish, checklist and bounding</summary>

Optimal: 14 moves (1 optimal finish, counting both orders of commuting moves).

| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |
|---:|---|---:|---|
| 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 67.0% | yes / yes |
| 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` | 89.6% | no / yes |
| 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.9% | no / yes |
| 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` | 94.0% | no / yes |
| 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` | 94.0% | no / no |

- Class 1: normal first: `F2 L2 U`, then on inverse `(U' F2 D B2 U' L2 U' B2 R2 U2 R2)`. HTR after 10 moves (within the budget); the whole finish, as read on normal: `F2 L2 U R2 U2 R2 B2 U L2 U B2 D' F2 U`.
- Class 2: normal first: `F2 L2 U R2 U2 R2 B2 U`, then on inverse `(U' F2 D B2 U' L2)`. HTR after 13 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 U R2 U2 R2 B2 U L2 U B2 D' F2 U`.
- Class 3: linear on normal: `F2 L2 U R2 U2 R2 B2 U L2 U B2 D' F2 U`. HTR after 14 moves (4 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 U R2 U2 R2 B2 U L2 U B2 D' F2 U`.
- Class 4: normal first: `F2 L2 U R2 U2 R2 B2 U L2 U`, then on inverse `(U' F2 D B2)`. HTR after 13 moves (3 over the shortest NISS HTR); the whole finish, as read on normal: `F2 L2 U R2 U2 R2 B2 U L2 U B2 D' F2 U`.

- Shortest reduction to 1q (4a1 4e) on an optimal path: 7 moves, `(U' F2 D B2 U' L2 U')`; the reduced state is then solved by `F2 L2 U R2 U2 R2 B2` (7 moves, 1 quarter turn).
- Shortest reduction to 2q (4a2 4e here) on an optimal path: 5 moves, `(U' F2 D B2 U')`; the reduced state is then solved by `F2 L2 U R2 U2 R2 B2 U L2` (9 moves, 2 quarter turns).

</details>
