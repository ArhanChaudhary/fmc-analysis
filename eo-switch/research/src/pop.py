#!/usr/bin/env python3
"""Targets (per coset, as probabilities) and populations (per coset weights) shared by the analysis scripts.

Targets, for a coset s of a uniformly random F/B-EO-solved cube (k = 5, 6, 7):
  plain     d(s) <= k (EO-kept, linear, one DR axis)
  lastF     min(d(s), d(s.F2)) <= k   (the EO's last turn, an F quarter turn, either way; B gives the same numbers)
  lastFB    min over s, s.F2, s.B2, s.F2.B2 (EO ending F B, both turns free)
  two       better of the two DR axes (U/D, R/L) of the same cube: 1 - [d > k] (1 - P(d_RL <= k | s))  (exact;
            eoswtools twoaxis)
  inv       better of normal and inverse: 1 - [d > k] (1 - P(d(s^-1) <= k | s)); given s, the inverse is uniform over
            the cosets with the two twist counts exchanged and the same number of E pieces out (shown in SUMMARY), so
            P(d(s^-1) <= k | s) is a class average.
Populations (weights over the cosets of the state the rule is read on, i.e. the state after the switch):
  P1        uniform
  P2_L      switched state of an RZP of length L (L = 1..6) reached from a uniform EO-solved state (eoswtools rzp,
            exact): the switched state is uniform within its class (twist counts exchanged, edges), so its weight is
            the class total of the RZP weights spread evenly.  P2n_L: the RZP's own end state (no switch).
  P3_L      sampled attempts at total length L = 5, 6 (eoswtools att): counts of switched states per coset."""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import geom
from geom import N0, N_SL, N_CO
BIG = os.path.join(HERE, '..', 'out', 'big'); OUT = os.path.join(HERE, '..', 'out')

_cache = {}
def feat():
    if 'F' not in _cache: _cache['F'] = dict(np.load(os.path.join(BIG, 'feat.npz')))
    return _cache['F']

def cls_key(F, swap=False):
    """Class of a coset: (twists 1, twists 2, E pieces out); swap exchanges the two twist counts."""
    t1, t2 = F['tw1'].astype(np.int64), F['tw2'].astype(np.int64)
    if swap: t1, t2 = t2, t1
    return (t1 * 9 + t2) * 5 + F['drm_e'].astype(np.int64) // 2
def class_mean(F, x, swap):
    """For each coset s: mean of x over the class of s (swap: over the class with the twist counts exchanged)."""
    k0 = cls_key(F); k1 = cls_key(F, swap)
    tot = np.bincount(k0, weights=x, minlength=405); cnt = np.bincount(k0, minlength=405)
    with np.errstate(invalid='ignore', divide='ignore'): m = tot / cnt
    return m[k1]

def targets(k):
    F = feat(); d = F['d'].astype(np.int64)
    if ('T', k) in _cache: return _cache[('T', k)]
    T = {}
    T['plain'] = (d <= k).astype(float)
    ix = np.arange(N0)
    dF = d[geom.move_ix(ix, geom.NAMES.index('F2'))]; dB = d[geom.move_ix(ix, geom.NAMES.index('B2'))]
    dFB = d[geom.move_ix(geom.move_ix(ix, geom.NAMES.index('F2')), geom.NAMES.index('B2'))]
    T['lastF'] = (np.minimum(d, dF) <= k).astype(float)
    T['lastB'] = (np.minimum(d, dB) <= k).astype(float)
    T['lastFB'] = (np.minimum.reduce([d, dF, dB, dFB]) <= k).astype(float)
    if k in (4, 5, 6, 7, 8):
        prl = np.fromfile(os.path.join(BIG, 'p_rl.u32'), dtype='<u4').reshape(5, N0)[k - 4] / 2822400.0
        T['p_rl'] = prl
        T['two'] = 1 - (d > k) * (1 - prl)
    pinv = class_mean(F, (d <= k).astype(float), swap=True)
    T['p_inv'] = pinv
    T['inv'] = 1 - (d > k) * (1 - pinv)
    _cache[('T', k)] = T
    return T

def rzp_w():
    if 'W' not in _cache:
        _cache['W'] = np.fromfile(os.path.join(BIG, 'rzp_w.u64'), dtype='<u8').reshape(7, N0).astype(float)
    return _cache['W']

def populations():
    """Weights per coset of the switched state, normalised per DRM later by the user of the weights."""
    if 'P' in _cache: return _cache['P']
    F = feat(); W = rzp_w(); P = {'P1': np.ones(N0)}
    k0 = cls_key(F); cnt = np.bincount(k0, minlength=405)
    for L in range(1, 7):
        P[f'P2n_{L}'] = W[L]
        tot = np.bincount(k0, weights=W[L], minlength=405)
        # switched state of an RZP end state in class c is uniform over class swap(c)
        ksw = cls_key(F, swap=True)    # class whose swap is the class of s
        with np.errstate(invalid='ignore', divide='ignore'):
            P[f'P2_{L}'] = np.nan_to_num(tot[ksw] / cnt[k0])
    att = os.path.join(BIG, 'att_counts.u32')
    if os.path.exists(att):
        A = np.fromfile(att, dtype='<u4').reshape(3, 11, N0).astype(float)
        for li, L in enumerate((4, 5, 6)):
            P[f'P3_{L}'] = A[li, 0]; P[f'P3n_{L}'] = A[li, 1]
            for j, nm in enumerate(['alt5', 'alt6', 'alt7', 'two5', 'two6', 'two7', 'all5', 'all6', 'all7']):
                P[f'P3_{L}_{nm}'] = A[li, 2 + j]
    _cache['P'] = P
    return P

DRMS_NAMED = [(4, 4), (4, 2), (3, 2), (7, 8), (8, 8), (4, 6), (3, 4), (3, 6), (5, 4), (5, 6), (6, 6), (2, 2)]
def drm_mask(c, e):
    F = feat(); return (F['drm_c'] == c) & (F['drm_e'] == e)
def drm_name(c, e): return f'{c}c{e}e'
