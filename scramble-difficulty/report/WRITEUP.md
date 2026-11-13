# Easy or hard? Reading a scramble before you look for DRs

Some scrambles hand you a dozen short DRs with nice subsets; on others every EO goes nowhere. Can you tell which kind you have before you search for DRs, from the cube and from the scramble's text? And can you tell which axis will have the short DRs? I measured it on 23,879 scrambles: 10,000 uniformly random states, all 8,108 official FMC scrambles with the `R' U' F` padding in the WCA results export, and 5,771 scrambles made with TNoodle's own solver. For each one I listed every DR that goes through an EO (EO of at most 5, NISS allowed, then DR, at most 10 moves in all) and scored each DR by its exact optimal finish. Then I tested every feature the server has proposed, and a few more, against that list. Everything is a sample, with 95% intervals; the facts about the scramble text are checked on every official scramble.

**Draft: speculative, not reviewed.**

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs, sheets and tools are listed with links at the end.

**This builds on** what the server already had:

- **torchlight's guess about the axis**: the axis with the fewest short EOs may be the one with the most short DRs, because a DR needs EO on two axes ([29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256590206958698517)). Section 6 measures it.
- **Levi Gibson's two ideas**: the corner QT count of a scramble, which is the same on all three axes ([21 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143384156198416426)), and seven counts that describe a DR axis without choosing an EO first ([26 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1344348188592574558)). **Zagros's** request for the bad edges of two axes and the ones they share ([17 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1341253090736738325)), and **rodneykinney's** wish to read the DR axis off the pairs already formed ([8 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1470074898830590205)).
- **The EO-count heuristics** of Tom Nelson, Yura Riabov, Lewis Isom and jisu101 (section 8), and **JTuu's** question whether the DRs come more than their share from the axes with few EOs ([29 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1521204868805693460)).
- **How an FMC scramble is made**, as Louis ([15 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1229460118119383131)), Sebastiano Tronto ([15 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1229472462698446920)), torchlight ([29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256591781672390656)), DougCube ([24 Oct 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1563590045577908265)) and wen ([14 Oct 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1559809438263541771)) described it, and **TNoodle's source** ([tnoodle-lib](https://github.com/thewca/tnoodle-lib), with Shuang Chen's min2phase solver inside).
- **DougCube's sheet** [*All WCA Scrambles by DougCube (Main)*](https://docs.google.com/spreadsheets/d/183AYpjKz4fZZAy5Hx5lxEthD2f356ReZG-uHPm_HWcY), tab FMC: an optimal solution for 8,532 official scrambles.
- **My own earlier studies**: the exact optimal finish of every DR state ([*Judging a DR*](../judging-a-dr/)), how many EOs and DRs a scramble has ([*EO to DR, and scramble to DR*](../eo-to-dr/), sections 3.3 and 4), DRM, ARM, pairs and corner cases after an EO ([*When to switch an EO*](../eo-switch/)), and the list of every EO-first DR on 10,000 uniform scrambles (`gaps/research` in the [repository](https://github.com/ArhanChaudhary/fmc-analysis)).

**What this adds**:

- **A measured scale for easy and hard**: four targets (how many DRs, the best DR + finish, how many good DRs, how many in a good subset) that agree with each other, and how much of each can be seen in advance at all.
- **What the cube says before any search**: the three bad-edge counts sort scrambles into four classes, from 22% easy to 51% hard. Corner orientation, slice edges, tetrads, ARM corners and the corner QT count add nothing to that.
- **What the EO list says**: the shortest EO and the number of 4-move EOs, as a lookup table, get four fifths of what any model can predict.
- **Which axis, and why**: a DR on one axis is paid for by the EOs of the other two. A table of DRs by the bad edges of those two axes, and two rules that follow from it: one for the bare cube, one for after the EOs are written.
- **Where the DRs come from**: when the EOs pile up on one axis, the other axes give more than their share of DRs. JTuu asked whether this is a thing. It is.
- **The scramble text**: its exact structure from TNoodle's source, the DR it contains, and the measurement that it predicts nothing about the scramble on current official scrambles.
- **Eighteen statements from the server, checked**, with one correction.

**Terms**, as used here.

- *DR*: a DR state reached through an EO of at most 5 moves on any axis (normal, inverse or with NISS inside the EO), then DR on either side without breaking that EO, at most 10 moves in all. Each DR state counts once per scramble. This is a computer's list, not what a solver finds (section 9).
- *Finish*: the optimal finish of a DR in U, D, R2, L2, F2, B2.
- *EO on F/B*: the edges are judged by F and B quarter turns. A DR on U/D can come from an EO on F/B or on R/L, and needs both in the end. Those are its *two EO axes*; U/D is its *own* axis.
- *Bad edges 4/6/8*: the bad-edge counts of the three axes, smallest first. They are the same on the inverse.
- *Number of EOs*: move sequences that reach EO at their last move, counted on all three axes, on the normal and the inverse scramble, without NISS. No face turns twice in a row, opposite faces come in one order, and an EO that ends F or F' counts once. Counted this way a random scramble has 15 EOs of at most 4 moves and 202 of at most 5. Counting both endings, as [*EO to DR*](../eo-to-dr/) does, doubles these.
- *Easy*: the best DR + finish is at most 19 (the best tenth of scrambles). *Hard*: it is at least 23, or there is no DR of at most 10 (about one in seven).
- *Flipped layer edge*, for a DR axis: an edge with a colour of that axis (white or yellow for U/D) that sits in one of that axis's two layers with that sticker on the side.
- *Corner QT*: forget the corner twists and count the quarter turns the corner permutation needs to reach HTR, with half turns free. This is the last digit of a DR's corner case (the 2 of 4b2; appendix A has the one exception).

**How to read it.**

- **Start with [section 1](#1-the-short-version)**, the short version. The rules you can use in an attempt are the two tables of [section 5.3](#53-rules-you-can-use) and the axis rules of [section 6.3](#63-the-axis-rules).
- Anything marked **computer only** is an answer key: it can't be done at the table.
- Every accuracy is measured on scrambles the rule or model was not fitted on. An interval in square brackets is a 95% bootstrap interval.
- Each exact statement is marked *exhaustive* (every case checked) or *proved in Lean*; everything else is *sampled*, with its sample size.

---

| Section | What is in it |
|---|---|
| [1. The short version](#1-the-short-version) | What is new, the rules, how well they work, what they confirm or correct. |
| [2. What was asked](#2-what-was-asked) | The questions and guesses, quoted, with the answer to each. |
| [3. Definitions and data](#3-definitions-and-data) | The four targets, the four sets of scrambles, the features. |
| [4. How much is predictable](#4-how-much-is-predictable) | How the targets agree, and the ceiling. |
| [5. Scramble difficulty](#5-scramble-difficulty) | Every feature, what each adds, the two lookup tables, corners. |
| [6. Which axis](#6-which-axis) | What a DR on an axis needs, per-axis features, the rules, where the DRs come from. |
| [7. The scramble text](#7-the-scramble-text) | How TNoodle builds it, the DR inside it, what it predicts. |
| [8. The claims, checked](#8-the-claims-checked) | Each statement with its verdict and numbers. |
| [9. What this does not cover](#9-what-this-does-not-cover) | Limits. |
| [Appendix A: how it was computed, and what checks it](#appendix-a-how-it-was-computed-and-what-checks-it) | Lists, model, statistics, Lean. |
| [Appendix B: worked scrambles](#appendix-b-worked-scrambles) | The example scrambles, each with its numbers and DRs. |
| [Docs referred to](#docs-referred-to) | Links. |

---

## 1. The short version

**What is new**

- **Edges decide how many DRs a scramble has. Corners don't.** Over 23,879 scrambles the fewest bad edges on any axis has a rank correlation of −0.65 with the number of DRs. The number of misoriented corners has 0.00 to 0.01 on every axis, and adding corners to a model changes its held-out R² by less than 0.001. Slice edges already in their slice, the tetrad split, ARM corners, twist direction and corner parity are all within 0.05 of zero.
- **Levi Gibson's corner QT count is a property of the scramble, and it barely matters.** It is the same on all three axes and on the inverse for every one of the 40,320 corner permutations (exhaustive). It does shift the corner cases of the DRs, in the direction Levi Gibson said, but only a little: DRs with at most 2 QT are 23% of the DRs on a QT 0 scramble and 16% on a QT 5 scramble. It says nothing about how many DRs there are (ρ = 0.00).
- **A class you can read off the bare cube.** Sort the scramble by its three bad-edge counts (table below). The four classes run from 22% easy to 51% hard and recover 62% of what a computer model on all 199 features can predict about the number of DRs.
- **After the EOs are written, two numbers do most of the work**: the shortest EO and the number of EOs of at most 4 moves. As a two-number score they reach a held-out R² of 0.58 for the number of DRs and 0.30 for the best DR + finish, and tell easy from the rest with AUC 0.77. Gradient boosting on everything (**computer only**) reaches 0.72, 0.36 and 0.78. [Section 5.3](#53-rules-you-can-use) has the score as a table: with no EO under 5 moves, 46% of scrambles are hard and the median is 6 DRs; with a 2-move EO and 50 or more 4-movers, half are easy and the median is 337.
- **The single best result is mostly luck.** Even the computer-only model explains 36% of the best DR + finish, against 72% of the number of DRs. You can see whether a scramble is rich. Whether its best line is short depends on which DRs happen to have short finishes.
- **A DR on one axis is paid for by the EOs of the other two.** The number of DRs on U/D that go through an F/B EO depends on the bad edges on F/B and on R/L, and not on U/D: 46 on average when both have 2 bad, 3 when both have 6, 0.2 when both have 10 ([section 6.1](#61-what-a-dr-on-an-axis-needs)). So the best DR axis is the one whose own EO looks worst. torchlight guessed this in 2024 and expected it to be weak. Picking the axis whose two EO axes have the most EOs of at most 5 finds the axis with the most DRs 51.3% of the time, against 36.3% by chance, and a computer-only model on every per-axis feature reaches 54.3%.
- **From the bare cube, flipped layer edges pick the axis best.** Counting, for each axis, the edges of that axis's colours that sit in its layers with that sticker on the side finds the best axis 45.5% of the time. The bad-edge counts get 43.8%, DRM-style pairs 40.0%, misoriented corners 35.8%. An axis with none of these edges has a median of 34 DRs, one with four has 3. The count comes out of Levi Gibson's seven features.
- **When the EOs pile up on one axis, the other axes give more than their share of DRs.** On the 2,972 scrambles with at least 80% of their EOs on one axis, that axis holds 86.5% of the EOs and 74.4% of the DRs.
- **The scramble text is a NISS DR of 12 to 19 moves, and it tells you nothing.** From TNoodle's source: the scramble is `R' U' F`, then the inverse of a min2phase solution of a random state, then `R' U' F`. The middle is some moves, then a run of 4 to 12 DR moves, then some more moves. Undoing the last part on normal and the first part on inverse puts the middle in DR, and with the padding undone as well it is a NISS DR of the scramble itself, 17 moves at the median. On official scrambles since August 2020 no feature of the text predicts anything: every rank correlation with difficulty is within ±0.03, and the text's DR axis is the best axis 36.5% of the time against 36.3% by chance.
- **TNoodle rarely keeps the first solution it finds.** On the 5,592 official scrambles since August 2020, the middle is the first solution of min2phase's search in 14.8%. In the other 85.2% it is a shorter one found in the 200 ms the search keeps running.

The bad-edge classes, over all 23,879 scrambles. A row is a class of scrambles; read across for how often it is easy or hard:

| Bad edges on the three axes | Scrambles, % | Easy, % | Hard, % | DRs of ≤ 10, median |
|---|---|---|---|---|
| two axes with 4 or fewer | 19.9 | 22 | 1 | 95 |
| one axis with 4 or fewer | 39.0 | 10 | 5 | 39 |
| none with 4 or fewer, worst at most 8 | 35.1 | 3 | 25 | 12 |
| none with 4 or fewer, and a 10 or 12 | 6.1 | 2 | 51 | 5 |

**What it confirms or corrects**

- The EO-count signals hold: few 4-move EOs (Tom Nelson), few 5-movers with barely any 4-movers (Yura Riabov), 10/8/8 with no EO under 5 (Lewis Isom), an axis with 2 or 4 bad (Tom Nelson), and jisu101's EO distributions without 6, 10 or 12. The cut points depend on how you count EOs; the direction doesn't.
- JTuu's "eo counts by themselves are not very predictive imo" ([2 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1302417164011311134)) depends on what you predict. For the number of DRs, EO counts are the best predictor there is (ρ = 0.78). For the best single result nothing is good (ρ = −0.54 at best).
- Scramble length says nothing useful. rogo found their own short scrambles bad; over all scrambles the short ones are, if anything, slightly better.
- The text's DR axis is no better than the others on current scrambles. On 2016 to 2020 scrambles it held 8% more DRs than the other axes.
- Zagros's shared bad edges add nothing once you know the two counts. Zagros was right that corner orientation gets swallowed by the edges.
- One correction, to a detail of Louis's description of the scrambler: the solution kept is the shortest found in 200 ms, not the first.
- Official scrambles are as easy as uniform random states: a median of 28 DRs in every set, and 9% to 10% easy.

**The rules, in one paragraph.** Count the bad edges on the three axes: two axes with 4 or fewer is a rich scramble, none with 4 or fewer plus a 10 is a poor one. When your EOs are written, note the shortest and the number of 4-movers and read the second table of section 5.3. For the axis, before any search prefer the axis with the fewest flipped layer edges; after it, prefer the axis whose other two axes have the most short EOs, which is the axis whose own EOs are the worst. Don't weigh corner orientation, and don't read anything into the scramble's text.

---

## 2. What was asked

The questions and guesses, in the askers' own words, and where each is answered. Statements that the numbers can settle are in [section 8](#8-the-claims-checked).

**Is this scramble easy or hard? (sections 4 and 5)**

- *For human solvers, some scrambles are easier than others. Easy/hard is not a well-defined distinction, but easy scrambles tend to have several "findable" DRs with good HTR subsets. The question: is there any way to estimate how easy or hard a scramble will be without having to actually search for DRs? Keep in mind that you may use any features that are observable from the scrambled cube state, as well as any features derived from the text of the written scramble, which can be interpreted as a DR solution inside the padding `R' U' F` on both sides.* *Answer*: partly. How many DRs there are is about 70% predictable, mostly from bad edges and the first EOs (section 5). The best result is about a third predictable (section 4). The text adds nothing (section 7).
- JTuu ([2 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1302417164011311134)), in reply to a question about how much easier non-random scrambles are: "there are ways to tell in which "direction" a scrambler is biased, but answering this comes down to the question of what makes a scramble easy in general, and I don't think we really have a great understanding of that. the only real heuristics we have are eo-related, and eo counts by themselves are not very predictive imo". *Answer*: the heuristics that work are indeed all EO-related. No other kind of feature adds more than 0.03 of R² (section 5.2). How predictive they are is in sections 4 and 8.
- Noah Swor ([2 May 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1103117997045989487)): "I wonder if theres a correlation between EO count and optimal length". wen ([4 May 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1103710842635165816)): "probably yes but very loosely". Zagros ([13 May 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1371907913244999772)): "Is there a correlation between eo count and opt solution length?" *Answer*: yes, loosely, as wen guessed. On 7,689 official scrambles the number of 4-move EOs has ρ = −0.14 [−0.16, −0.12] with the optimal length. Corner-edge pairs do better (−0.24): the optimal length follows blocks more than EOs (section 4).
- wen ([3 Nov 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1434944732932603977)): "We could probably evaluate how doomed a scramble is by seeing how many edges are bad on 0/1/2/3 axes but its not going to be a very good correlation". *Answer*: the number of edges bad on all three axes has ρ = −0.43 with the number of DRs, the number good on all three +0.35. Both are weaker than the plain bad-edge count of the best axis (−0.65), and together they add 0.018 of R² to the three counts (section 5.2).

**Which axis? (section 6)**

- *A related question to this: can you find any features that indicate which axes are likely to have a short DR? Consider features the FMC solvers already know about (EO, CO, HTR subset), but please be creative and investigate other possible features that we may not have thought of.* *Answer*: section 6.3.
- maxooma ([29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256589675200778352)): "Tbh this discussion has sparked an idea for me. I've always noticed how one axis is always "better" than the rest, for example my best drs from my recent solve were all fb axis. I wonder if there is some way of calculating an estimate as to which axis will be the "better" one in a solve (I will say, most of the time I use a dr on the same axis as the "dr" portion in the scramble)". *Answer*: the axes are lopsided, as maxooma noticed: on scrambles with at least 10 DRs the best axis holds 60% of them on average, and 27% of scrambles with a DR have an axis with none. The estimate is the rule of section 6.3. The axis of the scramble's DR portion is not it (section 7.3).
- torchlight, replying ([29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256590206958698517), [29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256590259370852384), [29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256590388802883696), [29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256590876994441296)): "axis with the lowest (# of short EO solutions) might weakly correlate with axis with the highest (# of short DR solutions)", "but I doubt there's anything usable from this", "("short" meaning like <=5 moves for EO and <=10 moves for DR, I guess)", "since DR needs EO to be solved on two axes at the same time". *Answer*: it does, for the reason torchlight gives, and with exactly these lengths it is the strongest per-axis signal measured here. Within a scramble the correlation is −0.47, and the axis with the fewest EOs of at most 4 is the axis with the most DRs 49.3% of the time against 36.3% by chance (section 6.2).
- JTuu ([28 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1520696576492699718)), of the scramble in [appendix B](#appendix-b-worked-scrambles): "interesting eo situation on this scram, only 10 of the 80 sub-6 eos are on an axis that is not FB". wen ([28 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1520701511137759392)): "Last week's league had an even more extreme case lol". JTuu, of that one ([29 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1521204868805693460)): "on mine too, it felt like there were disproportionately many drs from the other axes. I wonder if this is a thing". *Answer*: it is (section 6.4). With at least 80% of the EOs on one axis, the other two axes hold 13.5% of the EOs and 25.6% of the DRs. It is an average, not a law: on the scramble JTuu posted, the only two DRs of at most 10 both go through an F/B EO.
- kalindumaxxer ([29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256627760068169797), [29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256627802799865896), [29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256627821535825921)), recalling a tip: "i think on #fmc-tricks there was one saying how the axes that dont have a low amount of bad edges are better to check", "bc edges are more likely to be in rzp after", "maybe jay said that". Java ([29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256693525438005299)): "yes i remember that too". *Answer*, for the tip as recalled (the original is not among the messages read for this study): per EO there is something in it, but not in total. An EO on an axis with 6 or 8 bad edges leads to 0.25 to 0.28 DRs on average, one on an axis with 2 bad to 0.21, one on an axis with 4 bad to 0.34. But the axes with 2 or 4 bad have three to nine times as many EOs, and four to seven times as many DRs go through them (section 6.4).
- Zagros ([17 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1341253090736738325), [17 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1341253376532414505)): "Is anyone able to generate stats for average scrambled->dr for the these parameters: / -bad edges on one axis / -bad edges on the other axis / -number of bad edges shared between them", "I feel like this is probably a really good predictor of how good DRs there are on an axis, definitely better than just the edge counts without knowing how many of the bad edges are overlapping". *Answer*, for the number of EO-first DRs on the third axis (the optimal DR length is not measured here): the two counts are a good predictor. The shared count adds nothing to them. With 6 and 6 bad the median is 3 DRs whether 2, 3, 4, 5 or 6 edges are shared, and adding it to the two counts moves the share of best axes found from 43.1% to 42.7% (section 6.2).
- Levi Gibson, replying to Zagros ([17 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1341257879889641515)): "Corner orientation too is probably useful". Zagros ([17 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1341258311382597663)): "I think that any co count can typically be solved in fewer qts than your edges can, so it might kinda get swallowed up by that / But I'm still interested too". *Answer*: swallowed entirely, as Zagros thought. The axis with the fewest misoriented corners is the best axis 35.8% of the time, against 36.3% by chance.
- Levi Gibson ([26 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1344348188592574558)), of seven counts for one DR axis, a stat Levi Gibson credits FakeMMAP with suggesting (corner orientation; the U/D-layer edges misoriented on F/B, on R/L and on both; the E-slice edges misoriented on F/B, on R/L and on both): "This stat would also explain why some scrambles don’t have any short DRs even though there are lots of EOs". Two days later, with the combinations ranked as triggers in the sheet [*Trigger averages*](https://docs.google.com/spreadsheets/d/1ye-vV4OeGBofmlZIJyIMy_dEoZk9Xz-v2ijtcTyO5AM) ([28 Feb 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1345126076497793024)): "Welp, it's completely useless lol. Almost all the EO cases are much better than the non-eo cases." *Answer*: as triggers, that stands. As a way to choose the axis the seven counts are the best thing you can read off the bare cube: 46.5% of best axes found, against 43.1% for the two bad-edge counts. Nearly all of it is one count, the layer edges misoriented on both axes (section 6.2).
- rodneykinney ([8 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1470074898830590205)): "One is that it ignores corners for so long. I should be able to inspect the cube and see which axes are most promising for DR based on the number of corner-edge pairs that are already formed. (I mean DRM-style pairs: a white corner sticker facing away from an F/R edge)" and "The second is that you do EO on FB and look for UD-axis DRs, then do EO on RL and look again for UD-axis DRs. I should be able to figure out the best way to reach UD-axis DR without first committing to a particular EO axis." *Answer* to the first: a little. The axis with the most such pairs, normal and inverse together, is the best axis 40.0% of the time against 36.3% by chance; the edges alone do better (section 6.2). To the second: the table of section 6.1 says what a U/D DR needs from both EO axes at once. How to find it without committing to one is not covered; rodneykinney's own answer in that message is the dr-fe techniques.

**The scramble text (section 7)**

- Jeremy Mrzyglocki ([15 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1229432656597356666)): "How much information can we derive from the lenght of the scramble? How exactly does the padding work? If the "inner scramble" is random-state, it feels like the padding would make the outcome non-random-state. Are 16opt FMC-scrambles generally shorter or does tNoodle somehow extend then on purpose?" *Answer*: none that helps. The length has ρ = 0.007 with the optimal length (7,689 official scrambles) and −0.03 with the number of DRs. The padding is section 7.1, and Louis's and Sebastiano Tronto's answers at the time are in section 8.

What is left open is in section 9.

---

## 3. Definitions and data

### 3.1 The four targets

Every target comes from a scramble's DR list: all DR states reached by an EO of at most 5 moves (NISS allowed inside the EO), then DR on normal or inverse without breaking that EO, at most 10 moves in all. The list is cubelib's, with the steps of the examples page of [*Judging a DR*](../judging-a-dr/examples.html) (`EO[niss=always;max=5] > DR[niss=before;max=10]`), and a DR state counts once per scramble. Each row of the table is one target, with its mean and median over the 23,879 scrambles:

| Target | What it is | Unit | Mean | Median |
|---|---|---|---|---|
| DRs of ≤ 10 | how many DRs there are to find | DRs | 70.7 | 28 |
| Best DR + finish | the shortest DR + optimal finish among them | moves | 21.2 | 21 |
| Good DRs | DRs with DR + optimal finish of 22 or less | DRs | 12.9 | 4 |
| DRs in a good subset | DRs in corner case 0c0, 2c3, 4a1 or 4b2 with at most 4 bad edges | DRs | 18.7 | 7 |

*Easy* is a best DR + finish of at most 19 (9.7% of scrambles). *Hard* is at least 23, or no DR of at most 10 at all (13.9%; 1.4% have none). The four good corner cases are the ones whose 2e and 4e subsets have a mean optimal finish under 13 moves (11.7 to 12.9). The finish is the optimal one, so the totals are lower than anything written in an attempt, 14 to 26 moves, and the cut for a good DR is 22. The counts are used on a log scale. A fifth candidate, the number of DRs within one move of the best, is left out: it goes up on hard scrambles, where many DRs tie at a poor best.

### 3.2 The scrambles

Four sets, one row each:

| Set | Scrambles, count | What it is |
|---|---|---|
| Uniform | 10,000 | uniformly random states, no padding (the scrambles of `gaps/research`) |
| Official 2016-04 to 2020-07 | 2,516 | every padded 333fm scramble in the WCA results export of 13 Nov 2026, before the scrambler's 2020 change (section 7.2) |
| Official 2020-08 to 2026-11 | 5,592 | the same, after it |
| Generated | 5,771 | made here with tnoodle-lib's min2phase and the call TNoodle uses (section 7.1) |

Every set is made of uniformly random states, so they should have the same DR landscape. They do. One row per set:

| Set | DRs of ≤ 10, median | DRs of ≤ 10, mean | Best DR + finish, mean moves | Easy, % | No DR of ≤ 10, % |
|---|---|---|---|---|---|
| Uniform | 28 | 70.5 | 21.18 | 10.0 | 1.5 |
| Official 2016 to 2020 | 28 | 74.7 | 21.22 | 8.9 | 1.2 |
| Official 2020 to 2026 | 28 | 70.5 | 21.20 | 9.7 | 1.5 |
| Generated | 28 | 69.4 | 21.19 | 9.4 | 1.3 |

Features of the cube are tested on all 23,879 scrambles. Features of the text are tested on the 11,363 current scrambles (official since August 2020 and generated) and separately on the 2,516 older ones. Models are fitted on a random two thirds of the scrambles and scored on the other third.

### 3.3 The features

All of these are read on the cube, or come out of an EO search, on normal and on inverse.

- **Bare cube**: bad edges per axis; misoriented corners per axis and their twist direction; slice edges already in their slice; bad edges sitting in each slice; how the misoriented corners split between the two tetrads; misoriented corners whose sticker faces a given side axis (the corner half of ARM, read on the scramble); solved corner-edge pairs; pieces solved in place; corner parity; edges bad on 0, 1, 2 or 3 axes; whether the three counts avoid 6, 10 and 12; the fewest bad edges or corners one move away. From the server: the corner QT count, the shared bad edges of two axes, Levi Gibson's seven counts, DRM-style pairs per axis.
- **EO search**: the shortest EO per axis and side; the number of EOs of at most 4 and at most 5 per axis and side; and for every EO of at most 5 the DR case it leaves on each of its two DR axes, summed up as the best case and as the number of EOs that leave at most 4 bad corners and 4 bad edges. That last count is heavy by hand.
- **Scramble text** (section 7): the length of the middle, the run of DR moves and its axis, the length of the text's DR, the blocks before and after the run, and the quarter turns per axis.

---

## 4. How much is predictable

The four targets agree. Rank correlations between them over all 23,879 scrambles; a row and a column are two targets:

| | DRs of ≤ 10 | Best DR + finish | Good DRs | DRs in a good subset |
|---|---|---|---|---|
| DRs of ≤ 10 | 1 | −0.71 | 0.91 | 0.88 |
| Best DR + finish | −0.71 | 1 | −0.80 | −0.72 |
| Good DRs | 0.91 | −0.80 | 1 | 0.89 |
| DRs in a good subset | 0.88 | −0.72 | 0.89 | 1 |

A scramble with many DRs has many good ones and many in good subsets. The best single result follows the counts more loosely.

The ceiling is gradient boosting on all 199 features (**computer only**). One row per target, with the R² on the 7,881 held-out scrambles:

| Target | Ceiling R² | 95% low | 95% high |
|---|---|---|---|
| DRs of ≤ 10 | 0.715 | 0.701 | 0.728 |
| Best DR + finish | 0.364 | 0.347 | 0.380 |
| Good DRs | 0.616 | 0.602 | 0.632 |
| DRs in a good subset | 0.599 | 0.583 | 0.614 |

Nothing you can see before a DR search explains more than about a third of the best DR + finish. The rest is which DRs happen to have short finishes. The number of DRs is mostly visible in advance. A plain linear model on the summary features of section 5 gets nearly the same (0.68 and 0.34), so there is no hidden interaction that only a computer could use.

The optimal length of the scramble is a different thing again. On the 7,689 official scrambles with an optimal solution in DougCube's sheet it has ρ = −0.20 with the number of DRs and 0.19 with the best DR + finish. Solved corner-edge pairs predict it better than any EO feature (−0.24 against −0.14 for the number of 4-move EOs).

---

## 5. Scramble difficulty

### 5.1 Every feature on its own

Each row is one feature: its rank correlation with three of the targets, and how well it separates easy scrambles from the rest (AUC; 0.5 is useless). All 23,879 scrambles; every 95% interval is within ±0.015 of the value shown.

| Feature | Needs | ρ with DRs of ≤ 10 | ρ with best DR + finish | ρ with good DRs | AUC, easy vs rest |
|---|---|---|---|---|---|
| EOs of ≤ 5, all axes | EO search | 0.794 | −0.551 | 0.711 | 0.755 |
| EOs of ≤ 4, all axes | EO search | 0.778 | −0.537 | 0.696 | 0.752 |
| shortest EO, summed over the 3 axes | EO search | −0.752 | 0.523 | −0.675 | 0.746 |
| EOs of ≤ 4 on the axis with the most | EO search | 0.742 | −0.511 | 0.662 | 0.733 |
| shortest EO, any axis and side | EO search | −0.712 | 0.491 | −0.637 | 0.717 |
| EOs of ≤ 4, normal only | EO search | 0.703 | −0.483 | 0.629 | 0.727 |
| EOs of ≤ 5 that leave ≤ 4 bad corners and ≤ 4 bad edges | EO search | 0.559 | −0.384 | 0.517 | 0.720 |
| bad edges, best axis | cube | −0.649 | 0.447 | −0.579 | 0.677 |
| bad edges, second axis | cube | −0.496 | 0.350 | −0.453 | 0.658 |
| bad edges, worst axis | cube | −0.387 | 0.275 | −0.350 | 0.618 |
| fewest bad corners + bad edges for one DR axis | cube | −0.486 | 0.333 | −0.431 | 0.654 |
| fewest bad edges one move away | cube | −0.463 | 0.327 | −0.419 | 0.649 |
| edges bad on all three axes | cube | −0.426 | 0.297 | −0.385 | 0.638 |
| best DR case after an EO of ≤ 5 | EO search | −0.402 | 0.289 | −0.377 | 0.664 |
| edges good on all three axes | cube | 0.353 | −0.245 | 0.319 | 0.611 |
| no axis with 6, 10 or 12 bad | cube | 0.231 | −0.166 | 0.211 | 0.563 |
| solved corner-edge pairs | cube | 0.131 | −0.140 | 0.152 | 0.584 |
| pieces solved in place | cube | 0.129 | −0.085 | 0.117 | 0.535 |
| fewest bad corners after an EO of ≤ 5 | EO search | −0.099 | 0.069 | −0.092 | 0.525 |
| slice edges in their slice, best axis | cube | −0.047 | 0.034 | −0.042 | 0.507 |
| misoriented corners, best axis | cube | 0.004 | −0.007 | 0.008 | 0.496 |
| misoriented corners, worst axis | cube | 0.005 | −0.005 | 0.009 | 0.498 |
| fewest bad corners one move away | cube | 0.003 | −0.008 | 0.006 | 0.499 |
| tetrad split of the misoriented corners | cube | 0.005 | −0.001 | 0.004 | 0.501 |
| misoriented corners facing one side axis | cube | 0.005 | −0.009 | 0.008 | 0.499 |
| clockwise against anticlockwise twists | cube | −0.007 | 0.007 | −0.010 | 0.500 |
| corners oriented on all three axes | cube | −0.006 | 0.008 | −0.011 | 0.497 |
| corner parity | cube | 0.001 | −0.010 | 0.004 | 0.503 |

Three things to take from it:

- Everything that works is about edges.
- Every corner feature is at zero, the two-step ones included. How few bad corners a good EO can leave says almost nothing (−0.10), while the corners and edges it leaves together do (−0.40): the edges carry it.
- The counts of short EOs are the best single predictors. Part of that is built in, since every DR in the list starts with an EO of at most 5. But the count beats the shortest EO, and both beat the bad-edge counts.

### 5.2 What each kind of feature adds

The baseline is a linear model on the three bad-edge counts and the three corner counts, each sorted. Each row adds one group of features to it; the gain is the change in R² on the 7,881 held-out scrambles.

| Added to bad edges + corners | R², DRs of ≤ 10 | Gain | Gain, 95% low | Gain, 95% high | R², best DR + finish | Gain (best) |
|---|---|---|---|---|---|---|
| nothing (the baseline) | 0.431 | — | — | — | 0.223 | — |
| corners taken out | 0.431 | −0.000 | — | — | 0.223 | −0.000 |
| shortest EO per axis | 0.634 | +0.203 | +0.190 | +0.216 | 0.317 | +0.094 |
| number of short EOs | 0.582 | +0.151 | +0.136 | +0.167 | 0.285 | +0.062 |
| DR case after the EOs | 0.532 | +0.100 | +0.089 | +0.109 | 0.258 | +0.035 |
| one-move lookahead | 0.458 | +0.027 | +0.021 | +0.033 | 0.237 | +0.014 |
| no 6, 10 or 12; bad edges in slices; parity | 0.453 | +0.022 | +0.018 | +0.026 | 0.232 | +0.009 |
| edges and corners bad on 0 to 3 axes | 0.450 | +0.018 | +0.014 | +0.023 | 0.230 | +0.007 |
| solved pairs, solved pieces | 0.449 | +0.018 | +0.013 | +0.022 | 0.240 | +0.017 |
| slice edges in their slice | 0.431 | +0.000 | −0.000 | +0.000 | 0.222 | −0.000 |
| tetrads, corners facing a side axis, twist direction | 0.431 | +0.000 | −0.000 | +0.000 | 0.223 | +0.000 |
| corner QT | 0.431 | +0.000 | −0.000 | +0.000 | 0.223 | −0.000 |
| everything, linear | 0.679 | +0.248 | — | — | 0.342 | +0.119 |
| **computer only**: gradient boosting on everything | 0.715 | +0.284 | — | — | 0.364 | +0.141 |

Beyond bad edges only the EO search adds much. The other bare-cube features add 0.03 at most, and the corner features nothing. Solved pairs add a little to the best DR + finish, which fits their link to the optimal length.

### 5.3 Rules you can use

The candidate scores, one per row: a linear fit on two or three counts (EO counts on a log scale) or a shallow decision tree, fitted on two thirds of the scrambles and scored on the other 7,881. The last column is the score's R² for the number of DRs as a share of the computer-only ceiling.

| Score | Needs | R², DRs of ≤ 10 | R², best DR + finish | AUC, easy vs rest | Share of the ceiling, % |
|---|---|---|---|---|---|
| bad edges of the best and second axis | cube | 0.411 | 0.210 | 0.715 | 57 |
| the four bad-edge classes (table 1) | cube | 0.446 | 0.239 | — | 62 |
| a deeper tree on the bare-cube counts, 8 classes | cube | 0.470 | 0.247 | — | 66 |
| EOs of ≤ 4 | EO search | 0.536 | 0.288 | 0.755 | 75 |
| shortest EO and EOs of ≤ 4 (table 2) | EO search | 0.581 | 0.301 | 0.766 | 81 |
| EOs of ≤ 5 and EOs that leave ≤ 4 bad corners and edges | EO search, heavy | 0.606 | 0.325 | 0.764 | 85 |
| **computer only**: gradient boosting on everything | — | 0.715 | 0.364 | 0.781 | 100 |

For the best DR + finish the shares are 66% for the bad-edge classes, 83% for the shortest EO with the 4-movers, and 89% for the heavy score. Adding misoriented corners to any of them changes nothing.

**Table 1: before any search.** Sort the three bad-edge counts. A decision tree given every bare-cube count picks exactly these cuts: is the best axis at 4 or below; if so, is the second; if not, is the worst at 8 or below. A row is a class of scrambles (all 23,879):

| Bad edges | Scrambles, % | Easy, % | Hard, % | DRs of ≤ 10, median | Best DR + finish, mean moves |
|---|---|---|---|---|---|
| two axes with 4 or fewer | 19.9 | 22 | 1 | 95 | 20.26 |
| one axis with 4 or fewer | 39.0 | 10 | 5 | 39 | 20.87 |
| none with 4 or fewer, worst at most 8 | 35.1 | 3 | 25 | 12 | 21.79 |
| none with 4 or fewer, and a 10 or 12 | 6.1 | 2 | 51 | 5 | 22.85 |

**Table 2: after writing your EOs.** The shortest EO on any axis and side, and the number of EOs of at most 4 moves (all axes, normal and inverse, no NISS, an F or F' ending counted once). A row is a group of scrambles. Groups with fewer than 50 scrambles are left out (a shortest EO of 3 or less with fewer than eight 4-movers: 35 scrambles).

| Shortest EO, moves | EOs of ≤ 4, count | Scrambles, count | Easy, % | Hard, % | DRs of ≤ 10, median | Best DR + finish, mean moves |
|---|---|---|---|---|---|---|
| 2 or less | 8 to 19 | 390 | 20 | 1 | 93 | 20.27 |
| 2 or less | 20 to 49 | 1,174 | 31 | 0 | 155 | 19.90 |
| 2 or less | 50 or more | 301 | 49 | 0 | 337 | 19.47 |
| 3 | 8 to 19 | 3,003 | 8 | 4 | 36 | 20.93 |
| 3 | 20 to 49 | 5,039 | 16 | 1 | 70 | 20.49 |
| 3 | 50 or more | 366 | 29 | 0 | 176 | 19.91 |
| 4 | 1 to 7 | 5,980 | 3 | 24 | 12 | 21.79 |
| 4 | 8 to 19 | 4,336 | 7 | 10 | 25 | 21.21 |
| 4 | 20 to 49 | 527 | 12 | 2 | 49 | 20.67 |
| 5 or more | 0 | 2,728 | 1 | 46 | 6 | 22.60 |

One scramble in nine has no EO under 5 moves, and nearly half of those are hard. With a 2-move EO and 50 or more 4-movers half are easy, and none of the 301 is hard. If you count both endings of an EO, halve your count before reading the table.

### 5.4 Corners, three ways

**Orientation.** The number of misoriented corners on an axis tells nothing about the scramble (table of 5.1) and nothing about the axis (section 6.2). The EO moves the corners around, so what the scramble's corners look like doesn't survive to the DR.

**Corner QT.** Levi Gibson's count is a real property of the scramble: for every one of the 40,320 corner permutations it is the same on the three axes and on the inverse (exhaustive). The values 0 to 5 cover 96, 1,152, 5,856, 11,328, 14,208 and 7,680 permutations. A row of the table is the scrambles with one value; the two middle columns pool all their DRs:

| Scramble's corner QT | Scrambles, count | DRs with at most 2 QT, % | DRs in a good subset, % | DRs of ≤ 10, median | Easy, % |
|---|---|---|---|---|---|
| 0 | 69 | 23.1 | 35.9 | 29 | 11.6 |
| 1 | 678 | 20.5 | 29.7 | 27 | 10.2 |
| 2 | 3,516 | 18.8 | 27.9 | 28 | 10.2 |
| 3 | 6,709 | 19.2 | 28.5 | 28 | 10.2 |
| 4 | 8,427 | 16.9 | 25.0 | 28 | 9.3 |
| 5 | 4,480 | 16.4 | 24.2 | 28 | 9.1 |

So a low-QT scramble does have slightly better corner cases among its DRs. The rank correlation between the scramble's QT and the mean QT of its DRs is +0.07 [+0.06, +0.08]. It has none with the number of DRs (+0.00) or the best DR + finish (+0.01), and it adds nothing to the bad-edge baseline for any target. The EO and the DR moves in between change the count by too much, which is the caveat in Levi Gibson's own post.

**Pairs.** Solved corner-edge pairs are a weak sign of an easy scramble (ρ = 0.13 with the number of DRs) and the best sign measured here of a short optimal (−0.24). DRM-style pairs per axis are in section 6.2.

---

## 6. Which axis

### 6.1 What a DR on an axis needs

A DR on U/D has EO solved on F/B and on R/L. The list gets there by an EO on one of them, then the DR, which fixes the other. So the number of DRs should depend on the bad edges of those two axes, and it does. A row is the EO axis the DR goes through, by its bad edges; a column is the third axis, by its bad edges; a cell is the mean number of DRs of at most 10 on the DR axis that go through an EO on that EO axis. All 23,879 scrambles, six (EO axis, DR axis) pairs each; cells with fewer than 30 pairs are left out, and the smallest cell shown has 49.

| Bad edges on the EO axis | Third axis 2 bad, mean DRs | Third axis 4 bad, mean DRs | Third axis 6 bad, mean DRs | Third axis 8 bad, mean DRs | Third axis 10 bad, mean DRs |
|---|---|---|---|---|---|
| 2 | 46.2 | 34.5 | 24.1 | 22.0 | 17.0 |
| 4 | 44.3 | 32.8 | 22.9 | 18.7 | 11.3 |
| 6 | 9.9 | 6.0 | 3.3 | 2.6 | 1.6 |
| 8 | 16.4 | 8.7 | 4.9 | 4.1 | 2.6 |
| 10 | 1.4 | 0.9 | 0.6 | 0.4 | 0.2 |

Read down a column for the EO: 2 or 4 bad is far ahead, 8 bad beats 6 bad by about half, and 10 bad gives next to nothing (those DRs go through NISS EOs). Read across a row for what the DR has left to do: from 2 to 6 bad edges on the third axis the count halves or worse, and from 6 to 8 it drops only a little, as it does for the EO. The DR axis's own bad edges are not in the table. Within a scramble they only matter as the complement: the three counts are what they are, so the axis whose own count is highest is the axis whose other two are lowest.

### 6.2 Per-axis features

For each scramble, does the axis a feature favours have the most DRs of at most 10? A hit is counted when it is among the tied best, so chance is 36.3% for the most DRs, 56.4% for the shortest DR and 45.7% for the best DR + finish. *Within r* is the correlation between the feature and the log of the DR count on that axis, both taken relative to the scramble's mean. All 23,879 scrambles; every 95% interval is within ±0.7 points.

| Feature of a DR axis | Needs | Within r | Most DRs found, % | Shortest DR found, % | Best DR + finish found, % |
|---|---|---|---|---|---|
| chance | — | — | 36.3 | 56.4 | 45.7 |
| most EOs of ≤ 5 on its two EO axes | EO search | +0.471 | 51.3 | 66.1 | 55.7 |
| most EOs of ≤ 4 on its two EO axes | EO search | +0.467 | 49.3 | 64.7 | 54.2 |
| fewest EOs of ≤ 4 on its own axis | EO search | −0.467 | 49.3 | 64.7 | 54.2 |
| longest shortest EO on its own axis | EO search | +0.485 | 49.2 | 64.9 | 54.2 |
| most EOs that leave it ≤ 4 bad corners and edges | EO search | +0.261 | 47.7 | 63.3 | 52.7 |
| most bad edges on its own axis | cube | +0.304 | 43.8 | 61.1 | 50.6 |
| shortest EO on its two EO axes | EO search | −0.485 | 42.7 | 61.4 | 51.0 |
| best DR case an EO leaves it | EO search | −0.164 | 42.0 | 60.5 | 49.4 |
| fewest bad edges on the better of its two EO axes | cube | −0.327 | 40.8 | 59.7 | 49.2 |
| most bad edges sitting in its own slice | cube | +0.077 | 39.3 | 57.8 | 47.5 |
| fewest bad corners an EO leaves it | EO search | −0.082 | 38.0 | 57.6 | 46.7 |
| misoriented corners | cube | +0.021 | 36.9 | 57.0 | 46.2 |
| misoriented corners facing the third axis | cube | +0.016 | 36.8 | 56.9 | 46.1 |
| slice edges in its slice | cube | −0.026 | 36.4 | 56.8 | 46.3 |
| tetrad split | cube | +0.007 | 36.5 | 56.6 | 45.6 |
| the text's DR axis (scrambles since 2020-08) | text | +0.011 | 36.5 | 57.0 | 46.1 |

The corner rows sit at chance. The misoriented-corner row favours the axis with more of them, which is the direction of its tiny correlation; favouring the axis with fewer finds the best axis 35.8% of the time.

The features proposed on the server, the same way. A row is one feature; the hit rate is for the axis with the most DRs, with its 95% interval (chance 36.3%):

| Feature of a DR axis | From | Within r | Most DRs found, % | 95% low | 95% high |
|---|---|---|---|---|---|
| fewest bad edges on its two EO axes, summed | — | −0.304 | 43.8 | 43.3 | 44.3 |
| fewest edges bad on either EO axis (sum less shared) | Zagros | −0.214 | 42.9 | 42.4 | 43.3 |
| fewest shared bad edges | Zagros | −0.248 | 42.2 | 41.7 | 42.7 |
| fewest flipped layer edges | Levi Gibson's split | — | 45.5 | 45.0 | 46.0 |
| fewest edges of its colours flipped in a layer or sitting in the slice | Levi Gibson's split | — | 46.4 | 45.9 | 47.0 |
| most DRM-style pairs, normal | rodneykinney | +0.076 | 39.3 | 38.8 | 39.8 |
| most DRM-style pairs, normal + inverse | rodneykinney | +0.093 | 40.0 | 39.3 | 40.5 |

Levi Gibson's seven counts split the bad edges by where they are. For a U/D DR a white or yellow edge is in one of three states: in a U/D layer with white or yellow facing up or down (good on F/B and on R/L), in a U/D layer with it on the side (bad on both: a flipped layer edge), or in the E slice (bad on exactly one). That was checked on 72,000 pieces. A fit of the DR count on the counts gives the flipped layer edge four times the weight of any other kind (−0.51 per edge on the log scale, against −0.12, −0.12 and −0.08), and misoriented corners a weight of +0.02. A row is the DR axes with a given number of flipped layer edges, over all scrambles and axes:

| Flipped layer edges on the axis | Axes, count | DRs of ≤ 10 on it, mean | DRs of ≤ 10 on it, median | No DR of ≤ 10 on it, % |
|---|---|---|---|---|
| 0 | 2,047 | 167.0 | 34 | 0.2 |
| 1 | 10,076 | 46.0 | 22 | 1.2 |
| 2 | 20,292 | 26.5 | 12 | 5.3 |
| 3 | 21,906 | 11.1 | 5 | 12.9 |
| 4 | 12,528 | 6.4 | 3 | 23.8 |
| 5 | 4,116 | 4.3 | 2 | 34.0 |
| 6 | 625 | 3.7 | 1 | 42.1 |

Zagros's shared edges, with the two counts held fixed. A row is the pairs of EO axes with 6 and 6 bad edges, by how many of those edges are bad on both:

| Edges bad on both, of 6 and 6 | Axis pairs, count | DRs of ≤ 10 on the third axis, median | No DR on it, % |
|---|---|---|---|
| 2 | 2,076 | 3 | 17 |
| 3 | 6,341 | 3 | 18 |
| 4 | 5,060 | 3 | 18 |
| 5 | 1,182 | 3 | 20 |
| 6 | 72 | 3 | 24 |

It is much the same with 4 and 6 bad (median 16, 15, 15 and 13 DRs for 1 to 4 shared) and with 4 and 4 (32, 38, 34, 30 and 27 for 0 to 4 shared).

The same features as fitted models, scored on a held-out third of the scrambles. A row is a model:

| Model | Needs | Most DRs found, % | 95% low | 95% high |
|---|---|---|---|---|
| the two bad-edge counts, summed | cube | 43.1 | 42.3 | 44.0 |
| the two counts and the shared edges | cube | 42.7 | 41.7 | 43.8 |
| corners, bad edges, slice edges | cube | 43.9 | 42.8 | 44.9 |
| Levi Gibson's seven counts | cube | 46.5 | 45.4 | 47.4 |
| EOs of ≤ 5 on the two EO axes | EO search | 51.6 | 50.4 | 52.7 |
| counts and EO search | EO search | 52.1 | 51.1 | 53.1 |
| every per-axis feature, linear | EO search | 52.8 | 51.8 | 54.0 |
| **computer only**: gradient boosting on every per-axis feature | — | 54.3 | 53.2 | 55.4 |

One count, the EOs of at most 5 on the two EO axes, is within 3 points of the computer-only model. Adding the flipped layer edges to it gains nothing (51.6%), and adding the own-axis EO, the edges bad on either axis and the pairs gets 51.8%.

### 6.3 The axis rules

**Before any search**: prefer the DR axis with the fewest flipped layer edges. For U/D, look at the U and D layers and count the white and yellow edges whose white or yellow sticker is on the side. 45.5% of best axes found, against 36.3% by chance and 43.8% for plain bad-edge counts.

**After writing your EOs**: prefer the DR axis whose other two axes have the most EOs of at most 5 (51.3%). With 4-movers only it is 49.3%, and that is the same as torchlight's form, the axis whose own EOs are the fewest.

Example: HawaiiChampionship2026 (24 Jul 2026), `R' U' F R L2 F2 D2 B2 D B2 R2 D' R U2 B' U2 F' R D L U' F2 R' U' F`. One row per axis:

| Axis | Bad edges for EO on it, count | EOs of ≤ 4 on it, count | DRs of ≤ 10 with it as the DR axis, count | Shortest DR on it, moves |
|---|---|---|---|---|
| U/D | 2 | 31 | 123 | 9 |
| F/B | 6 | 10 | 331 | 6 |
| R/L | 2 | 36 | 298 | 9 |

F/B has the worst EO, and it is the best DR axis: the most DRs, and a 6-mover, `(F U2 L D' L D)`, a 2c3 4e with a 12-move finish. The DR is proved in Lean, and the finish was checked with nissy. The bare-cube rule can't choose here: each axis has one flipped layer edge.

None of these rules is strong. Half the time the favoured axis is not the one with the most DRs, so it orders the search; it doesn't replace it.

### 6.4 Where the DRs come from

The same lists, counted by the EO axis the DR goes through. A row is the EO axes with a given number of bad edges, over all 23,879 scrambles; the EOs are the ones of at most 5 on normal and inverse, and the DRs are the DR states of at most 10 that go through any EO on that axis, NISS EOs included. Axes with 0 or 12 bad (77 axes) are left out.

| Bad edges on the EO axis | Axes, count | EOs of ≤ 5 on it, mean | DRs through it, mean | DRs per EO |
|---|---|---|---|---|
| 2 | 2,271 | 262.8 | 56.1 | 0.21 |
| 4 | 17,299 | 147.6 | 50.8 | 0.34 |
| 6 | 32,452 | 28.6 | 7.9 | 0.28 |
| 8 | 17,253 | 44.1 | 11.2 | 0.25 |
| 10 | 2,285 | 0.0 | 1.1 | — |

An axis with 2 bad edges has the most EOs and the fewest DRs per EO. So on a scramble where one axis has nearly all the EOs, the other axes give more than their share of the DRs. On the 2,972 scrambles with at least 20 EOs of at most 5, at least 80% of them on one axis, and a DR of at most 10, that axis holds 86.5% of the EOs and 74.4% of the DRs, 12.1 points less [11.2, 12.9]. Over all scrambles the axis with the most EOs holds 61.7% of the EOs and 55.7% of the DRs.

This doesn't mean you should start with the poor axes. The rich axis still has three quarters of the DRs. It means the few EOs on the other axes are worth more each: an EO on a bad axis has done the hard part, and what is left for the DR is the easy axis.

---

## 7. The scramble text

### 7.1 How TNoodle builds an FMC scramble

From the source of tnoodle-lib (the classes `ThreeByThreeCubeFewestMovesPuzzle` and `ThreeByThreeCubePuzzle`, and `Search` and `SearchWCA` of min2phase):

1. It draws a uniformly random state S.
2. It asks min2phase for a solution of S of at most 21 moves. The search keeps going for 200 ms and returns the shortest solution it has by then. It never looks at a solution whose first move is on the R/L axis or whose last move is on the F/B axis, so nothing can cancel with the padding.
3. It inverts that solution, which gives the middle M, and writes `R' U' F`, M, `R' U' F`.

So the cube you solve is P·S·P with P = `R' U' F`. That is a uniformly random state as well, because S is. The source's comments give the reasons: the two-phase solution has an obvious orientation step that a competitor could use, so the scramble is padded (it credits Tom Rokicki for the scheme), with a quarter turn on each of the three axes at both ends so that no EO can be read off the text (it credits Michael Young for `R' U' F`).

min2phase solves in two phases: to DR on some axis, then to solved with DR moves only. It tries all three axes and the inverse, and since the 2019 update of the copy in TNoodle it also tries premoves. Inverted, its solution is the middle of the scramble:

  M = A h B,  with h a run of DR moves on one axis.

A and B are the two phase-1 parts: the phase 1 proper on one side, the premoves on the other. Then A⁻¹·M·B⁻¹ = h is a DR state. So **the middle contains a NISS DR**: undo B on normal and A on inverse, |A| + |B| moves. For the cube you actually solve the padding has to be undone too: on normal `F' U R` and then B undone, on inverse A undone and then `F' U R`, which is |A| + |B| + 6 moves. That is torchlight's count (section 8).

You can read the split off the text: h is the longest run of moves that are DR moves of one axis (for U/D: any U or D turn, and R2, L2, F2, B2). On the 5,771 generated scrambles, where the solver's own split was recorded, the text split has the same length in 98.8% and is within one move in 99.9%; the rest differ where a move at a seam merged or happens to be a DR move.

Two examples from the export. ColombianNationalsFMC2026 (8 Nov 2026):

`R' U' F L' D' U2 F2 L2 F2 U' F L2 F2 R2 B U2 L' U' F' R' D R' U' F`

A is `L'`, h is `D' U2 F2 L2 F2 U'` (DR moves of U/D), B is `F L2 F2 R2 B U2 L' U' F' R' D`. The NISS DR of the scramble is `F' U R D' R F U L U2 B' R2 F2 L2 F'` on normal with `(L F' U R)` on inverse, 18 moves. CrossstraitFMC2016 (9 Apr 2016), the earliest padded scrambles in the export: `R' U' F L' U2 B2 R B2 L F2 L' F2 D' B L D' U' F D2 L B' R D2 R' U' F`. A is empty, h is `L' U2 B2 R B2 L F2 L' F2` (R/L), B is `D' B L D' U' F D2 L B' R D2`, and the DR is `F' U R D2 R' B L' D2 F' U D L' B' D` on normal with `(F' U R)` on inverse, 17 moves. Both are proved in Lean.

### 7.2 The structure, measured

A row is a set of scrambles; the last one is 100,000 random-move sequences of 19 moves for comparison.

| Scrambles | Scrambles, count | Middle, mean moves | Run of 7 or more DR moves, % | Nothing before or nothing after the run, % | Longer outer part is at the end, % | Text DR of the middle, mean moves |
|---|---|---|---|---|---|---|
| official 2016-04 to 2020-07 | 2,516 | 20.06 | 98.6 | 99.3 | 99.6 | 10.70 |
| official 2020-08 to 2026-11 | 5,592 | 19.15 | 95.5 | 42.2 | 62.9 | 10.43 |
| generated | 5,771 | 19.05 | 94.4 | 41.8 | 62.5 | 10.52 |
| random moves | 100,000 | 19 | 16.9 | — | — | — |

The older scrambles are DR moves first, then phase 1: undo the end of the middle and the middle is in DR. Since 2020 there are premoves, so 58% of the scrambles have 1 to 5 moves on the other side of the run as well, and the long part is at the start in 37%. In the export the change falls between March and September 2020, when few competitions were held. The generator here matches the current official scrambles, with middles 0.1 moves shorter on average: the search runs for a fixed time, so a faster computer finds slightly shorter solutions. The run's axis is U/D in 42% of current official scrambles, F/B in 32% and R/L in 27% (50%, 26% and 24% before 2020).

The first and last move of the middle obey the rule of step 2 on all 8,108 official scrambles (exhaustive): the 4th move of the scramble is never an F or B turn, and the 4th from last never an R or L turn.

The text DR of the full scramble is 12 to 19 moves, 17 at the median. It is never one of the DRs you would look for.

How the solution is picked, on the 5,592 official scrambles since August 2020: the official middle is the first solution the search finds in 830 (14.8%), and shorter than it in 4,762 (85.2%), by 1 to 6 moves. It is never longer, and whenever it has the same length it is the same sequence. For the ColombianNationalsFMC2026 scramble above the first solution, inverted, is `R D' R2 D L2 F2 U' B2 R2 U2 B2 F L2 D2 F R U' F' L' D2`, 20 moves, against the official 18; both make the same state (proved in Lean).

### 7.3 What the text predicts

On the 11,363 current scrambles, a row is a feature of the text with its rank correlations with two targets (every 95% interval is within ±0.02):

| Text feature | ρ with DRs of ≤ 10 | ρ with best DR + finish | AUC, easy vs rest |
|---|---|---|---|
| length of the middle | −0.027 | 0.028 | 0.510 |
| length of the text DR | −0.022 | 0.029 | 0.498 |
| length of the run of DR moves | −0.002 | −0.001 | 0.489 |
| length of the shorter outer part | 0.008 | 0.000 | 0.507 |
| length of the longer outer part | −0.017 | 0.017 | 0.492 |
| the longer part is at the end | −0.009 | 0.006 | 0.504 |
| quarter turns in the middle | −0.014 | 0.017 | 0.518 |

Added to the bad-edge baseline, all of them together gain +0.001 of R² [−0.002, +0.004] for the number of DRs and +0.000 for the best DR + finish.

By length, the same scrambles; a row is a length of the middle:

| Middle, moves | Scrambles, count | Easy, % | Hard, % | DRs of ≤ 10, median |
|---|---|---|---|---|
| 17 or less | 433 | 12.5 | 9.9 | 33 |
| 18 | 1,972 | 9.8 | 13.5 | 28 |
| 19 | 5,137 | 9.4 | 13.6 | 29 |
| 20 | 3,585 | 9.3 | 15.1 | 27 |
| 21 | 236 | 9.7 | 16.1 | 24 |

If anything the short ones are a little better, but the correlation (−0.027 [−0.044, −0.009]) is far too small to use.

The text's DR axis is the axis with the most DRs 36.5% of the time, against 36.3% by chance, and holds 1.7% more DRs than the other two axes on average [−0.3%, +4.1%]. On the 2,516 scrambles of 2016 to 2020 there is a small tilt: 38.7% against 36.2%, and 8.4% more DRs [3.7%, 13.2%]. Why the older scrambles have it is not explained here. Either way it is too small to use.

---

## 8. The claims, checked

Statements that the numbers can settle. Questions and guesses are in section 2. Each verdict is one of **True**, **Corrected**, **Depends** (true under one reading, not under another), **Open** and **Withdrawn** (taken back at the time), and is no stronger than what was measured: 23,879 scrambles, DRs of at most 10 through an EO of at most 5, optimal finishes. The one correction has its example in the row.

**EO counts and bad edges.** These were said as rules of thumb for when to dig deeper, not as statistics. What is checked is the signal behind each: does the condition go with a hard or an easy scramble. One row per statement:

| Statement | Who | Verdict |
|---|---|---|
| Asked "how bad would a scramble have to be for y'all to check RZP in 6 (7 for DR-3c2e)": "if I have like <8 4 movers. It's really just when it feels like there won't be many rzp in 5 / or if I go for rzp in 5 but then I exhaust those quickly and have to look for 6" | Java [11 Jun 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1117627730847080608); Tom Nelson [11 Jun 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1117629397365686334) | **True** as a signal: with fewer than eight 4-movers 31% of scrambles are hard, against 4% of the rest. It holds whichever way the EOs are counted (table below). |
| "if i have less than 30 5movers and barely any 4movers i check rzp in 6", and "but i feel like these exact numbers are dependant on how many eos you can find(for example how many niss 5movers you write) and how fast you can check things" | Yura Riabov [9 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1260223364677767228), [9 Jul 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1260223585105084436) | **True** as a signal: with fewer than 30 EOs of exactly 5 and at most two of 4 or less (no NISS), 59% are hard and 0.5% easy. That is the worst 3% of scrambles. The numbers do depend on what is counted, as Yura Riabov says. |
| "but if you had 4 or 2 bad it's probably a good scramble", after a list of 4-move NISS EOs that are "Probably only worth checking on terrible scrambles" | Tom Nelson [5 Jan 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1060765408237457518), [5 Jan 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1060763966122512385) | **True**: with an axis at 2 or 4 bad, 3.5% of scrambles are hard, against 28.5% of the rest, and the median is 52 DRs against 11. |
| "Just a thought, what are the chances that a scramble's EO distribution only consists of 0, 2, 4 and 8?", "Cause obviously 6 10 and 12 are trash", "(Well 6 isn't trash but it's definitely way more annoying than 8 and slightly worse objectively)", "13.907% that's sort of lucky I guess" | jisu101 [3 Nov 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1567137823751020587), [3 Nov 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1567137898933780600), [3 Nov 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1567138262533800020), [3 Nov 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1567141993912737856) | **True**: such scrambles (13.7% of this sample; 13.907% exactly, [*EO to DR*](../eo-to-dr/)) are easy twice as often as the rest, 17.7% against 8.4%. And 6 is worse than 8: an axis with 6 bad has 29 EOs of at most 5 and 8 DRs through it on average, one with 8 bad has 44 and 11 (section 6.4). |
| "i think youre more likely to get a 4 move eo from 8 than 6" | wen [3 Nov 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1567140241989701753) | **True**: 28.9% of the states with 8 bad edges have an EO of at most 4, against 22.5% of those with 6 (exact for one axis, [*EO to DR*](../eo-to-dr/)). The DRs follow the EOs (previous row). |
| "23 on no sub5 eos 10/8/8 scramble / vs. / 22 on 2move eo scr with a billion 4 movers / ^first feels better much better" | Lewis Isom [22 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1276313125120905297) | **True** for what it takes for granted: 10/8/8 with no EO under 5 is hard 52.5% of the time (120 scrambles), and with an EO of 2 or less a scramble is hard 0.2% of the time and easy 32.2%. |
| "But 10/8/8 can have a 3mover with something easy while 4move eo spam can be relatively bad" | Yura Riabov [22 Aug 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1276313553783099522) | **True**, and both are rare. 10 of the 258 scrambles with 10/8/8 have an EO of 3 or less; none of the ten is hard (Juhannus2024, appendix B). Of the 667 scrambles with 50 or more 4-movers, 12 have a best DR + finish of 22 and none worse (EstonianOpen2019, appendix B). |
| "the only real heuristics we have are eo-related, and eo counts by themselves are not very predictive imo" (the whole message is in section 2) | JTuu [2 Nov 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1302417164011311134) | **Depends** on what is predicted. For the number of DRs the count of 4-move EOs has ρ = 0.78, the best of any feature. For the best DR + finish it has −0.54, and nothing does better than a third of the variance (section 4). The first half is **True**: nothing that isn't EO-related adds more than 0.03 of R². |
| "Awful scramble / 27 linear 5 movers / 58 total" | zakimoshi [27 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1410348093366337697) | **True**: 27 EOs of 5 on normal and inverse by the count used here, none shorter, and 3 DRs of at most 10 (appendix B). The 58 with NISS are not counted here. |

The signals behind the first rows, with both ways of counting. A row is a condition; *yes* is the scrambles that meet it, *no* the rest:

| Condition | Scrambles that meet it, % | Easy if yes, % | Easy if no, % | Hard if yes, % | Hard if no, % |
|---|---|---|---|---|---|
| fewer than 8 EOs of ≤ 4, normal + inverse | 36.6 | 2.6 | 13.8 | 30.9 | 4.0 |
| fewer than 8 EOs of ≤ 4, normal only | 56.7 | 4.7 | 16.2 | 22.5 | 2.5 |
| fewer than 8 EOs of ≤ 4, normal + inverse, both endings counted | 21.2 | 1.9 | 11.8 | 38.1 | 7.4 |
| fewer than 30 EOs of 5 and at most 2 of ≤ 4 | 3.2 | 0.5 | 10.0 | 58.9 | 12.4 |
| an axis with 2 or 4 bad | 58.6 | 14.0 | 3.6 | 3.5 | 28.5 |
| no axis with 6, 10 or 12 bad | 13.7 | 17.7 | 8.4 | 5.7 | 15.2 |
| 10/8/8 and no EO under 5 | 0.5 | 0.8 | 9.7 | 52.5 | 13.7 |
| an EO of 2 moves or less | 7.8 | 32.2 | 7.8 | 0.2 | 15.0 |

**The axis and the corners.** One row per statement:

| Statement | Who | Verdict |
|---|---|---|
| "This is also true when you take a completely scrambled cube, and you twist the corners to make CO on the three different axis, they're always the same number of quarter turns." | Levi Gibson [21 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143384156198416426) | **True**, for every one of the 40,320 corner permutations, and for the inverse (exhaustive). |
| "Even though there are so many things that impact the number of quarter turns before DR is made, it seems like on average the nuimber of quarter turns in the DR is impacted." and "If you take a scrambled cube, and twist all the corners to make them oriented, and you count the number of quarter turns, it can predict if you are gonna get DRs with good or bad corners (on average)." (the same post, which opens "I haven't found any practical uses for this") | Levi Gibson [21 Aug 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1143384156198416426) | **True** on average, and small: DRs with at most 2 QT are 23% of the DRs on QT 0 scrambles and 16% on QT 5 scrambles; ρ = +0.07 [+0.06, +0.08] between the scramble's count and the mean count of its DRs (section 5.4). |
| "(I will say, most of the time I use a dr on the same axis as the "dr" portion in the scramble)" (the whole message is in section 2) | maxooma [29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256589675200778352) | **Depends**. It reports maxooma's own solves, which can't be checked here. As a rule it doesn't hold on current scrambles: that axis is the best one 36.5% of the time against 36.3% by chance. On 2016 to 2020 scrambles it held 8% more DRs than the others (section 7.3). |

**The scramble text.** One row per statement:

| Statement | Who | Verdict |
|---|---|---|
| "if the scramble seq has an n-move DR excluding the R' U' F, then you already know there's an (n+3)-move DR on that same axis", struck out, then "wait", "sorry that's not true", "n+6 moves with NISS lol" | torchlight [29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256591562209628201), [29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256591714714521671), [29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256591730501746749), [29 Jun 2024](https://discord.com/channels/1007840975726575667/1007841335434285126/1256591781672390656) | n + 3: **Withdrawn**. n + 6 with NISS: **True**, on every one of the 8,108 official scrambles (section 7.1). |
| "FMC scrambles are random state, not only the "inner scramble". It is done by solving "F' U R random position F' U R" and then putting back the padding at both ends. / Many solutions are found using Kociemba's two phase algorithm and the first one which does not cancel with the padding is kept. / So to answer your question, a position with a short optimal does not necessarily have a short scramble, if for example the optimal solution doesn't correspond to a quick find in Kociemba algorithm (i.e. it doesn't use a short DR) or if it uses a longer sequence to avoid cancelling with the padding. / Reciprocally, if the scramble is short then that means that "F' U R random position F' U R" has a short solution, which does not mean that the actual random position has a short optimal." | Louis [15 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1229460118119383131) | **True**, with one detail **Corrected**. The state, the padding and the conclusion are right. The source draws the inner state and pads it, which comes to the same distribution (next row), and the length of the middle has ρ = 0.007 with the optimal length. The detail: the solution kept is the shortest found in 200 ms, not the first that doesn't cancel. On 5,592 official scrambles since August 2020 it is the first in 14.8%. Example: for ColombianNationalsFMC2026's `R' U' F L' D' U2 F2 L2 F2 U' F L2 F2 R2 B U2 L' U' F' R' D R' U' F` the first solution gives a 20-move middle, and the official one has 18 (section 7.2). |
| "Even if we generated a random position and *then* padded, it would still be uniformly random (because padding is a bijection on the set of positions)." | Sebastiano Tronto [15 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1229472462698446920) | **True**, and that is what the source does. The four sets of scrambles have the same DR landscape (section 3.2). |
| "it's just the 4th move not being a B-move and the 4th from last move not an L-move. And ofc the usual padding of `R' U' F` being on both ends.", and of the reason: "It's just how it was programmed. Prob to avoid stuff like `R' U' F B' F'...`" | DougCube [24 Oct 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1563590045577908265), [28 Oct 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1565088348807241799) | **True**, in the source and on all 8,108 official scrambles. The source bars the whole axis at each end, F and R turns included. |
| "This is only true in hindsight but if you look at the R3A2 scramble, it very clearly isn't following the usual structure that scrambles have (with a long-ish DR part etc) and has barely any half turns at all", of a scramble reported not to have come out of the generator | wen [14 Oct 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1559809438263541771) | **True** for the usual structure: 95.5% of current official scrambles have a run of 7 or more DR moves of one axis in the middle, against 16.9% of random-move sequences (section 7.2). The scramble wen means is not in the data. |
| "side note short scrambles i had were almost always shit" | rogo [15 Apr 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1229441961342009435) | **Depends**. It reports rogo's own scrambles. Over all current scrambles short ones are not worse: with a middle of 17 moves or less 9.9% are hard, against 15.1% at 20 moves (section 7.3). A short easy one: ColomboCubingChristmas2023, a 15-move middle, 402 DRs and a best DR + finish of 18 (appendix B). |

---

## 9. What this does not cover

- **What a solver finds.** A *DR* here is every DR state a computer lists through an EO of at most 5. A solver finds a fraction of them. The counts say how rich a scramble is, not what one person gets out of it in an hour.
- **Human finishes.** The finish is the optimal one. A human finish is longer and depends on the subset as well as on the optimum. The best DR + finish ranks scrambles; its values (14 to 26) are below anything written in an attempt.
- **DRs of 11 moves.** The lists stop at 10 moves. With 11-move DRs the best DR + finish would sometimes be lower, and the counts ten times larger.
- **EOs with NISS, as features.** The EO counts are linear, on normal and on inverse. The DR lists do go through NISS EOs.
- **How you count.** The EO counts here agree with nissy's listing to within a few EOs per axis, and with zakimoshi's count on the one scramble where both exist. Your own count may run differently, so treat the cut points of table 2 as approximate.
- **The optimal DR.** Zagros and Levi Gibson asked about the scramble to DR length without an EO first. Only EO-first DRs are counted here.
- **The 2016 to 2020 tilt** towards the text's DR axis is measured and not explained.
- **Blockbuilding.** Solved pairs are the one feature here that points at the optimal length (ρ = −0.24). Nothing else about blocks was measured.
- **The generator.** The generated scrambles come from the same solver with the same call, on a faster computer than most organisers', so their middles are 0.1 moves shorter. No text feature shows any effect on the official scrambles alone either.
- **Scramblers other than TNoodle**, and anything a solver learns from the first EOs beyond their number and length.

---

## Appendix A: how it was computed, and what checks it

The code of this study is not in the repository yet.

**The DR lists.** cubelib-cli with `EO[niss=always;max=5] > DR[niss=before;max=10]`, the same steps and the same per-scramble deduplication as the DR population in `gaps/research` of the [repository](https://github.com/ArhanChaudhary/fmc-analysis), which supplies the 10,000 uniform scrambles (its lists go to 11 moves and are cut to 10 here). Every DR state gets its optimal finish and subset from the exact table of [*Judging a DR*](../judging-a-dr/). Four finishes were recomputed with nissy (12, 13, 8 and 13 moves, as in the table). On 20 scrambles, the DRs of at most 10 from a run to 11 moves and from a run to 10 moves are the same 650 states. For section 6.4 the lists were made again with the EO axis of each DR kept; on 30 scrambles the per-axis counts agree with the first lists.

**The scrambles.** Official: the table of scrambles of the WCA results export of 13 November 2026, event 333fm, every scramble that starts and ends with `R' U' F` (8,108; the 843 older ones are not padded), dated by its competition. Generated: tnoodle-lib's min2phase compiled as it is, called the way `ThreeByThreeCubePuzzle` calls it (21 moves at most, 200 ms, first move not on R/L, last move not on F/B, solution inverted), with a subclass that only records which part of the solution is phase 1, phase 2 and premoves. For each generated scramble the middle, replayed on the cube model, gives the state the solver was handed. The first solution of section 7.2 is the same call with the 200 ms set to 0, which has no timing in it.

**The cube model and the features.** A cubie model with stickers, written for this study and tested against itself (inverses, sticker round trips, and that only quarter turns of an axis change that axis's EO and corner orientation). The optimal EO lengths over the 2,048 EO states come out as 1, 2, 25, 202, 620, 900, 285 and 13 states for 0 to 7 moves, the distribution proved in [*EO to DR*](../eo-to-dr/). The corner QT table is a search over the 40,320 corner permutations from the 96 in HTR; it agrees with the last digit of the corner case on 3,057 of 3,064 DRs, and the other 7 are 0c0 states with all eight corners in the other tetrad, where the name says 0 and the count is 2. All 8,532 optimal solutions of DougCube's sheet solve their scrambles on the model. The sheet's EO columns are not used: its linear EO is shorter than nissy's and this study's on 1,843 of the 7,689 padded scrambles.

**Statistics.** Rank correlations with 400 bootstrap resamples of scrambles; AUC with 200. Linear models and gradient boosting (scikit-learn, 400 rounds) are fitted on a random two thirds of the scrambles and scored on the rest. The per-axis hit rates are bootstrapped over scrambles.

**Lean.** A Lean 4 file (no Mathlib, `native_decide`), on the sticker model of the [*EO to DR*](../eo-to-dr/) certificate. A state is a DR on an axis when every sticker of that axis's colours is on one of its faces and the slice edges keep their second colour on its axis; that set has 8!·8!·4!/2 states and contains the DR group, so it is the DR group. Proved: the two text DRs of section 7.1; every DR written out in appendix B; for each of them that the scramble itself is not a DR on that axis; that the official middle and the first solution of section 7.2 make the same state; four sanity statements. 30 theorems, and a false one (that `R U` is a U/D DR) is rejected.

## Appendix B: worked scrambles

Counts are as defined under Terms. Every DR below was replayed on the cube model and is proved in Lean.

**An easy one.** HawaiiChampionship2026 (24 Jul 2026): `R' U' F R L2 F2 D2 B2 D B2 R2 D' R U2 B' U2 F' R D L U' F2 R' U' F`. Bad edges 2/2/6, shortest EO 3, 77 EOs of at most 4 and 810 of at most 5: table 1's first class, and table 2's row for a 3-move EO with 50 or more 4-movers. 752 DRs of at most 10, 176 good ones. The best: `(F U2 L D' L D)`, F/B, 2c3 4e, finish 12, 18 in all.

**A hard one.** FewestMovesBogota2025 (12 Jan 2025): `R' U' F L F' B2 L2 U2 F2 U B2 U' L2 D' R2 B2 R' D R2 B D' F' D R' U' F`. Bad edges 6/6/10, shortest EO 5, 19 EOs of at most 5: table 1's last class, table 2's last row. One DR of at most 10: `B' U (B' L2 U' F2 B' L2 R B)`, R/L, 2c4 4e, finish 13, 23 in all.

**Short text, easy.** ColomboCubingChristmas2023 (23 Dec 2023): `R' U' F L F2 D2 R' B2 F2 R' B2 D R F2 R' D L B' R' U' F`, a middle of 15 moves. Bad edges 2/4/6, shortest EO 3, 56 EOs of at most 4. 402 DRs of at most 10, 144 good ones. The best: `D (D F' R2 U2 F' D2 B2 L B)`, R/L, 4a1 4e, finish 8, 18 in all.

**10/8/8 with a 3-move EO.** Juhannus2024 (20 Jun 2024): `R' U' F R2 F' U2 R D B2 L D' F2 R F2 U' R2 B2 U' R2 D2 F2 B R' U' F`. Bad edges 8/8/10; `(L D U)` solves EO on U/D on the inverse (checked with nissy). 18 EOs of at most 4, 25 DRs of at most 10. The best: `(L B2 U' D' R D2 B L R F)`, R/L, 2c5 6e, finish 11, 21 in all.

**Many 4-movers, and no better than 22.** EstonianOpen2019 (21 Sep 2019): `R' U' F D2 F2 D B2 F2 D B2 D L2 F2 R' B L2 R2 B2 D2 L F R2 F R' U' F`. Bad edges 4/4/4, shortest EO 2, 57 EOs of at most 4, 179 DRs of at most 10. The best: `B' D2 L2 R2 B R (R F2 U)`, F/B, 4b5 2e, finish 13, 22 in all.

**zakimoshi's awful scramble** ([27 Aug 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1410348093366337697)): `R' U' F D B2 D B2 U' F2 L2 U2 F2 R2 D' F2 L' F' R' F D F L2 D R' U' F`. Bad edges 6 on U/D, 6 on F/B, 8 on R/L. The shortest EO is 5 on U/D and F/B and 6 on R/L, on both sides; 27 EOs of 5. Three DRs of at most 10: `B' D' R U' D F R2 U (B L)` and `B' D' R' U' D F' L2 D (B L)` on F/B, `L2 B (F' D2 B R D' L2 U L)` on U/D.

**JTuu's scramble** ([28 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1520696576492699718)): `R' U' F D2 B2 D2 F2 D F2 U' R2 F2 L2 U2 F D2 R' B U F2 R D' R D2 R' U' F`. Without NISS, 42 of its 45 EOs of at most 5 are on F/B; the other 3 are the three inverse EOs on R/L in the list JTuu posted of the ten that are not on F/B ([28 Jun 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1520698373605429328)). Its two DRs of at most 10 are both on R/L, through an F/B EO: `U2 R B' D' F L R' U' L' D` and `U2 R B' D' F L' R D' L' U`. Both rules of section 6.3 miss here. The EO rule rules out F/B and then picks U/D (45 EOs on its two EO axes, against 42 for R/L). The bare-cube rule picks U/D too: 3 flipped layer edges, against 4 on F/B and 5 on R/L.

## Docs referred to

- tnoodle-lib, the scrambling library of TNoodle: [github.com/thewca/tnoodle-lib](https://github.com/thewca/tnoodle-lib), as of 5 October 2026 (commit d01a947). min2phase is by Shuang Chen; the update with premoves entered TNoodle's source on 30 June 2019.
- WCA results export, version 2.0.2 of 13 November 2026: [worldcubeassociation.org/export/results](https://www.worldcubeassociation.org/export/results).
- DougCube, [*All WCA Scrambles by DougCube (Main)*](https://docs.google.com/spreadsheets/d/183AYpjKz4fZZAy5Hx5lxEthD2f356ReZG-uHPm_HWcY), tab FMC, as of 16 July 2026.
- [*Judging a DR*](../judging-a-dr/), [*EO to DR, and scramble to DR*](../eo-to-dr/), [*When to switch an EO*](../eo-switch/), and `gaps/research` in the [repository](https://github.com/ArhanChaudhary/fmc-analysis).
- Levi Gibson, [*Trigger averages*](https://docs.google.com/spreadsheets/d/1ye-vV4OeGBofmlZIJyIMy_dEoZk9Xz-v2ijtcTyO5AM).
- cubelib (Mallard) by Joba: [github.com/Jobarion/cubelib](https://github.com/Jobarion/cubelib). nissy 2.0.8 by Sebastiano Tronto: [nissy.tronto.net](https://nissy.tronto.net).
