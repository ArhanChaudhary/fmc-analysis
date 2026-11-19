# Corners in 3D: how far from HTR, and which turn gets closer

Take the corners of any state, not just a DR. Hold DBL still and turn only R, U and F. What can you see on them that says how far they are from HTR, what can you *prove* from it, and does it tell you the turn that gets closer? That's what this page answers. Everything is exact over all 3,674,160 corner states, and the theorems are checked in Lean.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion).

**This builds on** what the server already has. Pretty much every piece existed for DR corners; this page takes the DR axis away.

- **rodneykinney's [*Hyper-Parity*](https://docs.google.com/document/d/1Onc2lu5iW_ODnT71oN5lgpVVjVqbvUMzaylzxgykx0I)** (June 2020): the tetrads, the three conditions for HTR ("We call the method “Hyper-Parity” because there are three parity-like conditions that must all be satisfied to bring the cube into HTR."), the FB labels 0c / 4a / 4b / 2c, the UD labels 4a / 4b / 4c / 4d, the maze and the funnel.
- **The subset names** 0c0 … 4b5, from wen and exhaustingg's sheet [*HTR better smh (v2)*](https://docs.google.com/spreadsheets/d/1ZhulzHeNgv2Hiy4x9R1MzsMRlPlI-E8DRiHFJlPlboM), and zakimoshi's list of the 14 of them ([5 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1214532083612127324)).
- **zakimoshi's 3d maze** ([10 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404306506928881684), [10 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404306762261069915), [10 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404311546590527621)): "I really think the 3d maze should be explored more", "Like how qts on other axes effect your subset", and the recognition: "To find the bad corners all you have to do is look for ones with exactly 1 oriented sticker". This page is that maze.
- **beef beans' quarter-turn count of a scrambled cube** ([21 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143384156198416426)): twist every corner flat on any axis and read the subset, "so the orientation of the corners dosen't really matter, the corners always have a number of quarter turns it takes to solve them." torchlight's reason ([22 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143568556332691586)): "R and [D2 L2 : U'] permute corners in the same way". FakeMMAP's proof ([23 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143847973789384825)). And zakimoshi's catch ([23 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143786175438532709)): "orienting corners requires you to change the qt", "You need to solve them together which makes it much more complicated".
- **Jules Porteners' table** ([16 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1362033817325535253)) for Zagros's question "Anyone know if there are 2x2 scrambles that take >5qt to solve?" ([15 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1361555392814911488)): "sometimes 8 qt is required", with the count of states at each number of quarter turns.
- **The DR counts**: Radek B's quarter turns for all corner permutations, by shape ([14 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1273398601820799140), [14 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1273404063295475822)), FakeMMAP's over all 7! corner cases ([26 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1144917908078723112)), Shota's subset ratios ([14 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1273446142226731079)).
- **Triple DR and fake HTR**: six triple DRs up to half turns (zakimoshi asked, [4 Jun 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1115043982821572700); trig0n and Tom Nelson answered, [4 Jun 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1115045288609071164), [4 Jun 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1115047541281665155)), FakeMMAP's group orders with DBL fixed ([1 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1367524395983175782)), KrzychXyz's "DR on all axis, but not HTR" ([4 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1379886612380516434)), torchlight's Klein 4-group rule ([3 Oct 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1291448033787252736), [3 Oct 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1291448207208874014)).
- **FakeMMAP's Lemma 1 and Corollary 2** ([1 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412001179365408790)): "Lemma 1: If triple DR and OBL are solved, and there is even parity, then the state is in true HTR." and "Corollary 2: if you know the U/D pattern, the positioning of bad corners, and corner parity, then you know exactly the HTR solution."
- **Louis's bound** ([30 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1334522555968782411)): "as a first step we could consider distance to triple DR which is a lower bound to distance to HTR and doesn't require messing around with corner permutation". Zagros's reply ([30 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1334533412928880712)): "I don't think it should be possible to determine distance to htr, only to fake htr, since you could always cycle three corners and have the exact same orientations on every axis". Nobody posted numbers for either.
- **rodneykinney's CO maze** ([20 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1154064564946739200), [the gist](https://gist.github.com/rodneykinney/fd3473e7cc514ae192e4eb538dd134a7)): corner orientation on one axis as a maze. Their own verdict: "Still too complicated to keep in your head, IMO".
- **The H48 solver** of Sebastiano Tronto ([its doc](https://github.com/sebastianotronto/nissy-core/blob/master/doc/h48.md), quoted on the server by Arch, [11 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1382436238446821467)). Its target: "Each corner is placed in the corner tetrad it belongs to, and it is oriented." And it already keeps a bound from the same read as this page's types: its corner table "also stores a preliminary pruning value based on the corner coordinate", the coordinate being corner orientation plus which tetrad each corner is in. So a program has had Louis's bound all along. What wasn't known is how tight it is and what a person can do with it.
- **Joba's lower bounds with NISS** by quarter turns ([13 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1349876840914751578)).

**What this adds:**

- **The six things a corner can show, and the rule for what a quarter turn does to them** on any axis (section 4). Proved for every state.
- **Types alone find real HTR exactly 1 time in 6**, whatever the rule. With parity it's 1 in 3 at best, with the D-colour corners 1 in 2 at best, with both it's settled. The test for HTR is still Hyper-Parity's three conditions, with *every corner good* in place of the FB condition: FakeMMAP's lemma with the DR axis gone (section 5).
- **Fake HTR is exactly 9 moves from HTR**, all 120 of them, even with every R, U and F turn allowed (section 5).
- **Floors you can prove**, with how tight each one is: a count table you read at a glance, the types floor (Louis's distance to triple DR and H48's corner bound, measured against the truth), the parity and colour upgrades, and which of them survive NISS (section 6).
- **Which turn gets closer**, graded by distance, next to the best any rule could do with the same read (section 7).
- **What the twist costs on top of beef beans' count**: 0, 2, 4, 6 or 8 quarter turns (section 8).
- **DR corners seen from outside DR**: no quarter turn is ever saved, but 1 or 2 moves are on 40% of the cases (section 9).
- **The mazes**: rodneykinney's two small ones don't change off the DR axis, and there are only five kinds of 2-qt pattern (sections 5, 8 and 10).

**Terms.**

- *HTR* here means corners that half turns solve: the 24 states R2, U2 and F2 reach. *Solved* on this page means HTR.
- *Tetrads*: UFR-UBL-DFL-DBR and UFL-UBR-DFR-DBL. A corner is *out* when it sits in the other tetrad, so half turns can't bring it home. That's zakimoshi's bad corner without an axis.
- A sticker is *oriented* when its colour belongs to the axis of the face it's on (a white or yellow sticker on U or D, and so on).
- A corner is *good* (in its tetrad, all three stickers oriented), *twisted* (in its tetrad, none oriented) or *out* (exactly one oriented). The *types* of a state, or its *type pattern*, are the type of every corner, place by place.
- *All good* is triple DR: DR on all three axes at once. It's HTR or a *fake HTR*.
- *D-colour corners*: the four corners that carry DBL's U/D colour (yellow, if you scramble white top green front). Their *picture* is where they sit, labelled 4a / 4b / 4c / 4d as in *Hyper-Parity*.
- *4a* and *4b* get used for two things, as in *Hyper-Parity*: the shape of four out corners (the 4a of 4a1) and the picture of the D-colour corners. I always say which.
- *Parity*: even or odd placement of the corners. A quarter turn flips it, a half turn doesn't.
- *Moves* are HTM. *Quarter turns* (qt) are counted with half turns free, like the number in a subset name.
- *One side* means every move on the normal scramble. *NISS* means moves on both sides.
- A *floor* is a number proved to be at most the true distance: you can't do it in fewer.
- *Subset number of the placement*: beef beans' count. Forget the twists, read the subset.
- *Look-alikes*: states that show the same thing. Six HTR cases look alike on the types alone.

Types are written as seven characters in the order UFR UFL UBL UBR DFR DFL DBR: `.` good, `+` twisted clockwise, `-` twisted counter-clockwise, `r` `u` `f` out with only the R/L, U/D or F/B sticker oriented. After the scramble R that's `r . . r r . r`.

**How to read it.** Section 1 is the whole answer. Each read is marked with what it takes: *at a glance* (typing a corner is looking at its three stickers), *tracing* (parity), *a search* (finding a way to make every corner good) or *computer only*. Section 6 is the reference for floors, section 7 for the next turn. The examples file has the catalogue of every pattern within 3 moves of all good, 200 random states to try, and DR cases solved both ways. [The lookup page](tool/) does all the reads and floors for any scramble you type. All numbers are exact counts over the 3,674,160 states.

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | The answer: what is new, what is confirmed, what is corrected. |
| [2. What was asked](#2-what-was-asked) | The questions, and the ones the server left open. |
| [3. The model, and what carries over to a real cube](#3-the-model-and-what-carries-over-to-a-real-cube) | DBL held, R U F turns. The distance tables in moves and in quarter turns, one side and with NISS. |
| [4. Reading a corner](#4-reading-a-corner) | The six types, the rule for a quarter turn, and a floor you can prove by hand. |
| [5. Three reads fix everything: types, D-colour corners, parity](#5-three-reads-fix-everything-types-d-colour-corners-parity) | **The main result.** Why types alone hit HTR 1 time in 6, what the other two reads add, and the test for HTR. |
| [6. Floors: proving a state needs at least X](#6-floors-proving-a-state-needs-at-least-x) | **Reference.** The ladder of floors with how tight each is, the count table, the 9 − k rule, quarter turns, NISS. |
| [7. Which turn gets closer](#7-which-turn-gets-closer) | Every rule graded by distance, and the best any rule could do with the same read. The flow chart. |
| [8. Quarter turns in 3D](#8-quarter-turns-in-3d) | The subset number of the placement, what the twist costs, the out-corner maze, everything within 2 qt. |
| [9. DR corners, seen from outside DR](#9-dr-corners-seen-from-outside-dr) | Subset by subset: DR turns against all turns, with and without NISS. What going through CO costs. |
| [10. The mazes in one place](#10-the-mazes-in-one-place) | Where each maze is, and why there isn't one big one. |
| [11. The claims, checked](#11-the-claims-checked) | Everything said on the server that the search can check. |
| [12. What this does not cover](#12-what-this-does-not-cover) | Limits. |
| [Appendix: how it was computed, and what is proved in Lean](#appendix-how-it-was-computed-and-what-is-proved-in-lean) | The model, the searches, the Lean theorems by name. |

## 1. The short version

**New here:**

- **A corner shows one of six things, and a quarter turn changes them by one rule.** Good, twisted (two ways) or out (three ways, by which sticker is still oriented). A quarter turn of a face does this to its four corners: good ↔ out with that face's axis oriented, twisted ↔ out with another axis oriented. Half turns only move corners around. You read all of it at a glance. (Section 4.)
- **Types alone can't find HTR more than 1 time in 6.** Each type pattern is shared by 144 states, and any sequence that makes one of them all good makes all of them all good: 24 land in HTR and 120 in a fake HTR. So when a rule that reads only the types has made every corner good, it's in real HTR for exactly 1 state in 6. A rule that also reads parity gets 1 in 3 if it aims for an even number of quarter turns left, and one that reads the D-colour corners gets 1 in 2 if it aims for a 4a picture. Types + D-colour corners + parity settle it. (Section 5.)
- **A fake HTR is exactly 9 moves from HTR**, every one of the 120, with all nine turns allowed. Off-axis turns don't help. So if you're k moves from a fake HTR, you're at least 9 − k from the real one.
- **Floors.** Mean distance to HTR is 7.58 moves.
  - The count table (how many twisted, how many out per axis; at a glance): 4.34 on average. Weak, but free.
  - The types floor, which is Louis's distance to triple DR: 6.41 on average, exact on 30.9% of states, exact or 1 short on 65.8%.
  - With parity: 6.90, exact on 53.8%. With parity and the D-colour corners: 7.34, exact on 78.8%, never more than 4 short.
  - Two twisted corners and nothing else: at least 7 moves and 5 quarter turns. Twists are what's expensive.
- **Which turn gets closer.** Within 4 moves of HTR, following the types is always right. At 5 it's right 96.4%, at 6 75.1%, at 7 33.8%, and at 8, where half of all states are, 25.9%, which is what a random turn gets (25.2%). The best single table on the types is right 51.3% of the time over all states, and no rule on the types could beat 61.4% at 7 even if it knew the distance. Far out the types don't know. (Section 7.)
- **The quarter-turn count is beef beans' count plus what the twist costs**: +0 for 34.7% of states, +2 for 55.0%, +4 for 9.8%, +6 or +8 for the rest. Always even. (Section 8.)
- **Leaving DR saves moves, never quarter turns.** Of the 210 DR corner cases, 62 are 1 move closer to HTR with off-axis turns and 22 are 2 closer. Every 5-qt case is. The shorter solution nearly always spends 2 or 4 more quarter turns than the subset number to do it. Corners only, of course. (Section 9.)
- **Orienting first costs.** Optimal CO on the best of the three axes and then the best DR-only finish is 1.48 moves longer than the optimal on average, and it's optimal for only 32.3% of states.
- **With NISS** the mean drops to 6.89 and God's number from 10 to 9. Every floor in quarter turns still holds with NISS. The one-sided move floors don't: the types floor is too high for 14.2% of states once you allow moves on the inverse. (Section 6.)
- **Within 2 quarter turns of HTR there are only five kinds of pattern** besides the 4a face. Three of them don't exist on a DR. (Section 8.)

**Carries over from DR as it is** (known there, checked here for every state):

- **The test for HTR**: every corner good + D-colour corners in a 4a picture + even parity. Those are Hyper-Parity's three conditions with *every corner good* in place of the FB one, and FakeMMAP's Lemma 1 with all six pictures. You don't solve anything first; parity is still a trace. (Section 5.)
- **The subset number.** Quarter turns on the other axes never lower it: that's FakeMMAP's argument for beef beans' count, read the other way. (Section 9.)
- **rodneykinney's two small mazes** (out corners, D-colour corners), with the same 0 / 1 / 2 / 3 and 0 / 1 / 2 / 1 quarter turns. What 3D adds is the twist. (Sections 5, 8 and 10.)

**Confirmed:** Jules Porteners' table, FakeMMAP's counts over 7!, Shota's ratios, beef beans' axis-independence, torchlight's Klein 4-group rule, FakeMMAP's lemma, Joba's NISS bounds 1 / 2 / 4 / 6 / 8 with 0c3 at 6, and Yura Riabov's 11 to HTR. Section 11 has all of them.

**Corrected** (the errata page has the example): wen's 13-move 4a4 has a 12 inside DR turns. beef beans's sheet already had 12 as the longest for that subset, and 13 only for 2c5; the full search agrees.

## 2. What was asked

1. Which things you can see on the corners (wrong tetrad, orientation per axis, the pieces of a subset name) say how far a state is from HTR? *Answer*: sections 4 to 6 and 8.
2. How do I prove a state can't be solved in fewer than X moves from those patterns? *Answer*: section 6.
3. Which turn gets closer? *Answer*: section 7. Near HTR the types say it. Far out they don't, and section 7 says how far any rule could go.
4. Mazes and flow charts. *Answer*: sections 4, 5, 8 and 10.

And from the server:

5. zakimoshi's 3d maze: "Like how qts on other axes effect your subset" ([10 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404306762261069915)). *Answer*: sections 4, 8 and 9.
6. Louis's distance to triple DR as a bound ([30 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1334522555968782411)), and Jay's wish for move counts to HTR from two axes ([29 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1334328007476641832)). *Answer*: section 6.
7. JTuu: "it'd be interesting if we could know whether each qt is +1 or -1 just by looking at the moves" ([22 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143452357611499540)). *Answer*: section 8.5, partly.
8. Joba, on the tetrad twist: "There *has* to be a way to avoid having to actually solve the corners" ([14 Dec 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1184860107851448411)). torchlight gave one that computes it ([14 Dec 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1184861022377484328)). *Answer*: section 5.3 has one you read off the stickers.
9. mrauo: "What is CO movecount distribution?" ([18 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1153267556719800381)). FakeMMAP gave the best cases for Jay's version of it ([19 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1153814132445937795)). *Answer*: section 9.4 has the whole distribution, for this move set.

## 3. The model, and what carries over to a real cube

DBL never moves and only R, U and F turn. That's every corner state up to turning the whole cube: $7! \times 3^6$ = 3,674,160 of them. rodneykinney in *Hyper-Parity*: "It is always possible to solve corners up to rotation using only R/U/F moves." FakeMMAP counts the same way ("we consider corners only, and assume DBL to be fixed", [1 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1367524395983175782)).

What carries over to a real cube:

- **Every floor does.** A real solution into HTR with any of the 18 turns becomes an R, U, F sequence of the same length here, with the same number of quarter turns (L is R seen from the other side, and so on). The same goes for a solution with moves on both sides. So a state that needs at least X here needs at least X on the cube, with or without NISS, for the corners and so for everything.
- **The distances are a little short for a real cube.** Here U D' is HTR, because the corners only went round with DBL. On a cube it's two moves from HTR. That's the usual rule of the subset names, zakimoshi's "0c // htr/fake (8 is equivalent by slice)" ([5 Mar 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1214532083612127324)).

One row per number of moves. *One side* is every move on the normal scramble, and *with NISS* allows moves on both sides.

| Moves to HTR | States, one side | Share | This or fewer | States, with NISS | Share | This or fewer |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 24 | 0.00% | 0.00% | 24 | 0.00% | 0.00% |
| 1 | 72 | 0.00% | 0.00% | 132 | 0.00% | 0.00% |
| 2 | 432 | 0.01% | 0.01% | 876 | 0.02% | 0.03% |
| 3 | 2,304 | 0.06% | 0.08% | 5,376 | 0.15% | 0.17% |
| 4 | 13,464 | 0.37% | 0.44% | 32,972 | 0.90% | 1.07% |
| 5 | 65,496 | 1.78% | 2.23% | 171,056 | 4.66% | 5.73% |
| 6 | 296,400 | 8.07% | 10.29% | 760,416 | 20.70% | 26.42% |
| 7 | 1,077,072 | 29.31% | 39.61% | 1,889,352 | 51.42% | 77.85% |
| 8 | 1,813,680 | 49.36% | 88.97% | 806,756 | 21.96% | 99.80% |
| 9 | 401,472 | 10.93% | 99.90% | 7,200 | 0.20% | 100.00% |
| 10 | 3,744 | 0.10% | 100.00% | 0 | 0.00% | 100.00% |

God's number is 10 on one side and 9 with NISS. The means are 7.58 and 6.89. NISS saves nothing on 44.6% of states, 1 move on 42.3%, 2 on 12.2% and 3 on 0.9%.

Half of all states are 8 moves out (49.4%), and 89.6% are 7, 8 or 9. So a rule that *predicts the distance within one move* is worth nothing on its own: always saying 8 does that. That's why the floors below are graded by how often they're *exact*, and the rules of section 7 by whether their turn gets closer.

The same in quarter turns, with half turns free. The states column is Jules Porteners' table ([16 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1362033817325535253)), which this search reproduces to the last state.

| Quarter turns to HTR | States | Share | Fewest moves | Mean moves | Most moves | Mean moves with NISS |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 24 | 0.00% | 0 | 0.00 | 0 | 0.00 |
| 1 | 432 | 0.01% | 1 | 2.50 | 4 | 1.97 |
| 2 | 6,768 | 0.18% | 2 | 4.37 | 8 | 3.72 |
| 3 | 86,184 | 2.35% | 3 | 6.00 | 9 | 5.28 |
| 4 | 780,048 | 21.23% | 4 | 7.18 | 10 | 6.45 |
| 5 | 1,708,416 | 46.50% | 5 | 7.64 | 10 | 6.95 |
| 6 | 1,049,856 | 28.57% | 6 | 7.91 | 10 | 7.23 |
| 7 | 42,048 | 1.14% | 8 | 8.58 | 10 | 7.91 |
| 8 | 384 | 0.01% | 9 | 9.00 | 9 | 8.21 |

## 4. Reading a corner

### 4.1 The six types

Look at a corner's three stickers and count the oriented ones.

- **3 oriented: good.** The corner is in its tetrad and not twisted.
- **0 oriented: twisted.** It's in its tetrad, twisted clockwise or counter-clockwise. For the rule below it's easier to say where its U/D sticker is: on an F/B face or on an R/L face.
- **1 oriented: out.** It's in the wrong tetrad. Three kinds, by which sticker is the oriented one: R/L, U/D or F/B.

That's all there is. 2 oriented never happens, and the count tells you the tetrad. This is zakimoshi's "exactly 1 oriented sticker" ([10 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404311546590527621)) and the H48 remark that "For a corner that is placed in its own tetrad, the orientation does not depend on the reference axis chosen" ([11 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1382436238446821467)), put together and proved for every corner of every state.

Why it's true: a quarter turn keeps the sticker on the turning face where it is and swaps the other two between their axes. It also carries the corner to the other tetrad. So every quarter turn is one swap of two stickers and one change of tetrad, and they stay in step: an even number of swaps (0 or 3 stickers off) in your own tetrad, an odd number (exactly 2 off) in the other.

On a DR every corner is good or out with the DR axis oriented. So the bad corners of a subset name are the out corners, and *4a*, *2c* are shapes of out corners.

### 4.2 What a turn does

A half turn moves corners inside their tetrads and changes no type. A quarter turn of a face does this to the four corners on it, either direction:

- good ↔ out with that face's axis oriented;
- twisted ↔ out with one of the other two axes oriented.

So a U turn fixes the `u` corners on U, breaks the good ones into `u`, turns `r` and `f` corners into twisted ones and twisted ones into `r` or `f`. The full table, one row per face:

| Quarter turn | A good corner becomes | Twisted, U/D sticker on F/B, becomes | Twisted, U/D sticker on R/L, becomes |
|---|---|---|---|
| R or R' | out, only R/L oriented | out, only U/D oriented | out, only F/B oriented |
| U or U' | out, only U/D oriented | out, only F/B oriented | out, only R/L oriented |
| F or F' | out, only F/B oriented | out, only R/L oriented | out, only U/D oriented |

Read backwards it's the same table: every line goes both ways.

<figure>
<svg viewBox="0 0 720 330" width="720" role="img" aria-label="What a quarter turn does to a corner: the six types" style="max-width:100%;height:auto;color:var(--fg);font:14px system-ui,sans-serif" fill="currentColor"><title>What a quarter turn does to a corner: the six types</title><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker></defs><rect x="20" y="30" width="180" height="60" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="110.0" y="57.0" text-anchor="middle" font-weight="650">good</text><text x="110.0" y="72.0" text-anchor="middle">3 stickers oriented</text><rect x="20" y="135" width="180" height="60" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="110.0" y="162.0" text-anchor="middle" font-weight="650">twisted</text><text x="110.0" y="177.0" text-anchor="middle">U/D sticker on F/B</text><rect x="20" y="240" width="180" height="60" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="110.0" y="267.0" text-anchor="middle" font-weight="650">twisted</text><text x="110.0" y="282.0" text-anchor="middle">U/D sticker on R/L</text><rect x="520" y="30" width="180" height="60" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="610.0" y="57.0" text-anchor="middle" font-weight="650">out</text><text x="610.0" y="72.0" text-anchor="middle">only U/D oriented</text><rect x="520" y="135" width="180" height="60" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="610.0" y="162.0" text-anchor="middle" font-weight="650">out</text><text x="610.0" y="177.0" text-anchor="middle">only R/L oriented</text><rect x="520" y="240" width="180" height="60" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="610.0" y="267.0" text-anchor="middle" font-weight="650">out</text><text x="610.0" y="282.0" text-anchor="middle">only F/B oriented</text><line x1="200.0" y1="60.0" x2="520.0" y2="270.0" stroke="currentColor" stroke-width="1.2"/><text x="264.0" y="106.0" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">F</text><text x="264.0" y="106.0" text-anchor="middle" font-size="12">F</text><line x1="200.0" y1="165.0" x2="520.0" y2="165.0" stroke="currentColor" stroke-width="1.2"/><text x="305.6" y="169.0" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">F</text><text x="305.6" y="169.0" text-anchor="middle" font-size="12">F</text><line x1="200.0" y1="270.0" x2="520.0" y2="60.0" stroke="currentColor" stroke-width="1.2"/><text x="264.0" y="232.0" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">F</text><text x="264.0" y="232.0" text-anchor="middle" font-size="12">F</text><line x1="200.0" y1="60.0" x2="520.0" y2="165.0" stroke="currentColor" stroke-width="1.2"/><text x="264.0" y="85.0" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">R</text><text x="264.0" y="85.0" text-anchor="middle" font-size="12">R</text><line x1="200.0" y1="270.0" x2="520.0" y2="270.0" stroke="currentColor" stroke-width="1.2"/><text x="264.0" y="274.0" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">R</text><text x="264.0" y="274.0" text-anchor="middle" font-size="12">R</text><line x1="200.0" y1="165.0" x2="520.0" y2="60.0" stroke="currentColor" stroke-width="1.2"/><text x="305.6" y="134.3" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">R</text><text x="305.6" y="134.3" text-anchor="middle" font-size="12">R</text><line x1="200.0" y1="60.0" x2="520.0" y2="60.0" stroke="currentColor" stroke-width="1.2"/><text x="264.0" y="64.0" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">U</text><text x="264.0" y="64.0" text-anchor="middle" font-size="12">U</text><line x1="200.0" y1="165.0" x2="520.0" y2="270.0" stroke="currentColor" stroke-width="1.2"/><text x="305.6" y="203.7" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">U</text><text x="305.6" y="203.7" text-anchor="middle" font-size="12">U</text><line x1="200.0" y1="270.0" x2="520.0" y2="165.0" stroke="currentColor" stroke-width="1.2"/><text x="264.0" y="253.0" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">U</text><text x="264.0" y="253.0" text-anchor="middle" font-size="12">U</text><text x="360.0" y="322.0" text-anchor="middle" font-size="12">A line marked R is a quarter turn of R (either way) on a corner of the R face; U and F alike.</text></svg>
<figcaption>Every line is a quarter turn of the face named on it, for a corner on that face. Nine lines, and no line between two types on the same side.</figcaption>
</figure>

You don't need the table at the cube. Look at the two stickers that are *not* on the turning face: they trade faces. Whatever lands on a face of its own axis is oriented after the turn.

**What it means for a solution.** An out corner needs an odd number of quarter turns, and the one that fixes it is a turn about the axis of its oriented sticker: a `u` corner wants a U turn, so it has to be on U for that. A twisted corner needs two quarter turns on two different axes. A good corner on a face you turn has to be paid back.

### 4.3 A floor from that, by hand

Give a good corner 0, an out corner 1 and a twisted corner 2, and add up. Call it the weight. A quarter turn changes four corners by exactly 1 each, so the weight moves by at most 4, and a half turn doesn't move it. So:

> you need at least weight / 4 quarter turns, rounded up.

It holds with NISS too. It's a weak floor (2.29 quarter turns on average against a true 5.04): turns hit four corners of one face at a time and you can't choose which four. The count table of section 6.3 is the same idea done exactly.

## 5. Three reads fix everything: types, D-colour corners, parity

### 5.1 All good is six things

144 states have every corner good. That's triple DR. Only 24 of them are HTR.

| All corners good, and | States | Parity | Quarter turns to HTR | Moves to HTR |
|---|---:|---:|---:|---:|
| HTR | 24 | even | 0 | 0 |
| fake HTR, a swap away | 72 | odd | 3 | 9 |
| fake HTR, a 3-cycle away | 48 | even | 4 | 9 |

This is the six triple DRs of trig0n and Tom Nelson ("you have 3 options for corners (3-cycle, inverse, solved) and 2 options for parity = 3*2", [4 Jun 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1115047541281665155)) and torchlight's rule ([3 Oct 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1291448033787252736), [3 Oct 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1291448207208874014)): compare the placements of the two tetrads, and they agree up to the Klein 4-group for HTR, are a 3-cycle apart for the even fake, anything else for the odd one. It checks out on all 144 (section 11).

What's new is the last column. I expected off-axis turns to give some fake HTR a shortcut. They don't: all 120 are exactly 9 moves from HTR, with any turns. With NISS it's 6 to 9 for the odd ones and 6 or 7 for the even ones.

```
U R2 U F2 U2 R2 U F2 U     // KrzychXyz's fake HTR: every corner good, 4 qt
R' U2 R U2 R2 F2 R F2 R    // 9 moves to HTR with off-axis turns. Staying in DR is 9 too.
```

### 5.2 Why the types can't tell

Take any state and any sequence that makes all its corners good. The types of a state follow the rule of section 4.2 and nothing else, so the same sequence makes every state with those types all good. There are 144 such states, they end on 144 different all-good states, and 24 of those are HTR.

So a rule that reads only the types, however clever, has exactly 1 state in 6 in HTR at the moment it makes every corner good, and the other 5 in a fake HTR. That's JTuu's and Zagros's point made exact. JTuu ([29 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1334328689751490642)): "wouldn't a 2c within each tetrad always generate a case with the same drm/arm features but very different distance to htr?" Zagros ([30 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1334533412928880712)): you "could always cycle three corners and have the exact same orientations on every axis".

It's the reason a types floor is a floor and not the distance, and the reason the turn it picks stops being right far out.

### 5.3 What does tell: the D-colour corners, and parity

**Parity** removes three of the six. The number of quarter turns in any solution into HTR is even for an even placement and odd for an odd one. So a way to all good with the wrong number of quarter turns ends in a fake HTR for sure. (Parity is a trace.)

**The D-colour corners** remove the rest. Look at where the four corners with the D colour are (DBL is always one of them), wherever their D stickers face. Count them by tetrad:

- 2 and 2: *4a* if the two pairs are on the same face or on opposite faces, else *4b*;
- 3 and 1: *4c*;
- 4 and 0: *4d*.

These are rodneykinney's UD labels, and you read them at a glance.

> **A state is HTR exactly when every corner is good, the D-colour corners are in a 4a picture, and parity is even.**

There are six 4a pictures. Besides DBL the D colour is on: UFR UBL DFR; UFR UBR DFL; UFL UBL DFL; UFR UFL DBR; UBL UBR DBR; DFR DFL DBR.

You need all three conditions. Two fake HTRs, each failing one:

```
U R2 U F2 U2 R2 U F2 U       // all good, parity even, but the D-colour corners are 4b
U R2 U2 F2 U R2 U2 F2 U      // all good, D-colour corners 4a, but parity is odd
```

This is FakeMMAP's Lemma 1 ([1 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412001179365408790)) off the DR axis. Their version has OBL solved, which is the one picture with the D face whole, and gives the 4 states U2, R2 F2 R2, R2 F2 R2 U2 and solved. With all six pictures you get all 24.

Joba wanted "a way to avoid having to actually solve the corners" for the tetrad twist ([14 Dec 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1184860107851448411)), and torchlight gave one that computes it: number the corners so that opposite corners have the same number and compare the two tetrads ([14 Dec 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1184861022377484328)). This is the same thing read off the stickers: an even all-good state has no tetrad twist when its D-colour corners are 4a, and has one when they're 4b.

<figure>
<svg viewBox="0 0 720 300" width="720" role="img" aria-label="The D-colour corners: pictures, and where a quarter turn can take them" style="max-width:100%;height:auto;color:var(--fg);font:14px system-ui,sans-serif" fill="currentColor"><title>The D-colour corners: pictures, and where a quarter turn can take them</title><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker></defs><rect x="30" y="110" width="130" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="95.0" y="131.5" text-anchor="middle" font-weight="650">4d</text><text x="95.0" y="146.5" text-anchor="middle">4 and 0</text><text x="95.0" y="161.5" text-anchor="middle">at least 1 qt</text><rect x="200" y="110" width="130" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="265.0" y="131.5" text-anchor="middle" font-weight="650">4a</text><text x="265.0" y="146.5" text-anchor="middle">2 and 2, HTR-like</text><text x="265.0" y="161.5" text-anchor="middle">0 qt</text><rect x="380" y="110" width="130" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="445.0" y="131.5" text-anchor="middle" font-weight="650">4b</text><text x="445.0" y="146.5" text-anchor="middle">2 and 2, bars</text><text x="445.0" y="161.5" text-anchor="middle">at least 1 qt</text><rect x="560" y="110" width="130" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="625.0" y="131.5" text-anchor="middle" font-weight="650">4c</text><text x="625.0" y="146.5" text-anchor="middle">3 and 1</text><text x="625.0" y="161.5" text-anchor="middle">at least 2 qt</text><line x1="160.0" y1="142.0" x2="200.0" y2="142.0" stroke="currentColor" stroke-width="1.2"/><line x1="330.0" y1="142.0" x2="380.0" y2="142.0" stroke="currentColor" stroke-width="1.2"/><line x1="510.0" y1="142.0" x2="560.0" y2="142.0" stroke="currentColor" stroke-width="1.2"/><path d="M 251.0 110 C 235.0 76, 295.0 76, 279.0 110" fill="none" stroke="currentColor" stroke-width="1.2"/><text x="265.0" y="80.0" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">can stay</text><text x="265.0" y="80.0" text-anchor="middle" font-size="12">can stay</text><path d="M 611.0 110 C 595.0 76, 655.0 76, 639.0 110" fill="none" stroke="currentColor" stroke-width="1.2"/><text x="625.0" y="80.0" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">can stay</text><text x="625.0" y="80.0" text-anchor="middle" font-size="12">can stay</text><text x="360.0" y="235.0" text-anchor="middle" font-size="12">Count the four corners that carry the D colour (DBL is one) by tetrad: 2 and 2, 3 and 1, or 4 and 0.</text><text x="360.0" y="253.0" text-anchor="middle" font-size="12">4a: the two pairs sit on the same face or on opposite faces. One line = one quarter turn of R, U or F.</text><text x="360.0" y="271.0" text-anchor="middle" font-size="12">These are rodneykinney's UD labels with the same 0, 1, 2, 1 quarter turns: nothing changes off the DR axis.</text></svg>
<figcaption>The UD maze of Hyper-Parity, with turns on all three axes. The labels and the quarter turns are the same.</figcaption>
</figure>

A quarter turn can keep you in 4a or in 4c and always moves you out of 4b and 4d, exactly as in *Hyper-Parity*: "it is possible to remain in 4a or 4c, but not in 4b or 4d". Nothing changes off the DR axis, because this picture never looks at where a sticker faces.

### 5.4 How much each read settles

One row per set of reads. The fourth column is for a rule that sees only that read, at the moment it has made every corner good.

| What you read | Different things you can see | States that show the same | In HTR once every corner is good | States whose moves to HTR it determines | States whose quarter turns it determines |
|---|---:|---:|---:|---:|---:|
| the types | 25,515 | 144 | 1 in 6 | 1.2% | 0.0% |
| types + parity | 51,030 | 72 | 1 in 3 at best | 17.3% | 61.6% |
| types + D-colour corners | 459,270 | 8 | 1 in 2 at best | 34.9% | 0.0% |
| types + D-colour corners + parity | 918,540 | 4 | always | 100.0% | 100.0% |

- Types + D-colour corners + parity determine the moves to HTR and the quarter turns of every state. That's FakeMMAP's Corollary 2 for all corner states.
- Types + the D-colour corners + the B-colour corners determine the whole state, with no tracing: 3,674,160 different things to see for 3,674,160 states.
- Parity does most of the work for quarter turns (61.6% of states settled), the colour most of it for moves.

## 6. Floors: proving a state needs at least X

### 6.1 What makes a floor a proof

A floor is any number f you can read off a state with two properties: it's 0 on HTR, and no single turn lowers it by more than 1. Then a solution of n moves can't start from a state with f above n. That's the whole argument, and it's proved once in Lean for any such f.

Most of the floors below are the distance to something easier than HTR:

- forget everything but which corners are out: the distance to *all corners in their tetrads*;
- forget the pieces and keep the types: the distance to *all good*. That's the **types floor**, Louis's distance to triple DR;
- keep the types and the parity: the distance to an *even* all-good state;
- keep the types and the D-colour corners: the distance to an all-good state with a 4a picture.

HTR is inside each of those targets, so each distance is a floor. They're exact tables from a full search; the types floor and the parity floor are also checked state by state in Lean. The count table of 6.3 and weight / 4 are floors for other reasons: the first is the smallest distance among all states with the same counts, the second is the argument of 4.3.

### 6.2 The ladder

One row per floor, for solutions on one side. *Exact* is the share of all states where the floor equals the true distance.

| Floor | What it reads | How you get it | Mean floor (moves) | States where it is exact | Exact or 1 short | Most it is short by |
|---|---|---|---:|---:|---:|---:|
| corners back in their tetrads | which corners are out | at a glance | 2.31 | 0.0% | 0.3% | 10 |
| count table | how many twisted, how many out per axis | at a glance | 4.34 | 1.3% | 7.1% | 9 |
| corners oriented on one axis (U/D) | the U/D stickers | table | 4.44 | 1.1% | 7.2% | 9 |
| the same, best of the three axes | all stickers, by axis | table | 5.02 | 2.3% | 13.0% | 9 |
| placement alone | the pieces, twists ignored | table | 4.02 | 0.7% | 4.5% | 10 |
| types floor | the type of every corner | table, or a search | 6.41 | 30.9% | 65.8% | 9 |
| types + parity | types, and the parity | table, or a search | 6.90 | 53.8% | 83.2% | 9 |
| types + D-colour corners | types, and where the D-colour corners sit | table, or a search | 7.12 | 67.5% | 89.8% | 9 |
| the larger of the last two | types, parity, D-colour corners | table, or a search | 7.34 | 78.8% | 97.0% | 4 |
| the true distance | everything | computer | 7.58 | 100.0% | 100.0% | 0 |

- **The types floor is the big step.** Counting gets you to 4.34, orienting on the best axis to 5.02, and the types to 6.41 of the true 7.58. It's Louis's bound, and it "doesn't require messing around with corner permutation" ([30 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1334522555968782411)). It's also the kind of bound H48 keeps for its corner coordinate.
- **Where it falls short it's because of 5.2**: the nearest all-good state is a fake one. The types floor is short by 1 on 35.0% of states, by 2 on 23.3%, by 3 or more on 10.9%.
- **Parity and the D-colour corners each remove fakes.** Together they leave the floor exact on 78.8% of states.
- **The placement alone is a poor floor in moves** (4.02). It's much better in quarter turns (section 6.5).

How you get the types floor at the cube: it's the length of the shortest way to make every corner good. Within 3 moves that's 117 patterns besides all good itself, 20 up to symmetry, listed in the examples file; if yours isn't one of them, the floor is at least 4. Beyond that it's a search, and what you find is an upper bound on the floor until you've ruled out shorter ways. The exact table is computer only; [the lookup page](tool/) has it.

### 6.3 The count table

This one is read at a glance: count the twisted corners, and count the out corners by which sticker is oriented (R/L, U/D, F/B). Sort the three out counts, biggest first. The row gives the fewest moves any state with those counts needs, on one side and with NISS, and the fewest quarter turns. Every row is exact and has a state that meets it.

| Twisted | Out, by axis | Share of states | Floor, moves | Floor, moves with NISS | Floor, quarter turns | A scramble that meets the move floor |
|---:|---|---:|---:|---:|---:|---|
| 0 | 0 | 0.00% | 0 | 0 | 0 | (nothing) |
| 0 | 2 | 0.14% | 5 | 4 | 3 | `F R2 F' R2 F'` |
| 0 | 2 + 1 + 1 | 0.85% | 4 | 4 | 4 | `R' F' U F` |
| 0 | 2 + 2 | 0.85% | 6 | 4 | 4 | `U F' R' F R U'` |
| 0 | 2 + 2 + 2 | 0.56% | 5 | 3 | 3 | `R' U R2 F2 R'` |
| 0 | 3 + 2 + 1 | 1.69% | 5 | 4 | 4 | `F' U2 R' F' R` |
| 0 | 3 + 3 | 0.09% | 5 | 5 | 5 | `R U' R' U' R` |
| 0 | 4 | 0.21% | 1 | 1 | 1 | `U'` |
| 0 | 4 + 1 + 1 | 0.56% | 5 | 4 | 4 | `F' R' F2 R U` |
| 0 | 4 + 2 | 0.85% | 6 | 5 | 4 | `F' R F' R U F` |
| 0 | 6 | 0.05% | 5 | 4 | 3 | `U' R2 U F2 U'` |
| 1 | 1 + 1 | 1.41% | 5 | 5 | 5 | `R' F' U R' F` |
| 1 | 2 + 1 + 1 | 5.08% | 5 | 4 | 4 | `R U R F2 R'` |
| 1 | 2 + 2 | 1.27% | 6 | 5 | 5 | `F' R2 U R' U' F` |
| 1 | 2 + 2 + 2 | 0.85% | 6 | 5 | 5 | `R F U' R2 U' R` |
| 1 | 3 + 1 | 5.08% | 5 | 5 | 4 | `U R F U' R'` |
| 1 | 3 + 2 + 1 | 3.95% | 5 | 4 | 4 | `F R2 F R' U` |
| 1 | 3 + 3 | 0.85% | 4 | 3 | 3 | `R' F2 R' U'` |
| 1 | 4 + 1 + 1 | 0.85% | 3 | 3 | 3 | `F U' R` |
| 1 | 4 + 2 | 0.56% | 4 | 4 | 4 | `R' F U F` |
| 1 | 5 + 1 | 0.56% | 5 | 5 | 5 | `U F' U F' R` |
| 2 | 0 | 0.16% | 7 | 6 | 5 | `U F R F R' U' R'` |
| 2 | 1 + 1 | 2.82% | 3 | 3 | 3 | `F' R F` |
| 2 | 2 | 2.82% | 5 | 4 | 4 | `U' R F2 R' U` |
| 2 | 2 + 1 + 1 | 10.16% | 4 | 3 | 3 | `U' R' F2 U'` |
| 2 | 2 + 2 | 6.35% | 2 | 2 | 2 | `R' F'` |
| 2 | 3 + 1 | 5.08% | 5 | 4 | 4 | `U F U' F U` |
| 2 | 4 | 1.27% | 4 | 4 | 4 | `U' F' R U'` |
| 3 | 0 | 0.27% | 7 | 6 | 6 | `U' F U' F U F2 U` |
| 3 | 1 + 1 | 8.47% | 4 | 3 | 3 | `R F' U2 F` |
| 3 | 2 | 2.82% | 5 | 4 | 4 | `R U F' R2 U'` |
| 3 | 2 + 1 + 1 | 6.77% | 4 | 3 | 3 | `R' U2 F' U` |
| 3 | 2 + 2 | 2.96% | 5 | 4 | 4 | `U R U2 F' R'` |
| 3 | 3 + 1 | 5.08% | 5 | 4 | 4 | `R' F' U R' U'` |
| 3 | 4 | 0.42% | 4 | 4 | 4 | `F' U F' R` |
| 4 | 0 | 0.82% | 4 | 2 | 2 | `U F2 U2 F'` |
| 4 | 1 + 1 | 7.05% | 4 | 4 | 4 | `U' R' F' U'` |
| 4 | 2 | 4.23% | 5 | 3 | 3 | `U R' F2 U2 F'` |
| 5 | 0 | 0.82% | 5 | 4 | 4 | `F' R U2 F R'` |
| 5 | 1 + 1 | 3.10% | 3 | 3 | 3 | `R' U' F'` |
| 5 | 2 | 1.41% | 5 | 4 | 4 | `U R2 F U R'` |
| 6 | 0 | 0.60% | 5 | 4 | 3 | `R F R2 U R` |
| 7 | 0 | 0.16% | 7 | 6 | 5 | `U' R U2 F' R' U2 F` |

How to use it: your state can't be done in fewer than the row says. Nothing more: leaving out the all-good row, the mean distance of the states in a row is between 6.92 and 8.29 whatever the row, so the floor is usually far below the truth. It's on average 4.34 moves.

What the table is good for is the rows that stand out:

- **No out corner, some twisted**: with 2, 3 or 7 twisted corners these are the most expensive patterns there are.

| Twisted corners, nothing out | States | Fewest moves | Mean moves | Most moves | Fewest quarter turns | A scramble at the fewest | Its solution to HTR |
|---:|---:|---:|---:|---:|---:|---|---|
| 2 | 6,048 | 7 | 8.10 | 10 | 5 | `U F R F R' U' R'` | `R U R F' R' F' U` |
| 3 | 10,080 | 7 | 8.29 | 9 | 6 | `U' F U' F U F2 U` | `U' F2 U' F' U F' U` |
| 4 | 30,240 | 4 | 7.74 | 10 | 2 | `U F2 U2 F'` | `F U2 F2 U` |
| 5 | 30,240 | 5 | 7.94 | 10 | 4 | `F' R U2 F R'` | `R F' U2 R' F` |
| 6 | 22,176 | 5 | 7.98 | 10 | 3 | `R F R2 U R` | `R' U' R2 F' R` |
| 7 | 6,048 | 7 | 7.90 | 10 | 5 | `U' R U2 F' R' U2 F` | `F' U2 R F U2 R' U` |

- **Two out corners and nothing else** (the row 0 twisted, out 2): 5 moves and 3 quarter turns. That's 2c3 as the best case, and it's the same off the DR axis.
- **One twisted corner** never comes alone with nothing out, and with a pair of out corners (1 twisted, out 1 + 1) it's at least 5 moves and 5 quarter turns.

### 6.4 The 9 − k rule

From 5.1: a fake HTR is exactly 9 moves from HTR. So if you've found k moves that make every corner good and the result is fake, HTR is at least 9 − k away, on one side. With a short way to a fake HTR that's the best floor you'll get by hand:

```
U R' F U F2 R' F' R2 F      // types r r - u f f f
F' R2 U' F2 U F                  // all good in 6, but it's a fake HTR
```

Here the types floor is 6 and 9 − 6 = 3 says nothing more. The true distance is 8. The rule earns its keep when k is small: 2 moves from a fake HTR means at least 7 from the real one.

### 6.5 Floors in quarter turns

The same ladder with half turns free.

| Floor | How you get it | Mean floor (quarter turns) | States where it is exact | Exact or 1 short | Most it is short by |
|---|---|---:|---:|---:|---:|
| weight / 4 | at a glance | 2.29 | 0.5% | 8.9% | 6 |
| count table | at a glance | 3.51 | 13.0% | 50.4% | 5 |
| twist flat, read the subset | a subset read | 3.52 | 34.7% | 34.7% | 8 |
| types floor | table, or a search | 4.16 | 33.2% | 80.8% | 4 |
| types + parity | table, or a search | 4.66 | 80.8% | 80.8% | 4 |
| types + parity, and the subset read | table, or a search | 4.70 | 83.0% | 83.0% | 2 |
| the true count | computer | 5.04 | 100.0% | 100.0% | 0 |

- **Twist flat, read the subset** is beef beans' count. It's a floor because any solution also solves the placement. It's exact on 34.7% of states and never off by an odd number (section 8).
- **The types floor in quarter turns** is the smallest count any state with those types can have. Think of it as the look-alike number: 1 for a 4a face, 2 for bars, 3 for two out corners, like the first numbers of the subsets with those shapes.
- With parity it's exact on 80.8%, and with the subset read on top 83.0%.

### 6.6 With NISS

Two things to know.

**Every floor in quarter turns holds with NISS.** Moves on the inverse can't save a quarter turn: the count is the same on the inverse, and each quarter turn on either side changes it by 1. So weight / 4, the count table's quarter-turn column, the subset read and the types floor in quarter turns are all safe, and the number of quarter turns is itself a floor in moves.

**The one-sided move floors don't.** HTR isn't a normal subgroup, so a state can be far from HTR on normal and close with one move on the inverse:

```
F R2 F2 U2     // types . f f . f . f, types floor 4, and it is 4 moves on one side
(F)            // one move on the inverse and it's HTR: 1 with NISS
```

The one-sided types floor is too high for 14.2% of states once NISS is allowed, by up to 3 moves. The floors that hold with NISS, measured against the distance with NISS:

| Floor that holds with NISS | Mean floor (moves) | States where it is exact | Exact or 1 short | Most it is short by |
|---|---:|---:|---:|---:|
| quarter turns | 5.04 | 5.2% | 34.2% | 6 |
| count table | 3.59 | 0.8% | 5.3% | 9 |
| types on both sides | 5.68 | 27.5% | 64.3% | 9 |
| types on both sides + parity | 6.05 | 44.0% | 78.0% | 7 |
| the true distance with NISS | 6.89 | 100.0% | 100.0% | 0 |

*Types on both sides* is the fewest moves, split any way between normal and inverse, that make every corner good. It needs the types on the inverse too, which is NISS tracing for the corners that aren't good. The count table has its own NISS column because the counts are the same on the inverse.

### 6.7 By hand, in order

1. Count twisted and out per axis. Look up the row. (*At a glance.*)
2. Weight / 4 if you only want quarter turns. (*At a glance.*)
3. If you can see how to make every corner good in k moves and you're sure nothing shorter does it, k is the types floor (one side). Check the end against section 5.3: HTR means k is the distance; fake means at least max(k, 9 − k). (*A search.*)
4. Parity tells you whether the number of quarter turns is even or odd. Add 1 to a quarter-turn floor of the wrong kind. (*Tracing.*)

## 7. Which turn gets closer

One row per distance. *Turns that get closer* is how many of the nine turns lower the distance. Each rule column is how often the turn that makes its floor smallest gets closer; when several turns tie, they share the credit.

| Moves to HTR | Share of states | Turns that get closer (of 9) | A random turn | Follow the types floor | Types + parity floor | Types + D-colour floor | The larger of those two |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.00% | 2.00 | 22.2% | 100.0% | 100.0% | 100.0% | 100.0% |
| 2 | 0.01% | 1.00 | 11.1% | 100.0% | 100.0% | 100.0% | 100.0% |
| 3 | 0.06% | 1.06 | 11.8% | 100.0% | 100.0% | 100.0% | 100.0% |
| 4 | 0.37% | 1.02 | 11.3% | 100.0% | 100.0% | 100.0% | 100.0% |
| 5 | 1.78% | 1.15 | 12.8% | 96.4% | 98.2% | 99.4% | 100.0% |
| 6 | 8.07% | 1.19 | 13.3% | 75.1% | 85.5% | 96.1% | 100.0% |
| 7 | 29.31% | 1.38 | 15.3% | 33.8% | 62.7% | 76.7% | 96.3% |
| 8 | 49.36% | 2.27 | 25.2% | 25.9% | 36.9% | 48.2% | 64.2% |
| 9 | 10.93% | 5.62 | 62.5% | 64.3% | 65.5% | 67.0% | 69.9% |
| 10 | 0.10% | 6.08 | 67.5% | 90.4% | 84.6% | 90.2% | 84.9% |
| all states | 100.00% | 2.27 | 25.2% | 38.0% | 52.9% | 63.6% | 78.0% |

- **Within 4 moves the types are always right.** A fake HTR is 9 away, so anything within 4 of HTR is at least 5 from every fake one, and the nearest all-good state is the real one. For a state that close, any shortest way to all good is a shortest way to HTR. (You don't know it's that close until you've checked the end: of the states with a way to all good in 4 or less, 16.7% are.)
- **At 5 and 6 they're mostly right** (96.4%, 75.1%), and the two extra reads fix what's left: with parity and the D-colour corners the floor's turn is right every time up to 6.
- **At 8, where half of all states are, the types floor is a random turn** (25.9% against 25.2%). At 7 it beats chance (33.8% against 15.3%) and is still wrong two times in three. By then the types floor is mostly pointing at a fake HTR.
- **At 9 and 10 most turns get closer anyway.**

Following a floor needs the floor of all nine results, so every rule column is *a search* at best and *computer only* far out. What a human can actually do is in the first bullet.

How far could any rule go that reads the same things? Two answers.

**The best single table.** For each thing you can see, write down the one turn that gets closer for the most states showing it. Over all states no rule on that read does better. Here's how that table does by distance:

| Moves to HTR | Best table on the counts | Best table on the types | On types + parity | On types + D-colour corners |
|---|---:|---:|---:|---:|
| 1 | 33.3% | 0.0% | 33.3% | 33.3% |
| 2 | 11.1% | 0.0% | 27.8% | 31.5% |
| 3 | 12.5% | 10.4% | 25.0% | 39.9% |
| 4 | 7.8% | 20.3% | 16.2% | 52.5% |
| 5 | 13.4% | 25.0% | 29.9% | 58.0% |
| 6 | 13.9% | 29.3% | 46.9% | 54.7% |
| 7 | 17.1% | 37.2% | 57.6% | 59.2% |
| 8 | 26.4% | 55.5% | 67.6% | 74.2% |
| 9 | 67.0% | 91.1% | 92.7% | 95.0% |
| 10 | 89.7% | 100.0% | 100.0% | 98.3% |
| all states | 26.9% | 51.3% | 64.9% | 70.1% |

- **On the types the best table is right 51.3% of the time**, against 38.0% for following the types floor and 25.2% for a random turn. It gets there by playing the far states, where nearly all states are, and it's wrong near HTR, where following the floor is always right. With 25,515 patterns it's not a table for a person either.
- **The counts carry nothing about the turn**: the best table on them is a random turn.

**A bound that holds even if you knew the distance.** Take each distance on its own and pick the best turn for each thing you can see among the states at that distance. No rule on that read can do better there. A real rule doesn't know the distance, so it does worse.

| Moves to HTR | Bound on the counts | Bound on the types | On types + parity | On types + D-colour corners | On all three |
|---|---:|---:|---:|---:|---:|
| 1 | 33.3% | 100.0% | 100.0% | 100.0% | 100.0% |
| 2 | 22.2% | 100.0% | 100.0% | 100.0% | 100.0% |
| 3 | 18.8% | 100.0% | 100.0% | 100.0% | 100.0% |
| 4 | 20.7% | 100.0% | 100.0% | 100.0% | 100.0% |
| 5 | 20.3% | 97.4% | 99.1% | 99.4% | 100.0% |
| 6 | 16.5% | 83.8% | 89.9% | 97.7% | 100.0% |
| 7 | 17.7% | 61.4% | 80.8% | 86.7% | 100.0% |
| 8 | 26.7% | 66.0% | 80.0% | 87.5% | 100.0% |
| 9 | 68.4% | 98.3% | 99.3% | 99.7% | 100.0% |
| 10 | 92.3% | 100.0% | 100.0% | 100.0% | 100.0% |
| all states | 27.7% | 70.4% | 83.6% | 89.7% | 100.0% |

- **On the types nothing can beat 61.4% at 7 or 66.0% at 8.** No rule of thumb on the types is going to tell you the turn from 7 or 8 out.
- **With all three reads the turn is determined**, since the distance is. The catch is the size of that table.

The rules of thumb I tried, for the record. Lowering the weight works exactly as far as you look ahead, and going for the shortest CO helps up to about 5 moves out. Past that both are a random turn.

| Moves to HTR | A random turn | Lowest weight after the turn | Lowest weight within 2 turns | Lowest weight within 3 turns | Shortest CO on any axis after the turn |
|---|---:|---:|---:|---:|---:|
| 1 | 22.2% | 100.0% | 66.7% | 22.2% | 40.0% |
| 2 | 11.1% | 40.0% | 100.0% | 30.6% | 40.0% |
| 3 | 11.8% | 14.7% | 42.9% | 100.0% | 85.0% |
| 4 | 11.3% | 15.1% | 20.2% | 19.9% | 73.8% |
| 5 | 12.8% | 15.9% | 24.1% | 23.7% | 58.9% |
| 6 | 13.3% | 16.1% | 15.6% | 18.5% | 29.4% |
| 7 | 15.3% | 16.7% | 18.2% | 15.6% | 22.9% |
| 8 | 25.2% | 25.9% | 24.5% | 28.1% | 27.9% |
| 9 | 62.5% | 65.2% | 62.9% | 62.5% | 60.0% |
| 10 | 67.5% | 76.7% | 80.7% | 77.8% | 92.3% |
| all states | 25.2% | 26.5% | 26.2% | 27.4% | 30.9% |

With NISS there are 18 turns to choose from, 9 on each side:

| Moves to HTR with NISS | Share of states | Turns that get closer (of 18) | A random turn | Follow the types floor (both sides) | Types + parity floor (both sides) |
|---|---:|---:|---:|---:|---:|
| 1 | 0.00% | 2.18 | 12.1% | 100.0% | 100.0% |
| 2 | 0.02% | 1.75 | 9.7% | 100.0% | 100.0% |
| 3 | 0.15% | 1.86 | 10.3% | 98.1% | 98.9% |
| 4 | 0.90% | 1.88 | 10.4% | 94.0% | 95.4% |
| 5 | 4.66% | 2.14 | 11.9% | 82.4% | 89.5% |
| 6 | 20.70% | 2.38 | 13.2% | 44.5% | 63.6% |
| 7 | 51.42% | 3.56 | 19.8% | 23.4% | 32.2% |
| 8 | 21.96% | 9.11 | 50.6% | 52.1% | 52.0% |
| 9 | 0.20% | 16.34 | 90.8% | 95.1% | 93.4% |

**So, by hand:** read the types. If you can see a way to all good in 4 or less, it's the way to HTR as long as the end is HTR (section 5.3), and that check costs a glance at the D-colour corners plus parity. Further out, the reads give you floors to cut branches with, not the turn. Searching is the method there, and rodneykinney's verdict on the one-axis maze fits the 3D one too: "Still too complicated to keep in your head, IMO" ([20 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1154064564946739200)).

<figure>
<svg viewBox="0 0 720 560" width="720" role="img" aria-label="Flow chart: reading the corners for a floor and for the next turn" style="max-width:100%;height:auto;color:var(--fg);font:14px system-ui,sans-serif" fill="currentColor"><title>Flow chart: reading the corners for a floor and for the next turn</title><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker></defs><rect x="20" y="20" width="330" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="185.0" y="49.0" text-anchor="middle" font-weight="650">1. Type every corner</text><text x="185.0" y="64.0" text-anchor="middle">3 oriented stickers: good. 1: out. 0: twisted.</text><rect x="20" y="130" width="330" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="185.0" y="166.5" text-anchor="middle" font-weight="650">2. Are they all good?</text><rect x="20" y="240" width="330" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="185.0" y="269.0" text-anchor="middle" font-weight="650">3. Count twisted, and out per axis</text><text x="185.0" y="284.0" text-anchor="middle">The count table gives a floor.</text><rect x="20" y="350" width="330" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="185.0" y="379.0" text-anchor="middle" font-weight="650">4. Can you see how to make them</text><text x="185.0" y="394.0" text-anchor="middle">all good in 4 turns or less?</text><rect x="20" y="460" width="330" height="78" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="185.0" y="488.5" text-anchor="middle" font-weight="650">5. Further out</text><text x="185.0" y="503.5" text-anchor="middle">The types don't tell the closer turn.</text><text x="185.0" y="518.5" text-anchor="middle">Cut with the floors, then search.</text><line x1="185.0" y1="84.0" x2="185.0" y2="130.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#arr)"/><line x1="185.0" y1="194.0" x2="185.0" y2="240.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#arr)"/><line x1="185.0" y1="304.0" x2="185.0" y2="350.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#arr)"/><line x1="185.0" y1="414.0" x2="185.0" y2="460.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#arr)"/><text x="195.0" y="222.0" text-anchor="start" font-size="12">no</text><text x="195.0" y="442.0" text-anchor="start" font-size="12">no</text><rect x="420" y="110" width="280" height="104" rx="6" fill="none" stroke="currentColor" stroke-width="1.2"/><text x="560.0" y="144.0" text-anchor="middle">D-colour corners in a 4a picture,</text><text x="560.0" y="159.0" text-anchor="middle">and parity even?</text><text x="560.0" y="174.0" text-anchor="middle">Yes: HTR.</text><text x="560.0" y="189.0" text-anchor="middle">No: fake HTR, exactly 9 moves away.</text><line x1="350.0" y1="162.0" x2="420.0" y2="162.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#arr)"/><text x="384.0" y="154.0" text-anchor="middle" font-size="12">yes</text><rect x="420" y="330" width="280" height="104" rx="6" fill="none" stroke="currentColor" stroke-width="1.2"/><text x="560.0" y="364.0" text-anchor="middle">That is the shortest way to all good.</text><text x="560.0" y="379.0" text-anchor="middle">It ends in HTR for 1 state in 6</text><text x="560.0" y="394.0" text-anchor="middle">that look like yours: check the end</text><text x="560.0" y="409.0" text-anchor="middle">the way step 2 does.</text><line x1="350.0" y1="382.0" x2="420.0" y2="382.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#arr)"/><text x="384.0" y="374.0" text-anchor="middle" font-size="12">yes</text></svg>
<figcaption>Reading the corners, in order.</figcaption>
</figure>

## 8. Quarter turns in 3D

### 8.1 The count, and the subset number inside it

The fewest quarter turns into HTR with half turns free goes from 0 to 8 (table in section 3, Jules Porteners' numbers). For a DR it's the number in the subset name.

beef beans' count ([21 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143384156198416426)) is that number for the *placement*: forget the twists and read the subset. It doesn't depend on the axis you'd twist to, which checks out for all 5,040 placements and all three axes, and it has the distribution FakeMMAP posted ([26 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1144917908078723112)):

| Subset number | Placements (of 5,040) | In cases of 24 | Share |
|---|---:|---:|---:|
| 0 | 24 | 1 | 0.5% |
| 1 | 144 | 6 | 2.9% |
| 2 | 720 | 30 | 14.3% |
| 3 | 1,416 | 59 | 28.1% |
| 4 | 1,776 | 74 | 35.2% |
| 5 | 960 | 40 | 19.0% |

You don't have to twist anything in your head to read it. It's hyperparity with the stickers left where they are: the shape of the out corners (section 4.1), the picture of the D-colour corners (section 5.3) and parity. Those are rodneykinney's FB label, UD label and parity, and the number is the one in the maze, with the maze's own sub-cases where two states share a cell.

### 8.2 What the twist costs

zakimoshi's catch was that "orienting corners requires you to change the qt" ([23 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143786175438532709)). Here's by how much. True count minus the subset number of the placement:

| Extra quarter turns the twist costs | States | Share |
|---|---:|---:|
| 0 | 1,274,064 | 34.68% |
| 2 | 2,019,456 | 54.96% |
| 4 | 360,864 | 9.82% |
| 6 | 19,392 | 0.53% |
| 8 | 384 | 0.01% |

It's always even, since parity is the same for both. So the subset number is the true count for 34.7% of all states and 2 short for 55.0%.

By how many corners are twisted:

| Twisted corners | States | Costs nothing | Costs 2 | Costs 4 or more | Mean cost (quarter turns) |
|---|---:|---:|---:|---:|---:|
| 0 | 215,280 | 42.2% | 55.4% | 2.4% | 1.20 |
| 1 | 751,680 | 29.7% | 58.6% | 11.7% | 1.65 |
| 2 | 1,053,216 | 33.2% | 53.1% | 13.7% | 1.62 |
| 3 | 984,672 | 38.1% | 50.4% | 11.6% | 1.48 |
| 4 | 444,960 | 36.2% | 61.4% | 2.4% | 1.33 |
| 5 | 196,128 | 35.8% | 60.1% | 4.1% | 1.42 |
| 6 | 22,176 | 18.0% | 45.9% | 36.1% | 2.53 |
| 7 | 6,048 | 0.0% | 52.4% | 47.6% | 3.29 |

### 8.3 Out corners: the same maze as in DR

<figure>
<svg viewBox="0 0 720 330" width="720" role="img" aria-label="The out corners: shapes, and where a quarter turn can take them" style="max-width:100%;height:auto;color:var(--fg);font:14px system-ui,sans-serif" fill="currentColor"><title>The out corners: shapes, and where a quarter turn can take them</title><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker></defs><rect x="40" y="130" width="120" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="100.0" y="151.5" text-anchor="middle" font-weight="650">0c</text><text x="100.0" y="166.5" text-anchor="middle">no corner out</text><text x="100.0" y="181.5" text-anchor="middle">0 qt</text><rect x="200" y="130" width="120" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="260.0" y="151.5" text-anchor="middle" font-weight="650">4a</text><text x="260.0" y="166.5" text-anchor="middle">4 out, like a face</text><text x="260.0" y="181.5" text-anchor="middle">at least 1 qt</text><rect x="380" y="130" width="120" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="440.0" y="151.5" text-anchor="middle" font-weight="650">4b</text><text x="440.0" y="166.5" text-anchor="middle">4 out, bars</text><text x="440.0" y="181.5" text-anchor="middle">at least 2 qt</text><rect x="560" y="60" width="120" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="620.0" y="81.5" text-anchor="middle" font-weight="650">2c</text><text x="620.0" y="96.5" text-anchor="middle">2 out</text><text x="620.0" y="111.5" text-anchor="middle">at least 3 qt</text><rect x="560" y="210" width="120" height="64" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="620.0" y="231.5" text-anchor="middle" font-weight="650">6c</text><text x="620.0" y="246.5" text-anchor="middle">6 out</text><text x="620.0" y="261.5" text-anchor="middle">at least 3 qt</text><line x1="160.0" y1="162.0" x2="200.0" y2="162.0" stroke="currentColor" stroke-width="1.2"/><line x1="320.0" y1="162.0" x2="380.0" y2="162.0" stroke="currentColor" stroke-width="1.2"/><line x1="500.0" y1="162.0" x2="560.0" y2="92.0" stroke="currentColor" stroke-width="1.2"/><line x1="500.0" y1="162.0" x2="560.0" y2="242.0" stroke="currentColor" stroke-width="1.2"/><line x1="620.0" y1="124.0" x2="620.0" y2="210.0" stroke="currentColor" stroke-width="1.2"/><path d="M 246.0 130 C 230.0 96, 290.0 96, 274.0 130" fill="none" stroke="currentColor" stroke-width="1.2"/><text x="260.0" y="100.0" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">can stay</text><text x="260.0" y="100.0" text-anchor="middle" font-size="12">can stay</text><path d="M 606.0 60 C 590.0 26, 650.0 26, 634.0 60" fill="none" stroke="currentColor" stroke-width="1.2"/><text x="620.0" y="30.0" text-anchor="middle" font-size="12" stroke="var(--bg)" stroke-width="5" stroke-linejoin="round" fill="var(--bg)">can stay</text><text x="620.0" y="30.0" text-anchor="middle" font-size="12">can stay</text><text x="360.0" y="300.0" text-anchor="middle" font-size="12">One line = one quarter turn of R, U or F. Half turns never change the shape.</text><text x="360.0" y="318.0" text-anchor="middle" font-size="12">4a: on one face, or on one after half turns. 0c and 4b always change. 6 out is 2c seen from the other side.</text></svg>
<figcaption>The shapes of the out corners: the FB orientation of Hyper-Parity, with turns on all three axes.</figcaption>
</figure>

*Hyper-Parity* says of U turns in a DR: "It is possible to remain in 4a or 2c, but not 0c or 4b." It's the same with all six quarter turns. With DBL held, 6 out corners is a shape of its own; it's 2c seen from the other side, and the subset names fold it in.

| Out corners | Share of states | Quarter turns to put them back | Fewest quarter turns to HTR | Mean quarter turns | Fewest moves to HTR | Mean moves |
|---|---:|---:|---:|---:|---:|---:|
| 0c | 2.86% | 0 | 0 | 5.61 | 0 | 7.93 |
| 4a | 17.14% | 1 | 1 | 5.15 | 1 | 7.70 |
| 4b | 34.29% | 2 | 2 | 5.02 | 2 | 7.55 |
| 2c | 34.29% | 3 | 3 | 4.99 | 3 | 7.54 |
| 6c | 11.43% | 3 | 3 | 4.99 | 3 | 7.54 |

### 8.4 Everything within 2 quarter turns

Up to half turns and the symmetries that keep DBL, here's every kind of type pattern that can be 1 or 2 quarter turns from HTR. *Of 6 look-alikes* is how many of the six HTR cases with those types (section 5.2) are really that close.

| Quarter turns | What you count | Type patterns | Of 6 look-alikes, this close | A scramble | Its types | Its moves to HTR |
|---:|---|---:|---:|---|---|---:|
| 1 | 4 out (4a) | 18 | 1 of 6 | `U'` | `u u u u . . .` | 1 |
| 2 | 2 + 2 out, 2 twisted | 36 | 1 of 6 | `F U2 R` | `+ . f r r f +` | 3 |
| 2 | 2 + 2 out, 2 twisted | 144 | 1 of 6 | `R' F'` | `- + . r f f r` | 2 |
| 2 | 4 out (4a) | 18 | 1 of 6 | `R' U2 R2 F2 R'` | `. . r r r r .` | 5 |
| 2 | 4 out (4b) | 36 | 2 of 6 | `F' R2 F` | `. . . f f f f` | 3 |
| 2 | 4 twisted | 12 | 1 of 6 | `U F2 U2 F'` | `+ - . . - + .` | 4 |

<figure>
<svg viewBox="0 0 720 500" width="720" role="img" aria-label="Every kind of corner pattern within two quarter turns of HTR" style="max-width:100%;height:auto;color:var(--fg);font:14px system-ui,sans-serif" fill="currentColor"><title>Every kind of corner pattern within two quarter turns of HTR</title><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker></defs><text x="130.0" y="22.0" text-anchor="middle" font-weight="650">2 quarter turns</text><text x="380.0" y="22.0" text-anchor="middle" font-weight="650">1 quarter turn</text><text x="640.0" y="22.0" text-anchor="middle" font-weight="650">HTR</text><rect x="20" y="40" width="230" height="70" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="135.0" y="64.5" text-anchor="middle" font-weight="650">4 out (4a)</text><text x="135.0" y="79.5" text-anchor="middle">R' U2 R2 F2 R'</text><text x="135.0" y="94.5" text-anchor="middle">really 2 qt: 1 of 6</text><rect x="20" y="124" width="230" height="70" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="135.0" y="148.5" text-anchor="middle" font-weight="650">4 out (4b)</text><text x="135.0" y="163.5" text-anchor="middle">F' R2 F</text><text x="135.0" y="178.5" text-anchor="middle">really 2 qt: 2 of 6</text><rect x="20" y="208" width="230" height="70" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="135.0" y="232.5" text-anchor="middle" font-weight="650">2 + 2 out, 2 twisted</text><text x="135.0" y="247.5" text-anchor="middle">F U2 R</text><text x="135.0" y="262.5" text-anchor="middle">really 2 qt: 1 of 6</text><rect x="20" y="292" width="230" height="70" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="135.0" y="316.5" text-anchor="middle" font-weight="650">2 + 2 out, 2 twisted</text><text x="135.0" y="331.5" text-anchor="middle">R' F'</text><text x="135.0" y="346.5" text-anchor="middle">really 2 qt: 1 of 6</text><rect x="20" y="376" width="230" height="70" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="135.0" y="400.5" text-anchor="middle" font-weight="650">4 twisted</text><text x="135.0" y="415.5" text-anchor="middle">U F2 U2 F'</text><text x="135.0" y="430.5" text-anchor="middle">really 2 qt: 1 of 6</text><rect x="300" y="208" width="200" height="70" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="400.0" y="232.5" text-anchor="middle" font-weight="650">4 out (4a)</text><text x="400.0" y="247.5" text-anchor="middle">U'</text><text x="400.0" y="262.5" text-anchor="middle">really 1 qt: 1 of 6</text><rect x="560" y="208" width="140" height="70" rx="6" fill="var(--soft)" stroke="currentColor" stroke-width="1.2"/><text x="630.0" y="232.5" text-anchor="middle" font-weight="650">all good</text><text x="630.0" y="247.5" text-anchor="middle">really HTR:</text><text x="630.0" y="262.5" text-anchor="middle">1 of 6</text><line x1="250.0" y1="75.0" x2="300.0" y2="243.0" stroke="currentColor" stroke-width="1.2"/><line x1="250.0" y1="159.0" x2="300.0" y2="243.0" stroke="currentColor" stroke-width="1.2"/><line x1="250.0" y1="243.0" x2="300.0" y2="243.0" stroke="currentColor" stroke-width="1.2"/><line x1="250.0" y1="327.0" x2="300.0" y2="243.0" stroke="currentColor" stroke-width="1.2"/><line x1="250.0" y1="411.0" x2="300.0" y2="243.0" stroke="currentColor" stroke-width="1.2"/><line x1="500.0" y1="243.0" x2="560.0" y2="243.0" stroke="currentColor" stroke-width="1.2"/><text x="360.0" y="478.0" text-anchor="middle" font-size="12">Each box: what you count, a scramble that makes it, and how many of the six states that look</text><text x="360.0" y="494.0" text-anchor="middle" font-size="12">alike are that close. One line = one quarter turn, after half turns to set it up.</text></svg>
<figcaption>The 3D funnel down to HTR. Compare the right end of the Corner Case Funnel in Hyper-Parity: 4a1 is the same, 4b2 and 4a2 are two of the five.</figcaption>
</figure>

So off the DR axis there are three new 2-qt kinds, and they're what two quarter turns on *different* axes leave behind:

```
R' F'          // two faces sharing an edge: 2 twisted where they overlap, 2 + 2 out
F U2 R         // the same with a half turn between: the out corners are now a 4a shape
U F2 U2 F'     // both turns on the same four corners: 4 twisted, nothing out
```

The last one looks awful and is 2 quarter turns (4 moves) in the one case in six where it's real. It's a special arrangement, though: the four twisted corners sit on one face after half turns, two twisted each way. Of the 210 type patterns with 4 twisted corners and nothing out, 12 can be that close; 192 need 4 or 5 quarter turns at best.

### 8.5 Which quarter turn lowers the count

JTuu's question was whether you can know "whether each qt is +1 or -1 just by looking at the moves" ([22 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143452357611499540)). Looking at the corners, here's how often a rule picks a quarter turn that lowers the count. Half turns are free, so the choice is a setup plus a quarter turn, and states that differ by half turns at the end count as one *position* (153,090 of them; the HTR one is left out of the table).

| Quarter turns to HTR | Positions | A random setup and turn | Lowest types floor | Types + parity | Lowest subset number | Types + parity and subset number |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 18 | 5.6% | 100.0% | 100.0% | 33.3% | 100.0% |
| 2 | 282 | 6.0% | 80.9% | 87.2% | 32.6% | 100.0% |
| 3 | 3,591 | 7.4% | 87.9% | 87.9% | 16.5% | 95.7% |
| 4 | 32,502 | 10.2% | 72.6% | 74.6% | 16.6% | 89.6% |
| 5 | 71,184 | 41.0% | 68.8% | 61.9% | 43.7% | 58.9% |
| 6 | 43,744 | 96.0% | 98.5% | 98.2% | 92.6% | 97.8% |
| 7 | 1,752 | 99.1% | 100.0% | 100.0% | 94.5% | 100.0% |
| 8 | 16 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| all but HTR | 153,089 | 50.0% | 78.9% | 76.1% | 51.8% | 78.0% |

- Up to 4 quarter turns out, the types pick a lowering turn 73% to 100% of the time, and with parity and the subset number 90% to 100%.
- At 5, where most states are, the best column is the types at 69%, and at 6 and above nearly every quarter turn lowers the count anyway.
- The subset number alone is a bad guide. It only knows the placement, and the turn that helps the placement often wrecks the twist.

## 9. DR corners, seen from outside DR

### 9.1 No quarter turn is saved

For a DR state, allowing quarter turns on the other two axes never lowers the number of quarter turns into HTR. The subset number is the 3D count, for all 5,040 DR corner states. That's FakeMMAP's argument ([23 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143847973789384825)) read the other way: swap every off-axis quarter turn of a solution for [D2 L2 : U'] and friends and you have a DR solution with as many quarter turns. So a 4b5 is 5 quarter turns no matter what you allow.

### 9.2 Moves are saved

One row per subset. A *case* here is 24 states that differ by half turns done before the scramble, so they have the same solutions into HTR (210 cases in all). *DR turns* is U and the half turns; *all turns* adds R and F quarter turns.

| Subset | Cases (of 210) | DR turns: fewest | DR turns: most | All turns: fewest | All turns: most | Cases 1 shorter | Cases 2 shorter |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0c0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4a1 | 6 | 1 | 4 | 1 | 4 | 0 | 0 |
| 4a2 | 6 | 5 | 8 | 5 | 8 | 0 | 0 |
| 4b2 | 24 | 3 | 6 | 3 | 6 | 0 | 0 |
| 0c3 | 3 | 9 | 10 | 9 | 9 | 2 | 0 |
| 2c3 | 32 | 5 | 6 | 5 | 6 | 0 | 0 |
| 4a3 | 12 | 7 | 9 | 7 | 9 | 0 | 0 |
| 4b3 | 12 | 7 | 8 | 7 | 8 | 0 | 0 |
| 0c4 | 2 | 9 | 9 | 9 | 9 | 0 | 0 |
| 2c4 | 48 | 7 | 9 | 7 | 9 | 24 | 0 |
| 4a4 | 12 | 9 | 11 | 9 | 9 | 4 | 6 |
| 4b4 | 12 | 9 | 10 | 9 | 9 | 8 | 0 |
| 2c5 | 16 | 9 | 11 | 8 | 9 | 8 | 8 |
| 4b5 | 24 | 9 | 10 | 8 | 8 | 16 | 8 |

- 126 of the 210 cases are no shorter off-axis, 62 are 1 move shorter and 22 are 2 shorter.
- **Every 5-qt case is shorter off-axis**, and so is most of 4a4 and 4b4.
- Inside DR the longest way into HTR is 11, which is Yura Riabov's "11 to htr" ([12 May 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1239371562776268840)). With all turns it's 9.

```
R2 U' R2 U F2 U' F2 U R2 U' R2     // a 2c5
R2 U R2 U F2 U' R2 U F2 U     // 10 in DR turns
R F R' F2 R U' R U     // 8 with all turns
```

The shorter way costs quarter turns. Of the 84 cases that are shorter off-axis, the shortest solutions keep to the subset number in 2; in 64 they use 2 more quarter turns and in 18 they use 4 more. The 8-mover above has 7, where the DR solution has 5. So leaving DR trades half turns for quarter turns.

zakimoshi and torchlight had seen the same thing for full corner solutions of one case ("You can definitely under 12 if you leave DR", [12 May 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1239378987508301915); "there are some 12-move sols if you use the DR-breaking 2c4 triggers", [12 May 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1239391757339459657)). It's corners only: off-axis turns break the DR on the edges, which is why nobody does this in an attempt without a reason.

The same with NISS. Joba's assumed bounds ([13 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1349876840914751578)) are the *fewest* column of the DR side: 1, 2, 4, 6, 8 for 1 to 5 quarter turns, and 0c3 is the exception at 6, as Zagros said ("There's no U (U R2 U) with 0c3, it would have to be U (U R2 U2 F2 U)", [13 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1349806710105313392)).

| Subset | DR turns + NISS: fewest | Most | Mean | All turns + NISS: fewest | Most | Mean |
|---|---:|---:|---:|---:|---:|---:|
| 0c0 | 0 | 0 | 0.00 | 0 | 0 | 0.00 |
| 4a1 | 1 | 4 | 1.97 | 1 | 4 | 1.97 |
| 4a2 | 2 | 8 | 5.00 | 2 | 8 | 5.00 |
| 4b2 | 2 | 6 | 3.94 | 2 | 6 | 3.94 |
| 0c3 | 6 | 9 | 7.94 | 6 | 9 | 7.50 |
| 2c3 | 4 | 6 | 5.17 | 4 | 6 | 5.17 |
| 4a3 | 4 | 8 | 6.06 | 4 | 7 | 6.00 |
| 4b3 | 4 | 8 | 6.06 | 4 | 7 | 6.00 |
| 0c4 | 6 | 7 | 6.67 | 6 | 7 | 6.33 |
| 2c4 | 6 | 9 | 7.12 | 6 | 7 | 6.67 |
| 4a4 | 6 | 9 | 8.00 | 6 | 9 | 7.67 |
| 4b4 | 6 | 9 | 8.00 | 6 | 9 | 7.67 |
| 2c5 | 8 | 10 | 8.79 | 7 | 9 | 7.85 |
| 4b5 | 8 | 9 | 8.56 | 7 | 8 | 7.67 |

### 9.3 Going through DR costs

The usual route for corners is: orient them on an axis, then the subsets. Take the *optimal* orientation on an axis, and after it the best DR-only finish. How much longer than the optimal is that?

| Moves longer than the optimal | Orient on U/D first | Orient on the best of the three axes first |
|---|---:|---:|
| 0 | 12.9% | 32.3% |
| 1 | 12.2% | 23.4% |
| 2 | 16.3% | 22.4% |
| 3 | 15.6% | 12.3% |
| 4 | 15.3% | 6.1% |
| 5 | 14.0% | 2.7% |
| 6 | 8.8% | 0.6% |
| 7 | 3.8% | 0.1% |
| 8 | 1.0% | 0.0% |
| 9 | 0.1% | 0.0% |
| 10 | 0.0% | 0.0% |

On a fixed axis it's 3.12 moves longer on average, on the best of the three 1.48. Picking the axis with the shortest CO is no better than a fixed one (3.04): the short CO isn't the one that leaves a good subset. Jay asked for move counts to HTR from two axes ([29 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1334328007476641832)); this is the corner part of that.

### 9.4 CO on one axis

mrauo asked for the CO movecount distribution ([18 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1153267556719800381)). With R, U, F and DBL held there are 729 twist cases per axis:

| Moves to orient | Twist cases (of 729) | Share, one axis | Share, best of three axes |
|---|---:|---:|---:|
| 0 | 1 | 0.1% | 0.4% |
| 1 | 2 | 0.3% | 0.8% |
| 2 | 12 | 1.6% | 4.8% |
| 3 | 64 | 8.8% | 23.2% |
| 4 | 274 | 37.6% | 56.2% |
| 5 | 336 | 46.1% | 14.6% |
| 6 | 40 | 5.5% | 0.0% |

The mean is 4.44 on one axis and 3.78 on the best of three. By how many corners are misoriented for the axis (each cell is the share of that row):

| Corners misoriented for the axis | Share of states | 0 moves | 1 moves | 2 moves | 3 moves | 4 moves | 5 moves | 6 moves |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.1% | 100% | 0% | 0% | 0% | 0% | 0% | 0% |
| 2 | 5.8% | 0% | 0% | 0% | 0% | 29% | 57% | 14% |
| 3 | 9.6% | 0% | 0% | 0% | 29% | 57% | 14% | 0% |
| 4 | 28.8% | 0% | 1% | 4% | 10% | 39% | 42% | 4% |
| 5 | 28.8% | 0% | 0% | 0% | 0% | 34% | 60% | 6% |
| 6 | 21.1% | 0% | 0% | 3% | 12% | 31% | 45% | 9% |
| 7 | 5.8% | 0% | 0% | 0% | 10% | 48% | 43% | 0% |

Jay's version of the question was for the DR move set R L U D F2 B2 ([18 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1153280691384094750)), which this isn't: here F quarter turns are allowed. FakeMMAP gave the best case per number of misoriented corners for that move set ([19 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1153814132445937795)).

## 10. The mazes in one place

- **Types** (section 4.2): six types, nine lines. The rule for a quarter turn on any axis.
- **Out corners** (section 8.3): 0c, 4a, 4b, 2c and 6c, at 0, 1, 2, 3 and 3 quarter turns. rodneykinney's FB maze, unchanged.
- **D-colour corners** (section 5.3): 4a, 4b, 4c and 4d, at 0, 1, 2 and 1. rodneykinney's UD maze, unchanged.
- **The funnel** (section 8.4): the five 2-qt kinds and the 4a face.
- **The flow chart** (section 7).

Why there's no single 3D maze like the Hyper-Parity Maze: that one has 34 states because a DR corner has two types. With six types there are 25,515 type patterns, 1,284 up to half turns, each shared by six HTR cases. The three small mazes multiply out to that. The good news is that they're independent reads: types by the stickers' axes, the D-colour corners by one colour, parity by tracing.

## 11. The claims, checked

Everything from the server that this search can check. *Confirmed* means exactly, for every state. Corrections are on the errata page.

| Claim | Who and where | What the search says |
|---|---|---|
| 2x2x2 by quarter turns: 24, 432, 6768, 86184, 780048, 1708416, 1049856, 42048, 384 states at 0 to 8; "sometimes 8 qt is required" | Jules Porteners, [16 Apr 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1362033817325535253) | Confirmed, every number. |
| Quarter turns over all 7! corner cases: 24, 144, 720, 1416, 1776, 960 ("Can anyone check these stats") | FakeMMAP, [26 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1144917908078723112) | Confirmed. |
| "0c0:0c3:0c4:4a1:4a2:4a3:4a4:4b2:4b3:4b4:4b5:2c3:2c4:2c5=1:3:2:6:6:12:12:24:12:12:24:32:48:16" | Shota, [14 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1273446142226731079) | Confirmed: the cases column of 9.2. |
| The quarter-turn count of the placement is the same on every axis | beef beans, [21 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143384156198416426); proof by FakeMMAP, [23 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143847973789384825) | Confirmed for all 5,040 placements and three axes. |
| "R and [D2 L2 : U'] permute corners in the same way" | torchlight, [22 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143568556332691586) | Confirmed, and the same for L and [U2 L2 : U']. |
| "a way to see that twisting all the corners onto another axis doesn't change the subset: R2 U D L2 F B" | trangium, [13 Mar 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1482029128487141559) | Confirmed: it twists every corner and leaves the placement in HTR. |
| Six triple DRs up to half turns: "3 options for corners (3-cycle, inverse, solved) and 2 options for parity" | trig0n and Tom Nelson, [4 Jun 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1115045288609071164), [4 Jun 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1115047541281665155) | Confirmed: 144 = 6 × 24. |
| With DBL fixed the DR corners are 7!, HTR is 4!, and triple DR has index 6 over HTR | FakeMMAP, [1 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1367524395983175782) | Confirmed. |
| HTR when the two tetrads' placements agree up to the Klein 4-group; a 3-cycle apart is 0c4; anything else 0c3 | torchlight, [3 Oct 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1291448033787252736), [3 Oct 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1291448207208874014) | Confirmed on all 144: 24 agree, 48 are a 3-cycle apart (4 qt), 72 a swap or a 4-cycle (3 qt). |
| "Lemma 1: If triple DR and OBL are solved, and there is even parity, then the state is in true HTR." The even ones are U2, R2 F2 R2, R2 F2 R2 U2 and solved | FakeMMAP, [1 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412001179365408790) | Confirmed: exactly those 4 states, 8 without the parity condition. Section 5.3 is the version for all six pictures. |
| Bad corners are the "ones with exactly 1 oriented sticker" | zakimoshi, [10 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1404311546590527621) | Confirmed and proved (section 4.1). |
| A corner in its own tetrad is oriented or not whatever the axis | Sebastiano Tronto's H48 doc, quoted by Arch, [11 Jun 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1382436238446821467) | Confirmed and proved (section 4.1). |
| Distance to triple DR "is a lower bound to distance to HTR" | Louis, [30 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1334522555968782411) | Yes, and now measured: 6.41 against 7.58, exact on 30.9% (section 6.2). |
| You can determine the distance "only to fake htr" from the orientations | Zagros, [30 Jan 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1334533412928880712) | Confirmed and made exact: 1 in 6 (section 5.2). |
| "orienting corners requires you to change the qt" | zakimoshi, [23 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143786175438532709) | Measured (section 8.2): the twist costs nothing for 34.7% of states and 2, 4, 6 or 8 quarter turns for the rest. |
| With NISS, at least "2/1/2/4/6/8 moves for 0/1/2/3/4/5 qt cases for now, with the possible exception of 0c3" | Joba, [13 Mar 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1349876840914751578) | For corners, confirmed for 1 to 5 qt, and 0c3 is at 6 (section 9.2). I read the 2 for a 0-qt case as being about edges; corners in 0c0 need 0. |
| "11 to htr" for the longest DR corner case | Yura Riabov, [12 May 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1239371562776268840) | Confirmed, also on all eight corners with U, D and the six half turns. |
| An 11-move solution of wen's case off-axis: D2 F2 U' F' D F' R2 B U' B' D' | torchlight, [12 May 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1239391808585203763) | Confirmed: it solves that case. |
| Six <R,U,F> paths to HTR for R2 U R2 U' R2 U F2 U | rodneykinney, [24 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1144149392497065994) | All six reach HTR with 4 quarter turns, and the case is 4 qt. I didn't recount that there are no others. |
| "You can probably map the corner-position permutation (4c2c2c, 3c5c, 2c5c, etc.) directly to a quarter-turn count." | rodneykinney, [22 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143734842001985576) | Only partly: the cycles fix the parity and little else. A lone 3-cycle is always 4 qt. Table below. |
| "4a - 1/2 1q, 1/2 2q" | Lewis Isom, [14 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1273406691941159034) | True on Radek B's table ([14 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1273404063295475822)), which splits only the 2-qt cases with 4 bad corners by shape (6 cases each). With the sheet's letters 4a1 : 4a2 : 4a3 : 4a4 is 6 : 6 : 12 : 12. |
| "4e4c adds/subtracts 1 quarter turn", "4e2c is +- 2 qt", "2e3c is +- 3 qt" | beef beans, [21 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143384156198416426) | Depends on the reading. As the quarter turns in the trigger, each one adding or taking 1: yes, and that's how zakimoshi read it ("3 away then one closer or 2 away", [22 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143440084952170516)). As the net change of the subset number: R U2 R' leaves it alone for 60% of the DRs it makes and moves it by 2 for the rest, and R U R' moves it by 1 for 87.6% and by 3 for the rest. |
| The maze labels: UD 4a / 4b / 4c / 4d at 0 / 1 / 2 / 1 quarter turns, FB 0c / 4a / 4b / 2c at 0 / 1 / 2 / 3 | rodneykinney, *Hyper-Parity* | Confirmed, and unchanged with turns on all three axes (5.3, 8.3). |

rodneykinney's cycle-type idea, for the 5,040 placements with DBL in place. One row per cycle type, and how many placements of it have each subset number:

| Cycles of the placement | Placements | 0 qt | 1 qt | 2 qt | 3 qt | 4 qt | 5 qt |
|---|---:|---:|---:|---:|---:|---:|---:|
| 6c | 840 | 0 | 72 | 0 | 400 | 0 | 368 |
| 7c | 720 | 0 | 0 | 240 | 0 | 480 | 0 |
| 4c 2c | 630 | 6 | 0 | 180 | 0 | 444 | 0 |
| 5c | 504 | 0 | 0 | 72 | 0 | 432 | 0 |
| 5c 2c | 504 | 0 | 24 | 0 | 336 | 0 | 144 |
| 3c 2c | 420 | 0 | 0 | 0 | 276 | 0 | 144 |
| 4c 3c | 420 | 0 | 24 | 0 | 204 | 0 | 192 |
| 3c 3c | 280 | 8 | 0 | 168 | 0 | 104 | 0 |
| 3c 2c 2c | 210 | 0 | 0 | 24 | 0 | 186 | 0 |
| 4c | 210 | 0 | 12 | 0 | 150 | 0 | 48 |
| 2c 2c | 105 | 9 | 0 | 36 | 0 | 60 | 0 |
| 2c 2c 2c | 105 | 0 | 12 | 0 | 41 | 0 | 52 |
| 3c | 70 | 0 | 0 | 0 | 0 | 70 | 0 |
| 2c | 21 | 0 | 0 | 0 | 9 | 0 | 12 |
| solved | 1 | 1 | 0 | 0 | 0 | 0 | 0 |

## 12. What this does not cover

- **Edges.** This is corners only. A floor here is a floor for the cube, but a turn that's closer for the corners can be terrible for the edges. rodneykinney on the CO maze: "it only applies to corners, and the edges are too important to ignore" ([20 Sep 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1154070313554956380)).
- **Centres.** DBL is held, so a state is a corner state up to turning the cube (section 3).
- **A full recognition system.** Types + D-colour corners + parity settle the distance, but that's 918,540 different things to see. I haven't found a way to read the distance off them by hand beyond 4 moves, and section 7 says how much room is left with less.
- **rodneykinney's CO maze, node by node.** Section 9.4 has the one-axis numbers for this move set, not a check of the gist's 13 nodes.
- **Whether the six paths are all of them** (section 11).

## Appendix: how it was computed, and what is proved in Lean

**The model.** A corner place is a point (±1, ±1, ±1), a face turn is a rotation of space, and the twist a turn applies is worked out from where the U/D sticker goes. Nothing is typed in as a table. A second model that tracks all 24 stickers one by one agrees with it on random sequences, and the type of a corner is checked against the stickers themselves.

**The tables.** A breadth-first search outward from each target gives the distance of every state to it: HTR, all good, even all good, all good with a 4a picture, corners oriented on an axis, corners in their tetrads. Quarter turns use the same search with half turns at cost 0. NISS distances take the smaller of normal and inverse and then relax over moves on the normal side.

**Lean.** The certificate is in `lean/Corners3D` of the repository (Lean 4, no Mathlib; it builds in about two minutes). It redoes everything from a 54-sticker model of the cube, so no table of this page is taken on trust.

Proved by induction, for every sequence of turns:

- `floor_of_check`: the general floor argument of 6.1. `types_floor`, `parity_floor`, `placement_floor` and `weight_floor` are the floors of sections 6.2, 6.5 and 4.3, and `quarter_floors` the ones in quarter turns.
- `same_kinds_stay_same` and `types_solution_hits_every_good_state`: the 1 in 6 of section 5.2. If a sequence makes a state all good, every all-good state is hit by exactly one of the states with the same types.
- `htr_iff`: the test for HTR of section 5.3.
- `dHTR_exact`: the distance table is exact, so are the two floor tables.

Checked over all 3,674,160 states by running a compiled check (`native_decide`):

- `tetrad_theorem` and `quarter_rule`: the six types and the rule of section 4, with the table of 4.2 as `rule_table`.
- `dHTR_hist`, `qHTR_hist`: the two tables of section 3. `fake_htr_far`: every fake HTR is 9 turns away.
- `three_reads_fix_distance`, `types_and_two_colours_fix_state`, `types_class_size`: section 5.4.
- `floor_gaps`, `quarter_floor_gaps`, `qt_surcharge`: how far the floors are below the truth, and what the twist costs.
- `dr_qt_same`, `dr_turns_saved`, `placement_qt_same_on_three_axes`: section 9.1 and 9.2, and beef beans' count on three axes.
- `Pages.lean`: all 305 scrambles these pages print, each with its types line, moves, quarter turns, both floors and the printed solution.

Not in Lean: the distances with NISS, the *best rule* tables of section 7, the count table's rows (they're minima over the certified distance table, taken in Python), and the search over all eight corners behind the errata. Those are the Python and Rust searches of the repository, and every scramble they print is replayed on a second sticker model.

**Sizes.** 3,674,160 states, 25,515 type patterns, 1,284 up to half turns, 153,090 cases of 24.
