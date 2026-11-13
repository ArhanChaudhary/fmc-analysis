# Insertions: corrections

*Goes with the write-up on insertion cost by skeleton type, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#non-dr-discussion, #fmc-discussion or #fmc-theory). Docs are listed with links at the end.

**What everything below is measured against:**

- **Every alg of 12 moves or fewer** for every corner-only and edge-only leftover that one or two 3-cycle insertions solve, and for 2c2e. Exhaustive, by joining all 6-move sequences with all 6-move sequences.
- **Which leftovers one, two or three 3-cycles can make**, counted over all corner states and proved in Lean.
- **The exact best insertion of a skeleton**: every spot, every alg within a cap on the alg's length, two comms allowed to nest. The caps are 8 (pure 8-movers; for edges the 6-, 7- and 8-movers), 10 and 12. Cap 8 on a 3c is the true best over all 8-movers at all spots of the skeleton as written (a pair of moves on opposite faces is not also tried the other way round; see the limits in the write-up).
- **Random skeletons**: random move sequences with a random leftover of the type, {= NSK('5c') =} per type and length at cap 8 ({= NSK('2tc') =} for 2tc, 2fe and the two kinds of 2e2e), fewer for two comms at cap 10 ({= NSK('2tc', L=10) =} to {= NSK('5c', L=10) =}) and at cap 12 ({= NSK('3c1t', L=12, src='two12') =}, at 20 moves only). They are not solves: no blocks, no EO.
- **{= RL('covered') =} worked examples from real solves, {= RL('skeletons') =} distinct skeletons**: {= RL('server') =} examples from the server and {= RL('kalbarczyk') =} from Cyprian Kalbarczyk's example solves, each replayed on a sticker-level cube before it was counted.

I replayed every scramble and solution below on that sticker-level cube.

Below is what was said in the channels that the numbers go against, each with an example. The docs I checked hold up, and so does most of what was said; that's in the write-up's section 10, the claims checked one by one.

---

## A. Said in the channels

**A1. "i think 3c1t > 2c2c > 5c. mostly because a twist gives you the most freedom to pick comms"** (argonblue, [[N6507]]).
argonblue was answering jisu101's "if you can't find a 3c, what is generally better", "2c2c, 3c1t, or 5c?" ([[N6504]], [[N6505]]). jisu101 replied right away ([[N6508]], [[N6509]]): "True but so does 2c2c, you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions", which points the right way.
With 8-movers on 20-move random skeletons the order by cost is the order of the table below, cheapest first. So a 2c2c is the cheaper leftover, by {= DIFF('3c1t', '2c2c-pure') =} to {= DIFF('3c1t', '2c2c-twisted') =} over a 3c1t: 2c2c > 3c1t > 5c. Counted per spot, a 2c2c has {= FC('2c2c-pure') =} first comms that leave a 3c and a 3c1t has {= FC('3c1t') =}, which is jisu101's point. Longer algs keep the 2c2c ahead of the 3c1t. Mean added on random skeletons, and what the posted skeletons give:

| Leftover | Random, 8-movers: mean added | Random, cap 10: mean added | Random, cap 12: mean added | Posted skeletons | Posted, 8-movers: mean added |
|---|---:|---:|---:|---:|---:|
| twisted 2c2c | {= M('2c2c-twisted') =} | {= M('2c2c-twisted', L=10) =} | {= M('2c2c-twisted', L=12, src='two12') =} | {= POSTED('2c2c-twisted') =} | {= POSTEDM('2c2c-twisted') =} |
| pure 2c2c | {= M('2c2c-pure') =} | {= M('2c2c-pure', L=10) =} | {= M('2c2c-pure', L=12, src='two12') =} | {= POSTED('2c2c-pure') =} | {= POSTEDM('2c2c-pure') =} |
| 3c1t | {= M('3c1t') =} | {= M('3c1t', L=10) =} | {= M('3c1t', L=12, src='two12') =} | {= POSTED('3c1t') =} | {= POSTEDM('3c1t') =} |
| 5c | {= M('5c') =} | {= M('5c', L=10) =} | {= M('5c', L=12, src='two12') =} | {= POSTED('5c') =} | {= POSTEDM('5c') =} |

Cap 10 is {= NSK('3c1t', L=10) =} skeletons per type ({= NSK('5c', L=10) =} for the 5c), cap 12 {= NSK('3c1t', L=12, src='two12') =} per type. At cap 12 the 3c1t and the 5c are too close to order on that many skeletons. The posted skeletons are too few to rank the 4-corner types, and of different lengths; they only agree that a 5c is the dearest.

A typical skeleton of each, 20 moves, 8-movers. Each costs its type's average, rounded. They're there to show what the averages look like on a cube; the order rests on the {= NSK('5c') =} skeletons per type, not on these three.

{{WIT_TYPICAL_2C2C_TWISTED}}

{{WIT_TYPICAL_2C2C_PURE}}

{{WIT_TYPICAL_3C1T}}

✓ Lean: the three blocks replay as printed, 29, 29 and 30 are the best that two comms of 8 moves or fewer give on these skeletons, nested or not, and the {= FC('2c2c-pure') =} and {= FC('3c1t') =} first comms per spot hold for every 2c2c and every 3c1t. The means are sampled.

Jay's "i didn't notice a meaningful different between 2 insertion 4c types" ([[N4860]]) is what a one-move difference with a spread of more than a move looks like solve by solve.

**A2. Checking every other move "still guarantees you'll find them"** (notkevin, [[N4772]]: "if you're expecting at least a -3 somewhere, it has to cancel at least a full move, so checking every other still guarantees you'll find them").
Nearly. On random 3c skeletons of 20 moves, when the best 8-mover insertion is an 8-3 or better, checking every second spot and both ends (the odd spots or the even ones, both counted) finds an insertion that good {= CELL('one_skip_good', '20', 'Best is 8-3 or better: every other move finds it') =} of the time. All of those misses ({= SKIPNEAR() =} over seven skeleton lengths) are next to two moves on opposite faces, where the full cancel reaches across the pair and the alg moved one move over would go between the two moves of the pair, swapped. Nothing better than an {= SKIPWORST() =} was missed on any of {= SKIPTOTAL() =} skeletons. alkamaass had said the rule is not thorough when recommending it ([[N1144]]): "this isn't thorough tho bc it can miss stuff like R (R blah blah B' ) B'". Example:

{{WIT_SKIP}}

✓ Lean: the block replays; over every 8-mover at every spot the best is 25, at spot 16 only and by one alg only; the odd spots, the ends and spot 14 give at best an 8-1; with the pair written `B F'` the moved alg gives 25 between the two. The shares and the {= SKIPTOTAL() =} skeletons are computed.

**A3. "sub-22 for 3C skeleton", "sub-20 for every other skeleton"** for sub-30 (sequesteredcuber, [[N292]]).
Two moves apart is too close. With 8-movers on random skeletons:

| Skeleton | Chance of sub-30 |
|---|---:|
| 3c in 21 | {= CH('3c', 21, 29) =} |
| 5c in 19 | {= CH('5c', 19, 29) =} |
| 3c1t in 19 | {= CH('3c1t', 19, 29) =} |

For the same expected total as a 20-move 3c, a 5c has to be {= EXM('5c', 20) =} moves shorter, a 3c1t {= EXM('3c1t', 20) =}, a pure 2c2c {= EXM('2c2c-pure', 20) =} (write-up, section 7). Here's a 19-move 5c with the most common outcome, 30:

{{WIT_FIVEC19}}

✓ Lean: the block replays and 30 is the best that two comms of 8 moves or fewer give on it. The chances and the rates are sampled.

---

## Docs referred to

- Cyprian Kalbarczyk, [Blockbuilding example solves](https://docs.google.com/document/d/1oWbbzc375q4FRIuzA5U091yaiGxt0zkFObGPe5P24_I).
