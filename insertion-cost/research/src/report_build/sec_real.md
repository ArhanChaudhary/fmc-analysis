---

## 9. Real skeletons and Insertion Finder

### 9.1 Which skeletons

The reading notes for this study hold {= RL('examples') =} worked examples from the three channels and the docs: a scramble, a skeleton, usually the insertions and a final length. Nothing in those notes had been put on a cube, so every example was replayed here on a sticker model and counted only if the scramble and the skeleton really leave one of the leftovers of section 4.

{{real_counts}}

The second source is Cyprian Kalbarczyk's "Blockbuilding example solves" (Kalbarczyk's own solves from late 2019 to October 2022, "probably from a better half of all scrambles"): the solves whose first skeleton and final solution could be read by a script.

That makes {= RL('covered') =} worked examples on {= RL('skeletons') =} distinct skeletons (a few skeletons were posted twice, or with two solutions). By leftover the {= RL('skeletons') =} skeletons are {= RL('by_type', '3c') =} 3c, {= RL('by_type', '5c') =} 5c, {= RL('by_type', '3c1t') =} 3c1t, {= REALN('2c2c') =} 2c2c, {= RL('by_type', '3e') =} 3e and {= REALN('rest') =} others. All of them are searched like the random ones: every spot, every alg within the cap. For edge leftovers the comm-plus-alg search at cap 12 did not finish in the time allowed on {= RL('no_mixed12') =} examples; those keep the better of their cap-12 result without it and their cap-10 result with it.

### 9.2 Real against random

Each real skeleton is compared with random skeletons of its own length and type (one comm for 3c and 3e; otherwise the best of two comms and one alg; no comm plus alg on either side).

**Mean added: real skeletons, and random skeletons of the same lengths and types. At cap 8 (8-movers; for edges, algs of 8 moves or fewer) the means are over the real skeletons where something fits, counted in the fourth column; at caps 10 and 12 something fits on every one. There is no random sample at cap 12 for these lengths.**

{{real_cost}}

Real skeletons come out cheaper, and by a lot: {= RDIFF('3c', 8) =} for a 3c (±{= RSE('3c', 8) =}), {= RDIFF('5c', 8) =} for a 5c (±{= RSE('5c', 8) =}), {= RDIFF('3c1t', 8) =} for a 3c1t (±{= RSE('3c1t', 8) =}) with 8-movers. In this section ± is one standard error of the difference (Appendix C gives two standard errors for the random samples). Two tests say where the gap comes from.

**It is not how real skeletons are written.** Take the same real move sequences, all {= CPN('3c', 'sequences') =} of them that are 10 to 30 moves long, and put a random 3c or a random 5c on each, many times over:

**The real move sequences with a random leftover, against random sequences of the same lengths with a random leftover: mean added.**

{{real_corpus}}

For a 3c the same as random sequences ({= CP('3c', 8, 'real') =} against {= CP('3c', 8, 'rand') =} at cap 8). For a 5c within a tenth of a move: the real sequences are {= f2(float(CP('5c', 8, 'rand')) - float(CP('5c', 8, 'real'))) =} cheaper at cap 8 and {= f2(float(CP('5c', 10, 'rand')) - float(CP('5c', 10, 'real'))) =} at cap 10. Blocks, pairs and triggers in the moves make next to no difference to how insertions cancel.

**Selection is part of it.** Split by where the skeleton comes from:

**Real minus random, 8-movers, by where the skeleton was posted.**

{{real_subsets}}

- A skeleton posted together with its insertion is more than a move cheaper than a random one ({= SUB('from the server, an insertion written out', '3c') =} for a 3c). People post the solves that came out well, and a skeleton nobody found a decent insertion for is rarely shown.
- The two groups that are picked less, skeletons posted as they are and Kalbarczyk's collection, are {= SUB('from the server, no insertion written (a skeleton posted as it is)', '3c') =} and {= SUB("Kalbarczyk's example solves", '3c') =} from random for a 3c, on {= SUBN('from the server, no insertion written (a skeleton posted as it is)', '3c') =} and {= SUBN("Kalbarczyk's example solves", '3c') =} skeletons: {= SUB('the last two together', '3c') =} on the {= SUBN('the last two together', '3c') =} together. The {= SUBN('the last two together', '5c') =} such 5c are at zero ({= SUB('the last two together', '5c') =}).
- So selection is part of the gap: {= SUBD('from the server, an insertion written out', '3c') =} for the 3c skeletons posted with their insertion, {= SUBD('the last two together', '3c') =} for the {= SUBN('the last two together', '3c') =} less-picked ones. Whether those remaining few tenths are real (the three corners left are the ones the last moves just handled, so a comm may cancel into them more easily) or are selection again, these few skeletons cannot say. For a skeleton you have just found, start from the random-skeleton tables.

This bears on the estimates of section 2. The tutorial's corner rows and cpaul's 9 and 10 are what 8-movers give on random skeletons, each within about half a move. Phuwish's figures are close, except the 3tc. Baiqiang's are lower and are not averages ([[N4863]]). The posted skeletons are lower too, {= RC('3c1t', 8, 'real') =} for a 3c1t and {= RC('2c2c (pure or twisted)', 8, 'real') =} for a 2c2c with 8-movers: the skeletons that get posted are not a random draw from the skeletons that get found.

With a comm plus an alg also allowed, the same real skeletons average:

**Mean added on the real skeletons when a comm plus an alg is allowed as well. The last column is the number of skeletons where that search did not finish at cap 12; they keep the better of their cap-12 value without it and their cap-10 value with it.**

{{real_mixed}}

At cap 12 that is {= CELL('real_mixed', '3c1t', 'Cap 12') =} for a 3c1t and {= CELL('real_mixed', '2c2c (pure or twisted)', 'Cap 12') =} for a 2c2c. So posted skeletons searched with a full alg list give figures of the size of Baiqiang's 8-9 and 6-8.

**Edges.** The {= RL('by_type', '3e') =} real 3e skeletons cost {= RC('3e', 10, 'real') =} at cap 10 against {= RC('3e', 10, 'rand') =} for random ones ({= RDIFF('3e', 10) =}), and with algs of 8 or fewer something fits on {= RC('3e', 8, 'k') =} of the {= RL('by_type', '3e') =}. Is that because their edges are oriented? Count, for the leftover as it stands at the end of the skeleton, on how many of the three axes all three of its edges are oriented:

**Edge 3-cycles by the number of axes on which their three edges are oriented: all {= STATES('3e') =} of them and how many have a short alg; the real 3e skeletons; the random 20-move 3e skeletons of the sample. Mean added at cap 10 (every alg of up to 10 moves).**

{{real_eo}}

- **The short algs do depend on it**, the way bpaul said ([[N5569]]): every 3-cycle oriented on all three axes has a 6-mover and no other has one; half of those oriented on two axes have an alg of 8 or fewer; none of the rest does.
- **The real leftovers are oriented a little more often than a random 3-cycle**: {= EON('real', (2, 3)) =} of {= RL('by_type', '3e') =} on two or three axes, against {= EOSHARE('all', (2, 3)) =} of all edge 3-cycles, and {= EON('real', (0,)) =} of {= RL('by_type', '3e') =} on none, against {= EOSHARE('all', (0,)) =}.
- **But that is not what makes them cheap.** On random skeletons a leftover oriented on all three axes is about two moves cheaper at cap 10 than one oriented on none ({= EO('rand10', 3) =} against {= EO('rand10', 0) =}). The real ones are far below the random ones at every count: the {= EON('real', (0,)) =} that are oriented on no axis average {= EO('real10', 0) =}.
- **All {= RL('by_type', '3e') =} were posted with their insertion written out** (DougCube's 10-9 on the examples page is one of them). That is the selection of the 3c table again, and stronger. What a 3e costs on a skeleton you have just found, these {= RL('by_type', '3e') =} cannot say.

### 9.3 The authors against the search

For the examples that state a final length, the author's added moves against the best there is on the same skeleton. *One comm, two comms or one alg* is what the tables of section 6 use; the last two rows also allow a comm plus an alg.

**By hand, all leftovers:**

{{real_author_hand}}

**By hand, 3c only:**

{{real_author_hand_3c}}

**By hand, the corner leftovers that need two comms:**

{{real_author_hand_two}}

- **On a 3c, the posted insertion is the best 8-mover insertion or better in {= AUWN('author_hand_3c', 'L8', ' cases') =}.** {= DUPS('3c') =} of the {= AU('author_hand_3c', 'L8', 'k') =} are a second solution on a skeleton already in the list. Again these are posted solves, and several say they were checked with Insertion Finder first.
- **On the corner leftovers that need two comms, {= AUWN('author_hand_two', 'L8') =}** are as good as the best pair of 8-movers or better.
- ***Author shorter* at cap 8** is someone using an alg longer than 8 moves.
- **Against algs up to 12** (**computer only**, the answer key), {= AUL('author_hand', 'L12') =} of the hand solutions leave a move or more on the table. That is the size of what a full alg list adds over what people insert, on skeletons they were happy to post.
- **Shorter than anything in the search**: {= SHORTROWS() =}, beat the best at cap 12 with a comm plus an alg. None does it with a better insertion: they add slice insertions, or rewrite a stretch of the finished solution with something shorter.

**The {= str(len(REAL['shorter12'])) =} solutions shorter than the best at cap 12 with a comm plus an alg, and why. *By* says whether the solution was found by hand or is an Insertion Finder result.**

{{real_shorter}}

One of the slice pairs is the one kyh called "-3 with a slice insertion is insane" ([[N6812]]).

What the hand insertions cancel, replayed move by move where the solution is written out:

**8-move insertions in the hand solutions, by what they cancel.**

{{real_notes}}

{= NOTESGE3('on a 3c skeleton') =} of the posted 8-movers on a 3c are 8-3 or better. On random skeletons the best insertion is that good {= GE('18', 3) =} of the time at this length. That is the same selection, seen from the other side.

### 9.4 Where the best insertion is, on real skeletons

**3c: where the best 8-mover insertion is, by thirds of the skeleton, cut as in 8.1 (ties share). *Skeletons tried* is how many were searched; the shares are of the ones with an 8-mover somewhere (last column). The real move sequences with a random 3c are the first {= f"{6000:,}" =} of the {= CPN('3c', 'lines') =} of section 9.2, and the random sequences are as many, of the same lengths.**

{{real_spots}}

- On the {= RL('spots', 'k_real') =} real 3c skeletons the best spot is in the first third less often than in the other two, and not more often near the two ends. With a random 3c on the same move sequences the split is that of random sequences of the same lengths, {= SPOT('corpus', 0) =}, {= SPOT('corpus', 1) =}, {= SPOT('corpus', 2) =} (the first third has a spot more than the others at the lengths where the spots do not split evenly).
- {= DOUG('skeletons_3c') =} of the {= RL('spots', 'k_real') =} are DougCube's own skeletons ({= DOUG('examples') =} of the {= RL('covered') =} examples are DougCube's). On those the split is {= DOUGT(0) =}, {= DOUGT(1) =}, {= DOUGT(2) =}; on the other {= DOUG('rest_3c') =} it is {= DOUGT(0, 'rest_thirds') =}, {= DOUGT(1, 'rest_thirds') =}, {= DOUGT(2, 'rest_thirds') =}.
- So "first 1/3 or last 1/3" ([[N6409]]) is not reproduced: not on random skeletons, not on the real ones, not on DougCube's own. It is not refuted either. DougCube's stats count the insertions DougCube found, of every kind, in solves where the ends are searched first (8.1); this counts where the best 8-mover for a 3c is. And {= DOUG('skeletons_3c') =} skeletons are few.

### 9.5 Insertion Finder

Insertion Finder is at [333.fm/if](https://333.fm/if). Baiqiang ([[D3803]]): "i make the website 333.fm. the core is written by Yan Xuan". {= IFN('all') =} Insertion Finder result pages were posted on the server with their scramble and skeleton. {= IFN('not') =} of them have corners and edges or parity left, which this study does not search. The other {= IFN('compared') =}:

{{if_pages}}

- **Where Insertion Finder used only 8-movers, cap 8 gives the same**: {= IFP('18 to 3C1T', 'This search, cap 8') =} on the 18-move 3C1T (Insertion Finder: {= IFP('18 to 3C1T', 'Insertion Finder') =}), {= IFP('13 to 3T', 'This search, cap 8') =} on the 3T (Insertion Finder, run with its "3 Corners" set only: {= IFP('13 to 3T', 'Insertion Finder') =}).
- **16 to 3C1T**: Insertion Finder's {= IFP('16 to 3C1T', 'Insertion Finder') =} is an 8-5 and a 10-move double swap, `L2 F2 B2 R2 U R2 F2 B2 L2 D` (10-4). Two 8-movers give {= IFP('16 to 3C1T', 'This search, cap 8') =}; a comm plus an alg gives {= IFP('16 to 3C1T', 'Cap 10') =} at cap 10 and {= IFP('16 to 3C1T', 'Cap 12') =} at cap 12.
- **11 to 5C**: its {= IFP('11 to 5C', 'Insertion Finder') =} is an 8-5 and triple sexy (`B' U' B U B' U' B U B' U' B U`, 12-7). That is a comm plus an alg at cap 12, and the search finds {= IFP('11 to 5C', 'Cap 12') =} there. Two comms give {= IFP('11 to 5C', 'This search, cap 8') =} at cap 8 and {= IFP('11 to 5C', 'Cap 10') =} at cap 10.
- So the search is never worse than Insertion Finder once its cap covers the algs Insertion Finder used, and at cap 12 it is one move shorter on {= IFBETTER() =}. It should be: Insertion Finder works from lists of known algs, and here every sequence within the cap counts.

The pages that are not compared:

{{if_pages_not}}

**The insertion both miss.** alkamaass ([[D3794]], [[D3797]]) took the 18-move 3C1T skeleton, put in an 8-move comm that cancels 10 moves ("take that but with the 8-10"), and got a 16-move skeleton that still leaves a 3c1t. Insertion Finder gives {= IFP('16 to 3C1T', 'Insertion Finder') =} on that one and {= IFP('18 to 3C1T', 'Insertion Finder') =} on the original: "it missed 4 moves LMAO". Baiqiang ([[D3799]]): "IF supposed that the status of the cube becomes better after any insertion. so it won't work in this case". And twenty minutes later, having asked Yan Xuan ([[D3804]]): "this should be supported but somehow it doesn't". This search has the same limit. The comm does not bring the leftover any closer to solved, it makes the skeleton shorter, and then two more insertions finish. That is three insertions, and every model in this study stops at two. Such lines exist; how often is not known.

On the 16-move skeleton that the 8-10 leaves, a comm plus an alg of up to 12 moves gives 24:

{{WIT_IF92}}

**What an Insertion Finder "optimal" covers.** 2014chri04 ([[N2057]]), on an 8-4 for a 23-move 3c: "IF verifies that this is optimal". tseitsei89 ([[N1441]]), on two comms found by hand for a 21-move 5c: "IF says those are optimal insertions." Both report what Insertion Finder returned, with settings that are not stated, and neither says the result is the best possible: 2014chri04 goes on to a {= W('n2057', 'hand') =} found by hand, and tseitsei89 had written ([[N1440]]) "there might be somethng even better". Searched here, the 8-4 is the best 8-mover insertion on the first skeleton ({= RRLEN('N2057', 'L8') =}) and the two comms are the best pair of 8-movers on the second ({= RRLEN('N1440', 'L8') =}). With algs of up to 10 moves the first comes to {= RRLEN('N2057', 'L10') =} and the second to {= RRLEN('N1440', 'L10') =}; 2014chri04's own {= W('n2057', 'hand') =} on the first, by rewriting a stretch of the finished solution, is shorter still. So the word means optimal for the alg sets that were on. Baiqiang on the two corner sets ([[N3793]]): "Pure 3 corners includes 8 moves comms only. The other one includes some 10 moves". The first skeleton (both are on the examples page):

{{WIT_N2057}}

**Insertion Finder results quoted in the channels.** {= AU('author_if', 'L8', 'k') =} more examples in the notes give an Insertion Finder result with a scramble and a skeleton that could be replayed ({= RL('if_wording_only') =} of them are called Insertion Finder results only by the wording of the message).

{{real_author_if}}

At cap 8 the search is never better than Insertion Finder by more than a move, and Insertion Finder is ahead on {= AU('author_if', 'L8', 'shorter') =}, where it used a longer alg. At cap 12 with a comm plus an alg the search is ahead on {= AUL_N('author_if', 'L12m') =} of {= AU('author_if', 'L12m', 'k') =}. The settings of those Insertion Finder runs are mostly not stated, so this says what the alg list is worth, not that either tool is wrong.
