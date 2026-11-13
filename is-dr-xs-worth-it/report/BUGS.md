# DR-xs: corrections

*Goes with the write-up "Is DR-xs worth it?", but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs are listed with links at the end.

**What everything below is measured against:**

- **All 768 kinds of DR-xs state per colour**, with the fewest slices and the fewest face turns to a real DR for each, proved in Lean. Turns are HTM, a slice counts as its two outer turns, and all cancelling is done.
- **Searches over all 2,217,093,120 cosets of the DR group** for the nearest DR, DR-1s and DR-2s 8fe under each move rule. They reproduce the known DR-length counts and the dr-fe distribution trangium posted.
- **200,000 random DR-1s states and 5,000 random DR-2s 8fe states**, each finished as well as the method's form allows (setup, slice or slices, DR finish), using the exact optimal finish of every DR state from the first study.
- **The 500 scrambles** of the first study, with every DR-1s of 8 or less and DR-2s 8fe of 9 or less from a slice EO, each with a written-out solution, replayed on the scramble.

Section A is what's wrong in the docs, B what's wrong in things said in the channels, each with its example. Most of what the docs and the channels say checks out; that's in the write-up's section 8, the claims checked one by one.

---

## A. The docs

**A1. EO Meta Comparison (Rodney): the fix costs it assumes.**
The doc says "we assume 1 slice can be fixed in 3 moves, and 2 slices can be fixed in 5 moves", and its tables are the standard table shifted by those amounts. Here are the exact counts, from the state alone and with one turn of the slice cancelling into the move before it, which is how Rodney counts the 3 ("one ht, one qt, and -1 cancellation on the slice", [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560296978137485322)). Each row is a step; the columns are its fewest, most and average face turns:

| Step | Fewest turns | Most turns | Average turns from the state | Average turns, one slice turn cancelling |
|---|---:|---:|---:|---:|
| DR-1s to DR | 2 | 6 | 5.17 | 4.17 |
| DR-2s to DR | 4 | 9 | 6.83 | 5.83 |
| DR-3s to DR | 6 | 10 | 8.50 | 7.50 |

So in Rodney's own way of counting, the 3 and the 5 are each about a move short (1.17 and 0.83), and about two from the state alone. The median DR-1s layout is 4 with the cancel and 5 without (B2). The 6-turn layout in B2 still takes 5 with the cancel.

**A2. Simon's slice-DR doc: the table for step 3.**
"Num Cases out of 70" at 2, 3, 4, 5, 6 moves is given as 1, 4, 9, 40, 16, with "~4.9 moves on average". Taking the better direction of the last trigger move like the doc does, I get 1, 4, 13, 36, 16: thirteen layouts have a 4-turn fix, not nine. The average stays 4.9. The thirteen, with the corners on F/B, the fixing slice `R L` and the last trigger move a quarter turn of U or D:

Each row is one layout; the two middle columns are its fewest turns to a real DR as the layout stands and after turning the last trigger move the other way.

| Flipped edges at | Turns to DR as it is | Turns to DR with the last move the other way | Fix as it is |
|---|---:|---:|---|
| BL DB UB FR | 4 | 5 | `L2 F R L` |
| BL DB UF BR | 4 | 5 | `D2 B R L` |
| BL DF UF FR | 4 | 5 | `R2 B R L` |
| BL FL BR FR | 4 | 4 | `F B R L` |
| FL DB UB BR | 4 | 5 | `R2 F R L` |
| FL DF UB FR | 4 | 5 | `D2 F R L` |
| FL DF UF BR | 4 | 5 | `L2 B R L` |
| BL DB UB BR | 5 | 4 | `R2 L2 F R L` |
| BL DB UF FR | 5 | 4 | `L2 U2 F R L` |
| BL DF UB FR | 5 | 4 | `L2 D2 F R L` |
| FL DB UF BR | 5 | 4 | `D2 L2 B R L` |
| FL DF UB BR | 5 | 4 | `U2 L2 B R L` |
| FL DF UF FR | 5 | 4 | `U2 D2 F R L` |

You can check each fix on a cube: do a DR, do the fix backwards, and the fix brings the DR back.

---

## B. Said in the channels

**B1. "All edges misoriented (12 bad) -> FB on UD will be extra-good -1s"** (Rodney, [19 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474226073247027220)).
It is a DR-2s, not a DR-1s: four flipped edges, all of one slice, with the centers two slices off. `B' D2 L2 U2 F2 D2 F L2 F2 D2 R2 F2 U' D' L' F' B' U'` has all twelve edges bad on F/B and green or blue on the U and D face of every corner; it has 4 flipped edges, needs 2 slices, and a shortest fix to DR is `U B F L U D` (6 turns).
trangium said they could not get that line to work ([19 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474238124333858836)) and proposed "FB-colored misoriented, others oriented" instead: that one is right, it gives a DR-1s whose four flipped edges belong to one slice. count quackula's 12-bad notes say the same for green/blue: "This is a DR-2s 4fe." The other five lines of Rodney's list are right.

**B2. "I would guess the distribution is basically flat", and 3 moves as the median** for DR-1s to DR (Rodney, [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560294279010717737), [15 Oct 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1560296978137485322)).
Of the 70 layouts, how many need each number of turns:

| Turns to a real DR | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|
| layouts | 1 | 2 | 9 | 30 | 28 |

Rodney's 3 is one half turn, one quarter turn and the slice with one of its two turns cancelling; counted that way the median layout is 4, and 5 from scratch. A 6:

```
U R2 F2 D' B2 U2 L2 D R' L' B' L2 U2 F2 // scramble
F2 U2 L2 B R L // shortest fix, 6 turns
```

Right after a trigger, with the slice free to merge into its last move, the best case is 0 extra turns, but most layouts still need 5.

**B3. "If you have 8 bad edges, where all the good edges belong to the same slice, then you can orient the corners that correspond to the good edges along any axis and you are guaranteed an extra-good dr-xs"** (Rodney, [20 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474455821978042472)).
Take the EO axis as F/B and the four good edges as the E-slice edges, so the corners in question are the white/yellow ones. Each row is where their white or yellow faces go:

| Corners oriented on | You get | Extra-good? |
|---|---|---|
| U/D | a DR-2s with all eight edges flipped and the centers right | yes: no flipped edge to place |
| R/L | a DR-2s with no edge flipped | yes: no flipped edge to place |
| F/B, the faces of the EO axis itself | a DR-1s | no |

So "any axis" holds for two of the three. A flipped edge "belongs to" its home slice here, the slice it sits in when solved (as in the write-up, 5.4). On F/B, by the slice they belong to, the four flipped edges split like this over the 70 layouts:

| Split between their home slices | 2-2 | 3-1 | 4-0 |
|---|---:|---:|---:|
| layouts | 36 | 32 | 2 |

By where they sit, though, they're together in the E-slice places in all 70, which is the write-up's "wrong slice" case: every layout takes this to a DR, no better than an ordinary DR-1s:

```
F B R L // fix to DR, 4 turns
```

An example with 8 bad edges on F/B, the four good ones the E-slice edges, and white/yellow on F or B at every corner:

```
U D2 L2 D B2 L2 B2 D R2 F2 U' R' L F' B' // scramble
```

Its flipped edges are DB, DF, UF (M slice) and UR (S slice), a 3-1, sitting at BL, BR, FL, FR. nissy's shortest DRs, on any axis:

```
F B R L // normal (4)
B2 U' B2 U R L // on the inverse (6)
```

so no single slice turn reaches DR from either side.

---

## Docs referred to

- Rodney Kinney, [EO Meta Comparison](https://docs.google.com/document/d/131VWYrL3Z4t6p0fBGkHZ73w6arF8A7PEqRuNjsIQMGo), Jan 2026.
- Simon, [Slice DR](https://docs.google.com/document/d/15zDJ9_FQIYVgHLbt1eHdOPtEp10jFOOae_U8DTaH7tk), Jul 2025.
- count quackula, [12 bad dr-xs notes](https://docs.google.com/document/d/1-anqtLsBGg_oBvzz1TTf_6Mjsypv4jMkFhB9E8cwkQM), Feb 2026.
