# EO to DR, and scramble to DR: corrections

*Goes with the write-up on EO to DR and scramble to DR, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion).

**What everything below is measured against:**

- **Exact distance tables**: the fewest turns to DR from every coset of the DR group ({= COSETS() =} per axis), with any turns and with turns that keep an EO, and every EO distance.
- **EO to DR**: every one of the {= EODRT() =} EO-solved states on a DR axis, exactly.
- **{= n(X('n')) =} uniformly random scrambles**, each searched exactly: every DR axis, normal, inverse and NISS, every EO of up to 6 turns.

Every scramble and move sequence below was replayed on a sticker-level cube.

These are the statements the numbers go against, each with the numbers that settle it and an example. Most of what was said holds up; that's in the write-up's section 6, the claims checked one by one.

---

**1. "Last sheet of DRM/ARM doc has a distribution. 10 is the worst (~3% of all cases)"** (KrzychXyz, [[D14031]], answering zakimoshi's "What's the longest DR case after eo", [[D14026]]).
10 is the worst, as KrzychXyz says, but the share is wrong: on the sheet, and exactly, {= EODRN(10) =} of the {= EODRT() =} EO-solved states need 10 turns to DR (one DR axis, EO kept, linear), which is {= EODR(10) =}, ten times less. zakimoshi's follow-up "Wait so only 6.3% of all cases are sub 7able?" ([[D14033]]) was a question; the exact share is {= CT('plain', 'p_le6') =}.
For illustration, one of those states. The EO leaves {= WXX('X1', 'case') =} for DR on F/B, and the shortest DR that keeps the EO is 10:

```
{= SCR('X1') =}  // scramble
{= WXX('X1', 'eo') =}  // EO on R/L
{= WXX('X1', 'plain_dr') =}  // shortest DR keeping the EO
```

**2. "Superflip takes 6 moves to solve EO with NISS"** (Aneurin, [[D1281]]).
It takes 7, on every axis, with or without NISS; every NISS split was searched. Aneurin had it right the first time ([[D174]], [[D175]]): "EO is 7 moves", "Even with niss".
Example: the superflip, with a 7-move NISS EO on it from alkamaass ([[D6033]]); none of 6 exists.

```
{= SCR('W3') =}  // the superflip
{= WXX('X5', 'normal') =} ({= WXX('X5', 'inverse') =})  // EO on U/D
```

**3. DR-6e4c: "Similar efficiency to 4c4e and 4c2e in theory but many of the optimal solutions aren't findable with just setups to R U2 L"** (Jay, [[D584]], answering jellobean's "How good would you say … the Dr-6e4c case", [[D583]]).
The optimal DR alone already differs. Over all EO-solved states, one axis, EO kept; each row is a case:

| Case | DR in ≤ 6 | Mean, turns |
|---|---|---|
| 4c6e (Cale's 6e4c) | {= C6('4c6e', 'plain_p_le6') =} | {= C6('4c6e', 'plain_mean') =} |
| 4c4e | {= C6('4c4e', 'plain_p_le6') =} | {= C6('4c4e', 'plain_mean') =} |
| 4c2e | {= C6('4c2e', 'plain_p_le6') =} | {= C6('4c2e', 'plain_mean') =} |

Cale's later "even with full moveset sub-7 is 1 in 22" ([[T1805]]) says the same, and so did Jay within the hour: "hm, i guess it's a bit more worse than 4c2e than i thought" ([[T1806]]).
For illustration, a typical 4c6e. The EO leaves 4c6e for DR on {= WXX('X4', 'dr_axis') =}, and the shortest DR keeping the EO is {= WXX('X4', 'plain') =}, the most common length for that case:

```
{= SCR('X4') =}  // scramble
{= WXX('X4', 'eo') =}  // EO on {= WXX('X4', 'eo_axis') =}
{= WXX('X4', 'plain_dr') =}  // shortest DR keeping the EO
```
