import Insertions.Search10
/-
  Insertions.Ten — what the algs of 10 moves or fewer settle: their counts by type and length, and the cap-10 parts
  of the printed examples [b], [h], [i], [k], the 20-move 3c of 6.1 with no 8-mover and the 23-move 3c of 9.5.
  One function, so that the list of algs is made once.  Block strings copied from
  research/src/report_build/wit_ten.md, wit_setup10.md, wit_tenskip.md, wit_n21.md, wit_no8.md, wit_n2057.md.
-/
namespace Insertions
namespace ins
open cube

def B_scramble := "R' U' F U' D R2 F2 U L2 U B2 U2 R2 D' B' D L2 F U R' D' L U2 R D' R' U' F"
def B_block8 := [
  "F D' R' D F' L2 B2 R U F' U2 D' B' * R' D2 F L2 U' B2 U",
  "* = B' L' B R2 B' L B R2 // (8-2/26)",
  "Solution: F D' R' D F' L2 B2 R U F' U2 D' B2 L' B R2 B' L B R D2 F L2 U' B2 U (26)"]
def B_block10 := [
  "F D' * R' D F' L2 B2 R U F' U2 D' B' R' D2 F L2 U' B2 U",
  "* = D F' D' F R F' D F D' R' // (10-5/25)",
  "Solution: D' F R F' D F D' R2 D F' L2 B2 R U F' U2 D' B' R' D2 F L2 U' B2 U (25)"]

def I_scramble := "R' U' F L R U2 B2 U2 F2 R U2 L2 F2 D2 R F' U' B2 R' D2 B R U2 F' R' U' F"
def I_block8 := [
  "R' B' U' L' F' B' L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2 *",
  "* = D' F' D B' D' F D B // (8-0/28)",
  "Solution: R' B' U' L' F' B' L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2 D' F' D B' D' F D B (28)"]
def I_block10 := [
  "R' B' U' L' F' B' * L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2",
  "* = F B' R2 F' L2 F R2 F' L2 B // (10-3/27)",
  "Solution: R' B' U' L' B2 R2 F' L2 F R2 F' L2 B L' B' L2 U' F' L2 D2 L' D L U2 L2 U F2 (27)"]

def K_scramble := "R' U' F B' U2 B2 L2 F U2 F L2 U2 L2 R B2 F L D' B' U B L2 B' R' U' F"
def K_block := [
  "L' U' D B L' U' R D L D' * R' L D' B2 U' B2 U2 B D' B'",
  "* = D' L U' L' D L U L' // (8-3/25)",
  "Solution: L' U' D B L' U' R D L D2 L U' L' D L U R' D' B2 U' B2 U2 B D' B' (25)"]
def K_ten := "U' R' B2 R F R' B2 R F' U"

def H_scramble10 := "R' U' F L' D2 B2 L2 U2 B2 R' D2 U2 L2 U' F' R F2 D2 L2 D L B' U' R' U' F"
def H_skeleton := "B' D L' U2 L' U2 D2 R D B' U F R2 F B' U B' D' B2 U R2"
def N8_scramble10 := "R' U' F L2 D' R2 F2 U R2 D' F2 R2 F2 R2 D L' F' L R' D U R F' D' L R' U' F"
def N8_skeleton := "R2 U2 D R' U B' L' U' F2 D2 F2 R2 L B2 D' B' R2 B' R2 L2"

def P_scramble := "R' U' F U2 F2 D2 F2 L' B2 L D2 B2 L B2 R U' L' D' B D2 U' L R B' R' U' F"
def P_block8 := [
  "U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' L' D * L D' B D B'",
  "* = D' L D R D' L' D R' // (8-4/27)",
  "Solution: U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' D R D' L' D R' L D' B D B' (27)"]
def P_block10 := [
  "U' L2 B2 U' L F D' L2 D' F' D F2 B D2 F' B' L' D L D' * B D B'",
  "* = D L' D' L F L' D L D' F' // (10-10/23)",
  "Solution: U' L2 B2 U' L F D' L2 D' F' D F2 B D2 B' L' D L D' F' B D B' (23)"]
def P_hand := "U' L2 B2 U' L F D' L2 D' F' D F2 B D B R' B' R D F' D B'"

/-- Spot by spot: the shortest result of one alg of the table there (0 where no alg of the table fits). -/
def spotBest (tbl : Std.HashMap Nat (Array (List Nat))) (z s : List Nat) : List Nat :=
  (perSpot tbl z s).map fun o => (o.map (·.1)).getD 0
/-- Spot by spot: the length of the shortest alg of the table for the case there (0 where it has none). -/
def spotShortest (tbl : Std.HashMap Nat (Array (List Nat))) (z s : List Nat) : List Nat :=
  (List.range (s.length + 1)).map fun j =>
    ((tbl.getD (keyOn ALL (needed z s j)) #[]).toList.map (·.length)).foldl min 99 |> fun l => if l == 99 then 0 else l
/-- The smallest entry that is not 0 (1000 if there is none). -/
def least (l : List Nat) : Nat := (l.filter (· != 0)).foldl min 1000

structure TenFacts where
  /-- (type, shortest alg length, number of states) for everything the corner-only algs of at most 10 moves do -/
  states : List (List (Nat × Nat) × Nat × Nat)
  /-- (type, alg length, number of sequences) -/
  sequences : List (List (Nat × Nat) × Nat × Nat)
  /-- [b]: best with algs of at most 8, 9, 10 moves -/
  b : List Nat
  /-- [i]: best with at most 8 and at most 10 -/
  i : List Nat
  /-- [k]: best 8-mover result at each spot; the shortest alg (at most 10) for the case at spots 0, 2, 4, 6, 8;
  whether the printed 10-mover does what spot 8 needs -/
  k8 : List Nat
  kShort : List Nat
  kTen : Bool
  /-- [h]: best with at most 10 -/
  h : Nat
  /-- the 20-move 3c with no 8-mover: best with at most 10; the shortest alg for the case at each spot -/
  n8 : Nat
  n8Short : List Nat
  /-- the 23-move 3c of 9.5: best with at most 8 and at most 10 -/
  p : List Nat
deriving DecidableEq, Repr

def tenFacts (_ : Unit) : TenFacts := Id.run do
  let algs := joinedUpTo 5 EDGE_STICKERS
  let (el, sq) := summary algs cornerType
  let t10 := byState algs
  let t9 := byState (algs.filter (·.length ≤ 9))
  let t8 := byState (algs.filter (·.length ≤ 8))
  let sk (b : List String) : List Nat := (marked b[0]!).1
  let best (t : Std.HashMap Nat (Array (List Nat))) (z : String) (s : List Nat) : Nat := least (spotBest t (word z) s)
  let ks := sk K_block
  return {
    states := el, sequences := sq
    b := [best t8 B_scramble (sk B_block8), best t9 B_scramble (sk B_block8), best t10 B_scramble (sk B_block8)]
    i := [best t8 I_scramble (sk I_block8), best t10 I_scramble (sk I_block8)]
    k8 := spotBest t8 (word K_scramble) ks
    kShort := [0, 2, 4, 6, 8].map fun j => (spotShortest t10 (word K_scramble) ks)[j]!
    kTen := stateOf (word K_ten) == needed (word K_scramble) ks 8
    h := best t10 H_scramble10 (word H_skeleton)
    n8 := best t10 N8_scramble10 (word N8_skeleton)
    n8Short := spotShortest t10 (word N8_scramble10) (word N8_skeleton)
    p := [best t8 P_scramble (sk P_block8), best t10 P_scramble (sk P_block8)] }

end ins
end Insertions
