/-
  HTRRoutes.HtrTheorems — checked statements, part B: the HTR group (see README.md).  `native_decide` runs the
  statement as compiled code; `decide` is Lean's kernel alone (plain arithmetic).
-/
import HTRRoutes.HtrGroup
import HTRRoutes.Parse

namespace HTRRoutes
open pieces

set_option maxHeartbeats 0

/-! ## B. The HTR group and its half-turn-only finishes -/

/-- The coordinate of `HtrGroup.lean` is faithful: decoding is one to one on every part, slot 0 is the solved cube,
and every half turn's part tables give exactly the arrangements the move gives (and keep each part in its places). -/
theorem htr_coordinate_ok : htr.decodeOk = true ∧ htr.partsFollow = true := by native_decide

/-- The BFS from the solved cube with the six half turns: its table passes `search.ruleHolds` (each entry is the
fewest half turns that solve the state), it reaches 663,552 states, and its distance histogram is, row for row,
the half_turn_optimal column of the research's `out/checks/htr_states.tsv` (DougCube's table). -/
theorem htr_group_matches_study : htr.run = ⟨true, 663552, parse.htrHalfHist⟩ := by native_decide

/-- That histogram: half turns 0 … 15 solve 1, 6, 27, 120, 519, 1932, 6484, 20310, 55034, 113892, 178495, 179196,
89728, 16176, 1488, 144 states; the most is 15. -/
theorem htr_hist :
    parse.htrHalfHist = [(0, 1), (1, 6), (2, 27), (3, 120), (4, 519), (5, 1932), (6, 6484), (7, 20310),
      (8, 55034), (9, 113892), (10, 178495), (11, 179196), (12, 89728), (13, 16176), (14, 1488), (15, 144)] ∧
    (parse.htrHalfHist.map (·.2)).sum = 663552 ∧
    (parse.htrHalfHist.map fun (d, n) => d * n).sum = 6724652 := by native_decide

/-- The corner part and the edge part: the reached states use 96 corner values and 6,912 edge values (half of the
24³ arrangements of the M, S and E pieces).  With `htr_mean_digits`' 96 · 6,912 = 663,552: every one of the 96
corner values occurs with every one of the 6,912 edge values. -/
theorem htr_parts : htr.partsReached = (96, 6912) := by native_decide

/-- The mean: 6724652 / 663552 = 10.1343255690…, which rounds to 10.13432557 (the research's check prints
10.13432557 for both DougCube's table and its own; DougCube's 10.13). -/
theorem htr_mean_digits :
    96 * 6912 = 663552 ∧ 24 * 24 * 24 / 2 = 6912 ∧
    6724652 * 10 ^ 10 / 663552 = 101343255690 ∧
    (6724652 * 10 ^ 8 * 2 + 663552) / (2 * 663552) = 1013432557 := by decide

end HTRRoutes
