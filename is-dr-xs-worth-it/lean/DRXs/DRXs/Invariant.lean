/-
  DRXs.Invariant — "the signature is a complete invariant", for every state the allowed groups can reach and not
  only for the one state per signature that `fecosets.explore` keeps.  (Not in the Python, which spot-checks it.)

  What has to be shown: whenever a state s is reached from the solved cube by allowed groups (the face axis f
  following along as in `explore`), s has a signature, it is one of the 768 kinds, and each of the 29 groups leads
  from s to the signature that `nbr` records for that kind.  Then everything computed on the 768 kinds (slices,
  turns) is true of every such state.

  There are far too many states to try, but `fe.look` does not see much of a state:
    * it reads s only through `cax s i`, the colour axis of the sticker at place i;
    * its first loop reads the 24 corner places only, and can only say "not a DR-xs";
    * its second loop reads the 24 edge places only, and gives "not a DR-xs" or the signature.
  A face turn carries corner places to corner places and edge places to edge places (theorem
  `moves_keep_corners_and_edges`), so the colours at the corner places after a group depend only on the colours
  at the corner places before it, and the same for the edge places; and which groups are allowed depends only
  on f.  So it is enough to walk
    * the reachable (f, colours at the 24 corner places): `walk corner_places`, and
    * the reachable (f, colours at the 24 edge places):  `walk edge_places`,
  keeping one real state for each and checking that state.  A state s reached by some sequence of groups has its
  (f, corner colours) among the first and its (f, edge colours) among the second; the state kept for the first
  passes `look`'s first loop, so s does; the state kept for the second gets a signature from the second loop, one
  of the kinds, with the transitions `nbr` says, so s does.
-/
import Std.Data.HashSet
import DRXs.Fecosets

namespace DRXs
namespace invariant
open cube fecosets

/-- The 24 places on corner cubies, the 24 places on edge cubies. -/
def corner_places : List Nat := fe.CORNERS.flatMap fe.CUBIES
def edge_places : List Nat := fe.EDGES.flatMap fe.CUBIES

/-- The colour axes of the stickers of s at the given places. -/
def colours (s : State) (places : List Nat) : List Nat := places.map (fe.cax s)

/-- Walk the states reachable from the solved cube by the allowed groups, keeping one state for each
(face axis, colours at `places`).  Every state kept is checked: it must have a signature, the signature must be
one of the kinds, and every allowed group must lead to a state whose signature is the one `nbr` records.
Returns (number of states kept, number of failed checks). -/
def walk (places : List Nat) : Nat × Nat := Id.run do
  let mut seen : Std.HashSet (Nat × List Nat) := {}
  seen := seen.insert (1, colours SOLVED places)
  let mut todo : Array (Nat × State) := #[(1, SOLVED)]
  let mut kept := 0
  let mut failed := 0
  while !todo.isEmpty do
    let (f, s) := todo.back!; todo := todo.pop
    kept := kept + 1
    match sig_of s f with
    | none => failed := failed + 1                           -- s does not look like a DR-xs on faces f
    | some g =>
      if !nbr.contains g then failed := failed + 1           -- a signature that is not one of the kinds
      for (a, txt, cost, sl) in fe.gens f do
        let t := do_ s txt
        let f2 := if sl != 0 then third a f else f
        match sig_of t f2 with
        | none => failed := failed + 1
        | some h =>
          if !(nbr.getD g []).contains (a, txt, cost, sl, h) then
            failed := failed + 1                             -- not where `nbr` says this group leads
        let key := (f2, colours t places)
        if !seen.contains key then
          seen := seen.insert key
          todo := todo.push (f2, t)
  return (kept, failed)

end invariant
end DRXs
