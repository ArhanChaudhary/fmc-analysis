"""Scramble-text features of TNoodle 333fm scrambles.

A TNoodle FMC scramble is  P M P  with P = R' U' F and M = inverse of a min2phase solution of a uniform random state.
min2phase (with premoves) makes M = X h Y with h a run of DR moves on one axis (phase 2), X and Y the phase-1 and
premove parts.  Then  X^-1 . S . Y^-1 = h  is in DR, S = the middle's state: a NISS DR of the middle, normal moves Y^-1,
inverse moves X^-1.  This module reads that split off the text alone (longest run of DR moves of an axis).
"""
import cube

PAD = ["R'", "U'", "F"]
HMOVES = {'UD': lambda t: t[0] in 'UD' or t.endswith('2'),
          'FB': lambda t: t[0] in 'FB' or t.endswith('2'),
          'RL': lambda t: t[0] in 'RL' or t.endswith('2')}

def strip(scr):
    t = cube.parse(scr)
    if len(t) >= 6 and t[:3] == PAD and t[-3:] == PAD:
        return t[3:-3], True
    return t, False

def runs(mid, ax):
    """longest contiguous run of axis-ax DR moves in mid: (start, length)"""
    ok = HMOVES[ax]; best = (0, 0); i = 0
    while i < len(mid):
        if ok(mid[i]):
            j = i
            while j < len(mid) and ok(mid[j]): j += 1
            if j - i > best[1]: best = (i, j - i)
            i = j
        else:
            i += 1
    return best

def all_runs(mid, ax):
    ok = HMOVES[ax]; out = []; i = 0
    while i < len(mid):
        if ok(mid[i]):
            j = i
            while j < len(mid) and ok(mid[j]): j += 1
            out.append((i, j - i)); i = j
        else:
            i += 1
    return out

def text_split(mid):
    """Per axis: the split X h Y with the longest h. Returns dict ax -> (lenX, lenH, lenY)."""
    res = {}
    for ax in cube.AXES:
        s, n = runs(mid, ax)
        res[ax] = (s, n, len(mid) - s - n)
    return res

def text_dr(mid):
    """The text's DR of the middle: axis with the longest DR-move run (ties: shorter total, then UD/FB/RL order).
    Returns (axis, lenX, lenH, lenY, drlen = lenX + lenY)."""
    sp = text_split(mid)
    ax = max(cube.AXES, key=lambda a: (sp[a][1], -cube.AXES.index(a)))
    x, h, y = sp[ax]
    return ax, x, h, y, x + y

def check_dr(mid, ax, x, h):
    """X^-1 S Y^-1 in DR on ax, on the cubie model."""
    X, Y = mid[:x], mid[x + h:]
    st = cube.seq(cube.inv_moves(X) + mid + cube.inv_moves(Y))
    return cube.is_dr(st, ax)
