/-
  Corners3D.Witness — the functions the examples are checked with.  A scramble is a sequence of R, U, F turns as
  text; it is done on the 54-sticker model (`cube.do_`), the corner coordinate is read off the stickers, and
  the tables are looked up at that coordinate.  `Examples.lean` holds the checked examples, one theorem each.

  The kinds of a state are written as seven digits for the places UFR UFL UBR DFR UBL DFL DBR, in that order:
    0 good   1 twisted clockwise   2 twisted counter-clockwise
    3 out, R/L sticker oriented   4 out, U/D sticker oriented   5 out, F/B sticker oriented
-/
import Corners3D.Corners
namespace Corners3D
namespace witness
open cube pieces corners

/-- (x, y, z) of each of those places, to see that the order is the one the names say: x = +1 on R,
y = +1 on U, z = +1 on F. -/
def placeXYZ : List (List Int) := PLACE_ORDER.map fun c => CORNERS[c]!

/-- The seven kinds as text. -/
def kindsText (x : Nat) : String :=
  String.join (PLACE_ORDER.map fun c => toString (kindAt (kinds x) c))

/-- Only R, U, F turns. -/
def onlyRUF (seq : String) : Bool := (parse seq).all TURN_NAMES.contains

/-- `sol`, done after `scr`, reaches HTR. -/
def reaches (scr sol : String) : Bool :=
  onlyRUF scr && onlyRUF sol && inHTR (ofScramble (scr ++ " " ++ sol))

/-- An example: the state `scr` makes shows the kinds `ks`; it is `d` turns from HTR and needs `q` quarter
turns; its types floor (turns to every corner good) is `ft` and its parity floor `fp`; and `sol`, a sequence
of exactly `d` turns, reaches HTR. -/
def check (scr ks : String) (d q ft fp : Nat) (sol : String) : Bool :=
  let x := ofScramble scr
  onlyRUF scr && x < N && kindsText x == ks && fHTR x == d && gHTR x == q && fGood x == ft && fGoodEven x == fp &&
  (parse sol).length == d && reaches scr sol

/-- A looser example: the distances only, and any sequence that reaches HTR (it need not be shortest). -/
def checkLoose (scr : String) (d q : Nat) (sol : String) : Bool :=
  let x := ofScramble scr
  onlyRUF scr && x < N && fHTR x == d && gHTR x == q && reaches scr sol

end witness
end Corners3D
