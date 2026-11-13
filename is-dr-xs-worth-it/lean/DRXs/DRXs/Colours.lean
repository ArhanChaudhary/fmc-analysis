/-
  DRXs.Colours — the kinds of DR-xs state for any colour pair, not only U/D.  `fecosets` fixes the colour axis
  C = 1 (U/D colours); the errata witness B1 is a DR-xs of the F/B colours (C = 2).  This file repeats
  `fecosets.explore`, the slices and turns tables and `invariant.walk` with the colour as a parameter.  The code is
  that of DRXs/Fecosets.lean and DRXs/Invariant.lean with `C` replaced by `c` and the walk started from the real
  DR of colour c (corners on the faces of axis c); nothing else changed.
-/
import Std.Data.HashSet
import DRXs.Invariant

namespace DRXs
namespace colours
open cube fecosets

def sig_of (c : Nat) (s : State) (f : Nat) : Option Sig :=
  match fe.look s c f with
  | none => none
  | some (flips, sl) => some ⟨f, flips, sl⟩

def is_dr (c : Nat) (g : Sig) : Bool := fe.is_dr (c, g.f, g.flips, g.sl)

/-- `fecosets.explore` for colour c. -/
def explore (c : Nat) : Explored := Id.run do
  let start := (sig_of c SOLVED c).get!
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
      match sig_of c t f2 with
      | none => failed := failed + 1
      | some h =>
        out := out ++ [(a, txt, cost, sl, h)]
        if !rep.contains h then
          rep := rep.insert h t; todo := todo.push h
        else if checked < 20000 then
          checked := checked + 1
          let u := rep[h]!
          for (a2, txt2, _, sl2) in (fe.gens h.f).take 6 do
            let f3 := if sl2 != 0 then third a2 h.f else h.f
            let x := sig_of c (do_ t txt2) f3
            if x.isNone || x != sig_of c (do_ u txt2) f3 then
              failed := failed + 1
    nbr := nbr.insert g out
  return ⟨start, rep, nbr, checked, failed⟩

def explored2 : Explored := explore 2
def nbr2 : Std.HashMap Sig (List Edge) := explored2.nbr
def kinds2 : List Sig := nbr2.keys
def dsl2 : Dist := shortest nbr2 (is_dr 2) (fun _cost sl => sl)
def dmv2 : Dist := shortest nbr2 (is_dr 2) (fun cost _sl => cost)
def slices2 (g : Sig) : Nat := dsl2.getD (g, 3) INF
def turns_to_dr2 (g : Sig) : Nat := dmv2.getD (g, 3) INF

/-- `invariant.walk` for colour 2. -/
def walk2 (places : List Nat) : Nat × Nat := Id.run do
  let mut seen : Std.HashSet (Nat × List Nat) := {}
  seen := seen.insert (2, invariant.colours SOLVED places)
  let mut todo : Array (Nat × State) := #[(2, SOLVED)]
  let mut kept := 0
  let mut failed := 0
  while !todo.isEmpty do
    let (f, s) := todo.back!; todo := todo.pop
    kept := kept + 1
    match sig_of 2 s f with
    | none => failed := failed + 1
    | some g =>
      if !nbr2.contains g then failed := failed + 1
      for (a, txt, cost, sl) in fe.gens f do
        let t := do_ s txt
        let f2 := if sl != 0 then third a f else f
        match sig_of 2 t f2 with
        | none => failed := failed + 1
        | some h =>
          if !(nbr2.getD g []).contains (a, txt, cost, sl, h) then
            failed := failed + 1
        let key := (f2, invariant.colours t places)
        if !seen.contains key then
          seen := seen.insert key
          todo := todo.push (f2, t)
  return (kept, failed)

end colours
end DRXs
