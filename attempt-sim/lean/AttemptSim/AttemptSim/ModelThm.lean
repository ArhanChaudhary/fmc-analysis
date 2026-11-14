/-
  AttemptSim.ModelThm — checked statements, part A: the simulator's cube model is the cube.
  Each is a closed statement about `Cube.lean` (stickers, from geometry), `Cubie.lean` (the simulator's tables, read
  from data/model.txt) and `Perm.lean`, proved by running it (`native_decide`: compiled code, see README.md).
-/
import AttemptSim.Cubie
import AttemptSim.Perm

namespace AttemptSim
open cube pieces cubie

set_option maxHeartbeats 0

/-- 54 stickers, all different; the 18 face turns have the usual names and are permutations of the 54 places. -/
theorem sticker_model :
    cube.ST.size = 54 ∧ cube.ST.toList.eraseDups.length = 54 ∧
    NAMES = ["U", "U2", "U'", "D", "D2", "D'", "R", "R2", "R'", "L", "L2", "L'", "F", "F2", "F'", "B", "B2", "B'"] ∧
    (∀ name ∈ NAMES, is_permutation (MOVES name) = true) := by
  native_decide

/-- The turns are the usual ones: U carries the U sticker of UFR to UFL, R carries it to UBR facing B, F carries it
to DFR facing R; each face has order 4; X2 is X twice and X' is X three times; R U R' U' has order 6 and
R U2 D' B D' has order 1260. -/
theorem turn_directions :
    (let i := IDX ([1, 1, 1], [0, 1, 0])
     (MOVES "U")[i]! = IDX ([-1, 1, 1], [0, 1, 0]) ∧ (MOVES "R")[i]! = IDX ([1, 1, -1], [0, 0, -1]) ∧
     (MOVES "F")[i]! = IDX ([1, -1, 1], [1, 0, 0])) ∧
    (∀ f ∈ ["U", "D", "R", "L", "F", "B"], order f = 4 ∧
      do_ SOLVED (f ++ " " ++ f) = do_ SOLVED (f ++ "2") ∧ do_ SOLVED (f ++ " " ++ f ++ " " ++ f) = do_ SOLVED (f ++ "'")) ∧
    order "R U R' U'" = 6 ∧ order "R U2 D' B D'" = 1260 := by
  native_decide

/-- data/model.txt has the shape the simulator reads: 18 move tables, 24 rotations, 3 EO views and 6 DR views, each
table with 8 + 8 + 12 + 12 entries in range, each view a renaming of the 18 moves. -/
theorem model_shape :
    MODEL.moves.size = 18 ∧ MODEL.rots.size = 24 ∧ MODEL.rotAxes.size = 24 ∧ MODEL.rotFaces.size = 24 ∧
    MODEL.eoViews.size = 3 ∧ MODEL.drViews.size = 6 ∧
    ((MODEL.moves ++ MODEL.rots).all fun mp =>
      mp.cd.size == 8 && mp.ca.size == 8 && mp.ed.size == 12 && mp.ea.size == 12 &&
      mp.cd.all (· < 8) && mp.ca.all (· < 3) && mp.ed.all (· < 12) && mp.ea.all (· < 2)) ∧
    (MODEL.eoViews.all fun (_, _, u) => (List.range 18).all fun k => u.contains k) ∧
    (MODEL.drViews.all fun (_, _, _, u) => (List.range 18).all fun k => u.contains k) ∧
    MODEL.drC.size = 8 ∧ MODEL.drE.size = 8 ∧ MODEL.drS.size = 4 ∧ MODEL.drMoves.size = 10 ∧ MODEL.eoKeep.size = 14 := by
  native_decide

/-- **The simulator's 18 move tables are the sticker cube's turns.**  For every face turn, the table in
data/model.txt (where each corner and edge place goes, and the twist / flip it adds) is the one read off the
54-sticker permutation of that turn, and that permutation carries each corner's stickers onto the destination's
cyclically (so "adds a twist" is exact). -/
theorem moves_match :
    ((List.range 18).all fun mv => asMap MV[mv]! == MODEL.moves[mv]! && mapSound MV[mv]!) = true := by
  native_decide

/-- The piece description follows the stickers: the solved cube is the solved cube, and on every sticker state
reached with at most 3 face turns (6,175 sequences), for each of the 18 turns, reading the pieces off the turned
stickers gives what the simulator's `turn` computes from the pieces before the turn. -/
theorem cubie_follows_stickers :
    (toCubie SOLVED == SOLVEDC &&
     (near 3).all fun s => (List.range 18).all fun mv =>
       toCubie (apply s MV[mv]!) == turn MODEL.moves[mv]! (toCubie s)) = true := by
  native_decide

/-- `then` and `inverse` of the simulator (used for NISS: the state `I⁻¹ S N`, and the look at the inverse) are
composition and inverse of sticker states: checked on every pair of states within 2 turns of solved (343 × 343)
and on every state within 3 turns. -/
theorem then_inverse_follow :
    (((near 2).all fun s => (near 2).all fun t => toCubie (composeS s t) == thenC (toCubie s) (toCubie t)) &&
     ((near 3).all fun s => toCubie (inverseS s) == inverseC (toCubie s) &&
        composeS s (inverseS s) == SOLVED)) = true := by
  native_decide

/-- Composition of sticker states is doing one sequence after the other: for all sequences A, B of at most 2 turns,
the state after A ++ B is `composeS` of the states after A and after B. -/
theorem compose_is_concatenation :
    ((List.range 3).all fun a => (List.range 3).all fun b =>
      perm.allSeq (fun A => perm.allSeq (fun B =>
        let run := fun (L : List perm.Mv) => L.foldl (fun s m => apply s MV[m.val]!) SOLVED
        run (A ++ B) == composeS (run A) (run B)) b []) a []) = true := by
  native_decide

/-- The two descriptions of "this sequence does nothing" agree: following every sticker (`perm.run`, the one the
general theorems are about) and applying the turns to the 54-sticker state (`cube.apply`), on every sequence of at
most 4 turns; and `perm.mvF` is the table of `Cube.lean` entry for entry. -/
theorem run_is_apply :
    (((List.range 18).all fun m => (List.range 54).all fun p =>
        if h : m < 18 then if h2 : p < 54 then (perm.mvF ⟨m, h⟩ ⟨p, h2⟩).val == (MV[m]!)[p]! else false else false) &&
     ((List.range 5).all fun k => perm.allSeq (fun L =>
        perm.solvedB L == (L.foldl (fun s m => apply s MV[m.val]!) SOLVED == SOLVED)) k [])) = true := by
  native_decide

/-- **The 24 rotations of the simulator are the 24 rotations of the cube.**  Each row of the rotation table is the
`Map` of exactly one whole-cube rotation built from geometry, with the axes and faces going where the row says;
the 24 are different; row 0 is the identity. -/
theorem rotations_match :
    (ROTS.length == 24 && rotOf 0 == SOLVED &&
     ((List.range 24).map rotOf).eraseDups.length == 24 &&
     (List.range 24).all fun r =>
       let R := rotOf r
       R.size == 54 && is_permutation R && mapSound R &&
       axesOf R == MODEL.rotAxes[r]! && facesOf R == MODEL.rotFaces[r]!) = true := by
  native_decide

/-- `conj` of the simulator is looking at the cube after turning it as a whole: on every state within 2 turns of
solved and each of the 24 rotations. -/
theorem conj_follows :
    ((near 2).all fun s => (List.range 24).all fun r =>
      toCubie (conjS s (rotOf r)) == conjC MODEL.rots[r]! (toCubie s)) = true := by
  native_decide

/-- A view renames moves correctly: turning the cube by the *own* move u[mv] and then looking at it through the
view's rotation R is looking first and then turning the *view* move mv (R ∘ own = view ∘ R on all 54 places). -/
def renameOk (r : Nat) (u : Array Nat) : Bool :=
  let R := rotOf r
  (List.range 18).all fun mv => (List.range 54).all fun i => R[(MV[u[mv]!]!)[i]!]! == (MV[mv]!)[R[i]!]!

/-- **The nine views.**  The view for EO on axis y carries axis y to F/B; the view for (EO on y, DR on x) carries y
to F/B and x to U/D; all nine rename the moves correctly; the three EO views cover the three axes and the six DR
views the six ordered pairs of different axes. -/
theorem views_ok :
    ((MODEL.eoViews.all fun (y, r, u) => MODEL.rotAxes[r]![y]! == 2 && renameOk r u) &&
     (MODEL.drViews.all fun (y, x, r, u) => MODEL.rotAxes[r]![y]! == 2 && MODEL.rotAxes[r]![x]! == 1 && renameOk r u) &&
     MODEL.eoViews.toList.map (·.1) == [0, 1, 2] &&
     (MODEL.drViews.toList.map fun (y, x, _, _) => (y, x)) == [(1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2)]) = true := by
  native_decide

/-- EO on axis Y read from the stickers (`pieces.badMask`, the definition of the EO-to-DR and EO-switch
certificates: an edge is good when its reference sticker sits on the reference sticker of its place). -/
def eoOn (Y : Nat) (s : State) : Bool := badMask Y s == 0

/-- Corners oriented for axis X: the sticker on the X face of every corner place has an X colour. -/
def coOn (X : Nat) (s : State) : Bool :=
  (List.range 8).all fun c => (CPL[c]!).all fun i => nax i != X || cax s[i]! == X
/-- The X slice: the four edge places with no sticker on an X face hold the four pieces with no X colour. -/
def sliceOn (X : Nat) (s : State) : Bool :=
  (List.range 12).all fun k => (EPL[k]!).any (fun i => nax i == X) || (EPL[k]!).all fun i => cax s[i]! != X
/-- DR on axis X with EO on axis Y, from the stickers. -/
def drOn (X Y : Nat) (s : State) : Bool := eoOn Y s && coOn X s && sliceOn X s

/-- **What the views read is the real thing.**  On every state within 3 turns of solved: the simulator's EO test in
the view of axis y (no flip in the turned cube) is EO on axis y of the cube itself, read from the stickers; and its
DR test in the view of (y, x) (EO coordinate 0, twist coordinate 0, E-slice pieces home) is DR on x with EO on y. -/
theorem views_read_axes :
    ((near 3).all fun s =>
      let c := toCubie s
      (MODEL.eoViews.all fun (y, r, _) => (eoOf (conjC MODEL.rots[r]! c) == 0 && (conjC MODEL.rots[r]! c).ef[11]! == 0) == eoOn y s) &&
      (MODEL.drViews.all fun (y, x, r, _) =>
        let v := conjC MODEL.rots[r]! c
        (v.ef.all (· == 0) && v.ct.all (· == 0) && slOf v == MODEL.solvedSl) == drOn x y s)) = true := by
  native_decide

/-- The numbering of the DR tables and the move lists: drmap sends judging-a-dr's corner positions UFR UFL UBL UBR
DFR DFL DBL DBR, U/D-layer edge positions UF UL UB UR DF DL DB DR and E-slice positions FR FL BL BR to the places
with those names; the DR moves are U U2 U' D D2 D' R2 L2 F2 B2; the EO-keeping moves are exactly the 14 turns whose
table flips no edge (all but the F and B quarter turns); `solved_sl` is the slice coordinate of the solved cube. -/
theorem dr_numbering :
    (MODEL.drC.toList == ([[1,1,1],[-1,1,1],[-1,1,-1],[1,1,-1],[1,-1,1],[-1,-1,1],[-1,-1,-1],[1,-1,-1]] : List Vec).map (CORNERS.idxOf ·) &&
     MODEL.drE.toList == ([[0,1,1],[-1,1,0],[0,1,-1],[1,1,0],[0,-1,1],[-1,-1,0],[0,-1,-1],[1,-1,0]] : List Vec).map (EDGES.idxOf ·) &&
     MODEL.drS.toList == ([[1,0,1],[-1,0,1],[-1,0,-1],[1,0,-1]] : List Vec).map (EDGES.idxOf ·) &&
     MODEL.drMoves.toList == ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"].map (NAMES.idxOf ·) &&
     MODEL.eoKeep.toList == (List.range 18).filter (fun mv => MODEL.moves[mv]!.ea.all (· == 0)) &&
     MODEL.eoKeep.toList == (List.range 18).filter (fun mv => !(mv / 6 == 2 && mv % 3 != 1)) &&
     MODEL.solvedSl == slOf SOLVEDC) = true := by
  native_decide

/-- `cancel` (the HTM form) on every sequence of at most 5 turns (2,000,719 sequences): the result has no two
turns of one face next to each other or separated only by a turn of the opposite face, cancelling again changes
nothing, it is never longer, and a sequence that is already in that form is left as it is.  (That `cancel` never
changes what a sequence does is `perm.cancel_run`, for every sequence.) -/
theorem cancel_shape : perm.cancelShapeB 5 = true := by native_decide

end AttemptSim
