# Errata derivations (report/BUGS.md, A1 and A2; the former A3)

Each correction re-derived from the person's exact words, with every term mapped to the model, and the evidence
behind each printed number. Lean = `lean/Insertions/Insertions/ErrataTheorems.lean` (theorem names below).
Written 2026-11-13; revised the same day after a second reading of the messages before and after each quote:
A1 and A2 reworded, A3 taken off the corrections page.

## A1. argonblue, N6507: "i think 3c1t > 2c2c > 5c. mostly because a twist gives you the most freedom to pick comms"

Context (N6502 to N6514): jisu101 asked "speaking about skeletons though", "if you can't find a 3c, what is
generally better", "2c2c, 3c1t, or 5c?". argonblue answered with the order above; jisu101 replied "True but so does
2c2c, you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions". argonblue
did not defend the order: N6510 "then again, you could end up with a massive cancellation for the first comm, and
mediocre for the second one", N6512 "you could iterate with suboptimal first comms, but that takes forever".

The same person elsewhere: it is a held belief (D19111 "very few skeletons with corners twisted in place are useful.
3c1t is one of the exceptions (2 comms, but the extra freedom allows you to cancel more moves)"; N5674 "comms that
pick up twisted corners can cancel more moves, because orientation doesn't matter when you pick them up (only when
you put them back)"), and argonblue finds the 2c2c's choices hard to search by hand (N5507 "there's just so many
choices for 2c2c insertions, and it's hard for me to check them all").

Terms:
- `>` is "is better than" (the question was "what is generally better"), so the claim orders the three leftovers
  3c1t first, 2c2c second, 5c last.
- "better" for a skeleton = shorter final solution from the same skeleton length. Model: mean moves added by the
  best insertion on random 20-move skeletons, each leftover type at the same length. "Better" may also mean easier to
  find; that is not measured, and the page says the order is by cost.
- "2c2c" covers both kinds (pure and twisted). Both beat the 3c1t; had only one of them, the fair verdict would have
  been "depends on which 2c2c".
- "freedom to pick comms" = how many first comms leave a 3-cycle at a spot (per spot: 5c 5, 3c1t 9, 2c2c 24). So the
  reason is right against a 5c and wrong against a 2c2c.

What the model says: 8-movers, 20 moves: twisted 2c2c 8.73, pure 2c2c 9.13, 3c1t 9.90, 5c 10.37 (sampled,
20,000 each). The 2c2c-before-3c1t order also holds at cap 10 (8.66 / 8.48 against 9.73) and cap 12 (8.30 / 7.87
against 9.44), at every skeleton length from 14 to 24, and with the hand search (best first comm, then the best
second: 9.03 / 9.24 against 9.97; section 8.4), which is the search N6510 is about. So the first two are swapped under
every alg list measured; 5c last agrees. The posted skeletons cannot rank the 4-corner types (3c1t 8.65 on 20,
2c2c 8.46 on 13).

Evidence: means are sampled (Rust, cross-checked per skeleton by an independent recount where noted in the Lean
README / app); the per-spot counts 9 and 24 are Lean (`FirstComms.lean`); the three typical skeletons (29, 29, 30)
replay and are exact optima over every pair of 8-movers (`A1_blocks_replay`, `A1_best_two`). The typical skeletons
illustrate, they do not prove the order (the page says so).

Quotes on the page: argonblue's and jisu101's messages whole. Jay's N4860 is quoted from "ime when i was doing
blocks" to its end ("other than 2c2c being easier practically with rNISS"): the second half is on the 2c2c's side
and must not be dropped.

## A2. notkevin, N4772: "(this is also why it's often recommended to check every other move when doing a lot of 2-insertion skeletons, bc if you're expecting at least a -3 somewhere, it has to cancel at least a full move, so checking every other still guarantees you'll find them)"

Context: N4770 (trangium: a big cancel can be found at several spots), N4772 (the claim, about "a lot of
2-insertion skeletons"), N4773 ("the worst insertions you can miss with this without the second comm nesting is
-4, where both comms only partially cancel on both sides").

Terms:
- "-3" = an insertion that cancels 3 moves, an 8-3 for an 8-mover.
- "checking every other" = trying insertions at every second spot (alkamaass N1142, N1143: plus the ends).
- "guarantees you'll find them" = every -3 or better that exists is found at a checked spot, possibly as the
  same result by a shifted alg (the argument: a full cancel lets the alg move one spot over).
- N4773 limits the misses to partial cancels on both sides; a -3 with a full cancel is inside the claim.
- alkamaass's N1144 ("R (R blah blah B' ) B'") is a partial cancel at each end, an 8-2: the kind N4772 leaves out
  and N4773 allows for. It is not the miss of the counterexample and does not go against notkevin.

Model: one comm per spot (each comm of a two-comm skeleton is such a search), 8-movers, odd spots plus both ends,
or even spots (which include both ends at even length). The 97% of the page is this model on 3c skeletons; notkevin
spoke of two-insertion skeletons, and the two comms together are not tested.

Counterexample (`A2_example`): 20-move 3c skeleton, best 8-mover insertion 25 (8-3), at spot 16 only, one alg only.
The odd spots plus 0 and 20 give at best 27 (8-1). The 8-3 cancels `F` against the `F'` before `B` (a full
cancel), so it is exactly the case the argument covers, and the shift fails: spot 14 gives at best 27
(`A2_pair_swapped`). With the pair written `B F'` the shifted alg fits between the two (spot 15) for the same 25.
At spot 15 as written the same comm with the setup move `B` (`B F D F' U F D' F' U' B'`) is a 10-5 for the same 25
(replayed on the sticker model at build time, `xenv.SKS`; not in Lean): the miss is among 8-movers.

What closes the gap: trying an opposite-face pair both ways round, which is footnote 26 of the tutorial's 2.4.1
("when in a skeleton there are two consecutive parallel layers moves try swapping them too see if this gives better
insertions"). With it the guarantee is exact.

The share depends on how often two neighbouring moves are an opposite-face pair. The study's skeletons write such a
pair in one fixed order (1 pair of neighbouring moves in 11); the posted skeletons have 1 in 14. A separate program
(`research/verify/every_other.py`, own alg list, skeletons and search; `out/verify/every_other.txt`): 97.1% with
the fixed order (20,000 skeletons, 340 misses in 11,906 walks), 93.8% with a pair written either way round (20,000,
785 in 12,698), 98.5% for the first comm of a 5c (10,000, 247 in 16,102); every miss next to a pair and found by
the same walk once a pair is written the other way round.

Note for the page: the earlier wording "the shifted alg lands two spots away" is not what happens; as written there
is no spot for it. Fixed to "the alg moved one move over would go between the two moves of the pair, swapped" (and the example now shows it).

## Former A3, off the corrections page. sequesteredcuber, N292: "sub-22 for 3C skeleton" / "sub-20 for every other skeleton"

Context: N253 Sam, two days before: "How long would it take me of practicing fmc to get sub 30 consistently?";
N257 sequesteredcuber: "... should be good enough to get avg sub-30 (or close to)". Then N288 Sam: "If I wanna be
sub 30 what should I be aiming for"; N289, N290 Aneurin: "Remember a optimal 3c skeleton's insertion is 6 moves on
average", "5c is 10-11 moves."; N292 the two aims; N297 "So skeleton plus first insertion is sub 22?"; N298
sequesteredcuber: "just the skeleton minus insertion"; N303 "you cant "aim" for less moves in insertions,
insertions is what determines the luck, sometimes you can cancel many moves, sometimes you cant".

Terms:
- sub-30 = final length 29 or less.
- "sub-22 for 3C skeleton" = a 3c skeleton of 21 moves or fewer; "sub-20 for every other skeleton" = any other
  leftover in 19 or fewer. Two aims for sub-30, with insertions left to luck (N303).

Why it is not a correction. The first version of the page read the advice as "the two targets are two moves apart"
and corrected that gap. The person stated no gap and no exchange rate. Tested as said, at the limits and with the
best 8-mover pair:

| Skeleton at the limit | Chance of sub-30 | Expected total |
|---|---:|---:|
| 3c in 21 | 99.6% | 26.9 |
| twisted 2c2c in 19 | 97% | 27.8 |
| pure 2c2c in 19 | 87% | 28.2 |
| 3tc in 19 | 76% | 28.6 |
| 3c1t in 19 | 63% | 29.0 |
| 5c in 19 | 48% | 29.4 |

Every expected total is under 30, which is the reading "avg sub-30" of N257. So the advice holds on average for
every type and is unevenly safe: the write-up says so in 7.3 and in the claims table ("Holds on average, unevenly
safe"), with Aneurin's 6 and 10-11 credited for the four-to-five-move gap. The exchange rates for a 20-move 3c are
4.8 (5c), 4.4 (3c1t), 4.0 (3tc), 3.5 (pure 2c2c), 3.0 (twisted 2c2c) and 2.0 (2tc); an earlier line of these notes
gave them as "4.0 to 4.8", which left out the 2c2c and the 2tc.

Evidence: chances and rates are sampled (20,000 skeletons per length, odd lengths sampled directly); the 19-move 5c
example, now only in 7.3 as example [g], replays and 30 is its exact optimum with two 8-movers (the theorem keeps
the name `A3_example`); that 30 is the most common outcome of a 19-move 5c is from the sample.
