import DRBound.Census.Specs

open DRBound DRBound.Exact DRBound.Census

def outDir : String := "/data/disk/judging_recount/out/"

#eval show IO Unit from do
  let t0 ← IO.monoMsNow
  let tb := mkTabs ()
  IO.println s!"tabs: cosets {tb.ccosRep.size} patterns {tb.epatRep.size} subsets {tb.subNames.size} cases {tb.ncase} names {tb.subNames}"
  let t1 ← IO.monoMsNow
  IO.println s!"mkTabs {t1 - t0} ms"
  let T ← IO.FS.readBinFile "/data/disk/fmc/judging-a-dr/research/data/lean_exact_table.u8"
  let t2 ← IO.monoMsNow
  IO.println s!"table {T.size} bytes, {t2 - t1} ms"
  let h2 := h2Census tb T 2768
  let txt := printCells h2Header (h2Key tb) h2
  IO.FS.writeFile (outDir ++ "h2_lengths.csv") txt
  let t3 ← IO.monoMsNow
  IO.println s!"h2 census + print {t3 - t2} ms; total {h2.foldl (· + ·) 0}"
