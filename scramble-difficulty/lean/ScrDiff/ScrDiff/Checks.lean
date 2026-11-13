import ScrDiff.Cube

namespace ScrDiff
open cube

/-- axis of a face letter: 0 = R/L, 1 = U/D, 2 = F/B -/
def axisOf (c : Char) : Nat := (AX c).1

/-- DR on axis `a`: every sticker of an `a` colour is on an `a` face, and the four slice edges of axis `a`
    (home coordinate 0 on `a`) keep their colours of the next axis on that axis' faces.
    This set has 8!·8!·4!/2 states and contains <U,D,R2,L2,F2,B2> (for a = U/D), so it is that group. -/
def isDR (s : State) (a : Nat) : Bool :=
  (List.range 54).all fun i =>
    let h := s[i]!
    let col := axisOf (FACE_OF[h]!)
    let pl := axisOf (FACE_OF[i]!)
    let b := (a + 1) % 3
    (col != a || pl == a) && ((cube.ST[h]!).1[a]! != 0 || col != b || pl == b)

-- sanity: solved is DR on every axis; DR moves keep it; a quarter turn of another axis breaks it
theorem solved_dr : (isDR SOLVED 0 && isDR SOLVED 1 && isDR SOLVED 2) = true := by native_decide
theorem dr_moves_ud : isDR (do_ SOLVED "U R2 F2 D' L2 B2 U2 D") 1 = true := by native_decide
theorem r_breaks_ud : isDR (do_ SOLVED "R") 1 = false := by native_decide
theorem r_keeps_rl : isDR (do_ SOLVED "R U2 L' F2") 0 = true := by native_decide

/-- ColombianNationalsFMC2026 (2026-11-08): the text DR, normal F' U R D' R F U L U2 B' R2 F2 L2 F', inverse (R' U' F L') -/
theorem text_dr_recent : isDR (do_ SOLVED "L F' U R R' U' F L' D' U2 F2 L2 F2 U' F L2 F2 R2 B U2 L' U' F' R' D R' U' F F' U R D' R F U L U2 B' R2 F2 L2 F'") 1 = true := by native_decide
theorem text_dr_recent_scramble_not_dr : isDR (do_ SOLVED "R' U' F L' D' U2 F2 L2 F2 U' F L2 F2 R2 B U2 L' U' F' R' D R' U' F") 1 = false := by native_decide

/-- CrossstraitFMC2016 (2016-04-09): the text DR, normal F' U R D2 R' B L' D2 F' U D L' B' D, inverse (R' U' F) -/
theorem text_dr_old : isDR (do_ SOLVED "F' U R R' U' F L' U2 B2 R B2 L F2 L' F2 D' B L D' U' F D2 L B' R D2 R' U' F F' U R D2 R' B L' D2 F' U D L' B' D") 0 = true := by native_decide
theorem text_dr_old_scramble_not_dr : isDR (do_ SOLVED "R' U' F L' U2 B2 R B2 L F2 L' F2 D' B L D' U' F D2 L B' R D2 R' U' F") 0 = false := by native_decide

/-- easy example HawaiiChampionship2026: a 6-move DR with a 12-move finish -/
theorem easy_best_dr : isDR (do_ SOLVED "D' L' D L' U2 F' R' U' F R L2 F2 D2 B2 D B2 R2 D' R U2 B' U2 F' R D L U' F2 R' U' F") 2 = true := by native_decide
theorem easy_best_dr_scramble_not_dr : isDR (do_ SOLVED "R' U' F R L2 F2 D2 B2 D B2 R2 D' R U2 B' U2 F' R D L U' F2 R' U' F") 2 = false := by native_decide

/-- hard example FewestMovesBogota2025: DR 1 of 1 -/
theorem hard_dr_0 : isDR (do_ SOLVED "B' R' L2 B F2 U L2 B R' U' F L F' B2 L2 U2 F2 U B2 U' L2 D' R2 B2 R' D R2 B D' F' D R' U' F B' U") 0 = true := by native_decide
theorem hard_dr_0_scramble_not_dr : isDR (do_ SOLVED "R' U' F L F' B2 L2 U2 F2 U B2 U' L2 D' R2 B2 R' D R2 B D' F' D R' U' F") 0 = false := by native_decide

/-- w_zaki: DR 1 of 3 of at most 10 moves -/
theorem w_zaki_dr_0 : isDR (do_ SOLVED "L' B' R' U' F D B2 D B2 U' F2 L2 U2 F2 R2 D' F2 L' F' R' F D F L2 D R' U' F B' D' R U' D F R2 U") 2 = true := by native_decide
theorem w_zaki_dr_0_scramble_not_dr : isDR (do_ SOLVED "R' U' F D B2 D B2 U' F2 L2 U2 F2 R2 D' F2 L' F' R' F D F L2 D R' U' F") 2 = false := by native_decide

/-- w_zaki: DR 2 of 3 of at most 10 moves -/
theorem w_zaki_dr_1 : isDR (do_ SOLVED "L' B' R' U' F D B2 D B2 U' F2 L2 U2 F2 R2 D' F2 L' F' R' F D F L2 D R' U' F B' D' R' U' D F' L2 D") 2 = true := by native_decide
theorem w_zaki_dr_1_scramble_not_dr : isDR (do_ SOLVED "R' U' F D B2 D B2 U' F2 L2 U2 F2 R2 D' F2 L' F' R' F D F L2 D R' U' F") 2 = false := by native_decide

/-- w_zaki: DR 3 of 3 of at most 10 moves -/
theorem w_zaki_dr_2 : isDR (do_ SOLVED "L' U' L2 D R' B' D2 F R' U' F D B2 D B2 U' F2 L2 U2 F2 R2 D' F2 L' F' R' F D F L2 D R' U' F L2 B") 1 = true := by native_decide
theorem w_zaki_dr_2_scramble_not_dr : isDR (do_ SOLVED "R' U' F D B2 D B2 U' F2 L2 U2 F2 R2 D' F2 L' F' R' F D F L2 D R' U' F") 1 = false := by native_decide

/-- w_jtuuu: DR 1 of 2 of at most 10 moves -/
theorem w_jtuuu_dr_0 : isDR (do_ SOLVED "R' U' F D2 B2 D2 F2 D F2 U' R2 F2 L2 U2 F D2 R' B U F2 R D' R D2 R' U' F U2 R B' D' F L R' U' L' D") 0 = true := by native_decide
theorem w_jtuuu_dr_0_scramble_not_dr : isDR (do_ SOLVED "R' U' F D2 B2 D2 F2 D F2 U' R2 F2 L2 U2 F D2 R' B U F2 R D' R D2 R' U' F") 0 = false := by native_decide

/-- w_jtuuu: DR 2 of 2 of at most 10 moves -/
theorem w_jtuuu_dr_1 : isDR (do_ SOLVED "R' U' F D2 B2 D2 F2 D F2 U' R2 F2 L2 U2 F D2 R' B U F2 R D' R D2 R' U' F U2 R B' D' F L' R D' L' U") 0 = true := by native_decide
theorem w_jtuuu_dr_1_scramble_not_dr : isDR (do_ SOLVED "R' U' F D2 B2 D2 F2 D F2 U' R2 F2 L2 U2 F D2 R' B U F2 R D' R D2 R' U' F") 0 = false := by native_decide

/-- short text, easy: ColomboCubingChristmas2023 -/
theorem short_text_easy : isDR (do_ SOLVED "B' L' B2 D2 F U2 R2 F D' R' U' F L F2 D2 R' B2 F2 R' B2 D R F2 R' D L B' R' U' F D") 0 = true := by native_decide
theorem short_text_easy_scramble_not_dr : isDR (do_ SOLVED "R' U' F L F2 D2 R' B2 F2 R' B2 D R F2 R' D L B' R' U' F") 0 = false := by native_decide

/-- 10/8/8 with a short EO: Juhannus2024 -/
theorem ten_eight_eight_short_eo : isDR (do_ SOLVED "F' R' L' B' D2 R' D U B2 L' R' U' F R2 F' U2 R D B2 L D' F2 R F2 U' R2 B2 U' R2 D2 F2 B R' U' F") 0 = true := by native_decide
theorem ten_eight_eight_short_eo_scramble_not_dr : isDR (do_ SOLVED "R' U' F R2 F' U2 R D B2 L D' F2 R F2 U' R2 B2 U' R2 D2 F2 B R' U' F") 0 = false := by native_decide

/-- many 4-move EOs, best 22: EstonianOpen2019 -/
theorem many_four_movers_22 : isDR (do_ SOLVED "U' F2 R' R' U' F D2 F2 D B2 F2 D B2 D L2 F2 R' B L2 R2 B2 D2 L F R2 F R' U' F B' D2 L2 R2 B R") 2 = true := by native_decide
theorem many_four_movers_22_scramble_not_dr : isDR (do_ SOLVED "R' U' F D2 F2 D B2 F2 D B2 D L2 F2 R' B L2 R2 B2 D2 L F R2 F R' U' F") 2 = false := by native_decide

/-- ColombianNationalsFMC2026: the official middle and the first solution min2phase finds (inverted) make the same state -/
theorem first_solution_same_state : (do_ SOLVED "L' D' U2 F2 L2 F2 U' F L2 F2 R2 B U2 L' U' F' R' D" == do_ SOLVED "R D' R2 D L2 F2 U' B2 R2 U2 B2 F L2 D2 F R U' F' L' D2") = true := by native_decide
theorem first_solution_same_state_not_solved : (do_ SOLVED "L' D' U2 F2 L2 F2 U' F L2 F2 R2 B U2 L' U' F' R' D" == SOLVED) = false := by native_decide

end ScrDiff
