"""Section accounting against the skeleton's own section lengths (the solver's reading): a variant's section extra =
(its section length) - (the skeleton's length of that section).  Skeleton splits come from `drvar metasplit`
(../out/meta/split{M}.tsv: every shortest corner path's moves up to its states with 1, 2, 3 quarter turns left).
When a skeleton has several shortest corner paths, a variant is read against the one that gives it the fewest early
moves (the part the inverse would mirror: S on 2qt skeletons, pre-2qt on 3-5qt, the first three sections on 6qt),
among the paths it fits with no section below zero.  Reading the inverse the same way gives the mirror image."""
import numpy as np, pandas as pd

def load_splits(m):
    rows = []
    for l in open(f'../out/meta/split{m}.tsv'):
        f = l.rstrip('\n').split('\t')
        dr, side, q, kind = map(int, f[:4])
        key = ((dr * 2 + side) * 8 + q) * 8 + kind
        for o, s in enumerate(f[5:]):
            k1, k2, k3 = map(int, s.split(','))
            rows.append((key, o, k1, k2, k3))
    return pd.DataFrame(rows, columns=['key', 'opt', 'K1', 'K2', 'K3'])

def skel_acct(m, dr, side, q, kind, a1, a2, a3, ex):
    """Returns pre, S, T, c3 (extras by the state with 3 quarter turns left) and `fits` (some split fits)."""
    sp = load_splits(m)
    key = ((dr.astype(np.int64) * 2 + side) * 8 + q) * 8 + kind
    q = q.astype(np.int16); ex = ex.astype(np.int16)
    a1 = a1.astype(np.int16); a2 = a2.astype(np.int16); a3 = a3.astype(np.int16)
    n = len(key)
    best = dict(pre=np.zeros(n, np.int16), S=np.zeros(n, np.int16), T=np.zeros(n, np.int16), c3=np.zeros(n, np.int16))
    be = np.full(n, 999, np.int16); bS = np.full(n, 999, np.int16); fits = np.zeros(n, bool)
    for o in range(sp.opt.max() + 1):
        t = sp[sp.opt == o].set_index('key')
        K = t[['K1', 'K2', 'K3']].reindex(key).values
        has = ~np.isnan(K[:, 0])
        K = np.nan_to_num(K, nan=0).astype(np.int16)
        c1 = a1 - K[:, 0]
        c2 = np.where(q >= 3, a2 - K[:, 1], 0).astype(np.int16)
        c3 = np.where(q >= 4, a3 - K[:, 2], 0).astype(np.int16)
        S = c1 - c2; T = ex - c1
        ok = has & (c3 >= 0) & (c2 - c3 >= 0) & (S >= 0) & (T >= 0)
        early = np.where(q == 2, S, np.where(q == 6, c3, c2)).astype(np.int16)
        take = ok & ((early < be) | ((early == be) & (S < bS)))
        be[take] = early[take]; bS[take] = S[take]; fits |= ok
        for nm, v in (('pre', c2), ('S', S), ('T', T), ('c3', c3)):
            best[nm][take] = v[take]
    return best['pre'], best['S'], best['T'], best['c3'], fits
