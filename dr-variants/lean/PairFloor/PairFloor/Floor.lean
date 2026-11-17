/-
  PairFloor.Floor — the pair floor.

  `pair_floor`: if a sequence `w` of DR moves solves the corners and the U/D-layer edges of `g` (the E slice may
  be left as it falls), then  16 ≤ pairs g + 4 · (number of side half turns in w).

  Read at HTR with n moves left for the finish: you need at least 16 − 4n true pairs.
    0 moves left: 16 pairs     1: at least 12     2: at least 8     3: at least 4     4 or more: no condition
-/
import PairFloor.Steps

namespace DRBound

/-- One move: U and D moves keep the number of true pairs, a side half turn changes it by at most 4. -/
theorem pairs_step (g : State) (m : Move) :
    pairs (g.move m) ≤ pairs g + (if m.isSide then 4 else 0) ∧
    pairs g ≤ pairs (g.move m) + (if m.isSide then 4 else 0) := by
  rw [pairs_move]
  unfold pairs
  cases m
  · have h := step_U (fun p => g.c.get p) (fun q => g.e.get q); exact ⟨Nat.le_of_eq h, Nat.le_of_eq h.symm⟩
  · have h := step_U2 (fun p => g.c.get p) (fun q => g.e.get q); exact ⟨Nat.le_of_eq h, Nat.le_of_eq h.symm⟩
  · have h := step_U3 (fun p => g.c.get p) (fun q => g.e.get q); exact ⟨Nat.le_of_eq h, Nat.le_of_eq h.symm⟩
  · have h := step_D (fun p => g.c.get p) (fun q => g.e.get q); exact ⟨Nat.le_of_eq h, Nat.le_of_eq h.symm⟩
  · have h := step_D2 (fun p => g.c.get p) (fun q => g.e.get q); exact ⟨Nat.le_of_eq h, Nat.le_of_eq h.symm⟩
  · have h := step_D3 (fun p => g.c.get p) (fun q => g.e.get q); exact ⟨Nat.le_of_eq h, Nat.le_of_eq h.symm⟩
  · exact step_R2 (fun p => g.c.get p) (fun q => g.e.get q)
  · exact step_L2 (fun p => g.c.get p) (fun q => g.e.get q)
  · exact step_F2 (fun p => g.c.get p) (fun q => g.e.get q)
  · exact step_B2 (fun p => g.c.get p) (fun q => g.e.get q)

/-- U and D moves (quarter or half) never change the number of true pairs. -/
theorem pairs_move_ud (g : State) (m : Move) (h : m.isSide = false) : pairs (g.move m) = pairs g := by
  have := pairs_step g m
  simp [h] at this
  omega

/-- Corners and U/D-layer edges solved; the E slice is not looked at ("leave slice"). -/
def LsSolved (g : State) : Prop := g.c = id8 ∧ g.e = id8

instance (g : State) : Decidable (LsSolved g) := by unfold LsSolved; infer_instance

/-- With corners and U/D-layer edges solved, all 16 pairs are there. -/
theorem pairs_of_lsSolved (g : State) (h : LsSolved g) : pairs g = 16 := by
  obtain ⟨hc, he⟩ := h
  simp only [pairs, hc, he, id8_get]
  decide

/-- Number of side half turns (R2 L2 F2 B2) in a sequence. -/
def sideCount (w : List Move) : Nat := w.countP Move.isSide

/-- **The pair floor.**  A leave-slice finish of a state with `pairs g` true pairs has at least
`(16 - pairs g) / 4` side half turns. -/
theorem pair_floor (g : State) (w : List Move) (h : LsSolved (g.apply w)) :
    16 ≤ pairs g + 4 * sideCount w := by
  induction w generalizing g with
  | nil => simp only [State.apply_nil] at h; rw [pairs_of_lsSolved g h]; omega
  | cons m w ih =>
    have h1 := ih (g.move m) (by simpa using h)
    have h2 := (pairs_step g m).1
    have h3 : sideCount (m :: w) = sideCount w + (if m.isSide then 1 else 0) := by
      simp [sideCount, List.countP_cons]
    by_cases hm : m.isSide = true
    · simp [hm] at h2 h3; omega
    · simp [hm] at h2 h3; omega

/-- The same in total moves: a finish of `n` moves needs at least `16 - 4n` true pairs. -/
theorem pair_floor_length (g : State) (w : List Move) (h : LsSolved (g.apply w)) :
    16 ≤ pairs g + 4 * w.length := by
  have h1 := pair_floor g w h
  have h2 : sideCount w ≤ w.length := List.countP_le_length
  omega

/-- A full solve is a leave-slice solve, so the floor holds for full finishes too. -/
theorem pair_floor_full (g : State) (w : List Move) (h : g.apply w = solved) :
    16 ≤ pairs g + 4 * sideCount w :=
  pair_floor g w (by rw [h]; exact ⟨rfl, rfl⟩)

/-! ### The floor is reached at every level -/

/-- 12 pairs, one move: `R2`. -/
example : pairs (solved.apply [.R2]) = 12 ∧ LsSolved ((solved.apply [.R2]).apply [.R2]) := by decide
/-- 8 pairs, two moves: `R2 L2`. -/
example : pairs (solved.apply [.R2, .L2]) = 8 ∧ LsSolved ((solved.apply [.R2, .L2]).apply [.L2, .R2]) := by decide

/-- 4 pairs, three moves: `R2 L2 F2`. -/
example : pairs (solved.apply [.R2, .L2, .F2]) = 4 ∧ LsSolved ((solved.apply [.R2, .L2, .F2]).apply [.F2, .L2, .R2]) := by decide
/-- 0 pairs, four moves: `R2 L2 F2 B2`. -/
example : pairs (solved.apply [.R2, .L2, .F2, .B2]) = 0 ∧
    LsSolved ((solved.apply [.R2, .L2, .F2, .B2]).apply [.B2, .F2, .L2, .R2]) := by decide

end DRBound
