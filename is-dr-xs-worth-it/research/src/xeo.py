#!/usr/bin/env python3
"""The normal route by EO length, on the 500 scrambles: with EOs of at most 4 moves, and of at most 5, how many EOs
there are, how many DRs of 10 / 11 moves or less they lead to, and the best solution through those DRs (optimal
finishes).  Uses the first study's many_examples.py (cubelib-cli for the DRs, the exact table for the finishes).
Writes out/eo_run.tsv."""
import sys, re, subprocess, multiprocessing, os
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src'); sys.path.insert(0, '/data/fmc/judging-a-dr/research/src/report_build')
import many_examples as me
O = '/data/fmc/is-dr-xs-worth-it/research/out/'
def n_eos(scramble, eomax):
    out = subprocess.run(['cubelib-cli', '--no-check-update', 'solve', '-s', f'EO[niss=always;max={eomax}]', '-q', '0', '-M', str(eomax), '-f', 'detailed', scramble],
                         capture_output=True, text=True).stdout
    return len(re.findall(r'^Solution \(\d+\)', out, re.M))
def work(job):
    idx, scr = job; row = [idx]
    for eomax in (4, 5):
        me.STEPS = f'EO[niss=always;max={eomax}] > DR[niss=before;max=12]'
        found = me.cubelib(scr, 11)
        if found:
            recs = [r for r in me.drs_of(scr, 11) if r['length'] <= 11]
        else: recs = []
        row += [n_eos(scr, eomax), sum(r['length'] <= 10 for r in recs), len(recs), min([r['total'] for r in recs if r['length'] <= 10], default=99), min([r['total'] for r in recs], default=99)]
    return row
if __name__ == '__main__':
    scr = [l.strip() for l in open(me.SCR) if l.strip() and not l.startswith('#')]
    n = int(sys.argv[1]) if len(sys.argv) > 1 else len(scr)
    with multiprocessing.Pool(int(sys.argv[2]) if len(sys.argv) > 2 else 4) as pool:
        rows = pool.map(work, [(i + 1, s) for i, s in enumerate(scr[:n])], chunksize=2)
    with open(O + 'eo_run.tsv' if n == len(scr) else O + 'eo_run_test.tsv', 'w') as f:
        f.write('scramble\teos4\tdrs10_eo4\tdrs11_eo4\tbest10_eo4\tbest11_eo4\teos5\tdrs10_eo5\tdrs11_eo5\tbest10_eo5\tbest11_eo5\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    print(len(rows), 'scrambles')
