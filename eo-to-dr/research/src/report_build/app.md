## Appendix A: full tables

**EO to DR by case**, all 40 cases. Each cell: mean turns to DR, then the chance of at most 6. One axis, any turns and the last turn either way are exact over all 1,082,565 EO-solved states; the better of two DR axes is exact (read by the case on the first axis); normal or inverse and all EO-keeping options together are sampled ({= NSAMP('c') =} states; the last column gives how many fell in each case, and the cases marked *few* rest on about 300 to 1,000).

{{c6_case_full}}

**Normal against inverse after an EO**, by case (sampled, {= NSAMP('c') =} states, same DR axis, EO kept). Cases with fewer than 1,000 samples have noisy correlations.

{{c6_normal_inverse}}

**Bad edges on the three axes**, all 65 sorted triples, exact over all 70,963,200 classes of edge states (orientation and slice placement):

{{b5_sorted}}

## Appendix B: how it was computed, and what checks it

**The model.** The cube is the one of the DR-xs study (`is-dr-xs-worth-it/research/xstools/src/cubie.rs`, whose move tables come from a sticker model built from geometry), used unchanged by the Rust tool of this study (`research/eodrtools`). DR on U/D is a coset of the DR group, indexed by corner orientation (2,187), the F/B edge orientation (2,048) and the places of the four E-slice edges (495): {= COSETS() =} cosets. Two exact distance tables from the DR-xs study are reused: fewest turns of any kind to DR on U/D, and fewest turns without F/B quarter turns (keeping F/B EO). Every other DR axis and EO axis is read through a rotation of the cube, and every such mapping is checked against nissy (below). For EO to DR only the EO-solved part of each table is needed ({= EODRT() =} states each).

**The scrambles.** {= n(X('n')) =} uniformly random states, drawn by the study itself (`eodrtools mkscr`, seed 2026) and written as move sequences of about 23 turns. nissy 2.0.8's `scramble` was used first and dropped. Its source (`src/commands.c`, lines 505 to 508) draws a random state as

    eo = rand() % POW2TO11;
    ep = rand() % FACTORIAL12;
    co = rand() % POW3TO7;
    cp = rand() % FACTORIAL8;

and prints a solution of it as the scramble. glibc's `rand()` takes 2^31 values, {= NISSYBIAS('ratio') =} times 12!, so `rand() % FACTORIAL12` gives the lowest {= NISSYBIAS('low') =} edge-permutation indices ({= NISSYBIAS('lowshare') =} of them) one chance more than the rest: they are {= NISSYBIAS('more') =} more likely. The other three draws are over ranges small enough that the same bias is negligible. Since the scramble solves the drawn state, the drawn state is the inverse of the scramble, and that is where the effect shows: on {= n(X('n')) =} nissy scrambles the inverse side is shorter to DR, the normal side barely moved:

{{nissy_bias}}

The number of twisted corners per axis is also off on nissy's scrambles (chi² {= CHI('nissy', 'RL', 'twisted corners') =}, {= CHI('nissy', 'UD', 'twisted corners') =}, {= CHI('nissy', 'FB', 'twisted corners') =} on 7 degrees of freedom, p = {= CHIP('nissy', 'RL', 'twisted corners') =}, {= CHIP('nissy', 'UD', 'twisted corners') =}, {= CHIP('nissy', 'FB', 'twisted corners') =}); the cause of that is not identified. The test of every scramble set (twisted corners, bad edges and slice pieces in their slice, on each axis):

{{scramble_checks}}

The study's own scrambles pass every test. The {= n(X('s500_n')) =} scrambles the judging-a-dr study first used came from nissy's scrambler (it now uses uniform ones), and they show the same effect: the inverse best of 3 averages {= XN('s500_inv_mean', 3) =} ± {= XN('s500_inv_se', 3) =} against {= A1('inv', 'mean') =} on the uniform sample (z = {= XN('s500_inv_z', 1) =}), the best of six {= XN('s500_six_mean', 3) =} ± {= XN('s500_six_se', 3) =} against {= A1('six', 'mean') =} (z = {= XN('s500_six_z', 1) =}), while the normal side is unaffected ({= XN('s500_lin_mean', 3) =} against {= A1('lin', 'mean') =}).

**Per scramble** (`eodrtools scr`): the exact DR distance on each axis, normal and inverse; the NISS DR (pre-turns on one side, stopping where they can no longer win); the number of DR solutions of each length up to 12 on the normal side; the shortest EO inside an optimal DR; every EO of up to 6 turns on each axis, normal, inverse and NISS, each with the exact EO-keeping DR distance on both DR axes; from these the best route through an EO of each length, the (EO, DR axis) counts and the optimal EOs. About 30 minutes on four cores for the {= n(X('n')) =}.

**EO to DR** (`eodrtools eodr`): the per-coset tables directly (one axis, any turns, the last EO turn either way), the better of two DR axes exactly over every corner state and every placement of the E- and M-slice pieces, and the options that need the inverse sampled on {= NSAMP('c') =} uniform EO-solved states with exact lookups.

**Scramble to EO** (`eodrtools eo`): EO distances on one axis exactly (2,048 states), the bad-edge layouts exactly over the 34,650 slice placements times 2,048 flip patterns, and NISS EOs sampled on {= NSAMP('b') =} random states.

**What checks it.**

- Every table mapping against nissy 2.0.8: {= CHK(1) =} of {= CHK(0) =} positions agree, over {= CHK(2) =} mappings (DR from a scramble on each axis, EO-keeping DR for all six pairs of EO axis and DR axis, any-turn DR from EO-solved states, optimal EO per axis, NISS EO over all axes):

{{checks_nissy}}

- Counts against nissy on the first 30 scrambles (DR solutions of 9 and 10, EOs linear and NISS, `nissy -a`), and the NISS DR against `nissy solve dr -N` on 40 scrambles where NISS beats linear:

{{checks_counts}}

- The known tables come out exactly: the EO-solved part of the EO-keeping table is FakeMMAP's and Cale's 1, 2, 17, …, 3114 (mean {= CT('plain', 'mean') =}); the any-turn version gives torchlight's {= CT('any', 'mean') =}; one-axis EO {= EO1() =}; DougCube's one-axis DR from a scramble, mean {= A1('fixed', 'mean') =}. The sample agrees with the exact one-axis table (mean {= A1('pooled', 'mean') =} on {= PRIOR('one axis', 'ours_n') =} axes; chi² {= PRIOR('one axis', 'chi2') =} on {= PRIOR('one axis', 'df') =} df), and with the DR-xs study's {= PRIOR('best of 6 (normal or inverse)', 'prior_n') =} scrambles (best of three, chi² {= PRIOR('best of 3 axes, normal', 'chi2') =} on {= PRIOR('best of 3 axes, normal', 'df') =} df; best of six, {= PRIOR('best of 6 (normal or inverse)', 'chi2') =} on {= PRIOR('best of 6 (normal or inverse)', 'df') =}).
- The sampled EO to DR rows agree with the exact ones where both exist (one axis: {= CSTAT('check_plain_exact_vs_sampled', 'sampled', 'mean') =} sampled against {= CSTAT('check_plain_exact_vs_sampled', 'exact', 'mean') =} exact).
- Every solution in the per-scramble tables (NISS DR, optimal DR with its EO split, the best routes through EOs of at most 4, 5 and 6) is replayed on the sticker model, a separate implementation that reads EO and DR off the stickers; so is every example in this write-up ({= WX['checks'] =} checks) and every move sequence on the examples page.
- The optimal solutions of the first three scrambles with no sub-10 DR (nissy `solve optimal`, about 3.5 GB) are replayed and solve the cube.
- **Lean.** A certificate of the small exact tables (the bad-edge layouts and the one-axis EO distances) is being built separately: see `lean/EODR/README.md`.

`research/README.md` lists every step, its command, its input and output, and how long it takes; `research/out/SUMMARY.md` has every number the tables are made from.

## Docs referred to

- Cale, [*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0), and [*DR setup stats (switching last move)*](https://docs.google.com/spreadsheets/d/1_2PmFv1KyBX335SjSb4oweS0sx804fIhbuP50D-gBj4).
- Louis, [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs), code at [github.com/LouisSart/DRM-ARM-stats](https://github.com/LouisSart/DRM-ARM-stats).
- KrzychXyz, [*All EO-> DR cases*](https://docs.google.com/spreadsheets/d/1dNjuqAW0wTbP3qeV5aSfo1KbrVlfvCk0_0DOfsUiJLk).
- Evan, [*arm/pairs*](https://docs.google.com/spreadsheets/d/1YZYyokxYXwDdBTgN7ojpPAFHKKz48hCyNO2l6-iwmVk).
- Rodney Kinney, [*DRM corner variant+pair stats*](https://docs.google.com/spreadsheets/d/174ClwBFl-T2zJAq8MVyK1bKsIIuzxQU0_XmQGv82LPQ); [*Multi-Axis DR*](https://docs.google.com/spreadsheets/d/1fYdYEGlBk3bv5x2WVSA0NtsPWVlNKbtyK-Iq-J6VjDY).
- DougCube, [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo).
- Cale, [*Official 5 move EO counts*](https://docs.google.com/spreadsheets/d/1jLDRWYn31ou-Br3ReNVH7EnDYPovMZLIpuCWWZEBCO8) (official scrambles to April 2023).
- torchlight, the exact bad-edge counts on the three axes: [Probability Thread, post 1520621](https://www.speedsolving.com/threads/probability-thread.20384/post-1520621) (speedsolving.com).
- Kociemba, [*Distribution of the Pruning Values*](https://kociemba.org/math/distribution.htm) (the phase-1 table, by symmetry classes, not positions).
- nissy 2.0.8, by Sebastiano Tronto ([nissy.tronto.net](https://nissy.tronto.net)), used for the cross-checks.
