/-
  EODR.Layouts — bad-edge layouts: the exact number of edge states with each (F/B, R/L, U/D) triple of bad-edge
  counts (the research's `eodrtools eo layouts`, `out/eo_layouts.tsv`).

  An edge state = which piece is at each of the 12 edge places and how each is turned.  Describe a piece's turn by
  its F/B orientation o (1 = bad for F/B).  `badAt Y k p o` = is piece p, at place k with F/B orientation o, bad
  for axis Y?  It is read off the sticker model: put p's F/B reference sticker on k's F/B reference sticker (o = 0)
  or on the other one (o = 1), and apply the EO rule of `Pieces.lean` for Y.  The theorems check three facts about
  it, over all 12 x 12 x 2 cases and the three axes:
    * for Y = F/B it is o itself;
    * turning the piece over (o ↦ 1 - o) changes it on every axis;
    * it depends on the piece only through the piece's kind (E, M or S slice).
  So the three bad counts of a state depend only on the kind of piece at each place and on the 12 F/B bits f:
  bad_Y = popcount(f xor mask_Y), mask_Y = the places where a piece of that kind with o = 0 is bad for Y.

  The space counted (as in the research): the 34,650 ways to place four E, four M and four S pieces on the 12 places,
  times the 2,048 F/B orientation vectors with an even number of bad edges = 70,963,200 configurations; each
  stands for 4!³ edge permutations, so the counts below divided by 70,963,200 are the probabilities over all
  12!·2¹¹ edge states.  (That a face turn changes F/B goodness of 0 or 4 edges is `flip_table`; that every one of
  those 12!·2¹¹ states occurs on the cube is the usual fact, not proved here.)
-/
import EODR.Pieces

set_option compiler.extract_closed false

namespace EODR
namespace layouts
open pieces

/-- Is piece p (named by its home place), sitting at place k with F/B orientation o, bad for axis Y? -/
def badAt (Y k p o : Nat) : Bool :=
  let a := ref 2 p                                    -- the piece's F/B reference sticker
  let b := other 2 p
  let (onRef, onOther) := if o == 0 then (a, b) else (b, a)   -- what sits on k's F/B reference / other sticker
  let h := if ref Y k == ref 2 k then onRef else onOther      -- what sits on k's Y reference sticker
  !(REF Y).contains h

/-- One piece of each kind (0 M, 1 E, 2 S): the first place of that kind. -/
def rep (t : Nat) : Nat := ((List.range 12).find? fun p => kind p == t).getD 12

/-- All placements of the kinds: lists of 12 kinds with four of each. -/
def arrangements : List (List Nat) :=
  let rec go : Nat → Nat → Nat → Nat → List (List Nat)
    | 0, _, _, _ => [[]]
    | i + 1, a, b, c =>
      (if a > 0 then (go i (a - 1) b c).map (0 :: ·) else []) ++
      (if b > 0 then (go i a (b - 1) c).map (1 :: ·) else []) ++
      (if c > 0 then (go i a b (c - 1)).map (2 :: ·) else [])
  go 12 4 4 4

/-- mask_Y of a placement. -/
def mask (Y : Nat) (kinds : List Nat) : Nat := Id.run do
  let mut m := 0
  for k in [0:12] do
    if badAt Y k (rep kinds[k]!) 0 then m := m + 2 ^ k
  return m

-- Tables used inside the loop.  They are top-level constants (computed once) on purpose: a `let` inside the loop's
-- function can be inlined by the compiler into the loop body and recomputed at every step.
/-- popcount of each 12-bit number -/
def POP : Array Nat := (Array.range 4096).map popcount
/-- the 2,048 F/B orientation vectors with an even number of 1s -/
def EVENS : Array Nat := (Array.range 4096).filter fun f => POP[f]! % 2 == 0

/-- `count n` looks at the first n placements (the theorems use n = 34650, all of them; the parameter is
there only so that the compiled function is called with an argument).  The result: ((bad F/B, bad R/L, bad U/D), number of configurations), for the triples that occur, in
increasing order; and the number of configurations looked at. -/
def count (n : Nat) : List ((Nat × Nat × Nat) × Nat) × Nat := Id.run do
  let pop := POP
  let evens := EVENS
  let mut h : Array Nat := Array.replicate (13 * 13 * 13) 0
  let mut tot := 0
  for kinds in arrangements.take n do
    let mfb := mask 2 kinds
    let mrl := mask 0 kinds
    let mud := mask 1 kinds
    for f in evens do
      let i := (pop[f ^^^ mfb]! * 13 + pop[f ^^^ mrl]!) * 13 + pop[f ^^^ mud]!
      h := h.modify i (· + 1)
      tot := tot + 1
  let mut out := []
  for i in [0:13 * 13 * 13] do
    if h[i]! != 0 then out := out ++ [((i / 169, (i / 13) % 13, i % 13), h[i]!)]
  return (out, tot)

/-! Readings of the table -/

abbrev Table := List ((Nat × Nat × Nat) × Nat)

def total (t : Table) : Nat := (t.map (·.2)).sum
/-- Configurations whose triple satisfies P. -/
def countIf (t : Table) (P : Nat → Nat → Nat → Bool) : Nat :=
  ((t.filter fun ((a, b, c), _) => P a b c).map (·.2)).sum
/-- Configurations whose triple, sorted, is x ≤ y ≤ z. -/
def sortedCount (t : Table) (x y z : Nat) : Nat :=
  countIf t fun a b c => [a, b, c].mergeSort (· ≤ ·) == [x, y, z]
/-- The distribution of the sum of the three counts: (sum, configurations). -/
def sumHist (t : Table) : List (Nat × Nat) :=
  ((List.range 37).map fun s => (s, countIf t fun a b c => a + b + c == s)).filter (·.2 != 0)
/-- The triples that occur. -/
def triples (t : Table) : List (Nat × Nat × Nat) := t.map (·.1)

end layouts
end EODR
