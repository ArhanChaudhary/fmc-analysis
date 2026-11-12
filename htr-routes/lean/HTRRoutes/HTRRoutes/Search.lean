/-
  HTRRoutes.Search — breadth-first search over a finite state space given by a step function, and an independent
  check of the table it fills in.  (EODR's `Search.lean`, with a set of goals instead of one.)

  States are 0 … n-1; `step x mv` is the state after move `mv`.  `bfs` writes, for every state reached from one of
  the `goals`, the number of moves of the shortest sequence from a goal to it (255 = not reached).

  `ruleHolds` does not trust `bfs`.  It checks, for every state x with an entry:
    * x is a goal exactly when its entry is 0;
    * every move leads to a state with an entry, and d x ≤ d (step x mv) + 1;
    * if x is not a goal, some move leads to a state with entry d x - 1.
  The third point gives a sequence of d x moves from x to a goal; the second, followed along any sequence of k moves
  from x to a goal, gives d x ≤ k.  So when `ruleHolds` is true, d x is exactly the fewest moves that take x to a
  goal (moves applied forwards, after x), for every x with an entry, whatever `bfs` did.  The second point also
  says the states with an entry are closed under the moves.  (All move sets used here are closed under inverses,
  so a state without an entry cannot reach a goal either.)
-/
namespace HTRRoutes
namespace search

def bfs (n : Nat) (goals : List Nat) (moves : List Nat) (step : Nat → Nat → Nat) : ByteArray := Id.run do
  let mut d := ByteArray.emptyWithCapacity n
  for _ in [0:n] do d := d.push 255
  let mut q : Array Nat := #[]
  for g in goals do
    if d.get! g == 255 then
      d := d.set! g 0
      q := q.push g
  let mut head := 0
  while head < q.size do
    let x := q[head]!
    head := head + 1
    let dx := d.get! x
    for mv in moves do
      let y := step x mv
      if d.get! y == 255 then
        d := d.set! y (dx + 1)
        q := q.push y
  return d

def ruleHolds (n : Nat) (isGoal : Nat → Bool) (moves : List Nat) (step : Nat → Nat → Nat) (d : ByteArray) :
    Bool := Id.run do
  if d.size != n then return false
  for x in [0:n] do
    let dx := (d.get! x).toNat
    if dx == 255 then continue
    if isGoal x != (dx == 0) then return false
    for mv in moves do
      let dy := (d.get! (step x mv)).toNat
      if dy == 255 || dx > dy + 1 then return false
    if !isGoal x && !(moves.any fun mv => (d.get! (step x mv)).toNat + 1 == dx) then return false
  return true

/-- The states with an entry. -/
def reached (d : ByteArray) (x : Nat) : Bool := d.get! x != 255

/-- Histogram of the entries: (distance, how many states), for the distances that occur. -/
def distHist (d : ByteArray) : List (Nat × Nat) := Id.run do
  let mut h := Array.replicate 256 0
  for i in [0:d.size] do
    let v := (d.get! i).toNat
    if v != 255 then h := h.modify v (· + 1)
  return ((List.range 255).map fun v => (v, h[v]!)).filter (·.2 != 0)

end search
end HTRRoutes
