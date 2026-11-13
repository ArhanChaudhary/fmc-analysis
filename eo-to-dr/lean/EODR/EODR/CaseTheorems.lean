/-
  EODR.CaseTheorems — checked statements, part E (see README.md): the per-case figures the page prints, the page's
  case tables, the superflip's NISS EO, nissy's modulo bias and the binomials.  Statements that run the BFS or the
  sticker model are proved by `native_decide` (compiled code; this trusts the Lean compiler); plain arithmetic on
  numbers by `decide` (Lean's kernel alone).

  Reading aid.  `cases.stats c e o` = [states, DR in ≤ 4, ≤ 5, ≤ 6, ≤ 7, Σ distance] of case `c`c`e`e under option
  `o` ("eo": one axis, EO kept; "eo_switchF": the better of the state and the state after F2, i.e. the EO's last F
  quarter turn turned the other way).  `cases.rounds num den v p`: num/den rounded to p digits is v/10^p.
-/
import EODR.Cases
import EODR.EodrTheorems

namespace EODR
open cube pieces cases

set_option maxHeartbeats 0
set_option exponentiation.threshold 400

/-! ## E. Per-case figures, the page's case tables, the superflip, nissy's bias, binomials -/

/-- Lean's own per-case counts (from the checked BFS of `Eodr.lean`, not from the research's file), for the cases
the page quotes: [states, ≤ 4, ≤ 5, ≤ 6, ≤ 7, Σ distance] with one axis (EO kept), then ≤ 6 and Σ distance with the
EO's last turn either way.  The last-turn option is the same with F2 and with B2 in every case, and 4c4e's
last-turn histogram (0 … 11 turns) is given in full (Cale's 25 re-test). -/
theorem case_stats :
    stats 4 6 "eo" = [94080, 72, 568, 4344, 25624, 738096] ∧
    stats 4 4 "eo" = [70560, 578, 3064, 13576, 41926, 507090] ∧
    stats 4 2 "eo" = [13440, 72, 448, 2512, 8432, 96232] ∧
    stats 3 4 "eo" = [18816, 0, 184, 1872, 9032, 140112] ∧
    stats 7 8 "eo" = [23520, 120, 744, 3856, 13496, 170624] ∧
    stats 3 6 "eo" = [25088, 16, 160, 1216, 6792, 196792] ∧
    stats 6 6 "eo" = [137984, 40, 808, 7712, 45640, 1067168] ∧
    stats 5 6 "eo" = [125440, 64, 832, 7696, 44784, 964280] ∧
    ((stats 4 6 "eo_switchF")[3]!, (stats 4 6 "eo_switchF")[5]!) = (7216, 713496) ∧
    ((stats 4 4 "eo_switchF")[3]!, (stats 4 4 "eo_switchF")[5]!) = (19798, 486544) ∧
    ((stats 4 2 "eo_switchF")[3]!, (stats 4 2 "eo_switchF")[5]!) = (3656, 92636) ∧
    ((stats 3 4 "eo_switchF")[3]!, (stats 3 4 "eo_switchF")[5]!) = (2988, 135120) ∧
    ((stats 7 8 "eo_switchF")[3]!, (stats 7 8 "eo_switchF")[5]!) = (5740, 164100) ∧
    ((stats 3 6 "eo_switchF")[3]!, (stats 3 6 "eo_switchF")[5]!) = (1964, 190124) ∧
    hist 4 4 "eo_switchF" = [0, 4, 28, 136, 744, 4012, 14874, 32640, 17782, 340, 0, 0] ∧
    (BYCASE.all fun (c, e, o, h) => o != "eo_switchF" || hist c e "eo_switchB" == h) ∧
    (BYCASE.filter (·.2.2.1 == "eo")).length = 40 := by
  native_decide

/-- The per-case figures as the page prints them (section 1, the claims table of section 6, errata 1 and 3), each
the exact fraction of `case_stats` (or `eodr_facts`) rounded as printed.
* Jay's 6e4c (errata 3): DR in ≤ 6 on 4.6% of 4c6e, 19.2% of 4c4e, 18.7% of 4c2e; means 7.85, 7.19, 7.16.
* Cale's 4c6e "1 in 22": 1 in 21.7 (and 21.66… rounds to 22).
* Zagros's "10% vs 16%" (3c4e, 7c8e): 9.9% and 16.4% (which round to 10% and 16%).
* Noah Swor's 3c6e: 1 in 12.8 with the last turn either way, 1 in 20.6 in ≤ 6, 1 in 3.7 in ≤ 7; 7c8e with the last
  turn 1 in 4.1; 4c4e 1 in 5.2 and 1 in 3.6 (Tom Nelson), 28.1% with the last turn (Lichi Fang's row).
* Case shares: 3c6e 2.3% (1 in 43.2), 4c4e 1 in 15.3, 6c6e 12.7% against 5c6e 11.6% (Jay, torchlight).
* Tom Nelson's "150 4e4c's in 5": 150 × 4.3% = 6.5 DRs in ≤ 5, 150 × 0.82% = 1.2 in ≤ 4.
* Cale's 25 re-test, 4c4e with the last turn either way: 7.0% in ≤ 5, 21.1% in 6, 46.3% in 7, 25.2% in 8, 0.48% in 9.
* zakimoshi's / Louis's "5.9%": 64103/1082565 = 5.9% (one axis: 1 in 16.89); KrzychXyz's "~3%": 3114/1082565 = 0.29%. -/
theorem case_digits :
    rounds (100 * 4344) 94080 46 1 ∧ rounds (100 * 13576) 70560 192 1 ∧ rounds (100 * 2512) 13440 187 1 ∧
    rounds 738096 94080 785 2 ∧ rounds 507090 70560 719 2 ∧ rounds 96232 13440 716 2 ∧
    rounds 94080 4344 217 1 ∧ rounds 94080 4344 22 0 ∧
    rounds (100 * 1872) 18816 99 1 ∧ rounds (100 * 3856) 23520 164 1 ∧
    rounds (100 * 1872) 18816 10 0 ∧ rounds (100 * 3856) 23520 16 0 ∧
    rounds 25088 1964 128 1 ∧ rounds 25088 1216 206 1 ∧ rounds 25088 6792 37 1 ∧ rounds 23520 5740 41 1 ∧
    rounds 70560 13576 52 1 ∧ rounds 70560 19798 36 1 ∧ rounds (100 * 19798) 70560 281 1 ∧
    rounds (100 * 25088) 1082565 23 1 ∧ rounds 1082565 25088 432 1 ∧ rounds 1082565 70560 153 1 ∧
    rounds (100 * 137984) 1082565 127 1 ∧ rounds (100 * 125440) 1082565 116 1 ∧
    rounds (100 * 3064) 70560 43 1 ∧ rounds (150 * 3064) 70560 65 1 ∧
    rounds (100 * 578) 70560 82 2 ∧ rounds (150 * 578) 70560 12 1 ∧
    4 + 28 + 136 + 744 + 4012 = 4924 ∧ rounds (100 * 4924) 70560 70 1 ∧ rounds (100 * 14874) 70560 211 1 ∧
    rounds (100 * 32640) 70560 463 1 ∧ rounds (100 * 17782) 70560 252 1 ∧ rounds (100 * 340) 70560 48 2 ∧
    rounds (100 * 64103) 1082565 59 1 ∧ rounds (100 * 3114) 1082565 29 2 ∧ rounds 1082565 64103 1689 2 := by
  decide

/-- **The page's case tables** (section 5's table and the three tables of appendix A, `report/data/c6_case*.md`,
verbatim in Study.lean) agree with Lean's per-case counts.  Each row names a case that occurs (16 rows in section 5,
39 in each appendix table), and in the columns Lean has (share of the 1,082,565 EO-solved states, odds "1 in x",
mean turns and DR in ≤ 6, each with one axis and with the EO's last turn either way) every printed value is Lean's
exact fraction rounded as printed: no cell is off (`badCells … = []`).  The other columns (any turns, two DR axes,
normal or inverse, all options) are not Lean's.
This theorem first found three values, each printed in two tables, rounded twice (the research stored them to 5
decimals, then the page rounded again): 7c6e with the last turn ≤ 6 was printed 6.8% (exact 5080/75264 = 6.7%),
6c2e the same 0.33% (exact 64/19712 = 0.32%), 0c4e's share 0.015% (exact 168/1082565 = 0.016%).  `xtables.py` now
takes these columns from the exact counts; the last line keeps the exact values. -/
theorem case_tables_match_page :
    rowsOk study.PAGE_C6_CASE 16 = true ∧ rowsOk study.PAGE_C6_CASE_FULL 39 = true ∧
    rowsOk study.PAGE_C6_CASE_FULL_MEAN 39 = true ∧ rowsOk study.PAGE_C6_CASE_FULL_LE6 39 = true ∧
    badCells study.PAGE_C6_CASE [(1, 0), (2, 1), (3, 2), (4, 4), (5, 5)] = [] ∧
    badCells study.PAGE_C6_CASE_FULL [(1, 0), (2, 1)] = [] ∧
    badCells study.PAGE_C6_CASE_FULL_MEAN [(1, 2), (3, 3)] = [] ∧
    badCells study.PAGE_C6_CASE_FULL_LE6 [(1, 4), (3, 5)] = [] ∧
    stats 7 6 "eo_switchF" = [75264, 0, 452, 5080, 30624, 570016] ∧ (stats 6 2 "eo_switchF")[3]! = 64 ∧
    (stats 0 4 "eo")[0]! = 168 ∧
    pctOk 5080 75264 "6.7%" = true ∧ pctOk 64 19712 "0.32%" = true ∧ pctOk 168 1082565 "0.016%" = true := by
  native_decide

/-- **The superflip has no NISS EO of 6 or fewer turns, on any axis** (errata 2).  On the sticker model:
the superflip (as printed) commutes with each of the 18 face turns; it has 12 bad edges on each axis (mask 4095), and
the checked one-axis EO table (`eo_table_checked`) gives that mask 7 turns on each axis; and the printed 7-move NISS
EO `D F U' (L B R U')` (inverse moves done as premoves `U R' B' L'`) solves EO on U/D.
The step from these to "no NISS EO of 6" is a line on paper: a NISS EO is normal moves A and inverse moves B with
B⁻¹ · S · A EO-solved (the inverse moves act as premoves); since S commutes with every face turn it commutes with B⁻¹,
so B⁻¹ · S · A = S · (B⁻¹ A), and B⁻¹ A is a linear EO of |A| + |B| turns, at least 7 by the table. -/
theorem superflip_niss_eo :
    (NAMES.all fun m => do_ SOLVED (SF ++ " " ++ m) == do_ SOLVED (m ++ " " ++ SF)) = true ∧
    ((List.range 3).all fun Y => badMask Y (do_ SOLVED SF) == 4095 && ((eo.dist Y).get! 4095).toNat == 7) = true ∧
    badMask 1 (do_ SOLVED ("U R' B' L' " ++ SF ++ " D F U'")) = 0 := by
  native_decide

/-- **nissy 2.0.8's `ep = rand() % FACTORIAL12`** with glibc's rand() in [0, 2³¹ − 1]: 12! = 479,001,600 and
2³¹ = 4 · 12! + 231,477,248, so the lowest 231,477,248 indices (48.3% of 12!) come up 5 times and the rest 4 times:
5/4, 25% more likely.  2³¹ is 4.48 × 12!. -/
theorem nissy_modulo_bias :
    fact 12 = 479001600 ∧ 2 ^ 31 = 4 * fact 12 + 231477248 ∧ 231477248 < fact 12 ∧
    rounds (100 * 231477248) (fact 12) 483 1 ∧ rounds (2 ^ 31) (fact 12) 448 2 ∧
    rounds (100 * (5 - 4)) 4 25 0 := by
  decide

/-- **Binomials on the page.**
* Lichi Fang's "3 of 27": with p = 19798/70560 (4c4e, DR in ≤ 6 with the last turn either way, `eodr_facts`),
  P(at most 3 of 27) = 3.3% (compLex's 3.2% was the same computation, rounded down).
* DougCube's "92.71%": with p = 9409/1082565 (one axis, EO kept, DR in ≤ 5: 1 + 2 + 17 + 134 + 1065 + 8190),
  1 − (1 − p)³⁰⁰ = 92.71%; the page calls the arithmetic right.
* bpaul's DR skip: C(12,4) = 495 = 12!/(8!·4!), against 12!/8! = 11,880; 2¹¹ · 3⁷ · 495 = 2,217,093,120 cosets on one
  axis, a third of that 739 million. -/
theorem binomial_digits :
    rounds (100 * binomLe 3 27 19798 70560) (70560 ^ 27) 33 1 ∧
    1 + 2 + 17 + 134 + 1065 + 8190 = 9409 ∧
    rounds (100 * (1082565 ^ 300 - (1082565 - 9409) ^ 300)) (1082565 ^ 300) 9271 2 ∧
    choose 12 4 = 495 ∧ fact 12 / fact 8 = 11880 ∧ 2 ^ 11 * 3 ^ 7 * 495 = 2217093120 ∧
    rounds 2217093120 3000000 739 0 := by
  decide

end EODR
