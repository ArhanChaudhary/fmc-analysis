#!/usr/bin/env python3
"""Replay everything the pages print, on a model that shares no code with the tables (fullcorners.py: eight
corners as vectors, stickers tracked one by one).

For every scramble with a solution: the solution must end in the half-turn group and have the stated length.
For every scramble with a types line: the types read off the stickers must match.

usage: verify_pages.py"""
import json
import os

import fullcorners as fc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")
ORDER = ["UFR", "UFL", "UBL", "UBR", "DFR", "DFL", "DBR"]
XYZ = {"UFR": (1, 1, 1), "UFL": (-1, 1, 1), "UBL": (-1, 1, -1), "UBR": (1, 1, -1), "DFR": (1, -1, 1),
       "DFL": (-1, -1, 1), "DBR": (1, -1, -1)}


def half_turn_group():
    start = fc.key(fc.solved())
    seen = {start: fc.solved()}
    stack = [fc.solved()]
    while stack:
        s = stack.pop()
        for m in ("R2", "U2", "F2"):
            t = fc.turn(s, m)
            if fc.key(t) not in seen:
                seen[fc.key(t)] = t
                stack.append(t)
    return set(seen)


HTR = half_turn_group()
assert len(HTR) == 24


def types(state):
    """The types line, read off the stickers: for each place, the corner there and how many of its three
    stickers face along their own axis."""
    at = {v[0]: (piece, v[1]) for piece, v in state.items()}
    out = []
    for name in ORDER:
        piece, facing = at[XYZ[name]]
        oriented = [facing[a][a] != 0 for a in range(3)]
        n = sum(oriented)
        if n == 3:
            out.append(".")
        elif n == 1:
            out.append("ruf"[oriented.index(True)])
        else:
            assert n == 0, "two oriented stickers can't happen"
            # twisted: where is the U/D sticker, and which way round the corner is that from the U/D face
            p = XYZ[name]
            ud_axis = next(a for a in range(3) if facing[1][a] != 0)
            clockwise = [1, 0, 2] if p[0] * p[1] * p[2] > 0 else [1, 2, 0]
            out.append("+" if clockwise.index(ud_axis) == 1 else "-")
        same = (piece[0] * piece[1] * piece[2]) == (XYZ[name][0] * XYZ[name][1] * XYZ[name][2])
        assert same == (n != 1), "tetrad and sticker count must agree"
    return " ".join(out)


def check(scr, sol=None, length=None, kinds=None, where=""):
    s = fc.apply(scr)
    if kinds is not None:
        assert types(s) == kinds, (where, scr, types(s), kinds)
    if sol is not None:
        assert fc.key(fc.apply(sol, s)) in HTR, (where, scr, sol)
        if length is not None:
            assert len(sol.split()) == length, (where, scr, sol, length)
    return 1


def main():
    R = json.load(open(os.path.join(OUT, "numbers.json")))
    X = json.load(open(os.path.join(OUT, "extra.json")))
    E = json.load(open(os.path.join(OUT, "examples.json")))
    F = json.load(open(os.path.join(OUT, "figdata.json")))
    n = 0
    for r in R["count_table"]:
        n += check(r["witness"], r["witness_sol"], r["floor_d"], r["witness_kinds"], "count table")
        n += check(r["witness_q"], r["witness_q_sol"], None, None, "count table qt")
    for r in R["only_twisted"].values():
        n += check(r["witness"], r["sol"], r["min_d"], None, "only twisted")
    w = R["dr"]["witness_save2"]
    n += check(w["scramble"], w["sol"], w["all"], w["kinds"], "dr witness")
    for e in E["random"]:
        n += check(e["scramble"], e["solution"], e["d"], e["kinds"], "random")
        # the way to all good really makes every corner good
        s = fc.apply(e["scramble"] + " " + e["types_solution"])
        assert types(s) == ". . . . . . .", ("types solution", e["scramble"])
        assert (fc.key(s) in HTR) == (e["types_solution_ends"] == 0)
    for r in E["catalogue"]:
        for way in r["ways"]:
            s = fc.apply(r["scramble"] + " " + way)
            assert types(s) == ". . . . . . .", ("catalogue", r["scramble"], way)
            assert len(way.split()) == r["floor"]
        n += check(r["scramble"], None, None, r["kinds"], "catalogue")
    for r in E["dr"]:
        n += check(r["scramble"], r["solution"], r["all"], r["kinds"], "dr")
        n += check(r["scramble"], r["dr_solution"], r["dr_only"], None, "dr in DR turns")
        assert all(m in ("U", "U2", "U'", "R2", "F2") for m in r["dr_solution"].split())
    for c in F["cases"]:
        for w in c["witness"].values():
            n += check(w["scramble"], w["solution"], w["d"], w["kinds"], "low cases")
    wb = X["niss"]["witness_broken"]
    n += check(wb["scramble"], None, None, wb["kinds"], "niss witness")
    assert fc.key(fc.apply(wb["scramble"])) not in HTR
    # the errata's sequences
    e8 = X["eight"]
    st = fc.apply(e8["wen_case"])
    for seq in (e8["wen_alg"], e8["wen_sol"], "U' F2 U R2 U2 F2 U R2 U2 F2 U' F2 U2", "D2 F2 U' F' D F' R2 B U' B' D'"):
        assert fc.key(fc.apply(seq, st)) == fc.key(fc.solved()), seq
    assert fc.key(fc.apply(e8["thirteen_sol"], fc.apply(e8["thirteen_scramble"]))) == fc.key(fc.solved())
    print("replayed", n, "scrambles: every solution ends in HTR with the stated length, every types line matches the stickers")


if __name__ == "__main__":
    main()
