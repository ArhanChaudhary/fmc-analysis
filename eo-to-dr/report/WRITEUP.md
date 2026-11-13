# EO to DR, and scramble to DR

How far a random scramble is from DR: on one axis, on the best of three, with the inverse, with NISS, and through the short EOs a solver actually writes down. How many EOs a scramble has and how short. And what an EO leaves: how far DR is with the other DR axis, the inverse, the EO's last turn the other way and EO-breaking turns, case by case. Every distance is exact (from full distance tables). Where a number is a sample it says so: 50,000 uniformly random scrambles for the scramble-level questions, 1,000,000 random states for the shortest EOs, and 10,000,000 EO-solved states for the EO to DR options that need the inverse.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion). Docs and sheets are listed with links at the end.

**This builds on** what the server already had:

- **Cale's [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0)** (posted by Aneurin, [5 Oct 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1027339996308443176): "This has a bunch of useful stats for dr"), the per-case EO to DR table everyone uses: every EO-solved state on one DR axis, "I used the moveset <U, D, R, L, F2, B2>, so sequences that break EO like F R B2 R' F' aren't considered", average 7.80, with a tab per case. Cale's second sheet does the same "if you can change the direction of the last move(s) of EO" ([*DR setup stats (switching last move of EO)*](https://docs.google.com/spreadsheets/d/1_2PmFv1KyBX335SjSb4oweS0sx804fIhbuP50D-gBj4), made at Tom Nelson's request, [5 Jun 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1115138822192234527), [9 Jun 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1116937004282822726)).
- **Louis's [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs)**: "I've generated every possible EO->DR case of increasing lengths" and sorted them by DRM and ARM ([27 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1222749709039435839)); its last tab is the EO to DR distribution. **Rodney Kinney**'s *DRM corner variant+pair stats* is built on it ([13 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383068446736257125): "and I did some work on the DRM/ARM stats and came up with something cool."). Separately: **KrzychXyz**'s sheet of every case sorted by DRM ("all DR cases (from EO) grouped by subsets, sorted by optimal", [8 Jun 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1249110563011825778)), and **Evan**'s [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk) tables ("this stat is in my arm/pairs sheet", [11 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404504939190812763)).
- **FakeMMAP**'s counts of the same 1,082,565 states, "not allowing EO-breaking moves" ([16 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1141304202065367170)), and **torchlight**'s table that "allows breaking EO" ([16 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1141354103138693243)): EO-breaking turns change almost nothing. DougCube confirmed the counts two years later: "that matches the table I just generated:" ([15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417261933916196945)).
- **DougCube's [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo)** (posted [2 Mar 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1345852930544369684)): fixed-axis EO (mean 4.609), DR from a scramble on one fixed axis ("Going to DR", mean 9.5245, at most 12), and, added after August 2025, "NISS-EO on any axis. Credit: Joba". **Joba** computed that NISS EO table over all $12!\cdot 2^{11}$ edge states: "On average, eo can be solved in 3.455 moves." ([27 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1410262132783714485)).
- **Shota**'s table of the shortest linear EO against the number of bad edges ([11 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1283314529916420116): "here's a table that also takes into account the optimal move counts") and Shota's [*Full EO*](https://docs.google.com/spreadsheets/d/1K38k5BQUV5PQh4ZmeJGNfrRZbnuhVePp4CLqyCIelm4) sheet of every one-axis EO case (linked by KrzychXyz on [27 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1410290372118319134)).
- **Sebastiano Tronto**'s EO-solved scrambles, about 250 ("like 250") ([9 Apr 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1227179797512192033), [9 Apr 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1227180109698433074)), with optimal solutions with and without EO-breaking moves: "optimal average: 16.64" against "eofbfin average: 16.70" ([9 Apr 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1227181234061447240)). That's EO to solved, not EO to DR, but it's the only earlier measurement of what keeping the EO costs over the whole solve.
- **The server's own counts**: Louis's "Only 6.2% of axes are 8 moves or less away from DR if you don't allow NISS" ([9 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1326956621435506808)); torchlight's exact bad-edge counts on the three axes ([25 Sep 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1155803699025813594), [12 Oct 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1162060161507151983)); wen's "200ish <=5 movers and 17 <=4 movers" from memory ([12 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1250363326324543500)); Cale's sheet of EO counts on official scrambles, with about 4% having no EO of at most 4 ([13 Jul 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1128898843254194188); wen, [6 Aug 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1270547867097890827)); Rodney Kinney's 1,000 optimal EO to DR solutions (*Multi-Axis DR*, [18 Dec 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1186454920828825711)).
- **Tools**: DR Finder 2 (sanya.sweetduet.info), which Daichi pointed to for DRs from a scramble ([9 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1547200826983063552)), and nissy.
- **My own DR-xs study**, section 6.4: the best of six linear DR (3 axes, normal or inverse) on 2,000,000 scrambles. The numbers here agree with it (appendix B).

**What this adds**:

- **Scramble to DR over all axes, with NISS and through short EOs**, with the odds of 8, 9, 10 and 11, and the scrambles that have no sub-10 DR at all. One fixed axis (DougCube, Louis) and the best of six (my DR-xs study) were known; the best of three on each side, NISS, and the scrambles without a sub-10 DR were not (wen asked, [9 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1547198328792420393)).
- **How the optimal DR relates to the EOs people write**: the shortest EO inside the optimal DR, and the best DR through an EO of at most 3, 4, 5 or 6 turns, normal, inverse and NISS, as odds of a DR in 8 to 12.
- **How many DRs a scramble has** through its short EOs, and what 4-move against 5-move EOs and the other EO axes are worth.
- **EO counts and shortest EOs per scramble** on all three axes, linear and with the inverse (with NISS, Joba's table had the shortest EO), and the bad-edge layouts exactly, with the odds of a short EO by bad-edge count with the inverse and with NISS.
- **EO to DR with every option a solver has**: the other DR axis (exact), the inverse, the EO's last turn either way, and all together, overall and by case; and how the normal and inverse sides are related.
- **The claims, checked**, and **a finding about nissy 2.0.8's `scramble`**: a modulo bias in its edge permutation, which makes DRs on the inverse of its scrambles shorter (appendix B).

**Terms**, as the server uses them:

- *EO* on an axis: all edges good for that axis. *DR*: corners oriented and the slice edges in their slice for one axis.
- *Normal* is turns after the scramble, *inverse* turns after the inverse scramble (written in brackets), *NISS* turns on both sides, the length being the sum. A *linear* DR or EO is on one side only. *Best of six*: the shortest DR over the three axes on normal and on inverse.
- An EO of length L is a sequence that solves EO for the first time at its last turn (nissy's `-a` convention; both directions of the last turn count). A *route through an EO*: the EO, then turns that keep it (no quarter turns of its axis) to DR on one of the two other axes.
- A case like *4c4e*: bad corners, then edges out of place for DR on that axis (slice edges outside the slice and as many other edges inside it). Cale's sheet writes it edges first (4e4c), and Louis's ARM tables use the same counts.
- *In 10* means in 10 turns or fewer. Turns are face turns (HTM).

**How to read it.**

- **Start with [section 1](#1-the-short-version)**, the short version: what is new, then what it confirms or corrects, one line each.
- **The [worked examples](examples.html)** go with it: 150 scrambles with their shortest DRs and their best DRs through EOs of at most 4 and 5, then 60 EO-solved states by case, answers folded away. **The [errata](errata.html)** list what the numbers show is wrong in things said on the server, each with an example.
- **The appendices are reference**: every case, normal against inverse by case, every bad-edge triple, and how it was computed and checked (with nissy's scrambler).
- **✓ after a number: proved in Lean**, counted on a Lean model of the cube, not only computed. [Appendix B](#appendix-b-how-it-was-computed-and-what-checks-it) lists what is proved and what is only computed.
- **What you can use in an attempt, and what's the answer key.** Most numbers here are what exists, found by exact search: the optimal DR from a scramble, the best DR after every EO of a given length, counts of hundreds of EOs per scramble. Those are **computer only**: they say what's there, not something to do in an attempt, and each place says so. What you can use at the table is what you can see or count: the bad edges on each axis and the odds of a short EO from them (4.2), the case an EO leaves on each DR axis and its odds with each option (5.2), and which options after an EO are worth checking (5.1).

---

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | What is new, then what it confirms or corrects, one line each. |
| [2. What was asked](#2-what-was-asked) | The questions, quoted, with where each is answered. |
| [3. Scramble to DR](#3-scramble-to-dr) | The shortest DR on 1, 3 and 6 tries and with NISS; the EO inside the optimal DR; routes through short EOs; how many DRs. |
| [4. Scramble to EO](#4-scramble-to-eo) | How many EOs and how short, linear, inverse and NISS; bad edges on the three axes; EO odds by bad edges. |
| [5. EO to DR](#5-eo-to-dr) | The other DR axis, the inverse, the last EO turn, EO-breaking turns: overall and by case; normal against inverse. |
| [6. The claims, checked](#6-the-claims-checked) | Each checkable statement from the server, with the verdict, and the examples. |
| [7. What this does not cover](#7-what-this-does-not-cover) | Limits. |
| [Appendix A: full tables](#appendix-a-full-tables) | Every case, normal against inverse by case, every bad-edge triple. |
| [Appendix B: how it was computed, and what checks it](#appendix-b-how-it-was-computed-and-what-checks-it) | Model, scrambles (and nissy's scrambler), checks, Lean. |
| [Docs referred to](#docs-referred-to) | Links. |

---

## 1. The short version

New stuff first, then what the numbers confirm or correct. Scramble-level lines are on 50,000 uniformly random scrambles (a share has a standard error of at most 0.2 points); EO counts by length use 1,000,000 random states where they say so; EO to DR lines are exact unless they say sampled (10,000,000 states).

**What is new here**

**How often there's a short DR from the scramble** (optimal DR, 3.1). Each row is what you allow; the middle columns are the share of scrambles with a DR that short:

| Allowed | DR in ≤ 9 | DR in ≤ 8 | Mean, turns |
|---|---|---|---|
| One fixed axis | 43.3% | 6.2% | 9.52 |
| Linear, one side (3 axes) | 76.5% | 16.5% | 9.05 |
| Best of six | 91.5% | 28.4% | 8.76 |
| NISS | 99.1% | 47.5% | 8.46 |

NISS beats the best of six linear tries on 27.0% of scrambles. The best of six was already in my DR-xs study; the rest is new. **Computer only**: these are optimal DRs over every axis and side, the answer key for what's there, not a length you can check for in an attempt. By hand you get to DR through an EO, and that's what the lines below and 5.2 are about.

- **Sub-10 isn't universal.** 8.5% of scrambles have no DR under 10 on any of the six tries, and 0.87% have none even with NISS; none in the sample needs more than 10 with NISS. The superflip is one of these but not the only one, and they aren't 20-movers: the first three such scrambles of the sample are 18, 19 and 18 moves optimal [a].
- **The optimal DR usually starts with a long EO.** Its shortest EO (over every optimal DR of the scramble, normal side) is at most 4 turns on 22.1% of scrambles, at most 5 on 41.1%, and 7 or more on 37.2% (3.2) [c].
- **EO-breaking turns hardly ever help.** Among routes through an EO of at most 5, a continuation with any turns reaches the optimal DR where no EO-keeping one does on 4 of 50,000 scrambles (9 for EOs of at most 4, 3 for at most 6). **Computer only**, the answer key. What it means in an attempt: the optimal DR usually isn't behind any EO you write, so judge your DR against the route numbers below, not against the optimum.

**Through the EOs people write down** (each EO with its best EO-keeping DR on either DR axis; a NISS EO takes the DR on the better side; 3.2). Each row is a set of EOs; the columns are the share of scrambles where one of them leads to a DR that short:

| EOs | DR in ≤ 10 | DR in ≤ 11 |
|---|---|---|
| Every EO of at most 5 turns, normal, inverse and NISS | 97.7% | >99.9% |
| Normal EOs only | 77.7% | 97.3% |
| EOs of at most 4 of every kind | 82.3% | 95.0% |

A route in 9 or better exists on 64.6% of scrambles. **Computer only**: that's every EO of at most 5 (646.4 per scramble on average with NISS, 203.2 normal only), each with its best DR on both axes, which nobody writes out and solves in an hour. It says what's there to find. By hand, read the case each EO leaves on both DR axes and keep the EOs whose case has good odds (5.2).

**"Would you rather have 25 4 move eos or 200 5 move eos"** (Somebodyidk, [5 Jan 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1457758593762857091)). On average (3.3), the number of DRs that short you'd get from each pile of EOs:

| EOs | DRs in ≤ 10 | DRs in ≤ 11 |
|---|---|---|
| 25 EOs of at most 4 | 4.0 | 17.3 |
| 200 EOs of exactly 5 | 3.5 | 23.7 |

So the 25 win for a DR in 10 and the 200 for a DR in 11: a 5-move EO gives about a tenth as many DRs in 10 as an EO of at most 4. The counts are of DRs that exist after each EO (its best DR on both axes), **computer only**; what carries to an attempt is the ratio, one 4-mover worth about ten 5-movers for a DR in 10. Here the two directions of a last turn are two EOs; counted the server's way, one EO for both, each EO of a pile stands for about two of these, both piles give about twice as many DRs, and the answer is the same.

**EO to DR with every option is 7, not 8** (5.1). Two DR axes, normal or inverse, and the EO's last turn either way, all keeping the EO. Each row is what you check after the EO; the columns are the mean turns to DR and how often it's short:

| Options checked | Mean, turns | DR in ≤ 6 | DR in ≤ 6, odds | DR in ≤ 7 |
|---|---|---|---|---|
| Every option | 6.898 | 25.7% | 1 in 3.89 | 79.6% |
| One axis alone | 7.803 ✓ | 5.9% | 1 in 16.89 ✓ | 30.6% |

(The every-option row is sampled.) The lengths are optimal DRs after the EO, the answer key. What you use in an attempt is the list of options to check after each EO, and the case on each DR axis, which you can read at the table and which gives the odds of each (5.2).

- **The other DR axis of the same EO is worth more than switching the EO's last turn**: exact, at most 6 on 11.3% against 9.5% ✓, and about as much as checking the inverse (11.2%). DanielEgdal set out to compute the two-axis numbers in 2023 and thought it "pretty much infeasible with any current idea I have" ([27 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1156572910304112743)). FakeMMAP showed the state space is about $5\cdot 10^9$ ([27 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1156574602508644474)), and DanielEgdal ran it until it stalled at $3\cdot 10^8$ ([27 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1156656635566104657)). They're exact here (5.1).
- **Normal and inverse after an EO are related almost only through the case.** The DR lengths on the two sides correlate 0.1684 over all states, and at most 0.063 within a case. Once you know the case, the inverse is nearly a fresh draw (5.2).

**EO counts per scramble** (all three axes, counted the way nissy's `-a` lists them; nissy's default listing, the way counts are quoted on the server, keeps about two fifths of them; 4.1). Each row is the kind of EO counted; the last two columns are the share of scrambles with none that short:

| EOs counted | EOs of ≤ 4, mean | EOs of ≤ 4, median | Scrambles with no EO of ≤ 4 | Scrambles with no EO of ≤ 5 |
|---|---|---|---|---|
| Normal | 15.3 | 12 | 21.5% | 0.48% |
| With inverse and NISS EOs | 43.9 | 36 | 4.0% | 0.012% [d] |

**Shortest EO over three axes without NISS** (sampled, 1,000,000 states; 4.1). Each row is a side rule; the last column is the share of states with an EO that short:

| EOs allowed | Mean, turns | EO in ≤ 3 |
|---|---|---|
| Linear | 3.881 | 29.3% |
| Normal or inverse | 3.601 | 43.6% |

**Bad edges you can count at the table** (so these are for the attempt; 4.2):

- **8 bad beats 6 for a short linear EO**: an EO in 4 or fewer on 28.9% ✓ against 22.5% ✓. With NISS 6 bad is a little better, 63.3% against 61.4%.
- **12 bad beats 10 with NISS**: in 5 or fewer on 85.8% against 79.5%.

**nissy 2.0.8's `scramble` isn't uniform, and DRs on the inverse of its scrambles come out shorter.** Its source draws the edge permutation as

```
ep = rand() % FACTORIAL12;  // the edge permutation of the drawn state
```

rand() gives 4.48 ✓ times $12!$ values, so the lowest 48.3% ✓ of edge-permutation indices come up 25% ✓ more often than the rest. The inverse side is where the drawn state is, and that's where it shows, on 50,000 of its scrambles. Each row is one measure, on nissy's scrambles and on uniform ones:

| Measure | nissy's scrambles | Uniform states |
|---|---|---|
| Inverse, mean to DR (best of 3 axes) | 8.87 | 9.05 |
| Normal, the same (barely moved) | 9.02 | 9.05 |
| Best of six at most 8 | 34.8% | 28.4% |

The twisted-corner counts are off too ($\chi^2$ 33.2 and 34.9 on 7 degrees of freedom, p = $2\cdot 10^{-5}$ and $1\cdot 10^{-5}$); I haven't found the cause. This study draws its own uniform states (appendix B).

**What it confirms or corrects**

**The known tables reproduce exactly.** Each row is an earlier table or count, the number it gave where it gave one, and the number here:

| Table | Their number | Here |
|---|---|---|
| Cale's and FakeMMAP's 1,082,565 EO-solved states | | mean 7.803 ✓ |
| torchlight's EO-breaking version (EO-breaking turns change almost nothing, as torchlight's table showed in 2023) | | 7.797 |
| DougCube's one-axis DR from a scramble | | 9.52 |
| DougCube's one-axis EO | | 4.609 ✓ |
| Shota's shortest linear EO by bad-edge count | | the same table ✓ |
| Louis's one-axis DR shares | 6.2% and 43% | the same |
| Joba's exact NISS EO mean | 3.455 | 3.455 on 1,000,000 states, within sampling error |
| No EO of at most 4 even with NISS, on official scrambles: Cale ([13 Jul 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1128898843254194188)) and wen ([6 Aug 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1270547867097890827)) | about 4% | 4.0%, within sampling error |

- **The DR-4c4e numbers Tom Nelson quoted** ("1 in 5.2 normally, but 1 in 3.6 if you can switch the last move", [13 Jul 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1128948555684519946)) are exact for EO-solved states: 1 in 5.2 ✓ and 1 in 3.6 ✓ for a DR in 6 or fewer. At that rate Lichi Fang's 3 of 27 has probability 3.3% ✓ (4.0% at Cale's rate for switching the RZP's last move, which is what Lichi Fang switched), and Cale's 25 fit it. Both samples are the first 4c4e nissy online found, which needn't be like a 4c4e straight off an EO. Open (section 6).
- **Corrected:**
  - KrzychXyz's "~3%" of EO to DR cases at 10 is 0.29% ✓ (3,114 ✓ of 1,082,565 states; "10 is the worst" is right) [h].
  - Aneurin's later "Superflip takes 6 moves to solve EO with NISS": it takes 7 ✓, as Aneurin had first said [b].
  - Jay's "Similar efficiency to 4c4e and 4c2e in theory" for 6e4c (Jay's advice in the same breath was not to NISS for it): one axis, at most 6 on 4.6% ✓ against 19.2% ✓, as Cale's sheet had it and Cale told Jay in 2023 [j].
- **True as said**: the bad-edge facts (torchlight's exact counts, 6/6/4 and 6/6/8 above 6/6/6, no two axes more than 8 apart, at least 4 elsewhere when one axis has 12, 0 to 8 bad on the other axes after an EO), the EO odds for 10 and 12 bad edges, Emma's corner-twist odds, Zagros's 1 in 11 for 6+0, Cale's 1 in 22 for 4c6e, Zagros's 10% against 16% for 3c4e and 7c8e, wen's and Lichi Fang's EO counts per scramble (as Cale's sheet of official scrambles counts them), Jay's, Tom Nelson's and Rodney Kinney's take on normal against inverse once the case is known, and the rest of the claims table (section 6).

---

## 2. What was asked

The questions, in the words of the people who asked them, grouped as the sections that answer them. Most got a pointer, a guess or no answer.

**Scramble to DR (section 3)**

- wen ([9 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1547198328792420393)): "Is the distribution for scrambled->DR movecount known? I'm curious to know if sub-10 DRs exist on most scrambles, be it findable or not". Daichi, who had pointed to the DR Finder 2 tool ([9 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1547200826983063552)), after trying it ([9 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1547201574919606364), [9 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1547201629789360158)): "trying a ton of scrambles, there seems to be a sub10 on a lot of scrambles", "probably every, idk". wen ([9 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1547202526749786114), [9 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1547202601836351488)): "well sub-10 is not possible for superflip", "But I wonder if that is the worst case for this problem or not". Daichi ([9 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1547204956195528714)): "could it be for all 20 optimal scrambles where a sub10 DR doesn't exist?" No answer followed. *Answer*: 3.1. Most scrambles have a sub-10 DR (91.5% best of six, 99.1% with NISS); not every one; the superflip is not the only exception; and the exceptions are not 20-movers [a].
- Michael Smith sub7 ([14 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1416938916497326081)): "In a random shuffle, what is the probability that there will be Dr in x moves? That is, first there is eo and then the dr." JTuu ([15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417227840964923413)): "if your question is "for a random state, what is the probability it has a N-move dr beginning with a sub-6-move eo?" then I don't think that's been analyzed". The thread then turned to EO to DR alone and DougCube's estimate for 300 EOs (section 6). *Answer*: 3.2, the table of odds through an EO of at most 3, 4 or 5.
- Zagros ([12 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1306109662948491376)): "what percent of those good DRs would have <6 move eo? I don't even have a clue here. Is it like 50% or it is <1%?" JTuu ([12 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1306113780165513227), [12 Nov 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1306113817146822707)): "I've checked this for optimals (not for drs) and it's very low. I'll publish stats soon", "I'm guessing it's also low for drs". *Answer*, per scramble rather than per DR: on 41.1% of scrambles some optimal DR starts with an EO of at most 5 (normal side, 3.2); on the other 58.9% every optimal DR needs an EO of 6 or more. The share among all DRs of a given length, which is what Zagros asked and JTuu guessed is low, isn't measured here.
- Zagros ([12 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1294866800336703540), [12 Oct 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1294866963444531313)): "does anyone have stats on scrambled to dr without an eo/rzp step?", "Are the best DRs typically the findable ones, or is it usually like random 8 move dr from 7 move eo". No reply. *Answer*: 3.1 and 3.2 (the optimal DR's EO is 6 or more on 58.9% of scrambles [c]). Findability is not measured here.
- Aneurin ([12 Apr 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1095654217387085836)): "Could be interesting to see some stats genned in relation to number of EOs. And how that affects the RZPs and DRs you can find." Chris Choi ([25 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1255237793911804008)): "Roughly how many DRs should I expect to check for N amount of EOs". Noah Swor ([25 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1255238074258948107)): "lame answer is 'impossible to know'". *Answer*: 3.3, the DRs that exist per EO; how many a solver finds is not measured.
- Somebodyidk ([5 Jan 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1457758593762857091), a message forwarded from #fmc-theory): "Would you rather have 25 4 move eos or 200 5 move eos (ignoring time to write all of those eos)". No reply in the export. *Answer*: 3.3.

**Scramble to EO (section 4)**

- argonblue ([6 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1458219456693276692)): "how rare are 3-move EOs? i seem to find more of them than i would expect". wen ([2 Mar 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1213499066034425926)): "what is the probability of a 3 move NISS EO? (all 3 forms included)", meaning ([2 Mar 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1213650297575047238)) "Like F (F B), F (U F) and F (U2 F)". *Answer*: an EO of at most 3 on some axis: 29.3% of scrambles linearly, 43.6% on normal or inverse, 49.6% with NISS (4.1). Joba's exact table had the NISS figure already ([27 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1410262132783714485)). The share with a 3-move NISS EO of wen's 1+2 forms alone is not broken out here.
- Radek B ([15 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1516080351338827797)): "how to compute the exact distribution of the number of sub5 eos (including niss ofc) so that we can model the odds for over/under 😆 ? Is it even doable?" No result was posted. *Answer*: the sampled distribution in 4.1 (mean, median and the share with none; exact for one axis linearly).
- Ben ([14 Jul 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1129479619804926103)): "how common is it to have an N move eo but no N+1 move eos on a scramble?" JTuu ([14 Jul 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1129515888681431111)): "I feel like maybe it can only happen when N=1 or N=2 (edit: or N=0 lol)". *Answer*: 4.1. Linearly only for N = 0, 1, 2 in the sample, as JTuu guessed (N = 0, an EO already solved on some axis and no 1-move EO: 82 of 50,000 scrambles, the same with NISS); with NISS also for N = 3, rarely.
- Enrico ([18 Feb 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1208788430386110534)): "what is the least amount of eos in 5 you had on a scramble?" Answers from experience: Dunni "I think 26" ([18 Feb 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1208789333138735114)), Yura Riabov "7 on cubers.io" ([19 Feb 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1209148916940021761)). *Answer*: 0 happens, even with NISS on all three axes, on 0.012% of scrambles [d].
- Radek B ([18 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1440311597678592101)): "For each n, lets say from 0 to 7, for a given axis what is the maximum number of <=n move eos?" FakeMMAP answered for n up to 2 ([18 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1440383022145998918)). *Answer*, linear, one axis, exact over its 2,048 states: at most 92 EOs of at most 4 turns and 476 of at most 5 (both directions of the last turn counted). The NISS maximum is not computed (the sample's largest is in 4.1).
- JTuu ([1 Feb 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1202701695713284106), [1 Feb 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1202750000619069440)): "do we have stats anywhere on relative frequency of various bad-edge configurations for eo?", "by stats I just mean the exact probabilities". Tom Nelson ([12 Apr 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1095903422382887042)): "what are the odds of all bad, like 1 in 100 trillion?" Aneurin ([12 Apr 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1095921292777103441)): "So 1 in 10 quadrillion might be closer". *Answer*: 4.2, exact; 12/12/12 is 1 in 70963200.
- Jay ([17 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1064854971411091526)): "it could be worth researching this same info for 2-8 bad to get an idea of how much worse 10 bad really is", after wen's estimate for 10 bad with independence assumed ([14 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1064043808620298322), [14 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1064044127337062401)). trig0n ([17 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1064897872782442578)): "What about ≤4-move EOs?" wen ([6 Jan 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1060871206464667728), [6 Jan 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1060871254015496262)): "What is the probability of a <5 move 8 bad?", "It doesnt feel like it’s better than that of 6 bad". *Answer*: 4.2, by bad-edge count, linear, normal or inverse, and NISS.

**EO to DR (section 5)**

- DanielEgdal ([21 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1154347811412914238)): "Anyone know if the stats in Cale's dr stat document accounts for the fact that you could do a z and then have a different DR case?" Tom Nelson ([21 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1154354743133618269)): "the stats are for a given axis". DanielEgdal wanted to compute it, and a week later ([27 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1156572910304112743)): "I wanted to do it yeah, but realised the computation is pretty much infeasible with any current idea I have". FakeMMAP then showed the state space shrinks to "~5*10^9" ([27 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1156574602508644474)); DanielEgdal: "oh this does seem true" ([27 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1156584745271050280)), and ran it: "my program got to 3*10^8 after 10 min, before everything starting to lag and stall" ([27 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1156656635566104657)). *Answer*: 5.1 and 5.2, exact.
- zakimoshi ([12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1415997351633621022)): "What's the longest DR case after eo". KrzychXyz pointed to the last tab of Louis's *DRM/ARM average optimals* (see the [errata](errata.html)), and zakimoshi asked ([12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1416001772345884712)): "Wait so only 6.3% of all cases are sub 7able?" Yura Riabov ([12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1416001888121520219)): "Sounds about right". *Answer*: 5.1. 10 is the longest; a DR in 6 or fewer is 5.9% ✓ (one axis, EO kept), 9.5% ✓ with the EO's last turn either way.
- DanielEgdal ([1 Jan 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1191520771957338163)): "I'm thinking about taking every DR equivalent state and mapping it to inverse and taking the minimum movecount of the two". zakimoshi ([12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1416002099480625245)), of Louis's table: "Also doesn't include niss". *Answer*: 5.1. The inverse takes a DR in 6 or fewer from 5.9% to 11.2%.
- Yura Riabov ([12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1416001965229478052)), on the same table: "Does that include reverting the last move?"; zakimoshi ([12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1416002025887502367)): "No"; Yura Riabov ([12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1416008638639898665)), on how much it would change: "i'd guess by a couple of %". *Answer*: 5.1. The last EO turn either way takes a DR in 6 or fewer from 5.9% ✓ to 9.5% ✓, which fits the guess.
- Bhargav7777 ([24 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1078553751108988958)): "is it worth NISSing with all EOs -> RZP or will it be the same on both sides?" *Answer*, for EOs: 5.2. Not the same: within a case the two sides are unrelated.
- DougCube ([15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417257592325148794)): "there are EO-breaking DRs that Idk how to acct for." KrzychXyz ([15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417258791082135593)): "It doesn't include EO-breaking stuff and I've been meaning to check how much that changes for some time now, but I'm too lazy". *Answer*: 5.1. Hardly at all; torchlight's 2023 table already had it ([16 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1141354103138693243)).
- Zagros ([30 Jun 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1389269657126699138)): "What is typical eo->dr? I know the golden number we use for stats is sub-7 after rzp". *Answer*: 5.1, for EO-solved states; the states after an RZP are a different population (section 7).

What this leaves for later is in section 7.

---

## 3. Scramble to DR

Everything in this section is on 50,000 uniformly random scrambles (appendix B says how they're drawn and why I didn't use nissy's `scramble`), with exact distance tables for every lookup: each number for one scramble is exact, and the only uncertainty is the sample. On 50,000 scrambles a share has a standard error (one standard deviation of the estimate) of at most 0.2 points, and a mean about 0.003 turns. Any turns are allowed on the way to DR unless a line says the EO is kept. Turns are face turns (HTM).

**This whole section is computer only, the answer key.** Every number is what exists, from exact search: the optimal DR over every axis and side (3.1), or every EO of a given length with the best DR after it on both DR axes (3.2, 3.3). It says where the short DRs are, not what you find in an hour, and none of it is a check to run in an attempt. The versions you can use by hand are elsewhere: count the bad edges for the odds of a short EO (4.2), and read the case each EO leaves on both DR axes for the odds of a short DR (5.2).

### 3.1 The shortest DR

Each row is one way of reaching DR from the scramble; the *DR in ≤* columns are the share of scrambles with a DR that short.

| Shortest DR from the scramble | Exact or sampled | Mean, turns | DR in ≤ 8 | DR in ≤ 9 | DR in ≤ 10 | DR in ≤ 11 | Longest, turns |
|---|---:|---:|---:|---:|---:|---:|---:|
| One fixed axis, normal | exact, all 2,217,093,120 cosets | 9.52 | 6.2% | 43.3% | 97.4% | >99.9% | 12 |
| One fixed axis, normal (each of the 3 axes) | sampled, 150,000 axes | 9.53 | 6.2% | 43.1% | 97.4% | 100.0% | 11 |
| Best of 3 axes, normal | sampled, 50,000 | 9.05 | 16.5% | 76.5% | >99.9% | 100.0% | 11 |
| Best of 3 axes, inverse | sampled, 50,000 | 9.05 | 16.6% | 76.9% | >99.9% | 100.0% | 11 |
| Best of 6: 3 axes, normal or inverse | sampled, 50,000 | 8.76 | 28.4% | 91.5% | 100.0% | 100.0% | 10 |
| NISS: 3 axes, moves on both sides | sampled, 50,000 | 8.46 | 47.5% | 99.1% | 100.0% | 100.0% | 10 |

*One fixed axis* is DR on one given axis with turns after the scramble only, exact over every coset; it is DougCube's table (the "Going to DR" tab of [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo)) and Louis's 6.2% and 43% ([9 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1326953435177680938), [9 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1326954809827262576), restated for one axis, linear, on [9 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1326956179103940748)). *Best of 3 axes, normal*: the fewest turns to DR on any axis, turns after the scramble only. *Inverse*: the same on the inverse scramble. *Best of 6*: the better of those two, the six tries of 3 axes on each side. *NISS*: turns on both sides, counted together, best of 3 axes.

What it says:

**Three axes are worth 0.47 turns, the inverse another 0.29, NISS another 0.30.** Each row adds one option to the row above; the *DR in ≤* columns are the share of scrambles:

| Allowed | Mean, turns | DR in ≤ 10 | DR in ≤ 9 | DR in ≤ 8 |
|---|---|---|---|---|
| One axis | 9.52 | 97.4% | 43.3% | 6.2% |
| Best of three, one side (linear) | 9.05 | >99.9% | 76.5% | 16.5% |
| Best of six (with the inverse) | 8.76 | every scramble in the sample | 91.5% | 28.4% |
| NISS | 8.46 | every scramble in the sample | 99.1% | 47.5% |

- **Normal and inverse are the same thing statistically** (9.05 and 9.05), but on a given scramble they often differ: the inverse is shorter on 25.5% of scrambles and longer on 25.2%.
- **NISS beats the best of six linear tries on 27.0% of scrambles**: by one turn on 24.2%, by two on 2.7%, by three on 0.12%.
- **No sub-10 DR at all.** 8.5% of scrambles have no DR under 10 on any axis, normal or inverse, and 0.87% (437 of 50,000) have none even with NISS. None in the sample needs more than 10 with NISS, or more than 10 best of six [a].
- **The longest linear DR** seen on one side is 11 (on 12 scrambles).
- **The superflip** is one of the scrambles with no sub-10 DR, and not a special one: 10 on every axis, normal and inverse, and 10 with NISS [b].

How many DR solutions a scramble has, normal side, all three axes (each canonical move sequence that reaches DR for the first time at its last turn counts once, as `nissy solve dr -a` lists them; a solution and the same with its last turn the other way count as two). Each row is a DR length:

| DR length, turns | DR solutions per scramble, mean | Median | Scrambles with at least one | Most on one scramble |
|---|---:|---:|---:|---:|
| 6 | 0.004 | 0 | 0.13% | 12 |
| 7 | 0.061 | 0 | 1.8% | 56 |
| 8 | 0.821 | 0 | 16.3% | 448 |
| 9 | 11.0 | 4 | 76.3% | 3,568 |
| 10 | 147.4 | 82 | >99.9% | 30,106 |
| 11 | 1,968.2 | 1,322 | 100.0% | 247,220 |
| 12 | 26,271.0 | 19,707 | 100.0% | 2,071,460 |

So the median scramble has 4 DRs of 9 on the normal side and 82 of 10. Its optimal DRs, of whatever length that is, number 15.4 on average (median 6); on 27.5% of scrambles there is just one, counted twice for the direction of its last turn.

### 3.2 The optimal DR against DRs through a short EO

A human DR goes through an EO: an EO, then turns that keep it, to DR on one of the two other axes. Any DR solution contains an EO in that sense: cut it after its last quarter turn of an axis that is not the DR axis, and what comes before is an EO on that axis (Joba said the same of DR solutions in general, [15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417015142771724410)). So the question is how long that EO is.

The shortest EO inside an optimal normal DR, over all optimal DRs of the scramble and both EO axes, normal side, 50,000 scrambles. Each column is an EO length in turns; the cell is the share of scrambles whose shortest such EO has that length:

| Shortest EO inside an optimal DR (turns) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | Mean, turns |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Share of scrambles | 0.16% | 0.26% | 2.0% | 6.5% | 13.2% | 19.0% | 21.7% | 22.7% | 14.3% | 0.14% | 5.77 |

The optimal DR starts with an EO of at most 5 turns on 41.1% of scrambles, at most 4 on 22.1%. On 58.9% it needs 6 or more, and on 37.2% 7 or more [c]. So most optimal DRs are out of reach of the EOs people write down: their EO is too long. (Every DR solution starts with an EO in this sense, so the optimum never needs EO-breaking turns.)

What EO-breaking turns add to a short EO: among routes through EOs of at most 5, a continuation with any turns reaches the optimal DR where no EO-keeping one does on 4 of 50,000 scrambles (9 for EOs of at most 4, 3 for at most 6).

What the best route through a short EO gives, against the optimal (normal EOs for the optimal normal DR; normal or inverse EOs for the best of six; all EOs, normal, inverse and NISS, for the NISS optimum and for the best of six; a NISS EO takes its DR on the better of the two sides). Each row is a kind of EO and a maximum EO length; the cells are shares of all scrambles:

| EOs used | Compared with | EO length, turns | Scrambles with such an EO | Best route as short as the optimal | Best route shorter than the optimal |
|---|---:|---:|---:|---:|---:|
| normal | optimal normal DR (3 axes) | ≤ 3 | 29.3% | 8.9% | 0% |
| normal | optimal normal DR (3 axes) | ≤ 4 | 78.5% | 22.1% | 0% |
| normal | optimal normal DR (3 axes) | ≤ 5 | 99.5% | 41.1% | 0% |
| normal | optimal normal DR (3 axes) | ≤ 6 | 100.0% | 62.8% | 0% |
| normal or inverse, DR on that side | optimal DR, best of 6 | ≤ 3 | 43.3% | 11.7% | 0% |
| normal or inverse, DR on that side | optimal DR, best of 6 | ≤ 4 | 88.3% | 26.0% | 0% |
| normal or inverse, DR on that side | optimal DR, best of 6 | ≤ 5 | 99.9% | 45.6% | 0% |
| normal or inverse, DR on that side | optimal DR, best of 6 | ≤ 6 | 100.0% | 67.8% | 0% |
| normal, inverse or NISS | optimal NISS DR | ≤ 3 | 49.6% | 9.3% | 0% |
| normal, inverse or NISS | optimal NISS DR | ≤ 4 | 96.0% | 23.2% | 0% |
| normal, inverse or NISS | optimal NISS DR | ≤ 5 | >99.9% | 43.1% | 0% |
| normal, inverse or NISS | optimal NISS DR | ≤ 6 | 100.0% | 66.1% | 0% |
| normal, inverse or NISS | optimal DR, best of 6 | ≤ 3 | 49.6% | 14.2% | 0.78% |
| normal, inverse or NISS | optimal DR, best of 6 | ≤ 4 | 96.0% | 33.0% | 2.5% |
| normal, inverse or NISS | optimal DR, best of 6 | ≤ 5 | >99.9% | 53.9% | 5.8% |
| normal, inverse or NISS | optimal DR, best of 6 | ≤ 6 | 100.0% | 70.1% | 11.2% |

The same rows, by how many turns the best route loses to the optimal (shares of all scrambles; the mean is over the scrambles that have such an EO):

| EOs used | Compared with | EO length, turns | Best route 1 turn longer | 2 turns longer | 3 or more turns longer | Mean extra turns (where there is an EO) |
|---|---:|---:|---:|---:|---:|---:|
| normal | optimal normal DR (3 axes) | ≤ 3 | 12.4% | 6.6% | 1.3% | 1.02 |
| normal | optimal normal DR (3 axes) | ≤ 4 | 32.3% | 19.6% | 4.5% | 1.09 |
| normal | optimal normal DR (3 axes) | ≤ 5 | 41.5% | 15.1% | 1.9% | 0.78 |
| normal | optimal normal DR (3 axes) | ≤ 6 | 32.4% | 4.7% | 0.11% | 0.42 |
| normal or inverse, DR on that side | optimal DR, best of 6 | ≤ 3 | 18.3% | 10.9% | 2.5% | 1.10 |
| normal or inverse, DR on that side | optimal DR, best of 6 | ≤ 4 | 36.7% | 21.1% | 4.5% | 1.05 |
| normal or inverse, DR on that side | optimal DR, best of 6 | ≤ 5 | 41.5% | 11.9% | 1.0% | 0.68 |
| normal or inverse, DR on that side | optimal DR, best of 6 | ≤ 6 | 29.3% | 2.9% | 0.042% | 0.35 |
| normal, inverse or NISS | optimal NISS DR | ≤ 3 | 19.9% | 16.0% | 4.4% | 1.32 |
| normal, inverse or NISS | optimal NISS DR | ≤ 4 | 41.8% | 26.0% | 5.0% | 1.14 |
| normal, inverse or NISS | optimal NISS DR | ≤ 5 | 44.8% | 11.4% | 0.68% | 0.70 |
| normal, inverse or NISS | optimal NISS DR | ≤ 6 | 30.7% | 3.1% | 0.044% | 0.37 |
| normal, inverse or NISS | optimal DR, best of 6 | ≤ 3 | 21.0% | 11.3% | 2.4% | 1.01 |
| normal, inverse or NISS | optimal DR, best of 6 | ≤ 4 | 40.5% | 17.4% | 2.6% | 0.84 |
| normal, inverse or NISS | optimal DR, best of 6 | ≤ 5 | 34.6% | 5.5% | 0.28% | 0.40 |
| normal, inverse or NISS | optimal DR, best of 6 | ≤ 6 | 17.8% | 1.0% | 0.0040% | 0.07 |

*Scrambles with such an EO*: the scramble has an EO of that length or shorter of that kind on some axis. *As short as the optimal*: the best EO, then EO-keeping turns, is as short as the optimal DR it is compared with. *Shorter than the optimal*: possible only when NISS EOs are compared with the linear best of six. *Mean extra turns* is over the scrambles that have such an EO.

The same as odds of a DR of a given length from the scramble, which is what a solver aims at. Each row is a route; the *DR in ≤* columns are the share of scrambles where it's that short:

| DR from the scramble | Exact or sampled | DR in ≤ 8 | DR in ≤ 9 | DR in ≤ 10 | DR in ≤ 11 | DR in ≤ 12 | Scrambles with no such EO | Mean turns (where there is one) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Optimal DR, best of 3 axes, normal | sampled, 50,000 | 16.5% | 76.5% | >99.9% | 100.0% | 100.0% | 0% | 9.05 |
| Optimal DR, best of 6 (normal or inverse) | sampled, 50,000 | 28.4% | 91.5% | 100.0% | 100.0% | 100.0% | 0% | 8.76 |
| Optimal DR with NISS | sampled, 50,000 | 47.5% | 99.1% | 100.0% | 100.0% | 100.0% | 0% | 8.46 |
| Through a normal EO of ≤ 3, DR on normal | sampled, 50,000 | 2.2% | 9.6% | 23.6% | 29.1% | 29.3% | 70.7% | 9.78 |
| Through a normal EO of ≤ 4, DR on normal | sampled, 50,000 | 4.2% | 19.9% | 53.0% | 74.9% | 78.5% | 21.5% | 10.05 |
| Through a normal EO of ≤ 5, DR on normal | sampled, 50,000 | 7.1% | 32.9% | 77.7% | 97.3% | 99.4% | 0.48% | 9.83 |
| Through a normal EO of ≤ 6, DR on normal | sampled, 50,000 | 11.0% | 47.4% | 92.4% | 99.9% | 100.0% | 0% | 9.47 |
| Through a normal or inverse EO of ≤ 3, DR on the same side | sampled, 50,000 | 4.2% | 17.2% | 37.1% | 43.2% | 43.3% | 56.7% | 9.63 |
| Through a normal or inverse EO of ≤ 4, DR on the same side | sampled, 50,000 | 7.8% | 32.8% | 69.1% | 86.0% | 88.2% | 11.7% | 9.77 |
| Through a normal or inverse EO of ≤ 5, DR on the same side | sampled, 50,000 | 12.8% | 50.0% | 90.3% | 99.5% | 99.9% | 0.094% | 9.45 |
| Through a normal or inverse EO of ≤ 6, DR on the same side | sampled, 50,000 | 19.5% | 66.9% | 98.3% | >99.9% | 100.0% | 0% | 9.12 |
| Through any EO of ≤ 3 (normal, inverse, NISS; a NISS EO takes the DR on the better side) | sampled, 50,000 | 5.1% | 21.0% | 43.4% | 49.5% | 49.6% | 50.4% | 9.58 |
| Through any EO of ≤ 4 (normal, inverse, NISS; a NISS EO takes the DR on the better side) | sampled, 50,000 | 10.4% | 42.5% | 82.3% | 95.0% | 96.0% | 4.0% | 9.58 |
| Through any EO of ≤ 5 (normal, inverse, NISS; a NISS EO takes the DR on the better side) | sampled, 50,000 | 18.2% | 64.6% | 97.7% | >99.9% | >99.9% | 0.012% | 9.16 |
| Through any EO of ≤ 6 (normal, inverse, NISS; a NISS EO takes the DR on the better side) | sampled, 50,000 | 28.4% | 82.7% | 99.9% | 100.0% | 100.0% | 0% | 8.84 |

The two targets people ask about most, as the share of scrambles with such a route. Each row adds EOs to the row above:

| EOs | DR in ≤ 10 | DR in ≤ 11 |
|---|---|---|
| Normal, at most 5 turns | 77.7% | 97.3% |
| Adding the inverse EOs | 90.3% | 99.5% |
| Adding the NISS EOs | 97.7% | >99.9% |
| At most 4, every kind | 82.3% | 95.0% |

A route through an EO of at most 5 (all kinds) is 9 or better on 64.6% of scrambles, against 99.1% for the NISS optimum. These are what exists, not what anybody finds: every EO of that length is checked, with both DR axes and the best DR after it. **Computer only**: an answer key for how good the EOs you could write are, not a search to do in an attempt.

### 3.3 How many DRs

For every EO of at most k turns and each of its two DR axes, is the EO plus the best DR after it (EO kept; for a NISS EO on the better side) at most N turns? A scramble's count is the number of such (EO, DR axis) pairs. Like 3.2 these are **computer only**: they need the best DR after every EO on both axes, and say how many DRs exist, not how many a solver finds. 50,000 scrambles; EOs counted as in nissy's `-a` listing (both directions of the last turn). Each row is a kind of EO, its axes and maximum length; the *Pairs* columns are the mean number of pairs per scramble with EO plus DR at most that many turns:

| EOs | EO axes | EO length, turns | EOs per scramble | Pairs, total ≤ 9 | Pairs, total ≤ 10 | Pairs, total ≤ 11 | Pairs, total ≤ 12 |
|---|---:|---:|---:|---:|---:|---:|---:|
| normal | F/B only | ≤ 4 | 5.1 | 0.1 | 0.8 | 3.5 | 8.5 |
| normal | F/B only | ≤ 5 | 67.4 | 0.3 | 1.9 | 11.0 | 46.8 |
| normal | all three | ≤ 4 | 15.3 | 0.4 | 2.5 | 10.6 | 25.6 |
| normal | all three | ≤ 5 | 203.2 | 0.9 | 5.7 | 32.9 | 140.7 |
| normal or inverse | F/B only | ≤ 4 | 10.1 | 0.3 | 1.6 | 7.0 | 17.0 |
| normal or inverse | F/B only | ≤ 5 | 135.0 | 0.6 | 3.8 | 21.8 | 93.6 |
| normal or inverse | all three | ≤ 4 | 30.4 | 0.9 | 4.9 | 21.1 | 51.0 |
| normal or inverse | all three | ≤ 5 | 406.0 | 1.7 | 11.4 | 65.6 | 281.2 |
| normal, inverse or NISS (DR on the better side) | F/B only | ≤ 4 | 14.6 | 0.5 | 2.8 | 11.7 | 25.6 |
| normal, inverse or NISS (DR on the better side) | F/B only | ≤ 5 | 215.4 | 1.1 | 7.6 | 43.4 | 177.6 |
| normal, inverse or NISS (DR on the better side) | all three | ≤ 4 | 43.9 | 1.5 | 8.4 | 35.0 | 76.6 |
| normal, inverse or NISS (DR on the better side) | all three | ≤ 5 | 646.4 | 3.3 | 22.7 | 130.1 | 532.2 |

The same rows as the share of scrambles with no such pair:

| EOs | EO axes | EO length, turns | No pair, total ≤ 9 | No pair, total ≤ 10 | No pair, total ≤ 11 | No pair, total ≤ 12 |
|---|---:|---:|---:|---:|---:|---:|
| normal | F/B only | ≤ 4 | 92% | 77% | 62% | 59% |
| normal | F/B only | ≤ 5 | 86% | 57% | 27% | 16% |
| normal | all three | ≤ 4 | 80% | 47% | 25% | 22% |
| normal | all three | ≤ 5 | 67% | 22% | 3% | 0.62% |
| normal or inverse | F/B only | ≤ 4 | 86% | 64% | 47% | 43% |
| normal or inverse | F/B only | ≤ 5 | 77% | 39% | 11% | 6% |
| normal or inverse | all three | ≤ 4 | 67% | 31% | 14% | 12% |
| normal or inverse | all three | ≤ 5 | 50% | 10% | 0.51% | 0.11% |
| normal, inverse or NISS (DR on the better side) | F/B only | ≤ 4 | 81% | 51% | 32% | 29% |
| normal, inverse or NISS (DR on the better side) | F/B only | ≤ 5 | 66% | 21% | 3% | 1% |
| normal, inverse or NISS (DR on the better side) | all three | ≤ 4 | 58% | 18% | 5% | 4% |
| normal, inverse or NISS (DR on the better side) | all three | ≤ 5 | 35% | 2% | 0.042% | 0.012% |

Per EO it's a small number, and it drops fast with the EO's length. Expected (EO, DR axis) pairs per EO, normal EOs, all three axes. Each yield is a ratio of sums (all pairs over all EOs of the kind, over the 50,000 scrambles), and the column for EOs of at most 4 includes those of 0 to 3 turns. Each row is a target for EO plus DR:

| Total turns (EO + DR) | Pairs per EO of ≤ 4 | Pairs per EO of exactly 5 | Pairs from 25 EOs of ≤ 4 | Pairs from 200 EOs of exactly 5 |
|---|---:|---:|---:|---:|
| ≤ 9 | 0.028 | 0.0023 | 0.7 | 0.5 |
| ≤ 10 | 0.161 | 0.0174 | 4.0 | 3.5 |
| ≤ 11 | 0.693 | 0.1185 | 17.3 | 23.7 |
| ≤ 12 | 1.674 | 0.6128 | 41.9 | 122.6 |

The last two columns answer Somebodyidk's "25 4 move eos or 200 5 move eos" ([5 Jan 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1457758593762857091)): on average the 25 short EOs give more DRs of 10 or better, the 200 longer ones more of 11 or 12. EOs on one scramble are correlated, so these are expectations over scrambles, not a guarantee on any one. The part you can use in an attempt is the ratio: for a DR in 10, one EO of at most 4 is worth about ten 5-movers, so the 4-movers come first.

Two more measurements of what each kind of EO adds, normal EOs:

- **5-move EOs on top of the 4-movers**: on scrambles that have an EO of at most 4 (all axes), adding the 5-movers gives a shorter best route on 34.7% of them, by 0.44 turns on average counting the scrambles where nothing improves, 1.27 turns where it does. 21.5% of scrambles have no normal EO of at most 4 at all.
- **The other two EO axes on top of F/B** (EOs of at most 5): over all scrambles the best route improves on 52.8%. On 38.7% the F/B route gets shorter, and the other 14.6% have no F/B EO of at most 5 at all. On the 85.4% that do have one, it improves on 45.3% of them, from 10.47 to 9.76 on average.

---

## 4. Scramble to EO

### 4.1 How many EOs, how short

How many EOs a scramble has, on the same 50,000 uniformly random scrambles. An EO of length L is a move sequence that solves EO on its axis for the first time at its L-th turn, so its last turn is a quarter turn of that axis, and the two directions of that last turn count as two EOs. That's nissy's `solve eo -a` listing, and my counts match nissy's on 30 scrambles (appendix B). A NISS EO has turns on both sides, each side ending in a quarter turn of the axis.

nissy without `-a` lists an EO only if each side ends in a clockwise quarter turn (two of them where a side ends in turns of two opposite faces, like `F B`). So of the EOs that differ only in the directions of their last turns it keeps one: one of two for most one-sided EOs, one of four for most NISS EOs. On the first 150 scrambles it lists 46.6% of the normal and inverse EOs of at most 5 and 22.4% of the NISS ones, 37.8% in all, about two fifths. The counts quoted on the server are of that kind: on those scrambles nissy's default NISS listing has a mean of 242.9 EOs of at most 5 and 17.1 of at most 4 (medians 223.5 and 14), about what Cale's sheet of official scrambles has ("mean = 246", "median = 217"; "mean: 17.3", "median: 14").

Each row is a kind of EO and its axes; the cells are the mean number of EOs per scramble up to that length:

| EOs | Axes | EOs of ≤ 3, mean | EOs of ≤ 4, mean | EOs of ≤ 5, mean | EOs of ≤ 6, mean |
|---|---:|---:|---:|---:|---:|
| normal | F/B only | 0.38 | 5.1 | 67 | 900 |
| normal | all three | 1.15 | 15.3 | 203 | 2,709 |
| normal or inverse | F/B only | 0.76 | 10.1 | 135 | 1,802 |
| normal or inverse | all three | 2.27 | 30.5 | 406 | 5,415 |
| normal, inverse or NISS | F/B only | 0.98 | 14.6 | 215 | 3,147 |
| normal, inverse or NISS | all three | 2.95 | 43.9 | 646 | 9,443 |

The same rows: medians, the share of scrambles with no EO that short, and the most on one scramble:

| EOs | Axes | EOs of ≤ 4, median | EOs of ≤ 5, median | Scrambles with no EO of ≤ 4 | Scrambles with no EO of ≤ 5 | Most EOs of ≤ 5 on one scramble |
|---|---:|---:|---:|---:|---:|---:|
| normal | F/B only | 0 | 32 | 58.7% | 14.6% | 476 |
| normal | all three | 12 | 172 | 21.5% | 0.48% | 1,216 |
| normal or inverse | F/B only | 4 | 78 | 43.1% | 5.2% | 824 |
| normal or inverse | all three | 24 | 342 | 11.7% | 0.094% | 2,320 |
| normal, inverse or NISS | F/B only | 8 | 162 | 28.9% | 0.95% | 1,204 |
| normal, inverse or NISS | all three | 36 | 574 | 4.0% | 0.012% | 2,998 |

The columns up to 4 turns are lists you can actually write; the 5- and 6-turn counts, hundreds to thousands per scramble, are nissy's `-a` listings, **computer only**, there to compare scrambles, not to write out. The one-axis normal row is also exact over the 2,048 orientations of one axis: at most 5 turns, mean 67.4 in the sample against 67.7 exact.

The shortest EO of a scramble, over the three axes. Each row is a side rule; the *EO in ≤* columns are the share of scrambles with an EO that short:

| Shortest EO | Exact or sampled | Mean, turns | EO in ≤ 2 | EO in ≤ 3 | EO in ≤ 4 | EO in ≤ 5 | Longest seen, turns |
|---|---:|---:|---:|---:|---:|---:|---:|
| One fixed axis, normal | exact, 2,048 EO states | 4.609 | 1.4% | 11.2% | 41.5% | 85.4% | 7 |
| Best of 3 axes, normal | sampled, 1,000,000 | 3.881 | 4.0% | 29.3% | 78.5% | 99.5% | 7 |
| Best of 3 axes, normal or inverse | sampled, 1,000,000 | 3.601 | 7.5% | 43.6% | 88.1% | 99.9% | 7 |
| Best of 3 axes with NISS | sampled, 1,000,000 | 3.455 | 8.1% | 49.6% | 96.0% | >99.9% | 6 |

The fixed-axis row is exact (DougCube's 4.609 ✓ in [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo)). The NISS row reproduces Joba's exact 3.455 ([27 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1410262132783714485)) to within the sample's error, and Joba's table also gives the rarest case, one the sample never hit: 7 turns even with NISS ("Distance 7: 1792" of all $12!\cdot 2^{11}$ edge states).

What's new is the middle two rows, linear on all three axes and normal or inverse, and the odds at each length. (The 50,000 scrambles of section 3 agree within sampling error: an EO of at most 4, normal or inverse, on 88.3% of them against 88.1% here.) The short ones, as the share of scrambles with an EO of that length or shorter on some axis:

| EO on some axis | Linear | With the inverse | With NISS |
|---|---|---|---|
| 3-move | 29.3% | 43.6% | 49.6% |
| 2-move | 4.0% | 7.5% | 8.1% |

Odd scrambles, from the 50,000:

- **No EO of at most 5 turns on any axis, even with NISS**: 0.012% of scrambles, 6 in the sample [d].
- **More 3-move EOs than 4-move EOs**: never with linear EOs (normal side, all axes) in the sample; with NISS on 0.018% of scrambles [e].
- **An N-move EO but no (N+1)-move EO** (all axes):
  - 1 turn and none of 2: 0.14% linear;
  - 2 and no 3: 0.57%;
  - 3 and no 4: never linearly in the sample, 0.016% with NISS;
  - never for 4 and 5.

### 4.2 Bad edges on the three axes

Exact over all $12!\cdot 2^{11}$ edge states (34,650 ways to place the E-, M- and S-slice pieces times 2,048 flip patterns; within a slice the order does not matter). torchlight computed the sorted triples in 2023 (the speedsolving post on bad-edge counts, and [25 Sep 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1155803699025813594)). The table here is the same; on top of it I add the ordered triples, the layouts by axis and the EO odds by bad-edge count. The most common sorted triples; each row is a set of bad-edge counts on the three axes, in any order:

| Bad edges on the three axes (sorted) | Probability (exact) | As a percentage |
|---|---:|---:|
| 4/6/6 | $218033/1478400$ | 14.7% |
| 6/6/8 | $218033/1478400$ | 14.7% |
| 4/6/8 | $8539/61600$ | 13.9% |
| 6/6/6 | $815891/8870400$ | 9.2% |
| 4/4/6 | $43721/492800$ | 8.9% |
| 6/8/8 | $43721/492800$ | 8.9% |
| 4/4/8 | $1101/30800$ | 3.6% |
| 4/8/8 | $1101/30800$ | 3.6% |

All 65 are in appendix A. A few facts that come out exactly:

- all 12 edges good on one given axis: probability $1/2048$; on some axis: $103741/70963200$ (0.15%);
- 12/12/12 is 1 in 70,963,200;
- some axis has 10 bad on 9.2% of scrambles;
- no two axes differ by more than 8;
- after an EO the other two axes have 0, 2, 4, 6 or 8 bad.

Uneven triples are rarer than independent axes would make them: 2/10/10 has probability 0.0015%, against 0.010% if the axes were independent, 6.5 times less.

The chance of a short EO on one axis, by its number of bad edges. The last column, the shortest normal EO of each of the 2,048 states, is Shota's table ([11 Sep 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1283314529916420116)) and agrees with Shota's *Full EO* sheet; the new part is the odds with the inverse and with NISS. The normal columns are exact over the 2,048 states of one axis. The inverse and NISS columns are sampled, 1,000,000 random states times 3 axes, so ±0.1 point or better, except the rare 0-, 10- and 12-bad rows, which rest on about 1,400 to 97,000 axes. Each row is a number of bad edges on the axis; the *EO in ≤* columns are the share of such axes with an EO that short:

| Bad edges | Share of axes | Normal EO in ≤ 3 | Normal EO in ≤ 4 | Normal EO in ≤ 5 | Normal or inverse EO in ≤ 4 | Normal or inverse EO in ≤ 5 |
|---|---:|---:|---:|---:|---:|---:|
| 0 | $1/2048$ | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| 2 | $66/2048$ | 60.6% | 93.9% | 100.0% | 99.6% | 100.0% |
| 4 | $495/2048$ | 32.3% | 88.1% | 99.4% | 98.6% | >99.9% |
| 6 | $924/2048$ | 0.87% | 22.5% | 82.7% | 39.9% | 97.0% |
| 8 | $495/2048$ | 4.2% | 28.9% | 86.3% | 49.5% | 98.1% |
| 10 | $66/2048$ | 0% | 0% | 0% | 0% | 0% |
| 12 | $1/2048$ | 0% | 0% | 0% | 0% | 0% |

With NISS, same rows:

| Bad edges | NISS EO in ≤ 3 | NISS EO in ≤ 4 | NISS EO in ≤ 5 | Sampled axes (NISS columns) |
|---|---:|---:|---:|---:|
| 0 | 100.0% | 100.0% | 100.0% | 1,427 |
| 2 | 85.3% | >99.9% | 100.0% | 97,018 |
| 4 | 57.0% | 99.3% | 100.0% | 725,919 |
| 6 | 6.2% | 63.3% | 99.6% | 1,352,539 |
| 8 | 10.7% | 61.4% | 99.6% | 725,001 |
| 10 | 0.40% | 11.8% | 79.5% | 96,607 |
| 12 | 0.74% | 19.5% | 85.8% | 1,489 |

Shota's table: each row is a length of the shortest normal EO, each column a number of bad edges, and the cell is how many of the 2,048 edge-orientation states have it (– for none):

| Shortest normal EO, turns | 0 bad | 2 bad | 4 bad | 6 bad | 8 bad | 10 bad | 12 bad |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | – | – | – | – | – | – |
| 1 | – | – | 2 | – | – | – | – |
| 2 | – | – | 24 | – | 1 | – | – |
| 3 | – | 40 | 134 | 8 | 20 | – | – |
| 4 | – | 22 | 276 | 200 | 122 | – | – |
| 5 | – | 4 | 56 | 556 | 284 | – | – |
| 6 | – | – | 3 | 160 | 68 | 54 | – |
| 7 | – | – | – | – | – | 12 | 1 |

This table is for the attempt: the bad edges on each axis are what you see when you look for EO, and the row gives the odds of a short EO on that axis.

What it says:

- **8 bad beats 6 bad for short EOs, linearly**: an EO of at most 4 on 28.9% ✓ of 8-bad axes against 22.5% ✓ of 6-bad ones, of at most 3 on 4.2% ✓ against 0.87% ✓. With NISS 6 bad is a little better (63.3% against 61.4% for at most 4).
- **10 and 12 bad**: no normal EO under 6 (54 ✓ of the 66 ten-bad states of one axis take 6, 12 ✓ take 7; twelve bad takes 7 ✓).
- **With NISS a 12-bad axis is better than a 10-bad one**: at most 5 on 85.8% against 79.5%, at most 4 on 19.5% against 11.8%.
- **Normal or inverse doesn't help a 10- or 12-bad axis**: the inverse has the same number of bad edges on each axis as the normal side.

---

## 5. EO to DR

From an EO-solved state, how many turns to DR. With one DR axis, turns that keep the EO, linear, this is Cale's table ([*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0)), FakeMMAP's counts ([16 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1141304202065367170)), the last tab of Louis's [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs) and DougCube's [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo), all the same 1,082,565 states; torchlight's table allows EO-breaking turns ([16 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1141354103138693243)). Here I put the options you actually have next to it: the other DR axis of the same EO, the inverse, the EO's last turn the other way, and EO-breaking turns, alone and together.

How it's set up:

- **Weighting.** After an EO chosen as a function of the edge orientation alone, the state is uniform over the EO-solved states, so every one of the 1,082,565 (corner orientation, E-slice placement) cosets is equally likely. Cale's and Louis's tables assume the same. It doesn't hold exactly for NISS EOs (which ones exist depends on the edge permutation too), for EOs chosen by looking at the case they leave, or for the states after an RZP.
- *Last EO turn the other way*: the EO ends in a quarter turn of its axis (say `F`); the alternative is the same EO with `F'`, which is the state times `F2`.
- *Normal or inverse*: the same EO, then the DR found on the inverse of the post-EO state, written `EO (DR)`.
- **Exact and sampled.** The exact rows are over all 1,082,565 states (for the better of two axes: over all corner states times all placements of the E- and M-slice pieces). The sampled ones are 10,000,000 uniform EO-solved states with exact lookups, so a share is good to ±0.02 points.

### 5.1 The typical EO to DR, with each option

Each row is what you allow after the EO; the *DR in ≤* columns are the share of EO-solved states with a DR that short, and the last column is the same for 6 as odds.

| After the EO: DR with | Exact or sampled | Mean, turns | DR in ≤ 4 | DR in ≤ 5 | DR in ≤ 6 | DR in ≤ 7 | DR in ≤ 8 | DR in ≤ 6: 1 in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| one DR axis, EO kept, normal (the known table) | exact, 1,082,565 states | 7.803 | 0.11% | 0.87% | 5.9% | 30.6% | 82.4% | 16.89 |
| one DR axis, any turns (EO may break) | exact, 1,082,565 states | 7.797 | 0.11% | 0.87% | 5.9% | 30.8% | 82.8% | 16.82 |
| one DR axis, EO kept, last EO turn inverted if better | exact, 1,082,565 states | 7.542 | 0.19% | 1.5% | 9.5% | 43.2% | 91.6% | 10.56 |
| one DR axis, any turns, last EO turn inverted if better | exact, 1,082,565 states | 7.537 | 0.19% | 1.5% | 9.5% | 43.4% | 91.8% | 10.53 |
| better of the two DR axes, EO kept | exact, 1,082,565 states | 7.401 | 0.22% | 1.7% | 11.3% | 50.6% | 96.0% | 8.82 |
| one DR axis, EO kept, on the inverse only | sampled, 10,000,000 | 7.803 | 0.11% | 0.87% | 5.9% | 30.6% | 82.4% | 16.88 |
| one DR axis, EO kept, better of normal and inverse | sampled, 10,000,000 | 7.420 | 0.23% | 1.7% | 11.2% | 49.7% | 95.2% | 8.96 |
| two DR axes x last turn inverted, EO kept, normal | sampled, 10,000,000 | 7.139 | 0.38% | 2.9% | 17.8% | 66.1% | 98.9% | 5.63 |
| two DR axes x normal/inverse, EO kept | sampled, 10,000,000 | 7.045 | 0.45% | 3.3% | 20.4% | 71.9% | 99.4% | 4.91 |
| two axes x normal/inverse x last turn, EO kept | sampled, 10,000,000 | 6.898 | 0.60% | 4.4% | 25.7% | 79.6% | 99.7% | 3.89 |
| two DR axes, any turns, normal | sampled, 10,000,000 | 7.396 | 0.23% | 1.7% | 11.4% | 50.9% | 96.1% | 8.78 |
| everything above (EO kept or not) | sampled, 10,000,000 | 6.895 | 0.60% | 4.4% | 25.8% | 79.8% | 99.8% | 3.88 |

Zagros asked ([30 Jun 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1389269657126699138)): "What is typical eo->dr? … Is 7 moves from eo to dr typical? Or is 8 optimal common". Louis answered with the distribution ("That's the optimal distribution for EO to DR", [1 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1389570667267231815)) and Zagros read it as "So it is 8 then typically" ([1 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1389576595051774002)), adding "But I suppose this probably doesnt account for all the different ways you can rzp->switch" ([1 Jul 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1389576810953703516)). The first row is that distribution, for EO-solved states (Zagros's sub-7 is after an RZP, a different population). The rest of the table is what the ways to switch are worth:

- **The other DR axis** of the same EO is worth more than switching the EO's last turn: at most 6 on 11.3% of EOs against 9.5% ✓, mean 7.401 against 7.542 ✓. Checking the inverse is worth about the same as the other axis (11.2%).
- **All of the EO-keeping options together** (two axes, normal or inverse, last turn either way): mean 6.898, at most 6 on 25.7% (1 in 3.89, against 1 in 16.89 ✓ for one axis), at most 7 on 79.6%. So once you use every option, the typical EO is 7 from DR, not 8.
- **EO-breaking turns change almost nothing** (exact; torchlight's table). On top of all the EO-keeping options they add 0.003 turns on average [f]. Of the 6,433 EO-solved states where any turns are shorter, 485 have no edge out of place; then the other EO is solved too, and a DR as short keeps it. One axis, with and without them:

| Turns after the EO | Mean, turns | DR in ≤ 6 |
|---|---|---|
| Keeping the EO | 7.803 ✓ | 5.92% |
| Any turns | 7.797 | 5.94% |

The lengths are optimal DRs after the EO: an answer key for what's there, not what you find by hand on every EO. What carries to an attempt is the list of options and their order: after an EO, look at the other DR axis and at the inverse as well as the one you set out for, and try the last turn the other way. The case on each axis says how likely each one is to give something short (5.2).

An example of each, the EOs written out with the scrambles in [g] and [f]:

```
D2 L2 B' D   // the inverse: then 9 on the normal side, 5 on the inverse
F' B' U' F'  // the other axis: 9 on R/L, 5 on U/D
R' D2 L' D   // the switch: 6, and 5 with D'
```

And an EO-breaking turn, after an EO (F/B) that is the only EO solved: 7 keeping the EO, 6 breaking it.

### 5.2 By case

The case after the EO, on the DR axis you're looking at, in the server's naming: bad corners, then edges out of place for that DR (slice edges outside the slice and as many others inside it), with 6c and 8c not split into 3+3 and 6+0 (Cale's sheet splits them). Below are the 16 most common cases. The share of EOs and the mean are exact; the other columns are the chance of a DR of at most 6 with each option (exact for one axis, the switch and the better of two axes; sampled, 10,000,000 states, for the inverse and all together). Each row is a case; the *DR in ≤ 6* columns are the chance with each option:

| Case on the DR axis | Share of EO-solved states | Odds | Mean turns, one axis | DR in ≤ 6: one axis | DR in ≤ 6: last EO turn either way | DR in ≤ 6: better of 2 DR axes | DR in ≤ 6: normal or inverse | DR in ≤ 6: all of these |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 6c6e | 12.7% | 1 in 7.8 | 7.73 | 5.6% | 9.4% | 10.6% | 10.8% | 25.1% |
| 5c6e | 11.6% | 1 in 8.6 | 7.69 | 6.1% | 10.2% | 11.7% | 11.9% | 27.2% |
| 6c4e | 9.6% | 1 in 10.5 | 7.97 | 3.0% | 5.3% | 8.5% | 5.9% | 20.5% |
| 4c6e | 8.7% | 1 in 11.5 | 7.85 | 4.6% | 7.7% | 10.3% | 9.0% | 24.2% |
| 5c4e | 8.7% | 1 in 11.5 | 7.60 | 7.2% | 12.2% | 13.6% | 14.0% | 31.4% |
| 7c6e | 7.0% | 1 in 14.4 | 7.82 | 4.0% | 6.7% | 8.6% | 7.9% | 20.9% |
| 4c4e | 6.5% | 1 in 15.3 | 7.19 | 19.2% | 28.1% | 25.4% | 34.8% | 51.1% |
| 7c4e | 5.2% | 1 in 19.2 | 8.10 | 2.2% | 3.8% | 6.6% | 4.4% | 16.1% |
| 6c8e | 4.0% | 1 in 25.1 | 7.90 | 3.2% | 5.6% | 8.1% | 6.3% | 19.7% |
| 5c8e | 3.6% | 1 in 27.6 | 8.08 | 1.4% | 2.6% | 6.2% | 2.8% | 15.5% |
| 4c8e | 2.7% | 1 in 36.8 | 8.48 | 0.27% | 0.49% | 4.6% | 0.54% | 11.4% |
| 3c6e | 2.3% | 1 in 43.2 | 7.84 | 4.8% | 7.8% | 10.9% | 9.3% | 25.2% |
| 7c8e | 2.2% | 1 in 46.0 | 7.25 | 16.4% | 24.4% | 20.5% | 30.3% | 43.8% |
| 6c2e | 1.8% | 1 in 54.9 | 8.27 | 0.16% | 0.32% | 5.8% | 0.33% | 14.1% |
| 8c6e | 1.8% | 1 in 56.2 | 8.08 | 1.2% | 2.1% | 5.8% | 2.4% | 14.4% |
| 3c4e | 1.7% | 1 in 57.5 | 7.45 | 9.9% | 15.9% | 18.2% | 19.0% | 39.6% |

This table is for the attempt: the case is what you read at the table (twisted corners and edges out of place on each DR axis), and the row says how likely a DR in 6 or fewer is with each option. The DR lengths behind it are optimal, so treat the odds as what is there to find. All 40 cases but 0c0e (already a DR) with the mean and the odds of each option are in appendix A. The better of two axes is read by the case on the first one, so it mixes every case the second axis can have.

**Normal and inverse.** Java asked trig0n whether the rule not to switch when there's nothing on normal holds for RZP to DR ([11 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074172721140871330): "does this apply to RZP -> DR and HTR subsets?"). Tom Nelson: "it's the opposite for rzp to DR because if it's bad then it's more likely to be better after switching" ([11 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074181270952747120)); Jay: "i'm certain there's zero correlation" ([11 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074182849965596824)); Tom Nelson: "yeah that's what I mean. If it's 8 moves on normal then it's more likely to be better on inverse because any random case is probably sub-8" ([11 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074184563309428775)); Rodney Kinney: "Regression to the mean" ([11 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074187563704782908)). trig0n's own answer was the same: "Unfortunately no" ([12 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074261391671840868)), as was Jay's first ("actually that's definitely not true, i could easily set up a counter example", [11 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074176781524942948)).

Over all EO-solved states, the DR lengths on normal and on the inverse (same axis, EO kept) have correlation 0.1684: a bad normal side does make a bad inverse a little more likely. Almost all of that is the case. The inverse of a position has the same case on the same axis (as many twisted corners, as many slice edges out of the slice), and within one case the correlation is between -0.015 and 0.063 in each of the 35 cases with 1,000 or more samples (appendix A). Small, but not zero: the largest (0.0628 for 8c2e, 0.0282 for 6c8e, 0.0167 for 6c6e) are in cases that lump together sub-cases the inversion keeps (6c is 3+3 or 6+0, 8c is 4+4 or 7+1).

So they are right once the case is known, as it is after an RZP: the inverse is close to a fresh draw from that case (Jay), and a long normal side is no reason to expect a long inverse, so switching after a bad one pays (Tom Nelson and Rodney Kinney). The chance the inverse is at most 6, given the normal side's length (same axis, EO kept):

| Normal side, turns | Inverse DR in ≤ 6 |
|---|---|
| 9 | 3.2% |
| 6 | 11.2% |
| Any (overall) | 5.9% |

---

## 6. The claims, checked

Statements the numbers can settle, by theme. Questions and guesses are in section 2, not here. Each verdict is one of **True**, **Corrected**, **Depends** (true under one reading or convention, not another), **Open** (the numbers here do not settle it) and **Withdrawn** (taken back at the time by whoever said it), and is no stronger than what was measured: scramble-level numbers are on 50,000 uniformly random scrambles, EO to DR numbers exact unless marked. Every correction has an example written out under the tables (letters in brackets).

**Scramble to DR.** One claim per row, who said it, and the verdict.

| Claim | Who | Verdict |
|---|---|---|
| "Only 6.2% of axes are 8 moves or less away from DR if you don't allow NISS"; "43% of scrambles being 9 moves or better away from DR" | Louis [9 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1326956621435506808), [9 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1326954809827262576) (restated for one axis, [9 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1326956179103940748)) | **True**: exact, 6.2% and 43.3% on one fixed axis, linear. Over three axes and both sides it is 28.4% and 91.5% (3.1). |
| "5.9% of axes are 6 moves or fewer away from DR linearly if EO is solved (and you don't break it)" | Louis [10 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1327214655453663253) | **True**: 5.9% ✓, exact. |
| "well sub-10 is not possible for superflip" | wen [9 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1547202526749786114) | **True**: 10 on every axis, normal and inverse, and 10 with NISS [b]. |
| DR skip: "1 in 2^11 * 3^7 * 12! / 8! or something like that", a passing answer in a joke thread | bpaul [24 Jan 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1067539508649791558) | **Corrected**, lightly: the order of the four slice edges does not matter, so $12!/8!$ should be $12!/(8!\cdot 4!) = 495$ ✓; 1 in 2,217,093,120 ✓ on a given axis, about 1 in 739 million ✓ on some axis [i]. |
| From 4 four-move and 45 five-move EOs with RZPs in 5: "If you NISS for all of them let's just count that as 20", "If you can find optimal DR every time, you can expect 4 DRs in 11 and 10 DRs in 12" | Tom Nelson [9 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062115508641599498) | **Depends** on what is counted. Tom Nelson counted DRs through a few RZP types in 5, NISSed, found optimally ([11 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062872328960229487): "I just counted R, R U2 R and R U R"). Every route through those EOs on the normal side gives about 8.1 (EO, DR axis) pairs in 11 and 34.3 in 12 on average when each EO is one direction of its last turn (3.3). Tom Nelson's own arithmetic counts each 5-mover for both directions ("45 * 2 = 90", [9 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062115508641599498)), the way EOs are usually counted on the server (4.1), and counted that way it is about 16 and 69. So Tom Nelson's figures are a lower bound on what exists, as Tom Nelson's own caveats say ([9 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062118696950169742)). |
| "I see people checking ~50 EOs, so finding 6 DRs with <= 11 moves sounds realistic" | Rodney Kinney [9 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1062022602262065182) | **Depends** on the EOs: 50 EOs of 5 turns give about 5.9 routes in 11 on average, 11.9 if each stands for both directions of its last turn (the way EOs are usually counted on the server, 4.1); 50 of at most 4 about 35, or 69 (3.3). What exists, not what is found. |
| "150 4e4c's in 5 is ~7 10 move DRs and 1 9 move DR" | Tom Nelson [20 Sep 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1153957932375998534) | **True** as arithmetic on the exact table: an RZP in 5 then a DR in 5 or fewer is 150 × 4.3% ✓ = 6.5 ✓, in 4 or fewer 150 × 0.82% ✓ = 1.2 ✓ (4c4e straight off an EO, one axis, EO kept). zakimoshi's caveat ([20 Sep 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1153959223818989629), "This kinda implies that everything is unrelated to each other") stands: RZPs of one scramble are not independent, and RZPs are not covered here (section 7). |
| One of 300 EOs gives a DR in 5 or less "92.71%" (binomial, `1 - (1 - p)^300`, from the one-axis table) | DougCube [15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417264063553081415) | **Open**: the arithmetic is right ✓, for one DR axis per EO (JTuu, [15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417265136581873664): "oh, it's only UD dr"; DougCube, [15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417265956362915975): "oh sorry, I forgot to stipulate that"). DougCube flagged the assumption ([15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417264352293027912): "assuming each of the EOs are statistically independent of each other"; [15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417264724143374489): "tho, I think that by limiting to 5-move or less EO, then it becomes coupled and are not independent"; [15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417264810105639034): "if instead, it's any length EO, then I think these computations should hold very well"). How dependent the EOs of one scramble are for EO to DR alone is not measured here; for whole routes, see 3.3. |

**EO to DR.** One claim per row, who said it, and the verdict.

| Claim | Who | Verdict |
|---|---|---|
| The EO to DR counts 1, 2, 17, …, 3114 ("not allowing EO-breaking moves") | FakeMMAP [16 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1141304202065367170); DougCube [15 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1417261933916196945) | **True**, reproduced exactly. |
| EO to DR with EO-breaking turns: "allows breaking EO" | torchlight [16 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1141354103138693243) | **True**: mean 7.797 against 7.803, exact. |
| "Last sheet of DRM/ARM doc has a distribution. 10 is the worst (~3% of all cases)" | KrzychXyz [12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1415999087219839016) | **Corrected**: 10 is the worst, as KrzychXyz says, but 3,114 ✓ of the 1,082,565 EO-solved states need it, 0.29% ✓: ten times less than said. One such EO in [h]. |
| "like how DR-4e4c in 6 moves is 1 in 5.2 normally, but 1 in 3.6 if you can switch the last move" | Tom Nelson [13 Jul 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1128948555684519946) | **True** for at most 6: 1 in 5.2 ✓ and 1 in 3.6 ✓ (the EO's last turn). |
| Asking "Has anyone ever tried to verify the DR setup stats (switching last move)?": "only 3 out of this 27 DR-4e4c can be reduced to DR in 6 moves or less (accounting for switching the last move)", then "Is there anything obvious that I missed?" | Lichi Fang [8 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215614177234788352) | **Open**. The exact rate for a 4c4e straight off an EO, last EO turn either way, is 28.1% ✓; 3 or fewer of 27 has probability 3.3% ✓ under it (compLex: "only a 3.2% chance of those test results", [8 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215616530650497074)), and Cale's 25 fit it (next row). Both samples are the first 4c4e nissy online found, after an RZP, which need not be like a uniform EO-solved state (torchlight, [8 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215720321995382867): "if the EO isn't already 4c4e, it means that the 4c4e case you get from RZP is 1 move away from something that is not 4c4e"). Lichi Fang switched the RZP's last move, not the EO's, and asked whether that was it ("Or maybe switching the last move of rzp is much worse than switching the last move of eo?"); Cale's table for the RZP's last move ([9 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1216110077291925564)) gives 27.2%, and 3 or fewer of 27 is then 4.0%, so that doesn't explain it either. RZPs are not covered here. |
| Re-test, first 4c4e found on 25 scrambles: "The optimals were 6 moves for 24%, 7 moves for 56%, and 8 moves for 20%" | Cale [9 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1216110077291925564) | **True** within its sample: the exact shares for a 4c4e with the EO's last turn either way are 7.0% ✓ in 5 or fewer, 21.1% ✓ in 6, 46.3% ✓ in 7, 25.2% ✓ in 8 and 0.48% ✓ in 9; on 25 a share has a standard error of about 9 points. |
| "'dr setup sheet' shows that 4c4e pops up 1 in 15.3 eo"; "so 4e4c is about 1/15" | Mike [25 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1155743788506042398); Andrew [5 Oct 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1027344312876404759) | **True**: 1 in 15.3 ✓ on one given DR axis. With two DR axes per EO, about twice as often on one of them. |
| "~5.12% chance of 3 misoriented and ~19.20% chance of 4 misoriented" | Emma [29 Mar 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1090611423480127488) | **True**, exact: 112 ✓ and 420 ✓ of the 2,187 corner orientations. |
| "Shouldn't it be 1/11 chance of 6/0" (of 6-twist cases) | Zagros [6 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1402620621313020028) | **True**: 56 ✓ of the 616 ✓ orientations with six twisted corners. wen's "50/50?" ([6 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1402535429735059537)) was a guess. |
| "i think DR-5c6e is actually tied for the most common DRM you can get after any random EO"; "6c (including both 6+0 and 3+3) is a bit more common than 5c", "edit: 3+3 is tied with 5c" | Jay [5 Feb 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1336873153795854438); torchlight [5 Feb 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1336879107362914316) | **True**, both: 5c6e and 6c6e with 3+3 corners are tied in Cale's split; 6c6e as a whole is the most common case (12.7% ✓ against 11.6% ✓). |
| 4c6e: "even with full moveset sub-7 is 1 in 22" | Cale [10 Apr 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1094878042096152576) | **True**: 1 in 21.7 ✓ for at most 6 (one axis, EO kept). |
| DR-6e4c: "Similar efficiency to 4c4e and 4c2e in theory but many of the optimal solutions aren't findable with just setups to R U2 L" | Jay [14 Dec 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1052704838682689648), again [9 Apr 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1094803776336044113) | **Corrected** for the optimum too, by Cale when Jay said it again in 2023 ([10 Apr 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1094878042096152576)): at most 6 on 4.6% ✓ of 4c6e against 19.2% ✓ for 4c4e and 18.7% ✓ for 4c2e; means 7.85 ✓, 7.19 ✓, 7.16 ✓. Jay agreed ("hm, i guess it's a bit more worse than 4c2e than i thought", [10 Apr 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1094891233882685470)), and the advice in Jay's next message in 2022, "I wouldn't really NISS for it" ([14 Dec 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1052704980122996826)), stands [j]. |
| "It's 10% sub7 vs 78 being 16%" (3c4e against 7c8e); "3c4e (10.1% sub-7)" | Zagros [9 Jul 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1524816104239923201); Fanti [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436042954501390401) | **True**: at most 6 on 9.95% ✓ for 3c4e with the EO kept (Fanti's 10.1% allows any turn, F/B quarter turns included, and that count gives 10.08%) and 16.4% ✓. |
| 3c6e: "it’s 1/7 for 7 moves instead of 1/3 for 4e4c, 8c8e, 8e7c, 2e4c etc" | Noah Swor [3 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1269374128155267147) | **Depends** on what "7 moves" means, and the message was about switching from a 3c6e RZP (mrauo, [3 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1269372746723491851): "Is it worth to switch from 3c6e rzp in 5?"), while these numbers are for EO-solved states, a different population. The 1/3 figures fit a DR in 6 or fewer on normal or inverse, which is what switching gives (4c4e 34.8%, 4c2e 33.8%, 7c8e 30.3%, 8c8e 26.9%), and nearly as well with the EO's last turn either way (1 in 3.6 ✓, 3.7, 4.1 ✓ and 4.3). 3c6e is then 9.3% (1 in 10.7) or 1 in 12.8 ✓; with neither it is 1 in 20.6 ✓ in 6 and 1 in 3.7 ✓ in 7. So 3c6e is well behind those four on every reading, as Noah Swor says; the 1 in 7 isn't reproduced. |
| RZP to DR on normal and inverse: "i'm certain there's zero correlation"; "it's the opposite for rzp to DR because if it's bad then it's more likely to be better after switching"; "Regression to the mean" | Jay [11 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074182849965596824); Tom Nelson [11 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074181270952747120), [11 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074184563309428775); Rodney Kinney [11 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074187563704782908) | **True** for a known case, which is what an RZP is: within a case the two sides' DR lengths have correlation between -0.015 and 0.063, and under 0.006 either way for the cases people switch from (4c4e -0.0016, 4c2e 0.0036, 3c2e -0.0018, 7c8e -0.0055, 3c4e 0.0006, 8c8e 0.0032). Tom Nelson said so in the next message ([11 Feb 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1074184563309428775): "yeah that's what I mean. If it's 8 moves on normal then it's more likely to be better on inverse because any random case is probably sub-8"). Over all EO-solved states, case not known, it is 0.1684, almost all of it from the case (5.2). Measured for EO-solved states, not RZPs. |

**Scramble to EO.** One claim per row, who said it, and the verdict.

| Claim | Who | Verdict |
|---|---|---|
| EO skip: "also 1/2048 for fixed axis", "103741/70963200 for any axis"; "9335 (~0.1458%, 1 in 686) had solved EO already" on 6,406,775 scrambles | torchlight [12 Oct 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1162060161507151983); Minkowski [25 Sep 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1155752261566349332) | **True**: exact $103741/70963200$ ✓; Minkowski's sample is within its error. |
| The sum of bad edges over the three axes peaks at 18: "18    16978144    23.925280%" | torchlight [14 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1383629578248917003) | **True**, exact. |
| "13.907% that's sort of lucky I guess" (all three axes with 0, 2, 4 or 8 bad) | jisu101 [3 Nov 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1567141993912737856) | **True**: 9868829/70963200 = 13.906967% ✓. |
| "6/6/4 or 6/6/8 is more likely than 6/6/6"; "6/6/6 is more common than 4 on UD / 6 on LR / 6 on FB" | Yura Riabov [1 Feb 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1202771755161354291); torchlight [25 Sep 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1155834425523843143) | **True**, sorted and ordered: 218033/1478400 = 14.747903% and 815891/8870400 = 9.197905% sorted; 218033/4435200 = 4.915968% and 815891/8870400 = 9.197905% ordered. |
| "no 2 axes can differ by more than 8"; 10/10/2 "managed to set it up"; "12 bad one one axis means the other two axises will have to have at least 4 bad edges."; "after eo you could have anywhere from 0-8 bad edges on the other 2 axis, but never 10 or 12" | wen [28 Jan 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1068768848951640134), [28 Jan 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1068771254791843851); Aneurin [13 Apr 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1095998245680984114); Jay [12 Apr 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1095913568148406334) | **True**, exact. |
| "for example 2/10/10 is much rarer than what you would expect with a simple calculation" | wen [1 Sep 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1544377101958914128) | **True**: 6.5 times rarer than with independent axes. |
| A linear EO for 12 bad is 7 (wen); for 10 bad no 5-mover (Jay: "nope"), "10 bad is always 6 or 7"; "TIL that some 10 bad are 7 optimal for linear eo huh"; "2 cases. Both the ones where good edges are both on F." | wen [14 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1372121363321716777); Jay [21 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1363990899373113385), [21 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1363990973776007198); Zagros [18 Feb 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1341452145551216721); KrzychXyz [27 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1410290372118319134) | **True**: 12 ✓ of the 66 ten-bad states of one axis need 7 (two cases up to symmetry), the rest 6; twelve bad needs 7 ✓. |
| "i think youre more likely to get a 4 move eo from 8 than 6"; "maybe im weird i think 8 is lowk worse than 6" | wen [3 Nov 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1567140241989701753); kyh [3 Nov 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1567139891303809035) | **Depends**: linearly wen is right (28.9% ✓ against 22.5% ✓ for at most 4); with NISS 6 bad is a little better (63.3% against 61.4%). |
| 10 bad, NISS EO in at most 5: "68%, not bad", "Number goes up to 90% if we factor in starting from inverse, once again assuming that the inverse case is independent of the normal case" | wen [14 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1064043808620298322), [14 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1064044127337062401), [14 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1064044766775476334) | **Depends** on the independence wen assumed and said doesn't hold ([14 Jan 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1064044127337062401): "ofc using the assumption that the various possible nisses from a given case are independent of each other (which they arent)"): with every NISS EO (normal, inverse or both sides), which is what the 90% counts, it is 79.5%. |
| "On average, eo can be solved in 3.455 moves."; fixed axis 4.609 | Joba [27 Aug 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1410262132783714485); DougCube [3 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412657827918516265) | **True**: 3.455 on the sample; 4.609 ✓ exact. DougCube withdrew the comparison of the two ([3 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412702486145536000)), since one has NISS and the other not; with three axes and no NISS it is 3.881. |
| God's number for EO: "7"; "yeah 7 with superflip" | Noah Swor [17 Jun 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1252389040737488987); alkamaass [17 Jun 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1252389194437890088) | **True**, with or without NISS (Joba's table; the superflip [b]). |
| Superflip: "EO is 7 moves", "Even with niss" | Aneurin [13 Sep 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1019443537940594768), [13 Sep 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1019443653632069642) | **True** [b]. |
| "Superflip takes 6 moves to solve EO with NISS" | Aneurin [13 Apr 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1095997368069009439) | **Corrected**: 7 [b]. Aneurin's first statement was right. |
| More 3-move than 4-move EOs: "so the chance is 0" | Kai Cui [7 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1315061840354607256) | **Withdrawn** at the time: kalindumaxxer answered "i literally got one" ([7 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1315061928632258621)), Kai Cui "oh bruh" ([7 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1315061947477004338)) and, after Yura Riabov's `U (R2 U)` ([7 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1315062162749657159)), "nvm then" ([7 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1315062202729758750)) and "probably quite rare" ([7 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1315062624492322927)). Counting every EO (nissy `-a`), it happens on 0.018% of scrambles with NISS, never linearly in the sample [e]. kalindumaxxer asked "exluding htr equivalent variants" ([7 Dec 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1315059156046184611)); that convention is not counted here. |
| "I remember something like 200ish <=5 movers and 17 <=4 movers"; "the median for 4 or less is more like 14" | wen [12 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1250363326324543500); Lichi Fang [12 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1250367613356347464) | **True** as Cale's sheet of official scrambles counts them (NISS, all axes, nissy's default listing): "mean = 246", "median = 217" of at most 5, "mean: 17.3", "median: 14" of at most 4. On the first 150 uniform scrambles here, nissy's default NISS listing gives a mean of 242.9 and a median of 223.5 of at most 5, 17.1 and 14 of at most 4. Counting every EO (nissy `-a`, both directions of each last turn) gives more: normal only, 203.2 of at most 5 and 15.3 of at most 4 (median 12); with inverse and NISS EOs 646.4 and 43.9 (median 36). Of EOs that differ only in the directions of their last turns the default listing keeps one; on those scrambles that is 46.6% of the one-sided EOs of at most 5 and 22.4% of the two-sided ones, 37.8% in all, about two fifths (4.1). |
| "virtually all scrambles have some EO in 5" | Lewis Isom [17 Jun 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1252391829085622393) | **True**: none of at most 5 on 0.48% linearly, 0.012% with NISS [d]. |
| 12 bad on one axis: "1 in 2048"; 10 bad: "About 3% it seems", "close to 10% on a real scramble" | Aneurin [13 Apr 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1096002839890907156); wen [9 Aug 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1271343483147522069), [9 Aug 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1271354315990110292) | **True**: exact $1/2048$; 3.2% on one axis, 9.2% on some axis. |

The examples. Every move sequence here was replayed on the sticker model (appendix B).

**[a] No DR under 10, even with NISS.** The best DR on any axis, normal or inverse, is 10, and with NISS it's still 10. The scramble is 18 moves optimal.

```
F2 R2 U' F2 L2 F2 L2 U F2 D R2 D2 L2 U' R' U2 B D R' B F U B L2 U2  // scramble
L F R' D B2 L' B' U F D                                             // best DR with NISS (DR on R/L)
D' R2 D B' L' U2 L D' F' L' B U' L2 F' D' R2 B' L'                  // an optimal solution
```

A scramble with no sub-10 DR on its six linear tries that NISS gets under, 9 turns to DR on U/D:

```
R2 F2 L2 B2 D F2 L2 D2 L2 U F2 D B2 U' L' F' U B L D R B' L2 U'  // scramble
F B R' D' L' B (D F2 R)                                          // NISS DR on U/D
```

**[b] The superflip.** DR in 10 on each axis, normal and inverse, and 10 with NISS. No DR solution of 9 or fewer exists on the normal side; there are 9,216 of 10. Its shortest EO is 7 turns ✓ on every axis, also with NISS (the search of section 4 over every NISS split, and a short proof whose two facts Lean checks: the superflip commutes with every turn, so a NISS EO of it is a linear EO of the same length, and that linear EO needs 7).

```
U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2  // scramble
U D F L R' U2 F2 U F B                              // e.g. a DR on R/L
```

**[c] The optimal DR needs a long EO.** On the first scramble the optimal DR is 8 (U/D), and the shortest EO inside any optimal DR is 7 turns on F/B. Through a normal EO of at most 5 the best is 12.

```
D' R2 B2 D B2 L2 B2 R2 U2 F2 U F2 U2 R B' F D L R' B' F'  // scramble
F B R L' D' F' B R                                        // optimal DR (U/D)
L D F' B R'                                               // best route through a short EO: EO on R/L
D' F U2 D2 F R2 D                                         // then DR on F/B
```

On the second, both optimal DRs (10 turns) start with an EO of 9:

```
U' L2 B2 U' B2 D F2 U' L2 F2 D' F2 U L2 U' F' D F L B' R2 F U R B2 U'  // scramble
U2 L' B' D U' F D R L' D                                               // one of them
```

**[d] No EO in 5 at all.** No EO of at most 5 turns on any axis, normal, inverse or NISS (nissy `solve eo -N -a -M 5` lists none). An optimal NISS EO is 6.

```
U' B2 D2 U F2 D L2 B2 F2 U' B2 L2 D F' U2 R D' B L F R' D U  // scramble
U F B (D2 R' F)                                              // optimal NISS EO
```

**[e] More 3-move EOs than 4-move EOs.** Four 3-move EOs and no 4-move EO on any axis, normal, inverse or NISS.

```
L2 B2 D L2 U F2 D2 R2 U' F2 L2 U R2 U' F2 R' D' F' D' B' L D2 R F2 U'  // scramble
R (U2 R)
R (U2 R')
R' (U2 R)
R' (U2 R')                                                             // the four short EOs
```

**[f] An EO-breaking turn helps, rarely.** The EO (F/B) is the only EO solved and leaves 4c4e for DR on U/D: 7 keeping the EO, 6 breaking it.

```
R2 F' R U2 B2 D2 B F R' D F B' U' L' D B' F R2 L2 B F D'  // scramble
F' R L' B                                                 // EO (F/B), the only EO solved
D R2 D' L2 F2 U' R                                        // DR keeping the EO
R F R' B2 R F                                             // DR breaking it
```

**[g] The other options after an EO.**

The inverse. The EO (U/D) leaves 4c6e for DR on F/B, 9 on normal, 5 on the inverse:

```
U R2 D2 R2 U2 F2 L2 R2 U' L2 R2 L' U L R2 B D2 L' U2 R  // scramble
D2 L2 B' D                                              // EO
D2 L2 B' D (U2 F R B2 L)                                // EO, then DR on the inverse
```

The other axis. The EO (F/B) is 9 to DR on R/L but 5 on U/D:

```
B2 D' R2 U R2 U R2 B2 U2 L2 U R2 U' R2 U' B' D L2 D' L F L D' L  // scramble
F' B' U' F'                                                      // EO
L U R' D R                                                       // DR on U/D
```

The last turn. The EO (U/D) leaves 4c4e for R/L, 6 to DR; with the last turn switched it's 5:

```
L2 D2 U' F2 L2 U' L2 B2 U' R2 B2 L2 R' D L F' D F2 D' F2  // scramble
R' D2 L' D                                                // EO
D2 R2 B2 F2 L F                                           // DR
R' D2 L' D'                                               // EO, last turn switched
R2 B2 F2 L F                                              // DR after it
```

**[h] An EO 10 from DR.** The EO (R/L) leaves 3c8e for DR on F/B, and the shortest DR keeping the EO is 10. Only 0.29% of EO-solved states are this far. On the inverse this one is 8.

```
U2 B2 U' R2 U F2 U2 R2 B2 F2 R2 B2 U2 L' B D' U' L' R' F' L2 F'  // scramble
D L' B R                                                         // EO
F2 U F B' D B L2 F' L2 D                                         // shortest DR keeping the EO
D L' B R (B' D' B' R2 U B R2 U)                                  // EO, then DR on the inverse
```

**[i] Why the DR-skip count divides by 4!.** This position is in DR on U/D, with the four E-slice edges moved among themselves:

```
R2 L2 F2 B2  // scramble
```

Every order of the four slice edges in the slice is the same DR, so the placements count as $\binom{12}{4} = 495$, not $12!/8!$ = 11,880. The cosets of DR on one axis number $2^{11}\cdot 3^7\cdot 495$ = 2,217,093,120, the denominator of DougCube's "Going to DR" tab.

**[j] A 4c6e after an EO.** The EO (F/B) leaves 4c6e for DR on R/L; the shortest DR keeping the EO is 8, the most common length for 4c6e.

```
U B2 R2 U' R2 U B2 D' F2 R2 U L2 F2 L' U' R' F2 D F' R B R U'  // scramble
U B' R F'                                                      // EO
F2 D2 L' B2 R' U' R2 D                                         // shortest DR keeping the EO
```

One case shows nothing about averages: the averages are in Jay's DR-6e4c row of the claims table above and in appendix A (7.85 for 4c6e against 7.19 for 4c4e).

---

## 7. What this does not cover

- **Findability.** Every number is what exists: the best over every EO of a given length, every DR axis, every DR after it. How much of that you find in an hour isn't measured. The questions about how many DRs people find, check or should check (Aneurin [12 Apr 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1095654217387085836), Chris Choi [25 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1255237793911804008)) are answered only for what is there. Where a number needs a computer search to use (the optimal DR, the best DR after every EO, counts of hundreds of EOs), it is marked **computer only** where it appears.
- **RZPs.** EO-solved states are uniform over their cosets; the states a solver reaches after an RZP are not (torchlight's point in [8 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1215720321995382867)). So the 4c4e odds here are for a 4c4e straight off an EO, and KrzychXyz's question whether those are better than ones set up after the EO ([9 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1216123557776461895)) stays open. Switching the last move of the RZP rather than of the EO, which Cale measured as "slightly worse" ([9 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1216110077291925564)), I haven't redone.
- **More than the last EO turn.** Only the last quarter turn of the EO is switched. An EO that ends in `F B` can switch either; Cale's second sheet has that column; this study doesn't.
- **Full solutions.** The EO inside optimal full solutions (trig0n's estimate [5 Nov 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1038374075380273192), zakimoshi's question [30 Apr 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1102210756419784785), LiamDaBestest's [13 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1261651208775405568)) is a different quantity from the EO inside the optimal DR measured here.
- **Official scrambles.** Everything is on uniformly random states. Official scrambles are random-state too, but the counts people quote from Cale's and Tzak's sheets of official scrambles (and the official records) are not recomputed.
- **ARM and pairs.** Cases are by DRM only; the ARM, pairs and corner-case tables of Louis, Evan and Rodney Kinney are not extended (beyond the second DR axis, which they did not have).
- **Finishes.** Nothing here goes past DR.
- **The exact NISS EO counts per scramble** (Radek B's question, [15 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1516080351338827797)) are sampled, not exact, except for one axis linearly.

---

## Appendix A: full tables

**EO to DR by case**, all 40 cases but 0c0e (already a DR), in three tables: how common each case is, the mean turns to DR with each option, and the chance of a DR in 6 or fewer with each option. One axis, any turns and the last turn either way are exact over all 1,082,565 EO-solved states; the better of two DR axes is exact (read by the case on the first axis); normal or inverse and all EO-keeping options together are sampled (10,000,000 states; the last column gives how many fell in each case, and the cases marked *few* rest on about 300 to 1,000). The share and odds, and the one-axis and last-turn columns, are proved in Lean ✓: each printed value is Lean's exact count, rounded (appendix B). In the cases with no edge out of place (2c0e to 8c0e) the other EO is solved as well, so their any-turn column is not about EO-breaking turns: wherever any turns are shorter there (485 of their 2,186 states), a DR as short keeps the other EO.

Each row is a case: its share of EO-solved states, and how many of the sampled states fell in it.

| Case on the DR axis | Share of EO-solved states | Odds | States sampled (normal or inverse, all EO-keeping options) |
|---|---:|---:|---:|
| 6c6e | 12.7% | 1 in 7.8 | 1,274,785 |
| 5c6e | 11.6% | 1 in 8.6 | 1,157,431 |
| 6c4e | 9.6% | 1 in 10.5 | 957,958 |
| 4c6e | 8.7% | 1 in 11.5 | 868,439 |
| 5c4e | 8.7% | 1 in 11.5 | 869,787 |
| 7c6e | 7.0% | 1 in 14.4 | 694,211 |
| 4c4e | 6.5% | 1 in 15.3 | 652,018 |
| 7c4e | 5.2% | 1 in 19.2 | 520,005 |
| 6c8e | 4.0% | 1 in 25.1 | 397,422 |
| 5c8e | 3.6% | 1 in 27.6 | 362,239 |
| 4c8e | 2.7% | 1 in 36.8 | 272,394 |
| 3c6e | 2.3% | 1 in 43.2 | 232,084 |
| 7c8e | 2.2% | 1 in 46.0 | 218,132 |
| 6c2e | 1.8% | 1 in 54.9 | 182,237 |
| 8c6e | 1.8% | 1 in 56.2 | 177,952 |
| 3c4e | 1.7% | 1 in 57.5 | 173,359 |
| 5c2e | 1.7% | 1 in 60.4 | 165,385 |
| 8c4e | 1.3% | 1 in 74.9 | 133,037 |
| 4c2e | 1.2% | 1 in 80.5 | 125,012 |
| 2c6e | 1.2% | 1 in 86.3 | 115,310 |
| 7c2e | 0.99% | 1 in 100.7 | 99,427 |
| 2c4e | 0.87% | 1 in 115.1 | 86,873 |
| 3c8e | 0.72% | 1 in 138.1 | 72,416 |
| 8c8e | 0.56% | 1 in 179.8 | 55,365 |
| 2c8e | 0.36% | 1 in 276.2 | 36,388 |
| 3c2e | 0.33% | 1 in 302.1 | 32,985 |
| 8c2e | 0.25% | 1 in 393.4 | 25,531 |
| 2c2e | 0.17% | 1 in 604.1 | 16,832 |
| 6c0e | 0.057% | 1 in 1,757.4 | 5,686 |
| 5c0e | 0.052% | 1 in 1,933.2 | 5,255 |
| 4c0e | 0.039% | 1 in 2,577.5 | 3,983 |
| 7c0e | 0.031% | 1 in 3,221.9 | 3,140 |
| 0c6e | 0.021% | 1 in 4,832.9 | 2,048 |
| 0c4e | 0.016% | 1 in 6,443.8 | 1,575 |
| 3c0e | 0.010% | 1 in 9,665.8 | 1,019 (few) |
| 8c0e | 0.0079% | 1 in 12,588.0 | about 794 (few) |
| 0c8e | 0.0065% | 1 in 15,465.2 | about 647 (few) |
| 2c0e | 0.0052% | 1 in 19,331.5 | about 517 (few) |
| 0c2e | 0.0030% | 1 in 33,830.2 | about 296 (few) |

Mean turns to DR, one column per option:

| Case on the DR axis | Mean turns: one axis, EO kept | Mean turns: any turns | Mean turns: last EO turn either way, EO kept | Mean turns: better of 2 DR axes | Mean turns: normal or inverse | Mean turns: all EO-keeping options |
|---|---:|---:|---:|---:|---:|---:|
| 6c6e | 7.73 | 7.73 | 7.47 | 7.39 | 7.35 | 6.89 |
| 5c6e | 7.69 | 7.69 | 7.42 | 7.34 | 7.29 | 6.83 |
| 6c4e | 7.97 | 7.96 | 7.71 | 7.51 | 7.59 | 7.01 |
| 4c6e | 7.85 | 7.84 | 7.58 | 7.43 | 7.45 | 6.92 |
| 5c4e | 7.60 | 7.59 | 7.33 | 7.26 | 7.21 | 6.75 |
| 7c6e | 7.82 | 7.82 | 7.57 | 7.46 | 7.46 | 6.98 |
| 4c4e | 7.19 | 7.18 | 6.90 | 6.95 | 6.71 | 6.37 |
| 7c4e | 8.10 | 8.09 | 7.84 | 7.61 | 7.73 | 7.13 |
| 6c8e | 7.90 | 7.90 | 7.63 | 7.49 | 7.53 | 7.00 |
| 5c8e | 8.08 | 8.08 | 7.82 | 7.59 | 7.73 | 7.12 |
| 4c8e | 8.48 | 8.48 | 8.24 | 7.79 | 8.17 | 7.32 |
| 3c6e | 7.84 | 7.84 | 7.58 | 7.41 | 7.45 | 6.89 |
| 7c8e | 7.25 | 7.25 | 6.98 | 7.07 | 6.80 | 6.51 |
| 6c2e | 8.27 | 8.25 | 8.05 | 7.68 | 7.97 | 7.21 |
| 8c6e | 8.08 | 8.07 | 7.86 | 7.61 | 7.74 | 7.16 |
| 3c4e | 7.45 | 7.43 | 7.18 | 7.11 | 7.06 | 6.60 |
| 5c2e | 7.86 | 7.82 | 7.63 | 7.42 | 7.53 | 6.94 |
| 8c4e | 8.42 | 8.39 | 8.17 | 7.78 | 8.06 | 7.32 |
| 4c2e | 7.16 | 7.15 | 6.89 | 6.92 | 6.72 | 6.37 |
| 2c6e | 8.27 | 8.27 | 8.05 | 7.67 | 7.96 | 7.21 |
| 7c2e | 8.55 | 8.53 | 8.30 | 7.85 | 8.23 | 7.38 |
| 2c4e | 7.54 | 7.53 | 7.28 | 7.18 | 7.19 | 6.68 |
| 3c8e | 8.56 | 8.56 | 8.33 | 7.84 | 8.23 | 7.38 |
| 8c8e | 7.23 | 7.23 | 6.98 | 7.05 | 6.83 | 6.55 |
| 2c8e | 8.95 | 8.94 | 8.76 | 8.05 | 8.71 | 7.58 |
| 3c2e | 6.16 | 6.16 | 5.88 | 6.09 | 5.70 | 5.49 |
| 8c2e | 8.77 | 8.74 | 8.54 | 7.98 | 8.43 | 7.50 |
| 2c2e | 6.88 | 6.88 | 6.65 | 6.67 | 6.56 | 6.21 |
| 6c0e | 8.96 | 8.78 | 8.82 | 7.96 | 8.78 | 7.44 |
| 5c0e | 8.04 | 7.80 | 7.93 | 7.59 | 7.84 | 7.16 |
| 4c0e | 7.39 | 7.19 | 7.13 | 7.08 | 7.03 | 6.61 |
| 7c0e | 8.76 | 8.43 | 8.55 | 8.06 | 8.53 | 7.63 |
| 0c6e | 8.21 | 8.21 | 8.05 | 7.77 | 7.90 | 7.39 |
| 0c4e | 6.45 | 6.45 | 6.17 | 6.35 | 6.05 | 5.78 |
| 3c0e | 7.29 | 7.00 | 7.07 | 6.99 | 7.10 | 6.64 |
| 8c0e | 8.98 | 8.77 | 8.79 | 8.12 | 8.59 | 7.64 |
| 0c8e | 8.94 | 8.94 | 8.77 | 8.23 | 8.63 | 7.77 |
| 2c0e | 6.00 | 5.86 | 5.71 | 5.89 | 5.55 | 5.27 |
| 0c2e | 5.75 | 5.75 | 5.63 | 5.68 | 5.57 | 5.39 |

Chance of a DR in 6 or fewer, one column per option:

| Case on the DR axis | DR in ≤ 6: one axis, EO kept | DR in ≤ 6: any turns | DR in ≤ 6: last EO turn either way, EO kept | DR in ≤ 6: better of 2 DR axes | DR in ≤ 6: normal or inverse | DR in ≤ 6: all EO-keeping options |
|---|---:|---:|---:|---:|---:|---:|
| 6c6e | 5.6% | 5.6% | 9.4% | 10.6% | 10.8% | 25.1% |
| 5c6e | 6.1% | 6.1% | 10.2% | 11.7% | 11.9% | 27.2% |
| 6c4e | 3.0% | 3.0% | 5.3% | 8.5% | 5.9% | 20.5% |
| 4c6e | 4.6% | 4.6% | 7.7% | 10.3% | 9.0% | 24.2% |
| 5c4e | 7.2% | 7.3% | 12.2% | 13.6% | 14.0% | 31.4% |
| 7c6e | 4.0% | 4.0% | 6.7% | 8.6% | 7.9% | 20.9% |
| 4c4e | 19.2% | 19.3% | 28.1% | 25.4% | 34.8% | 51.1% |
| 7c4e | 2.2% | 2.2% | 3.8% | 6.6% | 4.4% | 16.1% |
| 6c8e | 3.2% | 3.2% | 5.6% | 8.1% | 6.3% | 19.7% |
| 5c8e | 1.4% | 1.4% | 2.6% | 6.2% | 2.8% | 15.5% |
| 4c8e | 0.27% | 0.27% | 0.49% | 4.6% | 0.54% | 11.4% |
| 3c6e | 4.8% | 4.8% | 7.8% | 10.9% | 9.3% | 25.2% |
| 7c8e | 16.4% | 16.4% | 24.4% | 20.5% | 30.3% | 43.8% |
| 6c2e | 0.16% | 0.16% | 0.32% | 5.8% | 0.33% | 14.1% |
| 8c6e | 1.2% | 1.2% | 2.1% | 5.8% | 2.4% | 14.4% |
| 3c4e | 9.9% | 10.1% | 15.9% | 18.2% | 19.0% | 39.6% |
| 5c2e | 2.3% | 2.5% | 4.3% | 9.5% | 4.5% | 22.3% |
| 8c4e | 0.72% | 0.72% | 1.2% | 4.6% | 1.4% | 11.2% |
| 4c2e | 18.7% | 19.2% | 27.2% | 26.2% | 33.8% | 51.9% |
| 2c6e | 0.13% | 0.13% | 0.26% | 6.0% | 0.25% | 14.4% |
| 7c2e | 0.30% | 0.30% | 0.60% | 4.2% | 0.60% | 10.6% |
| 2c4e | 6.2% | 6.2% | 10.7% | 15.1% | 11.9% | 33.5% |
| 3c8e | 0.41% | 0.41% | 0.77% | 4.3% | 0.75% | 10.4% |
| 8c8e | 14.5% | 14.5% | 23.5% | 19.2% | 26.9% | 42.5% |
| 2c8e | 0% | 0% | 0% | 3.2% | 0% | 7.8% |
| 3c2e | 61.6% | 61.6% | 77.0% | 66.0% | 85.5% | 93.4% |
| 8c2e | 0% | 0% | 0% | 3.2% | 0% | 8.5% |
| 2c2e | 23.7% | 23.7% | 35.9% | 34.5% | 41.5% | 63.7% |
| 6c0e | 0% | 0% | 0% | 4.8% | 0% | 12.0% |
| 5c0e | 0% | 0% | 0% | 6.3% | 0% | 15.1% |
| 4c0e | 7.6% | 15.2% | 13.3% | 17.2% | 14.3% | 36.7% |
| 7c0e | 0% | 0% | 0% | 2.8% | 0% | 6.9% |
| 0c6e | 0% | 0% | 0% | 4.5% | 0% | 10.4% |
| 0c4e | 47.6% | 47.6% | 64.3% | 53.1% | 72.1% | 84.4% |
| 3c0e | 0% | 0% | 0% | 13.5% | 0% | 30.6% |
| 8c0e | 1.2% | 2.3% | 1.2% | 3.4% | 2.4% | 6.5% |
| 0c8e | 1.4% | 1.4% | 1.4% | 3.0% | 3.0% | 5.6% |
| 2c0e | 71.4% | 71.4% | 85.7% | 77.1% | 92.9% | 98.5% |
| 0c2e | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

**Normal against inverse after an EO**, by case (sampled, 10,000,000 states, same DR axis, EO kept). Cases with fewer than 1,000 samples have noisy correlations. Each row is a case; the last three columns are the chance the inverse is at most 6:

| Case | States sampled | Correlation, normal against inverse | Inverse DR in ≤ 6 when normal is 6 | Inverse DR in ≤ 6 when normal is 8 | Inverse DR in ≤ 6, any normal |
|---|---:|---:|---:|---:|---:|
| all | 10,000,000 | 0.1684 | 11.2% | 5.3% | 5.9% |
| 0c4e | 1,575 | -0.0148 | 45.4% | – | 46.0% |
| 0c6e | 2,048 | -0.0012 | – | 0% | 0% |
| 2c2e | 16,832 | -0.0047 | 22.5% | 23.0% | 23.2% |
| 2c4e | 86,873 | -0.0023 | 6.0% | 6.3% | 6.2% |
| 2c6e | 115,310 | -0.0034 | – | 0.15% | 0.13% |
| 2c8e | 36,388 | 0.0021 | – | 0% | 0% |
| 3c0e | 1,019 | 0.0273 | – | 0% | 0% |
| 3c2e | 32,985 | -0.0018 | 61.4% | 59.0% | 61.7% |
| 3c4e | 173,359 | 0.0006 | 10.1% | 10.0% | 10.0% |
| 3c6e | 232,084 | 0.0001 | 5.0% | 4.7% | 4.8% |
| 3c8e | 72,416 | -0.0027 | 0.37% | 0.36% | 0.38% |
| 4c0e | 3,983 | -0.0035 | 9.0% | 7.9% | 8.2% |
| 4c2e | 125,012 | 0.0036 | 18.8% | 18.7% | 18.6% |
| 4c4e | 652,018 | -0.0016 | 19.2% | 19.3% | 19.2% |
| 4c6e | 868,439 | 0.0003 | 4.8% | 4.6% | 4.6% |
| 4c8e | 272,394 | 0.0011 | 0.14% | 0.30% | 0.28% |
| 5c0e | 5,255 | -0.0111 | – | 0% | 0% |
| 5c2e | 165,385 | -0.0004 | 2.6% | 2.3% | 2.3% |
| 5c4e | 869,787 | 0.0009 | 7.2% | 7.2% | 7.2% |
| 5c6e | 1,157,431 | 0.002 | 6.3% | 6.1% | 6.1% |
| 5c8e | 362,239 | -0.0012 | 1.4% | 1.4% | 1.4% |
| 6c0e | 5,686 | -0.0097 | – | 0% | 0% |
| 6c2e | 182,237 | 0.0162 | 0.64% | 0.15% | 0.16% |
| 6c4e | 957,958 | 0.0021 | 3.0% | 3.0% | 3.0% |
| 6c6e | 1,274,785 | 0.0167 | 6.0% | 5.5% | 5.6% |
| 6c8e | 397,422 | 0.0282 | 4.1% | 3.2% | 3.2% |
| 7c0e | 3,140 | 0.0026 | – | 0% | 0% |
| 7c2e | 99,427 | 0.0006 | 0.32% | 0.31% | 0.29% |
| 7c4e | 520,005 | -0.0006 | 2.1% | 2.2% | 2.2% |
| 7c6e | 694,211 | -0.0024 | 4.0% | 4.1% | 4.0% |
| 7c8e | 218,132 | -0.0055 | 16.4% | 16.5% | 16.4% |
| 8c2e | 25,531 | 0.0628 | – | 0% | 0% |
| 8c4e | 133,037 | 0.0159 | 1.1% | 0.75% | 0.71% |
| 8c6e | 177,952 | 0.0063 | 1.5% | 1.2% | 1.2% |
| 8c8e | 55,365 | 0.0032 | 14.4% | 14.4% | 14.5% |

**Bad edges on the three axes**, all 65 sorted triples, exact over all 70,963,200 classes of edge states (orientation and slice placement). Each row is a set of bad-edge counts on the three axes, in any order:

| Bad edges on the three axes (sorted) | Probability (exact) | As a percentage |
|---|---:|---:|
| 4/6/6 | $218033/1478400$ | 14.7% |
| 6/6/8 | $218033/1478400$ | 14.7% |
| 4/6/8 | $8539/61600$ | 13.9% |
| 6/6/6 | $815891/8870400$ | 9.2% |
| 4/4/6 | $43721/492800$ | 8.9% |
| 6/8/8 | $43721/492800$ | 8.9% |
| 4/4/8 | $1101/30800$ | 3.6% |
| 4/8/8 | $1101/30800$ | 3.6% |
| 2/4/6 | $3177/123200$ | 2.6% |
| 6/8/10 | $3177/123200$ | 2.6% |
| 4/4/4 | $1483843/70963200$ | 2.1% |
| 8/8/8 | $1483843/70963200$ | 2.1% |
| 2/6/6 | $9829/492800$ | 2.0% |
| 6/6/10 | $9829/492800$ | 2.0% |
| 2/6/8 | $249/15400$ | 1.6% |
| 4/6/10 | $249/15400$ | 1.6% |
| 2/4/4 | $2627/246400$ | 1.1% |
| 8/8/10 | $2627/246400$ | 1.1% |
| 2/4/8 | $1017/123200$ | 0.83% |
| 4/8/10 | $1017/123200$ | 0.83% |
| 2/8/8 | $257/70400$ | 0.37% |
| 4/4/10 | $257/70400$ | 0.37% |
| 2/2/4 | $261/123200$ | 0.21% |
| 8/10/10 | $261/123200$ | 0.21% |
| 2/2/6 | $3851/1971200$ | 0.20% |
| 6/10/10 | $3851/1971200$ | 0.20% |
| 2/6/10 | $1333/985600$ | 0.14% |
| 2/4/10 | $3/5600$ | 0.054% |
| 2/8/10 | $3/5600$ | 0.054% |
| 2/2/8 | $647/1478400$ | 0.044% |
| 4/10/10 | $647/1478400$ | 0.044% |
| 0/4/6 | $51/123200$ | 0.041% |
| 6/8/12 | $51/123200$ | 0.041% |
| 0/6/6 | $157/492800$ | 0.032% |
| 6/6/12 | $157/492800$ | 0.032% |
| 0/6/8 | $13/61600$ | 0.021% |
| 4/6/12 | $13/61600$ | 0.021% |
| 0/4/4 | $393/1971200$ | 0.020% |
| 8/8/12 | $393/1971200$ | 0.020% |
| 2/2/2 | $6301/35481600$ | 0.018% |
| 10/10/10 | $6301/35481600$ | 0.018% |
| 0/2/4 | $1/11200$ | 0.0089% |
| 0/4/8 | $1/11200$ | 0.0089% |
| 4/8/12 | $1/11200$ | 0.0089% |
| 8/10/12 | $1/11200$ | 0.0089% |
| 0/2/6 | $23/369600$ | 0.0062% |
| 6/10/12 | $23/369600$ | 0.0062% |
| 0/8/8 | $417/7884800$ | 0.0053% |
| 4/4/12 | $417/7884800$ | 0.0053% |
| 2/2/10 | $61/3942400$ | 0.0015% |
| 2/10/10 | $61/3942400$ | 0.0015% |
| 0/2/2 | $1/70400$ | 0.0014% |
| 10/10/12 | $1/70400$ | 0.0014% |
| 0/2/8 | $1/123200$ | 0.0008% |
| 4/10/12 | $1/123200$ | 0.0008% |
| 0/0/4 | $3/1971200$ | 0.0002% |
| 8/12/12 | $3/1971200$ | 0.0002% |
| 0/0/2 | $1/1478400$ | 0.0001% |
| 0/0/6 | $1/1478400$ | 0.0001% |
| 6/12/12 | $1/1478400$ | 0.0001% |
| 10/12/12 | $1/1478400$ | 0.0001% |
| 0/0/8 | $1/23654400$ | < 0.0001% |
| 4/12/12 | $1/23654400$ | < 0.0001% |
| 0/0/0 | $1/70963200$ | < 0.0001% |
| 12/12/12 | $1/70963200$ | < 0.0001% |

## Appendix B: how it was computed, and what checks it

**The model.** The cube is the one of the DR-xs study (`is-dr-xs-worth-it/research/xstools/src/cubie.rs`, whose move tables come from a sticker model built from geometry), used unchanged by the Rust tool of this study (`research/eodrtools`). DR on U/D is a coset of the DR group, indexed by corner orientation (2,187), the F/B edge orientation (2,048) and the places of the four E-slice edges (495): 2,217,093,120 cosets. Two exact distance tables from the DR-xs study are reused: fewest turns of any kind to DR on U/D, and fewest turns without F/B quarter turns (keeping F/B EO). Every other DR axis and EO axis is read through a rotation of the cube, and every such mapping is checked against nissy (below). For EO to DR only the EO-solved part of each table is needed (1,082,565 states each).

**The scrambles.** 50,000 uniformly random states, drawn by the study itself (`eodrtools mkscr`, seed 2026) and written as move sequences of about 23 turns. nissy 2.0.8's `scramble` isn't used, because it's biased. Its source (`src/commands.c`, lines 505 to 508) draws a random state as

    eo = rand() % POW2TO11;
    ep = rand() % FACTORIAL12;
    co = rand() % POW3TO7;
    cp = rand() % FACTORIAL8;

and prints a solution of it as the scramble. glibc's `rand()` takes $2^{31}$ values, 4.48 ✓ times $12!$, so `rand() % FACTORIAL12` gives the lowest 231,477,248 ✓ edge-permutation indices (48.3% ✓ of them) one chance more than the rest: they are 25% ✓ more likely. The other three draws are over ranges small enough that the same bias is negligible. Since the scramble solves the drawn state, the drawn state is the inverse of the scramble, and that is where the effect shows: on 50,000 nissy scrambles the inverse side is shorter to DR, the normal side barely moved. Each row is one way of reaching DR; the *DR in ≤* columns are the share of scrambles:

| Shortest DR (50,000 scrambles each) | Mean turns, uniform | Mean turns, nissy scramble | DR in ≤ 8, uniform | DR in ≤ 8, nissy scramble | DR in ≤ 9, uniform | DR in ≤ 9, nissy scramble |
|---|---:|---:|---:|---:|---:|---:|
| One fixed axis, normal (each of the 3 axes) | 9.53 | 9.50 | 6.2% | 6.7% | 43.1% | 45.1% |
| Best of 3 axes, normal | 9.05 | 9.02 | 16.5% | 17.8% | 76.5% | 78.5% |
| Best of 3 axes, inverse | 9.05 | 8.87 | 16.6% | 23.7% | 76.9% | 85.9% |
| Best of 6: 3 axes, normal or inverse | 8.76 | 8.65 | 28.4% | 34.8% | 91.5% | 95.0% |
| NISS: 3 axes, moves on both sides | 8.46 | 8.40 | 47.5% | 52.3% | 99.1% | 99.4% |

The number of twisted corners per axis is also off on nissy's scrambles, on 7 degrees of freedom; I haven't found the cause. Each row is an axis, with the test statistic and its p-value:

| Axis | $\chi^2$ | p-value |
|---|---|---|
| R/L | 33.2 | $2\cdot 10^{-5}$ |
| U/D | 34.9 | $1\cdot 10^{-5}$ |
| F/B | 17.8 | 0.01 |

The test of every scramble set (twisted corners, bad edges and slice pieces in their slice, on each axis). Each row is one scramble set, axis and count:

| Scrambles | Axis | What is counted | $\chi^2$ | Degrees of freedom |
|---|---:|---:|---:|---:|
| this study, uniform states (50,000) | R/L | twisted corners | 9.8 | 7 |
| this study, uniform states (50,000) | R/L | bad edges | 5.8 | 6 |
| this study, uniform states (50,000) | R/L | slice pieces in slice | 1.0 | 4 |
| this study, uniform states (50,000) | U/D | twisted corners | 4.1 | 7 |
| this study, uniform states (50,000) | U/D | bad edges | 1.4 | 6 |
| this study, uniform states (50,000) | U/D | slice pieces in slice | 2.8 | 4 |
| this study, uniform states (50,000) | F/B | twisted corners | 7.5 | 7 |
| this study, uniform states (50,000) | F/B | bad edges | 4.5 | 6 |
| this study, uniform states (50,000) | F/B | slice pieces in slice | 3.2 | 4 |
| nissy 2.0.8 `scramble` (50,000) | R/L | twisted corners | 33.2 | 7 |
| nissy 2.0.8 `scramble` (50,000) | R/L | bad edges | 1.3 | 6 |
| nissy 2.0.8 `scramble` (50,000) | R/L | slice pieces in slice | 0.8 | 4 |
| nissy 2.0.8 `scramble` (50,000) | U/D | twisted corners | 34.9 | 7 |
| nissy 2.0.8 `scramble` (50,000) | U/D | bad edges | 13.5 | 6 |
| nissy 2.0.8 `scramble` (50,000) | U/D | slice pieces in slice | 13.5 | 4 |
| nissy 2.0.8 `scramble` (50,000) | F/B | twisted corners | 17.8 | 7 |
| nissy 2.0.8 `scramble` (50,000) | F/B | bad edges | 11.0 | 6 |
| nissy 2.0.8 `scramble` (50,000) | F/B | slice pieces in slice | 2.3 | 4 |
| judging-a-dr's 500 (500) | R/L | twisted corners | 4.8 | 6 |
| judging-a-dr's 500 (500) | R/L | bad edges | 3.3 | 4 |
| judging-a-dr's 500 (500) | R/L | slice pieces in slice | 1.5 | 3 |
| judging-a-dr's 500 (500) | U/D | twisted corners | 6.8 | 6 |
| judging-a-dr's 500 (500) | U/D | bad edges | 1.5 | 4 |
| judging-a-dr's 500 (500) | U/D | slice pieces in slice | 2.4 | 3 |
| judging-a-dr's 500 (500) | F/B | twisted corners | 3.7 | 6 |
| judging-a-dr's 500 (500) | F/B | bad edges | 1.6 | 4 |
| judging-a-dr's 500 (500) | F/B | slice pieces in slice | 2.9 | 3 |

The study's own scrambles pass every test. A separate set of 500 scrambles from nissy's scrambler shows the same effect. Each row is a mean number of turns to DR; z is how many standard errors those scrambles sit from the uniform sample:

| Mean to DR | Those scrambles, mean turns | Standard error | Uniform sample, mean turns | z |
|---|---|---|---|---|
| Inverse, best of 3 | 8.894 | 0.031 | 9.05 | -4.8 |
| Best of six | 8.672 | 0.030 | 8.76 | -3.0 |
| Normal side (unaffected) | 9.054 | | 9.05 | |

**Per scramble** (`eodrtools scr`): the exact DR distance on each axis, normal and inverse; the NISS DR (pre-turns on one side, stopping where they can no longer win); the number of DR solutions of each length up to 12 on the normal side; the shortest EO inside an optimal DR; every EO of up to 6 turns on each axis, normal, inverse and NISS, each with the exact EO-keeping DR distance on both DR axes; from these the best route through an EO of each length, the (EO, DR axis) counts and the optimal EOs. About 30 minutes on four cores for the 50,000.

**EO to DR** (`eodrtools eodr`): the per-coset tables directly (one axis, any turns, the last EO turn either way), the better of two DR axes exactly over every corner state and every placement of the E- and M-slice pieces, and the options that need the inverse sampled on 10,000,000 uniform EO-solved states with exact lookups.

**Scramble to EO** (`eodrtools eo`): EO distances on one axis exactly (2,048 states), the bad-edge layouts exactly over the 34,650 slice placements times 2,048 flip patterns, and NISS EOs sampled on 1,000,000 random states.

**What checks it.**

- Every table mapping against nissy 2.0.8: 19,000 of 19,000 positions agree, over 16 mappings (DR from a scramble on each axis, EO-keeping DR for all six pairs of EO axis and DR axis, any-turn DR from EO-solved states, optimal EO per axis, NISS EO over all axes). Each row is one mapping:

| Table checked | nissy step | Positions compared | Positions that agree |
|---|---:|---:|---:|
| dr | drrl | 1,000 | 1,000 |
| dr | drud | 1,000 | 1,000 |
| dr | drfb | 1,000 | 1,000 |
| eo | eorl | 1,000 | 1,000 |
| eo | eoud | 1,000 | 1,000 |
| eo | eofb | 1,000 | 1,000 |
| eoniss | eo -N | 1,000 | 1,000 |
| eodr | drud-eorl | 1,000 | 1,000 |
| eoany | drud | 2,000 | 2,000 |
| eodr | drfb-eorl | 1,000 | 1,000 |
| eoany | drfb | 2,000 | 2,000 |
| eodr | drrl-eoud | 1,000 | 1,000 |
| eoany | drrl | 2,000 | 2,000 |
| eodr | drfb-eoud | 1,000 | 1,000 |
| eodr | drrl-eofb | 1,000 | 1,000 |
| eodr | drud-eofb | 1,000 | 1,000 |

- Counts against nissy on the first 30 scrambles (DR solutions of 9 and 10, EOs linear and NISS, `nissy -a`), and the NISS DR against `nissy solve dr -N` on 40 scrambles where NISS beats linear. Each row is one count:

| Count checked | Scrambles compared | Scrambles that agree |
|---|---:|---:|
| drud count of exactly 9 | 30 | 30 |
| drud count of exactly 10 | 30 | 30 |
| eofb linear count of exactly 4 | 30 | 30 |
| eofb nissy-default count of exactly 4 | 30 | not a check: nissy default lists 63 EOs where -a lists 138 |
| eofb linear count of exactly 5 | 30 | 30 |
| eofb nissy-default count of exactly 5 | 30 | not a check: nissy default lists 872 EOs where -a lists 1874 |
| eofb linear count of exactly 6 | 30 | 30 |
| eofb nissy-default count of exactly 6 | 30 | not a check: nissy default lists 11414 EOs where -a lists 24584 |
| eofb NISS count of exactly 4 | 30 | 30 |
| eofb NISS count of exactly 5 | 30 | 30 |
| dr best of 6 (nissy dr -L) | 30 | 30 |
| dr NISS (nissy dr -N), scrambles where NISS ≤ 7 beats linear | 40 | 40 |

- The known tables come out exactly: the EO-solved part of the EO-keeping table is FakeMMAP's and Cale's 1, 2, 17, …, 3114 (mean 7.803); the any-turn version gives torchlight's 7.797; one-axis EO 4.609; DougCube's one-axis DR from a scramble, mean 9.52. The sample agrees with the exact one-axis table (mean 9.53 on 150,000 axes; $\chi^2$ 5.94 on 6 df), and with the DR-xs study's 2,000,000 scrambles (best of three, $\chi^2$ 9.85 on 6 df; best of six, 9.47 on 5).
- The sampled EO to DR rows agree with the exact ones where both exist (one axis: 7.8026 sampled against 7.8031 exact).
- Every solution in the per-scramble tables (NISS DR, optimal DR with its EO split, the best routes through EOs of at most 4, 5 and 6) is replayed on the sticker model, a separate implementation that reads EO and DR off the stickers; so is every example in this write-up (56 checks) and every move sequence on the examples page.
- The optimal solutions of the first three scrambles with no sub-10 DR (nissy `solve optimal`, about 3.5 GB) are replayed and solve the cube.
- **Lean** (`lean/EODR`, Lean 4, no Mathlib; its README lists every theorem). **Proved**, marked ✓ in the text: Lean builds the cube from its geometry, redoes each search itself, and checks every distance table with an independent rule.
  - One-axis EO, all 2,048 states: the distances (mean 4.609), by bad-edge count (Shota's table, 8 against 6 bad, the 10- and 12-bad rows), and the EO counts per state.
  - The bad-edge layouts over all 70,963,200 classes: torchlight's counts, every triple, the shares of section 6.
  - EO to DR over all 1,082,565 EO-solved states, one axis and the EO's last turn either way: the distribution (Cale's and FakeMMAP's), the 3,114 at 10, the 5.9% in 6, every per-case figure quoted, and every value in the share, odds, one-axis and last-turn columns of the case tables (section 5 and appendix A). That check found three values rounded twice (7c6e and 6c2e with the last turn, 0c4e's share), now fixed. Also the corner-twist counts (Emma's and Zagros's).
  - The superflip has no NISS EO under 7 on any axis: it commutes with every face turn, so any NISS EO of it is a linear EO of the same length.
  - Arithmetic: nissy's modulo bias, the binomials (Lichi Fang's 3 of 27, DougCube's 92.71%), the coset count.
  - The errata examples (the EO 10 from DR, the 4c6e, the superflip's NISS EO) are checked on the Lean cube too (`htr-routes/lean/FakeBound/Corrections`).

  **Computed, not proved**: everything sampled (the 50,000 scrambles, the 1,000,000 EO states, the 10,000,000 EO-solved states: every NISS, inverse and all-options row); the any-turn tables over 2,217,093,120 cosets (torchlight's 7.797, DougCube's 9.52, Louis's shares); the better of two DR axes (exact, but in Rust only); the optimal solves; the measurements of nissy's scrambles.

`research/README.md` lists every step, its command, its input and output, and how long it takes; `research/out/SUMMARY.md` has every number the tables are made from.

## Docs referred to

- Cale, [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0), and [*DR setup stats (switching last move)*](https://docs.google.com/spreadsheets/d/1_2PmFv1KyBX335SjSb4oweS0sx804fIhbuP50D-gBj4).
- Louis, [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs), code at [github.com/LouisSart/DRM-ARM-stats](https://github.com/LouisSart/DRM-ARM-stats).
- KrzychXyz, [*All EO-> DR cases*](https://docs.google.com/spreadsheets/d/1dNjuqAW0wTbP3qeV5aSfo1KbrVlfvCk0_0DOfsUiJLk).
- Evan, [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk).
- Rodney Kinney, [*DRM corner variant+pair stats*](https://docs.google.com/spreadsheets/d/174ClwBFl-T2zJAq8MVyK1bKsIIuzxQU0_XmQGv82LPQ); [*Multi-Axis DR*](https://docs.google.com/spreadsheets/d/1fYdYEGlBk3bv5x2WVSA0NtsPWVlNKbtyK-Iq-J6VjDY).
- DougCube, [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo).
- Cale, [*Official 5 move EO counts*](https://docs.google.com/spreadsheets/d/1jLDRWYn31ou-Br3ReNVH7EnDYPovMZLIpuCWWZEBCO8) (official scrambles to April 2023).
- torchlight, the exact bad-edge counts on the three axes: [Probability Thread, post 1520621](https://www.speedsolving.com/threads/probability-thread.20384/post-1520621) (speedsolving.com).
- Kociemba, [*Distribution of the Pruning Values*](https://kociemba.org/math/distribution.htm) (the phase-1 table, by symmetry classes, not positions).
- nissy 2.0.8, by Sebastiano Tronto ([nissy.tronto.net](https://nissy.tronto.net)), used for the cross-checks.
