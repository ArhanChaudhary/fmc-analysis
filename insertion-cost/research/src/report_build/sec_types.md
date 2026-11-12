---

## 4. How many insertions each leftover needs

This part is exact: every pair of corner 3-cycles was multiplied out, then every triple, and the same for edge pairs. The counts are proved in Lean (Appendix C).

**One or two.** Two corner 3-cycles make exactly {= TWO('corner', 'names') =} kinds of leftover by name, and two edge 3-cycles exactly {= TWO('edge', 'names') =}, and they make every state of each kind. The Lean statement counts the two twist directions apart (three corners twisted clockwise and three twisted counter-clockwise are two types there, and so are the two kinds of 3c1t), which makes the {= TWO('corner', 'names') =} corner kinds {= TWO('corner', 'types') =} types. The last column gives that count for each row:

{{types}}

*States* is how many different leftovers of that kind there are. Nothing else can be solved with two 3-cycle insertions: counting the solved cube and the 3-cycles themselves, two corner 3-cycles reach {= WITHIN2('corner') =} corner states and two edge 3-cycles reach {= WITHIN2('edge') =} edge states, and all of them are in the table.

**Three.** Counted the same way, {= THREE('types') =} types of corner leftover need exactly three 3-cycles, {= THREE('states') =} states in all. By what you would call them they are {= THREE('names') =}:

{{types_three}}

What the server and the docs say about this is right, line by line:

- Yurii Riabov's guide lists "3c - 1 comm", "3s1t, 2s2s, 5s, 3s3s, 2t, 3t - 2 comms" and "All other situations (4c1t, 3c2t, 4t, 5t, etc.) are solved in more than 2 comms". The guide's six are exactly the seven two-comm corner rows above (2c2c counted once).
- Tronto on four twisted corners: "This case requires three inserted commutators." And on five corners: "the only one that requires 2 commutators is the one where the pieces make a 5-cycle. All other cases require 3 commutators, except when you have 5 corners placed but twisted: in that case you need 4." All three statements hold. Five twisted corners are not among the states three 3-cycles reach, and a 3tc plus a 2tc does them in four.
- FakeMMAP ([[N5307]]): "the only way to affect 5 corners with 2 3-cycles, is to do a 5-cycle." Right.
- DougCube's *mixed* 3c3c ([[N5328]]), "which although it doesn't have parity, it cannot be solved with only two 3c comms": right. It is the two twisted 3-cycles of the second table, {= THREE_ROW('mixed 3c3c') =} states, and it takes three.
- wen ([[N393]]): "Also theres 4 types of 7c that work!" torchlight listed three ([[N394]]: "these three?", "7-cycle", "one normal 3-cycle, one twisted 3-cycle, one twist", "one normal 3-cycle, two 2-cycles (normal/twisted)") and asked "what's the fourth" ([[N395]]). wen ([[N396]]): "I counted your last one as 2 separate". Counted wen's way, those are exactly the four leftovers on seven corners that three comms solve: the 7c, the 3c3c1t, and the 3c2c2c with plain swaps and with twisted swaps. Any other leftover on seven corners needs more.
- 2c2c1t "has to be done with 3 comms" (Java, [[N324]]), 5c1t is "Another 3 comms skeleton" (Renny, [[N5321]]): both right.
- Two flipped edges by two 3e algs (DougCube's 19, [[N4395]]): right, 2fe is a two-comm leftover. A pair of *flipped* edge 3-cycles is not: Kalbarczyk's "3E3E in 15, unfortunately with orientation change (you can’t solve them with 2 pure 3-cycles)" is exact.

Everything below is about the leftovers of the first table. What a three-comm leftover costs is not measured here.

---

## 5. The algorithms

For every leftover of every type, all move sequences of 12 moves or fewer that solve it were listed. The counts are reference: which case has an 8-mover is something you learn to recognise, not look up, and the lists of 10- and 12-movers are **computer only**. First the shortest alg per state:

{{alg_lengths}}

Read the 3c row as: {= ALGN('3c', 8) =} of the {= STATES('3c') =} corner 3-cycles have an 8-mover, {= ALGN('3c', 9) =} need 9 moves, and so on. And the number of different algs of each length, over all states of the type:

{{alg_counts}}

**Corner 3-cycles.**

- **About half have an 8-mover**: {= ALGN('3c', 8) =} of {= STATES('3c') =}. So at a random spot in a skeleton there is a pure comm about half the time, and that is what the per-spot count in section 8 shows.
- **Two ways or one.** Of the {= ALGN('3c', 8) =}, {= F8(2) =} have two different 8-movers and {= F8(1) =} have only one. Gezza Cubing ([[N1383]], [[N1397]]): "for most 3c cases theres 2 ways to do the commutator", then "i reckon about half of the 8 movers you can do 2 ways". It is {= F8PCT() =} of the cases that have an 8-mover. eff asked ([[N1407]]): "i feel like every 8 mover has two ways no". rogo ([[N1408]], [[N1409]]): "no", "U2, R' D R doesn't for example". That one is among the {= F8(1) =}.
- **The rest**: {= ALGN('3c', 9) =} states need a 9-mover (Ben's "1 move setup that cancels with an 8 mover like R2 D R' U2 R D' R' U2 R'", [[N5679]]), {= ALGN('3c', 10) =} need 10, {= ALGN('3c', 11) =} need 11 and {= ALGN('3c', 12) =} need 12.
- **Oriented corners.** Zagros ([[N2485]]): "There arent 8 movers if they're oriented". Jay answered with one that is ([[N2488]]): "R' F' R B2 R' F R B2". Counting them: of the {= FACT('oriented_3c') =} 3-cycles that keep all three corners oriented (U or D sticker on U or D), {= FACT('oriented_3c_with_8') =} have an 8-mover and the other {= FACT('oriented_3c') - FACT('oriented_3c_with_8') =} do not. So it is mostly true, and Jay's is one of the exceptions.
- **Cases where you can skip a spot.** Srećko ([[N4195]]): "theres a case where any single move you do doesnt give a pure comm (something like UFR UBL DFL), so you can skip one move from it". Right, and it is more than one case: {= FACT('no8_after_any_move_all_3c') =} of the {= STATES('3c') =} 3-cycles have no 8-mover and still have none after any one move. The UFR UBL DFL of the example (three corners no two of which share an edge, untwisted) is {= FACT('no8_after_any_move') =} of them, the ones whose shortest alg is 12 moves.
- **10-movers** are plenty: {= ALGS('3c', 10) =} ten-move algs against {= ALGS('3c', 8) =} eight-movers. They are, as Ben says ([[N5512]]), "sledge comms and cyclic shifts". What they buy is in 6.1.

**Twists.**

- **2tc**: nothing under 12 moves. {= ALGN('2tc', 12) =} of the {= STATES('2tc') =} cases have a 12-mover, like the tutorial's

  ```
  [F L' D2 L F', U2]   // the tutorial's two-twist
  ```

  and they're the pairs of corners that don't share an edge. The {= ALGN('2tc', '>12') =} cases with two neighbouring corners need 13 or more.
- **Twisting one corner in place.** torchlight ([[N505]]) went further: "optimal to twist one corner while preserving all edges is 12 moves", with a pure two-twist and "(R U' R U' R U2)2", which twists two corners the same way and swaps two pairs, as examples. That's right as stated. Of all move sequences of {= str(int(TW('min')) - 1) =} moves or fewer that keep every edge, none leaves a corner twisted in its place, whatever else it does to the corners. At {= TW('min') =} moves {= TW('seq') =} sequences do, reaching {= TW('states') =} states:

  | 2tc | 3c1t | kinds two comms can't solve (torchlight's second example among them) |
  |---:|---:|---:|
  | {= TW('2tc') =} | {= TW('3c1t') =} | {= TW('other') =} |

- **3tc**: no alg of 12 moves or fewer for any of the {= STATES('3tc') =} cases. The tutorial's alg and DougCube's ([[N2684]]) are {= ALGLEN('tronto_3tc') =} and {= ALGLEN('doug_3tc') =} moves, so 13 is the shortest for that case:

  ```
  U' B U' F U2 B2 D' R2 U D F' U' B   // the tutorial's
  R L U2 R' F2 L2 B L' F L' F L' B'   // DougCube's
  ```


**Double swaps.** The two kinds are told apart the way the tutorial does. A *pure* 2c2c is two swaps that each close on themselves: do it twice and all four corners are back (the tutorial's "double swap"; triple sexy and triple sledge are pure in this sense). A *twisted* 2c2c leaves a twist in each swap: do it twice and you have four twisted corners (the tutorial's "twisted double swap").

- **Pure 2c2c: the shortest alg is 10 moves.** kyh ([[N3525]]): "what's the shortest 2c2c alg". zakk drewji ([[N3526]]): "I think it’s 10?" Yes. {= ALGN('2c2c-pure', 10) =} of the {= STATES('2c2c-pure') =} cases have a 10-mover, {= ALGN('2c2c-pure', 11) =} need 11 and {= ALGN('2c2c-pure', 12) =} need 12. Here's one of the ten-movers, from the "DR algs with mnemonics" sheet that Riabov's guide links:

  ```
  R2 U' L2 D B2 R2 D' L2 U F2   // from the DR algs sheet
  ```

- **Twisted 2c2c: 12 moves** at the least, for {= ALGN('2c2c-twisted', 12) =} of {= STATES('2c2c-twisted') =} cases.
- **3c1t**: 12 at the least, and only for {= ALGN('3c1t', 12) =} of {= STATES('3c1t') =} cases. **5c**: 10 at the least, for {= ALGN('5c', 10) =} of {= STATES('5c') =}.

**Edges.**

- **Only {= EDGE8() =} of the edge 3-cycles have an alg of 8 moves or fewer** (for corners it's {= CORNER8() =}). Out of {= STATES('3e') =}:

  | 6 moves | 7 | 8 | 9 | 10 |
  |---:|---:|---:|---:|---:|
  | {= ALGN('3e', 6) =} | {= ALGN('3e', 7) =} | {= ALGN('3e', 8) =} | {= ALGN('3e', 9) =} | {= ALGN('3e', 10) =} |

  So the typical edge 3-cycle needs 9 or 10 moves. The six-movers are this one and its relatives:

  ```
  R L' U2 R' L F2   // a six-mover
  ```

- That is the whole reason edge insertions behave differently, and it is what people describe. FakeMMAP ([[N2876]]): "3e insertions have huge variance in non-DR solves." bpaul ([[N5569]]): "oh yeah the 6 move cases require eo on all axes". Exactly so: the {= EO('six', 3) =} cases with a 6-mover are the {= EO('all', 3) =} 3-cycles whose three edges are oriented on all three axes, and an alg of 8 moves or fewer needs them oriented on at least two (table in 9.2). DougCube ([[N5567]]): "when you have a fairly complete set of 3e insertion algs, then EO doesn't matter anymore". With every alg up to 12, every 3e has one; section 6.6 has what each cap costs.

**Parity.** A 2c2e leftover is not sampled in this study, but its algs were listed:

- There are {= STATES('2c2e') =} such states. argonblue ([[N6626]], [[N6628]]): "there’s only 1848 possible 2c2e states", then "oh wait actually 6x as many cases, because orientations". 1848 times 6 is {= STATES('2c2e') =}.
- **No 2c2e alg is shorter than 10 moves.** Noah Swor ([[N3120]]): "10 moves is the minimum for any 2E2C without cancellations". Right. {= ALGN('2c2e', 10) =} states have a 10-mover, {= ALGN('2c2e', 11) =} need 11, {= ALGN('2c2e', 12) =} need 12 and {= ALGN('2c2e', '>12') =} need more.
- **All {= ALGS('2c2e', 10) =} ten-move 2c2e algs are one alg**, up to turning the cube, mirroring, inverting and cyclic shifts, for example

  ```
  R' U F2 D' L D F2 U2 R U   // one of them
  ```

  notkevin ([[N3142]]): "every 10-move 2e2c is a cyclic shift of this alg or its inverse (up to rotations/mirrors ofc)". Confirmed.
- Fanti's question ([[N6624]]), "does someone know what Gods Number for 2e2c states is", stays open: it is more than 12.
