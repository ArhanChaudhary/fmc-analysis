"""Reader of `drvar metastd` (../out/meta/std{M}.tsv), and its checks against the page's records.

The file has, for every DR of the sample, the within-goal solutions either meta reaches, by a search of its own: each
solution with its class on normal and on inverse and in the premove pass of each side (q, L, P, S, T, ...), and its
moves to HTR in the ways of the standard meta (on normal, on inverse, with one NISS after a start of 1 to 3 moves); and
per DR the best total within each cap on the moves to HTR, by the number of moves before the NISS.

The comparison of the two caps (tord.py) is counted on the records.  This file is what it is checked against, and
where the examples' solutions come from (mkstd.py).  Whether the skeleton/variant meta finishes a class is worked out
here from its (L; P, S, T) under RULE (P <= 1 and P+S+T <= 5; no step 4, no bound), whatever rule the file was written
with.

usage: tstd.py [M ...]   (the checks alone)"""
import json, sys
import numpy as np, pandas as pd
from tcommon import drs, ORDER, BYQT, T, NDRS, path as tpath
from tmeta import Rule

RULE = Rule(caps={'P+S+T': 5}, floor=False, pmax=1)        # the skeleton/variant side of the comparison

CAPS = list(range(7, 15))
PRE = 3                    # the most moves before the NISS
LEVELS = list(range(PRE + 1))
DCOLS = ['dr', 'm', 'goal', 'ls', 'nadm', 'nadm_ok', 'svbest', 'b0', 'b1', 'b2', 'b3', 'b4', 'nsol', 'nsv', 'nstd']
SCOLS = ['dr', 'len', 'sv', 'cn', 'ci', 'readn', 'readi', 'mv', 'pn', 'pi', 'n1', 'n2', 'n3', 'i1', 'i2', 'i3', 'q', 'sol']
MV = ['mN', 'mI', 'mN1', 'mN2', 'mN3', 'mI1', 'mI2', 'mI3']      # moves to HTR: normal, inverse, NISS after k moves on normal / on inverse

def num(v): return 255 if v == '-' else int(v)

def load(m, path=None):
    D, S = [], []
    for l in open(path or tpath(f'std{m}.tsv')):
        if l[0] == '#': continue
        f = l.rstrip('\n').split('\t')
        (D if f[0] == 'D' else S).append(f[1:])
    d = pd.DataFrame(D, columns=DCOLS)
    for c in ['dr', 'm', 'goal', 'ls', 'nadm', 'nadm_ok', 'nsol', 'nsv']: d[c] = d[c].astype(int)
    d['svbest'] = d.svbest.map(num)
    for j, c in enumerate(CAPS):
        for L in LEVELS + [PRE + 1]:        # best total within cap c with a NISS after at most L moves (PRE + 1: the extra starts too)
            d[f'std{L}_{c}'] = d[f'b{L}'].map(lambda v: num(v.split(',')[j]))
        d[f'std{c}'] = d[f'std{PRE}_{c}']; d[f'one{c}'] = d[f'std0_{c}']
    d = d.set_index('dr')
    has_pass = bool(S) and len(S[0]) == len(SCOLS) + 2
    s = pd.DataFrame(S, columns=SCOLS + (['rn', 'ri'] if has_pass else []))
    if not has_pass: s['rn'] = '-'; s['ri'] = '-'
    s.attrs['has_pass'] = has_pass
    for c in ['dr', 'len', 'sv', 'pn', 'pi', 'q']: s[c] = s[c].astype(int)
    mv = np.array([[num(x) for x in v.split(',')] for v in s.mv]).reshape(len(s), len(MV))
    for j, k in enumerate(MV): s[k] = mv[:, j]
    # fewest moves to HTR with a NISS after at most L moves
    s['lev0'] = mv[:, :2].min(axis=1)
    for L in range(1, PRE + 1): s[f'lev{L}'] = np.minimum(s[f'lev{L - 1}'], np.minimum(s[f'mN{L}'], s[f'mI{L}']))
    s['std'] = s[f'lev{PRE}']; s['one'] = s['lev0']
    # the skeleton/variant meta reaches a solution when it finishes its class on a side or in the premove pass
    fin = lambda v: bool((cls(v) or {}).get('fin'))
    s['sv_full'] = (s.cn.map(fin) | s.ci.map(fin)).astype(int)
    s['sv'] = (s.sv_full.astype(bool) | s.rn.map(fin) | s.ri.map(fin)).astype(int)
    best = s[s.sv == 1].groupby('dr')['len'].min()
    d['svbest'] = best.reindex(d.index).fillna(255).astype(int)
    d['sv_found'] = d.svbest < 255
    return d, s

def cls(txt):
    """A class of the skeleton/variant meta as the tool prints it, or None.  `fin`: finished under RULE (an HTR the
    tool lists already has L+P+S+T within the goal, which the main part checks)."""
    if txt == '-': return None
    f = list(map(int, txt.split(',')))
    if len(f) == 9: f += [None, f[7]]          # a file from before the pair counts (the extra-starts check files)
    q, L, P, S, Tr, nb, fl, _adm, total, pairs, _fin = f
    ok = P <= RULE.pmax and P + S + Tr <= RULE.caps['P+S+T']
    return dict(q=q, L=L, P=P, S=S, T=Tr, nb=nb, floor=fl, adm=ok, total=total, pairs=pairs, fin=ok)

def checks(m, t=None):
    """The file against the records (tcommon.T with the premove pass, no step 4).  Returns (d, s, differ): the D and S
    lines of the sample's DRs (0c0 left out), and per cap the DRs where the standard meta's own search on normal and
    inverse has a better within-goal total than the records' HTRs within that cap (the records stop at two more
    quarter turns than the DR)."""
    d, s = load(m)
    info = drs(m)
    if NDRS:                                         # a test run on the first DRs of the sample
        info = info[info.index < NDRS]; d = d[d.index < NDRS]; s = s[s.dr < NDRS]
    keep = info.index[info.case != '0c0']
    g = int(info.goal.iloc[0])
    assert (d.ls == info.ls.reindex(d.index)).all(), 'not the same DRs as the sample'
    assert s.attrs['has_pass'], 'a file from before the premove pass'
    # every class the tool lists has L+P+S+T within the goal, so RULE is the two caps alone
    for col in ('cn', 'ci', 'rn', 'ri'):
        for v in s[col].unique():
            c = cls(v)
            assert c is None or c['P'] + c['S'] + c['T'] <= g - c['L'], (col, v)
    if t is None: t = T(m, uniss='add', rest_floor=False)
    # the skeleton/variant side against the records under the same rule: the same DRs found, with the same best solution
    a = RULE.admit(t, np.zeros(t.n, np.int16))
    best = np.full(t.ndr, 255); k = a & t.ok; np.minimum.at(best, t.dr[k], t.total[k])
    assert (best[keep] == d.svbest.reindex(keep).values).all(), 'the solutions and the records disagree on the skeleton/variant side'
    assert (t.found(a)[keep] == d.sv_found.reindex(keep).values).all()
    full = ~t.pre
    differ = {}
    for c in CAPS:
        # the standard meta on normal and inverse against the records: best total among the HTRs within the cap
        k = full & (t.wl <= c)
        best = np.full(t.ndr, 255); np.minimum.at(best, t.dr[k], t.total[k])
        best = np.where(best <= g, best, 255)[keep]
        mine = d[f'one{c}'].reindex(keep).values
        assert (mine <= best).all(), 'the standard meta misses an HTR of the records'
        differ[c] = keep[mine < best]
        # the premove pass is a NISS after one move (a quarter turn): its HTRs, premove counted, are in the standard
        # meta's reach with a NISS after 1 move
        k = t.pre & (t.wl <= c)
        best = np.full(t.ndr, 255); np.minimum.at(best, t.dr[k], t.total[k])
        best = np.where(best <= g, best, 255)[keep]
        assert (d[f'std1_{c}'].reindex(keep).values <= best).all(), 'the standard meta with a NISS after 1 move misses an HTR of the premove pass'
    d = d.loc[keep].copy(); d['case'] = info.case.reindex(keep); d['wg'] = info.wg.reindex(keep)
    assert (d.wg == (d.ls <= g)).all()
    s = s[s.dr.isin(keep)].copy(); s['case'] = info.case.reindex(s.dr.values).values
    # every solution whose path on a side is a class of the records must be in the standard meta's reach there
    for side, col in (('pn', 'mN'), ('pi', 'mI')):
        bad = s[(s[col] > s[side]) & (s['cn' if side == 'pn' else 'ci'] != '-')]
        assert not len(bad), f'{len(bad)} solutions not reached on their own path'
    # for every DR, cap and number of moves before the NISS: "a within-goal solution in reach" is the same from the
    # HTRs (the D lines) and from the list of solutions; and the extra starts are not in these files
    for L in LEVELS:
        low = s.groupby('dr')[f'lev{L}'].min().reindex(d.index).fillna(255)
        for c in CAPS:
            assert ((d[f'std{L}_{c}'] <= g) == (low <= c)).all(), (m, L, c)
            assert (d[f'std{PRE + 1}_{c}'] == d[f'std{PRE}_{c}']).all()
    return d, s, differ

if __name__ == '__main__':
    for m in [int(a) for a in sys.argv[1:]] or [2, 3, 4]:
        d, s, differ = checks(m)
        print(m, len(d), 'DRs,', len(s), 'solutions: the skeleton/variant side is the records\'; own search better than the records within the cap:',
              {c: len(v) for c, v in differ.items()}, flush=True)
