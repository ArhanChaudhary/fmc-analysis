# Errata derivations (report/BUGS.md, A1 to A3)

Each correction re-derived from the person's exact words, with every term mapped to the model, and the evidence
behind each printed number. Lean = `lean/Insertions/Insertions/ErrataTheorems.lean` (theorem names below).
Written 2026-11-13.

## A1. argonblue, N6507: "i think 3c1t > 2c2c > 5c. mostly because a twist gives you the most freedom to pick comms"

Context (N6502 to N6514): jisu101 asked "speaking about skeletons though", "if you can't find a 3c, what is
generally better", "2c2c, 3c1t, or 5c?". argonblue answered with the order above; jisu101 replied "True but so does
2c2c, you can pick literally any comm with 3 of the 4 corners", "and you can do it in both directions".

Terms:
- `>` is "is better than" (the question was "what is generally better"), so the claim orders the three leftovers
  3c1t first, 2c2c second, 5c last.
- "better" for a skeleton = shorter final solution from the same skeleton length. Model: mean moves added by the
  best insertion on random 20-move skeletons, each leftover type at the same length.
- "2c2c" covers both kinds (pure and twisted); the claim fails if either kind beats the 3c1t.
- "freedom to pick comms" = how many first comms leave a 3-cycle at a spot (per spot: 3c1t 9, 2c2c 24).

What the model says: 8-movers, 20 moves: twisted 2c2c 8.73, pure 2c2c 9.13, 3c1t 9.90, 5c 10.37 (sampled,
20,000 each). The 2c2c-before-3c1t order also holds at cap 10 (8.66 / 8.48 against 9.73) and cap 12 (8.30 / 7.87
against 9.44), and with the hand search (best first comm and the ones a move worse, section 8.4). So the first two
are swapped under every alg list measured; 5c last agrees.

Evidence: means are sampled (Rust, cross-checked per skeleton by an independent recount where noted in the Lean
README / app); the per-spot counts 9 and 24 are Lean (`FirstComms.lean`); the three typical skeletons (29, 29, 30)
replay and are exact optima over every pair of 8-movers (`A1_blocks_replay`, `A1_best_two`). The typical skeletons
illustrate, they do not prove the order (the page says so).

## A2. notkevin, N4772: "if you're expecting at least a -3 somewhere, it has to cancel at least a full move, so checking every other still guarantees you'll find them"

Context: N4770 (trangium: a big cancel can be found at several spots), N4772 (the claim, about "a lot of
2-insertion skeletons"), N4773 ("the worst insertions you can miss with this without the second comm nesting is
-4, where both comms only partially cancel on both sides").

Terms:
- "-3" = an insertion that cancels 3 moves, an 8-3 for an 8-mover.
- "checking every other" = trying insertions at every second spot (alkamaass N1142, N1143: plus the ends).
- "guarantees you'll find them" = every -3 or better that exists is found at a checked spot, possibly as the
  same result by a shifted alg (the argument: a full cancel lets the alg move one spot over).
- N4773 limits the misses to partial cancels on both sides; a -3 with a full cancel is inside the claim.

Model: one comm per spot (each comm of a two-comm skeleton is such a search), 8-movers, odd spots plus both ends,
or even spots (which include both ends at even length).

Counterexample (`A2_example`): 20-move 3c skeleton, best 8-mover insertion 25 (8-3), at spot 16 only, one alg only.
The odd spots plus 0 and 20 give at best 27 (8-1). The 8-3 cancels `F` against the `F'` before `B` (a full
cancel), so it is exactly the case the argument covers, and the shift fails: spot 14 gives at best 27
(`A2_pair_swapped`). With the pair written `B F'` the shifted alg fits between the two (spot 15) for the same 25.

Note for the page: the earlier wording "the shifted alg lands two spots away" is not what happens; as written there
is no spot for it. Fixed to "the alg moved one move over would go between the two moves of the pair, swapped" (and the example now shows it).

## A3. sequesteredcuber, N292: "sub-22 for 3C skeleton" / "sub-20 for every other skeleton"

Context: N288 Sam: "If I wanna be sub 30 what should I be aiming for"; N297 "So skeleton plus first insertion is
sub 22?"; N298 sequesteredcuber: "just the skeleton minus insertion".

Terms:
- sub-30 = final length 29 or less.
- "sub-22 for 3C skeleton" = a 3c skeleton of 21 moves or fewer; "sub-20 for every other skeleton" = any other
  leftover in 19 or fewer. The advice puts the two targets two moves apart.
- The correction is that two moves is too small a gap: at the stated limits the chances are uneven
  (3c in 21: 99.6%; 5c in 19: 48%; 3c1t in 19: 63%), and the same expected total needs 4.0 to 4.8 moves.

Evidence: chances and rates are sampled (20,000 skeletons per length, odd lengths sampled directly); the 19-move 5c
example replays and 30 is its exact optimum with two 8-movers (`A3_example`); that 30 is the most common outcome of
a 19-move 5c is from the sample.
