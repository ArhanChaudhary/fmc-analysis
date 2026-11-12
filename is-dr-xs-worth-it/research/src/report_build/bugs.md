# DR-xs: corrections

*Goes with the write-up "Is DR-xs worth it?", but reads on its own. The write-up has the measurements and the tables.*

November 2026. A date in brackets is a link to that message on the FMC solvers Discord (#fmc-theory or #fmc-discussion). Docs are listed with links at the end.

**What everything below is measured against:**

- **All 768 kinds of DR-xs state per colour**, with the fewest slices and the fewest face turns to a real DR for each, proved in Lean. Turns are HTM, a slice counts as its two outer turns, and all cancelling is done.
- **Searches over all 2,217,093,120 cosets of the DR group** for the nearest DR, DR-1s and DR-2s 8fe under each move rule. They reproduce the known DR-length counts and the dr-fe distribution trangium posted.
- **200,000 random DR-1s states and 5,000 random DR-2s 8fe states**, each finished as well as the method's form allows (setup, slice or slices, DR finish), using the exact optimal finish of every DR state from the first study.
- **The 500 scrambles** of the first study, with every DR-1s of 8 or less and DR-2s 8fe of 9 or less from a slice EO, each with a written solution that was replayed.

Section A is what's wrong in the docs, B what's wrong in things said in the channels, each with its example. Most of what the docs and the channels say checks out; that is in the write-up's section 8, the claims checked one by one.

---

## A. The docs

**A1. EO Meta Comparison (Rodney): the fix costs it assumes.**
The doc says "we assume 1 slice can be fixed in 3 moves, and 2 slices can be fixed in 5 moves", and its tables are the standard table shifted by those amounts. Counted exactly, from the state alone, and with one turn of the slice cancelling into the move before it, which is how Rodney counts the 3 ("one ht, one qt, and -1 cancellation on the slice", [[T12410]]):

| | Fewest | Most | Average from the state | Average, one slice turn cancelling |
|---|---:|---:|---:|---:|
| DR-1s to DR | {= FIXMIN(1) =} | {= FIXMAX(1) =} | {= FIXAVG(1) =} | {= f2(float(FIXAVG(1)) - 1) =} |
| DR-2s to DR | {= FIXMIN(2) =} | {= FIXMAX(2) =} | {= FIXAVG(2) =} | {= f2(float(FIXAVG(2)) - 1) =} |
| DR-3s to DR | {= FIXMIN(3) =} | {= FIXMAX(3) =} | {= FIXAVG(3) =} | {= f2(float(FIXAVG(3)) - 1) =} |

So in Rodney's own way of counting, the 3 and the 5 are each about a move short ({= f2(float(FIXAVG(1)) - 1 - 3) =} and {= f2(float(FIXAVG(2)) - 1 - 5) =}), and about two from the state alone. The median DR-1s layout is {= FIXMED(1) - 1 =} with the cancel and {= FIXMED(1) =} without (B2). The 6-turn layout in B2 still takes {= len(WIT['six']['fix'].split()) - 1 =} with the cancel.

**A2. Simon's slice-DR doc: the table for step 3.**
"Num Cases out of 70" at 2, 3, 4, 5, 6 moves is given as 1, 4, 9, 40, 16, with "~4.9 moves on average". Taking the better direction of the last trigger move as the doc does, I get {= SIMON() =}: thirteen layouts have a 4-turn fix, not nine. The average stays 4.9. The thirteen, with the corners on F/B, the fixing slice `R L` and the last trigger move a quarter turn of U or D:

{{simon13}}

Each fix can be checked on a cube: do a DR, do the fix backwards, and the fix brings the DR back.

---

## B. Said in the channels

**B1. "All edges misoriented (12 bad) -> FB on UD will be extra-good -1s"** (Rodney, [[T11232]]).
It is a DR-2s, not a DR-1s: four flipped edges, all of one slice, with the centers two slices off. {= W12() =}
trangium said they could not get that line to work ([[T11234]]) and proposed "FB-colored misoriented, others oriented" instead: that one is right, it gives a DR-1s whose four flipped edges belong to one slice. count quackula's 12-bad notes say the same for green/blue: "This is a DR-2s 4fe." The other five lines of Rodney's list are right.

**B2. "I would guess the distribution is basically flat", and 3 moves as the median** for DR-1s to DR (Rodney, [[T12409]], [[T12410]]).
Of the 70 layouts, {= FIX70(2) =} needs 2 turns, {= FIX70(3) =} need 3, {= FIX70(4) =} need 4, {= FIX70(5) =} need 5 and {= FIX70(6) =} need 6. Rodney's 3 is one half turn, one quarter turn and the slice with one of its two turns cancelling; counted that way the median layout is 4, and 5 from scratch. A 6: after `{= W6() =}` the shortest fix is 6 turns (`{= WIT['six']['fix'] =}`). Right after a trigger, with the slice free to merge into its last move, the best case is 0 extra turns but most layouts still need 5.

**B3. "If you have 8 bad edges, where all the good edges belong to the same slice, then you can orient the corners that correspond to the good edges along any axis and you are guaranteed an extra-good dr-xs"** (Rodney, [[T11255]]).
Take the EO axis as F/B and the four good edges as the E-slice edges, so the corners in question are the white/yellow ones. On U/D they give a DR-2s with all eight edges flipped and the centers right, and on R/L a DR-2s with no edge flipped: in both there is no flipped edge to place, which is Rodney's extra-good. On F/B, the faces of the EO axis itself, they give a DR-1s that is not extra-good. A flipped edge "belongs to" its home slice here, the slice it sits in when solved (as in the write-up, 5.4). By the slice they belong to, the four flipped edges split 2-2 in {= WS['home_split']['2-2'] =} of the {= sum(WS['home_split'].values()) =} layouts, 3-1 in {= WS['home_split']['3-1'] =} and 4-0 in {= WS['home_split']['4-0'] =}. By where they sit, they are together in the E-slice places in all {= WS['place_split']['4-0'] =}, which is the write-up's "wrong slice" case: every layout takes `{= WS['witness']['fix'] =}` ({= WS['witness']['turns'] =} turns) to a DR, no better than an ordinary DR-1s. So "any axis" holds for two of the three. `{= WIT['eight_bad_split']['scramble'] =}` has 8 bad edges on F/B with the four good ones the E-slice edges, and white/yellow on F or B at every corner. Its flipped edges are {= ', '.join(n for n, k in WS['witness']['pieces'] if k == 'M') =} (M slice) and {= ', '.join(n for n, k in WS['witness']['pieces'] if k == 'S') =} (S slice), a {= WS['witness']['home_split'] =}, sitting at {= ', '.join(WS['witness']['places']) =}. nissy's shortest DR on any axis is `{= WS['witness']['nissy_dr'].rsplit(' (', 1)[0] =}` ({= WS['witness']['nissy_dr_len'] =}), and on the inverse `{= WS['witness']['nissy_dr_inverse'].rsplit(' (', 1)[0] =}` ({= WS['witness']['nissy_dr_inverse_len'] =}), so no single slice turn reaches DR from either side.

---

## Docs referred to

- Rodney Kinney, [EO Meta Comparison](https://docs.google.com/document/d/131VWYrL3Z4t6p0fBGkHZ73w6arF8A7PEqRuNjsIQMGo), Jan 2026.
- Simon, [Slice DR](https://docs.google.com/document/d/15zDJ9_FQIYVgHLbt1eHdOPtEp10jFOOae_U8DTaH7tk), Jul 2025.
- count quackula, [12 bad dr-xs notes](https://docs.google.com/document/d/1-anqtLsBGg_oBvzz1TTf_6Mjsypv4jMkFhB9E8cwkQM), Feb 2026.
