import Insertions.Search
/-
  Insertions.Counts — definitions for `WitnessTheorems.lean` (kept in a file of their own so that the theorems run
  them compiled): two comms without nesting, all placements of three pieces in a cycle on the sticker cube,
  orientation of corners and of edges on each axis, and the 3-cycles the 8-movers reach one move over.
-/
namespace Insertions
namespace ins
open cube

/-- Two comms both put into the skeleton itself (no nesting): the first at spot i, the second at a spot j ≥ i of
the skeleton (at the same spot: right after it), then everything cancelled. -/
def bestFlat (algs : Array (List Nat)) (tbl : Std.HashMap Nat (Array (List Nat))) (z s : List Nat) : Nat := Id.run do
  let zs := stateOf z
  let mut best := 1000
  for i in [0:s.length + 1] do
    for a in algs do
      let t := run zs (s.take i ++ a ++ s.drop i)
      if !(edgesSolved t && cornersMoved t ≤ 3) then continue
      for j in [i:s.length + 1] do
        let pre := s.take i ++ a ++ (s.drop i).take (j - i)
        let need := stateOf (inv pre ++ inv z ++ inv (s.drop j))
        for b in tbl.getD (keyOn ALL need) #[] do
          best := min best (normal (pre ++ b ++ s.drop j)).length
  return best

/-- The three facelets of a corner place, the U/D one first, then clockwise seen from outside. -/
def cornerFacelets (p : Vec) : List Nat :=
  let ud : Vec := [0, p[1]!, 0]
  [placeOf p ud, placeOf p (cw p ud), placeOf p (cw p (cw p ud))]

/-- Every placement of three pieces in a cycle on the places `cubies` (each cyclic order once), with every choice
of how each piece is turned (k ways: the piece's facelets, in the order `fl` gives them, shifted round the
place's), as a sticker state; legal or not. -/
def cyclePlacements (cubies : List Vec) (fl : Vec → List Nat) (k : Nat) : List State := Id.run do
  let n := cubies.length
  let mut out : List State := []
  for i in List.range n do
    for j in List.range n do
      for l in List.range n do
        if !(i < j && i < l && j != l) then continue
        for t in List.range (k * k * k) do
          let tw := [t % k, t / k % k, t / (k * k)]
          -- the piece from place i goes to j, from j to l, from l to i
          let moves := [(i, j), (j, l), (l, i)]
          let mut s := SOLVED
          for ((src, dst), r) in moves.zip tw do
            let fs := fl cubies[src]!; let fd := fl cubies[dst]!
            for q in List.range k do
              s := s.set! fd[(q + r) % k]! fs[q]!
          out := out ++ [s]
  return out

def cornerOriented (s : State) : Bool := CORNERS.all fun p => (cornerAt s p).2 == 0
/-- An edge is oriented on an axis when, of its two stickers, the one whose colour ranks higher sits on the facelet
that ranks higher; ranks for the F/B axis U/D > F/B > R/L, for R/L U/D > R/L > F/B, for U/D F/B > U/D > R/L
(the usual EO rule and its two rotations). -/
def rank (ax : Nat) (n : Vec) : Nat :=
  let a := if n[0]! != 0 then 0 else if n[1]! != 0 then 1 else 2      -- 0 = R/L, 1 = U/D, 2 = F/B
  match ax, a with
  | 2, 1 => 2 | 2, 2 => 1 | 2, _ => 0
  | 0, 1 => 2 | 0, 0 => 1 | 0, _ => 0
  | _, 2 => 2 | _, 1 => 1 | _, _ => 0
def edgeOrientedOn (s : State) (ax : Nat) : Bool := EDGES.all fun p =>
  match facelets p with
  | [f, g] =>
    let hi := if rank ax (cube.ST[f]!).2 > rank ax (cube.ST[g]!).2 then f else g
    let lo := if hi == f then g else f
    rank ax (cube.ST[s[hi]!]!).2 > rank ax (cube.ST[s[lo]!]!).2
  | _ => false
def edgeAllAxes (s : State) : Bool := edgeOrientedOn s 0 && edgeOrientedOn s 1 && edgeOrientedOn s 2

def cornerThree : List State := (cyclePlacements CORNERS cornerFacelets 3).filter fun s => cornerType s == [(3, 0)]
/-- The states the 8-movers make, and those reached from them by one move either side (the alg one spot over). -/
def cornerCovered : Std.HashSet Nat := Id.run do
  let mut out : Std.HashSet Nat := {}
  for a in cornerAlgs do
    out := out.insert (keyOn ALL (stateOf a))
    for m in List.range 18 do out := out.insert (keyOn ALL (stateOf ([m] ++ a ++ inv [m])))
  return out

def isEdge3 (s : State) : Bool := cornersSolved s && edgesMoved s == 3 &&
  (EDGES.filter fun p => (facelets p).all fun i => (cube.ST[s[i]!]!).1 != p).length == 3
def edge3Algs : Array (List Nat) := edgeAlgs.filter fun a => isEdge3 (stateOf a)
def shortest (tbl : Std.HashMap Nat (Array (List Nat))) : List Nat :=
  tbl.toList.map fun e => (e.2.toList.map (·.length)).foldl min 99

end ins
end Insertions
