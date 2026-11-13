/-
  HTFirst.Table — the one run of DRBound's exact table (`mkTable 18`: rebuilds the 1.34-billion-entry table) over
  the worked DRs of the page and the recounted sample, kept apart so that the table is built once.  The theorems
  are in `HTFirst.Examples`.
-/
import HTFirst.Finishes
import HTFirst.Data

namespace HTFirst
open DRBound

set_option maxHeartbeats 0

/-- For each worked DR: the optimal length and the complete list of optimal finishes are the printed ones.  For
each recounted state: the summary of its optimal finishes is the study's row. -/
theorem table_run :
    tableRun 18 (examples.map fun c => st c.scr) (recount.map fun c => st c.2.1) =
      (examples.map fun c => (c.opt, c.fin.map fun f => drMoves f.1), recount.map fun c => c.2.2) := by
  native_decide

end HTFirst
