/-
  Insertions.LeftoverTypes — research/src/leftover_types.py in Lean: which kinds of leftover one or two 3-cycles
  can make, for corners and for edges, by multiplying everything out.

  A corner state is (perm, twist): the piece perm[i] sits at place i with twist[i] in Z3; an edge state is the same
  with flips in Z2.  Everywhere below, n is the number of pieces (8 corners, 12 edges) and m the number of ways a
  piece can sit in its place (3 for corners, 2 for edges).  The type of a state is its cycle structure with the
  twist (flip) sum of each cycle: a corner 3-cycle is [(3, 0)], two twisted corners are [(1, 2), (1, 1)].

  Python -> Lean:
    a tuple of numbers                         `Array Nat`, written `#[0, 1, 2]`;  `a[i]!` is Python's `a[i]`
    `tuple(f(i) for i in range(n))`            a loop: start from an empty `Array` (`Array.emptyWithCapacity n`,
                                               empty, with room for n entries) and `push` f(i) for each i
    `p = list(range(n)); p[j] = i`             `(Array.range n).set! j i`  (a changed copy)
    a tuple of pairs, the type of a state      `List (Nat × Nat)`, written `[(3, 0), (3, 0)]`;  `()` is `[]`
    `set()`, `s in seen`, `seen.add(s)`        `Std.HashSet`: `seen.contains s`, `seen.insert s`
    `for i in range(n)`                        `for i in [0:n]`

  Where this file differs from leftover_types.py (the results are the same):
    * `three_cycles` returns a list in the order the loops make it; the Python puts them in a set and sorts it.
      (Theorems `corner_three_cycles` and `edge_three_cycles` say that no state is listed twice.)
    * `(-oi - oj) % m` is written `(2 * m - oi - oj) % m`: Lean's `Nat` has no negative numbers.
    * `mul` fills its two tuples in one loop, the Python in two generator expressions.
    * `itertools.permutations(range(n), 3)` is three loops that skip equal indices.
    * `run` returns the types as a list sorted as the Python prints them (fewest 3-cycles, then most states); where
      two types have the same number of states they come in alphabetical order, in the Python in whatever order its
      set gave them.  Nothing is printed and no file is written.
-/
import Std.Data.HashMap
import Std.Data.HashSet

namespace Insertions

/-- A state `(perm, twist)`: the piece `perm[i]` sits at place i, twisted (flipped) by `twist[i]`. -/
abbrev State := Array Nat × Array Nat

/-- The type of a state: its cycles as (length, twist sum), largest first.  Pieces that are in place and not
twisted are left out, so the solved state has type `[]`, and an entry (1, t) is a piece twisted in place. -/
abbrev CType := List (Nat × Nat)

/-- a then b: place i gets what b brings there from the state a. -/
def mul (a b : State) (m : Nat) : State := Id.run do
  let (pa, ta) := a
  let (pb, tb) := b
  let mut p := Array.emptyWithCapacity pa.size
  let mut t := Array.emptyWithCapacity pa.size
  for i in [0:pa.size] do
    p := p.push pa[pb[i]!]!
    t := t.push ((ta[pb[i]!]! + tb[i]!) % m)
  return (p, t)

/-- The solved state. -/
def ident (n : Nat) : State := (Array.range n, Array.replicate n 0)

/-- All 3-cycles: three pieces i -> j -> k -> i with twists oi, oj, ok that add up to 0, everything else untouched. -/
def three_cycles (n m : Nat) : List State := Id.run do
  let mut out : Array State := #[]
  for i in [0:n] do
    for j in [0:n] do
      for k in [0:n] do
        if i == j || i == k || j == k then continue         -- three different places
        if !(i < j && i < k) then continue                  -- each cyclic order once: i is the smallest
        for oi in [0:m] do
          for oj in [0:m] do
            let ok := (2 * m - oi - oj) % m
            -- the piece at i goes to j, j to k, k to i
            let p := (((Array.range n).set! j i).set! k j).set! i k
            let t := (((Array.replicate n 0).set! j oi).set! k oj).set! i ok
            out := out.push (p, t)
  return out.toList

/-- `sorted(out, reverse=True)` for a list of pairs: largest first, comparing the first numbers, then the second. -/
def sorted_reverse (out : CType) : CType :=
  out.mergeSort fun a b => a.1 > b.1 || (a.1 == b.1 && a.2 >= b.2)

/-- The type of the state s: walk each cycle of `perm` once, adding up the twists along it. -/
def ctype (s : State) (m : Nat) : CType := Id.run do
  let (p, t) := s
  let mut seen := Array.replicate p.size false
  let mut out : CType := []
  for i in [0:p.size] do
    if seen[i]! then continue
    let mut j := i
    let mut L := 0
    let mut tw := 0
    while !seen[j]! do
      seen := seen.set! j true
      tw := tw + t[j]!
      j := p[j]!
      L := L + 1
    if L > 1 || tw % m != 0 then out := out ++ [(L, tw % m)]
  return sorted_reverse out

/-- The Python's table of names for corner types. -/
def corner_table : List (CType × String) :=
  [([(3, 0)], "3c"), ([(1, 2), (1, 1)], "2tc"), ([(1, 1), (1, 1), (1, 1)], "3tc"), ([(1, 2), (1, 2), (1, 2)], "3tc"),
   ([(2, 0), (2, 0)], "2c2c-pure"), ([(2, 2), (2, 1)], "2c2c-twisted"), ([(3, 1), (1, 2)], "3c1t"),
   ([(3, 2), (1, 1)], "3c1t"), ([(5, 0)], "5c"), ([(3, 0), (3, 0)], "3c3c"), ([(3, 2), (3, 1)], "3c3c-twisted")]

/-- The Python's table of names for edge types. -/
def edge_table : List (CType × String) :=
  [([(3, 0)], "3e"), ([(1, 1), (1, 1)], "2f"), ([(2, 0), (2, 0)], "2e2e"), ([(2, 1), (2, 1)], "2e2e-flipped"),
   ([(5, 0)], "5e"), ([(3, 0), (3, 0)], "3e3e"), ([(3, 1), (1, 1)], "3e1f"), ([(3, 1), (3, 1)], "3e3e-flipped")]

/-- The name of a type: from the table, else spelled out cycle by cycle ("5c+2 1c+1"). -/
def name (tp : CType) (kind : String) : String :=
  let c := if kind == "corner" then "c" else "e"
  if tp == [] then "solved" else
  let table := if kind == "corner" then corner_table else edge_table
  match table.lookup tp with
  | some nm => nm
  | none => " ".intercalate (tp.map fun (L, tw) =>
      if L > 1 then s!"{L}{c}" ++ (if tw != 0 then s!"+{tw}" else "") else s!"1{c}+{tw}")

/-- What `run` returns (the Python's `res`, the content of out/types.json). -/
structure Result where
  /-- how many 3-cycles there are -/
  three_cycles : Nat
  /-- (name of the type, fewest 3-cycles, number of states), for every type met with one or two 3-cycles -/
  types : List (String × Nat × Nat)
  /-- states reachable with at most two 3-cycles, the solved state included -/
  states_within_two : Nat
  deriving DecidableEq, Repr

/-- The order of the printout: fewest 3-cycles first, then most states first (then by name). -/
def sort_types (types : List (String × Nat × Nat)) : List (String × Nat × Nat) :=
  types.mergeSort fun (nm1, k1, c1) (nm2, k2, c2) =>
    k1 < k2 || (k1 == k2 && (c1 > c2 || (c1 == c2 && nm1 <= nm2)))

/-- From the solved state, multiply by every 3-cycle, twice; name the type of every new state. -/
def run (kind : String) : Result := Id.run do
  let (n, m) := if kind == "corner" then (8, 3) else (12, 2)
  let C3 := three_cycles n m
  let e := ident n
  let mut level : Array State := #[e]
  let mut seen : Std.HashSet State := {}
  seen := seen.insert e
  let mut types : Std.HashMap String (Nat × Nat) := {}
  for k in [1, 2] do
    let mut nxt : Array State := #[]
    for s in level do
      for g in C3 do
        let t := mul s g m
        if !seen.contains t then
          seen := seen.insert t
          nxt := nxt.push t
    for s in nxt do
      let nm := name (ctype s m) kind
      let (k0, count) := types.getD nm (k, 0)
      types := types.insert nm (k0, count + 1)
    level := nxt
  return ⟨C3.length, sort_types types.toList, seen.size⟩

end Insertions
