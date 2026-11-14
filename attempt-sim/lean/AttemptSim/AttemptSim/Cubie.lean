/-
  AttemptSim.Cubie — the simulator's cube model in Lean, read from the simulator's own export, next to the sticker
  model of `Cube.lean`.

  The simulator (research/attemptsim, vendor/cubie.rs) keeps a cube as pieces:
      cp[i], ct[i]   the corner piece at place i (named by its home place) and its twist
      ep[i], ef[i]   the edge piece at place i and its flip
  and applies a face turn through four small tables (`Map`): the piece at place i goes to place cd[i] (ed[i]), its
  twist grows by ca[i] mod 3 (its flip changes when ea[i] = 1).  `data/model.txt` is the simulator's dump of the 18
  tables it uses, of its 24 whole-cube rotations, of the nine views (rotation + how moves are renamed) and of the
  place numbering of its DR tables.  `turn`, `thenC`, `inverseC`, `conjC`, `coords` below are vendor/cubie.rs line
  for line.

  The other side is the sticker cube: places and conventions as in is-dr-xs-worth-it's coords.py, which is where the
  simulator's tables come from:
      corner places / edge places   the cubie positions in sorted order (`pieces.CORNERS`, `pieces.EDGES`)
      CF[c]   the three sticker places of corner place c: the U/D one first, then clockwise seen from outside
      EF[k]   the two sticker places of edge place k: the U/D one first if there is one, else the F/B one
      twist   where in CF the piece's U/D sticker sits;  flip: where in EF the piece's first sticker sits
  `toCubie` reads (cp, ct, ep, ef) off a sticker state, `asMap` turns a 54-sticker permutation into a `Map`.
  The theorems (ModelThm.lean) say the simulator's tables are the ones the sticker cube gives.
-/
import AttemptSim.Manifest
import AttemptSim.Pieces

namespace AttemptSim
namespace cubie
open cube pieces

/-! ### Text -/

/-- The natural numbers in a text, in order (every maximal run of digits). -/
def nats (s : String) : Array Nat := Id.run do
  let b := s.toUTF8
  let mut out : Array Nat := #[]
  let mut cur := 0
  let mut inNum := false
  for i in [0:b.size] do
    let c := (b.get! i).toNat
    if 48 ≤ c && c ≤ 57 then
      cur := cur * 10 + (c - 48)
      inNum := true
    else if inNum then
      out := out.push cur
      cur := 0
      inNum := false
  if inNum then out := out.push cur
  return out

def lines (s : String) : List String := (s.splitOn "\n").filter (· != "")

/-! ### The simulator's model -/

structure Map where
  cd : Array Nat
  ca : Array Nat
  ed : Array Nat
  ea : Array Nat
  deriving BEq, Inhabited, Repr

structure Cubie where
  cp : Array Nat
  ct : Array Nat
  ep : Array Nat
  ef : Array Nat
  deriving BEq, Inhabited, Repr

def SOLVEDC : Cubie := ⟨Array.range 8, Array.replicate 8 0, Array.range 12, Array.replicate 12 0⟩

/-- `Model::turn` of cubie.rs. -/
def turn (mp : Map) (s : Cubie) : Cubie := Id.run do
  let mut cp := s.cp
  let mut ct := s.ct
  let mut ep := s.ep
  let mut ef := s.ef
  for i in [0:8] do
    let j := mp.cd[i]!
    cp := cp.set! j s.cp[i]!
    ct := ct.set! j ((s.ct[i]! + mp.ca[i]!) % 3)
  for i in [0:12] do
    let j := mp.ed[i]!
    ep := ep.set! j s.ep[i]!
    ef := ef.set! j ((s.ef[i]! + mp.ea[i]!) % 2)
  return ⟨cp, ct, ep, ef⟩

/-- `Cubie::then` of cubie.rs: a, then b. -/
def thenC (a b : Cubie) : Cubie :=
  ⟨(Array.range 8).map fun i => a.cp[b.cp[i]!]!,
   (Array.range 8).map fun i => (a.ct[b.cp[i]!]! + b.ct[i]!) % 3,
   (Array.range 12).map fun i => a.ep[b.ep[i]!]!,
   (Array.range 12).map fun i => (a.ef[b.ep[i]!]! + b.ef[i]!) % 2⟩

/-- `Cubie::inverse` of cubie.rs. -/
def inverseC (s : Cubie) : Cubie := Id.run do
  let mut cp := s.cp
  let mut ct := s.ct
  let mut ep := s.ep
  let mut ef := s.ef
  for i in [0:8] do
    let p := s.cp[i]!
    cp := cp.set! p i
    ct := ct.set! p ((3 - s.ct[i]!) % 3)
  for i in [0:12] do
    let p := s.ep[i]!
    ep := ep.set! p i
    ef := ef.set! p s.ef[i]!
  return ⟨cp, ct, ep, ef⟩

/-- `Model::conj` of cubie.rs: the state seen after turning the whole cube by the rotation with map `mp`. -/
def conjC (mp : Map) (s : Cubie) : Cubie := Id.run do
  let mut cp := s.cp
  let mut ct := s.ct
  let mut ep := s.ep
  let mut ef := s.ef
  for i in [0:8] do
    let j := mp.cd[i]!
    cp := cp.set! j mp.cd[s.cp[i]!]!
    ct := ct.set! j ((s.ct[i]! + mp.ca[i]! + 3 - mp.ca[s.cp[i]!]!) % 3)
  for i in [0:12] do
    let j := mp.ed[i]!
    ep := ep.set! j mp.ed[s.ep[i]!]!
    ef := ef.set! j ((s.ef[i]! + mp.ea[i]! + mp.ea[s.ep[i]!]!) % 2)
  return ⟨cp, ct, ep, ef⟩

/-- Everything in data/model.txt. -/
structure Model where
  moves : Array Map
  /-- (EO axis y, rotation index, own move of each view move) for the three EO views -/
  eoViews : Array (Nat × Nat × Array Nat)
  /-- (EO axis y, DR axis x, rotation index, own move of each view move) for the six DR views -/
  drViews : Array (Nat × Nat × Nat × Array Nat)
  rots : Array Map
  rotAxes : Array (Array Nat)
  rotFaces : Array (Array Nat)
  drC : Array Nat
  drE : Array Nat
  drS : Array Nat
  drMoves : Array Nat
  eoKeep : Array Nat
  solvedSl : Nat
  deriving Inhabited

def parseMap (parts : List String) : Map :=
  ⟨nats (parts.getD 0 ""), nats (parts.getD 1 ""), nats (parts.getD 2 ""), nats (parts.getD 3 "")⟩

def parseModel (txt : String) : Model := Id.run do
  let mut m : Model := default
  let mut sec := ""
  for l in lines txt do
    if l.startsWith "#" then continue
    let w := (l.splitOn " ").headD ""
    if ["moves", "views", "rotations", "drmap", "drmoves", "eokeep"].contains w then
      sec := w
      continue
    if w == "solved_sl" then
      m := { m with solvedSl := (nats l).getD 0 0 }
      continue
    let parts := l.splitOn " | "
    if sec == "moves" then m := { m with moves := m.moves.push (parseMap parts) }
    else if sec == "views" then
      let h := nats (parts.getD 0 "")
      let u := nats (parts.getD 1 "")
      if w == "eo" then m := { m with eoViews := m.eoViews.push (h.getD 0 9, h.getD 1 99, u) }
      else m := { m with drViews := m.drViews.push (h.getD 0 9, h.getD 1 9, h.getD 2 99, u) }
    else if sec == "rotations" then
      m := { m with rots := m.rots.push (parseMap parts), rotAxes := m.rotAxes.push (nats (parts.getD 4 "")),
                    rotFaces := m.rotFaces.push (nats (parts.getD 5 "")) }
    else if sec == "drmap" then
      if m.drC.isEmpty then m := { m with drC := nats l }
      else if m.drE.isEmpty then m := { m with drE := nats l }
      else m := { m with drS := nats l }
    else if sec == "drmoves" then m := { m with drMoves := nats l }
    else if sec == "eokeep" then m := { m with eoKeep := nats l }
  return m

/-- The simulator's model: data/model.txt, embedded at build time. -/
def MODEL : Model := parseModel (include_str "../data/model.txt")

/-- Apply a sequence of moves (numbers 0 … 17) with the simulator's tables. -/
def applyC (s : Cubie) (seq : List Nat) : Cubie := seq.foldl (fun a mv => turn MODEL.moves[mv]! a) s

/-! ### Coordinates (`Model::coords` of cubie.rs, `coords` of coords.py) -/

/-- The edge whose home is place p is an E-slice piece (the places of drmap's third row). -/
def ePiece (p : Nat) : Bool := MODEL.drS.contains p

/-- Rank of each 12-bit mask with four bits among the 495, in the order of nested loops a < b < c < d
(itertools.combinations); 65535 for other masks. -/
def COMB : Array Nat := Id.run do
  let mut t := Array.replicate 4096 65535
  let mut r := 0
  for a in [0:12] do
    for b in [a+1:12] do
      for c in [b+1:12] do
        for d in [c+1:12] do
          t := t.set! (2^a + 2^b + 2^c + 2^d) r
          r := r + 1
  return t
/-- The mask of each rank. -/
def MASKS : Array Nat := Id.run do
  let mut t := Array.replicate 495 0
  for mask in [0:4096] do
    if COMB[mask]! != 65535 then t := t.set! COMB[mask]! mask
  return t

def coOf (s : Cubie) : Nat := (List.range 7).foldl (fun acc i => acc + s.ct[i]! * 3 ^ i) 0
def eoOf (s : Cubie) : Nat := (List.range 11).foldl (fun acc i => acc + s.ef[i]! * 2 ^ i) 0
def slMask (s : Cubie) : Nat := (List.range 12).foldl (fun acc i => if ePiece s.ep[i]! then acc + 2 ^ i else acc) 0
def slOf (s : Cubie) : Nat := COMB[slMask s]!

/-- The states the simulator builds its coordinate tables from (ctx.rs). -/
def repCo (co : Nat) : Cubie :=
  let t := (Array.range 7).map fun i => (co / 3 ^ i) % 3
  let sum := t.foldl (· + ·) 0
  { SOLVEDC with ct := t.push ((3 - sum % 3) % 3) }
def repEo (eo : Nat) : Cubie :=
  let f := (Array.range 11).map fun i => (eo / 2 ^ i) % 2
  let par := f.foldl (· + ·) 0 % 2
  { SOLVEDC with ef := f.push par }
def repSl (sl : Nat) : Cubie := Id.run do
  let mask := MASKS[sl]!
  let epieces := (List.range 12).filter ePiece
  let others := (List.range 12).filter (fun p => !ePiece p)
  let mut ep := Array.replicate 12 0
  let mut a := 0
  let mut b := 0
  for i in [0:12] do
    if (mask >>> i) % 2 == 1 then
      ep := ep.set! i epieces[a]!
      a := a + 1
    else
      ep := ep.set! i others[b]!
      b := b + 1
  return { SOLVEDC with ep := ep }

/-! ### The sticker side (coords.py and export_cubie.py of is-dr-xs-worth-it) -/

def det (a b c : Vec) : Int := dot a (cross b c)

/-- Sticker places of the corner at position p: the U/D one first, then clockwise seen from outside. -/
def cornerFacelets (p : Vec) : List Nat :=
  let pl := CUBIES p
  let ud := (pl.find? fun i => nax i == 1).getD 54
  let rest := pl.filter (· != ud)
  let a := rest[0]!
  let b := rest[1]!
  if det cube.ST[ud]!.2 cube.ST[a]!.2 cube.ST[b]!.2 > 0 then [ud, b, a] else [ud, a, b]

/-- Sticker places of the edge at position p: the U/D one first if it has one, else the F/B one. -/
def edgeFacelets (p : Vec) : List Nat :=
  let pl := CUBIES p
  let pri := match pl.find? (fun i => nax i == 1) with
    | some i => i
    | none => (pl.find? fun i => nax i == 2).getD 54
  [pri, (pl.find? (· != pri)).getD 54]

def CF : Array (List Nat) := CORNERS.toArray.map cornerFacelets
def EF : Array (List Nat) := EDGES.toArray.map edgeFacelets

/-- (cp, ct, ep, ef) of a sticker state (`cubie` of export_cubie.py). -/
def toCubie (s : State) : Cubie := Id.run do
  let mut cp := Array.replicate 8 0
  let mut ct := Array.replicate 8 0
  let mut ep := Array.replicate 12 0
  let mut ef := Array.replicate 12 0
  for i in [0:8] do
    let home := CF[i]!.map fun x => s[x]!
    let p := cornerOf home[0]!
    cp := cp.set! i p
    ct := ct.set! i (home.idxOf (CF[p]!)[0]!)
  for i in [0:12] do
    let home := EF[i]!.map fun x => s[x]!
    let p := edgeOf home[0]!
    ep := ep.set! i p
    ef := ef.set! i (home.idxOf (EF[p]!)[0]!)
  return ⟨cp, ct, ep, ef⟩

/-- A 54-sticker permutation (place i goes to place P[i]) as a `Map` (`as_map` of export_cubie.py). -/
def asMap (P : State) : Map := Id.run do
  let mut cd := #[]
  let mut ca := #[]
  let mut ed := #[]
  let mut ea := #[]
  for i in [0:8] do
    let img := CF[i]!.map fun x => P[x]!
    let j := cornerOf img[0]!
    cd := cd.push j
    ca := ca.push (CF[j]!.idxOf img[0]!)
  for i in [0:12] do
    let img := EF[i]!.map fun x => P[x]!
    let j := edgeOf img[0]!
    ed := ed.push j
    ea := ea.push (EF[j]!.idxOf img[0]!)
  return ⟨cd, ca, ed, ea⟩

/-- The map carries each corner's sticker list onto the list of its destination, shifted cyclically, and each
edge's pair onto the destination's pair (so twists and flips are well defined). -/
def mapSound (P : State) : Bool :=
  let mp := asMap P
  ((List.range 8).all fun i => (List.range 3).all fun k =>
    P[(CF[i]!)[k]!]! == (CF[mp.cd[i]!]!)[(k + mp.ca[i]!) % 3]!) &&
  ((List.range 12).all fun i => (List.range 2).all fun k =>
    P[(EF[i]!)[k]!]! == (EF[mp.ed[i]!]!)[(k + mp.ea[i]!) % 2]!)

/-! ### Sticker states: composition, inverse, whole-cube rotations -/

/-- s, then t (both as states reached from solved): the state after doing the moves of s and then those of t. -/
def composeS (s t : State) : State := (Array.range 54).map fun i => s[t[i]!]!
def inverseS (s : State) : State := Id.run do
  let mut r := Array.replicate 54 0
  for i in [0:54] do r := r.set! s[i]! i
  return r

/-- Turning the whole cube a quarter about axis a (all three layers). -/
def wholeTurn (a : Nat) : State := layer_move a [-1, 0, 1] 1
/-- P, then Q, as permutations of places. -/
def permThen (P Q : State) : State := (Array.range 54).map fun i => Q[P[i]!]!

/-- The 24 whole-cube rotations: everything reached from the identity by quarter turns of the whole cube. -/
def ROTS : List State := Id.run do
  let gens := [wholeTurn 0, wholeTurn 1, wholeTurn 2]
  let mut seen : List State := [SOLVED]
  let mut todo : List State := [SOLVED]
  for _ in [0:30] do
    let mut next : List State := []
    for P in todo do
      for g in gens do
        let Q := permThen P g
        if !(seen.contains Q) && !(next.contains Q) then next := next ++ [Q]
    seen := seen ++ next
    todo := next
  return seen

/-- The state seen after turning the whole cube by rotation R (stickers and colours): t[R[i]] = R[s[i]]. -/
def conjS (s R : State) : State := Id.run do
  let mut t := Array.replicate 54 0
  for i in [0:54] do t := t.set! R[i]! R[s[i]!]!
  return t

/-- The centre sticker of face f (U D R L F B = 0 … 5). -/
def centre (f : Nat) : Nat :=
  let (a, sg) := AX FACES[f]!
  ((List.range 54).find? fun k =>
    let (p, n) := cube.ST[k]!
    (p.map (·.natAbs)).foldl (· + ·) 0 == 1 && n[a]! == sg).getD 54
/-- Where rotation R sends each axis (0 R/L, 1 U/D, 2 F/B) and each face. -/
def axesOf (R : State) : Array Nat := (Array.range 3).map fun a => nax R[centre ([2, 0, 4][a]!)]!
def facesOf (R : State) : Array Nat := (Array.range 6).map fun f => FACES.idxOf FACE_OF[R[centre f]!]!

/-- The geometric rotation whose `Map` is row r of the simulator's rotation table (#[] if there is none). -/
def rotOf (r : Nat) : State := (ROTS.find? fun R => asMap R == MODEL.rots[r]!).getD #[]

end cubie
end AttemptSim
