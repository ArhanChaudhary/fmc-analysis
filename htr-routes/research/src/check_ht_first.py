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
Then the row's shares (first qt after 0 / 1 / 2 / 3+ half turns; better side, normal alone) are printed from this
enumeration next to the shares of the same states in the main data.
usage: check_ht_first.py <N> <M> <K> <subset> [<subset> ...]      (subset as "2c4_2e")
Output: out/checks/check_ht_first.txt"""
import sys, os, csv, json, itertools, time
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

def main():
    N, M, K = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); SUBS = sys.argv[4:]
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
               sticker_states=0, sticker_finishes=0, sticker_fail=0, depth_mismatch=0)
    for sub in SUBS:
        name = sub.replace('_', ' ')
        rows = list(csv.DictReader(open(os.path.join(R, 'out', 'big', 'run1', f'states_{sub}.tsv')), delimiter='\t'))[:N]
        t0 = time.time()
        mine = []; main_n = []; main_i = []
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
        keep = [(a, b) for a, b in zip(main_n, main_i) if a != 99]
        P(f'  better side, same states in the main data (htfirst.tsv):                 {dist([min(a, b) for a, b in keep])}')
        P(f'  normal side alone, same states in the main data:                         {dist([a for a, b in keep])}')
    for k, v in tot.items(): P(f'{k}\t{v}')
    ok = all(tot[k] == 0 for k in tot if 'mismatch' in k or 'fail' in k)
    P('ALL EQUAL' if ok else 'DIFFERENCES FOUND')
    open(os.path.join(R, 'out', 'checks', 'check_ht_first.txt'), 'w').write('\n'.join(lines) + '\n')

if __name__ == '__main__':
    main()
