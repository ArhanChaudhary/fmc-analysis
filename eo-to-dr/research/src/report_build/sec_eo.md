## 4. Scramble to EO

### 4.1 How many EOs, how short

How many EOs a scramble has, on the same {= n(X('n')) =} uniformly random scrambles. An EO of length L is a move sequence that solves EO on its axis for the first time at its L-th turn, so its last turn is a quarter turn of that axis, and the two directions of that last turn count as two EOs. That's nissy's `solve eo -a` listing, and my counts match nissy's on 30 scrambles (appendix B).

nissy without `-a` drops the EOs that end in `F'` or `B'` (or the matching turns of the other axes), so it lists about half as many; the counts quoted on the server are mostly of that kind. A NISS EO has turns on both sides, each side ending in a quarter turn of the axis. Each row is a kind of EO and its axes; the cells are the mean number of EOs per scramble up to that length:

{{b4}}

The same rows: medians, the share of scrambles with no EO that short, and the most on one scramble:

{{b4_more}}

The columns up to 4 turns are lists you can actually write; the 5- and 6-turn counts, hundreds to thousands per scramble, are nissy's `-a` listings, **computer only**, there to compare scrambles, not to write out. The one-axis normal row is also exact over the 2,048 orientations of one axis: at most 5 turns, mean {= B4('linear (normal)', 'one axis (F/B)', 5, 'mean_le') =} in the sample against {= B4X(5, 'mean_le') =} exact.

The shortest EO of a scramble, over the three axes. Each row is a side rule; the *EO in ≤* columns are the share of scrambles with an EO that short:

{{b4_opt}}

The fixed-axis row is exact (DougCube's {= EO1() =} in [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo)). The NISS row reproduces Joba's exact 3.455 ([[T9374]]) to within the sample's error, and Joba's table also gives the rarest case, one the sample never hit: 7 turns even with NISS ("Distance 7: 1792" of all $12!\cdot 2^{11}$ edge states).

What's new is the middle two rows, linear on all three axes and normal or inverse, and the odds at each length. (The {= n(X('n')) =} scrambles of section 3 agree within sampling error: an EO of at most 4, normal or inverse, on {= A2('b', 4, 'p_has_eo') =} of them against {= BOPT('any_axis_lin_or_inv', 'le4') =} here.) The short ones, as the share of scrambles with an EO of that length or shorter on some axis:

| EO on some axis | Linear | With the inverse | With NISS |
|---|---|---|---|
| 3-move | {= BOPT('any_axis_linear', 'le3') =} | {= BOPT('any_axis_lin_or_inv', 'le3') =} | {= BOPT('any_axis_niss', 'le3') =} |
| 2-move | {= BOPT('any_axis_linear', 'le2') =} | {= BOPT('any_axis_lin_or_inv', 'le2') =} | {= BOPT('any_axis_niss', 'le2') =} |

Odd scrambles, from the {= n(X('n')) =}:

- **No EO of at most 5 turns on any axis, even with NISS**: {= B4('NISS (normal, inverse, both)', 'all three axes', 5, 'p_none_le') =} of scrambles, {= NONE5() =} in the sample [d].
- **More 3-move EOs than 4-move EOs**: never with linear EOs (normal side, all axes) in the sample; with NISS on {= MORE3('niss') =} of scrambles [e].
- **An N-move EO but no (N+1)-move EO** (all axes):
  - 1 turn and none of 2: {= GAP('linear', '1_but_no_2') =} linear;
  - 2 and no 3: {= GAP('linear', '2_but_no_3') =};
  - 3 and no 4: never linearly in the sample, {= GAP('niss', '3_but_no_4') =} with NISS;
  - never for 4 and 5.

### 4.2 Bad edges on the three axes

Exact over all $12!\cdot 2^{11}$ edge states (34,650 ways to place the E-, M- and S-slice pieces times 2,048 flip patterns; within a slice the order does not matter). torchlight computed the sorted triples in 2023 (the speedsolving post on bad-edge counts, and [[D3299]]). The table here is the same; on top of it I add the ordered triples, the layouts by axis and the EO odds by bad-edge count. The most common sorted triples; each row is a set of bad-edge counts on the three axes, in any order:

{{b5_top}}

All 65 are in appendix A. A few facts that come out exactly:

- all 12 edges good on one given axis: probability $1/2048$; on some axis: ${= LAY('states_some_axis_eo_solved') =}/70963200$ ({= LAYP(lambda t: 0 in t) =});
- 12/12/12 is 1 in 70,963,200;
- some axis has 10 bad on {= LAYP(lambda t: 10 in t) =} of scrambles;
- no two axes differ by more than 8;
- after an EO the other two axes have 0, 2, 4, 6 or 8 bad.

Uneven triples are rarer than independent axes would make them: 2/10/10 has probability {= LAYP(lambda t: sorted(t) == [2, 10, 10]) =}, against {= INDEP((2, 10, 10)) =} if the axes were independent, {= RATIO_2_10_10() =} times less.

The chance of a short EO on one axis, by its number of bad edges. The last column, the shortest normal EO of each of the 2,048 states, is Shota's table ([[D7761]]) and agrees with Shota's *Full EO* sheet; the new part is the odds with the inverse and with NISS. The normal columns are exact over the 2,048 states of one axis. The inverse and NISS columns are sampled, 1,000,000 random states times 3 axes, so ±0.1 point or better, except the rare 0-, 10- and 12-bad rows, which rest on about 1,400 to 97,000 axes. Each row is a number of bad edges on the axis; the *EO in ≤* columns are the share of such axes with an EO that short:

{{b5_by_bad}}

With NISS, same rows:

{{b5_by_bad_niss}}

Shota's table: each row is a length of the shortest normal EO, each column a number of bad edges, and the cell is how many of the 2,048 edge-orientation states have it (– for none):

{{b5_hist}}

This table is for the attempt: the bad edges on each axis are what you see when you look for EO, and the row gives the odds of a short EO on that axis.

What it says:

- **8 bad beats 6 bad for short EOs, linearly**: an EO of at most 4 on {= B5(8, 'p_linear_le4') =} of 8-bad axes against {= B5(6, 'p_linear_le4') =} of 6-bad ones, of at most 3 on {= B5(8, 'p_linear_le3') =} against {= B5(6, 'p_linear_le3') =}. With NISS 6 bad is a little better ({= B5(6, 'p_niss_le4') =} against {= B5(8, 'p_niss_le4') =} for at most 4).
- **10 and 12 bad**: no normal EO under 6 ({= B5H(10, 6) =} of the {= B5N(10) =} ten-bad states of one axis take 6, {= B5H(10, 7) =} take 7; twelve bad takes {= [k for k in ('6','7') if B5H(12, k) != '0'][0] =}).
- **With NISS a 12-bad axis is better than a 10-bad one**: at most 5 on {= B5(12, 'p_niss_le5') =} against {= B5(10, 'p_niss_le5') =}, at most 4 on {= B5(12, 'p_niss_le4') =} against {= B5(10, 'p_niss_le4') =}.
- **Normal or inverse doesn't help a 10- or 12-bad axis**: the inverse has the same number of bad edges on each axis as the normal side.
