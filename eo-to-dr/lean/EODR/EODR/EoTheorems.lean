/-
  EODR.EoTheorems — checked statements, part B (see README.md).  Every one is a closed statement about the definitions in Cube / Pieces /
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

/-! ## B. EO on one axis: the 2,048 states -/

/-- On each axis, the BFS table passes the independent check of `search.ruleHolds` (so each entry is the fewest
face turns to EO), and the states reached are exactly the 2,048 masks with an even number of bad edges. -/
theorem eo_table_checked : ∀ Y ∈ List.range 3, eo.distRule Y = true ∧ eo.reachedIsEven Y = true := by
  native_decide

theorem eo_states : eo.STATES.length = 2048 := by native_decide

/-- Fewest face turns to EO on one axis (the same on all three): 0 for 1 state, 1 for 2, 2 for 25, 3 for 202,
4 for 620, 5 for 900, 6 for 285, 7 for 13.  So at most 7. -/
theorem eo_distance_hist : ∀ Y ∈ List.range 3,
    eo.distHist Y = [(0, 1), (1, 2), (2, 25), (3, 202), (4, 620), (5, 900), (6, 285), (7, 13)] := by
  native_decide

/-- The distances sum to 9439: the mean over the 2,048 states is 9439/2048. -/
theorem eo_distance_sum : ∀ Y ∈ List.range 3, eo.distSum Y = 9439 := by native_decide

/-- 9439/2048 = 4.60888… -/
theorem eo_mean_digits : 9439 * 100000 / 2048 = 460888 := by decide

/-- Fewest turns to EO by number of bad edges (on each axis): number of states with b bad edges and their
distance histogram.  (1, 66, 495, 924, 495, 66, 1 states.) -/
theorem eo_by_bad : ∀ Y ∈ List.range 3, eo.distByBad Y =
    [(0, [(0, 1)]),
     (2, [(3, 40), (4, 22), (5, 4)]),
     (4, [(1, 2), (2, 24), (3, 134), (4, 276), (5, 56), (6, 3)]),
     (6, [(3, 8), (4, 200), (5, 556), (6, 160)]),
     (8, [(2, 1), (3, 20), (4, 122), (5, 284), (6, 68)]),
     (10, [(6, 54), (7, 12)]),
     (12, [(7, 1)])] := by
  native_decide

/-- Number of canonical EO solutions on F/B that reach EO for the first time at their last turn, over the 2,048
states: for each length r = 0 … 8, the sum over the states (so the mean is this / 2048), the most any state has,
the most any state has of length ≤ r, the sum of those of length ≤ r, and the number of states with none of
length ≤ r. -/
theorem eo_solution_counts :
    eo.countSums 2 = [1, 4, 54, 720, 9612, 128176, 1710088, 22816024, 304466248] ∧
    eo.countMax 2 = [1, 2, 4, 16, 72, 384, 3920, 43748, 500774] ∧
    eo.cumMax 2 = [1, 2, 4, 20, 92, 476, 4332, 48080, 548854] ∧
    eo.cumSums 2 = [1, 5, 59, 779, 10391, 138567, 1848655, 24664679, 329130927] ∧
    eo.noneLe 2 = [2047, 2045, 2020, 1818, 1198, 298, 13, 0, 0] := by
  native_decide

/-- 138567/2048 = 67.6596… (the mean number of EOs of at most 5 turns). -/
theorem eo_le5_mean_digits : 138567 * 10000 / 2048 = 676596 := by decide

/-- The whole table, state by state (bad edges, fewest turns, n₀ … n₈), is the research's `eo_axis.tsv`
(as a list of 2,048 rows, both sides sorted). -/
theorem eo_axis_matches_study : eo.rows 2 = parse.eoAxisRows := by native_decide

end EODR
