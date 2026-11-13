#!/usr/bin/env python3
"""One example scramble, with its solution written out, for every striking finding; each replayed on the sticker
model (sticker.py), and counts confirmed by nissy where a count is the finding.  Writes out/witness.json.

Sources: out/big/scr50k.tsv (per-scramble results), out/superflip_scr.tsv, and `eodrtools eolist` (every EO of at
most 4 turns on the first scrambles, with each EO -> DR option written out)."""
import csv, json, os, re, subprocess, sys
import sticker

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out')
BIN = os.path.join(HERE, '..', 'eodrtools', 'target', 'release', 'eodrtools')
AX = {'RL': 0, 'UD': 1, 'FB': 2}
AXN = ['RL', 'UD', 'FB']
csv.field_size_limit(10**7)
rows = list(csv.DictReader(open(os.path.join(OUT, 'big', 'scr50k.tsv')), delimiter='\t'))
scr = [l.strip() for l in open(os.path.join(OUT, 'scrambles.txt')) if l.strip()]
I = lambda r, k: int(r[k])
W = []

def quarter_of(m, y):
    return sticker.FACE_AXIS[m[0]] == y and not m.endswith('2')

def verify_dr(s, normal, inverse, x, length):
    st = sticker.replay(s, normal, inverse)
    assert sticker.is_dr(st, x), ('not a DR', s, normal, inverse)
    assert len(normal.split()) + len(inverse.split()) == length, (normal, inverse, length)

def verify_route(s, eo, dr, y, x, total, dr_side='normal'):
    assert sticker.is_eo(sticker.replay(s, eo), y), ('not an EO', s, eo)
    assert not any(quarter_of(m, y) for m in dr.split()), ('DR part breaks the EO', dr)
    if dr_side == 'normal':
        assert sticker.is_dr(sticker.replay(s, eo + ' ' + dr), x)
    else:
        assert sticker.is_dr(sticker.replay(s, eo, dr), x)
    assert len(eo.split()) + len(dr.split()) == total

def add(fid, question, finding, s, solution, check, **extra):
    W.append({'id': f'W{len(W) + 1}', 'question': question, 'finding': finding, 'scramble': s, 'solution': solution,
              'replayed_on_sticker_model': check, **extra})

def nissy(cmds):
    res = subprocess.run(['nissy', '-b'], input=''.join(c + '\n' for c in cmds), capture_output=True, text=True, check=True).stdout
    blocks, cur = [], None
    for l in res.splitlines():
        if l.startswith('>>> Executing command'):
            cur = []
            blocks.append(cur)
        elif not l.startswith('>>>') and cur is not None:
            cur.append(l)
    return blocks

d6 = lambda r: min(I(r, f'd_{s}_{a}') for s in 'ni' for a in AXN)
dlin = lambda r: min(I(r, f'd_n_{a}') for a in AXN)

# ---- A1: the longest DR in the sample, linear and NISS; scrambles with no sub-10 DR
r = max(rows, key=lambda r: (I(r, 'dniss'), d6(r)))
s = scr[I(r, 'i') - 1]
verify_dr(s, r['niss_normal'].replace('-', ''), r['niss_inverse'].replace('-', ''), AX[r['niss_axis']], I(r, 'dniss'))
add(0, 'A1', f"worst scramble of the sample: no DR shorter than {r['dniss']} turns even with NISS (best of 6 linear: {d6(r)})", s,
    {'normal': r['niss_normal'], 'inverse': r['niss_inverse'], 'dr_axis': r['niss_axis'], 'length': I(r, 'dniss')}, True,
    sample_index=I(r, 'i'), scrambles_with_this_niss_length=sum(I(x, 'dniss') == I(r, 'dniss') for x in rows))
no10 = [x for x in rows if d6(x) >= 10]
if no10:
    r = no10[0]
    s = scr[I(r, 'i') - 1]
    verify_dr(s, r['niss_normal'].replace('-', ''), r['niss_inverse'].replace('-', ''), AX[r['niss_axis']], I(r, 'dniss'))
    add(0, 'A1', f'no sub-10 DR on any axis, normal or inverse (best of 6 = {d6(r)}); NISS gives {r["dniss"]}', s,
        {'normal': r['niss_normal'], 'inverse': r['niss_inverse'], 'dr_axis': r['niss_axis'], 'length': I(r, 'dniss')}, True,
        sample_index=I(r, 'i'), share_of_sample=round(len(no10) / len(rows), 5))
# superflip
sf = list(csv.DictReader(open(os.path.join(OUT, 'superflip_scr.tsv')), delimiter='\t'))[0]
s = open(os.path.join(OUT, 'superflip.txt')).read().strip()
st = sticker.replay(s)
assert all(sticker.bad_edges(st, y) == 12 for y in range(3))
verify_dr(s, sf['niss_normal'].replace('-', ''), sf['niss_inverse'].replace('-', ''), AX[sf['niss_axis']], I(sf, 'dniss'))
opt = sf['opt_solution']
verify_dr(s, opt, '', AX[sf['opt_axis']], dlin(sf))
add(0, 'A1', f"superflip: DR in {dlin(sf)} on each axis (normal), {d6(sf)} best of 6, {sf['dniss']} with NISS; optimal EO {sf['eoopt_n_FB']} linear, {sf['eoopt_x_FB']} with NISS",
    s, {'optimal_dr': opt, 'dr_axis': sf['opt_axis'], 'niss_dr': {'normal': sf['niss_normal'], 'inverse': sf['niss_inverse']}}, True,
    d_each_axis_normal=[sf[f'd_n_{a}'] for a in AXN], d_each_axis_inverse=[sf[f'd_i_{a}'] for a in AXN],
    dr_solutions_normal_by_length={L: sum(I(sf, f'ndr_{a}_{L}') for a in AXN) for L in range(8, 12)})

# ---- A2: the longest EO inside every optimal DR; the biggest loss of the 5-turn-EO route
r = max(rows, key=lambda r: I(r, 'estar'))
s = scr[I(r, 'i') - 1]
y, e = r['estar_eo_axis'].split(':')
opt = r['opt_solution'].split()
e = int(e)
if e > 0 and not quarter_of(opt[e - 1], AX[y]):
    opt = opt[:e - 1] + [opt[e], opt[e - 1]] + opt[e + 1:]
verify_dr(s, ' '.join(opt), '', AX[r['opt_axis']], dlin(r))
assert sticker.is_eo(sticker.replay(s, ' '.join(opt[:e])), AX[y])
add(0, 'A2', f"every optimal DR ({dlin(r)} turns, {r['nopt']} of them) starts with an EO of at least {e} turns", s,
    {'optimal_dr': ' '.join(opt), 'dr_axis': r['opt_axis'], 'eo_part': ' '.join(opt[:e]), 'eo_axis': y, 'rest': ' '.join(opt[e:])}, True,
    sample_index=I(r, 'i'), scrambles_with_this_estar=sum(I(x, 'estar') == e for x in rows))
def best5(r):
    return min(I(r, f'best_n_{a}_5') for a in AXN)
r = max((x for x in rows if best5(x) < 99), key=lambda r: (best5(r) - dlin(r), -I(r, 'i')))
s = scr[I(r, 'i') - 1]
head, rest = r['route5'].split(':', 1)
axes, moves = rest.split(':', 1)
ya, xa = axes.split('>')
eo, dr = [t.strip() for t in moves.split('|')]
verify_route(s, eo, dr, AX[ya], AX[xa], int(head))
verify_dr(s, r['opt_solution'], '', AX[r['opt_axis']], dlin(r))
add(0, 'A2', f"the best DR through any normal EO of at most 5 turns is {head}, the optimal DR {dlin(r)}", s,
    {'best_route_eo_le5': {'eo': eo, 'eo_axis': ya, 'dr': dr, 'dr_axis': xa, 'total': int(head)},
     'optimal_dr': {'moves': r['opt_solution'], 'dr_axis': r['opt_axis'], 'eo_inside': r['estar_eo_axis']}}, True,
    sample_index=I(r, 'i'), scrambles_with_this_loss=sum(best5(x) - dlin(x) == best5(r) - dlin(r) for x in rows), scrambles_without_any_normal_eo_le5=sum(best5(x) >= 99 for x in rows))
# a typical case: the optimal DR, 9 turns, needs a 7-turn EO; best through a 5-move EO is 2 worse
cands = [x for x in rows if dlin(x) <= 9 and I(x, 'estar') >= 7 and best5(x) >= dlin(x) + 2]
if cands:
    r = cands[0]
    s = scr[I(r, 'i') - 1]
    head, rest = r['route5'].split(':', 1)
    axes, moves = rest.split(':', 1)
    ya, xa = axes.split('>')
    eo, dr = [t.strip() for t in moves.split('|')]
    verify_route(s, eo, dr, AX[ya], AX[xa], int(head))
    verify_dr(s, r['opt_solution'], '', AX[r['opt_axis']], dlin(r))
    add(0, 'A2', f"a {dlin(r)}-turn DR whose shortest EO inside is {r['estar']} turns; through EOs of at most 5 the best is {head}", s,
        {'optimal_dr': r['opt_solution'], 'dr_axis': r['opt_axis'], 'eo_inside': r['estar_eo_axis'],
         'best_route_eo_le5': {'eo': eo, 'eo_axis': ya, 'dr': dr, 'dr_axis': xa, 'total': int(head)}}, True, sample_index=I(r, 'i'))

# ---- A3 / B4: fewest EOs; no route at all; more 3- than 4-move EOs (counted again by nissy)
def neo(r, kinds, L):
    return sum(I(r, f'neo_{k}_{a}_{l}') for k in kinds for a in AXN for l in range(L + 1))
r = min(rows, key=lambda r: (neo(r, 'nix', 5), I(r, 'i')))
s = scr[I(r, 'i') - 1]
b = nissy([f'solve eo -N -a -M 5 {s}', f'solve eo -a -M 5 {s}', f'solve eo -N -a -c -M 5 {s}'])
eos = [l for l in b[0] if l.strip()]
# nissy writes NISS moves in parentheses; replay each
ok = 0
for l in eos:
    mv = re.sub(r'\(\d+\)\s*$', '', l).strip()
    normal = ' '.join(t for t in re.sub(r'\([^)]*\)', ' ', mv).split())
    inverse = ' '.join(' '.join(re.findall(r'\(([^)]*)\)', mv)).split())
    stt = sticker.replay(s, normal, inverse)
    assert any(sticker.is_eo(stt, y) for y in range(3)), l
    ok += 1
bo = nissy([f'solve eo -N {s}'])[0]
best_eo = re.sub(r'\(\d+\)\s*$', '', [l for l in bo if l.strip()][0]).strip()
bnorm = ' '.join(re.sub(r'\([^)]*\)', ' ', best_eo).split()); binv = ' '.join(' '.join(re.findall(r'\(([^)]*)\)', best_eo)).split())
assert any(sticker.is_eo(sticker.replay(s, bnorm, binv), y) for y in range(3))
add(0, 'B4', f"fewest EOs of at most 5 turns in the sample: {neo(r, 'nix', 5)} with NISS on all three axes ({neo(r, 'n', 5)} linear normal); {sum(neo(x, 'nix', 5) == neo(r, 'nix', 5) for x in rows)} such scrambles", s,
    {'all_eos_le5_niss (nissy eo -N -a -M 5)': [l.strip() for l in eos], 'an optimal NISS EO (nissy eo -N)': best_eo, 'its length': len(bnorm.split()) + len(binv.split())}, True,
    nissy_count=len(eos), ours=neo(r, 'nix', 5), sample_index=I(r, 'i'))
assert len(eos) == neo(r, 'nix', 5), (len(eos), neo(r, 'nix', 5))
def niss_line(l):
    mv = re.sub(r'\(\d+\)\s*$', '', l).strip()
    normal = ' '.join(re.sub(r'\([^)]*\)', ' ', mv).split())
    inverse = ' '.join(' '.join(re.findall(r'\(([^)]*)\)', mv)).split())
    return mv, normal, inverse
lin3 = sum(1 for x in rows if neo(x, 'n', 3) - neo(x, 'n', 2) > neo(x, 'n', 4) - neo(x, 'n', 3))
cand = [x for x in rows if neo(x, 'nix', 3) - neo(x, 'nix', 2) > (neo(x, 'nix', 4) - neo(x, 'nix', 3))]
if cand:
    r = cand[0]
    s = scr[I(r, 'i') - 1]
    b = nissy([f'solve eo -N -a -m 3 -M 3 {s}', f'solve eo -N -a -m 4 -M 4 {s}'])
    e3 = [niss_line(l) for l in b[0] if l.strip()]
    e4 = [niss_line(l) for l in b[1] if l.strip()]
    for mv, nm, im in e3 + e4:
        assert any(sticker.is_eo(sticker.replay(s, nm, im), y) for y in range(3)), mv
    assert len(e3) > len(e4)
    add(0, 'B4', f'more 3-move EOs ({len(e3)}) than 4-move EOs ({len(e4)}) with NISS, all axes ({len(cand)} of {len(rows)} scrambles; linear: {lin3})', s,
        {'three_move_eos (nissy eo -N -a)': [m for m, _, _ in e3], 'four_move_eos': [m for m, _, _ in e4]}, True, sample_index=I(r, 'i'))

# ---- C: options after an EO, from eolist on the first scrambles
first = scr[:150]
res = subprocess.run([BIN, 'eolist', '4'] + first, capture_output=True, text=True, check=True).stdout
el = list(csv.DictReader(res.splitlines(), delimiter='\t'))
def vplain(x):
    verify_route(x['scramble'], x['eo'], x['plain_dr'], AX[x['eo_axis']], AX[x['dr_axis']], len(x['eo'].split()) + int(x['plain']))
def pick(pred):
    for x in el:
        if x['eo'] and pred(x):
            return x
    return None
x = pick(lambda x: x['case'] == '4c4e' and int(x['plain']) == 7 and int(x['switched']) <= 5)
x = x or pick(lambda x: x['case'] == '4c4e' and int(x['switched']) < int(x['plain']))
if x:
    vplain(x)
    verify_route(x['scramble'], x['switched_eo'], x['switched_dr'], AX[x['eo_axis']], AX[x['dr_axis']], len(x['switched_eo'].split()) + int(x['switched']))
    add(0, 'C6c', f"DR-4c4e after the EO: {x['plain']} to DR; with the EO's last turn inverted, {x['switched']}", x['scramble'],
        {'eo': x['eo'], 'eo_axis': x['eo_axis'], 'dr_axis': x['dr_axis'], 'dr': x['plain_dr'], 'eo_switched': x['switched_eo'], 'dr_after_switch': x['switched_dr']}, True)
x = pick(lambda x: int(x['plain']) >= 9 and int(x['inverse']) <= 5)
if x:
    vplain(x)
    verify_dr(x['scramble'], x['eo'], x['inverse_dr'], AX[x['dr_axis']], len(x['eo'].split()) + int(x['inverse']))
    assert not any(quarter_of(m, AX[x['eo_axis']]) for m in x['inverse_dr'].split())
    add(0, 'C6b', f"after the EO, {x['case']}: {x['plain']} to DR on normal, {x['inverse']} on the inverse (EO kept)", x['scramble'],
        {'eo': x['eo'], 'eo_axis': x['eo_axis'], 'dr_axis': x['dr_axis'], 'dr_normal': x['plain_dr'], 'dr_on_inverse': x['inverse_dr'],
         'written_niss': f"{x['eo']} ({x['inverse_dr']})"}, True)
by = {}
for x in el:
    by.setdefault((x['scramble'], x['eo_axis'], x['eo']), []).append(x)
for k, v in by.items():
    if len(v) == 2 and k[2] and int(v[0]['plain']) >= 9 and int(v[1]['plain']) <= 5:
        vplain(v[0]); vplain(v[1])
        add(0, 'C6a', f"one EO, two DR axes: {v[0]['case']} on {v[0]['dr_axis']} is {v[0]['plain']} to DR, {v[1]['case']} on {v[1]['dr_axis']} is {v[1]['plain']}", k[0],
            {'eo': k[2], 'eo_axis': k[1], v[0]['dr_axis']: v[0]['plain_dr'], v[1]['dr_axis']: v[1]['plain_dr']}, True)
        break
# (the first such row is a 3c0e state, which has the other EO solved as well, and its shorter DR keeps that one; the
# write-up's [f] uses xwitness.py's X6 instead, a state with one EO only)
x = pick(lambda x: int(x['any']) < int(x['plain']))
if x:
    vplain(x)
    verify_dr(x['scramble'], x['eo'] + ' ' + x['any_dr'], '', AX[x['dr_axis']], len(x['eo'].split()) + int(x['any']))
    add(0, 'C6d', f"after the EO, {x['case']}: {x['plain']} keeping EO, {x['any']} with a turn that breaks it", x['scramble'],
        {'eo': x['eo'], 'eo_axis': x['eo_axis'], 'dr_axis': x['dr_axis'], 'dr_keeping_eo': x['plain_dr'], 'dr_breaking_eo': x['any_dr']}, True,
        eolist_rows_with_any_shorter=sum(int(y['any']) < int(y['plain']) for y in el), eolist_rows=len(el))
json.dump(W, open(os.path.join(OUT, 'witness.json'), 'w'), indent=1)
print(f'{len(W)} witnesses written, every solution replayed on the sticker model')
