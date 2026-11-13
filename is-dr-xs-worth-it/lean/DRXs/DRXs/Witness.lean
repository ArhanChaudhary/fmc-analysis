/-
  DRXs.Witness — tools to check the printed examples of the errata and the write-up on the sticker model: the
  kind of a scrambled state, which edges are flipped where, that a printed fix reaches a real DR in its printed
  number of turns, and (for nissy's shortest DRs) a brute-force search for a DR on any axis.
-/
import DRXs.AfterTrigger
import DRXs.Colours
import DRXs.EdgeOrient

namespace DRXs
namespace witness
open cube fecosets aftertrigger edges

/-- The DR the Appendix A scrambles start from (witness.py's D0). -/
def D0 : String := "U R2 F2 D' B2 U2 L2 D"

/-- Number of face turns of a sequence (HTM; a slice written R L counts 2). -/
def len (seq : String) : Nat := (parse seq).length

/-- A real DR on axis a (colours of axis a on the faces of axis a, no flips, slice edges right). -/
def isDRon (s : State) (a : Nat) : Bool := match fe.look s a a with
  | none => false
  | some (fl, sl) => fe.is_dr (a, a, fl, sl)

def isDRany (s : State) : Bool := [0, 1, 2].any (isDRon s)

/-- The flipped layer places of a kind (positions). -/
def flippedAt (g : Sig) : List Vec := ((layer_places g.f).zip g.flips).filterMap fun (p, b) => if b == 1 then some p else none

/-- A Simon / Appendix A row: flipped places, turns as it is, turns after `alt` (U2 or D2), fix.  The state is the
DR D0 followed by the fix backwards.  Checks: it is a DR-1s with corners on F/B whose flipped edges are at the
named places; its fewest turns to DR (kind table) are `turns`; after the group `alt` they are `other`; the fix has
`turns` face turns and brings the state to a real DR. -/
def rowOK (alt : String) (row : List String × Nat × Nat × String) : Bool :=
  let (names, turns, other, fix) := row
  let s := do_ (do_ SOLVED D0) (invSeq fix)
  isDRon (do_ SOLVED D0) 1 &&
  match sig_of s 2 with
  | none => false
  | some g => slices g == 1 && sameEdges names (flippedAt g) && turns_to_dr g == turns &&
      turns_after g alt == other && len fix == turns && isDRon (do_ s fix) 1

/-- The same row, recomputed: (turns as it is, turns after alt). -/
def rowValues (alt : String) (fix : String) : Nat × Nat :=
  match sig_of (do_ (do_ SOLVED D0) (invSeq fix)) 2 with
  | none => (0, 0)
  | some g => (turns_to_dr g, turns_after g alt)

/-- Depth-first: is there a sequence of at most k face turns (no two in a row on one face, opposite faces in a fixed
order) taking s to a real DR on some axis? -/
def faceIdx (m : String) : Nat := match m.front with
  | 'U' => 0 | 'D' => 1 | 'R' => 2 | 'L' => 3 | 'F' => 4 | _ => 5

def drWithin : Nat → State → Nat → Bool
  | 0, s, _ => isDRany s
  | k + 1, s, last =>
    isDRany s || NAMES.any fun m =>
      let f := faceIdx m
      if f == last || (f / 2 == last / 2 && f < last) then false
      else drWithin k (apply s (MOVES m)) f

/-- Pieces (home positions) at the given places. -/
def pieceAt (s : State) (p : Vec) : Vec := homePos s[(fe.CUBIES p)[0]!]!

end witness
end DRXs
