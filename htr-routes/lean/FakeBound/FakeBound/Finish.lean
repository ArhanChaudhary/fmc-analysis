/-
  FakeBound.Finish — FakeMMAP's bound on the length of the reductions to 1 quarter turn that a DR finish of at most
  M moves needs (Discord #fmc-theory, 2026-04-08, messages quoted below), as pure arithmetic.

  ## The model, from FakeMMAP's text

  T11501: "Let's say we're looking for a finish in M moves (or less), assuming we're only allowed to use N>1 qts. …
  Let R be the biggest possible length of a reduction to 1q you have to check … Numbering these sections from 0 to
  N, let α_i be the bound for the ith section."

  A finish with N quarter turns is  s_0 Q_1 s_1 Q_2 … Q_N s_N : sections s_0 … s_N of half turns (lengths, naturals)
  separated by the N quarter turns.  Its length is L = N + Σ s_j  (`len`).  The path's bounds say s_j ≥ α_j.

  A reduction to 1q keeps one quarter turn and the two sections around it as the 1q finish and does everything else
  (T11502 term 1: "leaving those two as the 1q finish").  Keeping Q_{i+1} with sections i and i+1 (window i,
  i = 0 … N-1) leaves a reduction of length  L - 1 - s_i - s_{i+1}  (`red N s i`).  Term 1, M - α_i - α_{i+1} - 1, is
  exactly this length bounded with s ≤ α, so window i is sections i and i+1 and windows are numbered 0 … N-1, which
  is also the range of FakeMMAP's sets S.  The solver finds the finish if any window's reduction is among the ones
  it checks, so what must be bounded is the shortest one, `minRed`.  A theorem of the form "t ≤ red N s i for every
  window i ⇒ t ≤ X" says exactly "min over windows ≤ X".

  Hypotheses A, B, C (T11501: "Optimal HTR on normal: … A", "Optimal HTR on inverse: … B", "the shortest possible
  HTR in the subset … C (so 2c3 2e would have C=5 …)"):
  * s_0 Q_1 … Q_N (everything but s_N) brings the normal scramble to HTR, so  A ≤ L - s_N.
  * The inverse of the finish, read on the inverse scramble, reaches HTR before its last section s_0⁻¹, so
    B ≤ L - s_0.
  * The middle block Q_1 s_1 … s_{N-1} Q_N solves the state s_N · X · s_0 (half-turn pre- and post-moves of the
    scramble X), which is in the same HTR subset (FakeBound.Subset proves this on the cube), so it is a linear HTR of
    a state of the subset:  C ≤ L - s_0 - s_N.  FakeMMAP uses C only for N > 2 ("if N=2, you should just discard
    this constraint").

  ## FakeMMAP's sets S and which α the "edge" sum takes

  T11502, term 2: "For each subset S of {0,...,N-1}, such that 0 and N-1 are contained in it, and such that for every
  j=0,...,N-2, S ∩ {j,j+1} is nonempty, …, where the sum is over all i's such that i, i+1 are both in S."
  This is `Chain m 0 (N-1)` (m is the membership test of S).  Terms 3, 4, 5 use `Chain m 0 (N-2)`,
  `Chain m 1 (N-1)`, `Chain m 1 (N-2)`.

  When i and i+1 are both in S, windows i and i+1 share section i+1, so the bound that is proved below subtracts
  α_{i+1} for each edge (`edgeSum m (fun i => α (i+1))`).  FakeMMAP writes α_i.  FakeBound.Counter shows that with
  α_i the bounds are false, with α from a real corner path.  If one re-indexes S by quarter turn (q = i+1, so
  S ⊆ {1,…,N}) then the shared section of q and q+1 is q and "α_q" is right; but FakeMMAP's ranges ({0,…,N-1},
  {0,…,N-2}, {1,…,N-1}) and term 1 (α_i + α_{i+1}) fix the 0-based reading, in which α_i is off by one.
-/
import FakeBound.Sum

namespace FakeBound

/-- Length of the finish s_0 Q_1 s_1 … Q_N s_N. -/
def len (N : Nat) (s : Nat → Nat) : Int := N + sumZ (fun j => (s j : Int)) (N + 1)

/-- Length of the reduction to 1q that keeps window i (Q_{i+1} with sections i and i+1) as the 1q finish. -/
def red (N : Nat) (s : Nat → Nat) (i : Nat) : Int := len N s - 1 - s i - s (i + 1)

/-- FakeMMAP's sets: S ∋ lo, hi; S ⊆ [lo, hi]; every pair {j, j+1} with lo ≤ j < hi meets S. -/
structure Chain (m : Nat → Bool) (lo hi : Nat) : Prop where
  lo_mem : m lo = true
  hi_mem : m hi = true
  inside : ∀ i, m i = true → lo ≤ i ∧ i ≤ hi
  cover : ∀ j, lo ≤ j → j < hi → m j = true ∨ m (j + 1) = true

/-- |S|. -/
def card (m : Nat → Bool) (hi : Nat) : Int := sumZ (fun i => if m i then 1 else 0) (hi + 1)

/-- Σ over edges (i and i+1 both in S) of w i. -/
def edgeSum (m : Nat → Bool) (w : Nat → Int) (hi : Nat) : Int :=
  sumZ (fun i => if m i && m (i + 1) then w i else 0) (hi + 1)

theorem card_pos {m lo hi} (h : Chain m lo hi) : 1 ≤ card m hi := by
  have := le_sumZ (f := fun i => if m i then (1 : Int) else 0) (fun j => by split <;> omega)
    (j := lo) (hi + 1) (by have := h.inside lo h.lo_mem; omega)
  simp only [h.lo_mem, ite_true] at this
  exact this

/-- **Each section in [lo, hi+1] is covered once by the windows of S, and once more for each edge.**
Σ_{i∈S} (s_i + s_{i+1}) = Σ_{lo ≤ j ≤ hi+1} s_j + Σ_{edges i} s_{i+1}. -/
theorem cover_sum {m lo hi} (h : Chain m lo hi) (s : Nat → Int) :
    sumZ (fun i => if m i then s i + s (i + 1) else 0) (hi + 1)
      = (sumZ s (hi + 2) - sumZ s lo) + edgeSum m (fun i => s (i + 1)) hi := by
  have hout : m (hi + 1) = false := by
    cases hm : m (hi + 1)
    · rfl
    · have := h.inside _ hm; omega
  -- split the window sum into its two halves
  have e1 : sumZ (fun i => if m i then s i + s (i + 1) else 0) (hi + 1)
      = sumZ (fun i => if m i then s i else 0) (hi + 1)
        + sumZ (fun i => if m i then s (i + 1) else 0) (hi + 1) := by
    rw [← sumZ_add]; exact sumZ_congr _ (fun j _ => by split <;> simp)
  have eP : sumZ (fun i => if m i then s i else 0) (hi + 1)
      = sumZ (fun j => if m j then s j else 0) (hi + 2) := by
    show _ = sumZ _ (hi + 1) + _
    simp [hout]
  have eQ : sumZ (fun i => if m i then s (i + 1) else 0) (hi + 1)
      = sumZ (fun j => if j = 0 then 0 else if m (j - 1) then s j else 0) (hi + 2) := by
    symm; rw [sumZ_succ_left]; simp
  have eE : edgeSum m (fun i => s (i + 1)) hi
      = sumZ (fun j => if j = 0 then 0 else if m (j - 1) && m j then s j else 0) (hi + 2) := by
    unfold edgeSum; symm; rw [sumZ_succ_left]; simp
  have eF : sumZ s (hi + 2) - sumZ s lo = sumZ (fun j => if lo ≤ j then s j else 0) (hi + 2) := by
    rw [sumZ_from s lo (hi + 2) (by have := h.inside lo h.lo_mem; omega)]
  rw [e1, eP, eQ, eE, eF, ← sumZ_add, ← sumZ_add]
  apply sumZ_congr
  intro j hj
  cases hmj : m j
  · -- j not in S: the windows of S cover j once iff window j-1 is in S iff lo ≤ j
    have key : (j ≠ 0 ∧ m (j - 1) = true) ↔ lo ≤ j := by
      constructor
      · rintro ⟨_, hm⟩; have := h.inside _ hm; omega
      · intro hl
        have hne : j ≠ lo := by intro e; subst e; rw [h.lo_mem] at hmj; cases hmj
        refine ⟨by omega, ?_⟩
        by_cases hjh : j = hi + 1
        · subst hjh; simpa using h.hi_mem
        · have := h.cover (j - 1) (by omega) (by omega)
          rw [show j - 1 + 1 = j by omega, hmj] at this
          simpa using this
    by_cases hj0 : j = 0
    · subst hj0
      have : ¬ lo ≤ 0 := fun hl => by have := key.mpr hl; omega
      simp [this]
    · cases hm1 : m (j - 1)
      · have : ¬ lo ≤ j := fun hl => by have := (key.mpr hl).2; rw [hm1] at this; cases this
        simp [hj0, this]
      · have : lo ≤ j := key.mp ⟨hj0, hm1⟩
        simp [hj0, this]
  · have hl : lo ≤ j := (h.inside j hmj).1
    by_cases hj0 : j = 0
    · subst hj0; simp [hl]
    · cases hm1 : m (j - 1) <;> simp [hj0, hl]

/-- **The core inequality.**  If every window's reduction is ≥ t, then for every chain S with windows inside
0 … N-1:  |S|·t ≤ |S|·(L-1) - Σ_{lo ≤ j ≤ hi+1} s_j - Σ_{edges i} α_{i+1}. -/
theorem chain_bound {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j)
    {m : Nat → Bool} {lo hi : Nat} (h : Chain m lo hi) (hN : hi < N)
    {t : Int} (ht : ∀ i, i < N → t ≤ red N s i) :
    card m hi * t ≤ card m hi * (len N s - 1)
      - (sumZ (fun j => (s j : Int)) (hi + 2) - sumZ (fun j => (s j : Int)) lo)
      - edgeSum m (fun i => (α (i + 1) : Int)) hi := by
  have h1 : card m hi * t = sumZ (fun i => if m i then t else 0) (hi + 1) := by
    unfold card; rw [sumZ_ite_const m t, Int.mul_comm]
  have h2 : sumZ (fun i => if m i then t else 0) (hi + 1)
      ≤ sumZ (fun i => if m i then (len N s - 1) - ((s i : Int) + s (i + 1)) else 0) (hi + 1) := by
    apply sumZ_le; intro i hi'
    cases hm : m i
    · simp
    · have := ht i (by have := h.inside i hm; omega)
      simp only [ite_true]; unfold red at this; omega
  have h3 : sumZ (fun i => if m i then (len N s - 1) - ((s i : Int) + s (i + 1)) else 0) (hi + 1)
      = card m hi * (len N s - 1)
        - sumZ (fun i => if m i then (s i : Int) + s (i + 1) else 0) (hi + 1) := by
    unfold card
    rw [Int.mul_comm, ← sumZ_ite_const m (len N s - 1), ← sumZ_sub]
    exact sumZ_congr _ (fun j _ => by split <;> simp)
  have h4 := cover_sum h (fun j => (s j : Int))
  have h5 : edgeSum m (fun i => (α (i + 1) : Int)) hi ≤ edgeSum m (fun i => (s (i + 1) : Int)) hi := by
    apply sumZ_le; intro i hi'
    dsimp only
    split
    · rename_i hm
      have := hα (i + 1) (by
        simp only [Bool.and_eq_true] at hm
        have := h.inside _ hm.2; omega)
      omega
    · omega
  omega

/-! ### Facts about the length -/

theorem sum_all (N : Nat) (s : Nat → Nat) : sumZ (fun j => (s j : Int)) (N + 1) = len N s - N := by
  unfold len; omega

theorem sum_but_last (N : Nat) (s : Nat → Nat) :
    sumZ (fun j => (s j : Int)) N = len N s - N - s N := by
  unfold len; simp only [sumZ_succ]; omega

theorem sum_first (s : Nat → Nat) : sumZ (fun j => (s j : Int)) 1 = s 0 := by simp

/-! ## The five terms of T11502, each a sound upper bound on every window's reduction -/

/-- **Term 1** ("M-α_i-α_{i+1}-1"): the reduction of window i is at most M - 1 - α_i - α_{i+1}. -/
theorem term1_sound {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j) {M : Int} (hL : len N s ≤ M)
    {i : Nat} (hi : i < N) : red N s i ≤ M - α i - α (i + 1) - 1 := by
  have := hα i (by omega); have := hα (i + 1) (by omega)
  unfold red; omega

/-- **Term 2**, corrected.  For S as in term 2 (`Chain m 0 (N-1)`), k = |S|, E = Σ_{edges i} α_{i+1}:
  k·t ≤ (k-1)·M + (N-k) - E,  i.e.  t ≤ ((k-1)M + (N-k) - E)/k.
FakeMMAP's T11502 prints ((|S|-1)M - (N-|S|) + Σα_i)/|S|: both the (N-|S|) and the α sum have the wrong sign.
(The correct term is M - (M - (N-|S|) + E)/|S|, term 3's shape with M in place of A; T11503's first bound is this
correct term solved for M.) -/
theorem term2_sound {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j) {M : Int} (hL : len N s ≤ M)
    {m : Nat → Bool} (h : Chain m 0 (N - 1)) (hN : 1 ≤ N)
    {t : Int} (ht : ∀ i, i < N → t ≤ red N s i) :
    card m (N - 1) * t ≤ (card m (N - 1) - 1) * M + (N - card m (N - 1))
      - edgeSum m (fun i => (α (i + 1) : Int)) (N - 1) := by
  have hb := chain_bound hα h (by omega) ht
  have hk := card_pos h
  rw [show N - 1 + 2 = N + 1 by omega, sum_all] at hb
  have hm : (card m (N - 1) - 1) * len N s ≤ (card m (N - 1) - 1) * M :=
    Int.mul_le_mul_of_nonneg_left hL (by omega)
  simp only [sumZ_zero] at hb
  rw [Int.mul_sub, Int.mul_one] at hb
  rw [Int.sub_mul, Int.one_mul] at hm
  omega

/-- The common shape of terms 3, 4, 5: k·t ≤ k·(M-1) - (X - N + E) whenever the sections of the windows of S
(lo … hi+1) have total length (as a finish part with N quarter turns) at least X. -/
theorem side_bound {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j) {M : Int} (hL : len N s ≤ M)
    {m : Nat → Bool} {lo hi : Nat} (h : Chain m lo hi) (hN : hi < N)
    {t : Int} (ht : ∀ i, i < N → t ≤ red N s i) {X : Int}
    (hX : X ≤ N + (sumZ (fun j => (s j : Int)) (hi + 2) - sumZ (fun j => (s j : Int)) lo)) :
    card m hi * t ≤ card m hi * (M - 1) - (X - N + edgeSum m (fun i => (α (i + 1) : Int)) hi) := by
  have hb := chain_bound hα h hN ht
  have hk := card_pos h
  have hm : card m hi * (len N s - 1) ≤ card m hi * (M - 1) :=
    Int.mul_le_mul_of_nonneg_left (by omega) (by omega)
  omega

/-- **Term 3** (A, normal HTR): S as in term 3 (`Chain m 0 (N-2)`, N ≥ 2), A ≤ L - s_N:
  k·t ≤ k·(M-1) - (A - N + E),  i.e.  t ≤ M - (A - (N-k) + E)/k  as FakeMMAP writes it (with E = Σ α_{i+1}). -/
theorem term3_sound {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j) {M : Int} (hL : len N s ≤ M)
    {m : Nat → Bool} (h : Chain m 0 (N - 2)) (hN : 2 ≤ N)
    {t : Int} (ht : ∀ i, i < N → t ≤ red N s i) {A : Int} (hA : A ≤ len N s - s N) :
    card m (N - 2) * t ≤ card m (N - 2) * (M - 1) - (A - N + edgeSum m (fun i => (α (i + 1) : Int)) (N - 2)) := by
  apply side_bound hα hL h (by omega) ht
  rw [show N - 2 + 2 = N by omega, sum_but_last]; simp; omega

/-- **Term 4** (B, inverse HTR): S as in term 4 (`Chain m 1 (N-1)`), B ≤ L - s_0. -/
theorem term4_sound {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j) {M : Int} (hL : len N s ≤ M)
    {m : Nat → Bool} (h : Chain m 1 (N - 1)) (hN : 1 ≤ N)
    {t : Int} (ht : ∀ i, i < N → t ≤ red N s i) {B : Int} (hB : B ≤ len N s - s 0) :
    card m (N - 1) * t ≤ card m (N - 1) * (M - 1) - (B - N + edgeSum m (fun i => (α (i + 1) : Int)) (N - 1)) := by
  apply side_bound hα hL h (by omega) ht
  rw [show N - 1 + 2 = N + 1 by omega, sum_all, sum_first]; omega

/-- **Term 5** (C, the subset's shortest linear HTR, N > 2): S as in term 5 (`Chain m 1 (N-2)`),
C ≤ L - s_0 - s_N. -/
theorem term5_sound {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j) {M : Int} (hL : len N s ≤ M)
    {m : Nat → Bool} (h : Chain m 1 (N - 2)) (hN : 3 ≤ N)
    {t : Int} (ht : ∀ i, i < N → t ≤ red N s i) {C : Int} (hC : C ≤ len N s - s 0 - s N) :
    card m (N - 2) * t ≤ card m (N - 2) * (M - 1) - (C - N + edgeSum m (fun i => (α (i + 1) : Int)) (N - 2)) := by
  apply side_bound hα hL h (by omega) ht
  rw [show N - 2 + 2 = N by omega, sum_but_last, sum_first]; omega

/-! ## T11503: the same inequalities read as lower bounds on the finish length

"We're assuming we've tried all reductions of length strictly smaller than R'" — so every window's reduction is
≥ R'.  Then the finish (length L, FakeMMAP's M) satisfies the bounds below, with E = Σ_{edges i} α_{i+1}. -/

/-- T11503's "very stupid bounds" M ≥ A + α_N and M ≥ B + α_0. -/
theorem lower_stupid {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j) {A B : Int}
    (hA : A ≤ len N s - s N) (hB : B ≤ len N s - s 0) :
    A + α N ≤ len N s ∧ B + α 0 ≤ len N s := by
  have := hα N (Nat.le_refl _); have := hα 0 (Nat.zero_le _); omega

/-- T11503, first bound: (|S|-1)·L ≥ |S|(R'+1) - N + E, i.e. L ≥ (|S|(R'+1) - N + Σ α)/(|S|-1). -/
theorem lower_free {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j)
    {m : Nat → Bool} (h : Chain m 0 (N - 1)) (hN : 1 ≤ N)
    {R' : Int} (ht : ∀ i, i < N → R' ≤ red N s i) :
    card m (N - 1) * (R' + 1) - N + edgeSum m (fun i => (α (i + 1) : Int)) (N - 1)
      ≤ (card m (N - 1) - 1) * len N s := by
  have := term2_sound hα (Int.le_refl _) h hN ht
  rw [Int.mul_add, Int.mul_one]; omega

/-- T11503, second bound (A): |S|·L ≥ |S|(1+R') + A - N + E, i.e. L ≥ 1 + R' + (A - N + Σ α)/|S|. -/
theorem lower_A {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j)
    {m : Nat → Bool} (h : Chain m 0 (N - 2)) (hN : 2 ≤ N)
    {R' : Int} (ht : ∀ i, i < N → R' ≤ red N s i) {A : Int} (hA : A ≤ len N s - s N) :
    card m (N - 2) * (1 + R') + (A - N + edgeSum m (fun i => (α (i + 1) : Int)) (N - 2))
      ≤ card m (N - 2) * len N s := by
  have := term3_sound hα (Int.le_refl _) h hN ht hA
  rw [Int.mul_add, Int.mul_one]; rw [Int.mul_sub, Int.mul_one] at this; omega

/-- T11503, "similar for B". -/
theorem lower_B {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j)
    {m : Nat → Bool} (h : Chain m 1 (N - 1)) (hN : 1 ≤ N)
    {R' : Int} (ht : ∀ i, i < N → R' ≤ red N s i) {B : Int} (hB : B ≤ len N s - s 0) :
    card m (N - 1) * (1 + R') + (B - N + edgeSum m (fun i => (α (i + 1) : Int)) (N - 1))
      ≤ card m (N - 1) * len N s := by
  have := term4_sound hα (Int.le_refl _) h hN ht hB
  rw [Int.mul_add, Int.mul_one]; rw [Int.mul_sub, Int.mul_one] at this; omega

/-- T11503, "similar for … C" (N > 2). -/
theorem lower_C {N : Nat} {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j)
    {m : Nat → Bool} (h : Chain m 1 (N - 2)) (hN : 3 ≤ N)
    {R' : Int} (ht : ∀ i, i < N → R' ≤ red N s i) {C : Int} (hC : C ≤ len N s - s 0 - s N) :
    card m (N - 2) * (1 + R') + (C - N + edgeSum m (fun i => (α (i + 1) : Int)) (N - 2))
      ≤ card m (N - 2) * len N s := by
  have := term5_sound hα (Int.le_refl _) h hN ht hC
  rw [Int.mul_add, Int.mul_one]; rw [Int.mul_sub, Int.mul_one] at this; omega

end FakeBound
