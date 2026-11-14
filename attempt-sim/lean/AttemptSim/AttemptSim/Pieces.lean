/-
  AttemptSim.Pieces — copied unchanged, but for the namespace, from the EO-switch study's certificate (eo-switch/lean/EOSwitch), which has it from eo-to-dr's
  (lean/EODR/EODR/Pieces.lean).  Edge orientation, corner twist and the E-slice pieces, read off the sticker model of `Cube.lean`,
  and what each of the 18 face turns does to them.  Nothing here is typed by hand: every table is computed from
  the 54-sticker permutations of `Cube.lean`.

  Axes: 0 = R/L, 1 = U/D, 2 = F/B (as in `Cube.lean`: x, y, z).  Edge places k = 0 … 11 and corner places
  c = 0 … 7 are the cubie positions of `Cube.lean` in sorted order (`EDGES`, `CORNERS`).

  EO on axis Y.  For each edge place, one of its two stickers is the *reference sticker* for Y: the one on a face
  of the axis `PRI Y` (U/D, or F/B when Y is U/D) if the place has one, else the one on a Y face.  A piece's
  reference sticker is the one that is the reference sticker of its home place.  An edge is *good* for Y when its
  reference sticker sits on the reference sticker of the place it is in; *bad* otherwise.  This is the usual
  definition (good = can be brought home without quarter turns of the Y faces); the theorem `flip_table` checks
  that with this rule a face turn changes goodness for Y exactly when it is a quarter turn of a Y face, and then
  for the four edges of that face.

  Corner twist (for the U/D axis, the one DR is on in C).  The three stickers of a corner place are listed
  starting with its U/D sticker and going round the corner in a fixed sense (`CORD`, chosen by the sign of a
  determinant); the twist of the corner at a place is the position in that list of the sticker holding a U/D
  colour (0 = oriented for U/D).  `corner_turns_cyclic` checks that every face turn carries each such list onto
  the list of the destination place shifted cyclically, so a turn adds a fixed amount mod 3 to the twist.

  E-slice pieces: the four edges with no U/D colour.  DR on U/D (with F/B EO solved, as in the study's coset
  tables) = every corner twist 0 and the four E-slice pieces in the four E-slice places.
-/
import AttemptSim.Cube

namespace AttemptSim
namespace pieces
open cube

/-- Axis (0 R/L, 1 U/D, 2 F/B) of the face that sticker place `i` is on. -/
def nax (i : Nat) : Nat := argmax_abs cube.ST[i]!.2
/-- Axis of the colour of the sticker whose home is `h`. -/
def cax (h : Nat) : Nat := (AX FACE_OF[h]!).1

/-- (cubie position, its sticker places in increasing order), for the 26 cubies that have stickers. -/
def CUBIES_TABLE : List (Vec × List Nat) :=
  (product3.map fun p => (p, (List.range 54).filter fun i => cube.ST[i]!.1 == p)).filter fun (_, pl) => pl.length > 0
def CUBIES (p : Vec) : List Nat := (CUBIES_TABLE.lookup p).getD []
def CORNERS : List Vec := sorted ((CUBIES_TABLE.filter fun (_, pl) => pl.length == 3).map (·.1))
def EDGES : List Vec := sorted ((CUBIES_TABLE.filter fun (_, pl) => pl.length == 2).map (·.1))

/-- The two sticker places of edge place k. -/
def EPL : Array (List Nat) := EDGES.toArray.map CUBIES
/-- The three sticker places of corner place c. -/
def CPL : Array (List Nat) := CORNERS.toArray.map CUBIES

/-- The edge place that sticker place i belongs to (12 if none). -/
def edgeOf (i : Nat) : Nat := ((List.range 12).find? fun k => EPL[k]!.contains i).getD 12
/-- The corner place that sticker place i belongs to (8 if none). -/
def cornerOf (i : Nat) : Nat := ((List.range 8).find? fun c => CPL[c]!.contains i).getD 8

/-! ### Edge orientation -/

/-- The axis whose sticker is the reference where there is one: U/D, or F/B for EO on U/D. -/
def PRI (Y : Nat) : Nat := if Y == 1 then 2 else 1

/-- The reference sticker of edge place k for axis Y. -/
def refOf (Y k : Nat) : Nat :=
  let pl := EPL[k]!
  match pl.find? (fun i => nax i == PRI Y) with
  | some i => i
  | none => (pl.find? fun i => nax i == Y).getD 54
/-- `refOf` as a table, computed once (3 x 12); `ref Y k` reads it. -/
def REFT : Array (Array Nat) := (Array.range 3).map fun Y => (Array.range 12).map (refOf Y)
def ref (Y k : Nat) : Nat := REFT[Y]![k]!
/-- The other sticker of edge place k. -/
def other (Y k : Nat) : Nat := (EPL[k]!.find? (· != ref Y k)).getD 54
/-- The twelve reference stickers for Y (a table, computed once). -/
def REFS : Array (List Nat) := (Array.range 3).map fun Y => (List.range 12).map (ref Y)
def REF (Y : Nat) : List Nat := REFS[Y]!

/-- In state s, the edge at place k is good for Y. -/
def good (Y : Nat) (s : State) (k : Nat) : Bool := (REF Y).contains s[ref Y k]!
/-- The bad edges for Y as a 12-bit number: bit k set when the edge at place k is bad. -/
def badMask (Y : Nat) (s : State) : Nat :=
  (List.range 12).foldl (fun acc k => if good Y s k then acc else acc + 2 ^ k) 0

/-- The 18 face turns in the order of `NAMES` (U U2 U' D D2 D' R R2 R' L L2 L' F F2 F' B B2 B'). -/
def MV : Array State := (NAMES.map MOVES).toArray

/-- Where move `mv` carries the edge at place k. -/
def edest (mv k : Nat) : Nat := edgeOf (MV[mv]!)[(EPL[k]!)[0]!]!
/-- Whether move `mv` changes the goodness for Y of the edge at place k (its reference sticker lands on a place
sticker that is not the reference sticker of the new place). -/
def eflip (Y mv k : Nat) : Bool := (MV[mv]!)[ref Y k]! != ref Y (edest mv k)

/-- `EDEST[mv][k]`, `EFLIP[Y][mv][k]` as tables. -/
def EDEST : Array (Array Nat) := (Array.range 18).map fun mv => (Array.range 12).map (edest mv)
def EFLIP : Array (Array (Array Bool)) :=
  (Array.range 3).map fun Y => (Array.range 18).map fun mv => (Array.range 12).map (eflip Y mv)

/-- Move `mv` acting on a 12-bit mask of bad edges for Y. -/
def eoAct (Y mv e : Nat) : Nat := Id.run do
  let mut out := 0
  for k in [0:12] do
    let b := (e >>> k) &&& 1 == 1
    let b' := b != EFLIP[Y]![mv]![k]!
    if b' then out := out + 2 ^ (EDEST[mv]![k]!)
  return out

/-- `EOT[Y][mv][e] = eoAct Y mv e` for all 4096 masks, computed once. -/
def EOT : Array (Array (Array Nat)) :=
  (Array.range 3).map fun Y => (Array.range 18).map fun mv => (Array.range 4096).map (eoAct Y mv)

/-! ### Corner twist (U/D) -/

def cross (a b : Vec) : Vec :=
  [a[1]! * b[2]! - a[2]! * b[1]!, a[2]! * b[0]! - a[0]! * b[2]!, a[0]! * b[1]! - a[1]! * b[0]!]
def dot (a b : Vec) : Int := a[0]! * b[0]! + a[1]! * b[1]! + a[2]! * b[2]!

/-- The three sticker places of a corner: its U/D sticker first, then the other two in the sense that makes
(n₀ × n₁) · n₂ > 0 for their outward normals. -/
def corder (pl : List Nat) : List Nat :=
  let u := (pl.find? fun i => nax i == 1).getD 54
  let o := pl.filter (· != u)
  let a := o[0]!; let b := o[1]!
  if dot (cross cube.ST[u]!.2 cube.ST[a]!.2) cube.ST[b]!.2 > 0 then [u, a, b] else [u, b, a]
def CORD : Array (List Nat) := CPL.map corder

/-- Twist of the corner at place c in state s: the position in `CORD[c]` of the sticker with a U/D colour. -/
def twistAt (s : State) (c : Nat) : Nat := (CORD[c]!.findIdx? fun i => cax s[i]! == 1).getD 3

/-- Where move `mv` carries the corner at place c, and by how much it turns it (mod 3). -/
def cdest (mv c : Nat) : Nat := cornerOf (MV[mv]!)[(CORD[c]!)[0]!]!
def cdelta (mv c : Nat) : Nat := CORD[cdest mv c]!.idxOf (MV[mv]!)[(CORD[c]!)[0]!]!
def CDEST : Array (Array Nat) := (Array.range 18).map fun mv => (Array.range 8).map (cdest mv)
def CDELTA : Array (Array Nat) := (Array.range 18).map fun mv => (Array.range 8).map (cdelta mv)

/-- The move carries the list `CORD[c]` onto `CORD[cdest]` shifted by `cdelta`. -/
def cyclic (mv c : Nat) : Bool :=
  (List.range 3).all fun k => (MV[mv]!)[(CORD[c]!)[k]!]! == (CORD[cdest mv c]!)[(k + cdelta mv c) % 3]!

/-- The eight twists as one number Σ t_c·3^c (0 … 6560). -/
def coOf (s : State) : Nat := (List.range 8).foldl (fun acc c => acc + twistAt s c * 3 ^ c) 0

/-- Move `mv` acting on that number. -/
def coAct (mv co : Nat) : Nat := Id.run do
  let mut out := 0
  for c in [0:8] do
    let t := (co / 3 ^ c) % 3
    out := out + ((t + CDELTA[mv]![c]!) % 3) * 3 ^ (CDEST[mv]![c]!)
  return out

/-! ### E-slice pieces -/

/-- The places holding an E-slice piece (no U/D colour) as a 12-bit number. -/
def eMask (s : State) : Nat :=
  (List.range 12).foldl (fun acc k => if EPL[k]!.any (fun i => cax s[i]! == 1) then acc else acc + 2 ^ k) 0

/-- Move `mv` acting on such a mask. -/
def maskAct (mv m : Nat) : Nat := Id.run do
  let mut out := 0
  for k in [0:12] do
    if (m >>> k) &&& 1 == 1 then out := out + 2 ^ (EDEST[mv]![k]!)
  return out

/-- The E-slice places (= `eMask SOLVED`). -/
def E_HOME : Nat := eMask SOLVED

/-- Kind of an edge place, or of the piece whose home it is: the axis it has no sticker on
(1 = E slice, between U and D; 0 = M slice, between R and L; 2 = S slice, between F and B). -/
def kind (k : Nat) : Nat := ((List.range 3).find? fun a => !(EPL[k]!.any fun i => nax i == a)).getD 3

/-- Edge place k has a sticker on face number f (U D R L F B = 0 … 5). -/
def onFace (f k : Nat) : Bool := EPL[k]!.any fun i => FACE_OF[i]! == FACES[f]!

/-! ### Small helpers -/

def popcount (n : Nat) : Nat := Id.run do
  let mut c := 0
  let mut n := n
  while n > 0 do
    c := c + n % 2
    n := n / 2
  return c

/-- `sorted(Counter(l).items())`: (value, how many times it occurs), by value. -/
def hist (l : List Nat) : List (Nat × Nat) :=
  let vs := (l.eraseDups).mergeSort (· ≤ ·)
  vs.map fun v => (v, l.count v)

/-- The same for an array of distances, faster: (value, count) for the values that occur. -/
def histA (a : Array Nat) (bound : Nat) : List (Nat × Nat) := Id.run do
  let mut h := Array.replicate bound 0
  for x in a do h := h.modify x (· + 1)
  return ((List.range bound).map fun v => (v, h[v]!)).filter (·.2 != 0)

/-- The states reached from the solved cube with at most `n` face turns (with repeats), as sticker states. -/
def near (n : Nat) : List State := Id.run do
  let mut layer : List State := [SOLVED]
  let mut out : List State := [SOLVED]
  for _ in [0:n] do
    layer := layer.flatMap fun s => MV.toList.map fun m => apply s m
    out := out ++ layer
  return out

end pieces
end AttemptSim
