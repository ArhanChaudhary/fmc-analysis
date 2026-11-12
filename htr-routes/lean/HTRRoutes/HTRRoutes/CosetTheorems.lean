/-
  HTRRoutes.CosetTheorems — checked statements, part D: the 48 subsets and the labels of the docs' examples (see
  README.md).  `native_decide` runs the statement as compiled code.
-/
import HTRRoutes.Cosets
import HTRRoutes.Parse

namespace HTRRoutes
open pieces corners

set_option maxHeartbeats 0

/-! ## D. HTR cosets, the 48 subsets, and the 2qt a/b labels -/

/-- The move action on (corner coset, edge pattern) is well defined (the same for every arrangement of a coset);
the BFS over the HTR cosets passes `search.ruleHolds` (each entry is the shortest linear DR → HTR of the coset),
it reaches 29,400 = 420 × 70 cosets, and its table of (48-subset, shortest HTR, cosets) is, row for row, the
research's `out/checks/htr48.tsv` (161 rows). -/
theorem htr48_matches_study :
    cosets.cosetActionOk = true ∧ cosets.run = ⟨true, 29400, parse.htr48⟩ := by native_decide

/-- Readings of that table: 48 subset names; the shortest linear HTR of each subset (the smallest length of any of
its cosets) is ≤ 4 for 5 subsets, ≤ 5 for 9, ≤ 6 for 12 (claim C08: Jay's "8 cases in ≤ 5" is 9), and the 9 with
≤ 5 are those listed; the research's row C08 says the same. -/
theorem htr48_facts :
    let names := (parse.htr48.map (·.1)).eraseDups
    let shortest := fun (s : String) =>
      ((parse.htr48.filter (·.1 == s)).map (·.2.1)).foldl min 99
    names.length = 48 ∧
    (names.filter fun s => shortest s ≤ 4).length = 5 ∧
    (names.filter fun s => shortest s ≤ 5).length = 9 ∧
    (names.filter fun s => shortest s ≤ 6).length = 12 ∧
    ((names.filter fun s => shortest s ≤ 5).mergeSort fun a b => decide (a < b)) =
      ["0c0 0e", "0c0 2e", "0c0 4e", "2c3 2e", "2c3 4e", "4a1 4e", "4a2 4e", "4b2 2e", "4b2 4e"] ∧
    parse.says study.CLAIM_C08 "5 subsets <= 4, 9 <= 5, 12 <= 6" ∧
    parse.says study.CLAIM_C08
      "<=5: 0c0 0e, 0c0 2e, 0c0 4e, 4a2 4e, 4a1 4e, 2c3 2e, 2c3 4e, 4b2 2e, 4b2 4e" := by
  native_decide

/-- **The docs' example scrambles** (`out/name_map.tsv`, 95 rows from docs 15 and 66): each scramble, done on the
sticker model, gives the research's 48-subset, label, and label of the inverse. -/
theorem name_map_matches_study :
    parse.nameRows.length = 95 ∧
    parse.nameRows.all fun (_, _, ex, o, n, i) => cosets.scrambleLabels ex == (o, n, i) := by
  native_decide

/-- **2qt a/b**: doc 15's "2qt (a)" examples are 4b2 and its "2qt (b)" examples 4a2; doc 66 uses the letters the
other way round ("2qt(a)" = 4a2, "2qt(b)" = 4b2).  (Read off the research's rows, equal to Lean's labels by
`name_map_matches_study`.) -/
theorem two_qt_letters :
    let rows := fun (doc pre : String) =>
      (parse.nameRows.filter fun r => r.1 == doc && r.2.1.startsWith pre).map (·.2.2.2.1)
    rows "doc15" "2qt (a)" = ["4b2 0e", "4b2 2e", "4b2 4e"] ∧
    rows "doc15" "2qt (b)" = ["4a2 0e", "4a2 2e", "4a2 4e"] ∧
    rows "doc66" "2qt(a)" = ["4a2 0e", "4a2 2e", "4a2 4e"] ∧
    rows "doc66" "2qt(b)" = ["4b2 0e", "4b2 2e", "4b2 4e"] := by
  native_decide

end HTRRoutes
