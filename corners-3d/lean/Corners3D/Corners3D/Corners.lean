/-
  Corners3D.Corners — the corners with DBL held fixed, turned by R, U and F only, as coordinates read off the
  sticker model; what each corner shows (its *kind*); the colour pictures; and the distance tables.

  Corner places c = 0 … 7 are `pieces.CORNERS` (sorted cubie positions), so place 0 is DBL (-1, -1, -1), which no
  R, U or F turn moves, and place 7 is UFR.  A state is
    p[c] = the home place of the piece at place c   (p[0] = 0),
    t[c] = its twist, `pieces.twistAt` (0 = U/D colour on the U/D face; t[0] = 0).
  Coordinates: x = P · 729 + T, with P the Lehmer index of p[1 … 7] (0 … 5039) and T = Σ_{c=1…6} t[c]·3^(c-1)
  (t[7] follows, the twists adding up to 0 mod 3).  N = 5040 · 729 = 3,674,160 states.

  Turns are numbered m = 0 … 8 for R R2 R' U U2 U' F F2 F'; m / 3 is the axis (0 = R/L, 1 = U/D, 2 = F/B) and
  m % 3 = 1 is a half turn.

  The goal, HTR: the 24 states reached from solved with R2, U2, F2.
-/
import Corners3D.Pieces
import Corners3D.Search
namespace Corners3D
namespace corners
open cube pieces

def NCP : Nat := 5040
def NCO : Nat := 729
def N : Nat := NCP * NCO

/-- The nine turns R R2 R' U U2 U' F F2 F' as indices into `cube.NAMES` (U U2 U' D … R … L … F … B …). -/
def TURN : Array Nat := #[6, 7, 8, 0, 1, 2, 12, 13, 14]
def TURN_NAMES : List String := ["R", "R2", "R'", "U", "U2", "U'", "F", "F2", "F'"]
/-- The axis of turn m: 0 = R/L, 1 = U/D, 2 = F/B. -/
def turnAxis (m : Nat) : Nat := m / 3
def isQuarter (m : Nat) : Bool := m % 3 != 1
/-- The turn that undoes turn m. -/
def invTurn (m : Nat) : Nat := m - m % 3 + (2 - m % 3)
/-- Where turn m carries the corner at place c, and by how much it turns it (from `Pieces.lean`). -/
def dest (m c : Nat) : Nat := CDEST[TURN[m]!]![c]!
def delta (m c : Nat) : Nat := CDELTA[TURN[m]!]![c]!
/-- `dest` as one flat table (9 × 8), and the powers of 6, for the loops that run over every state. -/
def DEST : Array Nat := (Array.range 72).map fun i => dest (i / 8) (i % 8)
def POW6 : Array Nat := (Array.range 8).map fun c => 6 ^ c

/-! ### Coordinates -/

/-- Lehmer index of p[1 … 7] (a permutation of 1 … 7). -/
def encodeP (p : Array Nat) : Nat := Id.run do
  let mut idx := 0
  for i in [1:8] do
    let mut smaller := 0
    for j in [i+1:8] do
      if p[j]! < p[i]! then smaller := smaller + 1
    idx := idx * (8 - i) + smaller
  return idx

def decodeP (idx : Nat) : Array Nat := Id.run do
  let mut digits := Array.replicate 8 0
  let mut r := idx
  for k in [0:7] do
    let i := 7 - k
    digits := digits.set! i (r % (8 - i))
    r := r / (8 - i)
  let mut avail : List Nat := [1, 2, 3, 4, 5, 6, 7]
  let mut p : Array Nat := #[0]
  for i in [1:8] do
    let v := avail[digits[i]!]!
    p := p.push v
    avail := avail.erase v
  return p

def encodeT (t : Array Nat) : Nat := (List.range 6).foldl (fun a c => a + t[c + 1]! * 3 ^ c) 0

def decodeT (idx : Nat) : Array Nat := Id.run do
  let mut t : Array Nat := #[0]
  let mut s := 0
  for c in [0:6] do
    let v := (idx / 3 ^ c) % 3
    t := t.push v
    s := s + v
  return t.push ((3 - s % 3) % 3)

def actP (m : Nat) (p : Array Nat) : Array Nat := Id.run do
  let mut q := Array.replicate 8 0
  for c in [0:8] do q := q.set! (dest m c) p[c]!
  return q

def actT (m : Nat) (t : Array Nat) : Array Nat := Id.run do
  let mut u := Array.replicate 8 0
  for c in [0:8] do u := u.set! (dest m c) ((t[c]! + delta m c) % 3)
  return u

/-- Turn tables, computed once. -/
def CPM : Array (Array Nat) := (Array.range 9).map fun m => (Array.range NCP).map fun i => encodeP (actP m (decodeP i))
def COM : Array (Array Nat) := (Array.range 9).map fun m => (Array.range NCO).map fun i => encodeT (actT m (decodeT i))

/-- The state after turn m. -/
def step (x m : Nat) : Nat := (CPM[m]!)[x / NCO]! * NCO + (COM[m]!)[x % NCO]!
/-- The placement after turn m (twists ignored). -/
def pstep (P m : Nat) : Nat := (CPM[m]!)[P]!

def ALL : List Nat := List.range 9
def HALF : List Nat := [1, 4, 7]
/-- The cost of a turn when only quarter turns count. -/
def w (m : Nat) : Nat := if m % 3 == 1 then 0 else 1

/-- Corner coordinates of a sticker state. -/
def pieceAt (s : State) (c : Nat) : Nat := cornerOf s[(CORD[c]!)[0]!]!
def coordOf (s : State) : Nat :=
  encodeP ((Array.range 8).map (pieceAt s)) * NCO + encodeT ((Array.range 8).map (twistAt s))

def SOLVEDX : Nat := coordOf SOLVED

/-- The sticker permutation of turn m. -/
def turnPerm (m : Nat) : State := MOVES (TURN_NAMES[m]!)

/-! ### What a corner shows: its kind

  0  good: in its own tetrad, all three stickers on faces of their own axis
  1  twisted clockwise, 2 twisted counter-clockwise: in its own tetrad, no sticker on a face of its own axis
  3, 4, 5  out: in the other tetrad, and only the R/L (3), U/D (4) or F/B (5) sticker is on a face of its axis

  The tetrad of a place is the sign of x·y·z; DBL's tetrad is DBL, UFL, UBR, DFR. -/

def tet (c : Nat) : Bool := let p := CORNERS[c]!; p[0]! * p[1]! * p[2]! < 0

/-- The axis of the face on which the U/D sticker of the corner at place c sits when its twist is t. -/
def udFaceAxis (c t : Nat) : Nat := nax ((CORD[c]!)[t]!)

/-- The kind of piece h (a home place) sitting at place c with twist t.  `CORD` lists the faces of a corner
counter-clockwise seen from outside (`cord_is_counterclockwise`), so twist 2 is one step clockwise. -/
def kindOf (c h t : Nat) : Nat :=
  if tet c == tet h then (if t == 0 then 0 else if t == 2 then 1 else 2)
  else (if udFaceAxis c t == 1 then 4 else if udFaceAxis c t == 0 then 5 else 3)

def KINDT : Array Nat := (Array.range 192).map fun i => kindOf (i / 24) ((i / 3) % 8) (i % 3)

/-- The kinds at places 1 … 7 as one number, Σ kind(c)·6^(c-1). -/
def kindsOfCoords (p t : Array Nat) : Nat :=
  (List.range 7).foldl (fun a c => a + KINDT[(c + 1) * 24 + p[c + 1]! * 3 + t[c + 1]!]! * POW6[c]!) 0
def kindsOf (x : Nat) : Nat := kindsOfCoords (decodeP (x / NCO)) (decodeT (x % NCO))
def KINDS : Array Nat := (Array.range N).map kindsOf
/-- The kinds a state shows (a table look-up of `kindsOf`). -/
def kinds (x : Nat) : Nat := KINDS[x]!
/-- The kind at place c (1 … 7) in a kinds number. -/
def kindAt (ks c : Nat) : Nat := (ks / POW6[c - 1]!) % 6

/-! The same read straight off the stickers. -/

/-- The sticker place of corner place c on a face of axis a. -/
def cplAxis (c a : Nat) : Nat := (CPL[c]!.find? fun i => nax i == a).getD 54
/-- In sticker state s: the sticker of the corner at place c that is on an axis-a face has an axis-a colour. -/
def orientedOn (s : State) (c a : Nat) : Bool := cax s[cplAxis c a]! == a
def orientedCount (s : State) (c : Nat) : Nat := ((List.range 3).filter (orientedOn s c)).length
/-- How many steps clockwise from the U/D face the U/D-coloured sticker sits. -/
def cwTwist (s : State) (c : Nat) : Nat := (3 - twistAt s c) % 3
def stickerKind (s : State) (c : Nat) : Nat :=
  let n := orientedCount s c
  if n == 3 then 0
  else if n == 0 then (if cwTwist s c == 1 then 1 else 2)
  else if orientedOn s c 0 then 3 else if orientedOn s c 1 then 4 else 5

/-- The sticker states within `n` R, U, F turns of solved (with repeats). -/
def nearRUF (n : Nat) : List State := Id.run do
  let mut layer : List State := [SOLVED]
  let mut out : List State := [SOLVED]
  for _ in [0:n] do
    layer := layer.flatMap fun s => (List.range 9).map fun m => apply s (turnPerm m)
    out := out ++ layer
  return out

/-! ### What a turn does to the kinds -/

/-- A (piece, twist) pair that shows kind k at place c: the first one. -/
def repOf (c k : Nat) : Option (Nat × Nat) :=
  ((List.range 7).flatMap fun h => (List.range 3).map fun t => (h + 1, t)).find? fun (h, t) => kindOf c h t == k

/-- What turn m makes of a corner of kind k at place c: its new kind (6 if no corner shows k there).  Worked
out on one piece that shows k; `quarter_rule` checks it on every state, so it holds for every piece. -/
def kchg (m c k : Nat) : Nat :=
  match repOf c k with
  | some (h, t) => kindOf (dest m c) h ((t + delta m c) % 3)
  | none => 6
def KCHG : Array Nat := (Array.range 432).map fun i => kchg (i / 48) ((i / 6) % 8) (i % 6)

/-- Turn m acting on a kinds number: every corner goes where the turn carries it, with its kind changed. -/
def kindStep (m ks : Nat) : Nat := Id.run do
  let mut out := 0
  let mut r := ks
  for c in [1:8] do
    out := out + KCHG[m * 48 + c * 6 + r % 6]! * POW6[DEST[m * 8 + c]! - 1]!
    r := r / 6
  return out

/-! ### Parity and colours (both depend on the placement only) -/

/-- 1 when the placement is an odd permutation. -/
def parityOfP (p : Array Nat) : Nat := Id.run do
  let mut inv := 0
  for i in [1:8] do
    for j in [i+1:8] do
      if p[j]! < p[i]! then inv := inv + 1
  return inv % 2
def PAR : Array Nat := (Array.range NCP).map fun i => parityOfP (decodeP i)
def odd (x : Nat) : Bool := PAR[x / NCO]! == 1

/-- The places (bit c-1 for place c) holding a corner whose home is on the - side of axis a: for a = 1 the
corners with the D colour, for a = 2 those with the B colour, for a = 0 those with the L colour. -/
def colourOfP (a : Nat) (p : Array Nat) : Nat :=
  (List.range 7).foldl (fun acc c => if (CORNERS[p[c + 1]!]!)[a]! == -1 then acc + 2 ^ c else acc) 0
def COL : Array (Array Nat) := (Array.range 3).map fun a => (Array.range NCP).map fun i => colourOfP a (decodeP i)
def colourX (x : Nat) : Nat := (COL[0]!)[x / NCO]!
def colourY (x : Nat) : Nat := (COL[1]!)[x / NCO]!
def colourZ (x : Nat) : Nat := (COL[2]!)[x / NCO]!

/-- The corner places (indices into `pieces.CORNERS`) in the order UFR UFL UBR DFR UBL DFL DBR, the order the
study writes them in. -/
def PLACE_ORDER : List Nat := [7, 3, 6, 5, 2, 1, 4]
def PLACE_NAMES : List String := ["UFR", "UFL", "UBR", "DFR", "UBL", "DFL", "DBR"]
/-- The places a colour picture marks, by name (DBL, which always has its own colours, is left out). -/
def pictureNames (pic : Nat) : List String :=
  (List.range 7).filterMap fun i => if (pic >>> (PLACE_ORDER[i]! - 1)) % 2 == 1 then some PLACE_NAMES[i]! else none

/-! ### Goal sets -/

/-- HTR: the states reached from solved with half turns.  `dh` is that search. -/
def dh : ByteArray := search.bfs N [SOLVEDX] HALF step
def inHTR (x : Nat) : Bool := dh.get! x != 255
def HTR : List Nat := (List.range N).filter inHTR

/-- Every corner good: in its tetrad and oriented.  These are the states that are DR on all three axes. -/
def allGood (x : Nat) : Bool := kinds x == 0
def GOOD : List Nat := (List.range N).filter allGood
def goodEven (x : Nat) : Bool := allGood x && !odd x
def GOODEVEN : List Nat := GOOD.filter fun x => !odd x

/-- The six pictures the D-coloured corners show in HTR. -/
def SIX : List Nat := (HTR.map colourY).eraseDups

/-! ### Tables -/

/-- Turns from solved (the 2x2x2 table), used to see that every coordinate is a real state. -/
def dSolved : ByteArray := search.bfs N [SOLVEDX] ALL step
def isSolved (x : Nat) : Bool := x == SOLVEDX

def dHTR : ByteArray := search.bfs N HTR ALL step
def qHTR : ByteArray := search.bfs01 N HTR ALL w step
def dGood : ByteArray := search.bfs N GOOD ALL step
def qGood : ByteArray := search.bfs01 N GOOD ALL w step
def dGoodEven : ByteArray := search.bfs N GOODEVEN ALL step
def qGoodEven : ByteArray := search.bfs01 N GOODEVEN ALL w step

/-- Placements only (twists ignored): the 24 HTR placements, and the tables with all nine turns. -/
def HTRP : List Nat := (HTR.map (· / NCO)).eraseDups
def inHTRP (P : Nat) : Bool := HTRP.contains P
def dPerm : ByteArray := search.bfs NCP HTRP ALL pstep
def qPerm : ByteArray := search.bfs01 NCP HTRP ALL w pstep

/-- The DR turns of axis a: the quarter and half turns of its face, the half turns of the other two faces. -/
def DRM (a : Nat) : List Nat := ALL.filter fun m => m / 3 == a || m % 3 == 1
/-- DR turns only, as tables over placements.  DR turns of axis a keep the corners oriented on a, so the
states oriented on a correspond one to one to placements. -/
def dDR : Array ByteArray := (Array.range 3).map fun a => search.bfs NCP HTRP (DRM a) pstep
def qDR : Array ByteArray := (Array.range 3).map fun a => search.bfs01 NCP HTRP (DRM a) w pstep

/-- The state with placement P and every corner oriented on axis a (good, or out with the axis-a sticker
oriented): its twists are found place by place. -/
def orientedState (a P : Nat) : Nat :=
  let p := decodeP P
  let t := (Array.range 8).map fun c =>
    if c == 0 then 0 else ((List.range 3).find? fun t => kindOf c p[c]! t == 0 || kindOf c p[c]! t == 3 + a).getD 3
  P * NCO + encodeT t

/-! ### Named functions for the checks (so that they run compiled) -/

def fSolved (x : Nat) : Nat := (dSolved.get! x).toNat
def fHTR (x : Nat) : Nat := (dHTR.get! x).toNat
def fGood (x : Nat) : Nat := (dGood.get! x).toNat
def fGoodEven (x : Nat) : Nat := (dGoodEven.get! x).toNat
def fPerm (x : Nat) : Nat := (dPerm.get! (x / NCO)).toNat
def gHTR (x : Nat) : Nat := (qHTR.get! x).toNat
def gGood (x : Nat) : Nat := (qGood.get! x).toNat
def gGoodEven (x : Nat) : Nat := (qGoodEven.get! x).toNat
def gPerm (x : Nat) : Nat := (qPerm.get! (x / NCO)).toNat

/-- The weight of a state: 1 for each out corner, 2 for each twisted corner. -/
def weightOfKinds (ks : Nat) : Nat := Id.run do
  let mut out := 0
  let mut r := ks
  for _ in [0:7] do
    let k := r % 6
    out := out + (if k == 0 then 0 else if k ≥ 3 then 1 else 2)
    r := r / 6
  return out
def weight (x : Nat) : Nat := weightOfKinds (kinds x)

/-! ### Sequences of turns -/

/-- The state after a sequence of turns (numbers 0 … 8). -/
def run (x : Nat) (ms : List Nat) : Nat := ms.foldl step x
/-- How many quarter turns a sequence has. -/
def quarters (ms : List Nat) : Nat := (ms.filter isQuarter).length
/-- The sequence that undoes `ms`: the inverse turns in reverse order. -/
def invSeq (ms : List Nat) : List Nat := (ms.map invTurn).reverse
/-- A sequence written as text ("R U2 F'") as turn numbers (an unknown name becomes 9, which is no turn). -/
def turnsOf (scr : String) : List Nat := (parse scr).map fun t => TURN_NAMES.idxOf t

/-- The corner coordinate of a scramble (R, U, F turns as text), on the sticker model. -/
def ofScramble (scr : String) : Nat := coordOf (do_ SOLVED scr)

end corners
end Corners3D
