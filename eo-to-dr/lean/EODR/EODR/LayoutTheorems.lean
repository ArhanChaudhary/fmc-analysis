/-
  EODR.LayoutTheorems — checked statements, part C (see README.md).  Every one is a closed statement about the definitions in Cube / Pieces /
  Search / Eo / Layouts / Eodr, proved by running them: `native_decide` evaluates the statement with compiled code
  and accepts the answer (this trusts the Lean compiler; see README.md).  Statements that are plain arithmetic on
  numbers are proved by `decide` (Lean's kernel alone).

  Axes: 0 = R/L, 1 = U/D, 2 = F/B.  Moves: indices into NAMES = U U2 U' D D2 D' R R2 R' L L2 L' F F2 F' B B2 B'.
  Reading aid:  `hist l` = list of (value, how many times it occurs in l), by value.
-/
import EODR.Eo
import EODR.Layouts
import EODR.Eodr
import EODR.Parse

namespace EODR
open cube pieces

set_option maxHeartbeats 0

/-! ## C. Bad-edge layouts -/

/-- The three facts about `badAt` that the count rests on (all axes, places, pieces, orientations). -/
theorem badAt_rules :
    ((List.range 12).all fun k => (List.range 12).all fun p => (List.range 2).all fun o =>
        layouts.badAt 2 k p o == (o == 1)) ∧
    ((List.range 3).all fun Y => (List.range 12).all fun k => (List.range 12).all fun p =>
        layouts.badAt Y k p 1 == !layouts.badAt Y k p 0) ∧
    ((List.range 3).all fun Y => (List.range 12).all fun k => (List.range 12).all fun p =>
        (List.range 12).all fun q => kind p != kind q ||
          (layouts.badAt Y k p 0 == layouts.badAt Y k q 0 && layouts.badAt Y k p 1 == layouts.badAt Y k q 1)) ∧
    (List.range 3).all (fun t => kind (layouts.rep t) == t) := by
  native_decide

theorem arrangements_count : layouts.arrangements.length = 34650 ∧ 34650 * 2048 = 70963200 := by native_decide

/-- The count runs over 70,963,200 configurations, and its table of (bad F/B, bad R/L, bad U/D) triples with their
numbers of configurations is, row for row, the research's `eo_layouts.tsv`. -/
theorem layouts_matches_study :
    layouts.count 34650 = (parse.layoutRows, 70963200) := by native_decide

/-- Readings of that table, read off the research's rows (equal to Lean's by `layouts_matches_study`). -/
theorem layout_facts :
    let t := parse.layoutRows
    layouts.total t = 70963200 ∧
    -- 12/12/12: 1 configuration
    layouts.countIf t (fun a b c => a == 12 && b == 12 && c == 12) = 1 ∧
    -- some axis already EO'd (S-EO-67)
    layouts.countIf t (fun a b c => a == 0 || b == 0 || c == 0) = 103741 ∧
    -- every axis in {0, 2, 4, 8} (S-EO-44)
    layouts.countIf t (fun a b c => [a, b, c].all fun x => [0, 2, 4, 8].contains x) = 9868829 ∧
    -- sorted triples (S-EO-41, 43, 45)
    layouts.sortedCount t 4 6 6 = 10465584 ∧ layouts.sortedCount t 6 6 6 = 6527128 ∧
    layouts.sortedCount t 6 6 8 = 10465584 ∧ layouts.sortedCount t 0 0 2 = 48 ∧
    layouts.sortedCount t 0 0 8 = 3 ∧ layouts.sortedCount t 2 10 10 = 1098 ∧
    layouts.sortedCount t 10 10 10 = 12602 ∧
    -- the sum of the three counts (S-EO-39): peak at 18
    layouts.sumHist t = [(0, 1), (2, 48), (4, 1116), (6, 18986), (8, 168903), (10, 925164), (12, 3373795),
      (14, 8313066), (16, 14191449), (18, 16978144), (20, 14191449), (22, 8313066), (24, 3373795), (26, 925164),
      (28, 168903), (30, 18986), (32, 1116), (34, 48), (36, 1)] ∧
    -- two axes never differ by more than 8, and 8 occurs (S-EO-45)
    (layouts.triples t).all (fun (a, b, c) => [a, b, c].all fun x => [a, b, c].all fun y => x ≤ y + 8) ∧
    (layouts.triples t).any (fun (a, b, _) => a == b + 8) ∧
    -- 12 bad on one axis leaves at least 4 on each other axis, and 4 occurs (S-EO-46)
    (layouts.triples t).all (fun (a, b, c) => [a, b, c].all fun x => [a, b, c].all fun y => x != 12 || y ≥ 4) ∧
    (layouts.triples t).any (fun (a, b, _) => a == 12 && b == 4) ∧
    -- with 0 bad on one axis, each other axis has 0, 2, 4, 6 or 8 bad, and each of these occurs (S-EO-47)
    (layouts.triples t).all (fun (a, b, c) => [a, b, c].all fun x => [a, b, c].all fun y =>
      x != 0 || [0, 2, 4, 6, 8].contains y) ∧
    ([0, 2, 4, 6, 8].all fun y => (layouts.triples t).any fun (a, b, _) => a == 0 && b == y) := by
  native_decide

/-- The shares, as digits (integer division, so the last digit is cut, not rounded):
9868829/70963200 = 13.906967…%, 103741/70963200 = 0.146189(6…)% (the study rounds to 0.146190%),
16978144/70963200 = 23.9252(7…)% (rounded 23.9253%, torchlight's 23.93%), sorted 4/6/6 = 14.747903…%,
sorted 6/6/6 = 9.197905…%. -/
theorem layout_share_digits :
    9868829 * 100000000 / 70963200 = 13906967 ∧ 103741 * 100000000 / 70963200 = 146189 ∧
    16978144 * 1000000 / 70963200 = 239252 ∧ 10465584 * 100000000 / 70963200 = 14747903 ∧
    6527128 * 100000000 / 70963200 = 9197905 := by
  decide

end EODR
