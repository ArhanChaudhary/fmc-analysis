# DR-xs: corrections, and what the numbers settle

*Goes with the write-up "Is DR-xs worth it?", but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs are listed with links at the end.

**What everything below is measured against:**

- **All 768 kinds of DR-xs state per colour**, with the fewest slices and the fewest face turns to a real DR for each, proved in Lean. Turns are HTM, a slice counts as its two outer turns, and all cancelling is done.
- **Searches over all 2,217,093,120 cosets of the DR group** for the nearest DR, DR-1s and DR-2s 8fe under each move rule. They reproduce the known DR-length counts and the dr-fe distribution trangium posted.
- **200,000 random DR-1s states and 5,000 random DR-2s 8fe states**, each finished as well as the method's form allows (setup, slice or slices, DR finish), using the exact optimal finish of every DR state from the first study.
- **The 500 scrambles** of the first study, with every DR-1s of 8 or less and DR-2s 8fe of 9 or less from a slice EO, each with a written solution that was replayed.

Section A is the docs. B is things said in the channels that the numbers correct. C is what checked out, which is most of it.

---

## A. The docs

**A1. EO Meta Comparison (Rodney): the fix costs it assumes.**
The doc says "we assume 1 slice can be fixed in 3 moves, and 2 slices can be fixed in 5 moves", and its tables are the standard table shifted by those amounts. Counted exactly, from the state alone:

| | Fewest | Most | Average |
|---|---:|---:|---:|
| DR-1s to DR | 2 | 6 | 5.17 |
| DR-2s to DR | 4 | 9 | 6.83 |
| DR-3s to DR | 6 | 10 | 8.50 |

As move counts to a real DR the assumptions are about 2 short. As finish penalties they are close for the DR-1s and too hard on the DR-2s 8fe: a DR-1s finishes 2.27 longer than a DR, a DR-2s 8fe 1.19 longer. So the doc's "-1 slice" rows are about right and slightly pessimistic, and its "off-axis" rows (+2) are pessimistic by about a move for the 8-flipped case.

**A2. Simon's slice-DR doc: the table for step 3.**
"Num Cases out of 70" at 2, 3, 4, 5, 6 moves is given as 1, 4, 9, 40, 16, with "~4.9 moves on average". Taking the better direction of the last trigger move as the doc does, I get 1, 4, 13, 36, 16: thirteen layouts have a 4-turn fix, not nine. The average stays 4.9. The thirteen, with the corners on F/B, the fixing slice `R L` and the last trigger move a quarter turn of U or D:

| Flipped edges at | Turns as it is | Turns with the last move the other way | Fix as it is |
|---|---:|---:|---|
| BL DB UB FR | 4 | 5 | `L2 F R L` |
| BL DB UF BR | 4 | 5 | `D2 B R L` |
| BL DF UF FR | 4 | 5 | `R2 B R L` |
| BL FL BR FR | 4 | 4 | `F B R L` |
| FL DB UB BR | 4 | 5 | `R2 F R L` |
| FL DF UB FR | 4 | 5 | `D2 F R L` |
| FL DF UF BR | 4 | 5 | `L2 B R L` |
| BL DB UB BR | 5 | 4 | `R2 L2 F R L` |
| BL DB UF FR | 5 | 4 | `L2 U2 F R L` |
| BL DF UB FR | 5 | 4 | `L2 D2 F R L` |
| FL DB UF BR | 5 | 4 | `D2 L2 B R L` |
| FL DF UB BR | 5 | 4 | `U2 L2 B R L` |
| FL DF UF FR | 5 | 4 | `U2 D2 F R L` |

Each fix can be checked on a cube: do a DR, do the fix backwards, and the fix brings the DR back.

**A3. The DR-Xs tutorial (tseitsei89), and count quackula's two lists.** Nothing to correct. See C.

---

## B. Said in the channels

**B1. "All edges misoriented (12 bad) -> FB on UD will be extra-good -1s"** (Rodney, [19 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474226073247027220)).
It is a DR-2s, not a DR-1s: four flipped edges, all of one slice, with the centers two slices off. `B' D2 L2 U2 F2 D2 F L2 F2 D2 R2 F2 U' D' L' F' B' U'` has all twelve edges bad on F/B and green or blue on the U and D face of every corner; it has 4 flipped edges, needs 2 slices, and a shortest fix to DR is `U B F L U D` (6 turns).
trangium said he could not get that line to work ([19 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474238124333858836)) and proposed "FB-colored misoriented, others oriented" instead: that one is right, it gives a DR-1s whose four flipped edges belong to one slice. count quackula's 12-bad notes say the same for green/blue: "This is a DR-2s 4fe." The other five lines of Rodney's list are right.

**B2. "I would guess the distribution is basically flat", and 3 moves as the median** for DR-1s to DR (Rodney, [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560294279010717737), [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560296978137485322)).
Of the 70 layouts, 1 needs 2 turns, 2 need 3, 9 need 4, 30 need 5 and 28 need 6. The median is 5. A 6: after `U R2 F2 D' B2 U2 L2 D R' L' B' L2 U2 F2` the shortest fix is 6 turns (`F2 U2 L2 B R L`). Right after a trigger, with the slice free to merge into its last move, the best case is 0 extra turns but most layouts still need 5.

**B3. "closer to 3"** for the moves to fix the flipped edges (Rodney, [23 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1464356830040821947), answering trangium's "~6").
From a DR-1s it is 5.17 on average and from a DR-2s 6.83. trangium's 6 was nearer, and so was sqAree's "more than 5 moves most of the time" ([23 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1464341592952537128)): 83% of DR-1s layouts need 5 or 6.

**B4. "If you have 8 bad edges, where all the good edges belong to the same slice, then you can orient the corners that correspond to the good edges along any axis and you are guaranteed an extra-good dr-xs"** (Rodney, [20 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474455821978042472)).
True for two of the three pairs of faces. With the corners on the faces of the EO axis itself it is a DR-1s, but how its four flipped edges split between slices is not fixed: 2-2 about half the time, 3-1 nearly half, 4-0 rarely. `U D2 L2 D B2 L2 B2 D R2 F2 U' R' L F' B'` has 8 bad edges on F/B with the four good ones the E-slice edges, white/yellow corners oriented on F and B, and a 3-1 split.

---

## C. What checked out

- **The rule for the number of slices** from centers and flipped edges (trangium's dr-fe examples doc; Rodney [22 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1464027237656563783); FakeMMAP [25 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1464948138707255550); the tutorial): right for all 768 kinds.
- **"dr-1s to dr is like 6 moves max?"**, "i don't think 7 optimal exists" (Daichi, [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560144143441854566), [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560145175714472097)): exactly right.
- **"DR-2s needs at most 2 moves to reach DR-1s"** (Rodney, [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560294279010717737)): right, counting the setup before the slice.
- **From DR-3s, DR-2s in 0 moves** with a slice that cancels with the last DR move (the tutorial): right for every DR-3s.
- **trangium's averages** in the tutorial: DR-1s +2.2 to +2.4 over a DR, DR-2s 8fe +0.85 to +1.14. Mine, with the best finish of the method's form: +2.27 and +1.19 overall.
- **"8 move DR-1s is on average better than an 11 move DR but worse than 10 move DR"** (the tutorial): right, in odds too.
- **4-0 great, 2-2 good, 3-1 bad** (Rodney [28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1466198780582826057), tseitsei89): the order is right; the gap from 2-2 to 3-1 is a quarter of a move.
- **Slice EO "is never more than 2 moves away"**, "No matter which slice you pick" (FakeMMAP, [25 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1465100277303476304), [25 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1465100381318025409)); "partial EO in <=2 is guaranteed" (EO Meta Comparison): exact.
- **One in 2^3 for a slice and an axis** (tseitsei89 [3 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1533722203646988318), count quackula [3 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1533721112813244467)): right. At least one skip on a scramble: 68.7953% on normal, 79.3147% with inverse.
- **A misoriented slice EO needs an axis with 8 bad edges** to give a DR-1s (tseitsei89 [3 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1468124565681999932), trangium [8 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1480310254129516617)): right, and misoriented on the slice's own axis never does.
- **"The chance of getting 4 flipped edges in general is 55%"** (Rodney, [1 May 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1499635961015963751)): 70 in 128.
- **The optimal linear dr-fe distribution** 1, 4, 50, 586, 6800, 72894, 659610, 3479477, 4193028, 247986, 84 (trangium, [2 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1478068304819261513)): reproduced exactly.
- **count quackula's 12-bad notes and guaranteed-fix list**: every case is the kind the pattern table gives.
- **The tutorial's first example** (FMCL S9W3A2): its skips, its DR-2s, its 4a2-1s and its 19 all come out the same, and 19 is the best its DR-1s allows in that form.

---

## Docs referred to

- tseitsei89 (Janne Lehtimäki), [DR-Xs](https://docs.google.com/document/d/1_uLVLB5xqDm40NugXE5rjc8LgEtuHQCLz0odKY6mboE), 2 Feb 2026.
- Rodney Kinney, [EO Meta Comparison](https://docs.google.com/document/d/131VWYrL3Z4t6p0fBGkHZ73w6arF8A7PEqRuNjsIQMGo), Jan 2026.
- Simon, [Slice DR](https://docs.google.com/document/d/15zDJ9_FQIYVgHLbt1eHdOPtEp10jFOOae_U8DTaH7tk), Jul 2025.
- trangium, [dr-fe examples](https://docs.google.com/document/d/11Xu6BpEBLu-v8hVbFzneSqeMjHb83q_zurWb_V0DXDY), 19 Jan 2026.
- count quackula, [12 bad dr-xs notes](https://docs.google.com/document/d/1-anqtLsBGg_oBvzz1TTf_6Mjsypv4jMkFhB9E8cwkQM) and [guaranteed-fix cases](https://docs.google.com/document/d/190aVmEQFLILHGhrtuf1YFai0SYrsu_tWRYAWOe62P6U), Feb 2026.
