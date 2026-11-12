# Insertions: corrections, and what the numbers settle

*Goes with the write-up on insertion cost by skeleton type, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#non-dr-discussion, #fmc-discussion or #fmc-theory). Docs are listed with links at the end.

**What everything below is measured against:**

- **Every alg of 12 moves or fewer** for every corner-only and edge-only leftover that one or two 3-cycle insertions solve, and for 2c2e. Exhaustive, by joining all 6-move sequences with all 6-move sequences.
- **Which leftovers one, two or three 3-cycles can make**, counted over all corner states and proved in Lean.
- **The exact best insertion of a skeleton**: every spot, every alg within a cap on the alg's length, two comms allowed to nest. The caps are 8 (pure 8-movers; for edges the 6-, 7- and 8-movers), 10 and 12. Cap 8 on a 3c is the true best over all 8-movers at all spots.
- **Random skeletons**: random move sequences with a random leftover of the type, 20,000 per type and length at cap 8 (5,000 for 2tc, 2fe and the two kinds of 2e2e), fewer for two comms at cap 10 (200 to 2,000) and at cap 12 (100, at 20 moves only). They are not solves: no blocks, no EO.
- **{= RL('covered') =} worked examples from real solves, {= RL('skeletons') =} distinct skeletons**: {= RL('server') =} examples from the server and {= RL('kalbarczyk') =} from Cyprian Kalbarczyk's example solves, each replayed on a sticker-level cube before it was counted.

Every scramble and solution printed below was replayed on that sticker-level cube.

Section A is the docs. B is what was said in the channels that the numbers go against, each with an example. C is what depends on the alg list or on which skeletons you look at, where nobody is wrong. D is what checked out, which is most of it.

---

## A. The docs

**A1. The tutorial's table (Sebastiano Tronto, section 2.4.10, "Move count (an estimate)"), line by line.**
The tutorial says of it: "It is a heuristic estimate, not a mathematically proved one", and that the numbers depend on the algs you know and on the skeleton's length. Next to the computed means:

{{tronto}}

*Random skeletons* are the samples described above, and each cell has the number of skeletons behind it in brackets. Cap 12 for the two-comm types is on {= NSK('5c', L=12, src='two12') =} skeletons that are not the skeletons of the cap-8 column, so do not read a step off this table: on those same {= NSK('5c', L=12, src='two12') =} skeletons a 5c goes from {= PAIR('5c', '8') =} at cap 8 to {= PAIR('5c', '12') =} at cap 12. *not run*: cap 12 was not run for a 2tc. *Posted skeletons* are the real ones, which are the solves people chose to show; they are shorter than 20 moves (mean length in the brackets), and the 3tc cell is two 13-move skeletons.

- **Corner 3-cycle, 5/6**: {= M('3c') =}. Right.
- **Edge 3-cycle, 7**: on random skeletons {= M('3e', L=10) =} with every alg up to 10 moves; with 8 moves or fewer nothing fits on {= CELL('cost_3e', ('8', '20'), 'Nothing fits') =} of them. The tutorial's footnote already says "this varies a lot", so nothing to correct; C4 has what it varies with.
- **2 twisted corners, 8**: {= M('2tc') =} at 20 moves, {= M('2tc', 16) =} at 16. Right.
- **3 twisted corners, 9**: {= M('3tc') =} with 8-movers, {= M('3tc', L=10) =} with algs up to 10 ({= NSK('3tc', L=10) =} skeletons), {= M('3tc', L=12, src='two12') =} up to 12 ({= NSK('3tc', L=12, src='two12') =}). Right, half a move low for pure comms.
- **4 corners (double swap), 9/10**: {= M('2c2c-pure') =}. At the low end of the range. The twisted double swap, which has no row in the table, is {= M('2c2c-twisted') =}.
- **4 corners (3 + 1 twisted), 10**: {= M('3c1t') =}. Right.
- **Corner 5-cycle, 10/11**: {= M('5c') =} at 20 moves, {= M('5c', 16) =} at 16. Right.
- **2 corners and 2 edges, 10**: not sampled. What can be said: no 2c2e alg is shorter than 10 moves, so 10 is what an insertion costs before anything cancels.

Nothing to correct in the table. Its two caveats are both measurable: ten more moves of skeleton take {= PERTEN('3c') =} off a 3c insertion and {= PERTEN('5c') =} off a 5c; and going from 8-movers to every alg of 12 moves takes {= DIFFL('3c', 8, 12) =} off a 3c and about {= PAIRD('5c', '8', '12') =} off a 5c (the 5c on the same {= PAIRN('5c') =} skeletons).

**A2. The tutorial, section 2.4.1: "It happens extremely rarely that the best insertion is given by a 9 move commutator (or longer)".**
For 9-movers that is exact: on random 20-move 3c skeletons a 9-mover is the best {= CELL('one_longer', '20', 'A 9-mover beats every 8-mover and no 10-mover beats it') =} of the time. A 10-mover beats every 8- and 9-mover on {= CELL('one_longer', '20', 'A 10-mover beats every 8- and 9-mover') =} of skeletons, one in {= ONEIN('20', 'A 10-mover beats every 8- and 9-mover') =}, and by a single move {= CELL('one_longer', '20', 'When a 10-mover beats every 8- and 9-mover: by one move only') =} of those times. The tutorial says as much elsewhere ("On rare occasions, 10 moves “sledge insertion” corner commutators", "may cancel many more moves than the standard 8-move commutators"), so this is a number for how rare, not a correction. An example:

{{WIT_TEN}}

**A3. Which leftovers take how many comms** (Yurii Riabov's guide; the tutorial, 2.4.4 and 2.4.5). Nothing to correct. See D.

---

## B. Said in the channels

**B1. "if you can't find a 3c, what is generally better", "2c2c, 3c1t, or 5c?"** (jisu101, [[N6504]], [[N6505]]).
argonblue ([[N6507]]): "i think 3c1t > 2c2c > 5c. mostly because a twist gives you the most freedom to pick comms". jisu101, at the time ([[N6508]], [[N6509]]): "True but so does 2c2c, you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions".
With 8-movers on 20-move random skeletons the order by cost is twisted 2c2c ({= M('2c2c-twisted') =}), pure 2c2c ({= M('2c2c-pure') =}), 3c1t ({= M('3c1t') =}), 5c ({= M('5c') =}). So a 2c2c is the cheaper leftover, by {= DIFF('3c1t', '2c2c-pure') =} to {= DIFF('3c1t', '2c2c-twisted') =} over a 3c1t. Counted per spot, a 2c2c has {= FC('2c2c-pure') =} first comms that leave a 3c and a 3c1t has {= FC('3c1t') =}, which is what jisu101 answered. The posted skeletons are too few to rank the 4-corner types ({= POSTED('2c2c-pure') =} pure 2c2c, {= POSTED('2c2c-twisted') =} twisted, {= POSTED('3c1t') =} 3c1t, of different lengths); they only agree that a 5c is the dearest ({= POSTEDM('5c') =} on {= POSTED('5c') =} skeletons, against {= POSTEDM('2c2c-pure') =}, {= POSTEDM('2c2c-twisted') =} and {= POSTEDM('3c1t') =}).

A typical skeleton of each, 20 moves, 8-movers. Each costs its type's average, rounded: they show what the averages look like on a cube, and the order rests on the 20,000 skeletons per type, not on these three.

{{WIT_TYPICAL_2C2C_TWISTED}}

{{WIT_TYPICAL_2C2C_PURE}}

{{WIT_TYPICAL_3C1T}}

Jay's "i didn't notice a meaningful different between 2 insertion 4c types" ([[N4860]]) is what a one-move difference with a spread of more than a move looks like solve by solve.

**B2. Checking every other move "still guarantees you'll find them"** (notkevin, [[N4772]]: "if you're expecting at least a -3 somewhere, it has to cancel at least a full move, so checking every other still guarantees you'll find them").
Nearly. On random 3c skeletons of 20 moves, when the best 8-mover insertion is an 8-3 or better, checking every second spot and both ends finds an insertion that good {= CELL('one_skip', '20', 'Best is 8-3 or better: every other move finds it') =} of the time. All of those misses ({= SKIPNEAR() =} over seven skeleton lengths) are next to two moves on opposite faces, where the full cancel reaches across the pair and the shifted alg lands two spots away. Nothing better than an {= SKIPWORST() =} was missed on any of {= SKIPTOTAL() =} skeletons. alkamaass had said the rule is not thorough when recommending it ([[N1144]]): "this isn't thorough tho bc it can miss stuff like R (R blah blah B' ) B'". Example:

{{WIT_SKIP}}

**B3. "sub-22 for 3C skeleton", "sub-20 for every other skeleton"** for sub-30 (sequesteredcuber, [[N292]]).
Two moves apart is too close. With 8-movers on random skeletons a 3c in 21 gives sub-30 {= CH('3c', 21, 29) =} of the time; a 5c in 19 gives it {= CH('5c', 19, 29) =}, a 3c1t in 19 {= CH('3c1t', 19, 29) =}. For the same expected total as a 20-move 3c, a 5c has to be {= EXM('5c', 20) =} moves shorter, a 3c1t {= EXM('3c1t', 20) =}, a pure 2c2c {= EXM('2c2c-pure', 20) =} (write-up, section 7). A 19-move 5c with the most common outcome, 30:

{{WIT_FIVEC19}}

---

## C. Depends on the alg list or on the sample

Nobody is corrected here. Each of these is a figure or a report that is right for some alg list or some set of skeletons, and the numbers say which.

**C1. "more like 9 for pure 2-2", "like 9.5 for 2-2 with a twist", "like 10 for 3c1t"** (cpaul, [[N4857]], [[N4858]], [[N4859]]).
A pure 2c2c costs {= M('2c2c-pure') =} and a 3c1t {= M('3c1t') =} with 8-movers at 20 moves. Which 2c2c is the cheaper depends on the alg length: with 8-movers alone the twisted one ({= M('2c2c-twisted') =}), with algs of up to 10 moves the pure one ({= M('2c2c-pure', L=10) =} against {= M('2c2c-twisted', L=10) =}, 500 skeletons each), which is cpaul's order.

**C2. 3tc "mid to high 8 from my experience"** (Phuwish, [[N4537]]).
On random 20-move skeletons a 3tc costs {= M('3tc') =} with 8-movers and {= M('3tc', L=12, src='two12') =} with every alg of up to 12 moves ({= NSK('3tc', L=12, src='two12') =} skeletons). So the figure is lower than pure comms give on a random skeleton and within reach of a longer alg list. The posted 3tc skeletons are only {= POSTED('3tc') =}.

**C3. "5-6, 8-9, 6-8 for good 2c2c, 8-9 for bad 2c2c"** (Baiqiang, [[N4853]], for 3c, 3c1t and 2c2c; "this is i expected not avg expected", [[N4863]]).
Not averages, in Baiqiang's words. Which 2c2c is the good one was asked (kyh, [[N4855]]: "btw you mean good like as in the co matches, the stickers swap with eachother") and not answered, so the two 2c2c figures are not pinned on pure and twisted here. What comes out, in mean added:

| | 3c1t | pure 2c2c | twisted 2c2c |
|---|---:|---:|---:|
| Random 20-move skeletons, 8-movers ({= NSK('3c1t') =} each) | {= M('3c1t') =} | {= M('2c2c-pure') =} | {= M('2c2c-twisted') =} |
| Random 20-move skeletons, algs of up to 10 moves ({= NSK('3c1t', L=10) =} each) | {= M('3c1t', L=10) =} | {= M('2c2c-pure', L=10) =} | {= M('2c2c-twisted', L=10) =} |
| Random 20-move skeletons, algs of up to 12 moves ({= NSK('3c1t', L=12, src='two12') =} each) | {= M('3c1t', L=12, src='two12') =} | {= M('2c2c-pure', L=12, src='two12') =} | {= M('2c2c-twisted', L=12, src='two12') =} |
| Posted skeletons, 8-movers | {= POSTEDM('3c1t') =} ({= POSTED('3c1t') =} skeletons) | {= POSTEDM('2c2c-pure') =} ({= POSTED('2c2c-pure') =}) | {= POSTEDM('2c2c-twisted') =} ({= POSTED('2c2c-twisted') =}) |

On the posted skeletons with a comm plus an alg of up to 12 moves each, a 3c1t averages {= CELL('real_mixed', '3c1t', 'Cap 12') =} and a 2c2c {= CELL('real_mixed', '2c2c (pure or twisted)', 'Cap 12') =}. So figures of Baiqiang's size come out of the skeletons people post, searched with a full alg list. Jay had guessed at the alg list in the same exchange ([[N4860]]): "maybe there's some non 3c type insertion method for 2c2c that lowers the movecount that far". The 10-move 2c2c algs are one.

**C4. Edge 3-cycle, 7** (the tutorial's table, with its footnote: "Warning: this varies a lot! If edges are oriented early in the solve, you have better chances of finding a good insertion (6 or 8 movers).").
On random 20-move skeletons a 3e costs {= M('3e', L=10) =} with every alg of up to 10 moves; with algs of 8 moves or fewer nothing fits on {= CELL('cost_3e', ('8', '20'), 'Nothing fits') =} of them. The short algs do need oriented edges: every edge 3-cycle whose three edges are oriented on all three axes has a 6-mover and no other has one, and an alg of 8 or fewer needs them oriented on at least two. The {= RL('by_type', '3e') =} posted 3e skeletons cost {= RC('3e', 10, 'real') =} at cap 10, but all of them were posted with their insertion, and they are that cheap whether their edges are oriented or not (write-up, 9.2). So the 7 is a fair figure for some alg list on some skeletons, and these samples do not pin down which.

**C5. "In my stats, I found that the best insertion points tend to be in the first 1/3 or last 1/3 of the skel."** (DougCube, [[N6409]]; "no idea why", [[N6410]]).
Not reproduced, and not refuted. On random 3c skeletons the best 8-mover insertion is in each third a third of the time. On the {= RL('spots', 'k_real') =} posted 3c skeletons it is in the first third {= SPOT('real', 0) =} of the time, the middle {= SPOT('real', 1) =}, the last {= SPOT('real', 2) =}. {= DOUG('skeletons_3c') =} of those are DougCube's own skeletons, and on them it is {= DOUGT(0) =}, {= DOUGT(1) =}, {= DOUGT(2) =}. DougCube's stats are of another thing: the insertions DougCube found, of every kind, in solves searched from the ends ("if I need to do two insertions that are linked, the first one will be near the end of the skel or the start of the skel", [[N4641]]; "single 3c insertions are super quick when it's near the start or end of skel for me", [[N3251]]). What both samples here do show is paulduc03's point ([[N6411]]): the very first and very last spot are worse than the rest.

**C6. What an Insertion Finder "optimal" covers.**
2014chri04 ([[N2057]]), on an 8-4 for a 23-move 3c: "IF verifies that this is optimal". tseitsei89 ([[N1441]]), on two comms found by hand for a 21-move 5c: "IF says those are optimal insertions." Both are accurate reports of what Insertion Finder returned; the settings are not stated, and neither says the result is the best possible. 2014chri04 shows, in the same message, a {= W('n2057', 'hand') =} found by hand by rewriting a stretch of the finished solution ("5 moves shorter than the solution i originally found"), and tseitsei89 had written ([[N1440]]) "there might be somethng even better". Searched here: on the first skeleton the 8-4 is the best 8-mover insertion ({= RRLEN('N2057', 'L8') =}) and one 10-move comm gives {= RRLEN('N2057', 'L10') =}; on the second the two comms are the best pair of 8-movers ({= RRLEN('N1440', 'L8') =}) and algs of up to 10 moves give {= RRLEN('N1440', 'L10') =}. So the word means optimal for the alg sets that were on (Baiqiang, [[N3793]]: "Pure 3 corners includes 8 moves comms only. The other one includes some 10 moves"). The first skeleton; both are written out on the examples page:

{{WIT_N2057}}

---

## D. What checked out

**Costs**

- **"a optimal 3c skeleton's insertion is 6 moves on average"** (Aneurin, [[N289]]), **"3c on average gives ~ +6"** (Eli Rogers, [[N4194]]), **"3C insertions are usually +6 moves"** (Jay, [[T1918]]): {= M('3c') =} at 20 moves.
- **"5c is 10-11 moves."** (Aneurin, [[N290]]), **"5c ~high 10"** (Phuwish, [[N4542]]): {= M('5c', 16) =} at 16 moves, {= M('5c') =} at 20.
- **2tc "~8.0 I guess"** (Phuwish, [[N4532]]): {= M('2tc', 16) =} at 16, {= M('2tc') =} at 20.
- **"And isnt 3c1t and 2c2c close to 9.5?"** (tave_789, [[N4539]]; Phuwish, [[N4540]]: "yeah"): {= M('3c1t') =} for a 3c1t, {= M('2c2c-twisted') =} to {= M('2c2c-pure') =} for a 2c2c at 20 moves; {= M('3c1t', 16) =} and {= M('2c2c-twisted', 16) =} to {= M('2c2c-pure', 16) =} at 16. Close, with the 2c2c the lower one.
- **"getting +9 from 2tc is as bad as +11,+12 from 5c"** (Phuwish, [[N4535]]): +9 or worse on {= WORSE('2tc', 9) =} of 2tc skeletons, +12 or worse on {= WORSE('5c', 12) =} of 5c skeletons.
- **"you can usually do a bit better with 5c"** than 13 (Java, [[N1165]], to Zagros): the best is +13 or worse on only {= WORSE('5c', 13) =} of 20-move 5c skeletons.
- **"8-4 8-4 is soooooooo lucky tho"**, "for a 15 move skeleton" (alkamaass, [[N1219]], [[N1220]]): +8 or better on {= P('5c', 8, 14) =} of 14-move 5c skeletons and {= P('5c', 8, 16) =} of 16-move ones.

All of these are for 8-movers on random skeletons.

**Which skeleton**

- **A 5c "maybe like 5-6" shorter than a 3c** (asacuber, [[N1325]], to Fanti): 5 is break-even ({= EXM('5c', 20) =} against a 20-move 3c by expected total, {= EXR('5c') =} for equal chance of a target).
- **The tutorial's "3 corners in 23 moves you will probably get it"** (sub-30) **and "25 moves long you will need some luck"**: {= CH('3c', 23, 29) =} and {= CH('3c', 25, 29) =}. And "4 corner in 18 moves is probably better than one leaving 3 corners in 25": expected {= TOTAL('3c1t', 18) =} or less against {= TOTAL('3c', 25) =}.
- **"3c in 22-24 or 5c in 16-18"** (Gezza Cubing, [[N1740]]), **"18 to anything like 5c, 4c, 3c1t, and 24 for 3c"** (oliynykmax, [[N1741]]): fair pairs, with the two-comm skeleton the better half (sub-30 from a 5c in 18: {= CH('5c', 18, 29) =}; from a 3c in 24: {= CH('3c', 24, 29) =}).
- **21 to 3c: "not strictly guaranteed", "but it's very likely you're getting a 29 or better"** (kyh, [[N4837]], [[N4838]]): {= CH('3c', 21, 29) =}. A 21-move 3c that does not give 29:

{{WIT_N21}}

- **"the chance ur cancelling 4 moves or more is not that high"** (kyh, [[N4186]]): {= GE('24', 4) =} on a 24-move 3c.

**Searching**

- **"Why is there even a difference if the number of possible first insertions is the same tbh"** (wen, [[N4862]], asking, right after Jay's remark on the "2 insertion 4c types"). Read as about the two kinds of 2c2c: the number is the same, {= FC('2c2c-pure') =} first comms per spot for a pure and for a twisted 2c2c (jisu101's "you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions", [[N6508]], [[N6509]], times three ways to twist), and with two comms that do not touch the two cost the same, {= CELL('nesting', 'pure 2c2c', 'The two not touching') =} and {= CELL('nesting', 'twisted 2c2c', 'The two not touching') =}. The {= GAP2C2C('Two comms, nesting allowed') =} between them comes from comms that interact: {= GAP2C2CNEST() =} of it from nesting (the best pair is nested on {= CELL('nesting', 'twisted 2c2c', 'Best needs nesting') =} of twisted 2c2c skeletons and {= CELL('nesting', 'pure 2c2c', 'Best needs nesting') =} of pure ones), the other {= GAP2C2C('No nesting') =} from a second comm that cancels into the first without sitting inside it. Read as about a 2c2c against a 3c1t: the number is not the same, a 3c1t has {= FC('3c1t') =} first comms per spot and a 5c {= FC('5c') =}.
- **Three spots on after a case that needs 10 moves: "I don't think that works."** (DougCube, [[N5147]], to paulduc03's question, [[N5145]]). It does not. After a spot whose case has no alg shorter than 10 moves, the spot two further on holds an 8-3 or better {= TSP(20, 'two', 'ten') =} of the time on a 20-move 3c. One where it is the only 8-3 of the skeleton:

{{WIT_TENSKIP}}

- **The ends of the skeleton are worse** (paulduc03, [[N6411]]): an 8-3 or better at the first or last spot {= CELL('one_positions', 'before the first move', 'It is 8-3 or better') =} of the time, at an inner spot {= CELL('one_positions', 'after moves 3 to 17 (each)', 'It is 8-3 or better') =} (20-move 3c, 8-movers).
- **"for the first 5c insertion you have 5x more options than for the second"** (Not officially a David, [[N139]]): five cycles per spot.
- **Nested comms on a 5c** (Gezza Cubing, [[N1389]]; argonblue, on seeing Insertion Finder do it, [[N5530]]): the best pair is nested on {= CELL('nesting', '5c', 'Best needs nesting') =} of 20-move 5c skeletons with 8-movers. One:

{{WIT_NESTED}}

- **An insertion can cancel more than its own length** (Zagros, [[N3697]]; "true but highly unlikely", DougCube, [[N3696]]): on {= NEGSHARE() =} of 20-move 3c skeletons the best 8-mover makes the solution shorter than the skeleton. One:

{{WIT_NEGATIVE}}

- **A 10-mover that is a setup to an 8-mover "wont cancel more than just inserting 8 movers"** (Ben, [[N5510]]): right wherever the setup cancels a whole move, which is the 8-mover one spot over. The one exception found: on {= FACT('ten_wins_only_conjugates') =} of {= FACTN('ten_sample') =} random 20-move 3c skeletons a setup-type 10-mover is the only best, by one move, because its setup joins a turn of the skeleton. That is the 8-mover put inside that turn. One:

{{WIT_SETUP10}}

- **Suboptimal first comms can be needed** (kyh, [[N5837]]; argonblue, [[N5842]]), and what Ben ([[N5688]]: "greedy 1 is still reasonable if your skeleton is really good") and kyh ([[N5836]]: "i think 1 is realistic") say of greedy 1: {= GV('bugs') =}

{{WIT_GREEDY}}

- **More algs at greedy 0 can give a longer result** (bvcuber13, [[N5819]], [[N5821]]; Ben, [[N6705]], [[N6707]]), and tave_789's reason ([[N5825]]: "if 10-5 is the best first insertion it won’t find the optimals with a worse first insertion"): on {= G10('n') =} random 20-move 5c skeletons, the best first comm followed by the best second gives a longer result with every 3c alg of up to 10 moves than with 8-movers on {= G10('worse') =}, and a shorter one on {= G10('better') =}. One of the longer ones:

{{WIT_GREEDY10}}

- **Insertion Finder "supposed that the status of the cube becomes better after any insertion. so it won't work in this case"** (Baiqiang, [[D3799]], on alkamaass's 8-10; and twenty minutes later, having asked Yan Xuan, [[D3804]]: "this should be supported but somehow it doesn't"). This search has the same limit, and also stops at {= IFP('18 to 3C1T', 'Cap 12') =} on the 18-move skeleton. On the 16-move skeleton that the 8-10 leaves, Insertion Finder gives {= IFP('16 to 3C1T', 'Insertion Finder') =} and a comm plus an alg of up to 12 moves gives {= W('if92', 'l12m') =}:

{{WIT_IF92}}

**Algs and counts**

- **Which leftovers take one, two or three comms**: the "3c - 1 comm", "3s1t, 2s2s, 5s, 3s3s, 2t, 3t - 2 comms" of Yurii Riabov's guide, everything else more; the tutorial's "This case requires three inserted commutators" for four twisted corners and its 5-corner cases; FakeMMAP ([[N5307]]); DougCube's mixed 3c3c ([[N5328]]); wen's four kinds of 7c ([[N393]], [[N396]], to torchlight's list, [[N394]]); 2c2c1t and 5c1t in three (Java, [[N324]]; Renny, [[N5321]]). All right, proved in Lean.
- **Two ways to do an 8-mover** (Gezza Cubing, [[N1383]], [[N1397]]; rogo's "no" to eff's question, [[N1407]], [[N1408]], [[N1409]]): {= F8(2) =} corner 3-cycles have two 8-movers, {= F8(1) =} have one (rogo's `[U2, R' D R]` is one of these), {= F8(0) =} have none.
- **"There arent 8 movers if they're oriented"** (Zagros, [[N2485]]), answered by Jay's `R' F' R B2 R' F R B2` ([[N2488]]): {= FACT('oriented_3c_with_8') =} of the {= FACT('oriented_3c') =} oriented 3-cycles have an 8-mover, so both have a point.
- **A case you can skip a spot after** (Srećko, [[N4195]]): {= FACT('no8_after_any_move_all_3c') =} of the {= STATES('3c') =} 3-cycles have no 8-mover now and none after any one move.
- **"optimal to twist one corner while preserving all edges is 12 moves"** (torchlight, [[N505]]): right as stated. No sequence of {= str(int(TW('min')) - 1) =} moves or fewer that keeps every edge leaves a corner twisted in its place, whatever else it does to the corners; {= TW('seq') =} sequences of {= TW('min') =} moves do.
- **"the 6 move cases require eo on all axes"** (bpaul, [[N5569]]): exactly. The {= EO('six', 3) =} edge 3-cycles with a 6-mover are the {= EO('all', 3) =} whose three edges are oriented on all three axes.
- **The shortest 2c2c alg is 10** (zakk drewji, [[N3526]]): yes, `R2 U' L2 D B2 R2 D' L2 U F2` for one. A twisted 2c2c needs 12.
- **"10 moves is the minimum for any 2E2C without cancellations"** (Noah Swor, [[N3120]]); **"every 10-move 2e2c is a cyclic shift of this alg or its inverse (up to rotations/mirrors ofc)"** (notkevin, [[N3142]]); **1848 times 6 states** (argonblue, [[N6626]], [[N6628]]): all three exact. {= ALGS('2c2e', 10) =} ten-move algs, one class, {= STATES('2c2e') =} states.

---

## Docs referred to

- Sebastiano Tronto, [Fewest Moves Tutorial](https://fmcsolves.cubing.net/fmc_tutorial_ENG.pdf), version 3 (January 2020), revision 3.04 (August 2023).
- Yurii Riabov, [Hitchhiker’s Guide to FMC](https://docs.google.com/document/d/16nu10y1JkUmVDC11c1h_ULzAl4Vze7zR), March 2024.
- Cyprian Kalbarczyk, [Blockbuilding example solves](https://docs.google.com/document/d/1oWbbzc375q4FRIuzA5U091yaiGxt0zkFObGPe5P24_I).
- [Insertion Finder](https://333.fm/if): the site 333.fm is Baiqiang Dong's and the core was written by Yan Xuan (Baiqiang, [[D3803]]).
