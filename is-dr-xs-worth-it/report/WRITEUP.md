# Is DR-xs worth it?

What leaving slices unsolved at DR costs you, how often you get the chance, and what it buys on real scrambles. Whatever can be counted exactly, I counted exactly: all 768 kinds of DR-xs state and all 2,217,093,120 cosets of the DR group. The rest is sampled or run on real scrambles. Each row is one thing measured and the sample behind it:

| What was measured | Sample |
|---|---|
| Finishes of DR-1s | 200,000 random states |
| Finishes of DR-2s 8fe | 5,000 random states |
| The shortest DR-xs of a scramble | 2,000,000 random scrambles |
| Every DR-1s and DR-2s 8fe, found and finished | 500 real scrambles |

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs are listed with links at the end.

**This builds on** work that is already on the server:

- **tseitsei89's [DR-Xs tutorial](https://docs.google.com/document/d/1_uLVLB5xqDm40NugXE5rjc8LgEtuHQCLz0odKY6mboE)** (with Jay, Rodney, trangium, count quackula, KrzychXyz and others behind it): the method.
- **trangium's numbers in the [tutorial](https://docs.google.com/document/d/1_uLVLB5xqDm40NugXE5rjc8LgEtuHQCLz0odKY6mboE)**: on optimal a DR-1s finishes about 2.2 to 2.4 moves longer than a DR of the same subset (1.8 for 2c4), and a DR-2s 8fe about 1 move longer. tseitsei89's takeaway: "8 move DR-1s is on average better than an 11 move DR but worse than 10 move DR". Those hold up.
- **trangium's [dr-fe examples](https://docs.google.com/document/d/11Xu6BpEBLu-v8hVbFzneSqeMjHb83q_zurWb_V0DXDY)**: the rule for the number of slices.
- **The first study of this site, [Judging a DR by hand](../judging-a-dr/)**: the exact optimal finish of every DR state, which every finish here uses.

**What this adds**, all things people kept asking for:

- **Odds, not just averages**: the chance of a finish in N from a DR-1s or a DR-2s 8fe, by subset, next to the same for a DR.
- **The move counts** from DR-3s to DR-2s to DR-1s to DR, for every layout of flipped edges.
- **How often you get one**: the chance of a slice-EO skip, and how far a DR-1s is from one.
- **Real scrambles**: every DR-1s and DR-2s 8fe on 500 scrambles, finished, against every normal DR on the same scrambles.
- **The claims**: every concrete thing people said about DR-xs, checked.

**Terms**, as the tutorial uses them. A *slice EO* (sEO) is the four edges of one slice all oriented, or all misoriented, for one axis. A *DR-xs* is a cube that looks like a DR if you ignore the centers and let some of the eight non-slice edges be flipped. It's a *DR-1s*, *DR-2s* or *DR-3s* by the number of slice moves it takes to fix centers and flipped edges. *DR-2s 8fe* is the DR-2s with all eight edges flipped and the centers off, which is how it comes up in the tutorial (eight flipped edges with the centers right is a different, worse DR-2s). Turns are HTM, and a slice move counts as the two outer turns it's written with (`R L'`).

**How to read it.**

- **Start with [section 1](#1-the-short-version)**, the short version: what's new, what it confirms or corrects, and the verdict, one line each.
- **The [worked examples](examples.html)** go with it: the tutorial's example with the numbers, then 100 scrambles with their slice-EO skips and the DR-xs routes on them, answers folded away. **The [errata](errata.html)** list what the numbers show is wrong in the docs involved and in things said on the server, each with an example.
- **The appendices are reference**: every DR-1s layout with a shortest fix and a scramble, what each EO pattern leads to, and how it was computed and checked.
- **What you can use in an attempt, and what's the answer key.** These are **computer only**, and each place says so: they say what's there, not what you find in an hour.
  - every finish here is the best one of the method's form, with the optimal DR finish looked up in a table of every DR state;
  - the shortest DR-xs of a scramble and the distances from a skip are exact searches;
  - section 7 finishes tens of thousands of DR-xs.

  What carries over to an attempt are the rules they give, all things you can see at the table: a DR-1s in $N$ is worth about a DR in $N + 2.3$, the order to check things in (7.2), which skips can lead to a DR-1s (6.2) and which DR-1s are the good ones (5.4).

---

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | What is new, what it confirms or corrects, and the verdict, one line each. |
| [2. What was asked](#2-what-was-asked) | The questions and the standing disagreement, quoted. |
| [3. What a DR-xs is, and how many slices it needs](#3-what-a-dr-xs-is-and-how-many-slices-it-needs) | The 768 kinds and the rule for the number of slices. |
| [4. The move counts: DR-3s, DR-2s, DR-1s, DR](#4-the-move-counts-dr-3s-dr-2s-dr-1s-dr) | Every layout of flipped edges and what it takes to fix. |
| [5. The finish: DR-1s and DR-2s 8fe against a DR](#5-the-finish-dr-1s-and-dr-2s-8fe-against-a-dr) | Averages and odds by subset, which DR-1s are good, what a hand finish loses. |
| [6. Getting one](#6-getting-one) | Slice-EO skip odds, how far a DR-1s is from a skip, and why getting to an 8fe is the same problem as getting to a DR. |
| [7. On 500 real scrambles](#7-on-500-real-scrambles) | Every DR-1s and DR-2s 8fe against every normal DR on the same scrambles. |
| [8. The claims, checked](#8-the-claims-checked) | Each checkable statement from the server, with the verdict. |
| [9. What this does not cover](#9-what-this-does-not-cover) | Limits. |
| [Appendix A: every DR-1s layout](#appendix-a-every-dr-1s-layout) | The 70 layouts with a shortest fix and a scramble each. |
| [Appendix B: from an edge-orientation pattern to a kind of DR-xs](#appendix-b-from-an-edge-orientation-pattern-to-a-kind-of-dr-xs) | What each uniform EO pattern leads to, for each choice of faces. |
| [Appendix C: how it was computed, and what checks it](#appendix-c-how-it-was-computed-and-what-checks-it) | Method, cross-checks and the Lean certificate. |
| [Docs referred to](#docs-referred-to) | Links. |

---

## 1. The short version

First what nobody had before, each line with the sample and the move rule behind it; then what the numbers confirm or correct; then the verdict.

- **A DR-1s of 7 is worth about a normal DR of 9, and a DR-1s of 8 about a normal DR of 10.** On 500 real scrambles I counted how often each one gets the best solution any normal DR of 12 or less gives on its scramble (7.2). Each row is one kind of thing to finish; the number is how many of them you finish, on average, for one to give the scramble's best:

  | What you finish | One in this many gets the scramble's best |
  |---|---:|
  | a DR-1s of 7 | 49 |
  | a normal DR of 9 or less | 41 |
  | a DR-1s of 8 | 210 |
  | a 10-move DR | 202 |
  | an 11-move DR | 952 |
  | a DR-2s 8fe of 9 | 151 |
  | a DR-1s of 6 or less | 12 |

  That's the "how likely various things are to give you, say, sub-11 dr or sub-8 dr-1s" trangium wanted ([23 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1475550291343577168)), minus the time per check. The finishes behind these odds are the best of the method's form, **computer only**; the ranking is what you use in an attempt.
- **Slice EOs against 5-move EOs, the question left open.** Same scrambles, starting from the EOs of 4 or less and their DRs of 10 or less. Each row adds one set of things to finish on top of those, and the number is how much shorter that makes the average best solution (7.4):

  | Added on top | Average best solution shorter by, moves |
  |---|---:|
  | every DR-1s of 8 or less from a slice EO, no normal EO added | 0.36 |
  | only the ones of 7 or less | 0.17 |
  | every 5-move EO (about 253 more EOs) | 0.71 |
  | both together | 0.91 |

  The 5-movers give more and do better per thing finished (24 more DRs against 71 more DR-1s); the slice EOs take far less looking. Both sides are **computer only** (every DR-xs and every 5-move EO, each finished as well as possible). What carries over is the order: EOs of 4 or less, then the skips, then 5-movers.
- **A slice-EO skip is there on 68.7953% of scrambles on normal, 79.3147% counting inverse.** That's exact, over all 70,963,200 arrangements of edge kinds and orientations, and it answers wen's question, where tseitsei89 had said ([3 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1533719488564822026)): "I have no idea. But it seems to happen on most scrambles I would say." The skips clump, though: 2.25 per scramble on average over both sides, yet 21% of scrambles have none (6.1).
- **Getting to a DR-2s 8fe is getting to a DR with the pieces renamed.** An 8fe is placed like a DR on one pair of faces in the colours of another pair: move every piece a quarter turn around the third axis, leave the centres, flip every edge, and it's a real DR. So (6.3):
  - from a full EO, with moves that keep it, the distance to the 8fe has exactly the distribution of the distance to the DR over all 1,082,565 positions, 7.80 on average;
  - with any moves each 8fe is as far as a DR. A scramble has twelve 8fe targets against six DRs, which is why its shortest 8fe comes 0.33 of a move before its shortest DR;
  - only the finish differs, +1.19.

  So a skip isn't how you get an 8fe. An oriented one leads to it only when the whole axis is oriented (0.78% of them, and that's just a normal EO). A misoriented one on an axis with 8 bad edges is the one separate way in, 9.19 moves on average.
- **The whole trade in two numbers.** The shortest of each over 2,000,000 random scrambles (any moves, linear, three colours, normal and inverse), 6.4. Each row is a target; the number is the average length of the shortest one on a scramble:

  | Shortest on the scramble | Average length, moves |
  |---|---:|
  | a real DR | 8.76 |
  | a DR-1s | 6.81 |
  | a DR-2s 8fe | 8.43 |
  | any DR-xs | 6.46 |

  So the shortest DR-1s comes 2.0 moves before the shortest real DR, and it costs 2.27 in the finish. On average that's close to even, so it pays when you find the short ones. These are searches over every route, **computer only**, the answer key.
- **A DR-1s costs 2.27 more moves in the finish than a DR, and here are the odds.** Over 200,000 uniformly random ones, each finished as well as the method can (setup from either end, slice, optimal DR finish). The first row is the average finish, the others the share that finish in that many moves or fewer:

  | Finish | From a DR-1s | From a DR |
  |---|---:|---:|
  | average finish, moves | 15.85 | 13.58 |
  | in 14 or less | 9.0% | 80% |
  | in 15 or less | 32% | 99% |

  By subset the penalty is +2.04 to +2.53, a bit more on the low-qt subsets. At equal odds a DR-1s in $N$ is a DR in about $N + 2.3$. A DR-2s 8fe (5,000 random states) costs 1.19, from +0.95 (4a1) to +1.41 (4c4), going up with the qt count (5.2, 5.3). These finishes use the optimal DR finish from a table, **computer only**. A finish you find by hand is longer, so take the $N + 2.3$ rule from it, not the lengths themselves.
- **The one good kind of DR-1s** is the one a single slice turn fixes, seen from one side of the scramble or the other (2.8% of them): it finishes in 14.52 on average, 0.94 over a DR. Past that the layout doesn't matter much (5.4). Average finish by how far the DR-1s is from a real DR:

  | Fewest turns to a real DR, from the better side | 4 | 5 | 6 |
  |---|---:|---:|---:|
  | average finish, moves | 15.74 | 15.96 | 16.12 |

  And by how the four flipped edges split between the two slices they belong to:

  | Split of the flipped edges | 3-1 | 2-2 | 4-0 |
  |---|---:|---:|---:|
  | average finish, moves | 16.05 | 15.78 | 15.10 |

  The split is the same layout seen from the other side. The 4-0 is only good when its slice is the one that fixes; four in the other slice finish at +2.10, no better than an ordinary DR-1s.
- **Setting up only on the side where you found the DR-1s loses 1.06 moves.** With the setup at most 4 moves on that side and any DR finish after it, the average is 16.91 and only 38% of states keep their best finish, even though the best solution has its slice within 4 moves of one end for at least 64%. Try the setup from both sides before you judge a DR-1s (5.5). This one is for the attempt.
- **From an oriented skip on an axis that isn't the slice's own, a DR-1s is 7.68 moves away on average** without breaking that axis's EO (exact, over every coset with such a skip). The share of these skips with a DR-1s that close:

  | Moves to the nearest DR-1s | 6 or less | 7 or less | 8 or less |
  |---|---:|---:|---:|
  | share of skips | 7.1% | 36% | 88% |

  From a full EO the nearest real DR on one axis is 7.80 under the same rule, so in route length a skip like this is an EO that cost nothing. The distances are the nearest DR-1s over every route, **computer only**. The hand version is tseitsei89's 8, occasionally 7 ([28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1465952080756871423)): "I can usually find some DR-fe in 8 moves. Occasionally 7." (6.2)
- **On 500 real scrambles, here's how many have a DR-1s** from a skip or a one-move slice EO by the plain tutorial route (7.1). I took every route, so it's a floor. Each row is a length; the number is the share of the 500 scrambles that have a DR-1s that short:

  | DR-1s from a skip or a one-move slice EO | Share of the 500 scrambles that have one |
  |---|---:|
  | of 8 or less | 89% |
  | of 7 or less | 46% |
  | of 6 or less | 11% |

  There are 63.1 of them on average, nearly as many as the 69.7 normal DRs of 10 or less. **Computer only**: every route taken, which nobody does in an hour. It says how much is there, not how much you find.
- **What finishing them does.** On top of every normal DR of 10 or less, every DR-1s of 8 or less takes the average result from 20.62 to 20.42. Every 11-move DR instead takes it to 20.04, with 10.3 times as many to finish (7.3). **Computer only**: every one of them finished as well as possible, the answer key. The part you can use by hand: the DR-1s of 7 or less come before the 10-move DRs, and the ones of 8 before the 11s.
- **DR-1s to DR takes 2 to 6 turns, usually 5 or 6.** Of the 70 ways four flipped edges can sit, how many need each number of turns:

  | Turns to a real DR | 2 | 3 | 4 | 5 | 6 |
  |---|---:|---:|---:|---:|---:|
  | layouts | 1 | 2 | 9 | 30 | 28 |

  That's 83% needing 5 or 6, 5.17 on average. All 70 with a shortest fix and a scramble each are in Appendix A, the list Radek B asked for. Right after a trigger, DR-2s to DR-1s is free for 209 of the 383 kinds of DR-2s and costs 3 for the rest (4.2, 4.3).

**What it confirms or corrects**, each worked out in the section named:

- **trangium's averages hold.** trangium's nissy averages are 0.1 to 0.4 below my DR-1s numbers and a tenth or two below my 8fe ones on the subsets trangium measured; those are true optimals, which can leave the form. The tutorial's "8 move DR-1s is on average better than an 11 move DR but worse than 10 move DR" holds, in odds too. Rodney's "+3/+4 penalty for -1/-2 slice" is a bit hard on the DR-1s, and tseitsei89's "in reality around 3 moves worse" is what it turns into when you don't get the best finish (5.3).
- **DR-1s to DR.** Daichi's "6 moves max" is exact. Rodney's "basically flat", with 3 as the median, isn't: the distribution isn't flat and the typical fix isn't 3 (section 8). The EO Meta Comparison doc's "1 slice can be fixed in 3 moves" is 1.17 short on average with one slice turn cancelling, the way Rodney counts it, and 2.17 from the state alone (4.2). Simon's slice-DR table is four layouts off: 1, 4, 13, 36, 16, not 1, 4, 9, 40, 16; the thirteen 4-turn layouts are at the end of Appendix A.
- **Slice EOs.** For one given slice a slice EO is never more than 2 moves away, like FakeMMAP said, if all-misoriented counts; all-oriented only, it takes 3 moves 5.9% of the time. The 1 in 8 for a slice and an axis (tseitsei89, count quackula) is right (6.1).
- **Which skips can give a DR-1s at all**, as long as you keep that axis's EO, is a clean rule (6.2):
  - oriented, on an axis that isn't the slice's own: always;
  - misoriented on such an axis: only if that axis has exactly 8 bad edges, trangium's "MUST have 8 bad", which is 55% of them (70 in 128, Rodney's "55%");
  - oriented on the slice's own axis: 55% of the time;
  - misoriented on the slice's own axis: never.
- **The `U R L` ending** (a normal DR that's an 8fe two moves earlier) is worth about 0.8 of a move with the best finish of the form; trangium's "1 to 1.3 moves better" and count quackula's "one move better" stand at about one move (5.6).
- **Rodney's extra-good DR-1s**, "just 1-2 moves worse than full DR", is +1.52 on average (5.4). Five of Rodney's six patterns that guarantee one are right; the 12-bad line gives a DR-2s, not a DR-1s, with a scramble in section 8. count quackula's 12-bad notes already had it, and trangium's fix is right.
- **The groundwork checks out**:
  - trangium's rule for the number of slices holds for all 768 kinds (section 3);
  - trangium's dr-fe distribution comes out number for number from the search over all 2,217,093,120 cosets;
  - all 43 labelled examples from the server are what their labels say;
  - a DR-3s is a DR-2s for free right after the trigger for all 244 kinds, like the tutorial says (4.3);
  - the small exact tables are proved in Lean (Appendix C).

**The verdict:**

- **So is it worth it?** Each row is a DR-xs you might have, and where it goes in the order you finish things:

  | DR-xs you have | Where it goes |
  |---|---|
  | a DR-1s of 7 or less | yes, before your 10-move DRs. One is there on nearly half of scrambles |
  | a DR-1s of 8 | after the 10s and before the 11s, about 4.5 eleven-movers each |
  | a DR-2s 8fe of 9 | about as good as a 10-move DR |
  | a DR-1s of 6 or less | the only one that clearly beats a normal DR of 9 or less, and it's there on 11% of scrambles |

  Once the 11-movers are done, DR-xs adds 0.09 to the average. Mostly it gets you the same result from fewer and shorter things; on 3.4% of scrambles it beats everything a normal DR of 12 or less gives.
- **Against 5-move EOs**: the slice-EO routes give more than half of what all the 5-move EOs give, for far fewer starts, and the two stack. tseitsei89's order, sub-5 EOs, then slice-EO skips, then 5-movers, fits that as long as the skips are quick to check; the tables don't measure time.

---

## 2. What was asked

The questions, in the askers' own words.

- Tom Nelson ([15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560141873975394356)): "do we have movecount distributions for DR-1s > DR and DR-2s > DR? it feels like DR-xs is almost never good (apart from 2s8fe)". The answers were estimates. Daichi ([15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560144143441854566), [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560145175714472097)): "dr-1s to dr is like 6 moves max?", "i don't think 7 optimal exists". Rodney ([15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560294279010717737)): "I would guess the distribution is basically flat."
- Radek B ([21 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1518189603662594128)): "is there a list of all cases for dr-1/2s -> dr?" tseitsei89: "I dont think so".
- wen ([3 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1533718861914964080)): "what is the probability of at least one slice EO skip (fully oriented or vice versa) on a scramble?" tseitsei89 ([3 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1533719488564822026)): "I have no idea. But it seems to happen on most scrambles I would say."
- JTuu ([21 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1463631939092222032)): "what's the length distribution for the slice-eo condition? what about expected moves to dr from there?"
- tseitsei89 ([28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1465968381764309146)), on slice EO in 1 being better than EO in 5: "Do we have some proper stats for that?"
- trangium ([23 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1475550291343577168)): "at some point I want to do an analysis of how likely various things are to give you, say, sub-11 dr or sub-8 dr-1s", then divide by the time it takes to check. tseitsei89 ([23 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1475550510177325216)): "This I think would be EXTREMELY valuable!"
- tseitsei89 ([4 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1534105529683542047)): "For sEO I currently believe skips are better than 5 move EOs but 1 movers might not be."

And the verdicts that never got settled:

- tseitsei89 ([28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1465952080756871423)): "You are better off with classical DR it seems."
- Rodney ([3 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1468273993105805364)): "You're leaving money on the table if you don't check these, IMO."
- zakimoshi ([26 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1476697849600409620)): "sEO isn't actually a very cost effective strategy time wise".
- tseitsei89 again, three months later ([27 Apr 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1498259448454713424)): "most of the time it is not worth it to spend time on but it can occasionally save an otherwise doomed attempt".

---

## 3. What a DR-xs is, and how many slices it needs

Take a cube and one colour pair, say white/yellow. It is a DR-xs for that colour when:

- every corner has its white or yellow sticker on the same pair of opposite faces (any pair, not necessarily the white and yellow faces),
- the four edges with no white or yellow are in the slice between those two faces, and they all agree with each other.

The other eight edges can be flipped (white or yellow on the side), any even number of them, and centers don't matter. That's the group FakeMMAP wrote down ([25 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1464948138707255550)): "<U, D, F2, B2, R2, L2, M, S>, aka DR-fe."

How many slices it needs comes down to two things: where the corners' faces are relative to the centers, and how many edges are flipped. trangium's examples doc has the rule, and enumerating everything confirms it line for line. Each row is one group of kinds with the same slice count, corner faces and slice-edge alignment; "Kinds of state" is how many of the 768 fall in it:

| Slices needed | Corners oriented on | Slice edges against the centers | Possible numbers of flipped edges | Kinds of state | Turns to a real DR, fewest–most |
|---:|---|---|---|---:|---|
| 0 | the faces of their own colour | agree | 0 | 1 | 0 |
| 1 | two other faces | agree | 4 | 140 | 2–6 |
| 2 | two other faces | disagree | 0, 2, 4, 6 or 8 | 256 | 4–9 |
| 2 | the faces of their own colour | agree | 2, 4, 6 or 8 | 127 | 5–9 |
| 3 | two other faces | agree | 0, 2, 6 or 8 | 116 | 8–10 |
| 3 | the faces of their own colour | disagree | 0, 2, 4, 6 or 8 | 128 | 6–10 |
| all | | | | **768** | |

"Slice edges against the centers" is the tutorial's aligned and misaligned: do the four slice edges match the centers of their slice or not. Per colour there are 768 kinds of state, a kind being the faces, where the flipped edges are, and that one bit. Section 4 is an exact computation over these kinds, and section 6 uses them as targets.

Two sanity checks on the definition:

- The search for the nearest DR-xs on one colour and one pair of faces, over all cosets, gives this many states at 0 to 10 moves, which is the distribution trangium posted ([2 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1478068304819261513)), number for number:

  1, 4, 50, 586, 6800, 72894, 659610, 3479477, 4193028, 247986, 84
- The server's own worked examples carry labels like "DR-2s", "4a2-1s", "2c3 -2s 8fe". I replayed 43 such labelled states from the docs and the two channels, and all 43 are what the label says by the table above.

---

## 4. The move counts: DR-3s, DR-2s, DR-1s, DR

Face turns with all cancelling done, using only moves that keep the DR-xs: any turn of the two faces the corners are oriented on, half turns of the other four, and slice turns written as two outer turns. So `R2` then `R L'` is `R' L'`, two turns.

### 4.1 To a real DR

Each row is a number of face turns; each column counts the kinds of DR-1s, DR-2s or DR-3s state whose shortest fix takes that many:

| Turns to a real DR | Kinds of DR-1s state | Kinds of DR-2s state | Kinds of DR-3s state |
|---:|---:|---:|---:|
| 2 | 2 | 0 | 0 |
| 3 | 4 | 0 | 0 |
| 4 | 18 | 2 | 0 |
| 5 | 60 | 32 | 0 |
| 6 | 56 | 99 | 2 |
| 7 | 0 | 172 | 14 |
| 8 | 0 | 54 | 118 |
| 9 | 0 | 24 | 80 |
| 10 | 0 | 0 | 30 |
| all | 140 | 383 | 244 |
| average turns | 5.17 | 6.83 | 8.50 |

This is the count from the state alone, with nothing to cancel against. It's over kinds, and if you didn't steer the DR-xs, every kind with the same number of slices is equally likely.

### 4.2 DR-1s to DR: all 70 layouts

A DR-1s has exactly four flipped edges, and one slice turn fixes it once those four are in the slice that turn moves. Of the eight places they can be in, four are inside that slice and four outside it, so there are 70 layouts. Take the corners on F/B, where the slice that fixes is `R L`. Each row is how many of the four flipped edges already sit in that slice; the columns count its layouts by the turns their shortest fix takes:

| Flipped edges already in the slice that fixes | Layouts | Layouts that take 2 turns | 3 turns | 4 turns | 5 turns | 6 turns |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 1 | 1 | 0 | 0 | 0 | 0 |
| 3 | 16 | 0 | 0 | 0 | 8 | 8 |
| 2 | 36 | 0 | 2 | 8 | 14 | 12 |
| 1 | 16 | 0 | 0 | 0 | 8 | 8 |
| 0 | 1 | 0 | 0 | 1 | 0 | 0 |

And the shortest example of each row:

| Flipped edges already in the slice that fixes | Shortest example: flipped edges at | Its fix |
|---:|---|---|
| 4 | DB DF UB UF | `R L` |
| 3 | BL DB DF UB | `B' U2 B R L` |
| 2 | BL DF UF BR | `B R L` |
| 1 | BL DB BR FR | `F' D2 B R L` |
| 0 | BL FL BR FR | `F B R L` |

- **Daichi is right** that 6 is the most and 7 does not exist ([15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560145175714472097)). So is Rodney's bound ([15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560294279010717737)): "Worst case requires 2qt, with at most one half-turn before/between each qt, so 4 and then the slice."
- **The distribution is not flat.** 83% of layouts need 5 or 6 turns, and the average is 5.17. The EO Meta Comparison doc's working assumption, "1 slice can be fixed in 3 moves", is 1.17 short with one slice turn cancelling (Rodney's way of counting, [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560296978137485322)) and 2.17 from the state alone, and sqAree's "more than 5 moves most of the time" ([23 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1464341592952537128)) is the accurate one. That count isn't the cost, though: the setup moves are also finish moves and the slice gets moved around in the finish, so the cost that matters is the finish (section 5).
- **3-1 isn't much worse than 2-2 here.** With three of the four already in the slice it's 5 or 6. With two it's anything from 3 to 6. With none it's 4:

  ```
  F B R L // none of the four in the slice
  ```
- All 70 layouts with a shortest fix each are in Appendix A, the list Radek B asked for.

**Simon's table.** Simon's slice-DR doc has the same count for its step 3, taking the better direction of the last trigger move: "Num Cases out of 70": 1, 4, 9, 40, 16 for 2 to 6 moves. With the same choice I get 1, 4, 13, 36, 16. The ends agree, and so does Simon's "~4.9 moves on average", but thirteen layouts have a 4-turn fix, not nine. They're at the end of Appendix A, each with its fix.

### 4.3 The steps in between

Each row is a number of face turns; each column counts the kinds of state for that step whose shortest way through takes that many. Counted from scratch:

| Turns, counted from scratch | DR-3s to DR-2s | DR-2s to DR-1s | DR-1s to DR | DR-2s to DR |
|---:|---:|---:|---:|---:|
| 2 | 244 | 209 | 2 | 0 |
| 3 | 0 | 102 | 4 | 0 |
| 4 | 0 | 72 | 18 | 2 |
| 5 | 0 | 0 | 60 | 32 |
| 6 | 0 | 0 | 56 | 99 |
| 7 | 0 | 0 | 0 | 172 |
| 8 | 0 | 0 | 0 | 54 |
| 9 | 0 | 0 | 0 | 24 |
| all kinds | 244 | 383 | 140 | 383 |

And the extra turns when your last move was a quarter turn of a side face, on the better of the two side axes: a slice about that axis merges with it (`R` then `R' L` is just `L`):

| Extra turns right after a trigger, at best | DR-3s to DR-2s | DR-2s to DR-1s | DR-1s to DR | DR-2s to DR |
|---:|---:|---:|---:|---:|
| 0 | 244 | 209 | 2 | 0 |
| 2 | 0 | 0 | 0 | 2 |
| 3 | 0 | 174 | 20 | 32 |
| 4 | 0 | 0 | 14 | 31 |
| 5 | 0 | 0 | 104 | 128 |
| 6 | 0 | 0 | 0 | 112 |
| 8 | 0 | 0 | 0 | 78 |

- **A DR-3s is always a DR-2s for free** right after the trigger, as the tutorial says: "you can always go to DR-2s in 0 moves by inserting a slice move that cancels with your last DR move".
- **DR-2s to DR-1s** is a slice with 0, 1 or 2 setup moves. Rodney's "DR-2s needs at most 2 moves to reach DR-1s" ([15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560294279010717737)) is right if you don't count the slice itself. Right after the trigger, with its last move on the better of the two side axes, it is free for 209 of the 383 kinds and costs 3 for the rest. On the other side axis it is free for 69.

---

## 5. The finish: DR-1s and DR-2s 8fe against a DR

### 5.1 How it is measured

The tutorial finishes a DR-1s like this: set up the four flipped edges, do the slice, HTR from the other side, then leave slice while slicing the `R L'` back out. Every solution it can find has the form

> (moves that keep the DR-1s) (one slice turn) (a DR finish),

read from either side. For a given DR-1s I compute the shortest solution of that form exactly: every setup from both ends, and for the DR that comes out, its optimal finish from the first study's table of all 19,508,428,800 DR states. So "finish" below is the best the method can do, the same way "optimal finish" was for a DR: **computer only**, the answer key, not what you find in an hour (5.5 has what a hand finish loses). What you take into an attempt is the difference, the penalty against a DR. For a DR-2s 8fe the form is setup, both slices one after the other, DR finish.

The states are drawn uniformly: 200,000 DR-1s and 5,000 DR-2s 8fe. That's the right weighting for a DR-xs you reached without looking past the DR-xs itself: the part of the cube the route doesn't look at is still uniformly random. Section 7.5 checks it on real scrambles.

### 5.2 By subset

The subset of a DR-xs is its corner subset, as in "4a2-1s". trangium's columns are the nissy optimal averages from the tutorial. Each row is a corner subset; "DR-1s minus DR" is how many moves longer a DR-1s of that subset finishes than a DR of the same subset:

| Corner subset | Share of states | DR: average finish, moves | DR-1s: average finish, moves | DR-1s minus DR, moves | trangium's DR-1s, nissy optimal average |
|---|---:|---:|---:|---:|---:|
| 0c0 | 0.48% | 12.28 | 14.78 | +2.50 |  |
| 4a1 | 2.9% | 12.42 | 14.95 | +2.53 | 14.8 |
| 4a2 | 2.9% | 13.35 | 15.78 | +2.43 | 15.6 |
| 4b2 | 11% | 12.68 | 15.15 | +2.47 | 14.9 |
| 2c3 | 15% | 12.92 | 15.35 | +2.43 | 15.2 |
| 4c3 | 11% | 13.49 | 15.84 | +2.35 | 15.7 |
| 0c3 | 1.4% | 14.46 | 16.67 | +2.21 |  |
| 2c4 | 23% | 13.65 | 15.91 | +2.26 | 15.5 |
| 0c4 | 0.95% | 13.67 | 15.85 | +2.17 |  |
| 4c4 | 11% | 14.40 | 16.49 | +2.09 |  |
| 2c5 | 7.6% | 14.33 | 16.36 | +2.04 |  |
| 4b5 | 11% | 14.28 | 16.33 | +2.05 |  |
| **all** | 100% | 13.58 | 15.85 | +2.27 |  |

The same for the DR-2s 8fe, where "8fe minus DR" is against the DR column above:

| Corner subset | DR-2s 8fe: average finish, moves | 8fe minus DR, moves | trangium's 8fe, nissy optimal average |
|---|---:|---:|---:|
| 0c0 | 13.03 | +0.75 |  |
| 4a1 | 13.37 | +0.95 | 13.26 |
| 4a2 | 14.29 | +0.94 |  |
| 4b2 | 13.74 | +1.06 | 13.59 |
| 2c3 | 13.99 | +1.07 | 13.80 |
| 4c3 | 14.72 | +1.23 | 14.54 |
| 0c3 | 15.70 | +1.24 |  |
| 2c4 | 14.90 | +1.25 | 14.80 |
| 0c4 | 14.89 | +1.22 |  |
| 4c4 | 15.81 | +1.41 |  |
| 2c5 | 15.62 | +1.29 |  |
| 4b5 | 15.66 | +1.38 |  |
| **all** | 14.77 | +1.19 |  |

- The penalty for a DR-1s is +2.27 overall. It's larger on the low-qt subsets (+2.53 for 4a1) than on the high ones (+2.05 for 4b5), so a DR-1s flattens the difference between subsets a little.
- My DR-1s numbers are 0.1 to 0.4 above trangium's. trangium's are true optimals, which can leave the form, and trangium says of them that "lots of optimals are not findable" ([28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1465944533656141878)). The DR column agrees with trangium's to within 0.05.
- For DR-2s 8fe the penalty is +1.19, 0.1 to 0.2 above trangium's on each of the five subsets trangium measured. The 8fe sample is small for the rare subsets. The number of 8fe states sampled in each:

  | Corner subset | 0c0 | 0c4 | 0c3 |
  |---|---:|---:|---:|
  | 8fe states sampled | 35 | 45 | 50 |

### 5.3 In odds

Each row is a finish length; each column is the share of states of that kind that finish in that many moves or fewer, and the last row is the average:

| Finish in, moves | DR | DR-2s 8fe | DR-1s | DR-1s that one slice turn fixes | DR-1s that needs 5 or 6 turns to DR |
|---|---:|---:|---:|---:|---:|
| 10 or less | 0.74% | 0.06% | 0.01% | 0.24% | <0.01% |
| 11 or less | 3.6% | 0.30% | 0.07% | 1.2% | 0.03% |
| 12 or less | 15% | 2.6% | 0.40% | 3.9% | 0.27% |
| 13 or less | 44% | 12% | 2.0% | 16% | 1.5% |
| 14 or less | 80% | 39% | 9.0% | 46% | 7.4% |
| 15 or less | 99% | 73% | 32% | 81% | 29% |
| 16 or less | 99.9% | 97% | 73% | 99% | 71% |
| 17 or less | 99.9% | 99.9% | 98% | 100% | 98% |
| 18 or less | 100% | 100% | 100% | 100% | 100% |
| average finish, moves | 13.58 | 14.77 | 15.85 | 14.53 | 15.92 |

And adding the length of what you did before, the chance of a whole solution in $N$ moves or less. Each row is what you have and how long it took; each column is the share that ends in that many moves or fewer:

| You have | Solution in 18 or less | 19 or less | 20 or less | 21 or less |
|---|---:|---:|---:|---:|
| a DR in 9 | 0.14% | 0.74% | 3.6% | 15% |
| a DR in 10 | 0.03% | 0.14% | 0.74% | 3.6% |
| a DR in 11 | <0.01% | 0.03% | 0.14% | 0.74% |
| a DR in 12 | <0.01% | <0.01% | 0.03% | 0.14% |
| a DR-1s in 6 | 0.40% | 2.0% | 9.0% | 32% |
| a DR-1s in 7 | 0.07% | 0.40% | 2.0% | 9.0% |
| a DR-1s in 8 | 0.01% | 0.07% | 0.40% | 2.0% |
| a DR-1s in 9 | <0.01% | 0.01% | 0.07% | 0.40% |
| a DR-2s 8fe in 7 | 0.30% | 2.6% | 12% | 39% |
| a DR-2s 8fe in 8 | 0.06% | 0.30% | 2.6% | 12% |
| a DR-2s 8fe in 9 | 0 of 5,000 | 0.06% | 0.30% | 2.6% |
| a DR-2s 8fe in 10 | 0 of 5,000 | 0 of 5,000 | 0.06% | 0.30% |

The same rows, longer solutions:

| You have | Solution in 22 or less | 23 or less | 24 or less |
|---|---:|---:|---:|
| a DR in 9 | 44% | 80% | 99% |
| a DR in 10 | 15% | 44% | 80% |
| a DR in 11 | 3.6% | 15% | 44% |
| a DR in 12 | 0.74% | 3.6% | 15% |
| a DR-1s in 6 | 73% | 98% | 100% |
| a DR-1s in 7 | 32% | 73% | 98% |
| a DR-1s in 8 | 9.0% | 32% | 73% |
| a DR-1s in 9 | 2.0% | 9.0% | 32% |
| a DR-2s 8fe in 7 | 73% | 97% | 99.9% |
| a DR-2s 8fe in 8 | 39% | 73% | 97% |
| a DR-2s 8fe in 9 | 12% | 39% | 73% |
| a DR-2s 8fe in 10 | 2.6% | 12% | 39% |

Read these two tables by finding rows that match. Each row below is one thing you can have, and the DRs it matches:

| What you have | Where it sits |
|---|---|
| a DR-1s in 7 | between a DR in 9 and a DR in 10, about midway |
| a DR-1s in 8 | between a DR in 10 and a DR in 11 |
| a DR-2s 8fe in 9 | a little behind a DR in 10 |

So:

- **DR-1s in $N$ is about a DR in $N + 2.3$**, at equal odds for finishes of 13 to 16 (2.27 on the average). Rodney's "+3/+4 penalty for -1/-2 slice" ([30 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1466667769834508476)) is a bit hard on the DR-1s if you finish it well, and tseitsei89's later "in reality around 3 moves worse" ([7 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1469596164188930221)) is what it turns into when you don't find the best finish (5.5).
- **DR-2s 8fe in $N$ is about a DR in $N + 1.19$.**

### 5.4 Which DR-1s are the good ones

People said two things you can see on a DR-1s matter: how far it is from a DR, and how the four flipped edges split between the two slices they belong to (Rodney, [28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1466198780582826057): "3-1 is bad because it requires 2 QT", "2-2 requires 1 QT"). Those are the same thing seen from the two sides of the scramble: the four flipped edges all belong to one slice exactly when, on the other side, they all sit in one slice. So one table covers both, the fewest turns to a real DR from whichever side is better. Each row is the DR-1s whose better side is that many turns from a real DR; "minus a DR's" is its average finish minus a random DR's:

| Fewest turns to a real DR, from the better side | Share of DR-1s | Average finish, moves | Average finish minus a DR's, moves | Finish in 14 or less | Finish in 15 or less |
|---:|---:|---:|---:|---:|---:|
| 2 | 2.8% | 14.52 | +0.94 | 46% | 81% |
| 3 | 5.5% | 15.15 | +1.57 | 25% | 59% |
| 4 | 23% | 15.74 | +2.16 | 11% | 36% |
| 5 | 53% | 15.96 | +2.38 | 6.1% | 27% |
| 6 | 16% | 16.12 | +2.54 | 4.1% | 21% |

- **The DR-1s to want is the one a single slice turn fixes, from one side or the other**: +0.94, a little less than a DR-2s 8fe costs. It's 2.8% of them.
- **Past that, the layout doesn't matter much.** From 4 turns to 6 the average finish moves by 0.38. A DR-1s that's 6 from a real DR isn't 4 worse than one that's 2 away, because the setup moves are also finish moves.
- **"Extra-good" is two cases.** Rodney's extra-good DR-1s is four flipped edges all belonging to one slice ([19 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474226073247027220)), which Rodney put at "just 1-2 moves worse than full DR". When that slice is the one that fixes, it's the first row. When it's the other slice, the four sit together in the wrong slice and the finish is +2.10, no better than an ordinary DR-1s. Averaged over the two it's +1.52.

  ```
  F B R L // the fix when the four sit in the wrong slice
  ```

### 5.5 What a hand finish loses

The best solution has its slice within 4 moves of one end for at least 64% of DR-1s states, which is trangium's "pretty high chance that the slice ends up within 4 moves of the start or the end" ([30 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1466668019790123167)). But it isn't always the end you're on. If the setup has to be at most 4 moves and on the side where you found the DR-1s, with any DR finish after it, the average is 16.91, 1.06 more, and only 38% of states keep their best finish. So try the setup from both sides before you judge a DR-1s.

How often a person finds these finishes isn't something I can compute. trangium's findability tables in the tutorial are the data there is: for 4b2-1s, optimal findable 51% of the time and optimal + 1 another 32%.

### 5.6 DR-2s 8fe and the DR that ends in U R L

The tutorial's cheapest way to a DR-2s 8fe is a normal DR that ends in something like `U R L`: do `D` instead and you're at an 8fe two moves earlier. An 8fe in $N$ is worth a DR in $N + 1.19$, so the DR in $N + 2$ that ends that way is worth a DR in about $N + 1.2$. **The ending is worth about 0.8 of a move** with the best finish of this form, and 0.9 to 1.15 with trangium's optimal averages. trangium put it at "1 to 1.3 moves better" ([6 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1469483553963380829)) and count quackula at "one move better" ([6 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1469483105659392232)): about one move stands.

By subset the 8fe penalty runs from +0.95 (4a1) to +1.41 (4c4). Unlike the DR-1s penalty it goes up with the qt count, so the `U R L` ending is worth about a move on the low-qt subsets and about 0.6 on 4c4.

---

## 6. Getting one

### 6.1 How often there is a slice-EO skip

There are 9 pairs of a slice and an axis, each in two flavours (all oriented, all misoriented), on normal and on inverse. Whether a scramble has a skip only depends on which kind of edge sits where and on the orientations: 70,963,200 equally likely configurations. Counting all of them: each row is a number of skips and each column the share of scrambles that have that many, for skips on normal or on both sides, any flavour or all-oriented only. The last row is an average count, not a share:

| Slice-EO skips on the scramble | Any skip, on normal | Any skip, on normal or inverse | All-oriented skips only, on normal | All-oriented skips only, on normal or inverse |
|---|---:|---:|---:|---:|
| at least one | 69% | 79% | 43% | 56% |
| exactly 0 | 31% | 21% | 57% | 44% |
| exactly 1 | 37% | 19% | 31% | 24% |
| exactly 2 | 23% | 21% | 9.5% | 17% |
| exactly 3 | 7.3% | 14% | 1.6% | 7.5% |
| 4 or more | 2.0% | 25% | 0.24% | 7.0% |
| average number | 1.12 | 2.25 | 0.56 | 1.12 |

- **68.7953% of scrambles have at least one skip on normal, and 79.3147% have one on normal or inverse.** That's wen's question.
- Each single skip (one slice, one axis, one flavour, one side) has chance $1/16$, so $1/8$ for a slice and an axis with either flavour, like tseitsei89 and count quackula worked out ([3 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1533722203646988318), [3 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1533721112813244467)). The skips are far from independent: the average is 2.25 per scramble over both sides, but 21% of scrambles have none.
- The tutorial's "often 1-2 on a scramble" is right.

And for one given slice, the moves to a slice EO on some axis, over all 7,920 ways its four pieces can sit. Each row is the kind of slice EO you'll take; the columns are the share of those placements that need that many moves:

| Slice EO wanted | Already there (a skip) | 1 move | 2 moves | 3 moves | 4 moves |
|---|---:|---:|---:|---:|---:|
| any axis, oriented or misoriented | 32.2% | 38.3% | 29.5% | 0 | 0 |
| any axis, oriented only | 17.0% | 25.5% | 51.6% | 5.9% | 0 |
| one given axis, oriented or misoriented | 12.5% | 19.7% | 61.3% | 6.5% | 0 |
| one given axis, oriented only | 6.2% | 10.7% | 47.2% | 32.8% | 3.0% |

FakeMMAP's "never more than 2 moves away", "No matter which slice you pick" ([25 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1465100277303476304), [25 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1465100381318025409)) is exact, and so is the EO Meta Comparison doc's "partial EO in <=2 is guaranteed", as long as all-misoriented counts. All-oriented only, it takes 3 moves 5.9% of the time.

### 6.2 From a skip to a DR-1s

After the slice EO the tutorial looks for rzp and DR "like normal", ignoring flipped edges and centers. Normal means no quarter turns of the EO axis's two faces, which keeps every edge's orientation for that axis. Under exactly that rule, here's the nearest DR-1s from every state with a skip, by the kind of skip. The distances are exact searches, **computer only**; which skips can give a DR-1s at all is something you check at the table by counting bad edges. Each row is a kind of skip, with whether a DR-1s can be reached at all and how far it is on average:

| The skip | A route exists, share of such skips | Average moves, when there is one |
|---|---:|---:|
| another axis than the slice's own, all oriented | always | 7.68 |
| another axis, all misoriented | 55% | 7.80 |
| the slice's own axis, all oriented | 55% | 7.47 |
| the slice's own axis, all misoriented | never | |

And how often the nearest DR-1s is within that many moves, over all skips of the kind (the kind that never gets there is left out):

| The skip | In 5 moves or less, share of all such skips | 6 or less | 7 or less | 8 or less | 9 or less |
|---|---:|---:|---:|---:|---:|
| another axis than the slice's own, all oriented | 1.0% | 7.1% | 36% | 88% | 99.9% |
| another axis, all misoriented | 0.48% | 3.2% | 17% | 45% | 55% |
| the slice's own axis, all oriented | 0.93% | 6.0% | 26% | 51% | 55% |

- **Oriented, on an axis that is not the slice's own** (E-slice edges oriented on F/B, say): there's always a route. It's 7 or less for 36% of skips and 8 or less for 88%. For comparison, from a full EO the nearest real DR on one given axis is 7.80 moves away on average under the same rule. So in route length a skip like this is an EO that cost nothing, and in finish it's a DR-1s. That's the sense of Rodney's "sliceEO in N is as good as regular EO in N+3" ([3 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1468273993105805364)); with the finish penalty at 2.3 the 3 is a little generous to the normal EO, before you count how many of each you get to try.
- **Misoriented on such an axis**: without breaking that axis's EO a route exists only when exactly four of the other eight edges are bad, so that the axis has 8 bad edges in all. That's 55% of these skips (70 in 128). trangium ([8 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1480310254129516617)): "you MUST have 8 bad on that axis for even a chance at dr-1s". Rodney's "55%" ([1 May 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1499635961015963751)) is this number.
- **Oriented on the slice's own axis** (E-slice edges oriented on U/D): 55%, when as many M-slice pieces as S-slice pieces are bad. The same states can reach a real DR on that colour without U or D quarter turns, 9.19 moves away on average.
- **Misoriented on the slice's own axis**: never, with or without the extra quarter turns below. Daichi's "misoriented sEOs are just worse overall" ([10 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1536429112736882828)) is right in both families.

Allowing quarter turns of the EO axis when they miss the slice pieces (the tutorial's tip 2) fully opens the two half-open kinds of skip, misoriented on another axis and oriented on the slice's own, but doesn't shorten much. Allowing any move shortens it by a quarter move. Each row is a kind of skip under one move rule, "strict" being the rule above:

| The skip | Moves allowed | A route exists, share of such skips | Average moves, when there is one |
|---|---|---:|---:|
| another axis than the slice's own, all oriented | strict | always | 7.68 |
| another axis than the slice's own, all oriented | quarter turns of the EO axis when they miss the slice pieces | always | 7.59 |
| another axis than the slice's own, all oriented | any turns | always | 7.41 |
| another axis, all misoriented | strict | 55% | 7.80 |
| another axis, all misoriented | quarter turns of the EO axis when they miss the slice pieces | always | 8.08 |
| another axis, all misoriented | any turns | always | 7.65 |
| the slice's own axis, all oriented | strict | 55% | 7.47 |
| the slice's own axis, all oriented | quarter turns of the EO axis when they miss the slice pieces | always | 7.77 |
| the slice's own axis, all oriented | any turns | always | 7.43 |
| the slice's own axis, all misoriented | strict | never | |
| the slice's own axis, all misoriented | quarter turns of the EO axis when they miss the slice pieces | never | |
| the slice's own axis, all misoriented | any turns | always | 7.88 |

And how often it's within that many moves, same rows:

| The skip | Moves allowed | In 5 moves or less, share of all such skips | 6 or less | 7 or less | 8 or less | 9 or less |
|---|---|---:|---:|---:|---:|---:|
| another axis than the slice's own, all oriented | strict | 1.0% | 7.1% | 36% | 88% | 99.9% |
| another axis than the slice's own, all oriented | quarter turns of the EO axis when they miss the slice pieces | 1.1% | 8.0% | 41% | 91% | 99.9% |
| another axis than the slice's own, all oriented | any turns | 1.3% | 10% | 51% | 97% | 99.9% |
| another axis, all misoriented | strict | 0.48% | 3.2% | 17% | 45% | 55% |
| another axis, all misoriented | quarter turns of the EO axis when they miss the slice pieces | 0.52% | 3.8% | 22% | 68% | 98% |
| another axis, all misoriented | any turns | 0.73% | 6.1% | 37% | 92% | 99.9% |
| the slice's own axis, all oriented | strict | 0.93% | 6.0% | 26% | 51% | 55% |
| the slice's own axis, all oriented | quarter turns of the EO axis when they miss the slice pieces | 1.0% | 7.1% | 34% | 81% | 99.4% |
| the slice's own axis, all oriented | any turns | 1.3% | 10% | 49% | 96% | 99.9% |
| the slice's own axis, all misoriented | any turns | 0.26% | 2.8% | 24% | 85% | 99.9% |

### 6.3 To a DR-2s 8fe: the same problem as a DR

**Getting to a DR-2s 8fe is getting to a DR with the pieces renamed.** An 8fe has its corners and slice edges placed like a DR on one pair of faces, in the colours of another pair. Move every piece a quarter turn around the third axis, leave the centres where they are, and flip every edge in its place: the 8fe turns into a real DR. Do that to any position, rename the faces of a move sequence by the same quarter turn, and reaching the 8fe turns into reaching the DR. Edges that are good for the third axis stay good, so an EO on that axis carries over too. Counted over every position with a full EO, with moves that keep it. Each row is a distance, and the two columns count the positions that far from the real DR and from the 8fe:

| Moves from a full EO | Positions that many moves from the real DR | Positions that many moves from the DR-2s 8fe |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 2 | 2 |
| 2 | 17 | 17 |
| 3 | 134 | 134 |
| 4 | 1,065 | 1,065 |
| 5 | 8,190 | 8,190 |
| 6 | 54,694 | 54,694 |
| 7 | 267,576 | 267,576 |
| 8 | 560,568 | 560,568 |
| 9 | 187,204 | 187,204 |
| 10 | 3,114 | 3,114 |
| all 1,082,565 positions, average | 7.80 | 7.80 |

- **From an EO, the 8fe is exactly as far as the DR**: the same distribution, 7.80 on average. That's the tutorial's route 3: do the normal EO, then solve the wrong-coloured DR. Each of the EO's two DR axes has one, so an EO has four targets instead of two, and the two extra ones cost 1.19 more in the finish.
- **With any moves it is the same, target by target.** A scramble has twelve 8fe (two for each colour, on normal and on inverse) against six DRs, and each is as far away as a DR is. That's why the shortest 8fe of a scramble comes 0.33 of a move before its shortest DR in 6.4: there are twice as many, and none of them is closer. (Checked on 4,000 random positions: the distance to the 8fe is the distance of the renamed position to the DR every time.)
- **What doesn't carry over is the finish.** The renaming doesn't take the solved cube to the solved cube, and the two slice turns are there to make up the difference: +1.19 (section 5).

**So a slice-EO skip isn't what gets you an 8fe.** By the kind of skip, keeping that axis's EO: whether there's a route to an 8fe, and how long it is on average:

| The skip | A route exists, share of such skips | Average moves, when there is one |
|---|---:|---:|
| another axis than the slice's own, all oriented | 0.78% | 7.80 |
| another axis, all misoriented | 55% | 9.19 |
| the slice's own axis, all oriented | never | |
| the slice's own axis, all misoriented | 1.6% | 7.80 |

And how often it's within that many moves, over all skips of the kind:

| The skip | In 5 moves or less, share of all such skips | 6 or less | 7 or less | 8 or less | 9 or less |
|---|---:|---:|---:|---:|---:|
| another axis than the slice's own, all oriented | <0.01% | 0.05% | 0.24% | 0.64% | 0.78% |
| another axis, all misoriented | 0.02% | 0.14% | 1.1% | 8.1% | 35% |
| the slice's own axis, all misoriented | 0.01% | 0.09% | 0.48% | 1.3% | 1.6% |

- **An oriented skip** leads to an 8fe only when the rest of the axis is oriented as well (0.78% of such skips, 1 in 128), and that's just a normal EO. The skip adds nothing.
- **A misoriented skip on an axis with 8 bad edges** (the four slice edges and four of the other eight, 55% of misoriented skips) is the one separate way in. From there an 8fe is 9.19 moves away on average, against 7.80 from an EO, and you spend no moves on an EO first. It's 8 or less for 8.1% of those skips.

### 6.4 What exists, with any moves

Any moves, linear on one side, over 2,000,000 random scrambles (three colours, normal and inverse). **Computer only**: the shortest of each over every route, the answer key for what exists. Each row is a target; the columns are the average length of the scramble's shortest one and the share of scrambles where it's that short:

| Shortest on the scramble | Average length, moves | In 6 moves or less | 7 or less | 8 or less | 9 or less |
|---|---:|---:|---:|---:|---:|
| a real DR | 8.76 | 0.30% | 3.3% | 28% | 92% |
| a DR-2s 8fe | 8.43 | 0.60% | 6.6% | 50% | 99.5% |
| a DR-1s | 6.81 | 26% | 89% | 99.9% | 100% |
| any DR-xs | 6.46 | 48% | 98% | 100% | 100% |

- The first row is wen's other question ([9 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1547198328792420393)), "Is the distribution for scrambled->DR movecount known?". The row is the best of six; per colour it's exactly this, over the 2,217,093,120 cosets (0 to 12 moves):

  1, 4, 50, 592, 7156, 87236, 1043817, 12070278, 124946368, 821605960, 1199128738, 58202444, 476
- The last row is trangium's "almost always a linear 7-mover on some axis and side, around half the time a 6-mover, and pretty much never a 5-mover" ([23 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1464482670200488294)): 98%, 48%, and 7.3% for 5 or less.
- A DR-1s exists about 2.0 moves earlier than a real DR, and costs 2.27 in the finish. That's the whole trade in two numbers: on average it's close to even, so it pays when you find the short ones.

### 6.5 From an EO pattern to a kind

If the route keeps the EO of an axis, the EO pattern you start from decides what you can land on. Appendix B has the full table: for every pattern that is uniform by slice (each slice's four pieces all good or all bad) and each pair of faces for the corners, what the DR-xs is. Rodney's list of patterns that guarantee an extra-good case ([19 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474226073247027220)) and count quackula's two lists (the 12-bad notes and the guaranteed-fix cases) can be read straight off it. All of them check out except one line, the 12-bad one in Rodney's list (section 8).

---

## 7. On 500 real scrambles

The same 500 random-state scrambles as the tally on the first study's examples page.

- **Normal DRs**: every DR of 12 moves or less that goes through an EO of 5 moves or less (cubelib-cli, NISS allowed; it lists no longer EOs), each finished optimally. Same run as the first study.
- **DR-xs**: every DR-1s of 8 moves or less and every DR-2s 8fe of 9 or less that starts from a slice-EO skip or a one-move slice EO, on normal or on inverse, and then keeps that axis's EO. That's the plain version of the tutorial's route (no EO-changing triggers, no NISS inside the route), taken exhaustively, so the counts are a floor on what's there. Plus every DR-2s 8fe of 9 or less after a normal EO of 4 moves or fewer (the wrong-colour DR, and the DR that would end in `U R L`).
- **Finishes**: as in section 5, the best of the method's form, written out as a full solution and replayed on the scramble: 31,529 DR-1s and 5,918 DR-2s 8fe solutions, all correct. For the 8fe here I search setups up to 3 moves from either end, which finds the best for 85% of the random sample and is 0.16 moves off on average.

Like in the first study, every finish is the answer key, **computer only**, not what you find in an hour, and nobody finishes this many. Read the counts as the size of the haystack and the last column of 7.2 as how good each straw is.

### 7.1 What is there

Each row is a kind of thing to finish and a length; the columns are the share of the 500 scrambles that have at least one and how many there are on average:

| On a scramble | Share of the 500 that have one | Average number per scramble |
|---|---:|---:|
| a normal DR of 9 moves or less | 66% | 6.1 |
| a normal DR of 10 or less | 98% | 69.7 |
| a normal DR of 11 or less | 100% | 720.7 |
| a DR-1s of 6 or less from a slice-EO skip | 8.2% | 0.4 |
| a DR-1s of 7 or less from a slice-EO skip | 32% | 4.2 |
| a DR-1s of 8 or less from a slice-EO skip | 62% | 44.8 |
| a DR-1s of 6 or less from a skip or a one-move slice EO | 11% | 0.5 |
| a DR-1s of 7 or less from a skip or a one-move slice EO | 46% | 6.0 |
| a DR-1s of 8 or less from a skip or a one-move slice EO | 89% | 63.1 |
| a DR-2s 8fe of 7 or less (from a slice EO or an EO of 4 or less) | 2.4% | 0.1 |
| a DR-2s 8fe of 8 or less (from a slice EO or an EO of 4 or less) | 14% | 1.0 |
| a DR-2s 8fe of 9 or less (from a slice EO or an EO of 4 or less) | 56% | 11.8 |

- **Nine scrambles in ten have a DR-1s of 8 or less** from a skip or a one-move slice EO, and there are 63.1 of them on average, nearly as many as there are normal DRs of 10 or less.
- **Nearly half have one of 7 or less** (46%), and a 6 is there on 11%. tseitsei89's "I can usually find some DR-fe in 8 moves. Occasionally 7." ([28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1465952080756871423)) was about what you find by hand; this is what's there by the plain route.
- Skips alone carry most of it; one-move slice EOs add a little under a third.
- **The 8fe rows** are a floor too, and you don't need a skip for one (6.3). There are 482 DR-2s 8fe of 8 moves or fewer on these scrambles. By where the route starts:

  | Where the route starts | DR-2s 8fe of 8 or less |
  |---|---:|
  | a misoriented slice-EO skip | 238 |
  | a one-move slice EO | 70 |
  | an EO of 4 moves or less | 174 |

  Each is counted once, under the first of those three that reaches it, and I didn't take EOs of 5 moves for the 8fe, so the split leans towards the skips.

### 7.2 What each one is worth

For each kind of thing you could finish, how often its solution is as short as the best solution any normal DR of 12 or less gives on that scramble. The last column is the same share turned around, how many you finish for one to get there:

| What you finish | How many per scramble | Share that reach the scramble's best normal-DR solution | One in this many reaches it |
|---|---:|---:|---:|
| a DR-1s of 6 or less | 0.5 | 8.6% | 12 |
| a DR-2s 8fe of 8 or less | 1.0 | 3.7% | 27 |
| a normal DR of 9 or less | 6.1 | 2.4% | 41 |
| a DR-1s of 7 | 5.4 | 2.1% | 49 |
| a DR-2s 8fe of 9 | 10.9 | 0.66% | 151 |
| a normal DR of 10 | 63.6 | 0.49% | 202 |
| a DR-1s of 8 | 57.1 | 0.48% | 210 |
| a normal DR of 11 | 651.0 | 0.11% | 952 |
| a normal DR of 12 | 6,400.7 | 0.02% | 4,031 |

The table is sorted by that share. Rows 2 to 4 (a DR-2s 8fe of 8 or less, a normal DR of 9 or less, a DR-1s of 7) are within sampling error of each other. So:

- a DR-1s of 7 is worth about what a normal DR of 9 or less is;
- a DR-1s of 8 is worth 4.5 eleven-move DRs and 0.96 of a 10-move DR;
- a DR-2s 8fe of 9 comes out a little better than a 10-move DR on these scrambles.

That's kinder to DR-xs than the $N + 2.3$ of section 5, because on real scrambles the finish often cancels into the last move of the route (by 0.20 moves on average for a DR-1s).

### 7.3 What it does to the result

Over the 491 scrambles that have a normal DR of 10 or less (the first study's base), the best solution when you finish. Each row is a set of things you finish; the columns are how many that is, the average best solution, and the share of these scrambles where it's 20 or less and 19 or less:

| You finish | Things to finish, per scramble | Average best solution, moves | Best solution in 20 or less | 19 or less |
|---|---:|---:|---:|---:|
| every normal DR of 10 or less | 71 | 20.62 | 45% | 18% |
| normal DRs of 10 or less, and every DR-1s of 7 or less | 77 | 20.55 | 47% | 19% |
| normal DRs of 10 or less, and every DR-1s of 8 or less | 135 | 20.42 | 50% | 22% |
| normal DRs of 10 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less | 147 | 20.41 | 51% | 22% |
| every normal DR of 11 or less | 733 | 20.04 | 63% | 29% |
| normal DRs of 11 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less | 809 | 19.95 | 68% | 32% |
| every normal DR of 12 or less | 7,244 | 19.56 | 84% | 45% |
| normal DRs of 12 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less | 7,319 | 19.52 | 85% | 47% |

- On top of every normal DR of 10 or less, which gives 20.62 on average. Each row adds one set, on top of the row above, except the 11-move DRs, which go on the normal DRs of 10 alone; the last column is how much the average drops from what it builds on:

  | Add | More things to finish per scramble | Average best solution after, moves | Shorter by, moves |
  |---|---:|---:|---:|
  | the DR-1s of 7 or less | 6 | 20.55 | 0.07 |
  | those of 8 as well | 58 | 20.42 | 0.13 |
  | the 11-move DRs (instead) | 662 | 20.04 | 0.58 |
- Once every 11-mover is finished, DR-xs adds 0.09; once every 12-mover is, 0.04. Mostly DR-xs gets the same quality from fewer and shorter things to look at. Now and then it finds better, as the next table shows.

Scramble by scramble, over all 500. Each row is a budget for the normal DRs; the columns are the share of scrambles where the best DR-xs solution is shorter, equal, or longer:

| Against the best through a normal DR of | Best DR-xs solution shorter, share of scrambles | Equal | Longer, or no DR-xs |
|---|---:|---:|---:|
| 10 moves or less | 16% | 22% | 62% |
| 11 moves or less | 8.4% | 14% | 78% |
| 12 moves or less | 3.4% | 9.8% | 87% |

### 7.4 Against 5-move EOs

The open question: once you've done the EOs of 4 or less, are slice EOs a better use of the time than more 5-move EOs? tseitsei89's take ([4 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1534105529683542047)): "For sEO I currently believe skips are better than 5 move EOs but 1 movers might not be."

Counting EOs the way cubelib-cli does (every way to write one, with NISS):

- a scramble has 17 EOs of 4 moves or less and 244 of 5 or less; 26 of the 500 have none of 4 or less;
- the DRs of 10 or less that come from EOs of 4 or less are 49 per scramble, and the 5-move EOs bring that to 70.

Over the 418 scrambles that have a DR of 10 or less from an EO of 4 or less, here's what each set of checks gives. Each row is what you check and finish; the columns are how many normal EOs and how many things to finish that is, and the average best solution:

| You check and finish | Normal EOs to check, per scramble | Things to finish, per scramble | Average best solution, moves |
|---|---:|---:|---:|
| EOs of 4 or less: every DR of 10 or less | 20 | 58 | 21.13 |
| EOs of 4 or less: DRs of 10 or less, and every DR-1s of 7 or less from a slice EO | 20 | 65 | 20.96 |
| EOs of 4 or less: DRs of 10 or less, and every DR-1s of 8 or less from a slice EO | 20 | 129 | 20.77 |
| EOs of 4 or less: DRs of 10 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less | 20 | 143 | 20.72 |
| EOs of 5 or less: every DR of 10 or less | 273 | 82 | 20.42 |
| EOs of 5 or less: DRs of 10 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less | 273 | 167 | 20.22 |

And with the DRs of 11 as well (470 scrambles), same columns:

| You check and finish | Normal EOs to check, per scramble | Things to finish, per scramble | Average best solution, moves |
|---|---:|---:|---:|
| EOs of 4 or less: every DR of 11 or less | 18 | 532 | 20.65 |
| EOs of 4 or less: DRs of 11 or less, and every DR-1s of 7 or less from a slice EO | 18 | 538 | 20.57 |
| EOs of 4 or less: DRs of 11 or less, and every DR-1s of 8 or less from a slice EO | 18 | 598 | 20.47 |
| EOs of 4 or less: DRs of 11 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less | 18 | 610 | 20.44 |
| EOs of 5 or less: every DR of 11 or less | 255 | 763 | 20.00 |
| EOs of 5 or less: DRs of 11 or less, every DR-1s of 8 or less and every DR-2s 8fe of 9 or less | 255 | 841 | 19.90 |

- **The 5-move EOs are worth 0.71** on the average result at this budget, and they're about 253 more EOs to go through.
- **The slice-EO routes are worth 0.36** from the DR-1s of 8 or less (0.17 from those of 7 or less alone), and what you look through to get them is the slice-EO skips (2.25 per scramble on average over both sides) and the one-move slice EOs. No normal EO is added.
- **They combine**: both together give 20.22, 0.91 better than the start. That's less than the two gains added, because they often get to the same length. Neither replaces the other.
- **Per thing finished the 5-movers do better**: their gain comes from 24 more DRs to finish, the slice-EO gain from 71 more DR-1s. The slice EOs win on what you have to look through to get there.

This fits tseitsei89's order, sub-5 EOs first, then the slice-EO skips, then the 5-movers ([3 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1468181849300795445)), on one condition: a skip and the DR-1s behind it have to be quick to find. The slice-EO routes give about half of what all the 5-move EOs give, for far fewer starts. What that costs in minutes is the part these tables can't tell you, and it's where the doubts were: zakimoshi's "isn't actually a very cost effective strategy time wise" ([26 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1476697849600409620)), JTuu's "if it's even close, I feel like 5-move eos win for time management reasons" ([4 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1534117582104166441)).

### 7.5 Do real DR-xs finish like random ones?

Each row is a kind and route length on the 500 scrambles, against the uniform sample of section 5 finished with the same setup search:

| Kind and length | Number on the 500 scrambles | Their average finish, moves | Average finish of the uniform sample, moves | Setup searched, real and sample alike |
|---|---:|---:|---:|---|
| DR-1s in 6 | 228 | 16.04 | 15.85 | any length from either end |
| DR-1s in 7 | 2,719 | 15.99 | 15.85 | any length from either end |
| DR-1s in 8 | 28,554 | 15.93 | 15.85 | any length from either end |
| DR-2s 8fe in 7 | 36 | 15.58 | 14.92 | up to 3 moves from either end |
| DR-2s 8fe in 8 | 444 | 15.00 | 14.92 | up to 3 moves from either end |
| DR-2s 8fe in 9 | 5,436 | 14.95 | 14.92 | up to 3 moves from either end |

Close to it. A DR-1s you reach in few moves finishes slightly worse than a random one, by a tenth of a move or two. The 8fe ones of 8 and 9 moves finish about like random ones under the same 3-move setup search; the few of 7 moves finish worse.

### 7.6 Time

What these checks cost in an attempt isn't something the tables can tell you. What people wrote:

- "Computing orientation for 4 edges" "takes like 2 seconds" (tseitsei89, [4 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1468714183318048799), [4 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1468714083174973603)), and there are 9 slice-and-axis pairs to look at per side;
- "finding all the non-EO dr-fe's in like 5-10 mins" (trangium, [19 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1462954196755153113));
- a normal EO "takes 15 to 30 seconds" to check (Dunni, [25 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1476165481873408121)).

You see a slice-EO skip directly, but you still have to find a DR-1s from it the way you find a DR from an EO, and then finish it with a method fewer people have practised.

---

## 8. The claims, checked

Everything said that a computer can settle, and what the numbers say. Wherever something is refuted or a case is claimed to exist, there's a scramble. Each row is one claim, who made it, and the verdict:

| Claim | Who | Verdict |
|---|---|---|
| DR-1s to DR is 6 moves at most, no 7 | Daichi, [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560144143441854566), [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560145175714472097) | **True.** Exactly 2 to 6 turns over the 70 layouts (4.2). A 6: `U R2 F2 D' B2 U2 L2 D R' L' B' L2 U2 F2` gives a DR-1s whose shortest fix is 6 turns. |
| The DR-1s to DR distribution is "basically flat", 3 moves is the median | Rodney, [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560294279010717737), [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560296978137485322) | **No.** 1, 2, 9, 30, 28 of 70 for 2 to 6 turns. Rodney's 3 is one half turn, one quarter turn and the slice with one of its two turns cancelling; counted that way the median layout is 4, and 5 from scratch. |
| "DR-2s needs at most 2 moves to reach DR-1s" | Rodney, [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560294279010717737) | **True** for the setup: 0, 1 or 2 moves, then the slice (4.3). |
| From DR-3s you get DR-2s in 0 moves with a slice that cancels with the last DR move | tseitsei89's tutorial | **True** for all 244 kinds of DR-3s. |
| The rule for the number of slices from centers and flipped edges | trangium's dr-fe examples doc, Rodney [22 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1464027237656563783), the tutorial | **True**, all 768 kinds (section 3). |
| "1 slice can be fixed in 3 moves, and 2 slices can be fixed in 5 moves" | EO Meta Comparison doc (an assumption, stated as one) | As move counts to a real DR, about a move short with one slice turn cancelling, as Rodney counts the 3 (4.17 and 5.83 on average), and about 2 short from the state alone (5.17 and 6.83). As finish penalties, 3 is a little high for a DR-1s (+2.27) and 5 much too high for a DR-2s 8fe (+1.19). |
| "UD colors on the RL faces will result in 8 flipped edges, which can be fixed with U\* D\* R\* L\*, with a guaranteed -2 cancellation", "This effectively adds +2 to the moves to reach DR" | EO Meta Comparison doc, Off-Axis DR | **True** as moves to DR. Counted as finish length the 8-flipped case costs less: a DR-2s 8fe finishes 1.19 longer than a DR, so the off-axis table, which charges the full +2, undersells that case by about a move. |
| A DR-1s finish is about 2.2 to 2.4 longer than a DR's on optimal; a DR-2s 8fe about 1 | trangium, in the tutorial and [28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1466202453052494118), [6 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1469525403927580754) | **Consistent.** trangium's are optimals. With the best finish of the method's form, on 200,000 and 5,000 states: +2.27 and +1.19, 0.1 to 0.4 above trangium's by subset. |
| "8 move DR-1s is on average better than an 11 move DR but worse than 10 move DR" | the tutorial | **Holds** with these finishes: at +2.27 an 8-move DR-1s is 0.27 behind a 10-move DR and 0.73 ahead of an 11 (5.3). |
| 3-1 is bad, 2-2 is good, 4-0 is great | Rodney [28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1466198780582826057), tseitsei89 [28 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1466020882320461856) | **Right order, small effect** except for one case: 16.05, 15.78, 15.10 average finish, and the 4-0 is only good when the slice is the one that fixes (5.4). |
| An extra-good DR-1s is "just 1-2 moves worse than full DR" | Rodney, [19 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474226073247027220) | **On average**, +1.52: +0.94 when the four are in the slice that fixes, +2.10 when they are in the other one. |
| Slice EO for a given slice "is never more than 2 moves away"; "partial EO in <=2 is guaranteed" | FakeMMAP, [25 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1465100277303476304); EO Meta Comparison doc | **True**, exactly, counting all-misoriented as a slice EO (6.1). |
| A slice-EO skip for one slice and axis has chance 1 in 8 | tseitsei89, count quackula, [3 Aug 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1533722203646988318) | **True.** And at least one on a scramble: 68.7953% on normal, 79.3147% with inverse. |
| A misoriented slice EO gives a DR-1s only on an axis with 8 bad edges | tseitsei89 [3 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1468124565681999932), trangium [8 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1480310254129516617) | **True** for routes that keep the axis's EO, and 55% of misoriented skips qualify (6.2). |
| "The chance of getting 4 flipped edges in general is 55%" | Rodney, [1 May 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1499635961015963751) | **True**: 70 in 128. |
| The optimal linear dr-fe distribution 1, 4, 50, 586, … | trangium, [2 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1478068304819261513) | **Reproduced exactly.** |
| "almost always a linear 7-mover on some axis and side, around half the time a 6-mover, and pretty much never a 5-mover" | trangium, [23 Jan 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1464482670200488294) | **Right for 7 and 6**: 98% of scrambles have a 7, 48% a 6. A 5 or shorter is there on 7.3%, one scramble in 14 (6.4). |
| Six edge-orientation patterns that guarantee an extra-good DR-xs | Rodney, [19 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474226073247027220) | **Five of six.** "All edges misoriented (12 bad) -> FB on UD will be extra-good -1s" is not a DR-1s: it is a DR-2s with four flipped edges of one slice. `B' D2 L2 U2 F2 D2 F L2 F2 D2 R2 F2 U' D' L' F' B' U'` has all twelve edges bad on F/B and green or blue on the U and D face of every corner; it has 4 flipped edges, needs 2 slices, and a shortest fix to DR is `U B F L U D` (6 turns). trangium's fix ([19 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474238124333858836)), "FB-colored misoriented, others oriented", is right. count quackula's 12-bad notes already had it: "If the CO color is green/blue: This is a DR-2s 4fe." |
| The cases with a fix to DR guaranteed in net +4 or less | count quackula's guaranteed-fix doc and 12-bad notes | **All consistent** with Appendix B, case by case. |
| Step 3 of the slice-DR method: 1, 4, 9, 40, 16 cases of 70 at 2 to 6 moves | Simon's slice-DR doc | **Four cases off**: 1, 4, 13, 36, 16 (4.2, Appendix A). |

---

## 9. What this does not cover

- **Findability.** "Finish" is the best solution of the method's form, exact per state. What a person finds in the time is trangium's and tseitsei89's ground, and their tables in the tutorial are the data.
- **Solutions outside the form.** True optimals from a DR-1s are 0.1 to 0.4 shorter on average (trangium's nissy numbers against mine). For a DR-2s 8fe the form has the two slices together; I didn't search solutions with moves between them.
- **DR-2s other than 8fe, and DR-3s.** Only their move counts to DR (section 4). trangium's nissy averages for them are +2.7 to +3.0 and +3.0 to +3.5.
- **NISS inside the route, and EO-changing moves.** A slice EO is taken on normal or on inverse, and the route to the DR-xs stays on that side and keeps that axis's EO. The finish uses both sides. So the counts of section 7 are a floor on what's there.
- **Normal DRs through an EO longer than 5 moves.** The normal-DR lists of section 7 come from cubelib-cli, which lists no EO longer than 5.
- **EO-breaking triggers and the EO-shifting ideas** from the EO-free trigger doc. The route rule here keeps the EO of one axis; 6.2 shows what dropping that rule could gain at most.
- **Time.** Section 7 counts what there is to find and to finish. How long a check takes is up to the people who do them; the times people have posted are in section 7.

---

## Appendix A: every DR-1s layout

Corners oriented on F/B (so the slice turn that fixes is `R L`, and the places inside that slice are UF, UB, DF, DB). The other choice of faces is the same table with the cube turned. "Scramble" gives a DR-1s with that layout: it is a DR followed by the fix backwards.

Each row is one layout of the four flipped edges, sorted by how many face turns its shortest fix takes.

| Flipped edges at | Fewest turns to a real DR | A shortest fix | Scramble |
|---|---:|---|---|
| DB DF UB UF | 2 | `R L` | `U R2 F2 D' B2 U2 L2 D R' L'` |
| BL DF UF BR | 3 | `B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B'` |
| FL DB UB FR | 3 | `F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F'` |
| BL DB UB FR | 4 | `L2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' L2` |
| BL DB UF BR | 4 | `D2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' D2` |
| BL DF UB BR | 4 | `U2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' U2` |
| BL DF UF FR | 4 | `R2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' R2` |
| BL FL BR FR | 4 | `F B R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' B'` |
| FL DB UB BR | 4 | `R2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' R2` |
| FL DB UF FR | 4 | `U2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' U2` |
| FL DF UB FR | 4 | `D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2` |
| FL DF UF BR | 4 | `L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2` |
| BL DB BR FR | 5 | `F' D2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' D2 F` |
| BL DB DF BR | 5 | `B2 U2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' U2 B2` |
| BL DB DF UB | 5 | `B' U2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' U2 B` |
| BL DB UB BR | 5 | `R2 L2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' R2 L2` |
| BL DB UB UF | 5 | `B D2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' D2 B'` |
| BL DB UF FR | 5 | `L2 U2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' U2 L2` |
| BL DF UB FR | 5 | `L2 D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 L2` |
| BL FL DB BR | 5 | `B R2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' R2 B'` |
| BL FL DB UB | 5 | `B2 R2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' R2 B2` |
| BL FL DF FR | 5 | `B' D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 B` |
| BL FL DF UF | 5 | `B2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 B2` |
| BL FL UB BR | 5 | `B' R2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' R2 B` |
| BL FL UF FR | 5 | `B U2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' U2 B'` |
| BL UB BR FR | 5 | `F U2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' U2 F'` |
| BL UB UF BR | 5 | `F2 U2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' U2 F2` |
| DB DF UB BR | 5 | `F R2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' R2 F'` |
| DB DF UF FR | 5 | `F' U2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' U2 F` |
| DB UB BR FR | 5 | `F2 R2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' R2 F2` |
| DB UB UF BR | 5 | `F' R2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' R2 F` |
| DF UB UF FR | 5 | `F D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 F'` |
| DF UF BR FR | 5 | `F2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 F2` |
| FL DB DF FR | 5 | `B2 D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 B2` |
| FL DB DF UF | 5 | `B L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 B'` |
| FL DB UF BR | 5 | `D2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 D2` |
| FL DF BR FR | 5 | `F L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 F'` |
| FL DF UB BR | 5 | `U2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 U2` |
| FL DF UB UF | 5 | `B' L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 B` |
| FL DF UF FR | 5 | `U2 D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' U2 D2` |
| FL UB UF FR | 5 | `F2 D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 F2` |
| FL UF BR FR | 5 | `F' L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 F` |
| BL DB DF FR | 6 | `L2 B2 D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 B2 L2` |
| BL DB DF UF | 6 | `L2 B L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 B' L2` |
| BL DF BR FR | 6 | `L2 F L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 F' L2` |
| BL DF UB UF | 6 | `L2 B' L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 B L2` |
| BL FL DB DF | 6 | `B2 U2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 U2 B2` |
| BL FL DB FR | 6 | `D2 B' D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 B D2` |
| BL FL DB UF | 6 | `B D2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 D2 B'` |
| BL FL DF BR | 6 | `R2 B' D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 B R2` |
| BL FL DF UB | 6 | `B' U2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 U2 B` |
| BL FL UB FR | 6 | `U2 B U2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' U2 B' U2` |
| BL FL UB UF | 6 | `B2 D2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 D2 B2` |
| BL FL UF BR | 6 | `R2 B U2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' U2 B' R2` |
| BL UB UF FR | 6 | `L2 F2 D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 F2 L2` |
| BL UF BR FR | 6 | `L2 F' L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 F L2` |
| DB DF BR FR | 6 | `F2 D2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 D2 F2` |
| DB DF UB FR | 6 | `U2 F' U2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' U2 F U2` |
| DB DF UF BR | 6 | `R2 F' U2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' U2 F R2` |
| DB UB UF FR | 6 | `D2 F D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 F' D2` |
| DB UF BR FR | 6 | `D2 F2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 F2 D2` |
| DF UB BR FR | 6 | `U2 F2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 F2 U2` |
| DF UB UF BR | 6 | `R2 F D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 F' R2` |
| FL DB BR FR | 6 | `D2 F L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 F' D2` |
| FL DB DF BR | 6 | `B U2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 U2 B'` |
| FL DB DF UB | 6 | `U2 B L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 B' U2` |
| FL DB UB UF | 6 | `D2 B' L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 B D2` |
| FL UB BR FR | 6 | `U2 F' L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 F U2` |
| FL UB UF BR | 6 | `R2 F2 D2 F R L` | `U R2 F2 D' B2 U2 L2 D R' L' F' D2 F2 R2` |
| UB UF BR FR | 6 | `F2 U2 L2 B R L` | `U R2 F2 D' B2 U2 L2 D R' L' B' L2 U2 F2` |

**With the last trigger move free to go either way.** If the move before was a quarter turn of U or D, turning it the other way moves the layout by a `U2` or `D2`. Taking the better of the two, the count is 1, 4, 13, 36, 16 layouts at 2 to 6 turns. The 13 at 4:

Each row is one layout; the two middle columns are its fewest turns to a real DR as the layout stands and after turning the last trigger move the other way.

| Flipped edges at | Turns to DR as it is | Turns to DR with the last move the other way | Fix as it is |
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

---

## Appendix B: from an edge-orientation pattern to a kind of DR-xs

The frame: the corners' colour is white/yellow (U/D), so the slice edges of the DR-xs are the E-slice edges; "M" and "S" are the edges belonging to the M and S slices. The orientation is for the axis in the first column, and the route keeps it (no quarter turns of that axis's faces). Each class of edges is all good or all bad. A percentage means it depends on where the pieces end up; without one it is guaranteed. Any other colour or axis is this table with the cube turned.

**EO axis F/B, not the slice's own.** Each row is which edges are bad for that axis; each column is where the corners' white or yellow faces end up, and the cell is the DR-xs you land on.

| Bad edges | Corners on U/D (their own faces) | Corners on R/L | Corners on F/B |
|---|---|---|---|
| none | DR, 0 flipped | DR-2s 8fe | DR-1s, 4 flipped, any split |
| E | DR-3s, 0 flipped | DR-3s, 8 flipped | DR-2s, 4 flipped, any split |
| M | DR-2s, 4 flipped, split 4-0 | DR-2s, 4 flipped, split 4-0 | DR-1s (51%), 4 flipped, split 2-2; DR-3s (49%), 0 to 8 flipped |
| S | DR-2s, 4 flipped, split 4-0 | DR-2s, 4 flipped, split 4-0 | DR-1s (51%), 4 flipped, split 2-2; DR-3s (49%), 0 to 8 flipped |
| E and M | DR-3s, 4 flipped, split 4-0 | DR-1s, 4 flipped, split 4-0 | DR-2s, 0 to 8 flipped |
| E and S | DR-3s, 4 flipped, split 4-0 | DR-1s, 4 flipped, split 4-0 | DR-2s, 0 to 8 flipped |
| M and S | DR-2s, 8 flipped, centers right (6 turns to DR; not the 8fe case) | DR-2s, 0 flipped (6 turns to DR) | DR-1s, 4 flipped, any split |
| all twelve | DR-3s, 8 flipped | DR-3s, 0 flipped | DR-2s, 4 flipped, any split |

**EO axis U/D, the slice's own.** Each row is which edges are bad for that axis; each column is where the corners' white or yellow faces end up, and the cell is the DR-xs you land on.

| Bad edges | Corners on U/D (their own faces) | Corners on R/L | Corners on F/B |
|---|---|---|---|
| none | DR (1.4%), 0 flipped; DR-2s (99%), 2 to 8 flipped | DR-1s, 4 flipped, split 4-0 | DR-1s, 4 flipped, split 4-0 |
| E | DR-3s, 0 to 8 flipped | DR-2s, 4 flipped, split 4-0 | DR-2s, 4 flipped, split 4-0 |
| M | DR-2s, 4 flipped, any split | DR-3s, 8 flipped | DR-3s, 0 flipped |
| S | DR-2s, 4 flipped, any split | DR-3s, 0 flipped | DR-3s, 8 flipped |
| E and M | DR-3s, 4 flipped, any split | DR-2s 8fe | DR-2s, 0 flipped (6 turns to DR) |
| E and S | DR-3s, 4 flipped, any split | DR-2s, 0 flipped (6 turns to DR) | DR-2s 8fe |
| M and S | DR (1.4%), 0 flipped; DR-2s (99%), 2 to 8 flipped | DR-1s, 4 flipped, split 4-0 | DR-1s, 4 flipped, split 4-0 |
| all twelve | DR-3s, 0 to 8 flipped | DR-2s, 4 flipped, split 4-0 | DR-2s, 4 flipped, split 4-0 |

---

## Appendix C: how it was computed, and what checks it

**The model.** One sticker-level cube with centers, built from geometry, so no permutation is typed in by hand. Everything else (the Rust tools' move tables, the Lean model) is generated from it or checked against it.

**Kinds and move counts (sections 3 and 4).** A kind is read off the stickers. I walk every kind reachable from a DR with DR-xs moves (768 per colour), and a shortest-path search over them with the cancelling rule gives the slices and turns. Exhaustive.

**Searches over cosets (6.2, 6.3).** For one colour, a cube's distance from a DR depends only on the corner twists, the edge orientations and where the E-slice pieces are: 2,217,093,120 cosets. For each target (real DR, DR-1s, DR-2s 8fe, any DR-xs) and each move rule (any turn; no quarter turns of one axis; quarter turns of that axis only when they miss the slice pieces) a BFS gives the distance from every coset. The numbers by kind of skip are counts over all cosets with that skip. Exhaustive.

**Slice-EO skips (6.1).** A count over all 70,963,200 arrangements of edge kinds and orientations. Exhaustive.

**Shortest routes on random scrambles (6.4).** A sample of 2,000,000 uniformly random cube states, each looked up in the coset tables for three colours and both sides.

**Finishes (section 5).** Random states, uniform over DR-1s (200,000) and over DR-2s 8fe (5,000). For each, I find the shortest solution of the method's form exactly, by trying every setup from both ends and looking up the optimal finish of the resulting DR in the first study's table. The averages carry a standard error of 0.002 (DR-1s) and 0.02 (8fe); the search per state is exact for its form.

**Real scrambles (section 7).** The first study's 500 scrambles: uniformly random states drawn with the EO → DR study's generator, not nissy's scrambler, which isn't uniform ([EO → DR study, appendix B](https://fmc.arhan.sh/eo-to-dr/#appendix-b-how-it-was-computed-and-what-checks-it)). Normal DRs: every DR up to 12 moves through an EO of 5 moves or less, from cubelib-cli (it lists no longer EOs), each finished optimally (first study). For 7.4 the same lists restricted to EOs of 4 or less. DR-xs: every DR-1s up to 8 moves and DR-2s 8fe up to 9 that starts from a slice-EO skip or a one-move slice EO and then keeps the EO of that axis, plus every DR-2s 8fe after an EO of at most 4 moves, each finished as in section 5 (the 8fe with setups of at most 3 moves from either end) and written out as a solution.

**What checks what.**

- The sticker model solves 100 scramble-and-solution pairs from the first study's examples page.
- The search to a real DR reproduces the known counts by distance (1, 4, 50, 592, …, 476).
- The search to any DR-xs on one colour and axis reproduces the distribution trangium posted (1, 4, 50, 586, …, 84).
- The 43 labelled DR-xs states in the server's worked examples are all classified as labelled.
- The finisher agrees with a separate sticker-level brute force on test states, and every solution it writes is replayed: 31,529 DR-1s solutions and every 8fe solution of the 500 scrambles solve their scramble in the stated number of moves.
- The DR finish table is the Lean-certified one of the first study.

**Lean.** `lean/DRXs` in the repository proves, by evaluation of its own definitions (no Mathlib):

- the model is a cube: every turn is a permutation, its moves equal the Python model's, and the orders of `U` and of these come out right:

  ```
  R U R' U'    // order 6
  R U          // order 105
  R U2 D' B D' // order 1260
  ```

- exactly 768 kinds are reached, 256 per pair of faces, and the kind of a state decides where every move takes it (checked over all reachable corner and edge colourings, not just one state per kind);
- the slices: 1, 140, 383 and 244 kinds need 0, 1, 2 and 3;
- the turns to DR: 2, 4, 18, 60, 56 kinds of DR-1s at 2 to 6 turns and none above; the DR-2s and DR-3s rows of 4.1; DR-3s to DR-2s in 2 turns for all 244; DR-2s to DR-1s in 2, 3 or 4 turns for 209, 102 and 72;
- the slice-EO count: of 70,963,200 arrangements, 22,143,888 have no skip on normal and 14,678,928 none on either side.

The proofs use `native_decide`, which trusts the Lean compiler. The searches over 2.2 billion cosets, the finish samples and the real scrambles are not in Lean; they rest on the cross-checks above.

---

## Docs referred to

- tseitsei89 (Janne Lehtimäki), [DR-Xs](https://docs.google.com/document/d/1_uLVLB5xqDm40NugXE5rjc8LgEtuHQCLz0odKY6mboE), 2 Feb 2026: the tutorial; trangium's averages and findability tables are in its sections 2 and 6.
- Rodney Kinney, [EO Meta Comparison](https://docs.google.com/document/d/131VWYrL3Z4t6p0fBGkHZ73w6arF8A7PEqRuNjsIQMGo), Jan 2026.
- trangium, [dr-fe examples](https://docs.google.com/document/d/11Xu6BpEBLu-v8hVbFzneSqeMjHb83q_zurWb_V0DXDY), 19 Jan 2026: the rule for the number of slices.
- count quackula, [12 bad dr-xs notes](https://docs.google.com/document/d/1-anqtLsBGg_oBvzz1TTf_6Mjsypv4jMkFhB9E8cwkQM) and [guaranteed-fix cases](https://docs.google.com/document/d/190aVmEQFLILHGhrtuf1YFai0SYrsu_tWRYAWOe62P6U), Feb 2026.
- Simon, [Slice DR](https://docs.google.com/document/d/15zDJ9_FQIYVgHLbt1eHdOPtEp10jFOOae_U8DTaH7tk), Jul 2025.
- The first study of this site, [Judging a DR by hand](../judging-a-dr/): the exact optimal finish of every DR state, used here for every finish.
