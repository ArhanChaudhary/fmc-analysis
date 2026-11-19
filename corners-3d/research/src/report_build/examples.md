# Corners in 3D: worked examples

Examples for [the write-up](./). Corners only, DBL held, R U F turns, and *solved* means HTR.

Types are seven characters in the order UFR UFL UBL UBR DFR DFL DBR: `.` good (3 stickers oriented), `+` `-` twisted clockwise / counter-clockwise (0 oriented), `r` `u` `f` out (only the R/L, U/D or F/B sticker oriented). A scramble here is a shortest sequence that makes the state from solved, so you can put it on a cube in a few turns.

## 1. Twelve states, read step by step

**1. One face.**

```
R                         // types {= S("R")['kinds'] =}
```

Four out corners, all with the R/L sticker oriented, all on R. The count table row (0 twisted, out 4) says at least {= crow(0, [4, 0, 0])['floor_d'] =}. A quarter turn of R turns `r` corners on R into good ones (rule of 4.2), so R or R' makes everything good. Check the end: after R' the D-colour corners are the whole D face, a 4a picture, and one quarter turn from an odd state leaves even parity. HTR. {= S("R")['d'] =} move.

**2. Two faces.**

```
R U                       // types {= S("R U")['kinds'] =}
```

Two twisted corners where R and U overlap (UFR, UFL after the U), `u` corners on the rest of U, `r` corners on the rest of R. A U turn fixes the `u` ones and turns the twisted ones into `r`. Then R finishes. {= S("R U")['sol'] =}: {= S("R U")['d'] =} moves, and the types floor is {= S("R U")['types'] =}, so that's optimal.

**3. Bars.**

```
U R2 U'                   // types {= S("U R2 U'")['kinds'] =}
```

Four `u` corners in a 4b shape: no half turns bring them onto one face. That's 4b2 on a DR. {= S("U R2 U'")['sol'] =}, {= S("U R2 U'")['d'] =} moves and {= S("U R2 U'")['q'] =} quarter turns.

**4. A face that isn't 1 qt.**

```
R' U2 R2 F2 R'            // types {= S("R' U2 R2 F2 R'")['kinds'] =}
```

Four `r` corners in a 4a shape again, so it looks like example 1 after a setup: the types floor is {= S("R' U2 R2 F2 R'")['types'] =} moves and {= S("R' U2 R2 F2 R'")['types_q'] =} quarter turn. But parity is {= S("R' U2 R2 F2 R'")['parity'] =}, so the number of quarter turns has to be even. One quarter turn can't be it. With parity the floor is {= S("R' U2 R2 F2 R'")['par'] =}, and that's the answer: {= S("R' U2 R2 F2 R'")['sol'] =}, {= S("R' U2 R2 F2 R'")['d'] =} moves, {= S("R' U2 R2 F2 R'")['q'] =} quarter turns. This is 4a2. The 1-qt way, {= S("R' U2 R2 F2 R'")['tsol'] =}, makes every corner good and lands in a fake HTR.

**5. A fake HTR.**

```
U R2 U F2 U2 R2 U F2 U    // types {= S("U R2 U F2 U2 R2 U F2 U")['kinds'] =}
```

Every corner good. The D-colour corners: with DBL they sit 2 and 2 by tetrad, but the two pairs are on neighbouring faces. That's 4b, not 4a, so it isn't HTR, whatever the parity (here {= S("U R2 U F2 U2 R2 U F2 U")['parity'] =}). It's {= S("U R2 U F2 U2 R2 U F2 U")['d'] =} moves from HTR like every fake HTR, {= S("U R2 U F2 U2 R2 U F2 U")['q'] =} quarter turns, {= S("U R2 U F2 U2 R2 U F2 U")['niss'] =} moves with NISS.

**6. Two twisted corners.**

```
{= R['only_twisted']['2']['witness'] =}          // types {= S(R['only_twisted']['2']['witness'])['kinds'] =}
```

It looks like almost nothing. The count table row (2 twisted, out 0) says at least {= crow(2, [0, 0, 0])['floor_d'] =} moves and {= crow(2, [0, 0, 0])['floor_q'] =} quarter turns, and this state meets it: {= S(R['only_twisted']['2']['witness'])['sol'] =}. A twisted corner needs two quarter turns on different axes, and there's no way to give two corners that without dragging others along.

**7. Four twisted corners.**

```
U F2 U2 F'                // types {= S("U F2 U2 F'")['kinds'] =}
```

Twice as many twisted corners and it's {= S("U F2 U2 F'")['d'] =} moves: {= S("U F2 U2 F'")['sol'] =}. All four sit on one face, a half turn setup puts the same four on another face, and two quarter turns on different axes do the job. The row (4 twisted, out 0) has floor {= crow(4, [0, 0, 0])['floor_d'] =}.

**8. A typical state.**

```
{= rnd(0)['scramble'] =}     // types {= rnd(0)['kinds'] =}
```

{= rnd(0)['twisted'] =} twisted, out {= rnd(0)['out'][0] =} + {= rnd(0)['out'][1] =} + {= rnd(0)['out'][2] =} by axis. Count table: at least {= rnd(0)['floor_count'] =}. The types floor is {= rnd(0)['floor_types'] =}: `{= rnd(0)['types_solution'] =}` makes every corner good. But it ends in a fake HTR. Parity is {= rnd(0)['parity'] =}, and with parity the floor is {= rnd(0)['floor_par'] =}. The truth is {= rnd(0)['d'] =}: `{= rnd(0)['solution'] =}`. Only {= len(rnd(0)['closer']) =} of the nine turns get closer ({= ', '.join(rnd(0)['closer']) =}), and nothing you can read off the types says which.

**9. One where the types are enough.**

```
{= first_random(d=5)['scramble'] =}     // types {= first_random(d=5)['kinds'] =}
```

Types floor {= first_random(d=5)['floor_types'] =}, and it's {= first_random(d=5)['d'] =} from HTR: `{= first_random(d=5)['solution'] =}`. Closer turns: {= ', '.join(first_random(d=5)['closer']) =}.

**10. NISS beats the one-sided floor.**

```
{= X['niss']['witness_broken']['scramble'] =}                // types {= X['niss']['witness_broken']['kinds'] =}
```

Four `f` corners, in a 4a shape but not on F: on one side you need the three half turns back, so the types floor is {= X['niss']['witness_broken']['types_floor'] =} and the state is {= X['niss']['witness_broken']['linear'] =} from HTR. On the inverse the same four corners are on F, and (F) is HTR: {= X['niss']['witness_broken']['niss'] =} with NISS. The quarter-turn count is {= S(X['niss']['witness_broken']['scramble'])['q'] =} either way.

**11. Eight quarter turns.**

```
{= far('q') =}     // types {= S(far('q'))['kinds'] =}
```

One of the {= R['hist_q'][8] =} states that need 8 quarter turns. It's {= S(far('q'))['d'] =} moves from HTR, and the subset number of its placement is only {= S(far('q'))['subset'] =}: the twist costs {= S(far('q'))['q'] - S(far('q'))['subset'] =}.

**12. A 5-qt DR case, both ways.**

```
{= dr_row('2c5')['scramble'] =}     // a 2c5, types {= dr_row('2c5')['kinds'] =}
{= dr_row('2c5')['dr_solution'] =}     // {= dr_row('2c5')['dr_only'] =} moves staying in DR
{= dr_row('2c5')['solution'] =}     // {= dr_row('2c5')['all'] =} moves with off-axis turns
```

The fewest quarter turns is {= dr_row('2c5')['q'] =} either way, but the 8-mover isn't a 5-qt solution: it spends {= quarters_of(dr_row('2c5')['solution']) =} quarter turns and {= len(dr_row('2c5')['solution'].split()) - quarters_of(dr_row('2c5')['solution']) =} half turn, against {= quarters_of(dr_row('2c5')['dr_solution']) =} and {= len(dr_row('2c5')['dr_solution'].split()) - quarters_of(dr_row('2c5')['dr_solution']) =} for the DR one. Off-axis you trade half turns for quarter turns.

## 2. Every pattern within 3 moves of all good

If the types of your state, up to the symmetries that keep DBL, aren't in this table and aren't all good, the types floor is at least 4. There are {= E['catalogue_patterns'] - 1 =} such patterns; one row stands for the ones that are alike by turning the cube about the DBL-UFR diagonal or mirroring through it. *Quarter turns in them* is how many of the moves are quarter turns.

{{ t_catalogue() }}

By floor, the number of type patterns: {= ', '.join(f'{n(c)} at {i}' for i, c in enumerate(E['patterns_by_floor'])) =}.

## 3. 200 random states

Uniformly random over the {= n(N) =} states. For each one: the scramble, what you can read, and the floors. The answer is folded: moves and quarter turns to HTR, which turns get closer, a shortest way, and where the first shortest way to all good ends.

In this sample the types floor is the true distance for {= E['random_summary']['types_exact'] =} of the 200 and types + parity for {= E['random_summary']['par_exact'] =}. The first shortest way to all good ends in real HTR for {= E['random_summary']['types_way_htr'] =}. Over all states it's exactly 1 in 6, so about 33 was to be expected: this draw is on the lucky side (that many or more comes up {= pc(binom_tail(E['random_summary']['types_way_htr'], 200, 1 / 6)) =} of the time). The 200 are a plain uniform draw with a fixed seed, and every entry is checked.

{{ random_blocks() }}

## 4. DR corner cases, in DR turns and with all turns

One or two cases per subset, scrambled with U, R2 and F2 only. Where leaving DR helps, the first row of the subset is a case where it helps most.

{{ t_dr_examples() }}
