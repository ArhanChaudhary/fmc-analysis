/-
  HTRRoutes.Model — checked statements, part A: the model (see README.md).  Every theorem is a closed statement
  about the definitions, proved by running them: `native_decide` evaluates the statement with compiled code and
  accepts the answer (this trusts the Lean compiler; see README.md).

  Moves: DR moves 0 … 9 = U U2 U' D D2 D' R2 L2 F2 B2; HALF = U2 D2 R2 L2 F2 B2; QT = U U' D D'.
-/
import HTRRoutes.Corners
import HTRRoutes.HtrGroup
import HTRRoutes.Cosets

namespace HTRRoutes
open cube pieces

set_option maxHeartbeats 0

/-! ## A. The model -/

/-- 54 stickers, all different; the ten DR moves are permutations of them. -/
theorem model_size :
    cube.ST.size = 54 ∧ cube.ST.toList.eraseDups.length = 54 ∧
    DRNAMES = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"] ∧
    (∀ name ∈ DRNAMES, is_permutation (MOVES name) = true) := by
  native_decide

/-- 8 corner places, 8 U/D-layer edge places, 4 E-slice places, each a cubie of `Cube.lean` with 3, 2, 2 stickers;
4 corner places in each tetrad (UFR UBL DFL DBR are x·y·z > 0); 4 M places (UF UB DF DB) and 4 S places
(UL UR DL DR), together the 8 U/D edge places. -/
theorem places :
    CPOS.size = 8 ∧ EPOS.size = 8 ∧ SPOS.size = 4 ∧
    (CPOS.toList.all fun p => (placesOf p).length == 3) ∧ (EPOS.toList.all fun p => (placesOf p).length == 2) ∧
    (SPOS.toList.all fun p => (placesOf p).length == 2) ∧
    TET.toList.count true = 4 ∧ ISM.toList.count true = 4 ∧ ISS.toList.count true = 4 ∧
    (List.range 8).all (fun k => ISM[k]! != ISS[k]!) := by
  native_decide

/-- DR moves keep the axis of every sticker that matters: a sticker on a U/D face goes to a U/D face, and a sticker
of an E-slice edge stays on a face of the same axis.  So DR moves never twist a corner or flip an edge relative to
U/D and the E slice, and a DR state is given by its three arrangements. -/
theorem dr_keeps_axes : ∀ m ∈ List.range 10, ∀ i ∈ List.range 54,
    (nax i == 1 → nax DRMV[m]![i]! == 1) ∧
    ((SPOS.toList.any fun p => (placesOf p).contains i) → nax DRMV[m]![i]! == nax i) := by
  native_decide

/-- The arrangements follow the stickers: on every sticker state reached with at most 3 DR moves, and for each DR
move m, the corner, U/D-edge and E-slice arrangements after the move are `amul (before) (CMOV m)` (resp. EMOV,
SMOV).  The tables are permutations; the solved cube has the identity arrangements. -/
theorem arrangements_follow_stickers :
    (∀ s ∈ near 3, ∀ m ∈ List.range 10,
      corners (apply s DRMV[m]!) = amul (corners s) CMOV[m]! ∧
      edges (apply s DRMV[m]!) = amul (edges s) EMOV[m]! ∧
      slice (apply s DRMV[m]!) = amul (slice s) SMOV[m]!) ∧
    (∀ m ∈ List.range 10, isPerm 8 CMOV[m]! ∧ isPerm 8 EMOV[m]! ∧ isPerm 4 SMOV[m]!) ∧
    corners SOLVED = ident 8 ∧ edges SOLVED = ident 8 ∧ slice SOLVED = ident 4 := by
  native_decide

/-- Half turns keep each corner's tetrad, M places among M places, S among S; a quarter turn of U or D moves four
corners to the other tetrad and swaps two M with two S places; U D' moves all 8 corners to the other tetrad. -/
theorem half_turns_keep_parts :
    (∀ m ∈ HALF, ∀ i ∈ List.range 8,
      TET[CMOV[m]![i]!]! = TET[i]! ∧ ISM[EMOV[m]![i]!]! = ISM[i]!) ∧
    (∀ m ∈ QT, nbad CMOV[m]! = 4 ∧ ebad (mMask EMOV[m]!) = 4) ∧
    nbad (amul CMOV[0]! CMOV[5]!) = 8 := by
  native_decide

/-- Ranks: `unrank 8` lists all 40,320 permutations of eight, each once (rank ∘ unrank = id), with the identity
at rank 0; the same for the 24 permutations of four. -/
theorem ranks :
    (∀ r ∈ List.range 40320, isPerm 8 (unrank 8 r) = true ∧ rank (unrank 8 r) = r) ∧
    (∀ r ∈ List.range 24, isPerm 4 (unrank 4 r) = true ∧ rank (unrank 4 r) = r) ∧
    unrank 8 0 = ident 8 ∧ unrank 4 0 = ident 4 := by
  native_decide

end HTRRoutes
