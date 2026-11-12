/-
  Corrections.DRTable — the DR-finish examples of the corrections, and the one run of DRBound's exact table over
  them (split off so that the table, minutes and about 2 GB, is built once).  The theorems are in
  Corrections.Examples.
-/
import DRBound.CertifiedExact

namespace Corrections

set_option maxHeartbeats 0

/-! ## Move parsing (strict) -/

/-- DR moves of a string, `none` if any token is not one of the ten. -/
def drMoves? (s : String) : Option (List DRBound.Move) :=
  ((s.splitOn " ").filter (· != "")).mapM fun t =>
    match t with
    | "U" => some .U | "U2" => some .U2 | "U'" => some .U' | "D" => some .D | "D2" => some .D2 | "D'" => some .D'
    | "R2" => some .R2 | "L2" => some .L2 | "F2" => some .F2 | "B2" => some .B2 | _ => none
def drMoves (s : String) : List DRBound.Move := (drMoves? s).getD []
def drState (scr : String) : DRBound.State := DRBound.solved.apply (drMoves scr)

/-- (where, scramble, stated optimum).  judging-a-dr B2, B4, B5; htr-routes a, c, d, e, f. -/
def drOptima : List (String × String × Nat) := [
  ("judging-a-dr B2, 0c3 4e", "F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'", 18),
  ("judging-a-dr B2, 2c5 4e", "R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'", 18),
  ("judging-a-dr B2, 2c5 0e", "U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'", 18),
  ("judging-a-dr B2, 0c0 8e", "F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'", 18),
  ("judging-a-dr B4, first", "D F2 U' F2 D B2 D'", 7),
  ("judging-a-dr B4, second", "D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'", 16),
  ("judging-a-dr B5, 4b2 4e", "F2 D2 B2 R2 U' F2 R2 B2 R2 U' F2 L2 D2 R2 D U'", 16),
  ("judging-a-dr B5, 2c3 4e", "R2 U L2 D F2 L2 B2 D2 B2 U' B2 U' R2 F2 R2 U'", 16),
  ("judging-a-dr B5, 4a1 4e", "R2 U2 B2 L2 F2 L2 D2 F2 R2 U' B2 F2 L2 R2 U' R2 D'", 17),
  ("htr-routes a, X", "R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U", 13),
  ("htr-routes a, X R2", "R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U R2", 12),
  ("htr-routes c", "B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U", 16),
  ("htr-routes d", "F2 U' L2 U' F2 R2 F2 L2 U F2 D2 B2", 12),
  ("htr-routes e", "R2 B2 D2 B2 D U2 R2 U L2 F2 U' B2", 12),
  ("htr-routes f, index", "D2 F2 L2 U' B2 U' L2 U2 B2 U' L2 D R2 D2", 14),
  ("htr-routes f, C", "F2 U' B2 R2 B2 U R2", 7)]

/-- (where, scramble, printed solution); each must solve the scramble. -/
def drSolutions : List (String × String × String) := [
  ("htr-routes a, X", "R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U", "U' B2 D2 R2 B2 D' L2 D' R2 F2 R2 D' R2"),
  ("htr-routes a, X R2", "R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U R2", "B2 U' R2 L2 D L2 U L2 U2 R2 U' F2"),
  ("htr-routes d", "F2 U' L2 U' F2 R2 F2 L2 U F2 D2 B2", "B2 D2 F2 U' L2 F2 R2 F2 U L2 U F2"),
  ("htr-routes f, index", "D2 F2 L2 U' B2 U' L2 U2 B2 U' L2 D R2 D2", "D2 R2 D' L2 U B2 U2 L2 U B2 U L2 F2 D2"),
  ("htr-routes f, C", "F2 U' B2 R2 B2 U R2", "R2 U' B2 R2 B2 U F2")]

/-- The table lookup, run once for all examples (rebuilds the 1.34-billion-entry table: minutes, ~2 GB). -/
theorem dr_table_lookup :
    DRBound.Exact.tableValues 18 (drOptima.map fun c => drState c.2.1) = drOptima.map (·.2.2) := by
  native_decide

end Corrections
