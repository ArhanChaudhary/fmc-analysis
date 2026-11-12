#!/usr/bin/env python3
"""Run `instools best --L 8,10,12 --mixed` on every case of out/real_cases.tsv, one process per case, three at a time.
The model `mixed` at L = 12 can take very long on edge leftovers: a case that is not done after 120 seconds is run
again as `--L 8,10 --mixed` plus `--L 12` without `mixed`, and is listed in out/real_best.skipped.
Results are kept per (scramble, skeleton) in out/real_cache.json, so a second run only computes what is new.
Writes out/real_best.txt in the format of `best --file` (case numbers = line numbers of real_cases.tsv)."""
import subprocess, sys, re, json, os
from concurrent.futures import ThreadPoolExecutor
OUT = '/data/fmc/insertion-cost/research/out/'
BIN = '/data/fmc/insertion-cost/research/instools/target/release/instools'
CACHE = OUT + 'real_cache.json'
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
def run(args, timeout=None):
    return subprocess.run([BIN, 'best'] + args, capture_output=True, text=True, timeout=timeout).stdout
def one(job):
    k, scr, sk = job; key = scr + '|' + sk
    if key not in cache:
        try:
            out = run([scr, sk, '--L', '8,10,12', '--mixed'], timeout=120); skipped = False
        except subprocess.TimeoutExpired:
            a = run([scr, sk, '--L', '8,10', '--mixed']); b = run([scr, sk, '--L', '12'])
            out = a.rstrip('\n') + '\n' + '\n'.join(l for l in b.split('\n') if l.startswith(('L=12', '   ', 'SOL'))) + '\n'; skipped = True
        cache[key] = [out, skipped]
    out, skipped = cache[key]
    out = re.sub(r'^CASE\t1$', f'CASE\t{k}', out, flags=re.M)
    out = re.sub(r'^SOL\t1\t', f'SOL\t{k}\t', out, flags=re.M)
    return out.rstrip('\n') + '\n\n', skipped
if __name__ == '__main__':
    jobs = []
    for k, line in enumerate(open(OUT + 'real_cases.tsv'), 1):
        scr, sk, _ = line.rstrip('\n').split('\t'); jobs.append((k, scr, sk))
    new = sum(1 for j in jobs if j[1] + '|' + j[2] not in cache)
    with ThreadPoolExecutor(3) as ex: res = list(ex.map(one, jobs))
    json.dump(cache, open(CACHE, 'w'))
    open(OUT + 'real_best.txt', 'w').write(''.join(r[0] for r in res))
    open(OUT + 'real_best.skipped', 'w').write('\n'.join(str(j[0]) for j, r in zip(jobs, res) if r[1]) + '\n')
    print(len(jobs), 'cases,', new, 'computed now;', sum(r[1] for r in res), 'without `mixed` at L = 12 (not done in 120 s)')
