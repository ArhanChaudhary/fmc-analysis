# Worked examples: when to switch an EO

Examples to play along with [the write-up](index.html). Do the EO and RZP, look at the bad pieces, do the reads, decide, then open the answer.

These are 201 real attempts from uniformly random scrambles: an EO and an RZP that reach the DRM at 5 moves total, so a good switch is a DR in 6 or less on the other side (sub-7). They're spread over the groups of the cards, 4c4e most, and random within a group. Nothing is hand-picked. A handful of examples per group is a small sample, so the tallies below wobble. The exact numbers of each group are in the answers.

**How to read it.**

- Every attempt is turned so the EO is on F/B and the DR on U/D, like in the write-up. The scramble printed is the generated one with the faces renamed, so it is the same scramble held another way.
- An EO and RZP in brackets were found on the inverse scramble. The DR is then on the other side, as usual with NISS.
- Colours are for white top, green front: the U/D colours are white and yellow, F/B green and blue, R/L red and orange.
- *What you see* is the cube after the EO and RZP, before you switch: the U/D edges sitting in the E slice, the misoriented corners with the colour each one shows on the U/D face, and the E-slice edges that are out of the slice.
- *Reads* are what the card of that DRM asks for, all counted on the side you are on, the way the write-up traces them:
  - a *pair* is a misoriented corner whose two side stickers are the two colours of a U/D edge in the E slice, and two pairs on one edge are a *bar*;
  - a *fake pair* is a corner with both of that edge's colours that shows the edge's side colour on U/D;
  - a *side pair* is a corner with both colours of an E-slice edge that is out of the slice, showing green or blue on U/D;
  - *ARM* is the corners showing red or orange on U/D, then the U/D edges in the E slice with green or blue;
  - the *holes* are where the E-slice edges that are out of the slice belong: on one R/L face if the two share red or orange, on one F/B face if they share green or blue, diagonal if they share nothing;
  - 4a corners are *in two columns* when they are two twins, each a white corner and a yellow corner with the same two other colours (Evan's stacked corners);
  - *bad edges in one layer* (4c6e) means the U/D edges in the E slice are all white or all yellow, and the corner count is the misoriented corners by their white or yellow sticker;
  - a *split pair* (3c2e) is wen's ([12 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1471458126539526323)), read in colours: a U/D edge in the E slice and a misoriented corner with the same white or yellow and without the edge's other colour, where the edge has green or blue and the corner shows red or orange on U/D, or the other way round.
- The answer has the card's group and verdict (**switch**, **if you have time** or **skip**), how big that group is and how its cases split by DR length (exact, every case of the DRM once), what the pairs rule says, what Fanti's pairs + ARM list says where there is one, and one optimal DR on the other side with the EO kept.

The rules the card is put next to, one row per DRM. The pairs rules are the NISS column of rodneykinney's [*DRM Subsets Meta*](https://docs.google.com/document/d/1Jnd1Qy_6b1W5dR5fZQScloMoMPR2LCAF7VPrgeTaRgg) where it has one, with plain 5+ pairs for 7c8e and rodneykinney's decision tree for 8c8e ([2 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412510225906401403)). The pairs + ARM lists are Fanti's ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069), and [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436042954501390401) for 3c4e and 3c6e). [The write-up](index.html) has who said what, with the quotes.

| DRM | Pairs rule | From | Pairs + ARM list (Fanti) |
|---|---|---|---|
| 4c4e | 2+ pairs | *DRM Subsets Meta*; tseitsei89 | 2+ pairs; 1 pair with ARM 21; 0 pairs with JZP or ARM 42 |
| 4c2e | 1.5+ pairs (2 side pairs = 1 pair) | *DRM Subsets Meta*; rodneykinney; Jay | 1+ pairs; 0 pairs with JZP |
| 3c2e | always | *DRM Subsets Meta*; tseitsei89 | none |
| 7c8e | 5+ pairs, counting edge ARM under 2 as a pair | *DRM Subsets Meta*; tseitsei89 | 5+ pairs; 4 pairs with ARM 21, 31, 43; 3 pairs with ARM 21 |
| 8c8e | 3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs | rodneykinney's tree | none |
| 2c2e | 1+ pairs | *DRM Subsets Meta* | none |
| 4c6e | never | *DRM Subsets Meta* | none |
| 3c4e | 2+ pairs | *DRM Subsets Meta* (sometimes) | 2 pairs; 1 pair with ARM 00 or 21 |
| 3c6e | never | not on the *DRM Subsets Meta* list | 3 pairs with ARM 00; 2 pairs with ARM 21 |
| 5c4e | never | *DRM Subsets Meta* | none |
| 5c6e | never | *DRM Subsets Meta* | none |
| 6c6e | never | *DRM Subsets Meta* | none |

**Replay check.** Every move sequence here was replayed on a sticker model of the cube before the page was written: 4,708 checks, 0 mismatches. The turned scramble is the generated one after a rotation. EO + RZP solves the F/B EO in 5 moves and gives the stated DRM. Every read done on the side you are on equals the same count taken on the other side directly. The card group is the one the case falls in. The DR takes the other side to DR on U/D with the EO kept, in the optimal number of moves, and nissy 2.0.8 finds the same length for all 201.

**How these 201 came out.** One row per verdict, the columns are the examples by the length of the optimal DR after the switch:

| Verdict | Examples | DR in 4 or less | DR in 5 | DR in 6 | DR in 7 or more | DR in 6 or less, expected from the groups' exact rates |
|---|---|---|---|---|---|---|
| Card: switch | 127 | 5 | 14 | 52 | 56 | 70 |
| Card: if you have time | 34 | 0 | 0 | 2 | 32 | 7 |
| Card: skip | 40 | 0 | 0 | 1 | 39 | 2 |
| Pairs rule: switch | 90 | 4 | 13 | 32 | 41 | 49 |
| Pairs rule: skip | 111 | 1 | 1 | 23 | 86 | 30 |

The examples are spread over the groups, not drawn the way attempts come up, so read the rows as what each verdict looks like, not as how often you get it. The last column is how many of the row's examples would have a DR in 6 or less if every group came out at its exact rate. This draw is short on the *if you have time* row.

**Where the card and the pairs rule disagree.**

- Card switches, pairs rule skips (53 examples, 23 with a DR in 6 or less): 4, 7, 8, 9, 11, 29, 32, 36, 38, 40, 44, 47, 53, 64, 66, 67, 71, 74, 76, 77, 78, 79, 82, 85, 89, 94, 95, 98, 100, 103, 119, 147, 149, 151, 160, 162, 166, 173, 177, 180, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 196, 200, 201.
- Card says if you have time, pairs rule switches (15 examples, 1 with a DR in 6 or less): 1, 3, 5, 35, 43, 60, 65, 87, 122, 125, 130, 134, 136, 137, 156.
- Card skips, pairs rule switches (1 example, 0 with a DR in 6 or less): 165.

## 4c4e: examples 1–90

The 4c4e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 4c4e once; 19.2% for 4c4e as a whole):

| What you read | Verdict | Share of 4c4e | Sub-7 |
|---|---|---|---|
| 3 or 4 pairs | switch | 3.6% | 79.9% |
| 2 pairs on two edges | switch | 11.9% | 53.9% |
| 2 pairs on one edge (a bar), holes on one R/L face | switch | 3.5% | 43.7% |
| 1 pair, ARM 21, 4d corners | switch | 0.82% | 88.9% |
| 1 pair, ARM 21, 4b corners, 0 or 2 side pairs | switch | 2.8% | 50.4% |
| 1 pair, ARM 21, 4a corners in two columns | switch | 1.5% | 34.8% |
| 0 pairs, no fake pairs, corners 2 and 2 in the layers | switch | 0.82% | 21.9% |
| 2 pairs on one edge (a bar), holes not on one R/L face | if you have time | 7.0% | 18.1% |
| 1 pair, not ARM 21, 2+ side pairs, not 4b corners | if you have time | 6.8% | 19.2% |
| 1 pair, ARM 21, 4a corners not in two columns | skip | 1.4% | 2.5% |
| 1 pair, ARM 21, 4b corners, exactly 1 side pair | skip | 2.6% | 5.6% |
| 1 pair, anything else | skip | 28.3% | 6.1% |
| 0 pairs, anything else | skip | 28.9% | 3.8% |

**Example 1 (4c4e).** `L' F2 L' D2 R2 U2 F2 R' U2 L' U2 B2 U2 L' B' D L' B2 U L' D' F D`

EO `(B U R2 L B')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-orange
- Misoriented corners: yellow-green-orange showing green, yellow-green-red showing red, white-green-red showing red, yellow-blue-orange showing blue
- E-slice edges out of the slice: green-orange, blue-red

Reads: 2 pairs, both on yellow-orange (a bar), 1 fake pair, 1 side pair, ARM 20, 4b-2 corners, holes diagonal (the edges out of the slice share no colour), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*2 pairs on one edge (a bar), holes not on one R/L face*). That group is 7.0% of 4c4e, 4,960 cases: 0 with a DR in 4 or less, 56 in 5, 840 in 6, 4,064 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `L' U' R2 U' F2 L` (6 moves, good). The whole attempt: `(B U R2 L B') L' U' R2 U' F2 L`, 11 to DR.

</details>

**Example 2 (4c4e).** `R2 L2 D F2 U F2 U R2 F2 L2 B2 D B' U B R' D' F' D' U' B U'`

EO `(B L2 F' D2 B')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, white-blue
- Misoriented corners: white-blue-red showing red, white-green-red showing red, white-blue-orange showing blue, yellow-blue-red showing red
- E-slice edges out of the slice: green-red, blue-orange

Reads: 2 pairs, one on each edge, 1 fake pair, 1 side pair, ARM 31, 4c-1 corners, holes diagonal (the edges out of the slice share no colour), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `D' F2 L2 U' L` (5 moves, good). The whole attempt: `(B L2 F' D2 B') D' F2 L2 U' L`, 10 to DR.

</details>

**Example 3 (4c4e).** `D2 R D2 R' B2 L' F2 R2 B2 F2 R' B2 L' F' D' B2 F2 L' D F R2 U`

EO `(D' B2 D' R2 B)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-green, white-blue
- Misoriented corners: white-blue-orange showing orange, white-blue-red showing red, yellow-green-red showing green, yellow-blue-red showing blue
- E-slice edges out of the slice: green-orange, blue-red

Reads: 2 pairs, both on white-blue (a bar), 0 fake pairs, 1 side pair, ARM 22, 4b-2 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*2 pairs on one edge (a bar), holes not on one R/L face*). That group is 7.0% of 4c4e, 4,960 cases: 0 with a DR in 4 or less, 56 in 5, 840 in 6, 4,064 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U' R2 F2 U2 R2 F2 R` (7 moves, too long). The whole attempt: `(D' B2 D' R2 B) U' R2 F2 U2 R2 F2 R`, 12 to DR.

</details>

**Example 4 (4c4e).** `D R2 D2 R2 F2 D R2 D L2 F2 R2 U' R2 U' F2 L' U2 L2 B F2 L' F R' L'`

EO `R' L2 B' L' F`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-green
- Misoriented corners: yellow-blue-orange showing blue, white-green-red showing red, yellow-blue-red showing blue, yellow-green-red showing red
- E-slice edges out of the slice: blue-red, blue-orange

Reads: 1 pair (on yellow-green), 1 fake pair, 2 side pairs, ARM 21, 4b-2 corners, holes on one F/B face (both edges out of the slice have blue), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4b corners, 0 or 2 side pairs*). That group is 2.8% of 4c4e, 1,984 cases: 0 with a DR in 4 or less, 160 in 5, 840 in 6, 984 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `B2 D2 R2 B2 U R` (6 moves, good). The whole attempt: `R' L2 B' L' F (B2 D2 R2 B2 U R)`, 11 to DR.

</details>

**Example 5 (4c4e).** `F2 R2 U L2 D2 F2 U R2 U' R2 U B2 R2 R' B D B R' D B' R' F' D'`

EO `(F L' F' D B')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-green
- Misoriented corners: white-blue-red showing red, white-green-orange showing green, yellow-blue-red showing blue, yellow-green-red showing green
- E-slice edges out of the slice: green-orange, blue-red

Reads: 2 pairs, both on yellow-red (a bar), 1 fake pair, 2 side pairs, ARM 11, 4c-1 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*2 pairs on one edge (a bar), holes not on one R/L face*). That group is 7.0% of 4c4e, 4,960 cases: 0 with a DR in 4 or less, 56 in 5, 840 in 6, 4,064 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `D' F2 R' U' L2 D R` (7 moves, too long). The whole attempt: `(F L' F' D B') D' F2 R' U' L2 D R`, 12 to DR.

</details>

**Example 6 (4c4e).** `B2 F2 L D2 R D2 R B2 D2 F2 U2 L U' R U B' L' D' L' R' U R'`

EO `R L' U2 L' B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-green, yellow-blue
- Misoriented corners: yellow-blue-orange showing orange, white-green-orange showing green, yellow-green-orange showing green, white-blue-red showing blue
- E-slice edges out of the slice: green-orange, blue-orange

Reads: 1 pair (on yellow-blue), 1 fake pair, 2 side pairs, ARM 12, 4c-1 corners, holes on one R/L face (both edges out of the slice have orange), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, not ARM 21, 2+ side pairs, not 4b corners*). That group is 6.8% of 4c4e, 4,832 cases: 0 with a DR in 4 or less, 48 in 5, 880 in 6, 3,904 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `U' R2 U' F2 U2 B2 U R` (8 moves, too long). The whole attempt: `R L' U2 L' B' (U' R2 U' F2 U2 B2 U R)`, 13 to DR.

</details>

**Example 7 (4c4e).** `D R2 U2 F2 L2 R2 U L2 D' F2 U R2 F2 L2 U' R' U' R' B L' D2 R B' U2`

EO `F R U2 R2 B`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-blue
- Misoriented corners: white-green-red showing red, white-blue-orange showing blue, yellow-green-orange showing orange, yellow-blue-red showing blue
- E-slice edges out of the slice: blue-red, green-red

Reads: 1 pair (on white-orange), 1 fake pair, 1 side pair, ARM 21, 4d-2 corners, holes on one R/L face (both edges out of the slice have red), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4d corners*). That group is 0.82% of 4c4e, 576 cases: 32 with a DR in 4 or less, 96 in 5, 384 in 6, 64 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U' D B2 U F2 L` (6 moves, good). The whole attempt: `F R U2 R2 B (U' D B2 U F2 L)`, 11 to DR.

</details>

**Example 8 (4c4e).** `D2 F D2 L2 U2 F' L2 B2 R2 L2 B R2 F2 D' B2 F L B F L F2 D`

EO `D' B L F'`, RZP `R'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-blue, yellow-orange
- Misoriented corners: white-blue-orange showing orange, yellow-blue-red showing blue, yellow-blue-orange showing orange, white-blue-red showing blue
- E-slice edges out of the slice: green-orange, green-red

Reads: 1 pair (on yellow-blue), 2 fake pairs, 0 side pairs, ARM 21, 4a-2 corners, in two columns (two twins), holes on one F/B face (both edges out of the slice have green), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4a corners in two columns*). That group is 1.5% of 4c4e, 1,056 cases: 0 with a DR in 4 or less, 64 in 5, 304 in 6, 688 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 D' R' D' R2 F2 R` (7 moves, too long). The whole attempt: `D' B L F' R' (U2 D' R' D' R2 F2 R)`, 12 to DR.

</details>

**Example 9 (4c4e).** `F2 U2 F2 L U2 R U2 R' U2 F2 R2 U2 F2 R' U' L D R B R' F L B2 R`

EO `R' L F R B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-green, white-green
- Misoriented corners: yellow-blue-red showing red, yellow-blue-orange showing orange, white-blue-red showing red, white-blue-orange showing orange
- E-slice edges out of the slice: green-red, blue-red

Reads: 0 pairs, 0 fake pairs, 0 side pairs, ARM 42, 4a-4 corners, in two columns (two twins), holes on one R/L face (both edges out of the slice have red), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, no fake pairs, corners 2 and 2 in the layers*). That group is 0.82% of 4c4e, 576 cases: 14 with a DR in 4 or less, 24 in 5, 88 in 6, 450 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U D' F2 B2 L` (5 moves, good). The whole attempt: `R' L F R B' (U D' F2 B2 L)`, 10 to DR.

</details>

**Example 10 (4c4e).** `U2 F2 U2 B2 L2 B2 L2 R' B2 L' B2 D2 L' B' U' F2 L D2 B' U F' L2 R2`

EO `(U2 D' F L2 B)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-green, white-blue
- Misoriented corners: white-blue-orange showing orange, white-green-red showing green, white-green-orange showing green, white-blue-red showing red
- E-slice edges out of the slice: green-red, blue-red

Reads: 2 pairs, both on white-blue (a bar), 0 fake pairs, 1 side pair, ARM 22, 4a-2 corners, not in two columns, holes on one R/L face (both edges out of the slice have red), corners 4 white, 0 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on one edge (a bar), holes on one R/L face*). That group is 3.5% of 4c4e, 2,480 cases: 20 with a DR in 4 or less, 244 in 5, 820 in 6, 1,396 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `D B2 R U2 R' B2 U R` (8 moves, too long). The whole attempt: `(U2 D' F L2 B) D B2 R U2 R' B2 U R`, 13 to DR.

</details>

**Example 11 (4c4e).** `U2 F2 U2 B2 L2 B2 L2 R' B2 L' B2 D2 L' B' U' F2 L D2 B' U F' L2 R2`

EO `L2 D F' R2 B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, white-orange
- Misoriented corners: white-green-red showing green, white-green-orange showing green, yellow-green-red showing red, yellow-green-orange showing orange
- E-slice edges out of the slice: green-red, blue-orange

Reads: 1 pair (on white-orange), 0 fake pairs, 1 side pair, ARM 21, 4a-2 corners, in two columns (two twins), holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4a corners in two columns*). That group is 1.5% of 4c4e, 1,056 cases: 0 with a DR in 4 or less, 64 in 5, 304 in 6, 688 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `R2 U' L2 U B2 L` (6 moves, good). The whole attempt: `L2 D F' R2 B' (R2 U' L2 U B2 L)`, 11 to DR.

</details>

**Example 12 (4c4e).** `L2 B2 D2 F U2 R2 F U2 D2 B R2 F2 R2 R' D' F U F2 L' D' R' U'`

EO `D2 F' U' R B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-green, white-red
- Misoriented corners: white-blue-orange showing blue, yellow-green-red showing green, yellow-green-orange showing green, white-blue-red showing blue
- E-slice edges out of the slice: blue-orange, green-orange

Reads: 1 pair (on white-red), 2 fake pairs, 2 side pairs, ARM 01, 4a-0 corners, not in two columns, holes on one R/L face (both edges out of the slice have orange), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, not ARM 21, 2+ side pairs, not 4b corners*). That group is 6.8% of 4c4e, 4,832 cases: 0 with a DR in 4 or less, 48 in 5, 880 in 6, 3,904 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `R' D' L' D2 L2 F2 D' R` (8 moves, too long). The whole attempt: `D2 F' U' R B' (R' D' L' D2 L2 F2 D' R)`, 13 to DR.

</details>

**Example 13 (4c4e).** `F2 R2 U L2 D2 F2 U R2 U' R2 U B2 R2 R' B D B R' D B' R' F' D'`

EO `(D' F L' F B')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, white-green
- Misoriented corners: yellow-blue-orange showing orange, white-green-orange showing green, yellow-blue-red showing blue, white-green-red showing red
- E-slice edges out of the slice: green-orange, blue-red

Reads: 1 pair (on white-green), 2 fake pairs, 2 side pairs, ARM 21, 4a-2 corners, not in two columns, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, ARM 21, 4a corners not in two columns*). That group is 1.4% of 4c4e, 960 cases: 0 with a DR in 4 or less, 0 in 5, 24 in 6, 936 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U L B2 R2 F2 D' L` (7 moves, too long). The whole attempt: `(D' F L' F B') U L B2 R2 F2 D' L`, 12 to DR.

</details>

**Example 14 (4c4e).** `R2 B R2 B' D2 F' U2 B2 D2 U2 B' D2 F' U' R' D2 U2 F' R U B2 L`

EO `(L U2 D2 L F)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-green, yellow-blue
- Misoriented corners: yellow-blue-orange showing orange, white-blue-red showing blue, white-green-red showing red, yellow-green-red showing red
- E-slice edges out of the slice: blue-red, blue-orange

Reads: 2 pairs, one on each edge, 0 fake pairs, 1 side pair, ARM 32, 4c-1 corners, holes on one F/B face (both edges out of the slice have blue), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `D2 L2 D' B2 U L` (6 moves, good). The whole attempt: `(L U2 D2 L F) D2 L2 D' B2 U L`, 11 to DR.

</details>

**Example 15 (4c4e).** `F R2 B2 U2 L2 R2 B L2 F' U2 B R2 U2 L2 B' R' B' R' D L' F2 R D' B2`

EO `R U' D2 B'`, RZP `L'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, white-red
- Misoriented corners: yellow-green-orange showing green, yellow-green-red showing green, white-blue-red showing blue, yellow-blue-orange showing orange
- E-slice edges out of the slice: blue-red, blue-orange

Reads: 2 pairs, one on each edge, 1 fake pair, 1 side pair, ARM 10, 4c-1 corners, holes on one F/B face (both edges out of the slice have blue), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U L2 F2 U2 D R` (6 moves, good). The whole attempt: `R U' D2 B' L' (U L2 F2 U2 D R)`, 11 to DR.

</details>

**Example 16 (4c4e).** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `R' B' R L B`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-green
- Misoriented corners: white-green-red showing red, white-green-orange showing orange, yellow-green-orange showing green, white-blue-orange showing orange
- E-slice edges out of the slice: blue-orange, blue-red

Reads: 0 pairs, 3 fake pairs, 0 side pairs, ARM 31, 4c-1 corners, holes on one F/B face (both edges out of the slice have blue), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*0 pairs, anything else*). That group is 28.9% of 4c4e, 20,424 cases: 0 with a DR in 4 or less, 36 in 5, 748 in 6, 19,640 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `U2 R2 D' L' F2 L2 U L` (8 moves, too long). The whole attempt: `R' B' R L B (U2 R2 D' L' F2 L2 U L)`, 13 to DR.

</details>

**Example 17 (4c4e).** `R2 U2 L2 D2 F' U2 F R2 B2 D2 R2 F' B2 U' L' R2 F L R D L' F' B'`

EO `(R' B L U F)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-green, white-blue
- Misoriented corners: white-green-red showing green, white-blue-red showing blue, yellow-blue-red showing red, yellow-green-orange showing green
- E-slice edges out of the slice: green-red, blue-red

Reads: 0 pairs, 2 fake pairs, 2 side pairs, ARM 12, 4c-1 corners, holes on one R/L face (both edges out of the slice have red), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*0 pairs, anything else*). That group is 28.9% of 4c4e, 20,424 cases: 0 with a DR in 4 or less, 36 in 5, 748 in 6, 19,640 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `L' U' R2 L U' D R` (7 moves, too long). The whole attempt: `(R' B L U F) L' U' R2 L U' D R`, 12 to DR.

</details>

**Example 18 (4c4e).** `L2 B R2 D2 R2 L2 F' L2 F2 U2 F U2 F D2 B' L' F D R' U2 F' U' F' L F2`

EO `(F U' D' L' F)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-green, white-red
- Misoriented corners: white-blue-orange showing orange, white-green-red showing green, yellow-blue-orange showing orange, white-blue-red showing blue
- E-slice edges out of the slice: green-orange, blue-orange

Reads: 2 pairs, both on white-red (a bar), 0 fake pairs, 0 side pairs, ARM 21, 4b-2 corners, holes on one R/L face (both edges out of the slice have orange), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on one edge (a bar), holes on one R/L face*). That group is 3.5% of 4c4e, 2,480 cases: 20 with a DR in 4 or less, 244 in 5, 820 in 6, 1,396 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `L2 U2 R2 D' L` (5 moves, good). The whole attempt: `(F U' D' L' F) L2 U2 R2 D' L`, 10 to DR.

</details>

**Example 19 (4c4e).** `R2 D2 L' F2 D2 R2 D2 R' B2 D2 R2 D2 R F2 R' F' L F2 U2 R' D L F2 D'`

EO `(R2 L2 U2 L B)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-green, yellow-blue
- Misoriented corners: yellow-blue-red showing blue, yellow-green-red showing green, white-blue-red showing red, yellow-green-orange showing orange
- E-slice edges out of the slice: blue-orange, green-orange

Reads: 0 pairs, 1 fake pair, 0 side pairs, ARM 22, 4b-2 corners, holes on one R/L face (both edges out of the slice have orange), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*0 pairs, anything else*). That group is 28.9% of 4c4e, 20,424 cases: 0 with a DR in 4 or less, 36 in 5, 748 in 6, 19,640 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `U2 L2 D R' U' L U R` (8 moves, too long). The whole attempt: `(R2 L2 U2 L B) U2 L2 D R' U' L U R`, 13 to DR.

</details>

**Example 20 (4c4e).** `L2 U2 B2 R U2 R' U2 L' D2 L D2 B2 D' F2 L F2 R U B' U' F'`

EO `(B' L' U' L2 F')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, white-orange
- Misoriented corners: yellow-blue-red showing blue, white-blue-red showing red, white-green-orange showing green, yellow-green-orange showing orange
- E-slice edges out of the slice: blue-orange, green-red

Reads: 1 pair (on white-orange), 1 fake pair, 0 side pairs, ARM 20, 4a-2 corners, in two columns (two twins), holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, anything else*). That group is 28.3% of 4c4e, 19,936 cases: 0 with a DR in 4 or less, 56 in 5, 1,152 in 6, 18,728 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `B2 U2 D F2 R' U2 F2 R` (8 moves, too long). The whole attempt: `(B' L' U' L2 F') B2 U2 D F2 R' U2 F2 R`, 13 to DR.

</details>

**Example 21 (4c4e).** `D' R2 U' L2 U R2 B2 U L2 D' R2 U R2 U F' R L' D' L' B' R' F2 L2`

EO `L2 F R U' B`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, white-orange
- Misoriented corners: white-green-red showing green, white-blue-red showing blue, yellow-blue-red showing red, white-blue-orange showing blue
- E-slice edges out of the slice: blue-orange, blue-red

Reads: 1 pair (on white-orange), 2 fake pairs, 2 side pairs, ARM 11, 4c-1 corners, holes on one F/B face (both edges out of the slice have blue), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, not ARM 21, 2+ side pairs, not 4b corners*). That group is 6.8% of 4c4e, 4,832 cases: 0 with a DR in 4 or less, 48 in 5, 880 in 6, 3,904 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `D2 L2 B2 U L2 D L` (7 moves, too long). The whole attempt: `L2 F R U' B (D2 L2 B2 U L2 D L)`, 12 to DR.

</details>

**Example 22 (4c4e).** `L2 R2 B' U2 F2 U2 L2 F' U2 B2 U2 R2 F B2 R2 U' B2 L B R U B L' D L'`

EO `(U2 B D' F)`, RZP `(L)`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, white-green
- Misoriented corners: white-blue-orange showing blue, white-green-red showing red, white-green-orange showing green, yellow-blue-orange showing orange
- E-slice edges out of the slice: blue-red, blue-orange

Reads: 3 pairs (white-orange 2, white-green 1), 1 fake pair, 1 side pair, ARM 21, 4b-2 corners, holes on one F/B face (both edges out of the slice have blue), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 or 4 pairs*). That group is 3.6% of 4c4e, 2,520 cases: 332 with a DR in 4 or less, 522 in 5, 1,160 in 6, 506 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `L2 U' F2 D2 R` (5 moves, good). The whole attempt: `(U2 B D' F L) L2 U' F2 D2 R`, 10 to DR.

</details>

**Example 23 (4c4e).** `B D2 F2 L2 U2 D2 F U2 B' L2 F D2 L2 U2 F' D' F' D' R U' B2 D R' F2`

EO `U L2 U L B`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-blue
- Misoriented corners: yellow-blue-red showing blue, white-blue-red showing red, white-blue-orange showing orange, yellow-blue-orange showing blue
- E-slice edges out of the slice: green-red, blue-red

Reads: 3 pairs (yellow-red 1, white-blue 2), 0 fake pairs, 1 side pair, ARM 21, 4a-2 corners, in two columns (two twins), holes on one R/L face (both edges out of the slice have red), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 or 4 pairs*). That group is 3.6% of 4c4e, 2,520 cases: 332 with a DR in 4 or less, 522 in 5, 1,160 in 6, 506 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `R2 D B2 D' B2 R` (6 moves, good). The whole attempt: `U L2 U L B (R2 D B2 D' B2 R)`, 11 to DR.

</details>

**Example 24 (4c4e).** `F2 U F2 U' R2 D' L2 U2 R2 L2 U' R2 D' L' F' R2 L2 D' F L U2 B`

EO `D2 B2 D R B`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, white-green
- Misoriented corners: white-green-red showing green, yellow-blue-red showing blue, yellow-blue-orange showing blue, white-green-orange showing green
- E-slice edges out of the slice: green-orange, blue-red

Reads: 1 pair (on white-red), 2 fake pairs, 2 side pairs, ARM 01, 4a-0 corners, not in two columns, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, not ARM 21, 2+ side pairs, not 4b corners*). That group is 6.8% of 4c4e, 4,832 cases: 0 with a DR in 4 or less, 48 in 5, 880 in 6, 3,904 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `R D L2 B2 R2 U' R` (7 moves, too long). The whole attempt: `D2 B2 D R B (R D L2 B2 R2 U' R)`, 12 to DR.

</details>

**Example 25 (4c4e).** `L2 U2 B2 R U2 R' U2 L' D2 L D2 B2 D' F2 L F2 R U B' U' F'`

EO `(B U' F)`, RZP `(R2 L')`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, white-green
- Misoriented corners: white-green-orange showing green, white-green-red showing green, yellow-blue-orange showing orange, yellow-blue-red showing red
- E-slice edges out of the slice: green-orange, blue-red

Reads: 1 pair (on white-red), 2 fake pairs, 1 side pair, ARM 21, 4a-2 corners, not in two columns, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, ARM 21, 4a corners not in two columns*). That group is 1.4% of 4c4e, 960 cases: 0 with a DR in 4 or less, 0 in 5, 24 in 6, 936 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `L2 U R2 U2 B2 D' R` (7 moves, too long). The whole attempt: `(B U' F R2 L') L2 U R2 U2 B2 D' R`, 12 to DR.

</details>

**Example 26 (4c4e).** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `L B`, RZP `L' U' R`: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, white-orange
- Misoriented corners: white-blue-red showing red, white-blue-orange showing blue, white-green-orange showing green, yellow-blue-orange showing blue
- E-slice edges out of the slice: green-red, blue-orange

Reads: 3 pairs (yellow-orange 1, white-orange 2), 0 fake pairs, 2 side pairs, ARM 10, 4c-1 corners, holes diagonal (the edges out of the slice share no colour), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 or 4 pairs*). That group is 3.6% of 4c4e, 2,520 cases: 332 with a DR in 4 or less, 522 in 5, 1,160 in 6, 506 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U F2 U' L` (4 moves, good). The whole attempt: `L B L' U' R (U F2 U' L)`, 9 to DR.

</details>

**Example 27 (4c4e).** `F2 R2 D' U2 L2 U' F2 D L2 U' L2 B2 L2 R2 F' L D2 B' F R F' D`

EO `R2 L B'`, RZP `R' L'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, white-blue
- Misoriented corners: white-green-red showing green, white-green-orange showing orange, white-blue-orange showing orange, yellow-blue-orange showing blue
- E-slice edges out of the slice: blue-red, blue-orange

Reads: 1 pair (on white-blue), 2 fake pairs, 1 side pair, ARM 21, 4b-2 corners, holes on one F/B face (both edges out of the slice have blue), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, ARM 21, 4b corners, exactly 1 side pair*). That group is 2.6% of 4c4e, 1,856 cases: 0 with a DR in 4 or less, 24 in 5, 80 in 6, 1,752 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 B2 L2 U2 B2 D L` (7 moves, too long). The whole attempt: `R2 L B' R' L' (U2 B2 L2 U2 B2 D L)`, 12 to DR.

</details>

**Example 28 (4c4e).** `B2 F2 D R2 U R2 U B2 R2 F2 L2 D L' U L B' D' R' D' U' L U'`

EO `L D R2 F`, RZP `R'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, white-blue
- Misoriented corners: white-blue-red showing blue, yellow-blue-red showing blue, white-green-orange showing orange, yellow-green-orange showing orange
- E-slice edges out of the slice: green-orange, blue-orange

Reads: 0 pairs, 2 fake pairs, 0 side pairs, ARM 21, 4a-2 corners, in two columns (two twins), holes on one R/L face (both edges out of the slice have orange), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*0 pairs, anything else*). That group is 28.9% of 4c4e, 20,424 cases: 0 with a DR in 4 or less, 36 in 5, 748 in 6, 19,640 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `R2 L2 U2 D F2 D B2 R` (8 moves, too long). The whole attempt: `L D R2 F R' (R2 L2 U2 D F2 D B2 R)`, 13 to DR.

</details>

**Example 29 (4c4e).** `L2 F2 U2 R F2 R' F2 L' B2 L B2 U2 B' D2 L D2 R F U' F' D'`

EO `L F' D' R' F`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-green, white-orange
- Misoriented corners: yellow-green-orange showing green, white-blue-orange showing orange, white-green-orange showing green, white-blue-red showing red
- E-slice edges out of the slice: green-red, blue-red

Reads: 1 pair (on white-orange), 2 fake pairs, 0 side pairs, ARM 21, 4b-2 corners, holes on one R/L face (both edges out of the slice have red), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4b corners, 0 or 2 side pairs*). That group is 2.8% of 4c4e, 1,984 cases: 0 with a DR in 4 or less, 160 in 5, 840 in 6, 984 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U D R2 F2 B2 D L` (7 moves, too long). The whole attempt: `L F' D' R' F (U D R2 F2 B2 D L)`, 12 to DR.

</details>

**Example 30 (4c4e).** `L2 U2 L2 D2 F2 D2 F2 B' D2 F' D2 R2 F' D' L' U2 F R2 D' L U' F2 B2`

EO `(L D2 R' B)`, RZP `(L')`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-red
- Misoriented corners: yellow-green-orange showing orange, white-green-red showing green, yellow-green-red showing green, white-green-orange showing orange
- E-slice edges out of the slice: blue-red, green-orange

Reads: 2 pairs, one on each edge, 0 fake pairs, 0 side pairs, ARM 20, 4a-2 corners, in two columns (two twins), holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U B2 D2 R2 U L` (6 moves, good). The whole attempt: `(L D2 R' B L') U B2 D2 R2 U L`, 11 to DR.

</details>

**Example 31 (4c4e).** `D R2 D2 R2 F2 D R2 D L2 F2 R2 U' R2 U' F2 L' U2 L2 B F2 L' F R' L'`

EO `B' R F L' B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, yellow-green
- Misoriented corners: yellow-green-orange showing green, white-green-orange showing green, yellow-green-red showing green, yellow-blue-orange showing orange
- E-slice edges out of the slice: green-orange, blue-orange

Reads: 1 pair (on yellow-orange), 3 fake pairs, 2 side pairs, ARM 11, 4c-1 corners, holes on one R/L face (both edges out of the slice have orange), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, not ARM 21, 2+ side pairs, not 4b corners*). That group is 6.8% of 4c4e, 4,832 cases: 0 with a DR in 4 or less, 48 in 5, 880 in 6, 3,904 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `R2 L' U' F2 L U L` (7 moves, too long). The whole attempt: `B' R F L' B' (R2 L' U' F2 L U L)`, 12 to DR.

</details>

**Example 32 (4c4e).** `F L2 R2 U2 B L2 D2 B D2 R2 F2 L2 F R2 R' F L2 R U L2 U2 F2 B2`

EO `(R F' B2 L' F)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-green, white-red
- Misoriented corners: white-blue-orange showing orange, white-green-orange showing orange, yellow-blue-orange showing blue, yellow-blue-red showing blue
- E-slice edges out of the slice: green-orange, blue-red

Reads: 0 pairs, 0 fake pairs, 1 side pair, ARM 21, 4b-2 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, no fake pairs, corners 2 and 2 in the layers*). That group is 0.82% of 4c4e, 576 cases: 14 with a DR in 4 or less, 24 in 5, 88 in 6, 450 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `U' F2 U R2 D2 F2 B2 L` (8 moves, too long). The whole attempt: `(R F' B2 L' F) U' F2 U R2 D2 F2 B2 L`, 13 to DR.

</details>

**Example 33 (4c4e).** `L2 F2 D R2 D' F2 U B2 L2 D R2 U' F2 U' B2 F' L' D R' D L' D B2 D2 U2`

EO `(R' U F2 R2 B')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-red, yellow-green
- Misoriented corners: yellow-green-red showing green, white-green-orange showing green, white-blue-orange showing blue, white-blue-red showing red
- E-slice edges out of the slice: blue-orange, green-orange

Reads: 1 pair (on yellow-red), 1 fake pair, 2 side pairs, ARM 11, 4c-1 corners, holes on one R/L face (both edges out of the slice have orange), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, not ARM 21, 2+ side pairs, not 4b corners*). That group is 6.8% of 4c4e, 4,832 cases: 0 with a DR in 4 or less, 48 in 5, 880 in 6, 3,904 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `D L' U' B2 U F2 R` (7 moves, too long). The whole attempt: `(R' U F2 R2 B') D L' U' B2 U F2 R`, 12 to DR.

</details>

**Example 34 (4c4e).** `L2 U' B2 U R2 D' L2 D L2 F2 L2 B2 U' R2 U2 L' F U R' D L' R2 U2 F L U'`

EO `(L D F' B)`, RZP `(L')`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-red, yellow-blue
- Misoriented corners: white-blue-red showing blue, yellow-green-orange showing orange, white-green-orange showing orange, white-green-red showing green
- E-slice edges out of the slice: green-red, blue-red

Reads: 0 pairs, 0 fake pairs, 2 side pairs, ARM 21, 4b-2 corners, holes on one R/L face (both edges out of the slice have red), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*0 pairs, anything else*). That group is 28.9% of 4c4e, 20,424 cases: 0 with a DR in 4 or less, 36 in 5, 748 in 6, 19,640 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `D2 L2 D' F2 B2 L` (6 moves, good). The whole attempt: `(L D F' B L') D2 L2 D' F2 B2 L`, 11 to DR.

</details>

**Example 35 (4c4e).** `D2 L2 B2 U L2 U' L2 D' R2 D R2 B2 R' F2 D F2 U L B' L' F'`

EO `(L' F L B')`, RZP `(R)`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, white-orange
- Misoriented corners: white-blue-red showing blue, yellow-green-orange showing orange, white-green-red showing green, yellow-green-red showing red
- E-slice edges out of the slice: green-orange, blue-red

Reads: 2 pairs, both on white-red (a bar), 0 fake pairs, 1 side pair, ARM 20, 4b-2 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*2 pairs on one edge (a bar), holes not on one R/L face*). That group is 7.0% of 4c4e, 4,960 cases: 0 with a DR in 4 or less, 56 in 5, 840 in 6, 4,064 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `D' R2 F2 D2 R2 B2 L` (7 moves, too long). The whole attempt: `(L' F L B' R) D' R2 F2 D2 R2 B2 L`, 12 to DR.

</details>

**Example 36 (4c4e).** `D2 L2 B2 U L2 U' L2 D' R2 D R2 B2 R' F2 D F2 U L B' L' F'`

EO `(L' F' L B)`, RZP `(L')`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-blue
- Misoriented corners: yellow-green-red showing green, yellow-blue-orange showing orange, white-blue-red showing blue, white-green-orange showing orange
- E-slice edges out of the slice: blue-orange, green-orange

Reads: 1 pair (on yellow-red), 1 fake pair, 0 side pairs, ARM 21, 4d-2 corners, holes on one R/L face (both edges out of the slice have orange), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4d corners*). That group is 0.82% of 4c4e, 576 cases: 32 with a DR in 4 or less, 96 in 5, 384 in 6, 64 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U D F2 D' B2 R` (6 moves, good). The whole attempt: `(L' F' L B L') U D F2 D' B2 R`, 11 to DR.

</details>

**Example 37 (4c4e).** `L D2 L2 D2 F2 L D2 L U2 F2 D2 R' D2 R' F2 U' R2 U2 B F2 U' F D' U'`

EO `(D' F U' B')`, RZP `(L)`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-green
- Misoriented corners: white-green-red showing red, white-green-orange showing green, white-blue-red showing red, yellow-blue-red showing blue
- E-slice edges out of the slice: green-orange, green-red

Reads: 1 pair (on white-orange), 0 fake pairs, 1 side pair, ARM 21, 4b-2 corners, holes on one F/B face (both edges out of the slice have green), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, ARM 21, 4b corners, exactly 1 side pair*). That group is 2.6% of 4c4e, 1,856 cases: 0 with a DR in 4 or less, 24 in 5, 80 in 6, 1,752 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U D' F2 U' R2 B2 L` (7 moves, too long). The whole attempt: `(D' F U' B' L) U D' F2 U' R2 B2 L`, 12 to DR.

</details>

**Example 38 (4c4e).** `B2 L2 D2 B2 L F2 D2 L' U2 L U2 B2 L F2 R D' F' L' B2 U L2 B L2 F L'`

EO `(U2 F L2 B)`, RZP `(R')`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, yellow-green
- Misoriented corners: white-blue-orange showing blue, white-green-red showing red, yellow-green-orange showing green, yellow-blue-red showing red
- E-slice edges out of the slice: green-red, blue-orange

Reads: 1 pair (on yellow-orange), 1 fake pair, 1 side pair, ARM 21, 4d-2 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4d corners*). That group is 0.82% of 4c4e, 576 cases: 32 with a DR in 4 or less, 96 in 5, 384 in 6, 64 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `R2 D2 R2 D' B2 R` (6 moves, good). The whole attempt: `(U2 F L2 B R') R2 D2 R2 D' B2 R`, 11 to DR.

</details>

**Example 39 (4c4e).** `F2 U F2 L2 B2 U' L2 D2 R2 L2 D R2 U2 F' D2 U L D U L U2 F`

EO `L D2 L2 D F`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-red
- Misoriented corners: white-green-orange showing green, yellow-blue-red showing red, white-blue-orange showing blue, white-blue-red showing red
- E-slice edges out of the slice: blue-red, green-red

Reads: 2 pairs, both on white-orange (a bar), 1 fake pair, 0 side pairs, ARM 20, 4b-2 corners, holes on one R/L face (both edges out of the slice have red), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on one edge (a bar), holes on one R/L face*). That group is 3.5% of 4c4e, 2,480 cases: 20 with a DR in 4 or less, 244 in 5, 820 in 6, 1,396 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 D' L D R D' L` (7 moves, too long). The whole attempt: `L D2 L2 D F (U2 D' L D R D' L)`, 12 to DR.

</details>

**Example 40 (4c4e).** `F2 R F2 R' D2 L' U2 R2 D2 U2 R' D2 L' U' F' D2 U2 L' F U R2 B`

EO `(U2 L U2 R F)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, yellow-blue
- Misoriented corners: yellow-blue-orange showing blue, white-blue-red showing red, white-blue-orange showing orange, yellow-blue-red showing blue
- E-slice edges out of the slice: blue-red, blue-orange

Reads: 1 pair (on yellow-orange), 2 fake pairs, 2 side pairs, ARM 21, 4a-2 corners, in two columns (two twins), holes on one F/B face (both edges out of the slice have blue), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4a corners in two columns*). That group is 1.5% of 4c4e, 1,056 cases: 0 with a DR in 4 or less, 64 in 5, 304 in 6, 688 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `R D F2 L F2 D R` (7 moves, too long). The whole attempt: `(U2 L U2 R F) R D F2 L F2 D R`, 12 to DR.

</details>

**Example 41 (4c4e).** `R2 F' D2 R2 F D2 F R2 F' R2 F L2 B' D2 D' F R F2 L' D B R B F2`

EO `F R U' L2 B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, white-blue
- Misoriented corners: yellow-blue-red showing red, white-blue-orange showing blue, white-green-orange showing green, white-blue-red showing red
- E-slice edges out of the slice: blue-red, blue-orange

Reads: 1 pair (on white-blue), 1 fake pair, 1 side pair, ARM 21, 4b-2 corners, holes on one F/B face (both edges out of the slice have blue), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, ARM 21, 4b corners, exactly 1 side pair*). That group is 2.6% of 4c4e, 1,856 cases: 0 with a DR in 4 or less, 24 in 5, 80 in 6, 1,752 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `L' U2 D R2 U' B2 R` (7 moves, too long). The whole attempt: `F R U' L2 B' (L' U2 D R2 U' B2 R)`, 12 to DR.

</details>

**Example 42 (4c4e).** `R2 B R2 U2 L2 B' U2 F2 D2 U2 F D2 B2 R' F2 B U F B U B2 R`

EO `R D2 F U B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-red
- Misoriented corners: yellow-blue-orange showing blue, white-blue-orange showing blue, yellow-blue-red showing blue, yellow-green-orange showing orange
- E-slice edges out of the slice: blue-orange, green-red

Reads: 2 pairs, one on each edge, 0 fake pairs, 2 side pairs, ARM 10, 4c-1 corners, holes diagonal (the edges out of the slice share no colour), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `D F2 R2 D L` (5 moves, good). The whole attempt: `R D2 F U B' (D F2 R2 D L)`, 10 to DR.

</details>

**Example 43 (4c4e).** `F2 L2 U F2 R2 F2 L2 D' F2 D2 U R2 L' U R U2 R F U2 F U`

EO `U' B' R2 B`, RZP `R'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, white-orange
- Misoriented corners: white-blue-orange showing blue, yellow-blue-red showing red, white-green-orange showing green, white-green-red showing green
- E-slice edges out of the slice: blue-red, green-orange

Reads: 2 pairs, both on white-orange (a bar), 1 fake pair, 1 side pair, ARM 11, 4c-1 corners, holes diagonal (the edges out of the slice share no colour), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*2 pairs on one edge (a bar), holes not on one R/L face*). That group is 7.0% of 4c4e, 4,960 cases: 0 with a DR in 4 or less, 56 in 5, 840 in 6, 4,064 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U R D' R' F2 R2 U R` (8 moves, too long). The whole attempt: `U' B' R2 B R' (U R D' R' F2 R2 U R)`, 13 to DR.

</details>

**Example 44 (4c4e).** `L2 U2 B D2 B R2 F R2 F' R2 D2 B' R2 L' D' B' U R D' L2 U2 L2`

EO `F2 U D' B`, RZP `L'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-blue, yellow-orange
- Misoriented corners: white-blue-red showing blue, white-blue-orange showing blue, yellow-green-red showing red, yellow-blue-red showing red
- E-slice edges out of the slice: green-red, green-orange

Reads: 1 pair (on yellow-blue), 0 fake pairs, 0 side pairs, ARM 21, 4b-2 corners, holes on one F/B face (both edges out of the slice have green), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4b corners, 0 or 2 side pairs*). That group is 2.8% of 4c4e, 1,984 cases: 0 with a DR in 4 or less, 160 in 5, 840 in 6, 984 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 F2 L2 F2 D L` (6 moves, good). The whole attempt: `F2 U D' B L' (U2 F2 L2 F2 D L)`, 11 to DR.

</details>

**Example 45 (4c4e).** `R2 D2 B2 D' B2 U' R2 F2 D' R2 F2 U' B2 R2 D' B' L' F' L D' U R B2 D'`

EO `U' B L F`, RZP `L'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-green, yellow-orange
- Misoriented corners: yellow-green-orange showing green, white-green-red showing red, yellow-green-red showing red, yellow-blue-orange showing blue
- E-slice edges out of the slice: green-orange, green-red

Reads: 3 pairs (white-green 1, yellow-orange 2), 0 fake pairs, 1 side pair, ARM 21, 4b-2 corners, holes on one F/B face (both edges out of the slice have green), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 or 4 pairs*). That group is 3.6% of 4c4e, 2,520 cases: 332 with a DR in 4 or less, 522 in 5, 1,160 in 6, 506 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 R2 U F2 D2 R` (6 moves, good). The whole attempt: `U' B L F L' (U2 R2 U F2 D2 R)`, 11 to DR.

</details>

**Example 46 (4c4e).** `U2 D2 F' L2 B2 L2 U2 B' L2 F2 L2 D2 B F2 D2 L' F2 U F D L F U' R U'`

EO `D' F U B'`, RZP `L'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, white-green
- Misoriented corners: yellow-blue-orange showing orange, yellow-blue-red showing blue, white-green-red showing red, yellow-green-red showing green
- E-slice edges out of the slice: green-orange, blue-red

Reads: 1 pair (on white-green), 1 fake pair, 1 side pair, ARM 21, 4b-2 corners, holes diagonal (the edges out of the slice share no colour), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, ARM 21, 4b corners, exactly 1 side pair*). That group is 2.6% of 4c4e, 1,856 cases: 0 with a DR in 4 or less, 24 in 5, 80 in 6, 1,752 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U D R2 L2 U2 F2 U' L` (8 moves, too long). The whole attempt: `D' F U B' L' (U D R2 L2 U2 F2 U' L)`, 13 to DR.

</details>

**Example 47 (4c4e).** `L2 F2 U R2 U' B2 D U2 F2 R2 U B2 F2 U' F' L' B2 F2 U' L D2 L' D U2`

EO `(U2 R L2 D B)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-blue, yellow-orange
- Misoriented corners: white-green-red showing red, white-blue-orange showing blue, yellow-blue-orange showing orange, yellow-green-red showing green
- E-slice edges out of the slice: green-orange, blue-red

Reads: 1 pair (on yellow-blue), 1 fake pair, 0 side pairs, ARM 21, 4a-2 corners, in two columns (two twins), holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4a corners in two columns*). That group is 1.5% of 4c4e, 1,056 cases: 0 with a DR in 4 or less, 64 in 5, 304 in 6, 688 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U F2 U2 B2 U' F2 L` (7 moves, too long). The whole attempt: `(U2 R L2 D B) U F2 U2 B2 U' F2 L`, 12 to DR.

</details>

**Example 48 (4c4e).** `B2 U' R2 U' F2 D' R2 L2 D2 F2 L2 U R2 B2 F' D B' R L' U B' D2 L'`

EO `F' B' U' R' B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, yellow-green
- Misoriented corners: white-green-red showing green, yellow-green-red showing red, white-blue-orange showing orange, white-blue-red showing blue
- E-slice edges out of the slice: green-red, green-orange

Reads: 2 pairs, one on each edge, 1 fake pair, 1 side pair, ARM 22, 4b-2 corners, holes on one F/B face (both edges out of the slice have green), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U' L2 U F2 U L` (6 moves, good). The whole attempt: `F' B' U' R' B' (U' L2 U F2 U L)`, 11 to DR.

</details>

**Example 49 (4c4e).** `R2 D2 L' F2 D2 R2 D2 R' B2 D2 R2 D2 R F2 R' F' L F2 U2 R' D L F2 D'`

EO `(B' L B D2 F)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, white-green
- Misoriented corners: white-green-orange showing orange, white-green-red showing green, yellow-blue-red showing red, yellow-green-orange showing orange
- E-slice edges out of the slice: green-red, blue-orange

Reads: 2 pairs, one on each edge, 1 fake pair, 1 side pair, ARM 31, 4c-1 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `D B2 D R2 U' R` (6 moves, good). The whole attempt: `(B' L B D2 F) D B2 D R2 U' R`, 11 to DR.

</details>

**Example 50 (4c4e).** `D2 F2 L2 F2 R2 U' R2 B2 U2 R2 U' B2 U L' D B' F2 U' B D F2 U'`

EO `(U' B L F2 B')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, yellow-orange
- Misoriented corners: yellow-green-red showing red, yellow-green-orange showing green, yellow-blue-red showing red, yellow-blue-orange showing blue
- E-slice edges out of the slice: green-orange, blue-orange

Reads: 2 pairs, both on yellow-orange (a bar), 0 fake pairs, 2 side pairs, ARM 21, 4a-2 corners, not in two columns, holes on one R/L face (both edges out of the slice have orange), corners 0 white, 4 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on one edge (a bar), holes on one R/L face*). That group is 3.5% of 4c4e, 2,480 cases: 20 with a DR in 4 or less, 244 in 5, 820 in 6, 1,396 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U R2 U F2 R' F2 U2 L` (8 moves, too long). The whole attempt: `(U' B L F2 B') U R2 U F2 R' F2 U2 L`, 13 to DR.

</details>

**Example 51 (4c4e).** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `L' U' L' U B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-green
- Misoriented corners: white-blue-red showing red, yellow-green-red showing red, white-green-red showing red, white-blue-orange showing orange
- E-slice edges out of the slice: green-red, blue-red

Reads: 1 pair (on yellow-green), 2 fake pairs, 0 side pairs, ARM 41, 4b-0 corners, holes on one R/L face (both edges out of the slice have red), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, anything else*). That group is 28.3% of 4c4e, 19,936 cases: 0 with a DR in 4 or less, 56 in 5, 1,152 in 6, 18,728 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `U F2 D R D' F2 D R` (8 moves, too long). The whole attempt: `L' U' L' U B' (U F2 D R D' F2 D R)`, 13 to DR.

</details>

**Example 52 (4c4e).** `R D2 R' F2 R B2 U2 R' U2 R F2 L B' R' D L' U L' D2 B D2 L`

EO `(D L2 B' R F)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, yellow-green
- Misoriented corners: white-green-orange showing orange, yellow-green-red showing green, white-green-red showing red, white-blue-orange showing blue
- E-slice edges out of the slice: green-red, green-orange

Reads: 0 pairs, 2 fake pairs, 1 side pair, ARM 22, 4b-2 corners, holes on one F/B face (both edges out of the slice have green), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*0 pairs, anything else*). That group is 28.9% of 4c4e, 20,424 cases: 0 with a DR in 4 or less, 36 in 5, 748 in 6, 19,640 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `U R B2 L2 U' R' B2 D R` (9 moves, too long). The whole attempt: `(D L2 B' R F) U R B2 L2 U' R' B2 D R`, 14 to DR.

</details>

**Example 53 (4c4e).** `R2 F' D2 R2 F D2 F R2 F' R2 F L2 B' D2 D' F R F2 L' D B R B F2`

EO `F2 R U' L2 B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, white-blue
- Misoriented corners: yellow-green-orange showing orange, white-blue-orange showing blue, white-green-orange showing green, white-blue-red showing red
- E-slice edges out of the slice: green-red, blue-red

Reads: 1 pair (on white-blue), 2 fake pairs, 0 side pairs, ARM 21, 4b-2 corners, holes on one R/L face (both edges out of the slice have red), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4b corners, 0 or 2 side pairs*). That group is 2.8% of 4c4e, 1,984 cases: 0 with a DR in 4 or less, 160 in 5, 840 in 6, 984 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `L2 D2 F2 B2 D L` (6 moves, good). The whole attempt: `F2 R U' L2 B' (L2 D2 F2 B2 D L)`, 11 to DR.

</details>

**Example 54 (4c4e).** `B2 R' D2 B2 R D2 R B2 R' B2 R F2 L' D2 D' R B R2 F' D L B L R2`

EO `(B' D2 L2 U2 B)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, yellow-orange
- Misoriented corners: white-green-red showing green, white-green-orange showing orange, yellow-blue-red showing red, yellow-blue-orange showing blue
- E-slice edges out of the slice: green-red, blue-red

Reads: 1 pair (on yellow-orange), 0 fake pairs, 1 side pair, ARM 21, 4a-2 corners, not in two columns, holes on one R/L face (both edges out of the slice have red), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, ARM 21, 4a corners not in two columns*). That group is 1.4% of 4c4e, 960 cases: 0 with a DR in 4 or less, 0 in 5, 24 in 6, 936 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `D2 R2 U' B2 D F2 L` (7 moves, too long). The whole attempt: `(B' D2 L2 U2 B) D2 R2 U' B2 D F2 L`, 12 to DR.

</details>

**Example 55 (4c4e).** `R2 D' B2 L2 U' L2 D2 R2 F2 D' B2 L2 U F2 U B' R2 U' R L2 B L2 F`

EO `U F R B`, RZP `L`: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, white-red
- Misoriented corners: yellow-green-red showing green, white-green-red showing red, yellow-green-orange showing green, white-blue-orange showing blue
- E-slice edges out of the slice: blue-orange, green-red

Reads: 1 pair (on white-orange), 1 fake pair, 2 side pairs, ARM 10, 4c-1 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, not ARM 21, 2+ side pairs, not 4b corners*). That group is 6.8% of 4c4e, 4,832 cases: 0 with a DR in 4 or less, 48 in 5, 880 in 6, 3,904 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `F2 D2 R2 D R2 D L` (7 moves, too long). The whole attempt: `U F R B L (F2 D2 R2 D R2 D L)`, 12 to DR.

</details>

**Example 56 (4c4e).** `F2 U F2 U' R2 D' L2 U2 R2 L2 U' R2 D' L' F' R2 L2 D' F L U2 B`

EO `L' F' R2 D' F'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, white-orange
- Misoriented corners: white-blue-orange showing blue, yellow-blue-orange showing blue, white-green-orange showing green, yellow-green-orange showing green
- E-slice edges out of the slice: blue-orange, green-orange

Reads: 4 pairs (yellow-orange 2, white-orange 2), 0 fake pairs, 4 side pairs, ARM 00, 4a-0 corners, in two columns (two twins), holes on one R/L face (both edges out of the slice have orange), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 or 4 pairs*). That group is 3.6% of 4c4e, 2,520 cases: 332 with a DR in 4 or less, 522 in 5, 1,160 in 6, 506 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `L` (1 moves, good). The whole attempt: `L' F' R2 D' F' (L)`, 6 to DR.

</details>

**Example 57 (4c4e).** `D2 F2 L2 F2 R2 U' R2 B2 U2 R2 U' B2 U L' D B' F2 U' B D F2 U'`

EO `D' F2 B D2 B`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, white-orange
- Misoriented corners: yellow-blue-red showing blue, white-green-orange showing green, white-blue-red showing blue, yellow-green-orange showing green
- E-slice edges out of the slice: blue-orange, green-orange

Reads: 2 pairs, one on each edge, 0 fake pairs, 2 side pairs, ARM 00, 4a-0 corners, in two columns (two twins), holes on one R/L face (both edges out of the slice have orange), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `R U2 F2 U2 R D2 L` (7 moves, too long). The whole attempt: `D' F2 B D2 B (R U2 F2 U2 R D2 L)`, 12 to DR.

</details>

**Example 58 (4c4e).** `F2 D2 L' R2 U2 R' F2 L U2 R' U2 B2 U2 D2 F' U L2 B' F D F' L`

EO `B2 U D2 B`, RZP `R`: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, yellow-red
- Misoriented corners: white-green-orange showing green, white-green-red showing green, white-blue-orange showing blue, yellow-green-red showing green
- E-slice edges out of the slice: green-orange, blue-orange

Reads: 1 pair (on yellow-red), 1 fake pair, 2 side pairs, ARM 01, 4b-0 corners, holes on one R/L face (both edges out of the slice have orange), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, anything else*). That group is 28.3% of 4c4e, 19,936 cases: 0 with a DR in 4 or less, 56 in 5, 1,152 in 6, 18,728 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `D L2 U F2 B2 R2 U R` (8 moves, too long). The whole attempt: `B2 U D2 B R (D L2 U F2 B2 R2 U R)`, 13 to DR.

</details>

**Example 59 (4c4e).** `U2 L2 F R2 F D2 B D2 B' D2 R2 F' D2 U' R' F' L D R' U2 L2 U2`

EO `F' B2 R' L F'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-red
- Misoriented corners: white-blue-orange showing blue, white-green-red showing green, yellow-green-red showing green, yellow-blue-red showing red
- E-slice edges out of the slice: blue-red, green-red

Reads: 2 pairs, one on each edge, 1 fake pair, 2 side pairs, ARM 10, 4c-1 corners, holes on one R/L face (both edges out of the slice have red), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U L' U R' U' L` (6 moves, good). The whole attempt: `F' B2 R' L F' (U L' U R' U' L)`, 11 to DR.

</details>

**Example 60 (4c4e).** `B D2 F2 L2 U2 D2 F U2 B' L2 F D2 L2 U2 F' D' F' D' R U' B2 D R' F2`

EO `R D2 R L' F`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-green, white-blue
- Misoriented corners: yellow-green-orange showing green, white-blue-orange showing orange, white-green-orange showing green, white-blue-red showing red
- E-slice edges out of the slice: blue-red, green-orange

Reads: 2 pairs, both on white-blue (a bar), 1 fake pair, 2 side pairs, ARM 22, 4b-2 corners, holes diagonal (the edges out of the slice share no colour), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*2 pairs on one edge (a bar), holes not on one R/L face*). That group is 7.0% of 4c4e, 4,960 cases: 0 with a DR in 4 or less, 56 in 5, 840 in 6, 4,064 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `F2 U L D R D' L` (7 moves, too long). The whole attempt: `R D2 R L' F (F2 U L D R D' L)`, 12 to DR.

</details>

**Example 61 (4c4e).** `F2 L2 U F2 R2 F2 L2 D' F2 D2 U R2 L' U R U2 R F U2 F U`

EO `(U D2 F L F')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-green, yellow-orange
- Misoriented corners: white-green-red showing green, yellow-green-red showing green, yellow-blue-orange showing blue, yellow-blue-red showing blue
- E-slice edges out of the slice: green-red, blue-orange

Reads: 1 pair (on yellow-orange), 1 fake pair, 3 side pairs, ARM 01, 4b-0 corners, holes diagonal (the edges out of the slice share no colour), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, anything else*). That group is 28.3% of 4c4e, 19,936 cases: 0 with a DR in 4 or less, 56 in 5, 1,152 in 6, 18,728 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `F2 D L' D' R2 U L` (7 moves, too long). The whole attempt: `(U D2 F L F') F2 D L' D' R2 U L`, 12 to DR.

</details>

**Example 62 (4c4e).** `F2 R F2 U2 B2 R' U2 L2 D2 U2 L D2 R2 F' L2 R U L R U R2 F`

EO `U' L F`, RZP `U' R'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-blue, white-blue
- Misoriented corners: yellow-blue-orange showing blue, white-green-red showing green, yellow-blue-red showing red, yellow-green-red showing red
- E-slice edges out of the slice: green-orange, blue-red

Reads: 1 pair (on yellow-blue), 1 fake pair, 0 side pairs, ARM 22, 4b-2 corners, holes diagonal (the edges out of the slice share no colour), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, anything else*). That group is 28.3% of 4c4e, 19,936 cases: 0 with a DR in 4 or less, 56 in 5, 1,152 in 6, 18,728 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `D L2 U2 D L2 F2 D R` (8 moves, too long). The whole attempt: `U' L F U' R' (D L2 U2 D L2 F2 D R)`, 13 to DR.

</details>

**Example 63 (4c4e).** `D2 B' R2 D2 B R2 B D2 B' D2 B U2 F' R2 R' B D B2 U' R F D F B2`

EO `R2 L B`, RZP `U' L'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, yellow-green
- Misoriented corners: white-blue-orange showing orange, yellow-blue-orange showing blue, white-green-red showing green, white-blue-red showing red
- E-slice edges out of the slice: blue-orange, green-orange

Reads: 2 pairs, both on white-blue (a bar), 0 fake pairs, 1 side pair, ARM 22, 4b-2 corners, holes on one R/L face (both edges out of the slice have orange), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on one edge (a bar), holes on one R/L face*). That group is 3.5% of 4c4e, 2,480 cases: 20 with a DR in 4 or less, 244 in 5, 820 in 6, 1,396 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U' R2 L2 U L2 D' L` (7 moves, too long). The whole attempt: `R2 L B U' L' (U' R2 L2 U L2 D' L)`, 12 to DR.

</details>

**Example 64 (4c4e).** `R2 F2 L2 B2 D' F2 D R2 U2 B2 R2 D' U2 F' L' R2 D L R B L' D' U'`

EO `(L' U F' R B)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-blue
- Misoriented corners: yellow-green-orange showing orange, white-blue-red showing red, yellow-blue-red showing blue, white-green-orange showing green
- E-slice edges out of the slice: green-orange, blue-red

Reads: 1 pair (on white-orange), 1 fake pair, 2 side pairs, ARM 21, 4a-2 corners, in two columns (two twins), holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4a corners in two columns*). That group is 1.5% of 4c4e, 1,056 cases: 0 with a DR in 4 or less, 64 in 5, 304 in 6, 688 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `R' U2 L F2 R' D L` (7 moves, too long). The whole attempt: `(L' U F' R B) R' U2 L F2 R' D L`, 12 to DR.

</details>

**Example 65 (4c4e).** `R2 L2 D F2 U F2 U R2 F2 L2 B2 D B' U B R' D' F' D' U' B U'`

EO `(F L2 B L2 B)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, white-orange
- Misoriented corners: white-blue-red showing red, white-green-red showing red, yellow-blue-red showing blue, white-blue-orange showing orange
- E-slice edges out of the slice: green-red, blue-orange

Reads: 2 pairs, both on white-blue (a bar), 1 fake pair, 0 side pairs, ARM 31, 4c-1 corners, holes diagonal (the edges out of the slice share no colour), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*2 pairs on one edge (a bar), holes not on one R/L face*). That group is 7.0% of 4c4e, 4,960 cases: 0 with a DR in 4 or less, 56 in 5, 840 in 6, 4,064 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `B2 U2 B2 D B2 D' R` (7 moves, too long). The whole attempt: `(F L2 B L2 B) B2 U2 B2 D B2 D' R`, 12 to DR.

</details>

**Example 66 (4c4e).** `L2 F2 D R2 D' F2 U B2 L2 D R2 U' F2 U' B2 F' L' D R' D L' D B2 D2 U2`

EO `(U R F2 R2 B)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-red, yellow-green
- Misoriented corners: white-blue-red showing red, white-green-orange showing green, yellow-blue-orange showing orange, yellow-green-red showing green
- E-slice edges out of the slice: green-red, blue-orange

Reads: 1 pair (on yellow-red), 1 fake pair, 1 side pair, ARM 21, 4d-2 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4d corners*). That group is 0.82% of 4c4e, 576 cases: 32 with a DR in 4 or less, 96 in 5, 384 in 6, 64 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U2 R D2 L2 D B2 L` (7 moves, too long). The whole attempt: `(U R F2 R2 B) U2 R D2 L2 D B2 L`, 12 to DR.

</details>

**Example 67 (4c4e).** `R2 B2 D2 B2 R2 D2 F2 U B2 D' F2 U2 R' B L D2 L B2 D' U F' U2`

EO `(F R2 U F B')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, yellow-red
- Misoriented corners: white-green-red showing green, white-green-orange showing green, yellow-green-orange showing green, yellow-blue-orange showing blue
- E-slice edges out of the slice: green-red, green-orange

Reads: 0 pairs, 0 fake pairs, 3 side pairs, ARM 01, 4b-0 corners, holes on one F/B face (both edges out of the slice have green), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, no fake pairs, corners 2 and 2 in the layers*). That group is 0.82% of 4c4e, 576 cases: 14 with a DR in 4 or less, 24 in 5, 88 in 6, 450 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `U F2 D' L2 D B2 R` (7 moves, too long). The whole attempt: `(F R2 U F B') U F2 D' L2 D B2 R`, 12 to DR.

</details>

**Example 68 (4c4e).** `B D2 F2 L2 U2 D2 F U2 B' L2 F D2 L2 U2 F' D' F' D' R U' B2 D R' F2`

EO `U' L U' B`, RZP `L`: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-blue, white-blue
- Misoriented corners: yellow-blue-orange showing blue, yellow-green-orange showing green, white-blue-red showing red, white-blue-orange showing orange
- E-slice edges out of the slice: green-red, blue-red

Reads: 2 pairs, both on white-blue (a bar), 1 fake pair, 0 side pairs, ARM 22, 4b-2 corners, holes on one R/L face (both edges out of the slice have red), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on one edge (a bar), holes on one R/L face*). That group is 3.5% of 4c4e, 2,480 cases: 20 with a DR in 4 or less, 244 in 5, 820 in 6, 1,396 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `D L2 U R2 L2 U R` (7 moves, too long). The whole attempt: `U' L U' B L (D L2 U R2 L2 U R)`, 12 to DR.

</details>

**Example 69 (4c4e).** `L2 D2 F2 U B2 R2 U B2 F2 D R2 U2 R2 R' F' U B U2 L' F' R' B'`

EO `(L' F' B')`, RZP `(R L)`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-green
- Misoriented corners: yellow-blue-orange showing orange, yellow-blue-red showing blue, yellow-green-red showing green, white-blue-orange showing orange
- E-slice edges out of the slice: blue-red, green-red

Reads: 2 pairs, both on yellow-red (a bar), 0 fake pairs, 2 side pairs, ARM 21, 4b-2 corners, holes on one R/L face (both edges out of the slice have red), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on one edge (a bar), holes on one R/L face*). That group is 3.5% of 4c4e, 2,480 cases: 20 with a DR in 4 or less, 244 in 5, 820 in 6, 1,396 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `L2 U2 L2 U R` (5 moves, good). The whole attempt: `(L' F' B' R L) L2 U2 L2 U R`, 10 to DR.

</details>

**Example 70 (4c4e).** `U2 F D2 R2 D2 U2 B' U2 B2 L2 B L2 B R2 F' U' B R D' L2 B' L' B' U B2`

EO `R L B`, RZP `U' R'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-green
- Misoriented corners: white-green-red showing green, yellow-blue-orange showing blue, white-blue-red showing red, white-blue-orange showing orange
- E-slice edges out of the slice: green-orange, blue-orange

Reads: 1 pair (on white-red), 1 fake pair, 1 side pair, ARM 21, 4b-2 corners, holes on one R/L face (both edges out of the slice have orange), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, ARM 21, 4b corners, exactly 1 side pair*). That group is 2.6% of 4c4e, 1,856 cases: 0 with a DR in 4 or less, 24 in 5, 80 in 6, 1,752 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 L U2 F2 L U L` (7 moves, too long). The whole attempt: `R L B U' R' (U2 L U2 F2 L U L)`, 12 to DR.

</details>

**Example 71 (4c4e).** `F2 U2 R F2 D2 F2 U2 L' F2 L2 R D2 U' R D R2 D F R2 F R`

EO `R' F2 B U2 B`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-green
- Misoriented corners: yellow-blue-orange showing blue, white-green-red showing red, yellow-green-red showing red, white-blue-orange showing blue
- E-slice edges out of the slice: blue-red, blue-orange

Reads: 1 pair (on white-green), 1 fake pair, 2 side pairs, ARM 21, 4a-2 corners, in two columns (two twins), holes on one F/B face (both edges out of the slice have blue), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4a corners in two columns*). That group is 1.5% of 4c4e, 1,056 cases: 0 with a DR in 4 or less, 64 in 5, 304 in 6, 688 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `F2 B2 U R2 D B2 R` (7 moves, too long). The whole attempt: `R' F2 B U2 B (F2 B2 U R2 D B2 R)`, 12 to DR.

</details>

**Example 72 (4c4e).** `L2 F2 D R2 D' F2 U B2 L2 D R2 U' F2 U' B2 F' L' D R' D L' D B2 D2 U2`

EO `D B`, RZP `U' D2 R'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, yellow-green
- Misoriented corners: yellow-blue-red showing blue, yellow-green-orange showing orange, yellow-green-red showing green, white-blue-red showing red
- E-slice edges out of the slice: green-orange, blue-red

Reads: 2 pairs, one on each edge, 1 fake pair, 1 side pair, ARM 22, 4b-2 corners, holes diagonal (the edges out of the slice share no colour), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U' F2 U2 D' R2 U R` (7 moves, too long). The whole attempt: `D B U' D2 R' (U' F2 U2 D' R2 U R)`, 12 to DR.

</details>

**Example 73 (4c4e).** `L2 U2 L2 D2 F2 D2 F2 B' D2 F' D2 R2 F' D' L' U2 F R2 D' L U' F2 B2`

EO `R L B'`, RZP `D2 R`: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-green, yellow-red
- Misoriented corners: yellow-green-red showing green, white-green-red showing red, white-blue-red showing red, yellow-blue-red showing blue
- E-slice edges out of the slice: blue-orange, green-red

Reads: 3 pairs (white-green 1, yellow-red 2), 0 fake pairs, 1 side pair, ARM 21, 4a-2 corners, in two columns (two twins), holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 or 4 pairs*). That group is 3.6% of 4c4e, 2,520 cases: 332 with a DR in 4 or less, 522 in 5, 1,160 in 6, 506 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `F2 D' F2 U F2 L` (6 moves, good). The whole attempt: `R L B' D2 R (F2 D' F2 U F2 L)`, 11 to DR.

</details>

**Example 74 (4c4e).** `B2 L' U2 F2 R' F2 L2 B2 D2 L' U2 F2 R D2 R U' B2 R' B F2 U F2 D`

EO `B U' D' B`, RZP `R'`: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, white-blue
- Misoriented corners: yellow-green-orange showing green, yellow-blue-red showing red, white-green-red showing green, white-blue-orange showing orange
- E-slice edges out of the slice: green-orange, blue-red

Reads: 1 pair (on white-blue), 1 fake pair, 1 side pair, ARM 21, 4d-2 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4d corners*). That group is 0.82% of 4c4e, 576 cases: 32 with a DR in 4 or less, 96 in 5, 384 in 6, 64 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `F2 D2 B2 D F2 L` (6 moves, good). The whole attempt: `B U' D' B R' (F2 D2 B2 D F2 L)`, 11 to DR.

</details>

**Example 75 (4c4e).** `U2 R2 D' F2 R2 U2 R2 U' B2 R2 U2 R2 U F2 U' F' D F2 L2 U' R D F2 R'`

EO `(L D R2 L2 F)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, yellow-red
- Misoriented corners: yellow-green-red showing green, yellow-blue-red showing blue, white-green-orange showing green, white-blue-orange showing blue
- E-slice edges out of the slice: blue-red, green-red

Reads: 2 pairs, both on yellow-red (a bar), 0 fake pairs, 2 side pairs, ARM 00, 4a-0 corners, not in two columns, holes on one R/L face (both edges out of the slice have red), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on one edge (a bar), holes on one R/L face*). That group is 3.5% of 4c4e, 2,480 cases: 20 with a DR in 4 or less, 244 in 5, 820 in 6, 1,396 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U2 R2 F2 U2 B2 L` (6 moves, good). The whole attempt: `(L D R2 L2 F) U2 R2 F2 U2 B2 L`, 11 to DR.

</details>

**Example 76 (4c4e).** `F2 U2 L2 U2 R2 B' R2 D2 B2 R2 B' D2 B L' F D' U2 B' D F U2 B'`

EO `F B' L D' B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-green, white-orange
- Misoriented corners: yellow-green-red showing green, white-green-orange showing orange, white-blue-orange showing blue, white-green-red showing red
- E-slice edges out of the slice: blue-red, green-orange

Reads: 1 pair (on white-orange), 2 fake pairs, 0 side pairs, ARM 21, 4b-2 corners, holes diagonal (the edges out of the slice share no colour), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4b corners, 0 or 2 side pairs*). That group is 2.8% of 4c4e, 1,984 cases: 0 with a DR in 4 or less, 160 in 5, 840 in 6, 984 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `F2 U2 R2 L2 U R` (6 moves, good). The whole attempt: `F B' L D' B' (F2 U2 R2 L2 U R)`, 11 to DR.

</details>

**Example 77 (4c4e).** `F2 U2 R F2 D2 F2 U2 L' F2 L2 R D2 U' R D R2 D F R2 F R`

EO `R' L2 F' R2 F'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-green, yellow-red
- Misoriented corners: white-green-red showing red, yellow-green-red showing red, white-blue-red showing blue, white-blue-orange showing blue
- E-slice edges out of the slice: blue-red, blue-orange

Reads: 1 pair (on white-green), 1 fake pair, 2 side pairs, ARM 21, 4b-2 corners, holes on one F/B face (both edges out of the slice have blue), corners 3 white, 1 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4b corners, 0 or 2 side pairs*). That group is 2.8% of 4c4e, 1,984 cases: 0 with a DR in 4 or less, 160 in 5, 840 in 6, 984 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `B2 U2 R2 B2 D' R` (6 moves, good). The whole attempt: `R' L2 F' R2 F' (B2 U2 R2 B2 D' R)`, 11 to DR.

</details>

**Example 78 (4c4e).** `D2 F D2 L2 U2 F' L2 B2 R2 L2 B R2 F2 D' B2 F L B F L F2 D`

EO `D2 L' D' F' B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-green
- Misoriented corners: yellow-green-orange showing orange, yellow-blue-red showing blue, white-green-orange showing green, yellow-green-red showing red
- E-slice edges out of the slice: green-orange, blue-red

Reads: 1 pair (on yellow-red), 2 fake pairs, 2 side pairs, ARM 21, 4b-2 corners, holes diagonal (the edges out of the slice share no colour), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4b corners, 0 or 2 side pairs*). That group is 2.8% of 4c4e, 1,984 cases: 0 with a DR in 4 or less, 160 in 5, 840 in 6, 984 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `F2 U2 R2 L2 D R` (6 moves, good). The whole attempt: `D2 L' D' F' B' (F2 U2 R2 L2 D R)`, 11 to DR.

</details>

**Example 79 (4c4e).** `R2 D2 L' F2 D2 R2 D2 R' B2 D2 R2 D2 R F2 R' F' L F2 U2 R' D L F2 D'`

EO `(D' L D' F)`, RZP `(L')`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, white-green
- Misoriented corners: yellow-blue-red showing blue, white-blue-red showing blue, yellow-green-red showing red, yellow-green-orange showing orange
- E-slice edges out of the slice: blue-orange, green-orange

Reads: 1 pair (on white-red), 0 fake pairs, 0 side pairs, ARM 21, 4b-2 corners, holes on one R/L face (both edges out of the slice have orange), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4b corners, 0 or 2 side pairs*). That group is 2.8% of 4c4e, 1,984 cases: 0 with a DR in 4 or less, 160 in 5, 840 in 6, 984 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U' D' F2 B2 L2 D' R` (7 moves, too long). The whole attempt: `(D' L D' F L') U' D' F2 B2 L2 D' R`, 12 to DR.

</details>

**Example 80 (4c4e).** `F2 R2 D' U2 L2 U' F2 D L2 U' L2 B2 L2 R2 F' L D2 B' F R F' D`

EO `D L D2 R2 B`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-green, white-green
- Misoriented corners: yellow-green-orange showing orange, white-blue-red showing red, yellow-green-red showing red, white-green-red showing red
- E-slice edges out of the slice: green-orange, green-red

Reads: 3 pairs (yellow-green 2, white-green 1), 0 fake pairs, 0 side pairs, ARM 42, 4b-0 corners, holes on one F/B face (both edges out of the slice have green), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 or 4 pairs*). That group is 3.6% of 4c4e, 2,520 cases: 332 with a DR in 4 or less, 522 in 5, 1,160 in 6, 506 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `R U R B2 D' L` (6 moves, good). The whole attempt: `D L D2 R2 B (R U R B2 D' L)`, 11 to DR.

</details>

**Example 81 (4c4e).** `R2 U R2 F2 L2 U' F2 D2 B2 F2 D B2 U2 R' D2 U F D U F U2 R`

EO `(B' L' U B')`, RZP `(L)`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, white-green
- Misoriented corners: white-green-orange showing green, white-blue-red showing red, white-green-red showing red, white-blue-orange showing blue
- E-slice edges out of the slice: green-red, blue-red

Reads: 1 pair (on white-green), 3 fake pairs, 0 side pairs, ARM 21, 4a-2 corners, not in two columns, holes on one R/L face (both edges out of the slice have red), corners 4 white, 0 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, ARM 21, 4a corners not in two columns*). That group is 1.4% of 4c4e, 960 cases: 0 with a DR in 4 or less, 0 in 5, 24 in 6, 936 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U R U2 R U2 R U' R` (8 moves, too long). The whole attempt: `(B' L' U B' L) U R U2 R U2 R U' R`, 13 to DR.

</details>

**Example 82 (4c4e).** `R2 U R2 F2 L2 U' F2 D2 B2 F2 D B2 U2 R' D2 U F D U F U2 R`

EO `(B2 D' L2 D' B)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-green
- Misoriented corners: white-green-red showing green, white-blue-orange showing orange, yellow-blue-red showing red, yellow-green-orange showing green
- E-slice edges out of the slice: green-orange, blue-red

Reads: 1 pair (on white-red), 1 fake pair, 1 side pair, ARM 21, 4d-2 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 4d corners*). That group is 0.82% of 4c4e, 576 cases: 32 with a DR in 4 or less, 96 in 5, 384 in 6, 64 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U2 R2 U2 L2 D B2 R` (7 moves, too long). The whole attempt: `(B2 D' L2 D' B) U2 R2 U2 L2 D B2 R`, 12 to DR.

</details>

**Example 83 (4c4e).** `B2 L2 U2 F L2 F' L2 B' R2 B R2 U2 R' D2 B D2 F L U' L' D'`

EO `F2 B D' L B'`, no RZP needed: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-orange
- Misoriented corners: yellow-blue-orange showing blue, yellow-green-red showing red, white-blue-orange showing blue, white-blue-red showing blue
- E-slice edges out of the slice: green-red, blue-orange

Reads: 2 pairs, one on each edge, 0 fake pairs, 2 side pairs, ARM 10, 4c-1 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U L2 U R2 B2 D L` (7 moves, too long). The whole attempt: `F2 B D' L B' (U L2 U R2 B2 D L)`, 12 to DR.

</details>

**Example 84 (4c4e).** `B2 U' R2 B2 U R2 U B2 U' B2 U F2 D' R2 R' U B U2 F' R D B D U2`

EO `(F' L2 B)`, RZP `(R' L)`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, white-red
- Misoriented corners: yellow-blue-red showing red, white-blue-orange showing blue, white-blue-red showing blue, yellow-green-orange showing green
- E-slice edges out of the slice: green-red, blue-orange

Reads: 2 pairs, one on each edge, 0 fake pairs, 1 side pair, ARM 10, 4c-1 corners, holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs on two edges*). That group is 11.9% of 4c4e, 8,400 cases: 180 with a DR in 4 or less, 1,156 in 5, 3,192 in 6, 3,872 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `R B2 R U' R D2 R` (7 moves, too long). The whole attempt: `(F' L2 B R' L) R B2 R U' R D2 R`, 12 to DR.

</details>

**Example 85 (4c4e).** `L2 B2 R2 D' R2 D' L2 D' L2 R2 U2 B2 U' F2 F' R B D L' D' B F D' R2`

EO `(F B L' F' B)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-green, white-green
- Misoriented corners: white-blue-orange showing blue, white-blue-red showing blue, yellow-blue-red showing red, yellow-blue-orange showing orange
- E-slice edges out of the slice: blue-orange, green-red

Reads: 0 pairs, 0 fake pairs, 1 side pair, ARM 22, 4a-2 corners, in two columns (two twins), holes diagonal (the edges out of the slice share no colour), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, no fake pairs, corners 2 and 2 in the layers*). That group is 0.82% of 4c4e, 576 cases: 14 with a DR in 4 or less, 24 in 5, 88 in 6, 450 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `L2 U' L2 D B2 R` (6 moves, good). The whole attempt: `(F B L' F' B) L2 U' L2 D B2 R`, 11 to DR.

</details>

**Example 86 (4c4e).** `U2 R2 D' F2 R2 U2 R2 U' B2 R2 U2 R2 U F2 U' F' D F2 L2 U' R D F2 R'`

EO `(L2 U L' D' B')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, yellow-red
- Misoriented corners: yellow-green-orange showing orange, yellow-blue-orange showing orange, yellow-green-red showing green, white-green-red showing green
- E-slice edges out of the slice: blue-red, blue-orange

Reads: 1 pair (on yellow-red), 2 fake pairs, 0 side pairs, ARM 20, 4b-2 corners, holes on one F/B face (both edges out of the slice have blue), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, anything else*). That group is 28.3% of 4c4e, 19,936 cases: 0 with a DR in 4 or less, 56 in 5, 1,152 in 6, 18,728 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `U R2 U L' D F2 D' L` (8 moves, too long). The whole attempt: `(L2 U L' D' B') U R2 U L' D F2 D' L`, 13 to DR.

</details>

**Example 87 (4c4e).** `L2 B' R2 B2 R2 D2 F L2 U2 F' U2 R2 F2 U' B2 L' B U F' L2 D' R' L'`

EO `(L D2 B' R F)`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-green
- Misoriented corners: yellow-blue-orange showing blue, yellow-green-red showing red, yellow-blue-red showing blue, yellow-green-orange showing orange
- E-slice edges out of the slice: green-red, green-orange

Reads: 2 pairs, both on yellow-green (a bar), 0 fake pairs, 0 side pairs, ARM 21, 4a-2 corners, not in two columns, holes on one F/B face (both edges out of the slice have green), corners 0 white, 4 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*2 pairs on one edge (a bar), holes not on one R/L face*). That group is 7.0% of 4c4e, 4,960 cases: 0 with a DR in 4 or less, 56 in 5, 840 in 6, 4,064 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U R2 U B2 U2 R2 D' L` (8 moves, too long). The whole attempt: `(L D2 B' R F) U R2 U B2 U2 R2 D' L`, 13 to DR.

</details>

**Example 88 (4c4e).** `F2 R2 U L2 D2 F2 U R2 U' R2 U B2 R2 R' B D B R' D B' R' F' D'`

EO `(F D' L' F B')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-red
- Misoriented corners: yellow-blue-orange showing orange, white-green-orange showing green, yellow-green-red showing green, yellow-green-orange showing green
- E-slice edges out of the slice: green-orange, blue-red

Reads: 1 pair (on yellow-red), 0 fake pairs, 2 side pairs, ARM 10, 4c-1 corners, holes diagonal (the edges out of the slice share no colour), corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, not ARM 21, 2+ side pairs, not 4b corners*). That group is 6.8% of 4c4e, 4,832 cases: 0 with a DR in 4 or less, 48 in 5, 880 in 6, 3,904 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `D' R2 F2 L2 B2 U' R` (7 moves, too long). The whole attempt: `(F D' L' F B') D' R2 F2 L2 B2 U' R`, 12 to DR.

</details>

**Example 89 (4c4e).** `F2 D' B2 U2 B2 L2 F2 L2 F2 U' B2 D' B2 U2 L' U' F D2 L' R D L' B' U'`

EO `(D' R2 F' D2 B')`, no RZP needed, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: yellow-blue, white-red
- Misoriented corners: yellow-green-orange showing orange, yellow-green-red showing red, white-green-orange showing green, white-blue-orange showing blue
- E-slice edges out of the slice: green-orange, blue-orange

Reads: 0 pairs, 0 fake pairs, 2 side pairs, ARM 21, 4b-2 corners, holes on one R/L face (both edges out of the slice have orange), corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, no fake pairs, corners 2 and 2 in the layers*). That group is 0.82% of 4c4e, 576 cases: 14 with a DR in 4 or less, 24 in 5, 88 in 6, 450 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `D' F2 B2 R` (4 moves, good). The whole attempt: `(D' R2 F' D2 B') D' F2 B2 R`, 9 to DR.

</details>

**Example 90 (4c4e).** `B2 L2 U2 F L2 F' L2 B' R2 B R2 U2 R' D2 B D2 F L U' L' D'`

EO `(U2 R' L' B')`, RZP `(R')`, on the inverse scramble: 4c4e in 5.

What you see:

- U/D edges in the E slice: white-green, white-orange
- Misoriented corners: white-blue-orange showing blue, white-green-orange showing orange, white-blue-red showing blue, white-green-red showing red
- E-slice edges out of the slice: blue-red, blue-orange

Reads: 3 pairs (white-green 2, white-orange 1), 1 fake pair, 2 side pairs, ARM 21, 4a-2 corners, not in two columns, holes on one F/B face (both edges out of the slice have blue), corners 4 white, 0 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 or 4 pairs*). That group is 3.6% of 4c4e, 2,520 cases: 332 with a DR in 4 or less, 522 in 5, 1,160 in 6, 506 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U L' U2 F2 L2 D R` (7 moves, too long). The whole attempt: `(U2 R' L' B' R') U L' U2 F2 L2 D R`, 12 to DR.

</details>

## 4c2e: examples 91–120

The 4c2e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 4c2e once; 18.7% for 4c2e as a whole):

| What you read | Verdict | Share of 4c2e | Sub-7 |
|---|---|---|---|
| 2 pairs (a bar) | switch | 7.1% | 60.0% |
| 1 pair and a side pair | switch | 15.1% | 55.5% |
| 0 pairs, JZP (ARM 00) with 4b corners | switch | 0.71% | 66.7% |
| 1 pair, no side pair, 4b-0 corners | switch | 1.8% | 43.3% |
| 1 pair, no side pair, 4a-2 corners | if you have time | 2.5% | 23.8% |
| 1 pair, no side pair, ARM 31 | if you have time | 4.3% | 19.4% |
| 1 pair, anything else | skip | 12.0% | 9.4% |
| 0 pairs, anything else | skip | 56.4% | 3.9% |

**Example 91 (4c2e).** `F2 R F2 U2 B2 R' U2 L2 D2 U2 L D2 R2 F' L2 R U L R U R2 F`

EO `U' B2 L F'`, RZP `R`: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-green
- Misoriented corners: white-green-orange showing green, yellow-green-red showing red, white-blue-red showing red, white-green-red showing red
- E-slice edges out of the slice: green-orange

Reads: 1 pair, 1 side pair, ARM 31, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair and a side pair*). That group is 15.1% of 4c2e, 2,032 cases: 8 with a DR in 4 or less, 216 in 5, 904 in 6, 904 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `D2 R2 D' R F2 R` (6 moves, good). The whole attempt: `U' B2 L F' R (D2 R2 D' R F2 R)`, 11 to DR.

</details>

**Example 92 (4c2e).** `U2 R2 F D2 F' R2 B L2 U2 F D2 B' R2 B' L2 R' U' F D' F U' F L2 F2 B2`

EO `L F B U' B'`, no RZP needed: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-blue
- Misoriented corners: white-blue-red showing red, white-blue-orange showing orange, yellow-blue-red showing red, yellow-blue-orange showing orange
- E-slice edges out of the slice: green-red

Reads: 2 pairs (a bar), 0 side pairs, ARM 41, 4a-4 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs (a bar)*). That group is 7.1% of 4c2e, 960 cases: 64 with a DR in 4 or less, 152 in 5, 360 in 6, 384 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U D R' F2 B2 R B2 R` (8 moves, too long). The whole attempt: `L F B U' B' (U D R' F2 B2 R B2 R)`, 13 to DR.

</details>

**Example 93 (4c2e).** `F2 U2 L2 U2 R2 B' R2 D2 B2 R2 B' D2 B L' F D' U2 B' D F U2 B'`

EO `(F2 L' F R2 B')`, no RZP needed, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-blue
- Misoriented corners: white-green-red showing red, white-blue-orange showing blue, yellow-green-orange showing orange, white-blue-red showing red
- E-slice edges out of the slice: blue-orange

Reads: 1 pair, 1 side pair, ARM 31, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair and a side pair*). That group is 15.1% of 4c2e, 2,032 cases: 8 with a DR in 4 or less, 216 in 5, 904 in 6, 904 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `L2 U R' F2 R` (5 moves, good). The whole attempt: `(F2 L' F R2 B') L2 U R' F2 R`, 10 to DR.

</details>

**Example 94 (4c2e).** `L2 R2 F2 D2 B' D2 B L2 D2 B R2 U2 F' U' R D' R D F' B2 D B2`

EO `L' U L F2 B`, no RZP needed: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-orange
- Misoriented corners: white-blue-red showing blue, yellow-blue-red showing blue, white-green-orange showing green, white-blue-orange showing blue
- E-slice edges out of the slice: blue-orange

Reads: 0 pairs, 1 side pair, ARM 00, 4b-0 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, JZP (ARM 00) with 4b corners*). That group is 0.71% of 4c2e, 96 cases: 0 with a DR in 4 or less, 8 in 5, 56 in 6, 32 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `B2 U2 F2 R D2 R` (6 moves, good). The whole attempt: `L' U L F2 B (B2 U2 F2 R D2 R)`, 11 to DR.

</details>

**Example 95 (4c2e).** `U2 R2 U' L2 F2 D' L2 R2 F2 L2 D2 U' R' D2 R B' D B L2 R2 U'`

EO `U' D' F' U F'`, no RZP needed: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-blue
- Misoriented corners: white-blue-red showing red, yellow-blue-orange showing orange, yellow-blue-red showing red, yellow-green-orange showing orange
- E-slice edges out of the slice: green-orange

Reads: 1 pair, 0 side pairs, ARM 41, 4b-0 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, no side pair, 4b-0 corners*). That group is 1.8% of 4c2e, 240 cases: 0 with a DR in 4 or less, 0 in 5, 104 in 6, 136 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `L2 U D R B2 R` (6 moves, good). The whole attempt: `U' D' F' U F' (L2 U D R B2 R)`, 11 to DR.

</details>

**Example 96 (4c2e).** `L2 D2 B' F2 U2 F' L2 B U2 F' U2 R2 U2 D2 L' U B2 R' L D L' B`

EO `(L2 B U F)`, RZP `(R')`, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: yellow-green-orange showing orange, white-blue-orange showing orange, yellow-blue-red showing blue, white-green-orange showing orange
- E-slice edges out of the slice: green-red

Reads: 1 pair, 0 side pairs, ARM 31, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, no side pair, ARM 31*). That group is 4.3% of 4c2e, 576 cases: 0 with a DR in 4 or less, 0 in 5, 112 in 6, 464 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U' R F2 U R F2 R` (7 moves, too long). The whole attempt: `(L2 B U F R') U' R F2 U R F2 R`, 12 to DR.

</details>

**Example 97 (4c2e).** `F2 R F2 R' D2 L' U2 R2 D2 U2 R' D2 L' U' F' D2 U2 L' F U R2 B`

EO `U' D' R F`, RZP `R'`: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-red
- Misoriented corners: white-green-orange showing orange, yellow-green-orange showing green, white-blue-orange showing orange, yellow-blue-red showing red
- E-slice edges out of the slice: green-orange

Reads: 0 pairs, 1 side pair, ARM 30, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*0 pairs, anything else*). That group is 56.4% of 4c2e, 7,584 cases: 0 with a DR in 4 or less, 0 in 5, 296 in 6, 7,288 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `L' D F2 B2 R2 U' R` (7 moves, too long). The whole attempt: `U' D' R F R' (L' D F2 B2 R2 U' R)`, 12 to DR.

</details>

**Example 98 (4c2e).** `L2 B' R2 F U2 F' D2 F L2 R2 U2 B2 R' U2 B' R' U' L U2 B' L B'`

EO ``, RZP `D' R U D2 L`: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-red
- Misoriented corners: yellow-blue-orange showing blue, white-green-orange showing green, white-green-red showing green, yellow-green-orange showing green
- E-slice edges out of the slice: green-red

Reads: 0 pairs, 1 side pair, ARM 00, 4b-0 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, JZP (ARM 00) with 4b corners*). That group is 0.71% of 4c2e, 96 cases: 0 with a DR in 4 or less, 8 in 5, 56 in 6, 32 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 F2 R B2 U2 D2 L` (7 moves, too long). The whole attempt: `D' R U D2 L (U2 F2 R B2 U2 D2 L)`, 12 to DR.

</details>

**Example 99 (4c2e).** `L2 F2 U2 F2 D2 R' D2 B2 R2 D2 R' B2 R U' L B' F2 R' B L F2 R'`

EO `D2 F' U2 F`, RZP `R'`: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: yellow-blue-red showing blue, yellow-blue-orange showing blue, white-green-orange showing orange, white-blue-red showing blue
- E-slice edges out of the slice: green-red

Reads: 1 pair, 0 side pairs, ARM 11, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, anything else*). That group is 12.0% of 4c2e, 1,616 cases: 0 with a DR in 4 or less, 0 in 5, 152 in 6, 1,464 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U' R' B2 D R B2 R` (7 moves, too long). The whole attempt: `D2 F' U2 F R' (U' R' B2 D R B2 R)`, 12 to DR.

</details>

**Example 100 (4c2e).** `L2 F2 L2 B' R2 D2 F2 D2 F2 R2 F R2 L2 F L' D' R2 D' L F2 D B L`

EO `R' F2 R L B'`, no RZP needed: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-red
- Misoriented corners: white-blue-orange showing blue, white-green-orange showing green, yellow-blue-orange showing blue, white-green-red showing green
- E-slice edges out of the slice: blue-red

Reads: 1 pair, 0 side pairs, ARM 00, 4b-0 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, no side pair, 4b-0 corners*). That group is 1.8% of 4c2e, 240 cases: 0 with a DR in 4 or less, 0 in 5, 104 in 6, 136 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 D2 F2 D2 R' U2 R` (7 moves, too long). The whole attempt: `R' F2 R L B' (U2 D2 F2 D2 R' U2 R)`, 12 to DR.

</details>

**Example 101 (4c2e).** `U2 R2 F' B2 L2 B' U2 F L2 B' L2 D2 L2 R2 U' L F2 D' U R U' F`

EO `(U2 F' L B')`, RZP `(R')`, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-orange
- Misoriented corners: white-green-orange showing green, white-green-red showing green, yellow-green-orange showing green, yellow-blue-red showing red
- E-slice edges out of the slice: green-orange

Reads: 1 pair, 2 side pairs, ARM 10, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair and a side pair*). That group is 15.1% of 4c2e, 2,032 cases: 8 with a DR in 4 or less, 216 in 5, 904 in 6, 904 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U2 L' B2 U R D2 R` (7 moves, too long). The whole attempt: `(U2 F' L B' R') U2 L' B2 U R D2 R`, 12 to DR.

</details>

**Example 102 (4c2e).** `B2 L2 U2 L2 D2 F' D2 R2 F2 D2 F' R2 F U' B R' L2 F' R B L2 F'`

EO `(B2 U' F L2 B')`, no RZP needed, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-red
- Misoriented corners: yellow-blue-orange showing blue, white-blue-red showing red, white-green-red showing green, yellow-green-orange showing orange
- E-slice edges out of the slice: green-orange

Reads: 1 pair, 0 side pairs, ARM 20, 4a-2 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, no side pair, 4a-2 corners*). That group is 2.5% of 4c2e, 336 cases: 0 with a DR in 4 or less, 0 in 5, 80 in 6, 256 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `B2 U2 D F2 R U2 R` (7 moves, too long). The whole attempt: `(B2 U' F L2 B') B2 U2 D F2 R U2 R`, 12 to DR.

</details>

**Example 103 (4c2e).** `U2 R U2 R' D2 B2 L2 U2 F2 L' F2 D2 R D' R D R' B L B' L F`

EO `F D B' R2 B`, no RZP needed: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-orange
- Misoriented corners: white-green-red showing green, white-green-orange showing green, yellow-green-red showing green, white-blue-orange showing blue
- E-slice edges out of the slice: green-red

Reads: 0 pairs, 2 side pairs, ARM 00, 4b-0 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, JZP (ARM 00) with 4b corners*). That group is 0.71% of 4c2e, 96 cases: 0 with a DR in 4 or less, 8 in 5, 56 in 6, 32 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 F2 B2 D2 R F2 R` (7 moves, too long). The whole attempt: `F D B' R2 B (U2 F2 B2 D2 R F2 R)`, 12 to DR.

</details>

**Example 104 (4c2e).** `R2 B R2 B' D2 F' U2 B2 D2 U2 B' D2 F' U' R' D2 U2 F' R U B2 L`

EO `(U2 D2 L F')`, RZP `(L')`, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: yellow-green-orange showing green, yellow-green-red showing green, white-blue-orange showing blue, white-green-red showing red
- E-slice edges out of the slice: green-red

Reads: 1 pair, 1 side pair, ARM 11, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair and a side pair*). That group is 15.1% of 4c2e, 2,032 cases: 8 with a DR in 4 or less, 216 in 5, 904 in 6, 904 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U2 R' D R2 U R` (6 moves, good). The whole attempt: `(U2 D2 L F' L') U2 R' D R2 U R`, 11 to DR.

</details>

**Example 105 (4c2e).** `L2 F2 U2 F2 D2 R' D2 B2 R2 D2 R' B2 R U' L B' F2 R' B L F2 R'`

EO `F2 B L2 B`, RZP `L`: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: white-blue-red showing blue, white-blue-orange showing blue, yellow-blue-red showing red, yellow-blue-orange showing orange
- E-slice edges out of the slice: green-red

Reads: 0 pairs, 0 side pairs, ARM 21, 4a-2 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*0 pairs, anything else*). That group is 56.4% of 4c2e, 7,584 cases: 0 with a DR in 4 or less, 0 in 5, 296 in 6, 7,288 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `L2 D' R B2 U' B2 R` (7 moves, too long). The whole attempt: `F2 B L2 B L (L2 D' R B2 U' B2 R)`, 12 to DR.

</details>

**Example 106 (4c2e).** `F' R2 F' D2 B2 U2 R2 B' U2 F' U2 L2 U2 F' L' D F' L2 U F' D' R D`

EO `F' B2 U L' B`, no RZP needed: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-orange
- Misoriented corners: white-blue-orange showing blue, yellow-green-red showing green, yellow-blue-red showing red, yellow-green-orange showing green
- E-slice edges out of the slice: blue-red

Reads: 1 pair, 0 side pairs, ARM 10, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, anything else*). That group is 12.0% of 4c2e, 1,616 cases: 0 with a DR in 4 or less, 0 in 5, 152 in 6, 1,464 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `L D' F2 R2 U2 D' R` (7 moves, too long). The whole attempt: `F' B2 U L' B (L D' F2 R2 U2 D' R)`, 12 to DR.

</details>

**Example 107 (4c2e).** `F2 R F2 R' D2 L' U2 R2 D2 U2 R' D2 L' U' F' D2 U2 L' F U R2 B`

EO `(F R' B2 L2 F')`, no RZP needed, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-blue
- Misoriented corners: yellow-blue-red showing blue, white-blue-red showing red, white-blue-orange showing orange, yellow-green-orange showing orange
- E-slice edges out of the slice: blue-red

Reads: 2 pairs (a bar), 1 side pair, ARM 31, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs (a bar)*). That group is 7.1% of 4c2e, 960 cases: 64 with a DR in 4 or less, 152 in 5, 360 in 6, 384 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `F2 U' R' U2 R` (5 moves, good). The whole attempt: `(F R' B2 L2 F') F2 U' R' U2 R`, 10 to DR.

</details>

**Example 108 (4c2e).** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `L F2 B`, RZP `D2 L`: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-orange
- Misoriented corners: white-green-orange showing green, white-blue-red showing red, white-blue-orange showing orange, white-green-red showing green
- E-slice edges out of the slice: blue-red

Reads: 1 pair, 0 side pairs, ARM 20, 4a-2 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, no side pair, 4a-2 corners*). That group is 2.5% of 4c2e, 336 cases: 0 with a DR in 4 or less, 0 in 5, 80 in 6, 256 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U R2 U' B2 R U2 R` (7 moves, too long). The whole attempt: `L F2 B D2 L (U R2 U' B2 R U2 R)`, 12 to DR.

</details>

**Example 109 (4c2e).** `F R2 B2 U2 L2 R2 B L2 F' U2 B R2 U2 L2 B' R' B' R' D L' F2 R D' B2`

EO `L2 U F`, RZP `D2 R`: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-green
- Misoriented corners: white-blue-red showing red, yellow-green-orange showing green, white-green-orange showing green, white-green-red showing red
- E-slice edges out of the slice: green-orange

Reads: 0 pairs, 2 side pairs, ARM 21, 4b-2 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*0 pairs, anything else*). That group is 56.4% of 4c2e, 7,584 cases: 0 with a DR in 4 or less, 0 in 5, 296 in 6, 7,288 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `R2 U L2 D R' B2 R` (7 moves, too long). The whole attempt: `L2 U F D2 R (R2 U L2 D R' B2 R)`, 12 to DR.

</details>

**Example 110 (4c2e).** `B2 F2 R' U2 L2 U2 B2 L' U2 R2 U2 F2 L R2 F2 U' R2 B R F U R B' D B'`

EO `(R' L F' U' B)`, no RZP needed, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-red
- Misoriented corners: yellow-green-red showing green, white-blue-red showing blue, white-green-orange showing orange, white-blue-orange showing blue
- E-slice edges out of the slice: blue-orange

Reads: 1 pair, 1 side pair, ARM 10, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair and a side pair*). That group is 15.1% of 4c2e, 2,032 cases: 8 with a DR in 4 or less, 216 in 5, 904 in 6, 904 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `R D L2 F2 D' R` (6 moves, good). The whole attempt: `(R' L F' U' B) R D L2 F2 D' R`, 11 to DR.

</details>

**Example 111 (4c2e).** `B2 U' R2 B2 U R2 U B2 U' B2 U F2 D' R2 R' U B U2 F' R D B D U2`

EO `(B' U2 F')`, RZP `(D R)`, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-blue
- Misoriented corners: white-blue-red showing red, white-green-orange showing orange, white-green-red showing red, white-blue-orange showing orange
- E-slice edges out of the slice: blue-red

Reads: 2 pairs (a bar), 0 side pairs, ARM 41, 4a-4 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs (a bar)*). That group is 7.1% of 4c2e, 960 cases: 64 with a DR in 4 or less, 152 in 5, 360 in 6, 384 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U R' F2 B2 R' B2 R` (7 moves, too long). The whole attempt: `(B' U2 F' D R) U R' F2 B2 R' B2 R`, 12 to DR.

</details>

**Example 112 (4c2e).** `L D2 L2 D2 F2 L D2 L U2 F2 D2 R' D2 R' F2 U' R2 U2 B F2 U' F D' U'`

EO `(U D' F' U B')`, no RZP needed, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: yellow-green-orange showing green, yellow-blue-orange showing blue, white-green-orange showing orange, yellow-green-red showing green
- E-slice edges out of the slice: green-red

Reads: 1 pair, 1 side pair, ARM 11, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair and a side pair*). That group is 15.1% of 4c2e, 2,032 cases: 8 with a DR in 4 or less, 216 in 5, 904 in 6, 904 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U' F2 B2 R' F2 R` (6 moves, good). The whole attempt: `(U D' F' U B') U' F2 B2 R' F2 R`, 11 to DR.

</details>

**Example 113 (4c2e).** `U2 L2 F2 R B2 D2 R B2 F2 L D2 R2 D2 D' F' R B R2 U' F' D' B'`

EO `(U F' B)`, RZP `(U L')`, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-blue
- Misoriented corners: yellow-green-red showing green, white-green-red showing red, yellow-blue-orange showing orange, white-blue-red showing red
- E-slice edges out of the slice: green-orange

Reads: 1 pair, 0 side pairs, ARM 31, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, no side pair, ARM 31*). That group is 4.3% of 4c2e, 576 cases: 0 with a DR in 4 or less, 0 in 5, 112 in 6, 464 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `R2 U2 D' R F2 R` (6 moves, good). The whole attempt: `(U F' B U L') R2 U2 D' R F2 R`, 11 to DR.

</details>

**Example 114 (4c2e).** `D B2 D2 B2 R2 D B2 D F2 R2 B2 U' B2 U' R2 F' U2 F2 L R2 F' R B' F'`

EO `R B L' F`, RZP `R'`: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-blue
- Misoriented corners: yellow-blue-orange showing orange, white-green-orange showing green, yellow-blue-red showing red, white-blue-orange showing blue
- E-slice edges out of the slice: blue-orange

Reads: 2 pairs (a bar), 1 side pair, ARM 21, 4b-2 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs (a bar)*). That group is 7.1% of 4c2e, 960 cases: 64 with a DR in 4 or less, 152 in 5, 360 in 6, 384 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 R' F2 R U2 D L` (7 moves, too long). The whole attempt: `R B L' F R' (U2 R' F2 R U2 D L)`, 12 to DR.

</details>

**Example 115 (4c2e).** `F2 U2 L2 B U2 B' U2 F' D2 F D2 L2 D' R2 F R2 B U L' U' R'`

EO `(L U R' D B')`, no RZP needed, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-green
- Misoriented corners: yellow-blue-orange showing blue, white-green-orange showing orange, yellow-green-orange showing orange, white-blue-orange showing blue
- E-slice edges out of the slice: blue-red

Reads: 1 pair, 0 side pairs, ARM 21, 4a-2 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, no side pair, 4a-2 corners*). That group is 2.5% of 4c2e, 336 cases: 0 with a DR in 4 or less, 0 in 5, 80 in 6, 256 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `D B2 U R2 D' R B2 R` (8 moves, too long). The whole attempt: `(L U R' D B') D B2 U R2 D' R B2 R`, 13 to DR.

</details>

**Example 116 (4c2e).** `F2 R2 D' U2 L2 U' F2 D L2 U' L2 B2 L2 R2 F' L D2 B' F R F' D`

EO `F2 D' R' L2 B`, no RZP needed: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-green
- Misoriented corners: yellow-green-orange showing orange, yellow-blue-orange showing orange, yellow-green-red showing red, white-blue-orange showing orange
- E-slice edges out of the slice: blue-red

Reads: 2 pairs (a bar), 0 side pairs, ARM 41, 4b-0 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs (a bar)*). That group is 7.1% of 4c2e, 960 cases: 64 with a DR in 4 or less, 152 in 5, 360 in 6, 384 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U D' R D2 R` (5 moves, good). The whole attempt: `F2 D' R' L2 B (U D' R D2 R)`, 10 to DR.

</details>

**Example 117 (4c2e).** `B D2 F2 L2 U2 D2 F U2 B' L2 F D2 L2 U2 F' D' F' D' R U' B2 D R' F2`

EO `U2 L B`, RZP `U R'`: 4c2e in 5.

What you see:

- U/D edges in the E slice: yellow-orange
- Misoriented corners: yellow-blue-red showing blue, yellow-blue-orange showing blue, yellow-green-orange showing orange, yellow-green-red showing red
- E-slice edges out of the slice: blue-orange

Reads: 1 pair, 1 side pair, ARM 20, 4a-2 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair and a side pair*). That group is 15.1% of 4c2e, 2,032 cases: 8 with a DR in 4 or less, 216 in 5, 904 in 6, 904 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `D' L2 D' B2 R F2 R` (7 moves, too long). The whole attempt: `U2 L B U R' (D' L2 D' B2 R F2 R)`, 12 to DR.

</details>

**Example 118 (4c2e).** `L2 F2 U2 F2 D2 R' D2 B2 R2 D2 R' B2 R U' L B' F2 R' B L F2 R'`

EO `F' U2 F`, RZP `D2 R`: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: yellow-green-red showing red, yellow-blue-red showing red, white-blue-red showing blue, white-green-orange showing orange
- E-slice edges out of the slice: green-red

Reads: 1 pair, 0 side pairs, ARM 31, 4c-1 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*1 pair, no side pair, ARM 31*). That group is 4.3% of 4c2e, 576 cases: 0 with a DR in 4 or less, 0 in 5, 112 in 6, 464 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U R U L F2 L' U R` (8 moves, too long). The whole attempt: `F' U2 F D2 R (U R U L F2 L' U R)`, 13 to DR.

</details>

**Example 119 (4c2e).** `R2 D' U' L2 U' B2 L2 D L2 B2 U2 B2 L' U2 B D' F2 R B' D' F2 U2`

EO `(U' D2 R2 U2 B')`, no RZP needed, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-blue
- Misoriented corners: white-blue-red showing red, yellow-green-orange showing orange, yellow-blue-red showing red, yellow-green-red showing red
- E-slice edges out of the slice: blue-orange

Reads: 1 pair, 0 side pairs, ARM 41, 4b-0 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, no side pair, 4b-0 corners*). That group is 1.8% of 4c2e, 240 cases: 0 with a DR in 4 or less, 0 in 5, 104 in 6, 136 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U2 R2 U' D' R B2 R` (7 moves, too long). The whole attempt: `(U' D2 R2 U2 B') U2 R2 U' D' R B2 R`, 12 to DR.

</details>

**Example 120 (4c2e).** `B2 R' D2 B2 R D2 R B2 R' B2 R F2 L' D2 D' R B R2 F' D L B L R2`

EO `(F' U2 B)`, RZP `(D L')`, on the inverse scramble: 4c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: yellow-green-orange showing orange, white-green-orange showing orange, yellow-blue-red showing red, white-blue-red showing red
- E-slice edges out of the slice: green-red

Reads: 1 pair, 0 side pairs, ARM 41, 4a-4 corners.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*1 pair, anything else*). That group is 12.0% of 4c2e, 1,616 cases: 0 with a DR in 4 or less, 0 in 5, 152 in 6, 1,464 in 7 or more.

Pairs rule, 1.5+ pairs (2 side pairs = 1 pair): **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U' L' D L B2 D R` (7 moves, too long). The whole attempt: `(F' U2 B D L') U' L' D L B2 D R`, 12 to DR.

</details>

## 3c2e: examples 121–140

The 3c2e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 3c2e once; 61.6% for 3c2e as a whole):

| What you read | Verdict | Share of 3c2e | Sub-7 |
|---|---|---|---|
| 1 pair | switch | 37.5% | 88.7% |
| 0 pairs, a fake pair or a split pair | switch | 44.6% | 56.5% |
| 0 pairs, no fake pair, no split pair | if you have time | 17.9% | 17.5% |

**Example 121 (3c2e).** `D2 B' R2 D2 B R2 B D2 B' D2 B U2 F' R2 R' B D B2 U' R F D F B2`

EO `R2 L B`, RZP `D2 R`: 3c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: white-blue-red showing red, white-green-red showing green, yellow-blue-red showing blue
- E-slice edges out of the slice: blue-red

Reads: 0 pairs, 1 fake pair, 1 split pair.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, a fake pair or a split pair*). That group is 44.6% of 3c2e, 1,600 cases: 16 with a DR in 4 or less, 152 in 5, 736 in 6, 696 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the inverse: `U' R U2 D' R U2 R` (7 moves, too long). The whole attempt: `R2 L B D2 R (U' R U2 D' R U2 R)`, 12 to DR.

</details>

**Example 122 (3c2e).** `F2 U' B2 L2 D' B2 R2 U' L2 U F2 D R2 F2 U2 F' D L U' L2 U' B2 F2 U`

EO `(D' F)`, RZP `(R' U2 R')`, on the inverse scramble: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-green
- Misoriented corners: white-blue-red showing red, white-green-orange showing orange, white-blue-orange showing blue
- E-slice edges out of the slice: green-red

Reads: 0 pairs, 0 fake pairs, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*0 pairs, no fake pair, no split pair*). That group is 17.9% of 3c2e, 640 cases: 0 with a DR in 4 or less, 0 in 5, 112 in 6, 528 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the normal side: `U R2 U F2 R' U' R` (7 moves, too long). The whole attempt: `(D' F R' U2 R') U R2 U F2 R' U' R`, 12 to DR.

</details>

**Example 123 (3c2e).** `D2 L' B2 U2 R' U2 L2 D2 F2 L' B2 U2 R F2 R B' D2 R' D U2 B U2 F`

EO `R F D B'`, RZP `R'`: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-red
- Misoriented corners: yellow-blue-orange showing blue, yellow-green-orange showing orange, white-green-red showing red
- E-slice edges out of the slice: green-orange

Reads: 0 pairs, 0 fake pairs, 1 split pair.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, a fake pair or a split pair*). That group is 44.6% of 3c2e, 1,600 cases: 16 with a DR in 4 or less, 152 in 5, 736 in 6, 696 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the inverse: `D R2 U2 L D L` (6 moves, good). The whole attempt: `R F D B' R' (D R2 U2 L D L)`, 11 to DR.

</details>

**Example 124 (3c2e).** `D' B2 U R2 U' B2 U2 R2 U R2 B2 R2 B2 U R' F D2 L F D L2 F' D2 U'`

EO `R U2 B`, RZP `U L`: 3c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: white-blue-red showing red, white-green-orange showing orange, white-blue-orange showing blue
- E-slice edges out of the slice: green-orange

Reads: 1 pair, 0 fake pairs, 1 split pair.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair*). That group is 37.5% of 3c2e, 1,344 cases: 120 with a DR in 4 or less, 400 in 5, 672 in 6, 152 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the inverse: `U2 R2 D' R2 L' U' L` (7 moves, too long). The whole attempt: `R U2 B U L (U2 R2 D' R2 L' U' L)`, 12 to DR.

</details>

**Example 125 (3c2e).** `B2 D2 U' L2 D L2 B2 D F2 L2 U F2 U2 L' U' F2 L' U R F' L2 B2 U'`

EO `(F U D2 F)`, RZP `(L)`, on the inverse scramble: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-red
- Misoriented corners: white-green-red showing red, yellow-green-orange showing orange, white-blue-orange showing orange
- E-slice edges out of the slice: green-orange

Reads: 0 pairs, 0 fake pairs, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*0 pairs, no fake pair, no split pair*). That group is 17.9% of 3c2e, 640 cases: 0 with a DR in 4 or less, 0 in 5, 112 in 6, 528 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the normal side: `B2 U F2 D' R' D R` (7 moves, too long). The whole attempt: `(F U D2 F L) B2 U F2 D' R' D R`, 12 to DR.

</details>

**Example 126 (3c2e).** `L2 R2 B' U2 F2 U2 L2 F' U2 B2 U2 R2 F B2 R2 U' B2 L B R U B L' D L'`

EO `(B D' F')`, RZP `(R' L')`, on the inverse scramble: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-orange
- Misoriented corners: yellow-blue-red showing blue, white-green-red showing green, white-blue-orange showing blue
- E-slice edges out of the slice: blue-red

Reads: 0 pairs, 0 fake pairs, 1 split pair.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, a fake pair or a split pair*). That group is 44.6% of 3c2e, 1,600 cases: 16 with a DR in 4 or less, 152 in 5, 736 in 6, 696 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the normal side: `F2 B2 D L' D' L` (6 moves, good). The whole attempt: `(B D' F' R' L') F2 B2 D L' D' L`, 11 to DR.

</details>

**Example 127 (3c2e).** `L2 U2 B2 R U2 R' U2 L' D2 L D2 B2 D' F2 L F2 R U B' U' F'`

EO `(B U' F')`, RZP `(D R')`, on the inverse scramble: 3c2e in 5.

What you see:

- U/D edges in the E slice: white-blue
- Misoriented corners: yellow-blue-red showing red, white-blue-red showing blue, yellow-green-red showing green
- E-slice edges out of the slice: blue-orange

Reads: 0 pairs, 1 fake pair, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, a fake pair or a split pair*). That group is 44.6% of 3c2e, 1,600 cases: 16 with a DR in 4 or less, 152 in 5, 736 in 6, 696 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the normal side: `U' F2 B2 U R' U R` (7 moves, too long). The whole attempt: `(B U' F' D R') U' F2 B2 U R' U R`, 12 to DR.

</details>

**Example 128 (3c2e).** `F2 R2 D' U2 L2 U' F2 D L2 U' L2 B2 L2 R2 F' L D2 B' F R F' D`

EO `U2 L' D2 F'`, RZP `R`: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-green
- Misoriented corners: yellow-green-red showing green, white-blue-orange showing orange, white-blue-red showing blue
- E-slice edges out of the slice: blue-orange

Reads: 0 pairs, 1 fake pair, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, a fake pair or a split pair*). That group is 44.6% of 3c2e, 1,600 cases: 16 with a DR in 4 or less, 152 in 5, 736 in 6, 696 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the inverse: `U2 D2 R2 U L' D L` (7 moves, too long). The whole attempt: `U2 L' D2 F' R (U2 D2 R2 U L' D L)`, 12 to DR.

</details>

**Example 129 (3c2e).** `U2 L D2 F2 D2 U2 R' U2 R2 B2 R B2 R F2 L' U' R F D' B2 R' B' R' U R2`

EO `D' F' R' U B'`, no RZP needed: 3c2e in 5.

What you see:

- U/D edges in the E slice: white-red
- Misoriented corners: yellow-green-red showing green, white-green-orange showing green, yellow-blue-red showing red
- E-slice edges out of the slice: blue-red

Reads: 0 pairs, 0 fake pairs, 1 split pair.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, a fake pair or a split pair*). That group is 44.6% of 3c2e, 1,600 cases: 16 with a DR in 4 or less, 152 in 5, 736 in 6, 696 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the inverse: `U F2 U R L2 D R` (7 moves, too long). The whole attempt: `D' F' R' U B' (U F2 U R L2 D R)`, 12 to DR.

</details>

**Example 130 (3c2e).** `L2 U2 B2 R2 U' L2 D2 U L2 B2 U' F2 B' L2 R2 U L' U B R U'`

EO `R' U' L D2 F`, no RZP needed: 3c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: yellow-green-red showing red, yellow-blue-red showing blue, yellow-blue-orange showing orange
- E-slice edges out of the slice: green-red

Reads: 0 pairs, 0 fake pairs, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*0 pairs, no fake pair, no split pair*). That group is 17.9% of 3c2e, 640 cases: 0 with a DR in 4 or less, 0 in 5, 112 in 6, 528 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the inverse: `U B2 U F2 L' U' L` (7 moves, too long). The whole attempt: `R' U' L D2 F (U B2 U F2 L' U' L)`, 12 to DR.

</details>

**Example 131 (3c2e).** `D L2 U B2 D2 F2 U' F2 U' F2 R2 U' F2 L2 B' D' B' F2 R' D' L R U`

EO `B L2 D L B`, no RZP needed: 3c2e in 5.

What you see:

- U/D edges in the E slice: white-orange
- Misoriented corners: yellow-blue-red showing blue, white-blue-orange showing blue, yellow-blue-orange showing orange
- E-slice edges out of the slice: blue-red

Reads: 1 pair, 0 fake pairs, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair*). That group is 37.5% of 3c2e, 1,344 cases: 120 with a DR in 4 or less, 400 in 5, 672 in 6, 152 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the inverse: `U L2 U2 R' U' R` (6 moves, good). The whole attempt: `B L2 D L B (U L2 U2 R' U' R)`, 11 to DR.

</details>

**Example 132 (3c2e).** `D2 B U2 R2 B D2 F' U2 R2 B' D2 L2 B2 R2 D' U' B' D' L' F' L' U2 B'`

EO `(D R B' R' F)`, no RZP needed, on the inverse scramble: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-green
- Misoriented corners: white-green-red showing red, white-blue-red showing blue, yellow-green-orange showing orange
- E-slice edges out of the slice: blue-orange

Reads: 1 pair, 0 fake pairs, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair*). That group is 37.5% of 3c2e, 1,344 cases: 120 with a DR in 4 or less, 400 in 5, 672 in 6, 152 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the normal side: `U2 F2 D2 L U L` (6 moves, good). The whole attempt: `(D R B' R' F) U2 F2 D2 L U L`, 11 to DR.

</details>

**Example 133 (3c2e).** `R F2 R' U2 R D2 B2 R' B2 R U2 L D' R' F L' B L' F2 D F2 L`

EO `(D' L F R B)`, no RZP needed, on the inverse scramble: 3c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: yellow-blue-red showing red, yellow-blue-orange showing blue, white-green-orange showing green
- E-slice edges out of the slice: green-red

Reads: 0 pairs, 1 fake pair, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, a fake pair or a split pair*). That group is 44.6% of 3c2e, 1,600 cases: 16 with a DR in 4 or less, 152 in 5, 736 in 6, 696 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the normal side: `R2 U2 D' R' U R` (6 moves, good). The whole attempt: `(D' L F R B) R2 U2 D' R' U R`, 11 to DR.

</details>

**Example 134 (3c2e).** `L2 U R2 F2 U L2 B2 D L2 U R2 D L2 D' F' L U' R' D L F D B2`

EO `(F')`, RZP `(L' B2 U R')`, on the inverse scramble: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-red
- Misoriented corners: white-green-red showing red, yellow-green-orange showing orange, white-green-orange showing green
- E-slice edges out of the slice: green-red

Reads: 0 pairs, 0 fake pairs, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*0 pairs, no fake pair, no split pair*). That group is 17.9% of 3c2e, 640 cases: 0 with a DR in 4 or less, 0 in 5, 112 in 6, 528 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the normal side: `U F2 U B2 D L D L` (8 moves, too long). The whole attempt: `(F' L' B2 U R') U F2 U B2 D L D L`, 13 to DR.

</details>

**Example 135 (3c2e).** `L' D2 L2 U2 R B2 D2 R' F2 R B2 D2 R D' B D' U' F' U' L2 B L' R2`

EO `(R2 L' F B)`, RZP `(R')`, on the inverse scramble: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-blue
- Misoriented corners: yellow-green-red showing red, yellow-green-orange showing green, yellow-blue-orange showing orange
- E-slice edges out of the slice: green-orange

Reads: 1 pair, 0 fake pairs, 1 split pair.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair*). That group is 37.5% of 3c2e, 1,344 cases: 120 with a DR in 4 or less, 400 in 5, 672 in 6, 152 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the normal side: `R2 U2 F2 R' D' R` (6 moves, good). The whole attempt: `(R2 L' F B R') R2 U2 F2 R' D' R`, 11 to DR.

</details>

**Example 136 (3c2e).** `D R2 B2 R2 L2 D B2 D B2 U' R2 U F2 L2 R' B2 F' D' R2 D R2 F2`

EO `F'`, RZP `U2 D' B2 R'`: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-red
- Misoriented corners: white-blue-orange showing orange, white-blue-red showing blue, white-green-red showing red
- E-slice edges out of the slice: green-red

Reads: 0 pairs, 0 fake pairs, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*0 pairs, no fake pair, no split pair*). That group is 17.9% of 3c2e, 640 cases: 0 with a DR in 4 or less, 0 in 5, 112 in 6, 528 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the inverse: `D F2 U2 R2 L D L` (7 moves, too long). The whole attempt: `F' U2 D' B2 R' (D F2 U2 R2 L D L)`, 12 to DR.

</details>

**Example 137 (3c2e).** `F2 L' D2 B2 F2 R B2 L2 R' B2 L2 F2 R' U' L' U L2 U L' F L R'`

EO `U2 L D R' B`, no RZP needed: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-green
- Misoriented corners: white-green-red showing red, white-blue-red showing blue, white-blue-orange showing orange
- E-slice edges out of the slice: blue-red

Reads: 0 pairs, 0 fake pairs, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*0 pairs, no fake pair, no split pair*). That group is 17.9% of 3c2e, 640 cases: 0 with a DR in 4 or less, 0 in 5, 112 in 6, 528 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the inverse: `D2 R2 U2 F2 L D L` (7 moves, too long). The whole attempt: `U2 L D R' B (D2 R2 U2 F2 L D L)`, 12 to DR.

</details>

**Example 138 (3c2e).** `U2 R D2 L' U2 L F2 L' B2 R2 B2 U2 R2 D' L2 R' B2 D' U2 L F`

EO `F`, RZP `L' D2 F2 L`: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-blue
- Misoriented corners: yellow-blue-orange showing orange, yellow-green-orange showing green, yellow-green-red showing red
- E-slice edges out of the slice: blue-orange

Reads: 1 pair, 0 fake pairs, 1 split pair.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair*). That group is 37.5% of 3c2e, 1,344 cases: 120 with a DR in 4 or less, 400 in 5, 672 in 6, 152 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the inverse: `D2 R2 U' R2 L' D' L` (7 moves, too long). The whole attempt: `F L' D2 F2 L (D2 R2 U' R2 L' D' L)`, 12 to DR.

</details>

**Example 139 (3c2e).** `B2 L' F2 L2 F2 R U2 R B2 F2 D2 F2 L' D' U' L' B F' D R F'`

EO `(L2 F D' F B)`, no RZP needed, on the inverse scramble: 3c2e in 5.

What you see:

- U/D edges in the E slice: yellow-orange
- Misoriented corners: yellow-green-orange showing green, yellow-green-red showing red, white-blue-red showing red
- E-slice edges out of the slice: blue-red

Reads: 1 pair, 0 fake pairs, 0 split pairs.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair*). That group is 37.5% of 3c2e, 1,344 cases: 120 with a DR in 4 or less, 400 in 5, 672 in 6, 152 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the normal side: `D F2 R' U' R` (5 moves, good). The whole attempt: `(L2 F D' F B) D F2 R' U' R`, 10 to DR.

</details>

**Example 140 (3c2e).** `R2 D2 L' F2 D2 R2 D2 R' B2 D2 R2 D2 R F2 R' F' L F2 U2 R' D L F2 D'`

EO `(D2 L F')`, RZP `(U R')`, on the inverse scramble: 3c2e in 5.

What you see:

- U/D edges in the E slice: white-green
- Misoriented corners: white-blue-red showing red, white-green-red showing green, yellow-green-red showing red
- E-slice edges out of the slice: blue-red

Reads: 0 pairs, 1 fake pair, 1 split pair.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, a fake pair or a split pair*). That group is 44.6% of 3c2e, 1,600 cases: 16 with a DR in 4 or less, 152 in 5, 736 in 6, 696 in 7 or more.

Pairs rule, always: **switch**.

Optimal DR on the normal side: `F2 D2 R L2 D' R` (6 moves, good). The whole attempt: `(D2 L F' U R') F2 D2 R L2 D' R`, 11 to DR.

</details>

## 7c8e: examples 141–170

The 7c8e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 7c8e once; 16.4% for 7c8e as a whole):

| What you read | Verdict | Share of 7c8e | Sub-7 |
|---|---|---|---|
| 6 pairs, not ARM 64 | switch | 1.9% | 96.5% |
| 5 pairs, not ARM 20 or 54 | switch | 13.9% | 55.9% |
| 4 pairs, ARM 21, 31 or 43 | switch | 6.5% | 34.9% |
| 3 pairs, ARM 21 | switch | 0.61% | 27.8% |
| 4 pairs, ARM 11, 12, 33, 41 or 62 | if you have time | 8.1% | 21.8% |
| 4 pairs, anything else | skip | 19.0% | 6.8% |
| 5 or 6 pairs with ARM 20, 54 or 64 | skip | 0.51% | 0% |
| 3 pairs or fewer | skip | 49.4% | 2.5% |

**Example 141 (7c8e).** `B D2 F2 L2 U2 D2 F U2 B' L2 F D2 L2 U2 F' D' F' D' R U' B2 D R' F2`

EO `L U2 B'`, RZP `D2 R'`: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-blue, white-green, yellow-blue, white-orange
- Misoriented corners: white-blue-red showing red, yellow-blue-orange showing orange, yellow-green-orange showing green, yellow-blue-red showing red, white-blue-orange showing blue, white-green-red showing red, yellow-green-red showing red
- E-slice edges out of the slice: green-orange, blue-red, blue-orange, green-red

Reads: 5 pairs (white-blue 1, white-green 1, yellow-blue 2, white-orange 1), ARM 53.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*5 pairs, not ARM 20 or 54*). That group is 13.9% of 7c8e, 3,264 cases: 40 with a DR in 4 or less, 440 in 5, 1,344 in 6, 1,440 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `F2 D' F2 U2 R U L` (7 moves, too long). The whole attempt: `L U2 B' D2 R' (F2 D' F2 U2 R U L)`, 12 to DR.

</details>

**Example 142 (7c8e).** `D2 L2 B2 L' B2 R' D2 F2 L' D2 F2 R' B2 D2 L' B' U' F' U L' R D B2 L'`

EO `R' B U F'`, RZP `L`: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, yellow-blue, white-red, yellow-green
- Misoriented corners: yellow-blue-red showing red, yellow-blue-orange showing blue, yellow-green-orange showing green, white-green-orange showing green, white-blue-orange showing orange, yellow-green-red showing red, white-blue-red showing blue
- E-slice edges out of the slice: blue-orange, green-orange, blue-red, green-red

Reads: 5 pairs (yellow-orange 2, yellow-blue 1, white-red 1, yellow-green 1), ARM 32.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*5 pairs, not ARM 20 or 54*). That group is 13.9% of 7c8e, 3,264 cases: 40 with a DR in 4 or less, 440 in 5, 1,344 in 6, 1,440 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U' R' U L2 D R L` (7 moves, too long). The whole attempt: `R' B U F' L (U' R' U L2 D R L)`, 12 to DR.

</details>

**Example 143 (7c8e).** `F R2 B2 U2 L2 R2 B L2 F' U2 B R2 U2 L2 B' R' B' R' D L' F2 R D' B2`

EO `U L2 F`, RZP `D2 L`: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-red, white-blue, yellow-orange, yellow-red
- Misoriented corners: yellow-green-orange showing orange, white-green-red showing green, yellow-green-red showing green, white-green-orange showing orange, yellow-blue-orange showing orange, yellow-blue-red showing blue, white-blue-orange showing blue
- E-slice edges out of the slice: blue-red, green-orange, blue-orange, green-red

Reads: 3 pairs (white-red 1, yellow-red 2), ARM 31.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*3 pairs or fewer*). That group is 49.4% of 7c8e, 11,616 cases: 0 with a DR in 4 or less, 0 in 5, 296 in 6, 11,320 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `U' L2 U' F2 R2 L' D R` (8 moves, too long). The whole attempt: `U L2 F D2 L (U' L2 U' F2 R2 L' D R)`, 13 to DR.

</details>

**Example 144 (7c8e).** `R2 U2 F' D2 F2 R2 F' L2 B R2 F2 B' U2 L' R' B' D' L U B' L'`

EO `R F R D' F'`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-green, yellow-red, white-red, white-orange
- Misoriented corners: white-green-orange showing orange, yellow-green-orange showing green, white-blue-red showing blue, yellow-blue-orange showing blue, yellow-blue-red showing blue, yellow-green-red showing red, white-blue-orange showing blue
- E-slice edges out of the slice: green-orange, blue-orange, green-red, blue-red

Reads: 4 pairs (white-green 1, yellow-red 1, white-red 1, white-orange 1), ARM 21.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*4 pairs, ARM 21, 31 or 43*). That group is 6.5% of 7c8e, 1,536 cases: 0 with a DR in 4 or less, 40 in 5, 496 in 6, 1,000 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 B2 R2 F2 R D L` (7 moves, too long). The whole attempt: `R F R D' F' (U2 B2 R2 F2 R D L)`, 12 to DR.

</details>

**Example 145 (7c8e).** `U2 F L2 B R2 U2 B D2 F D2 B2 R2 F' R' D' R' F' L' B' D F2 D' R'`

EO `D2 R F' B`, RZP `R'`: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-red, yellow-green, white-orange, yellow-orange
- Misoriented corners: yellow-green-orange showing green, yellow-green-red showing red, white-blue-orange showing blue, yellow-blue-red showing blue, white-green-orange showing orange, yellow-blue-orange showing blue, white-green-red showing red
- E-slice edges out of the slice: green-orange, green-red, blue-red, blue-orange

Reads: 5 pairs (yellow-red 1, yellow-green 1, white-orange 1, yellow-orange 2), ARM 31.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*5 pairs, not ARM 20 or 54*). That group is 13.9% of 7c8e, 3,264 cases: 40 with a DR in 4 or less, 440 in 5, 1,344 in 6, 1,440 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `L D R2 D' R` (5 moves, good). The whole attempt: `D2 R F' B R' (L D R2 D' R)`, 10 to DR.

</details>

**Example 146 (7c8e).** `L2 U' B2 U' R2 D' B2 F2 D2 R2 F2 U B2 L2 R' D L' B F' U L' D2 F'`

EO `U' R F' R' B'`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-blue, yellow-green, yellow-red, white-red
- Misoriented corners: white-green-orange showing orange, yellow-blue-orange showing orange, yellow-green-orange showing green, white-blue-red showing blue, yellow-blue-red showing blue, white-blue-orange showing blue, yellow-green-red showing green
- E-slice edges out of the slice: blue-orange, green-orange, green-red, blue-red

Reads: 4 pairs (yellow-blue 1, yellow-red 2, white-red 1), ARM 22.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*4 pairs, anything else*). That group is 19.0% of 7c8e, 4,480 cases: 0 with a DR in 4 or less, 0 in 5, 304 in 6, 4,176 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `U R2 L2 D' B2 R' U L` (8 moves, too long). The whole attempt: `U' R F' R' B' (U R2 L2 D' B2 R' U L)`, 13 to DR.

</details>

**Example 147 (7c8e).** `U2 F2 R2 B L2 D2 B L2 R2 F D2 B2 D2 D' R' B L B2 U' R' D' L'`

EO `(L' F L' D2 B)`, no RZP needed, on the inverse scramble: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-green, yellow-blue, yellow-red, white-blue
- Misoriented corners: white-blue-orange showing blue, yellow-blue-red showing red, white-blue-red showing red, white-green-orange showing green, white-green-red showing red, yellow-green-red showing green, yellow-green-orange showing orange
- E-slice edges out of the slice: green-orange, blue-red, green-red, blue-orange

Reads: 4 pairs (white-green 1, yellow-blue 1, yellow-red 1, white-blue 1), ARM 43.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*4 pairs, ARM 21, 31 or 43*). That group is 6.5% of 7c8e, 1,536 cases: 0 with a DR in 4 or less, 40 in 5, 496 in 6, 1,000 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `L2 U' F2 D L D' R` (7 moves, too long). The whole attempt: `(L' F L' D2 B) L2 U' F2 D L D' R`, 12 to DR.

</details>

**Example 148 (7c8e).** `F D2 F2 D2 R2 F D2 F U2 R2 D2 B' D2 B' R2 U' B2 U2 L R2 U' R D' U'`

EO `B U2 F2 U B`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-green, yellow-blue, white-red, white-blue
- Misoriented corners: white-green-orange showing orange, yellow-green-red showing red, white-blue-red showing blue, white-green-red showing green, yellow-blue-orange showing orange, white-blue-orange showing blue, yellow-blue-red showing red
- E-slice edges out of the slice: blue-orange, blue-red, green-red, green-orange

Reads: 5 pairs (yellow-green 1, yellow-blue 2, white-red 2), ARM 43.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*5 pairs, not ARM 20 or 54*). That group is 13.9% of 7c8e, 3,264 cases: 40 with a DR in 4 or less, 440 in 5, 1,344 in 6, 1,440 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `L D' R' U' L` (5 moves, good). The whole attempt: `B U2 F2 U B (L D' R' U' L)`, 10 to DR.

</details>

**Example 149 (7c8e).** `L2 R2 D' L2 U L2 D2 B2 D' B2 L2 U' L2 B2 B' R U' F D2 L F2 D' L`

EO `D' F R' U B`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-green, yellow-orange, white-orange
- Misoriented corners: yellow-blue-red showing blue, yellow-green-red showing green, yellow-green-orange showing green, white-blue-red showing blue, yellow-blue-orange showing orange, white-green-orange showing orange, white-green-red showing green
- E-slice edges out of the slice: blue-orange, green-red, green-orange, blue-red

Reads: 3 pairs (white-red 2, yellow-orange 1), ARM 21.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 pairs, ARM 21*). That group is 0.61% of 7c8e, 144 cases: 0 with a DR in 4 or less, 0 in 5, 40 in 6, 104 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `L U2 R' U2 D R` (6 moves, good). The whole attempt: `D' F R' U B (L U2 R' U2 D R)`, 11 to DR.

</details>

**Example 150 (7c8e).** `D2 L2 B2 L' B2 R' D2 F2 L' D2 F2 R' B2 D2 L' B' U' F' U L' R D B2 L'`

EO `R' U' B' U' F'`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-red, white-green, yellow-red, yellow-green
- Misoriented corners: yellow-blue-orange showing orange, white-green-red showing green, yellow-green-orange showing orange, yellow-blue-red showing blue, yellow-green-red showing red, white-green-orange showing orange, white-blue-red showing blue
- E-slice edges out of the slice: green-red, blue-orange, blue-red, green-orange

Reads: 6 pairs (white-red 2, white-green 1, yellow-red 1, yellow-green 2), ARM 42.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*6 pairs, not ARM 64*). That group is 1.9% of 7c8e, 456 cases: 80 with a DR in 4 or less, 144 in 5, 216 in 6, 16 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U D' L D L2 U' R` (7 moves, too long). The whole attempt: `R' U' B' U' F' (U D' L D L2 U' R)`, 12 to DR.

</details>

**Example 151 (7c8e).** `D' B2 D2 R2 D R2 D L2 B2 F2 U2 F2 R2 R' U2 B L D L F D R' D`

EO `U' F B' U' F'`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-red, yellow-orange, white-blue
- Misoriented corners: white-green-orange showing green, yellow-green-orange showing orange, yellow-blue-orange showing blue, white-green-red showing red, yellow-blue-red showing blue, white-blue-red showing blue, white-blue-orange showing blue
- E-slice edges out of the slice: blue-orange, green-orange, green-red, blue-red

Reads: 3 pairs (yellow-red 1, white-red 1, yellow-orange 1), ARM 21.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 pairs, ARM 21*). That group is 0.61% of 7c8e, 144 cases: 0 with a DR in 4 or less, 0 in 5, 40 in 6, 104 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `R F2 L' F2 L2 U' L` (7 moves, too long). The whole attempt: `U' F B' U' F' (R F2 L' F2 L2 U' L)`, 12 to DR.

</details>

**Example 152 (7c8e).** `R2 F2 D' B2 D2 R2 D' L2 U R2 D2 U' F2 L' R' U' B' L F U' L'`

EO `(B' R' F' U B')`, no RZP needed, on the inverse scramble: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, yellow-green, yellow-blue, white-orange
- Misoriented corners: white-green-orange showing orange, yellow-green-red showing red, yellow-green-orange showing green, yellow-blue-red showing red, yellow-blue-orange showing orange, white-blue-red showing red, white-green-red showing red
- E-slice edges out of the slice: green-orange, green-red, blue-orange, blue-red

Reads: 4 pairs (yellow-orange 1, yellow-green 1, yellow-blue 2), ARM 62.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*4 pairs, ARM 11, 12, 33, 41 or 62*). That group is 8.1% of 7c8e, 1,904 cases: 0 with a DR in 4 or less, 0 in 5, 416 in 6, 1,488 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `U' B2 U B2 L D R` (7 moves, too long). The whole attempt: `(B' R' F' U B') U' B2 U B2 L D R`, 12 to DR.

</details>

**Example 153 (7c8e).** `U2 F2 R2 B L2 D2 B L2 R2 F D2 B2 D2 D' R' B L B2 U' R' D' L'`

EO `D R2 B' L2 F'`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-blue, white-green, yellow-orange
- Misoriented corners: white-green-red showing green, white-green-orange showing orange, yellow-green-red showing green, white-blue-orange showing orange, yellow-green-orange showing green, yellow-blue-red showing blue, white-blue-red showing red
- E-slice edges out of the slice: blue-orange, green-orange, green-red, blue-red

Reads: 6 pairs (yellow-red 2, white-blue 2, white-green 1, yellow-orange 1), ARM 32.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*6 pairs, not ARM 64*). That group is 1.9% of 7c8e, 456 cases: 80 with a DR in 4 or less, 144 in 5, 216 in 6, 16 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U' R' D' R2 D L` (6 moves, good). The whole attempt: `D R2 B' L2 F' (U' R' D' R2 D L)`, 11 to DR.

</details>

**Example 154 (7c8e).** `F2 D2 L' R2 U2 R' F2 L U2 R' U2 B2 U2 D2 F' U L2 B' F D F' L`

EO `U2 B2 U' D2 B`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-blue, yellow-red, yellow-orange, white-orange
- Misoriented corners: yellow-blue-orange showing orange, white-green-red showing green, white-blue-red showing blue, yellow-green-red showing red, yellow-green-orange showing green, white-blue-orange showing orange, yellow-blue-red showing blue
- E-slice edges out of the slice: green-red, green-orange, blue-orange, blue-red

Reads: 3 pairs (white-blue 1, yellow-red 1, yellow-orange 1), ARM 31.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*3 pairs or fewer*). That group is 49.4% of 7c8e, 11,616 cases: 0 with a DR in 4 or less, 0 in 5, 296 in 6, 11,320 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `R2 F2 B2 D' R D L` (7 moves, too long). The whole attempt: `U2 B2 U' D2 B (R2 F2 B2 D' R D L)`, 12 to DR.

</details>

**Example 155 (7c8e).** `R2 F2 D' B2 D2 R2 D' L2 U R2 D2 U' F2 L' R' U' B' L F U' L'`

EO `(B' U' R F' B)`, no RZP needed, on the inverse scramble: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-blue, yellow-orange, white-orange
- Misoriented corners: white-blue-orange showing orange, yellow-blue-orange showing orange, yellow-green-red showing green, white-green-orange showing orange, yellow-green-orange showing green, white-blue-red showing red, yellow-blue-red showing blue
- E-slice edges out of the slice: green-orange, blue-red, green-red, blue-orange

Reads: 2 pairs (yellow-blue 1, yellow-orange 1), ARM 41.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*3 pairs or fewer*). That group is 49.4% of 7c8e, 11,616 cases: 0 with a DR in 4 or less, 0 in 5, 296 in 6, 11,320 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `R L2 D L U R' D R` (8 moves, too long). The whole attempt: `(B' U' R F' B) R L2 D L U R' D R`, 13 to DR.

</details>

**Example 156 (7c8e).** `D2 B2 R F2 L2 D2 R B2 R' B2 R U2 B2 B' U L U B' L U' B' D' L'`

EO `(B D B2 R2 F)`, no RZP needed, on the inverse scramble: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-red, yellow-green, yellow-orange
- Misoriented corners: yellow-green-orange showing orange, white-blue-orange showing blue, white-green-red showing green, white-green-orange showing orange, yellow-green-red showing red, yellow-blue-orange showing orange, white-blue-red showing blue
- E-slice edges out of the slice: blue-orange, green-red, green-orange, blue-red

Reads: 4 pairs (white-red 2, yellow-green 2), ARM 41.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*4 pairs, ARM 11, 12, 33, 41 or 62*). That group is 8.1% of 7c8e, 1,904 cases: 0 with a DR in 4 or less, 0 in 5, 416 in 6, 1,488 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `U2 F2 U' B2 R' U L` (7 moves, too long). The whole attempt: `(B D B2 R2 F) U2 F2 U' B2 R' U L`, 12 to DR.

</details>

**Example 157 (7c8e).** `U2 L2 U2 R2 B2 R2 B2 F' R2 B' R2 D2 B' R' U' L2 B D2 R' U L' B2 F2`

EO `(U R D' R2 F)`, no RZP needed, on the inverse scramble: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-orange, yellow-blue, white-red
- Misoriented corners: white-blue-orange showing orange, white-blue-red showing blue, yellow-green-red showing red, yellow-green-orange showing orange, yellow-blue-orange showing blue, white-green-orange showing green, white-green-red showing green
- E-slice edges out of the slice: green-red, blue-red, green-orange, blue-orange

Reads: 4 pairs (white-orange 1, yellow-orange 1, white-red 2), ARM 31.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*4 pairs, ARM 21, 31 or 43*). That group is 6.5% of 7c8e, 1,536 cases: 0 with a DR in 4 or less, 40 in 5, 496 in 6, 1,000 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U2 R2 L D' R2 D R` (7 moves, too long). The whole attempt: `(U R D' R2 F) U2 R2 L D' R2 D R`, 12 to DR.

</details>

**Example 158 (7c8e).** `F R2 B2 U2 L2 R2 B L2 F' U2 B R2 U2 L2 B' R' B' R' D L' F2 R D' B2`

EO `U L2 F`, RZP `R2 L'`: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-blue, white-orange, yellow-red, yellow-orange
- Misoriented corners: yellow-green-red showing green, white-green-red showing green, white-green-orange showing green, white-blue-orange showing blue, yellow-blue-red showing blue, white-blue-red showing red, yellow-green-orange showing green
- E-slice edges out of the slice: blue-red, green-orange, blue-orange, green-red

Reads: 6 pairs (white-blue 1, white-orange 2, yellow-red 2, yellow-orange 1), ARM 11.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*6 pairs, not ARM 64*). That group is 1.9% of 7c8e, 456 cases: 80 with a DR in 4 or less, 144 in 5, 216 in 6, 16 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U' B2 U L U R` (6 moves, good). The whole attempt: `U L2 F R2 L' (U' B2 U L U R)`, 11 to DR.

</details>

**Example 159 (7c8e).** `B R2 B2 R2 D2 B R2 B L2 D2 R2 F' R2 F' D2 L' F2 L2 U D2 L' D R' L'`

EO `F' R2 F2 L' F`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-red, white-blue, yellow-blue, yellow-green
- Misoriented corners: yellow-green-red showing green, yellow-green-orange showing orange, yellow-blue-red showing red, white-green-red showing green, yellow-blue-orange showing orange, white-blue-orange showing orange, white-blue-red showing blue
- E-slice edges out of the slice: green-red, green-orange, blue-red, blue-orange

Reads: 6 pairs (white-red 2, white-blue 1, yellow-blue 2, yellow-green 1), ARM 43.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*6 pairs, not ARM 64*). That group is 1.9% of 7c8e, 456 cases: 80 with a DR in 4 or less, 144 in 5, 216 in 6, 16 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `D R' U' L` (4 moves, good). The whole attempt: `F' R2 F2 L' F (D R' U' L)`, 9 to DR.

</details>

**Example 160 (7c8e).** `U2 L2 F R2 F D2 B D2 B' D2 R2 F' D2 U' R' F' L D R' U2 L2 U2`

EO `(D' R2 B2 R B)`, no RZP needed, on the inverse scramble: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-green, yellow-red, white-green, white-blue
- Misoriented corners: yellow-blue-orange showing blue, yellow-green-orange showing orange, white-green-orange showing orange, white-blue-orange showing blue, yellow-green-red showing green, yellow-blue-red showing red, white-green-red showing red
- E-slice edges out of the slice: blue-red, green-orange, blue-orange, green-red

Reads: 4 pairs (yellow-green 1, yellow-red 1, white-green 2), ARM 43.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*4 pairs, ARM 21, 31 or 43*). That group is 6.5% of 7c8e, 1,536 cases: 0 with a DR in 4 or less, 40 in 5, 496 in 6, 1,000 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `D' R' F2 U' L D R` (7 moves, too long). The whole attempt: `(D' R2 B2 R B) D' R' F2 U' L D R`, 12 to DR.

</details>

**Example 161 (7c8e).** `L2 R2 B' U2 F2 U2 L2 F' U2 B2 U2 R2 F B2 R2 U' B2 L B R U B L' D L'`

EO `(B2 D B' D F)`, no RZP needed, on the inverse scramble: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-blue, white-green, white-orange, white-blue
- Misoriented corners: yellow-green-red showing red, white-green-orange showing orange, white-blue-orange showing blue, white-blue-red showing red, white-green-red showing red, yellow-blue-orange showing orange, yellow-green-orange showing orange
- E-slice edges out of the slice: blue-orange, green-orange, blue-red, green-red

Reads: 5 pairs (yellow-blue 1, white-green 2, white-orange 1, white-blue 1), ARM 63.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*5 pairs, not ARM 20 or 54*). That group is 13.9% of 7c8e, 3,264 cases: 40 with a DR in 4 or less, 440 in 5, 1,344 in 6, 1,440 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `F2 R2 D L' U R` (6 moves, good). The whole attempt: `(B2 D B' D F) F2 R2 D L' U R`, 11 to DR.

</details>

**Example 162 (7c8e).** `R2 B2 U2 R F2 L' U2 L2 U2 R D2 B2 D2 R' D' R' F D' B' R B2 L2 U R'`

EO `F' U' B' L F`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-red, white-orange, white-green, yellow-red
- Misoriented corners: yellow-green-red showing green, yellow-green-orange showing green, white-green-red showing green, white-blue-orange showing orange, yellow-blue-red showing red, white-green-orange showing green, yellow-blue-orange showing blue
- E-slice edges out of the slice: green-red, green-orange, blue-orange, blue-red

Reads: 3 pairs (white-red 1, white-orange 1, yellow-red 1), ARM 21.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 pairs, ARM 21*). That group is 0.61% of 7c8e, 144 cases: 0 with a DR in 4 or less, 0 in 5, 40 in 6, 104 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 F2 L2 F2 R' U' L` (7 moves, too long). The whole attempt: `F' U' B' L F (U2 F2 L2 F2 R' U' L)`, 12 to DR.

</details>

**Example 163 (7c8e).** `L2 B R2 D2 R2 L2 F' L2 F2 U2 F U2 F D2 B' L' F D R' U2 F' U' F' L F2`

EO `(U' R F')`, RZP `(D R)`, on the inverse scramble: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-blue, white-red, yellow-red, yellow-orange
- Misoriented corners: yellow-green-orange showing green, white-green-red showing green, white-green-orange showing green, white-blue-orange showing blue, white-blue-red showing red, yellow-green-red showing green, yellow-blue-red showing blue
- E-slice edges out of the slice: blue-orange, blue-red, green-red, green-orange

Reads: 5 pairs (white-blue 1, white-red 1, yellow-red 2, yellow-orange 1), ARM 11.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*5 pairs, not ARM 20 or 54*). That group is 13.9% of 7c8e, 3,264 cases: 40 with a DR in 4 or less, 440 in 5, 1,344 in 6, 1,440 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `U2 B2 U L' U R` (6 moves, good). The whole attempt: `(U' R F' D R) U2 B2 U L' U R`, 11 to DR.

</details>

**Example 164 (7c8e).** `B2 R' D2 B2 R D2 R B2 R' B2 R F2 L' D2 D' R B R2 F' D L B L R2`

EO `(D2 B' R2 F)`, RZP `(L)`, on the inverse scramble: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-red, yellow-blue, yellow-orange, white-blue
- Misoriented corners: white-blue-red showing blue, yellow-blue-red showing blue, white-blue-orange showing orange, yellow-green-red showing red, yellow-green-orange showing green, yellow-blue-orange showing orange, white-green-orange showing orange
- E-slice edges out of the slice: blue-orange, green-orange, blue-red, green-red

Reads: 4 pairs (yellow-red 1, yellow-blue 1, yellow-orange 1, white-blue 1), ARM 42.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*4 pairs, anything else*). That group is 19.0% of 7c8e, 4,480 cases: 0 with a DR in 4 or less, 0 in 5, 304 in 6, 4,176 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `U R2 B2 U' L U R` (7 moves, too long). The whole attempt: `(D2 B' R2 F L) U R2 B2 U' L U R`, 12 to DR.

</details>

**Example 165 (7c8e).** `D L2 R2 F2 U L2 B2 U B2 R2 D2 L2 D R2 R' D L2 R F L2 F2 D2 U2`

EO `B2 L2 B'`, RZP `R' L`: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-orange, white-red, yellow-orange, yellow-red
- Misoriented corners: yellow-blue-red showing blue, white-blue-red showing red, yellow-green-red showing green, white-blue-orange showing blue, white-green-red showing green, yellow-blue-orange showing blue, white-green-orange showing orange
- E-slice edges out of the slice: green-red, blue-orange, blue-red, green-orange

Reads: 5 pairs (white-orange 1, white-red 1, yellow-orange 1, yellow-red 2), ARM 20.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*5 or 6 pairs with ARM 20, 54 or 64*). That group is 0.51% of 7c8e, 120 cases: 0 with a DR in 4 or less, 0 in 5, 0 in 6, 120 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `R' D R' D' L D R` (7 moves, too long). The whole attempt: `B2 L2 B' R' L (R' D R' D' L D R)`, 12 to DR.

</details>

**Example 166 (7c8e).** `D2 F2 L2 F2 R2 U' R2 B2 U2 R2 U' B2 U L' D B' F2 U' B D F2 U'`

EO `R L' F' L' F`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-orange, white-blue, white-green, yellow-green
- Misoriented corners: white-blue-orange showing orange, white-green-red showing red, yellow-green-orange showing green, white-green-orange showing green, yellow-blue-orange showing blue, yellow-blue-red showing red, white-blue-red showing red
- E-slice edges out of the slice: green-orange, blue-orange, blue-red, green-red

Reads: 4 pairs (white-orange 1, white-blue 2, white-green 1), ARM 43.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*4 pairs, ARM 21, 31 or 43*). That group is 6.5% of 7c8e, 1,536 cases: 0 with a DR in 4 or less, 40 in 5, 496 in 6, 1,000 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U2 R U L D' F2 U2 L` (8 moves, too long). The whole attempt: `R L' F' L' F (U2 R U L D' F2 U2 L)`, 13 to DR.

</details>

**Example 167 (7c8e).** `F2 U2 L2 B U2 B' U2 F' D2 F D2 L2 D' R2 F R2 B U L' U' R'`

EO `(R D' R U' B)`, no RZP needed, on the inverse scramble: 7c8e in 5.

What you see:

- U/D edges in the E slice: white-green, yellow-red, white-red, yellow-blue
- Misoriented corners: white-blue-red showing blue, yellow-green-red showing green, yellow-blue-red showing red, yellow-green-orange showing orange, yellow-blue-orange showing blue, white-blue-orange showing blue, white-green-red showing green
- E-slice edges out of the slice: green-orange, blue-orange, green-red, blue-red

Reads: 4 pairs (yellow-red 1, white-red 2, yellow-blue 1), ARM 22.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*4 pairs, anything else*). That group is 19.0% of 7c8e, 4,480 cases: 0 with a DR in 4 or less, 0 in 5, 304 in 6, 4,176 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `R' D' R2 D' F2 D B2 R` (8 moves, too long). The whole attempt: `(R D' R U' B) R' D' R2 D' F2 D B2 R`, 13 to DR.

</details>

**Example 168 (7c8e).** `L2 B L2 F R2 F2 D2 B D2 L2 U2 F' L' D2 U F2 L' R2 B' R U L`

EO `D2 F B U' B'`, no RZP needed: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-orange, yellow-green, white-blue
- Misoriented corners: white-blue-orange showing orange, yellow-green-orange showing green, white-green-orange showing green, yellow-blue-orange showing orange, yellow-blue-red showing blue, white-blue-red showing red, yellow-green-red showing red
- E-slice edges out of the slice: green-red, blue-orange, blue-red, green-orange

Reads: 5 pairs (yellow-red 1, white-orange 1, yellow-green 1, white-blue 2), ARM 42.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*5 pairs, not ARM 20 or 54*). That group is 13.9% of 7c8e, 3,264 cases: 40 with a DR in 4 or less, 440 in 5, 1,344 in 6, 1,440 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `F2 U' R' L2 U L` (6 moves, good). The whole attempt: `D2 F B U' B' (F2 U' R' L2 U L)`, 11 to DR.

</details>

**Example 169 (7c8e).** `L2 F2 U2 F2 D2 R' D2 B2 R2 D2 R' B2 R U' L B' F2 R' B L F2 R'`

EO `D' F' U2 F`, RZP `L`: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-green, yellow-orange, white-blue, white-orange
- Misoriented corners: yellow-blue-red showing red, yellow-green-orange showing orange, white-green-orange showing green, white-blue-orange showing orange, yellow-blue-orange showing orange, yellow-green-red showing red, white-green-red showing red
- E-slice edges out of the slice: blue-orange, green-orange, green-red, blue-red

Reads: 4 pairs (yellow-green 2, white-blue 1, white-orange 1), ARM 62.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*4 pairs, ARM 11, 12, 33, 41 or 62*). That group is 8.1% of 7c8e, 1,904 cases: 0 with a DR in 4 or less, 0 in 5, 416 in 6, 1,488 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `U2 L2 U' R2 U' R' D' L` (8 moves, too long). The whole attempt: `D' F' U2 F L (U2 L2 U' R2 U' R' D' L)`, 13 to DR.

</details>

**Example 170 (7c8e).** `U2 D2 F' L2 B2 L2 U2 B' L2 F2 L2 D2 B F2 D2 L' F2 U F D L F U' R U'`

EO `(U2 F R' B')`, RZP `(L)`, on the inverse scramble: 7c8e in 5.

What you see:

- U/D edges in the E slice: yellow-blue, yellow-green, white-green, white-red
- Misoriented corners: white-green-red showing red, yellow-green-red showing green, white-blue-red showing blue, yellow-blue-orange showing blue, white-green-orange showing orange, yellow-green-orange showing green, yellow-blue-red showing red
- E-slice edges out of the slice: blue-red, green-red, green-orange, blue-orange

Reads: 4 pairs (yellow-blue 1, white-green 2, white-red 1), ARM 33.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*4 pairs, ARM 11, 12, 33, 41 or 62*). That group is 8.1% of 7c8e, 1,904 cases: 0 with a DR in 4 or less, 0 in 5, 416 in 6, 1,488 in 7 or more.

Pairs rule, 5+ pairs, counting edge ARM under 2 as a pair: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `F2 U' B2 D R U' L` (7 moves, too long). The whole attempt: `(U2 F R' B' L) F2 U' B2 D R U' L`, 12 to DR.

</details>

## 8c8e: examples 171–178

The 8c8e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 8c8e once; 14.5% for 8c8e as a whole):

| What you read | Verdict | Share of 8c8e | Sub-7 |
|---|---|---|---|
| 8 pairs | switch | 0.07% | 100% |
| 6 pairs, corner ARM 4 | switch | 3.7% | 50.0% |
| 5 pairs, edge ARM 1 or 3 | switch | 11.7% | 45.5% |
| 2 pairs, ARM 42 | switch | 2.7% | 32.5% |
| 4 pairs, ARM 42 | switch | 9.8% | 25.2% |
| 4 pairs, ARM 02, 43, 63 or 82 | if you have time | 5.7% | 22.1% |
| 6 pairs, corner ARM not 4 | skip | 3.7% | 14.3% |
| 5 pairs, edge ARM 2 | skip | 11.2% | 3.6% |
| anything else | skip | 51.5% | 3.4% |

**Example 171 (8c8e).** `U2 L2 F R2 F D2 B D2 B' D2 R2 F' D2 U' R' F' L D R' U2 L2 U2`

EO `R' L F'`, RZP `B2 L`: 8c8e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-green, white-orange, yellow-orange
- Misoriented corners: white-green-orange showing green, yellow-green-orange showing green, white-blue-orange showing orange, yellow-blue-red showing red, white-green-red showing red, yellow-blue-orange showing blue, yellow-green-red showing green, white-blue-red showing blue
- E-slice edges out of the slice: green-orange, blue-red, green-red, blue-orange

Reads: 5 pairs (yellow-red 1, white-green 1, white-orange 1, yellow-orange 2), ARM 31.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*5 pairs, edge ARM 1 or 3*). That group is 11.7% of 8c8e, 704 cases: 0 with a DR in 4 or less, 32 in 5, 288 in 6, 384 in 7 or more.

Pairs rule, 3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs: **switch**.

Optimal DR on the inverse: `R L D R' U' R` (6 moves, good). The whole attempt: `R' L F' B2 L (R L D R' U' R)`, 11 to DR.

</details>

**Example 172 (8c8e).** `R2 D2 B2 D' B2 U' R2 F2 D' R2 F2 U' B2 R2 D' B' L' F' L D' U R B2 D'`

EO `U' B L F`, RZP `R`: 8c8e in 5.

What you see:

- U/D edges in the E slice: yellow-green, yellow-blue, white-blue, yellow-red
- Misoriented corners: yellow-green-orange showing orange, white-green-red showing green, white-green-orange showing green, white-blue-red showing red, yellow-blue-orange showing orange, yellow-green-red showing green, yellow-blue-red showing blue, white-blue-orange showing orange
- E-slice edges out of the slice: blue-red, green-orange, green-red, blue-orange

Reads: 6 pairs (yellow-green 1, yellow-blue 1, white-blue 2, yellow-red 2), ARM 43.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*6 pairs, corner ARM 4*). That group is 3.7% of 8c8e, 224 cases: 8 with a DR in 4 or less, 32 in 5, 72 in 6, 112 in 7 or more.

Pairs rule, 3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs: **switch**.

Optimal DR on the inverse: `U' R2 D R L` (5 moves, good). The whole attempt: `U' B L F R (U' R2 D R L)`, 10 to DR.

</details>

**Example 173 (8c8e).** `L2 F2 U2 F2 D2 R' D2 B2 R2 D2 R' B2 R U' L B' F2 R' B L F2 R'`

EO `(L F' D' F')`, RZP `(R)`, on the inverse scramble: 8c8e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-red, white-green, yellow-blue
- Misoriented corners: yellow-blue-red showing red, white-blue-red showing blue, yellow-blue-orange showing orange, white-blue-orange showing blue, white-green-red showing green, white-green-orange showing green, yellow-green-red showing red, yellow-green-orange showing orange
- E-slice edges out of the slice: blue-orange, green-orange, blue-red, green-red

Reads: 4 pairs (white-red 2, yellow-blue 2), ARM 42.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*4 pairs, ARM 42*). That group is 9.8% of 8c8e, 588 cases: 0 with a DR in 4 or less, 20 in 5, 128 in 6, 440 in 7 or more.

Pairs rule, 3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs: **skip**.

Optimal DR on the normal side: `U2 R' L F2 U' D L` (7 moves, too long). The whole attempt: `(L F' D' F' R) U2 R' L F2 U' D L`, 12 to DR.

</details>

**Example 174 (8c8e).** `U2 D2 F' L2 B2 L2 U2 B' L2 F2 L2 D2 B F2 D2 L' F2 U F D L F U' R U'`

EO `(F' R' B)`, RZP `(U2 R')`, on the inverse scramble: 8c8e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, white-green, yellow-red, white-red
- Misoriented corners: white-blue-red showing blue, white-blue-orange showing orange, yellow-green-orange showing green, yellow-green-red showing red, white-green-red showing green, white-green-orange showing green, yellow-blue-orange showing blue, yellow-blue-red showing blue
- E-slice edges out of the slice: green-orange, blue-orange, green-red, blue-red

Reads: 5 pairs (yellow-orange 2, yellow-red 1, white-red 2), ARM 21.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*5 pairs, edge ARM 1 or 3*). That group is 11.7% of 8c8e, 704 cases: 0 with a DR in 4 or less, 32 in 5, 288 in 6, 384 in 7 or more.

Pairs rule, 3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs: **switch**.

Optimal DR on the normal side: `D L' D' R U L` (6 moves, good). The whole attempt: `(F' R' B U2 R') D L' D' R U L`, 11 to DR.

</details>

**Example 175 (8c8e).** `R2 F2 D' B2 D2 R2 D' L2 U R2 D2 U' F2 L' R' U' B' L F U' L'`

EO `L2 F' U' L B`, no RZP needed: 8c8e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-blue, white-orange, white-green
- Misoriented corners: yellow-green-red showing red, yellow-blue-red showing blue, white-green-orange showing green, yellow-green-orange showing orange, yellow-blue-orange showing orange, white-blue-orange showing blue, white-green-red showing red, white-blue-red showing blue
- E-slice edges out of the slice: blue-orange, blue-red, green-red, green-orange

Reads: 5 pairs (white-red 1, yellow-blue 1, white-orange 2, white-green 1), ARM 42.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*5 pairs, edge ARM 2*). That group is 11.2% of 8c8e, 672 cases: 0 with a DR in 4 or less, 0 in 5, 24 in 6, 648 in 7 or more.

Pairs rule, 3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs: **skip**.

Optimal DR on the inverse: `U R L2 U L D' R` (7 moves, too long). The whole attempt: `L2 F' U' L B (U R L2 U L D' R)`, 12 to DR.

</details>

**Example 176 (8c8e).** `D2 F' U2 B' D2 R2 B2 D2 R2 B' U2 B2 D2 R' B' R2 B L D' B' D R'`

EO `(R L U' F)`, RZP `(L')`, on the inverse scramble: 8c8e in 5.

What you see:

- U/D edges in the E slice: yellow-green, white-orange, white-red, yellow-blue
- Misoriented corners: yellow-green-orange showing orange, yellow-blue-red showing red, yellow-blue-orange showing orange, white-green-red showing green, white-blue-red showing blue, white-blue-orange showing blue, yellow-green-red showing red, white-green-orange showing green
- E-slice edges out of the slice: green-orange, green-red, blue-red, blue-orange

Reads: 8 pairs (yellow-green 2, white-orange 2, white-red 2, yellow-blue 2), ARM 42.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*8 pairs*). That group is 0.07% of 8c8e, 4 cases: 4 with a DR in 4 or less, 0 in 5, 0 in 6, 0 in 7 or more.

Pairs rule, 3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs: **switch**.

Optimal DR on the normal side: `D R L` (3 moves, good). The whole attempt: `(R L U' F L') D R L`, 8 to DR.

</details>

**Example 177 (8c8e).** `F2 R F2 R' D2 L' U2 R2 D2 U2 R' D2 L' U' F' D2 U2 L' F U R2 B`

EO `(R F2 R2 F')`, RZP `(L')`, on the inverse scramble: 8c8e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-orange, white-blue, yellow-blue
- Misoriented corners: white-blue-red showing blue, white-green-red showing red, yellow-green-red showing green, white-green-orange showing orange, yellow-blue-orange showing orange, yellow-blue-red showing blue, yellow-green-orange showing orange, white-blue-orange showing blue
- E-slice edges out of the slice: green-red, green-orange, blue-orange, blue-red

Reads: 2 pairs (white-red 1, yellow-blue 1), ARM 42.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs, ARM 42*). That group is 2.7% of 8c8e, 160 cases: 0 with a DR in 4 or less, 4 in 5, 48 in 6, 108 in 7 or more.

Pairs rule, 3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs: **skip**.

Optimal DR on the normal side: `U R L' U D F2 L` (7 moves, too long). The whole attempt: `(R F2 R2 F' L') U R L' U D F2 L`, 12 to DR.

</details>

**Example 178 (8c8e).** `F D2 F2 D2 R2 F D2 F U2 R2 D2 B' D2 B' R2 U' B2 U2 L R2 U' R D' U'`

EO `U F2 B' D2 B'`, no RZP needed: 8c8e in 5.

What you see:

- U/D edges in the E slice: yellow-green, yellow-blue, white-red, white-blue
- Misoriented corners: white-green-orange showing green, white-green-red showing red, yellow-green-red showing red, yellow-green-orange showing green, yellow-blue-red showing red, yellow-blue-orange showing orange, white-blue-orange showing blue, white-blue-red showing blue
- E-slice edges out of the slice: green-red, green-orange, blue-orange, blue-red

Reads: 4 pairs (yellow-green 1, yellow-blue 2, white-red 1), ARM 43.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*4 pairs, ARM 02, 43, 63 or 82*). That group is 5.7% of 8c8e, 344 cases: 0 with a DR in 4 or less, 0 in 5, 76 in 6, 268 in 7 or more.

Pairs rule, 3 or fewer fake pairs (5+ pairs), with edge ARM not 2 or 6+ pairs: **skip**.

Optimal DR on the inverse: `R' D' L U' F2 U2 R` (7 moves, too long). The whole attempt: `U F2 B' D2 B' (R' D' L U' F2 U2 R)`, 12 to DR.

</details>

## 2c2e: examples 179–183

The 2c2e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 2c2e once; 23.7% for 2c2e as a whole):

| What you read | Verdict | Share of 2c2e | Sub-7 |
|---|---|---|---|
| 1 pair | switch | 21.4% | 62.5% |
| 2 pairs and a side pair | switch | 0.45% | 100% |
| 0 pairs, 1 side pair, ARM 00 or 11 | switch | 7.1% | 68.8% |
| 0 pairs, JZP (ARM 00), no side pair | if you have time | 4.9% | 18.2% |
| anything else | skip | 66.1% | 6.1% |

**Example 179 (2c2e).** `D2 F' U2 B R2 U2 R2 U2 B D2 F2 R2 B' L2 F' L' D' L F2 D B R2 F' U`

EO `L D L2 F'`, RZP `L'`: 2c2e in 5.

What you see:

- U/D edges in the E slice: yellow-orange
- Misoriented corners: yellow-green-red showing green, white-green-red showing green
- E-slice edges out of the slice: blue-orange

Reads: 0 pairs, 0 side pairs, ARM 00.

<details><summary>Verdict and the DR after the switch</summary>

Card: **if you have time** (*0 pairs, JZP (ARM 00), no side pair*). That group is 4.9% of 2c2e, 88 cases: 0 with a DR in 4 or less, 0 in 5, 16 in 6, 72 in 7 or more.

Pairs rule, 1+ pairs: **skip**.

Optimal DR on the inverse: `U2 R' B2 U2 R' F2 L` (7 moves, too long). The whole attempt: `L D L2 F' L' (U2 R' B2 U2 R' F2 L)`, 12 to DR.

</details>

**Example 180 (2c2e).** `B2 U B2 F2 R2 U' B2 L2 D L2 D2 L2 U2 F' U' R' B2 D2 B2 D L2 U'`

EO `(U' R D' R F')`, no RZP needed, on the inverse scramble: 2c2e in 5.

What you see:

- U/D edges in the E slice: white-blue
- Misoriented corners: yellow-green-orange showing orange, yellow-blue-red showing blue
- E-slice edges out of the slice: blue-red

Reads: 0 pairs, 1 side pair, ARM 11.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*0 pairs, 1 side pair, ARM 00 or 11*). That group is 7.1% of 2c2e, 128 cases: 0 with a DR in 4 or less, 0 in 5, 88 in 6, 40 in 7 or more.

Pairs rule, 1+ pairs: **skip**.

Optimal DR on the normal side: `R L2 D' R2 U R` (6 moves, good). The whole attempt: `(U' R D' R F') R L2 D' R2 U R`, 11 to DR.

</details>

**Example 181 (2c2e).** `F L2 B' R2 F2 U2 B U2 R2 U2 R2 D2 F' D' R' F2 L U R U L2 D2 F'`

EO `D2 F2 D' R F'`, no RZP needed: 2c2e in 5.

What you see:

- U/D edges in the E slice: white-red
- Misoriented corners: white-blue-red showing blue, white-green-red showing green
- E-slice edges out of the slice: blue-red

Reads: 2 pairs (a bar), 1 side pair, ARM 00.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs and a side pair*). That group is 0.45% of 2c2e, 8 cases: 0 with a DR in 4 or less, 0 in 5, 8 in 6, 0 in 7 or more.

Pairs rule, 1+ pairs: **switch**.

Optimal DR on the inverse: `F2 R F2 R' F2 R` (6 moves, good). The whole attempt: `D2 F2 D' R F' (F2 R F2 R' F2 R)`, 11 to DR.

</details>

**Example 182 (2c2e).** `B D2 F2 L2 U2 D2 F U2 B' L2 F D2 L2 U2 F' D' F' D' R U' B2 D R' F2`

EO `(D B2 R2 B)`, RZP `(L)`, on the inverse scramble: 2c2e in 5.

What you see:

- U/D edges in the E slice: yellow-blue
- Misoriented corners: white-blue-orange showing orange, white-blue-red showing red
- E-slice edges out of the slice: blue-red

Reads: 0 pairs, 0 side pairs, ARM 21.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*anything else*). That group is 66.1% of 2c2e, 1,184 cases: 0 with a DR in 4 or less, 0 in 5, 72 in 6, 1,112 in 7 or more.

Pairs rule, 1+ pairs: **skip**.

Optimal DR on the normal side: `L' D L' D2 R D' R` (7 moves, too long). The whole attempt: `(D B2 R2 B L) L' D L' D2 R D' R`, 12 to DR.

</details>

**Example 183 (2c2e).** `D2 L2 B2 L2 F2 U' F2 R2 U2 F2 U' R2 U B' D R' L2 U' R D L2 U'`

EO `(F2 U2 R2 L2 F')`, no RZP needed, on the inverse scramble: 2c2e in 5.

What you see:

- U/D edges in the E slice: white-orange
- Misoriented corners: white-blue-orange showing blue, white-green-red showing red
- E-slice edges out of the slice: blue-red

Reads: 1 pair, 0 side pairs, ARM 10.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair*). That group is 21.4% of 2c2e, 384 cases: 0 with a DR in 4 or less, 48 in 5, 192 in 6, 144 in 7 or more.

Pairs rule, 1+ pairs: **switch**.

Optimal DR on the normal side: `L' U' B2 U L` (5 moves, good). The whole attempt: `(F2 U2 R2 L2 F') L' U' B2 U L`, 10 to DR.

</details>

## The low DRMs (4c6e, 3c4e, 3c6e, 5c4e, 5c6e, 6c6e): examples 184–201

The 4c6e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 4c6e once; 4.6% for 4c6e as a whole):

| What you read | Verdict | Share of 4c6e | Sub-7 |
|---|---|---|---|
| 4 pairs on three edges | switch | 0.85% | 74.0% |
| 3 pairs, JZP (ARM 00) | switch | 0.31% | 61.1% |
| 3 pairs on three edges, the three bad edges in one layer | switch | 0.27% | 62.5% |
| 3 pairs on three edges, corners 2 and 2 in the layers | switch | 2.2% | 25.8% |
| anything else | skip | 96.4% | 3.2% |

The 3c4e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 3c4e once; 9.9% for 3c4e as a whole):

| What you read | Verdict | Share of 3c4e | Sub-7 |
|---|---|---|---|
| 2 pairs and a side pair | switch | 6.9% | 43.2% |
| 2 pairs, no side pair, a fake pair | switch | 1.9% | 27.3% |
| 1 pair, 2 side pairs | switch | 5.7% | 28.1% |
| 1 pair, ARM 21, 1 side pair, 2 fake pairs or holes on one R/L face | switch | 2.6% | 40.3% |
| 1 pair, ARM 21, 1 side pair, the rest | if you have time | 3.5% | 19.5% |
| anything else | skip | 79.4% | 3.9% |

The 3c6e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 3c6e once; 4.8% for 3c6e as a whole):

| What you read | Verdict | Share of 3c6e | Sub-7 |
|---|---|---|---|
| 2 pairs, ARM 21, 1 or 2 fake pairs | switch | 4.1% | 31.3% |
| 2 pairs, ARM 12, 2 fake pairs | switch | 1.4% | 38.6% |
| 2 pairs, ARM 01 | switch | 1.5% | 22.9% |
| anything else | skip | 93.0% | 2.9% |

The 5c4e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 5c4e once; 7.2% for 5c4e as a whole):

| What you read | Verdict | Share of 5c4e | Sub-7 |
|---|---|---|---|
| 3 pairs, 2+ side pairs | switch | 2.2% | 38.3% |
| 2 pairs, ARM 21, 2+ side pairs | switch | 2.8% | 32.7% |
| 1 pair, ARM 21, 2+ side pairs, 2+ fake pairs | switch | 1.8% | 24.3% |
| 3 pairs, 0 or 1 side pair | if you have time | 3.9% | 21.5% |
| anything else | skip | 89.3% | 4.7% |

The 5c6e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 5c6e once; 6.1% for 5c6e as a whole):

| What you read | Verdict | Share of 5c6e | Sub-7 |
|---|---|---|---|
| 4 pairs | switch | 3.1% | 37.9% |
| 3 pairs, ARM 21, 3 side pairs | switch | 1.2% | 38.3% |
| 2 pairs, ARM 21, 3 side pairs | switch | 2.0% | 20.6% |
| 3 pairs, ARM 21, fewer than 3 side pairs | if you have time | 2.1% | 17.4% |
| anything else | skip | 91.6% | 4.1% |

The 6c6e card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of 6c6e once; 5.6% for 6c6e as a whole):

| What you read | Verdict | Share of 6c6e | Sub-7 |
|---|---|---|---|
| 5 or 6 pairs | switch | 1.2% | 39.0% |
| 3 pairs, 3 fake pairs, corners 3 and 3 in the layers | switch | 1.9% | 34.1% |
| anything else | skip | 97.0% | 4.6% |

**Example 184 (5c4e).** `L D2 R2 F2 U2 D2 R U2 L' F2 R D2 F2 U2 R' D' R' D' B U' L2 D B' R2`

EO `F' D' B2 L2 B'`, no RZP needed: 5c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-blue
- Misoriented corners: yellow-blue-orange showing orange, yellow-blue-red showing blue, white-green-red showing red, yellow-green-orange showing green, white-blue-orange showing blue
- E-slice edges out of the slice: blue-orange, blue-red

Reads: 2 pairs, one on each edge, 1 fake pair, 2 side pairs, ARM 21.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs, ARM 21, 2+ side pairs*). That group is 2.8% of 5c4e, 2,616 cases: 24 with a DR in 4 or less, 144 in 5, 688 in 6, 1,760 in 7 or more.

Pairs rule, never: **skip**.

Optimal DR on the inverse: `L B2 D2 L2 U F2 R` (7 moves, too long). The whole attempt: `F' D' B2 L2 B' (L B2 D2 L2 U F2 R)`, 12 to DR.

</details>

**Example 185 (3c6e).** `R' B2 R' F2 L B2 L' U2 L B2 R B2 R' D2 R' B' D' L R2 F R D' B' L'`

EO `(D2 F D2 R' B')`, no RZP needed, on the inverse scramble: 3c6e in 5.

What you see:

- U/D edges in the E slice: white-blue, white-red, yellow-red
- Misoriented corners: white-green-red showing red, white-blue-orange showing orange, white-blue-red showing blue
- E-slice edges out of the slice: blue-red, green-orange, blue-orange

Reads: 2 pairs (white-blue 1, white-red 1), 2 fake pairs, ARM 21.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs, ARM 21, 1 or 2 fake pairs*). That group is 4.1% of 3c6e, 1,024 cases: 16 with a DR in 4 or less, 64 in 5, 240 in 6, 704 in 7 or more.

Pairs rule, never: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the normal side: `R U' D' L2 U' L` (6 moves, good). The whole attempt: `(D2 F D2 R' B') R U' D' L2 U' L`, 11 to DR.

</details>

**Example 186 (5c6e).** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `D L D2 B'`, RZP `R'`: 5c6e in 5.

What you see:

- U/D edges in the E slice: white-red, yellow-orange, yellow-blue
- Misoriented corners: yellow-blue-orange showing blue, yellow-green-red showing red, yellow-blue-red showing blue, white-blue-red showing red, yellow-green-orange showing green
- E-slice edges out of the slice: green-orange, blue-orange, blue-red

Reads: 2 pairs (yellow-orange 2), 3 side pairs, ARM 21.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs, ARM 21, 3 side pairs*). That group is 2.0% of 5c6e, 2,568 cases: 16 with a DR in 4 or less, 96 in 5, 416 in 6, 2,040 in 7 or more.

Pairs rule, never: **skip**.

Optimal DR on the inverse: `F2 L2 B2 L B2 D' R` (7 moves, too long). The whole attempt: `D L D2 B' R' (F2 L2 B2 L B2 D' R)`, 12 to DR.

</details>

**Example 187 (3c4e).** `U2 F2 L D2 L' F2 R B2 U2 L D2 R' F2 R' B2 F' U' L D' L U' L B2 L2 R2`

EO `L B'`, RZP `R2 B2 L'`: 3c4e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, white-green
- Misoriented corners: yellow-blue-orange showing orange, white-green-orange showing orange, white-green-red showing green
- E-slice edges out of the slice: green-red, blue-red

Reads: 1 pair (on white-green), 2 fake pairs, 1 side pair, ARM 21, holes on one R/L face (both edges out of the slice have red).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, ARM 21, 1 side pair, 2 fake pairs or holes on one R/L face*). That group is 2.6% of 3c4e, 496 cases: 0 with a DR in 4 or less, 48 in 5, 152 in 6, 296 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `L2 D2 R F2 B2 D' L` (7 moves, too long). The whole attempt: `L B' R2 B2 L' (L2 D2 R F2 B2 D' L)`, 12 to DR.

</details>

**Example 188 (3c6e).** `B2 D2 R2 B2 D F2 R2 D' L2 D L2 B2 D F2 U R' F' D' B2 L D2 B D2 F D'`

EO `F' D2 B' L2 F'`, no RZP needed: 3c6e in 5.

What you see:

- U/D edges in the E slice: white-green, white-red, white-blue
- Misoriented corners: white-blue-orange showing blue, white-green-orange showing orange, white-green-red showing green
- E-slice edges out of the slice: blue-orange, blue-red, green-red

Reads: 2 pairs (white-green 1, white-red 1), 2 fake pairs, ARM 12.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs, ARM 12, 2 fake pairs*). That group is 1.4% of 3c6e, 352 cases: 0 with a DR in 4 or less, 16 in 5, 120 in 6, 216 in 7 or more.

Pairs rule, never: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `B2 U2 D L U D2 R` (7 moves, too long). The whole attempt: `F' D2 B' L2 F' (B2 U2 D L U D2 R)`, 12 to DR.

</details>

**Example 189 (6c6e).** `F2 R F2 R' D2 L' U2 R2 D2 U2 R' D2 L' U' F' D2 U2 L' F U R2 B`

EO `(R L' B2 L2 F')`, no RZP needed, on the inverse scramble: 6c6e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, yellow-blue, white-red
- Misoriented corners: yellow-blue-orange showing blue, white-blue-orange showing blue, white-green-red showing red, yellow-blue-red showing blue, yellow-green-orange showing green, white-blue-red showing blue
- E-slice edges out of the slice: green-red, blue-red, blue-orange

Reads: 3 pairs (yellow-orange 2, white-red 1), 3 fake pairs, corners 3 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 pairs, 3 fake pairs, corners 3 and 3 in the layers*). That group is 1.9% of 6c6e, 2,560 cases: 16 with a DR in 4 or less, 160 in 5, 696 in 6, 1,688 in 7 or more.

Pairs rule, never: **skip**.

Optimal DR on the normal side: `D2 R' L2 U' L D' L` (7 moves, too long). The whole attempt: `(R L' B2 L2 F') D2 R' L2 U' L D' L`, 12 to DR.

</details>

**Example 190 (6c6e).** `B D2 F2 L2 U2 D2 F U2 B' L2 F D2 L2 U2 F' D' F' D' R U' B2 D R' F2`

EO `(D F2 L2 B')`, RZP `(R')`, on the inverse scramble: 6c6e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, white-blue, yellow-green
- Misoriented corners: white-green-orange showing orange, yellow-green-orange showing orange, white-blue-red showing red, white-blue-orange showing orange, yellow-green-red showing red, yellow-blue-orange showing blue
- E-slice edges out of the slice: blue-orange, green-orange, blue-red

Reads: 5 pairs (yellow-orange 1, white-blue 2, yellow-green 2), 1 fake pair, corners 3 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*5 or 6 pairs*). That group is 1.2% of 6c6e, 1,600 cases: 8 with a DR in 4 or less, 112 in 5, 504 in 6, 976 in 7 or more.

Pairs rule, never: **skip**.

Optimal DR on the normal side: `R2 U' R F2 L' U' R` (7 moves, too long). The whole attempt: `(D F2 L2 B' R') R2 U' R F2 L' U' R`, 12 to DR.

</details>

**Example 191 (4c6e).** `U2 R2 D' F2 R2 U2 R2 U' B2 R2 U2 R2 U F2 U' F' D F2 L2 U' R D F2 R'`

EO `(R2 D F')`, RZP `(D2 L')`, on the inverse scramble: 4c6e in 5.

What you see:

- U/D edges in the E slice: yellow-orange, white-red, yellow-red
- Misoriented corners: yellow-green-red showing green, white-blue-orange showing blue, yellow-blue-red showing blue, yellow-blue-orange showing blue
- E-slice edges out of the slice: blue-orange, green-orange, blue-red

Reads: 3 pairs on 2 edges (yellow-orange 1, yellow-red 2), ARM 00, bad edges in both layers, corners 1 white, 3 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 pairs, JZP (ARM 00)*). That group is 0.31% of 4c6e, 288 cases: 8 with a DR in 4 or less, 56 in 5, 112 in 6, 112 in 7 or more.

Pairs rule, never: **skip**.

Optimal DR on the normal side: `D2 B2 D2 R U2 L` (6 moves, good). The whole attempt: `(R2 D F' D2 L') D2 B2 D2 R U2 L`, 11 to DR.

</details>

**Example 192 (3c4e).** `D2 F2 L2 F2 R2 U' R2 B2 U2 R2 U' B2 U L' D B' F2 U' B D F2 U'`

EO `U L F U' F'`, no RZP needed: 3c4e in 5.

What you see:

- U/D edges in the E slice: white-blue, yellow-orange
- Misoriented corners: yellow-blue-red showing blue, yellow-green-orange showing green, white-blue-orange showing blue
- E-slice edges out of the slice: green-orange, blue-orange

Reads: 1 pair (on yellow-orange), 1 fake pair, 2 side pairs, ARM 01, holes on one R/L face (both edges out of the slice have orange).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*1 pair, 2 side pairs*). That group is 5.7% of 3c4e, 1,080 cases: 0 with a DR in 4 or less, 32 in 5, 272 in 6, 776 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the inverse: `L' D R2 L U' L` (6 moves, good). The whole attempt: `U L F U' F' (L' D R2 L U' L)`, 11 to DR.

</details>

**Example 193 (4c6e).** `D2 F2 L' B2 L2 D2 L' U2 R D2 L2 R' F2 U' D' R' B' U F R' U'`

EO `R2 B U R F'`, no RZP needed: 4c6e in 5.

What you see:

- U/D edges in the E slice: yellow-red, yellow-orange, white-green
- Misoriented corners: white-green-orange showing orange, yellow-blue-orange showing blue, yellow-blue-red showing blue, white-green-red showing red
- E-slice edges out of the slice: green-red, green-orange, blue-orange

Reads: 4 pairs on 3 edges (yellow-red 1, yellow-orange 1, white-green 2), ARM 21, bad edges in both layers, corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*4 pairs on three edges*). That group is 0.85% of 4c6e, 800 cases: 64 with a DR in 4 or less, 168 in 5, 360 in 6, 208 in 7 or more.

Pairs rule, never: **skip**.

Optimal DR on the inverse: `U D2 B2 R B2 L` (6 moves, good). The whole attempt: `R2 B U R F' (U D2 B2 R B2 L)`, 11 to DR.

</details>

**Example 194 (5c4e).** `D2 U2 L F2 R F2 R D2 F2 U2 B2 L B' R B D' L' F' L' R' B R'`

EO `(D2 B D2 F')`, RZP `(L)`, on the inverse scramble: 5c4e in 5.

What you see:

- U/D edges in the E slice: yellow-red, white-blue
- Misoriented corners: white-blue-red showing red, yellow-blue-red showing red, yellow-green-orange showing orange, yellow-blue-orange showing blue, white-green-red showing red
- E-slice edges out of the slice: blue-red, green-red

Reads: 1 pair (on white-blue), 1 fake pair, 0 side pairs, ARM 41.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*anything else*). That group is 89.3% of 5c4e, 84,024 cases: 0 with a DR in 4 or less, 256 in 5, 3,672 in 6, 80,096 in 7 or more.

Pairs rule, never: **skip**.

Optimal DR on the normal side: `U2 R2 B2 D R U' B2 R` (8 moves, too long). The whole attempt: `(D2 B D2 F' L) U2 R2 B2 D R U' B2 R`, 13 to DR.

</details>

**Example 195 (3c6e).** `F2 R2 D' U2 L2 U' F2 D L2 U' L2 B2 L2 R2 F' L D2 B' F R F' D`

EO `(F2 U2 R' B')`, RZP `(R)`, on the inverse scramble: 3c6e in 5.

What you see:

- U/D edges in the E slice: yellow-blue, white-red, white-orange
- Misoriented corners: yellow-green-red showing red, yellow-blue-orange showing orange, yellow-blue-red showing blue
- E-slice edges out of the slice: green-red, blue-red, green-orange

Reads: 1 pair (on yellow-blue), 1 fake pair, ARM 21.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*anything else*). That group is 93.0% of 3c6e, 23,328 cases: 0 with a DR in 4 or less, 48 in 5, 624 in 6, 22,656 in 7 or more.

Pairs rule, never: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `R' F2 U' D' L2 U' R` (7 moves, too long). The whole attempt: `(F2 U2 R' B' R) R' F2 U' D' L2 U' R`, 12 to DR.

</details>

**Example 196 (5c6e).** `D' R2 U' L2 U R2 B2 U L2 D' R2 U R2 U F' R L' D' L' B' R' F2 L2`

EO `F U' R2 F2 B'`, no RZP needed: 5c6e in 5.

What you see:

- U/D edges in the E slice: white-blue, white-green, white-red
- Misoriented corners: yellow-blue-orange showing orange, white-blue-red showing red, white-green-red showing green, white-green-orange showing orange, white-blue-orange showing orange
- E-slice edges out of the slice: green-orange, blue-red, blue-orange

Reads: 4 pairs (white-blue 2, white-green 1, white-red 1), 0 side pairs, ARM 42.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*4 pairs*). That group is 3.1% of 5c6e, 3,840 cases: 24 with a DR in 4 or less, 232 in 5, 1,200 in 6, 2,384 in 7 or more.

Pairs rule, never: **skip**.

Optimal DR on the inverse: `D' R' U R' D2 L` (6 moves, good). The whole attempt: `F U' R2 F2 B' (D' R' U R' D2 L)`, 11 to DR.

</details>

**Example 197 (4c6e).** `L2 F2 U2 F2 D2 R' D2 B2 R2 D2 R' B2 R U' L B' F2 R' B L F2 R'`

EO `(L F' D' F)`, RZP `(R)`, on the inverse scramble: 4c6e in 5.

What you see:

- U/D edges in the E slice: white-red, white-green, yellow-blue
- Misoriented corners: yellow-blue-red showing red, yellow-blue-orange showing orange, white-green-red showing green, white-green-orange showing green
- E-slice edges out of the slice: blue-orange, blue-red, green-orange

Reads: 3 pairs on 2 edges (white-red 1, yellow-blue 2), ARM 22, bad edges in both layers, corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*anything else*). That group is 96.4% of 4c6e, 90,656 cases: 0 with a DR in 4 or less, 192 in 5, 2,688 in 6, 87,776 in 7 or more.

Pairs rule, never: **skip**.

Optimal DR on the normal side: `U' R B2 D R' U' B2 L` (8 moves, too long). The whole attempt: `(L F' D' F R) U' R B2 D R' U' B2 L`, 13 to DR.

</details>

**Example 198 (3c4e).** `U2 R2 F' B2 L2 B' U2 F L2 B' L2 D2 L2 R2 U' L F2 D' U R U' F`

EO `(L B L' F')`, RZP `(R')`, on the inverse scramble: 3c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-blue
- Misoriented corners: white-blue-red showing blue, white-blue-orange showing orange, yellow-blue-orange showing blue
- E-slice edges out of the slice: green-orange, green-red

Reads: 0 pairs, 2 fake pairs, 0 side pairs, ARM 11, holes on one F/B face (both edges out of the slice have green).

<details><summary>Verdict and the DR after the switch</summary>

Card: **skip** (*anything else*). That group is 79.4% of 3c4e, 14,936 cases: 0 with a DR in 4 or less, 8 in 5, 576 in 6, 14,352 in 7 or more.

Pairs rule, 2+ pairs: **skip**. Fanti's pairs + ARM list: **skip**.

Optimal DR on the normal side: `D2 F2 L U' B2 R2 U' R` (8 moves, too long). The whole attempt: `(L B L' F' R') D2 F2 L U' B2 R2 U' R`, 13 to DR.

</details>

**Example 199 (3c4e).** `D2 F2 L2 F2 R2 U' R2 B2 U2 R2 U' B2 U L' D B' F2 U' B D F2 U'`

EO `F' D' L' D F`, no RZP needed: 3c4e in 5.

What you see:

- U/D edges in the E slice: yellow-red, yellow-orange
- Misoriented corners: white-blue-red showing red, yellow-blue-red showing blue, yellow-green-orange showing green
- E-slice edges out of the slice: green-orange, blue-orange

Reads: 2 pairs, one on each edge, 0 fake pairs, 1 side pair, ARM 10, holes on one R/L face (both edges out of the slice have orange).

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*2 pairs and a side pair*). That group is 6.9% of 3c4e, 1,296 cases: 0 with a DR in 4 or less, 72 in 5, 488 in 6, 736 in 7 or more.

Pairs rule, 2+ pairs: **switch**. Fanti's pairs + ARM list: **switch**.

Optimal DR on the inverse: `U' L' D' L' D' L` (6 moves, good). The whole attempt: `F' D' L' D F (U' L' D' L' D' L)`, 11 to DR.

</details>

**Example 200 (5c4e).** `F2 U F2 U' R2 D' L2 U2 R2 L2 U' R2 D' L' F' R2 L2 D' F L U2 B`

EO `(F L U D F)`, no RZP needed, on the inverse scramble: 5c4e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-orange
- Misoriented corners: white-green-orange showing green, white-blue-red showing red, yellow-green-orange showing green, white-blue-orange showing blue, yellow-blue-orange showing orange
- E-slice edges out of the slice: blue-red, green-orange

Reads: 3 pairs (white-orange 2, yellow-orange 1), 1 fake pair, 2 side pairs, ARM 20.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 pairs, 2+ side pairs*). That group is 2.2% of 5c4e, 2,112 cases: 24 with a DR in 4 or less, 184 in 5, 600 in 6, 1,304 in 7 or more.

Pairs rule, never: **skip**.

Optimal DR on the normal side: `R2 F2 D L D' F2 L` (7 moves, too long). The whole attempt: `(F L U D F) R2 F2 D L D' F2 L`, 12 to DR.

</details>

**Example 201 (4c6e).** `F2 R F2 R' D2 L' U2 R2 D2 U2 R' D2 L' U' F' D2 U2 L' F U R2 B`

EO `(L D' R' L' F)`, no RZP needed, on the inverse scramble: 4c6e in 5.

What you see:

- U/D edges in the E slice: white-orange, yellow-green, yellow-blue
- Misoriented corners: white-blue-orange showing blue, white-blue-red showing red, yellow-green-orange showing orange, yellow-blue-red showing red
- E-slice edges out of the slice: green-orange, blue-orange, blue-red

Reads: 3 pairs on 3 edges (white-orange 1, yellow-green 1, yellow-blue 1), ARM 32, bad edges in both layers, corners 2 white, 2 yellow.

<details><summary>Verdict and the DR after the switch</summary>

Card: **switch** (*3 pairs on three edges, corners 2 and 2 in the layers*). That group is 2.2% of 4c6e, 2,080 cases: 0 with a DR in 4 or less, 56 in 5, 480 in 6, 1,544 in 7 or more.

Pairs rule, never: **skip**.

Optimal DR on the normal side: `U' R D' B2 R U L` (7 moves, too long). The whole attempt: `(L D' R' L' F) U' R D' B2 R U L`, 12 to DR.

</details>
