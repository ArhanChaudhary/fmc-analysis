/-
  HTFirst.Bridge — from DR states to HTR cosets: the theorems of `HTRRoutes.QtFull` (the fewest quarter turns of a
  finish, ready, the floor), restated for every DR state of DRBound's model and every sequence of DR moves.

  DRBound's state (`DRBound.State`: the piece at each corner, U/D-edge and E-slice position) and HTRRoutes' cosets
  (read off its sticker model) are two models of the cube.  `cosetOf g` is the HTR coset of g: its corners and
  U/D edges, renumbered into the sticker model's places (`CH`, `EH`: DRBound's position names as cubie positions),
  then `cosets.cid` and `pieces.mMask`.  Nothing about the renumbering is assumed.  The checks below run over all
  40,320 corner arrangements and all 40,320 U/D-edge arrangements of DRBound's model and all ten moves:

    chkC, chkE   the coset of g·m is the coset step (`cosets.CCM`, `cosets.MM`) of the coset of g;
    chkV         every (corner coset, edge pattern with four M places) is one of the 29,400 cosets;
    chkSolved    the solved cube is in the HTR coset;   chkMoves   the two models' move tables are the same;
    chkHtr       every legal, parity-consistent state in the HTR coset (663,552 of them) is either solved or has a
                 half turn that lowers its entry in `HD` (a breadth-first table over half turns from solved).

  From "the checks hold" (`Checked`, run by `native_decide` in `HTFirst.Theorems`) the kernel proves the
  statements about states; they are collected in `HTFirst.Theorems`.
-/
import DRBound.CertifiedExact
import HTRRoutes.QtFull
import Std.Data.HashMap

set_option compiler.extract_closed false

namespace HTFirst
open DRBound HTRRoutes

/-! ### The renumbering -/

/-- DRBound's corner positions 0 UFR 1 UFL 2 UBL 3 UBR 4 DFR 5 DFL 6 DBL 7 DBR as cubie positions
(x = R, y = U, z = F). -/
def DRC : Array cube.Vec :=
  #[[1, 1, 1], [-1, 1, 1], [-1, 1, -1], [1, 1, -1], [1, -1, 1], [-1, -1, 1], [-1, -1, -1], [1, -1, -1]]
/-- DRBound's U/D-edge positions 0 UF 1 UL 2 UB 3 UR 4 DF 5 DL 6 DB 7 DR. -/
def DRE : Array cube.Vec :=
  #[[0, 1, 1], [-1, 1, 0], [0, 1, -1], [1, 1, 0], [0, -1, 1], [-1, -1, 0], [0, -1, -1], [1, -1, 0]]
/-- DRBound position ↦ place of the sticker model, and back. -/
def CH : Array Nat := DRC.map fun p => pieces.CPOS.toList.idxOf p
def CD : Array Nat := (Array.range 8).map fun i => CH.toList.idxOf i
def EH : Array Nat := DRE.map fun p => pieces.EPOS.toList.idxOf p
def ED : Array Nat := (Array.range 8).map fun i => EH.toList.idxOf i

/-- The sticker model's arrangement (a[i] = home place of the piece at place i) of DRBound corners / edges. -/
def arrC (c : Arr8) : Array Nat := (Array.range 8).map fun i => CH[(c[CD[i]!]!).val]!
def arrE (e : Arr8) : Array Nat := (Array.range 8).map fun i => EH[(e[ED[i]!]!).val]!

/-- Corner coset (0 … 419) and edge pattern (8-bit mask of the places holding M pieces). -/
def ck (c : Arr8) : Nat := cosets.cid (pieces.rank (arrC c))
def em (e : Arr8) : Nat := pieces.mMask (arrE e)
/-- **The HTR coset of a DR state.** -/
def cosetOf (g : State) : Nat := ck g.c * 256 + em g.e

def popc (m : Nat) : Nat := (List.range 8).countP fun k => (m >>> k) % 2 == 1

/-! ### The checks -/

def chkCAt (c : Arr8) : Bool :=
  decide (ck c < 420) && Move.all.all fun m => ck (permute8 m.srcC c) == cosets.CCM[ck c]![m.idx]!
def chkEAt (e : Arr8) : Bool :=
  decide (em e < 256) && popc (em e) == 4 &&
    Move.all.all fun m => em (permute8 m.srcE e) == cosets.MM[m.idx]![em e]!
def chkC : Bool := (List.range 40320).all fun r => chkCAt (Exact.unrank8 r)
def chkE : Bool := (List.range 40320).all fun r => chkEAt (Exact.unrank8 r)
def chkV : Bool := (List.range 420).all fun k => (List.range 256).all fun mk =>
  popc mk != 4 || qtfull.V (k * 256 + mk)
/-- (Written with a leading `true &&` and under `List.all`: the kernel unfolds `==` and `decide` before anything
else, and on a closed term it would then evaluate the tables.) -/
def chkSolvedAt (g : State) : Bool := true && cosetOf g == cosets.GOAL
def chkSolved : Bool := [solved].all chkSolvedAt
/-- The two models have the same ten moves: the state after move m from solved is the sticker model's. -/
def chkMoves : Bool := Move.all.all fun m =>
  arrC (solved.move m).c == pieces.CMOV[m.idx]! && arrE (solved.move m).e == pieces.EMOV[m.idx]!

/-! ### Half turns from the HTR coset -/

instance : Inhabited State := ⟨solved⟩

def halfMoves : List Move := [.U2, .D2, .R2, .L2, .F2, .B2]

def keyOf (g : State) : Nat := (Exact.rank8 g.c * 40320 + Exact.rank8 g.e) * 256 + Exact.code4 g.s

/-- Breadth-first search from solved with the six half turns: state key ↦ number of half turns. -/
def htrBfs : Std.HashMap Nat Nat := Id.run do
  let mut d : Std.HashMap Nat Nat := {}
  d := d.insert (keyOf solved) 0
  let mut q : Array State := #[solved]
  let mut head := 0
  while head < q.size do
    let g := q[head]!
    head := head + 1
    let dg := d.getD (keyOf g) 0
    for m in halfMoves do
      let h := g.move m
      if !d.contains (keyOf h) then
        d := d.insert (keyOf h) (dg + 1)
        q := q.push h
  return d
def HD : Std.HashMap Nat Nat := htrBfs
def hd (g : State) : Nat := HD.getD (keyOf g) 255

/-- g has an entry; entry 0 only at solved; from a positive entry some half turn lowers it by one. -/
def htrAt (g : State) : Bool :=
  decide (hd g < 255) && (hd g != 0 || g == solved) &&
    (hd g == 0 || halfMoves.any fun m => hd (g.move m) + 1 == hd g)

/-- Ranks of the corner arrangements / edge arrangements of the HTR coset. -/
def HTRC : List Nat := (List.range 40320).filter fun r => ck (Exact.unrank8 r) == cosets.GOAL / 256
def HTRE : List Nat := (List.range 40320).filter fun r => em (Exact.unrank8 r) == cosets.GOAL % 256

def chkHtr : Bool :=
  (halfMoves.all fun m => qtcos.st cosets.GOAL m.idx == cosets.GOAL) &&
  HTRC.all fun rc => HTRE.all fun re => Exact.allPerm4 fun s =>
    !decide (State.ParityOK ⟨Exact.unrank8 rc, Exact.unrank8 re, s⟩) ||
      htrAt ⟨Exact.unrank8 rc, Exact.unrank8 re, s⟩

/-- How many states `chkHtr` looks at (legal, parity-consistent, in the HTR coset). -/
def htrCount : Nat :=
  HTRC.length * HTRE.length * (Exact.perms4.length / 2)

structure Checked : Prop where
  c : chkC = true
  e : chkE = true
  v : chkV = true
  solved : chkSolved = true
  moves : chkMoves = true
  htr : chkHtr = true

/-! ### Moves and sequences -/

theorem idx_lt (m : Move) : m.idx < 10 := by cases m <;> decide

/-- A DR move as a move number of the coset model. -/
def mv (m : Move) : qtfull.Mv := ⟨m.idx, idx_lt m⟩

theorem isQt_idx (m : Move) : qtfull.isQt m.idx = !m.isHalf := by cases m <;> rfl

/-- The number of quarter turns (U U' D D') of a sequence. -/
def quarterTurns : List Move → Nat
  | [] => 0
  | m :: w => (!m.isHalf).toNat + quarterTurns w

theorem qts_map : ∀ w : List Move, qtfull.qts (w.map mv) = quarterTurns w
  | [] => rfl
  | m :: w => by
    simp only [List.map_cons, qtfull.qts, quarterTurns, qts_map w]
    show (qtfull.isQt m.idx).toNat + _ = _
    rw [isQt_idx]

theorem apply_append : ∀ (a b : List Move) (g : State), g.apply (a ++ b) = (g.apply a).apply b
  | [], _, _ => rfl
  | m :: a, b, g => by
    simp only [List.cons_append, State.apply_cons]
    exact apply_append a b _

theorem quarterTurns_append : ∀ (a b : List Move), quarterTurns (a ++ b) = quarterTurns a + quarterTurns b
  | [], b => by simp [quarterTurns]
  | m :: a, b => by simp only [List.cons_append, quarterTurns, quarterTurns_append a b]; omega

theorem ofIdx_mv : ∀ i, i < 10 → (Move.ofIdx i).idx = i := by decide

/-! Plain arithmetic, stated on variables: `omega` must not see the table look-ups (it compares the terms it
finds up to unfolding, and would start evaluating the tables). -/
theorem divmod256 (k e : Nat) (h : e < 256) : (k * 256 + e) / 256 = k ∧ (k * 256 + e) % 256 = e := by omega
theorem split256 (k e G : Nat) (h : e < 256) (hg : k * 256 + e = G) : k = G / 256 ∧ e = G % 256 := by omega
theorem pred_eq (a b n : Nat) (h : a + 1 = b) (hb : b = n + 1) : a = n := by omega
theorem halfMoves_half : ∀ m ∈ halfMoves, m.isHalf = true := by decide

/-- One step of `run` on a mapped sequence (by the equation of `run`; the tables are not unfolded). -/
theorem run_cons (x : Nat) (m : Move) (w : List Move) :
    qtfull.run x ((m :: w).map mv) = qtfull.run (qtcos.st x m.idx) (w.map mv) := by
  rw [List.map_cons, qtfull.run] <;> rfl

theorem and_true {a b : Bool} (h : (a && b) = true) : a = true ∧ b = true := by
  cases a <;> cases b <;> simp_all

/-! ### From the checks to statements about every state -/

theorem solvedAt_spec (g : State) (h : chkSolvedAt g = true) : cosetOf g = cosets.GOAL :=
  beq_iff_eq.mp (and_true h).2

section
variable (M : Exact.ModelChecked) (B : Checked)
include M B

theorem chkC_spec (c : Arr8) (hc : IsPerm8 c) : chkCAt c = true := by
  obtain ⟨hlt, hun⟩ := M.rank_spec c hc
  have h := List.all_eq_true.mp B.c (Exact.rank8 c) (List.mem_range.mpr hlt)
  rw [hun] at h
  exact h

theorem chkE_spec (e : Arr8) (he : IsPerm8 e) : chkEAt e = true := by
  obtain ⟨hlt, hun⟩ := M.rank_spec e he
  have h := List.all_eq_true.mp B.e (Exact.rank8 e) (List.mem_range.mpr hlt)
  rw [hun] at h
  exact h

theorem ck_lt (c : Arr8) (hc : IsPerm8 c) : ck c < 420 := by
  have h := chkC_spec M B c hc
  simp only [chkCAt, Bool.and_eq_true, decide_eq_true_eq] at h
  exact h.1

theorem em_facts (e : Arr8) (he : IsPerm8 e) : em e < 256 ∧ popc (em e) = 4 := by
  have h := chkE_spec M B e he
  simp only [chkEAt, Bool.and_eq_true, decide_eq_true_eq, beq_iff_eq] at h
  exact ⟨h.1.1, h.1.2⟩

/-- The coset of a legal state is one of the 29,400. -/
theorem cosetOf_V (g : State) (hv : g.Valid) : qtfull.V (cosetOf g) = true := by
  have h1 := ck_lt M B g.c hv.1
  obtain ⟨h2, h3⟩ := em_facts M B g.e hv.2.1
  have h := List.all_eq_true.mp (List.all_eq_true.mp B.v (ck g.c) (List.mem_range.mpr h1)) (em g.e)
    (List.mem_range.mpr h2)
  have h4 : (popc (em g.e) != 4) = false := by simp [h3]
  exact qtfull.of_or h h4

/-- **Moves commute with taking the coset.**  (No `simp` or `omega` on the table look-ups here: both compare
terms up to unfolding and would start evaluating the tables.) -/
theorem cosetOf_move (g : State) (hv : g.Valid) (m : Move) :
    cosetOf (g.move m) = qtcos.st (cosetOf g) m.idx := by
  have hc := and_true (chkC_spec M B g.c hv.1)
  have he := and_true (chkE_spec M B g.e hv.2.1)
  have h1 : ck (permute8 m.srcC g.c) = cosets.CCM[ck g.c]![m.idx]! :=
    beq_iff_eq.mp (List.all_eq_true.mp hc.2 m (Move.mem_all m))
  have h2 : em (permute8 m.srcE g.e) = cosets.MM[m.idx]![em g.e]! :=
    beq_iff_eq.mp (List.all_eq_true.mp he.2 m (Move.mem_all m))
  have h3 : em g.e < 256 := of_decide_eq_true (and_true he.1).1
  obtain ⟨hd, hm⟩ := divmod256 (ck g.c) (em g.e) h3
  show ck (permute8 m.srcC g.c) * 256 + em (permute8 m.srcE g.e) =
    cosets.stepWith cosets.CCM cosets.MM (ck g.c * 256 + em g.e) m.idx
  rw [h1, h2]
  unfold cosets.stepWith
  rw [hd, hm]

theorem cosetOf_solved : cosetOf solved = cosets.GOAL :=
  solvedAt_spec solved (List.all_eq_true.mp B.solved solved List.mem_cons_self)

theorem cosetOf_apply : ∀ (w : List Move) (g : State), g.Valid →
    cosetOf (g.apply w) = qtfull.run (cosetOf g) (w.map mv)
  | [], _, _ => rfl
  | m :: w, g, hv => by
    rw [State.apply_cons, cosetOf_apply w (g.move m) (M.valid_move g hv m), cosetOf_move M B g hv m, run_cons]

theorem apply_valid : ∀ (w : List Move) (g : State), g.Valid → (g.apply w).Valid
  | [], _, h => h
  | m :: w, g, h => by
    rw [State.apply_cons]
    exact apply_valid w _ (M.valid_move g h m)

/-! ### Half turns solve every state of the HTR coset -/

theorem htr_spec (g : State) (hv : g.Valid) (hp : g.ParityOK) (hg : cosetOf g = cosets.GOAL) :
    htrAt g = true := by
  have hh := and_true B.htr
  obtain ⟨hcl, hcu⟩ := M.rank_spec g.c hv.1
  obtain ⟨hel, heu⟩ := M.rank_spec g.e hv.2.1
  have h3 := (em_facts M B g.e hv.2.1).1
  obtain ⟨hk, hm⟩ := split256 (ck g.c) (em g.e) cosets.GOAL h3 hg
  have hc : Exact.rank8 g.c ∈ HTRC :=
    List.mem_filter.mpr ⟨List.mem_range.mpr hcl, by rw [hcu, hk]; exact beq_self_eq_true _⟩
  have he : Exact.rank8 g.e ∈ HTRE :=
    List.mem_filter.mpr ⟨List.mem_range.mpr hel, by rw [heu, hm]; exact beq_self_eq_true _⟩
  have h := Exact.allPerm4_spec (List.all_eq_true.mp (List.all_eq_true.mp hh.2 _ hc) _ he) g.s hv.2.2
  rw [hcu, heu] at h
  have hp' : decide (State.ParityOK ⟨g.c, g.e, g.s⟩) = true := decide_eq_true hp
  exact qtfull.of_imp h hp'

theorem half_keeps_htr (g : State) (hv : g.Valid) (hg : cosetOf g = cosets.GOAL) (m : Move)
    (hm : m ∈ halfMoves) : cosetOf (g.move m) = cosets.GOAL := by
  have hh := and_true B.htr
  rw [cosetOf_move M B g hv m, hg]
  exact beq_iff_eq.mp (List.all_eq_true.mp hh.1 m hm)

theorem htr_solvable_aux : ∀ (n : Nat) (g : State), g.Valid → g.ParityOK → cosetOf g = cosets.GOAL →
    hd g = n → ∃ w : List Move, (∀ m ∈ w, m.isHalf = true) ∧ g.apply w = solved
  | 0, g, hv, hp, hg, hn => by
    have h := and_true (htr_spec M B g hv hp hg)
    have h0 : (hd g != 0) = false := by simp [hn]
    have hs := qtfull.of_or (and_true h.1).2 h0
    exact ⟨[], fun _ hh => absurd hh List.not_mem_nil, of_decide_eq_true hs⟩
  | n + 1, g, hv, hp, hg, hn => by
    have h := and_true (htr_spec M B g hv hp hg)
    have h0 : (hd g == 0) = false := by simp [hn]
    obtain ⟨m, hm, hlow⟩ := List.any_eq_true.mp (qtfull.of_or h.2 h0)
    have hlow' : hd (g.move m) = n := pred_eq _ _ _ (beq_iff_eq.mp hlow) hn
    obtain ⟨w, hw, hs⟩ := htr_solvable_aux n (g.move m) (M.valid_move g hv m) (M.parityOK_move g hv hp m)
      (half_keeps_htr M B g hv hg m hm) hlow'
    refine ⟨m :: w, ?_, hs⟩
    intro x hx
    rcases List.mem_cons.mp hx with rfl | hx
    · exact halfMoves_half x hm
    · exact hw x hx

/-- **Every state of the HTR coset is solved by half turns alone.** -/
theorem htr_solvable (g : State) (hv : g.Valid) (hp : g.ParityOK) (hg : cosetOf g = cosets.GOAL) :
    ∃ w : List Move, (∀ m ∈ w, m.isHalf = true) ∧ g.apply w = solved :=
  htr_solvable_aux M B (hd g) g hv hp hg rfl

end

theorem quarterTurns_half : ∀ w : List Move, (∀ m ∈ w, m.isHalf = true) → quarterTurns w = 0
  | [], _ => rfl
  | m :: w, h => by
    simp only [quarterTurns, h m List.mem_cons_self, quarterTurns_half w fun x hx => h x (List.mem_cons_of_mem _ hx)]
    rfl

end HTFirst
