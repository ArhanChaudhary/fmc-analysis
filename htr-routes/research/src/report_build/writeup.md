# Which HTR routes to try from a DR

Given a DR, which routes to HTR should you try, and in what order, to find the optimal finish? For each of the 48 subsets I sampled {= n(25000) =} uniformly random DR states (subset × bad edges, so {= n(1200000) =} in all) and solved each one exactly: every optimal finish and every finish one move longer, read in every way NISS allows (switch after any move, either side first), and the same for the DR with its last move turned the other way. From that come ordered checklists of routes per subset, how long the HTRs on them are, how DR bounding compares, and whether FakeMMAP's reduction-length bound holds and prunes. Everything a finish length rests on is the first study's exact table of all 19,508,428,800 DR states; where a number is exact over all states it says so, otherwise it is a sample of {= n(25000) =} states per subset × edges (a share's standard error is at most {= SE(0.5, 25000) =} points per subset × edges, {= SE(0.5, 75000) =} per corner subset) unless a smaller sample is named.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion). Docs and sheets are listed with links at the end.

**This builds on** what the server already had:

- **The two path sheets.** [*Sub-13 Optimal Niss-HTR Paths*](https://docs.google.com/spreadsheets/d/1etiCnl6U-OHQAjEZIVIlk9iE64OXK3lrCyy14TLE_wE), forwarded by Daichi ([[D18364]]), and [*Optimal Niss-HTR Paths*](https://docs.google.com/spreadsheets/d/1D4qUhLOsJrwsBEzUVfmnLikuQNNB_eSZiPq-nS8KPN4), posted by deven ([[D19660]]): for every subset × edges, the share of states whose optimal goes through each chain of corner subsets, NISS switches in brackets ("note that you can't add percentages because it counts all distinct paths from each state", [[D19661]]). Neither says how it was made. Section 5 reconstructs it.
- **Daichi's cheat sheet** ([[D18340]]: "to summarize, I think this is meta"), which turns the sub-13 sheet into a route list per subset ("It doesn't capture EVERYTHING, but I decided that checking these will capture a great portion of those", [[D18343]]). It is graded in section 10.
- **Levi Gibson's sheets and doc** (beef beans on Discord, posted as levitatingmagician): [*allcases*](https://docs.google.com/spreadsheets/d/1Vo6XzCFtJ-HEAuaBmk_pac-sJ3TbxEBb7BKsRJ_2wpA) ("What paths are most common for optimal DR solutions", [[D8290]]), the [*Extra Quarter-Turn Stats (By HTR Subset)*](https://docs.google.com/spreadsheets/d/1fPCjS1ZQlP_Munut9MQkSbsL3CEdtT3LC5h3R8OMHGw) ([[T2844]]), and [*DR Bounding*](https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA) ([[D9018]]), the method section 8 measures.
- **Aedan Bryant's [*HTR Subset Stats*](https://docs.google.com/spreadsheets/d/17iChOoeB205t3wHTXMLrjM9si2vtxRgFeYR2z3pn1i0)** ([[T621]]): 1,000 states per subset, mean optimal against shortest linear and NISS HTR.
- **Joba's exact optimal distribution per subset** ([[T9115]]: "This is not sampled, I looked at all 19508428800 DR states"), which the first study and this one reproduce cell for cell, and **DougCube's** [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo) ([[N2397]]) with the finish of all 663,552 HTR states ("the *expected value* is 10.13", [[D14065]]), also reproduced exactly.
- **rodneykinney's** [*DR Finish Move Counts*](https://docs.google.com/spreadsheets/d/1tv8rwo2GF9IWuywFTnde_YlikIPBQvHqW9pysNG6BPM) ([[T274]]), the corner-skeleton *normal forms* ([[T10436]]) and [*Advanced DR Bounding [Beta]*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0) ([[T11953]]).
- **FakeMMAP's** reduction-length bound and multi-qt lower bounds ([[T11501]], [[T11502]], [[T11503]]), with FakeMMAP's own caveat on the lower bounds, "I don't know how useful these bounds really are, I have to put in the numbers to see if there are situations where the typical bound is M \geq 11, rather than M \geq 7 lol." ([[T11504]]), and rodneykinney's request for per-case tables ([[T11512]]). Section 9 is that test.
- **JTuu's** 2c3 2e simulation of linear HTRs against bounding ([[T5744]]), **Zagros's** eight-step 4b2 order ([[D15884]]), **Lewis Isom's** 4a2 list ([[T6743]]) and 2c3 extension list ([[T7116]]), Yura Riabov's 4b2 4e order and rogo's question about it ([[D6409]], [[D6422]]), and Jay's and rodneykinney's 3qt checks ([[T328]], [[T333]]).
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

{{CONTENTS}}

---

## 1. The short version

{{SEC_SHORT}}

---

## 2. What was asked

{{SEC_ASKED}}

---

{{SEC_DEFS}}

---

{{SEC_CHECK}}

---

{{SEC_DOCS}}

---

{{SEC_HTR}}

---

{{SEC_BOUND}}

---

{{SEC_FAKE}}

---

{{SEC_HAND}}

---

{{SEC_CLAIMS}}

---

{{SEC_LIMITS}}

---

{{APP}}
