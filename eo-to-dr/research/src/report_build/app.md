## Appendix A: full tables

**EO to DR by case**, all 40 cases but 0c0e (already a DR), in three tables: how common each case is, the mean turns to DR with each option, and the chance of a DR in 6 or fewer with each option. One axis, any turns and the last turn either way are exact over all 1,082,565 EO-solved states; the better of two DR axes is exact (read by the case on the first axis); normal or inverse and all EO-keeping options together are sampled ({= NSAMP('c') =} states; the last column gives how many fell in each case, and the cases marked *few* rest on about 300 to 1,000). The share and odds, and the one-axis and last-turn columns, are proved in Lean ✓: each printed value is Lean's exact count, rounded (appendix B).

Each row is a case: its share of EO-solved states, and how many of the sampled states fell in it.

{{c6_case_full}}

Mean turns to DR, one column per option:

{{c6_case_full_mean}}

Chance of a DR in 6 or fewer, one column per option:

{{c6_case_full_le6}}

**Normal against inverse after an EO**, by case (sampled, {= NSAMP('c') =} states, same DR axis, EO kept). Cases with fewer than 1,000 samples have noisy correlations. Each row is a case; the last three columns are the chance the inverse is at most 6:

{{c6_normal_inverse}}

**Bad edges on the three axes**, all 65 sorted triples, exact over all 70,963,200 classes of edge states (orientation and slice placement). Each row is a set of bad-edge counts on the three axes, in any order:

{{b5_sorted}}

## Appendix B: how it was computed, and what checks it

**The model.** The cube is the one of the DR-xs study (`is-dr-xs-worth-it/research/xstools/src/cubie.rs`, whose move tables come from a sticker model built from geometry), used unchanged by the Rust tool of this study (`research/eodrtools`). DR on U/D is a coset of the DR group, indexed by corner orientation (2,187), the F/B edge orientation (2,048) and the places of the four E-slice edges (495): {= COSETS() =} cosets. Two exact distance tables from the DR-xs study are reused: fewest turns of any kind to DR on U/D, and fewest turns without F/B quarter turns (keeping F/B EO). Every other DR axis and EO axis is read through a rotation of the cube, and every such mapping is checked against nissy (below). For EO to DR only the EO-solved part of each table is needed ({= EODRT() =} states each).

**The scrambles.** {= n(X('n')) =} uniformly random states, drawn by the study itself (`eodrtools mkscr`, seed 2026) and written as move sequences of about 23 turns. nissy 2.0.8's `scramble` isn't used, because it's biased. Its source (`src/commands.c`, lines 505 to 508) draws a random state as

    eo = rand() % POW2TO11;
    ep = rand() % FACTORIAL12;
    co = rand() % POW3TO7;
    cp = rand() % FACTORIAL8;

and prints a solution of it as the scramble. glibc's `rand()` takes $2^{31}$ values, {= NISSYBIAS('ratio') =} ✓ times $12!$, so `rand() % FACTORIAL12` gives the lowest {= NISSYBIAS('low') =} ✓ edge-permutation indices ({= NISSYBIAS('lowshare') =} ✓ of them) one chance more than the rest: they are {= NISSYBIAS('more') =} ✓ more likely. The other three draws are over ranges small enough that the same bias is negligible. Since the scramble solves the drawn state, the drawn state is the inverse of the scramble, and that is where the effect shows: on {= n(X('n')) =} nissy scrambles the inverse side is shorter to DR, the normal side barely moved. Each row is one way of reaching DR; the *DR in ≤* columns are the share of scrambles:

{{nissy_bias}}

The number of twisted corners per axis is also off on nissy's scrambles, on 7 degrees of freedom; I haven't found the cause. Each row is an axis, with the test statistic and its p-value:

| Axis | $\chi^2$ | p-value |
|---|---|---|
| R/L | {= CHI('nissy', 'RL', 'twisted corners') =} | {= CHIP('nissy', 'RL', 'twisted corners') =} |
| U/D | {= CHI('nissy', 'UD', 'twisted corners') =} | {= CHIP('nissy', 'UD', 'twisted corners') =} |
| F/B | {= CHI('nissy', 'FB', 'twisted corners') =} | {= CHIP('nissy', 'FB', 'twisted corners') =} |

The test of every scramble set (twisted corners, bad edges and slice pieces in their slice, on each axis). Each row is one scramble set, axis and count:

{{scramble_checks}}

The study's own scrambles pass every test. A separate set of {= n(X('s500_n')) =} scrambles from nissy's scrambler shows the same effect. Each row is a mean number of turns to DR; z is how many standard errors those scrambles sit from the uniform sample:

| Mean to DR | Those scrambles, mean turns | Standard error | Uniform sample, mean turns | z |
|---|---|---|---|---|
| Inverse, best of 3 | {= XN('s500_inv_mean', 3) =} | {= XN('s500_inv_se', 3) =} | {= A1('inv', 'mean') =} | {= XN('s500_inv_z', 1) =} |
| Best of six | {= XN('s500_six_mean', 3) =} | {= XN('s500_six_se', 3) =} | {= A1('six', 'mean') =} | {= XN('s500_six_z', 1) =} |
| Normal side (unaffected) | {= XN('s500_lin_mean', 3) =} | | {= A1('lin', 'mean') =} | |

**Per scramble** (`eodrtools scr`): the exact DR distance on each axis, normal and inverse; the NISS DR (pre-turns on one side, stopping where they can no longer win); the number of DR solutions of each length up to 12 on the normal side; the shortest EO inside an optimal DR; every EO of up to 6 turns on each axis, normal, inverse and NISS, each with the exact EO-keeping DR distance on both DR axes; from these the best route through an EO of each length, the (EO, DR axis) counts and the optimal EOs. About 30 minutes on four cores for the {= n(X('n')) =}.

**EO to DR** (`eodrtools eodr`): the per-coset tables directly (one axis, any turns, the last EO turn either way), the better of two DR axes exactly over every corner state and every placement of the E- and M-slice pieces, and the options that need the inverse sampled on {= NSAMP('c') =} uniform EO-solved states with exact lookups.

**Scramble to EO** (`eodrtools eo`): EO distances on one axis exactly (2,048 states), the bad-edge layouts exactly over the 34,650 slice placements times 2,048 flip patterns, and NISS EOs sampled on {= NSAMP('b') =} random states.

**What checks it.**

- Every table mapping against nissy 2.0.8: {= CHK(1) =} of {= CHK(0) =} positions agree, over {= CHK(2) =} mappings (DR from a scramble on each axis, EO-keeping DR for all six pairs of EO axis and DR axis, any-turn DR from EO-solved states, optimal EO per axis, NISS EO over all axes). Each row is one mapping:

{{checks_nissy}}

- Counts against nissy on the first 30 scrambles (DR solutions of 9 and 10, EOs linear and NISS, `nissy -a`), and the NISS DR against `nissy solve dr -N` on 40 scrambles where NISS beats linear. Each row is one count:

{{checks_counts}}

- The known tables come out exactly: the EO-solved part of the EO-keeping table is FakeMMAP's and Cale's 1, 2, 17, …, 3114 (mean {= CT('plain', 'mean') =}); the any-turn version gives torchlight's {= CT('any', 'mean') =}; one-axis EO {= EO1() =}; DougCube's one-axis DR from a scramble, mean {= A1('fixed', 'mean') =}. The sample agrees with the exact one-axis table (mean {= A1('pooled', 'mean') =} on {= PRIOR('one axis', 'ours_n') =} axes; $\chi^2$ {= PRIOR('one axis', 'chi2') =} on {= PRIOR('one axis', 'df') =} df), and with the DR-xs study's {= PRIOR('best of 6 (normal or inverse)', 'prior_n') =} scrambles (best of three, $\chi^2$ {= PRIOR('best of 3 axes, normal', 'chi2') =} on {= PRIOR('best of 3 axes, normal', 'df') =} df; best of six, {= PRIOR('best of 6 (normal or inverse)', 'chi2') =} on {= PRIOR('best of 6 (normal or inverse)', 'df') =}).
- The sampled EO to DR rows agree with the exact ones where both exist (one axis: {= CSTAT('check_plain_exact_vs_sampled', 'sampled', 'mean') =} sampled against {= CSTAT('check_plain_exact_vs_sampled', 'exact', 'mean') =} exact).
- Every solution in the per-scramble tables (NISS DR, optimal DR with its EO split, the best routes through EOs of at most 4, 5 and 6) is replayed on the sticker model, a separate implementation that reads EO and DR off the stickers; so is every example in this write-up ({= WX['checks'] =} checks) and every move sequence on the examples page.
- The optimal solutions of the first three scrambles with no sub-10 DR (nissy `solve optimal`, about 3.5 GB) are replayed and solve the cube.
- **Lean** (`lean/EODR`, Lean 4, no Mathlib; its README lists every theorem). **Proved**, marked ✓ in the text: Lean builds the cube from its geometry, redoes each search itself, and checks every distance table with an independent rule.
  - One-axis EO, all 2,048 states: the distances (mean {= EO1() =}), by bad-edge count (Shota's table, 8 against 6 bad, the 10- and 12-bad rows), and the EO counts per state.
  - The bad-edge layouts over all 70,963,200 classes: torchlight's counts, every triple, the shares of section 6.
  - EO to DR over all {= EODRT() =} EO-solved states, one axis and the EO's last turn either way: the distribution (Cale's and FakeMMAP's), the {= EODRN(10) =} at 10, the {= CT('plain', 'p_le6') =} in 6, every per-case figure quoted, and every value in the share, odds, one-axis and last-turn columns of the case tables (section 5 and appendix A). That check found three values rounded twice (7c6e and 6c2e with the last turn, 0c4e's share), now fixed. Also the corner-twist counts (Emma's and Zagros's).
  - The superflip has no NISS EO under 7 on any axis: it commutes with every face turn, so any NISS EO of it is a linear EO of the same length.
  - Arithmetic: nissy's modulo bias, the binomials (Lichi Fang's 3 of 27, DougCube's 92.71%), the coset count.
  - The errata examples (the EO 10 from DR, the 4c6e, the superflip's NISS EO) are checked on the Lean cube too (`htr-routes/lean/FakeBound/Corrections`).

  **Computed, not proved**: everything sampled (the {= n(X('n')) =} scrambles, the {= NSAMP('b') =} EO states, the {= NSAMP('c') =} EO-solved states: every NISS, inverse and all-options row); the any-turn tables over 2,217,093,120 cosets (torchlight's {= CT('any', 'mean') =}, DougCube's {= A1('fixed', 'mean') =}, Louis's shares); the better of two DR axes (exact, but in Rust only); the optimal solves; the measurements of nissy's scrambles.

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
