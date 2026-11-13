import DRBound.Census.Specs

open DRBound DRBound.Exact DRBound.Census

@[noinline] def stage1 (_ : Unit) : Nat := (baseTabs ()).cmv.size
#eval show IO Unit from do
  let t0 ← IO.monoMsNow
  let bt := baseTabs ()
  IO.println s!"base {bt.cmv.size} {bt.inv.size}"
  let t1 ← IO.monoMsNow
  IO.println s!"baseTabs {t1 - t0} ms"
  let hd := bfs 40320 [0] fun r => halfMoves.map fun m => bt.cmv[m * 40320 + r]!
  let hs : Array Arr8 := ((List.range 40320).filter fun r => hd[r]! != unset).toArray.map unrank8
  let t2 ← IO.monoMsNow
  IO.println s!"hs {hs.size} {t2 - t1} ms"
  let (ccos, ccosRep) := cosetTabs hs
  let t3 ← IO.monoMsNow
  IO.println s!"cosets {ccosRep.size} {ccos.size} {t3 - t2} ms"
  let clen := bfs 40320 [0] fun r => allMoves.map fun m => bt.cmv[m * 40320 + r]!
  let t4 ← IO.monoMsNow
  IO.println s!"clen {clen.foldl max 0} {t4 - t3} ms"
