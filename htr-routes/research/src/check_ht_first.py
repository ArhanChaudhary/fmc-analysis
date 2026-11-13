#!/usr/bin/env python3
"""Independent recomputation of "half turns before the first quarter turn" for a few rows.

Nothing of htrtools' route code or of research/htfirst's search is used.  For the first N sampled states of each
chosen subset x edges:
  1. the state (c, e, s) is rebuilt as three permutations with this file's own move maps (the conventions in the header
     of judging-a-dr/research/drtools/src/core.rs, typed again here) and its own lexicographic rank;
  2. every canonical optimal finish is enumerated by depth-first search, the Lean-checked table of optimal finishes
     (lean_exact_table.u8) deciding which moves stay on an optimal path (index tables from `htfirst tables`);
  3. on each finish the half turns before its first quarter turn (normal side) and after its last one (= before the
     first one on inverse) are counted from the move names; the minimum over the finishes is compared, state by state,
     with ht_first_n / ht_first_i of `htrtools routes` and a0n / a0i of `htfirst run`;
  4. for the first M states every finish of at most optimal + 1 moves is enumerated the same way and compared with
     a1n / a1i of `htfirst run`;
  5. for the first K states every optimal finish is replayed on the sticker model (sticker.py, geometry only): the
     inverse of the first finish is the scramble, and every other finish must solve it;
  6. the number of optimal finishes is compared with nopt of `htrtools routes`.
  7. the fewest quarter turns any finish of a state can have (qt_full) is recomputed here by a 0-1 search over all
     40,320 x 70 pairs of a corner arrangement and an edge pattern (quarter turns cost 1, half turns 0, from the HTR
     states), with this file's move tables, and compared with qtfull of `htrtools routes` and qtf of `htfirst run`;
     the fewest and most quarter turns over the optimal finishes are compared with qmin / qmax of `htrtools routes`;
     and the count of step 3 restricted to the optimal finishes with exactly that many quarter turns ("no extra
     quarter turn") is compared with e0n / e0i / hasmin of `htfirst run`.
Then the row's shares (first qt after 0 / 1 / 2 / 3+ half turns; better side, normal alone) are printed from this
enumeration next to the shares of the same states in the main data, and the split of "0 half turns" into a finish
with no extra quarter turn and only finishes with extra ones.
usage: check_ht_first.py <N> <M> <K> <subset> [<subset> ...] [out=<file name in out/checks>]      (subset as "2c4_2e")
Output: out/checks/check_ht_first.txt unless out= is given"""
import sys, os, csv, json, itertools, time, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
R = os.path.normpath(os.path.join(HERE, '..'))
EXACT = '/data/fmc/judging-a-dr/research/data/lean_exact_table.u8'

NAMES = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
FACE = [0, 0, 0, 1, 1, 1, 2, 3, 4, 5]
ISQ = [True, False, True, True, False, True, False, False, False, False]
# position maps: the piece at position p goes to position t[p]
GEN = {
    'U': ([1, 2, 3, 0, 4, 5, 6, 7], [1, 2, 3, 0, 4, 5, 6, 7], [0, 1, 2, 3]),
    'D': ([0, 1, 2, 3, 7, 4, 5, 6], [0, 1, 2, 3, 7, 4, 5, 6], [0, 1, 2, 3]),
    'R2': ([7, 1, 2, 4, 3, 5, 6, 0], [0, 1, 2, 7, 4, 5, 6, 3], [3, 1, 2, 0]),
    'L2': ([0, 6, 5, 3, 4, 2, 1, 7], [0, 5, 2, 3, 4, 1, 6, 7], [0, 2, 1, 3]),
    'F2': ([5, 4, 2, 3, 1, 0, 6, 7], [4, 1, 2, 3, 0, 5, 6, 7], [1, 0, 2, 3]),
    'B2': ([0, 1, 7, 6, 4, 5, 3, 2], [0, 1, 6, 3, 4, 5, 2, 7], [0, 1, 3, 2]),
}
def power(t, k):
    out = list(range(len(t)))
    for _ in range(k): out = [t[x] for x in out]
    return out
MAPS = []
for nm in NAMES:
    base = nm[0] if nm[0] in 'UD' else nm
    k = 1 if nm in ('U', 'D') else 2 if nm in ('U2', 'D2') else 3 if nm in ("U'", "D'") else 1
    MAPS.append(tuple(power(t, k) for t in GEN[base]))
def move_table(n, idx):
    perms = list(itertools.permutations(range(n)))            # lexicographic: position in the list = rank
    rank = {p: i for i, p in enumerate(perms)}
    tab = np.zeros((10, len(perms)), dtype=np.int32)
    for m in range(10):
        t = MAPS[m][idx]
        for i, p in enumerate(perms):
            q = [0] * n
            for pos in range(n): q[t[pos]] = p[pos]
            tab[m, i] = rank[tuple(q)]
    return tab
CM, EM, SM = move_table(8, 0), move_table(8, 1), move_table(4, 2)
CML, EML, SML = CM.tolist(), EM.tolist(), SM.tolist()

T = json.load(open(os.path.join(R, 'out', 'big', 'htfirst', 'tables.json')))
CCLASS, CSYMTO, ESYM, SSYM, TO12 = T['cclass'], T['csymto'], T['esym'], T['ssym'], T['to12']
TABLE = np.memmap(EXACT, dtype=np.uint8, mode='r')
def depth(c, e, s):
    sym = CSYMTO[c]
    return int(TABLE[(CCLASS[c] * 40320 + ESYM[sym][e]) * 12 + TO12[SSYM[sym][s]]])

def finishes(c, e, s, budget):
    """every canonical finish of at most `budget` moves (list of move indices)"""
    out = []; seq = []
    def rec(c, e, s, rem, lf, la):
        if depth(c, e, s) == 0:
            out.append(list(seq))            # solved: any continuation would not be a finish of this state's prefix
            return
        if rem == 0: return
        for m in range(10):
            f = FACE[m]
            if f == lf or f // 2 == la: continue
            c2, e2, s2 = CML[m][c], EML[m][e], SML[m][s]
            if depth(c2, e2, s2) > rem - 1: continue
            seq.append(m)
            rec(c2, e2, s2, rem - 1, f, f // 2 if (lf != -1 and lf // 2 == f // 2) else -2)
            seq.pop()
    rec(c, e, s, budget, -1, -2)
    return out
def lead(seq):
    for i, m in enumerate(seq):
        if ISQ[m]: return i
    return 99
def trail(seq): return lead(seq[::-1])

# ---- fewest quarter turns of any finish: 0-1 search over (corner arrangement, edge pattern), own tables
PERM8 = list(itertools.permutations(range(8)))
PATS = [m for m in range(256) if bin(m).count('1') == 4]            # positions holding the four M-slice edges (UF UB DF DB)
PIDX = {m: i for i, m in enumerate(PATS)}
HOME = sum(1 << p for p in (0, 2, 4, 6))
def pattern_of(eperm): return sum(1 << p for p in range(8) if eperm[p] % 2 == 0)
def qt_full_table():
    PM = np.zeros((10, 70), dtype=np.int64)
    for m in range(10):
        t = MAPS[m][1]
        for i, mask in enumerate(PATS):
            PM[m, i] = PIDX[sum(1 << t[p] for p in range(8) if mask >> p & 1)]
    CMq = CM.astype(np.int64)
    half = [m for m in range(10) if not ISQ[m]]; quarter = [m for m in range(10) if ISQ[m]]
    hc = {0}; st = [0]                                           # corner arrangements of the half-turn group
    while st:
        x = st.pop()
        for m in half:
            y = int(CMq[m, x])
            if y not in hc: hc.add(y); st.append(y)
    assert len(hc) == 96
    dist = np.full(40320 * 70, -1, dtype=np.int8)
    step = lambda f, m: CMq[m, f // 70] * 70 + PM[m, f % 70]
    level = np.array(sorted(c * 70 + PIDX[HOME] for c in hc), dtype=np.int64); k = 0
    while len(level):
        dist[level] = k; queue = level; allk = [level]
        while len(queue):                                        # close under half turns
            nx = np.unique(np.concatenate([step(queue, m) for m in half]))
            nx = nx[dist[nx] == -1]; dist[nx] = k; allk.append(nx); queue = nx
        cur = np.concatenate(allk)
        nx = np.unique(np.concatenate([step(cur, m) for m in quarter]))
        level = nx[dist[nx] == -1]; k += 1
    assert (dist >= 0).all()
    return dist

def main():
    N, M, K = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); SUBS = [a for a in sys.argv[4:] if not a.startswith('out=')]
    outname = ([a[4:] for a in sys.argv[4:] if a.startswith('out=')] or ['check_ht_first.txt'])[0]
    QF = qt_full_table()
    import sticker
    from sticker import do, SOLVED, inv_seq
    lines = []
    def P(*a):
        s = ' '.join(str(x) for x in a); print(s, flush=True); lines.append(s)
    P(f'check_ht_first.py {N} {M} {K} {" ".join(SUBS)}')
    hf = {}
    with open(os.path.join(R, 'out', 'big', 'htfirst', 'htfirst.tsv')) as f:
        rd = csv.DictReader(f, delimiter='\t')
        want = {s.replace('_', ' ') for s in SUBS}
        for r in rd:
            if r['subset'] in want and int(r['idx']) < N: hf[(r['subset'], int(r['idx']))] = r
    tot = dict(states=0, opt_mismatch_htrtools=0, opt_mismatch_htfirst=0, nopt_mismatch=0, p1_states=0, p1_mismatch=0,
               sticker_states=0, sticker_finishes=0, sticker_fail=0, depth_mismatch=0,
               qtfull_mismatch_htrtools=0, qtfull_mismatch_htfirst=0, qmin_qmax_mismatch_htrtools=0, noextra_mismatch_htfirst=0)
    for sub in SUBS:
        name = sub.replace('_', ' ')
        rows = list(csv.DictReader(open(os.path.join(R, 'out', 'big', 'run1', f'states_{sub}.tsv')), delimiter='\t'))[:N]
        t0 = time.time()
        mine = []; main_n = []; main_i = []; split = collections.Counter()
        for k, r in enumerate(rows):
            c, e, s = int(r['c']), int(r['e']), int(r['s']); d = depth(c, e, s)
            h = hf[(name, int(r['idx']))]
            tot['states'] += 1
            tot['depth_mismatch'] += d != int(r['d'])
            fs = finishes(c, e, s, d)
            assert fs and all(len(x) == d for x in fs)
            a = min(lead(x) for x in fs); b = min(trail(x) for x in fs)
            noqt = any(lead(x) == 99 for x in fs)
            mine.append((a, b, noqt))
            # htrtools writes the finish length when no optimal has a quarter turn
            en, ei = int(r['ht_first_n']), int(r['ht_first_i'])
            tot['opt_mismatch_htrtools'] += (min(a, d) != en) or (min(b, d) != ei)
            tot['opt_mismatch_htfirst'] += (a != int(h['a0n'])) or (b != int(h['a0i'])) or (noqt != (h['noqt0'] == '1'))
            tot['nopt_mismatch'] += len(fs) != int(r['nopt'])
            main_n.append(99 if h['noqt0'] == '1' else int(h['a0n'])); main_i.append(int(h['a0i']))
            # quarter turns: the fewest any finish can have, and the optimal finishes with exactly that many
            qf = int(QF[c * 70 + PIDX[pattern_of(PERM8[e])]])
            nq = [sum(1 for m in x if ISQ[m]) for x in fs]
            tot['qtfull_mismatch_htrtools'] += qf != int(r['qtfull'])
            tot['qmin_qmax_mismatch_htrtools'] += (min(nq) != int(r['qmin'])) or (max(nq) != int(r['qmax']))
            keepf = [x for x, q in zip(fs, nq) if q == qf]
            en_, ei_ = (min(lead(x) for x in keepf), min(trail(x) for x in keepf)) if keepf else (99, 99)
            if 'e0n' in h:
                tot['qtfull_mismatch_htfirst'] += qf != int(h['qtf'])
                tot['noextra_mismatch_htfirst'] += (en_ != int(h['e0n'])) or (ei_ != int(h['e0i'])) or (bool(keepf) != (h['hasmin'] == '1'))
            split['states'] += 1
            split['every optimal has extra quarter turns'] += not keepf
            split['some optimal has extra quarter turns'] += max(nq) > qf
            split['an optimal starts or ends with a quarter turn'] += min(a, b) == 0
            split['an optimal with no extra quarter turn starts or ends with a quarter turn'] += min(en_, ei_) == 0
            split['only optimals with extra quarter turns start or end with a quarter turn'] += min(a, b) == 0 and min(en_, ei_) != 0
            if k < M:
                f1 = finishes(c, e, s, d + 1)
                a1 = min(lead(x) for x in f1); b1 = min(trail(x) for x in f1)
                tot['p1_states'] += 1
                tot['p1_mismatch'] += (a1 != int(h['a1n'])) or (b1 != int(h['a1i']))
            if k < K:
                scr = inv_seq([NAMES[m] for m in fs[0]])
                st = do(SOLVED, scr)
                tot['sticker_states'] += 1
                for x in fs:
                    tot['sticker_finishes'] += 1
                    tot['sticker_fail'] += do(st, [NAMES[m] for m in x]) != SOLVED
        mine = [(a, b) for a, b, q in mine if not q]          # states with an all-half-turn optimal are left out of the shares
        def dist(v):
            n = len(v); return ' / '.join(f'{100 * sum(1 for x in v if (x == k if k < 3 else x >= 3)) / n:.1f}%' for k in range(4))
        P(f'{name}: first {len(rows)} states, {time.time() - t0:.0f} s')
        P(f'  better side, first qt after 0 / 1 / 2 / 3+ half turns, this enumeration: {dist([min(a, b) for a, b in mine])}')
        P(f'  normal side alone, this enumeration:                                     {dist([a for a, b in mine])}')
        for kk, v in split.items():
            if kk != 'states': P(f'  {kk}: {100 * v / split["states"]:.1f}% of the {split["states"]} states')
        keep = [(a, b) for a, b in zip(main_n, main_i) if a != 99]
        P(f'  better side, same states in the main data (htfirst.tsv):                 {dist([min(a, b) for a, b in keep])}')
        P(f'  normal side alone, same states in the main data:                         {dist([a for a, b in keep])}')
    for k, v in tot.items(): P(f'{k}\t{v}')
    ok = all(tot[k] == 0 for k in tot if 'mismatch' in k or 'fail' in k)
    P('ALL EQUAL' if ok else 'DIFFERENCES FOUND')
    open(os.path.join(R, 'out', 'checks', outname), 'w').write('\n'.join(lines) + '\n')

if __name__ == '__main__':
    main()
