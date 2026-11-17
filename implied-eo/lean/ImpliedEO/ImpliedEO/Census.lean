/-
Every EO of 5 moves or less: no two of them are linked by anything but the trick.

The EO cases reachable with exactly k moves are computed layer by layer (k = 0..5) on each axis; a lemma says the
case of every sequence of length k is in layer k, so the finite checks below speak about every sequence.
-/
import ImpliedEO.CensusDefs
namespace ImpliedEO

theorem spots_idx : ∀ x, spots[idx x]? = some x := by decide

theorem tab_at (f : Facelet → Bool) (x : Facelet) : (tab f).at x = f x := by
  unfold Tab.at tab
  rw [List.getD_eq_getElem?_getD, List.getElem?_map, spots_idx]
  rfl
theorem tab_eq_iff (f g : Facelet → Bool) : tab f = tab g ↔ ∀ x, f x = g x := by
  constructor
  · intro h x; rw [← tab_at f x, ← tab_at g x, h]
  · intro h; unfold tab; exact List.map_congr_left (fun x _ => h x)

theorem bool_aux7 : ∀ p q r c d : Bool,
    ((p != r) != c) = (((p != q) != (c != d)) != ((q != r) != d)) := by decide
theorem kcase_cons (a : Axis) (m : Move) (s : List Move) (x : Facelet) :
    kcase a (m :: s) x = (cst a m x != kcase a s (mv m x)) := by
  unfold kcase flips cst
  rw [run_cons]
  exact bool_aux7 _ _ _ _ _

theorem tab_cons (a : Axis) (m : Move) (s : List Move) :
    tab (kcase a (m :: s)) = stepT a m (tab (kcase a s)) := by
  unfold stepT
  rw [tab_eq_iff]
  intro x
  rw [kcase_cons, tab_at]

theorem mem_dedup (t : Tab) (l : List Tab) : t ∈ dedup l ↔ t ∈ l := by
  induction l with
  | nil => simp [dedup]
  | cons u l ih =>
    simp only [dedup]
    split
    · rename_i h
      have hu : u ∈ dedup l := by simpa using h
      constructor
      · intro h1; exact List.mem_cons_of_mem _ (ih.mp h1)
      · intro h1
        rcases List.mem_cons.mp h1 with rfl | h2
        · exact hu
        · exact ih.mpr h2
    · simp [ih]

theorem Move.mem_all : ∀ m : Move, m ∈ Move.all := by decide

theorem mem_layer (a : Axis) (s : List Move) : tab (kcase a s) ∈ layer a s.length := by
  induction s with
  | nil => simp [layer]
  | cons m s ih =>
    show _ ∈ dedup ((layer a s.length).flatMap fun t => Move.all.map fun m => stepT a m t)
    rw [mem_dedup, List.mem_flatMap]
    exact ⟨_, ih, List.mem_map.mpr ⟨m, Move.mem_all m, (tab_cons a m s).symm⟩⟩

theorem mem_pres (a : Axis) (s : List Move) (h : s.length ≤ 5) :
    (s.length, tab (kcase a s)) ∈ pres a := by
  unfold pres
  rw [List.mem_flatMap]
  exact ⟨s.length, List.mem_range.mpr (by omega), List.mem_map.mpr ⟨_, mem_layer a s, rfl⟩⟩

theorem neg_tab (f : Facelet → Bool) : neg (tab f) = tab (fun x => !f x) := by
  simp [neg, tab]

/-- There is not, on any pair of axes (the same axis twice included).  Computed. -/
theorem no_clash : ∀ a b : Axis, clash (pres a) (pres b) = false := by native_decide

theorem bool_aux8 : ∀ a b : Bool, (a != b) = false → a = b := by decide
theorem bool_aux9 : ∀ a b : Bool, (a != b) = true → a = !b := by decide

theorem EO.same_cases_or_comp (X Y : EO) (h : X.same Y) :
    ((∀ y, X.invCase y = Y.invCase y) ∧ (∀ z, X.norCase z = Y.norCase z)) ∨
    ((∀ y, X.invCase y = !Y.invCase y) ∧ (∀ z, X.norCase z = !Y.norCase z)) := by
  cases hb : (X.norCase base != Y.norCase base) with
  | false =>
    left
    refine ⟨fun y => bool_aux8 _ _ ?_, fun z => bool_aux8 _ _ ?_⟩
    · rw [h y base, hb]
    · rw [← h base z, h base base, hb]
  | true =>
    right
    refine ⟨fun y => bool_aux9 _ _ ?_, fun z => bool_aux9 _ _ ?_⟩
    · rw [h y base, hb]
    · rw [← h base z, h base base, hb]

/-- **Up to 5 moves, an implied EO always has the same two cases** (never the complemented ones):
if one EO of at most 5 moves implies another of at most 5, the two have the same normal case and the same
inverse case in the axis-free form. -/
theorem same_cases_of_implies (X Y : EO) (hX : X.len ≤ 5) (hY : Y.len ≤ 5)
    (h : ∀ scr, X.holds scr → Y.holds scr) :
    (∀ y, X.invCase y = Y.invCase y) ∧ (∀ z, X.norCase z = Y.norCase z) := by
  rcases EO.same_cases_or_comp X Y ((EO.implies_iff_same X Y).mp h) with h1 | h1
  · exact h1
  · exfalso
    have hc := no_clash X.axis Y.axis
    unfold EO.len at hX hY
    have e1 : tab (kcase Y.axis Y.inverse) = neg (tab (kcase X.axis X.inverse)) := by
      rw [neg_tab, tab_eq_iff]; intro x
      have := h1.1 x
      unfold EO.invCase at this
      rw [this]; cases kcase Y.axis Y.inverse x <;> rfl
    have e2 : tab (kcase Y.axis Y.normal) = neg (tab (kcase X.axis X.normal)) := by
      rw [neg_tab, tab_eq_iff]; intro x
      have := h1.2 x
      unfold EO.norCase at this
      rw [this]; cases kcase Y.axis Y.normal x <;> rfl
    have m1 : (X.inverse.length, Y.inverse.length) ∈ sides (pres X.axis) (pres Y.axis) := by
      unfold sides
      rw [List.mem_flatMap]
      refine ⟨_, mem_pres X.axis X.inverse (by omega), ?_⟩
      rw [List.mem_filterMap]
      exact ⟨_, mem_pres Y.axis Y.inverse (by omega), by simp [e1]⟩
    have m2 : (X.normal.length, Y.normal.length) ∈ sides (pres X.axis) (pres Y.axis) := by
      unfold sides
      rw [List.mem_flatMap]
      refine ⟨_, mem_pres X.axis X.normal (by omega), ?_⟩
      rw [List.mem_filterMap]
      exact ⟨_, mem_pres Y.axis Y.normal (by omega), by simp [e2]⟩
    have : clash (pres X.axis) (pres Y.axis) = true := by
      unfold clash
      simp only [List.any_eq_true, Bool.and_eq_true, decide_eq_true_eq]
      exact ⟨_, m1, _, m2, by simp; omega, by simp; omega⟩
    rw [hc] at this
    exact absurd this (by decide)

/-! ### Same cases on another axis is what the trick gives -/

/-- The four moves of the trick from axis `a` to axis `b`: the quarter turns of `a` first. -/
def four : Axis → Axis → List Move
  | .fb, .rl => [Mv.F, Mv.B, Mv.R, Mv.L]
  | .fb, .ud => [Mv.F, Mv.B, Mv.U, Mv.D]
  | .rl, .fb => [Mv.R, Mv.L, Mv.F, Mv.B]
  | .rl, .ud => [Mv.R, Mv.L, Mv.U, Mv.D]
  | .ud, .fb => [Mv.U, Mv.D, Mv.F, Mv.B]
  | .ud, .rl => [Mv.U, Mv.D, Mv.R, Mv.L]
  | _, _ => []
theorem four_ok : ∀ a b, a ≠ b → ∀ y, key b (run (four a b) y) = (key a y != (sgn a != sgn b)) := by decide
theorem bool_aux10 : ∀ q cb sb r sa ca : Bool,
    ((((q != cb) != sb) != (r != (sa != sb))) != cb) = ((((q != ca) != sa) != r) != ca) := by decide
/-- Adding the four moves to a sequence leaves its axis-free case as it was. -/
theorem kcase_four (a b : Axis) (hab : a ≠ b) (N : List Move) (x : Facelet) :
    kcase b (N ++ four a b) x = kcase a N x := by
  unfold kcase flips
  rw [run_append, four_ok a b hab, key_q b x, key_q a x]
  exact bool_aux10 _ _ _ _ _ _

/-- **Up to 5 moves, every implied EO is the trick.**  If an EO of at most 5 moves implies another of at most 5
on a different axis, then the second one's normal part solves the same EO case as the first one's normal part
followed by the four moves, and the same for the inverse parts. -/
theorem only_the_trick (X Y : EO) (hX : X.len ≤ 5) (hY : Y.len ≤ 5) (hab : X.axis ≠ Y.axis)
    (h : ∀ scr, X.holds scr → Y.holds scr) :
    (∀ z, flips Y.axis Y.normal z = flips Y.axis (X.normal ++ four X.axis Y.axis) z) ∧
    (∀ y, flips Y.axis Y.inverse y = flips Y.axis (X.inverse ++ four X.axis Y.axis) y) := by
  have hc := same_cases_of_implies X Y hX hY h
  constructor
  · intro z
    have h1 := hc.2 z
    unfold EO.norCase at h1
    rw [← kcase_four X.axis Y.axis hab] at h1
    unfold kcase at h1
    revert h1
    generalize flips Y.axis (X.normal ++ four X.axis Y.axis) z = p
    generalize flips Y.axis Y.normal z = q
    generalize across Y.axis z = c
    cases p <;> cases q <;> cases c <;> simp
  · intro y
    have h1 := hc.1 y
    unfold EO.invCase at h1
    rw [← kcase_four X.axis Y.axis hab] at h1
    unfold kcase at h1
    revert h1
    generalize flips Y.axis (X.inverse ++ four X.axis Y.axis) y = p
    generalize flips Y.axis Y.inverse y = q
    generalize across Y.axis y = c
    cases p <;> cases q <;> cases c <;> simp

/-- On one axis, up to 5 moves: an implied EO solves the same two cases (it is the same EO solved differently). -/
theorem same_axis (X Y : EO) (hX : X.len ≤ 5) (hY : Y.len ≤ 5) (hab : X.axis = Y.axis)
    (h : ∀ scr, X.holds scr → Y.holds scr) :
    (∀ z, flips Y.axis Y.normal z = flips X.axis X.normal z) ∧
    (∀ y, flips Y.axis Y.inverse y = flips X.axis X.inverse y) := by
  have hc := same_cases_of_implies X Y hX hY h
  constructor
  · intro z
    have h1 := hc.2 z
    unfold EO.norCase kcase at h1
    rw [hab] at h1 ⊢
    revert h1
    generalize flips Y.axis X.normal z = p
    generalize flips Y.axis Y.normal z = q
    generalize across Y.axis z = c
    cases p <;> cases q <;> cases c <;> simp
  · intro y
    have h1 := hc.1 y
    unfold EO.invCase kcase at h1
    rw [hab] at h1 ⊢
    revert h1
    generalize flips Y.axis X.inverse y = p
    generalize flips Y.axis Y.inverse y = q
    generalize across Y.axis y = c
    cases p <;> cases q <;> cases c <;> simp

/-! ### The counts -/

/-- EO cases by length, 0 to 5 moves, on each axis: 1, 2, 25, 202, 620, 900. -/
theorem cases_by_length : ∀ a : Axis,
    (List.range 6).map (fun k => ((mins a).filter fun p => p.2 == k).length) = [1, 2, 25, 202, 620, 900] := by
  native_decide

/-- 239 pairs of cases are an EO of at most 5 on each two axes, 13 of them on all three:
3 × 239 − 2 × 13 = 691 sets of scrambles with two or more EOs of at most 5 moves. -/
theorem census : (shared .fb .rl).length = 239 ∧ (shared .fb .ud).length = 239 ∧ (shared .rl .ud).length = 239 ∧
    ((shared .fb .rl).filter fun p => (shared .fb .ud).contains p).length = 13 := by
  native_decide

end ImpliedEO
