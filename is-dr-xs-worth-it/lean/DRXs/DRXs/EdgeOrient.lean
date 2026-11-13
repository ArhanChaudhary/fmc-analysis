/-
  DRXs.EdgeOrient — edge orientation for each of the three axes, read off the stickers, and the pieces needed to
  check the slice-EO rule of research/src/seo_skip.py and to redo research/src/seo_dist.py.

  Edge orientation for axis e.  Rank the three axes: a reference axis o1 first, e second, the third axis last.
  An edge's *primary place* is its sticker place on the face of the lowest-ranked axis, and the piece's *primary
  colour* is its colour of the lowest-ranked axis.  The edge is good for e when the primary place shows the
  primary colour.  With e = F/B and o1 = U/D this is the usual EO, `coords.flips` of the Python: the U/D sticker
  of a U/D-layer place (else the F/B one), against the U/D colour of the piece (else its F/B colour).
  Theorem `eo_reference_free` says the choice of o1 between the other two axes makes no difference.

  Also here: the inverse of a state, the inverse of a move sequence, and edge-place names ("BL").
-/
import DRXs.SeoSkip
import DRXs.Fecosets

namespace DRXs
namespace edges
open cube

/-- Rank of axis a when orienting for axis e with reference o1. -/
def rank (e o1 a : Nat) : Nat := if a == o1 then 0 else if a == e then 1 else 2

/-- Is the edge at position p good for axis e (reference axis o1)?  `col i` is the colour axis of the sticker at
place i. -/
def goodWith (e o1 : Nat) (col : Nat → Nat) (p : Vec) : Bool :=
  let pl := fe.CUBIES p
  let a := pl[0]!; let b := pl[1]!
  let prim := if rank e o1 (fe.nax a) ≤ rank e o1 (fe.nax b) then a else b
  let pc := if rank e o1 (col a) ≤ rank e o1 (col b) then col a else col b
  col prim == pc

/-- The default reference: U/D for F/B and R/L, F/B for U/D. -/
def ref (e : Nat) : Nat := if e == 1 then 2 else 1
/-- The other reference (the remaining axis). -/
def ref' (e : Nat) : Nat := 3 - e - ref e

def good (e : Nat) (s : State) (p : Vec) : Bool := goodWith e (ref e) (fe.cax s) p

/-- The edge positions (`fe.EDGES` order) and the kind of each: 'E' (y = 0), 'M' (x = 0), 'S' (z = 0), as
seo_skip.KIND. -/
def kindOf (p : Vec) : Char := if p[1]! == 0 then 'E' else if p[0]! == 0 then 'M' else 'S'

/-- seo_skip's axis names. -/
def axisName (e : Nat) : String := if e == 1 then "UD" else if e == 0 then "RL" else "FB"

/-- The solved cube with the edge at position u replaced by piece t, turned (o = 1) or not (o = 0). -/
def place1 (u t : Vec) (o : Nat) : State :=
  let pu := fe.CUBIES u; let pt := fe.CUBIES t
  let (x, y) := if o == 0 then (pt[0]!, pt[1]!) else (pt[1]!, pt[0]!)
  (SOLVED.set! pu[0]! x).set! pu[1]! y

/-- The solved cube with piece t at u (turned o) and piece u at t (turned o'): a transposition of two edges, or
one edge flipped in place when u = t (then o' is ignored). -/
def place2 (u t : Vec) (o o' : Nat) : State :=
  if u == t then place1 u u o else
  let pu := fe.CUBIES u; let pt := fe.CUBIES t
  let (x, y) := if o == 0 then (pt[0]!, pt[1]!) else (pt[1]!, pt[0]!)
  let (x', y') := if o' == 0 then (pu[0]!, pu[1]!) else (pu[1]!, pu[0]!)
  (((SOLVED.set! pu[0]! x).set! pu[1]! y).set! pt[0]! x').set! pt[1]! y'

/-- The inverse of a state (a permutation of the 54 places): t[s[i]] = i. -/
def inverse (s : State) : State := Id.run do
  let mut t := Array.replicate 54 0
  for i in [0:54] do t := t.set! s[i]! i
  return t

/-- The position of the cubie whose sticker has home place h. -/
def homePos (h : Nat) : Vec := cube.ST[h]!.1

/-- Position of the edge cubie at place i (the cubie position of place i). -/
def posOf (i : Nat) : Vec := cube.ST[i]!.1

/-- Is move `m` a quarter turn of a face of axis e, and is position p in that face's layer? -/
def flipsEdge (m : String) (e : Nat) (p : Vec) : Bool :=
  let f := m.front
  let (a, sg) := AX f
  let quarter := m.length == 1 || m.endsWith "'"
  quarter && a == e && p[a]! == sg

/-- The inverse of a move sequence: reversed, each turn inverted. -/
def invMove (m : String) : String :=
  if m.endsWith "2" then m else if m.endsWith "'" then (m.take 1).toString else m ++ "'"
def invSeq (seq : String) : String := " ".intercalate ((parse seq).reverse.map invMove)

/-- Edge position named by its faces ("BL", "UF"): the coordinate of each face letter. -/
def posOfName (n : String) : Vec := Id.run do
  let mut v : Vec := [0, 0, 0]
  for ch in n.toList do
    let (a, sg) := AX ch
    v := v.set a sg
  return v

/-- Face-letter name of an edge position, in the order U D R L F B ... as written on the page we compare sets of
positions, so the order of letters does not matter. -/
def sameEdges (names : List String) (ps : List Vec) : Bool :=
  names.length == ps.length && names.all (fun n => ps.contains (posOfName n)) &&
  ps.all (fun p => names.any (fun n => posOfName n == p))

/-! ## seo_dist: turns to a slice EO for the E slice -/

/-- Is the sticker with home place h on an E-slice piece (an edge with y = 0)? -/
def isE (h : Nat) : Bool := let p := homePos h; p[1]! == 0 && p[0]! != 0 && p[2]! != 0

/-- What the slice-EO question sees of a state: at each place, 0 if the sticker there is not on an E-slice piece,
else 1 + its colour axis (1 = R/L colour, 3 = F/B colour). -/
def absE (s : State) : Array Nat :=
  (Array.range 54).map fun i => let h := s[i]!; if isE h then 1 + fe.AXIS_OF_FACE FACE_OF[h]! else 0

/-- The E-slice pieces' orientation for axis e, read off an abstract state: (number good, number of E pieces). -/
def eStats (e : Nat) (x : Array Nat) : Nat × Nat := Id.run do
  let mut good := 0
  let mut n := 0
  for p in fe.EDGES do
    let pl := fe.CUBIES p
    if x[pl[0]!]! != 0 then
      n := n + 1
      if goodWith e (ref e) (fun i => x[i]! - 1) p then good := good + 1
  return (good, n)

/-- A slice EO for the E slice on one of the axes `axes`: all four oriented, or (if `mis`) all four misoriented. -/
def goal (axes : List Nat) (mis : Bool) (x : Array Nat) : Bool :=
  axes.any fun e => let (g, n) := eStats e x; n == 4 && (g == 4 || (mis && g == 0))

/-- All abstract states reachable from the solved cube with the 18 face turns. -/
def reachE : Array (Array Nat) := Id.run do
  let start := absE SOLVED
  let mut seen : Std.HashMap (Array Nat) Nat := {}
  seen := seen.insert start 0
  let mut all : Array (Array Nat) := #[start]
  let mut i := 0
  while i < all.size do
    let x := all[i]!
    for m in NAMES do
      let y := apply x (MOVES m)
      if !seen.contains y then
        seen := seen.insert y all.size
        all := all.push y
    i := i + 1
  return all

/-- Fewest face turns from each reachable abstract state to the goal: breadth-first from the goal states (the 18
turns are closed under inverses, so searching from the goal with the turns themselves gives the distance to it). -/
def distTo (goal : Array Nat → Bool) : List Nat := Id.run do
  let states := reachE
  let mut d : Std.HashMap (Array Nat) Nat := {}
  let mut frontier : Array (Array Nat) := #[]
  for x in states do
    if goal x then
      d := d.insert x 0; frontier := frontier.push x
  let mut k := 0
  while !frontier.isEmpty do
    k := k + 1
    let mut next : Array (Array Nat) := #[]
    for x in frontier do
      for m in NAMES do
        let y := apply x (MOVES m)
        if !d.contains y then
          d := d.insert y k; next := next.push y
    frontier := next
  return states.toList.map fun x => d.getD x 1000

end edges
end DRXs
