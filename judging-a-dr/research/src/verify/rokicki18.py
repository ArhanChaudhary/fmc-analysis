#!/usr/bin/env python3
"""Tomas Rokicki's list "Distance-18 positions, phase 2 Kociemba, mod 16" (gist of 28 Sep 2021, linked by zakimoshi on
4 Sep 2023; kb copy docs/web/d5a3dc48d67d.md): each position's subset, optimal finish and optimal leave slice, from
`drtools read`.  Output: research/out/verify/rokicki18.txt."""
import re, sys, collections, importlib.util, importlib.machinery
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool'); import fmccube as fc
P = '/data/fmc/judging-a-dr/research/tool/drread'
spec = importlib.util.spec_from_file_location('drread', P, loader=importlib.machinery.SourceFileLoader('drread', P))
dr = importlib.util.module_from_spec(spec); spec.loader.exec_module(dr)
txt = open('/data/fmc/kb/docs/web/d5a3dc48d67d.md').read()
seqs = [' '.join(t) for t in (l.replace('|', ' ').split() for l in txt.split('\n')) if len(t) >= 15 and all(re.fullmatch(r"[UDRLFB][2']?", x) for x in t)]
lines = []
for s in seqs:
    axis, arrs = fc.find_dr(fc.state_after(s)); assert arrs, s
    lines.append(' '.join(map(str, arrs[0] + arrs[1] + arrs[2])))
c = collections.Counter((kv['subset'], kv['optimal'], kv['leave_slice']) for kv in dr.read_states(lines))
print(f'{len(seqs)} positions in the list')
print('positions | subset | optimal finish | optimal leave slice')
for (sub, opt, ls), n in sorted(c.items()): print(f'{n:9d} | {sub} | {opt} | {ls}')
