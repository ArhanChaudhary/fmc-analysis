# When to switch an EO

You have an EO and an RZP, and you're deciding whether to switch: go to the inverse, keep the EO, and look for a short DR there. I put a number on every switch rule the server uses and look for better ones you can check at the table. The best one I found is a count, not a feature: how many turns of the side faces the DR needs when U and D turns are free. For 4c4e that is the number of half turns to two bars, and it runs from a certain sub-7 to a certain miss. The target is the usual one: a DR in 6 or less on the switched side (sub-7), EO kept. I solved every EO-solved state for one EO axis and one DR axis exactly (1,082,565 states) and graded the rules on three populations: those uniform states (what every existing table uses), the states an RZP actually reaches (counted exactly), and 121,527,134 real attempts (every EO of up to 6 moves on 6,000 uniformly random scrambles, with every RZP after it to a total of 4, 5 or 6 moves). The real attempts are a sample, with a share's standard error taken from batches of scrambles; everything else is exact.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion). Docs and sheets are listed with links at the end.

**This builds on** what the server already had:

- **Cale's [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0)** and its [last-move version](https://docs.google.com/spreadsheets/d/1_2PmFv1KyBX335SjSb4oweS0sx804fIhbuP50D-gBj4): the EO to DR table per DRM. Cale also gave the observation that makes ARM a NISS tool: "the number of axially reduced pieces is always equal between one axis on normal and the other on inverse" ([3 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1213932643188473896)).
- **Louis's [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs)** ([27 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1222749709039435839)) with its code ([github.com/LouisSart/DRM-ARM-stats](https://github.com/LouisSart/DRM-ARM-stats)): every DRM × ARM cell exactly.
- **rodneykinney's** two-bar target for 4c4e, which the half-turn count here is built on ("The final trigger must have two full “bars” formed with the bad corners and edges.", with half turns as "an opportunity to form a pair for free", [*DR - 4c4e Theory*](https://docs.google.com/document/d/1DsxAAB2WRfpgDR-VWZZrXq2W4y_YMXBufRRYNLAGGoU)), the corner cases of the same doc (4a, 4b, 4c, 4d, "based on how the bad corners are split between the HTR orbits"), [*DRM corner variant+pair stats*](https://docs.google.com/spreadsheets/d/174ClwBFl-T2zJAq8MVyK1bKsIIuzxQU0_XmQGv82LPQ) ([13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383069263530692730)), the [*DRM Subsets*](https://docs.google.com/document/d/1AUQVrecEFZyR6okXAyJgtQZA-A0AJmAUevhJZlQMjAs) doc and [decision trees](https://rodneykinney.github.io/DRM-ARM-stats/drm_trees/), [*DRM Subsets Meta*](https://docs.google.com/document/d/1Jnd1Qy_6b1W5dR5fZQScloMoMPR2LCAF7VPrgeTaRgg), the older [*Domino Setup Theory*](https://docs.google.com/document/d/1Z3O8BY1LbAMF6m55ufXtSdtBVwSJpMArtRrDT-p_CwM) and [*Axial Reduction Theory*](https://docs.google.com/document/d/1TomrUJ9XWAQXBp7ghSB-iXs1WpPm20FGUw5OBoKgn7g). The side-pair rule ("2 side pairs counts as one top pair", [29 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1411128846069010586)) and "1.5+ pairs" ([30 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1411385789891350698)) are rodneykinney's. *DR - 4c4e Theory* is also where section 4 starts from: "The final trigger must have two full “bars” formed with the bad corners and edges.", with a side half turn as "an opportunity to form a pair for free" and "An additional 0-2 moves may be needed to solve the E slice."
- **Evan's** sampled [*4c4e ARM subtype stats*](https://docs.google.com/spreadsheets/d/1PAVonITR4HLBMml1-uxJwGRwHIoRWIGdNsK-A_KG_yA) and [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk).
- **Fanti's** rule sets with their measured performance (*armpairs_1.txt*, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069)), **Radek B's** tables from Louis's data, and **Levi Gibson's** (beef beans on Discord) [*Sub-7 simulations*](https://docs.google.com/spreadsheets/d/1Nqr2yICQqXuKrs1pkXWizsYw7-OU6FU4F7hzaE7pN2E).
- **The hand rules** of Yura Riabov, tseitsei89, wen, Jay, Noah Swor, Lewis Isom, caycala, compLex, Daichi, Zagros and Fanti; **torchlight's** point that an RZP biases the case it reaches ([8 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215720321995382867)); and **wen's** pair tracing in the [*Hitchhiker's Guide to DR*](https://docs.google.com/document/d/1E_5wSKvQFXXZY4f3xLM76qMUrVGp9Pe7vgotS0X-T4U).
- **My own EO-to-DR study** ([*EO to DR, and scramble to DR*](../eo-to-dr/)): the exact EO to DR distance of every EO-solved state, by DRM, with the EO's last turn free, the other DR axis and the inverse.

**What this adds**:

- **The two-ring picture**: U and D turns never change a pair, so a switched case is two rings and four E-slice places, a half turn swaps a row between the rings, and a quarter turn has a one-line rule. It is exact for every case.
- **For 4c4e, half turns to two bars**: 0 or 1 is a certain sub-7, 2 is 72.1%, 3 is 16.0%, 4 or 5 is 1.7%. How to count it from a pair trace, and what it costs.
- **For every DRM, side turns**: 2 or fewer is a certain sub-7, and 3 with no extra quarter turn is the switch group. It splits every card's groups, 7c8e with 5-6 pairs into 95.4% and 33.8%.
- **One switch card per DRM for a pair trace alone**: a rule you check by tracing, with the sub-7 share of each verdict and how much of the DRM it settles. Each card is the best cheap rule the search found, and it holds up on the real attempts.
- **For 4c4e, a better pair rule than pairs or ARM**: count the paired edges, then look at edge ARM. It settles about twice as many cases as either one.
- **Three new readings from the normal side**, each checked on 20,000 random cubes: the two rings with their holes, side pairs on the inverse, and edge ARM on the inverse without switching axes.
- **What a real RZP changes**: the RZP bias is gone once you switch, so the uniform tables are exactly right for switched cases. After a switch the RZP's last turn is worth nothing and the EO's last turn very little.
- **Every existing rule graded** the same way (how much it switches, how often that's a sub-7, how many sub-7s it throws away), on the uniform states and on the real attempts.
- **The claims checked**, the sheets reproduced cell by cell, and an [errata](errata.html) page with the one correction.

**Terms**, as the server uses them. *Switch* means NISS: after EO + RZP you go to the inverse and keep the EO ("switches means that after you go a certain path, you NISS?", "yeah", [14 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515647467691970581), [14 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1515649177718231051)). *DRM* is the number of bad corners and bad edges, corners first (4c4e = 4e4c), counting all edges out of DR. *ARM* is two digits, corners then edges (21 = AR-2c1e). *Pairs* are top pairs, *side pairs* are E-slice pairs, *4a* to *4d* are rodneykinney's corner cases. *Sub-7* means a DR in at most 6 moves, keeping the EO (U, D, R, L, F2, B2 for an F/B EO). New here: a *ring* is the 8 places of the U or D layer, a *row* is the corner, edge, corner of a layer on one side face, a bad corner *points* at the edge place it would pair with, a *hole* is an E-slice place holding a U/D edge, *side turns* are the turns of R, L, F and B in a DR, and *half turns to two bars* is the 4c4e count of section 4. Section 3 has the full definitions. The rules are read on the switched side; section 7 says how to see each feature on normal before you switch.

**How to read it.**

- **Start with [section 1](#1-the-short-version)**, the short version: what is new, then what it confirms or corrects. If you read one thing after it, make it [section 4](#4-two-rings-count-the-half-turns-4c4e): the ring picture and the half-turn count.
- **The [worked examples](examples.html)** go with it: 200 real attempts from random scrambles, each with what you'd trace on normal (the rings included), the half-turn or side-turn count, the card's verdict, and the optimal DR after the switch, answers folded away. **The [errata](errata.html)** have the one statement from the server that the numbers go against, with an example.
- **Sections 5 and 6** are the other DRMs and the cards for a pair trace alone. **Sections 8 to 13** are the details behind section 1. Anything marked **computer only** is an answer key, not advice: it can't be checked at the table.
- **✓ after a number: proved in Lean**, recounted on a Lean model of the cube, not only computed. [Appendix B](#appendix-b-how-it-was-computed-and-what-checks-it) lists what is proved and what is only computed.

---

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | What is new, then what it confirms or corrects, one line each. |
| [2. What was asked](#2-what-was-asked) | The questions, quoted, with where each is answered. |
| [3. Definitions](#3-definitions) | Switched case, sub-7, DRM, ARM, pairs, paired edges, corner case, rings, rows, holes, half turns to two bars, side turns, verdict bands, populations. |
| [4. Two rings: count the half turns (4c4e)](#4-two-rings-count-the-half-turns-4c4e) | **The main result.** The ring picture, what each turn does to it, half turns to two bars, its bands, how to count, what the U/D turns add. |
| [5. Every DRM: count the side turns](#5-every-drm-count-the-side-turns) | Side turns for all DRMs: the certain class, quarter turns against half turns, the trigger cases, one half turn away, crossed with the cards. |
| [6. The switch cards, DRM by DRM](#6-the-switch-cards-drm-by-drm) | What a pair trace alone gives. Per DRM: what to check, the share of each verdict with its sub-7 rate, by RZP length; the your-call groups split. |
| [7. Reading the switched case from normal](#7-reading-the-switched-case-from-normal) | The two rings and the holes, corner and edge ARM, pairs, paired edges, side pairs and corner case, each read before switching, with the checks. |
| [8. Real RZPs: does the uniform table apply after a switch?](#8-real-rzps-does-the-uniform-table-apply-after-a-switch) | The RZP bias, gone after a switch; RZP length; the last RZP and EO turns; the second axis. |
| [9. The existing rules, graded](#9-the-existing-rules-graded) | Every server rule: how much it switches, precision, recall, sub-7s thrown away, on exact cases and real attempts. |
| [10. What each feature adds](#10-what-each-feature-adds) | The half-turn count against ARM, pairs, corner case and paired edges; wen's 2 of 3; bars; unpaired corners; side pairs. |
| [11. Computer-only rules: the answer key](#11-computer-only-rules-the-answer-key) | The rule search over pair-trace features, the full setup distance, 8c8e, the low DRMs, information measures. |
| [12. The sheets, reproduced](#12-the-sheets-reproduced) | Which published numbers match, the two that don't, and Fanti's any-turn figures. |
| [13. The claims, checked](#13-the-claims-checked) | Each checkable statement from the server, with the verdict. |
| [14. What this does not cover](#14-what-this-does-not-cover) | Limits. |
| [Appendix A: full tables](#appendix-a-full-tables) | Every ring picture with 2 swaps or fewer, U/D turns per half-turn count, side-turn setups on the real attempts, 4c4e by ARM and paired edges, bars, 4c2e and 8c8e details, EO to DR by DRM with the options. |
| [Appendix B: how it was computed, and what checks it](#appendix-b-how-it-was-computed-and-what-checks-it) | Model, the ring picture, populations, nissy, unit tests, rodneykinney's code, the NISS checks, Lean. |
| [Docs referred to](#docs-referred-to) | Links. |

---

## 1. The short version

The question is whether there are switch guidelines, checkable at the table, that get closer to 100% or 0% sub-7 than ARM, DRM, pairs and the corner case do. There are, once you count the right thing. A U or D turn never makes or breaks a pair, so judge the setup as if U and D turns were free and count only the turns of the side faces. For 4c4e that is the number of half turns to two bars: at 0 or 1 a sub-7 is certain, at 2 it is 72.1% ✓, at 3 it is 16.0% ✓, at 4 it is 1.7% ✓ and at 5 never. By hand you can read the top of that scale (the 2s and below, with 2 or more pairs), not the bottom: telling a 3 from a 4 takes a search. All the rules are about the case on the switched side; section 7 shows how to see it on normal before you switch.

**What is new here**

**A switched case is two rings.** Forget how the U and D layers are turned. Each layer is then a ring of 8 places, with its bad edges and its bad corners, and every bad corner points along the ring at the edge place it would pair with. Between the rings sit the four E-slice places. On that picture (section 4.1):

- U and D turns do nothing.
- A half turn swaps one *row* (corner, edge, corner on one side face) between the two rings, any row of U with any row of D, and swaps the two E-slice places of the face you do it on.
- An R or L quarter turn moves the face's four corners one step: a good corner comes out pointing at the face's edge, one that pointed at it comes out good, one pointing away stays pointing away.

The three rules hold on every one of the 1,082,565 cases ✓.

**4c4e: count the half turns to two bars.** The two-bar target is rodneykinney's (*DR - 4c4e Theory*, section 4); what is new is counting the half turns to it exactly, with U and D turns free, and measuring what the count is worth. A 4c4e is one quarter turn from DR when each ring has a bar and the two holes (the U/D edges in the E slice) are on one R or L face. The count is the fewest half turns that get there, U and D turns free. One row per count, with its share of 4c4e, its sub-7 rate and the share of all of 4c4e's sub-7 cases it holds (section 4.3):

| Half turns to two bars | Verdict | Share of 4c4e | Sub-7 rate | Share of 4c4e's sub-7s |
|---|---|---|---|---|
| 0 or 1 | **switch**, certain | 1.0% ✓ | 100% ✓ | 5.3% ✓ |
| 2 | **switch** | 13.2% ✓ | 72.1% ✓ | 49.4% ✓ |
| 3 | **your call** | 51.0% ✓ | 16.0% ✓ | 42.3% ✓ |
| 4 or 5 | **discard** | 34.8% ✓ | 1.7% ✓ | 3.0% ✓ |

Against the best rule a pair trace gives, the paired-edge card further down: its switch group is 15.5% ✓ of 4c4e at 59.9% ✓, this one is 14.2% ✓ at 74.1% ✓. Its discard group throws away 18.0% ✓ of the sub-7s, this one 3.0% ✓. And the card's own groups split: both edges paired is 80.0% ✓ with 2 half turns or fewer and 28.9% ✓ with 3.

**What of that you can read by hand.** The switch end, not the discard end. With 2 or more pairs the count can be read (below), and that is where the 2s are. With 0 or 1 pair the reading only says *3 or more*: it can't tell a 3 from a 4, and 97.8% of the cases at 4 or 5 have 0 or 1 pair. So the 1.7% row is an answer key (**computer only**, unless you search for it), and for the low end the paired-edge card further down is still the tool. What a hand reading gives, one row per group, with its share of 4c4e and its sub-7 rate:

| What you see (4c4e) | How you read it | Share of 4c4e | Sub-7 rate |
|---|---|---|---|
| 2 or more pairs, 2 half turns or fewer | the count | 12.4% | 74.1% |
| 2 or more pairs, 3 half turns or more | the count | 13.6% | 21.1% |
| 1 pair or none, one bad edge paired with edge ARM 1 | the card: your call | 26.3% | 17.2% |
| 1 pair or none, the rest | the card: discard | 47.7% | 5.5% |

Against the card alone (15.5% at 59.9%, 32.5% at 20.0%, 52.0% at 6.7%): the switch group goes from 59.9% to 74.1%, and the discard group is about what it was.

The count is the larger of two readings ✓ (section 4.2):

- *Row swaps*: the fewest row swaps that leave a bar in each ring.
- *The holes*: 0 if the two holes are on one R/L face, 1 if diagonal, 2 if on one F/B face.

**How to count the row swaps** (section 4.4). There is no formula, and I say why there. Pairs tell you where to look:

- **4 pairs**: 0, or 1 if both bars are in one layer.
- **3 pairs**: 1, plus 1 if the unpaired corner is in the layer of the edge that lacks it, plus 1 if a bad piece sits in the two places behind it, plus 1 if both bad edges are in one layer and opposite. Exact ✓.
- **2 pairs**: look one swap ahead. 42.4% ✓ of 2-pair cases are at 2 or less, and those are 69.8% ✓ sub-7 against 20.0% ✓ for the others.
- **0 or 1 pair**: 3 or more, apart from four pictures. A swap makes at most two new pairs ✓.

```
R' D R2 D' L2 D2   // scramble, 4c4e, 2 pairs
D2 L2 D R2 D' R   // optimal DR, 6 moves
// U ring >-o->-o-, D ring oE<E<-o-, holes FR BR: 2 swaps, L2 then R2
```

**Every DRM: count the side turns** (section 5). Side turns are the R and L quarter turns and the half turns of a DR, U and D turns not counted.

- **2 side turns or fewer is a certain sub-7** in any DRM: all 2,197 ✓ such cases. They are the trigger cases (`R U R`, `R U2 R`, `R U L`, `R U2 L`, `R L`, `R U D2 L` with any U/D turns around them) and the 4c4e cases one half turn from two bars.
- **3 side turns with no extra quarter turn** is the switch group: one half turn from a trigger case, or one R/L quarter turn from a 4c4e that is one half turn from two bars. Call a case *short* if it needs 3 side turns or fewer of that kind. One row per DRM:

| DRM | Short: share of the DRM | Short: sub-7 rate | Not short: sub-7 rate | Share of the DRM's sub-7s that are short |
|---|---|---|---|---|
| 4c4e | 14.2% ✓ | 74.1% ✓ | 10.2% ✓ | 54.7% ✓ |
| 4c2e | 23.3% ✓ | 57.4% ✓ | 6.9% ✓ | 71.7% ✓ |
| 3c2e | 71.4% ✓ | 76.6% ✓ | 24.2% ✓ | 88.8% ✓ |
| 7c8e | 6.7% ✓ | 95.4% ✓ | 10.8% ✓ | 38.8% ✓ |
| 8c8e | 0.60% ✓ | 100% ✓ | 14.0% ✓ | 4.1% ✓ |
| 2c2e | 23.2% ✓ | 46.2% ✓ | 16.9% ✓ | 45.3% ✓ |
| 4c6e | 4.8% ✓ | 49.6% ✓ | 2.3% ✓ | 51.9% ✓ |
| 3c4e | 9.3% ✓ | 29.8% ✓ | 7.9% ✓ | 27.8% ✓ |
| 3c6e | 19.1% ✓ | 21.7% ✓ | 0.87% ✓ | 85.5% ✓ |
| 5c4e | 3.7% ✓ | 46.6% ✓ | 5.7% ✓ | 24.2% ✓ |
| 5c6e | 3.1% ✓ | 52.9% ✓ | 4.7% ✓ | 26.4% ✓ |
| 6c6e | 2.7% ✓ | 32.4% ✓ | 4.8% ✓ | 15.9% ✓ |

**The cards and the side turns stack** (section 5.5). The card's group, short against not short:

| Case | Short: sub-7 rate | Not short: sub-7 rate |
|---|---|---|
| 7c8e with 5 or 6 pairs | 95.4% ✓ | 33.8% ✓ |
| 2c2e with a paired edge | 95.0% ✓ | 37.5% ✓ |
| 4c6e JZP | 85.0% ✓ | 31.3% ✓ |
| 4c4e with both bad edges paired | 80.0% ✓ | 28.7% ✓ |
| 3c2e | 76.6% ✓ | 24.2% ✓ |
| 4c2e with 1.5+ pairs | 73.2% ✓ | 30.8% ✓ |

So rodneykinney's 5-6 pairs for 7c8e was an average of a near-certain group and a one-in-three group, and "3c2e: just always switch" hides 28.6% ✓ of 3c2e at 24.2% ✓.

**The low DRMs have a rescue where you can see a short setup.** Short 4c6e is 49.6% ✓ and holds 51.9% ✓ of 4c6e's sub-7s, short 5c6e is 52.9% ✓, short 5c4e 46.6% ✓. The other side is the cleaner discard: 3c6e that is not short is 0.87% ✓, 4c6e 2.3% ✓. By a pair trace alone they still have none: no rule of up to three of the features in section 11 puts more than 23.9% of their sub-7 cases into a cell above 50%.

**What the count leaves open.**

- *How the layers line up.* 2 half turns are a sub-7 when the setup needs 3 U/D turns or fewer, which is 64.6% of them. Nothing cheap predicts that, but you see it while you find the two swaps (section 4.5).
- *A 3 stays a 3.* Inside 3 half turns no pair, ARM or side-pair group gets above 43.3% (section 4.5). ARM adds almost nothing once you have the count: most of what it knew was the count.
- *It takes a look, not a tally.* For 4c4e with 2 pairs you search one swap deep, and for the other DRMs one half turn deep towards a trigger picture. Where that is more than a solver would do, the page says so.

**The rings read on normal.** Each U/D edge in the E slice marks its own edge place. Each misoriented corner marks its own corner place and points at the edge place of its U/D colour and the side colour that is *not* showing on the U/D face. Each E-slice edge in the U or D layer marks its own slot as a hole. It gave the inverse's rings and holes on 20,000 of 20,000 random cubes (section 7).

**What a pair trace alone gives.** If you only trace pairs, these are the best rules, each from the search of section 11.

**4c4e: count paired edges, then look at edge ARM.** Of the two bad U/D edges on the switched side, how many have a pair? Each row is a group of switched 4c4e cases, with its share of 4c4e and its sub-7 rate:

| Switched case (4c4e) | Verdict | Share of 4c4e | Sub-7 rate |
|---|---|---|---|
| both bad edges paired | **switch** | 15.5% ✓ | 59.9% ✓ |
| one paired, edge ARM 1 (the two bad edges in different slices) | **your call** | 32.5% ✓ | 20.0% ✓ |
| one paired with both edges in one slice (edge ARM 0 or 2), or none paired | **discard** | 52.0% ✓ | 6.7% ✓ |

That settles 67.5% ✓ of 4c4e. ARM alone settles 31.2% ✓ (its full 15-row table), pairs alone 33.3% ✓, and the full pairs × ARM table 49.6% ✓ (section 6.1).

**The 4c4e your-call group, split.** With one paired edge and edge ARM 1, the corners decide. Each row is a corner group inside it:

| Corners (one paired edge, edge ARM 1) | Sub-7 rate |
|---|---|
| 4d (rare: 0.82% ✓ of 4c4e) | 88.9% ✓ |
| 4b, ARM 21 | 33.0% ✓ |
| 4b, corner ARM 0 or 4 | 5.6% ✓ |

That answers tseitsei89's "It would be really nice to find a way to filter out good 1 pair cases but there doesnt seem to be one currently" ([25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409607396103290960)).

**A bar is worth half as much as two separate pairs.** In 4c4e, the sub-7 rate of two pairs on one edge against two pairs on the two edges:

| Two pairs (4c4e) | Sub-7 rate |
|---|---|
| on one edge (a bar) | 26.6% ✓ |
| on the two edges | 53.9% ✓ |

The gap holds in every ARM (11.8 ✓ to 31.2 ✓ points). That's why the card counts paired edges and not pairs, and it settles bpaul's question about pairs per edge ([21 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1397028793960370187)) and Yura Riabov's "1 bar is worse than 2 pairs for most arms" ([22 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1397110208685146265)) (section 10).

**Side pairs and edge ARM on the inverse, read on normal**, without switching axes:

- *Side pairs*: for each E-slice edge sitting in the U or D layer, count the misoriented corners that carry both its colours and show the EO axis's colour (green/blue for an F/B EO) on the U/D face.
- *Edge ARM*: count the U/D edges in the E slice whose other colour is green/blue.

Both held on 20,000 of 20,000 random cubes (section 7).

**7c8e: 3 pairs or fewer is a safe discard** (50.0% ✓ of 7c8e at 2.9% ✓). With 4 pairs, edge ARM 1 is 30.3% ✓ and every other edge ARM 17.0% ✓ or less.

**After a switch the RZP bias is gone.** torchlight was right that an RZP biases the case it reaches ([8 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215720321995382867)). The 4c4e sub-7 rate in three populations:

| 4c4e population | Sub-7 rate |
|---|---|
| uniform | 19.2% ✓ |
| end state of a 5-move RZP, same side | 18.3% |
| the same, switched | 19.2% |

The switched state is exactly uniform again, for every DRM, because the inverse of a cube with a given case is uniform over that case. So every exhaustive table is right for the cases you actually switch. On the 121,527,134 real attempts, no DRM × RZP length is more than 2.63 standard errors off the uniform rate (section 8).

**After a switch the last-turn options are worth little.** Turning the RZP's last move the other way never changes the switched case (114,102 of 114,102 pairs of attempts; proved in Lean ✓). For 4c4e (section 8), each row is an option; the points are its sub-7 rate minus the rate without it:

| Option (4c4e) | Sub-7 rate after a switch, without the option | With the option | Points added after a switch | Points added without a switch |
|---|---|---|---|---|
| EO's last turn | 19.1% | 21.2% | 2.1 | 8.8 ✓ |
| other DR axis | 19.1% | 25.0% | 5.9 | 6.1 |

**RZP length moves every band.** After a 4-move RZP (DR in 7 is enough), 4c4e with 3 half turns to two bars is still 71.3% ✓ and with 2 or fewer 99.2% ✓; every 4c4e case with a paired edge is around 50% or more, and only the no-pair group stays low (31.7% ✓). After a 6-move RZP (DR in 5 needed), only 0 or 1 half turn is a switch (93.3% ✓; 2 half turns are 21.4% ✓), and no common pair cell reaches 25%: 4c4e with both edges paired is 20.1% ✓ and 3c2e is 19.2% ✓ (section 6).

**The low DRMs, by pairs and ARM.** For 4c6e, 3c4e, 3c6e, 5c4e, 5c6e and 6c6e the best small cells a pair trace finds, with their sub-7 rates (the short setups above do better where you can see them):

| Cell | Sub-7 rate |
|---|---|
| 4c6e JZP (0.61% ✓ of 4c6e) | 61.1% ✓ |
| 5c6e with 4 pairs | 37.9% ✓ |
| 3c4e with 2 pairs | 33.7% ✓ |

**Fanti's rule figures are any-turn numbers**: they allow F/B quarter turns, which break the EO. With the EO kept they move by about a point at most (4c2e switch success: 38.8% any-turn, 37.7% EO kept) (section 12).

**What it confirms or corrects**

- **Confirmed: the 4c2e rule.** "1.5+ pairs" (rodneykinney, [30 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1411385789891350698)) switches exactly the same cases as Jay's 1 pair + 1 side pair or 2 pairs ([14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383640829280780392)) and tseitsei89's version ([25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018)): 22.3% ✓ of 4c2e at 57.0% ✓. What I add is the other end: 0 or 0.5 is 4.0% ✓, so the rule settles 75.4% ✓ of 4c2e.
- **Confirmed: the rest of the switch list.** rodneykinney's 5-6 pairs for 7c8e (59.0% ✓), "3c2e: just always switch" (tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018): 61.6% ✓), 1+ pairs for 2c2e (59.6% ✓), JZP-only for 4c6e, and Yura Riabov's "trash" ARMs for 4c4e (all under 4% ✓). The search found nothing cheap that does much better on those DRMs (section 11).
- **Confirmed: Zagros's 8c8e condition**, "8e8c - R L but only if four corners are clockwise and four are ccw (7/1 is possible)" ([20 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1342188064067424340)): all 4,900 8c8e cases with a 4-4 split have a DR with two quarter turns, and none of the 1,120 with a 7-1 split has (section 13).
- **Confirmed: the NISS predictors.** The ARM axis swap, R/L stickers on U/D for corner ARM, rodneykinney's corner-case flow chart and wen's pair tracing each held on every one of 20,000 sampled cubes. Louis's same-axis version, which Louis took back at the time, holds on only 10.4% (section 7).
- **Confirmed: the published tables.** 152 of 154 published numbers reproduce. The two that don't are sampled cells in Evan's *arm/pairs*, low by 0.017 and 0.032 (section 12).
- **Confirmed: Evan's stacked corners.** For 4c4e with 1 pair and ARM 21, "a corners - ~34% if corners are stacked, < 5% otherwise" ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418283868007436308)): with each bad corner directly above or below another the a corners are 34.8%, and otherwise 2.5% (section 13).
- **Corrected** (one statement, in the [errata](errata.html) with an example): Jay's count by hand of the 4c4e ARM sets that can be sub-6 after a switch, "10 total sets that can be sub 6 out of the 15 total sets" ([9 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215904716530384908), after "I believe I now know"), is 11 ✓: AR-4c1e is missing.
- **Depends**: rodneykinney's "there aren't any 4-movers with 0 or 1 pairs" ([25 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1068026817602125844)) holds with side pairs counted, not for top pairs alone (first line below); and the 0-pair catch for that case misses the same case one U/D turn earlier (second line). rodneykinney's "no number of pairs will save 3qt corners" for 4c2e ([15 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383677247545933874)) is about 4a-0 corners, the ones 3 U/D quarter turns from the `R U2 R` corners: no such case is under 6 moves and with 2 pairs they are 25.0% as rodneykinney's sheet folds them, but 50.0% for the 48 with corner ARM 0 (section 13).

```
F2 B2 R    // 4c4e with no top pair
D F2 B2 R  // 0 pairs, no fake pairs, missed by the 0-pair catch
```

---

## 2. What was asked

The questions, in the askers' own words, and where each is answered. Most got an opinion or no answer at the time.

**Better switch guidelines (sections 4 to 7)**

- *find better guidelines than we have already (arm, drm, pairs, maybe rodney's corner orbit thing) for when to switch an eo, closer to 100% vs 0% chance of sub7 to dr. Guidelines that humans can quickly check.* *Answer*: count the side turns with U and D free: for 4c4e the half turns to two bars (section 4), for the other DRMs the side turns (section 5), with a certain class at one end and a near-certain discard at the other. For a pair trace alone, the switch cards of section 6. All read from the normal side as in section 7.

**Which feature says most (sections 6, 10 and 11)**

- JTuu ([27 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1222755932518486027)): "it might be useful to have a table comparing P(optimal < N | rzp) against P(optimal < N | rzp, arm). that is, when is the arm info most informative?" eff ([21 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1386072579307081738), [21 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1386072782189756547)): "yeah is there an objective comparison between the two yet", "arm-xcxe vs xy-z with n pairs". *Answer*: pairs settle more cases than ARM for 4c4e, 4c2e and 7c8e, ARM more for 8c8e and 2c2e, and for 4c4e paired edges plus edge ARM settle more than pairs and ARM together (section 10). The information measures are in section 11 (**computer only**).
- wen ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418248619374678247)): "Interestingly now we have basically 3 criteria for NISS that we can trace, >1pair/ARM/corner structure", "if we pick 2 out of 3 to stick to, which gives the lowest false negative rate?" *Answer*: pairs + corner case, by a little over pairs + ARM; ARM + corner case is far behind. Paired edges + edge ARM, which isn't on wen's list, settles more cases than any two of the three (section 10).
- Zagros ([5 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1479199955444043899)): "Is number of corners NOT in a pair a better heuristic across all DRM than number of pairs?" *Answer*: once you know the DRM they say the same thing (section 10).
- tseitsei89 ([25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409607396103290960)): "It would be really nice to find a way to filter out good 1 pair cases but there doesnt seem to be one currently". *Answer*: the 1-pair cases 2 half turns from two bars, 1,152 of them at 73.6% (three ring pictures, appendix A); by a pair trace alone, edge ARM, then the corner case (section 6.1).
- bpaul ([21 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1397028793960370187), [21 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1397028895227772979)): "random thought i wonder whether looking at pair stats not just on the count but also based on the number of pairs per edge could be good", "sounds way harder to count for higher corner counts but maybe for 4c4e it would be helpful idk". *Answer*: yes, and it's the main 4c4e finding (sections 6.1 and 10).
- caycala ([25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1365339679385321552)): "i wonder what the probability is for 21 + no pairs+ 1 corner pair". *Answer*, reading "corner pair" as a side pair: 4c4e ARM 21 with no pairs and 1 side pair is 6.8%; with 2 side pairs it is 24.1%.
- FakeMMAP ([21 Jun 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1385961621888696432)): "Do you think it's worthwhile to check for ARM if you have 0 pairs on the off-chance it's a short setup to F2 B2 R?" *Answer*: with 0 pairs, ARM 00 is 66.7% and ARM 42 is 83.3%, but each is only 36 of the 21,000 zero-pair cases. Every other ARM is 11.0% or less (ARM 21 is the best of them). So it's only worth it if the ARM check costs you nothing. The ring picture finds the case directly: `F2 B2 R` is the one 0-pair picture that is 2 half turns from two bars, in each layer two bad corners pointing at each other across a good edge place with the bad edge opposite (`oEo->-<-` twice, 96 cases at 81.3%).

**Real RZPs, the last turn and the other axis (section 8)**

- KrzychXyz ([9 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1216123557776461895)): "Does this mean that DR-4c4e's occuring "naturally" are statistically better than those obtained by doing some post-EO moves?" (after torchlight's [8 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215720321995382867)). *Answer*: on the same side, yes, slightly; after a switch there is no difference at all.
- Jay ([6 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1358302313076363294)): "i'm wondering if it's worth investigating the affects on sub 6/7% chance for DRM/ARM combos where you also account for what the DRM/ARM is when you "flip" the RZP via RLUD stuff?" *Answer*: flipping the RZP's last turn never changes the switched case (section 8).
- DanielEgdal ([21 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1154347811412914238)), JTuu ([25 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1221904779853299962)), Evan ([16 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417546279931744357)): whether the other DR axis was ever counted: "has anyone thought about whether it's useful to consider ARM on both dr axes for a given eo? (I have not)", "i don't think any research has been done on dual axis switching probabilities". *Answer*: section 8 (and my EO-to-DR study for the unswitched case).
- Lichi Fang ([28 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1234107908695003187)): "Is there any practical approach to consistently find good DRs from DR-5c4e, DR-5c6e or DR-6e6c?" *Answer*: not by pairs and ARM (sections 6.6 and 11). The cases worth it are the short ones: an R or L turn that leaves a 4c4e one half turn from two bars (46.6%, 52.9% and 32.4% for 5c4e, 5c6e and 6c6e, on 3% to 4% of each; section 5.4).

What's left open is in section 14.

---

## 3. Definitions

Everything is written for an F/B EO and a DR on U/D. Other axes are the same up to a rotation.

**State, switched side.** What matters for the DR is the *case*: which corners are twisted and how, and which places hold the four E-slice edges ($2187 \times 495 = 1{,}082{,}565$ of them for one EO axis and one DR axis). After EO + RZP you have a case on normal. Switching means solving the DR on the inverse with the EO kept, so the case that matters is the inverse's, the *switched case*. All rules here are read on the switched case. Section 7 is about seeing it on normal.

**Sub-7.** A DR in at most 6 moves with turns that keep the EO (U, D, R, L, F2, B2), linear, on the switched side, the yardstick since "we are normally looking for rzp in 5 or less and dr in 11 or less. So sub-7 from 5 move rzp gives that" (tseitsei89, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436061424110538882)). For other RZP lengths the target moves: DR in 7 after a 4-move RZP, DR in 5 after a 6-move RZP. The cards give those columns too.

**DRM.** Bad corners: corners whose U/D sticker is not on U or D. Bad edges: twice the number of E-slice edges outside the E slice, so all edges out of DR are counted. Written corners first (4c4e).

**ARM.** Corner ARM: bad corners whose U/D sticker is on R or L. Edge ARM: bad edges in the M slice, that is E-slice edges sitting at UF, UB, DF or DB. Written corner digit first (21 = AR-2c1e = corner ARM 2, edge ARM 1). *JZP* is ARM 00 with an even number of bad corners.

**Pairs.** A *pair* (top pair) is a bad edge in the U or D layer and a bad corner next to it in the same layer whose U/D sticker is on the side face the edge doesn't touch, as after R from a solved cube (which leaves 4 pairs: two bars). A *fake pair* is the same two pieces with the corner twisted the other way, its U/D sticker on the edge's side face. A *side pair* is a bad edge in the E slice (a U/D edge sitting there) and the corner above or below it, twisted to pair. These are the counts of Louis's and rodneykinney's code, which agree with each other on every case (appendix B). A bar (an edge paired on both sides) counts as 2 pairs.

**Paired edges.** In 4c4e and 4c2e there are two bad edges in the U/D layers. *Paired edges* is how many of them have at least one pair: 0, 1 or 2. Two pairs on one edge (a bar) is 1 paired edge, and two pairs on two edges is 2.

**Corner case.** rodneykinney's 4a, 4b, 4c, 4d for four bad corners, by how the bad corners split between the two HTR orbits (4d all in one, 4c 3-1, 4a and 4b 2-2, 4b if some U, D, R or L face has exactly 1 or 3 bad corners), with the corner ARM suffix ("4b-0", "4d-2").

**Rings, rows, holes.** A *ring* is the 8 places of the U or D layer, read clockwise as you look at that face (U: UB UBR UR UFR UF UFL UL UBL; D: DB DBL DL DFL DF DFR DR DBR). A bad corner *points* at the edge place next to it that its U/D sticker does not touch, the one it would pair with: so a pair is a bad corner pointing at a bad edge and a fake pair is one pointing away from the bad edge next to it. A *row* is the corner, edge, corner of one layer on one side face. A *hole* is an E-slice place holding a U/D edge. Ring strings (`>E<-o-o-`) are explained in section 4.1.

**Half turns to two bars** (4c4e). The fewest half turns (R2, L2, F2, B2) after which one R or L quarter turn gives DR, with U and D turns allowed anywhere and not counted. It equals the larger of the *row swaps* (fewest exchanges of a U row with a D row that leave a bar in each ring) and the hole number (0 if the two holes are on one R/L face, 1 if diagonal, 2 if on one F/B face).

**Side turns** (any DRM). The fewest turns of the side faces (R, L quarter or half turns, F2, B2) in any DR of the case, U and D turns not counted. A case is *short* if it needs 3 side turns or fewer with no more quarter turns than its DRM needs anyway (1 for 4c4e, 2 for the other named DRMs).

**Verdict bands.** A group of cases is *switch* if over 50% of it is sub-7, *discard* if under 10%, and *your call* in between. That's where the server's own cut-offs sit ("i think it's best to find the <10% ones and dont switch for those and switch everything else maybe", wen, [12 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1272564863230808065); "i switch for around 20% and above", Yura Riabov, [12 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1272564881358323785); "I would say below 20% is never and above 30% is pretty much always.", tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409573949486137425)). A rule *settles* a case if its cell is switch or discard. *Settled* is the share of the DRM's cases that land in such cells. *Sub-7 states switched* (recall) and *sub-7 states discarded* are shares of the DRM's sub-7 cases and of all its cases.

**Populations.** *Uniform*: every case of the DRM counts once. That is what Cale's, Louis's and rodneykinney's tables count, and what the cards are graded on (exact). *After an RZP*: cases weighted by the number of RZPs of a given length that reach them from a uniform EO-solved cube (exact counts), on the same side or after the switch. *Real attempts*: 6,000 uniformly random scrambles, every EO of at most 6 moves on each axis, on normal and on inverse, both DR axes of each, and every RZP that first reaches its DRM at a total of 4, 5 or 6 moves (121,527,134 attempts, about 20,254 per scramble, so their errors come from batches of scrambles, not from the attempt count).

---

## 4. Two rings: count the half turns (4c4e)

A U or D turn never makes or breaks a pair. So when you size up a setup, don't count them: let both layers turn freely and ask how many turns of the side faces the DR needs. For 4c4e the finish is one R or L quarter turn and everything before it is half turns, so the question is *how many half turns to two bars*. That count sorts 4c4e far better than pairs, ARM or the corner case, and its two ends are near 100% and near 0%.

The target is rodneykinney's. *DR - 4c4e Theory* says "The final trigger must have two full “bars” formed with the bad corners and edges.", calls each side half turn "an opportunity to form a pair for free", and notes that "An additional 0-2 moves may be needed to solve the E slice." That doc builds a minimum move count from it (corner moves, a pairs penalty, a slice penalty). Here I count the half turns themselves, exactly, with U and D turns free, and measure what the count is worth.

### 4.1 The picture

Take the switched case and forget how the U and D layers are turned. What is left of a layer is a *ring*: its 8 places, read clockwise as you look at that face.

```
      UB
 UBL      UBR      U ring, clockwise from above:   UB UBR UR UFR UF UFL UL UBL
 UL        UR      D ring, clockwise from below:   DB DBL DL DFL DF DFR DR DBR
 UFL      UFR      between them, the E-slice places:   FR FL BL BR
      UF
```

Three things sit on it:

- **Bad edge places.** A ring edge place holding an E-slice edge, the usual bad U/D edge.
- **Bad corners, each pointing at an edge place.** A bad corner has its U/D sticker on one of its two side faces. It *points* along the layer away from that sticker, at the edge place next to it on its other side face. That is the edge place it would pair with. So a pair is a bad corner pointing at a bad edge, a fake pair is a bad corner next to a bad edge and pointing away from it, and a bar is a bad edge with a corner pointing at it from each side.
- **Holes.** The E-slice places that hold a U/D edge. 4c4e has two.

Examples on this page are a scramble from solved in EO-keeping moves (hold the cube with the EO on F/B), then an optimal DR of the case it gives.

I write a ring as 8 characters, clockwise, starting at any corner: `>` is a corner pointing clockwise (at the next place), `<` a corner pointing counter-clockwise (at the place before it), `o` a good corner, `E` a bad edge place, `-` a good one. The string closes on itself, and where it starts doesn't matter. A bar reads `>E<`.

```
R' U2 D2   // scramble
D2 U2 R   // optimal DR, 3 moves
// U ring >E<-o-o-, D ring >E<-o-o-, holes FR BR: a bar in each layer; U2 D2 puts both on the holes' face, then R
```

What each turn does to the picture:

| Turn | What it does |
|---|---|
| U, D | Turns one ring. Nothing else changes, so the picture doesn't see it. |
| R2, L2, F2, B2 | Swaps the *row* of that face between the two rings, and swaps the face's two E-slice places. A row is the corner, edge, corner of one layer on one side face. R2 swaps UBR UR UFR with DFR DR DBR, so the clockwise order is kept. |
| R, L (quarter turns) | The four corners on the face move one step round it. A good corner comes out pointing at the face's edge place. A corner that pointed at the face's edge place comes out good. A corner that pointed away keeps pointing away. The four edges on the face move one step round it, layer to slot to layer to slot. |

All three rules hold on every one of the 1,082,565 cases ✓ (Lean: `ring_turns`), and the picture loses nothing: two different cases never have the same rings and holes ✓ (`ring_faithful`).

Because U and D are free, **a half turn can swap any row of the U ring with any row of the D ring**: turn the two rows onto the same face first. Which face you do it on is your choice, and it only matters for the holes.

### 4.2 The count

A 4c4e is one quarter turn from DR when each layer has a bar, both bars are on the same R or L face, and the two holes are on that face. In ring terms: a bar in each ring, and the holes on one R/L face.

**Half turns to two bars** is the fewest half turns that get you there, U and D turns not counted. It is the larger of two things you read separately:

- **Row swaps.** The fewest row swaps that leave a bar in each ring. This is a small puzzle on the two rings alone. Up to turning each ring there are only 780 ring pairs in 4c4e, 1 of them needs 0 swaps, 12 need 1, 95 need 2, 392 need 3, 268 need 4 and 12 need 5 ✓ (`ring_swaps_checked`).
- **The holes.** 0 if the two holes are on one R or L face (FR and BR, or FL and BL), 1 if they are diagonal, 2 if they are on one F or B face. F2 or B2 moves a hole between *one R/L face* and *diagonal*. R2 or L2 moves one between *diagonal* and *one F/B face*.

That the count is the larger of the two holds on all 70,560 cases of 4c4e ✓ (`half_turns_to_bars`). The reason is short. Every half turn does one row swap, on a face of your choice, so the same turn can also fix the holes or leave them alone. A swap you don't need can exchange the two bars, which changes nothing.

Each row below is a number of row swaps with one hole layout. The count, and how the sub-7 rate follows it:

| Row swaps to a bar in each layer | The two holes | Half turns to two bars | States | Share of 4c4e | Sub-7 rate |
|---|---|---|---|---|---|
| 0 | same R/L face | 0 | 32 | 0.045% | 100% |
| 0 | diagonal | 1 | 32 | 0.045% | 100% |
| 0 | same F/B face | 2 | 32 | 0.045% | 93.8% |
| 1 | same R/L face | 1 | 328 | 0.46% | 100% |
| 1 | diagonal | 1 | 328 | 0.46% | 100% |
| 1 | same F/B face | 2 | 328 | 0.46% | 90.2% |
| 2 | same R/L face | 2 | 2,976 | 4.2% | 78.9% |
| 2 | diagonal | 2 | 2,976 | 4.2% | 63.4% |
| 2 | same F/B face | 2 | 2,976 | 4.2% | 71.8% |
| 3 | same R/L face | 3 | 12,000 | 17.0% | 14.8% |
| 3 | diagonal | 3 | 12,000 | 17.0% | 15.3% |
| 3 | same F/B face | 3 | 12,000 | 17.0% | 17.8% |
| 4 | same R/L face | 4 | 7,952 | 11.3% | 2.2% |
| 4 | diagonal | 4 | 7,952 | 11.3% | 1.2% |
| 4 | same F/B face | 4 | 7,952 | 11.3% | 1.7% |
| 5 | same R/L face | 5 | 232 | 0.33% | 0% |
| 5 | diagonal | 5 | 232 | 0.33% | 0% |
| 5 | same F/B face | 5 | 232 | 0.33% | 0% |

The holes only bite when the rings are nearly done. Two bars with the holes on an F/B face is a 2, not a 0:

```
R' U D' F2 U2 R2 U2   // scramble, a bar in each layer, holes on the F face
U2 R2 U2 F2 D U' R   // optimal DR, 7 moves
// U ring >E<-o-o-, D ring >E<-o-o-, holes FR FL: 0 swaps, but 2 half turns, and this one takes 7
```

### 4.3 The bands

One row per count. *Share of 4c4e's sub-7s* is how much of all the sub-7 cases of 4c4e sit in that row. Exact over every case, then the same on the real attempts:

| Half turns to two bars | States | Share of 4c4e | Sub-7 rate, exact | Share of 4c4e's sub-7s | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) |
|---|---|---|---|---|---|---|
| 0 | 32 | 0.045% | 100% | 0.24% | 100% | 284 |
| 1 | 688 | 0.98% | 100% | 5.1% | 100% | 5,726 |
| 2 | 9,288 | 13.2% | 72.1% | 49.4% | 72.1% | 73,332 |
| 3 | 36,000 | 51.0% | 16.0% | 42.3% | 15.8% | 284,482 |
| 4 | 23,856 | 33.8% | 1.7% | 3.0% | 1.6% | 191,432 |
| 5 | 696 | 0.99% | 0% | 0% | 0% | 5,566 |

- **0 or 1: a certain sub-7.** One half turn, at most two U/D turns before it and two after, then the quarter turn: 6 moves at most. It holds for all 720 ✓ cases.
- **2: switch.** 72.1% ✓ of them are sub-7, and they hold half of 4c4e's sub-7s.
- **3: your call.** 16.0% ✓, on half of 4c4e.
- **4 or 5: discard.** 1.7% ✓ on 34.8% ✓ of 4c4e. A 5 is never sub-7.

The same rows for the other RZP lengths. After a 4-move RZP a DR in 7 is enough, and after a 6-move RZP you need a DR in 5:

| Half turns to two bars | DR in 7 or fewer, exact (for a 4-move RZP) | DR in 7 or fewer, real attempts (RZP to 4) | Real attempts (RZP to 4) | DR in 5 or fewer, exact (for a 6-move RZP) | DR in 5 or fewer, real attempts (RZP to 6) | Real attempts (RZP to 6) |
|---|---|---|---|---|---|---|
| 0 | 100% | 100% | 30 | 100% | 100% | 3,610 |
| 1 | 100% | 100% | 406 | 93.0% | 92.7% | 74,044 |
| 2 | 99.1% | 99.2% | 5,578 | 21.4% | 21.2% | 978,550 |
| 3 | 71.3% | 70.3% | 21,350 | 1.1% | 1.1% | 3,800,040 |
| 4 | 26.6% | 27.4% | 14,558 | 0.017% | 0.016% | 2,533,814 |
| 5 | 1.1% | 0.97% | 412 | 0% | 0% | 72,792 |

So with a 4-move RZP, 3 half turns is still a switch (71.3%), and with a 6-move RZP only 0 or 1 is.

**Against the paired-edge card** (section 6.1), three groups each:

| Rule | Group (4c4e) | Share of 4c4e | Sub-7 rate | Share of 4c4e's sub-7s |
|---|---|---|---|---|
| this page | 2 half turns or fewer to two bars | 14.2% | 74.1% | 54.7% |
| this page | 3 half turns | 51.0% | 16.0% | 42.3% |
| this page | 4 or 5 half turns | 34.8% | 1.7% | 3.0% |
| the paired-edge card | both bad edges paired | 15.5% | 59.9% | 48.2% |
| the paired-edge card | one paired, edge ARM 1 | 32.5% | 20.0% | 33.8% |
| the paired-edge card | one paired with edge ARM 0 or 2, or none paired | 52.0% | 6.7% | 18.0% |

The switch group is as large as the card's and 14.2 points better, and the discard group throws away 3.0% of the sub-7s where the card's throws away 18.0%. What you pay is a bigger middle. The card's own groups, split by the count, show where it goes wrong:

| The paired-edge card's group | Half turns to two bars | States | Share of 4c4e | Sub-7 rate |
|---|---|---|---|---|
| switch | 2 or fewer | 6,648 | 9.4% | 80.0% |
| switch | 3 | 4,176 | 5.9% | 28.9% |
| switch | 4 or 5 | 96 | 0.14% | 16.7% |
| your call | 2 or fewer | 2,592 | 3.7% | 63.9% |
| your call | 3 | 17,184 | 24.4% | 16.8% |
| your call | 4 or 5 | 3,168 | 4.5% | 1.5% |
| discard | 2 or fewer | 768 | 1.1% | 58.1% |
| discard | 3 | 14,640 | 20.7% | 11.3% |
| discard | 4 or 5 | 21,288 | 30.2% | 1.6% |

Both edges paired with 3 half turns to go is a 28.9% case, not a 60% one. And 768 cases the card discards are 2 half turns from two bars, 58.1% sub-7:

```
L' U' R' D R2 U' R' U2   // scramble, both bad edges paired
U2 R U R2 D' R U L   // optimal DR, 8 moves
// U ring <-o->-o-, D ring >Eo-oE<-, holes FL BL: 3 swaps

L' F2 B2 U2 D2   // scramble, no pair at all
D2 U2 B2 F2 L   // optimal DR, 5 moves
// U ring oEo->-<-, D ring oEo->-<-, holes FR BR: 2 swaps
```

### 4.4 Reading the count

There is no formula for the row swaps. I looked for one. No score read off one layer at a time can work: the 179 different single rings fall into 114 groups that need different swap counts against some partner ring (**computer only**). And a table over pair counts, which layer each piece is in and which corners are blocked puts 82.4% of 4c4e in the right band (1 or fewer, 2, 3, 4 or more) with 99 cells. So you count by finding the swaps. That is less work than it sounds, because pairs tell you where to look.

**A swap makes at most two new pairs** ✓ (`pair_change`). So with 0 or 1 pair you need at least 2 swaps, and in practice 3 or more. Each row is a pair count with a count of half turns:

| Pairs | Half turns to two bars | States | Share of 4c4e | Sub-7 rate |
|---|---|---|---|---|
| 0 | 2 | 96 | 0.14% | 81.3% |
| 0 | 3 | 4,848 | 6.9% | 12.0% |
| 0 | 4 or 5 | 16,056 | 22.8% | 1.5% |
| 1 | 2 | 1,152 | 1.6% | 73.6% |
| 1 | 3 | 22,080 | 31.3% | 14.4% |
| 1 | 4 or 5 | 7,968 | 11.3% | 1.4% |
| 2 | 1 or fewer | 128 | 0.18% | 100% |
| 2 | 2 | 6,592 | 9.3% | 69.2% |
| 2 | 3 | 8,592 | 12.2% | 20.6% |
| 2 | 4 or 5 | 528 | 0.75% | 9.1% |
| 3 | 1 or fewer | 512 | 0.73% | 100% |
| 3 | 2 | 1,408 | 2.0% | 83.5% |
| 3 | 3 | 480 | 0.68% | 43.3% |
| 4 | 1 or fewer | 80 | 0.11% | 100% |
| 4 | 2 | 40 | 0.057% | 95.0% |

Read it as a recipe:

1. **4 pairs.** 0 swaps if the bars are in different layers, 1 if both are in one layer.
2. **3 pairs.** One corner is unpaired and one edge lacks a corner. Start at 1 swap. Add 1 if the unpaired corner is in the same layer as the edge that lacks it. Add 1 if it is *blocked*: a bad piece in the two places behind it (the edge place and corner on the side it points away from). Add 1 if both bad edges are in one layer, opposite each other. This is exact on every 3-pair case ✓ (`three_pair_rule`):

| The unpaired corner is in | A bad piece in the two places behind it | Both bad edges in one layer, opposite each other | Row swaps | States (4c4e) | Sub-7 rate |
|---|---|---|---|---|---|
| the other layer | no | no | 1 | 768 | 95.8% |
| the other layer | no | yes | 2 | 384 | 81.3% |
| the other layer | yes | no | 2 | 384 | 83.3% |
| the layer of the edge that lacks it | no | no | 2 | 384 | 83.3% |
| the layer of the edge that lacks it | yes | no | 3 | 480 | 43.3% |

3. **2 pairs.** Look one swap ahead: you are at 2 if some swap leaves one of the 1-swap pictures below. 42.4% of 2-pair cases are at 2 or less, and those are 69.8% sub-7 against 20.0% for the rest. This is the look that pays.
4. **0 or 1 pair.** Call it 3 or more and move on. You lose 1,248 cases that are really at 2 (2.4% of the 0- and 1-pair cases), one 0-pair picture and three 1-pair pictures in appendix A. That's the limit of the hand reading: with 0 or 1 pair it doesn't separate a 3 from a 4 or 5, and 97.8% of the 4s and 5s are here, so the near-zero row of the table in 4.3 can't be picked out without a search. With 0 or 1 pair, 29.8% of 4c4e has no pair (4.3% sub-7) and 44.2% has one (13.3%); the paired-edge card (section 6) splits them better than that.

The pictures with at most 1 swap, up to exchanging the layers and mirror image. Know the four with 1 swap and the rest is one swap of look-ahead:

| Row swaps | One layer | The other layer | What it is |
|---|---|---|---|
| 0 | `>E<-o-o-` | `>E<-o-o-` | a bar in each layer |
| 1 | `>E<->E<-` | `o-o-o-o-` | both bars in one layer: swap one over |
| 1 | `>E<E<-o-` | `>-o-o-o-` | 3 pairs, the two bad edges next to each other in one layer, the fourth corner alone in the other: swap the bar out and the corner in |
| 1 | `oE<-o-o-` | `>E<-o->-` | 3 pairs, the fourth corner in the bar's layer with nothing behind it: swap it across |
| 1 | `oE<-o-<-` | `>Eo->-o-` | one pair on each edge, and each layer holds the corner the other needs, two places from where it has to land: one swap trades them |

All ring pairs with at most 2 swaps, 33 pictures up to layer exchange and mirror image, are listed in appendix A ✓ (`patterns_le2`).

Three worked ones:

```
R' D' L2 U2 D'   // scramble, 3 pairs
D U2 L2 D R   // optimal DR, 5 moves
// U ring >E<-o->-, D ring oE<-o-o-, holes FR BR: 1 swap, L2 carries the fourth corner across

R' U' D L2 U'   // scramble, one pair on each edge
U L2 D' U R   // optimal DR, 5 moves
// U ring oE<-o-<-, D ring >Eo->-o-, holes FR BR: 1 swap, L2 trades the two corners

R' D R2 D' L2 D2   // scramble, 2 pairs
D2 L2 D R2 D' R   // optimal DR, 6 moves
// U ring >-o->-o-, D ring oE<E<-o-, holes FR BR: 2 swaps, L2 then R2, one corner each

L' D2 F2 R D L2 U'   // scramble, 2 pairs, 2 swaps again
U L2 D' R' F2 D2 L   // optimal DR, 7 moves
// U ring <-o->-o-, D ring oE>E<-o-, holes FL BR: but the layers don't line up: 7 moves
```

**What the look costs.** You trace the same six pieces as for pairs. On top of that you note which layer each piece is in, and for each unpaired corner where it sits and which way it points: one more look per unpaired corner, and one at the holes. With 3 or 4 pairs the recipe is a count. With 2 pairs it is a one-swap search. I timed none of it.

### 4.5 What the U and D turns add

The count ignores U and D turns, and they are what is left. A setup with h half turns and u U/D turns before the quarter turn is a DR in h + u + 1 moves, so 2 half turns are sub-7 with up to 3 U/D turns and 3 half turns with up to 2. Each row is a half-turn count with the U/D turns its shortest setup needs:

| Half turns to two bars | U/D turns that setup needs | States | Share of that half-turn count | Sub-7 rate |
|---|---|---|---|---|
| 2 | 3 or fewer | 6,004 | 64.6% | 100% |
| 2 | 4 or more | 3,284 | 35.4% | 21.2% |
| 3 | 2 or fewer | 3,964 | 11.0% | 100% |
| 3 | 3 or more | 32,036 | 89.0% | 5.6% |
| 4 | 1 or fewer | 124 | 0.52% | 100% |
| 4 | 2 or more | 23,732 | 99.5% | 1.2% |

So for a 2, about two in three line up, and once you have found the two swaps you check that in the same breath: every swap whose two rows are already on the same face costs no U/D turn. For a 3 it is one in nine. The rest of the 3s that are sub-7 take another route (section 4.6). The full table is in appendix A.

**Nothing cheap splits a 3 well.** Each row is a group inside *3 half turns*:

| Inside *3 half turns* | States | Share of 4c4e | Sub-7 rate, exact | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) |
|---|---|---|---|---|---|
| 0 pairs | 4,848 | 6.9% | 12.0% | 11.7% | 38,444 |
| 1 pair | 22,080 | 31.3% | 14.4% | 14.2% | 174,410 |
| 2 pairs | 8,592 | 12.2% | 20.6% | 20.8% | 67,882 |
| 3 pairs | 480 | 0.68% | 43.3% | 42.2% | 3,746 |
| 0 side pairs | 11,192 | 15.9% | 9.1% | 8.7% | 87,050 |
| 1 side pair | 15,136 | 21.5% | 13.4% | 13.4% | 120,024 |
| 2 or more side pairs | 9,672 | 13.7% | 28.0% | 27.6% | 77,408 |
| edge ARM 1 | 21,600 | 30.6% | 17.6% | 17.4% | 170,634 |
| edge ARM 0 or 2 | 14,400 | 20.4% | 13.5% | 13.4% | 113,848 |
| both bad edges paired | 4,176 | 5.9% | 28.9% | 29.2% | 33,364 |
| one bad edge paired | 26,976 | 38.2% | 14.7% | 14.5% | 212,674 |
| no bad edge paired | 4,848 | 6.9% | 12.0% | 11.7% | 38,444 |

**ARM adds little once you have the count.** In information terms (section 11) ARM removes 0.098 of the uncertainty about sub-7 in 4c4e on its own, and 0.028 once the count is known. The count alone removes 0.324, pairs 0.191, pairs and ARM together 0.262. Inside *2 half turns* every ARM is between 58.3% and 83.5%. And ARM says next to nothing about how the layers line up: it removes 0.010 of the uncertainty about whether a 2 needs 3 U/D turns or fewer, and 0.037 of the same question for a 3. So most of what ARM knew about sub-7 was the half-turn count.

### 4.6 The DRs that don't finish with one quarter turn

18.0% of 4c4e's sub-7 cases have no optimal DR with a single quarter turn. Each row is the fewest quarter turns in an optimal DR:

| Fewest quarter turns in an optimal DR | Sub-7 states (4c4e) | Share of 4c4e's sub-7s |
|---|---|---|
| 1 | 11,128 | 82.0% |
| 2 | 1,516 | 11.2% |
| 3 | 832 | 6.1% |
| 4 | 100 | 0.74% |

```
L' D' B2 D L' U   // scramble, 3 half turns to two bars, but a DR in 6 with two quarter turns
U' L D' B2 D L   // optimal DR, 6 moves
// U ring oE<-o->-, D ring <E>-o-o-, holes FL BR

R' U' L U' L' D2   // scramble, three quarter turns, no half turn
D2 L U L' U R   // optimal DR, 6 moves
// U ring <Eo->-o-, D ring >E<-o-o-, holes FR BR
```

Pairs don't see these and the half-turn count doesn't either: most of them sit at 3. They are why a 3 is 16.0% and not 11.0%. Counting side turns of any kind catches some of them, and that is the next section.

---

## 5. Every DRM: count the side turns

The same idea works for every DRM. Let U and D turn freely and count the turns of the side faces a DR needs: R and L quarter turns, and the half turns R2, L2, F2, B2. I call that number the case's *side turns*. A DR is never shorter than its side turns and never longer than three times them, and that already gives a certain class.

rodneykinney's *DRM Subsets* already sorts solutions by the trigger they end in (`R`, `R U R`, `R U2 R`, `R U L`, `R U2 L`, `R L`), from one stored optimal solution per case. Side turns count what comes before the trigger as well, and over every DR of the case.

### 5.1 Side turns

Over all 1,082,565 cases, one row per number of side turns:

| Side turns | States (all cases) | Share of all cases | Sub-7 rate | Shortest DR (moves) | Longest DR (moves) |
|---|---|---|---|---|---|
| 0 | 1 | <0.001% | 100% | 0 | 0 |
| 1 | 32 | 0.003% | 100% | 1 | 3 |
| 2 | 2,164 | 0.20% | 100% | 2 | 6 |
| 3 | 111,488 | 10.3% | 30.8% | 3 | 9 |
| 4 | 914,232 | 84.5% | 3.0% | 5 | 10 |
| 5 | 54,648 | 5.0% | 0.10% | 6 | 10 |

**2 side turns or fewer is a certain sub-7.** With s side turns you need at most two U/D turns before each of them and none after the last, so at most 3s moves. All 2,197 ✓ cases with 2 or fewer have a DR in 6 or less (`side_turns_certain`). At the other end, 5 side turns leaves room for one U/D turn at most, and 0.10% ✓ of those cases are sub-7.

By DRM, one row per number of side turns:

| DRM | Side turns | States | Share of the DRM | Sub-7 rate | Share of the DRM's sub-7s |
|---|---|---|---|---|---|
| 4c4e | 1 | 32 | 0.045% | 100% | 0.24% |
|  | 2 | 688 | 0.98% | 100% | 5.1% |
|  | 3 | 13,544 | 19.2% | 57.2% | 57.1% |
|  | 4 | 54,896 | 77.8% | 9.3% | 37.6% |
|  | 5 | 1,400 | 2.0% | 0% | 0% |
| 4c2e | 2 | 128 | 0.95% | 100% | 5.1% |
|  | 3 | 4,448 | 33.1% | 41.7% | 73.9% |
|  | 4 | 8,864 | 66.0% | 6.0% | 21.0% |
| 3c2e | 2 | 256 | 7.1% | 100% | 11.6% |
|  | 3 | 2,432 | 67.9% | 71.1% | 78.3% |
|  | 4 | 896 | 25.0% | 25.0% | 10.1% |
| 7c8e | 2 | 96 | 0.41% | 100% | 2.5% |
|  | 3 | 3,584 | 15.2% | 51.3% | 47.7% |
|  | 4 | 19,632 | 83.5% | 9.8% | 49.8% |
|  | 5 | 208 | 0.88% | 0% | 0% |
| 8c8e | 2 | 4 | 0.066% | 100% | 0.46% |
|  | 3 | 1,088 | 18.1% | 40.8% | 50.9% |
|  | 4 | 4,780 | 79.4% | 8.9% | 48.6% |
|  | 5 | 148 | 2.5% | 0% | 0% |
| 2c2e | 3 | 704 | 39.3% | 40.9% | 67.9% |
|  | 4 | 1,088 | 60.7% | 12.5% | 32.1% |
| 4c6e | 2 | 128 | 0.14% | 100% | 2.9% |
|  | 3 | 8,704 | 9.3% | 31.0% | 62.1% |
|  | 4 | 82,048 | 87.2% | 1.8% | 34.8% |
|  | 5 | 3,200 | 3.4% | 0.25% | 0.18% |
| 3c4e | 3 | 3,472 | 18.5% | 34.1% | 63.2% |
|  | 4 | 15,056 | 80.0% | 4.6% | 36.8% |
|  | 5 | 288 | 1.5% | 0% | 0% |
| 3c6e | 2 | 256 | 1.0% | 100% | 21.1% |
|  | 3 | 5,120 | 20.4% | 16.3% | 68.4% |
|  | 4 | 19,328 | 77.0% | 0.66% | 10.5% |
|  | 5 | 384 | 1.5% | 0% | 0% |
| 5c4e | 3 | 7,808 | 8.3% | 34.7% | 40.0% |
|  | 4 | 83,344 | 88.6% | 4.9% | 60.0% |
|  | 5 | 2,928 | 3.1% | 0% | 0% |
| 5c6e | 3 | 12,288 | 9.8% | 29.7% | 47.4% |
|  | 4 | 108,544 | 86.5% | 3.7% | 52.4% |
|  | 5 | 4,608 | 3.7% | 0.35% | 0.21% |
| 6c6e | 3 | 11,328 | 8.2% | 29.6% | 43.5% |
|  | 4 | 119,744 | 86.8% | 3.6% | 56.2% |
|  | 5 | 6,912 | 5.0% | 0.35% | 0.31% |

So 3 side turns is where the sub-7s are: it holds between 40.0% and 78.3% of each DRM's sub-7 cases. And a 3 comes in two kinds.

### 5.2 Quarter turns and half turns

4c4e can be finished with one quarter turn and never with none. Every other named DRM needs two at least (some 8c8e cases need three). A 3 with an extra quarter turn is much worse than a 3 without. Each row is a DRM with the make-up of its shortest setups, U/D turns not counted (where two make-ups tie on side turns, the one with fewer quarter turns):

| DRM | Shortest setup, U/D turns not counted | Side turns | States | Share of the DRM | Sub-7 rate, exact | Share of the DRM's sub-7s |
|---|---|---|---|---|---|---|
| 4c4e | 1 qt | 1 | 32 | 0.045% | 100% | 0.24% |
|  | 1 qt + 1 half turn | 2 | 688 | 0.98% | 100% | 5.1% |
|  | 1 qt + 2 half turns | 3 | 9,288 | 13.2% | 72.1% | 49.4% |
|  | 2 qt + 1 half turn | 3 | 1,440 | 2.0% | 35.6% | 3.8% |
|  | 3 qt | 3 | 2,816 | 4.0% | 19.0% | 3.9% |
|  | 1 qt + 3 half turns | 4 | 33,152 | 47.0% | 14.4% | 35.2% |
|  | 2 qt + 2 half turns | 4 | 8,576 | 12.2% | 2.6% | 1.6% |
|  | 3 qt + 1 half turn | 4 | 12,192 | 17.3% | 0.85% | 0.77% |
|  | 4 qt | 4 | 976 | 1.4% | 0% | 0% |
|  | 1 qt + 4 half turns | 5 | 1,088 | 1.5% | 0% | 0% |
|  | 2 qt + 3 half turns | 5 | 280 | 0.40% | 0% | 0% |
|  | 3 qt + 2 half turns | 5 | 32 | 0.045% | 0% | 0% |
| 4c2e | 2 qt | 2 | 128 | 0.95% | 100% | 5.1% |
|  | 2 qt + 1 half turn | 3 | 3,008 | 22.4% | 55.6% | 66.6% |
|  | 3 qt | 3 | 1,440 | 10.7% | 12.8% | 7.3% |
|  | 2 qt + 2 half turns | 4 | 8,032 | 59.8% | 6.6% | 21.0% |
|  | 3 qt + 1 half turn | 4 | 800 | 6.0% | 0% | 0% |
|  | 4 qt | 4 | 32 | 0.24% | 0% | 0% |
| 3c2e | 2 qt | 2 | 256 | 7.1% | 100% | 11.6% |
|  | 2 qt + 1 half turn | 3 | 2,304 | 64.3% | 74.0% | 77.2% |
|  | 3 qt | 3 | 128 | 3.6% | 18.8% | 1.1% |
|  | 2 qt + 2 half turns | 4 | 896 | 25.0% | 25.0% | 10.1% |
| 7c8e | 2 qt | 2 | 96 | 0.41% | 100% | 2.5% |
|  | 2 qt + 1 half turn | 3 | 1,472 | 6.3% | 95.1% | 36.3% |
|  | 3 qt | 3 | 2,112 | 9.0% | 20.8% | 11.4% |
|  | 2 qt + 2 half turns | 4 | 6,912 | 29.4% | 24.1% | 43.2% |
|  | 3 qt + 1 half turn | 4 | 11,040 | 46.9% | 2.2% | 6.4% |
|  | 4 qt | 4 | 1,680 | 7.1% | 0.48% | 0.21% |
|  | 2 qt + 3 half turns | 5 | 144 | 0.61% | 0% | 0% |
|  | 3 qt + 2 half turns | 5 | 64 | 0.27% | 0% | 0% |
| 8c8e | 2 qt | 2 | 4 | 0.066% | 100% | 0.46% |
|  | 2 qt + 1 half turn | 3 | 32 | 0.53% | 100% | 3.7% |
|  | 3 qt | 3 | 1,056 | 17.5% | 39.0% | 47.2% |
|  | 2 qt + 2 half turns | 4 | 424 | 7.0% | 35.8% | 17.4% |
|  | 3 qt + 1 half turn | 4 | 4,292 | 71.3% | 6.3% | 31.2% |
|  | 4 qt | 4 | 64 | 1.1% | 0% | 0% |
|  | 2 qt + 3 half turns | 5 | 32 | 0.53% | 0% | 0% |
|  | 3 qt + 2 half turns | 5 | 116 | 1.9% | 0% | 0% |
| 2c2e | 2 qt + 1 half turn | 3 | 416 | 23.2% | 46.2% | 45.3% |
|  | 3 qt | 3 | 288 | 16.1% | 33.3% | 22.6% |
|  | 2 qt + 2 half turns | 4 | 960 | 53.6% | 13.3% | 30.2% |
|  | 3 qt + 1 half turn | 4 | 128 | 7.1% | 6.3% | 1.9% |
| 4c6e | 2 qt | 2 | 128 | 0.14% | 100% | 2.9% |
|  | 2 qt + 1 half turn | 3 | 4,416 | 4.7% | 48.2% | 49.0% |
|  | 3 qt | 3 | 4,288 | 4.6% | 13.2% | 13.1% |
|  | 2 qt + 2 half turns | 4 | 41,920 | 44.6% | 3.1% | 30.0% |
|  | 3 qt + 1 half turn | 4 | 32,640 | 34.7% | 0.61% | 4.6% |
|  | 4 qt | 4 | 7,488 | 8.0% | 0.11% | 0.18% |
|  | 2 qt + 3 half turns | 5 | 2,880 | 3.1% | 0.28% | 0.18% |
|  | 3 qt + 2 half turns | 5 | 320 | 0.34% | 0% | 0% |
| 3c4e | 2 qt + 1 half turn | 3 | 1,744 | 9.3% | 29.8% | 27.8% |
|  | 3 qt | 3 | 1,728 | 9.2% | 38.4% | 35.5% |
|  | 2 qt + 2 half turns | 4 | 13,280 | 70.6% | 4.9% | 34.6% |
|  | 3 qt + 1 half turn | 4 | 1,616 | 8.6% | 2.5% | 2.1% |
|  | 4 qt | 4 | 160 | 0.85% | 0% | 0% |
|  | 2 qt + 3 half turns | 5 | 288 | 1.5% | 0% | 0% |
| 3c6e | 2 qt | 2 | 256 | 1.0% | 100% | 21.1% |
|  | 2 qt + 1 half turn | 3 | 4,544 | 18.1% | 17.3% | 64.5% |
|  | 3 qt | 3 | 576 | 2.3% | 8.3% | 3.9% |
|  | 2 qt + 2 half turns | 4 | 16,448 | 65.6% | 0.73% | 9.9% |
|  | 3 qt + 1 half turn | 4 | 1,664 | 6.6% | 0.48% | 0.66% |
|  | 4 qt | 4 | 1,216 | 4.8% | 0% | 0% |
|  | 2 qt + 3 half turns | 5 | 384 | 1.5% | 0% | 0% |
| 5c4e | 2 qt + 1 half turn | 3 | 3,520 | 3.7% | 46.6% | 24.2% |
|  | 3 qt | 3 | 4,288 | 4.6% | 25.0% | 15.8% |
|  | 2 qt + 2 half turns | 4 | 52,496 | 55.8% | 7.1% | 54.6% |
|  | 3 qt + 1 half turn | 4 | 28,480 | 30.3% | 1.3% | 5.3% |
|  | 4 qt | 4 | 2,368 | 2.5% | 0.34% | 0.12% |
|  | 2 qt + 3 half turns | 5 | 2,800 | 3.0% | 0% | 0% |
|  | 3 qt + 2 half turns | 5 | 128 | 0.14% | 0% | 0% |
| 5c6e | 2 qt + 1 half turn | 3 | 3,840 | 3.1% | 52.9% | 26.4% |
|  | 3 qt | 3 | 8,448 | 6.7% | 19.1% | 21.0% |
|  | 2 qt + 2 half turns | 4 | 58,944 | 47.0% | 6.2% | 47.3% |
|  | 3 qt + 1 half turn | 4 | 45,440 | 36.2% | 0.86% | 5.1% |
|  | 4 qt | 4 | 4,160 | 3.3% | 0% | 0% |
|  | 2 qt + 3 half turns | 5 | 4,544 | 3.6% | 0.35% | 0.21% |
|  | 3 qt + 2 half turns | 5 | 64 | 0.051% | 0% | 0% |
| 6c6e | 2 qt + 1 half turn | 3 | 3,776 | 2.7% | 32.4% | 15.9% |
|  | 3 qt | 3 | 7,552 | 5.5% | 28.2% | 27.6% |
|  | 2 qt + 2 half turns | 4 | 55,232 | 40.0% | 5.4% | 38.9% |
|  | 3 qt + 1 half turn | 4 | 59,904 | 43.4% | 2.2% | 17.0% |
|  | 4 qt | 4 | 4,608 | 3.3% | 0.52% | 0.31% |
|  | 2 qt + 3 half turns | 5 | 6,400 | 4.6% | 0.38% | 0.31% |
|  | 3 qt + 2 half turns | 5 | 512 | 0.37% | 0% | 0% |

- **4c2e**: 2 qt + 1 half turn is 55.6% ✓, 3 qt is 12.8% ✓.
- **7c8e**: 2 qt + 1 half turn is 95.1% ✓ on 6.3% ✓ of 7c8e. That is the closest thing to a certain switch outside the certain class.
- **3c2e**: 2 qt + 1 half turn is 74.0% ✓, and the cases that need a second half turn are 25.0% ✓. So *always switch* is really two groups.
- **The low DRMs**: 2 qt + 1 half turn is around a half for 4c6e (48.2% ✓), 5c4e (46.6% ✓) and 5c6e (52.9% ✓), on 3% to 5% of each.

The same rows on the real attempts and for the other RZP lengths are in appendix A.

### 5.3 The cases with 2 side turns

These are the triggers the server sets up to, "4e4c - set up to R", "2e3c - set up to R U R or R U' R", "2e4c - set up to R U2 R" (compLex, [20 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1342187906709848124)), "6e4c - R U2 L", "8e7c - R U L and R U' L" (Zagros, [20 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1342188845659193455)), with any U and D turns around them: `R` for 4c4e, `R U2 R` for 4c2e, `R U R` for 3c2e, `R U L` for 7c8e, `R L` for 8c8e, `R U2 L` for 4c6e, `R U D2 L` for 3c6e, and for 4c4e also the cases one half turn from two bars. In ring notation, up to exchanging the layers and mirror image, one row per picture:

| DRM | Side turns | One layer | The other layer | Holes (U/D edges in the E slice) | States |
|---|---|---|---|---|---|
| 4c4e | 1 | `>E<-o-o-` | `>E<-o-o-` | 2 | 32 |
|  | 2 | `>E<->E<-` | `o-o-o-o-` | 2 | 16 |
|  | 2 | `>E<-o-o-` | `>E<-o-o-` | 2 | 32 |
|  | 2 | `>E<E<-o-` | `>-o-o-o-` | 2 | 256 |
|  | 2 | `oE<-o-<-` | `>Eo->-o-` | 2 | 128 |
|  | 2 | `oE<-o-o-` | `>E<-o->-` | 2 | 256 |
| 4c2e | 2 | `>E<-o-<-` | `>-o-o-o-` | 1 | 128 |
| 3c2e | 2 | `>E>-o-o-` | `>-o-o-o-` | 1 | 128 |
|  | 2 | `>Eo->-o-` | `>-o-o-o-` | 1 | 128 |
| 7c8e | 2 | `>E>E<-o-` | `>E<->E>-` | 4 | 64 |
|  | 2 | `>E>E>-o-` | `>E<->E<-` | 4 | 32 |
| 8c8e | 2 | `>E<->E<-` | `>E<->E<-` | 4 | 4 |
| 4c6e | 2 | `>E<->Eo-` | `oE<-o-o-` | 3 | 128 |
| 3c6e | 2 | `<EoE<-o-` | `oE<-o-o-` | 3 | 128 |
|  | 2 | `>E>Eo-o-` | `oE>-o-o-` | 3 | 128 |

2c2e, 3c4e, 5c4e, 5c6e and 6c6e have no case with 2 side turns. One example per DRM, each the longest of its kind:

```
R' B2 R' U2 D   // scramble, 4c2e
D' U2 R B2 R   // optimal DR, 5 moves
// U ring >E<-o-<-, D ring >-o-o-o-, holes BL

L' D' L U2 D   // scramble, 3c2e
D' U2 L' D L   // optimal DR, 5 moves
// U ring >-o-o-o-, D ring >E>-o-o-, holes BL

R' U' L U' D'   // scramble, 7c8e
D U L' U R   // optimal DR, 5 moves
// U ring <E<E<-o-, D ring >E<->E<-, holes FR FL BL BR

R' L' U' D'   // scramble, 8c8e
D U L R   // optimal DR, 4 moves
// U ring >E<->E<-, D ring >E<->E<-, holes FR FL BL BR

L' F2 R' U2 D   // scramble, 4c6e
D' U2 R F2 L   // optimal DR, 5 moves
// U ring >E<-oE<-, D ring >Eo-o-o-, holes FR BL BR

R' U2 D L U2 D   // scramble, 3c6e
D' U2 L' D' U2 R   // optimal DR, 6 moves
// U ring oE>-o-o-, D ring >E>Eo-o-, holes FR BL BR
```

### 5.4 One half turn away

A setup of 2 qt + 1 half turn has its half turn in one of two places. *Before both quarter turns*: one half turn (after any U/D turns) leaves a 2-side-turn case of section 5.3. *Between them*: one R or L quarter turn leaves a 4c4e that is one half turn from two bars. One row per DRM and place:

| DRM | Where the half turn goes (2 qt + 1 half turn) | States | Share of the DRM | Sub-7 rate |
|---|---|---|---|---|
| 4c2e | before both quarter turns | 2,432 | 18.1% | 55.9% |
|  | only between them | 576 | 4.3% | 54.2% |
| 3c2e | before both quarter turns | 2,304 | 64.3% | 74.0% |
| 7c8e | before both quarter turns | 1,120 | 4.8% | 98.6% |
|  | only between them | 352 | 1.5% | 84.1% |
| 8c8e | before both quarter turns | 32 | 0.53% | 100% |
| 2c2e | only between them | 416 | 23.2% | 46.2% |
| 4c6e | before both quarter turns | 2,944 | 3.1% | 57.3% |
|  | only between them | 1,472 | 1.6% | 29.9% |
| 3c4e | only between them | 1,744 | 9.3% | 29.8% |
| 3c6e | before both quarter turns | 4,544 | 18.1% | 17.3% |
| 5c4e | only between them | 3,520 | 3.7% | 46.6% |
| 5c6e | only between them | 3,840 | 3.1% | 52.9% |
| 6c6e | only between them | 3,776 | 2.7% | 32.4% |

For 2c2e, 3c4e, 5c4e, 5c6e and 6c6e it is always the second kind: the good cases are the ones where an R or L turn gives a 4c4e with 3 or 4 pairs and at most one row swap left.

```
R' U L' F2 D   // scramble, 7c8e, one half turn from R U L
D' F2 L U' R   // optimal DR, 5 moves
// U ring >E>-o-<-, D ring >E>E>E<-, holes FR FL BL BR

L' D R U' R2 U' B2   // scramble, 7c8e with 5 pairs, but 2 half turns needed
B2 U R2 U R' D' L   // optimal DR, 7 moves
// U ring >E>-oE<-, D ring >E<->E>-, holes FR FL BL BR

L' D F2 L' D'   // scramble, 5c4e: L, then one half turn from two bars
D L F2 D' L   // optimal DR, 5 moves
// U ring >E>E>-o-, D ring <->-o-o-, holes FR FL
```

### 5.5 With the cards

The cards of section 6 and the side turns see different things, so they stack. *Short* means 3 side turns or fewer with no extra quarter turn (1 qt for 4c4e, 2 qt for the rest). Each row is a card group, split into its short cases and the others:

| DRM | The card's group | Setup | States | Share of the DRM | Sub-7 rate, exact | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) |
|---|---|---|---|---|---|---|---|
| 4c4e | both bad edges paired | short | 6,648 | 9.4% | 80.0% | 79.9% | 53,330 |
|  | both bad edges paired | not short | 4,272 | 6.1% | 28.7% | 28.9% | 34,138 |
|  | one paired, edge ARM 1 | short | 2,592 | 3.7% | 63.9% | 64.1% | 19,842 |
|  | one paired, edge ARM 1 | not short | 20,352 | 28.8% | 14.4% | 14.1% | 160,904 |
|  | the rest | short | 768 | 1.1% | 58.1% | 56.8% | 6,170 |
|  | the rest | not short | 35,928 | 50.9% | 5.6% | 5.4% | 286,438 |
| 4c2e | pairs + side pairs/2 is 1.5 or more | short | 1,848 | 13.8% | 73.2% | 73.0% | 16,048 |
|  | pairs + side pairs/2 is 1.5 or more | not short | 1,144 | 8.5% | 30.8% | 31.0% | 9,362 |
|  | exactly 1 | short | 1,160 | 8.6% | 33.1% | 33.5% | 9,862 |
|  | exactly 1 | not short | 2,144 | 16.0% | 6.3% | 6.3% | 17,678 |
|  | 0 or 0.5 | short | 128 | 0.95% | 50.0% | 48.7% | 1,006 |
|  | 0 or 0.5 | not short | 7,016 | 52.2% | 3.2% | 3.3% | 58,374 |
| 3c2e | any | short | 2,560 | 71.4% | 76.6% | 76.5% | 22,470 |
|  | any | not short | 1,024 | 28.6% | 24.2% | 24.2% | 8,870 |
| 7c8e | 5 or 6 pairs | short | 1,568 | 6.7% | 95.4% | 95.8% | 11,978 |
|  | 5 or 6 pairs | not short | 2,272 | 9.7% | 33.8% | 34.9% | 18,596 |
|  | 4 pairs | not short | 7,920 | 33.7% | 15.9% | 15.9% | 63,146 |
|  | 3 pairs or fewer | not short | 11,760 | 50.0% | 2.9% | 3.0% | 95,618 |
| 8c8e | corner ARM 0, 4 or 8 | short | 36 | 0.60% | 100% | 100% | 248 |
|  | corner ARM 0, 4 or 8 | not short | 2,624 | 43.6% | 19.4% | 19.6% | 20,754 |
|  | corner ARM 2, 3, 5 or 6 | not short | 3,360 | 55.8% | 9.8% | 9.2% | 27,574 |
| 2c2e | a bad edge with a pair | short | 160 | 8.9% | 95.0% | 96.0% | 1,454 |
|  | a bad edge with a pair | not short | 256 | 14.3% | 37.5% | 35.5% | 2,086 |
|  | no pair, JZP | not short | 144 | 8.0% | 38.9% | 43.9% | 1,284 |
|  | no pair, not JZP | short | 256 | 14.3% | 15.6% | 14.0% | 2,182 |
|  | no pair, not JZP | not short | 976 | 54.5% | 8.2% | 8.2% | 8,194 |
| 4c6e | JZP | short | 320 | 0.34% | 85.0% | 85.4% | 2,348 |
|  | JZP | not short | 256 | 0.27% | 31.3% | 26.9% | 2,008 |
|  | 4 pairs | short | 672 | 0.71% | 73.8% | 75.0% | 5,100 |
|  | 4 pairs | not short | 464 | 0.49% | 10.3% | 10.7% | 3,400 |
|  | anything else | short | 3,552 | 3.8% | 41.9% | 42.5% | 27,718 |
|  | anything else | not short | 88,816 | 94.4% | 2.2% | 2.2% | 680,048 |
| 3c4e | 2 pairs | short | 624 | 3.3% | 52.6% | 51.6% | 5,240 |
|  | 2 pairs | not short | 1,392 | 7.4% | 25.3% | 25.1% | 11,438 |
|  | 0 or 1 pair | short | 1,120 | 6.0% | 17.1% | 17.2% | 9,512 |
|  | 0 or 1 pair | not short | 15,680 | 83.3% | 6.4% | 6.4% | 129,744 |
| 3c6e | any | short | 4,800 | 19.1% | 21.7% | 21.0% | 37,560 |
|  | any | not short | 20,288 | 80.9% | 0.87% | 0.75% | 161,734 |
| 5c4e | 3 pairs | short | 864 | 0.92% | 62.0% | 61.4% | 6,356 |
|  | 3 pairs | not short | 4,896 | 5.2% | 21.6% | 22.4% | 36,964 |
|  | 2 pairs or fewer | short | 2,656 | 2.8% | 41.6% | 43.1% | 19,748 |
|  | 2 pairs or fewer | not short | 85,664 | 91.1% | 4.8% | 4.7% | 647,686 |
| 5c6e | 4 pairs | short | 704 | 0.56% | 77.3% | 75.0% | 5,274 |
|  | 4 pairs | not short | 3,136 | 2.5% | 29.1% | 29.2% | 23,298 |
|  | 3 pairs or fewer | short | 3,136 | 2.5% | 47.4% | 46.7% | 24,394 |
|  | 3 pairs or fewer | not short | 118,464 | 94.4% | 4.0% | 3.9% | 909,550 |
| 6c6e | JZP, or 5 or 6 pairs | short | 448 | 0.32% | 42.9% | 43.0% | 3,378 |
|  | JZP, or 5 or 6 pairs | not short | 1,296 | 0.94% | 37.7% | 34.9% | 10,042 |
|  | anything else | short | 3,328 | 2.4% | 31.0% | 29.8% | 25,050 |
|  | anything else | not short | 132,912 | 96.3% | 4.5% | 4.5% | 1,004,338 |

- **7c8e, 5 or 6 pairs**: short is 95.4% ✓, not short is 33.8% ✓. The card's 59% was an average of those two.
- **4c2e, 1.5+ pairs**: 73.2% ✓ against 30.8% ✓.
- **3c2e**: 76.6% ✓ against 24.2% ✓.
- **2c2e with a paired edge**: 95.0% ✓ against 37.5% ✓.
- **The discards get cleaner too.** 3c6e that is not short is 0.87% ✓ on 80.9% ✓ of it. 4c6e that is not short and has neither JZP nor 4 pairs is 2.2% ✓ on 94.4% ✓.

The real attempts follow the exact rates: in the rows with at least 5,000 attempts the largest gap is 2.7 points.

### 5.6 What of this you can read by hand

- **The 2-side-turn cases**: by hand. They are the trigger cases, and the pictures above are all of them.
- **One half turn before a trigger case**: by hand if you know the trigger pictures. It is the same row-swap look as for 4c4e, one swap deep, towards a picture of section 5.3 instead of two bars. I have no pair-count recipe for it like the 4c4e one.
- **A half turn between the quarter turns**: by hand as a two-step look. Do the R or L turn in your head with the quarter-turn rule of section 4.1 (on that face, good corners come out pointing at the face's edge, corners pointing at it come out good), then read the 4c4e you get with section 4.4.
- **Telling 3 side turns from 4 in general**: that is a search, not a read. If you don't see a short setup, treat the case as not short. The not-short rates above are then a floor for the group you end up with, because it also holds the short cases you missed.

---

## 6. The switch cards, DRM by DRM

These are the best rules if a pair trace is all you do: pairs, side pairs, ARM, JZP, the corner case. The half-turn and side-turn counts of sections 4 and 5 do better where you see the setup, and the two stack (section 5.5).

**The cards.** Exact over all cases of the DRM. Each row is one verdict group of a DRM's card: what to check on the switched case, the share of the DRM that lands in the group, and the group's sub-7 rate. A DRM with no row for a verdict has no such group.

| DRM | Verdict | What the switched case shows | Share of the DRM | Sub-7 rate |
|---|---|---|---|---|
| 4c4e | **switch** | both bad U/D edges paired | 15.5% | 59.9% |
|  | **your call** | one paired, edge ARM 1 (the two bad edges in different slices) | 32.5% | 20.0% |
|  | **discard** | one paired, edge ARM 0 or 2 (both bad edges in one slice); no bad edge paired | 52.0% | 6.7% |
| 4c2e | **switch** | pairs + side pairs/2 is 1.5 or more | 22.3% | 57.0% |
|  | **your call** | pairs + side pairs/2 is exactly 1 | 24.6% | 15.7% |
|  | **discard** | pairs + side pairs/2 is 0 or 0.5 | 53.2% | 4.0% |
| 3c2e | **switch** | always | >99.9% | 61.6% |
| 7c8e | **switch** | 5 or 6 pairs | 16.3% | 59.0% |
|  | **your call** | 4 pairs | 33.7% | 15.9% |
|  | **discard** | 3 pairs or fewer | 50.0% | 2.9% |
| 8c8e | **your call** | corner ARM 0, 4 or 8 | 44.2% | 20.5% |
|  | **discard** | corner ARM 2, 3, 5 or 6 | 55.8% | 9.8% |
| 2c2e | **switch** | a bad U/D edge with a pair | 23.2% | 59.6% |
|  | **your call** | no pair, but JZP | 8.0% | 38.9% |
|  | **discard** | no pair, not JZP | 68.8% | 9.7% |
| 4c6e | **switch** | JZP | 0.61% | 61.1% |
|  | **your call** | 4 pairs | 1.2% | 47.9% |
|  | **discard** | anything else | 98.2% | 3.7% |
| 3c4e | **your call** | 2 pairs | 10.7% | 33.7% |
|  | **discard** | 0 or 1 pair | 89.3% | 7.1% |
| 3c6e | **discard** | always | >99.9% | 4.8% |
| 5c4e | **your call** | 3 pairs | 6.1% | 27.6% |
|  | **discard** | 2 pairs or fewer | 93.9% | 5.9% |
| 5c6e | **your call** | 4 pairs | 3.1% | 37.9% |
|  | **discard** | 3 pairs or fewer | 96.9% | 5.1% |
| 6c6e | **your call** | JZP, or 5 or 6 pairs | 1.3% | 39.0% |
|  | **discard** | anything else | 98.7% | 5.2% |

What each card does to the whole DRM, one row per DRM. *Settled* is the share of the DRM in the switch and discard groups; the last two columns are the shares of the DRM's sub-7 cases that the card switches and that it throws away.

| DRM | Sub-7 rate, whole DRM | Settled (share of the DRM in switch or discard) | Sub-7 states switched (share of the DRM's sub-7s) | Sub-7 states discarded (share of the DRM's sub-7s) |
|---|---|---|---|---|
| 4c4e | 19.2% | 67.5% | 48.2% | 18.0% |
| 4c2e | 18.7% | 75.4% | 67.8% | 11.5% |
| 3c2e | 61.6% | >99.9% | >99.9% | 0% |
| 7c8e | 16.4% | 66.3% | 58.7% | 8.7% |
| 8c8e | 14.5% | 55.8% | 0% | 37.6% |
| 2c2e | 23.7% | 92.0% | 58.5% | 28.3% |
| 4c6e | 4.6% | 98.8% | 8.1% | 79.4% |
| 3c4e | 9.9% | 89.3% | 0% | 63.7% |
| 3c6e | 4.8% | >99.9% | 0% | >99.9% |
| 5c4e | 7.2% | 93.9% | 0% | 76.5% |
| 5c6e | 6.1% | 96.9% | 0% | 81.1% |
| 6c6e | 5.6% | 98.7% | 0% | 91.2% |

How the cards were chosen: every cross-table of one, two or three readable features (38 features, section 11) was scored per DRM by how much of the DRM it puts in cells under 10% or over 50%. A card is the best of the ones a solver can trace, kept only if every labelled cell stays in its band on the cases RZPs reach and on the real attempts. Each verdict above is its group's own band (checked when the tables are built). I timed nothing. The only timing on the server is Yura Riabov's for pairs + ARM on 4c4e, "Like 5 seconds", "±2", "That's for 4c4e btw, for 7c8e it's longer" ([17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417786183135526954), [17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417786220435738704), [17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417787071405490237)). The cards ask for no more than that: a pair trace, and for 4c4e one look at the edges.

**The cards cell by cell, with the RZP length.** Each row is one cell of a card, with its size and its exact sub-7 rate:

| DRM | Cell (read on the switched side) | Verdict | States | Share of the DRM | Sub-7 rate, exact |
|---|---|---|---|---|---|
| 4c4e | both bad U/D edges paired | switch | 10,920 | 15.5% | 59.9% |
|  | one paired, edge ARM 1 (the two bad edges in different slices) | your call | 22,944 | 32.5% | 20.0% |
|  | one paired, edge ARM 0 or 2 (both bad edges in one slice) | discard | 15,696 | 22.2% | 9.8% |
|  | no bad edge paired | discard | 21,000 | 29.8% | 4.3% |
| 4c2e | pairs + side pairs/2 is 1.5 or more | switch | 2,992 | 22.3% | 57.0% |
|  | pairs + side pairs/2 is exactly 1 | your call | 3,304 | 24.6% | 15.7% |
|  | pairs + side pairs/2 is 0 or 0.5 | discard | 7,144 | 53.2% | 4.0% |
| 3c2e | always | switch | 3,584 | >99.9% | 61.6% |
| 7c8e | 5 or 6 pairs | switch | 3,840 | 16.3% | 59.0% |
|  | 4 pairs | your call | 7,920 | 33.7% | 15.9% |
|  | 3 pairs or fewer | discard | 11,760 | 50.0% | 2.9% |
| 8c8e | corner ARM 0, 4 or 8 | your call | 2,660 | 44.2% | 20.5% |
|  | corner ARM 2, 3, 5 or 6 | discard | 3,360 | 55.8% | 9.8% |
| 2c2e | a bad U/D edge with a pair | switch | 416 | 23.2% | 59.6% |
|  | no pair, but JZP | your call | 144 | 8.0% | 38.9% |
|  | no pair, not JZP | discard | 1,232 | 68.8% | 9.7% |
| 4c6e | JZP | switch | 576 | 0.61% | 61.1% |
|  | 4 pairs | your call | 1,136 | 1.2% | 47.9% |
|  | anything else | discard | 92,368 | 98.2% | 3.7% |
| 3c4e | 2 pairs | your call | 2,016 | 10.7% | 33.7% |
|  | 0 or 1 pair | discard | 16,800 | 89.3% | 7.1% |
| 3c6e | always | discard | 25,088 | >99.9% | 4.8% |
| 5c4e | 3 pairs | your call | 5,760 | 6.1% | 27.6% |
|  | 2 pairs or fewer | discard | 88,320 | 93.9% | 5.9% |
| 5c6e | 4 pairs | your call | 3,840 | 3.1% | 37.9% |
|  | 3 pairs or fewer | discard | 121,600 | 96.9% | 5.1% |
| 6c6e | JZP, or 5 or 6 pairs | your call | 1,744 | 1.3% | 39.0% |
|  | anything else | discard | 136,240 | 98.7% | 5.2% |

The same cells on the real attempts at a total of 5 (EO + RZP), and the exact share with a DR in 7 or fewer (enough after a 4-move RZP) and in 5 or fewer (needed after a 6-move RZP):

| DRM | Cell (read on the switched side) | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) | DR in 7 or fewer, exact (for a 4-move RZP) | DR in 5 or fewer, exact (for a 6-move RZP) |
|---|---|---|---|---|---|
| 4c4e | both bad U/D edges paired | 60.0% | 87,468 | 96.1% | 20.1% |
|  | one paired, edge ARM 1 (the two bad edges in different slices) | 19.6% | 180,746 | 73.1% | 2.9% |
|  | one paired, edge ARM 0 or 2 (both bad edges in one slice) | 9.7% | 124,428 | 50.9% | 0.92% |
|  | no bad edge paired | 4.1% | 168,180 | 31.7% | 0.35% |
| 4c2e | pairs + side pairs/2 is 1.5 or more | 57.5% | 25,410 | 98.1% | 14.7% |
|  | pairs + side pairs/2 is exactly 1 | 16.0% | 27,540 | 80.1% | 0% |
|  | pairs + side pairs/2 is 0 or 0.5 | 4.1% | 59,380 | 39.9% | 0.11% |
| 3c2e | always | 61.7% | 31,340 | 98.7% | 19.2% |
| 7c8e | 5 or 6 pairs | 58.8% | 30,574 | 93.8% | 18.3% |
|  | 4 pairs | 15.9% | 63,146 | 73.7% | 0.51% |
|  | 3 pairs or fewer | 3.0% | 95,618 | 34.5% | 0% |
| 8c8e | corner ARM 0, 4 or 8 | 20.5% | 21,002 | 71.5% | 3.2% |
|  | corner ARM 2, 3, 5 or 6 | 9.2% | 27,574 | 56.3% | 0.48% |
| 2c2e | a bad U/D edge with a pair | 60.3% | 3,540 | >99.9% | 11.5% |
|  | no pair, but JZP | 43.9% | 1,284 | >99.9% | 0% |
|  | no pair, not JZP | 9.5% | 10,376 | 79.2% | 0% |
| 4c6e | JZP | 58.4% | 4,356 | 95.8% | 22.2% |
|  | 4 pairs | 49.3% | 8,500 | 90.1% | 15.5% |
|  | anything else | 3.8% | 707,766 | 26.0% | 0.29% |
| 3c4e | 2 pairs | 33.4% | 16,678 | 82.9% | 4.4% |
|  | 0 or 1 pair | 7.2% | 139,256 | 43.8% | 0.57% |
| 3c6e | always | 4.6% | 199,294 | 27.1% | 0.64% |
| 5c4e | 3 pairs | 28.2% | 43,320 | 87.2% | 4.4% |
|  | 2 pairs or fewer | 5.9% | 667,434 | 37.2% | 0.58% |
| 5c6e | 4 pairs | 37.6% | 28,572 | 94.4% | 6.7% |
|  | 3 pairs or fewer | 5.1% | 933,944 | 33.8% | 0.47% |
| 6c6e | JZP, or 5 or 6 pairs | 37.0% | 13,420 | 90.8% | 6.9% |
|  | anything else | 5.1% | 1,029,388 | 32.3% | 0.50% |

So after a 4-move RZP, almost every 4c4e case with a paired edge is a switch, and after a 6-move RZP almost nothing is. The cut-offs that solvers already use ("i'll add 1 to trigger if it's 3c2e specifically", Jay, [27 Sep 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1024463307836506132)) fit this: 3c2e is 19.2% for DR in 5, about what 4c4e with both edges paired is (20.1%).

### 6.1 4c4e

Trace the pairs on the inverse as usual, but keep track of which bad edges they sit on.

1. **Both bad edges paired: switch** (59.9%). With 3 pairs it is 79.0%, with 4 pairs 98.3%.
2. **No bad edge paired: discard** (5.3% at most, whatever the edge ARM).
3. **One paired edge: look at edge ARM** (or just at where the two bad edges are). Both in one slice (edge ARM 0 or 2): **discard**, 9.8%. One in M and one in S (edge ARM 1): **your call**, 20.0%. A bar counts as one paired edge: two pairs on one edge are 26.6%, against 13.3% for a single pair.

By paired edges and edge ARM, one row per cell. *Band* is the cell's verdict band:

| Paired edges, edge ARM | States | Share of the DRM | Sub-7 rate, exact | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) | Band |
|---|---|---|---|---|---|---|
| 0 paired, edge ARM 0 | 4,716 | 6.7% | 3.5% | 3.2% | 39,028 | discard |
| 0 paired, edge ARM 1 | 11,568 | 16.4% | 5.3% | 5.0% | 92,204 | discard |
| 0 paired, edge ARM 2 | 4,716 | 6.7% | 2.9% | 3.0% | 36,948 | discard |
| 1 paired, edge ARM 0 | 7,848 | 11.1% | 10.7% | 10.4% | 62,634 | your call |
| 1 paired, edge ARM 1 | 22,944 | 32.5% | 20.0% | 19.6% | 180,746 | your call |
| 1 paired, edge ARM 2 | 7,848 | 11.1% | 8.9% | 9.0% | 61,794 | discard |
| 2 paired, edge ARM 0 | 2,556 | 3.6% | 55.4% | 54.9% | 21,182 | switch |
| 2 paired, edge ARM 1 | 5,808 | 8.2% | 65.4% | 65.2% | 46,638 | switch |
| 2 paired, edge ARM 2 | 2,556 | 3.6% | 51.9% | 53.1% | 19,648 | switch |

Edge ARM 1 is the same thing as *the two bad edges are in different slices*, so the slice is no extra check once you have ARM. It also matches rodneykinney's slice penalty in *DR - 4c4e Theory*: "The slice penalty applies if you reach 1qt with both bad edges in the same slice." This is the one place where ARM helps a lot on top of pairs, and only the edge digit matters for it.

**The your-call group, split.** If your cut is around 20% ("i switch for around 20% and above", [12 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1272564881358323785)), you can switch all 32.5%: they're 20.0% as a group. With a higher cut, the corner case and the corner ARM split them. Each row is a part of the your-call group, with its share of all 4c4e:

| Inside *one paired, edge ARM 1* | States | Share of the DRM | Sub-7 rate, exact | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) | Band |
|---|---|---|---|---|---|---|
| 4d corners (always corner ARM 2: ARM 21) | 576 | 0.82% | 88.9% | 88.9% | 4,638 | switch |
| corner ARM 2 (ARM 21), 4b corners | 4,512 | 6.4% | 33.0% | 32.9% | 35,476 | your call |
| corner ARM 2 (ARM 21), 4a corners | 2,304 | 3.3% | 18.8% | 17.2% | 17,618 | your call |
| corner ARM 0 or 4, 4a corners | 1,728 | 2.4% | 23.6% | 22.5% | 13,712 | your call |
| corner ARM 1 or 3 (4c corners) | 10,368 | 14.7% | 15.0% | 14.7% | 82,382 | your call |
| corner ARM 0 or 4, 4b corners | 3,456 | 4.9% | 5.6% | 5.4% | 26,920 | discard |

So 4d corners are rare but a near-certain switch (this is Evan's "4d+1 is extremely good for AR-21 (~90% sub-7)", [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418247728328212585)). ARM 21 with 4b corners is a third. Corner ARM 0 or 4 with 4b corners is a discard. So with one paired edge and edge ARM 1: corner ARM 2 means switch if your cut is 30% or less (4b, 4d) and think again with 4a; corner ARM 0 or 4 means switch only with 4a; corner ARM 1 or 3 is 15.0%.

Against the rules in use (section 9). Each row is a group a rule switches or discards, with its share of 4c4e and its sub-7 rate:

| 4c4e group | Share of 4c4e | Sub-7 rate |
|---|---|---|
| *2+ pairs*: switch | 26.0% | 46.4% |
| rodneykinney's pairs + corner case: switch | 25.2% | 49.3% |
| the card: switch | 15.5% | 59.9% |
| *fewer than 2 pairs*: discard | 74.0% | 9.7% |
| the card: discard | 52.0% | 6.7% |

The card's switch group is smaller and better. The new part is the middle: you know which 32.5% are worth a thought.

### 6.2 4c2e

**Pairs + side pairs/2: 1.5 or more, switch; exactly 1, your call; 0 or 0.5, discard.** This is rodneykinney's rule ([30 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1411385391461830769), [30 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1411385789891350698)), and it switches exactly the same cases as Jay's ([14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383640829280780392)) and tseitsei89's ([25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018)). The card adds the discard end (53.2% of 4c2e at 4.0%) and a way to read side pairs from normal (section 7). One row per count of pairs and side pairs:

| Pairs, side pairs | States | Share of the DRM | Sub-7 rate, exact | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) | Band |
|---|---|---|---|---|---|---|
| 0 pairs, 0 side pairs | 4,376 | 32.6% | 1.5% | 1.4% | 37,042 | discard |
| 0 pairs, 1 side pair | 2,768 | 20.6% | 8.1% | 8.4% | 22,338 | discard |
| 0 pairs, 2 side pairs | 536 | 4.0% | 13.4% | 12.6% | 4,270 | your call |
| 1 pair, 0 side pairs | 2,768 | 20.6% | 16.2% | 16.7% | 23,270 | your call |
| 1 pair, 1 side pair | 1,664 | 12.4% | 51.4% | 53.2% | 14,188 | switch |
| 1 pair, 2 side pairs | 368 | 2.7% | 73.9% | 72.6% | 3,078 | switch |
| 2 pairs, 0 side pairs | 536 | 4.0% | 46.3% | 44.7% | 4,490 | your call |
| 2 pairs, 1 side pair | 368 | 2.7% | 76.1% | 75.3% | 3,144 | switch |
| 2 pairs, 2 side pairs | 56 | 0.42% | 85.7% | 92.2% | 510 | switch |

The your-call group is 1 pair and no side pair (16.2%) or 2 side pairs and no pair (13.4%). Two pairs without a side pair are 46.3%, just under the line.

Nothing cheap splits the your-call group well. By corner ARM, edge ARM or corner case every part stays between 8.5% and 25.0%, and the best part is JZP (42.9%, 0.83% of 4c2e). Table in appendix A.

### 6.3 3c2e and 2c2e

**3c2e: always switch** (61.6%). With a pair it is 88.7%, without 45.4%. wen's rule (switch on a pair, a fake pair or a split pair, [12 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1471458126539526323)) switches 82.1% at 71.2% and never drops a case of 5 or less, as wen said.

**2c2e: switch with a paired edge** (59.6%), **your call with no pair but JZP** (38.9%), otherwise discard (9.7%). It's rare, 0.17% of EO-solved cases.

### 6.4 7c8e

**5 or 6 pairs: switch** (59.0%, rodneykinney's "For 7c8e, it's 5 or 6 pairs", [14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383638467736506439)). **3 or fewer: discard** (2.9%). **4 pairs: your call** (15.9%), and here edge ARM is the split. Each row is 4 pairs with one edge ARM:

| Inside *4 pairs* | States | Share of the DRM | Sub-7 rate, exact | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) | Band |
|---|---|---|---|---|---|---|
| 4 pairs, edge ARM 0 | 96 | 0.41% | 0% | 0% | 678 | discard |
| 4 pairs, edge ARM 1 | 1,744 | 7.4% | 30.3% | 30.1% | 13,626 | your call |
| 4 pairs, edge ARM 2 | 4,240 | 18.0% | 10.2% | 10.4% | 34,130 | your call |
| 4 pairs, edge ARM 3 | 1,744 | 7.4% | 17.0% | 16.9% | 14,050 | your call |
| 4 pairs, edge ARM 4 | 96 | 0.41% | 0% | 0% | 662 | discard |

So 4 pairs with edge ARM 1 is worth switching at a 30% cut, and 4 pairs otherwise is not. This is close to tseitsei89's "4 pairs = switch if edge arm < 2" ([25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409426549287157780)). Edge ARM 0 is in it but empty of sub-7s, and it's only 0.41% of 7c8e. By pairs alone, one row per pair count:

| Pairs | States | Share of the DRM | Sub-7 rate, exact | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) | Band |
|---|---|---|---|---|---|---|
| 1 pair | 480 | 2.0% | 0% | 0% | 3,864 | discard |
| 2 pairs | 3,360 | 14.3% | 2.1% | 2.4% | 26,738 | discard |
| 3 pairs | 7,920 | 33.7% | 3.3% | 3.4% | 65,016 | discard |
| 4 pairs | 7,920 | 33.7% | 15.9% | 15.9% | 63,146 | your call |
| 5 pairs | 3,360 | 14.3% | 54.3% | 54.1% | 26,786 | switch |
| 6 pairs | 480 | 2.0% | 91.7% | 91.7% | 3,788 | switch |

ARM on top of pairs adds little: the full pairs × ARM table settles 68.8% of 7c8e, against 66.3% for pairs alone (section 10).

### 6.5 8c8e

**No group is a switch.** The one cheap discard is corner ARM 2, 3, 5 or 6 (55.8% of 8c8e at 9.8%). The rest (corner ARM 0, 4 or 8) is 20.5%, your call. One row per corner ARM:

| Corner ARM | States | Share of the DRM | Sub-7 rate, exact | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) | Band |
|---|---|---|---|---|---|---|
| corner ARM 0 | 70 | 1.2% | 27.1% | 25.9% | 548 | your call |
| corner ARM 2 | 1,120 | 18.6% | 5.0% | 4.9% | 8,942 | discard |
| corner ARM 3 | 560 | 9.3% | 8.6% | 7.6% | 4,538 | discard |
| corner ARM 4 | 2,520 | 41.9% | 20.4% | 20.5% | 19,892 | your call |
| corner ARM 5 | 560 | 9.3% | 14.3% | 14.2% | 4,888 | your call |
| corner ARM 6 | 1,120 | 18.6% | 12.9% | 11.6% | 9,206 | your call |
| corner ARM 8 | 70 | 1.2% | 15.7% | 14.9% | 562 | your call |

Pairs don't help much for 8c8e: the best common pair count, 6, is 32.1% (appendix A). The best 1-3 feature rule needs 65 cells (edge ARM × pairs × the orbit case of the out-of-AR corners) to settle 74.6%, which is **computer only**. The *correct 8c* check (R L gives JZP, Jay [4 Dec 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1181166799610445844), Yura Riabov [23 Mar 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1485595833180360725)) is always sub-7, but it covers 0.020% of 8c8e.

### 6.6 The low DRMs: 4c6e, 3c4e, 3c6e, 5c4e, 5c6e, 6c6e

**Discard**, with these exceptions worth knowing:

- **4c6e JZP: switch** (61.1%, 0.61% of 4c6e), as Yura Riabov said: "You shouldn't switch 6e4c unless it's jzp" ([24 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1265765209050714142)). 4c6e with 4 pairs is 47.9% (Radek B's "Like only if there are 4 pairs (or if it's jzp)", [29 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1278779433225814158)).
- **3c4e with 2 pairs** (33.7%, 10.7% of 3c4e), **5c4e with 3 pairs** (27.6%), **5c6e with 4 pairs** (37.9%), **6c6e with JZP or 5-6 pairs** (39.0%): your call, all rare.
- **3c6e**: no pair count is above 11.1%; Fanti's 3 pairs with ARM 00 or 2 pairs with ARM 21 ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436042954501390401)) is 28.4% on 4.7% of 3c6e, and ARM 21 alone (Jay, [3 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1269432136616771647)) 13.2%.

By pairs, one row per DRM and pair count (JZP as its own row):

| DRM | Pairs on the switched case | States | Share of the DRM | Sub-7 rate, exact | Band |
|---|---|---|---|---|---|
| 4c6e | 0 pairs | 12,800 | 13.6% | 0.13% | discard |
|  | 1 pair | 35,200 | 37.4% | 0.80% | discard |
|  | 2 pairs | 33,600 | 35.7% | 4.8% | discard |
|  | 3 pairs | 11,200 | 11.9% | 16.1% | your call |
|  | 4 pairs | 1,280 | 1.4% | 50.6% | switch |
|  | JZP | 576 | 0.61% | 61.1% | switch |
| 3c4e | 0 pairs | 6,720 | 35.7% | 2.7% | discard |
|  | 1 pair | 10,080 | 53.6% | 10.0% | your call |
|  | 2 pairs | 2,016 | 10.7% | 33.7% | your call |
| 3c6e | 0 pairs | 4,480 | 17.9% | 0.89% | discard |
|  | 1 pair | 13,440 | 53.6% | 2.9% | discard |
|  | 2 pairs | 6,720 | 26.8% | 11.1% | your call |
|  | 3 pairs | 448 | 1.8% | 8.9% | discard |
| 5c4e | 0 pairs | 15,840 | 16.8% | 1.4% | discard |
|  | 1 pair | 44,640 | 47.4% | 4.4% | discard |
|  | 2 pairs | 27,840 | 29.6% | 10.8% | your call |
|  | 3 pairs | 5,760 | 6.1% | 27.6% | your call |
| 5c6e | 0 pairs | 6,080 | 4.8% | 0.13% | discard |
|  | 1 pair | 37,440 | 29.8% | 1.2% | discard |
|  | 2 pairs | 51,840 | 41.3% | 4.7% | discard |
|  | 3 pairs | 26,240 | 20.9% | 12.7% | your call |
|  | 4 pairs | 3,840 | 3.1% | 37.9% | your call |
| 6c6e | 0 pairs | 4,864 | 3.5% | 0% | discard |
|  | 1 pair | 25,920 | 18.8% | 2.0% | discard |
|  | 2 pairs | 52,800 | 38.3% | 3.1% | discard |
|  | 3 pairs | 40,320 | 29.2% | 8.3% | discard |
|  | 4 pairs | 12,480 | 9.0% | 12.8% | your call |
|  | 5 pairs | 1,536 | 1.1% | 37.5% | your call |
|  | 6 pairs | 64 | 0.046% | 75.0% | switch |
|  | JZP | 256 | 0.19% | 50.0% | your call |

Together these exceptions catch few of the sub-7 cases: 8.1% of 4c6e's in its switch group. No rule of up to three of those features does much better (section 11). A short setup does (section 5.5).

---

## 7. Reading the switched case from normal

You decide before switching, so every feature of the cards has to be seen on the normal side, after EO + RZP. I tested each reading below on uniformly random cubes with the EO solved (a random case, then random pieces): read it on the normal cube, compare with the feature of its inverse. One row per feature; *Held* is on how many of the cubes tested the reading gave the right count.

| Feature on the switched case | What to look at on normal | Source | Held (cubes right of cubes tested) |
|---|---|---|---|
| The two rings and the holes | **each U/D edge in the E slice marks its own edge place; each misoriented corner marks its own corner place and points at the edge place of its U/D colour and the side colour that is not showing on the U/D face; each E-slice edge in the U or D layer marks its own slot** | new here (wen's pair tracing, kept for every corner) | 20,000 of 20,000 |
| Corner ARM | R/L stickers on the U/D faces (corners) | rodneykinney, *DR - 4c4e Theory* | 20,000 of 20,000 |
| ARM (both digits) | the ARM of the other DR axis on normal (U/D DR on inverse ↔ R/L DR on normal) | Cale [3 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1213932643188473896), wen [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285751016545058853) | 20,000 of 20,000 |
| Edge ARM | **the U/D edges sitting in the E slice whose other colour is the EO axis's (green/blue for F/B EO)**: how many | new here | 20,000 of 20,000 |
| Pairs | each U/D edge in the E slice, against each misoriented corner: a corner whose two stickers touching the E slice show the edge's colours is a pair on inverse | wen, *Hitchhiker's Guide to DR*; rodneykinney, *Domino Setup Theory* | 20,000 of 20,000 |
| Paired edges | the same tracing, counting the U/D edges in the E slice that find at least one such corner | new here (a count of the same tracing) | 20,000 of 20,000 |
| Side pairs | **each E-slice edge sitting in the U or D layer, against each misoriented corner that carries both its colours: one side pair if the corner shows its green/blue sticker (the EO axis's colour) on the U/D face** | new here | 20,000 of 20,000 |
| Corner case (4a-4d) | the flow chart of *DR - 4c4e Theory* on the misoriented corners' colours | rodneykinney | 20,000 of 20,000 (4c4e) |

The pair tracing is wen's, as the guide puts it: "look at one of the edges in the E slice that don't belong there, then look at a misoriented corner, if the 2 stickers on the corner that are touching the E slice match with that E slice edge, then that's a pair on inverse". For the 4c4e card, note which E-slice edge each matching corner belongs to: two different edges is *both paired*. The corner-ARM count is rodneykinney's: "It's easy to predict how many corners will be out of AR on inverse: count the number of R/L stickers on the U/D face."

**The two rings.** A piece that is out of place on normal marks its *own* place on the inverse. So the inverse's U ring is your U-coloured pieces and its D ring your D-coloured pieces, and you fill in the rings of section 4.1 by colour: with white on U and green on F, the U ring is white-blue, white-blue-red, white-red, white-red-green, white-green, white-green-orange, white-orange, white-orange-blue.

- A ring edge place is bad if that edge is sitting in the E slice.
- A ring corner place is bad if that corner is misoriented, wherever it is. To point it, look at which of its two side colours shows on the U or D face: it points at the edge place of its U/D colour and the *other* side colour. That is wen's tracing read the other way round: the corner's two stickers on the side faces are its U/D colour and that other colour.
- The holes are the E-slice edges sitting in the U or D layer. For the hole number look at what the two of them share: an R/L colour (red or orange) is 0, nothing is 1, an F/B colour (green or blue) is 2.

```
white-red edge in the E slice                   // UR is bad
white-red-green corner, green on the U/D face   // UFR points at UR: a pair
white-blue-red corner, red on the U/D face      // UBR points at UB, away from UR: a fake pair
```

This gave both rings and the holes of the inverse, place for place, on 20,000 of 20,000 uniform cubes and 20,000 of 20,000 4c4e cubes, and the half turns to two bars counted from it matched on all 20,000 of the 4c4e ones. The control, pointing each corner at the other edge place, was right on 5 of 20,000.

**Edge ARM without changing axes.** The inverse's bad U/D edges are, piece for piece, the U/D edges sitting in the E slice on normal. One whose other colour is green or blue (F/B EO) belongs in the M slice, so it is an edge in M on the inverse. So for 4c4e, *edge ARM 1* on the switched case means exactly one of the two U/D edges in the E slice has a green/blue sticker. Jay's colour rule reads the same thing through the other axis ("the unsolved belt edges (edges in E that belong in U) with green/blue on RL as being not in AR", [28 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1223072354956218589)). This version reads it straight off the edges you trace for pairs anyway.

**Side pairs.** The 4c2e card needs side pairs on the inverse, and I found no tracing for them on the server. Jay said why they matter: "Side pair stats would be valuable simply because NISS EO's don't destroy them unlike top pairs" ([29 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1278843980397674547)). The tracing in the table mirrors pair tracing: the E-slice edges that are out of the E slice (in U or D) play the edge, and the corner must carry both of the edge's colours and show its green or blue sticker on U or D. The control, the same count with the red or orange sticker on U or D, gives the right number on only 4,290 of 20,000 cubes, so the colour test is the whole rule.

The side-pair, edge-ARM and paired-edge readings also held on 20,000 cubes drawn from 4c2e and 20,000 from 4c4e. They're checked by sampling, not proved.

The same-axis version of the ARM swap is wrong, as its author said at the time: Louis wrote "It remains the same on the same axis." ([28 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1222965074398806066)) and then "Yes you're right it makes total sense" ([28 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1222967992015654952)). It holds on 2,087 of 20,000 cubes.

---

## 8. Real RZPs: does the uniform table apply after a switch?

Every table on the server counts each case once. Real cases come from RZPs, and torchlight pointed out why that matters: "if the EO isn't already 4c4e, it means that the 4c4e case you get from RZP is 1 move away from something that is not 4c4e", "the 4c4e cases that can go out of 4c4e in more ways will thus be more likely to show up" ([8 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215720321995382867)). KrzychXyz asked whether natural 4c4e is therefore better ([9 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1216123557776461895)). Here's the sub-7 rate by DRM, uniform against the cases RZPs reach (exact counts over every 5-move RZP from a uniform EO-solved cube) and against the real attempts. One row per DRM; the last column is how many real attempts the RZP-to-5 rate rests on:

| DRM | Sub-7 rate, uniform (the tables) | Sub-7 rate after an RZP of 5, same side | Sub-7 rate after an RZP of 5, switched | Sub-7 rate, real attempts, RZP to 5, switched | DR in 5 or fewer, real attempts, RZP to 6, switched | Real attempts (RZP to 5) |
|---|---|---|---|---|---|---|
| 4c4e | 19.2% | 18.3% | 19.2% | 19.1% | 4.3% | 560,822 |
| 4c2e | 18.7% | 17.9% | 18.7% | 19.1% | 3.3% | 112,330 |
| 3c2e | 61.6% | 61.3% | 61.6% | 61.7% | 19.2% | 31,340 |
| 7c8e | 16.4% | 15.8% | 16.4% | 16.3% | 3.1% | 189,338 |
| 8c8e | 14.5% | 14.4% | 14.5% | 14.1% | 1.6% | 48,576 |
| 2c2e | 23.7% | 23.4% | 23.7% | 24.2% | 2.6% | 15,200 |
| 4c6e | 4.6% | 4.9% | 4.6% | 4.7% | 0.61% | 720,622 |
| 3c4e | 9.9% | 9.7% | 9.9% | 10.0% | 0.96% | 155,934 |
| 3c6e | 4.8% | 4.8% | 4.8% | 4.6% | 0.60% | 199,294 |
| 5c4e | 7.2% | 6.9% | 7.2% | 7.2% | 0.82% | 710,754 |
| 5c6e | 6.1% | 6.1% | 6.1% | 6.0% | 0.65% | 962,516 |
| 6c6e | 5.6% | 5.7% | 5.6% | 5.6% | 0.59% | 1,042,810 |

**On the same side the bias is real but small** (4c4e 19.2% against 18.3%).

**After the switch it is gone exactly.** The inverse of a cube is uniform over the cubes with the same case (twist counts swapped, the same E-slice edges out), whatever path made the case. So the switched case is uniform, and an RZP's choice only picks the DRM. For every named DRM except 6cXe and 8cXe that leaves nothing to choose (one class, or two mirror classes with equal rates), and for those two the mix of twist splits (4+4 or 7+1 for 8c8e) could shift, which the test on real attempts below covers. So **the exhaustive tables, and the cards, are exactly right for switched RZPs.**

The real attempts agree. In 36 cells (12 DRMs × RZP to 4, 5 or 6), the attempts' rate is never more than 2.63 standard errors from the uniform rate of their own mix (errors from 20 batches of 300 scrambles). This also answers KrzychXyz: natural cases are slightly better on the same side and identical after a switch.

**RZP length.** The last column of the table is the real attempts with a 6-move RZP, where the target is DR in 5. The rates fall by a factor of 3.2 to 10.3, which is why solvers use a shorter cut for 6-move RZPs. The cards give DR in 5 and DR in 7 for every cell (section 6).

**The last turns after a switch.** Turning the RZP's last move the other way never changes the switched case: in 114,102 of 114,102 pairs of real attempts that differ only in that, the switched case is the same. The reason: on the inverse that move becomes the first premove, and a premove from the DR group (R and R' differ by R2) doesn't change which pieces are twisted or which places hold E-slice edges relative to home. So Jay's idea of looking at the case when you "flip" the RZP ([6 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1358302313076363294)) doesn't help after a switch. The EO's last turn still counts, but much less than without a switch, because the RZP sits between it and the inverse. On the real attempts at a total of 5, one row per DRM, the sub-7 rate after a switch, then with each option added:

| DRM | Sub-7 rate, switched | Sub-7 rate, also EO's last turn either way | Sub-7 rate, also the better DR axis | Sub-7 rate, both |
|---|---|---|---|---|
| 4c4e | 19.1% | 21.2% | 25.0% | 27.4% |
| 4c2e | 19.1% | 21.9% | 26.0% | 29.1% |
| 3c2e | 61.7% | 63.2% | 65.8% | 67.5% |
| 7c8e | 16.3% | 17.9% | 20.3% | 22.3% |
| 8c8e | 14.1% | 16.2% | 18.8% | 21.2% |

Without a switch the EO's last turn takes 4c4e from 19.2% to 28.1%, Tom Nelson's "1 in 3.6 if you can switch the last move" ([13 Jul 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1128948555684519946)). After a switch it adds only 2.1 points. Checking the other DR axis is worth more (5.9 points).

The two axes are close to independent, as caycala assumed ([16 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417554347738267838)): for 4c4e the better of the two is 25.4% against 25.7% if they were independent.

---

## 9. The existing rules, graded

Every rule from the server I could pin down, graded the same way on the switched case, one rule per row. *Switches*: the share of the DRM it switches. *Sub-7 among switched*: how often a switch finds a DR in 6 (precision). *Sub-7 states switched*: the share of the DRM's sub-7 cases it switches (recall). *Sub-7 states discarded*: sub-7 cases it throws away, as a share of all the DRM's cases. Exact, every case once. The last column is the same precision on the real attempts at a total of 5. The card's rows come first (bold), then the rules by precision. The two 4-move rules (Daichi, Zagros) are graded against DR in 7 and Fanti's 6-move 3c2e rule against DR in 5, since that's what they're for.

| DRM | Switch when | Who | Switches (share of the DRM) | Sub-7 among switched | Sub-7 states switched (share of the DRM's sub-7s) | Sub-7 states discarded (share of the DRM) | Real attempts: sub-7 among switched |
|---|---|---|---|---|---|---|---|
| 4c4e | **both bad U/D edges paired** | **this study** (switch) | 15.5% | 59.9% | 48.2% | 10.0% | 60.0% |
|  | **both bad edges paired, or one paired with edge ARM 1** | **this study** (switch + your call) | 48.0% | 32.9% | 82.0% | 3.5% | 32.8% |
|  | 3+ pairs unless all bad corners on one layer | caycala [11 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404468988070727700) | 3.4% | 81.6% | 14.4% | 16.5% | 81.5% |
|  | RZP in 6: 3-4 pairs, or 0 pairs with 42 | caycala (chart) [25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1365334546035245227) | 3.6% | 80.0% | 15.1% | 16.3% | 79.7% |
|  | 3+ pairs | rodneykinney, *Domino Setup Theory* | 3.6% | 79.9% | 14.8% | 16.4% | 79.7% |
|  | RZP in 4 (DR in 7): 2-4 pairs; 1 pair except 20d, 22d; 0 pairs except 02, 30, 40, 01b, 41b, 20d, 2c with all corners on U | Daichi [7 Jul 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1524192731432353853) | 90.6% | 63.9% | 97.5% | 1.5% | 63.5% |
|  | RZP in 4 (DR in 7): always | Zagros [7 Jul 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1524175174507692245) | >99.9% | 59.4% | >99.9% | 0% | 59.0% |
|  | 3-4 pairs; 2 pairs unless 4b-0; 1 pair if 4d-2 | rodneykinney [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383069263530692730) | 25.2% | 49.3% | 64.6% | 6.8% | 49.5% |
|  | 4d needs 1+ pair, 4b-0 3+, everything else 2+ | rodneykinney [21 Jun 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1385956016885338144) | 25.2% | 49.3% | 64.6% | 6.8% | 49.5% |
|  | caycala's RZP-in-5 chart without the bracketed (10), (11), (20), (31) | caycala (chart) [25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1365334546035245227) | 19.8% | 49.2% | 50.6% | 9.5% | 49.1% |
|  | 3-4 pairs; 2 pairs unless 4b-0; 1 pair if 4d-2; 0 pairs if 4a-0 or 4d-2 with no fake pairs | rodneykinney [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383069263530692730) [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383075044682633366) | 25.4% | 49.1% | 64.8% | 6.8% | 49.3% |
|  | ARM above 10% sub-7, then 2+ pairs | Yura Riabov [25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1365335058755489932) | 23.6% | 48.8% | 59.8% | 7.7% | 49.1% |
|  | 3+ pairs; 2 pairs unless 4b; 1 pair only if 4d | compLex [11 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404500827628113920) | 19.9% | 48.6% | 50.3% | 9.6% | 48.5% |
|  | per corner case: 4a-0 2+p, 4a-2 1+p, 4a-4 edge ARM 2, 4b-0 3+p, 4b-2 2+p and edge ARM 1, 4c 2+p, 4d 1+p and edge ARM 1 | rodneykinney, *DRM Subsets* | 26.7% | 47.0% | 65.2% | 6.7% | 46.9% |
|  | 2+ pairs | Jay [26 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1068170469007687721), rodneykinney [20 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1154070313554956380), tseitsei89 [17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417807554448195655) [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409603207239307457) | 26.0% | 46.4% | 62.8% | 7.2% | 46.6% |
|  | 2+ pairs, or 1 pair and 4d | tseitsei89 [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018) | 27.7% | 46.3% | 66.5% | 6.4% | 46.5% |
|  | RZP in 5: 3-4 pairs; 2 pairs with ARM 10, 11, 20, 21, 31, 32, 42a; 1 pair with 21; 0 pairs with 42 | caycala (chart) [25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1365334546035245227) | 29.5% | 45.6% | 69.8% | 5.8% | 45.5% |
|  | 2+ pairs; fewer only if JZP or anti-JZP, or 1 pair and 4d | Jay [21 Jun 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1385890589886775387) | 28.6% | 45.4% | 67.4% | 6.3% | 45.5% |
|  | 2+ pairs; 1 pair if 4d or one U/D turn from 4d; 0 pairs if anti-AR | wen [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418234619014283346) [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418248140372574260) | 29.3% | 45.4% | 69.2% | 5.9% | 45.5% |
|  | 2+ pairs; 1 pair with ARM 21; 0 pairs with JZP or ARM 42 | Fanti, *armpairs_1.txt* [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069) | 35.2% | 42.6% | 78.0% | 4.2% | 42.6% |
|  | 3+ pairs counting side pairs | rodneykinney's older advice, as Jay put it [26 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1068170469007687721) | 32.0% | 38.7% | 64.3% | 6.9% | 38.7% |
|  | ARM 00, 10, 21, 32, 42 ("good") | Yura Riabov [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285700941156323420) [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285700969795158128), Lewis Isom [12 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1272720588355665990) | 34.7% | 33.6% | 60.6% | 7.6% | 33.5% |
|  | the "good" ARMs and the "decent" 31, 11 | Yura Riabov [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285700969795158128) | 60.8% | 26.7% | 84.5% | 3.0% | 26.6% |
|  | anything but ARM 02, 12, 30, 40 | Yura Riabov [12 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1272565146916749436) | 86.5% | 21.8% | 98.2% | 0.34% | 21.7% |
|  | anything but ARM 01, 02, 12 | wen [19 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1275251294470410252) [19 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1275251364666019971) | 88.4% | 21.1% | 97.0% | 0.57% | 20.9% |
| 4c2e | **pairs + side pairs/2 is 1.5 or more** | **this study** (switch) | 22.3% | 57.0% | 67.8% | 6.0% | 57.5% |
|  | **pairs + side pairs/2 is 1 or more** | **this study** (switch + your call) | 46.8% | 35.3% | 88.5% | 2.1% | 36.0% |
|  | 1+ pair and 1+ side pair | rodneykinney [24 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409202165154844775), *DRM Subsets* | 18.3% | 59.3% | 58.0% | 7.9% | 60.3% |
|  | 1 pair and 1 side pair, or 2 pairs | Jay [14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383640829280780392) | 22.3% | 57.0% | 67.8% | 6.0% | 57.5% |
|  | 2 pairs, or 1 pair and a side pair | tseitsei89 [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018) | 22.3% | 57.0% | 67.8% | 6.0% | 57.5% |
|  | "1.5+ pairs" (pairs + side pairs/2) | rodneykinney [30 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1411385789891350698) | 22.3% | 57.0% | 67.8% | 6.0% | 57.5% |
|  | 2 pairs unless 4a; 1 pair unless 4a or 4b-2 | rodneykinney (table) [14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383638325281292389) | 27.1% | 42.5% | 61.8% | 7.1% | 43.7% |
|  | 2 pairs; 1 pair with edge ARM 1 or ARM 10; 0 pairs only JZP | caycala [16 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1395148255540678656) | 31.8% | 40.5% | 68.8% | 5.8% | 41.0% |
|  | any pair; 0 pairs with JZP | Fanti, *armpairs_1.txt* [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069) | 43.9% | 37.7% | 88.5% | 2.1% | 38.2% |
|  | ARM 00, 10, 31 | Noah Swor [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285692209844191306), Lewis Isom [12 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1272720588355665990) | 27.1% | 35.1% | 51.0% | 9.2% | 35.6% |
|  | ARM 00, 10, 31, 20, 21, 41 | Noah Swor, Yura Riabov [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285692209844191306) [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285692271005794425) [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285692301380681871) | 68.6% | 24.7% | 90.8% | 1.7% | 24.8% |
| 3c2e | **always** | **this study** (switch) | >99.9% | 61.6% | >99.9% | 0% | 61.7% |
|  | a pair, a fake pair or a split pair | wen [12 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1471458126539526323) | 82.1% | 71.2% | 94.9% | 3.1% | 71.2% |
|  | always | rodneykinney [24 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409268902478876906), tseitsei89 [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018) [20 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1275330107661352970) | >99.9% | 61.6% | >99.9% | 0% | 61.7% |
|  | RZP in 6 (DR in 5): a pair; 0 pairs with ARM 00, 21, 31 | Fanti, *armpairs_1.txt* [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069) | 50.0% | 34.4% | 89.5% | 2.0% | 34.7% |
| 7c8e | **5 or 6 pairs** | **this study** (switch) | 16.3% | 59.0% | 58.7% | 6.8% | 58.8% |
|  | **4 or more pairs** | **this study** (switch + your call) | 50.0% | 29.9% | 91.3% | 1.4% | 29.9% |
|  | ARM 10, 21, 11, 63 | Lewis Isom [12 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1272720588355665990) | 6.6% | 61.5% | 24.9% | 12.3% | 60.7% |
|  | 5 or 6 pairs | rodneykinney [14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383638467736506439) | 16.3% | 59.0% | 58.7% | 6.8% | 58.8% |
|  | drop the 0% ARMs, then 5+ pairs, or 4 pairs with edge ARM under 2 | tseitsei89 [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018) | 22.6% | 52.5% | 72.4% | 4.5% | 52.3% |
|  | 5-6 pairs; 4 pairs with ARM 21, 31, 43; 3 pairs with 21 | chart attached to Brayan's question [17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1406659474386849834) | 23.5% | 51.4% | 73.7% | 4.3% | 51.0% |
|  | 5+ pairs; 4 pairs with ARM 21, 31, 43; 3 pairs with 21 | Fanti, *armpairs_1.txt* [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069) | 23.5% | 51.4% | 73.7% | 4.3% | 51.0% |
|  | 5 pairs; 4 pairs with edge ARM under 2 | tseitsei89 [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409426549287157780) | 24.1% | 49.1% | 72.4% | 4.5% | 49.2% |
|  | 4+ pairs, then edge ARM under 2, or edge ARM 1 or 3 and corner ARM over 3 | tseitsei89 [24 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409257386622845080) | 20.3% | 43.0% | 53.3% | 7.6% | 43.0% |
| 8c8e | R L (one R/L quarter-turn pair) gives JZP | Jay [4 Dec 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1181166799610445844), Yura Riabov [23 Mar 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1485595833180360725) | 0.020% | >99.9% | 0.11% | 14.5% | >99.9% |
|  | ARM 00, 84, 01, 31, 63 | Lewis Isom [12 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1272720588355665990) | 6.7% | 38.3% | 17.7% | 11.9% | 33.2% |
|  | 3+ fake pairs and edge ARM not 2 | tseitsei89 [2 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412521094816075866) [2 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412521849803247656) | 44.3% | 15.3% | 46.8% | 7.7% | 14.7% |
| 2c2e | **a bad U/D edge with a pair** | **this study** (switch) | 23.2% | 59.6% | 58.5% | 9.8% | 60.3% |
|  | **a paired edge, or JZP** | **this study** (switch + your call) | 31.3% | 54.3% | 71.7% | 6.7% | 56.0% |
|  | 1+ pairs | rodneykinney, *DRM Subsets Meta* | 23.2% | 59.6% | 58.5% | 9.8% | 60.3% |
| 4c6e | **JZP** | **this study** (switch) | 0.61% | 61.1% | 8.1% | 4.2% | 58.4% |
|  | **JZP or 4 pairs** | **this study** (switch + your call) | 1.8% | 52.3% | 20.6% | 3.7% | 52.4% |
|  | JZP with b corners | tseitsei89 [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018) | 0.41% | 79.2% | 7.0% | 4.3% | 77.4% |
|  | only JZP | Yura Riabov [24 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1265765209050714142), *Hitchhiker's Guide to DR* | 0.61% | 61.1% | 8.1% | 4.2% | 58.5% |
|  | 4 pairs or JZP | Radek B [29 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1278779433225814158) [29 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1278779665435328555) | 1.8% | 52.3% | 20.6% | 3.7% | 52.4% |
|  | 3+ pairs and corner ARM under 4 | rodneykinney, *DRM Subsets* | 11.9% | 20.2% | 51.9% | 2.2% | 20.5% |
| 3c4e | 2+ pairs | rodneykinney [27 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1388031252090585169), *DRM Subsets* | 10.7% | 33.7% | 36.3% | 6.3% | 33.4% |
|  | 2 pairs; 1 pair with ARM 00 or 21 | Fanti [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436042954501390401) | 23.7% | 26.0% | 62.0% | 3.8% | 26.4% |
| 3c6e | 3 pairs with ARM 00, or 2 pairs with ARM 21 | Fanti [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436042954501390401) | 4.7% | 28.4% | 27.6% | 3.5% | 27.6% |
|  | ARM 21 only | Jay [3 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1269432136616771647) | 18.4% | 13.2% | 50.0% | 2.4% | 12.3% |
| 5c4e | 3+ pairs | rodneykinney, *DRM Subsets Meta* | 6.1% | 27.6% | 23.5% | 5.5% | 28.2% |
|  | 2+ pairs and 2+ side pairs | rodneykinney, *DRM Subsets* | 12.8% | 23.1% | 40.8% | 4.3% | 22.8% |
| 5c6e | 4+ pairs | rodneykinney, *DRM Subsets Meta* | 3.1% | 37.9% | 18.9% | 5.0% | 37.6% |
| 6c6e | 3+ pairs | rodneykinney, *DRM Subsets Meta* | 39.4% | 10.2% | 72.0% | 1.6% | 10.3% |

**The counts of sections 4 and 5 as switch rules**, in the same columns. One row per rule:

| DRM | Switch when | Switches (share of the DRM) | Sub-7 among switched | Sub-7 states switched (share of the DRM's sub-7s) | Sub-7 states discarded (share of the DRM) | Real attempts: sub-7 among switched |
|---|---|---|---|---|---|---|
| 4c4e | 1 half turn or fewer to two bars | 1.0% | 100% | 5.3% | 18.2% | 100% |
|  | 2 half turns or fewer to two bars | 14.2% | 74.1% | 54.7% | 8.7% | 74.2% |
|  | 3 half turns or fewer to two bars | 65.2% | 28.6% | 97.0% | 0.58% | 28.5% |
| 4c2e | 2 side turns or fewer | 0.95% | 100% | 5.1% | 17.7% | 100% |
|  | short: 3 side turns or fewer, 2 of them quarter turns | 23.3% | 57.4% | 71.7% | 5.3% | 57.6% |
| 3c2e | 2 side turns or fewer | 7.1% | 100% | 11.6% | 54.5% | 100% |
|  | short: 3 side turns or fewer, 2 of them quarter turns | 71.4% | 76.6% | 88.8% | 6.9% | 76.5% |
| 7c8e | 2 side turns or fewer | 0.41% | 100% | 2.5% | 16.0% | 100% |
|  | short: 3 side turns or fewer, 2 of them quarter turns | 6.7% | 95.4% | 38.8% | 10.0% | 95.8% |
| 8c8e | 2 side turns or fewer | 0.066% | 100% | 0.46% | 14.4% | 100% |
|  | short: 3 side turns or fewer, 2 of them quarter turns | 0.60% | 100% | 4.1% | 13.9% | 100% |
| 2c2e | short: 3 side turns or fewer, 2 of them quarter turns | 23.2% | 46.2% | 45.3% | 12.9% | 46.8% |
| 4c6e | 2 side turns or fewer | 0.14% | 100% | 2.9% | 4.5% | 100% |
|  | short: 3 side turns or fewer, 2 of them quarter turns | 4.8% | 49.6% | 51.9% | 2.2% | 50.1% |
| 3c4e | short: 3 side turns or fewer, 2 of them quarter turns | 9.3% | 29.8% | 27.8% | 7.2% | 29.4% |
| 3c6e | 2 side turns or fewer | 1.0% | 100% | 21.1% | 3.8% | 100% |
|  | short: 3 side turns or fewer, 2 of them quarter turns | 19.1% | 21.7% | 85.5% | 0.70% | 21.0% |
| 5c4e | short: 3 side turns or fewer, 2 of them quarter turns | 3.7% | 46.6% | 24.2% | 5.5% | 47.6% |
| 5c6e | short: 3 side turns or fewer, 2 of them quarter turns | 3.1% | 52.9% | 26.4% | 4.5% | 51.7% |
| 6c6e | short: 3 side turns or fewer, 2 of them quarter turns | 2.7% | 32.4% | 15.9% | 4.7% | 31.4% |

What the table says:

- **Real attempts change nothing.** The last column is close to the exact precision everywhere (the RZP bias is gone after a switch, section 8). The largest gap is Lewis Isom's 8c8e list, a small and rare group (38.3% exact, 33.2% in attempts).
- **4c4e.**
  - The rules built on 2+ pairs all land between 45.4% and 49.3% precision while switching 19.8% to 29.5% of 4c4e. Corner-case refinements (rodneykinney, compLex, tseitsei89, Jay, wen) move each by a point or two.
  - ARM-only rules switch more at lower precision. Yura Riabov's "good" list is 33.6%, and *anything but trash* keeps almost every sub-7 at 21.8%. Those are discard rules, and good ones: Yura Riabov's four "trash" ARMs throw away only 0.34% of 4c4e as lost sub-7s.
  - Fanti's rule switches the most of the pair rules (35.2%) and keeps 78.0% of the sub-7s.
- **The 4c4e card** gives a smaller, better switch group, and with the your-call group added it keeps 82.0% of the sub-7s, more than any pair rule, at 32.9%.
- **The half-turn count** beats every 4c4e row above at its own size: *2 half turns or fewer* switches 14.2% at 74.1%, where the pair rules of that size are at 59.9% or less, and *3 or fewer* keeps 97.0% of the sub-7s while dropping 34.8% of 4c4e. It costs a look where the others cost a count (section 4.4).
- **4c2e.** Four rules are the same rule ("1.5+ pairs"); rodneykinney's stricter 1 pair and 1 side pair is a little more precise and switches less. ARM-only rules are well behind.
- **7c8e.** 5-6 pairs is the core. The rules that add 4-pair cases by ARM (the chart in Brayan's question [17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1406659474386849834), Fanti, tseitsei89) keep about three quarters of the sub-7s at about 50%. Lewis Isom's ARM list is precise (61.5%) but switches only 6.6%.
- **8c8e.** No rule is both precise and common. tseitsei89's fake-pair rule is 15.3%, about the 8c8e base rate (14.5%).
- **The low DRMs.** The rules there either switch a few percent of cases or switch at about the base rate. The best is 4c6e JZP with b corners (tseitsei89, 79.2% on 0.41%).

---

## 10. What each feature adds

**How much each settles.** Exact. Each row is a feature (or two) to split by, using every value it takes; each cell is the share of that DRM that lands in cells under 10% or over 50%.

| Split by | 4c4e: settled | 4c2e: settled | 7c8e: settled | 8c8e: settled | 2c2e: settled |
|---|---|---|---|---|---|
| ARM | 31.2% | 35.7% | 32.2% | 43.0% | 42.9% |
| Pairs | 33.3% | 64.3% | 66.3% | 24.1% | 21.4% |
| Paired edges | 45.2% | 57.1% | 34.0% | 24.8% | 23.2% |
| Corner case (4 corners) | 11.4% | 2.9% | 0% | 0% | 0% |
| Pairs + ARM | 49.6% | 63.2% | 68.8% | 62.1% | 45.5% |
| Pairs + corner case | 43.6% | 64.6% | 66.3% | 24.1% | 21.4% |
| Paired edges + edge ARM | 56.4% | 57.1% | 43.2% | 40.2% | 11.6% |
| Pairs + side pairs/2 | 51.9% | 75.4% | 54.7% | 24.8% | 81.7% |

- **Pairs settle more than ARM** in 4c4e, 4c2e and 7c8e. In 8c8e and 2c2e ARM settles more. The corner case alone settles little anywhere: it is a refinement, not a first look. rodneykinney's corner orbit case is only worth reading inside a pair group (4c4e: the your-call group, section 6.1).
- **For 4c4e, the edges matter more than the count.** Paired edges plus edge ARM (56.4% with all 9 cells, 67.5% once edge ARM 0 and 2 are pooled as on the card) beat pairs + ARM (49.6%) and pairs + corner case (43.6%).

**The half-turn count against all of them** (4c4e). By the 10%/50% yardstick the count alone settles 49.0%, less than the paired-edge card (67.5%), because its middle row, 3 half turns, is half of 4c4e at 16.0%. Its ends are much further out though: 100% and 1.7%, where the card's are 59.9% and 6.7%. With side pairs inside the 3 (none, one, two or more) it settles 64.8%. In information terms (section 11), each row is what you know and the share of the uncertainty about sub-7 it removes, **computer only** as a measure:

| What you know (4c4e) | Share of the uncertainty about sub-7 removed |
|---|---|
| ARM | 0.098 |
| pairs | 0.191 |
| paired edges and edge ARM (the card) | 0.204 |
| pairs and ARM | 0.262 |
| side turns | 0.241 |
| half turns to two bars | 0.324 |
| half turns and pairs | 0.333 |
| half turns and ARM | 0.351 |
| half turns, pairs and side pairs | 0.370 |

So the count carries more than pairs and ARM together, and neither adds much to it. What is missing is how the layers line up (section 4.5).

**wen's 2 of 3** ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418248619374678247)): switch the best 26.0% of 4c4e (as many as "2+ pairs" switches) by each pair of criteria, best cells first, which is a **computer-only** way to use them. Each row is a way to pick them; the column is the share of 4c4e's sub-7 cases you miss:

| Criteria (4c4e) | Sub-7s missed (share of 4c4e's sub-7s) |
|---|---|
| pairs + corner case | 34.5% |
| pairs + ARM | 35.5% |
| ARM + corner case | 49.0% |
| all three | 32.0% |
| 2+ pairs alone | 37.2% |

**Bars against separate pairs.** In 4c4e, two pairs as a bar on one edge against two pairs on the two edges. One row per ARM: the two sub-7 rates, then how many states each rests on:

| ARM | Sub-7 rate, bar on one edge | Sub-7 rate, pairs on the two edges | States, bar on one edge | States, pairs on the two edges |
|---|---|---|---|---|
| 00 | 37.5% | 51.1% | 288 | 360 |
| 10 | 18.1% | 46.3% | 576 | 864 |
| 21 | 44.2% | 74.3% | 960 | 2,208 |
| 32 | 20.8% | 47.2% | 576 | 864 |
| 42 | 22.2% | 50.0% | 288 | 360 |
| 11 | 33.3% | 45.1% | 864 | 1,152 |
| 31 | 33.3% | 49.3% | 864 | 1,152 |
| 20 | 16.0% | 47.2% | 648 | 720 |
| 22 | 12.3% | 40.0% | 648 | 720 |

Yura Riabov had it from experience: "From my experience with pairs 1 bar is worse than 2 pairs for most arms" ([22 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1397110208685146265)), "Also a bar+fake pair sucks" ([22 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1397113410516291684)). It holds in every ARM, by a wide margin. With a bar, the second pair is on an edge that is already paired, so the other bad edge has nothing. That's why the card counts paired edges.

**Unpaired corners or pairs?** Zagros asked whether "number of corners NOT in a pair" beats pairs across all DRMs ([5 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1479199955444043899)). Pooled over the named DRMs without the DRM, unpaired corners carry more information (0.0375 against 0.0214 bits, **computer only**). Once you know the DRM, which you always do, both add the same (0.0594 bits), since within a DRM one is the other subtracted from a constant. So it's just convenience: count whichever is faster for you.

**Side pairs, outside 4c2e.** Jay thought side pairs aren't useful outside 4c2e ("I don't think they're any useful for other DRM's at the moment though", [14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383640829280780392)). For 4c4e, pairs + side pairs/2 settles 51.9%, more than pairs alone (33.3%) but less than the card. For 2c2e it settles 81.7%, but the card's paired edge + JZP is simpler and settles more.

---

## 11. Computer-only rules: the answer key

Everything in this section is **computer only**. It says how far any rule could go, not what to do at the table. The search here is over pair-trace features; the half-turn and side-turn counts of sections 4 and 5 are not in it.

**The search.** For each DRM, every cross-table of 1, 2 or 3 of 38 features: the ARMs, pairs and their variants (fake, side, paired edges, bars, split pairs, AR bars, unpaired corners and edges), the corner case and suffix, twist split, layer layouts, JZP and anti-AR, and seven features that need a search in your head (moves to AR, moves to orient the corners, and the setup distance to each trigger family). I scored each rule by how much of the DRM it settles and kept it only if it holds on the RZP-weighted cases and the real attempts. The Pareto front, rule size against how much it settles. Each row is a rule: the features crossed, how many cells its table has, and the share of the DRM it settles:

| DRM | Features crossed | Cells in the table | Settled (share of the DRM in cells under 10% or over 50%) | Usable |
|---|---|---|---|---|
| 4c4e | setup turns to an R/L-quarter-turn finish | 10 | >99.9% | its half turns by hand (section 4); with the U/D turns **computer only** |
| 4c4e | fake pairs + setup turns to an R/L-quarter-turn finish | 30 | >99.9% | **computer only** |
| 4c2e | pairs + side pairs/2 | 7 | 75.4% | by hand |
| 4c2e | pairs + side pairs/2 + setup turns to an R h R finish | 35 | 87.0% | **computer only** |
| 4c2e | bars + pairs + side pairs/2 + setup turns to an R h R finish | 40 | 90.2% | **computer only** |
| 3c2e | corner ARM | 4 | >99.9% | by hand |
| 7c8e | setup turns to an R U L finish | 8 | >99.9% | **computer only** |
| 8c8e | moves to orient the corners | 5 | 58.1% | **computer only** |
| 8c8e | bad edges in one layer + moves to orient the corners | 10 | 59.2% | **computer only** |
| 8c8e | edge ARM + pairs + orbit case of the out-of-AR corners | 65 | 74.6% | **computer only** |
| 4c6e | setup turns to an R h L finish | 9 | >99.9% | **computer only** |
| 3c4e | bad corners split L/R | 2 | >99.9% | by hand |
| 3c6e | corner ARM | 4 | >99.9% | by hand |
| 5c4e | edge ARM | 3 | >99.9% | by hand |
| 5c6e | corner ARM | 6 | >99.9% | by hand |
| 6c6e | corner ARM | 7 | >99.9% | by hand |
| 2c2e | pairs + side pairs/2 | 6 | 81.7% | by hand |
| 2c2e | paired edges + JZP | 4 | 92.0% | by hand |

- **The full setup distance is the perfect separator, and half of it is readable.** *How many U, D and half turns to an R/L-quarter-turn finish* settles all of 4c4e, and the same holds for 7c8e (R U L). Reading all of it means finding the DR, which is the server's habit of just NISS-tracing a promising case all the way. Zagros: "skip all the stats and just niss trace and know 100% if you should switch." ([16 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417535391698784306), on 4c2e). But the distance is a sum: the half turns, which section 4 reads off the rings, and the U/D turns between them, which you only get by doing it. The half turns alone give the bands of section 4.3.
- **8c8e** needs 65 cells (edge ARM × pairs × the orbit case of the out-of-AR corners) to settle 74.6%: a table to look things up in, not a rule.
- **The low DRMs** settle "completely" only because every cell is under 10%: that is the discard verdict. What the search asked for them is whether any traceable rule of up to three features finds a cell above 50% holding a real share of their sub-7s. One row per DRM: the best rule's share of that DRM's sub-7 cases in such cells:

| DRM | Sub-7s in cells above 50%, best rule (share of the DRM's sub-7s) |
|---|---|
| 4c6e | 20.1% |
| 3c4e | 23.9% |
| 3c6e | 22.4% |
| 5c4e | 5.8% |
| 5c6e | 8.8% |
| 6c6e | 7.0% |

  Short setups (section 5), which the search did not have, do better where you can see them. 4c6e at most one half turn before `R U2 L` is 59.1% and holds 41.8% of 4c6e's sub-7s. Short 5c6e is 52.9% and holds 26.4%. For 3c4e, 5c4e and 6c6e the short group stays under 50% (29.8%, 46.6%, 32.4%) until you add the pair count (section 5.5).

**Information.** JTuu asked when ARM is most informative ([27 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1222755932518486027)). In information terms (the share of the uncertainty about sub-7 within the DRM that the feature removes), ARM removes 0.098, pairs 0.191 and both 0.262 for 4c4e, and 0.159, 0.082 and 0.325 for 8c8e: ARM tells more than pairs only in 8c8e, 3c6e and 6c6e. rodneykinney's score ([29 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1388919153900912730), [29 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1388981949829218365)) is the product $p(\text{sub-7} \mid \text{subset}) \times N(\text{sub-7 in subset})$, which ranks rules well but is not mutual information in the usual sense. The values for every DRM are in the study's repository, with the code.

---

## 12. The sheets, reproduced

I recomputed every published number I could match to a definition: exact tables to their printed rounding, sampled ones within three standard errors of the exact value. One row per source:

| Source | Numbers compared | Reproduced |
|---|---|---|
| Cale, *DR setup stats* | 1 | 1 |
| rodneykinney, *DRM Subsets* | 1 | 1 |
| rodneykinney, *DRM Subsets* ranking and trees | 24 | 24 |
| FakeMMAP; my EO-to-DR study | 4 | 4 |
| rodneykinney (which ARM each corner case can have) | 4 | 4 |
| Louis, twist splits | 4 | 4 |
| Louis, corner case by ARM | 9 | 9 |
| rodneykinney, *DRM corner variant+pair stats* | 72 | 72 |
| Radek B, tables from Louis's data (images) | 5 | 5 |
| Levi Gibson, *Sub-7 simulations* (sampled) | 2 | 2 |
| Evan, *4c4e ARM subtype stats* (sampled) | 15 | 15 |
| Evan, *arm/pairs* (sampled) | 3 | 1 |
| my EO-to-DR study | 8 | 8 |
| Cale, *DR setup stats (switching last move of EO)* | 2 | 2 |

152 of 154 reproduce. The two that don't are both in **Evan's *arm/pairs***, far outside the sample's error. Each row is a sub-7 rate as a fraction, on the sheet and exact:

| Evan's *arm/pairs*, 4c4e | Sub-7 rate on the sheet | Sub-7 rate, exact | Distance in standard errors |
|---|---|---|---|
| 2 pairs | 0.394 | 0.411 | $z = 17.05$ |
| 3 pairs | 0.758 | 0.790 | $z = 15.44$ |

Its ARM 21 cell does match. None of the definitions I tried explains the gap (optimal with any turns, paired corners, edges with a pair).

**Fanti's figures are any-turn.** Fanti's rule figures in *armpairs_1.txt* ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069)) match the optimum that allows F and B quarter turns exactly, not the EO-kept one (U, D, R, L, F2, B2) that the other tables use. EO-kept they move by about a point at most (section 13). I use EO-kept throughout: with an EO, you keep the EO.

**What is in a match.** rodneykinney's *DRM corner variant+pair stats* (72 cells) and the *DRM Subsets* ranking and trees (24) match exactly. Louis's corner-case and twist-split figures, Radek B's tables from Louis's data and Cale's two sheets match. Evan's subtype stats and Levi Gibson's simulations are within their sample error. rodneykinney's "findable sub-7" numbers (the *DRM Subsets* trees) are not reproduced: they classify the one optimal solution the generator kept per case, so they depend on search order. Louis's README says so: "optimal sequence is only the first one that is found by the search algorithm, others are discarded".

---

## 13. The claims, checked

Statements the numbers can settle, by theme. Questions and guesses are in section 2 unless a number was given. Each verdict is one of **True**, **Corrected**, **Depends** (true under one reading, not another), **Open** (not settled here) or **Withdrawn** (taken back at the time). Exact over all cases unless marked. The one correction has its example in the errata.

**4c4e.** One claim per row, with its verdict.

| Claim | Who | Verdict |
|---|---|---|
| "02, 12, 30 and 40 for 4e4c are never worth switching" | Yura Riabov [12 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1272565146916749436) | **True**: 02 0.003, 12 0.032, 30 0.035, 40 0.003. |
| "02, 12, 03, 04 for 4e4c are like sub5 percent of sub7 dr" | Yura Riabov [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285700522514448444) | **True**, reading 03 and 04 as 30 and 40 (4c4e has no edge ARM above 2): 02 0.31%, 12 3.2%. |
| "00, 10, 21, 32 and 42 are more than 20% sub7 DR for 4c4e iirc" | tseitsei89 [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285700969795158128) | **True**: 00 0.475, 10 0.285, 21 0.343, 32 0.292, 42 0.367. |
| "AR-3c-0/1/2e is the same as AR-1c-2/1/0e"; "not strictly symmetrical (AR-1c is not exactly the same as AR-3c : see 0.28 vs 0.29 for the 4c case." | rodneykinney [8 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1381320727273148668); Louis [9 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1381623814307319828) | **True** to within a point, and Louis is right that it isn't exact: ARM 30 is 0.0347 against 0.0324 for 12, 31 is 0.1771 against 0.1762 for 11, 32 is 0.2917 against 0.2847 for 10. |
| "I believe I now know which DR-4C4E sets actually have a chance of being 5 or less moves after you NISS", "10 total sets that can be sub 6 out of the 15 total sets (7/15 can be sub 5!)" | Jay [9 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215904716530384908) | **Corrected** (errata): 11 of the 15 ARM sets have a case of at most 5 moves; AR-4c1e (shortest 5, 24 of its 3,456 cases) is missing from Jay's count, which was by hand. The 7 for sub-5 is right. |
| "For sure there aren't any 4-movers with 0 or 1 pairs, because any 4 moves from a solved cube always leaves at least 2 bad pairs." ("pairs" = bad pairs) | rodneykinney [25 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1068026817602125844), [25 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1068024296519254046) | **Depends** on what a pair is. Counting top and side pairs it is true (Radek B, [26 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1068097736454451201): "0 or 1 top and side pairs => at best 5 moves", also **True**). Counting top pairs alone it is not: `F2 B2 R` is a 3-move 4c4e with no top pair, and Radek B listed its mirror `F2 B2 L` ([26 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1068097453871611934)). |
| "you can also recognize that all the corners are on U and know that's the only 02 case that can be sub-7 :)", "whopping 5.60%"; "corners on U, edges on D", "then it goes up to 33%!!!" | Evan [16 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1395151816684998748), [16 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1395151868539310130); caycala [16 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1395152332349640766), [16 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1395152552655323348) | **True**: 5.6%, the rest 0%; with the bad edges on the other layer 33.3%. |
| "4d+1 is extremely good for AR-21 (~90% sub-7) but 0% for other AR" | Evan [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418247728328212585) | **True**: 4d 1p 20 0.000, 4d 1p 21 0.889, 4d 1p 22 0.000. |
| "b corners - 29%", "d corners - 89%", "a corners - ~34% if corners are stacked, < 5% otherwise" (1 pair + AR-21) | Evan [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418283868007436308) | **True**: b 28.8%, d 88.9%. *Stacked* is each bad corner directly above or below another: the layouts allF, allR and colU of the sheet Evan linked next ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418283874588295229), [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk), where "all-F means all bad corners are on F/B" and "col-F means the bad corners make columns orthogonal to F/B"). Stacked a corners are 34.8% over 1,056 cases. The other three layouts (allU, colF, colR) are 0%, 2.4% and 4.8%, 2.5% over 960 cases. An allU case: `L' D' U2 L2 F2 U2 L'`, optimal DR `L U2 F2 L2 U2 D L` (7 moves, and no allU case is shorter). |
| "interestingly 4a corners are basically the same for all ar-2X" | Evan [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418248145262874785) | **True**: 4a 2c0e 0.181, 4a 2c1e 0.200, 4a 2c2e 0.183. |
| "AR-0 can mean 4a-0, which is good, or 4b-0, which is bad (without pairs)" (and 4b-2 good, 4a-2 bad) | rodneykinney [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383073553376612404) | **True**: 4a-0 0.244, 4a-2 0.192, 4b-0 0.088, 4b-2 0.244. |
| "To catch this case, you can switch 4a-0 and 4d-2, but only if there also are no fake pairs" (the 0-pair `F2 B2 R` case Nico asked about, [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383069167409958932)) | rodneykinney [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383075044682633366) | **Depends**: the `F2 B2 R` case itself is 4a-0 with no fake pairs and is caught, but one U/D turn earlier, `D F2 B2 R` (0 pairs, no fake pairs, 4 moves), is 4b-2 and is discarded. |
| "It's simply:", "3-4 pairs: Always switch", "2 pairs: Switch unless 4b-0", "1 pair: Switch if 4d-2", "0 pairs: Don't switch" | rodneykinney [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383069263530692730) | **True** as a rule that beats "2+ pairs": 25.2% switched at 49.3%, against 46.4% (section 9). |
| "If you're looking to reach DR in ≤ 6 moves, then look for an inverse state with at least three pairs. Otherwise, you can save yourself the time of performing the NISS." | rodneykinney, *Domino Setup Theory* | **Depends** on your cut: 3+ pairs is 79.9% but holds only 14.8% of the sub-7 cases, and 2 pairs on two edges is 53.9%. rodneykinney moved to 2+ pairs later ([20 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1154070313554956380)). |
| "the only 3+ pairs case i wouldn’t switch for is 3 pairs with all white or all yellow corners" | caycala [11 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404468988070727700) | **True** in effect: the rule is 81.6% against 79.9% for 3+ pairs. |
| "It seems like you should pretty much always switch a 4 move DR-4c4e." | Zagros [7 Jul 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1524175174507692245) | **True** with DR in 7 as the target: 59.4%; Daichi's refinement ([7 Jul 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1524192731432353853)) is 63.9% on 90.6%. |
| "This is not accounting side pairs but you can quickly confirm that 0 or 1 top and side pairs => at best 5 moves" | Radek B [26 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1068097736454451201) | **True**: shortest 5 over 24,890 states. |

**4c2e and 3c2e.** One claim per row, with its verdict.

| Claim | Who | Verdict |
|---|---|---|
| "Because it’s a three move trigger, no number of pairs will save 3qt corners" | rodneykinney [15 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383677247545933874) | **Depends** on the fold. In 4c2e the corners 3 U/D quarter turns (half turns free) from the corners of `R U2 R` are 4a-0; the trigger's own are 4b-0, and 4b-2 is "2qt" in rodneykinney's next message ([15 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383856871869251735)). No 4a-0 case is under 6 moves. With 0, 1 and 2 pairs it is 1.7%, 8.3% and 25.0% as rodneykinney's sheet has the row, with corner ARM 4 folded into 0. Split, corner ARM 0 is 3.3%, 16.7% and 50.0% (48 cases with 2 pairs, one of them `R' F2 R' B2 F2 R'` with the DR `R F2 B2 R F2 R`), and corner ARM 4 is 0% at every pair count. |
| "4a-2 is good. 4b-2 is the bad case, because corners are 2qt, so 6 moves is the absolute minimum to DR" | rodneykinney [15 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383856871869251735) | **True**: shortest per case: 4a-0 6, 4a-2 5, 4b-0 3, 4b-2 6, 4c-1 4, 4d-2 5; 4a-2 sub-7 0.240, 4b-2 0.117. |
| "Yeah I often check for 4a corners before switching 4c2e since that seems to almost always suck" | tseitsei89 [20 Jan 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1463077953293521010) | **Depends**: 4c2e with 4a corners is 18.1%, about the 4c2e rate (18.7%); it is not worse in general. |
| "for 4c2e with 0p, I think niss tracing corner positions is worth it because JZP with b corners is way better than a corners" | Daichi [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436036602723045579) | **True**: b 66.7%, a 16.7%. |
| "41 is 0% chance of sub 7 with 0 pairs?" | caycala [16 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1395148977644634222) | **True**: 0.0000 over 144 states. |
| "3c2e is pretty much always worth NISSing, even as a 6 move rzp." | tseitsei89 [20 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1275330107661352970) | **Depends** on the cut: after a 6-move RZP the target is DR in 5, and 3c2e is 19.2%. That is still the best of any DRM. |
| "At the very least you will never miss a 5 mover by doing this" (switch 3c2e on a pair, a fake pair or a split pair) | wen [12 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1471458126539526323) | **True**: the 640 cases with none of the three are all 6 or more. |

**7c8e, 8c8e and the rest.** One claim per row, with its verdict.

| Claim | Who | Verdict |
|---|---|---|
| "DR-7C8E AR-2C1E is over 70% chance of sub7 dr" | Yura Riabov [12 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1283899100416442460) | **True**: 71.9%. tseitsei89's 7c8e 2c1e without a sub-7 ([2 Jun 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1379010221938053231)) is one of 216 such cases out of 768. |
| "And for 7c8e in particular, half the cases are 0% chance of sub7 dr" | Yura Riabov [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285701896123842690) | **True** by ARM set: 15 of 30 ARM sets have no sub-7 state, holding 12.6% of 7c8e cases. |
| "all that i've memorized is that 1C0E is always 5-6 and 2C1E is the only one that can give sub 4" | Jay [9 May 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1238050909171482666) | **True**: 1C0E 5–6; ARMs with a state of 3 or fewer: 21. |
| "After revisiting the ARM stats I noticed that edge ARM =4 always has 0% chance for sub7." "And yes 3 seems to be much better than 2, but also only good if corner ARM >= 4" | tseitsei89 [24 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409256324214034502) | **True**: edge ARM 4 0%; edge ARM 3 18.6% against edge ARM 2 12.2%. |
| "7c8e is actually the exception because with 8 bad edges, every bad in-ARM corner forms a side pair anyway." | rodneykinney [29 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1411129084410462270) | **True**: side pairs = bad corners not out of AR on 23,520 of 23,520 7c8e states. |
| "for 7c8e with 5p, 20/54 has a 0% chance of sub7"; "it's still 54% in general" | Daichi [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436036602723045579), Fanti [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436039819963662497) | **True**: 20 0.000 (48 states), 54 0.000 (48); 5 pairs 0.543. |
| "also 78 4p has a weird silver lining with 11/12/33/41/62 where they're all just slightly worse", "20-23% sub7, though keep in mind only 21 can have sub-6 on 4p" | Fanti [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436041311110172783), [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436041646180667422) | **True**: 11 0.222, 12 0.222, 33 0.231, 41 0.215, 62 0.200, 21 0.690; ARMs with a 4-pair state of at most 5: 21. |
| "AR-1C2E might be worth switching since it's exactly a 1-in-6 chance of sub 7 to DR" (7c8e) | Jay [23 Mar 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1353245667580973110) | **True**: 7c8e ARM 12 is 16.7%. |
| "4b: 12%", "4a: 43%" (8c8e AR-4c2e by the corner case of the out-of-AR corners) | trangium [7 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1491272130158002217) | **True**: 4a 0.431 (any-turn 0.431), 4b 0.120 (any-turn 0.120). |
| "8e8c - R L but only if four corners are clockwise and four are ccw (7/1 is possible)" | Zagros [20 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1342188064067424340) | **True**: every one of the 4,900 8c8e cases with a 4-4 twist split has a DR with two quarter turns (U, D and half turns free), and none of the 1,120 with a 7-1 split has: they need three. Sub-7 is 15.2% against 11.4% (section 5.2). |
| "You shouldn't switch 6e4c unless it's jzp" | Yura Riabov [24 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1265765209050714142) | **True**: JZP 61.1%, 4 pairs 47.9%, everything else together 3.7%. |
| "even with full moveset sub-7 is 1 in 22" (4c6e) | Cale [10 Apr 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1094878042096152576) | **True**: any turns: 1 in 21.7; EO kept: 1 in 21.7. |
| "it’s 1/7 for 7 moves instead of 1/3 for 4e4c, 8c8e, 8e7c, 2e4c etc" (3c6e) | Noah Swor [3 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1269374128155267147) | **Depends**: the 1/3 fits DR in 6 on the better of normal and inverse (4c4e 1 in 2.88, 7c8e 1 in 3.32), and then 3c6e is 1 in 10.57, worse than 1/7. No reading gives both numbers. |
| "It could be worth it mathematically if it's AR-2C1E (only subset where +4 to DR is possible)" (3c6e) | Jay [3 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1269432136616771647) | **True**: shortest per ARM: 00 6, 01 5, 02 6, 03 9, 10 7, 11 6, 12 5, 13 7, 20 7, 21 4, 22 6, 23 7, 30 8, 31 6, 32 5, 33 7. |
| "21 which is the 4move trigger one is only 15%" (5c4e); "They all have around a 15% chance of getting sub-7" | Yura Riabov [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285693332416233504); Levi Gibson [23 Mar 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1353530406397280328) | **True**: 5c4e 21 0.152, 5c6e 21 0.149, 6c6e 21 0.146. |
| "For example, 5c4e with 2 pairs has 40% chance of sub-8." | rodneykinney [26 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409789617573597184) | **Open**: any optimal DR gives 57.0%; rodneykinney's numbers may count only findable solutions. |
| "Yes, that’s the conclusion" (the DRMs outside the top ten are not worth looking at) | rodneykinney [30 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1411470906357977209), to zakimoshi [30 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1411464911313174769) | **True** for the time it takes: some are better per case but very rare (0c2e and 2c0e have 32 and 40 sub-7 cases in all). |

**Switching, NISS and the tables.** One claim per row, with its verdict.

| Claim | Who | Verdict |
|---|---|---|
| "if the EO isn't already 4c4e, it means that the 4c4e case you get from RZP is 1 move away from something that is not 4c4e", "the 4c4e cases that can go out of 4c4e in more ways will thus be more likely to show up" | torchlight [8 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215720321995382867) | **True** on the same side (18.3% against 19.2%), and it vanishes after a switch (section 8). |
| "the number of axially reduced pieces is always equal between one axis on normal and the other on inverse"; "Remember that ARM switches axis when you NISS" | Cale [3 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1213932643188473896); wen [17 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1285751016545058853) | **True** on every sampled cube (section 7). |
| "It remains the same on the same axis." | Louis [28 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1222965074398806066) | **Withdrawn** ("Yes you're right it makes total sense", [28 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1222967992015654952)): it holds on about one cube in ten. |
| "It's easy to predict how many corners will be out of AR on inverse: count the number of R/L stickers on the U/D face." and the corner-case flow chart | rodneykinney, *DR - 4c4e Theory* | **True** on every sampled cube; checked by sampling, not proved (section 7). |
| "if the 2 stickers on the corner that are touching the E slice match with that E slice edge, then that's a pair on inverse" | wen, *Hitchhiker's Guide to DR* | **True** on every sampled cube (section 7). |
| "But if you assume the axes are independent (which is probably a reasonable approximation) then if one has 20% chance and the other has 10%, then the combined chance is 28%" | caycala [16 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417554347738267838) | **True** to within half a point for the named DRMs (section 8). |
| "like how DR-4e4c in 6 moves is 1 in 5.2 normally, but 1 in 3.6 if you can switch the last move" | Tom Nelson [13 Jul 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1128948555684519946) | **True**: 1 in 5.20; 1 in 3.56. After a switch the last EO turn is worth much less (section 8). |
| "After EO, there are approximately 1 million distinct DR-equivalent cube states, of which approximately 64,000 have sub-7 solutions." | rodneykinney, *DRM Subsets* | **True**: 64,103 of 1,082,565. |
| Fanti's rule figures for 4c4e, 4c2e, 7c8e, 3c2e and 3c4e ("= 35.2% switches", "42.6% sub-7 switch success (15.0% total)", "4.3% of cases will be discarded with sub-7" for 4c4e, and the rest) | Fanti, *armpairs_1.txt* [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069) | **True**, exactly, with the any-turn optimum (F/B quarter turns allowed); EO-kept, 4c2e moves from 38.8% to 37.7% and the others by less (section 12). |

---

## 14. What this does not cover

- **Time.** I didn't time any check. The cards use the same tracing solvers already do. The half-turn count needs more: where each unpaired corner sits and which way it points, the holes, and for 2 pairs a one-swap search (section 4.4). Whether that is worth it against just tracing the DR depends on the solver.
- **No recipe outside 4c4e.** For the other DRMs the side-turn bands are exact, but the reading is a search one half turn deep towards a trigger picture (section 5.6). I have no pair-count shortcut for it.
- **How the layers line up.** Inside a half-turn count the U/D turns decide, and nothing I tried predicts them short of finding the setup (section 4.5).
- **Findability.** Sub-7 means some DR of 6 or less exists, not that you find it. rodneykinney's "findable" versions and the server's worry about rare shapes ("the "% of sub-7" stat has a couple of flaws", Evan, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409718740546879489)) are not modelled.
- **Beyond sub-7.** The target is a DR in 6 (or 5, or 7). The finish after the DR, and the value of variations such as AR and anti-AR cases, are not counted. A 7-move DR into a good HTR case can beat a 6-move one.
- **The real attempts** count every EO of up to 6 moves equally, not the ones a solver finds first, and the many attempts of one scramble are not independent (errors are from batches of scrambles). Rule rates on them are a check, not the source.
- **NISS EOs.** For an EO found partly on each side, the last turn on each side can change, and pair counts read before the EO is finished can be off. The cards assume the case after EO + RZP is what you trace.
- **Two DR axes at once.** Section 8 gives the gain from the second axis. I didn't build a combined rule over both axes of one EO.
- **The tracings** in section 7, the ring reading included, are checked on 20,000 random cubes each, not proved.

---

## Appendix A: full tables

**Every 4c4e ring picture with 2 row swaps or fewer** (section 4.4), up to exchanging the layers and mirror image. One row per picture, in the ring notation of section 4.1 (`>` and `<` bad corners pointing clockwise and counter-clockwise, `o` a good corner, `E` a bad edge place, `-` a good one). *States* counts all 4c4e cases with that picture, whatever the holes:

| One layer | The other layer | Row swaps to a bar in each layer | Pairs | States (4c4e) | Sub-7 rate |
|---|---|---|---|---|---|
| `>E<-o-o-` | `>E<-o-o-` | 0 | 4 | 96 | 97.9% |
| `>E<->E<-` | `o-o-o-o-` | 1 | 4 | 24 | 100% |
| `>E<E<-o-` | `>-o-o-o-` | 1 | 3 | 384 | 95.8% |
| `oE<-o-o-` | `>E<-o->-` | 1 | 3 | 384 | 95.8% |
| `oE<-o-<-` | `>Eo->-o-` | 1 | 2 | 192 | 100% |
| `>E<-o-o-` | `oE<-o->-` | 2 | 3 | 384 | 83.3% |
| `>E<-oE<-` | `>-o-o-o-` | 2 | 3 | 384 | 81.3% |
| `oE<-o-o-` | `>E<->-o-` | 2 | 3 | 384 | 83.3% |
| `<E>E<-o-` | `>-o-o-o-` | 2 | 2 | 384 | 70.8% |
| `>E<-o-o-` | `oEo->-<-` | 2 | 2 | 192 | 54.2% |
| `>E>-o-o-` | `<E<-o-o-` | 2 | 2 | 192 | 79.2% |
| `>E>-o-o-` | `oE<-o-<-` | 2 | 2 | 384 | 66.7% |
| `>Eo-o-<-` | `oE<->-o-` | 2 | 2 | 192 | 85.4% |
| `>Eo-o->-` | `oE<-<-o-` | 2 | 2 | 192 | 77.1% |
| `>Eo-o->-` | `oE<-o-<-` | 2 | 2 | 384 | 62.5% |
| `>Eo-oE<-` | `<->-o-o-` | 2 | 2 | 192 | 100% |
| `>EoE<-<-` | `>-o-o-o-` | 2 | 2 | 384 | 72.9% |
| `>EoE<-o-` | `<-o->-o-` | 2 | 2 | 192 | 83.3% |
| `oE<-o->-` | `>Eo-<-o-` | 2 | 2 | 192 | 83.3% |
| `oE<-o-o-` | `>E>-<-o-` | 2 | 2 | 384 | 66.7% |
| `oE<-o-o-` | `>E>-o-<-` | 2 | 2 | 384 | 77.1% |
| `oE<-o-o-` | `oE<->->-` | 2 | 2 | 384 | 72.9% |
| `oE<E<->-` | `>-o-o-o-` | 2 | 2 | 384 | 75.0% |
| `oE<E<-o-` | `>->-o-o-` | 2 | 2 | 384 | 79.2% |
| `oE<E<-o-` | `>-o->-o-` | 2 | 2 | 192 | 75.0% |
| `oE>E<-<-` | `>-o-o-o-` | 2 | 2 | 384 | 47.9% |
| `oE>E<-o-` | `<-o->-o-` | 2 | 2 | 384 | 62.5% |
| `oE>E<-o-` | `<-o-o->-` | 2 | 2 | 384 | 52.1% |
| `oEo-o-<-` | `>E<-o->-` | 2 | 2 | 384 | 45.8% |
| `oE<-o-<-` | `oE>->-o-` | 2 | 1 | 384 | 62.5% |
| `oE<-o->-` | `<Eo->-o-` | 2 | 1 | 384 | 79.2% |
| `oE<Eo->-` | `<-o->-o-` | 2 | 1 | 384 | 79.2% |
| `oEo->-<-` | `oEo->-<-` | 2 | 0 | 96 | 81.3% |

**4c4e: U/D turns by half-turn count** (section 4.5). Each row is a half-turn count with the number of U/D turns its shortest one-quarter-turn setup needs, **computer only** as a table:

| Half turns to two bars | U/D turns of the shortest such setup | Length of that DR (moves) | States | Share of that half-turn count | Sub-7 rate |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 6.3% | 100% |
| 0 | 1 | 2 | 12 | 37.5% | 100% |
| 0 | 2 | 3 | 18 | 56.3% | 100% |
| 1 | 0 | 2 | 4 | 0.58% | 100% |
| 1 | 1 | 3 | 60 | 8.7% | 100% |
| 1 | 2 | 4 | 260 | 37.8% | 100% |
| 1 | 3 | 5 | 308 | 44.8% | 100% |
| 1 | 4 | 6 | 56 | 8.1% | 100% |
| 2 | 0 | 3 | 6 | 0.065% | 100% |
| 2 | 1 | 4 | 200 | 2.2% | 100% |
| 2 | 2 | 5 | 1,606 | 17.3% | 100% |
| 2 | 3 | 6 | 4,192 | 45.1% | 100% |
| 2 | 4 | 7 | 2,712 | 29.2% | 21.1% |
| 2 | 5 | 8 | 548 | 5.9% | 21.2% |
| 2 | 6 | 9 | 24 | 0.26% | 33.3% |
| 3 | 1 | 5 | 256 | 0.71% | 100% |
| 3 | 2 | 6 | 3,708 | 10.3% | 100% |
| 3 | 3 | 7 | 15,600 | 43.3% | 6.8% |
| 3 | 4 | 8 | 14,696 | 40.8% | 4.5% |
| 3 | 5 | 9 | 1,740 | 4.8% | 3.2% |
| 4 | 1 | 6 | 124 | 0.52% | 100% |
| 4 | 2 | 7 | 2,532 | 10.6% | 2.5% |
| 4 | 3 | 8 | 13,852 | 58.1% | 1.2% |
| 4 | 4 | 9 | 7,020 | 29.4% | 0.74% |
| 4 | 5 | 10 | 328 | 1.4% | 0% |
| 5 | 2 | 8 | 52 | 7.5% | 0% |
| 5 | 3 | 9 | 460 | 66.1% | 0% |
| 5 | 4 | 10 | 184 | 26.4% | 0% |

**4c4e by ARM inside 2 and 3 half turns** (section 4.5), one row per ARM:

| Half turns to two bars | ARM | States | Sub-7 rate |
|---|---|---|---|
| 2 | 00 | 388 | 81.4% |
| 2 | 01 | 192 | 58.3% |
| 2 | 10 | 800 | 67.0% |
| 2 | 11 | 1,280 | 64.4% |
| 2 | 20 | 384 | 70.8% |
| 2 | 21 | 3,200 | 77.3% |
| 2 | 22 | 384 | 67.7% |
| 2 | 31 | 1,280 | 71.9% |
| 2 | 32 | 800 | 69.0% |
| 2 | 41 | 192 | 58.3% |
| 2 | 42 | 388 | 83.5% |
| 3 | 00 | 828 | 29.0% |
| 3 | 01 | 1,872 | 9.0% |
| 3 | 02 | 156 | 2.6% |
| 3 | 10 | 1,920 | 18.8% |
| 3 | 11 | 4,992 | 13.8% |
| 3 | 12 | 1,344 | 8.3% |
| 3 | 20 | 2,952 | 12.7% |
| 3 | 21 | 7,872 | 26.8% |
| 3 | 22 | 2,952 | 9.8% |
| 3 | 30 | 1,344 | 8.3% |
| 3 | 31 | 4,992 | 12.7% |
| 3 | 32 | 1,920 | 18.8% |
| 3 | 40 | 156 | 2.6% |
| 3 | 41 | 1,872 | 10.7% |
| 3 | 42 | 828 | 11.1% |

**The side-turn setups on the real attempts and for the other RZP lengths** (section 5.2), the rows of that section's table:

| DRM | Shortest setup, U/D turns not counted | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) | DR in 7 or fewer, exact (for a 4-move RZP) | DR in 5 or fewer, exact (for a 6-move RZP) |
|---|---|---|---|---|---|
| 4c4e | 1 qt | 100% | 284 | 100% | 100% |
|  | 1 qt + 1 half turn | 100% | 5,726 | 100% | 93.0% |
|  | 1 qt + 2 half turns | 72.1% | 73,332 | 99.1% | 21.4% |
|  | 2 qt + 1 half turn | 34.2% | 11,226 | 90.3% | 3.9% |
|  | 3 qt | 17.8% | 22,442 | 71.0% | 1.7% |
|  | 1 qt + 3 half turns | 14.4% | 262,200 | 69.6% | 0.88% |
|  | 2 qt + 2 half turns | 2.4% | 69,416 | 33.0% | 0.047% |
|  | 3 qt + 1 half turn | 0.82% | 97,104 | 20.6% | 0% |
|  | 4 qt | 0% | 8,128 | 13.1% | 0% |
|  | 1 qt + 4 half turns | 0% | 8,490 | 12.9% | 0% |
|  | 2 qt + 3 half turns | 0% | 2,212 | 2.9% | 0% |
|  | 3 qt + 2 half turns | 0% | 262 | 0% | 0% |
| 4c2e | 2 qt | 100% | 1,104 | 100% | 100% |
|  | 2 qt + 1 half turn | 55.8% | 25,812 | 99.2% | 10.4% |
|  | 3 qt | 13.0% | 11,744 | 65.6% | 0% |
|  | 2 qt + 2 half turns | 6.6% | 66,834 | 53.1% | 0.100% |
|  | 3 qt + 1 half turn | 0% | 6,574 | 13.0% | 0% |
|  | 4 qt | 0% | 262 | 25.0% | 0% |
| 3c2e | 2 qt | 100% | 2,368 | 100% | 100% |
|  | 2 qt + 1 half turn | 73.7% | 20,102 | 100% | 18.4% |
|  | 3 qt | 18.1% | 1,180 | 100% | 0% |
|  | 2 qt + 2 half turns | 25.2% | 7,690 | 94.6% | 0.89% |
| 7c8e | 2 qt | 100% | 802 | 100% | 100% |
|  | 2 qt + 1 half turn | 95.5% | 11,176 | 100% | 37.0% |
|  | 3 qt | 21.6% | 17,336 | 85.2% | 0.76% |
|  | 2 qt + 2 half turns | 24.2% | 56,150 | 84.0% | 1.3% |
|  | 3 qt + 1 half turn | 2.2% | 88,568 | 35.1% | 0% |
|  | 4 qt | 0.55% | 13,746 | 22.4% | 0% |
|  | 2 qt + 3 half turns | 0% | 1,092 | 50.0% | 0% |
|  | 3 qt + 2 half turns | 0% | 468 | 0% | 0% |
| 8c8e | 2 qt | 100% | 26 | 100% | 100% |
|  | 2 qt + 1 half turn | 100% | 222 | 100% | 100% |
|  | 3 qt | 36.2% | 8,878 | 86.4% | 4.9% |
|  | 2 qt + 2 half turns | 38.6% | 3,390 | 95.3% | 2.8% |
|  | 3 qt + 1 half turn | 6.1% | 34,404 | 56.8% | 0% |
|  | 4 qt | 0% | 556 | 0% | 0% |
|  | 2 qt + 3 half turns | 0% | 256 | 12.5% | 0% |
|  | 3 qt + 2 half turns | 0% | 844 | 1.7% | 0% |
| 2c2e | 2 qt + 1 half turn | 46.8% | 3,636 | 92.3% | 9.6% |
|  | 3 qt | 31.0% | 2,484 | 94.4% | 2.8% |
|  | 2 qt + 2 half turns | 14.3% | 8,114 | 84.2% | 0% |
|  | 3 qt + 1 half turn | 5.2% | 966 | 56.3% | 0% |
| 4c6e | 2 qt | 100% | 954 | 100% | 100% |
|  | 2 qt + 1 half turn | 48.7% | 34,212 | 96.4% | 8.0% |
|  | 3 qt | 13.2% | 32,982 | 58.4% | 1.1% |
|  | 2 qt + 2 half turns | 3.1% | 320,760 | 34.8% | 0.076% |
|  | 3 qt + 1 half turn | 0.66% | 249,380 | 10.9% | 0.025% |
|  | 4 qt | 0.076% | 57,530 | 5.4% | 0% |
|  | 2 qt + 3 half turns | 0.30% | 22,368 | 7.2% | 0% |
|  | 3 qt + 2 half turns | 0% | 2,436 | 0% | 0% |
| 3c4e | 2 qt + 1 half turn | 29.4% | 14,752 | 83.5% | 3.7% |
|  | 3 qt | 38.7% | 14,180 | 82.9% | 5.6% |
|  | 2 qt + 2 half turns | 4.9% | 109,596 | 42.9% | 0.18% |
|  | 3 qt + 1 half turn | 2.4% | 13,684 | 26.2% | 0% |
|  | 4 qt | 0% | 1,314 | 0% | 0% |
|  | 2 qt + 3 half turns | 0% | 2,408 | 8.3% | 0% |
| 3c6e | 2 qt | 100% | 1,852 | 100% | 43.8% |
|  | 2 qt + 1 half turn | 16.9% | 35,708 | 76.1% | 1.1% |
|  | 3 qt | 7.4% | 4,440 | 51.4% | 0% |
|  | 2 qt + 2 half turns | 0.62% | 131,116 | 16.3% | 0% |
|  | 3 qt + 1 half turn | 0.52% | 13,034 | 5.3% | 0% |
|  | 4 qt | 0% | 9,976 | 1.3% | 0% |
|  | 2 qt + 3 half turns | 0% | 3,168 | 0% | 0% |
| 5c4e | 2 qt + 1 half turn | 47.6% | 26,104 | 88.9% | 13.2% |
|  | 3 qt | 25.8% | 32,138 | 78.5% | 2.6% |
|  | 2 qt + 2 half turns | 7.0% | 396,362 | 48.3% | 0.35% |
|  | 3 qt + 1 half turn | 1.2% | 215,232 | 19.9% | 0.028% |
|  | 4 qt | 0.55% | 17,934 | 9.5% | 0% |
|  | 2 qt + 3 half turns | 0% | 21,958 | 4.6% | 0% |
|  | 3 qt + 2 half turns | 0% | 1,026 | 0% | 0% |
| 5c6e | 2 qt + 1 half turn | 51.7% | 29,668 | 94.2% | 14.2% |
|  | 3 qt | 18.9% | 65,944 | 71.2% | 1.6% |
|  | 2 qt + 2 half turns | 6.0% | 450,704 | 46.1% | 0.26% |
|  | 3 qt + 1 half turn | 0.88% | 349,442 | 16.3% | 0% |
|  | 4 qt | 0% | 31,352 | 6.7% | 0% |
|  | 2 qt + 3 half turns | 0.33% | 34,994 | 7.2% | 0% |
|  | 3 qt + 2 half turns | 0% | 412 | 0% | 0% |
| 6c6e | 2 qt + 1 half turn | 31.4% | 28,428 | 80.9% | 5.3% |
|  | 3 qt | 27.7% | 56,650 | 76.2% | 5.0% |
|  | 2 qt + 2 half turns | 5.5% | 415,322 | 42.4% | 0.23% |
|  | 3 qt + 1 half turn | 2.2% | 455,054 | 21.0% | 0.17% |
|  | 4 qt | 0.47% | 35,784 | 8.0% | 0% |
|  | 2 qt + 3 half turns | 0.28% | 47,616 | 7.1% | 0% |
|  | 3 qt + 2 half turns | 0% | 3,954 | 1.6% | 0% |

**4c4e by ARM and paired edges.** One row per ARM; each cell is the sub-7 rate of the ARM's cases with that many bad edges paired:

| ARM | No bad edge paired: sub-7 rate | One paired: sub-7 rate | Both paired: sub-7 rate | All: sub-7 rate |
|---|---|---|---|---|
| 00 | 66.7% | 29.9% | 61.4% | 47.5% |
| 01 | 0.93% | 10.8% | - | 8.3% |
| 02 | 0.31% | - | - | 0.31% |
| 10 | 8.3% | 15.1% | 56.9% | 28.5% |
| 11 | 1.9% | 15.6% | 53.3% | 17.6% |
| 12 | 1.9% | 4.6% | - | 3.2% |
| 20 | 5.3% | 7.9% | 47.2% | 12.3% |
| 21 | 11.0% | 32.9% | 74.9% | 34.3% |
| 22 | 3.5% | 6.3% | 40.0% | 10.0% |
| 30 | 2.3% | 4.6% | - | 3.5% |
| 31 | 1.5% | 14.5% | 58.3% | 17.7% |
| 32 | 8.3% | 16.3% | 56.9% | 29.2% |
| 40 | 0.31% | - | - | 0.31% |
| 41 | 0% | 12.3% | - | 9.3% |
| 42 | 83.3% | 11.1% | 55.8% | 36.7% |

The number of states behind each cell of that table:

| ARM | No bad edge paired: states | One paired: states | Both paired: states | All: states |
|---|---|---|---|---|
| 00 | 36 | 576 | 684 | 1,296 |
| 01 | 864 | 2,592 | - | 3,456 |
| 02 | 1,296 | - | - | 1,296 |
| 10 | 288 | 2,016 | 1,152 | 3,456 |
| 11 | 2,592 | 5,184 | 1,440 | 9,216 |
| 12 | 1,728 | 1,728 | - | 3,456 |
| 20 | 1,368 | 3,528 | 720 | 5,616 |
| 21 | 4,656 | 7,392 | 2,928 | 14,976 |
| 22 | 1,368 | 3,528 | 720 | 5,616 |
| 30 | 1,728 | 1,728 | - | 3,456 |
| 31 | 2,592 | 5,184 | 1,440 | 9,216 |
| 32 | 288 | 2,016 | 1,152 | 3,456 |
| 40 | 1,296 | - | - | 1,296 |
| 41 | 864 | 2,592 | - | 3,456 |
| 42 | 36 | 576 | 684 | 1,296 |

**4c4e by pairs and paired edges** (bars against separate pairs). One row per count of pairs and of the edges they sit on:

| Pairs, paired edges | States | Share of the DRM | Sub-7 rate, exact | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) | Band |
|---|---|---|---|---|---|---|
| 0 pairs on 0 edges | 21,000 | 29.8% | 4.3% | 4.1% | 168,180 | discard |
| 1 pair on 1 edge | 31,200 | 44.2% | 13.3% | 13.1% | 247,546 | your call |
| 2 pairs on 1 edge (a bar) | 7,440 | 10.5% | 26.6% | 26.3% | 57,628 | your call |
| 2 pairs on 2 edges | 8,400 | 11.9% | 53.9% | 54.0% | 67,030 | switch |
| 3 pairs on 2 edges | 2,400 | 3.4% | 79.0% | 78.6% | 19,310 | switch |
| 4 pairs on 2 edges | 120 | 0.17% | 98.3% | 99.5% | 1,128 | switch |

**4c2e, inside *pairs + side pairs/2 is exactly 1*.** Each row splits that group by one feature value:

| Inside *exactly 1* | States | Share of the DRM | Sub-7 rate, exact | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) | Band |
|---|---|---|---|---|---|---|
| corner ARM 0 | 256 | 1.9% | 25.0% | 24.3% | 2,152 | your call |
| corner ARM 1 | 656 | 4.9% | 8.5% | 8.6% | 5,394 | discard |
| corner ARM 2 | 1,240 | 9.2% | 14.2% | 14.0% | 10,610 | your call |
| corner ARM 3 | 864 | 6.4% | 17.6% | 18.8% | 7,180 | your call |
| corner ARM 4 | 288 | 2.1% | 25.0% | 26.9% | 2,204 | your call |
| edge ARM 0 | 1,392 | 10.4% | 13.2% | 13.3% | 11,390 | your call |
| edge ARM 1 | 1,912 | 14.2% | 17.6% | 18.0% | 16,150 | your call |
| 4a corners | 568 | 4.2% | 18.3% | 17.9% | 4,664 | your call |
| 4b corners | 1,120 | 8.3% | 17.1% | 17.3% | 9,314 | your call |
| 4c corners | 1,520 | 11.3% | 13.7% | 14.4% | 12,574 | your call |
| 4d corners | 96 | 0.71% | 16.7% | 15.8% | 988 | your call |
| JZP | 112 | 0.83% | 42.9% | 37.2% | 1,076 | your call |

**8c8e by pairs**, one row per pair count:

| Pairs | States | Share of the DRM | Sub-7 rate, exact | Sub-7 rate, real attempts (RZP to 5) | Real attempts (RZP to 5) | Band |
|---|---|---|---|---|---|---|
| 0 pairs | 4 | 0.066% | 0% | 0% | 22 | discard |
| 1 pair | 32 | 0.53% | 0% | 0% | 252 | discard |
| 2 pairs | 448 | 7.4% | 11.6% | 12.6% | 3,652 | your call |
| 3 pairs | 1,376 | 22.9% | 4.1% | 4.4% | 11,106 | discard |
| 4 pairs | 2,300 | 38.2% | 11.8% | 11.3% | 18,484 | your call |
| 5 pairs | 1,376 | 22.9% | 25.0% | 23.5% | 11,174 | your call |
| 6 pairs | 448 | 7.4% | 32.1% | 32.1% | 3,610 | your call |
| 7 pairs | 32 | 0.53% | 0% | 0% | 250 | discard |
| 8 pairs | 4 | 0.066% | >99.9% | >99.9% | 26 | switch |

**EO to DR by DRM, with the free options** (every case once; from my EO-to-DR study's definitions, recomputed here). One row per DRM: the mean distance to DR and the share of cases with a DR in at most 5, 6 and 7:

| DRM | States | Mean turns to DR | DR in 5 or fewer | DR in 6 or fewer | DR in 7 or fewer |
|---|---|---|---|---|---|
| 4c4e | 70,560 | 7.1866 | 4.3% | 19.2% | 59.4% |
| 4c2e | 13,440 | 7.1601 | 3.3% | 18.7% | 62.7% |
| 3c2e | 3,584 | 6.1629 | 19.2% | 61.6% | 98.7% |
| 7c8e | 23,520 | 7.2544 | 3.2% | 16.4% | 57.4% |
| 8c8e | 6,020 | 7.2296 | 1.7% | 14.5% | 63.0% |
| 2c2e | 1,792 | 6.8795 | 2.7% | 23.7% | 85.7% |
| 4c6e | 94,080 | 7.8454 | 0.60% | 4.6% | 27.2% |
| 3c4e | 18,816 | 7.4464 | 0.98% | 9.9% | 48.0% |
| 3c6e | 25,088 | 7.8441 | 0.64% | 4.8% | 27.1% |
| 5c4e | 94,080 | 7.5986 | 0.82% | 7.2% | 40.3% |
| 5c6e | 125,440 | 7.6872 | 0.66% | 6.1% | 35.7% |
| 6c6e | 137,984 | 7.7340 | 0.59% | 5.6% | 33.1% |

The share with a DR in at most 6 when one free option is allowed, one row per DRM:

| DRM | DR in 6 or fewer, EO's last turn free | DR in 6 or fewer, last two EO turns free (F B) | DR in 6 or fewer, better DR axis | DR in 6 or fewer, better of normal and inverse |
|---|---|---|---|---|
| 4c4e | 28.1% | 35.9% | 25.4% | 34.8% |
| 4c2e | 27.2% | 33.6% | 26.2% | 33.9% |
| 3c2e | 77.0% | 83.3% | 66.0% | 85.3% |
| 7c8e | 24.4% | 34.4% | 20.5% | 30.1% |
| 8c8e | 23.5% | 32.2% | 19.2% | 26.9% |
| 2c2e | 35.9% | 42.9% | 34.5% | 41.7% |
| 4c6e | 7.7% | 11.5% | 10.3% | 9.0% |
| 3c4e | 15.9% | 23.5% | 18.2% | 18.9% |
| 3c6e | 7.8% | 11.5% | 10.9% | 9.5% |
| 5c4e | 12.2% | 18.3% | 13.6% | 13.9% |
| 5c6e | 10.2% | 15.2% | 11.7% | 11.9% |
| 6c6e | 9.4% | 14.0% | 10.6% | 10.8% |

## Appendix B: how it was computed, and what checks it

**The model.** A case is the twists of the 8 corners and the set of places holding the 4 E-slice edges, for an F/B EO and a U/D DR (1,082,565 cases). A breadth-first search with the 14 turns that keep the EO (U, D, R, L, F2, B2, each way) gives the exact distance to DR of every case: 0: 1, 1: 2, 2: 17, 3: 134, 4: 1,065, 5: 8,190, 6: 54,694, 7: 267,576, 8: 560,568, 9: 187,204, 10: 3,114, mean 7.8031. Features are defined from the faces the stickers are on (a sticker model of the cube), not from index strings. The side turns of a case come from the same turn tables with the U and D turns free: the cases a solution with q quarter turns and h half turns of the side faces reaches are built up one side turn at a time, each step closed under U and D turns. The row swaps of 4c4e are a second, separate search on the 780 ring pairs alone. The RZP weights count every sequence of EO-keeping turns that first reaches its DRM, exactly. The real attempts use 6,000 uniformly random scrambles (random state, not nissy's scrambler, which has a bias). The whole thing runs in about six minutes on four cores, each job capped at 4 GB.

**What checks it.**

- **The distances** equal my EO-to-DR study's table on all 1,082,565 cases, and nissy 2.0.8 (`solve drud-eofb`) agrees on 1,000 of 1,000 random cases, with every nissy solution replayed to DR on the sticker model.
- **The options** (EO's last turn, the second axis, normal or inverse) equal the EO-to-DR study's per-case tables in all 123 cells, to their printed rounding.
- **The features** pass 28 unit tests on hand-made cases from the server's examples, for instance:

  ```
  R                 // 4c4e JZP with 4 pairs
  R U               // 4c4e ARM 21
  U' F2 B2 R2 U2 R  // ARM 02 with no pairs and 6 moves
  ```

  They also agree with rodneykinney's own string code (DRM, ARM, pairs, fake pairs, side pairs, AR pairs) on all 1,082,565 cases, once the corner order is read the way both Louis's and rodneykinney's comments mean it.
- **The ring picture** is checked against the turn tables on every twist state and every edge set: U and D turns rotate one ring and nothing else (16,092 of 16,092 checks), half turns swap the face's two rows and its two E-slice places (10,728 of 10,728), quarter turns follow the rule of section 4.1 (10,728 of 10,728). Half turns to two bars equals the larger of row swaps and hole number on 70,560 of 70,560 4c4e cases, with the two sides computed separately (on the cases, and on the rings).
- **The NISS readings** of section 7 hold on every sampled cube (20,000 uniform and 20,000 4c4e cubes per reading; 20,000 more from 4c2e for the new ones).
- **Switched cases are uniform** within their class: the real attempts' rate against the uniform rate of their own class mix in 36 DRM × length cells, worst 2.63 standard errors (20 batches of 300 scrambles).
- **Every example** in this write-up, the errata and the worked examples is replayed on the sticker model of my DR-xs study (`cube.py`): the scramble and EO + RZP give the stated DRM, the switched case has the stated features, and the DR written out reaches DR with the EO kept, in the stated number of moves.
- **Lean.** A Lean 4 certificate in the study's folder (`lean/EOSwitch`, no Mathlib, no `sorry`) builds its own cube from stickers and runs its own BFS over all 1,082,565 cases with the 14 EO-keeping turns. An independent checker confirms each entry: 0 exactly at DR, never more than one above a neighbour, and one below some neighbour. It defines the features from stickers (pairs, fake pairs, paired edges, bars, side pairs, same slice, the ARM counts, JZP) and redoes 27 of the feature unit tests. It proves the distance histogram (mean 7.8031), the per-DRM counts for 4c4e, 4c2e, 3c2e, 7c8e, 8c8e and 2c2e, and every cell of the card tables: 4c4e by paired edges and by paired edges × same slice, pairs × paired edges, 4c2e by pairs + side pairs/2, 7c8e by pairs, 2c2e by paired edge × JZP, and 3c2e. It also proves that the study's printed tables match those cells. A second part recounts, from the same BFS, the corner case (4a to 4d, suffix) and the other features the rules use, and proves the counts behind section 1, the switch cards and the errata item (listed under *Formally verified* below). Build: `lake build`, about four minutes from clean on two cores, under 1 GB.

  A third part (`Rings.lean`, `RingsThm.lean`) defines the ring picture from the same places and stickers, a bad corner pointing at the edge place it pairs with by the pair definition above. It proves the three turn rules of section 4.1 on every case and every EO-keeping turn (`ring_turns`) and that the picture determines the case (`ring_faithful`). The side turns come from a direct definition, not a search: the cases reached with q quarter and h half turns of the side faces, closed under U and D turns at each step. From it: the side-turn histogram and the sub-7 count of each value (`side_turns`), a DR in 6 or less for every case with 2 side turns or fewer (`side_turns_certain`), and every cell of the per-DRM tables of section 5 (`side_turns_by_drm`, `profiles_by_drm`, `cross_by_drm`). For 4c4e: the row-swap table of the ring pairs, checked independently like the distances (`ring_swaps_checked`); half turns to two bars equal to the larger of row swaps and hole number on every case (`half_turns_to_bars`); every cell of the tables by half turns, by row swaps and holes, by pairs, of the card's groups and inside 3 half turns (`bands_4c4e`, `swaps_slot_4c4e`, `pairs_bands_4c4e`, `card_split_4c4e`, `inside3_4c4e`); that a row swap changes the pair count by at most 2 (`pair_change`); the 3-pair recipe on every ring pair with 3 pairs (`three_pair_rule`); and that the ring pictures of appendix A are exactly the ones with 2 row swaps or fewer (`patterns_le2`). The numbers it asserts are copied by a script from the study's output, not typed.

  **Not proved in Lean**: the rule search, most of the graded rules of section 9, the second-axis option, the RZP-weighted and real-attempt populations, and the result that switched cases are uniform within their class (an argument plus the sampled test above).

**Formally verified.** What Lean proves for this study, and what it doesn't:

- *Proved* (lean/EOSwitch, as in the last bullet above): the EO-kept distance to DR of all 1,082,565 cases, the features defined from stickers, the distance histogram, the per-DRM counts and every cell of the card tables, and that the printed tables match them.
- *Proved, added 13 Nov 2026* (lean/EOSwitch, Recount.lean; marked ✓ in section 1 and the errata): the twelve switch cards (every row's states and sub-7 count, so each card's share, rate and settled share); the 4c4e your-call split by corner case; 4c4e by ARM × paired edges (Appendix A) and by paired edges × edge ARM, with both bad edges in one slice exactly when edge ARM is 0 or 2, on every 4c4e case; the settled shares of every feature (ARM, pairs, paired edges, corner case, pairs + ARM, pairs + corner case, paired edges + edge ARM, pairs + side pairs/2) for 4c4e, 4c2e, 7c8e, 8c8e and 2c2e; bars against two edges in every ARM; 7c8e with 4 pairs by edge ARM; the low DRMs by pairs and JZP; the EO's-last-turn option for 4c4e; the corner-case claims of rodneykinney ([13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383073553376612404), [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383075044682633366)), Evan ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418247728328212585), [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418248145262874785)) and Fanti ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436041311110172783)) and the graded rules quoted in section 1 and the claims table (4c2e "1.5+ pairs" switches exactly Jay's and tseitsei89's cases; 2+ and 3+ pairs; rodneykinney's pair and corner-case rule ([13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383069263530692730)); caycala's 3+ pairs; Daichi's and Zagros's 4-move rules; 7c8e 5-6 pairs; 2c2e 1+ pairs); the corner case of the errata example and its one-move NISS DR; and that the RZP's last quarter turn either way leaves the switched case unchanged (a general proof on the sticker model, with the premove step checked on every sequence of up to 3 turns).
- *Proved, for the ring sections* (lean/EOSwitch, Rings.lean and RingsThm.lean; marked ✓ in section 1 and sections 4 and 5): the turn rules of the ring picture on every case; side turns of every case, and that 2 or fewer means a DR in 6 or less; half turns to two bars as the larger of row swaps and hole number on every 4c4e case; the band tables (by half turns, by row swaps and holes, by pairs, the card's groups split, inside 3 half turns); at most two new pairs per row swap; the 3-pair recipe; the list of ring pictures with 2 swaps or fewer; side turns, setups and the cards crossed with them for the twelve DRMs.
- *An argument on top of those facts, not a Lean theorem*: why 2 side turns can't take more than 6 moves (two U/D turns before each side turn, none after the last) and why the half-turn count is the larger of the two readings (section 4.2). Lean checks both statements case by case; the reasons are on paper.
- *Proved, given the uniformity argument* (lean/EOSwitch): the better-of-normal-and-inverse option for 3c6e, 4c4e, 8c8e, 7c8e and 4c2e (Noah Swor's comparison, [3 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1269374128155267147)), as the class average the uniformity argument gives.
- *Proved, for the errata* (the Corrections library in the folder of [*Which HTR routes to try from a DR*](../htr-routes/), lean/FakeBound/Corrections/Examples.lean, built on lean/EOSwitch): the errata example's DRM, ARM, pairs and distance to DR, and that its printed DR is valid (`eo_switch_examples`), and the shortest case of each of the 15 4c4e ARM sets, so 11 sets sub-6 and 7 sub-5 (`arm_sets`).
- *Computed, not proved*: the U/D turns per half-turn count (section 4.5 and appendix A), the DRs by quarter turns (section 4.6), where the half turn of a setup goes (section 5.4), the information measures, the two findings behind *no formula* (section 4.4), the ring reading on normal (sampled), the rule search and most of section 9's graded rules, the second-axis option, the RZP-weighted populations and the real attempts (6,000 scrambles, including the sampled figures after a switch in section 1), the uniformity of switched cases within their class, and the NISS readings (sampled).

## Docs referred to

- Cale, [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0) and [*DR setup stats (switching last move of EO)*](https://docs.google.com/spreadsheets/d/1_2PmFv1KyBX335SjSb4oweS0sx804fIhbuP50D-gBj4).
- Louis, [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs), code at [github.com/LouisSart/DRM-ARM-stats](https://github.com/LouisSart/DRM-ARM-stats).
- rodneykinney, [*DRM corner variant+pair stats*](https://docs.google.com/spreadsheets/d/174ClwBFl-T2zJAq8MVyK1bKsIIuzxQU0_XmQGv82LPQ), [*DRM Subsets*](https://docs.google.com/document/d/1AUQVrecEFZyR6okXAyJgtQZA-A0AJmAUevhJZlQMjAs) with its [sheet](https://docs.google.com/spreadsheets/d/1gJxjQD77bb0u124cPBLQcS5IT2_6F97s-1qorfCKK2M) and [decision trees](https://rodneykinney.github.io/DRM-ARM-stats/drm_trees/), [*DRM Subsets Meta*](https://docs.google.com/document/d/1Jnd1Qy_6b1W5dR5fZQScloMoMPR2LCAF7VPrgeTaRgg), [*DR - 4c4e Theory*](https://docs.google.com/document/d/1DsxAAB2WRfpgDR-VWZZrXq2W4y_YMXBufRRYNLAGGoU), [*Axial Reduction Theory*](https://docs.google.com/document/d/1TomrUJ9XWAQXBp7ghSB-iXs1WpPm20FGUw5OBoKgn7g), [*Domino Setup Theory*](https://docs.google.com/document/d/1Z3O8BY1LbAMF6m55ufXtSdtBVwSJpMArtRrDT-p_CwM), and code at [github.com/rodneykinney/DRM-ARM-stats](https://github.com/rodneykinney/DRM-ARM-stats).
- Evan, [*4c4e ARM subtype stats*](https://docs.google.com/spreadsheets/d/1PAVonITR4HLBMml1-uxJwGRwHIoRWIGdNsK-A_KG_yA) and [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk).
- Fanti, *armpairs_1.txt*, attached to the message of [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069).
- Levi Gibson, [*Sub-7 simulations*](https://docs.google.com/spreadsheets/d/1Nqr2yICQqXuKrs1pkXWizsYw7-OU6FU4F7hzaE7pN2E).
- [*Hitchhiker’s Guide to DR*](https://docs.google.com/document/d/1E_5wSKvQFXXZY4f3xLM76qMUrVGp9Pe7vgotS0X-T4U) (the pair-tracing section is credited to wen).
- My earlier studies: [*EO to DR, and scramble to DR*](../eo-to-dr/) and [*Is DR-xs worth it?*](../is-dr-xs-worth-it/) (the sticker model).
- nissy 2.0.8, by Sebastiano Tronto ([nissy.tronto.net](https://nissy.tronto.net)), used for the cross-checks.
