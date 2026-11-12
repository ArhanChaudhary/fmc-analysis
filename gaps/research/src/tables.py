#!/usr/bin/env python3
"""Markdown tables for out/SUMMARY.md from out/a_*.tsv, b_*.tsv, g2.tsv (printed to stdout)."""
import csv, collections, json
G = '/data/fmc/gaps/research/out'
CORN = ['0c0', '2c5', '2c4', '0c3', '4a2', '4a1', '2c3', '0c4', '4c3', '4c4', '4b2', '4b5']
def rd(p): return list(csv.DictReader(open(f'{G}/{p}'), delimiter='\t'))
pc = lambda x: f'{100 * float(x):.1f}'
pse = lambda x, s: f'{100 * float(x):.1f} ± {100 * float(s):.1f}'

def t_subsets():
    R = {(r['group'], r['pop']): r for r in rd('a_subsets.tsv')}
    print('| corner subset | share: uniform | dr11 | scr11 | dr10 | scr10 | mean optimal: uniform | dr11 | scr11 | dr10 | scr10 |')
    print('|---|---|---|---|---|---|---|---|---|---|---|')
    for c in CORN:
        u = R[(c, 'dr11')]
        row = [c, f'{100 * float(u["uniform_share"]):.2f}%']
        row += [f'{100 * float(R[(c, p)]["share"]):.2f} ± {100 * float(R[(c, p)]["se"]):.2f}' for p in ('dr11', 'scr11', 'dr10', 'scr10')]
        row += [u['uniform_mean']] + [f'{R[(c, p)]["mean_opt"]} ± {R[(c, p)]["se_mean"]}' for p in ('dr11', 'scr11', 'dr10', 'scr10')]
        print('| ' + ' | '.join(row) + ' |')

def t_checklist():
    R = rd('b_checklist.tsv'); u = {r['group']: r for r in R if r['run'] == 'uniform'}
    o = {(r['group'], r['pop']): r for r in R if r['run'] == 'real' and r['classes'] == 'own'}
    print('| subset | after 1 / 2 / 3, +1 after 3: uniform | real, each DR once (dr11) | real, each scramble once (scr11) | same 3 classes in order (dr11 / scr11) |')
    print('|---|---|---|---|---|')
    for c in CORN:
        f = lambda r: ' / '.join(pse(r[a], r[s]) for a, s in (('after1', 'se1'), ('after2', 'se2'), ('after3', 'se3'), ('p1_after3', 'se_p1')))
        same = lambda r: 'yes' if [r['class1'], r['class2'], r['class3']] == [u[c]['class1'], u[c]['class2'], u[c]['class3']] else \
            ('1st same' if r['class1'] == u[c]['class1'] else 'NO')
        print(f'| {c} | {f(u[c])} | {f(o[(c, "dr11")])} | {f(o[(c, "scr11")])} | {same(o[(c, "dr11")])} / {same(o[(c, "scr11")])} |')

def t_grades():
    R = rd('b_grades.tsv')
    by = collections.defaultdict(dict)
    for r in R:
        if r['target'] == 'opt' and r['budget'] == '2' and 'Daichi' not in r['checklist'] and 'class alone' not in r['checklist']:
            by[(r['checklist'], r['step'], r['description'])][r['pop']] = (r['cumulative'], r['se'])
    print('| checklist | step | uniform | dr11 | scr11 | dr10 | scr10 |')
    print('|---|---|---|---|---|---|---|')
    for (cl, st, desc), v in by.items():
        print(f'| {cl} | {st}. {desc} | ' + ' | '.join(pse(*v[p]) if p in v else '-' for p in ('uniform', 'dr11', 'scr11', 'dr10', 'scr10')) + ' |')

def t_daichi():
    R = rd('b_grades.tsv'); v = collections.defaultdict(dict)
    for r in R:
        if 'Daichi' in r['checklist'] and r['target'] == 'opt' and r['budget'] == '2':
            v[r['checklist'].split(': ')[1]][r['pop']] = (r['cumulative'], r['se'])
    print('| subset | uniform | dr11 | scr11 |')
    print('|---|---|---|---|')
    for s, x in v.items():
        print(f'| {s} | ' + ' | '.join(pse(*x[p]) for p in ('uniform', 'dr11', 'scr11')) + ' |')

def t_bounding():
    R = rd('b_bounding.tsv'); v = {(r['group'], r['pop'], r['q'], r['R']): (r['found_opt'], r['se_opt']) for r in R}
    print('| subset | q | R <= 3: uniform / dr11 / scr11 | R <= 4 | R <= 5 |')
    print('|---|---|---|---|---|')
    for c in CORN + ['all']:
        for q in '12':
            print(f'| {c} | {q}q | ' + ' | '.join(' / '.join(pse(*v[(c, p, q, R_)]) for p in ('uniform', 'dr11', 'scr11')) for R_ in '345') + ' |')

def t_q3():
    R = rd('b_q3.tsv'); v = {(r['group'], r['pop'], r['metric']): (r['value'], r['se']) for r in R}
    ms = ['mean_htr_niss', 'mean_htr_linear_best_side', 'mean_htr_normal', 'niss_eq_linear', 'niss_shorter_by_1', 'niss_shorter_by_2plus',
          'opt_uses_shortest_niss', 'no_opt_through_shortest_niss', 'every_opt_htr_ge9', 'mean_opt_minus_leave_slice', 'xr2_one_shorter']
    print('| all DRs | uniform | dr11 | scr11 | dr10 | scr10 |')
    print('|---|---|---|---|---|---|')
    for m in ms:
        f = (lambda a, s: f'{float(a):.3f} ± {float(s):.3f}') if m.startswith('mean') else pse
        print(f'| {m} | ' + ' | '.join(f(*v[('all', p, m)]) for p in ('uniform', 'dr11', 'scr11', 'dr10', 'scr10')) + ' |')
    for g in ('0c3', '0c4'):
        print(f'| {g}: niss_shorter_by_2plus | ' + ' | '.join(pse(*v[(g, p, 'niss_shorter_by_2plus')]) for p in ('uniform', 'dr11', 'scr11', 'dr10', 'scr10')) + ' |')

def t_g2(pops=('uniform', 'dr11', 'scr11')):
    R = rd('g2.tsv'); v = {(r['group'], r['pop']): r for r in R}
    print('| subset | pop | n | true optimum < DR optimum | by 1 / by 2+ | mean gain (moves) | mean DR opt / true opt / leave-slice | true < leave slice |')
    print('|---|---|---|---|---|---|---|---|')
    for c in CORN + ['all']:
        for p in pops:
            r = v.get((c, p))
            if not r: continue
            print(f'| {c} | {p} | {r["n"]} | {pse(r["shorter"], r["se"])}% | {pc(r["by1"])} / {pc(r["by2plus"])} | {float(r["mean_gain"]):.3f} ± {float(r["se_gain"]):.3f} | '
                  f'{r["mean_dr_opt"]} / {r["mean_true_opt"]} / {r["mean_ls"]} | {pc(r["true_lt_ls"])}% |')

def t_g2_cells():
    R = rd('g2.tsv')
    print('| subset x edges | uniform: shorter, by 2+, mean gain |')
    print('|---|---|')
    for r in R:
        if r['pop'] == 'uniform' and ' ' in r['group']:
            print(f'| {r["group"]} | {pse(r["shorter"], r["se"])}%, {pc(r["by2plus"])}%, {float(r["mean_gain"]):.3f} |')

if __name__ == '__main__':
    import sys
    for name in sys.argv[1:]:
        print(f'<!-- {name} -->'); globals()['t_' + name](); print()
