/-
  DRBound.Theorems — from exhaustive checks to statements about every DR state.

  For a rung `R` (a way of looking at the cube, see `DRBound.Search`) we prove, for every legal state `g`:

    * `lower_bound`          every DR-move solution of `g` has at least `R.bound g` moves;
    * `lower_bound_inverse`  the same with the bound read off the inverse state (NISS side).

  The only inputs are three machine checks, collected in `Rung.Checked`:
    corners / edges : for each of the 8⁸ ways to fill eight positions that is a permutation, the class number
                      is in range and the class move-table agrees with really doing each of the ten moves
                      (`Rung.cornersOK`, `Rung.edgesOK`);
    table           : the table is 0 at the solved class and differs by at most 1 across every move.
-/
import DRBound.Search

namespace DRBound

/-! ### Plumbing -/

theorem nat_all_spec : ∀ (n : Nat) (f : (i : Nat) → i < n → Bool), n.all f = true →
    ∀ (i : Nat) (h : i < n), f i h = true
  | 0, _, _, i, h => absurd h (Nat.not_lt_zero i)
  | n + 1, f, hall, i, h => by
      rw [Nat.all_succ] at hall
      simp only [Bool.and_eq_true] at hall
      rcases Nat.lt_succ_iff_lt_or_eq.mp h with hlt | heq
      · exact nat_all_spec n _ hall.1 i hlt
      · subst heq; exact hall.2

/-- Checked for all 8⁸ fillings: a legal arrangement stays legal after any move. -/
theorem movesKeepPerm8_all : movesKeepPermAll = true := by
  native_decide

/-- Checked for all 4⁴ fillings of the E slice: legality is kept, side half turns flip the parity. -/
theorem sliceOK_all : sliceOKAll = true := by
  native_decide

theorem perm8_move (v : Arr8) (hv : IsPerm8 v) (m : Move) :
    IsPerm8 (permute8 m.srcC v) ∧ IsPerm8 (permute8 m.srcE v) := by
  have h := all8_spec (P := movesKeepPerm8) movesKeepPerm8_all v
  simp only [movesKeepPerm8, Bool.or_eq_true, Bool.not_eq_true', decide_eq_false_iff_not,
    List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq] at h
  rcases h with h | h
  · exact absurd hv h
  · exact h m (Move.mem_all m)

theorem slice_move (s : Arr4) (hs : IsPerm4 s) (m : Move) :
    parity4 s < 2 ∧ IsPerm4 (permute4 m.srcS s) ∧
      parity4 (permute4 m.srcS s) = (if m.isSide then 1 - parity4 s else parity4 s) := by
  have h := all4_spec (P := sliceOK) sliceOK_all s
  simp only [sliceOK, Bool.or_eq_true, Bool.not_eq_true', decide_eq_false_iff_not,
    List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq, beq_iff_eq] at h
  rcases h with h | h
  · exact absurd hs h
  · exact ⟨h.1, h.2 m (Move.mem_all m)⟩

/-- Legal states stay legal. -/
theorem State.valid_move (g : State) (m : Move) (hg : g.Valid) : (g.move m).Valid :=
  ⟨(perm8_move g.c hg.1 m).1, (perm8_move g.e hg.2.1 m).2, (slice_move g.s hg.2.2 m).2.1⟩

theorem solved_valid : solved.Valid := by decide

/-! ### What has to be checked for a rung -/

structure Rung.Checked (R : Rung) : Prop where
  corners : R.cornersOK = true
  edges : R.edgesOK = true
  table : R.checkTable = true

theorem Comp.ok_spec (C : Comp) (src : Move → Arr8)
    (h : all8 (C.okAt src) = true) (v : Arr8) (hv : IsPerm8 v) :
    C.feat v < C.n ∧ ∀ m : Move, C.mv.getD (C.feat v * 10 + m.idx) 0 = C.feat (permute8 (src m) v) := by
  have h' := all8_spec (P := C.okAt src) h v
  simp only [Comp.okAt, Bool.or_eq_true, Bool.not_eq_true', decide_eq_false_iff_not,
    List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq, beq_iff_eq] at h'
  rcases h' with h' | h'
  · exact absurd hv h'
  · exact ⟨h'.1, fun m => h'.2 m (Move.mem_all m)⟩

namespace Rung

variable (R : Rung)

theorem pbit_lt (s : Arr4) (hs : IsPerm4 s) : R.pbit s < R.pmul := by
  unfold pbit pmul
  cases R.par
  · simp
  · simpa using (slice_move s hs Move.U).1

theorem pbit_move (s : Arr4) (hs : IsPerm4 s) (m : Move) :
    R.pbit (permute4 m.srcS s) = R.pnext (R.pbit s) m := by
  unfold pbit pnext
  cases hp : R.par
  · simp
  · have h := (slice_move s hs m).2.2
    cases hm : m.isSide <;> simp [hm] at h ⊢ <;> exact h

/-- What we see after a move is what the class table says. -/
theorem index_move (ok : R.Checked) (g : State) (hg : g.Valid) (m : Move) :
    R.index (g.move m) = R.qnext (R.cC.feat g.c) (R.cE.feat g.e) (R.pbit g.s) m := by
  have hc := (Comp.ok_spec R.cC Move.srcC ok.corners g.c hg.1).2 m
  have he := (Comp.ok_spec R.cE Move.srcE ok.edges g.e hg.2.1).2 m
  have hp := R.pbit_move g.s hg.2.2 m
  simp only [index, qnext, State.move, hc, he, hp]

theorem table_spec (ok : R.Checked) :
    R.table.get! (R.index solved) = 0 ∧
    ∀ cc, cc < R.cC.n → ∀ ee, ee < R.cE.n → ∀ p, p < R.pmul → ∀ m : Move,
      (R.table.get! (R.q cc ee p)).toNat ≤ (R.table.get! (R.qnext cc ee p m)).toNat + 1 ∧
      (R.table.get! (R.qnext cc ee p m)).toNat ≤ (R.table.get! (R.q cc ee p)).toNat + 1 := by
  have h := ok.table
  simp only [checkTable, Bool.and_eq_true] at h
  replace h := h.1
  simp only [tableOK, Bool.and_eq_true, beq_iff_eq] at h
  refine ⟨h.1, ?_⟩
  intro cc hcc ee hee p hp m
  have h1 := nat_all_spec _ _ h.2 cc hcc
  have h2 := nat_all_spec _ _ h1 ee hee
  have h3 := nat_all_spec _ _ h2 p hp
  simp only [List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq] at h3
  exact h3 m (Move.mem_all m)

/-- One move changes the bound by at most one, in either direction. -/
theorem bound_move (ok : R.Checked) (g : State) (hg : g.Valid) (m : Move) :
    R.bound g ≤ R.bound (g.move m) + 1 ∧ R.bound (g.move m) ≤ R.bound g + 1 := by
  have hcc := (Comp.ok_spec R.cC Move.srcC ok.corners g.c hg.1).1
  have hee := (Comp.ok_spec R.cE Move.srcE ok.edges g.e hg.2.1).1
  have hp := R.pbit_lt g.s hg.2.2
  have h := (R.table_spec ok).2 _ hcc _ hee _ hp m
  unfold bound
  rw [R.index_move ok g hg m]
  exact h

theorem bound_solved (ok : R.Checked) : R.bound solved = 0 := by
  unfold bound
  rw [(R.table_spec ok).1]
  rfl

/-- **Lower bound (normal side).**  Every sequence of DR moves that solves `g` has at least
`R.bound g` moves. -/
theorem lower_bound (ok : R.Checked) (g : State) (hg : g.Valid) (w : List Move)
    (hw : g.apply w = solved) : R.bound g ≤ w.length := by
  have h := solution_length_ge State.move State.Valid State.valid_move R.index
    (fun q => (R.table.get! q).toNat) solved
    (fun s m hs => (R.bound_move ok s hs m).1) (R.bound_solved ok) g hg w hw
  exact h

/-- Doing `n` moves from the solved cube gives a state whose bound is at most `n`. -/
theorem bound_apply_solved (ok : R.Checked) (w : List Move) : R.bound (solved.apply w) ≤ w.length := by
  have h := table_rise_le_length State.move State.Valid State.valid_move R.index
    (fun q => (R.table.get! q).toNat) (fun s m hs => (R.bound_move ok s hs m).2) w solved solved_valid
  have h0 := R.bound_solved ok
  unfold bound at h0
  simp only [h0, Nat.zero_add] at h
  exact h

/-- From any class with a positive finite value some move goes down by one; value 0 means "looks solved". -/
theorem sharp_spec (ok : R.Checked) (g : State) (hg : g.Valid) (hb : R.bound g < 255) :
    (R.bound g = 0 → R.index g = R.index solved) ∧
    (R.bound g ≠ 0 → ∃ m : Move, R.bound (g.move m) + 1 = R.bound g) := by
  have hcc := (Comp.ok_spec R.cC Move.srcC ok.corners g.c hg.1).1
  have hee := (Comp.ok_spec R.cE Move.srcE ok.edges g.e hg.2.1).1
  have hp := R.pbit_lt g.s hg.2.2
  have h := ok.table
  simp only [checkTable, Bool.and_eq_true] at h
  have h3 := nat_all_spec _ _ (nat_all_spec _ _ (nat_all_spec _ _ h.2 _ hcc) _ hee) _ hp
  simp only [Bool.or_eq_true, Bool.and_eq_true, beq_iff_eq, bne_iff_ne, List.any_eq_true] at h3
  have hidx : R.q (R.cC.feat g.c) (R.cE.feat g.e) (R.pbit g.s) = R.index g := rfl
  rw [hidx] at h3
  unfold bound at hb ⊢
  refine ⟨fun h0 => ?_, fun hne => ?_⟩
  · rcases h3 with (h3 | h3) | h3
    · exact h3.2
    · omega
    · exact absurd h0 h3.1
  · rcases h3 with (h3 | h3) | h3
    · exact absurd h3.1 hne
    · omega
    · obtain ⟨m, _, hm⟩ := h3.2
      exact ⟨m, by rw [R.index_move ok g hg m]; exact hm⟩

/-- **Sharpness.**  The bound is exactly the fewest moves needed to make the visible part solved: there is a
sequence of `R.bound g` moves after which `g` looks solved through the eyes of rung `R`.
(So no better bound can be read off these features alone.) -/
theorem bound_attained (ok : R.Checked) : ∀ (d : Nat) (g : State), g.Valid → R.bound g = d → d < 255 →
    ∃ w : List Move, w.length = d ∧ R.index (g.apply w) = R.index solved
  | 0, g, hg, hd, _ => ⟨[], rfl, (R.sharp_spec ok g hg (by omega)).1 hd⟩
  | d + 1, g, hg, hd, hlt => by
      obtain ⟨m, hm⟩ := (R.sharp_spec ok g hg (by omega)).2 (by omega)
      obtain ⟨w, hw, hsol⟩ := bound_attained ok d (g.move m) (State.valid_move g m hg) (by omega) (by omega)
      exact ⟨m :: w, by simp [hw], hsol⟩

/-! #### Half turns only -/

theorem half_step (hT : R.checkHalfTable = true) (ok : R.Checked) (g : State) (hg : g.Valid) (m : Move)
    (hm : m.isHalf = true) : R.halfBound g ≤ R.halfBound (g.move m) + 1 := by
  have hcc := (Comp.ok_spec R.cC Move.srcC ok.corners g.c hg.1).1
  have hee := (Comp.ok_spec R.cE Move.srcE ok.edges g.e hg.2.1).1
  have hp := R.pbit_lt g.s hg.2.2
  simp only [checkHalfTable, halfTableOK, Bool.and_eq_true] at hT
  have h3 := nat_all_spec _ _ (nat_all_spec _ _ (nat_all_spec _ _ hT.2 _ hcc) _ hee) _ hp
  simp only [List.all_eq_true, Bool.or_eq_true, Bool.not_eq_true', decide_eq_true_eq] at h3
  unfold halfBound
  rw [R.index_move ok g hg m]
  rcases h3 m (Move.mem_all m) with h | h
  · rw [hm] at h; exact absurd h (by decide)
  · exact h

/-- **HTR-only lower bound.**  Every solution of `g` that uses half turns only has at least
`R.halfBound g` moves. -/
theorem half_lower_bound (hT : R.checkHalfTable = true) (ok : R.Checked) :
    ∀ (w : List Move) (g : State), g.Valid → (∀ m ∈ w, m.isHalf = true) → g.apply w = solved →
      R.halfBound g ≤ w.length
  | [], g, _, _, hw => by
      simp only [State.apply_nil] at hw
      subst hw
      simp only [checkHalfTable, halfTableOK, Bool.and_eq_true, beq_iff_eq] at hT
      unfold halfBound; rw [hT.1]; decide
  | m :: w, g, hg, hall, hw => by
      have h1 := R.half_step hT ok g hg m (hall m (by simp))
      have h2 := half_lower_bound hT ok w (g.move m) (State.valid_move g m hg)
        (fun x hx => hall x (by simp [hx])) hw
      simp only [List.length_cons]; omega

end Rung

/-! ### The inverse side -/

theorem apply_c : ∀ (w : List Move) (g : State) (p : Fin 8),
    (g.apply w).c.get p = g.c.get ((solved.apply w).c.get p)
  | [], g, p => by simp [solved]
  | m :: w, g, p => by
      rw [State.apply_cons, State.apply_cons, apply_c w (g.move m) p, apply_c w (solved.move m) p]
      simp [State.move, solved]

theorem apply_e : ∀ (w : List Move) (g : State) (p : Fin 8),
    (g.apply w).e.get p = g.e.get ((solved.apply w).e.get p)
  | [], g, p => by simp [solved]
  | m :: w, g, p => by
      rw [State.apply_cons, State.apply_cons, apply_e w (g.move m) p, apply_e w (solved.move m) p]
      simp [State.move, solved]

theorem apply_s : ∀ (w : List Move) (g : State) (p : Fin 4),
    (g.apply w).s.get p = g.s.get ((solved.apply w).s.get p)
  | [], g, p => by simp [solved]
  | m :: w, g, p => by
      rw [State.apply_cons, State.apply_cons, apply_s w (g.move m) p, apply_s w (solved.move m) p]
      simp [State.move, solved]

theorem vec8_ext (a b : Arr8) (h : ∀ p : Fin 8, a.get p = b.get p) : a = b :=
  Vector.ext fun i hi => by simpa [Vector.get] using h ⟨i, hi⟩

theorem vec4_ext (a b : Arr4) (h : ∀ p : Fin 4, a.get p = b.get p) : a = b :=
  Vector.ext fun i hi => by simpa [Vector.get] using h ⟨i, hi⟩

/-- If `w` solves `g`, then the inverse state of `g` is exactly the state that `w` produces from the
solved cube.  (This is the precise content of "switching to the inverse scramble".) -/
theorem inverse_eq_apply_solved (g h : State) (hg : g.Valid) (hh : h.IsInverseOf g) (w : List Move)
    (hw : g.apply w = solved) : h = solved.apply w := by
  have hc : h.c = (solved.apply w).c := vec8_ext _ _ fun p => by
    apply hg.1
    rw [hh.1 p, ← apply_c w g p, hw]; simp [solved]
  have he : h.e = (solved.apply w).e := vec8_ext _ _ fun p => by
    apply hg.2.1
    rw [hh.2.1 p, ← apply_e w g p, hw]; simp [solved]
  have hs : h.s = (solved.apply w).s := vec4_ext _ _ fun p => by
    apply hg.2.2
    rw [hh.2.2 p, ← apply_s w g p, hw]; simp [solved]
  cases h
  cases hsol : solved.apply w
  simp only [hsol] at hc he hs
  simp only [hc, he, hs]

/-- **Lower bound (inverse side).**  If `h` is the inverse of `g`, every DR-move solution of `g` has at
least `R.bound h` moves. -/
theorem Rung.lower_bound_inverse (R : Rung) (ok : R.Checked) (g h : State) (hg : g.Valid)
    (hh : h.IsInverseOf g) (w : List Move) (hw : g.apply w = solved) : R.bound h ≤ w.length := by
  rw [inverse_eq_apply_solved g h hg hh w hw]
  exact R.bound_apply_solved ok w

end DRBound
