---

## 6. What each type costs

How to read the tables of this section. A row is one skeleton length. *Mean added* is the average of what the best insertion adds, over the skeletons where something fits. The columns *k or less* are the share of all skeletons whose best insertion adds k moves or fewer. *Nothing fits* is the share with no alg within the cap at any spot. Everything is for random skeletons (section 3), and the first column is the cap. The cap-8 rows are what checking every spot with 8-movers gives, a target for the attempt; the cap-10 and cap-12 rows count every alg of that length and are **computer only**, the answer key for a full alg list.

### 6.1 A 3c

**3c: one comm. Random skeletons, 20,000 per row. Cap 8 is 8-movers only; caps 10 and 12 allow every alg up to that length.**

{{cost_3c}}

- **+{= M('3c') =} at 20 moves with 8-movers.** Everybody's +6 (Aneurin, Jay, Eli Rogers, Baiqiang's 5-6, Tronto's 5/6) is the right number. Share of skeletons that give:

  | +6 or better | +5 or better | +4 or better | +3 or better |
  |---:|---:|---:|---:|
  | {= CELL('cost_3c', ('8', '20'), '6 or less') =} | {= CELL('cost_3c', ('8', '20'), '5 or less') =} | {= CELL('cost_3c', ('8', '20'), '4 or less') =} | {= CELL('cost_3c', ('8', '20'), '3 or less') =} |

- **Length matters, slowly.** From {= CELL('cost_3c', ('8', '10'), 'Mean added') =} at 10 moves to {= CELL('cost_3c', ('8', '30'), 'Mean added') =} at 30: ten more moves of skeleton take {= PERTEN('3c') =} off the insertion. That's the tutorial's "longer skeletons give more spots where you can insert an algorithm, and so better chance of cancellations", in numbers. The tutorial adds "but you shouldn’t choose a long skeleton instead of a short one because of this!", and the number agrees: ten moves of skeleton buy less than half a move of insertion.
- **zakk drewji's 24 to 3c**: DougCube's "typically a (8-2/30)" ([[N3243]]) is the single most likely outcome, {= EXACT('3c', 24, 6) =} of skeletons. {= CH('3c', 24, 30) =} get 30 or better and {= CH('3c', 24, 28) =} get 28 or better.
- **No 8-mover at all** is rare but real: {= CELL('cost_3c', ('8', '20'), 'Nothing fits') =} of 20-move skeletons and {= CELL('cost_3c', ('8', '10'), 'Nothing fits') =} of 10-move ones have no spot where an 8-mover solves the three corners (one is written out below). That is the 19-move skeleton of [[N4549]] ("its not even an 8-0 its an 9-0"). An 8-0 as the best there is: {= CELL('one_cancel', '20', '8-0') =} at 20 moves.
- **Longer algs give little on a 3c**: {= CELL('cost_3c', ('10', '20'), 'Mean added') =} at cap 10 and {= CELL('cost_3c', ('12', '20'), 'Mean added') =} at cap 12, against {= CELL('cost_3c', ('8', '20'), 'Mean added') =}. Section 8.2 has how often a longer alg is the best.

A 20-move skeleton with no 8-mover at any spot:

{{WIT_NO8}}

**trig0n's question, 17 to 3c, all three versions.** trig0n asked ([[T73]]) for the chance of a ≤x-move insertion with "Random" moves, with "EO in 5, then random moves which don't break EO", and with "EO in 4, DR in 10, then DR moves". The three are modelled as move sequences, not solved: 17 random moves; 5 random moves and then 12 without quarter turns of F or B; 4 random moves, 6 without quarter turns of F or B, and 7 moves of the DR group. The 3c is random, except in the last pair of rows, where it is one of the {= FACT('oriented_3c') =} 3-cycles that DR moves can leave (all three corners keep their U or D sticker on U or D). 20,000 skeletons each.

{{dr17}}

- **Random moves**: +5 or better {= CELL('dr17', ('random moves', '8'), '5 or less') =}, +6 or better {= CELL('dr17', ('random moves', '8'), '6 or less') =}, +7 or better {= CELL('dr17', ('random moves', '8'), '7 or less') =} with 8-movers.
- **Keeping EO changes nothing**, and DR moves by themselves change next to nothing ({= CELL('dr17', ('EO in 4, DR in 10, then DR moves; any 3c', '8'), 'Mean added') =} against {= CELL('dr17', ('random moves', '8'), 'Mean added') =}).
- **What a DR leaves does matter, a little**: with a 3c that DR moves can leave, 8-movers give {= CELL('dr17', ('EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave', '8'), 'Mean added') =}, +6 or better only {= CELL('dr17', ('EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave', '8'), '6 or less') =} of the time, and no 8-mover anywhere on {= CELL('dr17', ('EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave', '8'), 'Nothing fits') =}. Oriented corners have few 8-movers (section 5). With 10-movers the gap nearly closes ({= CELL('dr17', ('EO in 4, DR in 10, then DR moves; a 3c that DR moves can leave', '10'), 'Mean added') =} against {= CELL('dr17', ('random moves', '10'), 'Mean added') =}).
- That is the old line in the Fokianos and Raposio guide, "there is the feeling that 8 move commutators cancel less moves on average on DR skeletons compared to regular ones, although we don’t think this has been proved yet", and trig0n's "after DR you often get something like 8-1" ([[D1572]]): in this model it is true, by {= DRGAP() =} of a move, and it comes from which corners are left, not from the moves. These are modelled skeletons, not DR solves; a real DR skeleton may differ.

### 6.2 Two comms: 2tc, 2c2c, 3tc, 3c1t, 5c

For these, cap 8 means two 8-move comms, the second allowed inside the first; no alg of 8 moves or fewer does any of them in one go.

Each number is the **best pair**, every first comm at every spot followed by the best second: **computer only** as a search. By hand you take the best first comm and then the best second, which costs {= f2(float(CELL('greedy', '5c', 'Best first comm only')) - float(CELL('greedy', '5c', 'Best pair of comms'))) =} more on a 5c; also following the first comms a move worse gets within {= f2(max(float(CELL('greedy', r, 'First comms within 1 move')) - float(CELL('greedy', r, 'Best pair of comms')) for r in ('2tc', '3tc', 'pure 2c2c', 'twisted 2c2c', '3c1t', '5c', '3c3c'))) =} of the best pair on every type (8.4). So read the cap-8 rows as a careful hand search, a few hundredths optimistic.

Cap 10 is the best of two comms of up to 10 moves and one alg of up to 10 for the whole leftover. All on random skeletons; the *Skeletons* column says how many each row rests on, and at cap 10 that is few, so read those rows to the nearest percent or so.

**2tc** (two corners twisted in place):

{{cost_2tc}}

**Twisted 2c2c:**

{{cost_2c2c-twisted}}

**Pure 2c2c:**

{{cost_2c2c-pure}}

**3tc** (three corners twisted the same way):

{{cost_3tc}}

**3c1t:**

{{cost_3c1t}}

**5c:**

{{cost_5c}}

**Mean added on random skeletons, next to what was estimated. Every computed cell has the number of skeletons behind it in brackets. *not run*: cap 12 with two comms was not run for a 2tc.**

{{estimates}}

The cap-12 column is on {= NSK('5c', L=12, src='two12') =} skeletons that are not the skeletons of the cap-8 column, so do not read a step off this table: those {= NSK('5c', L=12, src='two12') =} 5c skeletons average {= PAIR('5c', '8') =} with 8-movers, not {= M('5c') =}. The table of 6.3 has every cap on the same skeletons.

- **The tutorial's table holds up.** Every corner row is within about half a move of the 20-move, 8-mover column; the 3tc is the one a full half move off (9 against {= M('3tc') =}). Where the table gives a range (double swap 9/10, 5c 10/11) the computed mean sits at the low end, and shorter skeletons, which is what a 4c or 5c skeleton usually is, sit higher. Its 9/10 is the row "4 Corners (double swap)"; the twisted double swap has no row.
- **cpaul's 9 and 10 are right, and which 2c2c is the cheaper one depends on the alg length.** Pure 2c2c {= M('2c2c-pure') =}, 3c1t {= M('3c1t') =} at 20 moves. With 8-movers alone a twisted 2c2c costs {= M('2c2c-twisted') =}, less than a pure one. With algs of up to 10 moves it is the other way round, pure {= M('2c2c-pure', L=10) =} and twisted {= M('2c2c-twisted', L=10) =} (500 skeletons each), which is the order cpaul gave ("9 for pure 2-2", "9.5 for 2-2 with a twist", reading "with a twist" as the twisted double swap): a pure 2c2c has 10-move algs and a twisted one has none under 12.
- **Phuwish's numbers are close.**
  - 2tc "~8.0 I guess" ([[N4532]]) against {= M('2tc') =}.
  - 5c "~high 10" ([[N4542]]) against {= M('5c', 16) =} at 16 moves and {= M('5c') =} at 20.
  - tave_789's "close to 9.5?" for a 3c1t and a 2c2c ([[N4539]]), which Phuwish answered "yeah" ([[N4540]]), against {= M('3c1t') =} and {= M('2c2c-twisted') =} to {= M('2c2c-pure') =}.
  - The 3tc, "mid to high 8 from my experience" ([[N4537]]), is lower than 8-movers give on random skeletons ({= M('3tc') =}), and "a half to a move worse" than a 2tc is {= DIFF('3tc', '2tc') =} worse here. With algs up to 12 a 3tc comes to {= M('3tc', L=12, src='two12') =} on {= NSK('3tc', L=12, src='two12') =} skeletons, so the figure is reachable; it just takes more than pure comms.
- **Baiqiang's are not averages**, in Baiqiang's own words ([[N4863]]: "this is i expected not avg expected"). kyh asked which 2c2c is the good one ([[N4855]]) and nobody answered, so I don't pin the two figures on pure and twisted here.

  What the numbers give: with every alg of up to 12 moves a pure 2c2c averages {= M('2c2c-pure', L=12, src='two12') =} and a twisted one {= M('2c2c-twisted', L=12, src='two12') =} on {= NSK('2c2c-pure', L=12, src='two12') =} random skeletons of 20 moves each, figures of the size of "6-8" and "8-9" ([[N4853]]). Jay guessed as much in the same exchange ([[N4860]]): "maybe there's some non 3c type insertion method for 2c2c that lowers the movecount that far". The 10-move 2c2c algs are one such method: with algs of up to 10 moves a pure 2c2c is already at {= M('2c2c-pure', L=10) =} ({= NSK('2c2c-pure', L=10) =} skeletons). 

  A 3c1t averages {= M('3c1t', L=12, src='two12') =} at cap 12, above the 8-9. On the skeletons people posted a 3c1t averages {= POSTEDM('3c1t') =} with 8-movers alone ({= POSTED('3c1t') =} skeletons, section 9), which is inside it.
- **The order** at cap 8 is 2tc, twisted 2c2c, pure 2c2c, 3tc, 3c1t, 5c. argonblue's "i think 3c1t > 2c2c > 5c" ([[N6507]]) has the first two the other way round by cost: a 2c2c is {= DIFF('3c1t', '2c2c-pure') =} to {= DIFF('3c1t', '2c2c-twisted') =} cheaper than a 3c1t. jisu101's reply ([[N6508]], [[N6509]]: "you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions") is the reason, see below. And the difference Jay "didn't notice" between the "2 insertion 4c types" ([[N4860]]) is about a move on average: {= M('2c2c-twisted') =}, {= M('2c2c-pure') =}, {= M('3c1t') =}. The spread from one skeleton to the next is wider than that, so it is hard to notice solve by solve. Section 10 has a typical skeleton of each of the three (example [a]).
- **"getting +9 from 2tc is as bad as +11,+12 from 5c"** (Phuwish, [[N4535]]) is right in odds: +9 or worse happens on {= WORSE('2tc', 9) =} of 2tc skeletons, +11 or worse on {= WORSE('5c', 11) =} of 5c skeletons and +12 or worse on {= WORSE('5c', 12) =}.

**Why the types differ.** Four minutes after Jay's remark on the "2 insertion 4c types", wen asked ([[N4862]]): "Why is there even a difference if the number of possible first insertions is the same tbh". You can read that as about the two kinds of 2c2c or about a 2c2c against a 3c1t, so here's the count for every type. At one spot of the skeleton the first comm can be any 3-cycle that leaves a 3c behind. How many of those there are, and how many 8-move comms that gives per spot on average:

**The first comm of a two-comm leftover: 3-cycles that leave a 3c, per spot, and how many 8-move comms that is on average over the spots of {= GN('2tc') =} random 20-move skeletons per type ({= GN('5c') =} for a 5c).**

{{first_choices}}

- **For the two kinds of 2c2c the number is the same**, {= FC('2c2c-pure') =} each: any three of the four corners, either direction (jisu101's point, [[N6508]], [[N6509]]), with three ways to twist. They still cost {= M('2c2c-twisted') =} and {= M('2c2c-pure') =} with 8-movers, and the {= GAP2C2C('Two comms, nesting allowed') =} between them comes from comms that interact. When the two comms do not touch, a pure and a twisted 2c2c cost the same, {= CELL('nesting', 'pure 2c2c', 'The two not touching') =} and {= CELL('nesting', 'twisted 2c2c', 'The two not touching') =} (6.5). With nesting forbidden the twisted one is {= GAP2C2C('No nesting') =} cheaper ({= CELL('nesting', 'twisted 2c2c', 'No nesting') =} against {= CELL('nesting', 'pure 2c2c', 'No nesting') =}): its second comm cancels into the first more often without sitting inside it. Nesting is the other {= GAP2C2CNEST() =}: the best pair is nested on {= CELL('nesting', 'twisted 2c2c', 'Best needs nesting') =} of twisted 2c2c skeletons and {= CELL('nesting', 'pure 2c2c', 'Best needs nesting') =} of pure ones.
- **Across types it isn't the same.** More choices for the first comm means better odds of a good one, and the costs come in that order:

  | | 2tc | 2c2c | 3tc | 3c1t | 5c | 3c3c |
  |---|---:|---:|---:|---:|---:|---:|
  | First comms per spot | {= FC('2tc') =} | {= FC('2c2c-pure') =} | {= FC('3tc') =} | {= FC('3c1t') =} | {= FC('5c') =} | {= FC('3c3c') =} |
  | Mean added | {= M('2tc') =} | {= M('2c2c-twisted') =} and {= M('2c2c-pure') =} | {= M('3tc') =} | {= M('3c1t') =} | {= M('5c') =} | {= M('3c3c') =} |


### 6.3 What a longer alg list is worth

At 20 moves, the mean added under each cap. Caps 10 and 12 are every alg of that length, **computer only**: read them as what learning more algs could buy at most, not as a search to run in an attempt. First with each cap on its own sample:

**Mean added, random skeletons of 20 moves, by cap. Each *Skeletons* column is the number of skeletons behind the number to its left. At cap 8 the mean is over the skeletons where something fits, and the first column says on how many that is; at caps 10 and 12 something fits on every skeleton. *not run*: cap 12 with two comms was not run for that leftover.**

{{caps}}

The samples differ in size and are not the same skeletons: the {= NSK('5c', L=12, src='two12') =} 5c skeletons of the cap-12 column average {= PAIR('5c', '8') =} with 8-movers, not {= M('5c') =}, so {= M('5c') =} to {= M('5c', L=12, src='two12') =} overstates the step. For the step from one cap to the next the fair comparison is on the same skeletons:

**The same skeletons under every cap (the first 100 or 200 of the 20-move sample).**

{{caps_paired}}

- **3c**: 8 to 10 is worth {= PAIRD('3c', '8', '10') =}, 10 to 12 another {= PAIRD('3c', '10', '12') =} on these {= PAIRN('3c') =}; on the full 20,000 it is {= DIFFL('3c', 8, 10) =} and {= DIFFL('3c', 10, 12) =}. Not much.
- **5c**: {= M('5c') =} with 8-movers, {= M('5c', L=10) =} at cap 10 ({= NSK('5c', L=10) =} skeletons). On the same {= PAIRN('5c') =} skeletons: {= PAIR('5c', '8') =}, {= PAIR('5c', '10') =}, {= PAIR('5c', '12') =}.
- **Pure 2c2c gains the most**: {= PAIR('2c2c-pure', '8') =}, {= PAIR('2c2c-pure', '10') =}, {= PAIR('2c2c-pure', '12') =} on the same {= PAIRN('2c2c-pure') =}. The 10-move 2c2c algs are worth learning if you take 2c2c skeletons.
- **Twisted 2c2c, 3c1t, 3tc** gain little at 10, where nothing is new for them but longer comms, and more at 12: a 3tc goes from {= PAIR('3tc', '10') =} to {= PAIR('3tc', '12') =} on these {= PAIRN('3tc') =} skeletons, all of it from longer comms, since it has no alg of 12 moves or fewer.
- **A comm plus an alg** (the column *Cap 10 with a comm plus an alg*) is worth another {= PAIRD('5c', '10', '10m') =} on a 5c and {= PAIRD('2c2c-pure', '10', '10m') =} on a pure 2c2c at cap 10. That is a 5c done as a 3c comm and a 2c2c alg, the kind of line Insertion Finder returns with all its sets on.

These are averages over {= PAIRN('5c') =} or {= PAIRN('3c') =} skeletons, compared on the same skeletons, so the direction of each step is solid. For its size: two standard errors of a mean are ±{= SE2('5c', L=12, src='two12') =} for a 5c at cap 12 on {= NSK('5c', L=12, src='two12') =} skeletons (Appendix C).

### 6.4 One alg for the whole leftover

**One alg for the whole leftover, random skeletons of 20 moves (*Skeletons*: the sample). How often an alg within the cap fits at some spot, what it adds on the skeletons where it fits, and what two 8-move comms add on those same skeletons (for the edge rows: two 3e algs of 8 moves or fewer, which do not always fit).**

{{direct}}

- **Pure 2c2c**: a 10-move alg fits somewhere on {= CELL('direct', 'pure 2c2c', 'Alg of 10 or less: fits somewhere') =} of skeletons and then costs {= CELL('direct', 'pure 2c2c', 'Alg of 10 or less: mean added') =}. Two 8-move comms cost {= CELL('direct', 'pure 2c2c', 'Two 8-move comms on the skeletons where an alg of 10 or less fits') =} on those same skeletons ({= M('2c2c-pure') =} over all of them), so where it fits the alg is {= f2(float(CELL('direct', 'pure 2c2c', 'Two 8-move comms on the skeletons where an alg of 10 or less fits')) - float(CELL('direct', 'pure 2c2c', 'Alg of 10 or less: mean added'))) =} better.
- **2tc**: the 12-move two-twist is there on every skeleton, and costs {= CELL('direct', '2tc', 'Alg of 12 or less: mean added') =}. Two comms cost {= CELL('direct', '2tc', 'Two 8-move comms on the skeletons where an alg of 12 or less fits') =}. The tutorial already says of the 2tc and 3tc algs: "But this is usually not the best way". For the 2tc it is worse by {= f2(float(CELL('direct', '2tc', 'Alg of 12 or less: mean added')) - float(CELL('direct', '2tc', 'Two 8-move comms on the skeletons where an alg of 12 or less fits'))) =}.
- **5c, 3c1t**: one alg of up to 12 moves alone is no better than two 8-move comms on the skeletons where it fits ({= CELL('direct', '5c', 'Alg of 12 or less: mean added') =} against {= CELL('direct', '5c', 'Two 8-move comms on the skeletons where an alg of 12 or less fits') =} for a 5c, {= CELL('direct', '3c1t', 'Alg of 12 or less: mean added') =} against {= CELL('direct', '3c1t', 'Two 8-move comms on the skeletons where an alg of 12 or less fits') =} for a 3c1t), but on some skeletons it is the best, which is where the gain of 6.3 comes from.

### 6.5 Nesting

The second comm may go inside the first. How much that is worth, with 8-movers on 20-move skeletons (best pairs, a computer search; the hand version is to look for the second comm inside the first as well as outside it):

**Two 8-move comms, random skeletons of 20 moves: mean added with nesting allowed, with the second comm kept outside the moves the first one changed, and with the two comms not touching at all. The means are over the skeletons where all three ways have a solution (third column) out of the sample (second column). For the edge rows the comms are 3e algs of 8 moves or fewer.**

{{nesting}}

- **On a 5c, nesting is worth {= NEST('5c') =}**, and the best solution needs it on {= CELL('nesting', '5c', 'Best needs nesting') =} of skeletons. Gezza Cubing ([[N1389]]): "for things like 5c, you can insert a commutator in the middle of the first commutator". argonblue ([[N5530]]), on having just seen one: "i thought it wasn't possible to nest 3c comms that are parts of a 5-cycle, but insertion finder apparently did it for one of my skeletons (improving it by 1 move)?" What argonblue saw is no rarity: it is the best there is on that {= CELL('nesting', '5c', 'Best needs nesting') =} (one is written out as example [e] in section 10).
- **Twisted 2c2c**: {= NEST('2c2c-twisted') =}, needed on {= CELL('nesting', 'twisted 2c2c', 'Best needs nesting') =}. **3c1t**: {= NEST('3c1t') =}. **Pure 2c2c, 2tc, 3tc**: under a tenth of a move.
- **Two comms that do not touch** cost {= APART('5c') =} more than the best on a 5c. That is the price of treating a 5c as two separate 3c searches.

### 6.6 Edges

**3e: one comm. Random skeletons, 20,000 per row. Cap 8 is the 6-, 7- and 8-move algs.**

{{cost_3e}}

For the next two, cap 8 is the best of two 3e algs of 8 moves or fewer and one alg of 8 or fewer for the whole leftover (both have 6-movers), and cap 10 is the same with algs of up to 10 moves. Random skeletons; the *Skeletons* column is the sample behind each row.

**2e2e** (two swaps, no flip):

{{cost_2e2e}}

**5e:**

{{cost_5e}}

- **With algs of 8 or fewer, nothing fits on {= CELL('cost_3e', ('8', '20'), 'Nothing fits') =} of random 20-move skeletons.** When something fits it is good ({= CELL('cost_3e', ('8', '20'), 'Mean added') =}). That is FakeMMAP's "huge variance" ([[N2876]]).
- **With every alg up to 10, a 3e costs {= CELL('cost_3e', ('10', '20'), 'Mean added') =}**, about what a 3c costs. The tutorial's 7 is a move above that, and its footnote says why the number moves: "Warning: this varies a lot! If edges are oriented early in the solve, you have better chances of finding a good insertion (6 or 8 movers)."
- **Whether a short alg fits depends on how the three edges sit.** A 6-mover needs them oriented on all three axes and an alg of 8 or fewer on at least two (section 5); on these random skeletons the leftover is oriented on two or three axes {= EOSHARE('rand_n', (2, 3)) =} of the time. So read the cap-8 rows as what the short algs give when nothing in the solve has arranged that, and the cap-10 and cap-12 rows as what a full alg list gives on any skeleton. The {= RL('by_type', '3e') =} real 3e skeletons of section 9 are far cheaper than any row here, and how their edges are oriented does not explain it (9.2).
- **2e2e and 5e** at cap 10: {= M('2e2e', L=10) =} and {= M('5e', L=10) =} ({= NSK('2e2e', L=10) =} and {= NSK('5e', L=10) =} skeletons). A 2e2e is the cheap one, and a 5e costs {= DIFF('5c', '5e', L=10) =} less than a 5c at the same cap ({= NSK('5e', L=10) =} 5e skeletons against {= NSK('5c', L=10) =} 5c skeletons). The other edge types are in Appendix A.

---

## 7. Which skeleton to take

### 7.1 The chance of a result

The chance of a final solution of N or less from a skeleton of a given type and length, 8-movers, random skeletons. Every cell is its own sample of {= NSK('5c') =} skeletons ({= NSK('2tc') =} for a 2tc), at the odd lengths too. A cell under 0.05% is fewer than ten skeletons of the {= NSK('5c') =} (for a 2tc, one or two of the {= NSK('2tc') =}), so the smallest cells are rough. Two-comm types are at their best pair of comms; a hand search that takes only the best first comm comes out a little longer (8.4), so treat their cells as a ceiling.

**28 or less:**

{{chance_28}}

**26 or less:**

{{chance_26}}

**30 or less:**

{{chance_30}}

**24 or less:**

{{chance_24}}

### 7.2 Exchange rates

Fanti's question ([[N1324]]): "how many moves shorter should a 5c (normal cycle) skeleton be compared to a 3c (normal cycle) skeleton so that i should look at the 5c first". By expected final length, 8-movers:

**How much shorter the other skeleton has to be to give the same expected total as a 3c of the length in the first column. Random skeletons, cap 8. An expected total is the length plus the mean added over the skeletons where something fits (that leaves out the {= CELL('cost_3c', ('8', '20'), 'Nothing fits') =} of 20-move 3c skeletons with no 8-mover).**

{{exchange_mean}}

And by the chance of reaching a target, which is what matters when you need a specific result:

**How much shorter the other skeleton has to be to give the same chance of the target as the 3c in the second column. Random skeletons, cap 8. Each whole length is its own sample; the length of equal chance is read off between two whole lengths.**

{{exchange_cap8}}

- **A 5c has to be about 5 moves shorter than a 3c**: {= EXR('5c') =} depending on the lengths and the target. asacuber's "maybe like 5-6" ([[N1325]]) is right at the 5 end: 5 shorter is break-even, 6 shorter is clearly the better skeleton.
- **The others**, how many moves shorter:

  | 3c1t | 3tc | pure 2c2c | twisted 2c2c | 2tc |
  |---:|---:|---:|---:|---:|
  | {= EXR('3c1t') =} | {= EXR('3tc') =} | {= EXR('2c2c-pure') =} | {= EXR('2c2c-twisted') =} | {= EXR('2tc') =} |

- The rates are a little lower when the 3c is unlikely to make the target (bottom rows of each block): when you need luck, the two-comm skeleton has the wider spread.
- **With algs up to 10** the same table (Appendix A, fewer skeletons) gives a 5c about {= EXR('5c', 10) =} and a pure 2c2c about {= EXR('2c2c-pure', 10) =}: the longer algs help the two-comm types more than the 3c.

### 7.3 The thresholds people quoted

**Chance of the stated goal, random skeletons, 8-movers. The expected total is the length plus the mean added over the skeletons where something fits.**

{{thresholds}}

- **The tutorial's pair for sub-30 holds**: 3c in 23 "you will probably get it" is {= CH('3c', 23, 29) =}, and 3c in 25 "you will need some luck" is {= CH('3c', 25, 29) =}.
- **"a skeleton leaving 4 corner in 18 moves is probably better than one leaving 3 corners in 25"**: by a lot. Expected {= TOTAL('2c2c-twisted', 18) =} to {= TOTAL('3c1t', 18) =} against {= TOTAL('3c', 25) =}.
- **Gezza Cubing's and oliynykmax's pairs** (3c in 22-24 or 24, 5c in 16-18 or 18) put the 5c six moves under the 3c. At that distance the 5c is the better of the two: a 5c in 18 makes sub-30 {= CH('5c', 18, 29) =} of the time, a 3c in 24 {= CH('3c', 24, 29) =}.
- **sequesteredcuber's "sub-22 for 3C skeleton", "sub-20 for every other skeleton"** ([[N292]]) puts them two moves apart, which is too close: a 3c in 21 is sub-30 {= CH('3c', 21, 29) =} of the time, a 5c in 19 only {= CH('5c', 19, 29) =} (a 19-move 5c with the usual outcome, 30, is written out below).
- **21 to 3c, "thats a guaranteed 29 right?"** ([[N4836]]). kyh ([[N4837]], [[N4838]]): "not strictly guaranteed", "but it's very likely you're getting a 29 or better". {= CH('3c', 21, 29) =} with 8-movers. The rest are the skeletons where no 8-mover fits anywhere; there it takes a 9- or 10-mover, and the result can be 30 or 31 (one is written out below).
- **zakk drewji's 19 to 5c giving 29, or 24 to 3c with three minutes left** ([[N4183]]). Eli Rogers ([[N4193]]): "3c would need to cancel 4 to beat the 29". An 8-4 or better is there on {= CH('3c', 24, 28) =} of 24-move 3c skeletons. kyh ([[N4186]]): "the chance ur cancelling 4 moves or more is not that high i think". Right, and DougCube's "I would go with the 29" ([[N4187]]) follows.

A 19-move 5c that gives 30, the most common outcome for one:

{{WIT_FIVEC19}}

A 21-move 3c that does not give 29:

{{WIT_N21}}
