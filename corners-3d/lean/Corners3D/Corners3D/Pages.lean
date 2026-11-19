/-
  Corners3D.Pages — every scramble the study's pages print, checked on the sticker model (written by
  research/src/lean_witness.py; do not edit by hand).  An example is (scramble, kinds, turns to HTR, quarter
  turns, types floor, types + parity floor, the solution the page prints); `ok` is `witness.check`: the kinds
  are the ones the state shows, the four numbers are the tables', and the solution has exactly that many
  turns and ends in HTR.
-/
import Corners3D.Witness
namespace Corners3D
namespace pages
open witness cube corners

abbrev Example := String × String × Nat × Nat × Nat × Nat × String

def ok (e : Example) : Bool := check e.1 e.2.1 e.2.2.1 e.2.2.2.1 e.2.2.2.2.1 e.2.2.2.2.2.1 e.2.2.2.2.2.2

/-- The count table of section 6.3: for each row, the scramble that meets the move floor. -/
def COUNT_TABLE : List Example := [
  ("", "0000000", 0, 0, 0, 0, ""),
  ("F R2 F' R2 F'", "0005005", 5, 3, 5, 5, "F R2 F R2 F"),
  ("R' F' U F", "0044503", 4, 4, 4, 4, "F' U' F R"),
  ("U F' R' F R U'", "0045540", 6, 4, 6, 6, "U R' F' R F U"),
  ("R' U R2 F2 R'", "0453435", 5, 3, 5, 5, "R F2 R2 U' R"),
  ("F' U2 R' F' R", "3445550", 5, 4, 5, 5, "R' F R U2 F"),
  ("R U' R' U' R", "4333404", 5, 5, 5, 5, "R U R U R"),
  ("U'", "4440400", 1, 1, 1, 1, "U"),
  ("F' R' F2 R U", "3345330", 5, 4, 5, 5, "U' R' F2 R F"),
  ("F' R F' R U F", "4545055", 6, 4, 6, 6, "F' U' R' F R' F"),
  ("U' R2 U F2 U'", "0444444", 5, 3, 5, 5, "U F2 U' R2 U"),
  ("R' F' U R' F", "0003501", 5, 5, 5, 5, "F' R U' F R"),
  ("R U R F2 R'", "1043405", 5, 4, 5, 5, "R F2 R' U' R"),
  ("F' R2 U R' U' F", "0055313", 6, 5, 6, 6, "F' U R U R2 F"),
  ("R F U' R2 U' R", "4334525", 6, 5, 6, 6, "R' U R2 U F' R"),
  ("U R F U' R'", "0044524", 5, 5, 5, 5, "R U F' R' U"),
  ("F R2 F R' U", "3343451", 5, 4, 5, 5, "U' R F' R2 F"),
  ("R' F2 R' U'", "1443433", 4, 3, 4, 4, "U R F2 R"),
  ("F U' R", "1443454", 3, 3, 3, 3, "R' U F"),
  ("R' F U F", "3344233", 4, 4, 4, 4, "F' U' F' R"),
  ("U F' U F' R", "2533333", 5, 5, 5, 5, "R' F U' F U"),
  ("U F R F R' U' R'", "0001020", 7, 5, 7, 7, "R U R F' R' F' U"),
  ("F' R F", "0024023", 3, 3, 3, 3, "F' R' F"),
  ("U' R F2 R' U", "0003132", 5, 4, 5, 5, "U' R F2 R' U"),
  ("U' R' F2 U'", "5044123", 4, 3, 4, 4, "U F2 R U"),
  ("R' F'", "2135053", 2, 2, 2, 2, "F R"),
  ("U F U' F U", "1143440", 5, 5, 5, 5, "U' F' U F' U"),
  ("U' F' R U'", "3033312", 4, 4, 4, 4, "U R' F U"),
  ("U' F U' F U F2 U", "0001110", 7, 6, 7, 7, "U' F2 U' F' U F' U"),
  ("R F' U2 F", "2015203", 4, 3, 4, 4, "F' U2 F R"),
  ("R U F' R2 U'", "0024242", 5, 4, 5, 5, "U R2 F U' R"),
  ("R' U2 F' U", "4525223", 4, 3, 4, 4, "U' F U2 R"),
  ("U R U2 F' R'", "2244331", 5, 4, 5, 5, "R F U2 R' U"),
  ("R' F' U R' U'", "2155451", 5, 5, 5, 5, "U R U' F R"),
  ("F' U F' R", "3233232", 4, 4, 4, 4, "R' F U' F"),
  ("U F2 U2 F'", "1202010", 4, 2, 4, 4, "F U2 F2 U"),
  ("U' R' F' U'", "1025113", 4, 4, 4, 4, "U F R U"),
  ("U R' F2 U2 F'", "1213023", 5, 3, 5, 5, "F U2 F2 R U"),
  ("F' R U2 F R'", "1001121", 5, 4, 5, 5, "R F' U2 R' F"),
  ("R' U' F'", "2225113", 3, 3, 3, 3, "F U R"),
  ("U R2 F U R'", "3311211", 5, 4, 5, 5, "R U' F R2 U"),
  ("R F R2 U R", "0222222", 5, 4, 5, 5, "R' U' R2 F' R"),
  ("U' R U2 F' R' U2 F", "1121211", 7, 5, 7, 7, "F' U2 R F U2 R' U")
]

theorem COUNT_TABLE_ok : COUNT_TABLE.length = 43 ∧ COUNT_TABLE.all ok = true := by native_decide

/-- Twisted corners and nothing out (section 6.3). -/
def ONLY_TWISTED : List Example := [
  ("U F R F R' U' R'", "0001020", 7, 5, 7, 7, "R U R F' R' F' U"),
  ("U' F U' F U F2 U", "0001110", 7, 6, 7, 7, "U' F2 U' F' U F' U"),
  ("U F2 U2 F'", "1202010", 4, 2, 4, 4, "F U2 F2 U"),
  ("F' R U2 F R'", "1001121", 5, 4, 5, 5, "R F' U2 R' F"),
  ("R F R2 U R", "0222222", 5, 4, 5, 5, "R' U' R2 F' R"),
  ("U' R U2 F' R' U2 F", "1121211", 7, 5, 7, 7, "F' U2 R F U2 R' U")
]

theorem ONLY_TWISTED_ok : ONLY_TWISTED.length = 6 ∧ ONLY_TWISTED.all ok = true := by native_decide

/-- Every pattern within 3 turns of all good, one per symmetry class (examples page, part 2). -/
def CATALOGUE : List Example := [
  ("", "0000000", 0, 0, 0, 0, ""),
  ("U'", "4440400", 1, 1, 1, 1, "U"),
  ("R U2", "0303303", 2, 1, 2, 2, "U2 R"),
  ("R' F'", "2135053", 2, 2, 2, 2, "F R"),
  ("R' U'", "4423103", 2, 2, 2, 2, "U R"),
  ("F' R2 F2", "5055005", 3, 1, 3, 3, "F2 R2 F"),
  ("F' R2 F", "0055055", 3, 2, 3, 3, "F' R2 F"),
  ("R U2 R'", "3303300", 3, 2, 3, 3, "R U2 R"),
  ("F U2 R", "1033551", 3, 2, 3, 3, "R U2 F"),
  ("R F' U2", "0315253", 3, 2, 3, 3, "U2 F R"),
  ("R F U2", "0351523", 3, 2, 3, 3, "U2 F' R"),
  ("U R U2", "4143302", 3, 2, 3, 3, "U2 R' U"),
  ("U F U2", "4452150", 3, 2, 3, 3, "U2 F' U"),
  ("F U' R", "1443454", 3, 3, 3, 3, "R' U F"),
  ("F R U", "3343253", 3, 3, 3, 3, "U' R' F"),
  ("F' U' F", "1013400", 3, 3, 3, 3, "F' U F"),
  ("F' R F", "0024023", 3, 3, 3, 3, "F' R' F"),
  ("U R U'", "0023502", 3, 3, 3, 3, "U R' U"),
  ("U' F' U'", "3015010", 3, 3, 3, 3, "U F U"),
  ("F U R'", "2131251", 3, 3, 3, 3, "R U' F"),
  ("R' U' F'", "2225113", 3, 3, 3, 3, "F U R")
]

theorem CATALOGUE_ok : CATALOGUE.length = 21 ∧ CATALOGUE.all ok = true := by native_decide

/-- The 200 random states of the examples page, 1 to 50. -/
def RANDOM_1 : List Example := [
  ("U R' F U F2 R' F' R2 F", "3345255", 8, 5, 6, 7, "U2 R U' F R' F' R F"),
  ("U2 F R2 F U2 F' R F", "0531043", 7, 5, 6, 6, "F' R' F U2 F' R2 F"),
  ("R F' R' F' R' U2 R' F U'", "5244421", 8, 6, 7, 7, "F2 R' F U R F2 U' R"),
  ("F' R2 F' U' F2 R U2 R2", "4320222", 8, 4, 7, 8, "R2 U2 R' F2 U F R2 F"),
  ("F' U' F' U' R F' U R' F2", "5445542", 8, 4, 7, 8, "U F2 U2 R2 U' F' U2 F"),
  ("R U R' F2 R' U R' F2 R'", "5534235", 8, 5, 7, 7, "F U2 R' U F2 U F2 R"),
  ("U R2 F R' F' R F' R U2", "4331130", 8, 5, 6, 6, "U F2 U R' U2 F2 R' F"),
  ("F U' F2 R' F R", "5334440", 6, 5, 6, 6, "R' F' R F2 U F"),
  ("U' F2 U' F' U' R U' F2 R", "2323404", 8, 5, 5, 8, "R' F2 U2 R' F' R' F2 R"),
  ("U F' R' F' U2 R F' R", "5333424", 7, 5, 7, 7, "R' F R' F R F U"),
  ("F' U2 F2 R2 U' F U R'", "3223200", 6, 5, 6, 6, "F U' F' R U2 R"),
  ("U' F' U2 F2 U' F2 R' U R2", "4412021", 8, 5, 6, 6, "R U R2 F R2 F2 R' F"),
  ("R2 U' F' U' R' F2 R2", "1003041", 6, 4, 5, 6, "R2 F2 R U F U"),
  ("R F R F' R U' F2 U", "0424135", 8, 5, 7, 8, "U' F2 U R' F R' F' R"),
  ("R U F2 U F' R U2 F' R", "2420231", 7, 5, 7, 7, "U' R' U' R F U' F"),
  ("R U' F' R U2 F2 U' R'", "0321312", 8, 6, 8, 8, "R U F2 U2 R' F U R"),
  ("F2 U' R F2 U F2 U F' U' R'", "0440143", 9, 5, 7, 7, "R U F U' F2 U' F2 R' U"),
  ("F' U R2 F2 R' F U2 R' U'", "5334542", 8, 6, 8, 8, "U' F2 R U2 R' F R' U"),
  ("R U' F R U R' F U'", "1525313", 8, 6, 8, 8, "R' U' R2 F' R2 F U' R"),
  ("F' U' F2 U' R' F R' U' R'", "2125015", 9, 4, 6, 8, "R U R F' R U F2 U F"),
  ("U R2 F2 R' F2 U' R F2 R'", "1440523", 7, 5, 7, 7, "R F2 R' U F2 R' U"),
  ("R2 U F2 R' U F' R U'", "0014003", 7, 6, 6, 7, "R' F2 U' R' F U' R"),
  ("F R U' R U F' U R2", "0104213", 8, 5, 7, 7, "R2 U' F U' R' U R' F"),
  ("F R' U2 F R2 F R' U R'", "5343305", 7, 5, 6, 6, "R' U' R F2 U2 R F"),
  ("U' R U' R2 F R F2 U2 R'", "0232401", 8, 4, 5, 7, "U F2 U2 R2 U F2 U' R"),
  ("R2 F' R' U2 F U R2 U R2", "2320242", 7, 5, 7, 7, "F U R2 F' R' U2 R"),
  ("F2 R F' R2 U2 F' R2 F U", "4423232", 8, 5, 7, 7, "R F' R' U F' R2 U' F"),
  ("U F2 R2 U' R' F2 R' F2 U R'", "2503504", 8, 6, 7, 8, "U F R2 U' F' R U2 R"),
  ("R2 U F2 R' U F", "0204422", 5, 4, 5, 5, "F' U' R F2 U"),
  ("F U' F2 U F' U' R", "0513430", 7, 6, 7, 7, "R' U F U' F2 U F"),
  ("F U' R2 F R2 F U2 F2 U' R'", "2155541", 8, 6, 7, 8, "R2 U' F R' U2 F R' F"),
  ("F R F2 U F' R2 F' R F'", "2251132", 9, 5, 7, 8, "R F U2 F R2 U' F' R F"),
  ("R' F2 U R F2 U' F U F2 R2", "2255531", 8, 6, 7, 7, "R U R F R2 U2 R' U"),
  ("R2 U F2 U' R F2 R' F2 R", "0140042", 8, 5, 8, 8, "R' F2 R F2 R' U F2 U"),
  ("R' F U2 R' F2 R' F' U F2", "2413550", 8, 6, 6, 7, "F U' R F R2 U2 F' R"),
  ("F2 R2 F' R U' F2 R U2 R", "3203220", 7, 5, 6, 7, "R' U2 R' F2 U R' F"),
  ("F U2 F' U2 R F2 R' U R2", "1124132", 8, 5, 6, 7, "R U F U R' U2 F U"),
  ("U2 R U2 F' R F U' F2 R", "5420012", 7, 4, 7, 7, "U2 F R2 U' R2 U' F"),
  ("U R F2 U' F U' R2 F' R'", "2320032", 7, 5, 7, 7, "R F2 R' U2 F U' F"),
  ("F' U F' R F' R U' R2 U'", "2440045", 8, 6, 7, 7, "R U F2 U' R2 F R' F"),
  ("F U' F U' R F' U' R2", "0155552", 8, 5, 6, 8, "R2 U F R' U F' U F"),
  ("F U' F U2 R2 U' F U2 F'", "5450214", 8, 6, 7, 8, "R' U R F2 R F' R2 F"),
  ("F' R' U R F2 R2 U R' U' R2", "1503352", 9, 5, 5, 5, "R U2 R2 F' U F U' F R"),
  ("U2 F U2 R U' F2 U' R2", "1311141", 7, 4, 6, 6, "R2 U F2 U R U2 F"),
  ("R U' R2 U' R2 U' F' U2 R'", "2030421", 8, 4, 7, 8, "R2 F U R F2 U F' R"),
  ("U2 R2 F' U' F' R F U' F'", "3553154", 7, 5, 7, 7, "F U F' R' F U F"),
  ("R' F R2 F2 U' R' U F2", "3513031", 8, 5, 6, 6, "R2 F' R' U R2 U' R2 U"),
  ("F' R F' U F2 R' U R' U", "2501230", 8, 4, 6, 8, "F R' U F U2 F2 U F"),
  ("U2 F' R' U2 R' U' F2 U R", "5152111", 8, 6, 7, 7, "R' U' F2 U R U2 R F"),
  ("R U2 R' F' U2 R2 F' R'", "1500250", 8, 5, 7, 7, "R U F' U F U2 R' F")
]

theorem RANDOM_1_ok : RANDOM_1.length = 50 ∧ RANDOM_1.all ok = true := by native_decide

/-- The 200 random states of the examples page, 51 to 100. -/
def RANDOM_2 : List Example := [
  ("U' F' U2 F2 U' R' F2 R", "4414300", 8, 5, 7, 8, "R' F2 R U F2 U2 F U"),
  ("R2 U R2 U' F U2 R' F2 R", "2155514", 8, 5, 7, 8, "R' F2 R U2 F' U R2 U"),
  ("R2 F2 U2 F' R2 F R' U R2", "1334453", 6, 4, 6, 6, "R2 U' R F' R2 F"),
  ("F' R U2 R' F U' F R2 F2", "1023402", 8, 6, 6, 6, "R2 U' R' F' R2 U F R"),
  ("R2 U2 R F R2 F R2 F R' U2", "0334433", 8, 5, 6, 8, "U2 R F' R2 F' R2 F' R"),
  ("U' R' U' R F' R U' F2", "5533330", 8, 5, 7, 8, "F2 U R U' R U' F' U"),
  ("F2 U R U R F R2 F", "0451044", 7, 6, 7, 7, "F' R2 F' R' U' R' U"),
  ("U' F' U F2 R U' R' U2 R", "2043305", 8, 5, 6, 8, "U2 R' F U R2 U2 F R"),
  ("R2 U' F2 U F2 U R2 F' R2", "4554055", 7, 4, 7, 7, "R2 F U F2 U R2 U"),
  ("F' U F2 U' R U R' F", "5213220", 8, 5, 6, 7, "F U' F' U2 R U R' U"),
  ("U2 R F R2 U' R2 U' R F'", "1033134", 8, 6, 6, 7, "F R' U R2 U R2 F' R"),
  ("F U2 F U2 R2 F U R2 F'", "3050212", 8, 5, 7, 8, "F R U' R F' R' U2 R"),
  ("R2 F2 R F' U2 R' F2", "5303241", 5, 3, 5, 5, "F2 R U2 F R"),
  ("F U' R U R U' F2 U' F2 U", "5343053", 9, 6, 6, 6, "R U2 R F U2 R2 F U F"),
  ("R U' F2 R' U R' F2 R U2", "1113402", 8, 6, 6, 6, "F' U2 F R' U' F R2 F"),
  ("F U R2 F2 U F R2 U2 R'", "1303431", 9, 5, 6, 6, "R U2 R2 F' U' F2 R2 U' F"),
  ("F U2 F U R2 F2 U R2 U2", "5140202", 7, 4, 5, 7, "F U' F R2 U F' U"),
  ("R' U' R' U' R2 F R", "1543434", 6, 4, 6, 6, "R' F' U R U R"),
  ("U F R' F2 R F2 U F'", "0104300", 7, 6, 7, 7, "F' R F2 U F U R"),
  ("R2 U' R U' F' U F2 U R'", "1142231", 8, 5, 7, 7, "R U' F2 U R' U' R F"),
  ("U2 F R' U' R U' F' U2", "0150025", 7, 4, 7, 7, "R2 F R' U2 R' U2 R"),
  ("R U R' U R2 F' U F2 R'", "5513224", 8, 5, 7, 8, "R' U2 F2 U F' R U2 R"),
  ("U' R2 U' R' F R' U' F' R2", "0330054", 7, 5, 6, 6, "R' F R2 F' R2 F R"),
  ("F2 R2 U F' R' F U' R'", "3053140", 6, 4, 6, 6, "R U F' R F U"),
  ("R2 U R2 F U' F' U R2", "4440151", 6, 5, 6, 6, "F U2 R U F R"),
  ("F2 U R' F U' F R2 U' R'", "5322120", 7, 5, 6, 6, "R F2 U' R U2 R F"),
  ("F' R' F2 U' R F U R'", "0311502", 8, 5, 6, 6, "R U' F' R' U F2 R F"),
  ("F2 R2 F R2 F' R' U' R2", "3423302", 6, 4, 6, 6, "R2 U R F R2 F"),
  ("U2 R2 F2 U R2 U' F' U R2", "4350250", 6, 4, 6, 6, "R2 U' F U R2 U"),
  ("F' R U' R' U' F U R2 U", "2400410", 8, 6, 7, 7, "F' R2 U R2 U' F U F"),
  ("R' F2 R U2 R U F2 U'", "1322310", 8, 5, 6, 7, "R' U2 R' F2 R' F' U2 F"),
  ("R2 U R2 F U' R2 F R' U' R'", "0023025", 8, 5, 6, 6, "R2 F U2 F2 U F' U F"),
  ("F' R2 F2 U' R' U2 R2 F", "4514412", 7, 4, 7, 7, "F R2 F U R2 F2 R"),
  ("U2 R' F2 R' F U2 F U'", "1515503", 7, 5, 7, 7, "U F' U2 F' R F2 R"),
  ("U R2 F' U2 F R' F2 R U2", "1322214", 7, 5, 5, 5, "U' R F U' F U' F"),
  ("U F U F' R2 U", "4450224", 6, 5, 6, 6, "U' R2 F U' F' U"),
  ("U F R F U2 R2 F2 R' F'", "1113051", 8, 6, 7, 8, "F R F2 R2 F' U' R' U"),
  ("U R2 F U' R2 F2 U' R'", "0045243", 8, 5, 7, 8, "R U F2 R2 U F R2 U"),
  ("U2 R' F2 R' U' R2", "3434431", 5, 3, 5, 5, "R2 U R F2 R"),
  ("F R2 F' U2 F' U' F2 R'", "4523224", 7, 5, 7, 7, "U F2 U' F R2 U' F"),
  ("U F2 R2 U' R' U' F", "1252132", 5, 3, 5, 5, "F2 R2 F U R"),
  ("R2 U' F' U' F2 R' F2 R U'", "2430440", 7, 6, 7, 7, "U2 R' F R F U' F"),
  ("R2 U2 F' U' R2 F2 U' R F' R", "1351255", 8, 6, 7, 7, "R' F R' U F2 R2 U F"),
  ("R F' R2 F U' R F R2 U2 R'", "0254514", 9, 5, 6, 8, "R2 U R' U R2 F' R U F"),
  ("R U R' F' U R2 F R'", "1215151", 8, 5, 5, 7, "R F' R2 U R' F' R F"),
  ("U R2 U' F2 U' R F' R' U2", "0410051", 9, 6, 6, 6, "R2 U R2 U' R2 U' R F R"),
  ("U R' U' F U2 F' R2 F' U'", "5145510", 8, 5, 6, 7, "R' U2 F2 U' R' F U2 F"),
  ("R' U R' F R2 U' F' R2 F R'", "1024115", 8, 6, 6, 6, "R' U F R F2 U' F2 U"),
  ("F' R U2 F2 R F R2 U2 R'", "1045155", 9, 5, 6, 6, "R U2 R2 F' R' F2 U2 R' F"),
  ("R' U2 F' U2 F R F2 U2 R", "0245043", 8, 5, 6, 7, "U F2 R F U2 R2 F R")
]

theorem RANDOM_2_ok : RANDOM_2.length = 50 ∧ RANDOM_2.all ok = true := by native_decide

/-- The 200 random states of the examples page, 101 to 150. -/
def RANDOM_3 : List Example := [
  ("F2 R F2 R' U F' R U' F", "2401052", 8, 5, 4, 4, "R' F R' U F' U R2 U"),
  ("U F R F2 R F' U R' U2", "0530323", 8, 5, 7, 7, "F2 U R U' R F' U' F"),
  ("U' R2 F R' U' R' F U'", "0110211", 8, 5, 8, 8, "R' U R F2 U' F R F"),
  ("U F U2 R' U2 F' R F2 R2", "2240132", 8, 5, 7, 7, "R U2 F2 R U' R2 F U"),
  ("F R2 F U2 R2 F R' U", "1343453", 7, 5, 6, 7, "R' F U F' R U' R"),
  ("R2 U R U' F U R' F2", "2041241", 7, 6, 6, 6, "F2 R U' F' U R' U"),
  ("U R2 F U R2 U F", "5453154", 7, 5, 6, 7, "U R F' U F U' F"),
  ("R F' R U2 F U R2 U R2", "5430152", 9, 6, 6, 8, "R2 U' R U' R' U R F' U"),
  ("R2 F U R' U2 F U F2 R' U'", "1030251", 7, 5, 6, 7, "U' F2 U F R2 U' R"),
  ("R F' R2 F' U2 F U' F R'", "2043503", 8, 5, 6, 7, "F R' F U2 F' U F' U"),
  ("R2 U' R F' U R' F2 R'", "2255531", 7, 6, 7, 7, "R F2 R U' F R' U"),
  ("R' F R' F R' U' F' R2", "1422512", 8, 5, 6, 6, "R2 F U R F' R F' R"),
  ("R2 F U' F2 R2 U F'", "3503215", 6, 4, 6, 6, "F U' R2 F2 U F"),
  ("R' F2 R' U R F' R2 F' U R'", "0222102", 8, 6, 7, 7, "U' F R U2 R2 F U' R"),
  ("R2 F R F' U2 F2 U' R'", "2501005", 7, 5, 7, 7, "R U F2 U2 F R' F"),
  ("R F U' F' R U2 F' R U", "3541050", 8, 6, 6, 6, "R2 F2 U F U' F R' F"),
  ("F R' U' F' U F2 U F2", "3033411", 8, 6, 6, 6, "R U' F' U R U R' F"),
  ("F2 R' F R' F R2 F R2", "0225052", 7, 5, 7, 7, "R2 F' R2 F' R F' R"),
  ("U R2 F2 U' R U' F'", "3255152", 6, 5, 6, 6, "F U R' U R2 U"),
  ("R' F2 U F' U2 R2 F2 U' F R'", "0150511", 8, 6, 7, 8, "R2 U2 R U R' F U F"),
  ("F' U2 F' U R F2 U' F2 R'", "4410011", 8, 6, 7, 8, "U F2 U' F R' F' R2 F"),
  ("U' F2 R F' R2 F R2 F' R2", "2333454", 7, 5, 7, 7, "R U R2 U2 R' F R"),
  ("F R2 F' R' F R2 U2 R' U R'", "5325040", 8, 5, 7, 7, "F2 R2 F U2 F' R F' R"),
  ("R' U F2 U R' U R U'", "3442510", 7, 5, 6, 7, "F U2 F U' R' F2 R"),
  ("F2 U R' F U2 R2 F R2", "4113102", 7, 4, 7, 7, "R2 F' R2 U2 F' R U"),
  ("F' R2 U2 R' U2 F' R' U2", "1054143", 6, 4, 6, 6, "U2 R F U2 R' F"),
  ("U2 F U2 F U F R U2 F' R'", "1214051", 9, 5, 7, 8, "R F U2 R' U F2 U' F' U"),
  ("R2 U2 F' U' F2 R U", "3503224", 5, 4, 5, 5, "U' R' F2 U F"),
  ("U2 F U' R2 F2 U R' F", "3541512", 7, 5, 7, 7, "F U' R U2 F2 R' U"),
  ("R2 U2 R F' U R' F' U R'", "4451103", 7, 5, 7, 7, "R U' F R U' F R"),
  ("U' F R2 F' U R2 F2 U' R2", "3534414", 8, 5, 7, 8, "F' R2 U F' R U' F R"),
  ("F R2 U2 F' R U' R F2 U2", "3454055", 7, 5, 6, 6, "F R2 F' U2 R F R"),
  ("F2 R2 F R F U F U R2", "3310110", 6, 4, 6, 6, "R2 F R U F2 R"),
  ("F U F' R2 F' R2 F U2 R", "1145055", 8, 6, 7, 7, "R2 U' F R F' R2 U' F"),
  ("U2 F R' U' F R2 F2 U2", "1320411", 6, 4, 6, 6, "F2 R2 F' R U F"),
  ("R2 U R2 U' F U' R F U2", "0444534", 8, 6, 7, 7, "R' F2 R F' R U2 F' R"),
  ("U' R U2 R' F' R2 F U2 R'", "4500211", 7, 4, 7, 7, "R2 U R2 U' F R2 U"),
  ("F2 R' F' R' U2 F U' R' U2", "5541411", 8, 6, 6, 6, "U2 R U F' U2 R F R"),
  ("U' F U' R U R' U2 F", "2012220", 7, 5, 7, 7, "R' U2 F R F2 U' R"),
  ("F2 R' F' R F' U2 F' R'", "2532514", 7, 6, 7, 7, "R F U2 F R' F R"),
  ("R2 F2 U2 R' U' R U' F U'", "2155055", 6, 4, 6, 6, "U F' U R' U R"),
  ("R' F' R U' R U' R2", "0432350", 7, 6, 7, 7, "R2 U R' U R' F R"),
  ("F' U2 F' R F' U' R'", "1152103", 7, 4, 7, 7, "R U F R' F U2 F"),
  ("U2 R' U2 R U R2 U' F2", "0223401", 7, 4, 6, 7, "F2 U R2 U' R' U2 R"),
  ("R2 F2 R F' U' F R' U2 R'", "3005101", 7, 6, 5, 5, "R U2 R F' U F R"),
  ("U2 F' R F U2 R' U R", "0214322", 7, 6, 7, 7, "R' U' R U2 F' R' F"),
  ("U' F2 R U' R F2 R' F R'", "1505135", 7, 5, 7, 7, "R2 F U F R U2 F"),
  ("F' R' F U2 F' U2 R F' R", "0035350", 9, 5, 7, 8, "R U' R U2 F' U2 F U' F"),
  ("F R' F U' F2 R F' U' R2", "2324531", 7, 5, 6, 7, "F' R U2 F2 R F' U"),
  ("R U F R2 U2 F U' F' R2", "4443244", 8, 6, 5, 8, "F2 R' U2 F R' F U' F")
]

theorem RANDOM_3_ok : RANDOM_3.length = 50 ∧ RANDOM_3.all ok = true := by native_decide

/-- The 200 random states of the examples page, 151 to 200. -/
def RANDOM_4 : List Example := [
  ("F' U2 R U' R2 U2 F2 U' F' R'", "4414522", 8, 6, 7, 7, "U' R F' U F' U F' R"),
  ("R' U F2 U R' U R' U", "3441310", 8, 5, 6, 6, "R F' R F' U F2 U R"),
  ("U R' U2 F' R' U' F2 R F' U2", "4441051", 8, 5, 7, 7, "R' U' R2 U R2 F' R2 F"),
  ("R' F2 R' F R' F2 U' F R'", "1155431", 8, 5, 8, 8, "U R' F' U' F2 R U' F"),
  ("F' R' U F' R' F2 R2 F'", "0143234", 8, 4, 7, 7, "R2 U2 R' F2 R U' F2 U"),
  ("F2 R F R2 F U' R2 U R'", "4152022", 8, 6, 7, 7, "R U F2 R' U' R2 U' F"),
  ("R2 U R F' R2 U F2", "1105522", 6, 4, 6, 6, "F2 U' R2 F R' U"),
  ("U2 F' R F' R U F' R' U", "3542241", 8, 6, 7, 7, "U F' U2 R' F R2 F U"),
  ("R' U R F2 U2 F' U F U2", "3452502", 8, 4, 7, 7, "R2 F R F2 R2 F' U2 F"),
  ("R' U F U2 F2 R2 F' U R'", "3443515", 8, 6, 6, 8, "U' R' F' U2 R2 F U' F"),
  ("F2 R' F' R U' R U2 F' R'", "2534343", 8, 5, 7, 7, "R F U2 R' U R' F R"),
  ("F R2 U2 F' R' F R2 F2", "4245030", 7, 4, 7, 7, "R2 F2 R F2 R F R"),
  ("U' F2 R2 F' U2 R2 F U'", "4335304", 6, 4, 6, 6, "U F' R2 U2 F' U"),
  ("F2 R' F' R2 F2 U' F' R U2", "2044414", 7, 5, 6, 7, "F U R2 U2 F U F"),
  ("F2 R U F R2 U' R2 F' R2", "2234054", 8, 5, 8, 8, "R2 F R2 U R2 F' U' R"),
  ("F' U F R' U' F' R", "1222101", 7, 5, 7, 7, "R F U R F' U' F"),
  ("F2 U' F R' U R2 U' F2", "5015221", 7, 5, 7, 7, "F2 U R2 U' R F' U"),
  ("F' U F R' U F2 U R2 U'", "0010212", 8, 5, 7, 7, "R2 U' F2 R' F R2 U' R"),
  ("U2 F U' R U2 R2 U'", "0304154", 6, 4, 6, 6, "R F U F' R U"),
  ("R2 U2 F' R2 F' U' F2 U2 R", "2142023", 7, 4, 7, 7, "R' U2 F2 U F R2 F"),
  ("R' F2 R U R' F U' R'", "3302100", 8, 5, 7, 8, "R U F' R U' R' F2 R"),
  ("R' U F' R' U' F2 R U R'", "3252001", 8, 4, 5, 7, "R2 U2 R' U2 R' F' U2 F"),
  ("F U2 R2 U F U2 R' F", "3531130", 6, 5, 6, 6, "F' R U2 F' U F"),
  ("R2 U R2 U R' F' R2", "2151013", 6, 4, 6, 6, "R2 F R U' R2 U"),
  ("R2 U2 R' F2 R U R2 F' R'", "3555144", 7, 5, 7, 7, "R F R2 U' R' F2 R"),
  ("U' F' U2 F' U R2 U F2 U2", "0214103", 8, 5, 7, 7, "R2 U F2 U F' U2 F U"),
  ("F2 R2 U2 R' F U' F2 R F2", "2041124", 6, 4, 6, 6, "F2 R' F2 U F' R"),
  ("F' U R' F' R2 F' R2 F R2", "2311251", 8, 4, 4, 7, "R U' F' U R2 U' R2 U"),
  ("U' F2 R2 U F R2 U' R' U2 R", "3540213", 8, 6, 6, 8, "F R' U2 R U R2 U F"),
  ("R F R2 U2 F R U2 F U", "1131141", 8, 4, 6, 6, "U2 R2 U F2 U R U2 F"),
  ("R2 U2 R F' R F' U2 F R2", "0154551", 7, 5, 7, 7, "R2 F' U2 F R' F R"),
  ("U2 R' U2 R2 U' R F' R", "1142141", 7, 5, 7, 7, "R' F R' U R2 U2 R"),
  ("F U2 R' U' F2 U' F R2 F' U'", "0321042", 8, 5, 7, 8, "R U2 R2 U' R2 F' R F"),
  ("R F' U F' U' F2 R' F2 R'", "3313023", 8, 5, 6, 8, "R2 F U' R2 U F2 R F"),
  ("F U2 F U2 F' U F U' R'", "0034505", 8, 5, 4, 7, "F2 U' F R2 F2 U F R"),
  ("U' F' U F U2 R' U R2 U2", "4052101", 7, 4, 6, 7, "F' R U R' U2 R F"),
  ("R U2 F' R2 F2 R' U' F2 U2", "0342341", 8, 4, 7, 8, "U' R U' R' F U' R F"),
  ("F R U R' U R F2 R F' R2", "4412120", 8, 4, 7, 7, "R' U R U2 F2 R U' R"),
  ("U2 R F U2 R2 F2 R' U2 R'", "1332432", 6, 4, 6, 6, "R' F U' F2 R2 F"),
  ("U2 F' R' U R' U2 F R U'", "4542105", 8, 3, 5, 8, "U R U2 R2 F2 U R' U"),
  ("R' U R U F2 U R' U' F2", "2110002", 8, 7, 6, 8, "R' U R' U2 R' F' U' F"),
  ("R2 F R2 F U2 R' U' F R2", "1032321", 8, 5, 6, 6, "R2 F' U R U2 F' R2 F"),
  ("F' R' U2 R U R' U2 F", "0014501", 8, 6, 5, 7, "R F2 U' R' F2 U F' R"),
  ("U' R U' F2 U' R U F2 R", "5434525", 9, 5, 7, 7, "R' F2 U' R' U F2 U R' U"),
  ("F R U' R' F2 U F' U2 F R'", "5131101", 7, 6, 7, 7, "F' R' U2 F R F R"),
  ("F U2 R F2 U' R F R'", "1410104", 7, 6, 6, 7, "R2 F R F' U R U"),
  ("U' R U' R' U R F' R2", "4553432", 7, 5, 7, 7, "R U' R2 U F2 R' U"),
  ("F' U' R2 U2 R' F' R2 F U'", "2452413", 8, 6, 8, 8, "U R' F R U2 F2 U' R"),
  ("F2 U2 R' U2 R' F' U F' U'", "3143300", 7, 6, 5, 7, "U F U' F R U2 R"),
  ("U R2 F' U' F2 U' F R2 F' R'", "0224123", 9, 5, 6, 7, "U R' F2 U2 R' U R' U' R")
]

theorem RANDOM_4_ok : RANDOM_4.length = 50 ∧ RANDOM_4.all ok = true := by native_decide

/-- DR corner cases with the all-turn solution the page prints (examples page, part 4). -/
def DR_CASES : List Example := [
  ("", "0000000", 0, 0, 0, 0, ""),
  ("R2 U' F2 U2 R2 U' F2 U2 R2 U' R2", "0000000", 9, 3, 0, 9, "F R2 F2 U2 F R2 F2 U2 F"),
  ("U R2 U2 F2 U' F2 U2 R2 U'", "0000000", 9, 3, 0, 9, "U R2 U2 F2 U R2 U2 F2 U"),
  ("F2 U R2 U' R2 U2 F2 U' F2 U", "0000000", 9, 4, 0, 0, "R' U2 R U2 R2 F2 R F2 R"),
  ("U' R2 U' R2 U", "0004400", 5, 3, 5, 5, "U' R2 U R2 U"),
  ("F2 U' F2 U R2 U' F2 U F2", "0040400", 7, 4, 6, 7, "R U' R F2 R' U R"),
  ("U R2 U F2 U' R2 U'", "0004040", 7, 4, 6, 7, "U R2 U F2 U' R2 U"),
  ("R2 U' R2 U F2 U' F2 U R2 U' R2", "0400004", 8, 5, 5, 5, "R F R' F2 R U' R U"),
  ("U'", "4440400", 1, 1, 1, 1, "U"),
  ("U' F2 U2 R2 U'", "0440044", 5, 2, 4, 5, "U R2 U2 F2 U"),
  ("U R2 U R2 U2 F2 U'", "4044004", 7, 3, 3, 3, "U R2 U2 F2 U' F2 U"),
  ("U' R2 U F2 U' R2 U R2 U R2 U'", "0044440", 9, 4, 2, 7, "U R F' U F2 U' F R U"),
  ("U F2 U R2 U2 F2 U' R2 U", "0440044", 9, 4, 4, 5, "U R2 U R2 U2 F2 U' R2 U"),
  ("U R2 U'", "0044404", 3, 2, 3, 3, "U R2 U"),
  ("U R2 U2 F2 U' F2 U'", "4404004", 7, 3, 3, 7, "U F2 U R2 U2 F2 U"),
  ("F2 U' F2 U F2 U' F2 U F2 U' R2 U'", "0044044", 9, 4, 4, 4, "R' U' R' U' F2 U' R U R"),
  ("U2 R2 U R2 U R2 U2 F2 U' R2 U", "0044404", 9, 4, 3, 3, "R U' R U R' F2 R' U' R"),
  ("R2 U R2 U' R2 U F2 U' R2 U' R2", "0044404", 8, 5, 3, 7, "R' U F' R2 F R' F' U")
]

theorem DR_CASES_ok : DR_CASES.length = 18 ∧ DR_CASES.all ok = true := by native_decide

/-- The kinds of pattern within two quarter turns of HTR (section 8.4). -/
def WITHIN_TWO_QT : List Example := [
  ("", "0000000", 0, 0, 0, 0, ""),
  ("U'", "4440400", 1, 1, 1, 1, "U"),
  ("R' U2 R2 F2 R'", "0033330", 5, 2, 4, 5, "R U2 R2 F2 R"),
  ("F' R2 F", "0055055", 3, 2, 3, 3, "F' R2 F"),
  ("F U2 R", "1033551", 3, 2, 3, 3, "R U2 F"),
  ("R' F'", "2135053", 2, 2, 2, 2, "F R"),
  ("U F2 U2 F'", "1202010", 4, 2, 4, 4, "F U2 F2 U")
]

theorem WITHIN_TWO_QT_ok : WITHIN_TWO_QT.length = 7 ∧ WITHIN_TWO_QT.all ok = true := by native_decide

/-- States used in the text and in the worked examples. -/
def WORKED : List Example := [
  ("R", "3033003", 1, 1, 1, 1, "R"),
  ("R U", "1243403", 2, 2, 2, 2, "U' R"),
  ("U R2 U'", "0044404", 3, 2, 3, 3, "U R2 U"),
  ("R' U2 R2 F2 R'", "0033330", 5, 2, 4, 5, "R U2 R2 F2 R"),
  ("U R2 U F2 U2 R2 U F2 U", "0000000", 9, 4, 0, 0, "R' U2 R U2 R2 F2 R F2 R"),
  ("U R2 U2 F2 U R2 U2 F2 U", "0000000", 9, 3, 0, 9, "U R2 U2 F2 U R2 U2 F2 U"),
  ("U F2 U2 F'", "1202010", 4, 2, 4, 4, "F U2 F2 U"),
  ("F R2 F2 U2", "0505505", 4, 1, 4, 4, "R2 F2 U2 F"),
  ("F2 R2 U' R' F R' F2 R U' R'", "0004400", 8, 5, 5, 5, "R U R' F2 R F' R U"),
  ("R' U' F U' F U F2 U R'", "0000111", 9, 8, 9, 9, "R U' F2 U' F' U F' U R")
]

theorem WORKED_ok : WORKED.length = 10 ∧ WORKED.all ok = true := by native_decide

/-- `sol`, done after `scr`, solves the corners (not just into HTR). -/
def solves (scr sol : String) : Bool :=
  onlyRUF scr && onlyRUF sol && ofScramble (scr ++ " " ++ sol) == ofScramble ""

/-- The DR-only solutions of the examples page end in HTR and use U, R2, F2 only. -/
theorem dr_only_solutions :
    [("R2 U' F2 U2 R2 U' F2 U2 R2 U' R2", "R2 U R2 U2 F2 U R2 U2 F2 U"),
     ("U R2 U2 F2 U' F2 U2 R2 U'", "U R2 U2 F2 U R2 U2 F2 U"),
     ("F2 U R2 U' R2 U2 F2 U' F2 U", "U' R2 U R2 U2 F2 U R2 U"),
     ("U' R2 U' R2 U", "U' R2 U R2 U"),
     ("F2 U' F2 U R2 U' F2 U F2", "F2 U F2 U' R2 U R2 U"),
     ("U R2 U F2 U' R2 U'", "U R2 U F2 U' R2 U"),
     ("R2 U' R2 U F2 U' F2 U R2 U' R2", "R2 U R2 U F2 U' R2 U F2 U"),
     ("U'", "U"),
     ("U' F2 U2 R2 U'", "U R2 U2 F2 U"),
     ("U R2 U R2 U2 F2 U'", "U R2 U2 F2 U' F2 U"),
     ("U' R2 U F2 U' R2 U R2 U R2 U'", "U R2 U' R2 U R2 U' R2 U F2 U"),
     ("U F2 U R2 U2 F2 U' R2 U", "U R2 U R2 U2 F2 U' R2 U"),
     ("U R2 U'", "U R2 U"),
     ("U R2 U2 F2 U' F2 U'", "U F2 U R2 U2 F2 U"),
     ("F2 U' F2 U F2 U' F2 U F2 U' R2 U'", "R2 U' F2 U R2 U2 F2 U' R2 U"),
     ("U2 R2 U R2 U R2 U2 F2 U' R2 U", "U' R2 U R2 U2 F2 U' F2 U"),
     ("R2 U R2 U' R2 U F2 U' R2 U' R2", "R2 U R2 U F2 U' R2 U R2 U")].all
      (fun (p : String × String) => reaches p.1 p.2 &&
        (parse p.2).all (fun m => ["U", "U2", "U'", "R2", "F2"].contains m)) = true := by native_decide

/-- The errata's first item: the case, the two 13-move sequences and the 12-move one all solve the corners. -/
theorem wen_case :
    solves "R2 U' R2 U F2 U2 R2 U' R2 U F2 U2 R2" "R2 U2 F2 U' R2 U R2 U2 F2 U' R2 U R2" = true ∧
    solves "R2 U' R2 U F2 U2 R2 U' R2 U F2 U2 R2" "U' F2 U R2 U2 F2 U R2 U2 F2 U' F2 U2" = true ∧
    solves "R2 U' R2 U F2 U2 R2 U' R2 U F2 U2 R2" "U R2 U R2 U2 F2 U F2 U2 R2 U R2" = true ∧
    (parse "U R2 U R2 U2 F2 U F2 U2 R2 U R2").length = 12 := by native_decide

/-- Section 6.6: one turn on the inverse is enough.  The inverse of the scramble, then F, is in HTR, while
the scramble itself is 4 turns away. -/
theorem niss_example :
    fHTR (ofScramble "F R2 F2 U2") = 4 ∧
    inHTR (ofScramble "U2 F2 R2 F' F") = true := by native_decide

end pages
end Corners3D
