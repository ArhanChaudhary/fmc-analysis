/-
  HTRRoutes.QtCosetTheorems — checked statements, part E: which HTR cosets are one and two quarter turns from HTR
  (see README.md).  `native_decide` runs the statement as compiled code; the definitions are in `QtCosets.lean`,
  a separate file so that they are compiled before the statements run them.
-/
import HTRRoutes.QtCosets

namespace HTRRoutes

set_option maxHeartbeats 0

open qtcos cosets pieces corners in
/-- **One quarter turn from HTR is exactly 4a1 4e.** The half-turn closure of (HTR, then one quarter turn) is a
set of 432 HTR cosets, closed under half turns, and a coset is in it exactly when its label is "4a1 4e". So every
4a1 4e state is finished by one quarter turn and half turns (the study's "reduction to 1q"), and the subset just
before HTR on any finish, the state before its last quarter turn, is 4a1 4e. -/
theorem qt1_is_4a1_4e :
    closedUnderHalf S1D = true ∧
    ((List.range N).filter fun x => valid x && s1 x).length = 432 ∧
    (List.range N).all (fun x => !valid x || (s1 x == (lab x == "4a1 4e"))) = true ∧
    s1 GOAL = false := by
  native_decide

open qtcos cosets pieces corners in
/-- **Two quarter turns from HTR, and no fewer**: all of 4a2 and 4b2 (every edge count), 0c0 with 2, 4, 6 or 8 bad
edges, and one of the two 0c0 0e cosets (the other is HTR itself). -/
theorem qt2_cosets :
    closedUnderHalf S2D = true ∧
    tallyOf s2 = [("0c0 0e", 1), ("0c0 2e", 32), ("0c0 4e", 72), ("0c0 6e", 32), ("0c0 8e", 2),
                  ("4a2 0e", 24), ("4a2 2e", 384), ("4a2 4e", 432),
                  ("4b2 0e", 96), ("4b2 2e", 1536), ("4b2 4e", 1728)] ∧
    tallyOf (fun x => x == GOAL) = [("0c0 0e", 1)] := by
  native_decide

end HTRRoutes
