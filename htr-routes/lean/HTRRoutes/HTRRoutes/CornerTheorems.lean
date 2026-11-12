/-
  HTRRoutes.CornerTheorems — checked statements, part C: corner cases (see README.md).  `native_decide` runs the
  statement as compiled code; `decide` is Lean's kernel alone (plain arithmetic).

  Corner subsets by index: 0 0c0, 1 4a1, 2 4a2, 3 4b2, 4 0c3, 5 2c3, 6 4a3, 7 4b3, 8 0c4, 9 2c4, 10 4a4, 11 4b4,
  12 2c5, 13 4b5.  Ranks r = 0 … 40319 stand for the corner arrangements (`ranks` in `Model.lean`).
-/
import HTRRoutes.Corners
import HTRRoutes.Parse

namespace HTRRoutes
open pieces corners

set_option maxHeartbeats 0

/-! ## C. Corner cases -/

/-- The HTR corners: 96 arrangements are reached from solved by half turns; with U D' added, 192 ("HTR corners up
to U D'", the targets of the quarter-turn count). -/
theorem htr_corners : HC.size = 96 ∧ (List.range NC).countP inZ = 192 := by native_decide

/-- The quarter-turn count `qt` passes the independent check `qtRule`, so qt r is the fewest quarter turns of any
DR move sequence taking the corners r into HTR up to U D'.  Over the 40,320 arrangements: 0 qt 192, 1 qt 1152,
2 qt 5760, 3 qt 11328, 4 qt 14208, 5 qt 7680.  No corner case needs more than 5. -/
theorem qt_checked :
    qtRule = true ∧
    hist QTC.toList = [(0, 192), (1, 1152), (2, 5760), (3, 11328), (4, 14208), (5, 7680)] := by native_decide

/-- Every arrangement gets one of the 14 subsets (no combination of bad corners, qt and shape falls outside the
table); the subset is the same for every arrangement of a coset and does not change under half turns; there are
420 corner cosets, each of 96 arrangements. -/
theorem subsets_well_defined : subsetChecks = true ∧ REPS.size = 420 := by native_decide

/-- The 14 corner subsets: (name, cosets, the qt of every arrangement in it, bad corners of its arrangements).
The quarter-turn count in each name is the true fewest quarter turns (`qt_checked`); 0c0 holds the 2 cosets HTR and
U D'·HTR; the cosets add up to 420. -/
theorem subset_table :
    (List.range 14).map (fun t =>
      (NAMES[t]!, (REPS.toList.filter fun r => sub r == t).length,
       (((List.range NC).filter fun r => sub r == t).map qt).eraseDups,
       (((List.range NC).filter fun r => sub r == t).map fun r => NBAD[r]!).eraseDups.mergeSort (· ≤ ·))) =
    [("0c0", 2, [0], [0, 8]), ("4a1", 12, [1], [4]), ("4a2", 12, [2], [4]), ("4b2", 48, [2], [4]),
     ("0c3", 6, [3], [0, 8]), ("2c3", 64, [3], [2, 6]), ("4a3", 24, [3], [4]), ("4b3", 24, [3], [4]),
     ("0c4", 4, [4], [0, 8]), ("2c4", 96, [4], [2, 6]), ("4a4", 24, [4], [4]), ("4b4", 24, [4], [4]),
     ("2c5", 32, [5], [2, 6]), ("4b5", 48, [5], [4])] := by
  native_decide

/-- The inverse of an arrangement (the corners of the inverse scramble) is in the same subset, except that 4a3 and
4b3 swap, and 4a4 and 4b4 swap: so the a/b letter of 3 and 4 qt is a property of the side, and Mallard's 48
subsets merge them as 4c3 and 4c4.  The 2 qt letters (4a2, 4b2) are the same on both sides. -/
theorem inverse_subsets :
    (List.range NC).all fun r =>
      sub CINV[r]! == (match sub r with | 6 => 7 | 7 => 6 | 10 => 11 | 11 => 10 | t => t) := by
  native_decide

/-- **Fake HTRs** (claim C07, zakimoshi's "5/6"): of the 576 corner arrangements with no bad corner (every corner
in its own tetrad), exactly 96 are 0c0, and they are the HTR corners; 288 are 0c3 and 192 are 0c4. -/
theorem fake_htr :
    noBad.length = 576 ∧ hist (noBad.map sub) = [(0, 96), (4, 288), (8, 192)] ∧
    (noBad.all fun r => (sub r == 0) == inHC r) := by
  native_decide

/-- 480 / 576 = 5 / 6, and the research's claim row C07 says the same numbers. -/
theorem fake_htr_as_study :
    576 - 96 = 480 ∧ 480 * 6 = 576 * 5 ∧
    parse.says study.CLAIM_C07 "no bad corner (DR on all three axes): 576; of these 96 are 0c0" ∧
    parse.says study.CLAIM_C07 "480/576 = 0.8333" := by
  native_decide

/-- **Bare quarter turns** (claim C10): of the 11,328 arrangements with qt = 3, a single U, U', D or D' done on the
arrangement or on its inverse gives qt = 2 for 7,488 (66.10…%, rodneykinney's 2/3); of the 14,208 with qt = 4,
for none. -/
theorem bare_quarter_turns : bareQt 3 = (11328, 7488) ∧ bareQt 4 = (14208, 0) := by native_decide

theorem bare_quarter_turns_as_study :
    7488 * 1000 / 11328 = 661 ∧
    parse.says study.CLAIM_C10 "takes a 3qt case to 2qt in 66.1%" ∧
    parse.says study.CLAIM_C10 "cannot reach 2qt with one quarter turn (0.0%)" := by
  native_decide

/-! ### FakeMMAP's section bounds -/

/-- The tables `HT[t]` (fewest half turns to an arrangement from which a quarter turn lands in subset t) pass
`search.ruleHolds` for all 14 subsets. -/
theorem ht_checked :
    (List.range 14).all fun t =>
      search.ruleHolds NC (fun r => QT.any fun m => sub (step r m) == t) HALF step HT[t]! := by
  native_decide

/-- FakeMMAP's example (T11501): on the corner path 4a3 > 4b2 > 4a1 > HTR the sections must have at least
0, 3, 1, 0 half turns, and some arrangement follows the path. -/
theorem alpha_example : alphaOf HT (parsePath "4a3 > 4b2 > 4a1 > 0c0") = ([0, 3, 1, 0], true) := by
  native_decide

/-- **α for every corner path of the study**: the research's `out/q9_alpha.tsv` has 1,060 paths (1 to 10 corner
subsets); for each, Lean's α_0 … α_N are the file's, N is the file's, and some arrangement follows the path. -/
theorem alpha_matches_study :
    parse.alphaRows.length = 1060 ∧
    parse.alphaRows.all (fun (p, n, al) => alphaOf HT (parsePath p) == (al, true) && al.length == n + 1) := by
  native_decide

end HTRRoutes
