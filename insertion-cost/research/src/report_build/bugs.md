# Insertions: corrections

*Goes with the write-up on insertion cost by skeleton type, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#non-dr-discussion, #fmc-discussion or #fmc-theory). Docs are listed with links at the end.

**What everything below is measured against:**

- **Every alg of 12 moves or fewer** for every corner-only and edge-only leftover that one or two 3-cycle insertions solve, and for 2c2e. Exhaustive, by joining all 6-move sequences with all 6-move sequences.
- **Which leftovers one, two or three 3-cycles can make**, counted over all corner states and proved in Lean.
- **The exact best insertion of a skeleton**: every spot, every alg within a cap on the alg's length, two comms allowed to nest. The caps are 8 (pure 8-movers; for edges the 6-, 7- and 8-movers), 10 and 12. Cap 8 on a 3c is the true best over all 8-movers at all spots of the skeleton as written (a pair of moves on opposite faces is not also tried the other way round; see the limits in the write-up).
- **Random skeletons**: random move sequences with a random leftover of the type, {= NSK('5c') =} per type and length at cap 8 ({= NSK('2tc') =} for 2tc, 2fe and the two kinds of 2e2e), fewer for two comms at cap 10 ({= NSK('2tc', L=10) =} to {= NSK('5c', L=10) =}) and at cap 12 ({= NSK('3c1t', L=12, src='two12') =}, at 20 moves only). They are not solves: no blocks, no EO. Two moves in a row on opposite faces are always written in one order (`U D`, never `D U`).
- **{= RL('covered') =} worked examples from real solves, {= RL('skeletons') =} distinct skeletons**: {= RL('server') =} examples from the server and {= RL('kalbarczyk') =} from Cyprian Kalbarczyk's example solves, each replayed on a sticker-level cube before it was counted.

I replayed every scramble and solution below on that sticker-level cube.

Below is what was said in the channels that the numbers go against, each with an example. The docs I checked hold up, and so does most of what was said; that's in the write-up's section 10, the claims checked one by one.

---

## A. Said in the channels

**A1. "i think 3c1t > 2c2c > 5c. mostly because a twist gives you the most freedom to pick comms"** (argonblue, [[N6507]]).
argonblue was answering jisu101's "if you can't find a 3c, what is generally better", "2c2c, 3c1t, or 5c?" ([[N6504]], [[N6505]]). jisu101 replied right away ([[N6508]], [[N6509]]): "True but so does 2c2c, you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions", which points the right way.
With 8-movers on 20-move random skeletons the order by cost is the order of the table below, cheapest first. So by cost a 2c2c is the cheaper leftover, by {= DIFF('3c1t', '2c2c-pure') =} to {= DIFF('3c1t', '2c2c-twisted') =} over a 3c1t: 2c2c > 3c1t > 5c. The 5c last is as argonblue had it, and a twist does give more to pick from than a 5c: per spot, {= FC('3c1t') =} first comms leave a 3c on a 3c1t against {= FC('5c') =} on a 5c. A 2c2c has {= FC('2c2c-pure') =}, which is jisu101's point. Longer algs keep the 2c2c ahead of the 3c1t.

So does searching the way it's done by hand, the best first comm and then the best second ({= GN('3c1t') =} skeletons per type, {= GN('5c') =} for the 5c): twisted 2c2c {= CELL('greedy', 'twisted 2c2c', 'Best first comm only: mean added') =}, pure 2c2c {= CELL('greedy', 'pure 2c2c', 'Best first comm only: mean added') =}, 3c1t {= CELL('greedy', '3c1t', 'Best first comm only: mean added') =}, 5c {= CELL('greedy', '5c', 'Best first comm only: mean added') =}. argonblue's next message ([[N6510]]) is about that search: "then again, you could end up with a massive cancellation for the first comm, and mediocre for the second one".

This is cost only. How long the comms take to find isn't measured, and argonblue had said of a 2c2c ([[N5507]]): "there’s just so many choices for 2c2c insertions, and it’s hard for me to check them all". cpaul's estimates had the 2c2c ahead too ([[N4857]], [[N4858]], [[N4859]]): "I'd say more like 9 for pure 2-2", "and like 9.5 for 2-2 with a twist", "and like 10 for 3c1t".

Mean added on random skeletons, and what the posted skeletons give:

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

Jay ([[N4860]]): "ime when i was doing blocks i didn't notice a meaningful different between 2 insertion 4c types other than 2c2c being easier practically with rNISS". That's what a one-move difference with a spread of more than a move looks like solve by solve, and the one difference Jay did name is on the 2c2c's side.

**A2. Checking every other move "still guarantees you'll find them"** (notkevin, [[N4772]]: "(this is also why it's often recommended to check every other move when doing a lot of 2-insertion skeletons, bc if you're expecting at least a -3 somewhere, it has to cancel at least a full move, so checking every other still guarantees you'll find them)").
Nearly, and it is a guarantee once opposite-face pairs are tried both ways round. The argument holds when the move that cancels whole is next to the alg: the same result is then one spot over. It fails when a move on the opposite face sits in between. The full cancel reaches across the pair, and the alg moved one move over would go between the two moves of the pair written the other way round, a spot the skeleton as written doesn't have. Tronto's tutorial has the habit that closes it, in a footnote of 2.4.1: "when in a skeleton there are two consecutive parallel layers moves try swapping them too see if this gives better insertions".

How often it bites, for one 8-move comm on random 3c skeletons of 20 moves: when the best insertion is an 8-3 or better, every second spot and both ends (the odd spots or the even ones, both counted) finds one that good {= CELL('one_skip_good', '20', 'Best is 8-3 or better: every other move finds it') =} of the time. notkevin was talking about the comms of two-insertion skeletons. Each of them is a search of this kind; the two together are not tested. The misses all sit next to an opposite-face pair ({= SKIPNEAR() =}, over seven skeleton lengths), and nothing better than an {= SKIPWORST() =} was missed on any of {= SKIPTOTAL() =} skeletons. The share goes with how many such pairs a skeleton has. These skeletons write a pair in one fixed order (`U D`, never `D U`), which puts one at about 1 neighbouring pair of moves in {= PAIR1IN('study_sample_3c_n20') =}; the {= PAIRN1('posted', 'skeletons') =} posted skeletons have one at 1 in {= PAIR1IN('posted') =}.

{{EVERY_OTHER_CHECK}}

alkamaass's caveat when recommending the rule ([[N1144]]), "this isn't thorough tho bc it can miss stuff like R (R blah blah B' ) B'", is the other kind of miss: a half cancel at each end, an 8-2 if it's an 8-mover. notkevin's "at least a -3" leaves it out and notkevin's next line allows for it ([[N4773]]): "(aka, the worst insertions you can miss with this without the second comm nesting is -4, where both comms only partially cancel on both sides)".

A skeleton where every other move misses the only 8-3:

{{WIT_SKIP}}

At spot {= SKS('spot') =} itself the same comm with one setup move, `{= SKS('alg') =}`, is a {= SKS('note') =} for the same {= SKS('total') =}. The miss is of 8-movers tried at the spot.

✓ Lean: the block replays; over every 8-mover at every spot the best is 25, at spot 16 only and by one alg only; the odd spots, the ends and spot 14 give at best an 8-1; with the pair written `B F'` the moved alg gives 25 between the two. The shares and the {= SKIPTOTAL() =} skeletons are computed, and so is the separate check; the {= SKS('note') =} is replayed on the sticker-level cube.

---

## Docs referred to

- Sebastiano Tronto, [Fewest Moves Tutorial](https://fmcsolves.cubing.net/fmc_tutorial_ENG.pdf), version 3 (January 2020), revision 3.04 (August 2023): section 2.4 on insertions.
- Cyprian Kalbarczyk, [Blockbuilding example solves](https://docs.google.com/document/d/1oWbbzc375q4FRIuzA5U091yaiGxt0zkFObGPe5P24_I).
