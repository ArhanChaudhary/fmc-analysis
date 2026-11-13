/-
  DRBound.Census.Features — what a solver reads off a DR by hand, as tables over the piece model of
  `DRBound.Cube` (a port of `research/drtools/src/class.rs` and of the small tables of `hand.rs`).

  Everything is computed from the ten move tables of `DRBound.Cube` and the 16 symmetries of
  `DRBound.Exact`; nothing is typed in.  `DRBound.Census.SmallTables` compares the tables with the
  committed files `research/out/hand/cosets.csv` and `corner_perm_cases.csv`, character for character.

  Words (as in the write-up).
    HTR corners     the 96 corner arrangements reached from solved by half turns (`hCorners`)
    corner coset    a corner arrangement up to renaming its pieces by an HTR corner arrangement (420);
                    numbered by their smallest rank
    edge pattern    which of the eight U/D-layer positions hold M-slice edges (pieces UF UB DF DB) (70);
                    numbered in order of first appearance by rank
    HTR coset       (corner coset, edge pattern): 29,400; number `a * 70 + b`
    hN              fewest DR moves that bring the HTR coset to the coset of the solved cube (`htr`)
    bad corner      a corner in a position of the other tetrad; bad edge: an M-slice edge in an S position
                    (UL UR DL DR) or the reverse
    qt (corners)    fewest quarter turns of a DR sequence that brings the corners into the HTR corners or
                    into U D' times the HTR corners, half turns free (`ccQt`)
    qt (coset)      fewest quarter turns of a DR sequence that brings the HTR coset to the solved coset
                    (`qtFull`)
    subset          Mallard's 48 subsets, named "<bad corners><letter><qt> <bad edges>e" (`subName`)
    corner case     a corner coset up to the 16 symmetries and up to renaming by U D' (46) (`ccase`)
    L, Lp           optimal corner solution; the same among the corner solutions whose number of side
                    half turns has a given parity (`clen`, `lpar`)
    setup           fewest half turns before some quarter turn lowers the coset's quarter-turn count
    pairs           corner/edge pairs inside the U and D layers by the colours of the touching side
                    stickers: true, pseudo, side semi, top semi (`pairKind`)
-/
import DRBound.Exact

set_option compiler.extract_closed false

namespace DRBound
namespace Census
open Exact

/-! ### Searches on small graphs -/

/-- "Not reached". -/
def unset : Nat := 255

/-- Breadth-first distances on the nodes `0 … n-1` from the nodes `src`, along `nbr`. -/
def bfs (n : Nat) (src : List Nat) (nbr : Nat → List Nat) : Array Nat := Id.run do
  let mut dist := Array.replicate n unset
  let mut queue : Array Nat := Array.emptyWithCapacity n
  for s in src do
    if dist[s]! == unset then
      dist := dist.set! s 0
      queue := queue.push s
  let mut head := 0
  -- every node enters the queue at most once
  for _ in [0:n] do
    if head < queue.size then
      let x := queue[head]!
      head := head + 1
      let d := dist[x]! + 1
      for y in nbr x do
        if dist[y]! == unset then
          dist := dist.set! y d
          queue := queue.push y
    else break
  return dist

/-- Fewest steps along `one` from the nodes `src`, steps along `zero` being free. -/
def bfs01 (n : Nat) (src : List Nat) (zero one : Nat → List Nat) : Array Nat := Id.run do
  let mut dist := Array.replicate n unset
  let mut frontier : Array Nat := #[]
  for s in src do
    if dist[s]! == unset then
      dist := dist.set! s 0
      frontier := frontier.push s
  for d in [0:n] do
    if frontier.isEmpty then break
    -- close the level under free steps
    let mut level := frontier
    let mut head := 0
    for _ in [0:n] do
      if head < level.size then
        let x := level[head]!
        head := head + 1
        for y in zero x do
          if dist[y]! == unset then
            dist := dist.set! y d
            level := level.push y
      else break
    -- one paid step
    let mut next : Array Nat := #[]
    for x in level do
      for y in one x do
        if dist[y]! == unset then
          dist := dist.set! y (d + 1)
          next := next.push y
    frontier := next
  return dist

/-! ### Moves, inverses and renamings on ranks -/

/-- Move numbers: 0 U, 1 U2, 2 U', 3 D, 4 D2, 5 D', 6 R2, 7 L2, 8 F2, 9 B2 (`Move.ofIdx`). -/
def halfMoves : List Nat := [1, 4, 6, 7, 8, 9]
def quarterMoves : List Nat := [0, 2, 3, 5]
def allMoves : List Nat := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

/-- Rank of the corner arrangement of rank `r` after move number `m`. -/
def mvRankC (m r : Nat) : Nat := rank8 (permute8 (Move.ofIdx m).srcC (unrank8 r))
/-- The same for the U/D-layer edges. -/
def mvRankE (m r : Nat) : Nat := rank8 (permute8 (Move.ofIdx m).srcE (unrank8 r))
/-- Rank of the inverse arrangement. -/
def invRank (r : Nat) : Nat := rank8 (invPos8 (unrank8 r))

/-- Rename the pieces of `v` by `h` (the arrangement "`h`, then `v`"). -/
def rename (h v : Arr8) : Arr8 := Vector.ofFn fun p => h.get (v.get p)

/-- Tetrad of a corner position or piece: 0 for UFR UBL DFL DBR, 1 for the others. -/
def tetrad (p : Nat) : Nat := #[0, 1, 0, 1, 1, 0, 1, 0].getD p 0

/-- Bit `p` set: the corner at position `p` is out of its tetrad. -/
def badCornerMask (v : Arr8) : Nat :=
  (List.finRange 8).foldl (fun acc p => if tetrad (v.get p).val != tetrad p.val then acc + 2 ^ p.val else acc) 0

/-- Bit `p` set: position `p` holds an M-slice edge (pieces UF UB DF DB have even numbers). -/
def mMask (v : Arr8) : Nat :=
  (List.finRange 8).foldl (fun acc p => if (v.get p).val % 2 == 0 then acc + 2 ^ p.val else acc) 0

def popCount (m : Nat) : Nat := (List.range 8).countP fun k => m.testBit k

/-- Bad edges of an edge pattern: twice the M-slice edges in S positions (the odd positions). -/
def badEdges (mask : Nat) : Nat := 2 * popCount (mask &&& 0xAA)

/-- What a move does to a set of corner positions: position `p` is in the new set when the position its
corner came from was in the old one. -/
def maskMove (m mask : Nat) : Nat :=
  (List.finRange 8).foldl (fun acc p =>
    if mask.testBit ((Move.ofIdx m).srcC.get p).val then acc + 2 ^ p.val else acc) 0

/-- The faces U D F B R L as sets of corner positions. -/
def faceMasks : List Nat := [0x0F, 0xF0, 0x33, 0xCC, 0x99, 0x66]

/-- 0 ("a") when half turns can bring the four bad positions `mask` onto one face, else 1 ("b"). -/
def shapeOf (mask : Nat) : Nat :=
  let d := bfs 256 [mask] fun x => halfMoves.map fun m => maskMove m x
  if faceMasks.any fun f => d[f]! != unset then 0 else 1

/-- The name of a subset from the bad corners and bad edges of a coset, its corner quarter-turn count and
its shape.  With more than four bad corners, or four and more than four bad edges, both are counted in
the frame turned by U D' (`8 - n`).  The letter a/b is kept only for four bad corners and 1, 2 or 5 quarter
turns; with 3 or 4 the two sides of a state differ, and the name says c. -/
def subName (nc ne q shape : Nat) : String :=
  let flip := nc > 4 || (nc == 4 && ne > 4)
  let nc' := if flip then 8 - nc else nc
  let ne' := if flip then 8 - ne else ne
  let letter := if nc' == 4 && (q ≤ 2 || q == 5) then (if shape != 0 then "b" else "a") else "c"
  s!"{nc'}{letter}{q} {ne'}e"

/-- The 14 corner subsets (names of the 420 corner cosets): bad corners (8 counts as 0, 6 as 2), quarter
turns, and the letter a/b for four bad corners. -/
def cornerSubsetName (nbad q shape : Nat) : String :=
  let nb := if nbad == 8 then 0 else if nbad == 6 then 2 else nbad
  let letter := if nb == 4 then (if shape != 0 then "b" else "a") else "c"
  s!"{nb}{letter}{q}"

/-! ### Pairs -/

/-- Side colours of a corner piece: [F/B colour, R/L colour], faces numbered F 0, L 1, B 2, R 3. -/
def cornerCol (piece axis : Nat) : Nat :=
  #[0, 3, 0, 1, 2, 1, 2, 3].getD ((piece % 4) * 2 + axis) 0

/-- The kind of pair that corner piece `cp` at corner position `p` makes with edge piece `ep` at the
touching edge position `q` of the same layer, read off the two stickers that touch on the side face:
0 true pair (side colours equal, U/D colours equal), 1 pseudo pair (both opposite), 2 side semi (side
equal, U/D opposite), 3 top semi (side opposite, U/D equal), 4 none.  The side face of edge position `q`
is `q % 4` (F L B R); a corner in its own tetrad shows its F/B colour on F and B, out of it on R and L. -/
def pairKind (p q cp ep : Nat) : Nat :=
  let face := q % 4
  let axis := if tetrad cp == tetrad p then face % 2 else 1 - face % 2
  let ccol := cornerCol cp axis
  let ecol := ep % 4
  let topSame := (decide (cp < 4)) == (decide (ep < 4))
  if ccol == ecol then (if topSame then 0 else 2)
  else if ccol == (ecol + 2) % 4 then (if topSame then 3 else 1)
  else 4

/-- The two corner positions touching edge position `q` inside its layer. -/
def touching (q : Nat) : Nat × Nat :=
  #[(0, 1), (1, 2), (2, 3), (0, 3), (4, 5), (5, 6), (6, 7), (4, 7)].getD q (0, 0)

/-- The four pair counts of a state, packed in base 32: true + 32 · pseudo + 32² · side semi + 32³ · top
semi, summed over the 16 touching (corner, edge) position pairs of the U and D layers. -/
def pairCounts (c e : Arr8) : Nat :=
  (List.finRange 8).foldl (fun acc q =>
    let (p1, p2) := touching q.val
    let ep := (e.get q).val
    let one (p : Nat) : Nat :=
      let k := pairKind p q.val (c[p]!).val ep
      if k < 4 then 32 ^ k else 0
    acc + one p1 + one p2) 0

/-- For a corner arrangement: entry `q * 8 + x` is what edge piece `x` at edge position `q` adds to the
packed pair counts.  (`pairCounts c e` is the sum of the eight entries `q * 8 + e[q]`.) -/
def pairTable (c : Arr8) : Array Nat :=
  Array.ofFn (n := 64) fun i =>
    let q := i.val / 8
    let x := i.val % 8
    let (p1, p2) := touching q
    let one (p : Nat) : Nat :=
      let k := pairKind p q (c[p]!).val x
      if k < 4 then 32 ^ k else 0
    one p1 + one p2

/-! ### Small index helpers -/

/-- (subset, corner case, corner case) as one number. -/
@[inline] def tripleCode (sub c1 c2 : Nat) : Nat := (sub * 64 + c1) * 64 + c2

/-- (subset, corner case, corner case of the inverse, L, Lp - L, E-slice parity) as one number. -/
@[inline] def tupleCode (sub ccn cci l dl par : Nat) : Nat := ((((sub * 64 + ccn) * 64 + cci) * 16 + l) * 16 + dl) * 2 + par

/-- Place of `x` in the increasing array `a` (`a.size` if it is not there). -/
def findIdx (a : Array Nat) (x : Nat) : Nat := Id.run do
  let mut lo := 0
  let mut hi := a.size
  for _ in [0:64] do
    if lo < hi then
      let mid := (lo + hi) / 2
      if a[mid]! < x then lo := mid + 1 else hi := mid
    else break
  return if lo < a.size && a[lo]! == x then lo else a.size

/-- The numbers below `n` whose flag is set, in increasing order. -/
def flagged (flags : Array Bool) : Array Nat :=
  Nat.fold flags.size (fun i _ acc => if flags[i]! then acc.push i else acc) #[]

/-! ### The tables -/

structure Tabs where
  /-- `cmv[m * 40320 + r]`: rank of the corner arrangement `r` after move `m` -/
  cmv : Array Nat
  /-- the same for the U/D-layer edges -/
  emv : Array Nat
  /-- rank of the inverse arrangement (corners and edges are numbered alike) -/
  inv : Array Nat
  /-- parity of the arrangement of rank `r` -/
  par : Array Nat
  /-- rank ↦ corner coset (0 … 419) -/
  ccos : Array Nat
  /-- corner coset ↦ its smallest rank -/
  ccosRep : Array Nat
  /-- rank ↦ edge pattern (0 … 69) -/
  epat : Array Nat
  epatRep : Array Nat
  epatMask : Array Nat
  /-- `ccosMv[a * 10 + m]`, `epatMv[b * 10 + m]`: the coset / pattern after move `m` -/
  ccosMv : Array Nat
  epatMv : Array Nat
  /-- `htr[a * 70 + b]`: shortest DR → HTR of the HTR coset -/
  htr : Array Nat
  /-- renaming the pieces by U D': on corner cosets, on edge patterns -/
  lmulC : Array Nat
  lmulE : Array Nat
  /-- corner coset ↦ quarter-turn count of the corners -/
  ccQt : Array Nat
  /-- `qtFull[a * 70 + b]`: fewest quarter turns to HTR -/
  qtFull : Array Nat
  /-- corner coset ↦ number of bad corners, mask of the bad positions of its representative, shape (0 a, 1 b) -/
  ccNbad : Array Nat
  ccMask : Array Nat
  ccShape : Array Nat
  /-- `sub48[a * 70 + b]`: number of the subset (0 … 47, in order of first appearance) -/
  sub48 : Array Nat
  subNames : Array String
  /-- corner coset ↦ corner case (0 … 45) -/
  ccase : Array Nat
  ncase : Nat
  /-- rank ↦ optimal corner solution -/
  clen : Array Nat
  /-- `lpar[r * 2 + p]`: shortest corner solution with `p` = number of side half turns mod 2 -/
  lpar : Array Nat
  /-- `setup[a * 70 + b]` -/
  setup : Array Nat
  /-- `ebytes[r * 8 + q]`: the edge piece at position `q` of the arrangement of rank `r` -/
  ebytes : ByteArray
  /-- `symC[a * 16 + σ]`, `symE[b * 16 + σ]`: the corner coset / edge pattern after conjugation by symmetry `σ` -/
  symC : Array Nat
  symE : Array Nat
  /-- the (subset, smaller corner case, larger corner case) that occur, as `tripleCode`s in increasing order -/
  triples : Array Nat
  /-- `tripleCode` ↦ its place in `triples` (or `triples.size`) -/
  triIdx : Array Nat
  /-- the (subset, corner case, corner case of the inverse, L, Lp - L, E-slice parity) that occur, as
  `tupleCode`s in increasing order -/
  tuples : Array Nat

/-- Corner coset of every rank, and the smallest rank of every coset. -/
def cosetTabs (hs : Array Arr8) : Array Nat × Array Nat := Id.run do
  let mut ccos := Array.replicate 40320 65535
  let mut reps : Array Nat := #[]
  for c in [0:40320] do
    if ccos[c]! == 65535 then
      let p := unrank8 c
      let n := reps.size
      reps := reps.push c
      for h in hs do
        ccos := ccos.set! (rank8 (rename h p)) n
  return (ccos, reps)

/-- Edge pattern of every rank; first rank and mask of every pattern. -/
def patTabs (_ : Unit) : Array Nat × Array Nat × Array Nat := Id.run do
  let mut idx := Array.replicate 256 unset
  let mut epat := Array.emptyWithCapacity 40320
  let mut reps : Array Nat := #[]
  let mut masks : Array Nat := #[]
  for e in [0:40320] do
    let mask := mMask (unrank8 e)
    if idx[mask]! == unset then
      idx := idx.set! mask reps.size
      reps := reps.push e
      masks := masks.push mask
    epat := epat.push idx[mask]!
  return (epat, reps, masks)

/-- Smallest member of the class of each node under the maps `imgs` (classes = connected components). -/
def classMin (n : Nat) (imgs : Nat → List Nat) : Array Nat := Id.run do
  let mut lab := Array.replicate n n
  for a in [0:n] do
    if lab[a]! == n then
      -- flood fill from the smallest unlabelled node
      let mut stack : Array Nat := #[a]
      lab := lab.set! a a
      for _ in [0:n * 20] do
        if stack.isEmpty then break
        let x := stack.back!
        stack := stack.pop
        for y in imgs x do
          if lab[y]! == n then
            lab := lab.set! y a
            stack := stack.push y
  return lab

/-- The tables that depend on nothing: computed once by `mkTabs` and handed to `mkTabsFrom`.  (With
closed-term extraction off, a table without arguments that is used inside a loop would be computed again in
every round; so every loop below only sees arguments.) -/
structure BaseTabs where
  cmv : Array Nat
  emv : Array Nat
  inv : Array Nat
  par : Array Nat
  pat : Array Nat × Array Nat × Array Nat
  /-- U D' as a corner and as an edge arrangement -/
  xc : Arr8
  xe : Arr8

def baseTabs (_ : Unit) : BaseTabs where
  cmv := Array.ofFn (n := 10 * 40320) fun i => mvRankC (i.val / 40320) (i.val % 40320)
  emv := Array.ofFn (n := 10 * 40320) fun i => mvRankE (i.val / 40320) (i.val % 40320)
  inv := Array.ofFn (n := 40320) fun i => invRank i.val
  par := Array.ofFn (n := 40320) fun i => parity8 (unrank8 i.val)
  pat := patTabs ()
  xc := (solved.apply [.U, .D']).c
  xe := (solved.apply [.U, .D']).e

@[noinline] def mkTabsFrom (bt : BaseTabs) : Tabs := Id.run do
  let cmv := bt.cmv
  let emv := bt.emv
  -- HTR corners and corner cosets
  let hd := bfs 40320 [0] fun r => halfMoves.map fun m => cmv[m * 40320 + r]!
  let hs : Array Arr8 := ((List.range 40320).filter fun r => hd[r]! != unset).toArray.map unrank8
  let (ccos, ccosRep) := cosetTabs hs
  let (epat, epatRep, epatMask) := bt.pat
  let nc := ccosRep.size
  let ne := epatRep.size
  let ccosMv := Array.ofFn (n := nc * 10) fun i => ccos[cmv[(i.val % 10) * 40320 + ccosRep[i.val / 10]!]!]!
  let epatMv := Array.ofFn (n := ne * 10) fun i => epat[emv[(i.val % 10) * 40320 + epatRep[i.val / 10]!]!]!
  let c0 := ccos[0]!
  let e0 := epat[0]!
  let step (ms : List Nat) (x : Nat) : List Nat :=
    ms.map fun m => ccosMv[(x / 70) * 10 + m]! * 70 + epatMv[(x % 70) * 10 + m]!
  let htr := bfs (nc * 70) [c0 * 70 + e0] (step allMoves)
  -- renaming by U D'
  let lmulC := ccosRep.map fun r => ccos[rank8 (rename bt.xc (unrank8 r))]!
  let lmulE := epatRep.map fun r => epat[rank8 (rename bt.xe (unrank8 r))]!
  -- quarter-turn counts
  let ccQt := bfs01 nc [c0, lmulC[c0]!] (fun a => halfMoves.map fun m => ccosMv[a * 10 + m]!)
    (fun a => quarterMoves.map fun m => ccosMv[a * 10 + m]!)
  let qtFull := bfs01 (nc * 70) [c0 * 70 + e0] (step halfMoves) (step quarterMoves)
  -- bad corners, shape
  let ccMask := ccosRep.map fun r => badCornerMask (unrank8 r)
  let ccNbad := ccMask.map popCount
  let ccShape := ccMask.map fun mask => if popCount mask == 4 then shapeOf mask else 0
  -- the 48 subsets, numbered in order of first appearance
  let mut subNames : Array String := #[]
  let mut sub48 : Array Nat := Array.emptyWithCapacity (nc * 70)
  for a in [0:nc] do
    for b in [0:70] do
      let name := subName ccNbad[a]! (badEdges epatMask[b]!) ccQt[a]! ccShape[a]!
      let i := subNames.toList.idxOf name
      if i == subNames.size then subNames := subNames.push name
      sub48 := sub48.push i
  -- corner cases: corner cosets up to the 16 symmetries and renaming by U D'
  let symC := Array.ofFn (n := nc * 16) fun i =>
    ccos[rank8 (conjC (symOfNat (i.val % 16)) (unrank8 ccosRep[i.val / 16]!))]!
  let orbit := classMin nc fun a => lmulC[a]! :: (List.range 16).map fun s => symC[a * 16 + s]!
  let reps := ((List.range nc).filter fun a => orbit[a]! == a).toArray
  let ccase := orbit.map fun o => reps.toList.idxOf o
  -- corner lengths
  let clen := bfs 40320 [0] fun r => allMoves.map fun m => cmv[m * 40320 + r]!
  let lpar := bfs 80640 [0] fun y => allMoves.map fun m =>
    cmv[m * 40320 + y / 2]! * 2 + (if m ≥ 6 then 1 - y % 2 else y % 2)
  -- setup: half turns to the nearest coset from which a quarter turn lowers the quarter-turn count
  let lowers := (List.range (nc * 70)).filter fun y =>
    qtFull[y]! != 0 && (step quarterMoves y).any fun z => qtFull[z]! + 1 == qtFull[y]!
  let sd := bfs (nc * 70) lowers (step halfMoves)
  let setup := Array.ofFn (n := nc * 70) fun i => if qtFull[i.val]! == 0 then 0 else sd[i.val]!
  let ebytes := Nat.fold 40320 (fun r _ acc =>
    let v := unrank8 r
    (List.finRange 8).foldl (fun acc q => acc.push (v.get q).val.toUInt8) acc) (ByteArray.emptyWithCapacity (40320 * 8))
  let symE := Array.ofFn (n := ne * 16) fun i =>
    epat[rank8 (conjE (symOfNat (i.val % 16)) (unrank8 epatRep[i.val / 16]!))]!
  -- which (subset, corner cases) and which (subset, corner cases, L, Lp - L, parity) occur
  let mut triFlags : Array Bool := Array.replicate (48 * 64 * 64) false
  let mut seenC : Array Bool := Array.replicate (nc * nc * 16 * 16 * 16) false
  let mut tupList : Array Nat := #[]
  for r in [0:40320] do
    let a := ccos[r]!
    let ai := ccos[bt.inv[r]!]!
    let l := clen[r]!
    let d0 := min (lpar[r * 2]! - l) 15
    let d1 := min (lpar[r * 2 + 1]! - l) 15
    let key := (((a * nc + ai) * 16 + l) * 16 + d0) * 16 + d1
    if !seenC[key]! then
      seenC := seenC.set! key true
      let (cn, ci) := (ccase[a]!, ccase[ai]!)
      for b in [0:70] do
        let sub := sub48[a * 70 + b]!
        triFlags := triFlags.set! (tripleCode sub (min cn ci) (max cn ci)) true
        tupList := tupList.push (tupleCode sub cn ci l d0 0)
        tupList := tupList.push (tupleCode sub cn ci l d1 1)
  let triples := flagged triFlags
  let triIdx := Id.run do
    let mut t := Array.replicate (48 * 64 * 64) triples.size
    for i in [0:triples.size] do
      t := t.set! triples[i]! i
    return t
  let sorted := tupList.qsort (· < ·)
  let tuples := Nat.fold sorted.size (fun i _ (acc : Array Nat) =>
    if i == 0 || sorted[i]! != sorted[i - 1]! then acc.push sorted[i]! else acc) #[]
  return { cmv, emv, inv := bt.inv, par := bt.par, ccos, ccosRep, epat, epatRep, epatMask, ccosMv, epatMv, htr,
           lmulC, lmulE, ccQt, qtFull, ccNbad, ccMask, ccShape, sub48, subNames, ccase, ncase := reps.size, clen,
           lpar, setup, ebytes, symC, symE, triples, triIdx, tuples }

/-- All the tables. -/
def mkTabs (_ : Unit) : Tabs := mkTabsFrom (baseTabs ())

/-! ### What is read off one state: constants of the corner arrangement, then the edges -/

/-- Everything that depends on the corner arrangement alone. -/
structure CornerC where
  /-- corner coset, and corner coset of the inverse arrangement -/
  a : Nat
  ai : Nat
  /-- parity of the corner arrangement -/
  pc : Nat
  /-- optimal corner solution, and the shortest with an even / odd number of side half turns -/
  L : Nat
  lp0 : Nat
  lp1 : Nat
  /-- corner case, and corner case of the inverse -/
  ccn : Nat
  cci : Nat
  /-- pair tables of the arrangement and of its inverse -/
  pt : Array Nat
  pti : Array Nat
  /-- `t6[b * 2 + par]`: place in `Tabs.tuples` of (subset, corner cases, L, Lp - L, parity) with edge pattern `b` -/
  t6 : Array Nat

def cornerC (tb : Tabs) (c : Arr8) : CornerC :=
  let r := rank8 c
  let ri := tb.inv[r]!
  let a := tb.ccos[r]!
  let ai := tb.ccos[ri]!
  let l := tb.clen[r]!
  let lp0 := tb.lpar[r * 2]!
  let lp1 := tb.lpar[r * 2 + 1]!
  let ccn := tb.ccase[a]!
  let cci := tb.ccase[ai]!
  { a, ai, pc := tb.par[r]!, L := l, lp0, lp1, ccn, cci, pt := pairTable c, pti := pairTable (unrank8 ri),
    t6 := Array.ofFn (n := 140) fun i =>
      findIdx tb.tuples (tupleCode tb.sub48[a * 70 + i.val / 2]! ccn cci l
        (min ((if i.val % 2 == 0 then lp0 else lp1) - l) 15) (i.val % 2)) }

/-- Packed pair counts of (corner arrangement with pair table `pt`, U/D edges of rank `e`). -/
@[inline] def packedPairs (tb : Tabs) (pt : Array Nat) (e : Nat) : Nat :=
  let b := e * 8
  pt[(tb.ebytes.get! b).toNat]! + pt[8 + (tb.ebytes.get! (b + 1)).toNat]! +
  pt[16 + (tb.ebytes.get! (b + 2)).toNat]! + pt[24 + (tb.ebytes.get! (b + 3)).toNat]! +
  pt[32 + (tb.ebytes.get! (b + 4)).toNat]! + pt[40 + (tb.ebytes.get! (b + 5)).toNat]! +
  pt[48 + (tb.ebytes.get! (b + 6)).toNat]! + pt[56 + (tb.ebytes.get! (b + 7)).toNat]!

/-- The reads of a state with corner constants `C` and U/D edges of rank `e`. -/
structure Reads where
  sub : Nat
  hn : Nat
  hi : Nat
  /-- parity of the E slice (= parity of corners + parity of U/D edges) -/
  par : Nat
  L : Nat
  /-- Lp: shortest corner solution whose number of side half turns has the E slice's parity -/
  lp : Nat
  ccn : Nat
  cci : Nat
  /-- packed pair counts, and those of the inverse state -/
  pairs : Nat
  pairsI : Nat
  /-- the setup + HTR bound G (0 for HTR cosets) -/
  g : Nat
  /-- the HTR coset `a * 70 + b` -/
  coset : Nat
  /-- place in `Tabs.tuples` of (subset, corner case, corner case of the inverse, L, Lp - L, parity) -/
  t6 : Nat

@[inline] def reads (tb : Tabs) (C : CornerC) (e : Nat) : Reads :=
  let ei := tb.inv[e]!
  let x := C.a * 70 + tb.epat[e]!
  let xi := C.ai * 70 + tb.epat[ei]!
  let hn := tb.htr[x]!
  let hi := tb.htr[xi]!
  let par := (C.pc + tb.par[e]!) % 2
  { sub := tb.sub48[x]!, hn, hi, par, L := C.L, lp := if par == 0 then C.lp0 else C.lp1,
    ccn := C.ccn, cci := C.cci, pairs := packedPairs tb C.pt e, pairsI := packedPairs tb C.pti ei,
    g := if tb.qtFull[x]! == 0 then 0 else max (hn + tb.setup[xi]!) (hi + tb.setup[x]!),
    coset := x, t6 := C.t6[tb.epat[e]! * 2 + par]! }

end Census
end DRBound
