# Insertion cost by skeleton type

What a 3c, a 5c, a 2c2c, a 3c1t or a pair of twisted corners adds to a skeleton, by how long the skeleton is and how long an alg you allow yourself. Every skeleton is searched exactly: every position, every alg up to the cap.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#non-dr-discussion, #fmc-discussion or #fmc-theory). Docs are listed with links at the end.

**This builds on** what people had already worked out:

- **Sebastiano Tronto's table.** Section 2.4.10 of the [Fewest Moves Tutorial](https://fmcsolves.cubing.net/fmc_tutorial_ENG.pdf), "Move count (an estimate)", is the chart everyone points to: 3c 5/6, 3e 7, two twisted corners 8, three twisted corners 9, 2c2c 9/10, 3c1t 10, 5c 10/11, 2c2e 10. The tutorial says what it is: "It is a heuristic estimate, not a mathematically proved one", and its footnote says where the numbers came from: "Mostly taken from here, slightly adjusted to match my personal opinion", with a link to a post in the speedsolving FMC thread.
- **The estimates people posted.**
  - Phuwish: 2tc "~8.0 I guess", 3tc "mid to high 8 from my experience", 5c "~high 10", and "yeah" ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239358826778798)) to tave_789's "And isnt 3c1t and 2c2c close to 9.5?" ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239312396091486)).
  - cpaul: 9 for a pure 2c2c, 9.5 with a twist, 10 for a 3c1t.
  - Baiqiang: 5-6 for a 3c, 8-9 for a 3c1t, "6-8 for good 2c2c, 8-9 for bad 2c2c".
- **Exchange rates and thresholds from experience.**
  - asacuber's "maybe like 5-6" moves between a 5c and a 3c.
  - Gezza Cubing's and oliynykmax's pairs: a 5c in 16-18 against a 3c in 22-24.
  - The tutorial's 4 corners in 18 against 3 corners in 25.
  - Java ([12 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1128707308382335047)), on two comms against three: "you'd need the f2l-2 to be 6 moves shorter than the f2l-1 probably".
- **Which leftovers take how many comms**: the lists in Yurii Riabov's guide and in the tutorial. **Exhaustive alg results**: notkevin on the 10-move 2c2e algs, torchlight on the shortest alg that twists a corner. **Where insertions fall**: DougCube keeps stats on it.
- **Insertion Finder** ([333.fm/if](https://333.fm/if)), which gives the best insertions for one skeleton you type in. Baiqiang ([5 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181810277851865108)): "i make the website 333.fm. the core is written by Yan Xuan".

**What this adds** is the measured version:

- **Odds, not one number per type**: the chance of +4, +5, +6 and so on, for each leftover, at skeleton lengths from 10 to 30, under a stated cap on the alg length.
- **What the alg list is worth**: the same skeletons with algs of at most 8, 10 and 12 moves.
- **Exchange rates from those odds**: how many moves shorter a 5c, a 2c2c, a 3c1t or a 2tc has to be than a 3c to give the same chance.
- **Where the insertions are**: which part of the skeleton, what checking every other move misses, what taking the best first comm of a 5c loses.
- **The counts behind it**: which leftovers two comms can solve and which need three (proved in Lean), and the shortest alg for every case that has one of 12 moves or fewer.
- **Real skeletons**: 201 worked examples (191 distinct skeletons) from the server and from Cyprian Kalbarczyk's example solves, searched the same way, and the Insertion Finder pages people posted.
- **The claims**: each concrete statement people made about insertions that a computer can settle, checked.
- **How the estimates come out**: every corner row of the tutorial's table, and cpaul's 9 and 10, are within about half a move of what 8-movers give on a random 20-move skeleton. Phuwish's figures are close too, except the 3tc. Baiqiang's are lower, and Baiqiang said they are not averages.

**Terms**, as the server uses them. A *skeleton* is a solution that leaves a few pieces: *3c* is three corners in a cycle, *5c* five corners in one cycle, *2c2c* two swaps of corners, *3c1t* a twisted 3-cycle plus one corner twisted in place, *2tc* and *3tc* two and three corners twisted in place, and the same with *e* for edges (*2fe* is two flipped edges). An *insertion* is an alg put somewhere inside the skeleton that solves those pieces and leaves the rest alone. A *comm* here is any alg for a 3-cycle, commutator or not, and an *8-mover* is one of 8 moves. `(8-2/24)` is the usual note: an 8-move alg, 2 moves cancel, 24 moves so far; I write +6 for what that insertion added. A *nested* insertion is one put inside another. Moves are counted in HTM.

**How to read it.**

- **Start with [section 1](#1-the-short-version)**, the short version: what is new, then what it confirms, one line each.
- **The [worked examples](examples.html)** go with it: the examples from the tutorial and the server redone with the search, then 200 skeletons to play along with, answers folded away. **The [errata](errata.html)** list what the numbers show is wrong in things said on the server, each with an example.
- **The appendices are reference**: the full cost tables, every class of corner and edge 3-cycle with a shortest alg, and how it was computed and checked.
- **What you can do in an attempt, and what is the answer key.** Every cost here is the best insertion over every spot and every alg within the cap. With 8-movers on a 3c that's what you get by checking every spot with the 8-movers you know, so those numbers are a target you can actually reach. Two things aren't:
  - **caps 10 and 12** count every sequence of that length, far more than any list a person knows;
  - **the best pair of comms** for a two-comm leftover means following up every first comm at every spot.

  Those are **computer only**, Insertion Finder's job: the answer key, not something to do in an attempt, and each place says so. The hand version of the best pair is to take the best first comm, and the ones a move worse when there's time (8.4), which gets within 0.09 of a move of it. The rest is for the attempt: the odds and exchange rates for choosing a skeleton (section 7), the search rules of section 8 (every other move, the ends, opposite-face pairs), and the case facts of sections 4 and 5.

---

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | What is new, then what it confirms, one line each. |
| [2. What was asked](#2-what-was-asked) | The questions and the standing disagreement, quoted. |
| [3. What an insertion is here](#3-what-an-insertion-is-here) | Skeleton, leftover, cost, the cap on alg length, what may be inserted, random and real skeletons. |
| [4. How many insertions each leftover needs](#4-how-many-insertions-each-leftover-needs) | Which leftovers one, two or three comms solve. Exact. |
| [5. The algorithms](#5-the-algorithms) | The shortest alg for every case that has one of 12 moves or fewer, how many 8-movers there are, parity. |
| [6. What each type costs](#6-what-each-type-costs) | Mean and odds by skeleton length for every type; the cap; one alg; nesting; edges. |
| [7. Which skeleton to take](#7-which-skeleton-to-take) | The chance of a result by type and length, exchange rates, the thresholds people quoted. |
| [8. Finding them](#8-finding-them) | Where the best insertion is, what longer algs add, checking every other move, the first comm of a 5c. |
| [9. Real skeletons and Insertion Finder](#9-real-skeletons-and-insertion-finder) | The server's skeletons searched the same way, against random ones, their authors and Insertion Finder. |
| [10. The claims, checked](#10-the-claims-checked) | Each checkable statement from the server and the docs, with the verdict. |
| [11. What this does not cover](#11-what-this-does-not-cover) | Limits. |
| [Appendix A: every type and length](#appendix-a-every-type-and-length) | The full cost tables. |
| [Appendix B: the 3c and 3e cases](#appendix-b-the-3c-and-3e-cases) | Every class of corner and edge 3-cycle with a shortest alg. |
| [Appendix C: how it was computed, and what checks it](#appendix-c-how-it-was-computed-and-what-checks-it) | Method, cross-checks and the Lean certificate. |
| [Docs referred to](#docs-referred-to) | Links. |

---

## 1. The short version

New stuff first, then what the numbers confirm. Everything is on random skeletons unless a line says real. *8-movers* means pure 8-move comms only (cap 8), and a line with no length is for 20-move skeletons.

**What is new here**

- **Which 2c2c is the cheap one depends on your alg list.** It flips because only the pure one has 10-move algs; a twisted one has none under 12. Mean added on 20-move skeletons:

  | Algs allowed | Twisted 2c2c: mean added | Pure 2c2c: mean added |
  |---|---:|---:|
  | 8-movers | 8.73 | 9.13 |
  | every alg up to 10 moves (500 skeletons each) | 8.66 | 8.48 |

  The cap-10 order is cpaul's ("9 for pure 2-2", "9.5 for 2-2 with a twist"), and it's **computer only** unless you've learned the 10-move pure 2c2c algs. With the 8-movers you actually insert by hand, the twisted one is cheaper.
- **By cost a 2c2c beats a 3c1t, and a 3c1t beats a 5c.** That answers jisu101's "2c2c, 3c1t, or 5c?" ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125109978632212), [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125157483315321)). A 2c2c is 0.77 to 1.17 cheaper than a 3c1t (20 moves, 8-movers), so argonblue's "3c1t > 2c2c > 5c" has the first two swapped (a typical skeleton of each is example [a] in section 10). It's about a move on average, and the spread from one skeleton to the next is wider than that, so you won't really notice it solve by solve.
- **wen's question, answered**: "Why is there even a difference if the number of possible first insertions is the same tbh" ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443790851443785758)). For the two kinds of 2c2c the number really is the same, 24 first comms per spot, and when the two comms don't touch they cost the same (9.41 and 9.40). The 0.40 between them comes from comms that interact, 0.25 of it from nesting: the best twisted pair is nested on 24% of skeletons, the best pure pair on 5.1%. Across types the number isn't the same, and the costs come in the same order (first line of the next block):

  | Leftover | First comms that leave a 3c, per spot |
  |---|---:|
  | 2tc | 108 |
  | 2c2c | 24 |
  | 3tc | 18 |
  | 3c1t | 9 |
  | 5c | 5 |

  ✓ Lean: these counts, for every leftover of each type.

- **A longer alg list is worth far more on two comms than on one.** Same skeletons under every cap (100 of 20 moves per type):

  | Leftover | Cap 8: mean added | Cap 10: mean added | Cap 12: mean added |
  |---|---:|---:|---:|
  | pure 2c2c | 9.26 | 8.40 | 7.87 |
  | 5c | 10.10 | 9.79 | 9.49 |
  | 3tc | 9.41 | 9.32 | 8.56 |

  The 3tc's whole step from cap 10 to cap 12 comes from longer comms, since no 3tc alg is 12 moves or fewer. Where a 10-move pure 2c2c alg fits (62% of skeletons) it beats two 8-movers by 0.62. Caps 10 and 12 count every alg of that length, so these are **computer only**, the answer key for a full alg list. What carries over to an attempt is which algs are worth learning (the 10-move pure 2c2c algs, 6.3).
- **Longer algs barely help a 3c.** At 20 moves it's 5.90 with 8-movers, 5.85 with every alg up to 10 moves and 5.77 up to 12. How often a longer alg is what wins, on 20-move skeletons:

  | What happens | Share of skeletons |
  |---|---:|
  | An 8-mover is as good as anything up to 10 | 95% |
  | A 9-mover is the best | 0.61% |
  | A 10-mover is the only best (example [b]) | 4.7% |
  | of those, the 10-mover wins by a single move | 77% |

  A 10-mover as the only best is about one skeleton in 21. So the tutorial's "extremely rarely" holds for 9-movers. Ben's "if its a setup to a regular comm then it wont cancel more than just inserting 8 movers" holds on all but 0.43% of 20-move skeletons, and those are an 8-mover put inside a turn of the skeleton (a `B'` done as `B2`, the comm, `B`; example [i]). For a hand search on a 3c, 8-movers are enough.
- **The best first comm isn't always the one to follow.** On a 20-move 5c with 8-movers the best first comm is an 8-3 or better on 80% of skeletons (a 3c's best comm: 29%), but taking it and then the best second doesn't always give the best pair:

  | How you search | Misses the best pair on, share of skeletons | Mean moves added |
  |---|---:|---:|
  | best first comm, then the best second | 14% | 10.54 |
  | also first comms one move worse (Insertion Finder's greedy 1) | 3.7% | 10.41 |
  | also two moves worse (example [f]) | 0.48% | 10.38 |
  | best pair of comms (computer) | | 10.37 |

  With every 3c alg up to 10 the best first comm misses the best pair on 20%, and the longer list actually gives a longer result than 8-movers alone on 0.25% of 1,998 skeletons (shorter on 9.3%). That's what bvcuber13 and Ben ran into on Insertion Finder; it happens, but not often (example [l]). The best pair is a computer number. Best first comm then best second is the hand search, and also following the first comms a move worse is the hand fix.
- **Checking every other move** (3c, 8-movers):

  | Which spots you check | Finds the best, share of skeletons | Finds a best of 8-3 or better, share of those skeletons |
  |---|---:|---:|
  | every other move | 89% | 97% |
  | every third move (example [j]) | 72% | 75% |

  Every other move loses 0.11 of a move on average, and nothing better than an 8-4 was missed on any of 140,000 skeletons. Every miss of an 8-3 or better sits next to two moves on opposite faces (371 of 371 at 20 moves): a full cancel reaches across the pair, so the alg moved one move over would go between the two moves of the pair, swapped. So check every other move and both sides of a parallel pair. notkevin's "guarantees" ([7 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1436457200880189582)) is a bit too strong (example [c]).
- **paulduc03's question, answered**: after a case that needs 10 moves, "can I go 3 moves further instead of 2" ([30 Dec 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1455642235449114665))? No, like DougCube said. That walk misses a best of 8-3 or better on 3.9% of walks against 3.2% for plain every other move, and every one of the 80 3-cycles that need 10 moves can be at a case with an 8-mover two moves later (example [k]).
- **Exchange rates, 8-movers** (Fanti's question, [5 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1247972528425799841)): how many moves shorter each skeleton has to be to give the same expected total as a 20-move 3c.

  | Leftover | Shorter by, moves |
  |---|---:|
  | 5c | 4.8 |
  | 3c1t | 4.4 |
  | 3tc | 4.0 |
  | pure 2c2c | 3.5 |
  | twisted 2c2c | 3.0 |
  | 2tc | 2.0 |

  For the same chance of a given result the rates are about the same, a bit lower when the 3c would need luck. asacuber's "maybe like 5-6" ([5 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1247972799151341690)) for the 5c is right, at the 5 end. With algs up to 10 a 5c needs about 3.8 to 4.9 and a pure 2c2c about 1.8 to 3.9 (**computer only**: that assumes every alg up to 10). The cap-8 rates are for the attempt, but they price a two-comm skeleton at its best pair. Taking just the best first comm by hand adds 0.16 on a 5c and 0.31 on a twisted 2c2c (8.4), so add that to the rate if you won't follow up more than the best first comm.
- **trig0n's 17 to 3c** ([23 Sep 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1022791984907296778); nobody replied). Modelled 17-move sequences, 20,000 each, with 8-movers:

  | The moves | Mean moves added | Adds 6 or less | Nothing fits |
  |---|---:|---:|---:|
  | random moves | 6.02 | 66% | 0.80% |
  | after EO | 6.05 | 66% | 0.72% |
  | DR moves | 6.08 | 64% | 0.62% |
  | DR moves, a 3c that DR moves can leave | 6.18 | 56% | 2.5% |

  So the DR guide's feeling that 8-movers cancel less on DR skeletons, which it says hasn't been proved, is true in this model, by 0.16 of a move, and it comes from which corners are left, not from the moves. These are move sequences, not DR solves.
- **Nesting matters on a 5c.** With 8-movers on 20-move skeletons the best pair of comms is nested on 24% of 5c skeletons, and forbidding it costs 0.30; two comms that don't touch at all cost 0.58 more than the best. So the nested pair argonblue saw Insertion Finder return is no rarity (example [e]). With algs of up to 10 moves the best is a nested pair on 11% (2,000 skeletons). Finding the best pair is a computer search; the hand version is Gezza Cubing's: on a 5c, also try the second comm inside the first (6.5).
- **Real move sequences with a random leftover cost what random ones cost.** 201 worked examples, 191 distinct skeletons: 168 examples from the server and 33 from Kalbarczyk's example solves, searched the same way. With 8-movers:

  | Leftover on the real moves | Real moves: mean added | Random moves: mean added |
  |---|---:|---:|
  | a random 3c (the same) | 6.01 | 6.00 |
  | a random 5c (within a tenth of a move) | 10.48 | 10.54 |
  | the posted 3c, their own leftover | 5.12 | 5.98 |

  So blocks, pairs and triggers in the moves make next to no difference to how insertions cancel. The posted skeletons with their own leftover are cheaper, and selection is part of that: the skeletons shown with their insertion are -1.13 from random, the 34 posted bare or in a collection -0.41. Whether those last few tenths are real or selection again, these few skeletons can't say. For a skeleton you've just found, start from the random-skeleton tables.
- **Edges depend on the alg list.** Only 9.5% of edge 3-cycles have an alg of 8 moves or fewer (corners: 52%), and the 24 with a 6-mover are exactly the 24 whose three edges are oriented on all three axes (✓ Lean, these counts). With 8 or fewer nothing fits on 44% of random 20-move skeletons; with every alg up to 10 a 3e costs 6.05 (**computer only** unless you know every edge alg up to 10). The 17 real 3e skeletons cost 3.18 at cap 10. All of them were posted with their insertion, and whether their three edges are oriented doesn't explain the difference (9.2).
- **Where the insertion is** (3c, 8-movers). No third of a random skeleton is better than another. The first and the last spot are clearly worse: an 8-3 or better there 1.1% of the time, against 4.0% at an inner spot, and the spot next to them a little worse. An 8-mover fits at about half the spots (52%). On the 89 real 3c skeletons the best spot is in the first, middle and last third 24%, 39% and 37% of the time, so DougCube's "first 1/3 or last 1/3" doesn't show up. It isn't refuted either: DougCube's stats count the insertions DougCube found, of every kind (9.4).
- **Exact counts.**
  - Two 3-cycle insertions solve exactly 3c1t, 2c2c (pure and twisted), 5c, 3c3c, 2tc and 3tc. 22 other types of corner leftover (11 by name, 8,845,836 states) need exactly three (Lean).
  - 528 of the 1,008 corner 3-cycles have an 8-mover, 336 of them two different ones. 32 of the 112 3-cycles that keep all three corners oriented have one, and 112 3-cycles have none even after any one move. ✓ Lean
  - No 2c2c alg is shorter than 10 moves (132 pure cases have a 10-mover; a twisted one needs 12). ✓ Lean up to 10 moves
  - A 3c1t has an alg of 12 moves or fewer in only 528 of 10,080 cases, a 2tc in 32 of 56 (the pairs of corners that don't share an edge).
  - No alg that leaves a corner twisted in place is shorter than 12, no three-twist is within 12, no 2c2e is shorter than 10.
- **People and Insertion Finder.** The insertion that was posted for a 3c is the best 8-mover insertion or better in 76 of 79 cases (96%), and on the corner leftovers that need two comms in 52 of 60 (87%). Against algs up to 12 (**computer only**, the answer key), 21% of the hand solutions leave a move or more on the table. On the Insertion Finder pages the search gives the same result once its cap covers the algs Insertion Finder used, and at cap 12 it's one move shorter on two pages (16 to 3C1T: 24 against 25; 13 to 3T: 22 against 23). An Insertion Finder "optimal" is optimal for the alg sets that were on: on the 23-move 3c of [16 Oct 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1296311051121463346) the posted 8-4 is the best 8-mover insertion (27), and a 10-mover that cancels all ten of its moves gives 23 (9.5).

**What it confirms or corrects**

- **The tutorial's table holds.** The two-comm leftovers, 20 moves, 8-movers, next to the tutorial's corner rows:

  | Source | 2tc | twisted 2c2c | pure 2c2c | 3tc | 3c1t | 5c |
  |---|---:|---:|---:|---:|---:|---:|
  | Best pair of 8-movers | 7.71 | 8.73 | 9.13 | 9.50 | 9.90 | 10.37 |
  | The tutorial | two twisted 8 | | double swap 9/10 | three twisted 9 | 10 | 10/11 |

  Every tutorial row is within about half a move; the 3tc is the one that's a full half move off. At 16 moves the six are 0.28 to 0.38 higher. These are best pairs of 8-movers, a computer number, but following the best first comm and the ones a move worse gets within 0.09 of them (8.4), so they hold for a careful hand search too.
- **A 3c costs +5.90 on a 20-move skeleton with 8-movers.** (That average is over the skeletons where an 8-mover fits at all; the shares after it are over every skeleton.) +6 or better on 71% of skeletons, +5 or better on 29%, +4 or better on 9.3%. It's 6.44 at 10 moves and 5.56 at 30, so length matters little. Everybody's +6 is right.
- **The estimates people posted.** cpaul's 9 and 10 are right. Phuwish's are close (2tc 7.71, 5c 10.37) except the 3tc: "mid to high 8" against 9.50 with 8-movers, and algs up to 12 bring it to 8.56 (100 skeletons). Baiqiang's are lower and, in Baiqiang's words, not averages; with algs up to 12 (**computer only**) a pure 2c2c averages 7.87 and a twisted one 8.30 (100 skeletons each), figures of that size.
- **For sub-30, 8-movers.** How often each skeleton makes it:

  | Skeleton | Chance of sub-30 |
  |---|---:|
  | 3c in 21 (kyh's "very likely") | 99.6% |
  | 3c in 23 (the tutorial's "probably") | 76% |
  | 3c in 24 | 34% |
  | 3c in 25 (the tutorial's "some luck") | 12% |
  | 5c in 18 | 80% |
  | 5c in 19 | 48% |

  The tutorial's 4 corners in 18 beat 3 corners in 25 by a lot (expected 26.9 to 28.1 against 30.7). sequesteredcuber's "sub-22 for 3C skeleton", "sub-20 for every other skeleton" puts a 3c and a 5c two moves apart, which is too close (example [g]).
- **Odds people gave.** On a 5c, Java's "you can usually do a bit better" than Zagros's 13 is right: +13 or worse is the best there is on only 1.3% of 20-move skeletons. Phuwish's "getting +9 from 2tc is as bad as +11,+12 from 5c" is right in odds (26% against 51% and 16%). An insertion that cancels more than its own length is real and rare: 0.03% of 20-move 3c skeletons (example [d]).
- **The counts people gave.** The lists of which leftovers take one, two or three comms (Riabov's guide, the tutorial, FakeMMAP, DougCube's mixed 3c3c, wen's four 7-corner leftovers) are right, proved in Lean. Against the full alg lists, torchlight's 12 moves to twist a corner in place, Noah Swor's 10 for a 2c2e, notkevin's single class of 960 ten-move 2c2e algs and bpaul's "eo on all axes" for the 6-move edge cases are right too.

---

## 2. What was asked

The questions, in the words of the people who asked them. Most got an estimate or no answer.

- trig0n ([23 Sep 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1022791984907296778)): "What's the probability of getting ≤x-move 3C insertion if I have 17 to 3C", for random moves, for moves after EO, and for a DR. "Maybe it can be found using IF". Nobody replied.
- Zagros ([1 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246424587554783313)): "what is the average moves for corner insertion?" And on a 5c, from experience: "in reality it is soooo rare I find anything better than 8-2. Usually for two corner insertions I would say the average is 13 moves for me, one 8-2 and one 8-1." Java ([1 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246425063641579541)): "i think you can usually do a bit better with 5c".
- Fanti ([5 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1247972528425799841)): "how many moves shorter should a 5c (normal cycle) skeleton be compared to a 3c (normal cycle) skeleton so that i should look at the 5c first". asacuber ([5 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1247972799151341690)): "maybe like 5-6".
- zakk drewji ([17 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1395354444249563157)): "What’s the possible Movescount from 24 to 3c?" DougCube ([17 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1395361792225443892)): "It can be anything but typically a (8-2/30)."
- tave_789 ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424237220772057129)): "How many moves should 2tc take with 2 insertions on average?" Phuwish ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424237318960709642)): "~8.0 I guess". For a 3tc ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239016290553917)): "mid to high 8 from my experience", "It's s like 2tc but a half to a move worse". tave_789 ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239312396091486)): "And isnt 3c1t and 2c2c close to 9.5?" Phuwish ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239358826778798)): "yeah". tave_789 ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239402187489310)): "I think I remember one being a lil better but i dont remember". Phuwish ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239470932131973)): "and 5c ~high 10".
- Cuber4 ([21 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1474700741145792522)): "What can I expect in terms of moves added from different insertions?" argonblue ([21 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1474741204691193969)): "Sebastiano’s tutorial has a chart. it’s highly dependent on your skill level, luck, and the particular skeleton".
- jisu101 ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125109978632212), [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125157483315321)): "if you can't find a 3c, what is generally better", "2c2c, 3c1t, or 5c?"

And one disagreement that was left standing. compLex ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443753803940892803)) asked: "how many moves do you expect to add with 3c, 3c1t, and 2c2c skeletons, respectively?" One row per answer, in moves added:

| Who | 3c | 3c1t | 2c2c |
|---|---|---|---|
| Baiqiang ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443756810715664537)) | 5-6 | 8-9 | "6-8 for good 2c2c, 8-9 for bad 2c2c" |
| cpaul ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760547458842644), [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760556908740648), [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760590995853465)) | | "like 10 for 3c1t" | "more like 9 for pure 2-2", "like 9.5 for 2-2 with a twist" |
| tave_789, two months earlier ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239312396091486)): "close to 9.5?"; Phuwish ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239358826778798)): "yeah" | | close to 9.5 | close to 9.5 |
| The tutorial's table | 5/6 | 10 | 9/10 (its row is the double swap; the twisted double swap has no row) |

kyh ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443757408114708600)): "6-8 for good 2c2c?????" And ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443757686025093241)): "btw you mean good like as in the co matches, the stickers swap with eachother". Nobody answered that, so which 2c2c is the good one is not on record. cpaul ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760361856565319)): "I don't think 2c2c is 6-8 lol". Jay ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443789835356606609)): "maybe there's some non 3c type insertion method for 2c2c that lowers the movecount that far idk, but yeah ime when i was doing blocks i didn't notice a meaningful different between 2 insertion 4c types other than 2c2c being easier practically with rNISS". wen, four minutes later ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443790851443785758)): "Why is there even a difference if the number of possible first insertions is the same tbh". Baiqiang, the next day ([28 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443860338440146986)): "this is i expected not avg expected".

On which 4c or 5c to prefer there were two views. argonblue ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125544114131034)): "i think 3c1t > 2c2c > 5c. mostly because a twist gives you the most freedom to pick comms". jisu101 ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125667565080657)): "True but so does 2c2c, you can pick literally any comm with 3 of the 4 corners".

Sections 6 and 7 answer these. In short: the tutorial's corner rows and cpaul's 9 and 10 are what 8-movers give on a random skeleton, each within about half a move. Phuwish's figures are close, except for the 3tc. Baiqiang's are lower and are not averages. And by cost the order is 2c2c, then 3c1t, then 5c.

---

## 3. What an insertion is here

**The setup.** A skeleton is a sequence of $n$ moves that solves the scramble except for a *leftover*: a 3c, a 5c and so on. There are $n + 1$ places to insert, before the first move, between any two, and after the last. At each place exactly one cube state has to be produced by the inserted alg (it is the leftover carried through the moves that follow), so the only freedom is which alg for that state, and where.

**The cost** of an insertion is what it adds: the length of the solution with the alg in it and all cancelling done, minus $n$. An `(8-2)` costs +6. Cancelling is done the way you do it on paper: moves on the same face merge (`R R` is `R2`, `R R'` is nothing), moves on opposite faces commute, and it repeats as far as it goes, so an alg can also cancel into moves two or three deep, and moves on either side of it can meet through it.

**Why there has to be a cap.** If an alg of any length were allowed, the best insertion would be the optimal solution of the whole scramble written as one alg at one spot. Nobody means that by an insertion. So every number here is for a cap on the length of each inserted alg, and I give three:

| Cap | What it stands for |
|---:|---|
| 8 | Pure 8-move comms for corners. For edges: the 6-, 7- and 8-move algs. This is what most people insert, and it is Insertion Finder's "Pure 3 Corners" set (Baiqiang, [21 Aug 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1407986882700382259): "Pure 3 corners includes 8 moves comms only. The other one includes some 10 moves"). |
| 10 | Everything up to 10 moves: the 9-movers (a setup move that cancels into an 8-mover), the 10-move sledge comms, the 10-move 2c2c algs. |
| 12 | Everything up to 12: also the 12-move two-twist comms, triple sexy and the like. |

Within the cap *every* move sequence that does the job counts, not a list of known algs. So cap 8 on a 3c is the true best over all 8-movers at all spots of the skeleton as written (section 11 has the one kind of spot that leaves out), and cap 12 is every sequence of up to 12 moves, far more than any list a person knows. Cap 8 is the hand number: checking every spot with 8-movers is what solvers do. Caps 10 and 12 are **computer only** (unless you have learned the 10- and 12-move algs of that leftover): they say what a full alg list would give, which is an answer key, not a search to run in an attempt.

**What may be inserted.** Four ways of solving a leftover, each searched exactly:

| Name here | What it is | Used for |
|---|---|---|
| one comm | one 3-cycle alg, at the best spot | 3c, 3e |
| two comms | two 3-cycle algs, one after the other. The second may go anywhere in the solution the first one gave, also inside the first alg (nested) | 5c, 2c2c, 3c1t, 2tc, 3tc, 3c3c and the edge types |
| one alg | one alg that does the whole leftover at once, like a 10-move 2c2c alg or triple sexy | any leftover that has an alg within the cap |
| a comm plus an alg | two insertions where only one has to be a 3-cycle comm; the other is any alg within the cap that does a whole leftover in one go (a 2c2c alg, a two-twist, a 5-cycle alg) | compared separately, on fewer skeletons; Insertion Finder with all its sets on does part of this |

Unless a table says otherwise, a number for a two-comm leftover is the best of *two comms* and *one alg*. *A comm plus an alg* is kept apart because it is expensive to search and few people insert that way. With long algs it also starts to be something else: two algs wrapped around a stretch of the skeleton can cancel into less than the stretch, which is rewriting the solution more than inserting into it. Read it as the ceiling of what an unlimited alg list could do: **computer only**.

**Random skeletons.** The big tables are over random skeletons: each move is drawn at random (never two in a row on one face), and the leftover is drawn at random among all leftovers of its type. A random skeleton is a move sequence, not a solve. It has no blocks, no EO, and it doesn't end in a last-layer alg. Section 9 puts 201 worked examples from real solves (191 distinct skeletons) next to them, and two things come out of that:

- The same real move sequences with a random leftover on them cost what random sequences cost (the same for a 3c, within a tenth of a move for a 5c), so the tables aren't skewed by how skeletons are written.
- The skeletons people post, with their own leftover, come out most of a move cheaper than the tables with 8-movers. Selection is part of that: for a 3c, the skeletons posted with their insertion are -1.13 from random and the 34 less-picked ones -0.41. For edges the posted skeletons are further from the random tables (6.6, 9.2).

**How many.** Sample sizes per skeleton length, one row per run; each table also says which.

| What was run | Skeletons per length |
|---|---|
| cap 8, every type but 2tc, 2fe and the two kinds of 2e2e, each even length from 10 to 30 | 20,000 |
| the same for 2tc, 2fe and the two kinds of 2e2e | 5,000 |
| the same for the corner types of section 7 (3c, 2tc, 3tc, both 2c2c, 3c1t, 5c) at every odd length from 11 to 29 | the same size |
| cap 10, a 3c or a 3e, and one alg | 20,000 |
| cap 10, two comms (the search is slow there), 5c and 3c3c | 2,000 |
| the same for 2c2c, 3c1t and 3tc | 500 |
| the same for 2tc | 200 |
| cap 12, two comms, skeletons of 20 moves, for 3tc, pure 2c2c, twisted 2c2c, 3c1t, 5c, 3c3c, 3e1f, 5e and 3e3e (not for 2tc, 2fe, 2e2e and flipped 2e2e) | 100 |
| cap 10, a comm plus an alg, skeletons of 20 moves | 200 |

---

## 4. How many insertions each leftover needs

This part is exact: every pair of corner 3-cycles was multiplied out, then every triple, and the same for edge pairs. The counts are proved in Lean (Appendix C).

**One or two.** Two corner 3-cycles make exactly 7 kinds of leftover by name, and two edge 3-cycles exactly 6, and they make every state of each kind. The Lean statement counts the two twist directions apart (three corners twisted clockwise and three twisted counter-clockwise are two types there, and so are the two kinds of 3c1t), which makes the 7 corner kinds 9 types. The last column gives that count for each row:

| Leftover | What is left | States | 3-cycles needed | Types when the two twist directions are counted apart |
|---|---|---:|---:|---:|
| 3c | a corner 3-cycle | 1,008 | 1 | 1 |
| 2tc | two corners twisted in place | 56 | 2 | 1 |
| 3tc | three corners twisted in place, all the same way | 112 | 2 | 2 |
| pure 2c2c | two corner swaps, no twist | 1,890 | 2 | 1 |
| twisted 2c2c | two corner swaps, each with a twist | 3,780 | 2 | 1 |
| 3c1t | a twisted corner 3-cycle and one twisted corner | 10,080 | 2 | 2 |
| 5c | a corner 5-cycle | 108,864 | 2 | 1 |
| 3c3c | two separate corner 3-cycles | 90,720 | 2 | 1 |
| 3e | an edge 3-cycle | 1,760 | 1 | 1 |
| 2fe | two edges flipped in place | 66 | 2 | 1 |
| 2e2e | two edge swaps, no flip | 5,940 | 2 | 1 |
| flipped 2e2e | two edge swaps, each with a flip | 5,940 | 2 | 1 |
| 3e1f | a flipped edge 3-cycle and one flipped edge | 15,840 | 2 | 1 |
| 5e | an edge 5-cycle | 304,128 | 2 | 1 |
| 3e3e | two separate edge 3-cycles | 591,360 | 2 | 1 |

*States* is how many different leftovers of that kind there are. Nothing else can be solved with two 3-cycle insertions: counting the solved cube and the 3-cycles themselves, two corner 3-cycles reach 216,511 corner states and two edge 3-cycles reach 925,035 edge states, and all of them are in the table.

**Three.** Counted the same way, 22 types of corner leftover need exactly three 3-cycles, 8,845,836 states in all. By what you would call them they are 11:

| Leftover | What is left | States | Types when the two twist directions are counted apart |
|---|---|---:|---:|
| 7c | a 7-cycle | 4,199,040 | 1 |
| 5c3c | a 5-cycle, a 3-cycle | 1,959,552 | 1 |
| 3c3c1t | a 3-cycle, a twisted 3-cycle, one corner twisted in place | 725,760 | 2 |
| 5c1t | a twisted 5-cycle, one corner twisted in place | 653,184 | 2 |
| 4c2c | a twisted 4-cycle, a twisted swap; or a 4-cycle, a swap | 612,360 | 3 |
| 3c2c2c | a 3-cycle, two twisted swaps; or a 3-cycle, two swaps | 408,240 | 2 |
| mixed 3c3c | two twisted 3-cycles | 181,440 | 1 |
| 2c2c1t | a swap, a twisted swap, one corner twisted in place; or two twisted swaps, one corner twisted in place | 45,360 | 4 |
| 3c2t | a 3-cycle, two corners twisted in place; or a twisted 3-cycle, two corners twisted in place | 40,320 | 3 |
| 3c3t | a 3-cycle, three corners twisted in place | 20,160 | 2 |
| 4 twisted corners | four corners twisted in place | 420 | 1 |
| **all 11** | | **8,845,836** | **22** |

What the server and the docs say about this is right, line by line:

- Yurii Riabov's guide lists "3c - 1 comm", "3s1t, 2s2s, 5s, 3s3s, 2t, 3t - 2 comms" and "All other situations (4c1t, 3c2t, 4t, 5t, etc.) are solved in more than 2 comms". The guide's six are exactly the seven two-comm corner rows above (2c2c counted once).
- Tronto on four twisted corners: "This case requires three inserted commutators." And on five corners: "the only one that requires 2 commutators is the one where the pieces make a 5-cycle. All other cases require 3 commutators, except when you have 5 corners placed but twisted: in that case you need 4." All three statements hold. Five twisted corners are not among the states three 3-cycles reach, and a 3tc plus a 2tc does them in four.
- FakeMMAP ([9 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1459235380166525029)): "the only way to affect 5 corners with 2 3-cycles, is to do a 5-cycle." Right.
- DougCube's *mixed* 3c3c ([9 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1459256777555185872)), "which although it doesn't have parity, it cannot be solved with only two 3c comms": right. It is the two twisted 3-cycles of the second table, 181,440 states, and it takes three.
- wen ([29 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1134857937907613789)): "Also theres 4 types of 7c that work!" torchlight listed three ([29 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1134858381644025927): "these three?", "7-cycle", "one normal 3-cycle, one twisted 3-cycle, one twist", "one normal 3-cycle, two 2-cycles (normal/twisted)") and asked "what's the fourth" ([29 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1134858425407381544)). wen ([29 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1134860037613957220)): "I counted your last one as 2 separate". Counted wen's way, those are exactly the four leftovers on seven corners that three comms solve: the 7c, the 3c3c1t, and the 3c2c2c with plain swaps and with twisted swaps. Any other leftover on seven corners needs more.
- 2c2c1t "has to be done with 3 comms" (Java, [12 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1128541440314707968)), 5c1t is "Another 3 comms skeleton" (Renny, [9 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1459252311934111987)): both right.
- Two flipped edges by two 3e algs (DougCube's 19, [22 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1419687244955910226)): right, 2fe is a two-comm leftover. A pair of *flipped* edge 3-cycles is not: Kalbarczyk's "3E3E in 15, unfortunately with orientation change (you can’t solve them with 2 pure 3-cycles)" is exact.

Everything below is about the leftovers of the first table. What a three-comm leftover costs is not measured here.

---

## 5. The algorithms

For every leftover of every type, all move sequences of 12 moves or fewer that solve it were listed. The counts are reference: which case has an 8-mover is something you learn to recognise, not look up, and the lists of 10- and 12-movers are **computer only**. First the shortest alg per state:

| Leftover | States | 6 moves | 7 moves | 8 moves | 9 moves | 10 moves | 11 moves | 12 moves | more than 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3c | 1,008 |  |  | 528 | 336 | 80 | 48 | 16 |  |
| 2tc | 56 |  |  |  |  |  |  | 32 | 24 |
| 3tc | 112 |  |  |  |  |  |  |  | 112 |
| pure 2c2c | 1,890 |  |  |  |  | 132 | 222 | 630 | 906 |
| twisted 2c2c | 3,780 |  |  |  |  |  |  | 2,172 | 1,608 |
| 3c1t | 10,080 |  |  |  |  |  |  | 528 | 9,552 |
| 5c | 108,864 |  |  |  |  | 1,152 | 2,976 | 21,408 | 83,328 |
| 3c3c | 90,720 |  |  |  |  | 704 | 1,296 | 16,952 | 71,768 |
| 3e | 1,760 | 24 | 48 | 96 | 432 | 864 | 264 | 32 |  |
| 2fe | 66 |  |  |  |  |  |  |  | 66 |
| 2e2e | 5,940 | 18 | 30 | 171 | 432 | 990 | 1,320 | 2,526 | 453 |
| flipped 2e2e | 5,940 |  |  |  |  | 1,536 | 1,704 | 2,136 | 564 |
| 3e1f | 15,840 |  |  |  |  |  |  | 4,224 | 11,616 |
| 5e | 304,128 | 192 | 480 | 2,112 | 5,472 | 22,992 | 54,144 | 112,800 | 105,936 |
| 3e3e | 591,360 | 96 | 240 | 1,296 | 3,552 | 16,704 | 48,144 | 135,720 | 385,608 |
| 2c2e | 11,088 |  |  |  |  | 384 | 768 | 2,784 | 7,152 |

Read the 3c row as: 528 of the 1,008 corner 3-cycles have an 8-mover, 336 need 9 moves, and so on. And the number of different algs of each length, over all states of the type:

| Leftover | 6 moves | 7 moves | 8 moves | 9 moves | 10 moves | 11 moves | 12 moves | Up to 8 | Up to 10 | Up to 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3c |  |  | 864 | 1,728 | 11,856 | 29,664 | 197,664 | 864 | 14,448 | 241,776 |
| 2tc |  |  |  |  |  |  | 144 | 0 | 0 | 144 |
| 3tc |  |  |  |  |  |  |  | 0 | 0 | 0 |
| pure 2c2c |  |  |  |  | 1,296 | 3,768 | 49,440 | 0 | 1,296 | 54,504 |
| twisted 2c2c |  |  |  |  |  |  | 8,544 | 0 | 0 | 8,544 |
| 3c1t |  |  |  |  |  |  | 576 | 0 | 0 | 576 |
| 5c |  |  |  |  | 1,680 | 4,416 | 66,048 | 0 | 1,680 | 72,144 |
| 3c3c |  |  |  |  | 3,480 | 10,176 | 124,608 | 0 | 3,480 | 138,264 |
| 3e | 96 | 240 | 2,496 | 5,904 | 50,688 | 141,600 | 839,616 | 2,832 | 59,424 | 1,040,640 |
| 2fe |  |  |  |  |  |  |  | 0 | 0 | 0 |
| 2e2e | 144 | 312 | 3,912 | 9,096 | 63,312 | 216,240 | 1,321,296 | 4,368 | 76,776 | 1,614,312 |
| flipped 2e2e |  |  |  |  | 3,168 | 8,064 | 74,688 | 0 | 3,168 | 85,920 |
| 3e1f |  |  |  |  |  |  | 8,544 | 0 | 0 | 8,544 |
| 5e | 192 | 480 | 2,592 | 7,392 | 62,112 | 207,744 | 1,469,184 | 3,264 | 72,768 | 1,749,696 |
| 3e3e | 96 | 240 | 1,920 | 4,944 | 48,720 | 176,112 | 1,348,464 | 2,256 | 55,920 | 1,580,496 |
| 2c2e |  |  |  |  | 960 | 6,768 | 34,272 | 0 | 960 | 42,000 |

**Corner 3-cycles.**

- **About half have an 8-mover**: 528 of 1,008. So at a random spot in a skeleton there is a pure comm about half the time, and that is what the per-spot count in section 8 shows.
- **Two ways or one.** Of the 528, 336 have two different 8-movers and 192 have only one. Gezza Cubing ([20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253275920970551347), [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253278252026564668)): "for most 3c cases theres 2 ways to do the commutator", then "i reckon about half of the 8 movers you can do 2 ways". It is 64% of the cases that have an 8-mover. eff asked ([20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253302165154304010)): "i feel like every 8 mover has two ways no". rogo ([20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253304211752484905), [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253304286931062805)): "no", "U2, R' D R doesn't for example". That one is among the 192.
- **The rest**: 336 states need a 9-mover (Ben's "1 move setup that cancels with an 8 mover like R2 D R' U2 R D' R' U2 R'", [26 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1476513296981950494)), 80 need 10, 48 need 11 and 16 need 12.
- **Oriented corners.** Zagros ([26 Apr 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1365885825166082088)): "There arent 8 movers if they're oriented". Jay answered with one that is ([26 Apr 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1365886921221341216)): "R' F' R B2 R' F R B2". Counting them: of the 112 3-cycles that keep all three corners oriented (U or D sticker on U or D), 32 have an 8-mover and the other 80 do not. So it is mostly true, and Jay's is one of the exceptions.
- **Cases where you can skip a spot.** Srećko ([9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414947538515005494)): "theres a case where any single move you do doesnt give a pure comm (something like UFR UBL DFL), so you can skip one move from it". Right, and it is more than one case: 112 of the 1,008 3-cycles have no 8-mover and still have none after any one move. The UFR UBL DFL of the example (three corners no two of which share an edge, untwisted) is 16 of them, the ones whose shortest alg is 12 moves.
- **10-movers** are plenty: 11,856 ten-move algs against 864 eight-movers. They are, as Ben says ([25 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1465081653192818698)), "sledge comms and cyclic shifts". What they buy is in 6.1.

**Twists.**

- **2tc**: nothing under 12 moves. 32 of the 56 cases have a 12-mover, like the tutorial's

  ```
  [F L' D2 L F', U2]   // the tutorial's two-twist
  ```

  and they're the pairs of corners that don't share an edge. The 24 cases with two neighbouring corners need 13 or more.
- **Twisting one corner in place.** torchlight ([27 Aug 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1145356913731715073)) went further: "optimal to twist one corner while preserving all edges is 12 moves", with a pure two-twist and "(R U' R U' R U2)2", which twists two corners the same way and swaps two pairs, as examples. That's right as stated. Of all move sequences of 11 moves or fewer that keep every edge, none leaves a corner twisted in its place, whatever else it does to the corners. At 12 moves 4,464 sequences do, reaching 4,160 states:

  | 2tc | 3c1t | kinds two comms can't solve (torchlight's second example among them) |
  |---:|---:|---:|
  | 32 | 528 | 3,600 |

- **3tc**: no alg of 12 moves or fewer for any of the 112 cases. The tutorial's alg and DougCube's ([9 Jun 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1381689489784573992)) are 13 and 13 moves, so 13 is the shortest for that case:

  ```
  U' B U' F U2 B2 D' R2 U D F' U' B   // the tutorial's
  R L U2 R' F2 L2 B L' F L' F L' B'   // DougCube's
  ```


**Double swaps.** The two kinds are told apart the way the tutorial does. A *pure* 2c2c is two swaps that each close on themselves: do it twice and all four corners are back (the tutorial's "double swap"; triple sexy and triple sledge are pure in this sense). A *twisted* 2c2c leaves a twist in each swap: do it twice and you have four twisted corners (the tutorial's "twisted double swap").

- **Pure 2c2c: the shortest alg is 10 moves.** kyh ([29 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1399733098836394074)): "what's the shortest 2c2c alg". zakk drewji ([29 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1399740709698801775)): "I think it’s 10?" Yes. 132 of the 1,890 cases have a 10-mover, 222 need 11 and 630 need 12. Here's one of the ten-movers, from the "DR algs with mnemonics" sheet that Riabov's guide links:

  ```
  R2 U' L2 D B2 R2 D' L2 U F2   // from the DR algs sheet
  ```

- **Twisted 2c2c: 12 moves** at the least, for 2,172 of 3,780 cases.
- **3c1t**: 12 at the least, and only for 528 of 10,080 cases. **5c**: 10 at the least, for 1,152 of 108,864.

**Edges.**

- **Only 9.5% of the edge 3-cycles have an alg of 8 moves or fewer** (for corners it's 52%). Out of 1,760:

  | 6 moves | 7 | 8 | 9 | 10 |
  |---:|---:|---:|---:|---:|
  | 24 | 48 | 96 | 432 | 864 |

  So the typical edge 3-cycle needs 9 or 10 moves. The six-movers are this one and its relatives:

  ```
  R L' U2 R' L F2   // a six-mover
  ```

- That is the whole reason edge insertions behave differently, and it is what people describe. FakeMMAP ([3 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1390246333834596463)): "3e insertions have huge variance in non-DR solves." bpaul ([10 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1470815636128010393)): "oh yeah the 6 move cases require eo on all axes". Exactly so: the 24 cases with a 6-mover are the 24 3-cycles whose three edges are oriented on all three axes, and an alg of 8 moves or fewer needs them oriented on at least two (table in 9.2). DougCube ([10 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1470815044316168193)): "when you have a fairly complete set of 3e insertion algs, then EO doesn't matter anymore". With every alg up to 12, every 3e has one; section 6.6 has what each cap costs.

**Parity.** A 2c2e leftover is not sampled in this study, but its algs were listed:

- There are 11,088 such states. argonblue ([9 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1536138775816704062), [9 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1536141220403748894)): "there’s only 1848 possible 2c2e states", then "oh wait actually 6x as many cases, because orientations". 1848 times 6 is 11,088.
- **No 2c2e alg is shorter than 10 moves.** Noah Swor ([15 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1394725607153209354)): "10 moves is the minimum for any 2E2C without cancellations". Right. 384 states have a 10-mover, 768 need 11, 2,784 need 12 and 7,152 need more.
- **All 960 ten-move 2c2e algs are one alg**, up to turning the cube, mirroring, inverting and cyclic shifts, for example

  ```
  R' U F2 D' L D F2 U2 R U   // one of them
  ```

  notkevin ([15 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1394776450522943659)): "every 10-move 2e2c is a cyclic shift of this alg or its inverse (up to rotations/mirrors ofc)". Confirmed.
- Fanti's question ([9 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1536121634392510464)), "does someone know what Gods Number for 2e2c states is", stays open: it is more than 12.

---

## 6. What each type costs

How to read the tables of this section. A row is one cap and one skeleton length. *Mean moves added* is the average of what the best insertion adds, over the skeletons where something fits. The columns *Adds k or less* are the share of all skeletons whose best insertion adds k moves or fewer. *Nothing fits* is the share with no alg within the cap at any spot. Everything is for random skeletons (section 3), and the first column is the cap. The cap-8 rows are what checking every spot with 8-movers gives, a target for the attempt; the cap-10 and cap-12 rows count every alg of that length and are **computer only**, the answer key for a full alg list.

### 6.1 A 3c

**3c: one comm. Random skeletons, 20,000 per row. Cap 8 is 8-movers only; caps 10 and 12 allow every alg up to that length.**

| Cap | Skeleton length | Skeletons | Mean moves added | Adds 2 or less | Adds 3 or less | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 10 | 20,000 | 6.44 | 0.37% | 1.2% | 4.6% | 15% | 46% | 82% | 96% | 4.2% |
| 8 | 14 | 20,000 | 6.20 | 0.47% | 1.6% | 6.4% | 21% | 58% | 89% | 98% | 1.7% |
| 8 | 18 | 20,000 | 5.98 | 0.72% | 2.5% | 8.5% | 27% | 67% | 94% | 99.4% | 0.65% |
| 8 | 20 | 20,000 | 5.90 | 0.73% | 2.7% | 9.3% | 29% | 71% | 96% | 99.6% | 0.36% |
| 8 | 22 | 20,000 | 5.82 | 0.69% | 2.7% | 10% | 32% | 75% | 97% | 99.8% | 0.24% |
| 8 | 26 | 20,000 | 5.68 | 0.96% | 3.3% | 12% | 37% | 80% | 98% | 99.9% | 0.08% |
| 8 | 30 | 20,000 | 5.56 | 1.0% | 3.7% | 14% | 42% | 84% | 99% | 99.9% | 0.05% |
| 10 | 10 | 20,000 | 6.46 | 0.42% | 1.4% | 5.0% | 16% | 48% | 85% | 98% | <0.01% |
| 10 | 14 | 20,000 | 6.17 | 0.51% | 1.8% | 6.9% | 23% | 60% | 92% | 99.3% | 0 |
| 10 | 18 | 20,000 | 5.93 | 0.80% | 2.7% | 9.2% | 29% | 69% | 96% | 99.8% | 0 |
| 10 | 20 | 20,000 | 5.85 | 0.78% | 2.9% | 10% | 31% | 73% | 97% | 99.9% | 0 |
| 10 | 22 | 20,000 | 5.76 | 0.79% | 3.0% | 11% | 34% | 76% | 98% | 99.9% | 0 |
| 10 | 26 | 20,000 | 5.62 | 1.1% | 3.6% | 13% | 39% | 82% | 99% | 99.9% | 0 |
| 10 | 30 | 20,000 | 5.50 | 1.1% | 4.1% | 15% | 44% | 86% | 99.4% | 100% | 0 |
| 12 | 10 | 20,000 | 6.40 | 0.47% | 1.5% | 5.5% | 18% | 50% | 86% | 99% | 0 |
| 12 | 14 | 20,000 | 6.10 | 0.56% | 2.0% | 7.6% | 25% | 62% | 94% | 99.6% | 0 |
| 12 | 18 | 20,000 | 5.85 | 0.90% | 3.0% | 10% | 32% | 72% | 97% | 99.9% | 0 |
| 12 | 20 | 20,000 | 5.77 | 0.93% | 3.4% | 11% | 34% | 75% | 98% | 99.9% | 0 |
| 12 | 22 | 20,000 | 5.68 | 0.98% | 3.5% | 13% | 37% | 79% | 99% | 99.9% | 0 |
| 12 | 26 | 20,000 | 5.53 | 1.3% | 4.3% | 15% | 42% | 84% | 99.3% | 99.9% | 0 |
| 12 | 30 | 20,000 | 5.42 | 1.3% | 4.7% | 17% | 48% | 88% | 99.6% | 100% | 0 |

- **+5.90 at 20 moves with 8-movers.** Everybody's +6 (Aneurin, Jay, Eli Rogers, Baiqiang's 5-6, Tronto's 5/6) is the right number. Share of skeletons that give:

  | +6 or better | +5 or better | +4 or better | +3 or better |
  |---:|---:|---:|---:|
  | 71% | 29% | 9.3% | 2.7% |

- **Length matters, slowly.** From 6.44 at 10 moves to 5.56 at 30: ten more moves of skeleton take 0.44 off the insertion. That's the tutorial's "longer skeletons give more spots where you can insert an algorithm, and so better chance of cancellations", in numbers. The tutorial adds "but you shouldn’t choose a long skeleton instead of a short one because of this!", and the number agrees: ten moves of skeleton buy less than half a move of insertion.
- **zakk drewji's 24 to 3c**: DougCube's "typically a (8-2/30)" ([17 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1395361792225443892)) is the single most likely outcome, 43% of skeletons. 77% get 30 or better and 11% get 28 or better.
- **No 8-mover at all** is rare but real: 0.36% of 20-move skeletons and 4.2% of 10-move ones have no spot where an 8-mover solves the three corners (one is written out below). That is the 19-move skeleton of [5 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424362235312214127) ("its not even an 8-0 its an 9-0"). An 8-0 as the best there is: 3.8% at 20 moves.
- **Longer algs give little on a 3c**: 5.85 at cap 10 and 5.77 at cap 12, against 5.90. Section 8.2 has how often a longer alg is the best.

A 20-move skeleton with no 8-mover at any spot:

```
R' U' F L2 D' R2 F2 U R2 D' F2 R2 F2 R2 D L' F' L R' D U R F' D' L R' U' F   // scramble
R2 U2 D R' U B' L' U' F2 D2 F2 R2 L B2 D' B' R2 B' R2 L2                     // skeleton (20)
```

It leaves a corner 3-cycle: DFL → UBL → UFL → DFL.

**With 8-movers**: nothing. At none of the 21 spots does the case have an 8-move alg.

**Best with algs of up to 10 moves**: 28 in all, a 10-mover.

```
R2 U2 D R' U B' L' U' F2 D2 F2 R2 L B2 D' B' R2 * B' R2 L2
* = R B R' D2 R B' R' B D2 B' // (10-2/28)
Solution: R2 U2 D R' U B' L' U' F2 D2 F2 R2 L B2 D' B' R' B R' D2 R B' R' B D2 B2 R2 L2 (28)
```

Shortest alg for the case at each spot, from before the first move to after the last: 9, more than 10, more than 10, more than 10, more than 10, 10, 10, 9, 9, more than 10, more than 10, 9, 9, 9, more than 10, more than 10, more than 10, 9, 9, 9, 9.

**trig0n's question, 17 to 3c, all three versions.** trig0n asked ([23 Sep 2022](https://discord.com/channels/1007840975726575667/1007841335434285126/1022791984907296778)) for the chance of a ≤x-move insertion with "Random" moves, with "EO in 5, then random moves which don't break EO", and with "EO in 4, DR in 10, then DR moves". The three are modelled as move sequences, not solved: 17 random moves; 5 random moves and then 12 without quarter turns of F or B; 4 random moves, 6 without quarter turns of F or B, and 7 moves of the DR group. The 3c is random, except in the last pair of rows, where it is one of the 112 3-cycles that DR moves can leave (all three corners keep their U or D sticker on U or D). 20,000 skeletons each.

| 17 to 3c with | Cap | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| random moves | 8 | 6.02 | 8.0% | 26% | 66% | 94% | 99.2% | 0.80% |
| random moves | 10 | 5.98 | 8.6% | 28% | 68% | 96% | 99.7% | 0 |
| EO in 5, then moves that keep EO | 8 | 6.05 | 6.9% | 24% | 66% | 94% | 99.3% | 0.72% |
| EO in 5, then moves that keep EO | 10 | 6.00 | 7.6% | 26% | 67% | 96% | 99.7% | 0 |
| EO in 4, DR in 10, then DR moves; any 3c | 8 | 6.08 | 6.5% | 23% | 64% | 95% | 99.4% | 0.62% |
| EO in 4, DR in 10, then DR moves; any 3c | 10 | 6.03 | 7.1% | 25% | 66% | 96% | 99.8% | 0 |
| EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave | 8 | 6.18 | 7.5% | 22% | 56% | 87% | 98% | 2.5% |
| EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave | 10 | 6.04 | 11% | 28% | 61% | 92% | 99.2% | <0.01% |

- **Random moves**: +5 or better 26%, +6 or better 66%, +7 or better 94% with 8-movers.
- **Keeping EO changes nothing**, and DR moves by themselves change next to nothing (6.08 against 6.02).
- **What a DR leaves does matter, a little**: with a 3c that DR moves can leave, 8-movers give 6.18, +6 or better only 56% of the time, and no 8-mover anywhere on 2.5%. Oriented corners have few 8-movers (section 5). With 10-movers the gap nearly closes (6.04 against 5.98).
- That is the old line in the Fokianos and Raposio guide, "there is the feeling that 8 move commutators cancel less moves on average on DR skeletons compared to regular ones, although we don’t think this has been proved yet", and trig0n's "after DR you often get something like 8-1" ([16 Jun 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1119294685928763403)): in this model it is true, by 0.16 of a move, and it comes from which corners are left, not from the moves. These are modelled skeletons, not DR solves; a real DR skeleton may differ.

### 6.2 Two comms: 2tc, 2c2c, 3tc, 3c1t, 5c

For these, cap 8 means two 8-move comms, the second allowed inside the first; no alg of 8 moves or fewer does any of them in one go.

Each number is the **best pair**, every first comm at every spot followed by the best second: **computer only** as a search. By hand you take the best first comm and then the best second, which costs 0.16 more on a 5c; also following the first comms a move worse gets within 0.09 of the best pair on every type (8.4). So read the cap-8 rows as a careful hand search, a few hundredths optimistic.

Cap 10 is the best of two comms of up to 10 moves and one alg of up to 10 for the whole leftover. All on random skeletons; the *Skeletons* column says how many each row rests on, and at cap 10 that is few, so read those rows to the nearest percent or so.

**2tc** (two corners twisted in place), one row per cap and skeleton length, columns as in the 3c table but running from *Adds 4 or less* to *Adds 12 or less*.

| Cap | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 10 | 5,000 | 8.81 | 0.28% | 0.98% | 3.2% | 9.9% | 33% | 73% | 99% | 100% | 100% | 0 |
| 8 | 14 | 5,000 | 8.29 | 0.52% | 2.1% | 6.3% | 20% | 52% | 89% | 99.8% | 100% | 100% | 0 |
| 8 | 18 | 5,000 | 7.88 | 0.86% | 3.7% | 11% | 31% | 69% | 96% | 100% | 100% | 100% | 0 |
| 8 | 20 | 5,000 | 7.71 | 1.5% | 4.5% | 14% | 37% | 74% | 98% | 100% | 100% | 100% | 0 |
| 8 | 22 | 5,000 | 7.57 | 1.6% | 5.0% | 17% | 41% | 79% | 99% | 100% | 100% | 100% | 0 |
| 8 | 26 | 5,000 | 7.31 | 2.2% | 7.2% | 21% | 50% | 88% | 99.6% | 100% | 100% | 100% | 0 |
| 8 | 30 | 5,000 | 7.07 | 3.0% | 9.4% | 27% | 60% | 93% | 99.9% | 100% | 100% | 100% | 0 |
| 10 | 10 | 200 | 8.38 | 0.50% | 2.0% | 4.5% | 17% | 49% | 89% | 100% | 100% | 100% | 0 |
| 10 | 14 | 200 | 7.95 | 1.0% | 2.5% | 11% | 27% | 67% | 97% | 100% | 100% | 100% | 0 |
| 10 | 18 | 200 | 7.51 | 2.5% | 8.0% | 16% | 45% | 79% | 99% | 100% | 100% | 100% | 0 |
| 10 | 20 | 200 | 7.34 | 2.5% | 6.5% | 21% | 49% | 87% | 100% | 100% | 100% | 100% | 0 |
| 10 | 22 | 200 | 7.26 | 1.5% | 6.0% | 28% | 53% | 86% | 100% | 100% | 100% | 100% | 0 |
| 10 | 26 | 200 | 6.95 | 3.0% | 12% | 31% | 64% | 96% | 100% | 100% | 100% | 100% | 0 |
| 10 | 30 | 200 | 6.74 | 6.5% | 13% | 32% | 71% | 97% | 100% | 100% | 100% | 100% | 0 |

**Twisted 2c2c**, one row per cap and skeleton length, columns as in the 2tc table.

| Cap | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 10 | 20,000 | 9.62 | 0.09% | 0.29% | 1.2% | 4.5% | 15% | 40% | 79% | 98% | 99.9% | 0 |
| 8 | 14 | 20,000 | 9.18 | 0.22% | 0.80% | 2.5% | 7.9% | 24% | 56% | 91% | 99.7% | 100% | 0 |
| 8 | 18 | 20,000 | 8.87 | 0.26% | 1.0% | 3.7% | 11% | 32% | 68% | 96% | 99.9% | 100% | 0 |
| 8 | 20 | 20,000 | 8.73 | 0.38% | 1.3% | 4.2% | 13% | 36% | 74% | 98% | 99.9% | 100% | 0 |
| 8 | 22 | 20,000 | 8.59 | 0.43% | 1.6% | 5.2% | 15% | 41% | 78% | 98% | 99.9% | 100% | 0 |
| 8 | 26 | 20,000 | 8.38 | 0.70% | 2.1% | 6.3% | 19% | 49% | 85% | 99.4% | 100% | 100% | 0 |
| 8 | 30 | 20,000 | 8.19 | 0.74% | 2.6% | 8.3% | 23% | 56% | 90% | 99.8% | 100% | 100% | 0 |
| 10 | 10 | 500 | 9.54 | 0 of 500 | 0 of 500 | 1.4% | 4.8% | 15% | 43% | 83% | 99.2% | 100% | 0 |
| 10 | 14 | 500 | 9.11 | 0.20% | 1.4% | 3.0% | 11% | 25% | 57% | 92% | 99.8% | 100% | 0 |
| 10 | 18 | 500 | 8.74 | 0.60% | 1.2% | 4.2% | 12% | 38% | 71% | 97% | 100% | 100% | 0 |
| 10 | 20 | 500 | 8.66 | 0.80% | 2.4% | 4.8% | 16% | 36% | 76% | 98% | 100% | 100% | 0 |
| 10 | 22 | 500 | 8.39 | 0.60% | 2.0% | 6.8% | 19% | 49% | 85% | 99% | 100% | 100% | 0 |
| 10 | 26 | 500 | 8.29 | 0.60% | 2.8% | 7.6% | 21% | 52% | 87% | 99.6% | 100% | 100% | 0 |
| 10 | 30 | 500 | 8.02 | 1.0% | 2.6% | 8.8% | 27% | 65% | 94% | 100% | 100% | 100% | 0 |

**Pure 2c2c**, one row per cap and skeleton length, columns as in the 2tc table.

| Cap | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 10 | 20,000 | 10.22 | 0.06% | 0.17% | 0.68% | 2.5% | 8.6% | 25% | 56% | 87% | 98% | 0 |
| 8 | 14 | 20,000 | 9.69 | 0.15% | 0.43% | 1.6% | 4.9% | 15% | 39% | 75% | 95% | 99.7% | 0 |
| 8 | 18 | 20,000 | 9.31 | 0.28% | 0.92% | 2.7% | 7.8% | 23% | 52% | 85% | 98% | 99.9% | 0 |
| 8 | 20 | 20,000 | 9.13 | 0.22% | 0.91% | 3.0% | 9.9% | 27% | 58% | 89% | 99% | 99.9% | 0 |
| 8 | 22 | 20,000 | 8.98 | 0.29% | 1.1% | 3.7% | 11% | 30% | 64% | 92% | 99.3% | 99.9% | 0 |
| 8 | 26 | 20,000 | 8.70 | 0.55% | 1.7% | 5.4% | 15% | 38% | 73% | 96% | 99.8% | 100% | 0 |
| 8 | 30 | 20,000 | 8.46 | 0.74% | 2.3% | 6.9% | 19% | 46% | 80% | 98% | 99.9% | 100% | 0 |
| 10 | 10 | 500 | 9.51 | 0 of 500 | 0.20% | 2.0% | 7.8% | 22% | 49% | 74% | 94% | 99.2% | 0 |
| 10 | 14 | 500 | 8.84 | 0.40% | 1.2% | 4.8% | 14% | 36% | 72% | 90% | 98% | 99.6% | 0 |
| 10 | 18 | 500 | 8.60 | 0.40% | 1.6% | 6.2% | 18% | 40% | 79% | 95% | 99.4% | 100% | 0 |
| 10 | 20 | 500 | 8.48 | 0.60% | 2.2% | 6.4% | 18% | 46% | 83% | 96% | 99.4% | 100% | 0 |
| 10 | 22 | 500 | 8.28 | 1.6% | 3.6% | 8.8% | 24% | 53% | 84% | 97% | 99.8% | 100% | 0 |
| 10 | 26 | 500 | 8.05 | 0.80% | 3.0% | 12% | 28% | 61% | 91% | 99% | 100% | 100% | 0 |
| 10 | 30 | 500 | 7.93 | 1.0% | 3.6% | 13% | 33% | 63% | 93% | 99.6% | 100% | 100% | 0 |

**3tc** (three corners twisted the same way), one row per cap and skeleton length, columns as in the 2tc table.

| Cap | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 10 | 20,000 | 10.70 | 0.01% | 0.07% | 0.37% | 1.3% | 4.4% | 14% | 38% | 75% | 97% | 0 |
| 8 | 14 | 20,000 | 10.13 | 0.09% | 0.27% | 0.89% | 2.7% | 9.2% | 26% | 58% | 90% | 99.7% | 0 |
| 8 | 18 | 20,000 | 9.70 | 0.11% | 0.44% | 1.6% | 5.1% | 15% | 38% | 73% | 97% | 99.9% | 0 |
| 8 | 20 | 20,000 | 9.50 | 0.16% | 0.59% | 2.0% | 6.3% | 18% | 45% | 80% | 98% | 99.9% | 0 |
| 8 | 22 | 20,000 | 9.34 | 0.21% | 0.75% | 2.5% | 7.8% | 22% | 50% | 84% | 99% | 100% | 0 |
| 8 | 26 | 20,000 | 9.05 | 0.38% | 1.2% | 3.7% | 10% | 28% | 60% | 91% | 99.5% | 100% | 0 |
| 8 | 30 | 20,000 | 8.82 | 0.34% | 1.3% | 4.6% | 14% | 34% | 69% | 95% | 99.9% | 100% | 0 |
| 10 | 10 | 500 | 10.56 | 0 of 500 | 0 of 500 | 0.60% | 1.8% | 4.6% | 14% | 45% | 80% | 98% | 0 |
| 10 | 14 | 500 | 10.00 | 0.20% | 0.40% | 1.6% | 4.0% | 11% | 27% | 63% | 93% | 100% | 0 |
| 10 | 18 | 500 | 9.61 | 0 of 500 | 0.20% | 1.8% | 6.6% | 17% | 40% | 76% | 98% | 100% | 0 |
| 10 | 20 | 500 | 9.34 | 0.40% | 1.0% | 2.2% | 7.4% | 22% | 50% | 84% | 99% | 100% | 0 |
| 10 | 22 | 500 | 9.26 | 0.20% | 0.40% | 1.8% | 8.8% | 24% | 53% | 86% | 99.4% | 100% | 0 |
| 10 | 26 | 500 | 8.89 | 0.60% | 2.0% | 4.6% | 13% | 32% | 67% | 92% | 100% | 100% | 0 |
| 10 | 30 | 500 | 8.63 | 1.0% | 2.2% | 7.0% | 16% | 39% | 74% | 96% | 100% | 100% | 0 |

**3c1t**, one row per cap and skeleton length, columns as in the 2tc table.

| Cap | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 10 | 20,000 | 10.84 | 0.01% | 0.07% | 0.26% | 1.2% | 3.5% | 12% | 33% | 70% | 96% | 0 |
| 8 | 14 | 20,000 | 10.39 | 0.03% | 0.14% | 0.50% | 1.9% | 6.8% | 20% | 48% | 84% | 99% | 0 |
| 8 | 18 | 20,000 | 10.06 | 0.11% | 0.29% | 0.98% | 3.1% | 10% | 28% | 60% | 92% | 99.8% | 0 |
| 8 | 20 | 20,000 | 9.90 | 0.13% | 0.47% | 1.4% | 4.1% | 12% | 32% | 66% | 94% | 99.9% | 0 |
| 8 | 22 | 20,000 | 9.77 | 0.18% | 0.52% | 1.6% | 4.6% | 14% | 36% | 71% | 96% | 99.9% | 0 |
| 8 | 26 | 20,000 | 9.53 | 0.20% | 0.68% | 2.0% | 6.2% | 18% | 43% | 79% | 98% | 99.9% | 0 |
| 8 | 30 | 20,000 | 9.31 | 0.30% | 0.89% | 2.7% | 8.1% | 22% | 51% | 85% | 99% | 99.9% | 0 |
| 10 | 10 | 500 | 10.68 | 0 of 500 | 0 of 500 | 0.20% | 1.0% | 4.8% | 14% | 40% | 75% | 97% | 0 |
| 10 | 14 | 500 | 10.26 | 0 of 500 | 0 of 500 | 0.20% | 2.8% | 6.8% | 23% | 54% | 88% | 99.2% | 0 |
| 10 | 18 | 500 | 9.88 | 0.20% | 0.20% | 2.4% | 3.8% | 11% | 33% | 67% | 95% | 100% | 0 |
| 10 | 20 | 500 | 9.73 | 0.20% | 1.2% | 2.2% | 5.2% | 15% | 35% | 72% | 96% | 100% | 0 |
| 10 | 22 | 500 | 9.60 | 0.60% | 1.0% | 2.6% | 6.2% | 17% | 40% | 75% | 98% | 100% | 0 |
| 10 | 26 | 500 | 9.38 | 0.20% | 1.0% | 2.4% | 6.4% | 19% | 46% | 87% | 99% | 100% | 0 |
| 10 | 30 | 500 | 9.11 | 0.60% | 1.6% | 3.8% | 11% | 27% | 57% | 89% | 99.4% | 100% | 0 |

**5c**, one row per cap and skeleton length, columns as in the 2tc table.

| Cap | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 10 | 20,000 | 11.25 | <0.01% | 0.03% | 0.20% | 0.68% | 2.3% | 7.9% | 24% | 55% | 87% | 0 |
| 8 | 14 | 20,000 | 10.82 | 0.02% | 0.05% | 0.33% | 1.3% | 4.3% | 13% | 35% | 70% | 94% | 0 |
| 8 | 18 | 20,000 | 10.50 | 0.05% | 0.19% | 0.64% | 2.1% | 6.3% | 18% | 45% | 80% | 98% | 0 |
| 8 | 20 | 20,000 | 10.37 | 0.09% | 0.20% | 0.71% | 2.4% | 7.2% | 20% | 49% | 84% | 99% | 0 |
| 8 | 22 | 20,000 | 10.24 | 0.09% | 0.33% | 1.0% | 2.9% | 8.7% | 23% | 54% | 87% | 99% | 0 |
| 8 | 26 | 20,000 | 10.01 | 0.10% | 0.42% | 1.2% | 3.7% | 11% | 29% | 62% | 91% | 99.6% | 0 |
| 8 | 30 | 20,000 | 9.82 | 0.17% | 0.47% | 1.6% | 4.7% | 13% | 35% | 69% | 95% | 99.8% | 0 |
| 10 | 10 | 2,000 | 10.87 | 0 of 2,000 | 0 of 2,000 | 0.30% | 1.5% | 3.8% | 13% | 35% | 66% | 93% | 0 |
| 10 | 14 | 2,000 | 10.48 | 0.10% | 0.15% | 0.55% | 1.5% | 6.6% | 20% | 47% | 79% | 98% | 0 |
| 10 | 18 | 2,000 | 10.17 | 0.15% | 0.45% | 1.4% | 3.5% | 10% | 26% | 55% | 87% | 99.2% | 0 |
| 10 | 20 | 2,000 | 10.03 | 0.15% | 0.25% | 1.3% | 3.0% | 10% | 28% | 63% | 92% | 99.5% | 0 |
| 10 | 22 | 2,000 | 9.89 | 0.15% | 0.25% | 1.3% | 4.0% | 12% | 33% | 68% | 93% | 99.9% | 0 |
| 10 | 26 | 2,000 | 9.73 | 0.10% | 0.70% | 1.8% | 5.3% | 15% | 36% | 72% | 96% | 99.9% | 0 |
| 10 | 30 | 2,000 | 9.53 | 0.20% | 0.65% | 1.9% | 5.6% | 18% | 44% | 79% | 98% | 100% | 0 |

**Mean added on random skeletons, next to what was estimated. One row per leftover; the last four columns are the computed means, in moves. *not run*: cap 12 with two comms was not run for a 2tc.**

| Leftover | The tutorial's table | Posted on the server | Random, 16 moves, cap 8: mean added | Random, 20 moves, cap 8: mean added | Random, 20 moves, cap 10: mean added | Random, 20 moves, cap 12: mean added |
|---|---:|---|---:|---:|---:|---:|
| 3c | 5/6 | Baiqiang 5-6; Aneurin 6; Eli Rogers ~ +6 | 6.08 | 5.90 | 5.85 | 5.77 |
| 2tc | 8 | Phuwish ~8.0 | 8.06 | 7.71 | 7.34 | not run |
| 3tc | 9 | Phuwish mid to high 8 | 9.89 | 9.50 | 9.34 | 8.56 |
| pure 2c2c | 9/10 | cpaul 9 (pure); tave_789 asked whether a 2c2c is close to 9.5, Phuwish: yeah; Baiqiang 6-8 for a good 2c2c and 8-9 for a bad one, without saying which kind is which | 9.49 | 9.13 | 8.48 | 7.87 |
| twisted 2c2c | not a row of the table | cpaul 9.5 (with a twist); tave_789 and Phuwish as above; Baiqiang as above | 9.01 | 8.73 | 8.66 | 8.30 |
| 3c1t | 10 | cpaul 10; tave_789 asked whether a 3c1t is close to 9.5, Phuwish: yeah; Baiqiang 8-9 | 10.22 | 9.90 | 9.73 | 9.44 |
| 5c | 10/11 | Phuwish ~high 10; Aneurin 10-11 | 10.65 | 10.37 | 10.03 | 9.49 |

**The samples behind those means: how many random skeletons each one rests on, and at 16 moves on how many of them an 8-mover fits.**

| Leftover | 16 moves, cap 8: skeletons | 16 moves, cap 8: something fits on | 20 moves, cap 8: skeletons | 20 moves, cap 10: skeletons | 20 moves, cap 12: skeletons |
|---|---:|---:|---:|---:|---:|
| 3c | 20,000 | 99% | 20,000 | 20,000 | 20,000 |
| 2tc | 5,000 | every one | 5,000 | 200 | not run |
| 3tc | 20,000 | every one | 20,000 | 500 | 100 |
| pure 2c2c | 20,000 | every one | 20,000 | 500 | 100 |
| twisted 2c2c | 20,000 | every one | 20,000 | 500 | 100 |
| 3c1t | 20,000 | every one | 20,000 | 500 | 100 |
| 5c | 20,000 | every one | 20,000 | 2,000 | 100 |

The cap-12 column is on 100 skeletons that are not the skeletons of the cap-8 column, so do not read a step off this table: those 100 5c skeletons average 10.10 with 8-movers, not 10.37. The table of 6.3 has every cap on the same skeletons.

- **The tutorial's table holds up.** Every corner row is within about half a move of the 20-move, 8-mover column; the 3tc is the one a full half move off (9 against 9.50). Where the table gives a range (double swap 9/10, 5c 10/11) the computed mean sits at the low end, and shorter skeletons, which is what a 4c or 5c skeleton usually is, sit higher. Its 9/10 is the row "4 Corners (double swap)"; the twisted double swap has no row.
- **cpaul's 9 and 10 are right, and which 2c2c is the cheaper one depends on the alg length.** Pure 2c2c 9.13, 3c1t 9.90 at 20 moves. With 8-movers alone a twisted 2c2c costs 8.73, less than a pure one. With algs of up to 10 moves it is the other way round, pure 8.48 and twisted 8.66 (500 skeletons each), which is the order cpaul gave ("9 for pure 2-2", "9.5 for 2-2 with a twist", reading "with a twist" as the twisted double swap): a pure 2c2c has 10-move algs and a twisted one has none under 12.
- **Phuwish's numbers are close.**
  - 2tc "~8.0 I guess" ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424237318960709642)) against 7.71.
  - 5c "~high 10" ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239470932131973)) against 10.65 at 16 moves and 10.37 at 20.
  - tave_789's "close to 9.5?" for a 3c1t and a 2c2c ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239312396091486)), which Phuwish answered "yeah" ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239358826778798)), against 9.90 and 8.73 to 9.13.
  - The 3tc, "mid to high 8 from my experience" ([4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239016290553917)), is lower than 8-movers give on random skeletons (9.50), and "a half to a move worse" than a 2tc is 1.79 worse here. With algs up to 12 a 3tc comes to 8.56 on 100 skeletons, so the figure is reachable; it just takes more than pure comms.
- **Baiqiang's are not averages**, in Baiqiang's own words ([28 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443860338440146986): "this is i expected not avg expected"). kyh asked which 2c2c is the good one ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443757686025093241)) and nobody answered, so I don't pin the two figures on pure and twisted here.

  What the numbers give: with every alg of up to 12 moves a pure 2c2c averages 7.87 and a twisted one 8.30 on 100 random skeletons of 20 moves each, figures of the size of "6-8" and "8-9" ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443756810715664537)). Jay guessed as much in the same exchange ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443789835356606609)): "maybe there's some non 3c type insertion method for 2c2c that lowers the movecount that far". The 10-move 2c2c algs are one such method: with algs of up to 10 moves a pure 2c2c is already at 8.48 (500 skeletons). 

  A 3c1t averages 9.44 at cap 12, above the 8-9. On the skeletons people posted a 3c1t averages 8.65 with 8-movers alone (20 skeletons, section 9), which is inside it.
- **The order** at cap 8 is 2tc, twisted 2c2c, pure 2c2c, 3tc, 3c1t, 5c. argonblue's "i think 3c1t > 2c2c > 5c" ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125544114131034)) has the first two the other way round by cost: a 2c2c is 0.77 to 1.17 cheaper than a 3c1t. jisu101's reply ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125667565080657), [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125708480516218): "you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions") is the reason, see below. And the difference Jay "didn't notice" between the "2 insertion 4c types" ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443789835356606609)) is about a move on average: 8.73, 9.13, 9.90. The spread from one skeleton to the next is wider than that, so it is hard to notice solve by solve. Section 10 has a typical skeleton of each of the three (example [a]).
- **"getting +9 from 2tc is as bad as +11,+12 from 5c"** (Phuwish, [4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424238456275730556)) is right in odds: +9 or worse happens on 26% of 2tc skeletons, +11 or worse on 51% of 5c skeletons and +12 or worse on 16%.

**Why the types differ.** Four minutes after Jay's remark on the "2 insertion 4c types", wen asked ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443790851443785758)): "Why is there even a difference if the number of possible first insertions is the same tbh". You can read that as about the two kinds of 2c2c or about a 2c2c against a 3c1t, so here's the count for every type. At one spot of the skeleton the first comm can be any 3-cycle that leaves a 3c behind. How many of those there are, and how many 8-move comms that gives per spot on average:

**The first comm of a two-comm leftover: 3-cycles that leave a 3c, per spot, and how many 8-move comms that is on average over the spots of 5,000 random 20-move skeletons per type (20,000 for a 5c).**

| Leftover | Ways to choose the first comm at one spot | 8-move first comms at one spot, on average |
|---|---:|---:|
| 2tc | 108 | 92.6 |
| 3tc | 18 | 15.4 |
| pure 2c2c | 24 | 20.6 |
| twisted 2c2c | 24 | 20.6 |
| 3c1t | 9 | 7.7 |
| 5c | 5 | 4.3 |
| 3c3c | 2 | 1.7 |

- **For the two kinds of 2c2c the number is the same**, 24 each: any three of the four corners, either direction (jisu101's point, [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125667565080657), [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125708480516218)), with three ways to twist. They still cost 8.73 and 9.13 with 8-movers, and the 0.40 between them comes from comms that interact. When the two comms do not touch, a pure and a twisted 2c2c cost the same, 9.41 and 9.40 (6.5). With nesting forbidden the twisted one is 0.16 cheaper (9.03 against 9.19): its second comm cancels into the first more often without sitting inside it. Nesting is the other 0.25: the best pair is nested on 24% of twisted 2c2c skeletons and 5.1% of pure ones.
- **Across types it isn't the same.** More choices for the first comm means better odds of a good one, and the costs come in that order:

  | | 2tc | 2c2c | 3tc | 3c1t | 5c | 3c3c |
  |---|---:|---:|---:|---:|---:|---:|
  | First comms per spot | 108 | 24 | 18 | 9 | 5 | 2 |
  | Mean added | 7.71 | 8.73 and 9.13 | 9.50 | 9.90 | 10.37 | 11.05 |


### 6.3 What a longer alg list is worth

At 20 moves, the mean added under each cap. Caps 10 and 12 are every alg of that length, **computer only**: read them as what learning more algs could buy at most, not as a search to run in an attempt. First with each cap on its own sample:

**Mean added, random skeletons of 20 moves, by cap. Each *Skeletons* column is the number of skeletons behind the number to its left. At cap 8 the mean is over the skeletons where something fits, and the first column says on how many that is; at caps 10 and 12 something fits on every skeleton. *not run*: cap 12 with two comms was not run for that leftover.**

| Leftover | Cap 8: something fits on | Cap 8: mean added where something fits | Skeletons (cap 8) | Cap 10: mean added | Skeletons (cap 10) | Cap 10, a comm plus an alg: mean added | Skeletons (comm plus alg) | Cap 12: mean added | Skeletons (cap 12) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3c | 99.6% | 5.90 | 20,000 | 5.85 | 20,000 | 5.99 | 200 | 5.77 | 20,000 |
| 2tc | every one | 7.71 | 5,000 | 7.34 | 200 | 7.34 | 200 | not run | not run |
| 3tc | every one | 9.50 | 20,000 | 9.34 | 500 | 9.26 | 200 | 8.56 | 100 |
| pure 2c2c | every one | 9.13 | 20,000 | 8.48 | 500 | 8.25 | 200 | 7.87 | 100 |
| twisted 2c2c | every one | 8.73 | 20,000 | 8.66 | 500 | 8.60 | 200 | 8.30 | 100 |
| 3c1t | every one | 9.90 | 20,000 | 9.73 | 500 | 9.56 | 200 | 9.44 | 100 |
| 5c | every one | 10.37 | 20,000 | 10.03 | 2,000 | 9.66 | 200 | 9.49 | 100 |
| 3c3c | 99.9% | 11.05 | 20,000 | 10.48 | 2,000 | 10.09 | 200 | 9.88 | 100 |
| 3e | 56% | 5.95 | 20,000 | 6.05 | 20,000 | 5.68 | 200 | 5.95 | 20,000 |
| 2fe | 96% | 8.96 | 5,000 | 7.51 | 200 | 7.51 | 200 | not run | not run |
| 2e2e | 97% | 9.29 | 5,000 | 7.63 | 200 | 6.89 | 200 | not run | not run |
| flipped 2e2e | 91% | 11.08 | 5,000 | 7.83 | 200 | 7.54 | 200 | not run | not run |
| 3e1f | 60% | 11.82 | 20,000 | 9.85 | 500 | 8.87 | 200 | 9.34 | 100 |
| 5e | 81% | 10.94 | 20,000 | 9.06 | 500 | 8.43 | 200 | 8.83 | 100 |
| 3e3e | 56% | 11.62 | 20,000 | 10.32 | 2,000 | 9.44 | 200 | 9.82 | 100 |

The samples differ in size and are not the same skeletons: the 100 5c skeletons of the cap-12 column average 10.10 with 8-movers, not 10.37, so 10.37 to 9.49 overstates the step. For the step from one cap to the next the fair comparison is on the same skeletons:

**The same skeletons under every cap (the first 100 or 200 of the 20-move sample).**

| Leftover | Skeletons | Cap 8: mean added where something fits | Nothing fits at cap 8 | Cap 10: mean added | Cap 10, a comm plus an alg: mean added | Cap 12: mean added |
|---|---:|---:|---:|---:|---:|---:|
| 3c | 200 | 6.12 | 1 | 6.07 | 5.99 | 5.98 |
| 3tc | 100 | 9.41 | 0 | 9.32 | 9.32 | 8.56 |
| pure 2c2c | 100 | 9.26 | 0 | 8.40 | 8.09 | 7.87 |
| twisted 2c2c | 100 | 8.74 | 0 | 8.65 | 8.64 | 8.30 |
| 3c1t | 100 | 9.82 | 0 | 9.67 | 9.53 | 9.44 |
| 5c | 100 | 10.10 | 0 | 9.79 | 9.63 | 9.49 |
| 3c3c | 100 | 10.87 | 0 | 10.23 | 10.01 | 9.88 |
| 3e | 200 | 5.89 | 92 | 6.04 | 5.68 | 5.98 |
| 3e1f | 100 | 11.76 | 34 | 10.03 | 8.92 | 9.34 |
| 5e | 100 | 11.20 | 16 | 9.13 | 8.54 | 8.83 |
| 3e3e | 100 | 11.79 | 38 | 10.25 | 9.52 | 9.82 |

- **3c**: 8 to 10 is worth 0.05, 10 to 12 another 0.09 on these 200; on the full 20,000 it is 0.05 and 0.07. Not much.
- **5c**: 10.37 with 8-movers, 10.03 at cap 10 (2,000 skeletons). On the same 100 skeletons: 10.10, 9.79, 9.49.
- **Pure 2c2c gains the most**: 9.26, 8.40, 7.87 on the same 100. The 10-move 2c2c algs are worth learning if you take 2c2c skeletons.
- **Twisted 2c2c, 3c1t, 3tc** gain little at 10, where nothing is new for them but longer comms, and more at 12: a 3tc goes from 9.32 to 8.56 on these 100 skeletons, all of it from longer comms, since it has no alg of 12 moves or fewer.
- **A comm plus an alg** (the column *Cap 10, a comm plus an alg*) is worth another 0.16 on a 5c and 0.31 on a pure 2c2c at cap 10. That is a 5c done as a 3c comm and a 2c2c alg, the kind of line Insertion Finder returns with all its sets on.

These are averages over 100 or 200 skeletons, compared on the same skeletons, so the direction of each step is solid. For its size: two standard errors of a mean are ±0.26 for a 5c at cap 12 on 100 skeletons (Appendix C).

### 6.4 One alg for the whole leftover

**One alg for the whole leftover, random skeletons of 20 moves (*Skeletons*: the sample). How often an alg within the cap fits at some spot, what it adds on the skeletons where it fits, and what two 8-move comms add on those same skeletons (for the edge rows: two 3e algs of 8 moves or fewer, which do not always fit). One row per leftover; this table is algs of up to 10 moves, the next one up to 12.**

| Leftover | Skeletons | Alg of 10 or less: fits somewhere | Alg of 10 or less: mean added | Two 8-move comms on the skeletons where an alg of 10 or less fits: mean added | Of those skeletons, two 8-move comms fit on |
|---|---:|---:|---:|---:|---|
| 2tc | 5,000 | 0 |  |  |  |
| 3tc | 20,000 | 0 |  |  |  |
| pure 2c2c | 20,000 | 62% | 8.44 | 9.07 | all of them |
| twisted 2c2c | 20,000 | 0 |  |  |  |
| 3c1t | 20,000 | 0 |  |  |  |
| 5c | 20,000 | 14% | 9.41 | 10.28 | all of them |
| 3c3c | 20,000 | 9.9% | 9.16 | 11.25 | 1,975 |
| 2fe | 5,000 | 0 |  |  |  |
| 2e2e | 5,000 | 92% | 7.76 | 9.14 | 4,557 |
| flipped 2e2e | 5,000 | 97% | 8.35 | 11.07 | 4,394 |
| 3e1f | 20,000 | 0 |  |  |  |
| 5e | 20,000 | 71% | 8.90 | 11.46 | 10,751 |
| 3e3e | 20,000 | 38% | 9.16 | 11.28 | 4,959 |

**The same with algs of up to 12 moves.**

| Leftover | Skeletons | Alg of 12 or less: fits somewhere | Alg of 12 or less: mean added | Two 8-move comms on the skeletons where an alg of 12 or less fits: mean added | Of those skeletons, two 8-move comms fit on |
|---|---:|---:|---:|---:|---|
| 2tc | 5,000 | 100% | 9.03 | 7.71 | all of them |
| 3tc | 20,000 | 0 |  |  |  |
| pure 2c2c | 20,000 | 99.9% | 8.75 | 9.13 | all of them |
| twisted 2c2c | 20,000 | 99.9% | 9.45 | 8.73 | all of them |
| 3c1t | 20,000 | 54% | 11.33 | 9.80 | all of them |
| 5c | 20,000 | 97% | 10.50 | 10.35 | all of them |
| 3c3c | 20,000 | 95% | 10.53 | 11.03 | 19,030 |
| 2fe | 5,000 | 0 |  |  |  |
| 2e2e | 5,000 | 100% | 7.44 | 9.34 | 4,849 |
| flipped 2e2e | 5,000 | 100% | 8.04 | 11.08 | 4,536 |
| 3e1f | 20,000 | 99% | 10.43 | 11.81 | 11,956 |
| 5e | 20,000 | 99.9% | 9.08 | 11.55 | 15,508 |
| 3e3e | 20,000 | 99.6% | 10.02 | 11.86 | 10,907 |

- **Pure 2c2c**: a 10-move alg fits somewhere on 62% of skeletons and then costs 8.44. Two 8-move comms cost 9.07 on those same skeletons (9.13 over all of them), so where it fits the alg is 0.62 better.
- **2tc**: the 12-move two-twist is there on every skeleton, and costs 9.03. Two comms cost 7.71. The tutorial already says of the 2tc and 3tc algs: "But this is usually not the best way". For the 2tc it is worse by 1.32.
- **5c, 3c1t**: one alg of up to 12 moves alone is no better than two 8-move comms on the skeletons where it fits (10.50 against 10.35 for a 5c, 11.33 against 9.80 for a 3c1t), but on some skeletons it is the best, which is where the gain of 6.3 comes from.

### 6.5 Nesting

The second comm may go inside the first. How much that is worth, with 8-movers on 20-move skeletons (best pairs, a computer search; the hand version is to look for the second comm inside the first as well as outside it):

**Two 8-move comms, random skeletons of 20 moves: mean added with nesting allowed, with the second comm kept outside the moves the first one changed, and with the two comms not touching at all. The means are over the skeletons where all three ways have a solution (third column) out of the sample (second column). For the edge rows the comms are 3e algs of 8 moves or fewer.**

| Leftover | Skeletons in the sample | Of them, all three ways have a solution | Nesting allowed: mean added | No nesting: mean added | The two not touching: mean added | Best needs nesting |
|---|---:|---:|---:|---:|---:|---:|
| 2tc | 5,000 | 5,000 | 7.71 | 7.74 | 8.05 | 2.3% |
| 3tc | 20,000 | 20,000 | 9.50 | 9.51 | 9.66 | 0.88% |
| pure 2c2c | 20,000 | 20,000 | 9.13 | 9.19 | 9.41 | 5.1% |
| twisted 2c2c | 20,000 | 20,000 | 8.73 | 9.03 | 9.40 | 24% |
| 3c1t | 20,000 | 20,000 | 9.90 | 10.04 | 10.28 | 13% |
| 5c | 20,000 | 20,000 | 10.37 | 10.67 | 10.95 | 24% |
| 3c3c | 20,000 | 19,824 | 11.04 | 11.59 | 11.92 | 38% |
| 2fe | 5,000 | 4,796 | 8.96 | 8.96 | 9.04 | 0 |
| 2e2e | 5,000 | 4,289 | 8.93 | 9.51 | 10.71 | 28% |
| flipped 2e2e | 5,000 | 4,520 | 11.07 | 11.07 | 11.12 | 0.11% |
| 3e1f | 20,000 | 11,939 | 11.80 | 11.80 | 11.85 | 0.09% |
| 5e | 20,000 | 10,936 | 10.90 | 11.43 | 11.74 | 31% |
| 3e3e | 20,000 | 6,183 | 11.14 | 11.63 | 12.04 | 31% |

- **On a 5c, nesting is worth 0.30**, and the best solution needs it on 24% of skeletons. Gezza Cubing ([20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253277699506704424)): "for things like 5c, you can insert a commutator in the middle of the first commutator". argonblue ([27 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1465819786910109828)), on having just seen one: "i thought it wasn't possible to nest 3c comms that are parts of a 5-cycle, but insertion finder apparently did it for one of my skeletons (improving it by 1 move)?" What argonblue saw is no rarity: it is the best there is on that 24% (one is written out as example [e] in section 10).
- **Twisted 2c2c**: 0.30, needed on 24%. **3c1t**: 0.15. **Pure 2c2c, 2tc, 3tc**: under a tenth of a move.
- **Two comms that do not touch** cost 0.58 more than the best on a 5c. That is the price of treating a 5c as two separate 3c searches.

### 6.6 Edges

**3e: one comm. Random skeletons, 20,000 per row. Cap 8 is the 6-, 7- and 8-move algs.**

| Cap | Skeleton length | Skeletons | Mean moves added | Adds 2 or less | Adds 3 or less | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 10 | 20,000 | 6.15 | 0.57% | 1.8% | 4.9% | 10% | 19% | 33% | 38% | 62% |
| 8 | 14 | 20,000 | 6.05 | 0.83% | 2.7% | 6.3% | 13% | 25% | 40% | 45% | 55% |
| 8 | 18 | 20,000 | 5.96 | 1.3% | 3.4% | 7.8% | 16% | 30% | 47% | 52% | 48% |
| 8 | 20 | 20,000 | 5.95 | 1.2% | 3.6% | 8.6% | 18% | 32% | 51% | 56% | 44% |
| 8 | 22 | 20,000 | 5.89 | 1.5% | 4.2% | 9.6% | 19% | 35% | 54% | 59% | 41% |
| 8 | 26 | 20,000 | 5.83 | 1.8% | 4.8% | 11% | 22% | 39% | 58% | 63% | 37% |
| 8 | 30 | 20,000 | 5.77 | 1.8% | 5.3% | 13% | 25% | 43% | 63% | 68% | 32% |
| 10 | 10 | 20,000 | 6.77 | 0.82% | 2.4% | 6.8% | 16% | 36% | 67% | 94% | <0.01% |
| 10 | 14 | 20,000 | 6.43 | 1.1% | 3.5% | 9.0% | 21% | 46% | 79% | 98% | 0 |
| 10 | 18 | 20,000 | 6.16 | 1.6% | 4.3% | 11% | 26% | 55% | 86% | 99.4% | 0 |
| 10 | 20 | 20,000 | 6.05 | 1.7% | 4.9% | 12% | 29% | 58% | 89% | 99.7% | 0 |
| 10 | 22 | 20,000 | 5.93 | 2.1% | 5.5% | 14% | 31% | 63% | 91% | 99.8% | 0 |
| 10 | 26 | 20,000 | 5.78 | 2.4% | 6.4% | 16% | 35% | 68% | 94% | 99.9% | 0 |
| 10 | 30 | 20,000 | 5.63 | 2.5% | 7.0% | 18% | 39% | 73% | 96% | 99.9% | 0 |
| 12 | 10 | 20,000 | 6.67 | 0.90% | 2.6% | 7.2% | 17% | 38% | 71% | 96% | 0 |
| 12 | 14 | 20,000 | 6.33 | 1.2% | 3.8% | 9.6% | 22% | 49% | 82% | 99% | 0 |
| 12 | 18 | 20,000 | 6.06 | 1.8% | 4.7% | 12% | 28% | 58% | 89% | 99.6% | 0 |
| 12 | 20 | 20,000 | 5.95 | 1.8% | 5.3% | 13% | 31% | 62% | 91% | 99.8% | 0 |
| 12 | 22 | 20,000 | 5.84 | 2.2% | 5.9% | 15% | 33% | 66% | 93% | 99.9% | 0 |
| 12 | 26 | 20,000 | 5.68 | 2.6% | 6.8% | 17% | 37% | 71% | 96% | 99.9% | 0 |
| 12 | 30 | 20,000 | 5.53 | 2.8% | 7.7% | 19% | 42% | 77% | 97% | 99.9% | 0 |

For the next two, cap 8 is the best of two 3e algs of 8 moves or fewer and one alg of 8 or fewer for the whole leftover (both have 6-movers), and cap 10 is the same with algs of up to 10 moves. Random skeletons; the *Skeletons* column is the sample behind each row.

**2e2e** (two swaps, no flip), one row per cap and skeleton length, columns as in the 2tc table.

| Cap | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 10 | 5,000 | 10.51 | 1.8% | 3.8% | 7.8% | 17% | 24% | 30% | 38% | 47% | 58% | 15% |
| 8 | 14 | 5,000 | 10.02 | 2.4% | 5.7% | 11% | 22% | 29% | 38% | 48% | 58% | 70% | 8.3% |
| 8 | 18 | 5,000 | 9.60 | 3.8% | 7.8% | 14% | 27% | 36% | 46% | 56% | 66% | 78% | 4.0% |
| 8 | 20 | 5,000 | 9.29 | 4.3% | 9.6% | 17% | 30% | 40% | 50% | 61% | 72% | 82% | 3.0% |
| 8 | 22 | 5,000 | 9.08 | 5.0% | 11% | 19% | 33% | 43% | 53% | 64% | 75% | 85% | 2.2% |
| 8 | 26 | 5,000 | 8.64 | 6.1% | 12% | 22% | 38% | 50% | 60% | 71% | 81% | 90% | 1.3% |
| 8 | 30 | 5,000 | 8.36 | 6.5% | 14% | 25% | 41% | 54% | 65% | 77% | 85% | 93% | 0.64% |
| 10 | 10 | 200 | 8.42 | 4.0% | 7.0% | 11% | 27% | 45% | 71% | 93% | 99.5% | 100% | 0 |
| 10 | 14 | 200 | 8.00 | 2.5% | 6.5% | 16% | 32% | 61% | 85% | 97% | 100% | 100% | 0 |
| 10 | 18 | 200 | 7.64 | 5.0% | 10% | 20% | 39% | 69% | 93% | 100% | 100% | 100% | 0 |
| 10 | 20 | 200 | 7.63 | 5.5% | 12% | 22% | 37% | 66% | 92% | 99.5% | 100% | 100% | 0 |
| 10 | 22 | 200 | 7.60 | 3.5% | 11% | 23% | 42% | 66% | 95% | 100% | 100% | 100% | 0 |
| 10 | 26 | 200 | 7.08 | 9.0% | 19% | 30% | 55% | 78% | 96% | 100% | 100% | 100% | 0 |
| 10 | 30 | 200 | 7.08 | 9.5% | 15% | 32% | 57% | 79% | 98% | 100% | 100% | 100% | 0 |

**5e**, one row per cap and skeleton length, columns as in the 2tc table.

| Cap | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 10 | 20,000 | 11.72 | 0.06% | 0.29% | 1.1% | 3.2% | 8.1% | 11% | 16% | 24% | 34% | 41% |
| 8 | 14 | 20,000 | 11.40 | 0.17% | 0.62% | 1.8% | 5.1% | 12% | 16% | 23% | 33% | 45% | 30% |
| 8 | 18 | 20,000 | 11.11 | 0.19% | 0.75% | 2.4% | 6.4% | 15% | 20% | 28% | 40% | 53% | 22% |
| 8 | 20 | 20,000 | 10.94 | 0.26% | 0.97% | 2.9% | 7.4% | 17% | 23% | 32% | 45% | 58% | 19% |
| 8 | 22 | 20,000 | 10.86 | 0.34% | 1.1% | 3.2% | 8.3% | 18% | 24% | 34% | 48% | 61% | 15% |
| 8 | 26 | 20,000 | 10.58 | 0.42% | 1.4% | 4.1% | 10% | 22% | 29% | 40% | 55% | 68% | 11% |
| 8 | 30 | 20,000 | 10.28 | 0.53% | 1.8% | 5.0% | 12% | 26% | 34% | 47% | 62% | 75% | 7.8% |
| 10 | 10 | 500 | 9.98 | 0 of 500 | 0.20% | 1.2% | 4.0% | 13% | 38% | 65% | 84% | 97% | 0 |
| 10 | 14 | 500 | 9.34 | 0.20% | 0.80% | 3.6% | 11% | 27% | 54% | 79% | 92% | 99% | 0 |
| 10 | 18 | 500 | 9.18 | 0.40% | 1.6% | 3.8% | 9.8% | 28% | 57% | 84% | 97% | 100% | 0 |
| 10 | 20 | 500 | 9.06 | 0.40% | 1.6% | 3.6% | 11% | 30% | 62% | 88% | 97% | 99.8% | 0 |
| 10 | 22 | 500 | 8.91 | 0.20% | 0.60% | 3.6% | 14% | 36% | 68% | 90% | 98% | 100% | 0 |
| 10 | 26 | 500 | 8.70 | 1.0% | 2.0% | 5.8% | 18% | 39% | 71% | 94% | 99% | 100% | 0 |
| 10 | 30 | 500 | 8.51 | 0.60% | 1.8% | 8.4% | 22% | 46% | 75% | 94% | 99.8% | 100% | 0 |

- **With algs of 8 or fewer, nothing fits on 44% of random 20-move skeletons.** When something fits it is good (5.95). That is FakeMMAP's "huge variance" ([3 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1390246333834596463)).
- **With every alg up to 10, a 3e costs 6.05**, about what a 3c costs. The tutorial's 7 is a move above that, and its footnote says why the number moves: "Warning: this varies a lot! If edges are oriented early in the solve, you have better chances of finding a good insertion (6 or 8 movers)."
- **Whether a short alg fits depends on how the three edges sit.** A 6-mover needs them oriented on all three axes and an alg of 8 or fewer on at least two (section 5); on these random skeletons the leftover is oriented on two or three axes 18% of the time. So read the cap-8 rows as what the short algs give when nothing in the solve has arranged that, and the cap-10 and cap-12 rows as what a full alg list gives on any skeleton. The 17 real 3e skeletons of section 9 are far cheaper than any row here, and how their edges are oriented does not explain it (9.2).
- **2e2e and 5e** at cap 10: 7.63 and 9.06 (200 and 500 skeletons). A 2e2e is the cheap one, and a 5e costs 0.97 less than a 5c at the same cap (500 5e skeletons against 2,000 5c skeletons). The other edge types are in Appendix A.

---

## 7. Which skeleton to take

### 7.1 The chance of a result

The chance of a final solution of $N$ or less from a skeleton of a given type and length, 8-movers, random skeletons. Every cell is its own sample of 20,000 skeletons (5,000 for a 2tc), at the odd lengths too. A cell under 0.05% is fewer than ten skeletons of the 20,000 (for a 2tc, one or two of the 5,000), so the smallest cells are rough. Two-comm types are at their best pair of comms; a hand search that takes only the best first comm comes out a little longer (8.4), so treat their cells as a ceiling.

**28 or less.** Chance of a final 28 or less, one row per skeleton length, one column per leftover:

| Skeleton length | 3c | 2tc | 3tc | pure 2c2c | twisted 2c2c | 3c1t | 5c |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 15 | 99% | 100% | 100% | 100% | 100% | 100% | 99.8% |
| 16 | 99% | 100% | 99.9% | 99.8% | 100% | 99.5% | 96% |
| 17 | 99.1% | 100% | 95% | 98% | 99.9% | 90% | 77% |
| 18 | 99.4% | 100% | 73% | 85% | 96% | 60% | 45% |
| 19 | 99.5% | 97% | 41% | 56% | 72% | 29% | 20% |
| 20 | 99.6% | 74% | 18% | 27% | 36% | 12% | 7.2% |
| 21 | 96% | 39% | 7.0% | 10% | 14% | 4.0% | 2.8% |
| 22 | 75% | 17% | 2.5% | 3.7% | 5.2% | 1.6% | 1.0% |
| 23 | 33% | 5.5% | 0.74% | 1.3% | 1.6% | 0.51% | 0.41% |
| 24 | 11% | 1.9% | 0.27% | 0.46% | 0.52% | 0.13% | 0.07% |
| 25 | 3.2% | 0.58% | 0.10% | 0.13% | 0.14% | 0.06% | 0.03% |
| 26 | 0.96% | 0.20% | 0.04% | 0.02% | 0.07% | 0.02% | 0 |

**26 or less.** Chance of a final 26 or less, same layout:

| Skeleton length | 3c | 2tc | 3tc | pure 2c2c | twisted 2c2c | 3c1t | 5c |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 98% | 100% | 100% | 100% | 100% | 99.9% | 99.4% |
| 14 | 98% | 100% | 99.7% | 99.7% | 100% | 99% | 94% |
| 15 | 99% | 100% | 92% | 96% | 99.8% | 86% | 73% |
| 16 | 99% | 99.9% | 67% | 80% | 94% | 54% | 40% |
| 17 | 99.1% | 95% | 35% | 49% | 66% | 26% | 17% |
| 18 | 99.4% | 69% | 15% | 23% | 32% | 10% | 6.3% |
| 19 | 95% | 33% | 5.4% | 9.1% | 12% | 3.7% | 2.1% |
| 20 | 71% | 14% | 2.0% | 3.0% | 4.2% | 1.4% | 0.71% |
| 21 | 31% | 4.4% | 0.65% | 0.97% | 1.4% | 0.34% | 0.30% |
| 22 | 10% | 1.6% | 0.21% | 0.29% | 0.43% | 0.18% | 0.09% |
| 23 | 3.0% | 0.70% | 0.08% | 0.07% | 0.19% | 0.06% | 0.04% |
| 24 | 0.89% | 0.10% | 0.04% | 0.04% | 0.04% | 0.01% | <0.01% |
| 25 | 0.24% | 0.06% | 0.02% | <0.01% | <0.01% | <0.01% | 0 |

**30 or less.** Chance of a final 30 or less, same layout:

| Skeleton length | 3c | 2tc | 3tc | pure 2c2c | twisted 2c2c | 3c1t | 5c |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 99.1% | 100% | 100% | 99.9% | 100% | 100% | 99.8% |
| 18 | 99.4% | 100% | 99.9% | 99.9% | 100% | 99.8% | 98% |
| 19 | 99.5% | 100% | 97% | 99% | 99.9% | 93% | 82% |
| 20 | 99.6% | 100% | 80% | 89% | 98% | 66% | 49% |
| 21 | 99.6% | 98% | 47% | 61% | 76% | 34% | 22% |
| 22 | 99.8% | 79% | 22% | 30% | 41% | 14% | 8.7% |
| 23 | 97% | 43% | 8.3% | 12% | 16% | 4.9% | 2.9% |
| 24 | 77% | 18% | 3.2% | 4.7% | 5.8% | 1.8% | 1.0% |
| 25 | 36% | 6.7% | 0.96% | 1.7% | 1.8% | 0.60% | 0.36% |
| 26 | 12% | 2.2% | 0.38% | 0.55% | 0.70% | 0.20% | 0.10% |

**24 or less.** Chance of a final 24 or less, same layout:

| Skeleton length | 3c | 2tc | 3tc | pure 2c2c | twisted 2c2c | 3c1t | 5c |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 12 | 97% | 100% | 99% | 99.2% | 99.9% | 98% | 92% |
| 13 | 98% | 100% | 88% | 94% | 99.6% | 82% | 67% |
| 14 | 98% | 99.8% | 58% | 75% | 91% | 48% | 35% |
| 15 | 99% | 92% | 29% | 43% | 60% | 21% | 14% |
| 16 | 99% | 61% | 12% | 19% | 28% | 8.3% | 5.4% |
| 17 | 94% | 28% | 4.7% | 7.2% | 11% | 2.9% | 1.8% |
| 18 | 67% | 11% | 1.6% | 2.7% | 3.7% | 0.98% | 0.64% |
| 19 | 29% | 3.5% | 0.52% | 0.90% | 1.0% | 0.36% | 0.20% |
| 20 | 9.3% | 1.5% | 0.16% | 0.22% | 0.38% | 0.13% | 0.09% |
| 21 | 2.6% | 0.38% | 0.05% | 0.07% | 0.13% | 0.03% | 0.03% |
| 22 | 0.69% | 0.20% | 0.02% | 0.03% | 0.04% | 0.03% | 0.01% |
| 23 | 0.24% | 0.06% | 0.01% | 0 | 0.02% | <0.01% | 0.01% |

### 7.2 Exchange rates

Fanti's question ([5 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1247972528425799841)): "how many moves shorter should a 5c (normal cycle) skeleton be compared to a 3c (normal cycle) skeleton so that i should look at the 5c first". By expected final length, 8-movers:

**How much shorter the other skeleton has to be to give the same expected total as a 3c of the length in the first column. Random skeletons, cap 8. An expected total is the length plus the mean added over the skeletons where something fits (that leaves out the 0.36% of 20-move 3c skeletons with no 8-mover).**

| 3c skeleton of | Its expected total where an 8-mover fits | 2tc shorter by | 3tc shorter by | pure 2c2c shorter by | twisted 2c2c shorter by | 3c1t shorter by | 5c shorter by |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 16 | 22.1 | 2.2 | 4.4 | 3.8 | 3.2 | 4.6 | 5.1 |
| 18 | 24.0 | 2.1 | 4.2 | 3.7 | 3.1 | 4.5 | 4.9 |
| 20 | 25.9 | 2.0 | 4.0 | 3.5 | 3.0 | 4.4 | 4.8 |
| 22 | 27.8 | 1.9 | 3.9 | 3.4 | 3.0 | 4.3 | 4.7 |
| 24 | 29.7 | 1.8 | 3.7 | 3.3 | 2.9 | 4.2 | 4.7 |
| 26 | 31.7 | 1.8 | 3.6 | 3.2 | 2.9 | 4.1 | 4.6 |
| 28 | 33.6 | 1.7 | 3.5 | 3.2 | 2.8 | 4.0 | 4.5 |

And by the chance of reaching a target, which is what matters when you need a specific result:

**How much shorter the other skeleton has to be to give the same chance of the target as the 3c in the second column. Random skeletons, cap 8. Each whole length is its own sample; the length of equal chance is read off between two whole lengths.**

| Target | 3c skeleton of | Chance of the target | 2tc shorter by | 3tc shorter by | pure 2c2c shorter by | twisted 2c2c shorter by | 3c1t shorter by | 5c shorter by |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 22 or less | 15 | 91% | 2.1 | 4.4 | 4.1 | 3.2 | 4.6 |  |
| 22 or less | 16 | 63% | 2.2 | 4.4 | 3.9 | 3.3 | 4.6 | 5.1 |
| 22 or less | 17 | 26% | 2.1 | 4.1 | 3.6 | 3.1 | 4.4 | 4.8 |
| 22 or less | 18 | 8.5% | 1.9 | 3.9 | 3.4 | 3.0 | 4.2 | 4.7 |
| 22 or less | 19 | 2.2% | 1.7 | 3.6 | 3.1 | 2.7 | 4.0 | 4.4 |
| 24 or less | 17 | 94% | 2.0 | 4.3 | 4.0 | 3.1 | 4.5 | 5.1 |
| 24 or less | 18 | 67% | 2.1 | 4.2 | 3.7 | 3.2 | 4.5 | 5.0 |
| 24 or less | 19 | 29% | 2.0 | 4.0 | 3.5 | 3.0 | 4.4 | 4.8 |
| 24 or less | 20 | 9.3% | 1.8 | 3.7 | 3.3 | 2.9 | 4.1 | 4.6 |
| 24 or less | 21 | 2.6% | 1.7 | 3.5 | 3.0 | 2.7 | 3.9 | 4.3 |
| 26 or less | 19 | 95% | 2.0 | 4.2 | 3.8 | 3.1 | 4.4 | 5.1 |
| 26 or less | 20 | 71% | 2.0 | 4.1 | 3.7 | 3.1 | 4.4 | 4.9 |
| 26 or less | 21 | 31% | 1.9 | 3.8 | 3.4 | 3.0 | 4.2 | 4.7 |
| 26 or less | 22 | 10% | 1.7 | 3.6 | 3.1 | 2.9 | 4.0 | 4.5 |
| 26 or less | 23 | 3.0% | 1.6 | 3.4 | 3.0 | 2.7 | 3.8 | 4.3 |
| 28 or less | 21 | 96% | 1.9 | 4.1 | 3.7 | 3.0 | 4.3 | 5.0 |
| 28 or less | 22 | 75% | 2.0 | 4.0 | 3.6 | 3.1 | 4.4 | 4.9 |
| 28 or less | 23 | 33% | 1.8 | 3.7 | 3.3 | 2.9 | 4.2 | 4.6 |
| 28 or less | 24 | 11% | 1.6 | 3.5 | 3.1 | 2.8 | 3.9 | 4.4 |
| 28 or less | 25 | 3.2% | 1.5 | 3.2 | 2.9 | 2.6 | 3.8 | 4.1 |
| 30 or less | 23 | 97% | 1.8 | 4.0 | 3.6 | 3.0 | 4.3 | 4.9 |
| 30 or less | 24 | 77% | 1.9 | 3.9 | 3.5 | 3.0 | 4.3 | 4.8 |
| 30 or less | 25 | 36% | 1.8 | 3.6 | 3.2 | 2.8 | 4.1 | 4.5 |
| 30 or less | 26 | 12% | 1.6 | 3.4 | 3.0 | 2.7 | 3.9 | 4.4 |
| 30 or less | 27 | 3.6% | 1.4 | 3.1 | 2.7 | 2.6 | 3.7 | 4.2 |
| 32 or less | 25 | 98% | 1.7 | 3.9 | 3.6 | 2.9 | 4.2 | 4.8 |
| 32 or less | 26 | 80% | 1.8 | 3.8 | 3.4 | 3.0 | 4.2 | 4.8 |
| 32 or less | 27 | 37% | 1.6 | 3.5 | 3.1 | 2.8 | 4.0 | 4.5 |
| 32 or less | 28 | 13% | 1.5 | 3.3 | 2.9 | 2.7 | 3.8 | 4.3 |
| 32 or less | 29 | 3.9% | 1.3 | 3.0 | 2.7 | 2.6 | 3.6 | 4.0 |

- **A 5c has to be about 5 moves shorter than a 3c**: 4.0 to 5.1 depending on the lengths and the target. asacuber's "maybe like 5-6" ([5 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1247972799151341690)) is right at the 5 end: 5 shorter is break-even, 6 shorter is clearly the better skeleton.
- **The others**, how many moves shorter:

  | 3c1t | 3tc | pure 2c2c | twisted 2c2c | 2tc |
  |---:|---:|---:|---:|---:|
  | 3.6 to 4.6 | 3.0 to 4.4 | 2.7 to 4.1 | 2.6 to 3.3 | 1.3 to 2.2 |

- The rates are a little lower when the 3c is unlikely to make the target (bottom rows of each block): when you need luck, the two-comm skeleton has the wider spread.
- **With algs up to 10** the same table (Appendix A, fewer skeletons) gives a 5c about 3.8 to 4.9 and a pure 2c2c about 1.8 to 3.9: the longer algs help the two-comm types more than the 3c.

### 7.3 The thresholds people quoted

**Chance of the stated goal, random skeletons, 8-movers. The expected total is the length plus the mean added over the skeletons where something fits.**

| Who | Skeleton and goal | Chance of the goal | Expected total where something fits |
|---|---|---:|---:|
| the tutorial | 3c in 23: "you will probably get it" (sub-30) | 76% | 28.8 |
| the tutorial | 3c in 25: "you will need some luck" (sub-30) | 12% | 30.7 |
| sequesteredcuber | sub-22 for a 3c skeleton (sub-30) | 99.6% | 26.9 |
| sequesteredcuber | sub-20 for every other skeleton (sub-30): a 5c | 48% | 29.4 |
| sequesteredcuber | sub-20 for every other skeleton (sub-30): a 3c1t | 63% | 29.0 |
| sequesteredcuber | sub-20 for every other skeleton (sub-30): a pure 2c2c | 87% | 28.2 |
| Gezza Cubing | 3c in 22 (sub-30) | 97% | 27.8 |
| Gezza Cubing, oliynykmax | 3c in 24 (sub-30) | 34% | 29.7 |
| Gezza Cubing | 5c in 16 (sub-30) | 99.8% | 26.7 |
| Gezza Cubing, oliynykmax | 5c in 18 (sub-30) | 80% | 28.5 |
| oliynykmax | 3c1t in 18 (sub-30) | 92% | 28.1 |
| trangium | 3c in 28 (sub-35) | 83% | 33.6 |
| trangium | 5c in 22 (sub-35) | 99% | 32.2 |
| trangium | 3c1t in 22 (sub-35) | 99.9% | 31.8 |

- **The tutorial's pair for sub-30 holds**: 3c in 23 "you will probably get it" is 76%, and 3c in 25 "you will need some luck" is 12%.
- **"a skeleton leaving 4 corner in 18 moves is probably better than one leaving 3 corners in 25"**: by a lot. Expected 26.9 to 28.1 against 30.7.
- **Gezza Cubing's and oliynykmax's pairs** (3c in 22-24 or 24, 5c in 16-18 or 18) put the 5c six moves under the 3c. At that distance the 5c is the better of the two: a 5c in 18 makes sub-30 80% of the time, a 3c in 24 34%.
- **sequesteredcuber's "sub-22 for 3C skeleton", "sub-20 for every other skeleton"** ([8 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1127188954995769364)) puts them two moves apart, which is too close: a 3c in 21 is sub-30 99.6% of the time, a 5c in 19 only 48% (a 19-move 5c with the usual outcome, 30, is written out below).
- **21 to 3c, "thats a guaranteed 29 right?"** ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443620873839051034)). kyh ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443621022745235476), [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443621113996513372)): "not strictly guaranteed", "but it's very likely you're getting a 29 or better". 99.6% with 8-movers. The rest are the skeletons where no 8-mover fits anywhere; there it takes a 9- or 10-mover, and the result can be 30 or 31 (one is written out below).
- **zakk drewji's 19 to 5c giving 29, or 24 to 3c with three minutes left** ([9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414839448042082337)). Eli Rogers ([9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414943087272136715)): "3c would need to cancel 4 to beat the 29". An 8-4 or better is there on 11% of 24-move 3c skeletons. kyh ([9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414840422177570836)): "the chance ur cancelling 4 moves or more is not that high i think". Right, and DougCube's "I would go with the 29" ([9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414882469198696488)) follows.

A 19-move 5c that gives 30, the most common outcome for one:

```
R' U' F L2 D B2 L2 U B2 L2 D2 B2 D2 F2 U' R B L' B' F L' U' L R2 D R' U' F   // scramble
F2 D2 R2 D' F' L F R' D B2 L B R' B' U' B2 U2 L2 D                           // skeleton (19)
```

It leaves a corner 5-cycle: DBL → UFL → DBR → UBR → UBL → DBL.

**Best with two 8-move comms**: 30 in all.

```
F2 D2 R2 D' F' L F ^ R' D B2 L B R' * B' U' B2 U2 L2 D
* = D2 B' U2 B D2 B' U2 B // (8-3/24)
^ = D R' U2 R D' R' U2 R // (8-2/30)
Solution: F2 D2 R2 D' F' L F D R' U2 R D' R' U2 D B2 L B R' D2 B' U2 B D2 B' U B2 U2 L2 D (30)
```

A 21-move 3c that does not give 29:

```
R' U' F L' D2 B2 L2 U2 B2 R' D2 U2 L2 U' F' R F2 D2 L2 D L B' U' R' U' F   // scramble
B' D L' U2 L' U2 D2 R D B' U F R2 F B' U B' D' B2 U R2                     // skeleton (21)
```

It leaves a corner 3-cycle: DFL → UBR → UBL → DFL.

**With 8-movers**: nothing: no spot has a case with an 8-move alg.

**Best with algs of up to 10 moves**: 30 in all, a 9-mover.

```
B' D L' U2 L' U2 D2 R D B' U F R2 F * B' U B' D' B2 U R2
* = U2 B' U' F2 U B U' F2 U' // (9-0/30)
Solution: B' D L' U2 L' U2 D2 R D B' U F R2 F U2 B' U' F2 U B U' F2 U' B' U B' D' B2 U R2 (30)
```

---

## 8. Finding them

So far it's been what the best insertion costs. This section is where it sits and what you lose by searching less, so it's the part you can use in an attempt: every other move, the ends, opposite-face pairs, how far to follow first comms. It's all random skeletons unless I say otherwise, and none of it measures time.

### 8.1 Where the best insertion sits

Where the best 3c insertion sits in the skeleton, by thirds. When several spots tie for the best, each gets an equal share.

**Where the best 3c insertion is, random skeletons, 20,000 per row. Lengths where the spots split evenly into three.**

| Skeleton length | Cap 8: first third | Cap 8: middle third | Cap 8: last third | Cap 10: first third | Cap 10: middle third | Cap 10: last third |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 33% | 34% | 33% | 32% | 35% | 32% |
| 20 | 33% | 34% | 33% | 33% | 35% | 33% |
| 26 | 33% | 34% | 33% | 33% | 35% | 33% |

Flat. And spot by spot on the 20-move skeletons, with 8-movers:

**3c, 20,000 random skeletons of 20 moves, 8-movers: each spot of the skeleton.**

| Position | An 8-mover fits there | Mean added when one fits | It is 8-3 or better | A best insertion of the skeleton is there |
|---|---:|---:|---:|---:|
| before the first move | 52% | 7.58 | 1.1% | 7.8% |
| after move 1 | 53% | 7.24 | 2.7% | 13% |
| after move 2 | 52% | 7.18 | 3.8% | 14% |
| after moves 3 to 17 (each) | 52% | 7.17 | 4.0% | 13% |
| after move 18 | 52% | 7.17 | 3.9% | 14% |
| after move 19 | 53% | 7.23 | 2.8% | 13% |
| after the last move | 53% | 7.57 | 1.2% | 7.8% |

- **No third is better than another on a random skeleton.** DougCube ([8 Jul 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1524584097085657221)): "In my stats, I found that the best insertion points tend to be in the first 1/3 or last 1/3 of the skel." And ([8 Jul 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1524584188269953187)): "no idea why". Random move sequences don't show it. DougCube's stats are of the insertions they found in their own solves, of every kind, and two other messages say how they search: "if I need to do two insertions that are linked, the first one will be near the end of the skel or the start of the skel" ([14 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1427774293495910593)) and "single 3c insertions are super quick when it's near the start or end of skel for me" ([18 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1395640562861871221)). That's a different thing from where the best 8-mover for a 3c sits, which is what I count here. Section 9.4 has the real skeletons, DougCube's among them.
- **The two end spots are worse**, as paulduc03 says ([9 Jul 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1524669961338097684)): "if you are too close to the beginning or to the end of the skeleton, you have less chances to find a 8-6 or better". Before the first move and after the last, an alg can only cancel on one side, so an 8-3 or better is there 1.1% of the time against 4.0% at an inner spot. One move in from either end it is 2.7%. From the second move in, every spot is as good as any other.
- **An 8-mover fits at about half the spots** (52%), which is the 528 of 1,008 of section 5. Auric Cui's "if you get a 5c you only have 15 chances to find a commutator" on a 15-move skeleton ([21 Apr 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1098915502576906281)) is really 16 spots, as Not officially a David pointed out ([21 Apr 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1098919975273635921)), with five cycles to try at each.

### 8.2 How much cancels, and with which alg

**3c, the best insertion with 8-movers: how many moves it cancels. Random skeletons, 20,000 per row.**

| Skeleton length | No 8-mover fits | 8-0 | 8-1 | 8-2 | 8-3 | 8-4 | 8-5 | 8-6 or more |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 4.2% | 14% | 35% | 31% | 11% | 3.4% | 0.88% | 0.37% |
| 14 | 1.7% | 8.9% | 32% | 36% | 15% | 4.7% | 1.2% | 0.47% |
| 18 | 0.65% | 5.0% | 27% | 40% | 19% | 6.1% | 1.7% | 0.72% |
| 20 | 0.36% | 3.8% | 25% | 42% | 20% | 6.7% | 1.9% | 0.73% |
| 22 | 0.24% | 2.8% | 22% | 42% | 22% | 7.7% | 2.0% | 0.69% |
| 26 | 0.08% | 1.7% | 18% | 43% | 24% | 9.2% | 2.3% | 0.96% |
| 30 | 0.05% | 1.0% | 15% | 43% | 28% | 10% | 2.7% | 1.0% |

- **8-2 is the usual best**, 42% of 20-move skeletons, then 8-1 (25%) and 8-3 (20%).
- Gezza Cubing ([20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253277567209963522)): "usually you should at least be able to cancel like 2 moves for each comm". For a 3c: 71% of 20-move skeletons have an 8-2 or better.
- An 8-3 or better exists on 29% of 20-move 3c skeletons and 42% of 30-move ones. On a 5c the first comm has much better odds (8.4).
- kyh ([9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414840422177570836)): "the chance ur cancelling 4 moves or more is not that high i think". 9.3% at 20 moves, 12% at 26.

**3c: when a longer alg is the best. Random skeletons, 20,000 per row. The first four columns split the skeletons by the shortest alg that gives the best insertion with algs of up to 10 moves, so they add up to 100%. The four means at the end are over the same skeletons, the ones where an 8-mover fits.**

| Skeleton length | An 8-mover is as good as anything up to 10 | A 9-mover beats every 8-mover and no 10-mover beats it | A 10-mover beats every 8- and 9-mover | No alg of up to 10 moves fits | When a 10-mover beats every 8- and 9-mover: by one move only | An 11- or 12-mover beats everything up to 10 | Skeletons where an 8-mover fits | Mean added on those skeletons, cap 8 | Same skeletons, cap 9: mean added | Same skeletons, cap 10: mean added | Same skeletons, cap 12: mean added |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 91% | 4.1% | 5.4% | <0.01% | 80% | 4.7% | 19,151 | 6.44 | 6.43 | 6.37 | 6.32 |
| 14 | 93% | 2.1% | 5.0% | 0 | 78% | 5.3% | 19,655 | 6.20 | 6.19 | 6.13 | 6.07 |
| 18 | 94% | 0.93% | 4.9% | 0 | 78% | 5.5% | 19,870 | 5.98 | 5.97 | 5.91 | 5.84 |
| 20 | 95% | 0.61% | 4.7% | 0 | 77% | 5.5% | 19,928 | 5.90 | 5.90 | 5.84 | 5.77 |
| 22 | 95% | 0.48% | 4.5% | 0 | 76% | 5.7% | 19,952 | 5.82 | 5.81 | 5.75 | 5.68 |
| 26 | 95% | 0.29% | 4.5% | 0 | 76% | 6.1% | 19,984 | 5.68 | 5.67 | 5.62 | 5.53 |
| 30 | 95% | 0.16% | 4.6% | 0 | 75% | 6.2% | 19,991 | 5.56 | 5.56 | 5.50 | 5.41 |

- **An 8-mover is as good as anything up to 10 moves on 95% of 20-move skeletons.**
- **A 9-mover is the best on 0.61%** at 20 moves, and on short skeletons mostly because no 8-mover fits at all. The tutorial: "It happens extremely rarely that the best insertion is given by a 9 move commutator (or longer)". For 9-movers that's right.
- **A 10-mover beats everything shorter on 4.7%**, about one skeleton in 21, and an 11- or 12-mover beats everything up to 10 on 5.5%. That's not extremely rare (example [b] in section 10). notkevin's 15 to 3c ([15 Jun 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1383989835550953606)), "optimal is 10-4 for a 21, 8-1 for a 22 using 8-movers only", is one of these.
- **But you don't gain much**: when a 10-mover wins it's by a single move 77% of the time, so on the skeletons where an 8-mover fits the mean only goes from 5.90 to 5.84 to 5.77.

**Setups around a regular comm.** Ben ([25 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1465081370131959961)): "if its a setup to a regular comm then it wont cancel more than just inserting 8 movers". 10,368 of the 11,856 ten-move algs are a setup move, an 8-mover and the setup undone. When the setup cancels a whole move of the skeleton, that's the same solution as the 8-mover one spot over, like Ben says. On the 935 skeletons (of 20,000) where a 10-mover beats everything shorter:

| Which algs are among the best | Skeletons |
|---|---:|
| a 10-mover of another kind | 849 |
| only setup-type ones, each time by one move, with the setup joining a turn of the skeleton on its own face | 86 |

That second kind is the 8-mover put inside the turn (a `B'` done as `B2`, the comm, `B`), which no spot between two moves gives you. So Ben's rule holds on all but 0.43% of 20-move skeletons.

One of those 86:

```
R' U' F L R U2 B2 U2 F2 R U2 L2 F2 D2 R F' U' B2 R' D2 B R U2 F' R' U' F   // scramble
R' B' U' L' F' B' L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2                   // skeleton (20)
```

It leaves a corner 3-cycle: DBR → UBR → DFR → DBR.

**Best with 8-movers**: 28 in all.

```
R' B' U' L' F' B' L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2 *
* = D' F' D B' D' F D B // (8-0/28)
Solution: R' B' U' L' F' B' L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2 D' F' D B' D' F D B (28)
```

**Best with algs of up to 10 moves**: 27 in all, a setup move, an 8-mover and the setup undone.

```
R' B' U' L' F' B' * L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2
* = F B' R2 F' L2 F R2 F' L2 B // (10-3/27)
Solution: R' B' U' L' B2 R2 F' L2 F R2 F' L2 B L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2 (27)
```

The 10-mover is this 8-mover between `B'` and `B`:

```
F R2 F' L2 F R2 F' L2   // the 8-mover inside the 10-mover
```

The same solution is that 8-mover put inside move 6 of the skeleton, the `B'` done in two parts: `B2`, the comm, `B`. No spot between two moves gives that with an 8-mover.

### 8.3 Checking every other move

alkamaass ([31 May 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246265963264086037), [31 May 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246265995350380655), [31 May 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246266143551787058)): "desperate with time check every other move", "but you have to check the ends", "this isn't thorough tho bc it can miss stuff like R (R blah blah B' ) B'". notkevin ([7 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1436457200880189582)) on why it works: "(this is also why it's often recommended to check every other move when doing a lot of 2-insertion skeletons, bc if you're expecting at least a -3 somewhere, it has to cancel at least a full move, so checking every other still guarantees you'll find them)". The idea: an insertion that cancels a whole move against its neighbour also shows up one spot over, as a cyclic shift of the same alg.

Here's every second spot plus both ends, and every third spot plus both ends, against checking all of them, for one 8-move comm on a 3c:

**3c, 8-movers, random skeletons (20,000 per length, each counted once for every way of starting the count). Only skeletons with an 8-mover somewhere are counted. *Mean loss* is how much longer the result is than with every spot checked; a set of spots that holds no 8-mover at all is scored as an 8-0.**

| Skeleton length | Every other move finds the best | Every other move: mean loss, moves | All misses of every other move: next to two opposite-face moves | Every third move finds the best | Every third move: mean loss, moves |
|---:|---:|---:|---:|---:|---:|
| 10 | 86% | 0.14 | 27% | 71% | 0.35 |
| 14 | 87% | 0.13 | 31% | 71% | 0.36 |
| 18 | 89% | 0.12 | 38% | 72% | 0.36 |
| 20 | 89% | 0.11 | 38% | 72% | 0.36 |
| 22 | 90% | 0.11 | 42% | 73% | 0.35 |
| 26 | 91% | 0.09 | 46% | 74% | 0.34 |
| 30 | 93% | 0.08 | 50% | 75% | 0.32 |

**The same walks on the skeletons whose best is an 8-3 or better: how often each rule finds it, and, counted in walks, what every other move missed and where.**

| Skeleton length | Best is 8-3 or better: every other move finds it | Best is 8-3 or better: every third move finds it | Best is 8-3 or better and every other move missed it: walks | Of those, the best was 8-3 | Of those, the best was 8-4 | Of those, next to two opposite-face moves |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 97% | 75% | 205 | 201 | 4 | 205 |
| 14 | 97% | 75% | 266 | 264 | 2 | 266 |
| 18 | 97% | 75% | 361 | 349 | 12 | 361 |
| 20 | 97% | 75% | 371 | 361 | 10 | 371 |
| 22 | 97% | 75% | 426 | 408 | 18 | 426 |
| 26 | 97% | 75% | 418 | 408 | 10 | 418 |
| 30 | 97% | 76% | 490 | 470 | 20 | 490 |

- **Every other move finds the best insertion 89% of the time** at 20 moves, and loses 0.11 of a move on average.
- **When the best is an 8-3 or better it's found 97% of the time**, so "guarantees" is a little too strong. alkamaass had already said the rule isn't thorough, with a miss of another kind. This one only joins the move on either side, so it cancels one move at each end (an 8-2, if it's an 8-mover):

  ```
  R (R blah blah B' ) B'   // alkamaass's example of what every other move can miss
  ```

  The misses of an 8-3 or better are different. Every one of them sits next to two moves on opposite faces (`R L`, `U D'`), 371 of 371 at 20 moves: there a full cancel reaches across the pair, and the alg moved over the move it cancels would go between the two moves of the pair, which takes writing the pair the other way round (example [c]). The tutorial's footnote covers it: "when in a skeleton there are two consecutive parallel layers moves try swapping them too see if this gives better insertions". So check every other move, and both sides of a parallel pair. (Of all the misses, the 8-2s and worse included, 38% are next to such a pair.)
- **What you miss is small**: when the best is 8-3 or better, the misses are 8-3s and a few 8-4s (fifth and sixth columns). Nothing better than an 8-4 was missed on any of 140,000 skeletons.
- notkevin's next line ([7 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1436457482577907792)) is about two comms, which this table does not test: "(aka, the worst insertions you can miss with this without the second comm nesting is -4, where both comms only partially cancel on both sides)".
- **Every third move doesn't work.** With a best of 8-3 or better, every third spot and both ends finds it only 75% of the time.

A skeleton where every other move misses the only 8-3:

```
R' U' F R U2 F2 D2 R' U2 F2 R' F2 L2 R F2 R U R F' L2 B U2 F' L F' R' U' F   // scramble
F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' F' B U2 B' L D                       // skeleton (20)
```

It leaves a corner 3-cycle: DBR → UBR → DFR → DBR.

**The best 8-mover insertion**: 25 in all, the only 8-3 in the skeleton, after move 16.

```
F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' F' B * U2 B' L D
* = F D F' U F D' F' U' // (8-3/25)
Solution: F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' B D F' U F D' F' U B' L D (25)
```

Counting spots from 0 (before the first move), the 8-3 is at spot 16. Checking the odd spots (1, 3, 5, 7, 9, 11, 13, 15, 17, 19) and both ends finds nothing better than an 8-1; the even spots would find it. The spot is right after the pair `F' B`. Written the other way round, `B F'`, the alg moved one move over, `D F' U F D' F' U' F`, fits between the two for the same 25; as written, spot 14 gives nothing better than an 8-1.

And one where every third spot misses it:

```
R' U' F R2 D F2 U2 L2 U F2 U' B2 U2 B2 L' F R2 D' R' B2 L' F D2 R' U' F   // scramble
D' R2 U2 L U2 D' R' F2 L U L U' B U' R U2 R2 U2 D2 L2                     // skeleton (20)
```

It leaves a corner 3-cycle: UFL → DFR → UFR → UFL.

**The best 8-mover insertion**: 25 in all, the only 8-3 in the skeleton, after move 4.

```
D' R2 U2 L * U2 D' R' F2 L U L U' B U' R U2 R2 U2 D2 L2
* = L U' L' D' L U L' D // (8-3/25)
Solution: D' R2 U2 L2 U' L' D' L U L' U2 R' F2 L U L U' B U' R U2 R2 U2 D2 L2 (25)
```

Counting spots from 0 (before the first move), the 8-3 is at spot 4. Every other spot from the start (0, 2, 4, and so on) passes it. Every third spot from the start (0, 3, 6, and so on, and the end) does not, and finds nothing better than an 8-1. Of the three ways to take every third spot, only the one that starts at spot 1 passes spot 4.

**Three spots on after a 10-move case.** paulduc03 asked something narrower ([30 Dec 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1455642235449114665)): "When I check between 2 moves in my 3C skeleton, sometimes it happens that the most optimal way to solve the 3C is 10 moves. In this case, can I go 3 moves further instead of 2 and still make sur not to miss any insertion below 6 moves ?" DougCube ([30 Dec 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1455657733272633651)): "I don't think that works."

**3c, random skeletons, 20,000 per length. A spot *needs a 10-mover* when the shortest alg for the case at that spot has 10 moves; only spots with two more spots after them are counted. One row per skeleton length: how many such spots there are, and how often the next spot or the one after has an 8-3 or better.**

| Skeleton length | Spots whose case needs a 10-mover | An 8-3 or better at the next spot | An 8-3 or better two spots on |
|---:|---:|---:|---:|
| 10 | 14,466 | 0.41% | 1.4% |
| 14 | 20,761 | 0.44% | 1.6% |
| 18 | 27,041 | 0.41% | 1.5% |
| 20 | 30,002 | 0.57% | 1.7% |
| 22 | 33,149 | 0.52% | 1.5% |
| 26 | 39,723 | 0.42% | 1.5% |
| 30 | 46,177 | 0.50% | 1.7% |

**The walks check every other spot and both ends for 8-movers, once starting at spot 0 and once at spot 1, on the skeletons whose best is an 8-3 or better. One row per skeleton length: how many walks miss that best, plain and when going three spots on, not two, after every spot that needs a 10-mover.**

| Skeleton length | Walks on skeletons with a best of 8-3 or better | Every other move misses it: walks | Every other move misses it: share | Three spots on after a 10-move case misses it: walks | Three spots on after a 10-move case misses it: share |
|---:|---:|---:|---:|---:|---:|
| 10 | 6,114 | 205 | 3.4% | 239 | 3.9% |
| 14 | 8,552 | 266 | 3.1% | 317 | 3.7% |
| 18 | 10,820 | 361 | 3.3% | 426 | 3.9% |
| 20 | 11,708 | 371 | 3.2% | 462 | 3.9% |
| 22 | 12,894 | 426 | 3.3% | 482 | 3.7% |
| 26 | 14,710 | 418 | 2.8% | 490 | 3.3% |
| 30 | 16,614 | 490 | 2.9% | 567 | 3.4% |

- **DougCube is right.** At 20 moves:

  | After a spot whose case needs a 10-mover, 20-move skeletons | Share | How many | Out of |
  |---|---:|---:|---:|
  | the spot two further on holds an 8-3 or better (spots) | 1.7% | 514 | 30,002 |
  | the spot right after it holds one (spots) | 0.57% | 171 | 30,002 |
  | walking a 20-move skeleton that way misses a best of 8-3 or better (walks) | 3.9% | 462 | 11,708 |
  | plain every other move misses it (walks) | 3.2% | 371 | 11,708 |

- **By cases, exactly.** 80 of the 1,008 corner 3-cycles have a shortest alg of 10 moves.
  - One move on: for 48 of them no single move leads to a case with an 8-mover; for the other 32, 12 of the 18 moves do.
  - Two moves on: every one of the 80 can be at a case with an 8-mover (7,296 of the 21,600 combinations of a case and two moves).

  So a case that needs 10 moves tells you nothing safe about the spot two further on.

A skeleton where going three on misses the only 8-3:

```
R' U' F B' U2 B2 L2 F U2 F L2 U2 L2 R B2 F L D' B' U B L2 B' R' U' F   // scramble
L' U' D B L' U' R D L D' R' L D' B2 U' B2 U2 B D' B'                   // skeleton (20)
```

It leaves a corner 3-cycle: DFR → UBR → UFR → DFR.

**The best 8-mover insertion**: 25 in all, the only 8-3 in the skeleton, after move 10.

```
L' U' D B L' U' R D L D' * R' L D' B2 U' B2 U2 B D' B'
* = D' L U' L' D L U L' // (8-3/25)
Solution: L' U' D B L' U' R D L D2 L U' L' D L U R' D' B2 U' B2 U2 B D' B' (25)
```

Counting spots from 0. Checking every other spot from the start, spot 8 is the first whose case has no alg shorter than 10 moves. One of them:

```
U' R' B2 R F R' B2 R F' U   // a 10-mover for spot 8
```

Two spots on, at spot 10, is the 8-3. Going three on instead lands on spot 11, and the walk (spots 0, 2, 4, 6, 8, 11, 13, 15, 17, 19, 20) finds nothing better than an 8-1.

### 8.4 The first comm of a 5c

Nobody searches every pair of comms by hand. You find the best first comm, maybe write down a few more, and then look for the second comm in each. Insertion Finder's *greedy* setting is the same idea, in its own words: "Let's say when searching insertions for each step, the minimum moves of all skeletons is M. IF will keep all skeletons whose moves equal or less than M + N moves. 0 means always best first (human mode?)." So two questions: how good is the best first comm, and what do you lose by following only the best ones?

**The best first comm of a 5c, 8-movers, random skeletons (5,000 per length; 20,000 at 20 moves), next to the best comm of a 3c of the same length.**

| Skeleton length | 5c: best first comm, mean added | 5c: 8-3 or better | 5c: 8-4 or better | 5c: 8-5 or better | 3c: best comm, mean added | 3c: 8-3 or better | 3c: 8-4 or better |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 12 | 5.09 | 62% | 23% | 7.0% | 6.30 | 19% | 5.5% |
| 14 | 4.96 | 67% | 27% | 7.7% | 6.20 | 21% | 6.4% |
| 16 | 4.86 | 71% | 31% | 9.0% | 6.08 | 24% | 7.7% |
| 18 | 4.75 | 77% | 34% | 10% | 5.98 | 27% | 8.5% |
| 20 | 4.67 | 80% | 37% | 11% | 5.90 | 29% | 9.3% |
| 24 | 4.52 | 86% | 43% | 13% | 5.74 | 34% | 11% |

- **The first comm of a 5c is much better than the comm of a 3c**: 4.67 against 5.90 at 20 moves. You get five cycles to choose from at every spot (Not officially a David, [21 Apr 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1098919767429099570): "for the first 5c insertion you have 5x more options than for the second"; Zagros, [16 Aug 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1406274793552220182): "there are 5 possible cycles, not 1").
- Ben ([31 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1467098844712931498)): "you'll probably have at least an 8-3 or 8-4 for the first one". The best first comm on 5c skeletons:

  | Skeleton | 8-3 or better | 8-4 or better |
  |---|---:|---:|
  | 16 moves | 71% | 31% |
  | 20 moves | 80% | 37% |

  So you get an 8-3 most of the time, and an 8-4 about one time in 3 on a 16-move skeleton.

**Following only the best first comms: two 8-move comms on random skeletons of 20 moves. *Best first comm only* is the best first comm (all that tie for it) followed by the best second; *within 1 move* also follows the first comms one move worse. *Loses* is the share of skeletons where the result is longer than the best pair. A rule that ends with no second comm after the first comms it follows counts as a loss and is left out of that rule's mean; for the best first comm only, the sixth column says on how many skeletons that happens.**

| Leftover | Skeletons | Best pair of comms: mean added | Best first comm only: mean added | Best first comm only: loses | Best first comm only: no second comm fits | First comms within 1 move: mean added | Within 1 move: loses | First comms within 2 moves: mean added | Within 2 moves: loses |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2tc | 5,000 | 7.71 | 7.94 | 18% | 4 | 7.75 | 2.9% | 7.72 | 0.20% |
| 3tc | 5,000 | 9.52 | 9.58 | 6.5% | 6 | 9.52 | 0.34% | 9.52 | 0 |
| pure 2c2c | 5,000 | 9.15 | 9.24 | 8.8% | 7 | 9.15 | 0.60% | 9.15 | 0.02% |
| twisted 2c2c | 5,000 | 8.72 | 9.03 | 24% | 7 | 8.81 | 7.9% | 8.74 | 1.9% |
| 3c1t | 5,000 | 9.88 | 9.97 | 8.2% | 5 | 9.89 | 1.3% | 9.88 | 0.32% |
| 5c | 20,000 | 10.37 | 10.54 | 14% | 36 | 10.41 | 3.7% | 10.38 | 0.48% |
| 3c3c | 5,000 | 11.03 | 11.31 | 21% | 3 | 11.11 | 7.1% | 11.04 | 0.52% |

- **Taking the best first comm of a 5c and then the best second gets you 10.54 against 10.37 for the best pair**, and misses the best pair on 14% of skeletons. (All first comms that tie for the best are followed up.)
- **Also following up the first comms that are one move worse** brings that down to 3.7%, and two moves worse to 0.48%.
- This is what kyh ([26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486867754354086093), [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486867787023515738)) and argonblue ([26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486868609656688780)) ran into: "my pr single wouldve been a 30 if i didnt go look for sub optimal first insertions", "but its a 28"; "i just had to check a suboptimal first insertion (8-2 instead of 8-3) to get any cancellations in the second". The second comm depends on where the first one went, so the best first comm isn't always the one to follow.
- **What people say about the setting.** Ben ([26 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1476513726097129576), [26 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1476513882628685847)): "if you set greedy to 0 and only pick regular 3c comms then it basically shows human findable", "the main thing is setting it to greedy 0". And ([26 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1476514406320963629), [26 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1476514447182004265)): "greedy 1 is still reasonable if your skeleton is really good but anything higher isn't imo", "like if i have an 8-3 im not checking 8-1s ever". kyh ([26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486867581557280848)): "i think 1 is realistic". I don't measure what's findable. Here's what each setting gives on a 20-move 5c with 8-movers:

  | Setting | Mean added |
  |---|---:|
  | greedy 0 | 10.54 |
  | greedy 1 | 10.41 |
  | the best pair | 10.37 |

  By hand, greedy 1 means: when the best first comm is an 8-4, also follow up the 8-3s.
- **The other two-comm leftovers** are in the same table, with the same pattern: one move of slack on the first comm gets back most of the loss. A twisted 2c2c still loses on 7.9% of skeletons with it and a 3c3c on 7.1%.

A skeleton where the best first comm is the wrong one to follow:

```
R' U' F B2 L2 B2 U B2 D2 B2 U F2 R2 U' B2 R F U' B' R' U L F' L U' R' U' F   // scramble
F2 U2 L' D' F' R D2 F U B U' F2 R2 L2 D' L F2 U' D' F'                       // skeleton (20)
```

It leaves a corner 5-cycle: DFL → UFR → UBL → UFL → UBR → DFL.

**The best first comm, then the best second**: 33 in all, the first is the only 8-2 in the skeleton.

```
F2 U2 L' D' F' R D2 F U B U' F2 R2 L2 * D' L F2 U' ^ D' F'
* = R D L D' R' D L' D' // (8-2/26)
^ = U2 F' D2 F U2 F' D2 F // (8-1/33)
Solution: F2 U2 L' D' F' R D2 F U B U' F2 R' L2 D L D' R' D L' D2 L F2 U F' D2 F U2 F' D2 F D' F' (33)
```

**The best pair**: 31 in all.

```
F2 U2 L' D' F' R D2 F U B U' F2 R2 L2 D' * L F2 U' D' F'
* = D' R' U' R D R' U R // (8-1/27)
F2 U2 L' D' F' R D2 F U B U' F2 R2 L2 D2 R' U' R D R' U ^ R L F2 U' D' F'
^ = U' R2 U L2 U' R2 U L2 // (8-4/31)
Solution: F2 U2 L' D' F' R D2 F U B U' F2 R2 L2 D2 R' U' R D R U L2 U' R2 U R L' F2 U' D' F' (31)
```

**More algs at greedy 0 can make it worse, but rarely.** bvcuber13 on a 17-move 5c ([26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486828825756307620), [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486829034905014303)): "IF finds 30 🤮", "wait if i just do pure comms it finds a 29". tave_789 explained it on the spot ([26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486829396286246952)): "if 10-5 is the best first insertion it won’t find the optimals with a worse first insertion". Ben on a 14-move one ([24 Sep 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1552577949688008734), [24 Sep 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1552578104134860882)): "by enabling more corner algorithms on insertion finder with greedy 0 the result turns from 25 to 26", "with more obscure algs you can find a 10-4 for the first alg which doesn't give you the nested 8-4".

I see the same thing. I ran 2,000 random 5c skeletons of 20 moves with every 3c alg of up to 10 moves; on 1,998 of them the rule (best first comm, then the best second) ends with a solution under both lists. Against 8-movers only, the longer list gives:

| With the longer list | Skeletons |
|---|---:|
| a *longer* result | 0.25% |
| a shorter result | 9.3% |

So it's real and uncommon. What the longer list changes more is how often the best first comm is the right one to follow: at cap 10 it misses the best pair on 20% of skeletons, against 14% with 8-movers. Their Insertion Finder runs also had alg sets that aren't 3-cycles, which I don't model.

One of the 5 skeletons where the longer list gives the longer result:

```
R' U' F L2 B2 U2 B2 F2 D R2 U F2 D' L2 U' L U2 F' L' B2 D B' R2 D' L R' U' F   // scramble
D2 L D' L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U D' F                          // skeleton (20)
```

It leaves a corner 5-cycle: DBL → UBL → UBR → UFL → DFR → DBL.

**Best first comm, then the best second, 8-movers only**: 30 in all, the first comm is an 8-2 (2 first comms tie for the best; this is the one whose second comm is best).

```
D2 L D' L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U D' * F
* = D' B' D F2 D' B D F2 // (8-2/26)
D2 L D' L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U D2 B' ^ D F2 D' B D F'
^ = B U B' D' B U' B' D // (8-4/30)
Solution: D2 L D' L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U2 D2 B' D' B U' B' D2 F2 D' B D F' (30)
```

**The same rule with every 3c alg of up to 10 moves**: 32 in all, the first comm is now a 10-5 (3 first comms tie for the best; this is the one whose second comm is best), one move better than the 8-2, and the second comes out worse.

```
D2 L D' * L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U D' F ^
* = D L' D' L F L' D L D' F' // (10-5/25)
^ = F' U B' D2 B U' B' D2 F B // (10-3/32)
Solution: D L F L' D L D' F' L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U2 D' B' D2 B U' B' D2 F B (32)
```

---

## 9. Real skeletons and Insertion Finder

### 9.1 Which skeletons

The reading notes for this study hold 389 worked examples from the three channels and the docs: a scramble, a skeleton, usually the insertions and a final length. None of those had been put on a cube, so I replayed every one on a sticker model and only counted it if the scramble and the skeleton really leave one of the leftovers of section 4.

| Worked examples | How many |
|---|---:|
| Worked examples in the reading notes | 389 |
| left out: written with inverse-scramble parts | 147 |
| left out: skeleton has rotations, slice or wide moves | 5 |
| left out: scramble not in face turns | 4 |
| left out: corners and edges both left | 46 |
| left out: parity (2 corners and 2 edges) | 4 |
| left out: more than 6 pieces of one kind left | 5 |
| left out: scramble and skeleton do not fit | 3 |
| left out: three or more comms needed (not one of the types) | 7 |
| **used, from the server** | **168** |
| used, from Kalbarczyk's example solves (of 46 read) | 33 |
| **used in all** | **201** |
| distinct skeletons among them | 191 |
| of the server's: the author's own solution replays to the stated length | 119 |

The second source is Cyprian Kalbarczyk's "Blockbuilding example solves" (Kalbarczyk's own solves from late 2019 to October 2022, "probably from a better half of all scrambles"): the solves whose first skeleton and final solution could be read by a script.

That makes 201 worked examples on 191 distinct skeletons (a few skeletons were posted twice, or with two solutions). By leftover:

| Leftover | Skeletons |
|---|---:|
| 3c | 89 |
| 5c | 33 |
| 3c1t | 20 |
| 2c2c | 13 |
| 3e | 17 |
| others | 19 |

All of them are searched like the random ones: every spot, every alg within the cap. For edge leftovers the comm-plus-alg search at cap 12 didn't finish in the time allowed on 23 examples; those keep the better of their cap-12 result without it and their cap-10 result with it.

### 9.2 Real against random

Each real skeleton is compared with random skeletons of its own length and type (one comm for 3c and 3e; otherwise the best of two comms and one alg; no comm plus alg on either side).

**Mean added: real skeletons, and random skeletons of the same lengths and types. At cap 8 (8-movers; for edges, algs of 8 moves or fewer) the means are over the real skeletons where something fits, counted in the fourth column; at caps 10 and 12 something fits on every one. There is no random sample at cap 12 for these lengths.**

| Leftover | Real skeletons | Their mean length, moves | Cap 8: something fits on | Cap 8: real, mean added | Cap 8: random of the same lengths, mean added | Cap 10: real, mean added | Cap 10: random, mean added | Cap 12: real, mean added |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 3c | 89 | 18.4 | 89 of 89 | 5.12 | 5.98 | 4.96 | 5.94 | 4.89 |
| 2tc and 3tc | 2 | 13.0 | 2 of 2 | 10.00 | 10.25 | 10.00 | 10.11 | 9.00 |
| 2c2c (pure or twisted) | 13 | 17.5 | 13 of 13 | 8.46 | 9.04 | 7.92 | 8.80 | 7.15 |
| 3c1t | 20 | 16.9 | 20 of 20 | 8.65 | 10.16 | 8.45 | 10.06 | 8.35 |
| 5c | 33 | 16.7 | 33 of 33 | 9.85 | 10.63 | 9.39 | 10.29 | 8.94 |
| 3c3c | 2 | 14.5 | 2 of 2 | 10.50 | 11.45 | 10.50 | 10.92 | 10.50 |
| 3e | 17 | 20.2 | 14 of 17 | 4.79 | 5.93 | 3.18 | 6.05 | 3.12 |
| 2e2e, 2fe, 3e1f, 5e, 3e3e | 15 | 16.5 | 15 of 15 | 9.53 | 10.59 | 6.13 | 8.61 | 6.00 |

Real skeletons come out cheaper, and by a lot. With 8-movers, real minus random in moves added per skeleton:

| Leftover | Real minus random, moves | ± one standard error |
|---|---:|---:|
| 3c | -0.86 | 0.15 |
| 5c | -0.78 | 0.34 |
| 3c1t | -1.51 | 0.48 |

In this section ± is one standard error of the difference (Appendix C gives two standard errors for the random samples). Two tests say where the gap comes from.

**It's not how real skeletons are written.** Take the same real move sequences, all 188 of them that are 10 to 30 moves long, and put a random 3c or a random 5c on each, many times over:

**The real move sequences with a random leftover, against random sequences of the same lengths with a random leftover: mean added at cap 8. One row per leftover.**

| Leftover put on the real move sequences | Skeletons made (a real sequence with a random leftover) | Cap 8: real sequences, mean added | Cap 8: the mean is over | Cap 8: random sequences of the same lengths, mean added |
|---|---:|---:|---|---:|
| a random 3c | 18,800 | 6.01 | the 18,581 where something fits | 6.00 |
| a random 5c | 9,400 | 10.48 | all of them | 10.54 |

**The same at cap 10, one row per leftover.**

| Leftover put on the real move sequences | Skeletons made (a real sequence with a random leftover) | Cap 10: real sequences, mean added | Cap 10: the mean is over | Cap 10: random sequences of the same lengths, mean added |
|---|---:|---:|---|---:|
| a random 3c | 18,800 | 5.96 | all of them | 5.96 |
| a random 5c | 9,400 | 10.10 | the first 2,000 (only those were run) | 10.20 |

For a 3c it's the same as random sequences (6.01 against 6.00 at cap 8). For a 5c within a tenth of a move: the real sequences are 0.06 cheaper at cap 8 and 0.10 at cap 10. Blocks, pairs and triggers in the moves make next to no difference to how insertions cancel.

**Selection is part of it.** Split by where the skeleton comes from:

**Real minus random, 8-movers, by where the skeleton was posted. One row per group of skeletons; the difference is in moves added, with one standard error next to it.**

| Skeletons | 3c: how many | 3c: real minus random, moves | 3c: ± one standard error | 5c: how many | 5c: real minus random, moves | 5c: ± one standard error |
|---|---:|---:|---:|---:|---:|---:|
| all | 89 | -0.86 | 0.15 | 33 | -0.78 | 0.34 |
| from the server, an insertion written out | 55 | -1.13 | 0.20 | 22 | -1.15 | 0.46 |
| from the server, no insertion written (a skeleton posted as it is) | 17 | -0.49 | 0.34 | 7 | -0.04 | 0.54 |
| Kalbarczyk's example solves | 17 | -0.33 | 0.27 | 4 | -0.04 | 0.19 |
| the last two together | 34 | -0.41 | 0.21 | 11 | -0.04 | 0.34 |

- A skeleton posted together with its insertion is more than a move cheaper than a random one (-1.13 ± 0.20 for a 3c). People post the solves that came out well, and you rarely see a skeleton nobody found a decent insertion for.
- The two groups that are picked less are skeletons posted as they are and Kalbarczyk's collection:

  | For a 3c | Skeletons | Real minus random |
  |---|---:|---:|
  | posted as they are | 17 | -0.49 ± 0.34 |
  | Kalbarczyk's collection | 17 | -0.33 ± 0.27 |
  | both together | 34 | -0.41 ± 0.21 |

  The 11 such 5c are at zero (-0.04 ± 0.34).

- So selection is part of the gap: -1.13 for the 3c skeletons posted with their insertion, -0.41 for the 34 less-picked ones. Whether those last few tenths are real (the three corners left are the ones the last moves just handled, so a comm may cancel into them more easily) or just selection again, these few skeletons can't say. For a skeleton you've just found, start from the random-skeleton tables.

This bears on the estimates of section 2. The tutorial's corner rows and cpaul's 9 and 10 are what 8-movers give on random skeletons, each within about half a move. Phuwish's figures are close, except the 3tc. Baiqiang's are lower and are not averages ([28 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443860338440146986)). The posted skeletons are lower too: 8.65 for a 3c1t and 8.46 for a 2c2c with 8-movers: the skeletons that get posted are not a random draw from the skeletons that get found.

With a comm plus an alg also allowed, the same real skeletons average:

**Mean added on the real skeletons when a comm plus an alg is allowed as well. The last column is the number of skeletons where that search did not finish at cap 12; they keep the better of their cap-12 value without it and their cap-10 value with it.**

| Leftover | Real skeletons | Cap 8: something fits on | Cap 8: mean added | Cap 10: mean added | Cap 12: mean added | Cap 12 comm-plus-alg search not finished for |
|---|---:|---:|---:|---:|---:|---:|
| 3c | 89 | 89 of 89 | 5.08 | 4.88 | 4.67 | 0 |
| 2tc and 3tc | 2 | 2 of 2 | 10.00 | 10.00 | 9.00 | 0 |
| 2c2c (pure or twisted) | 13 | 13 of 13 | 8.46 | 7.62 | 6.85 | 0 |
| 3c1t | 20 | 20 of 20 | 8.65 | 8.25 | 7.65 | 0 |
| 5c | 33 | 33 of 33 | 9.85 | 9.18 | 8.27 | 0 |
| 3c3c | 2 | 2 of 2 | 10.50 | 10.50 | 10.50 | 0 |
| 3e | 17 | 17 of 17 | 5.06 | 3.00 | 3.00 | 17 |
| 2e2e, 2fe, 3e1f, 5e, 3e3e | 15 | 15 of 15 | 8.87 | 5.67 | 5.67 | 5 |

At cap 12 that's 7.65 for a 3c1t and 6.85 for a 2c2c. So posted skeletons searched with a full alg list land around Baiqiang's 8-9 and 6-8.

**Edges.** The 17 real 3e skeletons cost 3.18 at cap 10 against 6.05 for random ones (-2.87), and with algs of 8 or fewer something fits on 14 of the 17. Is that because their edges are oriented? For the leftover as it stands at the end of the skeleton, count on how many of the three axes all three of its edges are oriented:

**Edge 3-cycles by the number of axes on which their three edges are oriented: all 1,760 of them and how many have a short alg. One row per number of axes.**

| Axes on which the three edges are oriented | Edge 3-cycles | With a 6-move alg | With an alg of 8 moves or fewer | Share with an alg of 8 moves or fewer |
|---:|---:|---:|---:|---:|
| 3 | 24 | 24 | 24 | 100% |
| 2 | 288 | 0 | 144 | 50% |
| 1 | 672 | 0 | 0 | 0 |
| 0 | 776 | 0 | 0 | 0 |
| **all** | **1,760** | **24** | **168** | 9.5% |

**The same split for the real 3e skeletons and the random 20-move 3e skeletons of the sample, with their mean added at cap 10 (every alg of up to 10 moves).**

| Axes on which the three edges are oriented | Real 3e skeletons | Their mean added, cap 10 | Random 20-move 3e skeletons | Their mean added, cap 10 |
|---:|---:|---:|---:|---:|
| 3 | 2 | 2.50 | 257 | 4.29 |
| 2 | 4 | 4.00 | 3,262 | 5.68 |
| 1 | 7 | 3.57 | 7,581 | 6.06 |
| 0 | 4 | 2.00 | 8,900 | 6.22 |
| **all** | **17** | **3.18** | **20,000** | **6.05** |

- **The short algs do depend on it**, the way bpaul said ([10 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1470815636128010393)): every 3-cycle oriented on all three axes has a 6-mover and no other has one; half of those oriented on two axes have an alg of 8 or fewer; none of the rest does.
- **The real leftovers are oriented a little more often than a random 3-cycle:**

  | Oriented on | Real skeletons | All edge 3-cycles |
  |---|---:|---:|
  | two or three axes | 6 of 17 | 18% |
  | no axis | 4 of 17 | 44% |

- **But that's not what makes them cheap.** On random skeletons a leftover oriented on all three axes is about two moves cheaper at cap 10 than one oriented on none (4.29 against 6.22). The real ones are far below the random ones at every count: the 4 that are oriented on no axis average 2.00.
- **All 17 were posted with their insertion written out** (DougCube's 10-9 on the examples page is one of them). That's the selection of the 3c table again, only stronger. What a 3e costs on a skeleton you've just found, these 17 cannot say.

### 9.3 The authors against the search

For the examples that state a final length, the author's added moves against the best there is on the same skeleton. *One comm, two comms or one alg* is what the tables of section 6 use; the last two rows also allow a comm plus an alg.

Each row below is one cap the author is compared with; the middle columns count solutions by how many moves longer than the best the author's is.

**By hand, all leftovers:**

| Compared with the best at | Solutions | Author shorter | Same length | Author 1 move longer | Author 2 longer | Author 3 or more longer | Author, mean added | Best, mean added |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| cap 8: one comm or two (edges: algs of 6 to 8) | 168 | 32 | 125 | 4 | 2 | 5 | 6.30 | 6.80 |
| cap 10: one comm, two comms or one alg | 171 | 10 | 137 | 12 | 6 | 6 | 6.25 | 6.08 |
| cap 12: one comm, two comms or one alg | 171 | 8 | 127 | 16 | 11 | 9 | 6.25 | 5.89 |
| cap 10, a comm plus an alg also allowed | 171 | 9 | 128 | 18 | 7 | 9 | 6.25 | 5.96 |
| cap 12, a comm plus an alg also allowed | 171 | 6 | 114 | 21 | 14 | 16 | 6.25 | 5.63 |

**By hand, 3c only**, same columns:

| Compared with the best at | Solutions | Author shorter | Same length | Author 1 move longer | Author 2 longer | Author 3 or more longer | Author, mean added | Best, mean added |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| cap 8: one comm or two (edges: algs of 6 to 8) | 79 | 9 | 67 | 2 | 0 | 1 | 4.84 | 4.97 |
| cap 10: one comm, two comms or one alg | 79 | 6 | 66 | 3 | 2 | 2 | 4.84 | 4.77 |
| cap 12: one comm, two comms or one alg | 79 | 6 | 63 | 5 | 3 | 2 | 4.84 | 4.72 |
| cap 10, a comm plus an alg also allowed | 79 | 6 | 63 | 6 | 2 | 2 | 4.84 | 4.73 |
| cap 12, a comm plus an alg also allowed | 79 | 5 | 57 | 10 | 5 | 2 | 4.84 | 4.58 |

**By hand, the corner leftovers that need two comms**, same columns:

| Compared with the best at | Solutions | Author shorter | Same length | Author 1 move longer | Author 2 longer | Author 3 or more longer | Author, mean added | Best, mean added |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| cap 8: one comm or two (edges: algs of 6 to 8) | 60 | 7 | 45 | 2 | 2 | 4 | 9.03 | 9.00 |
| cap 10: one comm, two comms or one alg | 60 | 2 | 42 | 9 | 3 | 4 | 9.03 | 8.60 |
| cap 12: one comm, two comms or one alg | 60 | 1 | 36 | 9 | 7 | 7 | 9.03 | 8.20 |
| cap 10, a comm plus an alg also allowed | 60 | 2 | 40 | 10 | 2 | 6 | 9.03 | 8.48 |
| cap 12, a comm plus an alg also allowed | 60 | 0 | 32 | 9 | 6 | 13 | 9.03 | 7.73 |

- **On a 3c, the posted insertion is the best 8-mover insertion or better in 76 of 79 cases (96%).** 4 of the 79 are a second solution on a skeleton already in the list. Again, these are posted solves, and several say they were checked with Insertion Finder first.
- **On the corner leftovers that need two comms, 52 of 60 (87%)** are as good as the best pair of 8-movers or better.
- ***Author shorter* at cap 8** is someone using an alg longer than 8 moves.
- **Against algs up to 12** (**computer only**, the answer key), 21% of the hand solutions leave a move or more on the table. That's roughly what a full alg list adds over what people insert, on skeletons they were happy to post.
- **Shorter than anything in the search**: 6 solutions, all by hand, beat the best at cap 12 with a comm plus an alg. None of them does it with a better insertion: they add slice insertions, or rewrite a stretch of the finished solution with something shorter.

**The 6 solutions shorter than the best at cap 12 with a comm plus an alg, and why. *By* says whether the solution was found by hand or is an Insertion Finder result.**

| Example | By | Leftover | Skeleton, moves | Author's solution, moves | Best at cap 12 with a comm plus an alg, moves | What the author did besides inserting |
|---|---|---|---:|---:|---:|---|
| DougCube, [7 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1436364760076783727) | hand | flipped 2e2e | 18 | 22 | 25 | two slice insertions (`E2 ... E2`) on top of the 3e algs |
| DougCube, [21 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1463616140499615878) | hand | 3c | 11 | 17 | 18 | a slice pair (`M' ... M`) on top of the comm |
| caycala, [13 Sep 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1548755933352693924) | hand | 3c | 15 | 17 | 20 | a stretch of the finished solution rewritten shorter |
| DougCube, [7 Oct 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1557347209622585427) | hand | 3c | 17 | 19 | 21 | a slice pair (`S ... S'`) on top of the comm |
| Kalbarczyk, solve 27 | hand | 3c | 16 | 20 | 21 | a stretch of the finished solution rewritten shorter (the `[] =` line of the solve) |
| Kalbarczyk, solve 97 | hand | 3c | 20 | 24 | 25 | a stretch of the finished solution rewritten shorter (the `[] =` line of the solve) |

One of the slice pairs is the one kyh called "-3 with a slice insertion is insane" ([7 Oct 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1557347589911740479)).

What the hand insertions cancel, replayed move by move where the solution is written out:

**8-move insertions in the hand solutions, by what they cancel. One row per cancellation; each group has the number of insertions and their share of the group.**

| What the 8-move insertion cancels | All of them: insertions | All of them: share | On a 3c skeleton: insertions | On a 3c skeleton: share | On a skeleton that needs two: insertions | On a skeleton that needs two: share |
|---|---:|---:|---:|---:|---:|---:|
| all of them | 173 |  | 69 |  | 100 |  |
| 8-0 | 0 |  | 0 |  | 0 |  |
| 8-1 | 13 | 7.5% | 9 | 13% | 4 | 4.0% |
| 8-2 | 46 | 27% | 25 | 36% | 21 | 21% |
| 8-3 | 46 | 27% | 14 | 20% | 32 | 32% |
| 8-4 | 32 | 18% | 8 | 12% | 22 | 22% |
| 8-5 | 14 | 8.1% | 5 | 7.2% | 8 | 8.0% |
| 8-6 or more | 22 | 13% | 8 | 12% | 13 | 13% |

51% of the posted 8-movers on a 3c are 8-3 or better. On random skeletons the best insertion is that good 27% of the time at this length. Same selection, seen from the other side.

### 9.4 Where the best insertion is, on real skeletons

**3c: where the best 8-mover insertion is, by thirds of the skeleton, cut as in 8.1 (ties share). *Skeletons tried* is how many were searched; the shares are of the ones with an 8-mover somewhere (last column). The real move sequences with a random 3c are the first 6,000 of the 18,800 of section 9.2, and the random sequences are as many, of the same lengths.**

| 3c, the best 8-mover insertion is in the | First third | Middle third | Last third | Skeletons tried | Of them with an 8-mover somewhere |
|---|---:|---:|---:|---:|---:|
| real skeletons with their own 3c (counts) | 21.6 | 34.5 | 32.9 | 89 | 89 |
| real skeletons with their own 3c | 24% | 39% | 37% | 89 | 89 |
| of them, DougCube's | 31% | 38% | 31% | 23 | 23 |
| of them, everybody else's | 22% | 39% | 39% | 66 | 66 |
| the real move sequences with a random 3c | 35% | 34% | 31% | 6,000 | 5,929 |
| random sequences of the same lengths with a random 3c | 35% | 34% | 31% | 6,000 | 5,951 |

- On the 89 real 3c skeletons the best spot is in the first third less often than in the other two, and not more often near the two ends. 23 of them are DougCube's own (56 of the 201 examples are DougCube's). The split by thirds:

  | Skeletons | First third | Middle third | Last third |
  |---|---:|---:|---:|
  | a random 3c on the same move sequences | 35% | 34% | 31% |
  | DougCube's own | 31% | 38% | 31% |
  | the other 66 | 22% | 39% | 39% |

  The first row is the split of random sequences of the same lengths (the first third has a spot more than the others at the lengths where the spots don't split evenly).
- So "first 1/3 or last 1/3" ([8 Jul 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1524584097085657221)) isn't reproduced: not on random skeletons, not on the real ones, not on DougCube's own. It isn't refuted either. DougCube's stats count the insertions they found, of every kind, in solves where the ends are searched first (8.1); this counts where the best 8-mover for a 3c is. And 23 skeletons are few.

### 9.5 Insertion Finder

Insertion Finder is at [333.fm/if](https://333.fm/if). Baiqiang ([5 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181810277851865108)): "i make the website 333.fm. the core is written by Yan Xuan". 10 Insertion Finder result pages were posted on the server with their scramble and skeleton. 6 of them have corners and edges or parity left, which I don't search. The other 4, one row per page with the final length each gives:

| Insertion Finder page | Skeleton | Insertion Finder, moves | This search, cap 8, moves | Cap 10, moves | Cap 12, moves |
|---|---|---:|---:|---:|---:|
| [18 to 3C1T](https://333.fm/if/46dd6eb9c2669d9c0d770207ecc5e5b0) | 18 moves | 29 | 29 | 29 | 29 |
| [16 to 3C1T](https://333.fm/if/eba5f143ce0414ced5eb524a445d7f6d) | 16 moves | 25 | 27 | 25 | 24 |
| [13 to 3T](https://333.fm/if/6968e0c626f3158f3d21e2c9a8461fc1) | 13 moves | 23 | 23 | 23 | 22 |
| [11 to 5C](https://333.fm/if/476b748820bc0d4a723d9dac042ecd67) | 11 moves | 19 | 24 | 23 | 19 |

What the search inserted for those lengths, page by page:

| Insertion Finder page | Cap 8: what was inserted | Cap 10: what was inserted | Cap 12: what was inserted |
|---|---|---|---|
| 18 to 3C1T | two comms | two comms | two comms |
| 16 to 3C1T | two comms | a comm plus an alg | a comm plus an alg |
| 13 to 3T | two comms | two comms | two comms |
| 11 to 5C | two comms | two comms | a comm plus an alg |

- **Where Insertion Finder used only 8-movers, cap 8 gives the same**: 29 on the 18-move 3C1T (Insertion Finder: 29), 23 on the 3T (Insertion Finder, run with its "3 Corners" set only: 23).
- **16 to 3C1T**: Insertion Finder's 25 is an 8-5 and a 10-move double swap. Two 8-movers give 27; a comm plus an alg gives 25 at cap 10 and 24 at cap 12.

  ```
  L2 F2 B2 R2 U R2 F2 B2 L2 D   // the double swap Insertion Finder used (10-4)
  ```

- **11 to 5C**: its 19 is an 8-5 and triple sexy. That's a comm plus an alg at cap 12, and the search finds 19 there. Two comms give 24 at cap 8 and 23 at cap 10.

  ```
  B' U' B U B' U' B U B' U' B U   // triple sexy (12-7)
  ```

- So the search is never worse than Insertion Finder once its cap covers the algs Insertion Finder used, and at cap 12 it is one move shorter on two pages (16 to 3C1T: 24 against 25; 13 to 3T: 22 against 23). As it should be: Insertion Finder works from lists of known algs, and here every sequence within the cap counts.

The pages that are not compared, with Insertion Finder's final length:

| Insertion Finder page | Skeleton | Insertion Finder, moves | Why it is not compared |
|---|---|---:|---|
| [11 to 5C3E](https://333.fm/if/ecd00cdacaf79153d38d420319fa5623) | 11 moves | 22 | corners and edges both left |
| [11 to 2C2E](https://333.fm/if/731052d4eb815222020c8362d3584ec4) | 11 moves | 20 | a parity leftover (two corners and two edges) |
| [6 to 3C2T2E2E](https://333.fm/if/88a6f1de5bd9b8374fe6f57dd55a336d) | 6 moves | 18 | corners and edges both left |
| [6 to 3C2T2E2E](https://333.fm/if/899b2cd15cbe1133c8ab58fd53847dfa) | 6 moves | 18 | corners and edges both left |
| [12 to 2T3E](https://333.fm/if/d426a5276f2de3b3a4c72b4beba3fe8c) | 12 moves | 20 | corners and edges both left |
| [2 to 2C3C2T2E3E](https://333.fm/if/70bac280633de27ecf6b8a8ccceb5726) | 2 moves | 20 | corners and edges both left |

**The insertion both miss.** alkamaass ([4 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181359853491462185), [4 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181360036946137188)) took the 18-move 3C1T skeleton, put in an 8-move comm that cancels 10 moves ("take that but with the 8-10"), and got a 16-move skeleton that still leaves a 3c1t. Insertion Finder gives 25 on that one and 29 on the original: "it missed 4 moves LMAO". Baiqiang ([5 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181804907922198529)): "IF supposed that the status of the cube becomes better after any insertion. so it won't work in this case". And twenty minutes later, having asked Yan Xuan ([5 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181810401919381534)): "this should be supported but somehow it doesn't". My search has the same limit. The comm doesn't bring the leftover any closer to solved, it makes the skeleton shorter, and then two more insertions finish. That's three insertions, and every model here stops at two. Such lines exist; I don't know how often.

On the 16-move skeleton that the 8-10 leaves, a comm plus an alg of up to 12 moves gives 24:

```
R' U' F U2 L2 F2 D' R2 B2 L2 D' F2 L U' L' F R' F2 R' F L2 U F R' U' F   // scramble
D B2 D2 R2 D B L' D' R' L B' L F2 B2 L U                                 // skeleton (16)
```

It leaves a twisted corner 3-cycle and one twisted corner: UBL → DFR → UBR → UBL, DBR twisted clockwise.

**A comm plus an alg, each of up to 12 moves**: 24 in all.

```
D B2 D2 R2 ^ D B * L' D' R' L B' L F2 B2 L U
* = R U2 R' L' D' R L U2 R' L' D L // (12-7/21)
^ = R2 D2 B2 D' F D B2 D' F' D' R2 // (11-8/24)
Solution: F D B2 D' F' D' R2 D B R U2 R' L' D' R L U2 R2 B' L F2 B2 L U (24)
```

**What an Insertion Finder "optimal" covers.** 2014chri04 ([16 Oct 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1296311051121463346)), on an 8-4 for a 23-move 3c: "IF verifies that this is optimal". tseitsei89 ([24 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1254714471423676456)), on two comms found by hand for a 21-move 5c: "IF says those are optimal insertions." Both report what Insertion Finder returned, with settings that aren't stated, and neither says the result is the best possible: 2014chri04 goes on to a 22 found by hand, and tseitsei89 had written ([24 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1254712833237844018)) "there might be somethng even better". Searched here:

| Skeleton | Cap 8: best final length, moves | Cap 10: best final length, moves |
|---|---:|---:|
| first: the 8-4 is the best 8-mover insertion | 27 | 23 |
| second: the two comms are the best pair | 32 | 30 |

2014chri04's own 22 on the first, by rewriting a stretch of the finished solution, is shorter still. So the word means optimal for the alg sets that were on. Baiqiang on the two corner sets ([21 Aug 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1407986882700382259)): "Pure 3 corners includes 8 moves comms only. The other one includes some 10 moves". The first skeleton (both are on the examples page):

```
R' U' F U2 F2 D2 F2 L' B2 L D2 B2 L B2 R U' L' D' B D2 U' L R B' R' U' F   // scramble
U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' L' D L D' B D B'               // skeleton (23)
```

It leaves a corner 3-cycle: DBL → UBL → DFR → DBL.

**Best with 8-movers**: 27 in all, the 8-4 that was posted.

```
U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' L' D * L D' B D B'
* = D' L D R D' L' D R' // (8-4/27)
Solution: U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' D R D' L' D R' L D' B D B' (27)
```

**Best with one alg of up to 10 moves**: 23 in all, a 10-mover that cancels all ten of its moves.

```
U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' L' D L D' * B D B'
* = D L' D' L F L' D L D' F' // (10-10/23)
Solution: U' L2 B2 U' L F D' L2 D' F' D F2 B D2 B' L' D L D' F' B D B' (23)
```

The solution 2014chri04 then found by hand, by rewriting a stretch of the finished one (22 moves, solves the scramble):

```
U' L2 B2 U' L F D' L2 D' F' D F2 B D B R' B' R D F' D B'   // 2014chri04's 22, by hand
```

**Insertion Finder results quoted in the channels.** 14 more examples in the notes give an Insertion Finder result with a scramble and a skeleton that could be replayed (6 of them are called Insertion Finder results only by the wording of the message).

| Compared with the best at | Solutions | Author shorter | Same length | Author 1 move longer | Author 2 longer | Author 3 or more longer | Author, mean added | Best, mean added |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| cap 8: one comm or two (edges: algs of 6 to 8) | 14 | 5 | 8 | 1 | 0 | 0 | 7.64 | 8.43 |
| cap 10: one comm, two comms or one alg | 14 | 4 | 9 | 1 | 0 | 0 | 7.64 | 8.29 |
| cap 12: one comm, two comms or one alg | 14 | 3 | 8 | 1 | 0 | 2 | 7.64 | 7.79 |
| cap 10, a comm plus an alg also allowed | 14 | 2 | 9 | 0 | 2 | 1 | 7.64 | 7.50 |
| cap 12, a comm plus an alg also allowed | 14 | 0 | 7 | 4 | 1 | 2 | 7.64 | 6.79 |

At cap 8 the search is never better than Insertion Finder by more than a move, and Insertion Finder is ahead on 5, where it used a longer alg. At cap 12 with a comm plus an alg the search is ahead on 7 of 14. The settings of those Insertion Finder runs mostly aren't stated, so this says what the alg list is worth, not that either tool is wrong.

---

## 10. The claims, checked

Everything people said that the numbers can settle, by theme. A verdict is only as strong as what I measured: the samples are random skeletons unless the row says real ones, and *8-movers* is cap 8. Where the numbers go against a statement, or a statement says something exists, there's an example written out, under the tables or in the section named (letters in brackets).

**What a type costs**, one claim per row:

| Claim | Who | Verdict |
|---|---|---|
| The table: 3c 5/6, 2 twisted 8, 3 twisted 9, double swap 9/10, 3c1t 10, 5c 10/11 | Tronto's tutorial, 2.4.10 | **Every corner row is within about half a move**, the 3tc the full half. 8-movers on 20-move random skeletons: 5.90, 7.71, 9.50, 9.13, 9.90, 10.37. The twisted double swap, which has no row, is 8.73. The skeletons people posted come out cheaper, and selection is part of that (section 9). |
| Edge 3-cycle 7 | Tronto's tutorial, 2.4.10 | **Depends on the alg list**, as its footnote says. Random skeletons: 6.05 with every alg up to 10; with 8 or fewer nothing fits on 44% of them. |
| "a optimal 3c skeleton's insertion is 6 moves on average"; "3c on average gives ~ +6"; "3C insertions are usually +6 moves" | Aneurin [8 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1127188448462258266); Eli Rogers [9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414943185569845381); Jay [29 May 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1112910413688995890) | **True**: 5.90 at 20 moves, 6.08 at 16, 5.68 at 26. |
| "5c is 10-11 moves."; "5c ~high 10" | Aneurin [8 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1127188481563693068); Phuwish [4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239470932131973) | **True**: 10.65 at 16 moves, 10.37 at 20. |
| 2tc with two insertions: "~8.0 I guess" | Phuwish [4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424237318960709642) | **True**: 8.06 at 16 moves, 7.71 at 20. |
| 3tc: "mid to high 8", "a half to a move worse" than a 2tc | Phuwish [4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239016290553917) | **Higher with pure comms**: 9.50 at 20 moves, 1.79 worse than a 2tc. With algs up to 12 it is 8.56 (100 skeletons), so the alg list can explain the figure. |
| "more like 9 for pure 2-2", "like 9.5 for 2-2 with a twist", "like 10 for 3c1t" | cpaul [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760547458842644), [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760556908740648), [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760590995853465) | **9 and 10 are right** (9.13, 9.90). **Which 2c2c is cheaper depends on the alg length**: with 8-movers the twisted one (8.73); with algs up to 10 the pure one (8.48 against 8.66, 500 skeletons each), which is cpaul's order. |
| "5-6, 8-9, 6-8 for good 2c2c, 8-9 for bad 2c2c"; "this is i expected not avg expected" | Baiqiang [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443756810715664537), [28 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443860338440146986) | **Not averages, in Baiqiang's words.** Which 2c2c is the good one was asked (kyh, [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443757686025093241)) and not answered. With algs up to 12 on 100 random 20-move skeletons each: pure 2c2c 7.87, twisted 8.30, 3c1t 9.44. Posted skeletons with a comm plus an alg at cap 12: 2c2c 6.85, 3c1t 7.65 (9.2). |
| "i think 3c1t > 2c2c > 5c" | argonblue [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125544114131034) | **By cost the first two are the other way round**: 2c2c, then 3c1t, then 5c. A 2c2c is 0.77 to 1.17 cheaper than a 3c1t [a]. |
| "i didn't notice a meaningful different between 2 insertion 4c types" | Jay [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443789835356606609) | **There is one on average**: about a move between a 2c2c and a 3c1t, with a spread from skeleton to skeleton that is wider than that, so it is hard to notice solve by solve [a]. |
| "maybe there's some non 3c type insertion method for 2c2c that lowers the movecount that far" | Jay [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443789835356606609) | **There is**: the 10-move 2c2c algs. A pure 2c2c averages 8.48 with algs of up to 10 moves (500 skeletons) and 7.87 up to 12 (100), against 9.13 with 8-movers. |
| "Why is there even a difference if the number of possible first insertions is the same tbh" | wen [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443790851443785758), asking | **Answered both ways it can be read.** The two kinds of 2c2c: the number is the same, 24 first comms per spot each, and they cost the same when the two comms do not touch (9.41 and 9.40); the 0.40 between them comes from comms that interact, 0.25 of it from nesting. A 2c2c against a 3c1t or a 5c: the number is not the same, 24 against 9 against 5 (6.2). |
| "getting +9 from 2tc is as bad as +11,+12 from 5c" | Phuwish [4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424238456275730556) | **About right**: +9 or worse on 26% of 2tc skeletons, +12 or worse on 16% of 5c skeletons. |
| For two corner insertions "the average is 13 moves for me, one 8-2 and one 8-1"; "you can usually do a bit better with 5c" | Zagros [1 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246424587554783313); Java [1 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246425063641579541) | **Java is right**: the best is 10.37 on average, and +13 or worse is the best there is on only 1.3% of 20-move 5c skeletons. |
| "8-4 8-4 is soooooooo lucky tho", "for a 15 move skeleton" | alkamaass [1 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246494760366112789), [1 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246494791827591292) | **Yes**: +8 or better on 4.3% of 14-move and 5.4% of 16-move 5c skeletons. |

**Which skeleton**, one claim per row:

| Claim | Who | Verdict |
|---|---|---|
| A 5c should be "maybe like 5-6" shorter than a 3c | asacuber [5 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1247972799151341690) | **5 is break-even**: 4.8 against a 20-move 3c by expected total, 4.0 to 5.1 for equal chance of a target (7.2). |
| 3c in 23: sub-30 "you will probably get it"; in 25 "you will need some luck" | Tronto's tutorial, 2.4.10 | **Right**: 76% and 12%. |
| "a skeleton leaving 4 corner in 18 moves is probably better than one leaving 3 corners in 25" | Tronto's tutorial, 2.4.10 | **Right, by about 2.7 moves or more** in expected total. |
| "3c in 22-24 or 5c in 16-18"; "18 to anything like 5c, 4c, 3c1t, and 24 for 3c" | Gezza Cubing [18 Aug 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1274622450046603284); oliynykmax [18 Aug 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1274622638806925372) | **The 5c end is the better one**: sub-30 from a 5c in 18 80%, from a 3c in 24 34%. |
| "sub-22 for 3C skeleton", "sub-20 for every other skeleton" | sequesteredcuber [8 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1127188954995769364) | **Uneven**: sub-30 from a 3c in 21 99.6%, from a 5c in 19 48%, from a pure 2c2c in 19 87% [g]. |
| 21 to 3c: "a guaranteed 29 right?"; "not strictly guaranteed", "but it's very likely" | 2023HAMI08 [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443620873839051034); kyh [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443621022745235476), [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443621113996513372) | **kyh is right**: 99.6% with 8-movers [h]. |
| For sub-35: "get to 3c in 28 or 4c/5c in 22" | trangium [15 May 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1504709818521354241) | **Both work; the 5c in 22 is the safer**: 99% against 83%. |
| "the chance ur cancelling 4 moves or more is not that high" | kyh [9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414840422177570836) | **True**: 11% of 24-move 3c skeletons. |

**Cancelling and searching**, one claim per row:

| Claim | Who | Verdict |
|---|---|---|
| "8 move commutators cancel less moves on average on DR skeletons compared to regular ones, although we don’t think this has been proved yet"; "after DR you often get something like 8-1" | Fokianos and Raposio's DR guide, 5.1; trig0n [16 Jun 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1119294685928763403) | **A little, in a model**: on modelled 17-move DR skeletons a 3c costs 6.18 with 8-movers against 6.02 on random ones, because of which corners a DR leaves (6.1). Real DR skeletons were not sampled. |
| "usually you should at least be able to cancel like 2 moves for each comm" | Gezza Cubing [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253277567209963522) | **True for a 3c**: 8-2 or better on 71% of 20-move skeletons. |
| "In my stats, I found that the best insertion points tend to be in the first 1/3 or last 1/3 of the skel." | DougCube [8 Jul 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1524584097085657221) | **Not reproduced**: not on random skeletons (a third each, 8.1), not on the 89 posted 3c skeletons (first third 24%, middle 39%, last 37%), and not on the 23 of those that are DougCube's own (31%, 38%, 31%; 9.4). Not refuted either: DougCube's stats count the insertions DougCube found, of every kind, which is a different count. |
| Near either end "you have less chances to find a 8-6 or better" | paulduc03 [9 Jul 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1524669961338097684) | **True for the first and last spot**, and a little for the next one in (8.1). |
| "It happens extremely rarely that the best insertion is given by a 9 move commutator (or longer)" | Tronto's tutorial, 2.4.1 | **Right for 9-movers** (the best on 0.61% of 20-move skeletons). **A 10-mover is the only best on 4.7%** [b], by a single move 77% of the time. |
| "if its a setup to a regular comm then it wont cancel more than just inserting 8 movers" | Ben [25 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1465081370131959961) | **True on all but 0.43% of 20-move skeletons.** Where the setup cancels a whole move it is the 8-mover one spot over. On 86 of 20,000 skeletons a setup-type 10-mover is the only best, by one move: its setup joins a turn of the skeleton, which is the 8-mover put inside that turn [i]. |
| Checking every other move "still guarantees you'll find" a -3 or better; "this isn't thorough tho" | notkevin [7 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1436457200880189582); alkamaass [31 May 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246266143551787058) | **Almost**: a best of 8-3 or better is found 97% of the time on a 20-move 3c. Those misses are all next to two opposite-face moves [c]. Nothing better than an 8-4 was missed on any of 140,000 skeletons. |
| Every third spot instead of every other | tested here | **It does not work**: an 8-3 or better is found 75% of the time on a 20-move 3c [j]. |
| When the case at a spot needs 10 moves, "can I go 3 moves further instead of 2 and still make sur not to miss any insertion below 6 moves ?"; "I don't think that works." | paulduc03 [30 Dec 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1455642235449114665), asking; DougCube [30 Dec 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1455657733272633651) | **DougCube is right**: two spots on from such a spot there is an 8-3 or better 1.7% of the time on a 20-move 3c, and all 80 cases that need 10 moves can have an 8-mover two moves later [k]. |
| "for the first 5c insertion you have 5x more options than for the second"; "there are 5 possible cycles, not 1" | Not officially a David [21 Apr 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1098919767429099570); Zagros [16 Aug 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1406274793552220182) | **True**: 5 3-cycles per spot leave a 3c. ✓ Lean |
| For a 5c "you'll probably have at least an 8-3 or 8-4 for the first one" | Ben [31 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1467098844712931498) | **Yes for an 8-3**: there on 80% of 20-move 5c skeletons and 71% of 16-move ones. An 8-4 or better: 37% and 31% (8.4). |
| "my pr single wouldve been a 30 if i didnt go look for sub optimal first insertions", "but its a 28"; "i just had to check a suboptimal first insertion (8-2 instead of 8-3) to get any cancellations in the second" | kyh [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486867754354086093), [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486867787023515738); argonblue [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486868609656688780) | **True**: on a 20-move 5c, the best first comm followed by the best second misses the best pair on 14% of skeletons (8.4) [f]. |
| "if you set greedy to 0 and only pick regular 3c comms then it basically shows human findable"; "greedy 1 is still reasonable if your skeleton is really good but anything higher isn't imo"; "i think 1 is realistic" | Ben [26 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1476513726097129576), [26 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1476514406320963629); kyh [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486867581557280848) | **What the settings give**, with pure comms on a 20-move 5c: 10.54 at greedy 0 (longer than the best pair on 14% of skeletons), 10.41 at greedy 1 (3.7%), 10.37 for the best pair. What is findable is not measured. |
| With more algs at greedy 0 Insertion Finder gives a worse result; "if 10-5 is the best first insertion it won’t find the optimals with a worse first insertion" | bvcuber13 [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486828825756307620), [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486829034905014303); tave_789 [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486829396286246952); Ben [24 Sep 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1552577949688008734) | **It can happen, and it is uncommon**: on 1,998 random 20-move 5c skeletons, greedy 0 with every 3c alg of up to 10 moves is longer than greedy 0 with 8-movers on 0.25% and shorter on 9.3% [l]. tave_789's line is the reason: in each of those the longer list has a better first comm, and it is the wrong one to follow. |
| An insertion can cancel more than its own length | Zagros [17 Aug 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1406775061276524564); DougCube [17 Aug 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1406775022168838214) "true but highly unlikely" | **True, and rare**: the best 8-mover insertion shortens the skeleton on 0.03% of 20-move 3c skeletons [d]. |
| "i thought it wasn't possible to nest 3c comms that are parts of a 5-cycle, but insertion finder apparently did it for one of my skeletons (improving it by 1 move)?" | argonblue [27 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1465819786910109828) | **What argonblue found is common**: the best pair is nested on 24% of 20-move 5c skeletons with 8-movers [e]. |
| "IF supposed that the status of the cube becomes better after any insertion. so it won't work in this case"; then, having asked Yan Xuan, "this should be supported but somehow it doesn't" | Baiqiang [5 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181804907922198529), [5 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181810401919381534) | **This search has the same limit.** alkamaass's 8-move comm that turns an 18-move 3c1t into a 16-move 3c1t is a third insertion, outside both (9.5). |

**Algs and counts** (sections 4 and 5), one claim per row:

| Claim | Who | Verdict |
|---|---|---|
| Which leftovers take one, two or more comms | Riabov's guide; Tronto's tutorial 2.4.4, 2.4.5 | **All right**, proved in Lean (section 4). |
| "the only way to affect 5 corners with 2 3-cycles, is to do a 5-cycle" | FakeMMAP [9 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1459235380166525029) | **True.** |
| A mixed 3c3c "cannot be solved with only two 3c comms" | DougCube [9 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1459256777555185872) | **True**, it takes three. |
| "theres 4 types of 7c that work"; "I counted your last one as 2 separate" | wen [29 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1134857937907613789), [29 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1134860037613957220), to torchlight's list of three [29 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1134858381644025927) | **True**, counted wen's way: exactly four leftovers on seven corners take three comms. |
| "for most 3c cases theres 2 ways to do the commutator"; "about half of the 8 movers you can do 2 ways" | Gezza Cubing [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253275920970551347), [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253278252026564668) | **336 have two, 192 have one, 480 have none.** |
| "i feel like every 8 mover has two ways no"; "no", "U2, R' D R doesn't for example" | eff [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253302165154304010), asking; rogo [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253304211752484905), [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253304286931062805) | **rogo is right**: `[U2, R' D R]` is one of the 192 with a single 8-mover. |
| "There arent 8 movers if they're oriented" | Zagros [26 Apr 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1365885825166082088) | **Mostly**: 32 of the 112 oriented 3-cycles have one. Jay's `R' F' R B2 R' F R B2` ([26 Apr 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1365886921221341216)) is one of them. ✓ Lean |
| A case where no single move gives a pure comm, "so you can skip one move from it" | Srećko [9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414947538515005494) | **True** for 112 of the 1,008 3-cycles. ✓ Lean |
| "optimal to twist one corner while preserving all edges is 12 moves" | torchlight [27 Aug 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1145356913731715073) | **True as stated**: no sequence of 11 moves or fewer that keeps every edge leaves a corner twisted in its place, whatever else it does; 4,464 sequences of 12 moves do (section 5). |
| "what's the shortest 2c2c alg", "I think it’s 10?" | kyh [29 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1399733098836394074), zakk drewji [29 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1399740709698801775) | **10**, for a pure 2c2c. 12 for a twisted one. |
| "10 moves is the minimum for any 2E2C without cancellations" | Noah Swor [15 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1394725607153209354) | **True.** |
| "every 10-move 2e2c is a cyclic shift of this alg or its inverse (up to rotations/mirrors ofc)" | notkevin [15 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1394776450522943659) | **True**: 960 sequences, one class. |
| "there’s only 1848 possible 2c2e states", "6x as many cases, because orientations" | argonblue [9 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1536138775816704062), [9 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1536141220403748894) | **True**: 11,088. |

The examples:

**[a]** A typical skeleton of each of the three 4-corner types, 20 moves, 8-movers: each costs what its type costs on average, rounded. They're there to show what the averages look like on a cube. One skeleton of each proves nothing about the order; the tables of 6.2 do that.

```
R' U' F L B2 L B2 F2 U2 L B2 U2 B2 R' D2 F' R B' U2 F R2 U' R U R' U' F   // scramble
U' R2 F2 D' R' D' B R' U2 B' L' U F L' D2 B D2 R2 B' R2                   // skeleton (20)
```

It leaves two corner swaps, each with a twist: DFL ↔ UFR, DBR ↔ DFR.

**Best with two 8-move comms**: 29 in all.

```
U' R2 F2 D' R' D' B R' U2 B' L' U F L' D2 * B D2 R2 B' R2
* = U' B D' B' U B D B' // (8-3/25)
U' R2 F2 D' R' D' B R' U2 B' L' U F L' U' D2 B D' ^ B' U B D' R2 B' R2
^ = D B U2 B' D' B U2 B' // (8-4/29)
Solution: U' R2 F2 D' R' D' B R' U2 B' L' U F L' U' D2 B2 U2 B' D' B U2 B2 U B D' R2 B' R2 (29)
```

```
R' U' F B2 U2 L2 B2 L2 D' L2 D B2 D2 F2 U2 L R2 U' B' D' L B F R2 D R' U' F   // scramble
U' D2 B' D2 B' D L2 U R2 B' U2 D B L D B' U2 L' D' L'                         // skeleton (20)
```

It leaves two corner swaps, no twist: DFL ↔ DFR, DBR ↔ UFR.

**Best with two 8-move comms**: 29 in all.

```
U' D2 B' D2 B' D L2 U R2 B' U2 ^ D B L D * B' U2 L' D' L'
* = D F2 D' B' D F2 D' B // (8-3/25)
^ = F' D B D' F D B' D' // (8-4/29)
Solution: U' D2 B' D2 B' D L2 U R2 B' U2 F' D B D' F D L D2 F2 D' B' D F2 U2 D' L' D' L' (29)
```

```
R' U' F B2 L F2 L' D2 R' F2 U2 R2 U2 L F2 R' U' L F R' U2 B' R D2 L U' R' U' F   // scramble
L' B' D2 R D R' B' R2 U2 F R2 U2 D' L2 F2 U' L' D2 B2 U'                         // skeleton (20)
```

It leaves a twisted corner 3-cycle and one twisted corner: DFL → UFL → UBR → DFL, DBL twisted clockwise.

**Best with two 8-move comms**: 30 in all.

```
L' B' D2 R D R' B' R2 U2 F R2 U2 D' L2 F2 * U' L' D2 B2 U'
* = F D' F' U' F D F' U // (8-3/25)
L' B' D2 R D R' B' R2 U2 F R2 U2 D' L2 F' D' F' U' ^ F D F' L' D2 B2 U'
^ = U F' U' B U F U' B' // (8-3/30)
Solution: L' B' D2 R D R' B' R2 U2 F R2 U2 D' L2 F' D' F2 U' B U F U' F B' D F' L' D2 B2 U' (30)
```

**[b]** A 10-mover that beats every 8-mover and every 9-mover:

```
R' U' F U' D R2 F2 U L2 U B2 U2 R2 D' B' D L2 F U R' D' L U2 R D' R' U' F   // scramble
F D' R' D F' L2 B2 R U F' U2 D' B' R' D2 F L2 U' B2 U                       // skeleton (20)
```

It leaves a corner 3-cycle: UBL → DBR → UFL → UBL.

**Best with 8-movers**: 26 in all.

```
F D' R' D F' L2 B2 R U F' U2 D' B' * R' D2 F L2 U' B2 U
* = B' L' B R2 B' L B R2 // (8-2/26)
Solution: F D' R' D F' L2 B2 R U F' U2 D' B2 L' B R2 B' L B R D2 F L2 U' B2 U (26)
```

**Best with algs up to 10**: 25 in all, a 10-mover; no 9-mover does better than the 8-movers here.

```
F D' * R' D F' L2 B2 R U F' U2 D' B' R' D2 F L2 U' B2 U
* = D F' D' F R F' D F D' R' // (10-5/25)
Solution: D' F R F' D F D' R2 D F' L2 B2 R U F' U2 D' B' R' D2 F L2 U' B2 U (25)
```

**[c]** is the skeleton of 8.3 where every other move misses the only 8-3.

**[d]** An 8-move comm that makes the skeleton shorter:

```
R' U' F U' F D2 B' L2 R2 B L2 D2 U2 F D2 L R2 F2 R2 D R' F2 U' F2 U R' U' F   // scramble
U2 B U' R D2 F2 L D R' B' L B R' D' L F B2 D' L D'                            // skeleton (20)
```

It leaves a corner 3-cycle: UBL → UFL → DFR → UBL.

**The best 8-mover insertion**: 19 in all, 20 moves before, 19 after.

```
U2 B U' R D2 F2 L D R' B' L B R' * D' L F B2 D' L D'
* = R B' L' B R' B' L B // (8-9/19)
Solution: U2 B U' R D2 F2 L D R2 B' L B D' L F B2 D' L D' (19)
```

**[e]** A 5c whose best pair of comms is nested:

```
R' U' F B2 R F2 L' B2 R D2 B2 D2 B2 D2 L2 F' U' R' B' L' D' R2 U' R' U' F   // scramble
L' D' R F U' L2 U R2 F U' B D' L D F' D' B D' B2 R2                         // skeleton (20)
```

It leaves a corner 5-cycle: DBL → UBL → DBR → DFR → UFL → DBL.

**Best with two 8-move comms**: 29 in all, the second inside the first.

```
L' D' R F U' L2 U * R2 F U' B D' L D F' D' B D' B2 R2
* = D' L' D R2 D' L D R2 // (8-2/26)
L' D' R F U' L2 U D' L' ^ D R2 D' L D F U' B D' L D F' D' B D' B2 R2
^ = L U' L' D2 L U L' D2 // (8-5/29)
Solution: L' D' R F U' L2 D' L' D2 L U L' D' R2 D' L D F U' B D' L D F' D' B D' B2 R2 (29)
```

**Best without nesting**: 31 in all.

```
L' D' R F U' L2 ^ U * R2 F U' B D' L D F' D' B D' B2 R2
* = D' L' D R2 D' L D R2 // (8-2/26)
^ = L' D L U L' D' L U' // (8-3/31)
Solution: L' D' R F U' L D L U L' D' L D' L' D R2 D' L D F U' B D' L D F' D' B D' B2 R2 (31)
```

**[f]** is the skeleton of 8.4 where the best first comm is the wrong one to follow.

**[g]** is the 19-move 5c of 7.3 that gives 30, and **[h]** the 21-move 3c of 7.3 that does not give 29.

**[i]** is the skeleton of 8.2 where a setup-type 10-mover is the only best.

**[j]** and **[k]** are the skeletons of 8.3 where every third spot, and three spots on after a 10-move case, miss the only 8-3.

**[l]** is the skeleton of 8.4 where greedy 0 gives a longer result with more algs.

✓ Lean for [a] to [e] and [g] to [k]: every block replays as printed, and the best each states is exact over every alg of 8 moves or fewer, and of 10 or fewer where it says so. [f] and [l] are computed.

---

## 11. What this does not cover

- **Findability and time.** Every number is the best insertion that exists for its cap, the answer key. How often you find it in the time left isn't measured anywhere here. What people say about time: Tronto, "A single 3c insertion usually takes me about 5 minutes"; DougCube ([7 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414429451470766183)): "I find 3c in under 3 mins and 5c in under 10 mins now."
- **Random skeletons are move sequences, not solves.** No blocks, no EO, no last-layer alg at the end. The same real move sequences with a random leftover on them cost what random sequences cost, but the skeletons people post come out most of a move cheaper with 8-movers. Selection is part of that, and how much of the rest is real these skeletons can't say (9.2). The posted 3e skeletons are far cheaper than the random tables, and how their edges are oriented doesn't explain it.
- **Small samples at the long caps.**

  | Model | Sample |
  |---|---|
  | two comms at cap 10 | 200 to 2,000 skeletons per length |
  | a comm plus an alg | 200 skeletons of 20 moves |
  | two comms at cap 12 | 100 |

  Two standard errors of a mean are ±0.06 for a 5c at cap 10 and ±0.26 at cap 12 (Appendix C). Enough for a mean, not for the rare outcomes.
- **Parity and mixed leftovers.** 2c2e, 3e3c, 2e2e with corners, and everything else with both corners and edges left, are not sampled. Their algs are only counted for 2c2e (section 5).
- **Leftovers that need three comms** (2c2c1t, 3c2t, 7c and the rest of section 4): counted, not costed.
- **More than two insertions on a two-comm leftover.** A comm that leaves the same kind of leftover but shortens the skeleton, like the 8-10 of section 9.5, is a third insertion and isn't searched.
- **Spots inside a pair of opposite-face moves.** A skeleton is searched as it is written, with `U D` never also tried as `D U`, so the spot between the two moves the other way round isn't looked at. A recount that tries both orders finds a better 8-mover result on 76 of 20,000 random 3c skeletons of 20 moves (74 by one move, 2 where nothing fitted before) and on 8 of 2,000 5c skeletons, which moves the 3c average from 5.902 to 5.899. That recount is a separate program; as written, it gives the study's cap-8 value on every one of the 370,000 skeletons it reran. The every-other-move rule misses exactly this kind of spot (8.3). One of the 76, where the skeleton as written gets a 28 and `U' D` written `D U'` gets a 27:

      B2 D2 B' U' D L' U' B L' U' R2 B' U' L D2 F L F' L' U    // 3c skeleton, 20 moves; best 8-mover as written: 28
      B2 D2 B' D * U' L' U' B L' U' R2 B' U' L D2 F L F' L' U  // the pair written D U'
      * = L2 U R U' L2 U R' U'                                 // one move cancels: 27
- **Insertions inside a turn.** Every spot searched is between two moves of the skeleton. An alg put in the middle of a turn (a `B'` done as `B2`, the comm, `B`) is found only when a longer alg within the cap happens to equal it (8.2).
- **Algs longer than 12 moves**, so no 3tc alg and no two-twist of neighbouring corners in one piece, and the 13-move algs people do insert.
- **Slice insertions, centre insertions, real DR skeletons.** The DR rows of 6.1 are modelled move sequences. Whether 8-move comms cancel less on skeletons from real DR solves, the question in the Fokianos and Raposio guide, is answered here only for that model.

---

## Appendix A: every type and length

The full tables behind section 6: every even skeleton length from 10 to 30, every type, random skeletons. The first column is the cap and what was inserted. Rows at caps 10 and 12, and the comm-plus-alg rows, are **computer only** (every alg of that length); the cap-8 rows are best pairs of 8-movers, which a hand search following the first comms a move worse gets close to (8.4):

- *one comm*: one 3-cycle alg (3c and 3e only);
- *two comms*: two 3-cycle algs, nesting allowed;
- *one alg*: one alg for the whole leftover;
- *best of the two*: the shorter of two comms and one alg on each skeleton, over the skeletons where two comms was run.

A block is left out when nothing of that length exists (no alg of 8 or fewer does a 5c, and so on). The *Skeletons* column is the size of the sample behind each row. *Mean moves added* is over the skeletons where something fits; the *Adds k or less* shares are of all skeletons. Each table below is one leftover, one row per cap, model and skeleton length.

**3c**: one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 2 or less | Adds 3 or less | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, one comm | 10 | 20,000 | 6.44 | 0.37% | 1.2% | 4.6% | 15% | 46% | 82% | 96% | 4.2% |
| 8, one comm | 12 | 20,000 | 6.30 | 0.37% | 1.4% | 5.5% | 19% | 53% | 87% | 97% | 2.5% |
| 8, one comm | 14 | 20,000 | 6.20 | 0.47% | 1.6% | 6.4% | 21% | 58% | 89% | 98% | 1.7% |
| 8, one comm | 16 | 20,000 | 6.08 | 0.63% | 2.0% | 7.7% | 24% | 63% | 92% | 99% | 1.2% |
| 8, one comm | 18 | 20,000 | 5.98 | 0.72% | 2.5% | 8.5% | 27% | 67% | 94% | 99.4% | 0.65% |
| 8, one comm | 20 | 20,000 | 5.90 | 0.73% | 2.7% | 9.3% | 29% | 71% | 96% | 99.6% | 0.36% |
| 8, one comm | 22 | 20,000 | 5.82 | 0.69% | 2.7% | 10% | 32% | 75% | 97% | 99.8% | 0.24% |
| 8, one comm | 24 | 20,000 | 5.74 | 0.89% | 3.2% | 11% | 34% | 77% | 98% | 99.8% | 0.16% |
| 8, one comm | 26 | 20,000 | 5.68 | 0.96% | 3.3% | 12% | 37% | 80% | 98% | 99.9% | 0.08% |
| 8, one comm | 28 | 20,000 | 5.61 | 1.0% | 3.7% | 13% | 39% | 83% | 99% | 99.9% | 0.09% |
| 8, one comm | 30 | 20,000 | 5.56 | 1.0% | 3.7% | 14% | 42% | 84% | 99% | 99.9% | 0.05% |
| 10, one comm | 10 | 20,000 | 6.46 | 0.42% | 1.4% | 5.0% | 16% | 48% | 85% | 98% | <0.01% |
| 10, one comm | 12 | 20,000 | 6.28 | 0.39% | 1.5% | 5.9% | 20% | 55% | 90% | 99% | 0 |
| 10, one comm | 14 | 20,000 | 6.17 | 0.51% | 1.8% | 6.9% | 23% | 60% | 92% | 99.3% | 0 |
| 10, one comm | 16 | 20,000 | 6.04 | 0.72% | 2.3% | 8.4% | 26% | 65% | 94% | 99.6% | 0 |
| 10, one comm | 18 | 20,000 | 5.93 | 0.80% | 2.7% | 9.2% | 29% | 69% | 96% | 99.8% | 0 |
| 10, one comm | 20 | 20,000 | 5.85 | 0.78% | 2.9% | 10% | 31% | 73% | 97% | 99.9% | 0 |
| 10, one comm | 22 | 20,000 | 5.76 | 0.79% | 3.0% | 11% | 34% | 76% | 98% | 99.9% | 0 |
| 10, one comm | 24 | 20,000 | 5.68 | 0.99% | 3.6% | 12% | 37% | 79% | 99% | 99.9% | 0 |
| 10, one comm | 26 | 20,000 | 5.62 | 1.1% | 3.6% | 13% | 39% | 82% | 99% | 99.9% | 0 |
| 10, one comm | 28 | 20,000 | 5.55 | 1.1% | 4.1% | 14% | 42% | 84% | 99.4% | 99.9% | 0 |
| 10, one comm | 30 | 20,000 | 5.50 | 1.1% | 4.1% | 15% | 44% | 86% | 99.4% | 100% | 0 |
| 12, one comm | 10 | 20,000 | 6.40 | 0.47% | 1.5% | 5.5% | 18% | 50% | 86% | 99% | 0 |
| 12, one comm | 12 | 20,000 | 6.21 | 0.49% | 1.8% | 6.7% | 22% | 57% | 91% | 99.3% | 0 |
| 12, one comm | 14 | 20,000 | 6.10 | 0.56% | 2.0% | 7.6% | 25% | 62% | 94% | 99.6% | 0 |
| 12, one comm | 16 | 20,000 | 5.97 | 0.83% | 2.6% | 9.4% | 28% | 67% | 95% | 99.8% | 0 |
| 12, one comm | 18 | 20,000 | 5.85 | 0.90% | 3.0% | 10% | 32% | 72% | 97% | 99.9% | 0 |
| 12, one comm | 20 | 20,000 | 5.77 | 0.93% | 3.4% | 11% | 34% | 75% | 98% | 99.9% | 0 |
| 12, one comm | 22 | 20,000 | 5.68 | 0.98% | 3.5% | 13% | 37% | 79% | 99% | 99.9% | 0 |
| 12, one comm | 24 | 20,000 | 5.60 | 1.2% | 4.1% | 14% | 40% | 81% | 99% | 99.9% | 0 |
| 12, one comm | 26 | 20,000 | 5.53 | 1.3% | 4.3% | 15% | 42% | 84% | 99.3% | 99.9% | 0 |
| 12, one comm | 28 | 20,000 | 5.47 | 1.4% | 4.8% | 16% | 45% | 86% | 99.6% | 100% | 0 |
| 12, one comm | 30 | 20,000 | 5.42 | 1.3% | 4.7% | 17% | 48% | 88% | 99.6% | 100% | 0 |

**2tc**: one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 5,000 | 8.81 | 0.28% | 0.98% | 3.2% | 9.9% | 33% | 73% | 99% | 100% | 100% | 0 |
| 8, two comms | 12 | 5,000 | 8.53 | 0.52% | 1.4% | 4.9% | 15% | 43% | 82% | 99.5% | 100% | 100% | 0 |
| 8, two comms | 14 | 5,000 | 8.29 | 0.52% | 2.1% | 6.3% | 20% | 52% | 89% | 99.8% | 100% | 100% | 0 |
| 8, two comms | 16 | 5,000 | 8.06 | 0.82% | 3.1% | 9.6% | 26% | 61% | 94% | 99.9% | 100% | 100% | 0 |
| 8, two comms | 18 | 5,000 | 7.88 | 0.86% | 3.7% | 11% | 31% | 69% | 96% | 100% | 100% | 100% | 0 |
| 8, two comms | 20 | 5,000 | 7.71 | 1.5% | 4.5% | 14% | 37% | 74% | 98% | 100% | 100% | 100% | 0 |
| 8, two comms | 22 | 5,000 | 7.57 | 1.6% | 5.0% | 17% | 41% | 79% | 99% | 100% | 100% | 100% | 0 |
| 8, two comms | 24 | 5,000 | 7.46 | 1.9% | 5.9% | 18% | 45% | 84% | 99.6% | 100% | 100% | 100% | 0 |
| 8, two comms | 26 | 5,000 | 7.31 | 2.2% | 7.2% | 21% | 50% | 88% | 99.6% | 100% | 100% | 100% | 0 |
| 8, two comms | 28 | 5,000 | 7.16 | 2.7% | 8.4% | 25% | 56% | 90% | 99.9% | 100% | 100% | 100% | 0 |
| 8, two comms | 30 | 5,000 | 7.07 | 3.0% | 9.4% | 27% | 60% | 93% | 99.9% | 100% | 100% | 100% | 0 |
| 8, best of the two | 10 | 5,000 | 8.81 | 0.28% | 0.98% | 3.2% | 9.9% | 33% | 73% | 99% | 100% | 100% | 0 |
| 8, best of the two | 12 | 5,000 | 8.53 | 0.52% | 1.4% | 4.9% | 15% | 43% | 82% | 99.5% | 100% | 100% | 0 |
| 8, best of the two | 14 | 5,000 | 8.29 | 0.52% | 2.1% | 6.3% | 20% | 52% | 89% | 99.8% | 100% | 100% | 0 |
| 8, best of the two | 16 | 5,000 | 8.06 | 0.82% | 3.1% | 9.6% | 26% | 61% | 94% | 99.9% | 100% | 100% | 0 |
| 8, best of the two | 18 | 5,000 | 7.88 | 0.86% | 3.7% | 11% | 31% | 69% | 96% | 100% | 100% | 100% | 0 |
| 8, best of the two | 20 | 5,000 | 7.71 | 1.5% | 4.5% | 14% | 37% | 74% | 98% | 100% | 100% | 100% | 0 |
| 8, best of the two | 22 | 5,000 | 7.57 | 1.6% | 5.0% | 17% | 41% | 79% | 99% | 100% | 100% | 100% | 0 |
| 8, best of the two | 24 | 5,000 | 7.46 | 1.9% | 5.9% | 18% | 45% | 84% | 99.6% | 100% | 100% | 100% | 0 |
| 8, best of the two | 26 | 5,000 | 7.31 | 2.2% | 7.2% | 21% | 50% | 88% | 99.6% | 100% | 100% | 100% | 0 |
| 8, best of the two | 28 | 5,000 | 7.16 | 2.7% | 8.4% | 25% | 56% | 90% | 99.9% | 100% | 100% | 100% | 0 |
| 8, best of the two | 30 | 5,000 | 7.07 | 3.0% | 9.4% | 27% | 60% | 93% | 99.9% | 100% | 100% | 100% | 0 |
| 10, two comms | 10 | 200 | 8.38 | 0.50% | 2.0% | 4.5% | 17% | 49% | 89% | 100% | 100% | 100% | 0 |
| 10, two comms | 12 | 200 | 8.09 | 0 of 200 | 2.0% | 8.5% | 22% | 66% | 93% | 100% | 100% | 100% | 0 |
| 10, two comms | 14 | 200 | 7.95 | 1.0% | 2.5% | 11% | 27% | 67% | 97% | 100% | 100% | 100% | 0 |
| 10, two comms | 16 | 200 | 7.59 | 1.5% | 6.0% | 17% | 41% | 77% | 99% | 100% | 100% | 100% | 0 |
| 10, two comms | 18 | 200 | 7.51 | 2.5% | 8.0% | 16% | 45% | 79% | 99% | 100% | 100% | 100% | 0 |
| 10, two comms | 20 | 200 | 7.34 | 2.5% | 6.5% | 21% | 49% | 87% | 100% | 100% | 100% | 100% | 0 |
| 10, two comms | 22 | 200 | 7.26 | 1.5% | 6.0% | 28% | 53% | 86% | 100% | 100% | 100% | 100% | 0 |
| 10, two comms | 24 | 200 | 7.20 | 3.5% | 8.5% | 25% | 52% | 92% | 100% | 100% | 100% | 100% | 0 |
| 10, two comms | 26 | 200 | 6.95 | 3.0% | 12% | 31% | 64% | 96% | 100% | 100% | 100% | 100% | 0 |
| 10, two comms | 28 | 200 | 6.94 | 4.0% | 9.5% | 28% | 64% | 98% | 100% | 100% | 100% | 100% | 0 |
| 10, two comms | 30 | 200 | 6.74 | 6.5% | 13% | 32% | 71% | 97% | 100% | 100% | 100% | 100% | 0 |
| 10, best of the two | 10 | 200 | 8.38 | 0.50% | 2.0% | 4.5% | 17% | 49% | 89% | 100% | 100% | 100% | 0 |
| 10, best of the two | 12 | 200 | 8.09 | 0 of 200 | 2.0% | 8.5% | 22% | 66% | 93% | 100% | 100% | 100% | 0 |
| 10, best of the two | 14 | 200 | 7.95 | 1.0% | 2.5% | 11% | 27% | 67% | 97% | 100% | 100% | 100% | 0 |
| 10, best of the two | 16 | 200 | 7.59 | 1.5% | 6.0% | 17% | 41% | 77% | 99% | 100% | 100% | 100% | 0 |
| 10, best of the two | 18 | 200 | 7.51 | 2.5% | 8.0% | 16% | 45% | 79% | 99% | 100% | 100% | 100% | 0 |
| 10, best of the two | 20 | 200 | 7.34 | 2.5% | 6.5% | 21% | 49% | 87% | 100% | 100% | 100% | 100% | 0 |
| 10, best of the two | 22 | 200 | 7.26 | 1.5% | 6.0% | 28% | 53% | 86% | 100% | 100% | 100% | 100% | 0 |
| 10, best of the two | 24 | 200 | 7.20 | 3.5% | 8.5% | 25% | 52% | 92% | 100% | 100% | 100% | 100% | 0 |
| 10, best of the two | 26 | 200 | 6.95 | 3.0% | 12% | 31% | 64% | 96% | 100% | 100% | 100% | 100% | 0 |
| 10, best of the two | 28 | 200 | 6.94 | 4.0% | 9.5% | 28% | 64% | 98% | 100% | 100% | 100% | 100% | 0 |
| 10, best of the two | 30 | 200 | 6.74 | 6.5% | 13% | 32% | 71% | 97% | 100% | 100% | 100% | 100% | 0 |
| 12, one alg | 10 | 20,000 | 9.62 | 0.03% | 0.19% | 0.86% | 3.2% | 13% | 39% | 83% | 99.4% | 99.9% | 0.10% |
| 12, one alg | 12 | 20,000 | 9.45 | 0.11% | 0.27% | 1.3% | 4.4% | 16% | 46% | 88% | 99.7% | 99.9% | 0.08% |
| 12, one alg | 14 | 20,000 | 9.32 | 0.14% | 0.49% | 1.6% | 5.2% | 18% | 51% | 91% | 99.9% | 99.9% | 0.02% |
| 12, one alg | 16 | 20,000 | 9.21 | 0.11% | 0.47% | 1.6% | 5.9% | 21% | 56% | 94% | 99.9% | 99.9% | <0.01% |
| 12, one alg | 18 | 20,000 | 9.11 | 0.11% | 0.50% | 1.9% | 6.7% | 23% | 61% | 96% | 99.9% | 99.9% | <0.01% |
| 12, one alg | 20 | 20,000 | 9.03 | 0.14% | 0.55% | 2.0% | 7.2% | 25% | 65% | 97% | 100% | 100% | 0 |
| 12, one alg | 22 | 20,000 | 8.93 | 0.16% | 0.58% | 2.4% | 8.3% | 28% | 69% | 98% | 100% | 100% | 0 |
| 12, one alg | 24 | 20,000 | 8.87 | 0.17% | 0.66% | 2.7% | 9.0% | 30% | 72% | 99% | 100% | 100% | 0 |
| 12, one alg | 26 | 20,000 | 8.81 | 0.20% | 0.70% | 2.8% | 9.7% | 32% | 75% | 99% | 100% | 100% | 0 |
| 12, one alg | 28 | 20,000 | 8.74 | 0.20% | 0.74% | 3.0% | 11% | 35% | 78% | 99.3% | 100% | 100% | 0 |
| 12, one alg | 30 | 20,000 | 8.69 | 0.23% | 0.84% | 3.2% | 11% | 36% | 80% | 99.6% | 100% | 100% | 0 |

**3tc**: one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 20,000 | 10.70 | 0.01% | 0.07% | 0.37% | 1.3% | 4.4% | 14% | 38% | 75% | 97% | 0 |
| 8, two comms | 12 | 20,000 | 10.39 | 0.06% | 0.15% | 0.54% | 1.8% | 6.7% | 20% | 49% | 84% | 99% | 0 |
| 8, two comms | 14 | 20,000 | 10.13 | 0.09% | 0.27% | 0.89% | 2.7% | 9.2% | 26% | 58% | 90% | 99.7% | 0 |
| 8, two comms | 16 | 20,000 | 9.89 | 0.09% | 0.30% | 1.1% | 4.1% | 12% | 33% | 67% | 94% | 99.9% | 0 |
| 8, two comms | 18 | 20,000 | 9.70 | 0.11% | 0.44% | 1.6% | 5.1% | 15% | 38% | 73% | 97% | 99.9% | 0 |
| 8, two comms | 20 | 20,000 | 9.50 | 0.16% | 0.59% | 2.0% | 6.3% | 18% | 45% | 80% | 98% | 99.9% | 0 |
| 8, two comms | 22 | 20,000 | 9.34 | 0.21% | 0.75% | 2.5% | 7.8% | 22% | 50% | 84% | 99% | 100% | 0 |
| 8, two comms | 24 | 20,000 | 9.19 | 0.27% | 0.94% | 3.2% | 9.3% | 25% | 55% | 88% | 99.4% | 100% | 0 |
| 8, two comms | 26 | 20,000 | 9.05 | 0.38% | 1.2% | 3.7% | 10% | 28% | 60% | 91% | 99.5% | 100% | 0 |
| 8, two comms | 28 | 20,000 | 8.93 | 0.47% | 1.3% | 4.1% | 12% | 31% | 65% | 93% | 99.8% | 100% | 0 |
| 8, two comms | 30 | 20,000 | 8.82 | 0.34% | 1.3% | 4.6% | 14% | 34% | 69% | 95% | 99.9% | 100% | 0 |
| 8, best of the two | 10 | 20,000 | 10.70 | 0.01% | 0.07% | 0.37% | 1.3% | 4.4% | 14% | 38% | 75% | 97% | 0 |
| 8, best of the two | 12 | 20,000 | 10.39 | 0.06% | 0.15% | 0.54% | 1.8% | 6.7% | 20% | 49% | 84% | 99% | 0 |
| 8, best of the two | 14 | 20,000 | 10.13 | 0.09% | 0.27% | 0.89% | 2.7% | 9.2% | 26% | 58% | 90% | 99.7% | 0 |
| 8, best of the two | 16 | 20,000 | 9.89 | 0.09% | 0.30% | 1.1% | 4.1% | 12% | 33% | 67% | 94% | 99.9% | 0 |
| 8, best of the two | 18 | 20,000 | 9.70 | 0.11% | 0.44% | 1.6% | 5.1% | 15% | 38% | 73% | 97% | 99.9% | 0 |
| 8, best of the two | 20 | 20,000 | 9.50 | 0.16% | 0.59% | 2.0% | 6.3% | 18% | 45% | 80% | 98% | 99.9% | 0 |
| 8, best of the two | 22 | 20,000 | 9.34 | 0.21% | 0.75% | 2.5% | 7.8% | 22% | 50% | 84% | 99% | 100% | 0 |
| 8, best of the two | 24 | 20,000 | 9.19 | 0.27% | 0.94% | 3.2% | 9.3% | 25% | 55% | 88% | 99.4% | 100% | 0 |
| 8, best of the two | 26 | 20,000 | 9.05 | 0.38% | 1.2% | 3.7% | 10% | 28% | 60% | 91% | 99.5% | 100% | 0 |
| 8, best of the two | 28 | 20,000 | 8.93 | 0.47% | 1.3% | 4.1% | 12% | 31% | 65% | 93% | 99.8% | 100% | 0 |
| 8, best of the two | 30 | 20,000 | 8.82 | 0.34% | 1.3% | 4.6% | 14% | 34% | 69% | 95% | 99.9% | 100% | 0 |
| 10, two comms | 10 | 500 | 10.56 | 0 of 500 | 0 of 500 | 0.60% | 1.8% | 4.6% | 14% | 45% | 80% | 98% | 0 |
| 10, two comms | 12 | 500 | 10.39 | 0 of 500 | 0 of 500 | 0.20% | 1.6% | 6.0% | 21% | 50% | 85% | 99% | 0 |
| 10, two comms | 14 | 500 | 10.00 | 0.20% | 0.40% | 1.6% | 4.0% | 11% | 27% | 63% | 93% | 100% | 0 |
| 10, two comms | 16 | 500 | 9.83 | 0.20% | 0.20% | 1.2% | 4.6% | 12% | 36% | 69% | 94% | 100% | 0 |
| 10, two comms | 18 | 500 | 9.61 | 0 of 500 | 0.20% | 1.8% | 6.6% | 17% | 40% | 76% | 98% | 100% | 0 |
| 10, two comms | 20 | 500 | 9.34 | 0.40% | 1.0% | 2.2% | 7.4% | 22% | 50% | 84% | 99% | 100% | 0 |
| 10, two comms | 22 | 500 | 9.26 | 0.20% | 0.40% | 1.8% | 8.8% | 24% | 53% | 86% | 99.4% | 100% | 0 |
| 10, two comms | 24 | 500 | 9.08 | 0.40% | 1.0% | 3.2% | 11% | 27% | 59% | 90% | 99.4% | 100% | 0 |
| 10, two comms | 26 | 500 | 8.89 | 0.60% | 2.0% | 4.6% | 13% | 32% | 67% | 92% | 100% | 100% | 0 |
| 10, two comms | 28 | 500 | 8.78 | 0.80% | 1.8% | 4.2% | 16% | 36% | 69% | 95% | 99.8% | 100% | 0 |
| 10, two comms | 30 | 500 | 8.63 | 1.0% | 2.2% | 7.0% | 16% | 39% | 74% | 96% | 100% | 100% | 0 |
| 10, best of the two | 10 | 500 | 10.56 | 0 of 500 | 0 of 500 | 0.60% | 1.8% | 4.6% | 14% | 45% | 80% | 98% | 0 |
| 10, best of the two | 12 | 500 | 10.39 | 0 of 500 | 0 of 500 | 0.20% | 1.6% | 6.0% | 21% | 50% | 85% | 99% | 0 |
| 10, best of the two | 14 | 500 | 10.00 | 0.20% | 0.40% | 1.6% | 4.0% | 11% | 27% | 63% | 93% | 100% | 0 |
| 10, best of the two | 16 | 500 | 9.83 | 0.20% | 0.20% | 1.2% | 4.6% | 12% | 36% | 69% | 94% | 100% | 0 |
| 10, best of the two | 18 | 500 | 9.61 | 0 of 500 | 0.20% | 1.8% | 6.6% | 17% | 40% | 76% | 98% | 100% | 0 |
| 10, best of the two | 20 | 500 | 9.34 | 0.40% | 1.0% | 2.2% | 7.4% | 22% | 50% | 84% | 99% | 100% | 0 |
| 10, best of the two | 22 | 500 | 9.26 | 0.20% | 0.40% | 1.8% | 8.8% | 24% | 53% | 86% | 99.4% | 100% | 0 |
| 10, best of the two | 24 | 500 | 9.08 | 0.40% | 1.0% | 3.2% | 11% | 27% | 59% | 90% | 99.4% | 100% | 0 |
| 10, best of the two | 26 | 500 | 8.89 | 0.60% | 2.0% | 4.6% | 13% | 32% | 67% | 92% | 100% | 100% | 0 |
| 10, best of the two | 28 | 500 | 8.78 | 0.80% | 1.8% | 4.2% | 16% | 36% | 69% | 95% | 99.8% | 100% | 0 |
| 10, best of the two | 30 | 500 | 8.63 | 1.0% | 2.2% | 7.0% | 16% | 39% | 74% | 96% | 100% | 100% | 0 |

**Pure 2c2c**: one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 20,000 | 10.22 | 0.06% | 0.17% | 0.68% | 2.5% | 8.6% | 25% | 56% | 87% | 98% | 0 |
| 8, two comms | 12 | 20,000 | 9.94 | 0.07% | 0.36% | 1.2% | 3.8% | 12% | 32% | 66% | 92% | 99.2% | 0 |
| 8, two comms | 14 | 20,000 | 9.69 | 0.15% | 0.43% | 1.6% | 4.9% | 15% | 39% | 75% | 95% | 99.7% | 0 |
| 8, two comms | 16 | 20,000 | 9.49 | 0.15% | 0.60% | 2.1% | 6.6% | 19% | 46% | 80% | 97% | 99.8% | 0 |
| 8, two comms | 18 | 20,000 | 9.31 | 0.28% | 0.92% | 2.7% | 7.8% | 23% | 52% | 85% | 98% | 99.9% | 0 |
| 8, two comms | 20 | 20,000 | 9.13 | 0.22% | 0.91% | 3.0% | 9.9% | 27% | 58% | 89% | 99% | 99.9% | 0 |
| 8, two comms | 22 | 20,000 | 8.98 | 0.29% | 1.1% | 3.7% | 11% | 30% | 64% | 92% | 99.3% | 99.9% | 0 |
| 8, two comms | 24 | 20,000 | 8.82 | 0.46% | 1.5% | 4.7% | 14% | 35% | 69% | 94% | 99.7% | 100% | 0 |
| 8, two comms | 26 | 20,000 | 8.70 | 0.55% | 1.7% | 5.4% | 15% | 38% | 73% | 96% | 99.8% | 100% | 0 |
| 8, two comms | 28 | 20,000 | 8.56 | 0.75% | 2.2% | 6.4% | 18% | 42% | 77% | 97% | 99.9% | 100% | 0 |
| 8, two comms | 30 | 20,000 | 8.46 | 0.74% | 2.3% | 6.9% | 19% | 46% | 80% | 98% | 99.9% | 100% | 0 |
| 8, best of the two | 10 | 20,000 | 10.22 | 0.06% | 0.17% | 0.68% | 2.5% | 8.6% | 25% | 56% | 87% | 98% | 0 |
| 8, best of the two | 12 | 20,000 | 9.94 | 0.07% | 0.36% | 1.2% | 3.8% | 12% | 32% | 66% | 92% | 99.2% | 0 |
| 8, best of the two | 14 | 20,000 | 9.69 | 0.15% | 0.43% | 1.6% | 4.9% | 15% | 39% | 75% | 95% | 99.7% | 0 |
| 8, best of the two | 16 | 20,000 | 9.49 | 0.15% | 0.60% | 2.1% | 6.6% | 19% | 46% | 80% | 97% | 99.8% | 0 |
| 8, best of the two | 18 | 20,000 | 9.31 | 0.28% | 0.92% | 2.7% | 7.8% | 23% | 52% | 85% | 98% | 99.9% | 0 |
| 8, best of the two | 20 | 20,000 | 9.13 | 0.22% | 0.91% | 3.0% | 9.9% | 27% | 58% | 89% | 99% | 99.9% | 0 |
| 8, best of the two | 22 | 20,000 | 8.98 | 0.29% | 1.1% | 3.7% | 11% | 30% | 64% | 92% | 99.3% | 99.9% | 0 |
| 8, best of the two | 24 | 20,000 | 8.82 | 0.46% | 1.5% | 4.7% | 14% | 35% | 69% | 94% | 99.7% | 100% | 0 |
| 8, best of the two | 26 | 20,000 | 8.70 | 0.55% | 1.7% | 5.4% | 15% | 38% | 73% | 96% | 99.8% | 100% | 0 |
| 8, best of the two | 28 | 20,000 | 8.56 | 0.75% | 2.2% | 6.4% | 18% | 42% | 77% | 97% | 99.9% | 100% | 0 |
| 8, best of the two | 30 | 20,000 | 8.46 | 0.74% | 2.3% | 6.9% | 19% | 46% | 80% | 98% | 99.9% | 100% | 0 |
| 10, two comms | 10 | 500 | 10.09 | 0 of 500 | 0.20% | 0.40% | 2.8% | 10% | 28% | 60% | 90% | 99% | 0 |
| 10, two comms | 12 | 500 | 9.69 | 0 of 500 | 0.40% | 2.6% | 5.6% | 16% | 37% | 74% | 96% | 99.6% | 0 |
| 10, two comms | 14 | 500 | 9.51 | 0 of 500 | 0.40% | 1.8% | 6.2% | 19% | 47% | 78% | 97% | 99.6% | 0 |
| 10, two comms | 16 | 500 | 9.33 | 0 of 500 | 1.2% | 3.8% | 7.2% | 19% | 51% | 86% | 99% | 99.8% | 0 |
| 10, two comms | 18 | 500 | 9.12 | 0 of 500 | 0.20% | 3.8% | 9.8% | 25% | 60% | 90% | 99% | 100% | 0 |
| 10, two comms | 20 | 500 | 9.02 | 0 of 500 | 0.60% | 2.8% | 10% | 31% | 63% | 92% | 99.4% | 100% | 0 |
| 10, two comms | 22 | 500 | 8.80 | 1.0% | 1.6% | 4.8% | 15% | 37% | 67% | 94% | 99.6% | 100% | 0 |
| 10, two comms | 24 | 500 | 8.57 | 1.2% | 3.6% | 8.4% | 17% | 42% | 75% | 97% | 99.6% | 100% | 0 |
| 10, two comms | 26 | 500 | 8.52 | 0.40% | 1.2% | 5.2% | 17% | 45% | 81% | 98% | 100% | 100% | 0 |
| 10, two comms | 28 | 500 | 8.50 | 0.20% | 2.0% | 6.2% | 19% | 45% | 80% | 98% | 99.8% | 100% | 0 |
| 10, two comms | 30 | 500 | 8.35 | 0.80% | 2.8% | 8.8% | 23% | 48% | 82% | 99.2% | 100% | 100% | 0 |
| 10, one alg | 10 | 20,000 | 8.67 | 0.10% | 0.37% | 1.5% | 4.7% | 14% | 33% | 40% | 40% | 40% | 60% |
| 10, one alg | 12 | 20,000 | 8.62 | 0.24% | 0.61% | 2.0% | 5.8% | 16% | 38% | 45% | 45% | 45% | 55% |
| 10, one alg | 14 | 20,000 | 8.56 | 0.29% | 0.85% | 2.5% | 6.9% | 19% | 42% | 50% | 50% | 50% | 50% |
| 10, one alg | 16 | 20,000 | 8.53 | 0.31% | 0.93% | 2.7% | 7.9% | 21% | 46% | 54% | 54% | 54% | 46% |
| 10, one alg | 18 | 20,000 | 8.51 | 0.33% | 0.98% | 2.9% | 8.7% | 23% | 50% | 57% | 57% | 57% | 43% |
| 10, one alg | 20 | 20,000 | 8.44 | 0.42% | 1.2% | 3.5% | 10% | 26% | 54% | 62% | 62% | 62% | 38% |
| 10, one alg | 22 | 20,000 | 8.44 | 0.40% | 1.2% | 3.9% | 11% | 28% | 57% | 65% | 65% | 65% | 35% |
| 10, one alg | 24 | 20,000 | 8.40 | 0.43% | 1.3% | 4.2% | 12% | 30% | 60% | 68% | 68% | 68% | 32% |
| 10, one alg | 26 | 20,000 | 8.36 | 0.43% | 1.5% | 4.7% | 13% | 33% | 63% | 70% | 70% | 70% | 30% |
| 10, one alg | 28 | 20,000 | 8.33 | 0.48% | 1.6% | 5.0% | 14% | 35% | 66% | 73% | 73% | 73% | 27% |
| 10, one alg | 30 | 20,000 | 8.31 | 0.56% | 1.7% | 5.3% | 15% | 36% | 68% | 75% | 75% | 75% | 25% |
| 10, best of the two | 10 | 500 | 9.51 | 0 of 500 | 0.20% | 2.0% | 7.8% | 22% | 49% | 74% | 94% | 99.2% | 0 |
| 10, best of the two | 12 | 500 | 9.08 | 0.60% | 1.4% | 4.6% | 11% | 30% | 61% | 86% | 97% | 99.6% | 0 |
| 10, best of the two | 14 | 500 | 8.84 | 0.40% | 1.2% | 4.8% | 14% | 36% | 72% | 90% | 98% | 99.6% | 0 |
| 10, best of the two | 16 | 500 | 8.86 | 0 of 500 | 1.4% | 5.0% | 13% | 34% | 69% | 92% | 99.2% | 99.8% | 0 |
| 10, best of the two | 18 | 500 | 8.60 | 0.40% | 1.6% | 6.2% | 18% | 40% | 79% | 95% | 99.4% | 100% | 0 |
| 10, best of the two | 20 | 500 | 8.48 | 0.60% | 2.2% | 6.4% | 18% | 46% | 83% | 96% | 99.4% | 100% | 0 |
| 10, best of the two | 22 | 500 | 8.28 | 1.6% | 3.6% | 8.8% | 24% | 53% | 84% | 97% | 99.8% | 100% | 0 |
| 10, best of the two | 24 | 500 | 8.15 | 1.6% | 4.4% | 12% | 25% | 57% | 87% | 98% | 99.8% | 100% | 0 |
| 10, best of the two | 26 | 500 | 8.05 | 0.80% | 3.0% | 12% | 28% | 61% | 91% | 99% | 100% | 100% | 0 |
| 10, best of the two | 28 | 500 | 8.02 | 0.60% | 3.8% | 12% | 28% | 62% | 92% | 99% | 100% | 100% | 0 |
| 10, best of the two | 30 | 500 | 7.93 | 1.0% | 3.6% | 13% | 33% | 63% | 93% | 99.6% | 100% | 100% | 0 |
| 12, one alg | 10 | 20,000 | 9.51 | 0.24% | 0.79% | 2.7% | 7.7% | 21% | 46% | 72% | 95% | 98% | 1.8% |
| 12, one alg | 12 | 20,000 | 9.30 | 0.52% | 1.3% | 3.6% | 9.7% | 25% | 52% | 78% | 97% | 99% | 1.1% |
| 12, one alg | 14 | 20,000 | 9.14 | 0.58% | 1.6% | 4.4% | 11% | 28% | 57% | 83% | 98% | 99.5% | 0.49% |
| 12, one alg | 16 | 20,000 | 9.00 | 0.63% | 1.8% | 4.8% | 13% | 31% | 62% | 86% | 99% | 99.8% | 0.25% |
| 12, one alg | 18 | 20,000 | 8.87 | 0.77% | 2.1% | 5.5% | 14% | 34% | 66% | 89% | 99.3% | 99.8% | 0.16% |
| 12, one alg | 20 | 20,000 | 8.75 | 0.83% | 2.3% | 6.2% | 16% | 38% | 70% | 92% | 99.7% | 99.9% | 0.07% |
| 12, one alg | 22 | 20,000 | 8.64 | 0.95% | 2.5% | 7.0% | 17% | 41% | 74% | 94% | 99.8% | 99.9% | 0.05% |
| 12, one alg | 24 | 20,000 | 8.54 | 0.98% | 2.7% | 7.6% | 19% | 43% | 77% | 95% | 99.9% | 99.9% | 0.02% |
| 12, one alg | 26 | 20,000 | 8.45 | 1.0% | 3.0% | 8.5% | 21% | 46% | 79% | 96% | 99.9% | 99.9% | <0.01% |
| 12, one alg | 28 | 20,000 | 8.38 | 1.2% | 3.3% | 8.9% | 22% | 49% | 81% | 97% | 99.9% | 99.9% | <0.01% |
| 12, one alg | 30 | 20,000 | 8.29 | 1.3% | 3.6% | 9.6% | 23% | 51% | 84% | 98% | 99.9% | 100% | 0 |

**Twisted 2c2c**: one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 20,000 | 9.62 | 0.09% | 0.29% | 1.2% | 4.5% | 15% | 40% | 79% | 98% | 99.9% | 0 |
| 8, two comms | 12 | 20,000 | 9.38 | 0.15% | 0.53% | 1.9% | 5.9% | 19% | 49% | 86% | 99.3% | 99.9% | 0 |
| 8, two comms | 14 | 20,000 | 9.18 | 0.22% | 0.80% | 2.5% | 7.9% | 24% | 56% | 91% | 99.7% | 100% | 0 |
| 8, two comms | 16 | 20,000 | 9.01 | 0.26% | 0.85% | 3.0% | 9.7% | 28% | 63% | 94% | 99.9% | 100% | 0 |
| 8, two comms | 18 | 20,000 | 8.87 | 0.26% | 1.0% | 3.7% | 11% | 32% | 68% | 96% | 99.9% | 100% | 0 |
| 8, two comms | 20 | 20,000 | 8.73 | 0.38% | 1.3% | 4.2% | 13% | 36% | 74% | 98% | 99.9% | 100% | 0 |
| 8, two comms | 22 | 20,000 | 8.59 | 0.43% | 1.6% | 5.2% | 15% | 41% | 78% | 98% | 99.9% | 100% | 0 |
| 8, two comms | 24 | 20,000 | 8.48 | 0.52% | 1.8% | 5.8% | 17% | 45% | 82% | 99.1% | 100% | 100% | 0 |
| 8, two comms | 26 | 20,000 | 8.38 | 0.70% | 2.1% | 6.3% | 19% | 49% | 85% | 99.4% | 100% | 100% | 0 |
| 8, two comms | 28 | 20,000 | 8.28 | 0.70% | 2.3% | 7.3% | 21% | 53% | 88% | 99.6% | 100% | 100% | 0 |
| 8, two comms | 30 | 20,000 | 8.19 | 0.74% | 2.6% | 8.3% | 23% | 56% | 90% | 99.8% | 100% | 100% | 0 |
| 8, best of the two | 10 | 20,000 | 9.62 | 0.09% | 0.29% | 1.2% | 4.5% | 15% | 40% | 79% | 98% | 99.9% | 0 |
| 8, best of the two | 12 | 20,000 | 9.38 | 0.15% | 0.53% | 1.9% | 5.9% | 19% | 49% | 86% | 99.3% | 99.9% | 0 |
| 8, best of the two | 14 | 20,000 | 9.18 | 0.22% | 0.80% | 2.5% | 7.9% | 24% | 56% | 91% | 99.7% | 100% | 0 |
| 8, best of the two | 16 | 20,000 | 9.01 | 0.26% | 0.85% | 3.0% | 9.7% | 28% | 63% | 94% | 99.9% | 100% | 0 |
| 8, best of the two | 18 | 20,000 | 8.87 | 0.26% | 1.0% | 3.7% | 11% | 32% | 68% | 96% | 99.9% | 100% | 0 |
| 8, best of the two | 20 | 20,000 | 8.73 | 0.38% | 1.3% | 4.2% | 13% | 36% | 74% | 98% | 99.9% | 100% | 0 |
| 8, best of the two | 22 | 20,000 | 8.59 | 0.43% | 1.6% | 5.2% | 15% | 41% | 78% | 98% | 99.9% | 100% | 0 |
| 8, best of the two | 24 | 20,000 | 8.48 | 0.52% | 1.8% | 5.8% | 17% | 45% | 82% | 99.1% | 100% | 100% | 0 |
| 8, best of the two | 26 | 20,000 | 8.38 | 0.70% | 2.1% | 6.3% | 19% | 49% | 85% | 99.4% | 100% | 100% | 0 |
| 8, best of the two | 28 | 20,000 | 8.28 | 0.70% | 2.3% | 7.3% | 21% | 53% | 88% | 99.6% | 100% | 100% | 0 |
| 8, best of the two | 30 | 20,000 | 8.19 | 0.74% | 2.6% | 8.3% | 23% | 56% | 90% | 99.8% | 100% | 100% | 0 |
| 10, two comms | 10 | 500 | 9.54 | 0 of 500 | 0 of 500 | 1.4% | 4.8% | 15% | 43% | 83% | 99.2% | 100% | 0 |
| 10, two comms | 12 | 500 | 9.33 | 0.40% | 0.60% | 2.4% | 7.6% | 20% | 49% | 88% | 99.4% | 100% | 0 |
| 10, two comms | 14 | 500 | 9.11 | 0.20% | 1.4% | 3.0% | 11% | 25% | 57% | 92% | 99.8% | 100% | 0 |
| 10, two comms | 16 | 500 | 8.86 | 0.40% | 1.2% | 4.6% | 12% | 35% | 66% | 95% | 99.8% | 100% | 0 |
| 10, two comms | 18 | 500 | 8.74 | 0.60% | 1.2% | 4.2% | 12% | 38% | 71% | 97% | 100% | 100% | 0 |
| 10, two comms | 20 | 500 | 8.66 | 0.80% | 2.4% | 4.8% | 16% | 36% | 76% | 98% | 100% | 100% | 0 |
| 10, two comms | 22 | 500 | 8.39 | 0.60% | 2.0% | 6.8% | 19% | 49% | 85% | 99% | 100% | 100% | 0 |
| 10, two comms | 24 | 500 | 8.32 | 0.80% | 2.8% | 7.2% | 22% | 51% | 85% | 99% | 100% | 100% | 0 |
| 10, two comms | 26 | 500 | 8.29 | 0.60% | 2.8% | 7.6% | 21% | 52% | 87% | 99.6% | 100% | 100% | 0 |
| 10, two comms | 28 | 500 | 8.12 | 0.60% | 3.6% | 11% | 26% | 58% | 89% | 99.8% | 100% | 100% | 0 |
| 10, two comms | 30 | 500 | 8.02 | 1.0% | 2.6% | 8.8% | 27% | 65% | 94% | 100% | 100% | 100% | 0 |
| 10, best of the two | 10 | 500 | 9.54 | 0 of 500 | 0 of 500 | 1.4% | 4.8% | 15% | 43% | 83% | 99.2% | 100% | 0 |
| 10, best of the two | 12 | 500 | 9.33 | 0.40% | 0.60% | 2.4% | 7.6% | 20% | 49% | 88% | 99.4% | 100% | 0 |
| 10, best of the two | 14 | 500 | 9.11 | 0.20% | 1.4% | 3.0% | 11% | 25% | 57% | 92% | 99.8% | 100% | 0 |
| 10, best of the two | 16 | 500 | 8.86 | 0.40% | 1.2% | 4.6% | 12% | 35% | 66% | 95% | 99.8% | 100% | 0 |
| 10, best of the two | 18 | 500 | 8.74 | 0.60% | 1.2% | 4.2% | 12% | 38% | 71% | 97% | 100% | 100% | 0 |
| 10, best of the two | 20 | 500 | 8.66 | 0.80% | 2.4% | 4.8% | 16% | 36% | 76% | 98% | 100% | 100% | 0 |
| 10, best of the two | 22 | 500 | 8.39 | 0.60% | 2.0% | 6.8% | 19% | 49% | 85% | 99% | 100% | 100% | 0 |
| 10, best of the two | 24 | 500 | 8.32 | 0.80% | 2.8% | 7.2% | 22% | 51% | 85% | 99% | 100% | 100% | 0 |
| 10, best of the two | 26 | 500 | 8.29 | 0.60% | 2.8% | 7.6% | 21% | 52% | 87% | 99.6% | 100% | 100% | 0 |
| 10, best of the two | 28 | 500 | 8.12 | 0.60% | 3.6% | 11% | 26% | 58% | 89% | 99.8% | 100% | 100% | 0 |
| 10, best of the two | 30 | 500 | 8.02 | 1.0% | 2.6% | 8.8% | 27% | 65% | 94% | 100% | 100% | 100% | 0 |
| 12, one alg | 10 | 20,000 | 10.10 | 0.05% | 0.17% | 0.79% | 2.9% | 9.8% | 26% | 60% | 89% | 99.3% | 0.71% |
| 12, one alg | 12 | 20,000 | 9.94 | 0.07% | 0.28% | 0.96% | 3.3% | 12% | 31% | 66% | 92% | 99.6% | 0.37% |
| 12, one alg | 14 | 20,000 | 9.78 | 0.11% | 0.37% | 1.3% | 4.2% | 14% | 35% | 72% | 95% | 99.8% | 0.23% |
| 12, one alg | 16 | 20,000 | 9.66 | 0.14% | 0.38% | 1.4% | 4.7% | 15% | 39% | 76% | 96% | 99.9% | 0.07% |
| 12, one alg | 18 | 20,000 | 9.55 | 0.10% | 0.41% | 1.7% | 5.3% | 18% | 43% | 80% | 97% | 99.9% | 0.04% |
| 12, one alg | 20 | 20,000 | 9.45 | 0.12% | 0.47% | 1.5% | 5.9% | 19% | 46% | 84% | 98% | 99.9% | 0.02% |
| 12, one alg | 22 | 20,000 | 9.34 | 0.18% | 0.59% | 2.0% | 6.5% | 21% | 50% | 86% | 99% | 100% | 0 |
| 12, one alg | 24 | 20,000 | 9.26 | 0.23% | 0.62% | 2.3% | 7.3% | 23% | 53% | 88% | 99.2% | 99.9% | 0.01% |
| 12, one alg | 26 | 20,000 | 9.18 | 0.21% | 0.69% | 2.4% | 7.9% | 25% | 56% | 90% | 99.5% | 100% | 0 |
| 12, one alg | 28 | 20,000 | 9.12 | 0.26% | 0.70% | 2.6% | 8.4% | 26% | 58% | 92% | 99.6% | 100% | 0 |
| 12, one alg | 30 | 20,000 | 9.06 | 0.20% | 0.69% | 2.8% | 9.2% | 28% | 61% | 93% | 99.8% | 100% | 0 |

**3c1t**: one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 20,000 | 10.84 | 0.01% | 0.07% | 0.26% | 1.2% | 3.5% | 12% | 33% | 70% | 96% | 0 |
| 8, two comms | 12 | 20,000 | 10.62 | 0.02% | 0.07% | 0.44% | 1.5% | 4.9% | 15% | 41% | 77% | 98% | 0 |
| 8, two comms | 14 | 20,000 | 10.39 | 0.03% | 0.14% | 0.50% | 1.9% | 6.8% | 20% | 48% | 84% | 99% | 0 |
| 8, two comms | 16 | 20,000 | 10.22 | 0.13% | 0.35% | 0.84% | 2.5% | 8.3% | 23% | 54% | 88% | 99.5% | 0 |
| 8, two comms | 18 | 20,000 | 10.06 | 0.11% | 0.29% | 0.98% | 3.1% | 10% | 28% | 60% | 92% | 99.8% | 0 |
| 8, two comms | 20 | 20,000 | 9.90 | 0.13% | 0.47% | 1.4% | 4.1% | 12% | 32% | 66% | 94% | 99.9% | 0 |
| 8, two comms | 22 | 20,000 | 9.77 | 0.18% | 0.52% | 1.6% | 4.6% | 14% | 36% | 71% | 96% | 99.9% | 0 |
| 8, two comms | 24 | 20,000 | 9.64 | 0.13% | 0.63% | 1.8% | 5.4% | 16% | 40% | 76% | 97% | 99.9% | 0 |
| 8, two comms | 26 | 20,000 | 9.53 | 0.20% | 0.68% | 2.0% | 6.2% | 18% | 43% | 79% | 98% | 99.9% | 0 |
| 8, two comms | 28 | 20,000 | 9.40 | 0.24% | 0.76% | 2.5% | 7.6% | 20% | 48% | 82% | 99% | 99.9% | 0 |
| 8, two comms | 30 | 20,000 | 9.31 | 0.30% | 0.89% | 2.7% | 8.1% | 22% | 51% | 85% | 99% | 99.9% | 0 |
| 8, best of the two | 10 | 20,000 | 10.84 | 0.01% | 0.07% | 0.26% | 1.2% | 3.5% | 12% | 33% | 70% | 96% | 0 |
| 8, best of the two | 12 | 20,000 | 10.62 | 0.02% | 0.07% | 0.44% | 1.5% | 4.9% | 15% | 41% | 77% | 98% | 0 |
| 8, best of the two | 14 | 20,000 | 10.39 | 0.03% | 0.14% | 0.50% | 1.9% | 6.8% | 20% | 48% | 84% | 99% | 0 |
| 8, best of the two | 16 | 20,000 | 10.22 | 0.13% | 0.35% | 0.84% | 2.5% | 8.3% | 23% | 54% | 88% | 99.5% | 0 |
| 8, best of the two | 18 | 20,000 | 10.06 | 0.11% | 0.29% | 0.98% | 3.1% | 10% | 28% | 60% | 92% | 99.8% | 0 |
| 8, best of the two | 20 | 20,000 | 9.90 | 0.13% | 0.47% | 1.4% | 4.1% | 12% | 32% | 66% | 94% | 99.9% | 0 |
| 8, best of the two | 22 | 20,000 | 9.77 | 0.18% | 0.52% | 1.6% | 4.6% | 14% | 36% | 71% | 96% | 99.9% | 0 |
| 8, best of the two | 24 | 20,000 | 9.64 | 0.13% | 0.63% | 1.8% | 5.4% | 16% | 40% | 76% | 97% | 99.9% | 0 |
| 8, best of the two | 26 | 20,000 | 9.53 | 0.20% | 0.68% | 2.0% | 6.2% | 18% | 43% | 79% | 98% | 99.9% | 0 |
| 8, best of the two | 28 | 20,000 | 9.40 | 0.24% | 0.76% | 2.5% | 7.6% | 20% | 48% | 82% | 99% | 99.9% | 0 |
| 8, best of the two | 30 | 20,000 | 9.31 | 0.30% | 0.89% | 2.7% | 8.1% | 22% | 51% | 85% | 99% | 99.9% | 0 |
| 10, two comms | 10 | 500 | 10.68 | 0 of 500 | 0 of 500 | 0.20% | 1.0% | 4.8% | 14% | 40% | 75% | 97% | 0 |
| 10, two comms | 12 | 500 | 10.50 | 0 of 500 | 0 of 500 | 0.40% | 1.8% | 5.8% | 19% | 43% | 82% | 99% | 0 |
| 10, two comms | 14 | 500 | 10.26 | 0 of 500 | 0 of 500 | 0.20% | 2.8% | 6.8% | 23% | 54% | 88% | 99.2% | 0 |
| 10, two comms | 16 | 500 | 10.17 | 0 of 500 | 0.20% | 0.80% | 2.2% | 8.8% | 24% | 55% | 91% | 99.8% | 0 |
| 10, two comms | 18 | 500 | 9.88 | 0.20% | 0.20% | 2.4% | 3.8% | 11% | 33% | 67% | 95% | 100% | 0 |
| 10, two comms | 20 | 500 | 9.73 | 0.20% | 1.2% | 2.2% | 5.2% | 15% | 35% | 72% | 96% | 100% | 0 |
| 10, two comms | 22 | 500 | 9.60 | 0.60% | 1.0% | 2.6% | 6.2% | 17% | 40% | 75% | 98% | 100% | 0 |
| 10, two comms | 24 | 500 | 9.57 | 0.20% | 0.80% | 1.8% | 5.8% | 17% | 42% | 77% | 98% | 100% | 0 |
| 10, two comms | 26 | 500 | 9.38 | 0.20% | 1.0% | 2.4% | 6.4% | 19% | 46% | 87% | 99% | 100% | 0 |
| 10, two comms | 28 | 500 | 9.27 | 0.20% | 1.2% | 3.4% | 9.2% | 24% | 51% | 85% | 99.4% | 100% | 0 |
| 10, two comms | 30 | 500 | 9.11 | 0.60% | 1.6% | 3.8% | 11% | 27% | 57% | 89% | 99.4% | 100% | 0 |
| 10, best of the two | 10 | 500 | 10.68 | 0 of 500 | 0 of 500 | 0.20% | 1.0% | 4.8% | 14% | 40% | 75% | 97% | 0 |
| 10, best of the two | 12 | 500 | 10.50 | 0 of 500 | 0 of 500 | 0.40% | 1.8% | 5.8% | 19% | 43% | 82% | 99% | 0 |
| 10, best of the two | 14 | 500 | 10.26 | 0 of 500 | 0 of 500 | 0.20% | 2.8% | 6.8% | 23% | 54% | 88% | 99.2% | 0 |
| 10, best of the two | 16 | 500 | 10.17 | 0 of 500 | 0.20% | 0.80% | 2.2% | 8.8% | 24% | 55% | 91% | 99.8% | 0 |
| 10, best of the two | 18 | 500 | 9.88 | 0.20% | 0.20% | 2.4% | 3.8% | 11% | 33% | 67% | 95% | 100% | 0 |
| 10, best of the two | 20 | 500 | 9.73 | 0.20% | 1.2% | 2.2% | 5.2% | 15% | 35% | 72% | 96% | 100% | 0 |
| 10, best of the two | 22 | 500 | 9.60 | 0.60% | 1.0% | 2.6% | 6.2% | 17% | 40% | 75% | 98% | 100% | 0 |
| 10, best of the two | 24 | 500 | 9.57 | 0.20% | 0.80% | 1.8% | 5.8% | 17% | 42% | 77% | 98% | 100% | 0 |
| 10, best of the two | 26 | 500 | 9.38 | 0.20% | 1.0% | 2.4% | 6.4% | 19% | 46% | 87% | 99% | 100% | 0 |
| 10, best of the two | 28 | 500 | 9.27 | 0.20% | 1.2% | 3.4% | 9.2% | 24% | 51% | 85% | 99.4% | 100% | 0 |
| 10, best of the two | 30 | 500 | 9.11 | 0.60% | 1.6% | 3.8% | 11% | 27% | 57% | 89% | 99.4% | 100% | 0 |
| 12, one alg | 10 | 20,000 | 11.45 | 0 of 20,000 | 0 of 20,000 | 0.02% | 0.09% | 0.26% | 1.1% | 4.2% | 13% | 34% | 66% |
| 12, one alg | 12 | 20,000 | 11.43 | 0 of 20,000 | <0.01% | 0.01% | 0.11% | 0.35% | 1.4% | 4.9% | 15% | 39% | 61% |
| 12, one alg | 14 | 20,000 | 11.40 | <0.01% | <0.01% | 0.04% | 0.12% | 0.45% | 1.6% | 6.0% | 18% | 43% | 57% |
| 12, one alg | 16 | 20,000 | 11.37 | 0 of 20,000 | <0.01% | 0.07% | 0.13% | 0.49% | 1.9% | 6.7% | 20% | 46% | 54% |
| 12, one alg | 18 | 20,000 | 11.36 | <0.01% | 0.02% | 0.04% | 0.18% | 0.59% | 2.0% | 7.7% | 22% | 51% | 49% |
| 12, one alg | 20 | 20,000 | 11.33 | 0 of 20,000 | 0.02% | 0.05% | 0.15% | 0.65% | 2.4% | 8.3% | 24% | 54% | 46% |
| 12, one alg | 22 | 20,000 | 11.32 | <0.01% | 0.02% | 0.05% | 0.18% | 0.74% | 2.6% | 9.3% | 26% | 57% | 43% |
| 12, one alg | 24 | 20,000 | 11.30 | 0.01% | 0.02% | 0.05% | 0.22% | 0.76% | 2.8% | 10% | 28% | 60% | 40% |
| 12, one alg | 26 | 20,000 | 11.28 | 0 of 20,000 | 0.02% | 0.09% | 0.20% | 0.91% | 3.2% | 11% | 30% | 63% | 37% |
| 12, one alg | 28 | 20,000 | 11.27 | <0.01% | 0.02% | 0.07% | 0.22% | 0.86% | 3.3% | 11% | 31% | 65% | 35% |
| 12, one alg | 30 | 20,000 | 11.25 | <0.01% | 0.02% | 0.05% | 0.31% | 1.1% | 3.5% | 12% | 34% | 68% | 32% |

**5c**: one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 20,000 | 11.25 | <0.01% | 0.03% | 0.20% | 0.68% | 2.3% | 7.9% | 24% | 55% | 87% | 0 |
| 8, two comms | 12 | 20,000 | 11.02 | 0.03% | 0.12% | 0.33% | 0.94% | 3.3% | 10% | 30% | 63% | 92% | 0 |
| 8, two comms | 14 | 20,000 | 10.82 | 0.02% | 0.05% | 0.33% | 1.3% | 4.3% | 13% | 35% | 70% | 94% | 0 |
| 8, two comms | 16 | 20,000 | 10.65 | 0.08% | 0.20% | 0.58% | 1.8% | 5.4% | 15% | 40% | 75% | 96% | 0 |
| 8, two comms | 18 | 20,000 | 10.50 | 0.05% | 0.19% | 0.64% | 2.1% | 6.3% | 18% | 45% | 80% | 98% | 0 |
| 8, two comms | 20 | 20,000 | 10.37 | 0.09% | 0.20% | 0.71% | 2.4% | 7.2% | 20% | 49% | 84% | 99% | 0 |
| 8, two comms | 22 | 20,000 | 10.24 | 0.09% | 0.33% | 1.0% | 2.9% | 8.7% | 23% | 54% | 87% | 99% | 0 |
| 8, two comms | 24 | 20,000 | 10.12 | 0.07% | 0.28% | 1.0% | 3.4% | 10% | 26% | 58% | 89% | 99.5% | 0 |
| 8, two comms | 26 | 20,000 | 10.01 | 0.10% | 0.42% | 1.2% | 3.7% | 11% | 29% | 62% | 91% | 99.6% | 0 |
| 8, two comms | 28 | 20,000 | 9.88 | 0.16% | 0.43% | 1.4% | 4.5% | 13% | 33% | 66% | 93% | 99.8% | 0 |
| 8, two comms | 30 | 20,000 | 9.82 | 0.17% | 0.47% | 1.6% | 4.7% | 13% | 35% | 69% | 95% | 99.8% | 0 |
| 8, best of the two | 10 | 20,000 | 11.25 | <0.01% | 0.03% | 0.20% | 0.68% | 2.3% | 7.9% | 24% | 55% | 87% | 0 |
| 8, best of the two | 12 | 20,000 | 11.02 | 0.03% | 0.12% | 0.33% | 0.94% | 3.3% | 10% | 30% | 63% | 92% | 0 |
| 8, best of the two | 14 | 20,000 | 10.82 | 0.02% | 0.05% | 0.33% | 1.3% | 4.3% | 13% | 35% | 70% | 94% | 0 |
| 8, best of the two | 16 | 20,000 | 10.65 | 0.08% | 0.20% | 0.58% | 1.8% | 5.4% | 15% | 40% | 75% | 96% | 0 |
| 8, best of the two | 18 | 20,000 | 10.50 | 0.05% | 0.19% | 0.64% | 2.1% | 6.3% | 18% | 45% | 80% | 98% | 0 |
| 8, best of the two | 20 | 20,000 | 10.37 | 0.09% | 0.20% | 0.71% | 2.4% | 7.2% | 20% | 49% | 84% | 99% | 0 |
| 8, best of the two | 22 | 20,000 | 10.24 | 0.09% | 0.33% | 1.0% | 2.9% | 8.7% | 23% | 54% | 87% | 99% | 0 |
| 8, best of the two | 24 | 20,000 | 10.12 | 0.07% | 0.28% | 1.0% | 3.4% | 10% | 26% | 58% | 89% | 99.5% | 0 |
| 8, best of the two | 26 | 20,000 | 10.01 | 0.10% | 0.42% | 1.2% | 3.7% | 11% | 29% | 62% | 91% | 99.6% | 0 |
| 8, best of the two | 28 | 20,000 | 9.88 | 0.16% | 0.43% | 1.4% | 4.5% | 13% | 33% | 66% | 93% | 99.8% | 0 |
| 8, best of the two | 30 | 20,000 | 9.82 | 0.17% | 0.47% | 1.6% | 4.7% | 13% | 35% | 69% | 95% | 99.8% | 0 |
| 10, two comms | 10 | 2,000 | 11.00 | 0 of 2,000 | 0 of 2,000 | 0.10% | 1.0% | 2.8% | 10% | 30% | 64% | 93% | 0 |
| 10, two comms | 12 | 2,000 | 10.80 | 0 of 2,000 | 0.15% | 0.35% | 1.1% | 4.1% | 13% | 35% | 71% | 96% | 0 |
| 10, two comms | 14 | 2,000 | 10.61 | 0.10% | 0.10% | 0.35% | 1.1% | 5.2% | 16% | 42% | 77% | 97% | 0 |
| 10, two comms | 16 | 2,000 | 10.48 | 0.05% | 0.05% | 0.60% | 1.9% | 5.9% | 19% | 45% | 81% | 98% | 0 |
| 10, two comms | 18 | 2,000 | 10.30 | 0.15% | 0.40% | 1.3% | 3.2% | 9.1% | 22% | 49% | 85% | 99.2% | 0 |
| 10, two comms | 20 | 2,000 | 10.17 | 0.15% | 0.20% | 0.90% | 2.3% | 8.2% | 24% | 58% | 90% | 99.4% | 0 |
| 10, two comms | 22 | 2,000 | 10.03 | 0.15% | 0.25% | 1.2% | 3.6% | 11% | 28% | 62% | 92% | 99.8% | 0 |
| 10, two comms | 24 | 2,000 | 9.94 | 0.20% | 0.65% | 1.3% | 4.5% | 13% | 31% | 63% | 93% | 99.8% | 0 |
| 10, two comms | 26 | 2,000 | 9.85 | 0.10% | 0.70% | 1.7% | 4.8% | 13% | 32% | 68% | 95% | 99.9% | 0 |
| 10, two comms | 28 | 2,000 | 9.70 | 0.15% | 0.45% | 1.6% | 5.3% | 16% | 37% | 73% | 96% | 100% | 0 |
| 10, two comms | 30 | 2,000 | 9.65 | 0.20% | 0.55% | 1.6% | 4.9% | 16% | 39% | 76% | 97% | 100% | 0 |
| 10, one alg | 10 | 20,000 | 9.43 | 0.01% | 0.02% | 0.11% | 0.32% | 1.0% | 2.9% | 7.6% | 7.6% | 7.6% | 92% |
| 10, one alg | 12 | 20,000 | 9.46 | <0.01% | 0.03% | 0.09% | 0.27% | 1.1% | 3.6% | 9.4% | 9.4% | 9.4% | 91% |
| 10, one alg | 14 | 20,000 | 9.42 | 0.02% | 0.07% | 0.16% | 0.37% | 1.4% | 4.0% | 10% | 10% | 10% | 90% |
| 10, one alg | 16 | 20,000 | 9.39 | <0.01% | 0.04% | 0.18% | 0.50% | 1.6% | 4.7% | 11% | 11% | 11% | 89% |
| 10, one alg | 18 | 20,000 | 9.43 | <0.01% | 0.03% | 0.15% | 0.47% | 1.7% | 5.0% | 13% | 13% | 13% | 87% |
| 10, one alg | 20 | 20,000 | 9.41 | <0.01% | 0.04% | 0.15% | 0.55% | 1.9% | 5.6% | 14% | 14% | 14% | 86% |
| 10, one alg | 22 | 20,000 | 9.37 | 0.02% | 0.06% | 0.22% | 0.67% | 2.1% | 6.6% | 15% | 15% | 15% | 85% |
| 10, one alg | 24 | 20,000 | 9.41 | 0.01% | 0.03% | 0.14% | 0.63% | 2.3% | 6.6% | 16% | 16% | 16% | 84% |
| 10, one alg | 26 | 20,000 | 9.37 | 0.01% | 0.06% | 0.23% | 0.73% | 2.6% | 7.2% | 17% | 17% | 17% | 83% |
| 10, one alg | 28 | 20,000 | 9.39 | <0.01% | 0.06% | 0.22% | 0.78% | 2.8% | 7.7% | 19% | 19% | 19% | 81% |
| 10, one alg | 30 | 20,000 | 9.34 | 0.02% | 0.06% | 0.25% | 0.90% | 3.2% | 8.6% | 20% | 20% | 20% | 80% |
| 10, best of the two | 10 | 2,000 | 10.87 | 0 of 2,000 | 0 of 2,000 | 0.30% | 1.5% | 3.8% | 13% | 35% | 66% | 93% | 0 |
| 10, best of the two | 12 | 2,000 | 10.64 | 0 of 2,000 | 0.25% | 0.55% | 1.5% | 5.8% | 17% | 41% | 73% | 96% | 0 |
| 10, best of the two | 14 | 2,000 | 10.48 | 0.10% | 0.15% | 0.55% | 1.5% | 6.6% | 20% | 47% | 79% | 98% | 0 |
| 10, best of the two | 16 | 2,000 | 10.34 | 0.05% | 0.10% | 0.65% | 2.2% | 7.3% | 23% | 51% | 83% | 99% | 0 |
| 10, best of the two | 18 | 2,000 | 10.17 | 0.15% | 0.45% | 1.4% | 3.5% | 10% | 26% | 55% | 87% | 99.2% | 0 |
| 10, best of the two | 20 | 2,000 | 10.03 | 0.15% | 0.25% | 1.3% | 3.0% | 10% | 28% | 63% | 92% | 99.5% | 0 |
| 10, best of the two | 22 | 2,000 | 9.89 | 0.15% | 0.25% | 1.3% | 4.0% | 12% | 33% | 68% | 93% | 99.9% | 0 |
| 10, best of the two | 24 | 2,000 | 9.80 | 0.20% | 0.70% | 1.6% | 5.3% | 15% | 36% | 69% | 94% | 99.8% | 0 |
| 10, best of the two | 26 | 2,000 | 9.73 | 0.10% | 0.70% | 1.8% | 5.3% | 15% | 36% | 72% | 96% | 99.9% | 0 |
| 10, best of the two | 28 | 2,000 | 9.57 | 0.15% | 0.45% | 1.7% | 6.0% | 18% | 42% | 78% | 97% | 100% | 0 |
| 10, best of the two | 30 | 2,000 | 9.53 | 0.20% | 0.65% | 1.9% | 5.6% | 18% | 44% | 79% | 98% | 100% | 0 |
| 12, one alg | 10 | 20,000 | 10.92 | 0.03% | 0.05% | 0.22% | 0.75% | 2.5% | 8.2% | 25% | 55% | 84% | 16% |
| 12, one alg | 12 | 20,000 | 10.82 | 0.03% | 0.07% | 0.26% | 0.88% | 3.1% | 10% | 29% | 61% | 88% | 12% |
| 12, one alg | 14 | 20,000 | 10.75 | 0.04% | 0.12% | 0.31% | 0.96% | 3.7% | 11% | 32% | 66% | 91% | 8.7% |
| 12, one alg | 16 | 20,000 | 10.67 | 0.02% | 0.11% | 0.35% | 1.3% | 4.1% | 13% | 35% | 70% | 93% | 6.9% |
| 12, one alg | 18 | 20,000 | 10.59 | 0.02% | 0.08% | 0.33% | 1.3% | 4.5% | 15% | 39% | 75% | 95% | 4.6% |
| 12, one alg | 20 | 20,000 | 10.50 | 0.03% | 0.12% | 0.44% | 1.5% | 5.1% | 16% | 43% | 78% | 97% | 3.5% |
| 12, one alg | 22 | 20,000 | 10.43 | 0.04% | 0.15% | 0.55% | 1.6% | 5.6% | 18% | 46% | 81% | 97% | 2.8% |
| 12, one alg | 24 | 20,000 | 10.37 | 0.03% | 0.10% | 0.46% | 1.7% | 6.3% | 19% | 48% | 84% | 98% | 2.2% |
| 12, one alg | 26 | 20,000 | 10.31 | 0.06% | 0.18% | 0.58% | 1.9% | 6.7% | 20% | 51% | 86% | 99% | 1.4% |
| 12, one alg | 28 | 20,000 | 10.24 | 0.03% | 0.16% | 0.65% | 2.2% | 7.4% | 22% | 54% | 88% | 99% | 1.0% |
| 12, one alg | 30 | 20,000 | 10.18 | 0.07% | 0.22% | 0.65% | 2.3% | 7.9% | 23% | 56% | 89% | 99.2% | 0.80% |

**3c3c** (two separate corner 3-cycles): one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 20,000 | 11.87 | 0 of 20,000 | 0.02% | 0.08% | 0.30% | 1.3% | 4.3% | 13% | 35% | 70% | 0.38% |
| 8, two comms | 12 | 20,000 | 11.68 | 0.02% | 0.05% | 0.14% | 0.49% | 1.6% | 5.4% | 16% | 40% | 75% | 0.16% |
| 8, two comms | 14 | 20,000 | 11.49 | 0.01% | 0.03% | 0.15% | 0.64% | 2.2% | 6.5% | 20% | 46% | 81% | 0.08% |
| 8, two comms | 16 | 20,000 | 11.33 | 0.01% | 0.04% | 0.18% | 0.76% | 2.6% | 7.9% | 22% | 51% | 85% | 0.04% |
| 8, two comms | 18 | 20,000 | 11.17 | <0.01% | 0.08% | 0.28% | 0.93% | 3.1% | 9.3% | 26% | 57% | 88% | <0.01% |
| 8, two comms | 20 | 20,000 | 11.05 | 0.03% | 0.09% | 0.36% | 1.2% | 3.6% | 11% | 28% | 61% | 91% | 0.01% |
| 8, two comms | 22 | 20,000 | 10.93 | 0.05% | 0.16% | 0.38% | 1.3% | 4.2% | 12% | 32% | 65% | 93% | 0 |
| 8, two comms | 24 | 20,000 | 10.83 | 0.04% | 0.14% | 0.43% | 1.4% | 4.6% | 14% | 35% | 68% | 94% | 0 |
| 8, two comms | 26 | 20,000 | 10.71 | 0.05% | 0.21% | 0.69% | 1.8% | 5.4% | 15% | 38% | 72% | 96% | <0.01% |
| 8, two comms | 28 | 20,000 | 10.63 | 0.04% | 0.16% | 0.59% | 2.0% | 6.0% | 17% | 41% | 74% | 97% | 0 |
| 8, two comms | 30 | 20,000 | 10.53 | 0.06% | 0.20% | 0.66% | 2.2% | 6.6% | 18% | 44% | 78% | 97% | 0 |
| 8, best of the two | 10 | 20,000 | 11.87 | 0 of 20,000 | 0.02% | 0.08% | 0.30% | 1.3% | 4.3% | 13% | 35% | 70% | 0.38% |
| 8, best of the two | 12 | 20,000 | 11.68 | 0.02% | 0.05% | 0.14% | 0.49% | 1.6% | 5.4% | 16% | 40% | 75% | 0.16% |
| 8, best of the two | 14 | 20,000 | 11.49 | 0.01% | 0.03% | 0.15% | 0.64% | 2.2% | 6.5% | 20% | 46% | 81% | 0.08% |
| 8, best of the two | 16 | 20,000 | 11.33 | 0.01% | 0.04% | 0.18% | 0.76% | 2.6% | 7.9% | 22% | 51% | 85% | 0.04% |
| 8, best of the two | 18 | 20,000 | 11.17 | <0.01% | 0.08% | 0.28% | 0.93% | 3.1% | 9.3% | 26% | 57% | 88% | <0.01% |
| 8, best of the two | 20 | 20,000 | 11.05 | 0.03% | 0.09% | 0.36% | 1.2% | 3.6% | 11% | 28% | 61% | 91% | 0.01% |
| 8, best of the two | 22 | 20,000 | 10.93 | 0.05% | 0.16% | 0.38% | 1.3% | 4.2% | 12% | 32% | 65% | 93% | 0 |
| 8, best of the two | 24 | 20,000 | 10.83 | 0.04% | 0.14% | 0.43% | 1.4% | 4.6% | 14% | 35% | 68% | 94% | 0 |
| 8, best of the two | 26 | 20,000 | 10.71 | 0.05% | 0.21% | 0.69% | 1.8% | 5.4% | 15% | 38% | 72% | 96% | <0.01% |
| 8, best of the two | 28 | 20,000 | 10.63 | 0.04% | 0.16% | 0.59% | 2.0% | 6.0% | 17% | 41% | 74% | 97% | 0 |
| 8, best of the two | 30 | 20,000 | 10.53 | 0.06% | 0.20% | 0.66% | 2.2% | 6.6% | 18% | 44% | 78% | 97% | 0 |
| 10, two comms | 10 | 2,000 | 11.36 | 0 of 2,000 | 0.05% | 0.15% | 0.50% | 2.4% | 6.9% | 22% | 51% | 84% | 0 |
| 10, two comms | 12 | 2,000 | 11.20 | 0.05% | 0.05% | 0.15% | 0.50% | 2.0% | 8.2% | 24% | 58% | 89% | 0 |
| 10, two comms | 14 | 2,000 | 11.07 | 0.05% | 0.05% | 0.25% | 0.80% | 2.5% | 8.9% | 27% | 63% | 91% | 0 |
| 10, two comms | 16 | 2,000 | 10.90 | 0 of 2,000 | 0.10% | 0.40% | 1.1% | 3.3% | 10% | 32% | 69% | 95% | 0 |
| 10, two comms | 18 | 2,000 | 10.76 | 0 of 2,000 | 0.05% | 0.40% | 1.7% | 4.5% | 12% | 35% | 74% | 97% | 0 |
| 10, two comms | 20 | 2,000 | 10.64 | 0 of 2,000 | 0.05% | 0.55% | 1.5% | 4.7% | 14% | 41% | 78% | 97% | 0 |
| 10, two comms | 22 | 2,000 | 10.49 | 0.15% | 0.35% | 1.1% | 2.2% | 7.0% | 18% | 45% | 80% | 98% | 0 |
| 10, two comms | 24 | 2,000 | 10.42 | 0 of 2,000 | 0.10% | 0.30% | 1.9% | 6.9% | 20% | 48% | 83% | 99% | 0 |
| 10, two comms | 26 | 2,000 | 10.34 | 0 of 2,000 | 0.20% | 0.65% | 2.4% | 7.0% | 21% | 50% | 86% | 99.1% | 0 |
| 10, two comms | 28 | 2,000 | 10.22 | 0.15% | 0.25% | 1.2% | 3.0% | 9.7% | 25% | 52% | 87% | 99.2% | 0 |
| 10, two comms | 30 | 2,000 | 10.12 | 0.05% | 0.20% | 1.2% | 3.6% | 9.7% | 25% | 58% | 90% | 99.5% | 0 |
| 10, one alg | 10 | 20,000 | 9.26 | 0.02% | 0.05% | 0.11% | 0.33% | 0.99% | 2.5% | 5.4% | 5.4% | 5.4% | 95% |
| 10, one alg | 12 | 20,000 | 9.20 | <0.01% | 0.05% | 0.17% | 0.45% | 1.2% | 3.1% | 6.3% | 6.3% | 6.3% | 94% |
| 10, one alg | 14 | 20,000 | 9.15 | 0.02% | 0.07% | 0.19% | 0.55% | 1.5% | 3.7% | 7.1% | 7.1% | 7.1% | 93% |
| 10, one alg | 16 | 20,000 | 9.19 | 0.02% | 0.07% | 0.19% | 0.57% | 1.6% | 4.1% | 8.1% | 8.1% | 8.1% | 92% |
| 10, one alg | 18 | 20,000 | 9.18 | 0.02% | 0.06% | 0.24% | 0.60% | 1.8% | 4.4% | 8.6% | 8.6% | 8.6% | 91% |
| 10, one alg | 20 | 20,000 | 9.16 | 0.02% | 0.04% | 0.20% | 0.77% | 2.1% | 5.2% | 9.9% | 9.9% | 9.9% | 90% |
| 10, one alg | 22 | 20,000 | 9.20 | 0.03% | 0.05% | 0.17% | 0.65% | 2.1% | 5.1% | 10% | 10% | 10% | 90% |
| 10, one alg | 24 | 20,000 | 9.15 | 0.02% | 0.09% | 0.26% | 0.76% | 2.3% | 5.9% | 11% | 11% | 11% | 89% |
| 10, one alg | 26 | 20,000 | 9.16 | 0.02% | 0.07% | 0.24% | 0.87% | 2.4% | 6.3% | 12% | 12% | 12% | 88% |
| 10, one alg | 28 | 20,000 | 9.16 | 0.03% | 0.13% | 0.34% | 0.98% | 2.7% | 7.0% | 13% | 13% | 13% | 87% |
| 10, one alg | 30 | 20,000 | 9.13 | 0.06% | 0.17% | 0.43% | 1.1% | 3.0% | 7.1% | 14% | 14% | 14% | 86% |
| 10, best of the two | 10 | 2,000 | 11.24 | 0 of 2,000 | 0.15% | 0.35% | 0.90% | 3.4% | 9.3% | 26% | 54% | 85% | 0 |
| 10, best of the two | 12 | 2,000 | 11.06 | 0.05% | 0.05% | 0.25% | 0.75% | 3.3% | 11% | 29% | 61% | 89% | 0 |
| 10, best of the two | 14 | 2,000 | 10.95 | 0.05% | 0.10% | 0.40% | 1.1% | 3.7% | 12% | 31% | 66% | 92% | 0 |
| 10, best of the two | 16 | 2,000 | 10.78 | 0 of 2,000 | 0.10% | 0.50% | 1.7% | 4.5% | 14% | 37% | 70% | 95% | 0 |
| 10, best of the two | 18 | 2,000 | 10.61 | 0.05% | 0.10% | 0.55% | 2.4% | 6.5% | 16% | 41% | 76% | 97% | 0 |
| 10, best of the two | 20 | 2,000 | 10.48 | 0 of 2,000 | 0.05% | 0.55% | 2.2% | 6.7% | 19% | 47% | 79% | 97% | 0 |
| 10, best of the two | 22 | 2,000 | 10.33 | 0.20% | 0.45% | 1.3% | 3.0% | 9.1% | 22% | 51% | 81% | 98% | 0 |
| 10, best of the two | 24 | 2,000 | 10.26 | 0 of 2,000 | 0.30% | 0.65% | 2.6% | 9.1% | 24% | 53% | 84% | 99% | 0 |
| 10, best of the two | 26 | 2,000 | 10.20 | 0 of 2,000 | 0.20% | 0.85% | 3.0% | 9.2% | 25% | 56% | 87% | 99.2% | 0 |
| 10, best of the two | 28 | 2,000 | 10.05 | 0.20% | 0.50% | 1.7% | 4.0% | 12% | 30% | 59% | 89% | 99.3% | 0 |
| 10, best of the two | 30 | 2,000 | 9.97 | 0.10% | 0.25% | 1.4% | 4.3% | 12% | 30% | 63% | 92% | 99.6% | 0 |
| 12, one alg | 10 | 20,000 | 10.93 | 0.03% | 0.09% | 0.26% | 0.82% | 2.7% | 8.4% | 24% | 51% | 82% | 18% |
| 12, one alg | 12 | 20,000 | 10.86 | 0.02% | 0.11% | 0.37% | 1.0% | 3.4% | 9.9% | 26% | 57% | 86% | 14% |
| 12, one alg | 14 | 20,000 | 10.78 | 0.05% | 0.13% | 0.39% | 1.3% | 4.0% | 11% | 30% | 62% | 89% | 11% |
| 12, one alg | 16 | 20,000 | 10.69 | 0.05% | 0.14% | 0.43% | 1.4% | 4.5% | 13% | 34% | 67% | 92% | 7.6% |
| 12, one alg | 18 | 20,000 | 10.60 | 0.05% | 0.14% | 0.51% | 1.7% | 5.3% | 15% | 38% | 71% | 94% | 6.2% |
| 12, one alg | 20 | 20,000 | 10.53 | 0.05% | 0.19% | 0.64% | 2.0% | 6.0% | 17% | 40% | 75% | 95% | 4.8% |
| 12, one alg | 22 | 20,000 | 10.48 | 0.09% | 0.19% | 0.62% | 2.1% | 6.3% | 17% | 42% | 77% | 96% | 3.6% |
| 12, one alg | 24 | 20,000 | 10.42 | 0.05% | 0.20% | 0.66% | 2.0% | 6.5% | 19% | 45% | 80% | 97% | 2.8% |
| 12, one alg | 26 | 20,000 | 10.34 | 0.07% | 0.25% | 0.79% | 2.4% | 7.6% | 21% | 48% | 83% | 98% | 2.1% |
| 12, one alg | 28 | 20,000 | 10.27 | 0.07% | 0.32% | 0.91% | 2.6% | 8.1% | 22% | 51% | 85% | 98% | 1.6% |
| 12, one alg | 30 | 20,000 | 10.22 | 0.09% | 0.33% | 0.99% | 2.9% | 8.5% | 23% | 54% | 87% | 99% | 1.0% |

**3e**: one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 2 or less | Adds 3 or less | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, one comm | 10 | 20,000 | 6.15 | 0.57% | 1.8% | 4.9% | 10% | 19% | 33% | 38% | 62% |
| 8, one comm | 12 | 20,000 | 6.10 | 0.79% | 2.2% | 5.6% | 11% | 22% | 37% | 42% | 58% |
| 8, one comm | 14 | 20,000 | 6.05 | 0.83% | 2.7% | 6.3% | 13% | 25% | 40% | 45% | 55% |
| 8, one comm | 16 | 20,000 | 6.01 | 0.98% | 2.8% | 7.0% | 15% | 28% | 44% | 49% | 51% |
| 8, one comm | 18 | 20,000 | 5.96 | 1.3% | 3.4% | 7.8% | 16% | 30% | 47% | 52% | 48% |
| 8, one comm | 20 | 20,000 | 5.95 | 1.2% | 3.6% | 8.6% | 18% | 32% | 51% | 56% | 44% |
| 8, one comm | 22 | 20,000 | 5.89 | 1.5% | 4.2% | 9.6% | 19% | 35% | 54% | 59% | 41% |
| 8, one comm | 24 | 20,000 | 5.86 | 1.4% | 4.2% | 10% | 21% | 37% | 56% | 61% | 39% |
| 8, one comm | 26 | 20,000 | 5.83 | 1.8% | 4.8% | 11% | 22% | 39% | 58% | 63% | 37% |
| 8, one comm | 28 | 20,000 | 5.80 | 1.9% | 5.1% | 12% | 24% | 41% | 61% | 66% | 34% |
| 8, one comm | 30 | 20,000 | 5.77 | 1.8% | 5.3% | 13% | 25% | 43% | 63% | 68% | 32% |
| 10, one comm | 10 | 20,000 | 6.77 | 0.82% | 2.4% | 6.8% | 16% | 36% | 67% | 94% | <0.01% |
| 10, one comm | 12 | 20,000 | 6.59 | 0.99% | 2.7% | 7.7% | 18% | 41% | 73% | 97% | 0 |
| 10, one comm | 14 | 20,000 | 6.43 | 1.1% | 3.5% | 9.0% | 21% | 46% | 79% | 98% | 0 |
| 10, one comm | 16 | 20,000 | 6.30 | 1.3% | 3.7% | 9.9% | 23% | 50% | 83% | 99% | 0 |
| 10, one comm | 18 | 20,000 | 6.16 | 1.6% | 4.3% | 11% | 26% | 55% | 86% | 99.4% | 0 |
| 10, one comm | 20 | 20,000 | 6.05 | 1.7% | 4.9% | 12% | 29% | 58% | 89% | 99.7% | 0 |
| 10, one comm | 22 | 20,000 | 5.93 | 2.1% | 5.5% | 14% | 31% | 63% | 91% | 99.8% | 0 |
| 10, one comm | 24 | 20,000 | 5.87 | 1.9% | 5.7% | 14% | 33% | 65% | 92% | 99.9% | 0 |
| 10, one comm | 26 | 20,000 | 5.78 | 2.4% | 6.4% | 16% | 35% | 68% | 94% | 99.9% | 0 |
| 10, one comm | 28 | 20,000 | 5.70 | 2.5% | 6.7% | 17% | 37% | 71% | 95% | 99.9% | 0 |
| 10, one comm | 30 | 20,000 | 5.63 | 2.5% | 7.0% | 18% | 39% | 73% | 96% | 99.9% | 0 |
| 12, one comm | 10 | 20,000 | 6.67 | 0.90% | 2.6% | 7.2% | 17% | 38% | 71% | 96% | 0 |
| 12, one comm | 12 | 20,000 | 6.50 | 1.0% | 2.9% | 8.1% | 19% | 44% | 77% | 98% | 0 |
| 12, one comm | 14 | 20,000 | 6.33 | 1.2% | 3.8% | 9.6% | 22% | 49% | 82% | 99% | 0 |
| 12, one comm | 16 | 20,000 | 6.19 | 1.4% | 4.1% | 11% | 25% | 54% | 86% | 99.3% | 0 |
| 12, one comm | 18 | 20,000 | 6.06 | 1.8% | 4.7% | 12% | 28% | 58% | 89% | 99.6% | 0 |
| 12, one comm | 20 | 20,000 | 5.95 | 1.8% | 5.3% | 13% | 31% | 62% | 91% | 99.8% | 0 |
| 12, one comm | 22 | 20,000 | 5.84 | 2.2% | 5.9% | 15% | 33% | 66% | 93% | 99.9% | 0 |
| 12, one comm | 24 | 20,000 | 5.77 | 2.1% | 6.2% | 16% | 35% | 69% | 94% | 99.9% | 0 |
| 12, one comm | 26 | 20,000 | 5.68 | 2.6% | 6.8% | 17% | 37% | 71% | 96% | 99.9% | 0 |
| 12, one comm | 28 | 20,000 | 5.59 | 2.8% | 7.3% | 18% | 40% | 74% | 97% | 99.9% | 0 |
| 12, one comm | 30 | 20,000 | 5.53 | 2.8% | 7.7% | 19% | 42% | 77% | 97% | 99.9% | 0 |

**2fe** (two edges flipped in place): one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 5,000 | 10.77 | 0.04% | 0.24% | 0.86% | 2.7% | 7.0% | 16% | 32% | 53% | 71% | 19% |
| 8, two comms | 12 | 5,000 | 10.30 | 0.14% | 0.54% | 1.8% | 4.7% | 11% | 24% | 45% | 66% | 79% | 14% |
| 8, two comms | 14 | 5,000 | 9.95 | 0.32% | 0.74% | 2.5% | 7.4% | 16% | 32% | 55% | 75% | 87% | 9.7% |
| 8, two comms | 16 | 5,000 | 9.60 | 0.44% | 1.2% | 3.7% | 9.8% | 22% | 40% | 64% | 83% | 91% | 7.3% |
| 8, two comms | 18 | 5,000 | 9.26 | 0.74% | 2.1% | 5.8% | 13% | 28% | 49% | 72% | 88% | 93% | 5.8% |
| 8, two comms | 20 | 5,000 | 8.96 | 0.84% | 2.8% | 7.5% | 17% | 35% | 57% | 79% | 92% | 96% | 4.1% |
| 8, two comms | 22 | 5,000 | 8.74 | 1.3% | 3.6% | 9.4% | 20% | 40% | 64% | 84% | 94% | 97% | 3.1% |
| 8, two comms | 24 | 5,000 | 8.54 | 1.4% | 4.2% | 11% | 24% | 44% | 69% | 88% | 96% | 98% | 2.2% |
| 8, two comms | 26 | 5,000 | 8.32 | 2.3% | 5.5% | 13% | 27% | 50% | 75% | 92% | 98% | 99% | 1.3% |
| 8, two comms | 28 | 5,000 | 8.09 | 2.2% | 6.7% | 16% | 33% | 56% | 80% | 94% | 99% | 99% | 1.0% |
| 8, two comms | 30 | 5,000 | 7.93 | 2.7% | 7.3% | 17% | 36% | 60% | 84% | 96% | 99.1% | 99.2% | 0.76% |
| 8, best of the two | 10 | 5,000 | 10.77 | 0.04% | 0.24% | 0.86% | 2.7% | 7.0% | 16% | 32% | 53% | 71% | 19% |
| 8, best of the two | 12 | 5,000 | 10.30 | 0.14% | 0.54% | 1.8% | 4.7% | 11% | 24% | 45% | 66% | 79% | 14% |
| 8, best of the two | 14 | 5,000 | 9.95 | 0.32% | 0.74% | 2.5% | 7.4% | 16% | 32% | 55% | 75% | 87% | 9.7% |
| 8, best of the two | 16 | 5,000 | 9.60 | 0.44% | 1.2% | 3.7% | 9.8% | 22% | 40% | 64% | 83% | 91% | 7.3% |
| 8, best of the two | 18 | 5,000 | 9.26 | 0.74% | 2.1% | 5.8% | 13% | 28% | 49% | 72% | 88% | 93% | 5.8% |
| 8, best of the two | 20 | 5,000 | 8.96 | 0.84% | 2.8% | 7.5% | 17% | 35% | 57% | 79% | 92% | 96% | 4.1% |
| 8, best of the two | 22 | 5,000 | 8.74 | 1.3% | 3.6% | 9.4% | 20% | 40% | 64% | 84% | 94% | 97% | 3.1% |
| 8, best of the two | 24 | 5,000 | 8.54 | 1.4% | 4.2% | 11% | 24% | 44% | 69% | 88% | 96% | 98% | 2.2% |
| 8, best of the two | 26 | 5,000 | 8.32 | 2.3% | 5.5% | 13% | 27% | 50% | 75% | 92% | 98% | 99% | 1.3% |
| 8, best of the two | 28 | 5,000 | 8.09 | 2.2% | 6.7% | 16% | 33% | 56% | 80% | 94% | 99% | 99% | 1.0% |
| 8, best of the two | 30 | 5,000 | 7.93 | 2.7% | 7.3% | 17% | 36% | 60% | 84% | 96% | 99.1% | 99.2% | 0.76% |
| 10, two comms | 10 | 200 | 8.87 | 0 of 200 | 1.5% | 3.5% | 12% | 32% | 68% | 97% | 100% | 100% | 0 |
| 10, two comms | 12 | 200 | 8.49 | 1.0% | 2.5% | 8.5% | 19% | 45% | 77% | 99% | 100% | 100% | 0 |
| 10, two comms | 14 | 200 | 8.23 | 0.50% | 1.5% | 11% | 23% | 56% | 87% | 99.5% | 100% | 100% | 0 |
| 10, two comms | 16 | 200 | 7.94 | 2.0% | 4.0% | 12% | 33% | 64% | 94% | 99% | 100% | 100% | 0 |
| 10, two comms | 18 | 200 | 7.78 | 1.5% | 4.5% | 15% | 37% | 70% | 95% | 99.5% | 100% | 100% | 0 |
| 10, two comms | 20 | 200 | 7.51 | 1.5% | 9.0% | 21% | 44% | 77% | 97% | 100% | 100% | 100% | 0 |
| 10, two comms | 22 | 200 | 7.35 | 3.5% | 11% | 23% | 47% | 85% | 96% | 100% | 100% | 100% | 0 |
| 10, two comms | 24 | 200 | 7.31 | 3.5% | 9.0% | 26% | 51% | 82% | 98% | 100% | 100% | 100% | 0 |
| 10, two comms | 26 | 200 | 7.08 | 4.0% | 13% | 30% | 57% | 87% | 99.5% | 100% | 100% | 100% | 0 |
| 10, two comms | 28 | 200 | 6.86 | 5.0% | 15% | 37% | 65% | 91% | 99.5% | 100% | 100% | 100% | 0 |
| 10, two comms | 30 | 200 | 6.89 | 5.0% | 13% | 36% | 65% | 92% | 99.5% | 100% | 100% | 100% | 0 |
| 10, best of the two | 10 | 200 | 8.87 | 0 of 200 | 1.5% | 3.5% | 12% | 32% | 68% | 97% | 100% | 100% | 0 |
| 10, best of the two | 12 | 200 | 8.49 | 1.0% | 2.5% | 8.5% | 19% | 45% | 77% | 99% | 100% | 100% | 0 |
| 10, best of the two | 14 | 200 | 8.23 | 0.50% | 1.5% | 11% | 23% | 56% | 87% | 99.5% | 100% | 100% | 0 |
| 10, best of the two | 16 | 200 | 7.94 | 2.0% | 4.0% | 12% | 33% | 64% | 94% | 99% | 100% | 100% | 0 |
| 10, best of the two | 18 | 200 | 7.78 | 1.5% | 4.5% | 15% | 37% | 70% | 95% | 99.5% | 100% | 100% | 0 |
| 10, best of the two | 20 | 200 | 7.51 | 1.5% | 9.0% | 21% | 44% | 77% | 97% | 100% | 100% | 100% | 0 |
| 10, best of the two | 22 | 200 | 7.35 | 3.5% | 11% | 23% | 47% | 85% | 96% | 100% | 100% | 100% | 0 |
| 10, best of the two | 24 | 200 | 7.31 | 3.5% | 9.0% | 26% | 51% | 82% | 98% | 100% | 100% | 100% | 0 |
| 10, best of the two | 26 | 200 | 7.08 | 4.0% | 13% | 30% | 57% | 87% | 99.5% | 100% | 100% | 100% | 0 |
| 10, best of the two | 28 | 200 | 6.86 | 5.0% | 15% | 37% | 65% | 91% | 99.5% | 100% | 100% | 100% | 0 |
| 10, best of the two | 30 | 200 | 6.89 | 5.0% | 13% | 36% | 65% | 92% | 99.5% | 100% | 100% | 100% | 0 |

**2e2e** (two swaps, no flip): one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 5,000 | 10.56 | 1.7% | 3.7% | 7.5% | 17% | 23% | 30% | 38% | 46% | 58% | 15% |
| 8, two comms | 12 | 5,000 | 10.29 | 2.2% | 4.9% | 9.7% | 20% | 27% | 34% | 43% | 52% | 64% | 11% |
| 8, two comms | 14 | 5,000 | 10.06 | 2.0% | 5.3% | 10% | 21% | 29% | 37% | 48% | 58% | 70% | 8.3% |
| 8, two comms | 16 | 5,000 | 9.81 | 2.5% | 6.8% | 13% | 24% | 33% | 41% | 52% | 62% | 74% | 5.7% |
| 8, two comms | 18 | 5,000 | 9.64 | 3.3% | 7.2% | 14% | 26% | 36% | 45% | 55% | 66% | 78% | 4.0% |
| 8, two comms | 20 | 5,000 | 9.34 | 3.6% | 8.7% | 16% | 29% | 39% | 50% | 61% | 71% | 81% | 3.0% |
| 8, two comms | 22 | 5,000 | 9.13 | 4.5% | 10% | 18% | 32% | 42% | 53% | 64% | 75% | 85% | 2.2% |
| 8, two comms | 24 | 5,000 | 8.97 | 4.2% | 10% | 18% | 34% | 45% | 56% | 67% | 78% | 88% | 1.5% |
| 8, two comms | 26 | 5,000 | 8.69 | 5.2% | 11% | 21% | 38% | 49% | 59% | 71% | 81% | 90% | 1.3% |
| 8, two comms | 28 | 5,000 | 8.56 | 6.1% | 13% | 23% | 40% | 50% | 62% | 73% | 82% | 91% | 0.94% |
| 8, two comms | 30 | 5,000 | 8.42 | 5.7% | 13% | 24% | 41% | 53% | 64% | 76% | 85% | 93% | 0.64% |
| 8, one alg | 10 | 20,000 | 6.52 | 1.8% | 4.0% | 7.3% | 15% | 20% | 20% | 20% | 20% | 20% | 80% |
| 8, one alg | 12 | 20,000 | 6.41 | 2.2% | 5.0% | 9.1% | 18% | 23% | 23% | 23% | 23% | 23% | 78% |
| 8, one alg | 14 | 20,000 | 6.38 | 2.5% | 5.7% | 10% | 20% | 25% | 25% | 25% | 25% | 25% | 75% |
| 8, one alg | 16 | 20,000 | 6.35 | 2.8% | 6.7% | 12% | 22% | 27% | 27% | 27% | 27% | 27% | 73% |
| 8, one alg | 18 | 20,000 | 6.30 | 3.5% | 7.4% | 13% | 24% | 29% | 29% | 29% | 29% | 29% | 71% |
| 8, one alg | 20 | 20,000 | 6.31 | 3.6% | 8.3% | 15% | 26% | 32% | 32% | 32% | 32% | 32% | 68% |
| 8, one alg | 22 | 20,000 | 6.30 | 3.9% | 8.7% | 15% | 28% | 34% | 34% | 34% | 34% | 34% | 66% |
| 8, one alg | 24 | 20,000 | 6.29 | 4.2% | 9.3% | 17% | 30% | 37% | 37% | 37% | 37% | 37% | 63% |
| 8, one alg | 26 | 20,000 | 6.25 | 5.0% | 10% | 18% | 33% | 40% | 40% | 40% | 40% | 40% | 60% |
| 8, one alg | 28 | 20,000 | 6.25 | 4.9% | 11% | 19% | 34% | 41% | 41% | 41% | 41% | 41% | 59% |
| 8, one alg | 30 | 20,000 | 6.21 | 5.8% | 12% | 21% | 36% | 43% | 43% | 43% | 43% | 43% | 57% |
| 8, best of the two | 10 | 5,000 | 10.51 | 1.8% | 3.8% | 7.8% | 17% | 24% | 30% | 38% | 47% | 58% | 15% |
| 8, best of the two | 12 | 5,000 | 10.25 | 2.6% | 5.2% | 10% | 20% | 27% | 34% | 43% | 52% | 64% | 11% |
| 8, best of the two | 14 | 5,000 | 10.02 | 2.4% | 5.7% | 11% | 22% | 29% | 38% | 48% | 58% | 70% | 8.3% |
| 8, best of the two | 16 | 5,000 | 9.75 | 2.9% | 7.3% | 13% | 25% | 34% | 42% | 53% | 63% | 75% | 5.6% |
| 8, best of the two | 18 | 5,000 | 9.60 | 3.8% | 7.8% | 14% | 27% | 36% | 46% | 56% | 66% | 78% | 4.0% |
| 8, best of the two | 20 | 5,000 | 9.29 | 4.3% | 9.6% | 17% | 30% | 40% | 50% | 61% | 72% | 82% | 3.0% |
| 8, best of the two | 22 | 5,000 | 9.08 | 5.0% | 11% | 19% | 33% | 43% | 53% | 64% | 75% | 85% | 2.2% |
| 8, best of the two | 24 | 5,000 | 8.92 | 4.7% | 11% | 19% | 34% | 45% | 56% | 67% | 78% | 88% | 1.5% |
| 8, best of the two | 26 | 5,000 | 8.64 | 6.1% | 12% | 22% | 38% | 50% | 60% | 71% | 81% | 90% | 1.3% |
| 8, best of the two | 28 | 5,000 | 8.50 | 7.0% | 14% | 23% | 40% | 51% | 62% | 73% | 83% | 91% | 0.92% |
| 8, best of the two | 30 | 5,000 | 8.36 | 6.5% | 14% | 25% | 41% | 54% | 65% | 77% | 85% | 93% | 0.64% |
| 10, two comms | 10 | 200 | 8.65 | 3.5% | 6.5% | 10% | 24% | 38% | 63% | 90% | 99% | 100% | 0 |
| 10, two comms | 12 | 200 | 8.48 | 2.0% | 4.0% | 12% | 25% | 43% | 72% | 94% | 99.5% | 100% | 0 |
| 10, two comms | 14 | 200 | 8.31 | 2.0% | 5.5% | 13% | 25% | 50% | 77% | 96% | 100% | 100% | 0 |
| 10, two comms | 16 | 200 | 8.07 | 3.5% | 8.5% | 17% | 29% | 49% | 84% | 99% | 100% | 100% | 0 |
| 10, two comms | 18 | 200 | 7.93 | 5.0% | 10% | 17% | 34% | 57% | 85% | 99% | 100% | 100% | 0 |
| 10, two comms | 20 | 200 | 7.90 | 4.5% | 11% | 19% | 33% | 56% | 87% | 99% | 100% | 100% | 0 |
| 10, two comms | 22 | 200 | 7.84 | 3.5% | 9.0% | 19% | 39% | 58% | 88% | 100% | 100% | 100% | 0 |
| 10, two comms | 24 | 200 | 7.51 | 8.0% | 15% | 26% | 43% | 67% | 89% | 98% | 100% | 100% | 0 |
| 10, two comms | 26 | 200 | 7.29 | 7.0% | 18% | 27% | 49% | 73% | 94% | 100% | 100% | 100% | 0 |
| 10, two comms | 28 | 200 | 7.12 | 8.5% | 17% | 32% | 57% | 76% | 96% | 99% | 100% | 100% | 0 |
| 10, two comms | 30 | 200 | 7.35 | 9.0% | 14% | 27% | 50% | 70% | 95% | 100% | 100% | 100% | 0 |
| 10, one alg | 10 | 20,000 | 8.29 | 2.0% | 4.6% | 9.0% | 19% | 35% | 61% | 77% | 77% | 77% | 23% |
| 10, one alg | 12 | 20,000 | 8.17 | 2.6% | 5.8% | 11% | 22% | 40% | 67% | 82% | 82% | 82% | 18% |
| 10, one alg | 14 | 20,000 | 8.07 | 2.8% | 6.5% | 13% | 25% | 44% | 72% | 86% | 86% | 86% | 14% |
| 10, one alg | 16 | 20,000 | 7.99 | 3.3% | 7.7% | 14% | 28% | 48% | 76% | 89% | 89% | 89% | 11% |
| 10, one alg | 18 | 20,000 | 7.89 | 3.9% | 8.5% | 16% | 30% | 51% | 80% | 91% | 91% | 91% | 8.9% |
| 10, one alg | 20 | 20,000 | 7.80 | 4.1% | 9.5% | 18% | 33% | 55% | 82% | 93% | 93% | 93% | 7.2% |
| 10, one alg | 22 | 20,000 | 7.73 | 4.5% | 10% | 19% | 35% | 58% | 85% | 94% | 94% | 94% | 5.9% |
| 10, one alg | 24 | 20,000 | 7.65 | 4.7% | 11% | 20% | 38% | 61% | 87% | 95% | 95% | 95% | 4.7% |
| 10, one alg | 26 | 20,000 | 7.54 | 5.6% | 12% | 22% | 41% | 64% | 89% | 97% | 97% | 97% | 3.5% |
| 10, one alg | 28 | 20,000 | 7.48 | 5.7% | 12% | 23% | 42% | 66% | 91% | 97% | 97% | 97% | 3.1% |
| 10, one alg | 30 | 20,000 | 7.40 | 6.4% | 14% | 25% | 45% | 69% | 92% | 98% | 98% | 98% | 2.3% |
| 10, best of the two | 10 | 200 | 8.42 | 4.0% | 7.0% | 11% | 27% | 45% | 71% | 93% | 99.5% | 100% | 0 |
| 10, best of the two | 12 | 200 | 8.20 | 3.0% | 5.5% | 15% | 29% | 51% | 78% | 97% | 100% | 100% | 0 |
| 10, best of the two | 14 | 200 | 8.00 | 2.5% | 6.5% | 16% | 32% | 61% | 85% | 97% | 100% | 100% | 0 |
| 10, best of the two | 16 | 200 | 7.79 | 5.5% | 12% | 20% | 36% | 56% | 89% | 99.5% | 100% | 100% | 0 |
| 10, best of the two | 18 | 200 | 7.64 | 5.0% | 10% | 20% | 39% | 69% | 93% | 100% | 100% | 100% | 0 |
| 10, best of the two | 20 | 200 | 7.63 | 5.5% | 12% | 22% | 37% | 66% | 92% | 99.5% | 100% | 100% | 0 |
| 10, best of the two | 22 | 200 | 7.60 | 3.5% | 11% | 23% | 42% | 66% | 95% | 100% | 100% | 100% | 0 |
| 10, best of the two | 24 | 200 | 7.29 | 9.5% | 16% | 27% | 46% | 75% | 95% | 100% | 100% | 100% | 0 |
| 10, best of the two | 26 | 200 | 7.08 | 9.0% | 19% | 30% | 55% | 78% | 96% | 100% | 100% | 100% | 0 |
| 10, best of the two | 28 | 200 | 6.87 | 12% | 20% | 36% | 61% | 81% | 98% | 100% | 100% | 100% | 0 |
| 10, best of the two | 30 | 200 | 7.08 | 9.5% | 15% | 32% | 57% | 79% | 98% | 100% | 100% | 100% | 0 |
| 12, one alg | 10 | 20,000 | 8.27 | 2.4% | 5.5% | 11% | 26% | 49% | 80% | 97% | 99.9% | 100% | 0 |
| 12, one alg | 12 | 20,000 | 8.06 | 3.1% | 6.8% | 14% | 29% | 55% | 86% | 98% | 99.9% | 100% | 0 |
| 12, one alg | 14 | 20,000 | 7.88 | 3.4% | 7.8% | 16% | 33% | 61% | 89% | 99.2% | 99.9% | 100% | 0 |
| 12, one alg | 16 | 20,000 | 7.72 | 4.0% | 9.3% | 19% | 37% | 66% | 92% | 99.6% | 100% | 100% | 0 |
| 12, one alg | 18 | 20,000 | 7.59 | 4.5% | 10% | 20% | 40% | 69% | 94% | 99.7% | 100% | 100% | 0 |
| 12, one alg | 20 | 20,000 | 7.45 | 4.9% | 11% | 23% | 44% | 74% | 96% | 99.9% | 100% | 100% | 0 |
| 12, one alg | 22 | 20,000 | 7.35 | 5.4% | 12% | 24% | 47% | 77% | 97% | 99.9% | 100% | 100% | 0 |
| 12, one alg | 24 | 20,000 | 7.25 | 5.8% | 13% | 26% | 50% | 80% | 98% | 99.9% | 100% | 100% | 0 |
| 12, one alg | 26 | 20,000 | 7.14 | 6.7% | 14% | 28% | 53% | 82% | 98% | 99.9% | 100% | 100% | 0 |
| 12, one alg | 28 | 20,000 | 7.06 | 6.9% | 15% | 29% | 55% | 84% | 99% | 99.9% | 100% | 100% | 0 |
| 12, one alg | 30 | 20,000 | 6.97 | 7.6% | 16% | 32% | 58% | 86% | 99% | 100% | 100% | 100% | 0 |

**Flipped 2e2e** (two swaps, each with a flip): one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 5,000 | 12.42 | 0 of 5,000 | 0.02% | 0.12% | 0.42% | 1.3% | 3.6% | 8.1% | 15% | 26% | 44% |
| 8, two comms | 12 | 5,000 | 12.22 | 0.02% | 0.04% | 0.28% | 0.70% | 2.1% | 5.0% | 11% | 21% | 35% | 33% |
| 8, two comms | 14 | 5,000 | 11.85 | 0.04% | 0.12% | 0.40% | 1.2% | 3.6% | 8.7% | 17% | 30% | 46% | 25% |
| 8, two comms | 16 | 5,000 | 11.62 | 0.04% | 0.22% | 0.72% | 2.0% | 4.8% | 11% | 22% | 36% | 54% | 17% |
| 8, two comms | 18 | 5,000 | 11.31 | 0.14% | 0.38% | 1.2% | 3.0% | 6.2% | 15% | 28% | 45% | 63% | 13% |
| 8, two comms | 20 | 5,000 | 11.08 | 0.30% | 0.74% | 1.8% | 3.7% | 8.9% | 18% | 33% | 51% | 69% | 9.3% |
| 8, two comms | 22 | 5,000 | 10.90 | 0.28% | 0.54% | 1.7% | 4.8% | 10% | 21% | 37% | 56% | 74% | 6.3% |
| 8, two comms | 24 | 5,000 | 10.63 | 0.20% | 0.84% | 2.3% | 5.7% | 12% | 25% | 44% | 64% | 80% | 4.3% |
| 8, two comms | 26 | 5,000 | 10.36 | 0.40% | 1.1% | 2.8% | 6.8% | 15% | 30% | 50% | 70% | 86% | 2.7% |
| 8, two comms | 28 | 5,000 | 10.09 | 0.60% | 1.6% | 4.2% | 9.2% | 19% | 36% | 56% | 75% | 89% | 1.8% |
| 8, two comms | 30 | 5,000 | 9.93 | 0.48% | 1.7% | 4.5% | 10% | 21% | 38% | 60% | 79% | 91% | 1.3% |
| 8, best of the two | 10 | 5,000 | 12.42 | 0 of 5,000 | 0.02% | 0.12% | 0.42% | 1.3% | 3.6% | 8.1% | 15% | 26% | 44% |
| 8, best of the two | 12 | 5,000 | 12.22 | 0.02% | 0.04% | 0.28% | 0.70% | 2.1% | 5.0% | 11% | 21% | 35% | 33% |
| 8, best of the two | 14 | 5,000 | 11.85 | 0.04% | 0.12% | 0.40% | 1.2% | 3.6% | 8.7% | 17% | 30% | 46% | 25% |
| 8, best of the two | 16 | 5,000 | 11.62 | 0.04% | 0.22% | 0.72% | 2.0% | 4.8% | 11% | 22% | 36% | 54% | 17% |
| 8, best of the two | 18 | 5,000 | 11.31 | 0.14% | 0.38% | 1.2% | 3.0% | 6.2% | 15% | 28% | 45% | 63% | 13% |
| 8, best of the two | 20 | 5,000 | 11.08 | 0.30% | 0.74% | 1.8% | 3.7% | 8.9% | 18% | 33% | 51% | 69% | 9.3% |
| 8, best of the two | 22 | 5,000 | 10.90 | 0.28% | 0.54% | 1.7% | 4.8% | 10% | 21% | 37% | 56% | 74% | 6.3% |
| 8, best of the two | 24 | 5,000 | 10.63 | 0.20% | 0.84% | 2.3% | 5.7% | 12% | 25% | 44% | 64% | 80% | 4.3% |
| 8, best of the two | 26 | 5,000 | 10.36 | 0.40% | 1.1% | 2.8% | 6.8% | 15% | 30% | 50% | 70% | 86% | 2.7% |
| 8, best of the two | 28 | 5,000 | 10.09 | 0.60% | 1.6% | 4.2% | 9.2% | 19% | 36% | 56% | 75% | 89% | 1.8% |
| 8, best of the two | 30 | 5,000 | 9.93 | 0.48% | 1.7% | 4.5% | 10% | 21% | 38% | 60% | 79% | 91% | 1.3% |
| 10, two comms | 10 | 200 | 9.09 | 0 of 200 | 1.0% | 3.5% | 10% | 29% | 62% | 87% | 99.5% | 100% | 0 |
| 10, two comms | 12 | 200 | 8.94 | 0.50% | 1.5% | 4.5% | 11% | 33% | 66% | 91% | 100% | 100% | 0 |
| 10, two comms | 14 | 200 | 8.79 | 0 of 200 | 1.0% | 4.0% | 15% | 37% | 73% | 92% | 100% | 100% | 0 |
| 10, two comms | 16 | 200 | 8.42 | 1.0% | 2.0% | 7.0% | 20% | 49% | 81% | 98% | 100% | 100% | 0 |
| 10, two comms | 18 | 200 | 8.53 | 0.50% | 2.5% | 7.0% | 21% | 43% | 76% | 98% | 100% | 100% | 0 |
| 10, two comms | 20 | 200 | 8.07 | 1.0% | 4.0% | 13% | 29% | 56% | 92% | 100% | 100% | 100% | 0 |
| 10, two comms | 22 | 200 | 8.02 | 1.0% | 4.0% | 14% | 30% | 62% | 88% | 99.5% | 100% | 100% | 0 |
| 10, two comms | 24 | 200 | 8.00 | 1.0% | 4.0% | 14% | 31% | 63% | 89% | 99.5% | 100% | 100% | 0 |
| 10, two comms | 26 | 200 | 7.95 | 0 of 200 | 3.5% | 13% | 34% | 62% | 94% | 100% | 100% | 100% | 0 |
| 10, two comms | 28 | 200 | 7.72 | 1.0% | 2.5% | 19% | 38% | 74% | 95% | 100% | 100% | 100% | 0 |
| 10, two comms | 30 | 200 | 7.76 | 1.5% | 8.5% | 17% | 37% | 68% | 94% | 100% | 100% | 100% | 0 |
| 10, one alg | 10 | 20,000 | 8.80 | 0.25% | 0.87% | 3.2% | 9.7% | 28% | 57% | 83% | 83% | 83% | 17% |
| 10, one alg | 12 | 20,000 | 8.70 | 0.27% | 0.91% | 3.7% | 12% | 33% | 65% | 88% | 88% | 88% | 12% |
| 10, one alg | 14 | 20,000 | 8.61 | 0.38% | 1.1% | 4.3% | 14% | 37% | 70% | 91% | 91% | 91% | 9.2% |
| 10, one alg | 16 | 20,000 | 8.51 | 0.48% | 1.4% | 5.2% | 16% | 42% | 74% | 94% | 94% | 94% | 6.4% |
| 10, one alg | 18 | 20,000 | 8.43 | 0.33% | 1.4% | 5.7% | 17% | 46% | 78% | 95% | 95% | 95% | 5.2% |
| 10, one alg | 20 | 20,000 | 8.37 | 0.60% | 1.8% | 6.3% | 19% | 48% | 81% | 96% | 96% | 96% | 3.6% |
| 10, one alg | 22 | 20,000 | 8.29 | 0.44% | 1.8% | 6.7% | 21% | 52% | 84% | 97% | 97% | 97% | 2.9% |
| 10, one alg | 24 | 20,000 | 8.21 | 0.67% | 2.3% | 7.7% | 23% | 55% | 87% | 98% | 98% | 98% | 2.1% |
| 10, one alg | 26 | 20,000 | 8.13 | 0.64% | 2.2% | 8.4% | 25% | 59% | 89% | 98% | 98% | 98% | 1.6% |
| 10, one alg | 28 | 20,000 | 8.09 | 0.67% | 2.4% | 8.8% | 26% | 61% | 90% | 99% | 99% | 99% | 1.1% |
| 10, one alg | 30 | 20,000 | 8.02 | 0.90% | 2.7% | 9.7% | 28% | 63% | 91% | 99.2% | 99.2% | 99.2% | 0.78% |
| 10, best of the two | 10 | 200 | 8.69 | 0 of 200 | 1.5% | 5.0% | 15% | 40% | 78% | 93% | 100% | 100% | 0 |
| 10, best of the two | 12 | 200 | 8.58 | 0.50% | 2.0% | 6.0% | 16% | 46% | 78% | 95% | 100% | 100% | 0 |
| 10, best of the two | 14 | 200 | 8.43 | 0 of 200 | 1.5% | 5.5% | 21% | 50% | 83% | 97% | 100% | 100% | 0 |
| 10, best of the two | 16 | 200 | 8.08 | 1.0% | 2.0% | 9.0% | 27% | 62% | 89% | 100% | 100% | 100% | 0 |
| 10, best of the two | 18 | 200 | 8.14 | 0.50% | 3.5% | 9.5% | 28% | 57% | 90% | 99% | 100% | 100% | 0 |
| 10, best of the two | 20 | 200 | 7.83 | 1.0% | 4.0% | 16% | 36% | 65% | 96% | 100% | 100% | 100% | 0 |
| 10, best of the two | 22 | 200 | 7.71 | 1.0% | 5.0% | 16% | 39% | 74% | 94% | 99.5% | 100% | 100% | 0 |
| 10, best of the two | 24 | 200 | 7.72 | 1.5% | 4.5% | 16% | 36% | 74% | 96% | 100% | 100% | 100% | 0 |
| 10, best of the two | 26 | 200 | 7.65 | 1.0% | 4.5% | 18% | 42% | 73% | 99% | 100% | 100% | 100% | 0 |
| 10, best of the two | 28 | 200 | 7.47 | 1.0% | 2.5% | 22% | 45% | 84% | 99.5% | 100% | 100% | 100% | 0 |
| 10, best of the two | 30 | 200 | 7.45 | 1.5% | 9.0% | 20% | 45% | 83% | 98% | 100% | 100% | 100% | 0 |
| 12, one alg | 10 | 20,000 | 8.74 | 0.40% | 1.4% | 4.9% | 14% | 38% | 71% | 95% | 99.9% | 100% | 0 |
| 12, one alg | 12 | 20,000 | 8.56 | 0.45% | 1.5% | 5.8% | 17% | 44% | 78% | 97% | 99.9% | 100% | 0 |
| 12, one alg | 14 | 20,000 | 8.41 | 0.57% | 1.8% | 6.8% | 20% | 49% | 83% | 98% | 99.9% | 100% | 0 |
| 12, one alg | 16 | 20,000 | 8.26 | 0.71% | 2.2% | 7.9% | 23% | 54% | 87% | 99.1% | 99.9% | 100% | 0 |
| 12, one alg | 18 | 20,000 | 8.15 | 0.65% | 2.4% | 8.8% | 25% | 58% | 90% | 99.4% | 99.9% | 100% | 0 |
| 12, one alg | 20 | 20,000 | 8.05 | 1.1% | 2.9% | 9.9% | 28% | 62% | 92% | 99.6% | 100% | 100% | 0 |
| 12, one alg | 22 | 20,000 | 7.96 | 0.82% | 3.1% | 11% | 30% | 66% | 93% | 99.7% | 100% | 100% | 0 |
| 12, one alg | 24 | 20,000 | 7.86 | 1.1% | 3.6% | 12% | 33% | 69% | 95% | 99.9% | 100% | 100% | 0 |
| 12, one alg | 26 | 20,000 | 7.78 | 1.1% | 3.8% | 13% | 35% | 73% | 96% | 99.9% | 100% | 100% | 0 |
| 12, one alg | 28 | 20,000 | 7.73 | 1.2% | 4.1% | 14% | 37% | 74% | 97% | 99.9% | 100% | 100% | 0 |
| 12, one alg | 30 | 20,000 | 7.64 | 1.6% | 4.5% | 15% | 40% | 77% | 98% | 99.9% | 100% | 100% | 0 |

**3e1f** (a flipped 3-cycle and one flipped edge): one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 20,000 | 12.68 | 0 of 20,000 | 0.02% | 0.07% | 0.18% | 0.48% | 1.2% | 2.9% | 5.9% | 11% | 73% |
| 8, two comms | 12 | 20,000 | 12.47 | 0 of 20,000 | 0.04% | 0.11% | 0.35% | 0.98% | 2.2% | 4.6% | 9.1% | 16% | 65% |
| 8, two comms | 14 | 20,000 | 12.31 | 0.02% | 0.07% | 0.18% | 0.50% | 1.4% | 3.2% | 7.0% | 13% | 21% | 57% |
| 8, two comms | 16 | 20,000 | 12.15 | 0.03% | 0.10% | 0.30% | 0.82% | 2.0% | 4.4% | 8.9% | 16% | 26% | 51% |
| 8, two comms | 18 | 20,000 | 12.00 | 0.04% | 0.11% | 0.27% | 1.0% | 2.5% | 5.7% | 11% | 20% | 31% | 45% |
| 8, two comms | 20 | 20,000 | 11.82 | 0.07% | 0.21% | 0.54% | 1.4% | 3.4% | 7.3% | 14% | 24% | 36% | 40% |
| 8, two comms | 22 | 20,000 | 11.67 | 0.11% | 0.31% | 0.69% | 1.9% | 4.2% | 8.9% | 17% | 28% | 42% | 34% |
| 8, two comms | 24 | 20,000 | 11.52 | 0.10% | 0.32% | 0.94% | 2.4% | 5.4% | 11% | 20% | 33% | 47% | 29% |
| 8, two comms | 26 | 20,000 | 11.40 | 0.15% | 0.44% | 1.0% | 2.8% | 6.1% | 13% | 23% | 37% | 51% | 25% |
| 8, two comms | 28 | 20,000 | 11.27 | 0.20% | 0.47% | 1.4% | 3.2% | 7.0% | 14% | 26% | 40% | 56% | 22% |
| 8, two comms | 30 | 20,000 | 11.13 | 0.22% | 0.60% | 1.5% | 3.8% | 8.7% | 17% | 29% | 44% | 60% | 18% |
| 8, best of the two | 10 | 20,000 | 12.68 | 0 of 20,000 | 0.02% | 0.07% | 0.18% | 0.48% | 1.2% | 2.9% | 5.9% | 11% | 73% |
| 8, best of the two | 12 | 20,000 | 12.47 | 0 of 20,000 | 0.04% | 0.11% | 0.35% | 0.98% | 2.2% | 4.6% | 9.1% | 16% | 65% |
| 8, best of the two | 14 | 20,000 | 12.31 | 0.02% | 0.07% | 0.18% | 0.50% | 1.4% | 3.2% | 7.0% | 13% | 21% | 57% |
| 8, best of the two | 16 | 20,000 | 12.15 | 0.03% | 0.10% | 0.30% | 0.82% | 2.0% | 4.4% | 8.9% | 16% | 26% | 51% |
| 8, best of the two | 18 | 20,000 | 12.00 | 0.04% | 0.11% | 0.27% | 1.0% | 2.5% | 5.7% | 11% | 20% | 31% | 45% |
| 8, best of the two | 20 | 20,000 | 11.82 | 0.07% | 0.21% | 0.54% | 1.4% | 3.4% | 7.3% | 14% | 24% | 36% | 40% |
| 8, best of the two | 22 | 20,000 | 11.67 | 0.11% | 0.31% | 0.69% | 1.9% | 4.2% | 8.9% | 17% | 28% | 42% | 34% |
| 8, best of the two | 24 | 20,000 | 11.52 | 0.10% | 0.32% | 0.94% | 2.4% | 5.4% | 11% | 20% | 33% | 47% | 29% |
| 8, best of the two | 26 | 20,000 | 11.40 | 0.15% | 0.44% | 1.0% | 2.8% | 6.1% | 13% | 23% | 37% | 51% | 25% |
| 8, best of the two | 28 | 20,000 | 11.27 | 0.20% | 0.47% | 1.4% | 3.2% | 7.0% | 14% | 26% | 40% | 56% | 22% |
| 8, best of the two | 30 | 20,000 | 11.13 | 0.22% | 0.60% | 1.5% | 3.8% | 8.7% | 17% | 29% | 44% | 60% | 18% |
| 10, two comms | 10 | 500 | 10.92 | 0 of 500 | 0.20% | 0.40% | 1.6% | 6.0% | 13% | 34% | 64% | 90% | 0 |
| 10, two comms | 12 | 500 | 10.75 | 0.20% | 0.20% | 0.40% | 2.2% | 8.2% | 16% | 36% | 69% | 94% | 0 |
| 10, two comms | 14 | 500 | 10.42 | 0 of 500 | 0.20% | 1.2% | 3.2% | 8.2% | 21% | 48% | 79% | 97% | 0 |
| 10, two comms | 16 | 500 | 10.28 | 0 of 500 | 0.80% | 1.8% | 5.0% | 11% | 26% | 49% | 79% | 99% | 0 |
| 10, two comms | 18 | 500 | 10.16 | 0 of 500 | 0.20% | 1.2% | 3.0% | 13% | 28% | 57% | 84% | 98% | 0 |
| 10, two comms | 20 | 500 | 9.85 | 0 of 500 | 1.4% | 3.2% | 8.0% | 17% | 37% | 62% | 87% | 99.4% | 0 |
| 10, two comms | 22 | 500 | 9.80 | 0 of 500 | 0.80% | 2.6% | 7.4% | 18% | 36% | 64% | 92% | 100% | 0 |
| 10, two comms | 24 | 500 | 9.62 | 0.40% | 0.40% | 3.2% | 6.8% | 19% | 43% | 72% | 94% | 99.8% | 0 |
| 10, two comms | 26 | 500 | 9.51 | 0.40% | 1.6% | 3.0% | 7.4% | 23% | 44% | 74% | 96% | 100% | 0 |
| 10, two comms | 28 | 500 | 9.45 | 0.60% | 1.4% | 4.0% | 9.4% | 23% | 48% | 73% | 94% | 100% | 0 |
| 10, two comms | 30 | 500 | 9.28 | 1.0% | 2.8% | 5.2% | 13% | 28% | 50% | 78% | 95% | 100% | 0 |
| 10, best of the two | 10 | 500 | 10.92 | 0 of 500 | 0.20% | 0.40% | 1.6% | 6.0% | 13% | 34% | 64% | 90% | 0 |
| 10, best of the two | 12 | 500 | 10.75 | 0.20% | 0.20% | 0.40% | 2.2% | 8.2% | 16% | 36% | 69% | 94% | 0 |
| 10, best of the two | 14 | 500 | 10.42 | 0 of 500 | 0.20% | 1.2% | 3.2% | 8.2% | 21% | 48% | 79% | 97% | 0 |
| 10, best of the two | 16 | 500 | 10.28 | 0 of 500 | 0.80% | 1.8% | 5.0% | 11% | 26% | 49% | 79% | 99% | 0 |
| 10, best of the two | 18 | 500 | 10.16 | 0 of 500 | 0.20% | 1.2% | 3.0% | 13% | 28% | 57% | 84% | 98% | 0 |
| 10, best of the two | 20 | 500 | 9.85 | 0 of 500 | 1.4% | 3.2% | 8.0% | 17% | 37% | 62% | 87% | 99.4% | 0 |
| 10, best of the two | 22 | 500 | 9.80 | 0 of 500 | 0.80% | 2.6% | 7.4% | 18% | 36% | 64% | 92% | 100% | 0 |
| 10, best of the two | 24 | 500 | 9.62 | 0.40% | 0.40% | 3.2% | 6.8% | 19% | 43% | 72% | 94% | 99.8% | 0 |
| 10, best of the two | 26 | 500 | 9.51 | 0.40% | 1.6% | 3.0% | 7.4% | 23% | 44% | 74% | 96% | 100% | 0 |
| 10, best of the two | 28 | 500 | 9.45 | 0.60% | 1.4% | 4.0% | 9.4% | 23% | 48% | 73% | 94% | 100% | 0 |
| 10, best of the two | 30 | 500 | 9.28 | 1.0% | 2.8% | 5.2% | 13% | 28% | 50% | 78% | 95% | 100% | 0 |
| 12, one alg | 10 | 20,000 | 10.91 | <0.01% | 0.03% | 0.15% | 0.70% | 2.6% | 8.5% | 27% | 60% | 91% | 8.6% |
| 12, one alg | 12 | 20,000 | 10.81 | 0.01% | 0.06% | 0.26% | 0.80% | 2.9% | 10% | 32% | 67% | 94% | 5.6% |
| 12, one alg | 14 | 20,000 | 10.71 | <0.01% | 0.06% | 0.26% | 0.97% | 3.7% | 12% | 36% | 71% | 96% | 4.3% |
| 12, one alg | 16 | 20,000 | 10.62 | 0.06% | 0.11% | 0.37% | 1.2% | 4.1% | 13% | 39% | 76% | 97% | 2.6% |
| 12, one alg | 18 | 20,000 | 10.51 | 0.04% | 0.11% | 0.40% | 1.3% | 5.1% | 16% | 44% | 80% | 98% | 1.6% |
| 12, one alg | 20 | 20,000 | 10.43 | 0.03% | 0.13% | 0.48% | 1.6% | 5.5% | 17% | 47% | 83% | 99% | 1.1% |
| 12, one alg | 22 | 20,000 | 10.36 | 0.02% | 0.11% | 0.36% | 1.5% | 6.0% | 19% | 50% | 86% | 99.3% | 0.66% |
| 12, one alg | 24 | 20,000 | 10.26 | 0.03% | 0.13% | 0.51% | 2.1% | 7.1% | 21% | 54% | 89% | 99.5% | 0.52% |
| 12, one alg | 26 | 20,000 | 10.20 | 0.06% | 0.16% | 0.48% | 2.0% | 7.1% | 22% | 57% | 91% | 99.7% | 0.28% |
| 12, one alg | 28 | 20,000 | 10.16 | 0.07% | 0.19% | 0.63% | 2.2% | 7.9% | 23% | 58% | 91% | 99.8% | 0.24% |
| 12, one alg | 30 | 20,000 | 10.09 | 0.04% | 0.20% | 0.61% | 2.3% | 8.4% | 25% | 62% | 93% | 99.8% | 0.18% |

**5e**: one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 20,000 | 12.22 | 0.01% | 0.04% | 0.21% | 0.70% | 2.1% | 5.0% | 10% | 19% | 30% | 45% |
| 8, two comms | 12 | 20,000 | 12.05 | 0.05% | 0.14% | 0.45% | 1.3% | 2.9% | 6.3% | 13% | 23% | 34% | 40% |
| 8, two comms | 14 | 20,000 | 11.93 | 0.08% | 0.21% | 0.56% | 1.5% | 3.7% | 8.0% | 16% | 26% | 39% | 34% |
| 8, two comms | 16 | 20,000 | 11.81 | 0.11% | 0.24% | 0.68% | 1.9% | 4.5% | 9.0% | 18% | 30% | 43% | 30% |
| 8, two comms | 18 | 20,000 | 11.67 | 0.10% | 0.35% | 0.92% | 2.3% | 5.3% | 11% | 20% | 33% | 47% | 26% |
| 8, two comms | 20 | 20,000 | 11.55 | 0.14% | 0.39% | 1.2% | 2.6% | 6.0% | 13% | 23% | 37% | 51% | 22% |
| 8, two comms | 22 | 20,000 | 11.46 | 0.16% | 0.44% | 1.1% | 3.1% | 7.0% | 14% | 25% | 40% | 55% | 19% |
| 8, two comms | 24 | 20,000 | 11.32 | 0.18% | 0.55% | 1.4% | 3.6% | 8.1% | 16% | 28% | 43% | 59% | 16% |
| 8, two comms | 26 | 20,000 | 11.21 | 0.25% | 0.66% | 1.7% | 4.2% | 8.9% | 17% | 30% | 47% | 62% | 14% |
| 8, two comms | 28 | 20,000 | 11.09 | 0.24% | 0.71% | 1.9% | 4.6% | 10% | 19% | 33% | 50% | 65% | 12% |
| 8, two comms | 30 | 20,000 | 10.96 | 0.31% | 0.93% | 2.3% | 5.3% | 11% | 21% | 36% | 53% | 68% | 10% |
| 8, one alg | 10 | 20,000 | 7.40 | 0.05% | 0.26% | 0.87% | 2.5% | 6.2% | 6.2% | 6.2% | 6.2% | 6.2% | 94% |
| 8, one alg | 12 | 20,000 | 7.38 | 0.08% | 0.35% | 0.97% | 3.1% | 7.4% | 7.4% | 7.4% | 7.4% | 7.4% | 93% |
| 8, one alg | 14 | 20,000 | 7.35 | 0.09% | 0.42% | 1.2% | 3.7% | 8.4% | 8.4% | 8.4% | 8.4% | 8.4% | 92% |
| 8, one alg | 16 | 20,000 | 7.36 | 0.15% | 0.41% | 1.4% | 3.9% | 9.2% | 9.2% | 9.2% | 9.2% | 9.2% | 91% |
| 8, one alg | 18 | 20,000 | 7.38 | 0.09% | 0.40% | 1.6% | 4.3% | 10% | 10% | 10% | 10% | 10% | 90% |
| 8, one alg | 20 | 20,000 | 7.35 | 0.12% | 0.58% | 1.8% | 4.9% | 11% | 11% | 11% | 11% | 11% | 89% |
| 8, one alg | 22 | 20,000 | 7.32 | 0.18% | 0.67% | 2.0% | 5.4% | 12% | 12% | 12% | 12% | 12% | 88% |
| 8, one alg | 24 | 20,000 | 7.31 | 0.16% | 0.73% | 2.3% | 6.0% | 13% | 13% | 13% | 13% | 13% | 87% |
| 8, one alg | 26 | 20,000 | 7.31 | 0.17% | 0.74% | 2.4% | 6.2% | 14% | 14% | 14% | 14% | 14% | 86% |
| 8, one alg | 28 | 20,000 | 7.37 | 0.18% | 0.64% | 2.3% | 6.5% | 15% | 15% | 15% | 15% | 15% | 85% |
| 8, one alg | 30 | 20,000 | 7.31 | 0.23% | 0.84% | 2.8% | 7.5% | 17% | 17% | 17% | 17% | 17% | 83% |
| 8, best of the two | 10 | 20,000 | 11.72 | 0.06% | 0.29% | 1.1% | 3.2% | 8.1% | 11% | 16% | 24% | 34% | 41% |
| 8, best of the two | 12 | 20,000 | 11.53 | 0.12% | 0.48% | 1.4% | 4.4% | 9.9% | 13% | 19% | 29% | 40% | 36% |
| 8, best of the two | 14 | 20,000 | 11.40 | 0.17% | 0.62% | 1.8% | 5.1% | 12% | 16% | 23% | 33% | 45% | 30% |
| 8, best of the two | 16 | 20,000 | 11.26 | 0.26% | 0.65% | 2.1% | 5.7% | 13% | 17% | 25% | 37% | 49% | 26% |
| 8, best of the two | 18 | 20,000 | 11.11 | 0.19% | 0.75% | 2.4% | 6.4% | 15% | 20% | 28% | 40% | 53% | 22% |
| 8, best of the two | 20 | 20,000 | 10.94 | 0.26% | 0.97% | 2.9% | 7.4% | 17% | 23% | 32% | 45% | 58% | 19% |
| 8, best of the two | 22 | 20,000 | 10.86 | 0.34% | 1.1% | 3.2% | 8.3% | 18% | 24% | 34% | 48% | 61% | 15% |
| 8, best of the two | 24 | 20,000 | 10.69 | 0.33% | 1.3% | 3.7% | 9.3% | 20% | 27% | 38% | 52% | 65% | 13% |
| 8, best of the two | 26 | 20,000 | 10.58 | 0.42% | 1.4% | 4.1% | 10% | 22% | 29% | 40% | 55% | 68% | 11% |
| 8, best of the two | 28 | 20,000 | 10.44 | 0.41% | 1.3% | 4.2% | 11% | 24% | 32% | 44% | 59% | 72% | 9.1% |
| 8, best of the two | 30 | 20,000 | 10.28 | 0.53% | 1.8% | 5.0% | 12% | 26% | 34% | 47% | 62% | 75% | 7.8% |
| 10, two comms | 10 | 500 | 10.61 | 0 of 500 | 0.20% | 0.60% | 2.0% | 6.0% | 19% | 42% | 74% | 95% | 0 |
| 10, two comms | 12 | 500 | 10.43 | 0 of 500 | 0 of 500 | 1.4% | 4.4% | 7.8% | 23% | 45% | 79% | 96% | 0 |
| 10, two comms | 14 | 500 | 10.19 | 0 of 500 | 0 of 500 | 1.8% | 5.4% | 12% | 27% | 54% | 83% | 98% | 0 |
| 10, two comms | 16 | 500 | 10.03 | 0.40% | 1.0% | 2.6% | 5.8% | 12% | 30% | 60% | 88% | 98% | 0 |
| 10, two comms | 18 | 500 | 9.87 | 0.20% | 1.2% | 2.2% | 5.4% | 15% | 36% | 63% | 90% | 99.8% | 0 |
| 10, two comms | 20 | 500 | 9.77 | 0.40% | 1.2% | 2.6% | 7.4% | 16% | 36% | 66% | 94% | 99.8% | 0 |
| 10, two comms | 22 | 500 | 9.66 | 0 of 500 | 0.20% | 2.4% | 7.8% | 19% | 43% | 68% | 94% | 100% | 0 |
| 10, two comms | 24 | 500 | 9.59 | 0.60% | 1.4% | 3.6% | 8.8% | 20% | 38% | 73% | 96% | 99.8% | 0 |
| 10, two comms | 26 | 500 | 9.43 | 0.80% | 1.2% | 4.2% | 11% | 22% | 45% | 77% | 96% | 99.8% | 0 |
| 10, two comms | 28 | 500 | 9.09 | 1.2% | 2.6% | 6.8% | 13% | 31% | 55% | 82% | 98% | 100% | 0 |
| 10, two comms | 30 | 500 | 9.15 | 0.60% | 1.8% | 6.6% | 15% | 29% | 52% | 81% | 99% | 100% | 0 |
| 10, one alg | 10 | 20,000 | 9.10 | 0.07% | 0.35% | 1.2% | 3.6% | 11% | 28% | 50% | 50% | 50% | 50% |
| 10, one alg | 12 | 20,000 | 9.04 | 0.12% | 0.48% | 1.5% | 4.8% | 14% | 32% | 55% | 55% | 55% | 45% |
| 10, one alg | 14 | 20,000 | 9.01 | 0.13% | 0.52% | 1.6% | 5.2% | 16% | 36% | 59% | 59% | 59% | 41% |
| 10, one alg | 16 | 20,000 | 8.98 | 0.20% | 0.57% | 2.0% | 5.9% | 17% | 39% | 63% | 63% | 63% | 37% |
| 10, one alg | 18 | 20,000 | 8.95 | 0.12% | 0.56% | 2.1% | 6.5% | 19% | 43% | 68% | 68% | 68% | 32% |
| 10, one alg | 20 | 20,000 | 8.90 | 0.21% | 0.78% | 2.4% | 7.3% | 21% | 46% | 71% | 71% | 71% | 29% |
| 10, one alg | 22 | 20,000 | 8.87 | 0.25% | 0.85% | 2.8% | 8.0% | 22% | 49% | 74% | 74% | 74% | 26% |
| 10, one alg | 24 | 20,000 | 8.83 | 0.21% | 1.0% | 3.2% | 8.9% | 24% | 52% | 77% | 77% | 77% | 23% |
| 10, one alg | 26 | 20,000 | 8.80 | 0.26% | 1.1% | 3.4% | 9.4% | 26% | 55% | 80% | 80% | 80% | 20% |
| 10, one alg | 28 | 20,000 | 8.78 | 0.31% | 1.0% | 3.4% | 9.9% | 27% | 58% | 82% | 82% | 82% | 18% |
| 10, one alg | 30 | 20,000 | 8.73 | 0.34% | 1.1% | 3.8% | 11% | 30% | 60% | 84% | 84% | 84% | 16% |
| 10, best of the two | 10 | 500 | 9.98 | 0 of 500 | 0.20% | 1.2% | 4.0% | 13% | 38% | 65% | 84% | 97% | 0 |
| 10, best of the two | 12 | 500 | 9.70 | 0.20% | 1.0% | 3.8% | 8.6% | 18% | 43% | 69% | 88% | 98% | 0 |
| 10, best of the two | 14 | 500 | 9.34 | 0.20% | 0.80% | 3.6% | 11% | 27% | 54% | 79% | 92% | 99% | 0 |
| 10, best of the two | 16 | 500 | 9.37 | 0.40% | 1.0% | 3.6% | 8.2% | 22% | 53% | 82% | 93% | 99% | 0 |
| 10, best of the two | 18 | 500 | 9.18 | 0.40% | 1.6% | 3.8% | 9.8% | 28% | 57% | 84% | 97% | 100% | 0 |
| 10, best of the two | 20 | 500 | 9.06 | 0.40% | 1.6% | 3.6% | 11% | 30% | 62% | 88% | 97% | 99.8% | 0 |
| 10, best of the two | 22 | 500 | 8.91 | 0.20% | 0.60% | 3.6% | 14% | 36% | 68% | 90% | 98% | 100% | 0 |
| 10, best of the two | 24 | 500 | 8.92 | 0.60% | 1.6% | 5.2% | 14% | 33% | 64% | 91% | 98% | 99.8% | 0 |
| 10, best of the two | 26 | 500 | 8.70 | 1.0% | 2.0% | 5.8% | 18% | 39% | 71% | 94% | 99% | 100% | 0 |
| 10, best of the two | 28 | 500 | 8.36 | 1.2% | 3.6% | 11% | 21% | 49% | 82% | 96% | 99% | 100% | 0 |
| 10, best of the two | 30 | 500 | 8.51 | 0.60% | 1.8% | 8.4% | 22% | 46% | 75% | 94% | 99.8% | 100% | 0 |
| 12, one alg | 10 | 20,000 | 9.74 | 0.09% | 0.50% | 1.7% | 5.2% | 15% | 37% | 70% | 95% | 99.6% | 0.37% |
| 12, one alg | 12 | 20,000 | 9.55 | 0.19% | 0.69% | 2.1% | 6.7% | 18% | 43% | 76% | 97% | 99.8% | 0.22% |
| 12, one alg | 14 | 20,000 | 9.43 | 0.21% | 0.75% | 2.4% | 7.4% | 21% | 46% | 80% | 98% | 99.9% | 0.07% |
| 12, one alg | 16 | 20,000 | 9.31 | 0.29% | 0.85% | 2.9% | 8.4% | 23% | 51% | 84% | 99% | 99.9% | 0.04% |
| 12, one alg | 18 | 20,000 | 9.18 | 0.27% | 0.93% | 3.1% | 9.4% | 26% | 56% | 88% | 99.4% | 99.9% | <0.01% |
| 12, one alg | 20 | 20,000 | 9.08 | 0.30% | 1.1% | 3.6% | 10% | 28% | 59% | 90% | 99.6% | 99.9% | 0.01% |
| 12, one alg | 22 | 20,000 | 8.99 | 0.34% | 1.2% | 4.0% | 11% | 30% | 62% | 91% | 99.8% | 100% | 0 |
| 12, one alg | 24 | 20,000 | 8.91 | 0.32% | 1.4% | 4.5% | 13% | 32% | 65% | 93% | 99.8% | 100% | 0 |
| 12, one alg | 26 | 20,000 | 8.82 | 0.41% | 1.6% | 5.0% | 14% | 35% | 68% | 95% | 99.9% | 100% | 0 |
| 12, one alg | 28 | 20,000 | 8.75 | 0.46% | 1.6% | 5.0% | 14% | 37% | 71% | 95% | 99.9% | 100% | 0 |
| 12, one alg | 30 | 20,000 | 8.68 | 0.52% | 1.6% | 5.6% | 16% | 39% | 73% | 96% | 99.9% | 100% | 0 |

**3e3e** (two separate edge 3-cycles): one row per cap, model and skeleton length.

| Cap and model | Skeleton length | Skeletons | Mean moves added | Adds 4 or less | Adds 5 or less | Adds 6 or less | Adds 7 or less | Adds 8 or less | Adds 9 or less | Adds 10 or less | Adds 11 or less | Adds 12 or less | Nothing fits |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, two comms | 10 | 20,000 | 12.21 | 0.02% | 0.07% | 0.17% | 0.43% | 1.2% | 2.6% | 5.2% | 10% | 19% | 65% |
| 8, two comms | 12 | 20,000 | 12.20 | 0.01% | 0.04% | 0.17% | 0.55% | 1.3% | 2.9% | 5.7% | 11% | 21% | 61% |
| 8, two comms | 14 | 20,000 | 12.07 | 0.06% | 0.11% | 0.29% | 0.73% | 1.8% | 3.8% | 7.3% | 14% | 25% | 57% |
| 8, two comms | 16 | 20,000 | 12.01 | 0.05% | 0.12% | 0.36% | 0.82% | 2.0% | 4.4% | 8.5% | 16% | 28% | 53% |
| 8, two comms | 18 | 20,000 | 11.90 | 0.05% | 0.17% | 0.50% | 1.1% | 2.7% | 5.5% | 10% | 18% | 31% | 49% |
| 8, two comms | 20 | 20,000 | 11.86 | 0.08% | 0.19% | 0.50% | 1.3% | 3.0% | 6.3% | 11% | 20% | 34% | 45% |
| 8, two comms | 22 | 20,000 | 11.81 | 0.06% | 0.24% | 0.60% | 1.5% | 3.3% | 6.7% | 12% | 22% | 37% | 41% |
| 8, two comms | 24 | 20,000 | 11.71 | 0.11% | 0.30% | 0.71% | 1.7% | 3.8% | 7.7% | 14% | 24% | 40% | 39% |
| 8, two comms | 26 | 20,000 | 11.63 | 0.12% | 0.33% | 0.99% | 2.0% | 4.5% | 8.9% | 16% | 27% | 42% | 36% |
| 8, two comms | 28 | 20,000 | 11.58 | 0.14% | 0.31% | 0.89% | 2.1% | 4.8% | 9.5% | 17% | 29% | 45% | 33% |
| 8, two comms | 30 | 20,000 | 11.47 | 0.21% | 0.51% | 1.2% | 2.7% | 5.7% | 11% | 19% | 31% | 48% | 30% |
| 8, one alg | 10 | 20,000 | 7.37 | 0.02% | 0.10% | 0.33% | 0.85% | 2.0% | 2.0% | 2.0% | 2.0% | 2.0% | 98% |
| 8, one alg | 12 | 20,000 | 7.35 | 0.03% | 0.12% | 0.33% | 1.0% | 2.3% | 2.3% | 2.3% | 2.3% | 2.3% | 98% |
| 8, one alg | 14 | 20,000 | 7.31 | 0.04% | 0.14% | 0.40% | 1.2% | 2.6% | 2.6% | 2.6% | 2.6% | 2.6% | 97% |
| 8, one alg | 16 | 20,000 | 7.31 | 0.04% | 0.15% | 0.54% | 1.4% | 3.1% | 3.1% | 3.1% | 3.1% | 3.1% | 97% |
| 8, one alg | 18 | 20,000 | 7.34 | 0.01% | 0.17% | 0.53% | 1.6% | 3.5% | 3.5% | 3.5% | 3.5% | 3.5% | 96% |
| 8, one alg | 20 | 20,000 | 7.33 | 0.04% | 0.18% | 0.59% | 1.6% | 3.6% | 3.6% | 3.6% | 3.6% | 3.6% | 96% |
| 8, one alg | 22 | 20,000 | 7.33 | 0.05% | 0.21% | 0.63% | 1.7% | 3.9% | 3.9% | 3.9% | 3.9% | 3.9% | 96% |
| 8, one alg | 24 | 20,000 | 7.34 | 0.06% | 0.19% | 0.65% | 2.0% | 4.3% | 4.3% | 4.3% | 4.3% | 4.3% | 96% |
| 8, one alg | 26 | 20,000 | 7.28 | 0.10% | 0.27% | 0.83% | 2.2% | 4.8% | 4.8% | 4.8% | 4.8% | 4.8% | 95% |
| 8, one alg | 28 | 20,000 | 7.27 | 0.06% | 0.28% | 0.96% | 2.4% | 5.1% | 5.1% | 5.1% | 5.1% | 5.1% | 95% |
| 8, one alg | 30 | 20,000 | 7.30 | 0.06% | 0.27% | 0.94% | 2.6% | 5.6% | 5.6% | 5.6% | 5.6% | 5.6% | 94% |
| 8, best of the two | 10 | 20,000 | 11.98 | 0.04% | 0.16% | 0.50% | 1.3% | 3.1% | 4.3% | 6.7% | 11% | 20% | 64% |
| 8, best of the two | 12 | 20,000 | 11.97 | 0.04% | 0.16% | 0.49% | 1.5% | 3.4% | 4.8% | 7.4% | 13% | 22% | 60% |
| 8, best of the two | 14 | 20,000 | 11.83 | 0.09% | 0.24% | 0.69% | 1.9% | 4.2% | 6.1% | 9.3% | 16% | 26% | 56% |
| 8, best of the two | 16 | 20,000 | 11.76 | 0.08% | 0.27% | 0.89% | 2.2% | 4.8% | 7.0% | 11% | 18% | 29% | 52% |
| 8, best of the two | 18 | 20,000 | 11.65 | 0.06% | 0.33% | 1.0% | 2.6% | 5.9% | 8.4% | 12% | 20% | 33% | 48% |
| 8, best of the two | 20 | 20,000 | 11.62 | 0.12% | 0.37% | 1.1% | 2.9% | 6.2% | 9.1% | 14% | 22% | 35% | 44% |
| 8, best of the two | 22 | 20,000 | 11.56 | 0.11% | 0.44% | 1.2% | 3.1% | 6.8% | 9.9% | 15% | 24% | 39% | 40% |
| 8, best of the two | 24 | 20,000 | 11.46 | 0.17% | 0.48% | 1.3% | 3.4% | 7.6% | 11% | 17% | 27% | 41% | 38% |
| 8, best of the two | 26 | 20,000 | 11.37 | 0.22% | 0.60% | 1.8% | 4.0% | 8.7% | 13% | 19% | 30% | 44% | 34% |
| 8, best of the two | 28 | 20,000 | 11.30 | 0.20% | 0.58% | 1.8% | 4.3% | 9.2% | 13% | 20% | 31% | 47% | 32% |
| 8, best of the two | 30 | 20,000 | 11.20 | 0.27% | 0.77% | 2.1% | 5.1% | 10% | 15% | 22% | 34% | 50% | 29% |
| 10, two comms | 10 | 2,000 | 11.65 | 0.10% | 0.15% | 0.35% | 1.1% | 3.1% | 8.5% | 18% | 40% | 71% | 0 |
| 10, two comms | 12 | 2,000 | 11.42 | 0.05% | 0.15% | 0.35% | 1.1% | 3.8% | 10% | 22% | 48% | 77% | 0 |
| 10, two comms | 14 | 2,000 | 11.25 | 0.10% | 0.10% | 0.40% | 1.8% | 4.2% | 12% | 25% | 52% | 82% | 0 |
| 10, two comms | 16 | 2,000 | 11.05 | 0.15% | 0.55% | 1.2% | 2.1% | 6.0% | 14% | 30% | 57% | 87% | 0 |
| 10, two comms | 18 | 2,000 | 10.91 | 0.15% | 0.50% | 1.5% | 3.0% | 6.5% | 15% | 33% | 62% | 89% | 0 |
| 10, two comms | 20 | 2,000 | 10.76 | 0.10% | 0.40% | 0.85% | 3.3% | 7.9% | 19% | 37% | 65% | 91% | 0 |
| 10, two comms | 22 | 2,000 | 10.61 | 0.20% | 0.30% | 0.95% | 3.1% | 8.1% | 20% | 40% | 71% | 95% | 0 |
| 10, two comms | 24 | 2,000 | 10.53 | 0.20% | 0.70% | 1.5% | 3.8% | 9.1% | 22% | 42% | 73% | 95% | 0 |
| 10, two comms | 26 | 2,000 | 10.39 | 0.25% | 0.70% | 1.9% | 4.4% | 10% | 24% | 48% | 76% | 96% | 0 |
| 10, two comms | 28 | 2,000 | 10.35 | 0.20% | 0.55% | 1.9% | 4.4% | 11% | 24% | 49% | 78% | 97% | 0 |
| 10, two comms | 30 | 2,000 | 10.22 | 0.25% | 0.95% | 2.3% | 5.5% | 13% | 27% | 51% | 81% | 97% | 0 |
| 10, one alg | 10 | 20,000 | 9.23 | 0.03% | 0.12% | 0.47% | 1.4% | 4.4% | 11% | 23% | 23% | 23% | 77% |
| 10, one alg | 12 | 20,000 | 9.24 | 0.04% | 0.15% | 0.48% | 1.7% | 4.7% | 13% | 26% | 26% | 26% | 74% |
| 10, one alg | 14 | 20,000 | 9.19 | 0.06% | 0.20% | 0.64% | 1.9% | 5.6% | 15% | 29% | 29% | 29% | 71% |
| 10, one alg | 16 | 20,000 | 9.17 | 0.05% | 0.23% | 0.76% | 2.3% | 6.4% | 17% | 33% | 33% | 33% | 68% |
| 10, one alg | 18 | 20,000 | 9.15 | 0.01% | 0.23% | 0.87% | 2.6% | 7.5% | 19% | 36% | 36% | 36% | 64% |
| 10, one alg | 20 | 20,000 | 9.16 | 0.08% | 0.28% | 0.95% | 2.6% | 7.6% | 20% | 38% | 38% | 38% | 62% |
| 10, one alg | 22 | 20,000 | 9.14 | 0.08% | 0.31% | 0.98% | 2.9% | 8.5% | 22% | 41% | 41% | 41% | 59% |
| 10, one alg | 24 | 20,000 | 9.13 | 0.09% | 0.27% | 0.95% | 3.1% | 9.2% | 24% | 43% | 43% | 43% | 57% |
| 10, one alg | 26 | 20,000 | 9.10 | 0.12% | 0.37% | 1.2% | 3.7% | 10% | 26% | 46% | 46% | 46% | 54% |
| 10, one alg | 28 | 20,000 | 9.09 | 0.10% | 0.37% | 1.4% | 3.9% | 11% | 27% | 48% | 48% | 48% | 52% |
| 10, one alg | 30 | 20,000 | 9.08 | 0.13% | 0.43% | 1.4% | 4.2% | 12% | 29% | 51% | 51% | 51% | 50% |
| 10, best of the two | 10 | 2,000 | 11.31 | 0.10% | 0.15% | 0.50% | 1.9% | 5.5% | 15% | 31% | 48% | 74% | 0 |
| 10, best of the two | 12 | 2,000 | 11.00 | 0.10% | 0.40% | 0.80% | 2.3% | 6.5% | 18% | 36% | 58% | 81% | 0 |
| 10, best of the two | 14 | 2,000 | 10.81 | 0.15% | 0.35% | 1.1% | 3.5% | 8.1% | 21% | 41% | 61% | 85% | 0 |
| 10, best of the two | 16 | 2,000 | 10.56 | 0.25% | 0.90% | 1.8% | 3.6% | 9.7% | 23% | 48% | 67% | 89% | 0 |
| 10, best of the two | 18 | 2,000 | 10.38 | 0.20% | 0.80% | 2.1% | 5.1% | 11% | 27% | 52% | 72% | 92% | 0 |
| 10, best of the two | 20 | 2,000 | 10.32 | 0.15% | 0.55% | 1.2% | 5.0% | 12% | 29% | 54% | 74% | 93% | 0 |
| 10, best of the two | 22 | 2,000 | 10.14 | 0.20% | 0.35% | 1.8% | 4.9% | 13% | 32% | 58% | 79% | 96% | 0 |
| 10, best of the two | 24 | 2,000 | 10.03 | 0.25% | 0.85% | 2.0% | 5.7% | 15% | 35% | 61% | 81% | 96% | 0 |
| 10, best of the two | 26 | 2,000 | 9.91 | 0.30% | 0.90% | 2.5% | 6.2% | 16% | 37% | 66% | 84% | 97% | 0 |
| 10, best of the two | 28 | 2,000 | 9.84 | 0.20% | 0.80% | 2.8% | 7.1% | 16% | 38% | 67% | 86% | 98% | 0 |
| 10, best of the two | 30 | 2,000 | 9.70 | 0.30% | 1.1% | 3.0% | 7.5% | 19% | 41% | 71% | 89% | 99% | 0 |
| 12, one alg | 10 | 20,000 | 10.54 | 0.06% | 0.17% | 0.63% | 1.9% | 5.8% | 16% | 38% | 75% | 94% | 5.6% |
| 12, one alg | 12 | 20,000 | 10.43 | 0.07% | 0.22% | 0.72% | 2.4% | 6.7% | 18% | 43% | 80% | 97% | 3.3% |
| 12, one alg | 14 | 20,000 | 10.31 | 0.11% | 0.31% | 0.92% | 2.7% | 7.8% | 21% | 48% | 85% | 98% | 1.8% |
| 12, one alg | 16 | 20,000 | 10.21 | 0.06% | 0.31% | 1.1% | 3.1% | 8.9% | 23% | 53% | 88% | 99% | 1.2% |
| 12, one alg | 18 | 20,000 | 10.09 | 0.07% | 0.39% | 1.3% | 3.7% | 10% | 26% | 57% | 91% | 99.2% | 0.78% |
| 12, one alg | 20 | 20,000 | 10.02 | 0.11% | 0.42% | 1.4% | 3.8% | 11% | 28% | 60% | 93% | 99.6% | 0.41% |
| 12, one alg | 22 | 20,000 | 9.94 | 0.12% | 0.44% | 1.5% | 4.2% | 12% | 30% | 64% | 94% | 99.7% | 0.33% |
| 12, one alg | 24 | 20,000 | 9.86 | 0.15% | 0.45% | 1.5% | 4.6% | 13% | 32% | 66% | 95% | 99.8% | 0.20% |
| 12, one alg | 26 | 20,000 | 9.78 | 0.20% | 0.58% | 1.9% | 5.2% | 14% | 34% | 69% | 97% | 99.9% | 0.14% |
| 12, one alg | 28 | 20,000 | 9.72 | 0.18% | 0.57% | 2.0% | 5.5% | 15% | 36% | 71% | 97% | 99.9% | 0.06% |
| 12, one alg | 30 | 20,000 | 9.64 | 0.24% | 0.70% | 2.0% | 6.0% | 16% | 38% | 75% | 98% | 99.9% | 0.05% |

**Exchange rates at cap 10.** The table of 7.2 with algs up to 10 moves (3c: one comm, 20,000 skeletons per length; the others: best of two comms and one alg, on 200 to 2,000 skeletons per length, the sizes of the cap-10 rows above, so the last digit is soft; every whole length is its own sample):

| Target | 3c skeleton of | Chance of the target | 2tc shorter by | 3tc shorter by | pure 2c2c shorter by | twisted 2c2c shorter by | 3c1t shorter by | 5c shorter by |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 22 or less | 15 | 93% | 1.9 | 4.4 | 3.9 | 3.3 | 4.6 |  |
| 22 or less | 16 | 65% | 1.9 | 4.4 | 3.1 | 3.2 | 4.5 | 4.8 |
| 22 or less | 17 | 28% | 1.6 | 4.2 | 2.7 | 3.1 | 4.4 | 4.5 |
| 22 or less | 18 | 9.2% | 1.6 | 3.8 | 2.6 | 2.7 | 4.3 | 4.4 |
| 22 or less | 19 | 2.5% | 1.0 | 3.5 | 2.3 | 2.6 | 3.9 | 4.1 |
| 24 or less | 17 | 95% | 1.9 | 4.3 | 3.9 | 3.2 | 4.5 | 4.9 |
| 24 or less | 18 | 69% | 1.8 | 4.2 | 3.0 | 3.1 | 4.4 | 4.7 |
| 24 or less | 19 | 31% | 1.7 | 4.0 | 2.8 | 2.9 | 4.2 | 4.4 |
| 24 or less | 20 | 10% | 1.6 | 3.7 | 2.5 | 2.9 | 4.1 | 4.3 |
| 24 or less | 21 | 2.9% | 1.2 | 3.4 | 1.8 | 2.7 | 3.8 | 4.0 |
| 26 or less | 19 | 97% | 1.7 | 4.1 | 3.7 | 3.0 | 4.5 | 4.8 |
| 26 or less | 20 | 73% | 1.8 | 4.1 | 2.9 | 3.1 | 4.4 | 4.7 |
| 26 or less | 21 | 33% | 1.5 | 3.8 | 2.7 | 2.8 | 4.2 | 4.4 |
| 26 or less | 22 | 11% | 1.5 | 3.6 | 2.5 | 2.8 | 4.0 | 4.1 |
| 26 or less | 23 | 3.2% | 1.5 | 3.3 | 2.4 | 2.5 | 3.9 | 4.1 |
| 28 or less | 21 | 97% | 1.6 | 4.0 | 3.3 | 3.0 | 4.3 | 4.7 |
| 28 or less | 22 | 76% | 1.7 | 4.0 | 2.8 | 3.0 | 4.2 | 4.6 |
| 28 or less | 23 | 35% | 1.4 | 3.6 | 2.6 | 3.0 | 4.1 | 4.3 |
| 28 or less | 24 | 12% | 1.3 | 3.2 | 2.4 | 2.7 | 3.8 | 4.2 |
| 28 or less | 25 | 3.5% | 1.0 | 3.4 | 2.1 | 2.4 | 3.4 | 3.8 |
| 30 or less | 24 | 79% | 1.7 | 3.8 | 2.8 | 3.0 | 4.2 | 4.5 |
| 30 or less | 25 | 38% | 1.5 | 3.6 | 2.6 | 2.7 | 4.0 | 4.2 |
| 30 or less | 26 | 13% | 1.4 | 3.2 | 2.2 | 2.8 | 3.7 | 4.1 |
| 30 or less | 27 | 3.9% | 1.2 | 3.2 | 2.1 | 2.4 | 3.6 | 4.0 |
| 32 or less | 26 | 82% | 1.5 | 3.8 | 2.7 | 3.0 | 4.1 | 4.5 |
| 32 or less | 27 | 40% | 1.3 | 3.5 | 2.4 | 2.6 | 3.9 | 4.2 |
| 32 or less | 28 | 14% | 1.3 | 3.3 | 2.2 | 2.6 | 3.8 | 4.0 |
| 32 or less | 29 | 4.3% | 1.1 | 2.9 | 1.9 | 2.5 | 3.6 | 3.8 |

---

## Appendix B: the 3c and 3e cases

Every corner 3-cycle and every edge 3-cycle, grouped into classes: two cases are in one class when one is the other seen from another side of the cube (the 24 rotations), or its inverse. For each class a shortest alg, which pieces go where, and how many different algs of each length solve it. It's a reference to learn from: looking a case up here is **computer only**, nothing to do in an attempt.

*Pieces* reads `A>B`: the piece from A ends at B. `+1` and `+2` are a clockwise and a counter-clockwise twist of the corner as it arrives (for edges `+1` is a flip).

**Corner 3-cycles: 1,008 cases in 23 classes.** One row per class, with how many algs of each length it has.

| Shortest alg, moves | A shortest alg | Pieces (from > to, + twist) | States in the class | 8-move algs | 9-move algs | 10-move algs | 11-move algs | 12-move algs |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 8 | `F2 L B L' F2 L B' L'` | DFL>DBL UFR>DFL DBL>UFR | 48 | 2 | 1 | 15 | 28 | 236 |
| 8 | `L D' R2 D L' D' R2 D` | DFL>DBL+1 UFR>DFL+2 DBL>UFR | 48 | 1 | 2 | 12 | 33 | 218 |
| 8 | `B D F2 D' B' D F2 D'` | UBL>DBL+2 UFR>UBL+1 DBL>UFR | 48 | 2 | 3 | 17 | 40 | 291 |
| 8 | `L' D' R2 D L D' R2 D` | UBL>DBL+1 UFR>UBL+2 DBL>UFR | 48 | 2 | 3 | 17 | 40 | 291 |
| 8 | `U L2 U' R2 U L2 U' R2` | DBR>DBL UFR>DBR DBL>UFR | 48 | 2 | 1 | 15 | 28 | 236 |
| 8 | `B' D F2 D' B D F2 D'` | DBR>DBL+2 UFR>DBR+1 DBL>UFR | 48 | 1 | 2 | 12 | 33 | 218 |
| 8 | `D' B D F2 D' B' D F2` | UBL>DFL+2 UFR>UBL+1 DFL>UFR | 48 | 1 | 3 | 14 | 36 | 203 |
| 8 | `F2 R B' R' F2 R B R'` | UBL>DFL+1 UFR>UBL+2 DFL>UFR | 48 | 1 | 3 | 14 | 36 | 203 |
| 8 | `F' D' F U F' D F U'` | UFR>DFL+2 DFL>UFL+1 UFL>UFR | 48 | 2 | 6 | 18 | 52 | 274 |
| 8 | `B' R B L' B' R' B L` | UFR>UBL+2 UBL>UFL+1 UFL>UFR | 48 | 2 | 2 | 29 | 43 | 324 |
| 8 | `L D' L' U L D L' U'` | DFR>UFL+1 UFR>DFR+2 UFL>UFR | 48 | 2 | 2 | 29 | 43 | 324 |
| 9 | `B D2 B U' B' D2 B U B2` | DFL>DBL+2 UFR>DFL+1 DBL>UFR | 48 |  | 1 | 6 | 26 | 129 |
| 9 | `L' D2 L' U L D2 L' U' L2` | DBR>DBL+1 UFR>DBR+2 DBL>UFR | 48 |  | 1 | 6 | 26 | 129 |
| 9 | `D' L2 D' R2 D L2 D' R2 D2` | UFL>DFL UFR>UFL DFL>UFR | 48 |  | 1 | 8 | 24 | 160 |
| 9 | `R2 D2 R' U2 R D2 R' U2 R'` | UFL>DFL+2 UFR>UFL+1 DFL>UFR | 48 |  | 1 | 8 | 24 | 160 |
| 9 | `U2 L2 U R U' L2 U R' U` | UFL>DFL+1 UFR>UFL+2 DFL>UFR | 48 |  | 2 | 10 | 26 | 198 |
| 9 | `F U2 F D F' U2 F D' F2` | UFR>UBL+1 UBL>UFL+2 UFL>UFR | 48 |  | 1 | 4 | 23 | 118 |
| 9 | `F2 D' F U2 F' D F U2 F` | UBR>UFL+1 UFR>UBR+2 UFL>UFR | 48 |  | 1 | 4 | 23 | 118 |
| 10 | `L' U F2 U' L U L' F2 L U'` | UFR>DFL+2 DFL>DFR+1 DFR>UFR | 48 |  |  | 1 | 8 | 60 |
| 10 | `U' L' B2 L F L' B2 L F' U` | UBL>DFL+1 DBR>UBL+1 DFL>DBR+1 | 16 |  |  | 12 | 24 | 180 |
| 10 | `U' L' F R2 F' L F R2 F' U` | DBR>DFL+1 DFL>UBL+1 UBL>DBR+1 | 16 |  |  | 12 | 24 | 180 |
| 11 | `R' U2 R U L2 U' R' U L2 U R` | UBL>DBL UFR>UBL DBL>UFR | 48 |  |  |  | 10 | 96 |
| 12 | `L2 U' F2 U F2 U L2 U' F2 U' F2 U` | UBL>DFL UFR>UBL DFL>UFR | 16 |  |  |  |  | 36 |

**Edge 3-cycles: 1,760 cases in 43 classes.** One row per class, same columns plus 6- and 7-move algs.

| Shortest alg, moves | A shortest alg | Pieces (from > to, + twist) | States in the class | 6-move algs | 7-move algs | 8-move algs | 9-move algs | 10-move algs | 11-move algs | 12-move algs |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | `F' B L2 F B' U2` | UL>DL UR>UL DL>UR | 24 | 4 | 8 | 44 | 68 | 748 | 1924 | 9974 |
| 7 | `L F B' U2 F' B L` | FL>BL UR>FL BL>UR | 48 |  | 1 | 14 | 48 | 188 | 561 | 3450 |
| 8 | `B2 L' D2 F2 U2 R' F2 D2` | UL>BL UR>UL BL>UR | 48 |  |  | 8 | 8 | 62 | 97 | 890 |
| 8 | `F2 L D2 B2 U2 R B2 D2` | UL>FL UR>UL FL>UR | 48 |  |  | 8 | 8 | 62 | 97 | 890 |
| 9 | `D2 R U' D B2 U D' R D2` | BL>DL UR>BL DL>UR | 48 |  |  |  | 5 | 51 | 137 | 740 |
| 9 | `D2 R' U D' F2 U' D R' D2` | FL>DL UR>FL DL>UR | 48 |  |  |  | 5 | 51 | 137 | 740 |
| 9 | `D' R' U' D B2 U D' R' D` | DB>BL UR>DB BL>UR | 48 |  |  |  | 2 | 33 | 128 | 626 |
| 9 | `B U' R L' B2 R' L U' B'` | UR>BL+1 BL>UL+1 UL>UR | 48 |  |  |  | 1 | 35 | 76 | 472 |
| 9 | `F' U R' L F2 R L' U F` | UR>FL+1 FL>UL+1 UL>UR | 48 |  |  |  | 1 | 35 | 76 | 472 |
| 9 | `B' L B2 D2 F2 R F2 D2 B'` | DB>UL+1 UR>DB+1 UL>UR | 48 |  |  |  | 4 | 8 | 55 | 210 |
| 9 | `B2 U' R L' B2 R' L U' B2` | UB>UL UR>UB UL>UR | 48 |  |  |  | 1 | 14 | 71 | 425 |
| 9 | `B L B2 D2 F2 R F2 D2 B` | UB>UL+1 UR>UB+1 UL>UR | 48 |  |  |  | 4 | 10 | 65 | 233 |
| 9 | `D R' U' D B2 U D' R' D'` | DF>BL UR>DF BL>UR | 24 |  |  |  | 2 | 32 | 122 | 545 |
| 9 | `D' R U D' F2 U' D R D` | DB>FL UR>DB FL>UR | 24 |  |  |  | 2 | 32 | 122 | 545 |
| 10 | `F2 B2 D' B' D F2 B2 U' B U` | BL>DL+1 UR>BL+1 DL>UR | 48 |  |  |  |  | 6 | 40 | 278 |
| 10 | `F2 B2 D F D' F2 B2 U F' U'` | FL>DL+1 UR>FL+1 DL>UR | 48 |  |  |  |  | 6 | 40 | 278 |
| 10 | `D F U F' U D' L U' L' U'` | FL>BL+1 UR>FL+1 BL>UR | 48 |  |  |  |  | 6 | 16 | 67 |
| 10 | `F B' R B' R' F' B U B U'` | UL>BL+1 UR>UL+1 BL>UR | 48 |  |  |  |  | 6 | 17 | 136 |
| 10 | `B' R' U2 D2 L F L' U2 D2 R` | DB>BL+1 UR>DB+1 BL>UR | 48 |  |  |  |  | 5 | 20 | 176 |
| 10 | `R' U2 D2 L U L' U2 D2 R U'` | UB>BL UR>UB BL>UR | 48 |  |  |  |  | 2 | 20 | 124 |
| 10 | `D' B' U' B U' D L' U L U` | UR>BL+1 BL>FL+1 FL>UR | 48 |  |  |  |  | 6 | 16 | 67 |
| 10 | `F B' R' F R F' B U' F' U` | UL>FL+1 UR>UL+1 FL>UR | 48 |  |  |  |  | 6 | 17 | 136 |
| 10 | `F R U2 D2 L' B' L U2 D2 R'` | DF>FL+1 UR>DF+1 FL>UR | 48 |  |  |  |  | 5 | 20 | 176 |
| 10 | `R U2 D2 L' U' L U2 D2 R' U` | UF>FL UR>UF FL>UR | 48 |  |  |  |  | 2 | 20 | 124 |
| 10 | `R' F' B U L2 U' F B' R U2` | UR>DL+1 DL>UL+1 UL>UR | 48 |  |  |  |  | 4 | 16 | 80 |
| 10 | `F R B U' B' R' F' L' U L` | UR>UL+1 UL>UB+1 UB>UR | 48 |  |  |  |  | 8 | 14 | 93 |
| 10 | `F' R L' U B' U' R' L F U` | UR>DB+1 DB>UB+1 UB>UR | 48 |  |  |  |  | 10 | 17 | 114 |
| 10 | `L F R' F' R L' U R U' R'` | UF>UB+1 UR>UF+1 UB>UR | 48 |  |  |  |  | 8 | 14 | 93 |
| 10 | `U R' U' D B U' B' U D' R` | DR>UB+1 UR>DR+1 UB>UR | 48 |  |  |  |  | 10 | 17 | 114 |
| 10 | `B' D' F' U' R' U F D B R` | BR>UB UR>BR UB>UR | 48 |  |  |  |  | 2 | 12 | 65 |
| 10 | `L F R B U' B' R' F' L' U` | UR>BL+1 BL>UB+1 UB>UR | 24 |  |  |  |  | 7 | 6 | 85 |
| 10 | `R' U' R' U' R' U R U R U` | FR>UB UR>FR UB>UR | 24 |  |  |  |  | 7 | 6 | 85 |
| 10 | `F L B D B' L' F' R' D' R` | DR>DB+1 FR>DR+1 DB>FR | 24 |  |  |  |  | 2 | 6 | 99 |
| 10 | `L' U' R' F' R U L D F D'` | FR>DL+1 DL>DF+1 DF>FR | 24 |  |  |  |  | 2 | 6 | 99 |
| 11 | `U' B L' B' U' F' D' L D F U2` | UR>DL+1 DL>BL+1 BL>UR | 48 |  |  |  |  |  | 8 | 141 |
| 11 | `U F' L F U B D L' D' B' U2` | UR>DL+1 DL>FL+1 FL>UR | 48 |  |  |  |  |  | 8 | 141 |
| 11 | `U' R' F' B U L' U' F B' R U2` | UR>DL+1 DL>UB+1 UB>UR | 48 |  |  |  |  |  | 8 | 70 |
| 11 | `U2 F' U' D R U' R' U D' F U'` | UR>DF+1 DF>UB+1 UB>UR | 48 |  |  |  |  |  | 8 | 70 |
| 11 | `R2 B' D B R F L D' L' F' R` | FR>DL+1 DL>DB+1 DB>FR | 48 |  |  |  |  |  | 2 | 36 |
| 11 | `U2 L2 U R' L F' L2 F R L' U` | UL>DL+1 UR>UL+1 DL>UR | 24 |  |  |  |  |  | 8 | 50 |
| 12 | `D' R F2 B2 L' F' L F2 B2 R' F D` | DR>DF+1 FR>DR+1 DF>FR | 16 |  |  |  |  |  |  | 12 |
| 12 | `L' U R B R' U2 L2 D F' D' L' U` | FR>UL+1 UL>DB+1 DB>FR | 8 |  |  |  |  |  |  | 60 |
| 12 | `U' F' B U L2 U' F B' R U2 R' U` | FR>DL+1 DL>UB+1 UB>FR | 8 |  |  |  |  |  |  | 60 |

---

## Appendix C: how it was computed, and what checks it

**The model.** One sticker-level cube built from geometry, so no permutation is typed by hand. The search program reads its move tables from it, and every solution that is printed anywhere in this study is replayed on it.

**Leftover types (section 4).** Corner states as a permutation with twists, edge states as a permutation with flips. All products of two 3-cycles and, for corners, of three are formed and sorted by cycle type. Exhaustive.

**Algorithms (section 5, Appendix B).** Every reduced move sequence of 12 moves or fewer that moves corners only or edges only, found by joining all sequences of 6 moves with all sequences of 6 (meet in the middle), then sorted by what it does. *Reduced* means no two moves in a row on one face and a fixed order for two moves on opposite faces, so each alg is counted once. For the 3-cycle families a second, independent depth-first search gives the same lists class by class. The parity (2c2e) lists come from that second search. For torchlight's statement on twisting a corner (section 5) the same join was run over every corner-only sequence of 12 moves or fewer, whatever it does to the corners.

**One skeleton (everything in sections 6 to 9).** For a skeleton and a leftover I work out the state an insertion has to produce at each spot, then put in every alg within the cap for that state and cancel. For two comms, every first comm at every spot (every 3-cycle that leaves a 3-cycle) gets followed by every second comm at every spot of the result. The program only skips work where a bound proves nothing better can come out, so the minimum is exact for its cap over the spots of the skeleton as written (section 11).

**Samples.** A random skeleton is $n$ moves, each uniform among the moves that do not turn the face just turned (and that keep opposite-face pairs in the fixed order), and a leftover drawn uniformly from its type. The sizes are in section 3 and in each table; the odd lengths of section 7 have samples of their own, made the same way. Two standard errors of a mean, one row per sample:

| Leftover | Cap | Skeletons | ± two standard errors, moves |
|---|---:|---:|---:|
| 5c | 8 | 20,000 | 0.02 |
| 5c | 10 | 2,000 | 0.06 |
| 3c1t | 10 | 500 | 0.11 |
| 2tc | 10 | 200 | 0.17 |
| 5c | 12 | 100 | 0.26 |

**Exchange rates (section 7).** The chance of a total of $N$ or less from a skeleton of length $n$ is the share of sampled skeletons of that length whose best insertion adds $N - n$ or less. Every whole length from 10 to 30 is its own sample. The length of equal chance is read off between two whole lengths on the log-odds, and the length of equal expected total between two whole lengths on the mean.

**What checks what.**

- The search program's cube and its cancelling agree with the sticker model on random sequences.
- The sizes of all 15 leftover types come out the same three ways: by construction, among all products of two 3-cycles, and among all corner states.
- One comm: a separate Python program on the sticker model computes the best 8-mover and the best alg of up to 10 at every spot of every 3c skeleton of the samples. Its minimum equals the search program's on all 220,000 skeletons, at both caps.
- Two comms: the search agrees with a plain enumeration of every pair on small skeletons for every type, and the Python program, following up every first comm, gives the same total on 20,000 5c skeletons of 20 moves.
- 163,683 solutions printed in the sample files, every solution for the real skeletons (2,143) and every solution on the examples page were replayed: each solves its scramble with the stated length.
- On the Insertion Finder pages people posted, the search is never worse than Insertion Finder once its cap covers the algs Insertion Finder used (section 9).

**Formally verified.** `lean/Insertions` in the repository is a Lean 4 certificate (no Mathlib, no `sorry`). It recomputes from its own definitions, and states as theorems:

- *the leftover types (section 4)*:
  - `corner_three_cycles`, `edge_three_cycles`: there are 1,008 corner 3-cycles and 1,760 edge 3-cycles, all different, each of order 3, and the inverse of each is in the list.
  - `corner_products_of_two`: every pair of corner 3-cycles multiplied gives 216,511 different states, and by type exactly the 5c, 3c3c, 3c1t, twisted 2c2c, pure 2c2c, 3tc and 2tc counts of section 4, the 3c1t and the 3tc as two types each, one per twist direction (plus the 3-cycles and the solved state). No other type occurs.
  - `corner_no_two_twisted_3_cycles`, `corner_no_two_swaps_with_twist`: two 3-cycles never give two twisted 3-cycles (the mixed 3c3c), nor two swaps with a twisted corner (2c2c1t).
  - `corner_type_sizes`, `corner_two_gives_whole_types`: the number of all corner states of each type, counted over all 88,179,840 corner states, equals the number reached, so every state of those seven types is two 3-cycles away.
  - `edge_products_of_two`, `edge_type_sizes`, `edge_two_gives_whole_types`: the same for edges: 925,035 states, the six edge types of section 4, each reached in full.
  - `corner_fewest_up_to_three`, `corner_three_totals`, `corner_three_gives_whole_types`: multiplying by a third 3-cycle, exactly 22 more types appear (twist directions apart; 11 by name), 8,845,836 states, each type in full: the second table of section 4.
  - `corner_type_sizes_by_hand`, `edge_type_sizes_by_hand`: the same sizes again as plain arithmetic (which 5 corners, how many cyclic orders, how many twists).
- *first comms per spot* (`first_comms_per_spot`, 6.2): for every state of every type, the 3-cycles that leave a 3-cycle: 108 for a 2tc, 24 for either 2c2c, 18 for a 3tc, 9 for a 3c1t, 5 for a 5c.
- *the algs of 8 moves or fewer*, on a sticker cube whose 18 turns equal the Python model's (`moves_agree_with_python`), found by joining every sequence of up to 4 turns with every sequence of up to 4 turns, no pruning:
  - `corner_algs_up_to_8`, `corner_counts` (section 5): 864 corner-only sequences, all 8-move 3-cycles; 528 of the 1,008 3-cycles have one, 336 of them two; 32 of the 112 oriented 3-cycles have one; 112 have none even one move over; Jay's `R' F' R B2 R' F R B2` is one of the oriented ones (`jay_oriented_8_mover`).
  - `edge_counts` (6.6): the edge 3-cycles with an alg of 8 or fewer are 168, with 6-, 7- and 8-move sequences 96, 240 and 2,496; the 24 with a 6-mover are oriented on all three axes, and exactly that many edge 3-cycles are.
- *the corner algs of 10 moves or fewer* (`ten_facts`, the same join with halves of up to 5 turns): of the corner 3-cycles, 528 have an 8-mover, 336 more a 9-mover and 80 more a 10-mover (1,728 and 11,856 sequences of 9 and 10 moves); a pure 2c2c has a 10-mover in 132 cases and nothing shorter; nothing of 10 moves or fewer does a twisted 2c2c, a 3c1t, a 2tc or a 3tc.
- *the examples*: every scramble, skeleton, comm and solution of the corrections page and of [a] to [e] and [g] to [k] replays as printed (lengths, cancels, what the skeleton leaves), and the optima they state are exact over every alg of 8 moves or fewer, and of 10 or fewer where they say so:
  - [a]: 29, 29 and 30;
  - [b]: 26 with 8-movers, 25 with algs up to 10, and no 9-mover better than 26;
  - [c]: 25 at spot 16 only, and nothing better than an 8-1 on the odd spots and the ends;
  - [d]: 19;
  - [e]: 29 nested and 31 without nesting;
  - [g]: 30;
  - [h]: no 8-mover at any spot, 30 with algs up to 10;
  - [i]: 28 with 8-movers, 27 with algs up to 10;
  - [j]: 25 at spot 4 only;
  - [k]: 25 at spot 10 only, no alg under 10 moves for the case at spot 8, and the walk sees nothing better than an 8-1;
  - the 20-move 3c of 6.1 with no 8-mover: 28 with algs up to 10, and the shortest alg at each spot as printed;
  - the 23-move 3c of 9.5: 27 with 8-movers, 23 with algs up to 10.

*Computed, not proved*: the corner alg lists over 10 moves and the edge lists over 8 (cap 12, the 3c1t and 2tc alg counts, twisting in place, 2c2e), the insertion searches on the samples and on the real skeletons, every mean, share and exchange rate (the samples), and examples [f] and [l]. They rest on the cross-checks above. The proofs use `native_decide`, which trusts the Lean compiler. That the edge leftovers needing three comms are 13 types is counted in Python only, and is not used here.

---

## Docs referred to

- Sebastiano Tronto, [Fewest Moves Tutorial](https://fmcsolves.cubing.net/fmc_tutorial_ENG.pdf), version 3 (January 2020), revision 3.04 (August 2023): section 2.4 on insertions, the table in 2.4.10, the solves of Appendix D.
- Yurii Riabov, [Hitchhiker’s Guide to FMC](https://docs.google.com/document/d/16nu10y1JkUmVDC11c1h_ULzAl4Vze7zR), March 2024: which leftovers take how many comms. It links the alg sheet [DR algs with mnemonics](https://docs.google.com/document/d/1TqVjcA5DW3TzZOtxV1uzvHeYBACA4CP-lECrLuD9WAY).
- Cyprian Kalbarczyk, [Blockbuilding example solves](https://docs.google.com/document/d/1oWbbzc375q4FRIuzA5U091yaiGxt0zkFObGPe5P24_I) (solves from late 2019 to October 2022) and [FMC attempt with comments](https://docs.google.com/document/d/1_6hfBXK3cK-xZ1f7VjRH8EtSZ5hpLuV7TNFGT1zkZw8).
- Alexandros Fokianos and Tommaso Raposio, A Domino Reduction Guide, August 2019 ([shared folder](https://drive.google.com/drive/folders/1olTCi3CoDhHoKeikeDb6KFzlqIIi-CXe)).
- [Insertion Finder](https://333.fm/if): the site 333.fm is Baiqiang Dong's and the core was written by Yan Xuan (Baiqiang, [5 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181810277851865108)). The result pages people posted from it are linked in section 9.
