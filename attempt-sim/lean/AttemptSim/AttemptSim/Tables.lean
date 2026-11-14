/-
  AttemptSim.Tables — the simulator's small tables, embedded from its export (data/), and the DR group in
  judging-a-dr's numbering built from the sticker cube, for the HTR table.

    EOMV, COMV, SLMV   coordinate move tables: row = coordinate, 18 columns = moves (eo_mv.txt, co_mv.txt, sl_mv.txt)
    EODIST             fewest turns to F/B EO per flip coordinate (eodist.txt, 2,048 entries)
    DRDIST             fewest EO-keeping turns to DR on U/D per (twist coordinate, slice coordinate), EO solved
                       (drdist.txt: the simulator's drdist.u8 with value v written as the letter 'a' + v; 1,082,565)
    HTRDIST            fewest DR moves to HTR per (corner coset, edge pattern) (htrdist.txt, 420 × 70), with the coset
                       representatives and the patterns of cosets.txt (the numbering of judging-a-dr's class.rs)
-/
import AttemptSim.Manifest
import AttemptSim.Cubie
import AttemptSim.Search

namespace AttemptSim
namespace tables
open cube pieces cubie

def EOMV : Array Nat := nats (include_str "../data/eo_mv.txt")
def COMV : Array Nat := nats (include_str "../data/co_mv.txt")
def SLMV : Array Nat := nats (include_str "../data/sl_mv.txt")
def EODIST_L : Array Nat := nats (include_str "../data/eodist.txt")
def toBytes (a : Array Nat) : ByteArray := Id.run do
  let mut b := ByteArray.emptyWithCapacity a.size
  for x in a do b := b.push x.toUInt8
  return b
def EODIST : ByteArray := toBytes EODIST_L
/-- drdist.txt: one letter per entry, 'a' + value. -/
def DRDIST : ByteArray := Id.run do
  let t := (include_str "../data/drdist.txt").toUTF8
  let mut b := ByteArray.emptyWithCapacity t.size
  for i in [0:t.size] do b := b.push (t.get! i - 97)
  return b
def HTRDIST_L : Array Nat := nats (include_str "../data/htrdist.txt")
def HTRDIST : ByteArray := toBytes HTRDIST_L

/-- cosets.txt: line 2 = the 420 representatives, line 4 = the 70 masks. -/
def COSET_LINES : List String := lines (include_str "../data/cosets.txt")
def REPS : Array Nat := nats (COSET_LINES.getD 1 "")
def PMASKS : Array Nat := nats (COSET_LINES.getD 3 "")

def eoStep (e mv : Nat) : Nat := EOMV[e * 18 + mv]!
/-- State x = twist coordinate · 495 + slice coordinate. -/
def drStep (x mv : Nat) : Nat := COMV[(x / 495) * 18 + mv]! * 495 + SLMV[(x % 495) * 18 + mv]!

/-! ### The DR group in judging-a-dr's numbering, from the stickers

  corner positions 0 UFR 1 UFL 2 UBL 3 UBR 4 DFR 5 DFL 6 DBL 7 DBR;  U/D-layer edges 0 UF 1 UL 2 UB 3 UR 4 DF 5 DL
  6 DB 7 DR;  moves 0 U 1 U2 2 U' 3 D 4 D2 5 D' 6 R2 7 L2 8 F2 9 B2  (vendor/core.rs).
  A state is "the piece at each position"; a move that carries position p to t[p] gives new[t[p]] = old[p]. -/

def CPOS : Array Vec := #[[1,1,1],[-1,1,1],[-1,1,-1],[1,1,-1],[1,-1,1],[-1,-1,1],[-1,-1,-1],[1,-1,-1]]
def EPOS : Array Vec := #[[0,1,1],[-1,1,0],[0,1,-1],[1,1,0],[0,-1,1],[-1,-1,0],[0,-1,-1],[1,-1,0]]
def DRNAMES : List String := ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
def HALF : List Nat := [1, 4, 6, 7, 8, 9]

/-- Where DR move m carries each position of a group of positions: t[p]. -/
def posMap (P : Array Vec) (name : String) : Array Nat :=
  P.map fun p => P.toList.idxOf (cube.ST[(MOVES name)[(CUBIES p).headD 54]!]!.1)
def CT : Array (Array Nat) := (DRNAMES.map (posMap CPOS)).toArray
def ET : Array (Array Nat) := (DRNAMES.map (posMap EPOS)).toArray

/-- new[t[p]] = old[p]. -/
def applyPos (t a : Array Nat) : Array Nat := Id.run do
  let mut r := Array.replicate a.size 0
  for p in [0:a.size] do r := r.set! t[p]! a[p]!
  return r

/-- Lexicographic rank of a permutation (`rank_perm` of core.rs). -/
def rank (a : Array Nat) : Nat := Id.run do
  let n := a.size
  let mut r := 0
  for i in [0:n] do
    let mut c := 0
    for j in [i+1:n] do
      if a[j]! < a[i]! then c := c + 1
    r := r * (n - i) + c
  return r
/-- The permutation of 0 … n-1 with rank r (`unrank_perm`). -/
def unrank (n r : Nat) : Array Nat := Id.run do
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

/-- The corner permutations reached from solved by half turns (the HTR corner group), as arrays. -/
def HC : Array (Array Nat) := Id.run do
  let mut seen : Array (Array Nat) := #[Array.range 8]
  let mut head := 0
  while head < seen.size do
    let c := seen[head]!
    head := head + 1
    for m in HALF do
      let d := applyPos CT[m]! c
      if !seen.contains d then seen := seen.push d
  return seen

/-- The smallest rank in the coset H·p = { h ∘ p } (renaming the pieces of p by an HTR element): `ccos_rep`. -/
def canon (p : Array Nat) : Nat :=
  HC.foldl (fun best h => min best (rank (p.map fun x => h[x]!))) 40320
/-- `CANON[r]` for every corner permutation rank r. -/
def CANON : Array Nat := (Array.range 40320).map fun r => canon (unrank 8 r)
/-- Rank after DR move m. -/
def cstep (r m : Nat) : Nat := rank (applyPos CT[m]! (unrank 8 r))

/-- Number of each representative (420 = not a representative). -/
def KOF : Array Nat := Id.run do
  let mut a := Array.replicate 40320 420
  for k in [0:REPS.size] do a := a.set! REPS[k]! k
  return a

/-- The mask of positions holding M-slice edges (pieces 0 2 4 6 = UF UB DF DB), after a move: bit t[p] = bit p. -/
def maskStep (mask m : Nat) : Nat :=
  (List.range 8).foldl (fun acc p => if (mask >>> p) % 2 == 1 then acc + 2 ^ (ET[m]!)[p]! else acc) 0
def BOF : Array Nat := Id.run do
  let mut a := Array.replicate 256 70
  for b in [0:PMASKS.size] do a := a.set! PMASKS[b]! b
  return a

/-- Coset moves: `CCM[k * 10 + m]` = number of the coset of (representative k, then move m). -/
def CCM : Array Nat := (Array.range 4200).map fun i => KOF[CANON[cstep REPS[i / 10]! (i % 10)]!]!
def PPM : Array Nat := (Array.range 700).map fun i => BOF[maskStep PMASKS[i / 10]! (i % 10)]!
/-- State x = coset · 70 + pattern. -/
def htrStep (x m : Nat) : Nat := CCM[(x / 70) * 10 + m]! * 70 + PPM[(x % 70) * 10 + m]!
def HTR_GOAL : Nat := KOF[0]! * 70 + BOF[85]!

end tables
end AttemptSim
