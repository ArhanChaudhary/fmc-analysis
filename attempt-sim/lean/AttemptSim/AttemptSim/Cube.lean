/-
  AttemptSim.Cube — copied unchanged, but for the namespace and this line, from the EO-switch study's certificate
  (eo-switch/lean/EOSwitch/EOSwitch/Cube.lean), which has it from eo-to-dr's, which has it from is-dr-xs-worth-it's
  (lean/DRXs/DRXs/Cube.lean, itself research/src/cube.py of that study in Lean): a whole Rubik's cube at the
  sticker level, centers included, built from geometry so that no permutation is typed by hand.

    axes      x = R (+) / L (-),  y = U (+) / D (-),  z = F (+) / B (-)
    sticker   (cubie position, outward normal), 54 of them; index order: faces U D R L F B, each face row by row
    state     s[i] = the home index of the sticker now sitting at place i
    moves     the 18 face turns  U U2 U' D D2 D' R R2 R' L L2 L' F F2 F' B B2 B'
    apply     t = s after move m:  t[m[i]] = s[i]     (the sticker at place i is carried to place m[i])

  Clockwise seen from outside the face = a rotation by -90 degrees about the outward normal.

  Python -> Lean, for readers of cube.py:
    tuple of three ints          `Vec`  = `List Int`          `p[a]!` is Python's `p[a]`
    tuple of 54 ints             `State` = `Array Nat`
    dict MOVES[name]             `MOVES name`, a look-up in the list `MOVES_TABLE` of (name, permutation) pairs
    `for … in …`                 the same, inside `Id.run do`, with `let mut` for variables that are assigned again
    names starting with `_`      the same name without the underscore (`_rot` is `rot`)
    `do`                         `do_` (`do` is a Lean keyword); a move sequence is a string with spaces: "R U R' U'"
  Left out: the slice turns, wide turns and rotations of cube.py (nothing here uses them), `compose`, `inverse`.
-/

namespace AttemptSim
namespace cube

/-- A position or a direction: `[x, y, z]`. -/
abbrev Vec := List Int
/-- A sticker: (cubie position, outward normal). -/
abbrev Sticker := Vec × Vec
/-- A state, or a move: 54 numbers. -/
abbrev State := Array Nat

/-- face -> (axis, sign) -/
def AX (f : Char) : Nat × Int :=
  if f == 'U' then (1, 1) else if f == 'D' then (1, -1) else if f == 'R' then (0, 1)
  else if f == 'L' then (0, -1) else if f == 'F' then (2, 1) else (2, -1)        -- else: 'B'

def FACES : List Char := ['U', 'D', 'R', 'L', 'F', 'B']

/-- `itertools.product((-1, 0, 1), repeat=3)`: the 27 cubie positions. -/
def product3 : List Vec := Id.run do
  let mut out : List Vec := []
  for x in [-1, 0, 1] do
    for y in [-1, 0, 1] do
      for z in [-1, 0, 1] do
        out := out ++ [[x, y, z]]
  return out

/-- Python's `sorted` on a list of tuples (tuples compare entry by entry, like Lean lists). -/
def sorted (l : List Vec) : List Vec := l.mergeSort (fun p q => decide (p ≤ q))

def stickers : Array Sticker := Id.run do
  let mut out : Array Sticker := #[]
  for f in FACES do
    let (a, sg) := AX f
    let mut cells : List Vec := []
    for p in product3 do
      if p[a]! == sg then cells := cells ++ [p]
    for p in sorted cells do
      let n := ([0, 0, 0] : Vec).set a sg
      out := out.push (p, n)
  return out

def ST : Array Sticker := stickers

/-- `IDX[s]`: the index of sticker `s` in `ST` (54 if it is not there). -/
def IDX (s : Sticker) : Nat := ST.toList.idxOf s

/-- `max(range(3), key=lambda k: abs(n[k]))`: the first axis along which `n` is longest. -/
def argmax_abs (n : Vec) : Nat := Id.run do
  let mut best := 0
  for k in [1, 2] do
    if n[k]!.natAbs > n[best]!.natAbs then best := k
  return best

/-- The face each sticker is on (so also: the colour of the sticker whose home this is). -/
def FACE_OF : Array Char :=
  ST.map fun (_, n) => (FACES.find? fun f => AX f == (argmax_abs n, n[argmax_abs n]!)).get!

/-- Rotate vector v about axis a by quarter * (-90 degrees) (i.e. quarter = 1 is clockwise seen from +a). -/
def rot (v : Vec) (a : Nat) (quarter : Int) : Vec := Id.run do
  let (b, c) := [(1, 2), (2, 0), (0, 1)][a]!
  let mut v := v
  for _ in [0 : (quarter % 4).toNat] do            -- Lean's % on integers is Python's: (-1) % 4 = 3
    let vb := v[b]!; let vc := v[c]!
    v := (v.set b vc).set c (-vb)
  return v

def layer_move (a : Nat) (layers : List Int) (quarter : Int) : State := Id.run do
  let mut m := Array.range 54
  for i in [0:54] do
    let (p, n) := ST[i]!
    if layers.contains p[a]! then
      m := m.set! i (IDX (rot p a quarter, rot n a quarter))
  return m

/-- The 18 face turns, as (name, permutation) pairs. -/
def build : List (String × State) := Id.run do
  let mut M : List (String × State) := []
  for f in FACES do
    let (a, sg) := AX f
    -- add(f, a, (sg,), sg): clockwise seen from outside
    for (k, suf) in [((1 : Int), ""), (2, "2"), (3, "'")] do
      M := M ++ [(f.toString ++ suf, layer_move a [sg] ((sg * k) % 4))]
  return M

def MOVES_TABLE : List (String × State) := build
/-- The names of the 18 face turns. -/
def NAMES : List String := MOVES_TABLE.map (·.1)
/-- `MOVES[name]`.  (An unknown name gives the empty array, on which nothing below works.) -/
def MOVES (name : String) : State := (MOVES_TABLE.lookup name).getD #[]

def SOLVED : State := Array.range 54

def apply (s : State) (m : State) : State := Id.run do
  let mut t := Array.replicate 54 0
  for i in [0:54] do t := t.set! m[i]! s[i]!
  return t

/-- A move sequence as text -> the list of move names.  (Names must be separated by spaces.) -/
def parse (txt : String) : List String := (txt.splitOn " ").filter (· != "")

/-- cube.py's `do`: apply the moves of `seq`, left to right. -/
def do_ (s : State) (seq : String) : State := Id.run do
  let mut s := s
  for t in parse seq do s := apply s (MOVES t)
  return s

/-- How many times `seq` must be done, starting from the solved cube, to see the solved cube again
(the loop of cube.py's self-test; 0 if 2000 times are not enough). -/
def order (seq : String) : Nat := Id.run do
  let mut s := SOLVED
  for k in [1:2001] do
    s := do_ s seq
    if s == SOLVED then return k
  return 0

/-- `m` is a permutation of the 54 places: 54 entries, and every place 0 … 53 occurs among them. -/
def is_permutation (m : State) : Bool := m.size == 54 && (List.range 54).all fun j => m.contains j

end cube
end AttemptSim
