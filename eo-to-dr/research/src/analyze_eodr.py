#!/usr/bin/env python3
"""Question C (EO -> DR): per-case tables and the 'typical EO -> DR' table.

inputs  out/eodr_exact.tsv    eodrtools eodr exact   (1,082,565 cosets: EO kept, any turns, last-move inversion)
        out/eodr_twoaxis.tsv  eodrtools eodr twoaxis (exact: better of the two DR axes of one EO)
        out/eodr_sample.tsv   eodrtools eodr sample  (uniform EO-solved states, every option and combination)
outputs out/c6_by_case.tsv, out/c7_typical.tsv, out/c6_normal_inverse.tsv, out/c6_axis_pairs.tsv, out/c_stats.json

A case is DR-xcye: x corners twisted for the DR axis (U/D), y edges misplaced for it (E-slice pieces outside the E
slice, plus as many other pieces inside), as on the server and in Cale's 'DR setup stats'."""
import csv, json, os, math, collections

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out')
NV = 12

def rd(name):
    return list(csv.DictReader((l for l in open(os.path.join(OUT, name)) if not l.startswith('#')), delimiter='\t'))

def write(name, rows):
    keys = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(os.path.join(OUT, name), 'w') as f:
        f.write('\t'.join(keys) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(k, '')) for k in keys) + '\n')

def summ(h):
    t = sum(h)
    if t == 0:
        return {}
    m = sum(d * x for d, x in enumerate(h)) / t
    out = {'mean': round(m, 9)}            # 9 decimals: the page rounds once (formatted columns only)
    for k in (4, 5, 6, 7, 8):
        p = sum(h[:k + 1]) / t
        out[f'p_le{k}'] = round(p, 9)
    out['one_in_le6'] = round(t / sum(h[:7]), 2) if sum(h[:7]) else ''
    out['max'] = max(d for d, x in enumerate(h) if x)
    return out

case = lambda c, e: f'{c}c{e}e'
# exact options per case
ex = collections.defaultdict(lambda: [0] * NV)
for r in rd('eodr_exact.tsv'):
    h = [int(r[f'd{d}']) for d in range(NV)]
    key = (int(r['corners']), int(r['edges']))
    ex[(key, r['option'])] = h
    tot = ex[('all', r['option'])]
    for d in range(NV):
        tot[d] += h[d]
cases = sorted({k for (k, o) in ex if k != 'all'})
# exact two-axis: weights of distance >= v
tw = {}
for r in rd('eodr_twoaxis.tsv'):
    ge = [int(r[f'ge{v}']) for v in range(NV)]
    tw[(r['option'], (int(r['corners']), int(r['edges'])))] = ge
def ge_to_hist(ge):
    return [ge[v] - (ge[v + 1] if v + 1 < NV else 0) for v in range(NV)]
for opt in ('best_of_two_axes', 'ud_only'):
    allge = [sum(tw[(opt, c)][v] for c in cases if (opt, c) in tw) for v in range(NV)]
    tw[(opt, 'all')] = allge
# sampled options per case
sm = rd('eodr_sample.tsv')
so = collections.defaultdict(lambda: [0] * NV)
joint = collections.defaultdict(lambda: [[0] * NV for _ in range(NV)])
pairs = collections.defaultdict(lambda: [0] * NV)
for r in sm:
    h = [int(r[f'd{d}']) for d in range(NV)]
    key = (int(r['corners']), int(r['edges']))
    if r['table'] == 'opt':
        for k in (key, 'all'):
            a = so[(k, r['what'])]
            for d in range(NV):
                a[d] += h[d]
    elif r['table'] == 'joint':
        a = int(r['what'].split('=')[1])
        for k in (key, 'all'):
            for d in range(NV):
                joint[k][a][d] += h[d]
    else:
        pairs[(key, r['what'])] = h
nsample = sum(so[('all', 'plain')])

# consistency: sampled plain against exact plain (and the exact one-axis weights of twoaxis against eodr exact)
stats = {'sampled_states': nsample}
pe, ps = summ(ex[('all', 'eo')]), summ(so[('all', 'plain')])
stats['check_plain_exact_vs_sampled'] = {'exact': pe, 'sampled': ps}
ud = ge_to_hist(tw[('ud_only', 'all')])
stats['check_twoaxis_ud_only_matches_exact'] = all(abs(ud[d] / sum(ud) - ex[('all', 'eo')][d] / 1082565) < 1e-12 for d in range(NV))
stats['check_switch_F_equals_B'] = ex[('all', 'eo_switchF')] == ex[('all', 'eo_switchB')]

rows = []
for k in cases + ['all']:
    n = sum(ex[(k, 'eo')])
    row = {'case': 'all' if k == 'all' else case(*k), 'cosets': n, 'share': round(n / 1082565, 6),
           'one_in': round(1082565 / n, 2)}
    for name, h, kind in (('plain', ex[(k, 'eo')], 'exact'), ('any_turns', ex[(k, 'any')], 'exact'),
                          ('switch_last', ex[(k, 'eo_switchF')], 'exact'),
                          ('two_axes', ge_to_hist(tw[('best_of_two_axes', k)]) if ('best_of_two_axes', k) in tw else None, 'exact'),
                          ('normal_or_inverse', so[(k, 'normal_or_inverse')], 'sampled'),
                          ('all_eo_kept', so[(k, 'all_eo_kept')], 'sampled'),
                          ('everything', so[(k, 'everything')], 'sampled')):
        if h is None or sum(h) == 0:
            continue
        s = summ(h)
        for q in ('mean', 'p_le5', 'p_le6', 'p_le7'):
            row[f'{name}_{q}'] = s[q]
    rows.append(row)
write('c6_by_case.tsv', rows)

# C7: the typical EO -> DR, overall
c7 = []
def add(name, h, kind, note=''):
    s = summ(h)
    c7.append({'option': name, 'kind': kind, 'states': sum(h) if kind == 'sampled' else '', **s, 'note': note})
add('one DR axis, EO kept, normal (the known table)', ex[('all', 'eo')], 'exact', 'Cale doc 6 / EO-DR-47')
add('one DR axis, any turns (EO may break)', ex[('all', 'any')], 'exact', 'torchlight T2600')
add('one DR axis, EO kept, last EO turn inverted if better', ex[('all', 'eo_switchF')], 'exact', '')
add('one DR axis, any turns, last EO turn inverted if better', ex[('all', 'any_switchF')], 'exact', '')
add('better of the two DR axes, EO kept', ge_to_hist(tw[('best_of_two_axes', 'all')]), 'exact', '')
for name, key in (('one DR axis, EO kept, on the inverse only', 'inverse_only'),
                  ('one DR axis, EO kept, better of normal and inverse', 'normal_or_inverse'),
                  ('two DR axes x last turn inverted, EO kept, normal', 'two_axes_switch'),
                  ('two DR axes x normal/inverse, EO kept', 'two_axes_inverse'),
                  ('two axes x normal/inverse x last turn, EO kept', 'all_eo_kept'),
                  ('two DR axes, any turns, normal', 'any_two_axes'),
                  ('everything above (EO kept or not)', 'everything'),
                  ('one DR axis, EO kept, normal (sampled, to compare with the exact row)', 'plain')):
    add(name, so[('all', key)], 'sampled')
write('c7_typical.tsv', c7)

# normal against inverse (same DR axis): joint distribution and correlation
def corr(j):
    n = sum(sum(r) for r in j)
    mx = sum(a * sum(j[a]) for a in range(NV)) / n
    my = sum(b * j[a][b] for a in range(NV) for b in range(NV)) / n
    cov = sum((a - mx) * (b - my) * j[a][b] for a in range(NV) for b in range(NV)) / n
    vx = sum((a - mx) ** 2 * sum(j[a]) for a in range(NV)) / n
    vy = sum((b - my) ** 2 * j[a][b] for a in range(NV) for b in range(NV)) / n
    return cov / math.sqrt(vx * vy), n
ni = []
for k in ['all'] + cases:
    j = joint[k]
    if sum(sum(r) for r in j) < 1000:
        continue
    rho, n = corr(j)
    # P(inverse <= 6 | normal = a)
    row = {'case': 'all' if k == 'all' else case(*k), 'states': n, 'correlation': round(rho, 4)}
    for a in range(4, 11):
        tot = sum(j[a])
        row[f'p_inv_le6_given_normal_{a}'] = round(sum(j[a][:7]) / tot, 9) if tot >= 200 else ''
    row['p_inv_le6'] = round(sum(sum(j[a][:7]) for a in range(NV)) / n, 9)
    ni.append(row)
write('c6_normal_inverse.tsv', ni)
stats['joint_all'] = [[joint['all'][a][b] for b in range(NV)] for a in range(NV)]

# pairs of cases on the two DR axes (sampled): better-axis distance
pr = []
for (k, w), h in pairs.items():
    if sum(h) >= 2000:
        s = summ(h)
        pr.append({'ud_case': case(*k), 'rl_case': w.replace('rl=', ''), 'states': sum(h), 'mean_best_axis': s['mean'], 'p_le6': s['p_le6'], 'p_le7': s['p_le7']})
pr.sort(key=lambda r: -r['states'])
write('c6_axis_pairs.tsv', pr)
json.dump(stats, open(os.path.join(OUT, 'c_stats.json'), 'w'), indent=1)
print('C tables written; checks:', stats['check_twoaxis_ud_only_matches_exact'], stats['check_switch_F_equals_B'])
