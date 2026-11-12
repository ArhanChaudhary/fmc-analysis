/-
  FakeBound.Counter — explicit finishes on which the printed forms of T11502/T11503 fail, and the C placement.

  Every example is a finish (N, s_0 … s_N) with α from a real corner path (`q9_alpha.tsv`, re-derived in Lean by
  HTRRoutes' `alpha_matches_study`; the two paths used are checked again in FakeBound.Subset), L = M, and A, B, C set
  to the largest values the finish allows (A = L - s_N, B = L - s_0, C = L - s_0 - s_N), so the hypotheses hold
  with the strongest A, B, C there could be; the `∀ A B C` forms show the failure does not depend on them.
  All proofs are `decide` (kernel evaluation, no extra axiom).
-/
import FakeBound.Formula

namespace FakeBound

/-- A list as a function (0 past the end). -/
def ofL (l : List Nat) : Nat → Nat := fun i => l.getD i 0

/-! ### 1. Term 2 with T11502's signs is not an upper bound (min reading) -/

/-- **Printed term 2 fails.**  Path 4a1 > 0c0 > 4a1 > 0c0 (α = 0,0,0,0), finish with N = 3 and sections
s = (0, 3, 0, 4), L = M = 10.  Its reductions are 6, 6, 5, so the shortest is 5; R with the printed term 2 is 4 (from
S = {0, 2}: ((2-1)·10 - (3-2) + 0)/2 = 4.5), whatever A, B, C are; with the corrected term 2 (and the finish's own
A = 6, B = 10, C = 6) R is 5, which is exactly this finish's shortest reduction. -/
theorem printed_term2_fails :
    let s := ofL [0, 3, 0, 4]; let α := ofL [0, 0, 0, 0]
    len 3 s = 10 ∧ (List.range 3).map (red 3 s) = [6, 6, 5] ∧ minRed 3 s = 5 ∧
    (4 : Int) ∈ (chains 0 2).map (term2 3 α 10 1 true) ∧
    Rmin 3 α 10 6 10 6 (printed := true) = 4 ∧
    Rmin 3 α 10 6 10 6 = 5 := by decide

theorem printed_term2_fails_any_ABC (A B C : Int) :
    Rmin 3 (ofL [0, 0, 0, 0]) 10 A B C (printed := true) < minRed 3 (ofL [0, 3, 0, 4]) := by
  have hmem : (4 : Int) ∈ terms 3 (ofL [0, 0, 0, 0]) 10 A B C 1 true := by
    unfold terms
    apply List.mem_append_left; apply List.mem_append_left; apply List.mem_append_left
    apply List.mem_append_right
    decide
  have := foldl_min_le _ 10 4 hmem
  have h5 : minRed 3 (ofL [0, 3, 0, 4]) = 5 := by decide
  unfold Rmin; omega

/-- The smallest instance: N = 3, all sections empty (L = M = 3, e.g. three quarter turns), reductions 2, 2, 2;
printed R = 1. -/
theorem printed_term2_fails_small :
    minRed 3 (ofL [0, 0, 0, 0]) = 2 ∧ Rmin 3 (ofL [0, 0, 0, 0]) 3 3 3 3 (printed := true) = 1 := by decide

/-! ### 2. The edge sum needs α_{i+1}, not α_i -/

/-- **α_i fails, in T11502 and in T11503.**  Path 4b2 > 4a3 > 4b2 > 4a1 > 0c0 (α = 0,0,3,1,0), N = 4,
s = (2, 1, 3, 1, 3), L = M = 14.  Reductions 10, 9, 9, 9: shortest 9.
* R (min, corrected signs) with α_i: 8 < 9, for every A, B, C (S = {0, 2, 3}: (2·14 + 1 - α_2)/3 = 26/3).
  With α_{i+1} and the finish's own A = 11, B = 12, C = 9: R = 9 (sound, and tight here).
* T11503's first bound with α_i, R' = 9 (every reduction ≥ 9), S = {0, 2, 3}: it claims
  (|S|-1)·M ≥ |S|(R'+1) - N + α_2, i.e. 28 ≥ 29, false for this 14-move finish; with α_3 it reads 28 ≥ 27. -/
theorem alpha_i_fails :
    let s := ofL [2, 1, 3, 1, 3]; let α := ofL [0, 0, 3, 1, 0]; let S := [true, false, true, true]
    len 4 s = 14 ∧ (List.range 4).map (red 4 s) = [10, 9, 9, 9] ∧ minRed 4 s = 9 ∧
    (∀ j, j ≤ 4 → α j ≤ s j) ∧
    Rmin 4 α 14 11 12 9 (shift := 0) = 8 ∧ Rmin 4 α 14 11 12 9 = 9 ∧
    isChain S 0 3 = true ∧ card (memL S) 3 = 3 ∧
    edgeSum (memL S) (edgeW α 0) 3 = 3 ∧ edgeSum (memL S) (edgeW α 1) 3 = 1 ∧
    ¬ (card (memL S) 3 * (9 + 1) - 4 + edgeSum (memL S) (edgeW α 0) 3 ≤ (card (memL S) 3 - 1) * len 4 s) ∧
    (card (memL S) 3 * (9 + 1) - 4 + edgeSum (memL S) (edgeW α 1) 3 ≤ (card (memL S) 3 - 1) * len 4 s) := by
  refine ⟨by decide, by decide, by decide, ?_, by decide, by decide, by decide, by decide, by decide, by decide,
    by decide, by decide⟩
  intro j hj
  match j, hj with
  | 0, _ | 1, _ | 2, _ | 3, _ | 4, _ => decide

theorem alpha_i_fails_any_ABC (A B C : Int) :
    Rmin 4 (ofL [0, 0, 3, 1, 0]) 14 A B C (shift := 0) < minRed 4 (ofL [2, 1, 3, 1, 3]) := by
  have hmem : (8 : Int) ∈ terms 4 (ofL [0, 0, 3, 1, 0]) 14 A B C 0 false := by
    unfold terms
    apply List.mem_append_left; apply List.mem_append_left; apply List.mem_append_left
    apply List.mem_append_right
    decide
  have := foldl_min_le _ 14 8 hmem
  have h9 : minRed 4 (ofL [2, 1, 3, 1, 3]) = 9 := by decide
  unfold Rmin; omega

/-! ### 3. Where C goes: the middle block, not "the finish minus one middle section" -/

/-- **L - s_0 - s_N ≥ C and L - s_j ≥ C (j a middle section) are different statements**: neither implies the other.
(N = 3.)  With s = (0, 5, 0, 0) and C = 8 the true hypothesis holds (8 ≥ 8) but L - s_1 = 3 < 8; with
s = (5, 0, 0, 5) and C = 13, L - s_1 = 13 ≥ 13 but L - s_0 - s_3 = 3 < 13.  So a bound derived from "L - s_j ≥ C"
is about different finishes; the hypothesis that the middle block Q_1 s_1 … s_{N-1} Q_N is an HTR of a state of the
same subset (FakeBound.Subset) is the one `term5_sound` uses.  Since a NISS HTR is never longer than the shortest
linear one, any smaller C (e.g. the shortest NISS HTR) also satisfies the hypothesis, so it is allowed but only
weakens R: C does not *need* to be the NISS one. -/
theorem C_placement :
    (let s := ofL [0, 5, 0, 0]; len 3 s = 8 ∧ 8 ≤ len 3 s - s 0 - s 3 ∧ ¬ (8 ≤ len 3 s - s 1)) ∧
    (let s := ofL [5, 0, 0, 5]; len 3 s = 13 ∧ 13 ≤ len 3 s - s 1 ∧ ¬ (13 ≤ len 3 s - s 0 - s 3)) := by decide


/-! ### 4. The readings of T11502, verdict by verdict -/

/-- **The coordinator's witness** (0c3 path 0c3 > 4a2 > 4a1 > 0c0, α = 0,3,3,0; sections 2,3,3,3; L = M = 14):
reductions 8, 7, 7, so a 7-move reduction is needed.  Min reading with the printed term 2 gives 6 (with either α
index, and for every A, B, C since S = {0, 2} alone gives ⌊13/2⌋); with the derived signs and α_{i+1}, and the
finish's own A = 11, B = 12, C = 9, it gives 7, exactly what is needed. -/
theorem witness_0c3 :
    let s := ofL [2, 3, 3, 3]; let α := ofL [0, 3, 3, 0]
    len 3 s = 14 ∧ (List.range 3).map (red 3 s) = [8, 7, 7] ∧ minRed 3 s = 7 ∧
    Rmin 3 α 14 11 12 9 (printed := true) = 6 ∧ Rmin 3 α 14 11 12 9 (shift := 0) (printed := true) = 6 ∧
    Rmin 3 α 14 11 12 9 = 7 := by decide

/-- **Fully literal min reading** (printed signs and printed α_i) fails too: on the finish of
`printed_term2_fails` it gives 4 < 5. -/
theorem literal_min_fails :
    Rmin 3 (ofL [0, 0, 0, 0]) 10 6 10 6 (shift := 0) (printed := true) = 4 ∧
    minRed 3 (ofL [0, 3, 0, 4]) = 5 := by decide

/-- **The min of the terms is sound but not always tight.**  N = 3, α = 0, M = 5, A = B = 5, C = 0: R (min, derived
signs, α_{i+1}) is 3, but every finish satisfying the hypotheses has a reduction of at most 2 (A = 5 and B = 5 with
L ≤ 5 force s_0 = s_3 = 0, and then the middle window's reduction is L - 1 - s_1 - s_2 = 2).  The terms use A, B
and C one at a time, never together, so they are not the exact optimum of the linear program when two of them
bind at once. -/
theorem Rmin_not_tight :
    Rmin 3 (ofL [0, 0, 0, 0]) 5 5 5 0 = 3 ∧
    (∀ s : Nat → Nat, len 3 s ≤ 5 → 5 ≤ len 3 s - s 3 → 5 ≤ len 3 s - s 0 → minRed 3 s ≤ 2) ∧
    minRed 3 (ofL [0, 1, 1, 0]) = 2 ∧ len 3 (ofL [0, 1, 1, 0]) = 5 := by
  refine ⟨by decide, ?_, by decide, by decide⟩
  intro s hL hA hB
  have h := minRed_le (N := 3) (s := s) (i := 1) (by omega)
  have : red 3 s 1 = 2 := by
    unfold red len at *
    simp only [sumZ_succ, sumZ_zero, Nat.reduceAdd] at *
    omega
  omega

end FakeBound
