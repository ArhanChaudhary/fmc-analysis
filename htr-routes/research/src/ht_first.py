#!/usr/bin/env python3
"""Half turns before the first quarter turn: loading, the per-state reads a solver can make, and the tables.

Input: out/big/htfirst/htfirst.tsv (research/htfirst, `htfirst run`: per sampled state and side, the fewest half turns
before the first quarter turn over every optimal finish and over every finish within optimal + 1) and
out/big/htfirst/tables.json (`htfirst tables`: coordinate and coset tables of the shared model).

Columns of htfirst.tsv used here
  a0n / a0i   fewest half turns (U2 D2 R2 L2 F2 B2 all count) before the first quarter turn of an optimal finish,
              read on normal / on inverse; 99 = no optimal finish has a quarter turn
  a1n / a1i   the same over finishes of at most optimal + 1 moves
  b0n ...     the same counting only R2 L2 F2 B2
  noqt0/1     some optimal (some finish within +1) has no quarter turn at all
  ccn / cci   corner coset on normal / inverse;  epn / epi  edge pattern on normal / inverse

Reads computed here (all from the piece positions, per side)
  sC      corner setup: fewest half turns before some U or D quarter turn lowers the corners' quarter-turn count
  sF      full setup: the same for the quarter-turn count of corners and edges together (fewest quarter turns of any
          sequence reaching HTR), the first study's "s"
  case    the first study's corner case (46 cases; names as in its Appendix E)
  split   bad corners / bad edges per layer in the frame with at most 4 bad corners
  pairs   true corner-edge pairs in the U and D layers; slice pairs; E-slice edges solved
"""
import os, sys, csv, json, itertools, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.normpath(os.path.join(HERE, '..'))
BIG = os.path.join(R, 'out', 'big', 'htfirst')
J1 = '/data/fmc/judging-a-dr/research/out/hand/'
HALF = [1, 4, 6, 7, 8, 9]; QTS = [0, 2, 3, 5]
MOVE_NAME = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
TETRAD = np.array([0, 1, 0, 1, 1, 0, 1, 0])
PERM8 = np.array(list(itertools.permutations(range(8))), dtype=np.int8)      # lexicographic rank -> permutation
PERM4 = np.array(list(itertools.permutations(range(4))), dtype=np.int8)

_T = None
def tables():
    global _T
    if _T is None:
        _T = {k: (np.array(v) if isinstance(v, list) and k != 'subset_name' else v)
              for k, v in json.load(open(os.path.join(BIG, 'tables.json'))).items()}
    return _T

def load():
    """dict of numpy arrays, one entry per column (cached as .npz next to the tsv)"""
    p = os.path.join(BIG, 'htfirst.tsv'); z = os.path.join(BIG, 'htfirst.npz')
    if os.path.exists(z) and os.path.getmtime(z) > os.path.getmtime(p):
        d = np.load(z, allow_pickle=False)
        return {k: d[k] for k in d.files}
    cols = None; sub = []; rows = []
    with open(p) as f:
        cols = f.readline().rstrip('\n').split('\t')
        hexcols = {i for i, c in enumerate(cols) if c in ('p0n', 'p0i', 'p1n', 'p1i')}
        for l in f:
            v = l.rstrip('\n').split('\t')
            sub.append(v[0])
            rows.append([int(x, 16) if i in hexcols else int(x) for i, x in enumerate(v) if i > 0])
    a = np.array(rows, dtype=np.int32)
    out = {c: a[:, i] for i, c in enumerate(cols[1:])}
    out['subset'] = np.array(sub)
    np.savez(z, **out)
    return out

# ------------------------------------------------------------------ coset-level reads
def setup_tables():
    """sC[a] (corner coset), sF[a, b] (corner coset, edge pattern): fewest half turns before a quarter turn that
    lowers the corner / full quarter-turn count; 9 where the count is already 0.  qC[a]: bit mask (U U' D D') of the
    quarter turns that lower the corner count right now."""
    T = tables()
    cm, em, cq, qf = T['ccos_mv'], T['epat_mv'], T['cc_qt'], T['qt_full']
    NA, NB = cm.shape[0], em.shape[0]
    low = np.zeros(NA, bool); qC = np.zeros(NA, int)
    for i, q in enumerate(QTS):
        hit = cq[cm[:, q]] + 1 == cq
        low |= hit; qC |= hit.astype(int) << i
    sC = np.full(NA, 9)
    for a in range(NA):
        if cq[a] == 0: continue
        seen = {a}; fr = [a]; h = 0
        while fr:
            if any(low[x] for x in fr): sC[a] = h; break
            nx = []
            for x in fr:
                for m in HALF:
                    y = cm[x, m]
                    if y not in seen: seen.add(y); nx.append(y)
            fr = nx; h += 1
    lowF = np.zeros((NA, NB), bool)
    for q in QTS:
        lowF |= qf[cm[:, q][:, None], em[:, q][None, :]] + 1 == qf
    sF = np.full((NA, NB), 9)
    for a in range(NA):
        for b in range(NB):
            if qf[a, b] == 0: continue
            seen = {(a, b)}; fr = [(a, b)]; h = 0
            while fr:
                if any(lowF[x] for x in fr): sF[a, b] = h; break
                nx = []
                for (x, y) in fr:
                    for m in HALF:
                        z = (cm[x, m], em[y, m])
                        if z not in seen: seen.add(z); nx.append(z)
                fr = nx; h += 1
    return sC, sF, qC

def corner_case_of_coset():
    """corner coset -> the first study's corner case id (0..45), and id -> name ('2c4-3')"""
    T = tables()
    rank = {tuple(p): i for i, p in enumerate(PERM8.tolist())}
    case = np.full(T['ccos_mv'].shape[0], -1)
    with open(J1 + 'corner_perm_cases.csv') as f:
        next(f)
        for l in f:
            p, k = l.strip().split(',')
            a = T['ccos'][rank[tuple(int(x) for x in p)]]
            assert case[a] in (-1, int(k))
            case[a] = int(k)
    assert (case >= 0).all()
    # names as in drread.corner_names(): per corner subset, ordered by average optimal
    g = collections.defaultdict(lambda: collections.defaultdict(lambda: [0] * 19))
    with open(J1 + 'k1_corner_cases.csv') as f:
        r = csv.reader(f); next(r)
        for s, a, b, d, c in r:
            g[s.split()[0]][a][int(d)] += int(c)
    name = {}
    for cs, cases in g.items():
        mean = lambda h: sum(d * c for d, c in enumerate(h)) / sum(h)
        for i, (k, h) in enumerate(sorted(cases.items(), key=lambda kv: mean(kv[1]))):
            name[int(k)] = f'{cs}-{i + 1}'
    info = {}
    with open(J1 + 'corner_cases.csv') as f:
        for r in csv.DictReader(f):
            info[int(r['corner_case'])] = r
    return case, name, info

# ------------------------------------------------------------------ piece-level reads
CORNER_COL = np.array([[0, 3], [0, 1], [2, 1], [2, 3], [0, 3], [0, 1], [2, 1], [2, 3]])
EDGE_FACE = np.array([0, 1, 2, 3, 0, 1, 2, 3])
ADJ = [(0, 0), (0, 3), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 4), (4, 7), (5, 4), (5, 5), (6, 5), (6, 6), (7, 6), (7, 7)]
SLICE_COL = np.array([[0, 3], [0, 1], [2, 1], [2, 3]])
E_ADJ = [0, 1, 2, 3, 0, 1, 2, 3]

def inverse_perm(p):
    out = np.empty_like(p); n = p.shape[1]
    np.put_along_axis(out, p.astype(np.int64), np.broadcast_to(np.arange(n, dtype=p.dtype), p.shape), axis=1)
    return out

def true_pairs(cp, ep):
    """(true pairs, per-layer counts U, D) as in the first study (hand.rs pair_counts, kind 0)"""
    nU = np.zeros(len(cp), int); nD = np.zeros(len(cp), int)
    for p, q in ADJ:
        cpc, epc = cp[:, p].astype(int), ep[:, q].astype(int)
        face = EDGE_FACE[q]
        good = TETRAD[cpc] == TETRAD[p]
        axis = (face & 1) ^ (~good).astype(int)
        ccol = CORNER_COL[cpc, axis]
        ecol = EDGE_FACE[epc]
        t = (ccol == ecol) & ((cpc < 4) == (epc < 4))
        if p < 4: nU += t
        else: nD += t
    return nU + nD, nU, nD

def slice_pairs(cp, sp):
    n = np.zeros(len(cp), int)
    for p in range(8):
        cpc = cp[:, p].astype(int)
        spc = sp[:, E_ADJ[p]].astype(int)
        n += (TETRAD[cpc] == TETRAD[p]) & (CORNER_COL[cpc] == SLICE_COL[spc]).all(axis=1)
    return n

def layer_split(cp, ep):
    """bad corners in U / D and bad edges in U / D, in the frame with at most 4 bad corners (4 and 4: at most 4 bad
    edges; 4 corners and 4 edges: the frame as it stands).  Returns kU, kD, jU, jD and the two bad masks."""
    badc = TETRAD[cp.astype(int)] != TETRAD[None, :]
    bade = (ep.astype(int) & 1) != (np.arange(8)[None, :] & 1)
    nc, ne = badc.sum(1), bade.sum(1)
    flip = (nc > 4) | ((nc == 4) & (ne > 4))
    badc = badc ^ flip[:, None]; bade = bade ^ flip[:, None]
    return badc[:, :4].sum(1), badc[:, 4:].sum(1), bade[:, :4].sum(1), bade[:, 4:].sum(1), badc, bade

class Data:
    """everything per state, both sides"""
    def __init__(self):
        D = load(); T = tables()
        self.D = D; self.n = len(D['c'])
        self.sub = D['subset']
        self.cs = np.array([s.split()[0] for s in self.sub])
        self.ne = np.array([int(s.split()[1][0]) for s in self.sub])
        self.d = D['d']
        self.sC_t, self.sF_t, self.qC_t = setup_tables()
        self.case_t, self.case_name, self.case_info = corner_case_of_coset()
        self.sC = (self.sC_t[D['ccn']], self.sC_t[D['cci']])
        self.sF = (self.sF_t[D['ccn'], D['epn']], self.sF_t[D['cci'], D['epi']])
        self.case = (self.case_t[D['ccn']], self.case_t[D['cci']])
        self.cq = T['cc_qt'][D['ccn']]
        self.qf = (T['qt_full'][D['ccn'], D['epn']], T['qt_full'][D['cci'], D['epi']])
        self.htr = (T['htr_dist'][D['ccn'], D['epn']], T['htr_dist'][D['cci'], D['epi']])
        cp, ep, sp = PERM8[D['c']], PERM8[D['e']], PERM4[D['s']]
        self.perm = ((cp, ep, sp), (inverse_perm(cp), inverse_perm(ep), inverse_perm(sp)))
        # targets
        self.t0 = np.minimum(D['a0n'], D['a0i']); self.t1 = np.minimum(D['a1n'], D['a1i'])
        self.t0n = D['a0n']; self.t1n = D['a1n']
        self.u0 = np.minimum(D['b0n'], D['b0i']); self.u1 = np.minimum(D['b1n'], D['b1i'])

def sizes():
    sys.path.insert(0, HERE)
    import common
    return common.SIZE, common.SUBS, common.CGROUPS

if __name__ == '__main__':
    X = Data()
    print(X.n, 'states;', len(set(X.sub)), 'subsets')
