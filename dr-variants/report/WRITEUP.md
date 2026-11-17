# Pruning the search for a DR solution

You have a DR and a goal: a leave-slice solution in 12 from a 2qt DR, 13 from a 3qt, 14 from a 4qt. You go through corner skeletons and their variants, and nearly every HTR you could finish is a waste of time. This page measures which ones are: what the rule bound of Advanced DR Bounding removes, what a pair count at HTR removes on top of it, in which order to finish what's left, what NISS adds, and when to give up on the DR.

Every HTR in reach of the goal was finished exactly, on normal and on inverse, for about 2,000 uniformly random DRs of each kind (66 million HTRs). The pair floor is proved in Lean.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion).

**This builds on:**

- **Levi Gibson's [DR Bounding](https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA)** ([27 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311464464737898589)) and **Rodney Kinney's [Advanced DR Bounding [Beta]](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0)** ([29 Aug 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1543125354120609832)): corner skeletons and variants, the penalty L + S + T (+N), the NISS@1qt cases, bad slices and parity, and the rules that bound N from below. On the server Levi posts as beef beans; this page says Levi.
- **The doc's *HTR Search Meta***, which is the search this page prunes: "Start by writing down all of the distinct ways to reach 2qt, and explore each one in turn. DR Bounding will prune the search heavily." The goals are the ones of its random-scramble examples: "a leave-E-slice solution in 12 moves for 2qt, 13 for 3qt, and 14 for 4qt".
- **Rodney Kinney's sheet [Adv DR Bounding](https://docs.google.com/spreadsheets/d/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY)** ([18 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1550498925528485992)), tab *Optimals (Advanced)*: the 216 NISS@1qt cases with the rule's value for each (column *Heuristic*). From the doc: "Lorenzo Mauro has computed optimal algorithms for all 216 of the corner/edge combined cases."
- **Rodney Kinney's [DRM Subsets](https://docs.google.com/document/d/1AUQVrecEFZyR6okXAyJgtQZA-A0AJmAUevhJZlQMjAs)** ([14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383615680179601449)): precision, recall, and the score used here to weigh them, "mutual info ≡ p(objective | subset) \* N(subset, objective)".
- **Levi Gibson's sheet [Pairs in DR](https://docs.google.com/spreadsheets/d/1jY9dLAO6CbxF9Eu7BR-kD34KNnIvAVC8uh49aVDBTn8)** ([4 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1148330628358623242)) on how much pairs matter in each DR subset, and what Levi said about it ([4 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1148362613500162228)): "There are wild departures. HTR for example! In HTR, pairs matter so little compared to other DR states".
- **[*Judging a DR by hand*](../judging-a-dr/)** on this site: the exact optimal leave-slice finish of every DR state, the sorting of the HTR states into the 216 cases, and the Lean cube model the pair floor is proved on.

**What it adds:**

- **What the rule bound is worth as a filter**: how many HTRs it removes, and that it never removes a within-goal one (section 5).
- **A second floor, read at HTR by counting pairs.** With n moves left for the finish you need 16 − 4n pairs. It's proved in Lean, and together with the rule it leaves a few dozen HTRs per DR (sections 6 and 7).
- **What pairs tell you at 2qt, at 1qt and at HTR**, and how often a within-goal solution has to split them (section 8).
- **Which order to finish HTRs in**, which skeleton to start with, what NISS adds and when to abandon, in precision, recall and mutual info (sections 9 to 12).
- **How often a within-goal solution exists and where it sits**: how many extra moves, which side, how many quarter turns (sections 3 and 4).

**Terms.**

- **Leave-slice solution.** DR moves that solve the corners and the eight U/D edges and leave the E slice as it falls. Lengths are HTM. Finishes that leave the DR group (the M-slice algs of the sheet, 3e insertions) aren't counted.
- **HTR, variant.** Here an HTR is a sequence of DR moves that ends with a quarter turn and lands in HTR, on the normal scramble or on the inverse. Checking it means finishing from there: the solution has (moves to HTR) + (finish) moves.
  - U and D are the same quarter turn for a leave-slice solution (the doc: "we can freely choose between U and D moves in our variants"), and the direction of the last quarter turn is settled while finishing. HTRs that differ only in those choices are counted once.
- **Skeleton, L, M.** The skeleton of an HTR is (side, number of quarter turns, NISS@1qt corner case). L is the length of the shortest corner path of that kind. The corner case then needs 0 more moves for H-H, 1 for R-D and F-D, 2 for R-V and F-V, 3 for D-D. **M**, the doc's maximum penalty, is the goal minus both.
- **S+T, extra moves.** Moves to HTR minus L. The part spent before 2qt is given separately where it matters.
- **Rule bound.** Moves to HTR + the corner case's own moves + the rule's N for the case the HTR lands on. An HTR **passes the rule** if that is at most the goal.
- **Pairs.** True corner-edge pairs in the U and D layers: a corner and an edge of the same layer joined as on a solved cube. 16 when the layers are solved. The count is the same on the inverse of any state (a pair there is a pair here, somewhere else), so there is nothing extra to read on the inverse.
- **Pair floor.** With n moves left for the finish (goal minus moves to HTR), the HTR needs at least 16 − 4n pairs.
- **Within goal.** The HTR's optimal leave-slice finish fits the goal. A **solvable** DR is one with a leave-slice solution within the goal.
- **Precision, recall, mutual info.** For a set of HTRs: the share that are within goal; the share of solvable DRs with a within-goal HTR in the set; and precision times the number of such DRs, as in *DRM Subsets*.
- **Population.** Uniformly random DR states with 2, 3 or 4 quarter turns (4a2 and 4b2; 0c3, 2c3, 4a3, 4b3; 0c4, 2c4, 4a4, 4b4). Not states as they come up in attempts.

**How to read this.** Section 1 is the whole answer. Section 13 puts it in the order you'd use it, and section 14 walks ten scrambles through it. Sections 3 to 12 are the tables behind each line of section 1, always for 2qt, 3qt and 4qt DRs side by side, each with its own goal.

What each read takes at the table:

| Read | What it takes |
|---|---|
| L, M, S+T | finding the skeleton and the HTR (a search), then arithmetic |
| Rule bound | tracing the NISS@1qt case by colour at 1qt, per the doc |
| Pair floor | counting pairs at HTR, at a glance |
| Finishing an HTR | a search |
| 216-case table | **computer only** |

Counts per DR are exact for the DRs in the sample. A share of DRs carries about ±3 points.

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | The answer, with the headline numbers. |
| [2. What was asked](#2-what-was-asked) | The five questions. |
| [3. How often a within-goal solution exists](#3-how-often-a-within-goal-solution-exists) | Base rates by quarter turns and by subset. |
| [4. Where the within-goal solutions are](#4-where-the-within-goal-solutions-are) | By extra moves, by side, before or after 2qt. |
| [5. The rule bound as a filter](#5-the-rule-bound-as-a-filter) | What it removes, what it never removes, how much slack it leaves. |
| [6. The pair floor](#6-the-pair-floor) | **The new read.** The floor, its proof, and why it only bites under a goal. |
| [7. Both floors together](#7-both-floors-together) | The card: chance of a within-goal finish by pairs at HTR and moves left. |
| [8. Pairs along the route](#8-pairs-along-the-route) | Pairs at 2qt, at 1qt and at HTR, and how often they get split. |
| [9. Which order to finish in](#9-which-order-to-finish-in) | Eight orders against the baseline. |
| [10. Skeletons: which first, how far](#10-skeletons-which-first-how-far) | By maximum penalty M, and the mutual info level by level. |
| [11. NISS](#11-niss) | The inverse, and NISS in the middle of a skeleton. |
| [12. When to abandon](#12-when-to-abandon) | Each stop signal: how often it comes up, how often it's wrong. |
| [13. The meta](#13-the-meta) | The steps, and what they cost and find. |
| [14. Examples](#14-examples) | Ten scrambles. |
| [15. The claims, checked](#15-the-claims-checked) | What the doc, Levi and the question itself say, against the numbers. |
| [16. What this does not cover](#16-what-this-does-not-cover) | Limits. |
| [Appendix: how it was computed, and what is proved in Lean](#appendix-how-it-was-computed-and-what-is-proved-in-lean) | The sample, the checks, the Lean theorems by name. |

## 1. The short version

The headline numbers. A row is one measure, a column one kind of DR with its goal.

| Measure | 2qt, goal 12 | 3qt, goal 13 | 4qt, goal 14 |
|---|---:|---:|---:|
| DRs that have a solution within goal | 53% | 72% | 80% |
| HTRs in reach of the goal, per DR | 5,109 | 10,725 | 17,358 |
| Of those, HTRs that pass the rule bound | 186 | 349 | 544 |
| HTRs that pass the rule bound and the pair floor | 33 | 52 | 66 |
| Share of those that are within goal | 15% | 17% | 19% |
| Within-goal HTRs that fail the rule bound | 0 | 0 | 0 |
| Solvable DRs with a solution at S+T ≤ 2, both sides | 56% | 68% | 79% |
| Solvable DRs with a solution at S+T ≤ 3, both sides | 80% | 87% | 94% |
| Same, with at most 1 extra move before 2qt | 75% | 82% | 86% |
| Found within 5 finishes there: both floors, most pairs first | 61% | 63% | 69% |
| Found within 40 finishes there: the baseline | 69% | 67% | 60% |

The last three rows are about one fixed reach: every HTR with S+T ≤ 3 and at most 1 extra move before 2qt, on both sides. The share found is among the DRs that have a solution.

- **The rule bound removes 96–97% of the HTRs and never a within-goal one.** None of the 52,216 within-goal HTRs in the sample fails it, and it is a floor on all 663,552 HTR states. The parity half of the rule matters: counting bad slices alone keeps more than four times as many.

- **New: a pair floor at HTR does the same job again.** A side half turn makes at most 4 pairs. So with n moves left for the finish you need at least 16 − 4n pairs at HTR: 16 with none left, 12 with one, 8 with two, 4 with three. That's proved in Lean. On its own it removes about as many HTRs as the rule, and the two overlap little, which is how thousands of HTRs become a few dozen.

- **Finish the HTR with the most pairs first.** With both floors and most pairs first, 5 finishes find nearly what the baseline finds in 40, and more than that for 4qt DRs (the last two rows). The baseline is shortest HTR first with pairs as the tie-break.

- **Pairs are a weak read before the trigger and a strong one at HTR.** As a ranker of the HTRs that pass the rule, the pair count scores 0.62 to 0.73 at 2qt and 0.88 to 0.93 at HTR (0.5 is a coin flip). Pairs don't pick the route, they pick the HTR.

- **Within-goal solutions rarely split pairs.** The finish splits a pair that stood at HTR in 4% / 2% / 1% of them (2qt / 3qt / 4qt), and only with 5 or more moves left. The setup or trigger splits a 2qt pair in 32% / 28% / 22%, against 64% / 62% / 59% for HTRs in general.

- **One extra move before 2qt is worth it, a second mostly isn't.** For 4qt DRs, allowing none caps the reach at 60% (S+T ≤ 3 after 2qt), allowing one gives 92%, two 98%, and each step roughly triples the routes to 2qt.

- **The inverse is worth about one extra move.** Normal and inverse to S+T ≤ k reach about what normal alone reaches at k + 1. A NISS after the first quarter turn of each shortest route adds about 3 points more at S+T ≤ 2.

- **Skeletons with two more quarter turns can't be skipped.** They hold the only within-goal solutions of 32% of solvable 2qt DRs, 13% of 3qt and 9% of 4qt.

- **Start with the skeleton with the most room.** Among skeletons with the fewest quarter turns of a 3qt DR, one with maximum penalty M = 3 holds a within-goal HTR 20% of the time, with M = 5 48%, with M = 7 73%. Skip M ≤ 1.

- **Abandoning.** If no HTR with S+T ≤ 3 passes the rule on either side, a solution still exists in 3% of 2qt DRs. If you've finished everything that passes both floors through S+T ≤ 3 and found nothing, one still exists 19% / 25% / 19% of the time; through S+T ≤ 4, 8% / 10% / 4%.

- **The hand rule is close to what the 216 cases can give.** Looking every case up in an exact table instead (**computer only**) would leave 21 / 34 / 45 HTRs per DR instead of 30 / 48 / 60.

- **What's left is depth.** The floors only help with HTRs you get to, and a within-goal solution is rarely cheap: skeletons as they are (S+T = 0) hold one for 11% to 15% of solvable DRs.

## 2. What was asked

The search is the usual one from a DR. You go through corner skeletons one at a time, add extra moves to a skeleton's variants up to some point, then move to the next skeleton or give up on the DR. You know the moves to HTR at any point, you can work out the Advanced DR Bounding lower bound for what comes after HTR, and you can count corner-edge pairs on both sides of the scramble, with no finer tracing on the inverse. Long insertions have too many possibilities to try speculatively, so NISS is there to find the solutions with a long insertion near the beginning of the skeleton, and sometimes in the middle.

The baseline is to check variants in order of moves to HTR, on both sides, with no speculative mid-skeleton NISS, preferring variants that form pairs.

1. **What are the best heuristics for pruning that search, and how does the DR Bounding lower bound fit into a better meta than the baseline?** *Answer*: two floors and one order. The rule bound and the pair floor decide what to finish (sections 5 to 7), most pairs first decides the order (section 9), and section 13 puts it together.
2. **How good is each heuristic in precision and recall terms?** The weighing is the mutual info of *DRM Subsets*: how likely a variant is to give a leave-slice solution within the goal, against how many DRs have a within-goal solution starting with that variant's prefix. *Answer*: the tables give precision as the share within goal and recall as the share of solvable DRs covered. The mutual info level by level is in section 10.
3. **Where does NISS belong?** *Answer*: the inverse from the start is worth about one extra move. A NISS after the first quarter turn is cheap and adds a few points. Later ones find less than going a level deeper does (section 11).
4. **When should you abandon a DR that has no solution within the goal?** *Answer*: there is one safe signal and it's rare. After that it's a trade, with the numbers in section 12.
5. **Is forming pairs a poor heuristic?** The suspicion: pairs often have to be broken up after HTR or during the trigger, but forming pairs is a good way of telling apart variants with similar lower bounds. *Answer*: pairs seldom have to be broken up in a within-goal solution, and they tell variants apart well at HTR, weakly before the trigger (section 8).

Only 2qt, 3qt and 4qt DRs, with goals of 12, 13 and 14.

## 3. How often a within-goal solution exists

Share of DR states whose optimal leave-slice solution is within the goal (20 million random states, exact lengths).

| DR | Share of all DR states | Goal | Solution within goal − 2 | Within goal − 1 | Within goal | Mean optimal leave-slice |
|---|---:|---:|---:|---:|---:|---:|
| 2qt | 14.3% | 12 | 5.4% | 19.3% | 52.7% | 12.34 |
| 3qt | 28.1% | 13 | 9.5% | 32.7% | 72.0% | 12.88 |
| 4qt | 35.2% | 14 | 11.0% | 39.1% | 80.1% | 13.68 |

The same by subset, in the sample. A row is one subset with its number of bad edges.

| Subset | DRs in the sample | With a solution within goal |
|---|---:|---:|
| 4a2 2e | 172 | 18% |
| 4a2 4e | 193 | 45% |
| 4b2 0e | 47 | 62% |
| 4b2 2e | 719 | 62% |
| 4b2 4e | 818 | 58% |
| 0c3 4e | 49 | 16% |
| 2c3 2e | 231 | 97% |
| 2c3 4e | 537 | 87% |
| 2c3 6e | 241 | 76% |
| 4c3 2e | 374 | 58% |
| 4c3 4e | 450 | 62% |
| 2c4 2e | 293 | 91% |
| 2c4 4e | 599 | 90% |
| 2c4 6e | 314 | 90% |
| 4c4 2e | 296 | 55% |
| 4c4 4e | 376 | 59% |

A solvable DR has few within-goal HTRs: the median is 4 / 8 / 10 over both sides, against thousands in reach.

## 4. Where the within-goal solutions are

**By extra moves and side.** Share of solvable DRs with a within-goal HTR at that S+T or less.

2qt, goal 12:

| S+T at most | Normal only | Normal and inverse | Both, shortest-qt skeletons only |
|---|---:|---:|---:|
| 0 | 6% | 11% | 8% |
| 1 | 20% | 36% | 26% |
| 2 | 35% | 56% | 38% |
| 3 | 58% | 80% | 54% |
| 4 | 78% | 93% | 63% |
| 5 | 90% | 98% | 65% |

3qt, goal 13:

| S+T at most | Normal only | Normal and inverse | Both, shortest-qt skeletons only |
|---|---:|---:|---:|
| 0 | 8% | 14% | 12% |
| 1 | 27% | 43% | 37% |
| 2 | 49% | 68% | 57% |
| 3 | 74% | 87% | 72% |
| 4 | 89% | 95% | 81% |
| 5 | 96% | 99% | 84% |

4qt, goal 14:

| S+T at most | Normal only | Normal and inverse | Both, shortest-qt skeletons only |
|---|---:|---:|---:|
| 0 | 7% | 15% | 12% |
| 1 | 30% | 51% | 44% |
| 2 | 61% | 79% | 69% |
| 3 | 85% | 94% | 83% |
| 4 | 95% | 99% | 89% |
| 5 | 99% | 100% | 90% |

- **You need extra moves.** Skeletons as they are (S+T = 0) cover 11%–15%.
- **The inverse is worth about one extra move.** Both sides at S+T ≤ 2 reach a little less than normal alone at 3, and both at 3 a little more than normal alone at 4.
- **Shortest-qt skeletons run out.** The last column stalls at 65% / 84% / 90%. For 32% / 13% / 9% of solvable DRs every within-goal solution has two more quarter turns than the minimum. A further 0.5% / 0.1% / 0.0% need four more and are outside this page.

**Before or after 2qt.** Share of solvable DRs reached on both sides, all skeletons, by where the extra moves may sit. A 2qt DR has no moves before 2qt in its shortest-qt skeletons, so the table is for 3qt and 4qt.

| DR | Extra moves before 2qt | Reached with S+T after 2qt ≤ 2 | With ≤ 3 | With ≤ 4 | Routes to 2qt per DR (at ≤ 3) |
|---|---:|---:|---:|---:|---:|
| 3qt | none | 53% | 67% | 76% | 43 |
| 3qt | at most 1 | 74% | 88% | 94% | 206 |
| 3qt | at most 2 | 81% | 93% | 97% | 525 |
| 4qt | none | 48% | 60% | 68% | 96 |
| 4qt | at most 1 | 82% | 92% | 95% | 514 |
| 4qt | at most 2 | 92% | 98% | 99% | 1,385 |

The first extra move before 2qt buys a lot and the second little, while the routes to 2qt multiply. That's the split of section 2: short insertions early, the longer ones in the setup and the trigger, where the bound tells you which to make.

## 5. The rule bound as a filter

HTRs left per DR on both sides, at any depth, after each filter.

| HTRs left per DR after | 2qt | 3qt | 4qt |
|---|---:|---:|---:|
| Every HTR in reach | 5,109 | 10,725 | 17,358 |
| Bad slices only, no parity (0 / +3, +2 for R-V and F-V / +5) | 825 | 1,586 | 2,517 |
| Rule bound (the Advanced rule) | 186 | 349 | 544 |
| Pair floor alone | 190 | 324 | 410 |
| Rule bound and pair floor | 33 | 52 | 66 |
| Rule bound and exact pair floor | 30 | 48 | 60 |
| 216-case table and exact pair floor (computer only) | 21 | 34 | 45 |

The share of them that are within goal:

| Share within goal among the HTRs left after | 2qt | 3qt | 4qt |
|---|---:|---:|---:|
| Every HTR in reach | 0.1% | 0.1% | 0.1% |
| Bad slices only, no parity (0 / +3, +2 for R-V and F-V / +5) | 0.6% | 0.6% | 0.5% |
| Rule bound (the Advanced rule) | 2.6% | 2.5% | 2.3% |
| Pair floor alone | 2.5% | 2.7% | 3.1% |
| Rule bound and pair floor | 15% | 17% | 19% |
| Rule bound and exact pair floor | 16% | 18% | 21% |
| 216-case table and exact pair floor (computer only) | 23% | 26% | 28% |

- **It never loses a solution.** All 52,216 within-goal HTRs pass the rule, and the rule is a floor on every HTR state (appendix).
- **It's a floor, not an estimate.** Over all HTR states, only 1.7% sit exactly at the rule's value, 8% within 1, 25% within 2. Case by case, the best state of a case sits exactly at the rule's value in 46 of the 216 cases, 1 over in 57 and 2 or more over in 113. An H-H HTR with zero bad slices and good parity can still need 12 moves: `R2 U2 D2 F2 U2 L2 U2 B2 L2 F2 U2 B2 U2 B2` is one.
- **Slack under the goal is rare.** How far the rule bound is under the goal:

| Rule bound against the goal | 2qt: HTRs per DR | 2qt: within goal | 3qt: HTRs per DR | 3qt: within goal | 4qt: HTRs per DR | 4qt: within goal |
|---|---:|---:|---:|---:|---:|---:|
| over the goal | 4,922.6 | 0.0% | 10,376.2 | 0.0% | 16,813.9 | 0.0% |
| equal to the goal | 146.9 | 2.0% | 280.7 | 2.1% | 449.4 | 2.1% |
| 1 under | 30.7 | 3.2% | 55.6 | 3.1% | 78.3 | 2.6% |
| 2 under | 6.8 | 8.4% | 10.1 | 8.3% | 13.4 | 6.9% |
| 3 or more under | 1.7 | 17.6% | 2.4 | 16.7% | 2.6 | 13.7% |

More than nine in ten of the HTRs that pass sit exactly at the goal or 1 under, and that's also where most within-goal HTRs are. An HTR 2 or more under is a better bet, but there are few of them. Ordering by the bound doesn't get you far; you need another read.

- **Bad slices.** Of the HTRs that pass the rule, 94% / 96% / 97% have zero bad slices. At these goals a bad slice almost always means the HTR is out. The one-bad-slice HTRs that do pass are within goal more often (6.2% against 2.4% at 3qt).

## 6. The pair floor

U and D moves never change the number of pairs in the U and D layers: each layer turns as a whole. A side half turn carries four corner-edge slots as a whole and splits four, so it changes the count by at most 4. A leave-slice finish ends with all 16 pairs. So:

| Moves left for the finish | Pairs needed at HTR |
|---:|---:|
| 0 | 16 |
| 1 | 12 |
| 2 | 8 |
| 3 | 4 |
| 4 or more | any |

- **Proved in Lean.** `pair_floor`: if a sequence of DR moves solves the corners and the U/D edges of a state with p pairs, it has at least (16 − p) / 4 side half turns. It holds for any DR state, not only at HTR, and for full finishes too. The proof is on the cube model the exact table of DR finishes is certified on, and uses no computation outside the kernel. The floor is reached at every level: `R2` (12 pairs), `R2 L2` (8), `R2 L2 F2` (4), `R2 L2 F2 B2` (0).
- **Two refinements at HTR** (exact over all 663,552 HTR states, not in Lean): 10 pairs need 3 moves, not 2 (`R2 U2 R2`), and 2 pairs need 5, not 4 (`R2 U2 R2 F2 B2`). The tables call the floor with these two the exact pair floor.
- **Pairs aren't an estimate either.** Over all HTR states the pair count hardly moves the finish, which is what Levi said in 2023:

| Pairs at HTR | HTR states | Shortest finish of any of them | Mean finish | Longest finish |
|---|---:|---:|---:|---:|
| 0 | 32,352 | 4 | 8.8 | 12 |
| 2 | 167,424 | 5 | 8.7 | 12 |
| 4 | 282,240 | 3 | 8.7 | 12 |
| 6 | 144,384 | 3 | 8.5 | 12 |
| 8 | 26,688 | 2 | 8.4 | 12 |
| 10 | 7,680 | 3 | 7.0 | 9 |
| 12 | 2,688 | 1 | 7.5 | 10 |
| 16 | 96 | 0 | 5.2 | 10 |

`U2 R2 L2 U2 R2 L2 F2 R2 L2 B2` has all 16 pairs and needs 10 moves. The floor only bites because the goal leaves so few moves.

## 7. Both floors together

Neither floor knows what the other knows: the rule reads the NISS@1qt case, the pairs read how close the layers are.

The card: of the HTRs that pass the rule, the share that are within goal, by pairs at HTR and moves left (2,149,522 HTRs, 2qt to 4qt pooled). × fails the pair floor, · has under 150 HTRs.

| Moves left for the finish | 0 pairs | 2 pairs | 4 pairs | 6 pairs | 8 pairs | 10 pairs | 12 pairs | 16 pairs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | × | × | × | × | × | × | × | 45% |
| 1 | × | × | × | × | × | × | 44% | 50% |
| 2 | × | × | × | × | 14% | × | 49% | 52% |
| 3 | × | × | 3% | 4% | 23% | 45% | 49% | 40% |
| 4 | 2% | × | 5% | 11% | 24% | 26% | 46% | · |
| 5 | 3% | 2% | 7% | 11% | 10% | 14% | 19% | · |
| 6 | 7% | 13% | 15% | 16% | 19% | · | · | · |

- **At the floor with 0 or 1 move left, it's close to a coin flip:** 16 pairs with nothing left, 12 with 1.
- **At the floor with 2 or more moves left, it's a long shot:** 14% for 8 pairs with 2 left, 3%–4% for 4 or 6 pairs with 3 left.
- **A step above the floor is the good bet:** 12 pairs with 2 or 3 left (49%, 49%), 8 pairs with 3 or 4 left (23%, 24%).

## 8. Pairs along the route

How well the pair count ranks the HTRs that pass the rule: the chance that a within-goal one has more pairs than one that isn't (0.5 is useless, 1 is perfect).

| DR | Pairs at 2qt | Pairs at 1qt | Pairs at HTR |
|---|---:|---:|---:|
| 2qt | 0.62 | 0.76 | 0.88 |
| 3qt | 0.68 | 0.81 | 0.90 |
| 4qt | 0.73 | 0.84 | 0.93 |

Share within goal of the HTRs that pass the rule, by pairs at 2qt:

| Pairs at 2qt | 2qt | 3qt | 4qt |
|---|---:|---:|---:|
| 0–1 | 1.6% | 1.1% | 0.7% |
| 2–3 | 2.4% | 2.1% | 1.7% |
| 4–5 | 3.0% | 3.4% | 3.4% |
| 6–7 | 4.3% | 5.0% | 6.7% |
| 8 or more | 6.7% | 11.1% | 15.4% |

The same by pairs at HTR:

| Pairs at HTR | 2qt | 3qt | 4qt |
|---|---:|---:|---:|
| 0 | 0.0% | 0.0% | 0.0% |
| 2 | 0.3% | 0.3% | 0.1% |
| 4 | 1.0% | 0.7% | 0.5% |
| 6 | 2.6% | 2.3% | 1.7% |
| 8 | 2.5% | 2.1% | 1.7% |
| 10 | 10.8% | 10.1% | 8.2% |
| 12 or 16 | 42.1% | 46.5% | 46.6% |

How often pairs get split, among within-goal HTRs:

| Among within-goal HTRs | 2qt | 3qt | 4qt |
|---|---:|---:|---:|
| Pairs at 2qt (mean) | 3.8 | 4.2 | 4.5 |
| Of those, still together at HTR (mean) | 3.2 | 3.7 | 4.2 |
| Setup or trigger splits at least one 2qt pair | 32% | 28% | 22% |
| Same, among all HTRs that pass the rule | 64% | 62% | 59% |
| Pairs at HTR (mean) | 10.7 | 11.3 | 12.0 |
| Every optimal finish splits a pair that stood at HTR | 3.5% | 2.1% | 1.0% |

Share of within-goal HTRs whose every optimal finish splits a pair that stood at HTR, by finish length:

| Finish length | 2qt | 3qt | 4qt |
|---|---:|---:|---:|
| 3 moves | 0% | 0% | 0% |
| 4 moves | 1% | 1% | 2% |
| 5 moves | 23% | 21% | 24% |
| 6 moves | 51% | 54% | 51% |
| 7 moves | 78% | 84% | 74% |

- **Forming pairs on the way to 2qt says little.** An HTR whose route had 6–7 pairs at 2qt is within goal 4.3% / 5.0% / 6.7% of the time against 1.6% / 1.1% / 0.7% with 0–1, and few routes have that many.
- **The suspicion of section 2, checked.** Pairs seldom need to be broken after HTR: not at all in finishes of up to 3 moves, and those are 87% of the within-goal HTRs at 3qt. During the setup and trigger a 2qt pair is split in a quarter to a third of within-goal solutions, about half as often as in HTRs at large. So a split pair is a mild warning, not a need.
- **Where pairs do separate variants with similar bounds is at HTR.** With the same moves left and the same rule bound, the pair count is what tells the HTRs apart: that's the card of section 7.

## 9. Which order to finish in

Fix what's in reach: S+T ≤ 3, at most 1 extra move before 2qt, both sides, all skeletons. A row is one order. The first two columns say how many HTRs it has to finish, the others the chance of having found a within-goal solution after so many finishes, among DRs that have one.

2qt (the reach is 75%):

| Order | HTRs to finish per DR | Same, on a DR with no solution | Found within 3 finishes | Within 5 | Within 10 | Within 20 | Within 40 |
|---|---:|---:|---:|---:|---:|---:|---:|
| No floors, by moves to HTR, ties at random | 339 | 281 | 37% | 44% | 53% | 60% | 65% |
| No floors, by moves to HTR, most pairs first (the baseline) | 339 | 281 | 41% | 48% | 58% | 64% | 69% |
| Rule bound only, by moves to HTR, most pairs first | 23.4 | 14.1 | 48% | 57% | 69% | 74% | 75% |
| Both floors, in random order | 11.7 | 5.7 | 37% | 50% | 65% | 73% | 75% |
| Both floors, level by level, most pairs first inside a level | 11.7 | 5.7 | 39% | 52% | 67% | 73% | 75% |
| Both floors, skeleton by skeleton (largest M first) | 11.7 | 5.7 | 46% | 59% | 69% | 74% | 75% |
| Both floors, 12+ pairs on sight, the rest level by level | 11.7 | 5.7 | 45% | 56% | 68% | 74% | 75% |
| Both floors, look at all, then most pairs first | 11.7 | 5.7 | 52% | 61% | 70% | 74% | 75% |

3qt (the reach is 82%):

| Order | HTRs to finish per DR | Same, on a DR with no solution | Found within 3 finishes | Within 5 | Within 10 | Within 20 | Within 40 |
|---|---:|---:|---:|---:|---:|---:|---:|
| No floors, by moves to HTR, ties at random | 774 | 786 | 26% | 33% | 42% | 52% | 61% |
| No floors, by moves to HTR, most pairs first (the baseline) | 774 | 786 | 31% | 38% | 49% | 59% | 67% |
| Rule bound only, by moves to HTR, most pairs first | 46.1 | 30.3 | 39% | 49% | 64% | 76% | 81% |
| Both floors, in random order | 19.0 | 7.6 | 33% | 47% | 66% | 78% | 82% |
| Both floors, level by level, most pairs first inside a level | 19.0 | 7.6 | 35% | 47% | 64% | 77% | 82% |
| Both floors, skeleton by skeleton (largest M first) | 19.0 | 7.6 | 35% | 47% | 65% | 78% | 82% |
| Both floors, 12+ pairs on sight, the rest level by level | 19.0 | 7.6 | 46% | 56% | 69% | 78% | 82% |
| Both floors, look at all, then most pairs first | 19.0 | 7.6 | 54% | 63% | 74% | 80% | 82% |

4qt (the reach is 86%):

| Order | HTRs to finish per DR | Same, on a DR with no solution | Found within 3 finishes | Within 5 | Within 10 | Within 20 | Within 40 |
|---|---:|---:|---:|---:|---:|---:|---:|
| No floors, by moves to HTR, ties at random | 1,536 | 1,638 | 18% | 24% | 33% | 42% | 52% |
| No floors, by moves to HTR, most pairs first (the baseline) | 1,536 | 1,638 | 22% | 29% | 39% | 49% | 60% |
| Rule bound only, by moves to HTR, most pairs first | 72.4 | 47.7 | 31% | 42% | 59% | 74% | 83% |
| Both floors, in random order | 22.7 | 6.8 | 36% | 49% | 68% | 81% | 86% |
| Both floors, level by level, most pairs first inside a level | 22.7 | 6.8 | 30% | 42% | 62% | 79% | 85% |
| Both floors, skeleton by skeleton (largest M first) | 22.7 | 6.8 | 34% | 47% | 65% | 82% | 86% |
| Both floors, 12+ pairs on sight, the rest level by level | 22.7 | 6.8 | 51% | 58% | 71% | 82% | 86% |
| Both floors, look at all, then most pairs first | 22.7 | 6.8 | 61% | 69% | 79% | 84% | 86% |

- **The floors turn hundreds of HTRs into a dozen or two,** and on a DR with no solution you're done after 6 to 8 finishes instead of never.
- **Most pairs first beats every order by length.** Going level by level inside the floors is no better than a random order.
- **Skeleton by skeleton costs nothing** against level by level, so the order of section 2 works as long as pairs decide inside it.
- **12+ pairs on sight** gets most of the gain without looking at everything first.

## 10. Skeletons: which first, how far

Share of skeletons that hold a within-goal HTR, by maximum penalty M. First the skeletons with the fewest quarter turns (· is under 60 skeletons):

| Maximum penalty M | 2qt | 3qt | 4qt |
|---|---:|---:|---:|
| 1 | · | 1% | 4% |
| 2 | · | 10% | 12% |
| 3 | 17% | 20% | 33% |
| 4 | 24% | 34% | 59% |
| 5 | 35% | 48% | 77% |
| 6 | 38% | 56% | 92% |
| 7 | 50% | 73% | 97% |
| 8 | 52% | 77% | · |
| 9 | 53% | · | · |

Then the skeletons with two more quarter turns:

| Maximum penalty M | 2qt | 3qt | 4qt |
|---|---:|---:|---:|
| 1 | 1% | 2% | 2% |
| 2 | 3% | 5% | 8% |
| 3 | 6% | 11% | 20% |
| 4 | 14% | 26% | 38% |
| 5 | 22% | 41% | 64% |
| 6 | 34% | 55% | · |
| 7 | 35% | · | · |

- **More room, more often.** The doc starts its walkthrough with the longer skeleton, "since DR Bounding works best with longer skeletons". A longer skeleton has a smaller M, so fewer of its HTRs pass the rule, but it's also the one that holds a within-goal HTR less often.
- **How far to go in a skeleton.** Level by level, both sides and all skeletons. The mutual info is the share within goal among the HTRs that pass the rule, times the number of DRs with a within-goal HTR at that level, per 1,000 DRs.

4qt:

| S+T exactly | HTRs per DR | Pass the rule | Pass both floors | Within goal, of those passing the rule | Within goal, of those passing both floors | Solvable DRs with a within-goal HTR here | Mutual info per 1,000 DRs |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | 27 | 3.7 | 2.5 | 5.8% | 9% | 15% | 7.0 |
| 1 | 262 | 17.4 | 7.9 | 4.4% | 10% | 45% | 15.7 |
| 2 | 1,093 | 45.9 | 11.3 | 3.1% | 13% | 65% | 15.9 |
| 3 | 2,656 | 90.6 | 13.0 | 2.4% | 17% | 76% | 14.7 |
| 4 | 3,833 | 123.0 | 12.7 | 2.2% | 22% | 70% | 12.4 |
| 5 | 3,913 | 119.4 | 7.1 | 2.2% | 36% | 51% | 8.8 |
| 6 | 3,107 | 86.1 | 3.6 | 2.0% | 48% | 27% | 4.3 |

3qt:

| S+T exactly | HTRs per DR | Pass the rule | Pass both floors | Within goal, of those passing the rule | Within goal, of those passing both floors | Solvable DRs with a within-goal HTR here | Mutual info per 1,000 DRs |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | 17 | 2.5 | 1.9 | 8.6% | 11% | 14% | 8.5 |
| 1 | 123 | 10.2 | 5.5 | 5.3% | 10% | 38% | 14.4 |
| 2 | 422 | 22.1 | 8.0 | 4.0% | 11% | 53% | 15.3 |
| 3 | 1,119 | 46.0 | 10.1 | 3.0% | 14% | 66% | 14.1 |
| 4 | 2,226 | 73.6 | 10.2 | 2.6% | 19% | 69% | 12.7 |
| 5 | 2,785 | 85.5 | 7.0 | 2.0% | 24% | 55% | 7.8 |
| 6 | 1,867 | 55.6 | 3.1 | 2.2% | 40% | 32% | 4.9 |

2qt:

| S+T exactly | HTRs per DR | Pass the rule | Pass both floors | Within goal, of those passing the rule | Within goal, of those passing both floors | Solvable DRs with a within-goal HTR here | Mutual info per 1,000 DRs |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | 10 | 1.7 | 1.2 | 6.8% | 9% | 11% | 4.2 |
| 1 | 55 | 5.0 | 3.1 | 5.6% | 9% | 30% | 9.1 |
| 2 | 154 | 9.4 | 3.9 | 4.2% | 10% | 37% | 8.7 |
| 3 | 415 | 19.4 | 6.0 | 3.6% | 12% | 56% | 10.9 |
| 4 | 901 | 33.2 | 6.2 | 2.7% | 15% | 61% | 9.1 |
| 5 | 1,185 | 38.8 | 4.3 | 2.2% | 20% | 51% | 6.3 |
| 6 | 1,060 | 34.8 | 2.9 | 2.0% | 24% | 33% | 3.6 |

The rule keeps about 1 HTR in 7 at S+T = 0 and 1 in 20 to 30 from S+T = 3 on. Of those that pass, 6–9% are within goal at S+T = 0, 2–4% from S+T = 2 on. The mutual info peaks at S+T = 3 for 2qt, 2 for 3qt and 2 for 4qt. Past that the HTRs multiply faster than the DRs they add.

## 11. NISS

Share of solvable DRs reached, and what a mid-skeleton NISS costs in finishes after both floors. The NISS is: do a route's moves through a quarter turn on normal, switch, and search the inverse from there to the same S+T.

| DR | S+T at most | Normal only | Normal and inverse | Plus NISS after the first qt (shortest routes) | Extra finishes per DR for that | Plus NISS after any qt (routes with ≤ 1 extra) | Extra finishes per DR for that |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2qt | 1 | 20% | 36% | 38% | 0.4 | 41% | 1.3 |
| 2qt | 2 | 35% | 56% | 59% | 0.7 | 63% | 2.7 |
| 2qt | 3 | 58% | 80% | 82% | 1.2 | 85% | 4.1 |
| 3qt | 1 | 27% | 43% | 46% | 1.0 | 54% | 3.8 |
| 3qt | 2 | 49% | 68% | 72% | 1.7 | 79% | 8.0 |
| 3qt | 3 | 74% | 87% | 88% | 2.7 | 92% | 12.1 |
| 4qt | 1 | 30% | 51% | 57% | 2.6 | 70% | 9.6 |
| 4qt | 2 | 61% | 79% | 82% | 5.1 | 90% | 20.1 |
| 4qt | 3 | 85% | 94% | 96% | 8.1 | 98% | 29.4 |

- **The inverse is the big one.** It finds the solutions whose first section is long, because on the inverse that section is the finish.
- **A NISS after the first quarter turn of a shortest route is cheap and adds a few points.** There are only one or two such routes per DR.
- **After later quarter turns, or from routes with 1 extra move, it adds more,** but from many more starting points: about 60 routes after the second quarter turn of a 4qt DR and 463 after the third.
- **Against going one level deeper on both sides.** After both sides at S+T ≤ 2, the next level reaches 24% / 18% / 15% more of the solvable DRs for 6.0 / 10.1 / 13.0 finishes per DR. NISS at S+T ≤ 2 (any quarter turn, routes with at most 1 extra) reaches 7% / 11% / 11% more for 2.7 / 8.0 / 20.1.

## 12. When to abandon

How often each signal comes up, and how often a within-goal solution exists all the same. *Finished* means every HTR that passes both floors.

| Signal | 2qt: share of DRs | 2qt: still has a solution | 3qt: share of DRs | 3qt: still has a solution | 4qt: share of DRs | 4qt: still has a solution |
|---|---:|---:|---:|---:|---:|---:|
| No HTR with S+T ≤ 2 passes the rule | 13.1% | 31% | 2.5% | 18% | 0.0% | · |
| No HTR with S+T ≤ 3 passes the rule | 3.6% | 3% | 1.9% | 3% | 0.0% | · |
| No HTR with S+T ≤ 3 passes both floors | 9.7% | 7% | 4.3% | 3% | 1.9% | 0% |
| Everything with S+T ≤ 2 finished, nothing within goal | 69.3% | 35% | 51.2% | 44% | 37.4% | 45% |
| Everything with S+T ≤ 3 finished, nothing | 56.2% | 19% | 38.2% | 25% | 25.4% | 19% |
| Everything with S+T ≤ 4 finished, nothing | 49.0% | 8% | 31.9% | 10% | 21.6% | 4% |
| Same with at most 1 extra move before 2qt, S+T ≤ 3 | 58.8% | 23% | 41.4% | 31% | 31.5% | 34% |
| Same, S+T ≤ 4 | 51.6% | 12% | 34.6% | 17% | 25.6% | 19% |

- **Before any search,** the subset is the first signal (section 3): a 0c3 has a 13 less than one time in five, a 4a2 2e has a 12 about as rarely.
- **Nothing passes the rule with S+T ≤ 3: a safe stop,** but it only comes up for about 1 DR in 30 at 2qt and 1 in 50 at 3qt, and never at 4qt. Example F is one; example G is one of the 3% where a solution exists anyway.
- **After the finishes** the numbers are what they are: stopping at S+T ≤ 3 gives up on a fifth to a third of the DRs you stop on.
- **On a DR with no solution** the whole of S+T ≤ 3 costs 5.7 / 7.6 / 6.8 finishes.

## 13. The meta

What the numbers above add up to, for one DR and one goal.

1. **Check the subset.** Drop the ones that rarely make the goal.
2. **List the skeletons on both sides,** two more quarter turns included, with M for each. Skip M ≤ 1. Take them in order of M, largest first.
3. **In a skeleton, go by S+T,** with at most one extra move before 2qt. For each HTR work out the rule bound at 1qt. If it's over the goal, don't execute it.
4. **Execute the ones that pass and count pairs.** With n moves left you need 16 − 4n. Below that, move on.
5. **Finish on sight** anything with 12 or more pairs. Keep the rest in a list.
6. **When a level is done, finish the list, most pairs first.**
7. **NISS** after the first quarter turn of each shortest route, same steps on the inverse.
8. **Stop** at S+T = 3 unless the DR is one you'd rather not leave. Section 12 says what you leave behind.

What that costs and finds, with everything looked at before finishing. A row is one kind of DR and one depth.

| DR | S+T at most | Solvable DRs it can reach | Routes to 2qt per DR | HTRs that pass the rule, on a DR with a solution | Finishes on a DR with no solution | Found within 5 finishes (most pairs first) | Within 10 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2qt | 2 | 54% | 29 | 17 | 3.3 | 42% | 49% |
| 2qt | 3 | 75% | 54 | 31 | 5.7 | 61% | 70% |
| 2qt | 4 | 88% | 78 | 54 | 7.7 | 71% | 81% |
| 3qt | 2 | 66% | 101 | 29 | 5.9 | 50% | 58% |
| 3qt | 3 | 82% | 160 | 52 | 7.6 | 63% | 74% |
| 3qt | 4 | 92% | 209 | 88 | 8.9 | 73% | 83% |
| 4qt | 2 | 74% | 330 | 48 | 5.8 | 56% | 65% |
| 4qt | 3 | 86% | 451 | 79 | 6.8 | 69% | 79% |
| 4qt | 4 | 94% | 519 | 121 | 7.3 | 79% | 87% |

The routes to 2qt are the part no floor shortens: tens for a 2qt DR, hundreds for a 4qt one at S+T ≤ 3. Everything after that is short.

## 14. Examples

Each scramble is a sequence of DR moves; apply it to a solved cube to get the DR. A `|` marks HTR. Solutions on the inverse are given as found there and as a normal solution.

**A. The doc's first walkthrough**, `U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2` (subset 2c3 6e, quarter turns 3, goal 13, optimal leave-slice 13).

- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): 133 HTRs. 27 pass the rule, 20 of those pass the pair floor, 1 is within goal.
- **First within-goal HTR:** number 6 in the baseline order, number 6 with both floors and most pairs first.
- **Within-goal solutions, cheapest first:**
  - on normal, `R2 B2 U' L2 B2 U L2 B2 D | B2 R2 D2 F2` (13): 3qt F-V skeleton of 6, S+T = 3 (1 before 2qt), 0 bad slices, rule +1, 6 pairs at HTR.
  - on inverse, `F2 U2 L2 F2 U' R2 B2 U' R2 B2 D | B2 R2` (13): 3qt F-D skeleton of 7, S+T = 4 (2 before 2qt), 0 bad slices, rule +1, 8 pairs at HTR (as a normal solution: `R2 B2 D' B2 R2 U B2 R2 U F2 L2 U2 F2`).
  - on normal, `U F2 R2 D2 L2 F2 U L2 F2 U' | F2 L2 B2` (13): 3qt H-H skeleton of 5, S+T = 5 (1 before 2qt), 1 bad slice, rule +3, 6 pairs at HTR.
- This is the first random scramble of the doc. None of its 13s is cheap: the F-V one, the 13 the doc finds first, has S+T = 3 and the H-H one 5, so only the F-V one is in reach here. It has 6 pairs with 4 moves left, a long shot on the card of section 7, which is why it's the sixth finish and not the first.

**B. A 4qt DR where the floors leave one obvious HTR**, `B2 L2 D' R2 D F2 D F2 D2 B2 R2 D R2 D' U'` (subset 2c4 2e, quarter turns 4, goal 14, optimal leave-slice 14).

- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): 1,205 HTRs. 51 pass the rule, 8 of those pass the pair floor, 1 is within goal.
- **First within-goal HTR:** number 136 in the baseline order, number 1 with both floors and most pairs first.
- **Within-goal solutions, cheapest first:**
  - on normal, `U2 F2 U' R2 B2 U2 B2 U' L2 U' R2 D | L2 B2` (14): 4qt R-D skeleton of 11, S+T = 1 (1 before 2qt), 0 bad slices, rule +1, 8 pairs at HTR.
  - on inverse, `B2 L2 U' B2 U F2 U L2 U2 L2 B2 D | B2 D2` (14): 4qt F-V skeleton of 9, S+T = 3 (2 before 2qt), 0 bad slices, rule +0, 12 pairs at HTR (as a normal solution: `D2 B2 D' B2 L2 U2 L2 U' F2 U' B2 U L2 B2`).
- The baseline order reaches the 14 after well over a hundred HTRs. With the floors there are 51 to look at and 8 to finish, and the one with 8 pairs and 2 moves left is the solution.

**C. Only the inverse has it cheaply**, `D B2 R2 D L2 D R2 D' B2 D' L2 R2 D2` (subset 4c3 2e, quarter turns 3, goal 13, optimal leave-slice 13).

- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): 704 HTRs. 47 pass the rule, 10 of those pass the pair floor, 1 is within goal.
- **First within-goal HTR:** number 20 in the baseline order, number 1 with both floors and most pairs first.
- **Within-goal solutions, cheapest first:**
  - on inverse, `U R2 F2 U R2 U B2 U' F2 D' | R2 L2 U2` (13): 5qt H-H skeleton of 9, S+T = 1 (1 before 2qt), 0 bad slices, rule +0, 8 pairs at HTR (as a normal solution: `U2 L2 R2 D F2 U B2 U' R2 U' F2 R2 U'`).
  - on normal, `U2 R2 L2 U L2 U R2 D' L2 D' R2 B2 D' |` (13): 5qt H-H skeleton of 9, S+T = 4 (3 before 2qt), 0 bad slices, rule +0, 16 pairs at HTR.
- On normal the only 13 needs 3 extra moves before 2qt. On the inverse it's a 1-extra variant of a skeleton with two more quarter turns.

**D. A mid-skeleton NISS**, `D2 R2 U' L2 B2 L2 R2 D2 F2 D' B2 U' B2` (subset 4c3 4e, quarter turns 3, goal 13, optimal leave-slice 13).

- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): 1,410 HTRs. 96 pass the rule, 32 of those pass the pair floor, 2 are within goal.
- **First within-goal HTR:** number 156 in the baseline order, number 2 with both floors and most pairs first.
- **Within-goal solutions, cheapest first:**
  - on normal, `B2 U B2 U L2 U2 F2 B2 L2 F2 D | L2 U2` (13): 3qt R-V skeleton of 8, S+T = 3 (0 before 2qt), 0 bad slices, rule +0, 12 pairs at HTR.
  - on inverse, `U2 L2 U' R2 F2 R2 L2 U2 F2 U' L2 D' | B2` (13): 3qt F-D skeleton of 9, S+T = 3 (0 before 2qt), 0 bad slices, rule +0, 12 pairs at HTR (as a normal solution: `B2 D L2 U F2 U2 L2 R2 F2 R2 U L2 U2`).
- **NISS:** `B2 U B2 U (U2 L2 D')` then `(F2 L2 F2 B2 U2 L2)`, the parts in brackets on the inverse, 13 moves.
- Both sides need S+T = 3 here. After `B2 U B2 U` on normal, a shortest route to 1qt, the inverse reaches HTR in 3 moves with nothing extra. The 6-move finish there is the long insertion, and on normal it sits in the middle of the solution.

**E. Only a skeleton with two more quarter turns**, `R2 D2 U L2 B2 D' L2 U' F2 D L2 U2` (subset 4b2 2e, quarter turns 2, goal 12, optimal leave-slice 11).

- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): 581 HTRs. 28 pass the rule, 11 of those pass the pair floor, 2 are within goal.
- **First within-goal HTR:** number 28 in the baseline order, number 1 with both floors and most pairs first.
- **Within-goal solutions, cheapest first:**
  - on inverse, `R2 U' R2 F2 U' B2 U' L2 U | R2 D2` (11): 4qt R-V skeleton of 8, S+T = 1 (1 before 2qt), 0 bad slices, rule +0, 12 pairs at HTR (as a normal solution: `D2 R2 U' L2 U B2 U F2 R2 U R2`).
  - on normal, `U2 L2 U' R2 U F2 D L2 F2 D | R2` (11): 4qt R-D skeleton of 8, S+T = 2 (1 before 2qt), 0 bad slices, rule +0, 12 pairs at HTR.
- Every within-goal solution of this 4b2 has four quarter turns. Both 11s sit one or two extra moves into an 8-move 4qt skeleton, with 12 pairs at HTR.

**F. Nothing passes the rule: abandon**, `D2 F2 L2 D F2 L2 D2 R2 D' B2 D2 L2 B2` (subset 4a2 4e, quarter turns 2, goal 12, optimal leave-slice 13).

- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): 428 HTRs. 0 pass the rule, 0 of those pass the pair floor, 0 are within goal.
- **Nothing within goal in reach.** At any depth: 556 HTRs, 0 pass the rule, 0 pass both floors, 0 are within goal.
- A 4a2 4e whose optimal leave-slice is 13. Not one HTR with S+T ≤ 3 on either side passes the rule bound for 12, so there's nothing to look at.

**G. Nothing passes the rule with S+T ≤ 3, and a 12 exists**, `D' B2 D2 F2 L2 B2 U' B2 D2 L2 F2 U2` (subset 4b2 4e, quarter turns 2, goal 12, optimal leave-slice 12).

- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): 92 HTRs. 0 pass the rule, 0 of those pass the pair floor, 0 are within goal.
- **Nothing within goal in reach.** At any depth: 8,884 HTRs, 168 pass the rule, 19 pass both floors, 2 are within goal.
- **Within-goal solutions, cheapest first:**
  - on inverse, `U' L2 U2 L2 B2 R2 D' | F2 U2 L2 F2 U2` (12): 2qt R-D skeleton of 3, S+T = 4 (0 before 2qt), 1 bad slice, rule +4, 6 pairs at HTR (as a normal solution: `U2 F2 L2 U2 F2 D R2 B2 L2 U2 L2 U`).
  - on normal, `U2 F2 L2 U2 F2 U F2 R2 B2 U2 B2 D |` (12): 2qt H-H skeleton of 4, S+T = 8 (0 before 2qt), 0 bad slices, rule +0, 16 pairs at HTR.
- The counterexample to abandoning on that signal: the 12s are there, but the cheapest needs S+T = 4 on the inverse.

**H. Within goal after splitting every pair it had at 2qt**, `L2 B2 D U2 L2 U' R2 F2 L2 B2 U' F2` (subset 2c3 4e, quarter turns 3, goal 13, optimal leave-slice 11).

- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): 694 HTRs. 82 pass the rule, 45 of those pass the pair floor, 8 are within goal.
- **First within-goal HTR:** number 18 in the baseline order, number 1 with both floors and most pairs first.
- **Within-goal solutions, cheapest first:**
  - on normal, `R2 B2 U' F2 D L2 B2 U' | R2 F2 B2 R2 B2` (13): 3qt F-D skeleton of 6, S+T = 2 (1 before 2qt), 0 bad slices, rule +0, 0 pairs at HTR.
  - on normal, `R2 F2 U' L2 D B2 R2 U' | R2 B2 L2 B2 L2` (13): 3qt F-D skeleton of 6, S+T = 2 (1 before 2qt), 1 bad slice, rule +4, 2 pairs at HTR.
  - on inverse, `F2 U F2 R2 L2 U F2 D' | R2 B2 L2 F2 R2` (13): 3qt F-D skeleton of 6, S+T = 2 (0 before 2qt), 1 bad slice, rule +4, 2 pairs at HTR (as a normal solution: `R2 F2 L2 B2 R2 D F2 U' L2 R2 F2 U' F2`).
- The first 13 above has 4 pairs at 2qt, keeps none of them through the trigger and lands on an HTR with 0 pairs and 5 moves left. Rare, but it happens. The 11s of this DR are the ordinary kind: `F2 D L2 F2 R2 B2 D R2 D | B2 L2` has 8 pairs at HTR and a 2-move finish.

**I. A finish that splits a pair**, `R2 U B2 D2 B2 R2 U' R2 D2 L2 U' F2 U` (subset 2c4 2e, quarter turns 4, goal 14, optimal leave-slice 13).

- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): 2,640 HTRs. 139 pass the rule, 56 of those pass the pair floor, 9 are within goal.
- **First within-goal HTR:** number 3 in the baseline order, number 1 with both floors and most pairs first.
- **Within-goal solutions, cheapest first:**
  - on normal, `L2 U B2 U2 L2 U B2 U F2 U | F2 U2 R2` (13): 4qt D-D skeleton of 10, S+T = 0 (0 before 2qt), 0 bad slices, rule +0, 8 pairs at HTR.
  - on normal, `L2 U' L2 U2 B2 U' B2 U F2 U | F2 U2 R2` (13): 4qt D-D skeleton of 10, S+T = 0 (0 before 2qt), 0 bad slices, rule +0, 8 pairs at HTR.
  - on inverse, `U F2 U R2 U' L2 U L2 U' L2 D' | B2 D2 L2` (14): 6qt D-D skeleton of 11, S+T = 0 (0 before 2qt), 0 bad slices, rule +0, 8 pairs at HTR (as a normal solution: `L2 D2 B2 D L2 U L2 U' L2 U R2 U' F2 U'`).
- The one to look at is `B2 U' L2 F2 U L2 U' B2 U' | F2 L2 U2 R2 B2` (14): 10 pairs at HTR and a 5-move finish, and every optimal finish splits some of them (6 of the 10 survive at best). This only shows up with 5 or more moves left.

**J. Deep on both sides**, `U F2 D2 L2 U2 R2 D' L2 D' L2 B2 R2 U'` (subset 4b2 4e, quarter turns 2, goal 12, optimal leave-slice 12).

- **In reach** (S+T ≤ 3, at most 1 extra move before 2qt, both sides): 85 HTRs. 6 pass the rule, 4 of those pass the pair floor, 0 are within goal.
- **Nothing within goal in reach.** At any depth: 11,563 HTRs, 395 pass the rule, 22 pass both floors, 2 are within goal.
- **Within-goal solutions, cheapest first:**
  - on normal, `U R2 B2 L2 U B2 U L2 F2 U2 R2 U |` (12): 4qt H-H skeleton of 6, S+T = 6 (3 before 2qt), 0 bad slices, rule +0, 16 pairs at HTR.
  - on inverse, `U' R2 U2 F2 L2 U' B2 U' L2 B2 R2 U' |` (12): 4qt H-H skeleton of 6, S+T = 6 (3 before 2qt), 0 bad slices, rule +0, 16 pairs at HTR (as a normal solution: `U R2 B2 L2 U B2 U L2 F2 U2 R2 U`).
- The 12s need S+T = 6 on normal and on inverse. Nothing within reach finds them; this is the kind of DR the abandon numbers are about.


## 15. The claims, checked

| Claim | Who | Result |
|---|---|---|
| "Tweaking the baseline by hand to minimize the difference with the computed optimal yields these improved rules, which give a correct lower bound 100% of the time, and are within 1 of the true lower bound 80% of the time." | Rodney Kinney, [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0) | **The lower bound holds** for leave-slice finishes in DR moves on all 663,552 HTR states. The 80% is against the sheet's penalties, which allow finishes that leave DR, and isn't rechecked here. Against leave-slice finishes in DR moves the rule is exact for 46 of the 216 cases and 1 under for 57 (section 5). |
| "There are wild departures. HTR for example! In HTR, pairs matter so little compared to other DR states" | Levi Gibson ([4 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1148362613500162228)) | **Holds** over all HTR states: the mean finish is 8.8 moves with 0 pairs and 8.4 with 8. Under a goal it's another matter: the pair floor removes most HTRs (section 6). |
| "In the standard meta, one rarely makes a long-ish insertion (such as a non-cancelling corner swap) in the middle of the skeleton, because there are too many possible insertions to consider, and the ones that actually help can't be identified just by looking at pairs formed." | Rodney Kinney, [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0), *HTR Search Meta* | **In line with section 8**: pairs at 2qt say little about which routes lead to a within-goal HTR (0.62 to 0.73 as a ranker). Long insertions weren't tested on their own. |
| "Worthwhile long insertions at 3qt are still best found via NISS, but in general there is no need to ever NISS mid-skeleton when using DR Bounding." | Rodney Kinney, [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0), *HTR Search Meta* | **Mostly.** After both sides at S+T ≤ 2, one more level reaches 24% / 18% / 15% more of the solvable DRs. NISS in the middle of a route reaches 7% / 11% / 11% more, and 3.0% / 3.3% / 3.5% if it's kept to the first quarter turn of each shortest route (section 11). |
| "Let's start with skeleton #2, since DR Bounding works best with longer skeletons" | Rodney Kinney, [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0), first random scramble | **Depends on what you want from it.** A longer skeleton has a smaller M, so the rule leaves less to finish. The within-goal solutions are more often in the skeleton with the larger M (section 10). |
| Pairs often have to be broken up after HTR | Section 2, question 5 | **Not at these goals**: 4% / 2% / 1% of within-goal HTRs. Example I is one. |
| Pairs often have to be broken up during the trigger | Section 2, question 5 | **Sometimes**: in 32% / 28% / 22% of within-goal HTRs, about half the rate of HTRs at large. Example H. |
| Forming pairs is a good way of telling apart variants with similar lower bounds | Section 2, question 5 | **Yes at HTR, weakly at 2qt** (section 8). |

Nothing checked here turned out wrong, so there is no errata page.

## 16. What this does not cover

- **Uniform DRs.** Real attempts reach DRs through EO and a trigger; the mix of subsets and of pairs differs.
- **DR moves only.** A finish that leaves the DR group can be shorter than the best leave-slice finish counted here.
- **Counts, not minutes.** A route to 2qt, a rule read, a look at HTR and a finish don't cost the same, and how fast a solver finds the setups that pass the rule isn't measured.
- **Depth.** The floors only help with HTRs you get to. Solutions with S+T of 5 or more on both sides stay out of reach by hand (example J).
- **The doc's NISS advice by subset** (convert 4a3 to 4b3; from 0c4, 4a4 and 4b4, NISS after the first qt and set up to 4b3) isn't tested subset by subset. Section 11 pools all 3qt and all 4qt DRs.
- **Other goals.** One goal per kind of DR. A looser goal lets more HTRs past both floors.

## Appendix: how it was computed, and what is proved in Lean

**The sample.** 2,000 uniformly random DRs for each of 2qt, 3qt and 4qt. 40 of the 2qt draws have 0c0 corners up to a turn of both layers and are left out. Of the 1,960, 2,000 and 2,000 DRs, 1,073, 1,427 and 1,586 have a within-goal solution, so a share of DRs carries about ±3 points (95%).

**Every HTR in reach.** For each DR, on normal and on inverse, every HTR with up to two quarter turns more than the minimum whose moves plus corner-case moves fit the goal: 66,178,100 HTRs in all. Each one gets its optimal leave-slice finish from the exact table of HTR states, its rule value, and its pairs at 2qt, 1qt and HTR. The case of an HTR is read the way the sheet lists it, on the inverse of the state the HTR lands on.

**Checks.**

- The best HTR of each side equals the optimal leave-slice length of the DR, for every solvable DR in the sample but 7: 5 of the 2qt DRs and 2 of the 3qt DRs have all their within-goal solutions four quarter turns past the minimum (section 4), and the search stops at two.
- A second search that prunes with the exact leave-slice table instead finds the same within-goal HTRs with the same totals (450 DRs, 96,774 solutions).
- Every solution printed on this page was replayed on an independent sticker model.

**Base rates** come from 20 million random DR states looked up in the exact table.

**The rule on all HTR states.** In each of the 216 cases, the shortest leave-slice finish over its 3,072 states is at least the corner moves plus the rule's value. That is all 663,552 HTR states.

**Lean** (project *PairFloor*, no library, on the cube model of [*Judging a DR by hand*](../judging-a-dr/); builds in about half a minute).

| Theorem | What it says |
|---|---|
| `pairs_move_ud` | U and D moves, quarter or half, keep the number of pairs. |
| `pairs_step` | One DR move changes the number of pairs by at most 4 if it's a side half turn, and not at all otherwise. |
| `pairs_of_lsSolved` | With the corners and the U/D edges solved there are 16 pairs. |
| `pair_floor` | If a sequence of DR moves solves the corners and the U/D edges of a state with p pairs, then 16 ≤ p + 4 × (its side half turns). |
| `pair_floor_length` | The same with the length of the sequence: a finish of n moves needs at least 16 − 4n pairs. |
| `pair_floor_full` | The same for a full solve. |

All of them are checked by Lean's kernel, with no compiled computation. Four examples in the same file show the floor is reached: `R2`, `R2 L2`, `R2 L2 F2`, `R2 L2 F2 B2`.

Not in Lean: the two refinements at HTR (10 pairs need 3 moves, 2 pairs need 5), which are exact counts over the 663,552 HTR states; that the pair count is the same on the inverse, which held on every state of the sample; and every percentage on this page.
