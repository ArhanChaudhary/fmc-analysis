/-
  DRXs.EightFeTheorems — statement K: section 6.3, the DR-2s 8fe from a full EO.

  The search and the run are in DRXs/EightFe.lean, compiled.  **Editing this file repeats the run.**
-/
import DRXs.EightFe

namespace DRXs

open cube fecosets eightfe
set_option maxHeartbeats 0

/-- The renaming about F/B (`z`) and about R/L (`x`) turns every face turn into a face turn: R ∘ m = σ(m) ∘ R on
places, with σ_z: U→R, D→L, R→D, L→U, F→F, B→B (and the same suffix), σ_x: U→B, D→F, F→U, B→D, R→R, L→L.
σ_z maps the 14 turns that keep F/B EO onto themselves.  Since a state is moved by moving its places, this is
`rename (apply s m) = apply (rename s) (σ m)` for every state s. -/
theorem rename_conjugates :
    NAMES.map (sigma 2) = ["R", "R2", "R'", "L", "L2", "L'", "D", "D2", "D'", "U", "U2", "U'",
                           "F", "F2", "F'", "B", "B2", "B'"].map some ∧
    NAMES.map (sigma 0) = ["B", "B2", "B'", "F", "F2", "F'", "R", "R2", "R'", "L", "L2", "L'",
                           "U", "U2", "U'", "D", "D2", "D'"].map some ∧
    (KEEP.map fun m => (sigma 2 m).getD "").mergeSort (fun a b => decide (a ≤ b)) =
      KEEP.mergeSort (fun a b => decide (a ≤ b)) := by native_decide

/-- R is eo8_hist.rename: on a scrambled state the two agree (checked on three states). -/
theorem rename_is_python_rename : ∀ seq ∈ ["R U F' L2 D B", "F", "U R2 F2 D' B2 U2 L2 D R' L'"],
    renameSeq (do_ SOLVED seq) 2 = apply (do_ SOLVED seq) (R 2) ∧
    renameSeq (do_ SOLVED seq) 0 = apply (do_ SOLVED seq) (R 0) := by native_decide

/-- The 8fe kinds: corners on R/L or on F/B, all eight layer edges flipped, centres off (slice bits 0000), two
slices.  Undoing the renaming on the solved cube gives each of them: the renaming takes an 8fe to a real DR. -/
theorem eight_fe_is_renamed_dr :
    eightKinds.length = 2 ∧
    (eightKinds.all fun g => g.flips == [1, 1, 1, 1, 1, 1, 1, 1] && g.sl == [0, 0, 0, 0]) = true ∧
    (sig_of (apply SOLVED (edges.inverse (R 2))) 0).any eightKinds.contains = true ∧
    (sig_of (apply SOLVED (edges.inverse (R 0))) 2).any eightKinds.contains = true := by native_decide

/-- **Section 6.3, from a full EO.**  Over the 1,082,565 positions with F/B EO solved (all reached from the solved
cube with the 14 turns that keep it, none with a neighbour outside, all twelve edges good for F/B), exactly one is
a real DR and exactly one an 8fe.  The distances to each (BFS tables that pass the rule check) have the same
histogram, 1, 2, 17, 134, 1065, 8190, 54694, 267576, 560568, 187204, 3114 at 0 to 10 moves, sum 8,447,364
(mean 7.80); and position by position the 8fe distance is the DR distance of the renamed position. -/
theorem eight_fe_full_eo : run () =
    { positions := 1082565, outside := 0, notEO := 0, nDR := 1, n8fe := 1, rulesOK := true,
      histDR := [(0, 1), (1, 2), (2, 17), (3, 134), (4, 1065), (5, 8190), (6, 54694), (7, 267576),
                 (8, 560568), (9, 187204), (10, 3114)],
      hist8fe := [(0, 1), (1, 2), (2, 17), (3, 134), (4, 1065), (5, 8190), (6, 54694), (7, 267576),
                  (8, 560568), (9, 187204), (10, 3114)],
      sumDR := 8447364, sum8fe := 8447364, renameBad := 0, renameOutside := 0 } := by
  native_decide

/-- 8447364 / 1082565 = 7.803…, printed 7.80; 1,082,565 = 2187 × 495. -/
theorem eight_fe_mean_digits :
    7795 * 1082565 ≤ 8447364 * 1000 ∧ 8447364 * 1000 < 7805 * 1082565 ∧ 2187 * 495 = 1082565 := by decide

end DRXs
