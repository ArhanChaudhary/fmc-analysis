New stuff first, then what the numbers confirm or correct. Scramble-level lines are on {= n(X('n')) =} uniformly random scrambles (a share has a standard error of at most 0.2 points); EO counts by length use {= NSAMP('b') =} random states where they say so; EO to DR lines are exact unless they say sampled ({= NSAMP('c') =} states).

**What is new here**

**How often there's a short DR from the scramble** (optimal DR, 3.1). Each row is what you allow; the middle columns are the share of scrambles with a DR that short:

| Allowed | DR in ≤ 9 | DR in ≤ 8 | Mean, turns |
|---|---|---|---|
| One fixed axis | {= A1('fixed', 'p_le9') =} | {= A1('fixed', 'p_le8') =} | {= A1('fixed', 'mean') =} |
| Linear, one side (3 axes) | {= A1('lin', 'p_le9') =} | {= A1('lin', 'p_le8') =} | {= A1('lin', 'mean') =} |
| Best of six | {= A1('six', 'p_le9') =} | {= A1('six', 'p_le8') =} | {= A1('six', 'mean') =} |
| NISS | {= A1('niss', 'p_le9') =} | {= A1('niss', 'p_le8') =} | {= A1('niss', 'mean') =} |

NISS beats the best of six linear tries on {= GAINGE('niss_gain_over_6', 1) =} of scrambles. The best of six was already in my DR-xs study; the rest is new. **Computer only**: these are optimal DRs over every axis and side, the answer key for what's there, not a length you can check for in an attempt. By hand you get to DR through an EO, and that's what the lines below and 5.2 are about.

- **Sub-10 isn't universal.** {= XP('no_sub10_six') =} of scrambles have no DR under 10 on any of the six tries, and {= XP('no_sub10_niss') =} have none even with NISS; none in the sample needs more than 10 with NISS. The superflip is one of these but not the only one, and they aren't 20-movers: the first three such scrambles of the sample are {= WXX('X3', 0, 'optimal_length') =}, {= WXX('X3', 1, 'optimal_length') =} and {= WXX('X3', 2, 'optimal_length') =} moves optimal [a].
- **The optimal DR usually starts with a long EO.** Its shortest EO (over every optimal DR of the scramble, normal side) is at most 4 turns on {= EST(4) =} of scrambles, at most 5 on {= EST(5) =}, and 7 or more on {= EST(7, 'ge') =} (3.2) [c].
- **EO-breaking turns hardly ever help.** Among routes through an EO of at most 5, a continuation with any turns reaches the optimal DR where no EO-keeping one does on {= BRK(5) =} of {= n(X('n')) =} scrambles ({= BRK(4) =} for EOs of at most 4, {= BRK(6) =} for at most 6). **Computer only**, the answer key. What it means in an attempt: the optimal DR usually isn't behind any EO you write, so judge your DR against the route numbers below, not against the optimum.

**Through the EOs people write down** (each EO with its best EO-keeping DR on either DR axis; a NISS EO takes the DR on the better side; 3.2). Each row is a set of EOs; the columns are the share of scrambles where one of them leads to a DR that short:

| EOs | DR in ≤ 10 | DR in ≤ 11 |
|---|---|---|
| Every EO of at most 5 turns, normal, inverse and NISS | {= XP('route_x5_le10') =} | {= XP('route_x5_le11') =} |
| Normal EOs only | {= XP('route_n5_le10') =} | {= XP('route_n5_le11') =} |
| EOs of at most 4 of every kind | {= XP('route_x4_le10') =} | {= XP('route_x4_le11') =} |

A route in 9 or better exists on {= XP('route_x5_le9') =} of scrambles. **Computer only**: that's every EO of at most 5 ({= B4('NISS (normal, inverse, both)', 'all three axes', 5, 'mean_le') =} per scramble on average with NISS, {= B4('linear (normal)', 'all three axes', 5, 'mean_le') =} normal only), each with its best DR on both axes, which nobody writes out and solves in an hour. It says what's there to find. By hand, read the case each EO leaves on both DR axes and keep the EOs whose case has good odds (5.2).

**"Would you rather have 25 4 move eos or 200 5 move eos"** (Somebodyidk, [[D16056]]). On average (3.3), the number of DRs that short you'd get from each pile of EOs:

| EOs | DRs in ≤ 10 | DRs in ≤ 11 |
|---|---|---|
| 25 EOs of at most 4 | {= CELL('a3_yield', '≤ 10', 'Pairs from 25 EOs of ≤ 4') =} | {= CELL('a3_yield', '≤ 11', 'Pairs from 25 EOs of ≤ 4') =} |
| 200 EOs of exactly 5 | {= CELL('a3_yield', '≤ 10', 'Pairs from 200 EOs of exactly 5') =} | {= CELL('a3_yield', '≤ 11', 'Pairs from 200 EOs of exactly 5') =} |

So the 25 win for a DR in 10 and the 200 for a DR in 11: a 5-move EO gives about a tenth as many DRs in 10 as an EO of at most 4. The counts are of DRs that exist after each EO (its best DR on both axes), **computer only**; what carries to an attempt is the ratio, one 4-mover worth about ten 5-movers for a DR in 10. Here the two directions of a last turn are two EOs; counted the server's way, one EO for both, each EO of a pile stands for about two of these, both piles give about twice as many DRs, and the answer is the same.

**EO to DR with every option is 7, not 8** (5.1). Two DR axes, normal or inverse, and the EO's last turn either way, all keeping the EO. Each row is what you check after the EO; the columns are the mean turns to DR and how often it's short:

| Options checked | Mean, turns | DR in ≤ 6 | DR in ≤ 6, odds | DR in ≤ 7 |
|---|---|---|---|---|
| Every option | {= CT('allkept', 'mean') =} | {= CT('allkept', 'p_le6') =} | 1 in {= CT('allkept', 'one_in_le6') =} | {= CT('allkept', 'p_le7') =} |
| One axis alone | {= CT('plain', 'mean') =} ✓ | {= CT('plain', 'p_le6') =} | 1 in {= CT('plain', 'one_in_le6') =} ✓ | {= CT('plain', 'p_le7') =} |

(The every-option row is sampled.) The lengths are optimal DRs after the EO, the answer key. What you use in an attempt is the list of options to check after each EO, and the case on each DR axis, which you can read at the table and which gives the odds of each (5.2).

- **The other DR axis of the same EO is worth more than switching the EO's last turn**: exact, at most 6 on {= CT('two', 'p_le6') =} against {= CT('switch', 'p_le6') =} ✓, and about as much as checking the inverse ({= CT('ni', 'p_le6') =}). DanielEgdal set out to compute the two-axis numbers in 2023 and thought it "pretty much infeasible with any current idea I have" ([[T3329]]). FakeMMAP showed the state space is about $5\cdot 10^9$ ([[T3340]]), and DanielEgdal ran it until it stalled at $3\cdot 10^8$ ([[T3347]]). They're exact here (5.1).
- **Normal and inverse after an EO are related almost only through the case.** The DR lengths on the two sides correlate {= NI('all', 'correlation') =} over all states, and at most {= NIRANGE()[1] =} within a case. Once you know the case, the inverse is nearly a fresh draw (5.2).

**EO counts per scramble** (all three axes, counted the way nissy's `-a` lists them; nissy's default listing, the way counts are quoted on the server, keeps about half of the normal ones and two fifths of them with NISS; 4.1). Each row is the kind of EO counted; the last two columns are the share of scrambles with none that short:

| EOs counted | EOs of ≤ 4, mean | EOs of ≤ 4, median | Scrambles with no EO of ≤ 4 | Scrambles with no EO of ≤ 5 |
|---|---|---|---|---|
| Normal | {= B4('linear (normal)', 'all three axes', 4, 'mean_le') =} | {= B4('linear (normal)', 'all three axes', 4, 'median_le') =} | {= B4('linear (normal)', 'all three axes', 4, 'p_none_le') =} | {= B4('linear (normal)', 'all three axes', 5, 'p_none_le') =} |
| With inverse and NISS EOs | {= B4('NISS (normal, inverse, both)', 'all three axes', 4, 'mean_le') =} | {= B4('NISS (normal, inverse, both)', 'all three axes', 4, 'median_le') =} | {= B4('NISS (normal, inverse, both)', 'all three axes', 4, 'p_none_le') =} | {= B4('NISS (normal, inverse, both)', 'all three axes', 5, 'p_none_le') =} [d] |

**Shortest EO over three axes without NISS** (sampled, {= NSAMP('b') =} states; 4.1). Each row is a side rule; the last column is the share of states with an EO that short:

| EOs allowed | Mean, turns | EO in ≤ 3 |
|---|---|---|
| Linear | {= BOPT('any_axis_linear', 'mean') =} | {= BOPT('any_axis_linear', 'le3') =} |
| Normal or inverse | {= BOPT('any_axis_lin_or_inv', 'mean') =} | {= BOPT('any_axis_lin_or_inv', 'le3') =} |

**Bad edges you can count at the table** (so these are for the attempt; 4.2):

- **8 bad beats 6 for a short linear EO**: an EO in 4 or fewer on {= B5(8, 'p_linear_le4') =} ✓ against {= B5(6, 'p_linear_le4') =} ✓. With NISS 6 bad is a little better, {= B5(6, 'p_niss_le4') =} against {= B5(8, 'p_niss_le4') =}.
- **12 bad beats 10 with NISS**: in 5 or fewer on {= B5(12, 'p_niss_le5') =} against {= B5(10, 'p_niss_le5') =}.

**nissy 2.0.8's `scramble` isn't uniform, and DRs on the inverse of its scrambles come out shorter.** Its source draws the edge permutation as

```
ep = rand() % FACTORIAL12;   // the edge permutation of the drawn state
```

rand() gives {= NISSYBIAS('ratio') =} ✓ times $12!$ values, so the lowest {= NISSYBIAS('lowshare') =} ✓ of edge-permutation indices come up {= NISSYBIAS('more') =} ✓ more often than the rest. The inverse side is where the drawn state is, and that's where it shows, on {= n(X('n')) =} of its scrambles. Each row is one measure, on nissy's scrambles and on uniform ones:

| Measure | nissy's scrambles | Uniform states |
|---|---|---|
| Inverse, mean to DR (best of 3 axes) | {= A1('inv', 'mean', 'nissy') =} | {= A1('inv', 'mean') =} |
| Normal, the same (barely moved) | {= A1('lin', 'mean', 'nissy') =} | {= A1('lin', 'mean') =} |
| Best of six at most 8 | {= A1('six', 'p_le8', 'nissy') =} | {= A1('six', 'p_le8') =} |

The twisted-corner counts are off too ($\chi^2$ {= CHI('nissy', 'RL', 'twisted corners') =} and {= CHI('nissy', 'UD', 'twisted corners') =} on 7 degrees of freedom, p = {= CHIP('nissy', 'RL', 'twisted corners') =} and {= CHIP('nissy', 'UD', 'twisted corners') =}); I haven't found the cause. This study draws its own uniform states (appendix B).

**What it confirms or corrects**

**The known tables reproduce exactly.** Each row is an earlier table or count, the number it gave where it gave one, and the number here:

| Table | Their number | Here |
|---|---|---|
| Cale's and FakeMMAP's {= EODRT() =} EO-solved states | | mean {= CT('plain', 'mean') =} ✓ |
| torchlight's EO-breaking version (EO-breaking turns change almost nothing, as torchlight's table showed in 2023) | | {= CT('any', 'mean') =} |
| DougCube's one-axis DR from a scramble | | {= A1('fixed', 'mean') =} |
| DougCube's one-axis EO | | {= EO1() =} ✓ |
| Shota's shortest linear EO by bad-edge count | | the same table ✓ |
| Louis's one-axis DR shares | 6.2% and 43% | the same |
| Joba's exact NISS EO mean | 3.455 | {= BOPT('any_axis_niss', 'mean') =} on {= NSAMP('b') =} states, within sampling error |
| No EO of at most 4 even with NISS, on official scrambles: Cale ([[D2197]]) and wen ([[T5360]]) | about 4% | {= B4('NISS (normal, inverse, both)', 'all three axes', 4, 'p_none_le') =}, within sampling error |

- **The DR-4c4e numbers Tom Nelson quoted** ("1 in 5.2 normally, but 1 in 3.6 if you can switch the last move", [[D2200]]) are exact for EO-solved states: {= C6ONEIN('4c4e', 'plain_p_le6') =} ✓ and {= C6ONEIN('4c4e', 'switch_last_p_le6') =} ✓ for a DR in 6 or fewer. At that rate Lichi Fang's 3 of 27 has probability {= pc(BINOM(3, 27, float(E['c6']['4c4e']['switch_last_p_le6']))) =} ✓ ({= CALE_RZP('binom') =} at Cale's rate for switching the RZP's last move, which is what Lichi Fang switched), and Cale's 25 fit it. Both samples are the first 4c4e nissy online found, which needn't be like a 4c4e straight off an EO. Open (section 6).
- **Corrected:**
  - KrzychXyz's "~3%" of EO to DR cases at 10 is {= EODR(10) =} ✓ ({= EODRN(10) =} ✓ of {= EODRT() =} states; "10 is the worst" is right) [h].
  - Aneurin's later "Superflip takes 6 moves to solve EO with NISS": it takes 7 ✓, as Aneurin had first said [b].
  - Jay's "Similar efficiency to 4c4e and 4c2e in theory" for 6e4c (Jay's advice in the same breath was not to NISS for it): one axis, at most 6 on {= C6('4c6e', 'plain_p_le6') =} ✓ against {= C6('4c4e', 'plain_p_le6') =} ✓, as Cale's sheet had it and Cale told Jay in 2023 [j].
- **True as said**: the bad-edge facts (torchlight's exact counts, 6/6/4 and 6/6/8 above 6/6/6, no two axes more than 8 apart, at least 4 elsewhere when one axis has 12, 0 to 8 bad on the other axes after an EO), the EO odds for 10 and 12 bad edges, Emma's corner-twist odds, Zagros's 1 in 11 for 6+0, Cale's 1 in 22 for 4c6e, Zagros's 10% against 16% for 3c4e and 7c8e, wen's and Lichi Fang's EO counts per scramble (as Cale's sheet of official scrambles counts them), Jay's, Tom Nelson's and Rodney Kinney's take on normal against inverse once the case is known, and the rest of the claims table (section 6).
