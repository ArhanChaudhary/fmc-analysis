/-
  DRXs.Festeps — the "counted from scratch" part of research/src/festeps.py in Lean: fewest face turns from a
  DR-3s to a DR-2s, from a DR-2s to a DR-1s, and from each to a real DR.

  `to_set` is festeps.to_set; like `fecosets.dijkstra` it is computed by repeating the rule until nothing changes
  (see DRXs/Fecosets.lean), not with a heap.  Left out: `after_quarter` (the saving after a side quarter turn).
-/
import DRXs.Fecosets

namespace DRXs
namespace festeps
open fecosets

/-- dist[(g, last axis)] = fewest turns from kind g to the target set when the previous group was about `last`
(3 = none). -/
def to_set (target : Sig → Bool) : Dist := shortest nbr target (fun cost _sl => cost)

def to1 : Dist := to_set (fun g => slices g <= 1)
def to2 : Dist := to_set (fun g => slices g <= 2)
def to0 : Dist := to_set (fun g => slices g == 0)

/-- `to1[(g, 3)]`: fewest face turns from kind g to a kind that needs at most 1 slice. -/
def turns_to_1s (g : Sig) : Nat := to1.getD (g, 3) INF
/-- `to2[(g, 3)]`: fewest face turns from kind g to a kind that needs at most 2 slices. -/
def turns_to_2s (g : Sig) : Nat := to2.getD (g, 3) INF

end festeps
end DRXs
