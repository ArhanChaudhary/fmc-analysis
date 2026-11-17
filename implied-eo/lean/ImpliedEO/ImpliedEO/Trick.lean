/-
The F B R L trick, the examples everybody knows, and why the order of the four moves matters.
-/
import ImpliedEO.Criterion
namespace ImpliedEO

namespace Mv
def U : Move := ⟨.U, .cw⟩
def U2 : Move := ⟨.U, .half⟩
def U' : Move := ⟨.U, .ccw⟩
def D : Move := ⟨.D, .cw⟩
def D2 : Move := ⟨.D, .half⟩
def D' : Move := ⟨.D, .ccw⟩
def R : Move := ⟨.R, .cw⟩
def R2 : Move := ⟨.R, .half⟩
def R' : Move := ⟨.R, .ccw⟩
def L : Move := ⟨.L, .cw⟩
def L2 : Move := ⟨.L, .half⟩
def L' : Move := ⟨.L, .ccw⟩
def F : Move := ⟨.F, .cw⟩
def F2 : Move := ⟨.F, .half⟩
def F' : Move := ⟨.F, .ccw⟩
def B : Move := ⟨.B, .cw⟩
def B2 : Move := ⟨.B, .half⟩
def B' : Move := ⟨.B, .ccw⟩
end Mv
open Mv

instance (a : Axis) (s : List Move) : Decidable (isEO a s) := by unfold isEO; infer_instance
instance (P : Amount → Prop) [DecidablePred P] : Decidable (∀ t, P t) :=
  decidable_of_iff (P .cw ∧ P .half ∧ P .ccw)
    ⟨fun H t => by cases t; exact H.1; exact H.2.1; exact H.2.2, fun H => ⟨H _, H _, H _⟩⟩

/-- `G` carries the key spots of axis `a` onto the key spots of axis `b`, or onto all the others. -/
def Carries (a b : Axis) (G : List Move) : Prop :=
  (∀ y, key b (run G y) = key a y) ∨ (∀ y, key b (run G y) = !key a y)
instance (a b : Axis) (G : List Move) : Decidable (Carries a b G) := by unfold Carries; infer_instance

/-- With such a `G`: a state has EO on `a` exactly when `G` on both sides of it gives EO on `b`. -/
theorem conj_iff (a b : Axis) (G : List Move) (hG : Carries a b G) (W : List Move) :
    isEO a W ↔ isEO b (inv G ++ W ++ G) := by
  rw [isEO_iff, isEO_iff]
  constructor
  · intro h x
    rw [run_append, run_append]
    have hx : run G (run (inv G) x) = x := run_inv_right G x
    rcases hG with e | e
    · rw [e, h, ← e, hx]
    · rw [e, h, ← hx, e, hx]
  · intro h y
    have h1 := h (run G y)
    rw [run_append, run_append, run_inv_left] at h1
    rcases hG with e | e
    · rw [e, e] at h1; exact h1
    · rw [e, e] at h1
      cases hp : key a (run W y) <;> cases hq : key a y <;> rw [hp, hq] at h1 <;> first | rfl | exact absurd h1 (by decide)

/-- **The trick, for any EO with NISS.**  `N (I)` is an EO on `a` exactly when `N G (I G)` is an EO on `b`. -/
theorem trick (a b : Axis) (G : List Move) (hG : Carries a b G) (N I scr : List Move) :
    (EO.mk a N I).holds scr ↔ (EO.mk b (N ++ G) (I ++ G)).holds scr := by
  unfold EO.holds
  show isEO a (inv I ++ scr ++ N) ↔ isEO b (inv (I ++ G) ++ scr ++ (N ++ G))
  rw [conj_iff a b G hG, inv_append]
  simp only [List.append_assoc]

/-- F/B to R/L: add F B R L to both sides.  The axis you leave goes first. -/
theorem trick_fb_rl (N I scr : List Move) :
    (EO.mk .fb N I).holds scr ↔ (EO.mk .rl (N ++ [F, B, R, L]) (I ++ [F, B, R, L])).holds scr :=
  trick .fb .rl _ (by decide) N I scr
theorem trick_fb_ud (N I scr : List Move) :
    (EO.mk .fb N I).holds scr ↔ (EO.mk .ud (N ++ [F, B, U, D]) (I ++ [F, B, U, D])).holds scr :=
  trick .fb .ud _ (by decide) N I scr
theorem trick_rl_fb (N I scr : List Move) :
    (EO.mk .rl N I).holds scr ↔ (EO.mk .fb (N ++ [R, L, F, B]) (I ++ [R, L, F, B])).holds scr :=
  trick .rl .fb _ (by decide) N I scr
theorem trick_rl_ud (N I scr : List Move) :
    (EO.mk .rl N I).holds scr ↔ (EO.mk .ud (N ++ [R, L, U, D]) (I ++ [R, L, U, D])).holds scr :=
  trick .rl .ud _ (by decide) N I scr
theorem trick_ud_fb (N I scr : List Move) :
    (EO.mk .ud N I).holds scr ↔ (EO.mk .fb (N ++ [U, D, F, B]) (I ++ [U, D, F, B])).holds scr :=
  trick .ud .fb _ (by decide) N I scr
theorem trick_ud_rl (N I scr : List Move) :
    (EO.mk .ud N I).holds scr ↔ (EO.mk .rl (N ++ [U, D, R, L]) (I ++ [U, D, R, L])).holds scr :=
  trick .ud .rl _ (by decide) N I scr

/-- Each of the four moves can be turned either way. -/
theorem trick_either_way : ∀ f b r l : Amount, f ≠ .half → b ≠ .half → r ≠ .half → l ≠ .half →
    Carries .fb .rl [⟨.F, f⟩, ⟨.B, b⟩, ⟨.R, r⟩, ⟨.L, l⟩] := by decide

/-- **The order matters.**  The scramble F U F' has EO on R/L.  After F B R L (F B R L) it has EO on no axis;
after R L F B (R L F B) it has EO on F/B. -/
theorem order_matters :
    isEO .rl [F, U, F'] ∧
    (∀ a, ¬ isEO a (inv [F, B, R, L] ++ [F, U, F'] ++ [F, B, R, L])) ∧
    isEO .fb (inv [R, L, F, B] ++ [F, U, F'] ++ [R, L, F, B]) := by decide
/-- In the wrong order the four moves carry the key spots of the axis nowhere useful. -/
theorem wrong_order : ¬ Carries .rl .fb [F, B, R, L] ∧ ¬ Carries .rl .ud [F, B, R, L] ∧
    ¬ Carries .rl .rl [F, B, R, L] := by decide

/-! ### The examples -/

/-- F B (F B), R L (R L) and U D (U D) are EOs on the same scrambles. -/
theorem fbfb (scr : List Move) :
    ((EO.mk .fb [F, B] [F, B]).holds scr ↔ (EO.mk .rl [R, L] [R, L]).holds scr) ∧
    ((EO.mk .fb [F, B] [F, B]).holds scr ↔ (EO.mk .ud [U, D] [U, D]).holds scr) :=
  ⟨(EO.equiv_iff_same _ _).mpr (by decide) scr, (EO.equiv_iff_same _ _).mpr (by decide) scr⟩

/-- F B (F U B) and R L (R U' L). -/
theorem fb_fub (scr : List Move) :
    (EO.mk .fb [F, B] [F, U, B]).holds scr ↔ (EO.mk .rl [R, L] [R, U', L]).holds scr :=
  (EO.equiv_iff_same _ _).mpr (by decide) scr

theorem bool_aux6 : ∀ p q : Bool, ((p != q) = (true != true)) ↔ q = p := by decide

/-- torchlight: F B (F B) is an EO exactly when every edge is good in the orientation that every quarter
turn flips (an even number of quarter turns from home). -/
theorem fbfb_iff_quarter_turn_orientation (scr : List Move) :
    (EO.mk .fb [F, B] [F, B]).holds scr ↔ ∀ x, qkey (run scr x) = qkey x := by
  rw [EO.holds_iff_q]
  have hc : ∀ y, kcase .fb [F, B] y = true := by decide
  apply forall_congr'
  intro y
  show (qkey y != qkey (run scr y)) = (kcase .fb [F, B] y != kcase .fb [F, B] (run scr y)) ↔ _
  rw [hc, hc]
  exact bool_aux6 _ _

/-- fabio: in that case every edge is good on one axis or on all three, never on exactly two.
Said per sticker: the three axes' verdicts on it add up to an odd number of "good". -/
theorem good_on_one_or_three : ∀ y z, qkey z = qkey y →
    ((key .fb y == key .fb z) != ((key .rl y == key .rl z) != (key .ud y == key .ud z))) = true := by decide

/-! ### Not the trick: the superflip on both sides -/

/-- U D' F (U D' F) on F/B and R2 B2 R (R2 B2 R) on R/L are EOs on the same scrambles, and it is not the trick:
their axis-free cases are complements of each other. -/
theorem superflip_six :
    (∀ scr, (EO.mk .fb [U, D', F] [U, D', F]).holds scr ↔ (EO.mk .rl [R2, B2, R] [R2, B2, R]).holds scr) ∧
    (∀ y, (EO.mk .fb [U, D', F] [U, D', F]).norCase y = !(EO.mk .rl [R2, B2, R] [R2, B2, R]).norCase y) :=
  ⟨(EO.equiv_iff_same _ _).mpr (by decide), by decide⟩

/-- R L F (L U R F) and B U D F (B D F), both on F/B, are EOs on the same scrambles: every case complemented. -/
theorem superflip_seven :
    (∀ scr, (EO.mk .fb [R, L, F] [L, U, R, F]).holds scr ↔ (EO.mk .fb [B, U, D, F] [B, D, F]).holds scr) ∧
    (∀ y, flips .fb [R, L, F] y = !flips .fb [B, U, D, F] y) ∧
    (∀ y, flips .fb [L, U, R, F] y = !flips .fb [B, D, F] y) :=
  ⟨(EO.equiv_iff_same _ _).mpr (by decide), by decide, by decide⟩

end ImpliedEO
