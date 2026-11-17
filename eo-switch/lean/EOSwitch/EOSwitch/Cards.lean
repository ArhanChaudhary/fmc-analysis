/-
  EOSwitch.Cards — part G of README.md (added 2026-11-16): the reads, the switch cards and the current policies
  of the second version of the study (research/v2/cards.py), defined on the model of Switch.lean / Full.lean, with
  the table every count of CardsThm.lean is read from.

  The reads the cards add to those of Switch.lean and Full.lean (research: `src/features.py`, `v2/feat2.py`):
    * a *hole* is an E-slice place holding a U/D piece (no E-slice piece in it).  `holeCfg` (research `hole_cfg`),
      for exactly two holes: 0 when both are on one R/L face (the two places have the same x), 2 when both are on
      one F/B face (the same z), 1 when they are diagonal; 3 when there are not exactly two holes;
    * `udSplit` (research `ud_split`): the larger of the numbers of bad corners in the U layer and in the D layer
      ("corners 2 and 2 in the layers" is 2 for four bad corners, "3 and 3" is 3 for six);
    * `edgesSameLayer` (research `edges_same_layer`): at least two bad U/D edges, all in the U layer or all in the D
      layer;
    * `colsBad` (research `cols_bad`): a *column* is the two corner places above and below one E-slice place; the
      number of columns whose two corners are both bad ("4a corners in two columns" is 2);
    * `dfbr`: wen's "D F2 B2 R case" as rules.py reads it: the states solved by one U or D turn, then F2 B2, then an
      R or L quarter turn.  They are the states reached from DR by an R or L quarter turn, F2, B2 and one U or D
      turn (`DFBR`); CardsThm.lean shows there are 12, all 4c4e with no pair, no fake pair and a DR in 4.
  Reused: bad corners, the U/D sticker axis, pairs, fake pairs, side pairs, paired edges, ARM, JZP (`sw.feat`);
  corner case and suffix, split pairs, anti-AR, "4a one U/D turn from 4d" (`full`).

  A *group row* is [states, DR in 4 or less, DR in 5, DR in 6, DR in 7, DR longer than 7].
  A *policy row* is [states switched, DR in 4 or less not switched, DR in 5 not switched, DR in 6 not switched,
  switched with a DR of 7 or longer].
  A card is an ordered list of groups, and the first group whose property holds takes the state (research: the
  groups are disjoint as written, except those it writes "+…, anything else", which take what the earlier groups
  left of their property; `overlap` counts the states for which the two readings would differ).
-/
import EOSwitch.Full
import Std.Data.HashMap

set_option compiler.extract_closed false

namespace EOSwitch
namespace cards
open cube pieces sw full

/-! ### The reads the cards add -/

/-- The holes: E-slice places with no E-slice piece in them. -/
def holes (m : Nat) : List Nat := E_SLOTS.filter fun k => !holdsE m k

/-- Two holes: 0 on one R/L face, 1 diagonal, 2 on one F/B face.  3 when there are not exactly two holes. -/
def holeCfg (m : Nat) : Nat :=
  match holes m with
  | [a, b] => if (EV a)[0]! == (EV b)[0]! then 0 else if (EV a)[2]! == (EV b)[2]! then 2 else 1
  | _ => 3

/-- The larger of the numbers of bad corners in the U layer and in the D layer. -/
def udSplit (co : Nat) : Nat := let b := badList co; let u := b.countP onU; max u (b.length - u)

/-- At least two bad U/D edges, all in the U layer or all in the D layer. -/
def edgesSameLayer (m : Nat) : Bool :=
  let out := UD_PLACES.filter (holdsE m)
  out.length ≥ 2 && (out.all (fun k => (EV k)[1]! > 0) || out.all (fun k => (EV k)[1]! < 0))

/-- Columns (the two corners next to an E-slice place, one above and one below it) whose two corners are both bad. -/
def colsBad (co : Nat) : Nat := E_SLOTS.countP fun k => NB[k]!.all (bad co)

/-- wen's "D F2 B2 R" cases: from DR, an R or L quarter turn (6 R, 8 R', 9 L, 11 L'), F2 (13), B2 (16), one U or
D turn (0 … 5).  Such a state is solved by the U or D turn back, B2 F2, and the quarter turn back. -/
def DFBR : List Nat :=
  let st := step COT MT
  ([6, 8, 9, 11].flatMap fun y => (List.range 6).map fun x => st (st (st (st GOAL y) 13) 16) x).eraseDups

def UDS : Array Nat := (Array.range 6561).map udSplit
def COLS : Array Nat := (Array.range 6561).map colsBad
def HC : Array Nat := (Array.range 4096).map holeCfg
def ESL : Array Bool := (Array.range 4096).map edgesSameLayer

/-! ### The record of reads -/

structure Rd where
  /-- bad corners -/
  c : Nat
  /-- 2 × bad U/D edges -/
  e : Nat
  carm : Nat
  earm : Nat
  pairs : Nat
  fake : Nat
  side : Nat
  /-- paired edges: bad U/D edges with at least one pair -/
  ep : Nat
  /-- corner case: 0 a, 1 b, 2 c, 3 d; 4 when not 4 bad corners -/
  cc : Nat
  /-- suffix ("4b-0": cc = 1, suf = 0); 7 when not 4 bad corners -/
  suf : Nat
  /-- holes: 0 on one R/L face, 1 diagonal, 2 on one F/B face; 3 when not two holes -/
  hc : Nat
  /-- corners per layer: the larger count -/
  uds : Nat
  /-- all bad U/D edges in one layer (and at least two) -/
  esl : Bool
  /-- wen's split pairs -/
  split : Nat
  jzp : Bool
  /-- anti-AR: every bad corner and every bad U/D edge out of AR -/
  anti : Bool
  /-- 4a corners, one U or D turn from 4d corners -/
  a1d : Bool
  /-- one of the "D F2 B2 R" cases -/
  dfbr : Bool
  /-- columns with both corners bad -/
  cols : Nat
  deriving DecidableEq, Repr, Inhabited

/-- Field widths in bits, in the order of the structure. -/
def WIDTHS : List Nat := [4, 3, 4, 3, 4, 4, 4, 3, 3, 3, 2, 4, 1, 4, 1, 1, 1, 1, 3]

def fields (f : Rd) : List Nat :=
  [f.c, f.e / 2, f.carm, f.earm, f.pairs, f.fake, f.side, f.ep, f.cc, f.suf, f.hc, f.uds, full.b2n f.esl, f.split,
   full.b2n f.jzp, full.b2n f.anti, full.b2n f.a1d, full.b2n f.dfbr, f.cols]

def pack (f : Rd) : Nat := (List.zip (fields f) WIDTHS).foldr (fun (v, w) acc => acc * 2 ^ w + v) 0

def unpack (k : Nat) : Rd := Id.run do
  let mut k := k
  let mut out : Array Nat := #[]
  for w in WIDTHS do
    out := out.push (k % 2 ^ w)
    k := k / 2 ^ w
  let g := fun i => out[i]!
  return { c := g 0, e := 2 * g 1, carm := g 2, earm := g 3, pairs := g 4, fake := g 5, side := g 6, ep := g 7,
           cc := g 8, suf := g 9, hc := g 10, uds := g 11, esl := g 12 == 1, split := g 13, jzp := g 14 == 1,
           anti := g 15 == 1, a1d := g 16 == 1, dfbr := g 17 == 1, cols := g 18 }

def fits (f : Rd) : Bool := (List.zip (fields f) WIDTHS).all fun (v, w) => v < 2 ^ w

/-- The reads of state x = co · 4096 + m. -/
def rd (x : Nat) : Rd :=
  let co := x / 4096
  let m := x % 4096
  let f := feat co m
  { c := f.c, e := f.e, carm := f.carm, earm := f.earm, pairs := f.pairs, fake := f.fake, side := f.side,
    ep := f.edgesPaired, cc := CC[co]!, suf := SUF[co]!, hc := HC[m]!, uds := UDS[co]!, esl := ESL[m]!,
    split := splitPairs co m, jzp := f.jzp,
    anti := f.carm == f.c && 2 * f.earm == f.e && f.c > 0,
    a1d := A1D[co]!, dfbr := DFBR.contains x, cols := COLS[co]! }

/-! ### The table of groups -/

/-- Histogram length (DR in 0 … 11). -/
def W : Nat := 12

structure Table where
  /-- states reached by the BFS -/
  states : Nat
  /-- every state's reads fit the field widths, and `unpack ∘ pack` gives them back -/
  packs : Bool
  /-- each record of reads that occurs, with its states by DR length 0 … 11 -/
  groups : Array (Rd × Array Nat)

/-- Separate and not inlined, on purpose (see Switch.lean). -/
@[noinline] def build (d : ByteArray) : Table := Id.run do
  let mut idx : Std.HashMap Nat Nat := {}
  let mut keys : Array Nat := #[]
  let mut h : Array (Array Nat) := #[]
  let mut states := 0
  let mut ok := true
  for x in [0:N] do
    if !search.reached d x then continue
    states := states + 1
    let f := rd x
    let k := pack f
    if !(fits f && unpack k == f) then ok := false
    let v := (d.get! x).toNat
    let mut i := 0
    match idx.get? k with
    | some j => i := j
    | none =>
      i := keys.size
      idx := idx.insert k i
      keys := keys.push k
      h := h.push (Array.replicate W 0)
    h := h.modify i fun a => a.modify v (· + 1)
  let groups := (Array.range keys.size).map fun i => (unpack keys[i]!, h[i]!)
  return ⟨states, ok, groups⟩

def T : Table := build dist

/-! ### Readings -/

/-- States by DR length 0 … 11, over the records with `p`. -/
def sumWhere (p : Rd → Bool) : Array Nat := Id.run do
  let mut acc := Array.replicate W 0
  for (f, a) in T.groups do
    if p f then
      for i in [0:W] do acc := acc.modify i (· + a[i]!)
  return acc

def span (a : Array Nat) (lo hi : Nat) : Nat := ((List.range (hi - lo)).map fun i => a[lo + i]!).sum

/-- A group row: [states, DR in 4 or less, in 5, in 6, in 7, longer]. -/
def rowOf (a : Array Nat) : List Nat := [span a 0 W, span a 0 5, a[5]!, a[6]!, a[7]!, span a 8 W]

def isDrm (c e : Nat) (f : Rd) : Bool := f.c == c && f.e == e

/-- The group row of the states of DRM xcye with `p`. -/
def row (c e : Nat) (p : Rd → Bool) : List Nat := rowOf (sumWhere fun f => isDrm c e f && p f)

/-- The policy row of a switch set on DRM xcye: [switched, DR in 4 or less not switched, DR in 5 not switched,
DR in 6 not switched, switched with a DR of 7 or longer]. -/
def pol (c e : Nat) (sw : Rd → Bool) : List Nat :=
  let s := row c e sw
  let n := row c e fun f => !sw f
  [s[0]!, n[1]!, n[2]!, n[3]!, s[4]! + s[5]!]

/-! ### Cards -/

structure Group where
  label : String
  /-- "switch", "time" (the next ones to add with time to spare) or "skip" -/
  verdict : String
  /-- the research writes this group as what the earlier groups left of its property -/
  rest : Bool
  p : Rd → Bool

def G (label verdict : String) (p : Rd → Bool) : Group := ⟨label, verdict, false, p⟩
/-- A group that takes what the earlier groups left of its property. -/
def G' (label verdict : String) (p : Rd → Bool) : Group := ⟨label, verdict, true, p⟩
def anything : Group := ⟨"anything else", "skip", true, fun _ => true⟩

/-- Each group with the property it has on the card: its own, and no earlier group's. -/
def firstMatch (gs : List Group) : List (Group × (Rd → Bool)) :=
  let rec go (rs : List Group) (taken : Rd → Bool) : List (Group × (Rd → Bool)) :=
    match rs with
    | [] => []
    | g :: t => (g, fun f => !taken f && g.p f) :: go t (fun f => taken f || g.p f)
  go gs (fun _ => false)

/-- The card's rows: (label, verdict, group row), first match wins. -/
def cardRows (c e : Nat) (gs : List Group) : List (String × String × List Nat) :=
  (firstMatch gs).map fun (g, q) => (g.label, g.verdict, row c e q)

/-- States of the DRM that have the property of a group not marked `rest` and of an earlier group too. -/
def overlap (c e : Nat) (gs : List Group) : Nat :=
  let rec go (rs : List Group) (taken : Rd → Bool) : Nat :=
    match rs with
    | [] => 0
    | g :: t => (if g.rest then 0 else (row c e fun f => taken f && g.p f)[0]!) + go t (fun f => taken f || g.p f)
  go gs (fun _ => false)

/-- States of the DRM that no group takes. -/
def uncovered (c e : Nat) (gs : List Group) : Nat := (row c e fun f => !(gs.any fun g => g.p f))[0]!

/-- The states the card switches: its groups with one of the verdicts `vs`. -/
def cardSet (gs : List Group) (vs : List String) : Rd → Bool :=
  let fm := (firstMatch gs).filter fun (g, _) => vs.contains g.verdict
  fun f => fm.any fun (_, q) => q f

def armIs (a : Nat) (f : Rd) : Bool := f.carm * 10 + f.earm == a
def armIn (l : List Nat) (f : Rd) : Bool := l.contains (f.carm * 10 + f.earm)

/-- 4c4e (research/v2/cards.py, in its order). -/
def CARD44 : List Group :=
  [G "3 or 4 pairs" "switch" fun f => f.pairs ≥ 3,
   G "2 pairs on two edges" "switch" fun f => f.pairs == 2 && f.ep == 2,
   G "2 pairs on one edge (a bar), holes on one R/L face" "switch" fun f => f.pairs == 2 && f.ep == 1 && f.hc == 0,
   G "2 pairs on one edge (a bar), holes not on one R/L face, 2 fake pairs" "switch" fun f =>
     f.pairs == 2 && f.ep == 1 && f.hc ≥ 1 && f.fake == 2,
   G "1 pair, ARM 21, 4d corners" "switch" fun f => f.pairs == 1 && armIs 21 f && f.cc == 3,
   G "1 pair, ARM 21, 4b corners, 0 or 2 side pairs" "switch" fun f =>
     f.pairs == 1 && armIs 21 f && f.cc == 1 && f.side != 1,
   G "1 pair, ARM 20, 21 or 22, 4a corners in two columns, 1+ side pairs" "switch" fun f =>
     f.pairs == 1 && f.carm == 2 && f.cc == 0 && f.cols == 2 && f.side ≥ 1,
   G "0 pairs, no fake pairs, corners 2 and 2 in the layers" "switch" fun f =>
     f.pairs == 0 && f.fake == 0 && f.uds == 2,
   G "2 pairs on one edge (a bar), holes not on one R/L face, 0 or 1 fake pairs" "time" fun f =>
     f.pairs == 2 && f.ep == 1 && f.hc ≥ 1 && f.fake ≤ 1,
   G "1 pair, ARM 10 or 11, 2 or 3 side pairs" "time" fun f =>
     f.pairs == 1 && armIn [10, 11] f && f.side ≥ 2,
   G "1 pair, ARM 20, 21 or 22, 4a corners in two columns, no side pair" "skip" fun f =>
     f.pairs == 1 && f.carm == 2 && f.cc == 0 && f.cols == 2 && f.side == 0,
   G "1 pair, ARM 20, 21 or 22, 4a corners not in two columns" "skip" fun f =>
     f.pairs == 1 && f.carm == 2 && f.cc == 0 && f.cols != 2,
   G "1 pair, ARM 21, 4b corners, exactly 1 side pair" "skip" fun f =>
     f.pairs == 1 && armIs 21 f && f.cc == 1 && f.side == 1,
   G' "1 pair, anything else" "skip" fun f => f.pairs == 1,
   G' "0 pairs, anything else" "skip" fun f => f.pairs == 0]

/-- 4c2e. -/
def CARD42 : List Group :=
  [G "2 pairs (a bar)" "switch" fun f => f.pairs == 2,
   G "1 pair and a side pair" "switch" fun f => f.pairs == 1 && f.side ≥ 1,
   G "0 pairs, JZP (ARM 00) with 4b corners" "switch" fun f => f.pairs == 0 && armIs 0 f && f.cc == 1,
   G "1 pair, no side pair, 4b-0 corners" "switch" fun f => f.pairs == 1 && f.side == 0 && f.cc == 1 && f.suf == 0,
   G "1 pair, no side pair, 4a-2 corners" "time" fun f => f.pairs == 1 && f.side == 0 && f.cc == 0 && f.suf == 2,
   G "1 pair, no side pair, ARM 31" "time" fun f =>
     f.pairs == 1 && f.side == 0 && armIs 31 f && !(f.cc == 0 && f.suf == 2) && !(f.cc == 1 && f.suf == 0),
   G' "1 pair, anything else" "skip" fun f => f.pairs == 1,
   G' "0 pairs, anything else" "skip" fun f => f.pairs == 0]

/-- 3c2e (wen's rule). -/
def CARD32 : List Group :=
  [G "1 pair" "switch" fun f => f.pairs == 1,
   G "0 pairs, a fake pair or a split pair" "switch" fun f => f.pairs == 0 && (f.fake ≥ 1 || f.split ≥ 1),
   G "0 pairs, no fake pair, no split pair" "time" fun f => f.pairs == 0 && f.fake == 0 && f.split == 0]

/-- 7c8e. -/
def CARD78 : List Group :=
  [G "6 pairs, not ARM 64" "switch" fun f => f.pairs == 6 && !armIs 64 f,
   G "5 pairs, not ARM 20 or 54" "switch" fun f => f.pairs == 5 && !armIn [20, 54] f,
   G "4 pairs, ARM 21, 31 or 43" "switch" fun f => f.pairs == 4 && armIn [21, 31, 43] f,
   G "3 pairs, ARM 21" "switch" fun f => f.pairs == 3 && armIs 21 f,
   G "4 pairs, ARM 11, 12, 33, 41 or 62" "time" fun f => f.pairs == 4 && armIn [11, 12, 33, 41, 62] f,
   G' "4 pairs, anything else" "skip" fun f => f.pairs == 4,
   G' "5 or 6 pairs with ARM 20, 54 or 64" "skip" fun f => f.pairs ≥ 5,
   G' "3 pairs or fewer" "skip" fun f => f.pairs ≤ 3]

/-- 8c8e. -/
def CARD88 : List Group :=
  [G "8 pairs" "switch" fun f => f.pairs == 8,
   G "6 pairs, corner ARM 4" "switch" fun f => f.pairs == 6 && f.carm == 4,
   G "5 pairs, edge ARM 1 or 3" "switch" fun f => f.pairs == 5 && (f.earm == 1 || f.earm == 3),
   G "2 pairs, ARM 42" "switch" fun f => f.pairs == 2 && armIs 42 f,
   G "4 pairs, ARM 42" "switch" fun f => f.pairs == 4 && armIs 42 f,
   G "4 pairs, ARM 02, 43, 63 or 82" "time" fun f => f.pairs == 4 && armIn [2, 43, 63, 82] f,
   G' "6 pairs, corner ARM not 4" "skip" fun f => f.pairs == 6,
   G' "5 pairs, edge ARM 2" "skip" fun f => f.pairs == 5,
   anything]

/-- 2c2e. -/
def CARD22 : List Group :=
  [G "1 pair" "switch" fun f => f.pairs == 1,
   G "2 pairs and a side pair" "switch" fun f => f.pairs == 2 && f.side ≥ 1,
   G "0 pairs, 1 side pair, ARM 00 or 11" "switch" fun f => f.pairs == 0 && f.side == 1 && armIn [0, 11] f,
   G "0 pairs, JZP (ARM 00), no side pair" "time" fun f => f.pairs == 0 && f.side != 1 && armIs 0 f,
   anything]

/-- 4c6e. -/
def CARD46 : List Group :=
  [G "4 pairs on three edges" "switch" fun f => f.pairs == 4 && f.ep == 3,
   G "3 pairs, JZP (ARM 00)" "switch" fun f => f.pairs == 3 && armIs 0 f,
   G "3 pairs on three edges, the three bad edges in one layer" "switch" fun f =>
     f.pairs == 3 && !armIs 0 f && f.ep == 3 && f.esl,
   G "3 pairs on three edges, corners 2 and 2 in the layers" "switch" fun f =>
     f.pairs == 3 && !armIs 0 f && f.ep == 3 && !f.esl && f.uds == 2,
   anything]

/-- 3c4e. -/
def CARD34 : List Group :=
  [G "2 pairs and a side pair" "switch" fun f => f.pairs == 2 && f.side ≥ 1,
   G "2 pairs, no side pair, a fake pair" "switch" fun f => f.pairs == 2 && f.side == 0 && f.fake ≥ 1,
   G "1 pair, 2 side pairs" "switch" fun f => f.pairs == 1 && f.side == 2,
   G "1 pair, ARM 21, 1 side pair, 2 fake pairs or holes on one R/L face" "switch" fun f =>
     f.pairs == 1 && armIs 21 f && f.side == 1 && (f.fake == 2 || f.hc == 0),
   G "1 pair, ARM 21, 1 side pair, the rest" "time" fun f =>
     f.pairs == 1 && armIs 21 f && f.side == 1 && !(f.fake == 2 || f.hc == 0),
   anything]

/-- 3c6e. -/
def CARD36 : List Group :=
  [G "2 pairs, ARM 21, 1 or 2 fake pairs" "switch" fun f => f.pairs == 2 && armIs 21 f && f.fake ≥ 1,
   G "2 pairs, ARM 12, 2 fake pairs" "switch" fun f => f.pairs == 2 && armIs 12 f && f.fake == 2,
   G "2 pairs, ARM 01" "switch" fun f => f.pairs == 2 && armIs 1 f,
   anything]

/-- 5c4e. -/
def CARD54 : List Group :=
  [G "3 pairs, 2+ side pairs" "switch" fun f => f.pairs == 3 && f.side ≥ 2,
   G "2 pairs, ARM 21, 2+ side pairs" "switch" fun f => f.pairs == 2 && armIs 21 f && f.side ≥ 2,
   G "1 pair, ARM 21, 2+ side pairs, 2+ fake pairs" "switch" fun f =>
     f.pairs == 1 && armIs 21 f && f.side ≥ 2 && f.fake ≥ 2,
   G "3 pairs, 0 or 1 side pair" "time" fun f => f.pairs == 3 && f.side ≤ 1,
   anything]

/-- 5c6e. -/
def CARD56 : List Group :=
  [G "4 pairs" "switch" fun f => f.pairs == 4,
   G "3 pairs, ARM 21, 3 side pairs" "switch" fun f => f.pairs == 3 && armIs 21 f && f.side == 3,
   G "2 pairs, ARM 21, 3 side pairs" "switch" fun f => f.pairs == 2 && armIs 21 f && f.side == 3,
   G "3 pairs, ARM 21, fewer than 3 side pairs" "time" fun f => f.pairs == 3 && armIs 21 f && f.side != 3,
   anything]

/-- 6c6e. -/
def CARD66 : List Group :=
  [G "5 or 6 pairs" "switch" fun f => f.pairs ≥ 5,
   G "3 pairs, 3 fake pairs, corners 3 and 3 in the layers" "switch" fun f =>
     f.pairs == 3 && f.fake == 3 && f.uds == 3,
   anything]

/-! ### The current policies (research/v2/cards.py BASE, with the rules of research/src/rules.py) -/

def never (_ : Rd) : Bool := false
def always (_ : Rd) : Bool := true

/-- 4c4e.  "pairs": 2+ pairs.  "pairs+case" (tseitsei89): 2+ pairs, or 1 pair with 4d corners.  "pairs+case2"
(rodneykinney): 3-4 pairs; 2 pairs unless 4b-0; 1 pair if 4d; 0 pairs if 4a-0 or 4d with no fake pairs.  "wen": 2+
pairs; 1 pair if 4d or 4a one U/D turn from 4d; 0 pairs if anti-AR or a "D F2 B2 R" case.  "chart" (caycala): 3-4
pairs; 2 pairs with ARM 10, 11, 20, 21, 31, 32, or ARM 42 with 4a corners; 1 pair with ARM 21; 0 pairs with ARM 42.
"pairs+arm" (Fanti): 2+ pairs; 1 pair with ARM 21; 0 pairs with JZP or ARM 42. -/
def BASE44 : List (String × (Rd → Bool)) :=
  [("pairs", fun f => f.pairs ≥ 2),
   ("pairs+case", fun f => f.pairs ≥ 2 || (f.pairs == 1 && f.cc == 3)),
   ("pairs+case2", fun f => f.pairs ≥ 3 || (f.pairs == 2 && !(f.cc == 1 && f.suf == 0)) || (f.pairs == 1 && f.cc == 3) ||
      (f.pairs == 0 && ((f.cc == 0 && f.suf == 0) || f.cc == 3) && f.fake == 0)),
   ("wen", fun f => f.pairs ≥ 2 || (f.pairs == 1 && (f.cc == 3 || f.a1d)) || (f.pairs == 0 && (f.anti || f.dfbr))),
   ("chart", fun f => f.pairs ≥ 3 ||
      (f.pairs == 2 && (armIn [10, 11, 20, 21, 31, 32] f || (armIs 42 f && f.cc == 0))) ||
      (f.pairs == 1 && armIs 21 f) || (f.pairs == 0 && armIs 42 f)),
   ("pairs+arm", fun f => f.pairs ≥ 2 || (f.pairs == 1 && armIs 21 f) || (f.pairs == 0 && (f.jzp || armIs 42 f)))]

/-- 4c2e.  "pairs": 1.5+ pairs (pairs + side pairs / 2 ≥ 1.5).  "pairs+case" (rodneykinney): 2 pairs unless 4a-0 or
4a-4; 1 pair unless 4a-0, 4a-4 or 4b-2.  "pairs+arm" (caycala): 2 pairs; 1 pair with edge ARM 1 or ARM 10; 0 pairs
only JZP.  "pairs+arm2" (Fanti): 1+ pairs; 0 pairs with JZP. -/
def BASE42 : List (String × (Rd → Bool)) :=
  [("pairs", fun f => 2 * f.pairs + f.side ≥ 3),
   ("pairs+case", fun f => (f.pairs == 2 && !(f.cc == 0 && f.suf != 2)) ||
      (f.pairs == 1 && !(f.cc == 0 && f.suf != 2) && !(f.cc == 1 && f.suf == 2))),
   ("pairs+arm", fun f => f.pairs ≥ 2 || (f.pairs == 1 && (f.earm == 1 || armIs 10 f)) || (f.pairs == 0 && f.jzp)),
   ("pairs+arm2", fun f => f.pairs ≥ 1 || f.jzp)]

/-- 3c2e.  "pairs": always.  "wen": a pair, a fake pair or a split pair. -/
def BASE32 : List (String × (Rd → Bool)) :=
  [("pairs", always), ("wen", fun f => f.pairs + f.fake + f.split ≥ 1)]

/-- 7c8e.  "pairs" (tseitsei89): 5+ pairs, or 4 pairs with edge ARM under 2.  "pairs0" (rodneykinney): 5 or 6
pairs.  "chart" (caycala): 5-6 pairs, 4 pairs with ARM 21, 31, 43, 3 pairs with ARM 21, and never edge ARM 4, nor
edge ARM 0 except ARM 10.  "pairs+arm" (Fanti): 5+ pairs; 4 pairs with ARM 21, 31, 43; 3 pairs with ARM 21. -/
def BASE78 : List (String × (Rd → Bool)) :=
  [("pairs", fun f => f.pairs ≥ 5 || (f.pairs == 4 && f.earm < 2)),
   ("pairs0", fun f => f.pairs ≥ 5),
   ("chart", fun f => (f.pairs ≥ 5 || (f.pairs == 4 && armIn [21, 31, 43] f) || (f.pairs == 3 && armIs 21 f)) &&
      !(f.earm == 4 || (f.earm == 0 && !armIs 10 f))),
   ("pairs+arm", fun f => f.pairs ≥ 5 || (f.pairs == 4 && armIn [21, 31, 43] f) || (f.pairs == 3 && armIs 21 f))]

/-- 8c8e.  "pairs" (rodneykinney's tree): 3 or fewer fake pairs, and edge ARM not 2 or 6+ pairs. -/
def BASE88 : List (String × (Rd → Bool)) := [("pairs", fun f => f.fake ≤ 3 && (f.earm != 2 || f.pairs ≥ 6))]
/-- 2c2e.  "pairs": 1+ pairs. -/
def BASE22 : List (String × (Rd → Bool)) := [("pairs", fun f => f.pairs ≥ 1)]
/-- 4c6e.  "pairs": never.  "jzp" (Yura Riabov): only JZP.  "radek" (Radek B): 4 pairs or JZP. -/
def BASE46 : List (String × (Rd → Bool)) :=
  [("pairs", never), ("jzp", fun f => f.jzp), ("radek", fun f => f.pairs ≥ 4 || f.jzp)]
/-- 3c4e.  "pairs": 2+ pairs.  "pairs+arm" (Fanti): 2 pairs; 1 pair with ARM 00 or 21. -/
def BASE34 : List (String × (Rd → Bool)) :=
  [("pairs", fun f => f.pairs ≥ 2), ("pairs+arm", fun f => f.pairs ≥ 2 || (f.pairs == 1 && armIn [0, 21] f))]
/-- 3c6e.  "pairs": never.  "pairs+arm" (Fanti): 3 pairs with ARM 00; 2 pairs with ARM 21. -/
def BASE36 : List (String × (Rd → Bool)) :=
  [("pairs", never), ("pairs+arm", fun f => (f.pairs ≥ 3 && armIs 0 f) || (f.pairs == 2 && armIs 21 f))]
/-- 5c4e.  "pairs": never.  "jay" (Jay): 2 pairs with ARM 21, or 3+ pairs. -/
def BASE54 : List (String × (Rd → Bool)) :=
  [("pairs", never), ("jay", fun f => (f.pairs == 2 && armIs 21 f) || f.pairs ≥ 3)]
/-- 5c6e.  "pairs": never.  "jay" (Jay): 3 pairs with ARM 21, or 4+ pairs. -/
def BASE56 : List (String × (Rd → Bool)) :=
  [("pairs", never), ("jay", fun f => (f.pairs == 3 && armIs 21 f) || f.pairs ≥ 4)]
/-- 6c6e.  "pairs": never. -/
def BASE_NEVER : List (String × (Rd → Bool)) := [("pairs", never)]

/-- The policy rows of a DRM: the card's switch groups ("card"), the card with its "time" groups ("card+time"),
then each current policy. -/
def polRows (c e : Nat) (gs : List Group) (base : List (String × (Rd → Bool))) : List (String × List Nat) :=
  ([("card", cardSet gs ["switch"]), ("card+time", cardSet gs ["switch", "time"])] ++ base).map
    fun (k, sw) => (k, pol c e sw)

/-- The twelve DRMs, each with its card and its current policies, in the order of cards.py. -/
def ALL : List (Nat × Nat × List Group × List (String × (Rd → Bool))) :=
  [(4, 4, CARD44, BASE44), (4, 2, CARD42, BASE42), (3, 2, CARD32, BASE32), (7, 8, CARD78, BASE78),
   (8, 8, CARD88, BASE88), (2, 2, CARD22, BASE22), (4, 6, CARD46, BASE46), (3, 4, CARD34, BASE34),
   (3, 6, CARD36, BASE36), (5, 4, CARD54, BASE54), (5, 6, CARD56, BASE56), (6, 6, CARD66, BASE_NEVER)]

end cards
end EOSwitch
