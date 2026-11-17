/-
  EOSwitch.CardsThm — part G of README.md (added 2026-11-16): the v2 switch cards and the current policies,
  recounted from the checked BFS through the reads of `Cards.lean`, and compared with the research's numbers.

  Reading aid.  A *group row* is [states, DR in 4 or less, DR in 5, DR in 6, DR in 7, DR longer than 7].  A *policy
  row* is [states switched, DR in 4 or less not switched, DR in 5 not switched, DR in 6 not switched, switched with
  a DR of 7 or longer]; "not switched" short DRs are the ones the policy misses, "switched with 7 or longer" the
  wasted switches.  Every count takes each state of the DRM once (uniform within the DRM).
  The research's numbers are in `CardsRef.lean`, which `gen_cards.py` copies from research/v2/out/results.json and
  the sets of research/v2/cards.py, so no table entry of a `…_matches_study` theorem is typed here.
  Every computation is `native_decide` (trusts the compiler, see README).
-/
import EOSwitch.Cards
import EOSwitch.CardsRef
import EOSwitch.Model

namespace EOSwitch
open cube pieces sw full cards

set_option maxHeartbeats 0

/-! ## The table and the new reads -/

/-- The table of reads: every reached state (1,082,565) is in it, and every state's reads survive packing. -/
theorem cards_table : cards.T.states = 1082565 ∧ cards.T.packs = true := by native_decide

/-- The hole configuration of the mask whose holes are the E-slice places a and b. -/
def cfgOf (a b : Nat) : Nat := holeCfg (E_HOME - 2 ^ a - 2 ^ b)

/-- The geometry the new reads use, on the sticker model.  For each of the six pairs of E-slice places: the hole
configuration is 0 exactly when both places have a sticker on R or both on L, 2 exactly when both have one on F or
both on B, and 1 exactly when they share no face.  `holeCfg` is 3 exactly when a mask does not have two holes.
The corners counted for the U layer are those with a U sticker, and a U/D-layer edge place is in the U layer when
it has a U sticker, in the D layer when it has a D sticker.  A column is an E-slice place with the two corners
next to it: one has a U sticker, the other a D sticker, both have stickers on the two side faces of the place, and
the four columns are the eight corners, each once. -/
theorem cards_geometry :
    (E_SLOTS.all fun a => E_SLOTS.all fun b => a ≥ b ||
      (((cfgOf a b == 0) == ((onFace 2 a && onFace 2 b) || (onFace 3 a && onFace 3 b))) &&
       ((cfgOf a b == 2) == ((onFace 4 a && onFace 4 b) || (onFace 5 a && onFace 5 b))) &&
       ((cfgOf a b == 1) == !((List.range 6).any fun f => onFace f a && onFace f b)))) ∧
    ((List.range 4096).all fun m => (holeCfg m == 3) == ((holes m).length != 2)) ∧
    ((List.range 8).all fun c => onU c == (CPL[c]!.any fun i => FACE_OF[i]! == FACES[0]!)) ∧
    (UD_PLACES.all fun k => (decide ((EV k)[1]! > 0) == onFace 0 k) && (decide ((EV k)[1]! < 0) == onFace 1 k)) ∧
    (E_SLOTS.all fun k => NB[k]!.length == 2 && (NB[k]!.filter onU).length == 1 &&
      NB[k]!.all fun c => (List.range 6).all fun f => !onFace f k || (CPL[c]!.any fun i => FACE_OF[i]! == FACES[f]!)) ∧
    (E_SLOTS.flatMap fun k => NB[k]!).mergeSort (· ≤ ·) = List.range 8 := by
  native_decide

/-- The reads the cards add, on a sticker state: [paired edges, corner case, suffix, holes, corners per layer, bad
edges in one layer, split pairs, a "D F2 B2 R" case, 4a one U/D turn from 4d, anti-AR, columns with both corners
bad]. -/
def exReads (s : State) : List Nat :=
  let r := rd (coOf s * 4096 + eMask s)
  [r.ep, r.cc, r.suf, r.hc, r.uds, full.b2n r.esl, r.split, full.b2n r.dfbr, full.b2n r.a1d, full.b2n r.anti, r.cols]

/-- On the 27 worked examples of the research (the states of `feature_examples`, built on the sticker model with
their move sequences), the reads the cards add come out as the research's `features.py`, `feat2.py` and `rules.py`
have them. -/
theorem card_reads_match_study :
    (cardsref.EXAMPLES.all fun (a, seq, v) =>
      badMask 2 (exState a seq) == 0 && exReads (exState a seq) == v) = true := by
  native_decide

/-- The 48 sequences of rules.py's `dfbr`: one U or D turn, F2 B2 in either order, an R or L quarter turn. -/
def dfbrSeqs : List String :=
  ["U", "U'", "U2", "D", "D'", "D2"].flatMap fun x => ["R", "R'", "L", "L'"].flatMap fun y =>
    ["F2 B2", "B2 F2"].map fun h => x ++ " " ++ h ++ " " ++ y

/-- wen's "D F2 B2 R" cases.  `DFBR` has 12 states, as the research has; they are exactly the states that the 48
sequences of rules.py solve (built on the sticker model); each is a 4c4e with no pair and no fake pair whose DR
takes 4 turns; and the table marks 12 states. -/
theorem dfbr_cases :
    DFBR.length = 12 ∧ DFBR.length = cardsref.DFBR_COUNT ∧
    (dfbrSeqs.map fun s => coOf (exState false s) * 4096 + eMask (exState false s)).eraseDups.mergeSort (· ≤ ·) =
      DFBR.mergeSort (· ≤ ·) ∧
    (DFBR.all fun x => search.reached dist x && (dist.get! x).toNat == 4 &&
      (rd x).c == 4 && (rd x).e == 4 && (rd x).pairs == 0 && (rd x).fake == 0 && (rd x).dfbr) = true ∧
    (cards.sumWhere fun f => f.dfbr).toList.sum = 12 := by
  native_decide

/-- Each of the twelve DRMs as one group row, as the research has it: 4c4e [70560, 578, 2486, 10512, 28350,
28634], 4c2e [13440, 72, 376, 2064, 5920, 5008], 3c2e [3584, 136, 552, 1520, 1328, 48], 7c8e [23520, 120, 624,
3112, 9640, 10024], and so on. -/
theorem drm_totals_match_study :
    ALL.map (fun (c, e, _, _) => (c, e, row c e fun _ => true)) = cardsref.TOTALS := by
  native_decide

/-! ## The cards and the policies, DRM by DRM -/

def refGroups (c e : Nat) : List (String × String × List Nat) :=
  ((cardsref.GROUPS.find? fun (a, b, _) => a == c && b == e).map (·.2.2)).getD []
def refPolicies (c e : Nat) : List (String × List Nat) :=
  ((cardsref.POLICIES.find? fun (a, b, _) => a == c && b == e).map (·.2.2)).getD []

/-- The research's tables list the twelve DRMs in the order of `ALL`, each with at least two groups and with the
card, the card with its "time" groups and at least one current policy. -/
theorem cards_ref_shape :
    cardsref.GROUPS.map (fun (c, e, _) => (c, e)) = ALL.map (fun (c, e, _, _) => (c, e)) ∧
    cardsref.POLICIES.map (fun (c, e, _) => (c, e)) = ALL.map (fun (c, e, _, _) => (c, e)) ∧
    (ALL.all fun (c, e, _, _) => (refGroups c e).length ≥ 2 && (refPolicies c e).length ≥ 3) = true := by
  native_decide

/-- 4c4e.  The card's fifteen groups, with label, verdict and group row, are the research's; the groups are
disjoint as written (apart from the two "anything else" rows) and no 4c4e state is left out. -/
theorem card_4c4e_matches_study :
    cardRows 4 4 CARD44 = refGroups 4 4 ∧ overlap 4 4 CARD44 = 0 ∧ uncovered 4 4 CARD44 = 0 := by native_decide
/-- 4c4e: the policy rows of the card, the card with its "time" groups, 2+ pairs, tseitsei89's and rodneykinney's
pairs + corner case, wen's rule, caycala's chart and Fanti's pairs + ARM are the research's. -/
theorem policies_4c4e_matches_study : polRows 4 4 CARD44 BASE44 = refPolicies 4 4 := by native_decide

/-- 4c2e: the card's eight groups. -/
theorem card_4c2e_matches_study :
    cardRows 4 2 CARD42 = refGroups 4 2 ∧ overlap 4 2 CARD42 = 0 ∧ uncovered 4 2 CARD42 = 0 := by native_decide
/-- 4c2e: the card, the card with "time", 1.5+ pairs, rodneykinney's corner-case table, caycala's and Fanti's
rules. -/
theorem policies_4c2e_matches_study : polRows 4 2 CARD42 BASE42 = refPolicies 4 2 := by native_decide

/-- 3c2e: the card's three groups (wen's rule). -/
theorem card_3c2e_matches_study :
    cardRows 3 2 CARD32 = refGroups 3 2 ∧ overlap 3 2 CARD32 = 0 ∧ uncovered 3 2 CARD32 = 0 := by native_decide
/-- 3c2e: the card, the card with "time" (everything), "always", and wen's rule. -/
theorem policies_3c2e_matches_study : polRows 3 2 CARD32 BASE32 = refPolicies 3 2 := by native_decide

/-- 7c8e: the card's eight groups. -/
theorem card_7c8e_matches_study :
    cardRows 7 8 CARD78 = refGroups 7 8 ∧ overlap 7 8 CARD78 = 0 ∧ uncovered 7 8 CARD78 = 0 := by native_decide
/-- 7c8e: the card, the card with "time", 5+ pairs with edge ARM under 2 as a pair, 5 or 6 pairs, caycala's chart,
Fanti's rule. -/
theorem policies_7c8e_matches_study : polRows 7 8 CARD78 BASE78 = refPolicies 7 8 := by native_decide

/-- 8c8e: the card's nine groups. -/
theorem card_8c8e_matches_study :
    cardRows 8 8 CARD88 = refGroups 8 8 ∧ overlap 8 8 CARD88 = 0 ∧ uncovered 8 8 CARD88 = 0 := by native_decide
/-- 8c8e: the card, the card with "time", and rodneykinney's tree (3 or fewer fake pairs, with edge ARM not 2 or 6+
pairs). -/
theorem policies_8c8e_matches_study : polRows 8 8 CARD88 BASE88 = refPolicies 8 8 := by native_decide

/-- 2c2e: the card's five groups. -/
theorem card_2c2e_matches_study :
    cardRows 2 2 CARD22 = refGroups 2 2 ∧ overlap 2 2 CARD22 = 0 ∧ uncovered 2 2 CARD22 = 0 := by native_decide
/-- 2c2e: the card, the card with "time", and 1+ pairs. -/
theorem policies_2c2e_matches_study : polRows 2 2 CARD22 BASE22 = refPolicies 2 2 := by native_decide

/-- 4c6e: the card's five groups. -/
theorem card_4c6e_matches_study :
    cardRows 4 6 CARD46 = refGroups 4 6 ∧ overlap 4 6 CARD46 = 0 ∧ uncovered 4 6 CARD46 = 0 := by native_decide
/-- 4c6e: the card, "never", only JZP, and 4 pairs or JZP. -/
theorem policies_4c6e_matches_study : polRows 4 6 CARD46 BASE46 = refPolicies 4 6 := by native_decide

/-- 3c4e: the card's six groups. -/
theorem card_3c4e_matches_study :
    cardRows 3 4 CARD34 = refGroups 3 4 ∧ overlap 3 4 CARD34 = 0 ∧ uncovered 3 4 CARD34 = 0 := by native_decide
/-- 3c4e: the card, the card with "time", 2+ pairs, and Fanti's rule. -/
theorem policies_3c4e_matches_study : polRows 3 4 CARD34 BASE34 = refPolicies 3 4 := by native_decide

/-- 3c6e: the card's four groups. -/
theorem card_3c6e_matches_study :
    cardRows 3 6 CARD36 = refGroups 3 6 ∧ overlap 3 6 CARD36 = 0 ∧ uncovered 3 6 CARD36 = 0 := by native_decide
/-- 3c6e: the card, "never", and Fanti's rule. -/
theorem policies_3c6e_matches_study : polRows 3 6 CARD36 BASE36 = refPolicies 3 6 := by native_decide

/-- 5c4e: the card's five groups. -/
theorem card_5c4e_matches_study :
    cardRows 5 4 CARD54 = refGroups 5 4 ∧ overlap 5 4 CARD54 = 0 ∧ uncovered 5 4 CARD54 = 0 := by native_decide
/-- 5c4e: the card, the card with "time", "never", and Jay's 2 pairs with ARM 21 or 3+ pairs. -/
theorem policies_5c4e_matches_study : polRows 5 4 CARD54 BASE54 = refPolicies 5 4 := by native_decide

/-- 5c6e: the card's five groups. -/
theorem card_5c6e_matches_study :
    cardRows 5 6 CARD56 = refGroups 5 6 ∧ overlap 5 6 CARD56 = 0 ∧ uncovered 5 6 CARD56 = 0 := by native_decide
/-- 5c6e: the card, the card with "time", "never", and Jay's 3 pairs with ARM 21 or 4+ pairs. -/
theorem policies_5c6e_matches_study : polRows 5 6 CARD56 BASE56 = refPolicies 5 6 := by native_decide

/-- 6c6e: the card's three groups. -/
theorem card_6c6e_matches_study :
    cardRows 6 6 CARD66 = refGroups 6 6 ∧ overlap 6 6 CARD66 = 0 ∧ uncovered 6 6 CARD66 = 0 := by native_decide
/-- 6c6e: the card and "never". -/
theorem policies_6c6e_matches_study : polRows 6 6 CARD66 BASE_NEVER = refPolicies 6 6 := by native_decide

/-! ## The headline, with its numbers written out -/

def addRows (rs : List (List Nat)) : List Nat :=
  rs.foldl (fun acc r => List.zipWith (· + ·) acc r) (List.replicate 5 0)

/-- 4c4e has 70,560 states: 578 with a DR in 4 or less, 2,486 in 5, 10,512 in 6.
The card switches 18,312 of them (26.0%) and misses 0 of the 578, 132 of the 2,486 (5.3%) and 3,452 of the 10,512
(32.8%); 8,320 of its switches have no DR in 6.  2+ pairs switches 18,360 (26.0%) and misses 46 (8.0%), 508
(20.4%) and 4,500 (42.8%).  Fanti's pairs + ARM list switches 24,864 (35.2%) and misses 8, 144 and 2,840.  The card
with its two "time" groups switches 25,672 (36.4%) and misses 0, 84 and 2,132.
Over 4c4e, 4c2e, 3c2e and 7c8e together, each state once (111,104 states; 906 with a DR in 4 or less, 4,038 in 5,
17,208 in 6): the cards switch 29,984 and miss 0, 132 and 5,220; the pairs policies (2+ pairs, 1.5+ pairs, always,
and for 7c8e 5+ pairs counting edge ARM under 2 as a pair) switch 30,616 and miss 46, 516 and 6,364. -/
theorem card_headline :
    row 4 4 (fun _ => true) = [70560, 578, 2486, 10512, 28350, 28634] ∧
    pol 4 4 (cardSet CARD44 ["switch"]) = [18312, 0, 132, 3452, 8320] ∧
    pol 4 4 (fun f => f.pairs ≥ 2) = [18360, 46, 508, 4500, 9838] ∧
    pol 4 4 (fun f => f.pairs ≥ 2 || (f.pairs == 1 && armIs 21 f) || (f.pairs == 0 && (f.jzp || armIs 42 f))) =
      [24864, 8, 144, 2840, 14280] ∧
    pol 4 4 (cardSet CARD44 ["switch", "time"]) = [25672, 0, 84, 2132, 14312] ∧
    ((ALL.take 4).map fun (c, e, _, _) => (row c e fun _ => true).take 4).foldl
      (fun acc r => List.zipWith (· + ·) acc r) [0, 0, 0, 0] = [111104, 906, 4038, 17208] ∧
    addRows ((ALL.take 4).map fun (c, e, gs, _) => pol c e (cardSet gs ["switch"])) = [29984, 0, 132, 5220, 13184] ∧
    addRows ((ALL.take 4).map fun (c, e, _, base) => pol c e base[0]!.2) = [30616, 46, 516, 6364, 15390] ∧
    (ALL.take 4).map (fun (_, _, _, base) => base[0]!.1) = ["pairs", "pairs", "pairs", "pairs"] := by
  native_decide

end EOSwitch
