import Insertions.Products
/-
  How many first comms leave a 3-cycle, per spot (write-up, section 1, "wen's question"; section 6.2; the
  corrections page, A1): for a leftover x, the corner 3-cycles c such that x with c taken off (c⁻¹ x) is a 3-cycle.
  At a spot the leftover is a conjugate of x, which has the same count, so this is the count at every spot.
  Counted for every state of every type two 3-cycles make, in the cubie model of `LeftoverTypes.lean`.
-/
namespace Insertions

/-- The inverses of the corner 3-cycles (a 3-cycle done twice), in the order of `three_cycles 8 3`. -/
def inverses : Array State := (three_cycles 8 3).toArray.map fun c => mul c c 3

/-- `y` is a corner 3-cycle: exactly three places hold a piece that is not home or is twisted, and none of the
three holds its own piece (so the three pieces go round in one cycle; the twists then add up to 0, as in every
state the products reach, `corner_products_of_two`). -/
def is_three (y : State) : Bool := Id.run do
  let (p, t) := y
  let mut moved := 0
  for i in [0:8] do
    if p[i]! != i then moved := moved + 1
    else if t[i]! != 0 then return false
  return moved == 3

/-- The number of corner 3-cycles c with c⁻¹ x a 3-cycle. -/
def first_comms (x : State) : Nat := inverses.foldl (fun n ci => if is_three (mul ci x 3) then n + 1 else n) 0

/-- For each type of the products of two corner 3-cycles: the different values of `first_comms` over all states
of that type, and how many states there are.  (It takes `()` so that it runs when the theorem asks, not every
time a file that imports this one is loaded.) -/
def first_comms_by_type (_ : Unit) : List (CType × List Nat × Nat) := Id.run do
  let mut out : List (CType × List Nat × Nat) := []
  for x in products_of_two 8 3 do
    let tp := ctype x 3
    let k := first_comms x
    match out.lookup tp with
    | some (ks, n) =>
      out := out.map fun e => if e.1 == tp then (tp, (if ks.contains k then ks else ks ++ [k]), n + 1) else e
    | none => out := out ++ [(tp, [k], 1)]
  return out.mergeSort fun a b => a.2.2 > b.2.2 || (a.2.2 == b.2.2 && decide (a.1.toString ≤ b.1.toString))

end Insertions
