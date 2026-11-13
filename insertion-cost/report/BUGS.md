# Insertions: corrections

*Goes with the write-up on insertion cost by skeleton type, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#non-dr-discussion, #fmc-discussion or #fmc-theory). Docs are listed with links at the end.

**What everything below is measured against:**

- **Every alg of 12 moves or fewer** for every corner-only and edge-only leftover that one or two 3-cycle insertions solve, and for 2c2e. Exhaustive, by joining all 6-move sequences with all 6-move sequences.
- **Which leftovers one, two or three 3-cycles can make**, counted over all corner states and proved in Lean.
- **The exact best insertion of a skeleton**: every spot, every alg within a cap on the alg's length, two comms allowed to nest. The caps are 8 (pure 8-movers; for edges the 6-, 7- and 8-movers), 10 and 12. Cap 8 on a 3c is the true best over all 8-movers at all spots of the skeleton as written (a pair of moves on opposite faces is not also tried the other way round; see the limits in the write-up).
- **Random skeletons**: random move sequences with a random leftover of the type, 20,000 per type and length at cap 8 (5,000 for 2tc, 2fe and the two kinds of 2e2e), fewer for two comms at cap 10 (200 to 2,000) and at cap 12 (100, at 20 moves only). They are not solves: no blocks, no EO. Two moves in a row on opposite faces are always written in one order (`U D`, never `D U`).
- **201 worked examples from real solves, 191 distinct skeletons**: 168 examples from the server and 33 from Cyprian Kalbarczyk's example solves, each replayed on a sticker-level cube before it was counted.

I replayed every scramble and solution below on that sticker-level cube.

Below is what was said in the channels that the numbers go against, each with an example. The docs I checked hold up, and so does most of what was said; that's in the write-up's section 10, the claims checked one by one.

---

## A. Said in the channels

**A1. "i think 3c1t > 2c2c > 5c. mostly because a twist gives you the most freedom to pick comms"** (argonblue, [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125544114131034)).
argonblue was answering jisu101's "if you can't find a 3c, what is generally better", "2c2c, 3c1t, or 5c?" ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125109978632212), [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125157483315321)). jisu101 replied right away ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125667565080657), [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125708480516218)): "True but so does 2c2c, you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions", which points the right way.
With 8-movers on 20-move random skeletons the order by cost is the order of the table below, cheapest first. So by cost a 2c2c is the cheaper leftover, by 0.77 to 1.17 over a 3c1t: 2c2c > 3c1t > 5c. The 5c last is as argonblue had it, and a twist does give more to pick from than a 5c: per spot, 9 first comms leave a 3c on a 3c1t against 5 on a 5c. A 2c2c has 24, which is jisu101's point. Longer algs keep the 2c2c ahead of the 3c1t.

So does searching the way it's done by hand, the best first comm and then the best second (5,000 skeletons per type, 20,000 for the 5c): twisted 2c2c 9.03, pure 2c2c 9.24, 3c1t 9.97, 5c 10.54. argonblue's next message ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125925066248303)) is about that search: "then again, you could end up with a massive cancellation for the first comm, and mediocre for the second one".

This is cost only. How long the comms take to find isn't measured, and argonblue had said of a 2c2c ([24 Jan 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1464804654054637590)): "there’s just so many choices for 2c2c insertions, and it’s hard for me to check them all". cpaul's estimates had the 2c2c ahead too ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760547458842644), [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760556908740648), [27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443760590995853465)): "I'd say more like 9 for pure 2-2", "and like 9.5 for 2-2 with a twist", "and like 10 for 3c1t".

Mean added on random skeletons, and what the posted skeletons give:

| Leftover | Random, 8-movers: mean added | Random, cap 10: mean added | Random, cap 12: mean added | Posted skeletons | Posted, 8-movers: mean added |
|---|---:|---:|---:|---:|---:|
| twisted 2c2c | 8.73 | 8.66 | 8.30 | 10 | 8.30 |
| pure 2c2c | 9.13 | 8.48 | 7.87 | 3 | 9.00 |
| 3c1t | 9.90 | 9.73 | 9.44 | 20 | 8.65 |
| 5c | 10.37 | 10.03 | 9.49 | 33 | 9.85 |

Cap 10 is 500 skeletons per type (2,000 for the 5c), cap 12 100 per type. At cap 12 the 3c1t and the 5c are too close to order on that many skeletons. The posted skeletons are too few to rank the 4-corner types, and of different lengths; they only agree that a 5c is the dearest.

A typical skeleton of each, 20 moves, 8-movers. Each costs its type's average, rounded. They're there to show what the averages look like on a cube; the order rests on the 20,000 skeletons per type, not on these three.

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

✓ Lean: the three blocks replay as printed, 29, 29 and 30 are the best that two comms of 8 moves or fewer give on these skeletons, nested or not, and the 24 and 9 first comms per spot hold for every 2c2c and every 3c1t. The means are sampled.

Jay ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443789835356606609)): "ime when i was doing blocks i didn't notice a meaningful different between 2 insertion 4c types other than 2c2c being easier practically with rNISS". That's what a one-move difference with a spread of more than a move looks like solve by solve, and the one difference Jay did name is on the 2c2c's side.

**A2. Checking every other move "still guarantees you'll find them"** (notkevin, [7 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1436457200880189582): "(this is also why it's often recommended to check every other move when doing a lot of 2-insertion skeletons, bc if you're expecting at least a -3 somewhere, it has to cancel at least a full move, so checking every other still guarantees you'll find them)").
Nearly, and it is a guarantee once opposite-face pairs are tried both ways round. The argument holds when the move that cancels whole is next to the alg: the same result is then one spot over. It fails when a move on the opposite face sits in between. The full cancel reaches across the pair, and the alg moved one move over would go between the two moves of the pair written the other way round, a spot the skeleton as written doesn't have. Tronto's tutorial has the habit that closes it, in a footnote of 2.4.1: "when in a skeleton there are two consecutive parallel layers moves try swapping them too see if this gives better insertions".

How often it bites, for one 8-move comm on random 3c skeletons of 20 moves: when the best insertion is an 8-3 or better, every second spot and both ends (the odd spots or the even ones, both counted) finds one that good 97% of the time. notkevin was talking about the comms of two-insertion skeletons. Each of them is a search of this kind; the two together are not tested. The misses all sit next to an opposite-face pair (every one, over seven skeleton lengths), and nothing better than an 8-4 was missed on any of 140,000 skeletons. The share goes with how many such pairs a skeleton has. These skeletons write a pair in one fixed order (`U D`, never `D U`), which puts one at about 1 neighbouring pair of moves in 11; the 191 posted skeletons have one at 1 in 14.

**A separate check, with its own list of 8-movers, its own random skeletons and its own search: one 8-move comm on 20-move skeletons, every second spot and both ends against every spot, on the skeletons whose best is an 8-3 or better. One row per kind of skeleton. A walk is one of the two ways of starting the count, and a miss is a walk that finds nothing as good as the best.**

| Skeletons | How many | Opposite-face pairs: one neighbouring pair of moves in | Walks | Walks that find an insertion as good as the best | Misses | Misses next to an opposite-face pair | Misses the same walk finds once a pair is written the other way round |
|---|---:|---:|---:|---:|---:|---|---|
| a 3c, pairs written in the fixed order | 20,000 | 11 | 11,906 | 97% | 340 | every one | every one |
| a 3c, a pair written either way round | 20,000 | 6 | 12,698 | 94% | 785 | every one | every one |
| the first comm of a 5c, pairs written in the fixed order | 10,000 | 11 | 16,102 | 98% | 247 | every one | every one |

The first row is the measurement above again and gives the same share. With a pair written either way round there are nearly twice as many pairs, and the share of walks that miss about doubles. The first comm of a 5c, the search notkevin was talking about, is missed about half as often as the comm of a 3c. In all three, every miss is next to an opposite-face pair, and the same walk finds it once one such pair of the skeleton is written the other way round.

alkamaass's caveat when suggesting the rule for when time is short ([31 May 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246266143551787058)), "this isn't thorough tho bc it can miss stuff like R (R blah blah B' ) B'", is the other kind of miss: a half cancel at each end, an 8-2 if it's an 8-mover. notkevin's "at least a -3" leaves it out and notkevin's next line allows for it ([7 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1436457482577907792)): "(aka, the worst insertions you can miss with this without the second comm nesting is -4, where both comms only partially cancel on both sides)".

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

At spot 15 itself the same comm with one setup move, `B F D F' U F D' F' U' B'`, is a 10-5 for the same 25. The miss is of 8-movers tried at the spot.

✓ Lean: the block replays; over every 8-mover at every spot the best is 25, at spot 16 only and by one alg only; the odd spots, the ends and spot 14 give at best an 8-1; with the pair written `B F'` the moved alg gives 25 between the two. The shares and the 140,000 skeletons are computed, and so is the separate check; the 10-5 is replayed on the sticker-level cube.

---

## Docs referred to

- Sebastiano Tronto, [Fewest Moves Tutorial](https://fmcsolves.cubing.net/fmc_tutorial_ENG.pdf), version 3 (January 2020), revision 3.04 (August 2023): section 2.4 on insertions.
- Cyprian Kalbarczyk, [Blockbuilding example solves](https://docs.google.com/document/d/1oWbbzc375q4FRIuzA5U091yaiGxt0zkFObGPe5P24_I).
