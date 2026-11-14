"""Calibrate the search budget of GenProbe / GenProbeOld on the official scrambles: for each budget, the middles the
solver gives for the states of the official middles, against the official middles themselves.
usage: calib.py new|old BUDGET... [--n N]      (run from the folder that has big/ and build8/, build8old/)
out: out/calib_<era>.tsv   budget, states, mean length, mean official length, same text %, same length %, shorter %, longer %, seconds"""
import sys, subprocess, time, os, random
BIG = os.environ.get('SD_BIG', '/data/scramble-difficulty/big')
JAVA = os.environ.get('JAVA', '/data/scramble-difficulty/ext/jdk-17.0.21+9/bin/java')
BUILD = os.environ.get('SD_BUILD', '/data/scramble-difficulty')
era = sys.argv[1]; args = sys.argv[2:]
N = 600
if '--n' in args: i = args.index('--n'); N = int(args[i + 1]); args = args[:i] + args[i + 2:]
budgets = [int(a) for a in args]
real = [l.rstrip('\n').split('\t') for l in open(BIG + '/real_unique.tsv')][1:]
states = dict(l.rstrip('\n').split('\t') for l in open(BIG + '/states_real.tsv'))
ids = [f'r{i}' for i, r in enumerate(real) if (r[2] >= '2020-08') == (era == 'new')]
random.Random(1).shuffle(ids); ids = ids[:N]
mid = {f'r{i}': r[0].split()[3:-3] for i, r in enumerate(real)}
inp = ''.join(f'{k}\t{states[k]}\n' for k in ids)
cp, cls = (BUILD + '/build8', 'cs.min2phase.GenProbe') if era == 'new' else (BUILD + '/build8old', 'cs.min2phase.GenProbeOld')
rows = []
for b in budgets:
    t = time.time()
    out = subprocess.run([JAVA, '-cp', cp, cls, 'solve', str(b)], input=inp, capture_output=True, text=True).stdout
    got = dict(l.split('\t') for l in out.strip().split('\n'))
    L = [len(got[k].split()) for k in ids]; O = [len(mid[k]) for k in ids]
    same = sum(got[k].split() == mid[k] for k in ids); eq = sum(a == o for a, o in zip(L, O)); sh = sum(a < o for a, o in zip(L, O)); lo = sum(a > o for a, o in zip(L, O))
    r = (b, len(ids), sum(L) / len(L), sum(O) / len(O), 100 * same / len(ids), 100 * eq / len(ids), 100 * sh / len(ids), 100 * lo / len(ids), time.time() - t)
    rows.append(r); print('budget %d: n %d, mean length %.3f (official %.3f), same text %.1f%%, same length %.1f%%, shorter %.1f%%, longer %.1f%%, %.0f s' % r, flush=True)
with open(f'/data/fmc/scramble-difficulty/research/out/calib_{era}.tsv', 'a') as f:
    for r in rows: f.write('\t'.join(f'{x:.4f}' if isinstance(x, float) else str(x) for x in r) + '\n')
