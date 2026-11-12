# Insertions: corrections, and what the numbers settle

*Goes with the write-up on insertion cost by skeleton type, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#non-dr-discussion, #fmc-discussion or #fmc-theory). Docs are listed with links at the end.

**What everything below is measured against:**

- **Every alg of 12 moves or fewer** for every corner-only and edge-only leftover that one or two 3-cycle insertions solve, and for 2c2e. Exhaustive, by joining all 6-move sequences with all 6-move sequences.
- **Which leftovers one, two or three 3-cycles can make**, counted over all corner states and proved in Lean.
- **The exact best insertion of a skeleton**: every spot, every alg within a cap on the alg's length, two comms allowed to nest. The caps are 8 (pure 8-movers; for edges the 6-, 7- and 8-movers), 10 and 12. Cap 8 on a 3c is the true best over all 8-movers at all spots.
- **Random skeletons**: random move sequences with a random leftover of the type, 20,000 per type and length at cap 8 (5,000 for 2tc, 2fe and the two kinds of 2e2e), fewer for two comms at cap 10 (200 to 2,000) and at cap 12 (100, at 20 moves only). They are not solves: no blocks, no EO.
- **201 worked examples from real solves, 191 distinct skeletons**: 168 examples from the server and 33 from Cyprian Kalbarczyk's example solves, each replayed on a sticker-level cube before it was counted.

Every scramble and solution printed below was replayed on that sticker-level cube.

Section A is the docs. B is what was said in the channels that the numbers go against, each with an example. C is what depends on the alg list or on which skeletons you look at, where nobody is wrong. D is what checked out, which is most of it.

---

## A. The docs

**A1. The tutorial's table (Sebastiano Tronto, section 2.4.10, "Move count (an estimate)"), line by line.**
The tutorial says of it: "It is a heuristic estimate, not a mathematically proved one", and that the numbers depend on the algs you know and on the skeleton's length. Next to the computed means:

| Row of the tutorial's table | Tutorial | Random skeletons of 16 moves, cap 8: mean added (skeletons) | Random, 20 moves, cap 8 | Random, 20 moves, cap 10 | Random, 20 moves, cap 12 | Posted skeletons, cap 8: mean added (skeletons, their mean length) |
|---|---:|---:|---:|---:|---:|---:|
| Corner 3-cycle | 5/6 | 6.08 (20,000; fits on 99%) | 5.90 (20,000) | 5.85 (20,000) | 5.77 (20,000) | 5.12 (89, 18.4 moves) |
| Edge 3-cycle | 7 | 6.01 (20,000; fits on 49%) | 5.95 (20,000; fits on 56%) | 6.05 (20,000) | 5.95 (20,000) | 4.79 (14 of 17 where something fits, 20.3 moves) |
| 2 Twisted Corners (2 comms) | 8 | 8.05 (5,000) | 7.71 (5,000) | 7.34 (200) | not run | none posted |
| 3 Twisted Corners (2 comms) | 9 | 9.89 (20,000) | 9.50 (20,000) | 9.34 (500) | 8.56 (100) | 10.00 (2, 13.0 moves) |
| 4 Corners (double swap) | 9/10 | 9.49 (20,000) | 9.13 (20,000) | 8.48 (500) | 7.87 (100) | 9.00 (3, 16.7 moves) |
| the twisted double swap (not a row of the table) |  | 9.01 (20,000) | 8.73 (20,000) | 8.66 (500) | 8.30 (100) | 8.30 (10, 17.7 moves) |
| 4 Corners (3 + 1 twisted) | 10 | 10.22 (20,000) | 9.90 (20,000) | 9.73 (500) | 9.44 (100) | 8.65 (20, 16.9 moves) |
| Corner 5-cycle | 10/11 | 10.65 (20,000) | 10.37 (20,000) | 10.03 (2,000) | 9.49 (100) | 9.85 (33, 16.7 moves) |
| 2 Corners and 2 Edges (double 2-cycle) | 10 | not sampled | not sampled | not sampled | not sampled | not sampled |

*Random skeletons* are the samples described above, and each cell has the number of skeletons behind it in brackets. Cap 12 for the two-comm types is on 100 skeletons that are not the skeletons of the cap-8 column, so do not read a step off this table: on those same 100 skeletons a 5c goes from 10.10 at cap 8 to 9.49 at cap 12. *not run*: cap 12 was not run for a 2tc. *Posted skeletons* are the real ones, which are the solves people chose to show; they are shorter than 20 moves (mean length in the brackets), and the 3tc cell is two 13-move skeletons.

- **Corner 3-cycle, 5/6**: 5.90. Right.
- **Edge 3-cycle, 7**: on random skeletons 6.05 with every alg up to 10 moves; with 8 moves or fewer nothing fits on 44% of them. The tutorial's footnote already says "this varies a lot", so nothing to correct; C4 has what it varies with.
- **2 twisted corners, 8**: 7.71 at 20 moves, 8.05 at 16. Right.
- **3 twisted corners, 9**: 9.50 with 8-movers, 9.34 with algs up to 10 (500 skeletons), 8.56 up to 12 (100). Right, half a move low for pure comms.
- **4 corners (double swap), 9/10**: 9.13. At the low end of the range. The twisted double swap, which has no row in the table, is 8.73.
- **4 corners (3 + 1 twisted), 10**: 9.90. Right.
- **Corner 5-cycle, 10/11**: 10.37 at 20 moves, 10.65 at 16. Right.
- **2 corners and 2 edges, 10**: not sampled. What can be said: no 2c2e alg is shorter than 10 moves, so 10 is what an insertion costs before anything cancels.

Nothing to correct in the table. Its two caveats are both measurable: ten more moves of skeleton take 0.44 off a 3c insertion and 0.71 off a 5c; and going from 8-movers to every alg of 12 moves takes 0.13 off a 3c and about 0.61 off a 5c (the 5c on the same 100 skeletons).

**A2. The tutorial, section 2.4.1: "It happens extremely rarely that the best insertion is given by a 9 move commutator (or longer)".**
For 9-movers that is exact: on random 20-move 3c skeletons a 9-mover is the best 0.60% of the time. A 10-mover beats every 8- and 9-mover on 4.7% of skeletons, one in 21, and by a single move 77% of those times. The tutorial says as much elsewhere ("On rare occasions, 10 moves “sledge insertion” corner commutators", "may cancel many more moves than the standard 8-move commutators"), so this is a number for how rare, not a correction. An example:

Scramble: `R' U' F U' D R2 F2 U L2 U B2 U2 R2 D' B' D L2 F U R' D' L U2 R D' R' U' F`

Skeleton: `F D' R' D F' L2 B2 R U F' U2 D' B' R' D2 F L2 U' B2 U` (20), leaves a corner 3-cycle: UBL → DBR → UFL → UBL

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

**A3. Which leftovers take how many comms** (Yurii Riabov's guide; the tutorial, 2.4.4 and 2.4.5). Nothing to correct. See D.

---

## B. Said in the channels

**B1. "if you can't find a 3c, what is generally better", "2c2c, 3c1t, or 5c?"** (jisu101, [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125109978632212), [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125157483315321)).
argonblue ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125544114131034)): "i think 3c1t > 2c2c > 5c. mostly because a twist gives you the most freedom to pick comms". jisu101, at the time ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125667565080657), [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125708480516218)): "True but so does 2c2c, you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions".
With 8-movers on 20-move random skeletons the order by cost is twisted 2c2c (8.73), pure 2c2c (9.13), 3c1t (9.90), 5c (10.37). So a 2c2c is the cheaper leftover, by 0.77 to 1.17 over a 3c1t. Counted per spot, a 2c2c has 24 first comms that leave a 3c and a 3c1t has 9, which is what jisu101 answered. The posted skeletons are too few to rank the 4-corner types (3 pure 2c2c, 10 twisted, 20 3c1t, of different lengths); they only agree that a 5c is the dearest (9.85 on 33 skeletons, against 9.00, 8.30 and 8.65).

A typical skeleton of each, 20 moves, 8-movers. Each costs its type's average, rounded: they show what the averages look like on a cube, and the order rests on the 20,000 skeletons per type, not on these three.

Scramble: `R' U' F L B2 L B2 F2 U2 L B2 U2 B2 R' D2 F' R B' U2 F R2 U' R U R' U' F`

Skeleton: `U' R2 F2 D' R' D' B R' U2 B' L' U F L' D2 B D2 R2 B' R2` (20), leaves two corner swaps, each with a twist: DFL ↔ UFR, DBR ↔ DFR

**Best with two 8-move comms**: 29 in all.

```
U' R2 F2 D' R' D' B R' U2 B' L' U F L' D2 * B D2 R2 B' R2
* = U' B D' B' U B D B' // (8-3/25)
U' R2 F2 D' R' D' B R' U2 B' L' U F L' U' D2 B D' ^ B' U B D' R2 B' R2
^ = D B U2 B' D' B U2 B' // (8-4/29)
Solution: U' R2 F2 D' R' D' B R' U2 B' L' U F L' U' D2 B2 U2 B' D' B U2 B2 U B D' R2 B' R2 (29)
```

Scramble: `R' U' F B2 U2 L2 B2 L2 D' L2 D B2 D2 F2 U2 L R2 U' B' D' L B F R2 D R' U' F`

Skeleton: `U' D2 B' D2 B' D L2 U R2 B' U2 D B L D B' U2 L' D' L'` (20), leaves two corner swaps, no twist: DFL ↔ DFR, DBR ↔ UFR

**Best with two 8-move comms**: 29 in all.

```
U' D2 B' D2 B' D L2 U R2 B' U2 ^ D B L D * B' U2 L' D' L'
* = D F2 D' B' D F2 D' B // (8-3/25)
^ = F' D B D' F D B' D' // (8-4/29)
Solution: U' D2 B' D2 B' D L2 U R2 B' U2 F' D B D' F D L D2 F2 D' B' D F2 U2 D' L' D' L' (29)
```

Scramble: `R' U' F B2 L F2 L' D2 R' F2 U2 R2 U2 L F2 R' U' L F R' U2 B' R D2 L U' R' U' F`

Skeleton: `L' B' D2 R D R' B' R2 U2 F R2 U2 D' L2 F2 U' L' D2 B2 U'` (20), leaves a twisted corner 3-cycle and one twisted corner: DFL → UFL → UBR → DFL, DBL twisted clockwise

**Best with two 8-move comms**: 30 in all.

```
L' B' D2 R D R' B' R2 U2 F R2 U2 D' L2 F2 * U' L' D2 B2 U'
* = F D' F' U' F D F' U // (8-3/25)
L' B' D2 R D R' B' R2 U2 F R2 U2 D' L2 F' D' F' U' ^ F D F' L' D2 B2 U'
^ = U F' U' B U F U' B' // (8-3/30)
Solution: L' B' D2 R D R' B' R2 U2 F R2 U2 D' L2 F' D' F2 U' B U F U' F B' D F' L' D2 B2 U' (30)
```

Jay's "i didn't notice a meaningful different between 2 insertion 4c types" ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443789835356606609)) is what a one-move difference with a spread of more than a move looks like solve by solve.

**B2. Checking every other move "still guarantees you'll find them"** (notkevin, [7 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1436457200880189582): "if you're expecting at least a -3 somewhere, it has to cancel at least a full move, so checking every other still guarantees you'll find them").
Nearly. On random 3c skeletons of 20 moves, when the best 8-mover insertion is an 8-3 or better, checking every second spot and both ends finds an insertion that good 97% of the time. All of those misses (every one over seven skeleton lengths) are next to two moves on opposite faces, where the full cancel reaches across the pair and the shifted alg lands two spots away. Nothing better than an 8-4 was missed on any of 140,000 skeletons. alkamaass had said the rule is not thorough when recommending it ([31 May 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246266143551787058)): "this isn't thorough tho bc it can miss stuff like R (R blah blah B' ) B'". Example:

Scramble: `R' U' F R U2 F2 D2 R' U2 F2 R' F2 L2 R F2 R U R F' L2 B U2 F' L F' R' U' F`

Skeleton: `F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' F' B U2 B' L D` (20), leaves a corner 3-cycle: DBR → UBR → DFR → DBR

**The best 8-mover insertion**: 25 in all, the only 8-3 in the skeleton, after move 16.

```
F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' F' B * U2 B' L D
* = F D F' U F D' F' U' // (8-3/25)
Solution: F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' B D F' U F D' F' U B' L D (25)
```

Counting spots from 0 (before the first move), the 8-3 is at spot 16. Checking spots 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 and both ends finds nothing better than an 8-1. The spot is right after the pair `F' B`.

**B3. "sub-22 for 3C skeleton", "sub-20 for every other skeleton"** for sub-30 (sequesteredcuber, [8 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1127188954995769364)).
Two moves apart is too close. With 8-movers on random skeletons a 3c in 21 gives sub-30 99.6% of the time; a 5c in 19 gives it 48%, a 3c1t in 19 63%. For the same expected total as a 20-move 3c, a 5c has to be 4.8 moves shorter, a 3c1t 4.4, a pure 2c2c 3.5 (write-up, section 7). A 19-move 5c with the most common outcome, 30:

Scramble: `R' U' F L2 D B2 L2 U B2 L2 D2 B2 D2 F2 U' R B L' B' F L' U' L R2 D R' U' F`

Skeleton: `F2 D2 R2 D' F' L F R' D B2 L B R' B' U' B2 U2 L2 D` (19), leaves a corner 5-cycle: DBL → UFL → DBR → UBR → UBL → DBL

**Best with two 8-move comms**: 30 in all.

```
F2 D2 R2 D' F' L F ^ R' D B2 L B R' * B' U' B2 U2 L2 D
* = D2 B' U2 B D2 B' U2 B // (8-3/24)
^ = D R' U2 R D' R' U2 R // (8-2/30)
Solution: F2 D2 R2 D' F' L F D R' U2 R D' R' U2 D B2 L B R' D2 B' U2 B D2 B' U B2 U2 L2 D (30)
```

---

## C. Depends on the alg list or on the sample

Nobody is corrected here. Each of these is a figure or a report that is right for some alg list or some set of skeletons, and the numbers say which.

**C1. "more like 9 for pure 2-2", "like 9.5 for 2-2 with a twist", "like 10 for 3c1t"** (cpaul, [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760547458842644), [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760556908740648), [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760590995853465)).
A pure 2c2c costs 9.13 and a 3c1t 9.90 with 8-movers at 20 moves. Which 2c2c is the cheaper depends on the alg length: with 8-movers alone the twisted one (8.73), with algs of up to 10 moves the pure one (8.48 against 8.66, 500 skeletons each), which is cpaul's order.

**C2. 3tc "mid to high 8 from my experience"** (Phuwish, [4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239016290553917)).
On random 20-move skeletons a 3tc costs 9.50 with 8-movers and 8.56 with every alg of up to 12 moves (100 skeletons). So the figure is lower than pure comms give on a random skeleton and within reach of a longer alg list. The posted 3tc skeletons are only 2.

**C3. "5-6, 8-9, 6-8 for good 2c2c, 8-9 for bad 2c2c"** (Baiqiang, [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443756810715664537), for 3c, 3c1t and 2c2c; "this is i expected not avg expected", [28 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443860338440146986)).
Not averages, in Baiqiang's words. Which 2c2c is the good one was asked (kyh, [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443757686025093241): "btw you mean good like as in the co matches, the stickers swap with eachother") and not answered, so the two 2c2c figures are not pinned on pure and twisted here. What comes out, in mean added:

| | 3c1t | pure 2c2c | twisted 2c2c |
|---|---:|---:|---:|
| Random 20-move skeletons, 8-movers (20,000 each) | 9.90 | 9.13 | 8.73 |
| Random 20-move skeletons, algs of up to 10 moves (500 each) | 9.73 | 8.48 | 8.66 |
| Random 20-move skeletons, algs of up to 12 moves (100 each) | 9.44 | 7.87 | 8.30 |
| Posted skeletons, 8-movers | 8.65 (20 skeletons) | 9.00 (3) | 8.30 (10) |

On the posted skeletons with a comm plus an alg of up to 12 moves each, a 3c1t averages 7.65 and a 2c2c 6.85. So figures of Baiqiang's size come out of the skeletons people post, searched with a full alg list. Jay had guessed at the alg list in the same exchange ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443789835356606609)): "maybe there's some non 3c type insertion method for 2c2c that lowers the movecount that far". The 10-move 2c2c algs are one.

**C4. Edge 3-cycle, 7** (the tutorial's table, with its footnote: "Warning: this varies a lot! If edges are oriented early in the solve, you have better chances of finding a good insertion (6 or 8 movers).").
On random 20-move skeletons a 3e costs 6.05 with every alg of up to 10 moves; with algs of 8 moves or fewer nothing fits on 44% of them. The short algs do need oriented edges: every edge 3-cycle whose three edges are oriented on all three axes has a 6-mover and no other has one, and an alg of 8 or fewer needs them oriented on at least two. The 17 posted 3e skeletons cost 3.18 at cap 10, but all of them were posted with their insertion, and they are that cheap whether their edges are oriented or not (write-up, 9.2). So the 7 is a fair figure for some alg list on some skeletons, and these samples do not pin down which.

**C5. "In my stats, I found that the best insertion points tend to be in the first 1/3 or last 1/3 of the skel."** (DougCube, [8 Jul 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1524584097085657221); "no idea why", [8 Jul 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1524584188269953187)).
Not reproduced, and not refuted. On random 3c skeletons the best 8-mover insertion is in each third a third of the time. On the 89 posted 3c skeletons it is in the first third 24% of the time, the middle 39%, the last 37%. 23 of those are DougCube's own skeletons, and on them it is 31%, 38%, 31%. DougCube's stats are of another thing: the insertions DougCube found, of every kind, in solves searched from the ends ("if I need to do two insertions that are linked, the first one will be near the end of the skel or the start of the skel", [14 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1427774293495910593); "single 3c insertions are super quick when it's near the start or end of skel for me", [18 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1395640562861871221)). What both samples here do show is paulduc03's point ([9 Jul 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1524669961338097684)): the very first and very last spot are worse than the rest.

**C6. What an Insertion Finder "optimal" covers.**
2014chri04 ([16 Oct 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1296311051121463346)), on an 8-4 for a 23-move 3c: "IF verifies that this is optimal". tseitsei89 ([24 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1254714471423676456)), on two comms found by hand for a 21-move 5c: "IF says those are optimal insertions." Both are accurate reports of what Insertion Finder returned; the settings are not stated, and neither says the result is the best possible. 2014chri04 shows, in the same message, a 22 found by hand by rewriting a stretch of the finished solution ("5 moves shorter than the solution i originally found"), and tseitsei89 had written ([24 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1254712833237844018)) "there might be somethng even better". Searched here: on the first skeleton the 8-4 is the best 8-mover insertion (27) and one 10-move comm gives 23; on the second the two comms are the best pair of 8-movers (32) and algs of up to 10 moves give 30. So the word means optimal for the alg sets that were on (Baiqiang, [21 Aug 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1407986882700382259): "Pure 3 corners includes 8 moves comms only. The other one includes some 10 moves"). The first skeleton; both are written out on the examples page:

Scramble: `R' U' F U2 F2 D2 F2 L' B2 L D2 B2 L B2 R U' L' D' B D2 U' L R B' R' U' F`

Skeleton: `U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' L' D L D' B D B'` (23), leaves a corner 3-cycle: DBL → UBL → DFR → DBL

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

The solution 2014chri04 then found by hand, by rewriting a stretch of the finished one: `U' L2 B2 U' L F D' L2 D' F' D F2 B D B R' B' R D F' D B'` (22 moves, solves the scramble).

---

## D. What checked out

**Costs**

- **"a optimal 3c skeleton's insertion is 6 moves on average"** (Aneurin, [8 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1127188448462258266)), **"3c on average gives ~ +6"** (Eli Rogers, [9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414943185569845381)), **"3C insertions are usually +6 moves"** (Jay, [29 May 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1112910413688995890)): 5.90 at 20 moves.
- **"5c is 10-11 moves."** (Aneurin, [8 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1127188481563693068)), **"5c ~high 10"** (Phuwish, [4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239470932131973)): 10.65 at 16 moves, 10.37 at 20.
- **2tc "~8.0 I guess"** (Phuwish, [4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424237318960709642)): 8.05 at 16, 7.71 at 20.
- **"And isnt 3c1t and 2c2c close to 9.5?"** (tave_789, [4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239312396091486); Phuwish, [4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424239358826778798): "yeah"): 9.90 for a 3c1t, 8.73 to 9.13 for a 2c2c at 20 moves; 10.22 and 9.01 to 9.49 at 16. Close, with the 2c2c the lower one.
- **"getting +9 from 2tc is as bad as +11,+12 from 5c"** (Phuwish, [4 Oct 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1424238456275730556)): +9 or worse on 26% of 2tc skeletons, +12 or worse on 16% of 5c skeletons.
- **"you can usually do a bit better with 5c"** than 13 (Java, [1 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246425063641579541), to Zagros): the best is +13 or worse on only 1.3% of 20-move 5c skeletons.
- **"8-4 8-4 is soooooooo lucky tho"**, "for a 15 move skeleton" (alkamaass, [1 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246494760366112789), [1 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246494791827591292)): +8 or better on 4.3% of 14-move 5c skeletons and 5.4% of 16-move ones.

All of these are for 8-movers on random skeletons.

**Which skeleton**

- **A 5c "maybe like 5-6" shorter than a 3c** (asacuber, [5 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1247972799151341690), to Fanti): 5 is break-even (4.8 against a 20-move 3c by expected total, 4.0 to 5.1 for equal chance of a target).
- **The tutorial's "3 corners in 23 moves you will probably get it"** (sub-30) **and "25 moves long you will need some luck"**: 76% and 12%. And "4 corner in 18 moves is probably better than one leaving 3 corners in 25": expected 28.1 or less against 30.7.
- **"3c in 22-24 or 5c in 16-18"** (Gezza Cubing, [18 Aug 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1274622450046603284)), **"18 to anything like 5c, 4c, 3c1t, and 24 for 3c"** (oliynykmax, [18 Aug 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1274622638806925372)): fair pairs, with the two-comm skeleton the better half (sub-30 from a 5c in 18: 80%; from a 3c in 24: 34%).
- **21 to 3c: "not strictly guaranteed", "but it's very likely you're getting a 29 or better"** (kyh, [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443621022745235476), [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443621113996513372)): 99.6%. A 21-move 3c that does not give 29:

Scramble: `R' U' F L' D2 B2 L2 U2 B2 R' D2 U2 L2 U' F' R F2 D2 L2 D L B' U' R' U' F`

Skeleton: `B' D L' U2 L' U2 D2 R D B' U F R2 F B' U B' D' B2 U R2` (21), leaves a corner 3-cycle: DFL → UBR → UBL → DFL

**With 8-movers**: nothing: no spot has a case with an 8-move alg.

**Best with algs of up to 10 moves**: 30 in all, a 9-mover.

```
B' D L' U2 L' U2 D2 R D B' U F R2 F * B' U B' D' B2 U R2
* = U2 B' U' F2 U B U' F2 U' // (9-0/30)
Solution: B' D L' U2 L' U2 D2 R D B' U F R2 F U2 B' U' F2 U B U' F2 U' B' U B' D' B2 U R2 (30)
```

- **"the chance ur cancelling 4 moves or more is not that high"** (kyh, [9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414840422177570836)): 11% on a 24-move 3c.

**Searching**

- **"Why is there even a difference if the number of possible first insertions is the same tbh"** (wen, [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443790851443785758), asking, right after Jay's remark on the "2 insertion 4c types"). Read as about the two kinds of 2c2c: the number is the same, 24 first comms per spot for a pure and for a twisted 2c2c (jisu101's "you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions", [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125667565080657), [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125708480516218), times three ways to twist), and with two comms that do not touch the two cost the same, 9.41 and 9.40. The 0.40 between them comes from comms that interact: 0.24 of it from nesting (the best pair is nested on 24% of twisted 2c2c skeletons and 5.1% of pure ones), the other 0.16 from a second comm that cancels into the first without sitting inside it. Read as about a 2c2c against a 3c1t: the number is not the same, a 3c1t has 9 first comms per spot and a 5c 5.
- **Three spots on after a case that needs 10 moves: "I don't think that works."** (DougCube, [30 Dec 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1455657733272633651), to paulduc03's question, [30 Dec 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1455642235449114665)). It does not. After a spot whose case has no alg shorter than 10 moves, the spot two further on holds an 8-3 or better 1.7% of the time on a 20-move 3c. One where it is the only 8-3 of the skeleton:

Scramble: `R' U' F B' U2 B2 L2 F U2 F L2 U2 L2 R B2 F L D' B' U B L2 B' R' U' F`

Skeleton: `L' U' D B L' U' R D L D' R' L D' B2 U' B2 U2 B D' B'` (20), leaves a corner 3-cycle: DFR → UBR → UFR → DFR

**The best 8-mover insertion**: 25 in all, the only 8-3 in the skeleton, after move 10.

```
L' U' D B L' U' R D L D' * R' L D' B2 U' B2 U2 B D' B'
* = D' L U' L' D L U L' // (8-3/25)
Solution: L' U' D B L' U' R D L D2 L U' L' D L U R' D' B2 U' B2 U2 B D' B' (25)
```

Counting spots from 0. Checking every other spot from the start, spot 8 is the first whose case has no alg shorter than 10 moves (one of them: `U' R' B2 R F R' B2 R F' U`). Two spots on, at spot 10, is the 8-3. Going three on instead lands on spot 11, and the walk (spots 0, 2, 4, 6, 8, 11, 13, 15, 17, 19, 20) finds nothing better than an 8-1.

- **The ends of the skeleton are worse** (paulduc03, [9 Jul 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1524669961338097684)): an 8-3 or better at the first or last spot 1.1% of the time, at an inner spot 4.0% (20-move 3c, 8-movers).
- **"for the first 5c insertion you have 5x more options than for the second"** (Not officially a David, [21 Apr 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1098919767429099570)): five cycles per spot.
- **Nested comms on a 5c** (Gezza Cubing, [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253277699506704424); argonblue, on seeing Insertion Finder do it, [27 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1465819786910109828)): the best pair is nested on 24% of 20-move 5c skeletons with 8-movers. One:

Scramble: `R' U' F B2 R F2 L' B2 R D2 B2 D2 B2 D2 L2 F' U' R' B' L' D' R2 U' R' U' F`

Skeleton: `L' D' R F U' L2 U R2 F U' B D' L D F' D' B D' B2 R2` (20), leaves a corner 5-cycle: DBL → UBL → DBR → DFR → UFL → DBL

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

- **An insertion can cancel more than its own length** (Zagros, [17 Aug 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1406775061276524564); "true but highly unlikely", DougCube, [17 Aug 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1406775022168838214)): on 0.03% of 20-move 3c skeletons the best 8-mover makes the solution shorter than the skeleton. One:

Scramble: `R' U' F U' F D2 B' L2 R2 B L2 D2 U2 F D2 L R2 F2 R2 D R' F2 U' F2 U R' U' F`

Skeleton: `U2 B U' R D2 F2 L D R' B' L B R' D' L F B2 D' L D'` (20), leaves a corner 3-cycle: UBL → UFL → DFR → UBL

**The best 8-mover insertion**: 19 in all, 20 moves before, 19 after.

```
U2 B U' R D2 F2 L D R' B' L B R' * D' L F B2 D' L D'
* = R B' L' B R' B' L B // (8-9/19)
Solution: U2 B U' R D2 F2 L D R2 B' L B D' L F B2 D' L D' (19)
```

- **A 10-mover that is a setup to an 8-mover "wont cancel more than just inserting 8 movers"** (Ben, [25 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1465081370131959961)): right wherever the setup cancels a whole move, which is the 8-mover one spot over. The one exception found: on 86 of 20,000 random 20-move 3c skeletons a setup-type 10-mover is the only best, by one move, because its setup joins a turn of the skeleton. That is the 8-mover put inside that turn. One:

Scramble: `R' U' F L R U2 B2 U2 F2 R U2 L2 F2 D2 R F' U' B2 R' D2 B R U2 F' R' U' F`

Skeleton: `R' B' U' L' F' B' L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2` (20), leaves a corner 3-cycle: DBR → UBR → DFR → DBR

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

The 10-mover is the 8-mover `F R2 F' L2 F R2 F' L2` between `B'` and `B`. The same solution is that 8-mover put inside move 6 of the skeleton, the `B'` done in two parts: `B2`, the comm, `B`. No spot between two moves gives that with an 8-mover.

- **Suboptimal first comms can be needed** (kyh, [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486867754354086093); argonblue, [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486868609656688780)), and what Ben ([26 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1476514406320963629): "greedy 1 is still reasonable if your skeleton is really good") and kyh ([26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486867581557280848): "i think 1 is realistic") say of greedy 1: on a 20-move 5c the best first comm followed by the best second misses the best pair of 8-movers on 14% of skeletons; also following the first comms that are one move worse, on 3.7%. On average 10.54, 10.41 and 10.37. One where the best first comm is the wrong one:

Scramble: `R' U' F B2 L2 B2 U B2 D2 B2 U F2 R2 U' B2 R F U' B' R' U L F' L U' R' U' F`

Skeleton: `F2 U2 L' D' F' R D2 F U B U' F2 R2 L2 D' L F2 U' D' F'` (20), leaves a corner 5-cycle: DFL → UFR → UBL → UFL → UBR → DFL

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

- **More algs at greedy 0 can give a longer result** (bvcuber13, [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486828825756307620), [26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486829034905014303); Ben, [24 Sep 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1552577949688008734), [24 Sep 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1552578104134860882)), and tave_789's reason ([26 Mar 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1486829396286246952): "if 10-5 is the best first insertion it won’t find the optimals with a worse first insertion"): on 1,998 random 20-move 5c skeletons, the best first comm followed by the best second gives a longer result with every 3c alg of up to 10 moves than with 8-movers on 0.25%, and a shorter one on 9.3%. One of the longer ones:

Scramble: `R' U' F L2 B2 U2 B2 F2 D R2 U F2 D' L2 U' L U2 F' L' B2 D B' R2 D' L R' U' F`

Skeleton: `D2 L D' L2 B' U F' R F2 L' U' D B' L2 F' R2 B' U D' F` (20), leaves a corner 5-cycle: DBL → UBL → UBR → UFL → DFR → DBL

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

- **Insertion Finder "supposed that the status of the cube becomes better after any insertion. so it won't work in this case"** (Baiqiang, [5 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181804907922198529), on alkamaass's 8-10; and twenty minutes later, having asked Yan Xuan, [5 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181810401919381534): "this should be supported but somehow it doesn't"). This search has the same limit, and also stops at 29 on the 18-move skeleton. On the 16-move skeleton that the 8-10 leaves, Insertion Finder gives 25 and a comm plus an alg of up to 12 moves gives 24:

Scramble: `R' U' F U2 L2 F2 D' R2 B2 L2 D' F2 L U' L' F R' F2 R' F L2 U F R' U' F`

Skeleton: `D B2 D2 R2 D B L' D' R' L B' L F2 B2 L U` (16), leaves a twisted corner 3-cycle and one twisted corner: UBL → DFR → UBR → UBL, DBR twisted clockwise

**A comm plus an alg, each of up to 12 moves**: 24 in all.

```
D B2 D2 R2 ^ D B * L' D' R' L B' L F2 B2 L U
* = R U2 R' L' D' R L U2 R' L' D L // (12-7/21)
^ = R2 D2 B2 D' F D B2 D' F' D' R2 // (11-8/24)
Solution: F D B2 D' F' D' R2 D B R U2 R' L' D' R L U2 R2 B' L F2 B2 L U (24)
```

**Algs and counts**

- **Which leftovers take one, two or three comms**: the "3c - 1 comm", "3s1t, 2s2s, 5s, 3s3s, 2t, 3t - 2 comms" of Yurii Riabov's guide, everything else more; the tutorial's "This case requires three inserted commutators" for four twisted corners and its 5-corner cases; FakeMMAP ([9 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1459235380166525029)); DougCube's mixed 3c3c ([9 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1459256777555185872)); wen's four kinds of 7c ([29 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1134857937907613789), [29 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1134860037613957220), to torchlight's list, [29 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1134858381644025927)); 2c2c1t and 5c1t in three (Java, [12 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1128541440314707968); Renny, [9 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1459252311934111987)). All right, proved in Lean.
- **Two ways to do an 8-mover** (Gezza Cubing, [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253275920970551347), [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253278252026564668); rogo's "no" to eff's question, [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253302165154304010), [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253304211752484905), [20 Jun 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1253304286931062805)): 336 corner 3-cycles have two 8-movers, 192 have one (rogo's `[U2, R' D R]` is one of these), 480 have none.
- **"There arent 8 movers if they're oriented"** (Zagros, [26 Apr 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1365885825166082088)), answered by Jay's `R' F' R B2 R' F R B2` ([26 Apr 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1365886921221341216)): 32 of the 112 oriented 3-cycles have an 8-mover, so both have a point.
- **A case you can skip a spot after** (Srećko, [9 Sep 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1414947538515005494)): 112 of the 1,008 3-cycles have no 8-mover now and none after any one move.
- **"optimal to twist one corner while preserving all edges is 12 moves"** (torchlight, [27 Aug 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1145356913731715073)): right as stated. No sequence of 11 moves or fewer that keeps every edge leaves a corner twisted in its place, whatever else it does to the corners; 4,464 sequences of 12 moves do.
- **"the 6 move cases require eo on all axes"** (bpaul, [10 Feb 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1470815636128010393)): exactly. The 24 edge 3-cycles with a 6-mover are the 24 whose three edges are oriented on all three axes.
- **The shortest 2c2c alg is 10** (zakk drewji, [29 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1399740709698801775)): yes, `R2 U' L2 D B2 R2 D' L2 U F2` for one. A twisted 2c2c needs 12.
- **"10 moves is the minimum for any 2E2C without cancellations"** (Noah Swor, [15 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1394725607153209354)); **"every 10-move 2e2c is a cyclic shift of this alg or its inverse (up to rotations/mirrors ofc)"** (notkevin, [15 Jul 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1394776450522943659)); **1848 times 6 states** (argonblue, [9 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1536138775816704062), [9 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1536141220403748894)): all three exact. 960 ten-move algs, one class, 11,088 states.

---

## Docs referred to

- Sebastiano Tronto, [Fewest Moves Tutorial](https://fmcsolves.cubing.net/fmc_tutorial_ENG.pdf), version 3 (January 2020), revision 3.04 (August 2023).
- Yurii Riabov, [Hitchhiker’s Guide to FMC](https://docs.google.com/document/d/16nu10y1JkUmVDC11c1h_ULzAl4Vze7zR), March 2024.
- Cyprian Kalbarczyk, [Blockbuilding example solves](https://docs.google.com/document/d/1oWbbzc375q4FRIuzA5U091yaiGxt0zkFObGPe5P24_I).
- [Insertion Finder](https://333.fm/if): the site 333.fm is Baiqiang Dong's and the core was written by Yan Xuan (Baiqiang, [5 Dec 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1181810277851865108)).
