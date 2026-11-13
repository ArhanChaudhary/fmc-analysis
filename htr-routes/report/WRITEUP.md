# Which HTR routes to try from a DR

You have a DR: which routes to HTR do you try, and in what order, to find the optimal finish? For each of the 48 subsets I sampled 25,000 uniformly random DR states (subset × bad edges, so 1,200,000 in all) and solved each one exactly: every optimal finish and every finish one move longer, read in every way NISS allows (switch after any move, either side first), and the same for the DR with its last move turned the other way. From that come ordered checklists of routes per subset, how long the HTRs on them are, how DR bounding compares, and whether FakeMMAP's reduction-length bound holds and prunes.

Every finish length comes from the first study's exact table of all 19,508,428,800 DR states. Where a number is exact over all states it says so; otherwise it's a sample of 25,000 states per subset × edges (a share's standard error is at most 0.3 points per subset × edges, 0.2 per corner subset) unless a smaller sample is named.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion). Docs and sheets are listed with links at the end.

**This builds on** what the server already had:

- **Daichi's cheat sheet** ([12 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515146431542067290): "to summarize, I think this is meta"), a route list per subset ("It doesn't capture EVERYTHING, but I decided that checking these will capture a great portion of those", [12 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515177158870569101)). It is graded in section 10.
- **Levi Gibson's sheets and doc** (beef beans on Discord, posted as levitatingmagician): [*allcases*](https://docs.google.com/spreadsheets/d/1Vo6XzCFtJ-HEAuaBmk_pac-sJ3TbxEBb7BKsRJ_2wpA) ("What paths are most common for optimal DR solutions", [13 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1295051854635597856)), the [*Extra Quarter-Turn Stats (By HTR Subset)*](https://docs.google.com/spreadsheets/d/1fPCjS1ZQlP_Munut9MQkSbsL3CEdtT3LC5h3R8OMHGw) ([25 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1144726792217825370)), and [*DR Bounding*](https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA) ([27 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311464464737898589)), the method section 8 measures.
- **Aedan Bryant's [*HTR Subset Stats*](https://docs.google.com/spreadsheets/d/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0)** ([30 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069557424949833759)): 1,000 states per subset, mean optimal against shortest linear and NISS HTR.
- **Joba's exact optimal distribution per subset** ([17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406633631165714492): "This is not sampled, I looked at all 19508428800 DR states"), which the first study and this one reproduce cell for cell, and **DougCube's** [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo) ([2 Mar 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1345852930544369684)) with the finish of all 663,552 HTR states ("the *expected value* is 10.13", [13 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1416567970334773378)), also reproduced exactly.
- **rodneykinney's** [*DR Finish Move Counts*](https://docs.google.com/spreadsheets/d/1tv8rwo2GF9IWuywFTnde_YlikIPBQvHqW9pysNG6BPM) ([2 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1037387616313675806)), the corner-skeleton *normal forms* ([12 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1460293921883164881)) and [*Advanced DR Bounding [Beta]*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0) ([29 Aug 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1543125354120609832)).
- **FakeMMAP's** reduction-length bound and multi-qt lower bounds ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531394667773962), [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369), [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475)), with FakeMMAP's own caveat on the lower bounds, "I don't know how useful these bounds really are, I have to put in the numbers to see if there are situations where the typical bound is M \geq 11, rather than M \geq 7 lol." ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533429198553178)), and rodneykinney's request for per-case tables ([9 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491873063531188324)). Section 9 is that test.
- **JTuu's** 2c3 2e simulation of linear HTRs against bounding ([4 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313766061325156462)), **Zagros's** eight-step 4b2 order ([29 Dec 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1455301984415514719)), **Lewis Isom's** 4a2 list ([11 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1360414689019957449)) and 2c3 extension list ([18 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1373798214326554758)), Yura Riabov's 4b2 4e order and rogo's question about it ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258421085251178608), [4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258442750953525399)), and Jay's and rodneykinney's 3qt checks ([16 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1042617188370087988), [17 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1042817953072152596)).
- **My own first study** ([*Judging a DR by hand*](../judging-a-dr/)): the exact optimal finish of every DR state, the subset names, and *a third of the time the other DR is one shorter* for the last DR move.

**What this adds**:

- **A checklist per subset × edges**: the routes to try in order, each with the share of DRs where the routes so far find the optimal and a finish within +1, with and without a limit on how long the HTR may be; how much knowing the edge count changes it, and which edge count the optimal passes on the way (4b2 2e or 4b2 4e).
- **HTR lengths against the optimal**: linear against NISS HTR (rodneykinney's question from 2023), how often the optimal uses a shortest HTR, how often it needs 9 moves or more.
- **DR bounding measured**: per subset, how often checking every reduction to 1q (or 2q) of up to R moves finds the optimal, and how many reductions that is.
- **FakeMMAP's bound tested**: whether it is ever too short, how much it prunes, rodneykinney's per-subset tables, and a correction to the multi-qt lower bound.
- **Hand checklists graded** (Zagros, Yura Riabov's 4b2 4e order against reducing to 1q first, Lewis Isom, Daichi's cheat sheet), and **the claims checked**.

**Terms**, as the server uses them. Subsets are the first study's (Mallard's): 0c0, 4a1, 4a2, 4b2, 0c3, 2c3, 4c3, 0c4, 2c4, 4c4, 2c5, 4b5, each with its bad-edge count (4b2 4e). 4c3 is 4a3 on one side and 4b3 on the other, 4c4 is 4a4/4b4; routes name the side's own letter. Older names: Jay's qt names in Aedan Bryant's sheet and in *allcases* write 2qt(a) for 4b2 and 2qt(b) for 4a2, the *Extra Quarter-Turn Stats* sheet the other way round (its own example triggers show it), and Joba's file writes 4c5 for 4b5. *Optimal* is the shortest finish in DR moves (U, D, R2, L2, F2, B2), E slice solved (a finish that breaks DR is shorter on 4.3% of DRs, section 3); *+1* means a finish one move longer. *qt* is a U or D quarter turn. *Normal* and *inverse* are the two sides, inverse moves in brackets. Section 3 defines finish, route, HTR budget and the rest.

**How to read it.**

- **Start with [section 1](#1-the-short-version)**, the short version: what is new, then what it confirms or corrects. If you read one thing after it, make it the checklist table in [section 4](#4-the-checklists-subset-by-subset).
- **The [worked examples](examples.html)** go with it: 200 DRs from the 20 most common subset × edges, each with the checklist routes that find its optimal written out and the reduction bounding would use, answers folded away. **The [errata](errata.html)** list what the numbers show is wrong in things said on the server, each with an example.
- **Sections 5 to 11** are the details behind each line of section 1; the appendices are lookup tables.

---

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | What is new, then what it confirms or corrects, one line each. |
| [2. What was asked](#2-what-was-asked) | The questions, quoted, with where each is answered. |
| [3. Definitions](#3-definitions) | Finish, route, NISS readings, why an HTR budget, checklist, reduction. |
| [4. The checklists, subset by subset](#4-the-checklists-subset-by-subset) | **The main table.** Routes to try in order per subset × edges, with the share that finds the optimal and +1; what the edge count is worth; edge counts along the route; by HTR budget. |
| [5. The existing sheets, cell by cell](#5-the-existing-sheets-cell-by-cell) | allcases, the 2qt(a)/(b) labels, Aedan Bryant's, the extra-QT sheet, DR Finish Move Counts. |
| [6. Shortest HTR against the optimal](#6-shortest-htr-against-the-optimal) | Linear against NISS HTR, which HTR the optimal uses, nine-move HTRs. |
| [7. Extra quarter turns, and the last DR move](#7-extra-quarter-turns-and-the-last-dr-move) | Three readings of "uses extra qts", half turns before the first qt, the last move either way. |
| [8. DR bounding](#8-dr-bounding) | How often every reduction up to R finds the optimal, how many reductions, against the checklists; Levi Gibson's and JTuu's numbers. |
| [9. FakeMMAP's reduction-length bound](#9-fakemmaps-reduction-length-bound) | Sufficient, how much it prunes, rodneykinney's tables, the index in the multi-qt lower bound. |
| [10. Hand checklists, graded](#10-hand-checklists-graded) | Zagros, Yura Riabov against rogo and Adri, Fanti, Lewis Isom, Jay and rodneykinney, Daichi's cheat sheet. |
| [11. The claims, checked](#11-the-claims-checked) | Each checkable statement from the server, with the verdict. |
| [12. Real DRs](#12-real-drs) | The same tables on the DRs cubelib finds on random scrambles: subset mix, checklists, headlines. |
| [13. What this does not cover](#13-what-this-does-not-cover) | Limits. |
| [Appendix A: full tables](#appendix-a-full-tables) | Every checklist, edge-path checklists, rodneykinney's table, late switches. |
| [Appendix B: how it was computed, and what checks it](#appendix-b-how-it-was-computed-and-what-checks-it) | Model, sampling, the sticker model, nissy, Lean. |
| [Docs referred to](#docs-referred-to) | Links. |

---

## 1. The short version

There isn't much new in the routes themselves: the checklists below put them in the order Daichi's cheat sheet already suggests. What's new is everything around them: how much each route covers, how long its HTRs are, how bounding compares, and whether FakeMMAP's bound helps. Shares are over uniformly random DR states of the subset (25,000 per subset × edges); *finds the optimal* means some optimal finish can be read along that route.

**What's new here**

**How far a short checklist gets you, per subset.** Count a route only when its HTR is at most 2 moves longer than the DR's shortest NISS HTR (budget 2, section 3). Then three routes find the optimal on this share of each corner subset's DRs:

| Subset | Optimal found, 3 routes |
|---|---|
| 0c4 | 86.3% |
| 2c5 | 91.4% |
| 2c4 | 88.4% |
| 2c3 | 78.0% |
| 4c3 | 75.0% |
| 4b2 | 62.6% |
| 0c0 | 60.9% |
| 4a1 | 58.0% |

The same three get a finish within +1 on 84.3% (4a1) to 99.6% (4b5). After the third route each extra route adds at most 8.4 points, and under 3 points in 91.7% of the checklists (section 4).

**The bad-edge count matters, on a few subsets.** A checklist built for the subset × edges beats the corner subset's list (edges pooled) by 1.6 points of all DRs after one route and 0.4 after three. Not much on average, a lot on some. Each row is a subset × edges where it matters, and the share where each list finds the optimal after that many routes:

| Subset × edges | What changes | After | Own list finds the optimal | Pooled list finds the optimal |
|---|---|---|---|---|
| 0c0 0e | its own order | 2 routes | 84.4% | 42.7% |
| 2c4 0e | go linear first | 1 route | 70.1% | 42.7% |
| 2c3 6e (same on 0e and 8e) | switch at 4b2 first | 1 route | 66.1% | 40.9% |
| 4a2 0e | start with the 4b3 regression | 1 route | 29.1% | 4.0% |
| 4a1 0e | start with `4a1 0c0 (4a1 0c0)` | 3 routes | 54.6% | 33.9% |

On 2c5, 0c3, 0c4, 4c3, 4c4 and 4b2 the pooled list loses at most 4.2 points (section 4).

**Which edge count you pass on the way.** Of the DRs whose optimal (budget 2) can go through 4b2, 92.6% can go through 4b2 2e, 56.4% through 4b2 4e and 4.6% through 4b2 0e. From 2c3 it depends on the edges. Each row is a 2c3 edge count; each cell is the share of its DRs that can go through that 4b2:

| From | Can pass 4b2 2e | Can pass 4b2 4e |
|---|---|---|
| 2c3 2e | 69.2% | 46.3% |
| 2c3 0e | 58.3% | 88.6% |

The 4a1 before HTR is 4a1 4e, the 4a2 is 4a2 4e (94.6%), and 2c3 is 4e, 2e or 6e. Aiming for one edge count at each step doesn't give a better checklist, though: the first edge path finds 39.4% of DRs against 61.3% for the first corner route, because on 2c5 2e to 6e, 4b5 2e and 4e, and 4c4 2e and 4e one corner route is many edge paths. Per-step edge checklists are computer only (section 4).

**The HTR budget is what a checklist is really about, not the route.** A NISS reading of a finish is also a linear finish, so *some optimal follows this route* barely separates routes. The share of a corner subset's DRs the best single route covers, lowest to highest corner subset, per budget:

| HTR budget | Best single route covers |
|---|---|
| no limit | 51% to 98% |
| 0 (shortest HTRs only) | 13% to 48% |
| 2 | 29% to 84% |

(section 4).

**Linear vs NISS HTR** (rodneykinney asked in 2023, [30 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069660273356587082)). Over all DRs the shortest NISS HTR is as long as the shortest linear one (better side) on 55.8%, 1 shorter on 32.3% and 2 or more shorter on 11.9%. On 0c3 it's 2+ shorter on 52.4% (section 6).

**The optimal rarely goes through a shortest HTR.** The shortest HTR that any optimal uses, against the DR's shortest NISS HTR, as a share of all DRs:

| Shortest HTR in an optimal | Share of DRs |
|---|---|
| a shortest NISS HTR | 32.9% |
| 1 longer | 31.8% |
| 2 longer | 22.5% |
| 3 or more longer | 12.8% |

On 65.2% of all DRs every optimal needs an HTR of 9 moves or more, and on 29.7% that's the case even though a shorter HTR exists (section 6).

**DR bounding, measured.** Check every reduction to 1q (4a1 4e) of at most R moves, on either side or split. Each row is a value of R, over all DRs:

| R | Finds the optimal | Reductions on average |
|---|---|---|
| 4 | 24.9% | 89 |
| 5 | 40.6% | 748 |
| 6 | 59.3% | 6,242 |

Which subsets suit it depends on R. At R ≤ 4 it's best on 0c0 (91.5%), 4a2 (76.6%) and 4a1 (75.6%). Reducing to 2q instead, reductions of at most 3 moves reach 60.4%.

**By hand it stops at about R ≤ 4.** The counts grow about eightfold per move, and only up to 4 do they stay in the low hundreds, the size of the "check all sub-5 reductions" Levi Gibson calls "super quick" ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311670582601060354)). Past that it's **computer only, an answer key and not advice**. What it takes to find the optimal on 80% of a subset, one row per subset:

| Subset | Every reduction up to | About this many to write |
|---|---|---|
| 0c0 (eight budget-2 routes stay under 80%) | 3 | 156, in reach |
| 4a1 | 5 | 4,901 |
| 4b2 | 6 | 16,087 |
| 2c5, 4b5 | nothing under 6 moves works | |

Nobody writes the 4a1 or 4b2 lists in an hour (section 8).

**FakeMMAP's bound, tested the way FakeMMAP asked.**

- *R as written* is the largest of its five terms. That's proved never too short (Lean), but only because term 1, about $M - 1$, is one of them: it asks for reductions of 12.1 moves on average where 7.0 were needed (1,914,809 state-and-path cases at the optimum), longer than anyone writes. So it's safe to use but prunes nothing in practice.
- *The smallest term*, the bound FakeMMAP's derivation actually gives, is also proved sound once two slips in the printed formulas are fixed: term 2's signs, which as printed make it too short, and the $\alpha$ in every sum, which has to be $\alpha_{i+1}$, the section the two windows share, not $\alpha_i$. It averages 8.9 moves, the same to one decimal as the exact model of the same constraints (8.9, *computer only*).
- *C* bounds the middle block of the finish, a linear HTR of a DR in the same subset, so C is the subset's shortest linear HTR, as FakeMMAP defined it (proved in Lean).
- *The multi-qt lower bounds* ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475)) fail on 923 of those cases with $\alpha_i$; with $\alpha_{i+1}$ they never fail, and they're proved valid.

FakeMMAP asked whether "the typical bound is M \geq 11, rather than M \geq 7" ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533429198553178)). Once every reduction shorter than the one the optimal needs has failed, the corrected bound on a typical path (the median, in moves) is:

| Subset | Corrected bound, median |
|---|---|
| 2c3 | 11 |
| 4b2 | 9 |
| 0c0 | 8 |

That's one or two above the trivial bound, and it reaches the optimum in only 3.9% of 2c3 cases. The per-subset tables rodneykinney asked for ([9 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491873063531188324)) are in section 9 and appendix A.

**Hand checklists graded.** Zagros's eight-step 4b2 order finds the optimal on 71.3% with budget-2 HTRs and a finish within +1 on 93.4%. On 4b2 4e, the share each approach finds the optimal on:

| Approach | Optimal found |
|---|---|
| Yura Riabov's order (trigger, then regress to 2c3), after two steps | 62.3% |
| same, after three steps | 72.9% |
| reduce to 1q first, every reduction of at most 4 moves | 52.5% |
| same, at most 5 moves | 68.6% |

(section 10).

**Breaking DR rarely beats the DR-move optimum.** Solved with all 18 face turns (nissy, *computer only*), a finish outside DR is shorter on this share of DRs:

| DRs | Shorter finish outside DR |
|---|---|
| all | 4.3% |
| DR-move optimum 12 or less | 1.1% |
| DR-move optimum 16 | 35.7% |

It's almost always by one move (mean gain 0.048 moves). Besides long finishes it matters on 0c3 0e (36%), 0c4 0e (26%), 0c0 0e (21%), where shapes like this one win (section 3):

```
R L F2 B2 R' L'   // the type of finish that beats the DR-move optimum there
```

**What it confirms or corrects**

**Confirmed: the routes.** The first route of the budget-2 checklist is what Daichi's cheat sheet says: switch after 4b2 on 4c3 and 0c4, go through 2c3 on 2c4 and 2c5, 4a2 4e switch on 0c3. Graded against my first three routes, Daichi's sheet finds the optimal more often, about as often or less often on these subsets (section 10):

| Daichi's sheet | Where |
|---|---|
| more often | 4b2, 4a1, 2c3 0e and 8e, 0c0 2e to 6e |
| about as often | 2c4 0e to 6e, 4a2 2e, 0c4 2e |
| less often | all of 2c5, 0c3, 4c3, 4c4 and 4b5; 0c4 except 2e; 4a2 0e and 4e; 2c3 2e to 6e |

**Confirmed: uniform states are the right model.** Take the DRs cubelib finds on 10,000 random scrambles (every EO-first DR of at most 11 moves, 6,840,923 of them). Corner-subset shares are within 0.4 points of uniform and mean optimal finishes within 0.05 moves. Per corner subset, every checklist share, bounding share and HTR headline of this section moves by under a point, with two exceptions (share of DRs):

| Number | Real DRs | Uniform |
|---|---|---|
| 0c0, first route | 39.1–40.2% | 42.3% |
| 0c3, NISS HTR 2+ shorter | 50.1% (each DR once) | 52.4% |

The first route is the same on every corner subset, and the first three are the same everywhere but 0c4, where a near-tie changes the third. What shifts is the bad-edge mix inside a subset: 0e up to 43% rarer, 6e up to 17% commoner (section 12).

**Confirmed: the known tables**, exactly: Joba's optimal distribution, DougCube's 663,552 HTR states (mean 10.13), Joba's DR-to-HTR lengths; Aedan Bryant's sheet except four rows that carry another row's numbers and its two fake-HTR rows, whose states were built around one trigger; the *Extra Quarter-Turn Stats* sheet on every comparable row (sections 5, 11).

**The 2qt(a)/(b) labels.** Aedan Bryant's sheet and *allcases* call 4b2 "2qt(a)", as Tzak, Levi Gibson and Zagros said at the time. The one thing added here: the *Extra Quarter-Turn Stats* sheet uses the opposite letters, as its own example triggers show. So mrauo's "Only 1/3 of 2q 4b2e cases use 2qt" read the 4a2 2e row (section 5).

**Explained: the quoted extra-qt numbers.** They depend on whether you ask about every optimal, some optimal or one optimal from a solver; rodneykinney's 57% and Lichi Fang's "over 60%" fit different readings, and both fit (section 7).

**Corrected, with the first study's table: the last DR move.** Turning it the other way gives a finish one move shorter on 32.5% of DRs, never more than one, so about a third of a move on average, not the 1/6 Yura Riabov estimated in 2024 (Yura called it "very rough"). It doesn't change which routes to try (section 7).

**Corrected** (errata, each with an example). Levi Gibson's "check all sub-5 reductions … gets optimal like 75% of the time, and it gets optimal +1 the rest of the time", with bounding alone and every reduction of at most 4, share of DRs where it finds the optimal and a finish within +1:

| Subset | Optimal | Within +1 |
|---|---|---|
| 4a2 (the one Levi Gibson had just named) | 76.6% | 93.6% |
| 2c3 | 48.1% | 78.8% |

So on 4a2 the 75% holds, but +1 doesn't cover the rest. The other corrections:

- 4c4 0e has 10-move linear HTRs.
- The longest shortest HTR is 13 linear and 12 with NISS.
- The optimal through its shortest HTR needs a switch after more than 2 moves on 24.0% of the DRs outside the subsets Evan named as exceptions, an upper bound on how often a late switch is needed (Yura Riabov's "more like 3" holds outside 0c4, 4c4 and 2c5).
- In FakeMMAP's reduction bound and multi-qt lower bounds: the index of $\alpha$ ($\alpha_{i+1}$, not $\alpha_i$) and, when R is read as the smallest term, the signs of term 2 (proved in Lean, with counterexamples).

**Confirmed**: Levi Gibson's "pretty sure 15 is gods number for 4a1 4e" is right for the leave slice, which is what Levi Gibson measures (15, exact); the full finish can need 17.

---

## 2. What was asked

The questions, in the words of the people who asked them, and where each is answered. Most got a guess or no answer at the time.

**Which routes, how often (section 4)**

- Daichi built the cheat sheet "to filter routes to check rather than DRs itself" ([12 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515177158870569101)); JTuu asked for the data behind it ("did you post the raw stats somewhere?", [13 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515419517873033256)). *Answer*: section 4 gives the routes in order, each with the share of DRs where the routes so far find the optimal, so the shares add up (cumulative).
- Does the bad-edge count change which routes are good, not only the corner subset? And how often do you go through, say, 4b2 4e rather than 4b2 2e? *Answer*: section 4.
- wen ([8 Nov 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1171788784279494688)): "Anyone else feel like for 4q 2c, the optimals are most often reasonably explained with something like a direct HTR, or 1q then switch and 3q, and hardly ever with 2q switch 2q?" *Answer*: on 2c4, with HTRs at most 2 over the shortest, the optimal is reached by:

  | Route shape | Finds the optimal |
  |---|---|
  | 3 qts then switch (or 1 then 3) | 66.5% |
  | direct HTR | 54.0% |
  | 2 switch 2 | 30.8% |

  wen's order is right; "hardly ever" is too strong.
- Yura Riabov, on 4b2 4e ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258421085251178608)): "4b2 4e is basically the best 4q subset"; rogo ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258442750953525399)): "the first approach apart from R U2 F2 R to check should still be 'reduce to 1qt 4e and niss trace for short htrs' i think?" *Answer*: section 10.

**HTRs and the optimal (section 6)**

- rodneykinney ([30 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069660273356587082)): "How often is one significantly shorter than the other, and how often is it just as long to get to HTR either way?" (linear against NISS HTR). No answer in the Discord export. *Answer*: section 6, per subset.
- Brian ([24 Feb 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1211149426198847488)): "Are there stats for how often the optimal finish for a DR uses an optimal HTR solution for that DR?" Tom Nelson ([24 Feb 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1211151427460800612)): "I assume it'd be quite high for 4-5q and low for good subsets". Zagros ([27 Dec 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1454570265353912422)): "anyone know what % of DRs (maybe by subset?) have an optimal solution from the shortest HTR on one of the sides, or maybe also the shortest possible niss HTR". JTuu ([27 Dec 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1454571263434690803)): "anything of the form "does there exist an optimal with X property" is gonna be computationally very bad". *Answer*: some optimal uses a shortest NISS HTR on 32.9% of DRs, a shortest linear HTR of its side on 25.2%. Tom Nelson's guess is right in direction for 0c3, but not for 4-5qt in general:

  | Subset | Some optimal uses a shortest NISS HTR |
  |---|---|
  | 0c3 | 53.5% |
  | 2c4 | 31.6% |
  | 4b5 | 31.4% |
  | 4b2 | 30.0% |

- kalindumaxxer ([27 Jul 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1266881061418176522)): "how common does the optimal solution for htr-2e use an inoptimal htr". Jakob Jernsletten ([29 Jul 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1267543886184579072)): "Probably almost always? There are so few optimal HTRs compared to the many more variants in +1 or more". *Answer*: on 0c0 2e no optimal uses a shortest NISS HTR on 67.8%. Common, not almost always.
- rodneykinney ([13 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1063504388976545902)): "I'm interested to know how often the solution involves a non-optimal HTR". Daichi ([3 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1511617316876587109)): "Do we know the average length of post HTR on DR optimal solutions only?" wen ([3 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1511620241313108008)): "Tldr no". *Answer*: section 6; the post-HTR part of the optimal with the shortest HTR is 4.59 moves on average.
- Yura Riabov ([8 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1392217666130804837), [8 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1392217798851297352)): "Is there a stat on average slice in dr optimals?", "I know average slice is 0.9ish but i don't know about optimals". *Answer*: the optimal finish is 0.290 moves longer than the optimal leave-slice on average, from 0.71 on 0c0 down to 0.05 on 0c3. Aedan Bryant's sheet had the same in its "No E Difference" column.

**Extra quarter turns, and the last DR move (section 7)**

- tseitsei89 ([25 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1233062604705108060)): "how common is it to have a 3qt DR where the ONLY optimal solution(s) go through 5qt path? I just had one". Yura Riabov ([25 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1233063193782259764)): "not too rare, but depends on the case". *Answer*: every optimal uses 5qt on 17.5% of 2c3, 27.4% of 4c3, 24.0% of 0c3; by edges in section 7.
- Lichi Fang ([2 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1246934529072042056), [6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248336857452908564)): "Do we have any statistics about the average move it takes to finish a DR when allowing the last move of the DR to be inverted?", "how much do you think would inverting the last move of DR change the length for DR finish?" *Answer*: section 7 (and the first study, 6.6).

**DR bounding and FakeMMAP's bound (sections 8 and 9)**

- Kai Cui ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312050785743278140)): "How often can you get optimal with just sub5". Levi Gibson ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312050982489952397)): "Surprisingly often"; Kai Cui: "Would it be around 80 percent?" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051034906038323)), Levi Gibson: "yeah something like that I'd guess" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051081831780434)), "for 2c3 that is" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051112253329439)). *Answer*: section 8 and the errata.
- How effective is DR bounding per subset: how often does it find the optimal, and how many reductions to 1q or 2q do you have to check for that, depending on the threshold? And can FakeMMAP's linear-programming estimates prune branches? *Answer*: sections 8 and 9.
- rodneykinney, on FakeMMAP's bound ([9 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491873063531188324)): "This sounds interesting but, I must say, almost impossible to follow. Would it be possible to put together some tables for specific cases?" FakeMMAP ([9 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491880288597446767)): "Compute these bounds by HTR subsets." *Answer*: section 9 and appendix A.

What this leaves open is in section 13.

---

## 3. Definitions

**Finish.** A sequence of DR moves (U, D, R2, L2, F2, B2) that solves the DR state, E slice included. No DR-breaking or HTR-breaking moves in the HTR part; the post-HTR part may be anything in the DR group, so a finish whose last part has a quarter turn counts (it is rare: marked `| qt` in the files). For each state I list every optimal finish and every finish one move longer, including both orders of moves that commute.

**DR-breaking finishes.** *Optimal* here always means the best finish in DR moves. To see how much that leaves out I ran nissy's exact solver (`solve optimal`, all 18 face turns) on 48,000 uniform DR states (the first 1,000 of each subset × edges sample). A finish shorter than the DR-move optimum exists on **4.3% ± 0.1 points of DRs**, by one move in 90% of those and by up to 4; the mean gain is 0.048 moves. The real DRs of section 12 (23,976 states, 500 per subset × edges) give about the same, and it hardly touches the finishes you write. Each row is a set of DRs and the share of them with a shorter finish outside DR (± a standard error, in points, where given):

| DRs | Shorter finish outside DR |
|---|---|
| real, each DR once | 4.2% ± 0.2 |
| real, each scramble once | 3.9% ± 0.4 |
| uniform, DR-move optimum 12 or less | 1.1% |
| uniform, DR-move optimum 15 | 9.4% |
| uniform, DR-move optimum 16 | 35.7% |

So it only climbs for long finishes. The exceptions are three 0e cells: 0c3 0e 36% (13% by 2 or more); 0c4 0e 26% (5% by 2 or more); 0c0 0e 21% (7% by 2 or more). An example, with the slice-like shape these states have:

```
B2 L2 R2 F2 R2 U2 L2 R2 U2 R2 U2   // on a solved cube, so DR moves only: 0c0 0e, DR-move optimum 11
R L F2 B2 R' L' D2   // solves it in 7
```

*Computed with nissy, not proved in Lean*; every solution quoted was replayed on a sticker model (27 solutions, 0 failures). Each row is a corner subset: the share of DRs with a shorter finish outside DR, uniform and on real DRs (section 12), then how the uniform share splits by how many moves shorter:

| Subset | Shorter finish outside DR, uniform (± SE) | Real DRs, each DR once | Real DRs, each scramble once | Shorter by 1 move, uniform (%) | By 2 or more (%) |
|---|---|---|---|---|---|
| 0c0 | 7.6 ± 0.5% | 8.5 ± 0.8% | 7.0 ± 1.2% | 6.4 | 1.1 |
| 2c5 | 6.3 ± 0.5% | 6.0 ± 0.7% | 5.3 ± 1.0% | 5.5 | 0.8 |
| 2c4 | 3.0 ± 0.3% | 3.4 ± 0.5% | 4.0 ± 1.2% | 2.8 | 0.3 |
| 0c3 | 7.5 ± 0.5% | 8.4 ± 0.8% | 7.0 ± 1.2% | 6.8 | 0.7 |
| 4a2 | 4.2 ± 0.4% | 4.8 ± 0.7% | 4.2 ± 0.9% | 4.0 | 0.2 |
| 4a1 | 6.0 ± 0.5% | 6.2 ± 0.8% | 6.0 ± 1.4% | 5.2 | 0.8 |
| 2c3 | 3.4 ± 0.4% | 3.0 ± 0.5% | 1.9 ± 0.4% | 3.1 | 0.3 |
| 0c4 | 1.7 ± 0.2% | 1.6 ± 0.3% | 1.0 ± 0.2% | 1.7 | 0.1 |
| 4c3 | 2.8 ± 0.4% | 3.3 ± 0.6% | 1.7 ± 0.4% | 2.6 | 0.2 |
| 4c4 | 6.6 ± 0.5% | 6.5 ± 0.7% | 6.6 ± 1.3% | 5.8 | 0.8 |
| 4b2 | 3.5 ± 0.4% | 2.3 ± 0.4% | 1.8 ± 0.5% | 3.4 | 0.1 |
| 4b5 | 5.9 ± 0.5% | 5.9 ± 0.7% | 6.0 ± 1.2% | 5.1 | 0.8 |
| all DRs | 4.3 ± 0.1% | 4.2 ± 0.2% | 3.9 ± 0.4% | 3.9 | 0.4 |

Same rows, in moves: the mean gain over all DRs, and the mean optimum in DR moves and with any moves:

| Subset | Mean gain (moves) | Mean DR-move optimum (moves) | Mean any-move optimum (moves) |
|---|---|---|---|
| 0c0 | 0.088 | 12.27 | 12.18 |
| 2c5 | 0.071 | 14.34 | 14.27 |
| 2c4 | 0.033 | 13.64 | 13.61 |
| 0c3 | 0.084 | 14.41 | 14.33 |
| 4a2 | 0.044 | 13.37 | 13.32 |
| 4a1 | 0.068 | 12.45 | 12.38 |
| 2c3 | 0.037 | 12.94 | 12.90 |
| 0c4 | 0.018 | 13.68 | 13.66 |
| 4c3 | 0.031 | 13.49 | 13.46 |
| 4c4 | 0.075 | 14.40 | 14.32 |
| 4b2 | 0.036 | 12.68 | 12.65 |
| 4b5 | 0.067 | 14.29 | 14.22 |
| all DRs | 0.048 | 13.58 | 13.54 |

By the DR-move optimum (uniform, weighted by exact subset size). Each row is a DR-move optimum: its share of DR states, how many were sampled, and the share of those with a shorter finish outside DR:

| DR-move optimum | Share of DR states | Sampled | A shorter finish outside DR exists |
|---|---|---|---|
| 8 | 0.022% | 95 | 0.061% |
| 9 | 0.096% | 269 | 0.092% |
| 10 | 0.55% | 701 | 0.32% |
| 11 | 2.7% | 1,805 | 0.73% |
| 12 | 11.3% | 5,578 | 1.3% |
| 13 | 28.7% | 12,904 | 2.0% |
| 14 | 37.1% | 16,697 | 3.8% |
| 15 | 18.3% | 9,055 | 9.4% |
| 16 | 1.1% | 841 | 35.7% |
| 17 | 0.007% | 13 | 43.1% |

**Corner path, route.** Read a finish move by move and write down the corner subset at the start and after each quarter turn, until the cube is in HTR (corners and edges). `4b2 2c3 4b2 4a1 0c0` is a 4b2 that regresses to 2c3, comes back to 4b2, then goes 4a1 and HTR. The moves up to that point are the finish's HTR, the rest its post-HTR part. A *route* (route class) is the chain plus where the NISS switch is: `4b2 2c3 (4b2 4a1 0c0)` means one qt on the first side to 2c3, then switch, and the rest on the other side, where the subsets are read on that side. Routes are the kind Daichi's cheat sheet lists; the list of routes comes from the data, not from a list picked in advance. Edge counts are dropped from route names in the tables (they are in the files); where a route does carry them, its states are separated by arrows, `2c3 2e → 4b2 2e → 4a1 4e → 0c0`.

**NISS readings.** A finish S of a state X can be found as A on normal and then B on inverse whenever $S = A \cdot B^{-1}$; and the other way, B on inverse first. So every finish of $n$ moves has $2(n + 1)$ readings, one per split and side. A route *works* on a state if some reading of some optimal finish (or +1 finish, at +1) follows it. Both sides are always available: a linear route on the inverse is a reading too.

**Why a budget is needed.** The catch is that every NISS reading is also a linear finish of the same length. So *some optimal follows route X* says nothing about whether NISS was needed: whenever a NISS reading of an optimal follows X, the same moves read linearly follow some other route, and a route that is long enough on one side almost always has some reading that fits. With no limit, three routes cover 93.6% to >99.9% of a corner subset (section 4), which is true and useless. What NISS really changes is how long the HTR is that you have to find. So each route is graded with an **HTR budget**: it counts on a state only if its reading reaches HTR within the state's shortest NISS HTR plus the budget (moves on both sides counted). Budget 0 means you only ever look at the shortest HTRs; budget 2 means HTRs up to two moves longer than the shortest; *no limit* is the plain route. I use budget 2 as the default: it is about what a strong solver checks, and the tables give 0, 1, 2 and no limit.

**Checklist.** For a subset × edges (or a corner subset with its edge counts pooled by their exact sizes), the routes in greedy order: first the route that works on the most states, then the one that adds the most states not yet covered, and so on. The cumulative share after k routes is the share of DRs where at least one of the first k finds an optimal finish (or within +1). Greedy is close to the best possible set (tested with no HTR limit): among the top 25 to 40 routes, the best set of 1 to 4 routes beats greedy by at most 0.5 points in 2,192 of 2,208 cases, and by 1.8 points at worst.

**Reduction (bounding).** A reduction to 1q is a pair of sequences, P on normal and U on inverse, each empty or ending in a quarter turn, after which the state (inverse of U, then the scramble, then P) is 4a1 4e, so one more quarter turn and half turns finish it. Its length is |P| + |U|. A reduction to 2q ends in a state that a finish with exactly two quarter turns solves (4a2, 4b2, or 0c0 with bad edges). Bounding with threshold R means writing every reduction of length at most R and finishing each reduced state as well as it can be finished. *Bounding finds the optimal* means that some reduction of length at most R plus the optimal finish of the reduced state is an optimal finish of the DR. That is the best a solver can get from those reductions; the bound arithmetic in the bounding docs only decides the order and when to stop.

**The last DR move.** If the DR ends in a quarter turn of a side face (R, say), R' is also a DR, and its state is X·R2. *With the last move either way* takes the better of X and X·R2, as in the first study.

**Samples.** For each of the 48 subset × edges, 25,000 states drawn uniformly from the subset (each DR state equally likely), seed 20261112. Corner-subset rows pool the edge counts weighted by the exact number of states in each, so they are shares of uniformly random DR states of that corner subset. Counts of reductions use the first 4,000 states per subset × edges. Fixed targets (a finish of 10, 11 or 12 or better) use every finish up to max(optimal + 1, min(optimal + 2, 12)) moves. Where a reading needs one optimal per state picked at random (to compare with sheets that recorded one solver output), I use 5,000 states per subset × edges, seed 7.

---

## 4. The checklists, subset by subset

This is the main table. There's a checklist for every subset × edges, not just per corner subset, because the bad-edge count changes which routes are good (how much is measured below). Sampled, 25,000 states per subset × edges. Brackets are the part after the NISS switch, and a route ends at HTR (`0c0`). All 8 routes with their cumulative shares at the optimum and at +1, plus the no-limit lists, are in appendix A.

Each row is a subset × edges and the first three routes of its budget-2 checklist, in the order to try them:

| Subset | Try first | Then | Then |
|---|---|---|---|
| 0c0 0e | `0c0 4a1 0c0` | `0c0` | `0c0 \| qt` |
| 0c0 2e | `0c0 4a1 0c0` | `0c0 4a1 0c0 4a1 (0c0)` (mirror: `0c0 4a1 (4a2 4a1 0c0)`) | `0c0 4a1 (0c0)` |
| 0c0 4e | `0c0 4a1 0c0` | `0c0 4a1 (0c0)` | `0c0 4a1 4b2 4a1 0c0` |
| 0c0 6e | `0c0 4a1 (0c0)` | `0c0 4a1 0c0 4a1 (0c0)` (mirror: `0c0 4a1 (4a2 4a1 0c0)`) | `0c0 4a1 (0c0 4a1 0c0)` (mirror: `0c0 4a1 4b2 4a1 (0c0)`) |
| 0c0 8e | `0c0 4a1 (0c0)` | `0c0 4a1 0c0` | `0c0 4a1 0c0 4a1 (0c0)` (mirror: `0c0 4a1 (4a2 4a1 0c0)`) |
| 2c5 0e | `2c5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 (4a1 0c0)`) | `2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 4a1 (0c0)`) | `2c5 2c4 2c3 4b2 4a1 0c0` |
| 2c5 2e | `2c5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 (4a1 0c0)`) | `2c5 2c4 2c3 4b2 4a1 0c0` | `2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 4a1 (0c0)`) |
| 2c5 4e | `2c5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 (4a1 0c0)`) | `2c5 2c4 2c3 4b2 4a1 0c0` | `2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 4a1 (0c0)`) |
| 2c5 6e | `2c5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 (4a1 0c0)`) | `2c5 2c4 2c3 4b2 4a1 0c0` | `2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 4a1 (0c0)`) |
| 2c5 8e | `2c5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 (4a1 0c0)`) | `2c5 2c4 2c3 4b2 4a1 (0c0)` (mirror: `2c5 2c4 (2c3 4b2 4a1 0c0)`) | `2c5 2c4 2c3 4b2 4a1 0c0` |
| 2c4 0e | `2c4 2c3 4b2 4a1 0c0` | `2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b3 4a2 4a1 (0c0)`) | `2c4 2c3 4b2 (4a1 0c0)` (mirror: `2c4 4b3 4a2 (4a1 0c0)`) |
| 2c4 2e | `2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b3 4a2 4a1 (0c0)`) | `2c4 2c3 4b2 4a1 0c0` | `2c4 2c3 4b2 (4a1 0c0)` (mirror: `2c4 4b3 4a2 (4a1 0c0)`) |
| 2c4 4e | `2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b3 4a2 4a1 (0c0)`) | `2c4 2c3 4b2 4a1 0c0` | `2c4 2c3 4b2 (4a1 0c0)` (mirror: `2c4 4b3 4a2 (4a1 0c0)`) |
| 2c4 6e | `2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b3 4a2 4a1 (0c0)`) | `2c4 2c3 4b2 4a1 0c0` | `2c4 2c3 4b2 (4a1 0c0)` (mirror: `2c4 4b3 4a2 (4a1 0c0)`) |
| 2c4 8e | `2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b3 4a2 4a1 (0c0)`) | `2c4 2c3 4b2 (4a1 0c0)` (mirror: `2c4 4b3 4a2 (4a1 0c0)`) | `2c4 2c3 4b2 4a1 0c0` |
| 0c3 0e | `0c3 4a2 (4a1 0c0)` (mirror: `0c3 4a2 4a1 (0c0)`) | `0c3 4a2 4b3 4a2 4a1 (0c0)` (mirror: `0c3 4a2 (4a1 4b2 4a1 0c0)`) | `0c3 4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4b3 2c4 (2c3 4b2 4a1 0c0)`) |
| 0c3 2e | `0c3 4a2 (4a1 0c0)` (mirror: `0c3 4a2 4a1 (0c0)`) | `0c3 4a2 4b3 4a2 4a1 (0c0)` (mirror: `0c3 4a2 (4a1 4b2 4a1 0c0)`) | `0c3 4a2 4a1 0c0` |
| 0c3 4e | `0c3 4a2 (4a1 0c0)` (mirror: `0c3 4a2 4a1 (0c0)`) | `0c3 4a2 4b3 4a2 4a1 (0c0)` (mirror: `0c3 4a2 (4a1 4b2 4a1 0c0)`) | `0c3 4a2 4b3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4a1 4b2 (4a1 0c0)`) |
| 0c3 6e | `0c3 4a2 (4a1 0c0)` (mirror: `0c3 4a2 4a1 (0c0)`) | `0c3 4a2 4b3 4a2 4a1 (0c0)` (mirror: `0c3 4a2 (4a1 4b2 4a1 0c0)`) | `0c3 4a2 4a1 0c0` |
| 0c3 8e | `0c3 4a2 (4a1 0c0)` (mirror: `0c3 4a2 4a1 (0c0)`) | `0c3 4a2 4b3 4a2 4a1 (0c0)` (mirror: `0c3 4a2 (4a1 4b2 4a1 0c0)`) | `0c3 4a4 4b5 2c4 2c3 4b2 (4a1 0c0)` (mirror: `0c3 4a4 4b5 (2c4 2c3 4b2 4a1 0c0)`) |
| 4a2 0e | `4a2 4b3 4a2 4a1 (0c0)` (mirror: `4a2 4a1 (4b2 4a1 0c0)`) | `4a2 4a1 4b2 4a1 0c0` | `4a2 4a1 (0c0)` |
| 4a2 2e | `4a2 4b3 4a2 4a1 (0c0)` (mirror: `4a2 4a1 (4b2 4a1 0c0)`) | `4a2 4a1 (0c0)` | `4a2 4a1 4b2 4a1 0c0` |
| 4a2 4e | `4a2 4a1 0c0` | `4a2 4b3 4a2 4a1 (0c0)` (mirror: `4a2 4a1 (4b2 4a1 0c0)`) | `4a2 4a1 4b2 4a1 0c0` |
| 4a1 0e | `4a1 0c0 (4a1 0c0)` (mirror: `4a1 4a2 4a1 (0c0)`) | `4a1 4b2 2c3 4b2 4a1 (0c0)` (mirror: `4a1 4b2 (2c3 4b2 4a1 0c0)`) | `4a1 0c0 4a1 (0c0)` (mirror: `4a1 4a2 (4a1 0c0)`) |
| 4a1 2e | `4a1 4b2 4a1 0c0` | `4a1 0c0 4a1 0c0` | `4a1 0c0 (4a1 0c0)` (mirror: `4a1 4a2 4a1 (0c0)`) |
| 4a1 4e | `4a1 0c0` | `4a1 4b2 4a1 0c0` | `4a1 0c0 (4a1 0c0)` (mirror: `4a1 4a2 4a1 (0c0)`) |
| 2c3 0e | `2c3 4b2 (4a1 0c0)` (mirror: `2c3 4b2 4a1 (0c0)`) | `2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c3 2c4 2c3 4b2 4a1 (0c0)`) | `2c3 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 4a1 (0c0)`) |
| 2c3 2e | `2c3 4b2 4a1 0c0` | `2c3 4b2 (4a1 0c0)` (mirror: `2c3 4b2 4a1 (0c0)`) | `2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c3 2c4 2c3 4b2 4a1 (0c0)`) |
| 2c3 4e | `2c3 4b2 4a1 0c0` | `2c3 4b2 (4a1 0c0)` (mirror: `2c3 4b2 4a1 (0c0)`) | `2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c3 2c4 2c3 4b2 4a1 (0c0)`) |
| 2c3 6e | `2c3 4b2 (4a1 0c0)` (mirror: `2c3 4b2 4a1 (0c0)`) | `2c3 4b2 4a1 0c0` | `2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c3 2c4 2c3 4b2 4a1 (0c0)`) |
| 2c3 8e | `2c3 4b2 (4a1 0c0)` (mirror: `2c3 4b2 4a1 (0c0)`) | `2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c3 2c4 2c3 4b2 4a1 (0c0)`) | `2c3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 (4a1 0c0)`) |
| 0c4 0e | `0c4 4a3 4b2 (4a1 0c0)` | `0c4 4a3 4b2 4a1 0c0` | `0c4 4a3 (4a2 4a1 0c0)` (mirror: `0c4 4a3 4b2 4a1 (0c0)`) |
| 0c4 2e | `0c4 4a3 4b2 (4a1 0c0)` | `0c4 4a3 4b2 4a1 0c0` | `0c4 4a3 4b2 2c3 4b2 4a1 (0c0)` (mirror: `0c4 4a3 (2c4 2c3 4b2 4a1 0c0)`) |
| 0c4 4e | `0c4 4a3 4b2 (4a1 0c0)` | `0c4 4a3 4b2 4a1 0c0` | `0c4 4a3 (4a2 4a1 0c0)` (mirror: `0c4 4a3 4b2 4a1 (0c0)`) |
| 0c4 6e | `0c4 4a3 4b2 (4a1 0c0)` | `0c4 4a3 (4a2 4a1 0c0)` (mirror: `0c4 4a3 4b2 4a1 (0c0)`) | `0c4 4a3 4b2 2c3 4b2 4a1 (0c0)` (mirror: `0c4 4a3 (2c4 2c3 4b2 4a1 0c0)`) |
| 0c4 8e | `0c4 4a3 4b2 (4a1 0c0)` | `0c4 4a3 (4a2 4a1 0c0)` (mirror: `0c4 4a3 4b2 4a1 (0c0)`) | `0c4 4a3 4b2 2c3 4b2 4a1 (0c0)` (mirror: `0c4 4a3 (2c4 2c3 4b2 4a1 0c0)`) |
| 4c3 0e | `4a3 4b2 (4a1 0c0)` (mirror: `4b3 4a2 4a1 (0c0)`) | `4a3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b3 2c4 2c3 4b2 (4a1 0c0)`) | `4b3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4a3 0c4 4a3 4b2 (4a1 0c0)`) |
| 4c3 2e | `4a3 4b2 (4a1 0c0)` (mirror: `4b3 4a2 4a1 (0c0)`) | `4b3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4a3 0c4 4a3 4b2 (4a1 0c0)`) | `4a3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b3 2c4 2c3 4b2 (4a1 0c0)`) |
| 4c3 4e | `4a3 4b2 (4a1 0c0)` (mirror: `4b3 4a2 4a1 (0c0)`) | `4b3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4a3 0c4 4a3 4b2 (4a1 0c0)`) | `4a3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b3 2c4 2c3 4b2 (4a1 0c0)`) |
| 4c4 0e | `4b4 4a3 4b2 (4a1 0c0)` (mirror: `4a4 0c3 4a2 (4a1 0c0)`) | `4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b4 2c5 4b4 4a3 (4a2 4a1 0c0)`) | `4b4 2c5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `4a4 4a3 4b2 2c3 4b2 4a1 (0c0)`) |
| 4c4 2e | `4b4 4a3 4b2 (4a1 0c0)` (mirror: `4a4 0c3 4a2 (4a1 0c0)`) | `4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b4 4a3 0c4 4a3 4b2 (4a1 0c0)`) | `4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b4 2c5 4b4 4a3 (4a2 4a1 0c0)`) |
| 4c4 4e | `4b4 4a3 4b2 (4a1 0c0)` (mirror: `4a4 0c3 4a2 (4a1 0c0)`) | `4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b4 4a3 0c4 4a3 4b2 (4a1 0c0)`) | `4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b4 2c5 4b4 4a3 (4a2 4a1 0c0)`) |
| 4b2 0e | `4b2 4a1 0c0` | `4b2 2c3 4b2 (4a1 0c0)` (mirror: `4b2 4a1 0c0 (4a1 0c0)`) | `4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b2 2c3 4b2 4a1 (0c0)`) |
| 4b2 2e | `4b2 4a1 0c0` | `4b2 2c3 4b2 4a1 (0c0)` (mirror: `4b2 2c3 (4b2 4a1 0c0)`) | `4b2 4a1 (0c0)` |
| 4b2 4e | `4b2 4a1 0c0` | `4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b2 2c3 4b2 4a1 (0c0)`) | `4b2 2c3 4b2 4a1 0c0` |
| 4b5 0e | `4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b5 2c4 4b3 4a2 (4a1 0c0)`) | `4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b5 2c4 2c3 4b2 4a1 (0c0)`) | `4b5 2c4 2c3 4b2 4a1 0c0` |
| 4b5 2e | `4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b5 2c4 2c3 4b2 4a1 (0c0)`) | `4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b5 2c4 4b3 4a2 (4a1 0c0)`) | `4b5 2c4 2c3 4b2 4a1 0c0` |
| 4b5 4e | `4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b5 2c4 2c3 4b2 4a1 (0c0)`) | `4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b5 2c4 4b3 4a2 (4a1 0c0)`) | `4b5 2c4 2c3 4b2 4a1 0c0` |

How far those routes get, same rows: the share of DRs where the first 1, 2, 3 or 5 routes find an optimal finish, and where the first three find a finish within +1:

| Subset | Optimal found, 1 route | Optimal found, 2 routes | Optimal found, 3 routes | Optimal found, 5 routes | Within +1, same 3 routes |
|---|---|---|---|---|---|
| 0c0 0e | 42.5% | 84.4% | 92.6% | 93.0% | 98.3% |
| 0c0 2e | 60.5% | 65.7% | 70.2% | 73.0% | 92.3% |
| 0c0 4e | 44.9% | 57.8% | 61.5% | 65.1% | 88.1% |
| 0c0 6e | 40.8% | 53.7% | 60.2% | 65.7% | 88.0% |
| 0c0 8e | 53.5% | 70.1% | 77.1% | 78.3% | 95.0% |
| 2c5 0e | 77.8% | 86.5% | 89.6% | 91.8% | 98.7% |
| 2c5 2e | 74.8% | 86.2% | 91.0% | 92.9% | 98.7% |
| 2c5 4e | 71.5% | 86.0% | 91.9% | 93.4% | 99.0% |
| 2c5 6e | 73.0% | 84.1% | 90.6% | 92.7% | 98.7% |
| 2c5 8e | 77.6% | 86.0% | 91.0% | 92.5% | 98.9% |
| 2c4 0e | 70.1% | 85.9% | 88.6% | 88.9% | 98.7% |
| 2c4 2e | 67.7% | 86.3% | 89.9% | 90.8% | 98.9% |
| 2c4 4e | 62.0% | 82.0% | 87.6% | 88.4% | 98.7% |
| 2c4 6e | 73.8% | 84.1% | 88.5% | 89.6% | 98.6% |
| 2c4 8e | 77.7% | 89.5% | 91.5% | 92.9% | 99.4% |
| 0c3 0e | 85.5% | 94.2% | 96.6% | 97.2% | 99.8% |
| 0c3 2e | 80.8% | 91.3% | 92.1% | 92.8% | 99.5% |
| 0c3 4e | 67.2% | 85.1% | 85.8% | 86.8% | 98.7% |
| 0c3 6e | 82.6% | 93.9% | 94.6% | 95.2% | 99.7% |
| 0c3 8e | 87.3% | 94.8% | 96.1% | 96.8% | 99.7% |
| 4a2 0e | 29.1% | 40.4% | 44.4% | 50.3% | 68.2% |
| 4a2 2e | 42.2% | 67.8% | 76.8% | 81.4% | 95.7% |
| 4a2 4e | 60.9% | 72.2% | 79.1% | 85.3% | 93.6% |
| 4a1 0e | 33.5% | 46.5% | 54.6% | 66.5% | 84.2% |
| 4a1 2e | 38.8% | 58.8% | 70.5% | 78.2% | 91.7% |
| 4a1 4e | 33.6% | 50.3% | 60.6% | 69.5% | 86.2% |
| 2c3 0e | 46.3% | 67.0% | 75.1% | 85.5% | 95.9% |
| 2c3 2e | 66.5% | 79.6% | 80.2% | 80.8% | 96.6% |
| 2c3 4e | 55.3% | 76.6% | 78.1% | 79.9% | 96.1% |
| 2c3 6e | 66.1% | 73.3% | 76.7% | 79.8% | 95.8% |
| 2c3 8e | 46.3% | 67.2% | 74.5% | 81.3% | 95.7% |
| 0c4 0e | 83.2% | 86.8% | 87.6% | 88.3% | 97.5% |
| 0c4 2e | 86.5% | 88.0% | 89.1% | 90.6% | 98.1% |
| 0c4 4e | 83.5% | 85.1% | 86.1% | 87.8% | 97.5% |
| 0c4 6e | 81.8% | 83.7% | 85.4% | 87.3% | 97.8% |
| 0c4 8e | 80.3% | 86.2% | 87.1% | 88.1% | 98.2% |
| 4c3 0e | 70.8% | 78.4% | 83.3% | 88.6% | 96.2% |
| 4c3 2e | 66.2% | 72.0% | 75.1% | 80.1% | 94.3% |
| 4c3 4e | 62.3% | 70.2% | 74.4% | 79.6% | 93.9% |
| 4c4 0e | 65.2% | 72.4% | 76.7% | 81.9% | 96.3% |
| 4c4 2e | 67.9% | 75.4% | 78.7% | 82.1% | 96.4% |
| 4c4 4e | 68.4% | 74.8% | 78.2% | 81.5% | 95.9% |
| 4b2 0e | 36.5% | 51.1% | 61.0% | 72.4% | 85.5% |
| 4b2 2e | 45.9% | 53.7% | 59.0% | 66.3% | 86.3% |
| 4b2 4e | 30.3% | 53.3% | 66.8% | 76.0% | 89.1% |
| 4b5 0e | 60.8% | 84.2% | 92.6% | 93.0% | 99.4% |
| 4b5 2e | 62.6% | 85.1% | 93.6% | 93.8% | 99.6% |
| 4b5 4e | 67.0% | 89.6% | 93.9% | 94.0% | 99.6% |

The hardest row is 4a2 0e (44.4% after three routes). Where the edge count changes the order, and by how much, is next.

**What the edge count is worth.** Take the checklist built for the subset × edges itself, and the corner subset's list with edge counts pooled (the pooled table further down), and run both on the same DRs. The difference is what knowing the DR's bad-edge count buys you. Averaged over all DRs, each subset × edges weighted by its real frequency, the own list is ahead by this many percentage points (own list's share minus pooled list's share):

| Target | Own list ahead after 1 route (points) | After 2 routes | After 3 routes | After 5 routes |
|---|---|---|---|---|
| Optimal | 1.6 | 0.6 | 0.4 | 0.1 |
| Within +1 | 1.6 | 0.5 | 0.3 | 0.0 |

Small on average, because the edge counts where it matters are mostly the rare ones. Inside a corner subset it can be a lot more. Each row is a corner subset at the step where the gap is largest:

| Corner subset | Own list ahead by (points) | After |
|---|---|---|
| 4a2 | 9.8 | 1 route |
| 4a1 | 9.3 | 2 routes |
| 2c3 | 6.5 | 1 route |
| 0c0 | 5.3 | 1 route |

Every subset × edges where the own list gains at least a point somewhere (optimal or +1, after 1, 2, 3 or 5 routes). Each row is one subset × edges; the last four columns are how many more DRs out of 100 its own checklist finds the optimal on than the pooled one, after that many routes:

| Subset | Own list: first route | Pooled list's first route: place in own list | After 1 route (own − pooled, points) | After 2 routes | After 3 routes | After 5 routes |
|---|---|---|---|---|---|---|
| 0c0 0e | same | 1 | +0.0 | +41.7 | +49.9 | +50.4 |
| 0c0 4e | same | 1 | +0.0 | +0.0 | +2.0 | +0.7 |
| 0c0 6e | `0c0 4a1 (0c0)` | 6 | +22.7 | +11.5 | +5.3 | +3.6 |
| 0c0 8e | `0c0 4a1 (0c0)` | 2 | +6.9 | +0.0 | +0.0 | +0.4 |
| 2c5 0e | same | 1 | +0.0 | +4.2 | +0.0 | +0.0 |
| 2c5 8e | same | 1 | +0.0 | +1.8 | +0.1 | +0.1 |
| 2c4 0e | `2c4 2c3 4b2 4a1 0c0` | 2 | +27.4 | +0.0 | +0.0 | +0.1 |
| 2c4 8e | same | 1 | +0.0 | +6.5 | +0.0 | +0.3 |
| 0c3 0e | same | 1 | +0.0 | +0.0 | +2.4 | +0.6 |
| 0c3 8e | same | 1 | +0.0 | +0.0 | +1.2 | +1.5 |
| 4a2 0e | `4a2 4b3 4a2 4a1 (0c0)` | 3 | +25.1 | +7.4 | +0.0 | +2.5 |
| 4a2 2e | `4a2 4b3 4a2 4a1 (0c0)` | 2 | +8.3 | +0.0 | +0.0 | +1.8 |
| 4a2 4e | `4a2 4a1 0c0` | 4 | +10.4 | +9.6 | +7.5 | +0.0 |
| 4a1 0e | `4a1 0c0 (4a1 0c0)` | 14 | +24.3 | +12.6 | +20.7 | +17.0 |
| 4a1 2e | same | 1 | +0.0 | +2.1 | +13.8 | +1.4 |
| 4a1 4e | `4a1 0c0` | 2 | +11.5 | +15.4 | +0.0 | +0.0 |
| 2c3 0e | `2c3 4b2 (4a1 0c0)` | 14 | +26.8 | +20.6 | +8.1 | +5.3 |
| 2c3 6e | `2c3 4b2 (4a1 0c0)` | 2 | +25.2 | +0.0 | +0.0 | +0.0 |
| 2c3 8e | `2c3 4b2 (4a1 0c0)` | 13 | +26.0 | +20.8 | +7.2 | +2.9 |
| 0c4 0e | same | 1 | +0.0 | +2.3 | +0.0 | +0.0 |
| 0c4 6e | same | 1 | +0.0 | +0.0 | +1.3 | +0.5 |
| 4c3 0e | same | 1 | +0.0 | +0.3 | +0.0 | +0.0 |
| 4b2 0e | same | 1 | +0.0 | +1.0 | +2.9 | +0.1 |
| 4b5 0e | `4b5 2c4 2c3 (4b2 4a1 0c0)` | 2 | +4.7 | +0.0 | +0.0 | +0.0 |

*Pooled list's first route: place in own list* is where the pooled list's first route lands in the subset × edges list (computed to 60 routes). The same rows within +1, own minus pooled, in points:

| Subset | After 1 route (own − pooled, points) | After 2 routes | After 3 routes | After 5 routes |
|---|---|---|---|---|
| 0c0 0e | +0.0 | +46.8 | +50.0 | +50.3 |
| 0c0 4e | +0.0 | +0.0 | +3.1 | +0.0 |
| 0c0 6e | +30.5 | +10.4 | +2.7 | +1.7 |
| 0c0 8e | +9.4 | +0.0 | +0.0 | +0.0 |
| 2c5 0e | +0.0 | +1.4 | -0.0 | -0.0 |
| 2c5 8e | +0.0 | +0.2 | -0.0 | +0.0 |
| 2c4 0e | +21.6 | +0.0 | +0.0 | +0.0 |
| 2c4 8e | +0.0 | +2.7 | +0.0 | +0.1 |
| 0c3 0e | +0.0 | +0.0 | +0.3 | +0.2 |
| 0c3 8e | +0.0 | +0.0 | +0.2 | +0.1 |
| 4a2 0e | +31.8 | +0.0 | +10.1 | +1.2 |
| 4a2 2e | +12.1 | +0.0 | +3.7 | +0.5 |
| 4a2 4e | +16.9 | +12.0 | +0.1 | +0.0 |
| 4a1 0e | +35.7 | +14.8 | +25.0 | +10.5 |
| 4a1 2e | +0.0 | +2.0 | +9.0 | +0.5 |
| 4a1 4e | +8.4 | +13.2 | +0.7 | +0.0 |
| 2c3 0e | +34.9 | +11.6 | +2.4 | +0.9 |
| 2c3 6e | +22.4 | +0.0 | +0.0 | +0.1 |
| 2c3 8e | +34.3 | +11.7 | +2.4 | +0.7 |
| 0c4 0e | +0.0 | +1.2 | +1.3 | +0.0 |
| 0c4 6e | +0.0 | +0.0 | +0.0 | +0.1 |
| 4c3 0e | +0.0 | +0.3 | +1.1 | +0.0 |
| 4b2 0e | +0.0 | +0.0 | +1.4 | +0.5 |
| 4b5 0e | +4.0 | +0.0 | +0.0 | +0.0 |

And the shares the gains come from, own list and pooled list on the same DRs (share finding the optimal after that many routes):

| Subset | List | Optimal found, 1 route | Optimal found, 2 routes | Optimal found, 3 routes | Optimal found, 5 routes |
|---|---|---|---|---|---|
| 0c0 0e | own | 42.5% | 84.4% | 92.6% | 93.0% |
| 0c0 0e | pooled | 42.5% | 42.7% | 42.7% | 42.7% |
| 0c0 4e | own | 44.9% | 57.8% | 61.5% | 65.1% |
| 0c0 4e | pooled | 44.9% | 57.8% | 59.5% | 64.4% |
| 0c0 6e | own | 40.8% | 53.7% | 60.2% | 65.7% |
| 0c0 6e | pooled | 18.1% | 42.2% | 54.9% | 62.1% |
| 0c0 8e | own | 53.5% | 70.1% | 77.1% | 78.3% |
| 0c0 8e | pooled | 46.6% | 70.1% | 77.1% | 77.8% |
| 2c5 0e | own | 77.8% | 86.5% | 89.6% | 91.8% |
| 2c5 0e | pooled | 77.8% | 82.3% | 89.6% | 91.8% |
| 2c5 8e | own | 77.6% | 86.0% | 91.0% | 92.5% |
| 2c5 8e | pooled | 77.6% | 84.2% | 90.9% | 92.4% |
| 2c4 0e | own | 70.1% | 85.9% | 88.6% | 88.9% |
| 2c4 0e | pooled | 42.7% | 85.9% | 88.6% | 88.8% |
| 2c4 8e | own | 77.7% | 89.5% | 91.5% | 92.9% |
| 2c4 8e | pooled | 77.7% | 83.0% | 91.5% | 92.7% |
| 0c3 0e | own | 85.5% | 94.2% | 96.6% | 97.2% |
| 0c3 0e | pooled | 85.5% | 94.2% | 94.2% | 96.6% |
| 0c3 8e | own | 87.3% | 94.8% | 96.1% | 96.8% |
| 0c3 8e | pooled | 87.3% | 94.8% | 94.9% | 95.3% |
| 4a2 0e | own | 29.1% | 40.4% | 44.4% | 50.3% |
| 4a2 0e | pooled | 4.0% | 33.1% | 44.4% | 47.8% |
| 4a2 2e | own | 42.2% | 67.8% | 76.8% | 81.4% |
| 4a2 2e | pooled | 34.0% | 67.8% | 76.8% | 79.6% |
| 4a2 4e | own | 60.9% | 72.2% | 79.1% | 85.3% |
| 4a2 4e | pooled | 50.5% | 62.6% | 71.6% | 85.3% |
| 4a1 0e | own | 33.5% | 46.5% | 54.6% | 66.5% |
| 4a1 0e | pooled | 9.2% | 33.9% | 33.9% | 49.5% |
| 4a1 2e | own | 38.8% | 58.8% | 70.5% | 78.2% |
| 4a1 2e | pooled | 38.8% | 56.6% | 56.6% | 76.7% |
| 4a1 4e | own | 33.6% | 50.3% | 60.6% | 69.5% |
| 4a1 4e | pooled | 22.1% | 34.9% | 60.6% | 69.5% |
| 2c3 0e | own | 46.3% | 67.0% | 75.1% | 85.5% |
| 2c3 0e | pooled | 19.5% | 46.4% | 67.0% | 80.2% |
| 2c3 6e | own | 66.1% | 73.3% | 76.7% | 79.8% |
| 2c3 6e | pooled | 40.9% | 73.3% | 76.7% | 79.8% |
| 2c3 8e | own | 46.3% | 67.2% | 74.5% | 81.3% |
| 2c3 8e | pooled | 20.3% | 46.4% | 67.3% | 78.3% |
| 0c4 0e | own | 83.2% | 86.8% | 87.6% | 88.3% |
| 0c4 0e | pooled | 83.2% | 84.5% | 87.6% | 88.3% |
| 0c4 6e | own | 81.8% | 83.7% | 85.4% | 87.3% |
| 0c4 6e | pooled | 81.8% | 83.7% | 84.1% | 86.8% |
| 4c3 0e | own | 70.8% | 78.4% | 83.3% | 88.6% |
| 4c3 0e | pooled | 70.8% | 78.1% | 83.3% | 88.6% |
| 4b2 0e | own | 36.5% | 51.1% | 61.0% | 72.4% |
| 4b2 0e | pooled | 36.5% | 50.1% | 58.1% | 72.2% |
| 4b5 0e | own | 60.8% | 84.2% | 92.6% | 93.0% |
| 4b5 0e | pooled | 56.1% | 84.2% | 92.6% | 93.0% |

A gain of +0.0 means both lists are equal up to that route; a small negative one means the pooled order happens to be ahead (greedy isn't optimal). Gains under a point or so are within what fitting the own list to the same 25,000 states gives you anyway.

Where knowing the edge count changes what to try first. Each row is a subset × edges; the two share columns are the DRs where the own list and the pooled list find the optimal after that many routes:

| Subset × edges | Own list starts with | After | Own list finds the optimal | Pooled list finds the optimal | Note |
|---|---|---|---|---|---|
| 0c0 0e | `0c0 4a1 0c0`, then `0c0` (the DR is already HTR) | 2 routes | 84.4% | 42.7% | the pooled order never tries it |
| 0c0 6e | `0c0 4a1 (0c0)`, switching before the last qt | 1 route | 40.8% | 18.1% | pooled first route is only 6th here |
| 0c0 8e | the same switch first | 1 route | 53.5% | 46.6% | |
| 2c4 0e | linear, `2c4 2c3 4b2 4a1 0c0` | 1 route | 70.1% | 42.7% | pooled switches at 2c3 |
| 2c3 0e | switch at 4b2, `2c3 4b2 (4a1 0c0)` | 1 route | 46.3% | 19.5% | |
| 2c3 6e | the same | 1 route | 66.1% | 40.9% | |
| 2c3 8e | the same | 1 route | 46.3% | 20.3% | |
| 4a2 0e | the 4b3 regression `4a2 4b3 4a2 4a1 (0c0)` | 1 route | 29.1% | 4.0% | |
| 4a2 2e | the same | 1 route | 42.2% | 34.0% | |
| 4a2 4e | linear, `4a2 4a1 0c0` | 3 routes | 79.1% | 71.6% | |
| 4a1 0e | `4a1 0c0 (4a1 0c0)` | 3 routes | 54.6% | 33.9% | pooled first route is 14th |
| 4a1 4e | the 1qt route `4a1 0c0` | 2 routes | 50.3% | 34.9% | |
| 4a1 2e | the pooled first route, but a different third | 3 routes | 70.5% | 56.6% | |

On 2c3 2e and 4e the linear route stays first. On 4a2 the pooled first route, `4a2 4a1 (0c0)`, is first on none of the three edge counts.

Where it doesn't matter: on 2c5, 0c3, 0c4, 4c3, 4c4 and 4b2 the first route is the same for every edge count, and the own list gains at most 4.2 points at any step. The pooled list is fine there, and on 2c4 2e to 8e too.

**Pooled over edges.** One list per corner subset, edge counts pooled by their real frequency, as a summary. Each row is a corner subset and its first three budget-2 routes:

| Subset | Try first | Then | Then |
|---|---|---|---|
| 0c0 | `0c0 4a1 0c0` | `0c0 4a1 (0c0)` | `0c0 4a1 0c0 4a1 (0c0)` (mirror: `0c0 4a1 (4a2 4a1 0c0)`) |
| 2c5 | `2c5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 (4a1 0c0)`) | `2c5 2c4 2c3 4b2 4a1 0c0` | `2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 4a1 (0c0)`) |
| 2c4 | `2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b3 4a2 4a1 (0c0)`) | `2c4 2c3 4b2 4a1 0c0` | `2c4 2c3 4b2 (4a1 0c0)` (mirror: `2c4 4b3 4a2 (4a1 0c0)`) |
| 0c3 | `0c3 4a2 (4a1 0c0)` (mirror: `0c3 4a2 4a1 (0c0)`) | `0c3 4a2 4b3 4a2 4a1 (0c0)` (mirror: `0c3 4a2 (4a1 4b2 4a1 0c0)`) | `0c3 4a2 4b3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4a1 4b2 (4a1 0c0)`) |
| 4a2 | `4a2 4a1 (0c0)` | `4a2 4b3 4a2 4a1 (0c0)` (mirror: `4a2 4a1 (4b2 4a1 0c0)`) | `4a2 4a1 4b2 4a1 0c0` |
| 4a1 | `4a1 4b2 4a1 0c0` | `4a1 0c0 (4a1 0c0)` (mirror: `4a1 4a2 4a1 (0c0)`) | `4a1 0c0` |
| 2c3 | `2c3 4b2 4a1 0c0` | `2c3 4b2 (4a1 0c0)` (mirror: `2c3 4b2 4a1 (0c0)`) | `2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c3 2c4 2c3 4b2 4a1 (0c0)`) |
| 0c4 | `0c4 4a3 4b2 (4a1 0c0)` | `0c4 4a3 (4a2 4a1 0c0)` (mirror: `0c4 4a3 4b2 4a1 (0c0)`) | `0c4 4a3 4b2 4a1 0c0` |
| 4c3 | `4a3 4b2 (4a1 0c0)` (mirror: `4b3 4a2 4a1 (0c0)`) | `4b3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4a3 0c4 4a3 4b2 (4a1 0c0)`) | `4a3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b3 2c4 2c3 4b2 (4a1 0c0)`) |
| 4c4 | `4b4 4a3 4b2 (4a1 0c0)` (mirror: `4a4 0c3 4a2 (4a1 0c0)`) | `4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b4 4a3 0c4 4a3 4b2 (4a1 0c0)`) | `4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b4 2c5 4b4 4a3 (4a2 4a1 0c0)`) |
| 4b2 | `4b2 4a1 0c0` | `4b2 2c3 4b2 4a1 (0c0)` (mirror: `4b2 2c3 (4b2 4a1 0c0)`) | `4b2 2c3 4b2 4a1 0c0` |
| 4b5 | `4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b5 2c4 2c3 4b2 4a1 (0c0)`) | `4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b5 2c4 4b3 4a2 (4a1 0c0)`) | `4b5 2c4 2c3 4b2 4a1 0c0` |

The shares, same rows: the DRs where the first 1, 2, 3 or 5 routes find the optimal, where the same three find a finish within +1, and for comparison three routes with no limit on HTR length:

| Subset | Optimal found, 1 route | Optimal found, 2 routes | Optimal found, 3 routes | Optimal found, 5 routes | Within +1, same 3 routes | Optimal found, 3 routes, no HTR limit |
|---|---|---|---|---|---|---|
| 0c0 | 42.3% | 55.9% | 60.9% | 65.8% | 86.4% | 97.4% |
| 2c5 | 72.8% | 85.5% | 91.4% | 93.1% | 98.9% | 98.8% |
| 2c4 | 66.0% | 83.5% | 88.4% | 89.3% | 98.7% | 98.9% |
| 0c3 | 74.4% | 88.8% | 89.3% | 90.1% | 99.1% | 99.4% |
| 4a2 | 41.6% | 64.1% | 73.2% | 81.6% | 90.8% | 93.6% |
| 4a1 | 29.3% | 44.8% | 58.0% | 72.2% | 84.3% | 97.1% |
| 2c3 | 53.5% | 75.7% | 78.0% | 80.1% | 96.1% | 99.5% |
| 0c4 | 83.8% | 85.1% | 86.3% | 88.2% | 97.6% | >99.9% |
| 4c3 | 64.3% | 71.3% | 75.0% | 80.0% | 94.2% | 99.0% |
| 4c4 | 68.1% | 75.0% | 78.4% | 81.8% | 96.1% | 99.2% |
| 4b2 | 37.6% | 53.3% | 62.6% | 71.4% | 88.0% | 97.2% |
| 4b5 | 64.7% | 87.4% | 93.7% | 93.9% | 99.6% | 99.5% |

How to read a row, with 4c3 (the pooled row; 4c3 2e and 4e start the same way). Try `4a3 4b2 (4a1 0c0)` first: on the 4a3 side, one qt to 4b2, switch, and on the other side 4a1 and HTR. The same moves read the other way round are its mirror, `4b3 4a2 4a1 (0c0)`: start on the 4b3 side, qt to 4a2, qt to 4a1, switch for the last qt. Every split of a finish has a mirror like this, and the table names both. As classes they aren't the same, since each also collects other finishes (only 646 of 21,552 mirror pairs cover exactly the same states), so the share is for the reading named first. With HTRs up to two over the shortest, that route alone finds the optimal on 64.3% of 4c3. Then the b side, `4b3 2c4 2c3 (4b2 4a1 0c0)`, then the regression through 2c3 on the a side. The b-side route through 4a2 read linearly, `4b3 4a2 4a1 0c0`, is fifth.

There are more in the [worked examples](examples.html); here's one, replayed:

```
L2 U2 F2 L2 D' F2 R2 D' L2 B2 U2 B2 D' R2 // 4c3 4e, 14 optimal
B2 R2 D' // first route, normal
(F2 L2 U2 F2 D' L2 U R2 U2 R2 B2) // then inverse, HTR in 10
```

What the pooled table says, subset by subset. Each row is a corner subset, the share where its budget-2 checklist finds the optimal after that many routes, and what those routes are:

| Corner subset | Optimal found | After | What to try |
|---|---|---|---|
| 0c3 | 89.3% | 3 routes | `4a2 4e`, then switch |
| 0c4 | 86.3% | 3 routes | `4a3 4b2`, switch |
| 2c4 | 88.4% | 3 routes | down the 2c chain to 2c3, switch at 2c3 (or one step earlier), or linear |
| 2c5 | 91.4% | 3 routes | the same |
| 4b5 | 93.7% | 3 routes | the same |
| 4c3 | 80.0% | 5 routes | the first route does most of the work |
| 4c4 | 81.8% | 5 routes | the same |
| 2c3 | 80.1% | 5 routes | the same |
| 0c0 | 69.4% | 8 routes | the optimal is spread over many routes |
| 4a1 | 74.6% | 8 routes | the same |
| 4b2 | 75.0% | 8 routes | the same |

- **0c3, 0c4, 2c4, 2c5, 4b5** are the easy ones for a checklist, and the routes are what Daichi's cheat sheet says.
- **4c3, 4c4, 2c3** need four or five routes for 80%.
- **4b2, 4a1, 0c0** are where checklists struggle, and where bounding does better (section 8). On 4b2 the 2qt route `4b2 4a1 0c0` comes first but alone finds only 37.6%; the regressions through 2c3 come next.
- **Within +1** the same three routes reach 86.4% on 0c0, 84.3% on 4a1, 88.0% on 4b2, and 90% or more on the other 9. If you only need a finish within one move of optimal, three routes are enough nearly everywhere. (At +1 a route counts if any of its finishes within +1 has an HTR within the budget, which may be shorter than on its optimal finishes.)

**The budget.** The same checklists built for budget 0 (only the shortest HTRs), 1, 2 and no limit. Each row is a corner subset; each cell is the share where the first route finds the optimal with that budget:

| Subset | Budget 0 (shortest HTRs only) | Budget 1 | Budget 2 | No HTR limit |
|---|---|---|---|---|
| 0c0 | 20.5% | 32.0% | 42.3% | 59.2% |
| 2c5 | 20.0% | 48.1% | 72.8% | 95.3% |
| 2c4 | 17.4% | 40.5% | 66.0% | 94.2% |
| 0c3 | 47.7% | 68.0% | 74.4% | 76.0% |
| 4a2 | 18.1% | 31.3% | 41.6% | 50.6% |
| 4a1 | 12.8% | 16.8% | 29.3% | 79.1% |
| 2c3 | 16.3% | 33.6% | 53.5% | 82.5% |
| 0c4 | 34.6% | 61.7% | 83.8% | 90.0% |
| 4c3 | 25.8% | 46.7% | 64.3% | 72.6% |
| 4c4 | 26.2% | 51.0% | 68.1% | 72.9% |
| 4b2 | 18.8% | 30.0% | 37.6% | 73.5% |
| 4b5 | 14.8% | 39.7% | 64.7% | 98.0% |

The same after three routes:

| Subset | Budget 0 (shortest HTRs only) | Budget 1 | Budget 2 | No HTR limit |
|---|---|---|---|---|
| 0c0 | 32.8% | 48.1% | 60.9% | 97.4% |
| 2c5 | 30.8% | 69.3% | 91.4% | 98.8% |
| 2c4 | 30.9% | 64.7% | 88.4% | 98.9% |
| 0c3 | 53.2% | 78.3% | 89.3% | 99.4% |
| 4a2 | 35.0% | 59.6% | 73.2% | 93.6% |
| 4a1 | 23.3% | 41.0% | 58.0% | 97.1% |
| 2c3 | 31.0% | 57.2% | 78.0% | 99.5% |
| 0c4 | 37.5% | 67.4% | 86.3% | >99.9% |
| 4c3 | 32.8% | 56.8% | 75.0% | 99.0% |
| 4c4 | 31.6% | 57.4% | 78.4% | 99.2% |
| 4b2 | 26.6% | 43.8% | 62.6% | 97.2% |
| 4b5 | 31.1% | 69.8% | 93.7% | 99.5% |

With only the shortest HTRs, no subset gets past 53% with three routes: you have to write HTRs one or two moves longer than the shortest. With no limit, the first route alone covers most states. That's the *every route works if you allow the HTR to be long* effect of section 3, not a reason to try only one route.

**Cheap and marginal routes.** After the third route, each further route adds at most 8.4 points, and less than 3 points in 91.7% of the checklists (subsets × edges and corner subsets, budget 2). Routes 4 to 8 only pay at the margin. If you have time for more on 0c0, 4a1 and 4b2, a second DR or bounding (section 8) is probably the better use of it.

**Edge counts along the route.** It also matters how often you go through, say, 4b2 4e rather than 4b2 2e. Every state on a route has its own bad-edge count (counted as for the subset × edges groups), so a corner route splits into edge paths. From 2c3 2e, `2c3 4b2 4a1 0c0` is one of

```
2c3 2e → 4b2 2e → 4a1 4e → 0c0
2c3 2e → 4b2 4e → 4a1 4e → 0c0
```

Below, a DR *can pass* an intermediate subset if some route (after a qt, before HTR) that finds its optimal with budget 2 goes through it. One DR can pass several, so the edge columns add up to more than 100%. First the reverse view, over all DRs. Each row is an intermediate subset and a target: the share of DRs that can pass it, then, of those, the share that can pass it with each edge count.

| Intermediate subset | Target | DRs that can pass it | of those, via 0e | via 2e | via 4e | via 6e | via 8e |
|---|---|---|---|---|---|---|---|
| 4b2 | optimal | 80.5% | 4.6% | 92.6% | 56.4% | – | – |
|  | within +1 | 94.3% | 9.8% | 97.6% | 76.2% | – | – |
| 2c3 | optimal | 54.0% | 0.44% | 66.3% | 76.8% | 22.7% | 0.46% |
|  | within +1 | 74.2% | 1.3% | 78.6% | 87.3% | 39.3% | 1.2% |
| 4a1 | optimal | 86.8% | 0.091% | 3.9% | >99.9% | – | – |
|  | within +1 | 97.8% | 0.22% | 8.1% | >99.9% | – | – |
| 4a2 | optimal | 32.0% | 0.15% | 13.1% | 94.6% | – | – |
|  | within +1 | 52.0% | 0.26% | 26.2% | 94.8% | – | – |
| 4c3 | optimal | 33.9% | 5.9% | 64.6% | 67.0% | – | – |
|  | within +1 | 54.7% | 8.6% | 75.2% | 76.0% | – | – |

In short. Each row is an intermediate subset; each cell is the share, of the DRs that can pass it at all, that can pass it with that edge count:

| Intermediate subset | 0e | 2e | 4e | 6e |
|---|---|---|---|---|
| 4b2 | 4.6% | 92.6% | 56.4% | |
| 4a1 | 0.091% | 3.9% | >99.9% | |
| 4a2 | 0.15% | 13.1% | 94.6% | |
| 2c3 | 0.44% | 66.3% | 76.8% | 22.7% |
| 4c3 | 5.9% | 64.6% | 67.0% | |

So the 4b2 you go through is mostly 4b2 2e, the 4a1 before HTR is 4a1 4e, the 4a2 is 4a2 4e, 2c3 is split, and 4c3 is 2e or 4e about equally.

Per starting subset × edges, the share that can pass each intermediate subset at all, then per edge count, is in appendix A (one table per intermediate subset). What you can take from it, one row per starting subset × edges:

| From | Mostly through | Share that can pass it | Other edge count | Share that can pass it |
|---|---|---|---|---|
| 2c3 2e | 4b2 2e | 69.2% | 4b2 4e | 46.3% |
| 2c3 0e | 4b2 4e | 88.6% | 4b2 2e | 58.3% |
| 2c3 8e | 4b2 4e | 85.7% | 4b2 2e | 57.3% |
| 2c4 0e | 2c3 4e | 89.1% | 2c3 2e | 1.1% |
| 2c4 8e | 2c3 4e | 93.8% | 2c3 2e | 4.4% |
| 0c4 8e | 4b2 2e | 86.5% | 4b2 4e | 12.8% |
| 4b2 4e, regressing | 2c3 4e | 40.8% | 2c3 2e | 28.8% |
| | | | 2c3 6e | 13.1% |

From 0c4 in general the 4b2 is mostly 4b2 2e; 0c4 8e is the example in the table.

**Do edge paths make a better checklist?** No. An edge path lies inside its corner route, so a list of edge paths finds less per route; what it shows is how far a corner route is spread over edge paths. Built the same way (greedy, budget 2, per subset × edges). Each row is a kind of list; each cell is the share of all DRs where it finds the optimal:

| List | 1 route | 3 routes |
|---|---|---|
| Edge paths | 39.4% | 62.5% |
| Corner routes | 61.3% | 81.0% |

The first edge path is a piece of the first corner route (or its mirror) on 47 of 48 subset × edges (not on 4a2 2e), so it doesn't change what to try. How many edge paths it takes to find everything the first corner route finds:

- **one**, on 18 subset × edges (0c0 0e, 0c0 2e, 0c0 4e, 0c0 6e, 0c0 8e, 0c3 0e, 0c3 2e, 0c3 6e, 0c3 8e, 4a2 4e, 4a1 0e, 4a1 4e, 2c3 0e, 2c3 8e, 4c3 0e, 4b2 0e, 4b2 2e, 4b2 4e): there the corner route effectively is one edge path;
- **two**, on 14;
- **up to eight**, on 2c5 2e, 2c5 4e, 2c5 6e. There the first corner route is spread over many edge paths, and aiming for one edge count at each step would cost you most of it.

So check the corner route and take whatever edge count you land on. The edge-path checklists themselves, eight routes per subset × edges, are in appendix A, **computer only**: an answer key, not a list to check in an attempt.

Two more replayed examples, the first route on 2c4 and the 4b2 regression. The first is a no-limit instance: its HTR of 13 is longer than budget 2 allows on that DR.

```
R2 F2 R2 D2 F2 D F2 D R2 U' L2 D F2 U2 // 2c4 4e, 14 optimal
(R2 F2 R2 D2 F2 D) // inverse: 2c4 to 2c3
U2 F2 D' L2 U R2 D' F2 // then normal
```

```
B2 L2 U F2 D' R2 U L2 B2 L2 D2 B2 R2 D' // 4b2 4e, 14 optimal
D // to 2c3, switch
(B2 L2 U F2 D' R2 U L2 B2 L2 D2 B2 R2) // then inverse
```

**The last DR move** shifts every route about equally and changes no checklist (section 7).

---

## 5. The existing sheets, cell by cell

**Levi Gibson's *allcases*.** Its paths are linear chains in Jay's qt names, one path per state; the shares add to 1 per subset. Asked whether ties between optimal solutions were factored in, the answer was "Not factored in" ([13 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1295060590074531922)). Pick one leave-slice optimal per state at random among the optimal finishes (5,000 states per subset × edges, seed 7) and you get the sheet back, over 1,895 paths:

| Random optimal per state | Mean difference from the sheet (points) | Correlation |
|---|---|---|
| leave slice | 0.3 | 0.991 |
| E slice solved | 0.6 | 0.974 |

So its shares are *the path of one optimal found by a solver*, a third reading between *some optimal* and *every optimal*. Where the sheet and the random pick differ, the sheet has the fewer-qt path more often, by more than the 5,000-state sample explains:

| Cell | Rows | Sheet | One optimal at random |
|---|---|---|---|
| 4b2 4e | 2qt | 39.5% | 33.5% |
| 4a1 4e | 5qt | 6.1% | 9.6% |

So the solver behind it probably preferred fewer quarter turns among equal-length finishes.

**2qt(a) and 2qt(b).** The old names say "2qt(a)" and "2qt(b)" where today's say 4a2 and 4b2. The server worked most of this out: Tzak on *allcases*' letters, "good one, the bad one can't turn into 2c3" ([13 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1295059271746326699)); its author, "And yes, a and b are swapped in line with the old naming scheme", "a is the R U2 R’ case" ([8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315360877255327785), [8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315360910327414835)); Zagros, "I think a and b might be flipped" ([8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315341879910600775)). What the sheets themselves show:

- Aedan Bryant's *HTR Subset Stats* lists a trigger for every case. Played on a cube, its "2qt (a)" triggers are 4b2 0e, 4b2 2e and 4b2 4e, and its "2qt (b)" ones are 4a2. For example:

  ```
  U R2 U   // the sheet's 2qt (a) 4C2E trigger
  ```
- *allcases* has no triggers, but its own data settles it: its "2qt(a)" rows go to a "3qt 2c" case with one qt (30 rows do), none of its 113 "2qt(b)" rows does, and only 4b2 can reach 2c3 with one quarter turn. So 2qt(a) is 4b2 there too, as its author and Tzak said.
- The *Extra Quarter-Turn Stats* sheet has the letters the other way round: its own example triggers put "2qt(b)" on 4b2. That part is new.

So mrauo's "Only 1/3 of 2q 4b2e cases use 2qt for optimal wtf" ([8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315341544206631054)) read the *allcases* row "2qt(b) 4c2e", which is 4a2 2e. Zagros answered "I think a and b might be flipped" and "Should be 60%" ([8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315341879910600775), [8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315341893856657430)), which is right: with one optimal at random, the 4b2 2e path is 2qt on 53.7% of states, 4a2 2e on 27.7%.

**Aedan Bryant's *HTR Subset Stats*** (1,000 states per subset): the mean optimal and the mean NISS HTR are within 0.06 of mine on 39 of its 47 rows. Of the others, four are rows the sheet carries with the numbers of another row, a copy slip:

| Sheet row | Has the numbers of |
|---|---|
| 4qt 4E | 4qt 2E |
| 4qt 4C2E | 4qt 4C |
| 5qt 2C | 4qt 4C4E |
| 5qt 4C | 5qt 2C8E |

The two fake-HTR rows are off by 0.74 (0c3 0e) and 0.56 (0c4 0e) in the mean optimal: the sheet's states were built around one trigger ("25 random move HTR scramble + trigger + 25 random move HTR scramble", [29 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069288666981220492)), which for these two covers only part of the subset. The remaining two differ by at most 0.08. Its "Linear HTR" is the normal side only, not the better of the two: on 4b2 2e the sheet has 6.213, the normal side 6.156, the better side 5.654. Its "No E Difference" column already said that solving the slice costs well under a move for most subsets.

**Levi Gibson's *Extra Quarter-Turn Stats*.** Its "% with extra qts" is *every leave-slice optimal uses more qts than the corners need* ("The percentages are for if the dr CAN be solved optimally without extra qts", [29 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1301010836646531176)). On that reading it agrees with my sample on every comparable row within sampling error (its 0c0 0e row counts only the states already in HTR, half of 0c0 0e; the other half is U D' times HTR).

**rodneykinney's *DR Finish Move Counts*** (10,000 solutions). rodneykinney's summary "2 qt or less is 17%, but 3 qt or less is 45%" ([2 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1037387616313675806)) is right: exactly 17.6% and 45.7% over the 40,320 corner arrangements. The 4qt and 5qt shares are further off, more than its sample size explains:

| Corner qts | Sheet | Exact |
|---|---|---|
| 4 | 32.9% | 35.2% |
| 5 | 22.5% | 19.1% |

So its DRs probably weren't uniform DR states; the sheet doesn't say how they were made. Its extra-qt columns use one optimal per state and fall between my fewest-qt and most-qt readings.

**Joba's and DougCube's exact tables** are reproduced exactly: the optimal distribution of every subset (473 cells of subset and length), the shortest DR-to-HTR length per subset, and the 663,552 HTR states with mean 10.13432557.

---

## 6. Shortest HTR against the optimal

**Linear against NISS.** The shortest HTR per subset: with NISS (moves on both sides counted), linear on the better side, and on the normal side alone (what Aedan Bryant's sheet calls linear), and how often NISS is shorter. Sampled, 25,000 per subset × edges:

| Subset | Shortest NISS HTR, mean (moves) | Shortest linear, better side (moves) | Normal side (moves) | NISS = linear | NISS 1 shorter | NISS 2+ shorter |
|---|---|---|---|---|---|---|
| 0c0 | 5.25 | 5.80 | 6.16 | 66.6% | 18.1% | 15.3% |
| 2c5 | 9.25 | 9.93 | 10.34 | 41.1% | 49.1% | 9.7% |
| 2c4 | 8.00 | 8.46 | 8.88 | 61.1% | 31.9% | 7.0% |
| 0c3 | 8.90 | 10.50 | 10.84 | 23.1% | 24.5% | 52.4% |
| 4a2 | 7.26 | 8.15 | 8.80 | 50.5% | 24.6% | 24.9% |
| 4a1 | 5.72 | 5.91 | 6.48 | 83.3% | 13.8% | 2.9% |
| 2c3 | 6.61 | 6.98 | 7.38 | 72.3% | 20.2% | 7.5% |
| 0c4 | 8.02 | 9.39 | 9.57 | 12.8% | 46.7% | 40.5% |
| 4c3 | 7.67 | 8.48 | 8.92 | 42.8% | 37.9% | 19.3% |
| 4c4 | 9.09 | 10.07 | 10.48 | 28.8% | 47.8% | 23.4% |
| 4b2 | 6.13 | 6.34 | 6.85 | 83.8% | 12.3% | 3.9% |
| 4b5 | 9.12 | 9.76 | 10.03 | 46.4% | 43.9% | 9.7% |
| all DRs | 7.80 | 8.38 | 8.80 | 55.8% | 32.3% | 11.9% |

So, for rodneykinney's question ([30 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069660273356587082)):

- NISS saves nothing on about half of all DRs, one move on a third, and two or more on 11.9%.
- On 0c3 and 0c4 (fake HTR corners) it saves two or more on 52.4% and 40.5%.
- The two linear sides tie on 36.9% of DRs and differ by two or more on 16.9%.

**Which HTR the optimal uses.** For each DR, the shortest HTR among all readings of all its optimal finishes, against the DR's shortest NISS HTR (sampled, 25,000 per subset × edges, edges pooled by size; optimal finishes, NISS readings). Each row is a subset: the first four columns split its DRs by how much longer that HTR is than the shortest, then the 9-move columns and the mean number of moves after HTR:

| Subset | Optimal uses a shortest HTR | Best is 1 longer | 2 longer | 3 or more longer | Every optimal needs 9+ | … though a sub-9 HTR exists | Post-HTR moves, mean |
|---|---|---|---|---|---|---|---|
| 0c0 | 34.1% | 17.2% | 19.0% | 29.7% | 22.1% | 22.1% | 5.39 |
| 2c5 | 32.4% | 39.2% | 22.1% | 6.2% | 97.1% | 9.0% | 4.05 |
| 2c4 | 31.6% | 34.7% | 24.4% | 9.3% | 71.6% | 46.1% | 4.52 |
| 0c3 | 53.5% | 25.8% | 11.8% | 8.8% | 80.8% | 10.9% | 4.76 |
| 4a2 | 37.2% | 30.1% | 17.6% | 15.0% | 49.1% | 34.2% | 4.92 |
| 4a1 | 29.7% | 24.1% | 21.7% | 24.5% | 25.0% | 24.9% | 5.16 |
| 2c3 | 31.2% | 27.3% | 23.4% | 18.1% | 34.8% | 33.8% | 4.96 |
| 0c4 | 37.5% | 30.2% | 21.4% | 10.9% | 71.3% | 48.0% | 4.55 |
| 4c3 | 36.9% | 30.4% | 20.3% | 12.4% | 59.7% | 43.0% | 4.70 |
| 4c4 | 34.6% | 33.1% | 21.8% | 10.5% | 92.1% | 13.1% | 4.20 |
| 4b2 | 30.0% | 24.0% | 22.5% | 23.5% | 31.7% | 31.7% | 5.04 |
| 4b5 | 31.4% | 39.2% | 23.7% | 5.8% | 96.9% | 8.0% | 4.11 |
| all DRs | 32.9% | 31.8% | 22.5% | 12.8% | 65.2% | 29.7% | 4.59 |

Some optimal goes through a shortest HTR on only a third of DRs. On the other two thirds you have to find an HTR at least a move longer than the shortest to get the optimal, and on 35.3% at least two longer. That's why the checklists need budget 2 (section 4). On 0c3 a shortest HTR is used most often (53.5%); on 2c4 and 4b5 about as often as on 4b2. *Post-HTR moves* is the rest of that optimal: 4.59 moves on average, more on low-qt subsets, as tseitsei89 described ([29 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1466457851286524068)).

**Nine-move HTRs.** On 65.2% of all DRs every optimal finish needs an HTR of 9 moves or more in every reading. On 29.7% of DRs that's the case even though the DR has an HTR of 8 or less. By the length L of a DR's shortest NISS HTR, the share of DRs where some optimal uses an HTR of exactly L moves (all DRs, sampled; the rows cover 99.2% of DRs, the rest having a shortest NISS HTR of 3, 11 or 0 to 2):

| Shortest NISS HTR (L) | Share of DRs | An optimal uses an L-move HTR |
|---|---|---|
| 4 | 1.1% | 44.6% |
| 5 | 4.5% | 35.0% |
| 6 | 12.7% | 29.2% |
| 7 | 20.5% | 30.2% |
| 8 | 25.3% | 31.9% |
| 9 | 25.5% | 32.6% |
| 10 | 9.6% | 42.0% |

The chance that the shortest HTRs carry an optimal is about a third whatever their length, 6 to 9 alike. What a single 9-move HTR is worth once you've written many is a different question, and this doesn't measure it (there are many more 9-move HTRs than 6-move ones). An example where every optimal needs an HTR of 9 or more, replayed:

```
U2 L2 U F2 L2 R2 U' B2 R2 U' L2 U2 B2 // 2c3 2e, 13 optimal
```

The shortest HTR in any reading of any of its 2 optimal finishes is 10 moves.

---

## 7. Extra quarter turns, and the last DR move

**Extra quarter turns.** The share of DRs where every optimal uses more quarter turns than the corner subset needs, where some optimal does, and where every leave-slice optimal does (the *Extra Quarter-Turn Stats* reading). Sampled, 25,000 per subset × edges, edges pooled by size:

| Subset | Every optimal uses extra qts | Some optimal does | Every leave-slice optimal does |
|---|---|---|---|
| 0c0 | 99.4% | 99.6% | 99.3% |
| 2c5 | 3.2% | 17.5% | 3.0% |
| 2c4 | 5.8% | 33.2% | 4.8% |
| 0c3 | 24.0% | 43.2% | 24.4% |
| 4a2 | 49.4% | 73.3% | 43.3% |
| 4a1 | 82.5% | 92.7% | 73.8% |
| 2c3 | 17.5% | 53.6% | 11.2% |
| 0c4 | 10.0% | 43.6% | 9.3% |
| 4c3 | 27.4% | 64.1% | 25.3% |
| 4c4 | 27.1% | 65.1% | 27.4% |
| 4b2 | 55.0% | 82.5% | 40.9% |
| 4b5 | 1.9% | 13.2% | 1.4% |
| all DRs | 21.7% | 49.0% | 18.1% |

The three readings are far apart, and the numbers quoted on the server fit different ones.

- rodneykinney: "57% of the time, the optimal solution uses 4QT for a 2QT corner case" ([13 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1063355084697784371)). Radek B asked which reading ("Did you consider all optimals or just one that you had generated?", [13 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1063365972846706728)); there's no answer in the export (rodneykinney moved on to a thread, [13 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1063499873665695819)).
- Lichi Fang: "over 60% the optimal solution for htr subset 2qt(a) 4c4e … use 4qt rather than 2qt" ([6 Aug 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1137835695721939094)), read off the first optimal nissy gave ("these are just the first solution nissy gave for optimal", Aedan Bryant, [6 Aug 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1137864582036209824)).

Each reading on the cases they were talking about:

| Reading | 4a2 and 4b2: 4qt or more | 4b2 4e: 4qt |
|---|---|---|
| every optimal | 53.9% | 63.7% |
| some optimal | 80.7% | 86.9% |
| one optimal picked at random | 69.0% | 77.6% |
| one leave-slice optimal at random | 56.3% | 66.5% |

The 57% fits a random leave-slice optimal or *every optimal*. Both quotes fit.

On 4b2 4e no optimal uses only 2 qts on 63.7% of states, and on those the 2qt route never gives the optimal. In this one no optimal finish follows the 2qt route `4b2 4a1 0c0` in any reading:

```
F2 D F2 D L2 D2 L2 F2 L2 D L2 U // 4b2 4e, 12 optimal
U' L2 D' L2 F2 L2 D2 L2 D' F2 D' F2 // one of its 2 optimal finishes
```

Both optimal finishes, that one and the other, were re-read on the sticker model at every split.

**Half turns before the first qt.** Kai Cui's 2c3 2e stats ([5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457432898633840): "baically 85 percent chance that you dont need to check 2 ht before first qt"). Share where some optimal starts its first qt after 0 or 1 half turns:

| | On one of the two sides | On the normal side alone |
|---|---|---|
| 2c3 2e | 82.7% | 62.0% |
| All DRs | 92.0% | 76.4% |

**The last DR move.** With the last move either way (the better of X and X·R2; sampled, 25,000 per subset × edges, edges pooled by size; optimal lengths from the exact table):

| Subset | Mean optimal (moves) | Mean, last move either way (moves) | One shorter | Same | Optimal 15+ | 15+ either way |
|---|---|---|---|---|---|---|
| 0c0 | 12.28 | 11.94 | 34.2% | 31.6% | 0.27% | 0.030% |
| 2c5 | 14.33 | 14.00 | 33.3% | 33.5% | 44.9% | 26.8% |
| 2c4 | 13.65 | 13.32 | 32.5% | 35.2% | 14.6% | 5.3% |
| 0c3 | 14.45 | 14.10 | 35.1% | 30.2% | 53.0% | 35.4% |
| 4a2 | 13.35 | 13.02 | 32.7% | 34.3% | 10.6% | 4.3% |
| 4a1 | 12.42 | 12.08 | 33.3% | 33.0% | 0.13% | 0.010% |
| 2c3 | 12.93 | 12.60 | 32.6% | 34.6% | 1.2% | 0.14% |
| 0c4 | 13.67 | 13.35 | 31.6% | 36.7% | 10.8% | 2.4% |
| 4c3 | 13.49 | 13.17 | 32.0% | 35.5% | 9.3% | 2.8% |
| 4c4 | 14.40 | 14.09 | 30.6% | 38.6% | 49.4% | 30.8% |
| 4b2 | 12.68 | 12.35 | 33.5% | 33.5% | 0.21% | 0.010% |
| 4b5 | 14.28 | 13.96 | 32.5% | 35.5% | 42.3% | 22.1% |
| all DRs | 13.58 | 13.26 | 32.5% | 35.1% | 19.7% | 10.3% |

X·R2 is one move shorter on a third of DRs and never more than one shorter, in every subset alike; the first study had this exactly (*A third of the time the other DR is one shorter*). Yura Riabov's estimate in 2024 was 1/6 of a move ("so yeah, should be 1/6", [6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248337792673779803)), from "2/3(chance of dr solution ending in 1 of 4 moves) * 1/4(chance of that move being the right one)". Yura called it "very rough" and added "i doubt it will be more than a half move difference with 1 move inverted" ([6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248372741602545674)). The half-move ceiling holds; the 1/6 is half the real gain of 0.325.

Example, replayed. Think of the first line as the end of a DR on U/D whose last move was a quarter turn of R. Turning that move the other way is the same as adding R2 at the end:

```
R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U // as written: 13 optimal
R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U R2 // R2 added: 12 optimal
B2 U' R2 L2 D L2 U L2 U2 R2 U' F2 // its optimal finish
```

For routes the variation changes nothing in kind: every route's share goes up by about the same amount, and no checklist gains a route. It's worth its 0.32 moves on every subset, so write both finishes' DRs down, but don't let it change which routes you try.

Aedan Bryant's sheet has a "qt break" column; Yura Riabov explained it as "you know that qt break is dr plus one move that can be inverted, right?" ([25 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1376198140943929415)). One extra move that can go either way costs 0.68 moves over the plain optimal on average. That's a little more than the "around 0.5 worse, rather than 1 as you might expect" trangium described ([6 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1469487095407186093)).

---

## 8. DR bounding

The method of Levi Gibson's *DR Bounding* doc: "1. Find many reductions to the 1qt 4c4e subset … 2. For each case, create a lower bound of how good the solution can be … 3. Start checking the 1qt cases from best to worst … 4. Once you find a solution, cross off all the 1QT cases that can not be solved in less moves than the solution you found." rodneykinney's *Advanced DR Bounding* sharpens the bounds and adds 2qt.

What I measure here is the method's ceiling. Write every reduction to 1q of at most R moves (on normal, on inverse, or split between them, section 3) and finish each reduced state optimally, with however many quarter turns that takes: how often is one of them the optimal finish of the DR, and how many reductions is that? The search over reductions is exact. Reductions are counted the way a solver writes them (each side's sequence empty or ending in a quarter turn), exactly, by table. Sampled: the first 4,000 states per subset × edges; shares have standard errors of at most 0.5 points per corner subset.

Each row is a subset; each cell is the share of DRs where some reduction to 1q of at most R moves leads to an optimal finish:

| Subset | Optimal found, R ≤ 3 | R ≤ 4 | R ≤ 5 | R ≤ 6 | R ≤ 7 |
|---|---|---|---|---|---|
| 0c0 | 86.0% | 91.5% | 93.9% | 96.9% | 99.1% |
| 2c5 | 0% | 0% | 0% | 10.9% | 45.8% |
| 2c4 | 0% | 3.5% | 25.7% | 59.5% | 84.6% |
| 0c3 | 12.7% | 35.0% | 65.5% | 81.7% | 85.3% |
| 4a2 | 64.3% | 76.6% | 80.0% | 85.2% | 92.3% |
| 4a1 | 62.3% | 75.6% | 88.6% | 95.4% | 98.0% |
| 2c3 | 20.5% | 48.1% | 71.1% | 86.2% | 94.2% |
| 0c4 | 0% | 10.2% | 37.0% | 63.5% | 84.3% |
| 4c3 | 15.7% | 37.5% | 60.1% | 75.1% | 86.8% |
| 4c4 | 0% | 3.7% | 17.6% | 38.8% | 58.2% |
| 4b2 | 43.7% | 58.0% | 74.1% | 88.8% | 97.6% |
| 4b5 | 0% | 0% | 0% | 10.3% | 48.1% |
| all DRs | 14.1% | 24.9% | 40.6% | 59.3% | 78.3% |

How many reductions that is, the mean number of reductions of at most R moves per DR, same rows. Counts for R = 7 aren't reported: the table that counts them was checked against brute force only up to 5 moves on every subset and up to 7 on 40 states of 0c0, so for R ≤ 7 the table above gives the share only (that comes from the exact search).

| Subset | Reductions on average, R ≤ 3 | R ≤ 4 | R ≤ 5 | R ≤ 6 |
|---|---|---|---|---|
| 0c0 | 156 | 1,238 | 8,763 | 63,868 |
| 2c5 | 0 | 0 | 0 | 237 |
| 2c4 | 0 | 11 | 228 | 2,503 |
| 0c3 | 5 | 38 | 399 | 3,628 |
| 4a2 | 26 | 207 | 1,463 | 10,942 |
| 4a1 | 80 | 623 | 4,901 | 36,474 |
| 2c3 | 16 | 140 | 1,080 | 9,111 |
| 0c4 | 0 | 22 | 330 | 3,075 |
| 4c3 | 8 | 66 | 559 | 4,959 |
| 4c4 | 0 | 6 | 83 | 800 |
| 4b2 | 26 | 233 | 1,978 | 16,087 |
| 4b5 | 0 | 0 | 0 | 229 |
| all DRs | 10 | 89 | 748 | 6,242 |

Other targets, same rows: a finish within +1 with reductions of at most 4; a finish of 12 or better with reductions of at most 5 (for DRs that have one); and reductions to 2q of at most 3 moves, with how many there are:

| Subset | Within +1 found, R ≤ 4 | 12 or better found, R ≤ 5 | To 2q, R ≤ 3: optimal found | To 2q, R ≤ 3: reductions on average |
|---|---|---|---|---|
| 0c0 | 98.9% | 51.0% | >99.9% | 384 |
| 2c5 | 0% | 0% | 0% | 0 |
| 2c4 | 8.5% | 3.7% | 46.5% | 71 |
| 0c3 | 52.1% | 2.6% | 98.4% | 101 |
| 4a2 | 93.6% | 15.9% | >99.9% | 181 |
| 4a1 | 89.2% | 43.6% | 98.9% | 304 |
| 2c3 | 78.8% | 21.1% | 95.7% | 152 |
| 0c4 | 19.0% | 3.4% | 77.9% | 123 |
| 4c3 | 66.1% | 8.4% | 93.4% | 102 |
| 4c4 | 6.4% | 0.59% | 41.6% | 36 |
| 4b2 | 84.5% | 28.0% | >99.9% | 248 |
| 4b5 | 0% | 0% | 0% | 0 |
| all DRs | 38.5% | 10.3% | 60.4% | 102 |

What it says:

**Which subsets suit it depends on R.** Each row is a subset; each cell is the share where bounding finds the optimal:

| Subset | R ≤ 4 | R ≤ 6 |
|---|---|---|
| 0c0 | 91.5% | 96.9% |
| 4a2 | 76.6% | 85.2% |
| 4a1 | 75.6% | 95.4% |
| 4b2 | 58.0% | 88.8% |
| 2c3 | 48.1% | 86.2% |

So at R ≤ 6, 4a1, 4b2 and 2c3 overtake 4a2. On 2c5 and 4b5 no reduction of 5 or less reaches 4a1 4e at all (it takes at least 6), and 4c4 and 2c4 are close to that.

**Each extra move of reduction costs a lot.** The number of reductions grows 7.3 to 11.0 times from 5 to 6 moves. The mean number of reductions per DR, over all DRs:

| | R ≤ 4 | R ≤ 5 | R ≤ 6 |
|---|---|---|---|
| Reductions on average | 89 | 748 | 6,242 |

With the bounds doing their job you only finish a few of them, but you still write them, and NISS-trace them.

**2q needs much shorter reductions.** At most 3 moves to a 2q state reaches the optimal on 60.4% of all DRs, against 14.1% for 1q. But each 2q state still needs its own finish found by hand, and that's the hard part bounding at 1q avoids.

**Within +1** is much easier: at most 4 moves gives a finish within +1 on 38.5% of DRs.

**The one-quarter-turn reading** (the reduction, then a finish with exactly one quarter turn, which is what JTuu's simulation counted) finds less. Each row is a subset; each cell is the share where some reduction of at most 4 finds the optimal, read each way:

| Subset | One-qt finish | Any finish |
|---|---|---|
| 2c3 | 39.8% | 48.1% |
| 4b2 | 42.4% | 58.0% |

**Against the checklists.** How often does bounding find the optimal per subset, and how many reductions does that take? Here's the smallest R for which bounding finds the optimal on 80% of a subset, with the reductions that is, against how many routes the checklist of section 4 needs for 80%, one row per corner subset:

| Subset | Bounding: smallest R for 80% | Reductions on average at that R | If not reached: found at R ≤ 7 | Checklist routes for 80%, budget 2 | If not reached: found after 8 routes | Routes for 80%, no HTR limit |
|---|---|---|---|---|---|---|
| 0c0 | 3 | 156 |  | more than 8 | 69.4% | 2 |
| 2c5 | more than 7 |  | 45.8% | 2 |  | 1 |
| 2c4 | 7 | not reported |  | 2 |  | 1 |
| 0c3 | 6 | 3,628 |  | 2 |  | 2 |
| 4a2 | 5 | 1,463 |  | 5 |  | 3 |
| 4a1 | 5 | 4,901 |  | more than 8 | 74.6% | 2 |
| 2c3 | 6 | 9,111 |  | 5 |  | 1 |
| 0c4 | 7 | not reported |  | 1 |  | 1 |
| 4c3 | 7 | not reported |  | 5 |  | 2 |
| 4c4 | more than 7 |  | 58.2% | 4 |  | 2 |
| 4b2 | 6 | 16,087 |  | more than 8 | 75.0% | 2 |
| 4b5 | more than 7 |  | 48.1% | 2 |  | 1 |

Bounding gets to 80% with short reductions on 0c0 (3) and 4a1 (5), and to about 80% on 4a2 (5: 80.0%, on the line in every population of section 12). Those are where the budget-2 checklist struggles (0c0 and 4a1 stop short of 80% after eight routes). On 4b2 bounding needs every reduction up to 6, about 16,087 of them, where the checklist stops at 75.0%. On 2c4, 2c5, 4b5, 0c3, 0c4, 4c3 and 4c4 one to five routes reach 80%, and bounding needs 6 or 7 moves of reduction or doesn't get there by 7. A route and a reduction aren't the same amount of work, so this only compares them in kind.

**For a human the bounding column is mostly out of reach.** Each extra move of reduction multiplies the reductions by about eight, and in an attempt you write tens, maybe a couple of hundred (R ≤ 4 is about 89 on average). So only the 0c0 entry (R = 3, about 156 reductions) is a practical recommendation. Every entry with R of 5 or more, thousands of reductions, is **computer only**: it shows where the optimal lies, not how to find it. Plan an attempt with the R ≤ 4 column of the first table above.

**Levi Gibson's verdicts per subset.** After "lots and lots of solves" ([8 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1370092390362382348)): "0c0: Yes", "4a2: yes yes yes amazing muah chief's kiss", for 4a1 "if you get a 4a1 case randomly, bound it. Otherwise it's not great. For the 2e/6e case it's not great because you 99% of the time you want to find a 0c0 or 4b2 trigger", for 4b2 "just check the really short ones, and then just try triggers for the rest", for 2c3 "I only use it for the 6e subset now. Triggers will get you optimal usually for 2e and 4e", and "Bounding is actually REALLY good for 4c3". Row by row, bounding with every reduction of at most 4 and 5 moves against the first three and five budget-2 routes (4,000 states per subset × edges for bounding, 25,000 for the routes). Each row is a subset × edges; each cell is the share where that method finds the optimal:

| Subset | Bounding, R ≤ 4 | Bounding, R ≤ 5 | Checklist, 3 routes | Checklist, 5 routes |
|---|---|---|---|---|
| 0c0 0e | 98.7% | >99.9% | 92.6% | 93.0% |
| 0c0 2e | 96.4% | 97.0% | 70.2% | 73.0% |
| 0c0 4e | 91.3% | 94.4% | 61.5% | 65.1% |
| 0c0 6e | 86.2% | 88.8% | 60.2% | 65.7% |
| 0c0 8e | >99.9% | >99.9% | 77.1% | 78.3% |
| 4a1 0e | 44.5% | 59.2% | 54.6% | 66.5% |
| 4a1 2e | 50.2% | 77.6% | 70.5% | 78.2% |
| 4a1 4e | >99.9% | >99.9% | 60.6% | 69.5% |
| 4a2 0e | 76.9% | 77.0% | 44.4% | 50.3% |
| 4a2 2e | 71.1% | 73.2% | 76.8% | 81.4% |
| 4a2 4e | 81.5% | 86.3% | 79.1% | 85.3% |
| 4b2 0e | 77.1% | 83.6% | 61.0% | 72.4% |
| 4b2 2e | 63.0% | 79.6% | 59.0% | 66.3% |
| 4b2 4e | 52.5% | 68.6% | 66.8% | 76.0% |
| 2c3 0e | 34.9% | 52.3% | 75.1% | 85.5% |
| 2c3 2e | 52.1% | 78.0% | 80.2% | 80.8% |
| 2c3 4e | 46.2% | 69.5% | 78.1% | 79.9% |
| 2c3 6e | 50.3% | 70.5% | 76.7% | 79.8% |
| 2c3 8e | 32.2% | 48.9% | 74.5% | 81.3% |
| 4c3 0e | 32.9% | 63.1% | 83.3% | 88.6% |
| 4c3 2e | 39.3% | 62.3% | 75.1% | 80.1% |
| 4c3 4e | 36.2% | 57.9% | 74.4% | 79.6% |

Levi Gibson's verdicts against those rows, one row per corner subset:

| Subset | Verdict | Why |
|---|---|---|
| 0c0 | **agrees** | bounding is far ahead on every edge count |
| 4a2 | **agrees on 0e** | bounding finds 76.9% against 44.4% on 0e; the routes are a little ahead on 2e and level on 4e |
| 4a1 | **agrees** | on 4a1 4e (the case Levi Gibson would bound) bounding finds nearly every optimal; on 0e and 2e the routes are as good or better |
| 4b2 | **partly** | on 4b2 0e and 2e bounding with reductions of 4 already beats three routes, so it's worth writing more than the really short reductions; on 4b2 4e the routes are ahead |
| 2c3 | **agrees for 2e and 4e** (routes ahead), **not for 6e** | the routes are ahead on 6e too |
| 4c3 | **does not agree** | the routes are ahead on every edge count, by 12.8 points or more against reductions of 5 |

On 4c3, Levi Gibson's reason was the b side ("On the b corners side there are sooooo many finecky ways to reduce to 4a1 in very few moves"); these numbers count both sides together.

**Levi Gibson's 75 to 80%.** Asked how many reductions to check, Levi Gibson wrote "I like to check all sub-5 reductions. This can be done super quick and gets optimal like 75% of the time, and it gets optimal +1 the rest of the time" ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311670582601060354)), "sub-5" being "4 or less" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051485760163880)). Later, asked "Would it be around 80 percent?" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051034906038323)): "yeah something like that I'd guess" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051081831780434)), "for 2c3 that is" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051112253329439)), adding "The only thing it really misses is a bunch of half turns into a 5-move trigger, so check that in addition to bounding" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051209158525018)). The subsets Levi Gibson named for full bounding were 4a2 and 2c3 ("I don't use it fully for any subsets other than 4a2 and 2c3", [28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311671487379279872)). Bounding alone, every reduction of at most R moves. Each row is a target and R; each cell is the share of the subset's DRs where it is found:

| | 2c3 | 4a2 |
|---|---|---|
| Optimal, R ≤ 4 | 48.1% | 76.6% |
| Optimal, R ≤ 4, 2c3 2e only | 52.1% | |
| Reductions on average, R ≤ 4 (a count, not a share) | 140 | 207 |
| Within +1, R ≤ 4 | 78.8% | 93.6% |
| Optimal, R ≤ 5 | 71.1% | 80.0% |

On 4a2 the 75% holds (Levi Gibson had just written "for the 4a2 subset I use full DR Bounding", [28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311669869900464138)), but within +1 it's only the share in the *Within +1* row, not every DR. For 2c3 both halves are off for bounding alone: the optimal comes from a reduction of 4 or less on under half of 2c3, and on 21.2% not even +1 does. Levi Gibson does add the triggers ("For 2c3 2e and 4e I do full DR Bounding + checking the 5-move triggers, and that seems to catch everything", [28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311674286389334026)); I haven't measured that combination. There's an example in the errata: a 2c3 2e where the best any reduction of at most 4 gives is +2.

**JTuu's simulation** for Kai Cui's question ([3 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313597166270550137)): 2,000 2c3 2e states with Tzak's definitions, "4 move reduction to 4c4e just means you can strip off <=4 moves total from either end and be left with a single qt" ([3 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313620671607345254)) and "7 move linear htr means if you drop 7 moves on either end, are you left with just half turns" ([3 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313620835046789282)). That's the one-quarter-turn reading. JTuu's result ([4 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313766061325156462)) against mine on uniform 2c3 2e states, same definitions. Each row is an option; JTuu's column is quoted, mine is the share of DRs:

| Option | JTuu | Uniform 2c3 2e |
|---|---|---|
| linear HTR in 7 | "946/2000 (47.30%)" | 38.1% |
| 4a1 in 4 | "1071/2000 (53.55%)" | 44.7% |
| both together | "1293/2000 (64.65%)" | 55.3% |
| with 8 and 5 | "1721/2000 (86.05%)" | 80.3% |

Every number of mine is 5.8 to 9.4 points lower than JTuu's, far more than the standard error of 2,000 states (about 1.1 points). JTuu didn't say how the states were drawn. Two things in Kai Cui's generator would explain a gap: its states are random half turns around one trigger ("(random ht 100-110) (U R2 U R2 U) (random ht 100-110)", [5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457154635665448)), not a uniform 2c3 2e, and it allowed the last DR move to be inverted ("this accounts for inverting last move of dr", [5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457154635665448)). I can't reproduce it exactly. The order of the four options is the same in both.

---

## 9. FakeMMAP's reduction-length bound

**What FakeMMAP proposed.** From [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531394667773962): "Let's say we're looking for a finish in M moves (or less), assuming we're only allowed to use N>1 qts. We want to know how long our reductions to 1q should be, in order to find that solution. Let R be the biggest possible length of a reduction to 1q you have to check".

The inputs:

- **A** and **B**: the optimal HTR on normal and on inverse.
- **C**: "the shortest possible HTR in the subset" ("so 2c3 2e would have C=5, 4b2 0e would have C=6").
- **$\alpha_i$**, the section bounds: "Numbering these sections from 0 to N, let \alpha_i be the bound for the ith section. For example 4a3 2e would have \alpha_1=3, because you have to to the 4b2 parity fix."

Then [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369): "R is the max of the following", five families of terms over sets S of consecutive windows, solved "with Fourier-Motzkin elimination by hand". And [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475), "multi-qt DR bounding... well, sort of": lower bounds on M once every reduction shorter than R' has failed. On those lower bounds FakeMMAP added "I don't know how useful these bounds really are, I have to put in the numbers to see if there are situations where the typical bound is M \geq 11, rather than M \geq 7 lol." ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533429198553178)). This section puts in the numbers, for the upper bound R too.

**The model behind the five terms.** A finish with $N$ quarter turns is $h_0\, q_1\, h_1 \ldots q_N\, h_N$: sections $h_i$ of $s_i \geq \alpha_i$ half turns, length $L = N + \sum_i s_i \leq M$. FakeMMAP's term 1 ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369)), "M-\alpha_i-\alpha_{i+1}-1 (basically leaving those two as the 1q finish, unlikely to be the maximum, unless M is VERY small)", fixes the windows. Window $i$ is sections $i$ and $i+1$ around quarter turn $q_{i+1}$, and the 1q reduction that leaves it as the finish is $L - 1 - s_i - s_{i+1}$ moves (the moves before it on normal, the ones after it on inverse). Three blocks of the finish are HTRs, so you get three constraints:

- **A**, all but the last section: $L - s_N \geq A$.
- **B**, all but the first section, read on inverse: $L - s_0 \geq B$.
- **C**, the middle $q_1\, h_1 \ldots q_N$, without the first and last sections: $L - s_0 - s_N \geq C$.

The middle is a linear HTR of the DR you have after the first section's half turns. A half turn, before or after, never changes the subset or the bad-edge count (proved in Lean over all 40,320 corner and 40,320 U/D-edge arrangements and all six half turns: `half_turns_keep_subset_data` and `labels_keep`, lean/FakeBound/FakeBound/Subset.lean). So the right bound is the shortest linear HTR anywhere in the subset × edges, which is C exactly as FakeMMAP defined it (2c3 2e: 5, 4b2 0e: 6; Lean `fake_C_examples`, same file).

Every term is the sum of the window bounds over a set $S$ of windows covering a run of sections, plus one constraint on the total of that run. Two windows $i$, $i+1$ share section $i+1$, which gets counted twice. The five terms, one row each:

| Term | Sections covered | Windows S | Constraint used |
|---|---|---|---|
| 1 | one window | a single window | none |
| 2 | 0 to $N$ | $S \subset \{0, \ldots, N-1\}$ | the length |
| 3 | 0 to $N-1$ | $\{0, \ldots, N-2\}$ | A |
| 4 | 1 to $N$ | $\{1, \ldots, N-1\}$ | B |
| 5 | the middle, 1 to $N-1$ | $\{1, \ldots, N-2\}$ | C |

For $N = 2$ no window avoids both end sections, which is why FakeMMAP says to "just discard this constraint". Nothing in the derivation needs a NISS HTR.

The Lean theorems cited here are in the study's folder lean/FakeBound (Lean 4, no Mathlib, no `sorry`), in the files FakeBound/Finish.lean, Formula.lean, Counter.lean and Subset.lean, and Corrections/Examples.lean.

*Fixed 12 Nov 2026.* Until then this section said C must be the shortest NISS HTR. That was wrong: it modelled C as bounding every finish minus one middle section, which is a NISS HTR of the DR itself and not FakeMMAP's constraint.

**How I tested it.** First $\alpha_i$ for every corner path that occurs: the fewest half turns section i needs over every corner arrangement following the path. For 4a3 4b2 4a1 HTR that's 0,3,1,0, FakeMMAP's $\alpha_1 = 3$, and the study's Lean certificate re-derives every $\alpha$ (appendix B). Then for every sampled state, every corner path of its optimal (or +1, or ≤ 10, 11, 12) finishes, and the shortest reduction such a finish needs. I compared that need with R four ways:

1. the formula of [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369) as written, the largest of its terms;
2. the same without term 1;
3. the smallest term, with term 2's signs and the $\alpha$ index fixed (see (a));
4. the exact optimum of the same model, *computer only*: the largest shortest-reduction any whole-number section lengths allowed by $\alpha$, A, B and C can force, solved by enumeration instead of by hand.

Each row is a target finish length. It gives the number of (state, path) cases, the mean R in moves for each of the four readings with the corner path known, and the mean reduction the finishes actually needed. Sampled, 25,000 states per subset × edges.

| Target | (state, path) cases | Mean R, as written (largest term) | Without term 1 | Smallest term | Exact model | Mean reduction needed |
|---|---|---|---|---|---|---|
| optimal | 1,914,809 | 12.1 | 11.1 | 8.9 | 8.9 | 7.0 |
| optimal + 1 | 5,973,495 | 13.6 | 12.8 | 10.4 | 10.4 | 8.2 |
| 10 or better | 25,283 | 8.5 | 7.6 | 5.1 | 5.1 | 3.8 |
| 11 or better | 87,631 | 9.5 | 8.6 | 6.3 | 6.3 | 4.5 |
| 12 or better | 322,330 | 10.6 | 9.7 | 7.1 | 7.1 | 5.3 |

Same rows: the longest reduction any finish needed, and the share of cases where each reading of R was too short:

| Target | Longest reduction needed (moves) | R too short: as written | Smallest term | Exact model |
|---|---|---|---|---|
| optimal | 14 | 0% | 0% | 0% |
| optimal + 1 | 15 | 0% | 0% | 0% |
| 10 or better | 8 | 0% | 0% | 0% |
| 11 or better | 9 | 0% | 0% | 0% |
| 12 or better | 9 | 0% | 0% | 0% |

**(a) What is proved.** Each verdict below is a Lean theorem, with its file.

**C is the subset's shortest linear HTR, as FakeMMAP defined it.** Term 5 follows from $L - s_0 - s_N \geq C$ (`term5_sound`, FakeBound/Finish.lean), and half turns keep the subset × edges (`labels_keep`, above). A smaller C, like the DR's own shortest NISS HTR, is still a valid input but only weakens R. A bound on the middle block and a bound on the finish minus one middle section are different statements, and neither implies the other (`C_placement`, FakeBound/Counter.lean).

**Every sum needs $\alpha_{i+1}$, not $\alpha_i$**, in the terms of [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369) and in the lower bounds of [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475). Windows $i$ and $i+1$ share section $i+1$, and that's the section counted twice (`cover_sum`, FakeBound/Finish.lean). Counterexample to $\alpha_i$ (`alpha_i_fails`, FakeBound/Counter.lean). The row is one finish: its $\alpha$ per section, its length, its section lengths $s_i$, and the 1q reduction each window needs:

| Corner path | $\alpha$ per section | Finish | Section lengths | 1q reduction per window |
|---|---|---|---|---|
| 4b2 4a3 4b2 4a1 0c0 | 0, 0, 3, 1, 0 | 14 | 2, 1, 3, 1, 3 | 10, 9, 9, 9 |

So a 9-move reduction is needed. With $\alpha_i$ the smallest term is 8, whatever A, B and C are, and the first bound of [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475) claims $28 \geq 29$. (c) has a real DR on which the lower bound fails.

**R as written is sound, but only because term 1 is among the terms.** [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369) says "R is the max of the following". The largest term is never too short, with any signs and either $\alpha$ index (`Rmax_sound`, FakeBound/Formula.lean), because it's at least term 1, about $M - 1$. So R as written is safe to use, just loose. In the sample it was never too short in any case, at any target.

**The smallest term is sound for every finish** (`Rmin_sound`, FakeBound/Formula.lean), with term 2 as derived and $\alpha_{i+1}$. It's the bound the derivation gives, and it fits FakeMMAP's own remarks in [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369): term 1 is "unlikely to be the maximum, unless M is VERY small", which is true of the smallest term and false of the largest, and "You only need to consider minimal such S's". It isn't always the exact worst case (`Rmin_not_tight`, FakeBound/Counter.lean): with $N = 3$, $\alpha = 0$, $M = 5$, $A = B = 5$ and $C = 0$ it gives 3, but every finish allowed has a reduction of at most 2, because the terms use A, B and C one at a time, never together. On the sample it equals the exact model in >99.9% of cases at the optimum, and was never too short.

**Read as the smallest term, term 2 as printed is unsound: its signs are flipped.** The derivation gives

$$\frac{(|S|-1)M + (N-|S|) - \sum \alpha}{|S|};$$

[8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369) prints "\frac{(|S|-1)M-(N-|S|)+\sum_{i edge} \alpha_i}{|S|}", which renders as

$$\frac{(|S|-1)M-(N-|S|)+\sum_{i\ \mathrm{edge}} \alpha_i}{|S|}.$$

 The first bound of [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475) is the same inequality solved for M, and it has the derived signs, so the two messages disagree with each other. Counterexample (`printed_term2_fails`, FakeBound/Counter.lean), read as the table above:

| Corner path | $\alpha$ per section | Finish | Section lengths | 1q reduction per window |
|---|---|---|---|---|
| 4a1 0c0 4a1 0c0 | 0 | 10 | 0, 3, 0, 4 | 6, 6, 5 |

Term 2 as printed with $S = \{0, 2\}$ gives 4, whatever A, B and C are; derived, it gives 5. With the printed $\alpha_i$ as well it's still 4 (`literal_min_fails`). On the sample, the smallest term with term 2 and the index exactly as printed is too short on 9.2% of cases at the optimum.

A real DR where it bites, replayed ($N = 3$; every optimal finish takes the path in the table):

```
F2 D2 R2 D' R2 U2 B2 D' L2 U2 F2 U L2 R2 // 0c3 2e
R2 L2 U' F2 U2 L2 D B2 U2 R2 D R2 D2 F2 // optimal finish
```

Its finish, read as the tables above:

| Corner path | $\alpha$ per section | Finish | Section lengths | 1q reduction per window |
|---|---|---|---|---|
| 0c3 4a2 4a1 HTR | 0, 3, 3, 0 | 14 | 2, 3, 3, 3 | 8, 7, 7 |

Term 2 with $S = \{0, 2\}$ as printed gives 6.5, so 6. Derived, it gives 7.5, so 7. The arithmetic from the sections on is checked in Lean (`witness_0c3`); the state's optimum and its paths come from the exact table and the sample, not from Lean.

The other choices are readings, not corrections:

- A and B are the shortest *linear* HTR on each side.
- C is per subset × edges, as in FakeMMAP's examples.
- $\alpha$ counts corners only, so it stays a valid lower bound.
- R is taken over finishes of M moves or fewer and rounded down.
- FakeMMAP's advice to use C + 1, A + 1, B + 1 in an attempt is not modelled.
- Five families aren't everything Fourier–Motzkin elimination gives (for example A and B together raise C to $A + B - M$), which is why the smallest term sits a move above the exact model in a few cases.

**(b) It doesn't prune at the reduction lengths solvers write.** Each row is a case; each cell is the mean R in moves for that reading:

| Case | As written | Without term 1 | Smallest term | Exact model |
|---|---|---|---|---|
| at the optimum, corner path known | 12.1 | 11.1 | 8.9 | 8.9 |
| at the optimum, path unknown | 12.7 | 12.4 | 10.6 | 10.6 |
| 12 or better, path unknown | 11.2 | 11.0 | 9.0 | 9.0 |

*Path unknown* is the worst case over the subset's corner paths, with the DR's own A and B. What the finishes actually needed:

- at the optimum, path known: 7.0 on average and 14 at most;
- at the optimum, path unknown: the longest need per subset × edges is 11.2 on average, so none of them lets you skip a reduction you would have checked anyway;
- hunting a fixed M is the same story (last row): the longest need per subset × edges averages 8.5 and is 9 at most.

Solvers check reductions of 4 to 6 moves (section 8), and a bound that says *go to 9 or 10* never tells you to stop earlier than that. Where the bound could help is the other direction, proving that a short M is impossible, and that's (c).

**rodneykinney's tables.** rodneykinney asked for "some tables for specific cases" ([9 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491873063531188324)). They cover each subset × edges at target $M = 10$, 11, 12, and give R when nothing is read off the DR (A, B and C all set to the subset's shortest linear HTR, worst case over the subset's corner paths) three ways: from the formula without term 1, from the exact model (*computer only*), and as the longest reduction any sampled finish of that length needed. Each is one number per subset, so you can use it in an attempt. At $M = 12$ for a few subsets (all in appendix A), each row a subset × edges and each cell a reduction length in moves:

| Subset | R from the formula without term 1 | R from the exact model | Longest reduction needed |
|---|---|---|---|
| 2c3 2e | 11 | 9 | 8 |
| 4b2 4e | 11 | 9 | 9 |
| 4c3 2e | 11 | 9 | 8 |
| 4a2 2e | 10 | 9 | 9 |
| 2c4 4e | 10 | 9 | 9 |

**(c) The multi-qt lower bounds, and one index.** The first bound of [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475) is

$$M \geq \frac{|S|(R'+1) - N + \sum \alpha_i}{|S| - 1},$$

the sum "over all i's such that i, i+1 are both in S" (as in [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369)). Windows $i$ and $i+1$ share section $i+1$, so the section counted twice is $\alpha_{i+1}$, not $\alpha_i$. That follows from term 1's numbering alone (`cover_sum`).

As written, the bounds are wrong in 923 of 1,914,809 cases at the optimum (subsets 0c4, 4b2, 4c3, 4c4): 904 times the first bound and 19 times the one with B. With $\alpha_{i+1}$ they never fail (0 cases), and they're proved valid for every finish, along with the "very stupid bounds" (`lower_free`, `lower_A`, `lower_B`, `lower_C`, `lower_stupid`, FakeBound/Finish.lean).

A real DR where the index matters, replayed:

```
D2 F2 L2 U' B2 U' L2 U2 B2 U' L2 D R2 D2 // 0c4 0e
D2 R2 D' L2 U B2 U2 L2 U B2 U L2 F2 D2 // optimal finish
```

Its finish, read as the tables above:

| Corner path | $\alpha$ per section | Finish | Section lengths | 1q reduction per window |
|---|---|---|---|---|
| 0c4 4a3 4b2 4a1 HTR ($N = 4$) | 0, 1, 3, 1, 0 | 14 | 2, 1, 3, 1, 3 | 10, 9, 9, 9 |

So every reduction shorter than $R' = 9$ fails. With $S = \{0, 2, 3\}$:

- as written, the bound adds $\alpha_2 = 3$ and gives $M \geq 14.5$, so 15, but the finish is 14;
- with $\alpha_3 = 1$ it gives 13.5, so 14.

This one is checked in Lean end to end: the optimum (`dr_optima_correct`, from the first study's proved table), the finish (`dr_solutions_valid`), its corner path, $\alpha$, sections and reductions, and both inequalities (`index_example`, `index_example_arith`, Corrections/Examples.lean).

**The typical bound, FakeMMAP's question.** I took every (state, corner path) at the optimum with at least two quarter turns, set $R'$ to the shortest 1q reduction a finish of that path needs (so every shorter reduction has failed), and computed the corrected bounds ($\alpha_{i+1}$, C the subset's shortest linear HTR). They sit next to the "very stupid bounds" $M \geq A + \alpha_N$, $M \geq B + \alpha_0$ and the optimum itself (sampled, 25,000 per subset × edges; each corner subset's rows count every (state, path) case). Each row is a corner subset; the bounds and the optimum are in moves:

| Subset | (state, path) cases | Corrected bound, median | Corrected bound, mean | Trivial bound, median | Trivial bound, mean | Mean optimum |
|---|---|---|---|---|---|---|
| 0c0 | 183,502 | 8 | 7.99 | 6 | 6.01 | 12.44 |
| 2c5 | 181,404 | 12 | 12.07 | 11 | 10.91 | 14.61 |
| 2c4 | 195,143 | 11 | 10.98 | 9 | 9.37 | 13.92 |
| 0c3 | 182,652 | 13 | 12.73 | 11 | 10.93 | 14.55 |
| 4a2 | 137,305 | 12 | 11.57 | 10 | 10.03 | 13.85 |
| 4a1 | 129,339 | 10 | 9.69 | 8 | 7.73 | 12.96 |
| 2c3 | 226,253 | 11 | 10.50 | 9 | 8.64 | 13.44 |
| 0c4 | 169,721 | 12 | 11.56 | 10 | 9.89 | 13.84 |
| 4c3 | 120,789 | 11 | 10.96 | 9 | 9.30 | 13.68 |
| 4c4 | 129,413 | 12 | 12.33 | 11 | 11.14 | 14.69 |
| 4b2 | 136,970 | 9 | 9.74 | 8 | 7.55 | 13.05 |
| 4b5 | 122,318 | 11 | 11.68 | 10 | 10.05 | 14.52 |

How often the corrected bound beats the trivial one, reaches the optimum, and is 11 or more, as a share of the subset's cases:

| Subset | Bound above the trivial one | Bound reaches the optimum | Bound 11 or more |
|---|---|---|---|
| 0c0 | 72.5% | 0.73% | 14.8% |
| 2c5 | 66.9% | 3.1% | 87.4% |
| 2c4 | 73.4% | 2.7% | 61.0% |
| 0c3 | 84.4% | 8.9% | 94.9% |
| 4a2 | 78.8% | 6.2% | 76.3% |
| 4a1 | 78.1% | 3.8% | 36.4% |
| 2c3 | 81.5% | 3.9% | 54.0% |
| 0c4 | 82.0% | 4.9% | 83.9% |
| 4c3 | 80.8% | 3.7% | 60.4% |
| 4c4 | 71.5% | 7.5% | 93.2% |
| 4b2 | 82.9% | 1.8% | 40.4% |
| 4b5 | 76.4% | 2.6% | 77.5% |

So FakeMMAP's hope comes true on most subsets. The corrected bound on a typical path (the median) is one or two above the trivial bound. Each row is a bound and the subsets where it is the median:

| Typical bound (median) | Subsets |
|---|---|
| $M \geq 13$ | 0c3 |
| $M \geq 12$ | 2c5, 4a2, 0c4, 4c4 |
| $M \geq 11$ | 2c4, 2c3, 4c3, 4b5 |
| $M \geq 10$ | 4a1 |
| $M \geq 9$ | 4b2 |
| $M \geq 8$ | 0c0 |

It's 11 or more on 54.0% of 2c3 paths. It stays two to four and a half moves below the mean optimum, though, and reaches the optimum itself on at most 9% of a subset's cases. So it only tells you to stop writing longer reductions if you're hunting a finish well below the optimum.

How often the bounds beat the trivial one, size-weighted over all subsets, as a share of cases:

| Bound | Beats the trivial bound |
|---|---|
| as written, with $\alpha_i$ | 75.3% |
| with $\alpha_{i+1}$ | 77.3% |
| exact model, *computer only* | 84.4% |

---

## 10. Hand checklists, graded

I translate each checklist into route classes as closely as the route names allow and grade it on the same sample: the share of DRs where its steps so far find an optimal finish, and a finish within +1, with HTRs at most two over the shortest (budget 2), and with no HTR limit. Steps that depend on how many setup moves come before a trigger are graded as their whole route class, which flatters them a little. Sampled, 25,000 per subset × edges.

**Zagros's 4b2 order** ([29 Dec 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1455301984415514719)): "1. check shortest HTR on normal by settings up to triggers and reasonable extensions", "2. check more linear 2qt HTRs by just reducing to 4a1 and doing the HTR even if it's long", and on to "8. if it is seriously my only DR and I have nothing, try 2+2 HTRs". Steps 1 and 2 are graded together; 6 (the inverse) and 7 are already inside the others, since both sides are always graded. Each row is a step; each cell is the cumulative share of 4b2 DRs found after it:

| Step | What | Optimal (budget 2) | Within +1 (budget 2) | Optimal, no HTR limit |
|---|---|---|---|---|
| 1 | S1+S2 linear 2qt 4b2 4a1 HTR (normal or inverse) | 37.6% | 67.2% | 45.0% |
| 2 | S3 linear 4qt HTR of <= 8 moves | 45.4% | 75.7% | 54.3% |
| 3 | S4 reduce to 4a1, switch (4b2 4a1 (HTR)) | 50.8% | 80.8% | 54.3% |
| 4 | S5 regress to 2c3, switch (4b2 2c3 (...)) | 64.2% | 90.4% | 95.5% |
| 5 | S8 2+2: any 4qt route switching after the 2nd qt | 71.3% | 93.4% | >99.9% |

Zagros: "if I simply follow the system I have in my mind for each subset without getting distracted then it just produces optimal in 15 minutes like 80% of the time" ([29 Dec 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1455302363953758427)). Done fully on 4b2 with near-shortest HTRs, it finds the optimal on 71.3% and +1 on 93.4%; with HTRs of any length every 4b2 is covered. Zagros's 80% is about real attempts, where time is the limit, so I can't check it here, but nothing in the numbers contradicts it. After the first, the step that adds the most is table step 4 (Zagros's step 5, the regression to 2c3), 13.4 points.

**4b2 4e: regress to 2c3 first, or reduce to 1q first?** The thread:

- Yura Riabov ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258421085251178608), [4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258421209075417138), [4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258421267917312132)): "4b2 4e is basically the best 4q subset", go to 2c3 "if it's not 1-2 moves to trigger", "i also try 2-3 moves to 4a1 and niss trace if i don't forget to do that".
- rogo asked whether it shouldn't be the other way round ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258442750953525399)): "the first approach apart from R U2 F2 R to check should still be 'reduce to 1qt 4e and niss trace for short htrs' i think?"
- Adri agreed the label was the confusing part ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258454166830055454)): "I agree that's why calling it the best 4qt subset seems confusing".
- Jay ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258586844883451964)): "if you think of this subset as one where you only try to solve with U R2 F2 U, you're gonna miss optimal the vast majority of the time".

Yura Riabov's order, with the first step as a trigger with at most two setup moves (the setup limit is Yura's "1-2 moves"); each row is a step, each cell a cumulative share of 4b2 4e:

| Step | What | Optimal (budget 2) | Within +1 (budget 2) | Optimal, no HTR limit |
|---|---|---|---|---|
| 1 | S1 linear 2qt trigger with <= 2 setup moves (HTR <= 6) | 8.6% | 16.1% | 8.6% |
| 2 | S2 regress to 2c3 (2e or 4e), then 2c3 linear or switch (4qt) | 62.3% | 88.4% | 82.2% |
| 3 | S3 reduce to 4a1 and switch | 72.9% | 94.0% | 93.1% |

The other start, reducing to 1q and NISS-tracing, is DR bounding. On 4b2 4e, one row per start, share finding the optimal (budget-2 HTRs for the routes; bounding on 4,000 states, section 8):

| Start | Optimal found |
|---|---|
| Yura Riabov's first two steps | 62.3% |
| every reduction to 1q of at most 3 moves | 40.4% |
| every reduction to 1q of at most 4 moves | 52.5% |
| every reduction to 1q of at most 5 moves | 68.6% |

So the regression to 2c3 beats every reduction up to 4, and is a little behind every reduction up to 5 (about 1,919 of them). The 4a1 switch adds 10.6 points after it. Jay is right too: the 2qt trigger alone (with at most two setup moves) finds 8.6%. On 4b2 4e every optimal uses 4 quarter turns on 63.7% of states, as Yura Riabov's [*Hitchhiker’s Guide to HTR*](https://docs.google.com/document/d/1_NMlyPh2Ifd1E0ivos-15Sp-by-KPxoOsj9JD4pJuHI) says ("it’s optimal with 4q more than half of the time").

Fanti's split ([2 Feb 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1335799386914951218); probably read off *allcases*, since it matches its cells): "40% of opt 4b2 4e solutions use 2qt, 45% regress to 2c3", "only about 8% go to 0c0 2e/4e". Read as a checklist in that order, one row per step, cumulative shares of 4b2 4e:

| Step | What | Optimal (budget 2) | Within +1 (budget 2) | Optimal, no HTR limit |
|---|---|---|---|---|
| 1 | 2qt (4b2 4a1 HTR, any switch) | 35.5% | 66.0% | 36.2% |
| 2 | 4qt via 2c3 | 77.8% | 95.5% | 93.1% |
| 3 | 4qt via 4a1 0c0 | 80.2% | 96.3% | 97.6% |

**Lewis Isom's 4a2 0e/2e list** ([11 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1360414689019957449)): "1) Linear 2qt HTRs on both sides. This means the first qt makes 4a1 4e.", "2) Write down all the +1's and +2's to 4a1 4e, and NISS them.", then the U M2 U checks, the regression to 4c3, and to 0c3. One row per step, cumulative shares of 4a2 0e and 2e pooled:

| Step | What | Optimal (budget 2) | Within +1 (budget 2) | Optimal, no HTR limit |
|---|---|---|---|---|
| 1 | S1 linear 2qt 4a2 → 4a1 4e → HTR | 13.3% | 36.8% | 32.4% |
| 2 | S2 reduce to 4a1 4e, switch | 32.2% | 62.2% | 32.4% |
| 3 | S3 4qt linear through 4a2 4e again (qt, slice, qt) | 37.7% | 67.9% | 73.0% |
| 4 | S4 regress to 4b3 (2e/4e), switch, 4a3 4b2 4a1 | 52.7% | 81.1% | 73.6% |
| 5 | S5 regress to 0c3, then 0c3 4a2 4a1 (linear or NISS) | 53.4% | 81.6% | 73.6% |

Levi Gibson's reply for 4a2 0e, "you don’t have to try reductions to 4a1 4e because the average optimal solution length for that path is like 17.2 to slice" ([11 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1360460016330739854)), fits. On 4a2 0e one optimal picked at random is a 2qt path on only 2.6% of states, and steps 1 and 2 together find the optimal on 32.2% of 4a2 0e and 2e pooled. After the first, the step that adds the most is step 2 (S2 reduce to 4a1 4e, switch, 18.9 points). Next is step 4, the 4b3 regression with the switch, which is the first route of my 4a2 0e and 2e checklists.

**Jay's and rodneykinney's 3qt 2c0e checks.** Jay counted "11 total things" to check for every two half turns followed by a quarter turn ([16 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1042617188370087988)); rodneykinney: "I would count 9 cases" ([17 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1042817953072152596)), and later "You can check just F and R2 F" ([17 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1042825807892054106)). As a route class (one qt to 4b2 4e, switch, then 4a1 and HTR, any setup) it finds the optimal on 46.3% of 2c3 0e and +1 on 81.8%. The setup counts themselves aren't graded.

**Daichi's cheat sheet** ([12 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515146431542067290)), every listed route of each subset × edges together, against my checklist. Each row is a subset × edges and the share where the sheet's routes find the optimal (or +1), then the share of my first three routes:

| Subset | Optimal (budget 2) | Within +1 (budget 2) | Optimal, no HTR limit | My 3 classes (budget 2) | My classes to match |
|---|---|---|---|---|---|
| 0c0 0e | 84.5% | 95.2% | 91.8% | 92.6% | 3 |
| 0c0 2e | 71.5% | 93.4% | 95.9% | 70.2% | 4 |
| 0c0 4e | 65.1% | 90.8% | 94.4% | 61.5% | 6 |
| 0c0 6e | 61.2% | 89.4% | 94.5% | 60.2% | 4 |
| 0c0 8e | 70.1% | 91.7% | 77.9% | 77.1% | 2 |
| 2c5 0e | 81.6% | 96.5% | >99.9% | 89.6% | 2 |
| 2c5 2e | 86.1% | 97.8% | >99.9% | 91.0% | 2 |
| 2c5 4e | 85.7% | 97.7% | >99.9% | 91.9% | 2 |
| 2c5 6e | 83.7% | 97.2% | >99.9% | 90.6% | 2 |
| 2c5 8e | 83.0% | 97.1% | >99.9% | 91.0% | 2 |
| 2c4 0e | 88.4% | 98.7% | 98.8% | 88.6% | 3 |
| 2c4 2e | 89.7% | 98.8% | 98.6% | 89.9% | 3 |
| 2c4 4e | 87.3% | 98.6% | 98.5% | 87.6% | 3 |
| 2c4 6e | 88.0% | 98.6% | 98.6% | 88.5% | 3 |
| 2c4 8e | 89.5% | 99.3% | 98.1% | 91.5% | 2 |
| 0c3 0e | 92.6% | 99.3% | 97.5% | 96.6% | 2 |
| 0c3 2e | 85.6% | 98.8% | 93.1% | 92.1% | 2 |
| 0c3 4e | 72.6% | 95.2% | 84.3% | 85.8% | 2 |
| 0c3 6e | 87.9% | 99.0% | 94.3% | 94.6% | 2 |
| 0c3 8e | 92.9% | 99.4% | 98.8% | 96.1% | 2 |
| 4a2 0e | 37.6% | 64.8% | 69.3% | 44.4% | 2 |
| 4a2 2e | 76.8% | 96.3% | 87.1% | 76.8% | 4 |
| 4a2 4e | 65.9% | 87.7% | 67.8% | 79.1% | 2 |
| 4a1 0e | 70.1% | 92.1% | 95.7% | 54.6% | 6 |
| 4a1 2e | 76.5% | 95.4% | 86.3% | 70.5% | 4 |
| 4a1 4e | 69.4% | 92.2% | 89.8% | 60.6% | 5 |
| 2c3 0e | 87.8% | 98.8% | 99.9% | 75.1% | 8 |
| 2c3 2e | 79.6% | 96.4% | 89.8% | 80.2% | 2 |
| 2c3 4e | 76.6% | 95.6% | 83.2% | 78.1% | 2 |
| 2c3 6e | 73.3% | 94.7% | 78.1% | 76.7% | 2 |
| 2c3 8e | 85.9% | 98.5% | 99.9% | 74.5% | 8 |
| 0c4 0e | 83.6% | 95.6% | >99.9% | 87.6% | 2 |
| 0c4 2e | 89.2% | 98.0% | >99.9% | 89.1% | 4 |
| 0c4 4e | 84.5% | 97.1% | >99.9% | 86.1% | 2 |
| 0c4 6e | 83.4% | 97.1% | >99.9% | 85.4% | 2 |
| 0c4 8e | 80.7% | 96.3% | >99.9% | 87.1% | 2 |
| 4c3 0e | 74.8% | 94.8% | 76.5% | 83.3% | 2 |
| 4c3 2e | 72.4% | 94.1% | 74.6% | 75.1% | 3 |
| 4c3 4e | 67.8% | 92.0% | 70.7% | 74.4% | 2 |
| 4c4 0e | 66.9% | 92.8% | 86.5% | 76.7% | 2 |
| 4c4 2e | 70.6% | 93.8% | 90.7% | 78.7% | 2 |
| 4c4 4e | 70.7% | 93.7% | 91.4% | 78.2% | 2 |
| 4b2 0e | 74.9% | 94.2% | 91.6% | 61.0% | 6 |
| 4b2 2e | 67.2% | 90.9% | 94.4% | 59.0% | 6 |
| 4b2 4e | 77.8% | 95.5% | 93.1% | 66.8% | 6 |
| 4b5 0e | 74.6% | 93.8% | >99.9% | 92.6% | 2 |
| 4b5 2e | 78.8% | 95.1% | >99.9% | 93.6% | 2 |
| 4b5 4e | 77.4% | 94.3% | >99.9% | 93.9% | 2 |

The last two columns are my first three budget-2 routes and how many of my routes it takes to match the sheet. The sheet against my first three:

| Sheet is | On |
|---|---|
| ahead | 4b2, 4a1, 2c3 0e and 8e, 0c0 2e to 6e (where it lists several routes) |
| about level | 2c4 0e to 6e, 4a2 2e, 0c4 2e |
| behind | all of 2c5, 0c3, 4c3, 4c4 and 4b5; 0c4 except 2e; 4a2 0e and 4e; 2c3 2e to 6e; 2c4 8e; 0c0 0e and 8e |

Daichi aimed it at sub-13 finishes, so its routes favour the short ones, which is what you want in an attempt anyway.

---

## 11. The claims, checked

Everything said on the server that the numbers can settle, by theme. Questions and guesses are in section 2, unless they came with a number. Each verdict is one of **True**, **Corrected**, **Depends** (true under one reading, not another), **Open** (not settled here) and **Withdrawn** (taken back at the time). Shares are on the sample (25,000 per subset × edges) unless marked exact. Every correction has an example in the errata.

**Routes and sheets**

| Claim | Who | Verdict |
|---|---|---|
| "It doesn't capture EVERYTHING, but I decided that checking these will capture a great portion of those" (the cheat sheet) | Daichi [12 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515177158870569101) | **True**: the sheet's routes find the optimal on 37.6% (4a2 0e) to 92.9% (0c3 8e) with budget-2 HTRs (section 10). |
| "40% of opt 4b2 4e solutions use 2qt, 45% regress to 2c3", "only about 8% go to 0c0 2e/4e" | Fanti [2 Feb 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1335799386914951218) | **Depends**: these are *allcases*' own cells for 4b2 4e (39.5%, 44.8%, 8.4%; Fanti names no source, but the numbers match), so Fanti read the sheet right. One leave-slice optimal picked at random among the optimal finishes (5,000 states) gives 33.5%, 46.8% and 9.9%: the sheet picks the fewer-qt optimal more often than chance when there are ties (section 5). |
| "optimal for 4b2 0e goes through 4c3 4% of the time? wtf" (read off *allcases*) | Evan [29 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1300996305778380810) | **True** in kind: one leave-slice optimal at random (5,000 states) passes 4c3 on 6.1% of 4b2 0e; the sheet's lower figure fits its preference for fewer qts. |
| "Only 1/3 of 2q 4b2e cases use 2qt for optimal wtf" | mrauo [8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315341544206631054) | **Withdrawn**: it read the 4a2 2e row; Zagros said so at once ([8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315341879910600775), [8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315341893856657430)) and mrauo agreed ("Okey I was so confused hahaha", [8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315342166221918269)). Section 5. |
| "Much more common with the 3q 4c subset and high edge count (6 or 8) for 3q 2c" (DRs whose only optimals use 5qt) | Jakob Jernsletten [25 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1233064302634860554) | **True**: every optimal uses 5qt on 27.4% of 4c3, 21.9% of 2c3 6e and 52.8% of 2c3 8e, against 10.2% of 2c3 2e. |
| "2c3 rarely needs 5q for optimal, so I don't usually check 5q on 2c3", after pointing to the *Extra Quarter-Turn Stats* sheet ("Theres the stat sheet for that") | Levi Gibson [29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1312044914921439253), [29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1312044531805458514) | **Depends** on the edges, read as the sheet does (every leave-slice optimal needs 5qt): 11.2% of all 2c3, 5.1% of 2e and 10.6% of 4e, but 49.5% of 0e and 47.0% of 8e. |
| "So, ~25% of 4c3 requires 5qt to get optimal !!!?!?"; "Yes, this is correct" | Lichi Fang [29 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1301009545031585802), Levi Gibson [29 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1301010011912409129) | **True**: every leave-slice optimal uses 5qt on 25.3% of 4c3 (full finish 27.4%). |
| "oh yeah i got 6.10% adding them together" (4a1 4e optimals with 5qt, summed from *allcases*) | Fanti [29 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1301012887996731443) | **Depends**: the sheet's 5qt rows for 4a1 4e do add to 6.1%, and Levi Gibson's quick estimate just before was a slip on those same rows, taken back at once ([29 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1301012924143501322)). One leave-slice optimal at random (5,000 states) has 5qt on 9.6%, the sheet again favouring fewer qts; every leave-slice optimal needs 5qt on 3.6% (full finish 10.2%). Fanti's question was the last of these. |
| "A 1qt corners with 4c2e is going to need 3qt" | Aneurin [6 Oct 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1027525262486802492) | **True**: every optimal of 4a1 2e uses at least 3qt (every sampled state). |
| "baically 85 percent chance that you dont need to check 2 ht before first qt" (2c3 2e) | Kai Cui [5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457432898633840) | **True**: 82.7%, either side (section 7). Kai Cui's states were half turns around one trigger, not uniform DR states. |

**Extra quarter turns and the last DR move** (section 7)

| Claim | Who | Verdict |
|---|---|---|
| "57% of the time, the optimal solution uses 4QT for a  2QT corner case" | rodneykinney [13 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1063355084697784371) | **Depends** on which optimal: 53.9% every optimal, 80.7% some optimal, 69.0% one at random (leave slice 56.3%). |
| "over 60% the optimal solution for htr subset 2qt(a) 4c4e … use 4qt rather than 2qt" (first nissy optimal) | Lichi Fang [6 Aug 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1137835695721939094) | **True**: one optimal at random 77.6%, every optimal 63.7%. |
| "so yeah, should be 1/6" (mean gain from inverting the last DR move), "very rough" | Yura Riabov [6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248337792673779803), [6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248372741602545674) | **Corrected**: 0.325 moves, about 1/3 [a]. Yura's ceiling, "i doubt it will be more than a half move difference with 1 move inverted" ([6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248372741602545674)), is **True**. |
| "but inverting last move before dr will always reduce optimal by 1" (the 18-move states) | Yura Riabov [24 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1364979172774252674) | **True**, exact: every 18-move DR state is 17 after its last side half turn either way; torchlight's finding as Jay reported it ([28 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1355356897414348904): "i think torchlight figured out that for all those cases any of R2 L2 F2 B2 (UD oriented DR) would take the case from 18 to 17") is also true. |
| "a qt break from DR only makes it around 0.5 worse, rather than 1 as you might expect" | trangium [6 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1469487095407186093) | **True**, roughly: 0.68 on average. |

**HTR lengths** (exact over the 29,400 HTR cosets unless marked)

| Claim | Who | Verdict |
|---|---|---|
| "I figured out there's only 8 HTR" cases "where it's possible to solve it in 5 or less moves, and a further 3 that are 6 or less in their best case scenario", "one of the 6 movers is 8E with 0qt corners", "4 total cases which are potential 4 or less" | Jay [6 Oct 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1027524047174643742), [6 Oct 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1027524257296691200), [6 Oct 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1027524588101439499) | **True**, leaving out 0c0 0e (HTR already, or U D'): 8 subsets × edges at most 5, 3 more at 6 (one of them 0c0 8e), 4 at most 4. Counting 0c0 0e it is 9, 3 and 5. |
| "If you skip 4qt entirely there's only 7 cases (with my method/jacks method, with hyper parity I think there's more)" | Jay [14 Oct 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1030639402952699904) | **True**: 0c0 4a1 4a2 4b2 0c3 2c3 4c3, seven corner subsets with at most 3qt. |
| "2cxe I think it's at least worth noting if it's 0/2/4e (all 7 optimal w/o NISS) 6e (8) or 8e (9)" | Jay [2 Jan 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1191918611724505168) | **True**: the shortest linear HTR is 7 moves on 0e, 7 on 2e, 7 on 4e, 8 on 6e and 9 on 8e. |
| "4qt 2C is 6 moves to HTR at best using NISS (7 without)"; "10 linearly, 6 with NISS", "for the other type of fake htr its 9 linearly and 6 with NISS" | Jay [29 May 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1112914561524314236); Lewis Isom [23 Jun 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1254409343991025766) | **True**: 2c4 0e 7/6, 0c4 0e 9/6, 0c3 0e 10/6 (linear exact, NISS the sample's minimum). |
| "Interesting that it seems 4qt 4C0E is the only HTR subset that is guaranteed 11 moves without NISS" | Jay [29 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069455768782385294) | **Corrected**: 4c4 0e has linear HTRs of 10, and 0c4 8e is the subset that always needs 11 [b]. Lewis Isom noticed the 10 in 2024 ([23 Jan 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1199494282223038485)). |
| "No, the maximum it takes is 12 moves linearly, and 11 moves using NISS." | Lewis Isom [23 Jan 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1199490255921877022) | **Corrected**: 13 linearly on both sides and 12 with NISS occur (sample) [c]. Daichi's "0c3 4e and 4c4 0e have 13 move optimal HTR cases" ([14 May 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1504408526444040192)) is **True** (13 and 13, exact). |
| "5/6" (of HTRs that are fake) | zakimoshi [19 Sep 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1153601303801495632) | **True**, exact: 480/576 of the corner arrangements with no bad corner are fake (Lean-checked). |
| "the *expected value* is 10.13 -- the average number of moves to solve a random HTR state" | DougCube [13 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1416567970334773378) | **True**, exact over the 663,552 HTR states (half turns only). |
| "This should be it" (the share of each corner subset, in 210ths) | Daichi [6 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1391490386509172888) | **True**, exact. |
| "2c4 0e for example is actually really good a lot of the time" | Jay [27 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1300230075458916444) | **True**: it has the lowest mean optimal of the 2c4 cases, exact 13.218 against 13.531 to 14.015. |
| "2с4 is 13.5ish on average optimal, 4b2 2e is 12.5ish iirc" | Yura Riabov [25 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1476183753410744443) | **True**, exact: 13.647 and 12.611. |
| "9 moves from DR to HTR is quite a lot so usually the solution from those will also be too long to be optimal. And especially here you have so many shorter HTRs to check."; "If you have checked all shorter HTRs and you have no other DRs to check you might as well start checking 9 move HTRs." | tseitsei89 [12 Oct 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1426922640462970924), [12 Oct 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1426926451680215131) | **Open**: it's about each 9-move HTR you write, which I didn't measure. For context only: on 65.2% of DRs every optimal needs an HTR of 9 or more, on 29.7% although a shorter HTR exists (section 6). |
| "this isn't the worst practice but it's pretty rare for switching after doing more than 2 moves to actually be useful, unless you're variationmaxing" | Evan [2 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368063770576027648) | **Corrected** [d]: the optimal through its shortest HTR needs a switch after more than 2 moves on 28.2% of DRs. That's an upper bound on how often a late switch is needed (another optimal with a longer HTR may avoid it). Outside the cases Evan named ("the b side of 4c3", "4c4 and 0c4 ofc but those are pretty rare", [3 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368159205072175145), [3 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368159998848274462); all of 4c3, 4c4 and 0c4 left out) it's 24.0%. By subset: 17.9% of 2c3, 16.1% of 4b2, 24.1% of 2c4, 43.5% of 2c5. |
| "More like 3 imo"; "i almost never do this but i think it is useful"; "i really don't like switching after more than 2 moves or for badish cases, which is why i'm worse at finishes than i could be" | Yura Riabov [3 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368155824371007488), [3 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368162064148725770), [3 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368162218579071158) | **True** for most subsets. Switch after 4 or more moves: 5.5% of 2c3, 4.9% of 4b2, 2.7% of 4a1, 3.5% of 0c0 (9.7% outside 4c3, 4c4 and 0c4). Large only on 0c4 (32.4%), 4c4 (30.4%) and 2c5 (23.5%). |
| "pretty sure 15 is gods number for 4a1 4e" | Levi Gibson [29 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1377633973039009822) | **Depends** on the metric: Levi Gibson's stats are leave-slice ("E Slice is not a thing in this simulation", [13 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1295060662908751912)), and the longest leave-slice optimal of a 4a1 4e is 15, exact over all 286,654,464 of them; the longest full finish (E slice solved) is 17. |

**Bounding** (sections 8 and 9)

| Claim | Who | Verdict |
|---|---|---|
| "I like to check all sub-5 reductions. This can be done super quick and gets optimal like 75% of the time, and it gets optimal +1 the rest of the time" | Levi Gibson [28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311670582601060354) | **Corrected** [e]: bounding alone, every reduction of at most 4. On 4a2, the subset named just before ("for the 4a2 subset I use full DR Bounding", [28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311669869900464138)): optimal 76.6%, so the 75% holds there, but within +1 only 93.6%. On 2c3: optimal 48.1% (52.1% of 2c3 2e), within +1 78.8%. Levi Gibson used it with 5-move triggers on 2c3 ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311674286389334026)), which I didn't measure; the later "yeah something like that I'd guess" for 80% on 2c3 ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051081831780434)) was a guess. |
| JTuu's simulation: "Findable: 1293/2000 (64.65%)" (linear 7 or bounding 4) … "Findable: 1721/2000 (86.05%)" (8 and 5) | JTuu [4 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313766061325156462) | **Open**: same definitions, uniform states give 5.8 to 9.4 points less; the states were probably drawn differently, or with the last DR move inverted, which Kai Cui's generator did (section 8). |
| "Bounding update: after lots and lots of solves this is how I use it" (per-subset verdicts) | Levi Gibson [8 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1370092390362382348) | **Depends** on the subset: right for 0c0, 4a2 0e, 4a1 (bound 4a1 4e, not 0e/2e) and 2c3 2e/4e; on 4b2 0e and 2e bounding with reductions of 4 already beats three routes, more than "just check the really short ones" suggests; on 2c3 6e and on 4c3 ("Bounding is actually REALLY good for 4c3") the routes are well ahead (section 8). |
| "half of all 3QT cases and a quarter of all 4QT cases can immediately be reduced to 2QT by applying a U move to the normal and/or inverse", amended to "2/3 of 3QT cases and 1/6 of 4QT cases" | rodneykinney [11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062756177424961546), [11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062823846954160128) | 3qt: **True**, exact: one bare qt on normal or inverse does it for 66.1% of 3qt corner arrangements (Lean-checked). 4qt: **Open**: one bare qt never does it (exact); it takes a qt on each side, the "and" of "and/or", which rodneykinney's 1/6 counted from optimal corner solutions ([11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062820653113290773), [11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062821731091349525)) and this study did not. |
| R from [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369), "the biggest possible length of a reduction to 1q you have to check" | FakeMMAP [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531394667773962) | **True** as written, safe but loose: R, "the max of the following", is never too short, proved for every finish (Lean `Rmax_sound`), but only because term 1, about M − 1, is among the terms; in the sample it was never too short in 1,914,809 cases at the optimum. C is the subset's shortest linear HTR, as FakeMMAP defined it (Lean `term5_sound`, `labels_keep`). Read as the smallest term, it is sound (Lean `Rmin_sound`) once the $\alpha$ index and term 2's signs are fixed [f]. Section 9. |
| The multi-qt lower bounds of [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475), with "I don't know how useful these bounds really are, I have to put in the numbers to see if there are situations where the typical bound is M \geq 11, rather than M \geq 7 lol." | FakeMMAP [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475), [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533429198553178) | **Corrected** [f]: the sum needs $\alpha_{i+1}$; as written the bounds fail in 923 cases, and with $\alpha_{i+1}$ they are proved valid (Lean `lower_free`, `lower_A`, `lower_B`, `lower_C`). Section 9 gives the typical bound values FakeMMAP asked about. |
| "it just produces optimal in 15 minutes like 80% of the time" (following the system) | Zagros [29 Dec 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1455302363953758427) | **Open**: time isn't modelled; the 4b2 order done fully gives 71.3% with budget-2 HTRs (section 10). |

Letters refer to the errata.

---

## 12. Real DRs

Everything above weights DR states uniformly inside a subset. The DRs you actually get come from an EO and a DR search on a scramble, so here's the same code run on those. *Computer only*: this is a check of the tables, not something to do in an attempt.

**The population.** 10,000 uniformly random scrambles (random states, not nissy's scrambler, which is biased). For each one I take every EO-first DR of at most 11 moves that cubelib-cli lists, the way the first study's examples page lists them: an EO of at most 5 moves on normal, on inverse or with NISS, then DR on either side without breaking it, on either of the other two axes. That's 6,840,923 DRs (704,669 of at most 10 moves).

Each DR is the state on the side its DR step is written on (50% end on inverse), turned so its axis is U/D, deduplicated per scramble. Of a DR ending in `F` and its twin ending in `F'` only one is kept. The route questions use up to 25,000 of these DRs per subset × edges, drawn from the pool of that cell and weighted back to the population, through this study's own code.

**Two weightings**, both shown:

- **each DR once**: every DR found counts once, so a scramble with 3,000 DRs weighs 3,000 times one with a single DR (the model of *a DR someone wrote down*);
- **each scramble once**: every scramble counts once, split equally over its DRs (the model of *the DR a solver gets*).

Standard errors are clustered by scramble, since DRs of one scramble aren't independent. A cell is in **bold** when it's more than 2 points and more than 2 combined standard errors from uniform.

**What this doesn't model.** It's cubelib's EO-first list: no CO-first or direct DR, no EO longer than 5. A DR and its twin with the last move turned the other way count once. And each DR counts, not each DR a solver would *pick*: if you keep a DR for its subset or its short HTR, you're selecting on the state, and selection on features inside a subset (pairs, corner case) isn't modelled.

**Subset mix.** Largest difference from uniform, over corner subsets. Each row is a DR length limit:

| DRs of at most | Share of a corner subset | Mean optimal finish of a corner subset |
|---|---|---|
| 11 moves | 0.4 points | 0.05 moves |
| 10 moves (2 to 4 times larger standard errors) | 0.8 points | 0.13 moves |

Per corner subset, the share of all DRs it holds and its mean optimal finish in moves, uniform and on real DRs (± standard error):

| Subset | Share of DRs, uniform | Share, each DR once (± SE) | Share, each scramble once (± SE) | Mean optimal (moves), uniform | Mean optimal, each DR once | Mean optimal, each scramble once |
|---|---|---|---|---|---|---|
| 0c0 | 0.48% | 0.51 ± 0.03 | 0.48 ± 0.01 | 12.278 | 12.293 ± 0.040 | 12.327 ± 0.016 |
| 2c5 | 7.62% | 7.50 ± 0.11 | 7.49 ± 0.05 | 14.327 | 14.317 ± 0.005 | 14.332 ± 0.003 |
| 2c4 | 22.86% | 22.73 ± 0.16 | 22.98 ± 0.08 | 13.647 | 13.647 ± 0.003 | 13.660 ± 0.002 |
| 0c3 | 1.43% | 1.43 ± 0.05 | 1.46 ± 0.03 | 14.460 | 14.470 ± 0.009 | 14.460 ± 0.009 |
| 4a2 | 2.86% | 2.88 ± 0.07 | 2.82 ± 0.03 | 13.348 | 13.335 ± 0.013 | 13.355 ± 0.008 |
| 4a1 | 2.86% | 2.96 ± 0.08 | 2.90 ± 0.03 | 12.419 | 12.404 ± 0.009 | 12.435 ± 0.007 |
| 2c3 | 15.24% | 15.41 ± 0.19 | 15.24 ± 0.07 | 12.925 | 12.913 ± 0.004 | 12.930 ± 0.003 |
| 0c4 | 0.95% | 0.93 ± 0.03 | 0.96 ± 0.02 | 13.674 | 13.679 ± 0.008 | 13.679 ± 0.008 |
| 4c3 | 11.43% | 11.27 ± 0.11 | 11.40 ± 0.06 | 13.487 | 13.483 ± 0.003 | 13.488 ± 0.003 |
| 4c4 | 11.43% | 11.24 ± 0.11 | 11.39 ± 0.06 | 14.403 | 14.405 ± 0.002 | 14.411 ± 0.002 |
| 4b2 | 11.43% | 11.84 ± 0.18 | 11.44 ± 0.06 | 12.680 | 12.676 ± 0.006 | 12.693 ± 0.003 |
| 4b5 | 11.43% | 11.29 ± 0.12 | 11.44 ± 0.06 | 14.279 | 14.280 ± 0.002 | 14.284 ± 0.002 |

What does shift is the bad-edge mix inside a corner subset. With each scramble once, 0e is rarer than uniform in 11 of 12 corner subsets (up to 42.9% rarer, on 0c0 0e), and 6e up to 16.5% more common. Those cells are small, so pooled numbers hardly move.

**Why it's so close (an argument, not a proof).** The EO and DR search only sees orientations and which slice each edge is in. Given those, the rest of the scramble is uniformly random, and for a fixed move sequence the map from scramble to DR state is one-to-one. So each DR found is uniform among the DR states that agree with what the search saw. That information does fix part of the HTR structure, which is why the bad-edge mix can differ, but inside such a class every DR state is equally likely. The measurements agree.

**The checklists (section 4) on real DRs**, budget 2, greedy on each population. Each corner subset has three rows, uniform and the two real weightings; the cells are the percentage of DRs where the first 1, 2 or 3 routes find the optimal, then the same three within +1, and whether the real list's first three routes are the uniform ones in the same order.

| Subset | DRs | Optimal found, 1 route (%) | 2 routes | 3 routes | Within +1, 3 routes | Same three routes, same order as uniform |
|---|---|---|---|---|---|---|
| 0c0 | uniform | 42.3 | 55.9 | 60.9 | 86.4 |  |
|  | each DR once | **39.1 ± 1.2** | **53.6 ± 0.8** | 59.0 ± 0.6 | 85.3 ± 0.8 | yes |
|  | each scramble once | **40.2 ± 0.7** | 54.8 ± 0.7 | 60.1 ± 0.6 | 86.6 ± 0.4 | yes |
| 2c5 | uniform | 72.8 | 85.5 | 91.4 | 98.9 |  |
|  | each DR once | 73.1 ± 0.2 | 85.7 ± 0.1 | 91.6 ± 0.1 | 99.0 ± 0.0 | yes |
|  | each scramble once | 73.1 ± 0.4 | 85.4 ± 0.3 | 91.3 ± 0.2 | 99.1 ± 0.1 | yes |
| 2c4 | uniform | 66.0 | 83.5 | 88.4 | 98.7 |  |
|  | each DR once | 65.9 ± 0.2 | 83.8 ± 0.1 | 88.5 ± 0.1 | 98.7 ± 0.1 | yes |
|  | each scramble once | 66.1 ± 0.4 | 83.6 ± 0.3 | 88.4 ± 0.2 | 98.7 ± 0.1 | yes |
| 0c3 | uniform | 74.4 | 88.8 | 89.3 | 99.1 |  |
|  | each DR once | 75.3 ± 0.3 | 89.2 ± 0.2 | 89.7 ± 0.1 | 99.1 ± 0.0 | yes |
|  | each scramble once | 74.8 ± 0.4 | 89.3 ± 0.3 | 89.8 ± 0.3 | 98.9 ± 0.2 | yes |
| 4a2 | uniform | 41.6 | 64.1 | 73.2 | 90.8 |  |
|  | each DR once | 41.2 ± 0.3 | 63.8 ± 0.3 | 72.7 ± 0.3 | 90.6 ± 0.2 | yes |
|  | each scramble once | 41.6 ± 0.5 | 64.1 ± 0.5 | 73.0 ± 0.4 | 91.0 ± 0.2 | yes |
| 4a1 | uniform | 29.3 | 44.8 | 58.0 | 84.3 |  |
|  | each DR once | 29.4 ± 0.4 | 44.6 ± 0.3 | 58.0 ± 0.4 | 84.1 ± 0.3 | yes |
|  | each scramble once | 29.7 ± 0.4 | 45.0 ± 0.5 | 58.0 ± 0.5 | 84.6 ± 0.3 | yes |
| 2c3 | uniform | 53.5 | 75.7 | 78.0 | 96.1 |  |
|  | each DR once | 53.7 ± 0.2 | 75.5 ± 0.2 | 77.7 ± 0.2 | 96.0 ± 0.1 | yes |
|  | each scramble once | 53.8 ± 0.4 | 75.4 ± 0.4 | 77.8 ± 0.3 | 96.1 ± 0.1 | yes |
| 0c4 | uniform | 83.8 | 85.1 | 86.3 | 97.6 |  |
|  | each DR once | 83.2 ± 0.2 | 84.6 ± 0.2 | 85.8 ± 0.2 | 97.5 ± 0.1 | first two the same |
|  | each scramble once | 83.9 ± 0.3 | 85.2 ± 0.3 | 86.4 ± 0.3 | 97.5 ± 0.1 | first the same |
| 4c3 | uniform | 64.3 | 71.3 | 75.0 | 94.2 |  |
|  | each DR once | 64.4 ± 0.2 | 71.5 ± 0.2 | 75.0 ± 0.2 | 94.3 ± 0.1 | yes |
|  | each scramble once | 63.9 ± 0.4 | 71.0 ± 0.4 | 74.8 ± 0.4 | 94.5 ± 0.2 | yes |
| 4c4 | uniform | 68.1 | 75.0 | 78.4 | 96.1 |  |
|  | each DR once | 68.2 ± 0.2 | 74.9 ± 0.2 | 78.2 ± 0.2 | 95.9 ± 0.1 | yes |
|  | each scramble once | 68.2 ± 0.4 | 74.8 ± 0.4 | 78.2 ± 0.4 | 95.8 ± 0.2 | yes |
| 4b2 | uniform | 37.6 | 53.3 | 62.6 | 88.0 |  |
|  | each DR once | 37.8 ± 0.3 | 53.6 ± 0.2 | 62.8 ± 0.2 | 88.4 ± 0.2 | yes |
|  | each scramble once | 37.9 ± 0.5 | 54.2 ± 0.5 | 63.2 ± 0.5 | 88.6 ± 0.3 | yes |
| 4b5 | uniform | 64.7 | 87.4 | 93.7 | 99.6 |  |
|  | each DR once | 64.7 ± 0.2 | 87.3 ± 0.1 | 93.8 ± 0.1 | 99.6 ± 0.0 | yes |
|  | each scramble once | 64.4 ± 0.4 | 87.2 ± 0.3 | 93.7 ± 0.2 | 99.5 ± 0.1 | yes |

- **The first route is the same on every corner subset**, and on 47 of 48 subset × edges with each DR once (47 with each scramble once). The one change in each is a near-tie in a cell of a few hundred DRs.
- **The first three routes are the same, in the same order, everywhere except 0c4.** There the real greedy list brings in `0c4 4a3 4b2 2c3 4b2 4a1 (0c0)` in place of `0c4 4a3 4b2 4a1 0c0` (third with each DR once, second with each scramble once). The uniform three routes on the same real DRs find 0.05 and 0.16 points less. On 0c4 every route after the first adds about a point, so this is a tie, not a new route to learn.
- **0c0 is the one corner subset that moves** (first row of the table below). 0c0 is half a percent of DRs. Everywhere else no checklist number moves by more than 1.0 point.
- **Per subset × edges** the cells flagged are 0c0 8e, 0c3 0e, 2c3 0e, all 0e or 8e cells holding few DRs (two of them below).

**The other headlines of section 1**, one row per headline, each a percentage of DRs (± standard error):

| Headline | Uniform (± SE) | Each DR once (± SE) | Each scramble once (± SE) |
|---|---|---|---|
| Shortest NISS HTR = shortest linear, all DRs (section 6) | 55.8 ± 0.1 | 56.2 ± 0.2 | 55.8 ± 0.2 |
| NISS HTR 1 shorter, all DRs | 32.3 ± 0.1 | 32.0 ± 0.1 | 32.3 ± 0.1 |
| NISS HTR 2+ shorter, all DRs | 11.9 ± 0.1 | 11.8 ± 0.1 | 11.9 ± 0.1 |
| NISS HTR 2+ shorter, 0c3 | 52.4 ± 0.2 | **50.1 ± 0.8** | 52.0 ± 0.6 |
| Some optimal uses a shortest NISS HTR, all DRs | 32.9 ± 0.1 | 32.9 ± 0.1 | 32.7 ± 0.1 |
| Every optimal needs an HTR of 9+, all DRs | 65.2 ± 0.1 | 64.9 ± 0.2 | 65.5 ± 0.2 |
| Bounding to 1q, R ≤ 4, all DRs (section 8) | 24.9 ± 0.1 | 25.4 ± 0.2 | 25.0 ± 0.1 |
| Bounding to 1q, R ≤ 5, all DRs | 40.6 ± 0.2 | 41.0 ± 0.2 | 40.6 ± 0.2 |
| Bounding to 1q, R ≤ 3, 0c0 | 86.0 ± 0.3 | 86.0 ± 0.4 | 86.3 ± 0.4 |
| Bounding to 1q, R ≤ 5, 4a2 | 80.0 ± 0.4 | 80.3 ± 0.3 | 79.6 ± 0.4 |
| Bounding to 1q, R ≤ 5, 4a1 | 88.6 ± 0.3 | 88.3 ± 0.2 | 88.2 ± 0.3 |
| Bounding to 2q, R ≤ 3, all DRs | 60.4 ± 0.2 | 60.8 ± 0.2 | 60.4 ± 0.2 |
| Zagros's 4b2 order, all five steps (section 10) | 71.3 ± 0.2 | 71.3 ± 0.2 | 71.5 ± 0.4 |
| Yura Riabov's 4b2 4e order, three steps | 72.9 ± 0.3 | 73.1 ± 0.3 | 73.8 ± 0.6 |

The numbers that move, against uniform, as a share of DRs:

| Number | Uniform | Each DR once | Each scramble once |
|---|---|---|---|
| 0c0, first route | 42.3% | 39.1% | 40.2% |
| 2c3 0e, first route (flagged with each scramble once) | 46.3% | 45.7% | 43.4 ± 0.9% |
| 0c0 8e, first route (flagged with each DR once) | 53.5% | 47.5 ± 2.7% | 50.9% |
| 0c3, *NISS HTR 2+ shorter* (flagged with each DR once) | 52.4% | 50.1% | 52.0% |

The 0c3 one is the only flagged headline. Every other headline moves by at most 0.9 points; every bounding share at R ≤ 3 to 5, per corner subset, by at most 0.8; the per-subset HTR numbers of section 6 outside 0c0 by at most 1.4. The subsets where short reductions reach 80% are still 0c0, 4a1 and 4a2, with 4a2 on the line in every population (80.0% uniform, 80.3% and 79.6% on real DRs). **No recommendation in this study changes.**

---

## 13. What this does not cover

- **Findability and time.** Every number is what exists along a route, not what you'd find in an attempt. The HTR budget is a stand-in for effort (how much longer than the shortest HTR you are willing to look), not a cost model: it does not count how many HTRs of that length a route has, or how long setups take. A route and a reduction are different amounts of work, so section 8 compares them only in kind.
- **Half turns inside a route.** Routes record the corner subsets after each quarter turn, not how many half turns come between. Steps of hand checklists that limit setup moves ("1-2 moves to trigger", "two half turns followed by a quarter turn") are graded as their whole route, which flatters them; Jay's and rodneykinney's setup counts are not graded separately.
- **Samples.** Route and bounding questions are sampled (25,000 states per subset × edges; 4,000 for reduction counts). A share's standard error is at most 0.3 points per subset × edges; small differences between routes deep in a checklist are noise. The +1 level uses the same enumeration as the optimum but was not cross-checked by an independent solver.
- **DR-breaking and HTR-breaking finishes**, and finishes that leave the slice, are not routes here: finishes stay in the DR group, E slice solved. (The leave-slice optimum is used only where a sheet uses it.) How often breaking DR would beat the DR-move optimum is measured in section 3: 4.3% of DRs, more on 0c3 0e, 0c4 0e and 0c0 0e.
- **The DR itself.** The tables are over uniform DR states. The DRs cubelib finds on random scrambles give the same checklists, grades and bounding shares within about a point per corner subset (section 12), so that's not the gap it looked like; what section 12 doesn't model is which DRs a solver chooses to keep. Generated sets such as Kai Cui's and JTuu's states built around one trigger are not uniform, and section 8 shows how much that can matter. Variations of the DR other than its last move are not covered.
- **Fixed targets** of 10 to 12 in sections 8 and 9 use finishes up to max(optimal + 1, min(optimal + 2, 12)) moves; for DRs whose optimum is 9 or less, a longer target is not covered.
- **rodneykinney's 4qt "1/6"** (a quarter turn on each side taking 4qt to 2qt) is not computed.

---

## Appendix A: full tables

**Every checklist, budget 2**: one row per route, per subset × edges the first eight routes in greedy order, the cumulative share of DRs where the routes so far find an optimal finish, and where the same routes find a finish within +1 (same HTR budget). Sampled, 25,000 per subset × edges.

| Subset | # | Class | Optimal, cumulative | Within +1, cumulative |
|---|---|---|---|---|
| 0c0 0e | 1 | `0c0 4a1 0c0` | 42.5% | 48.2% |
|  | 2 | `0c0` | 84.4% | 95.1% |
|  | 3 | `0c0 \| qt` | 92.6% | 98.3% |
|  | 4 | `0c0 4a1 0c0 \| qt` (mirror: `0c0 4a1 (4a2 4a1 4b2 4a1 0c0)`) | 92.9% | 98.5% |
|  | 5 | `0c0 4a1 (0c0)` | 93.0% | 98.6% |
| 0c0 2e | 1 | `0c0 4a1 0c0` | 60.5% | 83.7% |
|  | 2 | `0c0 4a1 0c0 4a1 (0c0)` (mirror: `0c0 4a1 (4a2 4a1 0c0)`) | 65.7% | 88.3% |
|  | 3 | `0c0 4a1 (0c0)` | 70.2% | 92.3% |
|  | 4 | `0c0 4a1 4b2 4a1 0c0` | 72.3% | 93.8% |
|  | 5 | `0c0 4a1 0c0 (4a1 0c0)` (mirror: `0c0 4a1 0c0 \| qt`) | 73.0% | 94.1% |
|  | 6 | `0c0 4a1 (0c0 4a1 0c0)` (mirror: `0c0 4a1 4b2 4a1 (0c0)`) | 73.8% | 94.3% |
|  | 7 | `0c0 4a1 0c0 \| qt` (mirror: `0c0 4a1 (4a2 4a1 4b2 4a1 0c0)`) | 74.1% | 95.0% |
|  | 8 | `0c0 4a1 4b2 (4a1 0c0)` | 74.3% | 95.2% |
| 0c0 4e | 1 | `0c0 4a1 0c0` | 44.9% | 70.0% |
|  | 2 | `0c0 4a1 (0c0)` | 57.8% | 83.6% |
|  | 3 | `0c0 4a1 4b2 4a1 0c0` | 61.5% | 88.1% |
|  | 4 | `0c0 4a1 4b2 (4a1 0c0)` | 63.6% | 89.9% |
|  | 5 | `0c0 4a1 0c0 4a1 0c0` | 65.1% | 90.5% |
|  | 6 | `0c0 4a1 0c0 4a1 (0c0)` (mirror: `0c0 4a1 (4a2 4a1 0c0)`) | 66.4% | 91.3% |
|  | 7 | `0c0 4a1 (0c0 4a1 0c0)` (mirror: `0c0 4a1 4b2 4a1 (0c0)`) | 67.5% | 91.9% |
|  | 8 | `0c0 4a1 0c0 (4a1 0c0)` (mirror: `0c0 4a1 0c0 \| qt`) | 68.4% | 92.1% |
| 0c0 6e | 1 | `0c0 4a1 (0c0)` | 40.8% | 70.7% |
|  | 2 | `0c0 4a1 0c0 4a1 (0c0)` (mirror: `0c0 4a1 (4a2 4a1 0c0)`) | 53.7% | 83.9% |
|  | 3 | `0c0 4a1 (0c0 4a1 0c0)` (mirror: `0c0 4a1 4b2 4a1 (0c0)`) | 60.2% | 88.0% |
|  | 4 | `0c0 4a1 4b2 (4a1 0c0)` | 64.0% | 90.3% |
|  | 5 | `0c0 4a1 0c0 4a1 0c0` | 65.7% | 91.1% |
|  | 6 | `0c0 4a1 0c0` | 66.8% | 92.0% |
|  | 7 | `0c0 4a1 0c0 (4a1 0c0)` (mirror: `0c0 4a1 0c0 \| qt`) | 67.4% | 92.2% |
|  | 8 | `0c0 4a1 4b2 4a1 0c0` | 67.8% | 92.2% |
| 0c0 8e | 1 | `0c0 4a1 (0c0)` | 53.5% | 78.7% |
|  | 2 | `0c0 4a1 0c0` | 70.1% | 91.7% |
|  | 3 | `0c0 4a1 0c0 4a1 (0c0)` (mirror: `0c0 4a1 (4a2 4a1 0c0)`) | 77.1% | 95.0% |
|  | 4 | `0c0 4a1 4b2 (4a1 0c0)` | 77.8% | 95.4% |
|  | 5 | `0c0 4a1 4b2 4a1 0c0` | 78.3% | 95.7% |
|  | 6 | `0c0 4a1 0c0 (4a1 0c0)` (mirror: `0c0 4a1 0c0 \| qt`) | 78.5% | 95.8% |
|  | 7 | `0c0 4a1 (0c0 4a1 0c0)` (mirror: `0c0 4a1 4b2 4a1 (0c0)`) | 78.7% | 95.8% |
|  | 8 | `0c0 4a1 0c0 \| qt` (mirror: `0c0 4a1 (4a2 4a1 4b2 4a1 0c0)`) | 78.8% | 96.0% |
| 2c5 0e | 1 | `2c5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 (4a1 0c0)`) | 77.8% | 95.5% |
|  | 2 | `2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 4a1 (0c0)`) | 86.5% | 98.0% |
|  | 3 | `2c5 2c4 2c3 4b2 4a1 0c0` | 89.6% | 98.7% |
|  | 4 | `2c5 4b4 4a3 (4a2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 (4a1 0c0)`) | 91.4% | 99.1% |
|  | 5 | `2c5 4b4 (4b5 2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 4a1 (0c0)`) | 91.8% | 99.2% |
|  | 6 | `2c5 4b4 4a3 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 (4a1 0c0)`) | 91.9% | 99.3% |
|  | 7 | `2c5 4b4 2c5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 (4a1 0c0)`) | 92.0% | 99.3% |
|  | 8 | `2c5 4b4 2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 2c5 2c4 2c3 (4b2 4a1 0c0)`) | 92.1% | 99.3% |
| 2c5 2e | 1 | `2c5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 (4a1 0c0)`) | 74.8% | 94.2% |
|  | 2 | `2c5 2c4 2c3 4b2 4a1 0c0` | 86.2% | 97.7% |
|  | 3 | `2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 4a1 (0c0)`) | 91.0% | 98.7% |
|  | 4 | `2c5 4b4 4a3 (4a2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 (4a1 0c0)`) | 92.4% | 99.1% |
|  | 5 | `2c5 4b4 (4b5 2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 4a1 (0c0)`) | 92.9% | 99.4% |
|  | 6 | `2c5 4b4 2c5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 (4a1 0c0)`) | 93.1% | 99.4% |
|  | 7 | `2c5 4b4 4a3 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 (4a1 0c0)`) | 93.2% | 99.5% |
|  | 8 | `2c5 2c4 2c3 4b2 4a1 (0c0)` (mirror: `2c5 2c4 (2c3 4b2 4a1 0c0)`) | 93.2% | 99.5% |
| 2c5 4e | 1 | `2c5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 (4a1 0c0)`) | 71.5% | 92.8% |
|  | 2 | `2c5 2c4 2c3 4b2 4a1 0c0` | 86.0% | 97.8% |
|  | 3 | `2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 4a1 (0c0)`) | 91.9% | 99.0% |
|  | 4 | `2c5 4b4 4a3 (4a2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 (4a1 0c0)`) | 93.2% | 99.4% |
|  | 5 | `2c5 4b4 2c5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 (4a1 0c0)`) | 93.4% | 99.5% |
|  | 6 | `2c5 4b4 (4b5 2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 4a1 (0c0)`) | 93.6% | 99.5% |
|  | 7 | `2c5 4b4 4a3 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 (4a1 0c0)`) | 93.7% | 99.6% |
|  | 8 | `2c5 4b4 2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 2c5 2c4 2c3 (4b2 4a1 0c0)`) | 93.8% | 99.6% |
| 2c5 6e | 1 | `2c5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 (4a1 0c0)`) | 73.0% | 93.3% |
|  | 2 | `2c5 2c4 2c3 4b2 4a1 0c0` | 84.1% | 97.3% |
|  | 3 | `2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 4a1 (0c0)`) | 90.6% | 98.7% |
|  | 4 | `2c5 4b4 4a3 (4a2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 (4a1 0c0)`) | 92.4% | 99.3% |
|  | 5 | `2c5 4b4 4a3 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 (4a1 0c0)`) | 92.7% | 99.4% |
|  | 6 | `2c5 4b4 2c5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 (4a1 0c0)`) | 92.9% | 99.5% |
|  | 7 | `2c5 4b4 4a3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `2c5 2c4 2c3 2c4 (2c3 4b2 4a1 0c0)`) | 93.0% | 99.5% |
|  | 8 | `2c5 2c4 2c3 4b2 4a1 (0c0)` (mirror: `2c5 2c4 (2c3 4b2 4a1 0c0)`) | 93.2% | 99.5% |
| 2c5 8e | 1 | `2c5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 (4a1 0c0)`) | 77.6% | 94.9% |
|  | 2 | `2c5 2c4 2c3 4b2 4a1 (0c0)` (mirror: `2c5 2c4 (2c3 4b2 4a1 0c0)`) | 86.0% | 97.6% |
|  | 3 | `2c5 2c4 2c3 4b2 4a1 0c0` | 91.0% | 98.9% |
|  | 4 | `2c5 4b4 4a3 (4a2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 (4a1 0c0)`) | 92.2% | 99.3% |
|  | 5 | `2c5 4b4 (4b5 2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 4a1 (0c0)`) | 92.5% | 99.4% |
|  | 6 | `2c5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c5 2c4 2c3 4b2 4a1 (0c0)`) | 92.7% | 99.4% |
|  | 7 | `2c5 4b4 4a3 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c5 4b4 4a3 4b2 2c3 4b2 (4a1 0c0)`) | 92.9% | 99.5% |
|  | 8 | `2c5 4b4 4a3 4b2 4a1 (0c0)` (mirror: `2c5 2c4 (4b3 4a2 4a1 0c0)`) | 93.0% | 99.5% |
| 2c4 0e | 1 | `2c4 2c3 4b2 4a1 0c0` | 70.1% | 91.8% |
|  | 2 | `2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b3 4a2 4a1 (0c0)`) | 85.9% | 98.0% |
|  | 3 | `2c4 2c3 4b2 (4a1 0c0)` (mirror: `2c4 4b3 4a2 (4a1 0c0)`) | 88.6% | 98.7% |
|  | 4 | `2c4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c4 4b5 2c4 2c3 4b2 (4a1 0c0)`) | 88.8% | 98.8% |
|  | 5 | `2c4 2c3 4b2 4a1 (0c0)` (mirror: `2c4 2c3 (4b2 4a1 0c0)`) | 88.9% | 98.8% |
|  | 6 | `2c4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b5 4a4 4a3 (4a2 4a1 0c0)`) | 89.0% | 98.8% |
|  | 7 | `2c4 2c5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c4 2c3 4b2 4a1 0c0 4a1 (0c0)`) | 89.1% | 98.8% |
|  | 8 | `2c4 4b5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c4 2c3 4b2 2c3 4b2 4a1 (0c0)`) | 89.2% | 98.8% |
| 2c4 2e | 1 | `2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b3 4a2 4a1 (0c0)`) | 67.7% | 91.3% |
|  | 2 | `2c4 2c3 4b2 4a1 0c0` | 86.3% | 97.8% |
|  | 3 | `2c4 2c3 4b2 (4a1 0c0)` (mirror: `2c4 4b3 4a2 (4a1 0c0)`) | 89.9% | 98.9% |
|  | 4 | `2c4 4b5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c4 2c3 4b2 2c3 4b2 4a1 (0c0)`) | 90.5% | 99.0% |
|  | 5 | `2c4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c4 4b5 2c4 2c3 4b2 (4a1 0c0)`) | 90.8% | 99.1% |
|  | 6 | `2c4 4b3 4a2 4a1 0c0` | 91.0% | 99.1% |
|  | 7 | `2c4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b5 4a4 4a3 (4a2 4a1 0c0)`) | 91.2% | 99.1% |
|  | 8 | `2c4 2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c4 4b5 2c4 4b3 4a2 (4a1 0c0)`) | 91.3% | 99.1% |
| 2c4 4e | 1 | `2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b3 4a2 4a1 (0c0)`) | 62.0% | 88.0% |
|  | 2 | `2c4 2c3 4b2 4a1 0c0` | 82.0% | 97.0% |
|  | 3 | `2c4 2c3 4b2 (4a1 0c0)` (mirror: `2c4 4b3 4a2 (4a1 0c0)`) | 87.6% | 98.7% |
|  | 4 | `2c4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c4 4b5 2c4 2c3 4b2 (4a1 0c0)`) | 88.1% | 98.8% |
|  | 5 | `2c4 4b5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c4 2c3 4b2 2c3 4b2 4a1 (0c0)`) | 88.4% | 98.8% |
|  | 6 | `2c4 2c3 4b2 4a1 (0c0)` (mirror: `2c4 2c3 (4b2 4a1 0c0)`) | 88.7% | 98.9% |
|  | 7 | `2c4 4b3 4a2 4a1 0c0` | 88.9% | 98.9% |
|  | 8 | `2c4 2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c4 4b5 2c4 4b3 4a2 (4a1 0c0)`) | 89.1% | 98.9% |
| 2c4 6e | 1 | `2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b3 4a2 4a1 (0c0)`) | 73.8% | 94.2% |
|  | 2 | `2c4 2c3 4b2 4a1 0c0` | 84.1% | 97.3% |
|  | 3 | `2c4 2c3 4b2 (4a1 0c0)` (mirror: `2c4 4b3 4a2 (4a1 0c0)`) | 88.5% | 98.6% |
|  | 4 | `2c4 4b5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c4 2c3 4b2 2c3 4b2 4a1 (0c0)`) | 89.2% | 98.8% |
|  | 5 | `2c4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c4 4b5 2c4 2c3 4b2 (4a1 0c0)`) | 89.6% | 98.8% |
|  | 6 | `2c4 4b3 4a2 4a1 0c0` | 90.0% | 98.9% |
|  | 7 | `2c4 2c3 4b2 4a1 (0c0)` (mirror: `2c4 2c3 (4b2 4a1 0c0)`) | 90.1% | 98.9% |
|  | 8 | `2c4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b5 4a4 4a3 (4a2 4a1 0c0)`) | 90.3% | 98.9% |
| 2c4 8e | 1 | `2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b3 4a2 4a1 (0c0)`) | 77.7% | 95.3% |
|  | 2 | `2c4 2c3 4b2 (4a1 0c0)` (mirror: `2c4 4b3 4a2 (4a1 0c0)`) | 89.5% | 99.3% |
|  | 3 | `2c4 2c3 4b2 4a1 0c0` | 91.5% | 99.4% |
|  | 4 | `2c4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c4 4b5 2c4 2c3 4b2 (4a1 0c0)`) | 92.3% | 99.5% |
|  | 5 | `2c4 2c3 4b2 4a1 (0c0)` (mirror: `2c4 2c3 (4b2 4a1 0c0)`) | 92.9% | 99.6% |
|  | 6 | `2c4 4b5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `2c4 2c3 4b2 2c3 4b2 4a1 (0c0)`) | 93.3% | 99.6% |
|  | 7 | `2c4 2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c4 4b5 2c4 4b3 4a2 (4a1 0c0)`) | 93.5% | 99.6% |
|  | 8 | `2c4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c4 4b5 4a4 4a3 (4a2 4a1 0c0)`) | 93.7% | 99.6% |
| 0c3 0e | 1 | `0c3 4a2 (4a1 0c0)` (mirror: `0c3 4a2 4a1 (0c0)`) | 85.5% | 97.3% |
|  | 2 | `0c3 4a2 4b3 4a2 4a1 (0c0)` (mirror: `0c3 4a2 (4a1 4b2 4a1 0c0)`) | 94.2% | 99.5% |
|  | 3 | `0c3 4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4b3 2c4 (2c3 4b2 4a1 0c0)`) | 96.6% | 99.8% |
|  | 4 | `0c3 4a4 4b5 2c4 2c3 4b2 4a1 0c0` | 96.9% | 99.8% |
|  | 5 | `0c3 4a2 (4b3 4a2 4a1 0c0)` (mirror: `0c3 4a4 0c3 4a2 4a1 (0c0)`) | 97.2% | 99.8% |
|  | 6 | `0c3 4a4 4b5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `0c3 4a4 4b5 2c4 2c3 4b2 (4a1 0c0)`) | 97.3% | 99.8% |
|  | 7 | `0c3 4a2 4b3 2c4 (2c3 4b2 4a1 0c0)` (mirror: `0c3 4a4 4b5 2c4 2c3 (4b2 4a1 0c0)`) | 97.4% | 99.9% |
|  | 8 | `0c3 4a4 (2c5 2c4 2c3 4b2 4a1 0c0)` (mirror: `0c3 4a4 4b5 2c4 2c3 4b2 4a1 (0c0)`) | 97.4% | 99.9% |
| 0c3 2e | 1 | `0c3 4a2 (4a1 0c0)` (mirror: `0c3 4a2 4a1 (0c0)`) | 80.8% | 97.5% |
|  | 2 | `0c3 4a2 4b3 4a2 4a1 (0c0)` (mirror: `0c3 4a2 (4a1 4b2 4a1 0c0)`) | 91.3% | 99.3% |
|  | 3 | `0c3 4a2 4a1 0c0` | 92.1% | 99.5% |
|  | 4 | `0c3 4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4b3 2c4 (2c3 4b2 4a1 0c0)`) | 92.5% | 99.6% |
|  | 5 | `0c3 4a2 (4b3 4a2 4a1 0c0)` (mirror: `0c3 4a4 0c3 4a2 4a1 (0c0)`) | 92.8% | 99.6% |
|  | 6 | `0c3 4a4 4b5 2c4 2c3 4b2 4a1 (0c0)` (mirror: `0c3 4a4 (2c5 2c4 2c3 4b2 4a1 0c0)`) | 93.0% | 99.6% |
|  | 7 | `0c3 4a2 4b3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4a1 4b2 (4a1 0c0)`) | 93.2% | 99.6% |
|  | 8 | `0c3 4a4 4b5 2c4 2c3 4b2 (4a1 0c0)` (mirror: `0c3 4a4 4b5 (2c4 2c3 4b2 4a1 0c0)`) | 93.3% | 99.6% |
| 0c3 4e | 1 | `0c3 4a2 (4a1 0c0)` (mirror: `0c3 4a2 4a1 (0c0)`) | 67.2% | 94.5% |
|  | 2 | `0c3 4a2 4b3 4a2 4a1 (0c0)` (mirror: `0c3 4a2 (4a1 4b2 4a1 0c0)`) | 85.1% | 98.7% |
|  | 3 | `0c3 4a2 4b3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4a1 4b2 (4a1 0c0)`) | 85.8% | 98.7% |
|  | 4 | `0c3 4a4 4b5 2c4 2c3 4b2 (4a1 0c0)` (mirror: `0c3 4a4 4b5 (2c4 2c3 4b2 4a1 0c0)`) | 86.4% | 98.9% |
|  | 5 | `0c3 4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4b3 2c4 (2c3 4b2 4a1 0c0)`) | 86.8% | 98.9% |
|  | 6 | `0c3 4a2 (4b3 4a2 4a1 0c0)` (mirror: `0c3 4a4 0c3 4a2 4a1 (0c0)`) | 87.2% | 98.9% |
|  | 7 | `0c3 4a4 4b5 2c4 2c3 4b2 4a1 (0c0)` (mirror: `0c3 4a4 (2c5 2c4 2c3 4b2 4a1 0c0)`) | 87.4% | 99.0% |
|  | 8 | `0c3 4a2 4b3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4b3 2c4 (2c3 4b2 4a1 0c0)`) | 87.5% | 99.0% |
| 0c3 6e | 1 | `0c3 4a2 (4a1 0c0)` (mirror: `0c3 4a2 4a1 (0c0)`) | 82.6% | 98.0% |
|  | 2 | `0c3 4a2 4b3 4a2 4a1 (0c0)` (mirror: `0c3 4a2 (4a1 4b2 4a1 0c0)`) | 93.9% | 99.5% |
|  | 3 | `0c3 4a2 4a1 0c0` | 94.6% | 99.7% |
|  | 4 | `0c3 4a2 (4b3 4a2 4a1 0c0)` (mirror: `0c3 4a4 0c3 4a2 4a1 (0c0)`) | 94.9% | 99.7% |
|  | 5 | `0c3 4a2 4b3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4a1 4b2 (4a1 0c0)`) | 95.2% | 99.7% |
|  | 6 | `0c3 4a4 4b5 2c4 2c3 4b2 4a1 (0c0)` (mirror: `0c3 4a4 (2c5 2c4 2c3 4b2 4a1 0c0)`) | 95.3% | 99.7% |
|  | 7 | `0c3 4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4b3 2c4 (2c3 4b2 4a1 0c0)`) | 95.4% | 99.7% |
|  | 8 | `0c3 4a4 4b5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `0c3 4a4 4b5 2c4 2c3 4b2 (4a1 0c0)`) | 95.5% | 99.7% |
| 0c3 8e | 1 | `0c3 4a2 (4a1 0c0)` (mirror: `0c3 4a2 4a1 (0c0)`) | 87.3% | 98.0% |
|  | 2 | `0c3 4a2 4b3 4a2 4a1 (0c0)` (mirror: `0c3 4a2 (4a1 4b2 4a1 0c0)`) | 94.8% | 99.5% |
|  | 3 | `0c3 4a4 4b5 2c4 2c3 4b2 (4a1 0c0)` (mirror: `0c3 4a4 4b5 (2c4 2c3 4b2 4a1 0c0)`) | 96.1% | 99.7% |
|  | 4 | `0c3 4a2 4b3 2c4 2c3 4b2 (4a1 0c0)` (mirror: `0c3 4a4 4b5 (2c4 4b3 4a2 4a1 0c0)`) | 96.5% | 99.7% |
|  | 5 | `0c3 4a4 4b5 2c4 2c3 4b2 4a1 0c0` | 96.8% | 99.7% |
|  | 6 | `0c3 4a4 (2c5 2c4 2c3 4b2 4a1 0c0)` (mirror: `0c3 4a4 4b5 2c4 2c3 4b2 4a1 (0c0)`) | 97.0% | 99.7% |
|  | 7 | `0c3 4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `0c3 4a4 4b5 2c4 2c3 (4b2 4a1 0c0)`) | 97.1% | 99.8% |
|  | 8 | `0c3 4a2 4b3 (4b2 4a1 0c0)` (mirror: `0c3 4a2 4a1 4b2 (4a1 0c0)`) | 97.2% | 99.8% |
| 4a2 0e | 1 | `4a2 4b3 4a2 4a1 (0c0)` (mirror: `4a2 4a1 (4b2 4a1 0c0)`) | 29.1% | 46.4% |
|  | 2 | `4a2 4a1 4b2 4a1 0c0` | 40.4% | 56.4% |
|  | 3 | `4a2 4a1 (0c0)` | 44.4% | 68.2% |
|  | 4 | `4a2 4a1 4b2 (4a1 0c0)` | 48.2% | 73.3% |
|  | 5 | `4a2 4a1 (0c0 4a1 0c0)` (mirror: `4a2 4a1 4a2 4a1 (0c0)`) | 50.3% | 74.6% |
|  | 6 | `4a2 4b3 (4b2 2c3 4b2 4a1 0c0)` (mirror: `4a2 4b3 2c4 2c3 4b2 4a1 (0c0)`) | 52.1% | 75.5% |
|  | 7 | `4a2 4b3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4a2 4a1 4b2 2c3 (4b2 4a1 0c0)`) | 52.8% | 75.8% |
|  | 8 | `4a2 4b3 2c4 2c3 4b2 (4a1 0c0)` (mirror: `4a2 4b3 2c4 (2c3 4b2 4a1 0c0)`) | 53.1% | 75.9% |
| 4a2 2e | 1 | `4a2 4b3 4a2 4a1 (0c0)` (mirror: `4a2 4a1 (4b2 4a1 0c0)`) | 42.2% | 77.2% |
|  | 2 | `4a2 4a1 (0c0)` | 67.8% | 92.0% |
|  | 3 | `4a2 4a1 4b2 4a1 0c0` | 76.8% | 95.7% |
|  | 4 | `4a2 4a1 (0c0 4a1 0c0)` (mirror: `4a2 4a1 4a2 4a1 (0c0)`) | 79.6% | 96.9% |
|  | 5 | `4a2 4a1 4b2 (4a1 0c0)` | 81.4% | 97.6% |
|  | 6 | `4a2 4b3 2c4 2c3 4b2 4a1 0c0` | 82.4% | 97.8% |
|  | 7 | `4a2 4b3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4a2 4a1 4b2 2c3 (4b2 4a1 0c0)`) | 83.1% | 98.0% |
|  | 8 | `4a2 4b3 (4b2 2c3 4b2 4a1 0c0)` (mirror: `4a2 4b3 2c4 2c3 4b2 4a1 (0c0)`) | 83.6% | 98.1% |
| 4a2 4e | 1 | `4a2 4a1 0c0` | 60.9% | 83.9% |
|  | 2 | `4a2 4b3 4a2 4a1 (0c0)` (mirror: `4a2 4a1 (4b2 4a1 0c0)`) | 72.2% | 91.1% |
|  | 3 | `4a2 4a1 4b2 4a1 0c0` | 79.1% | 93.6% |
|  | 4 | `4a2 4a1 (0c0)` | 83.7% | 95.9% |
|  | 5 | `4a2 4a1 (0c0 4a1 0c0)` (mirror: `4a2 4a1 4a2 4a1 (0c0)`) | 85.3% | 96.5% |
|  | 6 | `4a2 4a1 4b2 (4a1 0c0)` | 86.1% | 96.9% |
|  | 7 | `4a2 4b3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4a2 4a1 4b2 2c3 (4b2 4a1 0c0)`) | 86.3% | 96.9% |
|  | 8 | `4a2 4b3 (4b2 2c3 4b2 4a1 0c0)` (mirror: `4a2 4b3 2c4 2c3 4b2 4a1 (0c0)`) | 86.4% | 97.0% |
| 4a1 0e | 1 | `4a1 0c0 (4a1 0c0)` (mirror: `4a1 4a2 4a1 (0c0)`) | 33.5% | 56.5% |
|  | 2 | `4a1 4b2 2c3 4b2 4a1 (0c0)` (mirror: `4a1 4b2 (2c3 4b2 4a1 0c0)`) | 46.5% | 71.3% |
|  | 3 | `4a1 0c0 4a1 (0c0)` (mirror: `4a1 4a2 (4a1 0c0)`) | 54.6% | 84.2% |
|  | 4 | `4a1 4b2 2c3 4b2 4a1 0c0` | 61.1% | 87.8% |
|  | 5 | `4a1 0c0 4a1 0c0` | 66.5% | 90.7% |
|  | 6 | `4a1 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4a1 4b2 2c3 4b2 (4a1 0c0)`) | 70.5% | 92.4% |
|  | 7 | `4a1 4b2 4a1 0c0 4a1 (0c0)` (mirror: `4a1 4b2 (2c3 4b2 4a1 0c0)`) | 71.7% | 92.9% |
|  | 8 | `4a1 4b2 4a1 0c0 (4a1 0c0)` (mirror: `4a1 4b2 4a1 (4b2 4a1 0c0)`) | 72.2% | 92.9% |
| 4a1 2e | 1 | `4a1 4b2 4a1 0c0` | 38.8% | 67.5% |
|  | 2 | `4a1 0c0 4a1 0c0` | 58.8% | 85.8% |
|  | 3 | `4a1 0c0 (4a1 0c0)` (mirror: `4a1 4a2 4a1 (0c0)`) | 70.5% | 91.7% |
|  | 4 | `4a1 0c0 4a1 (0c0)` (mirror: `4a1 4a2 (4a1 0c0)`) | 76.7% | 95.4% |
|  | 5 | `4a1 4b2 (2c3 4b2 4a1 0c0)` (mirror: `4a1 4b2 2c3 4b2 4a1 (0c0)`) | 78.2% | 96.0% |
|  | 6 | `4a1 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4a1 4b2 2c3 4b2 (4a1 0c0)`) | 79.0% | 96.2% |
|  | 7 | `4a1 0c0 4a1 (4b2 4a1 0c0)` (mirror: `4a1 4a2 4a1 4b2 (4a1 0c0)`) | 79.4% | 96.4% |
|  | 8 | `4a1 4b2 2c3 4b2 4a1 0c0` | 79.8% | 96.5% |
| 4a1 4e | 1 | `4a1 0c0` | 33.6% | 57.1% |
|  | 2 | `4a1 4b2 4a1 0c0` | 50.3% | 78.3% |
|  | 3 | `4a1 0c0 (4a1 0c0)` (mirror: `4a1 4a2 4a1 (0c0)`) | 60.6% | 86.2% |
|  | 4 | `4a1 0c0 4a1 (0c0)` (mirror: `4a1 4a2 (4a1 0c0)`) | 66.6% | 91.1% |
|  | 5 | `4a1 0c0 4a1 0c0` | 69.5% | 92.2% |
|  | 6 | `4a1 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4a1 4b2 2c3 4b2 (4a1 0c0)`) | 70.1% | 92.5% |
|  | 7 | `4a1 4b2 (2c3 4b2 4a1 0c0)` (mirror: `4a1 4b2 2c3 4b2 4a1 (0c0)`) | 70.5% | 92.7% |
|  | 8 | `4a1 0c0 \| qt` (mirror: `4a1 4b2 (4a1 4b2 4a1 0c0)`) | 70.7% | 93.1% |
| 2c3 0e | 1 | `2c3 4b2 (4a1 0c0)` (mirror: `2c3 4b2 4a1 (0c0)`) | 46.3% | 81.8% |
|  | 2 | `2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c3 2c4 2c3 4b2 4a1 (0c0)`) | 67.0% | 93.7% |
|  | 3 | `2c3 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 4a1 (0c0)`) | 75.1% | 95.9% |
|  | 4 | `2c3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 (4a1 0c0)`) | 81.4% | 97.5% |
|  | 5 | `2c3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c3 4b2 4a3 4b2 (4a1 0c0)`) | 85.5% | 98.4% |
|  | 6 | `2c3 2c4 2c3 4b2 4a1 0c0` | 86.7% | 98.5% |
|  | 7 | `2c3 4b2 4a1 (0c0 4a1 0c0)` (mirror: `2c3 4b2 4a3 4b2 (4a1 0c0)`) | 87.4% | 98.7% |
|  | 8 | `2c3 4b2 2c3 4b2 4a1 0c0` | 88.1% | 98.8% |
| 2c3 2e | 1 | `2c3 4b2 4a1 0c0` | 66.5% | 89.6% |
|  | 2 | `2c3 4b2 (4a1 0c0)` (mirror: `2c3 4b2 4a1 (0c0)`) | 79.6% | 96.4% |
|  | 3 | `2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c3 2c4 2c3 4b2 4a1 (0c0)`) | 80.2% | 96.6% |
|  | 4 | `2c3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 (4a1 0c0)`) | 80.6% | 96.7% |
|  | 5 | `2c3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c3 4b2 4a3 4b2 (4a1 0c0)`) | 80.8% | 96.7% |
|  | 6 | `2c3 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 4a1 (0c0)`) | 81.0% | 96.8% |
|  | 7 | `2c3 2c4 2c3 4b2 4a1 0c0` | 81.2% | 96.8% |
|  | 8 | `2c3 4b2 2c3 4b2 4a1 0c0` | 81.2% | 96.8% |
| 2c3 4e | 1 | `2c3 4b2 4a1 0c0` | 55.3% | 82.1% |
|  | 2 | `2c3 4b2 (4a1 0c0)` (mirror: `2c3 4b2 4a1 (0c0)`) | 76.6% | 95.6% |
|  | 3 | `2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c3 2c4 2c3 4b2 4a1 (0c0)`) | 78.1% | 96.1% |
|  | 4 | `2c3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 (4a1 0c0)`) | 79.1% | 96.4% |
|  | 5 | `2c3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c3 4b2 4a3 4b2 (4a1 0c0)`) | 79.9% | 96.6% |
|  | 6 | `2c3 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 4a1 (0c0)`) | 80.6% | 96.9% |
|  | 7 | `2c3 4b2 2c3 4b2 4a1 0c0` | 80.9% | 97.0% |
|  | 8 | `2c3 2c4 2c3 4b2 4a1 0c0` | 81.2% | 97.0% |
| 2c3 6e | 1 | `2c3 4b2 (4a1 0c0)` (mirror: `2c3 4b2 4a1 (0c0)`) | 66.1% | 91.8% |
|  | 2 | `2c3 4b2 4a1 0c0` | 73.3% | 94.7% |
|  | 3 | `2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c3 2c4 2c3 4b2 4a1 (0c0)`) | 76.7% | 95.8% |
|  | 4 | `2c3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c3 4b2 4a3 4b2 (4a1 0c0)`) | 78.3% | 96.3% |
|  | 5 | `2c3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 (4a1 0c0)`) | 79.8% | 96.7% |
|  | 6 | `2c3 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 4a1 (0c0)`) | 80.8% | 96.9% |
|  | 7 | `2c3 2c4 2c3 4b2 4a1 0c0` | 81.2% | 97.0% |
|  | 8 | `2c3 4b2 2c3 4b2 4a1 0c0` | 81.6% | 97.1% |
| 2c3 8e | 1 | `2c3 4b2 (4a1 0c0)` (mirror: `2c3 4b2 4a1 (0c0)`) | 46.3% | 81.2% |
|  | 2 | `2c3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `2c3 2c4 2c3 4b2 4a1 (0c0)`) | 67.2% | 93.2% |
|  | 3 | `2c3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 (4a1 0c0)`) | 74.5% | 95.7% |
|  | 4 | `2c3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `2c3 4b2 4a3 4b2 (4a1 0c0)`) | 78.3% | 96.8% |
|  | 5 | `2c3 2c4 2c3 4b2 4a1 0c0` | 81.3% | 97.5% |
|  | 6 | `2c3 4b2 2c3 4b2 4a1 0c0` | 83.4% | 98.0% |
|  | 7 | `2c3 2c4 (2c3 4b2 4a1 0c0)` (mirror: `2c3 4b2 2c3 4b2 4a1 (0c0)`) | 85.5% | 98.4% |
|  | 8 | `2c3 4b2 4a1 (0c0 4a1 0c0)` (mirror: `2c3 4b2 4a3 4b2 (4a1 0c0)`) | 85.9% | 98.4% |
| 0c4 0e | 1 | `0c4 4a3 4b2 (4a1 0c0)` | 83.2% | 95.4% |
|  | 2 | `0c4 4a3 4b2 4a1 0c0` | 86.8% | 97.3% |
|  | 3 | `0c4 4a3 (4a2 4a1 0c0)` (mirror: `0c4 4a3 4b2 4a1 (0c0)`) | 87.6% | 97.5% |
|  | 4 | `0c4 4a3 4b2 2c3 (4b2 4a1 0c0)` | 88.0% | 97.7% |
|  | 5 | `0c4 4a3 4b2 2c3 4b2 4a1 (0c0)` (mirror: `0c4 4a3 (2c4 2c3 4b2 4a1 0c0)`) | 88.3% | 97.7% |
|  | 6 | `0c4 4a3 4b2 2c3 4b2 (4a1 0c0)` (mirror: `0c4 4a3 4b2 (2c3 4b2 4a1 0c0)`) | 88.4% | 97.7% |
|  | 7 | `0c4 4a3 4b2 2c3 4b2 4a1 0c0` | 88.5% | 97.7% |
| 0c4 2e | 1 | `0c4 4a3 4b2 (4a1 0c0)` | 86.5% | 97.3% |
|  | 2 | `0c4 4a3 4b2 4a1 0c0` | 88.0% | 97.7% |
|  | 3 | `0c4 4a3 4b2 2c3 4b2 4a1 (0c0)` (mirror: `0c4 4a3 (2c4 2c3 4b2 4a1 0c0)`) | 89.1% | 98.1% |
|  | 4 | `0c4 4a3 4b2 2c3 (4b2 4a1 0c0)` | 89.9% | 98.2% |
|  | 5 | `0c4 4a3 (4a2 4a1 0c0)` (mirror: `0c4 4a3 4b2 4a1 (0c0)`) | 90.6% | 98.5% |
|  | 6 | `0c4 4a3 4b2 2c3 4b2 (4a1 0c0)` (mirror: `0c4 4a3 4b2 (2c3 4b2 4a1 0c0)`) | 91.0% | 98.5% |
|  | 7 | `0c4 4a3 4b2 2c3 4b2 4a1 0c0` | 91.2% | 98.6% |
|  | 8 | `0c4 4a3 0c4 4a3 4b2 (4a1 0c0)` (mirror: `0c4 4a3 4b2 (4a1 4b2 4a1 0c0)`) | 91.2% | 98.6% |
| 0c4 4e | 1 | `0c4 4a3 4b2 (4a1 0c0)` | 83.5% | 96.8% |
|  | 2 | `0c4 4a3 4b2 4a1 0c0` | 85.1% | 97.2% |
|  | 3 | `0c4 4a3 (4a2 4a1 0c0)` (mirror: `0c4 4a3 4b2 4a1 (0c0)`) | 86.1% | 97.5% |
|  | 4 | `0c4 4a3 4b2 2c3 (4b2 4a1 0c0)` | 87.1% | 97.7% |
|  | 5 | `0c4 4a3 4b2 2c3 4b2 4a1 (0c0)` (mirror: `0c4 4a3 (2c4 2c3 4b2 4a1 0c0)`) | 87.8% | 97.9% |
|  | 6 | `0c4 4a3 4b2 2c3 4b2 (4a1 0c0)` (mirror: `0c4 4a3 4b2 (2c3 4b2 4a1 0c0)`) | 88.3% | 98.0% |
|  | 7 | `0c4 4a3 4b2 2c3 4b2 4a1 0c0` | 88.6% | 98.1% |
|  | 8 | `0c4 4a3 4b2 (4a1 4b2 4a1 0c0)` (mirror: `0c4 4a3 4b4 4a3 4b2 (4a1 0c0)`) | 88.6% | 98.1% |
| 0c4 6e | 1 | `0c4 4a3 4b2 (4a1 0c0)` | 81.8% | 96.6% |
|  | 2 | `0c4 4a3 (4a2 4a1 0c0)` (mirror: `0c4 4a3 4b2 4a1 (0c0)`) | 83.7% | 97.3% |
|  | 3 | `0c4 4a3 4b2 2c3 4b2 4a1 (0c0)` (mirror: `0c4 4a3 (2c4 2c3 4b2 4a1 0c0)`) | 85.4% | 97.8% |
|  | 4 | `0c4 4a3 4b2 2c3 (4b2 4a1 0c0)` | 86.5% | 98.0% |
|  | 5 | `0c4 4a3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `0c4 4a3 4b2 2c3 4b2 (4a1 0c0)`) | 87.3% | 98.2% |
|  | 6 | `0c4 4a3 4b2 4a1 0c0` | 87.7% | 98.2% |
|  | 7 | `0c4 4a3 4b2 2c3 4b2 4a1 0c0` | 88.0% | 98.3% |
|  | 8 | `0c4 4a3 4b2 (4a1 0c0 4a1 0c0)` (mirror: `0c4 4a3 4b2 2c3 4b2 (4a1 0c0)`) | 88.1% | 98.3% |
| 0c4 8e | 1 | `0c4 4a3 4b2 (4a1 0c0)` | 80.3% | 96.2% |
|  | 2 | `0c4 4a3 (4a2 4a1 0c0)` (mirror: `0c4 4a3 4b2 4a1 (0c0)`) | 86.2% | 98.0% |
|  | 3 | `0c4 4a3 4b2 2c3 4b2 4a1 (0c0)` (mirror: `0c4 4a3 (2c4 2c3 4b2 4a1 0c0)`) | 87.1% | 98.2% |
|  | 4 | `0c4 4a3 4b2 2c3 (4b2 4a1 0c0)` | 87.9% | 98.4% |
|  | 5 | `0c4 4a3 4b2 2c3 4b2 (4a1 0c0)` (mirror: `0c4 4a3 4b2 (2c3 4b2 4a1 0c0)`) | 88.1% | 98.4% |
|  | 6 | `0c4 4a3 4b2 4a1 0c0` | 88.3% | 98.4% |
| 4c3 0e | 1 | `4a3 4b2 (4a1 0c0)` (mirror: `4b3 4a2 4a1 (0c0)`) | 70.8% | 90.7% |
|  | 2 | `4a3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b3 2c4 2c3 4b2 (4a1 0c0)`) | 78.4% | 94.5% |
|  | 3 | `4b3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4a3 0c4 4a3 4b2 (4a1 0c0)`) | 83.3% | 96.2% |
|  | 4 | `4b3 2c4 2c3 4b2 4a1 0c0` | 86.3% | 97.0% |
|  | 5 | `4b3 4a2 4a1 0c0` | 88.6% | 98.5% |
|  | 6 | `4a3 4b2 2c3 4b2 4a1 (0c0)` (mirror: `4b3 2c4 (2c3 4b2 4a1 0c0)`) | 90.2% | 98.8% |
|  | 7 | `4a3 4b2 2c3 4b2 4a1 0c0` | 91.5% | 99.1% |
|  | 8 | `4a3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `4b3 2c4 2c3 4b2 4a1 (0c0)`) | 92.3% | 99.2% |
| 4c3 2e | 1 | `4a3 4b2 (4a1 0c0)` (mirror: `4b3 4a2 4a1 (0c0)`) | 66.2% | 90.6% |
|  | 2 | `4b3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4a3 0c4 4a3 4b2 (4a1 0c0)`) | 72.0% | 93.0% |
|  | 3 | `4a3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b3 2c4 2c3 4b2 (4a1 0c0)`) | 75.1% | 94.3% |
|  | 4 | `4b3 4a2 4a1 0c0` | 77.9% | 95.7% |
|  | 5 | `4b3 2c4 2c3 4b2 4a1 0c0` | 80.1% | 96.2% |
|  | 6 | `4a3 4b2 4a1 0c0` | 81.8% | 96.8% |
|  | 7 | `4a3 4b2 2c3 4b2 4a1 (0c0)` (mirror: `4b3 2c4 (2c3 4b2 4a1 0c0)`) | 83.2% | 97.3% |
|  | 8 | `4a3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `4b3 2c4 2c3 4b2 4a1 (0c0)`) | 84.4% | 97.5% |
| 4c3 4e | 1 | `4a3 4b2 (4a1 0c0)` (mirror: `4b3 4a2 4a1 (0c0)`) | 62.3% | 88.3% |
|  | 2 | `4b3 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4a3 0c4 4a3 4b2 (4a1 0c0)`) | 70.2% | 92.2% |
|  | 3 | `4a3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b3 2c4 2c3 4b2 (4a1 0c0)`) | 74.4% | 93.9% |
|  | 4 | `4b3 2c4 2c3 4b2 4a1 0c0` | 77.6% | 94.9% |
|  | 5 | `4a3 4b2 4a1 0c0` | 79.6% | 95.8% |
|  | 6 | `4a3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `4b3 2c4 2c3 4b2 4a1 (0c0)`) | 81.3% | 96.3% |
|  | 7 | `4b3 4a2 4a1 0c0` | 82.9% | 97.2% |
|  | 8 | `4a3 4b2 2c3 4b2 4a1 (0c0)` (mirror: `4b3 2c4 (2c3 4b2 4a1 0c0)`) | 84.4% | 97.5% |
| 4c4 0e | 1 | `4b4 4a3 4b2 (4a1 0c0)` (mirror: `4a4 0c3 4a2 (4a1 0c0)`) | 65.2% | 92.0% |
|  | 2 | `4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b4 2c5 4b4 4a3 (4a2 4a1 0c0)`) | 72.4% | 95.0% |
|  | 3 | `4b4 2c5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `4a4 4a3 4b2 2c3 4b2 4a1 (0c0)`) | 76.7% | 96.3% |
|  | 4 | `4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b4 4a3 0c4 4a3 4b2 (4a1 0c0)`) | 80.0% | 97.0% |
|  | 5 | `4b4 4a3 (2c4 2c3 4b2 4a1 0c0)` (mirror: `4a4 4b5 2c4 2c3 4b2 4a1 (0c0)`) | 81.9% | 97.4% |
|  | 6 | `4a4 4b5 2c4 2c3 4b2 (4a1 0c0)` (mirror: `4b4 4a3 0c4 (4a3 4b2 4a1 0c0)`) | 82.9% | 97.6% |
|  | 7 | `4b4 2c5 2c4 2c3 4b2 4a1 0c0` | 83.5% | 97.6% |
|  | 8 | `4b4 4a3 (4a2 4a1 0c0)` (mirror: `4a4 4a3 4b2 4a1 (0c0)`) | 84.1% | 97.8% |
| 4c4 2e | 1 | `4b4 4a3 4b2 (4a1 0c0)` (mirror: `4a4 0c3 4a2 (4a1 0c0)`) | 67.9% | 92.4% |
|  | 2 | `4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b4 4a3 0c4 4a3 4b2 (4a1 0c0)`) | 75.4% | 95.5% |
|  | 3 | `4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b4 2c5 4b4 4a3 (4a2 4a1 0c0)`) | 78.7% | 96.4% |
|  | 4 | `4b4 2c5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `4a4 4a3 4b2 2c3 4b2 4a1 (0c0)`) | 80.8% | 96.9% |
|  | 5 | `4b4 4a3 (2c4 2c3 4b2 4a1 0c0)` (mirror: `4a4 4b5 2c4 2c3 4b2 4a1 (0c0)`) | 82.1% | 97.2% |
|  | 6 | `4a4 4b5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `4b4 4a3 4b2 2c3 4b2 4a1 (0c0)`) | 83.3% | 97.4% |
|  | 7 | `4a4 4b5 2c4 2c3 4b2 4a1 0c0` | 84.2% | 97.6% |
|  | 8 | `4b4 2c5 2c4 2c3 4b2 4a1 0c0` | 85.2% | 97.7% |
| 4c4 4e | 1 | `4b4 4a3 4b2 (4a1 0c0)` (mirror: `4a4 0c3 4a2 (4a1 0c0)`) | 68.4% | 92.5% |
|  | 2 | `4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b4 4a3 0c4 4a3 4b2 (4a1 0c0)`) | 74.8% | 95.1% |
|  | 3 | `4a4 4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b4 2c5 4b4 4a3 (4a2 4a1 0c0)`) | 78.2% | 95.9% |
|  | 4 | `4b4 2c5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `4a4 4a3 4b2 2c3 4b2 4a1 (0c0)`) | 80.2% | 96.5% |
|  | 5 | `4b4 4a3 (2c4 2c3 4b2 4a1 0c0)` (mirror: `4a4 4b5 2c4 2c3 4b2 4a1 (0c0)`) | 81.5% | 96.7% |
|  | 6 | `4a4 4b5 (2c4 2c3 4b2 4a1 0c0)` (mirror: `4b4 4a3 4b2 2c3 4b2 4a1 (0c0)`) | 82.6% | 97.0% |
|  | 7 | `4b4 4a3 (4a2 4a1 0c0)` (mirror: `4a4 4a3 4b2 4a1 (0c0)`) | 83.6% | 97.4% |
|  | 8 | `4b4 2c5 2c4 2c3 4b2 4a1 0c0` | 84.6% | 97.5% |
| 4b2 0e | 1 | `4b2 4a1 0c0` | 36.5% | 64.3% |
|  | 2 | `4b2 2c3 4b2 (4a1 0c0)` (mirror: `4b2 4a1 0c0 (4a1 0c0)`) | 51.1% | 78.4% |
|  | 3 | `4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b2 2c3 4b2 4a1 (0c0)`) | 61.0% | 85.5% |
|  | 4 | `4b2 4a1 (0c0)` | 68.1% | 91.5% |
|  | 5 | `4b2 2c3 4b2 4a1 0c0` | 72.4% | 93.1% |
|  | 6 | `4b2 4a3 4b2 (4a1 0c0)` (mirror: `4b2 4a1 0c0 (4a1 0c0)`) | 75.5% | 94.4% |
|  | 7 | `4b2 2c3 4b2 4a1 (0c0)` (mirror: `4b2 2c3 (4b2 4a1 0c0)`) | 77.9% | 95.3% |
|  | 8 | `4b2 4a1 4b2 (4a1 0c0)` (mirror: `4b2 4a1 0c0 (4a1 0c0)`) | 78.4% | 95.5% |
| 4b2 2e | 1 | `4b2 4a1 0c0` | 45.9% | 76.5% |
|  | 2 | `4b2 2c3 4b2 4a1 (0c0)` (mirror: `4b2 2c3 (4b2 4a1 0c0)`) | 53.7% | 83.2% |
|  | 3 | `4b2 4a1 (0c0)` | 59.0% | 86.3% |
|  | 4 | `4b2 2c3 4b2 4a1 0c0` | 63.3% | 88.8% |
|  | 5 | `4b2 2c3 4b2 (4a1 0c0)` (mirror: `4b2 4a1 0c0 (4a1 0c0)`) | 66.3% | 90.1% |
|  | 6 | `4b2 4a3 4b2 (4a1 0c0)` (mirror: `4b2 4a1 0c0 (4a1 0c0)`) | 67.3% | 90.5% |
|  | 7 | `4b2 4a1 0c0 4a1 (0c0)` (mirror: `4b2 2c3 (4b2 4a1 0c0)`) | 68.2% | 91.3% |
|  | 8 | `4b2 4a1 (0c0 4a1 0c0)` (mirror: `4b2 4a1 4a2 4a1 (0c0)`) | 68.6% | 91.5% |
| 4b2 4e | 1 | `4b2 4a1 0c0` | 30.3% | 59.1% |
|  | 2 | `4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b2 2c3 4b2 4a1 (0c0)`) | 53.3% | 82.2% |
|  | 3 | `4b2 2c3 4b2 4a1 0c0` | 66.8% | 89.1% |
|  | 4 | `4b2 2c3 4b2 (4a1 0c0)` (mirror: `4b2 4a1 0c0 (4a1 0c0)`) | 71.7% | 91.1% |
|  | 5 | `4b2 4a1 (0c0)` | 76.0% | 94.9% |
|  | 6 | `4b2 2c3 4b2 4a1 (0c0)` (mirror: `4b2 2c3 (4b2 4a1 0c0)`) | 77.8% | 95.5% |
|  | 7 | `4b2 4a3 4b2 (4a1 0c0)` (mirror: `4b2 4a1 0c0 (4a1 0c0)`) | 79.3% | 96.0% |
|  | 8 | `4b2 4a1 (0c0 4a1 0c0)` (mirror: `4b2 4a1 4a2 4a1 (0c0)`) | 80.5% | 96.5% |
| 4b5 0e | 1 | `4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b5 2c4 4b3 4a2 (4a1 0c0)`) | 60.8% | 86.9% |
|  | 2 | `4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b5 2c4 2c3 4b2 4a1 (0c0)`) | 84.2% | 97.4% |
|  | 3 | `4b5 2c4 2c3 4b2 4a1 0c0` | 92.6% | 99.4% |
|  | 4 | `4b5 2c4 (4b3 4a2 4a1 0c0)` (mirror: `4b5 4a4 4a3 4b2 4a1 (0c0)`) | 92.8% | 99.4% |
|  | 5 | `4b5 2c4 4b3 4a2 4a1 0c0` | 93.0% | 99.4% |
|  | 6 | `4b5 2c4 2c3 4b2 (4a1 0c0)` (mirror: `4b5 2c4 2c3 (4b2 4a1 0c0)`) | 93.2% | 99.5% |
|  | 7 | `4b5 4a4 (2c5 2c4 2c3 4b2 4a1 0c0)` (mirror: `4b5 2c4 2c3 4b2 4a1 0c0 4a1 (0c0)`) | 93.2% | 99.5% |
|  | 8 | `4b5 4a4 4a3 4b2 4a1 0c0` | 93.3% | 99.5% |
| 4b5 2e | 1 | `4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b5 2c4 2c3 4b2 4a1 (0c0)`) | 62.6% | 88.0% |
|  | 2 | `4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b5 2c4 4b3 4a2 (4a1 0c0)`) | 85.1% | 98.0% |
|  | 3 | `4b5 2c4 2c3 4b2 4a1 0c0` | 93.6% | 99.6% |
|  | 4 | `4b5 2c4 2c3 4b2 (4a1 0c0)` (mirror: `4b5 2c4 2c3 (4b2 4a1 0c0)`) | 93.7% | 99.6% |
|  | 5 | `4b5 2c4 (4b3 4a2 4a1 0c0)` (mirror: `4b5 4a4 4a3 4b2 4a1 (0c0)`) | 93.8% | 99.7% |
|  | 6 | `4b5 4a4 4a3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b5 2c4 2c3 4b2 (2c3 4b2 4a1 0c0)`) | 93.8% | 99.7% |
|  | 7 | `4b5 4a4 4a3 (2c4 2c3 4b2 4a1 0c0)` (mirror: `4b5 2c4 2c3 4b2 2c3 4b2 (4a1 0c0)`) | 93.9% | 99.7% |
|  | 8 | `4b5 2c4 2c3 4b2 2c3 (4b2 4a1 0c0)` (mirror: `4b5 4a4 4b5 2c4 (2c3 4b2 4a1 0c0)`) | 93.9% | 99.7% |
| 4b5 4e | 1 | `4b5 2c4 (2c3 4b2 4a1 0c0)` (mirror: `4b5 2c4 2c3 4b2 4a1 (0c0)`) | 67.0% | 90.5% |
|  | 2 | `4b5 2c4 2c3 (4b2 4a1 0c0)` (mirror: `4b5 2c4 4b3 4a2 (4a1 0c0)`) | 89.6% | 99.1% |
|  | 3 | `4b5 2c4 2c3 4b2 4a1 0c0` | 93.9% | 99.6% |
|  | 4 | `4b5 2c4 2c3 4b2 (4a1 0c0)` (mirror: `4b5 2c4 2c3 (4b2 4a1 0c0)`) | 94.0% | 99.7% |
|  | 5 | `4b5 2c4 (4b3 4a2 4a1 0c0)` (mirror: `4b5 4a4 4a3 4b2 4a1 (0c0)`) | 94.0% | 99.7% |
|  | 6 | `4b5 4a4 (2c5 2c4 2c3 4b2 4a1 0c0)` (mirror: `4b5 2c4 2c3 4b2 4a1 0c0 4a1 (0c0)`) | 94.1% | 99.7% |
|  | 7 | `4b5 4a4 4a3 4b2 (2c3 4b2 4a1 0c0)` (mirror: `4b5 4a4 4b5 2c4 2c3 (4b2 4a1 0c0)`) | 94.1% | 99.7% |
|  | 8 | `4b5 2c4 2c3 4b2 4a1 (0c0)` (mirror: `4b5 2c4 (2c3 4b2 4a1 0c0)`) | 94.2% | 99.7% |

**Edge-path checklists, computer only**: per subset × edges, the budget-2 checklist built over routes read with the bad-edge count at every step (section 4), against the corner-only one. An answer key, not a list to check in an attempt. Sampled, 25,000 per subset × edges. First the corner-only checklist: each row is a subset × edges, each cell the share where the first 1, 2, 3 or 5 corner routes find the optimal:

| Subset | Optimal found, 1 corner route | 2 routes | 3 routes | 5 routes |
|---|---|---|---|---|
| 0c0 0e | 42.5% | 84.4% | 92.6% | 93.0% |
| 0c0 2e | 60.5% | 65.7% | 70.2% | 73.0% |
| 0c0 4e | 44.9% | 57.8% | 61.5% | 65.1% |
| 0c0 6e | 40.8% | 53.7% | 60.2% | 65.7% |
| 0c0 8e | 53.5% | 70.1% | 77.1% | 78.3% |
| 2c5 0e | 77.8% | 86.5% | 89.6% | 91.8% |
| 2c5 2e | 74.8% | 86.2% | 91.0% | 92.9% |
| 2c5 4e | 71.5% | 86.0% | 91.9% | 93.4% |
| 2c5 6e | 73.0% | 84.1% | 90.6% | 92.7% |
| 2c5 8e | 77.6% | 86.0% | 91.0% | 92.5% |
| 2c4 0e | 70.1% | 85.9% | 88.6% | 88.9% |
| 2c4 2e | 67.7% | 86.3% | 89.9% | 90.8% |
| 2c4 4e | 62.0% | 82.0% | 87.6% | 88.4% |
| 2c4 6e | 73.8% | 84.1% | 88.5% | 89.6% |
| 2c4 8e | 77.7% | 89.5% | 91.5% | 92.9% |
| 0c3 0e | 85.5% | 94.2% | 96.6% | 97.2% |
| 0c3 2e | 80.8% | 91.3% | 92.1% | 92.8% |
| 0c3 4e | 67.2% | 85.1% | 85.8% | 86.8% |
| 0c3 6e | 82.6% | 93.9% | 94.6% | 95.2% |
| 0c3 8e | 87.3% | 94.8% | 96.1% | 96.8% |
| 4a2 0e | 29.1% | 40.4% | 44.4% | 50.3% |
| 4a2 2e | 42.2% | 67.8% | 76.8% | 81.4% |
| 4a2 4e | 60.9% | 72.2% | 79.1% | 85.3% |
| 4a1 0e | 33.5% | 46.5% | 54.6% | 66.5% |
| 4a1 2e | 38.8% | 58.8% | 70.5% | 78.2% |
| 4a1 4e | 33.6% | 50.3% | 60.6% | 69.5% |
| 2c3 0e | 46.3% | 67.0% | 75.1% | 85.5% |
| 2c3 2e | 66.5% | 79.6% | 80.2% | 80.8% |
| 2c3 4e | 55.3% | 76.6% | 78.1% | 79.9% |
| 2c3 6e | 66.1% | 73.3% | 76.7% | 79.8% |
| 2c3 8e | 46.3% | 67.2% | 74.5% | 81.3% |
| 0c4 0e | 83.2% | 86.8% | 87.6% | 88.3% |
| 0c4 2e | 86.5% | 88.0% | 89.1% | 90.6% |
| 0c4 4e | 83.5% | 85.1% | 86.1% | 87.8% |
| 0c4 6e | 81.8% | 83.7% | 85.4% | 87.3% |
| 0c4 8e | 80.3% | 86.2% | 87.1% | 88.1% |
| 4c3 0e | 70.8% | 78.4% | 83.3% | 88.6% |
| 4c3 2e | 66.2% | 72.0% | 75.1% | 80.1% |
| 4c3 4e | 62.3% | 70.2% | 74.4% | 79.6% |
| 4c4 0e | 65.2% | 72.4% | 76.7% | 81.9% |
| 4c4 2e | 67.9% | 75.4% | 78.7% | 82.1% |
| 4c4 4e | 68.4% | 74.8% | 78.2% | 81.5% |
| 4b2 0e | 36.5% | 51.1% | 61.0% | 72.4% |
| 4b2 2e | 45.9% | 53.7% | 59.0% | 66.3% |
| 4b2 4e | 30.3% | 53.3% | 66.8% | 76.0% |
| 4b5 0e | 60.8% | 84.2% | 92.6% | 93.0% |
| 4b5 2e | 62.6% | 85.1% | 93.6% | 93.8% |
| 4b5 4e | 67.0% | 89.6% | 93.9% | 94.0% |

The edge-path checklist, same rows: the share after 1, 2, 3 and 5 edge paths, the first edge path, and how many edge paths it takes to find what the first corner-only route finds:

| Subset | Optimal found, 1 edge path | 2 paths | 3 paths | 5 paths | First edge path | Edge paths to match the first corner route |
|---|---|---|---|---|---|---|
| 0c0 0e | 42.5% | 84.4% | 92.6% | 93.0% | `0c0 0e → 4a1 4e → 0c0 0e` | 1 |
| 0c0 2e | 60.5% | 65.3% | 68.8% | 71.2% | `0c0 2e → 4a1 4e → 0c0 0e` | 1 |
| 0c0 4e | 44.9% | 57.8% | 60.8% | 63.5% | `0c0 4e → 4a1 4e → 0c0 0e` | 1 |
| 0c0 6e | 40.8% | 47.2% | 52.0% | 60.2% | `0c0 6e → 4a1 4e → (0c0 0e)` | 1 |
| 0c0 8e | 53.5% | 70.1% | 76.8% | 78.1% | `0c0 8e → 4a1 4e → (0c0 0e)` | 1 |
| 2c5 0e | 63.9% | 71.1% | 76.4% | 83.3% | `2c5 0e → 2c4 4e → 2c3 2e → (4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `2c5 0e → 2c4 4e → 2c3 2e → 4b2 2e → (4a1 4e → 0c0 0e)`) | 4 |
| 2c5 2e | 29.4% | 42.3% | 51.8% | 65.3% | `2c5 2e → 2c4 4e → 2c3 4e → (4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `2c5 2e → 2c4 4e → 2c3 6e → 4b2 4e → (4a1 4e → 0c0 0e)`) | 8 |
| 2c5 4e | 23.9% | 36.4% | 45.3% | 59.8% | `2c5 4e → 2c4 4e → 2c3 2e → (4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `2c5 4e → 2c4 4e → 2c3 8e → 4b2 4e → (4a1 4e → 0c0 0e)`) | 8 |
| 2c5 6e | 23.7% | 36.8% | 45.9% | 60.7% | `2c5 6e → 2c4 4e → 2c3 4e → (4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `2c5 6e → 4b4 2e → 4a3 4e → 4b2 4e → (4a1 4e → 0c0 0e)`) | 8 |
| 2c5 8e | 57.9% | 71.9% | 79.6% | 87.2% | `2c5 8e → 2c4 4e → 2c3 2e → (4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `2c5 8e → 2c4 4e → 2c3 2e → 4b2 2e → (4a1 4e → 0c0 0e)`) | 3 |
| 2c4 0e | 59.8% | 77.8% | 84.4% | 88.4% | `2c4 0e → 2c3 4e → 4b2 2e → 4a1 4e → 0c0 0e` | 2 |
| 2c4 2e | 37.3% | 56.3% | 66.7% | 77.8% | `2c4 2e → 2c3 4e → (4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `2c4 2e → 4b3 4e → 4a2 2e → 4a1 4e → (0c0 0e)`) | 4 |
| 2c4 4e | 30.1% | 49.1% | 64.0% | 77.1% | `2c4 4e → 2c3 4e → (4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `2c4 4e → 4b3 4e → 4a2 2e → 4a1 4e → (0c0 0e)`) | 3 |
| 2c4 6e | 39.3% | 59.4% | 67.4% | 76.9% | `2c4 6e → 2c3 4e → (4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `2c4 6e → 4b3 2e → 4a2 2e → 4a1 4e → (0c0 0e)`) | 5 |
| 2c4 8e | 73.2% | 86.4% | 89.1% | 91.8% | `2c4 8e → 2c3 4e → (4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `2c4 8e → 4b3 4e → 4a2 2e → 4a1 4e → (0c0 0e)`) | 2 |
| 0c3 0e | 85.5% | 92.8% | 94.4% | 96.4% | `0c3 0e → 4a2 4e → (4a1 4e → 0c0 0e)` (mirror: `0c3 0e → 4a2 4e → 4a1 4e → (0c0 0e)`) | 1 |
| 0c3 2e | 80.8% | 86.8% | 90.0% | 91.9% | `0c3 2e → 4a2 4e → (4a1 4e → 0c0 0e)` (mirror: `0c3 2e → 4a2 4e → 4a1 4e → (0c0 0e)`) | 1 |
| 0c3 4e | 67.2% | 77.8% | 81.2% | 84.1% | `0c3 4e → 4a2 4e → (4a1 4e → 0c0 0e)` (mirror: `0c3 4e → 4a2 4e → 4a1 4e → (0c0 0e)`) | 2 |
| 0c3 6e | 82.6% | 89.5% | 92.4% | 94.4% | `0c3 6e → 4a2 4e → (4a1 4e → 0c0 0e)` (mirror: `0c3 6e → 4a2 4e → 4a1 4e → (0c0 0e)`) | 1 |
| 0c3 8e | 87.3% | 92.4% | 94.8% | 96.0% | `0c3 8e → 4a2 4e → (4a1 4e → 0c0 0e)` (mirror: `0c3 8e → 4a2 4e → 4a1 4e → (0c0 0e)`) | 1 |
| 4a2 0e | 27.9% | 38.2% | 42.2% | 48.4% | `4a2 0e → 4b3 4e → 4a2 4e → 4a1 4e → (0c0 0e)` (mirror: `4a2 0e → 4a1 4e → (4b2 2e → 4a1 4e → 0c0 0e)`) | 2 |
| 4a2 2e | 34.0% | 60.0% | 67.3% | 75.3% | `4a2 2e → 4a1 4e → (0c0 0e)` | 2 |
| 4a2 4e | 60.9% | 68.8% | 73.6% | 80.4% | `4a2 4e → 4a1 4e → 0c0 0e` | 1 |
| 4a1 0e | 33.5% | 42.6% | 50.3% | 61.2% | `4a1 0e → 0c0 4e → (4a1 4e → 0c0 0e)` (mirror: `4a1 0e → 0c0 4e → 4a1 4e → (0c0 0e)`) | 1 |
| 4a1 2e | 35.4% | 50.4% | 59.5% | 71.8% | `4a1 2e → 4b2 2e → 4a1 4e → 0c0 0e` | 2 |
| 4a1 4e | 33.6% | 44.4% | 52.5% | 62.3% | `4a1 4e → 0c0 0e` | 1 |
| 2c3 0e | 46.3% | 58.5% | 66.3% | 76.2% | `2c3 0e → 4b2 4e → (4a1 4e → 0c0 0e)` (mirror: `2c3 0e → 4b2 4e → 4a1 4e → (0c0 0e)`) | 1 |
| 2c3 2e | 50.9% | 66.5% | 76.8% | 79.8% | `2c3 2e → 4b2 2e → 4a1 4e → 0c0 0e` | 2 |
| 2c3 4e | 46.2% | 66.8% | 73.2% | 76.9% | `2c3 4e → 4b2 2e → 4a1 4e → 0c0 0e` | 2 |
| 2c3 6e | 55.8% | 66.1% | 70.1% | 74.5% | `2c3 6e → 4b2 2e → (4a1 4e → 0c0 0e)` (mirror: `2c3 6e → 4b2 2e → 4a1 4e → (0c0 0e)`) | 2 |
| 2c3 8e | 46.3% | 57.1% | 63.6% | 71.5% | `2c3 8e → 4b2 4e → (4a1 4e → 0c0 0e)` (mirror: `2c3 8e → 4b2 4e → 4a1 4e → (0c0 0e)`) | 1 |
| 0c4 0e | 75.0% | 83.2% | 86.8% | 87.9% | `0c4 0e → 4a3 4e → 4b2 2e → (4a1 4e → 0c0 0e)` | 2 |
| 0c4 2e | 70.1% | 84.7% | 86.5% | 88.1% | `0c4 2e → 4a3 2e → 4b2 2e → (4a1 4e → 0c0 0e)` (mirror: `0c4 2e → 4a3 2e → 4b2 4e → (4a1 4e → 0c0 0e)`) | 3 |
| 0c4 4e | 60.5% | 80.9% | 82.6% | 84.4% | `0c4 4e → 4a3 4e → 4b2 2e → (4a1 4e → 0c0 0e)` (mirror: `0c4 4e → 4a3 0e → 4b2 4e → (4a1 4e → 0c0 0e)`) | 4 |
| 0c4 6e | 65.0% | 80.0% | 81.8% | 83.7% | `0c4 6e → 4a3 2e → 4b2 2e → (4a1 4e → 0c0 0e)` (mirror: `0c4 6e → 4a3 4e → 4b2 0e → (4a1 4e → 0c0 0e)`) | 3 |
| 0c4 8e | 79.0% | 85.9% | 86.7% | 87.4% | `0c4 8e → 4a3 4e → 4b2 2e → (4a1 4e → 0c0 0e)` | 2 |
| 4c3 0e | 70.8% | 75.9% | 79.8% | 85.2% | `4a3 0e → 4b2 4e → (4a1 4e → 0c0 0e)` (mirror: `4b3 0e → 4a2 4e → 4a1 4e → (0c0 0e)`) | 1 |
| 4c3 2e | 58.4% | 66.2% | 69.3% | 72.6% | `4b3 2e → 4a2 4e → 4a1 4e → (0c0 0e)` (mirror: `4a3 2e → 4b2 2e → (4a1 4e → 0c0 0e)`) | 2 |
| 4c3 4e | 53.1% | 62.2% | 64.5% | 68.5% | `4b3 4e → 4a2 4e → 4a1 4e → (0c0 0e)` (mirror: `4a3 4e → 4b2 2e → (4a1 4e → 0c0 0e)`) | 3 |
| 4c4 0e | 59.3% | 65.2% | 68.3% | 71.8% | `4b4 0e → 4a3 4e → 4b2 2e → (4a1 4e → 0c0 0e)` (mirror: `4a4 0e → 4a3 4e → 4b2 2e → (4a1 4e → 0c0 0e)`) | 2 |
| 4c4 2e | 37.9% | 57.5% | 63.4% | 68.8% | `4b4 2e → 4a3 2e → 4b2 2e → (4a1 4e → 0c0 0e)` (mirror: `4a4 2e → 0c3 2e → 4a2 2e → (4a1 4e → 0c0 0e)`) | 5 |
| 4c4 4e | 31.6% | 56.3% | 61.9% | 68.3% | `4b4 4e → 4a3 4e → 4b2 2e → (4a1 4e → 0c0 0e)` (mirror: `4a4 4e → 4a3 2e → 4b2 4e → (4a1 4e → 0c0 0e)`) | 6 |
| 4b2 0e | 36.5% | 49.7% | 57.8% | 69.5% | `4b2 0e → 4a1 4e → 0c0 0e` | 1 |
| 4b2 2e | 45.9% | 52.0% | 55.1% | 60.3% | `4b2 2e → 4a1 4e → 0c0 0e` | 1 |
| 4b2 4e | 30.3% | 42.6% | 50.8% | 61.1% | `4b2 4e → 4a1 4e → 0c0 0e` | 1 |
| 4b5 0e | 42.3% | 65.1% | 77.7% | 86.1% | `4b5 0e → 2c4 4e → 2c3 2e → (4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `4b5 0e → 2c4 4e → 2c3 4e → 4b2 2e → (4a1 4e → 0c0 0e)`) | 2 |
| 4b5 2e | 26.4% | 42.1% | 51.1% | 63.6% | `4b5 2e → 2c4 4e → (2c3 4e → 4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `4b5 2e → 2c4 4e → 2c3 2e → 4b2 2e → 4a1 4e → (0c0 0e)`) | 5 |
| 4b5 4e | 24.3% | 39.9% | 49.9% | 61.3% | `4b5 4e → 2c4 4e → (2c3 4e → 4b2 2e → 4a1 4e → 0c0 0e)` (mirror: `4b5 4e → 2c4 8e → 4b3 4e → 4a2 2e → 4a1 4e → (0c0 0e)`) | 7 |

**Edge counts along the route**, per starting subset × edges (section 4), one table per intermediate subset. Each row is a starting subset × edges whose optimal (budget 2) can pass the intermediate subset: the share that can pass it at all, then the share that can pass it with each edge count (one DR can pass with several, so they add up to more; shares under 0.5% left out, starting cells under 0.5% not listed; 4a3 and 4b3 together as 4c3).

Through 4b2, one row per starting subset × edges:

| Subset | Can pass 4b2 | via 0e | via 2e | via 4e | via 6e | via 8e |
|---|---|---|---|---|---|---|
| 0c0 2e | 12.9% | – | 10.2% | 5.8% | – | – |
| 0c0 4e | 14.1% | – | 12.2% | 3.6% | – | – |
| 0c0 6e | 32.5% | – | 26.7% | 12.9% | – | – |
| 0c0 8e | 16.1% | – | 13.3% | 4.6% | – | – |
| 2c5 0e | 92.4% | 0.71% | 91.5% | 60.4% | – | – |
| 2c5 2e | 93.6% | 5.4% | 92.0% | 62.8% | – | – |
| 2c5 4e | 94.0% | 4.5% | 92.7% | 58.3% | – | – |
| 2c5 6e | 93.6% | 6.3% | 91.6% | 61.3% | – | – |
| 2c5 8e | 93.1% | 0.68% | 92.9% | 63.3% | – | – |
| 2c4 0e | 89.3% | – | 82.9% | 35.8% | – | – |
| 2c4 2e | 91.9% | 5.3% | 85.0% | 59.5% | – | – |
| 2c4 4e | 89.7% | 3.5% | 84.6% | 45.3% | – | – |
| 2c4 6e | 90.8% | 7.2% | 84.6% | 56.7% | – | – |
| 2c4 8e | 94.2% | 1.5% | 93.0% | 38.2% | – | – |
| 0c3 0e | 23.6% | – | 22.4% | 12.3% | – | – |
| 0c3 2e | 20.4% | – | 19.5% | 5.8% | – | – |
| 0c3 4e | 27.7% | – | 26.9% | 8.6% | – | – |
| 0c3 6e | 20.6% | – | 19.6% | 5.9% | – | – |
| 0c3 8e | 19.8% | – | 18.6% | 8.1% | – | – |
| 4a2 0e | 49.5% | – | 37.8% | 23.7% | – | – |
| 4a2 2e | 60.8% | – | 56.0% | 23.1% | – | – |
| 4a2 4e | 36.0% | – | 31.4% | 11.8% | – | – |
| 4a1 0e | 65.2% | – | 33.3% | 64.5% | – | – |
| 4a1 2e | 66.2% | – | 59.3% | 19.4% | – | – |
| 4a1 4e | 40.1% | 0.87% | 25.4% | 20.9% | – | – |
| 2c3 0e | 89.3% | – | 58.3% | 88.6% | – | – |
| 2c3 2e | 81.4% | – | 69.2% | 46.3% | – | – |
| 2c3 4e | 81.6% | 9.3% | 74.7% | 43.8% | – | – |
| 2c3 6e | 82.2% | – | 74.6% | 61.8% | – | – |
| 2c3 8e | 87.1% | – | 57.3% | 85.7% | – | – |
| 0c4 0e | 88.5% | – | 80.3% | 19.3% | – | – |
| 0c4 2e | 91.2% | 5.7% | 88.9% | 66.1% | – | – |
| 0c4 4e | 88.6% | 1.3% | 85.7% | 50.8% | – | – |
| 0c4 6e | 88.1% | 9.7% | 85.3% | 58.9% | – | – |
| 0c4 8e | 88.3% | – | 86.5% | 12.8% | – | – |
| 4c3 0e | 93.9% | – | 42.3% | 89.6% | – | – |
| 4c3 2e | 84.9% | 0.79% | 74.8% | 39.5% | – | – |
| 4c3 4e | 86.6% | 4.9% | 73.0% | 44.6% | – | – |
| 4c4 0e | 86.2% | 1.9% | 81.3% | 32.4% | – | – |
| 4c4 2e | 89.6% | 5.5% | 86.9% | 51.9% | – | – |
| 4c4 4e | 89.0% | 2.4% | 84.5% | 52.7% | – | – |
| 4b2 0e | 49.3% | 7.7% | 45.7% | 11.6% | – | – |
| 4b2 2e | 29.5% | 1.1% | 27.8% | 10.5% | – | – |
| 4b2 4e | 60.5% | 1.3% | 54.6% | 33.3% | – | – |
| 4b5 0e | 93.0% | 0.55% | 92.4% | 42.1% | – | – |
| 4b5 2e | 94.0% | 4.8% | 91.2% | 54.4% | – | – |
| 4b5 4e | 94.4% | 4.6% | 91.8% | 57.9% | – | – |

Through 2c3, same columns:

| Subset | Can pass 2c3 | via 0e | via 2e | via 4e | via 6e | via 8e |
|---|---|---|---|---|---|---|
| 2c5 0e | 90.7% | – | 83.2% | 47.7% | 31.6% | – |
| 2c5 2e | 92.2% | – | 67.5% | 79.9% | 20.9% | – |
| 2c5 4e | 92.8% | – | 72.2% | 75.9% | 22.2% | – |
| 2c5 6e | 91.8% | – | 72.6% | 76.0% | 20.7% | 0.64% |
| 2c5 8e | 92.0% | – | 89.3% | 36.8% | 32.6% | – |
| 2c4 0e | 89.3% | – | 1.1% | 89.1% | – | – |
| 2c4 2e | 91.9% | – | 60.4% | 68.6% | 24.8% | – |
| 2c4 4e | 89.7% | 1.1% | 55.1% | 66.6% | 23.0% | 1.2% |
| 2c4 6e | 90.8% | – | 60.0% | 66.8% | 27.8% | – |
| 2c4 8e | 94.2% | – | 4.4% | 93.8% | 1.7% | – |
| 0c3 0e | 6.8% | – | 4.9% | 4.8% | – | – |
| 0c3 2e | 3.0% | – | 2.3% | 2.3% | – | – |
| 0c3 4e | 4.7% | – | 3.3% | 3.9% | – | – |
| 0c3 6e | 2.2% | – | 1.6% | 1.7% | – | – |
| 0c3 8e | 4.6% | – | 2.8% | 4.6% | – | – |
| 4a2 0e | 6.9% | – | 4.3% | 5.2% | 0.64% | – |
| 4a2 2e | 7.3% | – | 5.0% | 5.6% | 0.70% | – |
| 4a2 4e | 2.0% | – | 1.2% | 1.6% | – | – |
| 4a1 0e | 31.5% | – | 27.6% | 14.6% | 8.4% | – |
| 4a1 2e | 6.4% | – | 3.0% | 5.2% | 0.95% | – |
| 4a1 4e | 2.2% | – | 1.4% | 1.5% | – | – |
| 2c3 0e | 59.6% | 2.1% | 48.4% | 36.9% | 12.6% | – |
| 2c3 2e | 6.1% | – | 4.6% | 2.8% | – | – |
| 2c3 4e | 13.5% | – | 6.1% | 10.6% | 1.5% | – |
| 2c3 6e | 21.6% | – | 11.7% | 14.2% | 6.6% | – |
| 2c3 8e | 59.0% | – | 47.3% | 39.5% | 13.8% | 2.6% |
| 0c4 0e | 4.7% | – | 3.3% | 2.7% | – | – |
| 0c4 2e | 9.3% | – | 6.5% | 7.0% | 0.56% | – |
| 0c4 4e | 8.7% | – | 5.6% | 6.6% | 1.0% | – |
| 0c4 6e | 12.1% | – | 6.9% | 10.4% | 2.2% | – |
| 0c4 8e | 8.1% | – | 2.8% | 7.0% | 2.1% | – |
| 4c3 0e | 40.8% | – | 37.5% | 16.6% | 10.2% | – |
| 4c3 2e | 29.8% | – | 17.3% | 22.7% | 3.4% | – |
| 4c3 4e | 35.8% | – | 23.0% | 25.9% | 5.3% | – |
| 4c4 0e | 36.3% | – | 27.2% | 26.2% | 5.6% | – |
| 4c4 2e | 39.3% | – | 28.9% | 32.2% | 4.8% | – |
| 4c4 4e | 35.9% | – | 26.7% | 28.0% | 4.7% | – |
| 4b2 0e | 44.0% | – | – | 43.9% | – | – |
| 4b2 2e | 26.4% | – | 11.9% | 17.6% | 7.7% | – |
| 4b2 4e | 55.5% | 0.64% | 28.8% | 40.8% | 13.1% | 0.72% |
| 4b5 0e | 93.0% | – | 81.2% | 53.9% | 25.2% | – |
| 4b5 2e | 93.9% | 0.57% | 69.5% | 77.7% | 19.0% | – |
| 4b5 4e | 94.3% | – | 72.8% | 75.0% | 22.6% | – |

Through 4a1, same columns:

| Subset | Can pass 4a1 | via 0e | via 2e | via 4e | via 6e | via 8e |
|---|---|---|---|---|---|---|
| 0c0 0e | 43.0% | – | – | 43.0% | – | – |
| 0c0 2e | 74.6% | – | 9.8% | 74.6% | – | – |
| 0c0 4e | 68.5% | 0.61% | 12.2% | 68.5% | – | – |
| 0c0 6e | 68.1% | – | 30.4% | 68.1% | – | – |
| 0c0 8e | 78.9% | – | – | 78.9% | – | – |
| 2c5 0e | 92.4% | – | – | 92.4% | – | – |
| 2c5 2e | 93.6% | – | – | 93.6% | – | – |
| 2c5 4e | 94.0% | – | – | 94.0% | – | – |
| 2c5 6e | 93.6% | – | – | 93.6% | – | – |
| 2c5 8e | 93.1% | – | – | 93.1% | – | – |
| 2c4 0e | 89.3% | – | – | 89.3% | – | – |
| 2c4 2e | 92.0% | – | – | 92.0% | – | – |
| 2c4 4e | 89.9% | – | – | 89.9% | – | – |
| 2c4 6e | 91.1% | – | – | 91.1% | – | – |
| 2c4 8e | 94.2% | – | – | 94.2% | – | – |
| 0c3 0e | 97.4% | – | 6.0% | 97.4% | – | – |
| 0c3 2e | 93.5% | – | 10.0% | 93.5% | – | – |
| 0c3 4e | 88.0% | – | 14.4% | 88.0% | – | – |
| 0c3 6e | 95.6% | – | 11.2% | 95.6% | – | – |
| 0c3 8e | 97.3% | – | 5.5% | 97.3% | – | – |
| 4a2 0e | 54.1% | – | – | 54.1% | – | – |
| 4a2 2e | 84.7% | – | 39.8% | 84.7% | – | – |
| 4a2 4e | 86.9% | 1.2% | 21.4% | 86.9% | – | – |
| 4a1 0e | 73.8% | 5.3% | 7.0% | 73.8% | – | – |
| 4a1 2e | 80.5% | – | 3.9% | 80.5% | – | – |
| 4a1 4e | 46.9% | – | – | 46.9% | – | – |
| 2c3 0e | 89.3% | – | 32.2% | 89.3% | – | – |
| 2c3 2e | 81.4% | – | – | 81.4% | – | – |
| 2c3 4e | 81.6% | – | 1.7% | 81.6% | – | – |
| 2c3 6e | 82.2% | – | 2.9% | 82.2% | – | – |
| 2c3 8e | 87.1% | – | 18.1% | 87.1% | – | – |
| 0c4 0e | 88.5% | – | – | 88.5% | – | – |
| 0c4 2e | 91.2% | – | 0.59% | 91.2% | – | – |
| 0c4 4e | 88.6% | – | – | 88.6% | – | – |
| 0c4 6e | 88.1% | – | 0.56% | 88.1% | – | – |
| 0c4 8e | 88.3% | – | 0.82% | 88.3% | – | – |
| 4c3 0e | 95.1% | – | 8.9% | 95.1% | – | – |
| 4c3 2e | 87.0% | – | 4.1% | 87.0% | – | – |
| 4c3 4e | 87.8% | – | 5.9% | 87.8% | – | – |
| 4c4 0e | 86.6% | – | 1.3% | 86.6% | – | – |
| 4c4 2e | 90.0% | – | 0.89% | 90.0% | – | – |
| 4c4 4e | 89.3% | – | 0.92% | 89.3% | – | – |
| 4b2 0e | 79.1% | – | – | 79.1% | – | – |
| 4b2 2e | 69.5% | – | 4.4% | 69.5% | – | – |
| 4b2 4e | 82.6% | 0.78% | 14.5% | 82.6% | – | – |
| 4b5 0e | 93.4% | – | – | 93.4% | – | – |
| 4b5 2e | 94.0% | – | – | 94.0% | – | – |
| 4b5 4e | 94.4% | – | – | 94.4% | – | – |

Through 4a2, same columns:

| Subset | Can pass 4a2 | via 0e | via 2e | via 4e | via 6e | via 8e |
|---|---|---|---|---|---|---|
| 0c0 6e | 0.62% | – | – | 0.60% | – | – |
| 2c5 0e | 15.1% | – | – | 15.1% | – | – |
| 2c5 2e | 16.4% | – | – | 16.4% | – | – |
| 2c5 4e | 15.0% | – | – | 15.0% | – | – |
| 2c5 6e | 17.5% | – | – | 17.4% | – | – |
| 2c5 8e | 14.2% | – | – | 14.2% | – | – |
| 2c4 0e | 11.7% | – | 3.6% | 9.1% | – | – |
| 2c4 2e | 36.2% | – | 3.1% | 34.7% | – | – |
| 2c4 4e | 36.5% | – | 4.6% | 34.3% | – | – |
| 2c4 6e | 45.6% | – | 4.3% | 43.7% | – | – |
| 2c4 8e | 37.1% | – | 12.0% | 29.8% | – | – |
| 0c3 0e | 95.9% | – | – | 95.9% | – | – |
| 0c3 2e | 93.0% | – | 36.8% | 92.5% | – | – |
| 0c3 4e | 87.4% | 3.2% | 46.1% | 86.1% | – | – |
| 0c3 6e | 95.4% | – | 37.7% | 95.1% | – | – |
| 0c3 8e | 96.4% | – | – | 96.4% | – | – |
| 4a2 0e | 30.5% | – | 1.5% | 29.1% | – | – |
| 4a2 2e | 44.0% | – | 8.1% | 39.1% | – | – |
| 4a2 4e | 22.9% | – | 0.97% | 22.6% | – | – |
| 4a1 0e | 3.1% | – | – | 3.1% | – | – |
| 4a1 2e | 9.0% | – | 2.6% | 6.5% | – | – |
| 4a1 4e | 5.0% | – | 0.67% | 4.4% | – | – |
| 2c3 0e | 13.0% | – | – | 12.9% | – | – |
| 2c3 4e | 1.3% | – | – | 1.2% | – | – |
| 2c3 6e | 3.1% | – | – | 3.0% | – | – |
| 2c3 8e | 15.1% | – | – | 14.9% | – | – |
| 0c4 0e | 22.9% | – | – | 22.9% | – | – |
| 0c4 2e | 35.4% | – | – | 35.3% | – | – |
| 0c4 4e | 27.4% | – | – | 27.2% | – | – |
| 0c4 6e | 35.4% | – | 0.54% | 35.2% | – | – |
| 0c4 8e | 37.4% | – | – | 37.2% | – | – |
| 4c3 0e | 80.1% | – | – | 80.1% | – | – |
| 4c3 2e | 73.8% | – | 17.1% | 65.5% | – | – |
| 4c3 4e | 70.9% | – | 16.7% | 60.7% | – | – |
| 4c4 0e | 28.6% | – | 4.8% | 28.3% | – | – |
| 4c4 2e | 46.9% | – | 2.4% | 46.7% | – | – |
| 4c4 4e | 42.9% | – | 2.6% | 42.8% | – | – |
| 4b2 0e | 1.7% | – | – | 1.7% | – | – |
| 4b2 2e | 0.66% | – | – | 0.61% | – | – |
| 4b2 4e | 2.1% | – | – | 2.1% | – | – |
| 4b5 0e | 44.2% | – | 2.4% | 43.2% | – | – |
| 4b5 2e | 45.2% | – | 2.3% | 44.6% | – | – |
| 4b5 4e | 51.8% | – | 2.8% | 51.2% | – | – |

Through 4c3 (4a3 or 4b3), same columns:

| Subset | Can pass 4c3 (4a3 or 4b3) | via 0e | via 2e | via 4e | via 6e | via 8e |
|---|---|---|---|---|---|---|
| 2c5 0e | 53.9% | 0.57% | 46.6% | 26.1% | – | – |
| 2c5 2e | 48.5% | 5.7% | 31.4% | 37.3% | – | – |
| 2c5 4e | 45.2% | 1.7% | 32.3% | 31.8% | – | – |
| 2c5 6e | 47.8% | 6.5% | 31.6% | 34.7% | – | – |
| 2c5 8e | 48.3% | – | 40.6% | 24.4% | – | – |
| 2c4 0e | 12.8% | – | – | 12.7% | – | – |
| 2c4 2e | 37.8% | – | 20.5% | 23.4% | – | – |
| 2c4 4e | 38.4% | 2.8% | 20.9% | 18.8% | – | – |
| 2c4 6e | 47.2% | – | 26.8% | 29.0% | – | – |
| 2c4 8e | 40.0% | – | 1.8% | 39.2% | – | – |
| 0c3 0e | 21.4% | – | 15.3% | 18.1% | – | – |
| 0c3 2e | 19.4% | 0.60% | 13.9% | 15.6% | – | – |
| 0c3 4e | 26.7% | 0.80% | 21.2% | 19.9% | – | – |
| 0c3 6e | 20.1% | 0.60% | 14.3% | 15.9% | – | – |
| 0c3 8e | 18.5% | – | 11.8% | 15.7% | – | – |
| 4a2 0e | 33.7% | – | – | 33.7% | – | – |
| 4a2 2e | 46.3% | – | 35.5% | 26.1% | – | – |
| 4a2 4e | 23.3% | 1.3% | 10.8% | 16.8% | – | – |
| 2c3 0e | 17.1% | – | 13.4% | 6.1% | – | – |
| 2c3 2e | 0.68% | – | – | – | – | – |
| 2c3 4e | 2.1% | – | 1.2% | 0.96% | – | – |
| 2c3 6e | 4.6% | – | 2.0% | 2.7% | – | – |
| 2c3 8e | 18.0% | – | 13.3% | 7.0% | – | – |
| 0c4 0e | 88.5% | – | – | 88.5% | – | – |
| 0c4 2e | 91.2% | – | 80.9% | 71.7% | – | – |
| 0c4 4e | 88.6% | 17.8% | 70.2% | 70.9% | – | – |
| 0c4 6e | 88.1% | – | 76.7% | 76.8% | – | – |
| 0c4 8e | 88.3% | – | – | 88.3% | – | – |
| 4c3 0e | 12.8% | 2.7% | 7.4% | 5.3% | – | – |
| 4c3 2e | 12.0% | 0.53% | 8.2% | 5.4% | – | – |
| 4c3 4e | 13.5% | – | 6.9% | 9.2% | – | – |
| 4c4 0e | 79.7% | – | 9.5% | 77.7% | – | – |
| 4c4 2e | 83.4% | – | 67.1% | 64.5% | – | – |
| 4c4 4e | 82.8% | 12.8% | 57.3% | 62.5% | – | – |
| 4b2 0e | 7.8% | – | – | 7.8% | – | – |
| 4b2 2e | 2.9% | – | 1.9% | 1.9% | – | – |
| 4b2 4e | 5.5% | – | 3.9% | 3.1% | – | – |
| 4b5 0e | 62.2% | – | 57.0% | 15.2% | – | – |
| 4b5 2e | 59.8% | 6.1% | 37.1% | 40.8% | – | – |
| 4b5 4e | 65.4% | 2.0% | 42.6% | 44.8% | – | – |

**Checklists with no HTR limit**, first four routes, one row per route with the cumulative share finding the optimal. With no limit the routes overlap so much that these lists tell you more about which readings exist than about what to try:

| Subset | # | Class | Optimal, cumulative |
|---|---|---|---|
| 0c0 0e | 1 | `0c0 4a1 0c0` | 49.4% |
|  | 2 | `0c0` | 91.2% |
|  | 3 | `0c0 \| qt` | 99.5% |
|  | 4 | `0c0 4a1 (0c0 4a1 0c0)` | 99.8% |
| 0c0 2e | 1 | `0c0 4a1 0c0` | 70.1% |
|  | 2 | `0c0 4a1 0c0 4a1 0c0` | 93.2% |
|  | 3 | `0c0 4a1 4b2 4a1 0c0` | 99.5% |
|  | 4 | `0c0 4a1 (4b2 2c3 4b2 4a1 0c0)` | 99.9% |
| 0c0 4e | 1 | `0c0 4a1 0c0` | 60.5% |
|  | 2 | `0c0 4a1 (0c0 4a1 0c0)` | 87.4% |
|  | 3 | `0c0 4a1 0c0 4a1 0c0` | 98.2% |
|  | 4 | `0c0 4a1 4b2 2c3 4b2 4a1 0c0` | 99.8% |
| 0c0 6e | 1 | `0c0 4a1 0c0 4a1 0c0` | 54.3% |
|  | 2 | `0c0 4a1 0c0` | 80.2% |
|  | 3 | `0c0 4a1 (0c0 4a1 0c0)` | 96.5% |
|  | 4 | `0c0 4a1 (4b2 2c3 4b2 4a1 0c0)` | 99.6% |
| 0c0 8e | 1 | `0c0 4a1 0c0` | 77.9% |
|  | 2 | `0c0 4a1 0c0 4a1 0c0` | 93.8% |
|  | 3 | `0c0 4a1 (0c0 4a1 0c0)` | 98.9% |
|  | 4 | `0c0 4a1 (4b2 2c3 4b2 4a1 0c0)` | >99.9% |
| 2c5 0e | 1 | `2c5 2c4 2c3 4b2 4a1 0c0` | 93.6% |
|  | 2 | `2c5 4b4 (4b5 2c4 2c3 4b2 4a1 0c0)` | 97.1% |
|  | 3 | `2c5 2c4 2c3 (4b2 2c3 4b2 4a1 0c0)` | 98.4% |
|  | 4 | `2c5 4b4 4a3 4b2 4a1 0c0` | 99.7% |
| 2c5 2e | 1 | `2c5 2c4 2c3 4b2 4a1 0c0` | 94.9% |
|  | 2 | `2c5 4b4 (4b5 2c4 2c3 4b2 4a1 0c0)` | 97.7% |
|  | 3 | `2c5 2c4 2c3 (4b2 2c3 4b2 4a1 0c0)` | 98.7% |
|  | 4 | `2c5 4b4 4a3 4b2 4a1 0c0` | 99.7% |
| 2c5 4e | 1 | `2c5 2c4 2c3 4b2 4a1 0c0` | 95.7% |
|  | 2 | `2c5 4b4 (4b5 2c4 2c3 4b2 4a1 0c0)` | 98.0% |
|  | 3 | `2c5 4b4 4a3 4b2 4a1 0c0` | 98.9% |
|  | 4 | `2c5 2c4 2c3 (4b2 2c3 4b2 4a1 0c0)` | 99.8% |
| 2c5 6e | 1 | `2c5 2c4 2c3 4b2 4a1 0c0` | 94.8% |
|  | 2 | `2c5 4b4 (4b5 2c4 2c3 4b2 4a1 0c0)` | 97.3% |
|  | 3 | `2c5 4b4 4a3 4b2 4a1 0c0` | 98.6% |
|  | 4 | `2c5 2c4 2c3 (4b2 2c3 4b2 4a1 0c0)` | 99.5% |
| 2c5 8e | 1 | `2c5 2c4 2c3 4b2 4a1 0c0` | 95.2% |
|  | 2 | `2c5 4b4 (4b5 2c4 2c3 4b2 4a1 0c0)` | 97.9% |
|  | 3 | `2c5 2c4 2c3 4b2 (2c3 4b2 4a1 0c0)` | 99.0% |
|  | 4 | `2c5 4b4 4a3 4b2 4a1 0c0` | 99.8% |
| 2c4 0e | 1 | `2c4 2c3 4b2 4a1 0c0` | 96.2% |
|  | 2 | `2c4 2c3 4b2 (2c3 4b2 4a1 0c0)` | 98.0% |
|  | 3 | `2c4 4b5 2c4 2c3 4b2 4a1 0c0` | 98.8% |
|  | 4 | `2c4 2c3 2c4 2c3 4b2 4a1 0c0` | 99.6% |
| 2c4 2e | 1 | `2c4 2c3 4b2 4a1 0c0` | 94.9% |
|  | 2 | `2c4 2c3 4b2 (2c3 4b2 4a1 0c0)` | 97.8% |
|  | 3 | `2c4 4b5 2c4 2c3 4b2 4a1 0c0` | 98.9% |
|  | 4 | `2c4 2c3 2c4 (2c3 4b2 4a1 0c0)` | 99.5% |
| 2c4 4e | 1 | `2c4 2c3 4b2 4a1 0c0` | 93.8% |
|  | 2 | `2c4 2c3 4b2 (2c3 4b2 4a1 0c0)` | 97.6% |
|  | 3 | `2c4 4b5 2c4 2c3 4b2 4a1 0c0` | 98.9% |
|  | 4 | `2c4 2c3 2c4 2c3 4b2 4a1 0c0` | 99.6% |
| 2c4 6e | 1 | `2c4 2c3 4b2 4a1 0c0` | 94.3% |
|  | 2 | `2c4 2c3 4b2 (2c3 4b2 4a1 0c0)` | 97.7% |
|  | 3 | `2c4 4b5 2c4 2c3 4b2 4a1 0c0` | 99.0% |
|  | 4 | `2c4 2c3 2c4 (2c3 4b2 4a1 0c0)` | 99.6% |
| 2c4 8e | 1 | `2c4 2c3 4b2 4a1 0c0` | 95.2% |
|  | 2 | `2c4 2c3 4b2 (2c3 4b2 4a1 0c0)` | 97.4% |
|  | 3 | `2c4 4b5 2c4 2c3 4b2 4a1 0c0` | 98.9% |
|  | 4 | `2c4 2c3 2c4 (2c3 4b2 4a1 0c0)` | 99.4% |
| 0c3 0e | 1 | `0c3 4a2 4a1 0c0` | 85.6% |
|  | 2 | `0c3 4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` | 94.5% |
|  | 3 | `0c3 4a2 4b3 4a2 4a1 0c0` | 99.9% |
|  | 4 | `0c3 4a2 4b3 2c4 2c3 4b2 4a1 0c0` | >99.9% |
| 0c3 2e | 1 | `0c3 4a2 4a1 0c0` | 83.1% |
|  | 2 | `0c3 4a2 4b3 4a2 4a1 0c0` | 94.2% |
|  | 3 | `0c3 4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` | 99.5% |
|  | 4 | `0c3 4a2 4b3 2c4 2c3 4b2 4a1 0c0` | 99.8% |
| 0c3 4e | 1 | `0c3 4a2 4a1 0c0` | 68.4% |
|  | 2 | `0c3 4a2 4b3 4a2 4a1 0c0` | 91.9% |
|  | 3 | `0c3 4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` | 99.2% |
|  | 4 | `0c3 4a2 4b3 (4b2 2c3 4b2 4a1 0c0)` | 99.7% |
| 0c3 6e | 1 | `0c3 4a2 4a1 0c0` | 84.9% |
|  | 2 | `0c3 4a2 4b3 4a2 4a1 0c0` | 96.9% |
|  | 3 | `0c3 4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` | 99.6% |
|  | 4 | `0c3 4a2 4a1 0c0 4a1 0c0` | 99.9% |
| 0c3 8e | 1 | `0c3 4a2 4a1 0c0` | 87.3% |
|  | 2 | `0c3 4a2 4b3 4a2 4a1 0c0` | 95.4% |
|  | 3 | `0c3 4a4 4b5 (2c4 2c3 4b2 4a1 0c0)` | 99.8% |
|  | 4 | `0c3 4a2 4b3 2c4 2c3 4b2 4a1 0c0` | >99.9% |
| 4a2 0e | 1 | `4a2 4a1 4b2 4a1 0c0` | 56.9% |
|  | 2 | `4a2 4b3 4a2 4a1 0c0` | 84.0% |
|  | 3 | `4a2 4b3 2c4 2c3 4b2 4a1 0c0` | 98.6% |
|  | 4 | `4a2 0c3 4a2 4a1 0c0` | 99.2% |
| 4a2 2e | 1 | `4a2 4b3 4a2 4a1 0c0` | 52.4% |
|  | 2 | `4a2 4a1 (0c0 4a1 0c0)` | 74.1% |
|  | 3 | `4a2 4a1 0c0` | 91.3% |
|  | 4 | `4a2 4b3 2c4 2c3 4b2 4a1 0c0` | 99.3% |
| 4a2 4e | 1 | `4a2 4a1 0c0` | 67.8% |
|  | 2 | `4a2 4a1 (0c0 4a1 0c0)` | 88.0% |
|  | 3 | `4a2 4b3 4a2 4a1 0c0` | 96.2% |
|  | 4 | `4a2 4b3 2c4 2c3 4b2 4a1 0c0` | 99.8% |
| 4a1 0e | 1 | `4a1 4b2 2c3 4b2 4a1 0c0` | 67.1% |
|  | 2 | `4a1 0c0 4a1 0c0` | 94.7% |
|  | 3 | `4a1 0c0 4a1 0c0 4a1 0c0` | 98.8% |
|  | 4 | `4a1 4b2 4a1 0c0 4a1 0c0` | 99.8% |
| 4a1 2e | 1 | `4a1 0c0 4a1 0c0` | 86.5% |
|  | 2 | `4a1 4b2 2c3 4b2 4a1 0c0` | 96.6% |
|  | 3 | `4a1 0c0 (4a1 0c0 4a1 0c0)` | 98.7% |
|  | 4 | `4a1 4b2 4a1 0c0 4a1 0c0` | >99.9% |
| 4a1 4e | 1 | `4a1 0c0 4a1 0c0` | 74.0% |
|  | 2 | `4a1 0c0` | 89.8% |
|  | 3 | `4a1 4b2 2c3 4b2 4a1 0c0` | 97.7% |
|  | 4 | `4a1 0c0 (4a1 0c0 4a1 0c0)` | 99.2% |
| 2c3 0e | 1 | `2c3 4b2 (2c3 4b2 4a1 0c0)` | 72.6% |
|  | 2 | `2c3 4b2 4a1 0c0` | 93.2% |
|  | 3 | `2c3 4b2 (4a1 0c0 4a1 0c0)` | 98.8% |
|  | 4 | `2c3 2c4 2c3 4b2 4a1 0c0` | 99.7% |
| 2c3 2e | 1 | `2c3 4b2 4a1 0c0` | 89.8% |
|  | 2 | `2c3 4b2 2c3 4b2 4a1 0c0` | 98.1% |
|  | 3 | `2c3 2c4 2c3 4b2 4a1 0c0` | 99.9% |
|  | 4 | `2c3 4b2 4a1 4b2 4a1 0c0` | >99.9% |
| 2c3 4e | 1 | `2c3 4b2 4a1 0c0` | 83.2% |
|  | 2 | `2c3 4b2 (2c3 4b2 4a1 0c0)` | 97.2% |
|  | 3 | `2c3 4b2 (4a1 0c0 4a1 0c0)` | 99.5% |
|  | 4 | `2c3 2c4 2c3 4b2 4a1 0c0` | >99.9% |
| 2c3 6e | 1 | `2c3 4b2 4a1 0c0` | 78.1% |
|  | 2 | `2c3 4b2 2c3 4b2 4a1 0c0` | 96.7% |
|  | 3 | `2c3 2c4 2c3 4b2 4a1 0c0` | 99.7% |
|  | 4 | `2c3 4b2 4a1 4b2 4a1 0c0` | 99.9% |
| 2c3 8e | 1 | `2c3 4b2 (2c3 4b2 4a1 0c0)` | 75.9% |
|  | 2 | `2c3 4b2 4a1 0c0` | 95.5% |
|  | 3 | `2c3 4b2 (4a1 0c0 4a1 0c0)` | 99.1% |
|  | 4 | `2c3 2c4 2c3 4b2 4a1 0c0` | 99.7% |
| 0c4 0e | 1 | `0c4 4a3 4b2 4a1 0c0` | 94.4% |
|  | 2 | `0c4 4a3 4b2 2c3 4b2 4a1 0c0` | >99.9% |
| 0c4 2e | 1 | `0c4 4a3 4b2 4a1 0c0` | 92.0% |
|  | 2 | `0c4 4a3 4b2 2c3 4b2 4a1 0c0` | >99.9% |
|  | 3 | `0c4 4a3 4b2 4a1 4b2 4a1 0c0` | >99.9% |
|  | 4 | `0c4 4a3 0c4 4a3 4b2 4a1 0c0` | >99.9% |
| 0c4 4e | 1 | `0c4 4a3 4b2 4a1 0c0` | 90.1% |
|  | 2 | `0c4 4a3 4b2 2c3 4b2 4a1 0c0` | 99.9% |
|  | 3 | `0c4 4a3 0c4 4a3 4b2 4a1 0c0` | >99.9% |
|  | 4 | `0c4 4a3 4b2 4a1 4b2 4a1 0c0` | >99.9% |
| 0c4 6e | 1 | `0c4 4a3 4b2 4a1 0c0` | 87.1% |
|  | 2 | `0c4 4a3 4b2 2c3 4b2 4a1 0c0` | 99.8% |
|  | 3 | `0c4 4a3 0c4 4a3 4b2 4a1 0c0` | >99.9% |
|  | 4 | `0c4 4a3 4b2 4a1 4b2 4a1 0c0` | >99.9% |
| 0c4 8e | 1 | `0c4 4a3 4b2 4a1 0c0` | 93.1% |
|  | 2 | `0c4 4a3 4b2 2c3 4b2 4a1 0c0` | 99.9% |
|  | 3 | `0c4 4a3 0c4 4a3 4b2 4a1 0c0` | >99.9% |
| 4c3 0e | 1 | `4a3 4b2 4a1 0c0` | 76.5% |
|  | 2 | `4a3 4b2 2c3 4b2 4a1 0c0` | 97.5% |
|  | 3 | `4a3 0c4 4a3 4b2 4a1 0c0` | 99.4% |
|  | 4 | `4b3 4a2 (4b3 4a2 4a1 0c0)` | 99.6% |
| 4c3 2e | 1 | `4a3 4b2 4a1 0c0` | 74.6% |
|  | 2 | `4a3 4b2 2c3 4b2 4a1 0c0` | 96.8% |
|  | 3 | `4a3 0c4 4a3 4b2 4a1 0c0` | 99.1% |
|  | 4 | `4b3 4a2 (4b3 4a2 4a1 0c0)` | 99.4% |
| 4c3 4e | 1 | `4a3 4b2 4a1 0c0` | 70.7% |
|  | 2 | `4a3 4b2 2c3 4b2 4a1 0c0` | 96.4% |
|  | 3 | `4a3 0c4 4a3 4b2 4a1 0c0` | 98.8% |
|  | 4 | `4b3 4a2 (4b3 4a2 4a1 0c0)` | 99.3% |
| 4c4 0e | 1 | `4b4 4a3 4b2 4a1 0c0` | 67.7% |
|  | 2 | `4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` | 93.2% |
|  | 3 | `4b4 2c5 2c4 2c3 4b2 4a1 0c0` | 99.2% |
|  | 4 | `4b4 4a3 4b2 2c3 4b2 4a1 0c0` | 99.7% |
| 4c4 2e | 1 | `4b4 4a3 4b2 4a1 0c0` | 72.1% |
|  | 2 | `4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` | 94.3% |
|  | 3 | `4b4 2c5 2c4 2c3 4b2 4a1 0c0` | 99.2% |
|  | 4 | `4b4 4a3 4b2 2c3 4b2 4a1 0c0` | 99.9% |
| 4c4 4e | 1 | `4b4 4a3 4b2 4a1 0c0` | 73.8% |
|  | 2 | `4a4 4b5 2c4 (2c3 4b2 4a1 0c0)` | 94.0% |
|  | 3 | `4b4 2c5 2c4 2c3 4b2 4a1 0c0` | 99.2% |
|  | 4 | `4b4 4a3 4b2 2c3 4b2 4a1 0c0` | 99.9% |
| 4b2 0e | 1 | `4b2 2c3 4b2 4a1 0c0` | 68.2% |
|  | 2 | `4b2 4a1 0c0` | 91.6% |
|  | 3 | `4b2 4a3 4b2 4a1 0c0` | 95.7% |
|  | 4 | `4b2 4a1 4b2 4a1 0c0` | 97.7% |
| 4b2 2e | 1 | `4b2 2c3 4b2 4a1 0c0` | 68.8% |
|  | 2 | `4b2 4a1 0c0` | 94.4% |
|  | 3 | `4b2 4a1 4b2 4a1 0c0` | 97.7% |
|  | 4 | `4b2 4a3 4b2 4a1 0c0` | 98.9% |
| 4b2 4e | 1 | `4b2 2c3 4b2 4a1 0c0` | 77.8% |
|  | 2 | `4b2 4a1 0c0` | 93.1% |
|  | 3 | `4b2 4a1 4b2 4a1 0c0` | 97.0% |
|  | 4 | `4b2 4a3 4b2 4a1 0c0` | 98.5% |
| 4b5 0e | 1 | `4b5 2c4 2c3 4b2 4a1 0c0` | 98.1% |
|  | 2 | `4b5 2c4 2c3 4b2 (2c3 4b2 4a1 0c0)` | 98.9% |
|  | 3 | `4b5 4a4 (2c5 2c4 2c3 4b2 4a1 0c0)` | 99.4% |
|  | 4 | `4b5 2c4 4b3 (4b2 2c3 4b2 4a1 0c0)` | 99.8% |
| 4b5 2e | 1 | `4b5 2c4 2c3 4b2 4a1 0c0` | 98.0% |
|  | 2 | `4b5 4a4 (2c5 2c4 2c3 4b2 4a1 0c0)` | 98.8% |
|  | 3 | `4b5 2c4 2c3 (4b2 2c3 4b2 4a1 0c0)` | 99.4% |
|  | 4 | `4b5 2c4 (2c3 4b2 2c3 4b2 4a1 0c0)` | 99.8% |
| 4b5 4e | 1 | `4b5 2c4 2c3 4b2 4a1 0c0` | 98.1% |
|  | 2 | `4b5 4a4 (2c5 2c4 2c3 4b2 4a1 0c0)` | 98.9% |
|  | 3 | `4b5 2c4 2c3 (4b2 2c3 4b2 4a1 0c0)` | 99.5% |
|  | 4 | `4b5 2c4 (2c3 4b2 2c3 4b2 4a1 0c0)` | 99.7% |

**rodneykinney's table** for FakeMMAP's bound: per subset × edges and target M, "reduce to 1q in at most R moves" with nothing read off the DR (A, B and C the subset's shortest linear HTR, worst case over the subset's corner paths). Each row is a subset × edges and a target M; the three columns are reduction lengths in moves: the formula of FakeMMAP's message without its first term, the exact model of section 9 (*computer only*), and the longest reduction any sampled finish of at most M needed. Sampled, 25,000 per subset × edges; a blank row means no sampled finish reaches that M.

| Subset | Target M | R from the formula without term 1 | R from the exact model | Longest reduction needed |
|---|---|---|---|---|
| 0c0 0e | 10 | 11 | 8 | 7 |
| 0c0 0e | 11 | 12 | 9 | 8 |
| 0c0 0e | 12 | 13 | 10 | 8 |
| 0c0 2e | 10 | 9 | 7 | 6 |
| 0c0 2e | 11 | 10 | 8 | 8 |
| 0c0 2e | 12 | 11 | 10 | 9 |
| 0c0 4e | 10 | 9 | 8 | 6 |
| 0c0 4e | 11 | 10 | 8 | 8 |
| 0c0 4e | 12 | 11 | 9 | 9 |
| 0c0 6e | 10 | 7 | 6 | 6 |
| 0c0 6e | 11 | 9 | 8 | 8 |
| 0c0 6e | 12 | 10 | 9 | 9 |
| 0c0 8e | 10 | 9 | 7 | 6 |
| 0c0 8e | 11 | 10 | 8 | 6 |
| 0c0 8e | 12 | 11 | 9 | 7 |
| 2c5 0e | 10 |  |  |  |
| 2c5 0e | 11 | 8 | 7 | 7 |
| 2c5 0e | 12 | 10 | 9 | 8 |
| 2c5 2e | 10 | 7 | 7 | 7 |
| 2c5 2e | 11 | 8 | 8 | 8 |
| 2c5 2e | 12 | 10 | 9 | 8 |
| 2c5 4e | 10 | 7 | 7 | 7 |
| 2c5 4e | 11 | 8 | 8 | 8 |
| 2c5 4e | 12 | 10 | 9 | 8 |
| 2c5 6e | 10 | 7 | 7 | 6 |
| 2c5 6e | 11 | 8 | 8 | 7 |
| 2c5 6e | 12 | 10 | 9 | 8 |
| 2c5 8e | 10 |  |  |  |
| 2c5 8e | 11 | 8 | 7 | 7 |
| 2c5 8e | 12 | 10 | 9 | 8 |
| 2c4 0e | 10 | 8 | 7 | 6 |
| 2c4 0e | 11 | 9 | 8 | 8 |
| 2c4 0e | 12 | 10 | 9 | 9 |
| 2c4 2e | 10 | 7 | 6 | 6 |
| 2c4 2e | 11 | 9 | 8 | 8 |
| 2c4 2e | 12 | 10 | 9 | 9 |
| 2c4 4e | 10 | 7 | 6 | 6 |
| 2c4 4e | 11 | 9 | 8 | 8 |
| 2c4 4e | 12 | 10 | 9 | 9 |
| 2c4 6e | 10 | 7 | 6 | 6 |
| 2c4 6e | 11 | 9 | 8 | 8 |
| 2c4 6e | 12 | 10 | 9 | 9 |
| 2c4 8e | 10 | 6 | 6 | 5 |
| 2c4 8e | 11 | 9 | 8 | 6 |
| 2c4 8e | 12 | 10 | 9 | 8 |
| 0c3 0e | 10 | 5 | 2 | 2 |
| 0c3 0e | 11 | 8 | 6 | 3 |
| 0c3 0e | 12 | 10 | 9 | 4 |
| 0c3 2e | 10 | 6 | 3 | 3 |
| 0c3 2e | 11 | 9 | 8 | 4 |
| 0c3 2e | 12 | 10 | 9 | 7 |
| 0c3 4e | 10 | 5 | 2 | 2 |
| 0c3 4e | 11 | 6 | 3 | 3 |
| 0c3 4e | 12 | 10 | 9 | 7 |
| 0c3 6e | 10 | 6 | 3 | 3 |
| 0c3 6e | 11 | 8 | 6 | 4 |
| 0c3 6e | 12 | 10 | 9 | 7 |
| 0c3 8e | 10 | 5 | 2 | 2 |
| 0c3 8e | 11 | 8 | 6 | 3 |
| 0c3 8e | 12 | 10 | 9 | 4 |
| 4a2 0e | 10 | 6 | 6 | 5 |
| 4a2 0e | 11 | 9 | 8 | 6 |
| 4a2 0e | 12 | 10 | 9 | 8 |
| 4a2 2e | 10 | 7 | 6 | 6 |
| 4a2 2e | 11 | 9 | 8 | 8 |
| 4a2 2e | 12 | 10 | 9 | 9 |
| 4a2 4e | 10 | 9 | 7 | 6 |
| 4a2 4e | 11 | 10 | 8 | 8 |
| 4a2 4e | 12 | 11 | 10 | 9 |
| 4a1 0e | 10 | 8 | 7 | 7 |
| 4a1 0e | 11 | 10 | 9 | 8 |
| 4a1 0e | 12 | 11 | 9 | 9 |
| 4a1 2e | 10 | 8 | 7 | 7 |
| 4a1 2e | 11 | 10 | 9 | 8 |
| 4a1 2e | 12 | 11 | 9 | 8 |
| 4a1 4e | 10 | 11 | 8 | 7 |
| 4a1 4e | 11 | 12 | 9 | 8 |
| 4a1 4e | 12 | 13 | 9 | 8 |
| 2c3 0e | 10 | 7 | 7 | 6 |
| 2c3 0e | 11 | 8 | 8 | 7 |
| 2c3 0e | 12 | 10 | 9 | 8 |
| 2c3 2e | 10 | 9 | 7 | 7 |
| 2c3 2e | 11 | 10 | 8 | 8 |
| 2c3 2e | 12 | 11 | 9 | 8 |
| 2c3 4e | 10 | 9 | 7 | 7 |
| 2c3 4e | 11 | 10 | 8 | 8 |
| 2c3 4e | 12 | 11 | 9 | 8 |
| 2c3 6e | 10 | 8 | 7 | 7 |
| 2c3 6e | 11 | 9 | 8 | 8 |
| 2c3 6e | 12 | 11 | 9 | 8 |
| 2c3 8e | 10 | 7 | 7 | 6 |
| 2c3 8e | 11 | 8 | 8 | 7 |
| 2c3 8e | 12 | 10 | 9 | 8 |
| 0c4 0e | 10 | 8 | 7 | 7 |
| 0c4 0e | 11 | 9 | 8 | 8 |
| 0c4 0e | 12 | 10 | 9 | 9 |
| 0c4 2e | 10 | 8 | 7 | 5 |
| 0c4 2e | 11 | 9 | 8 | 8 |
| 0c4 2e | 12 | 10 | 9 | 9 |
| 0c4 4e | 10 | 8 | 7 | 5 |
| 0c4 4e | 11 | 9 | 8 | 8 |
| 0c4 4e | 12 | 10 | 9 | 9 |
| 0c4 6e | 10 | 7 | 4 | 4 |
| 0c4 6e | 11 | 9 | 8 | 8 |
| 0c4 6e | 12 | 10 | 9 | 9 |
| 0c4 8e | 10 |  |  |  |
| 0c4 8e | 11 | 8 | 5 | 4 |
| 0c4 8e | 12 | 9 | 9 | 8 |
| 4c3 0e | 10 | 8 | 7 | 7 |
| 4c3 0e | 11 | 9 | 8 | 8 |
| 4c3 0e | 12 | 10 | 9 | 8 |
| 4c3 2e | 10 | 8 | 7 | 6 |
| 4c3 2e | 11 | 9 | 8 | 8 |
| 4c3 2e | 12 | 11 | 9 | 8 |
| 4c3 4e | 10 | 8 | 7 | 7 |
| 4c3 4e | 11 | 10 | 8 | 8 |
| 4c3 4e | 12 | 11 | 9 | 8 |
| 4c4 0e | 10 | 7 | 4 | 4 |
| 4c4 0e | 11 | 9 | 8 | 5 |
| 4c4 0e | 12 | 10 | 9 | 8 |
| 4c4 2e | 10 | 7 | 5 | 5 |
| 4c4 2e | 11 | 9 | 8 | 8 |
| 4c4 2e | 12 | 10 | 9 | 9 |
| 4c4 4e | 10 | 7 | 5 | 5 |
| 4c4 4e | 11 | 9 | 8 | 8 |
| 4c4 4e | 12 | 10 | 9 | 9 |
| 4b2 0e | 10 | 9 | 7 | 7 |
| 4b2 0e | 11 | 10 | 8 | 8 |
| 4b2 0e | 12 | 11 | 9 | 9 |
| 4b2 2e | 10 | 10 | 7 | 6 |
| 4b2 2e | 11 | 11 | 8 | 8 |
| 4b2 2e | 12 | 12 | 9 | 9 |
| 4b2 4e | 10 | 9 | 7 | 6 |
| 4b2 4e | 11 | 10 | 8 | 8 |
| 4b2 4e | 12 | 11 | 9 | 9 |
| 4b5 0e | 10 | 7 | 7 | 7 |
| 4b5 0e | 11 | 8 | 8 | 8 |
| 4b5 0e | 12 | 10 | 9 | 8 |
| 4b5 2e | 10 | 7 | 7 | 6 |
| 4b5 2e | 11 | 8 | 8 | 8 |
| 4b5 2e | 12 | 10 | 9 | 8 |
| 4b5 4e | 10 | 7 | 7 | 7 |
| 4b5 4e | 11 | 8 | 8 | 8 |
| 4b5 4e | 12 | 10 | 9 | 8 |

**Late switches**: share of DRs whose shortest HTR among all readings of all optimal finishes is reached only by readings that switch after 3 or more moves, or after 4 or more (sampled, 25,000 per subset × edges, edges pooled by size), one row per corner subset:

| Subset | Needs a switch after 3+ moves | After 4+ moves |
|---|---|---|
| 0c0 | 11.4% | 3.5% |
| 2c5 | 43.5% | 23.5% |
| 2c4 | 24.1% | 8.7% |
| 0c3 | 25.0% | 6.3% |
| 4a2 | 20.2% | 6.7% |
| 4a1 | 10.3% | 2.7% |
| 2c3 | 17.9% | 5.5% |
| 0c4 | 67.4% | 32.4% |
| 4c3 | 30.4% | 11.6% |
| 4c4 | 50.5% | 30.4% |
| 4b2 | 16.1% | 4.9% |
| 4b5 | 31.6% | 16.2% |
| all DRs | 28.2% | 12.5% |

## Appendix B: how it was computed, and what checks it

**The model.**

- The DR group ⟨U, D, R2, L2, F2, B2⟩ with the first study's exact table of the optimal finish of all 19,508,428,800 DR states (proved in Lean there) and of the optimal leave-slice.
- Subsets are the first study's 48 (corner subset from the bad corners, the quarter turns the corners need and the 4a/4b shape; bad edges counted up to turning a layer).
- A Rust tool samples states uniformly within each subset × edges and enumerates every finish of the optimal length and one longer (both orders of commuting moves), using the exact table to prune. Each finish is read at every split, either side first, and its route, HTR length and quarter-turn counts recorded.
- Shortest HTRs (normal, inverse, NISS) come from an exact search. Reductions are counted from coset tables.
- Fixed targets of 10 to 12 use finishes up to max(optimal + 1, min(optimal + 2, 12)) moves.
- About an hour on four cores, at most 5 GB per job.

**What checks it.**

- The optimal distribution of every subset equals the first study's and Joba's in all 473 cells; DougCube's 663,552 HTR states give mean 10.13432557 exactly; Joba's DR-to-HTR lengths per subset agree.
- An independent sticker model (a 54-sticker cube built from geometry, with its own subset labels, HTR test and NISS reading) re-reads every optimal finish of 1,240 states (1,000 random DR scrambles and 5 per subset × edges from the sample): every finish replayed, every route and HTR length of every reading equal to the tool's. nissy 2.0.8 lists the same optimal finishes for all 1,240.
- Reduction counts from the coset tables equal a brute-force enumeration of every pair of sequences for reductions of up to 5 moves on 4,800 states (the first 100 of every subset × edges), and up to 7 moves on 40 states of 0c0 (the brute force for 7 moves was stopped there), which is why counts for 7 moves are not reported. Which reductions find the optimal comes from an exact search, not from the counts.
- The leave-slice maximum of 4a1 4e (15) is a count over the first study's exact leave-slice table, every state.
- A Lean 4 certificate in the study's folder recomputes the small exact tables from its own cube model and proves they equal the study's: the 663,552 HTR states, the corner quarter-turn counts and subsets of all 40,320 corner arrangements, the shortest linear HTR of every subset (all 29,400 HTR cosets), FakeMMAP's $\alpha$ for every corner path used, the *5/6 fake* count, the bare-qt reductions of 3qt and 4qt cases, and the 2qt(a)/(b) labels of Aedan Bryant's and the *Extra Quarter-Turn Stats* sheets from their own example triggers.
- Every move sequence in this write-up, the errata and the worked examples is replayed on the sticker model (the examples page states its count).

**Formally verified.** Two Lean 4 libraries in the study's folder, no Mathlib, no `sorry`. What they prove for this study:

- *HTRRoutes* (lean/HTRRoutes): the small exact tables, as in the bullet above.
- *FakeBound* (lean/FakeBound/FakeBound), FakeMMAP's bound as arithmetic for every N:
  - Finish.lean: each of the five terms is an upper bound on the reduction a finish needs, with term 2 as derived and $\alpha_{i+1}$ (`term1_sound` … `term5_sound`, `cover_sum`, `chain_bound`); the multi-qt lower bounds with $\alpha_{i+1}$ (`lower_stupid`, `lower_free`, `lower_A`, `lower_B`, `lower_C`).
  - Formula.lean: the smallest term is sound (`Rmin_sound`) and so is the largest, the formula as written (`Rmax_sound`).
  - Counter.lean: the counterexamples to the printed forms (`printed_term2_fails`, `literal_min_fails`, `witness_0c3`, `alpha_i_fails`), that the smallest term isn't always the exact worst case (`Rmin_not_tight`), and where C goes (`C_placement`).
  - Subset.lean, on the cube: half turns keep the subset × bad edges (`half_turns_keep_subset_data`, `labels_keep`), FakeMMAP's $C = 5$ and 6 (`fake_C_examples`), and $\alpha$ of the two counterexample paths (`counter_alphas`).
- *Corrections* (lean/FakeBound/Corrections/Examples.lean), the errata examples: the optimal finish of every DR state in a, c, d, e and f (`dr_optima_correct`, from the first study's proved table) and the printed finishes of a, d and f (`dr_solutions_valid`); the HTR lengths and printed HTRs of b and c (`htr_4c4`, `htr_13`); the subset names of a, d, e and f (`labels_htr_routes`); f's index example end to end (`index_example`, `index_example_arith`) and the C example (`C_example`). Each errata item says how much of its example is Lean-checked.

**Computed, not proved**: every share and mean from the samples (25,000 states per subset × edges, 4,000 for bounding), the exact model of section 9 (an enumeration in Python), the shortest NISS HTRs (the Rust tool's search, cross-checked with nissy), which finishes are optimal and how they read (the Rust tool, cross-checked on the sticker model and with nissy), the reduction counts, and the means over the first study's exact table, such as the gain from the last DR move.

## Docs referred to

- Levi Gibson, [*allcases*](https://docs.google.com/spreadsheets/d/1Vo6XzCFtJ-HEAuaBmk_pac-sJ3TbxEBb7BKsRJ_2wpA), [*Extra Quarter-Turn Stats (By HTR Subset)*](https://docs.google.com/spreadsheets/d/1fPCjS1ZQlP_Munut9MQkSbsL3CEdtT3LC5h3R8OMHGw), [*DR Bounding*](https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA).
- Aedan Bryant, [*HTR Subset Stats*](https://docs.google.com/spreadsheets/d/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0).
- rodneykinney, [*DR Finish Move Counts*](https://docs.google.com/spreadsheets/d/1tv8rwo2GF9IWuywFTnde_YlikIPBQvHqW9pysNG6BPM) and [*Advanced DR Bounding [Beta]*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0).
- DougCube, [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo).
- Yura Riabov, [*Hitchhiker’s Guide to HTR*](https://docs.google.com/document/d/1_NMlyPh2Ifd1E0ivos-15Sp-by-KPxoOsj9JD4pJuHI).
- Joba's exact optimal distribution per subset: a text file posted in #fmc-theory ([17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406633631165714492)).
- My first study, [*Judging a DR by hand*](../judging-a-dr/).
- nissy 2.0.8, by Sebastiano Tronto ([nissy.tronto.net](https://nissy.tronto.net)), used for the cross-checks.
