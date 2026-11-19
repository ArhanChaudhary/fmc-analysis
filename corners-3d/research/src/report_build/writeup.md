# Corners in 3D: how far from HTR, and which turn gets closer

Take the corners of any state, not just a DR. Hold DBL still and turn only R, U and F. What can you see on them that says how far they are from HTR, what can you *prove* from it, and does it tell you the turn that gets closer? That's what this page answers. Everything is exact over all {= n(N) =} corner states, and the theorems are checked in Lean.

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion).

**This builds on** what the server already has. Pretty much every piece existed for DR corners; this page takes the DR axis away.

- **rodneykinney's [*Hyper-Parity*](https://docs.google.com/document/d/1Onc2lu5iW_ODnT71oN5lgpVVjVqbvUMzaylzxgykx0I)** (June 2020): the tetrads, the three conditions for HTR ("We call the method “Hyper-Parity” because there are three parity-like conditions that must all be satisfied to bring the cube into HTR."), the FB labels 0c / 4a / 4b / 2c, the UD labels 4a / 4b / 4c / 4d, the maze and the funnel.
- **The subset names** 0c0 … 4b5, from wen and exhaustingg's sheet [*HTR better smh (v2)*](https://docs.google.com/spreadsheets/d/1ZhulzHeNgv2Hiy4x9R1MzsMRlPlI-E8DRiHFJlPlboM), and zakimoshi's list of the 14 of them ([[T4226]]).
- **zakimoshi's 3d maze** ([[D13316]], [[D13318]], [[D13333]]): "I really think the 3d maze should be explored more", "Like how qts on other axes effect your subset", and the recognition: "To find the bad corners all you have to do is look for ones with exactly 1 oriented sticker". This page is that maze.
- **beef beans' quarter-turn count of a scrambled cube** ([[T2644]]): twist every corner flat on any axis and read the subset, "so the orientation of the corners dosen't really matter, the corners always have a number of quarter turns it takes to solve them." torchlight's reason ([[T2657]]): "R and [D2 L2 : U'] permute corners in the same way". FakeMMAP's proof ([[T2693]]). And zakimoshi's catch ([[T2685]]): "orienting corners requires you to change the qt", "You need to solve them together which makes it much more complicated".
- **Jules Porteners' table** ([[T6774]]) for Zagros's question "Anyone know if there are 2x2 scrambles that take >5qt to solve?" ([[T6773]]): "sometimes 8 qt is required", with the count of states at each number of quarter turns.
- **The DR counts**: Radek B's quarter turns for all corner permutations, by shape ([[D7214]], [[D7223]]), FakeMMAP's over all 7! corner cases ([[T2870]]), Shota's subset ratios ([[D7231]]).
- **Triple DR and fake HTR**: six triple DRs up to half turns (zakimoshi asked, [[T1929]]; trig0n and Tom Nelson answered, [[T1934]], [[T1946]]), FakeMMAP's group orders with DBL fixed ([[T7003]]), KrzychXyz's "DR on all axis, but not HTR" ([[T7274]]), torchlight's Klein 4-group rule ([[T5519]], [[T5520]]).
- **FakeMMAP's Lemma 1 and Corollary 2** ([[T9509]]): "Lemma 1: If triple DR and OBL are solved, and there is even parity, then the state is in true HTR." and "Corollary 2: if you know the U/D pattern, the positioning of bad corners, and corner parity, then you know exactly the HTR solution."
- **Louis's bound** ([[T6177]]): "as a first step we could consider distance to triple DR which is a lower bound to distance to HTR and doesn't require messing around with corner permutation". Zagros's reply ([[T6178]]): "I don't think it should be possible to determine distance to htr, only to fake htr, since you could always cycle three corners and have the exact same orientations on every axis". Nobody posted numbers for either.
- **rodneykinney's CO maze** ([[T3223]], [the gist](https://gist.github.com/rodneykinney/fd3473e7cc514ae192e4eb538dd134a7)): corner orientation on one axis as a maze. Their own verdict: "Still too complicated to keep in your head, IMO".
- **The H48 solver** of Sebastiano Tronto ([its doc](https://github.com/sebastianotronto/nissy-core/blob/master/doc/h48.md), quoted on the server by Arch, [[T8011]]). Its target: "Each corner is placed in the corner tetrad it belongs to, and it is oriented." And it already keeps a bound from the same read as this page's types: its corner table "also stores a preliminary pruning value based on the corner coordinate", the coordinate being corner orientation plus which tetrad each corner is in. So a program has had Louis's bound all along. What wasn't known is how tight it is and what a person can do with it.
- **Joba's lower bounds with NISS** by quarter turns ([[T6639]]).

**What this adds:**

- **The six things a corner can show, and the rule for what a quarter turn does to them** on any axis (section 4). Proved for every state.
- **Types alone find real HTR exactly 1 time in 6**, whatever the rule. With parity it's 1 in 3 at best, with the D-colour corners 1 in 2 at best, with both it's settled. The test for HTR is still Hyper-Parity's three conditions, with *every corner good* in place of the FB condition: FakeMMAP's lemma with the DR axis gone (section 5).
- **Fake HTR is exactly 9 moves from HTR**, all {= R['allgood']['fake'] =} of them, even with every R, U and F turn allowed (section 5).
- **Floors you can prove**, with how tight each one is: a count table you read at a glance, the types floor (Louis's distance to triple DR and H48's corner bound, measured against the truth), the parity and colour upgrades, and which of them survive NISS (section 6).
- **Which turn gets closer**, graded by distance, next to the best any rule could do with the same read (section 7).
- **What the twist costs on top of beef beans' count**: 0, 2, 4, 6 or 8 quarter turns (section 8).
- **DR corners seen from outside DR**: no quarter turn is ever saved, but 1 or 2 moves are on {= pc((R['dr']['save'][1] + R['dr']['save'][2]) / R['dr']['states'], 0) =} of the cases (section 9).
- **The mazes**: rodneykinney's two small ones don't change off the DR axis, and there are only five kinds of 2-qt pattern (sections 5, 8 and 10).

**Terms.**

- *HTR* here means corners that half turns solve: the 24 states R2, U2 and F2 reach. *Solved* on this page means HTR.
- *Tetrads*: UFR-UBL-DFL-DBR and UFL-UBR-DFR-DBL. A corner is *out* when it sits in the other tetrad, so half turns can't bring it home. That's zakimoshi's bad corner without an axis.
- A sticker is *oriented* when its colour belongs to the axis of the face it's on (a white or yellow sticker on U or D, and so on).
- A corner is *good* (in its tetrad, all three stickers oriented), *twisted* (in its tetrad, none oriented) or *out* (exactly one oriented). The *types* of a state, or its *type pattern*, are the type of every corner, place by place.
- *All good* is triple DR: DR on all three axes at once. It's HTR or a *fake HTR*.
- *D-colour corners*: the four corners that carry DBL's U/D colour (yellow, if you scramble white top green front). Their *picture* is where they sit, labelled 4a / 4b / 4c / 4d as in *Hyper-Parity*.
- *4a* and *4b* get used for two things, as in *Hyper-Parity*: the shape of four out corners (the 4a of 4a1) and the picture of the D-colour corners. I always say which.
- *Parity*: even or odd placement of the corners. A quarter turn flips it, a half turn doesn't.
- *Moves* are HTM. *Quarter turns* (qt) are counted with half turns free, like the number in a subset name.
- *One side* means every move on the normal scramble. *NISS* means moves on both sides.
- A *floor* is a number proved to be at most the true distance: you can't do it in fewer.
- *Subset number of the placement*: beef beans' count. Forget the twists, read the subset.
- *Look-alikes*: states that show the same thing. Six HTR cases look alike on the types alone.

Types are written as seven characters in the order UFR UFL UBL UBR DFR DFL DBR: `.` good, `+` twisted clockwise, `-` twisted counter-clockwise, `r` `u` `f` out with only the R/L, U/D or F/B sticker oriented. After the scramble R that's `r . . r r . r`.

**How to read it.** Section 1 is the whole answer. Each read is marked with what it takes: *at a glance* (typing a corner is looking at its three stickers), *tracing* (parity), *a search* (finding a way to make every corner good) or *computer only*. Section 6 is the reference for floors, section 7 for the next turn. The examples file has the catalogue of every pattern within 3 moves of all good, 200 random states to try, and DR cases solved both ways. [The lookup page](tool/) does all the reads and floors for any scramble you type. All numbers are exact counts over the {= n(N) =} states.

{{CONTENTS}}

## 1. The short version

**New here:**

- **A corner shows one of six things, and a quarter turn changes them by one rule.** Good, twisted (two ways) or out (three ways, by which sticker is still oriented). A quarter turn of a face does this to its four corners: good ↔ out with that face's axis oriented, twisted ↔ out with another axis oriented. Half turns only move corners around. You read all of it at a glance. (Section 4.)
- **Types alone can't find HTR more than 1 time in 6.** Each type pattern is shared by {= R['allgood']['n'] =} states, and any sequence that makes one of them all good makes all of them all good: {= R['allgood']['htr'] =} land in HTR and {= R['allgood']['fake'] =} in a fake HTR. So when a rule that reads only the types has made every corner good, it's in real HTR for exactly 1 state in 6. A rule that also reads parity gets 1 in 3 if it aims for an even number of quarter turns left, and one that reads the D-colour corners gets 1 in 2 if it aims for a 4a picture. Types + D-colour corners + parity settle it. (Section 5.)
- **A fake HTR is exactly 9 moves from HTR**, every one of the {= R['allgood']['fake'] =}, with all nine turns allowed. Off-axis turns don't help. So if you're k moves from a fake HTR, you're at least 9 − k from the real one.
- **Floors.** Mean distance to HTR is {= f2(R['mean_d']) =} moves.
  - The count table (how many twisted, how many out per axis; at a glance): {= f2(floor_by_key('count')['mean']) =} on average. Weak, but free.
  - The types floor, which is Louis's distance to triple DR: {= f2(floor_by_key('types')['mean']) =} on average, exact on {= pc(floor_by_key('types')['exact']) =} of states, exact or 1 short on {= pc(floor_by_key('types')['within1']) =}.
  - With parity: {= f2(floor_by_key('types_par')['mean']) =}, exact on {= pc(floor_by_key('types_par')['exact']) =}. With parity and the D-colour corners: {= f2(floor_by_key('both')['mean']) =}, exact on {= pc(floor_by_key('both')['exact']) =}, never more than {= floor_by_key('both')['maxgap'] =} short.
  - Two twisted corners and nothing else: at least {= R['only_twisted']['2']['min_d'] =} moves and {= R['only_twisted']['2']['min_q'] =} quarter turns. Twists are what's expensive.
- **Which turn gets closer.** Within 4 moves of HTR, following the types is always right. At 5 it's right {= pc(moves_row(5)['types']) =}, at 6 {= pc(moves_row(6)['types']) =}, at 7 {= pc(moves_row(7)['types']) =}, and at 8, where half of all states are, {= pc(moves_row(8)['types']) =}, which is what a random turn gets ({= pc(moves_row(8)['random']) =}). The best single table on the types is right {= pc(moves_row(0)['t_types']) =} of the time over all states, and no rule on the types could beat {= pc(moves_row(7)['c_types']) =} at 7 even if it knew the distance. Far out the types don't know. (Section 7.)
- **The quarter-turn count is beef beans' count plus what the twist costs**: +0 for {= share(R['perm']['surcharge'][0]) =} of states, +2 for {= share(R['perm']['surcharge'][2]) =}, +4 for {= share(R['perm']['surcharge'][4]) =}, +6 or +8 for the rest. Always even. (Section 8.)
- **Leaving DR saves moves, never quarter turns.** Of the 210 DR corner cases, {= sum(X['dr_subsets'][k]['saved'][1] for k in SUBSETS) // 24 =} are 1 move closer to HTR with off-axis turns and {= sum(X['dr_subsets'][k]['saved'][2] for k in SUBSETS) // 24 =} are 2 closer. Every 5-qt case is. The shorter solution nearly always spends 2 or 4 more quarter turns than the subset number to do it. Corners only, of course. (Section 9.)
- **Orienting first costs.** Optimal CO on the best of the three axes and then the best DR-only finish is {= f2(R['staged']['mean_best'] - R['mean_d']) =} moves longer than the optimal on average, and it's optimal for only {= share(R['staged']['best'][0]) =} of states.
- **With NISS** the mean drops to {= f2(X['niss']['mean']) =} and God's number from {= len(R['hist_d']) - 1 =} to {= len(X['niss']['hist']) - 1 =}. Every floor in quarter turns still holds with NISS. The one-sided move floors don't: the types floor is too high for {= pc(X['niss']['linear_types_floor_broken']) =} of states once you allow moves on the inverse. (Section 6.)
- **Within 2 quarter turns of HTR there are only five kinds of pattern** besides the 4a face. Three of them don't exist on a DR. (Section 8.)

**Carries over from DR as it is** (known there, checked here for every state):

- **The test for HTR**: every corner good + D-colour corners in a 4a picture + even parity. Those are Hyper-Parity's three conditions with *every corner good* in place of the FB one, and FakeMMAP's Lemma 1 with all six pictures. You don't solve anything first; parity is still a trace. (Section 5.)
- **The subset number.** Quarter turns on the other axes never lower it: that's FakeMMAP's argument for beef beans' count, read the other way. (Section 9.)
- **rodneykinney's two small mazes** (out corners, D-colour corners), with the same 0 / 1 / 2 / 3 and 0 / 1 / 2 / 1 quarter turns. What 3D adds is the twist. (Sections 5, 8 and 10.)

**Confirmed:** Jules Porteners' table, FakeMMAP's counts over 7!, Shota's ratios, beef beans' axis-independence, torchlight's Klein 4-group rule, FakeMMAP's lemma, Joba's NISS bounds 1 / 2 / 4 / 6 / 8 with 0c3 at 6, and Yura Riabov's 11 to HTR. Section 11 has all of them.

**Corrected** (the errata page has the example): wen's 13-move 4a4 has a 12 inside DR turns. beef beans's sheet already had 12 as the longest for that subset, and 13 only for 2c5; the full search agrees.

## 2. What was asked

1. Which things you can see on the corners (wrong tetrad, orientation per axis, the pieces of a subset name) say how far a state is from HTR? *Answer*: sections 4 to 6 and 8.
2. How do I prove a state can't be solved in fewer than X moves from those patterns? *Answer*: section 6.
3. Which turn gets closer? *Answer*: section 7. Near HTR the types say it. Far out they don't, and section 7 says how far any rule could go.
4. Mazes and flow charts. *Answer*: sections 4, 5, 8 and 10.

And from the server:

5. zakimoshi's 3d maze: "Like how qts on other axes effect your subset" ([[D13318]]). *Answer*: sections 4, 8 and 9.
6. Louis's distance to triple DR as a bound ([[T6177]]), and Jay's wish for move counts to HTR from two axes ([[T6170]]). *Answer*: section 6.
7. JTuu: "it'd be interesting if we could know whether each qt is +1 or -1 just by looking at the moves" ([[T2652]]). *Answer*: section 8.5, partly.
8. Joba, on the tetrad twist: "There *has* to be a way to avoid having to actually solve the corners" ([[T3886]]). torchlight gave one that computes it ([[T3889]]). *Answer*: section 5.3 has one you read off the stickers.
9. mrauo: "What is CO movecount distribution?" ([[T3196]]). FakeMMAP gave the best cases for Jay's version of it ([[T3215]]). *Answer*: section 9.4 has the whole distribution, for this move set.

## 3. The model, and what carries over to a real cube

DBL never moves and only R, U and F turn. That's every corner state up to turning the whole cube: $7! \times 3^6$ = {= n(N) =} of them. rodneykinney in *Hyper-Parity*: "It is always possible to solve corners up to rotation using only R/U/F moves." FakeMMAP counts the same way ("we consider corners only, and assume DBL to be fixed", [[T7003]]).

What carries over to a real cube:

- **Every floor does.** A real solution into HTR with any of the 18 turns becomes an R, U, F sequence of the same length here, with the same number of quarter turns (L is R seen from the other side, and so on). The same goes for a solution with moves on both sides. So a state that needs at least X here needs at least X on the cube, with or without NISS, for the corners and so for everything.
- **The distances are a little short for a real cube.** Here U D' is HTR, because the corners only went round with DBL. On a cube it's two moves from HTR. That's the usual rule of the subset names, zakimoshi's "0c // htr/fake (8 is equivalent by slice)" ([[T4226]]).

One row per number of moves. *One side* is every move on the normal scramble, and *with NISS* allows moves on both sides.

{{ t_moves() }}

God's number is {= len(R['hist_d']) - 1 =} on one side and {= len(X['niss']['hist']) - 1 =} with NISS. The means are {= f2(R['mean_d']) =} and {= f2(X['niss']['mean']) =}. NISS saves nothing on {= share(X['niss']['saves'][0]) =} of states, 1 move on {= share(X['niss']['saves'][1]) =}, 2 on {= share(X['niss']['saves'][2]) =} and 3 on {= share(X['niss']['saves'][3]) =}.

Half of all states are 8 moves out ({= share(R['hist_d'][8]) =}), and {= share(R['hist_d'][7] + R['hist_d'][8] + R['hist_d'][9]) =} are 7, 8 or 9. So a rule that *predicts the distance within one move* is worth nothing on its own: always saying 8 does that. That's why the floors below are graded by how often they're *exact*, and the rules of section 7 by whether their turn gets closer.

The same in quarter turns, with half turns free. The states column is Jules Porteners' table ([[T6774]]), which this search reproduces to the last state.

{{ t_quarters() }}

## 4. Reading a corner

### 4.1 The six types

Look at a corner's three stickers and count the oriented ones.

- **3 oriented: good.** The corner is in its tetrad and not twisted.
- **0 oriented: twisted.** It's in its tetrad, twisted clockwise or counter-clockwise. For the rule below it's easier to say where its U/D sticker is: on an F/B face or on an R/L face.
- **1 oriented: out.** It's in the wrong tetrad. Three kinds, by which sticker is the oriented one: R/L, U/D or F/B.

That's all there is. 2 oriented never happens, and the count tells you the tetrad. This is zakimoshi's "exactly 1 oriented sticker" ([[D13333]]) and the H48 remark that "For a corner that is placed in its own tetrad, the orientation does not depend on the reference axis chosen" ([[T8011]]), put together and proved for every corner of every state.

Why it's true: a quarter turn keeps the sticker on the turning face where it is and swaps the other two between their axes. It also carries the corner to the other tetrad. So every quarter turn is one swap of two stickers and one change of tetrad, and they stay in step: an even number of swaps (0 or 3 stickers off) in your own tetrad, an odd number (exactly 2 off) in the other.

On a DR every corner is good or out with the DR axis oriented. So the bad corners of a subset name are the out corners, and *4a*, *2c* are shapes of out corners.

### 4.2 What a turn does

A half turn moves corners inside their tetrads and changes no type. A quarter turn of a face does this to the four corners on it, either direction:

- good ↔ out with that face's axis oriented;
- twisted ↔ out with one of the other two axes oriented.

So a U turn fixes the `u` corners on U, breaks the good ones into `u`, turns `r` and `f` corners into twisted ones and twisted ones into `r` or `f`. The full table, one row per face:

{{ t_rule() }}

Read backwards it's the same table: every line goes both ways.

{{ fig('types', 'Every line is a quarter turn of the face named on it, for a corner on that face. Nine lines, and no line between two types on the same side.') }}

You don't need the table at the cube. Look at the two stickers that are *not* on the turning face: they trade faces. Whatever lands on a face of its own axis is oriented after the turn.

**What it means for a solution.** An out corner needs an odd number of quarter turns, and the one that fixes it is a turn about the axis of its oriented sticker: a `u` corner wants a U turn, so it has to be on U for that. A twisted corner needs two quarter turns on two different axes. A good corner on a face you turn has to be paid back.

### 4.3 A floor from that, by hand

Give a good corner 0, an out corner 1 and a twisted corner 2, and add up. Call it the weight. A quarter turn changes four corners by exactly 1 each, so the weight moves by at most 4, and a half turn doesn't move it. So:

> you need at least weight / 4 quarter turns, rounded up.

It holds with NISS too. It's a weak floor ({= f2(floor_by_key('weight', True)['mean']) =} quarter turns on average against a true {= f2(R['mean_q']) =}): turns hit four corners of one face at a time and you can't choose which four. The count table of section 6.3 is the same idea done exactly.

## 5. Three reads fix everything: types, D-colour corners, parity

### 5.1 All good is six things

{= R['allgood']['n'] =} states have every corner good. That's triple DR. Only {= R['allgood']['htr'] =} of them are HTR.

{{ t_fake() }}

This is the six triple DRs of trig0n and Tom Nelson ("you have 3 options for corners (3-cycle, inverse, solved) and 2 options for parity = 3*2", [[T1946]]) and torchlight's rule ([[T5519]], [[T5520]]): compare the placements of the two tetrads, and they agree up to the Klein 4-group for HTR, are a 3-cycle apart for the even fake, anything else for the odd one. It checks out on all {= R['allgood']['n'] =} (section 11).

What's new is the last column. I expected off-axis turns to give some fake HTR a shortcut. They don't: all {= R['allgood']['fake'] =} are exactly 9 moves from HTR, with any turns. With NISS it's {= X['dr_subsets']['0c3']['allniss_min'] =} to {= X['dr_subsets']['0c3']['allniss_max'] =} for the odd ones and {= X['dr_subsets']['0c4']['allniss_min'] =} or {= X['dr_subsets']['0c4']['allniss_max'] =} for the even ones.

```
U R2 U F2 U2 R2 U F2 U     // KrzychXyz's fake HTR: every corner good, {= S("U R2 U F2 U2 R2 U F2 U")['q'] =} qt
{= S("U R2 U F2 U2 R2 U F2 U")['sol'] =}    // {= S("U R2 U F2 U2 R2 U F2 U")['d'] =} moves to HTR with off-axis turns. Staying in DR is {= S("U R2 U F2 U2 R2 U F2 U")['ddr'] =} too.
```

### 5.2 Why the types can't tell

Take any state and any sequence that makes all its corners good. The types of a state follow the rule of section 4.2 and nothing else, so the same sequence makes every state with those types all good. There are {= R['allgood']['n'] =} such states, they end on {= R['allgood']['n'] =} different all-good states, and {= R['allgood']['htr'] =} of those are HTR.

So a rule that reads only the types, however clever, has exactly 1 state in 6 in HTR at the moment it makes every corner good, and the other 5 in a fake HTR. That's JTuu's and Zagros's point made exact. JTuu ([[T6171]]): "wouldn't a 2c within each tetrad always generate a case with the same drm/arm features but very different distance to htr?" Zagros ([[T6178]]): you "could always cycle three corners and have the exact same orientations on every axis".

It's the reason a types floor is a floor and not the distance, and the reason the turn it picks stops being right far out.

### 5.3 What does tell: the D-colour corners, and parity

**Parity** removes three of the six. The number of quarter turns in any solution into HTR is even for an even placement and odd for an odd one. So a way to all good with the wrong number of quarter turns ends in a fake HTR for sure. (Parity is a trace.)

**The D-colour corners** remove the rest. Look at where the four corners with the D colour are (DBL is always one of them), wherever their D stickers face. Count them by tetrad:

- 2 and 2: *4a* if the two pairs are on the same face or on opposite faces, else *4b*;
- 3 and 1: *4c*;
- 4 and 0: *4d*.

These are rodneykinney's UD labels, and you read them at a glance.

> **A state is HTR exactly when every corner is good, the D-colour corners are in a 4a picture, and parity is even.**

There are six 4a pictures. Besides DBL the D colour is on: {= '; '.join(R['colour']['six']) =}.

You need all three conditions. Two fake HTRs, each failing one:

```
U R2 U F2 U2 R2 U F2 U       // all good, parity {= S("U R2 U F2 U2 R2 U F2 U")['parity'] =}, but the D-colour corners are {= S("U R2 U F2 U2 R2 U F2 U")['colour'] =}
U R2 U2 F2 U R2 U2 F2 U      // all good, D-colour corners {= S("U R2 U2 F2 U R2 U2 F2 U")['colour'] =}, but parity is {= S("U R2 U2 F2 U R2 U2 F2 U")['parity'] =}
```

This is FakeMMAP's Lemma 1 ([[T9509]]) off the DR axis. Their version has OBL solved, which is the one picture with the D face whole, and gives the 4 states U2, R2 F2 R2, R2 F2 R2 U2 and solved. With all six pictures you get all 24.

Joba wanted "a way to avoid having to actually solve the corners" for the tetrad twist ([[T3886]]), and torchlight gave one that computes it: number the corners so that opposite corners have the same number and compare the two tetrads ([[T3889]]). This is the same thing read off the stickers: an even all-good state has no tetrad twist when its D-colour corners are 4a, and has one when they're 4b.

{{ fig('colour', 'The UD maze of Hyper-Parity, with turns on all three axes. The labels and the quarter turns are the same.') }}

A quarter turn can keep you in 4a or in 4c and always moves you out of 4b and 4d, exactly as in *Hyper-Parity*: "it is possible to remain in 4a or 4c, but not in 4b or 4d". Nothing changes off the DR axis, because this picture never looks at where a sticker faces.

### 5.4 How much each read settles

One row per set of reads. The fourth column is for a rule that sees only that read, at the moment it has made every corner good.

{{ t_reads() }}

- Types + D-colour corners + parity determine the moves to HTR and the quarter turns of every state. That's FakeMMAP's Corollary 2 for all corner states.
- Types + the D-colour corners + the B-colour corners determine the whole state, with no tracing: {= n(R['colour']['types_two']) =} different things to see for {= n(N) =} states.
- Parity does most of the work for quarter turns ({= pc(R['fix_types_par_q']['fixed']) =} of states settled), the colour most of it for moves.

## 6. Floors: proving a state needs at least X

### 6.1 What makes a floor a proof

A floor is any number f you can read off a state with two properties: it's 0 on HTR, and no single turn lowers it by more than 1. Then a solution of n moves can't start from a state with f above n. That's the whole argument, and it's proved once in Lean for any such f.

Most of the floors below are the distance to something easier than HTR:

- forget everything but which corners are out: the distance to *all corners in their tetrads*;
- forget the pieces and keep the types: the distance to *all good*. That's the **types floor**, Louis's distance to triple DR;
- keep the types and the parity: the distance to an *even* all-good state;
- keep the types and the D-colour corners: the distance to an all-good state with a 4a picture.

HTR is inside each of those targets, so each distance is a floor. They're exact tables from a full search; the types floor and the parity floor are also checked state by state in Lean. The count table of 6.3 and weight / 4 are floors for other reasons: the first is the smallest distance among all states with the same counts, the second is the argument of 4.3.

### 6.2 The ladder

One row per floor, for solutions on one side. *Exact* is the share of all states where the floor equals the true distance.

{{ t_floors() }}

- **The types floor is the big step.** Counting gets you to {= f2(floor_by_key('count')['mean']) =}, orienting on the best axis to {= f2(floor_by_key('co3')['mean']) =}, and the types to {= f2(floor_by_key('types')['mean']) =} of the true {= f2(R['mean_d']) =}. It's Louis's bound, and it "doesn't require messing around with corner permutation" ([[T6177]]). It's also the kind of bound H48 keeps for its corner coordinate.
- **Where it falls short it's because of 5.2**: the nearest all-good state is a fake one. The types floor is short by 1 on {= share(R['d_minus_types'][1]) =} of states, by 2 on {= share(R['d_minus_types'][2]) =}, by 3 or more on {= share(sum(R['d_minus_types'][3:])) =}.
- **Parity and the D-colour corners each remove fakes.** Together they leave the floor exact on {= pc(floor_by_key('both')['exact']) =} of states.
- **The placement alone is a poor floor in moves** ({= f2(floor_by_key('perm')['mean']) =}). It's much better in quarter turns (section 6.5).

How you get the types floor at the cube: it's the length of the shortest way to make every corner good. Within 3 moves that's {= E['catalogue_patterns'] - 1 =} patterns besides all good itself, {= len(E['catalogue']) - 1 =} up to symmetry, listed in the examples file; if yours isn't one of them, the floor is at least 4. Beyond that it's a search, and what you find is an upper bound on the floor until you've ruled out shorter ways. The exact table is computer only; [the lookup page](tool/) has it.

### 6.3 The count table

This one is read at a glance: count the twisted corners, and count the out corners by which sticker is oriented (R/L, U/D, F/B). Sort the three out counts, biggest first. The row gives the fewest moves any state with those counts needs, on one side and with NISS, and the fewest quarter turns. Every row is exact and has a state that meets it.

{{ t_count() }}

How to use it: your state can't be done in fewer than the row says. Nothing more: leaving out the all-good row, the mean distance of the states in a row is between {= f2(min(r['mean_d'] for r in R['count_table'][1:])) =} and {= f2(max(r['mean_d'] for r in R['count_table'][1:])) =} whatever the row, so the floor is usually far below the truth. It's on average {= f2(floor_by_key('count')['mean']) =} moves.

What the table is good for is the rows that stand out:

- **No out corner, some twisted**: with 2, 3 or 7 twisted corners these are the most expensive patterns there are.

{{ t_only_twisted() }}

- **Two out corners and nothing else** (the row 0 twisted, out 2): {= crow(0, [2, 0, 0])['floor_d'] =} moves and {= crow(0, [2, 0, 0])['floor_q'] =} quarter turns. That's 2c3 as the best case, and it's the same off the DR axis.
- **One twisted corner** never comes alone with nothing out, and with a pair of out corners (1 twisted, out 1 + 1) it's at least {= crow(1, [1, 1, 0])['floor_d'] =} moves and {= crow(1, [1, 1, 0])['floor_q'] =} quarter turns.

### 6.4 The 9 − k rule

From 5.1: a fake HTR is exactly 9 moves from HTR. So if you've found k moves that make every corner good and the result is fake, HTR is at least 9 − k away, on one side. With a short way to a fake HTR that's the best floor you'll get by hand:

```
{= E['random'][0]['scramble'] =}      // types {= E['random'][0]['kinds'] =}
{= E['random'][0]['types_solution'] =}                  // all good in {= E['random'][0]['floor_types'] =}, but it's a fake HTR
```

Here the types floor is {= E['random'][0]['floor_types'] =} and 9 − {= E['random'][0]['floor_types'] =} = {= 9 - E['random'][0]['floor_types'] =} says nothing more. The true distance is {= E['random'][0]['d'] =}. The rule earns its keep when k is small: 2 moves from a fake HTR means at least 7 from the real one.

### 6.5 Floors in quarter turns

The same ladder with half turns free.

{{ t_floors_qt() }}

- **Twist flat, read the subset** is beef beans' count. It's a floor because any solution also solves the placement. It's exact on {= pc(floor_by_key('perm', True)['exact']) =} of states and never off by an odd number (section 8).
- **The types floor in quarter turns** is the smallest count any state with those types can have. Think of it as the look-alike number: 1 for a 4a face, 2 for bars, 3 for two out corners, like the first numbers of the subsets with those shapes.
- With parity it's exact on {= pc(floor_by_key('types_par', True)['exact']) =}, and with the subset read on top {= pc(floor_by_key('types_perm', True)['exact']) =}.

### 6.6 With NISS

Two things to know.

**Every floor in quarter turns holds with NISS.** Moves on the inverse can't save a quarter turn: the count is the same on the inverse, and each quarter turn on either side changes it by 1. So weight / 4, the count table's quarter-turn column, the subset read and the types floor in quarter turns are all safe, and the number of quarter turns is itself a floor in moves.

**The one-sided move floors don't.** HTR isn't a normal subgroup, so a state can be far from HTR on normal and close with one move on the inverse:

```
{= X['niss']['witness_broken']['scramble'] =}     // types {= X['niss']['witness_broken']['kinds'] =}, types floor {= X['niss']['witness_broken']['types_floor'] =}, and it is {= X['niss']['witness_broken']['linear'] =} moves on one side
(F)            // one move on the inverse and it's HTR: {= X['niss']['witness_broken']['niss'] =} with NISS
```

The one-sided types floor is too high for {= pc(X['niss']['linear_types_floor_broken']) =} of states once NISS is allowed, by up to {= X['niss']['linear_types_floor_excess'] =} moves. The floors that hold with NISS, measured against the distance with NISS:

{{ t_floors_niss() }}

*Types on both sides* is the fewest moves, split any way between normal and inverse, that make every corner good. It needs the types on the inverse too, which is NISS tracing for the corners that aren't good. The count table has its own NISS column because the counts are the same on the inverse.

### 6.7 By hand, in order

1. Count twisted and out per axis. Look up the row. (*At a glance.*)
2. Weight / 4 if you only want quarter turns. (*At a glance.*)
3. If you can see how to make every corner good in k moves and you're sure nothing shorter does it, k is the types floor (one side). Check the end against section 5.3: HTR means k is the distance; fake means at least max(k, 9 − k). (*A search.*)
4. Parity tells you whether the number of quarter turns is even or odd. Add 1 to a quarter-turn floor of the wrong kind. (*Tracing.*)

## 7. Which turn gets closer

One row per distance. *Turns that get closer* is how many of the nine turns lower the distance. Each rule column is how often the turn that makes its floor smallest gets closer; when several turns tie, they share the credit.

{{ t_moves_rules() }}

- **Within 4 moves the types are always right.** A fake HTR is 9 away, so anything within 4 of HTR is at least 5 from every fake one, and the nearest all-good state is the real one. For a state that close, any shortest way to all good is a shortest way to HTR. (You don't know it's that close until you've checked the end: of the states with a way to all good in 4 or less, {= share(sum(R['hist_d'][:5]), sum(R['d_types_hist'][:5])) =} are.)
- **At 5 and 6 they're mostly right** ({= pc(moves_row(5)['types']) =}, {= pc(moves_row(6)['types']) =}), and the two extra reads fix what's left: with parity and the D-colour corners the floor's turn is right every time up to 6.
- **At 8, where half of all states are, the types floor is a random turn** ({= pc(moves_row(8)['types']) =} against {= pc(moves_row(8)['random']) =}). At 7 it beats chance ({= pc(moves_row(7)['types']) =} against {= pc(moves_row(7)['random']) =}) and is still wrong two times in three. By then the types floor is mostly pointing at a fake HTR.
- **At 9 and 10 most turns get closer anyway.**

Following a floor needs the floor of all nine results, so every rule column is *a search* at best and *computer only* far out. What a human can actually do is in the first bullet.

How far could any rule go that reads the same things? Two answers.

**The best single table.** For each thing you can see, write down the one turn that gets closer for the most states showing it. Over all states no rule on that read does better. Here's how that table does by distance:

{{ t_moves_table() }}

- **On the types the best table is right {= pc(moves_row(0)['t_types']) =} of the time**, against {= pc(moves_row(0)['types']) =} for following the types floor and {= pc(moves_row(0)['random']) =} for a random turn. It gets there by playing the far states, where nearly all states are, and it's wrong near HTR, where following the floor is always right. With {= n(R['patterns']) =} patterns it's not a table for a person either.
- **The counts carry nothing about the turn**: the best table on them is a random turn.

**A bound that holds even if you knew the distance.** Take each distance on its own and pick the best turn for each thing you can see among the states at that distance. No rule on that read can do better there. A real rule doesn't know the distance, so it does worse.

{{ t_moves_ceil() }}

- **On the types nothing can beat {= pc(moves_row(7)['c_types']) =} at 7 or {= pc(moves_row(8)['c_types']) =} at 8.** No rule of thumb on the types is going to tell you the turn from 7 or 8 out.
- **With all three reads the turn is determined**, since the distance is. The catch is the size of that table.

The rules of thumb I tried, for the record. Lowering the weight works exactly as far as you look ahead, and going for the shortest CO helps up to about 5 moves out. Past that both are a random turn.

{{ t_thumb() }}

With NISS there are 18 turns to choose from, 9 on each side:

{{ t_moves_niss() }}

**So, by hand:** read the types. If you can see a way to all good in 4 or less, it's the way to HTR as long as the end is HTR (section 5.3), and that check costs a glance at the D-colour corners plus parity. Further out, the reads give you floors to cut branches with, not the turn. Searching is the method there, and rodneykinney's verdict on the one-axis maze fits the 3D one too: "Still too complicated to keep in your head, IMO" ([[T3223]]).

{{ fig('flow', 'Reading the corners, in order.') }}

## 8. Quarter turns in 3D

### 8.1 The count, and the subset number inside it

The fewest quarter turns into HTR with half turns free goes from 0 to 8 (table in section 3, Jules Porteners' numbers). For a DR it's the number in the subset name.

beef beans' count ([[T2644]]) is that number for the *placement*: forget the twists and read the subset. It doesn't depend on the axis you'd twist to, which checks out for all 5,040 placements and all three axes, and it has the distribution FakeMMAP posted ([[T2870]]):

{{ t_subset_hist() }}

You don't have to twist anything in your head to read it. It's hyperparity with the stickers left where they are: the shape of the out corners (section 4.1), the picture of the D-colour corners (section 5.3) and parity. Those are rodneykinney's FB label, UD label and parity, and the number is the one in the maze, with the maze's own sub-cases where two states share a cell.

### 8.2 What the twist costs

zakimoshi's catch was that "orienting corners requires you to change the qt" ([[T2685]]). Here's by how much. True count minus the subset number of the placement:

{{ t_surcharge() }}

It's always even, since parity is the same for both. So the subset number is the true count for {= share(R['perm']['surcharge'][0]) =} of all states and 2 short for {= share(R['perm']['surcharge'][2]) =}.

By how many corners are twisted:

{{ t_surcharge_tw() }}

### 8.3 Out corners: the same maze as in DR

{{ fig('shape', 'The shapes of the out corners: the FB orientation of Hyper-Parity, with turns on all three axes.') }}

*Hyper-Parity* says of U turns in a DR: "It is possible to remain in 4a or 2c, but not 0c or 4b." It's the same with all six quarter turns. With DBL held, 6 out corners is a shape of its own; it's 2c seen from the other side, and the subset names fold it in.

{{ t_shape() }}

### 8.4 Everything within 2 quarter turns

Up to half turns and the symmetries that keep DBL, here's every kind of type pattern that can be 1 or 2 quarter turns from HTR. *Of 6 look-alikes* is how many of the six HTR cases with those types (section 5.2) are really that close.

{{ t_low() }}

{{ fig('funnel', 'The 3D funnel down to HTR. Compare the right end of the Corner Case Funnel in Hyper-Parity: 4a1 is the same, 4b2 and 4a2 are two of the five.') }}

So off the DR axis there are three new 2-qt kinds, and they're what two quarter turns on *different* axes leave behind:

```
R' F'          // two faces sharing an edge: 2 twisted where they overlap, 2 + 2 out
F U2 R         // the same with a half turn between: the out corners are now a 4a shape
U F2 U2 F'     // both turns on the same four corners: 4 twisted, nothing out
```

The last one looks awful and is 2 quarter turns (4 moves) in the one case in six where it's real. It's a special arrangement, though: the four twisted corners sit on one face after half turns, two twisted each way. Of the {= sum(R['twisted4_patterns_by_q']) =} type patterns with 4 twisted corners and nothing out, {= R['twisted4_patterns_by_q'][2] =} can be that close; {= R['twisted4_patterns_by_q'][4] + R['twisted4_patterns_by_q'][5] =} need 4 or 5 quarter turns at best.

### 8.5 Which quarter turn lowers the count

JTuu's question was whether you can know "whether each qt is +1 or -1 just by looking at the moves" ([[T2652]]). Looking at the corners, here's how often a rule picks a quarter turn that lowers the count. Half turns are free, so the choice is a setup plus a quarter turn, and states that differ by half turns at the end count as one *position* ({= n(X['cases_up_to_half_turns']) =} of them; the HTR one is left out of the table).

{= table(["Quarter turns to HTR", "Positions", "A random setup and turn", "Lowest types floor", "Types + parity", "Lowest subset number", "Types + parity and subset number"], [[("all but HTR" if r['q'] == 0 else r['q']), n(r['cases']), pc(r['random']), pc(r['types']), pc(r['types_par']), pc(r['subset']), pc(r['all'])] for r in X['qt_moves']]) =}

- Up to 4 quarter turns out, the types pick a lowering turn {= pc(min(r['types'] for r in X['qt_moves'] if 1 <= r['q'] <= 4), 0) =} to 100% of the time, and with parity and the subset number {= pc(min(r['all'] for r in X['qt_moves'] if 1 <= r['q'] <= 4), 0) =} to 100%.
- At 5, where most states are, the best column is the types at {= pc(next(r['types'] for r in X['qt_moves'] if r['q'] == 5), 0) =}, and at 6 and above nearly every quarter turn lowers the count anyway.
- The subset number alone is a bad guide. It only knows the placement, and the turn that helps the placement often wrecks the twist.

## 9. DR corners, seen from outside DR

### 9.1 No quarter turn is saved

For a DR state, allowing quarter turns on the other two axes never lowers the number of quarter turns into HTR. The subset number is the 3D count, for all {= n(R['dr']['states']) =} DR corner states. That's FakeMMAP's argument ([[T2693]]) read the other way: swap every off-axis quarter turn of a solution for [D2 L2 : U'] and friends and you have a DR solution with as many quarter turns. So a 4b5 is 5 quarter turns no matter what you allow.

### 9.2 Moves are saved

One row per subset. A *case* here is 24 states that differ by half turns done before the scramble, so they have the same solutions into HTR (210 cases in all). *DR turns* is U and the half turns; *all turns* adds R and F quarter turns.

{{ t_dr() }}

- {= R['dr']['save'][0] // 24 =} of the 210 cases are no shorter off-axis, {= R['dr']['save'][1] // 24 =} are 1 move shorter and {= R['dr']['save'][2] // 24 =} are 2 shorter.
- **Every 5-qt case is shorter off-axis**, and so is most of 4a4 and 4b4.
- Inside DR the longest way into HTR is {= len(R['dr']['hist_ddr']) - 1 =}, which is Yura Riabov's "11 to htr" ([[T4555]]). With all turns it's {= len(R['dr']['hist_d']) - 1 =}.

```
{= E['dr'][[r['subset'] for r in E['dr']].index('2c5')]['scramble'] =}     // a 2c5
{= E['dr'][[r['subset'] for r in E['dr']].index('2c5')]['dr_solution'] =}     // {= E['dr'][[r['subset'] for r in E['dr']].index('2c5')]['dr_only'] =} in DR turns
{= E['dr'][[r['subset'] for r in E['dr']].index('2c5')]['solution'] =}     // {= E['dr'][[r['subset'] for r in E['dr']].index('2c5')]['all'] =} with all turns
```

The shorter way costs quarter turns. Of the {= R['dr']['shorter_states'] // 24 =} cases that are shorter off-axis, the shortest solutions keep to the subset number in {= R['dr']['shorter_extra_q'][0] // 24 =}; in {= R['dr']['shorter_extra_q'][2] // 24 =} they use 2 more quarter turns and in {= R['dr']['shorter_extra_q'][4] // 24 =} they use 4 more. The {= dr_row('2c5')['all'] =}-mover above has {= quarters_of(dr_row('2c5')['solution']) =}, where the DR solution has {= quarters_of(dr_row('2c5')['dr_solution']) =}. So leaving DR trades half turns for quarter turns.

zakimoshi and torchlight had seen the same thing for full corner solutions of one case ("You can definitely under 12 if you leave DR", [[T4559]]; "there are some 12-move sols if you use the DR-breaking 2c4 triggers", [[T4564]]). It's corners only: off-axis turns break the DR on the edges, which is why nobody does this in an attempt without a reason.

The same with NISS. Joba's assumed bounds ([[T6639]]) are the *fewest* column of the DR side: 1, 2, 4, 6, 8 for 1 to 5 quarter turns, and 0c3 is the exception at 6, as Zagros said ("There's no U (U R2 U) with 0c3, it would have to be U (U R2 U2 F2 U)", [[T6636]]).

{{ t_dr_niss() }}

### 9.3 Going through DR costs

The usual route for corners is: orient them on an axis, then the subsets. Take the *optimal* orientation on an axis, and after it the best DR-only finish. How much longer than the optimal is that?

{{ t_staged() }}

On a fixed axis it's {= f2(R['staged']['mean_fixed'] - R['mean_d']) =} moves longer on average, on the best of the three {= f2(R['staged']['mean_best'] - R['mean_d']) =}. Picking the axis with the shortest CO is no better than a fixed one ({= f2(R['staged']['mean_shortest_co'] - R['mean_d']) =}): the short CO isn't the one that leaves a good subset. Jay asked for move counts to HTR from two axes ([[T6170]]); this is the corner part of that.

### 9.4 CO on one axis

mrauo asked for the CO movecount distribution ([[T3196]]). With R, U, F and DBL held there are 729 twist cases per axis:

{{ t_co_hist() }}

The mean is {= f2(R['co']['mean']) =} on one axis and {= f2(R['co']['mean_best3']) =} on the best of three. By how many corners are misoriented for the axis (each cell is the share of that row):

{{ t_co() }}

Jay's version of the question was for the DR move set R L U D F2 B2 ([[T3203]]), which this isn't: here F quarter turns are allowed. FakeMMAP gave the best case per number of misoriented corners for that move set ([[T3215]]).

## 10. The mazes in one place

- **Types** (section 4.2): six types, nine lines. The rule for a quarter turn on any axis.
- **Out corners** (section 8.3): 0c, 4a, 4b, 2c and 6c, at {= ', '.join(str(F['shape'][k]['qt']) for k in ('0c', '4a', '4b', '2c')) =} and {= F['shape']['6c']['qt'] =} quarter turns. rodneykinney's FB maze, unchanged.
- **D-colour corners** (section 5.3): 4a, 4b, 4c and 4d, at {= ', '.join(str(F['colour'][k]['floor']) for k in ('4a', '4b', '4c (3-1)')) =} and {= F['colour']['4d']['floor'] =}. rodneykinney's UD maze, unchanged.
- **The funnel** (section 8.4): the five 2-qt kinds and the 4a face.
- **The flow chart** (section 7).

Why there's no single 3D maze like the Hyper-Parity Maze: that one has 34 states because a DR corner has two types. With six types there are {= n(R['patterns']) =} type patterns, {= n(R['classes']) =} up to half turns, each shared by six HTR cases. The three small mazes multiply out to that. The good news is that they're independent reads: types by the stickers' axes, the D-colour corners by one colour, parity by tracing.

## 11. The claims, checked

Everything from the server that this search can check. *Confirmed* means exactly, for every state. Corrections are on the errata page.

| Claim | Who and where | What the search says |
|---|---|---|
| 2x2x2 by quarter turns: 24, 432, 6768, 86184, 780048, 1708416, 1049856, 42048, 384 states at 0 to 8; "sometimes 8 qt is required" | Jules Porteners, [[T6774]] | Confirmed, every number. |
| Quarter turns over all 7! corner cases: 24, 144, 720, 1416, 1776, 960 ("Can anyone check these stats") | FakeMMAP, [[T2870]] | Confirmed. |
| "0c0:0c3:0c4:4a1:4a2:4a3:4a4:4b2:4b3:4b4:4b5:2c3:2c4:2c5=1:3:2:6:6:12:12:24:12:12:24:32:48:16" | Shota, [[D7231]] | Confirmed: the cases column of 9.2. |
| The quarter-turn count of the placement is the same on every axis | beef beans, [[T2644]]; proof by FakeMMAP, [[T2693]] | Confirmed for all 5,040 placements and three axes. |
| "R and [D2 L2 : U'] permute corners in the same way" | torchlight, [[T2657]] | Confirmed, and the same for L and [U2 L2 : U']. |
| "a way to see that twisting all the corners onto another axis doesn't change the subset: R2 U D L2 F B" | trangium, [[T11371]] | Confirmed: it twists every corner and leaves the placement in HTR. |
| Six triple DRs up to half turns: "3 options for corners (3-cycle, inverse, solved) and 2 options for parity" | trig0n and Tom Nelson, [[T1934]], [[T1946]] | Confirmed: {= R['allgood']['n'] =} = 6 × {= R['allgood']['htr'] =}. |
| With DBL fixed the DR corners are 7!, HTR is 4!, and triple DR has index 6 over HTR | FakeMMAP, [[T7003]] | Confirmed. |
| HTR when the two tetrads' placements agree up to the Klein 4-group; a 3-cycle apart is 0c4; anything else 0c3 | torchlight, [[T5519]], [[T5520]] | Confirmed on all 144: {= X['klein']['(1, 1, 1, 1) q0'] + X['klein']['(2, 2) q0'] =} agree, {= X['klein']['(3, 1) q4'] =} are a 3-cycle apart (4 qt), {= X['klein']['(2, 1, 1) q3'] + X['klein']['(4,) q3'] =} a swap or a 4-cycle (3 qt). |
| "Lemma 1: If triple DR and OBL are solved, and there is even parity, then the state is in true HTR." The even ones are U2, R2 F2 R2, R2 F2 R2 U2 and solved | FakeMMAP, [[T9509]] | Confirmed: exactly those {= X['lemma1']['states'] =} states, {= X['lemma1']['without_parity'] =} without the parity condition. Section 5.3 is the version for all six pictures. |
| Bad corners are the "ones with exactly 1 oriented sticker" | zakimoshi, [[D13333]] | Confirmed and proved (section 4.1). |
| A corner in its own tetrad is oriented or not whatever the axis | Sebastiano Tronto's H48 doc, quoted by Arch, [[T8011]] | Confirmed and proved (section 4.1). |
| Distance to triple DR "is a lower bound to distance to HTR" | Louis, [[T6177]] | Yes, and now measured: {= f2(floor_by_key('types')['mean']) =} against {= f2(R['mean_d']) =}, exact on {= pc(floor_by_key('types')['exact']) =} (section 6.2). |
| You can determine the distance "only to fake htr" from the orientations | Zagros, [[T6178]] | Confirmed and made exact: 1 in 6 (section 5.2). |
| "orienting corners requires you to change the qt" | zakimoshi, [[T2685]] | Measured (section 8.2): the twist costs nothing for {= share(R['perm']['surcharge'][0]) =} of states and 2, 4, 6 or 8 quarter turns for the rest. |
| With NISS, at least "2/1/2/4/6/8 moves for 0/1/2/3/4/5 qt cases for now, with the possible exception of 0c3" | Joba, [[T6639]] | For corners, confirmed for 1 to 5 qt, and 0c3 is at 6 (section 9.2). I read the 2 for a 0-qt case as being about edges; corners in 0c0 need 0. |
| "11 to htr" for the longest DR corner case | Yura Riabov, [[T4555]] | Confirmed, also on all eight corners with U, D and the six half turns. |
| An 11-move solution of wen's case off-axis: D2 F2 U' F' D F' R2 B U' B' D' | torchlight, [[T4565]] | Confirmed: it solves that case. |
| Six <R,U,F> paths to HTR for R2 U R2 U' R2 U F2 U | rodneykinney, [[T2826]] | All six reach HTR with 4 quarter turns, and the case is 4 qt. I didn't recount that there are no others. |
| "You can probably map the corner-position permutation (4c2c2c, 3c5c, 2c5c, etc.) directly to a quarter-turn count." | rodneykinney, [[T2680]] | Only partly: the cycles fix the parity and little else. A lone 3-cycle is always 4 qt. Table below. |
| "4a - 1/2 1q, 1/2 2q" | Lewis Isom, [[D7229]] | True on Radek B's table ([[D7223]]), which splits only the 2-qt cases with 4 bad corners by shape (6 cases each). With the sheet's letters 4a1 : 4a2 : 4a3 : 4a4 is 6 : 6 : 12 : 12. |
| "4e4c adds/subtracts 1 quarter turn", "4e2c is +- 2 qt", "2e3c is +- 3 qt" | beef beans, [[T2644]] | Depends on the reading. As the quarter turns in the trigger, each one adding or taking 1: yes, and that's how zakimoshi read it ("3 away then one closer or 2 away", [[T2649]]). As the net change of the subset number: R U2 R' leaves it alone for {= pc(X['trigger_change_dr']["R U2 R'"]['0'] / sum(X['trigger_change_dr']["R U2 R'"].values()), 0) =} of the DRs it makes and moves it by 2 for the rest, and R U R' moves it by 1 for {= pc((X['trigger_change_dr']["R U R'"]['1'] + X['trigger_change_dr']["R U R'"]['-1']) / sum(X['trigger_change_dr']["R U R'"].values())) =} and by 3 for the rest. |
| The maze labels: UD 4a / 4b / 4c / 4d at 0 / 1 / 2 / 1 quarter turns, FB 0c / 4a / 4b / 2c at 0 / 1 / 2 / 3 | rodneykinney, *Hyper-Parity* | Confirmed, and unchanged with turns on all three axes (5.3, 8.3). |

rodneykinney's cycle-type idea, for the 5,040 placements with DBL in place. One row per cycle type, and how many placements of it have each subset number:

{{ t_cycle() }}

## 12. What this does not cover

- **Edges.** This is corners only. A floor here is a floor for the cube, but a turn that's closer for the corners can be terrible for the edges. rodneykinney on the CO maze: "it only applies to corners, and the edges are too important to ignore" ([[T3225]]).
- **Centres.** DBL is held, so a state is a corner state up to turning the cube (section 3).
- **A full recognition system.** Types + D-colour corners + parity settle the distance, but that's {= n(R['fix_types_col_par_d']['classes']) =} different things to see. I haven't found a way to read the distance off them by hand beyond 4 moves, and section 7 says how much room is left with less.
- **rodneykinney's CO maze, node by node.** Section 9.4 has the one-axis numbers for this move set, not a check of the gist's 13 nodes.
- **Whether the six paths are all of them** (section 11).

## Appendix: how it was computed, and what is proved in Lean

**The model.** A corner place is a point (±1, ±1, ±1), a face turn is a rotation of space, and the twist a turn applies is worked out from where the U/D sticker goes. Nothing is typed in as a table. A second model that tracks all 24 stickers one by one agrees with it on random sequences, and the type of a corner is checked against the stickers themselves.

**The tables.** A breadth-first search outward from each target gives the distance of every state to it: HTR, all good, even all good, all good with a 4a picture, corners oriented on an axis, corners in their tetrads. Quarter turns use the same search with half turns at cost 0. NISS distances take the smaller of normal and inverse and then relax over moves on the normal side.

**Lean.** {{ lean_text() }}

**Sizes.** {= n(N) =} states, {= n(R['patterns']) =} type patterns, {= n(R['classes']) =} up to half turns, {= n(R['cases']) =} cases of 24.
