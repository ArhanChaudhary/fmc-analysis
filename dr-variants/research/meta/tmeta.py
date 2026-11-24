"""The skeleton/variant meta as a rule on (L; P, S, T, N), and how it is applied to the sample.

A variant is finished when all of these hold, on either side, with the N the bound gives at 2qt:
  * P <= pmax
  * every cap in `caps` (on S, T, N, P+S, S+T, T+N, P+S+T, S+T+N or P+S+T+N)
  * L + P + S + T + max(N, mirror floor) <= G

The mirror floor is the smallest N this side has to cover: with a smaller N the inverse reads the same solution with
fewer early extra moves, so it comes earlier there.  2qt skeleton: (S, T, N) is (N, T, S) on the inverse, floor S.
3qt: (P, S, T, N) is (N, T, S, P), floor P.  4qt: (P, P, S, T, N) is (N, T, S, P, P), floor P - T.  5qt: floor
P - S - T.  6qt: the same without the extra moves of its middle section.

The most-pairs step (`pairs=True`) comes last: among the variants the conditions above let through on one skeleton
(one DR, one side, the same corner cases at every quarter turn) with the same (P, S, T, N), only the ones with the
most pairs right after their last insertion are finished.  Ties are all finished.  `admit` is the rule without that
step, `finish` the rule with it."""
import os
import numpy as np

# What the pairs do in the meta.  'first' (the page): nothing is dropped, among variants with the same (P, S, T, N)
# the ones with more pairs are taken first (torder's key 'pstp').  'drop': a most-pairs step, the less-paired
# variants are not finished (looked at on 23 Nov 2026 and not taken: it misses more, and it makes step 4 lose DRs).
# SVM_PAIRS sets it for a run; every script and `drvar metastd` read the same variable.
PAIRS_MODE = os.environ.get('SVM_PAIRS', 'first')
assert PAIRS_MODE in ('drop', 'first')

def most_pairs(t, mask, N):
    """The most-pairs step on the records: of the masked HTRs, the ones with the most pairs among the masked HTRs on
    the same skeleton with the same (P, S, T, N).  t: tcommon.T; N: the bound's N of every record."""
    assert t.pairs is not None, 'these records have no pair counts (a 48-byte file): run drvar metatuple again'
    idx = np.nonzero(mask)[0]
    out = np.zeros(t.n, bool)
    if not len(idx): return out
    P, S, Tr, Nn = t.P[idx].astype(np.int64), t.S[idx].astype(np.int64), t.T[idx].astype(np.int64), N[idx].astype(np.int64)
    assert min(P.min(), S.min(), Tr.min(), Nn.min()) >= 0 and max(P.max(), S.max(), Tr.max(), Nn.max()) < 32
    g = (((t.skel[idx].astype(np.int64) * 32 + P) * 32 + S) * 32 + Tr) * 32 + Nn
    pr = t.pairs[idx]
    o = np.lexsort((pr, g))
    gs = g[o]
    last = np.r_[gs[1:] != gs[:-1], True]                 # the last of each group has the most pairs
    best = pr[o][last][np.cumsum(np.r_[0, last[:-1]])]
    out[idx[o]] = pr[o] == best
    return out

def quantity(name, P, S, Tr, N):
    return {'S': S, 'T': Tr, 'N': N, 'P+S': P + S, 'S+T': S + Tr, 'T+N': Tr + N, 'P+S+T': P + S + Tr, 'S+T+N': S + Tr + N,
            'P+S+T+N': P + S + Tr + N}[name]

class Rule:
    def __init__(self, caps=None, floor=True, pmax=1, s0=0, label='', only=None, pairs=False):
        """only: a limit on the skeletons gone through, read off the records (not the cells): 'own' = the DR's own
        quarter turns, 'nopair' = no cancelling pair of quarter turns, 'p1own' = an extra move before 2qt only on
        skeletons with the DR's own quarter turns.  pairs: the most-pairs step (in `finish`, not in `admit`)."""
        self.caps = dict(caps or {}); self.floor = floor; self.pmax = pmax; self.s0 = s0; self.label = label; self.only = only
        self.pairs = pairs
    def but(self, **kw):
        d = dict(caps=self.caps, floor=self.floor, pmax=self.pmax, s0=self.s0, label=self.label, only=self.only, pairs=self.pairs); d.update(kw)
        return Rule(**d)
    def text(self):
        parts = [f'P ≤ {self.pmax}' if self.pmax < 9 else 'any P']
        parts += [f'{k} ≤ {v}' for k, v in self.caps.items()]
        if self.s0: parts.append(f'G−L ≥ {self.s0}')
        parts.append('mirror floor' if self.floor else 'no floor')
        if self.pairs: parts.append('most pairs')
        return ', '.join(parts)
    def finish(self, o, N, pairs=None):
        """The HTRs (or cells) the rule finishes: `admit`, then the most-pairs step if the rule has it (`pairs`
        overrides the rule's own switch)."""
        a = self.admit(o, N)
        if not (self.pairs if pairs is None else pairs): return a
        if hasattr(o, 'kt'):                 # cells: see tcells.py
            assert not self.only
            return a & (o.kt <= o.kstar(self.floor))
        return most_pairs(o, a, N)
    def admit(self, o, N):
        """o: tcommon.T (one row per HTR) or tcells.Cells (one row per cell); N: the bound's N for each row."""
        a = (o.P <= self.pmax) & (o.spare >= self.s0)
        fl = np.maximum(N, o.floor) if self.floor else N
        a &= o.P + o.S + o.T + fl <= o.spare
        for k, v in self.caps.items(): a &= quantity(k, o.P, o.S, o.T, N) <= v
        if self.only == 'own': a &= o.qsk == o.m
        elif self.only == 'nopair': a &= ~o.emptymid
        elif self.only == 'p1own': a &= (o.P == 0) | (o.qsk == o.m)
        return a
    def violations(self, o, N):
        """Per row: which conditions fail (dict name -> bool array)."""
        v = {'P': o.P > self.pmax}
        if self.s0: v['spare'] = o.spare < self.s0
        for k, c in self.caps.items(): v[k] = quantity(k, o.P, o.S, o.T, N) > c
        v['goal'] = o.P + o.S + o.T + N > o.spare
        if self.floor: v['floor'] = ~v['goal'] & (o.P + o.S + o.T + np.maximum(N, o.floor) > o.spare)
        return v
