/-
  AttemptSim.Complete — what the simulated solver can see, enumerated again by brute force on the sticker cube.

  The simulator lists, for a scramble S, every EO candidate up to a length (eo.rs `enumerate`) and every EO-first DR
  up to a length (cmds.rs `key_drs` with line.rs `all_drs`), using its coordinates and pruning tables.  Here the same
  two sets are defined from scratch and enumerated without any table: every sequence is tried, and EO and DR are
  read off the 54 stickers.

  Words.  Moves are numbers 0 … 17 (3 · face + quarter turns − 1, faces U D R L F B).  A *view* renames the moves of
  the cube turned as a whole (data/model.txt; `views_ok`): sequences are generated in the view's names, in *canonical
  order* there (never the same face twice in a row; of two opposite faces in a row, the one that comes first in
  U D R L F B, as the view names them, first), and written down in the cube's own names.

  EO candidates on axis y, at most K turns in all (view: the one that puts y on F/B).  A candidate is (N, I): N on the
  normal side, I on the inverse side.
    normal    I empty; N canonical, `S N` has EO on y, and no shorter start of N does (the empty N if S itself has)
    inverse   N empty; I canonical and not empty, `S⁻¹ I` has EO on y, and no shorter start of I does
    NISS      I canonical, 1 ≤ |I| < K, ending in a quarter turn of a y face, `I⁻¹ S` without EO on y;
              N canonical, |I| + |N| ≤ K, `I⁻¹ S N` has EO on y and no shorter start of N does
    not kept  a candidate in which the last turns about one axis of N or of I (the last turn and the one before it,
              if it is of the opposite face) include a half turn

  DRs from an EO candidate (N, I) on y, on axis x ≠ y, at most L turns in all (view: y on F/B, x on U/D), continued
  on one side: more turns after N (state `I⁻¹ S N`), or more turns after I (the inverse state `N⁻¹ S⁻¹ I`).  The
  continuation C uses the 14 turns that are not quarter turns of a y face; its first turn is not of the face of the
  last turn already on that side; after that it is canonical; the state is a DR on x (with EO on y) after C and after
  no shorter start of C; and the last turns of C about one axis include no half turn.
-/
import AttemptSim.ModelThm
import AttemptSim.Manifest

namespace AttemptSim
namespace complete
open cube pieces cubie

/-! ### Fast tests on sticker states (checked against the definitions of ModelThm.lean in `fast_tests_agree`) -/

/-- Colour axis of each home sticker. -/
def CAXA : Array Nat := (Array.range 54).map cax
/-- Per axis y: the reference sticker place of each edge place, and which home stickers are reference stickers. -/
def REFP : Array (Array Nat) := (Array.range 3).map fun y => (Array.range 12).map (ref y)
def ISREF : Array (Array Bool) := (Array.range 3).map fun y => (Array.range 54).map fun h => (REF y).contains h
/-- Per axis x: the corner sticker places on the x faces; the sticker places of the four x-slice edge places. -/
def COPL : Array (Array Nat) := (Array.range 3).map fun x =>
  ((List.range 54).filter fun i => cornerOf i < 8 && nax i == x).toArray
def SLPL : Array (Array Nat) := (Array.range 3).map fun x =>
  ((List.range 54).filter fun i => edgeOf i < 12 && !((EPL[edgeOf i]!).any fun j => nax j == x)).toArray

def eoFast (y : Nat) (s : State) : Bool := (REFP[y]!).all fun i => (ISREF[y]!)[s[i]!]!
def drFast (x y : Nat) (s : State) : Bool :=
  eoFast y s && ((COPL[x]!).all fun i => CAXA[s[i]!]! == x) && ((SLPL[x]!).all fun i => CAXA[s[i]!]! != x)

/-! ### Sequences -/

def stateOf (seq : List Nat) : State := seq.foldl (fun s m => apply s MV[m]!) SOLVED
/-- The inverse sequence. -/
def inv (seq : List Nat) : List Nat := seq.reverse.map fun m => 3 * (m / 3) + 2 - m % 3
/-- Canonical order (`canon_ok` of ctx.rs); 18 = no turn before. -/
def canonOk (last mv : Nat) : Bool := last == 18 || !(last / 3 == mv / 3 || (last / 6 == mv / 6 && last / 3 > mv / 3))
/-- The last turns about one axis include a half turn. -/
def redundant (q : List Nat) : Bool :=
  match q.reverse with
  | [] => false
  | l :: rest => ((l :: rest).takeWhile fun m => m / 6 == l / 6).any fun m => m % 3 == 1

/-- Every canonical sequence of exactly k turns (view names). -/
def seqs : Nat → Nat → List Nat → List (List Nat) → List (List Nat)
  | 0, _, path, acc => path.reverse :: acc
  | k + 1, last, path, acc =>
    (List.range 18).foldl (fun acc mv => if canonOk last mv then seqs k mv (mv :: path) acc else acc) acc

/-- From state s: every canonical continuation (view names, own turn u[mv]) of at most `left` turns that reaches EO
on y for the first time at its end. -/
def linDfs (y : Nat) (u : Array Nat) : Nat → State → Nat → List Nat → List (List Nat) → List (List Nat)
  | 0, s, _, path, acc => if eoFast y s then path.reverse :: acc else acc
  | left + 1, s, last, path, acc =>
    if eoFast y s then path.reverse :: acc
    else (List.range 18).foldl (fun acc mv =>
      if canonOk last mv then linDfs y u left (apply s MV[u[mv]!]!) mv (mv :: path) acc else acc) acc

/-- The EO candidates of scramble S on axis y with at most K turns: (kind, N, I) in the cube's own move names. -/
def eoCands (S : List Nat) (y K : Nat) : List (Nat × List Nat × List Nat) := Id.run do
  let u := ((MODEL.eoViews.toList.find? fun (yy, _, _) => yy == y).map (·.2.2)).getD #[]
  let own := fun (p : List Nat) => p.map fun mv => u[mv]!
  let mut out : List (Nat × List Nat × List Nat) := []
  for p in linDfs y u K (stateOf S) 18 [] [] do
    out := (0, own p, []) :: out
  for p in linDfs y u K (stateOf (inv S)) 18 [] [] do
    if p != [] then out := (1, [], own p) :: out
  for k in [1:K] do
    for I in seqs k 18 [] [] do
      let l := I.getLast!
      if l % 3 != 1 && l / 6 == 2 then
        let st := stateOf (inv (own I) ++ S)
        if !eoFast y st then
          for n in linDfs y u (K - k) st 18 [] [] do
            out := (2, own n, own I) :: out
  return out.filter fun (_, n, i) => !redundant n && !redundant i

/-- From state s: every continuation with the 14 EO-keeping turns (view names) of at most `left` turns that reaches
DR on x (EO on y) for the first time at its end.  `first`: the next turn is the first of the continuation, and must
only avoid the face of `last`. -/
def drDfs (x y : Nat) (u : Array Nat) : Nat → State → Nat → Bool → List Nat → List (List Nat) → List (List Nat)
  | 0, s, _, _, path, acc => if drFast x y s then path.reverse :: acc else acc
  | left + 1, s, last, first, path, acc =>
    if drFast x y s then path.reverse :: acc
    else MODEL.eoKeep.toList.foldl (fun acc mv =>
      let ok := if first then last == 18 || last / 3 != mv / 3 else canonOk last mv
      if ok then drDfs x y u left (apply s MV[u[mv]!]!) mv false (mv :: path) acc else acc) acc

/-- The EO-first DRs of S with at most L turns, from the EO candidates `eos` = (axis, kind, N, I): (DR axis, N, I). -/
def drCands (S : List Nat) (eos : List (Nat × Nat × List Nat × List Nat)) (L : Nat) : List (Nat × List Nat × List Nat) := Id.run do
  let mut out : List (Nat × List Nat × List Nat) := []
  for (y, _, n, i) in eos do
    let len := n.length + i.length
    if len > L then continue
    for x in [0:3] do
      if x == y then continue
      let u := ((MODEL.drViews.toList.find? fun (yy, xx, _, _) => yy == y && xx == x).map (·.2.2.2)).getD #[]
      let own := fun (p : List Nat) => p.map fun mv => u[mv]!
      let lastV := fun (q : List Nat) => match q.getLast? with
        | some o => u.toList.idxOf o
        | none => 18
      for p in drDfs x y u (L - len) (stateOf (inv i ++ S ++ n)) (lastV n) true [] [] do
        if !redundant p then out := (x, n ++ own p, i) :: out
      for p in drDfs x y u (L - len) (stateOf (inv n ++ inv S ++ i)) (lastV i) true [] [] do
        if !redundant p then out := (x, n, i ++ own p) :: out
  return out

/-! ### The simulator's lists (data/cands_*.tsv) -/

def parseSeq (txt : String) : List Nat := (cube.parse txt).map (NAMES.idxOf ·)

/-- (scramble number, scramble) -/
def SCRAMBLES : List (Nat × List Nat) :=
  ((lines (include_str "../data/cands_scrambles.tsv")).drop 1).map fun l =>
    let p := l.splitOn "\t"
    ((nats (p.getD 0 "")).getD 0 0, parseSeq (p.getD 1 ""))
/-- (scramble number, axis, kind, stated length, N, I) -/
def FILE_EO : List (Nat × Nat × Nat × Nat × List Nat × List Nat) :=
  ((lines (include_str "../data/cands_eo.tsv")).drop 1).map fun l =>
    let p := l.splitOn "\t"
    let n := fun k => (nats (p.getD k "")).getD 0 99
    (n 0, n 1, n 2, n 3, parseSeq (p.getD 4 ""), parseSeq (p.getD 5 ""))
/-- (scramble number, DR axis, stated length, N, I) -/
def FILE_DR : List (Nat × Nat × Nat × List Nat × List Nat) :=
  ((lines (include_str "../data/cands_dr.tsv")).drop 1).map fun l =>
    let p := l.splitOn "\t"
    let n := fun k => (nats (p.getD k "")).getD 0 99
    (n 0, n 1, n 2, parseSeq (p.getD 3 ""), parseSeq (p.getD 4 ""))

/-- One row as a list of numbers, for sorting and comparing. -/
def code (a b : Nat) (n i : List Nat) : List Nat := [a, b] ++ n ++ [99] ++ i
def sortRows (l : List (List Nat)) : List (List Nat) := l.mergeSort fun p q => decide (p ≤ q)

def eoBrute (S : List Nat) (K : Nat) : List (List Nat) :=
  sortRows ((List.range 3).flatMap fun y => (eoCands S y K).map fun (k, n, i) => code y k n i)
def eoFile (id : Nat) : List (List Nat) :=
  sortRows ((FILE_EO.filter (·.1 == id)).map fun (_, y, k, _, n, i) => code y k n i)

def drBrute (S : List Nat) (K L : Nat) : List (List Nat) :=
  let eos := (List.range 3).flatMap fun y => (eoCands S y K).map fun (k, n, i) => (y, k, n, i)
  sortRows ((drCands S eos L).map fun (x, n, i) => code x 0 n i).eraseDups
def drFile (id : Nat) : List (List Nat) :=
  sortRows ((FILE_DR.filter (·.1 == id)).map fun (_, x, _, n, i) => code x 0 n i).eraseDups

end complete
end AttemptSim
