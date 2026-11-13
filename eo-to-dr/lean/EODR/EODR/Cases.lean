/-
  EODR.Cases — readings of the per-case EO → DR table for the figures the page prints, the page's case tables, the
  superflip, and the arithmetic of nissy's scrambler and of the binomials quoted on the page.  The theorems are in
  `CaseTheorems.lean`; this file only defines things (so they are compiled before those theorems run them).

  `BYCASE` is Lean's own per-case table: `(eodr.run eodr.N).byCase`, the tally of the checked BFS of `Eodr.lean`
  (rows (corners, edges, option, [states at distance 0, …, 11]), options "eo", "eo_switchF", "eo_switchB").

  Printed figures are checked with `rounds num den v p`: the printed number with p digits after the point, read as
  the whole number v, is num/den rounded to p digits, i.e. |num/den − v/10^p| ≤ half a unit of the last digit
  (2·|num·10^p − v·den| ≤ den).  A percentage x% is (100·num)/den; "1 in x" is den/num.
-/
import EODR.Eodr
import EODR.Eo
import EODR.Study

set_option compiler.extract_closed false

namespace EODR
namespace cases
open pieces

/-- Lean's per-case table (computed once per Lean process). -/
def BYCASE : List (Nat × Nat × String × List Nat) := (eodr.run eodr.N).byCase

/-- The histogram of case `c`c`e`e under option `o` ("eo", "eo_switchF", "eo_switchB"). -/
def hist (c e : Nat) (o : String) : List Nat := eodr.caseRow BYCASE c e o
/-- States at distance ≤ k. -/
def le (h : List Nat) (k : Nat) : Nat := (h.take (k + 1)).sum
/-- [states, ≤ 4, ≤ 5, ≤ 6, ≤ 7, Σ distance] of one case and option. -/
def stats (c e : Nat) (o : String) : List Nat :=
  let h := hist c e o
  [h.sum, le h 4, le h 5, le h 6, le h 7, eodr.weighted h]

/-! ### Rounding -/

/-- num/den rounded to p digits after the point is v/10^p (half a unit of the last digit either way). -/
def rounds (num den v p : Nat) : Bool :=
  let a := num * 10 ^ p
  let b := v * den
  den > 0 && (if a ≥ b then a - b else b - a) * 2 ≤ den

/-- "0.043" ↦ (43, 3): the digits as a whole number, and how many follow the point. -/
def decimal (s : String) : Nat × Nat :=
  match s.splitOn "." with
  | [a, f] => (a.toNat! * 10 ^ f.length + f.toNat!, f.length)
  | _ => (s.toNat!, 0)

/-- The printed decimal s is num/den rounded to its digits.  Only digits and one point are accepted. -/
def roundsTo (num den : Nat) (s : String) : Bool :=
  s != "" && (s.toList.all fun ch => ch.isDigit || ch == '.') && (s.splitOn ".").length ≤ 2 &&
    let (v, p) := decimal s
    rounds num den v p

/-- A printed percentage ("12.7%") is num/den; "0%" is printed only for exactly 0 (the page's `pc`). -/
def pctOk (num den : Nat) (s : String) : Bool :=
  if s == "0%" then num == 0 && den > 0
  else s.endsWith "%" && roundsTo (100 * num) den (s.dropEnd 1).toString

/-- Printed odds "1 in x" are den/num. -/
def oddsOk (num den : Nat) (s : String) : Bool :=
  s.startsWith "1 in " && num > 0 && roundsTo den num (s.drop 5).toString

/-! ### The page's case tables -/

/-- The rows of a Markdown table (after its header and dash rows), each as its list of trimmed cells, with the
thousands separators (",") dropped. -/
def mdTable (txt : String) : List (List String) :=
  (((txt.splitOn "\n").filter (·.startsWith "|")).drop 2).map fun l =>
    ((((l.splitOn "|").drop 1).dropLast).map fun c => (c.trimAscii.toString.replace "," ""))

/-- "4c6e" ↦ (4, 6) (and (99, 99) for anything else). -/
def caseName (s : String) : Nat × Nat :=
  match (s.dropEnd 1).toString.splitOn "c" with
  | [c, e] => if s.endsWith "e" && c != "" && e != "" then (c.toNat!, e.toNat!) else (99, 99)
  | _ => (99, 99)

/-- What a column of a case table shows: 0 share of the 1,082,565 states (%), 1 odds of the case ("1 in x"),
2 mean turns with one axis (EO kept), 3 mean turns with the last EO turn either way, 4 DR in ≤ 6 with one axis (%),
5 DR in ≤ 6 with the last EO turn either way (%). -/
def cellOk (kind c e : Nat) (s : String) : Bool :=
  let h := hist c e "eo"
  let hs := hist c e "eo_switchF"
  let n := h.sum
  match kind with
  | 0 => pctOk n 1082565 s
  | 1 => oddsOk n 1082565 s
  | 2 => roundsTo (eodr.weighted h) n s
  | 3 => roundsTo (eodr.weighted hs) n s
  | 4 => pctOk (le h 6) n s
  | 5 => pctOk (le hs 6) n s
  | _ => false

/-- A case table has `nrows` rows, and each names a case that occurs. -/
def rowsOk (txt : String) (nrows : Nat) : Bool :=
  let t := mdTable txt
  t.length == nrows && t.all fun r => let (c, e) := caseName r[0]!; (hist c e "eo").sum > 0

/-- The cells of a case table, in the listed columns (index, kind), that are not Lean's exact value rounded as
printed: (case, column, printed text).  Empty = every cell agrees. -/
def badCells (txt : String) (cols : List (Nat × Nat)) : List (String × Nat × String) :=
  (mdTable txt).flatMap fun r =>
    let (c, e) := caseName r[0]!
    (cols.filter fun (i, k) => !(i < r.length && cellOk k c e r[i]!)).map fun (i, _) => (r[0]!, i, r[i]!)

/-! ### The superflip -/

/-- The superflip as the page prints it (BUGS item 2). -/
def SF : String := "U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2"

/-! ### Arithmetic -/

def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

/-- n choose k, as n! / (k! (n − k)!). -/
def choose (n k : Nat) : Nat := fact n / (fact k * fact (n - k))

/-- P(at most k successes in n independent trials with chance a/b), times b^n: Σ_{i ≤ k} C(n,i) aⁱ (b − a)ⁿ⁻ⁱ. -/
def binomLe (k n a b : Nat) : Nat :=
  ((List.range (k + 1)).map fun i => choose n i * a ^ i * (b - a) ^ (n - i)).sum

end cases
end EODR
