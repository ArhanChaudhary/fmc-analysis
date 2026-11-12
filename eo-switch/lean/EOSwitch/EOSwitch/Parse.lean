/-
  EOSwitch.Parse — reads the research's files of `Study.lean`, and checks printed decimals against exact fractions.
  A tab-separated file is split into lines and each line into fields; comment lines (#), the header line and empty
  lines are dropped.  A Markdown table (from SUMMARY.md) is read from its rows that start with "|", without its
  header row and the row of dashes under it; each cell is trimmed, and thousands separators (",") are dropped.
-/
import EOSwitch.Study
import EOSwitch.Switch

namespace EOSwitch
namespace parse

/-- The data lines of a tab-separated file with a header line, each as its list of fields. -/
def table (txt : String) : List (List String) :=
  ((txt.splitOn "\n").drop 1 |>.filter (· != "")).map (·.splitOn "\t")

/-- The rows of the Markdown table in `txt` (after its header and dash rows), each as its list of cells. -/
def mdTable (txt : String) : List (List String) :=
  (((txt.splitOn "\n").filter (·.startsWith "|")).drop 2).map fun l =>
    ((((l.splitOn "|").drop 1).dropLast).map fun c => (c.trimAscii.toString.replace "," ""))

/-- "0.043" ↦ (43, 3): the digits as a whole number and the number of digits after the point. -/
def decimal (s : String) : Nat × Nat :=
  match s.splitOn "." with
  | [a, f] => (a.toNat! * 10 ^ f.length + f.toNat!, f.length)
  | _ => (s.toNat!, 0)

/-- The printed decimal s is num/den rounded to its number of digits: |num/den − s| ≤ half a unit of its last
digit, i.e. 2·|num·10^p − v·den| ≤ den. -/
def roundsTo (num den : Nat) (s : String) : Bool :=
  let (v, p) := decimal s
  let a := num * 10 ^ p
  let b := v * den
  den > 0 && (if a ≥ b then a - b else b - a) * 2 ≤ den

/-- "4c4e" ↦ (4, 4). -/
def drmName (s : String) : Nat × Nat :=
  match (s.dropEnd 1).toString.splitOn "c" with
  | [c, e] => (c.toNat!, e.toNat!)
  | _ => (99, 99)

/-- dist_hist.txt: (distance, states), comment lines dropped. -/
def distHist : List (Nat × Nat) :=
  ((study.DIST_HIST_TXT.splitOn "\n").filter fun l => l != "" && !l.startsWith "#").map fun l =>
    match l.splitOn "\t" with
    | [a, b] => (a.toNat!, b.toNat!)
    | _ => (999, 0)

open sw

/-- The histogram of the DRM named `name` ("4c4e"), or of all states ("all"). -/
def histOf (rs : Rows) (name : String) : List Nat :=
  if name == "all" then total rs else total (drm rs (drmName name).1 (drmName name).2)

/-- [states, ≤ 5, ≤ 6, ≤ 7, Σ distance] of a histogram. -/
def stats (h : List Nat) : List Nat := [h.sum, le h 5, le h 6, le h 7, weighted h]

/-- One row of variants_by_drm.tsv (drm, cosets, share, mean_d, plain_le5, plain_le6, plain_le7, …) agrees with
Lean's histogram of that DRM: same number of states, and share, mean and the three "plain" shares are the exact
values rounded to the printed digits. -/
def variantRowOk (rs : Rows) (r : List String) : Bool :=
  let h := histOf rs r[0]!
  let n := h.sum
  r.length ≥ 7 && n == r[1]!.toNat! && roundsTo n 1082565 r[2]! && roundsTo (weighted h) n r[3]! &&
    roundsTo (le h 5) n r[4]! && roundsTo (le h 6) n r[5]! && roundsTo (le h 7) n r[6]!

/-- Every row of variants_by_drm.tsv agrees (the DRM rows and the row "all"), and the DRM rows cover every
state. -/
def variantsOk (rs : Rows) : Bool :=
  let t := table study.VARIANTS_BY_DRM_TSV
  (t.all (variantRowOk rs)) && ((t.filter (·[0]! != "all")).map fun r => (histOf rs r[0]!).sum).sum == 1082565

/-- The table of SUMMARY section 1 (DRM, states, mean, plain, …, plain ≤ 5, plain ≤ 7): for each row, the states,
the mean and the plain (≤ 6), ≤ 5 and ≤ 7 shares agree with Lean's histogram ("all" = every state).  The mean is
not checked for the DRMs in `skipMean`. -/
def plainOk (rs : Rows) (skipMean : List String) : Bool :=
  (mdTable study.SUM_PLAIN).all fun r =>
    let h := histOf rs r[0]!
    let n := h.sum
    r.length == 10 && n == r[1]!.toNat! && (skipMean.contains r[0]! || roundsTo (weighted h) n r[2]!) &&
      roundsTo (le h 6) n r[3]! && roundsTo (le h 5) n r[8]! && roundsTo (le h 7) n r[9]!

/-- The printed mean of one DRM's row in that table. -/
def plainMean (name : String) : String :=
  (((mdTable study.SUM_PLAIN).find? (·[0]! == name)).map (·[2]!)).getD ""

/-- A feature table of SUMMARY section 4 with k key columns, for DRM xcye: its rows are, in order, exactly the cells
of `split` (same key values), with the same number of states, and its "share" (of the DRM) and "p<=6 P1" columns
are Lean's exact values rounded to the printed digits. -/
def featTableOk (rs : Rows) (txt : String) (c e k : Nat) (key : Cell → List Nat) : Bool :=
  let t := mdTable txt
  let s := split rs c e key
  let n := (total (drm rs c e)).sum
  t.length == s.length && (List.zip t s).all fun (r, (kv, v)) =>
    (r.take k).map String.toNat! == kv && r[k]!.toNat! == v[0]! && roundsTo v[0]! n r[k + 1]! &&
      roundsTo v[2]! v[0]! r[k + 2]!

end parse
end EOSwitch
