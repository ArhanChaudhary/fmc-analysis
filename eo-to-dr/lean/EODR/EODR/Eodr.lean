/-
  EODR.Eodr — EO → DR, exact: with F/B EO solved, the fewest turns that keep it (all turns of U, D, R, L and the
  half turns F2, B2) to DR on U/D, over every (corner twists, places of the E-slice pieces).  This is the eo = 0
  part of the research's table `eo-fb_dr.u8` (Cale's 1,082,565 states) and `eodrtools eodr exact`'s options
  "eo", "eo_switchF", "eo_switchB".

  State x = co · 4096 + m:  co = Σ twist_c · 3^c over the 8 corner places (0 … 6560), m = 12-bit mask of the places
  holding E-slice pieces.  A face turn acts by `pieces.coAct`, `pieces.maskAct`.  The goal (DR on U/D) is co = 0,
  m = the four E-slice places.  `dist` is the BFS table from the goal with the 14 turns; `search.ruleHolds` checks
  it independently, so an entry is the fewest such turns from that state to DR.

  Case xcye (as in the research, Cale's "DR setup stats"): x = corners with twist ≠ 0, y = 2 x the E-slice pieces
  outside the E slice.  Last-move inversion: the same EO with its last F (or B) quarter turn turned the other way
  = the state after F2 (B2); the option's value is the better of the two.
-/
import EODR.Pieces
import EODR.Search

set_option compiler.extract_closed false

namespace EODR
namespace eodr
open pieces

/-- The 14 turns that keep F/B EO: U, D, R, L turns and F2, B2 (indices in `NAMES`). -/
def KEEP : List Nat := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 16]
def F2 : Nat := 13
def B2 : Nat := 16

def N : Nat := 6561 * 4096

def step (cot mt : Array (Array Nat)) (x mv : Nat) : Nat := cot[mv]![x / 4096]! * 4096 + mt[mv]![x % 4096]!

def COT : Array (Array Nat) := (Array.range 18).map fun mv => (Array.range 6561).map (coAct mv)
def MT : Array (Array Nat) := (Array.range 18).map fun mv => (Array.range 4096).map (maskAct mv)

def GOAL : Nat := E_HOME

/-- The digits of a twist number. -/
def twists (co : Nat) : List Nat := (List.range 8).map fun c => (co / 3 ^ c) % 3

/-- The 1,082,565 states one expects: twists summing to 0 mod 3, and four places marked. -/
def valid (x : Nat) : Bool := (twists (x / 4096)).sum % 3 == 0 && popcount (x % 4096) == 4

def caseOf (x : Nat) : Nat × Nat :=
  ((twists (x / 4096)).countP (· != 0), 2 * popcount ((x % 4096) &&& (4095 - E_HOME)))

-- Per twist number and per mask: valid?, twisted corners, E-slice pieces outside the E slice.  Top-level constants
-- (computed once) on purpose: a `let` inside `run` can be inlined into the loop body and recomputed at every step.
def CO_OK : Array Bool := (Array.range 6561).map fun co => (twists co).sum % 3 == 0
def CO_BAD : Array Nat := (Array.range 6561).map fun co => (twists co).countP (· != 0)
def M_OK : Array Bool := (Array.range 4096).map fun m => popcount m == 4
def M_OUT : Array Nat := (Array.range 4096).map fun m => popcount (m &&& (4095 - E_HOME))

structure Result where
  /-- the table satisfies the rule of `search.ruleHolds` -/
  rule : Bool
  /-- the states with an entry are exactly the `valid` ones -/
  reachedIsValid : Bool
  /-- how many states have an entry -/
  states : Nat
  /-- (corners, edges, option, [states at distance 0, …, 11]) for each case that occurs; options "eo",
  "eo_switchF", "eo_switchB" -/
  byCase : List (Nat × Nat × String × List Nat)
  deriving DecidableEq, Repr

/-- The tally over the states x < n of a filled-in table d.  A separate function, not inlined, on purpose: written
inside `run`, the compiler moved the computation of d into the loop body and redid the BFS at every step. -/
@[noinline] def tally (st : Nat → Nat → Nat) (d : ByteArray) (n : Nat) :
    Bool × Nat × List (Nat × Nat × String × List Nat) := Id.run do
  let coOk := CO_OK
  let coBad := CO_BAD
  let mOk := M_OK
  let mOut := M_OUT
  let mut ok := true
  let mut states := 0
  -- t[(bc * 5 + be) * 3 + option][distance]
  let mut t : Array (Array Nat) := Array.replicate (9 * 5 * 3) (Array.replicate 12 0)
  for x in [0:min n N] do
    let r := search.reached d x
    if r != (coOk[x / 4096]! && mOk[x % 4096]!) then ok := false     -- `valid x`, from the tables
    if !r then continue
    states := states + 1
    let bc := coBad[x / 4096]!                                          -- `caseOf x`, from the tables
    let be := mOut[x % 4096]!
    let v := (d.get! x).toNat
    let vf := min v (d.get! (st x F2)).toNat
    let vb := min v (d.get! (st x B2)).toNat
    let base := (bc * 5 + be) * 3
    t := t.modify base (·.modify v (· + 1))
    t := t.modify (base + 1) (·.modify vf (· + 1))
    t := t.modify (base + 2) (·.modify vb (· + 1))
  let names := ["eo", "eo_switchF", "eo_switchB"]
  let mut rows := []
  for bc in [0:9] do
    for be in [0:5] do
      for o in [0:3] do
        let row := t[(bc * 5 + be) * 3 + o]!
        if row.toList.sum > 0 then rows := rows ++ [(bc, 2 * be, names[o]!, row.toList)]
  return (ok, states, rows)

/-- `run n`: the BFS table, its check, and the tally of the states x < n (the theorems use n = N, all of them). -/
def run (n : Nat) : Result :=
  let st := step COT MT
  let d := search.bfs N GOAL KEEP st
  let rule := search.ruleHolds N GOAL KEEP st d
  let (ok, states, rows) := tally st d n
  ⟨rule, ok, states, rows⟩

/-! Readings of the per-case table -/

/-- Sum of the rows of one option: the distance histogram over all states, [d = 0, …, 11]. -/
def total (rows : List (Nat × Nat × String × List Nat)) (opt : String) : List Nat :=
  (rows.filter (·.2.2.1 == opt)).foldl (fun acc r => (List.zipWith (· + ·) acc r.2.2.2)) (List.replicate 12 0)
/-- One case's row. -/
def caseRow (rows : List (Nat × Nat × String × List Nat)) (bc e : Nat) (opt : String) : List Nat :=
  ((rows.find? fun r => r.1 == bc && r.2.1 == e && r.2.2.1 == opt).map (·.2.2.2)).getD []
/-- Σ d · count. -/
def weighted (h : List Nat) : Nat := ((List.range h.length).map fun i => i * h[i]!).sum

/-! Corner twists alone (over the 2,187 twist vectors with sum ≡ 0 mod 3) -/

def CO_VALID : List Nat := (List.range 6561).filter fun co => (twists co).sum % 3 == 0
/-- (number of twisted corners, how many twist vectors). -/
def twistedHist : List (Nat × Nat) := hist (CO_VALID.map fun co => (twists co).countP (· != 0))
/-- Six twisted corners: (all six the same way, three one way and three the other). -/
def sixTwisted : Nat × Nat :=
  let six := CO_VALID.filter fun co => (twists co).countP (· != 0) == 6
  ((six.filter fun co => (twists co).countP (· == 1) == 6 || (twists co).countP (· == 2) == 6).length,
   (six.filter fun co => (twists co).countP (· == 1) == 3).length)

end eodr
end EODR
