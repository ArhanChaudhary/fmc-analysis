/-
  AttemptSim.Sample — the checker for simulated attempts: replay of solutions, HTM, and the time ledger.

  Input: the simulator's own log file (data/lean_sample.jsonl, written by `attemptsim run --log`), one attempt per line:

    {"policy":"…","scr":N,"scramble":"…","seed":N,"budget_ms":N,"len":N,"solution":"…","t_end_ms":N,
     "steps":[[kind,ms],…],"sols":[[clock_ms,length,"moves"],…],"banks":[[clock_ms,length],…]}

  steps   every state the solver examined, in order, with its cost in milliseconds; kinds 0 … 10 =
          look, eo_scan, eo_write, eo_eval, rzp, switch, dr_find, dr_read, htr, tail, write
  sols    every full solution found: the clock when its finish was written out (the end of a `tail` step), its
          length, its moves
  banks   every time a solution was written down: the clock when the writing ended (the end of a `write` step)
          and the length written
  len     the result: 0 = DNF;   solution: its moves

  What `attemptOk` checks for one attempt (the theorems say it holds for every line of the file):

   replay      the scramble and every move sequence are made of the 18 face turns; every solution in `sols` and the
               result, appended to the scramble, do nothing (`perm.solvedB`); each is in HTM form (`cancel` leaves
               it unchanged) and has the stated length
   ledger      the costs of the steps add up to `t_end_ms`; the k-th solution's clock is the sum of the costs up to
               and including the k-th `tail` step, the k-th bank's clock the sum up to and including the k-th
               `write` step, and there are as many of each; the first step is the one `look`
   the hour    every step other than `dr_find` and `tail` (the second half of an examination already begun) starts
               before `budget_ms`
   the result  each bank writes the shortest solution found before its writing started; `len` is the length of the
               last bank that ended at or before `budget_ms` (0 if there is none), and `solution` is the first
               solution of that length found before that bank started (empty for a DNF)
-/
import AttemptSim.Perm
import AttemptSim.Cubie
-- the manifest carries the sha256 of the embedded files: importing it makes Lake rebuild this module when they change
-- (Lake does not track `include_str` files itself)
import AttemptSim.SampleManifest

namespace AttemptSim
namespace sample
open cube perm

/-- A move sequence as text -> moves; `none` if a word is not one of the 18 turn names. -/
def parseMoves (txt : String) : Option (List Mv) :=
  (cube.parse txt).mapM fun t =>
    let i := NAMES.idxOf t
    if h : i < 18 then some (⟨i, h⟩ : Mv) else none

def after (s key : String) : String := (s.splitOn key).getD 1 ""
def between (s a b : String) : String := ((after s a).splitOn b).headD ""
def strField (line key : String) : String := between line ("\"" ++ key ++ "\":\"") "\""
def numField (line key : String) : Nat := (cubie.nats (between line ("\"" ++ key ++ "\":") ",")).getD 0 0

structure Attempt where
  policy : String
  scramble : Option (List Mv)
  budget : Nat
  len : Nat
  solution : Option (List Mv)
  tEnd : Nat
  /-- (kind, cost) -/
  steps : Array (Nat × Nat)
  /-- (clock, length, moves) -/
  sols : Array (Nat × Nat × Option (List Mv))
  /-- (clock, length) -/
  banks : Array (Nat × Nat)

def pairs (a : Array Nat) : Array (Nat × Nat) := (Array.range (a.size / 2)).map fun i => (a[2 * i]!, a[2 * i + 1]!)

def parseLine (line : String) : Attempt :=
  let solsTxt := between line "\"sols\":[" "],\"banks\":["
  let sols := (if solsTxt == "" then [] else solsTxt.splitOn "],[").map fun e =>
    let parts := e.splitOn ","
    let n := cubie.nats ((parts.getD 0 "") ++ " " ++ (parts.getD 1 ""))
    (n.getD 0 0, n.getD 1 0, parseMoves (((parts.getD 2 "").replace "\"" "").replace "]" ""))
  { policy := strField line "policy"
    scramble := parseMoves (strField line "scramble")
    budget := numField line "budget_ms"
    len := numField line "len"
    solution := parseMoves (strField line "solution")
    tEnd := numField line "t_end_ms"
    steps := pairs (cubie.nats (between line "\"steps\":[" "],\"sols\":["))
    sols := sols.toArray
    banks := pairs (cubie.nats (after line "\"banks\":[")) }

/-- X solves the scramble S, is in HTM form, and has n moves. -/
def solves (S X : List Mv) (n : Nat) : Bool := solvedB (S ++ X) && cancel X == X && X.length == n

/-- Running totals of the step costs: `clock[i]` = the time when step i ends. -/
def clocks (steps : Array (Nat × Nat)) : Array Nat := Id.run do
  let mut out := #[]
  let mut t := 0
  for (_, ms) in steps do
    t := t + ms
    out := out.push t
  return out

def attemptOk (a : Attempt) : Bool := Id.run do
  let some S := a.scramble | return false
  let some X := a.solution | return false
  let ck := clocks a.steps
  let n := a.steps.size
  -- ledger
  if ck.getD (n - 1) 0 != a.tEnd || n == 0 then return false
  if !(a.steps.all fun (k, _) => k < 11) then return false
  if (a.steps[0]!).1 != 0 || (a.steps.toList.filter fun (k, _) => k == 0).length != 1 then return false
  let tailEnds := (List.range n).filter (fun i => (a.steps[i]!).1 == 9) |>.map (ck[·]!)
  let writeIdx := (List.range n).filter (fun i => (a.steps[i]!).1 == 10)
  if tailEnds != a.sols.toList.map (·.1) then return false
  if writeIdx.map (ck[·]!) != a.banks.toList.map (·.1) then return false
  -- the hour
  for i in [0:n] do
    let k := (a.steps[i]!).1
    let start := if i == 0 then 0 else ck[i - 1]!
    if k != 6 && k != 9 && start ≥ a.budget then return false
  -- replay of every solution found
  for (_, len, mv) in a.sols do
    let some Y := mv | return false
    if !solves S Y len then return false
  -- each bank writes the shortest solution found before it started
  let mut result := 0
  let mut resultMoves : List Mv := []
  for j in [0:a.banks.size] do
    let (endT, len) := a.banks[j]!
    let i := writeIdx[j]!
    let start := if i == 0 then 0 else ck[i - 1]!
    let found := a.sols.toList.filter fun (t, _, _) => t ≤ start
    if found.isEmpty then return false
    let best := (found.map (·.2.1)).foldl min 1000
    if len != best then return false
    if endT ≤ a.budget then
      result := len
      resultMoves := ((found.find? fun (_, l, _) => l == best).bind (·.2.2)).getD []
  -- the result
  if a.len != result then return false
  if X != resultMoves then return false
  if a.len == 0 then return X.isEmpty
  return solves S X a.len

/-! ### The two facts the write-up states about every sampled attempt, as plain definitions

  `logTotal a`       the sum of the costs of every step in the log
  `writeStart a j`   the clock when the j-th writing began: the sum of the costs of the steps before the j-th `write`
  `bestBy a t`       the shortest length among the solutions whose finish was written out by clock t (none if none)
  `lastInTime a`     the last writing that ended inside the hour (none if none) -/

def logTotal (a : Attempt) : Nat := (a.steps.toList.map (·.2)).foldl (· + ·) 0

def writeStart (a : Attempt) (j : Nat) : Nat :=
  let idx := (List.range a.steps.size).filter fun i => (a.steps[i]!).1 == 10
  (((a.steps.toList.take (idx.getD j 0)).map (·.2)).foldl (· + ·) 0)

def bestBy (a : Attempt) (t : Nat) : Option Nat :=
  ((a.sols.toList.filter fun (c, _, _) => c ≤ t).map (·.2.1)).min?

def lastInTime (a : Attempt) : Option Nat :=
  ((List.range a.banks.size).filter fun j => (a.banks[j]!).1 ≤ a.budget).getLast?

/-- A solution shorter than the result (any solution, for a DNF) was found after the last in-time writing began:
found too late to be written down. -/
def lateBetter (a : Attempt) : Bool :=
  let start : Int := match lastInTime a with
    | some j => (writeStart a j : Int)
    | none => -1
  let res := if a.len == 0 then 1000000 else a.len
  a.sols.toList.any fun (c, l, _) => (c : Int) > start && l < res

def SAMPLE : String := include_str "../data/lean_sample.jsonl"
def ATTEMPTS : Array Attempt := ((cubie.lines SAMPLE).map parseLine).toArray

/-- Per policy, in order of name: (name, attempts, DNFs, sum of the lengths, solutions found). -/
def tally (as : Array Attempt) : List (String × Nat × Nat × Nat × Nat) :=
  let names := (as.toList.map (·.policy)).eraseDups.mergeSort (fun a b => decide (a ≤ b))
  names.map fun p =>
    let l := as.toList.filter (·.policy == p)
    (p, l.length, (l.filter (·.len == 0)).length, (l.map (·.len)).foldl (· + ·) 0, (l.map (·.sols.size)).foldl (· + ·) 0)

/-! ### Solutions printed on the page: scramble TAB solution TAB length per line -/

def PAGE : String := include_str "../data/lean_page_solutions.tsv"
def pageRows : List (Option (List Mv) × Option (List Mv) × Nat) :=
  (cubie.lines PAGE).map fun l =>
    let p := l.splitOn "\t"
    (parseMoves (p.getD 0 ""), parseMoves (p.getD 1 ""), (cubie.nats (p.getD 2 "")).getD 0 0)
def pageOk : Bool :=
  pageRows.all fun (s, x, n) =>
    match s, x with
    | some S, some X => solves S X n
    | _, _ => false

end sample
end AttemptSim
