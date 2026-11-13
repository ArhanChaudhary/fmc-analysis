/-
  EOSwitch.Rings — the two-ring picture of a state, what each EO-keeping turn does to it, and the counts that do
  not count U and D turns (part F of README.md, added 2026-11-13; the research's `src/rings.py`).

  The picture.  A layer is a ring of 8 places read clockwise from outside the cube (U from above, D from below):
      U: UB UBR UR UFR UF UFL UL UBL        D: DB DBL DL DFL DF DFR DR DBR
  kept as 4 edge places 0 … 3 and 4 corner places 0 … 3, corner k between edge k and edge k + 1.  The places are
  found from coordinates: (x, z) = (0,−1) (1,−1) (1,0) (1,1) (0,1) (−1,1) (−1,0) (−1,−1) at y = 1 for U, and the
  same list with x negated at y = −1 for D.  An edge place is *bad* (1) when it holds an E-slice piece.  A bad
  corner *points* at the one of its two neighbouring edge places it would pair with, i.e. the place k with
  `udAxis c = ZAX[k]` (Switch.lean's definition of a pair): 1 = clockwise (edge k + 1), 2 = counter-clockwise
  (edge k), 0 = a good corner.  A *row* is corner k − 1, edge k, corner k of one ring: the three places of a layer
  on one side face.  The four E-slice places FR FL BL BR are *holes* (1) when they hold a U/D-layer piece.

  What the turns do to it (`expected`; theorem `ring_turns` checks it on every state and every turn):
    * U, D: rotate that ring, edges and corners by the same step; nothing else changes.
    * R2 L2 F2 B2 (`halfTurn`): exchange the U row and the D row of that face (`swapRows`) and the two E-slice
      places of that face.
    * R R' L L' (`quarter`): the four corners of the face move one step round it; a good corner arrives pointing at
      the face's edge place of its new layer, a corner that pointed at the face's edge place arrives good, a corner
      that pointed away keeps pointing away.  The four edges of the face move one step round it (layer, slot,
      layer, slot), each staying an E-slice piece or a U/D piece.

  Counts with U and D turns free.  R(q, h) is the set of states with a DR that uses exactly q quarter turns and h
  half turns of the side faces, in any order, with any U and D turns between.  It is defined directly, not by a
  search:  R(0, 0) = the U/D-orbit of the goal;  R(q, h) = the U/D-orbit of (the images of R(q−1, h) under R R' L L'
  ∪ the images of R(q, h−1) under R2 L2 F2 B2).  `GRID` holds R(q, h) for q + h ≤ 5 and R(1, 5).
    * `sig` (side turns) = the least q + h with the state in R(q, h); `q` = the fewest quarter turns among those.
    * `hbar` (4c4e: half turns to two bars) = the least h with the state in R(1, h).
    * `swaps` (4c4e) = fewest row exchanges to a bar in each ring, on the two rings up to rotation (`RD`, a BFS over
      ring-pair codes checked by `search.ruleHolds`);  `slot` (4c4e) = 0 if the two holes share an R/L face, 1 if
      they are diagonal, 2 if they share an F/B face.

  States are handled by a compact number i = (index of the twist number among the 2,187 valid ones) · 495 + (index
  of the mask among the 495 with four places), 0 … 1,082,564 (`xOf`, `cidOf`; theorem `compact_states`).
-/
import EOSwitch.Switch
import Std.Data.HashMap

set_option compiler.extract_closed false

namespace EOSwitch
namespace rg
open cube pieces sw

/-! ### Places of the rings -/

def r4 : List Nat := [0, 1, 2, 3]

/-- (x, z) of the 8 places of a ring, clockwise seen from above: B, BR, R, FR, F, FL, L, BL. -/
def RXZ : List (Int × Int) := [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

def edgeAt (v : Vec) : Nat := EDGES.idxOf v
def cornerAt (v : Vec) : Nat := CORNERS.idxOf v

/-- Ring place j (0 … 7) of the U layer, and of the D layer (x negated: clockwise seen from below). -/
def uPos (j : Nat) : Vec := [(RXZ[j]!).1, 1, (RXZ[j]!).2]
def dPos (j : Nat) : Vec := [-(RXZ[j]!).1, -1, (RXZ[j]!).2]

/-- Edge places and corner places of the two rings (indices into `EDGES`, `CORNERS`). -/
def UE : Array Nat := #[0, 2, 4, 6].map fun j => edgeAt (uPos j)
def UC : Array Nat := #[1, 3, 5, 7].map fun j => cornerAt (uPos j)
def DE : Array Nat := #[0, 2, 4, 6].map fun j => edgeAt (dPos j)
def DC : Array Nat := #[1, 3, 5, 7].map fun j => cornerAt (dPos j)
/-- The E-slice places FR FL BL BR. -/
def SLOTV : List Vec := [[1, 0, 1], [-1, 0, 1], [-1, 0, -1], [1, 0, -1]]
def SL : Array Nat := (SLOTV.map edgeAt).toArray

/-- The corner at ring place k (between edge k and edge k + 1): 0 good, 1 points clockwise (it pairs with edge
k + 1), 2 counter-clockwise (it pairs with edge k).  3 would be a bad corner that pairs with neither; theorem
`ring_places` checks that it never occurs. -/
def hook (E C : Array Nat) (co k : Nat) : Nat :=
  let c := C[k]!
  if !bad co c then 0
  else if udAxis co c == ZAX[E[(k + 1) % 4]!]! then 1
  else if udAxis co c == ZAX[E[k]!]! then 2 else 3

def hooksOf (E C : Array Nat) (co : Nat) : List Nat := r4.map (hook E C co)
def edgesOf (E : Array Nat) (m : Nat) : List Nat := r4.map fun k => b2n (holdsE m E[k]!)
def holesOf (m : Nat) : List Nat := r4.map fun k => b2n (!holdsE m SL[k]!)

/-- The picture: U edges, U corners, D edges, D corners, holes (4 entries each). -/
structure Pic where
  ue : List Nat
  uh : List Nat
  de : List Nat
  dh : List Nat
  ho : List Nat
  deriving DecidableEq, Repr, Inhabited

-- Per twist number and per mask, computed once.
def UHT : Array (List Nat) := (Array.range 6561).map (hooksOf UE UC)
def DHT : Array (List Nat) := (Array.range 6561).map (hooksOf DE DC)
def UET : Array (List Nat) := (Array.range 4096).map (edgesOf UE)
def DET : Array (List Nat) := (Array.range 4096).map (edgesOf DE)
def HOT : Array (List Nat) := (Array.range 4096).map holesOf

/-- The picture of state x = co · 4096 + m. -/
def picOf (x : Nat) : Pic := ⟨UET[x % 4096]!, UHT[x / 4096]!, DET[x % 4096]!, DHT[x / 4096]!, HOT[x % 4096]!⟩

/-! ### The turns on a picture -/

/-- A ring list turned by k places: new[j] = old[(j + k) % 4]. -/
def rotl (l : List Nat) (k : Nat) : List Nat := r4.map fun j => l[(j + k) % 4]!

/-- Exchange the row of the U ring at edge place p (corner p − 1, edge p, corner p) with the row of the D ring at
edge place q, keeping the clockwise order. -/
def swapRows (P : Pic) (p q : Nat) : Pic :=
  let p1 := (p + 3) % 4
  let q1 := (q + 3) % 4
  { P with
    ue := P.ue.set p P.de[q]!
    de := P.de.set q P.ue[p]!
    uh := (P.uh.set p1 P.dh[q1]!).set p P.dh[q]!
    dh := (P.dh.set q1 P.uh[p1]!).set q P.uh[p]! }

/-- The edge place of ring E on the side face (axis a, sign s): R (0, 1), L (0, −1), F (2, 1), B (2, −1). -/
def ringIdx (E : Array Nat) (a : Nat) (s : Int) : Nat := (r4.find? fun k => (EV E[k]!)[a]! == s).getD 4
/-- The two E-slice places of that face (indices into `SLOTV`). -/
def slotsOf (a : Nat) (s : Int) : List Nat := r4.filter fun j => (SLOTV[j]!)[a]! == s
/-- The E-slice place under (or over) corner place c: the one with its x and z. -/
def slotUnder (c : Nat) : Nat := SLOTV.idxOf [(CV c)[0]!, 0, (CV c)[2]!]

/-- A half turn of the side face (a, s). -/
def halfTurn (P : Pic) (a : Nat) (s : Int) : Pic :=
  let Q := swapRows P (ringIdx UE a s) (ringIdx DE a s)
  match slotsOf a s with
  | [i, j] => { Q with ho := (Q.ho.set i P.ho[j]!).set j P.ho[i]! }
  | _ => Q

/-- A quarter turn of the side face (a, s), R or L; `cw`: clockwise seen from that face.  Corners, in the order a
clockwise turn carries them: U corner after the face's edge place, U corner before it, D corner after, D corner
before; with each the hook value that points at the face's edge place (2 for the corner after it, 1 for the corner
before it).  Edges: U edge, slot under the U corner before, D edge, slot under the U corner after; an entry 1 means
an E-slice piece (for a slot: not a hole). -/
def quarter (P : Pic) (a : Nat) (s : Int) (cw : Bool) : Pic := Id.run do
  let p := ringIdx UE a s
  let q := ringIdx DE a s
  let p1 := (p + 3) % 4
  let q1 := (q + 3) % 4
  let cyc : List (Nat × Nat × Nat) := [(0, p, 2), (0, p1, 1), (1, q, 2), (1, q1, 1)]
  let ord := if cw then cyc else cyc.reverse
  let mut uh := P.uh
  let mut dh := P.dh
  for i in [0:4] do
    let src := ord[i]!
    let dst := ord[(i + 1) % 4]!
    let v := if src.1 == 0 then P.uh[src.2.1]! else P.dh[src.2.1]!
    let nv := if v == 0 then dst.2.2 else if v == src.2.2 then 0 else 3 - dst.2.2
    if dst.1 == 0 then uh := uh.set dst.2.1 nv else dh := dh.set dst.2.1 nv
  let ecyc : List (Nat × Nat) := [(0, p), (2, slotUnder UC[p1]!), (1, q), (2, slotUnder UC[p]!)]
  let eord := if cw then ecyc else ecyc.reverse
  let mut ue := P.ue
  let mut de := P.de
  let mut ho := P.ho
  for i in [0:4] do
    let src := eord[i]!
    let dst := eord[(i + 1) % 4]!
    let v := if src.1 == 0 then P.ue[src.2]! else if src.1 == 1 then P.de[src.2]! else 1 - P.ho[src.2]!
    if dst.1 == 0 then ue := ue.set dst.2 v
    else if dst.1 == 1 then de := de.set dst.2 v
    else ho := ho.set dst.2 (1 - v)
  return ⟨ue, uh, de, dh, ho⟩

/-- What turn `mv` (index in `NAMES`: face mv / 3 of U D R L F B; mv % 3 = 0 clockwise, 1 half, 2 counter-clockwise)
does to a picture.  U, U2, U' turn the U ring by 3, 2, 1 places; D, D2, D' the D ring by 3, 2, 1. -/
def expected (mv : Nat) (P : Pic) : Pic :=
  let f := mv / 3
  let k := mv % 3
  if f == 0 then { P with ue := rotl P.ue (3 - k), uh := rotl P.uh (3 - k) }
  else if f == 1 then { P with de := rotl P.de (3 - k), dh := rotl P.dh (3 - k) }
  else
    let ax := AX FACES[f]!
    if k == 1 then halfTurn P ax.1 ax.2 else quarter P ax.1 ax.2 (k == 0)

/-! ### Compact state numbers -/

/-- The valid twist numbers (twist sum ≡ 0 mod 3) and masks (four places), in increasing order. -/
def COL : Array Nat := (Array.range 6561).filter fun co => CO_OK[co]!
def ML : Array Nat := (Array.range 4096).filter fun m => M_OK[m]!
def NC : Nat := 2187 * 495

def invIdx (l : Array Nat) (n : Nat) : Array Nat := Id.run do
  let mut a := Array.replicate n 9999
  for i in [0:l.size] do a := a.set! l[i]! i
  return a
def COI : Array Nat := invIdx COL 6561
def MI : Array Nat := invIdx ML 4096

/-- The turns on the indices: `CCO[mv · 2187 + ci]`, `CM[mv · 495 + mi]`. -/
def CCO : Array Nat := Id.run do
  let mut a : Array Nat := #[]
  for mv in [0:18] do
    for ci in [0:2187] do
      a := a.push COI[(COT[mv]!)[COL[ci]!]!]!
  return a
def CM : Array Nat := Id.run do
  let mut a : Array Nat := #[]
  for mv in [0:18] do
    for mi in [0:495] do
      a := a.push MI[(MT[mv]!)[ML[mi]!]!]!
  return a

def xOf (i : Nat) : Nat := COL[i / 495]! * 4096 + ML[i % 495]!
def cidOf (x : Nat) : Nat := COI[x / 4096]! * 495 + MI[x % 4096]!
def cstep (i mv : Nat) : Nat := CCO[mv * 2187 + i / 495]! * 495 + CM[mv * 495 + i % 495]!
def GOALC : Nat := cidOf GOAL

@[noinline] def compactDist (d : ByteArray) : ByteArray := Id.run do
  let mut b := ByteArray.emptyWithCapacity NC
  for i in [0:NC] do b := b.push (d.get! (xOf i))
  return b
/-- The EO-kept distance to DR of compact state i (`dist` of Switch.lean). -/
def DCA : ByteArray := compactDist dist

/-- The compact numbers are the reached states: every one is reached, `cidOf` undoes `xOf`, `cstep` is `step`, and
`DCA` is `dist`. -/
def compactOk (_ : Unit) : Bool := Id.run do
  if COL.size != 2187 || ML.size != 495 then return false
  let st := step COT MT
  for i in [0:NC] do
    let x := xOf i
    if !search.reached dist x || cidOf x != i || DCA.get! i != dist.get! x then return false
    for mv in KEEP do
      if xOf (cstep i mv) != st x mv then return false
  return true

/-- `ring_turns`: on every state and every EO-keeping turn, the picture after the turn is `expected`. -/
def turnsOk (_ : Unit) : Bool := Id.run do
  let st := step COT MT
  for i in [0:NC] do
    let x := xOf i
    let P := picOf x
    for mv in KEEP do
      if picOf (st x mv) != expected mv P then return false
  return true

/-- The picture as one number below 16 · 81 · 16 · 81 · 16. -/
def picCode (P : Pic) : Nat :=
  let b := fun (l : List Nat) (base : Nat) => l.foldr (fun v acc => acc * base + v) 0
  b P.ue 2 + 16 * (b P.uh 3 + 81 * (b P.de 2 + 16 * (b P.dh 3 + 81 * b P.ho 2)))

/-- `ring_faithful`: no two states have the same picture; every entry is 0/1 (edges, holes) or 0/1/2 (corners). -/
def distinctOk (_ : Unit) : Bool := Id.run do
  let n := 16 * 81 * 16 * 81 * 16
  let mut seen := ByteArray.emptyWithCapacity n
  for _ in [0:n] do seen := seen.push 0
  for i in [0:NC] do
    let P := picOf (xOf i)
    if !((P.ue ++ P.de ++ P.ho).all (· < 2) && (P.uh ++ P.dh).all (· < 3)) then return false
    let c := picCode P
    if seen.get! c != 0 then return false
    seen := seen.set! c 1
  return true

/-! ### Reach sets with U and D turns free -/

def zeros (n : Nat) : ByteArray := Id.run do
  let mut b := ByteArray.emptyWithCapacity n
  for _ in [0:n] do b := b.push 0
  return b

/-- The 16 products U^a D^b, as lists of turn indices. -/
def UDW : List (List Nat) := [[], [0], [1], [2]].flatMap fun a => [[], [3], [4], [5]].map fun b => a ++ b

/-- `COORB[ci · 16 + j]`, `MORB[mi · 16 + j]`: the index after the j-th product of `UDW`. -/
def COORB : Array Nat := Id.run do
  let mut a : Array Nat := #[]
  for ci in [0:2187] do
    for w in UDW do
      a := a.push (w.foldl (fun c mv => CCO[mv * 2187 + c]!) ci)
  return a
def MORB : Array Nat := Id.run do
  let mut a : Array Nat := #[]
  for mi in [0:495] do
    for w in UDW do
      a := a.push (w.foldl (fun c mv => CM[mv * 495 + c]!) mi)
  return a

/-- The union of the images of the set s under the 16 products U^a D^b (a set is one byte per compact state). -/
def orbit (s : ByteArray) : ByteArray := Id.run do
  let mut o := zeros NC
  for i in [0:NC] do
    if s.get! i != 0 then
      let ci := i / 495
      let mi := i % 495
      for j in [0:16] do
        o := o.set! (COORB[ci * 16 + j]! * 495 + MORB[mi * 16 + j]!) 1
  return o

/-- o with the images of s under the given turns added. -/
def addImages (o s : ByteArray) (moves : List Nat) : ByteArray := Id.run do
  let mut o := o
  for i in [0:NC] do
    if s.get! i != 0 then
      for mv in moves do
        o := o.set! (cstep i mv) 1
  return o

/-- R R' L L', and R2 L2 F2 B2. -/
def QT : List Nat := [6, 8, 9, 11]
def HT : List Nat := [7, 10, 13, 16]

/-- The cells of the grid that are filled: q + h ≤ 5, and (1, 5). -/
def inGrid (q h : Nat) : Bool := q + h ≤ 5 || (q == 1 && h == 5)

/-- R(q, h) at index q · 6 + h, by the recursion of the header. -/
def reachGrid : Array ByteArray := Id.run do
  let mut g : Array ByteArray := Array.replicate 36 ByteArray.empty
  for q in [0:6] do
    for h in [0:6] do
      if inGrid q h then
        let mut s := zeros NC
        if q == 0 && h == 0 then s := s.set! GOALC 1
        if q > 0 then s := addImages s g[(q - 1) * 6 + h]! QT
        if h > 0 then s := addImages s g[q * 6 + (h - 1)]! HT
        g := g.set! (q * 6 + h) (orbit s)
  return g
def GRID : Array ByteArray := reachGrid

/-- State i is in R(q, h) (for a filled cell). -/
def inR (g : Array ByteArray) (q h i : Nat) : Bool := (g[q * 6 + h]!).get! i != 0

/-- (side turns, fewest quarter turns among the setups with that many side turns); (7, 7) if in no cell. -/
def sigQ (g : Array ByteArray) (i : Nat) : Nat × Nat := Id.run do
  let mut best := 7
  let mut bq := 7
  for q in [0:6] do
    for h in [0:6] do
      if q + h ≤ 5 && q + h < best && inR g q h i then
        best := q + h
        bq := q
  return (best, bq)

/-- The least h ≤ 5 with state i in R(1, h); 7 if none. -/
def hbarOf (g : Array ByteArray) (i : Nat) : Nat := ((List.range 6).find? fun h => inR g 1 h i).getD 7

/-! ### Ring codes and row swaps on the rings alone -/

/-- A ring as a number below 1296: Σ (edge k + 2 · corner k) · 6^k. -/
def codeOf (e h : List Nat) : Nat := r4.foldr (fun k acc => acc * 6 + (e[k]! + 2 * h[k]!)) 0
def decodeRing (c : Nat) : List Nat × List Nat :=
  (r4.map fun k => (c / 6 ^ k) % 6 % 2, r4.map fun k => (c / 6 ^ k) % 6 / 2)
/-- A ring up to rotation: the least code of its four rotations. -/
def canonOf (e h : List Nat) : Nat := (r4.map fun k => codeOf (rotl e k) (rotl h k)).foldl min 1296
def CANON : Array Nat := (Array.range 1296).map fun c => canonOf (decodeRing c).1 (decodeRing c).2

def UEC6 : Array Nat := (Array.range 4096).map fun m => codeOf (edgesOf UE m) [0, 0, 0, 0]
def DEC6 : Array Nat := (Array.range 4096).map fun m => codeOf (edgesOf DE m) [0, 0, 0, 0]
def UHC6 : Array Nat := (Array.range 6561).map fun co => codeOf [0, 0, 0, 0] (hooksOf UE UC co)
def DHC6 : Array Nat := (Array.range 6561).map fun co => codeOf [0, 0, 0, 0] (hooksOf DE DC co)

/-- The two rings of state x up to rotation, as (U code) · 1296 + (D code). -/
def pairCode (x : Nat) : Nat :=
  CANON[UEC6[x % 4096]! + UHC6[x / 4096]!]! * 1296 + CANON[DEC6[x % 4096]! + DHC6[x / 4096]!]!

/-- The rings of a pair code as a picture (no holes). -/
def ringsOfCode (pc : Nat) : Pic :=
  ⟨(decodeRing (pc / 1296)).1, (decodeRing (pc / 1296)).2, (decodeRing (pc % 1296)).1, (decodeRing (pc % 1296)).2, []⟩
def codeOfPic (P : Pic) : Nat := canonOf P.ue P.uh * 1296 + canonOf P.de P.dh

/-- Row swap number mv = p · 4 + q on a pair code. -/
def rstep (pc mv : Nat) : Nat := codeOfPic (swapRows (ringsOfCode pc) (mv / 4) (mv % 4))

/-- A bar: a bad edge place with the corner before it pointing clockwise and the corner after it pointing
counter-clockwise. -/
def hasBar (e h : List Nat) : Bool := r4.any fun k => e[k]! == 1 && h[(k + 3) % 4]! == 1 && h[k]! == 2

/-- The goal: a bar in each ring and nothing else. -/
def GOALP : Nat := codeOfPic ⟨[1, 0, 0, 0], [2, 0, 0, 1], [1, 0, 0, 0], [2, 0, 0, 1], []⟩

/-- Fewest row swaps to the goal, per pair code (255 = not reached). -/
def RD : ByteArray := search.bfs (1296 * 1296) GOALP (List.range 16) rstep
def swapsOf (pc : Nat) : Nat := (RD.get! pc).toNat

/-- Among the pair codes with an entry: the entry is 0 exactly when each ring has a bar. -/
def barsOk (_ : Unit) : Bool := Id.run do
  for pc in [0:1296 * 1296] do
    if search.reached RD pc then
      let P := ringsOfCode pc
      if (swapsOf pc == 0) != (hasBar P.ue P.uh && hasBar P.de P.dh) then return false
  return true
def reachedCount (_ : Unit) : Nat := Id.run do
  let mut n := 0
  for pc in [0:1296 * 1296] do
    if search.reached RD pc then n := n + 1
  return n

/-- 0 if the two holes share an R/L face, 2 if they share an F/B face, 1 if they are diagonal (3: not two holes). -/
def slotType (ho : List Nat) : Nat :=
  match r4.filter (fun j => ho[j]! == 1) with
  | [i, j] =>
    if (SLOTV[i]!)[0]! == (SLOTV[j]!)[0]! then 0 else if (SLOTV[i]!)[2]! == (SLOTV[j]!)[2]! then 2 else 1
  | _ => 3

/-- Pairs read off a ring, and off a picture. -/
def ringPairs (e h : List Nat) : Nat :=
  (r4.map fun k => if e[k]! == 1 then b2n (h[(k + 3) % 4]! == 1) + b2n (h[k]! == 2) else 0).sum
def picPairs (P : Pic) : Nat := ringPairs P.ue P.uh + ringPairs P.de P.dh

/-! ### The record of a state, and the table of groups -/

structure Rec where
  /-- bad corners -/
  c : Nat
  /-- 2 × bad U/D edges -/
  e : Nat
  pairs : Nat
  /-- bad U/D edges with a pair (`edgesPaired`) -/
  ep : Nat
  earm : Nat
  carm : Nat
  side : Nat
  jzp : Bool
  /-- side turns -/
  sig : Nat
  /-- fewest quarter turns among the setups with `sig` side turns -/
  q : Nat
  /-- 4c4e: half turns to two bars (7 otherwise) -/
  hbar : Nat
  /-- 4c4e: row swaps on the rings (7 otherwise) -/
  swaps : Nat
  /-- 4c4e: slot type (3 otherwise) -/
  slot : Nat
  deriving DecidableEq, Repr, Inhabited

def RWID : List Nat := [4, 3, 4, 3, 3, 4, 4, 1, 3, 3, 3, 3, 2]
def rfields (r : Rec) : List Nat :=
  [r.c, r.e / 2, r.pairs, r.ep, r.earm, r.carm, r.side, b2n r.jzp, r.sig, r.q, r.hbar, r.swaps, r.slot]
def rpack (r : Rec) : Nat := (List.zip (rfields r) RWID).foldr (fun (v, w) acc => acc * 2 ^ w + v) 0
def runpack (k : Nat) : Rec := Id.run do
  let mut k := k
  let mut out : Array Nat := #[]
  for w in RWID do
    out := out.push (k % 2 ^ w)
    k := k / 2 ^ w
  let g := fun i => out[i]!
  return { c := g 0, e := 2 * g 1, pairs := g 2, ep := g 3, earm := g 4, carm := g 5, side := g 6, jzp := g 7 == 1,
           sig := g 8, q := g 9, hbar := g 10, swaps := g 11, slot := g 12 }
def rfits (r : Rec) : Bool := (List.zip (rfields r) RWID).all fun (v, w) => v < 2 ^ w

def isDrm (c e : Nat) (r : Rec) : Bool := r.c == c && r.e == e
def is44 (r : Rec) : Bool := isDrm 4 4 r

def recOf (g : Array ByteArray) (rd : ByteArray) (i : Nat) : Rec :=
  let x := xOf i
  let f := feat (x / 4096) (x % 4096)
  let sq := sigQ g i
  let b := f.c == 4 && f.e == 4
  { c := f.c, e := f.e, pairs := f.pairs, ep := f.edgesPaired, earm := f.earm, carm := f.carm, side := f.side,
    jzp := f.jzp, sig := sq.1, q := sq.2,
    hbar := if b then hbarOf g i else 7,
    swaps := if b then min (rd.get! (pairCode x)).toNat 7 else 7,
    slot := if b then slotType HOT[x % 4096]! else 3 }

@[noinline] def buildRecs (g : Array ByteArray) (rd : ByteArray) : Array Nat := Id.run do
  let mut a : Array Nat := #[]
  for i in [0:NC] do a := a.push (rpack (recOf g rd i))
  return a
/-- The packed record of every compact state. -/
def RECS : Array Nat := buildRecs GRID RD

/-- Every state's record fits its fields and survives packing; every state has at most 5 side turns; a 4c4e state
has hbar, swaps ≤ 5 and slot type ≤ 2; and the pairs read off the rings are `feat`'s pairs. -/
def recsOk (_ : Unit) : Bool := Id.run do
  if RECS.size != NC then return false
  for i in [0:NC] do
    let r := recOf GRID RD i
    if !(rfits r && runpack RECS[i]! == r && r.sig ≤ 5 && r.q ≤ r.sig) then return false
    if is44 r && !(r.hbar ≤ 5 && r.swaps ≤ 5 && r.slot ≤ 2) then return false
    if picPairs (picOf (xOf i)) != r.pairs then return false
  return true

/-- Histogram length (distances 0 … 11). -/
def WD : Nat := 12

@[noinline] def buildGroups (recs : Array Nat) (dc : ByteArray) : Array (Rec × Array Nat) := Id.run do
  let mut idx : Std.HashMap Nat Nat := {}
  let mut keys : Array Nat := #[]
  let mut h : Array (Array Nat) := #[]
  for i in [0:NC] do
    let k := recs[i]!
    let v := (dc.get! i).toNat
    let mut j := 0
    match idx.get? k with
    | some j' => j := j'
    | none =>
      j := keys.size
      idx := idx.insert k j
      keys := keys.push k
      h := h.push (Array.replicate WD 0)
    h := h.modify j fun a => a.modify v (· + 1)
  return (Array.range keys.size).map fun j => (runpack keys[j]!, h[j]!)
/-- Each record that occurs, with its histogram of distances to DR. -/
def GROUPS : Array (Rec × Array Nat) := buildGroups RECS DCA

@[noinline] def buildRP (recs : Array Nat) (dc : ByteArray) : Array (Nat × Array Nat) := Id.run do
  let mut idx : Std.HashMap Nat Nat := {}
  let mut keys : Array Nat := #[]
  let mut h : Array (Array Nat) := #[]
  for i in [0:NC] do
    if is44 (runpack recs[i]!) then
      let k := pairCode (xOf i)
      let v := (dc.get! i).toNat
      let mut j := 0
      match idx.get? k with
      | some j' => j := j'
      | none =>
        j := keys.size
        idx := idx.insert k j
        keys := keys.push k
        h := h.push (Array.replicate WD 0)
      h := h.modify j fun a => a.modify v (· + 1)
  return (Array.range keys.size).map fun j => (keys[j]!, h[j]!)
/-- Each ring pair (pair code) that occurs among the 4c4e states, with the histogram of their distances to DR. -/
def RPT : Array (Nat × Array Nat) := buildRP RECS DCA

/-! ### Readings -/

/-- [states, DR ≤ 5, ≤ 6, ≤ 7] from a histogram. -/
def hcell (a : Array Nat) : List Nat :=
  let upto := fun k => ((List.range (k + 1)).map fun v => a[v]!).sum
  [upto 11, upto 5, upto 6, upto 7]

def rsum (p : Rec → Bool) : Array Nat := Id.run do
  let mut acc := Array.replicate WD 0
  for g in GROUPS do
    if p g.1 then
      for i in [0:WD] do acc := acc.modify i (· + (g.2)[i]!)
  return acc
/-- The cell of the states whose record satisfies p. -/
def rcell (p : Rec → Bool) : List Nat := hcell (rsum p)

/-- Every state with at most 2 side turns has a DR in at most 6. -/
def certainOk (_ : Unit) : Bool := Id.run do
  for i in [0:NC] do
    if (runpack RECS[i]!).sig ≤ 2 && (DCA.get! i).toNat > 6 then return false
  return true

/-- Every 4c4e state: half turns to two bars = max(row swaps of its ring pair, slot type). -/
def hbarOk (_ : Unit) : Bool := Id.run do
  for i in [0:NC] do
    let r := runpack RECS[i]!
    if is44 r && r.hbar != max r.swaps r.slot then return false
  return true

/-- The half-turn groups of the tables: ≤ 1, 2, 3, ≥ 4; and ≤ 2, 3, ≥ 4. -/
def hGroup4 (g : Nat) (r : Rec) : Bool :=
  if g == 0 then r.hbar ≤ 1 else if g == 1 then r.hbar == 2 else if g == 2 then r.hbar == 3 else r.hbar ≥ 4 && r.hbar ≤ 5
def hGroup3 (g : Nat) (r : Rec) : Bool :=
  if g == 0 then r.hbar ≤ 2 else if g == 1 then r.hbar == 3 else r.hbar ≥ 4 && r.hbar ≤ 5
/-- The groups of the paired-edge card for 4c4e: both bad edges paired; one paired and edge ARM 1; the rest. -/
def card44 (ci : Nat) (r : Rec) : Bool :=
  if ci == 0 then r.ep == 2 else if ci == 1 then r.ep == 1 && r.earm == 1 else r.ep == 0 || (r.ep == 1 && r.earm != 1)

/-- The rows whose state count (entry number `pos`) is not 0. -/
def occur (pos : Nat) (rows : List (List Nat)) : List (List Nat) := rows.filter fun r => r[pos]! != 0

def DRMS : List (Nat × Nat) :=
  [(4, 4), (4, 2), (3, 2), (7, 8), (8, 8), (2, 2), (4, 6), (3, 4), (3, 6), (5, 4), (5, 6), (6, 6)]

def sigmaRows (c e : Nat) : List (List Nat) :=
  occur 1 ((List.range 6).map fun s => [s] ++ rcell (fun r => isDrm c e r && r.sig == s))
def profileRows (c e : Nat) : List (List Nat) :=
  occur 2 ((List.range 6).flatMap fun s => (List.range (s + 1)).map fun q =>
    [q, s - q] ++ rcell (fun r => isDrm c e r && r.sig == s && r.q == q))

def anyR (_ : Rec) : Bool := true
/-- The cards of the page, as in the research's `xrings.CARD` (first match wins; the last row takes the rest). -/
def CARDS : List (Nat × Nat × List (Rec → Bool)) :=
  [(4, 4, [fun r => r.ep == 2, fun r => r.ep == 1 && r.earm == 1, anyR]),
   (4, 2, [fun r => 2 * r.pairs + r.side ≥ 3, fun r => 2 * r.pairs + r.side == 2, anyR]),
   (3, 2, [anyR]),
   (7, 8, [fun r => r.pairs ≥ 5, fun r => r.pairs == 4, anyR]),
   (8, 8, [fun r => [0, 4, 8].contains r.carm, anyR]),
   (2, 2, [fun r => r.ep ≥ 1, fun r => r.jzp, anyR]),
   (4, 6, [fun r => r.jzp, fun r => r.pairs == 4, anyR]),
   (3, 4, [fun r => r.pairs == 2, anyR]),
   (3, 6, [anyR]),
   (5, 4, [fun r => r.pairs == 3, anyR]),
   (5, 6, [fun r => r.pairs == 4, anyR]),
   (6, 6, [fun r => r.jzp || r.pairs ≥ 5, anyR])]

/-- A short setup: at most 3 side turns with 1 quarter turn (4c4e) or 2 (the other DRMs). -/
def isShort (c e : Nat) (r : Rec) : Bool := r.sig ≤ 3 && r.q == (if c == 4 && e == 4 then 1 else 2)

def crossGo (c e gi : Nat) (rs : List (Rec → Bool)) (taken : Rec → Bool) : List (List Nat) :=
  match rs with
  | [] => []
  | p :: t =>
    let g := fun r : Rec => isDrm c e r && !taken r && p r
    [[gi, 0] ++ rcell (fun r => g r && isShort c e r), [gi, 1] ++ rcell (fun r => g r && !isShort c e r)]
      ++ crossGo c e (gi + 1) t (fun r => taken r || p r)
/-- [card group, 0 short / 1 not] ++ cell, the groups that occur. -/
def crossRows (c e : Nat) (rows : List (Rec → Bool)) : List (List Nat) :=
  occur 2 (crossGo c e 0 rows (fun _ => false))

/-! ### Ring pairs: pair changes, the 3-pair rule, the patterns with at most 2 swaps -/

/-- Over the ring pairs of 4c4e and the 16 row swaps: pairs after − pairs before. -/
def pairDeltas (_ : Unit) : List Int := Id.run do
  let mut out : List Int := []
  for g in RPT do
    let P := ringsOfCode g.1
    let n := picPairs P
    for mv in [0:16] do
      out := (Int.ofNat (picPairs (swapRows P (mv / 4) (mv % 4))) - Int.ofNat n) :: out
  return out

/-- Every ring pair of 4c4e: 2 · swaps + pairs ≥ 4 (so swaps ≥ ⌈(4 − pairs)/2⌉), and 4 pairs give at most 1 swap. -/
def pairBoundOk (_ : Unit) : Bool :=
  RPT.all fun g =>
    let n := picPairs (ringsOfCode g.1)
    2 * swapsOf g.1 + n ≥ 4 && (n != 4 || swapsOf g.1 ≤ 1)

/-- [pairs, swaps, number of ring pairs], the combinations that occur. -/
def pairsSwapsClasses (_ : Unit) : List (List Nat) :=
  occur 2 ((List.range 5).flatMap fun p => (List.range 6).map fun s =>
    [p, s, (RPT.filter fun g => picPairs (ringsOfCode g.1) == p && swapsOf g.1 == s).size])

/-- For a ring pair with 3 pairs: (the unpaired corner is in the layer of the edge that lacks a corner, a bad piece
in the two places behind it, both bad edges in one layer and opposite each other), each 0 or 1.  "Behind" a corner
pointing clockwise at ring place i: edge place i and corner i − 1; counter-clockwise: edge i + 1 and corner i + 1. -/
def three (P : Pic) : Nat × Nat × Nat := Id.run do
  let rings := [(P.ue, P.uh), (P.de, P.dh)]
  let mut lone : Nat × Nat × Nat := (0, 0, 0)
  let mut lack := 9
  for ri in [0:2] do
    let e := (rings[ri]!).1
    let h := (rings[ri]!).2
    for i in [0:4] do
      if h[i]! == 1 && e[(i + 1) % 4]! == 0 then lone := (ri, i, 1)
      if h[i]! == 2 && e[i]! == 0 then lone := (ri, i, 2)
    for a in [0:4] do
      if e[a]! == 1 && !(h[(a + 3) % 4]! == 1 && h[a]! == 2) then lack := ri
  let e := (rings[lone.1]!).1
  let h := (rings[lone.1]!).2
  let i := lone.2.1
  let blocked :=
    if lone.2.2 == 1 then e[i]! == 1 || h[(i + 3) % 4]! != 0 else e[(i + 1) % 4]! == 1 || h[(i + 1) % 4]! != 0
  let nu := P.ue.sum
  let nd := P.de.sum
  let ee := if nu == 2 then P.ue else P.de
  let opp := !(nu == 1 && nd == 1) && !(r4.any fun a => ee[a]! == 1 && ee[(a + 1) % 4]! == 1)
  return (b2n (lack == lone.1), b2n blocked, b2n opp)

/-- Every ring pair of 4c4e with 3 pairs: swaps = 1 + the three entries of `three`. -/
def threeOk (_ : Unit) : Bool :=
  RPT.all fun g =>
    let P := ringsOfCode g.1
    picPairs P != 3 || (let t := three P; swapsOf g.1 == 1 + t.1 + t.2.1 + t.2.2)

/-- [same layer, blocked, opposite, 1 + their sum, states, states with DR ≤ 6] over the 4c4e states with 3 pairs,
the combinations that occur. -/
def threeRows (_ : Unit) : List (List Nat) :=
  occur 4 ((List.range 8).map fun k =>
    let t := (k / 4, k / 2 % 2, k % 2)
    let cells := (RPT.toList.filter fun g =>
      let P := ringsOfCode g.1
      picPairs P == 3 && three P == t).map fun g => hcell g.2
    [t.1, t.2.1, t.2.2, 1 + t.1 + t.2.1 + t.2.2, (cells.map fun c => c[0]!).sum, (cells.map fun c => c[2]!).sum])

def swapDir (h : Nat) : Nat := if h == 1 then 2 else if h == 2 then 1 else h
/-- A ring code seen in a mirror: the order reversed, clockwise and counter-clockwise exchanged. -/
def mirrorCode (c : Nat) : Nat :=
  let e := (decodeRing c).1
  let h := (decodeRing c).2
  canonOf (r4.map fun k => e[(4 - k) % 4]!) (r4.map fun k => swapDir h[3 - k]!)
/-- A ring pair up to exchanging the layers and mirroring: the least of its four pair codes. -/
def symKey (pc : Nat) : Nat :=
  let u := pc / 1296
  let d := pc % 1296
  let mu := mirrorCode u
  let md := mirrorCode d
  min (min (u * 1296 + d) (d * 1296 + u)) (min (mu * 1296 + md) (md * 1296 + mu))

/-- A ring from its string: clockwise from a corner, corner, edge, corner, edge, …; '>' a corner pointing
clockwise, '<' counter-clockwise, 'o' a good corner, 'E' a bad edge place, '-' a good one.  Character 2k is the
corner before edge k (corner k − 1), character 2k + 1 is edge k. -/
def ringOfString (s : String) : List Nat × List Nat :=
  let cs := s.toList
  (r4.map fun k => b2n (cs[2 * k + 1]! == 'E'),
   r4.map fun j => let c := cs[(2 * (j + 1)) % 8]!; if c == '>' then 1 else if c == '<' then 2 else 0)
def validString (s : String) : Bool :=
  let cs := s.toList
  cs.length == 8 && r4.all fun k => ['>', '<', 'o'].contains cs[2 * k]! && ['E', '-'].contains cs[2 * k + 1]!
def codeOfStrings (a b : String) : Nat :=
  canonOf (ringOfString a).1 (ringOfString a).2 * 1296 + canonOf (ringOfString b).1 (ringOfString b).2

def byKey (l : List (Nat × List Nat)) : List (Nat × List Nat) := l.mergeSort fun a b => decide (a.1 ≤ b.1)

/-- The ring pairs of 4c4e with at most 2 row swaps, up to exchanging the layers and mirroring:
(key, [swaps, pairs, states, states with DR ≤ 6]), by key.  All 780 ring pairs are gathered by key first; if two
ring pairs with one key disagreed on swaps or pairs, the entry would get swaps 99 and be kept. -/
def patternsLean (_ : Unit) : List (Nat × List Nat) := Id.run do
  let mut m : Std.HashMap Nat (List Nat) := {}
  for g in RPT do
    let sw := swapsOf g.1
    let k := symKey g.1
    let n := picPairs (ringsOfCode g.1)
    let c := hcell g.2
    let old := m.getD k [sw, n, 0, 0]
    let s' := if old[0]! == sw && old[1]! == n then sw else 99
    m := m.insert k [s', n, old[2]! + c[0]!, old[3]! + c[2]!]
  return byKey (m.toList.filter fun p => (p.2)[0]! ≤ 2 || (p.2)[0]! == 99)
/-- The same list from the strings of the research. -/
def patternsOf (l : List (String × String × List Nat)) : List (Nat × List Nat) :=
  byKey (l.map fun p => (symKey (codeOfStrings p.1 p.2.1), p.2.2))

end rg
end EOSwitch
