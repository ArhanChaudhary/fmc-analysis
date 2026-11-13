# DR bounding: errata

*Goes with the write-up "Judging a DR by hand: what the full BFS says", but reads on its own. The write-up has the measurements and the full tables.*

November 2026. A name with a date is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs and sheets are listed with links at the end.

**What everything below is measured against:**

- **A full BFS of the DR group** ⟨U, D, R2, L2, F2, B2⟩: the optimal finish in DR moves of all 19,508,428,800 DR states. I ran it in Rust, on the group reduced by the 16 symmetries that keep the U/D axis. "Optimal" below means that (same as nissy's `drudfin`) unless I say otherwise. It matches Joba's per-subset distribution in every cell and nissy on 40 random DRs, and it agrees entry for entry with the table Lean proves optimal (last bullet).
- **The 216 NISS@1qt cases** (FakeMMAP's: 12 corner cases $\times$ 3 M-slice patterns $\times$ 3 S-slice patterns $\times$ E-parity). Each case is 3,072 of the 663,552 HTR states. I solved them three ways, see the table below: one row per move set.
- **One pass per question over all DR states** for each thing people read off a DR (pairs, corner case, HTR length on both sides, corner length, E-parity), counted against the optimal.
- **A Lean proof** (about 2,500 lines) of the lower bounds in the write-up and of the exact optimal of every DR state: no DR-move finish is shorter than the table says, and one of exactly that length exists. The percentages are computed, not proven.

| The cases, solved with | How |
|---|---|
| half turns only | BFS |
| DR moves | BFS |
| any of the 18 face turns | A search that's complete to 10 moves. Every sequence of $\le 10$ moves is two sequences of $\le 5$ glued together, so I listed all 624,124 of those twice, matched the pairs that can land in HTR and tested each hit. DR-move values never go above 10, so anything shorter is $\le 9$ moves and the search can't miss it. |

Case labels like "F-D + F-V R-H odd" are FakeMMAP's: corner case with cs sign, M-slice edges, S-slice edges, E-parity.

What the entries are measured against is **computer only**, the answer key, not something to do in an attempt. What you can use by hand (the reads, the drop rules, the guide per subset) is in the write-up.

Section A is what's wrong in Rodney's bounding doc and sheet and in FakeMMAP's table, section B what's wrong in things said in the channels. Each entry has an example.

---

## A. The bounding docs and their tables

**A1. Two typos in Rodney's Advanced DR Bounding doc.** One per row:

| Where | The doc says | Should be |
|---|---|---|
| First random scramble | "A 3c2,6e case. Traditionally 3c2 is a good corner case" | 2c3 |
| Strategy section | "note its length, the cr/fr parity" | cs/fr |

The first random scramble is 2c3 6e (✓ Lean):

```
U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2   // Rodney's first random scramble
```

**A2. Rodney's "Adv DR Bounding" sheet: five penalties one too high, and one mislabelled alg.**
The sheet has no optimal column. Its "Penalty" is the length of the listed alg (HTM, after cancelling) minus the setup of the corner case itself. Each row is a corner case and the setup the sheet takes off:

| Corners | Setup taken off, moves |
|---|---:|
| F-D and R-D | 1 |
| F-V | 2 |
| H-H | 0 |

The complete-to-10 search over all 18 moves finds a finish one move shorter than the listed alg for five cases, the same five as in A3. Their penalties should be 5, 5, 8, 8, 8, not 6, 6, 9, 9, 9.

Each row is a case (corners, F edges, R edges, with the sheet's cs and fr labels), its listed alg, and the two penalties:

| Case | cs | fr | Listed alg | Alg length, moves | Sheet penalty | Real penalty |
|---|---:|---:|---|---:|---:|---:|
| F-D, F-V, R-H | 0 | 0 | `R2 U2 R2 F2 R2 U2 R2` | 7 | 6 | 5 |
| R-D, F-H, R-V | 0 | 0 | `F2 U2 F2 R2 F2 U2 F2` | 7 | 6 | 5 |
| H-H, F-D, R-D | 0 | 1 | `R2 U2 R2 U2 F2 R2 F2 R2 F2` | 9 | 9 | 8 |
| H-H, F-D, R-V | 0 | 1 | `F2 U2 R2 F2 U2 R2 F2 R2 F2` | 9 | 9 | 8 |
| H-H, F-V, R-D | 0 | 1 | `R2 U2 F2 R2 U2 F2 R2 F2 R2` | 9 | 9 | 8 |

A state of each case and a shorter finish for it (✓ Lean: each finish solves its state in the length given):

| Case | A state of the case | Shorter finish | Its length, moves |
|---|---|---|---:|
| F-D, F-V, R-H | `R L' B2 D2 R L'` | `L R' D2 B2 L R'` | 6 |
| R-D, F-H, R-V | `F' B R2 D2 F B'` | `B F' D2 R2 B' F` | 6 |
| H-H, F-D, R-D | `R D2 F2 B2 R' L F2 R'` | `R F2 L' R B2 F2 D2 R'` | 8 |
| H-H, F-D, R-V | `F L2 F B' R2 L2 D2 F'` | `F D2 L2 R2 B F' L2 F'` | 8 |
| H-H, F-V, R-D | `L' F2 R L' F2 B2 D2 L` | `L' D2 B2 F2 L R' F2 L` | 8 |

Separately, the alg in the row labelled F-V / F-D / R-H (0/0) has R2 where it should have F2. I graded every row by the case its alg actually produces, not by its label:

```
M R2 U2 M'   // listed: gives R-V + F-D R-V odd, not the labelled case
M F2 U2 M'   // gives the labelled case in 6 moves
```

That's the sheet's penalty of 4 after the 2-move F-V corner setup, so the penalty is fine.

The rule values ("Heuristic" column, same penalty scale) aren't affected. They stay at or below the real penalty in all 216 cases, the corrected ones too: 4 against 5 in the first two rows, 5 against 8 in the three H-H rows (write-up, section 10).

**A3. FakeMMAP's HTR-breaking table (`RK_OBL_table_DS_2e.csv`, attached to [FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546599572644696075)): five cells one too high, two of them labelled 7.**
Of the first version (`RK_OBL_table_HTR_breaking.csv`, posted the day before) FakeMMAP said ≤ 7 was proven optimal and 8, 9, 10 "might actually be solvable in as little as 7" ([FakeMMAP, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546263650015256606)). In the 7 Sep file 211 of 216 cells are right. The two 7s below are 6 in both files. The 6 Sep file has eight cells labelled 7 or less that are off by one: those two 7s, four more one too high (D-D + F-H R-V even and D-D − F-V R-H even say 7, R-D + F-H R-H odd and F-D + F-H R-H odd say 6), and two one too low (R-V + F-H R-H odd and F-V + F-H R-H odd say 5, and both are 6). The 7 Sep file fixes those six. Appendix C of the write-up has a state and an optimal solution for each.

Each row is one of the five cells, with the table's value, the real optimal and a state of the case (its inverse solves it):

| Case | Table value, moves | Real optimal, moves | A state of that case |
|---|---:|---:|---|
| F-D + F-V R-H odd | 7 | 6 | `R L' B2 D2 R L'` |
| R-D + F-H R-V odd | 7 | 6 | `F' B R2 D2 F B'` |
| H-H + F-D R-D odd | 9 | 8 | `R D2 F2 B2 R' L F2 R'` |
| H-H + F-V R-D odd | 9 | 8 | `L' F2 R L' F2 B2 D2 L` |
| H-H + F-D R-V odd | 9 | 8 | `F L2 F B' R2 L2 D2 F'` |

In this file nothing is too low and no 8, 9 or 10 drops to 7. (All 216 rows, with HT-only, DR-move and any-move optimals and a sequence for each, are Appendix C of the write-up.)

The later "OBL++" sheet ([FakeMMAP, 10 Nov 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1569733747526598676)), the one FakeMMAP is "not mathematically 100% sure" about ([same day](https://discord.com/channels/1007840975726575667/1007841335434285126/1569733928988704873)), has a finer grid (F/R parity), and I didn't grade it cell by cell. Collapsed to the 216 labels it covers 144 cases and matches on 140. It already has four of the five fixes above, and it's one *lower* in four cases, 8 vs 9:

- D-D ± F-H R-H even (two cases)
- R-V + F-D R-H even
- R-V + F-D R-D odd

nissy finds no solution of 8 or fewer for any of the 3,072 states in each of those four cases, so 9 stands for the cases as labelled here. Whether those cells mean something slightly different is open.

---

## B. Things said in the channels

**B1. "The maximum [DR→HTR] takes is 12 moves linearly, and 11 moves using NISS"** ([Lewis Isom, 23 Jan 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1199490255921877022), from the sampled HTR Subset Stats sheet).
Linearly it's 13 and no more (✓ Lean), which matches Joba's table ([Joba, 3 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1357402650441945299): 4c4 has a 13 in 0.24% of its cosets). With NISS it's at least 12 (the third state below). Each row is how often a DR needs 13 to HTR linearly:

| DR → HTR needs | DR states | Subsets |
|---|---:|---|
| 13 on a given side | 15,925,248 | 0c3 4e, and 4c4 0e from its 4a4 side |
| 13 on both sides | 786,432 | all 0c3 4e |

Two of them, both 0c3 4e (nissy's optimal HTR agrees on both; ✓ Lean):

    U' R2 D' B2 U B2 U' R2 U F2 U' F2 U       // 13 to HTR on normal, 12 on inverse
    D B2 D' B2 D L2 U L2 U' F2 D B2 U' F2     // 13 to HTR on both sides

Both of those have a NISS HTR of 11. This 0c3 4e, also 13 on both sides, has none: its shortest with NISS is 12.

    B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U
    U R2 U2 F2 U' F2 R2 U (B2 U L2 U)             // 12 to HTR, the bracket on inverse

✓ Lean for the 12 and for the two 11s, with one step argued by hand: a NISS HTR of 11 or less has five moves or fewer on one of its two sides, and Lean tries every such side.

**B2. "Only five subsets can be 18 optimal"** ([Zagros, 17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406635136526581810)), **and "We calculated all the 18 optimals once I remember it being either 5qt or the bad 3qt ons"** ([zakimoshi, 16 Dec 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1185609081629708298)).
It's four of the 48, 1,352 states in total, one subset per row:

| Subset | States |
|---|---:|
| 0c3 4e | 768 |
| 2c5 4e | 384 |
| 2c5 0e | 192 |
| 0c0 8e | 8 |

So "5qt or bad 3qt" misses the eight 0c0 8e states. Joba's file, which Zagros was reading, shows the same four. One of each (✓ Lean: subset and optimal 18):

    F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'   // 0c3 4e
    R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'  // 2c5 4e
    U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'      // 2c5 0e
    F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'      // 0c0 8e

I can't show a fifth subset because there isn't one: the other 44 top out at 17 or less, and the write-up's Appendix G has a longest state for each.

**B3. Arithmetic slip.** [Aneurin, 12 Mar 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1084362354894049340) has 27248 for $(4!)^4/12$. It's 27648 (✓ Lean).

**B4. "I hypothesize that corner case + moves to HTR on normal + moves to HTR on inverse can tell you the optimal solution with a standard deviation of like 0.25 moves"** ([Zagros, 4 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1490097940641878216)).
It's nowhere near that. The sd of the optimal over all DRs, given what you know, one set of reads per row (**computer only**, a measure of the reads over every DR state):

| Known | Scatter left, sd in moves |
|---|---:|
| the subset alone | 0.88 |
| subset (with the bad-edge count), corner case on both sides, HTR length on both sides | 0.80 |
| every read together: subset, pairs, corner case and HTR length on both sides, corner length and E-parity | 0.77 |

Zagros didn't list the bad-edge count. Without it, the corner case and HTR length on both sides leave 0.80 as well. Here's a pair, both 2c4 4e with the same corner case on normal and on inverse, 7 to HTR on both sides and the same corner length (7) (✓ Lean, all but the corner case):

    D F2 U' F2 D B2 D'                                 // optimal 7
    D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'      // optimal 16

**B5. "they are all(?) 0c3 or 5q"**, about DRs that are 16+ optimal ([wen, 24 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1364979626279174254)).
41% of the states with a 16+ optimal are in other subsets. 45 of the 48 subsets have some, all but 0c0 0e, 0c0 2e and 2c3 2e. They're rare everywhere though: 1.2% of all DR states. Three that are neither (✓ Lean: subset and optimal):

    F2 D2 B2 R2 U' F2 R2 B2 R2 U' F2 L2 D2 R2 D U'      // 4b2 4e, optimal 16
    R2 U L2 D F2 L2 B2 D2 B2 U' B2 U' R2 F2 R2 U'       // 2c3 4e, optimal 16
    R2 U2 B2 L2 F2 L2 D2 F2 R2 U' B2 F2 L2 R2 U' R2 D'  // 4a1 4e, optimal 17

---

## Docs and sheets referred to

- Rodney Kinney, "Advanced DR Bounding [Beta]": https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0
- Rodney Kinney, sheet "Adv DR Bounding" (rules vs the 216 computed cases): https://docs.google.com/spreadsheets/d/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY
- FakeMMAP, sheet "OBL++": https://docs.google.com/spreadsheets/d/1kax7evfA85p_4ArXKO7si3FrCpj7PEeFwoz4GY5wRAE
- Aedan Bryant, sheet "HTR Subset Stats" (sampled): https://docs.google.com/spreadsheets/d/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0
- FakeMMAP's BFS listing, script and tables are attachments on FakeMMAP's posts of 6–10 Sep 2026 in #fmc-theory.
