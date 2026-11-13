/-
  DRBound.Census.Count — counting table entries by a feature and by the table value.

  `census T nk size prep code` goes once through the rows `0 … nk-1` of the table `T` (`DRBound.Exact`: row `k`
  holds the 40320 × 12 states whose corners are the representative of corner class `k`).  The entry
  `(k, e, s)` is counted `classWeight k` times in the cell `code (prep k) e * 19 + (its table value)`.
  `prep k` is computed once per row (everything that depends on the corner arrangement), `code (prep k) e`
  once per arrangement `e` of the U/D-layer edges; the feature does not depend on the E slice.

  `DRBound.Census.Sums` proves what the cells are (`census_spec`), `DRBound.Census.Orbit` that a cell is a
  number of states.
-/
import DRBound.Exact

set_option compiler.extract_closed false

namespace DRBound
namespace Census
open Exact

/-- Optimal lengths are 0 … 18: 19 cells per feature value. -/
def nd : Nat := 19

/-- One U/D-edge arrangement of one row: its 12 entries, each counted `w` times, cells `b + value`. -/
@[inline] def countEdge (T : ByteArray) (w k e b : Nat) (acc : Array Nat) : Array Nat :=
  Nat.fold 12 (fun s _ acc => acc.modify (b + tv T (idx3 k e s)) (· + w)) acc

/-- One row. -/
@[specialize] def countRow {C : Type} (T : ByteArray) (code : C → Nat → Nat) (w k : Nat) (c : C)
    (acc : Array Nat) : Array Nat :=
  Nat.fold 40320 (fun e _ acc => countEdge T w k e (code c e * nd) acc) acc

/-- **The census**: cell `f * 19 + d` = the number of entries `(k, e, s)`, `k < nk`, with feature value
`code (prep k) e = f` and table value `d`, each counted `classWeight k` times. -/
@[specialize] def census {C : Type} (T : ByteArray) (nk size : Nat) (prep : Nat → C) (code : C → Nat → Nat) :
    Array Nat :=
  Nat.fold nk (fun k _ acc => countRow T code (classWeight k) k (prep k) acc) (Array.replicate size 0)

/-! ### Printing a census as the lines of a CSV file -/

/-- The digits of `x` in the mixed radix `radices` (most significant first). -/
def digits (radices : List Nat) (x : Nat) : List Nat :=
  (radices.foldr (fun r (acc : List Nat × Nat) => ((acc.2 % r) :: acc.1, acc.2 / r)) ([], x)).1

/-- `header`, then one line `key,depth,count` for every non-empty cell, in cell order; `key i` is the text
of the feature value `i`. -/
def printCells (header : String) (key : Nat → String) (a : Array Nat) : String := Id.run do
  let mut out : Array String := #[header]
  for i in [0:a.size] do
    let c := a[i]!
    if c != 0 then
      out := out.push s!"{key (i / nd)},{i % nd},{c}"
  return "\n".intercalate out.toList ++ "\n"

/-- The lines of a CSV file without the header, split at the commas. -/
def csvRows (text : String) : List (List String) :=
  ((text.splitOn "\n").drop 1).filterMap fun l => if l.isEmpty then none else some (l.splitOn ",")

/-- The cells of a CSV file whose lines are `key,depth,count`: `cellOf` gives the feature value of the key
columns.  (Lines whose key is not understood go to cell `size`, which does not exist.) -/
def cellsOfCsv (size : Nat) (cellOf : List String → Option Nat) (text : String) : Array Nat :=
  (csvRows text).foldl (fun acc row =>
    let n := row.length
    let i := match cellOf (row.take (n - 2)) with
      | some f => f * nd + (row.getD (n - 2) "").toNat!
      | none => size
    acc.modify i (· + (row.getD (n - 1) "").toNat!)) (Array.replicate size 0)

end Census
end DRBound
