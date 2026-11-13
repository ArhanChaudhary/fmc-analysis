"""Concrete scrambles for the report, each checked on the cube model, and the Lean claims (out/lean_claims.json).
  - the two text-DR examples of out/tnoodle_examples.txt
  - an easy and a hard official scramble (recent era), with their counts and their best DR written out
  - the server's two posted scrambles (zakimoshi's awful scramble, jtuuu's FB-heavy one)
out: out/witnesses.txt"""
import csv, json, math
import cube, textfeat as tf

O = open('../out/witnesses.txt', 'w')
def P(*a):
    s = ' '.join(map(str, a)); print(s); O.write(s + '\n')
claims = []

def split_niss(moves):
    n, i, inside = [], [], False
    for t in moves.replace('(', ' ( ').replace(')', ' ) ').split():
        if t == '(': inside = True
        elif t == ')': inside = False
        else: (i if inside else n).append(t)
    return n, i

def dr_rows(raw, lab, k):
    out = []
    fl = open(lab); next(fl)
    for line in open(raw):
        if line.startswith('#') or line.startswith('scr\t'): continue
        l = next(fl)
        r = line.rstrip('\n').split('\t')
        if r[0] == k:
            lb = l.rstrip('\n').split('\t'); out.append((int(r[3]), int(lb[1]), lb[0], r[1].replace('/', ''), r[5]))
    return out

def show_dr(name, scr, L, d, sub, ax, moves, what):
    n, i = split_niss(moves)
    pre = cube.inv_moves(i)
    st = cube.seq(pre + cube.parse(scr) + n)
    ok = cube.is_dr(st, ax)
    P(f'    DR ({ax}, {L} moves): {moves}   subset {sub}, optimal finish {d}, DR + finish {L + d}; DR state on the cube model: {ok}')
    assert ok
    claims.append({'name': name, 'premoves': ' '.join(pre), 'scramble': scr, 'normal': ' '.join(n), 'axis': ax,
                   'what': what, 'not_before': True})

# text DR examples
real = [l.rstrip('\n').split('\t') for l in open('../big/real_unique.tsv')][1:]
for nm, pick in (('text_dr_recent', max(real, key=lambda r: r[2])), ('text_dr_old', min((r for r in real if r[2] < '2020-08'), key=lambda r: r[2]))):
    s = pick[0]; m, _ = tf.strip(s); ax, x, h, y, d = tf.text_dr(m)
    X, Y = m[:x], m[x + h:]
    pre = cube.inv_moves(tf.PAD + X); nor = cube.inv_moves(Y + tf.PAD)
    assert cube.is_dr(cube.seq(pre + cube.parse(s) + nor), ax)
    claims.append({'name': nm, 'premoves': ' '.join(pre), 'scramble': s, 'normal': ' '.join(nor), 'axis': ax,
                   'what': f'{pick[1]} ({pick[2]}): the text DR, normal {" ".join(nor)}, inverse ({" ".join(cube.inv_moves(pre))})', 'not_before': True})

# easy / hard official scrambles
T = {r['id']: r for r in csv.DictReader(open('../out/tgt_real.tsv'), delimiter='\t')}
F = {r['id']: r for r in csv.DictReader(open('../out/feat_real.tsv'), delimiter='\t')}
info = {f'r{i}': r for i, r in enumerate(real)}
AX = ['UD', 'FB', 'RL']
def n_eo(k, L):
    return sum(int(F[k][f'n_eo{L}_{e}_{s}']) for e in AX for s in 'NI')
def describe(k):
    f = F[k]; t = T.get(k, {'n10': '0', 'best': 'none', 'good22': '0'})
    be = sorted(int(f[f'be_{e}']) for e in AX)
    eob = min(int(f[f'eo_opt_{e}_{s}']) for e in AX for s in 'NI')
    P(f'  {info[k][1]} ({info[k][2]}): {info[k][0]}')
    P(f'    bad edges {be[0]}/{be[1]}/{be[2]}; shortest EO {eob}; EOs of <= 4 moves: {n_eo(k, 4)}; of <= 5: {n_eo(k, 5)} (all axes, normal + inverse)')
    P(f'    DRs of <= 10 moves: {t["n10"]}; best DR + optimal finish: {t["best"]}; DRs with DR + finish <= 22: {t["good22"]}')
recent = [k for k in T if info[k][2] >= '2025-01' and k in F]
easy = [k for k in recent if int(T[k]['best']) <= 18 and min(int(F[k][f'eo_opt_{e}_{s}']) for e in AX for s in 'NI') >= 3]
easy.sort(key=lambda k: (-int(T[k]['n10']), info[k][2]))
hard = [k for k in recent if int(T[k]['n10']) <= 3 and int(T[k]['best']) >= 23]
hard.sort(key=lambda k: (int(T[k]['n10']), info[k][2]))
P('Easy official scramble (2025 or later, best DR + finish <= 18, no EO under 3 moves, most DRs of <= 10):')
ke = easy[0]; describe(ke)
rows = sorted(dr_rows('../big/real_raw_10.tsv', '../big/real_label_10.tsv', ke), key=lambda r: (r[0] + r[1], r[0]))
L, d, sub, ax, mv = rows[0]; show_dr('easy_best_dr', info[ke][0], L, d, sub, ax, mv, f'easy example {info[ke][1]}: a {L}-move DR with a {d}-move finish')
P('Hard official scramble (2025 or later, at most 3 DRs of <= 10, best DR + finish >= 23):')
kh = hard[0]; describe(kh)
rows = sorted(dr_rows('../big/real_raw_10.tsv', '../big/real_label_10.tsv', kh), key=lambda r: (r[0] + r[1], r[0]))
for j, (L, d, sub, ax, mv) in enumerate(rows):
    show_dr(f'hard_dr_{j}', info[kh][0], L, d, sub, ax, mv, f'hard example {info[kh][1]}: DR {j + 1} of {len(rows)}')

# the server's posted scrambles
P('Posted on the server:')
W = {l.split('\t')[0]: l.rstrip('\n').split('\t')[1] for l in open('../big/in_witness.tsv')}
FW = {r['id']: r for r in csv.DictReader(open('../out/feat_witness.tsv'), delimiter='\t')}
for k, s in W.items():
    f = FW[k]
    P(f'  {k}: {s}')
    for e in AX:
        P(f'    EO axis {e}: bad edges {f["be_" + e]}, shortest EO normal {f["eo_opt_" + e + "_N"]} inverse {f["eo_opt_" + e + "_I"]}, '
          f'EOs <= 5 normal {f["n_eo5_" + e + "_N"]} inverse {f["n_eo5_" + e + "_I"]}')
    drs = []
    for line in open('../big/witness_raw.tsv'):
        r = line.rstrip('\n').split('\t')
        if r[0] == k and int(r[3]) <= 10: drs.append(r)
    P(f'    DRs of <= 10 moves (EO <= 5 with NISS, then DR): {len(drs)}')
    for j, r in enumerate(drs):
        n, i = split_niss(r[5]); ax = r[1].replace('/', '')
        ok = cube.is_dr(cube.seq(cube.inv_moves(i) + cube.parse(s) + n), ax); assert ok
        P(f'      {ax} {r[3]} moves: {r[5]}  (DR on the cube model: {ok})')
        claims.append({'name': f'{k}_dr_{j}', 'premoves': ' '.join(cube.inv_moves(i)), 'scramble': s, 'normal': ' '.join(n),
                       'axis': ax, 'what': f'{k}: DR {j + 1} of {len(drs)} of at most 10 moves', 'not_before': True})

# ---- more examples for the claims section
import itertools
ID = {l.rstrip('\n').split('\t')[1]: l.split('\t')[0] for l in open('../big/in_real.tsv')}
def best_dr(k, name, what):
    rows = sorted(dr_rows('../big/real_raw_10.tsv', '../big/real_label_10.tsv', k), key=lambda r: (r[0] + r[1], r[0]))
    L, d, sub, ax, mv = rows[0]; show_dr(name, info[k][0], L, d, sub, ax, mv, what)
def short_eo(scr, maxlen=3):
    st = cube.seq(scr); out = []
    for side, s0 in (('normal', st), ('inverse', cube.inv(st))):
        for n in range(0, maxlen + 1):
            for seq in itertools.product(list(cube.MOVES), repeat=n):
                if any(seq[i][0] == seq[i + 1][0] for i in range(n - 1)): continue
                fl = cube.facelets(cube.apply(s0, list(seq)))
                for a in AX:
                    if not any(cube.eo_axis(fl, a)): out.append((n, side, a, ' '.join(seq)))
            if out: break
    return sorted(out)[:3]
P('Short text, easy scramble (official, since 2020-08, middle of at most 16 moves):')
ks = ID["R' U' F L F2 D2 R' B2 F2 R' B2 D R F2 R' D L B' R' U' F"]; describe(ks)
P(f'    middle: {len(tf.strip(info[ks][0])[0])} moves')
best_dr(ks, 'short_text_easy', f'short text, easy: {info[ks][1]}')
P('10/8/8 with a short EO (official):')
c1 = sorted([k for k in T if k in F and sorted(int(F[k][f"be_{e}"]) for e in AX) == [8, 8, 10]
             and min(int(F[k][f"eo_opt_{e}_{s}"]) for e in AX for s in "NI") <= 3], key=lambda k: (int(T[k]['best']), k))
for k in c1[:1]:
    describe(k); P('    EOs of at most 3 moves (length, side, EO axis, moves):', short_eo(info[k][0]))
    best_dr(k, 'ten_eight_eight_short_eo', f'10/8/8 with a short EO: {info[k][1]}')
P('50 or more EOs of <= 4 moves, best DR + finish 22 (official):')
c2 = sorted([k for k in T if k in F and n_eo(k, 4) >= 50 and int(T[k]['best']) >= 22], key=lambda k: (-int(T[k]['best']), k))
for k in c2[:1]:
    describe(k); best_dr(k, 'many_four_movers_22', f'many 4-move EOs, best 22: {info[k][1]}')
# Louis: the official middle is not the first solution min2phase finds
first = dict(l.rstrip('\n').split('\t') for l in open('../big/first_real.tsv'))
sx = "R' U' F L' D' U2 F2 L2 F2 U' F L2 F2 R2 B U2 L' U' F' R' D R' U' F"; kx = ID[sx]
mx = ' '.join(tf.strip(sx)[0]); fx = first[kx]
assert cube.seq(mx) == cube.seq(fx)
P(f'First solution against the official middle: {info[kx][1]} ({info[kx][2]})\n    official middle ({len(mx.split())} moves): {mx}\n    first solution found, inverted ({len(fx.split())} moves): {fx}\n    same state on the cube model: True')
claims.append({'kind': 'same', 'name': 'first_solution_same_state', 'a': mx, 'b': fx, 'what': f'{info[kx][1]}: the official middle and the first solution min2phase finds (inverted) make the same state'})

json.dump(claims, open('../out/lean_claims.json', 'w'), indent=1)
P(len(claims), 'Lean claims')
