/-
  Corrections.Examples — the published corrections (report/BUGS.md of each study) whose example is a scramble or
  DR state with lengths that come from tables a Lean certificate of the project already proves:

  * DRBound (judging-a-dr): `exactDist g`, the optimal DR-move finish of every DR state (`exact_optimal`).
  * HTRRoutes (htr-routes): the shortest linear DR → HTR of every HTR coset (the BFS of `cosets.run`, checked by
    `search.ruleHolds` in `htr48_matches_study`), the subset names, and α of a corner path.
  * EOSwitch (eo-switch): the EO-kept distance to DR of every F/B-EO state (`dist`, checked by `dist_checked`) and
    the features (ARM, pairs).
  * EODR (eo-to-dr): bad-edge masks on each axis; with `eo_by_bad` (12 bad edges need 7 turns to EO).

  For each such example: the state has the stated optimum, and the printed solution is valid (replayed) and has
  the stated length.  Conventions: "scramble then solution"; a NISS part in brackets is done on the inverse, i.e.
  its inverse is done before the scramble.  Every move token is checked to be one of the model's move names.
-/
import Corrections.DRTable
import HTRRoutes.Cosets
import HTRRoutes.Corners
import EOSwitch.Model
import EODR.Pieces
import FakeBound.Counter

namespace Corrections

set_option maxHeartbeats 0

/-- The inverse of a move sequence (as text). -/
def invSeq (s : String) : String :=
  " ".intercalate (((s.splitOn " ").filter (· != "")).reverse.map fun t =>
    if t.endsWith "'" then (t.dropEnd 1).toString else if t.endsWith "2" then t else t ++ "'")

def ntok (s : String) : Nat := ((s.splitOn " ").filter (· != "")).length

/-! ## 1. Optimal DR finishes (DRBound's exact table) -/

/-- `exactDist` is the table entry; the table is `Exact.tableValues 18` (the same `mkTable 18`). -/
theorem exactDist_eq_tableValues (gs : List DRBound.State) :
    gs.map DRBound.exactDist = DRBound.Exact.tableValues 18 gs := rfl

theorem dr_parse_ok :
    (drOptima.all fun c => (drMoves? c.2.1).isSome) ∧
    (drSolutions.all fun c => (drMoves? c.2.1).isSome && (drMoves? c.2.2).isSome) := by native_decide

/-- From the list equality to each entry. -/
theorem entries {l : List (String × String × Nat)}
    (h : l.map (fun c => DRBound.exactDist (drState c.2.1)) = l.map (·.2.2)) :
    ∀ c ∈ l, DRBound.exactDist (drState c.2.1) = c.2.2 := by
  induction l with
  | nil => intro c hc; cases hc
  | cons a l ih =>
    intro c hc
    simp only [List.map_cons, List.cons.injEq] at h
    rcases List.mem_cons.mp hc with rfl | hc
    · exact h.1
    · exact ih h.2 c hc

theorem map_exactDist (l : List (String × String × Nat)) :
    l.map (fun c => DRBound.exactDist (drState c.2.1))
      = DRBound.Exact.tableValues 18 (l.map fun c => drState c.2.1) := by
  rw [← exactDist_eq_tableValues, List.map_map, Function.comp_def]

theorem dr_values : drOptima.map (fun c => DRBound.exactDist (drState c.2.1)) = drOptima.map (·.2.2) := by
  have h := dr_table_lookup
  rw [← map_exactDist] at h
  exact h

/-- **Every DR optimum in the corrections is right**: for each example, every DR-move solution of the state has at
least the stated number of moves, and one has exactly that many. -/
theorem dr_optima_correct : ∀ c ∈ drOptima,
    (∃ w : List DRBound.Move, w.length = c.2.2 ∧ (drState c.2.1).apply w = DRBound.solved) ∧
    (∀ w : List DRBound.Move, (drState c.2.1).apply w = DRBound.solved → c.2.2 ≤ w.length) := by
  intro c hc
  have hv := entries dr_values c hc
  obtain ⟨hval, hpar⟩ := DRBound.reachable_good (drMoves c.2.1)
  obtain ⟨h1, h2⟩ := DRBound.exact_optimal (drState c.2.1) hval hpar
  rw [hv] at h1 h2
  exact ⟨h1, h2⟩

/-- **The printed solutions solve their scrambles**, with the stated lengths (13, 12, 12, 14, 7). -/
theorem dr_solutions_valid :
    (drSolutions.all fun c => (drState c.2.1).apply (drMoves c.2.2) == DRBound.solved) ∧
    drSolutions.map (fun c => (drMoves c.2.2).length) = [13, 12, 12, 14, 7] := by native_decide

/-! ## 2. HTR lengths and subset names (HTRRoutes) -/

section htr
open HTRRoutes HTRRoutes.pieces HTRRoutes.corners

def validSeq (s : String) : Bool := (cube.parse s).all fun t => cube.NAMES.contains t
def stOf (s : String) : cube.State := cube.do_ cube.SOLVED s
/-- The HTR coset of a sticker state (as in `cosets`). -/
def cosetOf (s : cube.State) : Nat := cosets.cid (rank (corners s)) * 256 + mMask (edges s)
/-- The BFS of `cosets.run`: shortest linear DR → HTR of every coset. -/
def HTRD : ByteArray := search.bfs cosets.N [cosets.GOAL] (List.range 10) (cosets.stepWith cosets.CCM cosets.MM)
/-- Shortest linear HTR of the state of scramble s on normal, and on inverse. -/
def htrLen (scr : String) : Nat × Nat :=
  ((HTRD.get! (cosetOf (stOf scr))).toNat, (HTRD.get! (cosetOf (stOf (invSeq scr)))).toNat)
def inHTR (s : cube.State) : Bool := cosetOf s == cosets.GOAL
def lab48 (scr : String) : String := (cosets.scrambleLabels scr).1
def lab (scr : String) : String := (cosets.scrambleLabels scr).2.1

/-- The BFS behind `htrLen` passes the same independent check as in `htr48_matches_study`. -/
theorem htr_table_checked : search.ruleHolds cosets.N (· == cosets.GOAL) (List.range 10)
    (cosets.stepWith cosets.CCM cosets.MM) HTRD = true := by native_decide

/-- **judging-a-dr B1** ("13, not 12"; both 0c3 4e) and **htr-routes c** (0c3 4e, 13 on either side). -/
theorem htr_13 :
    htrLen "U' R2 D' B2 U B2 U' R2 U F2 U' F2 U" = (13, 12) ∧
    lab48 "U' R2 D' B2 U B2 U' R2 U F2 U' F2 U" = "0c3 4e" ∧
    htrLen "D B2 D' B2 D L2 U L2 U' F2 D B2 U' F2" = (13, 13) ∧
    lab48 "D B2 D' B2 D L2 U L2 U' F2 D B2 U' F2" = "0c3 4e" ∧
    htrLen "B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U" = (13, 13) ∧
    lab48 "B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U" = "0c3 4e" ∧
    -- the printed 13-move linear HTR, on the normal side
    inHTR (stOf "B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U U R2 U B2 U' B2 U F2 U' R2 U B2 U") = true ∧
    -- the printed 12-move NISS HTR: (B2 U L2 U) on inverse = its inverse before the scramble
    inHTR (stOf (invSeq "B2 U L2 U" ++ " B2 U B2 R2 D' L2 U B2 D' F2 D' L2 F2 U' R2 U U R2 U2 F2 U' F2 R2 U"))
      = true := by native_decide

/-- **htr-routes b**: the 4c4 0e (Mallard's name; 14-name label below) has a 10-move linear HTR on the inverse,
the printed one is valid, and the one subset whose shortest linear HTR is never below 11 is 0c4 8e (minimum over
its cosets 11; 4c4 0e has 10). -/
theorem htr_4c4 :
    lab48 "D F2 R2 U2 B2 U' F2 U' F2 U L2 B2 U' R2 U'" = "4c4 0e" ∧
    (htrLen "D F2 R2 U2 B2 U' F2 U' F2 U L2 B2 U' R2 U'").2 = 10 ∧
    inHTR (stOf (invSeq "D F2 R2 U2 B2 U' F2 U' F2 U L2 B2 U' R2 U'" ++ " D R2 U R2 B2 U2 B2 U B2 U")) = true ∧
    (let shortest := fun (s : String) => ((cosets.run.table.filter (·.1 == s)).map (·.2.1)).foldl min 99
     shortest "4c4 0e" = 10 ∧ shortest "0c4 8e" = 11 ∧
     ((cosets.run.table.map (·.1)).eraseDups.filter fun s => shortest s ≥ 11) = ["0c4 8e"]) := by
  native_decide

/-- **judging-a-dr A1, B2, B4, B5** subset names; **B4** both 2c4 4e and 7 to HTR on both sides. -/
theorem labels_judging :
    lab48 "U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2" = "2c3 6e" ∧
    lab48 "F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'" = "0c3 4e" ∧
    lab48 "R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'" = "2c5 4e" ∧
    lab48 "U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'" = "2c5 0e" ∧
    lab48 "F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'" = "0c0 8e" ∧
    lab48 "D F2 U' F2 D B2 D'" = "2c4 4e" ∧
    lab48 "D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'" = "2c4 4e" ∧
    htrLen "D F2 U' F2 D B2 D'" = (7, 7) ∧
    htrLen "D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'" = (7, 7) ∧
    lab "F2 D2 B2 R2 U' F2 R2 B2 R2 U' F2 L2 D2 R2 D U'" = "4b2 4e" ∧
    lab "R2 U L2 D F2 L2 B2 D2 B2 U' B2 U' R2 F2 R2 U'" = "2c3 4e" ∧
    lab "R2 U2 B2 L2 F2 L2 D2 F2 R2 U' B2 F2 L2 R2 U' R2 D'" = "4a1 4e" := by native_decide

/-- **htr-routes a, d, e, f** subset names. -/
theorem labels_htr_routes :
    lab "R2 D R2 F2 R2 D L2 D B2 R2 D2 B2 U" = "4b2 2e" ∧
    lab "F2 U' L2 U' F2 R2 F2 L2 U F2 D2 B2" = "2c3 2e" ∧
    lab "R2 B2 D2 B2 D U2 R2 U L2 F2 U' B2" = "2c3 2e" ∧
    lab "D2 F2 L2 U' B2 U' L2 U2 B2 U' L2 D R2 D2" = "0c4 0e" ∧
    lab "F2 U' B2 R2 B2 U R2" = "0c0 2e" := by native_decide

/-- The corner subsets of the state of `scr` after each quarter turn of `sol` (and at the start). -/
def cornerPath (scr sol : String) : List String := Id.run do
  let mut s := stOf scr
  let mut path := [NAMES[sub (rank (corners s))]!]
  for t in cube.parse sol do
    s := cube.do_ s t
    if !(t.endsWith "2") then path := path ++ [NAMES[sub (rank (corners s))]!]
  return path

/-- Lengths of the half-turn sections between the quarter turns of a DR sequence. -/
def sections (sol : String) : List Nat :=
  (cube.parse sol).foldl (fun acc t => if t.endsWith "2" then acc.dropLast ++ [acc.getLast! + 1] else acc ++ [0]) [0]

/-- **htr-routes f, the index example, end to end**: the 0c4 0e's optimal finish (14, `dr_optima_correct`)
follows the corner path 0c4 > 4a3 > 4b2 > 4a1 > 0c0, whose α (computed from the cube) is 0, 1, 3, 1, 0; its
sections are 2, 1, 3, 1, 3 and they satisfy s ≥ α; its four 1q reductions are 10, 9, 9, 9 (FakeBound's `red`).
With S = {0, 2, 3} and R' = 9, T11503's first bound with α_i (α_2 = 3) claims 2·14 ≥ 3·10 - 4 + 3 = 29, false;
with α_{i+1} (α_3 = 1) it is 28 ≥ 27, true. -/
theorem index_example :
    let scr := "D2 F2 L2 U' B2 U' L2 U2 B2 U' L2 D R2 D2"
    let sol := "D2 R2 D' L2 U B2 U2 L2 U B2 U L2 F2 D2"
    cornerPath scr sol = ["0c4", "4a3", "4b2", "4a1", "0c0"] ∧
    alphaOf HT (parsePath "0c4 > 4a3 > 4b2 > 4a1 > 0c0") = ([0, 1, 3, 1, 0], true) ∧
    sections sol = [2, 1, 3, 1, 3] := by native_decide

theorem index_example_arith :
    let s := FakeBound.ofL [2, 1, 3, 1, 3]
    (List.range 4).map (FakeBound.red 4 s) = [10, 9, 9, 9] ∧ FakeBound.len 4 s = 14 ∧
    ¬ ((3 : Int) * (9 + 1) - 4 + 3 ≤ (3 - 1) * 14) ∧ ((3 : Int) * (9 + 1) - 4 + 1 ≤ (3 - 1) * 14) := by decide

/-- **htr-routes f, the C example**: the 0c0 2e's 7-move optimal read as `R2 U'` on normal and `(F2 U' B2 R2 B2)`
on inverse is in HTR after 4 moves (`R2 U'` and the first two inverse moves `F2 U'`), and the shortest linear HTR
of the subset 0c0 2e is 5. -/
theorem C_example :
    inHTR (stOf (invSeq "F2 U'" ++ " F2 U' B2 R2 B2 U R2 R2 U'")) = true ∧
    (let shortest := fun (s : String) => ((cosets.run.table.filter (·.1 == s)).map (·.2.1)).foldl min 99
     shortest "0c0 2e" = 5) := by native_decide

/-- **judging-a-dr A2/A3**: the printed any-move solutions solve their states (18 face turns, sticker model).
Their optimality (6 and 8 with all 18 moves) is not from a Lean table. -/
theorem any_move_solutions_valid :
    ([("R L' B2 D2 R L'", "L R' D2 B2 L R'"), ("F' B R2 D2 F B'", "B F' D2 R2 B' F"),
      ("R D2 F2 B2 R' L F2 R'", "R F2 L' R B2 F2 D2 R'"), ("F L2 F B' R2 L2 D2 F'", "F D2 L2 R2 B F' L2 F'"),
      ("L' F2 R L' F2 B2 D2 L", "L' D2 B2 F2 L R' F2 L")].all fun (a, b) =>
        validSeq a && validSeq b && stOf (a ++ " " ++ b) == cube.SOLVED) = true := by native_decide

/-- **judging-a-dr B3**: (4!)⁴/12 = 27648. -/
theorem arith_B3 : (24 ^ 4) / 12 = 27648 ∧ (24 ^ 4) % 12 = 0 := by decide

end htr

/-! ## 3. EO-kept distance to DR (EOSwitch) -/

section eo
open EOSwitch

def eoValid (s : String) : Bool := (cube.parse s).all fun t => cube.NAMES.contains t
/-- EO-keeping turns only (U D R L quarter or half, F2, B2). -/
def keepsFB (s : String) : Bool := (cube.parse s).all fun t =>
  ["U", "U2", "U'", "D", "D2", "D'", "R", "R2", "R'", "L", "L2", "L'", "F2", "B2"].contains t
/-- [bad corners, 2·bad U/D edges, carm, earm, pairs, fake pairs, side pairs, EO-kept distance to DR]. -/
def vals (s : String) : List Nat := exValues (exState true s)
/-- F/B EO solved on the sticker state (every edge good for F/B). -/
def fbEO (s : String) : Bool := pieces.badMask 2 (exState true s) == 0

/-- Relabel the faces by a rotation (R→F, L→B, F→U, B→D, U→R, D→L: x→z→y→x, a proper rotation). -/
def rotA (s : String) : String := " ".intercalate ((cube.parse s).map fun t =>
  let f := t.take 1
  let r := t.drop 1
  let g := match f.toString with
    | "R" => "F" | "L" => "B" | "F" => "U" | "B" => "D" | "U" => "R" | "D" => "L" | x => x
  g ++ r.toString)
/-- Relabel by the rotation R→U, L→D, U→L, D→R, F→F, B→B (about the F/B axis, proper). -/
def rotB (s : String) : String := " ".intercalate ((cube.parse s).map fun t =>
  let f := t.take 1
  let r := t.drop 1
  let g := match f.toString with
    | "R" => "U" | "L" => "D" | "U" => "L" | "D" => "R" | x => x
  g ++ r.toString)

/-- **The three EO-switch examples (once its errata a, b, c)**: features and EO-kept distance to DR of the three examples, and the printed DRs are
valid (EO-keeping turns, distance 0 afterwards) with the stated lengths.
a: 4c4e, ARM 41 (carm 4, earm 1), 2 pairs (and 1 fake pair), 5.  b: 4c2e, 2 pairs, 6.  c: 4c4e, ARM 21, 1 pair, 6. -/
theorem eo_switch_examples :
    vals "L' U' B2 F2 U'" = [4, 4, 4, 1, 2, 1, 0, 5] ∧
    vals "L' U' B2 F2 U' U F2 B2 U L" = [0, 0, 0, 0, 0, 0, 0, 0] ∧ keepsFB "U F2 B2 U L" ∧
    (vals "R' D2 R F2 D' U'").take 2 = [4, 2] ∧ (vals "R' D2 R F2 D' U'")[4]! = 2 ∧
    (vals "R' D2 R F2 D' U'")[7]! = 6 ∧
    (vals "R' D2 R F2 D' U' U D F2 R' D2 R")[7]! = 0 ∧ keepsFB "U D F2 R' D2 R" ∧
    (vals "L' B2 D' L2 D' U2").take 5 = [4, 4, 2, 1, 1] ∧ (vals "L' B2 D' L2 D' U2")[7]! = 6 ∧
    (vals "L' B2 D' L2 D' U2 U2 D L2 D B2 L")[7]! = 0 ∧ keepsFB "U2 D L2 D B2 L" := by native_decide

/-- The shortest EO-kept DR of each 4c4e ARM set (carm, earm), over all 70,560 4c4e states of the table:
eo-switch a's list "00:1, 01:5, 02:6, 10:4, 11:4, 12:6, 20:5, 21:2, 22:5, 30:6, 31:4, 32:4, 40:6, 41:5, 42:3",
so 11 sets have a case of 5 or less (Jay's list of 10 leaves out 41) and 7 have one of 4 or less. -/
def armMin : List (Nat × Nat × Nat) := Id.run do
  let mut best : Array Nat := Array.replicate 25 99
  for x in [0:sw.N] do
    let d := (sw.dist.get! x).toNat
    if d == 255 then continue
    let f := sw.feat (x / 4096) (x % 4096)
    if f.c == 4 && f.e == 4 then
      best := best.modify (f.carm * 5 + f.earm) (min d)
  return ((List.range 25).filter (fun i => best[i]! != 99)).map fun i => (i / 5, i % 5, best[i]!)

theorem arm_sets :
    armMin = [(0, 0, 1), (0, 1, 5), (0, 2, 6), (1, 0, 4), (1, 1, 4), (1, 2, 6), (2, 0, 5), (2, 1, 2), (2, 2, 5),
      (3, 0, 6), (3, 1, 4), (3, 2, 4), (4, 0, 6), (4, 1, 5), (4, 2, 3)] ∧
    (armMin.filter (·.2.2 ≤ 5)).length = 11 ∧ (armMin.filter (·.2.2 ≤ 4)).length = 7 := by native_decide

/-- **eo-to-dr 1**: scramble + EO `D L' B R` (on R/L) leaves 3c8e for DR on F/B, and the shortest EO-kept DR is 10;
the printed one is valid.  Checked after the rotation `rotA` (R/L → F/B, F/B → U/D), which keeps lengths.
**eo-to-dr 3**: the 4c6e (EO `U B' R F'` on F/B, DR on R/L) is 8 from DR keeping EO; the printed DR is valid
(checked after `rotB`: R/L → U/D). -/
theorem eo_to_dr_examples :
    let a := "U2 B2 U' R2 U F2 U2 R2 B2 F2 R2 B2 U2 L' B D' U' L' R' F' L2 F' D L' B R"
    let b := "U B2 R2 U' R2 U B2 D' F2 R2 U L2 F2 L' U' R' F2 D F' R B R U' U B' R F'"
    eoValid a && eoValid b &&
    fbEO (rotA a) && (vals (rotA a)).take 2 == [3, 8] && (vals (rotA a))[7]! == 10 &&
    (vals (rotA (a ++ " F2 U F B' D B L2 F' L2 D")))[7]! == 0 &&
    keepsFB (rotA "F2 U F B' D B L2 F' L2 D") && ntok "F2 U F B' D B L2 F' L2 D" == 10 &&
    fbEO (rotB b) && (vals (rotB b)).take 2 == [4, 6] && (vals (rotB b))[7]! == 8 &&
    (vals (rotB (b ++ " F2 D2 L' B2 R' U' R2 D")))[7]! == 0 &&
    keepsFB (rotB "F2 D2 L' B2 R' U' R2 D") && ntok "F2 D2 L' B2 R' U' R2 D" == 8 := by native_decide

end eo

/-! ## 4. Superflip EO (EODR) -/

section sf
open EODR

/-- **eo-to-dr 2**: the superflip has 12 bad edges on every axis, so by EODR's `eo_by_bad` (12 bad: 7 turns) its
linear EO needs 7 turns on every axis; the printed 7-move NISS EO `D F U' (L B R U')` gives EO on U/D (axis 1).
That no NISS EO of 6 exists follows from `EODR.superflip_niss_eo` (eo-to-dr/lean/EODR): the superflip commutes
with every face turn and its linear EO needs 7 on every axis; the last step is the one-line argument in its docstring. -/
theorem superflip :
    let sf := "U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2"
    ((List.range 3).map fun Y => pieces.popcount (pieces.badMask Y (cube.do_ cube.SOLVED sf))) = [12, 12, 12] ∧
    pieces.badMask 1 (cube.do_ cube.SOLVED (invSeq "L B R U'" ++ " " ++ sf ++ " D F U'")) = 0 := by
  native_decide

end sf

end Corrections
