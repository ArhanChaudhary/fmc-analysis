#!/usr/bin/env python3
"""Write lean/Corners3D/Corners3D/Pages.lean: every scramble the pages print, with what the pages say about it,
checked in Lean on the sticker model.

For each state: the types line (as seven digits for UFR UFL UBR DFR UBL DFL DBR), the moves and quarter turns to
HTR, the types floor, the types + parity floor, and the solution the page prints (which must have exactly that
many moves and end in HTR).  The lists are checked a list at a time.

usage: lean_witness.py"""
import json
import os

import numpy as np

import c3
from core import T

B = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(B, "..", "out")
LEAN = os.path.join(B, "..", "..", "lean", "Corners3D", "Corners3D", "Pages.lean")


def row(t, scr, sol=None):
    s = c3.apply(t.mv, 0, scr)
    if sol is None:
        from core import descend
        sol = c3.show(descend(t, s, t.d))
    ks = "".join(str(int(k)) for k in t.kinds[s])
    return f'("{scr}", "{ks}", {int(t.d[s])}, {int(t.q[s])}, {int(t.dg[s])}, {int(t.de[s])}, "{sol}")'


def block(name, doc, rows):
    lines = [f"/-- {doc} -/", f"def {name} : List Example := ["]
    lines += ["  " + r + ("," if i < len(rows) - 1 else "") for i, r in enumerate(rows)]
    lines += ["]", "", f"theorem {name}_ok : {name}.length = {len(rows)} ∧ {name}.all ok = true := by native_decide", ""]
    return lines


def main():
    t = T.load()
    R = json.load(open(os.path.join(OUT, "numbers.json")))
    X = json.load(open(os.path.join(OUT, "extra.json")))
    E = json.load(open(os.path.join(OUT, "examples.json")))
    F = json.load(open(os.path.join(OUT, "figdata.json")))
    out = [
        "/-",
        "  Corners3D.Pages — every scramble the study's pages print, checked on the sticker model (written by",
        "  research/src/lean_witness.py; do not edit by hand).  An example is (scramble, kinds, turns to HTR, quarter",
        "  turns, types floor, types + parity floor, the solution the page prints); `ok` is `witness.check`: the kinds",
        "  are the ones the state shows, the four numbers are the tables', and the solution has exactly that many",
        "  turns and ends in HTR.",
        "-/",
        "import Corners3D.Witness",
        "namespace Corners3D",
        "namespace pages",
        "open witness cube corners",
        "",
        "abbrev Example := String × String × Nat × Nat × Nat × Nat × String",
        "",
        "def ok (e : Example) : Bool := check e.1 e.2.1 e.2.2.1 e.2.2.2.1 e.2.2.2.2.1 e.2.2.2.2.2.1 e.2.2.2.2.2.2",
        "",
    ]
    out += block("COUNT_TABLE", "The count table of section 6.3: for each row, the scramble that meets the move floor.",
                 [row(t, r["witness"], r["witness_sol"]) for r in R["count_table"]])
    out += block("ONLY_TWISTED", "Twisted corners and nothing out (section 6.3).",
                 [row(t, r["witness"], r["sol"]) for r in R["only_twisted"].values()])
    out += block("CATALOGUE", "Every pattern within 3 turns of all good, one per symmetry class (examples page, part 2).",
                 [row(t, r["scramble"]) for r in E["catalogue"]])
    rnd = E["random"]
    for k in range(0, len(rnd), 50):
        out += block(f"RANDOM_{k // 50 + 1}", f"The 200 random states of the examples page, {k + 1} to {k + 50}.",
                     [row(t, e["scramble"], e["solution"]) for e in rnd[k:k + 50]])
    out += block("DR_CASES", "DR corner cases with the all-turn solution the page prints (examples page, part 4).",
                 [row(t, r["scramble"], r["solution"]) for r in E["dr"]])
    low = [w for c in F["cases"] for w in c["witness"].values()]
    out += block("WITHIN_TWO_QT", "The kinds of pattern within two quarter turns of HTR (section 8.4).",
                 [row(t, w["scramble"], w["solution"]) for w in low])
    worked = ["R", "R U", "U R2 U'", "R' U2 R2 F2 R'", "U R2 U F2 U2 R2 U F2 U", "U R2 U2 F2 U R2 U2 F2 U", "U F2 U2 F'",
              X["niss"]["witness_broken"]["scramble"], R["dr"]["witness_save2"]["scramble"]]
    q8 = np.where(t.q == t.q.max())[0]
    from core import scramble
    worked.append(scramble(t, int(q8[np.lexsort((q8, t.dsolved[q8]))[0]])))
    out += block("WORKED", "States used in the text and in the worked examples.", [row(t, s) for s in worked])

    # sequences that are not shortest solutions: they only have to end in HTR, or to solve the corners outright
    out += [
        "/-- `sol`, done after `scr`, solves the corners (not just into HTR). -/",
        "def solves (scr sol : String) : Bool :=",
        "  onlyRUF scr && onlyRUF sol && ofScramble (scr ++ \" \" ++ sol) == ofScramble \"\"",
        "",
    ]
    dr_rows = [f'("{r["scramble"]}", "{r["dr_solution"]}")' for r in E["dr"] if r["dr_solution"]]
    out += ["/-- The DR-only solutions of the examples page end in HTR and use U, R2, F2 only. -/",
            "theorem dr_only_solutions :",
            "    [" + ",\n     ".join(dr_rows) + "].all",
            "      (fun (p : String × String) => reaches p.1 p.2 &&",
            '        (parse p.2).all (fun m => ["U", "U2", "U\'", "R2", "F2"].contains m)) = true := by native_decide',
            ""]
    e8 = X["eight"]
    out += ["/-- The errata's first item: the case, the two 13-move sequences and the 12-move one all solve the corners. -/",
            "theorem wen_case :",
            f'    solves "{e8["wen_case"]}" "{e8["wen_alg"]}" = true ∧',
            f'    solves "{e8["wen_case"]}" "U\' F2 U R2 U2 F2 U R2 U2 F2 U\' F2 U2" = true ∧',
            f'    solves "{e8["wen_case"]}" "{e8["wen_sol"]}" = true ∧',
            f'    (parse "{e8["wen_sol"]}").length = {len(e8["wen_sol"].split())} := by native_decide',
            ""]
    te = X["trigger_examples"]
    out += ["/-- Section 6.6: one turn on the inverse is enough.  The inverse of the scramble, then F, is in HTR, while",
            "the scramble itself is 4 turns away. -/",
            "theorem niss_example :",
            f'    fHTR (ofScramble "{X["niss"]["witness_broken"]["scramble"]}") = {X["niss"]["witness_broken"]["linear"]} ∧',
            f'    inHTR (ofScramble "{c3.show(c3.invert(c3.parse(X["niss"]["witness_broken"]["scramble"])))} F") = true := by native_decide',
            ""]
    del te
    out += ["end pages", "end Corners3D", ""]
    with open(LEAN, "w") as fh:
        fh.write("\n".join(out))
    print("Pages.lean:", sum(1 for line in out if line.startswith("  (")), "examples")


if __name__ == "__main__":
    main()
