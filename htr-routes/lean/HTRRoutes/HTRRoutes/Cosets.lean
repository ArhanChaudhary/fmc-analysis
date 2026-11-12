/-
  HTRRoutes.Cosets — the 29,400 HTR cosets (420 corner cosets × 70 edge patterns), the shortest linear DR → HTR of
  each, the 48 subset names, and the labels of single scrambles.

  An HTR coset is (corner coset, edge pattern): the corner coset of `Corners.lean` and the mask of places holding
  M pieces.  It is "the state up to renaming its pieces by an HTR element" (an HTR element keeps M pieces among
  M pieces, so the mask does not change).  A move acts on the right: (coset of r, mask) ↦ (coset of r·m, mask·m);
  `cosetActionOk` checks that this does not depend on the representative.  State x = k · 256 + mask, k = 0 … 419
  the coset's number (its representative's place in `REPS`).  `bfs` from the coset of the solved cube with the
  ten DR moves gives the shortest DR → HTR of every coset (moves applied after the state: a linear HTR on the side
  the state is read on), checked by `search.ruleHolds`.

  Labels, as in the research (`class.rs`, `model.rs`, `sticker.py`):
    frame     with more than 4 bad corners, or 4 and more than 4 bad edges, count 8 - n of each
    label     "<corner subset> <bad edges>e" with the 14 corner names ("4a3 2e")
    label48   "<n><letter><qt> <bad edges>e" with letter a/b only for 4 bad corners and qt ≤ 2 or 5, else c
              (Mallard's 48 subsets: 4a3 and 4b3 are both "4c3", 4a4 and 4b4 both "4c4")
-/
import HTRRoutes.Corners
import HTRRoutes.Parse

set_option compiler.extract_closed false

namespace HTRRoutes
namespace cosets
open pieces corners

/-- Number of each representative (0 … 419), by rank of the representative. -/
def KOF : Array Nat := Id.run do
  let mut a := Array.replicate NC 0
  for k in [0:REPS.size] do a := a.set! REPS[k]! k
  return a
/-- Number of the coset of rank r. -/
def cid (r : Nat) : Nat := KOF[REP[r]!]!

/-- `CCM[k][m]`: the coset of (representative k then m). -/
def CCM : Array (Array Nat) := REPS.map fun r => (Array.range 10).map fun m => cid (step r m)
/-- `MM[m][mask]`. -/
def MM : Array (Array Nat) := (Array.range 10).map fun m => (Array.range 256).map (maskMv EMOV[m]!)

def cosetActionOk : Bool :=
  REPS.size == 420 && (List.range NC).all fun r => (List.range 10).all fun m => cid (step r m) == CCM[cid r]![m]!

def N : Nat := 420 * 256
def stepWith (ccm mm : Array (Array Nat)) (x m : Nat) : Nat := ccm[x / 256]![m]! * 256 + mm[m]![x % 256]!
def GOAL : Nat := cid 0 * 256 + mMask (ident 8)

/-- The frame: (bad corners, bad edges) counted as the community does. -/
def frame (nc ne : Nat) : Nat × Nat := if nc > 4 || (nc == 4 && ne > 4) then (8 - nc, 8 - ne) else (nc, ne)

/-- The label of corner rank r with edge pattern mask ("4a3 2e"). -/
def label (r mask : Nat) : String :=
  let (_, ne) := frame NBAD[r]! (ebad mask)
  s!"{NAMES[sub r]!} {ne}e"

/-- The 48-subset name of corner rank r with edge pattern mask ("4c3 2e"). -/
def label48 (r mask : Nat) : String :=
  let (nc, ne) := frame NBAD[r]! (ebad mask)
  let q := qt r
  let letter := if nc == 4 && (q ≤ 2 || q == 5) then (if SHAPEA[r]! then "a" else "b") else "c"
  s!"{nc}{letter}{q} {ne}e"

structure Result where
  rule : Bool
  states : Nat
  /-- (48-subset name, shortest linear HTR, how many cosets), sorted -/
  table : List (String × Nat × Nat)
  deriving DecidableEq, Repr

@[noinline] def tally (d : ByteArray) : Nat × List (String × Nat × Nat) := Id.run do
  let mut states := 0
  let mut rows : List (String × Nat) := []
  for x in [0:N] do
    if !search.reached d x then continue
    states := states + 1
    rows := (label48 REPS[x / 256]! (x % 256), (d.get! x).toNat) :: rows
  let keys := rows.eraseDups
  let tab := keys.map fun k => (k.1, k.2, rows.count k)
  return (states, tab.mergeSort parse.rowLe)

def run : Result :=
  let st := stepWith CCM MM
  let d := search.bfs N [GOAL] (List.range 10) st
  let (n, t) := tally d
  ⟨search.ruleHolds N (· == GOAL) (List.range 10) st d, n, t⟩

/-! ### Single scrambles -/

/-- The inverse of a move sequence ("R U2 F'" ↦ "F R U2'"... written with ' and 2 the usual way). -/
def invMove (m : String) : String :=
  if m.endsWith "2" then m else if m.endsWith "'" then String.ofList m.toList.dropLast else m ++ "'"
def invSeq (s : String) : String := " ".intercalate ((cube.parse s).reverse.map invMove)

/-- (48-subset name, label, label of the inverse) of the state a scramble gives, on the sticker model.
The typographic ’ is read as '. -/
def scrambleLabels (scr : String) : String × String × String :=
  let scr := scr.replace "’" "'"
  let s := cube.do_ cube.SOLVED scr
  let si := cube.do_ cube.SOLVED (invSeq scr)
  let r := rank (corners s)
  let ri := rank (corners si)
  (label48 r (mMask (edges s)), label r (mMask (edges s)), label ri (mMask (edges si)))

end cosets
end HTRRoutes
