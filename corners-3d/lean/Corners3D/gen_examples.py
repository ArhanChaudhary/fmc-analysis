#!/usr/bin/env python3
"""Write Corners3D/Examples.lean: one checked theorem per scramble.

    gen_examples.py                 the built-in sample (edge cases and a few extreme states)
    gen_examples.py FILE            one scramble per line (R, U, F turns; text after '#' is a comment that
                                    becomes the theorem's docstring; blank lines are skipped)

Every number is read from the study's tables (research/out/big, written by the Rust engine and derive.py);
Lean then checks each line against its own tables, on the sticker model.  The line format is

    theorem ex_0007 : check "<scramble>" "<kinds>" <turns> <quarter turns> <types floor> <parity floor> "<solution>" = true := by
      native_decide

where <kinds> is seven digits for UFR UFL UBR DFR UBL DFL DBR (0 good, 1 twisted cw, 2 twisted ccw, 3 / 4 / 5 out
with the R/L, U/D, F/B sticker oriented) and <solution> is a shortest sequence into HTR.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "research", "src"))
import c3  # noqa: E402


def descend(mv, table, s):
    """A shortest sequence from state s to a state where table is 0, taking the first turn that lowers it."""
    out = []
    while table[s] > 0:
        for m in range(9):
            t = int(mv[m][s])
            if table[t] + 1 == table[s]:
                out.append(m)
                s = t
                break
        else:
            raise AssertionError("table is not a distance")
    return out


def scramble_of(mv, d_solved, s):
    """A shortest sequence from solved to state s."""
    return c3.invert(descend(mv, d_solved, s))


def main():
    mv = c3.moves()
    kinds = c3.kinds()
    dh, q = c3.u8("d_htr"), c3.u8("qt_htr")
    dg, de = c3.u8("d_good"), c3.u8("d_goodeven")
    ds = c3.u8("d_solved")
    rows = []
    if len(sys.argv) > 1:
        for line in open(sys.argv[1]):
            scr, _, note = line.partition("#")
            if scr.strip():
                rows.append((scr.strip(), note.strip()))
    else:
        rows = [
            ("R2 U2", "an HTR state"),
            ("R", "one quarter turn: the four corners of R are out with the R/L sticker oriented"),
            ("R U", "two quarter turns on two axes: two twisted corners appear"),
            ("U R2 U2 F2 U R2 U2 F2 U", "a fake HTR (every corner good, odd placement): 9 turns and 3 quarter turns from HTR"),
            ("U R2 U R2 U2 F2 U R2 U", "a fake HTR with an even placement: 9 turns and 4 quarter turns from HTR"),
        ]
        far = int(np.where(dh == 10)[0][0])
        rows.append((c3.show(scramble_of(mv, ds, far)), "a state 10 turns from HTR, the most there is"))
        most = int(np.where(q == 8)[0][0])
        rows.append((c3.show(scramble_of(mv, ds, most)), "a state that needs 8 quarter turns, the most there is"))
        gap = int(np.where((dh.astype(int) - dg) == 9)[0][0])
        rows.append((c3.show(scramble_of(mv, ds, gap)), "types floor 0 and still 9 turns away"))
        tight = int(np.where((dh == dg) & (dh == 8))[0][0])
        rows.append((c3.show(scramble_of(mv, ds, tight)), "types floor exact at 8 turns"))
    out = [
        "/-",
        "  Corners3D.Examples — examples checked on the sticker model, one theorem each (written by gen_examples.py;",
        "  do not edit by hand).  `check scr kinds d q ft fp sol`: the state the scramble makes shows these kinds (seven",
        "  digits for UFR UFL UBR DFR UBL DFL DBR), is d turns and q quarter turns from HTR, has types floor ft and",
        "  parity floor fp, and the d-turn sequence `sol` takes it into HTR.",
        "-/",
        "import Corners3D.Witness",
        "namespace Corners3D",
        "namespace examples",
        "open witness",
        "",
    ]
    for i, (scr, note) in enumerate(rows, 1):
        s = c3.apply(mv, 0, scr)
        ks = "".join(str(int(k)) for k in kinds[s])
        sol = c3.show(descend(mv, dh, s))
        if note:
            out.append(f"/-- {note} -/")
        out.append(
            f'theorem ex_{i:04d} : check "{scr}" "{ks}" {int(dh[s])} {int(q[s])} {int(dg[s])} {int(de[s])} "{sol}" = true := by'
        )
        out.append("  native_decide")
    out += ["", "end examples", "end Corners3D", ""]
    path = os.path.join(HERE, "Corners3D", "Examples.lean")
    open(path, "w").write("\n".join(out))
    print(f"{path}: {len(rows)} examples")


if __name__ == "__main__":
    main()
