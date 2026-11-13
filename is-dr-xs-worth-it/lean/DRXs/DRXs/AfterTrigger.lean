/-
  DRXs.AfterTrigger — the rest of research/src/festeps.py: `after_quarter`, the saving when the move just made was
  a quarter turn of a side face (a trigger's last move), which a slice about the same axis merges with
  (R then R' L is just L).  Also the per-layout readings of the DR-1s table (one face axis = the 70 layouts) and
  the "last trigger move the other way" count of Appendix A / Simon's table (research/src/witness.py, `simon`).

  Python -> Lean:
    `after_quarter(g, dist)` returns a dict {side axis: extra turns}; here the list of its two values, in axis order.
    `parts = {face letter: quarter turns}` of the group's text      `quarters txt face`
    `dist.get(k, 99)`                                                `dist.getD k INF`
-/
import DRXs.Festeps

namespace DRXs
namespace aftertrigger
open cube fecosets festeps

/-- Quarter turns of `face` in a group's text ("R2 L'" -> R: 2, L: 3), 0 if the face is not turned. -/
def quarters (txt : String) (face : String) : Nat :=
  match (parse txt).find? (fun t => (t.take 1).toString == face) with
  | none => 0
  | some t => if t.endsWith "2" then 2 else if t.endsWith "'" then 3 else 1

/-- festeps.after_quarter: for each of the two side axes `ax` of kind g (axis order), the fewest extra turns to the
target when the move just made was a quarter turn about `ax`.  Either the next group is not about `ax` (that is
dist[(g, ax)]), or it is a group about `ax` merged into the quarter turn: the quarter turn q0 of one face of `ax`
plus that face's i quarters from the group, plus the other face's turn if the group has one. -/
def after_quarter (g : Sig) (dist : Dist) : List Nat := Id.run do
  let mut out : List Nat := []
  for ax in [0, 1, 2] do
    if ax == g.f then continue
    let mut b := dist.getD (g, ax) INF
    for (a, txt, _cost, _sl, h) in nbr.getD g [] do
      if a != ax then continue
      let (p, q) := fe.FACES_OF_AXIS ax
      for (face, other) in [(p, q), (q, p)] do
        for q0 in [1, 3] do
          let i := quarters txt face
          let hasOther := quarters txt other != 0
          if i == 0 && !hasOther then continue
          if (q0 + i) % 4 == 0 && !hasOther then continue          -- that just undoes the last move
          -- change in turn count: the merged face turn (0 if it cancels) + the other face's turn - the group's cost
          -- already paid by the quarter turn (1); never below 0 here
          let new := (if (q0 + i) % 4 != 0 then 1 else 0) + (if hasOther then 1 else 0) - 1
          let nd := new + dist.getD (h, ax) INF
          if nd < b then b := nd
    out := out ++ [b]
  return out

/-- min / max of a non-empty list (0 for the empty list). -/
def lmin (l : List Nat) : Nat := l.foldl min (l.headD 0)
def lmax (l : List Nat) : Nat := l.foldl max (l.headD 0)

/-- Right after a side quarter turn on the better / the worse of the two side axes. -/
def better (g : Sig) (dist : Dist) : Nat := lmin (after_quarter g dist)
def worse (g : Sig) (dist : Dist) : Nat := lmax (after_quarter g dist)

/-! Per layout: the DR-1s kinds with the corners on one pair of faces. -/

/-- The DR-1s kinds with corners on face axis f (2 = F/B, where the slice that fixes is R L). -/
def layouts (f : Nat) : List Sig := (kinds_with_slices 1).filter (·.f == f)

/-- The kind reached from g by the group with this text (the first such group). -/
def after (g : Sig) (txt : String) : Option Sig :=
  ((nbr.getD g []).find? (fun e => e.2.1 == txt)).map (·.2.2.2.2)

/-- Turns to a real DR after the group `txt` (INF if there is no such group). -/
def turns_after (g : Sig) (txt : String) : Nat := match after g txt with
  | none => INF
  | some h => turns_to_dr h

/-- The 8 places of the layer edges of face axis f, in the order of the flip bits. -/
def layer_places (f : Nat) : List Vec := fe.EDGES.filter fun p => p[f]! != 0

/-- How many flipped edges of a kind with corners on F/B sit inside the slice that fixes (R L: x = 0). -/
def inside (g : Sig) : Nat :=
  ((layer_places g.f).zip g.flips).countP fun (p, b) => b == 1 && p[0]! == 0

/-- Sum of a list. -/
def total (l : List Nat) : Nat := l.foldl (· + ·) 0

end aftertrigger
end DRXs
