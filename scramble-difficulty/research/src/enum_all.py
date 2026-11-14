#!/usr/bin/env python3
"""Every EO-first DR of at most 11 moves of each scramble, with its exact optimal finish.

The DR lists are the ones of gaps/research/src/population.py (and of judging-a-dr's examples page):

    cubelib-cli solve -s "EO[niss=always;max=5] > DR[niss=before;max=11]" -q 0 -M 11 -f detailed

an EO of at most 5 on any axis with NISS anywhere in it, then DR on normal or on inverse without breaking that EO.
Each DR is the state as written (quarter turns among the last moves of each side made clockwise), deduplicated per
scramble by (DR axis, state): the first listing, shortest first, gives the length.  The state looked up is the DR on
the side the DR step is written on.  New here: for each DR state, the shortest listing through an EO on each EO axis.

Stage 1 (all workers): cubelib and the state of every listed solution.  Stage 2 (after every CHUNK scrambles): the
optimal finish and subset of every DR state with `htrtools label` (gaps' fork; needs lean_exact_table.u8 and
ls_depth.u8), written to OUT/part_NNNNN.tsv.gz:
    scr  axis  side  len  eolen  viaUD  viaFB  viaRL  subset  d  [moves]
(via* = shortest listing of this DR state through an EO on that axis, 99 if none; moves only with --moves), and
OUT/done_NNNNN.txt with the ids of the chunk (a scramble with no DR is in done only).  A rerun skips ids already done.

Runs on Python 3.9 with nothing but this folder (drstate.py, fmccube.py), a cubelib-cli binary and htrtools.
cubelib writes its pruning tables to ~/.cubelib on first use: set CUBELIB_HOME to keep them elsewhere.
usage: CUBELIB=... HTRTOOLS=... TABLES=dir [CUBELIB_HOME=dir] enum_all.py in.tsv OUT [workers] [chunk] [--moves]"""
import sys, os, re, subprocess, multiprocessing, gzip, glob, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import drstate as ds
fc = ds.fc

STEPS = 'EO[niss=always;max=5] > DR[niss=before;max=11]'
CAP = 11
CUBELIB = os.environ.get('CUBELIB', 'cubelib-cli')
HTRTOOLS = os.environ.get('HTRTOOLS', 'htrtools')
TABLES = os.environ.get('TABLES', '.')
AXN = {'ud': 'U/D', 'fb': 'F/B', 'lr': 'R/L'}
EOI = {'ud': 0, 'fb': 1, 'lr': 2}
MOVES = '--moves' in sys.argv

ENV = dict(os.environ)
if os.environ.get('CUBELIB_HOME'): ENV['HOME'] = os.environ['CUBELIB_HOME']    # cubelib keeps its tables in ~/.cubelib

def cubelib(scramble):
    run = subprocess.run([CUBELIB, '--no-check-update', 'solve', '-s', STEPS, '-q', '0', '-M', str(CAP), '-f', 'detailed', scramble],
                         capture_output=True, text=True, env=ENV)
    assert run.returncode == 0, (scramble, run.returncode, run.stderr[-300:])
    out = run.stdout
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
        res.append((n, i, AXN[ax.group(1)], side, int(eo.group(3)) if eo else -1, EOI[eo.group(2)] if eo else -1))
    return res

def work(job):
    k, scramble = job
    sc = fc.parse(scramble)
    ps = ds.perm(sc); psi = ds.perm(fc.invert(sc))
    seen = {}; rows = []
    found = cubelib(scramble)
    # the order of cubelib's listing varies from run to run; ties (the same moves listed with the DR step on either
    # side, or through EOs of two lengths) are broken by side (normal first) and EO length, so that a rerun gives the same rows
    for n, i, axis, side, eol, eoax in sorted(found, key=lambda t: (len(t[0]) + len(t[1]), ds.niss(ds.canon(t[0]), ds.canon(t[1])), t[2], t[3] == 'I', t[4], t[5])):
        cn, ci = ds.canon(n), ds.canon(i)
        V = ds.VIEWS[axis]
        a = V.arrays(ds.state(ps, cn, ci))           # I^-1 S N
        assert a is not None, (scramble, n, i, axis)
        key = (axis, tuple(map(tuple, a)))
        L = len(n) + len(i)
        if key in seen:
            r = seen[key]
            if eoax >= 0 and L < r[5 + eoax]: r[5 + eoax] = L
            continue
        if side == 'I':                              # inverse side: N^-1 S^-1 I, on stickers
            b = V.arrays(ds.state(psi, ci, cn))
            assert b is not None and all(ds.invperm(x) == y for x, y in zip(a, b)), (scramble, n, i, axis)
        else:
            b = a
        r = [k, axis, side, L, eol, 99, 99, 99, ds.rank(b[0]), ds.rank(b[1]), ds.rank(b[2]), ds.niss(cn, ci)]
        if eoax >= 0: r[5 + eoax] = L
        seen[key] = r; rows.append(r)
    return k, rows

def flush(out, idx, buf):
    """label the DR states of a chunk and write it"""
    ces = os.path.join(out, 'tmp_%05d.ces' % idx)
    with open(ces, 'w') as f:
        for k, rows in buf:
            for r in rows: f.write('%d %d %d\n' % (r[8], r[9], r[10]))
    lab = subprocess.run([HTRTOOLS, 'label', os.path.join(TABLES, 'lean_exact_table.u8'), os.path.join(TABLES, 'ls_depth.u8')],
                         stdin=open(ces), capture_output=True, text=True)
    assert lab.returncode == 0, lab.stderr[-500:]
    labels = lab.stdout.split('\n')
    assert labels[0].startswith('subset\t'), labels[0]
    labels = [l for l in labels[1:] if l]
    assert len(labels) == sum(len(rows) for k, rows in buf), (len(labels), idx)
    j = 0; tmp = os.path.join(out, 'tmp_%05d.tsv.gz' % idx)
    with gzip.open(tmp, 'wt', compresslevel=4) as f:
        for k, rows in buf:
            for r in rows:
                l = labels[j].split('\t'); j += 1
                f.write('\t'.join(map(str, r[:8] + [l[0], l[1]] + ([r[11]] if MOVES else []))) + '\n')
    os.rename(tmp, os.path.join(out, 'part_%05d.tsv.gz' % idx)); os.remove(ces)
    with open(os.path.join(out, 'done_%05d.txt' % idx), 'w') as f:
        f.write('\n'.join(k for k, rows in buf) + '\n')

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    inp, out = args[0], args[1]; W = int(args[2]) if len(args) > 2 else 4; CHUNK = int(args[3]) if len(args) > 3 else 500
    os.makedirs(out, exist_ok=True)
    done = set()
    for p in glob.glob(os.path.join(out, 'done_*.txt')): done.update(open(p).read().split())
    idx = 1 + max([int(os.path.basename(p)[5:10]) for p in glob.glob(os.path.join(out, 'done_*.txt'))] or [-1])
    jobs = [tuple(l.rstrip('\n').split('\t')[:2]) for l in open(inp) if l.strip() and not l.startswith('#')]
    jobs = [j for j in jobs if j[0] not in done]
    print('%d scrambles to do, %d done before; %d workers' % (len(jobs), len(done), W), flush=True)
    if jobs: cubelib(jobs[0][1])                 # one run alone first: cubelib writes its tables on first use
    t0 = time.time(); n = 0; tot = 0; buf = []
    with multiprocessing.Pool(W) as pool:
        for k, rows in pool.imap_unordered(work, jobs, chunksize=1):
            buf.append((k, rows)); n += 1; tot += len(rows)
            if len(buf) >= CHUNK:
                flush(out, idx, buf); idx += 1; buf = []
                print('%d scrambles, %d DRs, %.0f s' % (n, tot, time.time() - t0), flush=True)
    if buf: flush(out, idx, buf)
    print('finished: %d scrambles, %d DRs, %.0f s' % (n, tot, time.time() - t0), flush=True)

if __name__ == '__main__':
    main()
