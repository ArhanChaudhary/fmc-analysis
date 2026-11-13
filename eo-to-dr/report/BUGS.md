# EO to DR, and scramble to DR: corrections

*Goes with the write-up on EO to DR and scramble to DR, but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory, #fmc-discussion or #non-dr-discussion).

**What everything below is measured against:**

- **Exact distance tables**: the fewest turns to DR from every coset of the DR group (2,217,093,120 per axis), with any turns and with turns that keep an EO, and every EO distance.
- **EO to DR**: every one of the 1,082,565 EO-solved states on a DR axis, exactly.
- **50,000 uniformly random scrambles**, each searched exactly: every DR axis, normal, inverse and NISS, every EO of up to 6 turns.

Every scramble and move sequence below was replayed on a sticker-level cube. A ✓ after a number means it is proved in Lean, on a Lean model of the cube (the write-up's appendix B lists what is proved).

These are the statements the numbers go against, each with the numbers that settle it and an example. Most of what was said holds up; that's in the write-up's section 6, the claims checked one by one.

---

**1. "Last sheet of DRM/ARM doc has a distribution. 10 is the worst (~3% of all cases)"** (KrzychXyz, [12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1415999087219839016), answering zakimoshi's "What's the longest DR case after eo", [12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1415997351633621022)).
10 is the worst, as KrzychXyz says, but the share is wrong: on the sheet, and exactly, 3,114 ✓ of the 1,082,565 EO-solved states need 10 turns to DR (one DR axis, EO kept, linear), which is 0.29% ✓, ten times less. zakimoshi's follow-up "Wait so only 6.3% of all cases are sub 7able?" ([12 Sep 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1416001772345884712)) was a question; the exact share is 5.9% ✓.
For illustration, one of those states. The EO leaves 3c8e for DR on F/B, and the shortest DR that keeps the EO is 10:

```
U2 B2 U' R2 U F2 U2 R2 B2 F2 R2 B2 U2 L' B D' U' L' R' F' L2 F'  // scramble
D L' B R                                                         // EO on R/L
F2 U F B' D B L2 F' L2 D                                         // shortest DR keeping the EO
```

**2. "Superflip takes 6 moves to solve EO with NISS"** (Aneurin, [13 Apr 2023](https://discord.com/channels/1007840975726575667/1007841273111117924/1095997368069009439)).
It takes 7 ✓, on every axis, with or without NISS; every NISS split was searched, and Lean proves it: the superflip commutes with every face turn, so a NISS EO of it is a linear EO of the same length, and the linear EO needs 7. Aneurin had it right the first time ([13 Sep 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1019443537940594768), [13 Sep 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1019443653632069642)): "EO is 7 moves", "Even with niss".
Example: the superflip, with a 7-move NISS EO on it from alkamaass ([17 Jun 2024](https://discord.com/channels/1007840975726575667/1007841273111117924/1252389998808928356)); none of 6 exists.

```
U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2  // the superflip
D F U' (L B R U')                                   // EO on U/D
```

**3. DR-6e4c: "Similar efficiency to 4c4e and 4c2e in theory but many of the optimal solutions aren't findable with just setups to R U2 L"** (Jay, [14 Dec 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1052704838682689648), answering jellobean's "How good would you say … the Dr-6e4c case", [14 Dec 2022](https://discord.com/channels/1007840975726575667/1007841273111117924/1052653676902228008)).
The optimal DR alone already differs. Over all EO-solved states, one axis, EO kept; each row is a case:

| Case | DR in ≤ 6 | Mean, turns |
|---|---|---|
| 4c6e (Cale's 6e4c) | 4.6% ✓ | 7.85 ✓ |
| 4c4e | 19.2% ✓ | 7.19 ✓ |
| 4c2e | 18.7% ✓ | 7.16 ✓ |

Cale's later "even with full moveset sub-7 is 1 in 22" ([10 Apr 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1094878042096152576)) says the same, and so did Jay within the hour: "hm, i guess it's a bit more worse than 4c2e than i thought" ([10 Apr 2023](https://discord.com/channels/1007840975726575667/1007841335434285126/1094891233882685470)).
For illustration, a typical 4c6e. The EO leaves 4c6e for DR on R/L, and the shortest DR keeping the EO is 8, the most common length for that case:

```
U B2 R2 U' R2 U B2 D' F2 R2 U L2 F2 L' U' R' F2 D F' R B R U'  // scramble
U B' R F'                                                      // EO on F/B
F2 D2 L' B2 R' U' R2 D                                         // shortest DR keeping the EO
```
