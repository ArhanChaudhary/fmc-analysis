/-
  HTFirst.ExampleDefs — what `HTFirst.Examples` computes on a worked DR (in a module of its own so that
  `native_decide` runs it compiled).
-/
import HTFirst.Theorems
import HTFirst.Finishes
import HTFirst.Data

namespace HTFirst
open DRBound HTRRoutes

/-- How many of U U' D D' lower the corners' count at once. -/
def lowNow (g : State) : Nat :=
  ([Move.U, .U', .D, .D'].filter fun m => cornerQt (g.move m) + 1 == cornerQt g).length
/-- The corner subset (14 names: 4a3 / 4b3 and 4a4 / 4b4 by the side's own letter). -/
def cornerSubset (g : State) : String := corners.NAMES[corners.sub corners.REPS[cosetOf g / 256]!]!
/-- The corner subsets those quarter turns lead to. -/
def lowersTo (g : State) : List String :=
  ([Move.U, .U', .D, .D'].filter fun m => cornerQt (g.move m) + 1 == cornerQt g).map fun m =>
    cornerSubset (g.move m)

/-- Everything the page prints about one worked DR, but the optimal and the completeness of the list. -/
def exOK (c : Ex) : Bool :=
  let g := st c.scr
  let h := stInv c.scr
  subset48 g == c.row && subset48 h == c.row &&
  (c.fin.all fun f =>
    let w := drMoves f.1
    g.apply w == solved && w.length == c.opt && h.apply (w.reverse.map inv) == solved &&
      lead w == f.2.1 && trail w == f.2.2.1 && quarterTurns w == f.2.2.2) &&
  setup g == c.setupN && setup h == c.setupI && lowNow g == c.lowN && lowNow h == c.lowI &&
  ready g == (c.setupN == 0) && ready h == (c.setupI == 0) &&
  qtFull g == c.qtf && qtFull h == c.qtf && cornerQt g == c.qtf && cornerQt h == c.qtf &&
  c.noExtra == c.fin.any fun f => f.2.2.2 == c.qtf

end HTFirst
