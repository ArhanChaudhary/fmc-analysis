"""Loader for the search-meta records written by `drvar metarun` (40-byte records + a TSV of per-DR lines)."""
import numpy as np, pandas as pd
DT = np.dtype([('dr','<u4'),('pre2','<u4'),('pre1','<u4'),('side','u1'),('q','u1'),('kind','u1'),('len','u1'),('lsk','u1'),
               ('e2','u1'),('e1','u1'),('maxsec','u1'),('total','u1'),('lbc','u1'),('lbr','u1'),('lbt','u1'),('bad','u1'),
               ('csfr','u1'),('pn0','u1'),('pi0','u1'),('pn1','u1'),('pi1','u1'),('pn2','u1'),('pi2','u1'),('keep20','u1'),
               ('keep10','u1'),('keptfin','u1'),('sp0','u1'),('m','u1'),('goal','u1'),('sn0','u1'),('si0','u1')])
assert DT.itemsize == 40
KIND = ["H-H","R-D","F-D","R-V","F-V","D-D"]
LC = np.array([0,1,1,2,2,3])
def load(prefix):
    r = np.fromfile(prefix + '.rec', dtype=DT)
    D, Q, M = [], [], []
    for l in open(prefix + '.tsv'):
        f = l.rstrip('\n').split('\t')
        if f[0] == 'D': D.append(f[1:])
        elif f[0] == 'Q': Q.append([int(v) for v in f[1:]])
        elif f[0] == 'M': M.append([int(v) for v in f[1:]])
    d = pd.DataFrame(D, columns=['dr','m','goal','ls','subset','lminN','nN','lminI','nI','scramble'])
    for c in ['dr','m','goal','ls','lminN','nN','lminI','nI']: d[c] = d[c].astype(int)
    q = pd.DataFrame(Q, columns=['dr','m','j','npre0','npre1'])
    mm = pd.DataFrame(M, columns=['dr','m','j','pfx','extra','slack','n','ns'])
    return r, d.set_index('dr'), q, mm
