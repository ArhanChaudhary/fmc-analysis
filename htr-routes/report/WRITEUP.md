# Which HTR routes to try from a DR

Given a DR, which routes to HTR should you try, and in what order, to find the optimal finish? For each of the 48 subsets I sampled 25,000 uniformly random DR states (subset × bad edges, so 1,200,000 in all) and solved each one exactly: every optimal finish and every finish one move longer, read in every way NISS allows (switch after any move, either side first), and the same for the DR with its last move turned the other way. From that come ordered checklists of routes per subset, how long the HTRs on them are, how DR bounding compares, and whether FakeMMAP's reduction-length bound holds and prunes. Everything a finish length rests on is the first study's exact table of all 19,508,428,800 DR states; where a number is exact over all states it says so, otherwise it is a sample of 25,000 states per subset × edges (a share's standard error is at most 0.3 points per subset × edges, 0.2 per corner subset) unless a smaller sample is named.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion). Docs and sheets are listed with links at the end.

**This builds on** what the server already had:

- **The two path sheets.** [*Sub-13 Optimal Niss-HTR Paths*](https://docs.google.com/spreadsheets/d/1etiCnl6U-OHQAjEZIVIlk9iE64OXK3lrCyy14TLE_wE), forwarded by Daichi ([13 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515419690917433537)), and [*Optimal Niss-HTR Paths*](https://docs.google.com/spreadsheets/d/1D4qUhLOsJrwsBEzUVfmnLikuQNNB_eSZiPq-nS8KPN4), posted by deven ([12 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1537113949726572614)): for every subset × edges, the share of states whose optimal goes through each chain of corner subsets, NISS switches in brackets ("note that you can't add percentages because it counts all distinct paths from each state", [12 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1537114175900483705)). Neither says how it was made. Section 5 reconstructs it.
- **Daichi's cheat sheet** ([12 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515146431542067290): "to summarize, I think this is meta"), which turns the sub-13 sheet into a route list per subset ("It doesn't capture EVERYTHING, but I decided that checking these will capture a great portion of those", [12 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515177158870569101)). It is graded in section 10.
- **Levi Gibson's sheets and doc** (beef beans on Discord, posted as levitatingmagician): [*allcases*](https://docs.google.com/spreadsheets/d/1Vo6XzCFtJ-HEAuaBmk_pac-sJ3TbxEBb7BKsRJ_2wpA) ("What paths are most common for optimal DR solutions", [13 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1295051854635597856)), the [*Extra Quarter-Turn Stats (By HTR Subset)*](https://docs.google.com/spreadsheets/d/1fPCjS1ZQlP_Munut9MQkSbsL3CEdtT3LC5h3R8OMHGw) ([25 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1144726792217825370)), and [*DR Bounding*](https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA) ([27 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311464464737898589)), the method section 8 measures.
- **Aedan Bryant's [*HTR Subset Stats*](https://docs.google.com/spreadsheets/d/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0)** ([30 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069557424949833759)): 1,000 states per subset, mean optimal against shortest linear and NISS HTR.
- **Joba's exact optimal distribution per subset** ([17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406633631165714492): "This is not sampled, I looked at all 19508428800 DR states"), which the first study and this one reproduce cell for cell, and **DougCube's** [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo) ([2 Mar 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1345852930544369684)) with the finish of all 663,552 HTR states ("the *expected value* is 10.13", [13 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1416567970334773378)), also reproduced exactly.
- **rodneykinney's** [*DR Finish Move Counts*](https://docs.google.com/spreadsheets/d/1tv8rwo2GF9IWuywFTnde_YlikIPBQvHqW9pysNG6BPM) ([2 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1037387616313675806)), the corner-skeleton *normal forms* ([12 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1460293921883164881)) and [*Advanced DR Bounding [Beta]*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0) ([29 Aug 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1543125354120609832)).
- **FakeMMAP's** reduction-length bound and multi-qt lower bounds ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531394667773962), [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369), [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475)), with FakeMMAP's own caveat on the lower bounds, "I don't know how useful these bounds really are, I have to put in the numbers to see if there are situations where the typical bound is M \geq 11, rather than M \geq 7 lol." ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533429198553178)), and rodneykinney's request for per-case tables ([9 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491873063531188324)). Section 9 is that test.
- **JTuu's** 2c3 2e simulation of linear HTRs against bounding ([4 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313766061325156462)), **Zagros's** eight-step 4b2 order ([29 Dec 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1455301984415514719)), **Lewis Isom's** 4a2 list ([11 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1360414689019957449)) and 2c3 extension list ([18 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1373798214326554758)), Yura Riabov's 4b2 4e order and rogo's question about it ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258421085251178608), [4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258442750953525399)), and Jay's and rodneykinney's 3qt checks ([16 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1042617188370087988), [17 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1042817953072152596)).
- **My own first study** ([*Judging a DR by hand*](../judging-a-dr/)): the exact optimal finish of every DR state, the subset names, and *a third of the time the other DR is one shorter* for the last DR move.

**What this adds**:

- **A checklist per subset × edges**: the routes to try in order, each with the share of DRs where the routes so far find the optimal and a finish within +1, with and without a limit on how long the HTR may be.
- **How the path sheets were made**, worked out by reproducing them, and what that means for reading them (their shares are not *how often this route works*).
- **HTR lengths against the optimal**: linear against NISS HTR (rodneykinney's question from 2023), how often the optimal uses a shortest HTR, how often it needs 9 moves or more.
- **DR bounding measured**: per subset, how often checking every reduction to 1q (or 2q) of up to R moves finds the optimal, and how many reductions that is.
- **FakeMMAP's bound tested**: whether it is ever too short, how much it prunes, rodneykinney's per-subset tables, and a correction to the multi-qt lower bound.
- **Hand checklists graded** (Zagros, Yura Riabov's 4b2 4e order against reducing to 1q first, Lewis Isom, Daichi's cheat sheet), and **the claims checked**.

**Terms**, as the server uses them. Subsets are the first study's (Mallard's): 0c0, 4a1, 4a2, 4b2, 0c3, 2c3, 4c3, 0c4, 2c4, 4c4, 2c5, 4b5, each with its bad-edge count (4b2 4e). 4c3 is 4a3 on one side and 4b3 on the other, 4c4 is 4a4/4b4; routes name the side's own letter. Older names: Jay's qt names in Aedan Bryant's sheet and in *allcases* write 2qt(a) for 4b2 and 2qt(b) for 4a2, the *Extra Quarter-Turn Stats* sheet the other way round (its own example triggers show it), and Joba's file writes 4c5 for 4b5. *Optimal* is the shortest finish in DR moves (U, D, R2, L2, F2, B2), E slice solved; *+1* means a finish one move longer. *qt* is a U or D quarter turn. *Normal* and *inverse* are the two sides, inverse moves in brackets. Section 3 defines finish, route, HTR budget and the rest.

**How to read it.**

- **Start with [section 1](#1-the-short-version)**, the short version: what is new, then what it confirms or corrects. If you read one thing after it, make it the checklist table in [section 4](#4-the-checklists-subset-by-subset).
- **The [worked examples](examples.html)** go with it: 200 DRs from the 20 most common subset × edges, each with the checklist routes that find its optimal written out and the reduction bounding would use, answers folded away. **The [errata](errata.html)** list what the numbers show is wrong in things said on the server, each with an example.
- **Sections 5 to 11** are the details behind each line of section 1; the appendices are tables to look things up in.

---

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | What is new, then what it confirms or corrects, one line each. |
| [2. What was asked](#2-what-was-asked) | The questions, quoted, with where each is answered. |
| [3. Definitions](#3-definitions) | Finish, route, NISS readings, why an HTR budget, checklist, reduction. |
| [4. The checklists, subset by subset](#4-the-checklists-subset-by-subset) | **The main table.** Routes to try in order per subset, with the share that finds the optimal and +1, by HTR budget and by edges. |
| [5. The existing sheets, cell by cell](#5-the-existing-sheets-cell-by-cell) | How the path sheets were made, allcases, the 2qt(a)/(b) labels, Aedan Bryant's, the extra-QT sheet, DR Finish Move Counts. |
| [6. Shortest HTR against the optimal](#6-shortest-htr-against-the-optimal) | Linear against NISS HTR, which HTR the optimal uses, nine-move HTRs. |
| [7. Extra quarter turns, and the last DR move](#7-extra-quarter-turns-and-the-last-dr-move) | Three readings of "uses extra qts", half turns before the first qt, the last move either way. |
| [8. DR bounding](#8-dr-bounding) | How often every reduction up to R finds the optimal, how many reductions, against the checklists; Levi Gibson's and JTuu's numbers. |
| [9. FakeMMAP's reduction-length bound](#9-fakemmaps-reduction-length-bound) | Sufficient, how much it prunes, rodneykinney's tables, the index in the multi-qt lower bound. |
| [10. Hand checklists, graded](#10-hand-checklists-graded) | Zagros, Yura Riabov against rogo and Adri, Fanti, Lewis Isom, Jay and rodneykinney, Daichi's cheat sheet. |
| [11. The claims, checked](#11-the-claims-checked) | Each checkable statement from the server, with the verdict. |
| [12. What this does not cover](#12-what-this-does-not-cover) | Limits. |
| [Appendix A: full tables](#appendix-a-full-tables) | Every checklist, the path sheets' top paths, rodneykinney's table, late switches. |
| [Appendix B: how it was computed, and what checks it](#appendix-b-how-it-was-computed-and-what-checks-it) | Model, sampling, the sticker model, nissy, Lean. |
| [Docs referred to](#docs-referred-to) | Links. |

---

## 1. The short version

A top solver told me not to expect anything novel here, and for the routes themselves that is mostly right: the checklists below put the routes in the order Daichi's cheat sheet and the two path sheets already suggest. What is new is everything around the routes: how much each one covers, how long its HTRs are, how the sheets were made, how bounding compares, and whether FakeMMAP's bound helps. Shares are over uniformly random DR states of the subset (25,000 per subset × edges); *finds the optimal* means some optimal finish can be read along that route.

**What is new here**

- **How far a short checklist gets you, per subset.** Counting a route only when its HTR is at most 2 moves longer than the DR's shortest NISS HTR (budget 2, section 3), three routes find the optimal on 86.3% of 0c4, 91.4% of 2c5, 88.4% of 2c4, 78.0% of 2c3, 75.0% of 4c3, and only 62.6% of 4b2, 60.9% of 0c0 and 58.0% of 4a1; the same three find a finish within +1 on 84.3% (4a1) to 99.6% (4b5). After the third route each one adds at most 8.4 points, and less than 3 points in 91.7% of the checklists (section 4).
- **The HTR budget is what a checklist is about, not the route.** A NISS reading of a finish is also a linear finish, so *some optimal follows this route* barely separates routes: with no limit on HTR length, the best single route already covers 51% to 98% of a corner subset. With only the shortest HTRs (budget 0) the best single route covers 13% to 48%; budget 2 gives 29% to 84% (section 4).
- **How the path sheets were made.** Both *Optimal Niss-HTR Paths* sheets are reproduced (the full sheet to a mean difference of 0.8 points over 7,007 paths, correlation 0.965; the sub-13 sheet to 3.4 points, 0.907) when every optimal finish of a state is read only at its shortest-HTR NISS readings and every distinct path is counted once per state. So a share there is *how often this path carries an optimal with that finish's shortest HTR*, not *how often trying this route finds the optimal* (section 5).
- **Linear against NISS HTR** (rodneykinney asked in 2023, [30 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069660273356587082)): over all DRs the shortest NISS HTR equals the shortest linear one (better side) on 55.8%, is 1 shorter on 32.3% and 2 or more shorter on 11.9%; on 0c3 it is 2+ shorter on 52.4% (section 6).
- **The optimal rarely goes through a shortest HTR.** Some optimal uses a shortest NISS HTR on 32.9% of DRs; the shortest HTR any optimal uses is 1 longer on 31.8%, 2 longer on 22.5%, 3 or more on 12.8%. On 65.2% of all DRs every optimal needs an HTR of 9 moves or more, and on 29.7% that is so although a shorter HTR exists (section 6).
- **DR bounding, measured.** Checking every reduction to 1q (4a1 4e) of at most 4 moves, on either side or split, finds the optimal on 24.9% of DRs (89 reductions on average); at most 5, 40.6% (748); at most 6, 59.3% (6,242). Which subsets suit it depends on R: with reductions of at most 4 it is best on 0c0 (91.5%), 4a2 (76.6%) and 4a1 (75.6%). **What is doable by hand stops at about R ≤ 4**: the counts grow about eightfold per move, and only up to 4 do they stay in the low hundreds, the size of the "check all sub-5 reductions" Levi Gibson calls "super quick" ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311670582601060354)). Beyond that it is **computer only, an answer key and not advice**: on 0c0, where eight budget-2 routes stay under 80%, reductions up to 3 get there with about 156 to write, which is in reach; on 4a1 the same 80% takes every reduction up to 5 (about 4,901) and on 4b2 up to 6 (about 16,087), which nobody writes in an hour. On 2c5 and 4b5 nothing under 6 moves works. Reducing to 2q instead, reductions of at most 3 moves reach 60.4% (section 8).
- **FakeMMAP's bound, tested as FakeMMAP asked.** As written it is never too short in the sample (1,914,809 state-and-path cases at the optimum), but it asks for reductions of 12.1 moves on average where 7.0 were needed, longer than any solver writes, so it prunes nothing in practice; solving the same model exactly gives 8.9. FakeMMAP's multi-qt lower bounds ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475)) fail on 923 of those cases: their sum needs α of the section the two windows share (α_{i+1}), not α_i; with that change they never fail. FakeMMAP asked whether "the typical bound is M \geq 11, rather than M \geq 7" ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533429198553178)): once every reduction shorter than the one the optimal needs has failed, the corrected bound is 11 on a typical 2c3 path, 10 on 4b2 and 8 on 0c0, one or two above the trivial bound, but it reaches the optimum in only 3.5% of 2c3 cases. The per-subset tables rodneykinney asked for ([9 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491873063531188324)) are in section 9 and appendix A.
- **Hand checklists graded.** Zagros's eight-step 4b2 order finds the optimal on 71.3% with budget-2 HTRs and a finish within +1 on 93.4%. On 4b2 4e, Yura Riabov's order (trigger, then regress to 2c3) finds 62.3% after two steps and 72.9% after three; reducing to 1q first, every reduction of at most 4 or 5 moves finds 52.5% or 68.6% (section 10).

**What it confirms or corrects**

- **Confirmed: the routes.** The first route of the budget-2 checklist is the top path of *Optimal Niss-HTR Paths* on 45 of the 48 subset × edges (of the sub-13 sheet on 35; counting a route and its mirror reading as one; where they differ it is mostly the same chain with the switch one quarter turn earlier or later), and it is what Daichi's cheat sheet says (switch after 4b2 on 4c3 and 0c4, through 2c3 on 2c4 and 2c5, 4a2 4e switch on 0c3). Graded, Daichi's sheet finds the optimal more often than my first three routes on 4b2, 4a1, 2c3 0e and 8e and 0c0 2e to 6e, about as often on 2c4 0e to 6e, 4a2 2e and 0c4 2e, and less often elsewhere (all of 2c5, 0c3, 4c3, 4c4 and 4b5, 0c4 except 2e, 4a2 0e and 4e, 2c3 2e to 6e) (section 10).
- **Confirmed: the known tables**, exactly: Joba's optimal distribution, DougCube's 663,552 HTR states (mean 10.13), Joba's DR-to-HTR lengths; Aedan Bryant's sheet except four rows that carry another row's numbers and its two fake-HTR rows, whose states were built around one trigger; the *Extra Quarter-Turn Stats* sheet on every comparable row (sections 5, 11).
- **The 2qt(a)/(b) labels.** Aedan Bryant's sheet and *allcases* call 4b2 "2qt(a)", as Tzak, Levi Gibson and Zagros said at the time; the one thing added here is that the *Extra Quarter-Turn Stats* sheet uses the opposite letters, shown by its own example triggers. So mrauo's "Only 1/3 of 2q 4b2e cases use 2qt" read the 4a2 2e row (section 5).
- **Explained: the quoted extra-qt numbers** depend on whether you ask about every optimal, some optimal or one optimal from a solver; rodneykinney's 57% and Lichi Fang's "over 60%" fit different readings, and both fit (section 7).
- **Corrected, with the first study's table: the last DR move.** Turning it the other way gives a finish one move shorter on 32.5% of DRs, never more than one, so about a third of a move on average, not the 1/6 Yura Riabov estimated in 2024 (Yura called it "very rough"). It does not change which routes to try (section 7).
- **Corrected** (errata, each with an example): Levi Gibson's "check all sub-5 reductions … gets optimal like 75% of the time, and it gets optimal +1 the rest of the time" (bounding alone on 2c3: 48.1% and 78.8%); 4c4 0e has 10-move linear HTRs; the longest shortest HTR is 13 linear and 12 with NISS; switching after more than 2 moves is needed for the shortest optimal HTR on 24.0% of the DRs outside the subsets Evan named as exceptions (Yura Riabov's "more like 3" holds outside 0c4, 4c4 and 2c5); the index in FakeMMAP's multi-qt lower bounds.
- **Confirmed**: Levi Gibson's "pretty sure 15 is gods number for 4a1 4e" is right for the leave slice, which is what Levi Gibson measures (15, exact); the full finish can need 17.

---

## 2. What was asked

The questions, in the words of the people who asked them, with where each is answered. Most got a guess or no answer at the time.

**Which routes, how often (sections 4 and 5)**

- Daichi built the cheat sheet from the sub-13 path sheet "to filter routes to check rather than DRs itself" ([12 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515177158870569101)); JTuu asked for the data behind it ("did you post the raw stats somewhere?", [13 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515419517873033256)) and got the sheet. deven, posting the full sheet: "note that you can't add percentages because it counts all distinct paths from each state" ([12 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1537114175900483705)). *Answer*: section 4 gives the routes in an order where the shares do add up (cumulative), section 5 shows what the sheets count.
- wen ([8 Nov 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1171788784279494688)): "Anyone else feel like for 4q 2c, the optimals are most often reasonably explained with something like a direct HTR, or 1q then switch and 3q, and hardly ever with 2q switch 2q?" *Answer*: on 2c4, with HTRs at most 2 over the shortest, 3 qts then a switch (or 1 then 3) reaches the optimal on 66.5%, a direct HTR on 54.0%, 2 switch 2 on 30.8%. wen's order is right; "hardly ever" is too strong.
- Yura Riabov, on 4b2 4e ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258421085251178608)): "4b2 4e is basically the best 4q subset"; rogo ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258442750953525399)): "the first approach apart from R U2 F2 R to check should still be 'reduce to 1qt 4e and niss trace for short htrs' i think?" *Answer*: section 10.

**HTRs and the optimal (section 6)**

- rodneykinney ([30 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069660273356587082)): "How often is one significantly shorter than the other, and how often is it just as long to get to HTR either way?" (linear against NISS HTR). No answer in the export. *Answer*: section 6, per subset.
- Brian ([24 Feb 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1211149426198847488)): "Are there stats for how often the optimal finish for a DR uses an optimal HTR solution for that DR?" Tom Nelson ([24 Feb 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1211151427460800612)): "I assume it'd be quite high for 4-5q and low for good subsets". Zagros ([27 Dec 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1454570265353912422)): "anyone know what % of DRs (maybe by subset?) have an optimal solution from the shortest HTR on one of the sides, or maybe also the shortest possible niss HTR". JTuu ([27 Dec 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1454571263434690803)): "anything of the form "does there exist an optimal with X property" is gonna be computationally very bad". *Answer*: some optimal uses a shortest NISS HTR on 32.9% of DRs, a shortest linear HTR of its side on 25.2%. Tom Nelson's guess is right in direction for 0c3 (53.5%) but not for 4-5qt in general (2c4 31.6%, 4b5 31.4%, against 4b2 30.0%).
- kalindumaxxer ([27 Jul 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1266881061418176522)): "how common does the optimal solution for htr-2e use an inoptimal htr". Jakob Jernsletten ([29 Jul 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1267543886184579072)): "Probably almost always? There are so few optimal HTRs compared to the many more variants in +1 or more". *Answer*: on 0c0 2e no optimal uses a shortest NISS HTR on 67.8%. Common, not almost always.
- rodneykinney ([13 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1063504388976545902)): "I'm interested to know how often the solution involves a non-optimal HTR". Daichi ([3 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1511617316876587109)): "Do we know the average length of post HTR on DR optimal solutions only?" wen ([3 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1511620241313108008)): "Tldr no". *Answer*: section 6; the post-HTR part of the optimal with the shortest HTR is 4.59 moves on average.
- Yura Riabov ([8 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1392217666130804837), [8 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1392217798851297352)): "Is there a stat on average slice in dr optimals?", "I know average slice is 0.9ish but i don't know about optimals". *Answer*: the optimal finish is 0.290 moves longer than the optimal leave-slice on average; from 0.71 on 0c0 down to 0.05 on 0c3. Aedan Bryant's sheet had the same in its "No E Difference" column.

**Extra quarter turns, and the last DR move (section 7)**

- tseitsei89 ([25 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1233062604705108060)): "how common is it to have a 3qt DR where the ONLY optimal solution(s) go through 5qt path? I just had one". Yura Riabov ([25 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1233063193782259764)): "not too rare, but depends on the case". *Answer*: every optimal uses 5qt on 17.5% of 2c3, 27.4% of 4c3, 24.0% of 0c3; by edges in section 7.
- Lichi Fang ([2 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1246934529072042056), [6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248336857452908564)): "Do we have any statistics about the average move it takes to finish a DR when allowing the last move of the DR to be inverted?", "how much do you think would inverting the last move of DR change the length for DR finish?" *Answer*: section 7 (and the first study, 6.6).

**DR bounding and FakeMMAP's bound (sections 8 and 9)**

- Kai Cui ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312050785743278140)): "How often can you get optimal with just sub5". Levi Gibson ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312050982489952397)): "Surprisingly often"; Kai Cui: "Would it be around 80 percent?" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051034906038323)), Levi Gibson: "yeah something like that I'd guess" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051081831780434)), "for 2c3 that is" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051112253329439)). *Answer*: section 8 and the errata.
- A professional solver asked me, through the site's author, how effective DR bounding is per subset (how often it finds the optimal, and how many reductions to 1q or 2q you need to check for that, depending on the threshold), and whether FakeMMAP's linear-programming estimates can prune branches. *Answer*: sections 8 and 9.
- rodneykinney, on FakeMMAP's bound ([9 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491873063531188324)): "This sounds interesting but, I must say, almost impossible to follow. Would it be possible to put together some tables for specific cases?" FakeMMAP ([9 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491880288597446767)): "Compute these bounds by HTR subsets." *Answer*: section 9 and appendix A.

What this leaves open is in section 12.

---

## 3. Definitions

**Finish.** A sequence of DR moves (U, D, R2, L2, F2, B2) that solves the DR state, E slice included. No DR-breaking or HTR-breaking moves in the HTR part; the post-HTR part may be anything in the DR group, so a finish whose last part has a quarter turn counts (it is rare: marked `| qt` in the files). For each state I list every optimal finish and every finish one move longer, including both orders of moves that commute.

**Corner path, route.** Read a finish move by move and write down the corner subset at the start and after each quarter turn, until the cube is in HTR (corners and edges). `4b2 > 2c3 > 4b2 > 4a1 > 0c0` is a 4b2 that regresses to 2c3, comes back to 4b2, then goes 4a1 and HTR. The moves up to that point are the finish's HTR, the rest its post-HTR part. A *route* (route class) is the chain plus where the NISS switch is: `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` means one qt on the first side to 2c3, then switch, and the rest on the other side, where the subsets are read on that side. That is the notation of the two path sheets and Daichi's cheat sheet; this study made the list of routes from the data, not from a list chosen in advance. Edge counts are dropped from route names in the tables (they are in the files).

**NISS readings.** A finish S of a state X can be found as A on normal and then B on inverse whenever S = A·B⁻¹; and the other way, B on inverse first. So every finish of n moves has 2(n + 1) readings, one per split and side. A route *works* on a state if some reading of some optimal finish (or +1 finish, at +1) follows it. Both sides are always available: a linear route on the inverse is a reading too.

**Why a budget is needed.** The catch is that every NISS reading is also a linear finish of the same length. So *some optimal follows route X* says nothing about whether NISS was needed: whenever a NISS reading of an optimal follows X, the same moves read linearly follow some other route, and a route that is long enough on one side almost always has some reading that fits. With no limit, three routes cover 93.6% to >99.9% of a corner subset (section 4), which is true and useless. What NISS really changes is how long the HTR is that you have to find. So each route is graded with an **HTR budget**: it counts on a state only if its reading reaches HTR within the state's shortest NISS HTR plus the budget (moves on both sides counted). Budget 0 means you only ever look at the shortest HTRs; budget 2 means HTRs up to two moves longer than the shortest; *no limit* is the plain route. I use budget 2 as the default: it is about what a strong solver checks, and the tables give 0, 1, 2 and no limit.

**Checklist.** For a subset × edges (or a corner subset with its edge counts pooled by their exact sizes), the routes in greedy order: first the route that works on the most states, then the one that adds the most states not yet covered, and so on. The cumulative share after k routes is the share of DRs where at least one of the first k finds an optimal finish (or within +1). Greedy is close to the best possible set (tested with no HTR limit): among the top 25 to 40 routes, the best set of 1 to 4 routes beats greedy by at most 0.5 points in 2,192 of 2,208 cases, and by 1.8 points at worst.

**Reduction (bounding).** A reduction to 1q is a pair of sequences, P on normal and U on inverse, each empty or ending in a quarter turn, after which the state (inverse of U, then the scramble, then P) is 4a1 4e, so one more quarter turn and half turns finish it. Its length is |P| + |U|. A reduction to 2q ends in a state that a finish with exactly two quarter turns solves (4a2, 4b2, or 0c0 with bad edges). Bounding with threshold R means writing every reduction of length at most R and finishing each reduced state as well as it can be finished. *Bounding finds the optimal* means that some reduction of length at most R plus the optimal finish of the reduced state is an optimal finish of the DR. That is the best a solver can get from those reductions; the bound arithmetic in the bounding docs only decides the order and when to stop.

**The last DR move.** If the DR ends in a quarter turn of a side face (R, say), R' is also a DR, and its state is X·R2. *With the last move either way* takes the better of X and X·R2, as in the first study.

**Samples.** For each of the 48 subset × edges, 25,000 states drawn uniformly from the subset (each DR state equally likely), seed 20261112. Corner-subset rows pool the edge counts weighted by the exact number of states in each, so they are shares of uniformly random DR states of that corner subset. Counts of reductions use the first 4,000 states per subset × edges. Fixed targets (a finish of 10, 11 or 12 or better) use every finish up to max(optimal + 1, min(optimal + 2, 12)) moves. Where a reading needs one optimal per state picked at random (to compare with sheets that recorded one solver output), I use 5,000 states per subset × edges, seed 7; the reading rules for the path sheets were tested on 5,000 per subset × edges, seed 11.

---

## 4. The checklists, subset by subset

This is the main table. For each corner subset (edge counts pooled by their real frequency): the first three routes of the budget-2 checklist, the share of DRs where the routes so far find an optimal finish after 1, 2, 3 and 5 routes, the share where the same three find a finish within +1, and, for comparison, three routes with no limit on HTR length. Sampled, 25,000 states per subset × edges; brackets are the part after the NISS switch; a route ends at HTR (`0c0`).

| Subset | Try first | Then | Then | Optimal after 1 / 2 / 3 / 5 classes | Within +1, same 3 | No HTR limit, 3 classes |
|---|---|---|---|---|---|---|
| 0c0 | `0c0 > 4a1 > 0c0` | `0c0 > 4a1 > (0c0)` | `0c0 > 4a1 > 0c0 > 4a1 > (0c0)` (mirror: `0c0 > 4a1 > (4a2 > 4a1 > 0c0)`) | 42.3% / 55.9% / 60.9% / 65.8% | 86.4% | 97.4% |
| 2c5 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 72.8% / 85.5% / 91.4% / 93.1% | 98.9% | 98.8% |
| 2c4 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > 4a1 > (0c0)`) | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 66.0% / 83.5% / 88.4% / 89.3% | 98.7% | 98.9% |
| 0c3 | `0c3 > 4a2 > (4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > (0c0)`) | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `0c3 > 4a2 > (4a1 > 4b2 > 4a1 > 0c0)`) | `0c3 > 4a2 > 4b3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > 4b2 > (4a1 > 0c0)`) | 74.4% / 88.8% / 89.3% / 90.1% | 99.1% | 99.4% |
| 4a2 | `4a2 > 4a1 > (0c0)` | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `4a2 > 4a1 > (4b2 > 4a1 > 0c0)`) | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 41.6% / 64.1% / 73.2% / 81.6% | 90.8% | 93.6% |
| 4a1 | `4a1 > 4b2 > 4a1 > 0c0` | `4a1 > 0c0 > (4a1 > 0c0)` (mirror: `4a1 > 4a2 > 4a1 > (0c0)`) | `4a1 > 0c0` | 29.3% / 44.8% / 58.0% / 72.2% | 84.3% | 97.1% |
| 2c3 | `2c3 > 4b2 > 4a1 > 0c0` | `2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a1 > (0c0)`) | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 53.5% / 75.7% / 78.0% / 80.1% | 96.1% | 99.5% |
| 0c4 | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | `0c4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 4a1 > (0c0)`) | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 83.8% / 85.1% / 86.3% / 88.2% | 97.6% | >99.9% |
| 4c3 | `4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4b3 > 4a2 > 4a1 > (0c0)`) | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b3 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 64.3% / 71.3% / 75.0% / 80.0% | 94.2% | 99.0% |
| 4c4 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4a4 > 0c3 > 4a2 > (4a1 > 0c0)`) | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b4 > 4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b4 > 2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)`) | 68.1% / 75.0% / 78.4% / 81.8% | 96.1% | 99.2% |
| 4b2 | `4b2 > 4a1 > 0c0` | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `4b2 > 2c3 > (4b2 > 4a1 > 0c0)`) | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 37.6% / 53.3% / 62.6% / 71.4% | 88.0% | 97.2% |
| 4b5 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 64.7% / 87.4% / 93.7% / 93.9% | 99.6% | 99.5% |

How to read a row, with 4c3: try `4a3 > 4b2 > (4a1 > 0c0)` first: on the 4a3 side, one qt to 4b2, switch, and on the other side 4a1 and HTR. The same moves read the other way round are its mirror, `4b3 > 4a2 > 4a1 > (0c0)`: starting on the 4b3 side, qt to 4a2, qt to 4a1, switch for the last qt. Every split of a finish has such a mirror, and the table names both; as classes they are not the same (each also collects other finishes, and only 646 of 21,552 mirror pairs cover exactly the same states), so the share is for the reading named first. With HTRs up to two over the shortest that route alone finds the optimal on 64.3% of 4c3. Then the b side: `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)`, then the regression through 2c3 on the a side. The b-side route through 4a2 read linearly, `4b3 > 4a2 > 4a1 > 0c0`, is fifth. An example is in the [worked examples](examples.html) and this one: the 4c3 4e reached by `L2 U2 F2 L2 D' F2 R2 D' L2 B2 U2 B2 D' R2` is 14 optimal, and the first route finds it as `B2 R2 D'` on normal, then `(F2 L2 U2 F2 D' L2 U R2 U2 R2 B2)` on inverse, HTR in 10 (replayed).

What the table says, subset by subset, in words:

- **0c3, 0c4, 2c4, 2c5, 4b5** are the easy ones for a checklist: three routes cover 89.3%, 86.3%, 88.4%, 91.4% and 93.7%. 0c3: `4a2 4e` then switch. 0c4: `4a3 > 4b2`, switch. 2c4, 2c5, 4b5: down the 2c chain to 2c3, switch at 2c3 (or one step earlier), or linear. This is what Daichi's cheat sheet says.
- **4c3, 4c4, 2c3** need four or five routes for 80% (80.0%, 81.8%, 80.1% after five); the first one does most of the work.
- **4b2, 4a1, 0c0** are where checklists struggle: the optimal is spread over many routes, and eight routes stop at 69.4% (0c0), 74.6% (4a1), 75.0% (4b2). These are the subsets where bounding does better (section 8). On 4b2 the 2qt route `4b2 > 4a1 > 0c0` comes first but alone finds only 37.6%; the regressions through 2c3 come next.
- **Within +1** the same three routes reach 86.4% on 0c0, 84.3% on 4a1, 88.0% on 4b2, and 90% or more on the other 9. If you only need a finish within one move of optimal, three routes are enough nearly everywhere. (At +1 a route counts if any of its finishes within +1 has an HTR within the budget, which may be shorter than on its optimal finishes.)

**The budget.** The same checklists built for budget 0 (only the shortest HTRs), 1, 2 and no limit, after 1 and 3 routes:

| Subset | Budget 0 (shortest HTRs only): 1 / 3 classes | Budget 1 | Budget 2 | No limit |
|---|---|---|---|---|
| 0c0 | 20.5% / 32.8% | 32.0% / 48.1% | 42.3% / 60.9% | 59.2% / 97.4% |
| 2c5 | 20.0% / 30.8% | 48.1% / 69.3% | 72.8% / 91.4% | 95.3% / 98.8% |
| 2c4 | 17.4% / 30.9% | 40.5% / 64.7% | 66.0% / 88.4% | 94.2% / 98.9% |
| 0c3 | 47.7% / 53.2% | 68.0% / 78.3% | 74.4% / 89.3% | 76.0% / 99.4% |
| 4a2 | 18.1% / 35.0% | 31.3% / 59.6% | 41.6% / 73.2% | 50.6% / 93.6% |
| 4a1 | 12.8% / 23.3% | 16.8% / 41.0% | 29.3% / 58.0% | 79.1% / 97.1% |
| 2c3 | 16.3% / 31.0% | 33.6% / 57.2% | 53.5% / 78.0% | 82.5% / 99.5% |
| 0c4 | 34.6% / 37.5% | 61.7% / 67.4% | 83.8% / 86.3% | 90.0% / >99.9% |
| 4c3 | 25.8% / 32.8% | 46.7% / 56.8% | 64.3% / 75.0% | 72.6% / 99.0% |
| 4c4 | 26.2% / 31.6% | 51.0% / 57.4% | 68.1% / 78.4% | 72.9% / 99.2% |
| 4b2 | 18.8% / 26.6% | 30.0% / 43.8% | 37.6% / 62.6% | 73.5% / 97.2% |
| 4b5 | 14.8% / 31.1% | 39.7% / 69.8% | 64.7% / 93.7% | 98.0% / 99.5% |

With only shortest HTRs, no subset gets past 53% with three routes: you have to write HTRs one or two moves longer than the shortest. With no limit, the first route alone covers most states: that is the *every route works if you allow the HTR to be long* effect of section 3, not a reason to try only one route.

**Cheap and marginal routes.** After the third route, each further route adds at most 8.4 points, and in 91.7% of the checklists (subsets × edges and corner subsets) less than 3 points (budget 2). Routes 4 to 8 pay only at the margin, so if you have time for more, a second DR or bounding (section 8) is likely the better use of it on 0c0, 4a1 and 4b2.

**By edges.** The checklist for each subset × edges, first three routes (all 8 routes with their cumulative shares at the optimum and at +1, and the no-limit lists, are in appendix A):

| Subset | Try first | Then | Then | Optimal after 1 / 2 / 3 | Within +1, same 3 |
|---|---|---|---|---|---|
| 0c0 0e | `0c0 > 4a1 > 0c0` | `0c0` | `0c0 | qt` | 42.5% / 84.4% / 92.6% | 98.3% |
| 0c0 2e | `0c0 > 4a1 > 0c0` | `0c0 > 4a1 > 0c0 > 4a1 > (0c0)` (mirror: `0c0 > 4a1 > (4a2 > 4a1 > 0c0)`) | `0c0 > 4a1 > (0c0)` | 60.5% / 65.7% / 70.2% | 92.3% |
| 0c0 4e | `0c0 > 4a1 > 0c0` | `0c0 > 4a1 > (0c0)` | `0c0 > 4a1 > 4b2 > 4a1 > 0c0` | 44.9% / 57.8% / 61.5% | 88.1% |
| 0c0 6e | `0c0 > 4a1 > (0c0)` | `0c0 > 4a1 > 0c0 > 4a1 > (0c0)` (mirror: `0c0 > 4a1 > (4a2 > 4a1 > 0c0)`) | `0c0 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `0c0 > 4a1 > 4b2 > 4a1 > (0c0)`) | 40.8% / 53.7% / 60.2% | 88.0% |
| 0c0 8e | `0c0 > 4a1 > (0c0)` | `0c0 > 4a1 > 0c0` | `0c0 > 4a1 > 0c0 > 4a1 > (0c0)` (mirror: `0c0 > 4a1 > (4a2 > 4a1 > 0c0)`) | 53.5% / 70.1% / 77.1% | 95.0% |
| 2c5 0e | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.8% / 86.5% / 89.6% | 98.7% |
| 2c5 2e | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 74.8% / 86.2% / 91.0% | 98.7% |
| 2c5 4e | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 71.5% / 86.0% / 91.9% | 99.0% |
| 2c5 6e | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 73.0% / 84.1% / 90.6% | 98.7% |
| 2c5 8e | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% / 86.0% / 91.0% | 98.9% |
| 2c4 0e | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > 4a1 > (0c0)`) | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 70.1% / 85.9% / 88.6% | 98.7% |
| 2c4 2e | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > 4a1 > (0c0)`) | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 67.7% / 86.3% / 89.9% | 98.9% |
| 2c4 4e | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > 4a1 > (0c0)`) | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 62.0% / 82.0% / 87.6% | 98.7% |
| 2c4 6e | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > 4a1 > (0c0)`) | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 73.8% / 84.1% / 88.5% | 98.6% |
| 2c4 8e | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > 4a1 > (0c0)`) | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.7% / 89.5% / 91.5% | 99.4% |
| 0c3 0e | `0c3 > 4a2 > (4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > (0c0)`) | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `0c3 > 4a2 > (4a1 > 4b2 > 4a1 > 0c0)`) | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4b3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 85.5% / 94.2% / 96.6% | 99.8% |
| 0c3 2e | `0c3 > 4a2 > (4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > (0c0)`) | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `0c3 > 4a2 > (4a1 > 4b2 > 4a1 > 0c0)`) | `0c3 > 4a2 > 4a1 > 0c0` | 80.8% / 91.3% / 92.1% | 99.5% |
| 0c3 4e | `0c3 > 4a2 > (4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > (0c0)`) | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `0c3 > 4a2 > (4a1 > 4b2 > 4a1 > 0c0)`) | `0c3 > 4a2 > 4b3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > 4b2 > (4a1 > 0c0)`) | 67.2% / 85.1% / 85.8% | 98.7% |
| 0c3 6e | `0c3 > 4a2 > (4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > (0c0)`) | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `0c3 > 4a2 > (4a1 > 4b2 > 4a1 > 0c0)`) | `0c3 > 4a2 > 4a1 > 0c0` | 82.6% / 93.9% / 94.6% | 99.7% |
| 0c3 8e | `0c3 > 4a2 > (4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > (0c0)`) | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `0c3 > 4a2 > (4a1 > 4b2 > 4a1 > 0c0)`) | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `0c3 > 4a4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 87.3% / 94.8% / 96.1% | 99.7% |
| 4a2 0e | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `4a2 > 4a1 > (4b2 > 4a1 > 0c0)`) | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | `4a2 > 4a1 > (0c0)` | 29.1% / 40.4% / 44.4% | 68.2% |
| 4a2 2e | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `4a2 > 4a1 > (4b2 > 4a1 > 0c0)`) | `4a2 > 4a1 > (0c0)` | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 42.2% / 67.8% / 76.8% | 95.7% |
| 4a2 4e | `4a2 > 4a1 > 0c0` | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `4a2 > 4a1 > (4b2 > 4a1 > 0c0)`) | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 60.9% / 72.2% / 79.1% | 93.6% |
| 4a1 0e | `4a1 > 0c0 > (4a1 > 0c0)` (mirror: `4a1 > 4a2 > 4a1 > (0c0)`) | `4a1 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `4a1 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)`) | `4a1 > 0c0 > 4a1 > (0c0)` (mirror: `4a1 > 4a2 > (4a1 > 0c0)`) | 33.5% / 46.5% / 54.6% | 84.2% |
| 4a1 2e | `4a1 > 4b2 > 4a1 > 0c0` | `4a1 > 0c0 > 4a1 > 0c0` | `4a1 > 0c0 > (4a1 > 0c0)` (mirror: `4a1 > 4a2 > 4a1 > (0c0)`) | 38.8% / 58.8% / 70.5% | 91.7% |
| 4a1 4e | `4a1 > 0c0` | `4a1 > 4b2 > 4a1 > 0c0` | `4a1 > 0c0 > (4a1 > 0c0)` (mirror: `4a1 > 4a2 > 4a1 > (0c0)`) | 33.6% / 50.3% / 60.6% | 86.2% |
| 2c3 0e | `2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a1 > (0c0)`) | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | `2c3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 46.3% / 67.0% / 75.1% | 95.9% |
| 2c3 2e | `2c3 > 4b2 > 4a1 > 0c0` | `2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a1 > (0c0)`) | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 66.5% / 79.6% / 80.2% | 96.6% |
| 2c3 4e | `2c3 > 4b2 > 4a1 > 0c0` | `2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a1 > (0c0)`) | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 55.3% / 76.6% / 78.1% | 96.1% |
| 2c3 6e | `2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a1 > (0c0)`) | `2c3 > 4b2 > 4a1 > 0c0` | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 66.1% / 73.3% / 76.7% | 95.8% |
| 2c3 8e | `2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a1 > (0c0)`) | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 46.3% / 67.2% / 74.5% | 95.7% |
| 0c4 0e | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | `0c4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 83.2% / 86.8% / 87.6% | 97.5% |
| 0c4 2e | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `0c4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 86.5% / 88.0% / 89.1% | 98.1% |
| 0c4 4e | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | `0c4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 83.5% / 85.1% / 86.1% | 97.5% |
| 0c4 6e | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | `0c4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 4a1 > (0c0)`) | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `0c4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 81.8% / 83.7% / 85.4% | 97.8% |
| 0c4 8e | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | `0c4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 4a1 > (0c0)`) | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `0c4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 80.3% / 86.2% / 87.1% | 98.2% |
| 4c3 0e | `4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4b3 > 4a2 > 4a1 > (0c0)`) | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b3 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 70.8% / 78.4% / 83.3% | 96.2% |
| 4c3 2e | `4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4b3 > 4a2 > 4a1 > (0c0)`) | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b3 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 66.2% / 72.0% / 75.1% | 94.3% |
| 4c3 4e | `4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4b3 > 4a2 > 4a1 > (0c0)`) | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b3 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 62.3% / 70.2% / 74.4% | 93.9% |
| 4c4 0e | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4a4 > 0c3 > 4a2 > (4a1 > 0c0)`) | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b4 > 2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)`) | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 65.2% / 72.4% / 76.7% | 96.3% |
| 4c4 2e | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4a4 > 0c3 > 4a2 > (4a1 > 0c0)`) | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b4 > 4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b4 > 2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)`) | 67.9% / 75.4% / 78.7% | 96.4% |
| 4c4 4e | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4a4 > 0c3 > 4a2 > (4a1 > 0c0)`) | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b4 > 4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b4 > 2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)`) | 68.4% / 74.8% / 78.2% | 95.9% |
| 4b2 0e | `4b2 > 4a1 > 0c0` | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `4b2 > 4a1 > 0c0 > (4a1 > 0c0)`) | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 36.5% / 51.1% / 61.0% | 85.5% |
| 4b2 2e | `4b2 > 4a1 > 0c0` | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `4b2 > 2c3 > (4b2 > 4a1 > 0c0)`) | `4b2 > 4a1 > (0c0)` | 45.9% / 53.7% / 59.0% | 86.3% |
| 4b2 4e | `4b2 > 4a1 > 0c0` | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 30.3% / 53.3% / 66.8% | 89.1% |
| 4b5 0e | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 60.8% / 84.2% / 92.6% | 99.4% |
| 4b5 2e | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 62.6% / 85.1% / 93.6% | 99.6% |
| 4b5 4e | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 67.0% / 89.6% / 93.9% | 99.6% |

Where the edges change the order: 4a2 0e and 2e start with the 4b3 regression (`4a2 > 4b3 > 4a2 > 4a1 > (0c0)`), 4a2 4e with the 2qt route; 4a1 0e with the 0c0 route and a switch, 4a1 2e through 4b2, 4a1 4e with the 1qt route; 2c4 0e linear, the other 2c4 with a switch at 2c3. The hardest row is 4a2 0e (44.4% after three routes).

Two examples of the first route on 2c4 and of the 4b2 regression, both replayed (the first is a no-limit instance: its HTR of 13 is longer than budget 2 allows on that DR): the 2c4 4e of `R2 F2 R2 D2 F2 D F2 D R2 U' L2 D F2 U2` (14 optimal) is found by `(R2 F2 R2 D2 F2 D)` on inverse (2c4 to 2c3), then `U2 F2 D' L2 U R2 D' F2` on normal; the 4b2 4e of `B2 L2 U F2 D' R2 U L2 B2 L2 D2 B2 R2 D'` (14 optimal) by `D` (to 2c3), switch, then `(B2 L2 U F2 D' R2 U L2 B2 L2 D2 B2 R2)`.

**The last DR move** shifts every route about equally and changes no checklist (section 7).

---

## 5. The existing sheets, cell by cell

**The two path sheets.** Neither *Sub-13 Optimal Niss-HTR Paths* nor *Optimal Niss-HTR Paths* says how it was made: not the sample, the solver, nor how a state with several optimal finishes counts. I tried three ways a program could count paths and compared every cell (every path listed in every tab) with what each gives on 5,000 states per subset × edges (seed 11):

| Sheet | How a state counts a path | Paths | Mean difference (points) | Correlation | Paths within 5 points |
|---|---|---|---|---|---|
| Optimal Niss-HTR Paths | every optimal finish, read only where its HTR is shortest | 7007 | 0.8 | 0.965 | 97.2% |
| Optimal Niss-HTR Paths | every optimal finish, every NISS reading | 7007 | 4.4 | 0.816 | 76.7% |
| Optimal Niss-HTR Paths | every optimal finish, linear readings only | 7007 | 2.5 | 0.455 | 88.6% |
| Sub-13 Optimal Niss-HTR Paths | every optimal finish, read only where its HTR is shortest | 768 | 3.4 | 0.907 | 79.2% |
| Sub-13 Optimal Niss-HTR Paths | every optimal finish, every NISS reading | 768 | 11.4 | 0.718 | 51.6% |
| Sub-13 Optimal Niss-HTR Paths | every optimal finish, linear readings only | 768 | 8.5 | 0.305 | 65.6% |

The first rule reproduces both sheets, the full one to 0.8 points on average (correlation 0.965), the sub-13 one less well (3.4 points, 0.907): each optimal finish of a state is read only at its readings with the shortest HTR among that finish's readings, and every distinct path among those counts once for the state. That is why the shares don't add up, as deven said ([12 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1537114175900483705)): a state with five optimal finishes can put a share on five paths. Counting every reading gives far too many paths; counting only linear readings misses the switches. The sub-13 sheet is the same count over states with an optimal of 12 or less (its unlabelled number in each tab matches the share of such states), on fewer states per tab, so its cells are noisier. Two details: the sheets' 0c0 0e tab holds HTR states only (its top row is the empty path, at 96%), while 0c0 0e as a subset is half HTR and half U D' times HTR; and the paths include edge counts, which my route names drop.

What that means for reading them: a share in the sheets says how often the path carries an optimal whose own shortest HTR is used. It is not how often trying the route finds the optimal (a route can find an optimal through a longer HTR than that finish's shortest), and the shares of different paths overlap. The checklists of section 4 count the second thing, in an order where the shares add up. The top path of each tab and my share for it are in appendix A; the top path of the full sheet is the first route of my budget-2 checklist on 45 of 48 subset × edges.

**Levi Gibson's *allcases*.** Its paths are linear chains in Jay's qt names, one path per state; the shares add to 1 per subset. Asked whether ties between optimal solutions were factored in, the answer was "Not factored in" ([13 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1295060590074531922)). One leave-slice optimal per state, chosen at random among the optimal finishes (5,000 states per subset × edges, seed 7), reproduces it: mean difference 0.3 points over 1,895 paths, correlation 0.991 (with the E slice solved: 0.6 and 0.974). Its shares are therefore *the path of one optimal found by a solver*, a third reading between *some optimal* and *every optimal*. Where the sheet and the random pick differ, the sheet has the fewer-qt path more often: on 4b2 4e its 2qt rows add to 39.5% against 33.5% for a random pick, on 4a1 4e its 5qt rows to 6.1% against 9.6%, more than the 5,000-state sample explains; so the solver behind it probably preferred fewer quarter turns among equal-length finishes.

**2qt(a) and 2qt(b).** The old names say "2qt(a)" and "2qt(b)" where today's say 4a2 and 4b2. The server worked most of this out: Tzak on *allcases*' letters, "good one, the bad one can't turn into 2c3" ([13 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1295059271746326699)); its author, "And yes, a and b are swapped in line with the old naming scheme", "a is the R U2 R’ case" ([8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315360877255327785), [8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315360910327414835)); Zagros, "I think a and b might be flipped" ([8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315341879910600775)). What the sheets themselves show:

- Aedan Bryant's *HTR Subset Stats* lists a trigger for every case. Played on a cube, its "2qt (a)" triggers are 4b2 0e, 4b2 2e and 4b2 4e (`U R2 U` is 2qt (a) 4C2E), and its "2qt (b)" ones are 4a2.
- *allcases* has no triggers, but its own data settles it: its "2qt(a)" rows go to a "3qt 2c" case with one qt (30 rows do), none of its 113 "2qt(b)" rows does, and only 4b2 can reach 2c3 with one quarter turn. So 2qt(a) is 4b2 there too, as its author and Tzak said.
- The *Extra Quarter-Turn Stats* sheet has the letters the other way round: its own example triggers put "2qt(b)" on 4b2. That one is new here.

So mrauo's "Only 1/3 of 2q 4b2e cases use 2qt for optimal wtf" ([8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315341544206631054)) read the *allcases* row "2qt(b) 4c2e", which is 4a2 2e. Zagros answered "I think a and b might be flipped" and "Should be 60%" ([8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315341879910600775), [8 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1315341893856657430)), which is right: with one optimal at random, the 4b2 2e path is 2qt on 53.7% of states, 4a2 2e on 27.7%.

**Aedan Bryant's *HTR Subset Stats*** (1,000 states per subset): the mean optimal and the mean NISS HTR are within 0.06 of mine on 39 of its 47 rows. Of the others, four are rows the sheet carries with the numbers of another row (4qt 4E has 4qt 2E's numbers, 4qt 4C2E 4qt 4C's, 5qt 2C 4qt 4C4E's, 5qt 4C 5qt 2C8E's: a copy slip), and the two fake-HTR rows are off by 0.74 (0c3 0e) and 0.56 (0c4 0e) in the mean optimal: the sheet's states were built around one trigger ("25 random move HTR scramble + trigger + 25 random move HTR scramble", [29 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069288666981220492)), which for these two covers only part of the subset. The remaining two differ by at most 0.08. Its "Linear HTR" is the normal side only, not the better of the two (4b2 2e: sheet 6.213, normal side 6.156, better side 5.654). Its "No E Difference" column already said that solving the slice costs well under a move for most subsets.

**Levi Gibson's *Extra Quarter-Turn Stats*.** Its "% with extra qts" is *every leave-slice optimal uses more qts than the corners need* ("The percentages are for if the dr CAN be solved optimally without extra qts", [29 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1301010836646531176)). On that reading it agrees with my sample on every comparable row within sampling error (its 0c0 0e row counts HTR states only, like the path sheets).

**rodneykinney's *DR Finish Move Counts*** (10,000 solutions). rodneykinney's summary "2 qt or less is 17%, but 3 qt or less is 45%" ([2 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1037387616313675806)) is right: exactly 17.6% and 45.7% over the 40,320 corner arrangements. The sheet's 4qt and 5qt shares are further off (32.9% and 22.5% against exactly 35.2% and 19.1%), more than its sample size explains, so its DRs were probably not uniform DR states; the sheet does not say how they were made. Its extra-qt columns use one optimal per state and fall between my fewest-qt and most-qt readings.

**Joba's and DougCube's exact tables** are reproduced exactly: the optimal distribution of every subset (473 cells of subset and length), the shortest DR-to-HTR length per subset, and the 663,552 HTR states with mean 10.13432557.

---

## 6. Shortest HTR against the optimal

**Linear against NISS.** The shortest HTR per subset: with NISS (moves on both sides counted), linear on the better side, and on the normal side alone (what Aedan Bryant's sheet calls linear), and how often NISS is shorter. Sampled, 25,000 per subset × edges:

| Subset | Shortest NISS HTR | Shortest linear, better side | Normal side | NISS = linear | NISS 1 shorter | NISS 2+ shorter |
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

So for rodneykinney's question ([30 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069660273356587082)): NISS saves nothing on about half of all DRs, one move on a third, two or more on 11.9%; on 0c3 and 0c4 (fake HTR corners) it saves two or more on 52.4% and 40.5%. The two linear sides tie on 36.9% of DRs and differ by two or more on 16.9%.

**Which HTR the optimal uses.** For each DR, the shortest HTR among all readings of all its optimal finishes, against the DR's shortest NISS HTR (sampled, 25,000 per subset × edges, edges pooled by size; optimal finishes, NISS readings):

| Subset | Shortest HTR | +1 | +2 | +3 or more | Every optimal needs 9+ | … though a sub-9 HTR exists | Post-HTR moves |
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

Some optimal goes through a shortest HTR on only a third of DRs; on two thirds you have to find an HTR at least a move longer than the shortest to get the optimal, and on 35.3% at least two longer. That is the reason the checklists need budget 2 (section 4). On 0c3 a shortest HTR is used most often (53.5%), on 2c4 and 4b5 about as often as on 4b2. *Post-HTR moves* is the rest of that optimal: 4.59 moves on average, more on low-qt subsets, as tseitsei89 described ([29 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1466457851286524068)).

**Nine-move HTRs.** On 65.2% of all DRs every optimal finish needs an HTR of 9 moves or more in every reading; on 29.7% of DRs that is so although the DR has an HTR of 8 or less. By the length L of a DR's shortest NISS HTR, the share of DRs where some optimal uses an HTR of exactly L moves (all DRs, sampled; the rows cover 99.2% of DRs, the rest having a shortest NISS HTR of 3, 11 or 0 to 2):

| Shortest NISS HTR (L) | Share of DRs | An optimal uses an L-move HTR |
|---|---|---|
| 4 | 1.1% | 44.6% |
| 5 | 4.5% | 35.0% |
| 6 | 12.7% | 29.2% |
| 7 | 20.5% | 30.2% |
| 8 | 25.3% | 31.9% |
| 9 | 25.5% | 32.6% |
| 10 | 9.6% | 42.0% |

The chance that the shortest HTRs carry an optimal is about a third whatever their length, 6 to 9 alike. What a single 9-move HTR is worth when you have written many is a different question that this does not measure (there are many more 9-move HTRs than 6-move ones). An example where every optimal needs an HTR of 9 or more: the 2c3 2e of `U2 L2 U F2 L2 R2 U' B2 R2 U' L2 U2 B2` is 13 optimal, and the shortest HTR in any reading of any of its 2 optimal finishes is 10 moves (replayed).

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

The three readings are far apart, and the numbers quoted on the server fit different ones. rodneykinney's "57% of the time, the optimal solution uses 4QT for a 2QT corner case" ([13 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1063355084697784371)): on 4a2 and 4b2 every optimal uses 4qt or more on 53.9%, some optimal does on 80.7%, one optimal picked at random on 69.0% (leave slice 56.3%); Radek B asked which ("Did you consider all optimals or just one that you had generated?", [13 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1063365972846706728)); there is no answer in the export (rodneykinney moved on to a thread, [13 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1063499873665695819)), and 57% fits a random leave-slice optimal or *every optimal*. Lichi Fang's "over 60% the optimal solution for htr subset 2qt(a) 4c4e … use 4qt rather than 2qt" ([6 Aug 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1137835695721939094)) was read off the first optimal nissy gave ("these are just the first solution nissy gave for optimal", Aedan Bryant, [6 Aug 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1137864582036209824)); on 4b2 4e one optimal at random uses 4qt on 77.6%, every optimal on 63.7%. Both fit.

On 4b2 4e, where no optimal uses only 2 qts (63.7% of states), the 2qt route never gives the optimal: the 4b2 4e of `F2 D F2 D L2 D2 L2 F2 L2 D L2 U` is 12 optimal and no optimal finish follows the 2qt route `4b2 > 4a1 > 0c0` in any reading (both of its 2 optimal finishes, `U' L2 D' L2 F2 L2 D2 L2 D' F2 D' F2` and the other, re-read on the sticker model at every split).

**Half turns before the first qt.** Kai Cui's 2c3 2e stats ([5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457432898633840): "baically 85 percent chance that you dont need to check 2 ht before first qt"): some optimal starts its first qt after 0 or 1 half turns on one of the two sides on 82.7%, on the normal side alone 62.0%. Over all DRs: 92.0% and 76.4%.

**The last DR move.** With the last move either way (the better of X and X·R2; sampled, 25,000 per subset × edges, edges pooled by size; optimal lengths from the exact table):

| Subset | Mean optimal | Last move either way | One shorter | Same | Optimal 15+ | 15+ either way |
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

X·R2 is one move shorter on a third of DRs and never more than one shorter, in every subset alike; the first study had this exactly (*A third of the time the other DR is one shorter*). Yura Riabov's estimate in 2024 was 1/6 of a move ("so yeah, should be 1/6", [6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248337792673779803)), from "2/3(chance of dr solution ending in 1 of 4 moves) * 1/4(chance of that move being the right one)"; Yura called it "very rough" and added "i doubt it will be more than a half move difference with 1 move inverted" ([6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248372741602545674)). The half-move ceiling holds; the 1/6 is half the real gain of 0.325. Example: think of `R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U` as the end of a DR on U/D whose last move was a quarter turn of R; turning that move the other way is the same as adding R2 at the end. As written it is 13 optimal; with R2 added, `R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U R2`, it is 12 (`B2 U' R2 L2 D L2 U L2 U2 R2 U' F2`, replayed).

For routes, the variation changes nothing in kind: every route's share rises by about the same amount, and no checklist gains a route. It is worth its 0.32 moves on every subset, so write both finishes' DRs down, but don't let it change which routes you try.

Aedan Bryant's sheet has a "qt break" column; Yura Riabov explained it as "you know that qt break is dr plus one move that can be inverted, right?" ([25 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1376198140943929415)). One extra move that can go either way costs 0.68 moves over the plain optimal on average, which is the "around 0.5 worse, rather than 1 as you might expect" trangium described ([6 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1469487095407186093)), a little more.

---

## 8. DR bounding

The method of Levi Gibson's *DR Bounding* doc: "1. Find many reductions to the 1qt 4c4e subset … 2. For each case, create a lower bound of how good the solution can be … 3. Start checking the 1qt cases from best to worst … 4. Once you find a solution, cross off all the 1QT cases that can not be solved in less moves than the solution you found." rodneykinney's *Advanced DR Bounding* sharpens the bounds and adds 2qt. Here I measure the method's ceiling: if you write every reduction to 1q of at most R moves (on normal, on inverse, or split between them, section 3) and finish each reduced state optimally, with however many quarter turns that takes, how often is one of them the optimal finish of the DR, and how many reductions is that? The search over reductions is exact; reductions are counted as a solver writes them (each side's sequence empty or ending in a quarter turn), exactly by table. Sampled: the first 4,000 states per subset × edges; shares have standard errors of at most 0.5 points per corner subset.

| Subset | R ≤ 3: optimal / reductions | R ≤ 4 | R ≤ 5 | R ≤ 6 | R ≤ 7 (optimal only) | Within +1, R ≤ 4 | 12 or better, R ≤ 5 | 2q, R ≤ 3 |
|---|---|---|---|---|---|---|---|---|
| 0c0 | 86.0% / 156 | 91.5% / 1,238 | 93.9% / 8,763 | 96.9% / 63,868 | 99.1% | 98.9% | 51.0% | >99.9% / 384 |
| 2c5 | 0% / 0 | 0% / 0 | 0% / 0 | 10.9% / 237 | 45.8% | 0% | 0% | 0% / 0 |
| 2c4 | 0% / 0 | 3.5% / 11 | 25.7% / 228 | 59.5% / 2,503 | 84.6% | 8.5% | 3.7% | 46.5% / 71 |
| 0c3 | 12.7% / 5 | 35.0% / 38 | 65.5% / 399 | 81.7% / 3,628 | 85.3% | 52.1% | 2.6% | 98.4% / 101 |
| 4a2 | 64.3% / 26 | 76.6% / 207 | 80.0% / 1,463 | 85.2% / 10,942 | 92.3% | 93.6% | 15.9% | >99.9% / 181 |
| 4a1 | 62.3% / 80 | 75.6% / 623 | 88.6% / 4,901 | 95.4% / 36,474 | 98.0% | 89.2% | 43.6% | 98.9% / 304 |
| 2c3 | 20.5% / 16 | 48.1% / 140 | 71.1% / 1,080 | 86.2% / 9,111 | 94.2% | 78.8% | 21.1% | 95.7% / 152 |
| 0c4 | 0% / 0 | 10.2% / 22 | 37.0% / 330 | 63.5% / 3,075 | 84.3% | 19.0% | 3.4% | 77.9% / 123 |
| 4c3 | 15.7% / 8 | 37.5% / 66 | 60.1% / 559 | 75.1% / 4,959 | 86.8% | 66.1% | 8.4% | 93.4% / 102 |
| 4c4 | 0% / 0 | 3.7% / 6 | 17.6% / 83 | 38.8% / 800 | 58.2% | 6.4% | 0.59% | 41.6% / 36 |
| 4b2 | 43.7% / 26 | 58.0% / 233 | 74.1% / 1,978 | 88.8% / 16,087 | 97.6% | 84.5% | 28.0% | >99.9% / 248 |
| 4b5 | 0% / 0 | 0% / 0 | 0% / 0 | 10.3% / 229 | 48.1% | 0% | 0% | 0% / 0 |
| all DRs | 14.1% / 10 | 24.9% / 89 | 40.6% / 748 | 59.3% / 6,242 | 78.3% | 38.5% | 10.3% | 60.4% / 102 |

Each cell: share of DRs where some reduction of at most R moves leads to an optimal finish / mean number of reductions of at most R moves. Counts for R = 7 are not reported: the table that counts them was checked against brute force only up to 5 moves on every subset and up to 7 on 40 states of 0c0, so for R ≤ 7 the table gives the share only (that comes from the exact search). The last three columns: a finish within +1 with reductions of at most 4; a finish of 12 or better with reductions of at most 5 (for DRs that have one); reductions to 2q of at most 3 moves.

What it says:

- **Which subsets suit it depends on R.** With reductions of at most 4, bounding finds the optimal on 91.5% of 0c0, 76.6% of 4a2, 75.6% of 4a1, 58.0% of 4b2 and 48.1% of 2c3; at most 6 puts 4a1 (95.4%) and 4b2 (88.8%) ahead of 4a2 (85.2%). On 2c5 and 4b5 no reduction of 5 or less reaches 4a1 4e at all (it takes at least 6), and 4c4 and 2c4 are close to that.
- **Each extra move of reduction costs a lot**: the number of reductions grows 7.3 to 11.0 times from 5 to 6 moves. Over all DRs it is 89 reductions on average at most 4, 748 at most 5, 6,242 at most 6. With the bounds doing their job you finish only a few of them, but you still write them, and NISS-trace them.
- **2q needs much shorter reductions**: at most 3 moves to a 2q state reaches the optimal on 60.4% of all DRs, against 14.1% for 1q. But each 2q state still needs its own finish found by hand, which is the hard part bounding at 1q avoids.
- **Within +1** is much easier: at most 4 moves gives a finish within +1 on 38.5% of DRs.
- **The one-quarter-turn reading** (the reduction, then a finish with exactly one quarter turn, which is what JTuu's simulation counted) finds less: on 2c3 39.8% at R ≤ 4 against 48.1%, on 4b2 42.4% against 58.0%.

**Against the checklists.** For the question I was asked (how often bounding finds the optimal per subset, and how many reductions that takes): the smallest R for which bounding finds the optimal on 80% of a subset, with the reductions that is, against how many routes the checklist of section 4 needs for 80%:

| Subset | Bounding: R for 80% (reductions) | Checklist classes for 80%, budget 2 | Checklist classes, no HTR limit |
|---|---|---|---|
| 0c0 | 3 (156) | more than 8 (69.4% at 8) | 2 |
| 2c5 | more than 7 (45.8% at 7) | 2 | 1 |
| 2c4 | 7 (count not reported) | 2 | 1 |
| 0c3 | 6 (3,628) | 2 | 2 |
| 4a2 | 5 (1,463) | 5 | 3 |
| 4a1 | 5 (4,901) | more than 8 (74.6% at 8) | 2 |
| 2c3 | 6 (9,111) | 5 | 1 |
| 0c4 | 7 (count not reported) | 1 | 1 |
| 4c3 | 7 (count not reported) | 5 | 2 |
| 4c4 | more than 7 (58.2% at 7) | 4 | 2 |
| 4b2 | 6 (16,087) | more than 8 (75.0% at 8) | 2 |
| 4b5 | more than 7 (48.1% at 7) | 2 | 1 |

Bounding gets to 80% with short reductions on 0c0 (3), 4a2 and 4a1 (5), where the budget-2 checklist struggles (0c0 and 4a1 stop short of 80% after eight routes); on 4b2 it needs every reduction up to 6, about 16,087 of them, where the checklist stops at 75.0%. On 2c4, 2c5, 4b5, 0c3, 0c4, 4c3 and 4c4 one to five routes reach 80%, and bounding needs 6 or 7 moves of reduction or does not get there by 7. A route and a reduction are not the same amount of work, so the comparison is only in kind. **For a human the bounding column is mostly out of reach**: each extra move of reduction multiplies the reductions by about eight, and a solver in an attempt writes tens, perhaps a couple of hundred (R ≤ 4 is about 89 on average). So only the 0c0 entry (R = 3, about 156 reductions) is a practical recommendation; every entry with R of 5 or more, thousands of reductions, is **computer only**, there to show where the optimal lies, not how to find it. The R ≤ 4 column of section 8 is the one to plan an attempt with.

**Levi Gibson's verdicts per subset.** After "lots and lots of solves" ([8 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1370092390362382348)): "0c0: Yes", "4a2: yes yes yes amazing muah chief's kiss", for 4a1 "if you get a 4a1 case randomly, bound it. Otherwise it's not great. For the 2e/6e case it's not great because you 99% of the time you want to find a 0c0 or 4b2 trigger", for 4b2 "just check the really short ones, and then just try triggers for the rest", for 2c3 "I only use it for the 6e subset now. Triggers will get you optimal usually for 2e and 4e", and "Bounding is actually REALLY good for 4c3". Row by row, bounding with every reduction of at most 4 and 5 moves against the first three and five budget-2 routes (4,000 states per subset × edges for bounding, 25,000 for the routes):

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

- **0c0: agrees**, bounding is far ahead on every edge count.
- **4a2: agrees on 0e**, where bounding finds 76.9% against 44.4%; the routes are a little ahead on 2e and level on 4e.
- **4a1: agrees**: on 4a1 4e (the case Levi Gibson would bound) bounding finds nearly every optimal; on 0e and 2e the routes are as good or better.
- **4b2: partly**: on 4b2 0e and 2e bounding with reductions of 4 already beats three routes, so more than the really short reductions is worth writing; on 4b2 4e the routes are ahead.
- **2c3: agrees for 2e and 4e** (routes ahead), **not for 6e**, where the routes are ahead too.
- **4c3: does not agree**: the routes are ahead on every edge count, by 12.8 points or more against reductions of 5. Levi Gibson's reason was the b side ("On the b corners side there are sooooo many finecky ways to reduce to 4a1 in very few moves"); these numbers count both sides together.

**Levi Gibson's 75 to 80%.** Asked how many reductions to check, Levi Gibson wrote "I like to check all sub-5 reductions. This can be done super quick and gets optimal like 75% of the time, and it gets optimal +1 the rest of the time" ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311670582601060354)), "sub-5" being "4 or less" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051485760163880)); and later, asked "Would it be around 80 percent?" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051034906038323)): "yeah something like that I'd guess" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051081831780434)), "for 2c3 that is" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051112253329439)), adding "The only thing it really misses is a bunch of half turns into a 5-move trigger, so check that in addition to bounding" ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051209158525018)). On 2c3, every reduction of at most 4 finds the optimal on 48.1% (52.1% of 2c3 2e; 140 reductions on average), a finish within +1 on 78.8%; at most 5, 71.1%. Of the subsets Levi Gibson named as the ones for full bounding ("I don't use it fully for any subsets other than 4a2 and 2c3", [28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311671487379279872)), 4a2 gets 76.6%. So for 2c3 both halves are off for bounding alone: the optimal comes from a reduction of 4 or less on under half of 2c3, and on 21.2% not even +1 does. Levi Gibson does add the triggers ("For 2c3 2e and 4e I do full DR Bounding + checking the 5-move triggers, and that seems to catch everything", [28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311674286389334026)); that combination is not measured here. Example in the errata (a 2c3 2e where the best any reduction of at most 4 gives is +2).

**JTuu's simulation** for Kai Cui's question ([3 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313597166270550137)), 2,000 2c3 2e states with Tzak's definitions: "4 move reduction to 4c4e just means you can strip off <=4 moves total from either end and be left with a single qt" ([3 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313620671607345254)) and "7 move linear htr means if you drop 7 moves on either end, are you left with just half turns" ([3 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313620835046789282)). That is the one-quarter-turn reading. JTuu's result ([4 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313766061325156462)): linear HTR in 7 "946/2000 (47.30%)", 4a1 in 4 "1071/2000 (53.55%)", both together "1293/2000 (64.65%)", and with 8 and 5 "1721/2000 (86.05%)". On uniform 2c3 2e states, same definitions, I get 38.1% for linear HTRs of at most 7, 44.7% for reductions of at most 4, 55.3% together, and 80.3% with 8 and 5. Every number is 5.8 to 9.4 points lower than JTuu's, far more than the standard error of 2,000 states (about 1.1 points). JTuu did not say how the states were drawn. Two things in Kai Cui's generator would explain a gap: its states are random half turns around one trigger ("(random ht 100-110) (U R2 U R2 U) (random ht 100-110)", [5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457154635665448)), not a uniform 2c3 2e, and it allowed the last DR move to be inverted ("this accounts for inverting last move of dr", [5 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1303457154635665448)). I can't reproduce it exactly. The order of the four options is the same in both.

---

## 9. FakeMMAP's reduction-length bound

**What was proposed.** FakeMMAP ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531394667773962)): "Let's say we're looking for a finish in M moves (or less), assuming we're only allowed to use N>1 qts. We want to know how long our reductions to 1q should be, in order to find that solution. Let R be the biggest possible length of a reduction to 1q you have to check". The inputs are A and B, the optimal HTR on normal and on inverse, C, "the shortest possible HTR in the subset" ("so 2c3 2e would have C=5, 4b2 0e would have C=6"), and section bounds: "Numbering these sections from 0 to N, let \alpha_i be the bound for the ith section. For example 4a3 2e would have \alpha_1=3, because you have to to the 4b2 parity fix." Then ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369)) "R is the max of the following", five families of terms over sets S of consecutive windows, solved "with Fourier-Motzkin elimination by hand"; and ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475)) "multi-qt DR bounding... well, sort of": lower bounds on M once every reduction shorter than R' has failed. Of the lower bounds FakeMMAP added "I don't know how useful these bounds really are, I have to put in the numbers to see if there are situations where the typical bound is M \geq 11, rather than M \geq 7 lol." ([8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533429198553178)). This section puts in the numbers, for the upper bound R as well.

**How I tested it.** A finish with N quarter turns has N + 1 sections of half turns, s_0 … s_N, each at least α_i; the 1q reduction that keeps quarter turn q with its two neighbouring sections has length (finish length) − 1 − s_{q−1} − s_q. I computed α_i for every corner path that occurs (fewest half turns section i needs over every corner arrangement following the path; for 4a3 > 4b2 > 4a1 > HTR it gives 0,3,1,0, FakeMMAP's α_1 = 3; this study's Lean certificate re-derives every α (appendix B)). Then, for every sampled state, every corner path of its optimal (or +1, or ≤ 10, 11, 12) finishes, and the shortest reduction such a finish needs, I compared that need with R three ways: the formula of [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369) as written; the same without its first term; and the exact optimum of the same linear model (the largest shortest-reduction any section lengths allowed by the constraints can force), solved by enumeration instead of by hand.

| Target | (state, path) cases | R as written | Without term 1 | Exact model | Needed: mean / largest | R too short: as written / exact model with linear C |
|---|---|---|---|---|---|---|
| optimal | 1,914,809 | 12.1 | 11.1 | 8.9 | 7.0 / 14 | 0% / 0.073% |
| optimal + 1 | 5,973,495 | 13.6 | 12.8 | 10.4 | 8.2 / 15 | 0% / 0.002% |
| 10 or better | 25,283 | 8.5 | 7.6 | 5.1 | 3.8 / 8 | 0% / 1.1% |
| 11 or better | 87,631 | 9.5 | 8.6 | 6.3 | 4.5 / 9 | 0% / 1.1% |
| 12 or better | 322,330 | 10.6 | 9.7 | 7.1 | 5.3 / 9 | 0% / 0.20% |

Each row: the number of (state, path) cases, the mean R with the corner path known, from the formula as written, without term 1 and from the exact model, the reduction the finishes actually needed (mean / largest), and how often R was too short. Sampled, 25,000 states per subset × edges.

**(a) It is sufficient.** As written, R was never shorter than what a finish needed, in any case, at any target. The derivation does need C to bound every HTR you can reach with a switch in the middle, which makes C the shortest NISS HTR, not the shortest linear one. FakeMMAP's examples (C = 5 for 2c3 2e) are linear minimums, and NISS HTRs go below them: on 2c3 2e as low as 4 (tseitsei89: "NISS HTR can be as low as 4 moves", [12 Oct 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1426927777722142895)). With the linear C the exact model is too short on 0.073% of cases at the optimum (1.1% when hunting a 10). Example: the 0c0 2e of `F2 U' B2 R2 B2 U R2` is 7 optimal through a NISS HTR of 4 moves, below the subset's linear minimum of 5 (replayed). The formula as written survives this because it is loose; with C the shortest NISS HTR the exact model is never too short either.

**(b) It does not prune at the reduction lengths solvers write.** At the optimum, with the corner path known, R averages 12.1 as written, 11.1 without term 1 and 8.9 in the exact model, where the finishes needed 7.0 on average and 14 at most. Not knowing which corner path the optimal takes (worst case over the subset's paths, with the DR's own A and B), R averages 12.7 as written, 12.4 without term 1 and 10.6 exactly, against a longest need per subset × edges of 11.2 on average: the formula lets you skip nothing compared with checking every reduction up to that longest need, the exact model next to nothing. Hunting a fixed M is the same story: for 12 or better, path unknown, R is 11.2 as written, 11.0 without term 1 and 9.0 exactly; the longest need per subset × edges averages 8.5 and is 9 at most. Solvers check reductions of 4 to 6 moves (section 8), and a bound that says *go to 9 or 10* never tells you to stop earlier than that. Where the bound could help is the other direction, proving that a short M is impossible, and that is (c).

**rodneykinney's tables.** rodneykinney asked for "some tables for specific cases" ([9 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491873063531188324)). Per subset × edges and target M = 10, 11, 12: R when nothing is read off the DR (A and B set to the subset's shortest linear HTR, worst case over the subset's corner paths), from the formula without term 1 (C the subset's shortest linear HTR, as FakeMMAP defined it) and from the exact model (C the shortest NISS HTR), and the longest reduction any sampled finish of that length needed. The M = 12 column for a few subsets (all in appendix A):

| Subset | Formula / exact / needed, M = 12 |
|---|---|
| 2c3 2e | 11 / 9 / 8 |
| 4b2 4e | 11 / 9 / 9 |
| 4c3 2e | 11 / 9 / 8 |
| 4a2 2e | 10 / 9 / 9 |
| 2c4 4e | 10 / 9 / 9 |

**(c) The multi-qt lower bounds, and one index.** The first bound of [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475) is M ≥ (|S|(R'+1) − N + Σ α_i) / (|S| − 1), the sum "over all i's such that i, i+1 are both in S" (as in [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369)). Windows i and i+1 share section i+1, so the section that is counted twice is α_{i+1}, not α_i. As written, the bounds are wrong in 923 of 1,914,809 cases at the optimum (subsets 0c4, 4b2, 4c3, 4c4): 904 times this first bound and 19 times the one with B. With α_{i+1} they hold in every case, and R stays sufficient. Example, replayed: the 0c4 0e of `D2 F2 L2 U' B2 U' L2 U2 B2 U' L2 D R2 D2` is 14 optimal by `D2 R2 D' L2 U B2 U2 L2 U B2 U L2 F2 D2`, path 0c4 > 4a3 > 4b2 > 4a1 > HTR (N = 4), α = 0, 1, 3, 1, 0. Its sections are 2, 1, 3, 1, 3 and its 1q reductions 10, 9, 9, 9 moves, so every reduction shorter than R' = 9 fails. With S = {0, 2, 3} the bound as written adds α_2 = 3 and gives M ≥ 14.5, so 15, but the finish is 14; with α_3 = 1 it gives 13.5, so 14. I take the shared section to be what was meant.

**The typical bound, FakeMMAP's question.** At the optimum, for every (state, corner path) with at least two quarter turns, take R' as the shortest 1q reduction a finish of that path needs (so every shorter reduction has failed) and compute the corrected bounds, next to the "very stupid bounds" M ≥ A + α_N, M ≥ B + α_0 and the optimum itself (sampled, 25,000 per subset × edges; each corner subset's rows count every (state, path) case):

| Subset | (state, path) cases | Lower bound: median / mean | Trivial bound: median / mean | Mean optimum | Bound above trivial | Bound reaches the optimum | Bound 11 or more |
|---|---|---|---|---|---|---|---|
| 0c0 | 183,502 | 8 / 7.99 | 6 / 6.01 | 12.44 | 72.5% | 0.73% | 14.8% |
| 2c5 | 181,404 | 12 / 12.03 | 11 / 10.91 | 14.61 | 64.7% | 3.0% | 85.2% |
| 2c4 | 195,143 | 11 / 11.00 | 9 / 9.37 | 13.92 | 73.8% | 2.7% | 61.3% |
| 0c3 | 182,652 | 13 / 12.49 | 11 / 10.93 | 14.55 | 72.4% | 7.6% | 88.5% |
| 4a2 | 137,305 | 12 / 11.57 | 10 / 10.03 | 13.85 | 78.9% | 6.2% | 76.3% |
| 4a1 | 129,339 | 10 / 9.79 | 8 / 7.73 | 12.96 | 80.5% | 4.1% | 38.1% |
| 2c3 | 226,253 | 11 / 10.46 | 9 / 8.64 | 13.44 | 78.6% | 3.5% | 51.0% |
| 0c4 | 169,721 | 11 / 11.17 | 10 / 9.89 | 13.84 | 69.5% | 2.7% | 72.6% |
| 4c3 | 120,789 | 11 / 11.06 | 9 / 9.30 | 13.68 | 81.4% | 5.1% | 61.8% |
| 4c4 | 129,413 | 12 / 12.32 | 11 / 11.14 | 14.69 | 70.5% | 7.3% | 92.1% |
| 4b2 | 136,970 | 10 / 9.78 | 8 / 7.55 | 13.05 | 83.7% | 1.8% | 40.7% |
| 4b5 | 122,318 | 12 / 11.72 | 10 / 10.05 | 14.52 | 77.5% | 2.6% | 78.6% |

So FakeMMAP's hope comes true on most subsets: on a typical path the corrected bound is M ≥ 11 on 2c3, 2c4, 0c4 and 4c3, 12 on 4a2, 4c4, 2c5 and 4b5, 13 on 0c3, 10 on 4a1 and 4b2 and 8 on 0c0, one or two above the trivial bound, and it is 11 or more on 51.0% of 2c3 paths. It stays two to four below the mean optimum, though, and reaches the optimum itself on at most 8% of a subset's cases: it tells you when to stop writing longer reductions only if you are hunting a finish well below the optimum. (With α_i as written the bounds beat the trivial one in 75.3% of cases, size-weighted over all subsets.)

---

## 10. Hand checklists, graded

Each checklist is translated into route classes as closely as the route names allow and graded on the same sample: the share of DRs where its steps so far find an optimal finish, and a finish within +1, with HTRs at most two over the shortest (budget 2), and with no HTR limit. Steps that depend on how many setup moves come before a trigger are graded as their whole route class, which flatters them a little. Sampled, 25,000 per subset × edges.

**Zagros's 4b2 order** ([29 Dec 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1455301984415514719)): "1. check shortest HTR on normal by settings up to triggers and reasonable extensions", "2. check more linear 2qt HTRs by just reducing to 4a1 and doing the HTR even if it's long", and on to "8. if it is seriously my only DR and I have nothing, try 2+2 HTRs". Steps 1 and 2 are graded together, 6 (the inverse) and 7 are inside the others since both sides are always graded:

| Step | What | Optimal (budget 2) | Within +1 (budget 2) | Optimal, no HTR limit |
|---|---|---|---|---|
| 1 | S1+S2 linear 2qt 4b2 > 4a1 > HTR (normal or inverse) | 37.6% | 67.2% | 45.0% |
| 2 | S3 linear 4qt HTR of <= 8 moves | 45.4% | 75.7% | 54.3% |
| 3 | S4 reduce to 4a1, switch (4b2 > 4a1 > (HTR)) | 50.8% | 80.8% | 54.3% |
| 4 | S5 regress to 2c3, switch (4b2 > 2c3 > (...)) | 64.2% | 90.4% | 95.5% |
| 5 | S8 2+2: any 4qt route switching after the 2nd qt | 71.3% | 93.4% | >99.9% |

Zagros: "if I simply follow the system I have in my mind for each subset without getting distracted then it just produces optimal in 15 minutes like 80% of the time" ([29 Dec 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1455302363953758427)). Done fully on 4b2 with near-shortest HTRs it finds the optimal on 71.3% and +1 on 93.4%; with HTRs of any length every 4b2 is covered. Zagros's 80% is about real attempts, where time is the limit, so it can't be checked here, but nothing in the numbers contradicts it. After the first, the step that adds the most is table step 4 (Zagros's step 5, the regression to 2c3), 13.4 points.

**4b2 4e: regress to 2c3 first, or reduce to 1q first?** Yura Riabov ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258421085251178608), [4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258421209075417138), [4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258421267917312132)): "4b2 4e is basically the best 4q subset", go to 2c3 "if it's not 1-2 moves to trigger", "i also try 2-3 moves to 4a1 and niss trace if i don't forget to do that". rogo asked whether it shouldn't be the other way round ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258442750953525399)): "the first approach apart from R U2 F2 R to check should still be 'reduce to 1qt 4e and niss trace for short htrs' i think?"; Adri agreed that the label was the confusing part ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258454166830055454)): "I agree that's why calling it the best 4qt subset seems confusing". Jay ([4 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1258586844883451964)): "if you think of this subset as one where you only try to solve with U R2 F2 U, you're gonna miss optimal the vast majority of the time". Yura Riabov's order (the first step as a trigger with at most two setup moves, the setup limit being Yura's "1-2 moves"):

| Step | What | Optimal (budget 2) | Within +1 (budget 2) | Optimal, no HTR limit |
|---|---|---|---|---|
| 1 | S1 linear 2qt trigger with <= 2 setup moves (HTR <= 6) | 8.6% | 16.1% | 8.6% |
| 2 | S2 regress to 2c3 (2e or 4e), then 2c3 linear or switch (4qt) | 62.3% | 88.4% | 82.2% |
| 3 | S3 reduce to 4a1 and switch | 72.9% | 94.0% | 93.1% |

The other start, reducing to 1q and NISS-tracing, is DR bounding: on 4b2 4e every reduction to 1q of at most 3, 4 and 5 moves finds the optimal on 40.4%, 52.5% and 68.6% (4,000 states, section 8), against 62.3% for Yura Riabov's first two steps with budget-2 HTRs. So the regression to 2c3 beats every reduction up to 4 and is a little behind every reduction up to 5 (about 1,919 of them); the 4a1 switch adds 10.6 points after it. Jay is right too: the 2qt trigger alone (with at most two setup moves) finds 8.6%. On 4b2 4e every optimal uses 4 quarter turns on 63.7% of states, as Yura Riabov's [*Hitchhiker’s Guide to HTR*](https://docs.google.com/document/d/1_NMlyPh2Ifd1E0ivos-15Sp-by-KPxoOsj9JD4pJuHI) says ("it’s optimal with 4q more than half of the time"). Fanti's split ([2 Feb 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1335799386914951218), probably read off *allcases*, whose cells it matches: "40% of opt 4b2 4e solutions use 2qt, 45% regress to 2c3", "only about 8% go to 0c0 2e/4e"), read as a checklist in that order:

| Step | What | Optimal (budget 2) | Within +1 (budget 2) | Optimal, no HTR limit |
|---|---|---|---|---|
| 1 | 2qt (4b2 > 4a1 > HTR, any switch) | 35.5% | 66.0% | 36.2% |
| 2 | 4qt via 2c3 | 77.8% | 95.5% | 93.1% |
| 3 | 4qt via 4a1 > 0c0 | 80.2% | 96.3% | 97.6% |

**Lewis Isom's 4a2 0e/2e list** ([11 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1360414689019957449)): "1) Linear 2qt HTRs on both sides. This means the first qt makes 4a1 4e.", "2) Write down all the +1's and +2's to 4a1 4e, and NISS them.", then the U M2 U checks, the regression to 4c3, and to 0c3:

| Step | What | Optimal (budget 2) | Within +1 (budget 2) | Optimal, no HTR limit |
|---|---|---|---|---|
| 1 | S1 linear 2qt 4a2 > 4a1 4e > HTR | 13.3% | 36.8% | 32.4% |
| 2 | S2 reduce to 4a1 4e, switch | 32.2% | 62.2% | 32.4% |
| 3 | S3 4qt linear through 4a2 4e again (qt, slice, qt) | 37.7% | 67.9% | 73.0% |
| 4 | S4 regress to 4b3 (2e/4e), switch, 4a3 > 4b2 > 4a1 | 52.7% | 81.1% | 73.6% |
| 5 | S5 regress to 0c3, then 0c3 > 4a2 > 4a1 (linear or NISS) | 53.4% | 81.6% | 73.6% |

Levi Gibson's reply, "you don’t have to try reductions to 4a1 4e because the average optimal solution length for that path is like 17.2 to slice" for 4a2 0e ([11 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1360460016330739854)), fits: on 4a2 0e one optimal picked at random is a 2qt path on only 2.6% of states, and steps 1 and 2 together find the optimal on 32.2% of 4a2 0e and 2e pooled. After the first, the step that adds the most is step 2 (S2 reduce to 4a1 4e, switch, 18.9 points), then step 4, the 4b3 regression with the switch, which is the first route of my 4a2 0e and 2e checklists.

**Jay's and rodneykinney's 3qt 2c0e checks.** Jay counted "11 total things" to check for every two half turns followed by a quarter turn ([16 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1042617188370087988)); rodneykinney: "I would count 9 cases" ([17 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1042817953072152596)), and later "You can check just F and R2 F" ([17 Nov 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1042825807892054106)). As a route class (one qt to 4b2 4e, switch, then 4a1 and HTR, any setup) it finds the optimal on 46.3% of 2c3 0e and +1 on 81.8%; the setup counts themselves are not graded.

**Daichi's cheat sheet** ([12 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515146431542067290)), every listed route of each subset × edges together, against my checklist:

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

The last two columns are my first three budget-2 routes and how many of my routes it takes to match the sheet. The sheet is ahead of my first three on 4b2, 4a1, 2c3 0e and 8e and 0c0 2e to 6e (where it lists several routes), about level on 2c4 0e to 6e, 4a2 2e and 0c4 2e, and behind on the rest: all of 2c5, 0c3, 4c3, 4c4 and 4b5, 0c4 except 2e, 4a2 0e and 4e, 2c3 2e to 6e, 2c4 8e, 0c0 0e and 8e. Daichi built it from sub-13 states only, so its routes favour the short finishes, which is what you want in an attempt.

---

## 11. The claims, checked

Statements the numbers can settle, by theme. Questions and guesses are in section 2, not here, unless a number was given. Each verdict is one of **True**, **Corrected**, **Depends** (true under one reading, not another), **Open** (not settled here) and **Withdrawn** (taken back at the time). Shares are on the sample (25,000 per subset × edges) unless marked exact. Every correction has an example in the errata.

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
| "so yeah, should be 1/6" (mean gain from inverting the last DR move), "very rough" | Yura Riabov [6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248337792673779803), [6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248372741602545674) | **Corrected**: 0.325 move, about 1/3 [a]. Yura's ceiling, "i doubt it will be more than a half move difference with 1 move inverted" ([6 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1248372741602545674)), is **True**. |
| "but inverting last move before dr will always reduce optimal by 1" (the 18-move states) | Yura Riabov [24 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1364979172774252674) | **True**, exact: every 18-move DR state is 17 after its last side half turn either way; torchlight's finding as Jay reported it ([28 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1355356897414348904): "i think torchlight figured out that for all those cases any of R2 L2 F2 B2 (UD oriented DR) would take the case from 18 to 17") is also true. |
| "a qt break from DR only makes it around 0.5 worse, rather than 1 as you might expect" | trangium [6 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1469487095407186093) | **True**, roughly: 0.68 on average. |

**HTR lengths** (exact over the 29,400 HTR cosets unless marked)

| Claim | Who | Verdict |
|---|---|---|
| "I figured out there's only 8 HTR" cases "where it's possible to solve it in 5 or less moves, and a further 3 that are 6 or less in their best case scenario", "one of the 6 movers is 8E with 0qt corners", "4 total cases which are potential 4 or less" | Jay [6 Oct 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1027524047174643742), [6 Oct 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1027524257296691200), [6 Oct 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1027524588101439499) | **True**, leaving out 0c0 0e (HTR already, or U D'): 8 subsets × edges at most 5, 3 more at 6 (one of them 0c0 8e), 4 at most 4. Counting 0c0 0e it is 9, 3 and 5. |
| "If you skip 4qt entirely there's only 7 cases (with my method/jacks method, with hyper parity I think there's more)" | Jay [14 Oct 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1030639402952699904) | **True**: 0c0 4a1 4a2 4b2 0c3 2c3 4c3, seven corner subsets with at most 3qt. |
| "2cxe I think it's at least worth noting if it's 0/2/4e (all 7 optimal w/o NISS) 6e (8) or 8e (9)" | Jay [2 Jan 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1191918611724505168) | **True**: shortest linear HTR 7, 7, 7, 8, 9. |
| "4qt 2C is 6 moves to HTR at best using NISS (7 without)"; "10 linearly, 6 with NISS", "for the other type of fake htr its 9 linearly and 6 with NISS" | Jay [29 May 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1112914561524314236); Lewis Isom [23 Jun 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1254409343991025766) | **True**: 2c4 0e 7/6, 0c4 0e 9/6, 0c3 0e 10/6 (linear exact, NISS the sample's minimum). |
| "Interesting that it seems 4qt 4C0E is the only HTR subset that is guaranteed 11 moves without NISS" | Jay [29 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1069455768782385294) | **Corrected**: 4c4 0e has linear HTRs of 10, and 0c4 8e is the subset that always needs 11 [b]. Lewis Isom noticed the 10 in 2024 ([23 Jan 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1199494282223038485)). |
| "No, the maximum it takes is 12 moves linearly, and 11 moves using NISS." | Lewis Isom [23 Jan 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1199490255921877022) | **Corrected**: 13 linearly on both sides and 12 with NISS occur (sample) [c]. Daichi's "0c3 4e and 4c4 0e have 13 move optimal HTR cases" ([14 May 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1504408526444040192)) is **True** (13 and 13, exact). |
| "5/6" (of HTRs that are fake) | zakimoshi [19 Sep 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1153601303801495632) | **True**, exact: 480/576 of the corner arrangements with no bad corner are fake (Lean-checked). |
| "the *expected value* is 10.13 -- the average number of moves to solve a random HTR state" | DougCube [13 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1416567970334773378) | **True**, exact over the 663,552 HTR states (half turns only). |
| "This should be it" (the share of each corner subset, in 210ths) | Daichi [6 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1391490386509172888) | **True**, exact. |
| "it's the best 2c4 case by mean number of moves to solved" (2c4 0e) | deven [7 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1513265401482707144) | **True**, exact: 13.218 against 13.531 to 14.015. |
| "2с4 is 13.5ish on average optimal, 4b2 2e is 12.5ish iirc" | Yura Riabov [25 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1476183753410744443) | **True**, exact: 13.647 and 12.611. |
| "9 moves from DR to HTR is quite a lot so usually the solution from those will also be too long to be optimal. And especially here you have so many shorter HTRs to check."; "If you have checked all shorter HTRs and you have no other DRs to check you might as well start checking 9 move HTRs." | tseitsei89 [12 Oct 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1426922640462970924), [12 Oct 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1426926451680215131) | **Open**: it is about each 9-move HTR you write, which this study does not measure. For context only: on 65.2% of DRs every optimal needs an HTR of 9 or more, on 29.7% although a shorter HTR exists (section 6). |
| "this isn't the worst practice but it's pretty rare for switching after doing more than 2 moves to actually be useful, unless you're variationmaxing" | Evan [2 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368063770576027648) | **Corrected** [d]: the shortest HTR any optimal uses needs a switch after 3 or more moves on 28.2% of DRs, and on 24.0% outside the cases Evan named ("the b side of 4c3", "4c4 and 0c4 ofc but those are pretty rare", [3 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368159205072175145), [3 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368159998848274462); all of 4c3, 4c4 and 0c4 left out): 17.9% of 2c3, 16.1% of 4b2, 24.1% of 2c4, 43.5% of 2c5. |
| "More like 3 imo"; "i almost never do this but i think it is useful"; "i really don't like switching after more than 2 moves or for badish cases, which is why i'm worse at finishes than i could be" | Yura Riabov [3 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368155824371007488), [3 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368162064148725770), [3 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1368162218579071158) | **True** for most subsets: after 4 or more moves it is 5.5% of 2c3, 4.9% of 4b2, 2.7% of 4a1, 3.5% of 0c0 (9.7% outside 4c3, 4c4 and 0c4), and large only on 0c4 (32.4%), 4c4 (30.4%) and 2c5 (23.5%). |
| "pretty sure 15 is gods number for 4a1 4e" | Levi Gibson [29 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1377633973039009822) | **Depends** on the metric: Levi Gibson's stats are leave-slice ("E Slice is not a thing in this simulation", [13 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1295060662908751912)), and the longest leave-slice optimal of a 4a1 4e is 15, exact over all 286,654,464 of them; the longest full finish (E slice solved) is 17. |

**Bounding** (sections 8 and 9)

| Claim | Who | Verdict |
|---|---|---|
| "I like to check all sub-5 reductions. This can be done super quick and gets optimal like 75% of the time, and it gets optimal +1 the rest of the time" | Levi Gibson [28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311670582601060354) | **Corrected** [e]: bounding alone with every reduction of at most 4 finds the optimal on 48.1% of 2c3 (52.1% of 2c3 2e), within +1 on 78.8%; no subset reaches 75%. Levi Gibson used it with 5-move triggers on 2c3 ([28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311674286389334026)), which this does not measure; the later "yeah something like that I'd guess" for 80% on 2c3 ([29 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1312051081831780434)) was a guess. |
| JTuu's simulation: "Findable: 1293/2000 (64.65%)" (linear 7 or bounding 4) … "Findable: 1721/2000 (86.05%)" (8 and 5) | JTuu [4 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1313766061325156462) | **Open**: same definitions, uniform states give 5.8 to 9.4 points less; the states were probably drawn differently, or with the last DR move inverted, which Kai Cui's generator did (section 8). |
| "Bounding update: after lots and lots of solves this is how I use it" (per-subset verdicts) | Levi Gibson [8 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1370092390362382348) | **Depends** on the subset: right for 0c0, 4a2 0e, 4a1 (bound 4a1 4e, not 0e/2e) and 2c3 2e/4e; on 4b2 0e and 2e bounding with reductions of 4 already beats three routes, more than "just check the really short ones" suggests; on 2c3 6e and on 4c3 ("Bounding is actually REALLY good for 4c3") the routes are well ahead (section 8). |
| "half of all 3QT cases and a quarter of all 4QT cases can immediately be reduced to 2QT by applying a U move to the normal and/or inverse", amended to "2/3 of 3QT cases and 1/6 of 4QT cases" | rodneykinney [11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062756177424961546), [11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062823846954160128) | 3qt: **True**, exact: one bare qt on normal or inverse does it for 66.1% of 3qt corner arrangements (Lean-checked). 4qt: **Open**: one bare qt never does it (exact); it takes a qt on each side, the "and" of "and/or", which rodneykinney's 1/6 counted from optimal corner solutions ([11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062820653113290773), [11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062821731091349525)) and this study did not. |
| R from [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531409959948369), "the biggest possible length of a reduction to 1q you have to check" | FakeMMAP [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491531394667773962) | **True** as written: never too short in 1,914,809 cases at the optimum. C must be the shortest NISS HTR for the derivation (section 9). |
| The multi-qt lower bounds of [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475), with "I don't know how useful these bounds really are, I have to put in the numbers to see if there are situations where the typical bound is M \geq 11, rather than M \geq 7 lol." | FakeMMAP [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533155201716475), [8 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491533429198553178) | **Corrected** [f]: the sum needs α_{i+1}; as written the bounds fail in 923 cases. Section 9 gives the typical bound values FakeMMAP asked about. |
| "it just produces optimal in 15 minutes like 80% of the time" (following the system) | Zagros [29 Dec 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1455302363953758427) | **Open**: time is not modelled; the 4b2 order done fully gives 71.3% with budget-2 HTRs (section 10). |

Letters refer to the errata.

---

## 12. What this does not cover

- **Findability and time.** Every number is what exists along a route, not what a solver finds in an attempt. The HTR budget is a stand-in for effort (how much longer than the shortest HTR you are willing to look), not a cost model: it does not count how many HTRs of that length a route has, or how long setups take. A route and a reduction are different amounts of work, so section 8's comparison is only in kind.
- **Half turns inside a route.** Routes record the corner subsets after each quarter turn, not how many half turns come between. Steps of hand checklists that limit setup moves ("1-2 moves to trigger", "two half turns followed by a quarter turn") are graded as their whole route, which flatters them; Jay's and rodneykinney's setup counts are not graded separately.
- **Samples.** Route and bounding questions are sampled (25,000 states per subset × edges; 4,000 for reduction counts). A share's standard error is at most 0.3 points per subset × edges; small differences between routes deep in a checklist are within noise. The +1 level uses the same enumeration as the optimum but was not cross-checked by an independent solver.
- **DR-breaking and HTR-breaking finishes**, and finishes that leave the slice, are not routes here: finishes stay in the DR group, E slice solved. (The leave-slice optimum is used only where a sheet uses it.)
- **The DR itself.** Uniform DR states. Real DRs come from EOs and triggers and are not uniform within a subset (Kai Cui's and JTuu's generated states show how much that can matter, section 8). Variations of the DR other than its last move are not covered.
- **Fixed targets** of 10 to 12 in sections 8 and 9 use finishes up to max(optimal + 1, min(optimal + 2, 12)) moves; for DRs whose optimum is 9 or less, a longer target is not covered.
- **rodneykinney's 4qt "1/6"** (a quarter turn on each side taking 4qt to 2qt) is not computed.

---

## Appendix A: full tables

**Every checklist, budget 2**: per subset × edges, the first eight routes in greedy order, the cumulative share of DRs where the routes so far find an optimal finish, and where the same routes find a finish within +1 (same HTR budget). Sampled, 25,000 per subset × edges.

| Subset | # | Class | Optimal, cumulative | Within +1, cumulative |
|---|---|---|---|---|
| 0c0 0e | 1 | `0c0 > 4a1 > 0c0` | 42.5% | 48.2% |
|  | 2 | `0c0` | 84.4% | 95.1% |
|  | 3 | `0c0 | qt` | 92.6% | 98.3% |
|  | 4 | `0c0 > 4a1 > 0c0 | qt` (mirror: `0c0 > 4a1 > (4a2 > 4a1 > 4b2 > 4a1 > 0c0)`) | 92.9% | 98.5% |
|  | 5 | `0c0 > 4a1 > (0c0)` | 93.0% | 98.6% |
| 0c0 2e | 1 | `0c0 > 4a1 > 0c0` | 60.5% | 83.7% |
|  | 2 | `0c0 > 4a1 > 0c0 > 4a1 > (0c0)` (mirror: `0c0 > 4a1 > (4a2 > 4a1 > 0c0)`) | 65.7% | 88.3% |
|  | 3 | `0c0 > 4a1 > (0c0)` | 70.2% | 92.3% |
|  | 4 | `0c0 > 4a1 > 4b2 > 4a1 > 0c0` | 72.3% | 93.8% |
|  | 5 | `0c0 > 4a1 > 0c0 > (4a1 > 0c0)` (mirror: `0c0 > 4a1 > 0c0 | qt`) | 73.0% | 94.1% |
|  | 6 | `0c0 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `0c0 > 4a1 > 4b2 > 4a1 > (0c0)`) | 73.8% | 94.3% |
|  | 7 | `0c0 > 4a1 > 0c0 | qt` (mirror: `0c0 > 4a1 > (4a2 > 4a1 > 4b2 > 4a1 > 0c0)`) | 74.1% | 95.0% |
|  | 8 | `0c0 > 4a1 > 4b2 > (4a1 > 0c0)` | 74.3% | 95.2% |
| 0c0 4e | 1 | `0c0 > 4a1 > 0c0` | 44.9% | 70.0% |
|  | 2 | `0c0 > 4a1 > (0c0)` | 57.8% | 83.6% |
|  | 3 | `0c0 > 4a1 > 4b2 > 4a1 > 0c0` | 61.5% | 88.1% |
|  | 4 | `0c0 > 4a1 > 4b2 > (4a1 > 0c0)` | 63.6% | 89.9% |
|  | 5 | `0c0 > 4a1 > 0c0 > 4a1 > 0c0` | 65.1% | 90.5% |
|  | 6 | `0c0 > 4a1 > 0c0 > 4a1 > (0c0)` (mirror: `0c0 > 4a1 > (4a2 > 4a1 > 0c0)`) | 66.4% | 91.3% |
|  | 7 | `0c0 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `0c0 > 4a1 > 4b2 > 4a1 > (0c0)`) | 67.5% | 91.9% |
|  | 8 | `0c0 > 4a1 > 0c0 > (4a1 > 0c0)` (mirror: `0c0 > 4a1 > 0c0 | qt`) | 68.4% | 92.1% |
| 0c0 6e | 1 | `0c0 > 4a1 > (0c0)` | 40.8% | 70.7% |
|  | 2 | `0c0 > 4a1 > 0c0 > 4a1 > (0c0)` (mirror: `0c0 > 4a1 > (4a2 > 4a1 > 0c0)`) | 53.7% | 83.9% |
|  | 3 | `0c0 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `0c0 > 4a1 > 4b2 > 4a1 > (0c0)`) | 60.2% | 88.0% |
|  | 4 | `0c0 > 4a1 > 4b2 > (4a1 > 0c0)` | 64.0% | 90.3% |
|  | 5 | `0c0 > 4a1 > 0c0 > 4a1 > 0c0` | 65.7% | 91.1% |
|  | 6 | `0c0 > 4a1 > 0c0` | 66.8% | 92.0% |
|  | 7 | `0c0 > 4a1 > 0c0 > (4a1 > 0c0)` (mirror: `0c0 > 4a1 > 0c0 | qt`) | 67.4% | 92.2% |
|  | 8 | `0c0 > 4a1 > 4b2 > 4a1 > 0c0` | 67.8% | 92.2% |
| 0c0 8e | 1 | `0c0 > 4a1 > (0c0)` | 53.5% | 78.7% |
|  | 2 | `0c0 > 4a1 > 0c0` | 70.1% | 91.7% |
|  | 3 | `0c0 > 4a1 > 0c0 > 4a1 > (0c0)` (mirror: `0c0 > 4a1 > (4a2 > 4a1 > 0c0)`) | 77.1% | 95.0% |
|  | 4 | `0c0 > 4a1 > 4b2 > (4a1 > 0c0)` | 77.8% | 95.4% |
|  | 5 | `0c0 > 4a1 > 4b2 > 4a1 > 0c0` | 78.3% | 95.7% |
|  | 6 | `0c0 > 4a1 > 0c0 > (4a1 > 0c0)` (mirror: `0c0 > 4a1 > 0c0 | qt`) | 78.5% | 95.8% |
|  | 7 | `0c0 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `0c0 > 4a1 > 4b2 > 4a1 > (0c0)`) | 78.7% | 95.8% |
|  | 8 | `0c0 > 4a1 > 0c0 | qt` (mirror: `0c0 > 4a1 > (4a2 > 4a1 > 4b2 > 4a1 > 0c0)`) | 78.8% | 96.0% |
| 2c5 0e | 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 77.8% | 95.5% |
|  | 2 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 86.5% | 98.0% |
|  | 3 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 89.6% | 98.7% |
|  | 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 91.4% | 99.1% |
|  | 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 91.8% | 99.2% |
|  | 6 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 91.9% | 99.3% |
|  | 7 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 92.0% | 99.3% |
|  | 8 | `2c5 > 4b4 > 2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 92.1% | 99.3% |
| 2c5 2e | 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 74.8% | 94.2% |
|  | 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.2% | 97.7% |
|  | 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 91.0% | 98.7% |
|  | 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 92.4% | 99.1% |
|  | 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 92.9% | 99.4% |
|  | 6 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 93.1% | 99.4% |
|  | 7 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 93.2% | 99.5% |
|  | 8 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 93.2% | 99.5% |
| 2c5 4e | 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 71.5% | 92.8% |
|  | 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.0% | 97.8% |
|  | 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 91.9% | 99.0% |
|  | 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 93.2% | 99.4% |
|  | 5 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 93.4% | 99.5% |
|  | 6 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 93.6% | 99.5% |
|  | 7 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 93.7% | 99.6% |
|  | 8 | `2c5 > 4b4 > 2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 93.8% | 99.6% |
| 2c5 6e | 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 73.0% | 93.3% |
|  | 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | 97.3% |
|  | 3 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 90.6% | 98.7% |
|  | 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 92.4% | 99.3% |
|  | 5 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 92.7% | 99.4% |
|  | 6 | `2c5 > 4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 92.9% | 99.5% |
|  | 7 | `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 93.0% | 99.5% |
|  | 8 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 93.2% | 99.5% |
| 2c5 8e | 1 | `2c5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 77.6% | 94.9% |
|  | 2 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 86.0% | 97.6% |
|  | 3 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 91.0% | 98.9% |
|  | 4 | `2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 92.2% | 99.3% |
|  | 5 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 92.5% | 99.4% |
|  | 6 | `2c5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 92.7% | 99.4% |
|  | 7 | `2c5 > 4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c5 > 4b4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 92.9% | 99.5% |
|  | 8 | `2c5 > 4b4 > 4a3 > 4b2 > 4a1 > (0c0)` (mirror: `2c5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)`) | 93.0% | 99.5% |
| 2c4 0e | 1 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 70.1% | 91.8% |
|  | 2 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > 4a1 > (0c0)`) | 85.9% | 98.0% |
|  | 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 88.6% | 98.7% |
|  | 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 88.8% | 98.8% |
|  | 5 | `2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 88.9% | 98.8% |
|  | 6 | `2c4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 4a4 > 4a3 > (4a2 > 4a1 > 0c0)`) | 89.0% | 98.8% |
|  | 7 | `2c4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 2c3 > 4b2 > 4a1 > 0c0 > 4a1 > (0c0)`) | 89.1% | 98.8% |
|  | 8 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 2c3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 89.2% | 98.8% |
| 2c4 2e | 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > 4a1 > (0c0)`) | 67.7% | 91.3% |
|  | 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | 97.8% |
|  | 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 89.9% | 98.9% |
|  | 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 2c3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 90.5% | 99.0% |
|  | 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 90.8% | 99.1% |
|  | 6 | `2c4 > 4b3 > 4a2 > 4a1 > 0c0` | 91.0% | 99.1% |
|  | 7 | `2c4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 4a4 > 4a3 > (4a2 > 4a1 > 0c0)`) | 91.2% | 99.1% |
|  | 8 | `2c4 > 2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 91.3% | 99.1% |
| 2c4 4e | 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > 4a1 > (0c0)`) | 62.0% | 88.0% |
|  | 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.0% | 97.0% |
|  | 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 87.6% | 98.7% |
|  | 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 88.1% | 98.8% |
|  | 5 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 2c3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 88.4% | 98.8% |
|  | 6 | `2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 88.7% | 98.9% |
|  | 7 | `2c4 > 4b3 > 4a2 > 4a1 > 0c0` | 88.9% | 98.9% |
|  | 8 | `2c4 > 2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 89.1% | 98.9% |
| 2c4 6e | 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > 4a1 > (0c0)`) | 73.8% | 94.2% |
|  | 2 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.1% | 97.3% |
|  | 3 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 88.5% | 98.6% |
|  | 4 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 2c3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 89.2% | 98.8% |
|  | 5 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 89.6% | 98.8% |
|  | 6 | `2c4 > 4b3 > 4a2 > 4a1 > 0c0` | 90.0% | 98.9% |
|  | 7 | `2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 90.1% | 98.9% |
|  | 8 | `2c4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 4a4 > 4a3 > (4a2 > 4a1 > 0c0)`) | 90.3% | 98.9% |
| 2c4 8e | 1 | `2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > 4a1 > (0c0)`) | 77.7% | 95.3% |
|  | 2 | `2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 89.5% | 99.3% |
|  | 3 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 91.5% | 99.4% |
|  | 4 | `2c4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 92.3% | 99.5% |
|  | 5 | `2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 92.9% | 99.6% |
|  | 6 | `2c4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 2c3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 93.3% | 99.6% |
|  | 7 | `2c4 > 2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 93.5% | 99.6% |
|  | 8 | `2c4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c4 > 4b5 > 4a4 > 4a3 > (4a2 > 4a1 > 0c0)`) | 93.7% | 99.6% |
| 0c3 0e | 1 | `0c3 > 4a2 > (4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > (0c0)`) | 85.5% | 97.3% |
|  | 2 | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `0c3 > 4a2 > (4a1 > 4b2 > 4a1 > 0c0)`) | 94.2% | 99.5% |
|  | 3 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4b3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 96.6% | 99.8% |
|  | 4 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 96.9% | 99.8% |
|  | 5 | `0c3 > 4a2 > (4b3 > 4a2 > 4a1 > 0c0)` (mirror: `0c3 > 4a4 > 0c3 > 4a2 > 4a1 > (0c0)`) | 97.2% | 99.8% |
|  | 6 | `0c3 > 4a4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 97.3% | 99.8% |
|  | 7 | `0c3 > 4a2 > 4b3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 97.4% | 99.9% |
|  | 8 | `0c3 > 4a4 > (2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 97.4% | 99.9% |
| 0c3 2e | 1 | `0c3 > 4a2 > (4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > (0c0)`) | 80.8% | 97.5% |
|  | 2 | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `0c3 > 4a2 > (4a1 > 4b2 > 4a1 > 0c0)`) | 91.3% | 99.3% |
|  | 3 | `0c3 > 4a2 > 4a1 > 0c0` | 92.1% | 99.5% |
|  | 4 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4b3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 92.5% | 99.6% |
|  | 5 | `0c3 > 4a2 > (4b3 > 4a2 > 4a1 > 0c0)` (mirror: `0c3 > 4a4 > 0c3 > 4a2 > 4a1 > (0c0)`) | 92.8% | 99.6% |
|  | 6 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `0c3 > 4a4 > (2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 93.0% | 99.6% |
|  | 7 | `0c3 > 4a2 > 4b3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > 4b2 > (4a1 > 0c0)`) | 93.2% | 99.6% |
|  | 8 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `0c3 > 4a4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 93.3% | 99.6% |
| 0c3 4e | 1 | `0c3 > 4a2 > (4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > (0c0)`) | 67.2% | 94.5% |
|  | 2 | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `0c3 > 4a2 > (4a1 > 4b2 > 4a1 > 0c0)`) | 85.1% | 98.7% |
|  | 3 | `0c3 > 4a2 > 4b3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > 4b2 > (4a1 > 0c0)`) | 85.8% | 98.7% |
|  | 4 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `0c3 > 4a4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 86.4% | 98.9% |
|  | 5 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4b3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 86.8% | 98.9% |
|  | 6 | `0c3 > 4a2 > (4b3 > 4a2 > 4a1 > 0c0)` (mirror: `0c3 > 4a4 > 0c3 > 4a2 > 4a1 > (0c0)`) | 87.2% | 98.9% |
|  | 7 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `0c3 > 4a4 > (2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 87.4% | 99.0% |
|  | 8 | `0c3 > 4a2 > 4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4b3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 87.5% | 99.0% |
| 0c3 6e | 1 | `0c3 > 4a2 > (4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > (0c0)`) | 82.6% | 98.0% |
|  | 2 | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `0c3 > 4a2 > (4a1 > 4b2 > 4a1 > 0c0)`) | 93.9% | 99.5% |
|  | 3 | `0c3 > 4a2 > 4a1 > 0c0` | 94.6% | 99.7% |
|  | 4 | `0c3 > 4a2 > (4b3 > 4a2 > 4a1 > 0c0)` (mirror: `0c3 > 4a4 > 0c3 > 4a2 > 4a1 > (0c0)`) | 94.9% | 99.7% |
|  | 5 | `0c3 > 4a2 > 4b3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > 4b2 > (4a1 > 0c0)`) | 95.2% | 99.7% |
|  | 6 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `0c3 > 4a4 > (2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 95.3% | 99.7% |
|  | 7 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4b3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 95.4% | 99.7% |
|  | 8 | `0c3 > 4a4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 95.5% | 99.7% |
| 0c3 8e | 1 | `0c3 > 4a2 > (4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > (0c0)`) | 87.3% | 98.0% |
|  | 2 | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `0c3 > 4a2 > (4a1 > 4b2 > 4a1 > 0c0)`) | 94.8% | 99.5% |
|  | 3 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `0c3 > 4a4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 96.1% | 99.7% |
|  | 4 | `0c3 > 4a2 > 4b3 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `0c3 > 4a4 > 4b5 > (2c4 > 4b3 > 4a2 > 4a1 > 0c0)`) | 96.5% | 99.7% |
|  | 5 | `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 96.8% | 99.7% |
|  | 6 | `0c3 > 4a4 > (2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 97.0% | 99.7% |
|  | 7 | `0c3 > 4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 97.1% | 99.8% |
|  | 8 | `0c3 > 4a2 > 4b3 > (4b2 > 4a1 > 0c0)` (mirror: `0c3 > 4a2 > 4a1 > 4b2 > (4a1 > 0c0)`) | 97.2% | 99.8% |
| 4a2 0e | 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `4a2 > 4a1 > (4b2 > 4a1 > 0c0)`) | 29.1% | 46.4% |
|  | 2 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 40.4% | 56.4% |
|  | 3 | `4a2 > 4a1 > (0c0)` | 44.4% | 68.2% |
|  | 4 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 48.2% | 73.3% |
|  | 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `4a2 > 4a1 > 4a2 > 4a1 > (0c0)`) | 50.3% | 74.6% |
|  | 6 | `4a2 > 4b3 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a2 > 4b3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 52.1% | 75.5% |
|  | 7 | `4a2 > 4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a2 > 4a1 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)`) | 52.8% | 75.8% |
|  | 8 | `4a2 > 4b3 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `4a2 > 4b3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 53.1% | 75.9% |
| 4a2 2e | 1 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `4a2 > 4a1 > (4b2 > 4a1 > 0c0)`) | 42.2% | 77.2% |
|  | 2 | `4a2 > 4a1 > (0c0)` | 67.8% | 92.0% |
|  | 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 76.8% | 95.7% |
|  | 4 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `4a2 > 4a1 > 4a2 > 4a1 > (0c0)`) | 79.6% | 96.9% |
|  | 5 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 81.4% | 97.6% |
|  | 6 | `4a2 > 4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 82.4% | 97.8% |
|  | 7 | `4a2 > 4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a2 > 4a1 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)`) | 83.1% | 98.0% |
|  | 8 | `4a2 > 4b3 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a2 > 4b3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 83.6% | 98.1% |
| 4a2 4e | 1 | `4a2 > 4a1 > 0c0` | 60.9% | 83.9% |
|  | 2 | `4a2 > 4b3 > 4a2 > 4a1 > (0c0)` (mirror: `4a2 > 4a1 > (4b2 > 4a1 > 0c0)`) | 72.2% | 91.1% |
|  | 3 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 79.1% | 93.6% |
|  | 4 | `4a2 > 4a1 > (0c0)` | 83.7% | 95.9% |
|  | 5 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `4a2 > 4a1 > 4a2 > 4a1 > (0c0)`) | 85.3% | 96.5% |
|  | 6 | `4a2 > 4a1 > 4b2 > (4a1 > 0c0)` | 86.1% | 96.9% |
|  | 7 | `4a2 > 4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a2 > 4a1 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)`) | 86.3% | 96.9% |
|  | 8 | `4a2 > 4b3 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a2 > 4b3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 86.4% | 97.0% |
| 4a1 0e | 1 | `4a1 > 0c0 > (4a1 > 0c0)` (mirror: `4a1 > 4a2 > 4a1 > (0c0)`) | 33.5% | 56.5% |
|  | 2 | `4a1 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `4a1 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)`) | 46.5% | 71.3% |
|  | 3 | `4a1 > 0c0 > 4a1 > (0c0)` (mirror: `4a1 > 4a2 > (4a1 > 0c0)`) | 54.6% | 84.2% |
|  | 4 | `4a1 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 61.1% | 87.8% |
|  | 5 | `4a1 > 0c0 > 4a1 > 0c0` | 66.5% | 90.7% |
|  | 6 | `4a1 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a1 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 70.5% | 92.4% |
|  | 7 | `4a1 > 4b2 > 4a1 > 0c0 > 4a1 > (0c0)` (mirror: `4a1 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)`) | 71.7% | 92.9% |
|  | 8 | `4a1 > 4b2 > 4a1 > 0c0 > (4a1 > 0c0)` (mirror: `4a1 > 4b2 > 4a1 > (4b2 > 4a1 > 0c0)`) | 72.2% | 92.9% |
| 4a1 2e | 1 | `4a1 > 4b2 > 4a1 > 0c0` | 38.8% | 67.5% |
|  | 2 | `4a1 > 0c0 > 4a1 > 0c0` | 58.8% | 85.8% |
|  | 3 | `4a1 > 0c0 > (4a1 > 0c0)` (mirror: `4a1 > 4a2 > 4a1 > (0c0)`) | 70.5% | 91.7% |
|  | 4 | `4a1 > 0c0 > 4a1 > (0c0)` (mirror: `4a1 > 4a2 > (4a1 > 0c0)`) | 76.7% | 95.4% |
|  | 5 | `4a1 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a1 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 78.2% | 96.0% |
|  | 6 | `4a1 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a1 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 79.0% | 96.2% |
|  | 7 | `4a1 > 0c0 > 4a1 > (4b2 > 4a1 > 0c0)` (mirror: `4a1 > 4a2 > 4a1 > 4b2 > (4a1 > 0c0)`) | 79.4% | 96.4% |
|  | 8 | `4a1 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 79.8% | 96.5% |
| 4a1 4e | 1 | `4a1 > 0c0` | 33.6% | 57.1% |
|  | 2 | `4a1 > 4b2 > 4a1 > 0c0` | 50.3% | 78.3% |
|  | 3 | `4a1 > 0c0 > (4a1 > 0c0)` (mirror: `4a1 > 4a2 > 4a1 > (0c0)`) | 60.6% | 86.2% |
|  | 4 | `4a1 > 0c0 > 4a1 > (0c0)` (mirror: `4a1 > 4a2 > (4a1 > 0c0)`) | 66.6% | 91.1% |
|  | 5 | `4a1 > 0c0 > 4a1 > 0c0` | 69.5% | 92.2% |
|  | 6 | `4a1 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a1 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 70.1% | 92.5% |
|  | 7 | `4a1 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a1 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 70.5% | 92.7% |
|  | 8 | `4a1 > 0c0 | qt` (mirror: `4a1 > 4b2 > (4a1 > 4b2 > 4a1 > 0c0)`) | 70.7% | 93.1% |
| 2c3 0e | 1 | `2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a1 > (0c0)`) | 46.3% | 81.8% |
|  | 2 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 67.0% | 93.7% |
|  | 3 | `2c3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 75.1% | 95.9% |
|  | 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 81.4% | 97.5% |
|  | 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a3 > 4b2 > (4a1 > 0c0)`) | 85.5% | 98.4% |
|  | 6 | `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.7% | 98.5% |
|  | 7 | `2c3 > 4b2 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a3 > 4b2 > (4a1 > 0c0)`) | 87.4% | 98.7% |
|  | 8 | `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 88.1% | 98.8% |
| 2c3 2e | 1 | `2c3 > 4b2 > 4a1 > 0c0` | 66.5% | 89.6% |
|  | 2 | `2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a1 > (0c0)`) | 79.6% | 96.4% |
|  | 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 80.2% | 96.6% |
|  | 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 80.6% | 96.7% |
|  | 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a3 > 4b2 > (4a1 > 0c0)`) | 80.8% | 96.7% |
|  | 6 | `2c3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 81.0% | 96.8% |
|  | 7 | `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 81.2% | 96.8% |
|  | 8 | `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 81.2% | 96.8% |
| 2c3 4e | 1 | `2c3 > 4b2 > 4a1 > 0c0` | 55.3% | 82.1% |
|  | 2 | `2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a1 > (0c0)`) | 76.6% | 95.6% |
|  | 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 78.1% | 96.1% |
|  | 4 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 79.1% | 96.4% |
|  | 5 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a3 > 4b2 > (4a1 > 0c0)`) | 79.9% | 96.6% |
|  | 6 | `2c3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 80.6% | 96.9% |
|  | 7 | `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 80.9% | 97.0% |
|  | 8 | `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 81.2% | 97.0% |
| 2c3 6e | 1 | `2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a1 > (0c0)`) | 66.1% | 91.8% |
|  | 2 | `2c3 > 4b2 > 4a1 > 0c0` | 73.3% | 94.7% |
|  | 3 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 76.7% | 95.8% |
|  | 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a3 > 4b2 > (4a1 > 0c0)`) | 78.3% | 96.3% |
|  | 5 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 79.8% | 96.7% |
|  | 6 | `2c3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 80.8% | 96.9% |
|  | 7 | `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 81.2% | 97.0% |
|  | 8 | `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 81.6% | 97.1% |
| 2c3 8e | 1 | `2c3 > 4b2 > (4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a1 > (0c0)`) | 46.3% | 81.2% |
|  | 2 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 67.2% | 93.2% |
|  | 3 | `2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 74.5% | 95.7% |
|  | 4 | `2c3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a3 > 4b2 > (4a1 > 0c0)`) | 78.3% | 96.8% |
|  | 5 | `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 81.3% | 97.5% |
|  | 6 | `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 83.4% | 98.0% |
|  | 7 | `2c3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 85.5% | 98.4% |
|  | 8 | `2c3 > 4b2 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `2c3 > 4b2 > 4a3 > 4b2 > (4a1 > 0c0)`) | 85.9% | 98.4% |
| 0c4 0e | 1 | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | 83.2% | 95.4% |
|  | 2 | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 86.8% | 97.3% |
|  | 3 | `0c4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 87.6% | 97.5% |
|  | 4 | `0c4 > 4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 88.0% | 97.7% |
|  | 5 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `0c4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 88.3% | 97.7% |
|  | 6 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)`) | 88.4% | 97.7% |
|  | 7 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 88.5% | 97.7% |
| 0c4 2e | 1 | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | 86.5% | 97.3% |
|  | 2 | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 88.0% | 97.7% |
|  | 3 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `0c4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 89.1% | 98.1% |
|  | 4 | `0c4 > 4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 89.9% | 98.2% |
|  | 5 | `0c4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 90.6% | 98.5% |
|  | 6 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)`) | 91.0% | 98.5% |
|  | 7 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 91.2% | 98.6% |
|  | 8 | `0c4 > 4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > (4a1 > 4b2 > 4a1 > 0c0)`) | 91.2% | 98.6% |
| 0c4 4e | 1 | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | 83.5% | 96.8% |
|  | 2 | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 85.1% | 97.2% |
|  | 3 | `0c4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 86.1% | 97.5% |
|  | 4 | `0c4 > 4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 87.1% | 97.7% |
|  | 5 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `0c4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 87.8% | 97.9% |
|  | 6 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)`) | 88.3% | 98.0% |
|  | 7 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 88.6% | 98.1% |
|  | 8 | `0c4 > 4a3 > 4b2 > (4a1 > 4b2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 88.6% | 98.1% |
| 0c4 6e | 1 | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | 81.8% | 96.6% |
|  | 2 | `0c4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 83.7% | 97.3% |
|  | 3 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `0c4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 85.4% | 97.8% |
|  | 4 | `0c4 > 4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 86.5% | 98.0% |
|  | 5 | `0c4 > 4a3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 87.3% | 98.2% |
|  | 6 | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 87.7% | 98.2% |
|  | 7 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 88.0% | 98.3% |
|  | 8 | `0c4 > 4a3 > 4b2 > (4a1 > 0c0 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 88.1% | 98.3% |
| 0c4 8e | 1 | `0c4 > 4a3 > 4b2 > (4a1 > 0c0)` | 80.3% | 96.2% |
|  | 2 | `0c4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 86.2% | 98.0% |
|  | 3 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `0c4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)`) | 87.1% | 98.2% |
|  | 4 | `0c4 > 4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` | 87.9% | 98.4% |
|  | 5 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `0c4 > 4a3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)`) | 88.1% | 98.4% |
|  | 6 | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 88.3% | 98.4% |
| 4c3 0e | 1 | `4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4b3 > 4a2 > 4a1 > (0c0)`) | 70.8% | 90.7% |
|  | 2 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b3 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 78.4% | 94.5% |
|  | 3 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 83.3% | 96.2% |
|  | 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 86.3% | 97.0% |
|  | 5 | `4b3 > 4a2 > 4a1 > 0c0` | 88.6% | 98.5% |
|  | 6 | `4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `4b3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 90.2% | 98.8% |
|  | 7 | `4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 91.5% | 99.1% |
|  | 8 | `4a3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 92.3% | 99.2% |
| 4c3 2e | 1 | `4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4b3 > 4a2 > 4a1 > (0c0)`) | 66.2% | 90.6% |
|  | 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 72.0% | 93.0% |
|  | 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b3 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 75.1% | 94.3% |
|  | 4 | `4b3 > 4a2 > 4a1 > 0c0` | 77.9% | 95.7% |
|  | 5 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 80.1% | 96.2% |
|  | 6 | `4a3 > 4b2 > 4a1 > 0c0` | 81.8% | 96.8% |
|  | 7 | `4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `4b3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 83.2% | 97.3% |
|  | 8 | `4a3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 84.4% | 97.5% |
| 4c3 4e | 1 | `4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4b3 > 4a2 > 4a1 > (0c0)`) | 62.3% | 88.3% |
|  | 2 | `4b3 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 70.2% | 92.2% |
|  | 3 | `4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b3 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)`) | 74.4% | 93.9% |
|  | 4 | `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 77.6% | 94.9% |
|  | 5 | `4a3 > 4b2 > 4a1 > 0c0` | 79.6% | 95.8% |
|  | 6 | `4a3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b3 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 81.3% | 96.3% |
|  | 7 | `4b3 > 4a2 > 4a1 > 0c0` | 82.9% | 97.2% |
|  | 8 | `4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `4b3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 84.4% | 97.5% |
| 4c4 0e | 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4a4 > 0c3 > 4a2 > (4a1 > 0c0)`) | 65.2% | 92.0% |
|  | 2 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b4 > 2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)`) | 72.4% | 95.0% |
|  | 3 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 76.7% | 96.3% |
|  | 4 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b4 > 4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 80.0% | 97.0% |
|  | 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 81.9% | 97.4% |
|  | 6 | `4a4 > 4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `4b4 > 4a3 > 0c4 > (4a3 > 4b2 > 4a1 > 0c0)`) | 82.9% | 97.6% |
|  | 7 | `4b4 > 2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 83.5% | 97.6% |
|  | 8 | `4b4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `4a4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 84.1% | 97.8% |
| 4c4 2e | 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4a4 > 0c3 > 4a2 > (4a1 > 0c0)`) | 67.9% | 92.4% |
|  | 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b4 > 4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 75.4% | 95.5% |
|  | 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b4 > 2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)`) | 78.7% | 96.4% |
|  | 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 80.8% | 96.9% |
|  | 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 82.1% | 97.2% |
|  | 6 | `4a4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 83.3% | 97.4% |
|  | 7 | `4a4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.2% | 97.6% |
|  | 8 | `4b4 > 2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 85.2% | 97.7% |
| 4c4 4e | 1 | `4b4 > 4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4a4 > 0c3 > 4a2 > (4a1 > 0c0)`) | 68.4% | 92.5% |
|  | 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b4 > 4a3 > 0c4 > 4a3 > 4b2 > (4a1 > 0c0)`) | 74.8% | 95.1% |
|  | 3 | `4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b4 > 2c5 > 4b4 > 4a3 > (4a2 > 4a1 > 0c0)`) | 78.2% | 95.9% |
|  | 4 | `4b4 > 2c5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 80.2% | 96.5% |
|  | 5 | `4b4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4a4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 81.5% | 96.7% |
|  | 6 | `4a4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 82.6% | 97.0% |
|  | 7 | `4b4 > 4a3 > (4a2 > 4a1 > 0c0)` (mirror: `4a4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 83.6% | 97.4% |
|  | 8 | `4b4 > 2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 84.6% | 97.5% |
| 4b2 0e | 1 | `4b2 > 4a1 > 0c0` | 36.5% | 64.3% |
|  | 2 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `4b2 > 4a1 > 0c0 > (4a1 > 0c0)`) | 51.1% | 78.4% |
|  | 3 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 61.0% | 85.5% |
|  | 4 | `4b2 > 4a1 > (0c0)` | 68.1% | 91.5% |
|  | 5 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 72.4% | 93.1% |
|  | 6 | `4b2 > 4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4b2 > 4a1 > 0c0 > (4a1 > 0c0)`) | 75.5% | 94.4% |
|  | 7 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `4b2 > 2c3 > (4b2 > 4a1 > 0c0)`) | 77.9% | 95.3% |
|  | 8 | `4b2 > 4a1 > 4b2 > (4a1 > 0c0)` (mirror: `4b2 > 4a1 > 0c0 > (4a1 > 0c0)`) | 78.4% | 95.5% |
| 4b2 2e | 1 | `4b2 > 4a1 > 0c0` | 45.9% | 76.5% |
|  | 2 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `4b2 > 2c3 > (4b2 > 4a1 > 0c0)`) | 53.7% | 83.2% |
|  | 3 | `4b2 > 4a1 > (0c0)` | 59.0% | 86.3% |
|  | 4 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 63.3% | 88.8% |
|  | 5 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `4b2 > 4a1 > 0c0 > (4a1 > 0c0)`) | 66.3% | 90.1% |
|  | 6 | `4b2 > 4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4b2 > 4a1 > 0c0 > (4a1 > 0c0)`) | 67.3% | 90.5% |
|  | 7 | `4b2 > 4a1 > 0c0 > 4a1 > (0c0)` (mirror: `4b2 > 2c3 > (4b2 > 4a1 > 0c0)`) | 68.2% | 91.3% |
|  | 8 | `4b2 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `4b2 > 4a1 > 4a2 > 4a1 > (0c0)`) | 68.6% | 91.5% |
| 4b2 4e | 1 | `4b2 > 4a1 > 0c0` | 30.3% | 59.1% |
|  | 2 | `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b2 > 2c3 > 4b2 > 4a1 > (0c0)`) | 53.3% | 82.2% |
|  | 3 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 66.8% | 89.1% |
|  | 4 | `4b2 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `4b2 > 4a1 > 0c0 > (4a1 > 0c0)`) | 71.7% | 91.1% |
|  | 5 | `4b2 > 4a1 > (0c0)` | 76.0% | 94.9% |
|  | 6 | `4b2 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `4b2 > 2c3 > (4b2 > 4a1 > 0c0)`) | 77.8% | 95.5% |
|  | 7 | `4b2 > 4a3 > 4b2 > (4a1 > 0c0)` (mirror: `4b2 > 4a1 > 0c0 > (4a1 > 0c0)`) | 79.3% | 96.0% |
|  | 8 | `4b2 > 4a1 > (0c0 > 4a1 > 0c0)` (mirror: `4b2 > 4a1 > 4a2 > 4a1 > (0c0)`) | 80.5% | 96.5% |
| 4b5 0e | 1 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 60.8% | 86.9% |
|  | 2 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 84.2% | 97.4% |
|  | 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 92.6% | 99.4% |
|  | 4 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` (mirror: `4b5 > 4a4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 92.8% | 99.4% |
|  | 5 | `4b5 > 2c4 > 4b3 > 4a2 > 4a1 > 0c0` | 93.0% | 99.4% |
|  | 6 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 93.2% | 99.5% |
|  | 7 | `4b5 > 4a4 > (2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0 > 4a1 > (0c0)`) | 93.2% | 99.5% |
|  | 8 | `4b5 > 4a4 > 4a3 > 4b2 > 4a1 > 0c0` | 93.3% | 99.5% |
| 4b5 2e | 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 62.6% | 88.0% |
|  | 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 85.1% | 98.0% |
|  | 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% | 99.6% |
|  | 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 93.7% | 99.6% |
|  | 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` (mirror: `4b5 > 4a4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 93.8% | 99.7% |
|  | 6 | `4b5 > 4a4 > 4a3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)`) | 93.8% | 99.7% |
|  | 7 | `4b5 > 4a4 > 4a3 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > 4b2 > 2c3 > 4b2 > (4a1 > 0c0)`) | 93.9% | 99.7% |
|  | 8 | `4b5 > 2c4 > 2c3 > 4b2 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b5 > 4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 93.9% | 99.7% |
| 4b5 4e | 1 | `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)`) | 67.0% | 90.5% |
|  | 2 | `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 4b3 > 4a2 > (4a1 > 0c0)`) | 89.6% | 99.1% |
|  | 3 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.9% | 99.6% |
|  | 4 | `4b5 > 2c4 > 2c3 > 4b2 > (4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 94.0% | 99.7% |
|  | 5 | `4b5 > 2c4 > (4b3 > 4a2 > 4a1 > 0c0)` (mirror: `4b5 > 4a4 > 4a3 > 4b2 > 4a1 > (0c0)`) | 94.0% | 99.7% |
|  | 6 | `4b5 > 4a4 > (2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0 > 4a1 > (0c0)`) | 94.1% | 99.7% |
|  | 7 | `4b5 > 4a4 > 4a3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` (mirror: `4b5 > 4a4 > 4b5 > 2c4 > 2c3 > (4b2 > 4a1 > 0c0)`) | 94.1% | 99.7% |
|  | 8 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > (0c0)` (mirror: `4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)`) | 94.2% | 99.7% |

**Checklists with no HTR limit**, first four routes. With no limit the routes overlap so much that these lists say more about which readings exist than what to try:

| Subset | # | Class | Optimal, cumulative |
|---|---|---|---|
| 0c0 0e | 1 | `0c0 > 4a1 > 0c0` | 49.4% |
|  | 2 | `0c0` | 91.2% |
|  | 3 | `0c0 | qt` | 99.5% |
|  | 4 | `0c0 > 4a1 > (0c0 > 4a1 > 0c0)` | 99.8% |
| 0c0 2e | 1 | `0c0 > 4a1 > 0c0` | 70.1% |
|  | 2 | `0c0 > 4a1 > 0c0 > 4a1 > 0c0` | 93.2% |
|  | 3 | `0c0 > 4a1 > 4b2 > 4a1 > 0c0` | 99.5% |
|  | 4 | `0c0 > 4a1 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.9% |
| 0c0 4e | 1 | `0c0 > 4a1 > 0c0` | 60.5% |
|  | 2 | `0c0 > 4a1 > (0c0 > 4a1 > 0c0)` | 87.4% |
|  | 3 | `0c0 > 4a1 > 0c0 > 4a1 > 0c0` | 98.2% |
|  | 4 | `0c0 > 4a1 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 99.8% |
| 0c0 6e | 1 | `0c0 > 4a1 > 0c0 > 4a1 > 0c0` | 54.3% |
|  | 2 | `0c0 > 4a1 > 0c0` | 80.2% |
|  | 3 | `0c0 > 4a1 > (0c0 > 4a1 > 0c0)` | 96.5% |
|  | 4 | `0c0 > 4a1 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.6% |
| 0c0 8e | 1 | `0c0 > 4a1 > 0c0` | 77.9% |
|  | 2 | `0c0 > 4a1 > 0c0 > 4a1 > 0c0` | 93.8% |
|  | 3 | `0c0 > 4a1 > (0c0 > 4a1 > 0c0)` | 98.9% |
|  | 4 | `0c0 > 4a1 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | >99.9% |
| 2c5 0e | 1 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.6% |
|  | 2 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 97.1% |
|  | 3 | `2c5 > 2c4 > 2c3 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 98.4% |
|  | 4 | `2c5 > 4b4 > 4a3 > 4b2 > 4a1 > 0c0` | 99.7% |
| 2c5 2e | 1 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 94.9% |
|  | 2 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 97.7% |
|  | 3 | `2c5 > 2c4 > 2c3 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 98.7% |
|  | 4 | `2c5 > 4b4 > 4a3 > 4b2 > 4a1 > 0c0` | 99.7% |
| 2c5 4e | 1 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 95.7% |
|  | 2 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 98.0% |
|  | 3 | `2c5 > 4b4 > 4a3 > 4b2 > 4a1 > 0c0` | 98.9% |
|  | 4 | `2c5 > 2c4 > 2c3 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.8% |
| 2c5 6e | 1 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 94.8% |
|  | 2 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 97.3% |
|  | 3 | `2c5 > 4b4 > 4a3 > 4b2 > 4a1 > 0c0` | 98.6% |
|  | 4 | `2c5 > 2c4 > 2c3 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.5% |
| 2c5 8e | 1 | `2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 95.2% |
|  | 2 | `2c5 > 4b4 > (4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 97.9% |
|  | 3 | `2c5 > 2c4 > 2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 99.0% |
|  | 4 | `2c5 > 4b4 > 4a3 > 4b2 > 4a1 > 0c0` | 99.8% |
| 2c4 0e | 1 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 96.2% |
|  | 2 | `2c4 > 2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 98.0% |
|  | 3 | `2c4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 98.8% |
|  | 4 | `2c4 > 2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.6% |
| 2c4 2e | 1 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 94.9% |
|  | 2 | `2c4 > 2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 97.8% |
|  | 3 | `2c4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 98.9% |
|  | 4 | `2c4 > 2c3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 99.5% |
| 2c4 4e | 1 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 93.8% |
|  | 2 | `2c4 > 2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 97.6% |
|  | 3 | `2c4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 98.9% |
|  | 4 | `2c4 > 2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.6% |
| 2c4 6e | 1 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 94.3% |
|  | 2 | `2c4 > 2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 97.7% |
|  | 3 | `2c4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.0% |
|  | 4 | `2c4 > 2c3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 99.6% |
| 2c4 8e | 1 | `2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 95.2% |
|  | 2 | `2c4 > 2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 97.4% |
|  | 3 | `2c4 > 4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 98.9% |
|  | 4 | `2c4 > 2c3 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 99.4% |
| 0c3 0e | 1 | `0c3 > 4a2 > 4a1 > 0c0` | 85.6% |
|  | 2 | `0c3 > 4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 94.5% |
|  | 3 | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > 0c0` | 99.9% |
|  | 4 | `0c3 > 4a2 > 4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | >99.9% |
| 0c3 2e | 1 | `0c3 > 4a2 > 4a1 > 0c0` | 83.1% |
|  | 2 | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > 0c0` | 94.2% |
|  | 3 | `0c3 > 4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 99.5% |
|  | 4 | `0c3 > 4a2 > 4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.8% |
| 0c3 4e | 1 | `0c3 > 4a2 > 4a1 > 0c0` | 68.4% |
|  | 2 | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > 0c0` | 91.9% |
|  | 3 | `0c3 > 4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 99.2% |
|  | 4 | `0c3 > 4a2 > 4b3 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.7% |
| 0c3 6e | 1 | `0c3 > 4a2 > 4a1 > 0c0` | 84.9% |
|  | 2 | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > 0c0` | 96.9% |
|  | 3 | `0c3 > 4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 99.6% |
|  | 4 | `0c3 > 4a2 > 4a1 > 0c0 > 4a1 > 0c0` | 99.9% |
| 0c3 8e | 1 | `0c3 > 4a2 > 4a1 > 0c0` | 87.3% |
|  | 2 | `0c3 > 4a2 > 4b3 > 4a2 > 4a1 > 0c0` | 95.4% |
|  | 3 | `0c3 > 4a4 > 4b5 > (2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.8% |
|  | 4 | `0c3 > 4a2 > 4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | >99.9% |
| 4a2 0e | 1 | `4a2 > 4a1 > 4b2 > 4a1 > 0c0` | 56.9% |
|  | 2 | `4a2 > 4b3 > 4a2 > 4a1 > 0c0` | 84.0% |
|  | 3 | `4a2 > 4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 98.6% |
|  | 4 | `4a2 > 0c3 > 4a2 > 4a1 > 0c0` | 99.2% |
| 4a2 2e | 1 | `4a2 > 4b3 > 4a2 > 4a1 > 0c0` | 52.4% |
|  | 2 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 74.1% |
|  | 3 | `4a2 > 4a1 > 0c0` | 91.3% |
|  | 4 | `4a2 > 4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.3% |
| 4a2 4e | 1 | `4a2 > 4a1 > 0c0` | 67.8% |
|  | 2 | `4a2 > 4a1 > (0c0 > 4a1 > 0c0)` | 88.0% |
|  | 3 | `4a2 > 4b3 > 4a2 > 4a1 > 0c0` | 96.2% |
|  | 4 | `4a2 > 4b3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.8% |
| 4a1 0e | 1 | `4a1 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 67.1% |
|  | 2 | `4a1 > 0c0 > 4a1 > 0c0` | 94.7% |
|  | 3 | `4a1 > 0c0 > 4a1 > 0c0 > 4a1 > 0c0` | 98.8% |
|  | 4 | `4a1 > 4b2 > 4a1 > 0c0 > 4a1 > 0c0` | 99.8% |
| 4a1 2e | 1 | `4a1 > 0c0 > 4a1 > 0c0` | 86.5% |
|  | 2 | `4a1 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 96.6% |
|  | 3 | `4a1 > 0c0 > (4a1 > 0c0 > 4a1 > 0c0)` | 98.7% |
|  | 4 | `4a1 > 4b2 > 4a1 > 0c0 > 4a1 > 0c0` | >99.9% |
| 4a1 4e | 1 | `4a1 > 0c0 > 4a1 > 0c0` | 74.0% |
|  | 2 | `4a1 > 0c0` | 89.8% |
|  | 3 | `4a1 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 97.7% |
|  | 4 | `4a1 > 0c0 > (4a1 > 0c0 > 4a1 > 0c0)` | 99.2% |
| 2c3 0e | 1 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 72.6% |
|  | 2 | `2c3 > 4b2 > 4a1 > 0c0` | 93.2% |
|  | 3 | `2c3 > 4b2 > (4a1 > 0c0 > 4a1 > 0c0)` | 98.8% |
|  | 4 | `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.7% |
| 2c3 2e | 1 | `2c3 > 4b2 > 4a1 > 0c0` | 89.8% |
|  | 2 | `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 98.1% |
|  | 3 | `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.9% |
|  | 4 | `2c3 > 4b2 > 4a1 > 4b2 > 4a1 > 0c0` | >99.9% |
| 2c3 4e | 1 | `2c3 > 4b2 > 4a1 > 0c0` | 83.2% |
|  | 2 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 97.2% |
|  | 3 | `2c3 > 4b2 > (4a1 > 0c0 > 4a1 > 0c0)` | 99.5% |
|  | 4 | `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | >99.9% |
| 2c3 6e | 1 | `2c3 > 4b2 > 4a1 > 0c0` | 78.1% |
|  | 2 | `2c3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 96.7% |
|  | 3 | `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.7% |
|  | 4 | `2c3 > 4b2 > 4a1 > 4b2 > 4a1 > 0c0` | 99.9% |
| 2c3 8e | 1 | `2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 75.9% |
|  | 2 | `2c3 > 4b2 > 4a1 > 0c0` | 95.5% |
|  | 3 | `2c3 > 4b2 > (4a1 > 0c0 > 4a1 > 0c0)` | 99.1% |
|  | 4 | `2c3 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.7% |
| 0c4 0e | 1 | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 94.4% |
|  | 2 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | >99.9% |
| 0c4 2e | 1 | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 92.0% |
|  | 2 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | >99.9% |
|  | 3 | `0c4 > 4a3 > 4b2 > 4a1 > 4b2 > 4a1 > 0c0` | >99.9% |
|  | 4 | `0c4 > 4a3 > 0c4 > 4a3 > 4b2 > 4a1 > 0c0` | >99.9% |
| 0c4 4e | 1 | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 90.1% |
|  | 2 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 99.9% |
|  | 3 | `0c4 > 4a3 > 0c4 > 4a3 > 4b2 > 4a1 > 0c0` | >99.9% |
|  | 4 | `0c4 > 4a3 > 4b2 > 4a1 > 4b2 > 4a1 > 0c0` | >99.9% |
| 0c4 6e | 1 | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 87.1% |
|  | 2 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 99.8% |
|  | 3 | `0c4 > 4a3 > 0c4 > 4a3 > 4b2 > 4a1 > 0c0` | >99.9% |
|  | 4 | `0c4 > 4a3 > 4b2 > 4a1 > 4b2 > 4a1 > 0c0` | >99.9% |
| 0c4 8e | 1 | `0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 93.1% |
|  | 2 | `0c4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 99.9% |
|  | 3 | `0c4 > 4a3 > 0c4 > 4a3 > 4b2 > 4a1 > 0c0` | >99.9% |
| 4c3 0e | 1 | `4a3 > 4b2 > 4a1 > 0c0` | 76.5% |
|  | 2 | `4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 97.5% |
|  | 3 | `4a3 > 0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 99.4% |
|  | 4 | `4b3 > 4a2 > (4b3 > 4a2 > 4a1 > 0c0)` | 99.6% |
| 4c3 2e | 1 | `4a3 > 4b2 > 4a1 > 0c0` | 74.6% |
|  | 2 | `4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 96.8% |
|  | 3 | `4a3 > 0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 99.1% |
|  | 4 | `4b3 > 4a2 > (4b3 > 4a2 > 4a1 > 0c0)` | 99.4% |
| 4c3 4e | 1 | `4a3 > 4b2 > 4a1 > 0c0` | 70.7% |
|  | 2 | `4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 96.4% |
|  | 3 | `4a3 > 0c4 > 4a3 > 4b2 > 4a1 > 0c0` | 98.8% |
|  | 4 | `4b3 > 4a2 > (4b3 > 4a2 > 4a1 > 0c0)` | 99.3% |
| 4c4 0e | 1 | `4b4 > 4a3 > 4b2 > 4a1 > 0c0` | 67.7% |
|  | 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 93.2% |
|  | 3 | `4b4 > 2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.2% |
|  | 4 | `4b4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 99.7% |
| 4c4 2e | 1 | `4b4 > 4a3 > 4b2 > 4a1 > 0c0` | 72.1% |
|  | 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 94.3% |
|  | 3 | `4b4 > 2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.2% |
|  | 4 | `4b4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 99.9% |
| 4c4 4e | 1 | `4b4 > 4a3 > 4b2 > 4a1 > 0c0` | 73.8% |
|  | 2 | `4a4 > 4b5 > 2c4 > (2c3 > 4b2 > 4a1 > 0c0)` | 94.0% |
|  | 3 | `4b4 > 2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 99.2% |
|  | 4 | `4b4 > 4a3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 99.9% |
| 4b2 0e | 1 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 68.2% |
|  | 2 | `4b2 > 4a1 > 0c0` | 91.6% |
|  | 3 | `4b2 > 4a3 > 4b2 > 4a1 > 0c0` | 95.7% |
|  | 4 | `4b2 > 4a1 > 4b2 > 4a1 > 0c0` | 97.7% |
| 4b2 2e | 1 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 68.8% |
|  | 2 | `4b2 > 4a1 > 0c0` | 94.4% |
|  | 3 | `4b2 > 4a1 > 4b2 > 4a1 > 0c0` | 97.7% |
|  | 4 | `4b2 > 4a3 > 4b2 > 4a1 > 0c0` | 98.9% |
| 4b2 4e | 1 | `4b2 > 2c3 > 4b2 > 4a1 > 0c0` | 77.8% |
|  | 2 | `4b2 > 4a1 > 0c0` | 93.1% |
|  | 3 | `4b2 > 4a1 > 4b2 > 4a1 > 0c0` | 97.0% |
|  | 4 | `4b2 > 4a3 > 4b2 > 4a1 > 0c0` | 98.5% |
| 4b5 0e | 1 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 98.1% |
|  | 2 | `4b5 > 2c4 > 2c3 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0)` | 98.9% |
|  | 3 | `4b5 > 4a4 > (2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.4% |
|  | 4 | `4b5 > 2c4 > 4b3 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.8% |
| 4b5 2e | 1 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 98.0% |
|  | 2 | `4b5 > 4a4 > (2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 98.8% |
|  | 3 | `4b5 > 2c4 > 2c3 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.4% |
|  | 4 | `4b5 > 2c4 > (2c3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.8% |
| 4b5 4e | 1 | `4b5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0` | 98.1% |
|  | 2 | `4b5 > 4a4 > (2c5 > 2c4 > 2c3 > 4b2 > 4a1 > 0c0)` | 98.9% |
|  | 3 | `4b5 > 2c4 > 2c3 > (4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.5% |
|  | 4 | `4b5 > 2c4 > (2c3 > 4b2 > 2c3 > 4b2 > 4a1 > 0c0)` | 99.7% |

**The path sheets' top paths.** Per tab, the path with the largest share in *Optimal Niss-HTR Paths* and in *Sub-13 Optimal Niss-HTR Paths*, the sheet's share and mine (same counting rule, section 5):

| Tab | Top path in "Optimal Niss-HTR Paths" | Sheet | Mine | Top path in *Sub-13 …* | Sheet | Mine |
|---|---|---|---|---|---|---|
| 0c0 0e | `0c0 0e` | 96.1% | 42.7% | `0c0 0e` | 96.2% | 42.8% |
| 0c0 2e | `0c0 2e > 4a1 4e > 0c0 0e` | 79.6% | 66.5% | `0c0 2e > 4a1 4e > 0c0 0e` | 76.8% | 64.1% |
| 0c0 4e | `0c0 4e > 4a1 4e > 0c0 0e` | 56.5% | 47.6% | `0c0 4e > 4a1 4e > 0c0 0e` | 53.9% | 45.4% |
| 0c0 6e | `0c0 6e > 4a1 4e > (0c0 0e)` | 48.5% | 41.0% | `0c0 6e > 4a1 4e > (0c0 0e)` | 54.1% | 42.3% |
| 0c0 8e | `0c0 8e > 4a1 4e > (0c0 0e)` | 70.2% | 61.1% | `0c0 8e > 4a1 4e > (0c0 0e)` | 80.6% | 67.2% |
| 2c5 0e | `2c5 0e > 2c4 4e > 2c3 2e > (4b2 2e > 4a1 4e > 0c0 0e)` | 61.0% | 67.9% | `2c5 0e > 2c4 4e > 2c3 2e > (4b2 2e > 4a1 4e > 0c0 0e)` | 33.3% | 84.7% |
| 2c5 2e | `2c5 2e > 2c4 4e > 2c3 4e > (4b2 2e > 4a1 4e > 0c0 0e)` | 28.4% | 32.5% | `2c5 2e > 2c4 2e > 2c3 4e > 4b2 4e > 4a1 4e > 0c0 0e` | 18.5% | 4.8% |
| 2c5 4e | `2c5 4e > 2c4 4e > 2c3 2e > (4b2 2e > 4a1 4e > 0c0 0e)` | 22.7% | 26.2% | `2c5 4e > 2c4 4e > 2c3 2e > 4b2 2e > 4a1 4e > 0c0 0e` | 30.0% | 8.6% |
| 2c5 6e | `2c5 6e > 2c4 4e > 2c3 4e > (4b2 2e > 4a1 4e > 0c0 0e)` | 20.7% | 26.4% | `2c5 6e > 2c4 4e > 2c3 4e > 4b2 2e > 4a1 4e > 0c0 0e` | 23.5% | 10.0% |
| 2c5 8e | `2c5 8e > 2c4 4e > 2c3 2e > (4b2 2e > 4a1 4e > 0c0 0e)` | 52.6% | 59.8% | `2c5 8e > 2c4 4e > 2c3 2e > 4b2 2e > 4a1 4e > 0c0 0e` | 56.2% | 27.1% |
| 2c4 0e | `2c4 0e > 2c3 4e > 4b2 2e > 4a1 4e > 0c0 0e` | 59.3% | 67.8% | `2c4 0e > 2c3 4e > 4b2 2e > 4a1 4e > 0c0 0e` | 47.2% | 59.6% |
| 2c4 2e | `2c4 2e > 2c3 4e > (4b2 2e > 4a1 4e > 0c0 0e)` | 30.9% | 39.6% | `2c4 2e > 2c3 2e > 4b2 2e > 4a1 4e > 0c0 0e` | 21.6% | 21.2% |
| 2c4 4e | `2c4 4e > 2c3 4e > (4b2 2e > 4a1 4e > 0c0 0e)` | 29.8% | 33.4% | `2c4 4e > 2c3 2e > (4b2 2e > 4a1 4e > 0c0 0e)` | 24.4% | 29.0% |
| 2c4 6e | `2c4 6e > 2c3 4e > (4b2 2e > 4a1 4e > 0c0 0e)` | 37.4% | 42.9% | `2c4 6e > 2c3 2e > (4b2 2e > 4a1 4e > 0c0 0e)` | 19.7% | 28.9% |
| 2c4 8e | `2c4 8e > 2c3 4e > (4b2 2e > 4a1 4e > 0c0 0e)` | 71.9% | 75.4% | `2c4 8e > 2c3 4e > (4b2 2e > 4a1 4e > 0c0 0e)` | 59.4% | 67.1% |
| 0c3 0e | `0c3 0e > 4a2 4e > (4a1 4e > 0c0 0e)` | 83.5% | 84.4% | `0c3 0e > 4a2 4e > (4a1 4e > 0c0 0e)` | >99.9% | >99.9% |
| 0c3 2e | `0c3 2e > 4a2 4e > (4a1 4e > 0c0 0e)` | 59.0% | 77.9% | `0c3 2e > 4a2 4e > (4a1 4e > 0c0 0e)` | 97.0% | 98.9% |
| 0c3 4e | `0c3 4e > 4a2 4e > (4a1 4e > 0c0 0e)` | 68.1% | 67.3% | `0c3 4e > 4a2 4e > (4a1 4e > 0c0 0e)` | >99.9% | >99.9% |
| 0c3 6e | `0c3 6e > 4a2 4e > (4a1 4e > 0c0 0e)` | 75.4% | 80.4% | `0c3 6e > 4a2 4e > (4a1 4e > 0c0 0e)` | 93.2% | 99.5% |
| 0c3 8e | `0c3 8e > 4a2 4e > (4a1 4e > 0c0 0e)` | 86.0% | 86.5% | `0c3 8e > 4a2 4e > (4a1 4e > 0c0 0e)` | >99.9% | >99.9% |
| 4a2 0e | `4a2 0e > 4b3 4e > (4b2 2e > 4a1 4e > 0c0 0e)` | 27.7% | 27.8% | `4a2 0e > 4a1 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 35.4% | 50.8% |
| 4a2 2e | `4a2 2e > 4a1 4e > (0c0 0e)` | 34.8% | 34.5% | `4a2 2e > 4a1 4e > (0c0 0e)` | 37.2% | 39.6% |
| 4a2 4e | `4a2 4e > 4a1 4e > 0c0 0e` | 54.9% | 60.1% | `4a2 4e > 4a1 4e > 0c0 0e` | 46.4% | 53.3% |
| 4a1 0e | `4a1 0e > 0c0 4e > (4a1 4e > 0c0 0e)` | 36.7% | 34.9% | `4a1 0e > 0c0 4e > (4a1 4e > 0c0 0e)` | 37.2% | 35.6% |
| 4a1 2e | `4a1 2e > 4b2 2e > 4a1 4e > 0c0 0e` | 42.8% | 44.2% | `4a1 2e > 4b2 2e > 4a1 4e > 0c0 0e` | 27.9% | 34.3% |
| 4a1 4e | `4a1 4e > 0c0 0e` | 45.4% | 35.3% | `4a1 4e > 0c0 0e` | 53.8% | 37.9% |
| 2c3 0e | `2c3 0e > 4b2 4e > (4a1 4e > 0c0 0e)` | 41.5% | 43.4% | `2c3 0e > 4b2 4e > (4a1 4e > 0c0 0e)` | 47.3% | 45.7% |
| 2c3 2e | `2c3 2e > 4b2 2e > 4a1 4e > 0c0 0e` | 59.2% | 60.5% | `2c3 2e > 4b2 2e > 4a1 4e > 0c0 0e` | 51.3% | 50.9% |
| 2c3 4e | `2c3 4e > 4b2 2e > 4a1 4e > 0c0 0e` | 49.8% | 52.3% | `2c3 4e > 4b2 2e > 4a1 4e > 0c0 0e` | 44.6% | 44.3% |
| 2c3 6e | `2c3 6e > 4b2 2e > (4a1 4e > 0c0 0e)` | 53.9% | 57.3% | `2c3 6e > 4b2 2e > (4a1 4e > 0c0 0e)` | 53.8% | 52.8% |
| 2c3 8e | `2c3 8e > 4b2 4e > (4a1 4e > 0c0 0e)` | 46.4% | 45.5% | `2c3 8e > 4b2 4e > (4a1 4e > 0c0 0e)` | 39.8% | 40.8% |
| 0c4 0e | `0c4 0e > 4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 75.8% | 78.6% | `0c4 0e > 4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 76.1% | 80.2% |
| 0c4 2e | `0c4 2e > 4a3 2e > 4b2 2e > (4a1 4e > 0c0 0e)` | 51.6% | 72.6% | `0c4 2e > 4a3 2e > 4b2 2e > (4a1 4e > 0c0 0e)` | 43.0% | 67.7% |
| 0c4 4e | `0c4 4e > 4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 44.8% | 62.9% | `0c4 4e > 4a3 2e > 4b2 2e > (4a1 4e > 0c0 0e)` | 39.5% | 48.3% |
| 0c4 6e | `0c4 6e > 4a3 2e > 4b2 2e > (4a1 4e > 0c0 0e)` | 45.4% | 67.2% | `0c4 6e > 4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 36.8% | 61.2% |
| 0c4 8e | `0c4 8e > 4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 78.2% | 83.5% | `0c4 8e > 4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 95.2% | 89.1% |
| 4c3 0e | `4a3 0e > 4b2 4e > (4a1 4e > 0c0 0e)` | 50.5% | 59.1% | `4a3 0e > 4b2 4e > (4a1 4e > 0c0 0e)` | 63.9% | 65.7% |
| 4c3 2e | `4a3 2e > 4b2 2e > (4a1 4e > 0c0 0e)` | 44.2% | 51.6% | `4a3 2e > 4b2 2e > (4a1 4e > 0c0 0e)` | 40.5% | 56.2% |
| 4c3 4e | `4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 38.9% | 42.2% | `4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 39.2% | 43.4% |
| 4c4 0e | `4b4 0e > 4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 37.4% | 57.8% | `4b4 0e > 4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 50.0% | 89.1% |
| 4c4 2e | `4b4 2e > 4a3 2e > 4b2 2e > (4a1 4e > 0c0 0e)` | 19.9% | 37.2% | `4a4 2e > 4a3 2e > 4b2 2e > (4a1 4e > 0c0 0e)` | 30.8% | 34.5% |
| 4c4 4e | `4b4 4e > 4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 17.6% | 30.1% | `4a4 4e > 4a3 4e > 4b2 2e > (4a1 4e > 0c0 0e)` | 45.8% | 35.6% |
| 4b2 0e | `4b2 0e > 4a1 4e > 0c0 0e` | 36.3% | 37.1% | `4b2 0e > 4a1 4e > (0c0 0e)` | 41.1% | 38.3% |
| 4b2 2e | `4b2 2e > 4a1 4e > 0c0 0e` | 50.8% | 49.0% | `4b2 2e > 4a1 4e > 0c0 0e` | 47.7% | 44.0% |
| 4b2 4e | `4b2 4e > 4a1 4e > 0c0 0e` | 32.5% | 28.6% | `4b2 4e > 4a1 4e > 0c0 0e` | 30.7% | 26.4% |
| 4b5 0e | `4b5 0e > 2c4 4e > 2c3 2e > (4b2 2e > 4a1 4e > 0c0 0e)` | 42.9% | 49.3% | `4b5 0e > 2c4 4e > 2c3 2e > 4b2 2e > 4a1 4e > 0c0 0e` | 37.5% | 27.9% |
| 4b5 2e | `4b5 2e > 2c4 4e > (2c3 4e > 4b2 2e > 4a1 4e > 0c0 0e)` | 24.7% | 29.6% | `4b5 2e > 2c4 4e > 2c3 4e > 4b2 2e > 4a1 4e > 0c0 0e` | 30.8% | 16.7% |
| 4b5 4e | `4b5 4e > 2c4 4e > (2c3 4e > 4b2 2e > 4a1 4e > 0c0 0e)` | 23.5% | 27.5% | `4b5 4e > 2c4 2e > (2c3 2e > 4b2 2e > 4a1 4e > 0c0 0e)` | 13.3% | 9.8% |

**rodneykinney's table** for FakeMMAP's bound: per subset × edges and target M, "reduce to 1q in at most R moves" with nothing read off the DR (A and B the subset's shortest linear HTR, worst case over the subset's corner paths): the formula of FakeMMAP's message without its first term (C the subset's shortest linear HTR) / the exact model (C the shortest NISS HTR) / the longest reduction any sampled finish of at most M needed. Sampled, 25,000 per subset × edges; a blank cell means no sampled finish reaches that M.

| Subset | M = 10: formula / exact / needed | M = 11 | M = 12 |
|---|---|---|---|
| 0c0 0e | 11 / 8 / 7 | 12 / 9 / 8 | 13 / 10 / 8 |
| 0c0 2e | 9 / 7 / 6 | 10 / 8 / 8 | 11 / 10 / 9 |
| 0c0 4e | 9 / 8 / 6 | 10 / 8 / 8 | 11 / 9 / 9 |
| 0c0 6e | 7 / 7 / 6 | 9 / 8 / 8 | 10 / 9 / 9 |
| 0c0 8e | 9 / 7 / 6 | 10 / 8 / 6 | 11 / 9 / 7 |
| 2c5 0e |  | 8 / 8 / 7 | 10 / 9 / 8 |
| 2c5 2e | 7 / 7 / 7 | 8 / 8 / 8 | 10 / 9 / 8 |
| 2c5 4e | 7 / 7 / 7 | 8 / 8 / 8 | 10 / 9 / 8 |
| 2c5 6e | 7 / 7 / 6 | 8 / 8 / 7 | 10 / 9 / 8 |
| 2c5 8e |  | 8 / 8 / 7 | 10 / 9 / 8 |
| 2c4 0e | 8 / 7 / 6 | 9 / 8 / 8 | 10 / 9 / 9 |
| 2c4 2e | 7 / 6 / 6 | 9 / 8 / 8 | 10 / 9 / 9 |
| 2c4 4e | 7 / 6 / 6 | 9 / 8 / 8 | 10 / 9 / 9 |
| 2c4 6e | 7 / 6 / 6 | 9 / 8 / 8 | 10 / 9 / 9 |
| 2c4 8e | 6 / 6 / 5 | 9 / 8 / 6 | 10 / 9 / 8 |
| 0c3 0e | 5 / 2 / 2 | 8 / 6 / 3 | 10 / 9 / 4 |
| 0c3 2e | 6 / 3 / 3 | 9 / 8 / 4 | 10 / 9 / 7 |
| 0c3 4e | 5 / 2 / 2 | 6 / 4 / 3 | 10 / 9 / 7 |
| 0c3 6e | 6 / 3 / 3 | 8 / 6 / 4 | 10 / 9 / 7 |
| 0c3 8e | 5 / 2 / 2 | 8 / 6 / 3 | 10 / 9 / 4 |
| 4a2 0e | 6 / 6 / 5 | 9 / 8 / 6 | 10 / 9 / 8 |
| 4a2 2e | 7 / 6 / 6 | 9 / 8 / 8 | 10 / 9 / 9 |
| 4a2 4e | 9 / 7 / 6 | 10 / 8 / 8 | 11 / 10 / 9 |
| 4a1 0e | 8 / 7 / 7 | 10 / 9 / 8 | 11 / 9 / 9 |
| 4a1 2e | 8 / 7 / 7 | 10 / 9 / 8 | 11 / 9 / 8 |
| 4a1 4e | 11 / 8 / 7 | 12 / 9 / 8 | 13 / 9 / 8 |
| 2c3 0e | 7 / 7 / 6 | 8 / 8 / 7 | 10 / 9 / 8 |
| 2c3 2e | 9 / 7 / 7 | 10 / 8 / 8 | 11 / 9 / 8 |
| 2c3 4e | 9 / 7 / 7 | 10 / 8 / 8 | 11 / 9 / 8 |
| 2c3 6e | 8 / 7 / 7 | 9 / 8 / 8 | 11 / 9 / 8 |
| 2c3 8e | 7 / 7 / 6 | 8 / 8 / 7 | 10 / 9 / 8 |
| 0c4 0e | 8 / 7 / 7 | 9 / 8 / 8 | 10 / 9 / 9 |
| 0c4 2e | 8 / 7 / 5 | 9 / 8 / 8 | 10 / 9 / 9 |
| 0c4 4e | 8 / 7 / 5 | 9 / 8 / 8 | 10 / 9 / 9 |
| 0c4 6e | 7 / 4 / 4 | 9 / 8 / 8 | 10 / 9 / 9 |
| 0c4 8e |  | 8 / 5 / 4 | 9 / 9 / 8 |
| 4c3 0e | 8 / 7 / 7 | 9 / 8 / 8 | 10 / 9 / 8 |
| 4c3 2e | 8 / 7 / 6 | 9 / 8 / 8 | 11 / 9 / 8 |
| 4c3 4e | 8 / 7 / 7 | 10 / 8 / 8 | 11 / 9 / 8 |
| 4c4 0e | 7 / 4 / 4 | 9 / 8 / 5 | 10 / 9 / 8 |
| 4c4 2e | 7 / 5 / 5 | 9 / 8 / 8 | 10 / 9 / 9 |
| 4c4 4e | 7 / 5 / 5 | 9 / 8 / 8 | 10 / 9 / 9 |
| 4b2 0e | 9 / 7 / 7 | 10 / 8 / 8 | 11 / 9 / 9 |
| 4b2 2e | 10 / 7 / 6 | 11 / 8 / 8 | 12 / 9 / 9 |
| 4b2 4e | 9 / 7 / 6 | 10 / 8 / 8 | 11 / 9 / 9 |
| 4b5 0e | 7 / 7 / 7 | 8 / 8 / 8 | 10 / 9 / 8 |
| 4b5 2e | 7 / 7 / 6 | 8 / 8 / 8 | 10 / 9 / 8 |
| 4b5 4e | 7 / 7 / 7 | 8 / 8 / 8 | 10 / 9 / 8 |

**Late switches**: share of DRs whose shortest HTR among all readings of all optimal finishes is reached only by readings that switch after 3 or more moves, or after 4 or more (sampled, 25,000 per subset × edges, edges pooled by size):

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

**The model.** The DR group ⟨U, D, R2, L2, F2, B2⟩ with the first study's exact table of the optimal finish of all 19,508,428,800 DR states (proved in Lean there) and of the optimal leave-slice. Subsets are the first study's 48 (corner subset from the bad corners, the quarter turns the corners need and the 4a/4b shape; bad edges counted up to turning a layer). A Rust tool samples states uniformly within each subset × edges and enumerates every finish of the optimal length and one longer (both orders of commuting moves), using the exact table to prune; each finish is read at every split, either side first, and its route, HTR length and quarter-turn counts recorded. Shortest HTRs (normal, inverse, NISS) come from an exact search. Reductions are counted from coset tables. About an hour on four cores, at most 5 GB per job. Fixed targets of 10 to 12 use finishes up to max(optimal + 1, min(optimal + 2, 12)) moves.

**What checks it.**

- The optimal distribution of every subset equals the first study's and Joba's in all 473 cells; DougCube's 663,552 HTR states give mean 10.13432557 exactly; Joba's DR-to-HTR lengths per subset agree.
- An independent sticker model (a 54-sticker cube built from geometry, with its own subset labels, HTR test and NISS reading) re-reads every optimal finish of 1,240 states (1,000 random DR scrambles and 5 per subset × edges from the sample): every finish replayed, every route and HTR length of every reading equal to the tool's. nissy 2.0.8 lists the same optimal finishes for all 1,240.
- Reduction counts from the coset tables equal a brute-force enumeration of every pair of sequences for reductions of up to 5 moves on 4,800 states (the first 100 of every subset × edges), and up to 7 moves on 40 states of 0c0 (the brute force for 7 moves was stopped there), which is why counts for 7 moves are not reported. Which reductions find the optimal comes from an exact search, not from the counts.
- The leave-slice maximum of 4a1 4e (15) is a count over the first study's exact leave-slice table, every state.
- A Lean 4 certificate in the study's folder recomputes the small exact tables from its own cube model and proves they equal the study's: the 663,552 HTR states, the corner quarter-turn counts and subsets of all 40,320 corner arrangements, the shortest linear HTR of every subset (all 29,400 HTR cosets), FakeMMAP's α for every corner path used, the *5/6 fake* count, the bare-qt reductions of 3qt and 4qt cases, and the 2qt(a)/(b) labels of Aedan Bryant's and the *Extra Quarter-Turn Stats* sheets from their own example triggers.
- Every move sequence in this write-up, the errata and the worked examples is replayed on the sticker model (the examples page states its count).

## Docs referred to

- [*Sub-13 Optimal Niss-HTR Paths*](https://docs.google.com/spreadsheets/d/1etiCnl6U-OHQAjEZIVIlk9iE64OXK3lrCyy14TLE_wE), forwarded by Daichi; [*Optimal Niss-HTR Paths*](https://docs.google.com/spreadsheets/d/1D4qUhLOsJrwsBEzUVfmnLikuQNNB_eSZiPq-nS8KPN4), posted by deven. The maker of the data is not stated.
- Levi Gibson, [*allcases*](https://docs.google.com/spreadsheets/d/1Vo6XzCFtJ-HEAuaBmk_pac-sJ3TbxEBb7BKsRJ_2wpA), [*Extra Quarter-Turn Stats (By HTR Subset)*](https://docs.google.com/spreadsheets/d/1fPCjS1ZQlP_Munut9MQkSbsL3CEdtT3LC5h3R8OMHGw), [*DR Bounding*](https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA).
- Aedan Bryant, [*HTR Subset Stats*](https://docs.google.com/spreadsheets/d/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0).
- rodneykinney, [*DR Finish Move Counts*](https://docs.google.com/spreadsheets/d/1tv8rwo2GF9IWuywFTnde_YlikIPBQvHqW9pysNG6BPM) and [*Advanced DR Bounding [Beta]*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0).
- DougCube, [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo).
- Yura Riabov, [*Hitchhiker’s Guide to HTR*](https://docs.google.com/document/d/1_NMlyPh2Ifd1E0ivos-15Sp-by-KPxoOsj9JD4pJuHI).
- Joba's exact optimal distribution per subset: a text file posted in #fmc-theory ([17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406633631165714492)).
- My first study, [*Judging a DR by hand*](../judging-a-dr/).
- nissy 2.0.8, by Sebastiano Tronto ([nissy.tronto.net](https://nissy.tronto.net)), used for the cross-checks.
