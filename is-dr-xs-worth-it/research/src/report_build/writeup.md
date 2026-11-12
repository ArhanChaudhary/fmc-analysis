# Is DR-xs worth it?

What it costs to leave slices unsolved at DR, how often the chance is there, and what it buys on real scrambles. Everything that can be counted exactly is counted exactly.

This builds on work that is already on the server. The method is tseitsei89's [DR-Xs tutorial](https://docs.google.com/document/d/1_uLVLB5xqDm40NugXE5rjc8LgEtuHQCLz0odKY6mboE) (with Jay, Rodney, trangium, count quackula, KrzychXyz and others behind it), and the numbers in it are trangium's: on optimal a DR-1s finishes about 2.2 to 2.4 moves longer than a DR of the same subset (1.8 for 2c4), and a DR-2s 8fe about 1 move longer. tseitsei89's conclusion from them is "8 move DR-1s is on average better than an 11 move DR but worse than 10 move DR". Those hold up. What was missing, and what people kept asking for, is here:

- **Odds, not just averages**: the chance of a finish in N from a DR-1s or a DR-2s 8fe, by subset, next to the same for a DR.
- **The move counts** from DR-3s to DR-2s to DR-1s to DR, for every layout of flipped edges.
- **How often you get one**: the chance of a slice-EO skip, and how far a DR-1s is from one.
- **Real scrambles**: every DR-1s and DR-2s 8fe on 500 scrambles, finished, against every normal DR on the same scrambles.
- **The claims**: each concrete statement people made about DR-xs, checked.

**Terms**, as the tutorial uses them. A *slice EO* (sEO) is the four edges belonging to one slice all oriented, or all misoriented, for one axis. A *DR-xs* is a cube that looks like a DR if you ignore the centers and let some of the eight non-slice edges be flipped. It is a *DR-1s*, *DR-2s* or *DR-3s* by the number of slice moves needed to fix centers and flipped edges. *DR-2s 8fe* is the DR-2s with all eight edges flipped and the centers off, which is how it comes up in the tutorial (eight flipped edges with the centers right is a different, worse DR-2s). Turns are counted in HTM, and a slice move counts as the two outer turns it is written with (`R L'`).

---

{{CONTENTS}}

---

## 1. The short version

- **A DR-1s costs {= D1() =} more moves in the finish than a DR.** Over {= N1() =} random DR-1s states, each finished as well as the method can (setup, slice, DR finish), the average is {= A1() =} against {= AD() =} for a DR. By subset it is +{= D1('2c5') =} to +{= D1('4a1') =}, a little more on the low-qt subsets. trangium's nissy averages are 0.1 to 0.4 lower; those are true optimals, which may leave the form.
- **In odds**: a DR-1s finishes in 14 or less {= P1(14) =} of the time and in 15 or less {= P1(15) =}. A DR does that {= PD(14) =} and {= PD(15) =} of the time. At equal odds a DR-1s in N is a DR in about N + {= EXCH() =}. The tutorial's line that an 8-move DR-1s sits between a 10- and an 11-move DR holds.
- **The one good kind of DR-1s** is the one that a single slice turn fixes, seen from one side of the scramble or the other ({= BETTER(2, 'share') =} of them): it finishes in {= BETTER(2) =} on average, {= BETTER(2, 'diff') =} over a DR. Past that the layout matters little: needing 4, 5 or 6 turns to DR from the better side gives {= BETTER(4) =}, {= BETTER(5) =} and {= BETTER(6) =}.
- **DR-1s to DR takes 2 to 6 turns, and usually 5 or 6.** Of the 70 ways four flipped edges can sit, {= FIX70(2) =} needs 2 turns, {= FIX70(3) =} need 3, {= FIX70(4) =} need 4, {= FIX70(5) =} need 5 and {= FIX70(6) =} need 6. Daichi's "6 moves max" is exact. The distribution is not flat and the typical fix is not 3.
- **A DR-2s 8fe costs {= D8() =} more** ({= N8() =} random states), +{= D8('4a1') =} (4a1) to +{= D8('4c4') =} (4c4) by subset, a tenth or two above trangium's nissy optimals on the subsets trangium measured. A normal DR that ends in `U R L` is one of these two moves earlier, so that ending is worth a little under a move.
- **A slice-EO skip is there on {= SKIP('normal') =} of scrambles on normal, {= SKIP('both') =} counting inverse.** That is exact, and it answers wen's question. For one given slice a slice EO is never more than 2 moves away, as FakeMMAP said.
- **From an oriented skip on an axis that is not the slice's own, a DR-1s is on average {= SHM('eo-fb_1s | A oriented') =} moves away** without breaking the EO of that axis: within 7 for {= SH('eo-fb_1s | A oriented', 7) =} of skips, within 8 for {= SH('eo-fb_1s | A oriented', 8) =}, within 6 for {= SH('eo-fb_1s | A oriented', 6) =}. tseitsei89, by hand ([[T10809]]): "I can usually find some DR-fe in 8 moves. Occasionally 7."
- **Which skips can work at all**, as long as you keep that axis's EO, is a clean rule. Oriented, on an axis that is not the slice's own: always. Misoriented on such an axis: only if that axis has exactly 8 bad edges. Oriented on the slice's own axis: {= SHR('eo-ud_1s | B oriented') =} of the time. Misoriented on the slice's own axis: never.
- **On 500 real scrambles**, {= TH('a DR-1s of 8 or less from a skip or a one-move slice EO') =} have a DR-1s of 8 or less from a skip or a one-move slice EO, and {= TH('a DR-1s of 7 or less from a skip or a one-move slice EO') =} have one of 7 or less. Finishing all of them on top of every normal DR of 10 or less takes the average result from {= POL(0) =} to {= POL(2) =}. Every 11-move DR instead takes it to {= POL(4) =}, with {= f1(float(POLN(4, 0).replace(',', '')) / float(POLN(2, 0).replace(',', ''))) =} times as many to finish.
- **What each one is worth**, by how often it reaches the best normal-DR solution of its scramble: a DR-1s of 7 one time in {= YIN('1s7') =}, close to a normal DR of 9 or less (one in {= YIN('dr9') =}); a DR-1s of 8 one in {= YIN('1s8') =}, between a 10-move DR (one in {= YIN('dr10') =}) and an 11 (one in {= YIN('dr11') =}); a DR-2s 8fe of 9 one in {= YIN('8fe9') =}.
- **So is it worth it?** A DR-1s of 7 or less: yes, before your 10-move DRs. One is there on about half of scrambles. A DR-1s of 8: it goes after the 10s and before the 11s, about {= YX('1s8', 'dr11') =} eleven-movers each. A DR-2s 8fe of 9 is about as good as a 10-move DR. Only a DR-1s of 6 or less beats a normal DR of 9 or less, and that is there on {= TH('a DR-1s of 6 or less from a skip or a one-move slice EO') =} of scrambles. Once the 11-movers are done DR-xs adds {= POLD(4, 5) =} to the average. Mostly it gets the same result from fewer and shorter things; on {= RL('win12') =} of scrambles it beats everything a normal DR of 12 or less gives.
- **Against 5-move EOs**: starting from the EOs of 4 or less and their DRs of 10 or less, the DR-1s of 8 or less from slice EOs improve the average result by {= EOD('eo10', 0, 2) =}, and every 5-move EO (about {= f'{REAL["eo10"]["policies"][4]["eos"] - REAL["eo10"]["policies"][0]["eos"]:,.0f}' =} more EOs) by {= EOD('eo10', 0, 4) =}. The 5-movers give more, the slice EOs take far less looking. tseitsei89's order, sub-5 EOs, then slice-EO skips, then 5-movers, fits that as long as the skips are quick to check; the tables do not measure time.

---

## 2. What was asked

The questions this answers, in the words of the people who asked them.

- Tom Nelson ([[T12405]]): "do we have movecount distributions for DR-1s > DR and DR-2s > DR? it feels like DR-xs is almost never good (apart from 2s8fe)". The answers were estimates. Daichi ([[T12406]], [[T12408]]): "dr-1s to dr is like 6 moves max?", "i don't think 7 optimal exists". Rodney ([[T12409]]): "I would guess the distribution is basically flat."
- Radek B ([[D18613]]): "is there a list of all cases for dr-1/2s -> dr?" tseitsei89: "I dont think so".
- wen ([[D19420]]): "what is the probability of at least one slice EO skip (fully oriented or vice versa) on a scramble?" tseitsei89 ([[D19421]]): "I have no idea. But it seems to happen on most scrambles I would say."
- JTuu ([[T10607]]): "what's the length distribution for the slice-eo condition? what about expected moves to dr from there?"
- tseitsei89 ([[T10813]]), on slice EO in 1 being better than EO in 5: "Do we have some proper stats for that?"
- trangium ([[T11296]]): "at some point I want to do an analysis of how likely various things are to give you, say, sub-11 dr or sub-8 dr-1s", then divide by the time it takes to check. tseitsei89 ([[T11299]]): "This I think would be EXTREMELY valuable!"
- tseitsei89 ([[D19521]]): "For sEO I currently believe skips are better than 5 move EOs but 1 movers might not be."

And the verdicts never settled. tseitsei89 ([[T10809]]): "You are better off with classical DR it seems." Rodney ([[T11020]]): "You're leaving money on the table if you don't check these, IMO." zakimoshi ([[T11306]]): "sEO isn't actually a very cost effective strategy time wise". tseitsei89 again, three months later ([[D17453]]): "most of the time it is not worth it to spend time on but it can occasionally save an otherwise doomed attempt".

---

## 3. What a DR-xs is, and how many slices it needs

Take a cube and one colour pair, say white/yellow. It is a DR-xs for that colour when:

- every corner has its white or yellow sticker on the same pair of opposite faces (any pair, not necessarily the white and yellow faces),
- the four edges with no white or yellow are in the slice between those two faces, and they all agree with each other.

The other eight edges can be flipped (white or yellow on the side) in any even number. Centers are ignored. This is the group FakeMMAP wrote down ([[T10755]]): "<U, D, F2, B2, R2, L2, M, S>, aka DR-fe."

How many slices such a state needs is read off two things: where the corners' faces are relative to the centers, and how many edges are flipped. trangium's examples doc gives the rule, and the full enumeration confirms it line for line:

{{kinds}}

"Slice edges against the centers" is the tutorial's aligned and misaligned: do the four slice edges match the centers of their slice or not. Per colour there are 768 kinds of state, a kind being the faces, the places of the flipped edges and that one bit. Section 4 is an exact computation over these kinds, and section 6 uses them as targets.

Two checks on the definition:

- The search for the nearest DR-xs on one colour and one pair of faces, over all cosets, gives 1, 4, 50, 586, 6800, 72894, 659610, 3479477, 4193028, 247986, 84 states at 0 to 10 moves. That is the distribution trangium posted ([[T11332]]), number for number.
- The server's own worked examples carry labels like "DR-2s", "4a2-1s", "2c3 -2s 8fe". I could replay 43 such labelled states from the docs and the two channels, and all 43 are what the label says by the table above.

---

## 4. The move counts: DR-3s, DR-2s, DR-1s, DR

Counted in face turns with all cancelling done, using only moves that keep the DR-xs: any turn of the two faces the corners are oriented on, half turns of the other four, and slice turns written as two outer turns. `R2` followed by `R L'` is `R' L'`, two turns.

### 4.1 To a real DR

{{fix_turns}}

This is the count from the state alone, with nothing to cancel against. It is over kinds, and every kind with the same number of slices is equally likely for a DR-xs you did not steer.

### 4.2 DR-1s to DR: all 70 layouts

A DR-1s has exactly four flipped edges, and one slice turn fixes it once those four are in the slice that the turn moves. The eight places they can be in are four inside that slice and four outside it, so there are 70 layouts. With the corners on F/B, where the slice that fixes is `R L`:

{{dr1s_layouts}}

- **Daichi is right** that 6 is the most and 7 does not exist ([[T12408]]). So is Rodney's bound ([[T12409]]): "Worst case requires 2qt, with at most one half-turn before/between each qt, so 4 and then the slice."
- **The distribution is not flat.** {= FIXSHARE(1, (5, 6)) =} of layouts need 5 or 6 turns, and the average is {= FIXAVG(1) =}. The working assumption in the EO Meta Comparison doc, "1 slice can be fixed in 3 moves", is {= f2(float(FIXAVG(1)) - 3) =} short, and sqAree's "more than 5 moves most of the time" ([[T10672]]) is the accurate one. That count is not the cost, though. The setup moves are also finish moves and the slice gets moved around in the finish, so the cost that matters is the finish (section 5).
- **3-1 is not much worse than 2-2 here.** With three of the four already in the slice it is 5 or 6. With two it is anything from 3 to 6. With none it is 4 (`F B R L`).
- All 70 layouts with a shortest fix each are in Appendix A. This is the list Radek B asked for.

**Simon's table.** Simon's slice-DR doc has the same count for its step 3, taking the better direction of the last trigger move: "Num Cases out of 70": 1, 4, 9, 40, 16 for 2 to 6 moves. Mine with the same choice is {= SIMON() =}. The ends agree, and so does Simon's "~4.9 moves on average". But thirteen layouts have a 4-turn fix, not nine. They are listed at the end of Appendix A, each with its fix.

### 4.3 The steps in between

| Step | Kinds | Turns, counted from scratch | Right after a trigger (a side quarter turn), at best |
|---|---:|---|---|
| DR-3s to DR-2s | {= STEPS['DR-3s -> DR-2s (or better)']['kinds'] =} | {= STEP('DR-3s -> DR-2s (or better)', 'scratch') =} | {= STEP('DR-3s -> DR-2s (or better)', 'after_quarter_better') =} |
| DR-2s to DR-1s | {= STEPS['DR-2s -> DR-1s (or better)']['kinds'] =} | {= STEP('DR-2s -> DR-1s (or better)', 'scratch') =} | {= STEP('DR-2s -> DR-1s (or better)', 'after_quarter_better') =} |
| DR-1s to DR | {= STEPS['DR-1s -> DR']['kinds'] =} | {= STEP('DR-1s -> DR', 'scratch') =} | {= STEP('DR-1s -> DR', 'after_quarter_better') =} |
| DR-2s to DR | {= STEPS['DR-2s -> DR']['kinds'] =} | {= STEP('DR-2s -> DR', 'scratch') =} | {= STEP('DR-2s -> DR', 'after_quarter_better') =} |

The last column is the extra turns when the move just made was a quarter turn of a side face, with the better of the two side axes: a slice about that axis merges with it (`R` then `R' L` is just `L`).

- **A DR-3s is always a DR-2s for free** right after the trigger, as the tutorial says: "you can always go to DR-2s in 0 moves by inserting a slice move that cancels with your last DR move".
- **DR-2s to DR-1s** is a slice with 0, 1 or 2 setup moves. Rodney's "DR-2s needs at most 2 moves to reach DR-1s" ([[T12409]]) is right if the slice itself is not counted. Right after the trigger, with its last move on the better of the two side axes, it is free for {= STEP('DR-2s -> DR-1s (or better)', 'after_quarter_better', 0) =} of the 383 kinds and costs 3 for the rest. On the other side axis it is free for {= STEP('DR-2s -> DR-1s (or better)', 'after_quarter_worse', 0) =}.

---

## 5. The finish: DR-1s and DR-2s 8fe against a DR

### 5.1 How it is measured

The tutorial's way to finish a DR-1s is: set the four flipped edges up, do the slice, HTR from the other side, then leave slice while slicing the `R L'` back out. Every solution it can find has the form

> (moves that keep the DR-1s) (one slice turn) (a DR finish),

read from either side. For a given DR-1s the shortest solution of that form is computed exactly: every setup from both ends, and for the DR that comes out, its optimal finish from the first study's table of all 19,508,428,800 DR states. So "finish" below is the best the method can do, the same way "optimal finish" was for a DR. For a DR-2s 8fe the form is setup, both slices one after the other, DR finish.

The states are drawn uniformly: {= N1() =} DR-1s and {= N8() =} DR-2s 8fe. That is the right weighting for a DR-xs reached by a route that was chosen without looking past the DR-xs itself: the part of the cube the route does not look at is still uniformly random. Section 7.5 checks it on real scrambles.

### 5.2 By subset

The subset of a DR-xs is its corner subset, as in "4a2-1s". trangium's columns are the nissy optimal averages from the tutorial.

{{finish_subset}}

- The penalty for a DR-1s is +{= D1() =} overall. It is larger on the low-qt subsets (+{= D1('4a1') =} for 4a1) than on the high ones (+{= D1('4b5') =} for 4b5), so a DR-1s flattens the difference between subsets a little.
- My DR-1s numbers are 0.1 to 0.4 above trangium's. trangium's are true optimals, which may leave the form, and trangium says of them that "lots of optimals are not findable" ([[T10808]]). The DR column agrees with trangium's to within 0.05.
- For DR-2s 8fe the penalty is +{= D8() =}, and 0.1 to 0.2 above trangium's on each of the five subsets trangium measured. The 8fe sample is small for the rare subsets: {= sum(xv.eight('0c0')) =} states of 0c0, {= sum(xv.eight('0c4')) =} of 0c4, {= sum(xv.eight('0c3')) =} of 0c3.

### 5.3 In odds

{{finish_odds}}

And with the length of what you have added on, the chance of a solution in N or less:

{{solution_odds}}

Read the second table by finding equal rows. A DR-1s in 7 sits between a DR in 9 and a DR in 10, about midway. A DR-1s in 8 sits between a DR in 10 and a DR in 11. A DR-2s 8fe in 9 is a little behind a DR in 10. So:

- **DR-1s in N is about a DR in N + {= EXCH() =}**, at equal odds for finishes of 13 to 16 ({= D1() =} on the average). Rodney's "+3/+4 penalty for -1/-2 slice" ([[T10919]]) is a bit hard on the DR-1s if you finish it well, and tseitsei89's later "in reality around 3 moves worse" ([[T11142]]) is what it becomes when you don't find the best finish (5.5).
- **DR-2s 8fe in N is about a DR in N + {= D8() =}.**

### 5.4 Which DR-1s are the good ones

Two things you can see on a DR-1s were said to matter: how far it is from a DR, and how the four flipped edges split between the two slices they belong to (Rodney, [[T10832]]: "3-1 is bad because it requires 2 QT", "2-2 requires 1 QT"). They are the same thing seen from the two sides of the scramble: the four flipped edges all belong to one slice exactly when, on the other side, they all sit in one slice. So one table covers both, the fewest turns to a real DR from whichever side is better:

{{better}}

- **The DR-1s to want is the one a single slice turn fixes, from one side or the other**: +{= BETTER(2, 'diff') =}, a little less than a DR-2s 8fe costs. It is {= BETTER(2, 'share') =} of them.
- **Beyond that, the layout matters little.** From 4 turns to 6 the average finish moves by {= f2(float(BETTER(6)) - float(BETTER(4))) =}. A DR-1s that is 6 from a real DR is not 4 worse than one that is 2 away, because the setup moves are also finish moves.
- **"Extra-good" is two cases.** Rodney's extra-good DR-1s is four flipped edges all belonging to one slice ([[T11232]]), which Rodney put at "just 1-2 moves worse than full DR". When that slice is the one that fixes, it is the first row. When it is the other slice, the four sit together in the wrong slice (`F B R L` to fix) and the finish is +{= OTHER4('diff') =}, no better than an ordinary DR-1s. Averaged over the two it is +{= f2(float(SPLIT('4-0')) - float(AD())) =}.

### 5.5 What a hand finish loses

The best solution has its slice within 4 moves of one end for at least {= SETUP_LE(4) =} of DR-1s states, which is trangium's "pretty high chance that the slice ends up within 4 moves of the start or the end" ([[T10921]]). But it is not always the end you are on. If the setup has to be at most 4 moves and on the side where you found the DR-1s, with any DR finish after it, the average is {= A1(col='finish_setup4') =}, which is {= f2(float(A1(col='finish_setup4')) - float(A1())) =} more, and only {= OWN4_SAME() =} of states keep their best finish. So try the setup from both sides before judging a DR-1s.

How often a person finds these finishes is not something I can compute. trangium's findability tables in the tutorial are the data there is: for 4b2-1s, optimal findable 51% of the time and optimal + 1 another 32%.

### 5.6 DR-2s 8fe and the DR that ends in U R L

The tutorial's cheapest way to a DR-2s 8fe is a normal DR that ends in something like `U R L`: do `D` instead and you are at an 8fe two moves earlier. An 8fe in N is worth a DR in N + {= D8() =}, so the DR in N + 2 that ends that way is worth a DR in about N + {= f1(float(D8())) =}. **The ending is worth about {= f1(2 - float(D8())) =} of a move** with the best finish of this form, and 0.9 to 1.15 with trangium's optimal averages. trangium put it at "1 to 1.3 moves better" ([[T11115]]) and count quackula at "one move better" ([[T11114]]): about one move stands.

By subset the 8fe penalty runs from +{= D8('4a1') =} (4a1) to +{= D8('4c4') =} (4c4). Unlike the DR-1s penalty it grows with the qt count, so the `U R L` ending is worth about a move on the low-qt subsets and about {= f1(2 - float(D8('4c4'))) =} on 4c4.

---

## 6. Getting one

### 6.1 How often there is a slice-EO skip

There are 9 pairs of a slice and an axis, each in two flavours (all oriented, all misoriented), on normal and on inverse. Whether a scramble has a skip depends only on which kind of edge sits where and on the orientations, which is 70,963,200 equally likely configurations. Counting all of them:

{{skip_odds}}

- **{= SKIP4('normal') =} of scrambles have at least one skip on normal, and {= SKIP4('both') =} have one on normal or inverse.** That is wen's question.
- Each single skip (one slice, one axis, one flavour, one side) has chance 1/16, so 1/8 for a slice and an axis with either flavour, as tseitsei89 and count quackula worked out ([[D19427]], [[D19423]]). The skips are far from independent: the average is {= SKIP('both', 'avg') =} per scramble over both sides, but {= SKIP('both', 0) =} of scrambles have none.
- The tutorial's "often 1-2 on a scramble" is right.

And for one given slice, the moves to a slice EO on some axis, over all 7,920 ways its four pieces can sit:

| Slice EO wanted | Skip | 1 move | 2 moves | 3 moves | 4 moves |
|---|---:|---:|---:|---:|---:|
| any axis, oriented or misoriented | {= SD('any axis, oriented or misoriented', 0) =} | {= SD('any axis, oriented or misoriented', 1) =} | {= SD('any axis, oriented or misoriented', 2) =} | 0 | 0 |
| any axis, oriented only | {= SD('any axis, oriented only', 0) =} | {= SD('any axis, oriented only', 1) =} | {= SD('any axis, oriented only', 2) =} | {= SD('any axis, oriented only', 3) =} | 0 |
| one given axis, oriented or misoriented | {= SD('F/B only, oriented or misoriented', 0) =} | {= SD('F/B only, oriented or misoriented', 1) =} | {= SD('F/B only, oriented or misoriented', 2) =} | {= SD('F/B only, oriented or misoriented', 3) =} | 0 |
| one given axis, oriented only | {= SD('F/B only, oriented', 0) =} | {= SD('F/B only, oriented', 1) =} | {= SD('F/B only, oriented', 2) =} | {= SD('F/B only, oriented', 3) =} | {= SD('F/B only, oriented', 4) =} |

FakeMMAP's "never more than 2 moves away", "No matter which slice you pick" ([[T10773]], [[T10774]]) is exact, and so is the EO Meta Comparison doc's "partial EO in <=2 is guaranteed", as long as all-misoriented counts. All-oriented only, it takes 3 moves {= SD('any axis, oriented only', 3) =} of the time.

### 6.2 From a skip to a DR-1s

After the slice EO the tutorial looks for rzp and DR "like normal", ignoring flipped edges and centers. Normal means without quarter turns of the EO axis's two faces, which keeps every edge's orientation for that axis. Under exactly that rule, the nearest DR-1s from every state with a skip, by the kind of skip:

{{skip_to_1s}}

- **Oriented, on an axis that is not the slice's own** (E-slice edges oriented on F/B, say): there is always a route. It is 7 or less for {= SH('eo-fb_1s | A oriented', 7) =} of skips and 8 or less for {= SH('eo-fb_1s | A oriented', 8) =}. For comparison, from a full EO the nearest real DR on one given axis is {= SHM('eo-fb_dr | A oriented') =} moves away on average under the same rule. So a skip of this kind is, in route length, an EO that cost nothing, and in finish it is a DR-1s. That is the sense of Rodney's "sliceEO in N is as good as regular EO in N+3" ([[T11020]]); with the finish penalty at {= EXCH() =} the 3 is a little generous to the normal EO, before you count how many of each you get to try.
- **Misoriented on such an axis**: without breaking that axis's EO a route exists only when exactly four of the other eight edges are bad, so that the axis has 8 bad edges in all. That is {= SHR('eo-fb_1s | A misoriented') =} of these skips (70 in 128). trangium ([[T11357]]): "you MUST have 8 bad on that axis for even a chance at dr-1s". Rodney's "55%" ([[T11566]]) is this number.
- **Oriented on the slice's own axis** (E-slice edges oriented on U/D): {= SHR('eo-ud_1s | B oriented') =}, when as many M-slice pieces as S-slice pieces are bad. The same states can reach a real DR on that colour without U or D quarter turns, {= SHM('eo-ud_dr | B oriented') =} moves away on average.
- **Misoriented on the slice's own axis**: never, with or without the extra quarter turns below. Daichi's "misoriented sEOs are just worse overall" ([[D19634]]) is right in both families.

Letting quarter turns of the EO axis in when they miss the slice pieces (the tutorial's tip 2) opens the two half-open kinds of skip fully, misoriented on another axis and oriented on the slice's own, but shortens little. Using any move at all shortens it by a quarter move:

{{skip_to_1s_rules}}

### 6.3 To a DR-2s 8fe: the same problem as a DR

**Getting to a DR-2s 8fe is getting to a DR with the pieces renamed.** An 8fe has its corners and slice edges placed as in a DR on one pair of faces, in the colours of another pair. Move every piece a quarter turn around the third axis, leave the centres where they are, and flip every edge in its place: the 8fe becomes a real DR. Do that to any position, and rename the faces of a move sequence by the same quarter turn, and reaching the 8fe becomes reaching the DR. Edges that are good for the third axis stay good, so an EO on that axis carries over as well. Counted over every position with a full EO, with moves that keep it:

{{eo_to_8fe}}

- **From an EO, the 8fe is exactly as far as the DR**: the same distribution, {= E8AVG() =} on average. This is the tutorial's route 3, do the normal EO and then solve the wrong-coloured DR. Each of the EO's two DR axes has one, so an EO has four targets where it had two, and the two extra ones cost {= D8() =} more in the finish.
- **With any moves it is the same, target by target.** A scramble has twelve 8fe (two for each colour, on normal and on inverse) against six DRs, and each is as far away as a DR is. That is why the shortest 8fe of a scramble comes {= f2(float(NEARAVG('dr')) - float(NEARAVG('2s8fe'))) =} of a move before its shortest DR in 6.4: there are twice as many, and none of them is closer. (Checked on {= E8CHK() =} random positions: the distance to the 8fe is the distance of the renamed position to the DR every time.)
- **What does not carry over is the finish.** The renaming does not take the solved cube to the solved cube, and making up the difference is what the two slice turns are for: +{= D8() =} (section 5).

**So a slice-EO skip is not what gets you an 8fe.** By the kind of skip, keeping that axis's EO:

{{skip_to_8fe}}

- **An oriented skip** leads to an 8fe only when the rest of the axis is oriented as well ({= SHR('eo-fb_2s8fe | A oriented') =} of such skips, 1 in 128), and that is a normal EO. The skip adds nothing to it.
- **A misoriented skip on an axis with 8 bad edges** (the four slice edges and four of the other eight, {= SHR('eo-fb_2s8fe | A misoriented') =} of misoriented skips) is the one separate way in. From there an 8fe is {= SHM('eo-fb_2s8fe | A misoriented') =} moves away on average, against {= E8AVG() =} from an EO, with no moves spent on an EO first. It is 8 or less for {= SH('eo-fb_2s8fe | A misoriented', 8) =} of those skips.

### 6.4 What exists, with any moves

Without any rule on the moves, linear on one side, over a sample of {= NEARN() =} random scrambles (three colours, normal and inverse):

| Shortest on the scramble | Average | 6 or less | 7 or less | 8 or less | 9 or less |
|---|---:|---:|---:|---:|---:|
| a real DR | {= NEARAVG('dr') =} | {= NEAR('dr', 6) =} | {= NEAR('dr', 7) =} | {= NEAR('dr', 8) =} | {= NEAR('dr', 9) =} |
| a DR-2s 8fe | {= NEARAVG('2s8fe') =} | {= NEAR('2s8fe', 6) =} | {= NEAR('2s8fe', 7) =} | {= NEAR('2s8fe', 8) =} | {= NEAR('2s8fe', 9) =} |
| a DR-1s | {= NEARAVG('1s') =} | {= NEAR('1s', 6) =} | {= NEAR('1s', 7) =} | {= NEAR('1s', 8) =} | {= NEAR('1s', 9) =} |
| any DR-xs | {= NEARAVG('xs') =} | {= NEAR('xs', 6) =} | {= NEAR('xs', 7) =} | {= NEAR('xs', 8) =} | {= NEAR('xs', 9) =} |

- The first row is wen's other question ([[D20015]]), "Is the distribution for scrambled->DR movecount known?": per colour it is the exact 1, 4, 50, 592, 7156, 87236, 1043817, 12070278, 124946368, 821605960, 1199128738, 58202444, 476 over the 2,217,093,120 cosets (0 to 12 moves), and the row is the best of six.
- The last row is trangium's "almost always a linear 7-mover on some axis and side, around half the time a 6-mover, and pretty much never a 5-mover" ([[T10696]]): {= NEAR('xs', 7) =}, {= NEAR('xs', 6) =}, and {= NEAR('xs', 5) =} for 5 or less.
- A DR-1s exists about {= f1(float(NEARAVG('dr')) - float(NEARAVG('1s'))) =} moves earlier than a real DR, and costs {= D1() =} in the finish. That is the whole trade in two numbers: on average it is close to even, so it pays when you find the short ones.

### 6.5 From an EO pattern to a kind

When the route keeps the EO of an axis, the EO pattern you start from decides what you can land on. Appendix B has the full table: for every pattern that is uniform by slice (each slice's four pieces all good or all bad) and each pair of faces for the corners, what the DR-xs is. Rodney's list of patterns that guarantee an extra-good case ([[T11232]]) and count quackula's two lists (the 12-bad notes and the guaranteed-fix cases) can be read straight off it. All of them check out except one line, the 12-bad one in Rodney's list (section 8).

---

## 7. On 500 real scrambles

{{REAL}}

---

## 8. The claims, checked

Statements that a computer can settle, with what the numbers say. A scramble is given wherever something is refuted or a case is claimed to exist.

| Claim | Who | Verdict |
|---|---|---|
| DR-1s to DR is 6 moves at most, no 7 | Daichi, [[T12406]], [[T12408]] | **True.** Exactly 2 to 6 turns over the 70 layouts (4.2). A 6: `{= W6() =}` gives a DR-1s whose shortest fix is 6 turns. |
| The DR-1s to DR distribution is "basically flat", 3 moves is the median | Rodney, [[T12409]], [[T12410]] | **No.** 1, 2, 9, 30, 28 of 70 for 2 to 6 turns. Rodney's 3 is one half turn, one quarter turn and the slice with one of its two turns cancelling; counted that way the median layout is 4, and 5 from scratch. |
| "DR-2s needs at most 2 moves to reach DR-1s" | Rodney, [[T12409]] | **True** for the setup: 0, 1 or 2 moves, then the slice (4.3). |
| From DR-3s you get DR-2s in 0 moves with a slice that cancels with the last DR move | tseitsei89's tutorial | **True** for all {= NK(3) =} kinds of DR-3s. |
| The rule for the number of slices from centers and flipped edges | trangium's dr-fe examples doc, Rodney [[T10661]], the tutorial | **True**, all 768 kinds (section 3). |
| "1 slice can be fixed in 3 moves, and 2 slices can be fixed in 5 moves" | EO Meta Comparison doc (an assumption, stated as one) | As move counts to a real DR, about 2 short: {= FIXAVG(1) =} and {= FIXAVG(2) =} on average from scratch. As finish penalties, 3 is a little high for a DR-1s (+{= D1() =}) and 5 much too high for a DR-2s 8fe (+{= D8() =}). |
| A DR-1s finish is about 2.2 to 2.4 longer than a DR's on optimal; a DR-2s 8fe about 1 | trangium, in the tutorial and [[T10847]], [[T11138]] | **Consistent.** trangium's are optimals. With the best finish of the method's form, on {= N1() =} and {= N8() =} states: +{= D1() =} and +{= D8() =}, 0.1 to 0.4 above trangium's by subset. |
| "8 move DR-1s is on average better than an 11 move DR but worse than 10 move DR" | the tutorial | **Holds** with these finishes: at +{= D1() =} an 8-move DR-1s is {= f2(float(D1()) - 2) =} behind a 10-move DR and {= f2(3 - float(D1())) =} ahead of an 11 (5.3). |
| 3-1 is bad, 2-2 is good, 4-0 is great | Rodney [[T10832]], tseitsei89 [[T10822]] | **Right order, small effect** except for one case: {= SPLIT('3-1') =}, {= SPLIT('2-2') =}, {= SPLIT('4-0') =} average finish, and the 4-0 is only good when the slice is the one that fixes (5.4). |
| An extra-good DR-1s is "just 1-2 moves worse than full DR" | Rodney, [[T11232]] | **On average**, +{= f2(float(SPLIT('4-0')) - float(AD())) =}: +{= BETTER(2, 'diff') =} when the four are in the slice that fixes, +{= OTHER4('diff') =} when they are in the other one. |
| Slice EO for a given slice "is never more than 2 moves away" | FakeMMAP, [[T10773]] | **True**, exactly, counting all-misoriented as a slice EO (6.1). |
| A slice-EO skip for one slice and axis has chance 1 in 8 | tseitsei89, count quackula, [[D19427]] | **True.** And at least one on a scramble: {= SKIP4('normal') =} on normal, {= SKIP4('both') =} with inverse. |
| A misoriented slice EO gives a DR-1s only on an axis with 8 bad edges | tseitsei89 [[T11009]], trangium [[T11357]] | **True** for routes that keep the axis's EO, and {= SHR('eo-fb_1s | A misoriented') =} of misoriented skips qualify (6.2). |
| "The chance of getting 4 flipped edges in general is 55%" | Rodney, [[T11566]] | **True**: 70 in 128. |
| The optimal linear dr-fe distribution 1, 4, 50, 586, … | trangium, [[T11332]] | **Reproduced exactly.** |
| "almost always a linear 7-mover on some axis and side, around half the time a 6-mover, and pretty much never a 5-mover" | trangium, [[T10696]] | **Right for 7 and 6**: {= NEAR('xs', 7) =} of scrambles have a 7, {= NEAR('xs', 6) =} a 6. A 5 or shorter is there on {= NEAR('xs', 5) =}, one scramble in {= f'{100 / float(NEAR("xs", 5).rstrip("%")):.0f}' =} (6.4). |
| Six edge-orientation patterns that guarantee an extra-good DR-xs | Rodney, [[T11232]] | **Five of six.** "All edges misoriented (12 bad) -> FB on UD will be extra-good -1s" is not a DR-1s: it is a DR-2s with four flipped edges of one slice. {= W12() =} trangium's fix ([[T11234]]), "FB-colored misoriented, others oriented", is right. count quackula's 12-bad notes already had it: "If the CO color is green/blue: This is a DR-2s 4fe." |
| The cases with a fix to DR guaranteed in net +4 or less | count quackula's guaranteed-fix doc | **All consistent** with Appendix B, case by case. |
| Step 3 of the slice-DR method: 1, 4, 9, 40, 16 cases of 70 at 2 to 6 moves | Simon's slice-DR doc | **Four cases off**: {= SIMON() =} (4.2, Appendix A). |

---

## 9. What this does not cover

- **Findability.** "Finish" is the best solution of the method's form, exact per state. What a person finds in the time is trangium's and tseitsei89's ground, and their tables in the tutorial are the data.
- **Solutions outside the form.** True optimals from a DR-1s are 0.1 to 0.4 shorter on average (trangium's nissy numbers against mine). For a DR-2s 8fe the form has the two slices together; solutions with moves between them are not searched.
- **DR-2s other than 8fe, and DR-3s.** Only their move counts to DR (section 4). trangium's nissy averages for them are +2.7 to +3.0 and +3.0 to +3.5.
- **NISS inside the route, and EO-changing moves.** A slice EO is taken on normal or on inverse, the route to the DR-xs stays on that side and keeps that axis's EO. The finish uses both sides. So the counts of section 7 are a floor on what is there.
- **Normal DRs through an EO longer than 5 moves.** The normal-DR lists of section 7 come from cubelib-cli, which lists no EO longer than 5.
- **EO-breaking triggers and the EO-shifting ideas** from the EO-free trigger doc. The route rule here keeps the EO of one axis; 6.2 shows what dropping that rule could gain at most.
- **Time.** Section 7 counts what there is to find and to finish. How long a check takes is for the people who do them; the stated times I could find are in section 7.

---

## Appendix A: every DR-1s layout

{{APP_A}}

---

## Appendix B: from an edge-orientation pattern to a kind of DR-xs

{{APP_B}}

---

## Appendix C: how it was computed, and what checks it

{{APP_C}}

---

## Docs referred to

- tseitsei89 (Janne Lehtimäki), [DR-Xs](https://docs.google.com/document/d/1_uLVLB5xqDm40NugXE5rjc8LgEtuHQCLz0odKY6mboE), 2 Feb 2026: the tutorial; trangium's averages and findability tables are in its sections 2 and 6.
- Rodney Kinney, [EO Meta Comparison](https://docs.google.com/document/d/131VWYrL3Z4t6p0fBGkHZ73w6arF8A7PEqRuNjsIQMGo), Jan 2026.
- trangium, [dr-fe examples](https://docs.google.com/document/d/11Xu6BpEBLu-v8hVbFzneSqeMjHb83q_zurWb_V0DXDY), 19 Jan 2026: the rule for the number of slices.
- count quackula, [12 bad dr-xs notes](https://docs.google.com/document/d/1-anqtLsBGg_oBvzz1TTf_6Mjsypv4jMkFhB9E8cwkQM) and [guaranteed-fix cases](https://docs.google.com/document/d/190aVmEQFLILHGhrtuf1YFai0SYrsu_tWRYAWOe62P6U), Feb 2026.
- Simon, [Slice DR](https://docs.google.com/document/d/15zDJ9_FQIYVgHLbt1eHdOPtEp10jFOOae_U8DTaH7tk), Jul 2025.
- The first study of this site, [Judging a DR by hand](../judging-a-dr/): the exact optimal finish of every DR state, used here for every finish.
