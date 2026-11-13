/-
  DRBound.PageChecks — the DR states that the published write-up of judging-a-dr prints with an optimal finish, an
  HTR length or a level (`Page.pageOptima`, `pageHTR`, `pageSolves`, `pageInHTR`, `pageLevels`, generated from
  report/WRITEUP.md by research/src/gen_page_checks.py), checked against the proved tables:

  * `page_optima_correct`  each stated optimal DR finish is exact (`exact_optimal`);
  * `page_solves`          each printed finish solves its state with the stated length;
  * `page_htr`             each stated shortest HTR (normal, inverse) is the value of the HTR rung (`rungHTR`, whose
                           table is the BFS distance to the HTR coset, `htr_length_bound`);
  * `page_in_htr`          each printed HTR lands in the HTR coset;
  * `page_levels`          the stated levels on the docs' examples (HTR, L, L with parity, L+S+T, NISS@DR,
                           NISS@DR + H-perm parity, on normal and on inverse) are the rung values;
  * `rung_maxima`          the "largest value" column of the seven-levels table for the six smaller rungs, and so
                           (HTR rung) the longest shortest DR→HTR is 13;
  * `niss_htr`             errata B1 with NISS: two states with a NISS HTR of 11, one with none of 11 or less and one
                           of 12 (with a paper step, stated at the theorem).
-/
import DRBound.PageDefs
import DRBound.Certified

namespace DRBound.Page

set_option maxHeartbeats 0

theorem page_parse_ok :
    (pageOptima.all fun c => (drMoves? c.2.1).isSome) ∧ (pageHTR.all fun c => (drMoves? c.2.1).isSome) ∧
    (pageSolves.all fun c => (drMoves? c.2.1).isSome && (drMoves? c.2.2.1).isSome) ∧
    (pageInHTR.all fun c => (drMoves? c.2.1).isSome && (drMoves? c.2.2).isSome) ∧
    (pageLevels.all fun c => (drMoves? c.2.1).isSome) := by native_decide

theorem exactDist_eq_tableValues (gs : List State) : gs.map exactDist = Exact.tableValues 18 gs := rfl

theorem entries {l : List (String × String × Nat)}
    (h : l.map (fun c => exactDist (st c.2.1)) = l.map (·.2.2)) :
    ∀ c ∈ l, exactDist (st c.2.1) = c.2.2 := by
  induction l with
  | nil => intro c hc; cases hc
  | cons a l ih =>
    intro c hc
    simp only [List.map_cons, List.cons.injEq] at h
    rcases List.mem_cons.mp hc with rfl | hc
    · exact h.1
    · exact ih h.2 c hc

theorem page_values : pageOptima.map (fun c => exactDist (st c.2.1)) = pageOptima.map (·.2.2) := by
  have h := page_table_lookup
  rw [← exactDist_eq_tableValues, List.map_map, Function.comp_def] at h
  exact h

/-- **Every stated optimal DR finish on the page is exact**: for each listed state, every DR-move solution has at
least the stated number of moves, and one has exactly that many. -/
theorem page_optima_correct : ∀ c ∈ pageOptima,
    (∃ w : List Move, w.length = c.2.2 ∧ (st c.2.1).apply w = solved) ∧
    (∀ w : List Move, (st c.2.1).apply w = solved → c.2.2 ≤ w.length) := by
  intro c hc
  have hv := entries page_values c hc
  obtain ⟨hval, hpar⟩ := reachable_good (drMoves c.2.1)
  obtain ⟨h1, h2⟩ := exact_optimal (st c.2.1) hval hpar
  rw [hv] at h1 h2
  exact ⟨h1, h2⟩

/-- The printed finishes solve their states, with the stated lengths. -/
theorem page_solves :
    pageSolves.all (fun c => (st c.2.1).apply (drMoves c.2.2.1) == solved && (drMoves c.2.2.1).length == c.2.2.2) = true := by
  native_decide

/-- Both sides of every state of a list, in order (normal, inverse, normal, inverse, …). -/
def bothSides (l : List String) : List State := l.flatMap fun s => [st s, stInv s]

/-- The stated shortest HTR lengths, normal and inverse, are the HTR rung's values. -/
theorem page_htr :
    rungHTR.bounds (bothSides (pageHTR.map (·.2.1))) = pageHTR.flatMap (fun c => [c.2.2.1, c.2.2.2]) := by
  native_decide

/-- The printed HTRs land in the HTR coset (HTR rung value 0, the value of the solved cube). -/
theorem page_in_htr :
    rungHTR.bounds (pageInHTR.map fun c => (st c.2.1).apply (drMoves c.2.2)) = pageInHTR.map (fun _ => 0) := by
  native_decide

/-- Rung `i` of the stated levels agrees on every listed example where the page states a value. -/
def levelOK (R : Rung) (i : Nat) : Bool :=
  let vs := R.bounds (bothSides (pageLevels.map (·.2.1)))
  (List.range pageLevels.length).all fun k =>
    match (pageLevels[k]!).2.2[i]! with
    | none => true
    | some (a, b) => vs[2 * k]! == a && vs[2 * k + 1]! == b

theorem page_levels :
    levelOK rungHTR 0 && levelOK rungC 1 && levelOK rungCP 2 && levelOK rungCBadP 3 && levelOK rungKF 4 &&
      levelOK rungK0F 5 = true := by
  native_decide

/-- The largest finite value in a rung's table. -/
def tableMax (R : Rung) : Nat := Id.run do
  let T := R.table
  let mut m := 0
  for i in [0:T.size] do
    let v := (T.get! i).toNat
    if v != 255 && v > m then m := v
  return m

/-- The "largest value" column of the seven-levels table (all but the finest level). The HTR rung's 13 is the
longest shortest DR→HTR (errata B1). -/
theorem rung_maxima :
    [tableMax rungHTR, tableMax rungC, tableMax rungCP, tableMax rungCBadP, tableMax rungKF, tableMax rungK0F]
      = [13, 13, 14, 15, 15, 16] := by
  native_decide

/-! ### DR → HTR with NISS (errata B1)

A NISS HTR of the state of `scr` is a pair of DR-move sequences `a` (on inverse, i.e. done before the scramble) and
`b` (on normal) with `a ++ scr ++ b` in HTR; its length is `|a| + |b|`.  For a fixed `a` the shortest `b` is the HTR
rung's value of `a ++ scr` (`rungHTR`: the BFS distance to the HTR coset, `Rung.bound_attained`).  A NISS HTR of
length ≤ 11 has a side of length ≤ 5, and its `b` side is the `a` side of the inverse scramble.  So `nissHTR5`
(the minimum over all `a` of length ≤ 5, on the scramble and on its inverse) is the shortest NISS HTR when it is ≤ 11,
and a value of 12 or more says there is no NISS HTR of 11 or less.  (That last step is this paragraph, not a Lean
theorem.) -/

/-- **Errata B1, the NISS half.**  The two 0c3 4e states of B1 (13 / 12 and 13 / 13 to HTR linearly) have a NISS HTR
of 11.  The 0c3 4e `B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U` (13 on both sides) has none of 11 or less, and
`U R2 U2 F2 U' F2 R2 U` on normal with `B2 U L2 U` on inverse is one of 12.  So "11 moves using NISS" is not the
maximum either. -/
theorem niss_htr :
    nissHTR5 "U' R2 D' B2 U B2 U' R2 U F2 U' F2 U" = 11 ∧
    nissHTR5 "D B2 D' B2 D L2 U L2 U' F2 D B2 U' F2" = 11 ∧
    nissHTR5 "B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U" = 12 ∧
    rungHTR.bounds [solved.apply ((drMoves "B2 U L2 U").reverse.map Move.inv ++
        drMoves "B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U" ++ drMoves "U R2 U2 F2 U' F2 R2 U")] = [0] ∧
    (drMoves "B2 U L2 U").length + (drMoves "U R2 U2 F2 U' F2 R2 U").length = 12 := by
  native_decide

end DRBound.Page
