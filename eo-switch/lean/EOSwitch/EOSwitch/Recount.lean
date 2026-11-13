/-
  EOSwitch.Recount — part E of README.md (added 2026-11-13): the study's corner-case, ARM, rule-card, strict-
  separation, low-DRM, last-turn and inverse figures, recounted from the checked BFS through the features of
  `Full.lean`; the example labels and errata a's NISS DR on the sticker model; and the RZP's last turn.  Two theorems
  keep the names of errata items the second read withdrew (`errata_b_3qt`, `errata_c_stacked`): the counts are still
  right and the pages still use them, but they no longer correct anyone.

  Reading aid.  `cell c e p` = [states, DR in ≤ 5, ≤ 6 ("sub-7"), ≤ 7] of the states of DRM `c`c`e`e with property
  p.  Corner case `cc`: 0 a, 1 b, 2 c, 3 d; `suf` the suffix ("4b-0": cc = 1, suf = 0); ARM = (carm, earm).
  Every computation is `native_decide` (trusts the compiler, see README); the percentages quoted in the docstrings
  are the exact fractions, compared with the pages outside Lean.
-/
import EOSwitch.Full
import EOSwitch.Model

namespace EOSwitch
open cube pieces sw full

set_option maxHeartbeats 0

/-- The feature table: every reached state (1,082,565) is in it, every state's features survive packing, and
JZP read from the per-twist tables equals `feat`'s. -/
theorem full_table : T.states = 1082565 ∧ T.packs = true := by native_decide

def armIs (a : Nat) (f : F2) : Bool := f.carm * 10 + f.earm == a

/-! ## Corner case (4a–4d), suffix, stacked -/

/-- The 4c4e your-call group (one paired edge, edge ARM 1) split by corners (page section 1 and `c44_check`):
4d 512/576 = 88.9%; 4b ARM 21 1488/4512 = 33.0%; 4a ARM 21 432/2304 = 18.75%; 4a corner ARM 0 or 4 408/1728 =
23.6%; corner ARM 1 or 3 (4c) 1560/10368 = 15.0%; 4b corner ARM 0 or 4 192/3456 = 5.6%. -/
theorem corner_case_your_call :
    let g := fun f : F2 => f.edgesPaired == 1 && f.earm == 1
    cell 4 4 (fun f => g f && f.cc == 3) = [576, 128, 512, 576] ∧
    cell 4 4 (fun f => g f && f.carm == 2 && f.cc == 1) = [4512, 320, 1488, 3840] ∧
    cell 4 4 (fun f => g f && f.carm == 2 && f.cc == 0) = [2304, 64, 432, 1712] ∧
    cell 4 4 (fun f => g f && (f.carm == 0 || f.carm == 4) && f.cc == 0) = [1728, 48, 408, 1224] ∧
    cell 4 4 (fun f => g f && (f.carm == 1 || f.carm == 3)) = [10368, 96, 1560, 7216] ∧
    cell 4 4 (fun f => g f && (f.carm == 0 || f.carm == 4) && f.cc == 1) = [3456, 0, 192, 2208] := by
  native_decide

/-- Once errata b, withdrawn (rodneykinney's "3qt corners" are the 4a-0 row in 4c2e, not 4b-0): 4c2e with 4b-0 corners, by pairs: 0 → 80/960 = 8.3%, 1 → 232/384 = 60.4%,
2 → 152/192 = 79.2%. -/
theorem errata_b_3qt :
    (List.range 3).map (fun p => cell 4 2 (fun f => f.cc == 1 && f.suf == 0 && f.pairs == p)) =
      [[960, 8, 80, 408], [384, 64, 232, 376], [192, 88, 152, 192]] := by
  native_decide

/-- Once errata c, withdrawn (Evan's "stacked" is the sheet's allF/allR/colU layouts, 34.8% / 2.5% on the page): 4c4e, 1 pair, ARM 21, by corners: a 392/2016 = 19.4%, b 1104/3840 = 28.75%, d 512/576 = 88.9%;
a with all four bad corners on one R/L side 120/336 = 35.7%, the rest 272/1680 = 16.2% (an earlier reading of "stacked"). -/
theorem errata_c_stacked :
    let g := fun f : F2 => f.pairs == 1 && armIs 21 f
    [0, 1, 3].map (fun k => cell 4 4 (fun f => g f && f.cc == k)) =
      [[2016, 64, 392, 1504], [3840, 184, 1104, 3216], [576, 128, 512, 576]] ∧
    cell 4 4 (fun f => g f && f.cc == 0 && f.lr == 4) = [336, 0, 120, 248] ∧
    cell 4 4 (fun f => g f && f.cc == 0 && f.lr != 4) = [1680, 64, 272, 1256] := by
  native_decide

/-- Claims T8122, T8123, D14342, D14348 (4c4e).  By case and suffix: 4a-0 492/2016, 4a-2 1548/8064, 4b-0 712/8064,
4b-2 3936/16128.  0 pairs and 0 fake pairs: 4a-0 28/120 = 23.3%, no 4d state, 4b-2 112/576 = 19.4%.  4d with 1
pair: ARM 20 0/288, 21 512/576, 22 0/288.  4a by ARM 20/21/22: 312/1728, 920/4608, 316/1728. -/
theorem corner_case_claims :
    [(0, 0), (0, 2), (1, 0), (1, 2)].map (fun (k, s) => cell 4 4 (fun f => f.cc == k && f.suf == s)) =
      [[2016, 172, 492, 1190], [8064, 224, 1548, 4988], [8064, 64, 712, 3936], [16128, 1112, 3936, 10296]] ∧
    [cell 4 4 (fun f => f.pairs == 0 && f.fake == 0 && f.cc == 0 && f.suf == 0),
     cell 4 4 (fun f => f.pairs == 0 && f.fake == 0 && f.cc == 3),
     cell 4 4 (fun f => f.pairs == 0 && f.fake == 0 && f.cc == 1 && f.suf == 2)] =
      [[120, 16, 28, 68], [0, 0, 0, 0], [576, 32, 112, 328]] ∧
    [20, 21, 22].map (fun a => cell 4 4 (fun f => f.cc == 3 && f.pairs == 1 && armIs a f)) =
      [[288, 0, 0, 64], [576, 128, 512, 576], [288, 0, 0, 56]] ∧
    [20, 21, 22].map (fun a => cell 4 4 (fun f => f.cc == 0 && armIs a f)) =
      [[1728, 56, 312, 952], [4608, 112, 920, 3096], [1728, 56, 316, 940]] := by
  native_decide

/-! ## ARM -/

/-- 4c4e by ARM (Appendix A), each ARM with its cells by paired edges 0, 1, 2 and the whole ARM.  Yura Riabov's
"trash" ARMs 02, 12, 30, 40: 4/1296, 112/3456, 120/3456, 4/1296, all under 4%. -/
theorem arm_4c4e :
    [0, 1, 2, 10, 11, 12, 20, 21, 22, 30, 31, 32, 40, 41, 42].map (fun a =>
      ((List.range 3).map fun e => cell 4 4 (fun f => armIs a f && f.edgesPaired == e), cell 4 4 (armIs a))) =
    [([[36, 16, 24, 36], [576, 32, 172, 480], [684, 164, 420, 668]], [1296, 212, 616, 1184]),
     ([[864, 0, 8, 144], [2592, 24, 280, 1664], [0, 0, 0, 0]], [3456, 24, 288, 1808]),
     ([[1296, 0, 4, 206], [0, 0, 0, 0], [0, 0, 0, 0]], [1296, 0, 4, 206]),
     ([[288, 0, 24, 144], [2016, 16, 304, 1288], [1152, 216, 656, 1112]], [3456, 232, 984, 2544]),
     ([[2592, 0, 48, 728], [5184, 48, 808, 3544], [1440, 240, 768, 1368]], [9216, 288, 1624, 5640]),
     ([[1728, 0, 32, 464], [1728, 0, 80, 704], [0, 0, 0, 0]], [3456, 0, 112, 1168]),
     ([[1368, 0, 72, 456], [3528, 32, 280, 1680], [720, 64, 340, 652]], [5616, 96, 692, 2788]),
     ([[4656, 48, 512, 2368], [7392, 512, 2432, 6128], [2928, 888, 2192, 2888]], [14976, 1448, 5136, 11384]),
     ([[1368, 0, 48, 388], [3528, 32, 224, 1420], [720, 48, 288, 616]], [5616, 80, 560, 2424]),
     ([[1728, 0, 40, 408], [1728, 0, 80, 664], [0, 0, 0, 0]], [3456, 0, 120, 1072]),
     ([[2592, 0, 40, 736], [5184, 48, 752, 3672], [1440, 248, 840, 1424]], [9216, 296, 1632, 5832]),
     ([[288, 0, 24, 160], [2016, 24, 328, 1384], [1152, 208, 656, 1112]], [3456, 232, 1008, 2656]),
     ([[1296, 0, 4, 200], [0, 0, 0, 0], [0, 0, 0, 0]], [1296, 0, 4, 200]),
     ([[864, 0, 0, 184], [2592, 24, 320, 1768], [0, 0, 0, 0]], [3456, 24, 320, 1952]),
     ([[36, 10, 30, 36], [576, 8, 64, 376], [684, 114, 382, 656]], [1296, 132, 476, 1068])] := by
  native_decide

/-- 4c4e by paired edges × edge ARM (`c44_paired_earm`); and on 4c4e, "both bad edges in one slice" is exactly
"edge ARM 0 or 2" (all 70,560 states). -/
theorem paired_edge_arm_4c4e :
    (List.range 3).flatMap (fun e => (List.range 3).map fun a =>
      cell 4 4 (fun f => f.edgesPaired == e && f.earm == a)) =
      [[4716, 16, 164, 1244], [11568, 48, 608, 4160], [4716, 10, 138, 1254],
       [7848, 80, 836, 4112], [22944, 656, 4592, 16776], [7848, 64, 696, 3884],
       [2556, 444, 1416, 2432], [5808, 1376, 3800, 5680], [2556, 370, 1326, 2384]] ∧
    nOf (sumWhere fun f => isDrm 4 4 f && f.sameSlice == (f.earm != 1)) = 70560 := by
  native_decide

/-- 7c8e with 4 pairs by edge ARM 0 … 4 (`c78_check`): 0/96, 528/1744 = 30.3%, 432/4240, 296/1744 = 17.0%, 0/96;
and by ARM 11, 12, 33, 41, 62, 21 (claim D15175): only 21 has a state with DR in ≤ 5. -/
theorem pairs4_7c8e :
    (List.range 5).map (fun a => cell 7 8 (fun f => f.pairs == 4 && f.earm == a)) =
      [[96, 0, 0, 64], [1744, 40, 528, 1488], [4240, 0, 432, 2768], [1744, 0, 296, 1464], [96, 0, 0, 56]] ∧
    [11, 12, 33, 41, 62, 21].map (fun a => cell 7 8 (fun f => f.pairs == 4 && armIs a f)) =
      [[144, 0, 32, 144], [360, 0, 80, 272], [520, 0, 120, 456], [520, 0, 112, 440], [360, 0, 72, 296],
       [336, 40, 232, 336]] := by
  native_decide

/-- Bars: 4c4e, 2 pairs, per ARM, (bar on one edge, pairs on the two edges).  The gap runs from 11.8 points (ARM
11: 288/864 vs 520/1152) to 31.2 (ARM 20: 104/648 vs 340/720). -/
theorem bars_by_arm :
    [0, 10, 21, 32, 42, 11, 31, 20, 22].map (fun a =>
      (cell 4 4 (fun f => armIs a f && f.pairs == 2 && f.edgesPaired == 1),
       cell 4 4 (fun f => armIs a f && f.pairs == 2 && f.edgesPaired == 2))) =
    [([288, 32, 108, 256], [360, 84, 184, 344]), ([576, 0, 104, 456], [864, 104, 400, 824]),
     ([960, 136, 424, 832], [2208, 600, 1640, 2184]), ([576, 8, 120, 488], [864, 88, 408, 824]),
     ([288, 8, 64, 224], [360, 84, 180, 332]), ([864, 48, 288, 784], [1152, 136, 520, 1080]),
     ([864, 40, 288, 800], [1152, 128, 568, 1136]), ([648, 0, 104, 480], [720, 64, 340, 652]),
     ([648, 0, 80, 388], [720, 48, 288, 616])] := by
  native_decide

/-! ## Strict separation ("settles") -/

def SKEYS : List (F2 → List Nat) :=
  [fun f => [f.carm, f.earm], fun f => [f.pairs], fun f => [f.edgesPaired], fun f => [f.cc, f.suf],
   fun f => [f.pairs, f.carm, f.earm], fun f => [f.pairs, f.cc, f.suf], fun f => [f.edgesPaired, f.earm],
   fun f => [2 * f.pairs + f.side]]

/-- `decided_by_feature` (and section 1's "ARM alone 31.2%, pairs alone 33.3%, pairs × ARM 49.6%"): for each key
(ARM; pairs; paired edges; corner case + suffix; pairs + ARM; pairs + corner case; paired edges + edge ARM;
pairs + side pairs/2) and each of 4c4e, 4c2e, 7c8e, 8c8e, 2c2e, the states in key cells under 10% or over 50%
sub-7, and the DRM's states. -/
theorem strict_separation :
    SKEYS.map (fun k => [(4, 4), (4, 2), (7, 8), (8, 8), (2, 2)].map fun (c, e) => strict c e k) =
    [[(22032, 70560), (4800, 13440), (7584, 23520), (2588, 6020), (768, 1792)],
     [(23520, 70560), (8640, 13440), (15600, 23520), (1448, 6020), (384, 1792)],
     [(31920, 70560), (7680, 13440), (8000, 23520), (1492, 6020), (416, 1792)],
     [(8064, 70560), (384, 13440), (0, 23520), (0, 6020), (0, 1792)],
     [(34992, 70560), (8496, 13440), (16176, 23520), (3736, 6020), (816, 1792)],
     [(30792, 70560), (8688, 13440), (15600, 23520), (1448, 6020), (384, 1792)],
     [(39768, 70560), (7680, 13440), (10152, 23520), (2422, 6020), (208, 1792)],
     [(36602, 70560), (10136, 13440), (12864, 23520), (1492, 6020), (1464, 1792)]] := by
  native_decide

/-! ## The rule cards (first matching row wins) -/

/-- A card: each row (verdict 0 switch, 1 your call, 2 discard; property), the states it takes that no earlier row
took, as [states, ≤ 5, ≤ 6, ≤ 7]. -/
def card (c e : Nat) (rows : List (Nat × (F2 → Bool))) : List (Nat × List Nat) :=
  let rec go (rs : List (Nat × (F2 → Bool))) (taken : F2 → Bool) : List (Nat × List Nat) :=
    match rs with
    | [] => []
    | (g, p) :: t => (g, cell c e (fun f => !taken f && p f)) :: go t (fun f => taken f || p f)
  go rows (fun _ => false)
def any (_ : F2) : Bool := true

/-- The twelve cards of section 3 (`rule_cards`, `rule_cells`, `rule_cards_sum`). -/
theorem rule_cards :
    card 4 4 [(0, fun f => f.edgesPaired == 2), (1, fun f => f.edgesPaired == 1 && f.earm == 1),
      (2, fun f => f.edgesPaired == 1), (2, any)] =
      [(0, [10920, 2190, 6542, 10496]), (1, [22944, 656, 4592, 16776]), (2, [15696, 144, 1532, 7996]),
       (2, [21000, 74, 910, 6658])] ∧
    card 4 2 [(0, fun f => 2 * f.pairs + f.side ≥ 3), (1, fun f => 2 * f.pairs + f.side == 2), (2, any)] =
      [(0, [2992, 440, 1704, 2936]), (1, [3304, 0, 520, 2648]), (2, [7144, 8, 288, 2848])] ∧
    card 3 2 [(0, any)] = [(0, [3584, 688, 2208, 3536])] ∧
    card 7 8 [(0, fun f => f.pairs ≥ 5), (1, fun f => f.pairs == 4), (2, any)] =
      [(0, [3840, 704, 2264, 3600]), (1, [7920, 40, 1256, 5840]), (2, [11760, 0, 336, 4056])] ∧
    card 8 8 [(1, fun f => [0, 4, 8].contains f.carm), (2, any)] =
      [(1, [2660, 84, 544, 1902]), (2, [3360, 16, 328, 1892])] ∧
    card 2 2 [(0, fun f => f.edgesPaired ≥ 1), (1, (·.jzp)), (2, any)] =
      [(0, [416, 48, 248, 416]), (1, [144, 0, 56, 144]), (2, [1232, 0, 120, 976])] ∧
    card 4 6 [(0, (·.jzp)), (1, fun f => f.pairs == 4), (2, any)] =
      [(0, [576, 128, 352, 552]), (1, [1136, 176, 544, 1024]), (2, [92368, 264, 3448, 24048])] ∧
    card 3 4 [(1, fun f => f.pairs == 2), (2, any)] = [(1, [2016, 88, 680, 1672]), (2, [16800, 96, 1192, 7360])] ∧
    card 3 6 [(2, any)] = [(2, [25088, 160, 1216, 6792])] ∧
    card 5 4 [(1, fun f => f.pairs == 3), (2, any)] = [(1, [5760, 256, 1592, 5024]), (2, [88320, 512, 5192, 32872])] ∧
    card 5 6 [(1, fun f => f.pairs == 4), (2, any)] =
      [(1, [3840, 256, 1456, 3624]), (2, [121600, 576, 6240, 41160])] ∧
    card 6 6 [(1, fun f => f.jzp || f.pairs ≥ 5), (2, any)] =
      [(1, [1744, 120, 680, 1584]), (2, [136240, 688, 7032, 44056])] := by
  native_decide

/-- The low DRMs by pairs 0 … 6, JZP, and all (`low_pairs`): 4c6e, 3c4e, 3c6e, 5c4e, 5c6e, 6c6e. -/
theorem low_drm_pairs :
    [(4, 6), (3, 4), (3, 6), (5, 4), (5, 6), (6, 6)].map (fun (c, e) =>
      ((List.range 7).map (fun p => cell c e (fun f => f.pairs == p)), cell c e (·.jzp))) =
    [([[12800, 0, 16, 592], [35200, 0, 280, 4960], [33600, 120, 1600, 11744], [11200, 216, 1800, 7160],
       [1280, 232, 648, 1168], [0, 0, 0, 0], [0, 0, 0, 0]], [576, 128, 352, 552]),
     ([[6720, 8, 184, 1784], [10080, 88, 1008, 5576], [2016, 88, 680, 1672], [0, 0, 0, 0], [0, 0, 0, 0],
       [0, 0, 0, 0], [0, 0, 0, 0]], [0, 0, 0, 0]),
     ([[4480, 0, 40, 408], [13440, 32, 392, 3024], [6720, 128, 744, 3112], [448, 0, 40, 248], [0, 0, 0, 0],
       [0, 0, 0, 0], [0, 0, 0, 0]], [0, 0, 0, 0]),
     ([[15840, 8, 216, 2488], [44640, 192, 1960, 14520], [27840, 312, 3016, 15864], [5760, 256, 1592, 5024],
       [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [0, 0, 0, 0]),
     ([[6080, 0, 8, 272], [37440, 8, 464, 6088], [51840, 216, 2424, 18096], [26240, 352, 3344, 16704],
       [3840, 256, 1456, 3624], [0, 0, 0, 0], [0, 0, 0, 0]], [0, 0, 0, 0]),
     ([[4864, 0, 0, 192], [25920, 48, 512, 4032], [52800, 112, 1648, 13672], [40320, 440, 3336, 18184],
       [12480, 88, 1592, 8120], [1536, 112, 576, 1376], [64, 8, 48, 64]], [256, 16, 128, 256])] := by
  native_decide

/-! ## Graded rules used in section 1 and the claims -/

/-- [switched, of them DR ≤ k, DRM states, DRM DR ≤ k] for a rule on DRM xcye. -/
def grade (c e k : Nat) (p : F2 → Bool) : List Nat :=
  let a := sumWhere fun f => isDrm c e f && p f
  let b := sumWhere (isDrm c e)
  [nOf a, leK a 0 k, nOf b, leK b 0 k]

/-- Section 1's "1.5+ pairs" (2·pairs + side pairs ≥ 3) switches exactly the 4c2e states of Jay's "1 pair + 1 side
pair, or 2 pairs" and tseitsei89's "2 pairs, or 1 pair and a side pair" (no state differs).  And: 4c4e 2+ pairs
8522/18360 = 46.4%; 3+ pairs 2014/2520 = 79.9% on 3.6%, holding 14.8% of the sub-7s; rodneykinney's T8108
8770/17784 = 49.3%; caycala's 3+ pairs off one layer 1958/2400 = 81.6% (the page grades caycala's rule as stated: 81.8% on 3.4%); Daichi's 4-move rule 40856/63960 = 63.9%
of DR ≤ 7 on 90.6%; Zagros "always" 41926/70560 = 59.4%. -/
theorem graded_rules :
    nOf (sumWhere fun f => isDrm 4 2 f &&
      ((((f.pairs ≥ 1 && f.side ≥ 1) || f.pairs ≥ 2) != (2 * f.pairs + f.side ≥ 3)) ||
       (((f.pairs ≥ 2) || (f.pairs == 1 && f.side ≥ 1)) != (2 * f.pairs + f.side ≥ 3)))) = 0 ∧
    grade 4 4 6 (fun f => f.pairs ≥ 2) = [18360, 8522, 70560, 13576] ∧
    grade 4 4 6 (fun f => f.pairs ≥ 3) = [2520, 2014, 70560, 13576] ∧
    grade 4 4 6 (fun f => f.pairs ≥ 3 || (f.pairs == 2 && !(f.cc == 1 && f.suf == 0)) || (f.pairs == 1 && f.cc == 3))
      = [17784, 8770, 70560, 13576] ∧
    grade 4 4 6 (fun f => f.pairs ≥ 3 && !f.oneLayer) = [2400, 1958, 70560, 13576] ∧
    grade 4 4 7 (fun f => f.pairs ≥ 2 ||
      (f.pairs == 1 && !((armIs 20 f || armIs 22 f) && f.cc == 3)) ||
      (f.pairs == 0 && !(armIs 2 f || armIs 30 f || armIs 40 f || ((armIs 1 f || armIs 41 f) && f.cc == 1) ||
        (armIs 20 f && f.cc == 3)) && !(f.carm == 2 && f.oneLayer))) = [63960, 40856, 70560, 41926] ∧
    grade 4 4 7 any = [70560, 41926, 70560, 41926] ∧
    grade 7 8 6 (fun f => f.pairs ≥ 5) = [3840, 2264, 23520, 3856] ∧
    grade 2 2 6 (fun f => f.pairs ≥ 1) = [416, 248, 1792, 424] := by
  native_decide

/-! ## Free options -/

/-- 4c4e with the EO's last turn either way: 19,798 sub-7 against 13,576 (+8.8 points of 70,560); with the last
two EO turns (F, B) free: 25,304 (35.9%). -/
theorem last_turn_4c4e :
    let a := sumWhere (isDrm 4 4)
    [nOf a, leK a 0 6, leK a 1 6, leK a 2 6] = [70560, 13576, 19798, 25304] := by
  native_decide

/-- Inverse option (claim D6979, `variants_options`): given the uniformity of the inverse within its class (the
research's argument: the class is (twist-1 corners, twist-2 corners, E pieces out), and the inverse swaps the twist
counts), the expected number of states of DRM xcye with DR ≤ k on the better of normal and inverse, as an exact
fraction (num, den). -/
def clsStat (c e n1 k : Nat) : Nat × Nat := let a := sumWhere fun f => isDrm c e f && f.n1 == n1; (nOf a, leK a 0 k)
def invNum (c e k : Nat) : Nat × Nat := Id.run do
  let mut num := 0
  let mut den := 1
  for n1 in List.range (c + 1) do
    let (n, h) := clsStat c e n1 k
    if n == 0 then continue
    let (n', h') := clsStat c e (c - n1) k
    num := num * n' + (h * n' + (n - h) * h') * den
    den := den * n'
    let g := Nat.gcd num den
    num := num / g
    den := den / g
  return (num, den)

/-- The better of normal and inverse, DR ≤ 6, as "1 in x" (x · 1000, cut): 3c6e 1 in 10.571, 4c4e 2.875,
8c8e 3.724, 7c8e 3.322, 4c2e 2.950; as a share (· 100000, cut): 9.458%, 34.778%, 26.850%, 30.101%, 33.887%. -/
theorem inverse_option :
    [(3, 6), (4, 4), (8, 8), (7, 8), (4, 2)].map (fun (c, e) =>
      let (u, v) := invNum c e 6
      let n := nOf (sumWhere (isDrm c e))
      (n * v * 1000 / u, u * 100000 / (v * n))) =
    [(10571, 9458), (2875, 34778), (3724, 26850), (3322, 30101), (2950, 33887)] := by
  native_decide

/-! ## Examples on the sticker model -/

/-- The examples (state after the scramble; once errata a, b, c), as (c, e, carm, earm, pairs, case, suffix, lr, distance):
a `L' U' B2 F2 U'` 4c4e ARM 41, 2 pairs, 4a-4, 5; b `R' D2 R F2 D' U'` 4c2e, 2 pairs, 4b-0, 6; c `L' B2 D' L2 D' U2`
4c4e ARM 21, 1 pair, 4a, not stacked (lr 2), 6.  Claim T8123 (states solved by the sequence): `F2 B2 R` 4a-0, 0
pairs, 0 fake, 3; `D F2 B2 R` 4b-2, 0 pairs, 0 fake, 4.  Errata a's NISS DR: the inverse of the setup then L
(`U F2 B2 U L L`) is a DR state with F/B EO. -/
theorem example_labels :
    [(true, "L' U' B2 F2 U'"), (true, "R' D2 R F2 D' U'"), (true, "L' B2 D' L2 D' U2"), (false, "F2 B2 R"),
     (false, "D F2 B2 R")].map (fun (a, s) =>
      let st := exState a s
      let x := coOf st * 4096 + eMask st
      let f := f2 x
      [f.c, f.e, f.carm, f.earm, f.pairs, f.fake, f.cc, f.suf, f.lr, (dist.get! x).toNat]) =
    [[4, 4, 4, 1, 2, 1, 0, 4, 2, 5], [4, 2, 4, 1, 2, 0, 1, 0, 3, 6], [4, 4, 2, 1, 1, 1, 0, 2, 2, 6],
     [4, 4, 0, 0, 0, 0, 0, 0, 4, 3], [4, 4, 2, 1, 0, 0, 1, 2, 3, 4]] ∧
    (let st := do_ SOLVED "U F2 B2 U L L"; coOf st == 0 && eMask st == E_HOME && badMask 2 st == 0) = true := by
  native_decide

/-! ## The RZP's last turn -/

/-- Colour axis of every sticker, read through a relabelling. -/
theorem cax_map_eq (s : State) (f g : Nat → Nat) (h : ∀ v, cax (f v) = cax (g v)) :
    ∀ i : Nat, cax ((s.map f)[i]!) = cax ((s.map g)[i]!) := by
  intro i
  by_cases hi : i < s.size
  · simp [hi, h]
  · simp [hi]

/-- The U/D coset (twists, places of the E pieces) reads the stickers only through their colour axis: two
relabellings of one sticker state that agree on the colour axis of every label give the same coset.  (Proved for
every array, by rewriting; no computation.) -/
theorem coset_of_relabel (s : State) (f g : Nat → Nat) (h : ∀ v, cax (f v) = cax (g v)) :
    coOf (s.map f) = coOf (s.map g) ∧ eMask (s.map f) = eMask (s.map g) := by
  have hc := cax_map_eq s f g h
  constructor
  · simp only [coOf, twistAt, hc]
  · simp only [eMask, hc]

/-- The relabelling of a premove: label v ↦ the label at place v after the turn (v < 54), unchanged otherwise. -/
def relabel (mv : String) (v : Nat) : Nat := if v < 54 then (do_ SOLVED mv)[v]! else v

/-- All move-index sequences of at most n turns. -/
def seqs : Nat → List (List Nat)
  | 0 => [[]]
  | n + 1 => [[]] ++ (List.range 18).flatMap fun m => (seqs n).map (m :: ·)
def doSeq (s : State) (w : List Nat) : State := w.foldl (fun s m => apply s MV[m]!) s
def relabelI (x v : Nat) : Nat := if v < 54 then (apply SOLVED MV[x]!)[v]! else v

/-- **The RZP's last quarter turn either way gives the same switched case.**  The switched state is the inverse;
it starts with the inverse of the RZP's last turn, so the two attempts differ by which quarter turn X or X' of one
face comes first.  (1) For each face, X and X' put stickers of the same colour axis on every place; so by
`coset_of_relabel`, for every sticker state s the relabellings of s by X and by X' have the same U/D coset (and,
since the check is on every colour axis, the same coset for any DR axis).  (2) A premove is that relabelling:
`do_ (X first) w = (do_ w).map (relabel X)`, checked here on every sequence w of up to 3 turns and every face turn;
in general it holds because a turn moves labels between places without reading them. -/
theorem rzp_last_turn :
    (["U", "D", "R", "L", "F", "B"].all fun x =>
      (List.range 54).all fun v => cax (relabel x v) == cax (relabel (x ++ "'") v)) ∧
    ((List.range 18).all fun x => (seqs 3).all fun w =>
      doSeq (apply SOLVED MV[x]!) w == (doSeq SOLVED w).map (relabelI x)) := by
  native_decide

end EOSwitch
