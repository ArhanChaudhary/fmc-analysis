# DR-xs: corrections

*Goes with the write-up "Is DR-xs worth it?", but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs are listed with links at the end.

**What everything below is measured against:**

- **All 768 kinds of DR-xs state per colour**, with the fewest slices and the fewest face turns to a real DR for each, proved in Lean. Turns are HTM, a slice counts as its two outer turns, and all cancelling is done.
- **What each edge-orientation pattern leads to** (the write-up's Appendix B): for every pattern that is all good or all bad slice by slice, and each pair of faces for the corners, the kind of DR-xs you land on.

Section A is what's wrong in a doc, B what's wrong in something said in the channels, each with its example. Most of what the docs and the channels say checks out. That's in the write-up's section 8, the claims checked one by one, and so are the guesses and working assumptions the numbers don't bear out.

---

## A. The docs

**A1. Simon's slice-DR doc: the table for step 3.**
"Num Cases out of 70" at 2, 3, 4, 5, 6 moves is given as 1, 4, 9, 40, 16, with "~4.9 moves on average". Taking the better direction of the last trigger move like the doc does, I get 1, 4, 13, 36, 16: thirteen layouts have a 4-turn fix, not nine. The average stays 4.9. The thirteen, with the corners on F/B, the fixing slice `R L` and the last trigger move a quarter turn of U (with a D trigger the counts 1, 4, 13, 36, 16 are the same, but the thirteen are a different set: for example `BL DB UF BR` and `FL DF UB FR` take 3 turns there):

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

You can check each fix on a cube: do a DR, do the fix backwards, and the fix brings the DR back. ✓ Lean: the 1, 4, 13, 36, 16 and every row with a `U` as the last trigger move.

---

## B. Said in the channels

**B1. "All edges misoriented (12 bad) -> FB on UD will be extra-good -1s"** (Rodney, [19 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474226073247027220), the first of three lines given under "As far as I can tell, there are three others").
The four flipped edges do all belong to one slice, but the centers are two slices off: it's a DR-2s, not a DR-1s. `B' D2 L2 U2 F2 D2 F L2 F2 D2 R2 F2 U' D' L' F' B' U'` has all twelve edges bad on F/B and green or blue on the U and D face of every corner; it has 4 flipped edges, needs 2 slices, and a shortest fix to DR is `U B F L U D` (6 turns).
trangium caught it within the hour ([19 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474238124333858836)): "hmm I can't get the 12 bad one to work, think it should be FB-colored misoriented, others oriented". That line is right: it gives a DR-1s whose four flipped edges belong to one slice. Rodney's restatement the next day ([20 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1474455821978042472)) starts from 8 bad edges only. count quackula's 12-bad notes ([2 Feb 2026](https://discord.com/channels/1007840975726575667/1007841335434285126/1467952398939983964)) had it for green/blue: "This is a DR-2s 4fe." The other five lines of Rodney's list are right. ✓ Lean: the example (twelve bad, 4 flipped, 2 slices, the 6-turn fix).

---

## Docs referred to

- Simon, [Slice DR](https://docs.google.com/document/d/15zDJ9_FQIYVgHLbt1eHdOPtEp10jFOOae_U8DTaH7tk), Jul 2025.
- count quackula, [12 bad dr-xs notes](https://docs.google.com/document/d/1-anqtLsBGg_oBvzz1TTf_6Mjsypv4jMkFhB9E8cwkQM), Feb 2026.
