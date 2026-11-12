/-
  EODR.Model — checked statements, part A (see README.md).  Every one is a closed statement about the definitions in Cube / Pieces /
  Search / Eo / Layouts / Eodr, proved by running them: `native_decide` evaluates the statement with compiled code
  and accepts the answer (this trusts the Lean compiler; see README.md).  Statements that are plain arithmetic on
  numbers are proved by `decide` (Lean's kernel alone).

  Axes: 0 = R/L, 1 = U/D, 2 = F/B.  Moves: indices into NAMES = U U2 U' D D2 D' R R2 R' L L2 L' F F2 F' B B2 B'.
  Reading aid:  `hist l` = list of (value, how many times it occurs in l), by value.
-/
import EODR.Eo
import EODR.Layouts
import EODR.Eodr
import EODR.Parse

namespace EODR
open cube pieces

set_option maxHeartbeats 0

/-! ## A. The model -/

/-- 54 stickers, all different; the 18 face turns are permutations of them, named U U2 U' … B B2 B'. -/
theorem model_size :
    cube.ST.size = 54 ∧ cube.ST.toList.eraseDups.length = 54 ∧
    NAMES = ["U", "U2", "U'", "D", "D2", "D'", "R", "R2", "R'", "L", "L2", "L'", "F", "F2", "F'", "B", "B2", "B'"] ∧
    (∀ name ∈ NAMES, is_permutation (MOVES name) = true) := by
  native_decide

/-- 12 edge places of 2 stickers and 8 corner places of 3, together all 48 non-centre stickers; four edge places
of each kind (0 M slice, 1 E slice, 2 S slice); the E-slice places are FR FL BR BL (no sticker on U or D). -/
theorem places :
    EPL.size = 12 ∧ (EPL.toList.all fun l => l.length == 2) ∧
    CPL.size = 8 ∧ (CPL.toList.all fun l => l.length == 3) ∧
    (EPL.toList.flatten ++ CPL.toList.flatten).eraseDups.length = 48 ∧
    ((List.range 12).map kind).count 0 = 4 ∧ ((List.range 12).map kind).count 1 = 4 ∧
    ((List.range 12).map kind).count 2 = 4 ∧
    E_HOME = ((List.range 12).filter fun k => kind k == 1).foldl (fun a k => a + 2 ^ k) 0 ∧
    (List.range 12).all (fun k => (kind k == 1) == !(onFace 0 k || onFace 1 k)) := by
  native_decide

/-- Each face turn carries edge places to edge places and corner places to corner places, one to one. -/
theorem turns_permute_pieces : ∀ mv ∈ List.range 18,
    (List.range 12).all (fun k => EDEST[mv]![k]! < 12) ∧ (EDEST[mv]!.toList.eraseDups.length = 12) ∧
    (List.range 8).all (fun c => CDEST[mv]![c]! < 8) ∧ (CDEST[mv]!.toList.eraseDups.length = 8) := by
  native_decide

/-- The EO rule: a face turn changes the goodness for axis Y of the edge at place k exactly when it is a quarter
turn of a face of axis Y and the edge is on that face.  (So turns other than Y's quarter turns keep every edge's
goodness, and a quarter turn of a Y face makes four good edges bad or the reverse.) -/
theorem flip_table : ∀ Y ∈ List.range 3, ∀ mv ∈ List.range 18, ∀ k ∈ List.range 12,
    EFLIP[Y]![mv]![k]! = (mv % 3 != 1 && (AX FACES[mv / 3]!).1 == Y && onFace (mv / 3) k) := by
  native_decide

/-- The turns that keep F/B EO are exactly U, D, R, L turns and F2, B2: the move set of C. -/
theorem keep_fb_eo :
    (List.range 18).filter (fun mv => (List.range 12).all fun k => !EFLIP[2]![mv]![k]!) = eodr.KEEP := by
  native_decide

/-- Every face turn carries the sticker list of each corner place (U/D sticker first, then round the corner)
onto that of its destination, shifted cyclically; so it adds `CDELTA` (mod 3) to the twist.  The twists it adds
sum to 0 mod 3. -/
theorem corner_turns_cyclic : ∀ mv ∈ List.range 18,
    (List.range 8).all (cyclic mv) ∧ (CDELTA[mv]!.toList.sum % 3 = 0) := by
  native_decide

/-- The coordinates follow the stickers: on every sticker state reached with at most 3 face turns, and for each of
the 18 turns, the bad-edge masks on the three axes, the twist number and the E-slice mask of the state after the
turn are what `EOT`, `coAct`, `maskAct` compute from those of the state before.  The solved cube has no bad edge,
no twist, and its E-slice pieces in the E-slice places. -/
theorem coordinates_follow_stickers :
    (∀ s ∈ near 3, ∀ mv ∈ List.range 18,
      (∀ Y ∈ List.range 3, badMask Y (apply s MV[mv]!) = EOT[Y]![mv]![badMask Y s]!) ∧
      coOf (apply s MV[mv]!) = coAct mv (coOf s) ∧
      eMask (apply s MV[mv]!) = maskAct mv (eMask s)) ∧
    (∀ Y ∈ List.range 3, badMask Y SOLVED = 0) ∧ coOf SOLVED = 0 ∧ eMask SOLVED = E_HOME := by
  native_decide

end EODR
