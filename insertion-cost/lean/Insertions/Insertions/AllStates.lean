/-
  Insertions.AllStates — the full size of a type, counted by going through every state.  Not in
  leftover_types.py.

  A state here is any permutation of the n pieces with any twists that add up to 0 (mod m): for corners
  8! x 3^7 = 88,179,840 states (even and odd permutations alike; the type decides the parity anyway).

  Python -> Lean:
    `permutations n`      `list(itertools.permutations(range(n)))`
    `twists n m`          `[t for t in itertools.product(range(m), repeat=n) if sum(t) % m == 0]`
    `type_counter n m`    `collections.Counter(ctype((p, t), m) for p in permutations(n) for t in twists(n, m))`
    `type_sizes n m tps`  `c = type_counter(n, m); [c[tp] for tp in tps]`
    `perm_index p`        `permutations(len(p)).index(p)`, computed without the list
    `twist_index t m`     `twists(len(t), m).index(t)`, computed without the list

  That the two lists are complete, each entry once, is theorem `every_state_once`.

  For edges the loop of `type_sizes` would be 12! x 2^11 = 980,995,276,800 states, too many.
  `type_size_by_places` gets the same number with a small loop: a type only touches the places in its cycles,
  k of them say (`places tp`), so a state of that type on n places is a choice of the k places it touches
  (n choose k) and a state of that type on those k places alone.  Theorem `corner_type_sizes_by_places` checks this
  shortcut against the full loop for corners.
-/
import Insertions.Products

-- Keep the compiler from moving loops that depend on nothing to load time.
set_option compiler.extract_closed false

namespace Insertions

/-- Every ordering of the k numbers in `l`, in sorted order when `l` is sorted. -/
def orderings : Nat → List Nat → List (List Nat)
  | 0, _ => [[]]
  | k + 1, l => l.flatMap fun x => (orderings k (l.erase x)).map (x :: ·)

/-- Every permutation of 0 .. n-1, in sorted order. -/
def permutations (n : Nat) : List (Array Nat) := (orderings n (List.range n)).map (·.toArray)

/-- Every list of n numbers below m, in sorted order. -/
def vectors : Nat → Nat → List (List Nat)
  | 0, _ => [[]]
  | n + 1, m => (List.range m).flatMap fun x => (vectors n m).map (x :: ·)

/-- Every twist vector for n pieces whose twists add up to 0 mod m, in sorted order. -/
def twists (n m : Nat) : List (Array Nat) :=
  ((vectors n m).filter fun t => t.sum % m == 0).map (·.toArray)

/-- `sorted(p) == list(range(n))`: p is a permutation of 0 .. n-1. -/
def is_permutation (p : Array Nat) (n : Nat) : Bool := p.toList.mergeSort == List.range n

/-- t has n entries, all below m, adding up to 0 mod m. -/
def is_twist (t : Array Nat) (n m : Nat) : Bool := t.size == n && t.all (· < m) && t.sum % m == 0

/-- The position of the permutation p in `permutations p.size`.  The permutations that start with a smaller
number come first, (n-1)! of them for each such number; then the same for the second entry among the numbers
not used yet; and so on. -/
def perm_index (p : Array Nat) : Nat := Id.run do
  let n := p.size
  let mut r := 0
  for i in [0:n] do
    let mut smaller := 0                          -- how many of the numbers not used yet are below p[i]
    for j in [i + 1:n] do
      if p[j]! < p[i]! then smaller := smaller + 1
    r := r * (n - i) + smaller
  return r

/-- The position of the twist vector t in `twists t.size m`: all its entries but the last, read as a number in
base m (the last entry is whatever makes the total 0). -/
def twist_index (t : Array Nat) (m : Nat) : Nat := Id.run do
  let mut r := 0
  for i in [0:t.size - 1] do
    r := r * m + t[i]!
  return r

/-- ALL states (p, t), p any permutation of the n pieces, t any twist vector with total 0, counted by type. -/
def type_counter (n m : Nat) : Std.HashMap CType Nat := Id.run do
  let ts := twists n m
  let mut count : Std.HashMap CType Nat := {}
  for p in permutations n do
    for t in ts do
      let tp := ctype (p, t) m
      count := count.insert tp (count.getD tp 0 + 1)
  return count

/-- For each type in `tps`: how many of all states on n pieces have exactly that type. -/
def type_sizes (n m : Nat) (tps : List CType) : List Nat :=
  let count := type_counter n m
  tps.map fun tp => count.getD tp 0

/-- n choose k. -/
def choose : Nat → Nat → Nat
  | _, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, k + 1 => choose n k + choose n (k + 1)

/-- n! -/
def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

/-- How many places a type touches: the lengths of its cycles added up. -/
def places (tp : CType) : Nat := (tp.map (·.1)).sum

/-- The size of a type on n places, counted as (n choose k) x (states of that type on k places), k = `places tp`. -/
def type_size_by_places (n m : Nat) (tp : CType) : Nat :=
  choose n (places tp) * (type_sizes (places tp) m [tp]).sum

end Insertions
