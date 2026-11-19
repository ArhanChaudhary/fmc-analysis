/-
  Corners3D.Proofs — what the checks mean for every sequence of turns.

  The theorems here are proved by induction on the sequence of turns; no `native_decide` appears in this file.
  The only computations they rest on are the checks of `Theorems.lean` (each a statement about one state and one
  turn, run over all 3,674,160 states), which enter as hypotheses of the form "the check returned true".

  A sequence of turns is a list of numbers 0 … 8 (R R2 R' U U2 U' F F2 F'); `run x ms` is the state after doing
  `ms` to state `x`, `ms.length` its number of turns and `quarters ms` its number of quarter turns.
-/
import Corners3D.Theorems
namespace Corners3D
namespace proofs
open corners checks

/-- Every entry is one of the nine turns. -/
def Turns (ms : List Nat) : Prop := ∀ m ∈ ms, m < 9

/-! ### Small tools -/

theorem allBelow_true {n : Nat} {p : Nat → Bool} (h : allBelow n p = true) (x : Nat) (hx : x < n) :
    p x = true := by
  unfold allBelow at h
  exact List.all_eq_true.mp h x (List.mem_range.mpr hx)

theorem run_nil (x : Nat) : run x [] = x := rfl
theorem run_cons (x m : Nat) (ms : List Nat) : run x (m :: ms) = run (step x m) ms := rfl
theorem run_append (x : Nat) (a b : List Nat) : run x (a ++ b) = run (run x a) b := by
  unfold run
  exact List.foldl_append

theorem turns_cons {m : Nat} {ms : List Nat} (h : Turns (m :: ms)) : m < 9 ∧ Turns ms :=
  ⟨h m (List.mem_cons_self ..), fun m' hm' => h m' (List.mem_cons_of_mem _ hm')⟩

theorem quarters_cons (m : Nat) (ms : List Nat) :
    quarters (m :: ms) = (if isQuarter m = true then 1 else 0) + quarters ms := by
  unfold quarters
  by_cases h : isQuarter m = true
  · simp [h]; omega
  · simp [h]

/-- No turn leaves the coordinates. -/
theorem step_lt {x m : Nat} (hx : x < N) (hm : m < 9) : step x m < N := by
  have h := closed_ok
  unfold closedOK at h
  have h1 : allBelow 9 (fun m => decide (step x m < N)) = true := allBelow_true h x hx
  exact of_decide_eq_true (allBelow_true h1 m hm)

theorem run_lt : ∀ (ms : List Nat) (x : Nat), x < N → Turns ms → run x ms < N := by
  intro ms
  induction ms with
  | nil => intro x hx _; exact hx
  | cons m ms ih =>
    intro x hx ht
    have ⟨hm, ht'⟩ := turns_cons ht
    exact ih (step x m) (step_lt hx hm) ht'

/-! ### Floors: the general statements -/

/-- **A floor from a local check.**  If f is 0 on the goal and no turn lowers f by more than 1, then every
sequence of turns from x into the goal has at least f x turns. -/
theorem floor_of_check {f : Nat → Nat} {goal : Nat → Bool} (h : floorOK f goal () = true) :
    ∀ (ms : List Nat) (x : Nat), x < N → Turns ms → goal (run x ms) = true → f x ≤ ms.length := by
  unfold floorOK at h
  intro ms
  induction ms with
  | nil =>
    intro x hx _ hg
    have h1 := allBelow_true h x hx
    simp only [Bool.and_eq_true, Bool.or_eq_true, Bool.not_eq_true', beq_iff_eq] at h1
    rw [run_nil] at hg
    rcases h1.1 with h2 | h2
    · rw [hg] at h2; cases h2
    · simp [h2]
  | cons m ms ih =>
    intro x hx ht hg
    have ⟨hm, ht'⟩ := turns_cons ht
    have h1 := allBelow_true h x hx
    simp only [Bool.and_eq_true] at h1
    have h2 : f x ≤ f (step x m) + 1 := of_decide_eq_true (allBelow_true h1.2 m hm)
    have h3 := ih (step x m) (step_lt hx hm) ht' hg
    simp only [List.length_cons]
    omega

/-- **A quarter-turn floor from a local check.**  If g is 0 on the goal, half turns do not lower g and a
quarter turn lowers it by at most c, then every sequence of turns from x into the goal has at least g x / c
quarter turns: c × (its quarter turns) ≥ g x. -/
theorem wfloor_of_check {g : Nat → Nat} {c : Nat} {goal : Nat → Bool} (h : wfloorOK g c goal () = true) :
    ∀ (ms : List Nat) (x : Nat), x < N → Turns ms → goal (run x ms) = true → g x ≤ c * quarters ms := by
  unfold wfloorOK at h
  intro ms
  induction ms with
  | nil =>
    intro x hx _ hg
    have h1 := allBelow_true h x hx
    simp only [Bool.and_eq_true, Bool.or_eq_true, Bool.not_eq_true', beq_iff_eq] at h1
    rw [run_nil] at hg
    rcases h1.1 with h2 | h2
    · rw [hg] at h2; cases h2
    · simp [h2]
  | cons m ms ih =>
    intro x hx ht hg
    have ⟨hm, ht'⟩ := turns_cons ht
    have h1 := allBelow_true h x hx
    simp only [Bool.and_eq_true] at h1
    have h2 : g x ≤ g (step x m) + (if isQuarter m = true then c else 0) :=
      of_decide_eq_true (allBelow_true h1.2 m hm)
    have h3 := ih (step x m) (step_lt hx hm) ht' hg
    rw [quarters_cons, Nat.mul_add]
    by_cases hq : isQuarter m = true
    · rw [ite_eq_left hq] at h2; rw [ite_eq_left hq, Nat.mul_one]; omega
    · rw [ite_eq_right hq] at h2; rw [ite_eq_right hq, Nat.mul_zero]; omega

/-- **An exact table from a local check.**  If f is 0 exactly on the goal, no turn lowers f by more than 1 and
off the goal some turn lowers it by 1, then f x is exactly the fewest turns from x into the goal: some
sequence of f x turns gets there, and none shorter does. -/
theorem exact_of_check {f : Nat → Nat} {goal : Nat → Bool} (h : exactOK f goal () = true) (x : Nat) (hx : x < N) :
    (∃ ms, Turns ms ∧ ms.length = f x ∧ goal (run x ms) = true) ∧
    (∀ ms, Turns ms → goal (run x ms) = true → f x ≤ ms.length) := by
  unfold exactOK at h
  constructor
  · -- a sequence of f x turns, by induction on the value
    have key : ∀ (n x : Nat), x < N → f x = n → ∃ ms, Turns ms ∧ ms.length = n ∧ goal (run x ms) = true := by
      intro n
      induction n with
      | zero =>
        intro x hx hf
        have h1 := allBelow_true h x hx
        simp only [Bool.and_eq_true, beq_iff_eq] at h1
        refine ⟨[], (by intro m hm; cases hm), rfl, ?_⟩
        rw [run_nil, h1.1.1, hf]; rfl
      | succ n ih =>
        intro x hx hf
        have h1 := allBelow_true h x hx
        simp only [Bool.and_eq_true, Bool.or_eq_true, beq_iff_eq, List.any_eq_true, List.mem_range] at h1
        rcases h1.2 with h2 | ⟨m, hm, h2⟩
        · omega
        · have hstep : f (step x m) = n := by omega
          obtain ⟨ms, ht, hl, hg⟩ := ih (step x m) (step_lt hx hm) hstep
          refine ⟨m :: ms, ?_, by simp [hl], hg⟩
          intro m' hm'
          rcases List.mem_cons.mp hm' with rfl | hm''
          · exact hm
          · exact ht m' hm''
    exact key (f x) x hx rfl
  · -- nothing shorter: the floor argument
    have hfloor : floorOK f goal () = true := by
      unfold floorOK allBelow
      unfold allBelow at h
      apply List.all_eq_true.mpr
      intro y hy
      have h1 := List.all_eq_true.mp h y hy
      simp only [Bool.and_eq_true, beq_iff_eq] at h1
      simp only [Bool.and_eq_true, Bool.or_eq_true, Bool.not_eq_true', beq_iff_eq]
      refine ⟨?_, h1.1.2⟩
      by_cases hg : goal y = true
      · right
        have := h1.1.1
        rw [hg] at this
        exact of_decide_eq_true (by simpa using this.symm)
      · left; simpa using hg
    intro ms ht hg
    exact floor_of_check hfloor ms x hx ht hg

/-! ### The kinds follow a rule of their own -/

theorem kinds_step {x m : Nat} (hx : x < N) (hm : m < 9) : kinds (step x m) = kindStep m (kinds x) := by
  have h := quarter_rule
  unfold ruleOK at h
  have h1 : allBelow 9 (fun m => kinds (step x m) == kindStep m (kinds x)) = true := allBelow_true h x hx
  exact eq_of_beq (allBelow_true h1 m hm)

/-- **Same kinds now, same kinds after any sequence of turns.**  What the corners show (good / twisted / out)
evolves by a rule that looks at nothing else, so two states that show the same kinds keep showing the same
kinds whatever is done to both. -/
theorem same_kinds_stay_same : ∀ (ms : List Nat) (x y : Nat), x < N → y < N → Turns ms →
    kinds x = kinds y → kinds (run x ms) = kinds (run y ms) := by
  intro ms
  induction ms with
  | nil => intro x y _ _ _ h; exact h
  | cons m ms ih =>
    intro x y hx hy ht h
    have ⟨hm, ht'⟩ := turns_cons ht
    have hs : kinds (step x m) = kinds (step y m) := by rw [kinds_step hx hm, kinds_step hy hm, h]
    exact ih (step x m) (step y m) (step_lt hx hm) (step_lt hy hm) ht' hs

/-- So a sequence that makes one of them all good makes the other all good too. -/
theorem same_kinds_same_solution (ms : List Nat) (x y : Nat) (hx : x < N) (hy : y < N) (ht : Turns ms)
    (h : kinds x = kinds y) (hsol : allGood (run x ms) = true) : allGood (run y ms) = true := by
  unfold allGood at hsol ⊢
  rw [← same_kinds_stay_same ms x y hx hy ht h]
  exact hsol

/-! ### Turns can be undone -/

theorem step_inv {x m : Nat} (hx : x < N) (hm : m < 9) : step (step x m) (invTurn m) = x := by
  have h := inv_ok
  unfold invOK at h
  have h1 : allBelow 9 (fun m => step (step x m) (invTurn m) == x) = true := allBelow_true h x hx
  exact eq_of_beq (allBelow_true h1 m hm)

theorem invTurn_lt {m : Nat} (hm : m < 9) : invTurn m < 9 := by unfold invTurn; omega
theorem invTurn_invTurn {m : Nat} (hm : m < 9) : invTurn (invTurn m) = m := by unfold invTurn; omega

theorem step_inv' {x m : Nat} (hx : x < N) (hm : m < 9) : step (step x (invTurn m)) m = x := by
  have h := step_inv hx (invTurn_lt hm)
  rw [invTurn_invTurn hm] at h
  exact h

theorem step_injective {x y m : Nat} (hx : x < N) (hy : y < N) (hm : m < 9) (h : step x m = step y m) :
    x = y := by
  have h1 := step_inv hx hm
  rw [h, step_inv hy hm] at h1
  exact h1.symm

/-- **A sequence of turns never sends two states to the same state.** -/
theorem run_injective : ∀ (ms : List Nat) (x y : Nat), x < N → y < N → Turns ms →
    run x ms = run y ms → x = y := by
  intro ms
  induction ms with
  | nil => intro x y _ _ _ h; exact h
  | cons m ms ih =>
    intro x y hx hy ht h
    have ⟨hm, ht'⟩ := turns_cons ht
    exact step_injective hx hy hm (ih (step x m) (step y m) (step_lt hx hm) (step_lt hy hm) ht' h)

theorem invSeq_cons (m : Nat) (ms : List Nat) : invSeq (m :: ms) = invSeq ms ++ [invTurn m] := by
  simp [invSeq]

theorem turns_invSeq {ms : List Nat} (h : Turns ms) : Turns (invSeq ms) := by
  intro m hm
  unfold invSeq at hm
  rcases List.mem_map.mp (List.mem_reverse.mp hm) with ⟨m', hm', rfl⟩
  exact invTurn_lt (h m' hm')

/-- Doing the inverse sequence first and then the sequence gives the state back. -/
theorem run_invSeq : ∀ (ms : List Nat) (x : Nat), x < N → Turns ms → run (run x (invSeq ms)) ms = x := by
  intro ms
  induction ms with
  | nil => intro x _ _; rfl
  | cons m ms ih =>
    intro x hx ht
    have ⟨hm, ht'⟩ := turns_cons ht
    have hz : run x (invSeq ms) < N := run_lt _ x hx (turns_invSeq ht')
    rw [invSeq_cons, run_append, run_cons (run x (invSeq ms)) (invTurn m) [], run_nil,
      run_cons (step (run x (invSeq ms)) (invTurn m)) m ms, step_inv' hz hm]
    exact ih x hx ht'

/-- Doing the sequence and then its inverse gives the state back. -/
theorem run_then_invSeq : ∀ (ms : List Nat) (x : Nat), x < N → Turns ms → run (run x ms) (invSeq ms) = x := by
  intro ms
  induction ms with
  | nil => intro x _ _; rfl
  | cons m ms ih =>
    intro x hx ht
    have ⟨hm, ht'⟩ := turns_cons ht
    rw [invSeq_cons, run_append, run_cons x m ms, ih (step x m) (step_lt hx hm) ht',
      run_cons (step x m) (invTurn m) [], run_nil, step_inv hx hm]

/-! ### Types alone find HTR one time in six -/

/-- **A sequence that makes a state all good sends the states that show the same kinds one to one onto the
all-good states.**  Take any sequence `ms` that makes every corner of `x` good, and any all-good state `g`.
Then exactly one state `t` showing the same kinds as `x` is sent to `g` by `ms`.

With `good_counts` (144 all-good states, 24 of them HTR) and `types_class_size` (144 states per kinds pattern)
this is the 1 in 6: of the 144 states that look like `x` to someone who reads only the kinds, `ms` puts exactly
24 into HTR and the other 120 into the fake HTR states (which are 9 turns from HTR, `fake_htr_far`). -/
theorem types_solution_hits_every_good_state (ms : List Nat) (x g : Nat) (hx : x < N) (hg : g < N)
    (ht : Turns ms) (hsol : allGood (run x ms) = true) (hgood : allGood g = true) :
    ∃ t, t < N ∧ kinds t = kinds x ∧ run t ms = g ∧ ∀ t', t' < N → run t' ms = g → t' = t := by
  have hti := turns_invSeq ht
  have ht_lt : run g (invSeq ms) < N := run_lt _ g hg hti
  have hrun : run (run g (invSeq ms)) ms = g := run_invSeq ms g hg ht
  refine ⟨run g (invSeq ms), ht_lt, ?_, hrun, ?_⟩
  · -- both g and run x ms are all good, so they show the same kinds; undo ms on both
    have hk : kinds g = kinds (run x ms) := by
      unfold allGood at hsol hgood
      rw [eq_of_beq hsol, eq_of_beq hgood]
    have h1 := same_kinds_stay_same (invSeq ms) g (run x ms) hg (run_lt _ x hx ht) hti hk
    rw [run_then_invSeq ms x hx ht] at h1
    exact h1
  · intro t' ht' h'
    exact run_injective ms t' (run g (invSeq ms)) ht' ht_lt ht (by rw [h', hrun])

/-! ### The theorems of the study -/

/-- **`dHTR` is exact.**  For every state: some sequence of `dHTR` turns reaches HTR, and no shorter one does. -/
theorem dHTR_exact (x : Nat) (hx : x < N) :
    (∃ ms, Turns ms ∧ ms.length = fHTR x ∧ inHTR (run x ms) = true) ∧
    (∀ ms, Turns ms → inHTR (run x ms) = true → fHTR x ≤ ms.length) :=
  exact_of_check dHTR_check x hx

/-- **`dGood` is exact**: the fewest turns to "every corner good" (triple DR). -/
theorem dGood_exact (x : Nat) (hx : x < N) :
    (∃ ms, Turns ms ∧ ms.length = fGood x ∧ allGood (run x ms) = true) ∧
    (∀ ms, Turns ms → allGood (run x ms) = true → fGood x ≤ ms.length) :=
  exact_of_check dGood_check x hx

/-- **`dGoodEven` is exact**: the fewest turns to "every corner good, even placement". -/
theorem dGoodEven_exact (x : Nat) (hx : x < N) :
    (∃ ms, Turns ms ∧ ms.length = fGoodEven x ∧ goodEven (run x ms) = true) ∧
    (∀ ms, Turns ms → goodEven (run x ms) = true → fGoodEven x ≤ ms.length) :=
  exact_of_check dGoodEven_check x hx

/-- **Every coordinate is a state of the puzzle**: a sequence of turns takes solved to it. -/
theorem every_state_reached (x : Nat) (hx : x < N) : ∃ ms, Turns ms ∧ run SOLVEDX ms = x := by
  obtain ⟨ms, ht, _, hg⟩ := (exact_of_check all_reached.1 x hx).1
  refine ⟨invSeq ms, turns_invSeq ht, ?_⟩
  have hs : run x ms = SOLVEDX := by
    unfold isSolved at hg
    exact eq_of_beq hg
  rw [← hs]
  exact run_then_invSeq ms x hx ht

/-- **The types floor.**  A state cannot reach HTR in fewer turns than it takes to make every corner good
(to reach triple DR).  `fGood x` is that number, a function of the kinds alone. -/
theorem types_floor (ms : List Nat) (x : Nat) (hx : x < N) (ht : Turns ms) (h : inHTR (run x ms) = true) :
    fGood x ≤ ms.length :=
  floor_of_check types_floor_check ms x hx ht h

/-- **The parity floor.**  Nor in fewer turns than it takes to make every corner good with an even placement. -/
theorem parity_floor (ms : List Nat) (x : Nat) (hx : x < N) (ht : Turns ms) (h : inHTR (run x ms) = true) :
    fGoodEven x ≤ ms.length :=
  floor_of_check parity_floor_check ms x hx ht h

/-- **The placement floor.**  Nor in fewer turns than the placement alone needs, twists ignored. -/
theorem placement_floor (ms : List Nat) (x : Nat) (hx : x < N) (ht : Turns ms) (h : inHTR (run x ms) = true) :
    fPerm x ≤ ms.length :=
  floor_of_check placement_floor_check ms x hx ht h

/-- **The weight floor.**  Count 1 for each out corner and 2 for each twisted corner.  Every solution to HTR
has at least a quarter of that many quarter turns. -/
theorem weight_floor (ms : List Nat) (x : Nat) (hx : x < N) (ht : Turns ms) (h : inHTR (run x ms) = true) :
    weight x ≤ 4 * quarters ms :=
  wfloor_of_check weight_floor_check ms x hx ht h

/-- **Quarter-turn floors.**  Every solution to HTR has at least `qHTR` quarter turns (so `qHTR`, which some
solution attains by `qHTR_exact`, is the fewest), at least as many as it takes to make every corner good, with
an even placement too, and at least the placement-only count. -/
theorem quarter_floors (ms : List Nat) (x : Nat) (hx : x < N) (ht : Turns ms) (h : inHTR (run x ms) = true) :
    gHTR x ≤ quarters ms ∧ gGood x ≤ quarters ms ∧ gGoodEven x ≤ quarters ms ∧ gPerm x ≤ quarters ms := by
  have h1 := wfloor_of_check quarter_floor_checks.1 ms x hx ht h
  have h2 := wfloor_of_check quarter_floor_checks.2.1 ms x hx ht h
  have h3 := wfloor_of_check quarter_floor_checks.2.2.1 ms x hx ht h
  have h4 := wfloor_of_check quarter_floor_checks.2.2.2 ms x hx ht h
  simp only [Nat.one_mul] at h1 h2 h3 h4
  exact ⟨h1, h2, h3, h4⟩

/-- The three floors in turns never exceed the true distance (each is a floor, and some solution has exactly
`dHTR` turns). -/
theorem floors_le_distance (x : Nat) (hx : x < N) : fGood x ≤ fHTR x ∧ fGoodEven x ≤ fHTR x ∧ fPerm x ≤ fHTR x := by
  obtain ⟨ms, ht, hl, hg⟩ := (dHTR_exact x hx).1
  have h1 := types_floor ms x hx ht hg
  have h2 := parity_floor ms x hx ht hg
  have h3 := placement_floor ms x hx ht hg
  omega

/-- **HTR, read off the cube.**  A state is in HTR exactly when every corner is good, the D-coloured corners
sit in one of the six pictures, and the placement is even. -/
theorem htr_iff (x : Nat) (hx : x < N) :
    inHTR x = true ↔ (allGood x = true ∧ SIX.contains (colourY x) = true ∧ odd x = false) := by
  have h := htr_iff_check
  unfold htrIffOK at h
  have h1 : inHTR x = (allGood x && SIX.contains (colourY x) && !odd x) := eq_of_beq (allBelow_true h x hx)
  rw [h1]
  simp [Bool.and_eq_true, and_assoc]

end proofs
end Corners3D
