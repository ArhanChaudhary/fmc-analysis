/-
  EOSwitch.RingsThm — part F of README.md (added 2026-11-13): the two-ring picture and the counts that do not count
  U and D turns, as checked statements about the definitions of `Rings.lean`.  Every one is proved by running it
  (`native_decide`, which trusts the Lean compiler; see README.md).

  The tables are compared with `RingsRef.lean`, which `gen_rings.py` copies from the research's output
  (`research/out/rings_lean_ref.json`), so no table entry is typed here.  A cell is [states, DR in ≤ 5, DR in ≤ 6
  ("sub-7"), DR in ≤ 7].  `rcell p` is the cell of the states whose record (`rg.Rec`) satisfies p.

  Reading aid.  Record fields: `c`, `e` the DRM (4c4e: c = 4, e = 4); `pairs`, `ep` (bad U/D edges with a pair),
  `earm`, `carm`, `side`, `jzp` as in Switch.lean; `sig` side turns; `q` the fewest quarter turns among the setups
  with `sig` side turns; for 4c4e, `hbar` half turns to two bars, `swaps` row swaps on the rings, `slot` slot type.
-/
import EOSwitch.Rings
import EOSwitch.RingsRef

namespace EOSwitch
open cube pieces sw rg

set_option maxHeartbeats 0

/-! ## F1. The picture -/

/-- The rings are the U/D layers: their edge places are the 8 U/D-layer edge places, their corner places the 8
corners, the slots the 4 E-slice places; U places have y = 1, D places y = −1.  Each ring corner k is next to ring
edges k and k + 1 (`NB`), and those two edge places have different zero axes, so a bad corner pairs with exactly
one of them: a hook is never 3, for any twist. -/
theorem ring_places :
    (UE.toList ++ DE.toList).mergeSort (fun a b => decide (a ≤ b)) = UD_PLACES ∧
    SL.toList.mergeSort (fun a b => decide (a ≤ b)) = E_SLOTS ∧
    (UC.toList ++ DC.toList).mergeSort (fun a b => decide (a ≤ b)) = List.range 8 ∧
    ([(UE, UC), (DE, DC)].all fun p => r4.all fun k =>
      (NB[(p.1)[k]!]!).contains (p.2)[k]! && (NB[(p.1)[(k + 1) % 4]!]!).contains (p.2)[k]! &&
      ZAX[(p.1)[k]!]! != ZAX[(p.1)[(k + 1) % 4]!]!) = true ∧
    (r4.all fun k => (EV UE[k]!)[1]! == 1 && (EV DE[k]!)[1]! == -1 && (CV UC[k]!)[1]! == 1 &&
      (CV DC[k]!)[1]! == -1) = true ∧
    ((UHT.toList ++ DHT.toList).all fun l => l.all fun v => v < 3) = true := by
  native_decide

/-- The compact numbers 0 … 1,082,564 are exactly the reached states (each is reached, and `dist_checked` counts
1,082,565 reached states), and their turn tables and distances are those of Switch.lean. -/
theorem compact_states : NC = 1082565 ∧ compactOk () = true := by native_decide

/-- On every one of the 1,082,565 states and each of the 14 EO-keeping turns, the picture after the turn is what
`expected` says: a U or D turn rotates that ring (edges and corners by the same step) and changes nothing else;
R2 L2 F2 B2 exchange the two rows of the face (`swapRows`) and its two E-slice places; R R' L L' follow the
quarter-turn rule (`quarter`). -/
theorem ring_turns : turnsOk () = true := by native_decide

/-- Different states have different pictures (both rings and the holes), so the picture is the state. -/
theorem ring_faithful : distinctOk () = true := by native_decide

/-- The record table: every state's record fits and survives packing, has at most 5 side turns, and its pairs
read off the rings are `feat`'s pairs; a 4c4e state has hbar ≤ 5, swaps ≤ 5, slot type ≤ 2.  The table holds every
state, with the distance histogram of Switch.lean. -/
theorem ring_records :
    recsOk () = true ∧
    rcell anyR = [le (total run.cells) 11, le (total run.cells) 5, le (total run.cells) 6, le (total run.cells) 7] ∧
    [([], rcell is44)] = split run.cells 4 4 (fun _ => []) := by
  native_decide

/-! ## F2. Side turns (U and D turns free) -/

/-- States by side turns 0 … 5: 1, 32, 2164, 111488, 914232, 54648, with their cells (sub-7: 1, 32, 2164, 34360,
27490, 56). -/
theorem side_turns :
    (List.range 6).map (fun s => rcell fun r => r.sig == s) = ringsref.SIGMA_CELLS ∧
    (List.range 6).map (fun s => (rcell fun r => r.sig == s)[0]!) = ringsref.SIGMA_HIST := by
  native_decide

/-- Every state with at most 2 side turns has a DR in at most 6 moves (2,197 states). -/
theorem side_turns_certain :
    certainOk () = true ∧ (rcell fun r => r.sig ≤ 2)[0]! = (rcell fun r => r.sig ≤ 2)[2]! := by
  native_decide

/-- Per DRM, the states by side turns. -/
theorem side_turns_by_drm :
    DRMS.map (fun p => (p.1, p.2, sigmaRows p.1 p.2)) = ringsref.SIGMA_DRM := by
  native_decide

/-- Per DRM, the states by (quarter turns, half turns) of the setups with the fewest side turns. -/
theorem profiles_by_drm :
    DRMS.map (fun p => (p.1, p.2, profileRows p.1 p.2)) = ringsref.PROFILES := by
  native_decide

/-- Per DRM, the card's groups split by short setup or not. -/
theorem cross_by_drm :
    CARDS.map (fun p => (p.1, p.2.1)) = DRMS ∧
    CARDS.map (fun p => (p.1, p.2.1, crossRows p.1 p.2.1 p.2.2)) = ringsref.CROSS := by
  native_decide

/-! ## F3. 4c4e: row swaps on the rings, and half turns to two bars -/

/-- The row-swap table over ring-pair codes passes `search.ruleHolds`, so an entry is the fewest row swaps to a bar
in each ring; among the codes with an entry, 0 is exactly "a bar in each ring"; 780 codes have an entry, and they
are the 780 ring pairs of the 4c4e states: 1, 12, 95, 392, 268, 12 of them at 0 … 5 swaps. -/
theorem ring_swaps_checked :
    search.ruleHolds (1296 * 1296) GOALP (List.range 16) rstep RD = true ∧
    barsOk () = true ∧ reachedCount () = 780 ∧ RPT.size = 780 ∧
    (RPT.all fun g => search.reached RD g.1) = true ∧
    (List.range 6).map (fun s => (RPT.filter fun g => swapsOf g.1 == s).size) = ringsref.RING_CLASSES_HIST := by
  native_decide

/-- For every 4c4e state (70,560): half turns to two bars = max(row swaps of its ring pair, slot type). -/
theorem half_turns_to_bars : hbarOk () = true := by native_decide

/-- 4c4e by half turns to two bars 0 … 5. -/
theorem bands_4c4e :
    (List.range 6).map (fun h => rcell fun r => is44 r && r.hbar == h) = ringsref.H_BANDS := by
  native_decide

/-- 4c4e by row swaps and slot type. -/
theorem swaps_slot_4c4e :
    ((List.range 6).flatMap fun a => (List.range 3).map fun t =>
      [a, t] ++ rcell (fun r => is44 r && r.swaps == a && r.slot == t)) = ringsref.SWAPS_SLOT := by
  native_decide

/-- 4c4e by pairs and half-turn group (≤ 1, 2, 3, ≥ 4). -/
theorem pairs_bands_4c4e :
    occur 2 ((List.range 5).flatMap fun p => (List.range 4).map fun g =>
      [p, g] ++ rcell (fun r => is44 r && r.pairs == p && hGroup4 g r)) = ringsref.PAIRS_H := by
  native_decide

/-- The groups of the paired-edge card for 4c4e, split by half-turn group (≤ 2, 3, ≥ 4). -/
theorem card_split_4c4e :
    occur 2 ((List.range 3).flatMap fun ci => (List.range 3).map fun g =>
      [ci, g] ++ rcell (fun r => is44 r && card44 ci r && hGroup3 g r)) = ringsref.CARD_SPLIT := by
  native_decide

/-- 4c4e with 3 half turns to two bars, by pairs, side pairs, edge ARM and paired edges. -/
theorem inside3_4c4e :
    let h3 := fun r : Rec => is44 r && r.hbar == 3
    (List.range 4).map (fun p => rcell fun r => h3 r && r.pairs == p) = ringsref.INSIDE3_PAIRS ∧
    [rcell (fun r => h3 r && r.side == 0), rcell (fun r => h3 r && r.side == 1),
     rcell (fun r => h3 r && r.side ≥ 2)] = ringsref.INSIDE3_SIDE ∧
    [rcell (fun r => h3 r && r.earm == 1), rcell (fun r => h3 r && r.earm != 1)] = ringsref.INSIDE3_EARM1 ∧
    (List.range 3).map (fun e => rcell fun r => h3 r && r.ep == e) = ringsref.INSIDE3_EDGES_PAIRED := by
  native_decide

/-! ## F4. Reading the row swaps by hand -/

/-- Over the 780 ring pairs × 16 row swaps, a row swap changes the number of pairs by −2 … 2 (104, 1984, 8388, 1912,
92 times), so by at most 2; every ring pair has 2 · swaps + pairs ≥ 4, i.e. swaps ≥ ⌈(4 − pairs)/2⌉, and 4 pairs
give at most 1 swap; the number of ring pairs per (pairs, swaps). -/
theorem pair_change :
    ([-2, -1, 0, 1, 2] : List Int).map (fun d => (d, (pairDeltas ()).count d)) = ringsref.PAIR_CHANGE ∧
    (pairDeltas ()).length = 780 * 16 ∧ (ringsref.PAIR_CHANGE.map fun p => p.2).sum = 780 * 16 ∧
    pairBoundOk () = true ∧ pairsSwapsClasses () = ringsref.PAIRS_SWAPS_CLASSES := by
  native_decide

/-- On every ring pair with 3 pairs: swaps = 1 + [the unpaired corner is in the layer of the edge that lacks a
corner] + [a bad piece in the two places behind it] + [both bad edges in one layer and opposite each other]; with
the states and sub-7 states of each combination. -/
theorem three_pair_rule : threeOk () = true ∧ threeRows () = ringsref.THREE_RULE := by native_decide

/-- The ring pairs with at most 2 row swaps, up to exchanging the layers and mirroring, are exactly the 33 pairs of
strings of the research's list, with its swaps, pairs, states and sub-7 states. -/
theorem patterns_le2 :
    (ringsref.PATTERNS.all fun p => validString p.1 && validString p.2.1) = true ∧
    patternsLean () = patternsOf ringsref.PATTERNS ∧ (patternsLean ()).length = 33 := by
  native_decide

end EOSwitch
