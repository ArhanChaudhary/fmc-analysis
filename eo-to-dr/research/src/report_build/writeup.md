# EO to DR, and scramble to DR

How far a random scramble is from DR: on one axis, on the best of three, with the inverse, with NISS, and through the short EOs a solver actually writes down. How many EOs a scramble has and how short. And what an EO leaves: how far DR is with the other DR axis, the inverse, the EO's last turn the other way and EO-breaking turns, case by case. Every distance is exact (from full distance tables). Where a number is a sample it says so: {= n(X('n')) =} uniformly random scrambles for the scramble-level questions, {= NSAMP('b') =} random states for the shortest EOs, and {= NSAMP('c') =} EO-solved states for the EO to DR options that need the inverse.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion). Docs and sheets are listed with links at the end.

**This builds on** what the server already had:

- **Cale's [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0)** (posted by Aneurin, [[D348]]: "This has a bunch of useful stats for dr"), the per-case EO to DR table everyone uses: every EO-solved state on one DR axis, "I used the moveset <U, D, R, L, F2, B2>, so sequences that break EO like F R B2 R' F' aren't considered", average {= f2(CT('plain', 'mean')) =}, with a tab per case. Cale's second sheet does the same "if you can change the direction of the last move(s) of EO" ([*DR setup stats (switching last move of EO)*](https://docs.google.com/spreadsheets/d/1_2PmFv1KyBX335SjSb4oweS0sx804fIhbuP50D-gBj4), made at Tom Nelson's request, [[D1534]], [[D1549]]).
- **Louis's [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs)**: "I've generated every possible EO->DR case of increasing lengths" and sorted them by DRM and ARM ([[T4327]]); its last tab is the EO to DR distribution. **Rodney Kinney**'s *DRM corner variant+pair stats* is built on it ([[T8104]]: "and I did some work on the DRM/ARM stats and came up with something cool."). Separately: **KrzychXyz**'s sheet of every case sorted by DRM ("all DR cases (from EO) grouped by subsets, sorted by optimal", [[D5802]]), **Evan**'s [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk) tables ("this stat is in my arm/pairs sheet", [[D13434]]), and the *arm/pairs NEW!!!* sheet deven posted ([[D16271]]).
- **FakeMMAP**'s counts of the same {= EODRT() =} states, "not allowing EO-breaking moves" ([[T2598]]), and **torchlight**'s table that "allows breaking EO" ([[T2600]]): EO-breaking turns change almost nothing. DougCube confirmed the counts two years later: "that matches the table I just generated:" ([[T9941]]).
- **DougCube's [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo)** (posted [[N2397]]): fixed-axis EO (mean {= EO1() =}), DR from a scramble on one fixed axis ("Going to DR", mean {= f4(A["a1"][A1N["fixed"]]["mean"]) =}, at most {= A1("fixed", "max") =}), and, added after August 2025, "NISS-EO on any axis. Credit: Joba". **Joba** computed that NISS EO table over all 12!·2^11 edge states: "On average, eo can be solved in 3.455 moves." ([[T9374]]).
- **Shota**'s table of the shortest linear EO against the number of bad edges ([[D7761]]: "here's a table that also takes into account the optimal move counts") and Shota's [*Full EO*](https://docs.google.com/spreadsheets/d/1K38k5BQUV5PQh4ZmeJGNfrRZbnuhVePp4CLqyCIelm4) sheet of every one-axis EO case (linked by KrzychXyz in [[T9408]]).
- **Tronto's** EO-solved scrambles, about 250 ("like 250") ([[T4458]], [[T4459]]), with optimal solutions with and without EO-breaking moves: "optimal average: 16.64" against "eofbfin average: 16.70" ([[T4462]]). That is EO to solved, not EO to DR, but it is the one earlier measurement of what keeping the EO costs for the whole solve.
- **The server's own counts**: Louis's "Only 6.2% of axes are 8 moves or less away from DR if you don't allow NISS" ([[T5965]]); torchlight's exact bad-edge counts on the three axes ([[D3299]], [[D3530]]); wen's "200ish <=5 movers and 17 <=4 movers" from memory ([[T4633]]); Cale's sheet of EO counts on official scrambles, with about 4% having no EO of at most 4 ([[D2197]]; wen, [[T5360]]); Rodney Kinney's 1,000 optimal EO to DR solutions (*Multi-Axis DR*, [[T3939]]).
- **Tools**: DR Finder 2 (sanya.sweetduet.info), which Daichi pointed to for DRs from a scramble ([[D20016]]), and nissy.
- **My own DR-xs study**, section 6.4: the best of six linear DR (3 axes, normal or inverse) on {= PRIOR('best of 6 (normal or inverse)', 'prior_n') =} scrambles. The numbers here agree with it (appendix B).

**What this adds**:

- **Scramble to DR over all axes, with NISS and through short EOs**, with the odds of 8, 9, 10 and 11, and the scrambles that have no sub-10 DR at all. One fixed axis (DougCube, Louis) and the best of six (my DR-xs study) were known; the best of three on each side, NISS, and the scrambles without a sub-10 DR were not (wen asked, [[D20015]]).
- **How the optimal DR relates to the EOs people write**: the shortest EO inside the optimal DR, and the best DR through an EO of at most 3, 4, 5 or 6 turns, normal, inverse and NISS, as odds of a DR in 8 to 12.
- **How many DRs a scramble has** through its short EOs, and what 4-move against 5-move EOs and the other EO axes are worth.
- **EO counts and shortest EOs per scramble** on all three axes, linear and with the inverse (with NISS, Joba's table had the shortest EO), and the bad-edge layouts exactly, with the odds of a short EO by bad-edge count with the inverse and with NISS.
- **EO to DR with every option a solver has**: the other DR axis (exact), the inverse, the EO's last turn either way, and all together, overall and by case; and how the normal and inverse sides are related.
- **The claims, checked**, and **a finding about nissy 2.0.8's `scramble`**: a modulo bias in its edge permutation, which makes DRs on the inverse of its scrambles shorter (appendix B).

**Terms**, as the server uses them. *EO* on an axis: all edges good for that axis. *DR*: corners oriented and the slice edges in their slice for one axis. *Normal* means turns after the scramble, *inverse* turns after the inverse scramble (written in brackets), *NISS* turns on both sides, the length being the sum. A *linear* DR or EO is on one side only. *Best of six*: the shortest DR over the three axes on normal and on inverse. An EO of length L is a sequence that solves EO for the first time at its last turn (nissy's `-a` convention; both directions of the last turn count). A *route through an EO*: the EO, then turns that keep it (no quarter turns of its axis) to DR on one of the two other axes. A case like *4c4e*: bad corners, then edges out of place for DR on that axis (slice edges outside the slice and as many other edges inside it); Cale's sheet writes it edges first (4e4c), and Louis's ARM tables use the same counts. *In 10* means in 10 turns or fewer. Turns are face turns (HTM).

**How to read it.**

- **Start with [section 1](#1-the-short-version)**, the short version: what is new, then what it confirms or corrects, one line each.
- **The [worked examples](examples.html)** go with it: 150 scrambles with their shortest DRs and their best DRs through EOs of at most 4 and 5, then 60 EO-solved states by case, answers folded away. **The [errata](errata.html)** list what the numbers show is wrong in things said on the server, each with an example.
- **The appendices are reference**: every case, normal against inverse by case, every bad-edge triple, and how it was computed and checked (with nissy's scrambler).
- **What you can use in an attempt, and what is the answer key.** Most numbers here are what exists, found by exact search: the optimal DR from a scramble, the best DR after every EO of a given length, counts of hundreds of EOs per scramble. Those are **computer only**: they say what is there, not something to do in an attempt, and each place says so. What you can use at the table is what you can see or count: the bad edges on each axis and the odds of a short EO from them (4.2), the case an EO leaves on each DR axis and its odds with each option (5.2), and which options after an EO are worth checking (5.1).

---

{{CONTENTS}}

---

## 1. The short version

{{SEC_SHORT}}

---

## 2. What was asked

{{SEC_ASKED}}

---

{{SEC_SCRDR}}

---

{{SEC_EO}}

---

{{SEC_EODR}}

---

{{SEC_CLAIMS}}

---

{{SEC_LIMITS}}

---

{{APP}}
