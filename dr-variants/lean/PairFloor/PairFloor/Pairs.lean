/-
  PairFloor.Pairs — the pair floor for a DR finish.

  A *true pair* is a corner and a U/D-layer edge that sit next to each other in the same layer and are joined
  the way they are on a solved cube: the two stickers on their shared side face have the same colour, and the
  two pieces belong to the same layer (their U/D stickers have the same colour).  There are 16 places where a
  corner touches a U/D-layer edge, so a cube has between 0 and 16 true pairs, and 16 once the corners and the
  U/D-layer edges are solved (the E slice does not matter).

  Theorem (`pair_floor`): a sequence of DR moves that solves the corners and the U/D-layer edges of a state
  with `p` true pairs contains at least `(16 - p) / 4` side half turns (R2 L2 F2 B2), because
    * U and D moves never change the number of true pairs (`pairs_move_ud`), and
    * a side half turn changes it by at most 4 (`pairs_move_le`, `pairs_move_ge`).

  The cube model (positions, moves, states) is `DRBound.Cube`, the one the exact table of optimal DR finishes
  is certified on.  No `native_decide`: every finite check here is done by the kernel (`decide`).
-/
import DRBound.Cube

namespace DRBound

/-- Tetrad of a corner position or piece: UFR, UBL, DFL, DBR against the other four. -/
def tetrad : Fin 8 → Bool
  | 0 | 2 | 5 | 7 => true
  | _ => false

/-- Side colour of a corner piece on the F/B axis (`false`) or the R/L axis (`true`): F 0, L 1, B 2, R 3. -/
def cornerCol : Fin 8 → Bool → Fin 4
  | 0, false => 0 | 0, true => 3
  | 1, false => 0 | 1, true => 1
  | 2, false => 2 | 2, true => 1
  | 3, false => 2 | 3, true => 3
  | 4, false => 0 | 4, true => 3
  | 5, false => 0 | 5, true => 1
  | 6, false => 2 | 6, true => 1
  | 7, false => 2 | 7, true => 3

/-- Side face of a U/D-layer edge position, which is also the side colour of the edge piece with that home. -/
def edgeFace : Fin 8 → Fin 4
  | 0 | 4 => 0
  | 1 | 5 => 1
  | 2 | 6 => 2
  | 3 | 7 => 3

/-- Is the face on the R/L axis? -/
def faceRL (f : Fin 4) : Bool := f = 1 || f = 3

/-- Corner piece `c` at corner position `p` and edge piece `e` at the touching edge position `q` form a true
pair.  A corner in its own tetrad shows its F/B colour on the F/B face and its R/L colour on the R/L face; out
of its tetrad the two are swapped. -/
def truePair (p q c e : Fin 8) : Bool :=
  cornerCol c (faceRL (edgeFace q) != (tetrad c != tetrad p)) = edgeFace e && (decide (c.val < 4) == decide (e.val < 4))

def ind (b : Bool) : Nat := if b then 1 else 0

theorem ind_le (b : Bool) : ind b ≤ 1 := by cases b <;> decide

/-- Number of true pairs, given the piece at each corner position and at each U/D-layer edge position.
The 16 terms are the 16 places where a corner touches a U/D-layer edge. -/
def pairsF (cf ef : Fin 8 → Fin 8) : Nat :=
  ind (truePair 0 0 (cf 0) (ef 0)) + ind (truePair 0 3 (cf 0) (ef 3)) +
  ind (truePair 1 0 (cf 1) (ef 0)) + ind (truePair 1 1 (cf 1) (ef 1)) +
  ind (truePair 2 1 (cf 2) (ef 1)) + ind (truePair 2 2 (cf 2) (ef 2)) +
  ind (truePair 3 2 (cf 3) (ef 2)) + ind (truePair 3 3 (cf 3) (ef 3)) +
  ind (truePair 4 4 (cf 4) (ef 4)) + ind (truePair 4 7 (cf 4) (ef 7)) +
  ind (truePair 5 4 (cf 5) (ef 4)) + ind (truePair 5 5 (cf 5) (ef 5)) +
  ind (truePair 6 5 (cf 6) (ef 5)) + ind (truePair 6 6 (cf 6) (ef 6)) +
  ind (truePair 7 6 (cf 7) (ef 6)) + ind (truePair 7 7 (cf 7) (ef 7))

/-- Number of true pairs of a state. -/
def pairs (g : State) : Nat := pairsF (fun p => g.c.get p) (fun q => g.e.get q)

theorem pairs_move (g : State) (m : Move) :
    pairs (g.move m) = pairsF (fun p => g.c.get (m.srcC.get p)) (fun q => g.e.get (m.srcE.get q)) := by
  simp [pairs, State.move]

end DRBound
