/-
  Corners3D.Checks — the checks the theorems run, as compiled functions.  Each returns a `Bool` (or a
  histogram) and is evaluated by `native_decide` in `Theorems.lean`.

  The checks that later feed a proof by induction (`Proofs.lean`) are written with `allBelow n p`, which is
  `(List.range n).all p`, so that "the check returned true" unfolds to "for every x < n, p x".
  Checks take a `Unit` argument (and closed-term extraction is off) so that nothing runs before it is asked for.
-/
import Corners3D.Corners
set_option compiler.extract_closed false
namespace Corners3D
namespace checks
open cube pieces corners

/-- p holds for every number below n. -/
def allBelow (n : Nat) (p : Nat → Bool) : Bool := (List.range n).all p

/-! ### A. The model -/

/-- Every one of the nine turns carries each corner's sticker list onto its destination's, shifted cyclically;
turns the corners by 0 mod 3 in total; leaves DBL (place 0) where it is, untwisted; and the coordinate maps are
bijections onto placements of 1 … 7 and twists that add up to 0 mod 3. -/
def modelOK (_ : Unit) : Bool :=
  (List.range 9).all (fun m => (List.range 8).all (cyclic TURN[m]!)) &&
  (List.range 9).all (fun m => (List.range 8).foldl (fun a c => a + delta m c) 0 % 3 == 0) &&
  (List.range 9).all (fun m => dest m 0 == 0 && delta m 0 == 0) &&
  (List.range NCP).all (fun i => encodeP (decodeP i) == i &&
    (decodeP i).toList.mergeSort (· ≤ ·) == List.range 8 && (decodeP i)[0]! == 0) &&
  (List.range NCO).all (fun i => encodeT (decodeT i) == i && (decodeT i).size == 8 &&
    (decodeT i).foldl (· + ·) 0 % 3 == 0 && (decodeT i)[0]! == 0) &&
  (List.range 9).all (fun m => (CPM[m]!).size == NCP && (COM[m]!).size == NCO) && KINDS.size == N

/-- On the sticker states within 3 R, U, F turns of solved and for each of the nine turns, the coordinate
after the turn (read off the stickers) is `step` of the coordinate before, and the coordinate decodes to the
pieces and twists the stickers show. -/
def coordsOK (_ : Unit) : Bool :=
  (nearRUF 3).all fun s =>
    (List.range 9).all (fun m => coordOf (apply s (turnPerm m)) == step (coordOf s) m) &&
    decodeP (coordOf s / NCO) == (Array.range 8).map (pieceAt s) &&
    decodeT (coordOf s % NCO) == (Array.range 8).map (twistAt s)

def nearCount (_ : Unit) : Nat := (nearRUF 3).length

/-- `CORD` starts with the U/D sticker and lists the three faces of each corner counter-clockwise seen from
outside: for outward normals n₀, n₁, n₂ in that order, (n₀ × n₁) · n₂ > 0, and a right-handed triple of outward
normals runs counter-clockwise.  (At UFR the clockwise order is U, R, F, and (U × R) · F = -1.) -/
def cordCCW (_ : Unit) : Bool :=
  (List.range 8).all fun c =>
    let l := CORD[c]!
    nax l[0]! == 1 && dot (cross cube.ST[l[0]!]!.2 cube.ST[l[1]!]!.2) cube.ST[l[2]!]!.2 > 0

/-- How many different (place, piece, twist) combinations the sticker states within 3 turns show. -/
def coverCount (_ : Unit) : Nat :=
  (((nearRUF 3).flatMap fun s => (List.range 8).map fun c => (c, pieceAt s c, twistAt s c)).eraseDups).length

/-- On those states, for every corner: in its own tetrad it has 3 oriented stickers (exactly when its twist is
0) or none; in the other tetrad exactly 1; and the kind worked out from the coordinates is the kind the
stickers show (0 good; 1 / 2 no sticker oriented, U/D sticker one step clockwise / counter-clockwise;
3 / 4 / 5 only the R/L / U/D / F/B sticker oriented). -/
def tetradOK (_ : Unit) : Bool :=
  (nearRUF 3).all fun s => (List.range 8).all fun c =>
    let h := pieceAt s c
    let n := orientedCount s c
    (if tet c == tet h then (n == 3 || n == 0) && ((n == 3) == (twistAt s c == 0)) else n == 1) &&
    stickerKind s c == kindOf c h (twistAt s c)

/-- The rule in words, checked on the table `KCHG`.  A half turn changes no kind.  A quarter turn about axis a
leaves a corner off its face alone; on its face it makes good ↔ out with the axis-a sticker oriented, turns each
twisted corner into an out corner with one of the other two stickers oriented (cw and ccw going to different
ones), and turns each of those two kinds of out corner into a twisted one (one cw, one ccw). -/
def ruleWords (_ : Unit) : Bool :=
  (List.range 9).all fun m => (List.range 7).all fun c' =>
    let c := c' + 1
    let a := turnAxis m
    let k := fun i => KCHG[m * 48 + c * 6 + i]!
    if !isQuarter m || dest m c == c then
      (List.range 6).all (fun i => k i == i)
    else
      k 0 == 3 + a && k (3 + a) == 0 &&
      k 1 ≥ 3 && k 2 ≥ 3 && k 1 != 3 + a && k 2 != 3 + a && k 1 != k 2 &&
      (List.range 3).all (fun b => b == a || (k (3 + b) == 1 || k (3 + b) == 2)) &&
      k (3 + (a + 1) % 3) != k (3 + (a + 2) % 3)

/-- The change a quarter turn about axis a makes to a corner on its face: the new kinds of kinds 0 … 5.  It is
the same for both directions and for every place of one tetrad (`tetr` = the place is in DBL's tetrad: UFL, UBR,
DFR; otherwise UFR, UBL, DFL, DBR).  The empty list if the places disagree. -/
def ruleRow (a : Nat) (tetr : Bool) : List Nat :=
  let rows := ((List.range 9).filter fun m => m / 3 == a && isQuarter m).flatMap fun m =>
    ((List.range 7).map (· + 1)).filterMap fun c =>
      if dest m c != c && tet c == tetr then some ((List.range 6).map fun k => KCHG[m * 48 + c * 6 + k]!) else none
  match rows with
  | [] => []
  | r :: rest => if rest.all (· == r) then r else []
/-- The six rows: R/L axis, U/D axis, F/B axis, each for a place of the other tetrad and then of DBL's. -/
def ruleTable (_ : Unit) : List (List Nat) := (List.range 3).flatMap fun a => [ruleRow a false, ruleRow a true]

/-- A quarter turn moves exactly the four corners of its face, a half turn too, and nothing else. -/
def faceOK (_ : Unit) : Bool :=
  (List.range 9).all fun m =>
    ((List.range 8).filter fun c => dest m c != c).length == 4 &&
    (List.range 8).all fun c => (dest m c != c) == ((CORNERS[c]!)[turnAxis m]! == 1)

/-- No turn leaves the 3,674,160 coordinates. -/
def closedOK (_ : Unit) : Bool := allBelow N fun x => allBelow 9 fun m => decide (step x m < N)

/-- Each turn is undone by its inverse turn. -/
def invOK (_ : Unit) : Bool := allBelow N fun x => allBelow 9 fun m => step (step x m) (invTurn m) == x

/-- For every state and turn, the kinds after the turn are `kindStep` of the kinds before. -/
def ruleOK (_ : Unit) : Bool := allBelow N fun x => allBelow 9 fun m => kinds (step x m) == kindStep m (kinds x)

/-! ### Floors and exact tables, in the form the induction proofs use -/

/-- f is 0 on the goal and no turn lowers it by more than 1. -/
def floorOK (f : Nat → Nat) (goal : Nat → Bool) (_ : Unit) : Bool :=
  allBelow N fun x => (!goal x || f x == 0) && allBelow 9 fun m => decide (f x ≤ f (step x m) + 1)

/-- f is 0 exactly on the goal, no turn lowers it by more than 1, and off the goal some turn lowers it by 1. -/
def exactOK (f : Nat → Nat) (goal : Nat → Bool) (_ : Unit) : Bool :=
  allBelow N fun x => (goal x == (f x == 0)) && (allBelow 9 fun m => decide (f x ≤ f (step x m) + 1)) &&
    (f x == 0 || (List.range 9).any fun m => f (step x m) + 1 == f x)

/-- g is 0 on the goal, a half turn does not lower it and a quarter turn lowers it by at most c. -/
def wfloorOK (g : Nat → Nat) (c : Nat) (goal : Nat → Bool) (_ : Unit) : Bool :=
  allBelow N fun x => (!goal x || g x == 0) &&
    allBelow 9 fun m => decide (g x ≤ g (step x m) + (if isQuarter m then c else 0))

/-! ### Histograms -/

/-- How many x < n have f x = v, for v = 0, 1, … (trailing zeros dropped). -/
def histOf (f : Nat → Nat) (n : Nat) : List Nat := Id.run do
  let mut h := Array.replicate 64 0
  for x in [0:n] do
    h := h.modify (f x) (· + 1)
  return (h.toList.reverse.dropWhile (· == 0)).reverse

/-- Histogram of f x - g x over all states (the floor theorems say g ≤ f). -/
def gapHist (f g : Nat → Nat) (_ : Unit) : List Nat := histOf (fun x => f x - g x) N

/-- g x ≤ f x for every state. -/
def below (g f : Nat → Nat) (_ : Unit) : Bool := Id.run do
  for x in [0:N] do
    if g x > f x then return false
  return true

/-- Four times the fewest quarter turns (for comparing with the weight). -/
def gHTR4 (x : Nat) : Nat := 4 * gHTR x

/-- Every floor is at most the truth, state by state (so the gap histograms above count real gaps). -/
def floorsBelow (_ : Unit) : Bool :=
  below fGood fHTR () && below fGoodEven fHTR () && below fPerm fHTR () &&
  below gGood gHTR () && below gGoodEven gHTR () && below gPerm gHTR () && below weight gHTR4 ()

/-! ### Fake HTR -/

/-- Of the 144 all-good states 24 are HTR; each of the other 120 is exactly 9 turns from HTR; 72 of them need
3 quarter turns and 48 need 4. -/
def fakeOK (_ : Unit) : Bool :=
  let fake := GOOD.filter fun x => !inHTR x
  GOOD.length == 144 && fake.length == 120 && fake.all (fun x => fHTR x == 9) &&
  (fake.filter fun x => gHTR x == 3).length == 72 && (fake.filter fun x => gHTR x == 4).length == 48 &&
  (fake.filter fun x => odd x).length == 72 && fake.all (fun x => odd x == (gHTR x == 3))

/-! ### The colour read -/

/-- HTR ⇔ every corner good ∧ the D-coloured corners in one of the six pictures ∧ even placement. -/
def htrIffOK (_ : Unit) : Bool :=
  allBelow N fun x => inHTR x == (allGood x && SIX.contains (colourY x) && !odd x)

/-- States with the same kinds, the same D-colour picture and the same parity have the same number of turns
and of quarter turns to HTR.  One table cell per (kinds, picture, parity); a cell is written once and every
later state with that key must agree. -/
def threeReadsOK (_ : Unit) : Bool := Id.run do
  let size := 279936 * 128 * 2
  let mut tab := ByteArray.emptyWithCapacity size
  for _ in [0:size] do tab := tab.push 0
  for x in [0:N] do
    let key := (kinds x * 128 + colourY x) * 2 + (if odd x then 1 else 0)
    let v := (fHTR x * 16 + gHTR x + 1).toUInt8
    let old := tab.get! key
    if old == 0 then tab := tab.set! key v
    else if old != v then return false
  return true

/-- No two states show the same kinds, the same D-colour picture and the same B-colour picture. -/
def twoColoursOK (_ : Unit) : Bool := Id.run do
  let keys := ((Array.range N).map fun x => (kinds x * 128 + colourY x) * 128 + colourZ x).qsort (· < ·)
  for i in [1:N] do
    if keys[i]! == keys[i - 1]! then return false
  return keys.size == N

/-- How many states show each kinds pattern (a table over the 6^7 kinds numbers), counting only the odd
placements when `oddOnly`. -/
def patternCounts (oddOnly : Bool) : Array Nat := Id.run do
  let mut cnt := Array.replicate 279936 0
  for x in [0:N] do
    if !oddOnly || odd x then cnt := cnt.modify (kinds x) (· + 1)
  return cnt

/-- (how many different kinds patterns occur, whether each is shown by exactly 144 states) -/
def classSizes (_ : Unit) : Nat × Bool :=
  let cnt := patternCounts false
  ((cnt.toList.filter (· != 0)).length, cnt.all fun c => c == 0 || c == 144)

/-- Every kinds pattern is shown by 72 states with an even placement and 72 with an odd one. -/
def classParity (_ : Unit) : Bool :=
  (patternCounts true).all fun c => c == 0 || c == 72

/-! ### DR inside 3D -/

/-- `orientedState a P` has placement P and every corner good or out with the axis-a sticker oriented; for
U/D these are the states with every twist 0. -/
def orientedOK (_ : Unit) : Bool :=
  (List.range 3).all fun a => (List.range NCP).all fun P =>
    let x := orientedState a P
    x / NCO == P && x < N && (List.range 7).all (fun c => let k := kindAt (kinds x) (c + 1); k == 0 || k == 3 + a) &&
    (a != 1 || x == P * NCO)

/-- The DR-only tables are exact, for each axis (`search.distRule`, `search.qtRule` over the placements). -/
def drTablesOK (_ : Unit) : Bool :=
  (List.range 3).all fun a => search.distRule NCP inHTRP (DRM a) pstep dDR[a]! &&
    search.qtRule NCP inHTRP (DRM a) w pstep qDR[a]!

/-- On the states oriented on axis a, the fewest quarter turns with the DR turns of that axis only is the
fewest with all nine turns. -/
def drQtSame (_ : Unit) : Bool :=
  (List.range 3).all fun a => (List.range NCP).all fun P => (qDR[a]!).get! P == qHTR.get! (orientedState a P)

/-- Turns saved by leaving the DR turns, on the states oriented on axis a: histogram of
(DR-only turns) - (turns with all nine). -/
def drSaveHist (a : Nat) (_ : Unit) : List Nat :=
  histOf (fun P => ((dDR[a]!).get! P).toNat - fHTR (orientedState a P)) NCP
def drSaveBelow (_ : Unit) : Bool :=
  (List.range 3).all fun a => (List.range NCP).all fun P => fHTR (orientedState a P) ≤ ((dDR[a]!).get! P).toNat

/-- For every placement, the quarter-turn count with DR turns is the same on all three axes and equals the
placement-only count with all nine turns. -/
def permQtSame (_ : Unit) : Bool :=
  (List.range NCP).all fun P => (List.range 3).all fun a => (qDR[a]!).get! P == qPerm.get! P

end checks
end Corners3D
