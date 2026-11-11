/-
  DRXs.Theorems — the checked statements A to E.  Every one is a closed statement about the definitions in
  Cube / Fe / Fecosets / Festeps, proved by running them: `native_decide` evaluates the statement with compiled
  code and accepts the answer (this trusts the Lean compiler; see README.md).

  Reading aid:  `hist l`  is `sorted(Counter(l).items())`: the list of (value, how many times it occurs in l).
                `∀ x ∈ l, P x`  is "P holds for every x in the list l".
-/
import DRXs.Festeps
import DRXs.Invariant
import DRXs.PyMoves

namespace DRXs
open cube fecosets festeps invariant

-- The checks run compiled code; Lean's default time-out for elaborating one statement does not fit them.
set_option maxHeartbeats 0

/-! ## A. The model is a cube -/

/-- There are 54 stickers, all different, and 18 face turns with these names. -/
theorem model_size :
    cube.ST.size = 54 ∧ cube.ST.toList.eraseDups.length = 54 ∧
    NAMES = ["U", "U2", "U'", "D", "D2", "D'", "R", "R2", "R'", "L", "L2", "L'", "F", "F2", "F'", "B", "B2", "B'"] := by
  native_decide

/-- Each of the 18 face-turn maps is a permutation of the 54 places. -/
theorem moves_are_permutations : ∀ name ∈ NAMES, is_permutation (MOVES name) = true := by native_decide

/-- U⁴ = F⁴ = R⁴ = identity. -/
theorem quarter_turn_four_times :
    do_ SOLVED "U U U U" = SOLVED ∧ do_ SOLVED "F F F F" = SOLVED ∧ do_ SOLVED "R R R R" = SOLVED := by
  native_decide

/-- Every face has order exactly 4; X2 is X done twice, X' is X done three times. -/
theorem turns_of_a_face : ∀ X ∈ ["U", "D", "R", "L", "F", "B"],
    order X = 4 ∧
    do_ SOLVED (X ++ "2") = do_ SOLVED (X ++ " " ++ X) ∧
    do_ SOLVED (X ++ "'") = do_ SOLVED (X ++ " " ++ X ++ " " ++ X) := by native_decide

/-- (R U R' U')⁶ = identity, and no smaller power is. -/
theorem sexy_move_order : order "R U R' U'" = 6 := by native_decide

/-- The sequence R U has order 105. -/
theorem RU_order : order "R U" = 105 := by native_decide

/-- R U2 D' B D' has order 1260 (another of cube.py's self-tests). -/
theorem order_1260 : order "R U2 D' B D'" = 1260 := by native_decide

/-- Turning sense (the first three asserts of cube.py): U clockwise from above carries the U-sticker of UFR to
UFL; R carries it to UBR, where it faces B; F carries it to DFR, where it faces R. -/
theorem turn_directions :
    IDX ([1, 1, 1], [0, 1, 0]) < 54 ∧
    (MOVES "U")[IDX ([1, 1, 1], [0, 1, 0])]! = IDX ([-1, 1, 1], [0, 1, 0]) ∧
    (MOVES "R")[IDX ([1, 1, 1], [0, 1, 0])]! = IDX ([1, 1, -1], [0, 0, -1]) ∧
    (MOVES "F")[IDX ([1, 1, 1], [0, 1, 0])]! = IDX ([1, -1, 1], [1, 0, 0]) := by native_decide

/-- The 18 permutations built here from geometry are, number for number, the ones cube.py builds
(`PY_MOVES`, written out by gen_moves.py). -/
theorem moves_agree_with_python : MOVES_TABLE = PY_MOVES := by native_decide

/-! ## B. Kinds -/

/-- A kind has 29 allowed groups of turns, and every move name in them is one of the 18. -/
theorem gens_well_formed : ∀ f ∈ [0, 1, 2],
    (fe.gens f).length = 29 ∧ ∀ g ∈ fe.gens f, ∀ name ∈ parse g.2.1, name ∈ NAMES := by native_decide

/-- No assert of the walk fails: every state met looks like a DR-xs on the expected faces, and the 20000 times
a signature reached again through another state was compared, the groups tried led to the same signatures. -/
theorem explore_asserts_hold : explored.failed = 0 ∧ explored.checked = 20000 := by native_decide

/-- Starting from the solved cube and closing under the allowed groups, exactly 768 signatures are reached. -/
theorem kinds_count : kinds.length = 768 ∧ kinds.eraseDups.length = 768 := by native_decide

/-- The 768 are closed: each has its 29 groups, and every group leads to one of the 768
(`e.2.2.2.2` is the last entry of the tuple e = (axis, text, cost, slices, kind it leads to)). -/
theorem kinds_closed : ∀ g ∈ kinds,
    (nbr.getD g []).length = 29 ∧ ∀ e ∈ nbr.getD g [], e.2.2.2.2 ∈ kinds := by native_decide

/-- 256 kinds for each face axis (0 = R/L, 1 = U/D, 2 = F/B). -/
theorem kinds_by_face_axis : hist (kinds.map (·.f)) = [(0, 256), (1, 256), (2, 256)] := by native_decide

/-- The walk starts at the real DR, and it is the only real DR among the kinds. -/
theorem one_real_dr :
    explored.start = ⟨1, [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1]⟩ ∧ kinds.filter is_dr = [explored.start] := by
  native_decide

/-- A face turn carries corner places to corner places and edge places to edge places (24 of each). -/
theorem moves_keep_corners_and_edges :
    corner_places.length = 24 ∧ edge_places.length = 24 ∧
    ∀ name ∈ NAMES, (∀ i ∈ corner_places, (MOVES name)[i]! ∈ corner_places) ∧
                    (∀ i ∈ edge_places, (MOVES name)[i]! ∈ edge_places) := by native_decide

/-- The signature is a complete invariant, for every reachable state (see DRXs/Invariant.lean for why these
two walks cover every state): walking all reachable (face axis, colours at the corner places) and all reachable
(face axis, colours at the edge places), 210 and 53760 of them, every state has a signature, it is one of the
768 kinds, and every group leads to the signature `nbr` records.  No check fails. -/
theorem signature_is_complete_invariant :
    walk corner_places = (210, 0) ∧ walk edge_places = (53760, 0) := by native_decide

/-- Fewest slices to a real DR: 1 kind needs 0, 140 need 1, 383 need 2, 244 need 3. -/
theorem slices_hist : hist (kinds.map slices) = [(0, 1), (1, 140), (2, 383), (3, 244)] := by native_decide

/-! ## C. DR-1s to DR -/

/-- Over the 140 kinds one slice away: fewest face turns to a real DR are 2 for 2 kinds, 3 for 4, 4 for 18,
5 for 60, 6 for 56. -/
theorem dr1s_turns_hist :
    hist ((kinds_with_slices 1).map turns_to_dr) = [(2, 2), (3, 4), (4, 18), (5, 60), (6, 56)] := by native_decide

/-- In particular no DR-1s needs 7 turns. -/
theorem dr1s_turns_le_6 : ∀ g ∈ kinds_with_slices 1, turns_to_dr g ≤ 6 := by native_decide

/-! ## D. DR-2s and DR-3s to DR -/

/-- Over the 383 kinds two slices away: fewest face turns to a real DR are 4 for 2 kinds, 5 for 32, 6 for 99,
7 for 172, 8 for 54, 9 for 24. -/
theorem dr2s_turns_hist :
    hist ((kinds_with_slices 2).map turns_to_dr) = [(4, 2), (5, 32), (6, 99), (7, 172), (8, 54), (9, 24)] := by
  native_decide

/-- Over the 244 kinds three slices away: 6 for 2 kinds, 7 for 14, 8 for 118, 9 for 80, 10 for 30. -/
theorem dr3s_turns_hist :
    hist ((kinds_with_slices 3).map turns_to_dr) = [(6, 2), (7, 14), (8, 118), (9, 80), (10, 30)] := by
  native_decide

/-! ## E. Steps -/

/-- From every one of the 244 DR-3s kinds, a kind that needs at most 2 slices is reached in exactly 2 face
turns. -/
theorem dr3s_to_2s_hist : hist ((kinds_with_slices 3).map turns_to_2s) = [(2, 244)] := by native_decide

/-- From the 383 DR-2s kinds, a kind that needs at most 1 slice is reached in 2 turns (209 kinds), 3 (102)
or 4 (72). -/
theorem dr2s_to_1s_hist :
    hist ((kinds_with_slices 2).map turns_to_1s) = [(2, 209), (3, 102), (4, 72)] := by native_decide

/-! ## The four tables satisfy their rule -/

/-- Every entry of each table equals what the rule gives from the table itself:
d(g, last) = 0 if g is in the target, else the least weight + d(h, a) over the groups of g about an axis a ≠ last. -/
theorem tables_satisfy_rule :
    satisfies_rule nbr is_dr (fun _cost sl => sl) dsl = true ∧
    satisfies_rule nbr is_dr (fun cost _sl => cost) dmv = true ∧
    satisfies_rule nbr (fun g => slices g <= 1) (fun cost _sl => cost) to1 = true ∧
    satisfies_rule nbr (fun g => slices g <= 2) (fun cost _sl => cost) to2 = true := by native_decide

/-- festeps' `to0` (target: the kinds that need 0 slices) is the same table as fecosets' `dmv` (target: real DR). -/
theorem to0_is_dmv : ∀ g ∈ kinds, ∀ last ∈ [0, 1, 2, 3], to0.getD (g, last) INF = dmv.getD (g, last) INF := by
  native_decide

end DRXs
