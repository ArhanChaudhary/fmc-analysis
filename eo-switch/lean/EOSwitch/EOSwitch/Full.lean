/-
  EOSwitch.Full — every feature the study's rules use, per state, and the table of all (features, distances)
  groups, built on the BFS of Switch.lean.  Added 2026-11-13 for the recounts of part E (see README.md).

  New features (as in the research's `src/features.py`):
    * *corner case* of a 4-bad-corner state (`cornerCase`, research `corner_case`): the tetrad {ULF URB DRF DLB}
      is the set of corner places with x·y·z = −1.  With a = bad corners in it, split = min(a, 4 − a):
      split 0 → d, split 1 → c, split 2 → b if some U/D layer or some R/L side holds exactly one bad corner, else a.
      Coded 0 a, 1 b, 2 c, 3 d, 4 = not 4 bad corners.
    * *suffix* (`suffix`, research `case_suffix`): corner ARM for a corners, min(carm, 4 − carm) otherwise ("4b-0").
    * *all on one side* (an earlier reading of Evan's "stacked", research `lr_split == 4`; the page now reads "stacked"
      as the sheet's allF/allR/colU layouts): all bad corners on one R/L side face (`lr` = the larger
      of the bad-corner counts on R and on L).
    * `oneLayer` (research `corners_one_layer`): all bad corners on one U/D layer (and at least one).
    * `n1`: corners with twist 1 (the class of the inverse option swaps the counts of twists 1 and 2).
    * `anti` (research `anti_ar`): every bad corner and every bad U/D edge out of AR (carm = c, earm = e/2, c > 0).
    * `split` (wen's split pairs, research `split_pairs`): a bad U/D edge and a bad corner of its layer not next to
      it, both in AR or both out of AR (corner out of AR = U/D sticker on R/L; edge out of AR = in an M place).
    * `a1d` (research `a_one_from_d`): 4a corners, and one U or D turn gives 4d corners.
    * `rlJzp` (research `rl_to_jzp`): an R quarter turn then an L quarter turn gives JZP.
  Distances kept per state: d (EO kept), lastF = min(d(s), d(s·F2)) (the EO's last turn either way), lastFB =
  min over s, s·F2, s·B2, s·F2·B2 (the last two EO turns, F and B, free).
-/
import EOSwitch.Switch
import Std.Data.HashMap

set_option compiler.extract_closed false

namespace EOSwitch
namespace full
open cube pieces sw

/-! ### Per-corner geometry -/

/-- Corner place c is in the tetrad {ULF URB DRF DLB} (x·y·z = −1). -/
def ORB1 (c : Nat) : Bool := (CV c)[0]! * (CV c)[1]! * (CV c)[2]! == -1
def onU (c : Nat) : Bool := (CV c)[1]! > 0
def onR (c : Nat) : Bool := (CV c)[0]! > 0

/-! ### Features that depend on the corner twists only -/

def badList (co : Nat) : List Nat := (List.range 8).filter (bad co)

/-- Rodney's corner case: 0 a, 1 b, 2 c, 3 d; 4 when there are not exactly 4 bad corners. -/
def cornerCase (co : Nat) : Nat :=
  let b := badList co
  if b.length != 4 then 4 else
  let a := b.countP ORB1
  let split := min a (4 - a)
  let u := b.countP onU
  let r := b.countP onR
  let faceMin := min (min u (4 - u)) (min r (4 - r))
  if split == 0 then 3 else if split == 1 then 2 else if faceMin == 1 then 1 else 0

def carmOf (co : Nat) : Nat := (List.range 8).countP fun i => bad co i && udAxis co i == 0

/-- The suffix: corner ARM for a corners, min(carm, 4 − carm) for b, c, d; 7 when not 4 bad corners. -/
def suffix (co : Nat) : Nat :=
  let cc := cornerCase co
  if cc == 4 then 7 else if cc == 0 then carmOf co else min (carmOf co) (4 - carmOf co)

/-- The larger of the numbers of bad corners on R and on L (4 = all four bad corners on one side). -/
def lr (co : Nat) : Nat := let b := badList co; let r := b.countP onR; max r (b.length - r)
def oneLayer (co : Nat) : Bool := let b := badList co; let u := b.countP onU; b.length > 0 && (u == 0 || u == b.length)
def n1 (co : Nat) : Nat := (List.range 8).countP fun i => twist co i == 1

def CC : Array Nat := (Array.range 6561).map cornerCase
/-- 4a corners and one U or D turn (U U2 U' D D2 D', indices 0 … 5) gives 4d corners. -/
def a1d (co : Nat) : Bool := CC[co]! == 0 && (List.range 6).any fun mv => CC[(COT[mv]!)[co]!]! == 3

/-! ### The feature record -/

structure F2 where
  c : Nat
  /-- 2 × bad U/D edges -/
  e : Nat
  carm : Nat
  earm : Nat
  pairs : Nat
  fake : Nat
  side : Nat
  edgesPaired : Nat
  bars : Nat
  sameSlice : Bool
  jzp : Bool
  cc : Nat
  suf : Nat
  lr : Nat
  oneLayer : Bool
  anti : Bool
  split : Nat
  a1d : Bool
  rlJzp : Bool
  n1 : Nat
  deriving DecidableEq, Repr, Inhabited

def b2n (b : Bool) : Nat := if b then 1 else 0

/-- Field widths in bits, in the order of the structure. -/
def WIDTHS : List Nat := [4, 3, 4, 3, 4, 4, 4, 3, 3, 1, 1, 3, 3, 4, 1, 1, 4, 1, 1, 4]

def fields (f : F2) : List Nat :=
  [f.c, f.e / 2, f.carm, f.earm, f.pairs, f.fake, f.side, f.edgesPaired, f.bars, b2n f.sameSlice, b2n f.jzp, f.cc,
   f.suf, f.lr, b2n f.oneLayer, b2n f.anti, f.split, b2n f.a1d, b2n f.rlJzp, f.n1]

def pack (f : F2) : Nat := (List.zip (fields f) WIDTHS).foldr (fun (v, w) acc => acc * 2 ^ w + v) 0

def unpack (k : Nat) : F2 := Id.run do
  let mut k := k
  let mut out : Array Nat := #[]
  for w in WIDTHS do
    out := out.push (k % 2 ^ w)
    k := k / 2 ^ w
  let g := fun i => out[i]!
  return { c := g 0, e := 2 * g 1, carm := g 2, earm := g 3, pairs := g 4, fake := g 5, side := g 6,
           edgesPaired := g 7, bars := g 8, sameSlice := g 9 == 1, jzp := g 10 == 1, cc := g 11, suf := g 12,
           lr := g 13, oneLayer := g 14 == 1, anti := g 15 == 1, split := g 16, a1d := g 17 == 1,
           rlJzp := g 18 == 1, n1 := g 19 }

/-- wen's split pairs. -/
def splitPairs (co m : Nat) : Nat :=
  ((UD_PLACES.filter (holdsE m)).map fun k =>
    ((List.range 8).filter fun c => (CV c)[1]! == (EV k)[1]! && !(NB[k]!.contains c)).countP fun c =>
      bad co c && ((udAxis co c == 0) == isM k)).sum

-- Per-twist-number tables, computed once (top-level constants).
def SUF : Array Nat := (Array.range 6561).map suffix
def LR : Array Nat := (Array.range 6561).map lr
def ONE : Array Bool := (Array.range 6561).map oneLayer
def N1 : Array Nat := (Array.range 6561).map n1
def A1D : Array Bool := (Array.range 6561).map a1d
def CARM : Array Nat := (Array.range 6561).map carmOf
def NBAD : Array Nat := (Array.range 6561).map fun co => (badList co).length
/-- E-slice pieces in M places, per mask. -/
def EARM : Array Nat := (Array.range 4096).map fun m => M_PLACES.countP (holdsE m)

/-- JZP of state x (carm = 0, earm = 0, even number of bad corners), from the tables; `jzp_tables` checks that it
is `feat`'s `jzp` on every state. -/
def jzpAt (x : Nat) : Bool :=
  let co := x / 4096
  CARM[co]! == 0 && EARM[x % 4096]! == 0 && NBAD[co]! % 2 == 0

def f2 (x : Nat) : F2 :=
  let co := x / 4096
  let m := x % 4096
  let f := feat co m
  let st := step COT MT
  { c := f.c, e := f.e, carm := f.carm, earm := f.earm, pairs := f.pairs, fake := f.fake, side := f.side,
    edgesPaired := f.edgesPaired, bars := f.bars, sameSlice := f.sameSlice, jzp := f.jzp,
    cc := CC[co]!, suf := SUF[co]!, lr := LR[co]!, oneLayer := ONE[co]!,
    anti := f.carm == f.c && 2 * f.earm == f.e && f.c > 0,
    split := splitPairs co m, a1d := A1D[co]!,
    rlJzp := [6, 8].any fun m1 => [9, 11].any fun m2 => jzpAt (st (st x m1) m2),
    n1 := N1[co]! }

/-! ### The table of groups -/

/-- Histogram length per distance kind (0 … 11). -/
def W : Nat := 12

structure Table where
  /-- states reached by the BFS -/
  states : Nat
  /-- every state's features fit the field widths, `unpack ∘ pack` gives them back, and `jzpAt` is `feat`'s JZP -/
  packs : Bool
  /-- each feature record that occurs, with 36 counts: d = 0 … 11, lastF = 0 … 11, lastFB = 0 … 11 -/
  groups : Array (F2 × Array Nat)

def fits (f : F2) : Bool := (List.zip (fields f) WIDTHS).all fun (v, w) => v < 2 ^ w

/-- Separate and not inlined, on purpose (see Switch.lean). -/
@[noinline] def build (d : ByteArray) : Table := Id.run do
  let st := step COT MT
  let mut idx : Std.HashMap Nat Nat := {}
  let mut keys : Array Nat := #[]
  let mut h : Array (Array Nat) := #[]
  let mut states := 0
  let mut ok := true
  for x in [0:N] do
    if !search.reached d x then continue
    states := states + 1
    let f := f2 x
    let k := pack f
    if !(fits f && unpack k == f && jzpAt x == f.jzp) then ok := false
    let v := (d.get! x).toNat
    let xf := st x 13
    let xb := st x 16
    let vF := min v (d.get! xf).toNat
    let vFB := min (min vF (d.get! xb).toNat) (d.get! (st xf 16)).toNat
    let mut i := 0
    match idx.get? k with
    | some j => i := j
    | none =>
      i := keys.size
      idx := idx.insert k i
      keys := keys.push k
      h := h.push (Array.replicate (3 * W) 0)
    h := h.modify i fun a => ((a.modify v (· + 1)).modify (W + vF) (· + 1)).modify (2 * W + vFB) (· + 1)
  let groups := (Array.range keys.size).map fun i => (unpack keys[i]!, h[i]!)
  return ⟨states, ok, groups⟩

def T : Table := build dist

/-! ### Readings -/

/-- Sum of the 36 counts over the groups whose features satisfy `p`. -/
def sumWhere (p : F2 → Bool) : Array Nat := Id.run do
  let mut acc := Array.replicate (3 * W) 0
  for (f, a) in T.groups do
    if p f then
      for i in [0:3 * W] do acc := acc.modify i (· + a[i]!)
  return acc

/-- [states, d ≤ k] for option o (0 plain, 1 lastF, 2 lastFB) from a 36-count array. -/
def leK (a : Array Nat) (o k : Nat) : Nat := ((List.range (k + 1)).map fun v => a[o * W + v]!).sum
def nOf (a : Array Nat) : Nat := leK a 0 11

/-- The DRM xcye. -/
def isDrm (c e : Nat) (f : F2) : Bool := f.c == c && f.e == e

/-- [states, ≤ 5, ≤ 6, ≤ 7] of the states of DRM xcye with `p`. -/
def cell (c e : Nat) (p : F2 → Bool) : List Nat :=
  let a := sumWhere fun f => isDrm c e f && p f
  [nOf a, leK a 0 5, leK a 0 6, leK a 0 7]

/-- Strict separation of a key in DRM xcye: the number of states in key cells whose sub-7 rate is under 10% or
over 50%, and the DRM's states. -/
def strict (c e : Nat) (key : F2 → List Nat) : Nat × Nat := Id.run do
  let sub := T.groups.filter fun g => isDrm c e g.1
  let mut cells : Std.HashMap (List Nat) (Nat × Nat) := {}
  for (f, a) in sub do
    let k := key f
    let (n, h) := cells.getD k (0, 0)
    cells := cells.insert k (n + nOf a, h + leK a 0 6)
  let mut good := 0
  let mut tot := 0
  for (_, (n, h)) in cells.toList do
    tot := tot + n
    if h * 10 < n || h * 2 > n then good := good + n
  return (good, tot)

end full
end EOSwitch
