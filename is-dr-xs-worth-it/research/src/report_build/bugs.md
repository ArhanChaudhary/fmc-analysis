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
"Num Cases out of 70" at 2, 3, 4, 5, 6 moves is given as 1, 4, 9, 40, 16, with "~4.9 moves on average". Taking the better direction of the last trigger move like the doc does, I get {= SIMON() =}: thirteen layouts have a 4-turn fix, not nine. The average stays 4.9. The thirteen, with the corners on F/B, the fixing slice `R L` and the last trigger move a quarter turn of U (with a D trigger the counts {= SIMON() =} are the same, but the thirteen are a different set: for example `BL DB UF BR` and `FL DF UB FR` take 3 turns there):

{{simon13}}

You can check each fix on a cube: do a DR, do the fix backwards, and the fix brings the DR back. ✓ Lean: the {= SIMON() =} and every row with a `U` as the last trigger move.

---

## B. Said in the channels

**B1. "All edges misoriented (12 bad) -> FB on UD will be extra-good -1s"** (Rodney, [[T11232]], the first of three lines given under "As far as I can tell, there are three others").
The four flipped edges do all belong to one slice, but the centers are two slices off: it's a DR-2s, not a DR-1s. {= W12() =}
trangium caught it within the hour ([[T11234]]): "hmm I can't get the 12 bad one to work, think it should be FB-colored misoriented, others oriented". That line is right: it gives a DR-1s whose four flipped edges belong to one slice. Rodney's restatement the next day ([[T11255]]) starts from 8 bad edges only. count quackula's 12-bad notes ([[T10982]]) had it for green/blue: "This is a DR-2s 4fe." The other five lines of Rodney's list are right. ✓ Lean: the example (twelve bad, 4 flipped, 2 slices, the 6-turn fix).

---

## Docs referred to

- Simon, [Slice DR](https://docs.google.com/document/d/15zDJ9_FQIYVgHLbt1eHdOPtEp10jFOOae_U8DTaH7tk), Jul 2025.
- count quackula, [12 bad dr-xs notes](https://docs.google.com/document/d/1-anqtLsBGg_oBvzz1TTf_6Mjsypv4jMkFhB9E8cwkQM), Feb 2026.
