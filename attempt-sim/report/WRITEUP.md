# How to spend the hour: a simulated FMC attempt

**This is a draft.** The time costs are my first guesses and the conclusions depend on them. Section 4 has every cost with where it comes from, and section 11 says which conclusions still hold when you halve or double each one.

How long should you write EOs? When do you stop looking for DRs? Is it worth finishing a good DR the moment you find it? When should you write a backup down? Everyone here has an answer, but nobody can do the same scramble twice to check. So I wrote a program that can. It plays an hour-long DR attempt on a real scramble the way the guides describe one (EO, RZP, DR, HTR, finish), charges a time cost for everything it looks at, misses stuff the way a person does, and writes down what it has when the hour runs out. Then it plays the same scrambles again with a different plan and compares, attempt by attempt. It's all sampled: 3,400 random scrambles to pick plans on, 4,000 others to check them on, plus the 609 official scrambles of the top 5's recent attempts.

November 2026. A date in brackets links to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion). Docs and sheets are linked at the end.

**This builds on** stuff that was already on the server:

- **The splits people use.** Yura Riabov's [*Hitchhiker's Guide to FMC*](https://docs.google.com/document/d/16nu10y1JkUmVDC11c1h_ULzAl4Vze7zR/edit) (5-10 minutes writing EOs, up to 30-35 minutes checking them for DRs, the rest finishing), the thread where beef beans, kalindumaxxer, mrauo, Jay and rogo compared their search/finish splits ([22 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1320539084967641130) and the replies), Lichi Fang's 7+28+25 ([11 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1360212357804195872)) and Tom Nelson's 10/25/25 ([11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062704122849132654)).
- **How long each step takes.** What people have said: an EO written in 7 to 20 seconds, 3-5 seconds to throw away a 4-mover, 10-30 seconds per RZP, 20-30 seconds per switch, over a minute to write and check the final solution (all quoted in section 4).
- **Backup and safety habits.** Yura Riabov writing the best solution down around minute 50 in comp, and anything sub-24 or sub-23 right away ([2 Mar 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1345802699937157362), [2 Mar 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1345802831776710737)). Jay's and Yura's quick check of the easiest paths on a DR that feels 22/21able ([22 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1320564371709100235), [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418370795176198316)). Zagros on the difference between a backup and committing early ([2 Mar 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1345849445912281152)).
- **The idea of simulating it.**
  - Tom Nelson suggested simulating 100k solves with human-findable steps ([22 Sep 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1154981651315695627)), and did the arithmetic by hand ([8 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1061775242944585878), [9 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062115508641599498)).
  - rodneykinney posed "the cost-optimized FMC search strategy" with time as the cost ([26 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1344207003601604690)).
  - Spencer asked for a heuristic for how many paths a human can check, "and then run simulations about how many we should check at each stage" ([23 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143772698665820232)).

  As far as I can find, nobody posted one for a DR attempt. DougCube mentions private simulations for blockbuilding ([26 Apr 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1365877518133100585)), and Jack Love's *100 Example Solves* are computer solutions, not a model of the search.
- **Tables from the other studies on this site**, used as they are:
  - the exact optimal finish of every DR state (proved in Lean), from [*Judging a DR by hand*](../judging-a-dr/);
  - the HTR route checklist per subset, from [*Which HTR routes to try from a DR*](../htr-routes/);
  - the EO-kept distance to DR of every EO-solved case (proved in Lean), from [*EO to DR, and scramble to DR*](../eo-to-dr/) and [*When to switch an EO*](../eo-switch/);
  - the scramble features (bad edges per axis, shortest EO, number of 4-move EOs), from [*Easy or hard? Reading a scramble before you look for DRs*](../scramble-difficulty/).

**What this adds**: a simulator of the whole hour, and the first measured answers to the time-management questions, with the costs out in the open so people can argue with them.

- How the result depends on when you stop writing EOs and when you stop looking for DRs, on the same scrambles.
- Breadth first vs depth first, and the quick check of a good DR the moment it shows up.
- Whether a plan that reacts to the scramble (lots of EOs or few, a short DR early, a backup in hand) beats a fixed one, checked on scrambles it wasn't tuned on.
- The best plan for *22 or better*, and what it costs in mean.
- How the mean moves with the length of the attempt and with each budgeting decision, and which of these conclusions flip when a time cost is halved or doubled.

**Terms.** The usual ones: *EO*, *RZP*, *DR*, *HTR*, *switch* (NISS on an RZP), *subset* (corner case plus bad edges, `4b2 4e`), *route* (the subsets a finish goes through to HTR, in the HTR study's notation), *backup* or *safety* (a solution written on the sheet before the end). Plus a few of my own for this page:

- *Policy* or *plan*: the plan for the hour, a handful of numbers (when to stop writing EOs, how many RZP states per EO, when to stop looking for DRs, how many routes per DR, when to write a backup). The *baseline* is the guides' plan (section 3.2). The *tuned plan* is the baseline with three changes that turned out better (section 1).
- *Score*: the result with a DNF counted as 30 moves. A plan's score is the mean over all attempts, DNFs included. *Mean* on its own leaves DNFs out, like your own average does.
- *Score − tuned plan*: the difference attempt by attempt on the same scrambles, with its standard error. Negative is better.
- *≤ 22*: the share of attempts that end at 22 or better (a DNF doesn't count).
- *Robust* / *depends on the costs*: whether a conclusion keeps its sign when each time cost is halved and doubled (section 11).

**How to read it.**

- **Start with [section 1](#1-the-short-version)**: the answers, a paragraph or a table each. Section 4 is the table of costs, with the questions that would tune them.
- **Sections 6 to 10** take one question each, and **section 11** tests every conclusion against the costs. **Section 12** is what the simulator leaves out.
- Anything marked **computer only** is something the simulated solver can do and you can't, or an answer key.

---

| Section | What's in it |
|---|---|
| [1. The short version](#1-the-short-version) | The answers, with their numbers and how much they depend on the costs. |
| [2. What was asked](#2-what-was-asked) | The questions, and the ones people asked on the server before. |
| [3. The simulated attempt](#3-the-simulated-attempt) | The steps, what each one shows, the baseline plan, finishing, what the simulated solver can do that you can't. |
| [4. The time costs and the human limits](#4-the-time-costs-and-the-human-limits) | Every cost and limit with its source and how sure I am, and what to tell me to tune them. |
| [5. The baseline against real results](#5-the-baseline-against-real-results) | The simulated solver against the top 5's official attempts and Yura Riabov's log, whole distribution. |
| [6. How long on each step](#6-how-long-on-each-step) | Minutes on EOs, when to stop the DR search, how much to look at per EO and per DR. |
| [7. Breadth first or depth first](#7-breadth-first-or-depth-first) | Finishing a DR when you find it, taking short EOs straight to DR, early backups. |
| [8. Adapting to the scramble](#8-adapting-to-the-scramble) | Rules that react to what the attempt shows, checked on new scrambles. |
| [9. At most 22: the safety plan](#9-at-most-22-the-safety-plan) | Plans that push ≤ 22 up, and what they cost in mean. |
| [10. How the result scales](#10-how-the-result-scales) | The result against the length of the attempt, the speed of the solver, and one decision at a time. |
| [11. What depends on the costs](#11-what-depends-on-the-costs) | Each conclusion with every cost halved and doubled. |
| [12. What this does not model](#12-what-this-does-not-model) | Limits. |
| [Appendix A: full tables](#appendix-a-full-tables) | Every plan run. |
| [Appendix B: how it was computed, and what checks it](#appendix-b-how-it-was-computed-and-what-checks-it) | The program, the runs, the checks, the Lean certificate. |
| [Docs referred to](#docs-referred-to) | Links. |

## 1. The short version

**Again, this is a draft.** Everything below rests on time costs that are my first guesses (section 4), and section 11 checks which answers survive halving or doubling each one. All comparisons are attempt by attempt on the same 4,000 uniformly random scrambles, which no plan was tuned on. *Score* counts a DNF as 30, *mean* leaves DNFs out, and *−0.02* means 0.02 moves better than the tuned plan.

**What's new**

- **Three tweaks to the guides' plan are worth about a quarter of a move.** The baseline is the hour the way the guides describe it (section 3.2). Each tweak on its own, on held-out scrambles (appendix A has the table):
  - Only work an RZP state if your read says it's a DR of 10 or less, not 11.5: −0.14 ± 0.02.
  - Keep 7 minutes to write the solution, not 5: −0.11 ± 0.02, and DNFs go from 1.9% to 0.1%.
  - Be as happy to switch as to stay on the same side: −0.06 ± 0.01.

  All three together make the *tuned plan*: mean 21.87, against 21.99 for the baseline. The baseline is +0.26 ± 0.02 moves worse on score.
- **Once the plan is sensible, the time split barely matters.** Stop writing EOs anywhere from minute 3 to 12, stop looking for DRs anywhere from minute 25 to 40: every combination is within 0.03 moves of the tuned plan's score, and 24 of the 39 splits I tried are within 0.02. It's pretty flat on both ends too: stopping the DR search at 15 or at 50 costs +0.03 and +0.02. The one split that really costs is writing EOs until minute 16 (+0.03 to +0.22), and so does stopping the DR search at 45 or 50 after a long EO phase (section 6).
- **What matters is how much you look at, not when.** Against the tuned plan:

  | Change | Score − tuned plan, moves |
  |---|---:|
  | finish only the best DR | +0.893 ± 0.020 |
  | finish at most 4 DRs | +0.113 ± 0.007 |
  | no RZP, only DRs you see straight from the EO | +0.377 ± 0.017 |
  | 1 RZP state per short EO (the tuned plan does 3) | +0.120 ± 0.011 |
  | 8 RZP states per short EO | −0.020 ± 0.007 |
  | one route per DR (the tuned plan does 4) | +0.211 ± 0.013 |
  | 8 routes per DR | +0.065 ± 0.009 |
  | never switch | +0.319 ± 0.016 |
  | read cut-off 8 | +0.497 ± 0.025 |
  | read cut-off 12 | +0.133 ± 0.011 |

  So: finish every DR you think can beat what you've got, give each one 3 or 4 routes, and work at least 3 RZP states per short EO. The read cut-off has a pretty sharp sweet spot, 9.5 to 10 with these costs.
- **Depth first doesn't help, and adapting to the scramble doesn't add anything you can measure.**
  - Depth first all the way (each EO straight to DR, each DR straight to a finish): +0.026 ± 0.006.
  - Every rule that reacts to the scramble (lots of EOs or few, a short DR early or none, a result already in hand) is within 0.01 of the fixed plan, except the ones that keep searching too long (sections 7, 8).
  - Picking the best plan per scramble type on training scrambles gains −0.029 ± 0.008 on new ones, about what the single best tweak gives on every scramble (section 8).

  The fixed plan kind of adapts already, though. Its minutes are when priorities change, not hard walls, so if you run out of DRs to look at you just go back to the EOs.
- **Playing safe for ≤ 22 costs nothing.** Try one route right away on any DR that looks like 22 or better, and write the 22 down: −0.011 ± 0.003 on score, +0.5 ± 0.1 points of ≤ 22. Writing down the first solution you find is a different story, +0.39, because the rewrite eats time (section 9).
- **How the result scales with time.** Tuned plan, mean by length of the attempt: 20 minutes 23.07, 30 minutes 22.48, an hour 21.87, two hours 21.52 (section 10). Being twice as fast at every step gives exactly the two-hour result. Twice as fast plus a sharper read plus better DR vision gets you 21.35.

**How solid is this?** Section 11 reruns every comparison with each time cost halved and doubled. The how-much-you-look-at answers keep their verdict in pretty much every run, and so does the tuned plan's win over the baseline. Two things depend on you: the read cut-off (a much noisier read wants 9, not 10) and the time you keep for writing (if your step times swing a lot, keep 10 minutes, not 7). The single cost that moves the result most is how accurate your read of an RZP state is.

**What it confirms or corrects**

- **The top's mean is about 21.9, not 20-21.** The five best official means since 2024 average 21.91 over 720 attempts, and Yura Riabov's 2025 log says 21.99. The baseline lands close, 22.04 on random scrambles. The simulated results are more bunched up than real ones though: fewer sub-20s and fewer 24s (section 5).
- **The guides' split holds up.** 5-10 minutes on EOs and up to 30-35 minutes looking for DRs (Yura Riabov's *Hitchhiker's Guide to FMC*), Lichi Fang's 7+28+25 and Tom Nelson's 10/25/25 are all in the flat part of section 6.

## 2. What was asked

The questions this study set out to answer:

- *How long should be spent on each step?* Section 6.
- *Are there situations where depth-first searching is helpful?* Section 7.
- *Is it useful to have an adaptive time budgeting strategy that changes based on features of the scramble?* Section 8.
- *What's the best "safety" approach to get at most 22, at risk of missing something better?* Section 9.
- *How does the average result scale as a function of different time budgeting decisions?* Section 10.
- *Top-level humans average around 20-21 moves, so target that or better.* Section 5 measures where the top is: the five best official means since 2024 average 21.9, and the simulated baseline sits next to them. Section 10 says how far faster steps and sharper reads take it.

Questions from the server that the same runs answer:

- JTuu: "when you have let's say 21 safety with 20 mins or so to look for better, anyone have advice for knowing when you should squeeze the 21 harder vs widen your search and prune very aggressively? I feel like I frequently do the wrong one" ([23 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1320666605478219837)), unanswered in the thread. Section 9.
- Lichi Fang: "In scrambles where you have several mid DRs at 30 minutes (for example a 11+2c3, a 10+4c3, a 10+2c4, and a 11+2b4), is it in general better to start finishing DRs sooner or later? (Or like what's the general philosophy of a good time management?)" ([30 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1290231351726968852)). Yura Riabov answered "Sooner in this case, cause you'd want to check briefly 11s, most simple paths of 4c3 and go grinding 2c4" ([30 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1290240287213621248)). Sections 6 and 8.
- Tzak: "at what time do people settle and work on some 2c4 vs trying for more drs" ([30 Jun 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1389421862475403326)). Section 6.
- DRCubeur: "Is stopping checking EOs at a certain time even if I’m not finished worth it?" ([25 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1476132917833896008)). Section 6.
- rodneykinney's "cost-optimized FMC search strategy" ([26 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1344207003601604690)) and Tom Nelson's proposal to simulate solves ([22 Sep 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1154981651315695627)): this page is a first version of both, for the DR method.

## 3. The simulated attempt

The simulator plays an attempt pretty much the way the guides describe one: write EOs, glance at each one and work the promising RZPs, write down the DRs you see, then try HTR routes on the best DRs and write the best solution down. Everything the solver looks at costs time, and then the hour runs out. The cube part is real: it runs on real scrambles, every EO, RZP, DR, HTR and finish it writes down actually exists on that scramble, and every solution it submits solves it (all of them get replayed). What's *modelled* is the solver: how long each step takes, what you see and what you miss, and the plan that decides what to look at next.

### 3.1 The steps and what each one costs

One attempt is a sequence of steps, each with a time cost. The clock is the sum of the costs. The steps, in the order an attempt meets them:

| Step | What the solver does | What it reveals to the solver |
|---|---|---|
| look | count the bad edges on the three axes | the bad-edge counts |
| EO scan | search one axis (both sides) for EOs one move longer than before | the EOs of that length on that axis that the solver *sees* (some are missed) |
| EO write | write one EO down | |
| glance | look at one EO on both DR axes, for each way of making its last quarter turn | each line's DRM, read as a guess of the distance to DR, and any DR in plain sight |
| RZP | work one RZP state: one more EO-keeping turn on the side the EO ended | the state's read; the DR if it is close enough and the solver sees it |
| switch | set up the other side and work the state there (NISS) | the same, on the other side |
| DR write | write a DR down | its length |
| DR read | read a DR's corner case and edges, for the last quarter turn either way | its subset, so a guess of its finish |
| route | try one HTR route on a DR, from the htr-routes checklist of its subset | a finish along that route, if the solver finds it |
| finish write | write out the finish the route gave | a full solution and its length |
| write | write the solution on the sheet and check it on the cube | the attempt's result, if it ends inside the hour |

Two kinds of randomness make it play like a person. First, time: each step takes its nominal cost times a random factor (one draw per step and object, so the same EO costs the same under every plan), and the whole attempt runs at a pace drawn once per attempt, so some attempts are just slower. Second, misses: a 5-move EO is seen with some chance, a DR 5 moves from an RZP state with some chance, a route that has a short finish gives it with some chance. There's also a *form* setting (missing less on a good day), but it's switched off in every run here (section 4 says why). Section 4 lists every cost and every chance.

### 3.2 What the solver knows and how it picks

The solver never sees the answer key. It knows only what its steps revealed: lengths, bad edges, the DRM of a state as a *read* of how far the DR is, the subsets of the DRs it read, the finishes it found. The read of a state is its true EO-keeping distance to DR plus a reading error (spread 1 move, see section 4). That spread is calibrated against the EO-switch study: with it, the solver flags 18.5% of 4c4e cases as 6 or less to DR and 60.8% of those are, close to the paired-edge card of that study (15.5% at 59.9%).

How the hour is spent is the *policy*. The baseline policy is the guides' plan, breadth first:

1. Count bad edges. Scan the axes for EOs up to 5 moves (NISS EOs included), the axes with the fewest bad edges first, and write them down until minute 8 or 40 EOs.
2. From minute 8: glance at the EOs, shortest first. Work up to 3 RZP states per EO of 4 moves or less (1 for 5-movers), most promising read first, a switch ranked 0.3 moves worse than staying on the same side, at most 3 RZP moves, only states whose read promises a DR of 11.5 moves or less. Write down every DR of 11 or less that is seen, and read its subset.
3. From minute 35: finish the DRs, the lowest expected total first, up to 4 routes each, skipping a DR whose chance (by subset) of beating the best solution so far is under 3%.
4. Keep 5 minutes to write the best solution down.

When a phase runs out of work early the solver goes back to whatever is left (more RZP states per EO, a looser read limit, more EOs), so the minutes in the plan are when the solver *switches priority*, not walls: a solver who has finished their DRs at minute 40 goes back to looking for more.

### 3.3 Finishing a DR

A DR in the simulator is a state of the DR group with a known subset (judging-a-dr's model). The solver tries routes to HTR from the htr-routes checklist of that subset (the *main checklist* of that study: level C, optimum, HTR budget 2), in its order, over both ways of making the DR's last quarter turn. A route tried gives the shortest finish that follows it with an HTR at most 2 moves over the shortest NISS HTR, if that finish is at most 2 moves over the DR's optimal finish; otherwise nothing. The finish is found with a chance (0.9) when it exists. What a route finds is computed on the cube from the DR state, not drawn from statistics.

### 3.4 What the simulated solver can do that a human can't

These are simplifications, and each one makes the simulated solver a bit better than its costs would suggest.

- **Its read of an RZP state is centred on the truth.** A human's read of a DRM is biased in ways that depend on the case; here the error is symmetric noise around the exact distance.
- **A DR seen is written optimally**: from a state d moves from DR the solver writes a d-move DR, never a longer one.
- **A route tried gives the best finish along it** (within 2 moves of the DR's optimum), or nothing. A human trying a route might find a worse finish along it.
- **The solver knows each subset's finish distribution** (all 19.5 billion DR states, from htr-routes) when it weighs a DR.
- **No mistakes**: no miswritten moves, no wrong scramble, no solution that fails the check. A DNF comes only from the clock.

And what a human can do that the simulator doesn't (section 12): EOs of 6 or more, DRs not through a written EO, DR-breaking finishes, insertions, blockbuilding, using a written solution as a faster scramble.

### 3.5 Runs

Every plan plays the same scrambles with the same random draws (the same EO gets missed, the same step takes the same time, the same attempt is a slow one under every plan). So two plans get compared attempt by attempt, and the difference has a way smaller error than either mean. Scrambles are uniform random states. Policies are chosen on training scrambles, and every comparison on this page is on 4,000 held-out scrambles (4,000 to 7,999) that no policy was chosen on (appendix B). One simulated attempt takes about 10 ms of computer time.

## 4. The time costs and the human limits

Every number here is a first guess, and they are what you would tune. Each row has its value, where it comes from, and how sure I am of it. *High* means a stated rule or a measured fit, *medium* means several solvers' figures agree roughly, *low* means a guess with little or nothing behind it.

The time of one step, in seconds (nominal; the real time of each step is this times a random factor, see the last rows):

| Step | Cost, s | Source | Confidence |
|---|---|---|---|
| look: count bad edges on 3 axes | 15 | none measured; Enrico counts them before writing EOs ([23 Nov 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1177168912878682142)) | low (small) |
| EO scan, one axis to length 1 / 2 / 3 / 4 / 5 | 2 / 3 / 5 / 10 / 30 | 50 s per axis to length 5, under 3 minutes for all three: Jay's "sub 2 minute passes" over the six axis-sides ([8 Nov 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1172011024346529852)), Fanti "~1m30" for 2+2 EOs on all axes without writing ([22 May 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1375167055208382545)) | medium |
| EO scan with NISS EOs too | × 1.5 | guess | low |
| EO write, per EO | 8 | Yura Riabov: 90 written in 11 minutes ([15 Feb 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1340412480911970489)), 7.3 s each; Kai Cui about 50 in 10 minutes ([21 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1275747036310011986)); FakeMMAP 26 in about 6 ([15 Feb 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1340413183466278933)) | medium |
| glance at one EO | 5 | Yura Riabov: "3-5 to discard if it doesn't lead to short dr" for a 4-mover ([27 Apr 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1366113860636905544)) | medium |
| work one RZP state | 15 | tseitsei89: "You should spend like 10-30s per rzp" ([12 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1404889693513977898)) | medium |
| switch (set up the other side, work the state) | 25 | Jay: NISSing for trigger in 5 "tends to cost me around 30 seconds" ([11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062697633195499630)); Evan: "20 seconds to scramble" ([9 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1260239771834388601)) | medium |
| write a DR seen 0 / 1 / 2 / 3 / 4 / 5 / 6 / 7 moves away | 3 / 3 / 5 / 8 / 12 / 20 / 30 / 45 | guess (longer DRs take longer to find and write) | low |
| read a DR (corner case and edges, last quarter turn either way) | 15 | no measured figure; Tom Nelson: "it takes like 0.5 seconds to note down" the bad-edge count ([2 Jan 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1191920567486513162)) | low |
| try one HTR route | 40 | Tom Nelson: "5 seconds to see if it's good or not" for a long HTR ([8 Nov 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1171751296550830090)), "30 seconds to check those kinds of variants" ([8 Nov 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1171749657676890162)) | low |
| write out the finish a route gave | 30 | tseitsei89: a 4-QT slice "in probably less or at least around 1 minute" ([17 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1406662901644791949)) | low |
| write the solution on the sheet and check it | 150 | Radek: with 16 of 21 moves written in the last minute, "realistically I needed an extra minute to submit 21" ([*Sub 22 Official Mean Stats*](https://docs.google.com/spreadsheets/d/17L6vArP8t_5yPIeCpiQpp66YBZcLcbxS10hzYtnB-XE/edit?gid=0), tab "Radek 21.00 (Euros 2024)") | medium-low |
| spread of one step's time (log-normal) | 0.25 | guess; it mostly sets how often the final write runs over | low |
| spread of the pace from attempt to attempt | 0.15 | fitted: the baseline's DNF rate matches the top 5's (section 5) | fitted |

What the solver sees (chances, or a spread in moves):

| Limit | Value | Source | Confidence |
|---|---|---|---|
| an EO on one side, found when its axis is searched to its length: 3 / 4 / 5 moves | 1 / 0.95 / 0.75 | guess; jaye writes "all the sub 5 move eos/the obvious 5 movers" ([23 Nov 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1177171075935780897)) | low |
| a NISS EO (moves on both sides): 2-3 / 4 / 5 moves | 0.9 / 0.7 / 0.3 | guess | low |
| a DR 3 / 4 / 5 / 6 moves away, seen at the glance | 0.9 / 0.6 / 0.25 / 0.05 | guess | low |
| a DR 4 / 5 / 6 / 7 moves away, seen from a worked RZP state | 0.95 / 0.8 / 0.5 / 0.15 | guess; *DR Miss* is the largest of Zagros's miss counts (34% of 34 solves, [1 Oct 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1555269932818899027)) | low |
| a route with a short finish gives it when tried | 0.9 | guess; Yura Riabov's log marks a finish miss in 11 of 138 attempts | low |
| reading error of an RZP state's distance to DR, moves | 1.0 | about the EO-switch paired-edge card (section 3.2) | medium |
| ranking of RZP states: weight of moves already made | 0.6 | guess | low |
| spread of the form from attempt to attempt | 0 | tried at 0.3 to 1.0: it makes bad days worse (more DNFs, a higher mean) but adds no sub-20s, so it can't produce the real spread (section 5); left out | tried |

### 4.1 What to tell me to tune them

These are the answers that would move the results most, in the order section 11 measured (how much the tuned plan's result moves when each one is halved or doubled):

1. **Your read of an RZP state.** When you look at an RZP state and think it's a DR in 6, how often is it? The simulator's read is off by about a move (spread 1). Twice as noisy costs half a move overall, half as noisy gains 0.15, so this is the big one. It also decides the read cut-off: with a much noisier read, 9 beats 10.
2. **What you see from an RZP.** From a state 4, 5 or 6 moves from DR, how often do you actually find that DR? The simulator uses 0.95, 0.8 and 0.5.
3. **Per route on a DR.** How long does trying one HTR route take you, finding the HTR and seeing its finish? The simulator uses 40 s and tries 4 routes on a DR it likes.
4. **How much your step times vary.** Some RZPs take 5 seconds and some take a minute. The simulator spreads every step's time by about 25%. If yours vary a lot more, keeping 10 minutes for writing starts to pay instead of 7.
5. **The final write.** How long do you need to write the solution down and check it? The simulator uses 2.5 minutes, and the tuned plan keeps 7 minutes for it.
6. **EOs.** Seconds to write one (8 here), to glance at one and throw it away (5), and how many 5-movers you miss.
7. **Writing out a finish, reading a DR, RZP and switch.** 30 s, 15 s, 15 s and 25 s here. Each of these moves the result by 0.05 or less when halved or doubled.

## 5. The baseline against real results

The real yardstick is the WCA results export (This information is based on competition results owned and maintained by the World Cube Association, published at https://worldcubeassociation.org/results as of November 13, 2026.): the five solvers with the best official mean since 2024 (at least 40 attempts each), 720 attempts. Their mean is 21.91, not 20-21: 20-21 is a good mean of 3, not where the best solvers sit over many attempts. Yura Riabov's own log of 138 attempts from 2025 ([*FMC Jan-May 2025*](https://docs.google.com/spreadsheets/d/1Cb7M3KqB5W99sSNOIKLG3xqZ-k58koIexTLahUiPNhs/edit?usp=sharing), posted [8 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1392205872595468319)) says the same: 21.99.

The baseline policy with the costs of section 4 lands within about a tenth of a move of them. One row per group of attempts; the simulator is run on random scrambles and, separately, on exactly the scrambles of the top 5's attempts (each scramble as many times as they had it):

| Who | Attempts | Mean, moves | ± SE, moves | SD, moves | DNF, % | Sub-20, % | ≤ 22, % | 24 or more, % |
|---|---|---|---|---|---|---|---|---|
| Simulator, baseline policy, 4,000 random scrambles | 4000 | 22.04 | 0.02 | 1.23 | 1.6 | 2.5 | 62.0 | 9.1 |
| Simulator, baseline policy, the top 5's official scrambles | 720 | 21.98 | 0.05 | 1.22 | 1.5 | 3.3 | 64.3 | 8.3 |
| Top 5 by mean, official, since 2024 | 720 | 21.91 | 0.07 | 1.79 | 1.4 | 7.4 | 66.5 | 16.1 |
| Top 10 by mean, official, since 2024 | 1405 | 22.31 | 0.05 | 2.00 | 3.8 | 5.8 | 56.0 | 23.3 |
| Yura Riabov's log, 2025 | 138 | 21.99 | 0.13 | 1.56 | 0.0 | 6.5 | 61.6 | 15.2 |

The mean and the DNF rate are close. The spread isn't: the simulated solver has about a third as many sub-20s and a bit over half as many 24s or worse. Result by result, as a share of each group's attempts:

| Result, moves | Simulator, % of attempts | Simulator, same scrambles as the top 5, % of attempts | Top 5 by mean, official, since 2024, % of attempts | Yura Riabov's log, 2025, % of attempts |
|---|---|---|---|---|
| DNF | 1.6 | 1.5 | 1.4 | 0.0 |
| ≤ 18 | 0.7 | 0.7 | 1.8 | 2.2 |
| 19 | 1.8 | 2.6 | 5.6 | 4.3 |
| 20 | 7.4 | 6.9 | 12.1 | 10.1 |
| 21 | 19.3 | 20.6 | 21.5 | 17.4 |
| 22 | 32.9 | 33.5 | 25.6 | 27.5 |
| 23 | 27.3 | 25.8 | 16.0 | 23.2 |
| 24 | 8.0 | 7.6 | 9.7 | 10.9 |
| 25 | 1.0 | 0.7 | 3.6 | 3.6 |
| 26 or more | 0.0 | 0.0 | 2.8 | 0.7 |

The simulated results pile up at 22 and 23. What it lacks at the good end is the finishes it can't make (section 12: DR-breaking finishes, insertions, other methods) and luck beyond the DR group; at the bad end, the mistakes it can't make (miswritten moves, ten minutes lost to a wrong scramble). So **read every ≤ 22 and sub-20 share on this page as a comparison between plans, not as a forecast of your own rate.** The differences between plans are what the runs measure well.

Does the simulator know which scrambles are hard? On the same scramble the real result and the simulated one go together, with correlation 0.30 ± 0.03 over 699 attempts. Grouped by what the simulator got on the scramble, the top 5's mean on those same scrambles:

| Simulated result on the scramble, moves | Real attempts | Real mean, moves | ± SE, moves |
|---|---|---|---|
| 20 or less | 74 | 20.62 | 0.25 |
| 21 | 146 | 21.59 | 0.13 |
| 22 | 235 | 21.94 | 0.10 |
| 23 | 184 | 22.45 | 0.13 |
| 24 or more | 60 | 22.43 | 0.25 |

The real solvers do better on the scrambles the simulator finds hardest than the simulator does, which fits the same picture: when the DRs are poor, a real solver has other ways out.

What the simulated attempt looks like, on average over the 4,000 scrambles (the real figures are Yura Riabov's log, and the sheets quoted in section 4):

| What | Simulated, per attempt | Real |
|---|---|---|
| EOs written | 52.8 | 40 checked per attempt, median (Yura Riabov's log, 138 attempts); 39 in the FMC League comments |
| RZP states worked | 69.0 | Tom Nelson's league comments: 28 RZPs, median |
| switches | 10.9 | "I never plan on having time to switch more than 10" (Zagros, [18 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1418250491120320532)) |
| DRs written (11 moves or less) | 12.5 | "i write down maybe 5 per attempt on average" (Yura Riabov, [24 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1299037487305588818)); "20+ every  attempt" counting the ones seen and not written (Zagros, [24 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1299031808469499965)) |
| DRs taken to a finish | 3.2 | "of those 1-3 are usually what i work on" (Yura Riabov, [24 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1299037537561608193)); "2-3 DRs with corners worth considering" (wen, [11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062713324783013918)) |
| routes tried | 11.4 | |
| length of the result's DR, moves | 9.79 | 9.96 (Yura Riabov's log); 9.71 (the sub-22 official means) |
| finish optimal from its DR, % of results | 87.9 | 0.38 moves missed from the DR on average (Yura Riabov's log) |
| minute the result's DR was written | 19.9 | |
| minute the result's finish was found | 36.7 | |
| minutes finding and writing EOs | 9.8 | "5-10 minutes: searching for and writing out eos" (*Hitchhiker's Guide to FMC*) |
| minutes glancing at EOs, working RZPs, writing DRs | 30.4 | "Up to 30-35 minutes: checking eos and searching for DR" (the same) |
| minutes reading DRs, trying routes, writing out finishes | 15.0 | "Until the end of the solve: solving the best dr" (the same) |
| minutes writing the solution down | 2.5 | |

## 6. How long on each step

From here on everything is compared against the tuned plan from section 1 (the baseline plus read cut-off 10, 7 minutes kept for writing, and switching as happily as staying). What a tuned-plan attempt looks like on average, over the held-out scrambles: 78.2 EOs written, 34.5 RZP states worked, 13.0 DRs written and 3.3 taken to a finish with 12.0 routes tried. That's 13.3 minutes finding and writing EOs, 24.2 looking for DRs, 15.7 finishing and 2.5 writing the solution. The DR of the result was written at minute 18.6 on average, and its finish found at minute 30.5.

**The split between EOs, DRs and finishing.** Each row is the minute EO writing stops, each column the minute the DR search stops (finishing gets the rest), and each cell the score against the tuned plan, which stops at 8 and 35:

| EO writing stops, minute | DR search stops at minute 20 | DR search stops at minute 25 | DR search stops at minute 30 | DR search stops at minute 35 | DR search stops at minute 40 | DR search stops at minute 45 | DR search stops at minute 50 |
|---|---|---|---|---|---|---|---|
| 3 | +0.019 ± 0.005 | +0.018 ± 0.005 | +0.018 ± 0.005 | +0.018 ± 0.005 | +0.019 ± 0.005 | +0.020 ± 0.006 | +0.029 ± 0.006 |
| 5 | +0.011 ± 0.005 | +0.007 ± 0.004 | +0.004 ± 0.004 | +0.006 ± 0.004 | +0.007 ± 0.004 | +0.009 ± 0.004 | +0.018 ± 0.005 |
| 8 | +0.020 ± 0.005 | +0.007 ± 0.003 | −0.001 ± 0.003 | +0.001 ± 0.001 | +0.008 ± 0.003 | +0.017 ± 0.004 | +0.033 ± 0.005 |
| 12 | +0.044 ± 0.006 | +0.031 ± 0.005 | +0.011 ± 0.005 | +0.007 ± 0.005 | +0.018 ± 0.005 | +0.038 ± 0.007 | +0.089 ± 0.008 |
| 16 | +0.089 ± 0.008 | +0.073 ± 0.007 | +0.050 ± 0.006 | +0.031 ± 0.007 | +0.045 ± 0.007 | +0.100 ± 0.009 | +0.221 ± 0.012 |

Everything from 3 to 12 minutes of EOs and 25 to 40 minutes of DR search is within 0.03 moves. Writing EOs until minute 16 costs, and more so with a late DR stop: it leaves too little for finishing. So for Tzak's "at what time do people settle and work on some 2c4 vs trying for more drs" ([30 Jun 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1389421862475403326)) and DRCubeur's "Is stopping checking EOs at a certain time even if I'm not finished worth it?" ([25 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1476132917833896008)): with these costs anything from minute 25 to 40 is as good as anything else, and yes, stopping EO writing at minute 8-12 costs nothing.

**How many EOs.** No time limit on writing, a cap on the number written. Each row is a cap:

| EOs written at most (no time limit on writing), EOs | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 10 | 21.88 | 0.1 | 69.5 | +0.016 ± 0.005 |
| 20 | 21.87 | 0.1 | 69.7 | +0.005 ± 0.004 |
| 30 | 21.87 | 0.1 | 70.0 | −0.002 ± 0.002 |
| 40 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |
| 60 | 21.87 | 0.1 | 69.8 | +0.003 ± 0.004 |
| 80 | 21.89 | 0.1 | 69.0 | +0.021 ± 0.006 |
| 120 | 21.95 | 0.1 | 67.0 | +0.076 ± 0.007 |

**How long an EO.** Each row is the longest EO looked for:

| Longest EO looked for, moves | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 3 | 21.89 | 0.1 | 69.3 | +0.020 ± 0.006 |
| 4 | 21.87 | 0.1 | 69.7 | +0.006 ± 0.004 |
| 5 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |

EOs of 4 or less are nearly as good as EOs of 5 here. A likely reason, not measured separately: the plan works only one RZP state per 5-mover (section 3.2), so the 5-movers add few DRs.

**How many RZP states per EO.** Each row is the number of RZP states worked per EO of 4 or less:

| RZP states worked per EO of 4 moves or less, states | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 0 | 22.24 | 0.1 | 55.9 | +0.377 ± 0.017 |
| 1 | 21.99 | 0.1 | 65.3 | +0.120 ± 0.011 |
| 2 | 21.90 | 0.1 | 68.8 | +0.033 ± 0.006 |
| 3 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |
| 4 | 21.86 | 0.1 | 70.0 | −0.004 ± 0.005 |
| 6 | 21.86 | 0.1 | 70.5 | −0.011 ± 0.007 |
| 8 | 21.85 | 0.1 | 70.6 | −0.020 ± 0.007 |

After how many DRs you finish, this is the steepest curve of the hour: 0 or 1 state per EO loses a lot. Going past 3 still gains a little, and 8 is the best value I tried, so the real best might be even higher.

**When the DR search stops**, with nothing else changed. Each row is the minute:

| DR search stops, minute | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 15 | 21.90 | 0.1 | 69.0 | +0.029 ± 0.006 |
| 20 | 21.88 | 0.1 | 69.3 | +0.018 ± 0.005 |
| 25 | 21.87 | 0.1 | 69.7 | +0.005 ± 0.003 |
| 30 | 21.87 | 0.1 | 70.0 | −0.002 ± 0.002 |
| 35 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |
| 40 | 21.87 | 0.1 | 69.8 | +0.004 ± 0.002 |
| 45 | 21.88 | 0.1 | 69.4 | +0.013 ± 0.003 |
| 50 | 21.89 | 0.1 | 69.0 | +0.025 ± 0.004 |

**How many routes per DR.** Each row is the number of routes from the subset's checklist (htr-routes) tried on a DR:

| Routes tried per DR, routes | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 1 | 22.08 | 0.1 | 62.7 | +0.211 ± 0.013 |
| 2 | 21.96 | 0.1 | 67.0 | +0.088 ± 0.010 |
| 3 | 21.86 | 0.1 | 70.7 | −0.006 ± 0.007 |
| 4 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |
| 6 | 21.90 | 0.1 | 68.5 | +0.028 ± 0.008 |
| 8 | 21.93 | 0.1 | 67.0 | +0.065 ± 0.009 |

**How many DRs to finish.** The solver takes DRs to a finish in order of expected total, skipping any whose chance of beating the best so far is under 3%. Each row is a cap on how many:

| DRs taken to a finish at most, DRs | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 1 | 22.70 | 0.9 | 41.9 | +0.893 ± 0.020 |
| 2 | 22.31 | 0.1 | 53.7 | +0.444 ± 0.013 |
| 3 | 22.10 | 0.1 | 60.4 | +0.229 ± 0.010 |
| 4 | 21.98 | 0.1 | 65.0 | +0.113 ± 0.007 |
| 5 | 21.91 | 0.1 | 67.9 | +0.044 ± 0.004 |
| 6 | 21.88 | 0.1 | 69.2 | +0.013 ± 0.002 |
| no limit (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |

With no cap the tuned plan finishes 3.3 DRs on average. Capping at 4 already costs +0.11. "of those 1-3 are usually what i work on" (Yura Riabov, [24 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1299037537561608193)) is in the range where the cap costs a lot here. To be fair, a real solver's 1-3 are picked by a much sharper eye than the simulator's (section 12).

## 7. Breadth first or depth first

*Breadth first* is the guides' order and the tuned plan's: all EOs, then the DRs, then the finishes. *Depth first* takes each EO straight to a DR and each DR straight to a finish. In between are the quick looks: one route at once on a DR that promises a good result, and a backup (the best DR finished early, so there is something on the sheet). Each row is a plan:

| Plan | Mean, moves | DNF, % | ≤ 22, % | Sub-20, % | Score − tuned plan, moves | ≤ 22 − tuned plan, points |
|---|---|---|---|---|---|---|
| the tuned plan (breadth first: all EOs, then DRs, then finishes) | 21.87 | 0.1 | 69.8 | 3.4 | 0 | 0 |
| depth first: each EO of 3 straight to DR, then each DR straight to a finish | 21.89 | 0.1 | 69.2 | 3.3 | +0.027 ± 0.007 | −0.5 ± 0.3 |
| depth first throughout | 21.89 | 0.1 | 69.2 | 3.3 | +0.026 ± 0.006 | −0.5 ± 0.3 |
| depth first, one route per DR | 21.89 | 0.1 | 69.3 | 3.3 | +0.023 ± 0.007 | −0.5 ± 0.3 |
| EOs of 2 moves or less straight to DR | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.001 | +0.0 ± 0.0 |
| EOs of 4 moves or less straight to DR | 21.88 | 0.1 | 69.4 | 3.3 | +0.016 ± 0.006 | −0.4 ± 0.2 |
| a DR that promises 22 or better: one route at once | 21.87 | 0.1 | 70.0 | 3.4 | −0.004 ± 0.001 | +0.1 ± 0.1 |
| a DR that promises 23 or better: one route at once | 21.86 | 0.1 | 70.0 | 3.4 | −0.004 ± 0.003 | +0.2 ± 0.1 |
| every DR: all its routes at once | 21.91 | 0.1 | 68.7 | 3.3 | +0.038 ± 0.007 | −1.1 ± 0.3 |
| a backup: best DR finished by minute 10 | 21.87 | 0.1 | 70.0 | 3.5 | −0.002 ± 0.003 | +0.2 ± 0.1 |
| a backup by minute 20 | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.001 | +0.1 ± 0.1 |
| a backup by minute 30 | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.001 | +0.1 ± 0.1 |
| a backup by minute 40 | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 | +0.0 ± 0.0 |

Depth first is a little worse, +0.026 ± 0.006. The runs don't say why. My guess: time spent finishing early DRs is time you don't spend finding the better DR that shows up later. The quick look at a promising DR comes out level with the tuned plan, and so do early backups. With 7 minutes kept for writing you almost never end with nothing on the sheet, so a backup doesn't buy much. Section 9 has the backup's other job, the safety of a result in hand.

## 8. Adapting to the scramble

Rules that change the plan by what the attempt shows: how many EOs turned up, whether a short DR came early, whether a result is already in hand. Each row is a plan:

| Plan | Mean, moves | DNF, % | ≤ 22, % | Sub-20, % | Score − tuned plan, moves | ≤ 22 − tuned plan, points |
|---|---|---|---|---|---|---|
| the tuned plan (fixed times) | 21.87 | 0.1 | 69.8 | 3.4 | 0 | 0 |
| rich in EOs (25+ found): DR search to minute 30 | 21.87 | 0.1 | 70.0 | 3.4 | −0.002 ± 0.002 | +0.2 ± 0.1 |
| rich in EOs (25+ found): DR search to minute 45 | 21.88 | 0.1 | 69.4 | 3.4 | +0.013 ± 0.003 | −0.4 ± 0.1 |
| poor in EOs (under 10 of 4 or less): 5-movers too, else 4 only | 21.87 | 0.1 | 69.8 | 3.4 | +0.004 ± 0.003 | −0.0 ± 0.1 |
| EOs of 4 or less only | 21.87 | 0.1 | 69.7 | 3.4 | +0.006 ± 0.004 | −0.1 ± 0.1 |
| no DR of 9 by minute 25: DR search to minute 45 | 21.87 | 0.1 | 69.7 | 3.4 | +0.003 ± 0.002 | −0.1 ± 0.1 |
| stop the DR search once 2 DRs of 9 are written | 21.87 | 0.1 | 69.7 | 3.4 | +0.004 ± 0.003 | −0.1 ± 0.1 |
| stop the DR search once 1 DR of 8 is written | 21.87 | 0.1 | 69.8 | 3.5 | +0.001 ± 0.001 | −0.1 ± 0.0 |
| a 22 on the sheet: DR search to minute 45 | 21.88 | 0.1 | 69.8 | 3.3 | +0.011 ± 0.003 | +0.0 ± 0.0 |
| a 23 on the sheet: DR search to minute 50 | 21.91 | 0.1 | 68.4 | 3.2 | +0.040 ± 0.005 | −1.4 ± 0.2 |
| DR search to 25, or 40 without a DR of 9 | 21.87 | 0.1 | 69.8 | 3.4 | +0.005 ± 0.003 | −0.0 ± 0.2 |

Nothing beats the fixed plan by more than the noise. The rules that lose are the ones that search longer once a result is in hand (a 23 on the sheet, DR search to minute 50), and they lose for the same reason as a late DR stop in section 6. Two things are behind the flat result:

- The fixed plan's minutes are priorities, not walls: a solver who runs out of EOs to look at moves on, and one with nothing left to finish goes back to look for more. So a scramble rich in EOs already gets more EO time, and one with few EOs already gets less.
- The decisions that do matter (section 6) are about how much to look at per EO and per DR, not about when, and those don't depend much on the scramble.

What about a different plan for each kind of scramble? I took every plan of round 3 and picked the best one per scramble type on the training scrambles (bad edges on the best axis, rich or poor in EOs, shortest EO, number of EOs of 4 or less), then played each type's pick on the held-out scrambles:

| Scramble feature | Plan chosen per type on the training scrambles (its gain there) | Held-out: score − tuned plan, moves |
|---|---|---|
| bad edges, best axis | 0 or 2: `te5_rzp_per_eo_6` (training −0.066); 4: `te5_rzp_per_eo_8` (training −0.058); 6 or more: `te5_rzp_per_eo_long_2` (training −0.028) | −0.028 ± 0.007 |
| scramble type (bad edges) | rich: two axes with 4 or fewer: `te5_rzp_per_eo_8` (training −0.052); neither: `te5_rzp_per_eo_8` (training −0.039); poor: none with 4 or fewer, one with 10 or more: `te5_dr_cap_12` (training −0.063) | −0.022 ± 0.008 |
| shortest EO | 2 or less: `te5_rzp_per_eo_8` (training −0.130); 3: `te5_rzp_per_eo_8` (training −0.054); 4: `te5_rzp_per_eo_long_3` (training −0.039); 5 or more: `te5_dr_cap_12` (training −0.083) | −0.029 ± 0.008 |
| EOs of 4 moves or less | 0 to 4: `te5_rzp_per_eo_long_2` (training −0.032); 5 to 14: `te5_rzp_per_eo_8` (training −0.030); 15 to 29: `te5_rzp_per_eo_8` (training −0.057); 30 or more: `te5_rzp_per_eo_6` (training −0.078) | −0.022 ± 0.007 |

So yeah, it helps a little, but only about as much as the best single tweak does on every scramble: 8 RZP states per short EO alone is −0.020 ± 0.007. Most of the picks *are* that tweak, and the training gains shrink a lot on new scrambles (that's just picking the luckiest plan out of 237). The one pick that looks like a real *adapt to the scramble* rule is on the hard ones (shortest EO 5 or more, or no axis with 4 bad edges or fewer): write DRs up to 12 instead of 11. That makes sense, a 12-move DR is worth having when nothing better is coming, but it's a small group and the gain isn't separately significant.

## 9. At most 22: the safety plan

The question is how to raise the share of attempts at 22 or better, and what it costs in mean. JTuu asked it from the other end: "when you have let's say 21 safety with 20 mins or so to look for better, anyone have advice for knowing when you should squeeze the 21 harder vs widen your search and prune very aggressively? I feel like I frequently do the wrong one" ([23 Dec 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1320666605478219837)). Each row is a plan:

| Plan | Mean, moves | DNF, % | ≤ 22, % | Sub-20, % | Score − tuned plan, moves | ≤ 22 − tuned plan, points |
|---|---|---|---|---|---|---|
| 2:30 minutes kept for writing | 21.77 | 56.4 | 32.3 | 1.7 | +4.535 ± 0.065 | −37.5 ± 0.8 |
| 3 minutes kept for writing | 21.77 | 33.1 | 49.2 | 2.6 | +2.620 ± 0.061 | −20.6 ± 0.7 |
| 3:30 minutes kept for writing | 21.80 | 17.1 | 60.4 | 3.1 | +1.317 ± 0.048 | −9.4 ± 0.5 |
| 4 minutes kept for writing | 21.81 | 8.2 | 66.2 | 3.2 | +0.606 ± 0.034 | −3.5 ± 0.4 |
| 4:30 minutes kept for writing | 21.82 | 4.0 | 69.0 | 3.4 | +0.277 ± 0.024 | −0.8 ± 0.3 |
| 6 minutes kept for writing | 21.86 | 0.2 | 70.1 | 3.5 | −0.003 ± 0.004 | +0.3 ± 0.1 |
| 7 minutes kept for writing (the tuned plan) | 21.87 | 0.1 | 69.8 | 3.4 | 0 | 0 |
| 10 minutes kept for writing | 21.90 | 0.1 | 68.8 | 3.4 | +0.034 ± 0.004 | −1.1 ± 0.2 |
| a DR that promises 22 or better: one route at once, bank a 22 | 21.86 | 0.1 | 70.3 | 3.4 | −0.011 ± 0.003 | +0.5 ± 0.1 |
| the same for 23 or better | 21.86 | 0.1 | 70.4 | 3.3 | −0.013 ± 0.004 | +0.6 ± 0.2 |
| bank every result at once (then 3 minutes to rewrite) | 21.89 | 0.1 | 69.3 | 3.4 | +0.015 ± 0.004 | −0.5 ± 0.2 |
| bank the first result | 22.26 | 0.1 | 58.7 | 2.9 | +0.390 ± 0.014 | −11.1 ± 0.5 |
| commit: DR search stops at minute 25, bank a 22 | 21.87 | 0.1 | 70.0 | 3.3 | −0.004 ± 0.004 | +0.2 ± 0.2 |

- **The time you keep for writing *is* the safety.** Below 4:30 the DNF rate shoots up: the last step before the reserve can run long, and so can the writing itself (section 4). Six or seven minutes is the sweet spot here, and 10 costs a little.
- **The quick look plus a written 22** raises ≤ 22 by +0.5 ± 0.1 points for −0.011 ± 0.003 in score: so the safe plan is actually slightly the better plan too.
- **Writing down every result at once** costs a little (+0.015 ± 0.004), and **writing down the first result** a lot (+0.390 ± 0.014). In the model a rewrite takes as long as the first write, so writing early only pays off when you'd otherwise lose the result.
- **Committing early** (DR search stops at minute 25, a 22 written down) is level with the tuned plan.

None of these runs isolates JTuu's case, a 21 in hand with 20 minutes left. What they do say is general: spreading routes over more DRs beats squeezing one (8 routes per DR costs +0.07 over the hour, finishing fewer DRs costs more, section 6), and searching longer once a result is in hand doesn't pay (section 8).

## 10. How the result scales

**With the length of the attempt.** The same two plans, with the clock set to other lengths (2,000 held-out scrambles each; the policy's minutes scale with the length). Each row is a length:

| Length of the attempt, minutes | Tuned plan: mean, moves | Tuned plan: DNF, % | Tuned plan: ≤ 22, % | Tuned plan: sub-20, % | Baseline: mean, moves | Baseline: DNF, % | Tuned − baseline score, moves |
|---|---|---|---|---|---|---|---|
| 20 | 23.07 | 1.5 | 31.9 | 1.4 | 23.04 | 3.4 | −0.10 ± 0.03 |
| 30 | 22.48 | 0.3 | 48.1 | 2.3 | 22.55 | 2.6 | −0.25 ± 0.03 |
| 45 | 22.09 | 0.1 | 60.9 | 2.9 | 22.19 | 1.8 | −0.23 ± 0.03 |
| 60 | 21.87 | 0.1 | 69.3 | 3.4 | 21.99 | 1.8 | −0.24 ± 0.03 |
| 75 | 21.74 | 0.1 | 75.0 | 3.6 | 21.84 | 1.2 | −0.19 ± 0.02 |
| 90 | 21.64 | 0.2 | 78.3 | 3.9 | 21.75 | 1.4 | −0.20 ± 0.02 |
| 120 | 21.52 | 0.1 | 83.0 | 4.3 | 21.61 | 1.0 | −0.16 ± 0.02 |

Going from 30 minutes to an hour is worth 0.6 of a move, and from one hour to two about 0.35. The tuned plan beats the baseline at every length, mostly by not DNFing.

**With the solver.** The same plans for a faster or sharper solver. Each row is a solver:

| Solver | Tuned plan: mean, moves | DNF, % | ≤ 22, % | Sub-20, % | Baseline: mean, moves |
|---|---|---|---|---|---|
| every step twice as slow (same as 30 minutes) | 22.48 | 0.3 | 48.1 | 2.3 | 22.55 |
| every step 1.4 times as slow | 22.13 | 0.1 | 59.6 | 2.9 | 22.23 |
| the costs of section 4 | 21.87 | 0.1 | 69.3 | 3.4 | 21.99 |
| every step 0.7 times as long | 21.67 | 0.1 | 77.3 | 3.9 | 21.78 |
| every step half as long (same as 2 hours) | 21.52 | 0.1 | 83.0 | 4.3 | 21.61 |
| reading error of an RZP state halved (0.5 moves) | 21.73 | 0.1 | 74.2 | 4.0 | 21.80 |
| sees more of the DRs near an RZP state | 21.81 | 0.1 | 71.4 | 3.6 | 21.92 |
| all three: half as long, sharper read, sees more DRs | 21.35 | 0.1 | 88.6 | 5.3 | 21.43 |

Every step twice as fast is exactly the same as two hours: in the model, speed and time are the same thing. A read of an RZP state that is twice as sharp is worth about as much as 15 extra minutes. With all three together the tuned plan averages 21.35, with 5.3% sub-20, still short of the real top 5's 7.4% sub-20. So what caps the simulator is its toolbox (section 12), not its clock.

**One decision at a time.** The read cut-off: work an RZP state only if its read promises a DR of at most this many moves. Each row is a cut-off:

| Work an RZP state only if its read promises a DR of at most, moves | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 8 | 22.13 | 3.1 | 58.4 | +0.497 ± 0.025 |
| 8.5 | 22.02 | 0.9 | 63.3 | +0.217 ± 0.018 |
| 9 | 21.94 | 0.2 | 66.4 | +0.080 ± 0.014 |
| 9.5 | 21.88 | 0.1 | 69.2 | +0.015 ± 0.010 |
| 10 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |
| 10.5 | 21.91 | 0.1 | 68.6 | +0.045 ± 0.009 |
| 11 | 21.96 | 0.1 | 66.8 | +0.096 ± 0.011 |
| 12 | 22.00 | 0.1 | 65.3 | +0.133 ± 0.011 |
| 13 | 22.00 | 0.1 | 65.3 | +0.135 ± 0.011 |

The sweet spot is sharp, 9.5 to 10. Go lower and you skip states that would've given good DRs. Go higher and you burn time on states that rarely give a DR worth finishing. A switch: how much worse a look on the other side is ranked than one on the same side. Each row is a penalty:

| A switch ranked this much worse than staying, moves | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 0 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |
| 0.6 | 21.90 | 0.1 | 69.0 | +0.026 ± 0.006 |
| 1 | 21.93 | 0.1 | 68.0 | +0.062 ± 0.009 |
| 2 | 22.02 | 0.1 | 65.2 | +0.153 ± 0.012 |
| never switch | 22.18 | 0.2 | 60.0 | +0.319 ± 0.016 |

Never switching costs +0.32. Appendix A has the other one-at-a-time curves.

## 11. What depends on the costs

Since every cost is a guess, here's the stress test. I took the plans behind the conclusions and reran each one against the tuned plan with one cost or limit moved at a time: every cost of section 4 halved and doubled (writing the solution together with the time you keep for it, since you know your own writing speed), and the reading error, how often a route gives its finish, and how many DRs and EOs you see, moved down and up. That's 32 runs of 2,000 held-out scrambles each, same scrambles every time. *Better* or *worse* means more than two standard errors, *level* means less. Each row is a plan:

| Plan, against the tuned plan | Score difference, costs of section 4 | Smallest difference over all runs | Largest difference | Runs where it is better | Runs where it is level | Runs where it is worse | Runs where it goes the other way |
|---|---|---|---|---|---|---|---|
| EO writing to minute 5, DR search to 25 | +0.01 ± 0.01 | −0.01 | 0.01 | 0 | 33 | 0 | none |
| EO writing to minute 12, DR search to 45 | +0.03 ± 0.01 | 0.00 | 0.18 | 0 | 1 | 32 | none |
| EO writing to minute 16, DR search to 50 | +0.21 ± 0.02 | 0.06 | 0.44 | 0 | 0 | 33 | none |
| depth first throughout | +0.01 ± 0.01 | 0.00 | 0.06 | 0 | 15 | 18 | none |
| quick route on a DR promising 22 | −0.01 ± 0.00 | −0.01 | 0.00 | 13 | 20 | 0 | none |
| a backup by minute 20 | −0.00 ± 0.00 | −0.00 | 0.01 | 1 | 32 | 0 | none |
| rich in EOs: DR search to 30 | −0.00 ± 0.00 | −0.01 | 0.01 | 3 | 30 | 0 | none |
| 5-movers only when poor in EOs | −0.00 ± 0.00 | −0.01 | 0.00 | 1 | 32 | 0 | none |
| a 22 on the sheet: DR search to 50 | +0.01 ± 0.00 | −0.06 | 0.04 | 1 | 2 | 30 | spread of step times: double |
| quick route on a DR promising 22, bank a 22 | −0.01 ± 0.00 | −0.09 | −0.00 | 30 | 3 | 0 | none |
| commit: DR search stops at 25 | −0.00 ± 0.01 | −0.08 | 0.01 | 5 | 28 | 0 | none |
| 10 minutes kept for writing | +0.04 ± 0.01 | −0.07 | 0.11 | 1 | 1 | 31 | spread of step times: double |
| 1 RZP state per short EO | +0.13 ± 0.02 | 0.07 | 0.17 | 0 | 0 | 33 | none |
| 8 RZP states per short EO | −0.03 ± 0.01 | −0.07 | −0.00 | 29 | 4 | 0 | none |
| read cut-off 9 | +0.09 ± 0.02 | −0.08 | 0.37 | 1 | 1 | 31 | reading error of an RZP state: 2 |
| read cut-off 11 | +0.09 ± 0.01 | 0.01 | 0.15 | 0 | 1 | 32 | none |
| 2 routes per DR | +0.07 ± 0.01 | 0.01 | 0.11 | 0 | 1 | 32 | none |
| 8 routes per DR | +0.06 ± 0.01 | 0.02 | 0.10 | 0 | 1 | 32 | none |
| finish at most 2 DRs | +0.44 ± 0.02 | 0.25 | 0.51 | 0 | 0 | 33 | none |
| EOs of 4 or less only | +0.00 ± 0.00 | −0.01 | 0.01 | 1 | 32 | 0 | none |
| never switch | +0.32 ± 0.02 | 0.27 | 0.37 | 0 | 0 | 33 | none |
| write at most 20 EOs | +0.00 ± 0.01 | −0.00 | 0.01 | 0 | 33 | 0 | none |
| DR search stops at 20 | +0.01 ± 0.01 | −0.00 | 0.03 | 0 | 13 | 20 | none |
| DR search stops at 45 | +0.01 ± 0.00 | −0.01 | 0.05 | 0 | 9 | 24 | none |
| the baseline | +0.24 ± 0.03 | 0.09 | 0.65 | 0 | 0 | 33 | none |

If a plan keeps its verdict in most runs and nothing flips it to the other side, I'd call that conclusion solid. The last column names the moved costs that do flip it.

What holds up:

- **Solid:** the stuff about how much you look at. Finishing only a couple of DRs, 1 RZP state per short EO, 2 or 8 routes per DR, never switching and writing EOs until minute 16 are worse in pretty much every run. 8 RZP states per short EO and the quick route plus a written 22 are better or level in every run, never worse. The baseline loses to the tuned plan in every single run.
- **Flat whatever the costs:** the time split between 3-12 minutes of EOs and 25-40 minutes of DR search, the adaptive rules and the backups stay level or close to it everywhere.
- **Depends on you:**
  - The read cut-off. With a much noisier read of RZP states, a cut-off of 9 beats 10, so the cut-off is really about how far you trust your read.
  - The time you keep for writing. If your step times vary a lot more than the model's, 10 minutes beats 7.
  - Depth first is level or a bit worse, never better.

The same runs read the other way: how much does the tuned plan's own result move when one cost moves? That's basically the order to tune the costs in, biggest effect first. Each row is one cost or limit moved:

| Cost or limit moved | Tuned plan: mean, moves | DNF, % | ≤ 22, % | Score change from section 4 costs, moves |
|---|---|---|---|---|
| reading error of an RZP state: 2 | 22.33 | 0.5 | 52.1 | +0.49 |
| reading error of an RZP state: 0.5 | 21.73 | 0.1 | 74.2 | −0.15 |
| DRs seen: fewer | 22.01 | 0.2 | 63.8 | +0.14 |
| try an HTR route: double | 22.00 | 0.1 | 63.9 | +0.13 |
| spread of step times: double | 21.87 | 1.8 | 68.3 | +0.13 |
| write the solution (and the reserve with it): double | 21.98 | 0.1 | 65.0 | +0.10 |
| write an EO: double | 21.97 | 0.1 | 65.8 | +0.10 |
| EOs seen: fewer | 21.96 | 0.3 | 66.3 | +0.10 |
| write out a finish: double | 21.95 | 0.1 | 65.9 | +0.08 |
| try an HTR route: half | 21.80 | 0.1 | 72.3 | −0.07 |
| work an RZP state: double | 21.94 | 0.1 | 66.8 | +0.07 |
| DRs seen: more | 21.81 | 0.1 | 71.4 | −0.07 |
| glance at an EO: double | 21.94 | 0.1 | 66.7 | +0.06 |
| write an EO: half | 21.82 | 0.1 | 71.4 | −0.05 |
| write a DR: double | 21.92 | 0.1 | 67.7 | +0.05 |
| a route gives its finish: 0.7 | 21.92 | 0.1 | 68.0 | +0.05 |
| write out a finish: half | 21.83 | 0.1 | 71.2 | −0.05 |
| switch: double | 21.92 | 0.1 | 67.7 | +0.05 |
| work an RZP state: half | 21.83 | 0.1 | 70.9 | −0.04 |
| scan for EOs: double | 21.91 | 0.2 | 68.0 | +0.04 |
| read a DR: double | 21.91 | 0.1 | 68.2 | +0.04 |
| EOs seen: more | 21.84 | 0.1 | 70.5 | −0.04 |
| glance at an EO: half | 21.84 | 0.1 | 70.5 | −0.03 |
| write the solution (and the reserve with it): half | 21.83 | 0.3 | 71.0 | −0.03 |
| write a DR: half | 21.85 | 0.1 | 70.2 | −0.03 |
| scan for EOs: half | 21.85 | 0.1 | 70.2 | −0.02 |
| switch: half | 21.85 | 0.1 | 70.2 | −0.02 |
| read a DR: half | 21.86 | 0.1 | 70.0 | −0.01 |
| a route gives its finish: 1 | 21.86 | 0.1 | 70.3 | −0.01 |
| look at the scramble (bad edges): double | 21.88 | 0.1 | 69.2 | +0.00 |
| spread of step times: half | 21.87 | 0.1 | 69.4 | −0.00 |
| look at the scramble (bad edges): half | 21.87 | 0.1 | 69.5 | −0.00 |
| costs as in section 4 | 21.87 | 0.1 | 69.3 | +0.00 |

## 12. What this does not model

The simulated solver is a DR solver with a fixed toolbox. Here's what it leaves out, roughly in order of how much I think it matters:

- **Finishes outside the DR group.** No DR-breaking finishes, no leave-slice skeleton with an insertion, no blockbuilding. Real sub-20s often come from these; it is the main reason the simulated results spread less than real ones (section 5).
- **EOs of 6 moves or more, RZPs of more than 3 moves, DRs not through a written EO.** The search space is the one the guides describe; a solver who goes further has more to find and more to spend time on.
- **Variations of a DR beyond the last quarter turn.** The solver tries routes on the DR and on its twin (the last quarter turn made the other way), not on other DRs of the same RZP.
- **How a route is searched.** A route tried gives the best finish along it or nothing, in a fixed time. In reality some routes take seconds and some take minutes, and a finish one move worse is often found first.
- **The reading of an RZP state** is the exact distance blurred by symmetric noise. Real reads are biased per case (some DRMs look better than they are), and better solvers have a sharper and less biased read.
- **Mistakes**: miswritten moves, a wrong scramble, a solution that fails the check, a slip that costs ten minutes. The only DNF in the simulator is the clock.
- **Learning within the attempt.** The solver doesn't get faster on a scramble it knows, or use a written solution as a shorter scramble (Jay's trick, [1 Mar 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1345610231337455706)).
- **Nerves and competition.** The pace varies from attempt to attempt, but there's no panic at the 30-minute call and no difference between home and comp, which people do describe: Dunni, "in comp as soon as 30 minutes is called put panic mode starts" ([14 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1405613442681016521)), and Yura Riabov playing it safer in comp ([2 Mar 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1345802699937157362)).
- **The solver is one person.** The costs are one set of numbers for a top solver; a 24-average solver is not just a slower version (they also see less, and that is a different column of section 4).

## Appendix A: full tables

**Each change of the tuned plan alone, against the baseline** (round 2, held-out scrambles). Each row is one change:

| Change to the baseline | Mean, moves | DNF, % | ≤ 22, % | Sub-20, % | Score − baseline, moves | ≤ 22 − baseline, points |
|---|---|---|---|---|---|---|
| baseline | 21.99 | 1.9 | 64.8 | 3.0 | 0 | 0 |
| only work an RZP whose read promises a DR of 10 or less (baseline 11.5) | 21.85 | 1.8 | 69.6 | 3.4 | −0.14 ± 0.02 | +4.9 ± 0.5 |
| keep 7 minutes for writing (baseline 5) | 22.02 | 0.1 | 64.7 | 3.0 | −0.11 ± 0.02 | −0.1 ± 0.2 |
| switch as readily as staying (baseline: a switch ranked 0.3 worse) | 21.96 | 1.6 | 66.1 | 3.1 | −0.06 ± 0.01 | +1.3 ± 0.3 |
| never switch | 22.26 | 1.7 | 56.3 | 1.9 | +0.25 ± 0.02 | −8.4 ± 0.6 |
| finish only one DR | 22.71 | 2.4 | 40.9 | 1.9 | +0.74 ± 0.02 | −23.9 ± 0.7 |

**The other one-at-a-time curves**, around the tuned plan. Each row of each table is a value of that one setting:

| RZP states worked per 5-move EO, states | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 0 | 21.98 | 0.1 | 65.4 | +0.113 ± 0.011 |
| 1 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |
| 2 | 21.86 | 0.1 | 70.1 | −0.011 ± 0.005 |
| 3 | 21.86 | 0.1 | 70.2 | −0.008 ± 0.006 |

| RZP moves at most, moves | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 1 | 21.88 | 0.1 | 69.6 | +0.007 ± 0.006 |
| 2 | 21.87 | 0.1 | 69.8 | −0.001 ± 0.001 |
| 3 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |

| Extra RZP states per EO on each pass back, states | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 0 | 21.94 | 1.1 | 66.6 | +0.153 ± 0.013 |
| 1 | 21.88 | 0.1 | 69.7 | +0.007 ± 0.003 |
| 2 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |
| 4 | 21.87 | 0.1 | 69.8 | −0.001 ± 0.003 |

| DRs taken from one EO ending and axis, DRs | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 1 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |
| 2 | 21.86 | 0.1 | 70.1 | −0.005 ± 0.006 |
| 3 | 21.86 | 0.1 | 70.1 | −0.004 ± 0.006 |

| Longest DR written, moves | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 10 | 21.90 | 4.8 | 65.3 | +0.414 ± 0.025 |
| 11 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |
| 12 | 21.89 | 0.1 | 69.3 | +0.019 ± 0.006 |

| Skip a DR whose chance of beating the best so far is under, % | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 0 | 21.91 | 0.1 | 67.6 | +0.039 ± 0.008 |
| 1 | 21.87 | 0.1 | 68.6 | +0.005 ± 0.008 |
| 3 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |
| 6 | 21.88 | 0.1 | 69.6 | +0.006 ± 0.002 |
| 10 | 21.95 | 0.1 | 67.5 | +0.077 ± 0.007 |
| 20 | 22.05 | 0.1 | 62.8 | +0.181 ± 0.010 |

| Time kept for writing the solution, minutes | Mean, moves | DNF, % | ≤ 22, % | Score − tuned plan, moves |
|---|---|---|---|---|
| 3 | 21.77 | 33.1 | 49.2 | +2.620 ± 0.061 |
| 4 | 21.81 | 8.2 | 66.2 | +0.606 ± 0.034 |
| 6 | 21.86 | 0.2 | 70.1 | −0.003 ± 0.004 |
| 7 (tuned plan) | 21.87 | 0.1 | 69.8 | 0 |

**Every plan of round 3** on the held-out scrambles, best score first. Names are the policy names in `research/policies/t_all.toml`: `te1` time split, `te2` order, `te3` adaptive, `te4` safety, `te5` one setting at a time. Each row is a plan:

| Plan (policy name) | Mean, moves | DNF, % | ≤ 22, % | Sub-20, % | Score − tuned plan, moves |
|---|---|---|---|---|---|
| `te5_rzp_per_eo_8` | 21.85 | 0.1 | 70.6 | 3.4 | −0.020 ± 0.007 |
| `te4_quick23p5_r1` | 21.86 | 0.1 | 70.4 | 3.3 | −0.013 ± 0.004 |
| `te4_quick22p5_r2` | 21.86 | 0.1 | 70.3 | 3.4 | −0.012 ± 0.003 |
| `te4_quick22p5_r1` | 21.86 | 0.1 | 70.3 | 3.4 | −0.011 ± 0.003 |
| `te4_safe_bk900_q22p5` | 21.86 | 0.1 | 70.4 | 3.4 | −0.011 ± 0.003 |
| `te5_rzp_per_eo_6` | 21.86 | 0.1 | 70.5 | 3.4 | −0.011 ± 0.007 |
| `te4_safe_bk1800_q22p5` | 21.86 | 0.1 | 70.3 | 3.4 | −0.011 ± 0.003 |
| `te5_rzp_per_eo_long_2` | 21.86 | 0.1 | 70.1 | 3.4 | −0.011 ± 0.005 |
| `te4_quick23p5_r2` | 21.86 | 0.1 | 70.4 | 3.3 | −0.011 ± 0.004 |
| `te4_safe_bk1200_q22p5` | 21.86 | 0.1 | 70.4 | 3.4 | −0.011 ± 0.003 |
| `te4_safe_bk1500_q22p5` | 21.86 | 0.1 | 70.3 | 3.4 | −0.011 ± 0.003 |
| `te4_commit1800` | 21.86 | 0.1 | 70.4 | 3.4 | −0.011 ± 0.004 |
| `te4_quick21p5_r2` | 21.86 | 0.1 | 70.2 | 3.4 | −0.010 ± 0.003 |
| `te4_quick21p5_r1` | 21.86 | 0.1 | 70.2 | 3.4 | −0.010 ± 0.003 |
| `te4_bankat22_rr180` | 21.86 | 0.1 | 70.2 | 3.4 | −0.009 ± 0.003 |
| `te5_rzp_per_eo_long_3` | 21.86 | 0.1 | 70.2 | 3.4 | −0.008 ± 0.006 |
| `te4_bankat21_rr180` | 21.86 | 0.1 | 70.1 | 3.4 | −0.007 ± 0.002 |
| `te5_htr_per_dr_3` | 21.86 | 0.1 | 70.7 | 3.5 | −0.006 ± 0.007 |
| `te4_bankat23_rr180` | 21.87 | 0.1 | 70.2 | 3.4 | −0.005 ± 0.003 |
| `te5_dr_per_line_2` | 21.86 | 0.1 | 70.1 | 3.4 | −0.005 ± 0.006 |
| `te2_eagerfin23p5_r1` | 21.86 | 0.1 | 70.0 | 3.4 | −0.004 ± 0.003 |
| `te5_rzp_per_eo_4` | 21.86 | 0.1 | 70.0 | 3.4 | −0.004 ± 0.005 |
| `te5_dr_per_line_3` | 21.86 | 0.1 | 70.1 | 3.4 | −0.004 ± 0.006 |
| `te2_eagerfin22p5_r1` | 21.87 | 0.1 | 70.0 | 3.4 | −0.004 ± 0.001 |
| `te2_eagerfin99_r1` | 21.86 | 0.1 | 70.1 | 3.4 | −0.004 ± 0.005 |
| `te4_commit1500` | 21.87 | 0.1 | 70.0 | 3.3 | −0.004 ± 0.004 |
| `te4_reserve360` | 21.86 | 0.2 | 70.1 | 3.5 | −0.003 ± 0.004 |
| `te5_reserve_360` | 21.86 | 0.2 | 70.1 | 3.5 | −0.003 ± 0.004 |
| `te2_eagerfin22p5_r2` | 21.87 | 0.1 | 69.9 | 3.5 | −0.003 ± 0.001 |
| `te2_eagerfin22p5_r99` | 21.87 | 0.1 | 70.0 | 3.5 | −0.003 ± 0.002 |
| `te3_rich35_tdr1800` | 21.87 | 0.1 | 70.0 | 3.4 | −0.002 ± 0.002 |
| `te5_eo_cap_30` | 21.87 | 0.1 | 70.0 | 3.4 | −0.002 ± 0.002 |
| `te2_backup600` | 21.87 | 0.1 | 70.0 | 3.5 | −0.002 ± 0.003 |
| `te2_backup900` | 21.87 | 0.1 | 69.9 | 3.4 | −0.002 ± 0.002 |
| `te3_rich25_tdr1800` | 21.87 | 0.1 | 70.0 | 3.4 | −0.002 ± 0.002 |
| `te3_rich15_tdr1800` | 21.87 | 0.1 | 70.0 | 3.4 | −0.002 ± 0.002 |
| `te3_early1800_late9_2400` | 21.87 | 0.1 | 70.0 | 3.4 | −0.002 ± 0.002 |
| `te5_t_dr_1800` | 21.87 | 0.1 | 70.0 | 3.4 | −0.002 ± 0.002 |
| `te2_eagerfin21p5_r1` | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.001 |
| `te2_backup1800` | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.001 |
| `te3_enough5_len9` | 21.87 | 0.1 | 69.9 | 3.4 | −0.001 ± 0.001 |
| `te2_eagerfin21p5_r2` | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.000 |
| `te2_eagerfin21p5_r99` | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.000 |
| `te2_backup1500` | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.001 |
| `te3_poor25` | 21.87 | 0.1 | 69.9 | 3.4 | −0.001 ± 0.001 |
| `te5_rzp_depth_2` | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.001 |
| `te3_poor15` | 21.87 | 0.1 | 69.9 | 3.4 | −0.001 ± 0.002 |
| `te5_rzp_more_4` | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.003 |
| `te1_teo480_tdr1800` | 21.87 | 0.1 | 70.0 | 3.4 | −0.001 ± 0.003 |
| `te2_eagerfin20p5_r2` | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.000 |
| `te2_eagerfin20p5_r99` | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.000 |
| `te2_backup1200` | 21.87 | 0.1 | 69.8 | 3.4 | −0.001 ± 0.001 |
| `te2_eagerfin20p5_r1` | 21.87 | 0.1 | 69.8 | 3.4 | −0.000 ± 0.000 |
| `te3_enough5_len8` | 21.87 | 0.1 | 69.8 | 3.4 | −0.000 ± 0.000 |
| `te3_early1800_late10_2400` | 21.87 | 0.1 | 70.0 | 3.4 | −0.000 ± 0.002 |
| `ref` | 21.87 | 0.1 | 69.8 | 3.4 | 0 |
| `te2_backup2100` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te2_backup2400` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te3_rich50_tdr1500` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te3_rich50_tdr1800` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te3_poor40` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te3_enough2_len8` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.001 |
| `te3_early1800_late9_2700` | 21.87 | 0.1 | 70.0 | 3.4 | +0.000 ± 0.003 |
| `te4_reserve420` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te4_stop20` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te4_stop21` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te4_stop22` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te4_stop23` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te5_read_max_10` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te5_switch_pen_0` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.000 |
| `te2_eagereo2` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.001 |
| `te3_enough3_len8` | 21.87 | 0.1 | 69.8 | 3.4 | +0.000 ± 0.001 |
| `te2_eagerfin23p5_r2` | 21.87 | 0.1 | 69.9 | 3.4 | +0.001 ± 0.004 |
| `te3_early1800_late10_2700` | 21.87 | 0.1 | 70.0 | 3.4 | +0.001 ± 0.003 |
| `te4_bankat21_rr300` | 21.87 | 0.1 | 69.8 | 3.4 | +0.001 ± 0.001 |
| `te4_bankat22_rr300` | 21.87 | 0.1 | 69.8 | 3.4 | +0.001 ± 0.002 |
| `te1_teo480_tdr2100` | 21.87 | 0.1 | 69.8 | 3.4 | +0.001 ± 0.001 |
| `te3_enough1_len8` | 21.87 | 0.1 | 69.8 | 3.5 | +0.001 ± 0.001 |
| `te3_rich35_tdr2400` | 21.87 | 0.1 | 69.8 | 3.4 | +0.001 ± 0.002 |
| `te3_late10_tdr2400` | 21.87 | 0.1 | 69.8 | 3.4 | +0.001 ± 0.001 |
| `te3_enough3_len9` | 21.87 | 0.1 | 69.8 | 3.4 | +0.001 ± 0.002 |
| `te3_rich50_tdr2400` | 21.87 | 0.1 | 69.8 | 3.4 | +0.002 ± 0.001 |
| `te3_rich35_tdr1500` | 21.87 | 0.1 | 69.7 | 3.4 | +0.002 ± 0.003 |
| `te3_late9_tdr2400` | 21.87 | 0.1 | 69.8 | 3.4 | +0.002 ± 0.001 |
| `te3_rich50_tdr2700` | 21.87 | 0.1 | 69.7 | 3.4 | +0.002 ± 0.001 |
| `te3_late10_tdr2700` | 21.87 | 0.1 | 69.8 | 3.4 | +0.002 ± 0.001 |
| `te3_bk21_tdr2700` | 21.87 | 0.1 | 69.8 | 3.4 | +0.003 ± 0.001 |
| `te3_late8_tdr2400` | 21.87 | 0.1 | 69.8 | 3.4 | +0.003 ± 0.002 |
| `te3_late9_tdr2700` | 21.87 | 0.1 | 69.7 | 3.4 | +0.003 ± 0.002 |
| `te5_eo_cap_60` | 21.87 | 0.1 | 69.8 | 3.4 | +0.003 ± 0.004 |
| `te3_late10_tdr3000` | 21.87 | 0.1 | 69.8 | 3.4 | +0.004 ± 0.002 |
| `te3_rich25_tdr2400` | 21.87 | 0.1 | 69.8 | 3.4 | +0.004 ± 0.002 |
| `te1_teo300_tdr1800` | 21.87 | 0.1 | 69.9 | 3.4 | +0.004 ± 0.004 |
| `te3_rich15_tdr2400` | 21.87 | 0.1 | 69.8 | 3.4 | +0.004 ± 0.002 |
| `te3_poor10` | 21.87 | 0.1 | 69.8 | 3.4 | +0.004 ± 0.003 |
| `te3_bk21_tdr3000` | 21.87 | 0.1 | 69.8 | 3.3 | +0.004 ± 0.001 |
| `te5_t_dr_2400` | 21.87 | 0.1 | 69.8 | 3.4 | +0.004 ± 0.002 |
| `te3_rich25_tdr1500` | 21.87 | 0.1 | 69.7 | 3.4 | +0.004 ± 0.003 |
| `te3_enough2_len9` | 21.87 | 0.1 | 69.7 | 3.4 | +0.004 ± 0.003 |
| `te2_eagereo3` | 21.87 | 0.1 | 69.8 | 3.4 | +0.005 ± 0.004 |
| `te2_dfs_eo3_fin22p5` | 21.87 | 0.1 | 69.9 | 3.4 | +0.005 ± 0.004 |
| `te3_early1500_late9_2400` | 21.87 | 0.1 | 69.8 | 3.4 | +0.005 ± 0.003 |
| `te4_bankat24_rr180` | 21.88 | 0.1 | 69.7 | 3.4 | +0.005 ± 0.003 |
| `te5_fin_min_p_0p01` | 21.87 | 0.1 | 68.6 | 3.7 | +0.005 ± 0.008 |
| `te5_eo_cap_20` | 21.87 | 0.1 | 69.7 | 3.4 | +0.005 ± 0.004 |
| `te3_rich15_tdr1500` | 21.87 | 0.1 | 69.7 | 3.4 | +0.005 ± 0.003 |
| `te3_poor6` | 21.87 | 0.1 | 69.8 | 3.4 | +0.005 ± 0.004 |
| `te3_enough5_len10` | 21.87 | 0.1 | 69.7 | 3.4 | +0.005 ± 0.004 |
| `te5_t_dr_1500` | 21.87 | 0.1 | 69.7 | 3.4 | +0.005 ± 0.003 |
| `te1_teo300_tdr2100` | 21.87 | 0.1 | 69.8 | 3.4 | +0.006 ± 0.004 |
| `te3_bk21_tdr3150` | 21.88 | 0.1 | 69.8 | 3.2 | +0.006 ± 0.002 |
| `te5_fin_min_p_0p06` | 21.88 | 0.1 | 69.6 | 3.3 | +0.006 ± 0.002 |
| `te3_early1500_late9_2700` | 21.88 | 0.1 | 69.7 | 3.4 | +0.006 ± 0.003 |
| `te2_eagerfin23p5_r99` | 21.87 | 0.1 | 69.6 | 3.4 | +0.006 ± 0.005 |
| `te3_eo4only` | 21.87 | 0.1 | 69.7 | 3.4 | +0.006 ± 0.004 |
| `te3_early1500_late10_2400` | 21.88 | 0.1 | 69.6 | 3.4 | +0.006 ± 0.003 |
| `te5_eo_len_4` | 21.87 | 0.1 | 69.7 | 3.4 | +0.006 ± 0.004 |
| `te1_teo720_tdr2100` | 21.88 | 0.1 | 69.5 | 3.4 | +0.007 ± 0.005 |
| `te4_bankat23_rr300` | 21.88 | 0.1 | 69.6 | 3.4 | +0.007 ± 0.003 |
| `te1_teo300_tdr1500` | 21.87 | 0.1 | 69.8 | 3.4 | +0.007 ± 0.004 |
| `te3_early1500_late10_2700` | 21.88 | 0.1 | 69.6 | 3.4 | +0.007 ± 0.003 |
| `te5_rzp_depth_1` | 21.88 | 0.1 | 69.6 | 3.3 | +0.007 ± 0.006 |
| `te1_teo300_tdr2400` | 21.87 | 0.1 | 69.8 | 3.4 | +0.007 ± 0.004 |
| `te1_teo480_tdr1500` | 21.88 | 0.1 | 69.6 | 3.4 | +0.007 ± 0.003 |
| `te5_rzp_more_1` | 21.88 | 0.1 | 69.7 | 3.4 | +0.007 ± 0.003 |
| `te1_teo480_tdr2400` | 21.88 | 0.1 | 69.7 | 3.4 | +0.008 ± 0.003 |
| `te3_enough1_len9` | 21.88 | 0.1 | 69.7 | 3.4 | +0.008 ± 0.004 |
| `te4_commit1200` | 21.88 | 0.1 | 69.8 | 3.3 | +0.008 ± 0.006 |
| `te1_teo300_tdr2700` | 21.88 | 0.1 | 69.8 | 3.4 | +0.009 ± 0.004 |
| `te3_rich35_tdr2700` | 21.88 | 0.1 | 69.6 | 3.4 | +0.009 ± 0.003 |
| `te3_late8_tdr2700` | 21.88 | 0.1 | 69.5 | 3.4 | +0.010 ± 0.003 |
| `te1_teo300_tdr1200` | 21.88 | 0.1 | 69.7 | 3.4 | +0.011 ± 0.005 |
| `te3_bk22_tdr2700` | 21.88 | 0.1 | 69.8 | 3.3 | +0.011 ± 0.003 |
| `te1_teo720_tdr1800` | 21.88 | 0.1 | 69.3 | 3.4 | +0.011 ± 0.005 |
| `te3_late9_tdr3000` | 21.88 | 0.1 | 69.3 | 3.4 | +0.011 ± 0.003 |
| `te5_read_on_find_false` | 21.88 | 0.1 | 69.8 | 3.2 | +0.011 ± 0.004 |
| `te3_rich25_tdr2700` | 21.88 | 0.1 | 69.4 | 3.4 | +0.013 ± 0.003 |
| `te3_rich15_tdr2700` | 21.88 | 0.1 | 69.4 | 3.4 | +0.013 ± 0.003 |
| `te5_t_dr_2700` | 21.88 | 0.1 | 69.4 | 3.4 | +0.013 ± 0.003 |
| `te5_fin_max_6` | 21.88 | 0.1 | 69.2 | 3.4 | +0.013 ± 0.002 |
| `te1_teo300_tdr900` | 21.88 | 0.1 | 69.5 | 3.3 | +0.014 ± 0.005 |
| `te4_bankalways` | 21.89 | 0.1 | 69.3 | 3.4 | +0.015 ± 0.004 |
| `te3_bk22_tdr3000` | 21.89 | 0.1 | 69.8 | 3.2 | +0.015 ± 0.003 |
| `te5_read_max_9p5` | 21.88 | 0.1 | 69.2 | 3.4 | +0.015 ± 0.010 |
| `te3_enough3_len10` | 21.88 | 0.1 | 69.2 | 3.4 | +0.015 ± 0.005 |
| `te5_eo_cap_10` | 21.88 | 0.1 | 69.5 | 3.2 | +0.016 ± 0.005 |
| `te2_eagereo4` | 21.88 | 0.1 | 69.4 | 3.3 | +0.016 ± 0.006 |
| `te1_teo480_tdr2700` | 21.89 | 0.1 | 69.3 | 3.4 | +0.017 ± 0.004 |
| `te1_teo300_tdr3000` | 21.88 | 0.1 | 69.4 | 3.4 | +0.018 ± 0.005 |
| `te5_t_dr_1200` | 21.88 | 0.1 | 69.3 | 3.3 | +0.018 ± 0.005 |
| `te1_teo180_tdr900` | 21.89 | 0.1 | 69.5 | 3.2 | +0.018 ± 0.005 |
| `te1_teo180_tdr1800` | 21.89 | 0.1 | 69.5 | 3.2 | +0.018 ± 0.005 |
| `te1_teo180_tdr2100` | 21.89 | 0.1 | 69.5 | 3.2 | +0.018 ± 0.005 |
| `te1_teo720_tdr2400` | 21.89 | 0.1 | 69.0 | 3.4 | +0.018 ± 0.005 |
| `te1_teo180_tdr1500` | 21.89 | 0.1 | 69.5 | 3.2 | +0.018 ± 0.005 |
| `te1_teo180_tdr1200` | 21.89 | 0.1 | 69.5 | 3.2 | +0.019 ± 0.005 |
| `te2_eagereo5` | 21.89 | 0.1 | 69.4 | 3.3 | +0.019 ± 0.006 |
| `te3_bk22_tdr3150` | 21.89 | 0.1 | 69.8 | 3.2 | +0.019 ± 0.004 |
| `te1_teo180_tdr2400` | 21.89 | 0.1 | 69.4 | 3.2 | +0.019 ± 0.005 |
| `te3_late8_tdr3000` | 21.89 | 0.1 | 69.1 | 3.4 | +0.019 ± 0.004 |
| `te4_bankat24_rr300` | 21.89 | 0.1 | 69.1 | 3.4 | +0.019 ± 0.004 |
| `te5_dr_cap_12` | 21.89 | 0.1 | 69.3 | 3.4 | +0.019 ± 0.006 |
| `te1_teo480_tdr1200` | 21.89 | 0.1 | 69.3 | 3.3 | +0.020 ± 0.005 |
| `te5_eo_len_3` | 21.89 | 0.1 | 69.3 | 3.3 | +0.020 ± 0.006 |
| `te1_teo180_tdr2700` | 21.89 | 0.1 | 69.3 | 3.2 | +0.020 ± 0.006 |
| `te5_eo_cap_80` | 21.89 | 0.1 | 69.0 | 3.3 | +0.021 ± 0.006 |
| `te2_eagerfin99_r2` | 21.89 | 0.1 | 69.1 | 3.4 | +0.022 ± 0.006 |
| `te2_dfs_r1` | 21.89 | 0.1 | 69.3 | 3.3 | +0.023 ± 0.007 |
| `te3_enough2_len10` | 21.89 | 0.1 | 69.1 | 3.4 | +0.023 ± 0.006 |
| `te5_t_dr_3000` | 21.89 | 0.1 | 69.0 | 3.3 | +0.025 ± 0.004 |
| `te4_bankfirst_rr300` | 21.90 | 0.1 | 69.2 | 3.4 | +0.025 ± 0.004 |
| `te2_dfs` | 21.89 | 0.1 | 69.2 | 3.3 | +0.026 ± 0.006 |
| `te5_switch_pen_0p6` | 21.90 | 0.1 | 69.0 | 3.3 | +0.026 ± 0.006 |
| `te2_dfs_eo3` | 21.89 | 0.1 | 69.2 | 3.3 | +0.027 ± 0.007 |
| `te3_enough1_len10` | 21.89 | 0.1 | 69.0 | 3.4 | +0.028 ± 0.006 |
| `te5_htr_per_dr_6` | 21.90 | 0.1 | 68.5 | 3.5 | +0.028 ± 0.008 |
| `te1_teo180_tdr3000` | 21.90 | 0.1 | 69.0 | 3.2 | +0.029 ± 0.006 |
| `te5_t_dr_900` | 21.90 | 0.1 | 69.0 | 3.3 | +0.029 ± 0.006 |
| `te1_teo480_tdr900` | 21.90 | 0.1 | 68.9 | 3.3 | +0.030 ± 0.006 |
| `te3_bk23_tdr2700` | 21.90 | 0.1 | 68.9 | 3.3 | +0.030 ± 0.005 |
| `te1_teo960_tdr2100` | 21.90 | 0.1 | 68.7 | 3.3 | +0.031 ± 0.007 |
| `te1_teo720_tdr1500` | 21.90 | 0.1 | 68.7 | 3.3 | +0.031 ± 0.005 |
| `te1_teo480_tdr3000` | 21.90 | 0.1 | 68.8 | 3.3 | +0.033 ± 0.005 |
| `te5_rzp_per_eo_2` | 21.90 | 0.1 | 68.8 | 3.4 | +0.033 ± 0.006 |
| `te4_reserve600` | 21.90 | 0.1 | 68.8 | 3.4 | +0.034 ± 0.004 |
| `te2_eagerfin99_r99` | 21.91 | 0.1 | 68.7 | 3.3 | +0.038 ± 0.007 |
| `te1_teo720_tdr2700` | 21.91 | 0.1 | 68.2 | 3.3 | +0.038 ± 0.007 |
| `te5_fin_min_p_0` | 21.91 | 0.1 | 67.6 | 3.5 | +0.039 ± 0.008 |
| `te3_bk23_tdr3000` | 21.91 | 0.1 | 68.4 | 3.2 | +0.040 ± 0.005 |
| `te1_teo720_tdr1200` | 21.91 | 0.1 | 68.3 | 3.2 | +0.044 ± 0.006 |
| `te5_fin_max_5` | 21.91 | 0.1 | 67.9 | 3.4 | +0.044 ± 0.004 |
| `te5_read_max_10p5` | 21.91 | 0.1 | 68.6 | 3.3 | +0.045 ± 0.009 |
| `te1_teo960_tdr2400` | 21.91 | 0.1 | 67.9 | 3.3 | +0.045 ± 0.007 |
| `te1_teo960_tdr1800` | 21.92 | 0.1 | 67.9 | 3.2 | +0.050 ± 0.006 |
| `te3_bk23_tdr3150` | 21.92 | 0.1 | 67.6 | 3.2 | +0.052 ± 0.005 |
| `te1_teo720_tdr900` | 21.93 | 0.1 | 67.8 | 3.2 | +0.058 ± 0.007 |
| `te5_switch_pen_1` | 21.93 | 0.1 | 68.0 | 3.0 | +0.062 ± 0.009 |
| `te5_htr_per_dr_8` | 21.93 | 0.1 | 67.0 | 3.5 | +0.065 ± 0.009 |
| `te1_teo960_tdr1500` | 21.94 | 0.1 | 67.1 | 3.2 | +0.073 ± 0.007 |
| `te5_eo_cap_120` | 21.95 | 0.1 | 67.0 | 3.1 | +0.076 ± 0.007 |
| `te5_fin_min_p_0p1` | 21.95 | 0.1 | 67.5 | 2.9 | +0.077 ± 0.007 |
| `te5_read_max_9` | 21.94 | 0.2 | 66.4 | 3.5 | +0.080 ± 0.014 |
| `te5_htr_per_dr_2` | 21.96 | 0.1 | 67.0 | 3.0 | +0.088 ± 0.010 |
| `te1_teo720_tdr3000` | 21.96 | 0.1 | 66.6 | 2.9 | +0.089 ± 0.008 |
| `te4_bankfirst_rr240` | 21.96 | 0.1 | 67.6 | 3.4 | +0.089 ± 0.008 |
| `te1_teo960_tdr1200` | 21.96 | 0.1 | 66.5 | 3.1 | +0.089 ± 0.008 |
| `te5_read_max_11` | 21.96 | 0.1 | 66.8 | 3.1 | +0.096 ± 0.011 |
| `te1_teo960_tdr2700` | 21.96 | 0.1 | 66.0 | 3.1 | +0.100 ± 0.009 |
| `te5_fin_max_4` | 21.98 | 0.1 | 65.0 | 3.3 | +0.113 ± 0.007 |
| `te5_rzp_per_eo_long_0` | 21.98 | 0.1 | 65.4 | 3.1 | +0.113 ± 0.011 |
| `te5_rzp_per_eo_1` | 21.99 | 0.1 | 65.3 | 2.9 | +0.120 ± 0.011 |
| `te5_read_max_12` | 22.00 | 0.1 | 65.3 | 3.0 | +0.133 ± 0.011 |
| `te5_read_max_13` | 22.00 | 0.1 | 65.3 | 3.0 | +0.135 ± 0.011 |
| `te5_rzp_more_0` | 21.94 | 1.1 | 66.6 | 3.4 | +0.153 ± 0.013 |
| `te5_switch_pen_2` | 22.02 | 0.1 | 65.2 | 2.8 | +0.153 ± 0.012 |
| `te5_eo_niss_false` | 22.01 | 0.4 | 65.1 | 3.1 | +0.159 ± 0.013 |
| `te5_fin_min_p_0p2` | 22.05 | 0.1 | 62.8 | 2.6 | +0.181 ± 0.010 |
| `te5_htr_per_dr_1` | 22.08 | 0.1 | 62.7 | 2.6 | +0.211 ± 0.013 |
| `te5_read_max_8p5` | 22.02 | 0.9 | 63.3 | 3.2 | +0.217 ± 0.018 |
| `te1_teo960_tdr3000` | 22.08 | 0.2 | 61.8 | 2.7 | +0.221 ± 0.012 |
| `te5_fin_max_3` | 22.10 | 0.1 | 60.4 | 3.1 | +0.229 ± 0.010 |
| `base` | 21.99 | 1.9 | 64.8 | 3.0 | +0.263 ± 0.020 |
| `te4_reserve270` | 21.82 | 4.0 | 69.0 | 3.4 | +0.277 ± 0.024 |
| `te5_switch_pen_99` | 22.18 | 0.2 | 60.0 | 2.1 | +0.319 ± 0.016 |
| `te5_rzp_per_eo_0` | 22.24 | 0.1 | 55.9 | 2.1 | +0.377 ± 0.017 |
| `te4_bankfirst_rr180` | 22.26 | 0.1 | 58.7 | 2.9 | +0.390 ± 0.014 |
| `te5_dr_cap_10` | 21.90 | 4.8 | 65.3 | 3.4 | +0.414 ± 0.025 |
| `te5_fin_max_2` | 22.31 | 0.1 | 53.7 | 2.7 | +0.444 ± 0.013 |
| `te5_read_max_8` | 22.13 | 3.1 | 58.4 | 3.0 | +0.497 ± 0.025 |
| `te4_reserve240` | 21.81 | 8.2 | 66.2 | 3.2 | +0.606 ± 0.034 |
| `te5_reserve_240` | 21.81 | 8.2 | 66.2 | 3.2 | +0.606 ± 0.034 |
| `te4_bankfirst_rr150` | 22.55 | 0.1 | 49.6 | 2.4 | +0.682 ± 0.017 |
| `te5_fin_max_1` | 22.70 | 0.9 | 41.9 | 1.9 | +0.893 ± 0.020 |
| `te4_reserve210` | 21.80 | 17.1 | 60.4 | 3.1 | +1.317 ± 0.048 |
| `te4_reserve180` | 21.77 | 33.1 | 49.2 | 2.6 | +2.620 ± 0.061 |
| `te5_reserve_180` | 21.77 | 33.1 | 49.2 | 2.6 | +2.620 ± 0.061 |
| `te4_reserve150` | 21.77 | 56.4 | 32.3 | 1.7 | +4.535 ± 0.065 |

## Appendix B: how it was computed, and what checks it

**The program.** `research/attemptsim`, written in Rust. It reads judging-a-dr's exact optimal finish of every DR state (1.3 GB, proved in Lean in that study), htr-routes' checklist per subset, and the EO-to-DR tables. It plays one attempt per plan and scramble, with every random draw (misses, step times, the day's pace) fixed per scramble, so plans differ only by their decisions. Every solution the simulated solver writes is replayed on the cube, and a run fails if one doesn't solve its scramble; no run has failed.

**The runs.** All with the costs of section 4 (`research/costs.toml`), on uniformly random states written as scrambles (`research/data/scrambles_uniform.txt`):

- *Round 1* tried the five experiments around the baseline with the first costs. Two calibration rounds then tried spreads of the pace and of the form from attempt to attempt. A pace spread of 0.15 gives the top 5's DNF rate. A form spread adds DNFs and bad results but no sub-20s, so it stayed at 0. The costs did not change after that.
- *Round 2* (`policies/all.toml`, 237 plans) ran on 3,400 training scrambles and on held-out scrambles 4,000 to 7,999. The tuned plan's three changes were chosen on the training scrambles. Appendix A's first table is the held-out check.
- *Round 3* (`policies/t_all.toml`, the same experiments around the tuned plan) ran on scrambles 0 to 7,999. Every table of sections 1 and 6 to 10 uses only 4,000 to 7,999.
- *Round 4* (`policies/scale.toml`): the length of the attempt and the solver, 2,000 held-out scrambles each.
- *Sensitivity* (`policies/conclusions.toml`, `src/sensitivity_jobs.sh`): section 11.
- *The official scrambles*: the scrambles of the top 10's official attempts since 2024, from the WCA export (`src/wca_top.py`).

Every table and number on the page comes out of `research/src/tables.py` from the result files and gets filled in by `report_build/assemble.py`. Nothing is typed by hand.

**The Lean certificate** (`lean/AttemptSim`, 56 theorems, no `sorry`) checks what the numbers rest on:

- the cube model, and that every table the simulator prunes and judges with is exact;
- that its candidate lists of EOs and DRs are complete on exported scrambles;
- that its DR moves are the ones of judging-a-dr's exact table;
- that a fixed sample of simulated attempts of the baseline and the tuned plan does what the log says: every solution solves its scramble in the stated length, the clock is the sum of the step costs, and the result is the shortest solution found before the last writing that ended in time.

Lean checks individual attempts, not the averages, which stay **sampled**.

## Docs referred to

- Yura Riabov, [*Hitchhiker's Guide to FMC*](https://docs.google.com/document/d/16nu10y1JkUmVDC11c1h_ULzAl4Vze7zR/edit) (Google Doc).
- Yura Riabov, [*FMC Jan-May 2025*](https://docs.google.com/spreadsheets/d/1Cb7M3KqB5W99sSNOIKLG3xqZ-k58koIexTLahUiPNhs/edit?usp=sharing), a log of 138 attempts (Google Sheet, posted [8 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1392205872595468319)).
- [*Sub 22 Official Mean Stats*](https://docs.google.com/spreadsheets/d/17L6vArP8t_5yPIeCpiQpp66YBZcLcbxS10hzYtnB-XE/edit?gid=0) (Google Sheet, first linked here by Yura Riabov, [26 May 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1244360346202931304)).
- The WCA results export, version 2.0.2 of 13 November 2026 ([worldcubeassociation.org/export/results](https://www.worldcubeassociation.org/export/results)): official FMC results of the top 10 by mean since 2024, and their scrambles. This information is based on competition results owned and maintained by the World Cube Association, published at https://worldcubeassociation.org/results as of November 13, 2026.
- The other studies on this site: [*Judging a DR by hand*](../judging-a-dr/), [*Which HTR routes to try from a DR*](../htr-routes/), [*EO to DR, and scramble to DR*](../eo-to-dr/), [*When to switch an EO*](../eo-switch/).
