/-
  DRXs.Fe — research/src/fe.py in Lean: DR with flipped edges (DR-xs), what kind of state a cube is in, read off
  the stickers.

  For a colour axis c and a face axis f (0 = R/L, 1 = U/D, 2 = F/B) a state "looks like a DR with colours c on
  faces f" when
    * every corner has its c-coloured sticker on an f face,
    * the four edges without a c colour (the slice pieces) sit in the slice between the two f faces,
      and the eight other edges sit in the two f layers.
  Then the signature records what is left to fix:
    flips   for each of the eight f-layer edge places, 1 if the edge there has its c colour on the side
    slice   for each of the four slice places, 1 if the slice edge there agrees with the centers
  A true DR is c == f, no flips, all four slice bits 1.

  Centers stay where they are in this model (a slice turn is written as the two outer turns), so "centers off by
  one slice" shows up as c != f.

  Python -> Lean:
    `None` / a pair               `none` / `some (flips, sl)`                (`Option`)
    `any(… for i in pl)`          `pl.any fun i => …`
    `next(x for x in l if …)`     `(l.find? fun x => …).get!`
    the tuple (a, txt, cost, sl)  the same tuple
-/
import DRXs.Cube

namespace DRXs
namespace fe
open cube

def AXIS_OF_FACE (f : Char) : Nat := (AX f).1
/-- axis of the face a place is on -/
def nax (i : Nat) : Nat := argmax_abs cube.ST[i]!.2
/-- colour axis of the sticker at place i -/
def cax (s : State) (i : Nat) : Nat := AXIS_OF_FACE FACE_OF[s[i]!]!

/-- (cubie position, its places in increasing order), for the 26 cubies that have stickers. -/
def CUBIES_TABLE : List (Vec × List Nat) :=
  (product3.map fun p => (p, (List.range 54).filter fun i => cube.ST[i]!.1 == p)).filter fun (_, pl) => pl.length > 0
/-- `CUBIES[p]`: the places of the cubie at position p. -/
def CUBIES (p : Vec) : List Nat := (CUBIES_TABLE.lookup p).getD []

def CORNERS : List Vec := sorted ((CUBIES_TABLE.filter fun (_, pl) => pl.length == 3).map (·.1))
def EDGES : List Vec := sorted ((CUBIES_TABLE.filter fun (_, pl) => pl.length == 2).map (·.1))

/-- `none` if s does not look like a DR with colours c on faces f, else (flips, slice): two lists of 0/1 in the
order of EDGES restricted to the f layers / to the f slice. -/
def look (s : State) (c f : Nat) : Option (List Nat × List Nat) := Id.run do
  for p in CORNERS do
    if !((CUBIES p).any fun i => cax s i == c && nax i == f) then return none
  let h := ([2, 1, 0].find? fun a => a != f && a != c).get!
  let mut flips : List Nat := []
  let mut sl : List Nat := []
  for p in EDGES do
    let pl := CUBIES p
    let has_c := pl.any fun i => cax s i == c
    if (p[f]! == 0) == has_c then return none             -- slice piece outside the slice, or the reverse
    if has_c then
      flips := flips ++ [if pl.any (fun i => cax s i == c && nax i == f) then 0 else 1]
    else
      let i := (pl.find? fun i => nax i == h).get!
      sl := sl ++ [if cax s i == h then 1 else 0]
  return some (flips, sl)

/-- All (c, f, flips, slice) the state looks like. -/
def looks (s : State) : List (Nat × Nat × List Nat × List Nat) := Id.run do
  let mut out := []
  for c in [0, 1, 2] do
    for f in [0, 1, 2] do
      if let some (fl, sl) := look s c f then out := out ++ [(c, f, fl, sl)]
  return out

/-- A real DR: colours c on their own faces, no flips, all slice bits 1. -/
def is_dr (sig : Nat × Nat × List Nat × List Nat) : Bool :=
  let (c, f, fl, sl) := sig
  c == f && !(fl.any (· != 0)) && sl.all (· != 0)

def FACES_OF_AXIS (a : Nat) : String × String :=
  if a == 0 then ("R", "L") else if a == 1 then ("U", "D") else ("F", "B")
def SUF (i : Nat) : String := if i == 1 then "" else if i == 2 then "2" else "'"

/-- The turns allowed on a DR-xs whose corners are oriented on faces f, grouped by axis so that no cancelling is
possible between groups: (axis, text, cost in face turns, slices). -/
def gens (f : Nat) : List (Nat × String × Nat × Nat) := Id.run do
  let mut out := []
  for a in [0, 1, 2] do
    let (p, q) := FACES_OF_AXIS a
    for i in [0, 1, 2, 3] do
      for j in [0, 1, 2, 3] do
        if i == 0 && j == 0 then continue
        if a != f && (i + j) % 2 != 0 then continue         -- a lone quarter turn of a side face: not allowed
        if a != f && i % 2 == 0 && j % 2 != 0 then continue
        let txt := " ".intercalate
          ([if i != 0 then p ++ SUF i else "", if j != 0 then q ++ SUF j else ""].filter (· != ""))
        out := out ++ [(a, txt, (if i > 0 then 1 else 0) + (if j > 0 then 1 else 0),
                        if a != f && i % 2 != 0 then 1 else 0)]
  return out

end fe
end DRXs
