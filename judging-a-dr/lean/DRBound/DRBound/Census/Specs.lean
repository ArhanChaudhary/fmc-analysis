/-
  DRBound.Census.Specs — the census tables of `research/out/hand/`, one feature code each.

  For every table: `xxCode tb C e` is the feature value (a number below `xxKeys`) of a state with corner
  constants `C` and U/D edges of rank `e`; the census cell is `code * 19 + optimal length`; `xxKey` prints a
  feature value as the key columns of the CSV file, and `xxCell` reads them back.  The digits of a code are
  the CSV's columns in the file's order, so cell order is the file's line order.
-/
import DRBound.Census.Features
import DRBound.Census.Count

set_option compiler.extract_closed false

namespace DRBound
namespace Census
open Exact

/-- `(hmin, hmax)` as one number, as in `hand.rs`. -/
@[inline] def hpair (hn hi : Nat) : Nat := let hmax := max hn hi; hmax * (hmax + 1) / 2 + min hn hi

/-- `hpair` undone: (hmin, hmax). -/
def unpair (hp : Nat) : Nat × Nat :=
  let hmax := ((List.range 14).filter fun m => m * (m + 1) / 2 ≤ hp).foldl max 0
  (hp - hmax * (hmax + 1) / 2, hmax)

def subIndex (tb : Tabs) (name : String) : Option Nat :=
  let i := tb.subNames.toList.idxOf name
  if i < tb.subNames.size then some i else none

def natOf (s : String) : Nat := s.toNat!

/-- The corner constants of row `k` of the exact table. -/
def prepRow (tb : Tabs) (k : Nat) : CornerC := cornerC tb (crep k)

/-! ### h2_lengths.csv : subset, hmin, hmax, L, dLp, parity -/

def h2Radices : List Nat := [48, 105, 14, 7, 2]
def h2Keys : Nat := 48 * 105 * 14 * 7 * 2

@[inline] def h2Code (tb : Tabs) (C : CornerC) (e : Nat) : Nat :=
  let r := reads tb C e
  (((r.sub * 105 + hpair r.hn r.hi) * 14 + r.L) * 7 + min (r.lp - r.L) 6) * 2 + r.par

def h2Key (tb : Tabs) (f : Nat) : String :=
  match digits h2Radices f with
  | [sub, hp, l, dl, par] => let (lo, hi) := unpair hp; s!"{tb.subNames[sub]!},{lo},{hi},{l},{dl},{par}"
  | _ => ""

def h2Cell (tb : Tabs) (row : List String) : Option Nat :=
  match row with
  | [sub, lo, hi, l, dl, par] =>
    (subIndex tb sub).map fun s => (((s * 105 + hpair (natOf lo) (natOf hi)) * 14 + natOf l) * 7 + natOf dl) * 2 + natOf par
  | _ => none

def h2Header : String := "subset,hmin,hmax,L,dLp,parity,depth,count"

def h2Census (tb : Tabs) (T : ByteArray) (nk : Nat) : Array Nat :=
  census T nk (h2Keys * nd) (prepRow tb) (h2Code tb)

end Census
end DRBound
