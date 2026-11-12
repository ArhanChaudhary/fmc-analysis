# DR bounding: errata, and what the full BFS settles

*Goes with the write-up "Judging a DR by hand: what the full BFS says", but reads on its own. The write-up has the measurements and the full tables.*

November 2026. A name with a date is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs and sheets are listed with links at the end.

**What everything below is measured against:**

- **A full BFS of the DR group** ⟨U, D, R2, L2, F2, B2⟩: the optimal DR-move finish of all 19,508,428,800 DR states, done in Rust on the group reduced by the 16 symmetries that keep the U/D axis. "Optimal" below means that (same as nissy's `drudfin`) unless it says otherwise. It matches Joba's per-subset distribution in every cell and nissy on 40 random DRs, and it's the same in every entry as the table Lean has proven optimal (next but one bullet).
- **The 216 NISS@1qt cases** (FakeMMAP's: 12 corner cases × 3 M-slice patterns × 3 S-slice patterns × E-parity, each case being 3,072 of the 663,552 HTR states), solved three ways: half turns only, DR moves, any of the 18 face turns. The first two are a BFS. The third is a search that's complete to 10 moves: every sequence of ≤ 10 moves is two sequences of ≤ 5 glued together, so I listed all 624,124 of those twice, matched the pairs that can land in HTR and tested each hit. DR-move values never go above 10, so anything shorter is ≤ 9 moves and that search can't miss it.
- **One pass per question over all DR states**, for the things people read off a DR (pairs, corner case, HTR length on both sides, corner length, E-parity), each counted against the optimal.
- **A Lean proof** (about 2,500 lines) of the lower bounds in the write-up and of the exact optimal of every DR state: no DR-move finish is shorter than the table says and one of exactly that length exists. "Proven in Lean" below means a theorem in that project. Everything else, including every percentage, is computed.

Case labels like "F-D + F-V R-H odd" are FakeMMAP's: corner case with cs sign, M-slice edges, S-slice edges, E-parity.

Section A is stuff in the two bounding docs and their tables. B is things said in the channels that the full BFS corrects or settles. C is what checked out.

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

The rule values ("Heuristic" column) are *not* affected. They stay at or below the real optimal in all 216 cases, so "the rules give a true lower bound 100% of the time" ([Rodney, 18 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1550363053625708656), [Rodney, 22 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1551960570440319087)) still holds, even against the corrected numbers.

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

**A4. The HT-only table is not a lower bound once other moves are allowed.**
FakeMMAP's own post says so ([FakeMMAP, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546158311945142375)). In numbers: with U and D qts allowed 2 of the 216 values drop (9 to 8, "R-D − F-V R-V even" and its mirror "F-D − F-V R-V even"; the count of 2 is proven in Lean). With all 18 moves 66 drop (35 by 1, 24 by 2, 6 by 3, 1 by 4, counted from the HT-only values). Rodney's "the lower bound still applies if you allow yourself to use DR-breaking moves" ([Rodney, 29 Aug 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1543273729780490411)) is true of Rodney's *rules*, not of the HT-only table they were first compared with. The two that drop with quarter turns:

    L2 B2 D B2 L2 R2 F2 U'      // a state of "R-D − F-V R-V even"
    U F2 R2 L2 B2 D' B2 L2      // solves it in 8

    B2 L2 D L2 B2 F2 R2 U'      // a state of "F-D − F-V R-V even"
    U R2 F2 B2 L2 D' L2 B2      // solves it in 8

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

**B3. FakeMMAP's corner counts per qt** ([FakeMMAP, 26 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1144917908078723112), where FakeMMAP asked someone to check them).
Confirmed: 24, 144, 720, 1416, 1776, 960 of 5040 for 0–5qt.

**B4. The arithmetic in Levi's example** ([tseitsei89, 28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311628919933501460)).
tseitsei89 got 4 + 7 + 3 + 1 = 15 where the doc has 4 + 6 + 2 + 1 = 13. The doc is right: at that 1qt state shortest HTR is 7 on normal and 3 on inverse, each count includes the qt, and the formula counts it once. wen's explanation ([wen, 28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311629216235913226)) is correct.

**B5. The Q in a subset name is not how many qts the finish needs.**
It's the corner qt count, up to turning both layers. So 0c0 0e contains states like `U D'` that need two qts, every 0c0 with bad edges (2e, 4e, 6e, 8e) needs two, and 4a1 0e and 4a1 2e need three. Mallard keeps both numbers (`qt_corners` and `qt` in its source). Stats quoted "by qt" on the server mix the two. The lookup tool I wrote for this prints both. Examples, each the shortest state of its subset, with its optimal finish:

    D F2 R2 F2 D            // 0c0 2e
    D' F2 R2 F2 D'          // two quarter turns

    D F2 U' B2 F2 D'        // 4a1 2e
    D F2 B2 U F2 D'         // three quarter turns

    U L2 R2 U L2 R2 U'      // 4a1 0e
    U R2 L2 U' R2 L2 U'     // three quarter turns

**B6. Two names for one subset.** Mallard and Joba's files say `4c5`, wen's "HTR better smh (v2)" sheet and most people say `4b5`. Same 48 of 420 cosets.

**B7. Arithmetic slip.** [Aneurin, 12 Mar 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1084362354894049340) has 27248 for (4!)⁴/12. It's 27648.

**B8. "HTR subsets are cosets."** The argument from [28 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1355272481208008824) to [31 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1356404254008414209) goes to KrzychXyz: the 48 subsets are double cosets of ⟨half turns, U D⟩ merged with their inverses (that is literally how Mallard builds its table). The 29,400 one-sided cosets are what decides HTR length. Built that way, all 48 sizes match Joba's.

**B9. "Corner case + moves to HTR on normal + moves to HTR on inverse can tell you the optimal solution with a standard deviation of like 0.25 moves"** ([Zagros, 4 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1490097940641878216)).
The sd left is 0.82 moves over all DRs, between 0.74 (4c4) and 0.97 (0c0) by corner subset. The subset alone leaves 0.88. Nothing readable gets under 0.78. A pair, both 2c4 4e with the same corner case on normal and on inverse, 7 to HTR on both sides and the same corner length (7):

    D F2 U' F2 D B2 D'                                 // optimal 7
    D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'      // optimal 16

**B10. "they are all(?) 0c3 or 5q"**, about DRs that are 16+ optimal ([wen, 24 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1364979626279174254)).
41% of the states with a 16+ optimal are in other subsets, and 45 of the 48 subsets contain some (all but 0c0 0e, 0c0 2e and 2c3 2e). They are rare everywhere though: 1.2% of all DR states. Three that are neither:

    F2 D2 B2 R2 U' F2 R2 B2 R2 U' F2 L2 D2 R2 D U'      // 4b2 4e, optimal 16
    R2 U L2 D F2 L2 B2 D2 B2 U' B2 U' R2 F2 R2 U'       // 2c3 4e, optimal 16
    R2 U2 B2 L2 F2 L2 D2 F2 R2 U' B2 F2 L2 R2 U' R2 D'  // 4a1 4e, optimal 17

**B11. trangium's "true 2q bound"** ([trangium, 27 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487207920256024738)): (shortest HTR on one side) + (half turns before the first qt on the other).
It is a bound for finishes with the minimum number of qts, as trangium says. Against the real optimal it is too high for 2.6% of 1–2qt DRs (23.8% of 4a1 4e, 2.2% of 4a2 4e, 1.3% of 4a2 0e, 0.9% of 4b2 4e) and for 0.002% of 3–5qt DRs. Daichi's objection that it's weak ([Daichi, 28 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487653636786880684)) holds: it adds 2 moves to the HTR length at 2qt, about half a move at 3–4qt and nothing at 5qt. Examples where a finish with extra quarter turns gets under it:

    D L2 U' R2 U' L2 F2 U'       // 4b2 4e, the bound says 12
    U F2 L2 U R2 U L2 D'         // solved in 8

    D' F2 R2 U' B2 F2 D          // 4a1 4e, the bound says 15
    D' F2 B2 U R2 F2 D           // solved in 7

    U' L2 D' B2 U' B2 U L2 D     // 4c3 4e (3qt), the bound says 10
    D' L2 U' B2 U B2 D L2 U      // solved in 9

---

## C. What checked out

- Levi's 1qt formula, (HTR normal) + (HTR inverse) − 1, bounds every finish with one quarter turn, which is what Levi's doc uses it for. For reference, a finish with three quarter turns is shorter for 11.7% of 4a1 4e (by 1 in 8.4%, by 2 in 2.7%, by 3+ in 0.6%), and for 2.5% when the formula says 12 or less. One of them, both lines proven in Lean:

  ```
  U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2   // 4a1 4e, formula 6 + 5 − 1 = 10
  U B2 L2 F2 D F2 D                  // solved in 7
  ```

- For 72 of the 432 cases of 4a1 4e the shortest HTR is itself a 3qt one:

  ```
  U L2 R2 U R2 B2 U L2          // 4a1 4e
  U L2 F2 L2 U B2 U             // shortest HTR on normal: 7, three quarter turns
  R2 F2 U2 R2 F2 U2 L2 D        // shortest HTR with one quarter turn: 8
  L2 U' B2 R2 U' R2 L2 U'       // optimal finish: 8
  ```

- Joba's safe lower bound for DR→HTR, "2/1/2/4/6/8 moves for 0/1/2/3/4/5 qt cases" ([Joba, 13 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1349876840914751578)): it holds. The exact floors for 1 to 5 corner qts are 1 / 3 / 5 / 7 / 9, reached on both sides by:

  ```
  D                            // 1qt, HTR 1
  D B2 D'                      // 2qt, HTR 3
  D' B2 D' B2 D'               // 3qt, HTR 5
  D B2 D' B2 D B2 D'           // 4qt, HTR 7
  U' L2 U R2 U' L2 U R2 D      // 5qt, HTR 9
  ```

- Joba's optimal distribution for all 48 subsets over 19,508,428,800 states ([Joba, 17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406633631165714492)): same in every cell.
- 18 as the longest optimal DR finish: now a Lean theorem (nothing needs more, and `U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'` needs 18).
- 1,352 states at 18, the number Reid gave (quoted by [Tomas Rokicki, 31 May 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1510792489236430968)).
- FakeMMAP's 216 HT-only values ([FakeMMAP, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546077758189477989)): same, and now a Lean theorem.
- "blocky 2c4s are way better than not-so-blocky 2c4s" ([Levi, 28 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1366528885432258592)): yes. In 10 / 11 / 12, 0.03% / 0.43% / 4.2% of 2c4 finish with no true pairs and 1.5% / 6.8% / 26% with five or more. About the same ratio holds in every subset.
- Zagros's "4c3 that is 9+ on both sides I throw away" ([Zagros, 10 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1470865840298655918)): that's half of all 4c3, and it keeps 92% of the finishes in 10, 83% of those in 11 and 73% of those in 12 (in 10 / 11 / 12: 0.06% / 0.76% / 6.4% of the tossed half, 0.67% / 3.9% / 18% of the kept half). One it throws away:

  ```
  U' L2 D' B2 U' B2 U L2 D     // 4c3 4e, 9 to HTR on both sides
  D' L2 U' B2 U B2 D L2 U      // its optimal finish: 9
  ```

- "90+% of 4b2 0e cases are 12-14 optimal" ([Daichi, 28 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487653636786880684)): 92.1%.
- Daichi's four kinds of 4b2 corners (2-2 and 3-1, good and bad parity, [Daichi, 8 May 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1502289912693522615)): there are exactly four corner cases in 4b2 and they rank as Daichi lists them at every target: 14% / 11% / 8.4% / 7.0% finishing in 11, 44% / 40% / 33% / 30% in 12.
- Rodney's advanced rules as lower bounds on the 216 cases: valid in all 216, even against DR-breaking optimals.
- Subset sizes, qt class fractions ([Oskar, 10 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1249777335239184405)), and 4a3 ↔ 4b3, 4a4 ↔ 4b4 on inverse (wen's sheet).
- The two worked examples in Rodney's Advanced DR Bounding doc: both 13-movers are optimal. In the 4a4 one you can prove it from the DR alone, by reading Rodney's NISS@1qt features straight off the 4qt DR state instead of off a 1qt state and looking up the fewest moves that fix them (the write-up calls that NISS@DR). It says 13 on the normal side.

---

## Docs and sheets referred to

- Levi Gibson, "DR Bounding": https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA
- Rodney Kinney, "Advanced DR Bounding [Beta]": https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0
- Rodney Kinney, sheet "Adv DR Bounding" (rules vs the 216 computed cases): https://docs.google.com/spreadsheets/d/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY
- FakeMMAP, sheet "OBL++": https://docs.google.com/spreadsheets/d/1kax7evfA85p_4ArXKO7si3FrCpj7PEeFwoz4GY5wRAE
- wen, sheet "HTR better smh (v2)" (the corner subsets): https://docs.google.com/spreadsheets/d/1ZhulzHeNgv2Hiy4x9R1MzsMRlPlI-E8DRiHFJlPlboM
- FakeMMAP's BFS listing, script and tables are attachments on FakeMMAP's posts of 6–10 Sep 2026 in #fmc-theory.
- Mallard (cubelib) source, for how the 48 subsets are built: https://github.com/Jobarion/cubelib
