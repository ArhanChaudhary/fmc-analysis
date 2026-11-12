/-
  HTRRoutes.HtrGroup — the HTR group <U2, D2, R2, L2, F2, B2> and the fewest half turns that solve each of its
  states (DougCube's "HTR Finish" table; the research's `out/checks/htr_states.tsv`, column half_turn_optimal).

  Half turns keep every corner in its tetrad, every M piece in an M place, every S piece in an S place, and the
  E-slice pieces in the E slice (`half_turns_keep_parts` in `Model.lean`).  So a state reached by half turns is
  given by four permutations of four pieces each, plus the corners' split into two tetrads:

    x = ((c · 24 + mE) · 24 + sE) · 24 + e,   c = rank(tetrad-1 corners) · 24 + rank(tetrad-2 corners) (0 … 575)
    mE, sE, e = rank of the M pieces among the M places, of the S pieces among the S places, of the E slice

  N = 576 · 24³ = 7,962,624 slots.  `decode x` gives the (corners, U/D edges, E slice) arrangements, and each
  half turn acts on each of the four parts on its own (tables `CT`, `MT`, `ST`, `LT`, built by doing the move on
  `decode`'s arrangements and reading the part back).  `parts_follow_moves` checks, for every value of every part
  and every half turn, that the table entry decodes to the arrangement the move gives.  `bfs` from the solved
  cube (x = 0) with the six half turns then gives the fewest half turns for every state reached, checked by
  `search.ruleHolds`.
-/
import HTRRoutes.Pieces
import HTRRoutes.Search

set_option compiler.extract_closed false

namespace HTRRoutes
namespace htr
open pieces

/-- The places of each part, in increasing order. -/
def T1 : Array Nat := (Array.range 8).filter fun i => TET[i]!
def T2 : Array Nat := (Array.range 8).filter fun i => !TET[i]!
def MP : Array Nat := (Array.range 8).filter fun k => ISM[k]!
def SP : Array Nat := (Array.range 8).filter fun k => ISS[k]!

/-- Put permutation σ (of 0 … 3) of the places P into arrangement a: a[P[j]] = P[σ j]. -/
def put (a : Array Nat) (P : Array Nat) (σ : Array Nat) : Array Nat := Id.run do
  let mut a := a
  for j in [0:4] do a := a.set! P[j]! P[σ[j]!]!
  return a
/-- Read the permutation of places P back from arrangement a (P.size if a piece is outside P). -/
def take (a : Array Nat) (P : Array Nat) : Array Nat := (Array.range 4).map fun j => P.toList.idxOf a[P[j]!]!
def stays (a : Array Nat) (P : Array Nat) : Bool := (Array.range 4).all fun j => P.contains a[P[j]!]!

def cDec (c : Nat) : Array Nat := put (put (ident 8) T1 (unrank 4 (c / 24))) T2 (unrank 4 (c % 24))
def cEnc (a : Array Nat) : Nat := rank (take a T1) * 24 + rank (take a T2)
def eDec (mE sE : Nat) : Array Nat := put (put (ident 8) MP (unrank 4 mE)) SP (unrank 4 sE)

def N : Nat := 576 * 24 * 24 * 24

/-- The (corners, U/D edges, E slice) arrangements of x. -/
def decode (x : Nat) : Array Nat × Array Nat × Array Nat :=
  let e := x % 24
  let sE := (x / 24) % 24
  let mE := (x / 576) % 24
  let c := x / 13824
  (cDec c, eDec mE sE, unrank 4 e)

/-- Part tables, `[move index in HALF order 0 … 5][value]`. -/
def CT : Array (Array Nat) := HALF.toArray.map fun m => (Array.range 576).map fun c => cEnc (amul (cDec c) CMOV[m]!)
def MT : Array (Array Nat) := HALF.toArray.map fun m =>
  (Array.range 24).map fun v => rank (take (amul (eDec v 0) EMOV[m]!) MP)
def ST : Array (Array Nat) := HALF.toArray.map fun m =>
  (Array.range 24).map fun v => rank (take (amul (eDec 0 v) EMOV[m]!) SP)
def LT : Array (Array Nat) := HALF.toArray.map fun m => (Array.range 24).map fun v => rank (amul (unrank 4 v) SMOV[m]!)

/-- Half turn number i (0 … 5 = U2 D2 R2 L2 F2 B2) on x. -/
def stepWith (ct mt st lt : Array (Array Nat)) (x i : Nat) : Nat :=
  let e := x % 24
  let sE := (x / 24) % 24
  let mE := (x / 576) % 24
  let c := x / 13824
  ((ct[i]![c]! * 24 + mt[i]![mE]!) * 24 + st[i]![sE]!) * 24 + lt[i]![e]!

/-- For every value of every part and each half turn: the move keeps the part in its places, and the table entry
decodes to what the move does.  (The edge parts are checked with every value of the other edge part.) -/
def partsFollow : Bool :=
  (List.range 6).all fun i =>
    let m := HALF[i]!
    ((List.range 576).all fun c =>
      let a := amul (cDec c) CMOV[m]!
      stays a T1 && stays a T2 && cDec (CT[i]![c]!) == a) &&
    ((List.range 24).all fun v => (List.range 24).all fun w =>
      let a := amul (eDec v w) EMOV[m]!
      stays a MP && stays a SP && eDec (MT[i]![v]!) (ST[i]![w]!) == a) &&
    ((List.range 24).all fun v => unrank 4 (LT[i]![v]!) == amul (unrank 4 v) SMOV[m]!)

/-- Decoding is one to one on the N slots, and slot 0 is the solved cube. -/
def decodeOk : Bool :=
  ((List.range 576).all fun c => cEnc (cDec c) == c) &&
  ((List.range 24).all fun v => rank (unrank 4 v) == v) &&
  ((List.range 24).all fun v => (List.range 24).all fun w =>
    rank (take (eDec v w) MP) == v && rank (take (eDec v w) SP) == w) &&
  decode 0 == (ident 8, ident 8, ident 4)

structure Result where
  rule : Bool
  states : Nat
  hist : List (Nat × Nat)
  deriving DecidableEq, Repr

def run : Result :=
  let st := stepWith CT MT ST LT
  let d := search.bfs N [0] (List.range 6) st
  let h := search.distHist d
  ⟨search.ruleHolds N (· == 0) (List.range 6) st d, h.foldl (· + ·.2) 0, h⟩

/-- How many corner values (of 576) and edge values (M, S, E parts together, of 24³) occur among the states the
BFS reaches. -/
@[noinline] def partsOf (d : ByteArray) : Nat × Nat := Id.run do
  let mut cs := Array.replicate 576 false
  let mut es := Array.replicate 13824 false
  for x in [0:N] do
    if search.reached d x then
      cs := cs.set! (x / 13824) true
      es := es.set! (x % 13824) true
  return (cs.toList.count true, es.toList.count true)

def partsReached : Nat × Nat := partsOf (search.bfs N [0] (List.range 6) (stepWith CT MT ST LT))

end htr
end HTRRoutes
