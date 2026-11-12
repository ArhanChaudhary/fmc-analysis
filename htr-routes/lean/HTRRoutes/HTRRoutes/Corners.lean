/-
  HTRRoutes.Corners — the 40,320 corner arrangements of a DR state, and everything the study reads off them:
  the HTR corners, the quarter-turn count, the 14 corner subsets, the 420 corner cosets, FakeMMAP's section bounds
  α_i, fake HTRs, and the bare-quarter-turn reductions of claim C10.

  A corner arrangement is identified by its rank r = `pieces.rank a` (0 … 40319; the solved corners have rank 0).
  `CMT[m][r]` = rank of (arrangement r, then move m).  Definitions, as in the research (`class.rs`, `sticker.py`,
  `htrtools alpha`):

    HC        the corner arrangements reached from solved by half turns (the corners of the HTR group)
    Z         the arrangements reached by half turns from solved or from U D' ("HTR corners up to U D'")
    qt r      the fewest quarter turns in a DR move sequence taking r into Z; half turns are free.  Checked by
              `qtRule` (below), not trusted from the computation.
    subset    from (bad corners n, qt, shape): n = 8 counts as 0 and n = 6 as 2; with 4 bad corners the shape is
              'a' when half turns can bring the four bad places onto one face, else 'b'.  The 14 names
              0c0 4a1 4a2 4b2 0c3 2c3 4a3 4b3 0c4 2c4 4a4 4b4 2c5 4b5 (index 0 … 13, the research's order).
              The letter of 4a3/4b3 and 4a4/4b4 is the side's own (a state and its inverse can differ).
    coset     H·r = {h then r : h ∈ HC}, the HTR corner coset ("the state up to renaming pieces by an HTR
              element"); its representative is its smallest rank.
-/
import HTRRoutes.Pieces
import HTRRoutes.Search

set_option compiler.extract_closed false

namespace HTRRoutes
namespace corners
open pieces

def NC : Nat := 40320

/-- The arrangement of each rank, computed once. -/
def ARR : Array (Array Nat) := (Array.range NC).map (unrank 8)
/-- `CMT[m][r]`: rank of (r then move m). -/
def CMT : Array (Array Nat) := (Array.range 10).map fun m => ARR.map fun a => rank (amul a CMOV[m]!)
def step (x m : Nat) : Nat := CMT[m]![x]!
/-- Rank of the inverse arrangement. -/
def CINV : Array Nat := ARR.map fun a => rank (ainv a)

/-! ### HTR corners, and HTR corners up to U D' -/

def UD : Nat := rank (amul CMOV[0]! CMOV[5]!)     -- U then D'
def HCD : ByteArray := search.bfs NC [0] HALF step
def ZD : ByteArray := search.bfs NC [0, UD] HALF step
/-- The 96 HTR corner arrangements, by rank. -/
def HC : Array Nat := (Array.range NC).filter fun r => search.reached HCD r
def inHC (r : Nat) : Bool := search.reached HCD r
def inZ (r : Nat) : Bool := search.reached ZD r

/-! ### The quarter-turn count -/

/-- Layered 0-1 search: level d is spread over half turns (cost 0), then quarter turns lead to level d + 1. -/
def qtCompute : Array Nat := Id.run do
  let mut q := Array.replicate NC 99
  let mut cur : Array Nat := (Array.range NC).filter inZ
  for r in cur do q := q.set! r 0
  for d in [0:12] do
    -- close level d under half turns
    let mut i := 0
    while i < cur.size do
      let x := cur[i]!
      i := i + 1
      for m in HALF do
        let y := step x m
        if q[y]! == 99 then
          q := q.set! y d
          cur := cur.push y
    let mut nxt : Array Nat := #[]
    for x in cur do
      for m in QT do
        let y := step x m
        if q[y]! == 99 then
          q := q.set! y (d + 1)
          nxt := nxt.push y
    cur := nxt
  return q
def QTC : Array Nat := qtCompute
def qt (r : Nat) : Nat := QTC[r]!

/-- The check of the quarter-turn count, independent of how `QTC` was computed.  For every r:
  * qt r = 0 exactly when r ∈ Z;
  * a half turn keeps qt, a quarter turn changes it by at most 1 (qt r ≤ qt (r·m) + 1);
  * if qt r > 0, some h ∈ HC and quarter turn m give qt (h then … ) — precisely: qt (rank (r then h then m)) =
    qt r - 1.
  (r then h) is reached from r by half turns (h is a product of half turns), so the third point gives a sequence
  with qt r quarter turns into Z; the second, followed along any sequence with k quarter turns into Z, gives
  qt r ≤ k.  So qt r is the fewest quarter turns. -/
def qtRule : Bool := Id.run do
  let hc := HC
  for r in [0:NC] do
    let d := qt r
    if d > 20 then return false
    if (d == 0) != inZ r then return false
    for m in HALF do
      if qt (step r m) != d then return false
    for m in QT do
      if d > qt (step r m) + 1 then return false
    if d > 0 then
      let a := ARR[r]!
      let ok := hc.any fun h => QT.any fun m => qt (rank (amul (amul a ARR[h]!) CMOV[m]!)) + 1 == d
      if !ok then return false
  return true

/-! ### Corner subsets -/

/-- Can half turns bring the corner places of `mask` onto one face?  (BFS over masks.) -/
def onAFace (mask : Nat) : Bool := Id.run do
  let mut seen := Array.replicate 256 false
  let mut q := #[mask]
  seen := seen.set! mask true
  let mut i := 0
  let mut ok := false
  while i < q.size do
    let x := q[i]!
    i := i + 1
    if FACEMASK.contains x then ok := true
    for m in HALF do
      let y := maskMv CMOV[m]! x
      if !seen[y]! then
        seen := seen.set! y true
        q := q.push y
  return ok

def NAMES : Array String :=
  #["0c0", "4a1", "4a2", "4b2", "0c3", "2c3", "4a3", "4b3", "0c4", "2c4", "4a4", "4b4", "2c5", "4b5"]

/-- (bad corners counted 0/2/4, qt, shape a?) ↦ subset index; 99 when no subset has that combination. -/
def subsetIndex (nb q : Nat) (isA : Bool) : Nat :=
  match nb, q, isA with
  | 0, 0, _ => 0 | 0, 3, _ => 4 | 0, 4, _ => 8
  | 2, 3, _ => 5 | 2, 4, _ => 9 | 2, 5, _ => 12
  | 4, 1, true => 1 | 4, 2, true => 2 | 4, 3, true => 6 | 4, 4, true => 10
  | 4, 2, false => 3 | 4, 3, false => 7 | 4, 4, false => 11 | 4, 5, false => 13
  | _, _, _ => 99

def subsetOf (r : Nat) : Nat :=
  let a := ARR[r]!
  let n := nbad a
  let nb := if n == 8 then 0 else if n == 6 then 2 else n
  subsetIndex nb (qt r) (if n == 4 then onAFace (badMask a) else false)
/-- The subset of every rank, computed once. -/
def SUB : Array Nat := (Array.range NC).map subsetOf
def sub (r : Nat) : Nat := SUB[r]!
def NBAD : Array Nat := ARR.map nbad
/-- Shape letter of a 4-bad-corner arrangement (true = 'a'). -/
def SHAPEA : Array Bool := ARR.map fun a => nbad a == 4 && onAFace (badMask a)

/-! ### Cosets -/

/-- The smallest rank of the coset {h then r : h ∈ HC}. -/
def cosetRep (r : Nat) : Nat :=
  let a := ARR[r]!
  HC.foldl (fun acc h => min acc (rank (amul ARR[h]! a))) NC
def REP : Array Nat := (Array.range NC).map cosetRep
/-- The 420 representatives, in increasing order. -/
def REPS : Array Nat := (Array.range NC).filter fun r => REP[r]! == r

/-- Per rank: the subset is that of its coset representative (so it is a function of the coset), and a half turn
does not change it.  Also: every coset has 96 elements. -/
def subsetChecks : Bool := Id.run do
  let mut size := Array.replicate NC 0
  for r in [0:NC] do
    if sub r == 99 then return false
    if sub r != sub REP[r]! then return false
    for m in HALF do
      if sub (step r m) != sub r then return false
    size := size.modify REP[r]! (· + 1)
  return REPS.all fun k => size[k]! == 96

/-! ### FakeMMAP's section bounds α_i (`htrtools alpha`) -/

/-- `HT[t]`: the fewest half turns from r to an arrangement from which some quarter turn lands in subset t (BFS
over half turns from all such arrangements; 255 = never). -/
def htGoals (t : Nat) : List Nat := (List.range NC).filter fun r => QT.any fun m => sub (step r m) == t
def HT : Array ByteArray := (Array.range 14).map fun t => search.bfs NC (htGoals t) HALF step

/-- The half-turn closure of a set of ranks (given as a 0/1 array). -/
def closeHalf (s : Array Bool) : Array Bool := Id.run do
  let mut c := s
  let mut q : Array Nat := (Array.range NC).filter fun r => s[r]!
  let mut i := 0
  while i < q.size do
    let x := q[i]!
    i := i + 1
    for m in HALF do
      let y := step x m
      if !c[y]! then
        c := c.set! y true
        q := q.push y
  return c

/-- α of a corner path p = [s_0, …, s_N] (subset indices) and whether some arrangement follows it.
R_0 = the arrangements in s_0; R_{i+1} = (half-turn closure of R_i) then a quarter turn landing in s_{i+1};
α_i = min over R_i of HT[s_{i+1}]; α_N = 0.  The same procedure as `htrtools alpha`. -/
@[noinline] def alphaOf (ht : Array ByteArray) (p : List Nat) : List Nat × Bool := Id.run do
  let mut cur : Array Bool := (Array.range NC).map fun r => sub r == p[0]!
  let mut al : List Nat := []
  let mut feasible := true
  for i in [0:p.length - 1] do
    let t := p[i + 1]!
    let htt := ht[t]!
    let mut a := 255
    for r in [0:NC] do
      if cur[r]! then a := min a (htt.get! r).toNat
    al := al ++ [a]
    let clo := closeHalf cur
    let mut nxt := Array.replicate NC false
    for r in [0:NC] do
      if clo[r]! then
        for m in QT do
          let y := step r m
          if sub y == t then nxt := nxt.set! y true
    if !nxt.any id then feasible := false
    cur := nxt
  return (al ++ [0], feasible)

def nameIdx (s : String) : Nat := (NAMES.toList.idxOf s)
/-- "4a3 > 4b2 > 4a1 > 0c0" ↦ [6, 3, 1, 0]. -/
def parsePath (s : String) : List Nat := (s.splitOn " > ").map nameIdx

/-! ### Fake HTRs (claim C07) and bare quarter turns (claim C10) -/

/-- The arrangements with no bad corner, with their subsets. -/
def noBad : List Nat := (List.range NC).filter fun r => NBAD[r]! == 0

/-- C10: arrangements with qt = q, and those among them from which a bare quarter turn (U U' D D'), done on the
arrangement or on its inverse, gives qt = 2. -/
def bareQt (q : Nat) : Nat × Nat := Id.run do
  let mut n := 0
  let mut hit := 0
  for r in [0:NC] do
    if qt r == q then
      n := n + 1
      if [r, CINV[r]!].any fun x => QT.any fun m => qt (step x m) == 2 then hit := hit + 1
  return (n, hit)

end corners
end HTRRoutes
