## 3. Scramble to DR

All of this section is on {= n(X('n')) =} uniformly random scrambles (appendix B says how they are drawn and why not with nissy's `scramble`), with exact distance tables for every lookup: each number for one scramble is exact, and the only uncertainty is the sample. On {= n(X('n')) =} scrambles a share has a standard error (one standard deviation of the estimate) of at most 0.2 points, and a mean about {= SE('six') =} turns. Any turns are allowed on the way to DR unless a line says the EO is kept. Turns are face turns (HTM).

**This whole section is computer only, the answer key.** Every number is what exists, from exact search: the optimal DR over every axis and side (3.1), or every EO of a given length with the best DR after it on both DR axes (3.2, 3.3). It says where the short DRs are, not what a solver finds in an hour, and none of it is a check to run in an attempt. The hand-usable versions are elsewhere: count the bad edges for the odds of a short EO (4.2), and read the case each EO leaves on both DR axes for the odds of a short DR (5.2).

### 3.1 The shortest DR

{{a1}}

*One fixed axis* is DR on one given axis with turns after the scramble only, exact over every coset; it is DougCube's table (the "Going to DR" tab of [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo)) and Louis's 6.2% and 43% ([[T5957]], [[T5959]], restated for one axis, linear, in [[T5964]]). *Best of 3 axes, normal*: the fewest turns to DR on any axis, turns after the scramble only. *Inverse*: the same on the inverse scramble. *Best of 6*: the better of those two, the six tries of 3 axes on each side. *NISS*: turns on both sides, counted together, best of 3 axes.

What it says:

- **Three axes are worth {= f2(A['a1'][A1N['fixed']]['mean'] - A['a1'][A1N['lin']]['mean']) =} turns, the inverse another {= f2(A['a1'][A1N['lin']]['mean'] - A['a1'][A1N['six']]['mean']) =}, NISS another {= f2(A['a1'][A1N['six']]['mean'] - A['a1'][A1N['niss']]['mean']) =}.** One axis averages {= A1('fixed', 'mean') =}, the best of three on one side {= A1('lin', 'mean') =}, the best of six {= A1('six', 'mean') =}, with NISS {= A1('niss', 'mean') =}. Normal and inverse are the same thing statistically ({= A1('lin', 'mean') =} and {= A1('inv', 'mean') =}), but on a given scramble they often differ: the inverse is shorter on {= XP('inv_better') =} of scrambles and longer on {= XP('inv_worse') =}.
- **In 10 or better.** Linear on one side: {= A1('lin', 'p_le10') =}. Best of six: every scramble in the sample. **In 9 or better**: {= A1('lin', 'p_le9') =}, {= A1('six', 'p_le9') =} with the inverse, {= A1('niss', 'p_le9') =} with NISS. **In 8 or better**: {= A1('lin', 'p_le8') =}, {= A1('six', 'p_le8') =}, {= A1('niss', 'p_le8') =}.
- **NISS beats the best of six linear tries on {= GAINGE('niss_gain_over_6', 1) =} of scrambles**: by one turn on {= GAIN('niss_gain_over_6', 1) =}, by two on {= GAIN('niss_gain_over_6', 2) =}, by three on {= GAIN('niss_gain_over_6', 3) =}.
- **No sub-10 DR at all.** {= XP('no_sub10_six') =} of scrambles have no DR under 10 on any axis, normal or inverse, and {= XP('no_sub10_niss') =} ({= n(X('no_sub10_niss_n')) =} of {= n(X('n')) =}) have none even with NISS. None in the sample needs more than 10 with NISS, or more than 10 best of six [a]; on one side, linear, the longest seen is {= A1('lin', 'max') =} (on {= A1COUNT('lin', 11) =} scrambles). The superflip is one of the scrambles with no sub-10 DR, and not a special one: 10 on every axis, normal and inverse, and 10 with NISS [b].

How many DR solutions a scramble has, normal side, all three axes (each canonical move sequence that reaches DR for the first time at its last turn counts once, as `nissy solve dr -a` lists them; a solution and the same with its last turn the other way count as two):

{{a1_solutions}}

So the median scramble has {= CELL('a1_solutions', '9', 'Median') =} DRs of 9 on the normal side and {= CELL('a1_solutions', '10', 'Median') =} of 10. Its optimal DRs, of whatever length that is, number {= NOPT() =} on average (median {= f'{X("nopt_median"):.0f}' =}); on {= XP('nopt_le2') =} of scrambles there is just one, counted twice for the direction of its last turn.

### 3.2 The optimal DR against DRs through a short EO

A human DR goes through an EO: an EO, then turns that keep it, to DR on one of the two other axes. Any DR solution contains an EO in that sense: cut it after its last quarter turn of an axis that is not the DR axis, and what comes before is an EO on that axis (Joba said the same of DR solutions in general, [[T9930]]). So the question is how long that EO is.

The shortest EO inside an optimal normal DR, over all optimal DRs of the scramble and both EO axes, normal side, {= n(X('n')) =} scrambles:

{{estar}}

The optimal DR starts with an EO of at most 5 turns on {= EST(5) =} of scrambles, at most 4 on {= EST(4) =}. On {= EST(6, 'ge') =} it needs 6 or more, and on {= EST(7, 'ge') =} 7 or more [c]. So most optimal DRs are out of reach of the EOs people write down, because their EO is long. (Every DR solution starts with an EO in this sense, so the optimum never needs EO-breaking turns.) What EO-breaking turns add to a short EO: among routes through EOs of at most 5, a continuation with any turns reaches the optimal DR where no EO-keeping one does on {= BRK(5) =} of {= n(X('n')) =} scrambles ({= BRK(4) =} for EOs of at most 4, {= BRK(6) =} for at most 6).

What the best route through a short EO gives, against the optimal (normal EOs for the optimal normal DR; normal or inverse EOs for the best of six; all EOs, normal, inverse and NISS, for the NISS optimum and for the best of six; a NISS EO takes its DR on the better of the two sides):

{{a2}}

*Has such an EO*: the scramble has an EO of that length or shorter of that kind on some axis. *Best route = optimal*: the best EO, then EO-keeping turns, is as short as the optimal DR it is compared with. *Shorter than it*: possible only when NISS EOs are compared with the linear best of six. *Mean loss* is over the scrambles that have such an EO.

The same as odds of a DR of a given length from the scramble, which is what a solver aims at:

{{a2_targets}}

In words, DR in 10 or better and in 11 or better: with normal EOs of at most 5 turns, {= XP('route_n5_le10') =} and {= XP('route_n5_le11') =} of scrambles; adding the inverse EOs, {= XP('route_b5_le10') =} and {= XP('route_b5_le11') =}; adding the NISS EOs, {= XP('route_x5_le10') =} and {= XP('route_x5_le11') =}. With EOs of at most 4 of every kind, {= XP('route_x4_le10') =} and {= XP('route_x4_le11') =}. A route through an EO of at most 5 (all kinds) is 9 or better on {= XP('route_x5_le9') =} of scrambles, against {= A1('niss', 'p_le9') =} for the NISS optimum. These are what exists, not what anybody finds: every EO of that length is checked, with both DR axes and the best DR after it. **Computer only**: an answer key for how good the EOs you could write are, not a search to do in an attempt.

### 3.3 How many DRs

For every EO of at most k turns and each of its two DR axes, is the EO plus the best DR after it (EO kept; for a NISS EO on the better side) at most N turns? A scramble's count is the number of such (EO, DR axis) pairs. Like 3.2 these are **computer only**: they need the best DR after every EO on both axes, and say how many DRs exist, not how many a solver finds. Cells: the mean number of pairs per scramble, and in brackets the share of scrambles with none. {= n(X('n')) =} scrambles. EOs counted as in nissy's `-a` listing (both directions of the last turn).

{{a3}}

Per EO this is a small number, and it drops fast with the EO's length. Expected (EO, DR axis) pairs per EO, normal EOs, all three axes. Each yield is a ratio of sums (all pairs over all EOs of the kind, over the {= n(X('n')) =} scrambles), and the column for EOs of at most 4 includes those of 0 to 3 turns:

{{a3_yield}}

The last two columns answer Somebodyidk's "25 4 move eos or 200 5 move eos" ([[D16056]]): on average the 25 short EOs give more DRs of 10 or better, the 200 longer ones more of 11 or 12. EOs on one scramble are correlated, so these are expectations over scrambles, not a guarantee on any one. The part you can use in an attempt is the ratio: for a DR in 10, one EO of at most 4 is worth about ten 5-movers, so the 4-movers come first.

Two more measurements of what each kind of EO adds, normal EOs:

- **5-move EOs on top of the 4-movers**: on scrambles that have an EO of at most 4 (all axes), adding the 5-movers gives a shorter best route on {= G('gain_5_over_4_normal', 'p_improves_given_eo_le4') =} of them, by {= G('gain_5_over_4_normal', 'mean_gain_given_eo_le4') =} turns on average counting the scrambles where nothing improves, {= XN('g54_mean_gain_improved') =} turns where it does. {= G('gain_5_over_4_normal', 'p_no_eo_le4') =} of scrambles have no normal EO of at most 4 at all.
- **The other two EO axes on top of F/B** (EOs of at most 5): over all scrambles the best route improves on {= XP('ax_p_improved_all') =}: on {= XP('ax_p_improved_all_part') =} the F/B route gets shorter, and the other {= XP('ax_p_no_fb') =} have no F/B EO of at most 5 at all. On the {= XP('ax_p_fb_has5') =} that have one, it improves on {= XP('ax_p_improved_given_fb') =} of them, from {= XN('ax_mean_fb') =} to {= XN('ax_mean_all_same') =} on average.
