/-
  DRXs.EightFe — section 6.3 of the write-up (research/src/eo8_hist.py): from a full EO, with the moves that keep
  it, the DR-2s 8fe is exactly as far as the real DR, because an 8fe is a DR with the pieces renamed.

  The renaming (eo8_hist.rename): move every piece a quarter turn around an axis (the whole-cube turn `z` about
  F/B, or `x` about R/L), leave the centres, then flip every edge in its place.  On places this is one permutation
  `R` (place i goes to FLIP[Zc[i]]), so rename(s) = apply s R.  It is not a legal cube move (it can break the
  permutation parity), which is fine: distances to a DR depend only on the colours that `fe.look` reads.

  The search space.  With F/B EO solved and the 14 turns that keep it (U D R L any way, F2, B2), what `fe.look`
  with the U/D colours reads of a state is: at each place whether the sticker is U/D-coloured, and at the stickers
  of the four E-slice pieces (no U/D colour) their colour axis.  `absF` keeps exactly that (codes 1 = U/D colour,
  2 = F/B colour of an E piece, 3 = R/L colour of an E piece, 0 = anything else), and `lift` turns it back into a
  sticker array with the same colour axes where `look` reads them (U centre, F centre, R centre as stand-ins;
  code 0 becomes the F centre, which is not U/D-coloured).  A turn acts on `absF s` by the same `apply`.
  So a BFS over these abstract positions is a BFS over cosets: 2187 twists x 495 E-slice placements.
-/
import DRXs.EdgeOrient

namespace DRXs
namespace eightfe
open cube fecosets

/-- The whole-cube quarter turn about axis a (`z` for a = 2, `x` for a = 0), as in cube.py's add('z', 2,
(-1, 0, 1), 1). -/
def rot (a : Nat) : State := layer_move a [-1, 0, 1] 1

/-- Centre places (one non-zero coordinate). -/
def isCentre (i : Nat) : Bool := (cube.ST[i]!.1.filter (· != 0)).length == 1

/-- The rotation with the centres left where they are. -/
def rotKeepCentres (a : Nat) : State := let r := rot a; (Array.range 54).map fun i => if isCentre i then i else r[i]!

/-- Flip every edge in its place: swap the two places of each edge cubie. -/
def FLIP : State := Id.run do
  let mut m := Array.range 54
  for p in fe.EDGES do
    let pl := fe.CUBIES p
    m := (m.set! pl[0]! pl[1]!).set! pl[1]! pl[0]!
  return m

/-- The renaming as one place permutation: place i goes to FLIP[Zc[i]]. -/
def R (a : Nat) : State := let z := rotKeepCentres a; let fl := FLIP; (Array.range 54).map fun i => fl[z[i]!]!

/-- eo8_hist.rename(s, 'z' / 'x'): turn the pieces, put the centres back, flip every edge. -/
def renameSeq (s : State) (a : Nat) : State := Id.run do
  let mut t := apply s (rot a)
  for i in [0:54] do
    if isCentre i then t := t.set! i i
  for p in fe.EDGES do
    let pl := fe.CUBIES p
    let x := t[pl[0]!]!; let y := t[pl[1]!]!
    t := (t.set! pl[0]! y).set! pl[1]! x
  return t

/-- The move that the renaming turns m into: the face turn m' with R ∘ m = m' ∘ R on places (none if there is
none). -/
def sigma (a : Nat) (m : String) : Option String :=
  let r := R a; let mm := MOVES m
  NAMES.find? fun m' => let mm' := MOVES m'; (List.range 54).all fun i => r[mm[i]!]! == mm'[r[i]!]!

/-- The 14 turns that keep F/B EO (no F or B quarter turns). -/
def KEEP : List String := ["U", "U2", "U'", "D", "D2", "D'", "R", "R2", "R'", "L", "L2", "L'", "F2", "B2"]

/-! ## The abstract positions -/

def absF (s : State) : Array Nat :=
  (Array.range 54).map fun i =>
    let h := s[i]!
    if fe.AXIS_OF_FACE FACE_OF[h]! == 1 then 1
    else if edges.isE h then (if fe.AXIS_OF_FACE FACE_OF[h]! == 2 then 2 else 3)
    else 0

def U_C : Nat := IDX ([0, 1, 0], [0, 1, 0])
def F_C : Nat := IDX ([0, 0, 1], [0, 0, 1])
def R_C : Nat := IDX ([1, 0, 0], [1, 0, 0])

def lift (x : Array Nat) : State :=
  let u := U_C; let r := R_C; let f := F_C
  x.map fun v => if v == 1 then u else if v == 3 then r else f

abbrev Key := UInt64 × UInt64

def pack (x : Array Nat) : Key := Id.run do
  let mut a : UInt64 := 0
  let mut b : UInt64 := 0
  for i in [0:27] do a := a ||| ((x[i]!.toUInt64) <<< (2 * i).toUInt64)
  for i in [0:27] do b := b ||| ((x[27 + i]!.toUInt64) <<< (2 * i).toUInt64)
  return (a, b)

def unpack (k : Key) : Array Nat := Id.run do
  let mut x := Array.replicate 54 0
  for i in [0:27] do x := x.set! i ((k.1 >>> (2 * i).toUInt64) &&& 3).toNat
  for i in [0:27] do x := x.set! (27 + i) ((k.2 >>> (2 * i).toUInt64) &&& 3).toNat
  return x

/-- The two 8fe kinds of the U/D colours: corners on a side axis, all eight layer edges flipped, two slices.
(The third kind with eight flips, on U/D with the centres right, is the other DR-2s, not the 8fe.) -/
def eightKinds : List Sig := kinds.filter fun g => g.f != 1 && g.flips.all (· == 1) && slices g == 2

/-- Real DR on U/D, read through `lift`. -/
def isDR (x : Array Nat) : Bool := match sig_of (lift x) 1 with
  | none => false
  | some g => is_dr g

/-- DR-2s 8fe of the U/D colours (either pair of side faces), read through `lift`. -/
def is8fe (x : Array Nat) : Bool :=
  [0, 2].any fun f => match sig_of (lift x) f with
    | none => false
    | some g => eightKinds.contains g

/-- All twelve edges good for F/B, read through `lift`. -/
def fullEO (x : Array Nat) : Bool := let y := lift x; fe.EDGES.all fun p => edges.good 2 y p

structure Space where
  keys : Array Key
  index : Std.HashMap Key Nat
  /-- for each position, the indices of its 14 neighbours (a neighbour outside the space would be 10^9) -/
  nbrs : Array (Array Nat)

/-- Code at place i of a packed position. -/
@[inline] def codeAt (k : Key) (i : Nat) : UInt64 :=
  if i < 27 then (k.1 >>> (2 * i).toUInt64) &&& 3 else (k.2 >>> (2 * (i - 27)).toUInt64) &&& 3

/-- `pack (apply (unpack k) P)` without building the arrays: the code at place i moves to place P[i]. -/
def stepKey (k : Key) (P : Array Nat) : Key := Id.run do
  let mut a : UInt64 := 0
  let mut b : UInt64 := 0
  for i in [0:54] do
    let c := codeAt k i
    let j := P[i]!
    if j < 27 then a := a ||| (c <<< (2 * j).toUInt64) else b := b ||| (c <<< (2 * (j - 27)).toUInt64)
  return (a, b)

def KEEPP : Array State := (KEEP.map MOVES).toArray

/-- Every abstract position reachable from the solved cube with the 14 turns, and the move graph on them. -/
def space (_ : Unit) : Space := Id.run do
  let start := pack (absF SOLVED)
  let mut index : Std.HashMap Key Nat := {}
  index := index.insert start 0
  let mut keys : Array Key := #[start]
  -- level by level, never reading the array that is being pushed to
  let mut frontier : Array Key := #[start]
  while !frontier.isEmpty do
    let mut next : Array Key := #[]
    for x in frontier do
      for P in KEEPP do
        let k := stepKey x P
        if !index.contains k then
          index := index.insert k (keys.size + next.size)
          next := next.push k
    keys := keys ++ next
    frontier := next
  let mut nbrs : Array (Array Nat) := Array.mkEmpty keys.size
  for k in keys do
    nbrs := nbrs.push (KEEPP.map fun P => index.getD (stepKey k P) 1000000000)
  return ⟨keys, index, nbrs⟩

/-- Breadth-first distances on the space from the positions where `target` holds (255 = not reached). -/
@[noinline] def bfs (sp : Space) (target : Array Bool) : Array Nat := Id.run do
  let n := sp.keys.size
  let mut d := Array.replicate n 255
  let mut frontier : Array Nat := #[]
  for i in [0:n] do
    if target[i]! then
      d := d.set! i 0; frontier := frontier.push i
  let mut k := 0
  while !frontier.isEmpty do
    k := k + 1
    let mut next : Array Nat := #[]
    for i in frontier do
      for j in sp.nbrs[i]! do
        if j < n && d[j]! == 255 then
          d := d.set! j k; next := next.push j
    frontier := next
  return d

/-- The distances form a BFS table: 0 exactly on the target, and every other entry is 1 + the least entry
among its neighbours (the moves are closed under inverses, so neighbours both ways are the same set). -/
def ruleHolds (sp : Space) (target : Array Bool) (d : Array Nat) : Bool :=
  (List.range sp.keys.size).all fun i =>
    let nb := sp.nbrs[i]!.toList.map fun j => d[j]!
    if target[i]! then d[i]! == 0 else d[i]! == 1 + nb.foldl min 255

/-- `sorted(Counter(l).items())` for an array of small numbers. -/
def histA (d : Array Nat) : List (Nat × Nat) := Id.run do
  let mut h := Array.replicate 256 0
  for v in d do h := h.modify v (· + 1)
  return ((List.range 256).map fun k => (k, h[k]!)).filter (·.2 != 0)

structure Result where
  positions : Nat
  /-- neighbours outside the space -/
  outside : Nat
  /-- positions that are not full F/B EO -/
  notEO : Nat
  /-- positions that are a real DR / an 8fe -/
  nDR : Nat
  n8fe : Nat
  /-- the DR table and the 8fe table pass `ruleHolds` -/
  rulesOK : Bool
  histDR : List (Nat × Nat)
  hist8fe : List (Nat × Nat)
  sumDR : Nat
  sum8fe : Nat
  /-- positions where the 8fe distance is not the DR distance of the renamed position (renaming about F/B) -/
  renameBad : Nat
  /-- positions whose renamed position is outside the space -/
  renameOutside : Nat
  deriving Repr, DecidableEq

/-- (positions where the 8fe distance differs from the DR distance of the renamed position, renamed positions
outside the space).  The renaming permutation is an argument so that it is built once. -/
@[noinline] def renameCheck (sp : Space) (Rz : State) (d8 dDR : Array Nat) : Nat × Nat := Id.run do
  let mut bad := 0
  let mut outside := 0
  for i in [0:sp.keys.size] do
    match sp.index.get? (stepKey sp.keys[i]! Rz) with
    | none => outside := outside + 1
    | some j => if d8[i]! != dDR[j]! then bad := bad + 1
  return (bad, outside)

def run (_ : Unit) : Result := Id.run do
  let sp := space ()
  let n := sp.keys.size
  let tDR := sp.keys.map fun k => isDR (unpack k)
  let t8 := sp.keys.map fun k => is8fe (unpack k)
  let dDR := bfs sp tDR
  let d8 := bfs sp t8
  let (bad, outside) := renameCheck sp (R 2) d8 dDR
  let sum (d : Array Nat) := d.foldl (· + ·) 0
  return { positions := n,
           outside := (sp.nbrs.toList.map fun a => a.toList.countP (· ≥ n)).foldl (· + ·) 0,
           notEO := (sp.keys.toList.countP fun k => !fullEO (unpack k)),
           nDR := tDR.toList.countP id, n8fe := t8.toList.countP id,
           rulesOK := ruleHolds sp tDR dDR && ruleHolds sp t8 d8,
           histDR := histA dDR, hist8fe := histA d8, sumDR := sum dDR, sum8fe := sum d8,
           renameBad := bad, renameOutside := outside }

end eightfe
end DRXs
