## 12. Real DRs

Everything above weights DR states uniformly inside a subset. The DRs you actually get come from an EO and a DR search on a scramble, so here is the same code run on those. *Computer only*: this is a check of the tables, not something to do in an attempt.

**The population.** {= n(E['gaps']['n_scr']) =} uniformly random scrambles (random states, not nissy's scrambler, which is biased). For each one, every EO-first DR of at most 11 moves cubelib-cli lists, the way the first study's examples page lists them: an EO of at most 5 moves on normal, on inverse or with NISS, then DR on either side without breaking it, on either of the other two axes. That is {= n(E['gaps']['n_dr11']) =} DRs ({= n(E['gaps']['n_dr10']) =} of at most 10 moves). Each DR is the state on the side its DR step is written on ({= p0(E['gaps']['side_inv']) =} end on inverse), turned so its axis is U/D, deduplicated per scramble; of a DR ending in `F` and its twin ending in `F'` only one is kept. The route questions use up to 25,000 of these DRs per subset × edges, drawn from the pool of that cell and weighted back to the population, through this study's own code.

**Two weightings**, both shown:

- **each DR once**: every DR found counts once, so a scramble with 3,000 DRs weighs 3,000 times one with a single DR (the model of *a DR someone wrote down*);
- **each scramble once**: every scramble counts once, split equally over its DRs (the model of *the DR a solver gets*).

Standard errors are clustered by scramble, since DRs of one scramble are not independent. A cell is in **bold** when it is more than 2 points and more than 2 combined standard errors from uniform.

**What this does not model.** It is cubelib's EO-first list: no CO-first or direct DR, no EO longer than 5. A DR and its twin with the last move turned the other way count once. And each DR counts, not each DR a solver would *pick*: someone who keeps a DR for its subset or its short HTR selects on the state, and selection on features inside a subset (pairs, corner case) is not modelled.

**Subset mix.** On 11-move DRs every corner subset's share is within {= f1(E['gaps']['share_maxdiff']) =} points of uniform, and each corner subset's mean optimal finish within {= f2(E['gaps']['mean_maxdiff']) =} moves (on 10-move DRs, with 2 to 4 times larger standard errors, {= f1(E['gaps']['share_maxdiff10']) =} points and {= f2(E['gaps']['mean_maxdiff10']) =} moves).

{{real_subsets}}

What does shift is the bad-edge mix inside a corner subset. With each scramble once, 0e is rarer than uniform in {= E['gaps']['e0_rarer_n'] =} of {= E['gaps']['e0_n'] =} corner subsets (up to {= f1(E['gaps']['e0_max_rarer']) =}% rarer, on {= E['gaps']['e0_max_cells'][0] =}) and 6e up to {= f1(E['gaps']['e6_max_more']) =}% more common. Those cells are small, so pooled numbers hardly move.

**Why it is so close (an argument, not a proof).** The EO and DR search only sees orientations and which slice each edge is in; given those, the rest of the scramble is uniformly random, and for a fixed move sequence the map from scramble to DR state is one-to-one. So each DR found is uniform among the DR states that agree with what the search saw. That information does fix part of the HTR structure, which is why the bad-edge mix can differ; inside such a class every DR state is equally likely. The measurements agree.

**The checklists (section 4) on real DRs**, budget 2, greedy on each population: cumulative share finding the optimal after 1 / 2 / 3 routes, then the same three within +1.

{{real_checklist}}

- **The first route is the same on every corner subset**, and on {= E['gaps']['cell_first_same']['dr11'] =} of 48 subset × edges with each DR once ({= E['gaps']['cell_first_same']['scr11'] =} with each scramble once); the one change in each is a near-tie in a cell of a few hundred DRs.
- **The first three routes are the same, in the same order, everywhere except 0c4.** There the real greedy list brings in {= E['gaps']['c0c4']['new'] =} in place of {= E['gaps']['c0c4']['uni3'] =} (third with each DR once, second with each scramble once); the uniform three routes on the same real DRs find {= f2(E['gaps']['c0c4']['gap']['dr11']) =} and {= f2(E['gaps']['c0c4']['gap']['scr11']) =} points less. On 0c4 every route after the first adds about a point, so this is a tie, not a new route to learn.
- **0c0 is the one corner subset that moves**: its first route finds {= f1(E['gaps']['c0c0_first'][0]) =}% with each DR once and {= f1(E['gaps']['c0c0_first'][1]) =}% with each scramble once, against {= f1(E['gaps']['c0c0_first'][2]) =}%. 0c0 is half a percent of DRs. Everywhere else no checklist number moves by more than {= f1(E['gaps']['chk_maxdiff_ex0c0']) =} point.
- **Per subset × edges** the cells flagged are {= ', '.join(E['gaps']['cell_flag_list']) =}, all 0e or 8e cells holding few DRs: 2c3 0e with each scramble once, first route {= f1(E['gaps']['c2c3_0e'][0]) =} ± {= f1(E['gaps']['c2c3_0e'][1]) =}% against {= f1(E['gaps']['c2c3_0e'][2]) =}%; 0c0 8e with each DR once, {= f1(E['gaps']['c0c0_8e'][0]) =} ± {= f1(E['gaps']['c0c0_8e'][1]) =}% against {= f1(E['gaps']['c0c0_8e'][2]) =}%.

**The other headlines of section 1**:

{{real_headlines}}

The one flagged number is 0c3's *NISS HTR 2+ shorter* with each DR once ({= f1(E['gaps']['c0c3_2plus'][1]) =}% against {= f1(E['gaps']['c0c3_2plus'][0]) =}%; {= f1(E['gaps']['c0c3_2plus'][2]) =}% with each scramble once). Every other headline moves by at most {= f1(E['gaps']['hl_maxdiff_ex0c3']) =} points; every bounding share at R ≤ 3 to 5, per corner subset, by at most {= f1(E['gaps']['bd_maxdiff']) =}; the per-subset HTR numbers of section 6 outside 0c0 by at most {= f1(E['gaps']['q3_corner_max']) =}. The subsets where short reductions reach 80% are still 0c0, 4a1 and 4a2, with 4a2 on the line in every population ({= f1(E['gaps']['b4a2_r5'][0]) =}% uniform, {= f1(E['gaps']['b4a2_r5'][1]) =}% and {= f1(E['gaps']['b4a2_r5'][2]) =}% on real DRs). **No recommendation in this study changes.**
