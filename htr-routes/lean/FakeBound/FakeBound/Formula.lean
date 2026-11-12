/-
  FakeBound.Formula — FakeMMAP's R (T11502) as a function you can evaluate, its soundness, and the readings of it.

  T11502: "It turns out that the value of R is the max of some simple expressions involving M, A, B, C and the
  α_i's … R is the max of the following: 1) M-α_i-α_{i+1}-1 (basically leaving those two as the 1q finish,
  unlikely to be the maximum, unless M is VERY small). 2) … 3) … 4) … 5) …"

  Every term is an upper bound on the shortest reduction (FakeBound.Finish), so the bound that the linear program
  gives is their **minimum**.  "max" cannot be meant: with max, term 1 alone (≈ M-1) would make R useless, and
  term 1 would be the maximum when M is large, while FakeMMAP says it is "unlikely to be the maximum, unless M is
  VERY small" — which is how the minimum behaves (term 1 is the smallest term only for small M).  Both readings
  are formalized:
  * `Rmin` (the bound), proved sound with the corrected term 2 and α_{i+1};
  * `Rmax` (the word "max" as printed), sound for the trivial reason that term 1 is among the terms;
  * the printed term 2 and the printed α_i, under the min reading, are refuted in FakeBound.Counter.

  Floors: all lengths are integers, so t ≤ x/k (real) ⇔ t ≤ ⌊x/k⌋, and `Int` division `/` by a positive k is ⌊·⌋.
  Term 3 as printed, M - (A - (N-|S|) + Σα)/|S|, has floor (k·(M-1) - (A - N + E)) / k.
-/
import FakeBound.Finish

namespace FakeBound

/-! ### Subsets as Bool lists -/

/-- All Bool lists of length n (the subsets of {0, …, n-1}). -/
def allBools : Nat → List (List Bool)
  | 0 => [[]]
  | n + 1 => (allBools n).flatMap fun l => [false :: l, true :: l]

/-- Membership: i ∈ S iff entry i of the list is true (false past the end). -/
def memL (bs : List Bool) (i : Nat) : Bool := bs.getD i false

/-- The decidable form of `Chain`. -/
def isChain (bs : List Bool) (lo hi : Nat) : Bool :=
  memL bs lo && memL bs hi && bs.length == hi + 1 &&
  (List.range (hi + 1)).all (fun i => !memL bs i || decide (lo ≤ i)) &&
  (List.range hi).all (fun j => !decide (lo ≤ j) || memL bs j || memL bs (j + 1))

theorem memL_lt : ∀ {bs : List Bool} {i : Nat}, memL bs i = true → i < bs.length
  | [], i, h => by simp [memL] at h
  | b :: bs, 0, _ => by simp
  | b :: bs, i + 1, h => by
    have : memL bs i = true := by simpa [memL] using h
    have := memL_lt this; simp; omega

theorem isChain_sound {bs : List Bool} {lo hi : Nat} (h : isChain bs lo hi = true) :
    Chain (memL bs) lo hi := by
  simp only [isChain, Bool.and_eq_true, beq_iff_eq, List.all_eq_true, List.mem_range, Bool.or_eq_true,
    Bool.not_eq_true', decide_eq_true_eq] at h
  obtain ⟨⟨⟨⟨h1, h2⟩, h3⟩, h4⟩, h5⟩ := h
  refine ⟨h1, h2, ?_, ?_⟩
  · intro i hi'
    have hl := memL_lt hi'
    rcases h4 i (by omega) with h' | h'
    · rw [hi'] at h'; cases h'
    · exact ⟨h', by omega⟩
  · intro j hl hj
    rcases h5 j hj with (h' | h') | h'
    · exact absurd hl (by simpa using h')
    · exact Or.inl h'
    · exact Or.inr h'

/-- The chains of [lo, hi], enumerated. -/
def chains (lo hi : Nat) : List (List Bool) := (allBools (hi + 1)).filter (isChain · lo hi)

/-! ### The terms -/

/-- Which α the edge sum takes: `shift = 1` is α_{i+1} (proved right), `shift = 0` is α_i (as printed). -/
def edgeW (α : Nat → Nat) (shift : Nat) : Nat → Int := fun i => (α (i + shift) : Int)

def term1s (N : Nat) (α : Nat → Nat) (M : Int) : List Int :=
  (List.range N).map fun i => M - α i - α (i + 1) - 1

/-- Term 2.  `printed = false`: ((k-1)M + (N-k) - E)/k (proved); `printed = true`: ((k-1)M - (N-k) + E)/k, the
signs of T11502. -/
def term2 (N : Nat) (α : Nat → Nat) (M : Int) (shift : Nat) (printed : Bool) (bs : List Bool) : Int :=
  let k := card (memL bs) (N - 1)
  let E := edgeSum (memL bs) (edgeW α shift) (N - 1)
  if printed then ((k - 1) * M - (N - k) + E) / k else ((k - 1) * M + (N - k) - E) / k

/-- Terms 3, 4, 5: ⌊M - (X - (N-k) + E)/k⌋ = (k(M-1) - (X - N + E))/k. -/
def termX (N : Nat) (α : Nat → Nat) (M X : Int) (shift hi : Nat) (bs : List Bool) : Int :=
  let k := card (memL bs) hi
  (k * (M - 1) - (X - N + edgeSum (memL bs) (edgeW α shift) hi)) / k

/-- All of FakeMMAP's terms, over all the sets S of each kind (not only the minimal ones: the extra ones never
lower the minimum below the true worst case, since each is sound). -/
def terms (N : Nat) (α : Nat → Nat) (M A B C : Int) (shift : Nat) (printed : Bool) : List Int :=
  term1s N α M
  ++ (chains 0 (N - 1)).map (term2 N α M shift printed)
  ++ (if 2 ≤ N then (chains 0 (N - 2)).map (termX N α M A shift (N - 2)) else [])
  ++ (chains 1 (N - 1)).map (termX N α M B shift (N - 1))
  ++ (if 3 ≤ N then (chains 1 (N - 2)).map (termX N α M C shift (N - 2)) else [])

/-- R as the minimum of the terms (the linear program's bound). -/
def Rmin (N : Nat) (α : Nat → Nat) (M A B C : Int) (shift : Nat := 1) (printed : Bool := false) : Int :=
  (terms N α M A B C shift printed).foldl min M

/-- R as the maximum of the terms (the word in T11502). -/
def Rmax (N : Nat) (α : Nat → Nat) (M A B C : Int) (shift : Nat := 0) (printed : Bool := true) : Int :=
  (terms N α M A B C shift printed).foldl max (M - α 0 - α 1 - 1)

/-- The shortest reduction to 1q of the finish. -/
def minRed (N : Nat) (s : Nat → Nat) : Int := ((List.range N).map (red N s)).foldl min (len N s)

/-! ### min / max over lists -/

theorem le_foldl_min {t : Int} : ∀ (l : List Int) (init : Int), t ≤ init → (∀ x ∈ l, t ≤ x) → t ≤ l.foldl min init
  | [], _, h, _ => h
  | x :: l, init, h, hl => by
    simp only [List.foldl_cons]
    apply le_foldl_min l
    · have := hl x (by simp); omega
    · intro y hy; exact hl y (by simp [hy])

theorem foldl_min_le : ∀ (l : List Int) (init x : Int), x ∈ l → l.foldl min init ≤ x
  | [], _, _, h => by cases h
  | y :: l, init, x, h => by
    simp only [List.foldl_cons]
    have key : ∀ (l : List Int) (a b : Int), a ≤ b → l.foldl min a ≤ b := by
      intro l; induction l with
      | nil => intro a b h; exact h
      | cons z l ih => intro a b h; simp only [List.foldl_cons]; exact ih _ _ (by omega)
    rcases List.mem_cons.mp h with rfl | h
    · exact key l _ _ (by omega)
    · exact foldl_min_le l _ x h

theorem le_foldl_max : ∀ (l : List Int) (init : Int), init ≤ l.foldl max init
  | [], _ => Int.le_refl _
  | x :: l, init => by
    simp only [List.foldl_cons]
    have := le_foldl_max l (max init x); omega

theorem minRed_le {N : Nat} {s : Nat → Nat} {i : Nat} (hi : i < N) : minRed N s ≤ red N s i :=
  foldl_min_le _ _ _ (List.mem_map.mpr ⟨i, List.mem_range.mpr hi, rfl⟩)

/-! ### Soundness -/

/-- k·t ≤ x with k > 0 gives t ≤ x / k. -/
theorem le_div_of_mul {k t x : Int} (hk : 1 ≤ k) (h : k * t ≤ x) : t ≤ x / k :=
  (Int.le_ediv_iff_mul_le (by omega)).mpr (by rw [Int.mul_comm]; exact h)

/-- **FakeMMAP's R is sound** (min reading, corrected term 2, α_{i+1}).  For every finish with N ≥ 1 quarter turns
and length L ≤ M whose sections satisfy s_j ≥ α_j, with A ≤ L - s_N, B ≤ L - s_0 and (used only when N ≥ 3)
C ≤ L - s_0 - s_N, the shortest reduction to 1q has length ≤ R.  This holds for every N, every α, every M. -/
theorem Rmin_sound {N : Nat} (hN : 1 ≤ N) {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j)
    {M A B C : Int} (hL : len N s ≤ M) (hA : A ≤ len N s - s N) (hB : B ≤ len N s - s 0)
    (hC : 3 ≤ N → C ≤ len N s - s 0 - s N) :
    minRed N s ≤ Rmin N α M A B C := by
  have ht : ∀ i, i < N → minRed N s ≤ red N s i := fun i hi => minRed_le hi
  apply le_foldl_min
  · have := minRed_le (s := s) (show 0 < N by omega)
    have := term1_sound (i := 0) hα hL (show 0 < N by omega)
    have := hα 0 (Nat.zero_le _); have := hα 1 (by omega)
    simp only [Nat.zero_add] at *; omega
  intro x hx
  simp only [terms, List.mem_append] at hx
  rcases hx with (((h1 | h2) | h3) | h4) | h5
  · obtain ⟨i, hi, rfl⟩ := List.mem_map.mp h1
    have hi := List.mem_range.mp hi
    exact Int.le_trans (ht i hi) (term1_sound hα hL hi)
  · obtain ⟨bs, hbs, rfl⟩ := List.mem_map.mp h2
    have hch := isChain_sound (List.mem_filter.mp hbs).2
    exact le_div_of_mul (card_pos hch) (term2_sound hα hL hch hN ht)
  · by_cases h2N : 2 ≤ N
    · simp only [h2N, ↓reduceIte] at h3
      obtain ⟨bs, hbs, rfl⟩ := List.mem_map.mp h3
      have hch := isChain_sound (List.mem_filter.mp hbs).2
      exact le_div_of_mul (card_pos hch) (term3_sound hα hL hch h2N ht hA)
    · simp only [h2N, ↓reduceIte] at h3; cases h3
  · obtain ⟨bs, hbs, rfl⟩ := List.mem_map.mp h4
    have hch := isChain_sound (List.mem_filter.mp hbs).2
    exact le_div_of_mul (card_pos hch) (term4_sound hα hL hch hN ht hB)
  · by_cases h3N : 3 ≤ N
    · simp only [h3N, ↓reduceIte] at h5
      obtain ⟨bs, hbs, rfl⟩ := List.mem_map.mp h5
      have hch := isChain_sound (List.mem_filter.mp hbs).2
      exact le_div_of_mul (card_pos hch) (term5_sound hα hL hch h3N ht (hC h3N))
    · simp only [h3N, ↓reduceIte] at h5; cases h5

/-- **"max" as printed is sound, trivially**: whatever the other terms are (printed signs, α_i), the maximum is at
least term 1 for window 0, which already bounds the reduction of window 0.  It is as weak as M - 1 - α_0 - α_1. -/
theorem Rmax_sound {N : Nat} (hN : 1 ≤ N) {s α : Nat → Nat} (hα : ∀ j, j ≤ N → α j ≤ s j)
    {M : Int} (hL : len N s ≤ M) (A B C : Int) (shift : Nat) (printed : Bool) :
    minRed N s ≤ Rmax N α M A B C shift printed := by
  have := minRed_le (s := s) (show 0 < N by omega)
  have := term1_sound (i := 0) hα hL (show 0 < N by omega)
  simp only [Nat.zero_add] at this
  have := le_foldl_max (terms N α M A B C shift printed) (M - α 0 - α 1 - 1)
  unfold Rmax; omega

end FakeBound
