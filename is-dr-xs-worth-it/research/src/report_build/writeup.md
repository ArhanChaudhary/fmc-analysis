# Is DR-xs worth it?

What leaving slices unsolved at DR costs you, how often you get the chance, and what it buys on real scrambles. Whatever can be counted exactly, I counted exactly: all 768 kinds of DR-xs state and all 2,217,093,120 cosets of the DR group. The rest is sampled or run on real scrambles. Each row is one thing measured and the sample behind it:

| What was measured | Sample |
|---|---|
| Finishes of DR-1s | {= N1() =} random states |
| Finishes of DR-2s 8fe | {= N8() =} random states |
| The shortest DR-xs of a scramble | {= NEARN() =} random scrambles |
| Every DR-1s and DR-2s 8fe, found and finished | 500 real scrambles |

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs are listed with links at the end.

**This builds on** work that is already on the server:

- **tseitsei89's [DR-Xs tutorial](https://docs.google.com/document/d/1_uLVLB5xqDm40NugXE5rjc8LgEtuHQCLz0odKY6mboE)** (with Jay, Rodney, trangium, count quackula, KrzychXyz and others behind it): the method.
- **trangium's numbers in the [tutorial](https://docs.google.com/document/d/1_uLVLB5xqDm40NugXE5rjc8LgEtuHQCLz0odKY6mboE)**: on optimal a DR-1s finishes about 2.2 to 2.4 moves longer than a DR of the same subset (1.8 for 2c4), and a DR-2s 8fe about 1 move longer. tseitsei89's takeaway: "8 move DR-1s is on average better than an 11 move DR but worse than 10 move DR". Those hold up.
- **trangium's [dr-fe examples](https://docs.google.com/document/d/11Xu6BpEBLu-v8hVbFzneSqeMjHb83q_zurWb_V0DXDY)**: the rule for the number of slices.
- **The first study of this site, [Judging a DR by hand](../judging-a-dr/)**: the exact optimal finish of every DR state, which every finish here uses.

**What this adds**, all things people kept asking for:

- **Odds, not just averages**: the chance of a finish in N from a DR-1s or a DR-2s 8fe, by subset, next to the same for a DR.
- **The move counts** from DR-3s to DR-2s to DR-1s to DR, for every layout of flipped edges.
- **How often you get one**: the chance of a slice-EO skip, and how far a DR-1s is from one.
- **Real scrambles**: every DR-1s and DR-2s 8fe on 500 scrambles, finished, against every normal DR on the same scrambles.
- **The claims**: every concrete thing people said about DR-xs, checked.

**Terms**, as the tutorial uses them. A *slice EO* (sEO) is the four edges of one slice all oriented, or all misoriented, for one axis. A *DR-xs* is a cube that looks like a DR if you ignore the centers and let some of the eight non-slice edges be flipped. It's a *DR-1s*, *DR-2s* or *DR-3s* by the number of slice moves it takes to fix centers and flipped edges. *DR-2s 8fe* is the DR-2s with all eight edges flipped and the centers off, which is how it comes up in the tutorial (eight flipped edges with the centers right is a different, worse DR-2s). Turns are HTM, and a slice move counts as the two outer turns it's written with (`R L'`).

**How to read it.**

- **Start with [section 1](#1-the-short-version)**, the short version: what's new, what it confirms or corrects, and the verdict, one line each.
- **The [worked examples](examples.html)** go with it: the tutorial's example with the numbers, then 100 scrambles with their slice-EO skips and the DR-xs routes on them, answers folded away. **The [errata](errata.html)** list what the numbers show is wrong in the docs involved and in things said on the server, each with an example.
- **The appendices are reference**: every DR-1s layout with a shortest fix and a scramble, what each EO pattern leads to, and how it was computed and checked.
- **What you can use in an attempt, and what's the answer key.** These are **computer only**, and each place says so: they say what's there, not what you find in an hour.
  - every finish here is the best one of the method's form, with the optimal DR finish looked up in a table of every DR state;
  - the shortest DR-xs of a scramble and the distances from a skip are exact searches;
  - section 7 finishes tens of thousands of DR-xs.

  What carries over to an attempt are the rules they give, all things you can see at the table: a DR-1s in $N$ is worth about a DR in $N + {= EXCH() =}$, the order to check things in (7.2), which skips can lead to a DR-1s (6.2) and which DR-1s are the good ones (5.4).

---

{{CONTENTS}}

---

## 1. The short version

First what nobody had before, each line with the sample and the move rule behind it; then what the numbers confirm or correct; then the verdict.

- **A DR-1s of 7 is worth about a normal DR of 9, and a DR-1s of 8 about a normal DR of 10.** On 500 real scrambles I counted how often each one gets the best solution any normal DR of 12 or less gives on its scramble (7.2). Each row is one kind of thing to finish; the number is how many of them you finish, on average, for one to give the scramble's best:

  | What you finish | One in this many gets the scramble's best |
  |---|---:|
  | a DR-1s of 7 | {= YIN('1s7') =} |
  | a normal DR of 9 or less | {= YIN('dr9') =} |
  | a DR-1s of 8 | {= YIN('1s8') =} |
  | a 10-move DR | {= YIN('dr10') =} |
  | an 11-move DR | {= YIN('dr11') =} |
  | a DR-2s 8fe of 9 | {= YIN('8fe9') =} |
  | a DR-1s of 6 or less | {= YIN('1s6') =} |

  That's the "how likely various things are to give you, say, sub-11 dr or sub-8 dr-1s" trangium wanted ([[T11296]]), minus the time per check. The finishes behind these odds are the best of the method's form, **computer only**; the ranking is what you use in an attempt.
- **Slice EOs against 5-move EOs, the question left open.** Same scrambles, starting from the EOs of 4 or less and their DRs of 10 or less. Each row adds one set of things to finish on top of those, and the number is how much shorter that makes the average best solution (7.4):

  | Added on top | Average best solution shorter by, moves |
  |---|---:|
  | every DR-1s of 8 or less from a slice EO, no normal EO added | {= EOD('eo10', 0, 2) =} |
  | only the ones of 7 or less | {= EOD('eo10', 0, 1) =} |
  | every 5-move EO (about {= f'{REAL["eo10"]["policies"][4]["eos"] - REAL["eo10"]["policies"][0]["eos"]:,.0f}' =} more EOs) | {= EOD('eo10', 0, 4) =} |
  | both together | {= EOD('eo10', 0, 5) =} |

  The 5-movers give more and do better per thing finished ({= f'{REAL["eo10"]["policies"][4]["n"] - REAL["eo10"]["policies"][0]["n"]:,.0f}' =} more DRs against {= f'{REAL["eo10"]["policies"][2]["n"] - REAL["eo10"]["policies"][0]["n"]:,.0f}' =} more DR-1s); the slice EOs take far less looking. Both sides are **computer only** (every DR-xs and every 5-move EO, each finished as well as possible). What carries over is the order: EOs of 4 or less, then the skips, then 5-movers.
- **A slice-EO skip is there on {= SKIP4('normal') =} of scrambles on normal, {= SKIP4('both') =} counting inverse.** That's exact, over all 70,963,200 arrangements of edge kinds and orientations, and it answers wen's question, where tseitsei89 had said ([[D19421]]): "I have no idea. But it seems to happen on most scrambles I would say." The skips clump, though: {= SKIP('both', 'avg') =} per scramble on average over both sides, yet {= SKIP('both', 0) =} of scrambles have none (6.1). ✓ Lean
- **Getting to a DR-2s 8fe is getting to a DR with the pieces renamed.** An 8fe is placed like a DR on one pair of faces in the colours of another pair: move every piece a quarter turn around the third axis, leave the centers, flip every edge, and it's a real DR. So (6.3):
  - from a full EO, with moves that keep it, the distance to the 8fe has exactly the distribution of the distance to the DR over all {= f"{sum(EO8['8fe']):,}" =} positions, {= E8AVG() =} on average (✓ Lean, position by position);
  - with any moves each 8fe is as far as a DR. A scramble has twelve 8fe targets against six DRs, which is why its shortest 8fe comes {= f2(float(NEARAVG('dr')) - float(NEARAVG('2s8fe'))) =} of a move before its shortest DR;
  - only the finish differs, +{= D8() =}.

  So a skip isn't how you get an 8fe. An oriented one leads to it only when the whole axis is oriented ({= SHR('eo-fb_2s8fe | A oriented') =} of them, and that's just a normal EO). A misoriented one on an axis with 8 bad edges is the one separate way in, {= SHM('eo-fb_2s8fe | A misoriented') =} moves on average.
- **The whole trade in two numbers.** The shortest of each over {= NEARN() =} random scrambles (any moves, linear, three colours, normal and inverse; 6.4). Each row is a target; the number is the average length of the shortest one on a scramble:

  | Shortest on the scramble | Average length, moves |
  |---|---:|
  | a real DR | {= NEARAVG('dr') =} |
  | a DR-1s | {= NEARAVG('1s') =} |
  | a DR-2s 8fe | {= NEARAVG('2s8fe') =} |
  | any DR-xs | {= NEARAVG('xs') =} |

  So the shortest DR-1s comes {= f1(float(NEARAVG('dr')) - float(NEARAVG('1s'))) =} moves before the shortest real DR, and it costs {= D1() =} in the finish. On average that's close to even, so it pays when you find the short ones. These are searches over every route, **computer only**, the answer key.
- **A DR-1s costs {= D1() =} more moves in the finish than a DR, and here are the odds.** Over {= N1() =} uniformly random ones, each finished as well as the method can (setup from either end, slice, optimal DR finish). The first row is the average finish, the others the share that finish in that many moves or fewer:

  | Finish | From a DR-1s | From a DR |
  |---|---:|---:|
  | average finish, moves | {= A1() =} | {= AD() =} |
  | in 14 or less | {= P1(14) =} | {= PD(14) =} |
  | in 15 or less | {= P1(15) =} | {= PD(15) =} |

  By subset the penalty is +{= D1('2c5') =} to +{= D1('4a1') =}, a bit more on the low-qt subsets. At equal odds a DR-1s in $N$ is a DR in about $N + {= EXCH() =}$. A DR-2s 8fe ({= N8() =} random states) costs {= D8() =}, from +{= D8('4a1') =} (4a1) to +{= D8('4c4') =} (4c4), going up with the qt count (5.2, 5.3). These finishes use the optimal DR finish from a table, **computer only**. A finish you find by hand is longer, so take the $N + {= EXCH() =}$ rule from it, not the lengths themselves.
- **The one good kind of DR-1s** is the one a single slice turn fixes, seen from one side of the scramble or the other ({= BETTER(2, 'share') =} of them): it finishes in {= BETTER(2) =} on average, {= BETTER(2, 'diff') =} over a DR. Past that the layout doesn't matter much (5.4). Average finish by how far the DR-1s is from a real DR:

  | Fewest turns to a real DR, from the better side | 4 | 5 | 6 |
  |---|---:|---:|---:|
  | average finish, moves | {= BETTER(4) =} | {= BETTER(5) =} | {= BETTER(6) =} |

  And by how the four flipped edges split between the two slices they belong to:

  | Split of the flipped edges | 3-1 | 2-2 | 4-0 |
  |---|---:|---:|---:|
  | average finish, moves | {= SPLIT('3-1') =} | {= SPLIT('2-2') =} | {= SPLIT('4-0') =} |

  The split is the same layout seen from the other side. The 4-0 is only good when its slice is the one that fixes; four in the other slice finish at +{= OTHER4('diff') =}, no better than an ordinary DR-1s.
- **Setting up only on the side where you found the DR-1s loses {= f2(float(A1(col='finish_setup4')) - float(A1())) =} moves.** With the setup at most 4 moves on that side and any DR finish after it, the average is {= A1(col='finish_setup4') =} and only {= OWN4_SAME() =} of states keep their best finish, even though the best solution has its slice within 4 moves of one end for at least {= SETUP_LE(4) =}. Try the setup from both sides before you judge a DR-1s (5.5). This one is for the attempt.
- **From an oriented skip on an axis that isn't the slice's own, a DR-1s is {= SHM('eo-fb_1s | A oriented') =} moves away on average** without breaking that axis's EO (exact, over every coset with such a skip). The share of these skips with a DR-1s that close:

  | Moves to the nearest DR-1s | 6 or less | 7 or less | 8 or less |
  |---|---:|---:|---:|
  | share of skips | {= SH('eo-fb_1s | A oriented', 6) =} | {= SH('eo-fb_1s | A oriented', 7) =} | {= SH('eo-fb_1s | A oriented', 8) =} |

  From a full EO the nearest real DR on one axis is {= SHM('eo-fb_dr | A oriented') =} under the same rule, so in route length a skip like this is an EO that cost nothing. The distances are the nearest DR-1s over every route, **computer only**. The hand version is tseitsei89's 8, occasionally 7 ([[T10809]]): "I can usually find some DR-fe in 8 moves. Occasionally 7." (6.2)
- **On 500 real scrambles, here's how many have a DR-1s** from a skip or a one-move slice EO by the plain tutorial route (7.1). I took every route, so it's a floor. Each row is a length; the number is the share of the 500 scrambles that have a DR-1s that short:

  | DR-1s from a skip or a one-move slice EO | Share of the 500 scrambles that have one |
  |---|---:|
  | of 8 or less | {= TH('a DR-1s of 8 or less from a skip or a one-move slice EO') =} |
  | of 7 or less | {= TH('a DR-1s of 7 or less from a skip or a one-move slice EO') =} |
  | of 6 or less | {= TH('a DR-1s of 6 or less from a skip or a one-move slice EO') =} |

  There are {= TH('a DR-1s of 8 or less from a skip or a one-move slice EO', 1) =} of them on average, nearly as many as the {= TH('a normal DR of 10 or less', 1) =} normal DRs of 10 or less. **Computer only**: every route taken, which nobody does in an hour. It says how much is there, not how much you find.
- **What finishing them does.** On top of every normal DR of 10 or less, every DR-1s of 8 or less takes the average result from {= POL(0) =} to {= POL(2) =}. Every 11-move DR instead takes it to {= POL(4) =}, with {= f1(float(POLN(4, 0).replace(',', '')) / float(POLN(2, 0).replace(',', ''))) =} times as many to finish (7.3). **Computer only**: every one of them finished as well as possible, the answer key. The part you can use by hand: the DR-1s of 7 or less come before the 10-move DRs, and the ones of 8 before the 11s.
- **DR-1s to DR takes 2 to 6 turns, usually 5 or 6.** Of the 70 ways four flipped edges can sit, how many need each number of turns:

  | Turns to a real DR | 2 | 3 | 4 | 5 | 6 |
  |---|---:|---:|---:|---:|---:|
  | layouts | {= FIX70(2) =} | {= FIX70(3) =} | {= FIX70(4) =} | {= FIX70(5) =} | {= FIX70(6) =} |

  That's {= FIXSHARE(1, (5, 6)) =} needing 5 or 6, {= FIXAVG(1) =} on average. All 70 with a shortest fix and a scramble each are in Appendix A, the list Radek B asked for. Right after a trigger, DR-2s to DR-1s is free for {= STEP('DR-2s -> DR-1s (or better)', 'after_quarter_better', 0) =} of the {= STEPS['DR-2s -> DR-1s (or better)']['kinds'] =} kinds of DR-2s and costs 3 for the rest (4.2, 4.3). ✓ Lean

**What it confirms or corrects**, each worked out in the section named:

- **trangium's averages hold.** trangium's nissy averages are 0.1 to 0.4 below my DR-1s numbers and a tenth or two below my 8fe ones on the subsets trangium measured; those are true optimals, which can leave the form. The tutorial's "8 move DR-1s is on average better than an 11 move DR but worse than 10 move DR" holds, in odds too. Rodney's "+3/+4 penalty for -1/-2 slice" is a bit hard on the DR-1s, and tseitsei89's "in reality around 3 moves worse" is what it turns into when you don't get the best finish (5.3).
- **DR-1s to DR.** Daichi's "6 moves max" is exact. Rodney's "basically flat", with 3 as the median, isn't: the distribution isn't flat and the typical fix isn't 3 (section 8). The EO Meta Comparison doc's "1 slice can be fixed in 3 moves" is {= f2(float(FIXAVG(1)) - 1 - 3) =} short on average with one slice turn cancelling, the way Rodney counts it, and {= f2(float(FIXAVG(1)) - 3) =} from the state alone (4.2). Simon's slice-DR table is four layouts off: {= SIMON() =}, not 1, 4, 9, 40, 16; the thirteen 4-turn layouts are at the end of Appendix A. ✓ Lean
- **Slice EOs.** For one given slice a slice EO is never more than 2 moves away, like FakeMMAP said, if all-misoriented counts; all-oriented only, it takes 3 moves {= SD('any axis, oriented only', 3) =} of the time. The 1 in 8 for a slice and an axis (tseitsei89, count quackula) is right (6.1). ✓ Lean
- **Which skips can give a DR-1s at all**, as long as you keep that axis's EO, is a clean rule (6.2):
  - oriented, on an axis that isn't the slice's own: always;
  - misoriented on such an axis: only if that axis has exactly 8 bad edges, trangium's "MUST have 8 bad", which is {= SHR('eo-fb_1s | A misoriented') =} of them (70 in 128, Rodney's "55%");
  - oriented on the slice's own axis: {= SHR('eo-ud_1s | B oriented') =} of the time;
  - misoriented on the slice's own axis: never.
- **The `U R L` ending** (a normal DR that's an 8fe two moves earlier) is worth about {= f1(2 - float(D8())) =} of a move with the best finish of the form; trangium's "1 to 1.3 moves better" and count quackula's "one move better" stand at about one move (5.6).
- **Rodney's extra-good DR-1s**, "just 1-2 moves worse than full DR", is +{= f2(float(SPLIT('4-0')) - float(AD())) =} on average (5.4). Five of Rodney's six patterns that guarantee one are right; the 12-bad line gives a DR-2s, not a DR-1s, with a scramble in section 8. count quackula's 12-bad notes already had it, and trangium's fix is right.
- **The groundwork checks out**:
  - trangium's rule for the number of slices holds for all 768 kinds (section 3);
  - trangium's dr-fe distribution comes out number for number from the search over all 2,217,093,120 cosets;
  - all 43 labelled examples from the server are what their labels say;
  - a DR-3s is a DR-2s for free right after the trigger for all {= NK(3) =} kinds, like the tutorial says (4.3);
  - the small exact tables are proved in Lean (Appendix C).

**The verdict:**

- **So is it worth it?** Each row is a DR-xs you might have, and where it goes in the order you finish things:

  | DR-xs you have | Where it goes |
  |---|---|
  | a DR-1s of 7 or less | yes, before your 10-move DRs. One is there on nearly half of scrambles |
  | a DR-1s of 8 | after the 10s and before the 11s, about {= YX('1s8', 'dr11') =} eleven-movers each |
  | a DR-2s 8fe of 9 | about as good as a 10-move DR |
  | a DR-1s of 6 or less | the only one that clearly beats a normal DR of 9 or less, and it's there on {= TH('a DR-1s of 6 or less from a skip or a one-move slice EO') =} of scrambles |

  Once the 11-movers are done, DR-xs adds {= POLD(4, 5) =} to the average. Mostly it gets you the same result from fewer and shorter things; on {= RL('win12') =} of scrambles it beats everything a normal DR of 12 or less gives.
- **Against 5-move EOs**: the slice-EO routes give more than half of what all the 5-move EOs give, for far fewer starts, and the two stack. tseitsei89's order, sub-5 EOs, then slice-EO skips, then 5-movers, fits that as long as the skips are quick to check; the tables don't measure time.

---

## 2. What was asked

The questions, in the askers' own words.

- Tom Nelson ([[T12405]]): "do we have movecount distributions for DR-1s > DR and DR-2s > DR? it feels like DR-xs is almost never good (apart from 2s8fe)". The answers were estimates. Daichi ([[T12406]], [[T12408]]): "dr-1s to dr is like 6 moves max?", "i don't think 7 optimal exists". Rodney ([[T12409]]): "I would guess the distribution is basically flat."
- Radek B ([[D18613]]): "is there a list of all cases for dr-1/2s -> dr?" tseitsei89: "I dont think so".
- wen ([[D19420]]): "what is the probability of at least one slice EO skip (fully oriented or vice versa) on a scramble?" tseitsei89 ([[D19421]]): "I have no idea. But it seems to happen on most scrambles I would say."
- JTuu ([[T10607]]): "what's the length distribution for the slice-eo condition? what about expected moves to dr from there?"
- tseitsei89 ([[T10813]]), on slice EO in 1 being better than EO in 5: "Do we have some proper stats for that?"
- trangium ([[T11296]]): "at some point I want to do an analysis of how likely various things are to give you, say, sub-11 dr or sub-8 dr-1s", then divide by the time it takes to check. tseitsei89 ([[T11299]]): "This I think would be EXTREMELY valuable!"
- tseitsei89 ([[D19521]]): "For sEO I currently believe skips are better than 5 move EOs but 1 movers might not be."

And the verdicts that never got settled:

- tseitsei89 ([[T10809]]): "You are better off with classical DR it seems."
- Rodney ([[T11020]]): "You're leaving money on the table if you don't check these, IMO."
- zakimoshi ([[T11306]]): "sEO isn't actually a very cost effective strategy time wise".
- tseitsei89 again, three months later ([[D17453]]): "most of the time it is not worth it to spend time on but it can occasionally save an otherwise doomed attempt".

---

## 3. What a DR-xs is, and how many slices it needs

Take a cube and one colour pair, say white/yellow. It is a DR-xs for that colour when:

- every corner has its white or yellow sticker on the same pair of opposite faces (any pair, not necessarily the white and yellow faces),
- the four edges with no white or yellow are in the slice between those two faces, and they all agree with each other.

The other eight edges can be flipped (white or yellow on the side), any even number of them, and centers don't matter. That's the group FakeMMAP wrote down ([[T10755]]): "<U, D, F2, B2, R2, L2, M, S>, aka DR-fe."

How many slices it needs comes down to two things: where the corners' faces are relative to the centers, and how many edges are flipped. trangium's examples doc has the rule, and enumerating everything confirms it line for line. Each row is one group of kinds with the same slice count, corner faces and slice-edge alignment; "Kinds of state" is how many of the 768 fall in it:

{{kinds}}

"Slice edges against the centers" is the tutorial's aligned and misaligned: do the four slice edges match the centers of their slice or not. Per colour there are 768 kinds of state, a kind being the faces, where the flipped edges are, and that one bit. Section 4 is an exact computation over these kinds, and section 6 uses them as targets.

Two sanity checks on the definition:

- The search for the nearest DR-xs on one colour and one pair of faces, over all cosets, gives this many states at 0 to 10 moves, which is the distribution trangium posted ([[T11332]]), number for number:

  1, 4, 50, 586, 6800, 72894, 659610, 3479477, 4193028, 247986, 84
- The server's own worked examples carry labels like "DR-2s", "4a2-1s", "2c3 -2s 8fe". I replayed 43 such labelled states from the docs and the two channels, and all 43 are what the label says by the table above.

---

## 4. The move counts: DR-3s, DR-2s, DR-1s, DR

Face turns with all cancelling done, using only moves that keep the DR-xs: any turn of the two faces the corners are oriented on, half turns of the other four, and slice turns written as two outer turns. So `R2` then `R L'` is `R' L'`, two turns.

### 4.1 To a real DR

Each row is a number of face turns; each column counts the kinds of DR-1s, DR-2s or DR-3s state whose shortest fix takes that many:

{{fix_turns}}

This is the count from the state alone, with nothing to cancel against. It's over kinds, and if you didn't steer the DR-xs, every kind with the same number of slices is equally likely.

### 4.2 DR-1s to DR: all 70 layouts

A DR-1s has exactly four flipped edges, and one slice turn fixes it once those four are in the slice that turn moves. Of the eight places they can be in, four are inside that slice and four outside it, so there are 70 layouts. Take the corners on F/B, where the slice that fixes is `R L`. Each row is how many of the four flipped edges already sit in that slice; the columns count its layouts by the turns their shortest fix takes:

{{dr1s_layouts}}

And the shortest example of each row:

{{dr1s_examples}}

- **Daichi is right** that 6 is the most and 7 does not exist ([[T12408]]). So is Rodney's bound ([[T12409]]): "Worst case requires 2qt, with at most one half-turn before/between each qt, so 4 and then the slice."
- **The distribution is not flat.** {= FIXSHARE(1, (5, 6)) =} of layouts need 5 or 6 turns, and the average is {= FIXAVG(1) =}. The EO Meta Comparison doc's working assumption, "1 slice can be fixed in 3 moves", is {= f2(float(FIXAVG(1)) - 1 - 3) =} short with one slice turn cancelling (Rodney's way of counting, [[T12410]]) and {= f2(float(FIXAVG(1)) - 3) =} from the state alone, and sqAree's "more than 5 moves most of the time" ([[T10672]]) is the accurate one. That count isn't the cost, though: the setup moves are also finish moves and the slice gets moved around in the finish, so the cost that matters is the finish (section 5).
- **3-1 isn't much worse than 2-2 here.** With three of the four already in the slice it's 5 or 6. With two it's anything from 3 to 6. With none it's 4:

  ```
  F B R L // none of the four in the slice
  ```
- All 70 layouts with a shortest fix each are in Appendix A, the list Radek B asked for.

**Simon's table.** Simon's slice-DR doc has the same count for its step 3, taking the better direction of the last trigger move: "Num Cases out of 70": 1, 4, 9, 40, 16 for 2 to 6 moves. With the same choice I get {= SIMON() =}. The ends agree, and so does Simon's "~4.9 moves on average", but thirteen layouts have a 4-turn fix, not nine. They're at the end of Appendix A, each with its fix.

### 4.3 The steps in between

Each row is a number of face turns; each column counts the kinds of state for that step whose shortest way through takes that many. Counted from scratch:

{{steps_scratch}}

And the extra turns when your last move was a quarter turn of a side face, on the better of the two side axes: a slice about that axis merges with it (`R` then `R' L` is just `L`):

{{steps_trigger}}

- **A DR-3s is always a DR-2s for free** right after the trigger, as the tutorial says: "you can always go to DR-2s in 0 moves by inserting a slice move that cancels with your last DR move".
- **DR-2s to DR-1s** is a slice with 0, 1 or 2 setup moves. Rodney's "DR-2s needs at most 2 moves to reach DR-1s" ([[T12409]]) is right if you don't count the slice itself. Right after the trigger, with its last move on the better of the two side axes, it is free for {= STEP('DR-2s -> DR-1s (or better)', 'after_quarter_better', 0) =} of the 383 kinds and costs 3 for the rest. On the other side axis it is free for {= STEP('DR-2s -> DR-1s (or better)', 'after_quarter_worse', 0) =}.

---

## 5. The finish: DR-1s and DR-2s 8fe against a DR

### 5.1 How it is measured

The tutorial finishes a DR-1s like this: set up the four flipped edges, do the slice, HTR from the other side, then leave slice while slicing the `R L'` back out. Every solution it can find has the form

> (moves that keep the DR-1s) (one slice turn) (a DR finish),

read from either side. For a given DR-1s I compute the shortest solution of that form exactly: every setup from both ends, and for the DR that comes out, its optimal finish from the first study's table of all 19,508,428,800 DR states. So "finish" below is the best the method can do, the same way "optimal finish" was for a DR: **computer only**, the answer key, not what you find in an hour (5.5 has what a hand finish loses). What you take into an attempt is the difference, the penalty against a DR. For a DR-2s 8fe the form is setup, both slices one after the other, DR finish.

The states are drawn uniformly: {= N1() =} DR-1s and {= N8() =} DR-2s 8fe. That's the right weighting for a DR-xs you reached without looking past the DR-xs itself: the part of the cube the route doesn't look at is still uniformly random. Section 7.5 checks it on real scrambles.

### 5.2 By subset

The subset of a DR-xs is its corner subset, as in "4a2-1s". trangium's columns are the nissy optimal averages from the tutorial. Each row is a corner subset; "DR-1s minus DR" is how many moves longer a DR-1s of that subset finishes than a DR of the same subset:

{{finish_subset}}

The same for the DR-2s 8fe, where "8fe minus DR" is against the DR column above:

{{finish_subset_8fe}}

- The penalty for a DR-1s is +{= D1() =} overall. It's larger on the low-qt subsets (+{= D1('4a1') =} for 4a1) than on the high ones (+{= D1('4b5') =} for 4b5), so a DR-1s flattens the difference between subsets a little.
- My DR-1s numbers are 0.1 to 0.4 above trangium's. trangium's are true optimals, which can leave the form, and trangium says of them that "lots of optimals are not findable" ([[T10808]]). The DR column agrees with trangium's to within 0.05.
- For DR-2s 8fe the penalty is +{= D8() =}, 0.1 to 0.2 above trangium's on each of the five subsets trangium measured. The 8fe sample is small for the rare subsets. The number of 8fe states sampled in each:

  | Corner subset | 0c0 | 0c4 | 0c3 |
  |---|---:|---:|---:|
  | 8fe states sampled | {= sum(xv.eight('0c0')) =} | {= sum(xv.eight('0c4')) =} | {= sum(xv.eight('0c3')) =} |

### 5.3 In odds

Each row is a finish length; each column is the share of states of that kind that finish in that many moves or fewer, and the last row is the average:

{{finish_odds}}

And adding the length of what you did before, the chance of a whole solution in $N$ moves or less. Each row is what you have and how long it took; each column is the share that ends in that many moves or fewer:

{{solution_odds}}

The same rows, longer solutions:

{{solution_odds_2}}

Read these two tables by finding rows that match. Each row below is one thing you can have, and the DRs it matches:

| What you have | Where it sits |
|---|---|
| a DR-1s in 7 | between a DR in 9 and a DR in 10, about midway |
| a DR-1s in 8 | between a DR in 10 and a DR in 11 |
| a DR-2s 8fe in 9 | a little behind a DR in 10 |

So:

- **DR-1s in $N$ is about a DR in $N + {= EXCH() =}$**, at equal odds for finishes of 13 to 16 ({= D1() =} on the average). Rodney's "+3/+4 penalty for -1/-2 slice" ([[T10919]]) is a bit hard on the DR-1s if you finish it well, and tseitsei89's later "in reality around 3 moves worse" ([[T11142]]) is what it turns into when you don't find the best finish (5.5).
- **DR-2s 8fe in $N$ is about a DR in $N + {= D8() =}$.**

### 5.4 Which DR-1s are the good ones

People said two things you can see on a DR-1s matter: how far it is from a DR, and how the four flipped edges split between the two slices they belong to (Rodney, [[T10832]]: "3-1 is bad because it requires 2 QT", "2-2 requires 1 QT"). Those are the same thing seen from the two sides of the scramble: the four flipped edges all belong to one slice exactly when, on the other side, they all sit in one slice. So one table covers both, the fewest turns to a real DR from whichever side is better. Each row is the DR-1s whose better side is that many turns from a real DR; "minus a DR's" is its average finish minus a random DR's:

{{better}}

- **The DR-1s to want is the one a single slice turn fixes, from one side or the other**: +{= BETTER(2, 'diff') =}, a little less than a DR-2s 8fe costs. It's {= BETTER(2, 'share') =} of them.
- **Past that, the layout doesn't matter much.** From 4 turns to 6 the average finish moves by {= f2(float(BETTER(6)) - float(BETTER(4))) =}. A DR-1s that's 6 from a real DR isn't 4 worse than one that's 2 away, because the setup moves are also finish moves.
- **"Extra-good" is two cases.** Rodney's extra-good DR-1s is four flipped edges all belonging to one slice ([[T11232]]), which Rodney put at "just 1-2 moves worse than full DR". When that slice is the one that fixes, it's the first row. When it's the other slice, the four sit together in the wrong slice and the finish is +{= OTHER4('diff') =}, no better than an ordinary DR-1s. Averaged over the two it's +{= f2(float(SPLIT('4-0')) - float(AD())) =}.

  ```
  F B R L // the fix when the four sit in the wrong slice
  ```

### 5.5 What a hand finish loses

The best solution has its slice within 4 moves of one end for at least {= SETUP_LE(4) =} of DR-1s states, which is trangium's "pretty high chance that the slice ends up within 4 moves of the start or the end" ([[T10921]]). But it isn't always the end you're on. If the setup has to be at most 4 moves and on the side where you found the DR-1s, with any DR finish after it, the average is {= A1(col='finish_setup4') =}, {= f2(float(A1(col='finish_setup4')) - float(A1())) =} more, and only {= OWN4_SAME() =} of states keep their best finish. So try the setup from both sides before you judge a DR-1s.

How often a person finds these finishes isn't something I can compute. trangium's findability tables in the tutorial are the data there is: for 4b2-1s, optimal findable 51% of the time and optimal + 1 another 32%.

### 5.6 DR-2s 8fe and the DR that ends in U R L

The tutorial's cheapest way to a DR-2s 8fe is a normal DR that ends in something like `U R L`: do `D` instead and you're at an 8fe two moves earlier. An 8fe in $N$ is worth a DR in $N + {= D8() =}$, so the DR in $N + 2$ that ends that way is worth a DR in about $N + {= f1(float(D8())) =}$. **The ending is worth about {= f1(2 - float(D8())) =} of a move** with the best finish of this form, and 0.9 to 1.15 with trangium's optimal averages. trangium put it at "1 to 1.3 moves better" ([[T11115]]) and count quackula at "one move better" ([[T11114]]): about one move stands.

By subset the 8fe penalty runs from +{= D8('4a1') =} (4a1) to +{= D8('4c4') =} (4c4). Unlike the DR-1s penalty it goes up with the qt count, so the `U R L` ending is worth about a move on the low-qt subsets and about {= f1(2 - float(D8('4c4'))) =} on 4c4.

---

## 6. Getting one

### 6.1 How often there is a slice-EO skip

There are 9 pairs of a slice and an axis, each in two flavours (all oriented, all misoriented), on normal and on inverse. Whether a scramble has a skip only depends on which kind of edge sits where and on the orientations: 70,963,200 equally likely configurations. Counting all of them: each row is a number of skips and each column the share of scrambles that have that many, for skips on normal or on both sides, any flavour or all-oriented only. The last row is an average count, not a share:

{{skip_odds}}

- **{= SKIP4('normal') =} of scrambles have at least one skip on normal, and {= SKIP4('both') =} have one on normal or inverse.** That's wen's question.
- Each single skip (one slice, one axis, one flavour, one side) has chance $1/16$, so $1/8$ for a slice and an axis with either flavour, like tseitsei89 and count quackula worked out ([[D19427]], [[D19423]]). The skips are far from independent: the average is {= SKIP('both', 'avg') =} per scramble over both sides, but {= SKIP('both', 0) =} of scrambles have none.
- The tutorial's "often 1-2 on a scramble" is right.

And for one given slice, the moves to a slice EO on some axis, over all 7,920 ways its four pieces can sit. Each row is the kind of slice EO you'll take; the columns are the share of those placements that need that many moves:

| Slice EO wanted | Already there (a skip) | 1 move | 2 moves | 3 moves | 4 moves |
|---|---:|---:|---:|---:|---:|
| any axis, oriented or misoriented | {= SD('any axis, oriented or misoriented', 0) =} | {= SD('any axis, oriented or misoriented', 1) =} | {= SD('any axis, oriented or misoriented', 2) =} | 0 | 0 |
| any axis, oriented only | {= SD('any axis, oriented only', 0) =} | {= SD('any axis, oriented only', 1) =} | {= SD('any axis, oriented only', 2) =} | {= SD('any axis, oriented only', 3) =} | 0 |
| one given axis, oriented or misoriented | {= SD('F/B only, oriented or misoriented', 0) =} | {= SD('F/B only, oriented or misoriented', 1) =} | {= SD('F/B only, oriented or misoriented', 2) =} | {= SD('F/B only, oriented or misoriented', 3) =} | 0 |
| one given axis, oriented only | {= SD('F/B only, oriented', 0) =} | {= SD('F/B only, oriented', 1) =} | {= SD('F/B only, oriented', 2) =} | {= SD('F/B only, oriented', 3) =} | {= SD('F/B only, oriented', 4) =} |

FakeMMAP's "never more than 2 moves away", "No matter which slice you pick" ([[T10773]], [[T10774]]) is exact, and so is the EO Meta Comparison doc's "partial EO in <=2 is guaranteed", as long as all-misoriented counts. All-oriented only, it takes 3 moves {= SD('any axis, oriented only', 3) =} of the time.

### 6.2 From a skip to a DR-1s

After the slice EO the tutorial looks for rzp and DR "like normal", ignoring flipped edges and centers. Normal means no quarter turns of the EO axis's two faces, which keeps every edge's orientation for that axis. Under exactly that rule, here's the nearest DR-1s from every state with a skip, by the kind of skip. The distances are exact searches, **computer only**; which skips can give a DR-1s at all is something you check at the table by counting bad edges. Each row is a kind of skip, with whether a DR-1s can be reached at all and how far it is on average:

{{skip_to_1s}}

And how often the nearest DR-1s is within that many moves, over all skips of the kind (the kind that never gets there is left out):

{{skip_to_1s_dist}}

- **Oriented, on an axis that is not the slice's own** (E-slice edges oriented on F/B, say): there's always a route. It's 7 or less for {= SH('eo-fb_1s | A oriented', 7) =} of skips and 8 or less for {= SH('eo-fb_1s | A oriented', 8) =}. For comparison, from a full EO the nearest real DR on one given axis is {= SHM('eo-fb_dr | A oriented') =} moves away on average under the same rule. So in route length a skip like this is an EO that cost nothing, and in finish it's a DR-1s. That's the sense of Rodney's "sliceEO in N is as good as regular EO in N+3" ([[T11020]]); with the finish penalty at {= EXCH() =} the 3 is a little generous to the normal EO, before you count how many of each you get to try.
- **Misoriented on such an axis**: without breaking that axis's EO a route exists only when exactly four of the other eight edges are bad, so that the axis has 8 bad edges in all. That's {= SHR('eo-fb_1s | A misoriented') =} of these skips (70 in 128). trangium ([[T11357]]): "you MUST have 8 bad on that axis for even a chance at dr-1s". Rodney's "55%" ([[T11566]]) is this number.
- **Oriented on the slice's own axis** (E-slice edges oriented on U/D): {= SHR('eo-ud_1s | B oriented') =}, when as many M-slice pieces as S-slice pieces are bad. The same states can reach a real DR on that colour without U or D quarter turns, {= SHM('eo-ud_dr | B oriented') =} moves away on average.
- **Misoriented on the slice's own axis**: never, with or without the extra quarter turns below. Daichi's "misoriented sEOs are just worse overall" ([[D19634]]) is right in both families.

Allowing quarter turns of the EO axis when they miss the slice pieces (the tutorial's tip 2) fully opens the two half-open kinds of skip, misoriented on another axis and oriented on the slice's own, but doesn't shorten much. Allowing any move shortens it by a quarter move. Each row is a kind of skip under one move rule, "strict" being the rule above:

{{skip_to_1s_rules}}

And how often it's within that many moves, same rows:

{{skip_to_1s_rules_dist}}

### 6.3 To a DR-2s 8fe: the same problem as a DR

**Getting to a DR-2s 8fe is getting to a DR with the pieces renamed.** An 8fe has its corners and slice edges placed like a DR on one pair of faces, in the colours of another pair. Move every piece a quarter turn around the third axis, leave the centers where they are, and flip every edge in its place: the 8fe turns into a real DR. Do that to any position, rename the faces of a move sequence by the same quarter turn, and reaching the 8fe turns into reaching the DR. Edges that are good for the third axis stay good, so an EO on that axis carries over too. Counted over every position with a full EO, with moves that keep it. Each row is a distance, and the two columns count the positions that far from the real DR and from the 8fe:

{{eo_to_8fe}}

- **From an EO, the 8fe is exactly as far as the DR**: the same distribution, {= E8AVG() =} on average. That's the tutorial's route 3: do the normal EO, then solve the wrong-coloured DR. Each of the EO's two DR axes has one, so an EO has four targets instead of two, and the two extra ones cost {= D8() =} more in the finish.
- **With any moves it is the same, target by target.** A scramble has twelve 8fe (two for each colour, on normal and on inverse) against six DRs, and each is as far away as a DR is. That's why the shortest 8fe of a scramble comes {= f2(float(NEARAVG('dr')) - float(NEARAVG('2s8fe'))) =} of a move before its shortest DR in 6.4: there are twice as many, and none of them is closer. (Checked on {= E8CHK() =} random positions: the distance to the 8fe is the distance of the renamed position to the DR every time.)
- **What doesn't carry over is the finish.** The renaming doesn't take the solved cube to the solved cube, and the two slice turns are there to make up the difference: +{= D8() =} (section 5).

**So a slice-EO skip isn't what gets you an 8fe.** By the kind of skip, keeping that axis's EO: whether there's a route to an 8fe, and how long it is on average:

{{skip_to_8fe}}

And how often it's within that many moves, over all skips of the kind:

{{skip_to_8fe_dist}}

- **An oriented skip** leads to an 8fe only when the rest of the axis is oriented as well ({= SHR('eo-fb_2s8fe | A oriented') =} of such skips, 1 in 128), and that's just a normal EO. The skip adds nothing.
- **A misoriented skip on an axis with 8 bad edges** (the four slice edges and four of the other eight, {= SHR('eo-fb_2s8fe | A misoriented') =} of misoriented skips) is the one separate way in. From there an 8fe is {= SHM('eo-fb_2s8fe | A misoriented') =} moves away on average, against {= E8AVG() =} from an EO, and you spend no moves on an EO first. It's 8 or less for {= SH('eo-fb_2s8fe | A misoriented', 8) =} of those skips.

### 6.4 What exists, with any moves

Any moves, linear on one side, over {= NEARN() =} random scrambles (three colours, normal and inverse). **Computer only**: the shortest of each over every route, the answer key for what exists. Each row is a target; the columns are the average length of the scramble's shortest one and the share of scrambles where it's that short:

| Shortest on the scramble | Average length, moves | In 6 moves or less | 7 or less | 8 or less | 9 or less |
|---|---:|---:|---:|---:|---:|
| a real DR | {= NEARAVG('dr') =} | {= NEAR('dr', 6) =} | {= NEAR('dr', 7) =} | {= NEAR('dr', 8) =} | {= NEAR('dr', 9) =} |
| a DR-2s 8fe | {= NEARAVG('2s8fe') =} | {= NEAR('2s8fe', 6) =} | {= NEAR('2s8fe', 7) =} | {= NEAR('2s8fe', 8) =} | {= NEAR('2s8fe', 9) =} |
| a DR-1s | {= NEARAVG('1s') =} | {= NEAR('1s', 6) =} | {= NEAR('1s', 7) =} | {= NEAR('1s', 8) =} | {= NEAR('1s', 9) =} |
| any DR-xs | {= NEARAVG('xs') =} | {= NEAR('xs', 6) =} | {= NEAR('xs', 7) =} | {= NEAR('xs', 8) =} | {= NEAR('xs', 9) =} |

- The first row is wen's other question ([[D20015]]), "Is the distribution for scrambled->DR movecount known?". The row is the best of six; per colour it's exactly this, over the 2,217,093,120 cosets (0 to 12 moves):

  1, 4, 50, 592, 7156, 87236, 1043817, 12070278, 124946368, 821605960, 1199128738, 58202444, 476
- The last row is trangium's "almost always a linear 7-mover on some axis and side, around half the time a 6-mover, and pretty much never a 5-mover" ([[T10696]]): {= NEAR('xs', 7) =}, {= NEAR('xs', 6) =}, and {= NEAR('xs', 5) =} for 5 or less.
- A DR-1s exists about {= f1(float(NEARAVG('dr')) - float(NEARAVG('1s'))) =} moves earlier than a real DR, and costs {= D1() =} in the finish. That's the whole trade in two numbers: on average it's close to even, so it pays when you find the short ones.

### 6.5 From an EO pattern to a kind

If the route keeps the EO of an axis, the EO pattern you start from decides what you can land on. Appendix B has the full table: for every pattern that is uniform by slice (each slice's four pieces all good or all bad) and each pair of faces for the corners, what the DR-xs is. Rodney's list of patterns that guarantee an extra-good case ([[T11232]]) and count quackula's two lists (the 12-bad notes and the guaranteed-fix cases) can be read straight off it. All of them check out except one line, the 12-bad one in Rodney's list (section 8).

---

## 7. On 500 real scrambles

{{REAL}}

---

## 8. The claims, checked

Everything said that a computer can settle, and what the numbers say. Wherever something is refuted or a case is claimed to exist, there's a scramble. Each row is one claim, who made it, and the verdict:

| Claim | Who | Verdict |
|---|---|---|
| DR-1s to DR is 6 moves at most, no 7 | Daichi, [[T12406]], [[T12408]] | **True.** Exactly 2 to 6 turns over the 70 layouts (4.2). A 6: `{= W6() =}` gives a DR-1s whose shortest fix is 6 turns. ✓ Lean |
| The DR-1s to DR distribution is "basically flat", 3 moves is the median | Rodney, [[T12409]], [[T12410]] | **No.** 1, 2, 9, 30, 28 of 70 for 2 to 6 turns. Rodney's 3 is one half turn, one quarter turn and the slice with one of its two turns cancelling; counted that way the median layout is 4, and 5 from scratch. ✓ Lean |
| "DR-2s needs at most 2 moves to reach DR-1s" | Rodney, [[T12409]] | **True** for the setup: 0, 1 or 2 moves, then the slice (4.3). ✓ Lean |
| From DR-3s you get DR-2s in 0 moves with a slice that cancels with the last DR move | tseitsei89's tutorial | **True** for all {= NK(3) =} kinds of DR-3s. ✓ Lean |
| The rule for the number of slices from centers and flipped edges | trangium's dr-fe examples doc, Rodney [[T10661]], the tutorial | **True**, all 768 kinds (section 3). ✓ Lean |
| "1 slice can be fixed in 3 moves, and 2 slices can be fixed in 5 moves" | EO Meta Comparison doc (an assumption, stated as one) | As move counts to a real DR, about a move short with one slice turn cancelling, as Rodney counts the 3 ({= f2(float(FIXAVG(1)) - 1) =} and {= f2(float(FIXAVG(2)) - 1) =} on average), and about 2 short from the state alone ({= FIXAVG(1) =} and {= FIXAVG(2) =}). As finish penalties, 3 is a little high for a DR-1s (+{= D1() =}) and 5 much too high for a DR-2s 8fe (+{= D8() =}). |
| "UD colors on the RL faces will result in 8 flipped edges, which can be fixed with U\* D\* R\* L\*, with a guaranteed -2 cancellation", "This effectively adds +2 to the moves to reach DR" | EO Meta Comparison doc, Off-Axis DR | **True** as moves to DR. Counted as finish length the 8-flipped case costs less: a DR-2s 8fe finishes {= D8() =} longer than a DR, so the off-axis table, which charges the full +2, undersells that case by about a move. |
| A DR-1s finish is about 2.2 to 2.4 longer than a DR's on optimal; a DR-2s 8fe about 1 | trangium, in the tutorial and [[T10847]], [[T11138]] | **Consistent.** trangium's are optimals. With the best finish of the method's form, on {= N1() =} and {= N8() =} states: +{= D1() =} and +{= D8() =}, 0.1 to 0.4 above trangium's by subset. |
| "8 move DR-1s is on average better than an 11 move DR but worse than 10 move DR" | the tutorial | **Holds** with these finishes: at +{= D1() =} an 8-move DR-1s is {= f2(float(D1()) - 2) =} behind a 10-move DR and {= f2(3 - float(D1())) =} ahead of an 11 (5.3). |
| 3-1 is bad, 2-2 is good, 4-0 is great | Rodney [[T10832]], tseitsei89 [[T10822]] | **Right order, small effect** except for one case: {= SPLIT('3-1') =}, {= SPLIT('2-2') =}, {= SPLIT('4-0') =} average finish, and the 4-0 is only good when the slice is the one that fixes (5.4). |
| An extra-good DR-1s is "just 1-2 moves worse than full DR" | Rodney, [[T11232]] | **On average**, +{= f2(float(SPLIT('4-0')) - float(AD())) =}: +{= BETTER(2, 'diff') =} when the four are in the slice that fixes, +{= OTHER4('diff') =} when they are in the other one. |
| Slice EO for a given slice "is never more than 2 moves away"; "partial EO in <=2 is guaranteed" | FakeMMAP, [[T10773]]; EO Meta Comparison doc | **True**, exactly, counting all-misoriented as a slice EO (6.1). ✓ Lean |
| A slice-EO skip for one slice and axis has chance 1 in 8 | tseitsei89, count quackula, [[D19427]] | **True.** And at least one on a scramble: {= SKIP4('normal') =} on normal, {= SKIP4('both') =} with inverse. ✓ Lean |
| A misoriented slice EO gives a DR-1s only on an axis with 8 bad edges | tseitsei89 [[T11009]], trangium [[T11357]] | **True** for routes that keep the axis's EO, and {= SHR('eo-fb_1s | A misoriented') =} of misoriented skips qualify (6.2). |
| "The chance of getting 4 flipped edges in general is 55%" | Rodney, [[T11566]] | **True**: 70 in 128. |
| The optimal linear dr-fe distribution 1, 4, 50, 586, … | trangium, [[T11332]] | **Reproduced exactly.** |
| "almost always a linear 7-mover on some axis and side, around half the time a 6-mover, and pretty much never a 5-mover" | trangium, [[T10696]] | **Right for 7 and 6**: {= NEAR('xs', 7) =} of scrambles have a 7, {= NEAR('xs', 6) =} a 6. A 5 or shorter is there on {= NEAR('xs', 5) =}, one scramble in {= f'{100 / float(NEAR("xs", 5).rstrip("%")):.0f}' =} (6.4). |
| Six edge-orientation patterns that guarantee an extra-good DR-xs | Rodney, [[T11232]] | **Five of six.** "All edges misoriented (12 bad) -> FB on UD will be extra-good -1s" is not a DR-1s: it is a DR-2s with four flipped edges of one slice. {= W12() =} trangium's fix ([[T11234]]), "FB-colored misoriented, others oriented", is right. count quackula's 12-bad notes already had it: "If the CO color is green/blue: This is a DR-2s 4fe." (the 12-bad example ✓ Lean) |
| The cases with a fix to DR guaranteed in net +4 or less | count quackula's guaranteed-fix doc and 12-bad notes | **All consistent** with Appendix B, case by case. |
| Step 3 of the slice-DR method: 1, 4, 9, 40, 16 cases of 70 at 2 to 6 moves | Simon's slice-DR doc | **Four cases off**: {= SIMON() =} (4.2, Appendix A). ✓ Lean |

---

## 9. What this does not cover

- **Findability.** "Finish" is the best solution of the method's form, exact per state. What a person finds in the time is trangium's and tseitsei89's ground, and their tables in the tutorial are the data.
- **Solutions outside the form.** True optimals from a DR-1s are 0.1 to 0.4 shorter on average (trangium's nissy numbers against mine). For a DR-2s 8fe the form has the two slices together; I didn't search solutions with moves between them.
- **DR-2s other than 8fe, and DR-3s.** Only their move counts to DR (section 4). trangium's nissy averages for them are +2.7 to +3.0 and +3.0 to +3.5.
- **NISS inside the route, and EO-changing moves.** A slice EO is taken on normal or on inverse, and the route to the DR-xs stays on that side and keeps that axis's EO. The finish uses both sides. So the counts of section 7 are a floor on what's there.
- **Normal DRs through an EO longer than 5 moves.** The normal-DR lists of section 7 come from cubelib-cli, which lists no EO longer than 5.
- **EO-breaking triggers and the EO-shifting ideas** from the EO-free trigger doc. The route rule here keeps the EO of one axis; 6.2 shows what dropping that rule could gain at most.
- **Time.** Section 7 counts what there is to find and to finish. How long a check takes is up to the people who do them; the times people have posted are in 7.6.

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
