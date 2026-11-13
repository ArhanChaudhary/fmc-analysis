New stuff first, then what the numbers confirm. Everything is on random skeletons unless a line says real. *8-movers* means pure 8-move comms only (cap 8), and a line with no length is for 20-move skeletons.

**What is new here**

- **Which 2c2c is the cheap one depends on your alg list.** It flips because only the pure one has 10-move algs; a twisted one has none under 12. Mean added on 20-move skeletons:

  | Algs allowed | Twisted 2c2c: mean added | Pure 2c2c: mean added |
  |---|---:|---:|
  | 8-movers | {= M('2c2c-twisted') =} | {= M('2c2c-pure') =} |
  | every alg up to 10 moves ({= NSK('2c2c-pure', L=10) =} skeletons each) | {= M('2c2c-twisted', L=10) =} | {= M('2c2c-pure', L=10) =} |

  The cap-10 order is cpaul's ("I'd say more like 9 for pure 2-2", "and like 9.5 for 2-2 with a twist"), and it's **computer only** unless you've learned the 10-move pure 2c2c algs. With the 8-movers you actually insert by hand, the twisted one is cheaper.
- **By cost a 2c2c beats a 3c1t, and a 3c1t beats a 5c.** That answers jisu101's "2c2c, 3c1t, or 5c?" ([[N6504]], [[N6505]]). A 2c2c is {= DIFF('3c1t', '2c2c-pure') =} to {= DIFF('3c1t', '2c2c-twisted') =} cheaper than a 3c1t (20 moves, 8-movers), so argonblue's "i think 3c1t > 2c2c > 5c" ([[N6507]]) has the 5c where it belongs and the first two swapped (a typical skeleton of each is example [a] in section 10). The hand search, best first comm and then the best second, keeps the order: a 2c2c is {= GDIFF('3c1t', 'pure 2c2c') =} to {= GDIFF('3c1t', 'twisted 2c2c') =} cheaper (8.4). It's about a move on average, and the spread from one skeleton to the next is wider than that, so you won't really notice it solve by solve. This is cost only: how long the comms take to find isn't measured.
- **wen's question, answered**: "Why is there even a difference if the number of possible first insertions is the same tbh" ([[N4862]]). For the two kinds of 2c2c the number really is the same, {= FC('2c2c-pure') =} first comms per spot, and when the two comms don't touch they cost the same ({= CELL('nesting', 'pure 2c2c', 'The two not touching: mean added') =} and {= CELL('nesting', 'twisted 2c2c', 'The two not touching: mean added') =}). The {= GAP2C2C('Nesting allowed: mean added') =} between them comes from comms that interact, {= GAP2C2CNEST() =} of it from nesting: the best twisted pair is nested on {= CELL('nesting', 'twisted 2c2c', 'Best needs nesting') =} of skeletons, the best pure pair on {= CELL('nesting', 'pure 2c2c', 'Best needs nesting') =}. Across types the number isn't the same, and the costs come in the same order (first line of the next block):

  | Leftover | First comms that leave a 3c, per spot |
  |---|---:|
  | 2tc | {= FC('2tc') =} |
  | 2c2c | {= FC('2c2c-pure') =} |
  | 3tc | {= FC('3tc') =} |
  | 3c1t | {= FC('3c1t') =} |
  | 5c | {= FC('5c') =} |

  ✓ Lean: these counts, for every leftover of each type.

- **A longer alg list is worth far more on two comms than on one.** Same skeletons under every cap ({= PAIRN('5c') =} of 20 moves per type):

  | Leftover | Cap 8: mean added | Cap 10: mean added | Cap 12: mean added |
  |---|---:|---:|---:|
  | pure 2c2c | {= PAIR('2c2c-pure', '8') =} | {= PAIR('2c2c-pure', '10') =} | {= PAIR('2c2c-pure', '12') =} |
  | 5c | {= PAIR('5c', '8') =} | {= PAIR('5c', '10') =} | {= PAIR('5c', '12') =} |
  | 3tc | {= PAIR('3tc', '8') =} | {= PAIR('3tc', '10') =} | {= PAIR('3tc', '12') =} |

  The 3tc's whole step from cap 10 to cap 12 comes from longer comms, since no 3tc alg is 12 moves or fewer. Where a 10-move pure 2c2c alg fits ({= CELL('direct', 'pure 2c2c', 'Alg of 10 or less: fits somewhere') =} of skeletons) it beats two 8-movers by {= f2(X('direct', 'pure 2c2c', 'Two 8-move comms on the skeletons where an alg of 10 or less fits: mean added') - X('direct', 'pure 2c2c', 'Alg of 10 or less: mean added')) =}. Caps 10 and 12 count every alg of that length, so these are **computer only**, the answer key for a full alg list. What carries over to an attempt is which algs are worth learning (the 10-move pure 2c2c algs, 6.3).
- **Longer algs barely help a 3c.** At 20 moves it's {= M('3c') =} with 8-movers, {= M('3c', L=10) =} with every alg up to 10 moves and {= M('3c', L=12) =} up to 12. How often a longer alg is what wins, on 20-move skeletons:

  | What happens | Share of skeletons |
  |---|---:|
  | An 8-mover is as good as anything up to 10 | {= CELL('one_longer', '20', 'An 8-mover is as good as anything up to 10') =} |
  | A 9-mover is the best | {= CELL('one_longer', '20', 'A 9-mover beats every 8-mover and no 10-mover beats it') =} |
  | A 10-mover is the only best (example [b]) | {= CELL('one_longer', '20', 'A 10-mover beats every 8- and 9-mover') =} |
  | of those, the 10-mover wins by a single move | {= CELL('one_longer', '20', 'When a 10-mover beats every 8- and 9-mover: by one move only') =} |

  A 10-mover as the only best is about one skeleton in {= ONEIN('20', 'A 10-mover beats every 8- and 9-mover') =}. So the tutorial's "extremely rarely" holds for 9-movers. Ben's "if its a setup to a regular comm then it wont cancel more than just inserting 8 movers" holds on all but {= fmt(FACT('ten_wins_only_conjugates'), FACT('ten_sample')) =} of 20-move skeletons, and those are an 8-mover put inside a turn of the skeleton (a `B'` done as `B2`, the comm, `B`; example [i]). For a hand search on a 3c, 8-movers are enough.
- **The best first comm isn't always the one to follow.** On a 20-move 5c with 8-movers the best first comm is an 8-3 or better on {= CELL('greedy_first', '20', '5c: 8-3 or better') =} of skeletons (a 3c's best comm: {= CELL('greedy_first', '20', '3c: 8-3 or better') =}), but taking it and then the best second doesn't always give the best pair:

  | How you search | Misses the best pair on, share of skeletons | Mean moves added |
  |---|---:|---:|
  | best first comm, then the best second | {= GLOSS('5c', 0) =} | {= CELL('greedy', '5c', 'Best first comm only: mean added') =} |
  | also first comms one move worse (Insertion Finder's greedy 1) | {= GLOSS('5c', 1) =} | {= CELL('greedy', '5c', 'First comms within 1 move: mean added') =} |
  | also two moves worse (example [f]) | {= GLOSS('5c', 2) =} | {= CELL('greedy', '5c', 'First comms within 2 moves: mean added') =} |
  | best pair of comms (computer) | | {= CELL('greedy', '5c', 'Best pair of comms: mean added') =} |

  With every 3c alg up to 10 the best first comm misses the best pair on {= GLOSS('5c', 0, L=10) =}, and the longer list actually gives a longer result than 8-movers alone on {= G10('worse') =} of {= G10('n') =} skeletons (shorter on {= G10('better') =}). That's what bvcuber13 and Ben ran into on Insertion Finder; it happens, but not often (example [l]). The best pair is a computer number. Best first comm then best second is the hand search, and also following the first comms a move worse is the hand fix.
- **Checking every other move** (3c, 8-movers):

  | Which spots you check | Finds the best, share of skeletons | Finds a best of 8-3 or better, share of those skeletons |
  |---|---:|---:|
  | every other move | {= CELL('one_skip', '20', 'Every other move finds the best') =} | {= CELL('one_skip_good', '20', 'Best is 8-3 or better: every other move finds it') =} |
  | every third move (example [j]) | {= CELL('one_skip', '20', 'Every third move finds the best') =} | {= CELL('one_skip_good', '20', 'Best is 8-3 or better: every third move finds it') =} |

  Every other move loses {= CELL('one_skip', '20', 'Every other move: mean loss, moves') =} of a move on average, and nothing better than an {= SKIPWORST() =} was missed on any of {= SKIPTOTAL() =} skeletons. Every miss of an 8-3 or better sits next to two moves on opposite faces ({= SKIPNEAR(20) =} at 20 moves): a full cancel reaches across the pair, so the alg moved one move over would go between the two moves of the pair, swapped. So check every other move and both sides of a parallel pair, which is a footnote of the tutorial's 2.4.1. With that, notkevin's "guarantees" ([[N4772]]) holds; as it stands it's a bit too strong (example [c]). These skeletons write an opposite-face pair in one fixed order, which puts one at about 1 neighbouring pair of moves in {= PAIR1IN('study_sample_3c_n20') =}. A separate check gives the same {= EVP('3c_fixed') =}, {= EVP('3c_free') =} where a pair is written either way round, and {= EVP('5c_fixed') =} for the first comm of a 5c (8.3).
- **paulduc03's question, answered**: after a case that needs 10 moves, "can I go 3 moves further instead of 2" ([[N5145]])? No, like DougCube said. That walk misses a best of 8-3 or better on {= TSP(20, 'rule_miss', 'walks') =} of walks against {= TSP(20, 'plain_miss', 'walks') =} for plain every other move, and every one of the {= FACT('ten_cases') =} 3-cycles that need 10 moves can be at a case with an 8-mover two moves later (example [k]).
- **Exchange rates, 8-movers** (Fanti's question, [[N1324]]): how many moves shorter each skeleton has to be to give the same expected total as a 20-move 3c.

  | Leftover | Shorter by, moves |
  |---|---:|
  | 5c | {= EXM('5c', 20) =} |
  | 3c1t | {= EXM('3c1t', 20) =} |
  | 3tc | {= EXM('3tc', 20) =} |
  | pure 2c2c | {= EXM('2c2c-pure', 20) =} |
  | twisted 2c2c | {= EXM('2c2c-twisted', 20) =} |
  | 2tc | {= EXM('2tc', 20) =} |

  For the same chance of a given result the rates are about the same, a bit lower when the 3c would need luck. asacuber's "maybe like 5-6" ([[N1325]]) for the 5c is right, at the 5 end. With algs up to 10 a 5c needs about {= EXR('5c', 10) =} and a pure 2c2c about {= EXR('2c2c-pure', 10) =} (**computer only**: that assumes every alg up to 10). The cap-8 rates are for the attempt, but they price a two-comm skeleton at its best pair. Taking just the best first comm by hand adds {= f2(X('greedy', '5c', 'Best first comm only: mean added') - X('greedy', '5c', 'Best pair of comms: mean added')) =} on a 5c and {= f2(X('greedy', 'twisted 2c2c', 'Best first comm only: mean added') - X('greedy', 'twisted 2c2c', 'Best pair of comms: mean added')) =} on a twisted 2c2c (8.4), so add that to the rate if you won't follow up more than the best first comm.
- **trig0n's 17 to 3c** ([[T73]]; nobody replied). Modelled 17-move sequences, {= DRN() =} each, with 8-movers:

  | The moves | Mean moves added | Adds 6 or less | Nothing fits |
  |---|---:|---:|---:|
  | random moves | {= CELL('dr17', ('random moves', '8'), 'Mean moves added') =} | {= CELL('dr17', ('random moves', '8'), 'Adds 6 or less') =} | {= CELL('dr17', ('random moves', '8'), 'Nothing fits') =} |
  | after EO | {= CELL('dr17', ('EO in 5, then moves that keep EO', '8'), 'Mean moves added') =} | {= CELL('dr17', ('EO in 5, then moves that keep EO', '8'), 'Adds 6 or less') =} | {= CELL('dr17', ('EO in 5, then moves that keep EO', '8'), 'Nothing fits') =} |
  | DR moves | {= CELL('dr17', ('EO in 4, DR in 10, then DR moves; any 3c', '8'), 'Mean moves added') =} | {= CELL('dr17', ('EO in 4, DR in 10, then DR moves; any 3c', '8'), 'Adds 6 or less') =} | {= CELL('dr17', ('EO in 4, DR in 10, then DR moves; any 3c', '8'), 'Nothing fits') =} |
  | DR moves, a 3c that DR moves can leave | {= CELL('dr17', ('EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave', '8'), 'Mean moves added') =} | {= CELL('dr17', ('EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave', '8'), 'Adds 6 or less') =} | {= CELL('dr17', ('EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave', '8'), 'Nothing fits') =} |

  So the DR guide's feeling that 8-movers cancel less on DR skeletons, which it says hasn't been proved, is true in this model, by {= DRGAP() =} of a move, and it comes from which corners are left, not from the moves. These are move sequences, not DR solves.
- **Nesting matters on a 5c.** With 8-movers on 20-move skeletons the best pair of comms is nested on {= CELL('nesting', '5c', 'Best needs nesting') =} of 5c skeletons, and forbidding it costs {= NEST('5c') =}; two comms that don't touch at all cost {= APART('5c') =} more than the best. So the nested pair argonblue saw Insertion Finder return is no rarity (example [e]). With algs of up to 10 moves the best is a nested pair on {= NESTED10('5c') =} ({= NSK('5c', L=10) =} skeletons). Finding the best pair is a computer search; the hand version is Gezza Cubing's: on a 5c, also try the second comm inside the first (6.5).
- **Real move sequences with a random leftover cost what random ones cost.** {= RL('covered') =} worked examples, {= RL('skeletons') =} distinct skeletons: {= RL('server') =} examples from the server and {= RL('kalbarczyk') =} from Kalbarczyk's example solves, searched the same way. With 8-movers:

  | Leftover on the real moves | Real moves: mean added | Random moves: mean added |
  |---|---:|---:|
  | a random 3c (the same) | {= CP('3c', 8, 'real') =} | {= CP('3c', 8, 'rand') =} |
  | a random 5c (within a tenth of a move) | {= CP('5c', 8, 'real') =} | {= CP('5c', 8, 'rand') =} |
  | the posted 3c, their own leftover | {= RC('3c', 8, 'real') =} | {= RC('3c', 8, 'rand') =} |

  So blocks, pairs and triggers in the moves make next to no difference to how insertions cancel. The posted skeletons with their own leftover are cheaper, and selection is part of that: the skeletons shown with their insertion are {= SUBD('from the server, an insertion written out', '3c') =} from random, the {= SUBN('the last two together', '3c') =} posted bare or in a collection {= SUBD('the last two together', '3c') =}. Whether those last few tenths are real or selection again, these few skeletons can't say. For a skeleton you've just found, start from the random-skeleton tables.
- **Edges depend on the alg list.** Only {= EDGE8() =} of edge 3-cycles have an alg of 8 moves or fewer (corners: {= CORNER8() =}), and the {= EO('six', 3) =} with a 6-mover are exactly the {= EO('all', 3) =} whose three edges are oriented on all three axes (✓ Lean, these counts). With 8 or fewer nothing fits on {= CELL('cost_3e', ('8', '20'), 'Nothing fits') =} of random 20-move skeletons; with every alg up to 10 a 3e costs {= M('3e', L=10) =} (**computer only** unless you know every edge alg up to 10). The {= RL('by_type', '3e') =} real 3e skeletons cost {= RC('3e', 10, 'real') =} at cap 10. All of them were posted with their insertion, and whether their three edges are oriented doesn't explain the difference (9.2).
- **Where the insertion is** (3c, 8-movers). No third of a random skeleton is better than another. The first and the last spot are clearly worse: an 8-3 or better there {= CELL('one_positions', 'before the first move', 'It is 8-3 or better') =} of the time, against {= CELL('one_positions', 'after moves 3 to 17 (each)', 'It is 8-3 or better') =} at an inner spot, and the spot next to them a little worse. An 8-mover fits at about half the spots ({= CELL('one_positions', 'after moves 3 to 17 (each)', 'An 8-mover fits there') =}). On the {= RL('spots', 'k_real') =} real 3c skeletons the best spot is in the first, middle and last third {= SPOT('real', 0) =}, {= SPOT('real', 1) =} and {= SPOT('real', 2) =} of the time, so DougCube's "first 1/3 or last 1/3" doesn't show up. It isn't refuted either: DougCube's stats count the insertions DougCube found, of every kind (9.4).
- **Exact counts.**
  - Two 3-cycle insertions solve exactly 3c1t, 2c2c (pure and twisted), 5c, 3c3c, 2tc and 3tc. {= THREE('types') =} other types of corner leftover ({= THREE('names') =} by name, {= THREE('states') =} states) need exactly three (Lean).
  - {= ALGN('3c', 8) =} of the {= STATES('3c') =} corner 3-cycles have an 8-mover, {= F8(2) =} of them two different ones. {= FACT('oriented_3c_with_8') =} of the {= FACT('oriented_3c') =} 3-cycles that keep all three corners oriented have one, and {= FACT('no8_after_any_move_all_3c') =} 3-cycles have none even after any one move. ✓ Lean
  - No 2c2c alg is shorter than 10 moves ({= ALGN('2c2c-pure', 10) =} pure cases have a 10-mover; a twisted one needs 12). ✓ Lean up to 10 moves
  - A 3c1t has an alg of 12 moves or fewer in only {= ALGN('3c1t', 12) =} of {= STATES('3c1t') =} cases, a 2tc in {= ALGN('2tc', 12) =} of {= STATES('2tc') =} (the pairs of corners that don't share an edge).
  - No alg that leaves a corner twisted in place is shorter than {= TW('min') =}, no three-twist is within 12, no 2c2e is shorter than 10.
- **People and Insertion Finder.** The insertion that was posted for a 3c is the best 8-mover insertion or better in {= AUWN('author_hand_3c', 'L8', ' cases') =}, and on the corner leftovers that need two comms in {= AUWN('author_hand_two', 'L8') =}. Against algs up to 12 (**computer only**, the answer key), {= AUL('author_hand', 'L12') =} of the hand solutions leave a move or more on the table. On the Insertion Finder pages the search gives the same result once its cap covers the algs Insertion Finder used, and at cap 12 it's one move shorter on {= IFBETTER() =}. An Insertion Finder "optimal" is optimal for the alg sets that were on: on the 23-move 3c of [[N2057]] the posted 8-4 is the best 8-mover insertion ({= RRLEN('N2057', 'L8') =}), and a 10-mover that cancels all ten of its moves gives {= RRLEN('N2057', 'L10') =} (9.5).

**What it confirms or corrects**

- **The tutorial's table holds.** The two-comm leftovers, 20 moves, 8-movers, next to the tutorial's corner rows:

  | Source | 2tc | twisted 2c2c | pure 2c2c | 3tc | 3c1t | 5c |
  |---|---:|---:|---:|---:|---:|---:|
  | Best pair of 8-movers | {= M('2tc') =} | {= M('2c2c-twisted') =} | {= M('2c2c-pure') =} | {= M('3tc') =} | {= M('3c1t') =} | {= M('5c') =} |
  | The tutorial | two twisted 8 | | double swap 9/10 | three twisted 9 | 10 | 10/11 |

  Every tutorial row is within about half a move; the 3tc is the one that's a full half move off. At 16 moves the six are {= D16RANGE() =} higher. These are best pairs of 8-movers, a computer number, but following the best first comm and the ones a move worse gets within {= f2(max(X('greedy', r, 'First comms within 1 move: mean added') - X('greedy', r, 'Best pair of comms: mean added') for r in ('2tc', '3tc', 'pure 2c2c', 'twisted 2c2c', '3c1t', '5c', '3c3c'))) =} of them (8.4), so they hold for a careful hand search too.
- **A 3c costs +{= M('3c') =} on a 20-move skeleton with 8-movers.** (That average is over the skeletons where an 8-mover fits at all; the shares after it are over every skeleton.) +6 or better on {= P('3c', 6) =} of skeletons, +5 or better on {= P('3c', 5) =}, +4 or better on {= P('3c', 4) =}. It's {= M('3c', 10) =} at 10 moves and {= M('3c', 30) =} at 30, so length matters little. Everybody's +6 is right.
- **The estimates people posted.** cpaul's 9 and 10 are right. Phuwish's are close (2tc {= M('2tc') =}, 5c {= M('5c') =}) except the 3tc: "mid to high 8 from my experience" against {= M('3tc') =} with 8-movers, and algs up to 12 bring it to {= M('3tc', L=12, src='two12') =} ({= NSK('3tc', L=12, src='two12') =} skeletons). Baiqiang's are lower and, in Baiqiang's words, not averages; with algs up to 12 (**computer only**) a pure 2c2c averages {= M('2c2c-pure', L=12, src='two12') =} and a twisted one {= M('2c2c-twisted', L=12, src='two12') =} ({= NSK('2c2c-pure', L=12, src='two12') =} skeletons each), figures of that size.
- **For sub-30, 8-movers.** How often each skeleton makes it:

  | Skeleton | Chance of sub-30 |
  |---|---:|
  | 3c in 21 (kyh's "very likely") | {= CH('3c', 21, 29) =} |
  | 3c in 23 (the tutorial's "probably") | {= CH('3c', 23, 29) =} |
  | 3c in 24 | {= CH('3c', 24, 29) =} |
  | 3c in 25 (the tutorial's "some luck") | {= CH('3c', 25, 29) =} |
  | 5c in 18 | {= CH('5c', 18, 29) =} |
  | 5c in 19 | {= CH('5c', 19, 29) =} |
  | pure 2c2c in 19 | {= CH('2c2c-pure', 19, 29) =} |

  The tutorial's 4 corners in 18 beat 3 corners in 25 by a lot (expected {= TOTAL('2c2c-twisted', 18) =} to {= TOTAL('3c1t', 18) =} against {= TOTAL('3c', 25) =}). sequesteredcuber's aims for sub-30, "sub-22 for 3C skeleton", "sub-20 for every other skeleton" ([[N292]]), hold on average for every type (a 19-move 5c averages {= TOTAL('5c', 19) =}) and are unevenly safe: the chance at the limit runs from {= CH('3c', 21, 29) =} for the 3c down to {= CH('5c', 19, 29) =} for a 5c (7.3, example [g]).
- **Odds people gave.** On a 5c, Java's "i think you can usually do a bit better with 5c", against Zagros's 13, is right: +13 or worse is the best there is on only {= WORSE('5c', 13) =} of 20-move skeletons. Phuwish's "I always think that getting +9 from 2tc is as bad as +11,+12 from 5c" is right in odds ({= WORSE('2tc', 9) =} against {= WORSE('5c', 11) =} and {= WORSE('5c', 12) =}). An insertion that cancels more than its own length is real and rare: {= NEGSHARE() =} of 20-move 3c skeletons (example [d]).
- **The counts people gave.** The lists of which leftovers take one, two or three comms (Riabov's guide, the tutorial, FakeMMAP, DougCube's mixed 3c3c, wen's four 7-corner leftovers) are right, proved in Lean. Against the full alg lists, torchlight's 12 moves to twist a corner in place, Noah Swor's 10 for a 2c2e, notkevin's single class of {= ALGS('2c2e', 10) =} ten-move 2c2e algs and bpaul's "eo on all axes" for the 6-move edge cases are right too.
