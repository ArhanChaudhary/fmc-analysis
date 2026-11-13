#!/usr/bin/env python3
"""A separate check of the every-other-move rule (write-up 8.3, corrections page A2).

It shares nothing with the study's programs except the sticker model (research/src/cube.py): its own list of the
8-move corner 3-cycles (every 4 moves joined with every 4 moves), its own random skeletons and leftovers, its own
search.  It measures, for one 8-move comm and 20-move skeletons:

  3c_fixed   a random 3c; opposite-face pairs written in one fixed order (U D, R L, F B), the way the study's samples
             are made.  This is the study's own table again.
  3c_free    a random 3c; an opposite-face pair may be written either way round (each move uniform among the moves
             that neither turn the face just turned nor put a third move on one axis).
  5c_fixed   the first comm of a random 5c (every 8-mover, at every spot, that leaves a 3c), pairs in the fixed order.

For each: on the skeletons whose best is an 8-3 or better, how many walks (every second spot and both ends, started at
spot 0 and at spot 1) find an insertion as good as the best; of the misses, what the best was, how many have every
best spot next to an opposite-face pair, and how many the same walk finds once one such pair of the skeleton is
written the other way round.

It also counts how often two neighbouring moves are an opposite-face pair: in its own skeletons, in the study's sample
(out/sample_3c_n20.tsv, when the file is there) and in the posted skeletons (out/real_rows.json, as posted).

  every_other.py [N_3c N_5c]      default 20000 10000; writes out/verify/every_other.json and .txt  (about three minutes)"""
import sys, os, json, random, time, collections
import numpy as np
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, R + '/src')
from cube import do, SOLVED, MOVES, cancel, parse, apply, compose, inverse
OUT = R + '/out/verify/'
NAMES = [f + s for f in 'UDRLFB' for s in ('', '2', "'")]
AXIS = {'U': 0, 'D': 0, 'R': 1, 'L': 1, 'F': 2, 'B': 2}; FIRST = set('URF')
MS = {m: do(SOLVED, [m]) for m in NAMES}; MSI = {m: inverse(MS[m]) for m in NAMES}

# ---------------------------------------------------------------- the 8-move corner 3-cycles
def three_cycle_states():
    """All 1,008 corner 3-cycles (three corners moved, nothing else), built from the stickers of the model."""
    from cube import ST
    corners = sorted({p for p, n in ST if all(abs(c) == 1 for c in p)})
    def stickers(p):                               # the three stickers of a corner in one rotational order
        ax = {max(range(3), key=lambda k: abs(ST[i][1][k])): i for i in range(54) if ST[i][0] == p}
        return [ax[0], ax[1], ax[2]] if p[0] * p[1] * p[2] > 0 else [ax[0], ax[2], ax[1]]
    ring = {p: stickers(p) for p in corners}; out = []
    for i, a in enumerate(corners):
        for b in corners[i + 1:]:
            for c in corners[i + 1:]:
                if b == c: continue
                for t1 in range(3):
                    for t2 in range(3):
                        s = list(range(54))
                        for src, dst, t in ((a, b, t1), (b, c, t2), (c, a, (-t1 - t2) % 3)):
                            for k in range(3): s[ring[dst][(k + t) % 3]] = ring[src][k]
                        out.append(tuple(s))
    assert len(set(out)) == 1008
    return out
def eight_movers(t3):
    """{3-cycle state: [8-move sequences]}: every sequence of 4 moves (no two in a row on one face) joined with every
    such sequence, matched on the whole sticker state."""
    seqs = [[]]
    for _ in range(4): seqs = [q + [k] for q in seqs for k in range(18) if not q or q[-1] // 3 != k // 3]
    S = np.zeros((len(seqs), 54), dtype=np.int16)
    for r, q in enumerate(seqs):
        s = SOLVED
        for k in q: s = apply(s, MOVES[NAMES[k]])
        S[r] = s
    INV = np.zeros_like(S); INV[np.arange(len(seqs))[:, None], S] = np.arange(54, dtype=np.int16)[None, :]
    W = np.random.default_rng(1).integers(1, 2 ** 62, size=54, dtype=np.uint64) | np.uint64(1)
    h = lambda A: (A.astype(np.uint64) * W[None, :]).sum(axis=1, dtype=np.uint64)
    HS = h(S); order = np.argsort(HS, kind='stable'); HSs = HS[order]; D = {}
    for T in t3:
        need = INV[:, np.array(T, dtype=np.int16)]              # a then b = T  =>  b = a^-1 then T
        hb = h(need); lo = np.searchsorted(HSs, hb, 'left'); hi = np.searchsorted(HSs, hb, 'right')
        for r in np.nonzero(hi > lo)[0]:
            for j in range(lo[r], hi[r]):
                b = order[j]
                if seqs[r][-1] // 3 != seqs[b][0] // 3 and (S[b] == need[r]).all():
                    D.setdefault(T, []).append([NAMES[k] for k in seqs[r] + seqs[b]])
    for T, algs in D.items():
        for a in algs: assert do(SOLVED, a) == T and len(cancel(a)) == 8
    return D

# ---------------------------------------------------------------- skeletons, leftovers, the search
def skeleton(n, rng, order):
    seq = []
    while len(seq) < n:
        m = rng.choice(NAMES)
        if seq and seq[-1][0] == m[0]: continue
        if seq and AXIS[seq[-1][0]] == AXIS[m[0]]:
            if order == 'fixed' and seq[-1][0] not in FIRST: continue                      # D U, L R, B F are not written
            if order == 'free' and len(seq) >= 2 and AXIS[seq[-2][0]] == AXIS[m[0]]: continue    # no third move on the axis
        seq.append(m)
    assert len(cancel(seq)) == n
    return seq
def is_pair(a, b): return a[0] != b[0] and AXIS[a[0]] == AXIS[b[0]]
def moved(s):
    from cube import ST
    return len({ST[i][0] for i in range(54) if s[i] != i})
def leftover(typ, t3, rng):
    if typ == '3c': return rng.choice(t3)
    while True:                                    # two 3-cycles that share one corner make a 5-cycle; each 5c is made 5 ways
        s = compose(rng.choice(t3), rng.choice(t3))
        if moved(s) == 5: return s
def insertions(seq, left, typ, D, T3):
    """[(total length, spot)] for every 8-mover at every spot that solves the 3c, or, for a 5c, leaves a 3c."""
    K = do(SOLVED, seq)
    x0 = compose(compose(K, inverse(left)), inverse(K))        # what an alg put before the first move has to do
    if typ == '3c': targets = [x0]
    else:
        targets = [c for c in T3 if compose(inverse(c), x0) in T3]; assert len(targets) == 5
    out = []
    for j in range(len(seq) + 1):
        for t in targets:
            for a in D.get(t, ()): out.append((len(cancel(seq[:j] + a + seq[j:])), j))
        if j < len(seq):
            m = seq[j]; targets = [compose(compose(MSI[m], t), MS[m]) for t in targets]
    return out
def walk(res, par, n):
    got = [t for t, j in res if j % 2 == par or j in (0, n)]
    return min(got) if got else None
def run(typ, order, N, seed, D, T3, t3, n=20):
    rng = random.Random(seed); c = collections.Counter(); by = collections.Counter(); pairs = 0
    for _ in range(N):
        seq = skeleton(n, rng, order); left = leftover(typ, t3, rng)
        pairs += sum(is_pair(a, b) for a, b in zip(seq, seq[1:]))
        res = insertions(seq, left, typ, D, T3)
        if not res: c['no_8_mover'] += 1; continue
        best = min(t for t, j in res); spots = [j for t, j in res if t == best]
        for par in (0, 1):
            g = walk(res, par, n); c['walks'] += 1; c['walks_find_best'] += g == best
            if best > n + 5: continue
            c['good_walks'] += 1
            if g == best: c['good_found'] += 1; continue
            c['good_missed'] += 1; by[f'8-{n + 8 - best}'] += 1
            c['missed_next_to_pair'] += all((j >= 2 and is_pair(seq[j - 2], seq[j - 1])) or (j <= n - 2 and is_pair(seq[j], seq[j + 1])) for j in spots)
            swapped = False
            for i in range(n - 1):
                if is_pair(seq[i], seq[i + 1]):
                    s2 = seq[:i] + [seq[i + 1], seq[i]] + seq[i + 2:]
                    if walk(insertions(s2, left, typ, D, T3), par, n) == best: swapped = True; break
            c['missed_found_once_a_pair_is_swapped'] += swapped
    out = {'leftover': typ, 'pair_order': order, 'moves': n, 'skeletons': N, 'seed': seed, 'pairs': pairs, 'joins': N * (n - 1), 'missed_by_best': dict(sorted(by.items()))}
    out.update({k: c[k] for k in ('no_8_mover', 'walks', 'walks_find_best', 'good_walks', 'good_found', 'good_missed', 'missed_next_to_pair', 'missed_found_once_a_pair_is_swapped')})
    return out
def pair_counts():
    out = {}
    p = R + '/out/sample_3c_n20.tsv'
    if os.path.exists(p):
        k = j = n = 0
        with open(p) as f:
            col = f.readline().rstrip('\n').split('\t').index('skeleton')
            for line in f:
                s = line.split('\t')[col].split(); n += 1; j += len(s) - 1; k += sum(is_pair(a, b) for a, b in zip(s, s[1:]))
        out['study_sample_3c_n20'] = {'skeletons': n, 'pairs': k, 'joins': j}
    rows = [r for r in json.load(open(R + '/out/real_rows.json')) if not r['dup_of']]
    k = j = first = 0
    for r in rows:
        s = parse(r['skeleton']); j += len(s) - 1
        for a, b in zip(s, s[1:]):
            if is_pair(a, b): k += 1; first += a[0] in FIRST
    out['posted'] = {'skeletons': len(rows), 'pairs': k, 'joins': j, 'pairs_written_U_D_R_L_F_B': first}
    return out
def main():
    N3 = int(sys.argv[1]) if len(sys.argv) > 1 else 20000; N5 = int(sys.argv[2]) if len(sys.argv) > 2 else 10000
    t0 = time.time(); t3 = three_cycle_states(); T3 = set(t3); D = eight_movers(t3)
    J = {'algs': {'sequences': sum(len(v) for v in D.values()), 'states': len(D), 'three_cycles': len(t3)}}
    assert J['algs'] == {'sequences': 864, 'states': 528, 'three_cycles': 1008}, J['algs']
    J['runs'] = {}
    for name, typ, order, N, seed in (('3c_fixed', '3c', 'fixed', N3, 20261113), ('3c_free', '3c', 'free', N3, 20261114), ('5c_fixed', '5c', 'fixed', N5, 20261115)):
        J['runs'][name] = run(typ, order, N, seed, D, T3, t3); print(name, J['runs'][name], f'{time.time() - t0:.0f}s', flush=True)
    J['pairs'] = pair_counts()
    os.makedirs(OUT, exist_ok=True)
    json.dump(J, open(OUT + 'every_other.json', 'w'), indent=1)
    L = ['every_other.py: one 8-move comm on 20-move skeletons, every second spot and both ends against every spot', '']
    for name, r in J['runs'].items():
        L += [f"{name}: {r['skeletons']:,} skeletons, opposite-face pairs at {r['pairs']:,} of {r['joins']:,} joins of two moves (1 in {r['joins'] / r['pairs']:.1f}); no 8-mover on {r['no_8_mover']}",
              f"  walks {r['walks']:,}, find the best {r['walks_find_best']:,} ({100 * r['walks_find_best'] / r['walks']:.1f}%)",
              f"  best is 8-3 or better: walks {r['good_walks']:,}, found {r['good_found']:,} ({100 * r['good_found'] / r['good_walks']:.1f}%), missed {r['good_missed']:,} {r['missed_by_best']}",
              f"  of the misses: every best spot next to an opposite-face pair {r['missed_next_to_pair']:,}; found by the same walk once a pair is written the other way round {r['missed_found_once_a_pair_is_swapped']:,}", '']
    for name, r in J['pairs'].items():
        L.append(f"{name}: {r['skeletons']:,} skeletons, opposite-face pairs at {r['pairs']:,} of {r['joins']:,} joins of two moves (1 in {r['joins'] / r['pairs']:.1f})" + (f"; {r['pairs_written_U_D_R_L_F_B']} of them written U D, R L or F B" if 'pairs_written_U_D_R_L_F_B' in r else ''))
    open(OUT + 'every_other.txt', 'w').write('\n'.join(L) + '\n'); print('\n'.join(L))
if __name__ == '__main__': main()
