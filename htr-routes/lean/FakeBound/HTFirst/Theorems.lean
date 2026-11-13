/-
  HTFirst.Theorems — the statements of the reference table "Half turns before the first quarter turn" that hold
  for every DR state, as theorems about DRBound's states and move sequences.

  A finish of g is a list w of DR moves with `g.apply w = solved`; `quarterTurns w` counts its U U' D D'.

    fewest_qt             every finish of g has at least `qtFull g` quarter turns, and one has exactly that many:
                          `qtFull g` is the page's "fewest number of quarter turns that any finish can have".
    fewest_qt_value       its value: 3 on 4a1 0e and 4a1 2e, 2 on 0c0 outside HTR, else the corners' count.
    half_turn_keeps       a half turn does not change it;   quarter_turn_by_one   a quarter turn changes it by one.
    no_extra_qt_lowers    on a finish with exactly `qtFull g` quarter turns ("no extra quarter turn"), every
                          quarter turn lowers it by one.
    first_qt_floor        if `qtFull g` is the corners' count, such a finish makes at least `setup g` half turns
                          before its first quarter turn (the half turns the corners need on that side).
    not_ready_no_qt_first rule 1, the exact half: if moreover g is not ready, no such finish starts with a quarter
                          turn.

  They are the theorems of `HTRRoutes.QtFull` carried over by `HTFirst.Bridge`; the table checks are run here by
  `native_decide`.  "On the inverse side" is the same statement for the inverse state (a finish read from its last
  move is a finish of the inverse state: DRBound's `inverse_eq_apply_solved`).
-/
import HTFirst.Bridge
import HTRRoutes.QtFullTheorems

namespace HTFirst
open DRBound HTRRoutes

set_option maxHeartbeats 0

/-- The checks of `HTFirst.Bridge`, over all corner and U/D-edge arrangements and the HTR coset's states. -/
theorem bridge_checked : Checked :=
  ⟨by native_decide, by native_decide, by native_decide, by native_decide, by native_decide, by native_decide⟩

/-- `chkHtr` runs over 663,552 states: 96 corner arrangements, 576 U/D-edge arrangements and 12 of the 24 E-slice
arrangements. -/
theorem htr_count : HTRC.length = 96 ∧ HTRE.length = 576 ∧ htrCount = 663552 := by native_decide

/-! `qtFull` … `subset48` are abbreviations, so that Lean (and its kernel) open them before anything else. -/

/-- The fewest quarter turns of a finish of g (`fewest_qt`). -/
abbrev qtFull (g : State) : Nat := qtfull.qf (cosetOf g)
/-- The corners' count: the quarter-turn number in the name of g's corner subset. -/
abbrev cornerQt (g : State) : Nat := qtfull.cq (cosetOf g)
/-- Some U or D quarter turn, done right away, takes the corners to a subset with one quarter turn less. -/
abbrev ready (g : State) : Bool := qtfull.ready (cosetOf g)
/-- The fewest half turns before some quarter turn lowers the corners' count (255 on 0c0). -/
abbrev setup (g : State) : Nat := qtfull.sC (cosetOf g)
/-- The subset × edges of g, in the 48 names ("4c3 2e"). -/
abbrev subset48 (g : State) : String := qtfull.lab48 (cosetOf g)

private theorem cV (g : State) (hv : g.Valid) : qtfull.V (cosetOf g) = true :=
  cosetOf_V exact_model_checked bridge_checked g hv

private theorem isQt_of (m : Move) (hm : m.isHalf = false) : qtfull.isQt (mv m).val = true := by
  show qtfull.isQt m.idx = true
  rw [isQt_idx, hm]; rfl

private theorem notQt_of (m : Move) (hm : m.isHalf = true) : qtfull.isQt (mv m).val = false := by
  show qtfull.isQt m.idx = false
  rw [isQt_idx, hm]; rfl

/-- Every finish has at least `qtFull g` quarter turns. -/
theorem qt_lower (g : State) (hv : g.Valid) (w : List Move) (hw : g.apply w = solved) :
    qtFull g ≤ quarterTurns w := by
  have h := cosetOf_apply exact_model_checked bridge_checked w g hv
  rw [hw, cosetOf_solved exact_model_checked bridge_checked] at h
  have h2 := qtfull.qf_lower qt_full_checked (cV g hv) (w.map mv) h.symm
  rw [qts_map] at h2
  exact h2

/-- Some finish has exactly `qtFull g` quarter turns. -/
theorem qt_attained (g : State) (hv : g.Valid) (hp : g.ParityOK) :
    ∃ w : List Move, g.apply w = solved ∧ quarterTurns w = qtFull g := by
  obtain ⟨u, hu, hq⟩ := qtfull.qf_attained qt_full_checked (cV g hv)
  have hmap : (u.map fun m => Move.ofIdx m.val).map mv = u := by
    rw [List.map_map]
    have hid : (mv ∘ fun m : qtfull.Mv => Move.ofIdx m.val) = id := by
      funext m
      exact Fin.ext (ofIdx_mv m.val m.isLt)
    rw [hid, List.map_id]
  have hc : cosetOf (g.apply (u.map fun m => Move.ofIdx m.val)) = cosets.GOAL := by
    rw [cosetOf_apply exact_model_checked bridge_checked _ g hv, hmap]
    exact hu
  have hgood := exact_model_checked.good_apply (u.map fun m => Move.ofIdx m.val) g hv hp
  obtain ⟨w2, hh, hs⟩ := htr_solvable exact_model_checked bridge_checked _ hgood.1 hgood.2 hc
  refine ⟨(u.map fun m => Move.ofIdx m.val) ++ w2, ?_, ?_⟩
  · rw [apply_append]; exact hs
  · rw [quarterTurns_append, quarterTurns_half w2 hh, Nat.add_zero, ← qts_map, hmap, hq]

/-- **The fewest quarter turns of a finish.**  For every DR state g (legal, parities consistent): every finish of g
has at least `qtFull g` quarter turns, and some finish has exactly `qtFull g`. -/
theorem fewest_qt (g : State) (hv : g.Valid) (hp : g.ParityOK) :
    (∃ w : List Move, g.apply w = solved ∧ quarterTurns w = qtFull g) ∧
    (∀ w : List Move, g.apply w = solved → qtFull g ≤ quarterTurns w) :=
  ⟨qt_attained g hv hp, qt_lower g hv⟩

/-- **A half turn never changes the fewest number of quarter turns.** -/
theorem half_turn_keeps (g : State) (hv : g.Valid) (m : Move) (hm : m.isHalf = true) :
    qtFull (g.move m) = qtFull g := by
  unfold qtFull
  rw [cosetOf_move exact_model_checked bridge_checked g hv m]
  exact qtfull.qf_half qt_full_checked (cV g hv) (mv m) (notQt_of m hm)

/-- **A quarter turn changes it by exactly one.** -/
theorem quarter_turn_by_one (g : State) (hv : g.Valid) (m : Move) (hm : m.isHalf = false) :
    qtFull (g.move m) + 1 = qtFull g ∨ qtFull (g.move m) = qtFull g + 1 := by
  unfold qtFull
  rw [cosetOf_move exact_model_checked bridge_checked g hv m]
  exact qtfull.qf_quarter qt_full_checked (cV g hv) (mv m) (isQt_of m hm)

/-- **On a finish with no extra quarter turn, every quarter turn lowers the number by one.** -/
theorem no_extra_qt_lowers (g : State) (hv : g.Valid) (a : List Move) (m : Move) (b : List Move)
    (hw : g.apply (a ++ m :: b) = solved) (ht : quarterTurns (a ++ m :: b) = qtFull g)
    (hm : m.isHalf = false) : qtFull ((g.apply a).move m) + 1 = qtFull (g.apply a) := by
  have hrun := cosetOf_apply exact_model_checked bridge_checked (a ++ m :: b) g hv
  rw [hw, cosetOf_solved exact_model_checked bridge_checked, List.map_append, List.map_cons] at hrun
  have hq : qtfull.qts (a.map mv ++ mv m :: b.map mv) = qtfull.qf (cosetOf g) := by
    rw [← List.map_cons, ← List.map_append, qts_map]; exact ht
  have h := qtfull.tight_lowers qt_full_checked (cV g hv) (a.map mv) (mv m) (b.map mv) hrun.symm hq
    (isQt_of m hm)
  unfold qtFull
  rw [cosetOf_move exact_model_checked bridge_checked _ (apply_valid exact_model_checked bridge_checked a g hv) m,
    cosetOf_apply exact_model_checked bridge_checked a g hv]
  exact h

/-- **The floor.**  If the fewest number of quarter turns of g is the corners' count, a finish with no extra
quarter turn makes at least `setup g` half turns before its first quarter turn. -/
theorem first_qt_floor (g : State) (hv : g.Valid) (hrow : qtFull g = cornerQt g) (p : List Move) (m : Move)
    (t : List Move) (hp : ∀ h ∈ p, h.isHalf = true) (hm : m.isHalf = false)
    (hw : g.apply (p ++ m :: t) = solved) (ht : quarterTurns (p ++ m :: t) = qtFull g) :
    setup g ≤ p.length := by
  have hrun := cosetOf_apply exact_model_checked bridge_checked (p ++ m :: t) g hv
  rw [hw, cosetOf_solved exact_model_checked bridge_checked, List.map_append, List.map_cons] at hrun
  have hq : qtfull.qts (p.map mv ++ mv m :: t.map mv) = qtfull.qf (cosetOf g) := by
    rw [← List.map_cons, ← List.map_append, qts_map]; exact ht
  have hp' : ∀ h ∈ p.map mv, qtfull.isQt h.val = false := by
    intro h hh
    obtain ⟨h', hmem, rfl⟩ := List.mem_map.mp hh
    exact notQt_of h' (hp h' hmem)
  have h := qtfull.floor qt_full_checked (cV g hv) hrow (p.map mv) (mv m) (t.map mv) hp' (isQt_of m hm)
    hrun.symm hq
  rw [List.length_map] at h
  exact h

/-- **Rule 1, the exact half.**  If the fewest number of quarter turns of g is the corners' count and g is not
ready, no finish with no extra quarter turn starts with a quarter turn. -/
theorem not_ready_no_qt_first (g : State) (hv : g.Valid) (hrow : qtFull g = cornerQt g) (hr : ready g = false)
    (m : Move) (t : List Move) (hm : m.isHalf = false) (hw : g.apply (m :: t) = solved) :
    quarterTurns (m :: t) ≠ qtFull g := by
  intro ht
  have hrun := cosetOf_apply exact_model_checked bridge_checked (m :: t) g hv
  rw [hw, cosetOf_solved exact_model_checked bridge_checked, List.map_cons] at hrun
  have hq : qtfull.qts (mv m :: t.map mv) = qtfull.qf (cosetOf g) := by
    rw [← List.map_cons, qts_map]; exact ht
  have h := qtfull.rule_one qt_full_checked (cV g hv) hrow (mv m) (t.map mv) (isQt_of m hm) hrun.symm hq
  unfold ready at hr
  rw [h] at hr
  exact Bool.noConfusion hr

/-- **The value.**  The fewest number of quarter turns of a finish is 3 on 4a1 0e and 4a1 2e, 2 on 0c0 outside
HTR (0 inside), and the corners' count everywhere else. -/
theorem fewest_qt_value (g : State) (hv : g.Valid) :
    qtFull g = (if subset48 g == "4a1 0e" || subset48 g == "4a1 2e" then 3
      else if cornerQt g == 0 then (if cosetOf g == cosets.GOAL then 0 else 2) else cornerQt g) :=
  beq_iff_eq.mp (qtfull.allV_spec qf_values (cV g hv))

end HTFirst
