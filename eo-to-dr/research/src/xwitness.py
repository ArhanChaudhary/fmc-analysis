#!/usr/bin/env python3
"""Extra worked examples for the write-up (out/witness_extra.json), each replayed on the sticker model; the twelve of
witness.py (out/witness.json) are replayed again here too.

  X1  an EO whose DR (EO kept, one axis) takes 10 turns, the longest there is (from out/big/ex_eolist.tsv)
  X2  a position in DR on U/D whose four E-slice edges are not in their home order (why the DR-skip count divides by 4!)
  X3  the optimal full solution of witness W1 (no DR under 10 even with NISS), from out/optimal_no_sub10.tsv
usage: xwitness.py"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sticker, cube
from canon import simplify
OUT = os.path.normpath(os.path.join(HERE, '..', 'out')) + '/'
AX = {'RL': 0, 'UD': 1, 'FB': 2}
csv.field_size_limit(10**8)
n = [0]
def ok(c, what):
    n[0] += 1
    assert c, what
def toks(t): return [] if t.strip() in ('', '-') else t.split()
def q(m, y): return sticker.FACE_AXIS[m[0]] == y and not m.endswith('2')
X = {}
# X1
for r in csv.DictReader(open(OUT + 'big/ex_eolist.tsv'), delimiter='\t'):
    if r['plain'] == '10':
        s, eo, y, x = r['scramble'], r['eo'], AX[r['eo_axis']], AX[r['dr_axis']]
        ok(sticker.is_eo(sticker.replay(s, eo), y), 'X1 eo')
        ok(sticker.is_dr(sticker.replay(s, eo + ' ' + r['plain_dr']), x) and not any(q(m, y) for m in toks(r['plain_dr'])) and len(toks(r['plain_dr'])) == 10, 'X1 dr')
        ok(sticker.is_dr(sticker.replay(s, r['switched_eo'] + ' ' + r['switched_dr']), x), 'X1 sw')
        ok(sticker.is_dr(sticker.replay(s, eo, r['inverse_dr']), x), 'X1 inv')
        X['X1'] = {k: r[k] for k in ('scramble', 'eo_axis', 'eo', 'dr_axis', 'case', 'plain', 'plain_dr', 'switched', 'switched_eo', 'switched_dr', 'inverse', 'inverse_dr', 'any')}
        break
# X4: a 4c6e at its most common length
for r in csv.DictReader(open(OUT + 'big/ex_eolist.tsv'), delimiter='\t'):
    if r['case'] == '4c6e' and r['plain'] == '8':
        s, eo, y, x = r['scramble'], r['eo'], AX[r['eo_axis']], AX[r['dr_axis']]
        ok(sticker.is_eo(sticker.replay(s, eo), y), 'X4 eo')
        ok(sticker.is_dr(sticker.replay(s, eo + ' ' + r['plain_dr']), x) and not any(q(m, y) for m in toks(r['plain_dr'])) and len(toks(r['plain_dr'])) == 8, 'X4 dr')
        X['X4'] = {k: r[k] for k in ('scramble', 'eo_axis', 'eo', 'dr_axis', 'case', 'plain', 'plain_dr')}
        X['X4']['eo_axis'] = {'RL': 'R/L', 'UD': 'U/D', 'FB': 'F/B'}[r['eo_axis']]; X['X4']['dr_axis'] = {'RL': 'R/L', 'UD': 'U/D', 'FB': 'F/B'}[r['dr_axis']]
        break
# X5: alkamaass's 7-move NISS EO (D6033) on the superflip of W3
sf = json.load(open(OUT + 'witness.json'))[2]['scramble']
ok(sticker.is_eo(sticker.replay(sf, "D F U'", "L B R U'"), 1), 'X5')
X['X5'] = {'scramble': sf, 'normal': "D F U'", 'inverse': "L B R U'", 'axis': 'U/D'}
# X2
s = 'R2 L2 F2 B2'
st = sticker.replay(s)
ok(sticker.is_dr(st, 1) and st != cube.SOLVED, 'X2')
X['X2'] = {'scramble': s}
# X3
for r in csv.DictReader((l for l in open(OUT + 'optimal_no_sub10.tsv') if not l.startswith('#')), delimiter='\t'):
    ok(sticker.replay(r['scramble'], r['optimal_solution']) == cube.SOLVED, 'X3')
    X.setdefault('X3', []).append(r)
# the twelve of witness.json, once more
W = {w['id']: w for w in json.load(open(OUT + 'witness.json'))}
for w in W.values():
    s, sol = w['scramble'], w['solution']
    if 'normal' in sol and 'dr_axis' in sol:
        ok(sticker.is_dr(sticker.replay(s, sol['normal'], sol['inverse'] if sol['inverse'] != '-' else ''), AX[sol['dr_axis']]), w['id'])
    if 'optimal_dr' in sol and isinstance(sol['optimal_dr'], str):
        ok(sticker.is_dr(sticker.replay(s, sol['optimal_dr']), AX[sol['dr_axis']]), w['id'])
    if 'optimal_dr' in sol and isinstance(sol['optimal_dr'], dict):
        ok(sticker.is_dr(sticker.replay(s, sol['optimal_dr']['moves']), AX[sol['optimal_dr']['dr_axis']]), w['id'])
    if 'best_route_eo_le5' in sol:
        b = sol['best_route_eo_le5']
        ok(sticker.is_eo(sticker.replay(s, b['eo']), AX[b['eo_axis']]) and sticker.is_dr(sticker.replay(s, b['eo'] + ' ' + b['dr']), AX[b['dr_axis']])
           and not any(q(m, AX[b['eo_axis']]) for m in toks(b['dr'])), w['id'])
    if 'eo' in sol and 'eo_axis' in sol:
        ok(sticker.is_eo(sticker.replay(s, sol['eo']), AX[sol['eo_axis']]), w['id'])
        for k, v in sol.items():
            if k in ('RL', 'UD', 'FB'):
                ok(sticker.is_dr(sticker.replay(s, sol['eo'] + ' ' + v), AX[k]), w['id'])
        if 'dr' in sol:
            ok(sticker.is_dr(sticker.replay(s, sol['eo'] + ' ' + sol['dr']), AX[sol['dr_axis']]), w['id'])
        if 'eo_switched' in sol:
            ok(sticker.is_dr(sticker.replay(s, sol['eo_switched'] + ' ' + sol['dr_after_switch']), AX[sol['dr_axis']]), w['id'])
        if 'dr_on_inverse' in sol:
            ok(sticker.is_dr(sticker.replay(s, sol['eo'], sol['dr_on_inverse']), AX[sol['dr_axis']]), w['id'])
        if 'dr_breaking_eo' in sol:
            ok(sticker.is_dr(sticker.replay(s, sol['eo'] + ' ' + sol['dr_breaking_eo']), AX[sol['dr_axis']]), w['id'])
            ok(sticker.is_dr(sticker.replay(s, sol['eo'] + ' ' + sol['dr_keeping_eo']), AX[sol['dr_axis']]), w['id'])
# printed scrambles: adjacent same-face turns merged, same position
X['scr'] = {}
for k, w in list(W.items()) + [(k, X[k]) for k in ('X1', 'X4')] + [(f'X3_{i}', r) for i, r in enumerate(X['X3'])]:
    s0 = w['scramble']; s1 = simplify(s0)
    ok(sticker.replay(s1) == sticker.replay(s0), ('printed', k))
    X['scr'][k] = s1
X['checks'] = n[0]
json.dump(X, open(OUT + 'witness_extra.json', 'w'), indent=1)
print(f'witness_extra.json: {n[0]} sticker-model checks passed')
