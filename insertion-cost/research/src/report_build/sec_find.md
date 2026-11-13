---

## 8. Finding them

So far it's been what the best insertion costs. This section is where it sits and what you lose by searching less, so it's the part you can use in an attempt: every other move, the ends, opposite-face pairs, how far to follow first comms. It's all random skeletons unless I say otherwise, and none of it measures time.

### 8.1 Where the best insertion sits

Where the best 3c insertion sits in the skeleton, by thirds. When several spots tie for the best, each gets an equal share.

**Where the best 3c insertion is, random skeletons, {= NSK('3c') =} per row. Lengths where the spots split evenly into three.**

{{one_thirds}}

Flat. And spot by spot on the 20-move skeletons, with 8-movers:

**3c, {= NSK('3c') =} random skeletons of 20 moves, 8-movers: each spot of the skeleton.**

{{one_positions}}

- **No third is better than another on a random skeleton.** DougCube ([[N6409]]): "In my stats, I found that the best insertion points tend to be in the first 1/3 or last 1/3 of the skel." And ([[N6410]]): "no idea why". Random move sequences don't show it. DougCube's stats are of the insertions they found in their own solves, of every kind, and two other messages say how they search: "if I need to do two insertions that are linked, the first one will be near the end of the skel or the start of the skel" ([[N4641]]) and "single 3c insertions are super quick when it's near the start or end of skel for me" ([[N3251]]). That's a different thing from where the best 8-mover for a 3c sits, which is what I count here. Section 9.4 has the real skeletons, DougCube's among them.
- **The two end spots are worse**, as paulduc03 says ([[N6411]]): "if you are too close to the beginning or to the end of the skeleton, you have less chances to find a 8-6 or better". Before the first move and after the last, an alg can only cancel on one side, so an 8-3 or better is there {= CELL('one_positions', 'before the first move', 'It is 8-3 or better') =} of the time against {= CELL('one_positions', 'after moves 3 to 17 (each)', 'It is 8-3 or better') =} at an inner spot. One move in from either end it is {= CELL('one_positions', 'after move 1', 'It is 8-3 or better') =}. From the second move in, every spot is as good as any other.
- **An 8-mover fits at about half the spots** ({= CELL('one_positions', 'after moves 3 to 17 (each)', 'An 8-mover fits there') =}), which is the {= ALGN('3c', 8) =} of {= STATES('3c') =} of section 5. Auric Cui's "if you get a 5c you only have 15 chances to find a commutator" on a 15-move skeleton ([[N136]]) is really 16 spots, as Not officially a David pointed out ([[N141]]), with five cycles to try at each.

### 8.2 How much cancels, and with which alg

**3c, the best insertion with 8-movers: how many moves it cancels. Random skeletons, {= NSK('3c') =} per row.**

{{one_cancel}}

- **8-2 is the usual best**, {= CELL('one_cancel', '20', '8-2') =} of 20-move skeletons, then 8-1 ({= CELL('one_cancel', '20', '8-1') =}) and 8-3 ({= CELL('one_cancel', '20', '8-3') =}).
- Gezza Cubing ([[N1388]]): "usually you should at least be able to cancel like 2 moves for each comm". For a 3c: {= GE('20', 2) =} of 20-move skeletons have an 8-2 or better.
- An 8-3 or better exists on {= GE('20', 3) =} of 20-move 3c skeletons and {= GE('30', 3) =} of 30-move ones. On a 5c the first comm has much better odds (8.4).
- kyh ([[N4186]]): "the chance ur cancelling 4 moves or more is not that high i think". {= GE('20', 4) =} at 20 moves, {= GE('26', 4) =} at 26.

**3c: when a longer alg is the best. Random skeletons, {= NSK('3c') =} per row. The first four columns split the skeletons by the shortest alg that gives the best insertion with algs of up to 10 moves, so they add up to 100%. The four means at the end are over the same skeletons, the ones where an 8-mover fits.**

{{one_longer}}

- **An 8-mover is as good as anything up to 10 moves on {= CELL('one_longer', '20', 'An 8-mover is as good as anything up to 10') =} of 20-move skeletons.**
- **A 9-mover is the best on {= CELL('one_longer', '20', 'A 9-mover beats every 8-mover and no 10-mover beats it') =}** at 20 moves, and on short skeletons mostly because no 8-mover fits at all. The tutorial: "It happens extremely rarely that the best insertion is given by a 9 move commutator (or longer)". For 9-movers that's right.
- **A 10-mover beats everything shorter on {= CELL('one_longer', '20', 'A 10-mover beats every 8- and 9-mover') =}**, about one skeleton in {= ONEIN('20', 'A 10-mover beats every 8- and 9-mover') =}, and an 11- or 12-mover beats everything up to 10 on {= CELL('one_longer', '20', 'An 11- or 12-mover beats everything up to 10') =}. So the tutorial's "(or longer)" is rare, not extremely rare (example [b] in section 10). notkevin's 15 to 3c ([[N2718]]), "optimal is 10-4 for a 21, 8-1 for a 22 using 8-movers only", is one of these.
- **But you don't gain much**: when a 10-mover wins it's by a single move {= CELL('one_longer', '20', 'When a 10-mover beats every 8- and 9-mover: by one move only') =} of the time, so on the skeletons where an 8-mover fits the mean only goes from {= CELL('one_longer', '20', 'Mean added on those skeletons, cap 8') =} to {= CELL('one_longer', '20', 'Same skeletons, cap 10: mean added') =} to {= CELL('one_longer', '20', 'Same skeletons, cap 12: mean added') =}.

**Setups around a regular comm.** Ben ([[N5510]]): "if its a setup to a regular comm then it wont cancel more than just inserting 8 movers". {= FACTN('ten_movers_conjugates') =} of the {= FACTN('ten_movers') =} ten-move algs are a setup move, an 8-mover and the setup undone. When the setup cancels a whole move of the skeleton, that's the same solution as the 8-mover one spot over, like Ben says. On the {= FACT('ten_wins') =} skeletons (of {= FACTN('ten_sample') =}) where a 10-mover beats everything shorter:

| Which algs are among the best | Skeletons |
|---|---:|
| a 10-mover of another kind | {= FACT('ten_wins') - FACT('ten_wins_only_conjugates') =} |
| only setup-type ones, each time by one move, with the setup joining a turn of the skeleton on its own face | {= FACT('ten_wins_only_conjugates') =} |

That second kind is the 8-mover put inside the turn (a `B'` done as `B2`, the comm, `B`), which no spot between two moves gives you. So Ben's rule holds on all but {= fmt(FACT('ten_wins_only_conjugates'), FACT('ten_sample')) =} of 20-move skeletons.

One of those {= FACT('ten_wins_only_conjugates') =}:

{{WIT_SETUP10}}

### 8.3 Checking every other move

alkamaass ([[N1142]], [[N1143]], [[N1144]]): "desperate with time check every other move", "but you have to check the ends", "this isn't thorough tho bc it can miss stuff like R (R blah blah B' ) B'". notkevin ([[N4772]]) on why it works: "(this is also why it's often recommended to check every other move when doing a lot of 2-insertion skeletons, bc if you're expecting at least a -3 somewhere, it has to cancel at least a full move, so checking every other still guarantees you'll find them)". The idea: an insertion that cancels a whole move against its neighbour also shows up one spot over, as a cyclic shift of the same alg.

Here's every second spot plus both ends, and every third spot plus both ends, against checking all of them, for one 8-move comm on a 3c:

**3c, 8-movers, random skeletons ({= NSK('3c') =} per length, each counted once for every way of starting the count). Only skeletons with an 8-mover somewhere are counted. *Mean loss* is how much longer the result is than with every spot checked; a set of spots that holds no 8-mover at all is scored as an 8-0.**

{{one_skip}}

**The same walks on the skeletons whose best is an 8-3 or better: how often each rule finds it, and, counted in walks, what every other move missed and where.**

{{one_skip_good}}

- **Every other move finds the best insertion {= CELL('one_skip', '20', 'Every other move finds the best') =} of the time** at 20 moves, and loses {= CELL('one_skip', '20', 'Every other move: mean loss, moves') =} of a move on average.
- **When the best is an 8-3 or better it's found {= CELL('one_skip_good', '20', 'Best is 8-3 or better: every other move finds it') =} of the time**, so "guarantees" is a little too strong as it stands. alkamaass had already said the rule isn't thorough, with a miss of another kind, one that notkevin's "at least a -3" leaves out. This one only joins the move on either side, so it cancels one move at each end (an 8-2, if it's an 8-mover):

  ```
  R (R blah blah B' ) B'   // alkamaass's example of what every other move can miss
  ```

  The misses of an 8-3 or better are different. Every one of them sits next to two moves on opposite faces (`R L`, `U D'`), {= SKIPNEAR(20) =} at 20 moves: there a full cancel reaches across the pair, and the alg moved over the move it cancels would go between the two moves of the pair, which takes writing the pair the other way round (example [c]). A footnote of the tutorial's 2.4.1 covers it: "when in a skeleton there are two consecutive parallel layers moves try swapping them too see if this gives better insertions". So check every other move, and both sides of a parallel pair. With that the rule is a guarantee for an 8-3 or better. (Of all the misses, the 8-2s and worse included, {= SKIPALL(20) =} are next to such a pair.)
- **What you miss is small**: when the best is 8-3 or better, the misses are 8-3s and a few 8-4s (fifth and sixth columns). Nothing better than an {= SKIPWORST() =} was missed on any of {= SKIPTOTAL() =} skeletons.
- notkevin's next line ([[N4773]]) is about two comms, which this table does not test: "(aka, the worst insertions you can miss with this without the second comm nesting is -4, where both comms only partially cancel on both sides)". Each of the two comms is a search of this kind, and the first comm alone is in the separate check below.
- **How many opposite-face pairs there are matters.** The skeletons of these tables write such a pair in one fixed order (`U D`, never `D U`; Appendix C), which puts one at about 1 neighbouring pair of moves in {= PAIR1IN('study_sample_3c_n20') =}. The {= PAIRN1('posted', 'skeletons') =} posted skeletons, as posted, have one at 1 in {= PAIR1IN('posted') =}.
- **Every third move doesn't work.** With a best of 8-3 or better, every third spot and both ends finds it only {= CELL('one_skip_good', '20', 'Best is 8-3 or better: every third move finds it') =} of the time.

{{EVERY_OTHER_CHECK}}

A skeleton where every other move misses the only 8-3:

{{WIT_SKIP}}

At spot {= SKS('spot') =} itself the same comm with one setup move, `{= SKS('alg') =}`, is a {= SKS('note') =} for the same {= SKS('total') =}. The miss is of 8-movers tried at the spot.

And one where every third spot misses it:

{{WIT_THIRD}}

**Three spots on after a 10-move case.** paulduc03 asked something narrower ([[N5145]]): "When I check between 2 moves in my 3C skeleton, sometimes it happens that the most optimal way to solve the 3C is 10 moves. In this case, can I go 3 moves further instead of 2 and still make sur not to miss any insertion below 6 moves ?" DougCube ([[N5147]]): "I don't think that works."

**3c, random skeletons, {= NSK('3c') =} per length. A spot *needs a 10-mover* when the shortest alg for the case at that spot has 10 moves; only spots with two more spots after them are counted. One row per skeleton length: how many such spots there are, and how often the next spot or the one after has an 8-3 or better.**

{{ten_skip}}

**The walks check every other spot and both ends for 8-movers, once starting at spot 0 and once at spot 1, on the skeletons whose best is an 8-3 or better. One row per skeleton length: how many walks miss that best, plain and when going three spots on, not two, after every spot that needs a 10-mover.**

{{ten_skip_walks}}

- **DougCube is right.** At 20 moves:

  | After a spot whose case needs a 10-mover, 20-move skeletons | Share | How many | Out of |
  |---|---:|---:|---:|
  | the spot two further on holds an 8-3 or better (spots) | {= TSP(20, 'two', 'ten') =} | {= TS(20, 'two') =} | {= TS(20, 'ten') =} |
  | the spot right after it holds one (spots) | {= TSP(20, 'next', 'ten') =} | {= TS(20, 'next') =} | {= TS(20, 'ten') =} |
  | walking a 20-move skeleton that way misses a best of 8-3 or better (walks) | {= TSP(20, 'rule_miss', 'walks') =} | {= TS(20, 'rule_miss') =} | {= TS(20, 'walks') =} |
  | plain every other move misses it (walks) | {= TSP(20, 'plain_miss', 'walks') =} | {= TS(20, 'plain_miss') =} | {= TS(20, 'walks') =} |

- **By cases, exactly.** {= FACT('ten_cases') =} of the {= STATES('3c') =} corner 3-cycles have a shortest alg of 10 moves.
  - One move on: for {= FACT('ten_cases_no8_after_one_move') =} of them no single move leads to a case with an 8-mover; for the other {= FACT('ten_cases_8_after_some_move') =}, {= FACT('ten_cases_moves_with_8')[0] =} of the 18 moves do.
  - Two moves on: every one of the {= FACT('ten_cases_8_after_some_two_moves') =} can be at a case with an 8-mover ({= f"{FACT('ten_cases_two_moves_pairs')[0]:,}" =} of the {= f"{FACT('ten_cases_two_moves_pairs')[1]:,}" =} combinations of a case and two moves).

  So a case that needs 10 moves tells you nothing safe about the spot two further on.

A skeleton where going three on misses the only 8-3:

{{WIT_TENSKIP}}

### 8.4 The first comm of a 5c

{{SEC_GREEDY}}
