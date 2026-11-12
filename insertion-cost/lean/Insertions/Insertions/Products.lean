/-
  Insertions.Products — what the theorems about two 3-cycles are stated with.  Not in leftover_types.py, which
  only prints the counts by name; here the same multiplication is kept as a list of states and counted by type.

  Python -> Lean, for the reader who wants the one-line equivalents:
    `products_of_two n m`     `{mul(g, h, m) for g in three_cycles(n, m) for h in three_cycles(n, m)}`, as a list
    `count_distinct l`        `len(set(l))`
    `count_in l among`        `sum(1 for s in l if s in set(among))`
    `by_type l m`             `collections.Counter(ctype(s, m) for s in l).most_common()`
    `cycles tp L`             `sum(1 for (length, tw) in tp if length == L)`
    `twisted_cycles tp L`     `sum(1 for (length, tw) in tp if length == L and tw != 0)`
-/
import Insertions.LeftoverTypes

namespace Insertions

/-- How many different states the list has. -/
def count_distinct (l : List State) : Nat := (Std.HashSet.ofList l).size

/-- How many states of the list `l` also occur in the list `among`. -/
def count_in (l among : List State) : Nat :=
  let set := Std.HashSet.ofList among
  (l.filter fun s => set.contains s).length

/-- Every product `mul g h m` of two 3-cycles g, h (all ordered pairs, g = h included), each state listed once,
in the order first met. -/
def products_of_two (n m : Nat) : List State := Id.run do
  let C3 := three_cycles n m
  let mut seen : Std.HashSet State := {}
  let mut out : Array State := #[]
  for g in C3 do
    for h in C3 do
      let t := mul g h m
      if !seen.contains t then
        seen := seen.insert t
        out := out.push t
  return out.toList

/-- Python's `a >= b` for two types (tuples of pairs): compare entry by entry, a longer tuple wins a tie. -/
def type_ge : CType → CType → Bool
  | [], [] => true
  | [], _ :: _ => false
  | _ :: _, [] => true
  | x :: xs, y :: ys => if x == y then type_ge xs ys else x.1 > y.1 || (x.1 == y.1 && x.2 > y.2)

/-- (type, how many) pairs in the order used everywhere here: most states first, and among types with the same
number of states the larger type (as Python compares tuples) first. -/
def sort_counts (counts : List (CType × Nat)) : List (CType × Nat) :=
  counts.mergeSort fun (tp1, c1) (tp2, c2) => c1 > c2 || (c1 == c2 && type_ge tp1 tp2)

/-- The states of `l` counted by type: (type, number of states of `l` with that type). -/
def by_type (l : List State) (m : Nat) : List (CType × Nat) := Id.run do
  let mut count : Std.HashMap CType Nat := {}
  for s in l do
    let tp := ctype s m
    count := count.insert tp (count.getD tp 0 + 1)
  return sort_counts count.toList

/-- How many cycles of length L the type has.  For L = 1: how many pieces are twisted (flipped) in place. -/
def cycles (tp : CType) (L : Nat) : Nat := (tp.filter fun c => c.1 == L).length

/-- How many cycles of length L with a twist sum other than 0 the type has. -/
def twisted_cycles (tp : CType) (L : Nat) : Nat := (tp.filter fun c => c.1 == L && c.2 != 0).length

end Insertions
