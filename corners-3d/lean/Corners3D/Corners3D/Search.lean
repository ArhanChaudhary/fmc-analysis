/-
  Corners3D.Search — copied, unchanged but for the namespace, from CornersHTR (corners-htr/lean/CornersHTR/CornersHTR/Search.lean;
  the 88 million states its comments mention are that study's: here there are 3,674,160).  Breadth-first search over states 0 … n-1 given by a step function, and independent checks of
  the tables it fills in.  `step x mv` is the state after doing move `mv` to state x.

  `bfs` writes, for every state reached from the sources, the fewest moves from a source (255 = not reached),
  by scanning the whole array once per level (no queue: the state spaces here are 88 million states).

  The checks do not trust the code that filled the tables.

  `distRule n goal moves step d` holds when, for every state x:
    * d x is filled in (every state is reached);
    * d x = 0 exactly when `goal x`;
    * d x ≤ d (step x mv) + 1 for every move;
    * if d x > 0, some move leads to a state with d = d x - 1.
  The fourth point gives a sequence of d x moves from x into the goal set; the third, followed along any sequence
  of k moves from x into the goal set, gives d x ≤ k.  So d x is exactly the fewest moves from x into the goal set.

  `qtRule n goal moves w step q` is the same for a cost w(mv) ∈ {0, 1} per move (here: 1 for a quarter turn, 0 for
  a half turn), where a zero-cost move can't serve as the step down by itself:
    * q x is filled in; q x = 0 exactly when `goal x`;
    * q x ≤ q (step x mv) + w mv for every move (lower bound, as above);
    * every x with q x = k > 0 reaches, by zero-cost moves through states with q = k only, a state that has a
      cost-1 move to a state with q = k - 1.  The zero-cost moves used here must be their own inverses (half
      turns are), so this is checked by marking those exit states and spreading the mark along zero-cost moves.
  So q x is exactly the fewest cost-1 moves over all sequences from x into the goal set.

  `optRule … d w q'` checks q' x = 0 on the goal set and, for d x > 0, q' x = the least q' y + w mv over the moves
  with d y = d x - 1.  With d exact, by induction on d, q' x is the fewest cost-1 moves among the shortest sequences.
-/
namespace Corners3D
namespace search

def full (n : Nat) (v : UInt8) : ByteArray := Id.run do
  let mut d := ByteArray.emptyWithCapacity n
  for _ in [0:n] do d := d.push v
  return d

def bfs (n : Nat) (srcs : List Nat) (moves : List Nat) (step : Nat → Nat → Nat) : ByteArray := Id.run do
  let mut d := full n 255
  for s in srcs do d := d.set! s 0
  let mut k : UInt8 := 0
  let mut grew := true
  while grew do
    grew := false
    for x in [0:n] do
      if d.get! x == k then
        for mv in moves do
          let y := step x mv
          if d.get! y == 255 then
            d := d.set! y (k + 1)
            grew := true
    k := k + 1
  return d

def distRule (n : Nat) (goal : Nat → Bool) (moves : List Nat) (step : Nat → Nat → Nat) (d : ByteArray) : Bool :=
  Id.run do
  if d.size != n then return false
  for x in [0:n] do
    let dx := (d.get! x).toNat
    if dx == 255 then return false
    if goal x != (dx == 0) then return false
    for mv in moves do
      let dy := (d.get! (step x mv)).toNat
      if dy == 255 || dx > dy + 1 then return false
    if dx > 0 && !(moves.any fun mv => (d.get! (step x mv)).toNat + 1 == dx) then return false
  return true

/-- Fewest cost-1 moves into the goal set, by levels: close each level under the zero-cost moves, then step out
with the cost-1 moves. -/
def bfs01 (n : Nat) (srcs : List Nat) (moves : List Nat) (w : Nat → Nat) (step : Nat → Nat → Nat) : ByteArray :=
  Id.run do
  let zero := moves.filter (w · == 0)
  let one := moves.filter (w · == 1)
  let mut q := full n 255
  for s in srcs do q := q.set! s 0
  let mut k : UInt8 := 0
  let mut more := true
  while more do
    let mut grew := true
    while grew do
      grew := false
      for x in [0:n] do
        if q.get! x == k then
          for mv in zero do
            let y := step x mv
            if q.get! y == 255 then
              q := q.set! y k
              grew := true
    more := false
    for x in [0:n] do
      if q.get! x == k then
        for mv in one do
          let y := step x mv
          if q.get! y == 255 then
            q := q.set! y (k + 1)
            more := true
    k := k + 1
  return q

def qtRule (n : Nat) (goal : Nat → Bool) (moves : List Nat) (w : Nat → Nat) (step : Nat → Nat → Nat)
    (q : ByteArray) : Bool := Id.run do
  if q.size != n then return false
  let zero := moves.filter (w · == 0)
  let one := moves.filter (w · == 1)
  -- zero-cost moves are their own inverses
  for x in [0:n] do
    for mv in zero do
      if step (step x mv) mv != x then return false
  -- filled in, goal ⇔ 0, lower-bound inequality; mark the exits
  let mut mark := full n 0
  for x in [0:n] do
    let qx := (q.get! x).toNat
    if qx == 255 then return false
    if goal x != (qx == 0) then return false
    for mv in moves do
      let qy := (q.get! (step x mv)).toNat
      if qy == 255 || qx > qy + w mv then return false
    if qx > 0 && one.any (fun mv => (q.get! (step x mv)).toNat + 1 == qx) then mark := mark.set! x 1
  -- spread the mark along zero-cost moves inside a level
  let mut grew := true
  while grew do
    grew := false
    for x in [0:n] do
      if mark.get! x == 1 then
        for mv in zero do
          let y := step x mv
          if mark.get! y == 0 && q.get! y == q.get! x then
            mark := mark.set! y 1
            grew := true
  for x in [0:n] do
    if q.get! x != 0 && mark.get! x == 0 then return false
  return true

/-- Fewest cost-1 moves among the shortest sequences, by levels of d. -/
def optQt (n : Nat) (d : ByteArray) (moves : List Nat) (w : Nat → Nat) (step : Nat → Nat → Nat) : ByteArray :=
  Id.run do
  let mut q := full n 255
  let mut maxd : UInt8 := 0
  for x in [0:n] do
    if d.get! x == 0 then q := q.set! x 0
    if d.get! x > maxd then maxd := d.get! x
  for k in [1:maxd.toNat + 1] do
    for x in [0:n] do
      if (d.get! x).toNat == k then
        let mut best := 255
        for mv in moves do
          let y := step x mv
          if (d.get! y).toNat + 1 == k then best := min best ((q.get! y).toNat + w mv)
        q := q.set! x best.toUInt8
  return q

def optRule (n : Nat) (goal : Nat → Bool) (moves : List Nat) (w : Nat → Nat) (step : Nat → Nat → Nat)
    (d q : ByteArray) : Bool := Id.run do
  if q.size != n then return false
  for x in [0:n] do
    let dx := (d.get! x).toNat
    let qx := (q.get! x).toNat
    if dx == 0 then
      if qx != 0 || !goal x then return false
    else
      let mut best := 255
      for mv in moves do
        let y := step x mv
        if (d.get! y).toNat + 1 == dx then best := min best ((q.get! y).toNat + w mv)
      if best == 255 || qx != best then return false
  return true

/-- Histogram of the entries (index = value), trailing zeros dropped. -/
def hist (d : ByteArray) : List Nat := Id.run do
  let mut h := Array.replicate 256 0
  for x in [0:d.size] do
    let v := (d.get! x).toNat
    h := h.set! v (h[v]! + 1)
  let mut l := h.toList.reverse.dropWhile (· == 0)
  return l.reverse

/-- Joint counts: rows = value in a, columns = value in b. -/
def joint (a b : ByteArray) (ra rb : Nat) : List (List Nat) := Id.run do
  let mut t := Array.replicate (ra * rb) 0
  for x in [0:a.size] do
    let i := (a.get! x).toNat * rb + (b.get! x).toNat
    t := t.set! i (t[i]! + 1)
  return (List.range ra).map fun r => (List.range rb).map fun c => t[r * rb + c]!

end search
end Corners3D
