/-
  HTRRoutes.QtCosets — which HTR cosets are one and two quarter turns from HTR (E: reductions to 1q and 2q).

  On the 29,400 HTR cosets of `Cosets.lean` (moves act on the right, as there):
    S0 = the coset of the solved cube (half turns keep it: a half turn of an HTR state is an HTR state);
    S1 = the half-turn closure of S0 followed by one quarter turn;
    S2 = the half-turn closure of S1 followed by one quarter turn, without S0 and S1.
  A state's coset is in S1 exactly when the state is h · q · h' (h, h' products of half turns, q a quarter turn),
  i.e. when one quarter turn and half turns finish it; S2 likewise for two quarter turns and no fewer.

  `closure` is `search.bfs` with the six half turns; `closedUnderHalf` checks that what it marks is closed under the
  half turns, and it only ever marks a start or a half turn of something marked, so it is exactly the closure (the
  argument is in this header, not a Lean theorem).
-/
import HTRRoutes.Cosets

set_option compiler.extract_closed false

namespace HTRRoutes
namespace qtcos
open pieces corners cosets

def st : Nat → Nat → Nat := stepWith CCM MM
/-- every valid HTR coset (the full BFS of `cosets.run`) -/
def ALL : ByteArray := search.bfs N [GOAL] (List.range 10) st
def valid (x : Nat) : Bool := search.reached ALL x

def closure (starts : List Nat) : ByteArray := search.bfs N starts HALF st
def closedUnderHalf (d : ByteArray) : Bool :=
  (List.range N).all fun x => !search.reached d x || HALF.all fun m => search.reached d (st x m)

def S1D : ByteArray := closure (QT.map (st GOAL))
def s1 (x : Nat) : Bool := search.reached S1D x
def S2D : ByteArray :=
  closure (((List.range N).filter s1).flatMap fun x => QT.map (st x))
def s2 (x : Nat) : Bool := search.reached S2D x && !s1 x && x != GOAL

def lab (x : Nat) : String := label REPS[x / 256]! (x % 256)

/-- (label, cosets) over a set, sorted -/
@[noinline] def tallyOf (p : Nat → Bool) : List (String × Nat) := Id.run do
  let mut rows : List String := []
  for x in [0:N] do
    if valid x && p x then rows := lab x :: rows
  let keys := rows.eraseDups.mergeSort fun a b => decide (a < b)
  return keys.map fun k => (k, rows.count k)

end qtcos

end HTRRoutes
