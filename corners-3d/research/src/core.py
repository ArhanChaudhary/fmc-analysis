"""Shared tables and small helpers for the analysis, the figures and the examples.

Everything is loaded once into the class `T`.  Names used throughout:

    d       moves to HTR (HTM, all nine turns)                 q      quarter turns to HTR, half turns free
    dg, qg  the same to "all good" (the types floor)           de, qe the same to the even half of "all good"
    dp, qp  the same for the placement alone (twists ignored)
    kinds   N x 7, the kind of the corner at each place        pid    the seven kinds as one number
    par     0 even / 1 odd                                     col    N x 3 colour pictures (7 bits each)
"""
import os

import numpy as np

import c3

N = c3.N
# the order corners are printed in: U layer from UFR the way a U turn carries them, then the D layer
SHOW = [0, 1, 4, 2, 3, 5, 6]
SHOW_NAMES = [c3.PLACES[p] for p in SHOW]
LETTER = ".+-ruf"          # good, twisted cw, twisted ccw, out with the R/L, U/D, F/B sticker oriented
A_FREE = [1, 2, 3]         # UFL, UBR, DFR: DBL's tetrad
B_PLACES = [0, 4, 5, 6]    # UFR, UBL, DFL, DBR


class T:
    """All tables, loaded on first use."""

    _loaded = False

    @classmethod
    def load(cls):
        if cls._loaded:
            return cls
        cls.mv = c3.moves()
        cls.kinds = c3.kinds()
        cls.P = c3.perm()
        cls.O = c3.ori()
        cls.d = c3.u8("d_htr")
        cls.q = c3.u8("qt_htr")
        cls.qtm = c3.u8("qtm_htr")
        cls.dsolved = c3.u8("d_solved")
        cls.dg = c3.u8("d_good")
        cls.qg = c3.u8("qt_good")
        cls.de = c3.u8("d_goodeven")
        cls.qe = c3.u8("qt_goodeven")
        cls.dtet = c3.u8("d_tet")
        cls.dco = np.stack([c3.u8("d_co_" + a) for a in "xyz"], 1)
        for name in ("parity", "inverse", "pid", "cls", "colour", "dperm", "qperm", "ddr", "qdr", "staged", "sym"):
            setattr(cls, name, np.load(os.path.join(c3.BIG, name + ".npy")))
        cls.par = cls.parity
        cls.col = cls.colour
        cls.dp = cls.dperm
        cls.qp = cls.qperm
        k = cls.kinds
        cls.nT = ((k == 1) | (k == 2)).sum(1)
        cls.nX = (k >= 3).sum(1)
        cls.xa = np.stack([(k == 3 + a).sum(1) for a in range(3)], 1)
        cls.xs = np.sort(cls.xa, 1)[:, ::-1]
        cls.W = cls.nX + 2 * cls.nT
        cls.closer = np.stack([cls.d[cls.mv[m]] < cls.d for m in range(9)], 1)
        cls._loaded = True
        return cls


def kinds_text(row):
    """The seven kinds in printing order, e.g. 'r . . r r . r' after the turn R."""
    return " ".join(LETTER[row[p]] for p in SHOW)


def scramble(t, s):
    """A shortest sequence of turns that makes state s from solved (the inverse of a shortest solution)."""
    out = []
    while t.dsolved[s] > 0:
        for m in range(9):
            n = int(t.mv[m][s])
            if t.dsolved[n] < t.dsolved[s]:
                out.append(m)
                s = n
                break
    return c3.show(c3.invert(out))


def descend(t, s, table):
    """One shortest way down `table` from state s to 0, as a list of turns."""
    out = []
    while table[s] > 0:
        for m in range(9):
            n = int(t.mv[m][s])
            if table[n] < table[s]:
                out.append(m)
                s = n
                break
        else:
            raise ValueError("no way down")
    return out


def all_shortest(t, s, table, limit=200):
    """Every shortest way down `table` from s (up to `limit` of them)."""
    out = []

    def go(x, acc):
        if len(out) >= limit:
            return
        if table[x] == 0:
            out.append(list(acc))
            return
        for m in range(9):
            n = int(t.mv[m][x])
            if table[n] < table[x]:
                acc.append(m)
                go(n, acc)
                acc.pop()

    go(s, [])
    return out


def quarters(ms):
    return sum(1 for m in ms if m % 3 != 1)


def shape_names(t):
    """The tetrad shape of the out corners of every state: '0c', '2c', '4a', '4b' or '6c'.

    The out corners sit on a set of places; half turns carry such sets round.  Four out corners come in two
    kinds of set: 6 of them form the smaller family (4a: a whole face, or two parallel diagonals on opposite
    faces), 12 the larger (4b)."""
    k = t.kinds
    mask = np.zeros(N, dtype=np.int64)
    for p in range(7):
        mask |= (k[:, p] >= 3).astype(np.int64) << p
    # orbits of masks under half turns: read them off the states themselves
    lab = mask.copy()
    changed = True
    while changed:
        changed = False
        for m in (1, 4, 7):
            new = np.minimum(lab, lab[t.mv[m]])
            if (new != lab).any():
                lab, changed = new, True
    names = np.empty(N, dtype="U2")
    for orbit in np.unique(lab):
        members = np.unique(mask[lab == orbit])
        n = bin(int(members[0])).count("1")
        if n == 4:
            name = "4a" if len(members) == 6 else "4b"
            assert len(members) in (6, 12)
        else:
            name = f"{n}c"
        names[lab == orbit] = name
    return names


def colour_text(bits):
    """The places of a colour picture, e.g. 'DFR DFL DBR' (DBL always has the colour too)."""
    return " ".join(c3.PLACES[p] for p in SHOW if bits >> p & 1)


def pct(x, digits=1):
    return f"{100 * x:.{digits}f}%"
