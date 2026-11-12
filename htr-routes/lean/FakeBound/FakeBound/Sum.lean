/-
  FakeBound.Sum — finite sums Σ_{j<n} f j over the integers, and the few facts about them that the bound needs.
  Plain Lean core (no Mathlib): every lemma is proved by induction on n and `omega`.
-/
namespace FakeBound

/-- `sumZ f n = f 0 + f 1 + … + f (n-1)`. -/
def sumZ (f : Nat → Int) : Nat → Int
  | 0 => 0
  | n + 1 => sumZ f n + f n

@[simp] theorem sumZ_zero (f : Nat → Int) : sumZ f 0 = 0 := rfl
@[simp] theorem sumZ_succ (f : Nat → Int) (n : Nat) : sumZ f (n + 1) = sumZ f n + f n := rfl

theorem sumZ_congr {f g : Nat → Int} : ∀ n, (∀ j, j < n → f j = g j) → sumZ f n = sumZ g n
  | 0, _ => rfl
  | n + 1, h => by
    simp only [sumZ_succ]
    rw [sumZ_congr n (fun j hj => h j (by omega)), h n (by omega)]

theorem sumZ_add (f g : Nat → Int) : ∀ n, sumZ (fun j => f j + g j) n = sumZ f n + sumZ g n
  | 0 => by simp
  | n + 1 => by simp only [sumZ_succ, sumZ_add f g n]; omega

theorem sumZ_sub (f g : Nat → Int) : ∀ n, sumZ (fun j => f j - g j) n = sumZ f n - sumZ g n
  | 0 => by simp
  | n + 1 => by simp only [sumZ_succ, sumZ_sub f g n]; omega

theorem sumZ_le {f g : Nat → Int} : ∀ n, (∀ j, j < n → f j ≤ g j) → sumZ f n ≤ sumZ g n
  | 0, _ => by simp
  | n + 1, h => by
    simp only [sumZ_succ]
    have := sumZ_le n (fun j hj => h j (by omega))
    have := h n (by omega)
    omega

theorem sumZ_const_zero : ∀ n, sumZ (fun _ => (0 : Int)) n = 0
  | 0 => rfl
  | n + 1 => by simp [sumZ_const_zero n]

/-- Peel off the first term. -/
theorem sumZ_succ_left (f : Nat → Int) : ∀ n, sumZ f (n + 1) = f 0 + sumZ (fun i => f (i + 1)) n
  | 0 => by simp
  | n + 1 => by
    rw [sumZ_succ, sumZ_succ_left f n, sumZ_succ]; omega

/-- A sum of a constant c over the members of m below n is c times their number. -/
theorem sumZ_ite_const (m : Nat → Bool) (c : Int) : ∀ n,
    sumZ (fun i => if m i then c else 0) n = c * sumZ (fun i => if m i then 1 else 0) n
  | 0 => by simp
  | n + 1 => by
    simp only [sumZ_succ, sumZ_ite_const m c n]
    cases m n <;> simp [Int.mul_add]

/-- Terms before `lo` dropped: Σ_{lo ≤ j < n} f j = Σ_{j<n} f j - Σ_{j<lo} f j. -/
theorem sumZ_from (f : Nat → Int) (lo : Nat) : ∀ n, lo ≤ n →
    sumZ (fun j => if lo ≤ j then f j else 0) n = sumZ f n - sumZ f lo
  | 0, h => by
    have : lo = 0 := by omega
    subst this; simp
  | n + 1, h => by
    by_cases hl : lo = n + 1
    · subst hl
      have : sumZ (fun j => if n + 1 ≤ j then f j else 0) (n + 1) = 0 := by
        rw [sumZ_congr (g := fun _ => 0) (n + 1) (fun j hj => by simp; omega), sumZ_const_zero]
      rw [this]; omega
    · simp only [sumZ_succ, sumZ_from f lo n (by omega)]
      simp only [show lo ≤ n from by omega, ite_true]
      omega

/-- One term of a sum of non-negative terms is at most the sum. -/
theorem le_sumZ {f : Nat → Int} (h0 : ∀ j, 0 ≤ f j) {j : Nat} : ∀ n, j < n → f j ≤ sumZ f n
  | 0, h => by omega
  | n + 1, h => by
    simp only [sumZ_succ]
    by_cases hj : j = n
    · subst hj
      have : 0 ≤ sumZ f j := by
        have := sumZ_le (f := fun _ => 0) (g := f) j (fun i _ => h0 i)
        rw [sumZ_const_zero] at this; exact this
      omega
    · have := le_sumZ h0 (j := j) n (by omega)
      have := h0 n
      omega

end FakeBound
