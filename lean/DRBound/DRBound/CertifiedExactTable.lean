/-
  DRBound.CertifiedExactTable — the machine checks behind the exact optimal lengths: nothing but
  `native_decide` runs of the checkers of `DRBound.Exact`.  (The theorems are in `DRBound.CertifiedExact`;
  the checks are kept in this file of their own so that the long run is not repeated when a statement
  further down is edited.)

    * `exact_model_checked`: nine exhaustive checks of the model — all arrangements of 8 pieces and of 4
      pieces against the 16 symmetries and the 10 moves.  Seconds each.
    * `exact_checked`: one run that builds the table of 1,339,269,120 entries by breadth-first search to
      depth 18, checks every entry against all ten moves and against the symmetries fixing its corner
      representative, checks that no entry exceeds 18, counts the entries by value, and looks up the sample
      scramble.  About 20 minutes on one core and 1.9 GB of memory (6 minutes of search, the rest is the
      check).
-/
import DRBound.Exact

namespace DRBound
open Exact

set_option maxHeartbeats 0

/-- The exhaustive checks of the model, run as compiled code. -/
theorem exact_model_checked : ModelChecked :=
  ⟨by native_decide, by native_decide, by native_decide, by native_decide, by native_decide,
   by native_decide, by native_decide, by native_decide, by native_decide⟩

/-- For `d` = 0 … 18: the weighted number of table entries with value `d` (see `Exact.depthCounts`), and
last the weighted number of entries with value 19 or more. -/
def exactCounts : List Nat :=
  [1, 10, 67, 456, 3079, 19948, 123074, 736850, 4185118, 22630733, 116767872, 552538680, 2176344160,
   5627785188, 7172925794, 3608731814, 224058996, 1575608, 1352, 0]

/-- A scramble with its table value, looked up in the big run: a state that needs 18 moves. -/
def exactSamples : List (List Move × Nat) :=
  [([.U2, .L2, .D, .B2, .U', .B2, .U', .L2, .D, .B2, .R2, .U, .R2, .U, .R2, .U2, .R2, .U'], 18)]

/-- **The big check.**  Search to depth 18; check all 2768 rows (every entry: `cap` = 256); no entry exceeds
18; the counts; the sample. -/
theorem exact_checked : exactCheck 18 2768 256 18 19 exactCounts exactSamples = true := by
  native_decide

end DRBound
