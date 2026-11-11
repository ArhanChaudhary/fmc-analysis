"""The names available inside {= ... =} in the report sources.  Every number in the guide comes through these."""
import sys
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
import pv
from pv import q, q2, tri, quad, pct, share, avg
T = tri
def S(ids): return frozenset(ids.split()) if isinstance(ids, str) else frozenset(ids)
def _ok(h, what):
    assert sum(h) > 0, f'no DR states match: {what}'
    return h
def E(cs, e): return tri(_ok(q(cs=cs, e=e), (cs, e)))
def PR(cs, n, e=None): return tri(_ok(q(cs=cs, e=e, pairs=n), (cs, 'pairs', n, e)))
def HX(cs, x, e=None): return tri(_ok(q(cs=cs, e=e, hmax=x), (cs, 'hmax', x, e)))
def HB(cs, a, b, e=None): return tri(_ok(q(cs=cs, e=e, htr=(a, b)), (cs, 'htr', a, b, e)))
def C1(cs, ids, e=None): return tri(_ok(q(cs=cs, e=e, cc=S(ids)), (cs, 'cc', ids, e)))
def C2(cs, X, Y, e=None): return tri(_ok(q(cs=cs, e=e, both=(S(X), S(Y))), (cs, 'both', X, Y, e)))
def SH(cs, h): return f'{100 * sum(h) / sum(q(cs=cs)):.0f}%'
def _pairs(cs):
    ids = sorted(pv.cases(cs), key=int); out = []
    for i, a in enumerate(ids):
        for b in ids[i:]:
            h = q(cs=cs, both=({a}, {b}))
            if sum(h): out.append((avg(h), h))
    out.sort(key=lambda t: t[0]); return out
def XPH(cs, which): return _pairs(cs)[0 if which == 'best' else -1][1]
def KEEP(cs, keep_if, T):
    """Share of the finishes in T that survive when only DRs whose shorter HTR satisfies keep_if are kept."""
    kept = q(cs=cs, hmin=keep_if); allh = q(cs=cs)
    return f'{100 * sum(kept[:T + 1]) / sum(allh[:T + 1]):.0f}%'
def XP(cs, which): return tri(_pairs(cs)[0 if which == 'best' else -1][1])
def XPS(cs, which): return SH(cs, _pairs(cs)[0 if which == 'best' else -1][1])
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
