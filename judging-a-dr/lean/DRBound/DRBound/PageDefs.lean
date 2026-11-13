/-
  DRBound.PageDefs — the small computations used by DRBound.PageChecks (in their own module so that
  `native_decide` runs them compiled).  Parsing (`drMoves?`, `st`) is in DRBound.PageTable.
-/
import DRBound.PageTable
import DRBound.Examples

namespace DRBound.Page

/-- The inverse state: the inverse scramble applied to solved. -/
def stInv (scr : String) : State := solved.apply ((drMoves scr).reverse.map Move.inv)

/-- min over premove sequences `a` with `|a| ≤ k` (`s` = solved after the premoves so far, `len` their number) of
`|a|` + the HTR rung's value of `a ++ w`. -/
def premoveMin (T : ByteArray) (w : List Move) : Nat → State → Nat → Nat
  | 0, s, len => len + (T.get! (rungHTR.index (s.apply w))).toNat
  | k + 1, s, len =>
    Move.all.foldl (fun acc m => min acc (premoveMin T w k (s.move m) (len + 1)))
      (len + (T.get! (rungHTR.index (s.apply w))).toNat)

/-- min over premove sequences `a` with `|a| ≤ 5`, on the scramble and on its inverse, of `|a|` + the HTR rung's
value of `a ++ scramble`: the shortest NISS DR → HTR of the state when that is 11 or less, and 12 or more otherwise
(see DRBound.PageChecks). -/
def nissHTR5 (scr : String) : Nat :=
  let T := rungHTR.table
  let w := drMoves scr
  min (premoveMin T w 5 solved 0) (premoveMin T ((w.reverse.map Move.inv)) 5 solved 0)

end DRBound.Page
