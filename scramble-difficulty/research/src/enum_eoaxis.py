#!/usr/bin/env python3
"""Which EO axis each DR comes from.  Same DR lists as enum_drs.py (EO <= 5 with NISS, then DR, total <= 10), but
for every scramble the output is the number of distinct DR states per (EO axis, DR axis), and the number of distinct
EOs (as cubelib writes them, NISS included) per EO axis that lead to a DR.
usage: enum_eoaxis.py in.tsv out.tsv [workers]      out: id, then dr_<eo>_<dr> for the six pairs, eos_<eo> for the three axes"""
import sys, re, subprocess, multiprocessing
import enum_drs as E
me, fc = E.me, E.fc
AXN = {'ud': 'UD', 'fb': 'FB', 'lr': 'RL'}
PAIRS = [(e, a) for e in ('UD', 'FB', 'RL') for a in ('UD', 'FB', 'RL') if a != e]

def work(job):
    k, scramble = job
    out = subprocess.run(['cubelib-cli', '--no-check-update', 'solve', '-s', E.STEPS, '-q', '0', '-M', str(E.CAP), '-f', 'detailed', scramble],
                         capture_output=True, text=True).stdout
    ps = me.perm(fc.parse(scramble))
    states = {p: set() for p in PAIRS}; eos = {e: set() for e in ('UD', 'FB', 'RL')}
    for block in out.split('\n\n'):
        sol = re.search(r'^Solution \((\d+)\): ?(.*)$', block, re.M)
        ax = re.search(r'//\s*dr(ud|fb|lr)', block)
        eo = re.search(r'^(.*?)//\s*eo(ud|fb|lr)\s*\((\d+)/', block, re.M)
        if not sol or not ax or not eo: continue
        e, a = AXN[eo.group(2)], AXN[ax.group(1)]
        assert e != a, block
        n, i = fc.split_niss(sol.group(2))
        cn, ci = me.canon(n), me.canon(i)
        V = me.VIEWS[{'UD': 'U/D', 'FB': 'F/B', 'RL': 'R/L'}[a]]
        arr = V.arrays(me.state(ps, cn, ci))
        states[(e, a)].add(tuple(map(tuple, arr)))
        eos[e].add(eo.group(1).strip())
    return k, [len(states[p]) for p in PAIRS] + [len(eos[e]) for e in ('UD', 'FB', 'RL')]

if __name__ == '__main__':
    inp, outp = sys.argv[1], sys.argv[2]; W = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    jobs = [tuple(l.rstrip('\n').split('\t')[:2]) for l in open(inp) if l.strip()]
    with open(outp, 'w') as f, multiprocessing.Pool(W) as pool:
        f.write('id\t' + '\t'.join(f'dr_{e}_{a}' for e, a in PAIRS) + '\teos_UD\teos_FB\teos_RL\n')
        for d, (k, v) in enumerate(pool.imap_unordered(work, jobs, chunksize=2)):
            f.write(k + '\t' + '\t'.join(map(str, v)) + '\n'); f.flush()
            if (d + 1) % 500 == 0: print(d + 1, flush=True)
