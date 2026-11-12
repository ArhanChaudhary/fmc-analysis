/-
  Insertions.Three — one more round of leftover_types.py's loop: the types that need exactly three 3-cycles.
  Used for corners only.

  The Python keeps every state it has met in a set.  With three 3-cycles that is 9 million corner states, which
  as tuples would not fit in the 2 GB this build is held to, so here the set is a table with one byte for every
  state there is (8! x 3^7 = 88,179,840 bytes), and a state is looked up by its number

    index s  =  perm_index s.perm x m^(n-1)  +  twist_index s.twist m

  that is, its position in the list of all states (p, t), p in `permutations n`, t in `twists n m`.  This is the
  one encoding in the project.  Theorem `every_state_once` says that `perm_index` and `twist_index` are the
  positions in those two lists, so two different states never share a number.  (Every state met is in the list:
  the 3-cycles are states, theorem `corner_three_cycles`, and `mul` of two states is a state.)

  Python -> Lean:
    `seen` (a set of states)        `fewest`, a `ByteArray`: `fewest[index s]` = the fewest 3-cycles that make s,
                                    255 = not met
    `types[nm][1] += 1`             `count[(k, type)] += 1`: counted by the exact type, not by name
    `level = nxt`                   the same, except that the states of the last round are counted and not kept
-/
import Insertions.AllStates

set_option compiler.extract_closed false

namespace Insertions

/-- (k, type, how many) in the order used in the theorems: fewest 3-cycles first, then as `sort_counts`. -/
def sort_levels (rows : List (Nat × CType × Nat)) : List (Nat × CType × Nat) :=
  rows.mergeSort fun (k1, tp1, c1) (k2, tp2, c2) =>
    k1 < k2 || (k1 == k2 && (c1 > c2 || (c1 == c2 && type_ge tp1 tp2)))

/-- The rows (k, type, how many) with a given k, as (type, how many). -/
def rows_at (k : Nat) (rows : List (Nat × CType × Nat)) : List (CType × Nat) :=
  (rows.filter fun row => row.1 == k).map fun row => (row.2.1, row.2.2)

/-- From the solved state, multiply by every 3-cycle, `depth` times.  Returns (k, type, number of states) for
every k up to `depth` and every type: how many states of that type are made by k 3-cycles and not by fewer. -/
def fewest_by_type (n m depth : Nat) : List (Nat × CType × Nat) := Id.run do
  let C3 := three_cycles n m
  let e := ident n
  let per_perm := m ^ (n - 1)                     -- how many twist vectors there are
  let index := fun (s : State) => perm_index s.1 * per_perm + twist_index s.2 m
  let size := fact n * per_perm                   -- how many states there are
  let mut fewest := ByteArray.emptyWithCapacity size
  for _ in [0:size] do
    fewest := fewest.push 255
  fewest := fewest.set! (index e) 0
  let mut count : Std.HashMap (Nat × CType) Nat := {}
  count := count.insert (0, []) 1
  let mut level : Array State := #[e]
  for k in [1:depth + 1] do
    let mut nxt : Array State := #[]
    for s in level do
      for g in C3 do
        let t := mul s g m
        let i := index t
        if fewest[i]! == 255 then
          fewest := fewest.set! i k.toUInt8
          let key := (k, ctype t m)
          count := count.insert key (count.getD key 0 + 1)
          if k < depth then nxt := nxt.push t
    level := nxt
  return sort_levels (count.toList.map fun ((k, tp), c) => (k, tp, c))

end Insertions
