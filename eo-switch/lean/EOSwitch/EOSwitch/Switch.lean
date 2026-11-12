/-
  EOSwitch.Switch — the EO-kept DR distance over the 1,082,565 EO-solved states, and the switch features of the
  study, per state, with the tally of (DRM, features) cells.

  State.  F/B EO solved, DR on U/D.  x = co · 4096 + m:  co = Σ twist_c · 3^c over the 8 corner places (0 … 6560,
  `pieces.coOf`), m = 12-bit mask of the edge places holding E-slice pieces (`pieces.eMask`).  The 14 turns that
  keep F/B EO (U, D, R, L turns, F2, B2) act by `pieces.coAct`, `pieces.maskAct`.  The goal (DR on U/D) is co = 0,
  m = the four E-slice places.  `dist` is the BFS from the goal with those turns, checked by `search.ruleHolds`
  (see Search.lean), so an entry is the fewest such turns from the state to DR.  This is the BFS of eo-to-dr's
  certificate (`EODR/Eodr.lean`), done again here.

  Features.  As in the research's `src/features.py` (`build`), all defined by places and stickers:
    * a corner is *bad* (twisted) when its twist ≠ 0; `udAxis` is the axis of the face its U/D sticker is on
      (0 R/L, 1 U/D, 2 F/B; read off `CORD`, so it does not depend on how the twist is numbered);
    * U/D-layer edge places: the 8 with a U or D sticker (y ≠ 0); E-slice places: the other 4;
      M places (UF UB DF DB): U/D-layer places with x = 0; a *bad U/D edge* is an E-slice piece in a U/D-layer place;
    * `NB k`: the two corners next to edge place k: those that agree with k on its two non-zero coordinates
      (research: `layer_nb` for a U/D-layer place, `vert_nb` for an E-slice place);
    * `zeroAxis k`: the axis on which edge place k has coordinate 0 (research: `free_axis`);
    * a *pair* is a bad U/D edge at k and a bad corner c in `NB k` with udAxis c = zeroAxis k (the U/D sticker is
      on the face the edge does not touch); a *fake pair* the same with udAxis c ≠ zeroAxis k;
    * `pairs` = number of pairs; `edgesPaired` = bad U/D edges with at least one pair; `bars` = with two;
    * `side` (side pairs) = over the E-slice places holding a non-E piece, the corners c in `NB k` that are bad with
      udAxis c = 2 (U/D sticker on F or B); the study's "pairs + side pairs / 2" is (2 · pairs + side) / 2;
    * `sameSlice` (research `edges_same_slice`): at least 2 bad U/D edges, and all in M places (x = 0) or all in S
      places (z = 0);
    * DRM xcye: x = bad corners, y = 2 × bad U/D edges; `carm` = bad corners with udAxis 0 (U/D sticker on R/L),
      `earm` = E-slice pieces in M places; `jzp` = carm = 0, earm = 0 and an even number of bad corners.
-/
import EOSwitch.Pieces
import EOSwitch.Search

set_option compiler.extract_closed false

namespace EOSwitch
namespace sw
open cube pieces

/-! ### The BFS (as in EODR/Eodr.lean) -/

/-- The 14 turns that keep F/B EO: U, D, R, L turns and F2, B2 (indices in `NAMES`). -/
def KEEP : List Nat := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 16]

def N : Nat := 6561 * 4096

def step (cot mt : Array (Array Nat)) (x mv : Nat) : Nat := cot[mv]![x / 4096]! * 4096 + mt[mv]![x % 4096]!

def COT : Array (Array Nat) := (Array.range 18).map fun mv => (Array.range 6561).map (coAct mv)
def MT : Array (Array Nat) := (Array.range 18).map fun mv => (Array.range 4096).map (maskAct mv)

def GOAL : Nat := E_HOME

/-- The BFS table (255 = not reached). -/
def dist : ByteArray := search.bfs N GOAL KEEP (step COT MT)

/-! ### Geometry of the places -/

/-- Position of edge place k and of corner place c ([x, y, z]). -/
def EV (k : Nat) : Vec := EDGES[k]!
def CV (c : Nat) : Vec := CORNERS[c]!

/-- The 8 U/D-layer edge places, the 4 E-slice places, the 4 M places. -/
def UD_PLACES : List Nat := (List.range 12).filter fun k => (EV k)[1]! != 0
def E_SLOTS : List Nat := (List.range 12).filter fun k => (EV k)[1]! == 0
def M_PLACES : List Nat := UD_PLACES.filter fun k => (EV k)[0]! == 0
def isM (k : Nat) : Bool := (EV k)[0]! == 0
def isS (k : Nat) : Bool := (EV k)[2]! == 0

/-- The corners next to edge place k: equal to k on each coordinate where k is not 0. -/
def nbOf (k : Nat) : List Nat :=
  (List.range 8).filter fun c => (List.range 3).all fun i => (EV k)[i]! == 0 || (CV c)[i]! == (EV k)[i]!
def NB : Array (List Nat) := (Array.range 12).map nbOf

/-- The axis on which edge place k has coordinate 0. -/
def zeroAxis (k : Nat) : Nat := ((List.range 3).find? fun i => (EV k)[i]! == 0).getD 3
def ZAX : Array Nat := (Array.range 12).map zeroAxis

/-- `UDAX[c][t]`: the axis of the face the U/D sticker of the corner at place c is on, when its twist is t. -/
def UDAX : Array (Array Nat) := (Array.range 8).map fun c => (Array.range 3).map fun t => nax (CORD[c]!)[t]!

/-! ### Features of a state -/

def twist (co c : Nat) : Nat := (co / 3 ^ c) % 3
def bad (co c : Nat) : Bool := twist co c != 0
def udAxis (co c : Nat) : Nat := UDAX[c]![twist co c]!
def holdsE (m k : Nat) : Bool := (m >>> k) &&& 1 == 1

/-- Pairs and fake pairs at a U/D-layer edge place k (counted whatever k holds). -/
def pairsAt (co k : Nat) : Nat := NB[k]!.countP fun c => bad co c && udAxis co c == ZAX[k]!
def fakeAt (co k : Nat) : Nat := NB[k]!.countP fun c => bad co c && udAxis co c != ZAX[k]!
/-- Side pairs at an E-slice place k (counted whatever k holds). -/
def sideAt (co k : Nat) : Nat := NB[k]!.countP fun c => bad co c && udAxis co c == 2

structure Feat where
  /-- bad (twisted) corners -/
  c : Nat
  /-- 2 × bad U/D edges (E-slice pieces in the U/D layers) -/
  e : Nat
  carm : Nat
  earm : Nat
  pairs : Nat
  fake : Nat
  edgesPaired : Nat
  bars : Nat
  side : Nat
  sameSlice : Bool
  jzp : Bool
  deriving DecidableEq, Repr

def feat (co m : Nat) : Feat :=
  let out := UD_PLACES.filter (holdsE m)
  let c := (List.range 8).countP (bad co)
  let carm := (List.range 8).countP fun i => bad co i && udAxis co i == 0
  let earm := M_PLACES.countP (holdsE m)
  { c, carm, earm
    e := 2 * out.length
    pairs := (out.map (pairsAt co)).sum
    fake := (out.map (fakeAt co)).sum
    edgesPaired := out.countP fun k => pairsAt co k ≥ 1
    bars := out.countP fun k => pairsAt co k == 2
    side := ((E_SLOTS.filter fun k => !holdsE m k).map (sideAt co)).sum
    sameSlice := out.length ≥ 2 && (out.all isM || out.all isS)
    jzp := carm == 0 && earm == 0 && c % 2 == 0 }

/-! ### The tally -/

/-- A cell: the features the study's tables split by. -/
structure Cell where
  c : Nat
  e : Nat
  pairs : Nat
  edgesPaired : Nat
  bars : Nat
  sameSlice : Bool
  side : Nat
  jzp : Bool
  deriving DecidableEq, Repr

def cellOf (f : Feat) : Cell := ⟨f.c, f.e, f.pairs, f.edgesPaired, f.bars, f.sameSlice, f.side, f.jzp⟩

def encode (k : Cell) : Nat :=
  ((((((k.c * 5 + k.e / 2) * 9 + k.pairs) * 5 + k.edgesPaired) * 5 + k.bars) * 2 + (if k.sameSlice then 1 else 0))
    * 9 + k.side) * 2 + (if k.jzp then 1 else 0)
def NCELL : Nat := 9 * 5 * 9 * 5 * 5 * 2 * 9 * 2
def decode (i : Nat) : Cell :=
  let j := i % 2; let i := i / 2
  let s := i % 9; let i := i / 9
  let ss := i % 2; let i := i / 2
  let b := i % 5; let i := i / 5
  let ep := i % 5; let i := i / 5
  let p := i % 9; let i := i / 9
  let e := i % 5; let c := i / 5
  ⟨c, 2 * e, p, ep, b, ss == 1, s, j == 1⟩

/-- Number of distances kept per cell: 0 … 11. -/
def W : Nat := 12

structure Result where
  /-- the BFS table passes `search.ruleHolds` -/
  rule : Bool
  /-- the reached states are exactly (twist sum ≡ 0 mod 3) × (4 marked places) -/
  reachedIsValid : Bool
  /-- states reached -/
  states : Nat
  /-- every reached state's features fit the cell encoding (bounds), and `encode` / `decode` agree on it -/
  encodable : Bool
  /-- each cell that occurs, with its distance histogram [states at 0, …, 11] -/
  cells : List (Cell × List Nat)
  deriving DecidableEq, Repr

def twists (co : Nat) : List Nat := (List.range 8).map (twist co)
def CO_OK : Array Bool := (Array.range 6561).map fun co => (twists co).sum % 3 == 0
def M_OK : Array Bool := (Array.range 4096).map fun m => popcount m == 4

def fits (k : Cell) : Bool :=
  k.c < 9 && k.e < 10 && k.e % 2 == 0 && k.pairs < 9 && k.edgesPaired < 5 && k.bars < 5 && k.side < 9

/-- The tally over all states of a filled-in table d.  Separate and not inlined, on purpose (EODR's note: the
compiler can otherwise move the BFS into the loop body). -/
@[noinline] def tally (d : ByteArray) : Bool × Nat × Bool × List (Cell × List Nat) := Id.run do
  let coOk := CO_OK
  let mOk := M_OK
  let mut ok := true
  let mut enc := true
  let mut states := 0
  let mut t : Array Nat := Array.replicate (NCELL * W) 0
  for x in [0:N] do
    let r := search.reached d x
    if r != (coOk[x / 4096]! && mOk[x % 4096]!) then ok := false
    if !r then continue
    states := states + 1
    let k := cellOf (feat (x / 4096) (x % 4096))
    if !(fits k && decode (encode k) == k) then enc := false
    let v := (d.get! x).toNat
    let i := encode k * W + v
    t := t.modify i (· + 1)
  let mut cells := []
  for i in [0:NCELL] do
    let row := (List.range W).map fun v => t[i * W + v]!
    if row.sum > 0 then cells := cells ++ [(decode i, row)]
  return (ok, states, enc, cells)

def run : Result :=
  let d := dist
  let rule := search.ruleHolds N GOAL KEEP (step COT MT) d
  let (ok, states, enc, cells) := tally d
  ⟨rule, ok, states, enc, cells⟩

/-! ### Readings of the cell table -/

abbrev Rows := List (Cell × List Nat)

def addH (a b : List Nat) : List Nat := List.zipWith (· + ·) a b
def sumH (rs : Rows) : List Nat := rs.foldl (fun acc r => addH acc r.2) (List.replicate W 0)

/-- Distance histogram of all states, and of one DRM. -/
def total (rs : Rows) : List Nat := sumH rs
def drm (rs : Rows) (c e : Nat) : Rows := rs.filter fun r => r.1.c == c && r.1.e == e
/-- Σ d · count. -/
def weighted (h : List Nat) : Nat := ((List.range h.length).map fun i => i * h[i]!).sum
/-- States at distance ≤ k. -/
def le (h : List Nat) (k : Nat) : Nat := (h.take (k + 1)).sum

def b2n (b : Bool) : Nat := if b then 1 else 0

/-- One DRM split by a key: for each key value that occurs (sorted), [states, ≤ 5, ≤ 6, ≤ 7]. -/
def split (rs : Rows) (c e : Nat) (key : Cell → List Nat) : List (List Nat × List Nat) :=
  let sub := drm rs c e
  let keys := ((sub.map fun r => key r.1).eraseDups).mergeSort (fun a b => decide (a ≤ b))
  keys.map fun kv =>
    let h := sumH (sub.filter fun r => key r.1 == kv)
    (kv, [h.sum, le h 5, le h 6, le h 7])

end sw
end EOSwitch
