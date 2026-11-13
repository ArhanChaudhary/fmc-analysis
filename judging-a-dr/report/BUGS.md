# DR bounding: errata

*Goes with the write-up "Judging a DR by hand: what the full BFS says", but reads on its own. The write-up has the measurements and the full tables.*

November 2026. A name with a date is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs and sheets are listed with links at the end.

**What everything below is measured against:**

- **A full BFS of the DR group** ⟨U, D, R2, L2, F2, B2⟩: the optimal finish in DR moves of all 19,508,428,800 DR states. I ran it in Rust, on the group reduced by the 16 symmetries that keep the U/D axis. "Optimal" below means that (same as nissy's `drudfin`) unless I say otherwise. It matches Joba's per-subset distribution in every cell and nissy on 40 random DRs, and it agrees entry for entry with the table Lean proves optimal (last bullet).
- **The 216 NISS@1qt cases** (FakeMMAP's: 12 corner cases $\times$ 3 M-slice patterns $\times$ 3 S-slice patterns $\times$ E-parity). Each case is 3,072 of the 663,552 HTR states. I solved them three ways, see the table below: one row per move set.
- **The shortest HTR of every DR state**, on normal and on inverse, from one pass over all of them.
- **A Lean proof** (about 2,500 lines) of the lower bounds in the write-up and of the exact optimal of every DR state: no DR-move finish is shorter than the table says, and one of exactly that length exists. The percentages are computed, not proven.

| The cases, solved with | How |
|---|---|
| half turns only | BFS |
| DR moves | BFS |
| any of the 18 face turns | A search that's complete to 10 moves. Every sequence of $\le 10$ moves is two sequences of $\le 5$ glued together, so I listed all 624,124 of those twice, matched the pairs that can land in HTR and tested each hit. DR-move values never go above 10, so anything shorter is $\le 9$ moves and the search can't miss it. |

Case labels like "F-D + F-V R-H odd" are FakeMMAP's: corner case with cs sign, M-slice edges, S-slice edges, E-parity.

What the entries are measured against is **computer only**, the answer key, not something to do in an attempt. What you can use by hand (the reads, the drop rules, the guide per subset) is in the write-up.

Section A is what's wrong in Rodney's bounding doc and sheet and in FakeMMAP's table. Section B is three slips in the channels: a maximum, a count and a typo. Each entry has an example.

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
The tab is called "Optimals (Advanced)" and Rodney's doc says the sheet holds "optimal algorithms for all 216" cases, so a listed alg that isn't optimal is an erratum there. The sheet has no optimal column. Its "Penalty" is the length of the listed alg (HTM, after cancelling) minus the setup of the corner case itself. Each row is a corner case and the setup the sheet takes off:

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

That's the sheet's penalty of 4 after the 2-move F-V corner setup, so the penalty is fine. The same line is in FakeMMAP's 7 Sep listing, where the sheet's algs come from (`F-V + F-D R-H  odd E-parity: 6 Example scramble: M R2 U2 M'`, in the attachment of [FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546566724189421781)). The 6 there is the length of the F2 version.

The rule values ("Heuristic" column, same penalty scale) aren't affected. They stay at or below the real penalty in all 216 cases, the corrected ones too: 4 against 5 in the first two rows, 5 against 8 in the three H-H rows (write-up, section 10).

**A3. FakeMMAP's HTR-breaking table (`RK_OBL_table_DS_2e.csv`, attached to [FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546599572644696075)): two cells labelled 7 are 6.**
FakeMMAP's own grading of these tables, with the first version (`RK_OBL_table_HTR_breaking.csv`): "Anything labeled with 7 or less is proven to be a lower bound, and the lower bound is proven optimal. Anything labeled 8, 9 or 10 might actually be solvable in as little as 7 moves if we allow for HTR-breaking" ([FakeMMAP, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546263650015256606)). And for the 7 Sep values: "Again, anything higher than 7 is not proven, those cases could be 7-movers" ([FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546567276571005048)). The first half fails for the two 7s below. The rest is inside the caveat and comes out better than it allowed: three of the unproven 9s are 8, and no 8, 9 or 10 drops to 7. The other 211 cells are exact, and nothing is too low.

A case covers 3,072 states and its value is the shortest finish over all of them, which is what a lower bound needs; the shorter value is reached by only some of the case's states (between 16 and 136 of them). Each row of the two tables is a cell, with the table's value, the real optimal and a state of the case (its inverse solves it).

The two cells labelled 7:

| Case | Table value, moves | Real optimal, moves | A state of that case |
|---|---:|---:|---|
| F-D + F-V R-H odd | 7 | 6 | `R L' B2 D2 R L'` |
| R-D + F-H R-V odd | 7 | 6 | `F' B R2 D2 F B'` |

The three 9s, among the cells FakeMMAP left unproven:

| Case | Table value, moves | Real optimal, moves | A state of that case |
|---|---:|---:|---|
| H-H + F-D R-D odd | 9 | 8 | `R D2 F2 B2 R' L F2 R'` |
| H-H + F-V R-D odd | 9 | 8 | `L' F2 R L' F2 B2 D2 L` |
| H-H + F-D R-V odd | 9 | 8 | `F L2 F B' R2 L2 D2 F'` |

The 6 Sep file has the same two 7s, and six more cells labelled 7 or less that are off by one: four one too high (D-D + F-H R-V even and D-D − F-V R-H even say 7, R-D + F-H R-H odd and F-D + F-H R-H odd say 6), and two one too low (R-V + F-H R-H odd and F-V + F-H R-H odd say 5, and both are 6). The 7 Sep file fixes those six. All 216 rows, with HT-only, DR-move and any-move optimals and a state and an optimal solution for each, are Appendix C of the write-up.

The later "OBL++" sheet ([FakeMMAP, 10 Nov 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1569733747526598676)) has a finer grid (F/R parity), and I didn't grade it cell by cell. FakeMMAP on what's in it: "They do include some HTR-breaking stuff." ([same day](https://discord.com/channels/1007840975726575667/1007841335434285126/1569733844528140384)) "Maybe all." "But I'm not mathematically 100% sure." ([same day](https://discord.com/channels/1007840975726575667/1007841335434285126/1569733928988704873)). Collapsed to the 216 labels it covers 144 cases and matches on 140. It already has four of the five fixes above, and it's one *lower* in four cases, 8 vs 9:

- D-D ± F-H R-H even (two cases)
- R-V + F-D R-H even
- R-V + F-D R-D odd

nissy finds no solution of 8 or fewer for any of the 3,072 states in each of those four cases, so 9 stands for the cases as labelled here. Whether those cells mean something slightly different is open.

---

## B. Things said in the channels

**B1. "No, the maximum it takes is 12 moves linearly, and 11 moves using NISS. See HTR subset stats under fmc-stats for more info."** ([Lewis Isom, 23 Jan 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1199490255921877022), on whether DR→HTR ever takes more than 9.)
Linearly it's 13 and no more (✓ Lean). The sheet Lewis points to, Aedan Bryant's sampled HTR Subset Stats, has it: its 3qt 4E column shows 13 for 7.6% of its sample. Exactly, it's 7.4% of the cosets of 0c3 4e and 0.24% of those of 4c4 ([Joba, 3 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1357402650441945299)), and Daichi had the full statement: "0c3 4e and 4c4 0e can be 13 optimal, which is the longest optimal HTR, is what I have on me" ([Daichi, 27 Jan 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1465829493745914054)).

The 11 with NISS is the largest value in the sheet's samples. The real maximum is at least 12 (the third state below). Five minutes after the first message Lewis had "found a mistake in the spreadsheet", a 6-move NISS HTR for a 5qt subset, "so the htr subsets doc could potentially be wrong about other info too" ([Lewis Isom, same day](https://discord.com/channels/1007840975726575667/1007841335434285126/1199491681465155675)).

Each row is how often a DR needs 13 to HTR linearly:

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

**B2. "Interesting how only five subsets can be 18 optimal, and one of them is 0c0 8e"** ([Zagros, 17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406635136526581810), six minutes after [Joba's per-subset counts](https://discord.com/channels/1007840975726575667/1007841335434285126/1406633631165714492)).
A count slip: it's four of the 48, in Joba's file and in the full BFS, 1,352 states in total. 0c0 8e is one of them, as Zagros says. Tomas Rokicki's list of the distance-18 positions, which zakimoshi had found and linked in 2023 ([zakimoshi, 4 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1148298741523161120)), has the same four subsets. One subset per row:

| Subset | States |
|---|---:|
| 0c3 4e | 768 |
| 2c5 4e | 384 |
| 2c5 0e | 192 |
| 0c0 8e | 8 |

One of each (✓ Lean: subset and optimal 18):

    F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'   // 0c3 4e
    R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'  // 2c5 4e
    U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'      // 2c5 0e
    F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'      // 0c0 8e

I can't show a fifth subset because there isn't one: the other 44 top out at 17 or less, and the write-up's Appendix G has a longest state for each.

**B3. A typo.** [Aneurin, 12 Mar 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1084362354894049340) has "27248 htr scrambles ignoring the E slice" for $(4!)^4/12$. The formula is right and the number is 27,648 (✓ Lean). Aneurin's next message was "Unless I made a mistake." ([a minute later](https://discord.com/channels/1007840975726575667/1007841335434285126/1084362390356897822)).

---

## Docs and sheets referred to

- Rodney Kinney, "Advanced DR Bounding [Beta]": https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0
- Rodney Kinney, sheet "Adv DR Bounding" (rules vs the 216 computed cases): https://docs.google.com/spreadsheets/d/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY
- FakeMMAP, sheet "OBL++": https://docs.google.com/spreadsheets/d/1kax7evfA85p_4ArXKO7si3FrCpj7PEeFwoz4GY5wRAE
- Aedan Bryant, sheet "HTR Subset Stats" (sampled): https://docs.google.com/spreadsheets/d/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0
- FakeMMAP's BFS listing, script and tables are attachments on FakeMMAP's posts of 6–10 Sep 2026 in #fmc-theory.
