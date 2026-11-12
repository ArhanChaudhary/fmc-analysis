#!/usr/bin/env python3
"""The tables of the report (report/data/*.md) and the few extra numbers the text needs (out/report_extra.json),
read from the outputs of the computations (out/*.tsv, out/*_stats.json, out/big/scr50k.tsv).  Nothing here is new
computation except the odds at several targets of the best route through an EO (A2), read off the per-scramble table.

usage: xtables.py"""
import csv, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..', 'out')) + '/'
DATA = os.path.normpath(os.path.join(HERE, '..', '..', 'report', 'data')) + '/'
AX = ['RL', 'UD', 'FB']
csv.field_size_limit(10**8)


def pc(x, d=None):
    """A share as a percentage: one decimal, two below 1%, more below 0.1%, '0' for none."""
    x = float(x) * 100
    if x == 0:
        return '0%'
    if x >= 99.95 and x < 100:
        return '>99.9%'
    if x < 0.00005:
        return '< 0.0001%'
    if d is None:
        d = 1 if x >= 1 else 2 if x >= 0.1 else 3 if x >= 0.01 else 4
    return f'{x:.{d}f}%'


def rd(name):
    return list(csv.DictReader(open(OUT + name), delimiter='\t'))


def table(name, head, rows):
    os.makedirs(DATA, exist_ok=True)
    lines = ['| ' + ' | '.join(head) + ' |', '|' + '|'.join('---' if i == 0 else '---:' for i in range(len(head))) + '|']
    for r in rows:
        assert len(r) == len(head), (name, r)
        lines.append('| ' + ' | '.join(str(x) for x in r) + ' |')
    firsts = [tuple(r[:1]) for r in rows]
    open(DATA + name + '.md', 'w').write('\n'.join(lines) + '\n')


EXTRA = {}

# ------------------------------------------------------------------------------------------------ A1
A1_NAMES = {
    'fixed axis, exact (all 2,217,093,120 cosets)': ('One fixed axis, normal', 'exact, all 2,217,093,120 cosets'),
    'fixed axis, all three axes pooled, sampled': ('One fixed axis, normal (each of the 3 axes)', 'sampled, 150,000 axes'),
    'best of 3 axes, normal (linear)': ('Best of 3 axes, normal', 'sampled, 50,000'),
    'best of 3 axes, inverse (linear)': ('Best of 3 axes, inverse', 'sampled, 50,000'),
    'best of 6 (3 axes x normal/inverse, linear)': ('Best of 6: 3 axes, normal or inverse', 'sampled, 50,000'),
    'NISS (moves on both sides), best of 3 axes': ('NISS: 3 axes, moves on both sides', 'sampled, 50,000'),
}


def a1_rows(tag):
    rows = []
    for r in rd(f'{tag}_a1.tsv'):
        if r['what'] not in A1_NAMES:
            continue
        h = [int(r[f'n{d}']) for d in range(13)]
        n = sum(h)
        le = lambda k: sum(h[:k + 1]) / n
        name, kind = A1_NAMES[r['what']]
        rows.append([name, kind, f"{float(r['mean']):.2f}", pc(le(8)), pc(le(9)), pc(le(10)), pc(le(11)), r['max']])
    return rows


H_A1 = ['Shortest DR from the scramble', 'Exact or sampled', 'Mean', '≤ 8', '≤ 9', '≤ 10', '≤ 11', 'Longest']
table('a1', H_A1, a1_rows('a50k'))

# the nissy-scramble comparison (method appendix)
rows = []
u = {r[0]: r for r in a1_rows('a50k')}
v = {r[0]: r for r in a1_rows('nissy50k')}
for k in u:
    if 'exact' in u[k][1]:
        continue
    rows.append([k, u[k][2], v[k][2], u[k][3], v[k][3], u[k][4], v[k][4]])
table('nissy_bias', ['Shortest DR (50,000 scrambles each)', 'Mean, uniform', 'Mean, nissy scramble', '≤ 8, uniform', '≤ 8, nissy scramble', '≤ 9, uniform', '≤ 9, nissy scramble'], rows)
cs = [r for r in rd('checks_scrambles.tsv')]
table('scramble_checks', ['Scrambles', 'Axis', 'What is counted', 'chi² (df)'],
      [[{'mkscr': 'this study (uniform states)', 'nissy': 'nissy 2.0.8 `scramble`', 'judging500': "judging-a-dr's 500"}[r['scrambles']] + f" ({int(r['n']):,})",
        r['axis'], r['what'], f"{r['chi2']} ({r['df']})"] for r in cs])

# number of DR solutions per length (normal side, 3 axes)
rows = []
for r in rd('a50k_a1_counts.tsv'):
    if r['length'] == 'optimal':
        continue
    rows.append([r['length'], f"{float(r['mean_dr_solutions']):,.1f}" if float(r['mean_dr_solutions']) >= 10 else r['mean_dr_solutions'],
                 f"{float(r['median']):,.0f}", pc(r['p_at_least_one']), f"{int(r['max']):,}"])
table('a1_solutions', ['Length', 'Mean number of DR solutions', 'Median', 'At least one', 'Most on one scramble'], rows)
opt = [r for r in rd('a50k_a1_counts.tsv') if r['length'] == 'optimal'][0]
EXTRA['nopt_mean'] = float(opt['mean_dr_solutions'])
EXTRA['nopt_median'] = float(opt['median'])
EXTRA['nopt_le2'] = float(opt["p_at_most_2 (one, up to the last turn's direction)"])

# ------------------------------------------------------------------------------------------------ per-scramble table
print('reading scr50k.tsv ...', file=sys.stderr)
R = list(csv.DictReader(open(OUT + 'big/scr50k.tsv'), delimiter='\t'))
N = len(R)
col = lambda k: np.array([int(r[k]) for r in R])
dn = np.stack([col(f'd_n_{a}') for a in AX], 1)
di = np.stack([col(f'd_i_{a}') for a in AX], 1)
dlin, dinv = dn.min(1), di.min(1)
d6 = np.minimum(dlin, dinv)
dniss = col('dniss')
best = {kind: np.stack([np.stack([col(f'best_{kind}_{y}_{k}') for k in range(7)], 1) for y in AX], 1) for kind in 'nix'}
bn = best['n'].min(1)                                   # [scramble, length] best over axes
bb = np.minimum(best['n'], best['i']).min(1)
bx = np.minimum(np.minimum(best['n'], best['i']), best['x']).min(1)
upto = lambda b, k: b[:, :k + 1].min(1)                 # best route through an EO of at most k turns

rows = []
def trow(name, v, kind='sampled, 50,000'):
    has = v < 99
    rows.append([name, kind] + [pc((v <= t).mean()) for t in (8, 9, 10, 11, 12)] + [pc(1 - has.mean()) if (~has).any() else '0%', f'{v[has].mean():.2f}'])
trow('Optimal DR, best of 3 axes, normal', dlin)
trow('Optimal DR, best of 6 (normal or inverse)', d6)
trow('Optimal DR with NISS', dniss)
for k in (3, 4, 5, 6):
    trow(f'Through a normal EO of ≤ {k}, DR on normal', upto(bn, k))
for k in (3, 4, 5, 6):
    trow(f'Through a normal or inverse EO of ≤ {k}, DR on the same side', upto(bb, k))
for k in (3, 4, 5, 6):
    trow(f'Through any EO of ≤ {k} (normal, inverse, NISS; a NISS EO takes the DR on the better side)', upto(bx, k))
table('a2_targets', ['DR from the scramble', 'Exact or sampled', '≤ 8', '≤ 9', '≤ 10', '≤ 11', '≤ 12', 'No such EO', 'Mean (where there is one)'], rows)
for k in (4, 5):
    for nm, b in (('n', bn), ('b', bb), ('x', bx)):
        v = upto(b, k)
        for t in (9, 10, 11):
            EXTRA[f'route_{nm}{k}_le{t}'] = float((v <= t).mean())
for t in (8, 9, 10, 11):
    EXTRA[f'opt_lin_le{t}'] = float((dlin <= t).mean()); EXTRA[f'opt6_le{t}'] = float((d6 <= t).mean()); EXTRA[f'optniss_le{t}'] = float((dniss <= t).mean())

# standard deviations of the A1 means (for standard errors)
for nm, v in (('lin', dlin), ('inv', dinv), ('six', d6), ('niss', dniss)):
    EXTRA[f'sd_{nm}'] = float(v.std(ddof=1))
EXTRA['n'] = N
# share of scrambles where the inverse alone beats normal, and normal vs inverse equal
EXTRA['inv_better'] = float((dinv < dlin).mean()); EXTRA['inv_worse'] = float((dinv > dlin).mean())
# no sub-10 on best of 6 / NISS
EXTRA['no_sub10_six'] = float((d6 >= 10).mean()); EXTRA['no_sub10_niss'] = float((dniss >= 10).mean())
EXTRA['no_sub10_niss_n'] = int((dniss >= 10).sum())
EXTRA['no_sub10_lin'] = float((dlin >= 10).mean())

# ------------------------------------------------------------------------------------------------ A2
rows = []
for r in rd('a50k_a2.tsv'):
    k = int(r['k'])
    if k < 3:
        continue
    kind = {'normal EOs, DR on normal': 'normal',
            'normal or inverse EOs, DR on the same side': 'normal or inverse, DR on that side',
            'normal, inverse and NISS EOs, NISS DR side rule': 'normal, inverse or NISS',
            'normal, inverse and NISS EOs, against the best of 6': 'normal, inverse or NISS'}[r['eo_kind']]
    ref = {'optimal normal DR': 'optimal normal DR (3 axes)', 'optimal DR, best of 6': 'optimal DR, best of 6',
           'optimal NISS DR': 'optimal NISS DR'}[r['reference']]
    better = pc(r['p_better_than_optimal_ref']) if r['p_better_than_optimal_ref'] not in ('', '0.0') else '0%'
    rows.append([kind, ref, f'≤ {k}', pc(r['p_has_eo']), pc(r['p_equals_optimal']), better, pc(r['p_loss1']), pc(r['p_loss2']), pc(r['p_loss3plus']),
                 f"{float(r['mean_loss_given_eo']):.2f}"])
table('a2', ['EOs used', 'Compared with', 'EO length', 'Has such an EO', 'Best route = optimal', 'Shorter than it', '1 longer', '2 longer', '3+ longer', 'Mean loss (where there is an EO)'], rows)
A2 = {(r['eo_kind'], int(r['k'])): r for r in rd('a50k_a2.tsv')}
st = json.load(open(OUT + 'a50k_stats.json'))
eh = st['estar_hist']; tot = sum(eh.values())
table('estar', ['Shortest EO inside an optimal DR (turns)'] + [k for k in sorted(eh, key=int)] + ['Mean'],
      [['Share of scrambles'] + [pc(eh[k] / tot) for k in sorted(eh, key=int)] + [f"{st['estar_mean']:.2f}"]])

# ------------------------------------------------------------------------------------------------ A3
rows = []
names = {'normal': 'normal', 'normal + inverse': 'normal or inverse', 'normal + inverse + NISS': 'normal, inverse or NISS (DR on the better side)'}
a3 = rd('a50k_a3.tsv')
grp = {}
for r in a3:
    grp.setdefault((r['eos'], r['axes'], r['eo_max']), {})[int(r['dr_total_max'])] = r
for (eos, axes, k), d in grp.items():
    cells = [f"{float(d[n]['mean_pairs']):.1f} ({pc(d[n]['p_none'], 0) if float(d[n]['p_none']) >= 0.01 else pc(d[n]['p_none'])})" for n in (9, 10, 11, 12)]
    rows.append([names[eos], 'F/B only' if 'one' in axes else 'all three', f'≤ {k}', f"{float(d[9]['mean_eos']):.1f}"] + cells)
table('a3', ['EOs', 'EO axes', 'EO length', 'EOs per scramble', 'Total ≤ 9', 'Total ≤ 10', 'Total ≤ 11', 'Total ≤ 12'], rows)
g = st['a3_gains']
rows = []
for N_ in (9, 10, 11, 12):
    x = g[f'normal_N{N_}']
    rows.append([f'≤ {N_}', f"{x['drs_per_eo_le4']:.3f}", f"{x['drs_per_5move_eo']:.4f}", f"{25 * x['drs_per_eo_le4']:.1f}", f"{200 * x['drs_per_5move_eo']:.1f}"])
table('a3_yield', ['Total (EO + DR)', 'Per EO of ≤ 4', 'Per EO of exactly 5', '25 EOs of ≤ 4', '200 EOs of exactly 5'], rows)

# ------------------------------------------------------------------------------------------------ B4
b4 = rd('a50k_b4.tsv')
bk = {(r['eos'], r['axes'], int(r['length'])): r for r in b4}
rows = []
for eos, en in (('linear (normal)', 'normal'), ('normal or inverse (linear)', 'normal or inverse'), ('NISS (normal, inverse, both)', 'normal, inverse or NISS')):
    for axes, an in (('one axis (F/B)', 'F/B only'), ('all three axes', 'all three')):
        r3, r4, r5, r6 = (bk[(eos, axes, k)] for k in (3, 4, 5, 6))
        rows.append([en, an, f"{float(r3['mean_le']):.2f}", f"{float(r4['mean_le']):.1f} ({float(r4['median_le']):.0f})", f"{float(r5['mean_le']):.0f} ({float(r5['median_le']):.0f})",
                     f"{float(r6['mean_le']):,.0f}", pc(r4['p_none_le']), pc(r5['p_none_le']), f"{int(r5['max_le']):,}"])
table('b4', ['EOs', 'Axes', '≤ 3: mean', '≤ 4: mean (median)', '≤ 5: mean (median)', '≤ 6: mean', 'None ≤ 4', 'None ≤ 5', 'Most ≤ 5 on one scramble'], rows)
EXTRA['b4'] = {f'{e}|{a}|{k}': {kk: r[kk] for kk in ('mean_le', 'median_le', 'p_none_le', 'min_le', 'max_le')} for (e, a, k), r in bk.items()}

bs = json.load(open(OUT + 'b_stats.json'))
rows = []
oh = bs['one_axis_optimal_hist']; t = sum(oh.values())
def orow(name, kind, h, mean):
    t = sum(h.values())
    le = lambda k: sum(v for kk, v in h.items() if int(kk) <= k) / t
    mx = max(int(k) for k, v in h.items() if v)
    rows.append([name, kind, f'{float(mean):.3f}'] + [pc(le(k)) for k in (2, 3, 4, 5)] + [str(mx)])
orow('One fixed axis, normal', 'exact, 2,048 EO states', oh, 9439 / 2048)
orow('Best of 3 axes, normal', 'sampled, 1,000,000', bs['any_axis_linear']['hist'], bs['any_axis_linear']['mean'])
orow('Best of 3 axes, normal or inverse', 'sampled, 1,000,000', bs['any_axis_lin_or_inv']['hist'], bs['any_axis_lin_or_inv']['mean'])
orow('Best of 3 axes with NISS', 'sampled, 1,000,000', bs['any_axis_niss']['hist'], bs['any_axis_niss']['mean'])
table('b4_opt', ['Shortest EO', 'Exact or sampled', 'Mean', '≤ 2', '≤ 3', '≤ 4', '≤ 5', 'Longest seen'], rows)

# ------------------------------------------------------------------------------------------------ B5
rows = []
for r in rd('b5_by_bad.tsv'):
    rows.append([r['bad'], r['p_state'], pc(r['p_linear_le3']), pc(r['p_linear_le4']), pc(r['p_linear_le5']),
                 pc(r['p_lin_or_inv_le4']), pc(r['p_lin_or_inv_le5']), pc(r['p_niss_le3']), pc(r['p_niss_le4']), pc(r['p_niss_le5']),
                 r['optimal_hist'].replace(' ', ', '), f"{int(r['sampled_axes']):,}"])
table('b5_by_bad', ['Bad edges', 'Share of axes', 'Normal ≤ 3', 'Normal ≤ 4', 'Normal ≤ 5', 'Normal or inverse ≤ 4', 'Normal or inverse ≤ 5', 'NISS ≤ 3', 'NISS ≤ 4', 'NISS ≤ 5',
                    'Shortest normal EO: length: states', 'Sampled axes (NISS columns)'], rows)
EXTRA['b5'] = {r['bad']: r for r in rd('b5_by_bad.tsv')}
rows = [[r['sorted_triple'], r['probability'], pc(r['p'])] for r in rd('b5_sorted.tsv')]
table('b5_sorted', ['Bad edges on the three axes (sorted)', 'Probability (exact)', 'As a percentage'], rows)
table('b5_top', ['Bad edges on the three axes (sorted)', 'Probability (exact)', 'As a percentage'], rows[:8])

# ------------------------------------------------------------------------------------------------ C
rows = []
for r in rd('c7_typical.tsv'):
    if r['option'].startswith('one DR axis, EO kept, normal (sampled'):
        continue
    kind = 'exact, 1,082,565 states' if r['kind'] == 'exact' else f"sampled, {int(r['states']):,}"
    rows.append([r['option'], kind, f"{float(r['mean']):.3f}", pc(r['p_le4']), pc(r['p_le5']), pc(r['p_le6']), pc(r['p_le7']), pc(r['p_le8']), r['one_in_le6']])
table('c7', ['After the EO: DR with', 'Exact or sampled', 'Mean', '≤ 4', '≤ 5', '≤ 6', '≤ 7', '≤ 8', '1 in … for ≤ 6'], rows)
EXTRA['c7'] = {r['option']: r for r in rd('c7_typical.tsv')}

cases = [r for r in rd('c6_by_case.tsv') if r['case'] not in ('all', '0c0e')]
NIC = {r['case']: r for r in rd('c6_normal_inverse.tsv')}
cases.sort(key=lambda r: -float(r['share']))
def crow(r, full):
    base = [r['case'], pc(r['share']), f"1 in {1082565 / int(r['cosets']):,.1f}"]
    if full:
        ns = int(NIC[r['case']]['states']) if r['case'] in NIC else round(10000000 * int(r['cosets']) / 1082565)
        return base + [f"{float(r[k + '_mean']):.2f} / {pc(r[k + '_p_le6'])}" for k in ('plain', 'any_turns', 'switch_last', 'two_axes', 'normal_or_inverse', 'all_eo_kept')] + [(f'{ns:,}' if r['case'] in NIC else f'about {ns:,}') + (' (few)' if ns < 1100 else '')]
    return base + [f"{float(r['plain_mean']):.2f}"] + [pc(r[k + '_p_le6']) for k in ('plain', 'switch_last', 'two_axes', 'normal_or_inverse', 'all_eo_kept')]
table('c6_case', ['Case on the DR axis', 'Share of EO-solved states', '1 in', 'Mean, one axis', '≤ 6: one axis', '≤ 6: last EO turn either way', '≤ 6: better of 2 DR axes', '≤ 6: normal or inverse', '≤ 6: all of these'],
      [crow(r, False) for r in cases[:16]])
table('c6_case_full', ['Case on the DR axis', 'Share of EO-solved states', '1 in', 'One axis, EO kept', 'Any turns', 'Last EO turn either way, EO kept', 'Better of 2 DR axes', 'Normal or inverse', 'All EO-keeping options', 'States sampled (last two columns)'],
      [crow(r, True) for r in cases])
EXTRA['c6'] = {r['case']: r for r in rd('c6_by_case.tsv')}
ni = rd('c6_normal_inverse.tsv')
table('c6_normal_inverse', ['Case', 'States sampled', 'Correlation normal/inverse', 'Inverse ≤ 6 when normal is 6', 'when normal is 8', 'Inverse ≤ 6 overall'],
      [[r['case'], f"{int(r['states']):,}", r['correlation'], pc(r['p_inv_le6_given_normal_6']) if r['p_inv_le6_given_normal_6'] else '–',
        pc(r['p_inv_le6_given_normal_8']) if r['p_inv_le6_given_normal_8'] else '–', pc(r['p_inv_le6'])] for r in ni])
EXTRA['c6ni'] = {r['case']: r for r in ni}

# ------------------------------------------------------------------------------------------------ checks
rows = [[r['kind'], r['nissy_step'], f"{int(r['positions']):,}", f"{int(r['agree']):,}"] for r in rd('checks_nissy.tsv')]
table('checks_nissy', ['What', 'nissy step', 'Positions', 'Agree'], rows)
import re as _re
rows = [[_re.sub(r'L=(\d+)', r'of exactly \1', r['check']).replace('(dr -L)', '(nissy dr -L)'), r['scrambles'], r['agree']] for r in rd('checks_counts.tsv')]
table('checks_counts', ['Count', 'Scrambles', 'Agree'], rows)
json.dump(EXTRA, open(OUT + 'report_extra.json', 'w'), indent=1, default=str)

# ---- review additions
# routes through EOs of at most 6 too (the odds table promises 3 to 6)
# gain of the 5-movers over the 4-movers (normal EOs, all axes): share improved over the scrambles with an EO of at most 4, mean gain incl. zeros and among the improved
b4v, b5v = upto(bn, 4), upto(bn, 5)
has4 = b4v < 99
imp = has4 & (b5v < b4v)
EXTRA['g54_p_improved_given4'] = float(imp.sum() / has4.sum())
EXTRA['g54_mean_gain_incl0'] = float((b4v - b5v)[has4].mean())
EXTRA['g54_mean_gain_improved'] = float((b4v - b5v)[imp].mean())
# the other two EO axes on top of F/B, EOs of at most 5, normal
fb = best['n'][:, 2, :6].min(1)
allv = upto(bn, 5)
hasfb = fb < 99
EXTRA['ax_p_fb_has5'] = float(hasfb.mean())
EXTRA['ax_p_improved_given_fb'] = float(((allv < fb) & hasfb).sum() / hasfb.sum())
EXTRA['ax_p_improved_all'] = float(((allv < fb) & hasfb).mean() + (~hasfb & (allv < 99)).mean())
EXTRA['ax_p_improved_all_part'] = float(((allv < fb) & hasfb).mean())
EXTRA['ax_p_no_fb'] = float((~hasfb).mean())
EXTRA['ax_mean_fb'] = float(fb[hasfb].mean()); EXTRA['ax_mean_all_same'] = float(allv[hasfb].mean())
# N = 0: an EO already solved on some axis but no 1-move EO
neo = lambda kind, l: sum(col(f'neo_{kind}_{y}_{l}') for y in AX)
h0 = neo('n', 0) > 0
EXTRA['gap0_lin'] = int((h0 & (neo('n', 1) == 0)).sum())
EXTRA['gap0_niss'] = int((h0 & (neo('n', 1) + neo('i', 1) == 0)).sum())
EXTRA['eo_skip_any'] = int(h0.sum())
# the 500 scrambles of judging-a-dr (nissy's scrambler): means and standard errors
R5 = list(csv.DictReader(open(OUT + 'big/scr500.tsv'), delimiter='\t'))
c5 = lambda k: np.array([int(r[k]) for r in R5])
dn5 = np.stack([c5(f'd_n_{a}') for a in AX], 1).min(1); di5 = np.stack([c5(f'd_i_{a}') for a in AX], 1).min(1)
for nm, v, ref in (('lin', dn5, dlin), ('inv', di5, dinv), ('six', np.minimum(dn5, di5), d6)):
    se = float(v.std(ddof=1) / np.sqrt(len(v)))
    EXTRA[f's500_{nm}_mean'] = float(v.mean()); EXTRA[f's500_{nm}_se'] = se
    EXTRA[f's500_{nm}_z'] = float((v.mean() - ref.mean()) / np.sqrt(se ** 2 + ref.var(ddof=1) / len(ref)))
EXTRA['s500_n'] = len(R5)
json.dump(EXTRA, open(OUT + 'report_extra.json', 'w'), indent=1, default=str)
print({k: v for k, v in EXTRA.items() if k.startswith(('g54', 'ax_', 'gap0', 's500', 'eo_skip'))})
print('tables written to', DATA)
