# When to switch an EO

You have an EO and an RZP, and you're deciding whether to switch: go to the inverse, keep the EO, and look for a short DR there. Right now the main thing people go by is the number of pairs on the inverse, sometimes with ARM or the corner case on top. This page asks whether there's a better policy that you can still run in a few seconds, and it grades every policy by what it *misses*: not switching a 4-mover hurts more than not switching a 5-mover, and both hurt more than switching something that turns out to be a 7. Everything is counted exactly over all 1,082,565 EO-solved cases of one EO axis and one DR axis. The one sampled thing is a check on real attempts (8,427,192 5-move EO + RZPs on 6,000 uniformly random scrambles).

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion). Docs and sheets are listed with links at the end. An earlier version of this page (13 November 2026) led with a different rule, the number of half turns to two bars. Section 7 says what that count is worth and why it isn't the recommendation here.

**This builds on** what the server already had. Most of the card is other people's reads put together:

- **The pairs policy**, as rodneykinney's [*DRM Subsets Meta*](https://docs.google.com/document/d/1Jnd1Qy_6b1W5dR5fZQScloMoMPR2LCAF7VPrgeTaRgg) puts it: one pair threshold per DRM, "Discard if not one of the identified subsets." It comes out of the decision trees of [*DRM Subsets*](https://docs.google.com/document/d/1AUQVrecEFZyR6okXAyJgtQZA-A0AJmAUevhJZlQMjAs). tseitsei89's short form: "So just simply if >1 pair = switch, else discard" ([25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409603207239307457)).
- **Pairs + corner case.**
  - rodneykinney's corner cases 4a to 4d ([*DR - 4c4e Theory*](https://docs.google.com/document/d/1DsxAAB2WRfpgDR-VWZZrXq2W4y_YMXBufRRYNLAGGoU)), the [*DRM corner variant+pair stats*](https://docs.google.com/spreadsheets/d/174ClwBFl-T2zJAq8MVyK1bKsIIuzxQU0_XmQGv82LPQ) sheet and the rule that came with it ([13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383069263530692730)).
  - rodneykinney's read for 0 pairs: "To catch this case, you can switch 4a-0 and 4d-2, but only if there also are no fake pairs" ([13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383075044682633366)).
  - tseitsei89's working list ([25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018)), wen's and Jay's own versions ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418235860729462835), [21 Jun 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1385890589886775387)).
  - Evan's split of 1 pair + ARM 21 by corner type: "b corners - 29%", "d corners - 89%", "a corners - ~34% if corners are stacked, < 5% otherwise" ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418283868007436308)). That split is on the card as it stands.
- **Pairs + ARM.**
  - Louis's [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs) and Evan's [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk) sheet.
  - caycala's chart ([25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1365334546035245227)): for 4c4e it already has 1 pair with ARM 21 and 0 pairs with ARM 42, and its 7c8e list is this page's 7c8e card.
  - Fanti's rule sets with their measured performance (*armpairs_1.txt*, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069)). On the yardstick used here Fanti's 4c4e list is the best thing on the server for 4c4e.
- **The other reads the cards use.**
  - Side pairs and the 1.5+ pairs rule for 4c2e (rodneykinney, [30 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1411385789891350698); Jay, [14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383640829280780392)).
  - wen's 3c2e rule with fake pairs and split pairs ([12 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1471458126539526323)).
  - Daichi's dead 5-pair ARMs for 7c8e and JZP with b corners for 4c2e ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436036602723045579)), and "8c8e 2 pair 42a is a good switch" ([5 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1479211440916271114)).
  - Jay's 5c rule: "iirc, need 2 pairs + ar21 for 5c4e to be good (3 pairs if it's another arm), same for 5c6e but need one extra pair" ([21 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1396982409290977382)).
  - bpaul's idea of looking at pairs per edge ([21 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1397028793960370187)) and Yura Riabov's "From my experience with pairs 1 bar is worse than 2 pairs for most arms" ([22 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1397110208685146265)).
- **How to read the inverse from normal**: wen's pair tracing in the [*Hitchhiker's Guide to DR*](https://docs.google.com/document/d/1E_5wSKvQFXXZY4f3xLM76qMUrVGp9Pe7vgotS0X-T4U), rodneykinney's side-pair read in [*Domino Setup Theory*](https://docs.google.com/document/d/1Z3O8BY1LbAMF6m55ufXtSdtBVwSJpMArtRrDT-p_CwM) and the corner-case flow chart in *DR - 4c4e Theory*, Jay's ARM by colour ([28 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1223072354956218589)).
- **The two bars** as the 4c4e target: Andrew's video [*How to do Domino Reductions: The Secret They Don't Want You To Know*](https://www.youtube.com/watch?v=oAbPQOfui2U) (FewestMoves channel, 2019) and *DR - 4c4e Theory* ("The final trigger must have two full “bars” formed with the bad corners and edges.").
- **Cale's [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0)** for the DR length of every case, and two of my own studies: [*EO to DR, and scramble to DR*](../eo-to-dr/) (the same table, proved in Lean) and [*Judging a DR by hand*](../judging-a-dr/) (what a move of DR length is worth at the finish).

**What this adds**:

- **A yardstick that counts misses by length.** For every policy: how much it switches, and which share of the 4-or-less, the 5-movers and the 6-movers it leaves on the table. The current rules hadn't been broken down that way.
- **A switch card per DRM**: pairs first, then one or two more looks that depend on the pair count. On 4c4e, 4c2e, 3c2e and 7c8e together it switches a little less than the pairs policy and misses less at every length.
- **Three reads that I didn't find in anyone's rule**:
  - for 2 pairs on one edge, where the two holes are;
  - for 1 pair with ARM 21 and 4b corners, whether there's exactly one side pair;
  - for 0 pairs and no fake pairs (rodneykinney's read), that the corners are 2 and 2 in the layers.
- **New cards for 8c8e and 2c2e**, and side pairs in the 5c pockets.
- **The half-turn count judged as a switch test**, on what it catches and on what it takes to read.
- **What doesn't help**, and **how far any rule could go** from the quick reads, so you know what's left on the table.
- **Every read done on the normal side by colour**, checked on 65,000 random cubes.

**Terms**, as the server uses them. *Switch* means NISS: after EO + RZP you go to the inverse and keep the EO. *DRM* is bad corners then bad edges (4c4e), counting all edges out of DR. *AR* (axial reduction) is the state you can finish with DR moves on the R/L axis, and *ARM* is how far you are from it, two digits, corners then edges (21 = AR-2c1e). *Pairs* are top pairs, *fake pairs* are the same two pieces with the corner twisted the other way, *side pairs* are E-slice pairs. A *bar* is two pairs on one edge. *4a* to *4d* are rodneykinney's corner cases, with the corner ARM as suffix (4b-0). *JZP* is ARM 00 with an even number of bad corners. *Sub-7* is a DR in 6 or less with the EO kept, and an *N-mover* is a case whose shortest such DR has N moves. One word is not the server's: a *hole* is an E-slice place of the inverse that holds a U/D edge. On normal you see it as an E-slice edge that's out of the slice. Section 3 has the exact definitions, section 6 how to read each thing before you switch.

**How to read it.**

- **Start with [section 1](#1-the-short-version)**. If you only want the rule, it's the 4c4e card there and the other cards in [section 5](#5-the-cards).
- **[Section 6](#6-reading-the-card-on-normal-and-how-long-it-takes)** is how each read looks on the cube in your hand. The **[worked examples](examples.html)** are real attempts to play along with: what you see, what the card says, what the pairs rule says, and the DR after the switch, folded away.
- **Sections 7 to 10** are the evidence: the two-bars count, what didn't work, the ceilings, other RZP lengths. Anything marked **computer only** is an answer key, not something to do in an attempt.
- **The [errata](errata.html)** have one statement from the server that the numbers go against.

---

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | The answer, the 4c4e card, what it is worth against pairs and against pairs + ARM, the two-bars verdict. |
| [2. What was asked](#2-what-was-asked) | The questions, quoted, with where each is answered. |
| [3. Definitions and the yardstick](#3-definitions-and-the-yardstick) | Switched case, DR length after the switch, what a miss costs, the reads, the populations. |
| [4. The current policies, by what they miss](#4-the-current-policies-by-what-they-miss) | Pairs, pairs + corner case, pairs + ARM: how much each switches and which 4-, 5- and 6-movers it leaves behind. |
| [5. The cards](#5-the-cards) | **The main result.** 4c4e in full, then 4c2e, 3c2e, 7c8e, 8c8e, 2c2e and the pockets in the low DRMs. |
| [6. Reading the card on normal, and how long it takes](#6-reading-the-card-on-normal-and-how-long-it-takes) | Every read as a colour match on the side you are on, the check on random cubes, a worked attempt, which reads you need how often. |
| [7. Two bars, evaluated](#7-two-bars-evaluated) | What the half-turn count is worth as a switch test, what it takes to read, and where it does earn its keep. |
| [8. What didn't help](#8-what-didnt-help) | The reads and systems I tried that add little or nothing, one line each. |
| [9. How far a rule can go](#9-how-far-a-rule-can-go) | **Computer only.** The best possible rule from each set of reads, and the gap to knowing the exact DR length. |
| [10. Other RZP lengths, real attempts, other weights](#10-other-rzp-lengths-real-attempts-other-weights) | The card after a 4-move and a 6-move RZP, on 8.4 million real attempts, and under other prices for a miss. |
| [11. The claims, checked](#11-the-claims-checked) | What people said about these rules, with the exact numbers next to it. |
| [12. What this does not cover](#12-what-this-does-not-cover) | Limits. |
| [Appendix A: full tables](#appendix-a-full-tables) | Every card with all its groups, every current policy per DRM, the other RZP lengths per group. |
| [Appendix B: how it was computed, and what checks it](#appendix-b-how-it-was-computed-and-what-checks-it) | The model, the search for the cards, the checks, what is proved in Lean. |
| [Docs referred to](#docs-referred-to) | Links. |

---

## 1. The short version

**Is there a better switch policy than pairs? Yes, a bit better, and it stays a matter of seconds.** Keep counting pairs first. What changes is the one extra look you take after it, which depends on the pair count. No quick read beats pairs as the first look: I tried every relation between two bad pieces, points systems, corner-only counts and trees that don't start from pairs, and pairs stays the first split every time (section 8).

**The yardstick.** After a 5-move RZP a case is *good* if the DR after the switch is 6 or less. A policy is graded on four numbers: how much it switches, and the share of the 4-or-less, of the 5-movers and of the 6-movers that it doesn't switch. When one number is needed, a declined 6-mover costs 3 wasted switches, a 5-mover 9 and a 4-or-less 27 (section 3 says where that comes from, section 10 what happens with other prices).

**4c4e: the card.** One row per group of switched cases. The last three columns say how much of all of 4c4e's 4-or-less, 5-movers and 6-movers sits in the group.

| What you read (4c4e) | Verdict | Share of 4c4e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 3 or 4 pairs | **switch** | 3.6% | 79.9% | 57.4% | 21.0% | 11.0% |
| 2 pairs on two edges | **switch** | 11.9% | 53.9% | 31.1% | 46.5% | 30.4% |
| 2 pairs on one edge (a bar), holes on one R/L face | **switch** | 3.5% | 43.7% | 3.5% | 9.8% | 7.8% |
| 1 pair, ARM 21, 4d corners | **switch** | 0.82% | 88.9% | 5.5% | 3.9% | 3.7% |
| 1 pair, ARM 21, 4b corners, 0 or 2 side pairs | **switch** | 2.8% | 50.4% | 0% | 6.4% | 8.0% |
| 1 pair, ARM 21, 4a corners in two columns | **switch** | 1.5% | 34.8% | 0% | 2.6% | 2.9% |
| 0 pairs, no fake pairs, corners 2 and 2 in the layers | **switch** | 0.82% | 21.9% | 2.4% | 0.97% | 0.84% |
| 2 pairs on one edge (a bar), holes not on one R/L face | if you have time | 7.0% | 18.1% | 0% | 2.3% | 8.0% |
| 1 pair, not ARM 21, 2+ side pairs, not 4b corners | if you have time | 6.8% | 19.2% | 0% | 1.9% | 8.4% |

Everything else is a skip: 1 pair without ARM 21, 0 pairs with a fake pair, and the two exceptions inside 1 pair + ARM 21 (4b corners with exactly one side pair, 5.6% sub-7; 4a corners that aren't in two columns, 2.5%).

**What it's worth on 4c4e.** Each row is a policy. *Cost per case* is the one-number version: misses and wasted switches, priced as above, per 4c4e case.

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| 2+ pairs | *DRM Subsets Meta*; tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409603207239307457) | 26.0% | 8.0% | 20.4% | 42.8% | 0.413 |
| 2+ pairs, or 1 pair with 4d corners | tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018) | 27.7% | 2.4% | 16.6% | 39.2% | 0.381 |
| 3-4 pairs; 2 pairs unless 4b-0; 1 pair if 4d-2; 0 pairs if 4a-0 or 4d-2 with no fake pairs | rodneykinney, [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383069263530692730), [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383075044682633366) | 25.4% | 1.4% | 16.8% | 41.4% | 0.370 |
| 2+ pairs; 1 pair if 4d or one U/D turn from 4d; 0 pairs if anti-AR or the D F2 B2 R case | wen, [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418235860729462835) | 29.4% | 0.35% | 11.0% | 37.1% | 0.362 |
| 3-4 pairs; 2 pairs with ARM 10, 11, 20, 21, 31, 32 or 42a; 1 pair with ARM 21; 0 pairs with ARM 42 | caycala, [25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1365334546035245227) | 29.5% | 9.3% | 13.1% | 35.4% | 0.381 |
| 2+ pairs; 1 pair with ARM 21; 0 pairs with JZP or ARM 42 | Fanti, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069) | 35.2% | 1.4% | 5.8% | 27.0% | 0.345 |
| **the card** | this page | 24.9% | 0% | 8.8% | 35.4% | 0.299 |
| the card with its *if you have time* groups | this page | 38.8% | 0% | 4.7% | 19.1% | 0.326 |

So against **2+ pairs** the card switches a little less and misses less at every length: no 4-or-less at all (pairs: 46 of 578), 8.8% of the 5-movers instead of 20.4%, 35.4% of the 6-movers instead of 42.8%. Against **pairs + ARM** (Fanti's list) it's a trade: 10.3 points fewer switches, for more missed 5- and 6-movers. Take the two *if you have time* groups as well and you miss less than Fanti's list at every length, for 3.6 points more switches. Honestly, at that end Fanti's list is already about as good as a short list gets. The card's gain is at the pairs end.

**The four DRMs people switch, together.** 4c4e, 4c2e, 3c2e and 7c8e, every case once (111,104 cases):

| Policy (4c4e, 4c2e, 3c2e and 7c8e together) | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|
| pairs only (the *DRM Subsets Meta* table) | 27.6% | 5.1% | 12.8% | 37.0% | 0.363 |
| the best list on the server for each DRM (Fanti's pairs + ARM for 4c4e, caycala's chart for 7c8e, 1.5+ pairs for 4c2e, wen's rule for 3c2e) | 32.6% | 0.88% | 3.8% | 27.7% | 0.314 |
| **the cards** | 26.3% | 0% | 5.4% | 31.9% | 0.282 |
| the cards with their *if you have time* groups | 38.3% | 0% | 2.9% | 17.7% | 0.304 |

**What's in the card, and whose it is.**

- **2 pairs on one edge is not 2 pairs on two edges** (new here). Two edges: 53.9% sub-7. A bar: it depends on the two holes. Holes on one R/L face (the two E-slice edges that are out of the slice share red or orange): 43.7%. Otherwise 18.1%, which is 7.0% of 4c4e that the pairs rule switches at a 1-pair rate. bpaul asked about pairs per edge and Yura Riabov said a bar is worse. The holes are what makes it a rule.
- **1 pair + ARM 21, by corner type** (Evan's split, exact: 4d 88.9%, 4b 28.8%, 4a in two columns 34.8% and 2.5% otherwise). New here is what splits the 4b cases, the side pairs: with none it's 36.3%, with exactly one 5.6%, with two 64.5%.
- **0 pairs: no fake pairs either, and the corners 2 and 2.** No fake pairs with 0 pairs is rodneykinney's read for the `F2 B2 R` setups, and wen has it for `D F2 B2 R` ("there are 2 'columns' of corners and no fake pairs", [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418241461048049796)). Adding that the misoriented corners are two white and two yellow gives 0.82% of 4c4e that holds every 0-pair case of 4 moves or less:

```
R' B2 F2 U'   // setup: 4c4e, 0 pairs, no fake pairs, 2 white and 2 yellow corners
U F2 B2 R   // DR in 4. The pairs rule says discard
```

**The other DRMs** (section 5). One row per DRM, the card against everything in that DRM:

| DRM | Sub-7 rate | Card switches | Sub-7 rate of what it switches | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers |
|---|---|---|---|---|---|---|
| 4c4e | 19.2% | 24.9% | 54.8% | 0% | 8.8% | 35.4% |
| 4c2e | 18.7% | 24.8% | 56.3% | 0% | 0% | 31.0% |
| 3c2e | 61.6% | 82.1% | 71.2% | 0% | 0% | 7.4% |
| 7c8e | 16.4% | 23.0% | 52.6% | 0% | 0% | 32.6% |
| 8c8e | 14.5% | 27.9% | 37.9% | 0% | 0% | 30.6% |
| 2c2e | 23.7% | 29.0% | 64.6% | - | 0% | 23.4% |
| 4c6e | 4.6% | 3.6% | 42.8% | 0% | 38.7% | 71.2% |
| 3c4e | 9.9% | 17.1% | 36.0% | - | 8.7% | 41.2% |
| 3c6e | 4.8% | 7.0% | 30.9% | 0% | 33.3% | 59.1% |
| 5c4e | 7.2% | 6.8% | 32.3% | 0% | 43.2% | 73.3% |
| 5c6e | 6.1% | 6.3% | 32.3% | 0% | 42.7% | 70.3% |
| 6c6e | 5.6% | 3.0% | 36.0% | 40.0% | 64.6% | 82.6% |

- **4c2e**: 1.5+ pairs stays, plus two small groups: 0 pairs with JZP and 4b corners (Daichi's read), and 1 pair without a side pair when the corners are 4b-0 (in rodneykinney's corner table).
- **3c2e**: wen's rule is the card (a pair, a fake pair or a split pair). What it skips is 17.9% of 3c2e at 17.5%, with no 5-mover in it, as wen said.
- **7c8e**: caycala's chart is the card. Fanti's list is the same thing without the chart's ban on edge ARM 0 and 4.
- **8c8e and 2c2e**: new cards (section 5.5). The 8c8e one costs 0.291 per case against 0.348 for the tree rule.
- **The low DRMs hold 42.3% of the 5-movers.** Counting the 12 DRMs of this page, 4c6e, 3c4e, 3c6e, 5c4e, 5c6e and 6c6e hold 21.8% of the 4-or-less, 42.3% of the 5-movers and 58.9% of the 6-movers. Small pockets hold a good part of them (5c4e with 3 pairs and 2 side pairs is 38.3%), but a short DR out of 5c4e costs about 3.9 times the tracing and switching it costs out of 4c4e (section 5.6).

**How long it takes.** Every read on the card is a count or a colour match on the pieces you already look at for the pair trace: the U/D edges in the E slice, the misoriented corners, and the E-slice edges that are out. None of them needs you to work out where a piece sits on the inverse. On 42.2% of 4c4e cases the pair trace settles it, and on average the card asks for 0.75 extra looks per 4c4e RZP, ARM being most of that. The longest branch (1 pair, ARM 21, 4b corners: 5.4% of cases) adds the corner case and the side pairs to the pairs + ARM check that Yura Riabov puts at "Like 5 seconds" ([17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417786183135526954)). I haven't timed anyone, and not everybody reads ARM that fast, so that's an argument and not a measurement (section 6).

**Two bars: a good read, not a switch test yet.** The numbers are good. Switch at 2 half turns or fewer and you switch 14.2% of 4c4e, with every 4-or-less in it, including all 46 that the pairs rule misses and 248 of the 508 5-movers it misses. Its cost per case is 0.332: better than any list on the server, behind the card (0.299), because it leaves 54.8% of the 6-movers. On top of the card it would help: the card plus *2 or fewer* costs 0.266.

The problem is reading it. The count needs the place of all eight bad pieces on the inverse and then a search, where the card needs colour matches. Zagros is convinced full NISS tracing of 4c4e is the way ("I think the optimal system is 100% niss tracing 4c4e", [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436040007654838402)), tried it, "did it for like four solves and gave up", because "I niss trace and then I just don't know if it has a 6 move DR or not. I need to actually do a few moves to check" ([19 Jan 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1462981640702656729)). caycala timed a whole switch at about 20 seconds and concluded about tracing instead: "tldr i dont think it’s worth it + it is much more mistake prone" ([16 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1395178375114653788)). The count is exactly a way to judge the DR after a trace, so it might be what Zagros was missing, but nobody has shown it done in a few seconds. Until someone does, I don't recommend it as the test before switching. If you can read it, add *2 or fewer: switch* to the card (section 7).

**How much is left.** **Computer only**: the best rule that uses every quick read at once (3,757 cells for 4c4e) would switch 24.4%, miss no 5-mover and 9.5% of the 6-movers. So the information is in the colours. It just doesn't fit in a rule you can carry: going from the card's 13 groups to 40 only moves the cost from 0.299 to 0.267 (section 9).

**Other RZP lengths.** After a 4-move RZP a DR in 7 is enough, and 59.4% of 4c4e has one. At the same prices every group of the card is then worth a switch, the 0-pair leftovers included, so "It seems like you should pretty much always switch a 4 move DR-4c4e." (Zagros, [7 Jul 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1524175174507692245)) holds. After a 6-move RZP only 3 or 4 pairs and 1 pair with ARM 21 and 4d corners are left (section 10).

---

## 2. What was asked

**Is there a better switching policy than pairs, with ARM and the corner case for some cases?** A way to switch more good cases or fewer bad ones, computable by a human from the cube state in seconds, without a full NISS trace of the bad pieces, where missing a good continuation counts for more than switching a bad one. *Answer*: the cards of section 5, graded in section 4 against the current policies. The gain over pairs is real and costs no extra switches overall (fewer on 4c4e, 3c2e and 7c8e, more on 4c2e). The gain over the pairs + ARM lists is small.

**Is the two-bars count fast enough to use?** *Answer*: nobody has shown that it is, and what people have said points the other way. Its numbers are good, so it's worth someone trying (section 7).

**The same questions, as people on the server asked them.**

- wen ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418248619374678247)): "Interestingly now we have basically 3 criteria for NISS that we can trace, >1pair/ARM/corner structure", "if we pick 2 out of 3 to stick to, which gives the lowest false negative rate?" *Answer*, with the best rule each pair of reads allows (section 9, **computer only**): on 4c4e pairs + ARM misses the least of the short ones (5.8% of the 5-movers, against 17.2% for pairs + corner case), and it switches more to do it. Nothing without pairs is close.
- wen ([13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383079417881821314)): "I personally think that the false positive rate isn't that important because switching something that ends up being bad isnt the worst thing, it's much worse to not switch something that is actually good, but the method says don't switch". And later: "false negative are more important because it will be the one that has an 18 then you will be sad" ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418282250230825144)). That's the yardstick of this page. The other side, for the record: "false positives are more important because i only have time to fully check a few EOs, and if im switching an RZP then i damn well better get a short DR out of it, lmao" (compLex, [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418290226895257621)), and rodneykinney on 2+ pairs: "It does miss some good cases, but I never have enough time to NISS every EO, so I'm mostly looking for excuses to avoid NISSing, and this is a pretty good one." ([20 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1154070313554956380)). The tables give all four numbers, so you can read them your own way.
- tseitsei89 ([25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409607396103290960)): "It would be really nice to find a way to filter out good 1 pair cases but there doesnt seem to be one currently". *Answer*: ARM 21 first, then Evan's corner types, then the side pairs for 4b (section 5.1). That takes the switched 1-pair cases from 31.2% sub-7 (all of 1 pair + ARM 21) to 52.0%.
- bpaul ([21 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1397028793960370187)): "random thought i wonder whether looking at pair stats not just on the count but also based on the number of pairs per edge could be good". *Answer*: yes for 2 pairs on 4c4e, once you add where the holes are (section 5.1).
- Zagros ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418250491120320532)), on not wanting to miss anything when switching: "seems like that would cause an absurd amount of rescrambling, maybe I'm just far too slow at solving at 3x3". *Answer*: here's the number. Missing no case of 5 or less on 4c4e by pairs and ARM alone means switching 59.8% of the cases. The card with its *if you have time* groups gets to 4.7% of the 5-movers missed at 38.8%.

What's left open is in section 12.

---

## 3. Definitions and the yardstick

Everything is written for an F/B EO and a DR on U/D. With white on top and green in front the U/D colours are white and yellow, the F/B colours green and blue, the R/L colours red and orange. Other axes are the same thing turned.

**Case, switched case.** What matters for the DR is the *case*: which corners are twisted and how, and which places hold the four E-slice edges (2187 × 495 = 1,082,565 cases). After EO + RZP you have a case on normal. Switching means doing the DR on the inverse with the EO kept, so the case that matters is the inverse's, the *switched case*. Every rule here is about the switched case, read from the normal side (section 6).

**DR length, good.** The fewest turns of U, D, R, L, F2, B2 that take the switched case to DR (linear, EO kept). After a 5-move RZP a case is *good* if that's 6 or less, the usual sub-7: "we are normally looking for rzp in 5 or less and dr in 11 or less. So sub-7 from 5 move rzp gives that" (tseitsei89, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436061424110538882)). For a 4-move RZP good means 7 or less, for a 6-move RZP 5 or less (section 10).

**What a policy is graded on.** A policy says switch or don't for every case of a DRM. Its grade is four numbers:

- *Switched*: the share of the DRM's cases it switches.
- *Missed: 4 or less*, *missed: 5-movers*, *missed: 6-movers*: of the cases with a DR that long, the share it doesn't switch.

If policy A switches no more than B and misses no more at each of the three lengths, A is better whatever you think a miss is worth. Where neither wins that way you need prices.

**The prices.** A switch that finds no DR in 6 costs 1. Not switching a 6-mover costs 3, a 5-mover 9, a 4-or-less 27. *Cost per case* is the total over the DRM divided by its cases, so lower is better. Two choices went into that:

- *Each move shorter counts three times as much.* A DR one move shorter leaves one more move for the finish. Over every DR state, an optimal finish in 10 or less is 0.74%, in 11 or less 3.6%, in 12 or less 15%, in 13 or less 44% (from *Judging a DR by hand*). So one move of DR length is worth a factor of 4 to 5 in the odds of a tight result and about 3 for a loose one. I use 3, the careful end, so the short cases aren't over-weighted. That's the asymmetry the grading has to carry: a declined 4-mover is worth nine declined 6-movers.
- *A declined 6-mover costs 3 wasted switches.* With that, a group whose good cases are all 6-movers is worth switching from 25% sub-7, and a group with 4c4e's usual mix of lengths from about 16%. The server's own cut-offs sit around there: "i switch for around 20% and above" (Yura Riabov, [12 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1272564881358323785)), "I would say below 20% is never and above 30% is pretty much always.", with "Of course as we get better estimators and statistics those might/will change." (tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409573949486137425)), "i think it's best to find the <10% ones and dont switch for those and switch everything else maybe" (wen, [12 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1272564863230808065)).

Section 10 redoes the comparison with a 6-mover at 2 and at 5 and with a factor of 2 and of 4.5. The card stays ahead of every current policy in each of them, and at 5 its wider version is the cheapest.

**The reads.** All on the switched case; section 6 has each one as you see it on normal.

- *Pairs*: a bad edge in the U or D layer (an E-slice edge sitting there) and a bad corner next to it in its layer, twisted so that its U/D sticker is on the side face the edge doesn't touch. As after R from solved, which has 4 pairs. *On one edge* or *on two edges* says where 2 pairs are. Two on one edge is a *bar*.
- *Fake pair*: the same two pieces with the corner twisted the other way.
- *Side pair*: a bad edge in the E slice (a U/D edge sitting there) and the corner above or below it with its U/D sticker on F or B.
- *ARM*: corner ARM is the number of bad corners with their U/D sticker on R or L, edge ARM the number of bad edges in the M slice (at UF, UB, DF, DB). A piece that doesn't count is *in AR*. ARM 21 is what `U' R` leaves.
- *Corner case*, for four bad corners: by how they split between the two HTR orbits. 4d is all four in one orbit, 4c is 3 and 1. 2 and 2 is 4b if some U, D, R or L face has exactly 1 or 3 of them, and 4a otherwise. The suffix is the corner ARM (folded to 0 to 2, except for 4a).
- *Columns*: a column is the two corner places above each other. Four bad corners are *in two columns* when each one sits above or below another one. That's Evan's *stacked*.
- *Holes*: the E-slice places that hold a U/D edge. With two holes: on one R/L face (FR and BR, or FL and BL), on one F/B face, or diagonal.
- *Layers*: how many bad corners are in the U layer and how many in the D layer (*2 and 2*, *3 and 1*, all in one).
- *Split pair* (wen, for 3c2e): a bad edge and a bad corner in the same layer, not next to each other, both in AR or both out of AR.

**Verdicts.** *Switch*: the group is worth it at the prices above. *If you have time*: the next groups down, between about 15% and 25% sub-7. They're just under break-even at these prices and above it for anyone who prices a 6-mover higher. *Skip*: the rest.

**Populations.** *Exact*: every case of the DRM counts once. That's the right weighting for switched cases. Do any sequence of DR moves (U, D, R2, L2, F2, B2) before the scramble: the case on normal stays what it was (same EO, same RZP, same DRM), and the inverse runs evenly over every case with the same DRM and the same number of clockwise and counter-clockwise corners. Both scrambles are equally likely, so whatever you did on normal, the switched case is uniform over those. For 4 bad corners that's the whole DRM. For 8c8e it's two classes, 4 and 4 or 7 and 1 (section 12). *Real attempts*: 6,000 uniformly random scrambles, every EO of up to 5 moves on every axis and side, every RZP after it that first reaches its DRM at a total of 5 moves: 8,427,192 switched cases. It's a sample, used as a check (section 10).

---

## 4. The current policies, by what they miss

Three kinds of rule are in use. Here's each as its author wrote it, graded on 4c4e. Each row is a policy.

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| 2+ pairs | *DRM Subsets Meta*; tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409603207239307457) | 26.0% | 8.0% | 20.4% | 42.8% | 0.413 |
| 2+ pairs, or 1 pair with 4d corners | tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018) | 27.7% | 2.4% | 16.6% | 39.2% | 0.381 |
| 3-4 pairs; 2 pairs unless 4b-0; 1 pair if 4d-2; 0 pairs if 4a-0 or 4d-2 with no fake pairs | rodneykinney, [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383069263530692730), [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383075044682633366) | 25.4% | 1.4% | 16.8% | 41.4% | 0.370 |
| 2+ pairs; 1 pair if 4d or one U/D turn from 4d; 0 pairs if anti-AR or the D F2 B2 R case | wen, [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418235860729462835) | 29.4% | 0.35% | 11.0% | 37.1% | 0.362 |
| 3-4 pairs; 2 pairs with ARM 10, 11, 20, 21, 31, 32 or 42a; 1 pair with ARM 21; 0 pairs with ARM 42 | caycala, [25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1365334546035245227) | 29.5% | 9.3% | 13.1% | 35.4% | 0.381 |
| 2+ pairs; 1 pair with ARM 21; 0 pairs with JZP or ARM 42 | Fanti, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069) | 35.2% | 1.4% | 5.8% | 27.0% | 0.345 |
| **the card** | this page | 24.9% | 0% | 8.8% | 35.4% | 0.299 |

**Pairs only.** 2+ pairs switches 26.0% of 4c4e at 46.4% sub-7. What it leaves behind: 46 of the 578 cases of 4 or less, 508 of the 2,486 5-movers and 4,500 of the 10,512 6-movers. So a fifth of the 5-movers have 0 or 1 pair. Here's one with 1 pair, ARM 21 and 4d corners:

```
L' F2 D L2   // setup: 4c4e, 1 pair, ARM 21, 4d corners
L2 D' F2 L   // DR in 4
```

**Pairs + corner case.** Adding 4d for 1 pair (tseitsei89, rodneykinney) gets most of the 4-or-less back and little else: the 5-movers go from 20.4% missed to 16.6%. wen's version (1 pair with 4d corners or one U/D turn from 4d; 0 pairs if it's anti-AR, every bad piece out of AR, or the `D F2 B2 R` case) does better, 11.0%.

**Pairs + ARM.** 1 pair with ARM 21 was on caycala's chart in April 2025, next to 0 pairs with ARM 42, and ben kyle wrote "I've gotten a lot better results recently from blindly switching 2 pairs and 1pair + arm2c1e since it's so fast to check" ([11 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404499232806932480)). Fanti's list is that with every 2-pair case and JZP for 0 pairs. It misses 5.8% of the 5-movers and 27.0% of the 6-movers, the least of any rule on the server, and pays for it with 35.2% of 4c4e switched. It's also exactly the best rule you can build from the pair count and the two ARM digits at these prices: the search of section 9 lands on the same list. Fanti's own figures for it, "35.2% switches", "42.6% sub-7 switch success (15.0% total)" and "4.3% of cases will be discarded with sub-7", come out at 35.2%, 42.6% and 4.2% with the EO kept.

**Where the room is.** Two places.

- *Inside 2 pairs.* Most people switch every 2-pair case ("2 pairs I just always switch.", tseitsei89, [17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417807554448195655); "I just switch regardless", wen, [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418281333838446723)). rodneykinney's rule and compLex drop 4b-0, and caycala's chart keeps 2 pairs only with some ARMs. 7.0% of 4c4e is a bar with the holes off the R/L faces, at 18.1%.
- *Inside 1 pair + ARM 21.* It's 9.1% of 4c4e, and 4.0% of 4c4e inside it is under 6% sub-7.

Both are places where a list *switches too much*. Dropping them is what pays for switching the good 0- and 1-pair groups without more switches in total.

The same grading for the other DRMs is in section 5 and appendix A.

---

## 5. The cards

Every card starts with the pair count, because no other quick read comes close as a first look (section 8). After that it's one or two looks, and which ones depends on the DRM and the pair count. The groups of a card don't overlap and cover the whole DRM. All numbers are exact, every case of the DRM once.

How the cards were found: a search over short rule lists on the quick reads, scored with the prices of section 3, then written down by hand in the server's words and graded again (appendix B). Where the search landed on a rule somebody already had, the card is that rule and says whose.

### 5.1 4c4e

| What you read (4c4e) | Verdict | Share of 4c4e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 3 or 4 pairs | **switch** | 3.6% | 79.9% | 57.4% | 21.0% | 11.0% |
| 2 pairs on two edges | **switch** | 11.9% | 53.9% | 31.1% | 46.5% | 30.4% |
| 2 pairs on one edge (a bar), holes on one R/L face | **switch** | 3.5% | 43.7% | 3.5% | 9.8% | 7.8% |
| 1 pair, ARM 21, 4d corners | **switch** | 0.82% | 88.9% | 5.5% | 3.9% | 3.7% |
| 1 pair, ARM 21, 4b corners, 0 or 2 side pairs | **switch** | 2.8% | 50.4% | 0% | 6.4% | 8.0% |
| 1 pair, ARM 21, 4a corners in two columns | **switch** | 1.5% | 34.8% | 0% | 2.6% | 2.9% |
| 0 pairs, no fake pairs, corners 2 and 2 in the layers | **switch** | 0.82% | 21.9% | 2.4% | 0.97% | 0.84% |
| 2 pairs on one edge (a bar), holes not on one R/L face | if you have time | 7.0% | 18.1% | 0% | 2.3% | 8.0% |
| 1 pair, not ARM 21, 2+ side pairs, not 4b corners | if you have time | 6.8% | 19.2% | 0% | 1.9% | 8.4% |
| 1 pair, ARM 21, 4a corners not in two columns | skip | 1.4% | 2.5% | 0% | 0% | 0.23% |
| 1 pair, ARM 21, 4b corners, exactly 1 side pair | skip | 2.6% | 5.6% | 0% | 0.97% | 0.76% |
| 1 pair, anything else | skip | 28.3% | 6.1% | 0% | 2.3% | 11.0% |
| 0 pairs, anything else | skip | 28.9% | 3.8% | 0% | 1.4% | 7.1% |

Read it top down:

- **3 or 4 pairs**: switch.
- **2 pairs**: on two edges, switch. On one edge, look at the two E-slice edges that are out of the slice. If they share red or orange, switch. If not, it's an *if you have time* case.
- **1 pair**: check ARM. Not 21: skip (the one *if you have time* pocket is 2 or more side pairs without 4b corners). ARM 21: look at the corners. 4d: switch. 4b: switch unless there's exactly one side pair. 4a: switch if the corners are in two columns.
- **0 pairs**: switch only if there's no fake pair either and the misoriented corners are two white and two yellow.

**The side pairs on 4b.** 1 pair, ARM 21, 4b corners, by the number of side pairs. Each row is a count:

| Side pairs (1 pair, ARM 21, 4b corners) | Share of 4c4e | Sub-7 rate | 5-movers |
|---|---|---|---|
| 0 | 1.4% | 36.3% | 0 |
| 1 | 2.6% | 5.6% | 24 |
| 2 | 1.4% | 64.5% | 160 |

A 1-pair case the card switches and the pairs rule doesn't, 5 moves:

```
L' U B2 R2 F2   // setup: 4c4e, 1 pair, ARM 21, 4b corners, 2 side pairs
F2 R2 B2 U' L   // DR in 5
```

Evan's stacked 4a corners, 5 moves:

```
L' F2 U B2 U'   // setup: 4c4e, 1 pair, ARM 21, 4a corners in two columns
U B2 U' F2 L   // DR in 5
```

A 2-pair case the pairs rule switches and the card leaves for later, 8 moves:

```
R' D L2 F2 D R2 F2 U   // setup: 4c4e, 2 pairs on one edge, holes on one F/B face
U' F2 R2 D' F2 L2 D' R   // DR in 8, and nothing shorter
```

And the card isn't free of misses. This 5-mover has 1 pair and ARM 32, and the card skips it like every other list does:

```
R' U B2 D' L2   // setup: 4c4e, 1 pair, ARM 32, 4c corners
L2 D B2 U' R   // DR in 5
```

### 5.2 4c2e

| What you read (4c2e) | Verdict | Share of 4c2e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 2 pairs (a bar) | **switch** | 7.1% | 60.0% | 88.9% | 40.4% | 17.4% |
| 1 pair and a side pair | **switch** | 15.1% | 55.5% | 11.1% | 57.4% | 43.8% |
| 0 pairs, JZP (ARM 00) with 4b corners | **switch** | 0.71% | 66.7% | 0% | 2.1% | 2.7% |
| 1 pair, no side pair, 4b-0 corners | **switch** | 1.8% | 43.3% | 0% | 0% | 5.0% |
| 1 pair, no side pair, 4a-2 corners | if you have time | 2.5% | 23.8% | 0% | 0% | 3.9% |
| 1 pair, no side pair, ARM 31 | if you have time | 4.3% | 19.4% | 0% | 0% | 5.4% |
| 1 pair, anything else | skip | 12.0% | 9.4% | 0% | 0% | 7.4% |
| 0 pairs, anything else | skip | 56.4% | 3.9% | 0% | 0% | 14.3% |

The same DRM, one row per policy:

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| 1.5+ pairs (2 side pairs = 1 pair) | *DRM Subsets Meta*; rodneykinney; Jay, [30 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1411385789891350698), [14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383640829280780392) | 22.3% | 0% | 2.1% | 38.8% | 0.280 |
| 2 pairs unless 4a-0 or 4a-4; 1 pair unless 4a-0, 4a-4 or 4b-2 | rodneykinney, [14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383638325281292389), [15 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383856871869251735) | 32.1% | 0% | 2.1% | 30.6% | 0.329 |
| 2 pairs; 1 pair with edge ARM 1 or ARM 10; 0 pairs only JZP | caycala, [16 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1395148255540678656) | 31.8% | 11.1% | 19.1% | 34.1% | 0.411 |
| 1+ pairs; 0 pairs with JZP | Fanti, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069) | 43.9% | 0% | 0% | 14.0% | 0.338 |
| **the card** | this page | 24.8% | 0% | 0% | 31.0% | 0.251 |
| the card with its *if you have time* groups | this page | 31.5% | 0% | 0% | 21.7% | 0.262 |

The 1.5+ pairs rule (2 pairs, or 1 pair and a side pair) is the top two rows, and it holds up: 2.1% of the 5-movers missed. The card adds the two groups under it, and both were on the server:

- *0 pairs with JZP and 4b corners.* JZP for 0 pairs is in caycala's and Fanti's rules. The corners are Daichi's: "for 4c2e with 0p, I think niss tracing corner positions is worth it because JZP with b corners is way better than a corners" ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436036602723045579)). Exactly: 66.7% with 4b corners, 16.7% with 4a.
- *1 pair with no side pair and 4b-0 corners*, 43.3% sub-7. rodneykinney's corner table for 4c2e ([14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383638325281292389)) switches it.

```
L' B2 F2 D2 R   // setup: 4c2e, 0 pairs, JZP, 4b-0 corners
R' D2 F2 B2 L   // DR in 5. 1.5+ pairs says discard
```

Fanti's 4c2e rule (any pair, or JZP) misses less than the card, 14.0% of the 6-movers, and switches 43.9% of 4c2e to do it. rodneykinney's corner table is graded with 4a-2 let in, as Moritz pointed out ("4a-2 seems fine (great even) and only 4a-0 is not that great", [15 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383847888249163867)) and rodneykinney agreed ("4a-2 is good. 4b-2 is the bad case, because corners are 2qt, so 6 moves is the absolute minimum to DR", [15 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383856871869251735)). It misses fewer 6-movers than 1.5+ pairs and switches 9.9 points more.

### 5.3 3c2e

| What you read (3c2e) | Verdict | Share of 3c2e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 1 pair | **switch** | 37.5% | 88.7% | 88.2% | 72.5% | 44.2% |
| 0 pairs, a fake pair or a split pair | **switch** | 44.6% | 56.5% | 11.8% | 27.5% | 48.4% |
| 0 pairs, no fake pair, no split pair | if you have time | 17.9% | 17.5% | 0% | 0% | 7.4% |

The same DRM, one row per policy:

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| always | *DRM Subsets Meta*; tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018) | 100% | 0% | 0% | 0% | 0.384 |
| a pair, a fake pair or a split pair | wen, [12 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1471458126539526323) | 82.1% | 0% | 0% | 7.4% | 0.330 |
| **the card** | this page | 82.1% | 0% | 0% | 7.4% | 0.330 |
| the card with its *if you have time* groups | this page | 100% | 0% | 0% | 0% | 0.384 |

"3c2e: just always switch" (tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018)) misses nothing and switches a 17.5% group along with the rest. wen's rule ([12 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1471458126539526323)) is exactly the cut the search finds, so it's the card. Its "At the very least you will never miss a 5 mover by doing this" is right: the skipped group has no 5-mover and no 4-mover, only 6-movers.

```
R' D' R' U2 L2 R2   // setup: 3c2e, no pair, no fake pair, no split pair
R2 L2 U2 R D R   // DR in 6, the best that group has
```

### 5.4 7c8e

| What you read (7c8e) | Verdict | Share of 7c8e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 6 pairs, not ARM 64 | **switch** | 1.9% | 96.5% | 66.7% | 23.1% | 6.9% |
| 5 pairs, not ARM 20 or 54 | **switch** | 13.9% | 55.9% | 33.3% | 70.5% | 43.2% |
| 4 pairs, ARM 21, 31 or 43 | **switch** | 6.5% | 34.9% | 0% | 6.4% | 15.9% |
| 3 pairs, ARM 21 | **switch** | 0.61% | 27.8% | 0% | 0% | 1.3% |
| 4 pairs, ARM 11, 12, 33, 41 or 62 | if you have time | 8.1% | 21.8% | 0% | 0% | 13.4% |
| 4 pairs, anything else | skip | 19.0% | 6.8% | 0% | 0% | 9.8% |
| 5 or 6 pairs with ARM 20, 54 or 64 | skip | 0.51% | 0% | 0% | 0% | 0% |
| 3 pairs or fewer | skip | 49.4% | 2.5% | 0% | 0% | 9.5% |

The same DRM, one row per policy:

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| 5+ pairs, counting edge ARM under 2 as a pair | *DRM Subsets Meta*; tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018) | 24.1% | 0% | 0% | 34.2% | 0.259 |
| 5 or 6 pairs | rodneykinney, [14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383638467736506439) | 16.3% | 0% | 6.4% | 49.9% | 0.280 |
| 5-6 pairs; 4 pairs with ARM 21, 31, 43; 3 pairs with ARM 21; never edge ARM 0 or 4, except ARM 10 | caycala, [25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1365334546035245227) | 23.0% | 0% | 0% | 32.6% | 0.238 |
| 5+ pairs; 4 pairs with ARM 21, 31, 43; 3 pairs with ARM 21 | Fanti, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069) | 23.5% | 0% | 0% | 32.6% | 0.244 |
| **the card** | this page | 23.0% | 0% | 0% | 32.6% | 0.238 |
| the card with its *if you have time* groups | this page | 31.1% | 0% | 0% | 19.3% | 0.249 |

The card is caycala's chart ([25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1365334546035245227)): never switch edge ARM 0 or 4 (with one exception that I read as ARM 10), 5 or 6 pairs always, 4 pairs with ARM 21, 31 or 43, 3 pairs with ARM 21. It's the best list on the server for 7c8e and the search has nothing to add to it. Fanti's list is the same without the edge-ARM ban, and Daichi said what the ban is worth at 5 pairs: "for 7c8e with 5p, 20/54 has a 0% chance of sub7" ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436036602723045579)), which is exact. The *if you have time* row is Fanti's too: "also 78 4p has a weird silver lining with 11/12/33/41/62 where they're all just slightly worse so consider those if you want" ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436041311110172783)).

```
L' U' L U' L' U2 R   // setup: 7c8e, 5 pairs, ARM 20
R' U2 L U L' U L   // DR in 7, the shortest any 5-pair ARM 20 case has
```

5 or 6 pairs alone ([14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383638467736506439)) misses 6.4% of the 5-movers. All of them are 4 pairs with ARM 21:

```
R' D L R2 F2   // setup: 7c8e, 4 pairs, ARM 21
F2 R2 L' D' R   // DR in 5
```

### 5.5 8c8e and 2c2e

| What you read (8c8e) | Verdict | Share of 8c8e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 8 pairs | **switch** | 0.07% | 100% | 33.3% | 0% | 0% |
| 6 pairs, corner ARM 4 | **switch** | 3.7% | 50.0% | 66.7% | 36.4% | 9.3% |
| 5 pairs, edge ARM 1 or 3 | **switch** | 11.7% | 45.5% | 0% | 36.4% | 37.3% |
| 2 pairs, ARM 42 | **switch** | 2.7% | 32.5% | 0% | 4.5% | 6.2% |
| 4 pairs, ARM 42 | **switch** | 9.8% | 25.2% | 0% | 22.7% | 16.6% |
| 4 pairs, ARM 02, 43, 63 or 82 | if you have time | 5.7% | 22.1% | 0% | 0% | 9.8% |
| 6 pairs, corner ARM not 4 | skip | 3.7% | 14.3% | 0% | 0% | 4.1% |
| 5 pairs, edge ARM 2 | skip | 11.2% | 3.6% | 0% | 0% | 3.1% |
| anything else | skip | 51.5% | 3.4% | 0% | 0% | 13.5% |

The same DRM, one row per policy:

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| 3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs | rodneykinney's tree, [2 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412510225906401403), [2 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412521488577466499) | 20.0% | 0% | 27.3% | 49.2% | 0.348 |
| **the card** | this page | 27.9% | 0% | 0% | 30.6% | 0.291 |
| the card with its *if you have time* groups | this page | 33.6% | 0% | 0% | 20.7% | 0.298 |

The rule on the server is rodneykinney's tree: "The decision tree for 8c8e (all difficulties) actually identifies fake pairs <= 3 as the most important feature" ([2 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412510225906401403)), then edge ARM not 2, with a branch tseitsei89 read out for edge ARM 2 with 6 or more pairs ([2 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412521488577466499)). In 8c8e every corner is bad, so 3 or fewer fake pairs is the same as 5 or more pairs. What the tree leaves out is the even pair counts with ARM 42. 2 pairs with ARM 42 is Daichi's ("8c8e 2 pair 42a is a good switch", [5 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1479211440916271114)), 32.5% sub-7. 4 pairs with ARM 42 is 25.2% and holds 22.7% of 8c8e's 5-movers:

```
R' D U' L' R   // setup: 8c8e, 4 pairs, ARM 42
R' L U D' R   // DR in 5. The tree rule says discard (4 fake pairs)
```

| What you read (2c2e) | Verdict | Share of 2c2e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 1 pair | **switch** | 21.4% | 62.5% | - | 100% | 51.1% |
| 2 pairs and a side pair | **switch** | 0.45% | 100% | - | 0% | 2.1% |
| 0 pairs, 1 side pair, ARM 00 or 11 | **switch** | 7.1% | 68.8% | - | 0% | 23.4% |
| 0 pairs, JZP (ARM 00), no side pair | if you have time | 4.9% | 18.2% | - | 0% | 4.3% |
| anything else | skip | 66.1% | 6.1% | - | 0% | 19.1% |

The same DRM, one row per policy:

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| 1+ pairs | *DRM Subsets Meta* | 23.2% | 0% | 0% | 46.8% | 0.388 |
| **the card** | this page | 29.0% | 0% | 0% | 23.4% | 0.250 |
| the card with its *if you have time* groups | this page | 33.9% | 0% | 0% | 19.1% | 0.263 |

For 2c2e the side pair is the second read: 0 pairs with one side pair and ARM 00 or 11 is 68.8%.

### 5.6 The low DRMs

The *DRM Subsets Meta* table says never for 4c6e, 5c4e, 5c6e and 6c6e, sometimes for 3c4e, and doesn't list 3c6e. On average that's right, they're 5% to 10% sub-7. But they're big DRMs: of the 12 DRMs on this page these six hold 21.8% of the 4-or-less, 42.3% of the 5-movers and 58.9% of the 6-movers. And some people do switch them. Yura Riabov: "Not for every rzp but 5c ones are decent" ([21 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1396980473896505387)). Jay's rule for the 5c ones (2 pairs with ARM 21 or 3 pairs for 5c4e, one pair more for 5c6e, [21 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1396982409290977382)) is graded in appendix A: it costs 0.243 per case on 5c4e against 0.278 for never.

The short ones sit in small pockets. The 5c pockets below are inside Jay's rule. What narrows them is the side pairs. Each row is a pocket worth switching:

| What you read (4c6e) | Verdict | Share of 4c6e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 4 pairs on three edges | **switch** | 0.85% | 74.0% | 88.9% | 33.9% | 9.5% |
| 3 pairs, JZP (ARM 00) | **switch** | 0.31% | 61.1% | 11.1% | 11.3% | 3.0% |
| 3 pairs on three edges, the three bad edges in one layer | **switch** | 0.27% | 62.5% | 0% | 4.8% | 3.6% |
| 3 pairs on three edges, corners 2 and 2 in the layers | **switch** | 2.2% | 25.8% | 0% | 11.3% | 12.7% |

| What you read (3c4e) | Verdict | Share of 3c4e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 2 pairs and a side pair | **switch** | 6.9% | 43.2% | - | 39.1% | 28.9% |
| 2 pairs, no side pair, a fake pair | **switch** | 1.9% | 27.3% | - | 8.7% | 4.7% |
| 1 pair, 2 side pairs | **switch** | 5.7% | 28.1% | - | 17.4% | 16.1% |
| 1 pair, ARM 21, 1 side pair, 2 fake pairs or holes on one R/L face | **switch** | 2.6% | 40.3% | - | 26.1% | 9.0% |
| 1 pair, ARM 21, 1 side pair, the rest | if you have time | 3.5% | 19.5% | - | 4.3% | 7.1% |

| What you read (3c6e) | Verdict | Share of 3c6e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 2 pairs, ARM 21, 1 or 2 fake pairs | **switch** | 4.1% | 31.3% | 100% | 44.4% | 22.7% |
| 2 pairs, ARM 12, 2 fake pairs | **switch** | 1.4% | 38.6% | 0% | 11.1% | 11.4% |
| 2 pairs, ARM 01 | **switch** | 1.5% | 22.9% | 0% | 11.1% | 6.8% |

| What you read (5c4e) | Verdict | Share of 5c4e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 3 pairs, 2+ side pairs | **switch** | 2.2% | 38.3% | 37.5% | 26.1% | 10.0% |
| 2 pairs, ARM 21, 2+ side pairs | **switch** | 2.8% | 32.7% | 37.5% | 20.5% | 11.4% |
| 1 pair, ARM 21, 2+ side pairs, 2+ fake pairs | **switch** | 1.8% | 24.3% | 25.0% | 10.2% | 5.3% |
| 3 pairs, 0 or 1 side pair | if you have time | 3.9% | 21.5% | 0% | 6.8% | 12.2% |

| What you read (5c6e) | Verdict | Share of 5c6e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 4 pairs | **switch** | 3.1% | 37.9% | 37.5% | 30.2% | 17.5% |
| 3 pairs, ARM 21, 3 side pairs | **switch** | 1.2% | 38.3% | 37.5% | 14.6% | 6.2% |
| 2 pairs, ARM 21, 3 side pairs | **switch** | 2.0% | 20.6% | 25.0% | 12.5% | 6.1% |
| 3 pairs, ARM 21, fewer than 3 side pairs | if you have time | 2.1% | 17.4% | 0% | 5.2% | 6.2% |

| What you read (6c6e) | Verdict | Share of 6c6e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 5 or 6 pairs | **switch** | 1.2% | 39.0% | 20.0% | 14.6% | 7.3% |
| 3 pairs, 3 fake pairs, corners 3 and 3 in the layers | **switch** | 1.9% | 34.1% | 40.0% | 20.8% | 10.1% |

A 5c4e that's 4 from DR after the switch:

```
L' F2 D' L   // setup: 5c4e, 3 pairs, 2 side pairs
L' D F2 L   // DR in 4
```

**Is it worth the tracing?** Rough arithmetic, with 5 seconds for a trace (Yura Riabov's pairs + ARM time on 4c4e) and 20 for a switch (caycala's): seconds of tracing and switching per short DR found, if you trace every RZP of the DRM and switch what the card says.

| DRM | Card switches | Sub-7 rate of what it switches | Seconds per short DR found (5 s a trace, 20 s a switch) |
|---|---|---|---|
| 4c4e | 24.9% | 54.8% | 73 |
| 4c2e | 24.8% | 56.3% | 71 |
| 3c2e | 82.1% | 71.2% | 37 |
| 7c8e | 23.0% | 52.6% | 79 |
| 8c8e | 27.9% | 37.9% | 100 |
| 2c2e | 29.0% | 64.6% | 58 |
| 4c6e | 3.6% | 42.8% | 368 |
| 3c4e | 17.1% | 36.0% | 137 |
| 3c6e | 7.0% | 30.9% | 295 |
| 5c4e | 6.8% | 32.3% | 289 |
| 5c6e | 6.3% | 32.3% | 308 |
| 6c6e | 3.0% | 36.0% | 517 |

So a short DR out of 5c4e or 5c6e costs about four times what it costs out of 4c4e, and that's with a 5-second trace, which is too kind for 5 or 6 bad corners. It's something for when the good DRMs have run dry, not a habit. The pockets do catch every 4-or-less of 4c6e, 3c6e, 5c4e and 5c6e.

---

## 6. Reading the card on normal, and how long it takes

You never look at the inverse. Three kinds of piece on the side you're on tell you everything the card asks:

- **the U/D edges sitting in the E slice** (white or yellow edges in the middle layer). On the inverse they're the bad edges in the U/D layers;
- **the misoriented corners** (no white or yellow on the U/D face). For each one, the colour it shows on the U/D face, and its two side stickers;
- **the E-slice edges that are out of the slice**. On the inverse they're the holes.

**The reads.** Each one is tagged with what it takes: *at a glance* (a count of colours), or *by tracing* (matching a few pieces against each other). Nothing here needs a search. The count of section 7 does.

- *Pairs*, by tracing (wen's tracing, [*Hitchhiker's Guide to DR*](https://docs.google.com/document/d/1E_5wSKvQFXXZY4f3xLM76qMUrVGp9Pe7vgotS0X-T4U)): "look at one of the edges in the E slice that don't belong there, then look at a misoriented corner, if the 2 stickers on the corner that are touching the E slice match with that E slice edge, then that's a pair on inverse". Do it edge by edge and you know for free whether 2 pairs are on one edge or on two.
- *Fake pairs*, free with the pair trace: a misoriented corner that has both colours of the edge but shows the edge's side colour on the U/D face. They're the near misses.
- *Edge ARM*, at a glance: how many of those U/D edges have green or blue as their other colour.
- *Corner ARM*, at a glance: how many misoriented corners show red or orange on the U/D face ("count the number of R/L stickers on the U/D face", *DR - 4c4e Theory*).
- *Corner case*, by tracing (rodneykinney's flow chart, same doc), for four misoriented corners with corner ARM 2: if some colour is on exactly 1 or 3 of the four corners it's 4b. If not, and two of the corners have two colours in common, 4a. Otherwise 4d.
- *4a in two columns*, by tracing: the four corners are two twins. Each twin is a white corner and a yellow corner with the same two other colours.
- *Side pairs*, by tracing (rodneykinney, *Domino Setup Theory*: "To predict side pairs on the inverse, look at the bad edges on the top/bottom faces. If there is also a bad corner showing the same color on the U/D face, then the inverse will have a side pair."). As checked: for each E-slice edge that's out of the slice, count the misoriented corners that carry both its colours and show the green or blue one on the U/D face.
- *Holes on one R/L face*, at a glance: the two E-slice edges that are out of the slice share red or orange. Sharing green or blue is one F/B face, sharing nothing is diagonal.
- *Corners 2 and 2*, at a glance: two misoriented corners are white, two are yellow.
- *Split pair*, by tracing: a U/D edge in the E slice and a misoriented corner with the same white or yellow that doesn't carry the edge's other colour. It counts when the edge has green or blue and the corner shows red or orange, or the other way round.

**The check.** Each read done on normal, by colour only, against the value on the inverse, on uniformly random EO-solved cubes (5,000 of each of the 12 DRMs and 5,000 with no DRM fixed):

| Read | Random cubes checked | Read on normal = the inverse's value |
|---|---|---|
| pairs | 65,000 | 65,000 |
| edges with a pair (two edges or a bar) | 65,000 | 65,000 |
| fake pairs | 65,000 | 65,000 |
| side pairs | 65,000 | 65,000 |
| corner ARM | 65,000 | 65,000 |
| edge ARM | 65,000 | 65,000 |
| corner case (4 bad corners) | 15,956 | 15,956 |
| corners in columns | 65,000 | 65,000 |
| where the two holes are (2 holes) | 16,734 | 16,734 |
| corners per layer | 65,000 | 65,000 |
| bad edges in one layer | 49,692 | 49,692 |
| split pairs | 65,000 | 65,000 |

**One attempt, start to finish.**

```
B2 D' L2 F2 U' F2 D2 B2 R2 D' L2 F2 U R2 U L' B2 U' B F2 L F2 R
R B' R2 L' B   // EO on F/B, and it's already 4c4e
```

What's on the cube now:

- U/D edges in the E slice: white-blue, white-orange.
- Misoriented corners: white-green-orange showing orange; yellow-blue-red showing red; yellow-blue-orange showing blue; white-blue-orange showing blue.
- E-slice edges out of the slice: blue-orange, green-orange.

Pairs: white-blue needs a corner with white and blue on its sides, and there's none. White-orange has one (the white-blue-orange corner, showing blue). 1 pair. Two corners have an edge's colours the wrong way round, so 2 fake pairs. ARM: two corners show red or orange, one edge has blue, so 21. Corners: white is on two, yellow on two, green on one. One colour on exactly one corner: 4b. Side pairs: both blue-orange corners show blue, so 2. The card says switch (1 pair, ARM 21, 4b corners, 0 or 2 side pairs: 50.4%). The pairs rule says discard.

```
(R' B2 U2 R D L)   // DR on the inverse, 6 moves: 11 to DR
```

**How long.** I haven't timed anyone, so here's what the card asks for and what people have said the pieces of it take.

- *The pair trace is the base.* Everyone who switches by pairs does it already.
- *ARM is the big addition, and people differ on it.* With pairs it takes Yura Riabov "Like 5 seconds", "±2", "That's for 4c4e btw, for 7c8e it's longer" ([17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417786183135526954), [17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417786220435738704), [17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417787071405490237)), and "Arm is very fast to check for me", "It's like, just look at the cube" ([17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417787132914696302), [17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417787214472941661)). Daichi: "7c8e is probably just double my 4c4e times" ([17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418007108577923226)). In the same exchange Dunni says "I take longer to check only for pairs" ([17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417786899900268594)) and dropped ARM: "Saves me from misrecognizing arm-2c1e, which definitely did not happen, ever" ([17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417787480404393984)). And wen: "I don't even count ARM for 4c4e tbh" ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418234619014283346)). So if you don't read ARM now, the card adds it on every 1-pair case, 44.2% of your 4c4e RZPs.
- *What the card adds on 4c4e*, by how often you need it. It comes to 0.75 extra looks per RZP on average:

| Extra look (4c4e) | When | Share of 4c4e cases |
|---|---|---|
| none: the pair trace settles it | 3 or 4 pairs, 2 pairs on two edges, 0 pairs with a fake pair | 42.2% |
| the two E-slice edges out of the slice: do they share red or orange? | 2 pairs on one edge | 10.5% |
| ARM | 1 pair | 44.2% |
| the corner case | 1 pair and ARM 21 | 9.1% |
| the side pairs | 1 pair, ARM 21 and 4b corners | 5.4% |
| are the corners two twins? | 1 pair, ARM 21 and 4a corners | 2.9% |
| white and yellow on the four corners | 0 pairs and no fake pair | 3.1% |

- *Nothing on the card needs a place on the inverse.* Every read is of the kind *does this piece have these colours, and which one is on top*. That's the difference with a full NISS trace, where you work out where each piece goes.
- *The corner case is the slowest read on the card*, and it's only asked for on 1 pair + ARM 21. People check corners on 1 pair today. tseitsei89: "I often check that if I trace 1 pair. It is usually very fast to see that it is NOT d  corners since if you see 3 of any one color or you see any 2 corners that share more than 1 color you instantly know it wont be d corners." ([17 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1417807431786037319)). Evan, on checking the corner type with 1 pair + ARM 21: "I only started to recently but i think it's been beneficial" ([18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418286352360804442)). With ARM 21 the corner ARM is 2, so the flow chart is two questions.
- *More reads, more chances to misread.* Dunni's ARM 21 is the example. I have no numbers on how often a read goes wrong, and a wrong read costs what a miss or a wasted switch costs.

If you only take one thing from the card, take 1 pair + ARM 21 with 4d corners, or with 4b corners and 0 or 2 side pairs. Those two rows are worth the most. The 2-pair split is what pays for them in switches.

---

## 7. Two bars, evaluated

**What it is.** A 4c4e is one R or L turn from DR when each layer has a bar and both holes are on that face. The *half turns to two bars* is the fewest half turns (R2, L2, F2, B2) that get there, with U and D turns free. The two bars as the target are in Andrew's 2019 video and in rodneykinney's *DR - 4c4e Theory*. The count is exact for every case and proved in Lean.

**What it's worth.** Each row is a value of the count.

| Half turns to two bars | Share of 4c4e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|
| 0 | 0.05% | 100% | 5.5% | 0% | 0% |
| 1 | 0.98% | 100% | 56.1% | 12.7% | 0.46% |
| 2 | 13.2% | 72.1% | 38.4% | 71.2% | 44.8% |
| 3 | 51.0% | 16.0% | 0% | 15.9% | 50.9% |
| 4 | 33.8% | 1.7% | 0% | 0.16% | 3.8% |
| 5 | 0.99% | 0% | 0% | 0% | 0% |

That's a clean scale. 0 to 2 holds every case of 4 or less and 83.9% of the 5-movers, at 74.1% sub-7. As a switch rule on this page's yardstick, one row per policy:

| Policy (4c4e) | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|
| 2+ pairs | 26.0% | 8.0% | 20.4% | 42.8% | 0.413 |
| pairs + ARM (Fanti) | 35.2% | 1.4% | 5.8% | 27.0% | 0.345 |
| 2 half turns or fewer | 14.2% | 0% | 16.1% | 54.8% | 0.332 |
| 3 half turns or fewer | 65.2% | 0% | 0.16% | 3.8% | 0.483 |
| the card | 24.9% | 0% | 8.8% | 35.4% | 0.299 |
| the card, or 2 half turns or fewer | 27.7% | 0% | 3.2% | 28.5% | 0.266 |

So the count cut at 2 beats every list on the server on cost, with far fewer switches. It finds a lot of what pairs miss: of the cases with 0 or 1 pair, 1,248 are at 2 or fewer (1.8% of 4c4e) and 74.2% of them are sub-7. That's all 46 of the 4-or-less that 2+ pairs misses, 248 of the 508 5-movers and 632 of the 4,500 6-movers. It also holds 140 of the 220 5-movers the card misses, which is why the last row is the best of the table.

Where it's weak is the 6-movers: more than half of them are at 3, and a 3 is 16.0% sub-7 on average. The count has nothing more to say about which 3s are the good ones. Cut at 3 it misses almost nothing and switches two thirds of 4c4e.

```
L' D F2 D' L   // setup: 4c4e, 1 pair, 3 half turns to two bars
L' D F2 D' L   // DR in 5, with two quarter turns of L and no stop at two bars
```

```
L' D' L2 D B2 D' U'   // setup: 4c4e, 2 pairs, 2 half turns to two bars
U D B2 D' L2 D L   // DR in 7: the two half turns need four U/D turns around them
```

**Where the count sits against pairs.** Each row is a pair count:

| Pairs (4c4e) | Cases | With 2 half turns or fewer | With 3 | With 4 or 5 | Sub-7 cases | Of them at 2 or fewer | Of them at 3 |
|---|---|---|---|---|---|---|---|
| 0 | 21,000 | 0.46% | 23.1% | 76.5% | 910 | 8.6% | 64.2% |
| 1 | 31,200 | 3.7% | 70.8% | 25.5% | 4,144 | 20.5% | 76.8% |
| 2 | 15,840 | 42.4% | 54.2% | 3.3% | 6,508 | 72.0% | 27.2% |
| 3 | 2,400 | 80.0% | 20.0% | 0% | 1,896 | 89.0% | 11.0% |
| 4 | 120 | 100% | 0% | 0% | 118 | 100% | 0% |

**What it takes to read.** This is the problem.

- *It needs places, not colours.* The count is made from where the four bad corners, the two bad edges and the two holes sit on the inverse, layer by layer, and which way each corner points. That's the full NISS trace of all eight pieces. The card's reads are colour matches on the same pieces.
- *Then it needs a search.* With 3 or 4 pairs there's a formula. With 2 pairs you have to try one half turn ahead, in your head, on a cube you can't see. With 0 or 1 pair there's no hand rule that tells a 2 from a 3, and those 1,248 cases are where the count would pay most.
- *What people have said about tracing 4c4e in full.* Zagros thinks it's the right idea: "I dont do this but ngl I am super convinced that more niss tracing is clearly optimal, I think the optimal system is 100% niss tracing 4c4e, and I think if someone were to commit to doing this, they would probably get good at it pretty fast" ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436040007654838402)). Then tried it: "btw i talked here earlier about niss tracing 4c4e rzp cases and I did it for like four solves and gave up. i still have hope in the concept, but I quickly found that I'm just not good enough at rzp->dr to be able to do it effectively. I niss trace and then I just don't know if it has a 6 move DR or not. I need to actually do a few moves to check" ([19 Jan 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1462981640702656729)), and "Still believe it is optimal, especially for stuff like 21 1 pair that is borderline on if I want to switch, but it is no help if I can't actually tell how many moves to DR after niss tracing half the time" ([19 Jan 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1462982368435507307)). So the trace was doable and the judging wasn't. A count is a way of judging, so this cuts both ways: it's the thing Zagros was missing, and it's four solves by one person.
- *And time.* caycala: "I just timed me switching an rzp and going back to solved cube, and it took ~20 seconds including some time to look specifically at the rzp. So you would have to be able to niss trace in that time (definitely doable for 4c4e and less, but also consider extra time for E slice) and also be able to determine if the case is good." ([16 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1395178075649478797)), and the conclusion: "tldr i dont think it’s worth it + it is much more mistake prone" ([16 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1395178375114653788)).

So: on what it catches, the count deserves a place on top of the card. On what it takes, nobody has shown a full trace plus the count done in a few seconds, and the two people who wrote about full tracing of 4c4e either stopped or advised against it. I can't make the case that it's fast enough, so it's not on the card. If you can do it, the rule is simple: *2 or fewer, switch*, whatever the card says.

**On a cube you can see** the count costs nothing. After the switch, or for an RZP on the side you're on, the bars and the holes are in front of you. Then the first table is the read: 2 or fewer is 74.1%, 4 or 5 is 1.7% and under.

**How the count splits the card** (**computer only**). Each row is a group of the card:

| What you read (4c4e) | Card says | 2 or fewer: share of the group | 2 or fewer: sub-7 rate | 3: share of the group | 3: sub-7 rate | 4 or 5: share of the group |
|---|---|---|---|---|---|---|
| 3 or 4 pairs | **switch** | 81.0% | 88.5% | 19.0% | 43.3% | 0% |
| 2 pairs on two edges | **switch** | 54.9% | 76.2% | 44.0% | 27.1% | 1.1% |
| 2 pairs on one edge (a bar), holes on one R/L face | **switch** | 28.4% | 95.5% | 65.8% | 24.3% | 5.8% |
| 1 pair, ARM 21, 4d corners | **switch** | 66.7% | 91.7% | 33.3% | 83.3% | 0% |
| 1 pair, ARM 21, 4b corners, 0 or 2 side pairs | **switch** | 0% | - | 100% | 50.4% | 0% |
| 1 pair, ARM 21, 4a corners in two columns | **switch** | 18.2% | 66.7% | 63.6% | 35.7% | 18.2% |
| 0 pairs, no fake pairs, corners 2 and 2 in the layers | **switch** | 16.7% | 81.3% | 66.7% | 12.5% | 16.7% |
| 2 pairs on one edge (a bar), holes not on one R/L face | if you have time | 28.4% | 35.8% | 65.8% | 11.5% | 5.8% |
| 1 pair, not ARM 21, 2+ side pairs, not 4b corners | if you have time | 3.3% | 70.0% | 67.5% | 23.5% | 29.1% |
| 1 pair, ARM 21, 4a corners not in two columns | skip | 0% | - | 90.0% | 2.8% | 10.0% |
| 1 pair, ARM 21, 4b corners, exactly 1 side pair | skip | 0% | - | 100% | 5.6% | 0% |
| 1 pair, anything else | skip | 2.1% | 61.5% | 66.5% | 6.7% | 31.5% |
| 0 pairs, anything else | skip | 0% | - | 21.9% | 12.0% | 78.1% |

Two things in there. A bar is at 2 or fewer in 28.4% of its cases wherever the holes are, so the holes are not the count in disguise: at the same count, a bar with the holes on one R/L face is 95.5% and one without is 35.8%. And 1 pair + ARM 21 with 4b corners is always a 3, good or bad, so there the side pairs see something the count doesn't.

---

## 8. What didn't help

Briefly, on 4c4e unless said otherwise. *Cost per case* of the best rule that uses the pair count and the read. Pairs alone is 0.413, the card 0.299. Each row is a read:

| Read added to the pair count (4c4e) | Cost per case, best rule on pairs + this read | Switched | Missed: 5-movers | Missed: 6-movers |
|---|---|---|---|---|
| (pairs alone) | 0.413 | 26.0% | 20.4% | 42.8% |
| side turns (needs the whole trace) | 0.317 | 18.1% | 13.2% | 46.4% |
| half turns to two bars (needs the whole trace) | 0.327 | 14.9% | 15.8% | 52.9% |
| ARM (both digits) | 0.345 | 35.2% | 5.8% | 27.0% |
| corner case with its suffix | 0.373 | 25.2% | 17.2% | 41.5% |
| side pairs | 0.387 | 36.2% | 9.8% | 29.9% |
| 4a corners one U/D turn from 4d (wen) | 0.400 | 27.7% | 15.3% | 40.9% |
| corners in columns | 0.400 | 30.0% | 15.3% | 37.1% |
| split pairs | 0.403 | 26.2% | 19.5% | 42.4% |
| moves to AR (computer only) | 0.404 | 26.2% | 19.7% | 42.4% |
| corner ARM | 0.408 | 43.3% | 4.0% | 24.8% |
| moves to orient the corners alone (computer only) | 0.410 | 28.9% | 16.6% | 39.8% |
| corner moves + missing pairs (computer only) | 0.410 | 28.9% | 16.6% | 39.8% |
| fake pairs | 0.412 | 26.7% | 20.1% | 41.7% |
| corners per layer | 0.412 | 25.2% | 20.8% | 43.9% |
| AR bars (rodneykinney) | 0.413 | 26.1% | 20.3% | 42.8% |
| edge ARM | 0.413 | 26.0% | 20.4% | 42.8% |
| paired edges (bar or two edges) | 0.413 | 26.0% | 20.4% | 42.8% |
| where the two holes are | 0.413 | 26.0% | 20.4% | 42.8% |
| bad edges in one layer | 0.413 | 26.0% | 20.4% | 42.8% |
| corners not in a pair | 0.413 | 26.0% | 20.4% | 42.8% |
| a pair and a fake pair on one edge | 0.413 | 26.0% | 20.4% | 42.8% |

*Side turns* in that table are the turns of R, L, F and B in the DR with the fewest of them, U and D turns free. Like the half-turn count they need the whole trace. *AR bars* are rodneykinney's: an edge with the two corners next to it each in AR or paired with it ([5 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1402488061203320864)). *Moves to AR* is the fewest moves to a JZP state.

- **The bar and the holes, one at a time.** Knowing only that 2 pairs sit on one edge changes nothing: a bar is 26.6% sub-7 overall, still a switch. Knowing only where the holes are changes nothing either. It's the two together that split 2 pairs.
- **A new kind of pair.** I took every way two bad pieces can sit relative to each other (corner and edge, corner and hole, corner and corner, edge and edge, edge and hole, hole and hole: 60 classes up to the symmetries that keep the EO and DR axes; top pairs, fake pairs and side pairs are three of them) and asked which one, counted next to pairs, helps most. The best is a corner-corner relation that just restates the corner case (0.380), then side pairs (0.387). There's no fourth pair hiding.
- **Points systems.** rodneykinney's old estimate 12 − 2 × top pairs − 2 × side pairs ([*Domino Setup Theory*](https://docs.google.com/document/d/1Z3O8BY1LbAMF6m55ufXtSdtBVwSJpMArtRrDT-p_CwM)), which switches at 3 pairs of any kind: 0.464. A top pair as 2 points and a side pair as 1, switch at 4: 0.389. The best weighted sum of pairs, side pairs, fake pairs, ARM, corner case, holes and layers (22 terms, fitted to these prices): 0.320. A sum can't do it because the reads don't add up: one side pair is worse than none for 4b corners.
- **Corner-only counts.** The moves to orient the corners alone, and that number plus the missing pairs (the bones of the lower bound in *DR - 4c4e Theory*, used as a switch rule at 6): 0.569. It's a bound for finding the DR, not a predictor.
- **Corners not in a pair** (Zagros's question, [5 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1479199955444043899)): the same thing as pairs once you know the DRM.
- **Fake pairs, on 4c4e with at least one pair**, and **AR bars**: nothing. Fake pairs matter with 0 pairs (the card), for 3c2e (wen's rule), and in 3c6e and 6c6e.
- **The bad edges' layers.** Both bad edges in one layer splits 1 pair + ARM 21 with 4a corners into 30.3% and 7.5%. Evan's stacked corners do it better (34.8% and 2.5%), so that's what the card uses.
- **wen's "one U/D turn away from 4d"**: a little, less than ARM does for the same effort.
- **Leading with something other than pairs.** A tree that's free to split on any quick read first still splits on pairs first (2 or more against fewer), then ARM 21. With 8 leaves it costs 0.315, with 16 0.303.
- **Bigger lists.** 40 leaves: 0.267. The card is where the curve flattens.

---

## 9. How far a rule can go

**Computer only.** For a set of reads, the best possible rule switches exactly the cells (combinations of values) that are worth it at the prices of section 3. No rule on those reads can cost less. These are lookups in hundreds or thousands of cells, so they're ceilings to measure a card against, not cards.

| Reads the rule may use (4c4e) | Cells | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| pairs | 5 | 26.0% | 8.0% | 20.4% | 42.8% | 0.413 |
| pairs and ARM | 49 | 35.2% | 1.4% | 5.8% | 27.0% | 0.345 |
| pairs and corner case | 28 | 25.2% | 2.4% | 17.2% | 41.5% | 0.373 |
| pairs and side pairs | 23 | 36.2% | 2.1% | 9.8% | 29.9% | 0.387 |
| pairs, ARM, corner case and side pairs | 206 | 30.3% | 0% | 3.9% | 27.0% | 0.285 |
| every quick read together | 3,757 | 24.4% | 0% | 0% | 9.5% | 0.109 |
| **the card** | 13 groups | 24.9% | 0% | 8.8% | 35.4% | 0.299 |
| the exact DR length | 70,560 | 19.2% | 0% | 0% | 0% | 0 |

Three things in there.

- *Pairs + ARM at its best is Fanti's list.* Same cells, same numbers.
- *The card beats every two-read ceiling* and sits a little above the four-read one, with 13 groups against 206 cells.
- *The quick reads together know almost everything about the short cases.* All of them at once miss no 5-mover and 9.5% of the 6-movers at 24.4% switched. That's a table of 3,757 cells. The gap between it and the card is what a much better memory, or a trainer, could still get.

**Which second read helps most**, per DRM. Cost per case of the best rule on pairs and one more read, the best one in bold:

| DRM | Pairs alone | Pairs + ARM | Pairs + corner case | Pairs + side pairs | Pairs + fake pairs |
|---|---|---|---|---|---|
| 4c4e | 0.413 | **0.345** | 0.373 | 0.387 | 0.412 |
| 4c2e | 0.352 | 0.326 | 0.325 | **0.280** | 0.352 |
| 3c2e | 0.384 | 0.384 | - | 0.384 | 0.384 |
| 7c8e | 0.280 | **0.237** | - | 0.278 | 0.280 |
| 8c8e | 0.435 | **0.284** | - | 0.390 | 0.435 |
| 2c2e | 0.388 | 0.335 | - | **0.326** | 0.388 |
| 4c6e | 0.148 | **0.132** | 0.146 | 0.141 | 0.145 |
| 3c4e | 0.292 | 0.285 | - | **0.267** | 0.287 |
| 3c6e | 0.195 | **0.156** | - | 0.194 | 0.168 |
| 5c4e | 0.250 | 0.240 | - | **0.232** | 0.250 |
| 5c6e | 0.202 | **0.186** | - | 0.197 | 0.202 |
| 6c6e | 0.195 | 0.192 | - | 0.194 | **0.188** |

ARM for 4c4e, 7c8e and 8c8e, side pairs for 4c2e and 2c2e. That's where the server ended up too.

The same ceilings for 4c2e and 7c8e:

| Reads the rule may use (4c2e) | Cells | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| pairs | 3 | 42.9% | 0% | 2.1% | 17.1% | 0.352 |
| pairs and ARM | 24 | 38.9% | 0% | 0% | 20.2% | 0.326 |
| pairs and corner case | 20 | 32.5% | 0% | 2.1% | 29.5% | 0.325 |
| pairs and side pairs | 9 | 22.3% | 0% | 2.1% | 38.8% | 0.280 |
| pairs, ARM, corner case and side pairs | 98 | 24.9% | 0% | 0% | 26.7% | 0.227 |
| every quick read together | 370 | 25.3% | 0% | 0% | 20.2% | 0.190 |
| **the card** | 8 groups | 24.8% | 0% | 0% | 31.0% | 0.251 |
| the exact DR length | 13,440 | 18.7% | 0% | 0% | 0% | 0 |

| Reads the rule may use (7c8e) | Cells | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| pairs | 6 | 16.3% | 0% | 6.4% | 49.9% | 0.280 |
| pairs and ARM | 92 | 22.0% | 0% | 0% | 34.2% | 0.237 |
| pairs and side pairs | 36 | 21.0% | 0% | 0% | 43.7% | 0.278 |
| every quick read together | 368 | 22.1% | 0% | 0% | 24.7% | 0.188 |
| **the card** | 8 groups | 23.0% | 0% | 0% | 32.6% | 0.238 |
| the exact DR length | 23,520 | 16.4% | 0% | 0% | 0% | 0 |

---

## 10. Other RZP lengths, real attempts, other weights

**After a 4-move or a 6-move RZP.** The target moves: a DR in 7 is enough after 4, and you need 5 after 6. The same groups, with the share that makes the target and the verdict at the same prices (a just-good-enough DR at 3, one move shorter at 9, shorter still at 27):

| What you read (4c4e) | 4-move RZP: DR in 7 or less | Verdict at 4 | 5-move RZP: DR in 6 or less | Verdict at 5 | 6-move RZP: DR in 5 or less | Verdict at 6 |
|---|---|---|---|---|---|---|
| 3 or 4 pairs | 99.4% | **switch** | 79.9% | **switch** | 33.9% | **switch** |
| 2 pairs on two edges | 95.1% | **switch** | 53.9% | **switch** | 15.9% | skip |
| 2 pairs on one edge (a bar), holes on one R/L face | 87.4% | **switch** | 43.7% | **switch** | 10.6% | skip |
| 1 pair, ARM 21, 4d corners | 100% | **switch** | 88.9% | **switch** | 22.2% | **switch** |
| 1 pair, ARM 21, 4b corners, 0 or 2 side pairs | 90.3% | **switch** | 50.4% | **switch** | 8.1% | skip |
| 1 pair, ARM 21, 4a corners in two columns | 80.3% | **switch** | 34.8% | **switch** | 6.1% | skip |
| 0 pairs, no fake pairs, corners 2 and 2 in the layers | 66.7% | **switch** | 21.9% | **switch** | 6.6% | skip |
| 2 pairs on one edge (a bar), holes not on one R/L face | 81.5% | **switch** | 18.1% | skip | 1.1% | skip |
| 1 pair, not ARM 21, 2+ side pairs, not 4b corners | 69.5% | **switch** | 19.2% | skip | 0.99% | skip |
| 1 pair, ARM 21, 4a corners not in two columns | 68.3% | **switch** | 2.5% | skip | 0% | skip |
| 1 pair, ARM 21, 4b corners, exactly 1 side pair | 76.7% | **switch** | 5.6% | skip | 1.3% | skip |
| 1 pair, anything else | 49.7% | **switch** | 6.1% | skip | 0.28% | skip |
| 0 pairs, anything else | 30.7% | **switch** | 3.8% | skip | 0.18% | skip |

- *4-move RZP*: every row is a switch at these prices, even 0 pairs (30.7% of the leftovers have a DR in 7 or less). That's "It seems like you should pretty much always switch a 4 move DR-4c4e." (Zagros, [7 Jul 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1524175174507692245)) and "yeah 4 is almost always a switch on normal scramble" (tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409604711069388970)). If you want to trim, trim from the bottom: Daichi's 4-move list ([7 Jul 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1524192731432353853)) drops a few 0-pair and 1-pair ARMs.
- *6-move RZP*: 3 or 4 pairs, and 1 pair with ARM 21 and 4d corners. 2 pairs on two edges is down to 15.9%.

The other DRMs are in appendix A.

**On real attempts.** The card's numbers on the 8,427,192 real 5-move attempts, next to the exact ones. It's a sample of 6,000 scrambles. Even if every attempt of a scramble counted as one, a standard error on a share would be about 0.6 points.

| DRM | Real 5-move attempts | Switched: exact | Switched: real attempts | Missed 5-movers: exact | Missed 5-movers: real | Missed 6-movers: exact | Missed 6-movers: real |
|---|---|---|---|---|---|---|---|
| 4c4e | 560,822 | 24.9% | 24.9% | 8.8% | 8.6% | 35.4% | 35.1% |
| 4c2e | 112,330 | 24.8% | 25.1% | 0% | 0% | 31.0% | 30.7% |
| 3c2e | 31,340 | 82.1% | 82.0% | 0% | 0% | 7.4% | 7.9% |
| 7c8e | 189,338 | 23.0% | 22.8% | 0% | 0% | 32.6% | 33.0% |

Same thing. For the four DRMs together the cards switch 26.5% of the real attempts and miss 0%, 5.2% and 31.6%; the pairs policy switches 27.6% and misses 4.2%, 12.5% and 36.4%.

**Other prices.** Cost per case on 4c4e when a declined 6-mover costs 2, 3 or 5 wasted switches and each move shorter counts 2, 3 or 4.5 times as much. The page uses 3 and 3.

| A declined 6-mover costs | Each move shorter multiplies by | Pairs only | Pairs + corner case | Pairs + ARM | The card | The card, wider |
|---|---|---|---|---|---|---|
| 2 wasted switches | 2 | 0.301 | 0.290 | 0.292 | 0.231 | 0.289 |
| 2 wasted switches | 3 | 0.322 | 0.304 | 0.297 | 0.237 | 0.292 |
| 2 wasted switches | 4.5 | 0.358 | 0.326 | 0.306 | 0.246 | 0.297 |
| 3 wasted switches | 2 | 0.382 | 0.361 | 0.337 | 0.290 | 0.321 |
| 3 wasted switches | 3 | 0.413 | 0.381 | 0.345 | 0.299 | 0.326 |
| 3 wasted switches | 4.5 | 0.468 | 0.414 | 0.358 | 0.313 | 0.333 |
| 5 wasted switches | 2 | 0.543 | 0.503 | 0.426 | 0.408 | 0.384 |
| 5 wasted switches | 3 | 0.596 | 0.537 | 0.439 | 0.423 | 0.392 |
| 5 wasted switches | 4.5 | 0.686 | 0.592 | 0.461 | 0.447 | 0.405 |

The card is the cheapest in every row but the last three, where a 6-mover at 5 wasted switches makes switching more the right call and the wider card takes over. Only one verdict on the card flips anywhere in that grid: with a 6-mover at 2 and a factor of 2, the 0-pair group drops to *if you have time*.

---

## 11. The claims, checked

Things people said about these rules, with the exact numbers. The one that doesn't hold is on the [errata](errata.html) page.

| Who and what | Exact |
|---|---|
| tseitsei89, [25 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1409579685716689018): "4c4e: >1 pairs = switch (43%), 1 pair and d corners = switch (44%)" | 2+ pairs is 46.4% sub-7 (the 43% is rodneykinney's findable sub-7). 1 pair with 4d corners is 44.4%. |
| Evan, [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418247728328212585): "4d+1 is extremely good for AR-21 (~90% sub-7) but 0% for other AR" | 88.9% with ARM 21, 0% with ARM 20 or 22. |
| Evan, [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418283868007436308), on 1 pair + ARM 21: "b corners - 29%", "d corners - 89%", "a corners - ~34% if corners are stacked, < 5% otherwise" | All three right: 4b 28.8%, 4d 88.9%, 4a in two columns 34.8% and 2.5% otherwise. |
| rodneykinney, [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383075044682633366), for 0 pairs: "To catch this case, you can switch 4a-0 and 4d-2, but only if there also are no fake pairs" | Those are 120 cases at 23.3%, with 6 of the 14 zero-pair cases of 4 or less. No fake pairs with the corners 2 and 2, any corner case, is 576 cases at 21.9% with all 14. |
| rodneykinney, [21 Jun 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1385965585833267210): "Zero pairs + zero pseudo-pairs would be a likely setup to F2 B2 R. But I don't have stats that include the pseudo-pair count." | The stats: 0 pairs and 0 fake pairs is 2,160 cases at 13.2%, against 4.3% for 0 pairs overall. |
| rodneykinney, [13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383069263530692730): "2 pairs: Switch unless 4b-0" | 2 pairs with 4b-0 corners is 15.3% sub-7, a skip at these prices too. 960 of its 1,728 cases are bars with the holes off the R/L faces, so the card's *if you have time* row has most of it. |
| compLex, [11 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404500827628113920): "you only need to actually learn to spot 4d (the only case worth switching 1 pair) and 4b (the only case not worth switching 2 pairs)" | By pairs and corner case alone the 4d half holds: 1 pair is 44.4% with 4d and 17.0% or less otherwise. The 4b half holds for 4b-0 (15.3% with 2 pairs), not for 4b-2 (51.9%). |
| Fanti, *armpairs_1.txt* ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069)): "35.2% switches", "42.6% sub-7 switch success (15.0% total)", "4.3% of cases will be discarded with sub-7" | 35.2%, 42.6%, 4.2% with the EO kept. |
| Yura Riabov, [22 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1397110208685146265): "From my experience with pairs 1 bar is worse than 2 pairs for most arms" | True in 9 of the 9 ARMs that have both. Overall a bar is 26.6%, two edges 53.9%. |
| wen, [12 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1471458126539526323), on the 3c2e rule: "At the very least you will never miss a 5 mover by doing this" | True. The skipped group has 112 6-movers, no 5-mover, no 4-mover. |
| Daichi, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436036602723045579): "for 7c8e with 5p, 20/54 has a 0% chance of sub7" | True, 48 cases each, none under 7. |
| Daichi, same message: "JZP with b corners is way better than a corners" (4c2e, 0 pairs) | 66.7% against 16.7%. |
| Daichi, [5 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1479211440916271114): "8c8e 2 pair 42a is a good switch" | 2 pairs with ARM 42 is 32.5% sub-7, on the card. |
| Jay, [21 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1396982409290977382): "iirc, need 2 pairs + ar21 for 5c4e to be good (3 pairs if it's another arm), same for 5c6e but need one extra pair" | As a rule it switches 11.7% of 5c4e at 24.5% and 6.4% of 5c6e at 31.1%. With 2 or more side pairs on top the 5c4e groups are 38.3% and 32.7%. |
| Zagros, [7 Jul 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1524175174507692245): "It seems like you should pretty much always switch a 4 move DR-4c4e." | 59.4% of 4c4e is 7 or less, and every group of the card is a switch at 4. |

---

## 12. What this does not cover

- **Whether you find the DR.** A case counts as good if a DR in 6 exists. A 6-mover through three half turns is harder to see than `U' R` with setup, and I haven't weighed that in. rodneykinney's *findable* is the server's attempt at it.
- **What the DR is worth after.** A short DR into a bad DR case isn't worth what its length says. That's [*Judging a DR by hand*](../judging-a-dr/).
- **The other DR axis and the EO's last move.** One EO axis, one DR axis, linear. Both options help a little after a switch (the EO's last move either way: about 2 points of sub-7 on 4c4e; the other DR axis: about 6), and neither changes which groups are better.
- **Human timing and misreads.** Section 6 is an argument from what the reads are and what people have said they take. Nobody has timed this card or counted how often a read goes wrong. If you do, tell me.
- **The twist split.** How many corners are twisted clockwise and how many counter-clockwise isn't a read on the cards. It matters for 8c8e: with 4 and 4 it's 15.2% sub-7, with 7 and 1 it's 11.4% and nothing under 6 moves.
- **DRMs outside the 12.** 6c4e, 7c6e and the rest are not carded.

---

## Appendix A: full tables

**Every current policy, per DRM.** One row per DRM: the pairs policy, the best list I found on the server, and the card, each with its *cost per case* at the prices of section 3.

| DRM | Pairs policy | Its cost per case | Best list on the server | Its cost per case | The card's cost per case |
|---|---|---|---|---|---|
| 4c4e | 2+ pairs | 0.413 | 2+ pairs; 1 pair with ARM 21; 0 pairs with JZP or ARM 42 | 0.345 | 0.299 |
| 4c2e | 1.5+ pairs (2 side pairs = 1 pair) | 0.280 | the same | 0.280 | 0.251 |
| 3c2e | always | 0.384 | a pair, a fake pair or a split pair | 0.330 | 0.330 |
| 7c8e | 5+ pairs, counting edge ARM under 2 as a pair | 0.259 | 5-6 pairs; 4 pairs with ARM 21, 31, 43; 3 pairs with ARM 21; never edge ARM 0 or 4, except ARM 10 | 0.238 | 0.238 |
| 8c8e | 3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs | 0.348 | the same | 0.348 | 0.291 |
| 2c2e | 1+ pairs | 0.388 | the same | 0.388 | 0.250 |
| 4c6e | never | 0.189 | 4 pairs or JZP | 0.135 | 0.125 |
| 3c4e | 2+ pairs | 0.292 | the same | 0.292 | 0.228 |
| 3c6e | never | 0.195 | 3 pairs with ARM 00; 2 pairs with ARM 21 | 0.158 | 0.140 |
| 5c4e | never | 0.278 | 2 pairs with ARM 21, or 3+ pairs | 0.243 | 0.216 |
| 5c6e | never | 0.233 | 3 pairs with ARM 21, or 4+ pairs | 0.190 | 0.181 |
| 6c6e | never | 0.208 | the same | 0.208 | 0.179 |

**The cards after a 4-move and a 6-move RZP.** One table per DRM. Each row is a group of the card, with the share that makes the target at each RZP length and the verdict at the same prices.

| What you read (4c2e) | 4-move RZP: DR in 7 or less | Verdict at 4 | 5-move RZP: DR in 6 or less | Verdict at 5 | 6-move RZP: DR in 5 or less | Verdict at 6 |
|---|---|---|---|---|---|---|
| 2 pairs (a bar) | 98.3% | **switch** | 60.0% | **switch** | 22.5% | **switch** |
| 1 pair and a side pair | 98.0% | **switch** | 55.5% | **switch** | 11.0% | skip |
| 0 pairs, JZP (ARM 00) with 4b corners | 100% | **switch** | 66.7% | **switch** | 8.3% | skip |
| 1 pair, no side pair, 4b-0 corners | 96.7% | **switch** | 43.3% | **switch** | 0% | skip |
| 1 pair, no side pair, 4a-2 corners | 83.3% | **switch** | 23.8% | skip | 0% | skip |
| 1 pair, no side pair, ARM 31 | 91.7% | **switch** | 19.4% | skip | 0% | skip |
| 1 pair, anything else | 70.3% | **switch** | 9.4% | skip | 0% | skip |
| 0 pairs, anything else | 42.5% | **switch** | 3.9% | skip | 0% | skip |

| What you read (3c2e) | 4-move RZP: DR in 7 or less | Verdict at 4 | 5-move RZP: DR in 6 or less | Verdict at 5 | 6-move RZP: DR in 5 or less | Verdict at 6 |
|---|---|---|---|---|---|---|
| 1 pair | 100% | **switch** | 88.7% | **switch** | 38.7% | **switch** |
| 0 pairs, a fake pair or a split pair | 100% | **switch** | 56.5% | **switch** | 10.5% | skip |
| 0 pairs, no fake pair, no split pair | 92.5% | **switch** | 17.5% | skip | 0% | skip |

| What you read (7c8e) | 4-move RZP: DR in 7 or less | Verdict at 4 | 5-move RZP: DR in 6 or less | Verdict at 5 | 6-move RZP: DR in 5 or less | Verdict at 6 |
|---|---|---|---|---|---|---|
| 6 pairs, not ARM 64 | 100% | **switch** | 96.5% | **switch** | 49.1% | **switch** |
| 5 pairs, not ARM 20 or 54 | 94.4% | **switch** | 55.9% | **switch** | 14.7% | skip |
| 4 pairs, ARM 21, 31 or 43 | 89.1% | **switch** | 34.9% | **switch** | 2.6% | skip |
| 3 pairs, ARM 21 | 100% | **switch** | 27.8% | **switch** | 0% | skip |
| 4 pairs, ARM 11, 12, 33, 41 or 62 | 84.5% | **switch** | 21.8% | skip | 0% | skip |
| 4 pairs, anything else | 63.9% | **switch** | 6.8% | skip | 0% | skip |
| 5 or 6 pairs with ARM 20, 54 or 64 | 53.3% | **switch** | 0% | skip | 0% | skip |
| 3 pairs or fewer | 33.7% | **switch** | 2.5% | skip | 0% | skip |

| What you read (8c8e) | 4-move RZP: DR in 7 or less | Verdict at 4 | 5-move RZP: DR in 6 or less | Verdict at 5 | 6-move RZP: DR in 5 or less | Verdict at 6 |
|---|---|---|---|---|---|---|
| 8 pairs | 100% | **switch** | 100% | **switch** | 100% | **switch** |
| 6 pairs, corner ARM 4 | 92.9% | **switch** | 50.0% | **switch** | 17.9% | skip |
| 5 pairs, edge ARM 1 or 3 | 90.9% | **switch** | 45.5% | **switch** | 4.5% | skip |
| 2 pairs, ARM 42 | 77.5% | **switch** | 32.5% | **switch** | 2.5% | skip |
| 4 pairs, ARM 42 | 74.1% | **switch** | 25.2% | **switch** | 3.4% | skip |
| 4 pairs, ARM 02, 43, 63 or 82 | 89.5% | **switch** | 22.1% | skip | 0% | skip |
| 6 pairs, corner ARM not 4 | 76.8% | **switch** | 14.3% | skip | 0% | skip |
| 5 pairs, edge ARM 2 | 63.1% | **switch** | 3.6% | skip | 0% | skip |
| anything else | 47.7% | **switch** | 3.4% | skip | 0% | skip |

| What you read (2c2e) | 4-move RZP: DR in 7 or less | Verdict at 4 | 5-move RZP: DR in 6 or less | Verdict at 5 | 6-move RZP: DR in 5 or less | Verdict at 6 |
|---|---|---|---|---|---|---|
| 1 pair | 100% | **switch** | 62.5% | **switch** | 12.5% | skip |
| 2 pairs and a side pair | 100% | **switch** | 100% | **switch** | 0% | skip |
| 0 pairs, 1 side pair, ARM 00 or 11 | 100% | **switch** | 68.8% | **switch** | 0% | skip |
| 0 pairs, JZP (ARM 00), no side pair | 100% | **switch** | 18.2% | skip | 0% | skip |
| anything else | 78.4% | **switch** | 6.1% | skip | 0% | skip |

**The low DRMs in full.** The card of each low DRM with all its groups, followed by the current policies where there are any. Radek B's 4c6e rule came with a hedge ("If the numbers are correct, then it seems to me like tracing pairs is a really good way of deciding whether to switch for 4c6e. Like only if there are 4 pairs (or if it's jzp)", [29 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1278779433225814158)), and Fanti's 3c4e list is "my rough sketch of 34 (maybe not final)" ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436042954501390401)).

| What you read (4c6e) | Verdict | Share of 4c6e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 4 pairs on three edges | **switch** | 0.85% | 74.0% | 88.9% | 33.9% | 9.5% |
| 3 pairs, JZP (ARM 00) | **switch** | 0.31% | 61.1% | 11.1% | 11.3% | 3.0% |
| 3 pairs on three edges, the three bad edges in one layer | **switch** | 0.27% | 62.5% | 0% | 4.8% | 3.6% |
| 3 pairs on three edges, corners 2 and 2 in the layers | **switch** | 2.2% | 25.8% | 0% | 11.3% | 12.7% |
| anything else | skip | 96.4% | 3.2% | 0% | 38.7% | 71.2% |

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| never | *DRM Subsets Meta* | 0% | 100% | 100% | 100% | 0.189 |
| only JZP | Yura Riabov, [24 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1265765209050714142) | 0.61% | 44.4% | 82.3% | 94.1% | 0.164 |
| 4 pairs or JZP | Radek B, [29 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1278779433225814158) | 1.8% | 0% | 53.2% | 84.3% | 0.135 |
| **the card** | this page | 3.6% | 0% | 38.7% | 71.2% | 0.125 |

| What you read (3c4e) | Verdict | Share of 3c4e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 2 pairs and a side pair | **switch** | 6.9% | 43.2% | - | 39.1% | 28.9% |
| 2 pairs, no side pair, a fake pair | **switch** | 1.9% | 27.3% | - | 8.7% | 4.7% |
| 1 pair, 2 side pairs | **switch** | 5.7% | 28.1% | - | 17.4% | 16.1% |
| 1 pair, ARM 21, 1 side pair, 2 fake pairs or holes on one R/L face | **switch** | 2.6% | 40.3% | - | 26.1% | 9.0% |
| 1 pair, ARM 21, 1 side pair, the rest | if you have time | 3.5% | 19.5% | - | 4.3% | 7.1% |
| anything else | skip | 79.4% | 3.9% | - | 4.3% | 34.1% |

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| 2+ pairs | *DRM Subsets Meta* (sometimes) | 10.7% | 0% | 52.2% | 64.9% | 0.292 |
| 2 pairs; 1 pair with ARM 00 or 21 | Fanti, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436042954501390401) | 23.7% | 0% | 21.7% | 39.8% | 0.302 |
| **the card** | this page | 17.1% | 0% | 8.7% | 41.2% | 0.228 |
| the card with its *if you have time* groups | this page | 20.6% | 0% | 4.3% | 34.1% | 0.233 |

| What you read (3c6e) | Verdict | Share of 3c6e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 2 pairs, ARM 21, 1 or 2 fake pairs | **switch** | 4.1% | 31.3% | 100% | 44.4% | 22.7% |
| 2 pairs, ARM 12, 2 fake pairs | **switch** | 1.4% | 38.6% | 0% | 11.1% | 11.4% |
| 2 pairs, ARM 01 | **switch** | 1.5% | 22.9% | 0% | 11.1% | 6.8% |
| anything else | skip | 93.0% | 2.9% | 0% | 33.3% | 59.1% |

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| never | not on the *DRM Subsets Meta* list | 0% | 100% | 100% | 100% | 0.195 |
| 3 pairs with ARM 00; 2 pairs with ARM 21 | Fanti, [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436042954501390401) | 4.7% | 0% | 55.6% | 75.8% | 0.158 |
| **the card** | this page | 7.0% | 0% | 33.3% | 59.1% | 0.140 |

| What you read (5c4e) | Verdict | Share of 5c4e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 3 pairs, 2+ side pairs | **switch** | 2.2% | 38.3% | 37.5% | 26.1% | 10.0% |
| 2 pairs, ARM 21, 2+ side pairs | **switch** | 2.8% | 32.7% | 37.5% | 20.5% | 11.4% |
| 1 pair, ARM 21, 2+ side pairs, 2+ fake pairs | **switch** | 1.8% | 24.3% | 25.0% | 10.2% | 5.3% |
| 3 pairs, 0 or 1 side pair | if you have time | 3.9% | 21.5% | 0% | 6.8% | 12.2% |
| anything else | skip | 89.3% | 4.7% | 0% | 36.4% | 61.0% |

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| never | *DRM Subsets Meta* | 0% | 100% | 100% | 100% | 0.278 |
| 2 pairs with ARM 21, or 3+ pairs | Jay, [21 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1396982409290977382) | 11.7% | 25.0% | 44.3% | 62.5% | 0.243 |
| **the card** | this page | 6.8% | 0% | 43.2% | 73.3% | 0.216 |
| the card with its *if you have time* groups | this page | 10.7% | 0% | 36.4% | 61.0% | 0.218 |

| What you read (5c6e) | Verdict | Share of 5c6e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 4 pairs | **switch** | 3.1% | 37.9% | 37.5% | 30.2% | 17.5% |
| 3 pairs, ARM 21, 3 side pairs | **switch** | 1.2% | 38.3% | 37.5% | 14.6% | 6.2% |
| 2 pairs, ARM 21, 3 side pairs | **switch** | 2.0% | 20.6% | 25.0% | 12.5% | 6.1% |
| 3 pairs, ARM 21, fewer than 3 side pairs | if you have time | 2.1% | 17.4% | 0% | 5.2% | 6.2% |
| anything else | skip | 91.6% | 4.1% | 0% | 37.5% | 64.1% |

| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |
|---|---|---|---|---|---|---|
| never | *DRM Subsets Meta* | 0% | 100% | 100% | 100% | 0.233 |
| 3 pairs with ARM 21, or 4+ pairs | Jay, [21 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1396982409290977382) | 6.4% | 25.0% | 50.0% | 70.2% | 0.190 |
| **the card** | this page | 6.3% | 0% | 42.7% | 70.3% | 0.181 |
| the card with its *if you have time* groups | this page | 8.4% | 0% | 37.5% | 64.1% | 0.186 |

| What you read (6c6e) | Verdict | Share of 6c6e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |
|---|---|---|---|---|---|---|
| 5 or 6 pairs | **switch** | 1.2% | 39.0% | 20.0% | 14.6% | 7.3% |
| 3 pairs, 3 fake pairs, corners 3 and 3 in the layers | **switch** | 1.9% | 34.1% | 40.0% | 20.8% | 10.1% |
| anything else | skip | 97.0% | 4.6% | 40.0% | 64.6% | 82.6% |

More pockets, one example each:

```
L' D2 R' D'   // setup: 4c6e, 4 pairs on three edges
D R D2 L   // DR in 4
```

```
R' D' L R   // setup: 6c6e, 3 pairs, 3 fake pairs, corners 3 and 3
R' L' D R   // DR in 4
```

```
R' B2 U2 R' B2 R   // setup: 2c2e, 0 pairs, 1 side pair, ARM 00
R' B2 R U2 B2 R   // DR in 6
```

---

## Appendix B: how it was computed, and what checks it

**The table.** The DR length of every case comes from a breadth-first search over the 1,082,565 cases with the 14 turns that keep an F/B EO. It's the table of my EO-to-DR study, it agrees with Cale's sheet, and its histogram is proved in Lean.

**The reads.** Defined from stickers, on the switched case. Pairs, fake pairs, side pairs and ARM agree with rodneykinney's own code on every case. The normal-side versions are the ones of section 6, checked there.

**The search for the cards.** Per DRM, over the quick reads (ARM, corner case, side pairs, fake pairs, edges with a pair, holes, layers, columns): a greedy list of rules of up to two conditions inside a pair count, and a small tree grown to rank well at three prices of a wasted switch. Both score with the prices of section 3. I then wrote each card by hand from what they agreed on, in as few groups as kept the cost, took the server's rule wherever it did as well or better (wen's for 3c2e, caycala's chart for 7c8e, Evan's stacked corners for 4a), and graded the written card from scratch. The ceilings of section 9 come from the same code with every combination of values as its own group.

**What *the best list on the server* is.** For each DRM, the rule with the lowest cost per case among the ones I found stated: the *DRM Subsets Meta* row, Fanti's lists, caycala's chart, tseitsei89's, rodneykinney's, wen's, Jay's and Radek B's. Appendix A names it per DRM.

**Real attempts.** The scrambles are uniformly random states, not nissy's scrambler. For each one, on both sides and all three EO axes: every EO of at most 5 moves, every RZP after it, kept when it first reaches its DRM at a total of 5.

**Examples.** Every setup and DR printed on this page was replayed on a sticker-level cube, and the DR lengths are the table's.

**Lean.** The Lean 4 project that goes with this study (no Mathlib) recounts the tables on its own model of the cube: its own breadth-first search for the DR lengths, the reads defined from stickers, and then, for each of the 12 DRMs, every group of the card with its cases by DR length, and every policy with what it switches and what it misses at each length. Every theorem is checked by compiled evaluation (`native_decide`), and every one equals the number printed here. Three of them spelled out:

| Policy (4c4e) | Cases switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Switched with a DR of 7 or more |
|---|---|---|---|---|---|
| the card | 17,592 | 0 | 220 | 3,724 | 7,960 |
| 2+ pairs | 18,360 | 46 | 508 | 4,500 | 9,838 |
| pairs + ARM (Fanti) | 24,864 | 8 | 144 | 2,840 | 14,280 |

Computed but not proved: the prices and the cost per case, the gradings after a 4-move and a 6-move RZP, the ceilings and the search, the real attempts, and the colour reads on normal (those are checked on a sample, section 6). The half-turn count of section 7 was proved in the same project earlier.

---

## Docs referred to

- rodneykinney, [*DRM Subsets Meta*](https://docs.google.com/document/d/1Jnd1Qy_6b1W5dR5fZQScloMoMPR2LCAF7VPrgeTaRgg), [*DRM Subsets*](https://docs.google.com/document/d/1AUQVrecEFZyR6okXAyJgtQZA-A0AJmAUevhJZlQMjAs), [*DR - 4c4e Theory*](https://docs.google.com/document/d/1DsxAAB2WRfpgDR-VWZZrXq2W4y_YMXBufRRYNLAGGoU), [*Domino Setup Theory*](https://docs.google.com/document/d/1Z3O8BY1LbAMF6m55ufXtSdtBVwSJpMArtRrDT-p_CwM), [*DRM corner variant+pair stats*](https://docs.google.com/spreadsheets/d/174ClwBFl-T2zJAq8MVyK1bKsIIuzxQU0_XmQGv82LPQ).
- Louis, [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs). Cale, [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0). Evan, [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk).
- caycala's chart, attached to the message of [25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1365334546035245227). Fanti, *armpairs_1.txt*, attached to the message of [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069).
- wen and others, [*Hitchhiker's Guide to DR*](https://docs.google.com/document/d/1E_5wSKvQFXXZY4f3xLM76qMUrVGp9Pe7vgotS0X-T4U).
- Andrew, [*How to do Domino Reductions: The Secret They Don't Want You To Know*](https://www.youtube.com/watch?v=oAbPQOfui2U) (FewestMoves channel, 6 Feb 2019).
- On this site: [*EO to DR, and scramble to DR*](../eo-to-dr/), [*Judging a DR by hand*](../judging-a-dr/).
