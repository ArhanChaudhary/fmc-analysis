/-
  AttemptSim.TablesThm — checked statements, part B: the tables the search trusts.

  The distance tables are not recomputed and compared: each is checked entry by entry with `search.ruleHolds`
  (0 exactly at the goal; no move leads to an entry more than one lower; every other entry has a move to an entry
  one lower), which makes every entry the exact fewest moves to the goal, whatever program wrote the table.
-/
import AttemptSim.Tables
import AttemptSim.ModelThm

namespace AttemptSim
open cube pieces cubie tables

set_option maxHeartbeats 0

/-- **The coordinate move tables are the model's.**  For every twist coordinate (2,187), flip coordinate (2,048) and
slice coordinate (495) and each of the 18 turns, the table entry is the coordinate of the simulator's own state for
that coordinate (as ctx.rs builds it) after the turn, computed with the move tables of data/model.txt; those
states have the coordinate they stand for. -/
theorem move_tables_match :
    (COMV.size == 2187 * 18 && EOMV.size == 2048 * 18 && SLMV.size == 495 * 18 &&
     ((List.range 2187).all fun co => coOf (repCo co) == co &&
        (List.range 18).all fun mv => coOf (turn MODEL.moves[mv]! (repCo co)) == COMV[co * 18 + mv]!) &&
     ((List.range 2048).all fun eo => eoOf (repEo eo) == eo &&
        (List.range 18).all fun mv => eoOf (turn MODEL.moves[mv]! (repEo eo)) == EOMV[eo * 18 + mv]!) &&
     ((List.range 495).all fun sl => slOf (repSl sl) == sl &&
        (List.range 18).all fun mv => slOf (turn MODEL.moves[mv]! (repSl sl)) == SLMV[sl * 18 + mv]!)) = true := by
  native_decide

/-- The coordinates of a state after a turn are the table entries at its coordinates before the turn, whatever the
rest of the state is: on every sticker state within 3 turns of solved and each of the 18 turns.  (In `turn` the new
twists are computed from the old twists alone, and so for flips and for where the E-slice pieces are; this is the
same fact checked on states that are not the tables' own.) -/
theorem coords_follow :
    ((near 3).all fun s =>
      let c := toCubie s
      (List.range 18).all fun mv =>
        let c' := toCubie (apply s MV[mv]!)
        coOf c' == COMV[coOf c * 18 + mv]! && eoOf c' == EOMV[eoOf c * 18 + mv]! && slOf c' == SLMV[slOf c * 18 + mv]!) = true := by
  native_decide

/-- The flip coordinate is F/B EO and the slice coordinate is where the E-slice pieces are, as the stickers have
them (`pieces.badMask 2`, `pieces.eMask`, the definitions of the EO-to-DR and EO-switch certificates): on every
state within 3 turns of solved. -/
theorem coords_are_stickers :
    ((near 3).all fun s =>
      let c := toCubie s
      (List.range 12).foldl (fun acc i => acc + c.ef[i]! * 2 ^ i) 0 == badMask 2 s && slMask c == eMask s) = true := by
  native_decide

/-- **EO distance.**  `eodist` passes the check with all 18 turns and goal "no flipped edge": each of its 2,048
entries is the fewest turns to F/B EO from that flip pattern.  By value 0 … 7: 1, 2, 25, 202, 620, 900, 285, 13. -/
theorem eodist_checked :
    search.ruleHolds 2048 0 (List.range 18) eoStep EODIST = true ∧
    EODIST_L.all (· < 255) = true ∧
    histA EODIST_L 16 = [(0, 1), (1, 2), (2, 25), (3, 202), (4, 620), (5, 900), (6, 285), (7, 13)] := by
  native_decide

/-- **EO-kept distance to DR.**  `drdist` passes the check over all 2,187 × 495 = 1,082,565 (twist, slice)
coordinates with the 14 EO-keeping turns and goal "no twist, E-slice pieces home": each entry is the fewest
EO-keeping turns to DR on U/D.  Every coordinate pair has an entry.  By value 0 … 10: 1, 2, 17, 134, 1065, 8190,
54694, 267576, 560568, 187204, 3114 (Cale's table; the same histogram is proved, from another program's table, in
the EO-switch certificate `dist_hist`). -/
theorem drdist_checked :
    search.ruleHolds (2187 * 495) MODEL.solvedSl MODEL.eoKeep.toList drStep DRDIST = true ∧
    DRDIST.size = 1082565 ∧
    histA (DRDIST.toList.map (·.toNat)).toArray 32 =
      [(0, 1), (1, 2), (2, 17), (3, 134), (4, 1065), (5, 8190), (6, 54694), (7, 267576), (8, 560568), (9, 187204), (10, 3114)] := by
  native_decide

/-- The DR group in judging-a-dr's numbering: the ten DR moves permute the 8 corner positions and the 8 U/D-layer
edge positions; half turns reach 96 corner permutations; rank and unrank are inverse on all 40,320 ranks. -/
theorem dr_group :
    (CT.size == 10 && ET.size == 10 &&
     (CT.all fun t => (List.range 8).all fun j => t.contains j) &&
     (ET.all fun t => (List.range 8).all fun j => t.contains j) &&
     HC.size == 96 &&
     (List.range 40320).all fun r => rank (unrank 8 r) == r) = true := by
  native_decide

/-- **The cosets are judging-a-dr's.**  The 420 representatives of cosets.txt are increasing, each is the smallest
rank of its own coset, and every one of the 40,320 corner permutations lies in the coset of one of them; the move
action on cosets does not depend on the representative (all 40,320 × 10).  The 70 patterns are the 70 ways to place
the four M-slice edges, in the listed order, the first being the solved one. -/
theorem cosets_ok :
    (REPS.size == 420 && (List.range 419).all (fun k => REPS[k]! < REPS[k + 1]!) &&
     REPS.all (fun r => CANON[r]! == r) &&
     (List.range 40320).all (fun r => KOF[CANON[r]!]! < 420 &&
        (List.range 10).all fun m => KOF[CANON[cstep r m]!]! == CCM[KOF[CANON[r]!]! * 10 + m]!) &&
     PMASKS.size == 70 && PMASKS.toList.eraseDups.length == 70 && PMASKS.all (fun mk => popcount mk == 4) &&
     PMASKS[0]! == 85 && PPM.all (· < 70)) = true := by
  native_decide

/-- **Fewest DR moves to HTR.**  `htrdist` passes the check over all 420 × 70 = 29,400 HTR cosets with the ten DR
moves and goal "the coset of the solved cube": each entry is the shortest linear DR → HTR of the coset.  The
longest is 13 (as proved for judging-a-dr's table in DRBound `rung_maxima`), and the values 0 … 13 occur
1, 2, 9, 36, 124, 530, 1806, 3732, 5158, 7070, 7218, 3202, 488, 24 times. -/
theorem htrdist_checked :
    search.ruleHolds 29400 HTR_GOAL (List.range 10) htrStep HTRDIST = true ∧
    HTRDIST_L.size = 29400 ∧ HTRDIST_L.all (· < 255) = true ∧
    histA HTRDIST_L 32 =
      [(0, 1), (1, 2), (2, 9), (3, 36), (4, 124), (5, 530), (6, 1806), (7, 3732), (8, 5158), (9, 7070), (10, 7218),
       (11, 3202), (12, 488), (13, 24)] := by
  native_decide

end AttemptSim
