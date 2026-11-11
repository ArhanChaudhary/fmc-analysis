/-
  DRBound.CertifiedExact — the exact optimal length of every state of the domino-reduction group
  ⟨U, D, R2, L2, F2, B2⟩ (ten moves U U2 U' D D2 D' R2 L2 F2 B2, each counted as one).

  `exactDist g` is the value of the table `exactTable` at the symmetry-reduced index of `g`
  (`DRBound.Exact`).  For every legal state `g` whose three permutation parities are consistent
  (`State.ParityOK`; every state reachable from the solved cube is of this kind, `reachable_good`):

    * `exact_lower`     every solution of `g` has at least `exactDist g` moves;
    * `exact_attained`  some solution of `g` has exactly `exactDist g` moves.

  So `exactDist g` is the optimal number of DR moves.  Moreover `exactDist g ≤ 18` (`exact_le_18`), and 18
  is attained (`exact_needs_18`).

  The machine checks that these theorems rest on are in `DRBound.CertifiedExactTable`.
-/
import DRBound.CertifiedExactTable

namespace DRBound
open Exact

/-! ### Legal, parity-consistent states -/

/-- The solved cube has consistent parities. -/
theorem solved_parityOK : solved.ParityOK := exact_model_checked.solved_parityOK

/-- Moves keep the parities consistent. -/
theorem State.parityOK_move (g : State) (hg : g.Valid) (hp : g.ParityOK) (m : Move) : (g.move m).ParityOK :=
  exact_model_checked.parityOK_move g hg hp m

/-- Every state reachable from the solved cube is legal and has consistent parities. -/
theorem reachable_good (w : List Move) : (solved.apply w).Valid ∧ (solved.apply w).ParityOK :=
  exact_model_checked.good_apply w solved Exact.solved_valid solved_parityOK

/-! ### The table and the optimal length -/

/-- The table of optimal lengths.  (Not compiled: building it takes minutes.  `Exact.tableValues 18`
computes values of it.) -/
noncomputable def exactTable : ByteArray := mkTable 18

/-- **The optimal length** of a state: the table value at its reduced index. -/
noncomputable def exactDist (g : State) : Nat := tv exactTable (ridx g)

theorem exact_table_spec : TableSpec exactTable 2768 256 := (exactCheck_spec exact_checked).1

/-- **Lower bound.**  Every sequence of DR moves that solves `g` has at least `exactDist g` moves. -/
theorem exact_lower (g : State) (hg : g.Valid) (hp : g.ParityOK) (w : List Move)
    (hw : g.apply w = solved) : exactDist g ≤ w.length :=
  lower_of exact_model_checked exact_table_spec g hg hp w hw

/-- **Upper bound.**  Some sequence of exactly `exactDist g` DR moves solves `g`. -/
theorem exact_attained (g : State) (hg : g.Valid) (hp : g.ParityOK) :
    ∃ w : List Move, w.length = exactDist g ∧ g.apply w = solved :=
  attained_of exact_model_checked exact_table_spec (exactDist g) g hg hp rfl (tv_lt _ _)

/-- Both together: `exactDist g` is the length of a shortest solution of `g`. -/
theorem exact_optimal (g : State) (hg : g.Valid) (hp : g.ParityOK) :
    (∃ w : List Move, w.length = exactDist g ∧ g.apply w = solved) ∧
    (∀ w : List Move, g.apply w = solved → exactDist g ≤ w.length) :=
  ⟨exact_attained g hg hp, fun w hw => exact_lower g hg hp w hw⟩

/-- No state needs more than 18 moves. -/
theorem exact_le_18 (g : State) (hg : g.Valid) : exactDist g ≤ 18 :=
  tv_le_of_max exact_model_checked (exactCheck_spec exact_checked).2.1 g hg

/-- Every legal, parity-consistent state can be solved in at most 18 moves. -/
theorem exact_solvable_18 (g : State) (hg : g.Valid) (hp : g.ParityOK) :
    ∃ w : List Move, w.length ≤ 18 ∧ g.apply w = solved := by
  obtain ⟨w, hw, hs⟩ := exact_attained g hg hp
  exact ⟨w, Nat.le_trans (Nat.le_of_eq hw) (exact_le_18 g hg), hs⟩

/-- The table values of the sample scrambles. -/
theorem exact_samples : ∀ c ∈ exactSamples, exactDist (solved.apply c.1) = c.2 :=
  (exactCheck_spec exact_checked).2.2.2

/-- Some state needs 18 moves: every solution of the state reached by the sample scramble has at least 18
moves. -/
theorem exact_needs_18 : ∃ g : State, g.Valid ∧ g.ParityOK ∧ exactDist g = 18 ∧
    ∀ w : List Move, g.apply w = solved → 18 ≤ w.length := by
  obtain ⟨c, hc, h18⟩ : ∃ c ∈ exactSamples, c.2 = 18 := ⟨_, List.mem_cons_self, rfl⟩
  have hd : exactDist (solved.apply c.1) = 18 := (exact_samples c hc).trans h18
  have hg := reachable_good c.1
  exact ⟨solved.apply c.1, hg.1, hg.2, hd,
    fun w hw => Nat.le_trans (Nat.le_of_eq hd.symm) (exact_lower _ hg.1 hg.2 w hw)⟩

/-! ### Counting

`Exact.depthCounts exactTable 2768 19` lists, for `d` = 0 … 18, the number of table entries with value `d`,
where an entry in the row of corner class `k` is counted `Exact.classWeight k` = 16 / (number of symmetries
fixing the class representative) times; its last element counts the entries with value 19 or more.

**Not proved in Lean:** that this weighted count of table entries is the number of *states* with optimal
length `d`.  The argument is the orbit–stabiliser fact.  For a corner arrangement `c` of class `k`,
conjugation by `Exact.symTo c` is a bijection from the legal, parity-consistent states with corners `c` onto
those with corners `Exact.crep k`, which are the entries of row `k`, and it preserves the optimal length;
and class `k` consists of exactly `Exact.classWeight k` = 16 / (size of the stabiliser) arrangements.  So
the states with corners in class `k` and optimal length `d` number `classWeight k` times the entries of row
`k` with value `d`.  With this, the list below is the distribution of optimal lengths over all
8! · 8! · 4! / 2 = 19,508,428,800 states (`exactCounts_total`). -/

/-- The weighted numbers of table entries with values 0, 1, …, 18 (and none with a larger value). -/
theorem exact_depth_counts : depthCounts exactTable 2768 19 =
    [1, 10, 67, 456, 3079, 19948, 123074, 736850, 4185118, 22630733, 116767872, 552538680, 2176344160,
     5627785188, 7172925794, 3608731814, 224058996, 1575608, 1352, 0] :=
  (exactCheck_spec exact_checked).2.2.1

/-- The counts add up to 8! · 8! · 4! / 2 = 19,508,428,800. -/
theorem exactCounts_total : exactCounts.foldl (· + ·) 0 = 19508428800 := by decide

end DRBound
