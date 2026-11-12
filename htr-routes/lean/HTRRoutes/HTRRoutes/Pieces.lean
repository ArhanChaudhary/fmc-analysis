/-
  HTRRoutes.Pieces — the pieces of a cube in DR on U/D, read off the sticker model of `Cube.lean`, and the ten DR
  moves acting on them.  Nothing here is typed by hand: every table is computed from the 54-sticker permutations.

  Places (cubie positions of `Cube.lean`, in sorted order, as in the research's `sticker.py`):
    CPOS  the 8 corner places (|x| = |y| = |z| = 1)
    EPOS  the 8 U/D-layer edge places (one coordinate 0, y ≠ 0)
    SPOS  the 4 E-slice edge places (y = 0)
  An *arrangement* of a group of pieces is an array a with a[i] = the home place (index in the same list) of the
  piece sitting at place i.  A DR state is the triple (corners, U/D edges, E-slice edges).  (DR moves never change
  orientation relative to U/D: `dr_keeps_axes` in `Model.lean`.  So the triple is the whole state.)

  Moves: DR = U U2 U' D D2 D' R2 L2 F2 B2, numbered 0 … 9 (the research's order).  Half turns HALF = 1 4 6 7 8 9
  (U2 D2 R2 L2 F2 B2), quarter turns QT = 0 2 3 5 (U U' D D').
  `amul a b` = the arrangement after doing a then b (from solved): (amul a b)[p] = a[b[p]].  The arrangement of a
  move m is `CMOV m` (what m does to the solved cube); doing m on a state with arrangement a gives `amul a (CMOV m)`.

  Words of the research (`sticker.py`, `class.rs`):
    tetrad        the two orbits of corner places under half turns: sign of x·y·z
    bad corner    a corner sitting in a place of the other tetrad
    M / S         a U/D-layer edge place with x = 0 (UF UB DF DB) is an M place, one with z = 0 (UL UR DL DR) an
                  S place; an M piece is one whose home is an M place
    bad edges     the M pieces in S places plus the S pieces in M places (always even: twice the first number)
-/
import HTRRoutes.Cube

namespace HTRRoutes
namespace pieces
open cube

/-- The sticker places of cubie position p, in increasing order. -/
def placesOf (p : Vec) : List Nat := (List.range 54).filter fun i => cube.ST[i]!.1 == p

def CPOS : Array Vec := (sorted (product3.filter fun p => p.all (·.natAbs == 1))).toArray
def EPOS : Array Vec :=
  (sorted (product3.filter fun p => (p.map (·.natAbs)).mergeSort (· ≤ ·) == [0, 1, 1] && p[1]! != 0)).toArray
def SPOS : Array Vec := (sorted (product3.filter fun p => p[1]! == 0 && p[0]!.natAbs == 1 && p[2]!.natAbs == 1)).toArray

/-- The first sticker place of cubie position p (`FIRST` of sticker.py). -/
def FIRST (p : Vec) : Nat := (placesOf p).headD 54
/-- The home cubie position of the piece now at position p, in sticker state s. -/
def homeAt (s : State) (p : Vec) : Vec := cube.ST[s[FIRST p]!]!.1

/-- The arrangement of a group of places (`CPOS`, `EPOS` or `SPOS`) in sticker state s. -/
def arr (P : Array Vec) (s : State) : Array Nat := P.map fun p => P.toList.idxOf (homeAt s p)
def corners (s : State) : Array Nat := arr CPOS s
def edges (s : State) : Array Nat := arr EPOS s
def slice (s : State) : Array Nat := arr SPOS s

/-- The ten DR moves, in the research's order. -/
def DRNAMES : List String := ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
def HALF : List Nat := [1, 4, 6, 7, 8, 9]
def QT : List Nat := [0, 2, 3, 5]
def ALLM : List Nat := List.range 10
/-- The sticker permutation of DR move m. -/
def DRMV : Array State := (DRNAMES.map MOVES).toArray

/-- What move m does to the solved cube, as arrangements. -/
def CMOV : Array (Array Nat) := DRMV.map fun m => corners (apply SOLVED m)
def EMOV : Array (Array Nat) := DRMV.map fun m => edges (apply SOLVED m)
def SMOV : Array (Array Nat) := DRMV.map fun m => slice (apply SOLVED m)

/-- a then b. -/
def amul (a b : Array Nat) : Array Nat := b.map fun p => a[p]!
/-- The inverse arrangement. -/
def ainv (a : Array Nat) : Array Nat := Id.run do
  let mut r := Array.replicate a.size 0
  for i in [0:a.size] do r := r.set! a[i]! i
  return r
def ident (n : Nat) : Array Nat := Array.range n

/-- An array of n entries holding each of 0 … n-1 once. -/
def isPerm (n : Nat) (a : Array Nat) : Bool := a.size == n && (List.range n).all fun j => a.contains j

/-! ### Tetrads, M and S -/

/-- Tetrad of corner place i: true when x·y·z > 0 (UFR UBL DFL DBR). -/
def TET : Array Bool := CPOS.map fun p => p[0]! * p[1]! * p[2]! > 0
/-- U/D edge place k is an M place (x = 0) / an S place (z = 0). -/
def ISM : Array Bool := EPOS.map fun p => p[0]! == 0
def ISS : Array Bool := EPOS.map fun p => p[2]! == 0

/-- Corner places, as bit masks: the 6 faces (U D R L F B), each a set of 4 places. -/
def FACEMASK : List Nat := FACES.map fun f =>
  let (a, sg) := AX f
  (List.range 8).foldl (fun acc i => if CPOS[i]![a]! == sg then acc + 2 ^ i else acc) 0

/-- Positions of the bad corners of arrangement a, as an 8-bit mask. -/
def badMask (a : Array Nat) : Nat :=
  (List.range 8).foldl (fun acc i => if TET[i]! != TET[a[i]!]! then acc + 2 ^ i else acc) 0
def nbad (a : Array Nat) : Nat := (List.range 8).countP fun i => TET[i]! != TET[a[i]!]!

/-- Places holding M pieces, as an 8-bit mask ("edge pattern"). -/
def mMask (e : Array Nat) : Nat := (List.range 8).foldl (fun acc k => if ISM[e[k]!]! then acc + 2 ^ k else acc) 0
/-- Bad edges of an edge pattern: 2 · (M pieces in S places). -/
def ebad (mask : Nat) : Nat := 2 * (List.range 8).countP fun k => ISS[k]! && (mask >>> k) % 2 == 1

/-- Move m on a mask of places: bit p of the result is bit (CMOV m)[p] (or EMOV) of the mask. -/
def maskMv (mv : Array Nat) (mask : Nat) : Nat :=
  (List.range 8).foldl (fun acc p => if (mask >>> mv[p]!) % 2 == 1 then acc + 2 ^ p else acc) 0

/-! ### Ranks of permutations (Lehmer code) -/

def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

/-- Rank of a permutation of 0 … n-1 (n = a.size): 0 … n! - 1, the identity has rank 0. -/
def rank (a : Array Nat) : Nat := Id.run do
  let n := a.size
  let mut r := 0
  for i in [0:n] do
    let mut c := 0
    for j in [i+1:n] do
      if a[j]! < a[i]! then c := c + 1
    r := r * (n - i) + c
  return r

/-- The permutation of 0 … n-1 with rank r. -/
def unrank (n r : Nat) : Array Nat := Id.run do
  -- digits c_0 … c_{n-1}, c_i < n - i
  let mut cs := Array.replicate n 0
  let mut r := r
  for k in [0:n] do
    let i := n - 1 - k
    cs := cs.set! i (r % (n - i))
    r := r / (n - i)
  let mut avail := List.range n
  let mut out := #[]
  for i in [0:n] do
    let v := avail[cs[i]!]!
    out := out.push v
    avail := avail.erase v
  return out

/-! ### Small helpers -/

/-- (value, how many times it occurs), by value. -/
def hist (l : List Nat) : List (Nat × Nat) :=
  let vs := (l.eraseDups).mergeSort (· ≤ ·)
  vs.map fun v => (v, l.count v)

/-- The sticker states reached from solved with at most `n` DR moves (with repeats). -/
def near (n : Nat) : List State := Id.run do
  let mut layer : List State := [SOLVED]
  let mut out : List State := [SOLVED]
  for _ in [0:n] do
    layer := layer.flatMap fun s => DRMV.toList.map fun m => apply s m
    out := out ++ layer
  return out

/-- Axis (0 R/L, 1 U/D, 2 F/B) of the face sticker place i is on. -/
def nax (i : Nat) : Nat := argmax_abs cube.ST[i]!.2

end pieces
end HTRRoutes
