"""Loaders for the search-meta records: `drvar metarun` writes 40-byte records (.rec), a second 32-byte record per
HTR (.ext) and a TSV of per-DR lines; `drvar metastates` writes 28-byte records of the states on the way."""
import numpy as np, pandas as pd
DT = np.dtype([('dr','<u4'),('pre2','<u4'),('pre1','<u4'),('side','u1'),('q','u1'),('kind','u1'),('len','u1'),('lsk','u1'),
               ('e2','u1'),('e1','u1'),('maxsec','u1'),('total','u1'),('lbc','u1'),('lbr','u1'),('lbt','u1'),('bad','u1'),
               ('csfr','u1'),('pn0','u1'),('pi0','u1'),('pn1','u1'),('pi1','u1'),('pn2','u1'),('pi2','u1'),('keep20','u1'),
               ('keep10','u1'),('keptfin','u1'),('sp0','u1'),('m','u1'),('goal','u1'),('sn0','u1'),('si0','u1')])
assert DT.itemsize == 40
# the second record of each HTR (file .ext, same order): the states with 1, 2 and 3 quarter turns left on its way
DTX = np.dtype([('key2','<u8'),('key3','<u8'),('a1','u1'),('a2','u1'),('a3','u1'),('e3','u1'),('pn3','u1'),('hn1','u1'),('hi1','u1'),
                ('hn2','u1'),('hi2','u1'),('hn3','u1'),('hi3','u1'),('d2n','u1'),('d2i','u1'),('d3n','u1'),('d3i','u1'),('ls2','u1')])
assert DTX.itemsize == 32
# one state on the way (file states{m}.bin, written by `drvar metastates`)
DTS = np.dtype([('dr','<u4'),('key','<u8'),('side','u1'),('q','u1'),('t','u1'),('a','u1'),('e','u1'),('pn','u1'),('hn','u1'),('hi','u1'),
                ('dn','u1'),('di','u1'),('ls','u1'),('cq','u1'),('bc','u1'),('be','u1'),('m','u1'),('goal','u1')])
assert DTS.itemsize == 28
KIND = ["H-H","R-D","F-D","R-V","F-V","D-D"]
LC = np.array([0,1,1,2,2,3])
def load_ext(prefix):
    return np.fromfile(prefix + '.ext', dtype=DTX)
def load_states(m, d=None):
    s = pd.DataFrame(np.fromfile(f'../out/meta/states{m}.bin', dtype=DTS))
    for c in ['a','e','pn','hn','hi','dn','di','ls','cq','bc','be','q','t']: s[c] = s[c].astype(np.int16)
    return s if d is None else s[s.dr.isin(d.index)].reset_index(drop=True)
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
