/-
  DRXs.Theorems2 — statements G to K, added 2026-11-13 to check the write-up's and the errata's corrections:
  the slice-EO rule against the stickers (G), the turns to a slice EO (H), the after-trigger counts and Simon's
  table (I), the printed examples of the errata and section 8 (J).  The 8fe renaming (section 6.3) is in
  DRXs/EightFeTheorems.lean (K).  All by `native_decide` except plain arithmetic (`decide`).
-/
import DRXs.Witness
import DRXs.SeoTheorems

namespace DRXs
open cube fecosets festeps aftertrigger edges witness

set_option maxHeartbeats 0

/-! ## G. The slice-EO rule, for every way an edge can sit -/

/-- Edge orientation for an axis does not depend on which of the other two axes is the reference: for every
edge place u, every piece t and both ways round, and each axis e. -/
theorem eo_reference_free : ∀ u ∈ fe.EDGES, ∀ t ∈ fe.EDGES, ∀ o ∈ [0, 1], ∀ e ∈ [0, 1, 2],
    goodWith e (ref e) (fe.cax (place1 u t o)) u = goodWith e (ref' e) (fe.cax (place1 u t o)) u := by
  native_decide

/-- It is edge orientation: a face turn keeps every edge's orientation for axis e, except a quarter turn of a face
of axis e, which turns over the four edges of that face. -/
theorem eo_moves : ∀ m ∈ NAMES, ∀ u ∈ fe.EDGES, ∀ t ∈ fe.EDGES, ∀ o ∈ [0, 1], ∀ e ∈ [0, 1, 2],
    good e (apply (place1 u t o) (MOVES m)) (posOf (MOVES m)[(fe.CUBIES u)[0]!]!) =
      (good e (place1 u t o) u ^^ flipsEdge m e u) := by
  native_decide

/-- **The slice-EO rule of seo_skip.py, exhaustively.**  For every edge place u (kind E, M or S), every piece t
and both ways round, and each axis e: the edge is bad for e exactly when
(bad for F/B) xor g_e(kind of u) xor g_e(kind of t), with seo_skip's `G` (g_UD = 1 on M, g_RL = 1 on E).
A configuration's slice EOs are read edge by edge, so the rule holds in all 70,963,200 configurations that
`seo_skip_counts` counts (and for every cube state). -/
theorem slice_eo_rule : ∀ u ∈ fe.EDGES, ∀ t ∈ fe.EDGES, ∀ o ∈ [0, 1], ∀ e ∈ [0, 1, 2],
    (!good e (place1 u t o) u) =
      ((!good 2 (place1 u t o) u) ^^ (seo_skip.G (axisName e) (kindOf u) == 1) ^^
        (seo_skip.G (axisName e) (kindOf t) == 1)) := by
  native_decide

/-- **The inverse side.**  On the inverse an edge keeps its orientation for every axis: if s has piece t at place
u, the inverse has piece u at place t, good for e exactly when the edge at u is in s.  (Checked on every
transposition of two edges and every edge flipped in place, both ways round each.)  With `slice_eo_rule` this is
seo_skip's "on inverse the roles of the kind of the place and the kind of the piece swap". -/
theorem eo_inverse : ∀ u ∈ fe.EDGES, ∀ t ∈ fe.EDGES, ∀ o ∈ [0, 1], ∀ o' ∈ [0, 1], ∀ e ∈ [0, 1, 2],
    good e (inverse (place2 u t o o')) t = good e (place2 u t o o') u := by
  native_decide

/-- seo_skip's place kinds are `kindOf` of the edge places. -/
theorem kinds_of_places : seo_skip.KIND = fe.EDGES.map kindOf := by native_decide

/-- (b) The average number of slice-EO skips: 1.125 on normal (1.13 on the page), 2.25 on normal and inverse, exactly 9/8 and 18/8 (exact sums over the
proved histograms: 79,833,600 and 159,667,200 skips over 70,963,200 configurations), and 20.6–20.7 % (printed 21 %) with none on
either side. -/
theorem seo_skip_average :
    (seo_skip.main ()).hist_both.foldl (fun a (k, c) => a + k * c) 0 = 159667200 ∧
    (seo_skip.main ()).hist_normal.foldl (fun a (k, c) => a + k * c) 0 = 79833600 := by
  rw [seo_skip_counts]; decide

theorem seo_skip_average_digits :
    159667200 * 4 = 70963200 * 9 ∧                               -- exactly 2.25 on both sides
    79833600 * 8 = 70963200 * 9 ∧                                -- exactly 1.125 on normal
    206 * 70963200 ≤ 14678928 * 1000 ∧ 14678928 * 1000 < 207 * 70963200 := by decide

/-! ## H. Turns to a slice EO for one slice (seo_dist.py) -/

/-- The E-slice pieces can sit 495 × 16 = 7,920 ways (placement and orientation), all reached. -/
theorem seo_dist_states : reachE.size = 7920 := by native_decide

/-- Fewest face turns to a slice EO of the E slice, over the 7,920: any axis, either flavour: 2550 / 3036 / 2334
at 0 / 1 / 2 (never more than 2); any axis, all oriented only: 1345 / 2022 / 4089 / 464 at 0 to 3 (3 moves:
464 = 5.9 %); F/B only, either: 990 / 1560 / 4852 / 518 (a skip 1 in 8); F/B only, oriented: 495 / 850 / 3740 /
2598 / 237 (a skip 1 in 16). -/
theorem seo_dist_hists :
    hist (distTo (goal [0, 1, 2] true)) = [(0, 2550), (1, 3036), (2, 2334)] ∧
    hist (distTo (goal [0, 1, 2] false)) = [(0, 1345), (1, 2022), (2, 4089), (3, 464)] ∧
    hist (distTo (goal [2] true)) = [(0, 990), (1, 1560), (2, 4852), (3, 518)] ∧
    hist (distTo (goal [2] false)) = [(0, 495), (1, 850), (2, 3740), (3, 2598), (4, 237)] := by
  native_decide

theorem seo_dist_digits : 990 * 8 = 7920 ∧ 495 * 16 = 7920 ∧
    585 * 7920 ≤ 464 * 10000 ∧ 464 * 10000 < 595 * 7920 := by decide

/-! ## I. After a trigger, and Simon's table -/

/-- Extra turns right after a side quarter turn, on the better side axis (the write-up's 4.3 table and its
"free for 209 of the 383 kinds of DR-2s and costs 3 for the rest"). -/
theorem after_trigger_better :
    hist ((kinds_with_slices 3).map (better · to2)) = [(0, 244)] ∧
    hist ((kinds_with_slices 2).map (better · to1)) = [(0, 209), (3, 174)] ∧
    hist ((kinds_with_slices 1).map (better · to0)) = [(0, 2), (3, 20), (4, 14), (5, 104)] ∧
    hist ((kinds_with_slices 2).map (better · to0)) = [(2, 2), (3, 32), (4, 31), (5, 128), (6, 112), (8, 78)] := by
  native_decide

/-- On the worse side axis DR-2s to DR-1s is free for 69. -/
theorem after_trigger_worse :
    hist ((kinds_with_slices 2).map (worse · to1)) = [(0, 69), (2, 140), (3, 150), (4, 24)] := by native_decide

/-- The 140 DR-1s kinds are 70 layouts on each of the two side axes; per layout 1, 2, 9, 30, 28 at 2 to 6 turns.
Sum of turns over the 140: 724 (mean 5.17); DR-2s 2614 / 383 (6.83); DR-3s 2074 / 244 (8.50). -/
theorem dr1s_layouts :
    (layouts 0).length = 70 ∧ (layouts 2).length = 70 ∧
    hist ((layouts 2).map turns_to_dr) = [(2, 1), (3, 2), (4, 9), (5, 30), (6, 28)] ∧
    hist ((layouts 0).map turns_to_dr) = [(2, 1), (3, 2), (4, 9), (5, 30), (6, 28)] ∧
    total ((kinds_with_slices 1).map turns_to_dr) = 724 ∧
    total ((kinds_with_slices 2).map turns_to_dr) = 2614 ∧
    total ((kinds_with_slices 3).map turns_to_dr) = 2074 := by native_decide

/-- **Simon's table (errata A1).**  With the last trigger move turned the other way when that is better, the 70
layouts need 2 to 6 turns: 1, 4, 13, 36, 16 — for a U trigger (the other way = the group U2) and, with a
different set of 13, for a D trigger (D2).  The two differ on 36 layouts. -/
theorem simon_count :
    hist ((layouts 2).map fun g => min (turns_to_dr g) (turns_after g "U2")) = [(2, 1), (3, 4), (4, 13), (5, 36), (6, 16)] ∧
    hist ((layouts 2).map fun g => min (turns_to_dr g) (turns_after g "D2")) = [(2, 1), (3, 4), (4, 13), (5, 36), (6, 16)] ∧
    ((layouts 2).filter fun g => turns_after g "U2" != turns_after g "D2").length = 36 := by native_decide

/-! ## J. The printed examples -/

/-- Errata A1's thirteen rows as printed in BUGS.md (flipped edges, turns as it is, turns with the last move the
other way, fix as it is). -/
def SIMON13 : List (List String × Nat × Nat × String) :=
  [(["BL", "DB", "UB", "FR"], 4, 5, "L2 F R L"),
   (["BL", "DB", "UF", "BR"], 4, 5, "D2 B R L"),
   (["BL", "DF", "UF", "FR"], 4, 5, "R2 B R L"),
   (["BL", "FL", "BR", "FR"], 4, 4, "F B R L"),
   (["FL", "DB", "UB", "BR"], 4, 5, "R2 F R L"),
   (["FL", "DF", "UB", "FR"], 4, 5, "D2 F R L"),
   (["FL", "DF", "UF", "BR"], 4, 5, "L2 B R L"),
   (["BL", "DB", "UB", "BR"], 5, 4, "R2 L2 F R L"),
   (["BL", "DB", "UF", "FR"], 5, 4, "L2 U2 F R L"),
   (["BL", "DF", "UB", "FR"], 5, 4, "L2 D2 F R L"),
   (["FL", "DB", "UF", "BR"], 5, 4, "D2 L2 B R L"),
   (["FL", "DF", "UB", "BR"], 5, 4, "U2 L2 B R L"),
   (["FL", "DF", "UF", "FR"], 5, 4, "U2 D2 F R L")]

/-- Every row checks with the last trigger move a U quarter turn (the other way = U2): the layout, both turn
counts, and the fix (it reaches a real DR in the printed number of turns), and these are 13 distinct layouts. -/
theorem simon13_rows_U : SIMON13.length = 13 ∧ SIMON13.all (rowOK "U2") = true := by native_decide

/-- With a D quarter turn as the last trigger move (the other way = D2) two rows change: BL DB UF BR and
FL DF UB FR take 3 turns after D2 (not 5), so for a D trigger they are 3-turn layouts and the thirteen 4-turn
layouts are a different set.  (Turns as it is, turns after D2) for each printed fix: -/
theorem simon13_rows_D : SIMON13.map (fun r => rowValues "D2" r.2.2.2) =
    [(4, 5), (4, 3), (4, 5), (4, 4), (4, 5), (4, 3), (4, 5), (5, 4), (5, 4), (5, 4), (5, 4), (5, 4), (5, 4)] := by
  native_decide

/-- **Errata B1** (and section 8): the printed scramble has all twelve edges bad on F/B and the F/B colours on the
U and D faces of every corner; as a DR-xs of the F/B colours it has 4 flipped edges and needs 2 slices (kind
table of colour 2, `colours`); its fewest turns to a real DR are 6, and the printed fix `U B F L U D` reaches a
real DR (F/B colours) in those 6 turns.  So it is a DR-2s, not a DR-1s. -/
theorem errata_B1 :
    let s := do_ SOLVED "B' D2 L2 U2 F2 D2 F L2 F2 D2 R2 F2 U' D' L' F' B' U'"
    fe.EDGES.all (fun p => !good 2 s p) = true ∧
    (match colours.sig_of 2 s 1 with
     | none => false
     | some g => g.flips.foldl (· + ·) 0 == 4 && colours.slices2 g == 2 && colours.turns_to_dr2 g == 6) = true ∧
    len "U B F L U D" = 6 ∧ isDRon (do_ s "U B F L U D") 2 = true := by native_decide

/-- The colour-2 kind table is as trustworthy as the U/D one: 768 kinds, no failed assert, the same slices
histogram, and the signature decides every transition over all reachable corner and edge colourings. -/
theorem colour2_kinds :
    colours.kinds2.length = 768 ∧ colours.explored2.failed = 0 ∧
    hist (colours.kinds2.map colours.slices2) = [(0, 1), (1, 140), (2, 383), (3, 244)] ∧
    colours.walk2 invariant.corner_places = (210, 0) ∧ colours.walk2 invariant.edge_places = (53760, 0) := by
  native_decide

/-- **Appendix A's `UB UF BR FR` row** (once errata B2, before the rework): the printed scramble is a DR-1s (corners on F/B) whose fewest turns to a real DR
are 6, and the printed fix reaches DR in 6. -/
theorem errata_B2_six :
    let s := do_ SOLVED "U R2 F2 D' B2 U2 L2 D R' L' B' L2 U2 F2"
    (match sig_of s 2 with
     | none => false
     | some g => slices g == 1 && turns_to_dr g == 6) = true ∧
    len "F2 U2 L2 B R L" = 6 ∧ isDRon (do_ s "F2 U2 L2 B R L") 1 = true := by native_decide

/-- **Section 5.4's wrong-slice DR-1s** (once errata B3, before the rework): the printed scramble has 8 edges bad on F/B, the four good ones the E-slice pieces, the U/D
colours on the F/B faces of every corner; it is a DR-1s whose flipped edges sit at BL BR FL FR and are the pieces
DB DF UF (M slice) and UR (S slice); its fewest turns to DR are 4 and `F B R L` does it. -/
theorem errata_B3 :
    let s := do_ SOLVED "U D2 L2 D B2 L2 B2 D R2 F2 U' R' L F' B'"
    (fe.EDGES.filter fun p => !good 2 s p).length = 8 ∧
    (fe.EDGES.filter fun p => good 2 s p).all (fun p => isE s[(fe.CUBIES p)[0]!]!) = true ∧
    (match sig_of s 2 with
     | none => false
     | some g => slices g == 1 && turns_to_dr g == 4 &&
         sameEdges ["BL", "BR", "FL", "FR"] (flippedAt g) &&
         sameEdges ["DB", "DF", "UF", "UR"] ((flippedAt g).map (pieceAt s))) = true ∧
    isDRon (do_ s "F B R L") 1 = true := by native_decide

/-- **Section 5.4's wrong-slice DR-1s, nissy's shortest DRs** (any axis, any face turns): on normal no DR within 3 turns and `F B R L`
is one in 4; on the inverse no DR within 5 turns and `B2 U' B2 U R L` is one in 6. -/
theorem errata_B3_nissy :
    let scr := "U D2 L2 D B2 L2 B2 D R2 F2 U' R' L F' B'"
    drWithin 3 (do_ SOLVED scr) 6 = false ∧ isDRany (do_ (do_ SOLVED scr) "F B R L") = true ∧
    drWithin 5 (do_ SOLVED (invSeq scr)) 6 = false ∧
    isDRany (do_ (do_ SOLVED (invSeq scr)) "B2 U' B2 U R L") = true := by native_decide

end DRXs
