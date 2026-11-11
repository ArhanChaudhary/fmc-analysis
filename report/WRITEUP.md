# Judging a DR by hand: what the full BFS says

*What you can read off a DR, how much it tells you about the finish, and which bounds hold. Every number is an exact count over all DR states.*

November 2026. A name with a date is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs and sheets are listed with links at the end.

---

## Start here

This is long because most of it is reference. You don't have to read it front to back.

- **If you read one thing**: the table in [section 8](#8-what-id-do-per-subset). For each kind of DR it says how often it finishes short, what to look at, when to drop it, and what not to conclude.
- **If you have five minutes**: the [Introduction](#introduction), then [section 3](#3-how-much-can-a-read-tell-you), which measures how much any read can tell you.
- **To see it on real DRs**: the examples file that goes with this doc, eleven DRs read step by step.
- **Everything from section 9 on** is checking and reference: the 216 cases, the proof, how it was computed, and seven appendices of tables to look things up in.

## Contents

| Section | What is in it | Size |
|---|---|---|
| [Introduction](#introduction) | The question, and what came out, in seven bullets. | 600 words |
| [1. What people asked for](#1-what-people-asked-for) | The gap in the solvers' own words, and the sixteen questions from the server that are answered here. | 500 words |
| [2. The data](#2-the-data) | What was computed, and what "optimal" and "in 12" mean. | 200 words |
| [3. How much can a read tell you?](#3-how-much-can-a-read-tell-you) | The ceiling: every read against the exact finish. Zagros's two hunches. | 550 words |
| [4. The reads, cheapest first](#4-the-reads-cheapest-first) | What each read is worth, with the tables: [4.1 Subset](#41-subset), [4.2 Pairs](#42-pairs), [4.3 Corner case, on both sides](#43-corner-case-on-both-sides), [4.4 HTR length on both sides](#44-htr-length-on-both-sides), [4.5 Corner length and E-slice parity](#45-corner-length-and-e-slice-parity), [4.6 The last DR move](#46-the-last-dr-move). | 1,950 words |
| [5. Bounds people use, graded](#5-bounds-people-use-graded) | Levi's formula, trangium's 2q bound at any qt, HTR length, the parity bound. Which never fail, how often the others do. | 1,300 words |
| [6. Leave slice, the slice, and width](#6-leave-slice-the-slice-and-width) | What the slice costs, and how many first moves are optimal. | 200 words |
| [7. What a computer can prove from the DR](#7-what-a-computer-can-prove-from-the-dr) | Table lookups that prove "no 12" for most 4–5qt DRs, and why no hand read gets there. | 1,450 words |
| [8. What I'd do per subset](#8-what-id-do-per-subset) | **The one to read.** For each of the 12 corner subsets: how it finishes, what to read, when to drop it, what not to conclude. | 3,550 words |
| [9. The 216 NISS@1qt cases, three ways](#9-the-216-niss1qt-cases-three-ways) | FakeMMAP's and Rodney's tables checked with half turns, with DR moves and with any move. | 700 words |
| [10. The proof, if you don't speak Lean](#10-the-proof-if-you-dont-speak-lean) | What is proven, how, and what you have to trust. | 1,200 words |
| [11. How it was computed and checked](#11-how-it-was-computed-and-checked) | The programs, and what agreed with what. | 650 words |
| [12. What this doesn't do](#12-what-this-doesnt-do) | Limits, and questions left open. | 250 words |
| [Appendix A: all 48 subsets](#appendix-a-all-48-subsets) | Share, average, shortest and longest optimal, odds for 12 and 13. | tables |
| [Appendix B: odds by corner length and E-slice parity](#appendix-b-odds-by-corner-length-and-e-slice-parity) | For the big high-qt subsets. | tables |
| [Appendix C: the 216 NISS@1qt cases](#appendix-c-the-216-niss1qt-cases) | Every case with its optimal for half turns, DR moves and any move. | tables |
| [Appendix D: odds by true pairs, all 48 subsets](#appendix-d-odds-by-true-pairs-all-48-subsets) | Odds for 12 and 13 by number of pairs. | tables |
| [Appendix E: the 46 corner cases](#appendix-e-the-46-corner-cases) | Layout, example scramble, corner solution lengths, odds, and the both-sides tables. | tables |
| [Appendix F: HTR length on both sides, all 48 subsets](#appendix-f-htr-length-on-both-sides-all-48-subsets) | The square tables. | tables |
| [Appendix G: a scramble for every subset](#appendix-g-a-scramble-for-every-subset) | A longest state, and one that finishes in exactly its longer HTR, for each of the 48 subsets. | tables |
| [Docs and sheets referred to](#docs-and-sheets-referred-to) | Links. | links |

Sections 1 to 8 are the main text, about 10,500 words with their tables. The rest is reference.

---

## Introduction

The question I started from: can Levi's and Rodney's DR bounding be pushed to 3qt, 4qt and 5qt DRs, so you can toss a DR because its bound is high instead of wasting time on it?

With a computer, yes. Look at part of the DR, tabulate the fewest moves that solve that part, and you have a lower bound at any qt with no skeleton. With the right table it proves "no finish in 12" for 59% of 5qt DRs. That was the first version of this doc and it is now section 7. The trouble is the tables have millions of cases, so nobody can use them in an attempt, and the bar on the server is clear:

> "is the lower bound fast to determine by human methods? If it takes too long to figure out the lower bound, you can just as well try to actually solve the DR" ([tseitsei89, 13 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1416359895761944657))

> "I don't expect anyone to use the decision trees directly. I'm just hoping to use them to find the most important 2-3 features … then make some simple rules out of just those features" ([Rodney, 1 Jul 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1389481110181777478))

So this version asks the human question. Take what you can actually read off a DR (subset, pairs, corner case, HTR length on both sides, corner solution length, E-slice parity) and measure exactly what each one tells you about the finish. I BFSed the whole DR group, 19,508,428,800 states, so nothing below is sampled.

What came out:

- **Nothing you can read is a clean yes/no.** The subset explains 35% of the variance of the optimal. Add pairs, corner length, parity and HTR length on both sides and you're at 48%. What's left has an sd of 0.78 moves (0.88 with the subset alone). Zagros's hunch that corner case + HTR on both sides pins the optimal to ~0.25 moves: it's 0.82.
- **The reads do move the odds, and they stack.** Cheapest first: pairs, corner case on both sides, HTR on both sides, corner length with E-parity. For 4qt DRs, if you keep only the best-looking quarter you keep 40% of the finishes in 12 going by subset alone, 53% going by pairs, 66% with everything.
- **A few real kill rules.** 2c5 with the bad corners stacked on both sides: no finish in 12 at all, 0.6% in 13. 2c4 stacked on both sides: 0.6% in 12. 0c3 4e that's 12 to HTR on both sides: 0.02% in 12. The tables are below.
- **Questions from the server, answered exactly**: stats by bad corner position (Daichi, JTuu, wen), by pairs (Rodney, Levi), the normal × inverse HTR table (Zagros), the 4a1 4e bound against the real leave slice (count quackula), the cost of the slice (JTuu), an invertible last move (Zagros), God's number per subset (compLex), optimal lengths of all corner cases (Evan).
- **Bounds measured.** Levi's 1qt formula, trangium's 2q bound taken to any qt, HTR length, corner length with parity. Which hold for every finish, how often a finish with extra quarter turns gets under the others, and how far below optimal they all sit.
- **Where the information is.** A computer that sees the corners exactly plus the edge colours proves "no 12" for 81% of 4qt and 95% of 5qt DRs. Everything readable put together can rule out 24% and 45% (to within 1%). The gap is the corner–edge relation, which is what Rodney's NISS@1qt tracing looks at. No count of visible features replaces it.
- **Proven in Lean**: the optimal finish of every DR state (so every stat here is a count over proven optimals), the HTR and corner-length-with-parity bounds, and the 216 HT-only values.

---

## 1. What people asked for

The gap, in the words of the people who bound in real solves:

- Jay: bounding "isn't really equipped to handle higher qt stuff which is where optimal usually gets missed" ([Jay, 28 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1311881154328133673)).
- Levi uses it at 2q and 3q. At 4q: "Too many variations unfortunately. It kinda works with 4q, but it is slower than just checking reductions to 2c3" ([Levi, 13 Feb 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1339747273902395507)). And: "If there are other metrics (i.e blocks, HTR patterns, etc) that you can bound 2q cases with that would be incredible" ([Levi, 12 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1371536829844689010)).
- Rodney: "+3 or lower penalties are really quite rare … That's what makes 4qt cases so intractable currently" ([Rodney, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546185406075244564)).
- tseitsei89: "Being able to quickly tell when a DR has a short finish would be a real holy grail" ([tseitsei89, 28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1466158543496544494)). His test for a good stat: "Optimally you would only have 100% cases and 0% cases" ([tseitsei89, 21 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1386074648424218745)).

And the specific questions, each with a section below:

| Asked | By | Where |
|---|---|---|
| Corner case + HTR on normal + HTR on inverse "can tell you the optimal solution with a standard deviation of like 0.25 moves"? | [Zagros, 4 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1490097940641878216) | §3 |
| Stats by optimal corner length and longest direct HTR; "predict the opt finish length within ~1 move"? | [Zagros, 25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1365341555308888114) | §3 |
| A square table, moves to HTR on both sides. "4c3 that is 9+ on both sides I throw away" | [Zagros, 10 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1470865840298655918) | §4.4 |
| "you won't get very clean stats from just the corner case plus bad edge count. You would need to break cases down by some kind of pair counts" | [Rodney, 4 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1490027292767027452) | §4.2 |
| "blocky 2c4s are way better than not-so-blocky 2c4s?" | [Levi, 28 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1366528885432258592) | §4.2 |
| "stats on just bad corner positions for each subset", good/bad parity, on both sides | [Daichi, 8 May 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1502289745143922790), [tseitsei89](https://discord.com/channels/1007840975726575667/1007841273111117924/1502290363916877954) | §4.3 |
| "stats on 4c3 that take 4a3 corner position/parity into account?" | [JTuu, 22 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1518725967948808223) | §4.3 |
| Average optimal of the 2c4 layouts: "double stack vs single stack vs no stack" | [wen, 24 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1563566658356908108) | §4.3 |
| "is there a doc with optimal lengths for all corner cases?" | [Evan, 23 Mar 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1485844126770532435) | Appendix E |
| "average difference between a 4a1 4e bound and the actual leave slice? And how likely it is to be +0, +1, +2" | [count quackula, 9 Jan 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1459279260824109322) | §5 |
| "publicly available statistics for the errors on bounding?" | [compLex, 27 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1377120894320906323) | §5 |
| trangium's "true 2q bound": how good is it, does it work at more qts? | [trangium, 27 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487207920256024738) | §5 |
| "probability distribution of +N to solve slice given #qt" | [JTuu, 21 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1286925282183483403) | §6 |
| "how does the optimal change from a pure DR vs. a DR in a solve where you have one move you can invert?" | [Zagros, 29 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1487985615319601312) | §4.6 |
| The "width" of a DR | [JTuu, 30 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1488242984259686461) | §6 |
| "are god's numbers known for htr subsets?" | [compLex, 16 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406380780904517663) | Appendix A |

---

## 2. The data

- **Optimal finish of every DR state.** BFS of the group ⟨U, D, R2, L2, F2, B2⟩, all 19,508,428,800 states. "Optimal" means the shortest finish with those ten moves, same as nissy's `drudfin` and Joba's table. Average 13.58, max 18.
- **Optimal leave slice of every DR state.** Same thing ignoring the E-slice: fewest DR moves that solve corners and the eight U/D-layer edges. Average 13.29, and the max is 18 as well. (`U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'` needs 18 for the leave slice and 18 for the full finish.)
- **Every count treats each DR state as equally likely.** Real DRs aren't uniform across subsets, so read everything per subset.
- Bad corners and edges are counted the way the server counts them, up to turning a layer. The Q in 2c**4** is the corner qt count. 4c3 = 4a3 and 4b3 together (they swap on inverse), same for 4c4.
- "Finishes in 12" always means 12 or fewer.

How it was checked, and what's proven, is in sections 10 and 11.

---

## 3. How much can a read tell you?

Two ways to measure a read. First, how much scatter is left in the optimal once you know it (sd, in moves). Second, triage: rank the DRs of a qt group by the read, keep only the best-looking 10% / 25% / 50%, and count how many of the finishes in 12 you kept.

| What you know | sd left | 3qt: kept at 10 / 25 / 50% | 4qt | 5qt |
|---|---:|---:|---:|---:|
| nothing | 1.09 | 10 / 25 / 50 | 10 / 25 / 50 | 10 / 25 / 50 |
| subset | 0.88 | 21 / 43 / 72 | 18 / 40 / 73 | 12 / 31 / 56 |
| + true pairs | 0.85 | 24 / 48 / 74 | 29 / 53 / 80 | 32 / 55 / 78 |
| + corner case on both sides | 0.83 | 23 / 48 / 76 | 32 / 59 / 86 | 23 / 44 / 72 |
| + corner length L and E-parity | 0.83 | 23 / 47 / 75 | 30 / 57 / 86 | 26 / 49 / 78 |
| + HTR length on both sides | 0.82 | 24 / 49 / 77 | 32 / 60 / 86 | 28 / 48 / 76 |
| + pairs and L | 0.81 | 25 / 50 / 78 | 35 / 62 / 87 | 38 / 63 / 85 |
| + pairs, L, E-parity, HTR on both sides | 0.78 | 27 / 54 / 81 | 38 / 66 / 90 | 42 / 68 / 89 |
| *the optimal leave slice (for scale, you can't read this)* | 0.43 | 46 / 83 / 100 | 92 / 100 / 100 | 100 / 100 / 100 |

Only 20% of 3qt, 6.8% of 4qt and 2.1% of 5qt DRs finish in 12, so a perfect read would put all of them in the top 10% at 4–5qt. The best combination of everything readable gets 38–42% there.

The other direction, throwing away. Call a class "dead" if at most 1% of it finishes in 12:

| What you know | 3qt dead | 4qt dead | 5qt dead |
|---|---:|---:|---:|
| true pairs | 0.3% | 9% | 32% |
| HTR length on both sides | 3% | 19% | 18% |
| L and E-parity | 3% | 19% | 19% |
| pairs, L, E-parity, HTR on both sides | 6% | 24% | 45% |
| *really don't finish in 12* | *80%* | *93%* | *98%* |

If your target is a finish in 13 instead, no read kills more than 4% of any qt group.

So tseitsei89's "100% cases and 0% cases" don't exist at this level. There is no feature count that sorts DRs into good and bad. What exists is a set of reads that each roughly double your hit rate, and a handful of corners of the tables that really are dead.

**Zagros's two hunches.**

- *Corner case + HTR on both sides gives the optimal to ~0.25 moves* ([Zagros, 4 Apr 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1490097940641878216)). The sd left is 0.82 over all DRs. By corner subset it runs from 0.74 (4c4) to 0.97 (0c0). Adding L and E-parity makes it 0.80.
- *L + longest HTR predicts within ~1 move* ([Zagros, 25 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1365341555308888114)). True, 93.3% of DRs are within one move of the typical value for their (subset, L, longer HTR). But 91.3% are within one move of the typical value for their subset alone. The finish just doesn't vary much inside a subset.

A pair that shows what the first hunch is up against. Both are 2c4 4e, with the same corner case on normal and on inverse, 7 to HTR on both sides, and the same corner length (7):

    D F2 U' F2 D B2 D'                                 // optimal 7
    D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'      // optimal 16

---

## 4. The reads, cheapest first

### 4.1 Subset

The baseline, and still the biggest single piece of information. Appendix A has all 48 with average, share finishing in 12 and 13, and the longest optimal in each (God's number per subset, which compLex asked about). The longest: 18 for 0c0 8e, 0c3 4e, 2c5 0e and 2c5 4e, 17 or 16 for most others, 13 for 0c0 0e. One of each 18:

    F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'      // 0c0 8e
    F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'   // 0c3 4e
    U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'      // 2c5 0e
    R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'  // 2c5 4e

Appendix G has a longest one for every subset.

The shortest possible HTR by corner qt is 1 / 3 / 5 / 7 / 9 moves for 1 to 5 qt. These five states have exactly that on both sides: `D`, `D B2 D'`, `D' B2 D' B2 D'`, `D B2 D' B2 D B2 D'`, `U' L2 U R2 U' L2 U R2 D`. Joba took 1 / 2 / 4 / 6 / 8 as a safe lower bound ([Joba, 13 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1349876840914751578)); the exact floor is one higher from 2qt up, on either side.

### 4.2 Pairs

Count the true pairs: a corner and an edge next to each other in the U or D layer with both touching stickers matching (16 places to look). This is the read that costs nothing, and it works at every qt.

Share of each corner subset finishing in 12, by number of true pairs:

| Corners | 0 pairs | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| 4b2 | 23% | 28% | 35% | 44% | 53% | 63% |
| 2c3 | 16% | 21% | 27% | 34% | 42% | 51% |
| 4c3 | 6.9% | 8.7% | 11% | 15% | 19% | 24% |
| 2c4 | 4.2% | 5.9% | 8.3% | 12% | 17% | 23% |
| 4c4 | 0.7% | 1.0% | 1.4% | 2.0% | 2.9% | 4.3% |
| 2c5 | 0.7% | 1.1% | 1.7% | 2.9% | 4.7% | 7.6% |
| 4b5 | 0.5% | 0.9% | 1.5% | 2.4% | 4.1% | 6.3% |
| share of all DRs | 14% | 27% | 27% | 18% | 9% | 4% |

Each pair is worth about 0.15 moves of average optimal and multiplies your odds of a 12 by about 1.4. So Levi is right about blocky 2c4s: from 4% with no pairs to 23% with five. It's not special to 2c4 though, the ratio is about the same in every subset. Appendix D has all 48 subsets, for 12 and 13.

On Rodney's finer split: I also counted pseudo-pairs (both stickers opposite), side semi-pairs and top semi-pairs, defined as in his message. Knowing all four counts instead of just the true pairs moves the sd left from 0.850 to 0.842. Pairs with E-slice edges add even less. So count true pairs and stop.

You don't need to count again on the inverse scramble: a block stays a block, so the number of true pairs is the same on both sides for every DR state.

### 4.3 Corner case, on both sides

This is what Daichi, JTuu and wen asked for. There are 46 corner cases once you merge rotations, mirrors and turning a layer. Inside a corner subset they are *not* equally good, and since the corner case on inverse is a different one, there are two reads.

**2c4** (wen's stacks). Seven cases:

| Bad corners | A qt takes it straight to | L | Share of 2c4 | Finishes in 12 | in 13 |
|---|---|---|---:|---:|---:|
| both on one layer, adjacent | 2c3 | 7–10 | 17% | 16.2% | 57% |
| one up one down, opposite | 4b3 | 8–10 | 8% | 13.2% | 51% |
| both on one layer, adjacent | 2c3 | 7–10 | 17% | 12.5% | 47% |
| both on one layer, adjacent | nothing, needs a setup | 8–11 | 17% | 7.0% | 33% |
| one up one down, stacked | 4b3 | 9–11 | 8% | 7.0% | 33% |
| one up one down, opposite | nothing, needs a setup | 8–11 | 17% | 6.4% | 31% |
| one up one down, stacked | nothing, needs a setup | 9–12 | 17% | 4.1% | 23% |

Both sides together: best is the first case on both sides, 26% in 12 and 75% in 13. Stacked-with-setup on both sides: 0.6% in 12 and 7.5% in 13. Any pair of stacked cases: 0.6–2.5% in 12. So "double stack" is as dead as a 5qt, and the best layout on both sides is as good as an average 2c3 4e (27%). The fastest any double-stacked 2c4 finishes is 11: `U2 L2 D' F2 U' R2 U F2 D L2 U2`.

**2c5.** Three cases: adjacent on one layer (half of 2c5, 3.4% in 12), one up one down opposite (1.9%), stacked (0.6%). Both sides adjacent: 4.7% in 12, 25% in 13. Both sides stacked: **0.0% in 12, 0.6% in 13**, average optimal 15.3. That's 6% of all 2c5 you can drop on sight, and with stacked on one side and opposite on the other (0.2% in 12) it's 19%. The fastest any double-stacked 2c5 finishes is 13: `U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2`.

**4c3** (JTuu's question). Nine cases, seven of them 4a3 and two 4b3. By the case you see on one side, the share finishing in 12 runs from 21.6% (a 4a3 with L 7–9) down to 3.6% (a 4a3 with L 9–11). The two 4b3 cases sit in the middle at 13.5% and 11.4%. With both sides: 23% down to 3%.

**4b2** (Daichi's four). They are exactly his list: 2-2 with L 3–6 (44% in 12), 3-1 with L 4–7 (40%), 3-1 with L 5–8 (33%), 2-2 with L 6–9 (30%). Both sides good 2-2: 50%. Both sides bad 2-2: 21%.

**4a2.** The widest spread of the low-qt subsets: 31% in 12 for the best case (L 5–8) down to 9% for the worst (L 8–11). Both sides worst: 2.3%.

**4c4**: 0.6% to 4.3%. **4b5**: 1.3% to 2.2%, nothing to see.

Appendix E lists all 46 cases with an example scramble for each, the L range (the optimal corner solution lengths the case can have, which is what Evan asked for), and the both-sides tables.

A warning: the bad corner *positions* don't always tell you the case. 2c4 has three different "both on one layer, adjacent" cases, at 16%, 12.5% and 7%. What separates them is the corner permutation, which you get the way you already get the subset (tracing, or whatever corner-case system you use). The column "a qt takes it straight to" is the quick tell: if some U or D quarter turn drops the corner qt count right away, you're in one of the good ones.

### 4.4 HTR length on both sides

Zagros asked for the square table ([Zagros, 10 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1470865840298655918)); trangium posted one from samples of 20–100 per cell. Exact, for the four big high-qt subsets. Each cell: share finishing in 12.

**4c3 4e**, shorter side down, longer side across:

| | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|
| 7 | 55% | 43% | 31% | 22% | 15% |
| 8 | | 30% | 20% | 13% | 4.6% |
| 9 | | | 11% | 5.6% | 1.8% |
| 10 | | | | 2.1% | 0.3% |

**2c4 4e**:

| | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|
| 7 | 36% | 27% | 20% | 16% | 13% |
| 8 | | 17% | 11% | 7.4% | 5.8% |
| 9 | | | 6.0% | 2.9% | 1.9% |
| 10 | | | | 0.9% | 0.4% |

**2c5 4e**:

| | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|
| 9 | 13% | 6.7% | 3.0% | 1.1% |
| 10 | | 2.7% | 1.0% | 0.2% |
| 11 | | | 0.1% | 0.0% |

**0c3 4e**:

| | 10 | 11 | 12 | 13 |
|---|---:|---:|---:|---:|
| 10 | 12% | 7.8% | 4.2% | 0.0% |
| 11 | | 4.5% | 0.4% | 0.0% |
| 12 | | | 0.0% | 0.0% |

One more move to HTR on both sides costs about half a move of average optimal and cuts the odds of a 12 by two to three. Appendix F has the square table for all 48 subsets with share, average, and odds for 12 and 13.

**Zagros's rule, "4c3 that is 9+ on both sides I throw away".** That's 51% of all 4c3. Of those, 6.4% finish in 12 and 34% in 13 (average 13.74). Of the other half, 18% and 59% (average 13.22). So the rule halves your 4c3s and keeps 73% of the finishes in 12. If you can be pickier: 4c3 with 7 or less on at least one side is 10% of them and finishes in 12 28% of the time. The rule does throw away real finds: `U' L2 D' B2 U' B2 U L2 D` is a 4c3 4e that is 9 to HTR on both sides and finishes in 9 (`D' L2 U' B2 U B2 D L2 U`).

Knowing the two HTR lengths does not give you a better *guarantee* than the longer one: in every subset some state finishes in exactly max(normal, inverse). The 4c3 4e just above is one, and Appendix G has one for every subset. It's an odds read.

### 4.5 Corner length and E-slice parity

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

This one is a true lower bound, proven in Lean: no finish is shorter than the best corner solution of the right parity. At 5qt it proves "no 12" for 13% of DRs, at 4qt for 5%. It needs the *optimal* corner solutions of both parities, so it's a read for when you've written the skeletons down anyway.

As an odds read, L does about what HTR length does (table in section 3). Appendix B splits the big high-qt subsets by L and parity. For 2c4 4e: with L = 8, 13–17% finish in 12. With L = 11, 2%. With L = 12, 1.6% if the E-slice is even and none if it's odd.

The E-slice parity on its own, without L, is a small read but it's free. It mostly decides whether the finish wants to be even or odd in length. At 4qt, 8.1% finish in 12 with an odd E-slice against 5.5% with an even one. At 5qt it's the other length that moves: 17.6% finish in 13 with an odd E-slice against 10.3% with an even one.

### 4.6 The last DR move

Zagros asked what one invertible move is worth. If your DR ends in R, then R' is also a DR and its state is yours plus an R2, so you get the better of two finishes.

| | Pure DR | Last move invertible |
|---|---:|---:|
| average optimal, all DRs | 13.58 | 13.26 |
| finishes in 12, 1–2qt | 35% | 49% |
| 3qt | 20% | 30% |
| 4qt | 6.8% | 11% |
| 5qt | 2.1% | 3.7% |

A third of the time the other DR is one shorter, a third the same, a third one longer, in every subset. So it's worth 0.33 moves flat. (If you could pick any of the four side half turns it would be 0.73.)

---

## 5. Bounds people use, graded

A bound is only a bound if it never exceeds the optimal. Graded on all states:

| Bound | Ever too high? | Its average | Average optimal there |
|---|---|---:|---:|
| longer HTR, normal or inverse (all DRs) | never (proven) | 9.22 | 13.58 |
| best corner solution with the right E-parity (all DRs) | never (proven) | 9.44 | 13.58 |
| Levi's 1qt formula, HTR normal + HTR inverse − 1 (4a1 4e) | never for a finish with one quarter turn. A finish with three is shorter for 11.7% of 4a1 4e | 10.85 | 12.27 |
| setup + HTR, any qt (below) | never for a finish with the minimum number of quarter turns. A finish with more is shorter for 2.6% at 1–2qt and 0.002% above | see below | |

**Levi's formula.** (HTR normal) + (HTR inverse) − 1 bounds the finishes with one quarter turn, which is what Levi's doc uses it for. (His doc writes it as the path to the trigger on normal + on inverse + 1. An HTR is that path plus the quarter turn, so it's the same number.) A 1qt state can also be solved with three quarter turns, and the number worth having is how often that is shorter. Over all 286,654,464 states of 4a1 4e, the optimal is below the formula for 11.7% (by 1 in 8.4%, by 2 in 2.7%, by 3+ in 0.6%), equal for 18.0%, above for 70.3%. If the formula says ≤ 12, a 3qt finish beats it 2.5% of the time. Example:

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

Average +0.70. The leave slice is below the formula 19.7% of the time, more often than the full finish is, because leaving the slice is easier.

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

**Rodney's rules at 1qt** are graded in section 9: a true lower bound in all 216 cases, even against DR-breaking finishes.

**So for bounding error stats** (compLex's question): the guaranteed bounds you can compute by hand are on average four moves under optimal. The useful hand bound is still Rodney's, per skeleton, late.

---

## 6. Leave slice, the slice, and width

**Cost of the slice** (JTuu's question): optimal finish minus optimal leave slice.

| | +0 | +1 | +2 | +3 or more | Average |
|---|---:|---:|---:|---:|---:|
| 0qt | 44% | 42% | 14% | 0.6% | +0.71 |
| 1–2qt | 56% | 39% | 5.4% | 0.1% | +0.50 |
| 3qt | 67% | 32% | 1.6% | | +0.35 |
| 4qt | 79% | 20% | 0.5% | | +0.21 |
| 5qt | 85% | 15% | 0.1% | | +0.15 |
| all DRs | 73% | 26% | 1.6% | | +0.29 |

The longer the finish, the more room to fit the slice for free. (+1 happens because the optimal finish doesn't have to be an optimal leave slice with a slice inserted.)

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

Short finishes are narrow: when a DR has a 12, two times out of three there is exactly one first move that gets it. Long finishes are wide. Higher qt DRs have more optimal first moves (3.1 on average at 5qt against 2.6 at 2qt) only because their optimals are longer.

---

## 7. What a computer can prove from the DR

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

- **NISS@DR on HTR states with half turns only *is* FakeMMAP's table.** His 216 example scrambles are 216 different cases and every value matches (both proven in Lean). So NISS@DR is that table grown from 216 cases to 6.35 million: one for every corner state and edge layout a DR can have.
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

How often does a level *prove* the finish is 13+ (so no 12)? Percentages are of all DR states in the row.

| Corner qt | Really 13+ | HTR | L+parity | L+S+T | NISS@DR | +H-perm | Everything | Really 14+ | Everything proves 14+ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1–2qt (4a1, 4a2, 4b2) | 64.7% | 0.0% | 0.0% | 1.9% | 3.8% | 8.2% | 23.9% | 21.2% | 3.8% |
| 3qt (0c3, 2c3, 4c3) | 79.9% | 0.4% | 0.7% | 4.6% | 9.2% | 21.6% | 48.9% | 41.2% | 12.6% |
| 4qt (0c4, 2c4, 4c4) | 93.2% | 0.2% | 5.0% | 16.5% | 34.0% | 53.5% | 81.3% | 70.3% | 41.3% |
| 5qt (2c5, 4b5) | 97.9% | 0.0% | 12.9% | 28.4% | 58.6% | 76.1% | 94.8% | 86.1% | 66.2% |

"The longer your HTR, the more useful it is to have a lower bound" ([Rodney, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546184215542898760)). This is that, in numbers: at 1–2qt bounding from the DR does almost nothing and you should bound late like Levi and Rodney do. At 4–5qt it kills most DRs on sight. (Rows go by the Q in the subset name, which is the corner qt count. A few subsets need more actual qts than that: every 0c0 with bad edges needs 2, and 4a1 0e and 4a1 2e need 3.)

All 48 subsets are in Appendix A. The big ones:

| Subset | Share of all DRs | Avg optimal | ≤ 12 | ≤ 13 | NISS@DR proves 13+ | Everything proves 13+ |
|---|---:|---:|---:|---:|---:|---:|
| 4b2 4e | 5.88% | 12.73 | 34.4% | 81.9% | 0% | 21% |
| 2c3 4e | 7.84% | 12.94 | 26.7% | 72.5% | 0% | 31% |
| 4c3 4e | 5.88% | 13.50 | 12.0% | 45.3% | 14% | 68% |
| 2c4 4e | 11.76% | 13.66 | 9.1% | 37.9% | 18% | 74% |
| 0c3 4e | 0.73% | 14.64 | 1.5% | 8.9% | 93% | 96% |
| 4c4 4e | 5.88% | 14.38 | 1.8% | 11.8% | 67% | 97% |
| 2c5 4e | 3.92% | 14.30 | 2.6% | 15.3% | 61% | 93% |
| 4b5 4e | 5.88% | 14.29 | 1.8% | 13.3% | 60% | 96% |

### Examples

I wrote a small lookup tool for this: give it a scramble and the moves to DR (NISS in brackets) and it prints every level on both sides plus the real optimal, straight from the precomputed tables. The numbers below are its output.

**Rodney's first random scramble** (from the Advanced DR Bounding doc):

    U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2   // 2c3 6e

He goes through three skeletons, kills about a dozen triggers with bounding, finds a 13 and says "to strictly prove it, we'd have to try inserting corner swaps in front of the first qt". From the DR alone:

    HTR length          9 / 7      (normal / inverse)
    corner length L     5 / 5
    L with parity       7 / 7
    L+S+T              10 / 9
    NISS@DR            10 / 11
    + H-perm parity    11 / 12
    everything         13 / 13
    optimal            13

So 13 is optimal, and the last level proves it without picking a skeleton.

**His 4a4 example:**

    U R2 L2 F2 U' B2 D2 F2 D L2 U B2 R2 U' F2 U   // 4a4 on normal, 4b4 on inverse, 4e

    HTR 11 / 10,  L 11 / 11,  L+S+T 13 / 11,  NISS@DR 13 / 12,  optimal 13

Here plain NISS@DR on the normal side already says 13. His 13-mover is optimal, read off a 4qt DR.

**Levi's example** (from his DR Bounding doc), the 10-move 3qt DR `(D2 B' L' B U' F2 D L U2 R)`: subset 4c3 4e, HTR 9 / 10, NISS@DR 12 / 12, everything 14 / 14, optimal DR finish 15. Levi says "14-move optimal finish, giving a 24". Both are right: the DR ends in R, a finish that ends on that face merges with it, and the same DR with R' instead has optimal 14. The tool prints both.

None of this is something you can do at the table, and that's the point of keeping it. Compare with section 3: everything readable put together rules out 24% of 4qt and 45% of 5qt DRs for a 12. A table that sees the corners exactly and the colours of the edges proves it for 81% and 95%. The difference is not a feature anyone forgot to count. It's the exact relation between the corner state and where each edge sits, the thing you get from picking a skeleton and tracing. So a real hand bound at 4–5qt would have to be a faster way of doing what Rodney's method does per skeleton, across all skeletons at once. Whether NISS@DR has a description compact enough for that, I don't know. The tables to test a guess against exist now.

---

## 8. What I'd do per subset

This table is the short version of the whole doc, so it's long. Read these first, they apply to every row.

- **"In 12" and "in 13"** mean the share of all DR states of that kind whose optimal finish, in DR moves, is 12 or less, or 13 or less. Whether a 12 is good depends on your DR: your solution is the DR length plus the finish (one less if the first finish move merges with the last DR move).
- **They are odds, not guarantees.** The only guarantee in the table is the parity bound (no finish shorter than the best corner solution with the right number of side turns) and the few places that say "never".
- **"Drop" means "spend your time somewhere else first".** It doesn't mean unsolvable, and with a short enough DR or nothing better on the page you come back to it.
- **No row says a subset is bad to *try*.** The rows say how often each kind finishes short and which reads change that.
- **HTR numbers are for the true shortest HTR on each side.** If the one you found isn't the shortest, your DR is in a better cell than you think.
- **L is the optimal corner solution**, not the first corner solution you found.
- **Pairs** are true pairs: corner and edge next to each other in the U or D layer, both touching stickers matching.
- **Edge count.** The second column splits every subset by its number of bad edges. In the third column a read is given per edge count wherever the edge count changes it, and the cell says so where it doesn't. *Where* the bad edges sit is not a read in this table: I only measured it through the HTR length.
- **Corner cases** are named by where the bad corners sit, counted up to turning a layer. "A qt goes straight to X" means some U or D quarter turn lowers the corner qt count right away, with no setup.
- Shares like "a third of 4c3" are of all DR states of that corner subset.

| Subset | How it finishes | What to read, and what each read changes | When to drop it, and what not to conclude |
|---|---|---|---|
| **0c0**<br>0.5% of all DRs<br>average 12.28 | Depends almost only on the bad edges.<br>0e: 99% in 12 (these are HTR states and their U D' turns).<br>2e: 80% in 12, 99% in 13.<br>4e: 53% in 12, 93% in 13.<br>6e: 27% in 12, 75% in 13.<br>8e: 39% in 12, 78% in 13. | **Pairs**, per edge count: with 2e, 67% in 12 with none and 86% with five or more. With 4e, 40% and 74%. With 6e, 19% with none and 35% with two.<br>**HTR length** adds nothing once you know the edge count. With 2e the longer side is always 5 or 6 (82% and 79% in 12). With 4e it's 5, 6 or 7 (59%, 52%, 53%). With 6e it's 7 or 8 (28% and 27%).<br>**Corners**: one case only, nothing to read.<br>**Parity**: L is 0–5, and the wrong E-parity costs +2 or more for three corner states in four, so check it before trusting a short corner solution.<br>For 6e and 8e, go for the setup to a quarter turn first (Rodney's examples in [Rodney, 23 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1563054901871902741)). | Never because of the subset. The weakest is 6e with no pairs: still 19% in 12 and 67% in 13.<br>**Don't conclude** that "0" means no quarter turns: every 0c0 with bad edges needs two. The shortest 0c0 2e is `D F2 R2 F2 D`, solved by `D' F2 R2 F2 D'`. |
| **4a1**<br>2.9% of all DRs<br>average 12.42 | 4e: 53% in 12, 91% in 13 (average 12.27).<br>2e: 42% in 12, 88% in 13 (average 12.56).<br>0e: 24% in 12, 70% in 13 (average 13.01, and only 3% of 4a1).<br>Only 4e can be finished with one quarter turn. 2e and 0e need three. | **Pairs**: with 4e, 38% in 12 with none and 84% with five or more. With 2e, 27% and 69%.<br>**Longer HTR**: with 4e, 5 gives 81% in 12, 6 gives 67%, 7 gives 47%, 8 gives 32%. With 2e, 6 gives 59%, 7 gives 46%, 8 gives 34%.<br>**Corners**: four cases. With 4e they barely differ (50% to 56% in 12). With 2e they do: 50% for all four on one layer (L 1–4) down to 35% for the L 4–7 case, and 22% with that case on both sides.<br>**Levi's formula (4e only)**: shortest *1qt* HTR on normal + on inverse − 1. It bounds the finishes with one quarter turn. For one case in six the shortest HTR is a 3qt one, and the formula wants the 1qt length. A 3qt finish is shorter than the formula 11.7% of the time (2.5% when the formula says 12 or less). | Rarely. 4a1 0e is the weak one.<br>**Don't conclude** that 4a1 2e or 0e are bad DRs: 2e is one of the better subsets. Levi's formula doesn't apply to them, that's all.<br>**Don't forget** the 3qt finishes on 4e. When a 4a1 4e is very blocky and the formula still says 10+, look for one: `U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2` has formula 10 and a 3qt finish in 7 (`U B2 L2 F2 D F2 D`).<br>2e and 0e really need three quarter turns: `D F2 U' B2 F2 D'` (4a1 2e) is solved by `D F2 B2 U F2 D'`, and `U L2 R2 U L2 R2 U'` (4a1 0e) by `U R2 L2 U' R2 L2 U'`. |
| **4a2**<br>2.9% of all DRs<br>average 13.35 | 4e: 26% in 12, 64% in 13.<br>2e: 10% in 12, 39% in 13.<br>0e: 6% in 12, 29% in 13.<br>So 4a2 2e and 0e finish like a 2c4, not like a 2qt. | **Corners** carry the most. Best case: 2-2, each layer's pair on a diagonal, L 5–8, a qt goes straight to 4a1. Worst case: all four on one layer, L 8–11. With 4e: 41% in 12 and 81% in 13 for the best, 16% and 47% for the worst, 53% and 89% for the best on both sides, 4% and 24% for the worst on both sides. With 2e: 21% and 64% for the best, 3% and 19% for the worst, 34% and 77% for the best on both sides, and for the worst on both sides no 12 at all and 1% in 13.<br>**Longer HTR**: with 4e, 7 gives 59% in 12, 8 gives 36%, 9 gives 20%, 10 gives 10%, 11 gives 7%. With 2e it is almost always 9 or more: 9 gives 21%, 10 gives 8%, 11 gives 3% (21% in 13).<br>**Pairs**: with 4e, 21% in 12 with none and 37% with five or more. With 2e, 5% and 19%.<br>**Method**: 4a2 4e is where Levi's bounding and Rodney's rules work best. Use them. | 10 or more to HTR on both sides (12% of 4a2): 0.6–2% in 12, 8–17% in 13.<br>The worst corner case on both sides, above all with 2e (no 12, 1% in 13).<br>**Don't conclude** that 2qt means good. On average 4a2 finishes worse than 2c3 and 4b2 (18% in 12 against 28% and 37%). |
| **4b2**<br>11.4% of all DRs<br>average 12.68 | Flat across edges.<br>2e: 39% in 12, 85% in 13.<br>4e: 34% in 12, 82% in 13.<br>0e: 29% in 12, 74% in 13. | **Pairs** are the best read here: 23% in 12 with none, 65% with five or more (27% and 70% with 2e, 20% and 62% with 4e).<br>**Corners**: four cases. 2-2 with L 3–6 (a qt goes straight to 4a1) 44% in 12. 3-1 with L 4–7 40%. 3-1 with L 5–8 33%. 2-2 with L 6–9 30%. Best on both sides 50%, worst on both sides 21%. A few points higher with 2e than with 4e throughout.<br>**Longer HTR** has to be read with the edge count, because 4e HTRs run a move longer. With 2e: 6 gives 48% in 12, 7 gives 34%, 8 gives 24%. With 4e: 7 gives 49%, 8 gives 33%, 9 gives 22%.<br>**Method**: Rodney's, as written. | There is no dead corner of 4b2. The worst cells (8 and 9 to HTR) are still 15% in 12 and 63% in 13.<br>**Don't conclude** that a short HTR means a short finish. Example 10 in the examples file has a 4-move HTR, sits in an 85%-in-12 cell, and is a 13. |
| **2c3**<br>15.2% of all DRs<br>average 12.92 | The edge count matters a lot.<br>2e: 42% in 12, 88% in 13.<br>4e: 27% in 12, 73% in 13.<br>6e: 17% in 12, 61% in 13.<br>0e: 12% in 12, 52% in 13.<br>8e: 10% in 12, 45% in 13.<br>(0e and 8e are 1% of 2c3 each.) | **Corners**: three cases. Stacked (one above the other), L 5–8, a qt goes straight to 4b2. Opposite corners of the cube, L 5–8, also straight to 4b2. Next to each other on one layer, L 6–9, needs a setup (half of all 2c3). Share in 12 for stacked / opposite / adjacent: 52% / 44% / 36% with 2e, 36% / 28% / 21% with 4e, 26% / 19% / 12% with 6e. Stacked on both sides: 59%, 44%, 35% with 2e, 4e, 6e. Adjacent on both sides (a quarter of 2c3): 29%, 16%, 8%.<br>**Pairs**, none against five or more: 30% and 63% in 12 with 2e, 16% and 51% with 4e, 11% and 36% with 6e.<br>**Longer HTR**: with 4e, 7 gives 35% in 12, 8 gives 24%, 9 gives 14%. With 6e, 8 gives 19% and 9 gives 14%. With 2e it's 6 (52%) or 7 (40%).<br>**Parity**: for half of all 2c3 corner states the wrong E-parity costs +2, so the corner solution you like may be two moves short of reality.<br>**Method**: Rodney's. | Nothing is dead. Least promising: 6e with adjacent corners on both sides (8% in 12, 41% in 13).<br>**Don't conclude** that stacked corners are bad. At 3qt stacked is the *best* layout. It's at 4qt and 5qt that stacked is the worst. |
| **4c3**<br>(4a3 and 4b3)<br>11.4% of all DRs<br>average 13.49 | Flat across edges.<br>4e: 12% in 12, 45% in 13.<br>2e: 12% in 12, 46% in 13.<br>0e: 17% in 12, 54% in 13. | **Corners** carry the most, and which 4a3 you have is the big one. 4a3 that is 2-2 with L 7–9 and a qt straight to 4b2 (two such cases): 18–22% in 12, 60–68% in 13. 4b3 (3-1, a third of all 4c3): 11% and 45%. 4a3 with L 9–11: 3.6% and 22%. 4a3 with all four on one layer and L 9–10: 5.1% and 28%. Both sides: 23% in 12 for the best pair of cases, 3.0% for the worst (and the worst pair is 11% of all 4c3).<br>**HTR on both sides**: 7 and 8 gives 34% in 12. 8 and 9 gives 16% (56% in 13). 9 and 9 gives 9.4% (43%). 9 and 10 gives 5.0% (31%). 10 and 10 gives 1.9% (17%). The same length is worth a little more with 4e than with 2e (longer side 9: 17% in 12 with 4e, 12% with 2e), because 4e HTRs run about a move longer.<br>**Pairs**: 7% with none, 27% with five or more.<br>Corners and pairs read the same at 2e and 4e. | For a 12: 10 to HTR on both sides, or 9 and 10 with nothing else going for it. For a 13 nothing is dead; 10 and 10 is still 17%.<br>**Zagros's rule** (9+ on both sides, toss) drops half of all 4c3 and keeps 73% of the 12s.<br>**Don't conclude** that the rule is free: 6.4% of what it drops finishes in 12 and 34% in 13. `U' L2 D' B2 U' B2 U L2 D` is 9 to HTR on both sides and finishes in 9. |
| **0c3**<br>1.4% of all DRs<br>average 14.46 | The worst subset on average, worse than 5qt.<br>4e (half of 0c3): 1.5% in 12, 9% in 13.<br>2e and 6e: 3.7% in 12, 17–18% in 13.<br>0e and 8e: 5.6% in 12, 25% in 13. | **Longer HTR** is the read, and it has to be read with the edge count. With 4e the longer side is 11 (one in seven: 6% in 12, 19% in 13), 12 (most of them: 1% and 8%) or 13 (one in seven: no 12, 1% in 13). With 2e or 6e it is 10 (two thirds: 4% and 19%) or 11 (a third: 1% and 12%). So an 11 is the best case with 4e and the worst with 2e or 6e.<br>**Corners**: two cases, both with no bad corners. If a qt goes straight to 4a2 (a third of 0c3): 5% in 12 and 22% in 13 with 2e or 6e, 2% and 13% with 4e. Otherwise 3% and 15%, or 1% and 7% with 4e.<br>**Pairs** barely move it: with 2e, 1% in 12 with none and 6% with five or more. With 4e, 1% and 2%.<br>**Parity**: the wrong E-parity always costs exactly +1. | By default. 0c3 4e with 12 or 13 on the longer side (six in seven of 0c3 4e) is at most 1% for a 12 and 8% for a 13.<br>**Don't conclude** that no bad corners means good corners. |
| **2c4**<br>22.9% of all DRs, the most common subset<br>average 13.65 | 2e: 12% in 12, 44% in 13.<br>4e: 9% in 12, 38% in 13.<br>6e: 8% in 12, 35% in 13.<br>0e: 20% in 12, 59% in 13.<br>8e: 4.5% in 12, 24% in 13.<br>(0e and 8e are 1% of 2c4 each.) | **Corners first**, seven cases. Next to each other on one layer with a qt straight to 2c3 (two cases, L 7–10): 16% and 12.5% in 12. Opposite corners with a qt straight to 4b3 (L 8–10): 13%. The other two non-stacked cases need a setup: 6–7%. Stacked (one above the other): 7% if a qt goes straight to 4b3, 4% if not. Both sides: 26% in 12 and 75% in 13 for the best layout on both, 15–23% for other straight-to-2c3 or 4b3 pairs, 0.6–2.5% in 12 for a stack on both sides. This holds at every edge count to within a few points: the best layout on both sides is 31% in 12 with 2e, 25% with 4e, 24% with 6e, and a stack on both sides is 1% or less at all three.<br>**Pairs**: 4% with none, 26% with five or more, the same at 2e, 4e and 6e.<br>**HTR on both sides**: 7 and 8 gives 29% in 12. 8 and 8 gives 20%. 8 and 9 gives 12%. 9 and 9 gives 6.1% (32% in 13). 9 and 10 gives 3.1% (22%). 10 and 10 gives 0.9% (11%). Within two or three points of this at 2e, 4e and 6e.<br>**Parity** (if the corner solutions are written down): for 2c4 4e, L = 12 with an odd E-slice has no 12 at all, and L of 11 or more is about 2%. | A stack on both sides (the fastest any of them finishes is 11: `U2 L2 D' F2 U' R2 U F2 D L2 U2`). 10 to HTR on both sides. No pairs and nothing else going for it.<br>**Don't conclude** that 2c4 is bad as a subset. The best layouts are as good as an average 2c3 4e, and 2c4 is where reading pays the most, because the spread inside it is the widest (0.6% to 26%).<br>**Don't conclude** that 6e is a discard on its own: it's 8% in 12 against 9% for 4e. 8e is worse (4.5%). |
| **0c4**<br>1.0% of all DRs<br>average 13.67 | Finishes like an average 2c4.<br>2e: 9% in 12, 44% in 13.<br>4e: 7% in 12, 37% in 13.<br>6e: 3.6% in 12, 24% in 13. | **Pairs** are the only read with much in it: about 3% in 12 with none and 15–17% with five or more, at 2e and 4e alike. With 6e, 2% with none and 5% with two.<br>**HTR** is always 9 or 10 on each side and tells you nothing beyond the edge count: with 2e, 9 and 10 both give 9% in 12 and 44% in 13, and with 6e it's always 10.<br>**Corners**: one case, L is always 9 or 10, and the wrong E-parity always costs +1. | 6e or 8e, or no pairs.<br>**Don't conclude** anything from the corners here, there's nothing to tell apart. |
| **4c4**<br>(4a4 and 4b4)<br>11.4% of all DRs<br>average 14.40 | Flat across edges: 1.2–1.8% in 12, 9–12% in 13. | **Corners**: best case (2-2, each layer's pair on a diagonal, L 9–10, a qt straight to 4a3) 4.3% in 12 and 23% in 13. The two worst (L 11–12) 0.6% and 6%. Best pair of cases on both sides 5.6% and 28%. Worst pair 0.2% and 4%.<br>**Longer HTR**: 10 gives 3.5% in 12 and 19% in 13. 11 (two thirds of 4c4) gives 1.2% and 9%. 12 gives 0.3% and 4%.<br>**Pairs**: 0.7% with none, 5.0% in 12 and 25% in 13 with five or more.<br>All of this reads the same at 2e and 4e. | By default. It takes a short DR *and* something going for it (five pairs, or 9 and 10 to HTR, or the best corners), and then it's about 5% for a 12 and 25% for a 13.<br>11 to HTR on both sides: 0.4% in 12, 6% in 13.<br>**Don't conclude** from examples 2 and 9 in the examples file that 4c4 comes good. Those were a 10% and a 3% outcome. |
| **2c5**<br>7.6% of all DRs<br>average 14.33 | Flat across edges: 1.5–2.6% in 12, 11–16% in 13. | **Corners**: next to each other on one layer (half of 2c5) 3.4% in 12 and 19% in 13. Opposite corners 1.9% and 13%. Stacked 0.6% and 6%. Adjacent on both sides (a quarter of 2c5) 4.7% and 25%. **Stacked on both sides: never a 12, 0.6% in 13** (the fastest is 13: `U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2`). Stacked on one side and opposite on the other: 0.2% and 4.5%.<br>**Pairs**: 0.7% with none, 9% in 12 and 35% in 13 with five or more.<br>**Longer HTR**: 9 (2% of 2c5) gives 13% in 12 and 47% in 13. 10 gives 4.0% and 23%. 11 gives 1.2% and 10%. 12 gives 0.3% and 4%.<br>**Parity**: this is where the parity bound does the most. It proves "no 12" outright for 13% of 5qt DRs.<br>The reads are about the same at 2e, 4e and 6e, a little lower with 6e. | By default, and at once with a stack on both sides, a stack plus opposite, or 11 to HTR on both sides (0.1% in 12, 3% in 13).<br>Worth a look with a short DR and five pairs, or adjacent corners on both sides with 9 or 10 to HTR.<br>**Don't conclude** that "5qt, skip" loses nothing: one 2c5 in seven finishes in 13. |
| **4b5**<br>11.4% of all DRs<br>average 14.28 | Flat across edges: 1.8–2.0% in 12, 13–14% in 13. | **Pairs** are the only read that does anything: 0.5% in 12 with none, 8% in 12 and 34% in 13 with five or more.<br>**Corners**: two cases. 3-1 with a qt straight to 2c4 (two thirds) 2.2% and 15%. 2-2 with a qt straight to 4a4 1.3% and 11%.<br>**HTR**: 9, 10 or 11 on each side. 9 and 9 gives 3.5% in 12, 11 and 11 gives 0.4% (7% in 13).<br>The same at 2e and 4e. | By default. Unlike 2c5 there is no layout that kills it or saves it. A short DR with four or five pairs is the only case for it.<br>**Don't conclude** that 4b5 and 2c5 read the same way: 2c5 has the stacked-corner rule, 4b5 has nothing like it. |

On top of any row: an invertible last DR move is worth a third of a move on average, in every subset, so read the DR both ways (example 3 in the examples file). And if a row's reads disagree with each other, that's normal: together they explain about half of what there is to know.

---

## 9. The 216 NISS@1qt cases, three ways

FakeMMAP's first table is HT only. He then added HTR-breaking finishes from a list of algs, said ≤ 7 was proven and 8/9/10 might secretly be 7-movers ([FakeMMAP, 6 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546263650015256606), [FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546599572644696075)), and of the newer OBL++ sheet that he's "not mathematically 100% sure" ([FakeMMAP, 10 Nov 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1569733928988704873)). Rodney's "Adv DR Bounding" sheet uses those optimals.

Here are all three (the full table is Appendix C):

| Moves allowed | How | Result |
|---|---|---|
| Half turns | BFS over the 216 cases | same as FakeMMAP's listing, all 216 (proven in Lean) |
| DR moves | same BFS with U and D qts | 214 the same, 2 shorter: "R-D − F-V R-V even" and its mirror "F-D − F-V R-V even" go from 9 to 8 (the count of 2 is proven in Lean) |
| Any face turn (HTM) | every sequence of ≤ 10 moves is two sequences of ≤ 5 glued together, so I listed all 624,124 of those twice, matched the pairs that can land in HTR, and tested each hit | vs DR moves: 150 the same, 37 shorter by 1, 22 by 2, 6 by 3, 1 by 4. (vs half turns: 150 / 35 / 24 / 6 / 1.) |

DR-move values never go above 10, so anything shorter is ≤ 9 moves and a search that's complete to 10 can't miss it. Against that:

The two that get shorter with quarter turns, explicitly. `L2 B2 D B2 L2 R2 F2 U'` is a state of "R-D − F-V R-V even", and `U F2 R2 L2 B2 D' B2 L2` solves it in 8. `B2 L2 D L2 B2 F2 R2 U'` is a state of "F-D − F-V R-V even", and `U R2 F2 B2 L2 D' L2 B2` solves it in 8. With half turns alone both cases need 9.

- **FakeMMAP's HTR-breaking table ([FakeMMAP, 7 Sep 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1546599572644696075)) is right in 211 of 216 cells and one too high in 5.** Two of those were labelled 7 and are 6-movers, so "7 or less is proven optimal" doesn't hold for them.

  | Case | His | Real | A state of that case |
  |---|---:|---:|---|
  | F-D + F-V R-H odd | 7 | 6 | `R L' B2 D2 R L'` |
  | R-D + F-H R-V odd | 7 | 6 | `F' B R2 D2 F B'` |
  | H-H + F-D R-D odd | 9 | 8 | `R D2 F2 B2 R' L F2 R'` |
  | H-H + F-V R-D odd | 9 | 8 | `L' F2 R L' F2 B2 D2 L` |
  | H-H + F-D R-V odd | 9 | 8 | `F L2 F B' R2 L2 D2 F'` |

  (The inverse of each sequence solves it.)
- **Rodney's sheet** uses the same optimals, so same five, the other 211 agree. One more row, labelled F-V / F-D / R-H, lists `M R2 U2 M'`, which actually gives a different case (R-V + F-D R-V odd). `M F2 U2 M'` gives the labelled case in the 6 moves the sheet says, so the R2 is a typo for F2.
- **Rodney's rules are still a true lower bound in all 216 cases**, even against the shorter optimals. The "100%" survives.
- **OBL++** has a finer grid and I didn't grade it cell by cell. Collapsed to these 216 labels it matches on 140 of the 144 cases it covers, already has four of the five fixes above, and is one *lower* in four (D-D ± F-H R-H even, R-V + F-D R-H even, R-V + F-D R-D odd: 8 vs my 9). For those four I ran nissy on all 3,072 states of each case and none has a solution of 8 or fewer. So 9 stands for the cases as I label them. Whether those cells are off or just mean something slightly different, I don't know.

Two sanity checks on my side: listing the HTR group directly gives 663,552 states in 216 cases of exactly 3,072 each, and all 216 sequences in Appendix C land in the case they claim.

This part is a Python script, not Lean. Nothing in either sheet beats its values, including Rodney's `F R2 E2 R2 F'` algs.

---

## 10. The proof, if you don't speak Lean

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

## 11. How it was computed and checked

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
| FakeMMAP's corner counts per qt, 24 / 144 / 720 / 1416 / 1776 / 960 of 5040 ([FakeMMAP, 26 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1144917908078723112), he asked someone to check them) | confirmed |
| Lean's proven optimal table vs the Rust BFS | same in all 1,339,269,120 entries, and the same depth distribution |
| Lean vs the Rust program, bound tables | same case counts (96, 420, 70, 5040, 630, 10080), same distribution of the corner and HTR tables, same bounds on the examples |
| Rust vs the first C version | every output byte-identical |
| nissy `drudfin` on 40 random DRs | same optimal on all 40 |
| Bounds vs optimal | never above it, any level, any of the 19.5 billion states |

For the hand reads in sections 3 to 6:

- **Leave slice**: a second BFS over corners and U/D-layer edges only, reduced by the same 16 symmetries (111,605,760 reduced states, five seconds). It reaches all 19,508,428,800 states when each is counted with its 12 E-slice arrangements.
- **The reads**: three more passes over all DR states. Each computes the read for the state (and for its inverse where that's a different thing) and adds the state's optimal to a histogram. Every pass counts exactly 19,508,428,800 states.
- **Pairs**: the four kinds are defined by the colours of the two touching sticker pairs, as in Rodney's message. Checked on his example: after `B2 L2 B2 R2` the UF edge has a top semi-pair on one side and a side semi-pair on the other, which is what he says it sets up.
- **Corner cases**: classes of the 420 HTR corner cosets under the 16 symmetries and under turning both layers. There are 46.
- **Setup lengths** for the setup + HTR bound: breadth-first over the 29,400 HTR cosets with half turns only, until some quarter turn lowers the minimum qt count. At 1qt it has to give the shortest 1qt HTR minus one, and it does.
- **Example scrambles**: every scramble quoted as an example of something was found by a search over all DR states, then re-read from its text alone (subset, HTR lengths, leave slice and optimal recomputed from the moves). The ones that stand against something a person wrote were also solved with nissy.
- **What the server has said**: all of #fmc-theory and #fmc-discussion (about 33,000 messages, August 2022 to November 2026) was reread line by line for this version, looking for what people read off a DR, how they discard, and what they asked for. Every quote above was checked against the export.

---

## 12. What this doesn't do

- **DR moves only.** "Optimal" here is U, D, R2, L2, F2, B2. DR-breaking finishes can be shorter: at the HTR level that's 66 of the 216 cases.
- **Uniform states.** Every DR state counts once. The DRs you actually reach are spread differently over the subsets, so use the per-subset numbers, not the "all DRs" ones, for a decision.
- **No hand bound for 4–5qt.** That was the hope and it isn't here. What's here is the measurement that says a feature count won't give one, the reads ranked by what they buy, and the kill rules that do exist.
- **Reads I didn't test.** Bigger blocks than pairs, anything you only see after a few moves (moves to FR, the shape after the first qt), and Rodney's NISS@1qt features per skeleton, which is section 7's table rather than a read.
- **Width is only first moves.** JTuu's real question, how many finishes are within one of optimal, needs a count of solutions per state. Not done.
- **Not done either**: what share of DRs have an optimal finish that goes through a shortest HTR ([Zagros, 27 Dec 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1454570265353912422)), and how many U2/D2 an optimal has per subset ([wen, 8 May 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1502269153774669904)).
- **Stats are counted, not proven.** The optimal of every state is a Lean theorem, and the table the stats are counted from is that same table, entry for entry. What isn't formal is the counting on top: the percentages, the reads, and the symmetry weights behind "1,352 states at 18".

---

## Appendix A: all 48 subsets

Exact over all DR states. "Proves 13+" = share of the subset where that level, on the better of normal and inverse, shows there is no 12-move finish.

| Subset | Share of all DRs | Avg optimal | Min | Longest | ≤ 12 | ≤ 13 | L+parity proves 13+ | NISS@DR proves 13+ | Everything proves 13+ | Everything proves 14+ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0c0 0e | 0.01% | 9.95 | 0 | 13 | 99.2% | 100.0% | 0% | 0% | 0% | 0% |
| 0c0 2e | 0.11% | 11.69 | 5 | 15 | 79.9% | 99.0% | 0% | 0% | 1% | 0% |
| 0c0 4e | 0.24% | 12.31 | 4 | 16 | 53.1% | 92.5% | 0% | 0% | 8% | 0% |
| 0c0 6e | 0.11% | 12.92 | 7 | 16 | 27.0% | 75.2% | 0% | 1% | 21% | 1% |
| 0c0 8e | 0.01% | 12.69 | 6 | 18 | 38.6% | 78.0% | 0% | 3% | 20% | 3% |
| 4a1 0e | 0.08% | 13.01 | 7 | 16 | 24.0% | 70.3% | 0% | 12% | 43% | 6% |
| 4a1 2e | 1.31% | 12.56 | 6 | 16 | 42.3% | 87.8% | 0% | 0% | 11% | 0% |
| 4a1 4e | 1.47% | 12.27 | 1 | 17 | 53.2% | 91.1% | 0% | 0% | 9% | 0% |
| 4a2 0e | 0.08% | 13.91 | 9 | 17 | 6.1% | 28.5% | 0% | 57% | 84% | 48% |
| 4a2 2e | 1.31% | 13.65 | 8 | 17 | 10.0% | 39.5% | 0% | 28% | 69% | 28% |
| 4a2 4e | 1.47% | 13.05 | 5 | 16 | 26.4% | 63.7% | 0% | 16% | 46% | 13% |
| 4b2 0e | 0.33% | 12.89 | 6 | 16 | 28.5% | 74.3% | 0% | 1% | 33% | 2% |
| 4b2 2e | 5.22% | 12.61 | 3 | 16 | 39.3% | 84.9% | 0% | 0% | 15% | 0% |
| 4b2 4e | 5.88% | 12.73 | 4 | 16 | 34.4% | 81.9% | 0% | 0% | 21% | 0% |
| 0c3 0e | 0.02% | 14.08 | 10 | 17 | 5.7% | 25.9% | 14% | 80% | 86% | 61% |
| 0c3 2e | 0.33% | 14.27 | 9 | 17 | 3.7% | 17.4% | 14% | 67% | 93% | 71% |
| 0c3 4e | 0.73% | 14.64 | 10 | 18 | 1.5% | 8.9% | 14% | 93% | 96% | 83% |
| 0c3 6e | 0.33% | 14.29 | 9 | 17 | 3.7% | 17.6% | 14% | 66% | 93% | 71% |
| 0c3 8e | 0.02% | 14.14 | 10 | 17 | 5.6% | 24.8% | 14% | 80% | 86% | 62% |
| 2c3 0e | 0.22% | 13.39 | 9 | 16 | 12.4% | 51.9% | 0% | 11% | 63% | 13% |
| 2c3 2e | 3.48% | 12.55 | 5 | 15 | 42.0% | 87.9% | 0% | 0% | 10% | 0% |
| 2c3 4e | 7.84% | 12.94 | 5 | 16 | 26.7% | 72.5% | 0% | 0% | 31% | 1% |
| 2c3 6e | 3.48% | 13.20 | 7 | 16 | 17.4% | 61.1% | 0% | 0% | 45% | 2% |
| 2c3 8e | 0.22% | 13.52 | 9 | 16 | 9.6% | 44.8% | 0% | 11% | 67% | 15% |
| 4c3 0e | 0.33% | 13.31 | 8 | 16 | 17.0% | 54.1% | 0% | 16% | 58% | 17% |
| 4c3 2e | 5.22% | 13.48 | 7 | 16 | 12.0% | 45.8% | 0% | 9% | 67% | 18% |
| 4c3 4e | 5.88% | 13.50 | 7 | 16 | 12.0% | 45.3% | 0% | 14% | 68% | 20% |
| 0c4 0e | 0.01% | 13.22 | 9 | 16 | 17.4% | 60.7% | 0% | 0% | 46% | 2% |
| 0c4 2e | 0.22% | 13.52 | 9 | 16 | 8.9% | 43.8% | 0% | 4% | 77% | 11% |
| 0c4 4e | 0.49% | 13.64 | 9 | 16 | 6.9% | 37.2% | 0% | 9% | 82% | 16% |
| 0c4 6e | 0.22% | 13.90 | 10 | 16 | 3.6% | 24.5% | 0% | 27% | 90% | 35% |
| 0c4 8e | 0.01% | 14.18 | 11 | 16 | 1.9% | 15.6% | 0% | 56% | 92% | 51% |
| 2c4 0e | 0.33% | 13.22 | 7 | 16 | 20.0% | 58.5% | 1% | 15% | 50% | 12% |
| 2c4 2e | 5.22% | 13.53 | 7 | 17 | 11.5% | 44.1% | 1% | 12% | 68% | 20% |
| 2c4 4e | 11.76% | 13.66 | 7 | 16 | 9.1% | 37.9% | 1% | 18% | 74% | 26% |
| 2c4 6e | 5.22% | 13.73 | 8 | 17 | 7.7% | 34.9% | 1% | 20% | 78% | 30% |
| 2c4 8e | 0.33% | 14.02 | 9 | 17 | 4.5% | 24.1% | 1% | 47% | 83% | 44% |
| 4c4 0e | 0.33% | 14.54 | 10 | 17 | 1.2% | 8.8% | 14% | 75% | 96% | 76% |
| 4c4 2e | 5.22% | 14.42 | 9 | 17 | 1.5% | 10.6% | 14% | 71% | 97% | 76% |
| 4c4 4e | 5.88% | 14.38 | 9 | 17 | 1.8% | 11.8% | 14% | 67% | 97% | 73% |
| 2c5 0e | 0.11% | 14.42 | 10 | 18 | 1.5% | 11.4% | 22% | 78% | 95% | 71% |
| 2c5 2e | 1.74% | 14.28 | 9 | 17 | 2.5% | 15.5% | 22% | 59% | 93% | 62% |
| 2c5 4e | 3.92% | 14.30 | 9 | 18 | 2.6% | 15.3% | 22% | 61% | 93% | 63% |
| 2c5 6e | 1.74% | 14.42 | 9 | 17 | 1.7% | 11.7% | 22% | 65% | 95% | 70% |
| 2c5 8e | 0.11% | 14.46 | 10 | 17 | 1.5% | 11.0% | 22% | 81% | 95% | 72% |
| 4b5 0e | 0.33% | 14.30 | 9 | 17 | 2.0% | 13.1% | 7% | 62% | 94% | 66% |
| 4b5 2e | 5.22% | 14.26 | 9 | 16 | 2.0% | 14.0% | 7% | 51% | 96% | 66% |
| 4b5 4e | 5.88% | 14.29 | 9 | 17 | 1.8% | 13.3% | 7% | 60% | 96% | 69% |

---

## Appendix B: odds by corner length and E-slice parity

For the big 3–5qt subsets. L = optimal corner solution. "Min" is the best case for that row, so `L+1` means no L-move finish exists there.

| Subset | L | E-slice | Share of subset | Min | Avg optimal | ≤ 12 | ≤ 13 |
|---|---:|---|---:|---|---:|---:|---:|
| 4c3 4e | 7 | even | 2.8% | 8 (L+1) | 13.03 | 22.0% | 67.7% |
| 4c3 4e | 7 | odd | 2.8% | 7 (L+0) | 12.95 | 28.8% | 69.7% |
| 4c3 4e | 8 | even | 11.1% | 8 (L+0) | 13.15 | 19.1% | 63.9% |
| 4c3 4e | 8 | odd | 11.1% | 9 (L+1) | 13.20 | 19.0% | 59.7% |
| 4c3 4e | 9 | even | 19.4% | 9 (L+0) | 13.43 | 10.8% | 49.0% |
| 4c3 4e | 9 | odd | 19.4% | 9 (L+0) | 13.45 | 13.2% | 47.4% |
| 4c3 4e | 10 | even | 13.9% | 11 (L+1) | 13.80 | 3.6% | 32.4% |
| 4c3 4e | 10 | odd | 13.9% | 10 (L+0) | 13.86 | 7.5% | 25.4% |
| 4c3 4e | 11 | even | 2.8% | 11 (L+0) | 14.05 | 2.5% | 16.9% |
| 4c3 4e | 11 | odd | 2.8% | 11 (L+0) | 14.13 | 2.8% | 21.1% |
| 0c3 4e | 9 | even | 2.8% | 11 (L+2) | 13.68 | 4.5% | 38.0% |
| 0c3 4e | 9 | odd | 2.8% | 10 (L+1) | 13.86 | 8.7% | 30.3% |
| 0c3 4e | 10 | even | 11.1% | 11 (L+1) | 14.22 | 0.9% | 22.1% |
| 0c3 4e | 10 | odd | 11.1% | 12 (L+2) | 14.16 | 6.5% | 10.0% |
| 0c3 4e | 11 | even | 22.2% | 12 (L+1) | 14.73 | 0.4% | 8.4% |
| 0c3 4e | 11 | odd | 22.2% | 12 (L+1) | 14.72 | 0.8% | 4.6% |
| 0c3 4e | 12 | even | 13.9% | 13 (L+1) | 14.96 | 0.0% | 0.2% |
| 0c3 4e | 12 | odd | 13.9% | 13 (L+1) | 15.09 | 0.0% | 4.0% |
| 2c4 4e | 7 | even | 2.8% | 8 (L+1) | 13.15 | 15.0% | 66.3% |
| 2c4 4e | 7 | odd | 2.8% | 7 (L+0) | 13.15 | 23.2% | 58.7% |
| 2c4 4e | 8 | even | 11.1% | 8 (L+0) | 13.29 | 13.4% | 58.6% |
| 2c4 4e | 8 | odd | 11.1% | 9 (L+1) | 13.37 | 16.6% | 49.4% |
| 2c4 4e | 9 | even | 17.0% | 9 (L+0) | 13.61 | 6.6% | 41.1% |
| 2c4 4e | 9 | odd | 17.0% | 9 (L+0) | 13.58 | 11.4% | 38.8% |
| 2c4 4e | 10 | even | 13.2% | 10 (L+0) | 13.84 | 3.9% | 30.8% |
| 2c4 4e | 10 | odd | 13.2% | 10 (L+0) | 13.90 | 6.5% | 23.7% |
| 2c4 4e | 11 | even | 5.2% | 11 (L+0) | 14.16 | 2.0% | 13.7% |
| 2c4 4e | 11 | odd | 5.2% | 11 (L+0) | 14.28 | 1.9% | 16.1% |
| 2c4 4e | 12 | even | 0.7% | 12 (L+0) | 14.37 | 1.6% | 2.8% |
| 2c4 4e | 12 | odd | 0.7% | 13 (L+1) | 14.55 | 0.0% | 12.3% |
| 4c4 4e | 9 | even | 2.8% | 9 (L+0) | 13.79 | 4.4% | 30.8% |
| 4c4 4e | 9 | odd | 2.8% | 10 (L+1) | 13.85 | 7.2% | 29.4% |
| 4c4 4e | 10 | even | 11.1% | 11 (L+1) | 14.03 | 2.9% | 21.1% |
| 4c4 4e | 10 | odd | 11.1% | 10 (L+0) | 14.05 | 4.5% | 18.8% |
| 4c4 4e | 11 | even | 22.2% | 11 (L+0) | 14.37 | 1.4% | 8.1% |
| 4c4 4e | 11 | odd | 22.2% | 11 (L+0) | 14.42 | 1.1% | 13.1% |
| 4c4 4e | 12 | even | 13.9% | 12 (L+0) | 14.68 | 0.6% | 1.6% |
| 4c4 4e | 12 | odd | 13.9% | 13 (L+1) | 14.79 | 0.0% | 5.8% |
| 0c4 4e | 9 | even | 16.7% | 9 (L+0) | 13.62 | 5.4% | 36.5% |
| 0c4 4e | 9 | odd | 16.7% | 10 (L+1) | 13.64 | 8.6% | 39.4% |
| 0c4 4e | 10 | even | 33.3% | 11 (L+1) | 13.62 | 5.6% | 36.7% |
| 0c4 4e | 10 | odd | 33.3% | 10 (L+0) | 13.67 | 8.1% | 37.0% |
| 2c5 4e | 9 | even | 4.2% | 9 (L+0) | 13.75 | 5.8% | 29.3% |
| 2c5 4e | 9 | odd | 4.2% | 10 (L+1) | 13.96 | 4.4% | 31.2% |
| 2c5 4e | 10 | even | 14.6% | 11 (L+1) | 14.04 | 3.7% | 16.0% |
| 2c5 4e | 10 | odd | 14.6% | 10 (L+0) | 13.96 | 6.1% | 26.6% |
| 2c5 4e | 11 | even | 17.2% | 11 (L+0) | 14.20 | 2.4% | 12.9% |
| 2c5 4e | 11 | odd | 17.2% | 11 (L+0) | 14.41 | 0.8% | 17.1% |
| 2c5 4e | 12 | even | 9.9% | 12 (L+0) | 14.49 | 1.3% | 2.4% |
| 2c5 4e | 12 | odd | 9.9% | 12 (L+0) | 14.64 | 0.2% | 10.6% |
| 2c5 4e | 13 | even | 4.2% | 13 (L+0) | 15.01 | 0.0% | 1.3% |
| 2c5 4e | 13 | odd | 4.2% | 13 (L+0) | 15.30 | 0.0% | 1.8% |
| 4b5 4e | 9 | even | 5.6% | 9 (L+0) | 13.96 | 3.9% | 17.0% |
| 4b5 4e | 9 | odd | 5.6% | 10 (L+1) | 14.16 | 2.0% | 25.6% |
| 4b5 4e | 10 | even | 20.8% | 11 (L+1) | 14.19 | 2.5% | 8.8% |
| 4b5 4e | 10 | odd | 20.8% | 10 (L+0) | 14.22 | 2.6% | 20.9% |
| 4b5 4e | 11 | even | 20.8% | 11 (L+0) | 14.31 | 1.5% | 8.5% |
| 4b5 4e | 11 | odd | 20.8% | 11 (L+0) | 14.52 | 0.4% | 12.7% |
| 4b5 4e | 12 | even | 2.8% | 12 (L+0) | 14.49 | 1.0% | 1.9% |
| 4b5 4e | 12 | odd | 2.8% | 12 (L+0) | 14.50 | 0.7% | 10.8% |

---

## Appendix C: the 216 NISS@1qt cases

Labels are FakeMMAP's (corner case with cs sign, M-slice edges, S-slice edges, E-parity). HT = half turns only (his first BFS), DR = DR moves, Any = any of the 18 face turns. The sequence makes a state of the case in "Any" moves, so its inverse is an optimal solution.

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

Each cell: share finishing in 12 / in 13 (%), for DRs of that subset with that many true pairs (corner + U/D-layer edge, both touching stickers matching, 16 places to look).

| Subset | 0 pairs | 1 | 2 | 3 | 4 | 5 | 6+ |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0c0 0e | 99.2 / 100 |  | 99.5 / 100 |  | 98.9 / 100 |  | 99.5 / 100 |
| 0c0 2e | 66.8 / 97 | 77.1 / 99 | 77.7 / 99 | 81.0 / 99 | 81.8 / 99 | 84.7 / 100 | 86.7 / 99 |
| 0c0 4e | 40.4 / 86 | 48.0 / 92 | 52.0 / 92 | 61.0 / 96 | 63.9 / 96 | 75.8 / 99 | 71.7 / 97 |
| 0c0 6e | 19.1 / 67 | 27.0 / 76 | 34.8 / 81 | 44.1 / 90 | 51.6 / 87 |  |  |
| 0c0 8e | 38.6 / 78 |  |  |  |  |  |  |
| 4a1 0e | 17.0 / 58 | 20.0 / 69 | 24.1 / 68 | 27.6 / 78 | 29.5 / 76 | 41.6 / 92 | 47.0 / 83 |
| 4a1 2e | 27.5 / 78 | 32.8 / 83 | 41.9 / 89 | 51.9 / 93 | 59.7 / 96 | 67.2 / 98 | 73.4 / 98 |
| 4a1 4e | 38.2 / 83 | 43.6 / 88 | 52.3 / 92 | 61.4 / 95 | 72.4 / 97 | 81.2 / 99 | 89.2 / 99 |
| 4a2 0e | 2.4 / 17 | 2.3 / 20 | 5.6 / 26 | 5.6 / 36 | 15.6 / 46 | 28.7 / 62 | 34.5 / 63 |
| 4a2 2e | 4.9 / 27 | 7.0 / 34 | 9.5 / 40 | 12.8 / 46 | 16.7 / 51 | 18.5 / 53 | 20.1 / 55 |
| 4a2 4e | 20.8 / 57 | 22.8 / 60 | 26.3 / 64 | 29.6 / 68 | 33.2 / 70 | 35.4 / 73 | 41.6 / 77 |
| 4b2 0e | 19.8 / 64 | 23.7 / 70 | 28.6 / 75 | 32.2 / 78 | 38.4 / 82 | 43.6 / 88 | 47.7 / 88 |
| 4b2 2e | 26.6 / 75 | 30.5 / 80 | 37.7 / 85 | 47.2 / 91 | 56.7 / 95 | 66.4 / 97 | 77.4 / 99 |
| 4b2 4e | 20.1 / 69 | 26.3 / 77 | 33.6 / 83 | 42.1 / 89 | 50.8 / 93 | 60.0 / 95 | 66.9 / 97 |
| 0c3 0e | 0.9 / 11 | 3.5 / 27 | 3.3 / 21 | 4.4 / 21 | 6.9 / 30 | 1.8 / 12 | 9.8 / 35 |
| 0c3 2e | 1.3 / 12 | 2.3 / 14 | 2.8 / 15 | 3.9 / 18 | 3.9 / 18 | 4.8 / 22 | 7.4 / 27 |
| 0c3 4e | 0.6 / 6 | 1.3 / 8 | 1.5 / 9 | 1.8 / 10 | 1.9 / 11 | 2.4 / 13 | 1.5 / 11 |
| 0c3 6e | 2.4 / 15 | 3.8 / 18 | 4.7 / 20 | 6.9 / 25 | 4.8 / 21 |  |  |
| 0c3 8e | 5.6 / 25 |  |  |  |  |  |  |
| 2c3 0e | 3.2 / 26 | 4.4 / 35 | 7.6 / 44 | 10.8 / 54 | 16.0 / 60 | 22.0 / 68 | 29.6 / 75 |
| 2c3 2e | 30.0 / 80 | 33.1 / 83 | 37.4 / 86 | 44.2 / 90 | 51.7 / 93 | 59.7 / 96 | 68.1 / 97 |
| 2c3 4e | 15.8 / 59 | 20.1 / 66 | 25.7 / 73 | 32.5 / 80 | 40.5 / 85 | 48.7 / 90 | 57.7 / 93 |
| 2c3 6e | 11.5 / 50 | 15.0 / 58 | 19.1 / 65 | 24.1 / 71 | 28.6 / 76 | 35.9 / 82 | 33.8 / 82 |
| 2c3 8e | 5.7 / 36 | 8.9 / 45 | 13.8 / 53 | 22.8 / 65 | 19.0 / 61 |  |  |
| 4c3 0e | 11.1 / 47 | 13.1 / 49 | 15.2 / 52 | 20.0 / 58 | 26.7 / 67 | 33.4 / 74 | 50.2 / 86 |
| 4c3 2e | 6.9 / 35 | 8.5 / 39 | 11.2 / 45 | 14.7 / 52 | 18.9 / 59 | 23.4 / 65 | 31.1 / 72 |
| 4c3 4e | 6.7 / 33 | 8.6 / 39 | 11.3 / 45 | 14.4 / 51 | 18.5 / 58 | 24.1 / 66 | 32.8 / 73 |
| 0c4 0e | 0.0 / 16 | 0.8 / 12 | 1.8 / 36 | 10.0 / 60 | 16.6 / 66 | 21.9 / 81 | 37.6 / 81 |
| 0c4 2e | 3.0 / 27 | 4.8 / 33 | 6.5 / 38 | 8.5 / 44 | 8.6 / 48 | 14.1 / 58 | 21.0 / 63 |
| 0c4 4e | 3.1 / 25 | 4.7 / 31 | 6.7 / 37 | 8.9 / 43 | 11.3 / 51 | 14.6 / 57 | 18.3 / 64 |
| 0c4 6e | 1.9 / 18 | 3.8 / 26 | 5.1 / 30 | 6.0 / 34 | 3.4 / 27 |  |  |
| 0c4 8e | 1.9 / 16 |  |  |  |  |  |  |
| 2c4 0e | 10.4 / 46 | 12.3 / 50 | 16.0 / 54 | 19.2 / 59 | 23.8 / 63 | 28.1 / 68 | 34.0 / 72 |
| 2c4 2e | 4.3 / 27 | 6.3 / 34 | 8.5 / 40 | 11.7 / 47 | 16.9 / 56 | 23.2 / 65 | 32.8 / 74 |
| 2c4 4e | 4.4 / 26 | 5.8 / 31 | 8.1 / 37 | 11.1 / 44 | 15.7 / 52 | 21.5 / 62 | 30.2 / 70 |
| 2c4 6e | 3.9 / 24 | 5.8 / 31 | 8.4 / 38 | 12.1 / 47 | 17.1 / 55 | 24.1 / 65 | 29.6 / 67 |
| 2c4 8e | 3.4 / 20 | 4.7 / 24 | 5.7 / 29 | 5.1 / 28 | 6.8 / 30 |  |  |
| 4c4 0e | 0.2 / 4 | 0.7 / 7 | 1.2 / 9 | 1.9 / 12 | 2.0 / 13 | 3.1 / 18 | 0.2 / 10 |
| 4c4 2e | 0.6 / 6 | 0.8 / 7 | 1.3 / 10 | 1.8 / 13 | 2.7 / 17 | 4.4 / 23 | 6.8 / 29 |
| 4c4 4e | 0.9 / 7 | 1.1 / 9 | 1.5 / 11 | 2.2 / 14 | 3.1 / 18 | 4.4 / 23 | 6.1 / 28 |
| 2c5 0e | 0.5 / 7 | 0.4 / 5 | 0.7 / 9 | 1.0 / 9 | 2.4 / 15 | 1.3 / 16 | 7.3 / 25 |
| 2c5 2e | 0.5 / 7 | 0.8 / 9 | 1.5 / 12 | 2.3 / 17 | 3.9 / 22 | 6.2 / 30 | 11.4 / 38 |
| 2c5 4e | 0.6 / 7 | 1.1 / 10 | 1.9 / 14 | 3.3 / 20 | 5.5 / 26 | 9.4 / 36 | 14.6 / 44 |
| 2c5 6e | 0.8 / 7 | 1.2 / 10 | 1.6 / 13 | 2.8 / 17 | 4.6 / 23 | 6.7 / 29 | 4.6 / 23 |
| 2c5 8e | 0.6 / 7 | 1.7 / 12 | 2.5 / 14 | 2.2 / 14 | 0.8 / 8 |  |  |
| 4b5 0e | 1.0 / 9 | 1.1 / 10 | 1.8 / 12 | 2.2 / 15 | 3.6 / 21 | 8.2 / 29 | 5.3 / 37 |
| 4b5 2e | 0.6 / 7 | 0.9 / 9 | 1.7 / 13 | 2.7 / 18 | 4.1 / 24 | 6.2 / 30 | 8.9 / 37 |
| 4b5 4e | 0.4 / 6 | 0.8 / 8 | 1.3 / 12 | 2.2 / 17 | 4.1 / 24 | 6.4 / 32 | 12.1 / 43 |
| share of DRs | 13.8% | 27.0% | 26.8% | 17.8% | 9.1% | 3.7% | 1.8% |

---

## Appendix E: the 46 corner cases

A corner case is what the corners look like up to rotation, mirror and turning a layer. "Bad corners" says where the bad ones sit for the example (fewest bad corners, shortest corner solution). L is the range of optimal corner solution lengths the case can have. The example scramble, done on a solved cube, gives a state of that case. "A qt takes it straight to" lists the corner subsets one U or D quarter turn can reach with one qt less. Shares are of the corner subset, all edge counts together; odds are for the full finish.

In the both-sides tables the two columns are the case on normal and on inverse, in either order.

**0c0**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 0c0-1 | none bad | 0–5 | `` | nothing (set up first) | 100.0% | 12.28 | 53.7% | 89.9% |

**4a1**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 4a1-1 | 4-0 | 1–4 | `D` | 0c0 | 16.7% | 12.30 | 52.5% | 90.7% |
| 4a1-2 | 2-2, pairs on opposite sides | 2–5 | `D B2` | nothing (set up first) | 33.3% | 12.36 | 50.1% | 90.7% |
| 4a1-3 | 2-2, pairs stacked | 3–6 | `D B2 D2` | nothing (set up first) | 33.3% | 12.48 | 44.7% | 88.1% |
| 4a1-4 | 2-2, diagonal over diagonal | 4–7 | `D' R2 D2 F2` | nothing (set up first) | 16.7% | 12.54 | 42.3% | 85.8% |

4a1, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---:|---:|---:|---:|
| 4a1-1 | 4a1-3 | 11.1% | 12.29 | 52.6% | 91.6% |
| 4a1-1 | 4a1-2 | 11.1% | 12.29 | 52.7% | 91.0% |
| 4a1-1 | 4a1-4 | 5.6% | 12.31 | 52.3% | 90.4% |
| 4a1-1 | 4a1-1 | 2.8% | 12.32 | 52.0% | 88.7% |
| 4a1-2 | 4a1-2 | 11.1% | 12.34 | 51.1% | 91.0% |
| 4a1-2 | 4a1-3 | 22.2% | 12.38 | 49.3% | 90.8% |
| 4a1-2 | 4a1-4 | 11.1% | 12.42 | 47.3% | 89.8% |
| 4a1-3 | 4a1-3 | 11.1% | 12.59 | 40.1% | 86.1% |
| 4a1-3 | 4a1-4 | 11.1% | 12.66 | 36.9% | 83.3% |
| 4a1-4 | 4a1-4 | 2.8% | 12.78 | 33.0% | 78.3% |

**4a2**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 4a2-1 | 2-2, diagonal over diagonal | 5–8 | `U R2 U2 F2 U` | 4a1 | 16.7% | 12.86 | 31.0% | 72.3% |
| 4a2-2 | 2-2, pairs stacked | 6–9 | `D' B2 D2 R2 U R2` | nothing (set up first) | 33.3% | 13.14 | 22.4% | 60.5% |
| 4a2-3 | 2-2, pairs on opposite sides | 7–10 | `U' R2 U2 F2 U R2 U2` | nothing (set up first) | 33.3% | 13.58 | 12.4% | 41.6% |
| 4a2-4 | 4-0 | 8–11 | `D R2 U2 F2 U F2 U2 R2` | nothing (set up first) | 16.7% | 13.80 | 9.3% | 33.4% |

4a2, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---:|---:|---:|---:|
| 4a2-1 | 4a2-1 | 2.8% | 12.54 | 43.4% | 83.0% |
| 4a2-2 | 4a2-1 | 11.1% | 12.71 | 35.4% | 78.5% |
| 4a2-2 | 4a2-2 | 11.1% | 12.97 | 27.3% | 68.0% |
| 4a2-3 | 4a2-1 | 11.1% | 13.02 | 25.5% | 66.3% |
| 4a2-4 | 4a2-1 | 5.6% | 13.16 | 20.9% | 60.9% |
| 4a2-2 | 4a2-3 | 22.2% | 13.33 | 16.0% | 52.8% |
| 4a2-4 | 4a2-2 | 11.1% | 13.52 | 12.2% | 42.7% |
| 4a2-3 | 4a2-3 | 11.1% | 13.85 | 6.3% | 28.8% |
| 4a2-4 | 4a2-3 | 11.1% | 14.09 | 4.2% | 20.4% |
| 4a2-4 | 4a2-4 | 2.8% | 14.42 | 2.3% | 13.1% |

**4b2**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 4b2-1 | 2-2, pairs sharing one column | 3–6 | `U R2 U'` | 4a1 | 16.7% | 12.50 | 43.9% | 88.3% |
| 4b2-2 | 3-1 | 4–7 | `D' F2 U' F2` | nothing (set up first) | 33.3% | 12.61 | 39.6% | 85.6% |
| 4b2-3 | 3-1 | 5–8 | `U' L2 U' F2 U2` | nothing (set up first) | 33.3% | 12.76 | 33.1% | 80.7% |
| 4b2-4 | 2-2, pairs sharing one column | 6–9 | `D F2 U R2 U2 F2` | nothing (set up first) | 16.7% | 12.85 | 29.6% | 77.5% |

4b2, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---:|---:|---:|---:|
| 4b2-1 | 4b2-1 | 2.8% | 12.36 | 49.7% | 90.7% |
| 4b2-2 | 4b2-1 | 11.1% | 12.44 | 46.6% | 89.7% |
| 4b2-2 | 4b2-2 | 11.1% | 12.55 | 42.3% | 87.1% |
| 4b2-3 | 4b2-1 | 11.1% | 12.56 | 41.3% | 87.2% |
| 4b2-4 | 4b2-1 | 5.6% | 12.63 | 38.1% | 85.2% |
| 4b2-3 | 4b2-2 | 22.2% | 12.67 | 36.5% | 83.9% |
| 4b2-2 | 4b2-4 | 11.1% | 12.75 | 33.4% | 81.6% |
| 4b2-3 | 4b2-3 | 11.1% | 12.85 | 29.4% | 77.5% |
| 4b2-3 | 4b2-4 | 11.1% | 12.95 | 25.6% | 74.0% |
| 4b2-4 | 4b2-4 | 2.8% | 13.06 | 21.2% | 68.9% |

**0c3**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 0c3-1 | none bad | 9–12 | `D' R2 D2 F2 U F2 U2 R2 U` | 4a2 | 33.3% | 14.29 | 4.0% | 17.8% |
| 0c3-2 | none bad | 10–12 | `U L2 D2 F2 U F2 U2 R2 U R2` | nothing (set up first) | 66.7% | 14.54 | 1.9% | 11.1% |

0c3, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---:|---:|---:|---:|
| 0c3-1 | 0c3-1 | 11.1% | 14.22 | 5.4% | 23.2% |
| 0c3-1 | 0c3-2 | 44.4% | 14.33 | 3.3% | 15.2% |
| 0c3-2 | 0c3-2 | 44.4% | 14.65 | 1.2% | 9.0% |

**2c3**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 2c3-1 | 1 up 1 down, stacked | 5–8 | `D' F2 D' L2 U'` | 4b2 | 25.0% | 12.68 | 36.9% | 83.4% |
| 2c3-2 | 1 up 1 down, opposite | 5–8 | `U' R2 U' R2 U` | 4b2 | 25.0% | 12.87 | 29.2% | 75.3% |
| 2c3-3 | both on one layer, adjacent | 6–9 | `U R2 U' F2 U F2` | nothing (set up first) | 50.0% | 13.08 | 22.3% | 66.1% |

2c3, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---:|---:|---:|---:|
| 2c3-1 | 2c3-1 | 6.2% | 12.49 | 45.1% | 88.4% |
| 2c3-2 | 2c3-1 | 12.5% | 12.64 | 38.2% | 84.7% |
| 2c3-3 | 2c3-1 | 25.0% | 12.78 | 32.1% | 80.3% |
| 2c3-2 | 2c3-2 | 6.2% | 12.84 | 30.3% | 77.1% |
| 2c3-3 | 2c3-2 | 25.0% | 13.01 | 24.1% | 69.7% |
| 2c3-3 | 2c3-3 | 25.0% | 13.25 | 16.5% | 57.3% |

**4c3**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 4c3-1 | 2-2, pairs on opposite sides | 7–9 | `D B2 U F2 U2 R2 U` | 4b2 | 8.3% | 13.06 | 21.6% | 68.1% |
| 4c3-2 | 2-2, pairs stacked | 7–9 | `D' R2 D' B2 U2 R2 U` | 4b2 | 8.3% | 13.21 | 17.6% | 59.6% |
| 4c3-3 | 4-0 | 8–9 | `D' R2 U B2 U2 R2 U R2` | nothing (set up first) | 4.2% | 13.27 | 15.2% | 57.0% |
| 4c3-4 | 2-2, pairs sharing one column | 7–10 | `D' B2 U2 R2 U F2 U` | 4a2 | 16.7% | 13.45 | 13.5% | 47.2% |
| 4c3-5 | 3-1 | 8–11 | `D B2 D2 R2 U F2 U' R2` | nothing (set up first) | 33.3% | 13.51 | 11.4% | 45.1% |
| 4c3-6 | 2-2, diagonal over diagonal | 8–10 | `U' F2 U' R2 U2 F2 U F2` | nothing (set up first) | 8.3% | 13.52 | 10.3% | 43.0% |
| 4c3-7 | 2-2, pairs stacked | 8–10 | `U' L2 U' R2 U2 F2 U F2` | nothing (set up first) | 8.3% | 13.59 | 9.4% | 39.8% |
| 4c3-8 | 4-0 | 9–10 | `U' F2 D R2 U2 F2 U R2 U2` | nothing (set up first) | 4.2% | 13.83 | 5.1% | 28.5% |
| 4c3-9 | 2-2, pairs on opposite sides | 9–11 | `D' B2 U' F2 U2 R2 U F2 U2` | nothing (set up first) | 8.3% | 14.00 | 3.6% | 21.5% |

4c3, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---:|---:|---:|---:|
| 4c3-4 | 4c3-1 | 5.6% | 13.04 | 23.1% | 67.8% |
| 4c3-5 | 4c3-1 | 11.1% | 13.07 | 20.9% | 68.3% |
| 4c3-4 | 4c3-2 | 5.6% | 13.19 | 18.8% | 59.4% |
| 4c3-5 | 4c3-2 | 11.1% | 13.22 | 17.1% | 59.8% |
| 4c3-3 | 4c3-4 | 2.8% | 13.24 | 16.6% | 57.7% |
| 4c3-3 | 4c3-5 | 5.6% | 13.28 | 14.5% | 56.7% |
| 4c3-4 | 4c3-6 | 5.6% | 13.47 | 12.0% | 45.7% |
| 4c3-4 | 4c3-7 | 5.6% | 13.54 | 11.0% | 41.9% |
| 4c3-5 | 4c3-6 | 11.1% | 13.54 | 9.5% | 41.7% |
| 4c3-5 | 4c3-7 | 11.1% | 13.61 | 8.5% | 38.7% |
| 4c3-8 | 4c3-4 | 2.8% | 13.79 | 5.8% | 30.4% |
| 4c3-8 | 4c3-5 | 5.6% | 13.84 | 4.8% | 27.5% |
| 4c3-4 | 4c3-9 | 5.6% | 13.95 | 4.8% | 24.1% |
| 4c3-5 | 4c3-9 | 11.1% | 14.03 | 3.0% | 20.3% |

**0c4**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 0c4-1 | none bad | 9–10 | `U' F2 D L2 U2 F2 U F2 U'` | 4a3 | 100.0% | 13.67 | 6.7% | 35.8% |

**2c4**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 2c4-1 | both on one layer, adjacent | 7–10 | `U F2 U L2 U' F2 U'` | 2c3 | 16.7% | 13.27 | 16.2% | 56.7% |
| 2c4-2 | 1 up 1 down, opposite | 8–10 | `U' F2 U' L2 U R2 U F2` | 4b3 | 8.3% | 13.39 | 13.2% | 50.9% |
| 2c4-3 | both on one layer, adjacent | 7–10 | `D F2 U' F2 U R2 U'` | 2c3 | 16.7% | 13.45 | 12.5% | 47.3% |
| 2c4-4 | both on one layer, adjacent | 8–11 | `U' R2 U' R2 U F2 U' F2` | nothing (set up first) | 16.7% | 13.77 | 7.0% | 32.5% |
| 2c4-5 | 1 up 1 down, stacked | 9–11 | `D F2 U2 R2 U F2 U' F2 U` | 4b3 | 8.3% | 13.77 | 7.0% | 33.1% |
| 2c4-6 | 1 up 1 down, opposite | 8–11 | `U' R2 U F2 U' R2 U R2` | nothing (set up first) | 16.7% | 13.80 | 6.4% | 30.8% |
| 2c4-7 | 1 up 1 down, stacked | 9–12 | `U F2 D' L2 U F2 U' F2 U2` | nothing (set up first) | 16.7% | 14.01 | 4.1% | 22.9% |

2c4, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---:|---:|---:|---:|
| 2c4-1 | 2c4-1 | 2.8% | 12.93 | 26.3% | 74.7% |
| 2c4-1 | 2c4-2 | 2.8% | 13.01 | 23.1% | 71.6% |
| 2c4-3 | 2c4-1 | 5.6% | 13.11 | 20.4% | 65.3% |
| 2c4-2 | 2c4-2 | 0.7% | 13.15 | 18.2% | 64.5% |
| 2c4-3 | 2c4-2 | 2.8% | 13.17 | 18.3% | 62.3% |
| 2c4-3 | 2c4-3 | 2.8% | 13.32 | 15.1% | 54.0% |
| 2c4-1 | 2c4-5 | 2.8% | 13.32 | 13.7% | 54.4% |
| 2c4-4 | 2c4-1 | 5.6% | 13.40 | 12.4% | 50.0% |
| 2c4-1 | 2c4-6 | 5.6% | 13.44 | 11.6% | 47.6% |
| 2c4-3 | 2c4-5 | 2.8% | 13.47 | 11.1% | 46.4% |
| 2c4-4 | 2c4-2 | 2.8% | 13.49 | 10.2% | 44.9% |
| 2c4-5 | 2c4-2 | 1.4% | 13.53 | 9.1% | 43.0% |
| 2c4-6 | 2c4-2 | 2.8% | 13.54 | 9.1% | 42.5% |
| 2c4-1 | 2c4-7 | 5.6% | 13.59 | 8.4% | 39.7% |
| 2c4-4 | 2c4-3 | 5.6% | 13.60 | 9.3% | 39.6% |
| 2c4-3 | 2c4-6 | 5.6% | 13.63 | 8.7% | 37.8% |
| 2c4-3 | 2c4-7 | 5.6% | 13.73 | 6.8% | 33.0% |
| 2c4-7 | 2c4-2 | 2.8% | 13.78 | 5.1% | 30.4% |
| 2c4-4 | 2c4-5 | 2.8% | 13.82 | 5.4% | 28.8% |
| 2c4-6 | 2c4-5 | 2.8% | 13.87 | 4.9% | 26.9% |
| 2c4-4 | 2c4-4 | 2.8% | 13.90 | 5.0% | 26.1% |
| 2c4-4 | 2c4-6 | 5.6% | 13.95 | 4.4% | 24.0% |
| 2c4-6 | 2c4-6 | 2.8% | 13.98 | 3.9% | 22.8% |
| 2c4-4 | 2c4-7 | 5.6% | 14.09 | 2.8% | 18.7% |
| 2c4-6 | 2c4-7 | 5.6% | 14.11 | 2.7% | 17.6% |
| 2c4-5 | 2c4-5 | 0.7% | 14.13 | 2.5% | 17.7% |
| 2c4-7 | 2c4-5 | 2.8% | 14.33 | 1.3% | 11.8% |
| 2c4-7 | 2c4-7 | 2.8% | 14.49 | 0.6% | 7.5% |

**4c4**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 4c4-1 | 2-2, diagonal over diagonal | 9–10 | `U' R2 U' R2 U2 F2 U R2 U` | 4a3 | 8.3% | 13.97 | 4.3% | 23.4% |
| 4c4-2 | 2-2, pairs sharing one column | 9–11 | `U' R2 U' F2 U2 R2 U R2 U` | 4a3 | 16.7% | 14.25 | 2.5% | 15.0% |
| 4c4-3 | 2-2, pairs stacked | 10–11 | `U L2 D' B2 U2 R2 U F2 U' R2` | nothing (set up first) | 16.7% | 14.27 | 1.9% | 13.1% |
| 4c4-4 | 3-1 | 10–12 | `D' R2 D' B2 U2 R2 U R2 U' R2` | nothing (set up first) | 33.3% | 14.48 | 1.2% | 9.3% |
| 4c4-5 | 2-2, pairs on opposite sides | 11–12 | `D B2 U' L2 U2 F2 U R2 U' R2 U2` | nothing (set up first) | 16.7% | 14.60 | 0.6% | 6.0% |
| 4c4-6 | 4-0 | 11–12 | `D F2 U2 R2 U F2 U2 R2 U F2 U` | 0c3 | 8.3% | 14.71 | 0.6% | 5.6% |

4c4, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---:|---:|---:|---:|
| 4c4-2 | 4c4-1 | 5.6% | 13.87 | 5.6% | 28.0% |
| 4c4-4 | 4c4-1 | 11.1% | 14.01 | 3.7% | 21.2% |
| 4c4-2 | 4c4-3 | 11.1% | 14.14 | 2.9% | 16.7% |
| 4c4-4 | 4c4-3 | 22.2% | 14.33 | 1.3% | 11.3% |
| 4c4-5 | 4c4-2 | 11.1% | 14.43 | 1.1% | 9.4% |
| 4c4-6 | 4c4-2 | 5.6% | 14.50 | 1.3% | 9.5% |
| 4c4-4 | 4c4-5 | 22.2% | 14.69 | 0.3% | 4.3% |
| 4c4-6 | 4c4-4 | 11.1% | 14.81 | 0.2% | 3.7% |

**2c5**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 2c5-1 | both on one layer, adjacent | 9–12 | `U R2 U F2 U' F2 U R2 U` | 2c4 | 50.0% | 14.12 | 3.4% | 19.4% |
| 2c5-2 | 1 up 1 down, opposite | 10–13 | `D B2 U' R2 U F2 U' R2 U R2` | 4b4 | 25.0% | 14.34 | 1.9% | 12.9% |
| 2c5-3 | 1 up 1 down, stacked | 11–13 | `D F2 U' F2 U F2 U' F2 U R2 U2` | 4b4 | 25.0% | 14.72 | 0.6% | 6.0% |

2c5, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---:|---:|---:|---:|
| 2c5-1 | 2c5-1 | 25.0% | 13.95 | 4.7% | 25.1% |
| 2c5-1 | 2c5-2 | 25.0% | 14.15 | 2.9% | 17.8% |
| 2c5-2 | 2c5-2 | 6.2% | 14.38 | 1.4% | 11.4% |
| 2c5-1 | 2c5-3 | 25.0% | 14.44 | 1.1% | 9.5% |
| 2c5-2 | 2c5-3 | 12.5% | 14.69 | 0.2% | 4.5% |
| 2c5-3 | 2c5-3 | 6.2% | 15.31 | 0.0% | 0.6% |

**4b5**

| Case | Bad corners | L | Example (scramble) | A qt takes it straight to | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---|---|---|---:|---:|---:|---:|
| 4b5-1 | 3-1 | 9–12 | `U' L2 D F2 U' R2 U F2 U` | 2c4 | 66.7% | 14.23 | 2.2% | 15.1% |
| 4b5-2 | 2-2, pairs sharing one column | 10–12 | `D F2 U R2 U' R2 U R2 U F2` | 4a4 | 33.3% | 14.37 | 1.3% | 10.7% |

4b5, corner case on both sides (normal and inverse, either order):

| One side | Other side | Share | Avg optimal | ≤ 12 | ≤ 13 |
|---|---|---:|---:|---:|---:|
| 4b5-1 | 4b5-1 | 44.4% | 14.19 | 2.6% | 16.5% |
| 4b5-1 | 4b5-2 | 44.4% | 14.31 | 1.6% | 12.2% |
| 4b5-2 | 4b5-2 | 11.1% | 14.48 | 0.7% | 7.9% |

---

## Appendix F: HTR length on both sides, all 48 subsets

Rows: the shorter of the two HTR lengths (normal, inverse). Columns: the longer. Each cell: share of the subset · average optimal · % finishing in 12 · % finishing in 13.

**0c0 0e**

| shorter \ longer | 0 | 2 |
|---|---:|---:|
| 0 | 50.0% · 9.89 · 99.5 · 100 |  |
| 2 |  | 50.0% · 10.00 · 98.9 · 100 |

**0c0 2e**

| shorter \ longer | 5 | 6 |
|---|---:|---:|
| 5 | 25.0% · 11.58 · 82.3 · 99 | 50.0% · 11.67 · 80.8 · 99 |
| 6 |  | 25.0% · 11.84 · 75.7 · 99 |

**0c0 4e**

| shorter \ longer | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|
| 4 | 0.3% · 11.96 · 64.3 · 90 | 2.5% · 11.90 · 67.9 · 97 | 4.3% · 11.87 · 70.4 · 96 | 3.7% · 11.81 · 70.4 · 98 |
| 5 |  | 4.9% · 12.30 · 53.8 · 91 | 17.3% · 12.32 · 52.8 · 92 | 14.8% · 12.20 · 57.5 · 95 |
| 6 |  |  | 15.1% · 12.45 · 46.6 · 90 | 25.9% · 12.38 · 50.9 · 93 |
| 7 |  |  |  | 11.1% · 12.51 · 45.2 · 90 |

**0c0 6e**

| shorter \ longer | 7 | 8 |
|---|---:|---:|
| 7 | 25.0% · 12.90 · 28.0 · 75 | 50.0% · 12.91 · 27.4 · 76 |
| 8 |  | 25.0% · 12.95 · 25.5 · 74 |

**0c0 8e**

| shorter \ longer | 6 |
|---|---:|
| 6 | 100.0% · 12.69 · 38.6 · 78 |

**4a1 0e**

| shorter \ longer | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|
| 7 | 2.8% · 12.91 · 27.9 · 72 | 11.1% · 12.81 · 31.2 · 77 | 11.1% · 12.73 · 35.2 · 82 | 5.6% · 12.83 · 31.3 · 79 |
| 8 |  | 11.1% · 12.96 · 25.3 · 73 | 22.2% · 12.94 · 26.1 · 75 | 11.1% · 13.09 · 19.2 · 69 |
| 9 |  |  | 11.1% · 13.17 · 19.3 · 64 | 11.1% · 13.37 · 10.5 · 54 |
| 10 |  |  |  | 2.8% · 13.82 · 3.0 · 28 |

**4a1 2e**

| shorter \ longer | 6 | 7 | 8 |
|---|---:|---:|---:|
| 6 | 6.2% · 12.19 · 58.9 · 96 | 27.1% · 12.34 · 52.1 · 94 | 10.4% · 12.48 · 45.9 · 92 |
| 7 |  | 29.3% · 12.58 · 41.0 · 87 | 22.6% · 12.80 · 30.9 · 81 |
| 8 |  |  | 4.3% · 13.11 · 17.5 · 69 |

**4a1 4e**

| shorter \ longer | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.0% · 10.10 · 94.8 · 100 | 0.0% · 9.67 · 100.0 · 100 | 0.0% · 9.69 · 99.2 · 100 | 0.1% · 9.67 · 100.0 · 100 | 0.1% · 9.79 · 99.8 · 100 | 0.2% · 9.91 · 99.8 · 100 | 0.3% · 10.34 · 99.7 · 100 | 0.1% · 10.85 · 100.0 · 100 |
| 2 |  | 0.0% · 10.27 · 95.9 · 100 | 0.2% · 10.36 · 96.7 · 100 | 0.3% · 10.40 · 97.1 · 100 | 0.6% · 10.56 · 97.2 · 100 | 1.0% · 10.69 · 97.9 · 100 | 1.3% · 11.13 · 96.2 · 100 | 0.3% · 11.69 · 83.1 · 100 |
| 3 |  |  | 0.2% · 10.68 · 89.8 · 100 | 0.9% · 10.80 · 89.1 · 100 | 1.4% · 11.00 · 91.3 · 100 | 2.4% · 11.12 · 94.1 · 100 | 3.3% · 11.56 · 86.2 · 100 | 0.7% · 12.12 · 68.2 · 98 |
| 4 |  |  |  | 0.9% · 11.23 · 81.1 · 97 | 2.8% · 11.52 · 79.6 · 97 | 4.8% · 11.73 · 80.8 · 99 | 6.5% · 12.09 · 66.1 · 97 | 1.4% · 12.54 · 43.5 · 89 |
| 5 |  |  |  |  | 2.3% · 11.94 · 70.1 · 96 | 7.9% · 12.19 · 62.5 · 96 | 10.8% · 12.44 · 48.7 · 93 | 2.3% · 12.80 · 31.0 · 81 |
| 6 |  |  |  |  |  | 6.7% · 12.51 · 45.6 · 93 | 18.2% · 12.64 · 37.8 · 89 | 3.8% · 12.89 · 26.8 · 77 |
| 7 |  |  |  |  |  |  | 12.4% · 12.71 · 34.2 · 85 | 5.2% · 12.93 · 26.3 · 75 |
| 8 |  |  |  |  |  |  |  | 0.5% · 13.17 · 18.8 · 64 |

**4a2 0e**

| shorter \ longer | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|
| 9 | 2.8% · 13.08 · 24.6 · 64 | 11.1% · 13.25 · 17.7 · 57 | 11.1% · 13.54 · 9.8 · 42 | 5.6% · 13.75 · 4.7 · 33 |
| 10 |  | 11.1% · 13.60 · 9.1 · 41 | 22.2% · 13.89 · 3.8 · 26 | 11.1% · 14.21 · 0.3 · 12 |
| 11 |  |  | 11.1% · 14.31 · 1.4 · 12 | 11.1% · 14.59 · 0.3 · 6 |
| 12 |  |  |  | 2.8% · 15.01 · 0.0 · 1 |

**4a2 2e**

| shorter \ longer | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|
| 8 | 1.6% · 12.76 · 34.8 · 77 | 9.4% · 12.92 · 26.6 · 74 | 8.3% · 13.21 · 17.2 · 60 | 4.2% · 13.37 · 13.2 · 53 |
| 9 |  | 14.1% · 13.22 · 18.0 · 59 | 25.0% · 13.60 · 7.6 · 40 | 12.5% · 13.83 · 2.5 · 28 |
| 10 |  |  | 11.1% · 14.17 · 1.5 · 16 | 11.1% · 14.45 · 0.2 · 6 |
| 11 |  |  |  | 2.8% · 14.85 · 0.0 · 1 |

**4a2 4e**

| shorter \ longer | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5 | 0.1% · 11.61 · 70.4 · 94 | 0.8% · 11.54 · 78.1 · 96 | 1.4% · 11.82 · 70.7 · 96 | 2.2% · 12.07 · 64.6 · 94 | 1.6% · 12.28 · 55.2 · 93 | 1.0% · 12.65 · 37.3 · 85 | 0.2% · 12.70 · 37.8 · 81 |
| 6 |  | 1.2% · 11.67 · 74.5 · 97 | 4.1% · 12.03 · 65.8 · 93 | 6.6% · 12.30 · 53.8 · 93 | 4.7% · 12.56 · 42.6 · 89 | 2.9% · 12.89 · 27.5 · 79 | 0.6% · 13.00 · 24.4 · 76 |
| 7 |  |  | 3.4% · 12.49 · 44.9 · 87 | 11.0% · 12.78 · 33.9 · 78 | 7.9% · 13.07 · 20.9 · 70 | 4.8% · 13.39 · 11.5 · 53 | 1.0% · 13.58 · 2.0 · 47 |
| 8 |  |  |  | 8.8% · 13.13 · 19.3 · 65 | 12.6% · 13.41 · 12.4 · 50 | 7.7% · 13.64 · 6.1 · 39 | 1.6% · 13.84 · 5.0 · 24 |
| 9 |  |  |  |  | 4.5% · 13.74 · 4.7 · 35 | 5.5% · 13.91 · 4.4 · 24 | 1.2% · 14.17 · 3.6 · 21 |
| 10 |  |  |  |  |  | 1.7% · 14.16 · 2.0 · 18 | 0.7% · 14.33 · 0.1 · 11 |
| 11 |  |  |  |  |  |  | 0.1% · 14.64 · 0.0 · 0 |

**4b2 0e**

| shorter \ longer | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|
| 6 | 2.8% · 12.62 · 39.8 · 83 | 11.1% · 12.63 · 36.1 · 84 | 11.1% · 12.68 · 37.2 · 82 | 5.6% · 12.66 · 37.9 · 84 |
| 7 |  | 11.1% · 12.82 · 31.5 · 76 | 22.2% · 12.91 · 27.4 · 74 | 11.1% · 12.94 · 26.9 · 74 |
| 8 |  |  | 11.1% · 13.11 · 20.4 · 65 | 11.1% · 13.19 · 17.2 · 63 |
| 9 |  |  |  | 2.8% · 13.36 · 11.8 · 54 |

**4b2 2e**

| shorter \ longer | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|
| 3 | 0.0% · 11.20 · 90.7 · 100 | 0.1% · 11.19 · 92.0 · 100 | 0.3% · 11.26 · 88.6 · 100 | 0.8% · 11.32 · 86.2 · 100 | 0.7% · 11.38 · 84.8 · 100 | 0.1% · 11.32 · 85.8 · 99 |
| 4 |  | 0.2% · 11.66 · 77.8 · 99 | 1.3% · 11.84 · 72.4 · 98 | 3.4% · 11.97 · 66.6 · 97 | 2.9% · 12.08 · 62.7 · 96 | 0.3% · 12.12 · 61.3 · 95 |
| 5 |  |  | 2.4% · 12.15 · 59.5 · 96 | 12.7% · 12.35 · 50.9 · 93 | 10.7% · 12.50 · 44.4 · 90 | 1.3% · 12.62 · 39.7 · 87 |
| 6 |  |  |  | 16.5% · 12.60 · 39.7 · 87 | 27.9% · 12.80 · 31.1 · 82 | 3.4% · 12.99 · 22.8 · 75 |
| 7 |  |  |  |  | 11.8% · 13.03 · 21.9 · 72 | 2.9% · 13.25 · 13.7 · 61 |
| 8 |  |  |  |  |  | 0.2% · 13.52 · 5.7 · 45 |

**4b2 4e**

| shorter \ longer | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|---:|
| 4 | 0.0% · 10.97 · 80.7 · 98 | 0.1% · 10.98 · 89.4 · 100 | 0.2% · 11.21 · 89.1 · 100 | 0.6% · 11.45 · 85.2 · 100 | 0.8% · 11.59 · 84.5 · 100 | 0.2% · 11.66 · 81.3 · 99 |
| 5 |  | 0.1% · 11.37 · 82.7 · 99 | 0.6% · 11.67 · 76.8 · 99 | 1.8% · 11.94 · 69.4 · 98 | 2.3% · 12.11 · 63.3 · 98 | 0.6% · 12.22 · 59.9 · 96 |
| 6 |  |  | 1.2% · 12.07 · 62.6 · 96 | 7.2% · 12.35 · 51.2 · 93 | 9.4% · 12.56 · 42.0 · 90 | 2.4% · 12.72 · 34.6 · 87 |
| 7 |  |  |  | 10.5% · 12.58 · 40.9 · 88 | 27.3% · 12.78 · 31.7 · 83 | 6.9% · 12.98 · 23.0 · 76 |
| 8 |  |  |  |  | 17.7% · 12.99 · 22.9 · 74 | 9.0% · 13.21 · 14.6 · 63 |
| 9 |  |  |  |  |  | 1.1% · 13.44 · 9.2 · 48 |

**0c3 0e**

| shorter \ longer | 10 | 11 |
|---|---:|---:|
| 10 | 11.1% · 13.81 · 10.9 · 31 | 44.4% · 13.89 · 8.7 · 34 |
| 11 |  | 44.4% · 14.33 · 1.4 · 17 |

**0c3 2e**

| shorter \ longer | 9 | 10 | 11 |
|---|---:|---:|---:|
| 9 | 2.8% · 13.61 · 16.3 · 42 | 22.2% · 13.86 · 8.3 · 31 | 5.6% · 13.92 · 6.5 · 31 |
| 10 |  | 44.4% · 14.44 · 2.1 · 13 | 22.2% · 14.48 · 0.3 · 8 |
| 11 |  |  | 2.8% · 14.69 · 0.1 · 6 |

**0c3 4e**

| shorter \ longer | 10 | 11 | 12 | 13 |
|---|---:|---:|---:|---:|
| 10 | 0.9% · 14.07 · 12.3 · 25 | 5.5% · 14.07 · 7.8 · 26 | 9.9% · 14.17 · 4.2 · 22 | 1.4% · 14.71 · 0.0 · 0 |
| 11 |  | 8.8% · 14.39 · 4.5 · 14 | 31.8% · 14.55 · 0.4 · 9 | 4.4% · 15.08 · 0.0 · 2 |
| 12 |  |  | 28.8% · 14.83 · 0.0 · 2 | 8.0% · 15.26 · 0.0 · 0 |
| 13 |  |  |  | 0.5% · 15.79 · 0.0 · 0 |

**0c3 6e**

| shorter \ longer | 9 | 10 | 11 |
|---|---:|---:|---:|
| 9 | 2.8% · 13.60 · 16.6 · 43 | 22.2% · 13.87 · 8.3 · 31 | 5.6% · 13.93 · 6.5 · 31 |
| 10 |  | 44.4% · 14.46 · 2.1 · 13 | 22.2% · 14.49 · 0.3 · 8 |
| 11 |  |  | 2.8% · 14.70 · 0.3 · 6 |

**0c3 8e**

| shorter \ longer | 10 | 11 |
|---|---:|---:|
| 10 | 11.1% · 13.83 · 10.9 · 31 | 44.4% · 13.95 · 8.5 · 32 |
| 11 |  | 44.4% · 14.41 · 1.4 · 16 |

**2c3 0e**

| shorter \ longer | 9 | 10 |
|---|---:|---:|
| 9 | 25.0% · 13.10 · 20.4 · 67 | 50.0% · 13.34 · 12.4 · 55 |
| 10 |  | 25.0% · 13.78 · 4.2 · 31 |

**2c3 2e**

| shorter \ longer | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|
| 5 | 0.4% · 11.97 · 65.8 · 97 | 4.3% · 12.08 · 62.7 · 96 | 7.0% · 12.19 · 58.7 · 96 | 0.4% · 12.11 · 62.4 · 97 |
| 6 |  | 11.8% · 12.40 · 48.7 · 92 | 38.7% · 12.56 · 41.7 · 88 | 2.1% · 12.47 · 45.8 · 91 |
| 7 |  |  | 31.6% · 12.76 · 33.1 · 82 | 3.5% · 12.64 · 38.0 · 87 |
| 8 |  |  |  | 0.1% · 12.61 · 40.0 · 86 |

**2c3 4e**

| shorter \ longer | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|
| 5 | 0.1% · 12.14 · 55.6 · 93 | 0.8% · 12.16 · 57.4 · 95 | 2.1% · 12.32 · 51.9 · 92 | 2.2% · 12.39 · 48.9 · 91 | 0.3% · 12.61 · 40.4 · 86 |
| 6 |  | 1.9% · 12.35 · 49.9 · 91 | 10.4% · 12.59 · 40.1 · 86 | 11.2% · 12.71 · 35.5 · 82 | 1.5% · 12.96 · 25.3 · 74 |
| 7 |  |  | 14.1% · 12.89 · 28.2 · 76 | 30.2% · 13.03 · 22.5 · 70 | 4.2% · 13.27 · 14.3 · 58 |
| 8 |  |  |  | 16.2% · 13.21 · 16.5 · 62 | 4.5% · 13.45 · 9.2 · 48 |
| 9 |  |  |  |  | 0.3% · 13.73 · 5.2 · 31 |

**2c3 6e**

| shorter \ longer | 7 | 8 | 9 |
|---|---:|---:|---:|
| 7 | 3.5% · 12.82 · 30.8 · 78 | 20.5% · 13.00 · 23.8 · 71 | 10.0% · 13.06 · 21.0 · 69 |
| 8 |  | 29.9% · 13.25 · 16.0 · 58 | 29.1% · 13.33 · 13.2 · 55 |
| 9 |  |  | 7.1% · 13.42 · 10.0 · 50 |

**2c3 8e**

| shorter \ longer | 9 | 10 |
|---|---:|---:|
| 9 | 25.0% · 13.23 · 16.0 · 61 | 50.0% · 13.47 · 9.6 · 47 |
| 10 |  | 25.0% · 13.91 · 3.3 · 25 |

**4c3 0e**

| shorter \ longer | 8 | 9 | 10 |
|---|---:|---:|---:|
| 8 | 11.1% · 12.87 · 29.6 · 75 | 36.1% · 13.06 · 22.9 · 66 | 8.3% · 13.61 · 8.7 · 38 |
| 9 |  | 27.8% · 13.40 · 13.9 · 50 | 16.7% · 13.85 · 4.8 · 28 |

**4c3 2e**

| shorter \ longer | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|
| 7 | 0.3% · 12.68 · 36.7 · 78 | 3.2% · 12.90 · 28.1 · 72 | 7.1% · 12.99 · 25.0 · 70 | 1.5% · 13.11 · 21.6 · 65 |
| 8 |  | 7.4% · 13.23 · 17.7 · 57 | 31.7% · 13.38 · 13.2 · 51 | 6.6% · 13.58 · 9.4 · 42 |
| 9 |  |  | 28.6% · 13.62 · 8.0 · 39 | 12.2% · 13.95 · 3.3 · 24 |
| 10 |  |  |  | 1.3% · 14.28 · 0.3 · 10 |

**4c3 4e**

| shorter \ longer | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|
| 7 | 0.2% · 12.22 · 54.9 · 92 | 1.7% · 12.54 · 42.6 · 85 | 3.8% · 12.82 · 31.2 · 78 | 3.2% · 13.04 · 22.1 · 69 | 0.2% · 13.31 · 14.5 · 57 |
| 8 |  | 3.4% · 12.86 · 30.0 · 75 | 15.1% · 13.14 · 19.7 · 63 | 12.3% · 13.38 · 12.8 · 52 | 1.0% · 13.70 · 4.6 · 34 |
| 9 |  |  | 16.9% · 13.45 · 11.1 · 48 | 27.1% · 13.73 · 5.6 · 34 | 2.4% · 14.09 · 1.8 · 16 |
| 10 |  |  |  | 10.5% · 14.08 · 2.1 · 18 | 2.3% · 14.37 · 0.3 · 8 |

**0c4 0e**

| shorter \ longer | 9 |
|---|---:|
| 9 | 100.0% · 13.22 · 17.4 · 61 |

**0c4 2e**

| shorter \ longer | 9 | 10 |
|---|---:|---:|
| 9 | 25.0% · 13.51 · 9.1 · 44 | 50.0% · 13.50 · 9.3 · 45 |
| 10 |  | 25.0% · 13.57 · 7.9 · 41 |

**0c4 4e**

| shorter \ longer | 9 | 10 |
|---|---:|---:|
| 9 | 37.3% · 13.61 · 7.6 · 39 | 47.5% · 13.64 · 6.9 · 37 |
| 10 |  | 15.1% · 13.70 · 5.3 · 34 |

**0c4 6e**

| shorter \ longer | 10 |
|---|---:|
| 10 | 100.0% · 13.90 · 3.6 · 24 |

**0c4 8e**

| shorter \ longer | 11 |
|---|---:|
| 11 | 100.0% · 14.18 · 1.9 · 16 |

**2c4 0e**

| shorter \ longer | 7 | 8 | 9 |
|---|---:|---:|---:|
| 7 | 11.1% · 12.63 · 38.9 · 84 | 27.8% · 12.92 · 27.6 · 73 | 16.7% · 13.16 · 18.8 · 62 |
| 8 |  | 17.4% · 13.30 · 16.2 · 54 | 20.8% · 13.60 · 9.0 · 39 |
| 9 |  |  | 6.2% · 14.22 · 2.1 · 16 |

**2c4 2e**

| shorter \ longer | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|
| 7 | 0.2% · 12.29 · 52.5 · 93 | 2.6% · 12.66 · 36.9 · 84 | 4.0% · 12.99 · 24.2 · 72 | 1.4% · 13.13 · 18.4 · 66 |
| 8 |  | 9.8% · 13.04 · 23.1 · 68 | 29.9% · 13.36 · 13.5 · 52 | 10.4% · 13.54 · 9.0 · 42 |
| 9 |  |  | 23.0% · 13.75 · 6.3 · 33 | 16.0% · 14.01 · 3.0 · 21 |
| 10 |  |  |  | 2.8% · 14.37 · 0.7 · 10 |

**2c4 4e**

| shorter \ longer | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|
| 7 | 0.4% · 12.67 · 35.6 · 83 | 3.3% · 12.94 · 26.6 · 72 | 6.0% · 13.12 · 20.2 · 64 | 2.7% · 13.24 · 16.1 · 59 | 0.1% · 13.39 · 12.8 · 51 |
| 8 |  | 6.5% · 13.29 · 16.8 · 56 | 23.6% · 13.51 · 10.9 · 45 | 10.6% · 13.68 · 7.4 · 36 | 0.5% · 13.78 · 5.8 · 32 |
| 9 |  |  | 21.4% · 13.79 · 6.0 · 31 | 19.3% · 14.01 · 2.9 · 21 | 0.9% · 14.10 · 1.9 · 17 |
| 10 |  |  |  | 4.3% · 14.32 · 0.9 · 11 | 0.4% · 14.36 · 0.4 · 8 |
| 11 |  |  |  |  | 0.0% · 14.42 · 0.9 · 7 |

**2c4 6e**

| shorter \ longer | 8 | 9 | 10 |
|---|---:|---:|---:|
| 8 | 4.3% · 12.98 · 24.8 · 72 | 21.7% · 13.35 · 13.5 · 53 | 11.3% · 13.54 · 9.3 · 43 |
| 9 |  | 27.1% · 13.77 · 6.2 · 32 | 28.2% · 14.01 · 3.2 · 21 |
| 10 |  |  | 7.3% · 14.40 · 0.8 · 9 |

**2c4 8e**

| shorter \ longer | 9 | 10 | 11 |
|---|---:|---:|---:|
| 9 | 11.1% · 13.36 · 13.6 · 52 | 27.8% · 13.72 · 6.8 · 34 | 16.7% · 13.93 · 3.3 · 24 |
| 10 |  | 17.4% · 14.16 · 2.5 · 18 | 20.8% · 14.43 · 0.6 · 8 |
| 11 |  |  | 6.2% · 14.93 · 0.0 · 2 |

**4c4 0e**

| shorter \ longer | 10 | 11 | 12 | 13 |
|---|---:|---:|---:|---:|
| 10 | 5.6% · 13.98 · 4.1 · 25 | 22.2% · 14.17 · 3.0 · 16 | 11.1% · 14.58 · 0.7 · 6 | 5.6% · 14.74 · 0.0 · 5 |
| 11 |  | 22.2% · 14.43 · 0.9 · 10 | 22.2% · 14.82 · 0.2 · 3 | 11.1% · 15.04 · 0.0 · 1 |

**4c4 2e**

| shorter \ longer | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|
| 9 | 0.9% · 13.66 · 9.1 · 36 | 6.9% · 13.91 · 5.2 · 25 | 9.3% · 14.13 · 3.1 · 18 | 0.9% · 14.37 · 1.5 · 12 |
| 10 |  | 13.4% · 14.21 · 2.3 · 15 | 37.6% · 14.46 · 0.9 · 9 | 3.8% · 14.73 · 0.2 · 4 |
| 11 |  |  | 23.7% · 14.65 · 0.4 · 5 | 3.6% · 14.89 · 0.2 · 3 |

**4c4 4e**

| shorter \ longer | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|
| 9 | 1.2% · 13.76 · 7.1 · 32 | 8.6% · 13.92 · 4.9 · 25 | 9.7% · 14.15 · 2.9 · 17 | 1.4% · 14.45 · 1.1 · 10 |
| 10 |  | 13.9% · 14.15 · 2.7 · 17 | 34.9% · 14.41 · 1.3 · 10 | 6.5% · 14.71 · 0.3 · 5 |
| 11 |  |  | 18.7% · 14.61 · 0.5 · 6 | 5.0% · 14.89 · 0.1 · 2 |

**2c5 0e**

| shorter \ longer | 10 | 11 |
|---|---:|---:|
| 10 | 25.0% · 14.11 · 3.2 · 19 | 50.0% · 14.37 · 1.4 · 11 |
| 11 |  | 25.0% · 14.86 · 0.3 · 4 |

**2c5 2e**

| shorter \ longer | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|
| 9 | 1.6% · 13.38 · 16.5 · 50 | 14.1% · 13.79 · 6.2 · 32 | 7.0% · 14.09 · 2.9 · 19 | 0.8% · 14.28 · 1.0 · 12 |
| 10 |  | 31.6% · 14.12 · 2.7 · 18 | 31.6% · 14.45 · 0.9 · 9 | 3.5% · 14.62 · 0.3 · 5 |
| 11 |  |  | 7.9% · 15.03 · 0.0 · 2 | 1.8% · 15.23 · 0.0 · 1 |
| 12 |  |  |  | 0.1% · 15.54 · 0.0 · 1 |

**2c5 4e**

| shorter \ longer | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|
| 9 | 2.3% · 13.45 · 13.0 · 47 | 14.6% · 13.78 · 6.7 · 32 | 9.8% · 14.08 · 3.0 · 19 | 1.5% · 14.34 · 1.1 · 11 |
| 10 |  | 23.0% · 14.13 · 2.7 · 18 | 30.6% · 14.45 · 1.0 · 9 | 4.7% · 14.67 · 0.2 · 5 |
| 11 |  |  | 10.2% · 14.93 · 0.1 · 3 | 3.1% · 15.23 · 0.0 · 1 |
| 12 |  |  |  | 0.2% · 15.60 · 0.0 · 0 |

**2c5 6e**

| shorter \ longer | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|
| 9 | 0.4% · 13.88 · 5.4 · 27 | 6.2% · 13.93 · 4.8 · 25 | 3.1% · 14.18 · 2.5 · 16 | 2.3% · 14.44 · 0.9 · 9 |
| 10 |  | 25.0% · 14.08 · 3.1 · 20 | 25.0% · 14.35 · 1.4 · 11 | 18.8% · 14.60 · 0.4 · 6 |
| 11 |  |  | 6.2% · 14.67 · 0.4 · 5 | 9.4% · 14.98 · 0.0 · 1 |
| 12 |  |  |  | 3.5% · 15.47 · 0.0 · 0 |

**2c5 8e**

| shorter \ longer | 10 | 11 | 12 |
|---|---:|---:|---:|
| 10 | 25.0% · 14.09 · 3.6 · 20 | 25.0% · 14.26 · 1.7 · 14 | 25.0% · 14.54 · 0.7 · 7 |
| 11 |  | 6.2% · 14.57 · 0.8 · 6 | 12.5% · 14.87 · 0.0 · 2 |
| 12 |  |  | 6.2% · 15.52 · 0.0 · 0 |

**4b5 0e**

| shorter \ longer | 9 | 10 |
|---|---:|---:|
| 9 | 44.4% · 14.23 · 2.6 · 15 | 44.4% · 14.33 · 1.6 · 12 |
| 10 |  | 11.1% · 14.51 · 0.8 · 8 |

**4b5 2e**

| shorter \ longer | 9 | 10 | 11 |
|---|---:|---:|---:|
| 9 | 6.2% · 14.12 · 3.6 · 19 | 36.5% · 14.20 · 2.6 · 16 | 1.0% · 14.32 · 1.5 · 12 |
| 10 |  | 53.2% · 14.31 · 1.6 · 12 | 3.0% · 14.43 · 0.7 · 9 |
| 11 |  |  | 0.0% · 14.68 · 0.3 · 5 |

**4b5 4e**

| shorter \ longer | 9 | 10 | 11 |
|---|---:|---:|---:|
| 9 | 0.9% · 13.96 · 6.3 · 26 | 9.8% · 14.06 · 4.0 · 21 | 7.0% · 14.22 · 2.2 · 16 |
| 10 |  | 27.9% · 14.20 · 2.4 · 16 | 40.1% · 14.35 · 1.3 · 11 |
| 11 |  |  | 14.4% · 14.52 · 0.4 · 7 |

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

## Docs and sheets referred to

- Levi Gibson, "DR Bounding": https://docs.google.com/document/d/1q7rig4GEo26GunBMtuagZdGyzyjCGlduH84CHLpGLSA
- Rodney Kinney, "Advanced DR Bounding [Beta]": https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0
- Rodney Kinney, sheet "Adv DR Bounding" (rules vs the 216 computed cases): https://docs.google.com/spreadsheets/d/1jRvikzLlm3yHlDQmQ0DLyj3Aw6uinL3Oa-U9_U7R5mY
- FakeMMAP, sheet "OBL++": https://docs.google.com/spreadsheets/d/1kax7evfA85p_4ArXKO7si3FrCpj7PEeFwoz4GY5wRAE
- wen, sheet "HTR better smh (v2)" (the corner subsets): https://docs.google.com/spreadsheets/d/1ZhulzHeNgv2Hiy4x9R1MzsMRlPlI-E8DRiHFJlPlboM
- FakeMMAP's BFS listing, script and tables are attachments on his posts of 6–10 Sep 2026 in #fmc-theory.
- Mallard (cubelib) source, for how the 48 subsets are built: https://github.com/Jobarion/cubelib
- Rodney Kinney, "HTR Theory" (September 2023): https://docs.google.com/document/d/1HjS92UBCeCasbW44ezE0fjt5vmWQvlfkaC4rA113nmw
- Levi Gibson, sheet "Corner Solution Length x DR Finish length" (sampled; Appendix B is the exact version): https://docs.google.com/spreadsheets/d/14rZI1Nf84Og1jS8dN1MfT0sYhvdIWu9gPXkHDs1iVU4

