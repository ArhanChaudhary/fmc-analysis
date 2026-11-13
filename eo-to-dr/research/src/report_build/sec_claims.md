## 6. The claims, checked

Statements the numbers can settle, by theme. Questions and guesses are in section 2, not here. Each verdict is one of **True**, **Corrected**, **Depends** (true under one reading or convention, not another), **Open** (the numbers here do not settle it) and **Withdrawn** (taken back at the time by whoever said it), and is no stronger than what was measured: scramble-level numbers are on {= n(X('n')) =} uniformly random scrambles, EO to DR numbers exact unless marked. Every correction has an example written out under the tables (letters in brackets).

**Scramble to DR.** One claim per row, who said it, and the verdict.

| Claim | Who | Verdict |
|---|---|---|
| "Only 6.2% of axes are 8 moves or less away from DR if you don't allow NISS"; "43% of scrambles being 9 moves or better away from DR" | Louis [[T5965]], [[T5959]] (restated for one axis, [[T5964]]) | **True**: exact, {= A1('fixed', 'p_le8') =} and {= A1('fixed', 'p_le9') =} on one fixed axis, linear. Over three axes and both sides it is {= A1('six', 'p_le8') =} and {= A1('six', 'p_le9') =} (3.1). |
| "5.9% of axes are 6 moves or fewer away from DR linearly if EO is solved (and you don't break it)" | Louis [[T5975]] | **True**: {= CT('plain', 'p_le6') =} ✓, exact. |
| "well sub-10 is not possible for superflip" | wen [[D20021]] | **True**: 10 on every axis, normal and inverse, and 10 with NISS [b]. |
| DR skip: "1 in 2^11 * 3^7 * 12! / 8! or something like that", a passing answer in a joke thread | bpaul [[D796]] | **Corrected**, lightly: the order of the four slice edges does not matter, so $12!/8!$ should be $12!/(8!\cdot 4!) = {= str(math.comb(12, 4)) =}$ ✓; 1 in {= COSETS() =} ✓ on a given axis, about 1 in {= COSETS3() =} ✓ on some axis [i]. |
| From 4 four-move and 45 five-move EOs with RZPs in 5: "If you NISS for all of them let's just count that as 20", "If you can find optimal DR every time, you can expect 4 DRs in 11 and 10 DRs in 12" | Tom Nelson [[T463]] | **Depends** on what is counted. Tom Nelson counted DRs through a few RZP types in 5, NISSed, found optimally ([[T525]]: "I just counted R, R U2 R and R U R"). Every route through those EOs on the normal side gives about {= f'{4 * A["a3_gains"]["normal_N11"]["drs_per_eo_le4"] + 45 * A["a3_gains"]["normal_N11"]["drs_per_5move_eo"]:.1f}' =} (EO, DR axis) pairs in 11 and {= f'{4 * A["a3_gains"]["normal_N12"]["drs_per_eo_le4"] + 45 * A["a3_gains"]["normal_N12"]["drs_per_5move_eo"]:.1f}' =} in 12 on average (3.3), and twice that, about {= f'{hu(2 * (4 * A["a3_gains"]["normal_N11"]["drs_per_eo_le4"] + 45 * A["a3_gains"]["normal_N11"]["drs_per_5move_eo"])):.0f}' =} and {= f'{hu(2 * (4 * A["a3_gains"]["normal_N12"]["drs_per_eo_le4"] + 45 * A["a3_gains"]["normal_N12"]["drs_per_5move_eo"])):.0f}' =}, if each of those EOs stands for both directions of its last turn, the way EOs are usually counted on the server (4.1). So Tom Nelson's figures are a lower bound on what exists, as Tom Nelson's own caveats say ([[T464]]). |
| "I see people checking ~50 EOs, so finding 6 DRs with <= 11 moves sounds realistic" | Rodney Kinney [[T461]] | **Depends** on the EOs: 50 EOs of 5 turns give about {= f'{50 * A["a3_gains"]["normal_N11"]["drs_per_5move_eo"]:.1f}' =} routes in 11 on average, {= f'{hu(100 * A["a3_gains"]["normal_N11"]["drs_per_5move_eo"], 1):.1f}' =} if each stands for both directions of its last turn (the way EOs are usually counted on the server, 4.1); 50 of at most 4 about {= f'{50 * A["a3_gains"]["normal_N11"]["drs_per_eo_le4"]:.0f}' =}, or {= f'{hu(100 * A["a3_gains"]["normal_N11"]["drs_per_eo_le4"]):.0f}' =} (3.3). What exists, not what is found. |
| "150 4e4c's in 5 is ~7 10 move DRs and 1 9 move DR" | Tom Nelson [[D3167]] | **True** as arithmetic on the exact table: an RZP in 5 then a DR in 5 or fewer is 150 × {= pc(CASELE(4, 4, 5)) =} ✓ = {= f'{hu(CASELE(4, 4, 5), 1, 150):.1f}' =} ✓, in 4 or fewer 150 × {= pc(CASELE(4, 4, 4)) =} ✓ = {= f'{hu(CASELE(4, 4, 4), 1, 150):.1f}' =} ✓ (4c4e straight off an EO, one axis, EO kept). zakimoshi's caveat ([[D3170]], "This kinda implies that everything is unrelated to each other") stands: RZPs of one scramble are not independent, and RZPs are not covered here (section 7). |
| One of 300 EOs gives a DR in 5 or less "92.71%" (binomial, `1 - (1 - p)^300`, from the one-axis table) | DougCube [[T9951]] | **Open**: the arithmetic is right ✓, for one DR axis per EO (JTuu, [[T9960]]: "oh, it's only UD dr"; DougCube, [[T9963]]: "oh sorry, I forgot to stipulate that"). DougCube flagged the assumption ([[T9953]]: "assuming each of the EOs are statistically independent of each other"; [[T9956]]: "tho, I think that by limiting to 5-move or less EO, then it becomes coupled and are not independent"; [[T9957]]: "if instead, it's any length EO, then I think these computations should hold very well"). How dependent the EOs of one scramble are for EO to DR alone is not measured here; for whole routes, see 3.3. |

**EO to DR.** One claim per row, who said it, and the verdict.

| Claim | Who | Verdict |
|---|---|---|
| The EO to DR counts 1, 2, 17, …, 3114 ("not allowing EO-breaking moves") | FakeMMAP [[T2598]]; DougCube [[T9941]] | **True**, reproduced exactly. |
| EO to DR with EO-breaking turns: "allows breaking EO" | torchlight [[T2600]] | **True**: mean {= CT('any', 'mean') =} against {= CT('plain', 'mean') =}, exact. |
| "Last sheet of DRM/ARM doc has a distribution. 10 is the worst (~3% of all cases)" | KrzychXyz [[D14031]] | **Corrected**: 10 is the worst, as KrzychXyz says, but {= EODRN(10) =} ✓ of the {= EODRT() =} EO-solved states need it, {= EODR(10) =} ✓: ten times less than said. One such EO in [h]. |
| "like how DR-4e4c in 6 moves is 1 in 5.2 normally, but 1 in 3.6 if you can switch the last move" | Tom Nelson [[D2200]] | **True** for at most 6: {= C6ONEIN('4c4e', 'plain_p_le6') =} ✓ and {= C6ONEIN('4c4e', 'switch_last_p_le6') =} ✓ (the EO's last turn). |
| Asking "Has anyone ever tried to verify the DR setup stats (switching last move)?": "only 3 out of this 27 DR-4e4c can be reduced to DR in 6 moves or less (accounting for switching the last move)", then "Is there anything obvious that I missed?" | Lichi Fang [[T4233]] | **Open**. The exact rate for a 4c4e straight off an EO, last EO turn either way, is {= pc(E['c6']['4c4e']['switch_last_p_le6']) =} ✓; 3 or fewer of 27 has probability {= pc(BINOM(3, 27, float(E['c6']['4c4e']['switch_last_p_le6']))) =} ✓ under it (compLex: "only a 3.2% chance of those test results", [[T4234]]), and Cale's 25 fit it (next row). Both samples are the first 4c4e nissy online found, after an RZP, which need not be like a uniform EO-solved state (torchlight, [[T4250]]: "if the EO isn't already 4c4e, it means that the 4c4e case you get from RZP is 1 move away from something that is not 4c4e"). Lichi Fang switched the RZP's last move, not the EO's, and guessed that was it ("Or maybe switching the last move of rzp is much worse than switching the last move of eo?"); Cale's table for the RZP's last move ([[T4264]]) gives {= CALE_RZP('p') =}, and 3 or fewer of 27 is then {= CALE_RZP('binom') =}, so that doesn't explain it either. RZPs are not covered here. |
| Re-test, first 4c4e found on 25 scrambles: "The optimals were 6 moves for 24%, 7 moves for 56%, and 8 moves for 20%" | Cale [[T4264]] | **True** within its sample: the exact shares for a 4c4e with the EO's last turn either way are {= pc(CASELE(4, 4, 5, 'eo_switchF')) =} ✓ in 5 or fewer, {= pc(CASELE(4, 4, 6, 'eo_switchF') - CASELE(4, 4, 5, 'eo_switchF')) =} ✓ in 6, {= pc(CASELE(4, 4, 7, 'eo_switchF') - CASELE(4, 4, 6, 'eo_switchF')) =} ✓ in 7, {= pc(CASELE(4, 4, 8, 'eo_switchF') - CASELE(4, 4, 7, 'eo_switchF')) =} ✓ in 8 and {= pc(1 - CASELE(4, 4, 8, 'eo_switchF')) =} ✓ in 9; on 25 a share has a standard error of about 9 points. |
| "'dr setup sheet' shows that 4c4e pops up 1 in 15.3 eo"; "so 4e4c is about 1/15" | Mike [[T3314]]; Andrew [[D350]] | **True**: {= C6ONEIN('4c4e', 'share') =} ✓ on one given DR axis. With two DR axes per EO, about twice as often on one of them. |
| "~5.12% chance of 3 misoriented and ~19.20% chance of 4 misoriented" | Emma [[T1726]] | **True**, exact: {= TWIST(3) =} ✓ and {= TWIST(4) =} ✓ of the {= TWIST_ALL() =} corner orientations. |
| "Shouldn't it be 1/11 chance of 6/0" (of 6-twist cases) | Zagros [[D13190]] | **True**: {= TWIST6SAME() =} ✓ of the {= TWIST(6) =} ✓ orientations with six twisted corners. wen's "50/50?" ([[D13169]]) was a guess. |
| "i think DR-5c6e is actually tied for the most common DRM you can get after any random EO"; "6c (including both 6+0 and 3+3) is a bit more common than 5c", "edit: 3+3 is tied with 5c" | Jay [[D10053]]; torchlight [[D10057]] | **True**, both: 5c6e and 6c6e with 3+3 corners are tied in Cale's split; 6c6e as a whole is the most common case ({= C6('6c6e', 'share') =} ✓ against {= C6('5c6e', 'share') =} ✓). |
| 4c6e: "even with full moveset sub-7 is 1 in 22" | Cale [[T1805]] | **True**: {= C6ONEIN('4c6e', 'plain_p_le6') =} ✓ for at most 6 (one axis, EO kept). |
| DR-6e4c: "Similar efficiency to 4c4e and 4c2e in theory but many of the optimal solutions aren't findable with just setups to R U2 L" | Jay [[D584]], again [[T1802]] | **Corrected** for the optimum too, by Cale when Jay said it again in 2023 ([[T1805]]): at most 6 on {= C6('4c6e', 'plain_p_le6') =} ✓ of 4c6e against {= C6('4c4e', 'plain_p_le6') =} ✓ for 4c4e and {= C6('4c2e', 'plain_p_le6') =} ✓ for 4c2e; means {= C6('4c6e', 'plain_mean') =} ✓, {= C6('4c4e', 'plain_mean') =} ✓, {= C6('4c2e', 'plain_mean') =} ✓. Jay agreed ("hm, i guess it's a bit more worse than 4c2e than i thought", [[T1806]]), and Jay's advice the same day, "I wouldn't really NISS for it" ([[D585]]), stands [j]. |
| "It's 10% sub7 vs 78 being 16%" (3c4e against 7c8e); "3c4e (10.1% sub-7)" | Zagros [[D18971]]; Fanti [[D15179]] | **True**: at most 6 on {= '%.2f%%' % hu(E['c6']['3c4e']['plain_p_le6'], 2, 100) =} ✓ for 3c4e with the EO kept (Fanti's 10.1% allows any turn, F/B quarter turns included, and that count gives 10.08%) and {= C6('7c8e', 'plain_p_le6') =} ✓. |
| 3c6e: "it’s 1/7 for 7 moves instead of 1/3 for 4e4c, 8c8e, 8e7c, 2e4c etc" | Noah Swor [[D6979]] | **Depends** on what "7 moves" means, and the message was about switching from a 3c6e RZP (mrauo, [[D6977]]: "Is it worth to switch from 3c6e rzp in 5?"), while these numbers are for EO-solved states, a different population. The 1/3 figures fit a DR in 6 or fewer on normal or inverse, which is what switching gives (4c4e {= C6('4c4e', 'normal_or_inverse_p_le6') =}, 4c2e {= C6('4c2e', 'normal_or_inverse_p_le6') =}, 7c8e {= C6('7c8e', 'normal_or_inverse_p_le6') =}, 8c8e {= C6('8c8e', 'normal_or_inverse_p_le6') =}), and nearly as well with the EO's last turn either way ({= C6ONEIN('4c4e', 'switch_last_p_le6') =} ✓, {= C6ONEIN('4c2e', 'switch_last_p_le6')[5:] =}, {= C6ONEIN('7c8e', 'switch_last_p_le6')[5:] =} ✓ and {= C6ONEIN('8c8e', 'switch_last_p_le6')[5:] =}). 3c6e is then {= C6('3c6e', 'normal_or_inverse_p_le6') =} ({= C6ONEIN('3c6e', 'normal_or_inverse_p_le6') =}) or {= C6ONEIN('3c6e', 'switch_last_p_le6') =} ✓; with neither it is {= C6ONEIN('3c6e', 'plain_p_le6') =} ✓ in 6 and {= C6ONEIN('3c6e', 'plain_p_le7') =} ✓ in 7. So 3c6e is well behind those four on every reading, as Noah Swor says; the 1 in 7 isn't reproduced. |
| RZP to DR on normal and inverse: "i'm certain there's zero correlation"; "it's the opposite for rzp to DR because if it's bad then it's more likely to be better after switching"; "Regression to the mean" | Jay [[D848]]; Tom Nelson [[D847]], [[D850]]; Rodney Kinney [[D851]] | **True** for a known case, which is what an RZP is: within a case the two sides' DR lengths have correlation between {= NIRANGE()[0] =} and {= NIRANGE()[1] =}, and under {= SWCORR() =} either way for the cases people switch from ({= ', '.join(f"{c} {NI(c, 'correlation')}" for c in SWITCHED) =}). Tom Nelson meant the same ([[D850]]: "yeah that's what I mean. If it's 8 moves on normal then it's more likely to be better on inverse because any random case is probably sub-8"). Over all EO-solved states, case not known, it is {= NI('all', 'correlation') =}, almost all of it from the case (5.2). Measured for EO-solved states, not RZPs. |

**Scramble to EO.** One claim per row, who said it, and the verdict.

| Claim | Who | Verdict |
|---|---|---|
| EO skip: "also 1/2048 for fixed axis", "103741/70963200 for any axis"; "9335 (~0.1458%, 1 in 686) had solved EO already" on 6,406,775 scrambles | torchlight [[D3530]]; Minkowski [[D3289]] | **True**: exact ${= LAY('states_some_axis_eo_solved') =}/70963200$ ✓; Minkowski's sample is within its error. |
| The sum of bad edges over the three axes peaks at 18: "18    16978144    23.925280%" | torchlight [[T8139]] | **True**, exact. |
| "13.907% that's sort of lucky I guess" (all three axes with 0, 2, 4 or 8 bad) | jisu101 [[D20495]] | **True**: {= LAY('p_all_axes_in_0_2_4_8') =} ✓. |
| "6/6/4 or 6/6/8 is more likely than 6/6/6"; "6/6/6 is more common than 4 on UD / 6 on LR / 6 on FB" | Yura Riabov [[T4163]]; torchlight [[D3303]] | **True**, sorted and ordered: {= LAY('sorted_6/6/4') =} and {= LAY('sorted_6/6/6') =} sorted; {= LAY('ordered_6/6/4') =} and {= LAY('ordered_6/6/6') =} ordered. |
| "no 2 axes can differ by more than 8"; 10/10/2 "managed to set it up"; "12 bad one one axis means the other two axises will have to have at least 4 bad edges."; "after eo you could have anywhere from 0-8 bad edges on the other 2 axis, but never 10 or 12" | wen [[D816]], [[D817]]; Aneurin [[D1289]]; Jay [[T1831]] | **True**, exact. |
| "for example 2/10/10 is much rarer than what you would expect with a simple calculation" | wen [[D19913]] | **True**: {= RATIO_2_10_10() =} times rarer than with independent axes. |
| A linear EO for 12 bad is 7 (wen); for 10 bad no 5-mover (Jay: "nope"), "10 bad is always 6 or 7"; "TIL that some 10 bad are 7 optimal for linear eo huh"; "2 cases. Both the ones where good edges are both on F." | wen [[T7104]]; Jay [[T6816]], [[T6817]]; Zagros [[D10207]]; KrzychXyz [[T9408]] | **True**: {= B5H(10, 7) =} ✓ of the {= B5N(10) =} ten-bad states of one axis need 7 (two cases up to symmetry), the rest 6; twelve bad needs 7 ✓. |
| "i think youre more likely to get a 4 move eo from 8 than 6"; "maybe im weird i think 8 is lowk worse than 6" | wen [[D20492]]; kyh [[D20491]] | **Depends**: linearly wen is right ({= B5(8, 'p_linear_le4') =} ✓ against {= B5(6, 'p_linear_le4') =} ✓ for at most 4); with NISS 6 bad is a little better ({= B5(6, 'p_niss_le4') =} against {= B5(8, 'p_niss_le4') =}). |
| 10 bad, NISS EO in at most 5: "68%, not bad", "Number goes up to 90% if we factor in starting from inverse, once again assuming that the inverse case is independent of the normal case" | wen [[T562]], [[T563]], [[T564]] | **Depends** on the independence wen assumed and said doesn't hold ([[T563]]: "ofc using the assumption that the various possible nisses from a given case are independent of each other (which they arent)"): with every NISS EO (normal, inverse or both sides), which is what the 90% counts, it is {= B5(10, 'p_niss_le5') =}. |
| "On average, eo can be solved in 3.455 moves."; fixed axis 4.609 | Joba [[T9374]]; DougCube [[T9582]] | **True**: {= BOPT('any_axis_niss', 'mean') =} on the sample; {= EO1() =} ✓ exact. DougCube withdrew the comparison of the two ([[T9587]]), since one has NISS and the other not; with three axes and no NISS it is {= BOPT('any_axis_linear', 'mean') =}. |
| God's number for EO: "7"; "yeah 7 with superflip" | Noah Swor [[D6019]]; alkamaass [[D6020]] | **True**, with or without NISS (Joba's table; the superflip [b]). |
| Superflip: "EO is 7 moves", "Even with niss" | Aneurin [[D174]], [[D175]] | **True** [b]. |
| "Superflip takes 6 moves to solve EO with NISS" | Aneurin [[D1281]] | **Corrected**: 7 [b]. Aneurin's first statement was right. |
| More 3-move than 4-move EOs: "so the chance is 0" | Kai Cui [[T5752]] | **Withdrawn** at the time: kalindumaxxer answered "i literally got one" ([[T5753]]), Kai Cui "oh bruh" ([[T5754]]) and, after Yura Riabov's `U (R2 U)` ([[T5758]]), "nvm then" ([[T5760]]) and "probably quite rare" ([[T5764]]). Counting every EO (nissy `-a`), it happens on {= MORE3('niss') =} of scrambles with NISS, never linearly in the sample [e]. kalindumaxxer asked "exluding htr equivalent variants" ([[T5750]]); that convention is not counted here. |
| "I remember something like 200ish <=5 movers and 17 <=4 movers"; "the median for 4 or less is more like 14" | wen [[T4633]]; Lichi Fang [[T4636]] | **True** as Cale's sheet of official scrambles counts them (NISS, all axes, nissy's default listing): "mean = 246", "median = 217" of at most 5, "mean: 17.3", "median: 14" of at most 4. On the first {= DL['scrambles'] =} uniform scrambles here, nissy's default NISS listing gives a mean of {= DLPER(5, 'mean') =} and a median of {= DLPER(5, 'median') =} of at most 5, {= DLPER(4, 'mean') =} and {= DLPER(4, 'median') =} of at most 4. Counting every EO (nissy `-a`, both directions of each last turn) gives more: normal only, {= B4('linear (normal)', 'all three axes', 5, 'mean_le') =} of at most 5 and {= B4('linear (normal)', 'all three axes', 4, 'mean_le') =} of at most 4 (median {= B4('linear (normal)', 'all three axes', 4, 'median_le') =}); with inverse and NISS EOs {= B4('NISS (normal, inverse, both)', 'all three axes', 5, 'mean_le') =} and {= B4('NISS (normal, inverse, both)', 'all three axes', 4, 'mean_le') =} (median {= B4('NISS (normal, inverse, both)', 'all three axes', 4, 'median_le') =}). Of EOs that differ only in the directions of their last turns the default listing keeps one; on those scrambles that is {= DLP(5, 'one_sided') =} of the one-sided EOs of at most 5 and {= DLP(5, 'two_sided') =} of the two-sided ones, {= DLP(5, 'niss') =} in all, about two fifths (4.1). |
| "virtually all scrambles have some EO in 5" | Lewis Isom [[D6036]] | **True**: none of at most 5 on {= B4('linear (normal)', 'all three axes', 5, 'p_none_le') =} linearly, {= B4('NISS (normal, inverse, both)', 'all three axes', 5, 'p_none_le') =} with NISS [d]. |
| 12 bad on one axis: "1 in 2048"; 10 bad: "About 3% it seems", "close to 10% on a real scramble" | Aneurin [[D1295]]; wen [[T5364]], [[T5370]] | **True**: exact $1/2048$; {= B5P(10) =} on one axis, {= LAYP(lambda t: 10 in t) =} on some axis. |

The examples. Every move sequence here was replayed on the sticker model (appendix B).

**[a] No DR under 10, even with NISS.** The best DR on any axis, normal or inverse, is 10, and with NISS it's still {= WIT('W1', 'solution', 'length') =}. The scramble is {= WXX('X3', 0, 'optimal_length') =} moves optimal.

```
{= SCR('W1') =}  // scramble
{= WIT('W1', 'solution', 'normal') =}  // best DR with NISS (DR on R/L)
{= WXX('X3', 0, 'optimal_solution') =}  // an optimal solution
```

A scramble with no sub-10 DR on its six linear tries that NISS gets under, {= WIT('W2', 'solution', 'length') =} turns to DR on U/D:

```
{= SCR('W2') =}  // scramble
{= WIT('W2', 'solution', 'normal') =} ({= WIT('W2', 'solution', 'inverse') =})  // NISS DR on U/D
```

**[b] The superflip.** DR in 10 on each axis, normal and inverse, and 10 with NISS. No DR solution of 9 or fewer exists on the normal side; there are {= n(WIT('W3', 'dr_solutions_normal_by_length', '10')) =} of 10. Its shortest EO is 7 turns ✓ on every axis, also with NISS (the search of section 4 over every NISS split, and a short proof whose two facts Lean checks: the superflip commutes with every turn, so a NISS EO of it is a linear EO of the same length, and that linear EO needs 7).

```
{= SCR('W3') =}  // scramble
{= WIT('W3', 'solution', 'optimal_dr') =}  // e.g. a DR on R/L
```

**[c] The optimal DR needs a long EO.** On the first scramble the optimal DR is 8 (U/D), and the shortest EO inside any optimal DR is 7 turns on F/B. Through a normal EO of at most 5 the best is {= WIT('W5', 'solution', 'best_route_eo_le5', 'total') =}.

```
{= SCR('W5') =}  // scramble
{= WIT('W5', 'solution', 'optimal_dr', 'moves') =}  // optimal DR (U/D)
{= WIT('W5', 'solution', 'best_route_eo_le5', 'eo') =}  // best route through a short EO: EO on R/L
{= WIT('W5', 'solution', 'best_route_eo_le5', 'dr') =}  // then DR on F/B
```

On the second, both optimal DRs (10 turns) start with an EO of 9:

```
{= SCR('W4') =}  // scramble
{= WIT('W4', 'solution', 'optimal_dr') =}  // one of them
```

**[d] No EO in 5 at all.** No EO of at most 5 turns on any axis, normal, inverse or NISS (nissy `solve eo -N -a -M 5` lists none). An optimal NISS EO is 6.

```
{= SCR('W7') =}  // scramble
{= WIT('W7', 'solution', 'an optimal NISS EO (nissy eo -N)') =}  // optimal NISS EO
```

**[e] More 3-move EOs than 4-move EOs.** Four 3-move EOs and no 4-move EO on any axis, normal, inverse or NISS.

```
{= SCR('W8') =}  // scramble
R (U2 R)
R (U2 R')
R' (U2 R)
R' (U2 R')       // the four short EOs
```

**[f] An EO-breaking turn helps, rarely.** The EO ({= WXX('X6', 'eo_axis') =}) is the only EO solved and leaves {= WXX('X6', 'case') =} for DR on {= WXX('X6', 'dr_axis') =}: {= WXX('X6', 'keep') =} keeping the EO, {= WXX('X6', 'any') =} breaking it.

```
{= SCR('X6') =}  // scramble
{= WXX('X6', 'eo') =}  // EO ({= WXX('X6', 'eo_axis') =}), the only EO solved
{= WXX('X6', 'dr_keeping_eo') =}  // DR keeping the EO
{= WXX('X6', 'dr_breaking_eo') =}  // DR breaking it
```

**[g] The other options after an EO.**

The inverse. The EO (U/D) leaves 4c6e for DR on F/B, 9 on normal, 5 on the inverse:

```
{= SCR('W10') =}  // scramble
{= WIT('W10', 'solution', 'eo') =}  // EO
{= WIT('W10', 'solution', 'written_niss') =}  // EO, then DR on the inverse
```

The other axis. The EO (F/B) is 9 to DR on R/L but 5 on U/D:

```
{= SCR('W11') =}  // scramble
{= WIT('W11', 'solution', 'eo') =}  // EO
{= WIT('W11', 'solution', 'UD') =}  // DR on U/D
```

The last turn. The EO (U/D) leaves 4c4e for R/L, 6 to DR; with the last turn switched it's 5:

```
{= SCR('W9') =}  // scramble
{= WIT('W9', 'solution', 'eo') =}  // EO
{= WIT('W9', 'solution', 'dr') =}  // DR
{= WIT('W9', 'solution', 'eo_switched') =}  // EO, last turn switched
{= WIT('W9', 'solution', 'dr_after_switch') =}  // DR after it
```

**[h] An EO 10 from DR.** The EO (R/L) leaves {= WXX('X1', 'case') =} for DR on F/B, and the shortest DR keeping the EO is 10. Only {= EODR(10) =} of EO-solved states are this far. On the inverse this one is {= WXX('X1', 'inverse') =}.

```
{= SCR('X1') =}  // scramble
{= WXX('X1', 'eo') =}  // EO
{= WXX('X1', 'plain_dr') =}  // shortest DR keeping the EO
{= WXX('X1', 'eo') =} ({= WXX('X1', 'inverse_dr') =})  // EO, then DR on the inverse
```

**[i] Why the DR-skip count divides by 4!.** This position is in DR on U/D, with the four E-slice edges moved among themselves:

```
{= WXX('X2', 'scramble') =}  // scramble
```

Every order of the four slice edges in the slice is the same DR, so the placements count as $\binom{12}{4} = {= str(math.comb(12, 4)) =}$, not $12!/8!$ = {= n(math.perm(12, 4)) =}. The cosets of DR on one axis number $2^{11}\cdot 3^7\cdot {= str(math.comb(12, 4)) =}$ = {= COSETS() =}, the denominator of DougCube's "Going to DR" tab.

**[j] A 4c6e after an EO.** The EO ({= WXX('X4', 'eo_axis') =}) leaves 4c6e for DR on {= WXX('X4', 'dr_axis') =}; the shortest DR keeping the EO is {= WXX('X4', 'plain') =}, the most common length for 4c6e.

```
{= SCR('X4') =}  // scramble
{= WXX('X4', 'eo') =}  // EO
{= WXX('X4', 'plain_dr') =}  // shortest DR keeping the EO
```

One case shows nothing about averages: the averages are in Jay's DR-6e4c row of the claims table above and in appendix A ({= C6('4c6e', 'plain_mean') =} for 4c6e against {= C6('4c4e', 'plain_mean') =} for 4c4e).
