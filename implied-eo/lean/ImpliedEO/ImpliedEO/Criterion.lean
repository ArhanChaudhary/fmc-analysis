/-
When is `N (I)` an EO on a scramble, and when do two EOs hold on exactly the same scrambles.
-/
import ImpliedEO.Cube
namespace ImpliedEO

/-- An EO with NISS: the axis, the moves on normal, the moves on inverse.
`F B (F U B)` on F/B is `⟨.fb, [F, B], [F, U, B]⟩`. -/
structure EO where
  axis : Axis
  normal : List Move
  inverse : List Move

def EO.len (X : EO) : Nat := X.normal.length + X.inverse.length

/-- `X` is an EO on the scramble `scr`: with the inverse moves undone in front of the scramble (premoves)
and the normal moves after it, EO on the axis is solved. -/
def EO.holds (X : EO) (scr : List Move) : Prop := isEO X.axis (inv X.inverse ++ scr ++ X.normal)

/-- Doing `s` turns the edge whose sticker is at `x` from good to bad or from bad to good on `a`. -/
def flips (a : Axis) (s : List Move) (x : Facelet) : Bool := key a x != key a (run s x)

theorem bool_aux1 : ∀ p q r : Bool, (p != q) = ((p != r) != (q != r)) := by decide
theorem bool_aux2 : ∀ p q r n : Bool, ((p != q) = ((p != r) != (q != n))) → n = r := by decide

/-- **The two cases.**  `N (I)` is an EO on a scramble exactly when every edge is bad or good as two sets say:
bad if and only if exactly one of "its home place is flipped by `I`" and "its place now is flipped by `N`" holds.
(`y` is a sticker's home spot, `run scr y` where the scramble puts it.) -/
theorem EO.holds_iff (X : EO) (scr : List Move) :
    X.holds scr ↔ ∀ y, (key X.axis y != key X.axis (run scr y)) =
      (flips X.axis X.inverse y != flips X.axis X.normal (run scr y)) := by
  unfold EO.holds
  rw [isEO_iff]
  constructor
  · intro h y
    have h1 := h (run X.inverse y)
    rw [run_append, run_append, run_inv_left] at h1
    unfold flips
    rw [h1]
    exact bool_aux1 _ _ _
  · intro h x
    have h1 := h (run (inv X.inverse) x)
    unfold flips at h1
    rw [run_inv_right] at h1
    rw [run_append, run_append]
    exact bool_aux2 _ _ _ _ h1

/-! ### The same thing without an axis -/

/-- torchlight's orientation: the one every quarter turn of any face flips. -/
def qkey (x : Facelet) : Bool := key .fb x != across .fb x

/-- Which axes see torchlight's orientation with good and bad swapped (a global swap changes nothing about EO). -/
def sgn : Axis → Bool
  | .fb => false
  | _ => true
theorem key_q : ∀ a x, key a x = ((qkey x != across a x) != sgn a) := by decide
theorem qkey_mate : ∀ x, qkey x.mate = !qkey x := by decide
theorem qkey_quarter : ∀ m x, m.amt ≠ .half →
    ((qkey (mv m x) != qkey x) = decide (x.on = m.face ∨ x.side = m.face)) := by decide
theorem qkey_half : ∀ m x, m.amt = .half → qkey (mv m x) = qkey x := by decide
/-- Changing the axis changes whether an edge is bad exactly when one of its home place and its place now,
not both, is in the slice across the third axis.  (`y`: the sticker's home spot, `z`: where it is.) -/
theorem change_axis : ∀ a b c, a ≠ b → a ≠ c → b ≠ c → ∀ y z,
    ((key a y != key a z) != (key b y != key b z)) = (across c y != across c z) := by decide

/-- The case a sequence solves, with the slice across the axis toggled so that it no longer depends on the axis. -/
def kcase (a : Axis) (s : List Move) (x : Facelet) : Bool := flips a s x != across a x
def EO.norCase (X : EO) : Facelet → Bool := kcase X.axis X.normal
def EO.invCase (X : EO) : Facelet → Bool := kcase X.axis X.inverse

theorem bool_aux3 : ∀ p q c d f g s : Bool,
    ((((p != c) != s) != ((q != d) != s)) = (f != g)) ↔ ((p != q) = ((f != c) != (g != d))) := by decide

/-- The two cases again, with torchlight's orientation: nothing in it depends on the axis any more. -/
theorem EO.holds_iff_q (X : EO) (scr : List Move) :
    X.holds scr ↔ ∀ y, (qkey y != qkey (run scr y)) = (X.invCase y != X.norCase (run scr y)) := by
  rw [EO.holds_iff]
  apply forall_congr'
  intro y
  rw [key_q X.axis y, key_q X.axis (run scr y)]
  exact bool_aux3 _ _ _ _ _ _ _

theorem flips_mate (a : Axis) (s : List Move) (x : Facelet) : flips a s x.mate = flips a s x := by
  unfold flips
  rw [run_mate, key_mate, key_mate]
  cases key a x <;> cases key a (run s x) <;> rfl
theorem kcase_mate (a : Axis) (s : List Move) (x : Facelet) : kcase a s x.mate = kcase a s x := by
  unfold kcase; rw [flips_mate, across_mate]

/-- Two EOs with the same pair of cases, or with both cases complemented. -/
def EO.same (X Y : EO) : Prop := ∀ y z, (X.invCase y != Y.invCase y) = (X.norCase z != Y.norCase z)
instance (X Y : EO) : Decidable (X.same Y) := by unfold EO.same; infer_instance

theorem bool_aux4 : ∀ k a b c d : Bool, (a != b) = (c != d) → ((k = (a != c)) ↔ (k = (b != d))) := by decide
theorem bool_aux5 : ∀ k a b c d : Bool, k = (a != c) → k = (b != d) → (a != b) = (c != d) := by decide

theorem EO.holds_of_same {X Y : EO} (h : X.same Y) (scr : List Move) : X.holds scr ↔ Y.holds scr := by
  rw [EO.holds_iff_q, EO.holds_iff_q]
  apply forall_congr'
  intro y
  exact bool_aux4 _ _ _ _ _ (h y (run scr y))

/-! ### The converse: a scramble that tells two different EOs apart -/

def Move.all : List Move := Face.all.flatMap (fun f => [⟨f, .cw⟩, ⟨f, .half⟩, ⟨f, .ccw⟩])
def base : Facelet := ⟨.U, .R, by decide⟩
/-- Sequences of at most two moves that keep EO on `a`. -/
def cands (a : Axis) : List (List Move) :=
  [] :: (Move.all.filter (Move.keeps a)).flatMap
    (fun m => [m] :: (Move.all.filter (Move.keeps a)).map (fun n => [m, n]))
/-- EO-keeping moves that bring the edge of `x` to UR. -/
def toBase (a : Axis) (x : Facelet) : List Move :=
  ((cands a).find? (fun s => run s x == base || run s x == base.mate)).getD []
theorem toBase_ok : ∀ a x, keepsAll a (toBase a x) = true ∧
    (run (toBase a x) x = base ∨ run (toBase a x) x = base.mate) := by decide

theorem key_run_inv_keeps (a : Axis) (s : List Move) (h : keepsAll a s = true) (x : Facelet) :
    key a (run (inv s) x) = key a x := by
  have := key_run_keeps a s h (run (inv s) x)
  rw [run_inv_right] at this
  exact this.symm

/-- EO-keeping moves `T` such that `I T N⁻¹` takes the sticker at `y0` to the edge of `z0`. -/
theorem route (a : Axis) (I N : List Move) (y0 z0 : Facelet) : ∃ T : List Move,
    (∀ x, key a (run T x) = key a x) ∧
    (run (I ++ T ++ inv N) y0 = z0 ∨ run (I ++ T ++ inv N) y0 = z0.mate) := by
  refine ⟨toBase a (run I y0) ++ inv (toBase a (run N z0)), ?_, ?_⟩
  · intro x
    rw [run_append, key_run_inv_keeps a _ (toBase_ok _ _).1, key_run_keeps a _ (toBase_ok _ _).1]
  · simp only [run_append]
    have q2 : run (inv (toBase a (run N z0))) (run (toBase a (run N z0)) (run N z0)) = run N z0 :=
      run_inv_left _ _
    have q2m : run (inv (toBase a (run N z0))) (run (toBase a (run N z0)) (run N z0)).mate
        = (run N z0).mate := by rw [run_mate, q2]
    have n1 : run (inv N) (run N z0) = z0 := run_inv_left _ _
    have n1m : run (inv N) (run N z0).mate = z0.mate := by rw [run_mate, n1]
    rcases (toBase_ok a (run I y0)).2 with e1 | e1 <;> rcases (toBase_ok a (run N z0)).2 with e2 | e2
    · left; rw [e1, ← e2, q2, n1]
    · right
      have : base = (run (toBase a (run N z0)) (run N z0)).mate := by rw [e2]; rfl
      rw [e1, this, q2m, n1m]
    · right
      have : base.mate = (run (toBase a (run N z0)) (run N z0)).mate := by rw [e2]
      rw [e1, this, q2m, n1m]
    · left; rw [e1, ← e2, q2, n1]

/-- If two EOs differ somewhere, some scramble has the first and not the second. -/
theorem EO.same_of_implies (X Y : EO) (h : ∀ scr, X.holds scr → Y.holds scr) : X.same Y := by
  intro y0 z0
  obtain ⟨T, hT, hz⟩ := route X.axis X.inverse X.normal y0 z0
  have hX : X.holds (X.inverse ++ T ++ inv X.normal) := by
    unfold EO.holds
    rw [isEO_iff]
    intro x
    simp only [run_append]
    rw [run_inv_right, run_inv_right, hT]
  have e1 := (X.holds_iff_q _).mp hX y0
  have e2 := (Y.holds_iff_q _).mp (h _ hX) y0
  rcases hz with hz | hz
  · rw [hz] at e1 e2
    exact bool_aux5 _ _ _ _ _ e1 e2
  · rw [hz] at e1 e2
    unfold EO.norCase at e1 e2
    rw [kcase_mate] at e1 e2
    exact bool_aux5 _ _ _ _ _ e1 e2

/-- **One EO implies another exactly when they have the same pair of cases** (or both complemented),
and then each implies the other. -/
theorem EO.implies_iff_same (X Y : EO) : (∀ scr, X.holds scr → Y.holds scr) ↔ X.same Y :=
  ⟨EO.same_of_implies X Y, fun h scr hx => (EO.holds_of_same h scr).mp hx⟩

theorem EO.equiv_iff_same (X Y : EO) : (∀ scr, X.holds scr ↔ Y.holds scr) ↔ X.same Y :=
  ⟨fun h => EO.same_of_implies X Y (fun scr hx => (h scr).mp hx), fun h scr => EO.holds_of_same h scr⟩

end ImpliedEO
