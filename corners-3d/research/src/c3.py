"""Loader for the tables written by `c3d tables` (research/out/big), and the shared feature definitions.

Places are in the order UFR, UFL, UBR, DFR, UBL, DFL, DBR (DBL is fixed).  Kinds: 0 good, 1 twisted cw,
2 twisted ccw, 3 out with the R/L sticker oriented, 4 out with the U/D sticker oriented, 5 out with the F/B
sticker oriented.  Turns: R R2 R' U U2 U' F F2 F'.
"""
import os
import numpy as np

BIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out", "big")
N = 5040 * 729
PLACES = ["UFR", "UFL", "UBR", "DFR", "UBL", "DFL", "DBR"]
MOVES = ["R", "R2", "R'", "U", "U2", "U'", "F", "F2", "F'"]
AXES = ["R/L", "U/D", "F/B"]
FACE = ["R", "U", "F"]
# which places each turning face holds (x, y, z = +1)
XYZ = np.array([[1, 1, 1], [-1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, -1], [-1, -1, 1], [1, -1, -1]])
ON = [np.where(XYZ[:, a] > 0)[0] for a in range(3)]
TETRAD = XYZ.prod(axis=1) < 0  # True: UFL, UBR, DFR (DBL's tetrad)


def u8(name):
    return np.fromfile(os.path.join(BIG, name + ".u8"), dtype=np.uint8)


def moves():
    return np.fromfile(os.path.join(BIG, "moves.u32"), dtype=np.uint32).reshape(9, N)


def kinds():
    return u8("kinds").reshape(N, 7)


def perm():
    return u8("perm").reshape(N, 7)


def ori():
    return u8("ori").reshape(N, 7)


def parse(seq):
    return [MOVES.index(t.replace("’", "'")) for t in seq.split()]


def show(ms):
    return " ".join(MOVES[m] for m in ms)


def apply(mv, s, seq):
    for m in (parse(seq) if isinstance(seq, str) else seq):
        s = int(mv[m][s])
    return s


def invert(ms):
    return [m - m % 3 + 2 - m % 3 for m in reversed(ms)]
