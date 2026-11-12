# DR bounding: errata

*Goes with the write-up "Judging a DR by hand: what the full BFS says", but reads on its own. The write-up has the measurements and the full tables.*

November 2026. A name with a date is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs and sheets are listed with links at the end.

**What everything below is measured against:**

- **A full BFS of the DR group** ⟨U, D, R2, L2, F2, B2⟩: the optimal DR-move finish of all 19,508,428,800 DR states, done in Rust on the group reduced by the 16 symmetries that keep the U/D axis. "Optimal" below means that (same as nissy's `drudfin`) unless it says otherwise. It matches Joba's per-subset distribution in every cell and nissy on 40 random DRs, and it's the same in every entry as the table Lean has proven optimal (last bullet).
- **The 216 NISS@1qt cases** (FakeMMAP's: 12 corner cases × 3 M-slice patterns × 3 S-slice patterns × E-parity, each case being 3,072 of the 663,552 HTR states), solved three ways: half turns only, DR moves, any of the 18 face turns. The first two are a BFS. The third is a search that's complete to 10 moves: every sequence of ≤ 10 moves is two sequences of ≤ 5 glued together, so I listed all 624,124 of those twice, matched the pairs that can land in HTR and tested each hit. DR-move values never go above 10, so anything shorter is ≤ 9 moves and that search can't miss it.
- **One pass per question over all DR states**, for the things people read off a DR (pairs, corner case, HTR length on both sides, corner length, E-parity), each counted against the optimal.
- **A Lean proof** (about 2,500 lines) of the lower bounds in the write-up and of the exact optimal of every DR state: no DR-move finish is shorter than the table says and one of exactly that length exists. The percentages are computed, not proven.

Case labels like "F-D + F-V R-H odd" are FakeMMAP's: corner case with cs sign, M-slice edges, S-slice edges, E-parity.

Section A is what's wrong in the two bounding docs and their tables, B what's wrong in things said in the channels, each with its example.

---

## A. The bounding docs and their tables

**A1. Two typos in Rodney's Advanced DR Bounding doc.**
- First random scramble: "A 3c2,6e case. Traditionally 3c2 is a good corner case" should be 2c3 (`U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2` is 2c3 6e).
- Strategy section: "note its length, the cr/fr parity" should be cs/fr.

**A2. Rodney's "Adv DR Bounding" sheet: five optimals one too high, and one mislabelled alg.**
The "Penalty" column is the optimal with HTR-breaking finishes allowed. The complete-to-10 search over all 18 moves finds a shorter one for five cases, the same five as in A3:

| Corners / F edges / R edges (cs/fr) | Listed alg | Sheet | Real | A state of the case, and a solution of that length |
|---|---|---:|---:|---|
| F-D / F-V / R-H (0/0) | `R2 U2 R2 F2 R2 U2 R2` | 7 | 6 | `R L' B2 D2 R L'`, solved by `L R' D2 B2 L R'` |
| R-D / F-H / R-V (0/0) | `F2 U2 F2 R2 F2 U2 F2` | 7 | 6 | `F' B R2 D2 F B'`, solved by `B F' D2 R2 B' F` |
| H-H / F-D / R-D (0/1) | `R2 U2 R2 U2 F2 R2 F2 R2 F2` | 9 | 8 | `R D2 F2 B2 R' L F2 R'`, solved by `R F2 L' R B2 F2 D2 R'` |
| H-H / F-D / R-V (0/1) | `F2 U2 R2 F2 U2 R2 F2 R2 F2` | 9 | 8 | `F L2 F B' R2 L2 D2 F'`, solved by `F D2 L2 R2 B F' L2 F'` |
| H-H / F-V / R-D (0/1) | `R2 U2 F2 R2 U2 F2 R2 F2 R2` | 9 | 8 | `L' F2 R L' F2 B2 D2 L`, solved by `L' D2 B2 F2 L R' F2 L` |

Separately, the row labelled F-V / F-D / R-H (0/0) lists `M R2 U2 M'`. That alg gives R-V + F-D R-V odd, not the labelled case. `M F2 U2 M'` gives the labelled case in the 6 moves the sheet says, so R2 is a typo for F2 and the value is fine. (I graded the sheet by the case each alg actually produces, not by its label, which is how this row showed up.)

The rule values ("Heuristic" column) aren't affected: they stay at or below the real optimal in all 216 cases, against the corrected numbers too (write-up, section 10).

**A3. FakeMMAP's HTR-breaking table (`RK_OBL_table_DS_2e.csv`, attached to [FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546599572644696075)): five cells one too high, two of them labelled 7.**
About the first version (`RK_OBL_table_HTR_breaking.csv`, the day before) FakeMMAP said ≤ 7 was proven optimal and 8, 9, 10 "might actually be solvable in as little as 7" ([FakeMMAP, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546263650015256606)). For the 7 Sep file: 211 of 216 cells are right, and the two 7s below are 6 in both files.

| Case | Table | Real | A state of that case (its inverse solves it) |
|---|---:|---:|---|
| F-D + F-V R-H odd | 7 | 6 | `R L' B2 D2 R L'` |
| R-D + F-H R-V odd | 7 | 6 | `F' B R2 D2 F B'` |
| H-H + F-D R-D odd | 9 | 8 | `R D2 F2 B2 R' L F2 R'` |
| H-H + F-V R-D odd | 9 | 8 | `L' F2 R L' F2 B2 D2 L` |
| H-H + F-D R-V odd | 9 | 8 | `F L2 F B' R2 L2 D2 F'` |

In this file nothing is too low and no 8, 9 or 10 drops to 7. (All 216 rows, with HT-only, DR-move and any-move optimals and a sequence for each, are Appendix C of the write-up.)

The later "OBL++" sheet ([FakeMMAP, 10 Nov 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1569733747526598676)), the one FakeMMAP is "not mathematically 100% sure" about ([same day](https://discord.com/channels/1007840975726575667/1007841335434285126/1569733928988704873)), has a finer grid (F/R parity) and I didn't grade it cell by cell. Collapsed to the 216 labels it matches on 140 of the 144 cases it covers, already has four of the five fixes above, and is one *lower* in four (D-D ± F-H R-H even, R-V + F-D R-H even, R-V + F-D R-D odd: 8 vs 9). nissy finds no solution of 8 or fewer for any of the 3,072 states in each of those four cases, so 9 stands for the cases as labelled here. Whether those cells mean something slightly different is open.

---

## B. Things said in the channels

**B1. "The maximum [DR→HTR] takes is 12 moves linearly, and 11 moves using NISS"** ([Lewis Isom, 23 Jan 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1199490255921877022), from the sampled HTR Subset Stats sheet).
It's 13. 15,925,248 DR states need 13 on a given side (0c3 4e, and 4c4 0e from its 4a4 side), and 786,432 states, all in 0c3 4e, need 13 on both sides. Matches Joba's table ([Joba, 3 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1357402650441945299): 4c4 has a 13 in 0.24% of its cosets). Two of them, both 0c3 4e (nissy's optimal HTR agrees on both):

    U' R2 D' B2 U B2 U' R2 U F2 U' F2 U       // 13 to HTR on normal, 12 on inverse
    D B2 D' B2 D L2 U L2 U' F2 D B2 U' F2     // 13 to HTR on both sides

**B2. "Only five subsets can be 18 optimal"** ([Zagros, 17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406635136526581810)), **and "all the 18 optimals … either 5qt or the bad 3qt ones"** ([zakimoshi, 16 Dec 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1185609081629708298)).
It's four of the 48: 0c3 4e (768), 2c5 4e (384), 2c5 0e (192), 0c0 8e (8), 1,352 in total. So "5qt or bad 3qt" misses the eight 0c0 8e states. (Joba's file, which Zagros was reading, shows the same four.) One of each:

    F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'   // 0c3 4e
    R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'  // 2c5 4e
    U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'      // 2c5 0e
    F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'      // 0c0 8e

I can't show a fifth subset because there isn't one: the other 44 top out at 17 or less, and the write-up's Appendix G has a longest state for each.

**B3. Arithmetic slip.** [Aneurin, 12 Mar 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1084362354894049340) has 27248 for (4!)⁴/12. It's 27648.

**B4. "Corner case + moves to HTR on normal + moves to HTR on inverse can tell you the optimal solution with a standard deviation of like 0.25 moves"** ([Zagros, 4 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1490097940641878216)).
The sd left is 0.82 moves over all DRs, between 0.74 (4c4) and 0.97 (0c0) by corner subset. The subset alone leaves 0.88. Nothing readable gets under 0.78. A pair, both 2c4 4e with the same corner case on normal and on inverse, 7 to HTR on both sides and the same corner length (7):

    D F2 U' F2 D B2 D'                                 // optimal 7
    D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'      // optimal 16

**B5. "they are all(?) 0c3 or 5q"**, about DRs that are 16+ optimal ([wen, 24 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1364979626279174254)).
41% of the states with a 16+ optimal are in other subsets, and 45 of the 48 subsets contain some (all but 0c0 0e, 0c0 2e and 2c3 2e). They are rare everywhere though: 1.2% of all DR states. Three that are neither:

    F2 D2 B2 R2 U' F2 R2 B2 R2 U' F2 L2 D2 R2 D U'      // 4b2 4e, optimal 16
    R2 U L2 D F2 L2 B2 D2 B2 U' B2 U' R2 F2 R2 U'       // 2c3 4e, optimal 16
    R2 U2 B2 L2 F2 L2 D2 F2 R2 U' B2 F2 L2 R2 U' R2 D'  // 4a1 4e, optimal 17

---

## Docs and sheets referred to

- Rodney Kinney, "Advanced DR Bounding [Beta]": https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0
- Rodney Kinney, sheet "Adv DR Bounding" (rules vs the 216 computed cases): https://docs.google.com/spreadsheets/d/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY
- FakeMMAP, sheet "OBL++": https://docs.google.com/spreadsheets/d/1kax7evfA85p_4ArXKO7si3FrCpj7PEeFwoz4GY5wRAE
- FakeMMAP's BFS listing, script and tables are attachments on FakeMMAP's posts of 6–10 Sep 2026 in #fmc-theory.
