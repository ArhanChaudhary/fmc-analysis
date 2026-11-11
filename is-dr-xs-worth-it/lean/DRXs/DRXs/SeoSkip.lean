/-
  DRXs.SeoSkip — the counting loop of research/src/seo_skip.py in Lean: how often a scramble has a slice-EO skip,
  exact, over every way the twelve edges can be placed and oriented.

  A slice EO is "the four edges belonging to one slice (E, M or S) all oriented, or all misoriented, for one axis
  (U/D, R/L or F/B)": 9 slice-and-axis pairs, each in two flavours, on normal and on inverse.

  Whether a state has one depends only on (a) which kind of piece (E, M or S) sits at each of the 12 edge places
  and (b) the 12 orientation bits for the F/B axis: 34,650 x 2,048 = 70,963,200 equally likely configurations.
    orientation for axis e of a piece of kind t sitting at a place of kind u, F/B bit b:   b ^ g_e(u) ^ g_e(t)
    with g_FB = 0, g_UD = 1 on M places / M pieces, g_RL = 1 on E places / E pieces
  On inverse the roles of "kind of the place" and "kind of the piece" swap.

  This file takes that rule as given and counts.  It uses no stickers and no moves; from the cube model it takes
  only the order of the twelve edge places (`fe.EDGES`), to know which place is of which kind, as the Python does.
  (seo_skip.check_rule, which tries the rule on 200 random states of the sticker model, is not redone here.)

  Python -> Lean:
    numpy does all 2048 orientation vectors of a placement at once; here they are an inner loop `for b in bits`.
    `o = bits[:, idx] ^ g; sm = o.sum(axis=1)`   `osum b idx g`, written out for the four places of `idx`
    `hist['normal']`, `hist['both']`              `hn`, `hb`: entry k = configurations with exactly k skips
  Left out: `count_each` (each single slice EO), and the 'oriented only' histograms.
-/
import DRXs.Fe

-- Without this the compiler would move the whole count, which depends on nothing, out of `main` and run it
-- every time this file is loaded.
set_option compiler.extract_closed false

namespace DRXs
namespace seo_skip

/-- kind of each edge place -/
def KIND : List Char := fe.EDGES.map fun p => if p[1]! == 0 then 'E' else if p[0]! == 0 then 'M' else 'S'

/-- `G[e][t]`: g_e of a place or piece of kind t. -/
def G (e : String) (t : Char) : Nat :=
  if e == "UD" then (if t == 'M' then 1 else 0)
  else if e == "RL" then (if t == 'E' then 1 else 0)
  else 0                                                    -- "FB"

/-- `itertools.combinations(l, k)`, in the same order. -/
def combinations : List Nat → Nat → List (List Nat)
  | _, 0 => [[]]
  | [], _ + 1 => []
  | x :: xs, k + 1 => (combinations xs k).map (x :: ·) ++ combinations xs (k + 1)

def slots : List Nat := List.range 12

/-- `bits[v]`: the 12 orientation bits number v, the last one making the number of 1s even.  2048 x 12. -/
def bits : Array (Array Nat) := (Array.range 2048).map fun v =>
  let first := (List.range 11).map fun i => (v >>> i) &&& 1
  (first ++ [first.sum % 2]).toArray

/-- For one placement, the 18 slice-and-axis pairs as (idx, g): `idx` the four places looked at, `g` what to
xor onto their bits.  Order as in the Python: normal then inverse, T in "EMS", e in ("UD", "RL", "FB"). -/
def events (kind_at : List Char) : Array (Array Nat × Array Nat) := Id.run do
  let mut ev := #[]
  for side in ["normal", "inverse"] do
    for T in ['E', 'M', 'S'] do
      let idx :=
        if side == "normal" then slots.filter fun i => kind_at[i]! == T    -- places holding the T pieces
        else slots.filter fun i => KIND[i]! == T                            -- the T places
      for e in ["UD", "RL", "FB"] do
        let g := idx.map fun i => G e KIND[i]! ^^^ G e kind_at[i]!
        ev := ev.push (idx.toArray, g.toArray)
  return ev

/-- `sum(b[i] ^ g for i, g in zip(idx, g))` for the four places: how many of the four edges are misoriented. -/
def osum (b idx g : Array Nat) : Nat :=
  (b[idx[0]!]! ^^^ g[0]!) + (b[idx[1]!]! ^^^ g[1]!) + (b[idx[2]!]! ^^^ g[2]!) + (b[idx[3]!]! ^^^ g[3]!)

/-- Among the pairs number lo … hi-1 of `ev`: how many slice EOs the orientation bits `b` have (a pair counts
once if its four edges are all oriented, `sm == 0`, and once if all misoriented, `sm == 4`). -/
def skips (ev : Array (Array Nat × Array Nat)) (b : Array Nat) (lo hi : Nat) : Nat := Id.run do
  let mut n := 0
  for k in [lo:hi] do
    let (idx, g) := ev[k]!
    let sm := osum b idx g
    if sm == 0 || sm == 4 then n := n + 1
  return n

structure Counts where
  /-- configurations looked at -/
  tot : Nat
  /-- (k, number of configurations with exactly k slice-EO skips on normal), for the k that occur -/
  hist_normal : List (Nat × Nat)
  /-- the same, counting skips on normal and on inverse together -/
  hist_both : List (Nat × Nat)
  deriving DecidableEq, Repr

/-- A list of counts as the (k, count) pairs with count > 0. -/
def items (h : Array Nat) : List (Nat × Nat) := ((List.range h.size).map fun k => (k, h[k]!)).filter (·.2 != 0)

def main (_ : Unit) : Counts := Id.run do
  let mut tot := 0
  let mut hn := Array.replicate 19 0
  let mut hb := Array.replicate 37 0
  for E in combinations slots 4 do
    let rest := slots.filter fun i => !E.contains i
    for Mi in combinations rest 4 do
      -- kind_at[i] = 'E' for i in E, 'M' for i in Mi, 'S' for the four places left
      let kind_at := slots.map fun i => if E.contains i then 'E' else if Mi.contains i then 'M' else 'S'
      let ev := events kind_at
      for b in bits do
        let nn := skips ev b 0 9                 -- on normal
        let nb := nn + skips ev b 9 18           -- on normal or inverse
        hn := hn.modify nn (· + 1)
        hb := hb.modify nb (· + 1)
        tot := tot + 1
  return ⟨tot, items hn, items hb⟩

/-- Configurations with no slice-EO skip on normal. -/
def Counts.none_normal (r : Counts) : Nat := (r.hist_normal.lookup 0).getD 0
/-- Configurations with no slice-EO skip on normal or inverse. -/
def Counts.none_both (r : Counts) : Nat := (r.hist_both.lookup 0).getD 0

end seo_skip
end DRXs
