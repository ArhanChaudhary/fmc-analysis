# Judging a DR by hand: what the full BFS says

What you can read off a DR, how much each read says about the finish, and which lower bounds hold, measured on the whole DR group: I BFSed all 19,508,428,800 states, so nothing below is sampled.

November 2026. A name with a date is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs and sheets are listed with links at the end.

**This builds on** the bounding docs and tables people already use:

- **Levi Gibson's [DR Bounding](https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA)** and **Rodney Kinney's [Advanced DR Bounding [Beta]](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0)**: DR bounding by hand, which this study set out to push to 3qt, 4qt and 5qt (**How this started**, section 3). Levi's formula and the worked examples of both docs are checked here, and Rodney's NISS@1qt features are the basis of section 9.
- **Rodney Kinney's sheet [Adv DR Bounding](https://docs.google.com/spreadsheets/d/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY)**: the bounding rules against the 216 computed cases, checked in section 10.
- **FakeMMAP's 216-case tables**: the half-turn-only values ([FakeMMAP, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546077758189477989)), the HTR-breaking table ([FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546599572644696075)) and the sheet [OBL++](https://docs.google.com/spreadsheets/d/1kax7evfA85p_4ArXKO7si3FrCpj7PEeFwoz4GY5wRAE), all checked in section 10; and FakeMMAP's corner counts per qt.
- **Joba's optimal distribution for all 48 subsets** ([Joba, 17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406633631165714492)), matched here in every cell, and **Mallard** ([cubelib](https://github.com/Jobarion/cubelib)), whose table is built from the same 48 subsets.
- **wen's sheet [HTR better smh (v2)](https://docs.google.com/spreadsheets/d/1ZhulzHeNgv2Hiy4x9R1MzsMRlPlI-E8DRiHFJlPlboM)**: the corner subsets, with 4a3 and 4b3 swapping on inverse.
- **trangium's "true 2q bound"** ([trangium, 27 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487207920256024738)), taken to any qt in section 7.
- **Levi Gibson's sheet [Corner Solution Length x DR Finish length](https://docs.google.com/spreadsheets/d/14rZI1Nf84Og1jS8dN1MfT0sYhvdIWu9gPXkHDs1iVU4)**: sampled; Appendix B is the exact version.

**What this adds**: the exact numbers for the reads a solver can make by hand.

- **A guide per subset**: for each of the 12 corner subsets, how often it finishes in 10, 11 and 12, what to read, when to drop it for the finish you need, what not to conclude.
- **Every read against the exact finish**, for each finish you might need from 9 to 13: ranking, throwing away, plain rules with their price, what is proven.
- **What each read is worth**: subset, pairs, corner case on both sides, HTR length on both sides, corner length and E-slice parity, the last DR move.
- **The bounds people use, graded**: Levi's formula, trangium's 2q bound at any qt, HTR length, the parity bound. Which never fail, how often the others do.
- **What a computer can prove from the DR**: table lookups that prove "no 12" for most 4–5qt DRs and "no 11" for nearly all, and why no hand read gets there.
- **The 216 NISS@1qt cases, three ways**: FakeMMAP's and Rodney's tables checked with half turns, with DR moves and with any move.
- **A Lean proof** of the optimal finish of every DR state, so every stat here is a count over proven optimals.

**Terms**, as the server uses them. "Optimal" is the shortest finish in DR moves (U, D, R2, L2, F2, B2), and "in 11" means an optimal finish of 11 or less. Bad corners and edges are counted the way the server counts them, up to turning a layer: the Q in 2c**4** is the corner qt count, the 4e in 2c4 4e the number of bad edges, and 4c3 = 4a3 and 4b3 together (they swap on inverse), same for 4c4. *Pairs* are true pairs: corner and edge next to each other in the U or D layer, both touching stickers matching. Every count treats each DR state as equally likely.

**How to read it.** This is long because most of it is reference. You don't have to read it front to back.

- **Start with [section 1](#1-the-short-version)**, the short version: what is new, then what it confirms or corrects, one line each. If you read one thing after it, make it the table in [section 2](#2-what-id-do-per-subset): for each kind of DR it says how often it finishes short, what to look at, when to drop it, and what not to conclude. With five minutes more, [section 5](#5-how-much-can-a-read-tell-you) measures how much any read can tell you for the finish you need (10, 11, 12 or 13).
- **The [worked examples](examples.html)** go with it, to see it on real DRs: eleven DRs read step by step, then 100 scrambles with the DRs on the page and the answers folded away. **The [errata](errata.html)** list what the full search shows is wrong in the docs and sheets involved and in things said on the server, each with an example.
- **Everything from section 10 on** is checking and reference: the 216 cases, the proof, how it was computed, and eight appendices of tables to look things up in.

---

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | What is new, then what it confirms or corrects, one line each. |
| [2. What I'd do per subset](#2-what-id-do-per-subset) | **The reference to keep open.** For each of the 12 corner subsets: how often it finishes in 10, 11 and 12, what to read, when to drop it for the finish you need, what not to conclude. |
| [3. What people asked for](#3-what-people-asked-for) | How this started, the gap in the solvers' own words, the sixteen questions from the server that are answered here, and which finish matters. |
| [4. The data](#4-the-data) | What was computed, and what "optimal" and "in 11" mean. |
| [5. How much can a read tell you?](#5-how-much-can-a-read-tell-you) | Every read against the exact finish, for each finish you might need from 9 to 13: ranking, throwing away, plain rules with their price, what is proven. Zagros's two hunches. |
| [6. The reads, cheapest first](#6-the-reads-cheapest-first) | What each read is worth, with the tables: [6.1 Subset](#61-subset), [6.2 Pairs](#62-pairs), [6.3 Corner case, on both sides](#63-corner-case-on-both-sides), [6.4 HTR length on both sides](#64-htr-length-on-both-sides), [6.5 Corner length and E-slice parity](#65-corner-length-and-e-slice-parity), [6.6 The last DR move](#66-the-last-dr-move). |
| [7. Bounds people use, graded](#7-bounds-people-use-graded) | Levi's formula, trangium's 2q bound at any qt, HTR length, the parity bound. Which never fail, how often the others do. |
| [8. Leave slice, the slice, and width](#8-leave-slice-the-slice-and-width) | What the slice costs, and how many first moves are optimal. |
| [9. What a computer can prove from the DR](#9-what-a-computer-can-prove-from-the-dr) | Table lookups that prove "no 12" for most 4–5qt DRs and "no 11" for nearly all, and why no hand read gets there. |
| [10. The 216 NISS@1qt cases, three ways](#10-the-216-niss1qt-cases-three-ways) | FakeMMAP's and Rodney's tables checked with half turns, with DR moves and with any move. |
| [11. The proof, if you don't speak Lean](#11-the-proof-if-you-dont-speak-lean) | What is proven, how, and what you have to trust. |
| [12. How it was computed and checked](#12-how-it-was-computed-and-checked) | The programs, and what agreed with what. |
| [13. What this doesn't do](#13-what-this-doesnt-do) | Limits, and questions left open. |
| [Appendix A: all 48 subsets](#appendix-a-all-48-subsets) | Share, average, fastest and longest optimal, odds for 9 to 13, and what is proven per subset. |
| [Appendix B: odds by corner length and E-slice parity](#appendix-b-odds-by-corner-length-and-e-slice-parity) | For the big high-qt subsets. |
| [Appendix C: the 216 NISS@1qt cases](#appendix-c-the-216-niss1qt-cases) | Every case with its optimal for half turns, DR moves and any move. |
| [Appendix D: odds by true pairs, all 48 subsets](#appendix-d-odds-by-true-pairs-all-48-subsets) | Odds for 10, 11, 12 and 13 by number of pairs. |
| [Appendix E: the 46 corner cases](#appendix-e-the-46-corner-cases) | Layout, example scramble, corner solution lengths, odds for 10 to 13, and the both-sides tables. |
| [Appendix F: HTR length on both sides, all 48 subsets](#appendix-f-htr-length-on-both-sides-all-48-subsets) | Odds for 10 to 13 for every pair of HTR lengths. |
| [Appendix G: a scramble for every subset](#appendix-g-a-scramble-for-every-subset) | A longest state, and one that finishes in exactly its longer HTR, for each of the 48 subsets. |
| [Appendix H: every read at every target](#appendix-h-every-read-at-every-target) | Ranking and pruning power of each read, for a finish in 9, 10, 11, 12 or 13. |
| [Docs and sheets referred to](#docs-and-sheets-referred-to) | Links. |

---

## 1. The short version

The finishes that matter are 10 and 11, which is what an 11- or 12-move DR needs (why is under **Which finish** in section 3).

What is new here, in one line each:

- **Some DRs are dead on sight, no solving needed.** A 2c5 with the bad corners stacked on both sides never finishes in 12 (the fastest is 13). Stacked on one side and opposite on the other: no 11, 0.24% in 12. Together that's 19% of all 2c5. A 2c4 stacked on both sides: no 10, 0.06% in 11, 1.1% in 12 (the fastest is 11), as dead as a 5qt. A 4a2 2e with all four bad corners on one layer on both sides: no 12 at all. The fastest double-stacked 2c4 and 2c5 are in section 6.3.
- **A five-line prune list for an 11-move DR that needs no solving** (section 2) drops 8% of 1–2qt, 28% of 3qt and 81% of 4qt DRs and every 5qt one, for 0.68%, 6.0% and 36% of their finishes in 11. Over all DR states it drops 57% and keeps 92% of the 11s and 96% of the 10s. On 491 of 500 random scrambles (those with an EO-first DR of 10 or less), finishing every DR of 10 or less plus only the 11-movers the list keeps averages 20.05 with 353 DRs per scramble; finishing every 11-mover averages 20.04 with 733.
- **For a 10 or an 11, the subset does most of the pruning.** In 11: 10% of 1–2qt DRs, 4.6% of 3qt, 1.1% of 4qt, 0.24% of 5qt. In 10: 2.4%, 0.87%, 0.16%, 0.02%.
- **Still no clean yes/no: tseitsei89's "100% cases and 0% cases" don't exist at any target.** The subset explains 35% of the variance of the optimal, everything readable together 48%, and what's left has an sd of 0.78 moves. Zagros's hunch that corner case + HTR on both sides pins the optimal to ~0.25 moves: it's 0.80. Two 2c4 4e with the same corner case on both sides, 7 to HTR on both sides and the same corner length finish in 7 and in 16 (section 5).
- **The lower the target, the more the reads tell you, and the free reads tell the most.** Keep only the best-looking quarter of 4qt DRs, going by pairs and corner case, which need no solving. It holds 65% of the finishes in 12, 77% of those in 11 and 89% of those in 10. At 3qt: 52%, 63%, 74%. From 3qt up, pairs plus corner cases rank better than the two HTR lengths at every target from 10 up, and the HTR lengths on top add 1 to 7 points. At 1–2qt it's the other way round: HTR length is the best single read.
- **Plain rules, with their price.** Zagros's "9+ on both sides, toss" turned into a rule against your target T. The safe version drops every DR that is T−1 or more to HTR on both sides: for an 11 that's 10+, and it drops 8% of 3qt and 31% of 4qt DRs for 0.2% and 2.5% of the 11s. The aggressive version, T−2 or more, is Zagros's 9+ when you need an 11: it drops 28% and 67% and costs 5% and 20% of them. With no solving: dropping every DR without a pair drops 14% and costs 2–7% of the 11s.
- **Count true pairs and stop.** One more pair multiplies the odds of an 11 by 1.4 at 4a1, 1.7 at 2c4 and 1.9 at 2c5. A 2c4 with five or more pairs finishes in 11 sixteen times as often as one with none (6.8% against 0.43%). Adding pseudo-pairs and semi-pairs moves the sd left from 0.850 to 0.842. The pair count is the same on inverse for every DR state, so count once.
- **Inside a subset the corner case on both sides is a big read.** 2c4 runs from 0.92% / 5.6% / 26% (in 10 / 11 / 12) with the best layout on both sides to 0 / 0.06% / 1.1% with a stack on both. At 3qt stacked is the *best* layout; at 4qt and 5qt it's the worst. Two 2c4 cases with the same bad corners (0.48% / 3.1% / 16% and 0.38% / 2.4% / 13%) are told apart by the diagonals of the back face (section 6.3). In 4b2 (3-1) and 4c3 (4-0) two cases look the same, and only the optimal corner solution separates them.
- **The two guaranteed hand bounds wake up at low targets.** The longer HTR, and the corner solution with the right E-parity (the number of side turns in any finish has the parity of the E-slice: Rodney's fr-parity used on the whole finish). They prove almost nothing for a 12 (5% of 4qt DRs, 13% of 5qt). For a 10 they rule out half of 4qt and 80% of 5qt DRs.
- **trangium's 2q bound works at any qt, and from 3qt up it's as good as a true bound.** On each side: fewest half turns before a quarter turn lowers the qt count, plus the shortest HTR of the other side. A finish with extra quarter turns gets under it for 2.6% of 1–2qt DRs and 0.002% from 3qt up (section 7 has a scramble for each of the 13 subsets where it happens). At 3qt it rules out 19% of DRs for a 10 and 6% for an 11, more than the two proven bounds together.
- **Levi's formula, measured.** It bounds every finish with one quarter turn, as Levi's doc says. A finish with three is shorter for 11.7% of 4a1 4e, and for 2.5% when the formula says 12 or less. For 72 of the 432 cases of 4a1 4e (one in six) the shortest HTR is a 3qt one, and the formula wants the shortest 1qt length. Against the real leave slice (count quackula's question) it's +0.70 on average and too high 19.7% of the time. Examples in section 7.
- **How far off they all sit.** The guaranteed bounds you can compute by hand are on average four moves under optimal.
- **A last DR move you can turn the other way is worth 0.33 moves flat**, in every subset (Zagros's question). At 3qt it takes the share finishing in 11 from 4.6% to 7.5%.
- **Where the information is.** Rodney's NISS@1qt features read straight off the DR state give a bound at any qt with no skeleton: on HTR states with half turns only it *is* FakeMMAP's 216-case table, at the DR it has 6,350,400 cases. With the H-perm parity and the real colours added it's exact 44% of the time and within one 86% (Rodney's guess was about right), and it proves Rodney's 4a4 13-mover optimal from the DR alone. A computer that sees the corners exactly plus the edge colours proves "no 12" for 81% of 4qt and 95% of 5qt DRs, and "no 11" for 97% and 99%. Everything readable put together gets 24% and 45% of them under 1% for a 12. The gap is the corner–edge relation, which is what Rodney's NISS@1qt tracing looks at. No count of visible features replaces it.
- **Exact numbers that were guesses.** The shortest HTR at 1 to 5 corner qts is 1 / 3 / 5 / 7 / 9 on either side (Joba's safe bound took 1 / 2 / 4 / 6 / 8). Only four subsets ever need 18: 0c0 8e, 0c3 4e, 2c5 0e and 2c5 4e. The slice is free (finish = leave slice) for 73% of DRs, from 56% at 1–2qt to 85% at 5qt. A DR whose optimal is 10 or 11 has exactly one optimal first move three times in four. 0c3 is the worst subset on average (14.46), worse than 5qt, and 4a2 2e and 0e finish like a 2c4.
- **Questions from the server, answered exactly**: stats by bad corner position (Daichi, JTuu, wen), by pairs (Rodney, Levi), the normal × inverse HTR table (Zagros), the 4a1 4e bound against the real leave slice (count quackula), the cost of the slice and the width of a DR (JTuu), an invertible last move (Zagros), error stats for bounding (compLex), God's number per subset (compLex), optimal lengths of all corner cases (Evan).
- **Proven in Lean**: the optimal finish of every DR state (so every stat here is a count over proven optimals) and its maximum of 18, the HTR and corner-length-with-parity bounds, the 216 HT-only values, and the counterexample to Levi's formula.

What it confirms or corrects in the docs and sheets people use:

- **FakeMMAP's HTR-breaking table is right in 211 of 216 cells and one too high in 5.** Two of those are labelled 7 and are 6-movers, so "7 or less is proven optimal" doesn't hold for them. Rodney's "Adv DR Bounding" sheet's penalties are built on the same optimals, so the same five are one too high, plus one alg with R2 for F2. Rodney's rules stay a true lower bound in all 216. A state of each case is in section 10.
- **FakeMMAP's HT-only table is not a bound once other moves are allowed**, as FakeMMAP said: with U and D quarter turns 2 of the 216 values drop from 9 to 8 (the count is proven in Lean), with any face turn 66 drop (section 10).
- **OBL++**, collapsed to the 216 labels, matches on 140 of the 144 cases it covers and is one lower in four. nissy finds no 8 in any of the 3,072 states of each of those four, so 9 stands for the cases as labelled here.
- **Zagros's "4c3 that is 9+ on both sides I throw away"** drops half of all 4c3 and keeps 92% of the 10s, 83% of the 11s and 73% of the 12s. It does throw away real finds: one 9 to HTR on both sides finishes in 9 (section 6.4).
- **Zagros's "L + longest HTR predicts within ~1 move"** is true for 93.3% of DRs, but the subset alone does it for 91.3%.
- **Levi's "blocky 2c4s are way better"**: yes, the ×16 above.
- **Rodney's two worked examples** in the Advanced DR Bounding doc are optimal 13s, and Levi's example in the DR Bounding doc is right once the last DR move is turned the other way (section 9).
- **Checked and matching**: Joba's optimal distribution for all 48 subsets, in every cell; FakeMMAP's corner counts per qt; the 1,352 states at 18 that Reid gave (section 12).
- The errata page that goes with this doc has the rest: typos in Rodney's doc, and claims from the channels about the longest DR→HTR, which subsets reach 18 and where 16+ optimals live, each with a scramble.

---

## 2. What I'd do per subset

This table is the per-subset reference, so it's long. Read these first, they apply to every row.

- **Three numbers, like 0.23% / 1.6% / 9.1%**, are the shares of all DR states of that kind whose optimal finish, in DR moves, is 10 or less / 11 or less / 12 or less. Which one is yours depends on the DR: your solution is the DR length plus the finish (one less if the first finish move merges with the last DR move). A 9- or 10-move DR gets a look whatever it is, so the numbers that decide something are the first two: an 11-move DR needs a 10 or an 11.
- **0 means no state at all** finishes that fast. "<0.01%" means a few do.
- **For a 13**, and for every case not quoted here, the same numbers are in appendices A, D, E and F (Appendix E gives the corner cases with all edge counts together).
- **They are odds, not guarantees.** The only guarantees are the two bounds (no finish is shorter than the longer HTR, and none is shorter than the best corner solution with the right number of side turns) and the cells that say 0.
- **"Drop" means "spend your time somewhere else first".** It doesn't mean unsolvable, and with a short enough DR or nothing better on the page you come back to it.
- **No row says a subset is bad to *try*.** The rows say how often each kind finishes short and which reads change that.
- **Pairs and the corner case need no solving.** Count the pairs, recognise the corners on normal and on inverse. **HTR length and L do**: the numbers are for the true shortest HTR on each side and the optimal corner solution. If the HTR you found isn't the shortest, your DR is in a better cell than you think.
- **Pairs** are true pairs: corner and edge next to each other in the U or D layer, both touching stickers matching.
- **Edge count.** The second column splits every subset by its number of bad edges. In the third column a read is given per edge count wherever the edge count changes it, and the cell says so where it doesn't. *Where* the bad edges sit is not a read in this table: I only measured it through the HTR length.
- **Corner cases** are named by where the bad corners sit, counted up to turning a layer. "A qt goes straight to X" means some U or D quarter turn lowers the corner qt count right away, with no setup.
- Shares like "a third of 4c3" are of all DR states of that corner subset.

**The short version for an 11-move DR**, which needs a 10 or an 11. This is the last column of the table boiled down to what you can see without solving anything:

- **2c5, 4b5, 4c4, 0c3, 0c4**: drop it.
- **2c4**: keep it only if on both sides the bad corners are not stacked and a quarter turn takes them straight to 2c3 or 4b3, or if it has four or more pairs.
- **4c3**: keep it only if its 4a3 side is 2-2 with a quarter turn straight to 4b2, or if it has four or more pairs.
- **4a2**: with 4e, keep it if on at least one side the bad corners are 2-2 with the two pairs stacked or each on a diagonal. With 2e or 0e, keep it only if one side has each layer's pair on a diagonal (a quarter turn straight to 4a1).
- **4a1, 4b2, 2c3, 0c0**: keep.

What that does, counted over all DR states:

| DRs | Dropped | 10s lost | 11s lost | 12s lost | All of them: in 10 / 11 / 12 | What you keep: in 10 / 11 / 12 |
|---|---:|---:|---:|---:|---|---|
| 1–2qt (4a1, 4a2, 4b2) | 8% | 0.25% | 0.68% | 1.4% | 2.4% / 10% / 35% | 2.6% / 11% / 38% |
| 3qt (2c3, 4c3, 0c3) | 28% | 3.7% | 6.0% | 9.0% | 0.87% / 4.6% / 20% | 1.2% / 6.0% / 25% |
| 4qt (2c4, 4c4, 0c4) | 81% | 24% | 36% | 48% | 0.16% / 1.1% / 6.8% | 0.63% / 3.8% / 19% |
| 5qt (2c5, 4b5) | 100% | 100% | 100% | 100% | 0.02% / 0.24% / 2.1% | nothing is kept |
| **all DR states** | 57% | 3.8% | 7.8% | 14% | 0.74% / 3.6% / 15% | 1.7% / 7.6% / 29% |

Read it row by row, not from the last row. The last row counts every DR state once, and 54% of all DR states are 4qt or 5qt, so it mostly says what happens up there: 84% of what the list drops is 4qt or 5qt.

- **1–2qt**: drops 8%, loses 0.68% of the finishes in 11. At 1–2qt the list hardly prunes.
- **3qt**: drops 28%, loses 6.0% of the finishes in 11. What it keeps finishes in 11 6.0% of the time, against 4.6% for all of 3qt.
- **4qt**: drops 81%, loses 36% of the finishes in 11. If you'd skip 4qt anyway, read that the other way round: the 2c4s the list keeps are 19% of 4qt and hold 64% of its finishes in 11.
- **5qt**: all dropped. 0.24% of 5qt DRs finish in 11.
- **All DR states**: 57% dropped, 92% of the finishes in 11 and 96% of those in 10 kept.

On real scrambles the price is smaller still, because the short DRs carry most of the result. Over the 491 of 500 random scrambles that have an EO-first DR of 10 moves or less: finish every DR of 10 or less and every 11-mover, optimally, and the best solution averages 20.04 (733 DRs per scramble). Finish only the 11-movers the list keeps and it averages 20.05 (353 DRs). The tally is at the end of the examples page.

If you have the HTR lengths, do the 4c3 line as "9+ on both sides, toss" instead: it drops about as many and loses 17% of the 4c3 finishes in 11 instead of 28%.

The table, subset by subset:

| Subset | How it finishes: in 10 / 11 / 12 | What to read, and what each read changes | When to drop it, and what not to conclude |
|---|---|---|---|
| **0c0**<br>0.5% of all DRs<br>average 12.28 | Depends almost only on the bad edges.<br>0e: 64% / 90% / 99.2% (these are HTR states and their U D' turns).<br>2e: 11% / 38% / 80%.<br>4e: 4.5% / 18% / 53%.<br>6e: 0.93% / 5.8% / 27%.<br>8e: 3.0% / 13% / 39%. | **Pairs**, none against five or more.<br>2e: 3.5% / 21% / 67% against 17% / 46% / 86%.<br>4e: 2.1% / 11% / 40% against 12% / 34% / 74%.<br>6e: 0.34% / 3.1% / 19% with none, 1.8% / 8.6% / 35% with two.<br>**Longer HTR** adds little once you know the edge count.<br>2e, always 5 or 6: 14% / 42% / 82% and 11% / 36% / 79%.<br>4e, 5, 6 or 7: 6.9% / 23% / 59%, 4.7% / 18% / 52%, 4.0% / 17% / 53%.<br>6e, 7 or 8: 1.3% / 6.7% / 28% and 0.82% / 5.5% / 27%.<br>**Corners**: one case only, nothing to read.<br>**Parity**: L is 0–5, and the wrong E-parity costs +2 or more for three corner states in four, so check it before trusting a short corner solution.<br>For 6e and 8e, go for the setup to a quarter turn first (Rodney's examples in [Rodney, 23 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1563054901871902741)). | **Needing a 10 or an 11**: 6e is the weak one, 0.93% / 5.8% / 27%, and with no pairs 0.34% / 3.1% / 19%. 2e is worth it at any length.<br>**Needing a 12**: never because of the subset. 6e with no pairs is still 19%.<br>**Don't conclude** that "0" means no quarter turns: every 0c0 with bad edges needs two. The shortest 0c0 2e is `D F2 R2 F2 D`, solved by `D' F2 R2 F2 D'`. |
| **4a1**<br>2.9% of all DRs<br>average 12.42 | 4e: 6.4% / 21% / 53%.<br>2e: 2.3% / 12% / 42%.<br>0e: 0.85% / 5.1% / 24% (only 3% of 4a1).<br>Only 4e can be finished with one quarter turn. 2e and 0e need three. | **Pairs**, none against five or more.<br>4e: 2.5% / 11% / 38% against 20% / 49% / 84%.<br>2e: 0.65% / 5.2% / 27% against 8.4% / 28% / 69%.<br>**Corners**: four cases.<br>4e: they barely differ, from 5.6% / 19% / 50% to 7.6% / 23% / 56%.<br>2e: they do. All four on one layer (L 1–4): 3.7% / 16% / 50%. The L 4–7 case: 1.4% / 8.2% / 35%, and 0.22% / 3.1% / 22% with that case on both sides.<br>**Longer HTR**.<br>4e: 5 gives 20% / 49% / 81%, 6 gives 8.2% / 28% / 67%, 7 gives 3.3% / 15% / 47%, 8 gives 1.4% / 7.8% / 32%.<br>2e: 6 gives 4.9% / 20% / 59%, 7 gives 2.8% / 13% / 46%, 8 gives 1.3% / 7.7% / 34%.<br>**Levi's formula (4e only)**: shortest *1qt* HTR on normal + on inverse − 1. It bounds the finishes with one quarter turn. For one case in six the shortest HTR is a 3qt one, and the formula wants the 1qt length. A 3qt finish is shorter than the formula 11.7% of the time (2.5% when the formula says 12 or less). | **Needing a 10 or an 11**: 8 to HTR on the longer side is the weak cell at 4e and 2e alike (1.3% / 7.7% / 33%), and 0e as a whole. Everything else is a real chance: 7 on the longer side is still 14% for an 11.<br>**Needing a 12**: rarely. 4a1 0e is the weak one.<br>**Don't conclude** that 4a1 2e or 0e are bad DRs: 2e is one of the better subsets. Levi's formula doesn't apply to them, that's all.<br>**Don't forget** the 3qt finishes on 4e. When a 4a1 4e is very blocky and the formula still says 10+, look for one: `U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2` has formula 10 and a 3qt finish in 7 (`U B2 L2 F2 D F2 D`).<br>2e and 0e really need three quarter turns: `D F2 U' B2 F2 D'` (4a1 2e) is solved by `D F2 B2 U F2 D'`, and `U L2 R2 U L2 R2 U'` (4a1 0e) by `U R2 L2 U' R2 L2 U'`. |
| **4a2**<br>2.9% of all DRs<br>average 13.35 | 4e: 1.9% / 7.7% / 26%.<br>2e: 0.26% / 1.8% / 10%.<br>0e: 0.09% / 0.86% / 6.1%.<br>So 4a2 2e and 0e finish like a 2c4, not like a 2qt. | **Corners** carry the most. Best case: 2-2, each layer's pair on a diagonal, L 5–8, a qt goes straight to 4a1. Worst case: all four on one layer, L 8–11.<br>4e, best: 3.8% / 14% / 41%. Worst: 0.62% / 3.6% / 16%. Best on both sides: 6.8% / 20% / 53%. Worst on both sides: 0 / 0.30% / 4.4%.<br>2e, best: 0.84% / 4.7% / 21%. Worst: 0 / 0.17% / 2.7%. Best on both sides: 2.0% / 8.8% / 34%. Worst on both sides: 0 / 0 / 0.<br>**Pairs**, none against five or more.<br>4e: 0.75% / 4.8% / 21% against 4.4% / 14% / 37%.<br>2e: 0.03% / 0.55% / 4.9% against 0.66% / 4.5% / 19%.<br>**Longer HTR**.<br>4e: 7 gives 7.1% / 24% / 59%, 8 gives 2.3% / 11% / 36%, 9 gives 0.60% / 4.1% / 20%, 10 gives 0.14% / 1.5% / 10%, 11 gives 0 / 0.71% / 6.9%.<br>2e, almost always 9 or more: 9 gives 0.80% / 4.8% / 21%, 10 gives 0.07% / 1.0% / 7.9%, 11 gives 0 / 0.18% / 2.9%.<br>**Method**: 4a2 4e is where Levi's bounding and Rodney's rules work best. Use them. | **Needing a 10 or an 11**: 2e and 0e unless one side is the best corner case. With 4e, neither side 2-2 with the pairs stacked or on diagonals (0.16% / 1.5% / 8.8%). 10 or more to HTR on the longer side (52% of 4a2): 0.06% / 0.87% / 6.9%.<br>**Needing a 12**: 10 or more to HTR on both sides (15% of 4a2): 0 / 0.05% / 1.1%. The worst corner case on both sides, above all with 2e.<br>**Don't conclude** that 2qt means good. On average 4a2 finishes worse than 2c3 and 4b2: 1.1% / 4.8% / 18% against 1.3% / 6.7% / 28% and 2.2% / 10% / 36%. |
| **4b2**<br>11.4% of all DRs<br>average 12.68 | Flat across edges.<br>2e: 2.7% / 11% / 39%.<br>4e: 1.8% / 8.8% / 34%.<br>0e: 1.5% / 7.2% / 28%. | **Pairs** are the best read here, none against five or more.<br>All edge counts: 0.68% / 4.5% / 23% against 8.7% / 27% / 65%.<br>2e: 1.0% / 5.8% / 27% against 11% / 31% / 70%.<br>4e: 0.41% / 3.4% / 20% against 7.2% / 24% / 62%.<br>**Corners**: four cases, three looks.<br>2-2 with L 3–6, a qt goes straight to 4a1: 3.4% / 14% / 44%.<br>3-1: 2.1% / 9.8% / 36%. This is two cases that look the same, 2.5% / 11% / 40% and 1.7% / 8.4% / 33%; only the optimal corner solution separates them, 4 moves being the better one and 8 the worse.<br>2-2 with L 6–9: 1.3% / 7.0% / 30%.<br>Best on both sides: 4.8% / 17% / 50%. Worst on both sides: 0.61% / 4.2% / 21%.<br>A little higher with 2e than with 4e throughout.<br>**Longer HTR** has to be read with the edge count, because 4e HTRs run a move longer.<br>2e: 6 gives 4.0% / 15% / 48%, 7 gives 1.7% / 8.7% / 34%, 8 gives 0.85% / 5.0% / 24%.<br>4e: 7 gives 3.7% / 15% / 48%, 8 gives 1.2% / 7.4% / 33%, 9 gives 0.47% / 3.8% / 22%.<br>**Method**: Rodney's, as written. | **Needing a 10 or an 11**: no pairs (0.68% / 4.5% / 23%), or 8 and 9 to HTR (0.19% / 2.1% / 15%). Three or more pairs (17% for an 11) or 5 on the shorter side (17%) make it a fair shot.<br>**Needing a 12**: there is no dead corner of 4b2. The weakest HTR cells of any size are 7 and 8 with 2e (14%) and 8 and 9 with 4e (15%).<br>**Don't conclude** that a short HTR means a short finish. Example 10 in the examples file has a 4-move HTR, sits in a cell where 84% finish in 12, and is a 13. |
| **2c3**<br>15.2% of all DRs<br>average 12.92 | The edge count matters a lot.<br>2e: 2.5% / 12% / 42%.<br>4e: 1.3% / 6.4% / 27%.<br>6e: 0.47% / 3.2% / 17%.<br>0e: 0.16% / 1.7% / 12%.<br>8e: 0.13% / 1.3% / 9.6%.<br>(0e and 8e are 1% of 2c3 each.) | **Corners**: three cases. Stacked (one above the other), L 5–8, a qt goes straight to 4b2. Opposite corners of the cube, L 5–8, also straight to 4b2. Next to each other on one layer, L 6–9, needs a setup (half of all 2c3).<br>2e, stacked: 3.8% / 16% / 52%. Opposite: 2.7% / 12% / 44%. Adjacent: 1.8% / 9.0% / 36%.<br>4e, stacked: 2.0% / 9.4% / 36%. Opposite: 1.4% / 6.9% / 28%. Adjacent: 0.84% / 4.6% / 21%.<br>6e, stacked: 0.84% / 5.3% / 26%. Opposite: 0.57% / 3.7% / 19%. Adjacent: 0.23% / 1.9% / 12%.<br>Stacked on both sides: 5.4% / 21% / 59% with 2e, 2.9% / 13% / 44% with 4e, 1.5% / 8.3% / 35% with 6e.<br>Adjacent on both sides (a quarter of 2c3): 1.1% / 6.4% / 29% with 2e, 0.50% / 3.1% / 16% with 4e, 0.08% / 0.94% / 7.6% with 6e.<br>**Pairs**, none against five or more.<br>2e: 0.83% / 6.1% / 30% against 7.5% / 25% / 63%.<br>4e: 0.30% / 2.6% / 16% against 5.4% / 18% / 51%.<br>6e: 0.19% / 1.7% / 11% against 1.6% / 8.7% / 36%.<br>**Longer HTR**.<br>2e: 6 gives 4.3% / 17% / 52%, 7 gives 2.1% / 11% / 40%.<br>4e: 7 gives 2.0% / 9.3% / 35%, 8 gives 0.89% / 5.3% / 24%, 9 gives 0.27% / 2.3% / 14%.<br>6e: 8 gives 0.58% / 3.7% / 19%, 9 gives 0.26% / 2.3% / 14%.<br>**Parity**: for half of all 2c3 corner states the wrong E-parity costs +2, so the corner solution you like may be two moves short of reality.<br>**Method**: Rodney's. | **Needing a 10 or an 11**: 6e with adjacent corners on both sides (0.08% / 0.94% / 7.6%). 9 to HTR on the longer side (0.27% / 2.3% / 14% with 4e, 0.26% / 2.3% / 14% with 6e). No pairs with 4e or 6e. Keep 2e with stacked or opposite corners, and anything with five pairs.<br>**Needing a 12**: nothing is dead. The weakest cells of any size: 6e with adjacent corners on both sides (7.6%), 4e at 8 and 9 to HTR (9.2%), 6e at 9 and 9 (10%).<br>**Don't conclude** that stacked corners are bad. At 3qt stacked is the *best* layout. It's at 4qt and 5qt that stacked is the worst. |
| **4c3**<br>(4a3 and 4b3)<br>11.4% of all DRs<br>average 13.49 | Flat across edges.<br>4e: 0.35% / 2.3% / 12%.<br>2e: 0.35% / 2.2% / 12%.<br>0e: 0.57% / 3.6% / 17%. | **Corners** carry the most, and which 4a3 you have is the big one.<br>4a3 that is 2-2 with L 7–9 and a qt straight to 4b2 (two such cases): 0.75% / 4.5% / 22% and 0.62% / 3.6% / 18%.<br>4b3 that is 2-2 with a qt straight to 4a2: 0.50% / 2.8% / 13%.<br>4b3 that is 3-1 (a third of all 4c3): 0.29% / 2.0% / 11%.<br>4a3 with all four on one layer: 0.24% / 1.7% / 10%. Two cases that look the same: with an optimal corner solution of 8 it is the better one, 0.40% / 2.8% / 15%, with 10 the worse one, 0.07% / 0.68% / 5.1%.<br>4a3 with L 9–11: 0.05% / 0.47% / 3.6%.<br>Both sides, best pair of cases: 0.95% / 5.3% / 23%. Worst pair (11% of all 4c3): 0.01% / 0.29% / 3.0%.<br>**Pairs**: 0.07% / 0.89% / 6.9% with none, 1.5% / 7.1% / 27% with five or more.<br>**HTR on both sides**.<br>7 and 8: 2.6% / 10% / 33%.<br>8 and 8: 1.2% / 5.6% / 22%.<br>8 and 9: 0.41% / 3.0% / 16%.<br>9 and 9: 0.11% / 1.3% / 9.4%.<br>9 and 10: 0.01% / 0.44% / 5.0%.<br>10 and 10: 0 / 0.09% / 1.9%.<br>The same length is worth a little more with 4e than with 2e (longer side 9: 0.50% / 3.3% / 17% with 4e, 0.29% / 2.2% / 12% with 2e), because 4e HTRs run about a move longer.<br>Corners and pairs read the same at 2e and 4e. | **Needing a 10 or an 11**: Zagros's rule (9+ on both sides, toss) is a fair trade here. It drops half of all 4c3 and keeps 92% of the 10s and 83% of the 11s. What it drops is 0.06% / 0.76% / 6.4%. Also drop the 4a3 with L 9–11 and the worse 4-0. Worth keeping: a qt straight to 4b2 on the 4a3 side, four or more pairs (5.4% for an 11), or 8 or less on the shorter side.<br>**Needing a 12**: 10 on both sides, or 9 and 10 with nothing else going for it. The rule keeps 73% of the 12s, so there it costs a quarter of them.<br>**Don't conclude** that what the rule drops is dead: `U' L2 D' B2 U' B2 U L2 D` is 9 to HTR on both sides and finishes in 9. |
| **0c3**<br>1.4% of all DRs<br>average 14.46 | The worst subset on average, worse than 5qt.<br>4e (half of 0c3): 0.01% / 0.18% / 1.5%.<br>2e and 6e: 0.07% / 0.58% / 3.7%.<br>0e and 8e: 0.04% / 0.75% / 5.7%. | **Longer HTR** is the read, and it has to be read with the edge count.<br>4e: 11 (one in seven) gives 0 / 1.0% / 5.8%, 12 (most of them) gives 0 / 0 / 0.76%, 13 (one in seven) gives 0 / 0 / 0.<br>2e or 6e: 10 (two thirds) gives 0.06% / 0.67% / 4.2%, 11 (a third) gives 0 / 0.06% / 1.4%.<br>So an 11 is the best case with 4e and the worst with 2e or 6e.<br>**Corners**: two cases, both with no bad corners.<br>A qt goes straight to 4a2 (a third of 0c3): 0.15% / 0.97% / 5.3% with 2e or 6e, 0.04% / 0.40% / 2.5% with 4e.<br>Needs a setup: 0.03% / 0.39% / 2.9% with 2e or 6e, 0 / 0.07% / 0.96% with 4e.<br>**Pairs** barely move it.<br>2e: 0 / 0.05% / 1.3% with none, 0.19% / 1.3% / 5.9% with five or more.<br>4e: 0 / 0 / 0.62% and 0 / 0.41% / 2.2%.<br>**Parity**: the wrong E-parity always costs exactly +1. | **Needing a 10 or an 11**: always. The longer HTR is 10 or more for 99% of 0c3, so a 10 is all but ruled out before you look. For an 11 even the better cells are 1–3%: 2e or 6e with a qt straight to 4a2 is 0.97%, 2e with five pairs 1.3%, 2e or 6e at 9 and 10 to HTR 1.7%, 4e at 10 and 11 2.6%. 9 on the longer side reaches 4.3%, and that is one 0c3 in a hundred.<br>**Needing a 12**: by default. 0c3 4e with 12 or 13 on the longer side (six in seven of 0c3 4e) is at most 0.76%.<br>**Don't conclude** that no bad corners means good corners. |
| **2c4**<br>22.9% of all DRs, the most common subset<br>average 13.65 | 2e: 0.31% / 2.1% / 11%.<br>4e: 0.23% / 1.6% / 9.1%.<br>6e: 0.14% / 1.2% / 7.7%.<br>0e: 0.90% / 4.7% / 20%.<br>8e: 0.05% / 0.58% / 4.5%.<br>(0e and 8e are 1% of 2c4 each.) | **Corners first**, seven cases.<br>Next to each other on one layer with a qt straight to 2c3, two cases with the same bad corners, told apart by the diagonals of the back face (section 6.3 says how): 0.48% / 3.1% / 16% and 0.38% / 2.4% / 13%.<br>Opposite corners with a qt straight to 4b3 (L 8–10): 0.31% / 2.3% / 13%.<br>The other two non-stacked cases, which need a setup: 0.15% / 1.1% / 7.0% and 0.13% / 0.99% / 6.4%.<br>Stacked (one above the other) with a qt straight to 4b3: 0.13% / 1.1% / 7.0%. Stacked, needing a setup: 0.04% / 0.52% / 4.1%.<br>Best layout on both sides: 0.92% / 5.6% / 26%.<br>A stack on both sides: 0 / 0.06% / 1.1%.<br>This holds at every edge count: the best layout on both sides is 1.2% / 7.0% / 31% with 2e, 0.89% / 5.4% / 25% with 4e, 0.61% / 4.5% / 24% with 6e.<br>**Pairs**: 0.03% / 0.43% / 4.2% with none, 1.5% / 6.8% / 26% with five or more, about the same at 2e, 4e and 6e.<br>**HTR on both sides**.<br>7 and 8: 1.6% / 7.4% / 29%.<br>8 and 8: 0.72% / 4.2% / 20%.<br>8 and 9: 0.28% / 2.1% / 12%.<br>9 and 9: 0.06% / 0.79% / 6.1%.<br>9 and 10: <0.01% / 0.23% / 3.1%.<br>10 and 10: <0.01% / 0.04% / 0.94%.<br>Within a few points of this at 2e, 4e and 6e.<br>**Parity** (if the corner solutions are written down): for 2c4 4e, L of 11 or more is 0 / 0.17% / 1.8%, and L = 12 with an odd E-slice has no 12 at all. | **Needing a 10** (0.23% as a subset): it takes the best layout on both sides (0.92%), five pairs (1.5%) or 7 and 8 to HTR (1.6%) to get near 1 in 100.<br>**Needing an 11** (1.6% as a subset): under 1% with a stack that needs a setup (0.52%), 9 and 9 or worse to HTR (0.47%), or no pairs (0.43%). Worth it with a qt straight to 2c3 on both sides (4.3%), four or more pairs (4.7%), or 8 and 8 or better to HTR (5.4%).<br>**Needing a 12**: a stack on both sides (the fastest any of them finishes is 11: `U2 L2 D' F2 U' R2 U F2 D L2 U2`). 10 to HTR on both sides. No pairs and nothing else going for it.<br>**Don't conclude** that 2c4 is bad as a subset. The best layout on both sides is as good as an average 2c3 4e (0.92% / 5.6% / 26% against 1.3% / 6.4% / 27%), and 2c4 is where reading pays the most, because the spread inside it is the widest.<br>**Don't conclude** that 6e is a discard on its own: it's 0.14% / 1.2% / 7.7% against 0.23% / 1.6% / 9.1% for 4e. 8e is worse. |
| **0c4**<br>1.0% of all DRs<br>average 13.67 | Same average as 2c4 but fewer short finishes: 0.08% / 0.87% / 6.7% against 0.23% / 1.6% / 9.4%.<br>2e: 0.12% / 1.2% / 8.9%.<br>4e: 0.09% / 0.90% / 6.9%.<br>6e: 0.02% / 0.36% / 3.6%. | **Pairs** are the only read with much in it.<br>2e: 0 / 0 / 3.0% with none, 0.32% / 2.9% / 17% with five or more.<br>4e: 0 / 0.21% / 3.1% and 0.26% / 2.8% / 15%.<br>6e: 0.01% / 0.11% / 1.9% with none, 0.09% / 0.66% / 5.1% with two.<br>**HTR** is 9 or 10 on each side (11 only with 8e) and tells you little beyond the edge count: 9 and 9 gives 0.15% / 1.3% / 8.5%, 10 and 10 gives 0.03% / 0.51% / 4.6%, and with 6e it's always 10.<br>**Corners**: one case, L is always 9 or 10, and the wrong E-parity always costs +1. | **Needing a 10 or an 11**: always. Five pairs is the only thing that lifts it: 0.32% / 2.9% / 17% with 2e, 0.26% / 2.8% / 15% with 4e.<br>**Needing a 12**: 6e or 8e, or no pairs.<br>**Don't conclude** anything from the corners here, there's nothing to tell apart. |
| **4c4**<br>(4a4 and 4b4)<br>11.4% of all DRs<br>average 14.40 | Flat across edges.<br>4e: 0.02% / 0.21% / 1.8%.<br>2e: 0.02% / 0.17% / 1.5%.<br>0e: 0.01% / 0.13% / 1.2%. | **Corners**.<br>Best case (2-2, each layer's pair on a diagonal, L 9–10, a qt straight to 4a3): 0.08% / 0.63% / 4.3%.<br>The two worst (L 11–12): 0 / 0.03% / 0.58%.<br>Best pair of cases on both sides: 0.17% / 0.92% / 5.6%. Worst pair: 0 / 0 / 0.20%.<br>**Pairs**: <0.01% / 0.05% / 0.73% with none, 0.07% / 0.71% / 5.0% with five or more.<br>**Longer HTR**: 10 gives 0.06% / 0.53% / 3.5%, 11 (two thirds of 4c4) gives 0 / 0.09% / 1.2%, 12 gives 0 / 0 / 0.33%.<br>All of this reads the same at 2e and 4e. | **Needing a 10 or an 11**: always. With 11 or more on the longer side (three quarters of 4c4) a 10 is impossible and an 11 is 0.08%. The best single reads for an 11: 9 on the longer side (1.5%, but that is one 4c4 in a hundred), the best pair of corner cases (0.92%), five pairs (0.71%).<br>**Needing a 12**: by default. It takes a short DR *and* something going for it (five pairs, or 9 and 10 to HTR, or the best corners), and then it's about 5.0%. 11 to HTR on both sides: 0.44%.<br>**Don't conclude** from examples 2 and 9 in the examples file that 4c4 comes good. Those were rare outcomes. |
| **2c5**<br>7.6% of all DRs<br>average 14.33 | Flat across edges.<br>4e: 0.03% / 0.33% / 2.6%.<br>2e: 0.03% / 0.30% / 2.5%.<br>6e: 0.01% / 0.18% / 1.7%. | **Corners**.<br>Next to each other on one layer (half of 2c5): 0.05% / 0.45% / 3.4%.<br>Opposite corners: 0.01% / 0.20% / 1.9%.<br>Stacked: 0 / 0.03% / 0.62%.<br>Adjacent on both sides (a quarter of 2c5): 0.08% / 0.69% / 4.7%.<br>Stacked on one side, opposite on the other: 0 / 0 / 0.24%.<br>**Stacked on both sides: 0 / 0 / 0**, so never a 12 (the fastest is 13: `U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2`).<br>**Pairs**: 0 / 0.04% / 0.68% with none, 0.27% / 1.8% / 9.2% with five or more.<br>**Longer HTR**: 9 (2% of 2c5) gives 0.49% / 3.1% / 13%, 10 gives 0.05% / 0.51% / 4.0%, 11 gives 0 / 0.09% / 1.2%, 12 gives 0 / 0 / 0.28%.<br>**Parity**: this is where the parity bound does the most. At 5qt it proves "no 11" outright for 37% of DRs and "no 12" for 13%.<br>The reads are about the same at 2e, 4e and 6e, a little lower with 6e. | **Needing a 10 or an 11**: always. The exceptions are 9 on the longer side (3.1% for an 11, but that is one 2c5 in fifty) and five pairs (1.8%).<br>**Needing a 12**: by default, and at once with a stack on both sides, a stack plus opposite, or 11 to HTR on both sides (0.13%). Worth a look with a short DR and five pairs, or adjacent corners on both sides with 9 or 10 to HTR.<br>**Don't conclude** that "5qt, skip" loses nothing when a 13 is enough: one 2c5 in seven finishes in 13. |
| **4b5**<br>11.4% of all DRs<br>average 14.28 | Flat across edges.<br>4e: 0.01% / 0.19% / 1.8%.<br>2e: 0.02% / 0.23% / 2.0%.<br>0e: 0.02% / 0.22% / 2.0%. | **Pairs** are the only read that does anything: <0.01% / 0.03% / 0.52% with none, 0.15% / 1.2% / 7.7% with five or more.<br>**Corners**: two cases.<br>3-1 with a qt straight to 2c4 (two thirds): 0.02% / 0.25% / 2.2%.<br>2-2 with a qt straight to 4a4: <0.01% / 0.12% / 1.3%.<br>**HTR**: 9, 10 or 11 on each side. 9 and 9 gives 0.09% / 0.53% / 3.5%, 11 and 11 gives 0 / 0 / 0.43%.<br>The same at 2e and 4e. | **Needing a 10 or an 11**: always. Five pairs gets it to 1.2% for an 11 and nothing gets it further.<br>**Needing a 12**: by default. Unlike 2c5 there is no layout that kills it or saves it. A short DR with four or five pairs is the only case for it.<br>**Don't conclude** that 4b5 and 2c5 read the same way: 2c5 has the stacked-corner rule, 4b5 has nothing like it. |

On top of any row: a last DR move that can be turned the other way is worth a third of a move on average, in every subset, so read the DR both ways (example 3 in the examples file). At 3qt it takes the share finishing in 11 from 4.6% to 7.5%. And if a row's reads disagree with each other, that's normal: together they explain about half of what there is to know.

---

## 3. What people asked for

**How this started.** The question I started from: can Levi's and Rodney's DR bounding be pushed to 3qt, 4qt and 5qt DRs, so you can toss a DR because its bound is high instead of wasting time on it?

With a computer, yes. Look at part of the DR, tabulate the fewest moves that solve that part, and you have a lower bound at any qt with no skeleton. With the right table it proves "no finish in 12" for 59% of 5qt DRs and "no finish in 11" for 94%. That was the first version of this doc and it is now section 9. The trouble is the tables have millions of cases, so nobody can use them in an attempt, and the bar on the server is clear:

> "is the lower bound fast to determine by human methods? If it takes too long to figure out the lower bound, you can just as well try to actually solve the DR" ([tseitsei89, 13 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1416359895761944657))

> "I don't expect anyone to use the decision trees directly. I'm just hoping to use them to find the most important 2-3 features … then make some simple rules out of just those features" ([Rodney, 1 Jul 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1389481110181777478))

So this version asks the human question. Take what you can actually read off a DR (subset, pairs, corner case, HTR length on both sides, corner solution length, E-slice parity) and measure exactly what each one tells you about the finish.

The gap, in the words of the people who bound in real solves:

- Jay: bounding "isn't really equipped to handle higher qt stuff which is where optimal usually gets missed" ([Jay, 28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1311881154328133673)).
- Levi uses it at 2q and 3q. At 4q: "Too many variations unfortunately. It kinda works with 4q, but it is slower than just checking reductions to 2c3" ([Levi, 13 Feb 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1339747273902395507)). And: "If there are other metrics (i.e blocks, HTR patterns, etc) that you can bound 2q cases with that would be incredible" ([Levi, 12 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1371536829844689010)).
- Rodney: "+3 or lower penalties are really quite rare … That's what makes 4qt cases so intractable currently" ([Rodney, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546185406075244564)).
- tseitsei89: "Being able to quickly tell when a DR has a short finish would be a real holy grail" ([tseitsei89, 28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1466158543496544494)). tseitsei89's test for a good stat: "Optimally you would only have 100% cases and 0% cases" ([tseitsei89, 21 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1386074648424218745)).

And the specific questions, each with a section below:

| Asked | By | Where |
|---|---|---|
| Corner case + HTR on normal + HTR on inverse "can tell you the optimal solution with a standard deviation of like 0.25 moves"? | [Zagros, 4 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1490097940641878216) | §5 |
| Stats by optimal corner length and longest direct HTR; "predict the opt finish length within ~1 move"? | [Zagros, 25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1365341555308888114) | §5 |
| A square table, moves to HTR on both sides. "4c3 that is 9+ on both sides I throw away" | [Zagros, 10 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1470865840298655918) | §6.4 |
| "you won't get very clean stats from just the corner case plus bad edge count. You would need to break cases down by some kind of pair counts" | [Rodney, 4 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1490027292767027452) | §6.2 |
| "blocky 2c4s are way better than not-so-blocky 2c4s?" | [Levi, 28 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1366528885432258592) | §6.2 |
| "stats on just bad corner positions for each subset", good/bad parity, on both sides | [Daichi, 8 May 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1502289745143922790), [tseitsei89](https://discord.com/channels/1007840975726575667/1007841273111117924/1502290363916877954) | §6.3 |
| "stats on 4c3 that take 4a3 corner position/parity into account?" | [JTuu, 22 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1518725967948808223) | §6.3 |
| Average optimal of the 2c4 layouts: "double stack vs single stack vs no stack" | [wen, 24 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1563566658356908108) | §6.3 |
| "is there a doc with optimal lengths for all corner cases?" | [Evan, 23 Mar 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1485844126770532435) | Appendix E |
| "average difference between a 4a1 4e bound and the actual leave slice? And how likely it is to be +0, +1, +2" | [count quackula, 9 Jan 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1459279260824109322) | §7 |
| "publicly available statistics for the errors on bounding?" | [compLex, 27 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1377120894320906323) | §7 |
| trangium's "true 2q bound": how good is it, does it work at more qts? | [trangium, 27 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487207920256024738) | §7 |
| "probability distribution of +N to solve slice given #qt" | [JTuu, 21 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1286925282183483403) | §8 |
| "how does the optimal change from a pure DR vs. a DR in a solve where you have one move you can invert?" | [Zagros, 29 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487985615319601312) | §6.6 |
| The "width" of a DR | [JTuu, 30 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1488242984259686461) | §8 |
| "are god's numbers known for htr subsets?" | [compLex, 16 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406380780904517663) | Appendix A |

**Which finish.** A 9- or 10-move DR gets checked whatever it looks like. The DRs worth pruning are the 11- and 12-movers, and what they need is a finish in 10 or 11 (one more if the first finish move merges with the last DR move). So every table gives the share finishing in 10, 11, 12 and 13 or less, and the pruning is measured at each target from 9 to 13.

---

## 4. The data

- **Optimal finish of every DR state.** BFS of the group ⟨U, D, R2, L2, F2, B2⟩, all 19,508,428,800 states. "Optimal" means the shortest finish with those ten moves, same as nissy's `drudfin` and Joba's table. Average 13.58, max 18.
- **Optimal leave slice of every DR state.** Same thing ignoring the E-slice: fewest DR moves that solve corners and the eight U/D-layer edges. Average 13.29, and the max is 18 as well. (`U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'` needs 18 for the leave slice and 18 for the full finish.)
- **Every count treats each DR state as equally likely.** That is also close to how the DRs you reach are spread. On the EO-first DRs of at most 11 moves that cubelib finds on 10,000 random scrambles, every corner subset's share is within 0.4 points of the share here and its average optimal within 0.05 moves. What differs is the bad-edge mix inside a subset (section 13), so the edge-count cells are uniform-state numbers.
- Bad corners and edges are counted the way the server counts them, up to turning a layer. The Q in 2c**4** is the corner qt count. 4c3 = 4a3 and 4b3 together (they swap on inverse), same for 4c4. That's not how many qts the finish needs: 0c0 0e has states like `U D'` that need two, every 0c0 with bad edges needs two (`D F2 R2 F2 D`, 0c0 2e, solved by `D' F2 R2 F2 D'`), and 4a1 0e and 4a1 2e need three (`D F2 U' B2 F2 D'`, 4a1 2e, solved by `D F2 B2 U F2 D'`; `U L2 R2 U L2 R2 U'`, 4a1 0e, solved by `U R2 L2 U' R2 L2 U'`). Mallard keeps both numbers (`qt_corners` and `qt`). Mallard and Joba's files say `4c5` where wen's "HTR better smh (v2)" sheet and most people say `4b5`: same 48 of 420 cosets.
- The 48 subsets are double cosets of ⟨half turns, U D⟩ merged with their inverses, as KrzychXyz said ([KrzychXyz, 28 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1355272481208008824)), which is how Mallard builds its table (https://github.com/Jobarion/cubelib); the 29,400 one-sided cosets decide HTR length. Built that way, all 48 sizes match Joba's.
- Daichi's "90+% of 4b2 0e cases are 12-14 optimal" ([Daichi, 28 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487653636786880684)): 92.1%.
- "In 11" always means an optimal finish of 11 moves or fewer. A cell that says 0 means no state at all; "<0.01%" means a few.

How it was checked, and what's proven, is in sections 11 and 12.

---

## 5. How much can a read tell you?

**Which finish you need.** Your result is the DR length plus the finish (one less if the first finish move merges with the last DR move). A 9- or 10-move DR gets a look whatever it is, and a 12 from it is a good result. The DRs you want to prune are the 11- and 12-movers, and those need a 10 or an 11. So this section measures everything for each target from 9 to 13.

How rare each target is, as a share of all DR states of the kind:

| DRs | Share of all DRs | In 8 | In 9 | In 10 | In 11 | In 12 | In 13 | In 14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **0qt (0c0)** | 0.5% | 0.41% | 1.6% | 6.1% | 21% | 54% | 90% | 99.7% |
| **1–2qt (4a1, 4a2, 4b2)** | 17.1% | 0.10% | 0.51% | 2.4% | 10% | 35% | 79% | 98% |
| 4a1 | 2.9% | 0.25% | 1.1% | 4.4% | 16% | 47% | 89% | 99.9% |
| 4a2 | 2.9% | 0.04% | 0.21% | 1.1% | 4.8% | 18% | 52% | 89% |
| 4b2 | 11.4% | 0.08% | 0.44% | 2.2% | 10% | 36% | 83% | 99.8% |
| **3qt (2c3, 4c3, 0c3)** | 28.1% | 0.02% | 0.14% | 0.87% | 4.6% | 20% | 59% | 93% |
| 2c3 | 15.2% | 0.04% | 0.23% | 1.3% | 6.7% | 28% | 73% | 99% |
| 4c3 | 11.4% | <0.01% | 0.05% | 0.36% | 2.3% | 12% | 46% | 91% |
| 0c3 | 1.4% | 0 | <0.01% | 0.04% | 0.38% | 2.6% | 13% | 47% |
| **4qt (2c4, 4c4, 0c4)** | 35.2% | <0.01% | 0.02% | 0.16% | 1.1% | 6.8% | 30% | 74% |
| 2c4 | 22.9% | <0.01% | 0.03% | 0.23% | 1.6% | 9.4% | 39% | 85% |
| 0c4 | 1.0% | 0 | <0.01% | 0.08% | 0.87% | 6.7% | 36% | 89% |
| 4c4 | 11.4% | 0 | <0.01% | 0.02% | 0.19% | 1.6% | 11% | 50% |
| **5qt (2c5, 4b5)** | 19.0% | 0 | <0.01% | 0.02% | 0.24% | 2.1% | 14% | 57% |
| 2c5 | 7.6% | 0 | <0.01% | 0.03% | 0.28% | 2.3% | 14% | 55% |
| 4b5 | 11.4% | 0 | <0.01% | 0.02% | 0.21% | 1.9% | 14% | 58% |
| **all DRs** | 100% | 0.03% | 0.14% | 0.74% | 3.6% | 15% | 44% | 80% |

For a 10 or an 11 the subset has already done most of the pruning: one 4qt DR in 90 finishes in 11, one 5qt DR in 400. The reads matter most where the odds are still alive, at 1–3qt, and for finding the few high-qt DRs worth keeping. (The tables below go by corner-qt group from 1–2qt up. 0c0, half a percent of DR states, has its own row in section 2.)

**Two kinds of read.** Some need no solving: the subset, the true pairs, the corner case on normal and on inverse. Some need you to solve something: the shortest HTR on both sides, the optimal corner solution and its parity. The tables keep the two apart, because a read you have to work for costs time, and because the HTR numbers assume you found the *shortest* HTR. If yours is longer than the shortest, the DR looks worse than it is, and an HTR rule drops more than it should.

### Ranking

Rank the DRs of a qt group by what the read says, keep only the best-looking quarter, and count how many of the finishes in T you kept. With no information that's 25%. Each number is the best any rule based on that read could do.

| Corner qt | Finish needed | DRs that get there | No solving: subset alone | No solving: + pairs | No solving: + corner case on both sides | No solving: + pairs and corner cases | With solving: + HTR on both sides | With solving: + pairs, corner cases and HTR | With solving: + pairs, HTR, L and E-parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1–2qt | 9 or less | 0.51% | 48% | 71% | 59% | 77% | 87% | 93% | 95% |
| 1–2qt | 10 or less | 2.4% | 42% | 60% | 50% | 64% | 72% | 79% | 81% |
| 1–2qt | 11 or less | 10% | 36% | 49% | 42% | 52% | 57% | 62% | 63% |
| 1–2qt | 12 or less | 35% | 32% | 39% | 35% | 40% | 42% | 45% | 45% |
| 1–2qt | 13 or less | 79% | 28% | 30% | 29% | 30% | 30% | 31% | 31% |
| 3qt | 9 or less | 0.14% | 59% | 79% | 70% | 85% | 85% | 93% | 98% |
| 3qt | 10 or less | 0.87% | 54% | 68% | 63% | 74% | 73% | 81% | 83% |
| 3qt | 11 or less | 4.6% | 49% | 58% | 56% | 63% | 61% | 67% | 68% |
| 3qt | 12 or less | 20% | 43% | 48% | 48% | 52% | 49% | 53% | 54% |
| 3qt | 13 or less | 59% | 34% | 36% | 36% | 37% | 36% | 38% | 38% |
| 4qt | 9 or less | 0.02% | 51% | 88% | 89% | 99% | 99% | 100% | 100% |
| 4qt | 10 or less | 0.16% | 47% | 76% | 77% | 89% | 85% | 94% | 96% |
| 4qt | 11 or less | 1.1% | 44% | 64% | 67% | 77% | 71% | 80% | 80% |
| 4qt | 12 or less | 6.8% | 40% | 53% | 59% | 65% | 60% | 67% | 66% |
| 4qt | 13 or less | 30% | 36% | 42% | 48% | 51% | 47% | 52% | 50% |
| 5qt | 9 or less | <0.01% | 45% | 100% | 87% | 100% | 100% | 100% | 100% |
| 5qt | 10 or less | 0.02% | 38% | 83% | 64% | 93% | 84% | 100% | 100% |
| 5qt | 11 or less | 0.24% | 34% | 69% | 52% | 76% | 62% | 80% | 88% |
| 5qt | 12 or less | 2.1% | 31% | 55% | 44% | 61% | 48% | 63% | 68% |
| 5qt | 13 or less | 14% | 28% | 43% | 37% | 48% | 40% | 48% | 52% |

- **The lower the target, the more a read tells you.** At 4qt, pairs and corner cases put 65% of the 12s in the best-looking quarter, 77% of the 11s and 89% of the 10s. At 3qt: 52%, 63%, 74%. For a 13 nothing does much.
- **Most of it needs no solving.** From 3qt up, pairs plus the corner case on both sides rank better than the two HTR lengths do, at every target from 10 up. Adding the HTR lengths on top is worth 1 to 7 points.
- **At 1–2qt it's the other way round.** HTR length is the best single read there (72% of the 10s against 64% for pairs and corner cases), and at 1–2qt you find the HTR quickly anyway.

### Throwing away

The other direction: how many DRs can you drop and still keep 95% of the finishes in T?

| Corner qt | Finish needed | No solving: subset alone | No solving: + pairs | No solving: + corner case on both sides | No solving: + pairs and corner cases | With solving: + HTR on both sides | With solving: + pairs, corner cases and HTR | With solving: + pairs, HTR, L and E-parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1–2qt | 9 or less | 16% | 34% | 31% | 46% | 55% | 71% | 75% |
| 1–2qt | 10 or less | 14% | 23% | 23% | 32% | 37% | 48% | 51% |
| 1–2qt | 11 or less | 13% | 17% | 18% | 23% | 25% | 30% | 32% |
| 1–2qt | 12 or less | 12% | 13% | 14% | 16% | 17% | 19% | 20% |
| 1–2qt | 13 or less | 9% | 9% | 11% | 11% | 11% | 12% | 12% |
| 3qt | 9 or less | 22% | 45% | 42% | 57% | 61% | 72% | 79% |
| 3qt | 10 or less | 18% | 31% | 34% | 42% | 44% | 53% | 58% |
| 3qt | 11 or less | 15% | 23% | 28% | 31% | 31% | 38% | 40% |
| 3qt | 12 or less | 13% | 17% | 21% | 23% | 22% | 26% | 27% |
| 3qt | 13 or less | 10% | 12% | 15% | 15% | 14% | 16% | 17% |
| 4qt | 9 or less | 40% | 61% | 68% | 83% | 80% | 91% | 94% |
| 4qt | 10 or less | 36% | 44% | 53% | 65% | 61% | 74% | 77% |
| 4qt | 11 or less | 31% | 34% | 42% | 48% | 45% | 54% | 56% |
| 4qt | 12 or less | 22% | 27% | 32% | 36% | 31% | 38% | 39% |
| 4qt | 13 or less | 14% | 18% | 22% | 24% | 21% | 25% | 26% |
| 5qt | 9 or less | 14% | 86% | 68% | 95% | 97% | 99% | 100% |
| 5qt | 10 or less | 8% | 55% | 44% | 72% | 62% | 83% | 94% |
| 5qt | 11 or less | 7% | 29% | 27% | 44% | 33% | 50% | 66% |
| 5qt | 12 or less | 6% | 17% | 19% | 28% | 21% | 29% | 36% |
| 5qt | 13 or less | 6% | 11% | 14% | 17% | 15% | 18% | 22% |

For an 11 that's a third of the 1–2qt DRs, two in five at 3qt and more than half at 4–5qt. For a 12 it's a fifth to two in five.

Another way to cut it. Say a class of DRs is "under 1%" if at most one in a hundred of it finishes in T. Share of DRs in such classes, and in brackets the share of all the finishes in T those classes hold, which is what you lose by dropping them:

| Corner qt | Finish needed | No solving: subset alone | No solving: + pairs | No solving: + corner case on both sides | No solving: + pairs and corner cases | With solving: + HTR on both sides | With solving: + pairs, corner cases and HTR | With solving: + pairs, HTR, L and E-parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1–2qt | 9 or less | 91% (71%) | 87% (45%) | 87% (60%) | 87% (40%) | 91% (33%) | 89% (23%) | 90% (20%) |
| 1–2qt | 10 or less | 9% (1%) | 34% (9%) | 22% (4%) | 37% (7%) | 51% (10%) | 54% (7%) | 56% (7%) |
| 1–2qt | 11 or less | 0% (0%) | 3% (0%) | 5% (0%) | 6% (0%) | 8% (0%) | 10% (0%) | 12% (0%) |
| 1–2qt | 12 or less | 0% (0%) | 0% (0%) | 1% (0%) | 2% (0%) | 1% (0%) | 3% (0%) | 3% (0%) |
| 1–2qt | 13 or less | 0% (0%) | 0% (0%) | 0% (0%) | 0% (0%) | 0% (0%) | 0% (0%) | 0% (0%) |
| 3qt | 9 or less | 100% (100%) | 97% (68%) | 99% (94%) | 97% (66%) | 97% (71%) | 97% (54%) | 96% (45%) |
| 3qt | 10 or less | 60% (24%) | 77% (34%) | 73% (34%) | 74% (25%) | 71% (22%) | 77% (21%) | 77% (18%) |
| 3qt | 11 or less | 5% (0%) | 11% (1%) | 19% (2%) | 20% (2%) | 17% (1%) | 29% (2%) | 30% (2%) |
| 3qt | 12 or less | 0% (0%) | 0% (0%) | 1% (0%) | 1% (0%) | 3% (0%) | 5% (0%) | 6% (0%) |
| 3qt | 13 or less | 0% (0%) | 0% (0%) | 0% (0%) | 0% (0%) | 0% (0%) | 1% (0%) | 2% (0%) |
| 4qt | 9 or less | 100% (100%) | 100% (100%) | 100% (100%) | 100% (91%) | 100% (98%) | 100% (79%) | 100% (71%) |
| 4qt | 10 or less | 100% (100%) | 96% (65%) | 99% (93%) | 97% (58%) | 98% (78%) | 96% (51%) | 96% (49%) |
| 4qt | 11 or less | 35% (7%) | 61% (21%) | 60% (16%) | 69% (17%) | 68% (21%) | 71% (16%) | 69% (13%) |
| 4qt | 12 or less | 0% (0%) | 9% (1%) | 13% (1%) | 20% (1%) | 19% (2%) | 22% (1%) | 24% (1%) |
| 4qt | 13 or less | 0% (0%) | 0% (0%) | 0% (0%) | 0% (0%) | 0% (0%) | 0% (0%) | 3% (0%) |
| 5qt | 9 or less | 100% (100%) | 100% (100%) | 100% (100%) | 100% (100%) | 100% (100%) | 100% (100%) | 100% (34%) |
| 5qt | 10 or less | 100% (100%) | 100% (100%) | 100% (100%) | 100% (100%) | 100% (100%) | 100% (84%) | 100% (61%) |
| 5qt | 11 or less | 100% (100%) | 95% (67%) | 100% (100%) | 96% (64%) | 99% (90%) | 96% (62%) | 94% (47%) |
| 5qt | 12 or less | 0% (0%) | 32% (11%) | 17% (4%) | 36% (8%) | 18% (3%) | 38% (9%) | 45% (9%) |
| 5qt | 13 or less | 0% (0%) | 0% (0%) | 2% (0%) | 2% (0%) | 1% (0%) | 2% (0%) | 4% (0%) |

Read the row "4qt, 11 or less" like this. By subset alone 35% of 4qt DRs are under 1% (that's 4c4, 0c4 with four or more bad edges, and 2c4 8e). With pairs and corner cases it's 69%, and those 69% hold 17% of the 11s. For a 10, all of 4qt is under 1% as a group, and the reads work the other way: with pairs, corner cases and HTR they pick out the 4% of 4qt DRs that hold half of the 10s. For a 13 no read puts more than 4% of any qt group under 1%.

So tseitsei89's "100% cases and 0% cases" don't exist at any target. There is no feature count that sorts DRs into good and bad. What exists is a set of reads that each multiply your hit rate by two or three, more the lower your target, and a handful of corners of the tables that really are dead.

### Plain rules

The tables above are ceilings: a rule that reaches them needs a table of thousands of classes. These are rules you can carry in your head.

**HTR length against your target** (needs the shortest HTR on both sides). This is Zagros's "4c3 that is 9+ on both sides I throw away" ([Zagros, 10 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1470865840298655918)) moved to the finish you need, T. Each cell: share of the qt group the rule drops, and in brackets the share of the finishes in T it loses.

| Corner qt | Finish needed, T | Longer side more than T (proven, loses nothing) | Both sides T or more | Longer side T or more | Both sides T−1 or more | Longer side T−1 or more | Both sides T−2 or more |
|---|---|---:|---:|---:|---:|---:|---:|
| 1–2qt | 9 | 8.8% | 8.0% (0.02%) | 21% (1.2%) | 23% (1.2%) | 51% (11%) | 51% (8.0%) |
| 1–2qt | 10 | 3.2% | 2.5% (0) | 8.8% (0.24%) | 8.0% (0.19%) | 21% (3.1%) | 23% (2.7%) |
| 1–2qt | 11 | 0.15% | 0.34% (<0.01%) | 3.2% (0.08%) | 2.5% (0.01%) | 8.8% (0.78%) | 8.0% (0.63%) |
| 1–2qt | 12 | 0 | 0.01% (0) | 0.15% (<0.01%) | 0.34% (<0.01%) | 3.2% (0.32%) | 2.5% (0.08%) |
| 1–2qt | 13 | 0 | 0 | 0 | 0.01% (<0.01%) | 0.15% (0.02%) | 0.34% (0.02%) |
| 3qt | 9 | 23% | 28% (0.42%) | 53% (6.0%) | 57% (7.1%) | 80% (32%) | 83% (31%) |
| 3qt | 10 | 4.6% | 7.7% (0.04%) | 23% (1.5%) | 28% (1.9%) | 53% (13%) | 57% (14%) |
| 3qt | 11 | 2.2% | 2.3% (0) | 4.6% (0.14%) | 7.7% (0.24%) | 23% (3.8%) | 28% (4.6%) |
| 3qt | 12 | 0.37% | 0.98% (<0.01%) | 2.2% (0.07%) | 2.3% (0.07%) | 4.6% (0.39%) | 7.7% (0.66%) |
| 3qt | 13 | 0 | 0.01% (0) | 0.37% (<0.01%) | 0.98% (0.03%) | 2.2% (0.27%) | 2.3% (0.25%) |
| 4qt | 9 | 59% | 67% (2.8%) | 94% (38%) | 94% (46%) | 99.7% (89%) | 100% (100%) |
| 4qt | 10 | 26% | 31% (0.55%) | 59% (9.9%) | 67% (11%) | 94% (58%) | 94% (62%) |
| 4qt | 11 | 3.9% | 8.6% (0.07%) | 26% (1.9%) | 31% (2.5%) | 59% (19%) | 67% (20%) |
| 4qt | 12 | 0.15% | 0 | 3.9% (0.18%) | 8.6% (0.49%) | 26% (4.3%) | 31% (5.3%) |
| 4qt | 13 | 0 | 0 | 0.15% (0.01%) | 0 | 3.9% (0.57%) | 8.6% (1.5%) |
| 5qt | 9 | 97% | 100% (100%) | 100% (100%) | 100% (100%) | 100% (100%) | 100% (100%) |
| 5qt | 10 | 44% | 72% (20%) | 97% (74%) | 100% (100%) | 100% (100%) | 100% (100%) |
| 5qt | 11 | 5.9% | 10% (0) | 44% (13%) | 72% (38%) | 97% (85%) | 100% (100%) |
| 5qt | 12 | 0 | 0.41% (0) | 5.9% (0.80%) | 10% (1.2%) | 44% (23%) | 72% (51%) |
| 5qt | 13 | 0 | 0 | 0 | 0.41% (<0.01%) | 5.9% (1.8%) | 10% (3.1%) |

- **The first column is a proof**: no finish is shorter than the longer HTR. For a 12 it is next to nothing (0.15% of 4qt DRs). For a 10 it rules out a quarter of 4qt and 44% of 5qt.
- **"Both sides T−1 or more" is the safe rule.** For an 11 that's 10+ on both sides: it drops 31% of 4qt DRs and loses 2.5% of the 11s, and at 3qt it drops 8% and loses 0.2%.
- **"Both sides T−2 or more" is the aggressive one**, and for an 11 it is exactly 9+ on both sides: it drops 28% of 3qt and 67% of 4qt DRs and loses 5% and 20% of the 11s.
- A DR that is exactly T to HTR on the longer side can still finish in T. `U' L2 D' B2 U' B2 U L2 D` (4c3 4e) is 9 to HTR on both sides and finishes in 9, and Appendix G has such a state for every subset.

**Pairs against your target** (no solving). Share of the qt group dropped, and in brackets the share of the finishes in T lost:

| Corner qt | Finish needed | No pairs | One pair or none | Two pairs or fewer |
|---|---|---:|---:|---:|
| 1–2qt | 9 or less | 14% (2.8%) | 41% (10%) | 68% (30%) |
| 1–2qt | 10 or less | 14% (4.5%) | 41% (17%) | 68% (39%) |
| 1–2qt | 11 or less | 14% (6.5%) | 41% (23%) | 68% (48%) |
| 1–2qt | 12 or less | 14% (8.9%) | 41% (30%) | 68% (56%) |
| 1–2qt | 13 or less | 14% (12%) | 41% (37%) | 68% (64%) |
| 3qt | 9 or less | 14% (1.4%) | 41% (7.6%) | 68% (22%) |
| 3qt | 10 or less | 14% (3.2%) | 41% (14%) | 68% (34%) |
| 3qt | 11 or less | 14% (5.4%) | 41% (21%) | 68% (44%) |
| 3qt | 12 or less | 14% (7.9%) | 41% (28%) | 68% (53%) |
| 3qt | 13 or less | 14% (11%) | 41% (35%) | 68% (62%) |
| 4qt | 9 or less | 14% (0.48%) | 41% (3.6%) | 68% (13%) |
| 4qt | 10 or less | 14% (1.6%) | 41% (9.1%) | 68% (24%) |
| 4qt | 11 or less | 14% (3.7%) | 41% (16%) | 68% (36%) |
| 4qt | 12 or less | 14% (6.2%) | 41% (23%) | 68% (47%) |
| 4qt | 13 or less | 14% (9.0%) | 41% (31%) | 68% (56%) |
| 5qt | 9 or less | 14% (0) | 41% (0) | 68% (3.3%) |
| 5qt | 10 or less | 14% (0.18%) | 41% (2.9%) | 68% (14%) |
| 5qt | 11 or less | 14% (2.0%) | 41% (9.3%) | 68% (25%) |
| 5qt | 12 or less | 14% (3.9%) | 41% (16%) | 68% (37%) |
| 5qt | 13 or less | 14% (6.6%) | 41% (24%) | 68% (49%) |

Pairs are spread the same way in every qt group, so each rule drops the same share everywhere. What changes is the price: dropping the DRs with no pairs costs 2–7% of the 11s, dropping one pair or none costs 9–23%.

The corner-case rules are per subset. They are in section 2 and section 6.3.

**What is proven at each target.** Two bounds hold for every finish and can be worked out by hand: the longer HTR, and the best corner solution with the right E-parity (section 6.5). Share of DRs for which they prove there is no finish in T, next to two of the computer tables of section 9:

| Corner qt | Finish needed | DRs with no such finish | Longer HTR proves it | Corner length with parity proves it | Either one | Setup + HTR says no (not a proof: share of the finishes in T it is wrong about) | NISS@DR table | Everything visible |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1–2qt | 9 or less | 99.5% | 8.8% | 4.2% | 10% | 50% (5.9%) | 88% | 98% |
| 1–2qt | 10 or less | 98% | 3.2% | 1.4% | 3.8% | 32% (6.6%) | 57% | 90% |
| 1–2qt | 11 or less | 90% | 0.15% | 0.23% | 0.37% | 16% (5.2%) | 16% | 66% |
| 1–2qt | 12 or less | 65% | 0 | 0 | 0 | 6.5% (3.3%) | 3.8% | 24% |
| 1–2qt | 13 or less | 21% | 0 | 0 | 0 | 2.4% (1.9%) | 0.74% | 3.8% |
| 3qt | 9 or less | 99.9% | 23% | 29% | 37% | 42% (0.15%) | 95% | 99.5% |
| 3qt | 10 or less | 99.1% | 4.6% | 12% | 13% | 19% (0.03%) | 77% | 97% |
| 3qt | 11 or less | 95% | 2.2% | 2.5% | 3.6% | 6.2% (0.01%) | 37% | 84% |
| 3qt | 12 or less | 80% | 0.37% | 0.71% | 1.0% | 1.7% (0) | 9.2% | 49% |
| 3qt | 13 or less | 41% | 0 | 0 | 0 | 0.24% (<0.01%) | 2.1% | 13% |
| 4qt | 9 or less | 99.9% | 59% | 72% | 78% | 75% (0) | 99.6% | 99.9% |
| 4qt | 10 or less | 99.8% | 26% | 48% | 51% | 42% (0) | 96% | 99.6% |
| 4qt | 11 or less | 99% | 3.9% | 21% | 22% | 19% (0.16%) | 75% | 97% |
| 4qt | 12 or less | 93% | 0.15% | 5.0% | 5.1% | 2.6% (0.03%) | 34% | 81% |
| 4qt | 13 or less | 70% | 0 | 0 | 0 | 0.10% (<0.01%) | 5.2% | 41% |
| 5qt | 9 or less | 99.9% | 97% | 95% | 99.5% | 97% (0) | 99.9% | 99.9% |
| 5qt | 10 or less | 99.9% | 44% | 73% | 80% | 44% (0) | 99.6% | 99.9% |
| 5qt | 11 or less | 99.8% | 5.9% | 37% | 38% | 5.9% (0) | 94% | 99.4% |
| 5qt | 12 or less | 98% | 0 | 13% | 13% | 0 | 59% | 95% |
| 5qt | 13 or less | 86% | 0 | 1.2% | 1.2% | 0 | 7.9% | 66% |

For a 12 the hand bounds prove next to nothing below 5qt. For a 10 they rule out half of the 4qt DRs and 80% of the 5qt ones, and for an 11 a fifth and 38%. So the lower your target, the more a guaranteed bound is worth working out, on the high-qt DRs where it bites.

The setup + HTR bound of section 7 (trangium's 2q bound taken to any qt) is not a proof, because a finish with extra quarter turns can get under it. From 3qt up that almost never happens: it is wrong about 0.2% of the finishes in T at most. It is the hand bound that does something at 3qt, where it rules out 19% of the DRs for a 10 and 6% for an 11, more than the two proven bounds together. At 1–2qt it rules out a third of the DRs for a 10 and a sixth for an 11, and is wrong about 5–7% of those finishes.

Appendix H has every read at every target with more cut-offs (best 10%, 25%, 50%; keeping 90%, 95%, 99%).

### Scatter

The same thing without a target: how much scatter is left in the optimal once you know the read (sd, in moves).

| What you know | Needs solving | sd left |
|---|---|---:|
| nothing | | 1.09 |
| subset | no | 0.88 |
| + true pairs | no | 0.85 |
| + corner case on both sides | no | 0.83 |
| + pairs and corner cases | no | 0.80 |
| + HTR length on both sides | yes | 0.82 |
| + corner case and HTR on both sides | yes | 0.80 |
| + corner length L and E-parity | yes | 0.83 |
| + pairs, corner cases and HTR | yes | 0.78 |
| + pairs, HTR, L and E-parity | yes | 0.78 |
| *the optimal leave slice (for scale, you can't read this)* | | 0.43 |

**Zagros's two hunches.**

- *Corner case + HTR on both sides gives the optimal to ~0.25 moves* ([Zagros, 4 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1490097940641878216)). The sd left is 0.80 over all DRs. Adding pairs makes it 0.78.
- *L + longest HTR predicts within ~1 move* ([Zagros, 25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1365341555308888114)). True, 93.3% of DRs are within one move of the typical value for their (subset, L, longer HTR). But 91.3% are within one move of the typical value for their subset alone. The finish just doesn't vary much inside a subset.

A pair that shows what the first hunch is up against. Both are 2c4 4e, with the same corner case on normal and on inverse, 7 to HTR on both sides, and the same corner length (7):

    D F2 U' F2 D B2 D'                                 // optimal 7
    D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'      // optimal 16

---

## 6. The reads, cheapest first

### 6.1 Subset

The baseline, and still the biggest single piece of information. Appendix A has all 48 with average, share finishing in 9 to 13, and the fastest and longest optimal in each (God's number per subset, which compLex asked about). The longest, in DR moves: 18 for 0c0 8e, 0c3 4e, 2c5 0e and 2c5 4e, 17 or 16 for most others, 13 for 0c0 0e. One of each 18:

    F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'      // 0c0 8e
    F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'   // 0c3 4e
    U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'      // 2c5 0e
    R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'  // 2c5 4e

Appendix G has a longest one for every subset.

The shortest possible HTR by corner qt:

| Corner qt | Shortest HTR | A state with exactly that on both sides |
|---:|---:|---|
| 1 | 1 | `D` |
| 2 | 3 | `D B2 D'` |
| 3 | 5 | `D' B2 D' B2 D'` |
| 4 | 7 | `D B2 D' B2 D B2 D'` |
| 5 | 9 | `U' L2 U R2 U' L2 U R2 D` |

Joba took 1 / 2 / 4 / 6 / 8 as a safe lower bound ([Joba, 13 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1349876840914751578)); the exact floor is one higher from 2qt up, on either side.

### 6.2 Pairs

Count the true pairs: a corner and an edge next to each other in the U or D layer with both touching stickers matching (16 places to look). This is the read that costs nothing, and it works at every qt.

Share of each corner subset finishing in 10, 11 and 12 or less, by number of true pairs:

| Corners | Finish in | 0 pairs | 1 | 2 | 3 | 4 | 5 or more |
|---|---|---:|---:|---:|---:|---:|---:|
| 4a1 | 10 or less | 1.6% | 2.0% | 3.9% | 5.2% | 9.6% | 15% |
| 4a1 | 11 or less | 8.2% | 10% | 15% | 20% | 28% | 39% |
| 4a1 | 12 or less | 33% | 38% | 47% | 56% | 65% | 77% |
| 4b2 | 10 or less | 0.68% | 0.99% | 1.7% | 2.8% | 4.6% | 8.7% |
| 4b2 | 11 or less | 4.5% | 6.0% | 8.8% | 13% | 18% | 27% |
| 4b2 | 12 or less | 23% | 28% | 35% | 44% | 53% | 65% |
| 2c3 | 10 or less | 0.32% | 0.54% | 0.96% | 1.7% | 2.8% | 5.9% |
| 2c3 | 11 or less | 2.6% | 3.9% | 5.8% | 8.6% | 13% | 20% |
| 2c3 | 12 or less | 16% | 21% | 26% | 34% | 42% | 54% |
| 4c3 | 10 or less | 0.07% | 0.14% | 0.30% | 0.41% | 0.85% | 1.5% |
| 4c3 | 11 or less | 0.89% | 1.3% | 2.1% | 2.8% | 4.3% | 7.1% |
| 4c3 | 12 or less | 6.9% | 8.7% | 11% | 15% | 19% | 27% |
| 2c4 | 10 or less | 0.03% | 0.06% | 0.13% | 0.27% | 0.51% | 1.5% |
| 2c4 | 11 or less | 0.43% | 0.75% | 1.2% | 2.0% | 3.3% | 6.8% |
| 2c4 | 12 or less | 4.2% | 5.9% | 8.3% | 12% | 17% | 26% |
| 4c4 | 10 or less | <0.01% | <0.01% | 0.01% | 0.01% | 0.06% | 0.07% |
| 4c4 | 11 or less | 0.05% | 0.08% | 0.16% | 0.21% | 0.43% | 0.71% |
| 4c4 | 12 or less | 0.73% | 0.95% | 1.4% | 2.0% | 2.9% | 5.0% |
| 2c5 | 10 or less | 0 | <0.01% | <0.01% | 0.02% | 0.05% | 0.27% |
| 2c5 | 11 or less | 0.04% | 0.08% | 0.15% | 0.33% | 0.63% | 1.8% |
| 2c5 | 12 or less | 0.68% | 1.1% | 1.7% | 2.9% | 4.7% | 9.2% |
| 4b5 | 10 or less | <0.01% | <0.01% | <0.01% | 0.02% | 0.05% | 0.15% |
| 4b5 | 11 or less | 0.03% | 0.05% | 0.13% | 0.23% | 0.49% | 1.2% |
| 4b5 | 12 or less | 0.52% | 0.85% | 1.5% | 2.4% | 4.1% | 7.7% |
| share of all DRs | | 14% | 27% | 27% | 18% | 9% | 5% |

Each pair is worth about 0.15 moves of average optimal. What that does to the odds depends on how rare the finish is. One more pair multiplies the odds of a 12 by 1.2 at 4a1, 1.4 at 2c4 and 1.6 at 2c5. For an 11 it's 1.4, 1.7 and 1.9, and for a 10 at 4a1 and 2c4, 1.6 and 2.1. So pairs matter more the lower your target and the higher the qt.

Levi is right about blocky 2c4s: for an 11, from 0.43% with no pairs to 6.8% with five or more, 16 times as often. The same step is worth ×5 at 4a1, ×8 at 2c3 and ×40 at 2c5. Appendix D has all 48 subsets, for 10, 11, 12 and 13.

On Rodney's finer split: I also counted pseudo-pairs (both stickers opposite), side semi-pairs and top semi-pairs, defined as in Rodney's message. Knowing all four counts instead of just the true pairs moves the sd left from 0.850 to 0.842. Pairs with E-slice edges add even less. So count true pairs and stop.

You don't need to count again on the inverse scramble: a block stays a block, so the number of true pairs is the same on both sides for every DR state.

### 6.3 Corner case, on both sides

This is what Daichi, JTuu and wen asked for. There are 46 corner cases once you merge rotations, mirrors and turning a layer. Inside a corner subset they are *not* equally good, and since the corner case on inverse is a different one, there are two reads.

How to read the tables:

- "A qt takes it straight to" means some U or D quarter turn lowers the corner qt count right away, with no setup.
- L is the range of optimal corner solution lengths the case can have.
- The last column is a typical DR of the case: a state whose optimal is the median for that case, with that optimal in brackets.

**2c4** (wen's stacks). Seven cases. Two of them have the same bad corners and are told apart by the back face, as explained under the table:

| Bad corners | L | A qt takes it straight to | Share | In 10 | In 11 | In 12 | In 13 | A typical DR (its optimal) |
|---|---|---|---:|---:|---:|---:|---:|---|
| both on one layer, adjacent; back-face diagonals agree | 7–10 | 2c3 | 17% | 0.48% | 3.1% | 16% | 57% | `R2 D' B2 F2 L2 D' B2 U B2 D' B2 F2 U2` (13) |
| 1 up 1 down, opposite | 8–10 | 4b3 | 8% | 0.31% | 2.3% | 13% | 51% | `R2 B2 F2 U' L2 D2 B2 U' F2 L2 U' L2 U'` (13) |
| both on one layer, adjacent; back-face diagonals differ | 7–10 | 2c3 | 17% | 0.38% | 2.4% | 13% | 47% | `F2 U' B2 D' L2 D' L2 U B2 R2 U L2 F2 U'` (14) |
| both on one layer, adjacent | 8–11 | nothing, needs a setup | 17% | 0.15% | 1.1% | 7.0% | 33% | `B2 D2 R2 U F2 U L2 U' R2 D2 R2 F2 U' R2` (14) |
| 1 up 1 down, stacked | 9–11 | 4b3 | 8% | 0.13% | 1.1% | 7.0% | 33% | `B2 U B2 U2 B2 F2 R2 D B2 L2 U' B2 R2 U'` (14) |
| 1 up 1 down, opposite | 8–11 | nothing, needs a setup | 17% | 0.13% | 0.99% | 6.4% | 31% | `U' L2 D B2 U2 B2 L2 F2 U' L2 B2 D2 U' R2` (14) |
| 1 up 1 down, stacked | 9–12 | nothing, needs a setup | 17% | 0.04% | 0.52% | 4.1% | 23% | `U F2 U' L2 F2 D B2 R2 F2 D2 B2 U' F2 U2` (14) |

**Telling the two look-alike 2c4 cases apart.** Hold the cube so the two bad corners are on the front edge of one layer (if you see six bad corners, turn both layers, U D', and you will see two). The four corners of the back face are then all good. Take each diagonal of the back face. Its two corners share exactly one colour: their sticker on the back face, their U/D sticker, or their sticker on the side. If both diagonals share the same kind of sticker, the diagonals agree; otherwise they differ.

Both sides together:

| Normal and inverse | Share | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|
| the best case on both sides (adjacent, a qt straight to 2c3, first row) | 2.8% | 0.92% | 5.6% | 26% | 75% |
| no stack on either side, and a qt goes straight to 2c3 or 4b3 on both | 17.4% | 0.68% | 4.2% | 21% | 66% |
| a stack on one side only | 37.5% | 0.10% | 0.92% | 6.4% | 32% |
| a stack on both sides | 6.2% | 0 | 0.06% | 1.1% | 11% |

So a double stack is as dead as a 5qt at every target (0 / 0.06% / 1.1% / 11% against 0.02% / 0.24% / 2.1% / 14% for all 5qt DRs, in 10 / 11 / 12 / 13), and the best layout on both sides is as good as an average 2c3 4e (1.3% / 6.4% / 27% / 73%).

    U2 L2 D' F2 U' R2 U F2 D L2 U2   // the fastest any double-stacked 2c4 finishes: 11

**2c5.** Three cases:

| Bad corners | L | A qt takes it straight to | Share | In 10 | In 11 | In 12 | In 13 | A typical DR (its optimal) |
|---|---|---|---:|---:|---:|---:|---:|---|
| both on one layer, adjacent | 9–12 | 2c4 | 50% | 0.05% | 0.45% | 3.4% | 19% | `D' R2 D R2 U2 L2 D' F2 U' R2 U F2 L2 U2` (14) |
| 1 up 1 down, opposite | 10–13 | 4b4 | 25% | 0.01% | 0.20% | 1.9% | 13% | `B2 D U2 F2 U L2 U R2 U2 L2 U' F2 U' R2` (14) |
| 1 up 1 down, stacked | 11–13 | 4b4 | 25% | 0 | 0.03% | 0.62% | 6.0% | `B2 D' B2 D' B2 R2 D2 L2 U' F2 D F2 L2 U R2` (15) |

Both sides together:

| Normal and inverse | Share | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|
| adjacent on both sides | 25.0% | 0.08% | 0.69% | 4.7% | 25% |
| adjacent and opposite | 25.0% | 0.02% | 0.35% | 2.9% | 18% |
| opposite on both sides | 6.2% | 0 | 0.09% | 1.4% | 11% |
| adjacent and stacked | 25.0% | 0 | 0.06% | 1.1% | 9.5% |
| opposite and stacked | 12.5% | 0 | 0 | 0.24% | 4.5% |
| stacked on both sides | 6.2% | 0 | 0 | 0 | 0.64% |

The last two rows are 19% of all 2c5, and you can drop them on sight whatever your target: a 2c5 that is stacked on both sides never finishes in 12, and stacked on one side with opposite on the other never finishes in 11 and is 0.24% for a 12.

    U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2   // the fastest any double-stacked 2c5 finishes: 13

**4c3** (JTuu's question). Nine cases, seven of them 4a3 and two 4b3. Eight rows, because two of the 4a3 cases look the same:

| Bad corners | Subset | L | A qt takes it straight to | Share | In 10 | In 11 | In 12 | In 13 | A typical DR (its optimal) |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| 2-2, pairs on opposite sides | 4a3 | 7–9 | 4b2 | 8% | 0.75% | 4.5% | 22% | 68% | `D R2 D' F2 D' B2 R2 B2 U L2 D2 U' R2` (13) |
| 2-2, pairs stacked | 4a3 | 7–9 | 4b2 | 8% | 0.62% | 3.6% | 18% | 60% | `R2 U' F2 U R2 B2 D L2 U2 R2 U' R2 U'` (13) |
| 2-2, pairs sharing one column | 4b3 | 7–10 | 4a2 | 17% | 0.50% | 2.8% | 13% | 47% | `R2 D2 R2 U L2 U' B2 R2 B2 U L2 D F2 U'` (14) |
| 3-1 | 4b3 | 8–11 | nothing, needs a setup | 33% | 0.29% | 2.0% | 11% | 45% | `R2 F2 U' B2 D' B2 R2 D' R2 D R2 U2 L2 U'` (14) |
| 2-2, diagonal over diagonal | 4a3 | 8–10 | nothing, needs a setup | 8% | 0.26% | 1.8% | 10% | 43% | `B2 F2 U' F2 L2 U R2 U2 L2 R2 B2 D' F2 L2` (14) |
| 4-0 (two cases that look the same) | 4a3 | 8–10 | nothing, needs a setup | 8% | 0.24% | 1.7% | 10% | 43% | `D2 B2 D' B2 U' B2 D2 L2 U' L2 U' F2 U'` (13) or `D' F2 U L2 D' L2 R2 U' B2 U R2 D F2 U'` (14) |
| 2-2, pairs stacked | 4a3 | 8–10 | nothing, needs a setup | 8% | 0.23% | 1.6% | 9.4% | 40% | `D' L2 U' F2 D' F2 L2 D' L2 U B2 U2 R2 U2` (14) |
| 2-2, pairs on opposite sides | 4a3 | 9–11 | nothing, needs a setup | 8% | 0.05% | 0.47% | 3.6% | 22% | `D' L2 U F2 D' B2 L2 U' R2 U L2 D F2 U'` (14) |

The row marked "two cases that look the same" is two corner cases with the same bad corners and no quarter turn that lowers the count. I have not found a visible test that separates them, so the row gives their odds together. Apart, they are 0.40% / 2.8% / 15% / 57% and 0.07% / 0.68% / 5.1% / 28% (in 10 / 11 / 12 / 13), and only the optimal corner solution tells you which: 8 moves is the better one, 10 the worse one, and with 9 it can be either.

Both sides together:

| Normal and inverse | Share | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|
| the best pair of cases | 5.6% | 0.95% | 5.3% | 23% | 68% |
| the worst pair of cases | 11.1% | 0.01% | 0.29% | 3.0% | 20% |

**4b2** (Daichi's four: 2-2 and 3-1, each with good and bad parity). Three rows, because the two 3-1 cases look the same:

| Bad corners | L | A qt takes it straight to | Share | In 10 | In 11 | In 12 | In 13 | A typical DR (its optimal) |
|---|---|---|---:|---:|---:|---:|---:|---|
| 2-2, pairs sharing one column | 3–6 | 4a1 | 17% | 3.4% | 14% | 44% | 88% | `U' L2 D' L2 U' F2 U L2 U2 R2 D' R2 U'` (13) |
| 3-1 (two cases that look the same) | 4–8 | nothing, needs a setup | 67% | 2.1% | 9.8% | 36% | 83% | `U' L2 D' L2 U B2 D2 B2 U' L2 U B2 D'` (13) or `R2 U L2 R2 D L2 U' B2 F2 R2 D' R2 D2` (13) |
| 2-2, pairs sharing one column | 6–9 | nothing, needs a setup | 17% | 1.3% | 7.0% | 30% | 78% | `B2 D2 L2 D R2 F2 D' L2 B2 F2 D' U' L2` (13) |

The 3-1 row is two corner cases that look the same (Daichi's "3-1 good parity" and "3-1 bad parity"). I have not found a visible test that separates them, so the row gives their odds together. Apart, they are 2.5% / 11% / 40% / 86% and 1.7% / 8.4% / 33% / 81% (in 10 / 11 / 12 / 13), and only the optimal corner solution tells you which: 4 moves is the better one, 8 the worse one, and with 5 to 7 it can be either.

Both sides together:

| Normal and inverse | Share | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|
| the best pair of cases | 2.8% | 4.8% | 17% | 50% | 91% |
| the worst pair of cases | 2.8% | 0.61% | 4.2% | 21% | 69% |

**4a2.** The widest spread of the low-qt subsets:

| Bad corners | L | A qt takes it straight to | Share | In 10 | In 11 | In 12 | In 13 | A typical DR (its optimal) |
|---|---|---|---:|---:|---:|---:|---:|---|
| 2-2, diagonal over diagonal | 5–8 | 4a1 | 17% | 2.4% | 9.3% | 31% | 72% | `F2 R2 U B2 F2 U' L2 R2 U' R2 D2 F2 U` (13) |
| 2-2, pairs stacked | 6–9 | nothing, needs a setup | 33% | 1.4% | 6.1% | 22% | 60% | `B2 L2 D' L2 D2 B2 D F2 R2 U2 R2 F2 D2` (13) |
| 2-2, pairs on opposite sides | 7–10 | nothing, needs a setup | 33% | 0.50% | 2.7% | 12% | 42% | `D R2 U2 L2 R2 B2 U' B2 R2 U B2 U2 R2 U'` (14) |
| 4-0 | 8–11 | nothing, needs a setup | 17% | 0.32% | 1.9% | 9.3% | 33% | `B2 R2 U2 R2 U' B2 R2 U2 R2 D B2 L2 U2 L2` (14) |

Both sides together:

| Normal and inverse | Share | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|
| the best pair of cases | 2.8% | 4.4% | 14% | 43% | 83% |
| the worst pair of cases | 2.8% | 0 | 0.16% | 2.3% | 13% |

**4c4** and **4b5** are too rare at 10 and 11 for the case to matter (under 1% in 11 for every case). For a 12, 4c4 runs from 0.57% to 4.3% by case and 4b5 from 1.3% to 2.2%.

Appendix E lists all 46 cases with a typical DR and the shortest setup for each, the L range (which is what Evan asked for), and the full both-sides tables.

A warning: the bad corner *positions* don't always tell you the case. 2c4 has three different "both on one layer, adjacent" cases, at 0.48% / 3.1% / 16%, 0.38% / 2.4% / 13% and 0.15% / 1.1% / 7.0% (in 10 / 11 / 12). What separates them is the corner permutation, which you get the way you already get the subset (tracing, or whatever corner-case system you use). The column "a qt takes it straight to" is the quick tell: if some U or D quarter turn drops the corner qt count right away, you're in one of the good ones.

### 6.4 HTR length on both sides

Zagros asked for the square table ([Zagros, 10 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1470865840298655918)); trangium posted one from samples of 20–100 per cell. Exact, for the four big high-qt subsets. Each cell: share finishing in 10 / 11 / 12.

**4c3 4e**, shorter side down, longer side across:

| | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|
| 7 | 6.7% / 22% / 55% | 3.4% / 14% / 43% | 1.7% / 7.6% / 31% | 0.60% / 4.8% / 22% | 0 / 1.7% / 14% |
| 8 |  | 2.0% / 8.1% / 30% | 0.60% / 4.1% / 20% | 0.11% / 1.8% / 13% | 0 / 0.29% / 4.6% |
| 9 |  |  | 0.15% / 1.6% / 11% | 0.02% / 0.51% / 5.6% | 0 / 0.09% / 1.8% |
| 10 |  |  |  | 0 / 0.11% / 2.1% | 0 / 0 / 0.34% |

**2c4 4e**, shorter side down, longer side across:

| | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|
| 7 | 3.0% / 11% / 36% | 1.4% / 6.7% / 27% | 0.75% / 4.3% / 20% | 0.37% / 2.8% / 16% | 0 / 2.0% / 13% |
| 8 |  | 0.59% / 3.4% / 17% | 0.24% / 1.9% / 11% | 0.06% / 0.97% / 7.4% | 0 / 0.64% / 5.8% |
| 9 |  |  | 0.05% / 0.74% / 6.0% | <0.01% / 0.20% / 2.9% | 0 / 0.03% / 1.9% |
| 10 |  |  |  | <0.01% / 0.04% / 0.89% | 0 / 0.02% / 0.36% |

**2c5 4e**, shorter side down, longer side across:

| | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|
| 9 | 0.45% / 3.0% / 13% | 0.14% / 0.95% / 6.7% | 0 / 0.35% / 3.0% | 0 / 0 / 1.1% |
| 10 |  | 0.01% / 0.31% / 2.7% | 0 / 0.04% / 1.0% | 0 / 0 / 0.23% |
| 11 |  |  | 0 / 0 / 0.08% | 0 / 0 / 0 |
| 12 |  |  |  | 0 / 0 / 0 |

**0c3 4e**, shorter side down, longer side across:

| | 10 | 11 | 12 | 13 |
|---|---:|---:|---:|---:|
| 10 | 1.4% / 4.3% / 12% | 0 / 2.6% / 7.8% | 0 / 0 / 4.2% | 0 / 0 / 0 |
| 11 |  | 0 / 0 / 4.5% | 0 / 0 / 0.35% | 0 / 0 / 0 |
| 12 |  |  | 0 / 0 / 0.02% | 0 / 0 / 0 |
| 13 |  |  |  | 0 / 0 / 0 |

One more move to HTR on both sides costs about half a move of average optimal. From 8 and 8 to 9 and 9 it divides the odds of a 12 by about three, of an 11 by about five and of a 10 by more than ten. The step from 7 and 7 to 8 and 8 is gentler: about two, three and three to five. Appendix F has every subset with share, average, fastest finish, and odds for 10 to 13. Section 5 has the same read as a plain rule against your target.

**By the longer side alone**, for a whole corner-qt group. This is the table to use when you have one HTR length per side and no time for more (rows under 0.1% of the group are left out):

| Corner qt | Longer HTR | Share of the group | In 9 | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1–2qt | 4 | 0.27% | 14% | 31% | 58% | 86% | 99% |
| 1–2qt | 5 | 1.9% | 4.1% | 13% | 34% | 71% | 97% |
| 1–2qt | 6 | 14% | 1.2% | 5.1% | 18% | 52% | 92% |
| 1–2qt | 7 | 33% | 0.48% | 2.6% | 12% | 41% | 86% |
| 1–2qt | 8 | 30% | 0.17% | 1.3% | 7.5% | 32% | 81% |
| 1–2qt | 9 | 12% | 0.05% | 0.57% | 4.1% | 21% | 68% |
| 1–2qt | 10 | 5.7% | 0 | 0.10% | 1.3% | 9.1% | 41% |
| 1–2qt | 11 | 3.0% | 0 | 0 | 0.28% | 3.7% | 23% |
| 1–2qt | 12 | 0.15% | 0 | 0 | 0 | 1.1% | 13% |
| 3qt | 6 | 2.8% | 1.1% | 4.6% | 18% | 52% | 93% |
| 3qt | 7 | 18% | 0.37% | 2.1% | 9.9% | 37% | 84% |
| 3qt | 8 | 27% | 0.14% | 0.94% | 5.3% | 24% | 69% |
| 3qt | 9 | 30% | 0.03% | 0.34% | 2.5% | 14% | 53% |
| 3qt | 10 | 18% | 0 | 0.07% | 0.93% | 7.0% | 34% |
| 3qt | 11 | 2.4% | 0 | 0 | 0.27% | 2.7% | 17% |
| 3qt | 12 | 1.8% | 0 | 0 | 0 | 0.76% | 8.3% |
| 3qt | 13 | 0.37% | 0 | 0 | 0 | 0 | 0.81% |
| 4qt | 7 | 0.27% | 0.75% | 3.0% | 12% | 38% | 84% |
| 4qt | 8 | 6.2% | 0.15% | 0.96% | 5.1% | 23% | 66% |
| 4qt | 9 | 34% | 0.02% | 0.22% | 1.7% | 10% | 42% |
| 4qt | 10 | 33% | 0 | 0.05% | 0.58% | 4.6% | 26% |
| 4qt | 11 | 22% | 0 | 0 | 0.10% | 1.3% | 9.9% |
| 4qt | 12 | 3.7% | 0 | 0 | 0 | 0.33% | 4.5% |
| 4qt | 13 | 0.15% | 0 | 0 | 0 | 0 | 2.3% |
| 5qt | 9 | 3.4% | 0.04% | 0.17% | 1.0% | 5.5% | 24% |
| 5qt | 10 | 52% | 0 | 0.03% | 0.33% | 2.7% | 17% |
| 5qt | 11 | 39% | 0 | 0 | 0.08% | 1.2% | 10% |
| 5qt | 12 | 5.9% | 0 | 0 | 0 | 0.28% | 4.2% |

**Zagros's rule, "4c3 that is 9+ on both sides I throw away".**

| 4c3 that is… | Share of 4c3 | Average optimal | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|
| 9+ to HTR on both sides (what the rule throws away) | 51% | 13.74 | 0.06% | 0.76% | 6.4% | 34% |
| the rest | 49% | 13.22 | 0.67% | 3.9% | 18% | 58% |
| 7 or less to HTR on at least one side | 10% | 12.91 | 1.6% | 7.2% | 28% | 73% |

Share of the 4c3 finishes the rule keeps: 92% of those in 10, 83% of those in 11, 73% of those in 12, 63% of those in 13.

So the rule halves your 4c3s, and what it costs depends on what you need. For an 11-move DR, which needs a 10 or an 11, it trades half of your 4c3s for 8% of the 10s and 17% of the 11s. For a 12 it throws away a quarter of the finishes. It does throw away real finds:

    U' L2 D' B2 U' B2 U L2 D     // 4c3 4e, 9 to HTR on both sides
    D' L2 U' B2 U B2 D L2 U      // its optimal finish: 9

Knowing the two HTR lengths does not give you a better *guarantee* than the longer one: in every subset some state finishes in exactly max(normal, inverse). The 4c3 4e just above is one, and Appendix G has one for every subset. It's an odds read.

### 6.5 Corner length and E-slice parity

Side half turns (R2 L2 F2 B2) each swap two E-slice edges, and U and D never touch the slice. So the number of side turns in *any* DR finish is even if the E-slice is an even permutation (solved, 3-cycle, 2e2e) and odd if it's odd (2-swap, 4-cycle). This is Rodney's fr-parity, used on the whole finish instead of after HTR.

> Find an optimal corner solution, length L. Count its side turns. If that's the wrong parity for the E-slice, there is no L-move finish. You need the best corner solution of the other parity.

What the other parity costs, over all corner states of each subset:

| Corners | +0 | +1 | +2 | more |
|---|---:|---:|---:|---:|
| 4a2, 0c3, 0c4 | | 100% | | |
| 4a3, 4b3 | 11% | 89% | | |
| 4a4, 4b4 | 6% | 94% | | |
| 2c4 | | 75% | 25% | |
| 2c5 | 2% | 80% | 18% | |
| 4b5 | 14% | 56% | 31% | |
| 4b2 | 3% | 73% | 25% | |
| 2c3 | 15% | 35% | 50% | |
| 4a1 | | 75% | 4% | 21% (+3 to +5) |
| 0c0 | 25% | | 50% | 25% (+3 to +6) |

This one is a true lower bound, proven in Lean: no finish is shorter than the best corner solution of the right parity. For a 12 it proves "no" for 13% of 5qt DRs and 5% of 4qt. For an 11: 37% and 21%. For a 10: 73% and 48% (the table of what is proven in section 5). It needs the *optimal* corner solutions of both parities, so it's a read for when you've written the skeletons down anyway.

Two DRs where it bites:

    U B2 U' F2 U B2 D2 L2 U' R2 U R2 U' L2 U2      // 2c4 4e, odd E-slice
    // best corner solution: 12, with an even number of side turns. Best with an odd number: 13.
    // So no 12. (Its optimal is 15.)

    U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2   // 2c3 6e, odd E-slice (Rodney's first random scramble)
    U' R2 U' R2 U                                   // corners in 5, but two side turns
    U R2 U2 R2 U R2 U                               // best with an odd number: 7

As an odds read, L does about what HTR length does from 3qt up, and less at 1–2qt (Appendix H). Appendix B splits the big high-qt subsets by L and parity. For 2c4 4e, in 10 / 11 / 12: with L = 8, 0.49% / 2.8% / 15%. With L = 11, 0 / 0.20% / 1.9%. With L = 12, 0 / 0 / 1.6% if the E-slice is even and 0 / 0 / 0 if it's odd.

The E-slice parity on its own, without L, is a small read but it's free. It mostly decides whether the finish wants to be even or odd in length. At 4qt, 8.1% finish in 12 with an odd E-slice against 5.5% with an even one, and in 11 it's the even one that is ahead, 1.4% against 0.84%. At 5qt, 18% finish in 13 with an odd E-slice against 10% with an even one.

### 6.6 The last DR move

Zagros asked what one invertible move is worth. If your DR ends in R, then R' is also a DR and its state is yours plus an R2, so you get the better of two finishes. Average optimal over all DRs: 13.58 for a pure DR, 13.26 when the last move can go either way.

| Corner qt | | In 9 | In 10 | In 11 | In 12 | In 13 |
|---|---|---:|---:|---:|---:|---:|
| 1–2qt | pure DR | 0.51% | 2.4% | 10% | 35% | 79% |
| 1–2qt | last move can go either way | 0.84% | 3.8% | 16% | 49% | 90% |
| 3qt | pure DR | 0.14% | 0.87% | 4.6% | 20% | 59% |
| 3qt | last move can go either way | 0.25% | 1.5% | 7.5% | 30% | 73% |
| 4qt | pure DR | 0.02% | 0.16% | 1.1% | 6.8% | 30% |
| 4qt | last move can go either way | 0.03% | 0.28% | 2.0% | 11% | 43% |
| 5qt | pure DR | <0.01% | 0.02% | 0.24% | 2.1% | 14% |
| 5qt | last move can go either way | <0.01% | 0.04% | 0.43% | 3.7% | 23% |

A third of the time the other DR is one shorter, a third the same, a third one longer, in every subset. So it's worth 0.33 moves flat. It multiplies the odds of a 10 or an 11 by 1.6 to 2 and of a 12 by 1.4 to 1.8. (If you could pick any of the four side half turns it would be 0.73.) An example:

    D' L2 D R2 B2 F2 U2 B2 R2 U L2 U'       // optimal 12
    D' L2 D R2 B2 F2 U2 B2 R2 U L2 U' L2    // the same DR with its last move (an L) turned the other way: optimal 11

---

## 7. Bounds people use, graded

A bound is only a bound if it never exceeds the optimal. Graded on all states:

| Bound | Ever too high? | Its average | Average optimal there |
|---|---|---:|---:|
| longer HTR, normal or inverse (all DRs) | never (proven) | 9.22 | 13.58 |
| best corner solution with the right E-parity (all DRs) | never (proven) | 9.44 | 13.58 |
| Levi's 1qt formula, HTR normal + HTR inverse − 1 (4a1 4e) | never for a finish with one quarter turn. A finish with three is shorter for 11.7% of 4a1 4e | 10.85 | 12.27 |
| setup + HTR, any qt (below) | never for a finish with the minimum number of quarter turns. A finish with more is shorter for 2.6% at 1–2qt and 0.002% above | see below | |

**Levi's formula.** (HTR normal) + (HTR inverse) − 1 bounds the finishes with one quarter turn, which is what Levi's doc uses it for. (The doc writes it as the path to the trigger on normal + on inverse + 1. An HTR is that path plus the quarter turn, so it's the same number.) That's the 4 + 6 + 2 + 1 = 13 of Levi's 1qt example after `R2 U' F2 U`: shortest HTR there is 7 on normal and 3 on inverse, each counting the qt, and the formula counts it once ([wen, 28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1311629216235913226)).

A 1qt state can also be solved with three quarter turns, and the number worth having is how often that is shorter. Over all 286,654,464 states of 4a1 4e:

| The optimal is… | Share of 4a1 4e |
|---|---:|
| below the formula, so a 3qt finish is shorter (by 1: 8.4%, by 2: 2.7%, by 3 or more: 0.6%) | 11.7% |
| equal to the formula | 18.0% |
| above the formula | 70.3% |

If the formula says 12 or less, a 3qt finish beats it 2.5% of the time, and 0.6% of the time if it says 11 or less. Example:

    U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2   // 4a1 4e. HTR is 6 on normal, 5 on inverse, formula says 10
    U B2 L2 F2 D F2 D                  // 7

(Both lines are proven in Lean.) For 4a1 2e optimal is below the formula 44% of the time and for 4a1 0e 95%, so the formula is only for 4c4e, like Levi says. (4a1 2e and 0e are fine DRs to solve. It's the formula that doesn't apply to them, because they can't be finished with one quarter turn.)

One more thing about 4a1 4e that I haven't seen written down: for 72 of its 432 cases (one in six) the shortest HTR is not a 1qt HTR at all. The shortest 1qt path is 8, 9 or 10 moves and a 3qt HTR does it in 7 or 8. So "shortest HTR" and "shortest way to the trigger" are different numbers there, and the formula wants the second. One where it happens on both sides:

    U L2 R2 U R2 B2 U L2          // 4a1 4e
    U L2 F2 L2 U B2 U             // shortest HTR on normal: 7, three quarter turns
    R2 F2 U2 R2 F2 U2 L2 D        // shortest HTR with one quarter turn: 8
    L2 U' B2 R2 U' R2 L2 U'       // optimal finish: 8

(The inverse is the same: 7 with three quarter turns, 8 with one.)

**The bound against the real leave slice** (count quackula's question). For 4a1 4e, leave slice minus formula:

| −3 or less | −2 | −1 | +0 | +1 | +2 | +3 | +4 or more |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.7% | 5.4% | 12.6% | 26.9% | 25.8% | 15.9% | 7.9% | 3.8% |

Average +0.70. The leave slice is below the formula 19.7% of the time, more often than the full finish is, because leaving the slice is easier. (The example above is one: formula 10, leave slice 7.)

**Setup + HTR at any qt.** trangium's "true 2q bound" ([trangium, 27 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487207920256024738)) is (shortest HTR on one side) + (half turns before the first qt on the other side). FakeMMAP pointed out it works for more qts. The general version: on each side count the fewest half turns you need before some quarter turn lowers the qt count, add the shortest HTR of the other side, take the bigger of the two sums. At 1qt this is Levi's formula. Like Levi's, it's only a bound for finishes that use the minimum number of qts.

| | Beaten by extra qts | Exact | 1 under | 2 under | 3+ under | Its average | Longer HTR | Optimal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1–2qt | 2.6% | 4.0% | 11% | 18% | 64% | 9.62 | 7.66 | 12.75 |
| 3qt | 0.00% | 0.3% | 2.3% | 9.5% | 88% | 9.22 | 8.60 | 13.23 |
| 4qt | 0.00% | 0.3% | 2.6% | 13% | 84% | 10.35 | 9.83 | 13.89 |
| 5qt | 0.00% | 0.1% | 0.8% | 6.3% | 93% | 10.47 | 10.47 | 14.30 |

A finish with extra quarter turns gets under it for 23.8% of 4a1 4e (more than the 11.7% for Levi's formula because this one uses the real setup, see above), 2.2% of 4a2 4e, 1.3% of 4a2 0e, 0.9% of 4b2 4e, and for 0.002% of everything at 3qt and up. So from 3qt it's as good as a true bound. One state for every subset where it happens (there are 13):

| Subset | Scramble | Setup + HTR bound | Optimal finish |
|---|---|---:|---|
| 4a1 4e | `D' F2 R2 U' B2 F2 D` | 15 | `D' F2 B2 U R2 F2 D` (7, 3 quarter turns against a minimum of 1) |
| 4a2 0e | `D' F2 D2 L2 U F2 D' B2 U2 R2 U` | 13 | `U' R2 U2 B2 D F2 U' L2 D2 F2 D` (11, 4 quarter turns against a minimum of 2) |
| 4a2 2e | `D' L2 D' B2 F2 U' F2 D'` | 10 | `D F2 U F2 B2 D L2 D` (8, 4 quarter turns against a minimum of 2) |
| 4a2 4e | `D B2 D L2 D F2 U F2 U' L2 U` | 15 | `U' L2 U F2 U' F2 D' L2 D' B2 D'` (11, 6 quarter turns against a minimum of 2) |
| 4b2 0e | `D' R2 U' F2 U2 L2 U' R2 D` | 12 | `D' R2 U L2 U2 F2 U R2 D` (9, 4 quarter turns against a minimum of 2) |
| 4b2 2e | `D' F2 U B2 U F2 D'` | 8 | `D F2 U' B2 U' F2 D` (7, 4 quarter turns against a minimum of 2) |
| 4b2 4e | `D L2 U' R2 U' L2 F2 U'` | 12 | `U F2 L2 U R2 U L2 D'` (8, 4 quarter turns against a minimum of 2) |
| 0c3 4e | `U' F2 U F2 U' R2 D L2 U' L2 U R2 U` | 14 | `U' R2 U' L2 U L2 D' R2 U F2 U' F2 U` (13, 7 quarter turns against a minimum of 3) |
| 4c3 2e | `D' B2 D' L2 D' L2 U B2 U'` | 10 | `U B2 U' L2 D L2 D B2 D` (9, 5 quarter turns against a minimum of 3) |
| 4c3 4e | `U' L2 D' B2 U' B2 U L2 D` | 10 | `D' L2 U' B2 U B2 D L2 U` (9, 5 quarter turns against a minimum of 3) |
| 4c4 0e | `U F2 U' F2 U R2 U' F2 U F2 R2 U'` | 13 | `U R2 F2 U' F2 U R2 U' F2 U F2 U'` (12, 6 quarter turns against a minimum of 4) |
| 4c4 2e | `D B2 D R2 U' R2 D L2 D B2 D'` | 12 | `D B2 D' L2 D' R2 U R2 D' B2 D'` (11, 6 quarter turns against a minimum of 4) |
| 4c4 4e | `D B2 D' F2 D F2 D' F2 U F2 U'` | 12 | `U F2 U' F2 D F2 D' F2 D B2 D'` (11, 6 quarter turns against a minimum of 4) |

Daichi's objection ([Daichi, 28 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487653636786880684)) holds everywhere: it adds two moves to the HTR bound at 2qt, half a move at 3–4qt, nothing at 5qt (a qt that lowers the count is always available right away), and it sits three or more under optimal for most DRs.

**Rodney's rules at 1qt** are graded in section 10: a true lower bound in all 216 cases, even against DR-breaking finishes.

**So for bounding error stats** (compLex's question): the guaranteed bounds you can compute by hand are on average four moves under optimal. The useful hand bound is still Rodney's, per skeleton, late.

---

## 8. Leave slice, the slice, and width

**Cost of the slice** (JTuu's question): optimal finish minus optimal leave slice.

| | +0 | +1 | +2 | +3 or more | Average |
|---|---:|---:|---:|---:|---:|
| 0qt | 44% | 42% | 14% | 0.6% | +0.71 |
| 1–2qt | 56% | 39% | 5.4% | 0.1% | +0.50 |
| 3qt | 67% | 32% | 1.6% | | +0.35 |
| 4qt | 79% | 20% | 0.5% | | +0.21 |
| 5qt | 85% | 15% | 0.1% | | +0.15 |
| all DRs | 73% | 26% | 1.6% | | +0.29 |

The longer the finish, the more room to fit the slice for free. (+1 happens because the optimal finish doesn't have to be an optimal leave slice with a slice inserted.) Examples:

    D' U2 F2 U2               // leave slice 3, optimal finish 4: the slice costs +1
    U R2 D U'                 // leave slice 2, optimal finish 4: +2
    B2 F2 D' U L2 R2 D U'     // only the E-slice is unsolved and it takes 8: the most the slice can cost

**Width** (JTuu, Zagros: "higher qt means more opt+1"). A cheap measure: how many of the ten moves start an optimal finish.

| Optimal | Average number of optimal first moves | Exactly one |
|---:|---:|---:|
| 10 | 1.3 | 78% |
| 11 | 1.4 | 73% |
| 12 | 1.6 | 64% |
| 13 | 2.0 | 47% |
| 14 | 2.8 | 29% |
| 15 | 4.3 | 8% |
| 16 | 7.6 | 0.2% |

Short finishes are narrow: when the optimal is 10 or 11, three times out of four exactly one first move gets it, and with a 12 two times out of three. Long finishes are wide. Higher qt DRs have more optimal first moves (3.1 on average at 5qt against 2.6 at 2qt) only because their optimals are longer. One of each:

    D' L2 D R2 B2 F2 U2 B2 R2 U L2 U'                  // optimal 12: only U or L2 starts an optimal finish
    D2 B2 U' R2 D R2 B2 R2 F2 U2 R2 D F2 U R2 U'       // optimal 16: nine of the ten moves do

---

## 9. What a computer can prove from the DR

This is the first version of the doc, kept because it shows where the information is and what any hand rule is up against.

### You can't finish faster than the part you're looking at

Pick something to look at on a DR. Say, only the corners. Ask how many moves it takes to solve *just that*. The real finish solves everything, so it solves the corners too, so it can't be shorter. That's the corner-length bound, and it's the logic of every bound here. Look at more and the bound goes up. A solution read backwards solves the inverse scramble, so the same number computed on the inverse is also a lower bound, and you take the bigger one.

If you look at exactly what Rodney traces at 1qt (the corners, which slice each U/D-layer edge belongs to, its U/D colour, the E-parity) but on the DR state itself, you get one number that no skeleton and no variant can beat, at any qt. I call that NISS@DR. On HTR states with half turns only it *is* FakeMMAP's 216-case table. The catch is that at the DR it has 6,350,400 cases instead of 216.

### The seven levels

All tables use the ten DR moves. "Cases" = things that look the same.

| Level | What you look at | Cases | Max |
|---|---|---:|---:|
| HTR length | which corners and edges are bad | 29,400 | 13 |
| Corner length L | corners | 40,320 | 13 |
| L with parity | corners + E-slice parity | 80,640 | 14 |
| L+S+T | corners + which edges are bad + E-parity | 5,644,800 | 15 |
| **NISS@DR** | Rodney's NISS@1qt info: corners up to a free U2; where the M-slice and S-slice edges sit; their U/D colours up to swapping white and yellow within a slice; E-parity | 6,350,400 | 15 |
| NISS@DR + H-perm parity | same, no free U2, plus the double-swap parity | 25,401,600 | 16 |
| Everything visible | corners; slice and colour of the edge in every U/D position; double-swap parity | 406,425,600 | 17 |

The real optimal maxes out at 18 (1,352 states, the number Reid gave, quoted by [Tomas Rokicki, 31 May 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1510792489236430968)).

Some notes:

- **NISS@DR on HTR states with half turns only *is* FakeMMAP's table.** FakeMMAP's 216 example scrambles are 216 different cases and every value matches (both proven in Lean). So NISS@DR is that table grown from 216 cases to 6.35 million: one for every corner state and edge layout a DR can have.
- **"Up to swapping white and yellow"** is Rodney's *reflection* ("yellow FH edges with white HH corners", +2). The last level looks at the actual colours, so reflection is built in.
- **Double-swap parity** is the H-perm thing FakeMMAP and Rodney went back and forth on ([here](https://discord.com/channels/1007840975726575667/1007841335434285126/1546101477334978650) and [here](https://discord.com/channels/1007840975726575667/1007841335434285126/1546232388013785088)): are the four M-slice edges, read in order, an even or odd arrangement, and same for S. On HTR states that's the parity of F2/B2 turns and of R2/L2 turns separately, the F-parity and R-parity of FakeMMAP's "OBL++" sheet. Rodney guessed that knowing it would make the bound basically exact ([Rodney, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546126576247247028)). Below you can see how close it gets.
- **What the last level still can't see**: which of the two white M-slice edges is which (same for the other three pairs), and the E-slice beyond its parity. So H-perm-style 2e2e's inside a slice and E-slice 3-cycles are the only blind spot.

Everything here is an exact count over all 19,508,428,800 DR states. "Bound" = the bigger of normal and inverse.

### How close each level gets

| Level | Average bound | Equal to optimal | Within 1 |
|---|---:|---:|---:|
| HTR length (longer side) | 9.22 | 0.1% | 0.7% |
| Corner length L | 8.86 | 0.1% | 0.8% |
| L with parity | 9.44 | 0.8% | 2.4% |
| L+S+T | 10.99 | 3.4% | 13.6% |
| NISS@DR | 11.68 | 7.6% | 32.8% |
| NISS@DR + H-perm parity | 12.14 | 17.1% | 52.1% |
| Everything visible | 12.86 | 43.8% | 85.8% |
| actual optimal | 13.58 | | |

So Rodney was about right on the H-perm parity: with it and the real colours, the bound is exact 44% of the time and within one 86% of the time.

### Throwing DRs away

How often does a level *prove* that there is no finish in T? Percentages are of all DR states in the row.

| Corner qt | Finish needed | DRs with no such finish | HTR | L+parity | L+S+T | NISS@DR | +H-perm | Everything |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1–2qt (4a1, 4a2, 4b2) | 10 or less | 98% | 3.2% | 1.4% | 22% | 57% | 76% | 90% |
| 1–2qt (4a1, 4a2, 4b2) | 11 or less | 90% | 0.15% | 0.23% | 6.8% | 16% | 37% | 66% |
| 1–2qt (4a1, 4a2, 4b2) | 12 or less | 65% | 0 | 0 | 1.9% | 3.8% | 8.2% | 24% |
| 1–2qt (4a1, 4a2, 4b2) | 13 or less | 21% | 0 | 0 | 0.14% | 0.74% | 1.7% | 3.8% |
| 3qt (2c3, 4c3, 0c3) | 10 or less | 99.1% | 4.6% | 12% | 48% | 77% | 88% | 97% |
| 3qt (2c3, 4c3, 0c3) | 11 or less | 95% | 2.2% | 2.5% | 18% | 37% | 59% | 84% |
| 3qt (2c3, 4c3, 0c3) | 12 or less | 80% | 0.37% | 0.71% | 4.6% | 9.2% | 22% | 49% |
| 3qt (2c3, 4c3, 0c3) | 13 or less | 41% | 0 | 0 | 1.1% | 2.1% | 4.8% | 13% |
| 4qt (2c4, 4c4, 0c4) | 10 or less | 99.8% | 26% | 48% | 82% | 96% | 98% | 99.6% |
| 4qt (2c4, 4c4, 0c4) | 11 or less | 99% | 3.9% | 21% | 51% | 75% | 86% | 97% |
| 4qt (2c4, 4c4, 0c4) | 12 or less | 93% | 0.15% | 5.0% | 16% | 34% | 53% | 81% |
| 4qt (2c4, 4c4, 0c4) | 13 or less | 70% | 0 | 0 | 1.7% | 5.2% | 15% | 41% |
| 5qt (2c5, 4b5) | 10 or less | 99.9% | 44% | 73% | 97% | 99.6% | 99.7% | 99.9% |
| 5qt (2c5, 4b5) | 11 or less | 99.8% | 5.9% | 37% | 76% | 94% | 97% | 99.4% |
| 5qt (2c5, 4b5) | 12 or less | 98% | 0 | 13% | 28% | 59% | 76% | 95% |
| 5qt (2c5, 4b5) | 13 or less | 86% | 0 | 1.2% | 3.9% | 7.9% | 25% | 66% |

"The longer your HTR, the more useful it is to have a lower bound" ([Rodney, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546184215542898760)). This is that, in numbers: at 1–2qt bounding from the DR does almost nothing for a 12, and you should bound late like Levi and Rodney do. At 4–5qt it kills most DRs on sight, and for an 11 nearly all of them. (Rows go by the Q in the subset name, which is the corner qt count. A few subsets need more actual qts than that: every 0c0 with bad edges needs 2, and 4a1 0e and 4a1 2e need 3.)

All 48 subsets are in Appendix A. The big ones:

| Subset | Share of all DRs | Avg optimal | In 11 | In 12 | NISS@DR proves no 11 | Everything proves no 11 | NISS@DR proves no 12 | Everything proves no 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 4b2 4e | 5.88% | 12.73 | 8.8% | 34% | 10% | 69% | 0.09% | 21% |
| 2c3 4e | 7.84% | 12.94 | 6.4% | 27% | 17% | 78% | 0.17% | 31% |
| 4c3 4e | 5.88% | 13.50 | 2.3% | 12% | 60% | 94% | 14% | 68% |
| 2c4 4e | 11.76% | 13.66 | 1.6% | 9.1% | 65% | 95% | 18% | 74% |
| 0c3 4e | 0.73% | 14.64 | 0.18% | 1.5% | 99% | 99.6% | 93% | 96% |
| 4c4 4e | 5.88% | 14.38 | 0.21% | 1.8% | 96% | 99.7% | 67% | 97% |
| 2c5 4e | 3.92% | 14.30 | 0.33% | 2.6% | 93% | 99% | 61% | 93% |
| 4b5 4e | 5.88% | 14.29 | 0.19% | 1.8% | 96% | 99.6% | 60% | 96% |

### Examples

I wrote a small lookup tool for this: give it a scramble and the moves to DR (NISS in brackets) and it prints every level on both sides plus the real optimal, straight from the precomputed tables. The numbers below are its output.

**Rodney's first random scramble** (from the Advanced DR Bounding doc):

    U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2   // 2c3 6e

Rodney goes through three skeletons, kills about a dozen triggers with bounding, finds a 13 and says "to strictly prove it, we'd have to try inserting corner swaps in front of the first qt". From the DR alone:

    HTR length          9 / 7      (normal / inverse)
    corner length L     5 / 5
    L with parity       7 / 7
    L+S+T              10 / 9
    NISS@DR            10 / 11
    + H-perm parity    11 / 12
    everything         13 / 13
    optimal            13

So 13 is optimal, and the last level proves it without picking a skeleton.

**Rodney's 4a4 example:**

    U R2 L2 F2 U' B2 D2 F2 D L2 U B2 R2 U' F2 U   // 4a4 on normal, 4b4 on inverse, 4e

    HTR 11 / 10,  L 11 / 11,  L+S+T 13 / 11,  NISS@DR 13 / 12,  optimal 13

Here plain NISS@DR on the normal side already says 13. Rodney's 13-mover is optimal, read off a 4qt DR.

**Levi's example** (from the DR Bounding doc), the 10-move 3qt DR `(D2 B' L' B U' F2 D L U2 R)`: subset 4c3 4e, HTR 9 / 10, NISS@DR 12 / 12, everything 14 / 14, optimal DR finish 15. Levi says "14-move optimal finish, giving a 24". Both are right: the DR ends in R, a finish that ends on that face merges with it, and the same DR with R' instead has optimal 14. The tool prints both.

None of this is something you can do at the table, and that's the point of keeping it. Next to what a hand can do (section 5), for the finish you need:

| Corner qt | Finish needed | Everything readable puts it under 1% | The two hand bounds prove it | A table that sees the corners exactly and the colours of the edges proves it | DRs that really have no such finish |
|---|---|---:|---:|---:|---:|
| 3qt | 10 or less | 77% | 13% | 97% | 99.1% |
| 3qt | 11 or less | 30% | 3.6% | 84% | 95% |
| 3qt | 12 or less | 6% | 1.0% | 49% | 80% |
| 4qt | 10 or less | 96% | 51% | 99.6% | 99.8% |
| 4qt | 11 or less | 69% | 22% | 97% | 99% |
| 4qt | 12 or less | 24% | 5.1% | 81% | 93% |
| 5qt | 10 or less | 100% | 80% | 99.9% | 99.9% |
| 5qt | 11 or less | 94% | 38% | 99.4% | 99.8% |
| 5qt | 12 or less | 45% | 13% | 95% | 98% |

"Under 1%" in the first column is not a proof: it means the reads put the DR in a class where at most one in a hundred gets there. The next two columns are proofs.

The difference is not a feature anyone forgot to count. It's the exact relation between the corner state and where each edge sits, the thing you get from picking a skeleton and tracing. So a real hand bound at 4–5qt would have to be a faster way of doing what Rodney's method does per skeleton, across all skeletons at once.

Whether NISS@DR has a description compact enough for that, I don't know. The tables to test a guess against exist now.

---

## 10. The 216 NISS@1qt cases, three ways

FakeMMAP's first table is HT only. FakeMMAP then added HTR-breaking finishes from a list of algs, said ≤ 7 was proven and 8/9/10 might secretly be 7-movers ([FakeMMAP, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546263650015256606), [FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546599572644696075)), and is "not mathematically 100% sure" about the newer OBL++ sheet ([FakeMMAP, 10 Nov 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1569733928988704873)). Rodney's "Adv DR Bounding" sheet uses those optimals.

Here are all three (the full table is Appendix C):

| Moves allowed | How | Result |
|---|---|---|
| Half turns | BFS over the 216 cases | same as FakeMMAP's listing, all 216 (proven in Lean) |
| DR moves | same BFS with U and D qts | 214 the same, 2 shorter: "R-D − F-V R-V even" and its mirror "F-D − F-V R-V even" go from 9 to 8 (the count of 2 is proven in Lean) |
| Any face turn (HTM) | every sequence of ≤ 10 moves is two sequences of ≤ 5 glued together, so I listed all 624,124 of those twice, matched the pairs that can land in HTR, and tested each hit | vs DR moves: 150 the same, 37 shorter by 1, 22 by 2, 6 by 3, 1 by 4. (vs half turns: 150 / 35 / 24 / 6 / 1.) |

DR-move values never go above 10, so anything shorter is ≤ 9 moves and a search that's complete to 10 can't miss it. Against that:

The two that get shorter with quarter turns, explicitly (with half turns alone both cases need 9):

    L2 B2 D B2 L2 R2 F2 U'      // a state of "R-D − F-V R-V even"
    U F2 R2 L2 B2 D' B2 L2      // solves it in 8

    B2 L2 D L2 B2 F2 R2 U'      // a state of "F-D − F-V R-V even"
    U R2 F2 B2 L2 D' L2 B2      // solves it in 8

- **FakeMMAP's HTR-breaking table ([FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546599572644696075)) is right in 211 of 216 cells and one too high in 5.** Two of those were labelled 7 and are 6-movers, so "7 or less is proven optimal" doesn't hold for them.

  | Case | Table | Real | A state of that case |
  |---|---:|---:|---|
  | F-D + F-V R-H odd | 7 | 6 | `R L' B2 D2 R L'` |
  | R-D + F-H R-V odd | 7 | 6 | `F' B R2 D2 F B'` |
  | H-H + F-D R-D odd | 9 | 8 | `R D2 F2 B2 R' L F2 R'` |
  | H-H + F-V R-D odd | 9 | 8 | `L' F2 R L' F2 B2 D2 L` |
  | H-H + F-D R-V odd | 9 | 8 | `F L2 F B' R2 L2 D2 F'` |

  (The inverse of each sequence solves it.)
- **Rodney's sheet** has no optimal column: its Penalty is the finish length minus the corner case's setup (1 move for F-D and R-D corners, 2 for F-V, 0 for H-H). It is built on the same optimals, so the same five are one too high (6, 6, 9, 9, 9 should be 5, 5, 8, 8, 8), and the other 211 agree. One more row, labelled F-V / F-D / R-H, lists `M R2 U2 M'`, which actually gives a different case (R-V + F-D R-V odd). `M F2 U2 M'` gives the labelled case in 6 moves, the sheet's penalty of 4 after the 2-move F-V setup, so the R2 is a typo for F2.
- **Rodney's rules are still a true lower bound in all 216 cases**, even against the shorter optimals. The "100%" survives.
- **OBL++** has a finer grid and I didn't grade it cell by cell. Collapsed to these 216 labels it matches on 140 of the 144 cases it covers, already has four of the five fixes above, and is one *lower* in four (D-D ± F-H R-H even, R-V + F-D R-H even, R-V + F-D R-D odd: 8 vs my 9). For those four I ran nissy on all 3,072 states of each case and none has a solution of 8 or fewer. So 9 stands for the cases as I label them. Whether those cells are off or just mean something slightly different, I don't know.

Two sanity checks on my side: listing the HTR group directly gives 663,552 states in 216 cases of exactly 3,072 each, and all 216 sequences in Appendix C land in the case they claim.

This part is a Python script, not Lean. Nothing in either sheet beats its values, including Rodney's `F R2 E2 R2 F'` algs.

---

## 11. The proof, if you don't speak Lean

Lean is a proof checker. You write a statement and a proof, and a small trusted program checks every step. The project is about 2,500 lines, no Mathlib, and I can share it.

**What's stated.** A DR state is three lists: the piece in each of the 8 corner positions, the 8 U/D edge positions, the 4 E-slice positions. Each of the ten moves shuffles those lists in a fixed way, written out as tables (that file is 150 lines and it's the one to read if you want to convince yourself it's the cube). A solution is a list of moves that puts all three lists in order.

For each level `R` these are the theorems, copied from the files:

```lean
-- every DR-move solution w of a legal state g is at least as long as the bound
theorem Rung.lower_bound (ok : R.Checked) (g : State) (hg : g.Valid) (w : List Move)
    (hw : g.apply w = solved) : R.bound g ≤ w.length

-- same with the bound read off h, the inverse of g
theorem Rung.lower_bound_inverse (ok : R.Checked) (g h : State) (hg : g.Valid)
    (hh : h.IsInverseOf g) (w : List Move) (hw : g.apply w = solved) : R.bound h ≤ w.length

-- and the bound is reached: d moves make g look solved to R
theorem Rung.bound_attained (ok : R.Checked) : ∀ (d : Nat) (g : State), g.Valid → R.bound g = d → d < 255 →
    ∃ w : List Move, w.length = d ∧ R.index (g.apply w) = R.index solved
```

(`d < 255` is there because 255 marks combinations a real cube can't show.) `R.Checked` is the brute-force part, see below.

**How.**

1. A two-page general lemma: if what you see after a move depends only on what you saw and the move, and one move changes the table by at most 1, then n moves change it by at most n. Plain induction on the number of moves, nothing about cubes in it.
2. `R.Checked` is three brute-force checks, done by a program Lean runs:
   - for each of the 8⁸ = 16,777,216 ways to fill eight positions, if it's a permutation, the case number is in range and the case move table agrees with actually doing each of the ten moves (once for corners, once for edges);
   - on the E-slice, side turns flip the parity and the other moves don't;
   - for every table entry and every move the neighbour differs by at most 1, only the solved case has 0, and every positive entry has a neighbour that's one lower.
3. The table isn't trusted. Lean builds it with its own BFS, but nothing is assumed about that BFS, only the checks are used. A wrong table or a wrong feature would fail a check and the file wouldn't compile.
4. The inverse side needs one more fact, proven by hand: if w solves g, the inverse of g is exactly what w does to a solved cube. So its table value is at most the length of w.

**The optimal itself.** Same trick, one size up: take the table of *everything*, one entry per DR state, holding its optimal. That's 19.5 billion entries, so it's stored up to the 16 symmetries that keep the U/D axis: 2,768 corner classes × 40,320 edge arrangements × 12 E-slice arrangements = 1,339,269,120 entries, one byte each. Lean builds it with its own BFS and then checks every entry against each of the ten moves for the same three things as before: a move changes the value by at most 1, only the solved cube has 0, and every positive entry has a move that goes down by 1. On top of that it checks that entries the symmetries identify hold the same value, and nine brute-force facts about the bookkeeping: the 16 symmetries map legal states to legal states, turn each move into a move and form a group; every corner arrangement is carried to the representative of its class; moves change the three parities the way they should; and the numbering of edge and E-slice arrangements round-trips. From those:

```lean
-- every solution of g has at least exactDist g moves
theorem exact_lower (g : State) (hg : g.Valid) (hp : g.ParityOK) (w : List Move)
    (hw : g.apply w = solved) : exactDist g ≤ w.length

-- and some solution has exactly that many
theorem exact_attained (g : State) (hg : g.Valid) (hp : g.ParityOK) :
    ∃ w : List Move, w.length = exactDist g ∧ g.apply w = solved

-- nothing needs more than 18, and something does need 18
theorem exact_le_18 (g : State) (hg : g.Valid) : exactDist g ≤ 18
theorem exact_needs_18 : ∃ g : State, g.Valid ∧ g.ParityOK ∧ exactDist g = 18 ∧
    ∀ w : List Move, g.apply w = solved → 18 ≤ w.length
```

`Valid` says the three lists are permutations, `ParityOK` is the usual parity condition (corner parity + U/D edge parity = E-slice parity). Together that's exactly the states DR moves can reach: Lean proves both directions (anything you can scramble to satisfies them, and anything that satisfies them gets solved by `exact_attained`). `exactDist g` is the table entry of g's symmetry-reduced image. The witness for 18 is `U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'`.

In the same run Lean counts the table: 1, 10, 67, 456, 3079, 19948, 123074, 736850, 4185118, 22630733, 116767872, 552538680, 2176344160, 5627785188, 7172925794, 3608731814, 224058996, 1575608, 1352 at depths 0 to 18, total 19,508,428,800, where an entry counts 16 / (number of symmetries fixing the representative of its corner class) times. Same numbers as the Rust BFS. The one step that is *not* formalised is that this weighting counts states: that an entry stands for exactly that many of them. It's the standard orbit count, but here it's a paper argument, not a Lean theorem. So "1,352 states at 18" is proven up to that step, and "some state needs 18, none needs more" is proven outright.

**What's proven.** `R.Checked` for all seven levels, so all seven bounds, both sides. Plus the HT-only version of NISS@DR, that it equals FakeMMAP's 216 values, that exactly 2 of them get shorter with qts, the counterexample to Levi's formula, and the exact optimal of every DR state with its maximum of 18. The biggest bound check reads 406,425,600 entries against ten moves each and takes about 4.5 minutes. The exact-optimal check reads 1,339,269,120 and takes 17 minutes and 1.9 GB. Everything builds in under half an hour, in 3 GB of RAM if that last check is run on its own.

**What you have to trust.**

- That the move tables are the cube. They're short, and the same tables drive a separate Rust program (and an older C one with byte-identical output) whose results match Joba's per-subset counts and nissy on 40 random DRs.
- Lean's kernel, and its compiler: the brute-force checks run as compiled code (`native_decide`), which adds one axiom per check on top of the three standard ones. The general lemma itself uses none of them.

**What's not in Lean.** The stats (they're counts over the optimal of every state: the optimal is proven now, the counting isn't), the weights in the depth distribution above, the subset labels, and the DR-breaking search.

---

## 12. How it was computed and checked

- **Optimal for every DR state**: a Rust program does a BFS over the DR group reduced by the 16 symmetries that keep the U/D axis (1.34 billion reduced states, one bit per state per depth, under a minute on 4 cores, 500 MB of RAM).
- **The seven tables**: BFS over the cases of each level, then one pass over all DR states comparing bound and optimal.
- **The 216 cases with any move**: a Python script, as described above, plus nissy for the disputed cells.
- **The proof**: the Lean project builds its own tables from its own definitions. It shares nothing with the Rust code except the ten move tables and, for the exact table, the numbering of the symmetry-reduced states (so the two tables can be compared entry by entry).

What agreed with what:

| Check | Result |
|---|---|
| Total and depth distribution | 19,508,428,800; 1,352 at 18 ([Tomas Rokicki, 31 May 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1510792489236430968)) |
| Joba's optimal distribution, all 48 subsets ([Joba, 17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406633631165714492)) | same in every cell |
| Subset sizes, qt class sizes ([Oskar, 10 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1249777335239184405), [Joba, 3 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1357402650441945299)), 4a3↔4b3 on inverse (wen's "HTR better smh (v2)" sheet) | same |
| FakeMMAP's 216 values ([FakeMMAP, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546077758189477989)) | same |
| FakeMMAP's corner counts per qt, 24 / 144 / 720 / 1416 / 1776 / 960 of 5040 ([FakeMMAP, 26 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1144917908078723112), FakeMMAP asked someone to check them) | confirmed |
| Lean's proven optimal table vs the Rust BFS | same in all 1,339,269,120 entries, and the same depth distribution |
| Lean vs the Rust program, bound tables | same case counts (96, 420, 70, 5040, 630, 10080), same distribution of the corner and HTR tables, same bounds on the examples |
| Rust vs the first C version | every output byte-identical |
| nissy `drudfin` on 40 random DRs | same optimal on all 40 |
| Bounds vs optimal | never above it, any level, any of the 19.5 billion states |

For the hand reads in sections 5 to 8:

- **Leave slice**: a second BFS over corners and U/D-layer edges only, reduced by the same 16 symmetries (111,605,760 reduced states, five seconds). It reaches all 19,508,428,800 states when each is counted with its 12 E-slice arrangements.
- **The reads**: three more passes over all DR states. Each computes the read for the state (and for its inverse where that's a different thing) and adds the state's optimal to a histogram. Every pass counts exactly 19,508,428,800 states.
- **Pairs**: the four kinds are defined by the colours of the two touching sticker pairs, as in Rodney's message. Checked on Rodney's example: after `B2 L2 B2 R2` the UF edge has a top semi-pair on one side and a side semi-pair on the other, which is what Rodney says it sets up.
- **Corner cases**: classes of the 420 HTR corner cosets under the 16 symmetries and under turning both layers. There are 46.
- **Setup lengths** for the setup + HTR bound: breadth-first over the 29,400 HTR cosets with half turns only, until some quarter turn lowers the minimum qt count. At 1qt it has to give the shortest 1qt HTR minus one, and it does.
- **The 500 scrambles** (the guide's real-scramble numbers and the tally on the examples page): uniformly random states drawn with the EO → DR study's generator, written with R' U' F at both ends. An earlier version of this page used nissy's scrambler, which is not uniform ([EO → DR study, appendix B](https://fmc.arhan.sh/eo-to-dr/#appendix-b-how-it-was-computed-and-what-checks-it)).
- **Example scrambles**: every scramble quoted as an example of something was found by a search over all DR states, then re-read from its text alone (subset, HTR lengths, leave slice and optimal recomputed from the moves). The ones that stand against something a person wrote were also solved with nissy.
- **What the server has said**: all of #fmc-theory and #fmc-discussion (about 33,000 messages, August 2022 to November 2026) was reread line by line for this version, looking for what people read off a DR, how they discard, and what they asked for. Every quote above was checked against the export.

---

## 13. What this doesn't do

- **DR moves only.** "Optimal" here is U, D, R2, L2, F2, B2. A finish that breaks DR is shorter for 4.3% of DR states (± 0.1 points), by one move in 90% of those, 0.048 moves on average (48,000 uniform states, 1,000 per subset × edges, solved with all 18 face turns by nissy's `solve optimal`; 4.2% on real DRs with each DR counted once, 3.9% with each scramble once). For a DR whose DR-move optimum is 12 or less it is 1.1%; it climbs only on long finishes (9.4% at 15, 36% at 16). Most of it sits in three cells: 0c3 0e 36%, 0c4 0e 26%, 0c0 0e 21%. Example: `B2 L2 R2 F2 R2 U2 L2 R2 U2 R2 U2` (0c0 0e, DR moves only) has a DR-move optimum of 11 and `R L F2 B2 R' L' D2` solves it in 7. At the HTR level that's 66 of the 216 cases. Computed with nissy, not in Lean; every solution quoted was replayed on a sticker model.
- **Uniform states.** Every DR state counts once. Measured against the DRs you actually reach, that is close to right. The test: 10,000 uniformly random scrambles, every EO-first DR of at most 11 moves cubelib-cli lists for each, as on the examples page (6,840,923 DRs), counted once per DR and once per scramble, standard errors clustered by scramble. Every corner subset's share is within 0.4 points of uniform, its average optimal within 0.05 moves, and its share finishing in 11 within 0.5 points (1.3 on 0c0). The "all DRs" numbers hold too: the HTR routes study's all-DR headlines move by at most 0.4 points. What does shift is the bad-edge mix inside a subset: with each scramble counted once, 0e is up to 43% rarer than uniform and 6e up to 17% commoner. Not modelled: CO-first or direct DRs, EOs over 5 moves, the twin of a DR with its last move turned the other way (counted once), and which DRs a solver chooses to keep. Computed, not proven; the full tables are in the [HTR routes study's real-DR section](https://fmc.arhan.sh/htr-routes/#12-real-drs).
- **No hand bound for a 12 at 4–5qt.** That was the hope and it isn't here. What's here is the measurement that says a feature count won't give one, the reads ranked by what they buy at each target, and the kill rules that do exist. For a 10 or an 11 the two proven hand bounds do rule out a good share of 4–5qt DRs (section 5), but those are DRs you were dropping anyway.
- **Your HTR may not be the shortest.** Every HTR number assumes the shortest HTR on each side. How often a solver finds it, and how fast, is not something a BFS can measure.
- **Reads I didn't test.** Bigger blocks than pairs, anything you only see after a few moves (moves to FR, the shape after the first qt), and Rodney's NISS@1qt features per skeleton, which is section 9's table rather than a read.
- **Width is only first moves.** JTuu's real question, how many finishes are within one of optimal, needs a count of solutions per state. Not done.
- **Not done either**: what share of DRs have an optimal finish that goes through a shortest HTR ([Zagros, 27 Dec 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1454570265353912422)), and how many U2/D2 an optimal has per subset ([wen, 8 May 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1502269153774669904)).
- **Stats are counted, not proven.** The optimal of every state is a Lean theorem, and the table the stats are counted from is that same table, entry for entry. What isn't formal is the counting on top: the percentages, the reads, and the symmetry weights behind "1,352 states at 18".

---

## Appendix A: all 48 subsets

Exact over all DR states. Fastest and Longest are the shortest and the longest optimal finish in the subset (the longest is God's number for the subset in DR moves). Every column counts DR-move finishes. With all 18 face turns allowed a finish is sometimes shorter (section 13), so for any moves the "In N" shares are lower bounds; it matters on 0c3 0e (shorter on 36% of states), 0c4 0e (shorter on 26% of states), 0c0 0e (shorter on 21% of states). The 18-move states were not solved with all moves.

| Subset | Share of all DRs | Avg optimal | Fastest | Longest | In 9 | In 10 | In 11 | In 12 | In 13 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0c0 0e | 0.01% | 9.95 | 0 | 13 | 34% | 64% | 90% | 99.2% | 100% |
| 0c0 2e | 0.11% | 11.69 | 5 | 15 | 2.6% | 11% | 38% | 80% | 99% |
| 0c0 4e | 0.24% | 12.31 | 4 | 16 | 0.99% | 4.5% | 18% | 53% | 93% |
| 0c0 6e | 0.11% | 12.92 | 7 | 16 | 0.11% | 0.93% | 5.8% | 27% | 75% |
| 0c0 8e | 0.01% | 12.69 | 6 | 18 | 0.57% | 3.0% | 13% | 39% | 78% |
| 4a1 0e | 0.08% | 13.01 | 7 | 16 | 0.11% | 0.85% | 5.1% | 24% | 70% |
| 4a1 2e | 1.31% | 12.56 | 6 | 16 | 0.39% | 2.3% | 12% | 42% | 88% |
| 4a1 4e | 1.47% | 12.27 | 1 | 17 | 1.7% | 6.4% | 21% | 53% | 91% |
| 4a2 0e | 0.08% | 13.91 | 9 | 17 | <0.01% | 0.09% | 0.86% | 6.1% | 29% |
| 4a2 2e | 1.31% | 13.65 | 8 | 17 | 0.03% | 0.26% | 1.8% | 10% | 39% |
| 4a2 4e | 1.47% | 13.05 | 5 | 16 | 0.39% | 1.9% | 7.7% | 26% | 64% |
| 4b2 0e | 0.33% | 12.89 | 6 | 16 | 0.24% | 1.5% | 7.2% | 28% | 74% |
| 4b2 2e | 5.22% | 12.61 | 3 | 16 | 0.59% | 2.7% | 11% | 39% | 85% |
| 4b2 4e | 5.88% | 12.73 | 4 | 16 | 0.32% | 1.8% | 8.8% | 34% | 82% |
| 0c3 0e | 0.02% | 14.08 | 10 | 17 | 0 | 0.04% | 0.75% | 5.7% | 26% |
| 0c3 2e | 0.33% | 14.27 | 9 | 17 | <0.01% | 0.07% | 0.58% | 3.7% | 17% |
| 0c3 4e | 0.73% | 14.64 | 10 | 18 | 0 | 0.01% | 0.18% | 1.5% | 8.9% |
| 0c3 6e | 0.33% | 14.29 | 9 | 17 | <0.01% | 0.07% | 0.58% | 3.7% | 18% |
| 0c3 8e | 0.02% | 14.14 | 10 | 17 | 0 | 0.04% | 0.75% | 5.6% | 25% |
| 2c3 0e | 0.22% | 13.39 | 9 | 16 | <0.01% | 0.16% | 1.7% | 12% | 52% |
| 2c3 2e | 3.48% | 12.55 | 5 | 15 | 0.46% | 2.5% | 12% | 42% | 88% |
| 2c3 4e | 7.84% | 12.94 | 5 | 16 | 0.22% | 1.3% | 6.4% | 27% | 73% |
| 2c3 6e | 3.48% | 13.20 | 7 | 16 | 0.06% | 0.47% | 3.2% | 17% | 61% |
| 2c3 8e | 0.22% | 13.52 | 9 | 16 | <0.01% | 0.13% | 1.3% | 9.6% | 45% |
| 4c3 0e | 0.33% | 13.31 | 8 | 16 | 0.07% | 0.57% | 3.6% | 17% | 54% |
| 4c3 2e | 5.22% | 13.48 | 7 | 16 | 0.05% | 0.35% | 2.2% | 12% | 46% |
| 4c3 4e | 5.88% | 13.50 | 7 | 16 | 0.05% | 0.35% | 2.3% | 12% | 45% |
| 0c4 0e | 0.01% | 13.22 | 9 | 16 | 0.03% | 0.36% | 3.1% | 17% | 61% |
| 0c4 2e | 0.22% | 13.52 | 9 | 16 | <0.01% | 0.12% | 1.2% | 8.9% | 44% |
| 0c4 4e | 0.49% | 13.64 | 9 | 16 | <0.01% | 0.09% | 0.90% | 6.9% | 37% |
| 0c4 6e | 0.22% | 13.90 | 10 | 16 | 0 | 0.02% | 0.36% | 3.6% | 24% |
| 0c4 8e | 0.01% | 14.18 | 11 | 16 | 0 | 0 | 0.11% | 1.9% | 16% |
| 2c4 0e | 0.33% | 13.22 | 7 | 16 | 0.14% | 0.90% | 4.7% | 20% | 59% |
| 2c4 2e | 5.22% | 13.53 | 7 | 17 | 0.04% | 0.31% | 2.1% | 11% | 44% |
| 2c4 4e | 11.76% | 13.66 | 7 | 16 | 0.03% | 0.23% | 1.6% | 9.1% | 38% |
| 2c4 6e | 5.22% | 13.73 | 8 | 17 | 0.01% | 0.14% | 1.2% | 7.7% | 35% |
| 2c4 8e | 0.33% | 14.02 | 9 | 17 | <0.01% | 0.05% | 0.58% | 4.5% | 24% |
| 4c4 0e | 0.33% | 14.54 | 10 | 17 | 0 | 0.01% | 0.13% | 1.2% | 8.8% |
| 4c4 2e | 5.22% | 14.42 | 9 | 17 | <0.01% | 0.02% | 0.17% | 1.5% | 11% |
| 4c4 4e | 5.88% | 14.38 | 9 | 17 | <0.01% | 0.02% | 0.21% | 1.8% | 12% |
| 2c5 0e | 0.11% | 14.42 | 10 | 18 | 0 | <0.01% | 0.14% | 1.5% | 11% |
| 2c5 2e | 1.74% | 14.28 | 9 | 17 | <0.01% | 0.03% | 0.30% | 2.5% | 16% |
| 2c5 4e | 3.92% | 14.30 | 9 | 18 | <0.01% | 0.03% | 0.33% | 2.6% | 15% |
| 2c5 6e | 1.74% | 14.42 | 9 | 17 | <0.01% | 0.01% | 0.18% | 1.7% | 12% |
| 2c5 8e | 0.11% | 14.46 | 10 | 17 | 0 | 0.01% | 0.14% | 1.5% | 11% |
| 4b5 0e | 0.33% | 14.30 | 9 | 17 | <0.01% | 0.02% | 0.22% | 2.0% | 13% |
| 4b5 2e | 5.22% | 14.26 | 9 | 16 | <0.01% | 0.02% | 0.23% | 2.0% | 14% |
| 4b5 4e | 5.88% | 14.29 | 9 | 17 | <0.01% | 0.01% | 0.19% | 1.8% | 13% |

What is proven, per subset. "Hand" is the better of the two guaranteed hand bounds (longer HTR, corner length with the right parity). The other two are the computer tables of section 9.

| Subset | No 10: hand | No 10: NISS@DR | No 10: everything | No 11: hand | No 11: NISS@DR | No 11: everything | No 12: hand | No 12: NISS@DR | No 12: everything |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0c0 0e | 0 | 0.46% | 15% | 0 | 0 | 3.1% | 0 | 0 | 0 |
| 0c0 2e | 0 | 13% | 44% | 0 | 0 | 14% | 0 | 0 | 0.80% |
| 0c0 4e | 0 | 50% | 78% | 0 | 9.9% | 45% | 0 | 0.04% | 8.1% |
| 0c0 6e | 0 | 66% | 90% | 0 | 16% | 65% | 0 | 0.81% | 21% |
| 0c0 8e | 0 | 56% | 78% | 0 | 22% | 52% | 0 | 3.2% | 20% |
| 4a1 0e | 0 | 87% | 94% | 0 | 59% | 80% | 0 | 12% | 43% |
| 4a1 2e | 0 | 41% | 89% | 0 | 4.1% | 58% | 0 | 0 | 11% |
| 4a1 4e | 0 | 41% | 77% | 0 | 7.1% | 46% | 0 | 0.09% | 8.8% |
| 4a2 0e | 75% | 97% | 99.4% | 31% | 90% | 96% | 0 | 57% | 84% |
| 4a2 2e | 31% | 93% | 98% | 1.4% | 70% | 92% | 0 | 28% | 69% |
| 4a2 4e | 13% | 75% | 93% | 1.4% | 45% | 77% | 0 | 16% | 46% |
| 4b2 0e | 0 | 72% | 92% | 0 | 25% | 73% | 0 | 1.0% | 33% |
| 4b2 2e | 0 | 46% | 89% | 0 | 4.8% | 61% | 0 | 0 | 15% |
| 4b2 4e | 0 | 60% | 92% | 0 | 10% | 69% | 0 | 0.09% | 21% |
| 0c3 0e | 94% | 99.4% | 99.7% | 50% | 96% | 97% | 14% | 80% | 86% |
| 0c3 2e | 93% | 99% | 99.8% | 50% | 94% | 99% | 14% | 67% | 93% |
| 0c3 4e | 99.6% | 99.9% | 99.9% | 92% | 99% | 99.6% | 26% | 93% | 96% |
| 0c3 6e | 93% | 99% | 99.8% | 50% | 94% | 99% | 14% | 66% | 93% |
| 0c3 8e | 94% | 99.4% | 99.7% | 50% | 96% | 97% | 14% | 80% | 86% |
| 2c3 0e | 0 | 93% | 99.4% | 0 | 59% | 93% | 0 | 11% | 63% |
| 2c3 2e | 0 | 35% | 90% | 0 | 2.5% | 58% | 0 | 0 | 10% |
| 2c3 4e | 0 | 66% | 95% | 0 | 17% | 78% | 0 | 0.17% | 31% |
| 2c3 6e | 0 | 82% | 98% | 0 | 27% | 87% | 0 | 0.27% | 45% |
| 2c3 8e | 0 | 93% | 99.6% | 0 | 61% | 95% | 0 | 11% | 67% |
| 4c3 0e | 19% | 87% | 98% | 0 | 56% | 88% | 0 | 16% | 58% |
| 4c3 2e | 19% | 93% | 99.1% | 0 | 55% | 94% | 0 | 9.2% | 67% |
| 4c3 4e | 22% | 92% | 99.2% | 0 | 60% | 94% | 0 | 14% | 68% |
| 0c4 0e | 33% | 73% | 99% | 0 | 17% | 89% | 0 | 0 | 46% |
| 0c4 2e | 33% | 98% | 99.8% | 0 | 66% | 98% | 0 | 3.7% | 77% |
| 0c4 4e | 33% | 98% | 99.8% | 0 | 74% | 98% | 0 | 8.9% | 82% |
| 0c4 6e | 33% | 99.2% | 99.9% | 0 | 89% | 99.2% | 0 | 27% | 90% |
| 0c4 8e | 100% | 100% | 100% | 0 | 93% | 99.5% | 0 | 56% | 92% |
| 2c4 0e | 31% | 80% | 96% | 9.4% | 48% | 84% | 0.69% | 15% | 50% |
| 2c4 2e | 31% | 92% | 99.1% | 9.4% | 56% | 94% | 0.69% | 12% | 68% |
| 2c4 4e | 32% | 94% | 99.4% | 9.4% | 65% | 95% | 0.69% | 18% | 74% |
| 2c4 6e | 31% | 96% | 99.6% | 9.4% | 69% | 97% | 0.69% | 20% | 78% |
| 2c4 8e | 52% | 97% | 99.8% | 9.4% | 82% | 98% | 0.69% | 47% | 83% |
| 4c4 0e | 94% | 99.4% | 99.9% | 58% | 95% | 99.7% | 25% | 75% | 96% |
| 4c4 2e | 92% | 99.9% | 99.9% | 49% | 98% | 99.7% | 14% | 71% | 97% |
| 4c4 4e | 89% | 99.7% | 99.9% | 50% | 96% | 99.7% | 14% | 67% | 97% |
| 2c5 0e | 86% | 99.1% | 99.9% | 49% | 95% | 99.6% | 22% | 78% | 95% |
| 2c5 2e | 80% | 99.2% | 99.9% | 51% | 92% | 99% | 22% | 59% | 93% |
| 2c5 4e | 82% | 99.3% | 99.9% | 51% | 93% | 99% | 22% | 61% | 93% |
| 2c5 6e | 84% | 99.6% | 99.9% | 56% | 94% | 99.4% | 22% | 65% | 95% |
| 2c5 8e | 86% | 99.5% | 99.9% | 58% | 97% | 99.4% | 22% | 81% | 95% |
| 4b5 0e | 69% | 99.1% | 99.9% | 29% | 94% | 99.2% | 6.9% | 62% | 94% |
| 4b5 2e | 70% | 99.7% | 99.9% | 29% | 94% | 99.5% | 6.9% | 51% | 96% |
| 4b5 4e | 86% | 99.7% | 99.9% | 29% | 96% | 99.6% | 6.9% | 60% | 96% |

---

## Appendix B: odds by corner length and E-slice parity

For the big 3–5qt subsets. L = optimal corner solution. "Fastest" is the shortest optimal finish in the row, so `L+1` means no L-move finish exists there.

| Subset | L | E-slice | Share of subset | Fastest | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|
| 4c3 4e | 7 | even | 2.8% | 8 (L+1) | 13.03 | 1.5% | 6.5% | 22% | 68% |
| 4c3 4e | 7 | odd | 2.8% | 7 (L+0) | 12.95 | 0.92% | 6.5% | 29% | 70% |
| 4c3 4e | 8 | even | 11.1% | 8 (L+0) | 13.15 | 0.78% | 3.5% | 19% | 64% |
| 4c3 4e | 8 | odd | 11.1% | 9 (L+1) | 13.20 | 0.60% | 4.1% | 19% | 60% |
| 4c3 4e | 9 | even | 19.4% | 9 (L+0) | 13.43 | 0.29% | 2.5% | 11% | 49% |
| 4c3 4e | 9 | odd | 19.4% | 9 (L+0) | 13.45 | 0.33% | 1.9% | 13% | 47% |
| 4c3 4e | 10 | even | 13.9% | 11 (L+1) | 13.80 | 0 | 1.3% | 3.6% | 32% |
| 4c3 4e | 10 | odd | 13.9% | 10 (L+0) | 13.86 | 0.09% | 0.23% | 7.5% | 25% |
| 4c3 4e | 11 | even | 2.8% | 11 (L+0) | 14.05 | 0 | 0.20% | 2.5% | 17% |
| 4c3 4e | 11 | odd | 2.8% | 11 (L+0) | 14.13 | 0 | 0.14% | 2.8% | 21% |
| 0c3 4e | 9 | even | 2.8% | 11 (L+2) | 13.68 | 0 | 2.6% | 4.5% | 38% |
| 0c3 4e | 9 | odd | 2.8% | 10 (L+1) | 13.86 | 0.44% | 0.46% | 8.7% | 30% |
| 0c3 4e | 10 | even | 11.1% | 11 (L+1) | 14.22 | 0 | 0.85% | 0.89% | 22% |
| 0c3 4e | 10 | odd | 11.1% | 12 (L+2) | 14.16 | 0 | 0 | 6.5% | 10% |
| 0c3 4e | 11 | even | 22.2% | 12 (L+1) | 14.73 | 0 | 0 | 0.44% | 8.4% |
| 0c3 4e | 11 | odd | 22.2% | 12 (L+1) | 14.72 | 0 | 0 | 0.82% | 4.6% |
| 0c3 4e | 12 | even | 13.9% | 13 (L+1) | 14.96 | 0 | 0 | 0 | 0.17% |
| 0c3 4e | 12 | odd | 13.9% | 13 (L+1) | 15.09 | 0 | 0 | 0 | 4.0% |
| 2c4 4e | 7 | even | 2.8% | 8 (L+1) | 13.15 | 0.52% | 4.3% | 15% | 66% |
| 2c4 4e | 7 | odd | 2.8% | 7 (L+0) | 13.15 | 0.81% | 3.7% | 23% | 59% |
| 2c4 4e | 8 | even | 11.1% | 8 (L+0) | 13.29 | 0.51% | 3.6% | 13% | 59% |
| 2c4 4e | 8 | odd | 11.1% | 9 (L+1) | 13.37 | 0.47% | 2.0% | 17% | 49% |
| 2c4 4e | 9 | even | 17.0% | 9 (L+0) | 13.61 | 0.09% | 1.8% | 6.6% | 41% |
| 2c4 4e | 9 | odd | 17.0% | 9 (L+0) | 13.58 | 0.26% | 1.3% | 11% | 39% |
| 2c4 4e | 10 | even | 13.2% | 10 (L+0) | 13.84 | 0.04% | 1.1% | 3.9% | 31% |
| 2c4 4e | 10 | odd | 13.2% | 10 (L+0) | 13.90 | 0.10% | 0.22% | 6.5% | 24% |
| 2c4 4e | 11 | even | 5.2% | 11 (L+0) | 14.16 | 0 | 0.31% | 2.0% | 14% |
| 2c4 4e | 11 | odd | 5.2% | 11 (L+0) | 14.28 | 0 | 0.08% | 1.9% | 16% |
| 2c4 4e | 12 | even | 0.7% | 12 (L+0) | 14.37 | 0 | 0 | 1.6% | 2.8% |
| 2c4 4e | 12 | odd | 0.7% | 13 (L+1) | 14.55 | 0 | 0 | 0 | 12% |
| 0c4 4e | 9 | even | 16.7% | 9 (L+0) | 13.62 | 0.05% | 1.5% | 5.4% | 37% |
| 0c4 4e | 9 | odd | 16.7% | 10 (L+1) | 13.64 | 0.24% | 0.42% | 8.6% | 39% |
| 0c4 4e | 10 | even | 33.3% | 11 (L+1) | 13.62 | 0 | 1.3% | 5.6% | 37% |
| 0c4 4e | 10 | odd | 33.3% | 10 (L+0) | 13.67 | 0.12% | 0.46% | 8.1% | 37% |
| 4c4 4e | 9 | even | 2.8% | 9 (L+0) | 13.79 | 0.04% | 1.5% | 4.4% | 31% |
| 4c4 4e | 9 | odd | 2.8% | 10 (L+1) | 13.85 | 0.37% | 0.58% | 7.2% | 29% |
| 4c4 4e | 10 | even | 11.1% | 11 (L+1) | 14.03 | 0 | 0.86% | 2.9% | 21% |
| 4c4 4e | 10 | odd | 11.1% | 10 (L+0) | 14.05 | 0.06% | 0.20% | 4.5% | 19% |
| 4c4 4e | 11 | even | 22.2% | 11 (L+0) | 14.37 | 0 | 0.06% | 1.4% | 8.1% |
| 4c4 4e | 11 | odd | 22.2% | 11 (L+0) | 14.42 | 0 | 0.07% | 1.1% | 13% |
| 4c4 4e | 12 | even | 13.9% | 12 (L+0) | 14.68 | 0 | 0 | 0.57% | 1.5% |
| 4c4 4e | 12 | odd | 13.9% | 13 (L+1) | 14.79 | 0 | 0 | 0 | 5.8% |
| 2c5 4e | 9 | even | 4.2% | 9 (L+0) | 13.75 | 0.11% | 1.7% | 5.8% | 29% |
| 2c5 4e | 9 | odd | 4.2% | 10 (L+1) | 13.96 | 0.11% | 0.76% | 4.4% | 31% |
| 2c5 4e | 10 | even | 14.6% | 11 (L+1) | 14.04 | 0 | 0.48% | 3.7% | 16% |
| 2c5 4e | 10 | odd | 14.6% | 10 (L+0) | 13.96 | 0.17% | 0.44% | 6.1% | 27% |
| 2c5 4e | 11 | even | 17.2% | 11 (L+0) | 14.20 | 0 | 0.41% | 2.4% | 13% |
| 2c5 4e | 11 | odd | 17.2% | 11 (L+0) | 14.41 | 0 | 0.12% | 0.80% | 17% |
| 2c5 4e | 12 | even | 9.9% | 12 (L+0) | 14.49 | 0 | 0 | 1.3% | 2.4% |
| 2c5 4e | 12 | odd | 9.9% | 12 (L+0) | 14.64 | 0 | 0 | 0.17% | 11% |
| 2c5 4e | 13 | even | 4.2% | 13 (L+0) | 15.01 | 0 | 0 | 0 | 1.3% |
| 2c5 4e | 13 | odd | 4.2% | 13 (L+0) | 15.30 | 0 | 0 | 0 | 1.8% |
| 4b5 4e | 9 | even | 5.6% | 9 (L+0) | 13.96 | 0.02% | 0.59% | 3.9% | 17% |
| 4b5 4e | 9 | odd | 5.6% | 10 (L+1) | 14.16 | 0.02% | 0.31% | 2.0% | 26% |
| 4b5 4e | 10 | even | 20.8% | 11 (L+1) | 14.19 | 0 | 0.20% | 2.5% | 8.8% |
| 4b5 4e | 10 | odd | 20.8% | 10 (L+0) | 14.22 | 0.06% | 0.21% | 2.6% | 21% |
| 4b5 4e | 11 | even | 20.8% | 11 (L+0) | 14.31 | 0 | 0.20% | 1.5% | 8.5% |
| 4b5 4e | 11 | odd | 20.8% | 11 (L+0) | 14.52 | 0 | 0.03% | 0.44% | 13% |
| 4b5 4e | 12 | even | 2.8% | 12 (L+0) | 14.49 | 0 | 0 | 1.0% | 1.9% |
| 4b5 4e | 12 | odd | 2.8% | 12 (L+0) | 14.50 | 0 | 0 | 0.70% | 11% |

---

## Appendix C: the 216 NISS@1qt cases

Labels are FakeMMAP's (corner case with cs sign, M-slice edges, S-slice edges, E-parity). HT = half turns only (FakeMMAP's first BFS), DR = DR moves, Any = any of the 18 face turns. The sequence makes a state of the case in "Any" moves, so its inverse is an optimal solution.

| Corners | F edges | R edges | E | HT | DR | Any | Sequence |
|---|---|---|---|---:|---:|---:|---|
| H-H + | F-H | R-H | even | 0 | 0 | 0 | ` ` |
| R-D + | F-H | R-D | odd | 1 | 1 | 1 | ` L2` |
| F-D + | F-D | R-H | odd | 1 | 1 | 1 | ` B2` |
| R-V + | F-H | R-V | odd | 2 | 2 | 2 | ` L2 D2` |
| R-D - | F-D | R-D | even | 2 | 2 | 2 | ` L2 B2` |
| F-V + | F-V | R-H | odd | 2 | 2 | 2 | ` B2 D2` |
| F-D - | F-D | R-D | even | 2 | 2 | 2 | ` B2 L2` |
| R-V + | F-H | R-V | even | 3 | 3 | 3 | ` L2 D2 L2` |
| D-D + | F-D | R-V | even | 3 | 3 | 3 | ` L2 D2 B2` |
| R-V - | F-V | R-V | even | 3 | 3 | 3 | ` L2 B2 D2` |
| H-H - | F-D | R-H | odd | 3 | 3 | 3 | ` L2 B2 L2` |
| D-D - | F-V | R-D | even | 3 | 3 | 3 | ` B2 D2 L2` |
| F-V + | F-V | R-H | even | 3 | 3 | 3 | ` B2 D2 B2` |
| F-V - | F-V | R-V | even | 3 | 3 | 3 | ` B2 L2 D2` |
| H-H - | F-H | R-D | odd | 3 | 3 | 3 | ` F2 R2 F2` |
| R-D + | F-H | R-D | even | 4 | 4 | 4 | ` L2 D2 L2 D2` |
| D-D + | F-D | R-V | odd | 4 | 4 | 4 | ` L2 D2 L2 B2` |
| F-V - | F-D | R-V | odd | 4 | 4 | 4 | ` L2 D2 B2 L2` |
| R-V - | F-V | R-V | odd | 4 | 4 | 4 | ` L2 B2 D2 L2` |
| D-D - | F-V | R-V | odd | 4 | 4 | 4 | ` L2 F2 U2 F2` |
| H-H - | F-V | R-H | odd | 4 | 4 | 4 | ` L2 B2 L2 D2` |
| F-D - | F-H | R-H | even | 4 | 4 | 4 | ` L2 B2 L2 B2` |
| R-V - | F-V | R-D | odd | 4 | 4 | 4 | ` F2 U2 R2 F2` |
| F-D + | F-D | R-H | even | 4 | 4 | 4 | ` B2 D2 B2 D2` |
| D-D - | F-V | R-D | odd | 4 | 4 | 4 | ` F2 U2 F2 L2` |
| D-D + | F-V | R-V | odd | 4 | 4 | 4 | ` B2 L2 D2 L2` |
| F-V - | F-V | R-V | odd | 4 | 4 | 4 | ` B2 L2 D2 B2` |
| H-H - | F-H | R-V | odd | 4 | 4 | 4 | ` F2 R2 F2 D2` |
| R-D - | F-H | R-H | even | 4 | 4 | 4 | ` B2 L2 B2 L2` |
| H-H + | F-H | R-H | odd | 5 | 5 | 5 | ` R2 U2 L2 U2 R2` |
| R-D - | F-D | R-D | odd | 5 | 5 | 5 | ` L2 D2 L2 D2 B2` |
| F-V - | F-D | R-V | even | 5 | 5 | 5 | ` R2 D2 L2 B2 R2` |
| F-D - | F-V | R-D | odd | 5 | 5 | 5 | ` L2 D2 B2 L2 D2` |
| F-V - | F-H | R-V | even | 5 | 5 | 5 | ` L2 D2 F2 R2 F2` |
| D-D - | F-V | R-V | even | 5 | 5 | 5 | ` L2 F2 U2 R2 F2` |
| D-D + | F-D | R-D | odd | 5 | 5 | 5 | ` L2 F2 U2 F2 D2` |
| F-V + | F-V | R-V | even | 5 | 5 | 5 | ` R2 B2 D2 B2 R2` |
| R-D - | F-V | R-D | even | 5 | 5 | 5 | ` R2 B2 L2 D2 R2` |
| F-D - | F-V | R-H | even | 5 | 5 | 5 | ` L2 B2 L2 D2 B2` |
| F-V - | F-H | R-H | even | 5 | 5 | 5 | ` L2 B2 L2 B2 D2` |
| F-D + | F-H | R-D | odd | 5 | 5 | 5 | ` R2 B2 R2 B2 R2` |
| R-D - | F-D | R-V | odd | 5 | 5 | 5 | ` F2 U2 R2 F2 D2` |
| R-V - | F-V | R-H | even | 5 | 5 | 5 | ` B2 D2 L2 B2 L2` |
| F-D - | F-D | R-D | odd | 5 | 5 | 5 | ` B2 D2 B2 D2 L2` |
| R-V - | F-V | R-D | even | 5 | 5 | 5 | ` B2 D2 F2 R2 F2` |
| D-D - | F-D | R-D | odd | 5 | 5 | 5 | ` B2 L2 D2 L2 D2` |
| R-V + | F-V | R-V | even | 5 | 5 | 5 | ` F2 R2 U2 R2 F2` |
| D-D + | F-V | R-V | even | 5 | 5 | 5 | ` F2 R2 U2 F2 L2` |
| R-D - | F-H | R-V | even | 5 | 5 | 5 | ` F2 R2 F2 D2 L2` |
| F-D - | F-D | R-V | even | 5 | 5 | 5 | ` F2 R2 F2 D2 B2` |
| R-V - | F-H | R-H | even | 5 | 5 | 5 | ` B2 L2 B2 L2 D2` |
| R-D + | F-D | R-H | odd | 5 | 5 | 5 | ` F2 R2 B2 R2 F2` |
| H-H - | F-D | R-H | even | 6 | 6 | 6 | `L2 B2 D2 L2 D2 L2` |
| F-D - | F-V | R-D | even | 6 | 6 | 6 | `R2 U2 R2 F2 L2 U2` |
| F-V - | F-H | R-V | odd | 6 | 6 | 6 | `R2 D2 L2 F2 L2 F2` |
| F-D + | F-V | R-H | even | 6 | 6 | 6 | `R2 U2 F2 L2 U2 R2` |
| H-H - | F-V | R-D | even | 6 | 6 | 6 | `L2 D2 F2 R2 U2 F2` |
| F-D - | F-H | R-D | even | 6 | 6 | 5 | ` R L' D2 R' L'` |
| D-D + | F-H | R-V | odd | 6 | 6 | 6 | `F2 R' L' F2 R L` |
| D-D + | F-D | R-D | even | 6 | 6 | 6 | `L2 F2 U2 R2 F2 D2` |
| F-V + | F-V | R-V | odd | 6 | 6 | 6 | `F' B R2 F B D2` |
| F-V - | F-D | R-H | even | 6 | 6 | 6 | `L2 B2 D2 B2 D2 L2` |
| R-V + | F-H | R-D | even | 6 | 6 | 6 | `L2 B2 D2 F2 U2 F2` |
| F-D + | F-D | R-D | even | 6 | 6 | 6 | `R2 B2 D2 B2 R2 D2` |
| R-V - | F-D | R-V | even | 6 | 6 | 6 | `R2 B2 L2 D2 R2 D2` |
| R-D + | F-V | R-D | odd | 6 | 6 | 6 | `R2 F2 R2 U2 L2 F2` |
| F-D + | F-V | R-D | odd | 6 | 6 | 6 | `R2 B2 R2 D2 B2 R2` |
| D-D + | F-H | R-D | odd | 6 | 6 | 6 | `R2 F2 R2 F2 D2 R2` |
| F-V - | F-D | R-H | odd | 6 | 6 | 6 | `L2 B2 L2 B2 D2 B2` |
| F-V + | F-H | R-V | odd | 6 | 6 | 6 | `R2 B2 R2 B2 R2 D2` |
| H-H + | F-D | R-D | even | 6 | 6 | 6 | `R2 F2 L2 B2 L2 F2` |
| H-H - | F-D | R-V | even | 6 | 6 | 6 | `F2 U2 R2 F2 D2 L2` |
| R-D + | F-H | R-V | even | 6 | 6 | 6 | `F2 U2 R2 F2 D2 B2` |
| R-D - | F-D | R-H | even | 6 | 6 | 5 | ` F' B D2 F B` |
| D-D - | F-V | R-H | odd | 6 | 6 | 6 | `L2 F B L2 F' B'` |
| H-H - | F-H | R-D | even | 6 | 6 | 6 | `F2 U2 B2 U2 R2 F2` |
| R-D - | F-D | R-V | even | 6 | 6 | 6 | `F' B R2 D2 F B` |
| R-V - | F-V | R-H | odd | 6 | 6 | 6 | `B2 D2 B2 L2 B2 L2` |
| F-V + | F-D | R-H | even | 6 | 6 | 6 | `B2 R2 U2 L2 U2 R2` |
| R-V - | F-H | R-D | even | 6 | 6 | 6 | `F2 R2 U2 R2 U2 F2` |
| R-D + | F-D | R-D | even | 6 | 6 | 6 | `F2 R2 U2 R2 F2 D2` |
| R-V + | F-V | R-V | odd | 6 | 6 | 6 | `R' L B2 R L D2` |
| D-D - | F-D | R-D | even | 6 | 6 | 6 | `R' L D2 B2 R' L'` |
| R-D + | F-D | R-V | odd | 6 | 6 | 6 | `F2 R2 F2 D2 L2 B2` |
| F-V - | F-V | R-D | even | 6 | 6 | 6 | `F' B' D2 R2 F B'` |
| F-D + | F-D | R-V | odd | 6 | 6 | 6 | `B2 R2 B2 D2 B2 R2` |
| R-V - | F-H | R-D | odd | 6 | 6 | 6 | `F2 L2 F2 L2 D2 R2` |
| D-D - | F-D | R-H | odd | 6 | 6 | 6 | `B2 L2 B2 L2 D2 B2` |
| R-V + | F-V | R-H | odd | 6 | 6 | 6 | `F2 R2 B2 R2 F2 D2` |
| H-H - | F-V | R-H | even | 7 | 7 | 7 | `L2 B2 U2 R2 D2 R2 U2` |
| F-D - | F-H | R-H | odd | 7 | 7 | 7 | `L2 B2 D2 L2 D2 L2 B2` |
| F-D + | F-V | R-H | odd | 7 | 7 | 6 | `R L' B2 D2 R L'` |
| H-H - | F-V | R-D | odd | 7 | 7 | 6 | `B2 R L D2 R' L` |
| F-D - | F-H | R-D | odd | 7 | 7 | 7 | `R2 D2 L2 F2 L2 F2 D2` |
| D-D + | F-H | R-V | even | 7 | 7 | 6 | `R' L' F2 R' L F2` |
| H-H + | F-V | R-H | odd | 7 | 7 | 7 | `R2 U2 B2 R2 D2 L2 F2` |
| R-D - | F-V | R-H | odd | 7 | 7 | 7 | `L2 D2 B2 L2 D2 B2 L2` |
| F-D + | F-H | R-H | odd | 7 | 7 | 5 | ` R L' D2 R' L` |
| H-H - | F-D | R-D | odd | 7 | 7 | 6 | `R L' D2 R' L' B2` |
| D-D - | F-H | R-D | odd | 7 | 7 | 7 | `R' L' F2 R L F2 D2` |
| R-V + | F-D | R-V | even | 7 | 7 | 5 | ` R' L' B2 R L` |
| R-V + | F-H | R-D | odd | 7 | 7 | 6 | `F' B D2 R2 F B'` |
| F-D + | F-D | R-D | odd | 7 | 7 | 5 | ` F' B R2 F B` |
| F-V - | F-H | R-H | odd | 7 | 7 | 7 | `L2 B2 D2 B2 D2 L2 B2` |
| R-V + | F-H | R-H | odd | 7 | 7 | 6 | `L2 F B' L2 F' B` |
| F-D - | F-D | R-H | odd | 7 | 7 | 7 | `R2 F2 U2 F2 R2 D2 L2` |
| H-H + | F-H | R-D | odd | 7 | 7 | 6 | `L B2 U2 D2 F2 R'` |
| R-V - | F-D | R-V | odd | 7 | 7 | 6 | `R' L' D2 B2 R' L'` |
| D-D - | F-H | R-V | odd | 7 | 7 | 7 | `R2 F2 R2 F2 D2 R2 D2` |
| R-V + | F-D | R-V | odd | 7 | 7 | 5 | ` R' L' B2 R L'` |
| H-H + | F-V | R-H | even | 7 | 7 | 6 | `B2 R L' D2 R' L` |
| F-V + | F-D | R-V | odd | 7 | 7 | 7 | `L2 F2 R2 U2 F2 L2 D2` |
| H-H + | F-V | R-D | even | 7 | 7 | 7 | `R2 F2 L2 U2 B2 L2 F2` |
| R-V + | F-D | R-D | even | 7 | 7 | 7 | `R2 F2 R2 F2 D2 R2 B2` |
| F-D - | F-V | R-H | odd | 7 | 7 | 7 | `L2 B2 L2 B2 D2 B2 D2` |
| D-D - | F-H | R-V | even | 7 | 7 | 7 | `R2 F2 R2 F2 R2 D2 R2` |
| F-V + | F-D | R-V | even | 7 | 7 | 7 | `L2 F2 R2 F2 L2 D2 B2` |
| H-H + | F-V | R-V | even | 7 | 7 | 7 | `F2 R2 F2 L2 B2 L2 D2` |
| F-D - | F-H | R-V | odd | 7 | 7 | 7 | `F2 U2 R2 F2 D2 L2 B2` |
| H-H + | F-H | R-V | odd | 7 | 7 | 7 | `F2 U2 L2 B2 U2 F2 R2` |
| R-D + | F-H | R-H | odd | 7 | 7 | 5 | ` F' B D2 F B'` |
| D-D + | F-D | R-H | odd | 7 | 7 | 7 | `L2 F B' L2 U2 F' B'` |
| F-V + | F-V | R-D | even | 7 | 7 | 5 | ` F' B' R2 F B` |
| H-H - | F-H | R-V | even | 7 | 7 | 7 | `F2 U2 B2 U2 R2 F2 D2` |
| R-D - | F-H | R-H | odd | 7 | 7 | 7 | `B2 L2 D2 B2 D2 B2 L2` |
| H-H - | F-D | R-V | odd | 7 | 7 | 6 | `L2 F B U2 F' B` |
| R-D + | F-H | R-V | odd | 7 | 7 | 6 | `F' B R2 D2 F B'` |
| R-D - | F-D | R-H | odd | 7 | 7 | 7 | `B2 D2 B2 L2 B2 L2 D2` |
| D-D - | F-V | R-H | even | 7 | 7 | 6 | `F B L2 F' B L2` |
| F-V + | F-H | R-H | odd | 7 | 7 | 6 | `B2 R' L B2 R L'` |
| R-V - | F-H | R-H | odd | 7 | 7 | 7 | `B2 L2 D2 L2 D2 B2 L2` |
| H-H + | F-D | R-H | odd | 7 | 7 | 6 | `F L2 U2 D2 R2 B'` |
| R-D - | F-H | R-D | odd | 7 | 7 | 7 | `F2 R2 U2 R2 B2 U2 F2` |
| R-D + | F-D | R-D | odd | 7 | 7 | 5 | ` R' L B2 R L` |
| F-V + | F-D | R-H | odd | 7 | 7 | 6 | `R' L D2 B2 R' L` |
| R-V + | F-V | R-D | odd | 7 | 7 | 7 | `F2 R2 F2 D2 L2 B2 D2` |
| H-H + | F-D | R-V | even | 7 | 7 | 7 | `F2 R2 F2 D2 L2 B2 L2` |
| D-D + | F-V | R-H | odd | 7 | 7 | 7 | `F B U2 L2 B F' L2` |
| F-V - | F-V | R-D | odd | 7 | 7 | 6 | `F' B' D2 R2 F B` |
| F-V + | F-V | R-D | odd | 7 | 7 | 5 | ` F' B' R2 F B'` |
| H-H + | F-H | R-V | even | 7 | 7 | 6 | `R2 F B' D2 F' B` |
| R-D - | F-H | R-V | odd | 7 | 7 | 7 | `F2 L2 F2 L2 U2 L2 U2` |
| F-V + | F-D | R-D | even | 7 | 7 | 7 | `B2 R2 B2 R2 D2 B2 R2` |
| R-V + | F-V | R-D | even | 7 | 7 | 7 | `B2 R2 F2 R2 F2 D2 R2` |
| D-D + | F-V | R-H | even | 7 | 7 | 7 | `F2 R2 B2 R2 F2 D2 B2` |
| R-D - | F-V | R-D | odd | 8 | 8 | 7 | `R' L' F2 R L U2 F2` |
| F-D + | F-H | R-D | even | 8 | 8 | 8 | `L2 F2 U2 R2 U2 R2 F2 L2` |
| R-D - | F-V | R-H | even | 8 | 8 | 6 | `B2 R L D2 R' L'` |
| F-D + | F-H | R-H | even | 8 | 8 | 6 | `F L2 U2 D2 R2 B` |
| H-H - | F-D | R-D | even | 8 | 8 | 8 | `F2 U2 B2 R2 F2 L2 D2 L2` |
| D-D - | F-H | R-D | even | 8 | 8 | 6 | `F2 R L' F2 R L` |
| R-D + | F-V | R-D | even | 8 | 8 | 6 | `R' L' B2 R L D2` |
| R-V - | F-D | R-H | odd | 8 | 8 | 8 | `B2 D2 B2 R L D2 R' L'` |
| R-D + | F-V | R-H | even | 8 | 8 | 8 | `L2 D2 F2 R2 U2 B2 R2 F2` |
| H-H + | F-D | R-H | even | 8 | 8 | 5 | ` R' L B2 R L'` |
| H-H - | F-V | R-V | odd | 8 | 8 | 7 | `F2 R' L' U2 F2 R' L` |
| F-V + | F-H | R-H | even | 8 | 8 | 7 | `F2 R' L F2 D2 R L'` |
| R-V - | F-D | R-D | even | 8 | 8 | 8 | `R' L' F2 R L F2 D2 B2` |
| R-V + | F-H | R-H | even | 8 | 8 | 7 | `L2 F B' L2 U2 F' B` |
| F-D - | F-D | R-H | even | 8 | 8 | 5 | ` F' B' D2 F B'` |
| H-H + | F-H | R-D | even | 8 | 8 | 5 | ` F' B R2 F B'` |
| D-D + | F-H | R-D | even | 8 | 8 | 8 | `R2 F2 R2 F2 R2 U2 L2 U2` |
| D-D + | F-D | R-H | even | 8 | 8 | 6 | `L2 F B' L2 F' B'` |
| F-V - | F-V | R-H | odd | 8 | 8 | 7 | `F2 R2 F B' R2 F B` |
| H-H - | F-H | R-H | even | 8 | 8 | 8 | `R2 F2 U2 B2 L2 U2 R2 F2` |
| R-D + | F-H | R-H | even | 8 | 8 | 6 | `R B2 U2 D2 F2 L` |
| F-V + | F-H | R-V | even | 8 | 8 | 8 | `L2 F2 R' L F2 D2 R L` |
| D-D - | F-D | R-V | even | 8 | 8 | 8 | `L2 B2 U2 R L U2 R' L` |
| R-D + | F-V | R-H | odd | 8 | 8 | 7 | `F2 R L U2 R' L' F2` |
| R-D + | F-V | R-V | even | 8 | 8 | 8 | `R2 F2 R2 F2 D2 R2 B2 D2` |
| R-V + | F-D | R-H | odd | 8 | 8 | 8 | `L2 F2 R2 B2 U2 R2 F2 L2` |
| F-D + | F-V | R-D | even | 8 | 8 | 8 | `L2 F2 R2 F2 L2 D2 B2 D2` |
| D-D - | F-D | R-V | odd | 8 | 8 | 7 | `R L D2 R' L D2 B2` |
| R-D + | F-V | R-V | odd | 8 | 8 | 8 | `R2 F2 R2 F2 R2 B2 D2 R2` |
| F-D + | F-V | R-V | odd | 8 | 8 | 8 | `L2 F2 R2 F2 L2 B2 D2 B2` |
| F-V - | F-H | R-D | odd | 8 | 8 | 8 | `F2 U2 R2 F2 D2 L2 B2 D2` |
| F-D + | F-H | R-V | even | 8 | 8 | 8 | `B2 D2 R2 B2 D2 R2 B2 R2` |
| F-D + | F-D | R-V | even | 8 | 8 | 6 | `F' B' R2 F B D2` |
| F-V - | F-D | R-D | even | 8 | 8 | 8 | `R2 F' B R2 D2 F B R2` |
| F-D - | F-D | R-V | odd | 8 | 8 | 7 | `F' B' D2 R2 B F D2` |
| R-D + | F-D | R-H | even | 8 | 8 | 8 | `F2 R2 U2 B2 U2 B2 R2 F2` |
| F-D - | F-H | R-V | even | 8 | 8 | 6 | `L2 F B U2 F' B'` |
| D-D - | F-D | R-H | even | 8 | 8 | 8 | `F2 R2 B2 R2 F2 D2 B2 D2` |
| R-V - | F-H | R-V | odd | 8 | 8 | 7 | `L2 F2 R L' F2 R L` |
| R-D - | F-H | R-D | even | 8 | 8 | 5 | ` R L D2 R' L` |
| R-V + | F-V | R-H | even | 8 | 8 | 8 | `F2 R2 F B' R2 D2 F B` |
| D-D + | F-V | R-D | even | 8 | 8 | 8 | `F2 R2 F2 D2 L2 B2 D2 B2` |
| F-D + | F-H | R-V | odd | 8 | 8 | 7 | `R2 F B D2 F' B' R2` |
| R-D + | F-D | R-V | even | 8 | 8 | 8 | `B2 R2 F2 R2 F2 D2 R2 D2` |
| F-D + | F-V | R-V | even | 8 | 8 | 8 | `B2 L2 F2 R2 U2 F2 L2 D2` |
| F-V + | F-H | R-D | odd | 8 | 8 | 8 | `B2 R2 F2 L2 U2 B2 L2 F2` |
| D-D + | F-V | R-D | odd | 8 | 8 | 7 | `F' B' D2 F B' D2 L2` |
| H-H + | F-D | R-D | odd | 9 | 9 | 8 | `R D2 F2 B2 R' L F2 R'` |
| R-V - | F-D | R-H | even | 9 | 9 | 7 | `B2 D2 R L D2 R' L'` |
| H-H - | F-V | R-V | even | 9 | 9 | 9 | `F2 U2 B2 R2 F2 L2 D2 L2 D2` |
| R-V - | F-D | R-D | odd | 9 | 9 | 7 | `F2 R L' F2 R L B2` |
| D-D - | F-H | R-H | even | 9 | 9 | 9 | `R2 D2 F2 R2 D2 F2 R2 D2 F2` |
| R-V + | F-D | R-H | even | 9 | 9 | 9 | `L2 D2 F2 R2 D2 F2 L2 B2 U2` |
| H-H + | F-V | R-D | odd | 9 | 9 | 8 | `L' F2 R L' F2 B2 D2 L` |
| R-D - | F-V | R-V | even | 9 | 8 | 7 | `F2 R' L' U2 F2 R' L'` |
| F-D - | F-V | R-V | even | 9 | 8 | 7 | `L2 F B U2 L2 F' B'` |
| F-V - | F-V | R-H | even | 9 | 9 | 6 | `F' B' D2 F B' D2` |
| H-H - | F-H | R-H | odd | 9 | 9 | 5 | ` F' B' D2 F B` |
| R-V + | F-D | R-D | odd | 9 | 9 | 9 | `L2 F2 R2 U2 B2 U2 F2 L2 B2` |
| F-V - | F-D | R-D | odd | 9 | 9 | 7 | `L2 F' B R2 F B L2` |
| H-H + | F-V | R-V | odd | 9 | 9 | 9 | `L2 F2 R2 F2 D2 L2 B2 D2 L2` |
| R-D - | F-V | R-V | odd | 9 | 9 | 8 | `F2 R L' F2 L R B2 D2` |
| D-D + | F-H | R-H | even | 9 | 9 | 9 | `F2 D2 R2 F2 D2 R2 F2 D2 R2` |
| R-V - | F-H | R-V | even | 9 | 9 | 6 | `R L D2 R' L D2` |
| F-V + | F-D | R-D | odd | 9 | 9 | 9 | `B2 L2 F2 R2 F2 L2 D2 B2 D2` |
| F-V + | F-H | R-D | even | 9 | 9 | 9 | `B2 D2 L2 F2 D2 L2 B2 R2 U2` |
| H-H + | F-D | R-V | odd | 9 | 9 | 8 | `F L2 F B' R2 L2 D2 F'` |
| F-V - | F-H | R-D | even | 9 | 9 | 7 | `L2 D2 F B U2 F' B'` |
| F-D - | F-V | R-V | odd | 9 | 9 | 8 | `L2 U2 F B U2 F B' U2` |
| D-D - | F-H | R-H | odd | 10 | 10 | 8 | `B2 D2 R L D2 R' L' B2` |
| D-D + | F-H | R-H | odd | 10 | 10 | 8 | `L2 D2 F' B' D2 F B L2` |

---

## Appendix D: odds by true pairs, all 48 subsets

One table per target. Each cell: the share finishing in that many moves or less, for DRs of that subset with that many true pairs (corner + U/D-layer edge, both touching stickers matching, 16 places to look). An empty cell means the subset has no state with that many pairs.

**Share finishing in 10 or less**

| Subset | 0 pairs | 1 | 2 | 3 | 4 | 5 | 6 or more |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0c0 0e | 56% |  | 62% |  | 64% |  | 66% |
| 0c0 2e | 3.5% | 8.9% | 8.8% | 12% | 13% | 16% | 19% |
| 0c0 4e | 2.1% | 2.3% | 4.6% | 5.7% | 8.2% | 8.0% | 15% |
| 0c0 6e | 0.34% | 0.83% | 1.8% | 1.4% | 4.8% |  |  |
| 0c0 8e | 3.0% |  |  |  |  |  |  |
| 4a1 0e | 0.35% | 0.49% | 1.1% | 0.63% | 1.3% | 0.97% | 6.1% |
| 4a1 2e | 0.65% | 0.91% | 1.9% | 3.2% | 5.1% | 7.2% | 11% |
| 4a1 4e | 2.5% | 3.0% | 5.8% | 7.3% | 14% | 15% | 29% |
| 4a2 0e | 0.01% | 0 | 0.03% | 0 | 0.38% | 0 | 3.2% |
| 4a2 2e | 0.03% | 0.08% | 0.21% | 0.36% | 0.82% | 0.59% | 0.82% |
| 4a2 4e | 0.75% | 0.96% | 2.0% | 2.1% | 4.0% | 3.4% | 6.4% |
| 4b2 0e | 0.66% | 0.68% | 1.4% | 1.9% | 3.2% | 2.5% | 4.2% |
| 4b2 2e | 1.0% | 1.2% | 2.1% | 3.4% | 5.7% | 8.4% | 16% |
| 4b2 4e | 0.41% | 0.81% | 1.4% | 2.3% | 3.8% | 5.9% | 9.8% |
| 0c3 0e | 0 | 0 | 0 | 0 | 0 | 0 | 0.19% |
| 0c3 2e | 0 | 0 | 0 | 0.04% | 0.15% | 0.10% | 0.31% |
| 0c3 4e | 0 | 0 | 0.02% | 0 | 0.07% | 0 | 0 |
| 0c3 6e | 0 | 0.07% | 0.15% | 0.21% | 0 |  |  |
| 0c3 8e | 0.04% |  |  |  |  |  |  |
| 2c3 0e | 0 | 0 | 0 | 0.08% | 0.09% | 0.31% | 1.2% |
| 2c3 2e | 0.83% | 1.0% | 1.5% | 2.5% | 3.7% | 6.0% | 10% |
| 2c3 4e | 0.30% | 0.52% | 0.94% | 1.6% | 2.7% | 4.3% | 7.9% |
| 2c3 6e | 0.19% | 0.32% | 0.51% | 0.86% | 1.2% | 1.7% | 1.3% |
| 2c3 8e | <0.01% | 0.09% | 0.29% | 0.58% | 0 |  |  |
| 4c3 0e | 0.10% | 0.26% | 0.41% | 0.74% | 1.5% | 2.1% | 4.0% |
| 4c3 2e | 0.07% | 0.13% | 0.28% | 0.38% | 0.89% | 1.1% | 2.6% |
| 4c3 4e | 0.08% | 0.13% | 0.30% | 0.42% | 0.78% | 1.0% | 2.4% |
| 0c4 0e | 0 | 0 | 0 | 0 | 0 | 0 | 1.4% |
| 0c4 2e | 0 | 0 | 0.04% | 0.11% | 0.15% | 0.16% | 0.55% |
| 0c4 4e | 0 | 0.02% | 0.06% | 0.14% | 0.27% | 0.33% | 0 |
| 0c4 6e | 0.01% | 0 | 0.09% | 0 | 0 |  |  |
| 0c4 8e | 0 |  |  |  |  |  |  |
| 2c4 0e | 0.04% | 0.11% | 0.26% | 0.50% | 1.2% | 1.7% | 4.3% |
| 2c4 2e | 0.03% | 0.05% | 0.11% | 0.25% | 0.44% | 0.90% | 2.4% |
| 2c4 4e | 0.03% | 0.07% | 0.14% | 0.27% | 0.52% | 1.0% | 2.1% |
| 2c4 6e | 0.02% | 0.07% | 0.14% | 0.29% | 0.53% | 0.99% | 2.3% |
| 2c4 8e | 0.02% | 0.08% | 0.04% | 0.06% | 0 |  |  |
| 4c4 0e | 0 | 0 | 0.02% | 0 | 0.05% | 0 | 0 |
| 4c4 2e | 0 | <0.01% | 0.01% | 0.01% | 0.05% | 0.03% | 0.19% |
| 4c4 4e | <0.01% | <0.01% | 0.01% | 0.01% | 0.07% | 0.05% | 0.12% |
| 2c5 0e | 0 | 0 | 0 | 0 | 0 | 0 | 0.12% |
| 2c5 2e | 0 | 0 | <0.01% | <0.01% | 0.02% | 0.11% | 0.38% |
| 2c5 4e | 0 | <0.01% | 0.01% | 0.03% | 0.06% | 0.22% | 0.69% |
| 2c5 6e | 0 | 0.01% | <0.01% | 0.02% | 0.09% | 0.17% | 0 |
| 2c5 8e | 0 | 0 | 0.06% | 0 | 0 |  |  |
| 4b5 0e | 0 | 0 | 0.02% | 0 | 0.11% | 0.15% | 0 |
| 4b5 2e | <0.01% | <0.01% | 0.01% | 0.02% | 0.07% | 0.11% | 0.20% |
| 4b5 4e | 0 | <0.01% | <0.01% | 0.01% | 0.03% | 0.06% | 0.34% |

**Share finishing in 11 or less**

| Subset | 0 pairs | 1 | 2 | 3 | 4 | 5 | 6 or more |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0c0 0e | 86% |  | 90% |  | 89% |  | 91% |
| 0c0 2e | 21% | 34% | 34% | 38% | 41% | 44% | 50% |
| 0c0 4e | 11% | 13% | 17% | 22% | 25% | 35% | 34% |
| 0c0 6e | 3.1% | 5.7% | 8.6% | 12% | 16% |  |  |
| 0c0 8e | 13% |  |  |  |  |  |  |
| 4a1 0e | 3.1% | 3.4% | 5.7% | 5.2% | 6.9% | 7.9% | 20% |
| 4a1 2e | 5.2% | 6.8% | 11% | 15% | 21% | 26% | 33% |
| 4a1 4e | 11% | 13% | 19% | 24% | 36% | 43% | 61% |
| 4a2 0e | 0.19% | 0.05% | 0.74% | 0.28% | 3.2% | 3.3% | 13% |
| 4a2 2e | 0.55% | 0.94% | 1.6% | 2.4% | 3.9% | 4.4% | 4.9% |
| 4a2 4e | 4.8% | 5.6% | 8.0% | 8.8% | 12% | 12% | 17% |
| 4b2 0e | 4.1% | 4.8% | 7.1% | 8.8% | 12% | 12% | 18% |
| 4b2 2e | 5.8% | 6.9% | 10% | 14% | 20% | 27% | 40% |
| 4b2 4e | 3.4% | 5.3% | 7.8% | 11% | 16% | 22% | 30% |
| 0c3 0e | 0 | 0 | 0 | 0.51% | 1.0% | 0 | 1.7% |
| 0c3 2e | 0.05% | 0.21% | 0.35% | 0.38% | 0.89% | 0.92% | 1.7% |
| 0c3 4e | 0 | 0.14% | 0.18% | 0.28% | 0.21% | 0.44% | 0.29% |
| 0c3 6e | 0.23% | 0.57% | 0.93% | 1.5% | 0.54% |  |  |
| 0c3 8e | 0.75% |  |  |  |  |  |  |
| 2c3 0e | 0.20% | 0.26% | 0.56% | 1.0% | 2.2% | 3.7% | 7.0% |
| 2c3 2e | 6.1% | 7.0% | 9.0% | 12% | 16% | 22% | 30% |
| 2c3 4e | 2.6% | 3.8% | 5.6% | 8.2% | 12% | 16% | 24% |
| 2c3 6e | 1.7% | 2.4% | 3.5% | 5.1% | 6.7% | 8.9% | 7.8% |
| 2c3 8e | 0.47% | 1.0% | 2.5% | 3.9% | 4.5% |  |  |
| 4c3 0e | 1.4% | 2.2% | 3.0% | 4.3% | 7.2% | 9.7% | 17% |
| 4c3 2e | 0.88% | 1.2% | 2.0% | 2.8% | 4.4% | 5.7% | 9.7% |
| 4c3 4e | 0.87% | 1.3% | 2.1% | 2.7% | 4.1% | 5.7% | 10% |
| 0c4 0e | 0 | 0 | 0.15% | 0 | 2.6% | 0 | 10% |
| 0c4 2e | 0 | 0.50% | 0.70% | 1.0% | 1.2% | 2.1% | 4.1% |
| 0c4 4e | 0.21% | 0.46% | 0.81% | 1.3% | 1.7% | 2.7% | 3.0% |
| 0c4 6e | 0.11% | 0.35% | 0.66% | 0.70% | 0 |  |  |
| 0c4 8e | 0.11% |  |  |  |  |  |  |
| 2c4 0e | 0.96% | 1.6% | 2.9% | 3.9% | 6.1% | 8.1% | 13% |
| 2c4 2e | 0.41% | 0.73% | 1.2% | 2.0% | 3.3% | 5.3% | 10% |
| 2c4 4e | 0.48% | 0.74% | 1.2% | 2.0% | 3.2% | 5.1% | 9.0% |
| 2c4 6e | 0.38% | 0.74% | 1.3% | 2.2% | 3.5% | 5.7% | 9.6% |
| 2c4 8e | 0.36% | 0.66% | 0.77% | 0.56% | 0.83% |  |  |
| 4c4 0e | 0 | 0.05% | 0.18% | 0.19% | 0.22% | 0.27% | 0 |
| 4c4 2e | 0.04% | 0.06% | 0.14% | 0.18% | 0.39% | 0.52% | 1.2% |
| 4c4 4e | 0.07% | 0.10% | 0.17% | 0.24% | 0.47% | 0.60% | 0.93% |
| 2c5 0e | 0 | 0 | 0 | 0.12% | 0.11% | 0 | 1.4% |
| 2c5 2e | 0.03% | 0.04% | 0.10% | 0.22% | 0.48% | 0.87% | 2.5% |
| 2c5 4e | 0.04% | 0.08% | 0.17% | 0.39% | 0.77% | 1.7% | 3.6% |
| 2c5 6e | 0.07% | 0.11% | 0.15% | 0.34% | 0.62% | 1.2% | 1.1% |
| 2c5 8e | 0.02% | 0.13% | 0.35% | 0.15% | 0 |  |  |
| 4b5 0e | 0.05% | 0.06% | 0.23% | 0.16% | 0.67% | 1.3% | 0.06% |
| 4b5 2e | 0.04% | 0.06% | 0.18% | 0.29% | 0.54% | 0.94% | 1.6% |
| 4b5 4e | 0.01% | 0.05% | 0.09% | 0.18% | 0.44% | 0.83% | 2.4% |

**Share finishing in 12 or less**

| Subset | 0 pairs | 1 | 2 | 3 | 4 | 5 | 6 or more |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0c0 0e | 99.2% |  | 99.5% |  | 99% |  | 99.5% |
| 0c0 2e | 67% | 77% | 78% | 81% | 82% | 85% | 87% |
| 0c0 4e | 40% | 48% | 52% | 61% | 64% | 76% | 72% |
| 0c0 6e | 19% | 27% | 35% | 44% | 52% |  |  |
| 0c0 8e | 39% |  |  |  |  |  |  |
| 4a1 0e | 17% | 20% | 24% | 28% | 30% | 42% | 47% |
| 4a1 2e | 27% | 33% | 42% | 52% | 60% | 67% | 73% |
| 4a1 4e | 38% | 44% | 52% | 61% | 72% | 81% | 89% |
| 4a2 0e | 2.4% | 2.3% | 5.6% | 5.6% | 16% | 29% | 34% |
| 4a2 2e | 4.9% | 7.0% | 9.5% | 13% | 17% | 19% | 20% |
| 4a2 4e | 21% | 23% | 26% | 30% | 33% | 35% | 42% |
| 4b2 0e | 20% | 24% | 29% | 32% | 38% | 44% | 48% |
| 4b2 2e | 27% | 30% | 38% | 47% | 57% | 66% | 77% |
| 4b2 4e | 20% | 26% | 34% | 42% | 51% | 60% | 67% |
| 0c3 0e | 0.91% | 3.5% | 3.3% | 4.4% | 6.9% | 1.8% | 9.8% |
| 0c3 2e | 1.3% | 2.3% | 2.8% | 3.9% | 3.9% | 4.8% | 7.4% |
| 0c3 4e | 0.62% | 1.3% | 1.5% | 1.8% | 1.9% | 2.4% | 1.5% |
| 0c3 6e | 2.4% | 3.8% | 4.7% | 6.9% | 4.8% |  |  |
| 0c3 8e | 5.6% |  |  |  |  |  |  |
| 2c3 0e | 3.2% | 4.4% | 7.6% | 11% | 16% | 22% | 30% |
| 2c3 2e | 30% | 33% | 37% | 44% | 52% | 60% | 68% |
| 2c3 4e | 16% | 20% | 26% | 32% | 41% | 49% | 58% |
| 2c3 6e | 11% | 15% | 19% | 24% | 29% | 36% | 34% |
| 2c3 8e | 5.7% | 8.9% | 14% | 23% | 19% |  |  |
| 4c3 0e | 11% | 13% | 15% | 20% | 27% | 33% | 50% |
| 4c3 2e | 6.9% | 8.5% | 11% | 15% | 19% | 23% | 31% |
| 4c3 4e | 6.7% | 8.6% | 11% | 14% | 18% | 24% | 33% |
| 0c4 0e | 0 | 0.81% | 1.8% | 10% | 17% | 22% | 38% |
| 0c4 2e | 3.0% | 4.8% | 6.5% | 8.5% | 8.6% | 14% | 21% |
| 0c4 4e | 3.1% | 4.7% | 6.7% | 8.9% | 11% | 15% | 18% |
| 0c4 6e | 1.9% | 3.8% | 5.1% | 6.0% | 3.4% |  |  |
| 0c4 8e | 1.9% |  |  |  |  |  |  |
| 2c4 0e | 10% | 12% | 16% | 19% | 24% | 28% | 34% |
| 2c4 2e | 4.3% | 6.3% | 8.5% | 12% | 17% | 23% | 33% |
| 2c4 4e | 4.4% | 5.8% | 8.1% | 11% | 16% | 22% | 30% |
| 2c4 6e | 3.9% | 5.8% | 8.4% | 12% | 17% | 24% | 30% |
| 2c4 8e | 3.4% | 4.7% | 5.7% | 5.1% | 6.8% |  |  |
| 4c4 0e | 0.24% | 0.75% | 1.2% | 1.9% | 2.0% | 3.1% | 0.16% |
| 4c4 2e | 0.61% | 0.83% | 1.3% | 1.8% | 2.7% | 4.4% | 6.8% |
| 4c4 4e | 0.86% | 1.1% | 1.5% | 2.2% | 3.1% | 4.4% | 6.1% |
| 2c5 0e | 0.50% | 0.41% | 0.70% | 0.97% | 2.4% | 1.3% | 7.3% |
| 2c5 2e | 0.52% | 0.84% | 1.5% | 2.3% | 3.9% | 6.2% | 11% |
| 2c5 4e | 0.63% | 1.1% | 1.9% | 3.3% | 5.5% | 9.4% | 15% |
| 2c5 6e | 0.82% | 1.2% | 1.6% | 2.8% | 4.6% | 6.7% | 4.6% |
| 2c5 8e | 0.59% | 1.7% | 2.5% | 2.2% | 0.84% |  |  |
| 4b5 0e | 0.97% | 1.1% | 1.8% | 2.2% | 3.6% | 8.2% | 5.3% |
| 4b5 2e | 0.63% | 0.93% | 1.7% | 2.7% | 4.1% | 6.2% | 8.9% |
| 4b5 4e | 0.41% | 0.77% | 1.3% | 2.2% | 4.1% | 6.4% | 12% |

**Share finishing in 13 or less**

| Subset | 0 pairs | 1 | 2 | 3 | 4 | 5 | 6 or more |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0c0 0e | 100% |  | 100% |  | 100% |  | 100% |
| 0c0 2e | 97% | 99.1% | 99% | 99.2% | 99.2% | 99.6% | 99.3% |
| 0c0 4e | 86% | 92% | 92% | 96% | 96% | 99.3% | 97% |
| 0c0 6e | 67% | 76% | 81% | 90% | 87% |  |  |
| 0c0 8e | 78% |  |  |  |  |  |  |
| 4a1 0e | 58% | 69% | 68% | 78% | 76% | 92% | 83% |
| 4a1 2e | 78% | 83% | 89% | 93% | 96% | 98% | 98% |
| 4a1 4e | 83% | 88% | 92% | 95% | 97% | 99% | 99.2% |
| 4a2 0e | 17% | 20% | 26% | 36% | 46% | 62% | 63% |
| 4a2 2e | 27% | 34% | 40% | 46% | 51% | 53% | 55% |
| 4a2 4e | 57% | 60% | 64% | 68% | 70% | 73% | 77% |
| 4b2 0e | 64% | 70% | 75% | 78% | 82% | 88% | 88% |
| 4b2 2e | 75% | 80% | 85% | 91% | 95% | 97% | 99% |
| 4b2 4e | 69% | 77% | 83% | 89% | 93% | 95% | 97% |
| 0c3 0e | 11% | 27% | 21% | 21% | 30% | 12% | 35% |
| 0c3 2e | 12% | 14% | 15% | 18% | 18% | 22% | 27% |
| 0c3 4e | 5.8% | 8.2% | 9.1% | 10% | 11% | 13% | 11% |
| 0c3 6e | 15% | 18% | 20% | 25% | 21% |  |  |
| 0c3 8e | 25% |  |  |  |  |  |  |
| 2c3 0e | 26% | 35% | 44% | 54% | 60% | 68% | 75% |
| 2c3 2e | 80% | 83% | 86% | 90% | 93% | 96% | 97% |
| 2c3 4e | 59% | 66% | 73% | 80% | 85% | 90% | 93% |
| 2c3 6e | 50% | 58% | 65% | 71% | 76% | 82% | 82% |
| 2c3 8e | 36% | 45% | 53% | 65% | 61% |  |  |
| 4c3 0e | 47% | 49% | 52% | 58% | 67% | 74% | 86% |
| 4c3 2e | 35% | 39% | 45% | 52% | 59% | 65% | 72% |
| 4c3 4e | 33% | 39% | 45% | 51% | 58% | 66% | 73% |
| 0c4 0e | 16% | 12% | 36% | 60% | 66% | 81% | 81% |
| 0c4 2e | 27% | 33% | 38% | 44% | 48% | 58% | 63% |
| 0c4 4e | 25% | 31% | 37% | 43% | 51% | 57% | 64% |
| 0c4 6e | 18% | 26% | 30% | 34% | 27% |  |  |
| 0c4 8e | 16% |  |  |  |  |  |  |
| 2c4 0e | 46% | 50% | 54% | 59% | 63% | 68% | 72% |
| 2c4 2e | 27% | 34% | 40% | 47% | 56% | 65% | 74% |
| 2c4 4e | 26% | 31% | 37% | 44% | 52% | 62% | 70% |
| 2c4 6e | 24% | 31% | 38% | 47% | 55% | 65% | 67% |
| 2c4 8e | 20% | 24% | 29% | 28% | 30% |  |  |
| 4c4 0e | 3.7% | 6.5% | 8.6% | 12% | 13% | 18% | 10% |
| 4c4 2e | 5.9% | 7.4% | 9.8% | 13% | 17% | 23% | 29% |
| 4c4 4e | 7.4% | 8.7% | 11% | 14% | 18% | 23% | 28% |
| 2c5 0e | 6.7% | 5.2% | 8.6% | 9.4% | 15% | 16% | 25% |
| 2c5 2e | 6.9% | 9.0% | 12% | 17% | 22% | 30% | 38% |
| 2c5 4e | 7.0% | 10% | 14% | 20% | 26% | 36% | 44% |
| 2c5 6e | 7.4% | 9.7% | 13% | 17% | 23% | 29% | 23% |
| 2c5 8e | 7.2% | 12% | 14% | 14% | 8.1% |  |  |
| 4b5 0e | 9.1% | 9.8% | 12% | 15% | 21% | 29% | 37% |
| 4b5 2e | 7.1% | 9.2% | 13% | 18% | 24% | 30% | 37% |
| 4b5 4e | 5.7% | 8.3% | 12% | 17% | 24% | 32% | 43% |

Share of all DRs with that many pairs: 0: 13.8%, 1: 27.0%, 2: 26.8%, 3: 17.8%, 4: 9.1%, 5: 3.7%, 6 or more: 1.8%.

---

## Appendix E: the 46 corner cases

A corner case is what the corners look like up to rotation, mirror and turning a layer. The columns:

- **Bad corners**: where the bad ones sit in the shortest setup (fewest bad corners).
- **L**: the range of optimal corner solution lengths the case can have.
- **A typical DR**: a state of that case whose optimal finish is the median for the case, with that optimal in brackets. This is what the case usually looks like.
- **Shortest setup**: the shortest scramble that produces those corners, so you can put the layout on a cube quickly. As a DR it is one of the rare best ones of its case (it finishes in as many moves as the scramble is long), so don't judge the case by it.
- **A qt takes it straight to**: the corner subsets one U or D quarter turn can reach with one qt less.
- **Share** is of the corner subset, all edge counts together. **In 10 … In 13** are the shares whose optimal finish is that long or shorter.

In the both-sides tables the two columns are the case on normal and on inverse, in either order.

**0c0**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 0c0-1 | none bad | 0–5 | `R2 U' F2 R2 D L2 B2 R2 U L2 U R2` (12) | `` | nothing (set up first) |  | 100.0% | 12.28 | 6.1% | 21% | 54% | 90% |

**4a1**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 4a1-1 | 4-0 | 1–4 | `U2 F2 R2 B2 U B2 U2 B2 U2 R2 F2 U2` (12) | `D` | 0c0 |  | 16.7% | 12.30 | 5.6% | 19% | 52% | 91% |
| 4a1-2 | 2-2, pairs on opposite sides | 2–5 | `B2 U' F2 D F2 L2 U2 B2 D2 B2 U' L2` (12) | `D B2` | nothing (set up first) |  | 33.3% | 12.36 | 4.8% | 17% | 50% | 91% |
| 4a1-3 | 2-2, pairs stacked | 3–6 | `R2 U' B2 L2 D2 B2 D2 B2 D B2 U' F2 U2` (13) | `D B2 D2` | nothing (set up first) |  | 33.3% | 12.48 | 3.8% | 14% | 45% | 88% |
| 4a1-4 | 2-2, diagonal over diagonal | 4–7 | `D2 B2 U L2 D' B2 R2 B2 D' L2 D' U' F2` (13) | `D' R2 D2 F2` | nothing (set up first) |  | 16.7% | 12.54 | 3.5% | 14% | 42% | 86% |

4a1, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---:|---:|---:|---:|---:|---:|
| 4a1-1 | 4a1-3 | 11.1% | 12.29 | 5.6% | 20% | 53% | 92% |
| 4a1-1 | 4a1-2 | 11.1% | 12.29 | 5.6% | 19% | 53% | 91% |
| 4a1-1 | 4a1-4 | 5.6% | 12.31 | 5.6% | 19% | 52% | 90% |
| 4a1-1 | 4a1-1 | 2.8% | 12.32 | 5.7% | 19% | 52% | 89% |
| 4a1-2 | 4a1-2 | 11.1% | 12.34 | 4.9% | 18% | 51% | 91% |
| 4a1-2 | 4a1-3 | 22.2% | 12.38 | 4.3% | 16% | 49% | 91% |
| 4a1-2 | 4a1-4 | 11.1% | 12.42 | 4.3% | 16% | 47% | 90% |
| 4a1-3 | 4a1-3 | 11.1% | 12.59 | 3.0% | 12% | 40% | 86% |
| 4a1-3 | 4a1-4 | 11.1% | 12.66 | 2.5% | 11% | 37% | 83% |
| 4a1-4 | 4a1-4 | 2.8% | 12.78 | 1.9% | 8.6% | 33% | 78% |

**4a2**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 4a2-1 | 2-2, diagonal over diagonal | 5–8 | `F2 R2 U B2 F2 U' L2 R2 U' R2 D2 F2 U` (13) | `U R2 U2 F2 U` | 4a1 |  | 16.7% | 12.86 | 2.4% | 9.3% | 31% | 72% |
| 4a2-2 | 2-2, pairs stacked | 6–9 | `B2 L2 D' L2 D2 B2 D F2 R2 U2 R2 F2 D2` (13) | `D' B2 D2 R2 U R2` | nothing (set up first) |  | 33.3% | 13.14 | 1.4% | 6.1% | 22% | 60% |
| 4a2-3 | 2-2, pairs on opposite sides | 7–10 | `D R2 U2 L2 R2 B2 U' B2 R2 U B2 U2 R2 U'` (14) | `U' R2 U2 F2 U R2 U2` | nothing (set up first) |  | 33.3% | 13.58 | 0.50% | 2.7% | 12% | 42% |
| 4a2-4 | 4-0 | 8–11 | `B2 R2 U2 R2 U' B2 R2 U2 R2 D B2 L2 U2 L2` (14) | `D R2 U2 F2 U F2 U2 R2` | nothing (set up first) |  | 16.7% | 13.80 | 0.32% | 1.9% | 9.3% | 33% |

4a2, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---:|---:|---:|---:|---:|---:|
| 4a2-1 | 4a2-1 | 2.8% | 12.54 | 4.4% | 14% | 43% | 83% |
| 4a2-2 | 4a2-1 | 11.1% | 12.71 | 3.1% | 12% | 35% | 79% |
| 4a2-2 | 4a2-2 | 11.1% | 12.97 | 1.8% | 7.7% | 27% | 68% |
| 4a2-3 | 4a2-1 | 11.1% | 13.02 | 1.3% | 6.6% | 25% | 66% |
| 4a2-4 | 4a2-1 | 5.6% | 13.16 | 1.0% | 4.8% | 21% | 61% |
| 4a2-2 | 4a2-3 | 22.2% | 13.33 | 0.68% | 3.5% | 16% | 53% |
| 4a2-4 | 4a2-2 | 11.1% | 13.52 | 0.42% | 2.7% | 12% | 43% |
| 4a2-3 | 4a2-3 | 11.1% | 13.85 | 0.15% | 1.1% | 6.3% | 29% |
| 4a2-4 | 4a2-3 | 11.1% | 14.09 | 0.04% | 0.59% | 4.2% | 20% |
| 4a2-4 | 4a2-4 | 2.8% | 14.42 | 0 | 0.16% | 2.3% | 13% |

**4b2**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 4b2-1 | 2-2, pairs sharing one column | 3–6 | `U' L2 D' L2 U' F2 U L2 U2 R2 D' R2 U'` (13) | `U R2 U'` | 4a1 |  | 16.7% | 12.50 | 3.4% | 14% | 44% | 88% |
| 4b2-2 | 3-1 | 4–7 | `U' L2 D' L2 U B2 D2 B2 U' L2 U B2 D'` (13) | `D' F2 U' F2` | nothing (set up first) | looks the same as the 3-1 case with L 5–8. Only the corner solution separates them: L = 4 is this one | 33.3% | 12.61 | 2.5% | 11% | 40% | 86% |
| 4b2-3 | 3-1 | 5–8 | `R2 U L2 R2 D L2 U' B2 F2 R2 D' R2 D2` (13) | `U' L2 U' F2 U2` | nothing (set up first) | looks the same as the 3-1 case with L 4–7. Only the corner solution separates them: L = 8 is this one | 33.3% | 12.76 | 1.7% | 8.4% | 33% | 81% |
| 4b2-4 | 2-2, pairs sharing one column | 6–9 | `B2 D2 L2 D R2 F2 D' L2 B2 F2 D' U' L2` (13) | `D F2 U R2 U2 F2` | nothing (set up first) |  | 16.7% | 12.85 | 1.3% | 7.0% | 30% | 78% |

4b2, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---:|---:|---:|---:|---:|---:|
| 4b2-1 | 4b2-1 | 2.8% | 12.36 | 4.8% | 17% | 50% | 91% |
| 4b2-2 | 4b2-1 | 11.1% | 12.44 | 3.8% | 15% | 47% | 90% |
| 4b2-2 | 4b2-2 | 11.1% | 12.55 | 2.9% | 12% | 42% | 87% |
| 4b2-3 | 4b2-1 | 11.1% | 12.56 | 2.8% | 12% | 41% | 87% |
| 4b2-4 | 4b2-1 | 5.6% | 12.63 | 2.5% | 11% | 38% | 85% |
| 4b2-3 | 4b2-2 | 22.2% | 12.67 | 2.1% | 9.7% | 36% | 84% |
| 4b2-2 | 4b2-4 | 11.1% | 12.75 | 1.6% | 8.2% | 33% | 82% |
| 4b2-3 | 4b2-3 | 11.1% | 12.85 | 1.2% | 6.8% | 29% | 78% |
| 4b2-3 | 4b2-4 | 11.1% | 12.95 | 0.87% | 5.3% | 26% | 74% |
| 4b2-4 | 4b2-4 | 2.8% | 13.06 | 0.61% | 4.2% | 21% | 69% |

**0c3**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 0c3-1 | none bad | 9–12 | `R2 U F2 U2 L2 D' L2 U B2 U2 L2 U' F2 U'` (14) | `D' R2 D2 F2 U F2 U2 R2 U` | 4a2 |  | 33.3% | 14.29 | 0.09% | 0.70% | 4.0% | 18% |
| 0c3-2 | none bad | 10–12 | `L2 B2 D L2 F2 U2 F2 D L2 U2 B2 U' L2 B2 U2` (15) | `U L2 D2 F2 U F2 U2 R2 U R2` | nothing (set up first) |  | 66.7% | 14.54 | 0.01% | 0.22% | 1.9% | 11% |

0c3, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---:|---:|---:|---:|---:|---:|
| 0c3-1 | 0c3-1 | 11.1% | 14.22 | 0.20% | 1.1% | 5.4% | 23% |
| 0c3-1 | 0c3-2 | 44.4% | 14.33 | 0.04% | 0.51% | 3.3% | 15% |
| 0c3-2 | 0c3-2 | 44.4% | 14.65 | 0 | 0.08% | 1.2% | 9.0% |

**2c3**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 2c3-1 | 1 up 1 down, stacked | 5–8 | `R2 D' F2 D' R2 D2 F2 R2 U F2 D' L2 U'` (13) | `D' F2 D' L2 U'` | 4b2 |  | 25.0% | 12.68 | 2.1% | 9.9% | 37% | 83% |
| 2c3-2 | 1 up 1 down, opposite | 5–8 | `L2 D2 B2 D R2 D' B2 L2 D R2 U B2 U'` (13) | `U' R2 U' R2 U` | 4b2 |  | 25.0% | 12.87 | 1.5% | 7.2% | 29% | 75% |
| 2c3-3 | both on one layer, adjacent | 6–9 | `L2 B2 F2 D' R2 F2 D' F2 D2 U' F2 L2 D2` (13) | `U R2 U' F2 U F2` | nothing (set up first) |  | 50.0% | 13.08 | 0.89% | 4.9% | 22% | 66% |

2c3, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---:|---:|---:|---:|---:|---:|
| 2c3-1 | 2c3-1 | 6.2% | 12.49 | 3.1% | 14% | 45% | 88% |
| 2c3-2 | 2c3-1 | 12.5% | 12.64 | 2.3% | 10% | 38% | 85% |
| 2c3-3 | 2c3-1 | 25.0% | 12.78 | 1.5% | 7.7% | 32% | 80% |
| 2c3-2 | 2c3-2 | 6.2% | 12.84 | 1.6% | 7.7% | 30% | 77% |
| 2c3-3 | 2c3-2 | 25.0% | 13.01 | 1.0% | 5.4% | 24% | 70% |
| 2c3-3 | 2c3-3 | 25.0% | 13.25 | 0.53% | 3.3% | 16% | 57% |

**4c3**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 4c3-1 | 2-2, pairs on opposite sides | 7–9 | `D R2 D' F2 D' B2 R2 B2 U L2 D2 U' R2` (13) | `D B2 U F2 U2 R2 U` | 4b2 |  | 8.3% | 13.06 | 0.75% | 4.5% | 22% | 68% |
| 4c3-2 | 2-2, pairs stacked | 7–9 | `R2 U' F2 U R2 B2 D L2 U2 R2 U' R2 U'` (13) | `D' R2 D' B2 U2 R2 U` | 4b2 |  | 8.3% | 13.21 | 0.62% | 3.6% | 18% | 60% |
| 4c3-3 | 4-0 | 8–9 | `D2 B2 D' B2 U' B2 D2 L2 U' L2 U' F2 U'` (13) | `D' R2 U B2 U2 R2 U R2` | nothing (set up first) | looks the same as the 4-0 case with L 9–10. Only the corner solution separates them: L = 8 is this one | 4.2% | 13.27 | 0.40% | 2.8% | 15% | 57% |
| 4c3-4 | 2-2, pairs sharing one column | 7–10 | `R2 D2 R2 U L2 U' B2 R2 B2 U L2 D F2 U'` (14) | `D' B2 U2 R2 U F2 U` | 4a2 |  | 16.7% | 13.45 | 0.50% | 2.8% | 13% | 47% |
| 4c3-5 | 3-1 | 8–11 | `R2 F2 U' B2 D' B2 R2 D' R2 D R2 U2 L2 U'` (14) | `D B2 D2 R2 U F2 U' R2` | nothing (set up first) |  | 33.3% | 13.51 | 0.29% | 2.0% | 11% | 45% |
| 4c3-6 | 2-2, diagonal over diagonal | 8–10 | `B2 F2 U' F2 L2 U R2 U2 L2 R2 B2 D' F2 L2` (14) | `U' F2 U' R2 U2 F2 U F2` | nothing (set up first) |  | 8.3% | 13.52 | 0.26% | 1.8% | 10% | 43% |
| 4c3-7 | 2-2, pairs stacked | 8–10 | `D' L2 U' F2 D' F2 L2 D' L2 U B2 U2 R2 U2` (14) | `U' L2 U' R2 U2 F2 U F2` | nothing (set up first) |  | 8.3% | 13.59 | 0.23% | 1.6% | 9.4% | 40% |
| 4c3-8 | 4-0 | 9–10 | `D' F2 U L2 D' L2 R2 U' B2 U R2 D F2 U'` (14) | `U' F2 D R2 U2 F2 U R2 U2` | nothing (set up first) | looks the same as the 4-0 case with L 8–9. Only the corner solution separates them: L = 10 is this one | 4.2% | 13.83 | 0.07% | 0.68% | 5.1% | 28% |
| 4c3-9 | 2-2, pairs on opposite sides | 9–11 | `D' L2 U F2 D' B2 L2 U' R2 U L2 D F2 U'` (14) | `D' B2 U' F2 U2 R2 U F2 U2` | nothing (set up first) |  | 8.3% | 14.00 | 0.05% | 0.47% | 3.6% | 22% |

4c3, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---:|---:|---:|---:|---:|---:|
| 4c3-4 | 4c3-1 | 5.6% | 13.04 | 0.95% | 5.3% | 23% | 68% |
| 4c3-5 | 4c3-1 | 11.1% | 13.07 | 0.65% | 4.1% | 21% | 68% |
| 4c3-4 | 4c3-2 | 5.6% | 13.19 | 0.78% | 4.4% | 19% | 59% |
| 4c3-5 | 4c3-2 | 11.1% | 13.22 | 0.54% | 3.3% | 17% | 60% |
| 4c3-3 | 4c3-4 | 2.8% | 13.24 | 0.60% | 3.2% | 17% | 58% |
| 4c3-3 | 4c3-5 | 5.6% | 13.28 | 0.31% | 2.5% | 15% | 57% |
| 4c3-4 | 4c3-6 | 5.6% | 13.47 | 0.41% | 2.3% | 12% | 46% |
| 4c3-4 | 4c3-7 | 5.6% | 13.54 | 0.35% | 2.1% | 11% | 42% |
| 4c3-5 | 4c3-6 | 11.1% | 13.54 | 0.19% | 1.6% | 9.5% | 42% |
| 4c3-5 | 4c3-7 | 11.1% | 13.61 | 0.17% | 1.4% | 8.5% | 39% |
| 4c3-8 | 4c3-4 | 2.8% | 13.79 | 0.16% | 1.0% | 5.8% | 30% |
| 4c3-8 | 4c3-5 | 5.6% | 13.84 | 0.03% | 0.51% | 4.8% | 28% |
| 4c3-4 | 4c3-9 | 5.6% | 13.95 | 0.11% | 0.84% | 4.8% | 24% |
| 4c3-5 | 4c3-9 | 11.1% | 14.03 | 0.01% | 0.29% | 3.0% | 20% |

**0c4**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 0c4-1 | none bad | 9–10 | `B2 U R2 B2 U' L2 B2 D2 B2 U B2 R2 D2 U'` (14) | `U' F2 D L2 U2 F2 U F2 U'` | 4a3 |  | 100.0% | 13.67 | 0.08% | 0.87% | 6.7% | 36% |

**2c4**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 2c4-1 | both on one layer, adjacent | 7–10 | `R2 D' B2 F2 L2 D' B2 U B2 D' B2 F2 U2` (13) | `U F2 U L2 U' F2 U'` | 2c3 | the two diagonals of the back face agree (see the note under the table) | 16.7% | 13.27 | 0.48% | 3.1% | 16% | 57% |
| 2c4-2 | 1 up 1 down, opposite | 8–10 | `R2 B2 F2 U' L2 D2 B2 U' F2 L2 U' L2 U'` (13) | `U' F2 U' L2 U R2 U F2` | 4b3 |  | 8.3% | 13.39 | 0.31% | 2.3% | 13% | 51% |
| 2c4-3 | both on one layer, adjacent | 7–10 | `F2 U' B2 D' L2 D' L2 U B2 R2 U L2 F2 U'` (14) | `D F2 U' F2 U R2 U'` | 2c3 | the two diagonals of the back face differ (see the note under the table) | 16.7% | 13.45 | 0.38% | 2.4% | 13% | 47% |
| 2c4-4 | both on one layer, adjacent | 8–11 | `B2 D2 R2 U F2 U L2 U' R2 D2 R2 F2 U' R2` (14) | `U' R2 U' R2 U F2 U' F2` | nothing (set up first) |  | 16.7% | 13.77 | 0.15% | 1.1% | 7.0% | 33% |
| 2c4-5 | 1 up 1 down, stacked | 9–11 | `B2 U B2 U2 B2 F2 R2 D B2 L2 U' B2 R2 U'` (14) | `D F2 U2 R2 U F2 U' F2 U` | 4b3 |  | 8.3% | 13.77 | 0.13% | 1.1% | 7.0% | 33% |
| 2c4-6 | 1 up 1 down, opposite | 8–11 | `U' L2 D B2 U2 B2 L2 F2 U' L2 B2 D2 U' R2` (14) | `U' R2 U F2 U' R2 U R2` | nothing (set up first) |  | 16.7% | 13.80 | 0.13% | 0.99% | 6.4% | 31% |
| 2c4-7 | 1 up 1 down, stacked | 9–12 | `U F2 U' L2 F2 D B2 R2 F2 D2 B2 U' F2 U2` (14) | `U F2 D' L2 U F2 U' F2 U2` | nothing (set up first) |  | 16.7% | 14.01 | 0.04% | 0.52% | 4.1% | 23% |

**Telling the two look-alike 2c4 cases apart.** Hold the cube so the two bad corners are on the front edge of one layer (if you see six bad corners, turn both layers, U D', and you will see two). The four corners of the back face are then all good. Take each diagonal of the back face. Its two corners share exactly one colour: their sticker on the back face, their U/D sticker, or their sticker on the side. If both diagonals share the same kind of sticker, the diagonals agree; otherwise they differ.

2c4, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---:|---:|---:|---:|---:|---:|
| 2c4-1 | 2c4-1 | 2.8% | 12.93 | 0.92% | 5.6% | 26% | 75% |
| 2c4-1 | 2c4-2 | 2.8% | 13.01 | 0.68% | 4.4% | 23% | 72% |
| 2c4-3 | 2c4-1 | 5.6% | 13.11 | 0.72% | 4.3% | 20% | 65% |
| 2c4-2 | 2c4-2 | 0.7% | 13.15 | 0.37% | 3.2% | 18% | 65% |
| 2c4-3 | 2c4-2 | 2.8% | 13.17 | 0.56% | 3.5% | 18% | 62% |
| 2c4-3 | 2c4-3 | 2.8% | 13.32 | 0.55% | 3.1% | 15% | 54% |
| 2c4-1 | 2c4-5 | 2.8% | 13.32 | 0.32% | 2.3% | 14% | 54% |
| 2c4-4 | 2c4-1 | 5.6% | 13.40 | 0.32% | 2.2% | 12% | 50% |
| 2c4-1 | 2c4-6 | 5.6% | 13.44 | 0.28% | 1.9% | 12% | 48% |
| 2c4-3 | 2c4-5 | 2.8% | 13.47 | 0.29% | 1.9% | 11% | 46% |
| 2c4-4 | 2c4-2 | 2.8% | 13.49 | 0.19% | 1.7% | 10% | 45% |
| 2c4-5 | 2c4-2 | 1.4% | 13.53 | 0.09% | 1.3% | 9.1% | 43% |
| 2c4-6 | 2c4-2 | 2.8% | 13.54 | 0.17% | 1.4% | 9.1% | 42% |
| 2c4-1 | 2c4-7 | 5.6% | 13.59 | 0.12% | 1.2% | 8.4% | 40% |
| 2c4-4 | 2c4-3 | 5.6% | 13.60 | 0.26% | 1.6% | 9.3% | 40% |
| 2c4-3 | 2c4-6 | 5.6% | 13.63 | 0.21% | 1.5% | 8.7% | 38% |
| 2c4-3 | 2c4-7 | 5.6% | 13.73 | 0.11% | 1.1% | 6.8% | 33% |
| 2c4-7 | 2c4-2 | 2.8% | 13.78 | 0.02% | 0.49% | 5.1% | 30% |
| 2c4-4 | 2c4-5 | 2.8% | 13.82 | 0.05% | 0.75% | 5.4% | 29% |
| 2c4-6 | 2c4-5 | 2.8% | 13.87 | 0.05% | 0.69% | 4.9% | 27% |
| 2c4-4 | 2c4-4 | 2.8% | 13.90 | 0.09% | 0.77% | 5.0% | 26% |
| 2c4-4 | 2c4-6 | 5.6% | 13.95 | 0.08% | 0.64% | 4.4% | 24% |
| 2c4-6 | 2c4-6 | 2.8% | 13.98 | 0.07% | 0.55% | 3.9% | 23% |
| 2c4-4 | 2c4-7 | 5.6% | 14.09 | <0.01% | 0.26% | 2.8% | 19% |
| 2c4-6 | 2c4-7 | 5.6% | 14.11 | <0.01% | 0.25% | 2.7% | 18% |
| 2c4-5 | 2c4-5 | 0.7% | 14.13 | 0 | 0.18% | 2.5% | 18% |
| 2c4-7 | 2c4-5 | 2.8% | 14.33 | 0 | 0.07% | 1.3% | 12% |
| 2c4-7 | 2c4-7 | 2.8% | 14.49 | 0 | 0.03% | 0.63% | 7.5% |

**4c4**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 4c4-1 | 2-2, diagonal over diagonal | 9–10 | `L2 B2 D2 B2 D' L2 B2 D B2 U2 R2 U' R2 U'` (14) | `U' R2 U' R2 U2 F2 U R2 U` | 4a3 |  | 8.3% | 13.97 | 0.08% | 0.63% | 4.3% | 23% |
| 4c4-2 | 2-2, pairs sharing one column | 9–11 | `F2 U B2 R2 U' R2 D2 F2 D' B2 R2 U2 R2 U'` (14) | `U' R2 U' F2 U2 R2 U R2 U` | 4a3 |  | 16.7% | 14.25 | 0.04% | 0.33% | 2.5% | 15% |
| 4c4-3 | 2-2, pairs stacked | 10–11 | `B2 L2 F2 U' R2 U F2 U' L2 D L2 U L2 D` (14) | `U L2 D' B2 U2 R2 U F2 U' R2` | nothing (set up first) |  | 16.7% | 14.27 | 0.01% | 0.20% | 1.9% | 13% |
| 4c4-4 | 3-1 | 10–12 | `U' F2 D' L2 B2 D2 F2 U F2 R2 U2 R2 U F2 R2` (15) | `D' R2 D' B2 U2 R2 U R2 U' R2` | nothing (set up first) |  | 33.3% | 14.48 | <0.01% | 0.11% | 1.2% | 9.3% |
| 4c4-5 | 2-2, pairs on opposite sides | 11–12 | `R2 B2 D R2 U' B2 U' F2 D F2 U' F2 U L2 U2` (15) | `D B2 U' L2 U2 F2 U R2 U' R2 U2` | nothing (set up first) |  | 16.7% | 14.60 | 0 | 0.03% | 0.59% | 6.0% |
| 4c4-6 | 4-0 | 11–12 | `B2 U R2 F2 D2 F2 D' F2 R2 D2 R2 D' F2 R2 U'` (15) | `D F2 U2 R2 U F2 U2 R2 U F2 U` | 0c3 |  | 8.3% | 14.71 | 0 | 0.03% | 0.57% | 5.6% |

4c4, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---:|---:|---:|---:|---:|---:|
| 4c4-2 | 4c4-1 | 5.6% | 13.87 | 0.17% | 0.92% | 5.6% | 28% |
| 4c4-4 | 4c4-1 | 11.1% | 14.01 | 0.03% | 0.49% | 3.7% | 21% |
| 4c4-2 | 4c4-3 | 11.1% | 14.14 | 0.03% | 0.43% | 2.9% | 17% |
| 4c4-4 | 4c4-3 | 22.2% | 14.33 | 0 | 0.08% | 1.3% | 11% |
| 4c4-5 | 4c4-2 | 11.1% | 14.43 | 0 | 0.07% | 1.1% | 9.4% |
| 4c4-6 | 4c4-2 | 5.6% | 14.50 | 0 | 0.08% | 1.3% | 9.5% |
| 4c4-4 | 4c4-5 | 22.2% | 14.69 | 0 | 0.01% | 0.33% | 4.3% |
| 4c4-6 | 4c4-4 | 11.1% | 14.81 | 0 | 0 | 0.20% | 3.7% |

**2c5**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 2c5-1 | both on one layer, adjacent | 9–12 | `D' R2 D R2 U2 L2 D' F2 U' R2 U F2 L2 U2` (14) | `U R2 U F2 U' F2 U R2 U` | 2c4 |  | 50.0% | 14.12 | 0.05% | 0.45% | 3.4% | 19% |
| 2c5-2 | 1 up 1 down, opposite | 10–13 | `B2 D U2 F2 U L2 U R2 U2 L2 U' F2 U' R2` (14) | `D B2 U' R2 U F2 U' R2 U R2` | 4b4 |  | 25.0% | 14.34 | 0.01% | 0.20% | 1.9% | 13% |
| 2c5-3 | 1 up 1 down, stacked | 11–13 | `B2 D' B2 D' B2 R2 D2 L2 U' F2 D F2 L2 U R2` (15) | `D F2 U' F2 U F2 U' F2 U R2 U2` | 4b4 |  | 25.0% | 14.72 | 0 | 0.03% | 0.62% | 6.0% |

2c5, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---:|---:|---:|---:|---:|---:|
| 2c5-1 | 2c5-1 | 25.0% | 13.95 | 0.08% | 0.69% | 4.7% | 25% |
| 2c5-1 | 2c5-2 | 25.0% | 14.15 | 0.02% | 0.35% | 2.9% | 18% |
| 2c5-2 | 2c5-2 | 6.2% | 14.38 | 0 | 0.09% | 1.4% | 11% |
| 2c5-1 | 2c5-3 | 25.0% | 14.44 | 0 | 0.06% | 1.1% | 9.5% |
| 2c5-2 | 2c5-3 | 12.5% | 14.69 | 0 | 0 | 0.24% | 4.5% |
| 2c5-3 | 2c5-3 | 6.2% | 15.31 | 0 | 0 | 0 | 0.64% |

**4b5**

| Case | Bad corners | L | A typical DR (its optimal) | Shortest setup of these corners | A qt takes it straight to | Told apart from a look-alike by | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 4b5-1 | 3-1 | 9–12 | `D' L2 F2 U' B2 D B2 L2 D B2 F2 R2 D' U2` (14) | `U' L2 D F2 U' R2 U F2 U` | 2c4 |  | 66.7% | 14.23 | 0.02% | 0.25% | 2.2% | 15% |
| 4b5-2 | 2-2, pairs sharing one column | 10–12 | `R2 D' L2 U L2 U' B2 U L2 F2 U' L2 B2 D2` (14) | `D F2 U R2 U' R2 U R2 U F2` | 4a4 |  | 33.3% | 14.37 | <0.01% | 0.12% | 1.3% | 11% |

4b5, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | In 10 | In 11 | In 12 | In 13 |
|---|---|---:|---:|---:|---:|---:|---:|
| 4b5-1 | 4b5-1 | 44.4% | 14.19 | 0.03% | 0.30% | 2.6% | 17% |
| 4b5-1 | 4b5-2 | 44.4% | 14.31 | <0.01% | 0.16% | 1.6% | 12% |
| 4b5-2 | 4b5-2 | 11.1% | 14.48 | 0 | 0.03% | 0.75% | 7.9% |

---

## Appendix F: HTR length on both sides, all 48 subsets

One table per subset, one row per pair of HTR lengths (the shorter of normal and inverse, then the longer). Fastest is the shortest optimal finish in the row. These are the true shortest HTRs.

**0c0 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 50% | 9.89 | 0 | 65% | 91% | 99.5% | 100% |
| 2 | 2 | 50% | 10.00 | 2 | 62% | 89% | 99% | 100% |

**0c0 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 5 | 25% | 11.58 | 5 | 14% | 42% | 82% | 99.1% |
| 5 | 6 | 50% | 11.67 | 6 | 12% | 38% | 81% | 99.2% |
| 6 | 6 | 25% | 11.84 | 7 | 8.1% | 32% | 76% | 99% |

**0c0 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 4 | 0.31% | 11.96 | 4 | 11% | 34% | 64% | 90% |
| 4 | 5 | 2.5% | 11.90 | 5 | 11% | 30% | 68% | 97% |
| 4 | 6 | 4.3% | 11.87 | 6 | 9.9% | 33% | 70% | 96% |
| 4 | 7 | 3.7% | 11.81 | 7 | 13% | 33% | 70% | 98% |
| 5 | 5 | 4.9% | 12.30 | 6 | 4.8% | 19% | 54% | 91% |
| 5 | 6 | 17% | 12.32 | 7 | 4.6% | 17% | 53% | 92% |
| 5 | 7 | 15% | 12.20 | 8 | 5.3% | 21% | 57% | 95% |
| 6 | 6 | 15% | 12.45 | 8 | 3.4% | 14% | 47% | 90% |
| 6 | 7 | 26% | 12.38 | 8 | 3.0% | 15% | 51% | 93% |
| 7 | 7 | 11% | 12.51 | 8 | 1.8% | 12% | 45% | 90% |

**0c0 6e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 7 | 25% | 12.90 | 7 | 1.3% | 6.7% | 28% | 75% |
| 7 | 8 | 50% | 12.91 | 8 | 0.91% | 5.9% | 27% | 76% |
| 8 | 8 | 25% | 12.95 | 9 | 0.65% | 4.9% | 25% | 74% |

**0c0 8e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | 6 | 100% | 12.69 | 6 | 3.0% | 13% | 39% | 78% |

**4a1 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 7 | 2.8% | 12.91 | 7 | 2.2% | 7.5% | 28% | 72% |
| 7 | 8 | 11% | 12.81 | 8 | 1.8% | 8.2% | 31% | 77% |
| 7 | 9 | 11% | 12.73 | 9 | 1.8% | 8.4% | 35% | 82% |
| 7 | 10 | 5.6% | 12.83 | 10 | 1.0% | 7.4% | 31% | 79% |
| 8 | 8 | 11% | 12.96 | 9 | 1.3% | 6.1% | 25% | 73% |
| 8 | 9 | 22% | 12.94 | 9 | 0.70% | 5.6% | 26% | 75% |
| 8 | 10 | 11% | 13.09 | 10 | 0.06% | 2.5% | 19% | 69% |
| 9 | 9 | 11% | 13.17 | 9 | 0.21% | 2.8% | 19% | 64% |
| 9 | 10 | 11% | 13.37 | 10 | 0.06% | 0.95% | 11% | 54% |
| 10 | 10 | 2.8% | 13.82 | 11 | 0 | 0.19% | 3.0% | 28% |

**4a1 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | 6 | 6.2% | 12.19 | 6 | 4.9% | 20% | 59% | 96% |
| 6 | 7 | 27% | 12.34 | 7 | 3.4% | 16% | 52% | 94% |
| 6 | 8 | 10% | 12.48 | 8 | 2.1% | 12% | 46% | 92% |
| 7 | 7 | 29% | 12.58 | 7 | 2.1% | 11% | 41% | 87% |
| 7 | 8 | 23% | 12.80 | 8 | 1.1% | 6.8% | 31% | 81% |
| 8 | 8 | 4.3% | 13.11 | 10 | 0.14% | 2.4% | 18% | 69% |

**4a1 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | <0.01% | 10.10 | 1 | 50% | 80% | 95% | 100% |
| 1 | 2 | 0.02% | 9.67 | 2 | 66% | 94% | 100% | 100% |
| 1 | 3 | 0.04% | 9.69 | 3 | 67% | 93% | 99.2% | 100% |
| 1 | 4 | 0.09% | 9.67 | 4 | 67% | 95% | 100% | 100% |
| 1 | 5 | 0.14% | 9.79 | 5 | 69% | 95% | 99.8% | 100% |
| 1 | 6 | 0.24% | 9.91 | 6 | 66% | 92% | 99.8% | 100% |
| 1 | 7 | 0.33% | 10.34 | 7 | 52% | 87% | 99.7% | 100% |
| 1 | 8 | 0.07% | 10.85 | 8 | 34% | 73% | 100% | 100% |
| 2 | 2 | 0.03% | 10.27 | 3 | 50% | 78% | 96% | 100% |
| 2 | 3 | 0.17% | 10.36 | 4 | 45% | 75% | 97% | 99.9% |
| 2 | 4 | 0.34% | 10.40 | 5 | 50% | 74% | 97% | 100% |
| 2 | 5 | 0.57% | 10.56 | 6 | 43% | 78% | 97% | 99.8% |
| 2 | 6 | 0.96% | 10.69 | 7 | 40% | 78% | 98% | 99.9% |
| 2 | 7 | 1.3% | 11.13 | 8 | 23% | 61% | 96% | 100% |
| 2 | 8 | 0.27% | 11.69 | 9 | 7.4% | 39% | 83% | 100% |
| 3 | 3 | 0.21% | 10.68 | 5 | 41% | 64% | 90% | 99.6% |
| 3 | 4 | 0.86% | 10.80 | 6 | 39% | 65% | 89% | 99.5% |
| 3 | 5 | 1.4% | 11.00 | 7 | 32% | 63% | 91% | 99.6% |
| 3 | 6 | 2.4% | 11.12 | 8 | 24% | 64% | 94% | 99.9% |
| 3 | 7 | 3.3% | 11.56 | 7 | 12% | 44% | 86% | 99.7% |
| 3 | 8 | 0.69% | 12.12 | 9 | 3.0% | 19% | 68% | 98% |
| 4 | 4 | 0.86% | 11.23 | 7 | 30% | 56% | 81% | 97% |
| 4 | 5 | 2.8% | 11.52 | 8 | 17% | 48% | 80% | 97% |
| 4 | 6 | 4.8% | 11.73 | 7 | 9.4% | 37% | 81% | 99% |
| 4 | 7 | 6.5% | 12.09 | 7 | 4.4% | 23% | 66% | 97% |
| 4 | 8 | 1.4% | 12.54 | 8 | 1.9% | 11% | 43% | 89% |
| 5 | 5 | 2.3% | 11.94 | 8 | 8.2% | 31% | 70% | 96% |
| 5 | 6 | 7.9% | 12.19 | 7 | 3.2% | 19% | 62% | 96% |
| 5 | 7 | 11% | 12.44 | 7 | 1.9% | 12% | 49% | 93% |
| 5 | 8 | 2.3% | 12.80 | 8 | 1.4% | 7.1% | 31% | 81% |
| 6 | 6 | 6.7% | 12.51 | 8 | 0.92% | 9.5% | 46% | 93% |
| 6 | 7 | 18% | 12.64 | 8 | 1.4% | 8.1% | 38% | 89% |
| 6 | 8 | 3.8% | 12.89 | 9 | 0.94% | 6.0% | 27% | 77% |
| 7 | 7 | 12% | 12.71 | 7 | 1.4% | 8.0% | 34% | 85% |
| 7 | 8 | 5.2% | 12.93 | 8 | 0.72% | 5.2% | 26% | 75% |
| 8 | 8 | 0.55% | 13.17 | 10 | 0.37% | 2.8% | 19% | 64% |

**4a2 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 2.8% | 13.08 | 9 | 1.1% | 6.0% | 25% | 64% |
| 9 | 10 | 11% | 13.25 | 10 | 0.55% | 3.5% | 18% | 57% |
| 9 | 11 | 11% | 13.54 | 11 | 0 | 1.4% | 9.8% | 42% |
| 9 | 12 | 5.6% | 13.75 | 12 | 0 | 0 | 4.7% | 33% |
| 10 | 10 | 11% | 13.60 | 11 | 0 | 1.1% | 9.1% | 41% |
| 10 | 11 | 22% | 13.89 | 11 | 0 | 0.08% | 3.8% | 26% |
| 10 | 12 | 11% | 14.21 | 12 | 0 | 0 | 0.30% | 12% |
| 11 | 11 | 11% | 14.31 | 11 | 0 | 0.08% | 1.4% | 12% |
| 11 | 12 | 11% | 14.59 | 12 | 0 | 0 | 0.30% | 5.7% |
| 12 | 12 | 2.8% | 15.01 | 13 | 0 | 0 | 0 | 0.95% |

**4a2 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 8 | 1.6% | 12.76 | 8 | 2.6% | 9.7% | 35% | 77% |
| 8 | 9 | 9.4% | 12.92 | 9 | 1.6% | 7.3% | 27% | 74% |
| 8 | 10 | 8.3% | 13.21 | 10 | 0.32% | 3.3% | 17% | 60% |
| 8 | 11 | 4.2% | 13.37 | 11 | 0 | 1.2% | 13% | 53% |
| 9 | 9 | 14% | 13.22 | 9 | 0.30% | 3.2% | 18% | 59% |
| 9 | 10 | 25% | 13.60 | 10 | <0.01% | 0.65% | 7.6% | 40% |
| 9 | 11 | 12% | 13.83 | 11 | 0 | 0.03% | 2.5% | 28% |
| 10 | 10 | 11% | 14.17 | 11 | 0 | 0.05% | 1.5% | 16% |
| 10 | 11 | 11% | 14.45 | 12 | 0 | 0 | 0.20% | 6.1% |
| 11 | 11 | 2.8% | 14.85 | 13 | 0 | 0 | 0 | 1.1% |

**4a2 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 5 | 0.14% | 11.61 | 5 | 20% | 44% | 70% | 94% |
| 5 | 6 | 0.82% | 11.54 | 6 | 20% | 44% | 78% | 96% |
| 5 | 7 | 1.4% | 11.82 | 7 | 12% | 36% | 71% | 96% |
| 5 | 8 | 2.2% | 12.07 | 8 | 7.5% | 25% | 65% | 94% |
| 5 | 9 | 1.6% | 12.28 | 9 | 3.9% | 18% | 55% | 93% |
| 5 | 10 | 0.96% | 12.65 | 10 | 2.4% | 9.9% | 37% | 85% |
| 5 | 11 | 0.21% | 12.70 | 11 | 0 | 11% | 38% | 81% |
| 6 | 6 | 1.2% | 11.67 | 7 | 15% | 42% | 75% | 97% |
| 6 | 7 | 4.1% | 12.03 | 8 | 8.2% | 27% | 66% | 93% |
| 6 | 8 | 6.6% | 12.30 | 9 | 4.4% | 18% | 54% | 93% |
| 6 | 9 | 4.7% | 12.56 | 10 | 2.2% | 11% | 43% | 89% |
| 6 | 10 | 2.9% | 12.89 | 11 | 0 | 5.4% | 28% | 79% |
| 6 | 11 | 0.62% | 13.00 | 12 | 0 | 0 | 24% | 76% |
| 7 | 7 | 3.4% | 12.49 | 9 | 3.7% | 16% | 45% | 87% |
| 7 | 8 | 11% | 12.78 | 9 | 1.6% | 8.3% | 34% | 78% |
| 7 | 9 | 7.9% | 13.07 | 10 | 0.03% | 4.1% | 21% | 70% |
| 7 | 10 | 4.8% | 13.39 | 11 | 0 | 0.23% | 12% | 53% |
| 7 | 11 | 1.0% | 13.58 | 12 | 0 | 0 | 2.0% | 47% |
| 8 | 8 | 8.8% | 13.13 | 8 | 0.16% | 3.9% | 19% | 65% |
| 8 | 9 | 13% | 13.41 | 9 | 0.13% | 1.0% | 12% | 50% |
| 8 | 10 | 7.7% | 13.64 | 10 | 0.12% | 0.95% | 6.1% | 39% |
| 8 | 11 | 1.6% | 13.84 | 11 | 0 | 0.79% | 5.0% | 24% |
| 9 | 9 | 4.5% | 13.74 | 10 | 0.08% | 0.69% | 4.7% | 35% |
| 9 | 10 | 5.5% | 13.91 | 11 | 0 | 0.44% | 4.4% | 24% |
| 9 | 11 | 1.2% | 14.17 | 11 | 0 | 0.20% | 3.6% | 21% |
| 10 | 10 | 1.7% | 14.16 | 11 | 0 | 0.04% | 2.0% | 18% |
| 10 | 11 | 0.72% | 14.33 | 12 | 0 | 0 | 0.10% | 11% |
| 11 | 11 | 0.08% | 14.64 | 13 | 0 | 0 | 0 | 0.13% |

**4b2 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | 6 | 2.8% | 12.62 | 6 | 3.7% | 11% | 40% | 83% |
| 6 | 7 | 11% | 12.63 | 7 | 3.3% | 12% | 36% | 84% |
| 6 | 8 | 11% | 12.68 | 8 | 2.2% | 10% | 37% | 82% |
| 6 | 9 | 5.6% | 12.66 | 9 | 2.1% | 11% | 38% | 84% |
| 7 | 7 | 11% | 12.82 | 8 | 1.7% | 8.6% | 31% | 76% |
| 7 | 8 | 22% | 12.91 | 8 | 1.3% | 6.6% | 27% | 74% |
| 7 | 9 | 11% | 12.94 | 9 | 0.54% | 5.3% | 27% | 74% |
| 8 | 8 | 11% | 13.11 | 8 | 0.42% | 3.8% | 20% | 65% |
| 8 | 9 | 11% | 13.19 | 9 | 0.22% | 2.5% | 17% | 63% |
| 9 | 9 | 2.8% | 13.36 | 9 | 0.30% | 1.7% | 12% | 54% |

**4b2 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 3 | 0.01% | 11.20 | 3 | 18% | 58% | 91% | 99.6% |
| 3 | 4 | 0.09% | 11.19 | 4 | 22% | 54% | 92% | 99.9% |
| 3 | 5 | 0.33% | 11.26 | 5 | 21% | 53% | 89% | 99.9% |
| 3 | 6 | 0.85% | 11.32 | 6 | 21% | 51% | 86% | 99.7% |
| 3 | 7 | 0.72% | 11.38 | 7 | 20% | 50% | 85% | 99.7% |
| 3 | 8 | 0.09% | 11.32 | 8 | 22% | 53% | 86% | 99.3% |
| 4 | 4 | 0.17% | 11.66 | 5 | 12% | 38% | 78% | 99.1% |
| 4 | 5 | 1.3% | 11.84 | 6 | 9.8% | 30% | 72% | 98% |
| 4 | 6 | 3.4% | 11.97 | 7 | 8.7% | 27% | 67% | 97% |
| 4 | 7 | 2.9% | 12.08 | 8 | 6.9% | 24% | 63% | 96% |
| 4 | 8 | 0.35% | 12.12 | 9 | 6.4% | 24% | 61% | 95% |
| 5 | 5 | 2.4% | 12.15 | 6 | 6.1% | 21% | 59% | 96% |
| 5 | 6 | 13% | 12.35 | 7 | 4.1% | 16% | 51% | 93% |
| 5 | 7 | 11% | 12.50 | 8 | 2.6% | 12% | 44% | 90% |
| 5 | 8 | 1.3% | 12.62 | 9 | 1.5% | 9.9% | 40% | 87% |
| 6 | 6 | 17% | 12.60 | 7 | 2.0% | 10% | 40% | 87% |
| 6 | 7 | 28% | 12.80 | 7 | 0.92% | 6.7% | 31% | 82% |
| 6 | 8 | 3.4% | 12.99 | 9 | 0.19% | 3.4% | 23% | 75% |
| 7 | 7 | 12% | 13.03 | 8 | 0.44% | 3.7% | 22% | 72% |
| 7 | 8 | 2.9% | 13.25 | 10 | 0.06% | 1.3% | 14% | 61% |
| 8 | 8 | 0.17% | 13.52 | 10 | 0.05% | 0.57% | 5.7% | 45% |

**4b2 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 4 | <0.01% | 10.97 | 4 | 34% | 60% | 81% | 98% |
| 4 | 5 | 0.05% | 10.98 | 5 | 31% | 60% | 89% | 99.9% |
| 4 | 6 | 0.21% | 11.21 | 6 | 24% | 53% | 89% | 99.8% |
| 4 | 7 | 0.60% | 11.45 | 7 | 17% | 47% | 85% | 99.8% |
| 4 | 8 | 0.78% | 11.59 | 8 | 13% | 41% | 84% | 99.6% |
| 4 | 9 | 0.20% | 11.66 | 9 | 12% | 40% | 81% | 99.5% |
| 5 | 5 | 0.08% | 11.37 | 6 | 21% | 48% | 83% | 99.3% |
| 5 | 6 | 0.62% | 11.67 | 7 | 13% | 38% | 77% | 99% |
| 5 | 7 | 1.8% | 11.94 | 7 | 8.7% | 28% | 69% | 98% |
| 5 | 8 | 2.3% | 12.11 | 8 | 5.1% | 22% | 63% | 98% |
| 5 | 9 | 0.59% | 12.22 | 9 | 3.1% | 19% | 60% | 96% |
| 6 | 6 | 1.2% | 12.07 | 6 | 7.4% | 24% | 63% | 96% |
| 6 | 7 | 7.2% | 12.35 | 7 | 4.0% | 16% | 51% | 93% |
| 6 | 8 | 9.4% | 12.56 | 8 | 1.7% | 10% | 42% | 90% |
| 6 | 9 | 2.4% | 12.72 | 9 | 0.47% | 6.5% | 35% | 87% |
| 7 | 7 | 11% | 12.58 | 7 | 1.9% | 11% | 41% | 88% |
| 7 | 8 | 27% | 12.78 | 8 | 0.83% | 6.4% | 32% | 83% |
| 7 | 9 | 6.9% | 12.98 | 9 | 0.38% | 3.3% | 23% | 76% |
| 8 | 8 | 18% | 12.99 | 8 | 0.50% | 3.9% | 23% | 74% |
| 8 | 9 | 9.0% | 13.21 | 9 | 0.19% | 2.0% | 15% | 63% |
| 9 | 9 | 1.1% | 13.44 | 10 | 0.06% | 0.95% | 9.2% | 48% |

**0c3 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 10 | 11% | 13.81 | 10 | 0.39% | 3.6% | 11% | 31% |
| 10 | 11 | 44% | 13.89 | 11 | 0 | 0.79% | 8.7% | 34% |
| 11 | 11 | 44% | 14.33 | 12 | 0 | 0 | 1.4% | 17% |

**0c3 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 2.8% | 13.61 | 9 | 1.2% | 4.3% | 16% | 42% |
| 9 | 10 | 22% | 13.86 | 10 | 0.17% | 1.7% | 8.3% | 31% |
| 9 | 11 | 5.6% | 13.92 | 11 | 0 | 0.33% | 6.5% | 31% |
| 10 | 10 | 44% | 14.44 | 11 | 0 | 0.17% | 2.1% | 13% |
| 10 | 11 | 22% | 14.48 | 12 | 0 | 0 | 0.33% | 8.1% |
| 11 | 11 | 2.8% | 14.69 | 12 | 0 | 0 | 0.09% | 6.0% |

**0c3 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 10 | 0.86% | 14.07 | 10 | 1.4% | 4.3% | 12% | 25% |
| 10 | 11 | 5.5% | 14.07 | 11 | 0 | 2.6% | 7.8% | 26% |
| 10 | 12 | 9.9% | 14.17 | 12 | 0 | 0 | 4.2% | 22% |
| 10 | 13 | 1.4% | 14.71 | 13 | 0 | 0 | 0 | 0.31% |
| 11 | 11 | 8.8% | 14.39 | 12 | 0 | 0 | 4.5% | 14% |
| 11 | 12 | 32% | 14.55 | 12 | 0 | 0 | 0.35% | 9.4% |
| 11 | 13 | 4.4% | 15.08 | 13 | 0 | 0 | 0 | 1.8% |
| 12 | 12 | 29% | 14.83 | 12 | 0 | 0 | 0.02% | 2.3% |
| 12 | 13 | 8.0% | 15.26 | 13 | 0 | 0 | 0 | 0.38% |
| 13 | 13 | 0.55% | 15.79 | 14 | 0 | 0 | 0 | 0 |

**0c3 6e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 2.8% | 13.60 | 9 | 1.2% | 4.3% | 17% | 43% |
| 9 | 10 | 22% | 13.87 | 10 | 0.17% | 1.7% | 8.3% | 31% |
| 9 | 11 | 5.6% | 13.93 | 11 | 0 | 0.33% | 6.5% | 31% |
| 10 | 10 | 44% | 14.46 | 11 | 0 | 0.17% | 2.1% | 13% |
| 10 | 11 | 22% | 14.49 | 12 | 0 | 0 | 0.33% | 8.0% |
| 11 | 11 | 2.8% | 14.70 | 12 | 0 | 0 | 0.33% | 6.0% |

**0c3 8e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 10 | 11% | 13.83 | 10 | 0.39% | 3.6% | 11% | 31% |
| 10 | 11 | 44% | 13.95 | 11 | 0 | 0.79% | 8.5% | 32% |
| 11 | 11 | 44% | 14.41 | 12 | 0 | 0 | 1.4% | 16% |

**2c3 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 25% | 13.10 | 9 | 0.42% | 3.6% | 20% | 67% |
| 9 | 10 | 50% | 13.34 | 10 | 0.11% | 1.5% | 12% | 55% |
| 10 | 10 | 25% | 13.78 | 11 | 0 | 0.34% | 4.2% | 31% |

**2c3 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 5 | 0.39% | 11.97 | 5 | 9.1% | 27% | 66% | 97% |
| 5 | 6 | 4.3% | 12.08 | 6 | 6.8% | 24% | 63% | 96% |
| 5 | 7 | 7.0% | 12.19 | 7 | 5.3% | 20% | 59% | 96% |
| 5 | 8 | 0.39% | 12.11 | 8 | 5.7% | 23% | 62% | 97% |
| 6 | 6 | 12% | 12.40 | 6 | 3.4% | 15% | 49% | 92% |
| 6 | 7 | 39% | 12.56 | 7 | 2.3% | 11% | 42% | 88% |
| 6 | 8 | 2.1% | 12.47 | 8 | 2.5% | 13% | 46% | 91% |
| 7 | 7 | 32% | 12.76 | 7 | 1.3% | 7.6% | 33% | 82% |
| 7 | 8 | 3.5% | 12.64 | 9 | 1.5% | 8.9% | 38% | 87% |
| 8 | 8 | 0.10% | 12.61 | 10 | 1.9% | 11% | 40% | 86% |

**2c3 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 5 | 0.08% | 12.14 | 5 | 9.2% | 22% | 56% | 93% |
| 5 | 6 | 0.77% | 12.16 | 6 | 6.9% | 22% | 57% | 95% |
| 5 | 7 | 2.1% | 12.32 | 7 | 4.9% | 18% | 52% | 92% |
| 5 | 8 | 2.2% | 12.39 | 8 | 4.3% | 16% | 49% | 91% |
| 5 | 9 | 0.31% | 12.61 | 9 | 2.2% | 11% | 40% | 86% |
| 6 | 6 | 1.9% | 12.35 | 6 | 5.0% | 17% | 50% | 91% |
| 6 | 7 | 10% | 12.59 | 7 | 2.7% | 12% | 40% | 86% |
| 6 | 8 | 11% | 12.71 | 8 | 1.9% | 9.5% | 36% | 82% |
| 6 | 9 | 1.5% | 12.96 | 9 | 0.58% | 4.8% | 25% | 74% |
| 7 | 7 | 14% | 12.89 | 7 | 1.1% | 6.3% | 28% | 76% |
| 7 | 8 | 30% | 13.03 | 8 | 0.61% | 4.4% | 22% | 70% |
| 7 | 9 | 4.2% | 13.27 | 9 | 0.19% | 2.0% | 14% | 58% |
| 8 | 8 | 16% | 13.21 | 8 | 0.25% | 2.5% | 16% | 62% |
| 8 | 9 | 4.5% | 13.45 | 9 | 0.11% | 1.1% | 9.2% | 48% |
| 9 | 9 | 0.31% | 13.73 | 10 | 0.03% | 0.61% | 5.2% | 31% |

**2c3 6e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 7 | 3.5% | 12.82 | 7 | 1.6% | 7.8% | 31% | 78% |
| 7 | 8 | 21% | 13.00 | 8 | 0.84% | 5.1% | 24% | 71% |
| 7 | 9 | 10% | 13.06 | 9 | 0.57% | 3.9% | 21% | 69% |
| 8 | 8 | 30% | 13.25 | 8 | 0.40% | 2.8% | 16% | 58% |
| 8 | 9 | 29% | 13.33 | 9 | 0.19% | 2.0% | 13% | 55% |
| 9 | 9 | 7.1% | 13.42 | 9 | 0.09% | 1.1% | 10% | 50% |

**2c3 8e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 25% | 13.23 | 9 | 0.31% | 2.6% | 16% | 61% |
| 9 | 10 | 50% | 13.47 | 10 | 0.10% | 1.2% | 9.6% | 47% |
| 10 | 10 | 25% | 13.91 | 11 | 0 | 0.29% | 3.3% | 25% |

**4c3 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 8 | 11% | 12.87 | 8 | 1.4% | 7.5% | 30% | 75% |
| 8 | 9 | 36% | 13.06 | 9 | 0.90% | 5.1% | 23% | 66% |
| 8 | 10 | 8.3% | 13.61 | 10 | 0.16% | 1.5% | 8.7% | 38% |
| 9 | 9 | 28% | 13.40 | 10 | 0.28% | 2.5% | 14% | 50% |
| 9 | 10 | 17% | 13.85 | 11 | 0 | 0.43% | 4.8% | 28% |

**4c3 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 7 | 0.35% | 12.68 | 7 | 3.7% | 12% | 37% | 78% |
| 7 | 8 | 3.2% | 12.90 | 8 | 2.1% | 7.9% | 28% | 72% |
| 7 | 9 | 7.1% | 12.99 | 9 | 1.2% | 6.0% | 25% | 70% |
| 7 | 10 | 1.5% | 13.11 | 10 | 0.74% | 5.1% | 22% | 65% |
| 8 | 8 | 7.4% | 13.23 | 8 | 0.87% | 4.1% | 18% | 57% |
| 8 | 9 | 32% | 13.38 | 9 | 0.27% | 2.3% | 13% | 51% |
| 8 | 10 | 6.6% | 13.58 | 10 | 0.04% | 1.2% | 9.4% | 42% |
| 9 | 9 | 29% | 13.62 | 9 | 0.08% | 1.0% | 8.0% | 39% |
| 9 | 10 | 12% | 13.95 | 10 | <0.01% | 0.25% | 3.3% | 24% |
| 10 | 10 | 1.3% | 14.28 | 12 | 0 | 0 | 0.35% | 9.6% |

**4c3 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 7 | 0.21% | 12.22 | 7 | 6.7% | 22% | 55% | 92% |
| 7 | 8 | 1.7% | 12.54 | 8 | 3.4% | 14% | 43% | 85% |
| 7 | 9 | 3.8% | 12.82 | 9 | 1.7% | 7.6% | 31% | 78% |
| 7 | 10 | 3.2% | 13.04 | 10 | 0.60% | 4.8% | 22% | 69% |
| 7 | 11 | 0.21% | 13.31 | 11 | 0 | 1.7% | 14% | 57% |
| 8 | 8 | 3.4% | 12.86 | 8 | 2.0% | 8.1% | 30% | 75% |
| 8 | 9 | 15% | 13.14 | 9 | 0.60% | 4.1% | 20% | 63% |
| 8 | 10 | 12% | 13.38 | 10 | 0.11% | 1.8% | 13% | 52% |
| 8 | 11 | 0.96% | 13.70 | 11 | 0 | 0.29% | 4.6% | 34% |
| 9 | 9 | 17% | 13.45 | 9 | 0.15% | 1.6% | 11% | 48% |
| 9 | 10 | 27% | 13.73 | 10 | 0.02% | 0.51% | 5.6% | 34% |
| 9 | 11 | 2.4% | 14.09 | 11 | 0 | 0.09% | 1.8% | 16% |
| 10 | 10 | 11% | 14.08 | 11 | 0 | 0.11% | 2.1% | 18% |
| 10 | 11 | 2.3% | 14.37 | 12 | 0 | 0 | 0.34% | 8.2% |

**0c4 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 100% | 13.22 | 9 | 0.36% | 3.1% | 17% | 61% |

**0c4 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 25% | 13.51 | 9 | 0.17% | 1.4% | 9.1% | 44% |
| 9 | 10 | 50% | 13.50 | 10 | 0.11% | 1.2% | 9.3% | 45% |
| 10 | 10 | 25% | 13.57 | 10 | 0.08% | 1.0% | 7.9% | 41% |

**0c4 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 37% | 13.61 | 9 | 0.13% | 1.1% | 7.6% | 39% |
| 9 | 10 | 48% | 13.64 | 10 | 0.08% | 0.82% | 6.9% | 37% |
| 10 | 10 | 15% | 13.70 | 11 | 0 | 0.60% | 5.3% | 34% |

**0c4 6e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 10 | 100% | 13.90 | 10 | 0.02% | 0.36% | 3.6% | 24% |

**0c4 8e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 11 | 11 | 100% | 14.18 | 11 | 0 | 0.11% | 1.9% | 16% |

**2c4 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 7 | 11% | 12.63 | 7 | 2.5% | 11% | 39% | 84% |
| 7 | 8 | 28% | 12.92 | 8 | 1.4% | 6.9% | 28% | 73% |
| 7 | 9 | 17% | 13.16 | 9 | 0.63% | 3.8% | 19% | 62% |
| 8 | 8 | 17% | 13.30 | 9 | 0.62% | 3.4% | 16% | 54% |
| 8 | 9 | 21% | 13.60 | 10 | 0.14% | 1.5% | 9.0% | 39% |
| 9 | 9 | 6.2% | 14.22 | 11 | 0 | 0.20% | 2.1% | 16% |

**2c4 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 7 | 0.17% | 12.29 | 7 | 5.2% | 18% | 53% | 93% |
| 7 | 8 | 2.6% | 12.66 | 8 | 2.2% | 9.9% | 37% | 84% |
| 7 | 9 | 4.0% | 12.99 | 9 | 0.76% | 4.9% | 24% | 72% |
| 7 | 10 | 1.4% | 13.13 | 10 | 0.33% | 3.2% | 18% | 66% |
| 8 | 8 | 9.8% | 13.04 | 8 | 0.86% | 5.1% | 23% | 68% |
| 8 | 9 | 30% | 13.36 | 9 | 0.33% | 2.4% | 14% | 52% |
| 8 | 10 | 10% | 13.54 | 10 | 0.09% | 1.3% | 9.0% | 42% |
| 9 | 9 | 23% | 13.75 | 10 | 0.06% | 0.82% | 6.3% | 33% |
| 9 | 10 | 16% | 14.01 | 10 | <0.01% | 0.20% | 3.0% | 21% |
| 10 | 10 | 2.8% | 14.37 | 10 | <0.01% | 0.02% | 0.70% | 10% |

**2c4 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 7 | 0.42% | 12.67 | 7 | 3.0% | 11% | 36% | 83% |
| 7 | 8 | 3.3% | 12.94 | 8 | 1.4% | 6.7% | 27% | 72% |
| 7 | 9 | 6.0% | 13.12 | 9 | 0.75% | 4.3% | 20% | 64% |
| 7 | 10 | 2.7% | 13.24 | 10 | 0.37% | 2.8% | 16% | 59% |
| 7 | 11 | 0.12% | 13.39 | 11 | 0 | 2.0% | 13% | 51% |
| 8 | 8 | 6.5% | 13.29 | 8 | 0.59% | 3.4% | 17% | 56% |
| 8 | 9 | 24% | 13.51 | 9 | 0.24% | 1.9% | 11% | 45% |
| 8 | 10 | 11% | 13.68 | 10 | 0.06% | 0.97% | 7.4% | 36% |
| 8 | 11 | 0.47% | 13.78 | 11 | 0 | 0.64% | 5.8% | 32% |
| 9 | 9 | 21% | 13.79 | 9 | 0.05% | 0.74% | 6.0% | 31% |
| 9 | 10 | 19% | 14.01 | 10 | <0.01% | 0.20% | 2.9% | 21% |
| 9 | 11 | 0.86% | 14.10 | 11 | 0 | 0.03% | 1.9% | 17% |
| 10 | 10 | 4.3% | 14.32 | 10 | <0.01% | 0.04% | 0.89% | 11% |
| 10 | 11 | 0.39% | 14.36 | 11 | 0 | 0.02% | 0.36% | 7.6% |
| 11 | 11 | <0.01% | 14.42 | 12 | 0 | 0 | 0.91% | 7.2% |

**2c4 6e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 8 | 4.3% | 12.98 | 8 | 0.84% | 5.3% | 25% | 72% |
| 8 | 9 | 22% | 13.35 | 9 | 0.32% | 2.3% | 14% | 53% |
| 8 | 10 | 11% | 13.54 | 10 | 0.12% | 1.4% | 9.3% | 43% |
| 9 | 9 | 27% | 13.77 | 9 | 0.07% | 0.84% | 6.2% | 32% |
| 9 | 10 | 28% | 14.01 | 10 | <0.01% | 0.26% | 3.2% | 21% |
| 10 | 10 | 7.3% | 14.40 | 11 | 0 | 0.04% | 0.85% | 9.4% |

**2c4 8e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 11% | 13.36 | 9 | 0.32% | 2.3% | 14% | 52% |
| 9 | 10 | 28% | 13.72 | 10 | 0.07% | 0.93% | 6.8% | 34% |
| 9 | 11 | 17% | 13.93 | 11 | 0 | 0.26% | 3.3% | 24% |
| 10 | 10 | 17% | 14.16 | 11 | 0 | 0.15% | 2.5% | 18% |
| 10 | 11 | 21% | 14.43 | 12 | 0 | 0 | 0.63% | 8.3% |
| 11 | 11 | 6.2% | 14.93 | 12 | 0 | 0 | 0.01% | 1.5% |

**4c4 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 10 | 5.6% | 13.98 | 10 | 0.19% | 0.81% | 4.1% | 25% |
| 10 | 11 | 22% | 14.17 | 11 | 0 | 0.38% | 3.0% | 16% |
| 10 | 12 | 11% | 14.58 | 12 | 0 | 0 | 0.68% | 6.4% |
| 10 | 13 | 5.6% | 14.74 | 13 | 0 | 0 | 0 | 5.2% |
| 11 | 11 | 22% | 14.43 | 12 | 0 | 0 | 0.94% | 9.6% |
| 11 | 12 | 22% | 14.82 | 12 | 0 | 0 | 0.23% | 3.2% |
| 11 | 13 | 11% | 15.04 | 13 | 0 | 0 | 0 | 0.81% |

**4c4 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 0.87% | 13.66 | 9 | 0.54% | 1.7% | 9.1% | 36% |
| 9 | 10 | 6.9% | 13.91 | 10 | 0.14% | 1.1% | 5.2% | 25% |
| 9 | 11 | 9.3% | 14.13 | 11 | 0 | 0.31% | 3.1% | 18% |
| 9 | 12 | 0.87% | 14.37 | 12 | 0 | 0 | 1.5% | 12% |
| 10 | 10 | 13% | 14.21 | 10 | <0.01% | 0.24% | 2.3% | 15% |
| 10 | 11 | 38% | 14.46 | 11 | 0 | 0.04% | 0.91% | 8.8% |
| 10 | 12 | 3.8% | 14.73 | 12 | 0 | 0 | 0.25% | 4.3% |
| 11 | 11 | 24% | 14.65 | 11 | 0 | 0.01% | 0.40% | 5.1% |
| 11 | 12 | 3.6% | 14.89 | 12 | 0 | 0 | 0.19% | 3.0% |

**4c4 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 1.2% | 13.76 | 9 | 0.22% | 1.4% | 7.1% | 32% |
| 9 | 10 | 8.6% | 13.92 | 10 | 0.16% | 0.74% | 4.9% | 25% |
| 9 | 11 | 9.7% | 14.15 | 11 | 0 | 0.43% | 2.9% | 17% |
| 9 | 12 | 1.4% | 14.45 | 12 | 0 | 0 | 1.1% | 10% |
| 10 | 10 | 14% | 14.15 | 10 | 0.02% | 0.40% | 2.7% | 17% |
| 10 | 11 | 35% | 14.41 | 11 | 0 | 0.07% | 1.3% | 10% |
| 10 | 12 | 6.5% | 14.71 | 12 | 0 | 0 | 0.31% | 4.9% |
| 11 | 11 | 19% | 14.61 | 11 | 0 | <0.01% | 0.45% | 5.9% |
| 11 | 12 | 5.0% | 14.89 | 12 | 0 | 0 | 0.07% | 2.2% |

**2c5 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 10 | 25% | 14.11 | 10 | 0.03% | 0.33% | 3.2% | 19% |
| 10 | 11 | 50% | 14.37 | 11 | 0 | 0.12% | 1.4% | 11% |
| 11 | 11 | 25% | 14.86 | 12 | 0 | 0 | 0.30% | 3.9% |

**2c5 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 1.6% | 13.38 | 9 | 0.69% | 3.9% | 17% | 50% |
| 9 | 10 | 14% | 13.79 | 10 | 0.08% | 0.88% | 6.2% | 32% |
| 9 | 11 | 7.0% | 14.09 | 11 | 0 | 0.18% | 2.9% | 19% |
| 9 | 12 | 0.78% | 14.28 | 12 | 0 | 0 | 0.99% | 12% |
| 10 | 10 | 32% | 14.12 | 10 | 0.02% | 0.29% | 2.7% | 18% |
| 10 | 11 | 32% | 14.45 | 11 | 0 | 0.03% | 0.85% | 8.7% |
| 10 | 12 | 3.5% | 14.62 | 12 | 0 | 0 | 0.25% | 5.1% |
| 11 | 11 | 7.9% | 15.03 | 12 | 0 | 0 | 0.02% | 2.0% |
| 11 | 12 | 1.8% | 15.23 | 13 | 0 | 0 | 0 | 0.62% |
| 12 | 12 | 0.10% | 15.54 | 13 | 0 | 0 | 0 | 0.84% |

**2c5 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 2.3% | 13.45 | 9 | 0.45% | 3.0% | 13% | 47% |
| 9 | 10 | 15% | 13.78 | 10 | 0.14% | 0.95% | 6.7% | 32% |
| 9 | 11 | 9.8% | 14.08 | 11 | 0 | 0.35% | 3.0% | 19% |
| 9 | 12 | 1.5% | 14.34 | 12 | 0 | 0 | 1.1% | 11% |
| 10 | 10 | 23% | 14.13 | 10 | 0.01% | 0.31% | 2.7% | 18% |
| 10 | 11 | 31% | 14.45 | 11 | 0 | 0.04% | 1.0% | 9.2% |
| 10 | 12 | 4.7% | 14.67 | 12 | 0 | 0 | 0.23% | 4.5% |
| 11 | 11 | 10% | 14.93 | 12 | 0 | 0 | 0.08% | 2.8% |
| 11 | 12 | 3.1% | 15.23 | 13 | 0 | 0 | 0 | 0.57% |
| 12 | 12 | 0.24% | 15.60 | 13 | 0 | 0 | 0 | 0.04% |

**2c5 6e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 0.39% | 13.88 | 9 | 0.23% | 1.5% | 5.4% | 27% |
| 9 | 10 | 6.2% | 13.93 | 10 | 0.10% | 0.73% | 4.8% | 25% |
| 9 | 11 | 3.1% | 14.18 | 11 | 0 | 0.37% | 2.5% | 16% |
| 9 | 12 | 2.3% | 14.44 | 12 | 0 | 0 | 0.93% | 9.2% |
| 10 | 10 | 25% | 14.08 | 10 | 0.03% | 0.36% | 3.1% | 20% |
| 10 | 11 | 25% | 14.35 | 11 | 0 | 0.10% | 1.4% | 11% |
| 10 | 12 | 19% | 14.60 | 12 | 0 | 0 | 0.39% | 5.6% |
| 11 | 11 | 6.2% | 14.67 | 12 | 0 | 0 | 0.38% | 5.3% |
| 11 | 12 | 9.4% | 14.98 | 13 | 0 | 0 | 0 | 1.5% |
| 12 | 12 | 3.5% | 15.47 | 13 | 0 | 0 | 0 | 0.11% |

**2c5 8e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 10 | 25% | 14.09 | 10 | 0.05% | 0.35% | 3.6% | 20% |
| 10 | 11 | 25% | 14.26 | 11 | 0 | 0.21% | 1.7% | 14% |
| 10 | 12 | 25% | 14.54 | 12 | 0 | 0 | 0.65% | 6.9% |
| 11 | 11 | 6.2% | 14.57 | 12 | 0 | 0 | 0.77% | 6.3% |
| 11 | 12 | 12% | 14.87 | 13 | 0 | 0 | 0 | 2.4% |
| 12 | 12 | 6.2% | 15.52 | 13 | 0 | 0 | 0 | 0.03% |

**4b5 0e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 44% | 14.23 | 9 | 0.03% | 0.32% | 2.6% | 15% |
| 9 | 10 | 44% | 14.33 | 10 | 0.02% | 0.16% | 1.6% | 12% |
| 10 | 10 | 11% | 14.51 | 11 | 0 | 0.06% | 0.77% | 7.5% |

**4b5 2e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 6.2% | 14.12 | 9 | 0.09% | 0.49% | 3.6% | 19% |
| 9 | 10 | 36% | 14.20 | 10 | 0.04% | 0.36% | 2.6% | 16% |
| 9 | 11 | 1.0% | 14.32 | 11 | 0 | 0.09% | 1.5% | 12% |
| 10 | 10 | 53% | 14.31 | 10 | <0.01% | 0.12% | 1.6% | 12% |
| 10 | 11 | 3.0% | 14.43 | 11 | 0 | 0.04% | 0.74% | 8.7% |
| 11 | 11 | 0.04% | 14.68 | 12 | 0 | 0 | 0.32% | 5.0% |

**4b5 4e**

| Shorter side | Longer side | Share of subset | Avg optimal | Fastest | In 10 | In 11 | In 12 | In 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 0.86% | 13.96 | 9 | 0.27% | 1.5% | 6.3% | 26% |
| 9 | 10 | 9.8% | 14.06 | 10 | 0.07% | 0.57% | 4.0% | 21% |
| 9 | 11 | 7.0% | 14.22 | 11 | 0 | 0.21% | 2.2% | 16% |
| 10 | 10 | 28% | 14.20 | 10 | 0.02% | 0.25% | 2.4% | 16% |
| 10 | 11 | 40% | 14.35 | 11 | 0 | 0.08% | 1.3% | 11% |
| 11 | 11 | 14% | 14.52 | 12 | 0 | 0 | 0.43% | 6.7% |

---

## Appendix G: a scramble for every subset

For each of the 48 subsets: a state with the longest optimal finish in the subset, and a state that finishes in exactly its longer HTR (so the HTR length is all the bound you get from HTR lengths, in every subset). Do the scramble on a solved cube.

| Subset | A longest one | Its optimal | One that finishes in exactly its longer HTR | HTR normal / inverse = optimal |
|---|---|---:|---|---:|
| 0c0 0e | `U2 L2 F2 R2 U2 F2 U2 B2 L2 F2 U2 R2 U2` | 13 | `D U'` | 2 / 2 = 2 |
| 0c0 2e | `L2 D F2 R2 B2 D L2 U F2 U2 R2 B2 D2 L2 U'` | 15 | `L2 D' B2 L2 B2 D` | 5 / 6 = 6 |
| 0c0 4e | `R2 U' F2 D2 F2 L2 B2 L2 U2 L2 U L2 R2 F2 D U'` | 16 | `D' B2 F2 U F2 L2 D2` | 7 / 4 = 7 |
| 0c0 6e | `B2 U F2 R2 B2 L2 R2 D' L2 R2 B2 D' U' R2 D' U'` | 16 | `L2 D B2 F2 R2 F2 L2 D'` | 7 / 8 = 8 |
| 0c0 8e | `F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'` | 18 | `U' B2 F2 L2 R2 U'` | 6 / 6 = 6 |
| 4a1 0e | `R2 F2 U F2 U2 L2 U2 R2 U2 F2 U L2 R2 F2 R2 U'` | 16 | `D F2 D' F2 U' R2 D' R2 D B2` | 10 / 9 = 10 |
| 4a1 2e | `L2 B2 F2 D F2 R2 F2 D' R2 D' F2 L2 D2 R2 D' U'` | 16 | `D R2 B2 D' R2 B2 R2 D` | 8 / 7 = 8 |
| 4a1 4e | `R2 U2 B2 L2 F2 L2 D2 F2 R2 U' B2 F2 L2 R2 U' R2 D'` | 17 | `D2 F2 L2 B2 L2 F2 R2 D'` | 1 / 8 = 8 |
| 4a2 0e | `B2 D2 L2 B2 F2 D F2 D2 L2 U' R2 B2 U' B2 F2 U' R2` | 17 | `D' B2 U2 R2 U' B2 D B2 D2 R2 U' B2` | 12 / 10 = 12 |
| 4a2 2e | `D' F2 D' R2 U L2 U' B2 L2 D L2 F2 U L2 U' R2 U'` | 17 | `D' L2 B2 L2 F2 U2 R2 U F2 D2 L2` | 11 / 8 = 11 |
| 4a2 4e | `B2 R2 B2 R2 D2 B2 U' B2 L2 D2 L2 U R2 U2 F2 U2` | 16 | `D B2 D L2 D F2 U F2 U' L2 U` | 11 / 9 = 11 |
| 4b2 0e | `F2 U2 R2 D F2 R2 D B2 U2 L2 D' R2 B2 F2 R2 U'` | 16 | `D' R2 U' F2 U2 L2 U' R2 D` | 9 / 9 = 9 |
| 4b2 2e | `U2 L2 D F2 U2 L2 F2 U B2 U' L2 B2 U' L2 D' U'` | 16 | `D F2 U F2 D2 B2 L2 D2` | 8 / 3 = 8 |
| 4b2 4e | `F2 D2 B2 R2 U' F2 R2 B2 R2 U' F2 L2 D2 R2 D U'` | 16 | `L2 U' B2 D B2 U F2 L2 D` | 7 / 9 = 9 |
| 0c3 0e | `R2 D2 R2 D' L2 D L2 D' L2 B2 U' R2 U F2 U' R2 U'` | 17 | `R2 D B2 R2 D2 R2 U' B2 U2 R2 U'` | 10 / 11 = 11 |
| 0c3 2e | `B2 F2 L2 U' B2 D' B2 D2 F2 R2 D' F2 D' L2 U2 B2 U'` | 17 | `B2 F2 U' F2 U2 R2 D R2 U2 B2 D'` | 9 / 11 = 11 |
| 0c3 4e | `F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'` | 18 | `U' F2 U F2 U' R2 D L2 U' L2 U R2 U` | 12 / 13 = 13 |
| 0c3 6e | `R2 D B2 U L2 F2 U' L2 U F2 D' B2 U F2 U2 L2 U'` | 17 | `B2 F2 U' R2 U2 F2 U B2 U2 L2 U` | 9 / 11 = 11 |
| 0c3 8e | `B2 L2 F2 L2 D R2 F2 U2 F2 D' B2 R2 U2 R2 U' R2 U2` | 17 | `L2 U' B2 R2 D2 R2 D' L2 U2 B2 U'` | 10 / 11 = 11 |
| 2c3 0e | `U' B2 U L2 U F2 L2 D' R2 D' L2 U2 B2 U' R2 U'` | 16 | `D L2 F2 D' L2 B2 D2 R2 U' B2` | 10 / 9 = 10 |
| 2c3 2e | `B2 U2 R2 D F2 D2 B2 L2 D L2 D' R2 D' B2 U'` | 15 | `D' F2 U' F2 D2 B2 D' B2` | 8 / 5 = 8 |
| 2c3 4e | `R2 U L2 D F2 L2 B2 D2 B2 U' B2 U' R2 F2 R2 U'` | 16 | `D B2 D' F2 U' B2 F2 D2 B2` | 9 / 5 = 9 |
| 2c3 6e | `L2 U L2 F2 U' R2 B2 U2 L2 U' L2 R2 B2 D R2 U'` | 16 | `D F2 D' R2 D2 B2 F2 U' B2` | 9 / 7 = 9 |
| 2c3 8e | `R2 U R2 D' L2 F2 D B2 L2 U2 B2 U' B2 F2 R2 U'` | 16 | `D F2 U' B2 U B2 D B2 F2 U'` | 10 / 9 = 10 |
| 4c3 0e | `R2 F2 L2 R2 D' B2 U L2 D' B2 U R2 B2 D2 L2 U'` | 16 | `D2 L2 D' F2 U2 R2 D' F2 L2 U'` | 8 / 10 = 10 |
| 4c3 2e | `B2 U R2 B2 D' L2 D2 L2 F2 D L2 F2 L2 B2 D' U'` | 16 | `D' R2 D2 B2 D B2 D R2 D2 B2` | 10 / 7 = 10 |
| 4c3 4e | `L2 D2 U' R2 U B2 L2 B2 R2 U2 B2 U' B2 U R2 U'` | 16 | `D' R2 D' F2 U' F2 U R2 U L2 U2` | 11 / 9 = 11 |
| 0c4 0e | `F2 L2 B2 L2 D' B2 R2 D' L2 U2 F2 U' F2 R2 D2 U'` | 16 | `U' L2 U L2 D2 B2 U B2 U'` | 9 / 9 = 9 |
| 0c4 2e | `R2 B2 R2 F2 R2 U B2 D R2 U2 L2 B2 D' F2 D2 U'` | 16 | `B2 D L2 D' L2 D2 B2 D' L2 D` | 9 / 10 = 10 |
| 0c4 4e | `L2 R2 B2 L2 R2 D F2 U R2 D2 B2 D F2 L2 D2 U'` | 16 | `D' R2 U B2 D2 L2 U R2 U' F2` | 10 / 9 = 10 |
| 0c4 6e | `F2 D B2 D L2 U2 L2 F2 L2 R2 U' B2 L2 R2 D2 U'` | 16 | `D' R2 U' R2 F2 U2 F2 U B2 U'` | 10 / 10 = 10 |
| 0c4 8e | `F2 U F2 R2 D' F2 U2 R2 U B2 F2 L2 U2 F2 L2 U'` | 16 | `U' R2 D F2 L2 U2 F2 R2 U B2 U'` | 11 / 11 = 11 |
| 2c4 0e | `U2 L2 D' R2 B2 D F2 D' B2 R2 U F2 L2 R2 D' U'` | 16 | `D2 B2 U F2 U' B2 U F2 U'` | 7 / 9 = 9 |
| 2c4 2e | `D R2 U' R2 U L2 D' L2 B2 U R2 F2 U F2 U' R2 U'` | 17 | `D B2 D L2 R2 D2 F2 U R2 U'` | 10 / 10 = 10 |
| 2c4 4e | `B2 D B2 R2 D B2 R2 D2 R2 U F2 D' F2 D' F2 U'` | 16 | `D2 R2 D F2 D' L2 U F2 U2 R2 D'` | 7 / 11 = 11 |
| 2c4 6e | `L2 D B2 D' R2 U B2 U F2 U R2 U' R2 U B2 R2 U'` | 17 | `L2 U' F2 D L2 F2 D L2 F2 U` | 8 / 10 = 10 |
| 2c4 8e | `R2 D L2 D' L2 U' F2 U2 R2 U B2 R2 U L2 F2 R2 U'` | 17 | `D2 B2 D B2 F2 R2 U' R2 D F2 U'` | 9 / 11 = 11 |
| 4c4 0e | `F2 U' B2 L2 D2 R2 U' B2 U' B2 F2 U' F2 U B2 R2 U'` | 17 | `B2 U2 L2 U B2 D' B2 L2 U2 R2 D' R2 U'` | 10 / 13 = 13 |
| 4c4 2e | `U B2 D' F2 D L2 U' R2 F2 D' B2 U B2 L2 U R2 U'` | 17 | `U' R2 U' L2 D B2 U' B2 D R2 U' L2` | 12 / 10 = 12 |
| 4c4 4e | `B2 D' F2 U B2 U' R2 D B2 D F2 R2 D L2 U R2 U'` | 17 | `D' R2 D R2 U' B2 D R2 U' R2 U B2` | 12 / 10 = 12 |
| 2c5 0e | `U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'` | 18 | `U F2 U' R2 B2 U' L2 U B2 U' R2` | 11 / 10 = 11 |
| 2c5 2e | `F2 L2 U2 L2 D' F2 U' L2 U2 B2 L2 R2 U B2 U' R2 U'` | 17 | `D B2 D R2 U2 B2 D' R2 U B2 D' R2` | 12 / 10 = 12 |
| 2c5 4e | `R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'` | 18 | `D' F2 U' R2 D B2 D' F2 D L2 D2 B2` | 12 / 9 = 12 |
| 2c5 6e | `B2 U' L2 D F2 U' L2 U2 B2 F2 U' F2 R2 D2 L2 R2 U'` | 17 | `D B2 D' F2 D F2 D' B2 U' L2 D2 L2` | 12 / 9 = 12 |
| 2c5 8e | `U' B2 D' L2 B2 D R2 D2 F2 D' R2 D B2 R2 U2 R2 U2` | 17 | `U B2 U' L2 D B2 L2 D B2 D' L2 D2` | 12 / 10 = 12 |
| 4b5 0e | `U B2 U' R2 U2 B2 R2 B2 U B2 L2 U' F2 U R2 D' U'` | 17 | `D F2 D F2 U' L2 D L2 D B2` | 10 / 9 = 10 |
| 4b5 2e | `D' L2 R2 B2 U B2 D' L2 B2 F2 U B2 L2 R2 D2 U'` | 16 | `D F2 U' L2 U B2 U' F2 D' R2 B2` | 11 / 9 = 11 |
| 4b5 4e | `R2 F2 U' L2 U L2 B2 F2 U2 B2 D' F2 R2 D F2 R2 U'` | 17 | `D' L2 B2 D' F2 D R2 D' F2 L2 U` | 9 / 11 = 11 |

---

## Appendix H: every read at every target

For each corner-qt group and each finish you might need, what each read is worth. "How you get it": look (count or see it), recognise (know the corner case on normal and on inverse), solve (find the shortest HTR on both sides, or the optimal corner solutions).

- **Best 10% / 25% / 50% keeps**: rank the group's DRs by the read, keep that share of them, and this is the share of the finishes in T you still have.
- **Drop, keeping 90% / 95% / 99%**: the share of the group's DRs you can drop while keeping that share of the finishes in T.
- **In classes under 1%**: the share of the group's DRs that the read puts in a class where at most one in a hundred finishes in T. The last column is the share of the finishes in T those classes hold.

Every number is the best any rule based on that read could do.

**1–2qt (4a1, 4a2, 4b2)**

| Finish needed | What you know | How you get it | Best 10% keeps | Best 25% keeps | Best 50% keeps | Drop, keeping 90% | Drop, keeping 95% | Drop, keeping 99% | In classes under 1% | Finishes lost by dropping those |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **9 or less** (0.51% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 100% | 100% |
| 9 or less | subset | look | 31% | 48% | 73% | 24% | 16% | 10% | 91% | 71% |
| 9 or less | + true pairs | look | 48% | 71% | 89% | 48% | 34% | 16% | 87% | 45% |
| 9 or less | + corner case on both sides | recognise | 34% | 59% | 84% | 41% | 31% | 18% | 87% | 60% |
| 9 or less | + pairs and corner cases | recognise | 54% | 77% | 94% | 58% | 46% | 27% | 87% | 40% |
| 9 or less | + HTR length on both sides | solve | 68% | 87% | 96% | 69% | 55% | 31% | 91% | 33% |
| 9 or less | + corner length L and E-parity | solve | 34% | 62% | 85% | 42% | 32% | 19% | 84% | 53% |
| 9 or less | + pairs and HTR | solve | 74% | 91% | 98% | 76% | 66% | 45% | 89% | 25% |
| 9 or less | + pairs, corner cases and HTR | solve | 76% | 93% | 99% | 80% | 71% | 54% | 89% | 23% |
| 9 or less | + pairs, HTR, L and E-parity | solve | 80% | 95% | 100% | 82% | 75% | 61% | 90% | 20% |
| **10 or less** (2.4% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 10 or less | subset | look | 25% | 42% | 68% | 21% | 14% | 9% | 9% | 1% |
| 10 or less | + true pairs | look | 35% | 60% | 82% | 35% | 23% | 10% | 34% | 9% |
| 10 or less | + corner case on both sides | recognise | 27% | 50% | 78% | 33% | 23% | 12% | 22% | 4% |
| 10 or less | + pairs and corner cases | recognise | 39% | 64% | 86% | 43% | 32% | 17% | 37% | 7% |
| 10 or less | + HTR length on both sides | solve | 50% | 72% | 90% | 50% | 37% | 20% | 51% | 10% |
| 10 or less | + corner length L and E-parity | solve | 28% | 52% | 78% | 32% | 23% | 13% | 21% | 4% |
| 10 or less | + pairs and HTR | solve | 54% | 77% | 93% | 57% | 45% | 25% | 52% | 8% |
| 10 or less | + pairs, corner cases and HTR | solve | 56% | 79% | 94% | 60% | 48% | 29% | 54% | 7% |
| 10 or less | + pairs, HTR, L and E-parity | solve | 57% | 81% | 95% | 62% | 51% | 33% | 56% | 7% |
| **11 or less** (10% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 11 or less | subset | look | 19% | 36% | 63% | 20% | 13% | 6% | 0% | 0% |
| 11 or less | + true pairs | look | 26% | 49% | 74% | 27% | 17% | 7% | 3% | 0% |
| 11 or less | + corner case on both sides | recognise | 20% | 42% | 71% | 26% | 18% | 9% | 5% | 0% |
| 11 or less | + pairs and corner cases | recognise | 28% | 52% | 78% | 32% | 23% | 11% | 6% | 0% |
| 11 or less | + HTR length on both sides | solve | 34% | 57% | 80% | 35% | 25% | 13% | 8% | 0% |
| 11 or less | + corner length L and E-parity | solve | 21% | 44% | 71% | 26% | 18% | 9% | 6% | 0% |
| 11 or less | + pairs and HTR | solve | 36% | 61% | 84% | 40% | 29% | 14% | 10% | 0% |
| 11 or less | + pairs, corner cases and HTR | solve | 37% | 62% | 85% | 42% | 30% | 16% | 10% | 0% |
| 11 or less | + pairs, HTR, L and E-parity | solve | 38% | 63% | 86% | 43% | 32% | 17% | 12% | 0% |
| **12 or less** (35% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 12 or less | subset | look | 15% | 32% | 59% | 18% | 12% | 4% | 0% | 0% |
| 12 or less | + true pairs | look | 18% | 39% | 66% | 20% | 13% | 5% | 0% | 0% |
| 12 or less | + corner case on both sides | recognise | 15% | 35% | 64% | 21% | 14% | 7% | 1% | 0% |
| 12 or less | + pairs and corner cases | recognise | 19% | 40% | 68% | 24% | 16% | 7% | 2% | 0% |
| 12 or less | + HTR length on both sides | solve | 21% | 42% | 69% | 25% | 17% | 8% | 1% | 0% |
| 12 or less | + corner length L and E-parity | solve | 16% | 36% | 64% | 21% | 14% | 7% | 1% | 0% |
| 12 or less | + pairs and HTR | solve | 21% | 44% | 72% | 27% | 18% | 8% | 2% | 0% |
| 12 or less | + pairs, corner cases and HTR | solve | 22% | 45% | 73% | 28% | 19% | 9% | 3% | 0% |
| 12 or less | + pairs, HTR, L and E-parity | solve | 22% | 45% | 74% | 29% | 20% | 9% | 3% | 0% |
| **13 or less** (79% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 13 or less | subset | look | 12% | 28% | 55% | 16% | 9% | 2% | 0% | 0% |
| 13 or less | + true pairs | look | 12% | 30% | 57% | 16% | 9% | 3% | 0% | 0% |
| 13 or less | + corner case on both sides | recognise | 12% | 29% | 56% | 16% | 11% | 4% | 0% | 0% |
| 13 or less | + pairs and corner cases | recognise | 12% | 30% | 57% | 17% | 11% | 4% | 0% | 0% |
| 13 or less | + HTR length on both sides | solve | 12% | 30% | 58% | 17% | 11% | 4% | 0% | 0% |
| 13 or less | + corner length L and E-parity | solve | 12% | 29% | 56% | 16% | 11% | 4% | 0% | 0% |
| 13 or less | + pairs and HTR | solve | 13% | 30% | 58% | 18% | 11% | 4% | 0% | 0% |
| 13 or less | + pairs, corner cases and HTR | solve | 13% | 31% | 59% | 18% | 12% | 5% | 0% | 0% |
| 13 or less | + pairs, HTR, L and E-parity | solve | 13% | 31% | 59% | 18% | 12% | 5% | 0% | 0% |

**3qt (2c3, 4c3, 0c3)**

| Finish needed | What you know | How you get it | Best 10% keeps | Best 25% keeps | Best 50% keeps | Drop, keeping 90% | Drop, keeping 95% | Drop, keeping 99% | In classes under 1% | Finishes lost by dropping those |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **9 or less** (0.14% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 100% | 100% |
| 9 or less | subset | look | 32% | 59% | 86% | 38% | 22% | 9% | 100% | 100% |
| 9 or less | + true pairs | look | 57% | 79% | 94% | 60% | 45% | 25% | 97% | 68% |
| 9 or less | + corner case on both sides | recognise | 42% | 70% | 91% | 52% | 42% | 28% | 99% | 94% |
| 9 or less | + pairs and corner cases | recognise | 63% | 85% | 97% | 68% | 57% | 38% | 97% | 66% |
| 9 or less | + HTR length on both sides | solve | 58% | 85% | 98% | 70% | 61% | 44% | 97% | 71% |
| 9 or less | + corner length L and E-parity | solve | 44% | 72% | 96% | 59% | 52% | 40% | 99% | 89% |
| 9 or less | + pairs and HTR | solve | 71% | 91% | 99% | 76% | 68% | 51% | 97% | 57% |
| 9 or less | + pairs, corner cases and HTR | solve | 74% | 93% | 100% | 79% | 72% | 58% | 97% | 54% |
| 9 or less | + pairs, HTR, L and E-parity | solve | 80% | 98% | 100% | 84% | 79% | 71% | 96% | 45% |
| **10 or less** (0.87% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 100% | 100% |
| 10 or less | subset | look | 29% | 54% | 81% | 30% | 18% | 8% | 60% | 24% |
| 10 or less | + true pairs | look | 44% | 68% | 88% | 45% | 31% | 14% | 77% | 34% |
| 10 or less | + corner case on both sides | recognise | 36% | 63% | 87% | 44% | 34% | 18% | 73% | 34% |
| 10 or less | + pairs and corner cases | recognise | 49% | 74% | 92% | 54% | 42% | 24% | 74% | 25% |
| 10 or less | + HTR length on both sides | solve | 43% | 73% | 93% | 55% | 44% | 26% | 71% | 22% |
| 10 or less | + corner length L and E-parity | solve | 36% | 63% | 88% | 47% | 37% | 23% | 68% | 28% |
| 10 or less | + pairs and HTR | solve | 52% | 78% | 95% | 61% | 50% | 31% | 75% | 22% |
| 10 or less | + pairs, corner cases and HTR | solve | 55% | 81% | 96% | 64% | 53% | 36% | 77% | 21% |
| 10 or less | + pairs, HTR, L and E-parity | solve | 57% | 83% | 98% | 67% | 58% | 43% | 77% | 18% |
| **11 or less** (4.6% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 11 or less | subset | look | 25% | 49% | 77% | 25% | 15% | 7% | 5% | 0% |
| 11 or less | + true pairs | look | 33% | 58% | 82% | 35% | 23% | 9% | 11% | 1% |
| 11 or less | + corner case on both sides | recognise | 30% | 56% | 82% | 38% | 28% | 13% | 19% | 2% |
| 11 or less | + pairs and corner cases | recognise | 37% | 63% | 86% | 43% | 31% | 15% | 20% | 2% |
| 11 or less | + HTR length on both sides | solve | 32% | 61% | 86% | 42% | 31% | 17% | 17% | 1% |
| 11 or less | + corner length L and E-parity | solve | 29% | 56% | 82% | 38% | 30% | 16% | 15% | 1% |
| 11 or less | + pairs and HTR | solve | 38% | 65% | 88% | 46% | 35% | 18% | 23% | 2% |
| 11 or less | + pairs, corner cases and HTR | solve | 40% | 67% | 90% | 49% | 38% | 21% | 29% | 2% |
| 11 or less | + pairs, HTR, L and E-parity | solve | 41% | 68% | 91% | 51% | 40% | 25% | 30% | 2% |
| **12 or less** (20% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 12 or less | subset | look | 21% | 43% | 72% | 21% | 13% | 6% | 0% | 0% |
| 12 or less | + true pairs | look | 24% | 48% | 74% | 27% | 17% | 6% | 0% | 0% |
| 12 or less | + corner case on both sides | recognise | 23% | 48% | 76% | 31% | 21% | 8% | 1% | 0% |
| 12 or less | + pairs and corner cases | recognise | 26% | 52% | 79% | 33% | 23% | 9% | 1% | 0% |
| 12 or less | + HTR length on both sides | solve | 24% | 49% | 77% | 32% | 22% | 10% | 3% | 0% |
| 12 or less | + corner length L and E-parity | solve | 23% | 47% | 75% | 30% | 22% | 9% | 3% | 0% |
| 12 or less | + pairs and HTR | solve | 26% | 52% | 79% | 34% | 24% | 11% | 3% | 0% |
| 12 or less | + pairs, corner cases and HTR | solve | 27% | 53% | 81% | 37% | 26% | 13% | 5% | 0% |
| 12 or less | + pairs, HTR, L and E-parity | solve | 27% | 54% | 81% | 37% | 27% | 14% | 6% | 0% |
| **13 or less** (59% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 13 or less | subset | look | 15% | 34% | 63% | 17% | 10% | 5% | 0% | 0% |
| 13 or less | + true pairs | look | 15% | 36% | 64% | 19% | 12% | 5% | 0% | 0% |
| 13 or less | + corner case on both sides | recognise | 15% | 36% | 66% | 22% | 15% | 5% | 0% | 0% |
| 13 or less | + pairs and corner cases | recognise | 16% | 37% | 67% | 23% | 15% | 5% | 0% | 0% |
| 13 or less | + HTR length on both sides | solve | 15% | 36% | 65% | 22% | 14% | 6% | 0% | 0% |
| 13 or less | + corner length L and E-parity | solve | 15% | 36% | 65% | 22% | 14% | 5% | 0% | 0% |
| 13 or less | + pairs and HTR | solve | 16% | 37% | 66% | 23% | 15% | 6% | 0% | 0% |
| 13 or less | + pairs, corner cases and HTR | solve | 16% | 38% | 68% | 25% | 16% | 7% | 1% | 0% |
| 13 or less | + pairs, HTR, L and E-parity | solve | 16% | 38% | 68% | 25% | 17% | 7% | 2% | 0% |

**4qt (2c4, 4c4, 0c4)**

| Finish needed | What you know | How you get it | Best 10% keeps | Best 25% keeps | Best 50% keeps | Drop, keeping 90% | Drop, keeping 95% | Drop, keeping 99% | In classes under 1% | Finishes lost by dropping those |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **9 or less** (0.02% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 100% | 100% |
| 9 or less | subset | look | 26% | 51% | 88% | 47% | 40% | 21% | 100% | 100% |
| 9 or less | + true pairs | look | 71% | 88% | 98% | 71% | 61% | 41% | 100% | 100% |
| 9 or less | + corner case on both sides | recognise | 59% | 89% | 100% | 74% | 68% | 57% | 100% | 100% |
| 9 or less | + pairs and corner cases | recognise | 86% | 99% | 100% | 88% | 83% | 75% | 100% | 91% |
| 9 or less | + HTR length on both sides | solve | 80% | 99% | 100% | 84% | 80% | 75% | 100% | 98% |
| 9 or less | + corner length L and E-parity | solve | 58% | 97% | 100% | 79% | 76% | 73% | 100% | 100% |
| 9 or less | + pairs and HTR | solve | 91% | 100% | 100% | 91% | 87% | 79% | 100% | 83% |
| 9 or less | + pairs, corner cases and HTR | solve | 96% | 100% | 100% | 93% | 91% | 87% | 100% | 79% |
| 9 or less | + pairs, HTR, L and E-parity | solve | 99% | 100% | 100% | 95% | 94% | 91% | 100% | 71% |
| **10 or less** (0.16% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 100% | 100% |
| 10 or less | subset | look | 23% | 47% | 83% | 42% | 36% | 11% | 100% | 100% |
| 10 or less | + true pairs | look | 54% | 76% | 92% | 56% | 44% | 23% | 96% | 65% |
| 10 or less | + corner case on both sides | recognise | 47% | 77% | 96% | 62% | 53% | 40% | 99% | 93% |
| 10 or less | + pairs and corner cases | recognise | 68% | 89% | 99% | 73% | 65% | 51% | 97% | 58% |
| 10 or less | + HTR length on both sides | solve | 57% | 85% | 99% | 70% | 61% | 49% | 98% | 78% |
| 10 or less | + corner length L and E-parity | solve | 44% | 77% | 100% | 64% | 59% | 52% | 100% | 96% |
| 10 or less | + pairs and HTR | solve | 69% | 90% | 99% | 76% | 67% | 53% | 96% | 53% |
| 10 or less | + pairs, corner cases and HTR | solve | 74% | 94% | 100% | 80% | 74% | 64% | 96% | 51% |
| 10 or less | + pairs, HTR, L and E-parity | solve | 76% | 96% | 100% | 82% | 77% | 69% | 96% | 49% |
| **11 or less** (1.1% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 11 or less | subset | look | 20% | 44% | 78% | 38% | 31% | 7% | 35% | 7% |
| 11 or less | + true pairs | look | 40% | 64% | 86% | 44% | 34% | 15% | 61% | 21% |
| 11 or less | + corner case on both sides | recognise | 39% | 67% | 91% | 52% | 42% | 26% | 60% | 16% |
| 11 or less | + pairs and corner cases | recognise | 51% | 77% | 94% | 59% | 48% | 32% | 69% | 17% |
| 11 or less | + HTR length on both sides | solve | 43% | 71% | 92% | 54% | 45% | 27% | 68% | 21% |
| 11 or less | + corner length L and E-parity | solve | 36% | 66% | 92% | 53% | 45% | 31% | 58% | 14% |
| 11 or less | + pairs and HTR | solve | 51% | 77% | 94% | 59% | 48% | 29% | 70% | 18% |
| 11 or less | + pairs, corner cases and HTR | solve | 54% | 80% | 96% | 63% | 54% | 37% | 71% | 16% |
| 11 or less | + pairs, HTR, L and E-parity | solve | 54% | 80% | 97% | 64% | 56% | 43% | 69% | 13% |
| **12 or less** (6.8% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 12 or less | subset | look | 18% | 40% | 73% | 35% | 22% | 5% | 0% | 0% |
| 12 or less | + true pairs | look | 29% | 53% | 80% | 37% | 27% | 9% | 9% | 1% |
| 12 or less | + corner case on both sides | recognise | 32% | 59% | 86% | 43% | 32% | 15% | 13% | 1% |
| 12 or less | + pairs and corner cases | recognise | 38% | 65% | 88% | 47% | 36% | 19% | 20% | 1% |
| 12 or less | + HTR length on both sides | solve | 32% | 60% | 86% | 42% | 31% | 14% | 19% | 2% |
| 12 or less | + corner length L and E-parity | solve | 30% | 57% | 86% | 43% | 33% | 16% | 19% | 1% |
| 12 or less | + pairs and HTR | solve | 36% | 63% | 87% | 45% | 34% | 16% | 19% | 1% |
| 12 or less | + pairs, corner cases and HTR | solve | 40% | 67% | 90% | 49% | 38% | 20% | 22% | 1% |
| 12 or less | + pairs, HTR, L and E-parity | solve | 38% | 66% | 90% | 49% | 39% | 23% | 24% | 1% |
| **13 or less** (30% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 13 or less | subset | look | 15% | 36% | 68% | 27% | 14% | 3% | 0% | 0% |
| 13 or less | + true pairs | look | 20% | 42% | 72% | 29% | 18% | 4% | 0% | 0% |
| 13 or less | + corner case on both sides | recognise | 23% | 48% | 77% | 33% | 22% | 8% | 0% | 0% |
| 13 or less | + pairs and corner cases | recognise | 25% | 51% | 79% | 35% | 24% | 10% | 0% | 0% |
| 13 or less | + HTR length on both sides | solve | 22% | 47% | 76% | 32% | 21% | 7% | 0% | 0% |
| 13 or less | + corner length L and E-parity | solve | 21% | 46% | 76% | 33% | 23% | 9% | 0% | 0% |
| 13 or less | + pairs and HTR | solve | 23% | 49% | 77% | 33% | 22% | 8% | 0% | 0% |
| 13 or less | + pairs, corner cases and HTR | solve | 25% | 52% | 80% | 35% | 25% | 10% | 0% | 0% |
| 13 or less | + pairs, HTR, L and E-parity | solve | 24% | 50% | 79% | 35% | 26% | 12% | 3% | 0% |

**5qt (2c5, 4b5)**

| Finish needed | What you know | How you get it | Best 10% keeps | Best 25% keeps | Best 50% keeps | Drop, keeping 90% | Drop, keeping 95% | Drop, keeping 99% | In classes under 1% | Finishes lost by dropping those |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **9 or less** (<0.01% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 100% | 100% |
| 9 or less | subset | look | 19% | 45% | 73% | 24% | 14% | 4% | 100% | 100% |
| 9 or less | + true pairs | look | 90% | 100% | 100% | 90% | 86% | 80% | 100% | 100% |
| 9 or less | + corner case on both sides | recognise | 55% | 87% | 100% | 73% | 68% | 65% | 100% | 100% |
| 9 or less | + pairs and corner cases | recognise | 100% | 100% | 100% | 96% | 95% | 92% | 100% | 100% |
| 9 or less | + HTR length on both sides | solve | 100% | 100% | 100% | 98% | 97% | 97% | 100% | 100% |
| 9 or less | + corner length L and E-parity | solve | 100% | 100% | 100% | 96% | 96% | 95% | 100% | 100% |
| 9 or less | + pairs and HTR | solve | 100% | 100% | 100% | 99% | 99% | 99% | 100% | 100% |
| 9 or less | + pairs, corner cases and HTR | solve | 100% | 100% | 100% | 99% | 99% | 99% | 100% | 100% |
| 9 or less | + pairs, HTR, L and E-parity | solve | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 34% |
| **10 or less** (0.02% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 100% | 100% |
| 10 or less | subset | look | 16% | 38% | 64% | 15% | 8% | 2% | 100% | 100% |
| 10 or less | + true pairs | look | 64% | 83% | 97% | 64% | 55% | 39% | 100% | 100% |
| 10 or less | + corner case on both sides | recognise | 39% | 64% | 92% | 53% | 44% | 31% | 100% | 100% |
| 10 or less | + pairs and corner cases | recognise | 74% | 93% | 100% | 79% | 72% | 62% | 100% | 100% |
| 10 or less | + HTR length on both sides | solve | 60% | 84% | 99% | 68% | 62% | 49% | 100% | 100% |
| 10 or less | + corner length L and E-parity | solve | 57% | 98% | 100% | 79% | 77% | 74% | 100% | 100% |
| 10 or less | + pairs and HTR | solve | 79% | 96% | 100% | 82% | 77% | 68% | 100% | 84% |
| 10 or less | + pairs, corner cases and HTR | solve | 83% | 100% | 100% | 86% | 83% | 78% | 100% | 84% |
| 10 or less | + pairs, HTR, L and E-parity | solve | 100% | 100% | 100% | 95% | 94% | 92% | 100% | 61% |
| **11 or less** (0.24% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 100% | 100% |
| 11 or less | subset | look | 14% | 34% | 60% | 13% | 7% | 2% | 100% | 100% |
| 11 or less | + true pairs | look | 46% | 69% | 87% | 44% | 29% | 10% | 95% | 67% |
| 11 or less | + corner case on both sides | recognise | 29% | 52% | 80% | 36% | 27% | 16% | 100% | 100% |
| 11 or less | + pairs and corner cases | recognise | 54% | 76% | 93% | 57% | 44% | 26% | 96% | 64% |
| 11 or less | + HTR length on both sides | solve | 39% | 62% | 87% | 44% | 33% | 20% | 99% | 90% |
| 11 or less | + corner length L and E-parity | solve | 34% | 62% | 89% | 49% | 43% | 39% | 99% | 91% |
| 11 or less | + pairs and HTR | solve | 55% | 78% | 93% | 57% | 45% | 27% | 96% | 64% |
| 11 or less | + pairs, corner cases and HTR | solve | 57% | 80% | 95% | 61% | 50% | 34% | 96% | 62% |
| 11 or less | + pairs, HTR, L and E-parity | solve | 66% | 88% | 100% | 73% | 66% | 55% | 94% | 47% |
| **12 or less** (2.1% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 12 or less | subset | look | 12% | 31% | 56% | 12% | 6% | 1% | 0% | 0% |
| 12 or less | + true pairs | look | 32% | 55% | 78% | 29% | 17% | 5% | 32% | 11% |
| 12 or less | + corner case on both sides | recognise | 23% | 44% | 72% | 27% | 19% | 9% | 17% | 4% |
| 12 or less | + pairs and corner cases | recognise | 37% | 61% | 84% | 40% | 28% | 13% | 36% | 8% |
| 12 or less | + HTR length on both sides | solve | 28% | 48% | 76% | 30% | 21% | 10% | 18% | 3% |
| 12 or less | + corner length L and E-parity | solve | 26% | 49% | 78% | 33% | 24% | 16% | 19% | 2% |
| 12 or less | + pairs and HTR | solve | 38% | 61% | 84% | 39% | 27% | 12% | 38% | 9% |
| 12 or less | + pairs, corner cases and HTR | solve | 38% | 63% | 85% | 41% | 29% | 14% | 38% | 9% |
| 12 or less | + pairs, HTR, L and E-parity | solve | 42% | 68% | 89% | 48% | 36% | 20% | 45% | 9% |
| **13 or less** (14% get there) | nothing | | 10% | 25% | 50% | 10% | 5% | 1% | 0% | 0% |
| 13 or less | subset | look | 11% | 28% | 53% | 12% | 6% | 1% | 0% | 0% |
| 13 or less | + true pairs | look | 22% | 43% | 68% | 19% | 11% | 2% | 0% | 0% |
| 13 or less | + corner case on both sides | recognise | 18% | 37% | 65% | 21% | 14% | 6% | 2% | 0% |
| 13 or less | + pairs and corner cases | recognise | 25% | 48% | 74% | 27% | 17% | 7% | 2% | 0% |
| 13 or less | + HTR length on both sides | solve | 20% | 40% | 67% | 22% | 15% | 6% | 1% | 0% |
| 13 or less | + corner length L and E-parity | solve | 20% | 43% | 72% | 26% | 19% | 7% | 1% | 0% |
| 13 or less | + pairs and HTR | solve | 25% | 47% | 73% | 26% | 17% | 6% | 1% | 0% |
| 13 or less | + pairs, corner cases and HTR | solve | 25% | 48% | 74% | 28% | 18% | 7% | 2% | 0% |
| 13 or less | + pairs, HTR, L and E-parity | solve | 27% | 52% | 78% | 32% | 22% | 10% | 4% | 0% |

---

## Docs and sheets referred to

- Levi Gibson, "DR Bounding": https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA
- Rodney Kinney, "Advanced DR Bounding [Beta]": https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0
- Rodney Kinney, sheet "Adv DR Bounding" (rules vs the 216 computed cases): https://docs.google.com/spreadsheets/d/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY
- FakeMMAP, sheet "OBL++": https://docs.google.com/spreadsheets/d/1kax7evfA85p_4ArXKO7si3FrCpj7PEeFwoz4GY5wRAE
- wen, sheet "HTR better smh (v2)" (the corner subsets): https://docs.google.com/spreadsheets/d/1ZhulzHeNgv2Hiy4x9R1MzsMRlPlI-E8DRiHFJlPlboM
- FakeMMAP's BFS listing, script and tables are attachments on FakeMMAP's posts of 6–10 Sep 2026 in #fmc-theory.
- Mallard (cubelib) source, for how the 48 subsets are built: https://github.com/Jobarion/cubelib
- Rodney Kinney, "HTR Theory" (September 2023): https://docs.google.com/document/d/1HjS92UBCeCasbW44ezE0fjt5vmWQvlfkaC4rA113nmw
- Levi Gibson, sheet "Corner Solution Length x DR Finish length" (sampled; Appendix B is the exact version): https://docs.google.com/spreadsheets/d/14rZI1Nf84Og1jS8dN1MfT0sYhvdIWu9gPXkHDs1iVU4

