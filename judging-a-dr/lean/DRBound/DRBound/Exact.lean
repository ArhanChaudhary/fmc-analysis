/-
  DRBound.Exact — the exact optimal length of every state of the domino-reduction group, by a
  symmetry-reduced table.

  Plan.
    * The 16 symmetries of the cube that keep the U/D axis act on states by conjugation (`State.conj`).
      Conjugate states have the same optimal length, because conjugation carries moves to moves.
    * Every corner arrangement is conjugate to exactly one of 2768 representatives (`crep`).  A state whose
      corners are a representative is stored at index `(class, rank of the U/D edges, number of the E-slice
      arrangement among the 12 of the right parity)`; any other state is first conjugated (`ridx`).
    * A table `T` of 2768 × 40320 × 12 = 1,339,269,120 bytes is filled by breadth-first search (`mkTable`).

  Nothing about the symmetries, the class tables or the search is assumed.  The theorems at the end of this
  file take as hypotheses that certain exhaustive checks return `true` (`ModelChecked`, `tableOK … = true`);
  `DRBound.CertifiedExactTable` runs those checks as compiled code, and `DRBound.CertifiedExact` states the
  results.

  This file depends only on `DRBound.Cube` (the model) and `DRBound.Certificate` (the general lemma), so
  that changes to the rungs in `DRBound.Search` do not force the long table check to run again.  Its
  auxiliary definitions live in the namespace `DRBound.Exact`.

  Engineering notes.
    * Compiled Lean evaluates every definition without arguments, and every closed subterm, when the module
      is loaded.  Nothing expensive may be evaluated that way, so closed-term extraction is switched off for
      this file and every expensive value is a function of an argument.
    * With extraction off, a closed `let` used inside a loop is recomputed in every iteration.  Hence the big
      tables are built once by a caller and handed to `@[noinline]` workers as arguments (`bfsPasses`,
      `tableOKWith`).
    * The kernel must never be led to *evaluate* a class table or the big table.  The proofs below therefore
      only unfold definitions down to syntactically equal terms (`simp only`, `rw`, `show`), and never ask
      for a computation by `rfl` or `decide`.
-/
import DRBound.Cube

set_option compiler.extract_closed false

namespace DRBound
namespace Exact

/-! ### Memo tables

`memoGet (memo n f) f i` is `f i`, looked up in a table when `i < n`.  The checkers below are written with
such tables so that they run fast, and `memoGet_memo` turns them back into the plain formulas. -/

def memo {α : Type} (n : Nat) (f : Nat → α) : Array α := Array.ofFn (n := n) fun i => f i.val

@[inline] def memoGet {α : Type} (a : Array α) (f : Nat → α) (i : Nat) : α :=
  if h : i < a.size then a[i] else f i

theorem memoGet_memo {α : Type} (n : Nat) (f : Nat → α) (i : Nat) : memoGet (memo n f) f i = f i := by
  unfold memoGet memo
  split
  · simp
  · rfl

/-! ### Small utilities: `Nat.all`, ranks, parities, moves by number -/

theorem nat_all_spec : ∀ (n : Nat) (f : (i : Nat) → i < n → Bool), n.all f = true →
    ∀ (i : Nat) (h : i < n), f i h = true
  | 0, _, _, i, h => absurd h (Nat.not_lt_zero i)
  | n + 1, f, hall, i, h => by
      rw [Nat.all_succ] at hall
      simp only [Bool.and_eq_true] at hall
      rcases Nat.lt_succ_iff_lt_or_eq.mp h with hlt | heq
      · exact nat_all_spec n _ hall.1 i hlt
      · subst heq; exact hall.2

def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

/-- Lexicographic rank of an arrangement of 8 pieces (0 … 40319 for permutations). -/
def rank8 (v : Arr8) : Nat := Id.run do
  let mut r := 0
  for i in [0:8] do
    let mut k := 0
    for j in [i+1:8] do
      if (v[j]!).val < (v[i]!).val then k := k + 1
    r := r * (8 - i) + k
  return r

/-- The arrangement with a given rank. -/
def unrank8 (r : Nat) : Arr8 := Id.run do
  let mut avail : List (Fin 8) := List.finRange 8
  let mut out : Array (Fin 8) := #[]
  let mut r := r
  for i in [0:8] do
    let f := fact (7 - i)
    let x := avail.getD (r / f) 0
    r := r % f
    out := out.push x
    avail := avail.erase x
  return Vector.ofFn fun p => out.getD p.val 0

/-- Parity (0 or 1) of an arrangement of eight pieces: the number of inversions mod 2. -/
def parity8 (v : Arr8) : Nat := Id.run do
  let mut k := 0
  for i in [0:8] do
    for j in [i+1:8] do
      if (v[j]!).val < (v[i]!).val then k := k + 1
  return k % 2

/-- Parity (0 or 1) of an arrangement of the four E-slice edges. -/
def parity4 (s : Arr4) : Nat := Id.run do
  let mut k := 0
  for i in [0:4] do
    for j in [i+1:4] do
      if (s[j]!).val < (s[i]!).val then k := k + 1
  return k % 2

def _root_.DRBound.Move.ofIdx : Nat → Move
  | 0 => .U | 1 => .U2 | 2 => .U' | 3 => .D | 4 => .D2 | 5 => .D' | 6 => .R2 | 7 => .L2 | 8 => .F2 | _ => .B2

@[simp] theorem ofIdx_idx (m : Move) : Move.ofIdx m.idx = m := by cases m <;> rfl

/-- Quarter turns are odd on the corners; half turns are even. -/
def _root_.DRBound.Move.flipC (m : Move) : Nat := if m.isHalf then 0 else 1

/-- Quarter turns (a 4-cycle) and side half turns (one swap) are odd on the U/D-layer edges; U2 and D2 are even. -/
def _root_.DRBound.Move.flipE (m : Move) : Nat := if m.isSide || !m.isHalf then 1 else 0

/-- Side half turns (one swap) are odd on the E slice; U and D moves do not touch it. -/
def _root_.DRBound.Move.flipS (m : Move) : Nat := if m.isSide then 1 else 0

/-- The three permutation parities fit together: corners and U/D-layer edges together are even exactly when
the E slice is.  Every state reachable from the solved cube is of this kind (`ModelChecked.good_apply`). -/
def _root_.DRBound.State.ParityOK (g : State) : Prop := (parity8 g.c + parity8 g.e) % 2 = parity4 g.s

instance (g : State) : Decidable g.ParityOK := by unfold State.ParityOK; infer_instance

/-! ### The 16 symmetries (as in `drtools/src/core.rs`) -/

/-- A position map: whatever sits at position `p` is carried to position `t[p]`. -/
structure PosMap where
  c : Arr8
  e : Arr8
  s : Arr4

def PosMap.one : PosMap := ⟨id8, id8, id4⟩

/-- First `a`, then `b`. -/
def PosMap.andThen (a b : PosMap) : PosMap :=
  ⟨Vector.ofFn fun p => b.c.get (a.c.get p), Vector.ofFn fun p => b.e.get (a.e.get p),
   Vector.ofFn fun p => b.s.get (a.s.get p)⟩

def invPos8 (t : Arr8) : Arr8 :=
  Vector.ofFn fun q => ((List.finRange 8).find? fun p => decide (t.get p = q)).getD 0

def invPos4 (t : Arr4) : Arr4 :=
  Vector.ofFn fun q => ((List.finRange 4).find? fun p => decide (t.get p = q)).getD 0

def PosMap.inv (a : PosMap) : PosMap := ⟨invPos8 a.c, invPos8 a.e, invPos4 a.s⟩

/-- y: quarter rotation of the whole cube about the U/D axis. -/
def symY : PosMap := ⟨#v[1, 2, 3, 0, 5, 6, 7, 4], #v[1, 2, 3, 0, 5, 6, 7, 4], #v[1, 2, 3, 0]⟩
/-- x2: half rotation of the whole cube about the R/L axis. -/
def symX2 : PosMap := ⟨#v[7, 6, 5, 4, 3, 2, 1, 0], #v[6, 5, 4, 7, 2, 1, 0, 3], #v[3, 2, 1, 0]⟩
/-- The mirror L ↔ R. -/
def symM : PosMap := ⟨#v[1, 0, 3, 2, 5, 4, 7, 6], #v[0, 3, 2, 1, 4, 7, 6, 5], #v[1, 0, 3, 2]⟩

/-- Symmetry number `mir*8 + x2*4 + ypow`: the mirror `mir` times, then x2 `x2` times, then y `ypow` times. -/
def mkSym (i : Nat) : PosMap :=
  let a := if i / 8 % 2 = 1 then symM else PosMap.one
  let a := if i / 4 % 2 = 1 then a.andThen symX2 else a
  Nat.repeat (fun a => a.andThen symY) (i % 4) a

/-- A symmetry, by its number. -/
abbrev Sym := Fin 16

def allSyms : List Sym := List.finRange 16

theorem mem_allSyms (σ : Sym) : σ ∈ allSyms := List.mem_finRange σ

def symOfNat (i : Nat) : Sym := ⟨i % 16, Nat.mod_lt _ (by decide)⟩

@[simp] theorem symOfNat_val (σ : Sym) : symOfNat σ.val = σ := Fin.ext (Nat.mod_eq_of_lt σ.isLt)

/-- The number of a symmetry.  (A plain function on purpose: with the projection `σ.val` in its place, the
kernel would try to *compute* `σ` when it unfolds a definition, and `σ` may be a table lookup.) -/
def symIdx (σ : Sym) : Nat := σ.val

@[simp] theorem symOfNat_idx (σ : Sym) : symOfNat (symIdx σ) = σ := Fin.ext (Nat.mod_eq_of_lt σ.isLt)

def symTab : Array PosMap := memo 16 mkSym
def symTabInv : Array PosMap := memo 16 fun i => (mkSym i).inv

def symPos (σ : Sym) : PosMap := symTab.getD σ.val PosMap.one
def symPosInv (σ : Sym) : PosMap := symTabInv.getD σ.val PosMap.one

/-- Conjugation by the position map `t` with inverse `ti`: position `t p` receives piece `t (v p)`. -/
def conj8 (t ti v : Arr8) : Arr8 := Vector.ofFn fun q => t.get (v.get (ti.get q))
def conj4 (t ti v : Arr4) : Arr4 := Vector.ofFn fun q => t.get (v.get (ti.get q))

def conjC (σ : Sym) (v : Arr8) : Arr8 := conj8 (symPos σ).c (symPosInv σ).c v
def conjE (σ : Sym) (v : Arr8) : Arr8 := conj8 (symPos σ).e (symPosInv σ).e v
def conjS (σ : Sym) (v : Arr4) : Arr4 := conj4 (symPos σ).s (symPosInv σ).s v

/-- The state `g` as seen after turning / mirroring the whole cube by the symmetry `σ`. -/
def _root_.DRBound.State.conj (g : State) (σ : Sym) : State := ⟨conjC σ g.c, conjE σ g.e, conjS σ g.s⟩

/-- `symMul τ σ`: first `σ`, then `τ`. -/
def symMulTab : Array Sym := memo 256 fun i =>
  let t := (mkSym (i % 16)).andThen (mkSym (i / 16))
  (allSyms.find? fun ρ => decide ((symPos ρ).c = t.c)).getD 0

def symMul (τ σ : Sym) : Sym := symMulTab.getD (τ.val * 16 + σ.val) 0

def symInvTab : Array Sym := memo 16 fun i =>
  (allSyms.find? fun ρ => decide ((symPos ρ).c = (mkSym i).inv.c)).getD 0

def symInv (σ : Sym) : Sym := symInvTab.getD σ.val 0

/-- The move that `m` becomes under the symmetry `σ`. -/
def symMoveTab : Array Move := memo 160 fun i =>
  (Move.all.find? fun m' => decide (m'.srcC = conjC (symOfNat (i / 10)) (Move.ofIdx (i % 10)).srcC)).getD .U

def symMove (σ : Sym) (m : Move) : Move := symMoveTab.getD (σ.val * 10 + m.idx) .U

/-! ### Corner classes -/

structure ClassData where
  /-- rank of a corner arrangement ↦ its class -/
  cls : Array Nat
  /-- rank of a corner arrangement ↦ a symmetry carrying it to the representative of its class -/
  sym : Array Sym
  /-- class ↦ representative (the arrangement of smallest rank) -/
  rep : Array Arr8

def classData : ClassData := Id.run do
  let mut cls : Array Nat := Array.replicate 40320 40320
  let mut sym : Array Sym := Array.replicate 40320 0
  let mut rep : Array Arr8 := #[]
  for r in [0:40320] do
    if cls[r]! == 40320 then
      let c := unrank8 r
      let k := rep.size
      rep := rep.push c
      for σ in allSyms do
        let d := rank8 (conjC σ c)
        if cls[d]! == 40320 then
          cls := cls.set! d k
          sym := sym.set! d (symInv σ)
  return ⟨cls, sym, rep⟩

/-- Class (0 … 2767) of a corner arrangement under the 16 symmetries. -/
def cclass (c : Arr8) : Nat := classData.cls.getD (rank8 c) 0
/-- A symmetry that carries `c` to the representative of its class. -/
def symTo (c : Arr8) : Sym := classData.sym.getD (rank8 c) 0
/-- The representative of class `k`. -/
def crep (k : Nat) : Arr8 := classData.rep.getD k id8

/-! ### The E slice: 12 arrangements of each parity -/

def perms4 : List Arr4 :=
  (List.finRange 4).flatMap fun a => (List.finRange 4).flatMap fun b => (List.finRange 4).flatMap fun c =>
    (List.finRange 4).filterMap fun d =>
      let v : Arr4 := #v[a, b, c, d]
      if decide (IsPerm4 v) then some v else none

def sliceTab : Array Arr4 :=
  ((perms4.filter fun s => parity4 s == 0) ++ (perms4.filter fun s => parity4 s == 1)).toArray

/-- The `j`-th (0 … 11) arrangement of the E slice with parity `p`. -/
def slice (p j : Nat) : Arr4 := sliceTab.getD (p * 12 + j) id4

def code4 (s : Arr4) : Nat :=
  (((s.get 0).val * 4 + (s.get 1).val) * 4 + (s.get 2).val) * 4 + (s.get 3).val

def s12Tab : Array Nat := Id.run do
  let mut t := Array.replicate 256 0
  for p in [0:2] do
    for j in [0:12] do
      t := t.set! (code4 (slice p j)) j
  return t

/-- Number (0 … 11) of an E-slice arrangement among those of its own parity. -/
def s12 (s : Arr4) : Nat := s12Tab.getD (code4 s) 0

/-! ### The reduced index -/

/-- Table index of (corner class, rank of the U/D edges, number of the E-slice arrangement). -/
def idx3 (k e s : Nat) : Nat := (k * 40320 + e) * 12 + s

/-- The state stored at `(k, e, s)`: corners = representative of class `k`, U/D edges of rank `e`, and the
`s`-th E-slice arrangement of the parity that corners and edges force. -/
def entryState (k e s : Nat) : State :=
  ⟨crep k, unrank8 e, slice ((parity8 (crep k) + parity8 (unrank8 e)) % 2) s⟩

/-- `g`, conjugated so that its corners are a class representative. -/
def canon (g : State) : State := g.conj (symTo g.c)

/-- **The reduced index** of a state. -/
def ridx (g : State) : Nat := idx3 (cclass g.c) (rank8 (canon g).e) (s12 (canon g).s)

/-- Table value as a number. -/
def tv (T : ByteArray) (i : Nat) : Nat := (T.get! i).toNat

/-! ### Exhaustive checks of the model (run in `DRBound.CertifiedExact`) -/

def allPerm8 (P : Arr8 → Bool) : Bool := all8 fun v => !decide (IsPerm8 v) || P v
def allPerm4 (P : Arr4 → Bool) : Bool := all4 fun v => !decide (IsPerm4 v) || P v

/-- Conjugation keeps arrangements legal and keeps their parity. -/
def conjPermOK (syms : List Sym) : Bool :=
  (allPerm8 fun v => syms.all fun σ =>
    decide (IsPerm8 (conjC σ v)) && decide (IsPerm8 (conjE σ v)) &&
    decide (parity8 (conjC σ v) = parity8 v) && decide (parity8 (conjE σ v) = parity8 v)) &&
  (allPerm4 fun v => syms.all fun σ =>
    decide (IsPerm4 (conjS σ v)) && decide (parity4 (conjS σ v) = parity4 v))

/-- Conjugation carries moves to moves: doing `m` and then conjugating by `σ` is conjugating and then
doing `symMove σ m`. -/
def conjMoveOK (syms : List Sym) : Bool :=
  (allPerm8 fun v => syms.all fun σ => Move.all.all fun m =>
    decide (conjC σ (permute8 m.srcC v) = permute8 (symMove σ m).srcC (conjC σ v)) &&
    decide (conjE σ (permute8 m.srcE v) = permute8 (symMove σ m).srcE (conjE σ v))) &&
  (allPerm4 fun v => syms.all fun σ => Move.all.all fun m =>
    decide (conjS σ (permute4 m.srcS v) = permute4 (symMove σ m).srcS (conjS σ v)))

/-- Conjugating twice is conjugating by the product; symmetry 0 does nothing. -/
def conjMulOK (syms : List Sym) : Bool :=
  (allPerm8 fun v => decide (conjC 0 v = v) && decide (conjE 0 v = v) &&
    syms.all fun τ => syms.all fun σ =>
      decide (conjC τ (conjC σ v) = conjC (symMul τ σ) v) &&
      decide (conjE τ (conjE σ v) = conjE (symMul τ σ) v)) &&
  (allPerm4 fun v => decide (conjS 0 v = v) &&
    syms.all fun τ => syms.all fun σ => decide (conjS τ (conjS σ v) = conjS (symMul τ σ) v))

/-- Inverses, the solved cube is fixed by every symmetry, and `symMove σ` is onto. -/
def symGroupOK (syms : List Sym) : Bool :=
  syms.all fun a =>
    decide (symMul (symInv a) a = 0) &&
    decide (conjC a id8 = id8) && decide (conjE a id8 = id8) && decide (conjS a id4 = id4) &&
    (syms.all fun b => decide (symMul (symMul a (symInv b)) b = a)) &&
    (Move.all.all fun m => decide (symMove a (symMove (symInv a) m) = m))

/-- Corner classes: the class number is in range, `symTo` carries an arrangement to the representative of
its class, and conjugate arrangements are in the same class. -/
def classOK (syms : List Sym) : Bool :=
  allPerm8 fun c =>
    decide (cclass c < 2768) && decide (conjC (symTo c) c = crep (cclass c)) &&
    syms.all fun σ => decide (cclass (conjC σ c) = cclass c)

/-- Moves keep arrangements legal, and change their parities as `flipC`, `flipE`, `flipS` say. -/
def moveOK (ms : List Move) : Bool :=
  (allPerm8 fun v => ms.all fun m =>
    decide (IsPerm8 (permute8 m.srcC v)) && decide (IsPerm8 (permute8 m.srcE v)) &&
    decide (parity8 (permute8 m.srcC v) = (parity8 v + m.flipC) % 2) &&
    decide (parity8 (permute8 m.srcE v) = (parity8 v + m.flipE) % 2)) &&
  (allPerm4 fun v => ms.all fun m =>
    decide (IsPerm4 (permute4 m.srcS v)) &&
    decide (parity4 (permute4 m.srcS v) = (parity4 v + m.flipS) % 2))

/-- Ranks: below `n` (= 40320), and `unrank8` undoes `rank8`. -/
def rankOK (n : Nat) : Bool :=
  allPerm8 fun v => decide (rank8 v < n) && decide (unrank8 (rank8 v) = v)

/-- E slice: the number is below `n` (= 12) and `slice` undoes `s12`. -/
def sliceIdxOK (n : Nat) : Bool :=
  allPerm4 fun s => decide (s12 s < n) && decide (slice (parity4 s) (s12 s) = s)

/-- The solved cube has consistent parities. -/
def solvedParityOK (g : State) : Bool := decide g.ParityOK

/-- All the exhaustive checks of the model. -/
structure ModelChecked : Prop where
  conjPerm : conjPermOK allSyms = true
  conjMove : conjMoveOK allSyms = true
  conjMul : conjMulOK allSyms = true
  group : symGroupOK allSyms = true
  cls : classOK allSyms = true
  move : moveOK Move.all = true
  rank : rankOK 40320 = true
  sliceIdx : sliceIdxOK 12 = true
  solvedPar : solvedParityOK solved = true

/-! ### Tables shared by the search and by the table check -/

/-- Rank of the U/D edges after move number `b` and conjugation by symmetry number `a`. -/
def emF (a b e : Nat) : Nat := rank8 (conjE (symOfNat a) (permute8 (Move.ofIdx b).srcE (unrank8 e)))

def emTable (_ : Unit) : Array (Array (Array Nat)) :=
  memo 16 fun a => memo 10 fun b => memo 40320 fun e => emF a b e

@[inline] def emGet (em : Array (Array (Array Nat))) (a b e : Nat) : Nat :=
  memoGet (memoGet (memoGet em (fun a => memo 10 fun b => memo 40320 fun e => emF a b e) a)
    (fun b => memo 40320 fun e => emF a b e) b) (fun e => emF a b e) e

theorem emGet_eq (a b e : Nat) : emGet (emTable ()) a b e = emF a b e := by
  simp only [emGet, emTable, memoGet_memo]

/-- Rank of the U/D edges after conjugation by symmetry number `a`. -/
def esF (a e : Nat) : Nat := rank8 (conjE (symOfNat a) (unrank8 e))

def esTable (_ : Unit) : Array (Array Nat) := memo 16 fun a => memo 40320 fun e => esF a e

@[inline] def esGet (es : Array (Array Nat)) (a e : Nat) : Nat :=
  memoGet (memoGet es (fun a => memo 40320 fun e => esF a e) a) (fun e => esF a e) e

theorem esGet_eq (a e : Nat) : esGet (esTable ()) a e = esF a e := by
  simp only [esGet, esTable, memoGet_memo]

/-- Parity of the U/D-edge arrangement of rank `e`. -/
def peF (e : Nat) : Nat := parity8 (unrank8 e)

def peTable (_ : Unit) : Array Nat := memo 40320 peF

/-- Number of the `s`-th E-slice arrangement of parity `p` after conjugation by `ρ`. -/
def ssF (ρ : Sym) (p s : Nat) : Nat := s12 (conjS ρ (slice p s))

/-- For the representative `c` and move number `j`: class of the moved corners … -/
def rowK (c : Arr8) (j : Nat) : Nat := cclass (permute8 (Move.ofIdx j).srcC c)
/-- … the number of the symmetry that carries them to their representative … -/
def rowS (c : Arr8) (j : Nat) : Nat := symIdx (symTo (permute8 (Move.ofIdx j).srcC c))
/-- … and what happens to the `s`-th E-slice arrangement of parity `p`. -/
def rowSm (c : Arr8) (p j s : Nat) : Nat :=
  s12 (conjS (symTo (permute8 (Move.ofIdx j).srcC c)) (permute4 (Move.ofIdx j).srcS (slice p s)))

/-! ### Breadth-first search (not trusted: its result is checked entry by entry) -/

structure SearchTabs where
  em : Array (Array (Array Nat))
  pe : Array Nat
  /-- `es[ρ][e]`: rank of the U/D edges of rank `e` after conjugation by `ρ` -/
  es : Array (Array Nat)
  /-- `ss[ρ][p][s]`: number of the `s`-th E-slice arrangement of parity `p` after conjugation by `ρ` -/
  ss : Array (Array (Array Nat))
  /-- class ↦ the symmetries other than 0 that fix its representative -/
  stab : Array (List Nat)
  /-- class ↦ parity of its representative -/
  cpar : Array Nat

def searchTabs (_ : Unit) : SearchTabs where
  em := emTable ()
  pe := peTable ()
  es := esTable ()
  ss := memo 16 fun a => memo 2 fun p => memo 12 fun s => ssF (symOfNat a) p s
  stab := memo 2768 fun k =>
    ((List.range 16).filter fun a => a != 0 && decide (conjC (symOfNat a) (crep k) = crep k))
  cpar := memo 2768 fun k => parity8 (crep k)

/-- Expand every entry of row `k` that has value `d`: each unreached neighbour, and its images under the
symmetries fixing the neighbour's corner representative, get value `d + 1`. -/
def bfsRow (tb : SearchTabs) (d : UInt8) (k : Nat) (T : ByteArray) : ByteArray :=
  let c := crep k
  let pc := parity8 c
  let kk := memo 10 (rowK c)
  let sg := memo 10 (rowS c)
  let sm := memo 2 fun p => memo 10 fun j => memo 12 fun s => rowSm c p j s
  let d1 := d + 1
  Nat.fold 40320 (fun e _ T =>
    let i0 := (k * 40320 + e) * 12
    if !(Nat.any 12 fun s _ => T.get! (i0 + s) == d) then T else
      let p := (pc + tb.pe[e]!) % 2
      let smp := sm[p]!
      let e2 := memo 10 fun j => tb.em[sg[j]!]![j]![e]!
      Nat.fold 12 (fun s _ T =>
        if T.get! (i0 + s) != d then T else
          Nat.fold 10 (fun j _ T =>
            let k2 := kk[j]!
            let ej := e2[j]!
            let s2 := smp[j]![s]!
            let i2 := (k2 * 40320 + ej) * 12 + s2
            if T.get! i2 != 255 then T else
              let T := T.set! i2 d1
              match tb.stab[k2]! with
              | [] => T
              | st =>
                let p2 := (tb.cpar[k2]! + tb.pe[ej]!) % 2
                st.foldl (fun T ρ =>
                  let i3 := (k2 * 40320 + tb.es[ρ]![ej]!) * 12 + tb.ss[ρ]![p2]![s2]!
                  if T.get! i3 != 255 then T else T.set! i3 d1) T) T) T) T

/-- A table of `n` entries, all 255 ("not reached"). -/
def blankTable (n : Nat) : ByteArray :=
  Nat.fold n (fun _ _ T => T.push 255) (ByteArray.emptyWithCapacity n)

/-- One round of search: expand every entry with value `d`. -/
@[noinline] def bfsPass (tb : SearchTabs) (d : Nat) (T : ByteArray) : ByteArray :=
  Nat.fold 2768 (fun k _ T => bfsRow tb d.toUInt8 k T) T

/-- Rounds `0 … depth-1`. -/
@[noinline] def bfsPasses (tb : SearchTabs) (depth : Nat) (T : ByteArray) : ByteArray :=
  Nat.fold depth (fun d _ T => bfsPass tb d T) T

/-- **The table**: breadth-first search from the solved cube, `depth` rounds.  After round `d` every state
with optimal length at most `d + 1` has its value; 255 = not reached yet. -/
def mkTable (depth : Nat) : ByteArray :=
  bfsPasses (searchTabs ()) depth ((blankTable (2768 * 40320 * 12)).set! (ridx solved) 0)

/-! ### The table check -/

/-- One entry, given the table index `nb m` of the state reached by each move `m`.  Skipped if the value is
`cap` or more.  Otherwise: every move changes the value by at most one; value 0 only at the solved cube;
from a positive value some move goes down by one. -/
@[inline] def entryOK (T : ByteArray) (cap k e s : Nat) (nb : Move → Nat) : Bool :=
  decide (cap ≤ tv T (idx3 k e s)) ||
    ((Move.all.all fun m =>
        decide (tv T (idx3 k e s) ≤ tv T (nb m) + 1) && decide (tv T (nb m) ≤ tv T (idx3 k e s) + 1)) &&
     (if tv T (idx3 k e s) = 0 then decide (entryState k e s = solved)
      else Move.all.any fun m => tv T (nb m) + 1 == tv T (idx3 k e s)))

/-- All entries of row `k`, against all ten moves. -/
def checkRow (T : ByteArray) (cap : Nat) (em : Array (Array (Array Nat))) (pe : Array Nat) (k : Nat) : Bool :=
  let c := crep k
  let pc := parity8 c
  let kk := memo 10 (rowK c)
  let sg := memo 10 (rowS c)
  let sm := memo 2 fun p => memo 10 fun j => memo 12 fun s => rowSm c p j s
  Nat.all 40320 fun e _ =>
    let p := (pc + memoGet pe peF e) % 2
    let smp := memoGet sm (fun p => memo 10 fun j => memo 12 fun s => rowSm c p j s) p
    let fb : Nat → Nat := fun j => (memoGet kk (rowK c) j * 40320 + emGet em (memoGet sg (rowS c) j) j e) * 12
    let base := memo 10 fb
    Nat.all 12 fun s _ =>
      entryOK T cap k e s fun m =>
        memoGet base fb m.idx +
          memoGet (memoGet smp (fun j => memo 12 fun s => rowSm c p j s) m.idx) (fun s => rowSm c p m.idx s) s

/-- Row `k`: the table is constant on the images of an entry under the symmetries (other than 0) that fix
the corner representative. -/
def stabRow (T : ByteArray) (syms : List Sym) (es : Array (Array Nat)) (pe : Array Nat) (k : Nat) : Bool :=
  let c := crep k
  let pc := parity8 c
  syms.all fun ρ => decide (ρ = 0) || !decide (conjC ρ c = c) ||
    (let ss := memo 2 fun p => memo 12 fun s => ssF ρ p s
     Nat.all 40320 fun e _ =>
      let p := (pc + memoGet pe peF e) % 2
      let ssp := memoGet ss (fun p => memo 12 fun s => ssF ρ p s) p
      let e2 := esGet es ρ.val e
      Nat.all 12 fun s _ =>
        T.get! (idx3 k e2 (memoGet ssp (fun s => ssF ρ p s) s)) == T.get! (idx3 k e s))

/-- The table check with the lookup tables handed in. -/
@[noinline] def tableOKWith (T : ByteArray) (nk cap : Nat) (em : Array (Array (Array Nat)))
    (es : Array (Array Nat)) (pe : Array Nat) : Bool :=
  decide (T.get! (ridx solved) = 0) &&
    Nat.all nk fun k _ => checkRow T cap em pe k && stabRow T allSyms es pe k

/-- **The table check**, rows `0 … nk-1`, entries with value below `cap`. -/
def tableOK (T : ByteArray) (nk cap : Nat) : Bool :=
  tableOKWith T nk cap (emTable ()) (esTable ()) (peTable ())

/-- No entry of rows `0 … nk-1` exceeds `maxv`. -/
def maxOK (T : ByteArray) (nk maxv : Nat) : Bool :=
  Nat.all nk fun k _ => Nat.all 40320 fun e _ => Nat.all 12 fun s _ => decide (tv T (idx3 k e s) ≤ maxv)

/-- The listed (scramble, value) pairs agree with the table. -/
def samplesOK (T : ByteArray) (samples : List (List Move × Nat)) : Bool :=
  samples.all fun c => tv T (ridx (solved.apply c.1)) == c.2

/-! ### Counting -/

/-- Number of corner arrangements in class `k`: 16 / (number of symmetries fixing the representative). -/
def classWeight (k : Nat) : Nat :=
  16 / (allSyms.filter fun ρ => decide (conjC ρ (crep k) = crep k)).length

/-- The list of `n + 1` numbers: for each value `t` = 0 … n-1 the number of table entries with value `t`,
and last the number of entries with value `n` or more; an entry of row `k` is counted `classWeight k`
times.

That this weighted count of *entries* is the number of *states* with that table value is the
orbit–stabiliser fact (each state with corners in class `k` is conjugate to `16 / classWeight k` entries of
row `k`, counted with multiplicity).  It is not proved in Lean. -/
def depthCounts (T : ByteArray) (nk n : Nat) : List Nat :=
  (Nat.fold nk (fun k _ acc =>
    let w := classWeight k
    Nat.fold 40320 (fun e _ acc =>
      Nat.fold 12 (fun s _ acc => acc.modify (min (tv T (idx3 k e s)) n) (· + w)) acc) acc)
    (Array.replicate (n + 1) 0)).toList

/-! ## From the checks to the theorems -/

theorem allPerm8_spec {P : Arr8 → Bool} (h : allPerm8 P = true) (v : Arr8) (hv : IsPerm8 v) : P v = true := by
  have h' : (!decide (IsPerm8 v) || P v) = true := all8_spec (P := fun v => !decide (IsPerm8 v) || P v) h v
  simp only [Bool.or_eq_true, Bool.not_eq_true', decide_eq_false_iff_not] at h'
  rcases h' with h' | h'
  · exact absurd hv h'
  · exact h'

theorem allPerm4_spec {P : Arr4 → Bool} (h : allPerm4 P = true) (v : Arr4) (hv : IsPerm4 v) : P v = true := by
  have h' : (!decide (IsPerm4 v) || P v) = true := all4_spec (P := fun v => !decide (IsPerm4 v) || P v) h v
  simp only [Bool.or_eq_true, Bool.not_eq_true', decide_eq_false_iff_not] at h'
  rcases h' with h' | h'
  · exact absurd hv h'
  · exact h'

theorem solved_valid : solved.Valid := by decide

namespace ModelChecked

variable (M : ModelChecked)
include M

/-! ### The model facts, one by one -/

theorem conj_perm8 (v : Arr8) (hv : IsPerm8 v) (σ : Sym) :
    IsPerm8 (conjC σ v) ∧ IsPerm8 (conjE σ v) ∧
      parity8 (conjC σ v) = parity8 v ∧ parity8 (conjE σ v) = parity8 v := by
  have h := M.conjPerm
  simp only [conjPermOK, Bool.and_eq_true] at h
  have h1 := allPerm8_spec h.1 v hv
  simp only [List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq] at h1
  have h2 := h1 σ (mem_allSyms σ)
  exact ⟨h2.1.1.1, h2.1.1.2, h2.1.2, h2.2⟩

theorem conj_perm4 (v : Arr4) (hv : IsPerm4 v) (σ : Sym) :
    IsPerm4 (conjS σ v) ∧ parity4 (conjS σ v) = parity4 v := by
  have h := M.conjPerm
  simp only [conjPermOK, Bool.and_eq_true] at h
  have h1 := allPerm4_spec h.2 v hv
  simp only [List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq] at h1
  exact h1 σ (mem_allSyms σ)

theorem conj_move8 (v : Arr8) (hv : IsPerm8 v) (σ : Sym) (m : Move) :
    conjC σ (permute8 m.srcC v) = permute8 (symMove σ m).srcC (conjC σ v) ∧
    conjE σ (permute8 m.srcE v) = permute8 (symMove σ m).srcE (conjE σ v) := by
  have h := M.conjMove
  simp only [conjMoveOK, Bool.and_eq_true] at h
  have h1 := allPerm8_spec h.1 v hv
  simp only [List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq] at h1
  exact h1 σ (mem_allSyms σ) m (Move.mem_all m)

theorem conj_move4 (v : Arr4) (hv : IsPerm4 v) (σ : Sym) (m : Move) :
    conjS σ (permute4 m.srcS v) = permute4 (symMove σ m).srcS (conjS σ v) := by
  have h := M.conjMove
  simp only [conjMoveOK, Bool.and_eq_true] at h
  have h1 := allPerm4_spec h.2 v hv
  simp only [List.all_eq_true, decide_eq_true_eq] at h1
  exact h1 σ (mem_allSyms σ) m (Move.mem_all m)

theorem conj_mul8 (v : Arr8) (hv : IsPerm8 v) :
    (conjC 0 v = v ∧ conjE 0 v = v) ∧
    ∀ τ σ : Sym, conjC τ (conjC σ v) = conjC (symMul τ σ) v ∧ conjE τ (conjE σ v) = conjE (symMul τ σ) v := by
  have h := M.conjMul
  simp only [conjMulOK, Bool.and_eq_true] at h
  have h1 := allPerm8_spec h.1 v hv
  simp only [List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq] at h1
  exact ⟨h1.1, fun τ σ => h1.2 τ (mem_allSyms τ) σ (mem_allSyms σ)⟩

theorem conj_mul4 (v : Arr4) (hv : IsPerm4 v) :
    conjS 0 v = v ∧ ∀ τ σ : Sym, conjS τ (conjS σ v) = conjS (symMul τ σ) v := by
  have h := M.conjMul
  simp only [conjMulOK, Bool.and_eq_true] at h
  have h1 := allPerm4_spec h.2 v hv
  simp only [List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq] at h1
  exact ⟨h1.1, fun τ σ => h1.2 τ (mem_allSyms τ) σ (mem_allSyms σ)⟩

theorem group_spec (a : Sym) :
    symMul (symInv a) a = 0 ∧ conjC a id8 = id8 ∧ conjE a id8 = id8 ∧ conjS a id4 = id4 ∧
    (∀ b : Sym, symMul (symMul a (symInv b)) b = a) ∧
    (∀ m : Move, symMove a (symMove (symInv a) m) = m) := by
  have h := M.group
  simp only [symGroupOK, List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq] at h
  have h1 := h a (mem_allSyms a)
  exact ⟨h1.1.1.1.1.1, h1.1.1.1.1.2, h1.1.1.1.2, h1.1.1.2, fun b => h1.1.2 b (mem_allSyms b),
    fun m => h1.2 m (Move.mem_all m)⟩

theorem class_spec (c : Arr8) (hc : IsPerm8 c) :
    cclass c < 2768 ∧ conjC (symTo c) c = crep (cclass c) ∧ ∀ σ : Sym, cclass (conjC σ c) = cclass c := by
  have h1 := allPerm8_spec M.cls c hc
  simp only [List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq] at h1
  exact ⟨h1.1.1, h1.1.2, fun σ => h1.2 σ (mem_allSyms σ)⟩

theorem move_spec8 (v : Arr8) (hv : IsPerm8 v) (m : Move) :
    IsPerm8 (permute8 m.srcC v) ∧ IsPerm8 (permute8 m.srcE v) ∧
    parity8 (permute8 m.srcC v) = (parity8 v + m.flipC) % 2 ∧
    parity8 (permute8 m.srcE v) = (parity8 v + m.flipE) % 2 := by
  have h := M.move
  simp only [moveOK, Bool.and_eq_true] at h
  have h1 := allPerm8_spec h.1 v hv
  simp only [List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq] at h1
  have h2 := h1 m (Move.mem_all m)
  exact ⟨h2.1.1.1, h2.1.1.2, h2.1.2, h2.2⟩

theorem move_spec4 (v : Arr4) (hv : IsPerm4 v) (m : Move) :
    IsPerm4 (permute4 m.srcS v) ∧ parity4 (permute4 m.srcS v) = (parity4 v + m.flipS) % 2 := by
  have h := M.move
  simp only [moveOK, Bool.and_eq_true] at h
  have h1 := allPerm4_spec h.2 v hv
  simp only [List.all_eq_true, Bool.and_eq_true, decide_eq_true_eq] at h1
  exact h1 m (Move.mem_all m)

theorem rank_spec (v : Arr8) (hv : IsPerm8 v) : rank8 v < 40320 ∧ unrank8 (rank8 v) = v := by
  have h1 := allPerm8_spec M.rank v hv
  simp only [Bool.and_eq_true, decide_eq_true_eq] at h1
  exact h1

theorem slice_spec (s : Arr4) (hs : IsPerm4 s) : s12 s < 12 ∧ slice (parity4 s) (s12 s) = s := by
  have h1 := allPerm4_spec M.sliceIdx s hs
  simp only [Bool.and_eq_true, decide_eq_true_eq] at h1
  exact h1

/-! ### The same facts for states -/

/-- Legal states stay legal. -/
theorem valid_move (g : State) (hv : g.Valid) (m : Move) : (g.move m).Valid :=
  ⟨(M.move_spec8 g.c hv.1 m).1, (M.move_spec8 g.e hv.2.1 m).2.1, (M.move_spec4 g.s hv.2.2 m).1⟩

theorem solved_parityOK : solved.ParityOK := by
  have h := M.solvedPar
  simp only [solvedParityOK, decide_eq_true_eq] at h
  exact h

theorem conj_valid (g : State) (hv : g.Valid) (σ : Sym) : (g.conj σ).Valid :=
  ⟨(M.conj_perm8 g.c hv.1 σ).1, (M.conj_perm8 g.e hv.2.1 σ).2.1, (M.conj_perm4 g.s hv.2.2 σ).1⟩

theorem conj_parityOK (g : State) (hv : g.Valid) (hp : g.ParityOK) (σ : Sym) : (g.conj σ).ParityOK := by
  unfold State.ParityOK at hp ⊢
  show (parity8 (conjC σ g.c) + parity8 (conjE σ g.e)) % 2 = parity4 (conjS σ g.s)
  rw [(M.conj_perm8 g.c hv.1 σ).2.2.1, (M.conj_perm8 g.e hv.2.1 σ).2.2.2, (M.conj_perm4 g.s hv.2.2 σ).2]
  exact hp

theorem conj_conj (g : State) (hv : g.Valid) (σ τ : Sym) : (g.conj σ).conj τ = g.conj (symMul τ σ) := by
  show State.mk (conjC τ (conjC σ g.c)) (conjE τ (conjE σ g.e)) (conjS τ (conjS σ g.s)) = _
  rw [((M.conj_mul8 g.c hv.1).2 τ σ).1, ((M.conj_mul8 g.e hv.2.1).2 τ σ).2, (M.conj_mul4 g.s hv.2.2).2 τ σ]
  rfl

theorem conj_zero (g : State) (hv : g.Valid) : g.conj 0 = g := by
  show State.mk (conjC 0 g.c) (conjE 0 g.e) (conjS 0 g.s) = g
  rw [(M.conj_mul8 g.c hv.1).1.1, (M.conj_mul8 g.e hv.2.1).1.2, (M.conj_mul4 g.s hv.2.2).1]

theorem conj_solved (a : Sym) : solved.conj a = solved := by
  show State.mk (conjC a id8) (conjE a id8) (conjS a id4) = solved
  rw [(M.group_spec a).2.1, (M.group_spec a).2.2.1, (M.group_spec a).2.2.2.1]
  rfl

/-- Doing a move and then conjugating is conjugating and then doing the corresponding move. -/
theorem conj_move (g : State) (hv : g.Valid) (σ : Sym) (m : Move) :
    (g.move m).conj σ = (g.conj σ).move (symMove σ m) := by
  show State.mk (conjC σ (permute8 m.srcC g.c)) (conjE σ (permute8 m.srcE g.e)) (conjS σ (permute4 m.srcS g.s)) = _
  rw [(M.conj_move8 g.c hv.1 σ m).1, (M.conj_move8 g.e hv.2.1 σ m).2, M.conj_move4 g.s hv.2.2 σ m]
  rfl

/-- Moves keep the parities consistent. -/
theorem parityOK_move (g : State) (hv : g.Valid) (hp : g.ParityOK) (m : Move) : (g.move m).ParityOK := by
  have hc := (M.move_spec8 g.c hv.1 m).2.2.1
  have he := (M.move_spec8 g.e hv.2.1 m).2.2.2
  have hs := (M.move_spec4 g.s hv.2.2 m).2
  unfold State.ParityOK at hp ⊢
  show (parity8 (permute8 m.srcC g.c) + parity8 (permute8 m.srcE g.e)) % 2 = parity4 (permute4 m.srcS g.s)
  rw [hc, he, hs]
  cases m <;> simp [Move.flipC, Move.flipE, Move.flipS, Move.isSide, Move.isHalf] <;> omega

/-- Every state reachable from a legal, parity-consistent state is legal and parity-consistent. -/
theorem good_apply (w : List Move) (g : State) (hv : g.Valid) (hp : g.ParityOK) :
    (g.apply w).Valid ∧ (g.apply w).ParityOK :=
  run_valid State.move (fun g => g.Valid ∧ g.ParityOK)
    (fun s m hs => ⟨M.valid_move s hs.1 m, M.parityOK_move s hs.1 hs.2 m⟩) w g ⟨hv, hp⟩

/-- The corners of `canon g` are the representative of the class of `g`'s corners. -/
theorem canon_c (g : State) (hv : g.Valid) : (canon g).c = crep (cclass g.c) :=
  (M.class_spec g.c hv.1).2.1

/-- A legal, parity-consistent state whose corners are the representative of class `k` is the state stored
at its own index. -/
theorem entryState_eq (g : State) (hv : g.Valid) (hp : g.ParityOK) (k : Nat) (hk : g.c = crep k) :
    entryState k (rank8 g.e) (s12 g.s) = g := by
  have hr := (M.rank_spec g.e hv.2.1).2
  have hs := (M.slice_spec g.s hv.2.2).2
  unfold State.ParityOK at hp
  cases g with
  | mk c e s =>
    simp only at hk hr hs hp
    subst hk
    simp only [entryState, hr, hp, hs]

end ModelChecked

/-! ### What the table check says -/

/-- The statements that `tableOK T nk cap = true` amounts to. -/
structure TableSpec (T : ByteArray) (nk cap : Nat) : Prop where
  /-- value 0 at the solved cube -/
  solved0 : T.get! (ridx solved) = 0
  /-- for every entry with value below `cap`: each move changes the value by at most one; value 0 only at
  the solved cube; from a positive value some move goes down by one -/
  entry : ∀ k, k < nk → ∀ e, e < 40320 → ∀ s, s < 12 → tv T (idx3 k e s) < cap →
    (∀ m : Move, tv T (idx3 k e s) ≤ tv T (ridx ((entryState k e s).move m)) + 1 ∧
                 tv T (ridx ((entryState k e s).move m)) ≤ tv T (idx3 k e s) + 1) ∧
    (tv T (idx3 k e s) = 0 → entryState k e s = solved) ∧
    (tv T (idx3 k e s) ≠ 0 → ∃ m : Move, tv T (ridx ((entryState k e s).move m)) + 1 = tv T (idx3 k e s))
  /-- the table is constant on the images of an entry under the symmetries fixing the corner representative -/
  stab : ∀ k, k < nk → ∀ ρ : Sym, ρ ≠ 0 → conjC ρ (crep k) = crep k → ∀ e, e < 40320 → ∀ s, s < 12 →
    T.get! (idx3 k (rank8 ((entryState k e s).conj ρ).e) (s12 ((entryState k e s).conj ρ).s)) =
      T.get! (idx3 k e s)

theorem entryOK_spec {T : ByteArray} {cap k e s : Nat} {nb : Move → Nat}
    (h : entryOK T cap k e s nb = true) (hc : tv T (idx3 k e s) < cap) :
    (∀ m : Move, tv T (idx3 k e s) ≤ tv T (nb m) + 1 ∧ tv T (nb m) ≤ tv T (idx3 k e s) + 1) ∧
    (tv T (idx3 k e s) = 0 → entryState k e s = solved) ∧
    (tv T (idx3 k e s) ≠ 0 → ∃ m : Move, tv T (nb m) + 1 = tv T (idx3 k e s)) := by
  unfold entryOK at h
  simp only [Bool.or_eq_true, Bool.and_eq_true, decide_eq_true_eq, List.all_eq_true] at h
  rcases h with h | ⟨h1, h2⟩
  · omega
  · refine ⟨fun m => h1 m (Move.mem_all m), ?_, ?_⟩
    · intro h0
      split at h2
      · exact of_decide_eq_true h2
      · contradiction
    · intro hne
      split at h2
      · contradiction
      · simp only [List.any_eq_true, beq_iff_eq] at h2
        obtain ⟨m, _, hm⟩ := h2
        exact ⟨m, hm⟩

/-- The index that the fast check computes for the neighbour of an entry is its reduced index. -/
theorem ridx_entry_move (k e s : Nat) (m : Move) :
    ridx ((entryState k e s).move m) =
      (cclass (permute8 m.srcC (crep k)) * 40320 +
          rank8 (conjE (symTo (permute8 m.srcC (crep k))) (permute8 m.srcE (unrank8 e)))) * 12 +
        s12 (conjS (symTo (permute8 m.srcC (crep k)))
          (permute4 m.srcS (slice ((parity8 (crep k) + parity8 (unrank8 e)) % 2) s))) := by
  simp only [ridx, canon, State.conj, State.move, entryState, idx3]

theorem checkRow_spec {T : ByteArray} {cap k : Nat} (h : checkRow T cap (emTable ()) (peTable ()) k = true)
    (e : Nat) (he : e < 40320) (s : Nat) (hs : s < 12) :
    entryOK T cap k e s (fun m => ridx ((entryState k e s).move m)) = true := by
  simp only [checkRow] at h
  have h1 := nat_all_spec _ _ (nat_all_spec _ _ h e he) s hs
  simp only [peTable, memoGet_memo, emGet_eq, rowK, rowS, rowSm, emF, peF, ofIdx_idx, symOfNat_idx] at h1
  simp only [ridx_entry_move]
  exact h1

theorem stabRow_spec {T : ByteArray} {k : Nat} (h : stabRow T allSyms (esTable ()) (peTable ()) k = true)
    (ρ : Sym) (hρ : ρ ≠ 0) (hfix : conjC ρ (crep k) = crep k) (e : Nat) (he : e < 40320) (s : Nat)
    (hs : s < 12) :
    T.get! (idx3 k (rank8 ((entryState k e s).conj ρ).e) (s12 ((entryState k e s).conj ρ).s)) =
      T.get! (idx3 k e s) := by
  simp only [stabRow, List.all_eq_true, Bool.or_eq_true, decide_eq_true_eq, Bool.not_eq_true',
    decide_eq_false_iff_not] at h
  rcases h ρ (mem_allSyms ρ) with (h1 | h1) | h1
  · exact absurd h1 hρ
  · exact absurd hfix h1
  · have h2 := nat_all_spec _ _ (nat_all_spec _ _ h1 e he) s hs
    simp only [peTable, memoGet_memo, esGet_eq, esF, ssF, peF, symOfNat_val, beq_iff_eq] at h2
    exact h2

theorem tableOK_spec {T : ByteArray} {nk cap : Nat} (h : tableOK T nk cap = true) : TableSpec T nk cap := by
  simp only [tableOK, tableOKWith, Bool.and_eq_true, decide_eq_true_eq] at h
  refine ⟨h.1, ?_, ?_⟩
  · intro k hk e he s hs hc
    have hr := nat_all_spec _ _ h.2 k hk
    simp only [Bool.and_eq_true] at hr
    exact entryOK_spec (checkRow_spec hr.1 e he s hs) hc
  · intro k hk ρ hρ hfix e he s hs
    have hr := nat_all_spec _ _ h.2 k hk
    simp only [Bool.and_eq_true] at hr
    exact stabRow_spec hr.2 ρ hρ hfix e he s hs

/-! ### The step lemma and the theorems, for any table that passes the check -/

section Main

variable {T : ByteArray} {cap : Nat} (M : ModelChecked) (S : TableSpec T 2768 cap)
include M S

/-- A state whose corners are the representative of class `k`, and its image under a symmetry fixing that
representative, have the same table value. -/
theorem stab_inv (g0 : State) (hv : g0.Valid) (hp : g0.ParityOK) (k : Nat) (hk : k < 2768) (hc : g0.c = crep k)
    (ρ : Sym) (hfix : conjC ρ (crep k) = crep k) :
    T.get! (idx3 k (rank8 (g0.conj ρ).e) (s12 (g0.conj ρ).s)) = T.get! (idx3 k (rank8 g0.e) (s12 g0.s)) := by
  by_cases hρ : ρ = 0
  · subst hρ
    rw [M.conj_zero g0 hv]
  · have h := S.stab k hk ρ hρ hfix (rank8 g0.e) (M.rank_spec g0.e hv.2.1).1 (s12 g0.s)
      (M.slice_spec g0.s hv.2.2).1
    rw [M.entryState_eq g0 hv hp k hc] at h
    exact h

/-- **Conjugate states have the same table value.** -/
theorem get_ridx_conj (h : State) (hv : h.Valid) (hp : h.ParityOK) (θ : Sym) :
    T.get! (ridx (h.conj θ)) = T.get! (ridx h) := by
  have hvθ := M.conj_valid h hv θ
  have hg0v : (canon h).Valid := M.conj_valid h hv _
  have hg0p : (canon h).ParityOK := M.conj_parityOK h hv hp _
  have hk : cclass h.c < 2768 := (M.class_spec h.c hv.1).1
  have hcls : cclass (h.conj θ).c = cclass h.c := (M.class_spec h.c hv.1).2.2 θ
  have hcan : canon (h.conj θ) =
      (canon h).conj (symMul (symMul (symTo (h.conj θ).c) θ) (symInv (symTo h.c))) := by
    show (h.conj θ).conj (symTo (h.conj θ).c) = (h.conj (symTo h.c)).conj _
    rw [M.conj_conj h hv, M.conj_conj h hv, (M.group_spec (symMul (symTo (h.conj θ).c) θ)).2.2.2.2.1]
  have hfix : conjC (symMul (symMul (symTo (h.conj θ).c) θ) (symInv (symTo h.c))) (crep (cclass h.c)) =
      crep (cclass h.c) := by
    have h1 : (canon (h.conj θ)).c = crep (cclass (h.conj θ).c) := M.canon_c _ hvθ
    rw [hcan, hcls] at h1
    have h2 : (canon h).c = crep (cclass h.c) := M.canon_c h hv
    have h3 : ∀ ρ : Sym, ((canon h).conj ρ).c = conjC ρ (canon h).c := fun _ => rfl
    rw [h3, h2] at h1
    exact h1
  unfold ridx
  rw [hcan, hcls]
  exact stab_inv M S (canon h) hg0v hg0p _ hk (M.canon_c h hv) _ hfix

theorem tv_ridx_conj (h : State) (hv : h.Valid) (hp : h.ParityOK) (θ : Sym) :
    tv T (ridx (h.conj θ)) = tv T (ridx h) := by
  unfold tv
  rw [get_ridx_conj M S h hv hp θ]

/-- What the table check says about the entry of an arbitrary state `g`, read at `canon g`. -/
theorem entry_canon (g : State) (hv : g.Valid) (hp : g.ParityOK) (hc : tv T (ridx g) < cap) :
    (∀ m : Move, tv T (ridx g) ≤ tv T (ridx ((canon g).move m)) + 1 ∧
                 tv T (ridx ((canon g).move m)) ≤ tv T (ridx g) + 1) ∧
    (tv T (ridx g) = 0 → canon g = solved) ∧
    (tv T (ridx g) ≠ 0 → ∃ m : Move, tv T (ridx ((canon g).move m)) + 1 = tv T (ridx g)) := by
  have hk := (M.class_spec g.c hv.1).1
  have hg0v : (canon g).Valid := M.conj_valid g hv _
  have hg0p : (canon g).ParityOK := M.conj_parityOK g hv hp _
  have hE := M.entryState_eq (canon g) hg0v hg0p _ (M.canon_c g hv)
  have hS := S.entry _ hk _ (M.rank_spec (canon g).e hg0v.2.1).1 _ (M.slice_spec (canon g).s hg0v.2.2).1 hc
  rw [hE] at hS
  exact hS

/-- **Step lemma.**  One move changes the table value by at most one. -/
theorem step_spec (g : State) (hv : g.Valid) (hp : g.ParityOK) (m : Move) (hc : tv T (ridx g) < cap) :
    tv T (ridx g) ≤ tv T (ridx (g.move m)) + 1 ∧ tv T (ridx (g.move m)) ≤ tv T (ridx g) + 1 := by
  have h := (entry_canon M S g hv hp hc).1 (symMove (symTo g.c) m)
  have hmv : (canon g).move (symMove (symTo g.c) m) = (g.move m).conj (symTo g.c) :=
    (M.conj_move g hv _ m).symm
  rw [hmv, tv_ridx_conj M S (g.move m) (M.valid_move g hv m) (M.parityOK_move g hv hp m)] at h
  exact h

/-- From a positive value some move goes down by one. -/
theorem down_spec (g : State) (hv : g.Valid) (hp : g.ParityOK) (hc : tv T (ridx g) < cap)
    (hne : tv T (ridx g) ≠ 0) : ∃ m : Move, tv T (ridx (g.move m)) + 1 = tv T (ridx g) := by
  obtain ⟨m', hm'⟩ := (entry_canon M S g hv hp hc).2.2 hne
  refine ⟨symMove (symInv (symTo g.c)) m', ?_⟩
  have hmv := M.conj_move g hv (symTo g.c) (symMove (symInv (symTo g.c)) m')
  rw [(M.group_spec (symTo g.c)).2.2.2.2.2 m'] at hmv
  have hmv' : (canon g).move m' = (g.move (symMove (symInv (symTo g.c)) m')).conj (symTo g.c) := hmv.symm
  rw [hmv', tv_ridx_conj M S _ (M.valid_move g hv _) (M.parityOK_move g hv hp _)] at hm'
  exact hm'

/-- Value 0 only at the solved cube. -/
theorem zero_spec (g : State) (hv : g.Valid) (hp : g.ParityOK) (hc : tv T (ridx g) < cap)
    (h0 : tv T (ridx g) = 0) : g = solved := by
  have h1 : g.conj (symTo g.c) = solved := (entry_canon M S g hv hp hc).2.1 h0
  have h2 : (g.conj (symTo g.c)).conj (symInv (symTo g.c)) = g := by
    rw [M.conj_conj g hv, (M.group_spec (symTo g.c)).1, M.conj_zero g hv]
  rw [h1] at h2
  rw [← h2]
  exact M.conj_solved _

/-- **Upper bound.**  A state with table value `d` (below `cap`) is solved by some `d` moves. -/
theorem attained_of : ∀ (d : Nat) (g : State), g.Valid → g.ParityOK → tv T (ridx g) = d → d < cap →
    ∃ w : List Move, w.length = d ∧ g.apply w = solved
  | 0, g, hv, hp, hd, hc => ⟨[], rfl, zero_spec M S g hv hp (by omega) hd⟩
  | d + 1, g, hv, hp, hd, hc => by
      obtain ⟨m, hm⟩ := down_spec M S g hv hp (by omega) (by omega)
      obtain ⟨w, hw, hs⟩ := attained_of d (g.move m) (M.valid_move g hv m) (M.parityOK_move g hv hp m)
        (by omega) (by omega)
      exact ⟨m :: w, by simp [hw], hs⟩

end Main

theorem tv_lt (T : ByteArray) (i : Nat) : tv T i < 256 := UInt8.toNat_lt _

/-- **Lower bound.**  If the whole table passes the check, every solution of `g` has at least as many moves
as the table value of `g`. -/
theorem lower_of {T : ByteArray} (M : ModelChecked) (S : TableSpec T 2768 256) (g : State) (hv : g.Valid)
    (hp : g.ParityOK) (w : List Move) (hw : g.apply w = solved) : tv T (ridx g) ≤ w.length :=
  solution_length_ge State.move (fun g => g.Valid ∧ g.ParityOK)
    (fun s m hs => ⟨M.valid_move s hs.1 m, M.parityOK_move s hs.1 hs.2 m⟩)
    ridx (tv T) solved
    (fun s m hs => (step_spec M S s hs.1 hs.2 m (tv_lt T _)).1)
    (by show (T.get! (ridx solved)).toNat = 0; rw [S.solved0]; rfl)
    g ⟨hv, hp⟩ w hw

/-! ### Search, check and count in one go (the table is built once) -/

/-- Build the table with `depth` rounds of search; check rows `0 … nk-1` for the entries below `cap`; check
that no entry exceeds `maxv`; compare the weighted numbers of entries with values `0, 1, …, n-1` and `≥ n`
with `counts`; and compare the table values of the listed scrambles with the listed numbers. -/
def exactCheck (depth nk cap maxv n : Nat) (counts : List Nat) (samples : List (List Move × Nat)) : Bool :=
  let T := mkTable depth
  tableOK T nk cap && maxOK T nk maxv && decide (depthCounts T nk n = counts) && samplesOK T samples

theorem exactCheck_spec {depth nk cap maxv n : Nat} {counts : List Nat} {samples : List (List Move × Nat)}
    (h : exactCheck depth nk cap maxv n counts samples = true) :
    TableSpec (mkTable depth) nk cap ∧
    (∀ k, k < nk → ∀ e, e < 40320 → ∀ s, s < 12 → tv (mkTable depth) (idx3 k e s) ≤ maxv) ∧
    depthCounts (mkTable depth) nk n = counts ∧
    (∀ c ∈ samples, tv (mkTable depth) (ridx (solved.apply c.1)) = c.2) := by
  simp only [exactCheck, Bool.and_eq_true, decide_eq_true_eq] at h
  refine ⟨tableOK_spec h.1.1.1, ?_, h.1.2, ?_⟩
  · intro k hk e he s hs
    have h1 := nat_all_spec _ _ (nat_all_spec _ _ (nat_all_spec _ _ h.1.1.2 k hk) e he) s hs
    exact of_decide_eq_true h1
  · intro c hc
    have h2 := h.2
    simp only [samplesOK, List.all_eq_true, beq_iff_eq] at h2
    exact h2 c hc

/-- If no entry exceeds `maxv`, no state has a table value above `maxv`. -/
theorem tv_le_of_max {T : ByteArray} {maxv : Nat} (M : ModelChecked)
    (hmax : ∀ k, k < 2768 → ∀ e, e < 40320 → ∀ s, s < 12 → tv T (idx3 k e s) ≤ maxv)
    (g : State) (hv : g.Valid) : tv T (ridx g) ≤ maxv :=
  hmax _ (M.class_spec g.c hv.1).1 _ (M.rank_spec (canon g).e (M.conj_valid g hv _).2.1).1 _
    (M.slice_spec (canon g).s (M.conj_valid g hv _).2.2).1

/-- Table values of several states at once (the table is built once, which takes minutes); for `#eval`. -/
def tableValues (depth : Nat) (gs : List State) : List Nat :=
  let T := mkTable depth
  gs.map fun g => tv T (ridx g)

end Exact
end DRBound
