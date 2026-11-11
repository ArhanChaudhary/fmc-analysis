/-
  DRBound.Search — the computing part: how a state is looked at ("features"), and the tables.

  Nothing in this file has to be trusted to be *correct*: the theorems in `DRBound.Theorems` only use
  facts that are re-checked exhaustively (every arrangement of 8 pieces, every table entry, every move).
  If a feature map or a table were wrong, those checks would fail and the theorems would not compile.
-/
import DRBound.Cube

namespace DRBound

/-! ### Small utilities -/

def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

/-- Lexicographic rank of an arrangement of 8 pieces (0 … 40319 for permutations). -/
def rank8 (v : Arr8) : Nat := Id.run do
  let mut r := 0
  for i in [0:8] do
    let mut k := 0
    for j in [i+1:8] do
      if (v[j]!).val < (v[i]!).val then k := k + 1
    r := r * (8 - i) + k
  return r

/-- The arrangement with a given rank. -/
def unrank8 (r : Nat) : Arr8 := Id.run do
  let mut avail : List (Fin 8) := List.finRange 8
  let mut out : Array (Fin 8) := #[]
  let mut r := r
  for i in [0:8] do
    let f := fact (7 - i)
    let x := avail.getD (r / f) 0
    r := r % f
    out := out.push x
    avail := avail.erase x
  return Vector.ofFn fun p => out.getD p.val 0

/-- Rename the pieces of `v` by `k` (the state "k, then v"). -/
def relabel (k v : Arr8) : Arr8 := Vector.ofFn fun p => k[v[p]]

/-- Parity (0 or 1) of an arrangement of the four E-slice edges. -/
def parity4 (s : Arr4) : Nat := Id.run do
  let mut k := 0
  for i in [0:4] do
    for j in [i+1:4] do
      if (s[j]!).val < (s[i]!).val then k := k + 1
  return k % 2

/-! ### A coordinate: "what we see" of eight pieces, as a number, with its move table -/

/-- `feat v` is the class of the arrangement `v`; `mv[i*10 + m.idx]` is the class reached from class `i`
by move `m`. -/
structure Comp where
  n : Nat
  feat : Arr8 → Nat
  mv : Array Nat

/-- Build a coordinate from a "code" (any function that is constant on classes): number the codes in
order of first appearance among the 40320 permutations, and fill the move table from representatives. -/
def mkComp (code : Arr8 → Nat) (codeBound : Nat) (src : Move → Arr8) : Comp := Id.run do
  let mut lookup : Array Nat := Array.replicate codeBound 0
  let mut seen : Array Bool := Array.replicate codeBound false
  let mut reps : Array Arr8 := #[]
  for r in [0:40320] do
    let v := unrank8 r
    let c := code v
    if !(seen.getD c true) then
      seen := seen.set! c true
      lookup := lookup.set! c reps.size
      reps := reps.push v
  let feat : Arr8 → Nat := fun v => lookup.getD (code v) 0
  let mut mv : Array Nat := Array.emptyWithCapacity (reps.size * 10)
  for v in reps do
    for m in Move.all do
      mv := mv.push (feat (permute8 (src m) v))
  return { n := reps.size, feat := feat, mv := mv }

/-- The coordinate that sees nothing. -/
def trivialComp : Comp := { n := 1, feat := fun _ => 0, mv := Array.replicate 10 0 }

/-! ### The codes -/

/-- Corner pieces seen exactly. -/
def codeExact (v : Arr8) : Nat := rank8 v

/-- Corner pieces seen up to renaming by the elements of `grp`. -/
def codeMin (grp : List Arr8) (v : Arr8) : Nat :=
  grp.foldl (fun acc k => min acc (rank8 (relabel k v))) 40320

/-- Corner arrangements of whole-cube half rotations (as seen with fixed centres): id, U2 D2, R2 L2, F2 B2. -/
def grpV : List Arr8 :=
  [id8, (solved.apply [.U2, .D2]).c, (solved.apply [.R2, .L2]).c, (solved.apply [.F2, .B2]).c]

/-- … together with U2. -/
def grpVU : List Arr8 := grpV ++ grpV.map fun k => relabel k (solved.move .U2).c

/-- The 96 corner arrangements reachable by half turns (the HTR corner group). -/
def grpH : List Arr8 := Id.run do
  let mut seen : Array Bool := Array.replicate 40320 false
  let mut all : Array Arr8 := #[id8]
  seen := seen.set! (rank8 id8) true
  let mut i := 0
  while i < all.size do
    let v := all[i]!
    for m in Move.all do
      if m.isHalf then
        let u := permute8 m.srcC v
        if !(seen.getD (rank8 u) true) then
          seen := seen.set! (rank8 u) true
          all := all.push u
    i := i + 1
  return all.toList

/-- Edges: which positions hold M-slice edges (pieces UF UB DF DB have even numbers). -/
def codeMask (v : Arr8) : Nat := Id.run do
  let mut c := 0
  for p in [0:8] do
    if (v[p]!).val % 2 == 0 then c := c + 2 ^ p
  return c

/-- Edges: which positions hold M-slice edges, plus the U/D colour of every edge, where the two colours
of the M-slice edges may be swapped, and likewise for the S-slice edges (630 classes). -/
def code630 (v : Arr8) : Nat := Id.run do
  let mut mask := 0
  let mut lay := 0
  let mut firstM := 2
  let mut firstS := 2
  for p in [0:8] do
    let q := (v[p]!).val
    let layer := q / 4
    if q % 2 == 0 then
      mask := mask + 2 ^ p
      if firstM == 2 then firstM := layer
      if layer != firstM then lay := lay + 2 ^ p
    else
      if firstS == 2 then firstS := layer
      if layer != firstS then lay := lay + 2 ^ p
  return mask * 256 + lay

/-- Edges: slice type (M or S) and U/D colour of the edge at every position, plus the two "double-swap
parities" (parity of the order in which the four M-slice edges, resp. S-slice edges, appear). -/
def code2520F (v : Arr8) : Nat := Id.run do
  let mut types := 0
  let mut seqM : Array Nat := #[]
  let mut seqS : Array Nat := #[]
  for p in [0:8] do
    let q := (v[p]!).val
    types := types + ((q % 2) * 2 + q / 4) * 4 ^ p
    if q % 2 == 0 then seqM := seqM.push (q / 2) else seqS := seqS.push (q / 2)
  let inv (a : Array Nat) : Nat := Id.run do
    let mut k := 0
    for i in [0:a.size] do
      for j in [i+1:a.size] do
        if a[j]! < a[i]! then k := k + 1
    return k % 2
  return types * 4 + inv seqM * 2 + inv seqS

/-! ### A rung of the ladder = corner coordinate × edge coordinate (× E-slice parity) -/

structure Rung where
  cC : Comp
  cE : Comp
  par : Bool

namespace Rung

def pmul (R : Rung) : Nat := if R.par then 2 else 1

/-- Table index of the class (corner class, edge class, parity bit). -/
def q (R : Rung) (cc ee p : Nat) : Nat := (cc * R.cE.n + ee) * R.pmul + p

def pbit (R : Rung) (s : Arr4) : Nat := if R.par then parity4 s else 0

def pnext (R : Rung) (p : Nat) (m : Move) : Nat := if R.par && m.isSide then 1 - p else p

/-- Index of the class reached by move `m`. -/
def qnext (R : Rung) (cc ee p : Nat) (m : Move) : Nat :=
  R.q (R.cC.mv.getD (cc * 10 + m.idx) 0) (R.cE.mv.getD (ee * 10 + m.idx) 0) (R.pnext p m)

/-- What we see of a state, as a table index. -/
def index (R : Rung) (g : State) : Nat := R.q (R.cC.feat g.c) (R.cE.feat g.e) (R.pbit g.s)

def size (R : Rung) : Nat := R.cC.n * R.cE.n * R.pmul

/-- Breadth-first search from the solved class: fewest moves to make the visible part look solved.
`halfOnly` restricts to half turns (the HTR-only variant); 255 marks classes never reached. -/
def tableWith (R : Rung) (halfOnly : Bool) : ByteArray := Id.run do
  let N := R.size
  let mut T := ByteArray.emptyWithCapacity N
  for _ in [0:N] do
    T := T.push 255
  T := T.set! (R.index solved) 0
  for d in [0:60] do
    let mut found := false
    for cc in [0:R.cC.n] do
      for ee in [0:R.cE.n] do
        for p in [0:R.pmul] do
          if (T.get! (R.q cc ee p)).toNat == d then
            for m in Move.all do
              if !halfOnly || m.isHalf then
                let j := R.qnext cc ee p m
                if T.get! j == 255 then
                  T := T.set! j (d + 1).toUInt8
                  found := true
    if !found then break
  return T

/-- The table used for bounds: all ten DR moves. -/
def table (R : Rung) : ByteArray := R.tableWith false

/-- The table is 0 at the solved class and changes by at most one along every move, in both directions. -/
def tableOK (R : Rung) (T : ByteArray) : Bool :=
  T.get! (R.index solved) == 0 &&
  Nat.all R.cC.n fun cc _ => Nat.all R.cE.n fun ee _ => Nat.all R.pmul fun p _ =>
    Move.all.all fun m =>
      (T.get! (R.q cc ee p)).toNat ≤ (T.get! (R.qnext cc ee p m)).toNat + 1 &&
      (T.get! (R.qnext cc ee p m)).toNat ≤ (T.get! (R.q cc ee p)).toNat + 1

/-- Every class with a positive (and finite) table value has a move leading to a class with value one less,
and the only class with value 0 is the solved one.  Together with `tableOK` this says the table is *exactly*
the fewest moves needed to make the visible part solved. -/
def sharpOK (R : Rung) (T : ByteArray) : Bool :=
  Nat.all R.cC.n fun cc _ => Nat.all R.cE.n fun ee _ => Nat.all R.pmul fun p _ =>
    let t := (T.get! (R.q cc ee p)).toNat
    (t == 0 && R.q cc ee p == R.index solved) || t == 255 ||
      (t != 0 && Move.all.any fun m => (T.get! (R.qnext cc ee p m)).toNat + 1 == t)

def checkTable (R : Rung) : Bool := R.tableOK R.table && R.sharpOK R.table

/-- The same search with half turns only (the HTR-only variant, as in FakeMMAP's 216-case computation). -/
def halfTable (R : Rung) : ByteArray := R.tableWith true

def halfTableOK (R : Rung) (T : ByteArray) : Bool :=
  T.get! (R.index solved) == 0 &&
  Nat.all R.cC.n fun cc _ => Nat.all R.cE.n fun ee _ => Nat.all R.pmul fun p _ =>
    Move.all.all fun m => !m.isHalf ||
      (T.get! (R.q cc ee p)).toNat ≤ (T.get! (R.qnext cc ee p m)).toNat + 1

def checkHalfTable (R : Rung) : Bool := R.halfTableOK R.halfTable

/-- HTR-only bound: table value of what we see of `g`, searching with half turns only. -/
def halfBound (R : Rung) (g : State) : Nat := (R.halfTable.get! (R.index g)).toNat

/-- **The bound**: the table value of what we see of `g`. -/
def bound (R : Rung) (g : State) : Nat := (R.table.get! (R.index g)).toNat

end Rung

/-- Do the listed (scramble, value) pairs agree with the half-turn-only table?  (Table computed once.) -/
def Rung.halfBoundsMatch (R : Rung) (cases : List (List Move × Nat)) : Bool :=
  let T := R.halfTable
  cases.all fun c => (T.get! (R.index (solved.apply c.1))).toNat == c.2

/-- How many of the listed cases get a strictly smaller value when quarter turns are allowed? -/
def Rung.countShorter (R : Rung) (cases : List (List Move × Nat)) : Nat :=
  let T := R.table
  (cases.filter fun c => (T.get! (R.index (solved.apply c.1))).toNat < c.2).length

/-- Number of different classes among the listed scrambles. -/
def Rung.countClasses (R : Rung) (cases : List (List Move × Nat)) : Nat :=
  ((cases.map fun c => R.index (solved.apply c.1)).eraseDups).length

/-- Bounds of several states at once (table computed once); for `#eval`. -/
def Rung.bounds (R : Rung) (gs : List State) : List Nat :=
  let T := R.table
  gs.map fun g => (T.get! (R.index g)).toNat

/-- For one arrangement: the class number is in range and the move table agrees with actually moving. -/
def Comp.okAt (C : Comp) (src : Move → Arr8) (v : Arr8) : Bool :=
  !decide (IsPerm8 v) ||
    (decide (C.feat v < C.n) &&
      Move.all.all fun m => C.mv.getD (C.feat v * 10 + m.idx) 0 == C.feat (permute8 (src m) v))

/-- Moves keep arrangements legal. -/
def movesKeepPerm8 (v : Arr8) : Bool :=
  !decide (IsPerm8 v) ||
    Move.all.all fun m => decide (IsPerm8 (permute8 m.srcC v)) && decide (IsPerm8 (permute8 m.srcE v))

/-- E slice: moves keep arrangements legal; side half turns flip the parity, other moves keep it. -/
def sliceOK (s : Arr4) : Bool :=
  !decide (IsPerm4 s) ||
    (decide (parity4 s < 2) && Move.all.all fun m =>
      decide (IsPerm4 (permute4 m.srcS s)) &&
      parity4 (permute4 m.srcS s) == (if m.isSide then 1 - parity4 s else parity4 s))

/-- The three exhaustive checks of a rung, as compiled programs. -/
def Rung.cornersOK (R : Rung) : Bool := all8 (R.cC.okAt Move.srcC)
def Rung.edgesOK (R : Rung) : Bool := all8 (R.cE.okAt Move.srcE)
def movesKeepPermAll : Bool := all8 movesKeepPerm8
def sliceOKAll : Bool := all4 sliceOK

/-! ### The rungs that are certified -/

/-- Corners only: the optimal corner-solution length `L`. -/
def rungC : Rung := { cC := mkComp codeExact 40320 Move.srcC, cE := trivialComp, par := false }

/-- Corners + E-slice parity. -/
def rungCP : Rung := { cC := mkComp codeExact 40320 Move.srcC, cE := trivialComp, par := true }

/-- HTR coset: which corners and edges are bad.  Its table is the optimal DR→HTR length. -/
def rungHTR : Rung :=
  { cC := mkComp (codeMin grpH) 40321 Move.srcC, cE := mkComp codeMask 256 Move.srcE, par := false }

/-- The features behind Rodney Kinney's NISS@1qt recognition and FakeMMAP's 216-case table, for every DR
state: corners up to whole-cube half rotations and U2, 630 edge classes, E-slice parity. -/
def rungKF : Rung :=
  { cC := mkComp (codeMin grpVU) 40321 Move.srcC, cE := mkComp code630 65536 Move.srcE, par := true }

/-- Corners + which edges are bad + E-slice parity: the shortest HTR that also solves the corners. -/
def rungCBadP : Rung :=
  { cC := mkComp codeExact 40320 Move.srcC, cE := mkComp codeMask 256 Move.srcE, par := true }

/-- Edges: the 630 classes of `code630` plus the two double-swap parities. -/
def code630F (v : Arr8) : Nat := code630 v * 4 + code2520F v % 4

/-- `KF` without the free U2 and with the double-swap parities (generalises FakeMMAP's "OBL++" sheet). -/
def rungK0F : Rung :=
  { cC := mkComp (codeMin grpV) 40321 Move.srcC, cE := mkComp code630F 262144 Move.srcE, par := false }

/-- The finest rung: corners exactly, slice type and colour of every U/D-layer edge, double-swap parities. -/
def rungFull : Rung :=
  { cC := mkComp codeExact 40320 Move.srcC, cE := mkComp code2520F 262144 Move.srcE, par := false }

end DRBound
