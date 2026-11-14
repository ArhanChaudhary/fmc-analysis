/-
  AttemptSim.DRLink — checked statements, part F: the simulator's DR moves are judging-a-dr's.

  judging-a-dr's certificate (DRBound) describes the cube after DR as plain data: the piece at each of 8 corner
  positions, 8 U/D-layer edge positions and 4 E-slice positions, and the ten DR moves U U2 U' D D2 D' R2 L2 F2 B2 as
  explicit tables (`DRBound.Move.srcC/srcE/srcS`: after the move, position p holds what was at position src[p]).  Its
  theorems about exact optimal finishes are about that model, and the exact table the simulator reads
  (lean_exact_table.u8, sha256 in `manifest.EXACT_SHA256`) was written from it.  The two DRBound files are copied here
  unchanged (DRBound/Cube.lean, DRBound/Certificate.lean; gen.py checks they are byte-identical to judging-a-dr's and
  records their sha256 in `manifest.VENDORED`).

  The statements below tie the simulator's own move tables (data/model.txt, proved to be the sticker cube's turns in
  ModelThm) and the sticker cube's DR moves (Tables.lean, `CT`, `ET`) to those ten tables, through the place numbering
  `drmap` (ModelThm `dr_numbering`: the places named UFR … DBR, UF … DR, FR … BR).
-/
import AttemptSim.Cubie
import AttemptSim.Tables
import DRBound.Cube

namespace AttemptSim
namespace drlink
open cubie

/-- DRBound's tables as lists of numbers. -/
def srcCn (m : DRBound.Move) : List Nat := (DRBound.Move.srcC m).toList.map (·.val)
def srcEn (m : DRBound.Move) : List Nat := (DRBound.Move.srcE m).toList.map (·.val)
def srcSn (m : DRBound.Move) : List Nat := (DRBound.Move.srcS m).toList.map (·.val)

/-- The simulator's table for DR move m (the move `drmoves[m]` of data/model.txt). -/
def simMap (m : DRBound.Move) : Map := MODEL.moves[MODEL.drMoves[m.idx]!]!

/-- Move m of the simulator, read through drmap, is DRBound's move m: for each position p, the piece at the place of
position src[p] goes to the place of position p, and its twist (flip) does not change. -/
def tableOk (m : DRBound.Move) : Bool :=
  let mp := simMap m
  (List.range 8).all (fun p =>
    let i := MODEL.drC[(srcCn m)[p]!]!
    mp.cd[i]! == MODEL.drC[p]! && mp.ca[i]! == 0) &&
  (List.range 8).all (fun p =>
    let i := MODEL.drE[(srcEn m)[p]!]!
    mp.ed[i]! == MODEL.drE[p]! && mp.ea[i]! == 0) &&
  (List.range 4).all (fun p =>
    let i := MODEL.drS[(srcSn m)[p]!]!
    mp.ed[i]! == MODEL.drS[p]! && mp.ea[i]! == 0)

/-- **The simulator's ten DR moves are DRBound's ten move tables**, entry by entry, and none of them twists a corner
or flips an edge. -/
theorem dr_moves_are_drbound : DRBound.Move.all.all tableOk = true := by native_decide

/-- A cube of the simulator read as a DRBound state: at each position, the position whose home piece sits there. -/
def readDR (c : Cubie) : List Nat × List Nat × List Nat :=
  ((List.range 8).map fun p => MODEL.drC.toList.idxOf c.cp[MODEL.drC[p]!]!,
   (List.range 8).map fun p => MODEL.drE.toList.idxOf c.ep[MODEL.drE[p]!]!,
   (List.range 4).map fun p => MODEL.drS.toList.idxOf c.ep[MODEL.drS[p]!]!)

def ofState (g : DRBound.State) : List Nat × List Nat × List Nat :=
  (g.c.toList.map (·.val), g.e.toList.map (·.val), g.s.toList.map (·.val))

/-- Every sequence of exactly k DR moves. -/
def seqsK : Nat → List (List DRBound.Move)
  | 0 => [[]]
  | k + 1 => (seqsK k).flatMap fun w => DRBound.Move.all.map fun m => w ++ [m]

/-- **Sequences follow.**  For every sequence w of at most 4 DR moves (11,111 sequences): the simulator's cube after
w, from solved, read through drmap, is DRBound's `solved.apply w`, with every corner twist and edge flip 0. -/
theorem dr_sequences_follow_drbound :
    ((List.range 5).all fun k => (seqsK k).all fun w =>
      let c := applyC SOLVEDC (w.map fun m => MODEL.drMoves[m.idx]!)
      readDR c == ofState (DRBound.solved.apply w) && c.ct.all (· == 0) && c.ef.all (· == 0)) = true := by
  native_decide

/-- The four E-slice positions FR FL BL BR (DRBound's order). -/
def SPOS : Array cube.Vec := #[[1,0,1],[-1,0,1],[-1,0,-1],[1,0,-1]]

/-- **The sticker cube's DR moves are DRBound's too.**  `tables.CT`, `tables.ET` (and the same construction for the
E-slice positions) are built from the 54-sticker turns of Cube.lean: position p goes to position t[p].  DRBound's
tables are their inverses: src[t[p]] = p for every move and position. -/
theorem sticker_dr_moves_are_drbound :
    (DRBound.Move.all.all fun m =>
      (List.range 8).all (fun p => (srcCn m)[(tables.CT[m.idx]!)[p]!]! == p) &&
      (List.range 8).all (fun p => (srcEn m)[(tables.ET[m.idx]!)[p]!]! == p) &&
      (List.range 4).all (fun p => (srcSn m)[(tables.posMap SPOS (tables.DRNAMES[m.idx]!))[p]!]! == p)) = true := by
  native_decide

end drlink
end AttemptSim
