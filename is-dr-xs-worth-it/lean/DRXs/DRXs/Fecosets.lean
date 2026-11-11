/-
  DRXs.Fecosets — research/src/fecosets.py in Lean: every kind of DR-xs state (U/D colours on some pair of faces,
  slice pieces in their slice, any flips), and for each the fewest slices and the fewest face turns to a real DR
  using only DR-xs moves: turns of the two oriented faces, half turns of the others, and slice turns written as two
  outer turns (R L', F B, ...).

  The kind of a state is its signature (fe.look with c = U/D colours): which faces the corners are oriented on,
  which of the eight layer-edge places hold a flipped edge, and the four slice bits.  Costs are counted in face
  turns with all cancelling done: consecutive turns about one axis are one group (R2 then R L' is R' L', two turns).

  Python -> Lean:
    the signature (f, flips, slice)     `Sig`, with fields `g.f`, `g.flips`, `g.sl` for Python's g[0], g[1], g[2]
    dict                                `Std.HashMap` (Lean's hash table): `d[k]!`, `d.getD k default`, `d.insert k v`
    `todo` (a list used as a stack)     an `Array`: `todo.back!` + `todo.pop` is Python's `todo.pop()`
    `assert`                            counted in `failed` (theorem `explore_asserts_hold`: it stays 0)
    `l[:6]`                             `l.take 6`

  Where this file differs from fecosets.py (the result is the same table):
    * `dijkstra` is not Dijkstra's algorithm with a heap.  It repeats the rule written in the Python comment,
          d(g, last) = 0 if g is a DR, else min over the groups of g about an axis a != last of w + d(h, a),
      over all (g, last) until no entry changes (`shortest`).  Entries start at INF and only ever take the cost of
      an actual sequence of groups, so what is left when nothing changes is the fewest.
    * `sig_of` returns `none` where the Python assert would fail, and `explore` counts such cases in `failed`
      and goes on.  (The spot check inside `explore` is the Python's, the first 20000 times and 6 groups each;
      the complete check, for every reachable state, is in DRXs/Invariant.lean.)
    * `best_move` / `path` (the move sequences) are left out.
-/
import Std.Data.HashMap
import DRXs.Fe

namespace DRXs
namespace fecosets
open cube

/-- The colour axis: U/D colours. -/
def C : Nat := 1

/-- The kind of a DR-xs state: face axis of the corners, 8 flip bits, 4 slice bits. -/
structure Sig where
  f : Nat
  flips : List Nat
  sl : List Nat
  deriving DecidableEq, Hashable, Repr, Inhabited

/-- `(f,) + fe.look(s, C, f)`; `none` where the Python assert would fail. -/
def sig_of (s : State) (f : Nat) : Option Sig :=
  match fe.look s C f with
  | none => none
  | some (flips, sl) => some ⟨f, flips, sl⟩

def third (a b : Nat) : Nat := 3 - a - b

/-- `fe.is_dr((C,) + g)` -/
def is_dr (g : Sig) : Bool := fe.is_dr (C, g.f, g.flips, g.sl)

/-- One allowed group of turns from a kind: (axis, text, cost in face turns, slices, the kind it leads to). -/
abbrev Edge := Nat × String × Nat × Nat × Sig

structure Explored where
  start : Sig
  /-- one state for each signature -/
  rep : Std.HashMap Sig State
  /-- the groups of turns out of each signature -/
  nbr : Std.HashMap Sig (List Edge)
  /-- how many times a signature reached again through another state was compared (at most 20000) -/
  checked : Nat
  /-- how many Python asserts would have failed -/
  failed : Nat

def explore : Explored := Id.run do
  let start := (sig_of SOLVED 1).get!
  let mut rep : Std.HashMap Sig State := {}
  rep := rep.insert start SOLVED
  let mut nbr : Std.HashMap Sig (List Edge) := {}
  let mut todo : Array Sig := #[start]
  let mut checked := 0
  let mut failed := 0
  while !todo.isEmpty do
    let g := todo.back!; todo := todo.pop
    let s := rep[g]!
    let mut out : List Edge := []
    for (a, txt, cost, sl) in fe.gens g.f do
      let t := do_ s txt
      let f2 := if sl != 0 then third a g.f else g.f
      match sig_of t f2 with
      | none => failed := failed + 1                         -- assert r is not None
      | some h =>
        out := out ++ [(a, txt, cost, sl, h)]
        if !rep.contains h then
          rep := rep.insert h t; todo := todo.push h
        else if checked < 20000 then
          -- same signature reached through another state: its moves must lead to the same signatures
          checked := checked + 1
          let u := rep[h]!
          for (a2, txt2, _, sl2) in (fe.gens h.f).take 6 do
            let f3 := if sl2 != 0 then third a2 h.f else h.f
            let x := sig_of (do_ t txt2) f3
            if x.isNone || x != sig_of (do_ u txt2) f3 then
              failed := failed + 1                           -- 'signature is not a complete invariant'
    nbr := nbr.insert g out
  return ⟨start, rep, nbr, checked, failed⟩

/-- `dist[(sig, last axis)]`; last axis 3 = free start.  A missing entry counts as INF. -/
abbrev Dist := Std.HashMap (Sig × Nat) Nat
def INF : Nat := 10 ^ 9

/-- The rule:  d(g, last) = 0 if g is in the target, else the least  weight(cost, slices) + d(h, a)  over the
groups (a, _, cost, slices, h) out of g about an axis a != last. -/
def rule (target : Sig → Bool) (weight : Nat → Nat → Nat) (dist : Dist) (g : Sig) (out : List Edge) (last : Nat) :
    Nat := Id.run do
  if target g then return 0
  let mut d := INF
  for (a, _, cost, sl, h) in out do
    if a == last then continue
    let nd := weight cost sl + dist.getD (h, a) INF
    if nd < d then d := nd
  return d

/-- Fewest total weight from every (kind, last axis) to the target set, two consecutive groups never about the
same axis: repeat the rule until no entry changes. -/
def shortest (nbr : Std.HashMap Sig (List Edge)) (target : Sig → Bool) (weight : Nat → Nat → Nat) : Dist :=
  Id.run do
    let mut dist : Dist := {}
    let mut changed := true
    while changed do
      changed := false
      for (g, out) in nbr do
        for last in [0, 1, 2, 3] do
          let d := rule target weight dist g out last
          if d < dist.getD (g, last) INF then
            dist := dist.insert (g, last) d
            changed := true
    return dist

/-- Does every entry of the finished table equal what the rule gives from the table? -/
def satisfies_rule (nbr : Std.HashMap Sig (List Edge)) (target : Sig → Bool) (weight : Nat → Nat → Nat)
    (dist : Dist) : Bool :=
  nbr.toList.all fun (g, out) =>
    [0, 1, 2, 3].all fun last => dist.getD (g, last) INF == rule target weight dist g out last

/-- dist[(sig, last axis)] to a real DR; last axis 3 = free start.  weight(cost, slices) -> edge weight. -/
def dijkstra (nbr : Std.HashMap Sig (List Edge)) (weight : Nat → Nat → Nat) : Dist :=
  shortest nbr is_dr weight

/-- `sorted(collections.Counter(l).items())`: each value that occurs, with how often. -/
def hist (l : List Nat) : List (Nat × Nat) :=
  (l.eraseDups.mergeSort (fun a b => decide (a ≤ b))).map fun k => (k, l.count k)

/-! The run (the `__main__` part of fecosets.py). -/

def explored : Explored := explore
def nbr : Std.HashMap Sig (List Edge) := explored.nbr
/-- All kinds found (in no particular order). -/
def kinds : List Sig := nbr.keys

/-- fewest slices to a real DR -/
def dsl : Dist := dijkstra nbr (fun _cost sl => sl)
/-- fewest face turns to a real DR -/
def dmv : Dist := dijkstra nbr (fun cost _sl => cost)

/-- `dsl[(g, 3)]`: the fewest slice groups from kind g to a real DR ("g is a DR-1s / 2s / 3s"). -/
def slices (g : Sig) : Nat := dsl.getD (g, 3) INF
/-- `dmv[(g, 3)]`: the fewest face turns from kind g to a real DR. -/
def turns_to_dr (g : Sig) : Nat := dmv.getD (g, 3) INF
/-- The kinds that need exactly n slices. -/
def kinds_with_slices (n : Nat) : List Sig := kinds.filter fun g => slices g == n

end fecosets
end DRXs
