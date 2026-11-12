#!/usr/bin/env python3
"""Gap 1: the DRs solvers actually reach.

For each of the first N uniformly random states of the eo-to-dr study (out/scrambles.txt, `eodrtools mkscr 50000
2026`; adjacent turns of one face merged with eo-to-dr's canon.py), every DR of at most 11 moves that goes through an
EO first, as judging-a-dr's examples page lists them:

    cubelib-cli solve -s "EO[niss=always;max=5] > DR[niss=before;max=11]" -q 0 -M 11 -f detailed

(EO on any axis, NISS anywhere in the EO; then DR on one side without breaking that EO, all three axes.  cubelib lists
no EO longer than 5 even with max=8, so judging-a-dr's "max=8" step lists the same DRs.)

Each DR is the state as written, with the quarter turns among the last moves of each side written clockwise
(judging-a-dr many_examples.canon), turned so its axis is U/D, and deduplicated per scramble by (axis, state) as on the
examples page: each DR state counts once per scramble, its first listing (shortest, then text) gives the moves.
The state analysed is the DR on the side the DR step is written on: the DR step on normal -> I^-1 S N (the state
as written), on inverse -> its inverse N^-1 S^-1 I, computed separately on stickers (and checked to be the inverse
permutation).

Output: big/pop_raw.tsv, one row per (scramble, DR):
    scr  axis  side  len  eolen  moves  c e s (side's state, ranks as drtools/htrtools)  cn en sn (normal-side state)
usage: population.py N [workers]"""
import sys, os, subprocess, re, multiprocessing
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
sys.path.insert(0, '/data/fmc/eo-to-dr/research/src')
import many_examples as me
import canon as eocanon
fc = me.fc

STEPS = 'EO[niss=always;max=5] > DR[niss=before;max=11]'
CAP = 11
SCR = '/data/fmc/eo-to-dr/research/out/scrambles.txt'
OUT = '/data/fmc/gaps/research/big/pop_raw.tsv'

def rank(p):
    n = len(p); r = 0; f = [1] * (n + 1)
    for i in range(1, n + 1): f[i] = f[i - 1] * i
    for i in range(n):
        r += sum(1 for x in p[i + 1:] if x < p[i]) * f[n - 1 - i]
    return r

def invperm(p):
    q = [0] * len(p)
    for i, x in enumerate(p): q[x] = i
    return q

def cubelib(scramble):
    out = subprocess.run(['cubelib-cli', '--no-check-update', 'solve', '-s', STEPS, '-q', '0', '-M', str(CAP), '-f', 'detailed', scramble],
                         capture_output=True, text=True).stdout
    res = []
    for block in out.split('\n\n'):
        sol = re.search(r'^Solution \((\d+)\): ?(.*)$', block, re.M)
        ax = re.search(r'//\s*dr(ud|fb|lr)', block)
        if not sol or not ax: continue
        eo = re.search(r'^(.*?)//\s*eo(ud|fb|lr)\s*\((\d+)/', block, re.M)
        drl = re.search(r'^(.*?)//\s*dr(ud|fb|lr)', block, re.M)
        drmoves = drl.group(1).strip()
        if drmoves:
            side = 'I' if drmoves.startswith('(') else 'N'
        else:                                    # DR step empty: the side the EO ends on (normal unless EO is inverse only)
            e = eo.group(1).strip()
            side = 'I' if e.startswith('(') and e.endswith(')') and e.count('(') == 1 else 'N'
        n, i = fc.split_niss(sol.group(2))
        assert len(n) + len(i) == int(sol.group(1)), block
        res.append((n, i, {'ud': 'U/D', 'fb': 'F/B', 'lr': 'R/L'}[ax.group(1)], side, int(eo.group(3)) if eo else -1))
    return res

def work(job):
    k, scramble = job
    sc = fc.parse(scramble)
    ps = me.perm(sc)
    psi = me.perm(fc.invert(sc))
    seen = set(); rows = []
    found = cubelib(scramble)
    for n, i, axis, side, eol in sorted(found, key=lambda t: (len(t[0]) + len(t[1]), me.niss(me.canon(t[0]), me.canon(t[1])), t[2])):
        cn, ci = me.canon(n), me.canon(i)
        V = me.VIEWS[axis]
        a = V.arrays(me.state(ps, cn, ci))           # I^-1 S N
        assert a is not None, (scramble, n, i, axis)
        key = (axis, tuple(map(tuple, a)))
        if key in seen: continue
        seen.add(key)
        if side == 'I':
            # inverse side: N^-1 S^-1 I, on stickers
            b = V.arrays(me.state(psi, ci, cn))
            assert b is not None and all(invperm(x) == y for x, y in zip(a, b)), (scramble, n, i, axis)
        else:
            b = a
        rows.append(f"{k}\t{axis}\t{side}\t{len(n) + len(i)}\t{eol}\t{me.niss(cn, ci)}\t"
                    f"{rank(b[0])}\t{rank(b[1])}\t{rank(b[2])}\t{rank(a[0])}\t{rank(a[1])}\t{rank(a[2])}")
    return k, rows

def main():
    N = int(sys.argv[1]); W = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    scr = [eocanon.simplify(l) for l in open(SCR).read().split('\n') if l.strip()][:N]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    tot = 0
    with open(OUT, 'w') as f, multiprocessing.Pool(W) as pool:
        f.write(f'# {N} scrambles (eo-to-dr out/scrambles.txt, first N, canon.simplify); cubelib-cli steps "{STEPS}" -q 0 -M {CAP}; deduplicated by (axis, state) per scramble\n')
        f.write('scr\taxis\tside\tlen\teolen\tmoves\tc\te\ts\tcn\ten\tsn\n')
        for d, (k, rows) in enumerate(pool.imap_unordered(work, list(enumerate(scr)), chunksize=4)):
            for r in rows: f.write(r + '\n')
            tot += len(rows)
            if (d + 1) % 500 == 0: print(f'{d + 1} scrambles, {tot} DRs', flush=True)
    with open(OUT.replace('.tsv', '_scrambles.txt'), 'w') as f:
        for s in scr: f.write(s + '\n')
    print('rows', tot)

if __name__ == '__main__':
    main()
