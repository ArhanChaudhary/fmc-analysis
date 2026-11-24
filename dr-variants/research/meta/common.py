"""Shared helpers for the search-meta analysis."""
import numpy as np, pandas as pd
from math import comb
from load import *

def frame(m, pref=None, ext=False):
    r, d, q, mm = load(pref or f'../out/meta/run{m}')
    df = pd.DataFrame(r)
    if ext:
        x = load_ext(pref or f'../out/meta/run{m}')
        assert len(x) == len(df)
        for c in x.dtype.names: df[c] = x[c] if c.startswith('key') else x[c].astype(np.int16)
    # a 2qt DR is a 4a2 or 4b2: drop the few states whose corners are 0c0 up to a turn of both layers
    # (two quarter turns in the fixed frame, but a 0qt corner case to a solver)
    keep = ~d.subset.str.startswith('0c0')
    if not keep.all():
        d = d[keep].copy(); df = df[df.dr.isin(d.index)].reset_index(drop=True)
    g = int(d.goal.iloc[0])
    for c in ['len','lsk','e2','e1','total','lbc','lbr','lbt','q','m','pn0','pn1','pn2','keep20','keep10','maxsec','bad','kind']:
        df[c] = df[c].astype(np.int16)
    df['ex'] = df.len - df.lsk                 # S + T: extra moves before HTR
    df['S'] = df.e1 - df.e2                    # extra moves of the setup section (2qt -> 1qt)
    df['T'] = df.ex - df.e1                    # extra moves of the trigger section (1qt -> HTR)
    df['cs'] = g - df.lbc                      # corner slack
    df['rs'] = g - df.lbr                      # rule slack
    df['ts'] = g - df.lbt                      # table slack
    df['nr'] = df.lbr - df.lbc                 # rule penalty
    df['ok'] = df.total <= g
    df['dq'] = df.q - df.m
    df['M'] = g - df.lsk - LC[df.kind.values]  # the skeleton's maximum penalty
    d['solv'] = d.ls <= g
    return df, d, q, mm, g

def first_hit(n, s, K):
    """Chance that the first K draws without replacement from n items with s successes hold a success."""
    if s == 0 or K <= 0: return 0.0
    K = min(K, n)
    if K > n - s: return 1.0
    return 1.0 - comb(n - s, K) / comb(n, K)

def policy(df, d, mask, keys, Ks=(5, 10, 20, 40, 80, 160)):
    """Order the masked variants of each DR by `keys` (ascending, ties in random order).
    Returns per solvable DR: expected number of HTRs finished until the first within-goal one (inf if none),
    and the chance of having found one within K finishes; and per DR the number of variants in the mask."""
    s = df[mask]
    grp = s.groupby(['dr'] + keys, sort=True).agg(n=('ok', 'size'), s=('ok', 'sum')).reset_index()
    out = {}
    tot = grp.groupby('dr').n.sum()
    for dr, gg in grp.groupby('dr'):
        n = gg.n.values; sc = gg.s.values
        hit = np.nonzero(sc)[0]
        if len(hit) == 0:
            out[dr] = (np.inf, [0.0] * len(Ks)); continue
        i = hit[0]; before = n[:i].sum()
        exp = before + (n[i] + 1) / (sc[i] + 1)
        out[dr] = (exp, [first_hit(int(n[i]), int(sc[i]), K - int(before)) for K in Ks])
    sol = d.index[d.solv]
    exp = np.array([out.get(i, (np.inf, None))[0] for i in sol])
    rec = np.array([out[i][1] if i in out else [0.0] * len(Ks) for i in sol])
    return dict(found=np.isfinite(exp).mean(), median=np.median(exp), mean_found=exp[np.isfinite(exp)].mean() if np.isfinite(exp).any() else np.nan,
                recall={K: rec[:, j].mean() for j, K in enumerate(Ks)}, size_all=tot.reindex(d.index).fillna(0).mean(),
                size_unsolv=tot.reindex(d.index[~d.solv]).fillna(0).mean(), exp=pd.Series(exp, index=sol))
