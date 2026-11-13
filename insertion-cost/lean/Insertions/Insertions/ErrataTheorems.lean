import Insertions.Search
import Insertions.PyMoves
/-
  The examples of the corrections page (report/BUGS.md, A1 to A3), replayed from the printed text and their optima
  recomputed by brute force over every alg of 8 moves or fewer (`Search.lean`).

  The strings are copied from research/src/report_build/wit_typical_2c2c_twisted.md, wit_typical_2c2c_pure.md,
  wit_typical_3c1t.md (A1), wit_skip.md (A2) and wit_fivec19.md (A3), which the page includes word for word.
-/
namespace Insertions
namespace ins
open cube

/-- The 18 face turns built from geometry are, number for number, the ones cube.py builds (the model every
solution in the study is replayed on). -/
theorem moves_agree_with_python : MOVES_TABLE = PY_MOVES := by native_decide

/-! ## The alg list it all rests on -/

/-- Every corner-only alg of at most 8 moves: 864 sequences, all of exactly 8 moves, every one a corner 3-cycle
(type `[(3, 0)]`); they do 528 different things, 192 of them with one alg and 336 with two. -/
theorem corner_algs_up_to_8 :
    cornerAlgs.size = 864 ∧ cornerAlgs.all (·.length == 8) ∧
    cornerAlgs.all (fun a => cornerType (stateOf a) == [(3, 0)]) ∧
    (byState cornerAlgs).size = 528 ∧
    ((byState cornerAlgs).toList.filter (·.2.size == 1)).length = 192 ∧
    ((byState cornerAlgs).toList.filter (·.2.size == 2)).length = 336 := by native_decide

/-! ## A1: a typical skeleton of each type -/

def A1_twisted_scramble := "R' U' F L B2 L B2 F2 U2 L B2 U2 B2 R' D2 F' R B' U2 F R2 U' R U R' U' F"
def A1_twisted_block := [
  "U' R2 F2 D' R' D' B R' U2 B' L' U F L' D2 * B D2 R2 B' R2",
  "* = U' B D' B' U B D B' // (8-3/25)",
  "U' R2 F2 D' R' D' B R' U2 B' L' U F L' U' D2 B D' ^ B' U B D' R2 B' R2",
  "^ = D B U2 B' D' B U2 B' // (8-4/29)",
  "Solution: U' R2 F2 D' R' D' B R' U2 B' L' U F L' U' D2 B2 U2 B' D' B U2 B2 U B D' R2 B' R2 (29)"]

def A1_pure_scramble := "R' U' F B2 U2 L2 B2 L2 D' L2 D B2 D2 F2 U2 L R2 U' B' D' L B F R2 D R' U' F"
def A1_pure_block := [
  "U' D2 B' D2 B' D L2 U R2 B' U2 ^ D B L D * B' U2 L' D' L'",
  "* = D F2 D' B' D F2 D' B // (8-3/25)",
  "^ = F' D B D' F D B' D' // (8-4/29)",
  "Solution: U' D2 B' D2 B' D L2 U R2 B' U2 F' D B D' F D L D2 F2 D' B' D F2 U2 D' L' D' L' (29)"]

def A1_3c1t_scramble := "R' U' F B2 L F2 L' D2 R' F2 U2 R2 U2 L F2 R' U' L F R' U2 B' R D2 L U' R' U' F"
def A1_3c1t_block := [
  "L' B' D2 R D R' B' R2 U2 F R2 U2 D' L2 F2 * U' L' D2 B2 U'",
  "* = F D' F' U' F D F' U // (8-3/25)",
  "L' B' D2 R D R' B' R2 U2 F R2 U2 D' L2 F' D' F' U' ^ F D F' L' D2 B2 U'",
  "^ = U F' U' B U F U' B' // (8-3/30)",
  "Solution: L' B' D2 R D R' B' R2 U2 F R2 U2 D' L2 F' D' F2 U' B U F U' F B' D F' L' D2 B2 U' (30)"]

/-- The skeleton of a block: its first line without the marks. -/
def skel (b : List String) : List Nat := (marked b[0]!).1

/-- The three A1 blocks replay as printed: each skeleton has 20 moves and leaves what the page says (twisted
2c2c "DFL ↔ UFR, DBR ↔ DFR", each swap with a twist; pure 2c2c "DFL ↔ DFR, DBR ↔ UFR", no twist; 3c1t
"DFL → UFL → UBR → DFL, DBL twisted clockwise", the 3-cycle twisted), every comm is an 8-move corner-only alg
with the printed cancel and length, and the solutions (29, 29, 30) solve the scrambles. -/
theorem A1_blocks_replay :
    checkBlock A1_twisted_scramble A1_twisted_block "DFL ↔ UFR, DBR ↔ DFR" ∧
    checkBlock A1_pure_scramble A1_pure_block "DFL ↔ DFR, DBR ↔ UFR" ∧
    checkBlock A1_3c1t_scramble A1_3c1t_block "DFL → UFL → UBR → DFL, DBL twisted clockwise" ∧
    (skel A1_twisted_block).length = 20 ∧ (skel A1_pure_block).length = 20 ∧ (skel A1_3c1t_block).length = 20 ∧
    cornerType (stateOf (word A1_twisted_scramble ++ skel A1_twisted_block)) = [(2, 2), (2, 1)] ∧
    cornerType (stateOf (word A1_pure_scramble ++ skel A1_pure_block)) = [(2, 0), (2, 0)] ∧
    cornerType (stateOf (word A1_3c1t_scramble ++ skel A1_3c1t_block)) = [(3, 2), (1, 1)] := by native_decide

/-- "Best with two 8-move comms: 29 / 29 / 30": no two algs of 8 moves or fewer, at any spots, nested or not,
give anything shorter on these three skeletons. -/
theorem A1_best_two :
    (best2 cornerAlgs (byState cornerAlgs) (word A1_twisted_scramble) (skel A1_twisted_block)).1 = 29 ∧
    (best2 cornerAlgs (byState cornerAlgs) (word A1_pure_scramble) (skel A1_pure_block)).1 = 29 ∧
    (best2 cornerAlgs (byState cornerAlgs) (word A1_3c1t_scramble) (skel A1_3c1t_block)).1 = 30 := by native_decide

/-! ## A2: checking every other move -/

def A2_scramble := "R' U' F R U2 F2 D2 R' U2 F2 R' F2 L2 R F2 R U R F' L2 B U2 F' L F' R' U' F"
def A2_block := [
  "F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' F' B * U2 B' L D",
  "* = F D F' U F D' F' U' // (8-3/25)",
  "Solution: F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' B D F' U F D' F' U B' L D (25)"]
def A2_spots : List (Option (Nat × Nat)) :=
  perSpot (byState cornerAlgs) (word A2_scramble) (skel A2_block)
def bestAt (l : List (Option (Nat × Nat))) (js : List Nat) : Nat :=
  (js.filterMap fun j => (l[j]!).map (·.1)).foldl min 1000

/-- A2's example: the block replays (a 20-move skeleton leaving "DBR → UBR → DFR → DBR"); over every 8-mover at
every spot the best is 25, at spot 16 only and by one alg only (the only 8-3); the odd spots and both ends give at
best 27 (an 8-1); spot 16 comes right after `F' B`. -/
theorem A2_example :
    checkBlock A2_scramble A2_block "DBR → UBR → DFR → DBR" ∧ (skel A2_block).length = 20 ∧
    A2_spots[16]! = some (25, 1) ∧
    (List.range 21).all (fun j => j == 16 || bestAt A2_spots [j] > 25) ∧
    bestAt A2_spots [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20] = 27 ∧
    text ((skel A2_block).drop 14 |>.take 2) = "F' B" := by native_decide

/-- Why every other move misses it.  The comm cancels its `F` against the `F'` before `B`, across the pair: as
written, the spot two moves back (14) gives at best 27, so no shifted 8-mover there does the same.  With the pair
written the other way round (`B F'`, the same skeleton), the comm moved one move over, `D F' U F D' F' U' F`, fits
between the two (spot 15) for the same 25, and that block replays to the same solution. -/
def A2_swapped_block := [
  "F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' B * F' U2 B' L D",
  "* = D F' U F D' F' U' F // (8-3/25)",
  "Solution: F2 D2 B2 U' D2 L2 F2 L' D R' B' R2 F U' B D F' U F D' F' U B' L D (25)"]
theorem A2_pair_swapped :
    bestAt A2_spots [14] = 27 ∧
    stateOf (skel A2_swapped_block) = stateOf (skel A2_block) ∧
    checkBlock A2_scramble A2_swapped_block "DBR → UBR → DFR → DBR" ∧
    bestAt (perSpot (byState cornerAlgs) (word A2_scramble) (skel A2_swapped_block)) [15] = 25 := by native_decide

/-! ## A3: a 19-move 5c -/

def A3_scramble := "R' U' F L2 D B2 L2 U B2 L2 D2 B2 D2 F2 U' R B L' B' F L' U' L R2 D R' U' F"
def A3_block := [
  "F2 D2 R2 D' F' L F ^ R' D B2 L B R' * B' U' B2 U2 L2 D",
  "* = D2 B' U2 B D2 B' U2 B // (8-3/24)",
  "^ = D R' U2 R D' R' U2 R // (8-2/30)",
  "Solution: F2 D2 R2 D' F' L F D R' U2 R D' R' U2 D B2 L B R' D2 B' U2 B D2 B' U B2 U2 L2 D (30)"]

/-- A3's example replays (19 moves, "DBL → UFL → DBR → UBR → UBL → DBL", a 5-cycle with twist sum 0) and 30 is
the best with two algs of 8 moves or fewer. -/
theorem A3_example :
    checkBlock A3_scramble A3_block "DBL → UFL → DBR → UBR → UBL → DBL" ∧ (skel A3_block).length = 19 ∧
    cornerType (stateOf (word A3_scramble ++ skel A3_block)) = [(5, 0)] ∧
    (best2 cornerAlgs (byState cornerAlgs) (word A3_scramble) (skel A3_block)).1 = 30 := by native_decide

end ins
end Insertions
