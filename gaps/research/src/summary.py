#!/usr/bin/env python3
"""Writes out/SUMMARY.md from the result files (tables via tables.py and edgemix.py, numbers via g2.tsv)."""
import subprocess, csv, json, collections, sys
G = '/data/fmc/gaps/research'
sys.path.insert(0, f'{G}/src')
def tab(name): return subprocess.run([sys.executable, f'{G}/src/tables.py', name], capture_output=True, text=True, check=True).stdout.split('\n', 1)[1].strip()
edgemix = subprocess.run([sys.executable, f'{G}/src/edgemix.py'], capture_output=True, text=True, check=True).stdout.strip()
g2 = {(r['group'], r['pop']): r for r in csv.DictReader(open(f'{G}/out/g2.tsv'), delimiter='\t')}
ex = json.load(open(f'{G}/out/g2_examples.json'))
from real_analysis import SIZE
rows = [l.rstrip('\n').split('\t') for l in open(f'{G}/big/g2/uni1000.out')]
n = collections.Counter(r[0] for r in rows)
W = collections.Counter(); S = collections.Counter(); C = collections.Counter(); GN = collections.Counter()
for r in rows:
    w = SIZE[r[0]] / n[r[0]]; d = int(r[5]); W[d] += w; C[d] += 1
    if int(r[9]) < d: S[d] += w
    GN[int(r[5]) - int(r[9])] += 1
tot = sum(W.values())
bylen = '| DR optimum | states solved | share of all DR states | a shorter any-move finish exists |\n|---|---|---|---|\n' + '\n'.join(
    f'| {d} | {C[d]:,} | {100 * W[d] / tot:.2f}% | {100 * S[d] / W[d]:.1f}% |' for d in sorted(W) if d >= 8)
le12 = sum(S[d] for d in W if d <= 12) / sum(W[d] for d in W if d <= 12)
A = g2[('all', 'uniform')]
R11 = g2.get(('all', 'dr11')); S11 = g2.get(('all', 'scr11'))
pc = lambda x: f'{100 * float(x):.1f}%'
B1 = collections.Counter()                                                            # weight of states shorter by g
for r in rows: B1[int(r[5]) - int(r[9])] += SIZE[r[0]] / n[r[0]]
by1w = f"{100 * B1[1] / sum(v for k, v in B1.items() if k > 0):.0f}%"                 # weighted by subset size (89.7%)
by1u = f"{100 * GN[1] / sum(v for k, v in GN.items() if k > 0):.1f}%"                 # raw sample, 0e cells oversampled (2,505 / 2,999)
ck = {(r['group'], r['run'], r['pop'], r['classes']): r for r in csv.DictReader(open(f'{G}/out/b_checklist.tsv'), delimiter='\t')}
c04 = lambda pop: f"{100 * (float(ck[('0c4', 'real', pop, 'own')]['after3']) - float(ck[('0c4', 'real', pop, 'uniform classes')]['after3'])):.2f}"
def exblock():
    out = []
    for e in ex['examples']:
        out.append(f"- **{e['subset']}**, DR optimum {e['dr_optimum']}, any-move optimum {e['true_optimum']} (leave slice {e['leave_slice_optimum']}). "
                   f"State: `{e['scramble_reaching_state']}` applied to a solved cube (DR moves only). DR-optimal finish `{e['dr_optimal_finish']}`. "
                   f"Every optimal solution nissy lists ({e['n_optimal_solutions']}): " + ', '.join(f"`{s['moves']}`" for s in e['solutions']) + '.')
    return '\n'.join(out)
real_line = ''
if R11:
    real_line = (f" On the real population the share is {pc(R11['shorter'])} ± {pc(R11['se'])} with each DR once and "
                 f"{pc(S11['shorter'])} ± {pc(S11['se'])} with each scramble once (uniform {pc(A['shorter'])}).")
md = open(f'{G}/src/summary_template.txt').read()
for k, v in {'SUBSETS': tab('subsets'), 'EDGEMIX': edgemix, 'CHECKLIST': tab('checklist'), 'GRADES': tab('grades'),
             'BOUNDING': tab('bounding'), 'Q3': tab('q3'), 'G2TABLE': tab('g2'), 'G2CELLS': tab('g2_cells'), 'G2BYLEN': bylen,
             'G2EX': exblock(), 'G2ALL': f"{pc(A['shorter'])} ± {pc(A['se'])}", 'G2GAIN': f"{float(A['mean_gain']):.3f}",
             'G2LE12': f'{100 * le12:.1f}%', 'G2REAL': real_line,
             'G2GAINS': ', '.join(f'{k}: {GN[k]:,}' for k in sorted(GN)),
             'G2BY1W': by1w, 'G2BY1U': by1u, 'C04DR': c04('dr11'), 'C04SCR': c04('scr11'),
             'EXFAIL': str(ex['failures']), 'EXN': str(sum(len(e['solutions']) for e in ex['examples']))}.items():
    md = md.replace('{{' + k + '}}', v)
open(f'{G}/out/SUMMARY.md', 'w').write(md)
print('SUMMARY.md', len(md))
