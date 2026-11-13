import Insertions.ErrataTheorems
import Insertions.Counts
/-
  More of the printed examples (write-up sections 6 to 10), replayed from the text, with their 8-mover optima, and
  the counts of section 1 ("Exact counts", "Edges depend on the alg list") that the list of algs of 8 moves or fewer
  settles.  Strings copied from research/src/report_build/wit_negative.md, wit_nested.md, wit_third.md,
  wit_n21.md and wit_no8.md.
-/
namespace Insertions
namespace ins
open cube

/-! ## Examples -/

def D_scramble := "R' U' F U' F D2 B' L2 R2 B L2 D2 U2 F D2 L R2 F2 R2 D R' F2 U' F2 U R' U' F"
def D_block := [
  "U2 B U' R D2 F2 L D R' B' L B R' * D' L F B2 D' L D'",
  "* = R B' L' B R' B' L B // (8-9/19)",
  "Solution: U2 B U' R D2 F2 L D R2 B' L B D' L F B2 D' L D' (19)"]

/-- [d]: the block replays, and 19 is the best 8-mover insertion (20 moves before). -/
theorem example_d_negative :
    checkBlock D_scramble D_block "UBL → UFL → DFR → UBL" ∧ (skel D_block).length = 20 ∧
    bestAt (perSpot (byState cornerAlgs) (word D_scramble) (skel D_block)) (List.range 21) = 19 := by native_decide

def E_scramble := "R' U' F B2 R F2 L' B2 R D2 B2 D2 B2 D2 L2 F' U' R' B' L' D' R2 U' R' U' F"
def E_block := [
  "L' D' R F U' L2 U * R2 F U' B D' L D F' D' B D' B2 R2",
  "* = D' L' D R2 D' L D R2 // (8-2/26)",
  "L' D' R F U' L2 U D' L' ^ D R2 D' L D F U' B D' L D F' D' B D' B2 R2",
  "^ = L U' L' D2 L U L' D2 // (8-5/29)",
  "Solution: L' D' R F U' L2 D' L' D2 L U L' D' R2 D' L D F U' B D' L D F' D' B D' B2 R2 (29)"]
def E_flat_block := [
  "L' D' R F U' L2 ^ U * R2 F U' B D' L D F' D' B D' B2 R2",
  "* = D' L' D R2 D' L D R2 // (8-2/26)",
  "^ = L' D L U L' D' L U' // (8-3/31)",
  "Solution: L' D' R F U' L D L U L' D' L D' L' D R2 D' L D F U' B D' L D F' D' B D' B2 R2 (31)"]

/-- [e]: both blocks replay; 29 is the best with two 8-movers, and the best pair needs the second comm inside the
first: with both comms put into the skeleton itself the best is 31. -/
theorem example_e_nested :
    checkBlock E_scramble E_block "DBL → UBL → DBR → DFR → UFL → DBL" ∧
    checkBlock E_scramble E_flat_block "DBL → UBL → DBR → DFR → UFL → DBL" ∧ (skel E_block).length = 20 ∧
    (best2 cornerAlgs (byState cornerAlgs) (word E_scramble) (skel E_block)).1 = 29 ∧
    bestFlat cornerAlgs (byState cornerAlgs) (word E_scramble) (skel E_block) = 31 := by native_decide

def J_scramble := "R' U' F R2 D F2 U2 L2 U F2 U' B2 U2 B2 L' F R2 D' R' B2 L' F D2 R' U' F"
def J_block := [
  "D' R2 U2 L * U2 D' R' F2 L U L U' B U' R U2 R2 U2 D2 L2",
  "* = L U' L' D' L U L' D // (8-3/25)",
  "Solution: D' R2 U2 L2 U' L' D' L U L' U2 R' F2 L U L U' B U' R U2 R2 U2 D2 L2 (25)"]
def J_spots : List (Option (Nat × Nat)) := perSpot (byState cornerAlgs) (word J_scramble) (skel J_block)

/-- [j]: the block replays; the best 8-mover insertion is 25, at spot 4 only and by one alg only; every third spot
from the start (0, 3, …, 18) and the end give at best 27 (an 8-1). -/
theorem example_j_third :
    checkBlock J_scramble J_block "UFL → DFR → UFR → UFL" ∧ (skel J_block).length = 20 ∧
    J_spots[4]! = some (25, 1) ∧ (List.range 21).all (fun j => j == 4 || bestAt J_spots [j] > 25) ∧
    bestAt J_spots [0, 3, 6, 9, 12, 15, 18, 20] = 27 := by native_decide

def H_scramble := "R' U' F L' D2 B2 L2 U2 B2 R' D2 U2 L2 U' F' R F2 D2 L2 D L B' U' R' U' F"
def H_block := [
  "B' D L' U2 L' U2 D2 R D B' U F R2 F * B' U B' D' B2 U R2",
  "* = U2 B' U' F2 U B U' F2 U' // (9-0/30)",
  "Solution: B' D L' U2 L' U2 D2 R D B' U F R2 F U2 B' U' F2 U B U' F2 U' B' U B' D' B2 U R2 (30)"]
def N8_scramble := "R' U' F L2 D' R2 F2 U R2 D' F2 R2 F2 R2 D L' F' L R' D U R F' D' L R' U' F"
def N8_block := [
  "R2 U2 D R' U B' L' U' F2 D2 F2 R2 L B2 D' B' R2 * B' R2 L2",
  "* = R B R' D2 R B' R' B D2 B' // (10-2/28)",
  "Solution: R2 U2 D R' U B' L' U' F2 D2 F2 R2 L B2 D' B' R' B R' D2 R B' R' B D2 B2 R2 L2 (28)"]

/-- [h] (the 21-move 3c of 7.3) and the 20-move 3c of 3.1: both blocks replay (the 9-mover and the 10-mover are
corner-only algs with the printed cancels), and at none of the spots does the case have an alg of 8 moves or fewer. -/
theorem examples_no_8_mover :
    checkBlock H_scramble H_block "DFL → UBR → UBL → DFL" ∧ (skel H_block).length = 21 ∧
    (perSpot (byState cornerAlgs) (word H_scramble) (skel H_block)).all (· == none) ∧
    checkBlock N8_scramble N8_block "DFL → UBL → UFL → DFL" ∧ (skel N8_block).length = 20 ∧
    (perSpot (byState cornerAlgs) (word N8_scramble) (skel N8_block)).all (· == none) := by native_decide

/-! ## Counts of section 1 -/

/-- "528 of the 1,008 corner 3-cycles have an 8-mover, 336 of them two different ones" (`corner_algs_up_to_8`);
"32 of the 112 3-cycles that keep all three corners oriented have one"; "112 3-cycles have none even after any one
move".  The 1008 and the 112 are counted here on the sticker cube: all 3,024 ways to cycle three corners with
any twists, of which 1008 have twist sum 0 and 112 leave all three oriented. -/
theorem corner_counts :
    cornerThree.length = 1008 ∧
    (cornerThree.filter cornerOriented).length = 112 ∧
    ((byState cornerAlgs).toList.filter fun e => cornerOriented (stateOf e.2[0]!)).length = 32 ∧
    cornerCovered.size = 896 ∧
    (cornerThree.filter fun s => !cornerCovered.contains (keyOn ALL s)).length = 112 := by native_decide

/-- Zagros: "There arent 8 movers if they're oriented"; Jay's answer `R' F' R B2 R' F R B2` is an 8-move corner
3-cycle that leaves all three corners oriented, one of the 864 of `corner_algs_up_to_8`. -/
theorem jay_oriented_8_mover :
    cornerType (stateOf (word "R' F' R B2 R' F R B2")) = [(3, 0)] ∧
    cornerOriented (stateOf (word "R' F' R B2 R' F R B2")) ∧ edgesSolved (stateOf (word "R' F' R B2 R' F R B2")) ∧
    cornerAlgs.contains (normal (word "R' F' R B2 R' F R B2")) := by native_decide

/-- Edges: the edge 3-cycles with an alg of 8 moves or fewer are 168 (24 with a 6-mover, 48 more with a 7-mover,
96 more with an 8-mover), with 96, 240 and 2,496 different sequences of 6, 7 and 8 moves; the 24 with a 6-mover
all have their three edges oriented on all three axes, and exactly 24 edge 3-cycles do. -/
theorem edge_counts :
    (byState edge3Algs).size = 168 ∧
    ((shortest (byState edge3Algs)).count 6, (shortest (byState edge3Algs)).count 7,
      (shortest (byState edge3Algs)).count 8) = (24, 48, 96) ∧
    ((edge3Algs.toList.map (·.length)).count 6, (edge3Algs.toList.map (·.length)).count 7,
      (edge3Algs.toList.map (·.length)).count 8) = (96, 240, 2496) ∧
    ((byState edge3Algs).toList.filter fun e => (e.2.toList.map (·.length)).foldl min 99 == 6).all
      (fun e => edgeAllAxes (stateOf e.2[0]!)) ∧
    ((cyclePlacements EDGES facelets 2).filter fun s => isEdge3 s && edgeAllAxes s).length = 24 := by native_decide

end ins
end Insertions
