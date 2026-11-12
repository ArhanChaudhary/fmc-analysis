# Insertions: corrections

*Goes with the write-up on insertion cost by skeleton type, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#non-dr-discussion, #fmc-discussion or #fmc-theory). Docs are listed with links at the end.

**What everything below is measured against:**

- **Every alg of 12 moves or fewer** for every corner-only and edge-only leftover that one or two 3-cycle insertions solve, and for 2c2e. Exhaustive, by joining all 6-move sequences with all 6-move sequences.
- **Which leftovers one, two or three 3-cycles can make**, counted over all corner states and proved in Lean.
- **The exact best insertion of a skeleton**: every spot, every alg within a cap on the alg's length, two comms allowed to nest. The caps are 8 (pure 8-movers; for edges the 6-, 7- and 8-movers), 10 and 12. Cap 8 on a 3c is the true best over all 8-movers at all spots.
- **Random skeletons**: random move sequences with a random leftover of the type, 20,000 per type and length at cap 8 (5,000 for 2tc, 2fe and the two kinds of 2e2e), fewer for two comms at cap 10 (200 to 2,000) and at cap 12 (100, at 20 moves only). They are not solves: no blocks, no EO.
- **{= RL('covered') =} worked examples from real solves, {= RL('skeletons') =} distinct skeletons**: {= RL('server') =} examples from the server and {= RL('kalbarczyk') =} from Cyprian Kalbarczyk's example solves, each replayed on a sticker-level cube before it was counted.

Every scramble and solution printed below was replayed on that sticker-level cube.

Below is what was said in the channels that the numbers go against, each with an example. The docs this study checks hold up, and so does most of what was said; that is in the write-up's section 10, the claims checked one by one.

---

## A. Said in the channels

**A1. "i think 3c1t > 2c2c > 5c. mostly because a twist gives you the most freedom to pick comms"** (argonblue, [[N6507]]).
argonblue was answering jisu101's "if you can't find a 3c, what is generally better", "2c2c, 3c1t, or 5c?" ([[N6504]], [[N6505]]). jisu101 replied right away ([[N6508]], [[N6509]]): "True but so does 2c2c, you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions", which points the right way.
With 8-movers on 20-move random skeletons the order by cost is twisted 2c2c ({= M('2c2c-twisted') =}), pure 2c2c ({= M('2c2c-pure') =}), 3c1t ({= M('3c1t') =}), 5c ({= M('5c') =}). So a 2c2c is the cheaper leftover, by {= DIFF('3c1t', '2c2c-pure') =} to {= DIFF('3c1t', '2c2c-twisted') =} over a 3c1t: 2c2c > 3c1t > 5c. Counted per spot, a 2c2c has {= FC('2c2c-pure') =} first comms that leave a 3c and a 3c1t has {= FC('3c1t') =}, which is jisu101's point. Longer algs keep the 2c2c ahead of the 3c1t: at cap 10 a pure 2c2c averages {= M('2c2c-pure', L=10) =} and a twisted one {= M('2c2c-twisted', L=10) =}, against {= M('3c1t', L=10) =} ({= NSK('3c1t', L=10) =} skeletons per type), and at cap 12 {= M('2c2c-pure', L=12, src='two12') =} and {= M('2c2c-twisted', L=12, src='two12') =} against {= M('3c1t', L=12, src='two12') =} ({= NSK('3c1t', L=12, src='two12') =} per type). At cap 12 the 3c1t and the 5c ({= M('5c', L=12, src='two12') =}) are too close to order on that many skeletons. The posted skeletons are too few to rank the 4-corner types ({= POSTED('2c2c-pure') =} pure 2c2c, {= POSTED('2c2c-twisted') =} twisted, {= POSTED('3c1t') =} 3c1t, of different lengths); they only agree that a 5c is the dearest ({= POSTEDM('5c') =} on {= POSTED('5c') =} skeletons, against {= POSTEDM('2c2c-pure') =}, {= POSTEDM('2c2c-twisted') =} and {= POSTEDM('3c1t') =}).

A typical skeleton of each, 20 moves, 8-movers. Each costs its type's average, rounded: they show what the averages look like on a cube, and the order rests on the 20,000 skeletons per type, not on these three.

{{WIT_TYPICAL_2C2C_TWISTED}}

{{WIT_TYPICAL_2C2C_PURE}}

{{WIT_TYPICAL_3C1T}}

Jay's "i didn't notice a meaningful different between 2 insertion 4c types" ([[N4860]]) is what a one-move difference with a spread of more than a move looks like solve by solve.

**A2. Checking every other move "still guarantees you'll find them"** (notkevin, [[N4772]]: "if you're expecting at least a -3 somewhere, it has to cancel at least a full move, so checking every other still guarantees you'll find them").
Nearly. On random 3c skeletons of 20 moves, when the best 8-mover insertion is an 8-3 or better, checking every second spot and both ends (the odd spots or the even ones, both counted) finds an insertion that good {= CELL('one_skip', '20', 'Best is 8-3 or better: every other move finds it') =} of the time. All of those misses ({= SKIPNEAR() =} over seven skeleton lengths) are next to two moves on opposite faces, where the full cancel reaches across the pair and the shifted alg lands two spots away. Nothing better than an {= SKIPWORST() =} was missed on any of {= SKIPTOTAL() =} skeletons. alkamaass had said the rule is not thorough when recommending it ([[N1144]]): "this isn't thorough tho bc it can miss stuff like R (R blah blah B' ) B'". Example:

{{WIT_SKIP}}

**A3. "sub-22 for 3C skeleton", "sub-20 for every other skeleton"** for sub-30 (sequesteredcuber, [[N292]]).
Two moves apart is too close. With 8-movers on random skeletons a 3c in 21 gives sub-30 {= CH('3c', 21, 29) =} of the time; a 5c in 19 gives it {= CH('5c', 19, 29) =}, a 3c1t in 19 {= CH('3c1t', 19, 29) =}. For the same expected total as a 20-move 3c, a 5c has to be {= EXM('5c', 20) =} moves shorter, a 3c1t {= EXM('3c1t', 20) =}, a pure 2c2c {= EXM('2c2c-pure', 20) =} (write-up, section 7). A 19-move 5c with the most common outcome, 30:

{{WIT_FIVEC19}}

---

## Docs referred to

- Cyprian Kalbarczyk, [Blockbuilding example solves](https://docs.google.com/document/d/1oWbbzc375q4FRIuzA5U091yaiGxt0zkFObGPe5P24_I).
