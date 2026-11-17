/-
The edges of the cube, the face turns, and EO on each axis, from stickers.

Only edges matter for EO, so the model has the 24 edge stickers and nothing else.
-/
namespace ImpliedEO

inductive Face | U | D | R | L | F | B
  deriving DecidableEq, Repr

inductive Axis | ud | rl | fb
  deriving DecidableEq, Repr

def Face.axis : Face → Axis
  | .U | .D => .ud
  | .R | .L => .rl
  | .F | .B => .fb

def Face.all : List Face := [.U, .D, .R, .L, .F, .B]
def Axis.all : List Axis := [.ud, .rl, .fb]

theorem Face.mem_all (f : Face) : f ∈ Face.all := by cases f <;> simp [Face.all]
theorem Axis.mem_all (a : Axis) : a ∈ Axis.all := by cases a <;> simp [Axis.all]

instance (P : Face → Prop) [DecidablePred P] : Decidable (∀ f, P f) :=
  decidable_of_iff (∀ f ∈ Face.all, P f) ⟨fun h f => h f (Face.mem_all f), fun h f _ => h f⟩
instance (P : Axis → Prop) [DecidablePred P] : Decidable (∀ a, P a) :=
  decidable_of_iff (∀ a ∈ Axis.all, P a) ⟨fun h a => h a (Axis.mem_all a), fun h a _ => h a⟩

/-- A quarter turn of the face `m`, clockwise seen from outside, carries a sticker on face `f` of that layer
to this face.  (U: front to left.  R: front to up.  F: up to right.  D, L, B: the same seen from their side.) -/
def Face.turn : Face → Face → Face
  | .U, .F => .L | .U, .L => .B | .U, .B => .R | .U, .R => .F
  | .D, .F => .R | .D, .R => .B | .D, .B => .L | .D, .L => .F
  | .R, .F => .U | .R, .U => .B | .R, .B => .D | .R, .D => .F
  | .L, .F => .D | .L, .D => .B | .L, .B => .U | .L, .U => .F
  | .F, .U => .R | .F, .R => .D | .F, .D => .L | .F, .L => .U
  | .B, .U => .L | .B, .L => .D | .B, .D => .R | .B, .R => .U
  | _, f => f

theorem Face.turn_ok : ∀ m f g : Face, f.axis ≠ g.axis → (m.turn f).axis ≠ (m.turn g).axis := by decide

/-- An edge sticker's spot: the face it is on and the other face of the same edge.  24 of them. -/
structure Facelet where
  on : Face
  side : Face
  ok : on.axis ≠ side.axis
  deriving DecidableEq

instance (P : Facelet → Prop) [DecidablePred P] : Decidable (∀ x, P x) :=
  decidable_of_iff (∀ f g : Face, ∀ h : f.axis ≠ g.axis, P ⟨f, g, h⟩)
    ⟨fun H x => H x.on x.side x.ok, fun H f g h => H ⟨f, g, h⟩⟩

/-- The other sticker spot of the same edge. -/
def Facelet.mate (x : Facelet) : Facelet := ⟨x.side, x.on, fun h => x.ok h.symm⟩

inductive Amount | cw | half | ccw
  deriving DecidableEq, Repr

structure Move where
  face : Face
  amt : Amount
  deriving DecidableEq, Repr

instance (P : Move → Prop) [DecidablePred P] : Decidable (∀ m, P m) :=
  decidable_of_iff (∀ f : Face, P ⟨f, .cw⟩ ∧ P ⟨f, .half⟩ ∧ P ⟨f, .ccw⟩)
    ⟨fun H m => by
      obtain ⟨f, a⟩ := m
      cases a
      · exact (H f).1
      · exact (H f).2.1
      · exact (H f).2.2,
     fun H f => ⟨H _, H _, H _⟩⟩

def Move.inv (m : Move) : Move :=
  ⟨m.face, match m.amt with | .cw => .ccw | .half => .half | .ccw => .cw⟩

/-- Where a quarter turn of face `m` takes the sticker at `x`. -/
def quarter (m : Face) (x : Facelet) : Facelet :=
  if x.on = m ∨ x.side = m then ⟨m.turn x.on, m.turn x.side, Face.turn_ok m x.on x.side x.ok⟩ else x

def mv (m : Move) (x : Facelet) : Facelet :=
  match m.amt with
  | .cw => quarter m.face x
  | .half => quarter m.face (quarter m.face x)
  | .ccw => quarter m.face (quarter m.face (quarter m.face x))

/-- Where a move sequence takes the sticker at `x`. -/
def run (s : List Move) (x : Facelet) : Facelet := s.foldl (fun y m => mv m y) x

/-- The sequence undone. -/
def inv (s : List Move) : List Move := (s.map Move.inv).reverse

/-- Looking order of the faces for EO on an axis: for F/B it is U/D first, then F/B, then R/L. -/
def rank : Axis → Axis → Nat
  | .fb, .ud => 0 | .fb, .fb => 1 | .fb, .rl => 2
  | .rl, .ud => 0 | .rl, .rl => 1 | .rl, .fb => 2
  | .ud, .fb => 0 | .ud, .ud => 1 | .ud, .rl => 2

/-- The key spot of each place for EO on `a` (for F/B: the U/D one if the place has one, else the F/B one),
which is also the key sticker of each edge.  An edge is good when its key sticker is on a key spot. -/
def key (a : Axis) (x : Facelet) : Bool := rank a x.on.axis < rank a x.side.axis

/-- EO on `a` is solved after the sequence `s` (done on a solved cube): every key sticker is on a key spot. -/
def isEO (a : Axis) (s : List Move) : Prop := ∀ x, key a x = true → key a (run s x) = true

/-- The place of `x` is in the slice across axis `c` (for F/B: UR, UL, DR, DL). -/
def across (c : Axis) (x : Facelet) : Bool := x.on.axis != c && x.side.axis != c

/-- A move that keeps EO on `a`: any turn of the other four faces, or a half turn. -/
def Move.keeps (a : Axis) (m : Move) : Bool := m.face.axis != a || m.amt == .half

/-! ### Facts about single moves (finite checks) -/

theorem mate_mate (x : Facelet) : x.mate.mate = x := rfl
theorem mv_inv_left : ∀ m x, mv m.inv (mv m x) = x := by decide
theorem mv_inv_right : ∀ m x, mv m (mv m.inv x) = x := by decide
theorem mv_mate : ∀ m x, mv m x.mate = (mv m x).mate := by decide
theorem key_mate : ∀ a x, key a x.mate = !key a x := by decide
theorem across_mate : ∀ a x, across a x.mate = across a x := by decide
theorem key_keeps : ∀ a m x, m.keeps a = true → key a (mv m x) = key a x := by decide
/-- A quarter turn of a face on the axis flips exactly the four edges it moves: this is the solver's EO. -/
theorem key_quarter : ∀ a m x, m.keeps a = false →
    ((key a (mv m x) != key a x) = decide (x.on = m.face ∨ x.side = m.face)) := by decide
/-- The same notion with the other looking order (for F/B: R/L first, then F/B, then U/D). -/
def rank' : Axis → Axis → Nat
  | .fb, .rl => 0 | .fb, .fb => 1 | .fb, .ud => 2
  | .rl, .fb => 0 | .rl, .rl => 1 | .rl, .ud => 2
  | .ud, .rl => 0 | .ud, .ud => 1 | .ud, .fb => 2
theorem key_other_order : ∀ a x y, (key a x == key a y) =
    (decide (rank' a x.on.axis < rank' a x.side.axis) == decide (rank' a y.on.axis < rank' a y.side.axis)) := by
  decide

/-! ### Sequences -/

theorem run_nil (x : Facelet) : run [] x = x := rfl
theorem run_cons (m : Move) (s : List Move) (x : Facelet) : run (m :: s) x = run s (mv m x) := rfl
theorem run_append (s t : List Move) (x : Facelet) : run (s ++ t) x = run t (run s x) := by
  simp [run, List.foldl_append]
theorem inv_nil : inv [] = [] := rfl
theorem inv_cons (m : Move) (s : List Move) : inv (m :: s) = inv s ++ [m.inv] := by
  simp [inv]
theorem inv_append (s t : List Move) : inv (s ++ t) = inv t ++ inv s := by
  simp [inv]
theorem length_inv (s : List Move) : (inv s).length = s.length := by simp [inv]

theorem run_inv_left (s : List Move) (x : Facelet) : run (inv s) (run s x) = x := by
  induction s generalizing x with
  | nil => rfl
  | cons m s ih =>
    rw [inv_cons, run_append]
    show mv m.inv (run (inv s) (run s (mv m x))) = x
    rw [ih, mv_inv_left]
theorem run_inv_right (s : List Move) (x : Facelet) : run s (run (inv s) x) = x := by
  induction s generalizing x with
  | nil => rfl
  | cons m s ih =>
    rw [inv_cons, run_append]
    show run s (mv m (mv m.inv (run (inv s) x))) = x
    rw [mv_inv_right, ih]
theorem run_mate (s : List Move) (x : Facelet) : run s x.mate = (run s x).mate := by
  induction s generalizing x with
  | nil => rfl
  | cons m s ih => rw [run_cons, run_cons, mv_mate, ih]

def keepsAll (a : Axis) (s : List Move) : Bool := s.all (Move.keeps a)
theorem key_run_keeps (a : Axis) (s : List Move) (h : keepsAll a s = true) (x : Facelet) :
    key a (run s x) = key a x := by
  induction s generalizing x with
  | nil => rfl
  | cons m s ih =>
    simp [keepsAll] at h
    rw [run_cons, ih (by simpa [keepsAll] using h.2), key_keeps a m x h.1]

/-- EO solved, said for every sticker: each is on a key spot exactly when it is a key sticker. -/
theorem isEO_iff (a : Axis) (s : List Move) : isEO a s ↔ ∀ x, key a (run s x) = key a x := by
  constructor
  · intro h x
    cases hx : key a x with
    | true => exact h x hx
    | false =>
      have h1 : key a x.mate = true := by rw [key_mate, hx]; rfl
      have h2 := h x.mate h1
      rw [run_mate, key_mate] at h2
      cases hk : key a (run s x) with
      | true => rw [hk] at h2; exact absurd h2 (by decide)
      | false => rfl
  · intro h x hx; rw [h x]; exact hx

end ImpliedEO
