#!/usr/bin/env python3
"""Side-by-side uniform vs real tables with flags, from out/b_*.tsv and out/a_subsets.tsv.
A cell is flagged when |real - uniform| > 2 points ("pts") or > 2 combined standard errors ("se").
Outputs: out/cmp_checklist.tsv, cmp_grades.tsv, cmp_bounding.tsv, cmp_q3.tsv, cmp_subsets.tsv"""
import csv, collections, math
G = '/data/fmc/gaps/research/out'
POPS = ['dr11', 'scr11', 'dr10', 'scr10']

def flag(u, su, r, sr, pct=True):
    d = r - u; se = math.hypot(su, sr)
    f = []
    if pct and abs(d) > 0.02: f.append('pts')
    if not pct and abs(d) > 0.2: f.append('0.2mv')
    if se > 0 and abs(d) > 2 * se: f.append('se')
    return d, ','.join(f)

def rd(p): return list(csv.DictReader(open(p), delimiter='\t'))

def checklist():
    R = rd(f'{G}/b_checklist.tsv')
    uni = {r['group']: r for r in R if r['run'] == 'uniform'}
    with open(f'{G}/cmp_checklist.tsv', 'w') as f:
        f.write('group\tpop\tcolumn\tuniform\tse_u\treal_own_order\tse_r\tdiff\tflag\treal_with_uniform_classes\tse\tdiff\tflag\tsame_first_class\tsame_three_classes_in_order\treal_classes\n')
        for g, u in uni.items():
            for pop in POPS:
                own = [r for r in R if r['group'] == g and r['pop'] == pop and r['classes'] == 'own']
                uc = [r for r in R if r['group'] == g and r['pop'] == pop and r['classes'] == 'uniform classes']
                if not own: continue
                o = own[0]; c = uc[0] if uc else None
                same1 = o['class1'] == u['class1']; same3 = [o['class1'], o['class2'], o['class3']] == [u['class1'], u['class2'], u['class3']]
                for col, se in (('after1', 'se1'), ('after2', 'se2'), ('after3', 'se3'), ('p1_after3', 'se_p1')):
                    a, b = float(u[col]), float(o[col]); d, fl = flag(a, float(u[se]), b, float(o[se]))
                    line = f'{g}\t{pop}\t{col}\t{a:.4f}\t{float(u[se]):.4f}\t{b:.4f}\t{float(o[se]):.4f}\t{d:+.4f}\t{fl}'
                    if c:
                        b2 = float(c[col]); d2, fl2 = flag(a, float(u[se]), b2, float(c[se]))
                        line += f'\t{b2:.4f}\t{float(c[se]):.4f}\t{d2:+.4f}\t{fl2}'
                    else: line += '\t\t\t\t'
                    f.write(line + f'\t{same1}\t{same3}\t{o["class1"]} ; {o["class2"]} ; {o["class3"]}\n')

def generic(name, keyf, valcol, secol, pct=True, extra=None):
    R = rd(f'{G}/b_{name}.tsv')
    uni = {keyf(r): r for r in R if r['run'] == 'uniform'}
    with open(f'{G}/cmp_{name}.tsv', 'w') as f:
        f.write('key\tpop\tuniform\tse_u\treal\tse_r\tdiff\tflag\n')
        for r in R:
            if r['run'] != 'real': continue
            k = keyf(r); u = uni.get(k)
            if not u: continue
            a, b = float(u[valcol]), float(r[valcol])
            if math.isnan(a) or math.isnan(b): continue
            p = pct if not callable(pct) else pct(r)
            d, fl = flag(a, float(u[secol]), b, float(r[secol]), p)
            f.write(f'{" | ".join(k)}\t{r["pop"]}\t{a:.4f}\t{float(u[secol]):.4f}\t{b:.4f}\t{float(r[secol]):.4f}\t{d:+.4f}\t{fl}\n')

def subsets():
    R = rd(f'{G}/a_subsets.tsv')
    with open(f'{G}/cmp_subsets.tsv', 'w') as f:
        f.write('group\tpop\tshare\tuniform_share\tshare_ratio\tz_share\tmean_opt\tuniform_mean\tdiff_mean\tz_mean\tle11\tuniform_le11\tz_le11\tflag\n')
        for r in R:
            if r['n_drs'] == '0': continue
            sh, us, se = float(r['share']), float(r['uniform_share']), float(r['se'])
            m, um, mse = float(r['mean_opt']), float(r['uniform_mean']), float(r['se_mean'])
            l, ul, lse = float(r['le11']), float(r['uniform_le11']), float(r['se_le11'])
            z1 = (sh - us) / se if se else 0; z2 = (m - um) / mse if mse else 0; z3 = (l - ul) / lse if lse else 0
            fl = []
            if abs(z1) > 2: fl.append('share_se')
            if abs(sh / us - 1) > 0.2: fl.append('share_20pct')
            if abs(z2) > 2: fl.append('mean_se')
            if abs(m - um) > 0.1: fl.append('mean_0.1mv')
            if abs(z3) > 2: fl.append('le11_se')
            if abs(l - ul) > 0.02: fl.append('le11_pts')
            f.write(f'{r["group"]}\t{r["pop"]}\t{sh:.5f}\t{us:.5f}\t{sh / us:.3f}\t{z1:+.1f}\t{m:.3f}\t{um:.3f}\t{m - um:+.3f}\t{z2:+.1f}\t{l:.4f}\t{ul:.4f}\t{z3:+.1f}\t{",".join(fl)}\n')

if __name__ == '__main__':
    import os
    subsets()
    if os.path.exists(f'{G}/b_checklist.tsv'): checklist()
    if os.path.exists(f'{G}/b_grades.tsv'):
        generic('grades', lambda r: (r['checklist'], r['target'], r['budget'], r['step']), 'cumulative', 'se')
    if os.path.exists(f'{G}/b_bounding.tsv'):
        R = rd(f'{G}/b_bounding.tsv')
        # two value columns: write opt; p1 in a second file
        generic('bounding', lambda r: (r['group'], 'q' + r['q'], 'R' + r['R']), 'found_opt', 'se_opt')
    if os.path.exists(f'{G}/b_q3.tsv'):
        generic('q3', lambda r: (r['group'], r['metric']), 'value', 'se', pct=lambda r: not r['metric'].startswith('mean'))
    print('ok')
