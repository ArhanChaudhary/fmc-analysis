/-
  EOSwitch.Model — checked statements, part A (see README.md): the model, the geometry the features use, and the
  features on the research's worked examples.  Every one is a closed statement about the definitions in Cube /
  Pieces / Search / Switch, proved by running them: `native_decide` evaluates the statement with compiled code and
  accepts the answer (this trusts the Lean compiler; see README.md).

  Axes: 0 = R/L, 1 = U/D, 2 = F/B.  Moves: indices into NAMES = U U2 U' D D2 D' R R2 R' L L2 L' F F2 F' B B2 B'.
-/
import EOSwitch.Switch

namespace EOSwitch
open cube pieces sw

set_option maxHeartbeats 0

/-! ## A. The model (as in eo-to-dr's certificate) -/

/-- 54 stickers, all different; the 18 face turns are permutations of them, named U U2 U' … B B2 B'. -/
theorem model_size :
    cube.ST.size = 54 ∧ cube.ST.toList.eraseDups.length = 54 ∧
    NAMES = ["U", "U2", "U'", "D", "D2", "D'", "R", "R2", "R'", "L", "L2", "L'", "F", "F2", "F'", "B", "B2", "B'"] ∧
    (∀ name ∈ NAMES, is_permutation (MOVES name) = true) := by
  native_decide

/-- 12 edge places of 2 stickers and 8 corner places of 3, together all 48 non-centre stickers; the E-slice
places are the four with no sticker on U or D, and they are what the solved cube's E-slice mask marks. -/
theorem places :
    EPL.size = 12 ∧ (EPL.toList.all fun l => l.length == 2) ∧
    CPL.size = 8 ∧ (CPL.toList.all fun l => l.length == 3) ∧
    (EPL.toList.flatten ++ CPL.toList.flatten).eraseDups.length = 48 ∧
    E_HOME = ((List.range 12).filter fun k => kind k == 1).foldl (fun a k => a + 2 ^ k) 0 ∧
    (List.range 12).all (fun k => (kind k == 1) == !(onFace 0 k || onFace 1 k)) := by
  native_decide

/-- The turns that keep F/B EO are exactly U, D, R, L turns and F2, B2 (`KEEP`, the 14 turns of the BFS): a turn
changes the goodness of an edge for F/B exactly when it is an F or B quarter turn and the edge is on that face. -/
theorem keep_fb_eo :
    (∀ mv ∈ List.range 18, ∀ k ∈ List.range 12,
      EFLIP[2]![mv]![k]! = (mv % 3 != 1 && (AX FACES[mv / 3]!).1 == 2 && onFace (mv / 3) k)) ∧
    (List.range 18).filter (fun mv => (List.range 12).all fun k => !EFLIP[2]![mv]![k]!) = KEEP := by
  native_decide

/-- Each face turn carries corner places to corner places one to one, and the sticker list of each corner place
(U/D sticker first, then round the corner) onto that of its destination, shifted cyclically: it adds `CDELTA`
(mod 3) to the twist, and these sum to 0 mod 3.  Edge places go to edge places one to one. -/
theorem turns_permute_pieces : ∀ mv ∈ List.range 18,
    (List.range 12).all (fun k => EDEST[mv]![k]! < 12) ∧ (EDEST[mv]!.toList.eraseDups.length = 12) ∧
    (List.range 8).all (fun c => CDEST[mv]![c]! < 8) ∧ (CDEST[mv]!.toList.eraseDups.length = 8) ∧
    (List.range 8).all (cyclic mv) ∧ (CDELTA[mv]!.toList.sum % 3 = 0) := by
  native_decide

/-- The coordinates follow the stickers: on every sticker state reached with at most 3 face turns, and for each
turn, the twist number and the E-slice mask after the turn are what `coAct`, `maskAct` compute from those before.
The solved cube has no twist, no bad edge for F/B, and its E-slice pieces in the E-slice places. -/
theorem coordinates_follow_stickers :
    (∀ s ∈ near 3, ∀ mv ∈ List.range 18,
      coOf (apply s MV[mv]!) = coAct mv (coOf s) ∧ eMask (apply s MV[mv]!) = maskAct mv (eMask s)) ∧
    coOf SOLVED = 0 ∧ badMask 2 SOLVED = 0 ∧ eMask SOLVED = E_HOME := by
  native_decide

/-! ## The geometry the features use -/

/-- Places.  U/D-layer edge places are the 8 with a U or D sticker, E-slice places the other 4; the M places are
the four U/D-layer places with no R or L sticker (UF UB DF DB), the other four U/D-layer places have no F or B
sticker (UR UL DR DL, the S places).  Every edge place has exactly two corners next to it (`NB`), each sharing two
stickers' faces with it; for a U/D-layer place, they are in its layer, and its zero axis is R/L (M places) or F/B
(S places).  For each corner place, a twist of 0 puts the U/D sticker on U or D, and the twists 0, 1, 2 put it on
the three axes, one each (so `udAxis` reads the face of the U/D sticker for every twist). -/
theorem feature_places :
    UD_PLACES.length = 8 ∧ E_SLOTS.length = 4 ∧
    (UD_PLACES.all fun k => onFace 0 k || onFace 1 k) ∧ (E_SLOTS.all fun k => !(onFace 0 k || onFace 1 k)) ∧
    M_PLACES = UD_PLACES.filter (fun k => !(onFace 2 k || onFace 3 k)) ∧ M_PLACES.length = 4 ∧
    (UD_PLACES.all fun k => isM k != isS k) ∧ (UD_PLACES.filter isS).all (fun k => !(onFace 4 k || onFace 5 k)) ∧
    ((List.range 12).all fun k => NB[k]!.length == 2 &&
      NB[k]!.all fun c => ((List.range 6).filter fun f => (onFace f k) &&
        (CPL[c]!.any fun i => FACE_OF[i]! == FACES[f]!)).length == 2) ∧
    (UD_PLACES.all fun k => NB[k]!.all fun c => (CV c)[1]! == (EV k)[1]!) ∧
    (UD_PLACES.all fun k => ZAX[k]! == (if isM k then 0 else 2)) ∧
    ((List.range 8).all fun c => UDAX[c]![0]! == 1 && UDAX[c]!.toList.mergeSort (· ≤ ·) == [0, 1, 2]) := by
  native_decide

/-! ## The features on the research's worked examples -/

/-- The inverse of a move sequence. -/
def invSeq (seq : String) : String :=
  " ".intercalate ((cube.parse seq).reverse.map fun t =>
    if t.endsWith "'" then (t.dropEnd 1).toString else if t.endsWith "2" then t else t ++ "'")

/-- The sticker state of an example: the state after `seq` from solved (`after` = true), or the state that `seq`
solves (= after the inverse of `seq`). -/
def exState (after : Bool) (seq : String) : State := do_ SOLVED (if after then seq else invSeq seq)

/-- [bad corners, 2 × bad U/D edges, carm, earm, pairs, fake pairs, side pairs, EO-kept distance to DR] of a
sticker state, read through `coOf`, `eMask`, `feat` and the BFS table. -/
def exValues (s : State) : List Nat :=
  let co := coOf s
  let m := eMask s
  let f := feat co m
  [f.c, f.e, f.carm, f.earm, f.pairs, f.fake, f.side, (dist.get! (co * 4096 + m)).toNat]

/-- The research's unit tests of its features (`src/features.py`: the 25 distinct states of TESTS and the two of E1; printed in
`out/checks_features.txt`), with every value that file prints for the state: "xcye AR-acbe pairs p fake f side s
d n".  Each example has F/B EO solved; its values are as printed.  (The research's tests of `corner_case`,
`case_suffix` and `rl_to_jzp` are about features this certificate does not define; JZP is checked on R L.) -/
theorem feature_examples :
    ([(true, "R", [4, 4, 0, 0, 4, 0, 4, 1]),
      (true, "R U", [4, 4, 2, 1, 4, 0, 2, 2]),
      (false, "U' F2 B2 R2 U2 R", [4, 4, 0, 2, 0, 0, 2, 6]),
      (false, "D F2 B2 L2 U2 R", [4, 4, 0, 2, 0, 0, 2, 6]),
      (false, "R F2 U2 R", [4, 4, 0, 0, 3, 0, 3, 4]),
      (false, "U' R2 D B2 R", [4, 4, 2, 1, 2, 0, 1, 5]),
      (false, "D R' U2 F2 R", [4, 4, 1, 0, 3, 0, 2, 5]),
      (false, "U' R2 D R2 D L", [4, 4, 4, 2, 3, 0, 0, 6]),
      (false, "R2 U D' F2 L", [4, 4, 4, 2, 4, 0, 0, 5]),
      (false, "R' U2 F2 L2 U R", [4, 4, 2, 1, 3, 1, 1, 6]),
      (false, "R U2 B2 R2 D' R", [4, 4, 2, 1, 3, 1, 1, 6]),
      (false, "U B2 D2 L D R", [7, 8, 2, 2, 5, 3, 5, 6]),
      (false, "D L U R2 U' R", [7, 8, 2, 2, 5, 3, 5, 6]),
      (false, "D' L' D L2 D' R", [7, 8, 2, 2, 6, 1, 5, 6]),
      (false, "R", [4, 4, 0, 0, 4, 0, 4, 1]),
      (false, "U' R", [4, 4, 2, 1, 4, 0, 2, 2]),
      (false, "U' R2 U R", [4, 4, 3, 1, 3, 1, 1, 4]),
      (false, "U F2 R", [4, 4, 2, 1, 2, 0, 2, 3]),
      (false, "D F2 B2 R", [4, 4, 2, 1, 0, 0, 2, 4]),
      (false, "F2 B2 R", [4, 4, 0, 0, 0, 0, 4, 3]),
      (false, "R U2 R", [4, 2, 0, 0, 2, 0, 2, 3]),
      (false, "R U R", [3, 2, 2, 1, 1, 0, 1, 3]),
      (false, "R U L", [7, 8, 2, 1, 6, 2, 5, 3]),
      (false, "R L", [8, 8, 0, 0, 8, 0, 8, 2]),
      (false, "R U2 L", [4, 6, 0, 0, 4, 0, 4, 3]),
      (true, "R U D2 L U' R U2", [4, 4, 2, 1, 0, 2, 1, 7]),
      (true, "R U D2 L U' R U2 L'", [4, 4, 2, 1, 2, 0, 1, 6])] : List (Bool × String × List Nat)).all
      (fun (a, seq, v) => badMask 2 (exState a seq) == 0 && exValues (exState a seq) == v) ∧
    (let s := exState false "R L"; (feat (coOf s) (eMask s)).jzp = true) := by
  native_decide

end EOSwitch
