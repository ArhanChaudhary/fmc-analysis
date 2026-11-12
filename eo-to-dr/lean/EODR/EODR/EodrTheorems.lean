/-
  EODR.EodrTheorems — checked statements, part D (see README.md).  Every one is a closed statement about the definitions in Cube / Pieces /
  Search / Eo / Layouts / Eodr, proved by running them: `native_decide` evaluates the statement with compiled code
  and accepts the answer (this trusts the Lean compiler; see README.md).  Statements that are plain arithmetic on
  numbers are proved by `decide` (Lean's kernel alone).

  Axes: 0 = R/L, 1 = U/D, 2 = F/B.  Moves: indices into NAMES = U U2 U' D D2 D' R R2 R' L L2 L' F F2 F' B B2 B'.
  Reading aid:  `hist l` = list of (value, how many times it occurs in l), by value.
-/
import EODR.Eo
import EODR.Layouts
import EODR.Eodr
import EODR.Parse

namespace EODR
open cube pieces

set_option maxHeartbeats 0

/-! ## D. EO → DR, exact over the 1,082,565 cosets -/

/-- The BFS over (corner twists, E-slice places) with the 14 EO-keeping turns: its table passes the check of
`search.ruleHolds` (so each entry is the fewest such turns to DR on U/D), the states reached are exactly the
twist vectors with sum ≡ 0 mod 3 times the 4-place masks, there are 1,082,565 of them, and the per-case table
of the options "eo", "eo_switchF", "eo_switchB" is, row for row, the research's `eodr_exact.tsv`. -/
theorem eodr_matches_study :
    eodr.run eodr.N = ⟨true, true, 1082565, parse.eodrRows⟩ := by native_decide

theorem eodr_states : 2187 * 495 = 1082565 := by decide

/-- Readings of that table (read off the research's rows, equal to Lean's by `eodr_matches_study`). -/
theorem eodr_facts :
    let r := parse.eodrRows
    -- EO kept, one DR axis: Cale's distribution, Σ = 8447364 (mean 7.8031), ≤ 6 for 64103
    eodr.total r "eo" = [1, 2, 17, 134, 1065, 8190, 54694, 267576, 560568, 187204, 3114, 0] ∧
    eodr.weighted (eodr.total r "eo") = 8447364 ∧ ((eodr.total r "eo").take 7).sum = 64103 ∧
    -- last EO turn inverted if better (F or B the same): Σ = 8164226 (mean 7.5416), ≤ 6 for 102533
    eodr.total r "eo_switchF" = [1, 4, 29, 228, 1809, 13736, 86726, 365050, 523932, 90098, 952, 0] ∧
    eodr.total r "eo_switchB" = eodr.total r "eo_switchF" ∧
    eodr.weighted (eodr.total r "eo_switchF") = 8164226 ∧ ((eodr.total r "eo_switchF").take 7).sum = 102533 ∧
    -- 4c4e: 70560 cosets, ≤ 6 for 13576, with the switch 19798 (EO-DR-22, EO-DR-79)
    (eodr.caseRow r 4 4 "eo").sum = 70560 ∧ ((eodr.caseRow r 4 4 "eo").take 7).sum = 13576 ∧
    ((eodr.caseRow r 4 4 "eo_switchF").take 7).sum = 19798 ∧
    -- the five most common cases (EO-DR-32)
    (eodr.caseRow r 6 6 "eo").sum = 137984 ∧ (eodr.caseRow r 5 6 "eo").sum = 125440 ∧
    (eodr.caseRow r 6 4 "eo").sum = 103488 ∧ (eodr.caseRow r 5 4 "eo").sum = 94080 ∧
    (eodr.caseRow r 4 6 "eo").sum = 94080 ∧
    (r.all fun (_, _, o, h) => o != "eo" || h.sum ≤ 137984) := by
  native_decide

/-- The research's histogram of the eo = 0 part of `eo-fb_dr.u8` (its own file) is the same distribution. -/
theorem eo0_hist_matches_study :
    parse.eo0Hist = [(0, 1), (1, 2), (2, 17), (3, 134), (4, 1065), (5, 8190), (6, 54694), (7, 267576),
      (8, 560568), (9, 187204), (10, 3114)] := by
  native_decide

/-- Digits: 8447364/1082565 = 7.8031…, 8164226/1082565 = 7.5415(57…), 64103/1082565 = 5.92…%,
102533/1082565 = 9.47…%, 13576/70560 = 19.24…%, 19798/70560 = 28.05(8…)%, 1082565/70560 = 15.34…,
3114/1082565 = 0.287…%, 137984/1082565 = 12.74(6…)%. -/
theorem eodr_digits :
    8447364 * 10000 / 1082565 = 78031 ∧ 8164226 * 1000000 / 1082565 = 7541557 ∧
    64103 * 10000 / 1082565 = 592 ∧ 102533 * 10000 / 1082565 = 947 ∧
    13576 * 10000 / 70560 = 1924 ∧ 19798 * 100000 / 70560 = 28058 ∧
    1082565 * 100 / 70560 = 1534 ∧ 3114 * 100000 / 1082565 = 287 ∧ 137984 * 100000 / 1082565 = 12746 := by
  decide

/-- Corner twists alone, over the 2,187 twist vectors (sum ≡ 0 mod 3): how many have k twisted corners
(EO-DR-18: 3 for 112, 4 for 420); of the 616 with six twisted, 56 have all six twisted the same way and 560 three
each way (EO-DR-5: 1 in 11). -/
theorem twist_counts :
    eodr.CO_VALID.length = 2187 ∧
    eodr.twistedHist = [(0, 1), (2, 56), (3, 112), (4, 420), (5, 560), (6, 616), (7, 336), (8, 86)] ∧
    eodr.sixTwisted = (56, 560) := by
  native_decide

end EODR
