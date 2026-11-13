# EO to DR, and scramble to DR: corrections

*Goes with the write-up on EO to DR and scramble to DR, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion).

**What everything below is measured against:**

- **Exact distance tables**: the fewest turns to DR from every coset of the DR group ({= COSETS() =} per axis), with any turns and with turns that keep an EO, and every EO distance.
- **EO to DR**: every one of the {= EODRT() =} EO-solved states on a DR axis, exactly.
- **{= n(X('n')) =} uniformly random scrambles**, each searched exactly: every DR axis, normal, inverse and NISS, every EO of up to 6 turns.

Every scramble and move sequence below was replayed on a sticker-level cube. A ✓ after a number means it is proved in Lean, on a Lean model of the cube (the write-up's appendix B lists what is proved).

These are the statements the numbers go against, each with the numbers that settle it and an example. Most of what was said holds up; that's in the write-up's section 6, the claims checked one by one.

---

**1. "Last sheet of DRM/ARM doc has a distribution. 10 is the worst (~3% of all cases)"** (KrzychXyz, [[D14031]], answering zakimoshi's "What's the longest DR case after eo", [[D14026]]).
10 is the worst, as KrzychXyz says, but the share is wrong: on the sheet, and exactly, {= EODRN(10) =} ✓ of the {= EODRT() =} EO-solved states need 10 turns to DR (one DR axis, EO kept, linear), which is {= EODR(10) =} ✓, ten times less.
For illustration, one of those states. The EO leaves {= WXX('X1', 'case') =} for DR on F/B, and the shortest DR that keeps the EO is 10:

```
{= SCR('X1') =}  // scramble
{= WXX('X1', 'eo') =}  // EO on R/L
{= WXX('X1', 'plain_dr') =}  // shortest DR keeping the EO
```

**2. "Superflip takes 6 moves to solve EO with NISS"** (Aneurin, [[D1281]]).
It takes 7 ✓, on every axis, with or without NISS; every NISS split was searched, and there is a short proof: the superflip commutes with every face turn (✓ Lean), so a NISS EO of it is a linear EO of the same length, and the linear EO needs 7 (✓ Lean). Aneurin had it right the first time ([[D174]], [[D175]]): "EO is 7 moves", "Even with niss".
The thread was about scrambles with 12 bad edges on every axis, and most of those do have a NISS EO shorter than 7: Joba's table has only 1,792 edge states that need 7 ([[T9374]]), against {= EDGESTATES(lambda t: t == (12, 12, 12)) =} with 12 bad on every axis, and torchlight gave one with 6, "(superflip + 3-cycle on M) has 6-move NISS EOs" ([[T9414]]). The superflip itself is not one of them.
Example: the superflip, with a 7-move NISS EO on it from alkamaass ([[D6033]]); none of 6 exists.

```
{= SCR('W3') =}  // the superflip
{= WXX('X5', 'normal') =} ({= WXX('X5', 'inverse') =})  // EO on U/D
```

**3. DR-6e4c: "Similar efficiency to 4c4e and 4c2e in theory but many of the optimal solutions aren't findable with just setups to R U2 L"** (Jay, [[D584]], answering jellobean's "How good would you say (is it worth looking at most of the time) the Dr-6e4c case", [[D583]]; Jay's next message: "I wouldn't really NISS for it", [[D585]]).
The advice holds. The "in theory" half doesn't: the optimal DR alone already differs. Over all EO-solved states, one axis, EO kept; each row is a case:

| Case | DR in ≤ 6 | Mean, turns |
|---|---|---|
| 4c6e (Cale's 6e4c) | {= C6('4c6e', 'plain_p_le6') =} ✓ | {= C6('4c6e', 'plain_mean') =} ✓ |
| 4c4e | {= C6('4c4e', 'plain_p_le6') =} ✓ | {= C6('4c4e', 'plain_mean') =} ✓ |
| 4c2e | {= C6('4c2e', 'plain_p_le6') =} ✓ | {= C6('4c2e', 'plain_mean') =} ✓ |

These rows are in Cale's *DR setup stats* sheet. Jay said it once more in April 2023 ("I feel like 4C6E in 5 is probably just as good as 4C2E in 5, if not better", one reason being "The average move count when you account for trickier solutions (shifting to other triggers) is around the same as 4C2E", [[T1802]]); Cale answered "even with full moveset sub-7 is 1 in 22" ([[T1805]]), and Jay within the hour: "hm, i guess it's a bit more worse than 4c2e than i thought" ([[T1806]]).
For illustration, a typical 4c6e. The EO leaves 4c6e for DR on {= WXX('X4', 'dr_axis') =}, and the shortest DR keeping the EO is {= WXX('X4', 'plain') =}, the most common length for that case:

```
{= SCR('X4') =}  // scramble
{= WXX('X4', 'eo') =}  // EO on {= WXX('X4', 'eo_axis') =}
{= WXX('X4', 'plain_dr') =}  // shortest DR keeping the EO
```
