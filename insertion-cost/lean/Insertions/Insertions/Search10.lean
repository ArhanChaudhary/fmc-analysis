import Insertions.Search
/-
  Insertions.Search10 — the join of `Search.lean` with halves of up to 5 turns: every alg of 10 moves or fewer
  that touches only corners (or only edges).  All 2,000,719 sequences of at most 5 turns are listed, cancelling or
  not; a sequence of at most 10 turns in normal form is one of them followed by one of them.

  The halves are matched by a 64-bit mix of the stickers that have to come home (those of `b`'s state against those
  of the state of `a` reversed), not by the stickers themselves, to keep the table small; a chance match of two
  different sticker patterns would only add a candidate, and every candidate kept is checked on the cube
  (`fixed` stickers home, not the identity).  Functions of `()` so that nothing runs when the file is loaded.
-/
namespace Insertions
namespace ins
open cube

def mixOn (idx : Array Nat) (s : State) : UInt64 :=
  idx.foldl (fun h i => h * 1099511628211 + (s[i]!).toUInt64 + 1) 14695981039346656037

/-- Every sequence of at most `2 * k` turns, in normal form and once each, that leaves the stickers `fixed` home
and is not the identity. -/
def joinedUpTo (k : Nat) (fixed : List Nat) : Array (List Nat) := Id.run do
  let hs := (Array.range (k + 1)).flatMap wordsOfLen
  let idx := fixed.toArray
  let mut left : Std.HashMap UInt64 (Array Nat) := {}
  for i in [0:hs.size] do
    let key := mixOn idx (stateOf (inv hs[i]!))
    left := left.insert key ((left.getD key #[]).push i)
  let mut seen : Std.HashSet (List Nat) := {}
  let mut out : Array (List Nat) := #[]
  for b in hs do
    for i in left.getD (mixOn idx (stateOf b)) #[] do
      let w := normal (hs[i]! ++ b)
      if !seen.contains w then
        seen := seen.insert w
        let s := stateOf w
        if fixed.all (fun j => s[j]! == j) && s != SOLVED then out := out.push w
  return out

/-- For a list of algs: each thing they do with its type and the length of its shortest alg, counted:
(type, shortest length, number of states), and (type, alg length, number of sequences). -/
def summary (algs : Array (List Nat)) (typeOf : State → List (Nat × Nat)) :
    List (List (Nat × Nat) × Nat × Nat) × List (List (Nat × Nat) × Nat × Nat) := Id.run do
  let tbl := byState algs
  let mut el : Std.HashMap (List (Nat × Nat) × Nat) Nat := {}
  let mut sq : Std.HashMap (List (Nat × Nat) × Nat) Nat := {}
  for (_, as) in tbl.toList do
    let tp := typeOf (stateOf as[0]!)
    let short := (as.toList.map (·.length)).foldl min 99
    el := el.insert (tp, short) (el.getD (tp, short) 0 + 1)
    for a in as do sq := sq.insert (tp, a.length) (sq.getD (tp, a.length) 0 + 1)
  let srt (m : Std.HashMap (List (Nat × Nat) × Nat) Nat) : List (List (Nat × Nat) × Nat × Nat) :=
    (m.toList.map fun ((tp, l), n) => (tp, l, n)).mergeSort fun a b =>
      a.2.1 < b.2.1 || (a.2.1 == b.2.1 && decide (toString a.1 ≤ toString b.1))
  return (srt el, srt sq)

end ins
end Insertions
