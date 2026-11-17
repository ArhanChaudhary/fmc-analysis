/-
A sub-6 EO implied by a longer one: apply the short side, trace, and read the other side for the other axes.
-/
import ImpliedEO.Census
namespace ImpliedEO
open Mv

theorem EO.same_of_cases {X Y : EO} (h1 : ∀ z, X.norCase z = Y.norCase z) (h2 : ∀ y, X.invCase y = Y.invCase y) :
    X.same Y := by
  intro y z
  rw [h1 z, h2 y]
  cases Y.invCase y <;> cases Y.norCase z <;> rfl

theorem carries_four : ∀ a b, a ≠ b → Carries a b (four a b) := by decide

/-- **One side translated, the other side whatever it is.**  If `P` followed by the four moves solves the same case
on `b` as `P'`, then `P (I)` on `a` and `P' (I + the four moves)` on `b` are EOs on the same scrambles, for every `I`,
and the same with normal and inverse swapped. -/
theorem probe (a b : Axis) (hab : a ≠ b) (P P' : List Move)
    (hP : ∀ z, flips b (P ++ four a b) z = flips b P' z) (I scr : List Move) :
    ((EO.mk a P I).holds scr ↔ (EO.mk b P' (I ++ four a b)).holds scr) ∧
    ((EO.mk a I P).holds scr ↔ (EO.mk b (I ++ four a b) P').holds scr) := by
  constructor
  · rw [trick a b (four a b) (carries_four a b hab) P I scr]
    have hs : (EO.mk b (P ++ four a b) (I ++ four a b)).same (EO.mk b P' (I ++ four a b)) :=
      EO.same_of_cases (fun z => by show kcase b (P ++ four a b) z = kcase b P' z; unfold kcase; rw [hP])
        (fun _ => rfl)
    exact EO.holds_of_same hs scr
  · rw [trick a b (four a b) (carries_four a b hab) I P scr]
    have hs : (EO.mk b (I ++ four a b) (P ++ four a b)).same (EO.mk b (I ++ four a b) P') :=
      EO.same_of_cases (fun _ => rfl)
        (fun y => by show kcase b (P ++ four a b) y = kcase b P' y; unfold kcase; rw [hP])
    exact EO.holds_of_same hs scr

/-- **One trace, three axes.**  After F B on one side, whatever the other side needs (`I`):
F B (I) on F/B, R L (I F B R L) on R/L and U D (I F B U D) on U/D are EOs on the same scrambles. -/
theorem probe_fb (I scr : List Move) :
    ((EO.mk .fb [F, B] I).holds scr ↔ (EO.mk .rl [R, L] (I ++ [F, B, R, L])).holds scr) ∧
    ((EO.mk .fb [F, B] I).holds scr ↔ (EO.mk .ud [U, D] (I ++ [F, B, U, D])).holds scr) ∧
    ((EO.mk .fb I [F, B]).holds scr ↔ (EO.mk .rl (I ++ [F, B, R, L]) [R, L]).holds scr) ∧
    ((EO.mk .fb I [F, B]).holds scr ↔ (EO.mk .ud (I ++ [F, B, U, D]) [U, D]).holds scr) :=
  ⟨(probe .fb .rl (by decide) [F, B] [R, L] (by decide) I scr).1,
   (probe .fb .ud (by decide) [F, B] [U, D] (by decide) I scr).1,
   (probe .fb .rl (by decide) [F, B] [R, L] (by decide) I scr).2,
   (probe .fb .ud (by decide) [F, B] [U, D] (by decide) I scr).2⟩
/-- The same from R/L and from U/D. -/
theorem probe_rl (I scr : List Move) :
    ((EO.mk .rl [R, L] I).holds scr ↔ (EO.mk .fb [F, B] (I ++ [R, L, F, B])).holds scr) ∧
    ((EO.mk .rl [R, L] I).holds scr ↔ (EO.mk .ud [U, D] (I ++ [R, L, U, D])).holds scr) :=
  ⟨(probe .rl .fb (by decide) [R, L] [F, B] (by decide) I scr).1,
   (probe .rl .ud (by decide) [R, L] [U, D] (by decide) I scr).1⟩
theorem probe_ud (I scr : List Move) :
    ((EO.mk .ud [U, D] I).holds scr ↔ (EO.mk .fb [F, B] (I ++ [U, D, F, B])).holds scr) ∧
    ((EO.mk .ud [U, D] I).holds scr ↔ (EO.mk .rl [R, L] (I ++ [U, D, R, L])).holds scr) :=
  ⟨(probe .ud .fb (by decide) [U, D] [F, B] (by decide) I scr).1,
   (probe .ud .rl (by decide) [U, D] [R, L] (by decide) I scr).1⟩

/-- Every edge place is in exactly one slice. -/
theorem one_slice : ∀ x, (across .fb x != across .rl x) = !across .ud x ∧
    (across .fb x != across .ud x) = !across .rl x := by decide

theorem bool_aux11 : ∀ p q c1 c2 c3 : Bool, (p != c1) = (q != c2) → (c2 != c1) = !c3 → p = (q != !c3) := by decide

/-- **The flip rule.**  The R/L case of `I F B R L` is the F/B case of `I` with the eight places of the U and D
layers flipped (the E slice kept).  For U/D it is the places of the R and L layers. -/
theorem flip_rule (I : List Move) (x : Facelet) :
    flips .rl (I ++ [F, B, R, L]) x = (flips .fb I x != !across .ud x) ∧
    flips .ud (I ++ [F, B, U, D]) x = (flips .fb I x != !across .rl x) := by
  constructor
  · have h := kcase_four .fb .rl (by decide) I x
    unfold kcase at h
    exact bool_aux11 _ _ _ _ _ h (one_slice x).1
  · have h := kcase_four .fb .ud (by decide) I x
    unfold kcase at h
    exact bool_aux11 _ _ _ _ _ h (one_slice x).2

/-- The case that was pointed out: U D (D U2 F U), a 6-mover, and F B (F U2 B), a 5-mover. -/
theorem ud_du2fu (scr : List Move) :
    (EO.mk .ud [U, D] [D, U2, F, U]).holds scr ↔ (EO.mk .fb [F, B] [F, U2, B]).holds scr :=
  (EO.equiv_iff_same _ _).mpr (by decide) scr

/-- The 230 cases of at most 3 moves on R/L, by their length and the length of the same case seen from F/B:
1 of (0, 4), 2 of (1, 3), 1 of (2, 2), 24 of (2, 4), 2 of (3, 1), 10 of (3, 3), 28 of (3, 4), 162 of (3, 5). -/
theorem probe_census : probeTotal .rl = 230 ∧ probeHist .fb .rl =
    [(0, 4, 1), (1, 3, 2), (2, 2, 1), (2, 4, 24), (3, 1, 2), (3, 3, 10), (3, 4, 28), (3, 5, 162)] := by
  native_decide

end ImpliedEO
