/-
The computations of the census (every EO of 5 moves or less), kept in their own file so that they are compiled.
The theorems about them are in Census.lean.
-/
import ImpliedEO.Trick
namespace ImpliedEO

/-- The 24 sticker spots in a fixed order. -/
def spots : List Facelet :=
  Face.all.flatMap fun f => Face.all.filterMap fun g =>
    if h : f.axis ≠ g.axis then some ⟨f, g, h⟩ else none
def idx (x : Facelet) : Nat := spots.idxOf x

/-- A set of edges written as a table over the 24 spots. -/
abbrev Tab := List Bool
def tab (f : Facelet → Bool) : Tab := spots.map f
def Tab.at (t : Tab) (x : Facelet) : Bool := t.getD (idx x) false

/-- What one more move in front does to a case. -/
def cst (a : Axis) (m : Move) (x : Facelet) : Bool :=
  (key a x != key a (mv m x)) != (across a x != across a (mv m x))

def stepT (a : Axis) (m : Move) (t : Tab) : Tab := tab (fun x => cst a m x != t.at (mv m x))

def dedup : List Tab → List Tab
  | [] => []
  | t :: l => let r := dedup l; if r.contains t then r else t :: r

/-- The cases of the sequences of exactly k moves. -/
def layer (a : Axis) : Nat → List Tab
  | 0 => [tab (kcase a [])]
  | k + 1 => dedup ((layer a k).flatMap fun t => Move.all.map fun m => stepT a m t)

/-- Every (length, case) for lengths 0 to 5. -/
def pres (a : Axis) : List (Nat × Tab) :=
  (List.range 6).flatMap fun k => (layer a k).map fun t => (k, t)

def neg (t : Tab) : Tab := t.map not

/-- The lengths (on the first axis, on the second axis) of every case of the first axis whose complement is a
case of the second axis. -/
def sides (pa pb : List (Nat × Tab)) : List (Nat × Nat) :=
  pa.flatMap fun p =>
    let n := neg p.2
    pb.filterMap fun p' => if p'.2 == n then some (p.1, p'.1) else none

/-- Is there an EO of at most 5 on the first axis whose two cases, both complemented, are an EO of at most 5 on
the second axis? -/
def clash (pa pb : List (Nat × Tab)) : Bool :=
  let sd := sides pa pb
  sd.any fun x => sd.any fun y => decide (x.1 + y.1 ≤ 5) && decide (x.2 + y.2 ≤ 5)

/-- Each case with its shortest length, lengths 0 to 5. -/
def mins (a : Axis) : List (Tab × Nat) :=
  (List.range 6).foldl
    (fun acc k => acc ++ ((layer a k).filter fun t => !(acc.any fun p => p.1 == t)).map fun t => (t, k)) []
def lenOn (ms : List (Tab × Nat)) (t : Tab) : Nat :=
  match ms.find? (fun p => p.1 == t) with
  | some p => p.2
  | none => 99
/-- The pairs (inverse case, normal case), axis-free, that are an EO of at most 5 on both axes. -/
def shared (a b : Axis) : List (Tab × Tab) :=
  let mb := mins b
  let side := (mins a).filterMap fun p =>
    let l := lenOn mb p.1
    if l ≤ 5 then some (p.1, p.2, l) else none
  side.flatMap fun p => side.filterMap fun q =>
    if p.2.1 + q.2.1 ≤ 5 && p.2.2 + q.2.2 ≤ 5 then some (p.1, q.1) else none

/-- For the cases of axis `b` of at most 3 moves: (moves on `b`, moves of the same axis-free case on `a`, how many). -/
def probeHist (a b : Axis) : List (Nat × Nat × Nat) :=
  let ma := mins a
  let rows := (mins b).filterMap fun p => if p.2 ≤ 3 then some (p.2, lenOn ma p.1) else none
  [(0, 4), (1, 3), (2, 2), (2, 4), (3, 1), (3, 3), (3, 4), (3, 5)].map fun k =>
    (k.1, k.2, (rows.filter fun r => r == k).length)
def probeTotal (b : Axis) : Nat := ((mins b).filter fun p => p.2 ≤ 3).length

end ImpliedEO
