/-
  AttemptSim.Perm — move sequences as permutations, with the general (kernel-checked) part of the study's certificate:
  what a solution is, the inverse of a sequence, the NISS convention, and `cancel` (the HTM form of a sequence).

  A move is a number 0 … 17: 3 · face + (quarter turns − 1), faces U D R L F B (the simulator's numbering, and the
  order of `cube.NAMES`).  `mvF m p` is the place the sticker at place p is carried to by move m (the 54-sticker
  permutations of `Cube.lean`, built from geometry).  `run L p` follows the sticker at place p through the sequence L.
  A sequence *does nothing* (`solved L`) when every sticker ends where it started; a solution of a scramble S is a
  sequence X with `solved (S ++ X)`.

  Proved for every sequence, with no bound on length (the kernel checks the induction; the facts about single moves
  and pairs of moves are finite checks run by `native_decide`):

    run_invert, run_invert'   a sequence followed by its inverse, or the inverse followed by the sequence, does nothing
    solved_rotate             if A ++ B does nothing then B ++ A does nothing
    niss_convention           I⁻¹ S N does nothing  ⇔  S N I⁻¹ does nothing: a normal part N and an inverse part I
                              that bring the scramble S to solved in the simulator's sense (`state_ni` of ctx.rs:
                              the inverse of I, then S, then N) are the solution N ++ invert I, and conversely
    cancel_run                `cancel L` moves every sticker exactly as L does
    cancel_solves             so `cancel (N ++ invert I)` solves S exactly when N ++ invert I does
-/
import AttemptSim.Cube

namespace AttemptSim
namespace perm
open cube

abbrev P := Fin 54
abbrev Mv := Fin 18

/-- The 18 face turns of `Cube.lean`, in the order U U2 U' D D2 D' R R2 R' L L2 L' F F2 F' B B2 B'. -/
def TAB : Array State := (NAMES.map MOVES).toArray

/-- Where move m carries the sticker at place p. -/
def mvF (m : Mv) (p : P) : P := ⟨(TAB[m.val]!)[p.val]! % 54, Nat.mod_lt _ (by decide)⟩

/-- Follow the sticker at place p through a move sequence. -/
def run : List Mv → P → P
  | [], p => p
  | m :: L, p => run L (mvF m p)

/-- The sequence brings every sticker back to where it started. -/
def solved (L : List Mv) : Prop := ∀ p, run L p = p

theorem run_append (A B : List Mv) (p : P) : run (A ++ B) p = run B (run A p) := by
  induction A generalizing p with
  | nil => rfl
  | cons m A ih => simp [run, ih]

/-- The inverse of a move: the same face turned back (`inv_move` of ctx.rs). -/
def invM (m : Mv) : Mv := ⟨3 * (m.val / 3) + 2 - m.val % 3, by omega⟩
/-- The inverse of a sequence: the inverse moves in reverse order (`invert` of ctx.rs). -/
def invert (L : List Mv) : List Mv := (L.map invM).reverse

/-! ### Finite checks, run as compiled code -/

def allFin {n : Nat} (f : Fin n → Bool) : Bool := (List.finRange n).all f
theorem allFin_spec {n : Nat} {f : Fin n → Bool} (h : allFin f = true) (i : Fin n) : f i = true :=
  List.all_eq_true.mp h i (List.mem_finRange i)

/-- The 18 tables have 54 entries below 54 (so the `% 54` in `mvF` changes nothing), and each is a permutation. -/
def tabOkB : Bool :=
  TAB.size == 18 && TAB.all fun m => m.size == 54 && m.all (· < 54) && is_permutation m
theorem tabOk : tabOkB = true := by native_decide

/-- A move and its inverse undo each other, on every sticker. -/
def invOkB : Bool :=
  allFin fun m : Mv => allFin fun p : P => mvF (invM m) (mvF m p) == p && mvF m (mvF (invM m) p) == p
theorem invOk : invOkB = true := by native_decide

theorem mv_inv (m : Mv) (p : P) : mvF (invM m) (mvF m p) = p := by
  have h := allFin_spec (allFin_spec invOk m) p
  simp at h
  exact h.1
theorem mv_inv' (m : Mv) (p : P) : mvF m (mvF (invM m) p) = p := by
  have h := allFin_spec (allFin_spec invOk m) p
  simp at h
  exact h.2

theorem invert_cons (m : Mv) (L : List Mv) : invert (m :: L) = invert L ++ [invM m] := by
  simp [invert]

theorem run_invert (L : List Mv) (p : P) : run (invert L) (run L p) = p := by
  induction L generalizing p with
  | nil => simp [invert, run]
  | cons m L ih => rw [invert_cons, run_append]; simp [run, ih, mv_inv]

theorem run_invert' (L : List Mv) (p : P) : run L (run (invert L) p) = p := by
  induction L generalizing p with
  | nil => simp [invert, run]
  | cons m L ih => rw [invert_cons, run_append]; simp [run, ih, mv_inv']

/-- If A then B does nothing, so does B then A. -/
theorem solved_rotate (A B : List Mv) (h : solved (A ++ B)) : solved (B ++ A) := by
  intro p
  rw [run_append]
  have key : run B p = run (invert A) p := by
    have h1 := h (run (invert A) p)
    rw [run_append, run_invert'] at h1
    exact h1
  rw [key, run_invert']

/-- **The NISS convention.**  The simulator calls a scramble S solved by a normal part N and an inverse part I when
the state `I⁻¹ S N` (the inverse of I, then S, then N: `state_ni`) is the solved cube.  That is so exactly when the
sequence `N ++ invert I` solves S. -/
theorem niss_convention (S N I : List Mv) :
    solved (invert I ++ (S ++ N)) ↔ solved (S ++ (N ++ invert I)) := by
  constructor
  · intro h
    have := solved_rotate _ _ h
    simpa [List.append_assoc] using this
  · intro h
    have h' : solved ((S ++ N) ++ invert I) := by simpa [List.append_assoc] using h
    exact solved_rotate _ _ h'

/-! ### The executable check -/

def solvedB (L : List Mv) : Bool := allFin fun p : P => run L p == p

theorem solvedB_iff (L : List Mv) : solvedB L = true ↔ solved L := by
  constructor
  · intro h p
    have := allFin_spec h p
    simpa using this
  · intro h
    unfold solvedB allFin
    rw [List.all_eq_true]
    intro p _
    simp [h p]

/-! ### cancel: the HTM form -/

def face (m : Mv) : Nat := m.val / 3
/-- Quarter turns of a move: 1, 2 or 3. -/
def amt (m : Mv) : Nat := m.val % 3 + 1
/-- The move of face f with t quarter turns (t = 1, 2, 3). -/
def mk (f t : Nat) : Mv := ⟨(3 * f + t - 1) % 18, Nat.mod_lt _ (by decide)⟩

/-- Try to merge the move m into `out`, a sequence written backwards (latest move first): walk back over the
trailing moves on m's axis; a move of m's own face is merged with m (and dropped if they cancel).  `none` if no move
of m's face is found before a move of another axis.  (The loop of `cancel` in ctx.rs.) -/
def pushBack : List Mv → Mv → Option (List Mv)
  | [], _ => none
  | q :: rest, m =>
    if face q = face m then
      (if (amt q + amt m) % 4 = 0 then some rest else some (mk (face m) ((amt q + amt m) % 4) :: rest))
    else if face q / 2 = face m / 2 then (pushBack rest m).map (fun r => q :: r)
    else none

def push (out : List Mv) (m : Mv) : List Mv := (pushBack out m).getD (m :: out)

/-- Merge turns of one face (also across a turn of the opposite face) until nothing merges: `cancel` of ctx.rs. -/
def cancel (L : List Mv) : List Mv := (L.foldl push []).reverse

/-- Two moves of one face are the merged move (or nothing); two moves of opposite faces commute. -/
def mergeOkB : Bool :=
  allFin fun q : Mv => allFin fun m : Mv => allFin fun p : P =>
    if face q = face m then
      (if (amt q + amt m) % 4 = 0 then mvF m (mvF q p) == p
       else mvF (mk (face m) ((amt q + amt m) % 4)) p == mvF m (mvF q p))
    else if face q / 2 = face m / 2 then mvF q (mvF m p) == mvF m (mvF q p)
    else true
theorem mergeOk : mergeOkB = true := by native_decide

theorem pushBack_run : ∀ (out : List Mv) (m : Mv) (out' : List Mv), pushBack out m = some out' →
    ∀ p, run out'.reverse p = run (out.reverse ++ [m]) p
  | [], m, out', h => by simp [pushBack] at h
  | q :: rest, m, out', h => by
    intro p
    have fact := allFin_spec (allFin_spec (allFin_spec mergeOk q) m) (run rest.reverse p)
    unfold pushBack at h
    by_cases hf : face q = face m
    · by_cases ht : (amt q + amt m) % 4 = 0
      · simp [hf, ht] at h
        subst h
        simp [hf, ht] at fact
        simp [run_append, run, fact]
      · simp [hf, ht] at h
        subst h
        simp [hf, ht] at fact
        simp [run_append, run, fact]
    · by_cases ha : face q / 2 = face m / 2
      · simp [hf, ha] at h
        obtain ⟨r, hr, rfl⟩ := h
        have ih := pushBack_run rest m r hr p
        simp [hf, ha] at fact
        simp [run_append, run] at ih ⊢
        rw [ih, fact]
      · simp [hf, ha] at h

theorem push_run (out : List Mv) (m : Mv) (p : P) : run (push out m).reverse p = run (out.reverse ++ [m]) p := by
  unfold push
  cases h : pushBack out m with
  | none => simp
  | some out' => simpa using pushBack_run out m out' h p

theorem foldl_push_run (L acc : List Mv) (p : P) :
    run (L.foldl push acc).reverse p = run (acc.reverse ++ L) p := by
  induction L generalizing acc with
  | nil => simp
  | cons m L ih =>
    simp only [List.foldl_cons]
    rw [ih, run_append, push_run, ← run_append]
    simp [List.append_assoc]

/-- **`cancel` never changes what a sequence does.** -/
theorem cancel_run (L : List Mv) (p : P) : run (cancel L) p = run L p := by
  unfold cancel
  simpa using foldl_push_run L [] p

/-- So the cancelled sequence solves a scramble exactly when the sequence does. -/
theorem cancel_solves (S X : List Mv) : solved (S ++ cancel X) ↔ solved (S ++ X) := by
  constructor <;> intro h p
  · have := h p
    rw [run_append, cancel_run, ← run_append] at this
    exact this
  · rw [run_append, cancel_run, ← run_append]
    exact h p

/-- The written solution of the simulator, `cancel (N ++ invert I)`, solves S exactly when `I⁻¹ S N` is solved. -/
theorem written_solution (S N I : List Mv) :
    solved (S ++ cancel (N ++ invert I)) ↔ solved (invert I ++ (S ++ N)) := by
  rw [cancel_solves, niss_convention]

/-! ### What the HTM form looks like (checked on every sequence of up to 5 moves) -/

/-- No two neighbours on one face, and no two moves of one face with only a move of the opposite face between. -/
def reducedB : List Mv → Bool
  | a :: b :: rest =>
    face a != face b &&
    (match rest with
     | c :: _ => !(face a == face c && face a / 2 == face b / 2)
     | [] => true) &&
    reducedB (b :: rest)
  | _ => true

/-- `f` holds on every sequence of exactly n moves that extends `pre` (written backwards). -/
def allSeq (f : List Mv → Bool) : Nat → List Mv → Bool
  | 0, pre => f pre.reverse
  | n + 1, pre => allFin fun m : Mv => allSeq f n (m :: pre)

def cancelShapeB (n : Nat) : Bool :=
  (List.range (n + 1)).all fun k =>
    allSeq (fun L =>
      let c := cancel L
      reducedB c && cancel c == c && c.length ≤ L.length && (!reducedB L || c == L)) k []

end perm
end AttemptSim
