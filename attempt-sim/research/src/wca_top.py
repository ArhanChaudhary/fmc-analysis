#!/usr/bin/env python3
"""The real results the simulator is compared with: official FMC attempts of the best current solvers.

"Best current solvers": the TOP solvers with the lowest mean over their official attempts since SINCE (DNFs left out
of the mean), among those with at least MIN such attempts.  No names are written: only the group.

Input : out/big/wca/fm_attempts.tsv, fm_scrambles.tsv (wca_extract.py)
Output: out/wca_top_summary.tsv        distribution of the group's results (and of wider groups)
        out/wca_top_attempts.tsv       one row per attempt of the group: solver number, year, value, scramble index
        data/official_scrambles.txt    the scrambles of those attempts (rounds with one scramble group), one per line,
                                       "index<TAB>scramble" (WCA style, with the R' U' F padding)
usage: wca_top.py [TOP=10] [SINCE=2024] [MIN=40]"""
import sys, csv, collections, statistics as st, math, os
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
W = f'{R}/out/big/wca'
TOP = int(sys.argv[1]) if len(sys.argv) > 1 else 10
SINCE = int(sys.argv[2]) if len(sys.argv) > 2 else 2024
MIN = int(sys.argv[3]) if len(sys.argv) > 3 else 40

att = [a for a in csv.DictReader(open(f'{W}/fm_attempts.tsv'), delimiter='\t') if int(a['year']) >= SINCE and a['value'] in ('-1',) or (int(a['year']) >= SINCE and int(a['value']) > 0)]
by = collections.defaultdict(list)
for a in att: by[a['person_id']].append(a)
def mean_ok(rows):
    v = [int(r['value']) for r in rows if int(r['value']) > 0]
    return st.mean(v) if v else 99
elig = sorted((p for p in by if len(by[p]) >= MIN), key=lambda p: mean_ok(by[p]))

def dist(rows):
    v = [int(r['value']) for r in rows]; ok = [x for x in v if x > 0]; n = len(v)
    m = st.mean(ok); sd = st.stdev(ok)
    d = {'attempts': n, 'solvers': len({r['person_id'] for r in rows}), 'mean': round(m, 3), 'se': round(sd / math.sqrt(len(ok)), 3), 'sd': round(sd, 2),
         'dnf_pct': round(100 * (n - len(ok)) / n, 2), 'sub20_pct': round(100 * sum(x < 20 for x in ok) / n, 2),
         'le22_pct': round(100 * sum(x <= 22 for x in ok) / n, 2)}
    for k in range(16, 29): d[f'n_{k}'] = sum(x == k for x in ok)
    d['n_le15'] = sum(x <= 15 for x in ok); d['n_ge29'] = sum(x >= 29 for x in ok)
    return d

rows = []
for top in (5, TOP, 25, 50):
    grp = [a for p in elig[:top] for a in by[p]]
    d = dist(grp); d = {'group': f'top {top} by mean since {SINCE} (at least {MIN} attempts)', **d}; rows.append(d)
with open(f'{R}/out/wca_top_summary.tsv', 'w') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t'); w.writeheader(); w.writerows(rows)
for d in rows: print({k: d[k] for k in ('group', 'attempts', 'solvers', 'mean', 'se', 'sd', 'dnf_pct', 'sub20_pct', 'le22_pct')})
print('per solver means of the top group:', [round(mean_ok(by[p]), 2) for p in elig[:TOP]], 'attempts', [len(by[p]) for p in elig[:TOP]])

# scrambles of the group's attempts
scr = collections.defaultdict(dict); groups = collections.defaultdict(set)
for s in csv.DictReader(open(f'{W}/fm_scrambles.tsv'), delimiter='\t'):
    if s['is_extra'] == '0':
        groups[(s['competition_id'], s['round_type_id'])].add(s['group_id'])
        scr[(s['competition_id'], s['round_type_id'])][s['scramble_num']] = s['scramble']
index = {}; out = []
for k, p in enumerate(elig[:TOP]):
    for a in by[p]:
        key = (a['competition_id'], a['round_type_id'])
        if len(groups.get(key, ())) != 1 or a['attempt'] not in scr[key]: continue
        s = scr[key][a['attempt']]
        i = index.setdefault(s, len(index))
        out.append((k + 1, a['year'], a['value'], i))
with open(f'{R}/data/official_scrambles.txt', 'w') as f:
    for s, i in sorted(index.items(), key=lambda t: t[1]): f.write(f'{i}\t{s}\n')
with open(f'{R}/out/wca_top_attempts.tsv', 'w') as f:
    f.write('solver\tyear\tvalue\tscramble\n')
    for r in out: f.write('\t'.join(map(str, r)) + '\n')
print('attempts with a scramble', len(out), 'of', sum(len(by[p]) for p in elig[:TOP]), '; distinct scrambles', len(index))
