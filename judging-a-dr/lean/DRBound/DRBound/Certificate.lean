/-
  DRBound.Certificate — the one piece of mathematics everything else rests on.

  Setting.  A puzzle has states `S` and moves `M`; `step s m` is the state after doing move `m`.
  We look at the puzzle through a "feature" map `feat : S → Q` (what we can see of a state), and we are
  given a table `T : Q → Nat`.

  Claim.  Suppose
    * features commute with moves: `feat (step s m) = qstep (feat s) m`,
    * the table changes by at most one per move: `T q ≤ T (qstep q m) + 1`.
  Then a sequence of `n` moves can lower `T` by at most `n`.  In particular, if the solved state has
  table value 0, every solution of `s` has at least `T (feat s)` moves.

  This is the "admissible heuristic" argument of optimal solvers, and it is exactly the logic behind
  DR bounding: Levi Gibson's 1qt bound and Rodney Kinney's NISS@1qt tables are instances.
-/
namespace DRBound

variable {S M Q : Type}

/-- Do the moves of `w` one after the other, starting from `s`. -/
def run (step : S → M → S) : S → List M → S
  | s, [] => s
  | s, m :: w => run step (step s m) w

/-- Legal states stay legal under any move sequence. -/
theorem run_valid (step : S → M → S) (valid : S → Prop)
    (valid_step : ∀ s m, valid s → valid (step s m)) :
    ∀ (w : List M) (s : S), valid s → valid (run step s w)
  | [], _, h => h
  | m :: w, s, h => run_valid step valid valid_step w (step s m) (valid_step s m h)

/-- **Going down.**  A move sequence of length `n` lowers the table value by at most `n`. -/
theorem table_drop_le_length
    (step : S → M → S) (valid : S → Prop)
    (valid_step : ∀ s m, valid s → valid (step s m))
    (feat : S → Q) (T : Q → Nat)
    (h_step : ∀ s m, valid s → T (feat s) ≤ T (feat (step s m)) + 1) :
    ∀ (w : List M) (s : S), valid s → T (feat s) ≤ w.length + T (feat (run step s w))
  | [], s, _ => by simp [run]
  | m :: w, s, hs => by
      have h1 := h_step s m hs
      have h2 := table_drop_le_length step valid valid_step feat T h_step w (step s m) (valid_step s m hs)
      simp only [run, List.length_cons]
      omega

/-- **Going up.**  A move sequence of length `n` raises the table value by at most `n`. -/
theorem table_rise_le_length
    (step : S → M → S) (valid : S → Prop)
    (valid_step : ∀ s m, valid s → valid (step s m))
    (feat : S → Q) (T : Q → Nat)
    (h_step : ∀ s m, valid s → T (feat (step s m)) ≤ T (feat s) + 1) :
    ∀ (w : List M) (s : S), valid s → T (feat (run step s w)) ≤ T (feat s) + w.length
  | [], s, _ => by simp [run]
  | m :: w, s, hs => by
      have h1 := h_step s m hs
      have h2 := table_rise_le_length step valid valid_step feat T h_step w (step s m) (valid_step s m hs)
      simp only [run, List.length_cons]
      omega

/-- **Lower bound.**  If the solved state has table value 0, any solution of `s` has at least
`T (feat s)` moves. -/
theorem solution_length_ge
    (step : S → M → S) (valid : S → Prop)
    (valid_step : ∀ s m, valid s → valid (step s m))
    (feat : S → Q) (T : Q → Nat) (solved : S)
    (h_step : ∀ s m, valid s → T (feat s) ≤ T (feat (step s m)) + 1)
    (h_solved : T (feat solved) = 0)
    (s : S) (hs : valid s) (w : List M) (hw : run step s w = solved) :
    T (feat s) ≤ w.length := by
  have h := table_drop_le_length step valid valid_step feat T h_step w s hs
  rw [hw, h_solved] at h
  simpa using h

end DRBound
