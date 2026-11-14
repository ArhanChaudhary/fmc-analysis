/-
  AttemptSim.CompleteThm — checked statements, part D: on the exported scrambles, the simulator's candidate lists are
  exactly the sets defined in Complete.lean, enumerated by brute force on the sticker cube.
-/
import AttemptSim.Complete

namespace AttemptSim
open cube pieces cubie complete

set_option maxHeartbeats 0

/-- The fast tests are the tests: on every state within 3 turns of solved, for every axis and pair of axes. -/
theorem fast_tests_agree :
    ((near 3).all fun s =>
      (List.range 3).all fun y => eoFast y s == eoOn y s &&
        (List.range 3).all fun x => x == y || drFast x y s == drOn x y s) = true := by
  native_decide

/-- The files are what the generator counted, every move name in them is one of the 18, and the stated lengths
are the numbers of turns. -/
theorem candidate_files :
    SCRAMBLES.length = manifest.CAND_SCRAMBLES ∧ FILE_EO.length = manifest.CAND_EOS ∧ FILE_DR.length = manifest.CAND_DRS ∧
    (SCRAMBLES.all fun (_, S) => S.all (· < 18)) = true ∧
    (FILE_EO.all fun (_, y, k, len, n, i) => y < 3 && k < 3 && n.all (· < 18) && i.all (· < 18) && len == n.length + i.length &&
       len ≤ manifest.CAND_EO_MAX) = true ∧
    (FILE_DR.all fun (_, x, len, n, i) => x < 3 && n.all (· < 18) && i.all (· < 18) && len == n.length + i.length &&
       len ≤ manifest.CAND_DR_CAP) = true := by
  native_decide

/-- **Every EO candidate is in the list, and nothing else is.**  For each exported scramble, the simulator's list of
EO candidates of at most `CAND_EO_MAX` turns (normal, inverse and NISS, all three axes) is, row for row, the set of
Complete.lean found by trying every sequence on the sticker cube. -/
theorem eo_candidates_complete :
    (SCRAMBLES.all fun (id, S) => eoBrute S manifest.CAND_EO_MAX == eoFile id) = true := by
  native_decide

/-- Every listed EO candidate (N, I) really is one: `I⁻¹ S N` has EO on its axis, by the definition from the
stickers (`eoOn`, not the fast test). -/
theorem eo_candidates_are_eos :
    (FILE_EO.all fun (id, y, _, _, n, i) =>
      match SCRAMBLES.find? (·.1 == id) with
      | some (_, S) => eoOn y (stateOf (inv i ++ S ++ n))
      | none => false) = true := by
  native_decide

/-- **Every EO-first DR is in the list, and nothing else is.**  For each exported scramble, the simulator's list of
DRs of at most `CAND_DR_CAP` turns through an EO candidate of at most `CAND_EO_MAX` turns is, as a set, the set of
Complete.lean found by trying every continuation on the sticker cube. -/
theorem dr_candidates_complete :
    (SCRAMBLES.all fun (id, S) => drBrute S manifest.CAND_EO_MAX manifest.CAND_DR_CAP == drFile id) = true := by
  native_decide

/-- Every listed DR (N, I) really is one: `I⁻¹ S N` has its corners oriented for the DR axis, the slice of that
axis in place, and EO on another axis (definitions from the stickers). -/
theorem dr_candidates_are_drs :
    (FILE_DR.all fun (id, x, _, n, i) =>
      match SCRAMBLES.find? (·.1 == id) with
      | some (_, S) =>
        let s := stateOf (inv i ++ S ++ n)
        (List.range 3).any fun y => y != x && drOn x y s
      | none => false) = true := by
  native_decide

end AttemptSim
