import Insertions.Replay
import Std.Data.HashMap
import Std.Data.HashSet
/-
  Insertions.Search — every alg of 8 moves or fewer that touches only corners (or only edges), and the exact best
  insertion of one or two such algs into a skeleton.  Brute force, no pruning.

  The algs.  Every move sequence of at most 8 face turns is a sequence `a` of at most 4 turns followed by a sequence
  `b` of at most 4 turns, and all 18^0 + … + 18^4 = 111,151 sequences of at most 4 turns are listed, cancelling or
  not.  `a ++ b` leaves every edge sticker home exactly when `b` does to the edges what the inverse of `a` does, so the
  pairs are found by sorting the `a`s by the edge stickers of the inverse of `a` and looking up each `b` by its own.
  Each such `a ++ b` is put in normal form (`normal`, all cancelling done) and kept once.  A sequence that cancels
  down is found in its cancelled form, and every cancelled sequence of at most 8 turns splits into two halves of at
  most 4, so the list is every alg of at most 8 moves, each written once (opposite-face pairs in the fixed order).

  The search.  A comm is inserted at a spot (after the first i moves) and the result is cancelled.  The alg needed at
  spot i of skeleton s after scramble z is the state of inv(s[:i]) ++ inv(z) ++ inv(s[i:]); the algs are looked up
  by their state, so every alg in the list that does the right thing there is tried.  Two comms: every first comm
  (every alg in the list, at every spot) that leaves at most three corners, then every second comm at every spot of
  the cancelled result, the spots inside what is left of the first comm included (nesting).
-/
namespace Insertions
namespace ins
open cube

def wordsOfLen : Nat → Array (List Nat)
  | 0 => #[[]]
  | n + 1 => (wordsOfLen n).flatMap fun w => (Array.range 18).map fun m => m :: w
/-- All sequences of at most 4 turns, cancelling or not: 111,151 of them. -/
def halves : Array (List Nat) := (Array.range 5).flatMap wordsOfLen

/-- The stickers at the places `idx`, as one number (6 bits each). -/
def keyOn (idx : List Nat) (s : State) : Nat := idx.foldl (fun acc i => acc * 64 + s[i]!) 0
def ALL : List Nat := List.range 54

/-- Every sequence of at most 8 turns, in normal form and once each, that leaves the stickers `fixed` home and is
not the identity. -/
def joined (fixed : List Nat) : Array (List Nat) := Id.run do
  let hs := halves
  let mut left : Std.HashMap Nat (Array Nat) := {}
  for i in [0:hs.size] do
    let k := keyOn fixed (stateOf (inv hs[i]!))
    left := left.insert k ((left.getD k #[]).push i)
  let mut seen : Std.HashSet (List Nat) := {}
  let mut out : Array (List Nat) := #[]
  for b in hs do
    for i in left.getD (keyOn fixed (stateOf b)) #[] do
      let w := normal (hs[i]! ++ b)
      if !seen.contains w then
        seen := seen.insert w
        if stateOf w != SOLVED then out := out.push w
  return out

/-- Corner-only algs of at most 8 moves (edges and centres untouched). -/
def cornerAlgs : Array (List Nat) := joined EDGE_STICKERS
/-- Edge-only algs of at most 8 moves. -/
def edgeAlgs : Array (List Nat) := joined CORNER_STICKERS

/-- The algs grouped by what they do (the whole sticker state). -/
def byState (algs : Array (List Nat)) : Std.HashMap Nat (Array (List Nat)) := Id.run do
  let mut m : Std.HashMap Nat (Array (List Nat)) := {}
  for a in algs do
    let k := keyOn ALL (stateOf a)
    m := m.insert k ((m.getD k #[]).push a)
  return m

/-- What an insertion at spot j of s has to do so that z, then s with it, is solved. -/
def needed (z s : List Nat) (j : Nat) : State := stateOf (inv (s.take j) ++ inv z ++ inv (s.drop j))

/-- For each spot 0 … |s|: the shortest result of one alg from the table inserted there, and how many algs give
it (`none` if no alg in the table does what is needed there). -/
def perSpot (tbl : Std.HashMap Nat (Array (List Nat))) (z s : List Nat) : List (Option (Nat × Nat)) :=
  (List.range (s.length + 1)).map fun j =>
    let ls := (tbl.getD (keyOn ALL (needed z s j)) #[]).toList.map fun a => (insertAt s j a).length
    match ls.min? with
    | none => none
    | some b => some (b, ls.count b)

/-- The shortest result of two algs from the list `algs` (the second from `tbl`, the same algs by state) that solve
scramble z after skeleton s, and how many (first spot, first alg, second spot, second alg) give it.  Large
(1000) if none. -/
def best2 (algs : Array (List Nat)) (tbl : Std.HashMap Nat (Array (List Nat))) (z s : List Nat) : Nat × Nat := Id.run do
  let zs := stateOf z
  let mut best := 1000
  let mut cnt := 0
  for i in [0:s.length + 1] do
    for a in algs do
      let s1 := insertAt s i a
      let t := run zs s1
      if !(edgesSolved t && cornersMoved t ≤ 3) then continue
      for j in [0:s1.length + 1] do
        for b in tbl.getD (keyOn ALL (needed z s1 j)) #[] do
          let l := (insertAt s1 j b).length
          if l < best then best := l; cnt := 1
          else if l == best then cnt := cnt + 1
  return (best, cnt)

/-- The leftover type on the corners, as (cycle length, twist sum mod 3) for each cycle, longest first, pieces
home and untwisted left out: `[(2, 1), (2, 2)]` is two swaps, each with a twist. -/
def cornerType (s : State) : List (Nat × Nat) := Id.run do
  let perm := CORNERS.map fun p => CORNERS.idxOf (cornerAt s p).1
  let tw := CORNERS.map fun p => (cornerAt s p).2
  let mut seen : List Nat := []
  let mut out : List (Nat × Nat) := []
  for i in List.range 8 do
    if seen.contains i then continue
    let mut j := i; let mut L := 0; let mut t := 0
    for _ in List.range 9 do
      if seen.contains j then break
      seen := seen ++ [j]; t := t + tw[j]!; j := perm[j]!; L := L + 1
    if L > 1 || t % 3 != 0 then out := out ++ [(L, t % 3)]
  return out.mergeSort fun a b => a.1 > b.1 || (a.1 == b.1 && a.2 >= b.2)

end ins
end Insertions
