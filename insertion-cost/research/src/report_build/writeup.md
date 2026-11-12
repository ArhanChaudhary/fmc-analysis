# Insertion cost by skeleton type

What a 3c, a 5c, a 2c2c, a 3c1t or a pair of twisted corners adds to a skeleton, by how long the skeleton is and how long an alg you allow yourself. Every skeleton is searched exactly: every position, every alg up to the cap.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#non-dr-discussion, #fmc-discussion or #fmc-theory). Docs are listed with links at the end.

**This builds on** what people had already worked out:

- **Sebastiano Tronto's table.** Section 2.4.10 of the [Fewest Moves Tutorial](https://fmcsolves.cubing.net/fmc_tutorial_ENG.pdf), "Move count (an estimate)", is the chart everyone points to: 3c 5/6, 3e 7, two twisted corners 8, three twisted corners 9, 2c2c 9/10, 3c1t 10, 5c 10/11, 2c2e 10. The tutorial says what it is: "It is a heuristic estimate, not a mathematically proved one", and its footnote says where the numbers came from: "Mostly taken from here, slightly adjusted to match my personal opinion", with a link to a post in the speedsolving FMC thread.
- **The estimates people posted.**
  - Phuwish: 2tc "~8.0 I guess", 3tc "mid to high 8 from my experience", 5c "~high 10", and "yeah" ([[N4540]]) to tave_789's "And isnt 3c1t and 2c2c close to 9.5?" ([[N4539]]).
  - cpaul: 9 for a pure 2c2c, 9.5 with a twist, 10 for a 3c1t.
  - Baiqiang: 5-6 for a 3c, 8-9 for a 3c1t, "6-8 for good 2c2c, 8-9 for bad 2c2c".
- **Exchange rates and thresholds from experience.**
  - asacuber's "maybe like 5-6" moves between a 5c and a 3c.
  - Gezza Cubing's and oliynykmax's pairs: a 5c in 16-18 against a 3c in 22-24.
  - The tutorial's 4 corners in 18 against 3 corners in 25.
  - Java ([[N332]]), on two comms against three: "you'd need the f2l-2 to be 6 moves shorter than the f2l-1 probably".
- **Which leftovers take how many comms**: the lists in Yurii Riabov's guide and in the tutorial. **Exhaustive alg results**: notkevin on the 10-move 2c2e algs, torchlight on the shortest alg that twists a corner. **Where insertions fall**: DougCube keeps stats on it.
- **Insertion Finder** ([333.fm/if](https://333.fm/if)), which gives the best insertions for one skeleton you type in. Baiqiang ([[D3803]]): "i make the website 333.fm. the core is written by Yan Xuan".

**What this adds** is the measured version:

- **Odds, not one number per type**: the chance of +4, +5, +6 and so on, for each leftover, at skeleton lengths from 10 to 30, under a stated cap on the alg length.
- **What the alg list is worth**: the same skeletons with algs of at most 8, 10 and 12 moves.
- **Exchange rates from those odds**: how many moves shorter a 5c, a 2c2c, a 3c1t or a 2tc has to be than a 3c to give the same chance.
- **Where the insertions are**: which part of the skeleton, what checking every other move misses, what taking the best first comm of a 5c loses.
- **The counts behind it**: which leftovers two comms can solve and which need three (proved in Lean), and the shortest alg for every case that has one of 12 moves or fewer.
- **Real skeletons**: {= RL('covered') =} worked examples ({= RL('skeletons') =} distinct skeletons) from the server and from Cyprian Kalbarczyk's example solves, searched the same way, and the Insertion Finder pages people posted.
- **The claims**: each concrete statement people made about insertions that a computer can settle, checked.
- **How the estimates come out**: every corner row of the tutorial's table, and cpaul's 9 and 10, are within about half a move of what 8-movers give on a random 20-move skeleton. Phuwish's figures are close too, except the 3tc. Baiqiang's are lower, and Baiqiang said they are not averages.

**Terms**, as the server uses them. A *skeleton* is a solution that leaves a few pieces: *3c* is three corners in a cycle, *5c* five corners in one cycle, *2c2c* two swaps of corners, *3c1t* a twisted 3-cycle plus one corner twisted in place, *2tc* and *3tc* two and three corners twisted in place, and the same with *e* for edges (*2fe* is two flipped edges). An *insertion* is an alg put somewhere inside the skeleton that solves those pieces and leaves the rest alone. A *comm* here is any alg for a 3-cycle, commutator or not, and an *8-mover* is one of 8 moves. `(8-2/24)` is the usual note: an 8-move alg, 2 moves cancel, 24 moves so far; I write +6 for what that insertion added. A *nested* insertion is one put inside another. Moves are counted in HTM.

**How to read it.**

- **Start with [section 1](#1-the-short-version)**, the short version: what is new, then what it confirms, one line each.
- **The [worked examples](examples.html)** go with it: the examples from the tutorial and the server redone with the search, then 200 skeletons to play along with, answers folded away. **The [errata](errata.html)** list what the numbers show is wrong in things said on the server, each with an example.
- **The appendices are reference**: the full cost tables, every class of corner and edge 3-cycle with a shortest alg, and how it was computed and checked.
- **What you can do in an attempt, and what is the answer key.** Every cost here is the best insertion over every spot and every alg within the cap. With 8-movers on a 3c that's what you get by checking every spot with the 8-movers you know, so those numbers are a target you can actually reach. Two things aren't:
  - **caps 10 and 12** count every sequence of that length, far more than any list a person knows;
  - **the best pair of comms** for a two-comm leftover means following up every first comm at every spot.

  Those are **computer only**, Insertion Finder's job: the answer key, not something to do in an attempt, and each place says so. The hand version of the best pair is to take the best first comm, and the ones a move worse when there's time (8.4), which gets within {= f2(max(float(CELL('greedy', r, 'First comms within 1 move')) - float(CELL('greedy', r, 'Best pair of comms')) for r in ('2tc', '3tc', 'pure 2c2c', 'twisted 2c2c', '3c1t', '5c', '3c3c'))) =} of a move of it. The rest is for the attempt: the odds and exchange rates for choosing a skeleton (section 7), the search rules of section 8 (every other move, the ends, opposite-face pairs), and the case facts of sections 4 and 5.

---

{{CONTENTS}}

---

## 1. The short version

{{SEC_SHORT}}

---

## 2. What was asked

The questions, in the words of the people who asked them. Most got an estimate or no answer.

- trig0n ([[T73]]): "What's the probability of getting ≤x-move 3C insertion if I have 17 to 3C", for random moves, for moves after EO, and for a DR. "Maybe it can be found using IF". Nobody replied.
- Zagros ([[N1164]]): "what is the average moves for corner insertion?" And on a 5c, from experience: "in reality it is soooo rare I find anything better than 8-2. Usually for two corner insertions I would say the average is 13 moves for me, one 8-2 and one 8-1." Java ([[N1165]]): "i think you can usually do a bit better with 5c".
- Fanti ([[N1324]]): "how many moves shorter should a 5c (normal cycle) skeleton be compared to a 3c (normal cycle) skeleton so that i should look at the 5c first". asacuber ([[N1325]]): "maybe like 5-6".
- zakk drewji ([[N3241]]): "What’s the possible Movescount from 24 to 3c?" DougCube ([[N3243]]): "It can be anything but typically a (8-2/30)."
- tave_789 ([[N4531]]): "How many moves should 2tc take with 2 insertions on average?" Phuwish ([[N4532]]): "~8.0 I guess". For a 3tc ([[N4537]]): "mid to high 8 from my experience", "It's s like 2tc but a half to a move worse". tave_789 ([[N4539]]): "And isnt 3c1t and 2c2c close to 9.5?" Phuwish ([[N4540]]): "yeah". tave_789 ([[N4541]]): "I think I remember one being a lil better but i dont remember". Phuwish ([[N4542]]): "and 5c ~high 10".
- Cuber4 ([[N5649]]): "What can I expect in terms of moves added from different insertions?" argonblue ([[N5650]]): "Sebastiano’s tutorial has a chart. it’s highly dependent on your skill level, luck, and the particular skeleton".
- jisu101 ([[N6504]], [[N6505]]): "if you can't find a 3c, what is generally better", "2c2c, 3c1t, or 5c?"

And one disagreement that was left standing. compLex ([[N4852]]) asked: "how many moves do you expect to add with 3c, 3c1t, and 2c2c skeletons, respectively?"

| Who | 3c | 3c1t | 2c2c |
|---|---|---|---|
| Baiqiang ([[N4853]]) | 5-6 | 8-9 | "6-8 for good 2c2c, 8-9 for bad 2c2c" |
| cpaul ([[N4857]], [[N4858]], [[N4859]]) | | "like 10 for 3c1t" | "more like 9 for pure 2-2", "like 9.5 for 2-2 with a twist" |
| tave_789, two months earlier ([[N4539]]): "close to 9.5?"; Phuwish ([[N4540]]): "yeah" | | close to 9.5 | close to 9.5 |
| The tutorial's table | 5/6 | 10 | 9/10 (its row is the double swap; the twisted double swap has no row) |

kyh ([[N4854]]): "6-8 for good 2c2c?????" And ([[N4855]]): "btw you mean good like as in the co matches, the stickers swap with eachother". Nobody answered that, so which 2c2c is the good one is not on record. cpaul ([[N4856]]): "I don't think 2c2c is 6-8 lol". Jay ([[N4860]]): "maybe there's some non 3c type insertion method for 2c2c that lowers the movecount that far idk, but yeah ime when i was doing blocks i didn't notice a meaningful different between 2 insertion 4c types other than 2c2c being easier practically with rNISS". wen, four minutes later ([[N4862]]): "Why is there even a difference if the number of possible first insertions is the same tbh". Baiqiang, the next day ([[N4863]]): "this is i expected not avg expected".

On which 4c or 5c to prefer there were two views. argonblue ([[N6507]]): "i think 3c1t > 2c2c > 5c. mostly because a twist gives you the most freedom to pick comms". jisu101 ([[N6508]]): "True but so does 2c2c, you can pick literally any comm with 3 of the 4 corners".

Sections 6 and 7 answer these. In short: the tutorial's corner rows and cpaul's 9 and 10 are what 8-movers give on a random skeleton, each within about half a move. Phuwish's figures are close, except for the 3tc. Baiqiang's are lower and are not averages. And by cost the order is 2c2c, then 3c1t, then 5c.

---

## 3. What an insertion is here

**The setup.** A skeleton is a sequence of n moves that solves the scramble except for a *leftover*: a 3c, a 5c and so on. There are n + 1 places to insert, before the first move, between any two, and after the last. At each place exactly one cube state has to be produced by the inserted alg (it is the leftover carried through the moves that follow), so the only freedom is which alg for that state, and where.

**The cost** of an insertion is what it adds: the length of the solution with the alg in it and all cancelling done, minus n. An `(8-2)` costs +6. Cancelling is done the way you do it on paper: moves on the same face merge (`R R` is `R2`, `R R'` is nothing), moves on opposite faces commute, and it repeats as far as it goes, so an alg can also cancel into moves two or three deep, and moves on either side of it can meet through it.

**Why there has to be a cap.** If an alg of any length were allowed, the best insertion would be the optimal solution of the whole scramble written as one alg at one spot. Nobody means that by an insertion. So every number here is for a cap on the length of each inserted alg, and I give three:

| Cap | What it stands for |
|---:|---|
| 8 | Pure 8-move comms for corners. For edges: the 6-, 7- and 8-move algs. This is what most people insert, and it is Insertion Finder's "Pure 3 Corners" set (Baiqiang, [[N3793]]: "Pure 3 corners includes 8 moves comms only. The other one includes some 10 moves"). |
| 10 | Everything up to 10 moves: the 9-movers (a setup move that cancels into an 8-mover), the 10-move sledge comms, the 10-move 2c2c algs. |
| 12 | Everything up to 12: also the 12-move two-twist comms, triple sexy and the like. |

Within the cap *every* move sequence that does the job counts, not a list of known algs. So cap 8 on a 3c is the true best over all 8-movers at all spots, and cap 12 is every sequence of up to 12 moves, far more than any list a person knows. Cap 8 is the hand number: checking every spot with 8-movers is what solvers do. Caps 10 and 12 are **computer only** (unless you have learned the 10- and 12-move algs of that leftover): they say what a full alg list would give, which is an answer key, not a search to run in an attempt.

**What may be inserted.** Four ways of solving a leftover, each searched exactly:

| Name here | What it is | Used for |
|---|---|---|
| one comm | one 3-cycle alg, at the best spot | 3c, 3e |
| two comms | two 3-cycle algs, one after the other. The second may go anywhere in the solution the first one gave, also inside the first alg (nested) | 5c, 2c2c, 3c1t, 2tc, 3tc, 3c3c and the edge types |
| one alg | one alg that does the whole leftover at once, like a 10-move 2c2c alg or triple sexy | any leftover that has an alg within the cap |
| a comm plus an alg | two insertions where only one has to be a 3-cycle comm; the other is any alg within the cap that does a whole leftover in one go (a 2c2c alg, a two-twist, a 5-cycle alg) | compared separately, on fewer skeletons; Insertion Finder with all its sets on does part of this |

Unless a table says otherwise, a number for a two-comm leftover is the best of *two comms* and *one alg*. *A comm plus an alg* is kept apart because it is expensive to search and few people insert that way. With long algs it also starts to be something else: two algs wrapped around a stretch of the skeleton can cancel into less than the stretch, which is rewriting the solution more than inserting into it. Read it as the ceiling of what an unlimited alg list could do: **computer only**.

**Random skeletons.** The big tables are over random skeletons: each move is drawn at random (never two in a row on one face), and the leftover is drawn at random among all leftovers of its type. A random skeleton is a move sequence, not a solve. It has no blocks, no EO, and it doesn't end in a last-layer alg. Section 9 puts {= RL('covered') =} worked examples from real solves ({= RL('skeletons') =} distinct skeletons) next to them, and two things come out of that:

- The same real move sequences with a random leftover on them cost what random sequences cost (the same for a 3c, within a tenth of a move for a 5c), so the tables aren't skewed by how skeletons are written.
- The skeletons people post, with their own leftover, come out most of a move cheaper than the tables with 8-movers. Selection is part of that: for a 3c, the skeletons posted with their insertion are {= SUBD('from the server, an insertion written out', '3c') =} from random and the {= SUBN('the last two together', '3c') =} less-picked ones {= SUBD('the last two together', '3c') =}. For edges the posted skeletons are further from the random tables (6.6, 9.2).

**How many.** Sample sizes per skeleton length; each table also says which.

| What was run | Skeletons per length |
|---|---|
| cap 8, every type, each even length from 10 to 30 | {= NSK('5c') =} ({= NSK('2tc') =} for 2tc, 2fe and the two kinds of 2e2e) |
| the same for the corner types of section 7 (3c, 2tc, 3tc, both 2c2c, 3c1t, 5c) at every odd length from 11 to 29 | the same size |
| cap 10, a 3c or a 3e, and one alg | {= NSK('3c', L=10) =} |
| cap 10, two comms (the search is slow there) | {= NSK('5c', L=10) =} for 5c and 3c3c, {= NSK('3c1t', L=10) =} for 2c2c, 3c1t and 3tc, {= NSK('2tc', L=10) =} for 2tc |
| cap 12, two comms, skeletons of 20 moves, for {= CAP12RUN() =} (not for {= CAP12NOT() =}) | {= NSK('5c', L=12, src='two12') =} |
| cap 10, a comm plus an alg, skeletons of 20 moves | {= NSK('5c', L=10, model='mixed', src='mixed') =} |

{{SEC_TYPES}}

{{SEC_COST}}

{{SEC_FIND}}

{{SEC_REAL}}

{{SEC_CLAIMS}}

{{APP}}
