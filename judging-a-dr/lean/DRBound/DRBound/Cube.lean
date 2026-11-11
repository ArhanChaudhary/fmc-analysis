/-
  DRBound.Cube — the cube after domino reduction (DR on the U/D axis), as plain data.

  Positions
    corners          0 UFR  1 UFL  2 UBL  3 UBR  4 DFR  5 DFL  6 DBL  7 DBR
    U/D-layer edges  0 UF   1 UL   2 UB   3 UR   4 DF   5 DL   6 DB   7 DR
    E-slice edges    0 FR   1 FL   2 BL   3 BR
  Pieces are named after their home position.  A state records which piece sits at each position.
  (Orientation never changes under DR moves, so permutations are the whole story.)

  Moves are the ten DR moves U U2 U' D D2 D' R2 L2 F2 B2, each counted as one move (HTM).
-/
import DRBound.Certificate

namespace DRBound

abbrev Arr8 := Vector (Fin 8) 8
abbrev Arr4 := Vector (Fin 4) 4

/-- The ten moves that preserve domino reduction on the U/D axis. -/
inductive Move where
  | U | U2 | U' | D | D2 | D' | R2 | L2 | F2 | B2
  deriving DecidableEq, Repr, Inhabited

namespace Move

def all : List Move := [U, U2, U', D, D2, D', R2, L2, F2, B2]

theorem mem_all (m : Move) : m ∈ all := by cases m <;> decide

/-- Position of the move in `all` (used to index tables). -/
def idx : Move → Nat
  | U => 0 | U2 => 1 | U' => 2 | D => 3 | D2 => 4 | D' => 5 | R2 => 6 | L2 => 7 | F2 => 8 | B2 => 9

/-- Side half turns: the only DR moves that touch the E slice. -/
def isSide : Move → Bool
  | R2 | L2 | F2 | B2 => true
  | _ => false

/-- Half turns (the HTR moves). -/
def isHalf : Move → Bool
  | U | U' | D | D' => false
  | _ => true

/-- After move `m`, the corner at position `p` is the one that was at position `(srcC m)[p]`. -/
def srcC : Move → Arr8
  | U  => #v[3, 0, 1, 2, 4, 5, 6, 7]
  | U2 => #v[2, 3, 0, 1, 4, 5, 6, 7]
  | U' => #v[1, 2, 3, 0, 4, 5, 6, 7]
  | D  => #v[0, 1, 2, 3, 5, 6, 7, 4]
  | D2 => #v[0, 1, 2, 3, 6, 7, 4, 5]
  | D' => #v[0, 1, 2, 3, 7, 4, 5, 6]
  | R2 => #v[7, 1, 2, 4, 3, 5, 6, 0]
  | L2 => #v[0, 6, 5, 3, 4, 2, 1, 7]
  | F2 => #v[5, 4, 2, 3, 1, 0, 6, 7]
  | B2 => #v[0, 1, 7, 6, 4, 5, 3, 2]

/-- Same for the eight U/D-layer edges. -/
def srcE : Move → Arr8
  | U  => #v[3, 0, 1, 2, 4, 5, 6, 7]
  | U2 => #v[2, 3, 0, 1, 4, 5, 6, 7]
  | U' => #v[1, 2, 3, 0, 4, 5, 6, 7]
  | D  => #v[0, 1, 2, 3, 5, 6, 7, 4]
  | D2 => #v[0, 1, 2, 3, 6, 7, 4, 5]
  | D' => #v[0, 1, 2, 3, 7, 4, 5, 6]
  | R2 => #v[0, 1, 2, 7, 4, 5, 6, 3]
  | L2 => #v[0, 5, 2, 3, 4, 1, 6, 7]
  | F2 => #v[4, 1, 2, 3, 0, 5, 6, 7]
  | B2 => #v[0, 1, 6, 3, 4, 5, 2, 7]

/-- Same for the four E-slice edges. -/
def srcS : Move → Arr4
  | R2 => #v[3, 1, 2, 0]
  | L2 => #v[0, 2, 1, 3]
  | F2 => #v[1, 0, 2, 3]
  | B2 => #v[0, 1, 3, 2]
  | _  => #v[0, 1, 2, 3]

end Move

/-- Rearrange `v` so that position `p` receives what was at position `src[p]`. -/
def permute8 (src v : Arr8) : Arr8 := Vector.ofFn fun p => v.get (src.get p)
def permute4 (src v : Arr4) : Arr4 := Vector.ofFn fun p => v.get (src.get p)

@[simp] theorem permute8_get (src v : Arr8) (p : Fin 8) : (permute8 src v).get p = v.get (src.get p) := by
  simp [permute8, Vector.get]
  rfl

@[simp] theorem permute4_get (src v : Arr4) (p : Fin 4) : (permute4 src v).get p = v.get (src.get p) := by
  simp [permute4, Vector.get]
  rfl

/-- A DR state: the piece at each corner position, each U/D-layer edge position, each E-slice position. -/
structure State where
  c : Arr8
  e : Arr8
  s : Arr4
  deriving DecidableEq, Repr

def id8 : Arr8 := #v[0, 1, 2, 3, 4, 5, 6, 7]
def id4 : Arr4 := #v[0, 1, 2, 3]

/-- The solved cube. -/
def solved : State := ⟨id8, id8, id4⟩

@[simp] theorem id8_get (p : Fin 8) : id8.get p = p := by revert p; decide
@[simp] theorem id4_get (p : Fin 4) : id4.get p = p := by revert p; decide

namespace State

/-- Apply one move. -/
def move (g : State) (m : Move) : State :=
  ⟨permute8 m.srcC g.c, permute8 m.srcE g.e, permute4 m.srcS g.s⟩

/-- Apply a sequence of moves, left to right. -/
def apply (g : State) (w : List Move) : State := run move g w

@[simp] theorem apply_nil (g : State) : g.apply [] = g := rfl
@[simp] theorem apply_cons (g : State) (m : Move) (w : List Move) :
    g.apply (m :: w) = (g.move m).apply w := rfl

end State

/-- No piece appears twice (so the eight entries are a permutation of the eight pieces). -/
def IsPerm8 (v : Arr8) : Prop := ∀ i j : Fin 8, v.get i = v.get j → i = j
def IsPerm4 (v : Arr4) : Prop := ∀ i j : Fin 4, v.get i = v.get j → i = j

instance (v : Arr8) : Decidable (IsPerm8 v) := by unfold IsPerm8; infer_instance
instance (v : Arr4) : Decidable (IsPerm4 v) := by unfold IsPerm4; infer_instance

/-- A legal arrangement of the pieces (every piece exactly once in each of the three groups).
All states reachable from the solved cube are of this kind; the theorems below hold for all of them. -/
def State.Valid (g : State) : Prop := IsPerm8 g.c ∧ IsPerm8 g.e ∧ IsPerm4 g.s

instance (g : State) : Decidable g.Valid := by unfold State.Valid; infer_instance

/-- `h` is the inverse of `g`: doing `g`'s arrangement after `h`'s gives the solved cube.
If `g` is the state produced by a scramble, `h` is the state produced by the inverse scramble. -/
def State.IsInverseOf (h g : State) : Prop :=
  (∀ p : Fin 8, g.c.get (h.c.get p) = p) ∧ (∀ p : Fin 8, g.e.get (h.e.get p) = p) ∧
    (∀ p : Fin 4, g.s.get (h.s.get p) = p)

/-! ### Every 8-tuple is `#v[a0, …, a7]` : lets us prove facts about all arrangements by listing them. -/

theorem arr8_eta (v : Arr8) : v = #v[v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]] := by
  apply Vector.ext
  intro i hi
  match i, hi with
  | 0, _ => rfl | 1, _ => rfl | 2, _ => rfl | 3, _ => rfl
  | 4, _ => rfl | 5, _ => rfl | 6, _ => rfl | 7, _ => rfl
  | n + 8, h => exact absurd h (by omega)

theorem arr4_eta (v : Arr4) : v = #v[v[0], v[1], v[2], v[3]] := by
  apply Vector.ext
  intro i hi
  match i, hi with
  | 0, _ => rfl | 1, _ => rfl | 2, _ => rfl | 3, _ => rfl
  | n + 4, h => exact absurd h (by omega)

theorem forall_arr8 {P : Arr8 → Prop}
    (h : ∀ a0 a1 a2 a3 a4 a5 a6 a7 : Fin 8, P #v[a0, a1, a2, a3, a4, a5, a6, a7]) (v : Arr8) : P v := by
  rw [arr8_eta v]; exact h _ _ _ _ _ _ _ _

theorem forall_arr4 {P : Arr4 → Prop}
    (h : ∀ a0 a1 a2 a3 : Fin 4, P #v[a0, a1, a2, a3]) (v : Arr4) : P v := by
  rw [arr4_eta v]; exact h _ _ _ _

/-- Test `P` on all 8⁸ fillings of eight positions (compiled; used by the exhaustive checks). -/
def all8 (P : Arr8 → Bool) : Bool :=
  (List.finRange 8).all fun a0 => (List.finRange 8).all fun a1 => (List.finRange 8).all fun a2 =>
  (List.finRange 8).all fun a3 => (List.finRange 8).all fun a4 => (List.finRange 8).all fun a5 =>
  (List.finRange 8).all fun a6 => (List.finRange 8).all fun a7 => P #v[a0, a1, a2, a3, a4, a5, a6, a7]

def all4 (P : Arr4 → Bool) : Bool :=
  (List.finRange 4).all fun a0 => (List.finRange 4).all fun a1 => (List.finRange 4).all fun a2 =>
  (List.finRange 4).all fun a3 => P #v[a0, a1, a2, a3]

theorem all8_spec {P : Arr8 → Bool} (h : all8 P = true) (v : Arr8) : P v = true := by
  simp only [all8, List.all_eq_true] at h
  rw [arr8_eta v]
  exact h _ (List.mem_finRange _) _ (List.mem_finRange _) _ (List.mem_finRange _) _ (List.mem_finRange _)
    _ (List.mem_finRange _) _ (List.mem_finRange _) _ (List.mem_finRange _) _ (List.mem_finRange _)

theorem all4_spec {P : Arr4 → Bool} (h : all4 P = true) (v : Arr4) : P v = true := by
  simp only [all4, List.all_eq_true] at h
  rw [arr4_eta v]
  exact h _ (List.mem_finRange _) _ (List.mem_finRange _) _ (List.mem_finRange _) _ (List.mem_finRange _)

end DRBound
