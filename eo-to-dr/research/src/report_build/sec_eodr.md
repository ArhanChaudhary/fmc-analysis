## 5. EO to DR

From an EO-solved state, how many turns to DR. With one DR axis, turns that keep the EO, linear, this is Cale's table ([*DR setup stats*](https://docs.google.com/spreadsheets/d/11bTZ4Y7_6qKlIWo4a4TLW45M2ZkctQZAVxgQqEtlUs0)), FakeMMAP's counts ([[T2598]]), the last tab of Louis's [*DRM/ARM average optimals*](https://docs.google.com/spreadsheets/d/13fSwUROzP0hZQV1Cn96GndWbPy4UrsHiYTaWFSeWtJs) and DougCube's [*Tables of Distinct Positions*](https://docs.google.com/spreadsheets/d/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo), all the same {= EODRT() =} states; torchlight's table allows EO-breaking turns ([[T2600]]). Here I put the options you actually have next to it: the other DR axis of the same EO, the inverse, the EO's last turn the other way, and EO-breaking turns, alone and together.

How it's set up:

- **Weighting.** After an EO chosen as a function of the edge orientation alone, the state is uniform over the EO-solved states, so every one of the 1,082,565 (corner orientation, E-slice placement) cosets is equally likely. Cale's and Louis's tables assume the same. It doesn't hold exactly for NISS EOs (which ones exist depends on the edge permutation too), for EOs chosen by looking at the case they leave, or for the states after an RZP.
- *Last EO turn the other way*: the EO ends in a quarter turn of its axis (say `F`); the alternative is the same EO with `F'`, which is the state times `F2`.
- *Normal or inverse*: the same EO, then the DR found on the inverse of the post-EO state, written `EO (DR)`.
- **Exact and sampled.** The exact rows are over all 1,082,565 states (for the better of two axes: over all corner states times all placements of the E- and M-slice pieces). The sampled ones are 10,000,000 uniform EO-solved states with exact lookups, so a share is good to ±0.02 points.

### 5.1 The typical EO to DR, with each option

Each row is what you allow after the EO; the *DR in ≤* columns are the share of EO-solved states with a DR that short, and the last column is the same for 6 as odds.

{{c7}}

Zagros asked ([[D12300]]): "What is typical eo->dr? … Is 7 moves from eo to dr typical? Or is 8 optimal common". Louis answered with the distribution ("That's the optimal distribution for EO to DR", [[D12306]]) and Zagros read it as "So it is 8 then typically" ([[D12307]]), adding "But I suppose this probably doesnt account for all the different ways you can rzp->switch" ([[D12308]]). The first row is that distribution, for EO-solved states (Zagros's sub-7 is after an RZP, a different population). The rest of the table is what the ways to switch are worth:

- **The other DR axis** of the same EO is worth more than switching the EO's last turn: at most 6 on {= CT('two', 'p_le6') =} of EOs against {= CT('switch', 'p_le6') =} ✓, mean {= CT('two', 'mean') =} against {= CT('switch', 'mean') =} ✓. Checking the inverse is worth about the same as the other axis ({= CT('ni', 'p_le6') =}).
- **All of the EO-keeping options together** (two axes, normal or inverse, last turn either way): mean {= CT('allkept', 'mean') =}, at most 6 on {= CT('allkept', 'p_le6') =} (1 in {= CT('allkept', 'one_in_le6') =}, against 1 in {= CT('plain', 'one_in_le6') =} ✓ for one axis), at most 7 on {= CT('allkept', 'p_le7') =}. So once you use every option, the typical EO is 7 from DR, not 8.
- **EO-breaking turns change almost nothing** (exact; torchlight's table). On top of all the EO-keeping options they add {= f3(float(CT('allkept', 'mean')) - float(CT('all', 'mean'))) =} turns on average [f]. Of the {= BOTH('states_shorter_with_any_turns') =} EO-solved states where any turns are shorter, {= BOTH('all_0e_cases', 'shorter_with_any_turns') =} have no edge out of place; then the other EO is solved too, and a DR as short keeps it. One axis, with and without them:

| Turns after the EO | Mean, turns | DR in ≤ 6 |
|---|---|---|
| Keeping the EO | {= CT('plain', 'mean') =} ✓ | {= pc(E['c7'][C7N['plain']]['p_le6'], 2, rounded=True) =} |
| Any turns | {= CT('any', 'mean') =} | {= pc(E['c7'][C7N['any']]['p_le6'], 2, rounded=True) =} |

The lengths are optimal DRs after the EO: an answer key for what's there, not what you find by hand on every EO. What carries to an attempt is the list of options and their order: after an EO, look at the other DR axis and at the inverse as well as the one you set out for, and try the last turn the other way. The case on each axis says how likely each one is to give something short (5.2).

An example of each, the EOs written out with the scrambles in [g] and [f]:

```
D2 L2 B' D    // the inverse: then 9 on the normal side, 5 on the inverse
F' B' U' F'   // the other axis: 9 on R/L, 5 on U/D
R' D2 L' D    // the switch: 6, and 5 with D'
```

And an EO-breaking turn, after an EO ({= WXX('X6', 'eo_axis') =}) that is the only EO solved: {= WXX('X6', 'keep') =} keeping the EO, {= WXX('X6', 'any') =} breaking it.

### 5.2 By case

The case after the EO, on the DR axis you're looking at, in the server's naming: bad corners, then edges out of place for that DR (slice edges outside the slice and as many others inside it), with 6c and 8c not split into 3+3 and 6+0 (Cale's sheet splits them). Below are the 16 most common cases. The share of EOs and the mean are exact; the other columns are the chance of a DR of at most 6 with each option (exact for one axis, the switch and the better of two axes; sampled, 10,000,000 states, for the inverse and all together). Each row is a case; the *DR in ≤ 6* columns are the chance with each option:

{{c6_case}}

This table is for the attempt: the case is what you read at the table (twisted corners and edges out of place on each DR axis), and the row says how likely a DR in 6 or fewer is with each option. The DR lengths behind it are optimal, so treat the odds as what is there to find. All 40 cases but 0c0e (already a DR) with the mean and the odds of each option are in appendix A. The better of two axes is read by the case on the first one, so it mixes every case the second axis can have.

**Normal and inverse.** Java asked trig0n whether the rule not to switch when there's nothing on normal holds for RZP to DR ([[D844]]: "does this apply to RZP -> DR and HTR subsets?"). Tom Nelson: "it's the opposite for rzp to DR because if it's bad then it's more likely to be better after switching" ([[D847]]); Jay: "i'm certain there's zero correlation" ([[D848]]); Tom Nelson: "yeah that's what I mean. If it's 8 moves on normal then it's more likely to be better on inverse because any random case is probably sub-8" ([[D850]]); Rodney Kinney: "Regression to the mean" ([[D851]]).

Over all EO-solved states, the DR lengths on normal and on the inverse (same axis, EO kept) have correlation {= NI('all', 'correlation') =}: a bad normal side does make a bad inverse a little more likely. Almost all of that is the case. The inverse of a position has the same case on the same axis (as many twisted corners, as many slice edges out of the slice), and within one case the correlation is between {= NIRANGE()[0] =} and {= NIRANGE()[1] =} in each of the {= NIRANGE()[2] =} cases with 1,000 or more samples (appendix A). Small, but not zero: the largest ({= NI('8c2e', 'correlation') =} for 8c2e, {= NI('6c8e', 'correlation') =} for 6c8e, {= NI('6c6e', 'correlation') =} for 6c6e) are in cases that lump together sub-cases the inversion keeps (6c is 3+3 or 6+0, 8c is 4+4 or 7+1).

So they are right once the case is known, as it is after an RZP: the inverse is close to a fresh draw from that case (Jay), and a long normal side is no reason to expect a long inverse, so switching after a bad one pays (Tom Nelson and Rodney Kinney). The chance the inverse is at most 6, given the normal side's length (same axis, EO kept):

| Normal side, turns | Inverse DR in ≤ 6 |
|---|---|
| 9 | {= NI('all', 'p_inv_le6_given_normal_9') =} |
| 6 | {= NI('all', 'p_inv_le6_given_normal_6') =} |
| Any (overall) | {= NI('all', 'p_inv_le6') =} |
