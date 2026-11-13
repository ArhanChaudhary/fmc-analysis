import Insertions.Cube
/-
  Insertions.Replay — move sequences on the sticker cube of `Cube.lean`: cancelling, inserting, what a skeleton
  leaves (in the words the pages use), and a replay of a solution block exactly as it is printed.

  Written for this check, not ported from the study's Python or Rust: the cancelling below is the normal form of a
  word in the group where turns of one face add up mod 4 and turns of opposite faces commute (one "syllable" per run
  of turns about one axis), and the leftover text is read off the stickers with "clockwise" defined by a rotation.

    move m     a number 0 … 17: 3 * face + (quarter turns - 1), faces U D R L F B (the order of `cube.NAMES`)
    word       a list of moves, done left to right
    stateOf w  the sticker state after doing w on the solved cube
    normal w   w with all cancelling done; turns about one axis are written first face first (U before D, R before L,
               F before B), which is how the pages write them
-/
namespace Insertions
namespace ins
open cube

def MV : Array State := (MOVES_TABLE.map (·.2)).toArray
def NAMEA : Array String := NAMES.toArray
def face (m : Nat) : Nat := m / 3
def quarters (m : Nat) : Nat := m % 3 + 1
def axis (m : Nat) : Nat := m / 6
def mk (f q : Nat) : Nat := 3 * f + (q - 1)

/-- A move sequence as printed ("R U R' U'") -> a word.  An unknown name gives 18, which `ok` rejects. -/
def word (txt : String) : List Nat := (parse txt).map fun t => NAMES.idxOf t
def ok (w : List Nat) : Bool := w.all (· < 18)
def text (w : List Nat) : String := " ".intercalate (w.map fun m => NAMEA[m]!)

def run (s : State) (w : List Nat) : State := w.foldl (fun s m => apply s MV[m]!) s
def stateOf (w : List Nat) : State := run SOLVED w
/-- The inverse word: reversed, every turn the other way. -/
def inv (w : List Nat) : List Nat := w.reverse.map fun m => mk (face m) (4 - quarters m)

/-- One syllable: an axis and the quarter turns (mod 4) of its first and its second face. -/
abbrev Syl := Nat × Nat × Nat
def push (st : List Syl) (m : Nat) : List Syl :=
  let a := axis m
  let first := face m % 2 == 0
  let fresh : Syl := (a, if first then quarters m else 0, if first then 0 else quarters m)
  match st with
  | (b, p, q) :: rest =>
    if b == a then
      let p' := if first then (p + quarters m) % 4 else p
      let q' := if first then q else (q + quarters m) % 4
      if p' == 0 && q' == 0 then rest else (a, p', q') :: rest
    else fresh :: st
  | [] => [fresh]
def normal (w : List Nat) : List Nat :=
  ((w.foldl push []).reverse).flatMap fun (a, p, q) =>
    (if p == 0 then [] else [mk (2 * a) p]) ++ (if q == 0 then [] else [mk (2 * a + 1) q])
/-- Insert `alg` at spot `i` (after the first i moves) and cancel. -/
def insertAt (s : List Nat) (i : Nat) (alg : List Nat) : List Nat := normal (s.take i ++ alg ++ s.drop i)

/-! ## Pieces, read off the stickers -/

def nz (v : Vec) : Nat := (v.filter (· != 0)).length
/-- The 8 corner places and the 12 edge places, sorted by coordinates (the order the pages list them in). -/
def CORNERS : List Vec := sorted (product3.filter fun p => nz p == 3)
def EDGES : List Vec := sorted (product3.filter fun p => nz p == 2)
/-- The sticker places of a cubie. -/
def facelets (p : Vec) : List Nat := (List.range 54).filter fun i => cube.ST[i]!.1 == p
def CORNER_STICKERS : List Nat := CORNERS.flatMap facelets
def EDGE_STICKERS : List Nat := EDGES.flatMap facelets
/-- Name of a place, faces in the order U D F B R L: `DFL`, `UBR`. -/
def placeName (p : Vec) : String := String.ofList <|
  [('U', 1, (1 : Int)), ('D', 1, -1), ('F', 2, 1), ('B', 2, -1), ('R', 0, 1), ('L', 0, -1)].filterMap
    fun (c, a, sg) => if p[a]! == sg then some c else none
def dot (a b : Vec) : Int := a[0]! * b[0]! + a[1]! * b[1]! + a[2]! * b[2]!
def cross (a b : Vec) : Vec :=
  [a[1]! * b[2]! - a[2]! * b[1]!, a[2]! * b[0]! - a[0]! * b[2]!, a[0]! * b[1]! - a[1]! * b[0]!]
/-- Turn `v` by 120 degrees clockwise, seen from outside, about the corner direction `p` (all entries ±1):
Rodrigues' formula with cos = -1/2, sin = -√3/2 and |p|² = 3, which comes out in whole numbers. -/
def cw (p v : Vec) : Vec :=
  let c := cross p v; let d := dot p v
  (List.range 3).map fun k => (-v[k]! - c[k]! + p[k]! * d) / 2
/-- The sticker place of cubie `p` whose outward normal is `n`. -/
def placeOf (p n : Vec) : Nat := IDX (p, n)
def isUD (i : Nat) : Bool := cube.ST[i]!.2[1]! != 0

/-- For the corner at place `p` in state `s`: (the home place of the piece there, its twist), twist 0 when the
piece's U/D sticker is on the place's U/D facelet, 1 when it is one facelet clockwise from it, 2 otherwise. -/
def cornerAt (s : State) (p : Vec) : Vec × Nat :=
  let ud : Vec := [0, p[1]!, 0]
  let f0 := placeOf p ud; let f1 := placeOf p (cw p ud)
  let homeCubie := cube.ST[s[f0]!]!.1
  (homeCubie, if isUD s[f0]! then 0 else if isUD s[f1]! then 1 else 2)

/-- What a state leaves on the corners, as the pages write it: each cycle of places starting from its first place
in `CORNERS` order, `A → B` = the piece now at A belongs at B (`A ↔ B` for a swap), then the corners twisted in
place.  Empty when the corners are solved. -/
def cornerText (s : State) : String := Id.run do
  let idx (p : Vec) : Nat := CORNERS.idxOf p
  let perm := CORNERS.map fun p => idx (cornerAt s p).1
  let tw := CORNERS.map fun p => (cornerAt s p).2
  let mut seen : List Nat := []
  let mut parts : List String := []
  for i in List.range 8 do
    if seen.contains i || perm[i]! == i then continue
    let mut c := [i]; seen := seen ++ [i]; let mut j := perm[i]!
    for _ in List.range 8 do
      if j == i then break
      c := c ++ [j]; seen := seen ++ [j]; j := perm[j]!
    let names := c.map fun k => placeName CORNERS[k]!
    parts := parts ++ [if c.length == 2 then " ↔ ".intercalate names
                       else " → ".intercalate names ++ " → " ++ names[0]!]
  for i in List.range 8 do
    if perm[i]! == i && tw[i]! != 0 then
      parts := parts ++ [placeName CORNERS[i]! ++
        (if tw[i]! == 1 then " twisted clockwise" else " twisted counter-clockwise")]
  return ", ".intercalate parts

def edgesSolved (s : State) : Bool := EDGE_STICKERS.all fun i => s[i]! == i
def cornersSolved (s : State) : Bool := CORNER_STICKERS.all fun i => s[i]! == i
/-- Number of corner places whose piece is not home or is twisted. -/
def cornersMoved (s : State) : Nat := (CORNERS.filter fun p => (facelets p).any fun i => s[i]! != i).length
def edgesMoved (s : State) : Nat := (EDGES.filter fun p => (facelets p).any fun i => s[i]! != i).length

/-! ## A printed solution block, replayed -/

/-- A skeleton line with marks (`… L' D2 * B D2 …`): the moves, and each mark with the number of moves before it. -/
def marked (line : String) : List Nat × List (String × Nat) := Id.run do
  let mut ms : List Nat := []; let mut mk : List (String × Nat) := []
  for t in parse line do
    if t == "*" || t == "^" then mk := mk ++ [(t, ms.length)] else ms := ms ++ [NAMES.idxOf t]
  return (ms, mk)
/-- `* = U' B D' B' U B D B' // (8-3/25)` -> (mark, alg, printed alg length, printed cancel, printed length after). -/
def stepLine (line : String) : String × List Nat × Nat × Nat × Nat :=
  match line.splitOn " = " with
  | [m, rest] =>
    match rest.splitOn " // (" with
    | [alg, note] =>
      let note := note.replace ")" ""
      match note.splitOn "/" with
      | [ab, after] => match ab.splitOn "-" with
        | [a, b] => (m, word alg, a.toNat!, b.toNat!, after.toNat!)
        | _ => ("?", [], 0, 0, 0)
      | _ => ("?", [], 0, 0, 0)
    | _ => ("?", [], 0, 0, 0)
  | _ => ("?", [], 0, 0, 0)
/-- `Solution: F2 D2 … (25)` -> (moves, printed length). -/
def solutionLine (line : String) : List Nat × Nat :=
  let body := (line.replace "Solution: " "")
  match body.splitOn " (" with
  | [mv, n] => (word mv, (n.replace ")" "").toNat!)
  | _ => ([], 0)

/-- Replay a block as printed.  `lines`: the skeleton line with marks, then the lines that follow it in the page's
code block (a `mark = alg // (a-b/n)` line per comm, possibly a second skeleton line with the second mark, then the
`Solution:` line).  Checks, everything from the printed text:
  - every name is a face turn; nothing cancels in the scramble, the skeleton or a comm as written;
  - the skeleton leaves exactly `left` on the corners and nothing on the edges;
  - every comm has the printed length, is a corner-only alg (edges untouched) and inserted where its mark is gives
    the printed length after it, with the printed cancel = length before + alg length - length after;
  - a second skeleton line is the sequence as it stands after the first comm;
  - with both marks on the first line, the result is that of inserting both there;
  - the Solution line is the result, of the printed length, and the scramble followed by it is solved. -/
def checkBlock (scramble : String) (lines : List String) (left : String) : Bool := Id.run do
  let z := word scramble
  let (s, marks) := marked lines[0]!
  if !(ok z && ok s && (normal z).length == z.length && (normal s).length == s.length) then return false
  let st := stateOf (z ++ s)
  if !(edgesSolved st && cornerText st == left) then return false
  let steps := (lines.filter fun l => (l.splitOn " = ").length == 2).map stepLine
  let sols := lines.filter fun l => l.startsWith "Solution: "
  let second := (lines.drop 1).filter fun l => (marked l).2.length > 0 && !l.startsWith "Solution" && (l.splitOn " = ").length == 1
  let mut cur := s
  let mut prevLen := s.length
  -- first comm
  let some (_, a1, l1, c1, n1) := steps.find? (·.1 == "*") | return false
  let some p1 := marks.lookup "*" | return false
  let algOk (a : List Nat) (l : Nat) : Bool :=
    ok a && a.length == l && (normal a).length == a.length && edgesSolved (stateOf a) && !(cornersSolved (stateOf a))
  if !(algOk a1 l1) then return false
  let s1 := insertAt s p1 a1
  if !(s1.length == n1 && prevLen + l1 == n1 + c1) then return false
  cur := s1; prevLen := n1
  match steps.find? (·.1 == "^") with
  | none => pure ()
  | some (_, a2, l2, c2, n2) =>
    if !(algOk a2 l2) then return false
    let s2 ← match marks.lookup "^" with
      | some q =>                                   -- both marks on the skeleton line
        let (x, ax, y, ay) := if p1 < q then (p1, a1, q, a2) else (q, a2, p1, a1)
        if x == y then return false
        pure (normal (s.take x ++ ax ++ (s.drop x).take (y - x) ++ ay ++ s.drop y))
      | none =>
        match second with
        | [l] =>
          let (m1, mk1) := marked l
          if m1 != s1 then return false
          match mk1.lookup "^" with
          | some q => pure (insertAt s1 q a2)
          | none => return false
        | _ => return false
    if !(s2.length == n2 && prevLen + l2 == n2 + c2) then return false
    -- with both marks on one line the second comm must also be the second step of the printed numbers:
    -- the result after the first comm alone is s1 (checked above) and the result of both is s2.
    cur := s2
  match sols with
  | [l] =>
    let (sol, n) := solutionLine l
    return sol == cur && sol.length == n && stateOf (z ++ sol) == SOLVED
  | _ => return false

end ins
end Insertions
