#!/usr/bin/env python3
"""Checks before any number is used (SPEC "Checks"):

1. the per-subset optimal-finish distribution from the Lean-checked table (htrtools dist) against
   (a) the first study's census (judging-a-dr/research/out/census.csv) and (b) Joba's doc 580, count by count;
2. the 663,552 HTR states against DougCube's "3x3x3 HTR Finish" tab (doc 218, mean 10.13432557), count by count;
3. the DR->HTR length per subset (every HTR coset is the same size) against Joba's docs 566 / 567.

Input: out/checks/{dist48,htr_states,htr48}.tsv.  Output: out/checks/check_dist.txt (also printed)."""
import csv, collections, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out', 'checks')
ATT = '/data/fmc/assets/attachments'
lines = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); lines.append(s)

ours = collections.Counter()
for r in csv.DictReader(open(f'{OUT}/dist48.tsv'), delimiter='\t'):
    ours[(r['subset'], int(r['depth']))] = int(r['states'])
say('total states', sum(ours.values()))

# (a) first study census
c1 = collections.Counter()
for r in csv.DictReader(open('/data/fmc/judging-a-dr/research/out/census.csv')):
    c1[(r['subset'], int(r['depth']))] += int(r['count'])
bad = [k for k in set(ours) | set(c1) if ours[k] != c1[k]]
say(f'(1a) vs first study census.csv: {len(set(ours))} (subset, depth) cells, {len(bad)} differ')

# (b) Joba doc 580
j = collections.Counter(); cur = None
for l in open(f'{ATT}/1406633631165714492_0_drfin_subset_dist.txt'):
    if not l.strip(): continue
    m = re.match(r'\s*-\s*(\d+):\s*(\d+)', l)
    if m: j[(cur, int(m.group(1)))] = int(m.group(2))
    else: cur = l.strip().replace('4c5', '4b5')
bad = [k for k in set(ours) | set(j) if ours[k] != j[k]]
say(f'(1b) vs Joba doc 580 (4c5 read as 4b5): {len(set(j))} cells, {len(bad)} differ', bad[:5])

# 2. DougCube
dc = {}
for r in csv.reader(open('/data/fmc/kb/docs/gsheet/1p5goyNTGe_rlIqVslV4bJJzHNmKETUlrU-ndj9EIWAo/3x3x3_HTR_Finish.csv')):
    if len(r) > 2 and re.match(r'^\d+\.0$', r[1] or ''):
        dc[int(float(r[1]))] = int(float(r[2]))
ht, dr = {}, {}
for r in csv.DictReader(open(f'{OUT}/htr_states.tsv'), delimiter='\t'):
    ht[int(r['depth'])] = int(r['half_turn_optimal']); dr[int(r['depth'])] = int(r['dr_optimal'])
mean = lambda h: sum(k * v for k, v in h.items()) / sum(h.values())
same = all(dc.get(d, 0) == ht.get(d, 0) for d in set(dc) | set(ht))
say(f'(2) DougCube HTR Finish: {sum(dc.values())} states, mean {mean(dc):.8f}; ours half-turn-only: {sum(ht.values())} '
    f'states, mean {mean(ht):.8f}; all depth counts equal: {same}')
say(f'    the same 663,552 HTR states with any DR move allowed (HTR-breaking finishes): mean {mean(dr):.5f}, '
    f'{sum(v for d, v in dr.items() if d < 99)} states; max {max(d for d, v in dr.items() if v)} vs {max(d for d, v in ht.items() if v)}')

# 3. docs 566 / 567
h48 = collections.defaultdict(collections.Counter)
for r in csv.DictReader(open(f'{OUT}/htr48.tsv'), delimiter='\t'):
    h48[r['subset']][int(r['htr_len'])] += int(r['cosets'])
def joba(path):
    out = collections.defaultdict(dict); share = {}; cur = None
    for l in open(path):
        if not l.strip(): continue
        m = re.match(r'\s*-\s*(\d+):\s*([\d.]+)%', l)
        if m: out[cur][int(m.group(1))] = float(m.group(2))
        else:
            n, p = l.strip().split(':'); cur = n.replace('4c5', '4b5'); share[cur] = float(p.strip().rstrip('%'))
    return out, share
w, wshare = joba(f'{ATT}/1357402650441945299_0_subsets_with_edges.txt')
agree = disagree = 0; bads = []
for s, dd in w.items():
    tot = sum(h48[s].values())
    ok = abs(wshare[s] - 100 * tot / 29400) < 1e-4 and all(abs(dd.get(k, 0) - 100 * h48[s][k] / tot) < 1e-4 for k in set(dd) | set(h48[s]))
    agree += ok; disagree += not ok
    if not ok: bads.append(s)
say(f'(3) Joba doc 566 (DR->HTR length per subset, with edges): {agree} of {agree + disagree} subsets agree to 1e-4 %; differ: {bads}')
for s in bads[:6]:
    tot = sum(h48[s].values())
    say(f'    {s}: doc 566 {dict(sorted(w[s].items()))}  exact {dict(sorted((k, round(100 * v / tot, 4)) for k, v in h48[s].items()))}')
open(f'{OUT}/check_dist.txt', 'w').write('\n'.join(lines) + '\n')
