/-
  Corners3D.Theorems — the checks, run.  Every theorem here is a computation closed with `native_decide`
  (the compiled code is trusted, as in the project's other certificates).  `Proofs.lean` turns the ones written
  with `allBelow` into statements about every sequence of turns, by induction.
-/
import Corners3D.Checks
namespace Corners3D
open cube pieces corners checks

/-! ### A. The model -/

/-- Each of the nine turns (R, U, F faces) carries each corner's sticker list onto its destination's, shifted
cyclically, turns the corners by 0 mod 3 in total and leaves DBL alone; the coordinate maps are bijections. -/
theorem model_ok : modelOK () = true := by native_decide

/-- On all 820 sticker states within 3 turns of solved (with repeats) and for each of the nine turns, the
coordinate after the turn, read off the stickers, is `step` of the coordinate before it. -/
theorem coords_follow_stickers : nearCount () = 820 ∧ coordsOK () = true := by native_decide

/-- `CORD` lists the faces of a corner counter-clockwise seen from outside, starting with the U/D face.  So a
twist of 2 in `Pieces.lean` is "U/D sticker one step clockwise", the study's "twisted clockwise". -/
theorem cord_is_counterclockwise : cordCCW () = true := by native_decide

/-- The places UFR UFL UBR DFR UBL DFL DBR, as (x, y, z) with x = +1 on R, y = +1 on U, z = +1 on F: the
names the kinds are written under are the right ones. -/
theorem place_names_ok :
    PLACE_ORDER.map (fun c => CORNERS[c]!) =
      [[1, 1, 1], [-1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, -1], [-1, -1, 1], [1, -1, -1]] ∧
    PLACE_NAMES.length = 7 := by native_decide

/-- The table of turns from solved is exact, so every one of the 3,674,160 coordinates is a state R, U, F
turns reach; and it is the known 2x2x2 table (God's number 11). -/
theorem all_reached :
    exactOK fSolved isSolved () = true ∧
    search.hist dSolved = [1, 9, 54, 321, 1847, 9992, 50136, 227536, 870072, 1887748, 623800, 2644] := by
  native_decide

/-! ### B. What a corner shows -/

/-- The sticker states within 3 turns show all 148 combinations of (place, piece, twist) that exist (7 × 7 × 3
for the free corners, and DBL).  On them, a corner in its own tetrad has all three stickers on faces of their
own axis, or none; a corner in the other tetrad has exactly one; and the kind worked out from the coordinates
is the kind the stickers show.  A corner's stickers depend only on its place, piece and twist, so this holds
in every state. -/
theorem tetrad_theorem : coverCount () = 148 ∧ tetradOK () = true := by native_decide

/-- What a turn does to a kind, in words (see `ruleWords`), and that a turn moves exactly the four corners of
its face. -/
theorem rule_in_words : ruleWords () = true ∧ faceOK () = true := by native_decide

/-- The rule as a table.  Kinds: 0 good, 1 twisted cw, 2 twisted ccw, 3 / 4 / 5 out with the R/L / U/D / F/B
sticker oriented.  Each row lists what kinds 0 … 5 become when a quarter turn (either direction) moves the corner;
rows: R (corner at UFR or DBR), R (at UBR or DFR), U (at UFR or UBL), U (at UFL or UBR), F (at UFR or DFL),
F (at UFL or DFR).  The place matters only through its tetrad, and only for which of the two twists pairs with
which of the two other out kinds. -/
theorem rule_table :
    ruleTable () = [[3, 5, 4, 0, 1, 2], [3, 4, 5, 0, 2, 1], [4, 3, 5, 2, 0, 1], [4, 5, 3, 1, 0, 2],
                    [5, 4, 3, 1, 2, 0], [5, 3, 4, 2, 1, 0]] := by native_decide

/-- No turn leaves the coordinates. -/
theorem closed_ok : closedOK () = true := by native_decide

/-- Each turn is undone by its inverse turn, on every state. -/
theorem inv_ok : invOK () = true := by native_decide

/-- For every state and every turn, the kinds after the turn are `kindStep` of the kinds before: the kinds
change by a rule that looks at nothing but the kinds. -/
theorem quarter_rule : ruleOK () = true := by native_decide

/-! ### C. Goal sets -/

/-- HTR has 24 states; it contains solved, is closed under the half turns, and each of its states goes back to
solved by half turns.  So HTR is exactly the states half turns reach. -/
theorem goal_HTR :
    HTR.length = 24 ∧ inHTR SOLVEDX = true ∧
    HTR.all (fun x => HALF.all fun m => inHTR (step x m)) = true ∧
    HTR.all (fun x => x == SOLVEDX || HALF.any fun m =>
      inHTR (step x m) && (dh.get! (step x m)).toNat + 1 == (dh.get! x).toNat) = true := by
  native_decide

/-- 144 states have every corner good; 24 of them are HTR (and every HTR state is one of them); 72 have an even
placement. -/
theorem good_counts :
    GOOD.length = 144 ∧ (GOOD.filter inHTR).length = 24 ∧ HTR.all allGood = true ∧ GOODEVEN.length = 72 ∧
    HTR.all goodEven = true := by
  native_decide

/-! ### D. Exact tables -/

/-- `dHTR` is 0 exactly on HTR, no turn lowers it by more than 1, and off HTR some turn lowers it by 1
(`exactOK`; `Proofs.dHTR_exact` draws the conclusion). -/
theorem dHTR_check : exactOK fHTR inHTR () = true := by native_decide

/-- 0 … 10 turns to HTR.  God's number for these corners to HTR is 10. -/
theorem dHTR_hist :
    search.hist dHTR = [24, 72, 432, 2304, 13464, 65496, 296400, 1077072, 1813680, 401472, 3744] := by
  native_decide

/-- `qHTR` is exactly the fewest quarter turns to HTR over all solutions, half turns free (`search.qtRule`). -/
theorem qHTR_exact : search.qtRule N inHTR ALL w step qHTR = true := by native_decide

/-- 0 … 8 quarter turns: the table jules_porteners posted for the 2x2x2.  The maximum is 8 (384 states). -/
theorem qHTR_hist :
    search.hist qHTR = [24, 432, 6768, 86184, 780048, 1708416, 1049856, 42048, 384] := by native_decide

/-- Turns to "every corner good" (triple DR), exact, with its histogram: at most 9. -/
theorem dGood_check : exactOK fGood allGood () = true := by native_decide
theorem dGood_hist :
    search.hist dGood = [144, 432, 2592, 13824, 80784, 378720, 1304928, 1692288, 198144, 2304] := by
  native_decide

/-- Turns to "every corner good, even placement", exact, with its histogram. -/
theorem dGoodEven_check : exactOK fGoodEven goodEven () = true := by native_decide
theorem dGoodEven_hist :
    search.hist dGoodEven = [72, 216, 1296, 6912, 40392, 193032, 751824, 1793520, 856008, 30888] := by
  native_decide

/-- The same two in quarter turns (half turns free), exact (`search.qtRule`), with their histograms. -/
theorem qGood_exact : search.qtRule N allGood ALL w step qGood = true := by native_decide
theorem qGood_hist : search.hist qGood = [144, 2592, 32832, 368064, 2257920, 993024, 19584] := by native_decide
theorem qGoodEven_exact : search.qtRule N goodEven ALL w step qGoodEven = true := by native_decide
theorem qGoodEven_hist :
    search.hist qGoodEven = [72, 1296, 17712, 200520, 1312992, 1625472, 506304, 9792] := by native_decide

/-- Placements only (twists ignored), all nine turns: turns and quarter turns to an HTR placement, exact. -/
theorem perm_tables :
    HTRP.length = 24 ∧
    search.distRule NCP inHTRP ALL pstep dPerm = true ∧ search.qtRule NCP inHTRP ALL w pstep qPerm = true ∧
    search.hist dPerm = [24, 72, 360, 1128, 1440, 1776, 240] ∧
    search.hist qPerm = [24, 144, 720, 1416, 1776, 960] := by
  native_decide

/-! ### E. Floors: the local conditions (the conclusions are in `Proofs.lean`) -/

/-- The types floor: `dGood` is 0 on HTR and no turn lowers it by more than 1. -/
theorem types_floor_check : floorOK fGood inHTR () = true := by native_decide
/-- The parity floor: the same for `dGoodEven`. -/
theorem parity_floor_check : floorOK fGoodEven inHTR () = true := by native_decide
/-- The placement floor: the same for the placement-only table. -/
theorem placement_floor_check : floorOK fPerm inHTR () = true := by native_decide
/-- The weight floor: the weight (out corners + 2 × twisted corners) is 0 on HTR, a half turn keeps it and a
quarter turn lowers it by at most 4. -/
theorem weight_floor_check : wfloorOK weight 4 inHTR () = true := by native_decide
/-- Quarter-turn floors: each of these is 0 on HTR, kept by half turns, lowered by at most 1 by a quarter turn. -/
theorem quarter_floor_checks :
    wfloorOK gHTR 1 inHTR () = true ∧ wfloorOK gGood 1 inHTR () = true ∧ wfloorOK gGoodEven 1 inHTR () = true ∧
    wfloorOK gPerm 1 inHTR () = true := by
  native_decide

/-- How far each floor is below the truth, in turns: number of states at gap 0, 1, 2, …
The types floor is exact on 1,134,744 states (30.9%), the parity floor on 1,977,024 (53.8%). -/
theorem floor_gaps :
    gapHist fHTR fGood () = [1134744, 1284552, 854736, 300576, 78336, 16128, 3888, 864, 216, 120] ∧
    gapHist fHTR fGoodEven () = [1977024, 1079952, 464448, 107904, 34704, 7632, 1872, 504, 72, 48] ∧
    gapHist fHTR fPerm () = [24480, 140064, 542976, 1106424, 1054992, 575304, 170400, 43488, 13440, 1440, 1152] := by
  native_decide

/-- The same in quarter turns.  The last line is the surcharge over the placement count (levitatingmagician's
quarter-turn count of a scrambled cube): always even, 0 on 1,274,064 states (34.7%). -/
theorem quarter_floor_gaps :
    gapHist gHTR gGood () = [1220712, 1749744, 616320, 87336, 48] ∧
    gapHist gHTR gGoodEven () = [2970528, 0, 703584, 0, 48] ∧
    gapHist gHTR gPerm () = [1274064, 0, 2019456, 0, 360864, 0, 19392, 0, 384] := by
  native_decide

/-- Each floor is at most the truth on every state: the three floors in turns, the three in quarter turns, and
the weight against four times the fewest quarter turns.  So the histograms above count real gaps. -/
theorem floors_below : floorsBelow () = true := by native_decide

/-- The surcharge over levitatingmagician's count: fewest quarter turns minus the placement-only count is 0 for
1,274,064 states, 2 for 2,019,456, 4 for 360,864, 6 for 19,392 and 8 for 384.  It is never odd. -/
theorem qt_surcharge : gapHist gHTR gPerm () = [1274064, 0, 2019456, 0, 360864, 0, 19392, 0, 384] := by
  native_decide

/-- The weight of a state: how many states have weight 0, 1, …, 14. -/
theorem weight_hist :
    histOf weight N = [144, 0, 5184, 0, 127872, 0, 777312, 0, 1564704, 0, 1004832, 0, 188064, 0, 6048] := by
  native_decide

/-! ### F. Fake HTR -/

/-- Of the 144 all-good states, the 120 outside HTR are each exactly 9 turns from HTR.  72 of them (the odd
placements) need 3 quarter turns and 48 (even) need 4. -/
theorem fake_htr_far : fakeOK () = true := by native_decide

/-! ### G. The colour read -/

/-- The D-coloured corners show six pictures in HTR.  Next to DBL, the other three D-coloured corners sit at:
the rest of the D face; the rest of the L face; the rest of the B face; or one more corner of DBL's tetrad
(UBR, UFL or DFR) and the two corners of the other tetrad that share a face with each other parallel to the
face that corner shares with DBL (UFR + DFL, UFR + UBL, UFR + DBR). -/
theorem six_pictures :
    SIX.length = 6 ∧
    SIX.map pictureNames = [["DFR", "DFL", "DBR"], ["UFR", "UBR", "DFL"], ["UFL", "UBL", "DFL"],
      ["UBR", "UBL", "DBR"], ["UFR", "DFR", "UBL"], ["UFR", "UFL", "DBR"]] := by native_decide

/-- For every state: HTR ⇔ every corner good ∧ the D-coloured corners in one of the six pictures ∧ even
placement (`Proofs.htr_iff` states it as an equivalence). -/
theorem htr_iff_check : htrIffOK () = true := by native_decide

/-- States with the same kinds, the same D-colour picture and the same parity are equally far from HTR, in
turns and in quarter turns. -/
theorem three_reads_fix_distance : threeReadsOK () = true := by native_decide

/-- The kinds, the D-colour picture and the B-colour picture together determine the state. -/
theorem types_and_two_colours_fix_state : twoColoursOK () = true := by native_decide

/-- 25,515 kinds patterns occur, each shown by exactly 144 states, 72 even and 72 odd. -/
theorem types_class_size : classSizes () = (25515, true) ∧ classParity () = true := by native_decide

/-! ### H. DR inside 3D -/

/-- The oriented states: for each axis and each placement, the one state with that placement whose corners are
all oriented on that axis (for U/D: every twist 0). -/
theorem oriented_ok : orientedOK () = true := by native_decide

/-- DR turns only, for each axis: turns and quarter turns to HTR over the 5,040 placements, exact.  The
DR-only maximum is 11 turns and 5 quarter turns. -/
theorem dr_tables :
    drTablesOK () = true ∧
    (List.range 3).map (fun a => search.hist dDR[a]!) =
      [[24, 24, 48, 144, 216, 600, 528, 624, 816, 1152, 624, 240],
       [24, 24, 48, 144, 216, 600, 528, 624, 816, 1152, 624, 240],
       [24, 24, 48, 144, 216, 600, 528, 624, 816, 1152, 624, 240]] ∧
    (List.range 3).map (fun a => search.hist qDR[a]!) =
      [[24, 144, 720, 1416, 1776, 960], [24, 144, 720, 1416, 1776, 960], [24, 144, 720, 1416, 1776, 960]] := by
  native_decide

/-- On a state oriented on an axis, quarter turns of the other two faces never save a quarter turn: the HTR
subset number is the same with all nine turns. -/
theorem dr_qt_same : drQtSame () = true := by native_decide

/-- In turns they can: leaving the DR turns saves nothing on 3,024 of the 5,040 oriented states, 1 turn on
1,488 and 2 turns on 528, for each axis. -/
theorem dr_turns_saved :
    drSaveBelow () = true ∧ drSaveHist 0 () = [3024, 1488, 528] ∧ drSaveHist 1 () = [3024, 1488, 528] ∧
    drSaveHist 2 () = [3024, 1488, 528] := by
  native_decide

/-- levitatingmagician's statement: for every placement, the quarter-turn count of the oriented state is the
same on all three axes, and it is the placement-only count with all nine turns. -/
theorem placement_qt_same_on_three_axes : permQtSame () = true := by native_decide

end Corners3D
