/-
  DRBound.CertifiedFull — the finest rung (406,425,600 classes): corners exactly, slice type and U/D colour of
  every U/D-layer edge, and the two double-swap parities.  The table check reads every entry against all ten moves.
-/
import DRBound.Theorems

namespace DRBound

set_option maxHeartbeats 0

theorem rungFull_checked : rungFull.Checked :=
  ⟨by native_decide, by native_decide, by native_decide⟩

/-- **Main bound, normal side.** -/
theorem full_bound (g : State) (hg : g.Valid) (w : List Move) (hw : g.apply w = solved) :
    rungFull.bound g ≤ w.length := rungFull.lower_bound rungFull_checked g hg w hw

/-- **Main bound, inverse side.** -/
theorem full_bound_inverse (g h : State) (hg : g.Valid) (hh : h.IsInverseOf g) (w : List Move)
    (hw : g.apply w = solved) : rungFull.bound h ≤ w.length :=
  rungFull.lower_bound_inverse rungFull_checked g h hg hh w hw

/-- **Sharpness.**  `rungFull.bound g` moves suffice to make `g` look solved through these features, so the
bound is the best that the features allow. -/
theorem full_bound_attained (g : State) (hg : g.Valid) (hb : rungFull.bound g < 255) :
    ∃ w : List Move, w.length = rungFull.bound g ∧ rungFull.index (g.apply w) = rungFull.index solved :=
  rungFull.bound_attained rungFull_checked _ g hg rfl hb

end DRBound
