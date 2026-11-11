/-
  DRBound.Certified — the machine checks for each rung, and the resulting theorems.

  `native_decide` runs the compiled checker and accepts the result (this trusts the Lean compiler; see the
  write-up for what exactly is and is not trusted).
-/
import DRBound.Theorems
import DRBound.FakeMMAPData

namespace DRBound

-- The checks run compiled code for a long time; Lean's default elaboration time-out does not apply to them.
set_option maxHeartbeats 0

/-! ### Rung "corners": the optimal corner-solution length L -/

theorem rungC_checked : rungC.Checked :=
  ⟨by native_decide, by native_decide, by native_decide⟩

/-- Every DR-move solution is at least as long as the optimal solution of the corners alone. -/
theorem corner_length_bound (g : State) (hg : g.Valid) (w : List Move) (hw : g.apply w = solved) :
    rungC.bound g ≤ w.length := rungC.lower_bound rungC_checked g hg w hw

/-! ### Rung "corners + E-slice parity" -/

theorem rungCP_checked : rungCP.Checked :=
  ⟨by native_decide, by native_decide, by native_decide⟩

/-- …and at least as long as the shortest corner solution whose number of side half turns has the parity
of the E-slice permutation. -/
theorem corner_parity_bound (g : State) (hg : g.Valid) (w : List Move) (hw : g.apply w = solved) :
    rungCP.bound g ≤ w.length := rungCP.lower_bound rungCP_checked g hg w hw

/-! ### Rung "HTR coset": the optimal DR→HTR length -/

theorem rungHTR_checked : rungHTR.Checked :=
  ⟨by native_decide, by native_decide, by native_decide⟩

theorem htr_length_bound (g : State) (hg : g.Valid) (w : List Move) (hw : g.apply w = solved) :
    rungHTR.bound g ≤ w.length := rungHTR.lower_bound rungHTR_checked g hg w hw

/-! ### Rung "KF": the NISS@1qt features of Advanced DR Bounding, on every DR state -/

theorem rungKF_checked : rungKF.Checked :=
  ⟨by native_decide, by native_decide, by native_decide⟩

theorem kf_bound (g : State) (hg : g.Valid) (w : List Move) (hw : g.apply w = solved) :
    rungKF.bound g ≤ w.length := rungKF.lower_bound rungKF_checked g hg w hw

theorem kf_bound_inverse (g h : State) (hg : g.Valid) (hh : h.IsInverseOf g) (w : List Move)
    (hw : g.apply w = solved) : rungKF.bound h ≤ w.length :=
  rungKF.lower_bound_inverse rungKF_checked g h hg hh w hw

/-- The KF bound is attained: `rungKF.bound g` moves suffice to make `g` look solved through these features. -/
theorem kf_bound_attained (g : State) (hg : g.Valid) (hb : rungKF.bound g < 255) :
    ∃ w : List Move, w.length = rungKF.bound g ∧ rungKF.index (g.apply w) = rungKF.index solved :=
  rungKF.bound_attained rungKF_checked _ g hg rfl hb

/-! ### Rung "corners + bad edges + E parity" and rung "K0 + double-swap parity" -/

theorem rungCBadP_checked : rungCBadP.Checked :=
  ⟨by native_decide, by native_decide, by native_decide⟩

theorem cbadp_bound (g : State) (hg : g.Valid) (w : List Move) (hw : g.apply w = solved) :
    rungCBadP.bound g ≤ w.length := rungCBadP.lower_bound rungCBadP_checked g hg w hw

theorem cbadp_bound_inverse (g h : State) (hg : g.Valid) (hh : h.IsInverseOf g) (w : List Move)
    (hw : g.apply w = solved) : rungCBadP.bound h ≤ w.length :=
  rungCBadP.lower_bound_inverse rungCBadP_checked g h hg hh w hw

theorem rungK0F_checked : rungK0F.Checked :=
  ⟨by native_decide, by native_decide, by native_decide⟩

theorem k0f_bound (g : State) (hg : g.Valid) (w : List Move) (hw : g.apply w = solved) :
    rungK0F.bound g ≤ w.length := rungK0F.lower_bound rungK0F_checked g hg w hw

theorem k0f_bound_inverse (g h : State) (hg : g.Valid) (hh : h.IsInverseOf g) (w : List Move)
    (hw : g.apply w = solved) : rungK0F.bound h ≤ w.length :=
  rungK0F.lower_bound_inverse rungK0F_checked g h hg hh w hw

/-! ### The 216-case table of Advanced DR Bounding (half turns only) -/

theorem rungKF_half_checked : rungKF.checkHalfTable = true := by native_decide

/-- HTR-only finishes: a solution of `g` made of half turns has at least `rungKF.halfBound g` moves. -/
theorem kf_half_bound (g : State) (hg : g.Valid) (w : List Move) (hall : ∀ m ∈ w, m.isHalf = true)
    (hw : g.apply w = solved) : rungKF.halfBound g ≤ w.length :=
  rungKF.half_lower_bound rungKF_half_checked rungKF_checked w g hg hall hw

/-- FakeMMAP's 216 example scrambles fall into 216 different classes of the KF rung … -/
theorem fakemmap_classes : rungKF.countClasses fakemmapCases = 216 := by native_decide

/-- … and each value he lists equals our half-turn-only table value for that class.  So his table is this
quotient distance, and by `kf_half_bound` each of his numbers is a true lower bound for HTR-only finishes. -/
theorem fakemmap_values : rungKF.halfBoundsMatch fakemmapCases = true := by native_decide

/-- With quarter turns allowed (still DR moves), exactly 2 of the 216 cases get shorter. -/
theorem fakemmap_shorter_with_quarter_turns : rungKF.countShorter fakemmapCases = 2 := by native_decide

end DRBound
