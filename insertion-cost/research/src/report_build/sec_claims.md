---

## 10. The claims, checked

Everything people said that the numbers can settle, by theme. A verdict is only as strong as what I measured: the samples are random skeletons unless the row says real ones, and *8-movers* is cap 8. Where the numbers go against a statement, or a statement says something exists, there's an example written out, under the tables or in the section named (letters in brackets).

**What a type costs**

| Claim | Who | Verdict |
|---|---|---|
| The table: 3c 5/6, 2 twisted 8, 3 twisted 9, double swap 9/10, 3c1t 10, 5c 10/11 | Tronto's tutorial, 2.4.10 | **Every corner row is within about half a move**, the 3tc the full half. 8-movers on 20-move random skeletons: {= M('3c') =}, {= M('2tc') =}, {= M('3tc') =}, {= M('2c2c-pure') =}, {= M('3c1t') =}, {= M('5c') =}. The twisted double swap, which has no row, is {= M('2c2c-twisted') =}. The skeletons people posted come out cheaper, and selection is part of that (section 9). |
| Edge 3-cycle 7 | Tronto's tutorial, 2.4.10 | **Depends on the alg list**, as its footnote says. Random skeletons: {= M('3e', L=10) =} with every alg up to 10; with 8 or fewer nothing fits on {= CELL('cost_3e', ('8', '20'), 'Nothing fits') =} of them. |
| "a optimal 3c skeleton's insertion is 6 moves on average"; "3c on average gives ~ +6"; "3C insertions are usually +6 moves" | Aneurin [[N289]]; Eli Rogers [[N4194]]; Jay [[T1918]] | **True**: {= M('3c') =} at 20 moves, {= M('3c', 16) =} at 16, {= M('3c', 26) =} at 26. |
| "5c is 10-11 moves."; "5c ~high 10" | Aneurin [[N290]]; Phuwish [[N4542]] | **True**: {= M('5c', 16) =} at 16 moves, {= M('5c') =} at 20. |
| 2tc with two insertions: "~8.0 I guess" | Phuwish [[N4532]] | **True**: {= M('2tc', 16) =} at 16 moves, {= M('2tc') =} at 20. |
| 3tc: "mid to high 8", "a half to a move worse" than a 2tc | Phuwish [[N4537]] | **Higher with pure comms**: {= M('3tc') =} at 20 moves, {= DIFF('3tc', '2tc') =} worse than a 2tc. With algs up to 12 it is {= M('3tc', L=12, src='two12') =} ({= NSK('3tc', L=12, src='two12') =} skeletons), so the alg list can explain the figure. |
| "more like 9 for pure 2-2", "like 9.5 for 2-2 with a twist", "like 10 for 3c1t" | cpaul [[N4857]], [[N4858]], [[N4859]] | **9 and 10 are right** ({= M('2c2c-pure') =}, {= M('3c1t') =}). **Which 2c2c is cheaper depends on the alg length**: with 8-movers the twisted one ({= M('2c2c-twisted') =}); with algs up to 10 the pure one ({= M('2c2c-pure', L=10) =} against {= M('2c2c-twisted', L=10) =}, 500 skeletons each), which is cpaul's order. |
| "5-6, 8-9, 6-8 for good 2c2c, 8-9 for bad 2c2c"; "this is i expected not avg expected" | Baiqiang [[N4853]], [[N4863]] | **Not averages, in Baiqiang's words.** Which 2c2c is the good one was asked (kyh, [[N4855]]) and not answered. With algs up to 12 on {= NSK('2c2c-pure', L=12, src='two12') =} random 20-move skeletons each: pure 2c2c {= M('2c2c-pure', L=12, src='two12') =}, twisted {= M('2c2c-twisted', L=12, src='two12') =}, 3c1t {= M('3c1t', L=12, src='two12') =}. Posted skeletons with a comm plus an alg at cap 12: 2c2c {= CELL('real_mixed', '2c2c (pure or twisted)', 'Cap 12') =}, 3c1t {= CELL('real_mixed', '3c1t', 'Cap 12') =} (9.2). |
| "i think 3c1t > 2c2c > 5c" | argonblue [[N6507]] | **By cost the first two are the other way round**: 2c2c, then 3c1t, then 5c. A 2c2c is {= DIFF('3c1t', '2c2c-pure') =} to {= DIFF('3c1t', '2c2c-twisted') =} cheaper than a 3c1t [a]. |
| "i didn't notice a meaningful different between 2 insertion 4c types" | Jay [[N4860]] | **There is one on average**: about a move between a 2c2c and a 3c1t, with a spread from skeleton to skeleton that is wider than that, so it is hard to notice solve by solve [a]. |
| "maybe there's some non 3c type insertion method for 2c2c that lowers the movecount that far" | Jay [[N4860]] | **There is**: the 10-move 2c2c algs. A pure 2c2c averages {= M('2c2c-pure', L=10) =} with algs of up to 10 moves ({= NSK('2c2c-pure', L=10) =} skeletons) and {= M('2c2c-pure', L=12, src='two12') =} up to 12 ({= NSK('2c2c-pure', L=12, src='two12') =}), against {= M('2c2c-pure') =} with 8-movers. |
| "Why is there even a difference if the number of possible first insertions is the same tbh" | wen [[N4862]], asking | **Answered both ways it can be read.** The two kinds of 2c2c: the number is the same, {= FC('2c2c-pure') =} first comms per spot each, and they cost the same when the two comms do not touch ({= CELL('nesting', 'pure 2c2c', 'The two not touching') =} and {= CELL('nesting', 'twisted 2c2c', 'The two not touching') =}); the {= GAP2C2C('Two comms, nesting allowed') =} between them comes from comms that interact, {= GAP2C2CNEST() =} of it from nesting. A 2c2c against a 3c1t or a 5c: the number is not the same, {= FC('2c2c-pure') =} against {= FC('3c1t') =} against {= FC('5c') =} (6.2). |
| "getting +9 from 2tc is as bad as +11,+12 from 5c" | Phuwish [[N4535]] | **About right**: +9 or worse on {= WORSE('2tc', 9) =} of 2tc skeletons, +12 or worse on {= WORSE('5c', 12) =} of 5c skeletons. |
| For two corner insertions "the average is 13 moves for me, one 8-2 and one 8-1"; "you can usually do a bit better with 5c" | Zagros [[N1164]]; Java [[N1165]] | **Java is right**: the best is {= M('5c') =} on average, and +13 or worse is the best there is on only {= WORSE('5c', 13) =} of 20-move 5c skeletons. |
| "8-4 8-4 is soooooooo lucky tho", "for a 15 move skeleton" | alkamaass [[N1219]], [[N1220]] | **Yes**: +8 or better on {= P('5c', 8, 14) =} of 14-move and {= P('5c', 8, 16) =} of 16-move 5c skeletons. |

**Which skeleton**

| Claim | Who | Verdict |
|---|---|---|
| A 5c should be "maybe like 5-6" shorter than a 3c | asacuber [[N1325]] | **5 is break-even**: {= EXM('5c', 20) =} against a 20-move 3c by expected total, {= EXR('5c') =} for equal chance of a target (7.2). |
| 3c in 23: sub-30 "you will probably get it"; in 25 "you will need some luck" | Tronto's tutorial, 2.4.10 | **Right**: {= CH('3c', 23, 29) =} and {= CH('3c', 25, 29) =}. |
| "a skeleton leaving 4 corner in 18 moves is probably better than one leaving 3 corners in 25" | Tronto's tutorial, 2.4.10 | **Right, by about {= f1(float(TOTAL('3c', 25)) - float(TOTAL('3c1t', 18))) =} moves or more** in expected total. |
| "3c in 22-24 or 5c in 16-18"; "18 to anything like 5c, 4c, 3c1t, and 24 for 3c" | Gezza Cubing [[N1740]]; oliynykmax [[N1741]] | **The 5c end is the better one**: sub-30 from a 5c in 18 {= CH('5c', 18, 29) =}, from a 3c in 24 {= CH('3c', 24, 29) =}. |
| "sub-22 for 3C skeleton", "sub-20 for every other skeleton" | sequesteredcuber [[N292]] | **Uneven**: sub-30 from a 3c in 21 {= CH('3c', 21, 29) =}, from a 5c in 19 {= CH('5c', 19, 29) =}, from a pure 2c2c in 19 {= CH('2c2c-pure', 19, 29) =} [g]. |
| 21 to 3c: "a guaranteed 29 right?"; "not strictly guaranteed", "but it's very likely" | 2023HAMI08 [[N4836]]; kyh [[N4837]], [[N4838]] | **kyh is right**: {= CH('3c', 21, 29) =} with 8-movers [h]. |
| For sub-35: "get to 3c in 28 or 4c/5c in 22" | trangium [[D17624]] | **Both work; the 5c in 22 is the safer**: {= CH('5c', 22, 34) =} against {= CH('3c', 28, 34) =}. |
| "the chance ur cancelling 4 moves or more is not that high" | kyh [[N4186]] | **True**: {= GE('24', 4) =} of 24-move 3c skeletons. |

**Cancelling and searching**

| Claim | Who | Verdict |
|---|---|---|
| "8 move commutators cancel less moves on average on DR skeletons compared to regular ones, although we don’t think this has been proved yet"; "after DR you often get something like 8-1" | Fokianos and Raposio's DR guide, 5.1; trig0n [[D1572]] | **A little, in a model**: on modelled 17-move DR skeletons a 3c costs {= CELL('dr17', ('EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave', '8'), 'Mean added') =} with 8-movers against {= CELL('dr17', ('random moves', '8'), 'Mean added') =} on random ones, because of which corners a DR leaves (6.1). Real DR skeletons were not sampled. |
| "usually you should at least be able to cancel like 2 moves for each comm" | Gezza Cubing [[N1388]] | **True for a 3c**: 8-2 or better on {= GE('20', 2) =} of 20-move skeletons. |
| "In my stats, I found that the best insertion points tend to be in the first 1/3 or last 1/3 of the skel." | DougCube [[N6409]] | **Not reproduced**: not on random skeletons (a third each, 8.1){= REALTHIRDS() =} |
| Near either end "you have less chances to find a 8-6 or better" | paulduc03 [[N6411]] | **True for the first and last spot**, and a little for the next one in (8.1). |
| "It happens extremely rarely that the best insertion is given by a 9 move commutator (or longer)" | Tronto's tutorial, 2.4.1 | **Right for 9-movers** (the best on {= CELL('one_longer', '20', 'A 9-mover beats every 8-mover and no 10-mover beats it') =} of 20-move skeletons). **A 10-mover is the only best on {= CELL('one_longer', '20', 'A 10-mover beats every 8- and 9-mover') =}** [b], by a single move {= CELL('one_longer', '20', 'When a 10-mover beats every 8- and 9-mover: by one move only') =} of the time. |
| "if its a setup to a regular comm then it wont cancel more than just inserting 8 movers" | Ben [[N5510]] | **True on all but {= fmt(FACT('ten_wins_only_conjugates'), FACT('ten_sample')) =} of 20-move skeletons.** Where the setup cancels a whole move it is the 8-mover one spot over. On {= FACT('ten_wins_only_conjugates') =} of {= FACTN('ten_sample') =} skeletons a setup-type 10-mover is the only best, by one move: its setup joins a turn of the skeleton, which is the 8-mover put inside that turn [i]. |
| Checking every other move "still guarantees you'll find" a -3 or better; "this isn't thorough tho" | notkevin [[N4772]]; alkamaass [[N1144]] | **Almost**: a best of 8-3 or better is found {= CELL('one_skip', '20', 'Best is 8-3 or better: every other move finds it') =} of the time on a 20-move 3c. Those misses are all next to two opposite-face moves [c]. Nothing better than an {= SKIPWORST() =} was missed on any of {= SKIPTOTAL() =} skeletons. |
| Every third spot instead of every other | tested here | **It does not work**: an 8-3 or better is found {= CELL('one_skip', '20', 'Best is 8-3 or better: every third move finds it') =} of the time on a 20-move 3c [j]. |
| When the case at a spot needs 10 moves, "can I go 3 moves further instead of 2 and still make sur not to miss any insertion below 6 moves ?"; "I don't think that works." | paulduc03 [[N5145]], asking; DougCube [[N5147]] | **DougCube is right**: two spots on from such a spot there is an 8-3 or better {= TSP(20, 'two', 'ten') =} of the time on a 20-move 3c, and all {= FACT('ten_cases') =} cases that need 10 moves can have an 8-mover two moves later [k]. |
| "for the first 5c insertion you have 5x more options than for the second"; "there are 5 possible cycles, not 1" | Not officially a David [[N139]]; Zagros [[N3688]] | **True**: {= FC('5c') =} 3-cycles per spot leave a 3c. |
| For a 5c "you'll probably have at least an 8-3 or 8-4 for the first one" | Ben [[N5538]] | {= GV('first83') =} |
| "my pr single wouldve been a 30 if i didnt go look for sub optimal first insertions", "but its a 28"; "i just had to check a suboptimal first insertion (8-2 instead of 8-3) to get any cancellations in the second" | kyh [[N5837]], [[N5838]]; argonblue [[N5842]] | {= GV('subopt') =} |
| "if you set greedy to 0 and only pick regular 3c comms then it basically shows human findable"; "greedy 1 is still reasonable if your skeleton is really good but anything higher isn't imo"; "i think 1 is realistic" | Ben [[N5683]], [[N5688]]; kyh [[N5836]] | {= GV('greedy') =} |
| With more algs at greedy 0 Insertion Finder gives a worse result; "if 10-5 is the best first insertion it won’t find the optimals with a worse first insertion" | bvcuber13 [[N5819]], [[N5821]]; tave_789 [[N5825]]; Ben [[N6705]] | {= GV('morealgs') =} |
| An insertion can cancel more than its own length | Zagros [[N3697]]; DougCube [[N3696]] "true but highly unlikely" | **True, and rare**: the best 8-mover insertion shortens the skeleton on {= NEGSHARE() =} of 20-move 3c skeletons [d]. |
| "i thought it wasn't possible to nest 3c comms that are parts of a 5-cycle, but insertion finder apparently did it for one of my skeletons (improving it by 1 move)?" | argonblue [[N5530]] | **What argonblue found is common**: the best pair is nested on {= CELL('nesting', '5c', 'Best needs nesting') =} of 20-move 5c skeletons with 8-movers [e]. |
| "IF supposed that the status of the cube becomes better after any insertion. so it won't work in this case"; then, having asked Yan Xuan, "this should be supported but somehow it doesn't" | Baiqiang [[D3799]], [[D3804]] | **This search has the same limit.** alkamaass's 8-move comm that turns an 18-move 3c1t into a 16-move 3c1t is a third insertion, outside both (9.5). |

**Algs and counts** (sections 4 and 5)

| Claim | Who | Verdict |
|---|---|---|
| Which leftovers take one, two or more comms | Riabov's guide; Tronto's tutorial 2.4.4, 2.4.5 | **All right**, proved in Lean (section 4). |
| "the only way to affect 5 corners with 2 3-cycles, is to do a 5-cycle" | FakeMMAP [[N5307]] | **True.** |
| A mixed 3c3c "cannot be solved with only two 3c comms" | DougCube [[N5328]] | **True**, it takes three. |
| "theres 4 types of 7c that work"; "I counted your last one as 2 separate" | wen [[N393]], [[N396]], to torchlight's list of three [[N394]] | **True**, counted wen's way: exactly four leftovers on seven corners take three comms. |
| "for most 3c cases theres 2 ways to do the commutator"; "about half of the 8 movers you can do 2 ways" | Gezza Cubing [[N1383]], [[N1397]] | **{= F8(2) =} have two, {= F8(1) =} have one, {= F8(0) =} have none.** |
| "i feel like every 8 mover has two ways no"; "no", "U2, R' D R doesn't for example" | eff [[N1407]], asking; rogo [[N1408]], [[N1409]] | **rogo is right**: `[U2, R' D R]` is one of the {= F8(1) =} with a single 8-mover. |
| "There arent 8 movers if they're oriented" | Zagros [[N2485]] | **Mostly**: {= FACT('oriented_3c_with_8') =} of the {= FACT('oriented_3c') =} oriented 3-cycles have one. Jay's `R' F' R B2 R' F R B2` ([[N2488]]) is one of them. |
| A case where no single move gives a pure comm, "so you can skip one move from it" | Srećko [[N4195]] | **True** for {= FACT('no8_after_any_move_all_3c') =} of the {= STATES('3c') =} 3-cycles. |
| "optimal to twist one corner while preserving all edges is 12 moves" | torchlight [[N505]] | **True as stated**: no sequence of {= str(int(TW('min')) - 1) =} moves or fewer that keeps every edge leaves a corner twisted in its place, whatever else it does; {= TW('seq') =} sequences of {= TW('min') =} moves do (section 5). |
| "what's the shortest 2c2c alg", "I think it’s 10?" | kyh [[N3525]], zakk drewji [[N3526]] | **10**, for a pure 2c2c. 12 for a twisted one. |
| "10 moves is the minimum for any 2E2C without cancellations" | Noah Swor [[N3120]] | **True.** |
| "every 10-move 2e2c is a cyclic shift of this alg or its inverse (up to rotations/mirrors ofc)" | notkevin [[N3142]] | **True**: {= ALGS('2c2e', 10) =} sequences, one class. |
| "there’s only 1848 possible 2c2e states", "6x as many cases, because orientations" | argonblue [[N6626]], [[N6628]] | **True**: {= STATES('2c2e') =}. |

The examples:

**[a]** A typical skeleton of each of the three 4-corner types, 20 moves, 8-movers: each costs what its type costs on average, rounded. They're there to show what the averages look like on a cube. One skeleton of each proves nothing about the order; the tables of 6.2 do that.

{{WIT_TYPICAL_2C2C_TWISTED}}

{{WIT_TYPICAL_2C2C_PURE}}

{{WIT_TYPICAL_3C1T}}

**[b]** A 10-mover that beats every 8-mover and every 9-mover:

{{WIT_TEN}}

**[c]** is the skeleton of 8.3 where every other move misses the only 8-3.

**[d]** An 8-move comm that makes the skeleton shorter:

{{WIT_NEGATIVE}}

**[e]** A 5c whose best pair of comms is nested:

{{WIT_NESTED}}

**[f]** is the skeleton of 8.4 where the best first comm is the wrong one to follow.

**[g]** is the 19-move 5c of 7.3 that gives 30, and **[h]** the 21-move 3c of 7.3 that does not give 29.

**[i]** is the skeleton of 8.2 where a setup-type 10-mover is the only best.

**[j]** and **[k]** are the skeletons of 8.3 where every third spot, and three spots on after a 10-move case, miss the only 8-3.

**[l]** is the skeleton of 8.4 where greedy 0 gives a longer result with more algs.

---

## 11. What this does not cover

- **Findability and time.** Every number is the best insertion that exists for its cap, the answer key. How often you find it in the time left isn't measured anywhere here. What people say about time: Tronto, "A single 3c insertion usually takes me about 5 minutes"; DougCube ([[N4159]]): "I find 3c in under 3 mins and 5c in under 10 mins now."
- **Random skeletons are move sequences, not solves.** No blocks, no EO, no last-layer alg at the end. The same real move sequences with a random leftover on them cost what random sequences cost, but the skeletons people post come out most of a move cheaper with 8-movers. Selection is part of that, and how much of the rest is real these skeletons can't say (9.2). The posted 3e skeletons are far cheaper than the random tables, and how their edges are oriented doesn't explain it.
- **Small samples at the long caps.**

  | Model | Sample |
  |---|---|
  | two comms at cap 10 | 200 to 2,000 skeletons per length |
  | a comm plus an alg | 200 skeletons of 20 moves |
  | two comms at cap 12 | 100 |

  Two standard errors of a mean are ±{= SE2('5c', L=10) =} for a 5c at cap 10 and ±{= SE2('5c', L=12, src='two12') =} at cap 12 (Appendix C). Enough for a mean, not for the rare outcomes.
- **Parity and mixed leftovers.** 2c2e, 3e3c, 2e2e with corners, and everything else with both corners and edges left, are not sampled. Their algs are only counted for 2c2e (section 5).
- **Leftovers that need three comms** (2c2c1t, 3c2t, 7c and the rest of section 4): counted, not costed.
- **More than two insertions on a two-comm leftover.** A comm that leaves the same kind of leftover but shortens the skeleton, like the 8-10 of section 9.5, is a third insertion and isn't searched.
- **Insertions inside a turn.** Every spot searched is between two moves of the skeleton. An alg put in the middle of a turn (a `B'` done as `B2`, the comm, `B`) is found only when a longer alg within the cap happens to equal it (8.2).
- **Algs longer than 12 moves**, so no 3tc alg and no two-twist of neighbouring corners in one piece, and the 13-move algs people do insert.
- **Slice insertions, centre insertions, real DR skeletons.** The DR rows of 6.1 are modelled move sequences. Whether 8-move comms cancel less on skeletons from real DR solves, the question in the Fokianos and Raposio guide, is answered here only for that model.
