/-
  DRBound.Examples — the certified bounds on positions taken from the documents this work extends.
  Each `#eval` prints the bound of every rung on the normal side and on the inverse side.
-/
import DRBound.Search

namespace DRBound

/-- Read a sequence of DR moves such as "U R2 U' F2". -/
def parseMoves (s : String) : List Move :=
  (s.splitOn " ").filterMap fun t =>
    match t.replace "’" "'" with
    | "U" => some .U | "U2" => some .U2 | "U'" => some .U' | "D" => some .D | "D2" => some .D2 | "D'" => some .D'
    | "R2" => some .R2 | "L2" => some .L2 | "F2" => some .F2 | "B2" => some .B2 | _ => none

def Move.inv : Move → Move
  | .U => .U' | .U' => .U | .D => .D' | .D' => .D | m => m

/-- The state produced by a scramble, and the state produced by the inverse scramble. -/
def scrambled (s : String) : State × State :=
  let w := parseMoves s
  (solved.apply w, solved.apply (w.reverse.map Move.inv))

/-- Bounds (normal, inverse) from the small rungs; the 406-million-class rung is left to the compiled tool. -/
def report (s : String) : List (String × Nat × Nat) :=
  let (g, h) := scrambled s
  [("shortest HTR", rungHTR), ("corner length L", rungC), ("L with E-slice parity", rungCP), ("Adv. DR Bounding features", rungKF)].map
    fun (name, R) => match R.bounds [g, h] with
      | [a, b] => (name, a, b)
      | _ => (name, 0, 0)

-- Rodney Kinney, "Advanced DR Bounding", first random-scramble example (he finds 13 and argues it is optimal)
#eval report "U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2"
-- second example, a 4a4 case (he finds 13)
#eval report "U R2 L2 F2 U' B2 D2 F2 D L2 U B2 R2 U' F2 U"
-- an 18-move optimal DR state quoted on the server (T3897)
#eval report "L2 B2 L2 F2 U' L2 U2 F2 U' R2 U B2 F2 U L2 U F2 U2"

/-! ### Levi's 1qt formula is not always a lower bound

The state below is 1qt 4c4e (subset 4a1 4e).  Its shortest HTR has 6 moves on the normal scramble and 5 on the inverse,
so the formula (HTR normal) + (HTR inverse) − 1 gives 10.  It is solved in 7 moves, using three quarter turns. -/

def leviScramble : List Move := parseMoves "U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2"
def leviFinish : List Move := parseMoves "U B2 L2 F2 D F2 D"

theorem levi_example_htr_lengths :
    rungHTR.bounds [solved.apply leviScramble, solved.apply (leviScramble.reverse.map Move.inv)] = [6, 5] := by
  native_decide

theorem levi_example_solved_in_7 :
    (solved.apply leviScramble).apply leviFinish = solved ∧ leviFinish.length = 7 := by
  native_decide

end DRBound
