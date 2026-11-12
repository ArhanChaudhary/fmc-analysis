/-
  EODR.Eo — EO on one axis, exact over its 2,048 states (the research's `eodrtools eo axis`).

  A state is the 12-bit mask of bad edges for axis Y (`pieces.badMask`); a face turn acts on it by `pieces.EOT`.
  `dist Y` is the BFS table from the solved mask 0 with all 18 face turns: the fewest face turns to EO on Y.

  `counts Y e` = (n₀, …, n₈): the number of canonical sequences of r turns that take mask e to EO for the first time
  at their end (no shorter prefix, the empty one included, is an EO).  Canonical as in the research
  (`common.rs: canon_ok`): no two turns of one face in a row, and of two turns of opposite faces in a row the
  U, R or F turn comes first.  The recursion is `eo.rs: eo_counts`, written over the 4,096 masks:
    f r lf e = number of such sequences of r turns from e when the previous turn was on face lf (6 = none)
    f 0 lf 0 = 1, f 0 lf e = 0 for e ≠ 0, f r lf 0 = 0 for r ≥ 1,
    f r lf e = Σ over turns mv allowed after face lf of f (r-1) (face of mv) (mv applied to e).
-/
import EODR.Pieces
import EODR.Search

namespace EODR
namespace eo
open pieces

def step (Y : Nat) (e mv : Nat) : Nat := EOT[Y]![mv]![e]!
def ALL : List Nat := List.range 18

/-- Fewest face turns to EO on axis Y, for each of the 4,096 masks (255 = not reachable). -/
def dist (Y : Nat) : ByteArray := search.bfs 4096 0 ALL (step Y)

def distRule (Y : Nat) : Bool := search.ruleHolds 4096 0 ALL (step Y) (dist Y)

-- (`dist Y` is a function call: each definition below computes it once with `let` and reads that.)

/-- The masks reached are exactly those with an even number of bad edges. -/
def reachedIsEven (Y : Nat) : Bool :=
  let d := dist Y
  (List.range 4096).all fun e => search.reached d e == (popcount e % 2 == 0)

/-- The reachable masks. -/
def STATES : List Nat := (List.range 4096).filter fun e => popcount e % 2 == 0

/-- (distance, how many of the 2,048 states) for axis Y. -/
def distHist (Y : Nat) : List (Nat × Nat) :=
  let d := dist Y
  hist (STATES.map fun e => (d.get! e).toNat)

/-- For each number of bad edges b: (b, the distance histogram of the states with b bad edges). -/
def distByBad (Y : Nat) : List (Nat × List (Nat × Nat)) :=
  let d := dist Y
  [0, 2, 4, 6, 8, 10, 12].map fun b =>
    (b, hist ((STATES.filter fun e => popcount e == b).map fun e => (d.get! e).toNat))

/-- Σ of the distances over the 2,048 states. -/
def distSum (Y : Nat) : Nat :=
  let d := dist Y
  (STATES.map fun e => (d.get! e).toNat).sum

/-- `canon_ok`: may a turn `mv` follow a turn on face `lf` (6 = no previous turn)? Faces U D R L F B = 0 … 5. -/
def canonOk (lf mv : Nat) : Bool :=
  lf == 6 || !(lf == mv / 3 || (lf / 2 == mv / 3 / 2 && lf > mv / 3))

/-- `counts Y` : for each of the 4,096 masks, [n₀, …, n₈]. -/
def counts (Y : Nat) : Array (Array Nat) := Id.run do
  -- f[lf][e] for the current r
  let mut f : Array (Array Nat) :=
    (Array.range 7).map fun _ => (Array.range 4096).map fun e => if e == 0 then 1 else 0
  let mut out : Array (Array Nat) := (Array.range 4096).map fun e => #[if e == 0 then 1 else 0]
  for _ in [1:9] do
    let g := (Array.range 7).map fun lf => (Array.range 4096).map fun e =>
      if e == 0 then 0 else
        (ALL.filter (canonOk lf)).foldl (fun acc mv => acc + f[mv / 3]![step Y e mv]!) 0
    f := g
    out := (Array.range 4096).map fun e => out[e]!.push g[6]![e]!
  return out

/-- The research's `eo_axis.tsv` row of a state without its first column (the eo coordinate):
[bad, optimal, n₀, …, n₈]. -/
def row (d : ByteArray) (c : Array (Array Nat)) (e : Nat) : List Nat :=
  [popcount e, (d.get! e).toNat] ++ c[e]!.toList

/-- All 2,048 rows, sorted (so the comparison with the file does not depend on how states are numbered). -/
def rows (Y : Nat) : List (List Nat) :=
  let c := counts Y
  let d := dist Y
  (STATES.map (row d c)).mergeSort (fun a b => decide (a ≤ b))

/-- Over the 2,048 states: Σ n_r for r = 0 … 8. -/
def countSums (Y : Nat) : List Nat :=
  let c := counts Y
  (List.range 9).map fun r => (STATES.map fun e => c[e]![r]!).sum
/-- max over the states of n_r, r = 0 … 8. -/
def countMax (Y : Nat) : List Nat :=
  let c := counts Y
  (List.range 9).map fun r => (STATES.map fun e => c[e]![r]!).foldl max 0
/-- max over the states of n₀ + … + n_r (EOs of at most r turns), r = 0 … 8. -/
def cumMax (Y : Nat) : List Nat :=
  let c := counts Y
  (List.range 9).map fun r => (STATES.map fun e => (c[e]!.toList.take (r + 1)).sum).foldl max 0
/-- Σ over the states of n₀ + … + n_r. -/
def cumSums (Y : Nat) : List Nat :=
  let c := counts Y
  (List.range 9).map fun r => (STATES.map fun e => (c[e]!.toList.take (r + 1)).sum).sum
/-- Number of states with no EO of at most r turns, r = 0 … 8. -/
def noneLe (Y : Nat) : List Nat :=
  let c := counts Y
  (List.range 9).map fun r => (STATES.filter fun e => (c[e]!.toList.take (r + 1)).sum == 0).length

end eo
end EODR
