# Insertions: corrections

*Goes with the write-up on insertion cost by skeleton type, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#non-dr-discussion, #fmc-discussion or #fmc-theory). Docs are listed with links at the end.

**What everything below is measured against:**

- **Every alg of 12 moves or fewer** for every corner-only and edge-only leftover that one or two 3-cycle insertions solve, and for 2c2e. Exhaustive, by joining all 6-move sequences with all 6-move sequences.
- **Which leftovers one, two or three 3-cycles can make**, counted over all corner states and proved in Lean.
- **The exact best insertion of a skeleton**: every spot, every alg within a cap on the alg's length, two comms allowed to nest. The caps are 8 (pure 8-movers; for edges the 6-, 7- and 8-movers), 10 and 12. Cap 8 on a 3c is the true best over all 8-movers at all spots.
- **Random skeletons**: random move sequences with a random leftover of the type, 20,000 per type and length at cap 8 (5,000 for 2tc, 2fe and the two kinds of 2e2e), fewer for two comms at cap 10 (200 to 2,000) and at cap 12 (100, at 20 moves only). They are not solves: no blocks, no EO.
- **201 worked examples from real solves, 191 distinct skeletons**: 168 examples from the server and 33 from Cyprian Kalbarczyk's example solves, each replayed on a sticker-level cube before it was counted.

I replayed every scramble and solution below on that sticker-level cube.

Below is what was said in the channels that the numbers go against, each with an example. The docs I checked hold up, and so does most of what was said; that's in the write-up's section 10, the claims checked one by one.

---

## A. Said in the channels

**A1. "i think 3c1t > 2c2c > 5c. mostly because a twist gives you the most freedom to pick comms"** (argonblue, [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125544114131034)).
argonblue was answering jisu101's "if you can't find a 3c, what is generally better", "2c2c, 3c1t, or 5c?" ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125109978632212), [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125157483315321)). jisu101 replied right away ([1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125667565080657), [1 Aug 2026](https://discord.com/channels/1007840975726575667/1077216728683135046/1533125708480516218)): "True but so does 2c2c, you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions", which points the right way.
With 8-movers on 20-move random skeletons the order by cost is the order of the table below, cheapest first. So a 2c2c is the cheaper leftover, by 0.77 to 1.17 over a 3c1t: 2c2c > 3c1t > 5c. Counted per spot, a 2c2c has 24 first comms that leave a 3c and a 3c1t has 9, which is jisu101's point. Longer algs keep the 2c2c ahead of the 3c1t. Mean added on random skeletons, and what the posted skeletons give:

| Leftover | Random, 8-movers: mean added | Random, cap 10: mean added | Random, cap 12: mean added | Posted skeletons | Posted, 8-movers: mean added |
|---|---:|---:|---:|---:|---:|
| twisted 2c2c | 8.73 | 8.66 | 8.30 | 10 | 8.30 |
| pure 2c2c | 9.13 | 8.48 | 7.87 | 3 | 9.00 |
| 3c1t | 9.90 | 9.73 | 9.44 | 20 | 8.65 |
| 5c | 10.37 | | 9.49 | 33 | 9.85 |

Cap 10 is 500 skeletons per type, cap 12 100 per type. At cap 12 the 3c1t and the 5c are too close to order on that many skeletons. The posted skeletons are too few to rank the 4-corner types, and of different lengths; they only agree that a 5c is the dearest.

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

Jay's "i didn't notice a meaningful different between 2 insertion 4c types" ([27 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1443789835356606609)) is what a one-move difference with a spread of more than a move looks like solve by solve.

**A2. Checking every other move "still guarantees you'll find them"** (notkevin, [7 Nov 2025](https://discord.com/channels/1007840975726575667/1077216728683135046/1436457200880189582): "if you're expecting at least a -3 somewhere, it has to cancel at least a full move, so checking every other still guarantees you'll find them").
Nearly. On random 3c skeletons of 20 moves, when the best 8-mover insertion is an 8-3 or better, checking every second spot and both ends (the odd spots or the even ones, both counted) finds an insertion that good 97% of the time. All of those misses (every one over seven skeleton lengths) are next to two moves on opposite faces, where the full cancel reaches across the pair and the shifted alg lands two spots away. Nothing better than an 8-4 was missed on any of 140,000 skeletons. alkamaass had said the rule is not thorough when recommending it ([31 May 2024](https://discord.com/channels/1007840975726575667/1077216728683135046/1246266143551787058)): "this isn't thorough tho bc it can miss stuff like R (R blah blah B' ) B'". Example:

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

Counting spots from 0 (before the first move), the 8-3 is at spot 16. Checking the odd spots (1, 3, 5, 7, 9, 11, 13, 15, 17, 19) and both ends finds nothing better than an 8-1; the even spots would find it. The spot is right after the pair `F' B`.

**A3. "sub-22 for 3C skeleton", "sub-20 for every other skeleton"** for sub-30 (sequesteredcuber, [8 Jul 2023](https://discord.com/channels/1007840975726575667/1077216728683135046/1127188954995769364)).
Two moves apart is too close. With 8-movers on random skeletons:

| Skeleton | Chance of sub-30 |
|---|---:|
| 3c in 21 | 99.6% |
| 5c in 19 | 48% |
| 3c1t in 19 | 63% |

For the same expected total as a 20-move 3c, a 5c has to be 4.8 moves shorter, a 3c1t 4.4, a pure 2c2c 3.5 (write-up, section 7). Here's a 19-move 5c with the most common outcome, 30:

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

---

## Docs referred to

- Cyprian Kalbarczyk, [Blockbuilding example solves](https://docs.google.com/document/d/1oWbbzc375q4FRIuzA5U091yaiGxt0zkFObGPe5P24_I).
