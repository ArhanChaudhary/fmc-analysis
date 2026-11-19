/-
  Corners3D.Examples — examples checked on the sticker model, one theorem each (written by gen_examples.py;
  do not edit by hand).  `check scr kinds d q ft fp sol`: the state the scramble makes shows these kinds (seven
  digits for UFR UFL UBR DFR UBL DFL DBR), is d turns and q quarter turns from HTR, has types floor ft and
  parity floor fp, and the d-turn sequence `sol` takes it into HTR.
-/
import Corners3D.Witness
namespace Corners3D
namespace examples
open witness

/-- an HTR state -/
theorem ex_0001 : check "R2 U2" "0000000" 0 0 0 0 "" = true := by
  native_decide
/-- one quarter turn: the four corners of R are out with the R/L sticker oriented -/
theorem ex_0002 : check "R" "3033003" 1 1 1 1 "R" = true := by
  native_decide
/-- two quarter turns on two axes: two twisted corners appear -/
theorem ex_0003 : check "R U" "1243403" 2 2 2 2 "U' R" = true := by
  native_decide
/-- a fake HTR (every corner good, odd placement): 9 turns and 3 quarter turns from HTR -/
theorem ex_0004 : check "U R2 U2 F2 U R2 U2 F2 U" "0000000" 9 3 0 9 "U R2 U2 F2 U R2 U2 F2 U" = true := by
  native_decide
/-- a fake HTR with an even placement: 9 turns and 4 quarter turns from HTR -/
theorem ex_0005 : check "U R2 U R2 U2 F2 U R2 U" "0000000" 9 4 0 0 "R' U2 R U2 R2 F2 R F2 R" = true := by
  native_decide
/-- a state 10 turns from HTR, the most there is -/
theorem ex_0006 : check "U R F' R2 F2 U R' F R U" "0011112" 10 6 8 8 "R U F' U R' F R U2 R2 U" = true := by
  native_decide
/-- a state that needs 8 quarter turns, the most there is -/
theorem ex_0007 : check "F' U2 F' U R' F' U R' U2 R'" "0000111" 9 8 9 9 "R U' F2 U' F' U F' U R" = true := by
  native_decide
/-- types floor 0 and still 9 turns away -/
theorem ex_0008 : check "F2 U' R U R F2 R U' R' U R'" "0000000" 9 3 0 9 "U R2 U2 F2 U R2 U2 F2 U" = true := by
  native_decide
/-- types floor exact at 8 turns -/
theorem ex_0009 : check "R' F2 U F' R' F' U R'" "0011112" 8 5 8 8 "R U' F R F U F2 R" = true := by
  native_decide

end examples
end Corners3D
