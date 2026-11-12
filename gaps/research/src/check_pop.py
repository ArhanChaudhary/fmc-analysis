#!/usr/bin/env python3
"""Check the population file (big/pop_raw.tsv or a part): for a random sample of DRs,
  1. the ranks (c, e, s) unranked to arrays and read by judging-a-dr's `drtools read --quick` give the same subset and
     optimal as `htrtools label` (gaps fork, the code every later step uses);
  2. the first optimal finish htrtools `trace` gives for the side's state, turned back to the cube's frame, solves the
     scramble on stickers (judging-a-dr fmccube): side N: S N F I^-1 = solved; side I: S^-1 I F N^-1 = solved; and
     its length equals the optimum.
usage: check_pop.py <pop file> <n> <seed>   -> prints counts, exit 1 on any failure"""
import sys, random, subprocess, json
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
import many_examples as me
fc = me.fc
D = '/data/fmc/judging-a-dr/research/data'
T = '/data/fmc/gaps/research/src/htrreal/target/release/htrtools'
CAP = ['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=4G']

def unrank(r, n):
    f = [1] * (n + 1)
    for i in range(1, n + 1): f[i] = f[i - 1] * i
    items = list(range(n)); p = []
    for i in range(n):
        k, r = divmod(r, f[n - 1 - i]); p.append(items.pop(k))
    return p

def main():
    path, n, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    sys.path.insert(0, '/data/fmc/eo-to-dr/research/src'); import canon
    scr = [canon.simplify(l) for l in open('/data/fmc/eo-to-dr/research/out/scrambles.txt').read().split('\n') if l.strip()]
    rows = [l.rstrip('\n').split('\t') for l in open(path) if not l.startswith('#') and not l.startswith('scr\t')]
    random.seed(seed); pick = random.sample(rows, min(n, len(rows)))
    cesl = '\n'.join(f'{r[6]} {r[7]} {r[8]}' for r in pick) + '\n'
    lab = subprocess.run(CAP + [T, 'label', f'{D}/lean_exact_table.u8', f'{D}/ls_depth.u8'], input=cesl, capture_output=True, text=True).stdout.split('\n')[1:]
    arrays = [[unrank(int(r[6]), 8), unrank(int(r[7]), 8), unrank(int(r[8]), 4)] for r in pick]
    q = me.quick(arrays)
    tr = subprocess.run(CAP + [T, 'trace', f'{D}/lean_exact_table.u8', '1'], input=''.join(f'#{r[6]},{r[7]},{r[8]}\n' for r in pick),
                        capture_output=True, text=True).stdout.strip().split('\n')
    bad = 0
    for r, l, kv, t in zip(pick, lab, q, tr):
        sub, d = l.split('\t')[:2]
        if kv['subset'] != sub or int(kv['optimal']) != int(d):
            bad += 1; print('LABEL MISMATCH', r, l, kv['subset'], kv['optimal'])
        j = json.loads(t); fin = j['all'][0]
        V = me.VIEWS[r[1]]
        F = [(V.face_back[b], tt) for b, tt in fc.parse(fin)]
        nm, im = fc.split_niss(r[5])
        S = fc.parse(scr[int(r[0])])
        seq = S + nm + F + fc.invert(im) if r[2] == 'N' else fc.invert(S) + im + F + fc.invert(nm)
        if fc.apply(fc.solved(), seq) != fc.solved() or len(F) != int(d):
            bad += 1; print('REPLAY FAIL', r, fin)
    sides = sum(r[2] == 'I' for r in pick)
    print(f'{len(pick)} DRs checked ({sides} on the inverse side): drtools read --quick subset and optimal = htrtools label; '
          f'first optimal finish replayed on stickers solves the scramble with the stated length. failures: {bad}')
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
