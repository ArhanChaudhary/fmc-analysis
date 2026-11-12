#!/usr/bin/env python3
"""Small exact facts about the 3-cycle algs that the write-up states, each computed on the sticker model from the
lists of all sequences (py3.table): out/facts.json.  Also checks, on the sticker model, what each alg quoted from the
server or the docs really does."""
import json, collections
import cube, cubie, py3, exlib, replay
O = py3.OUT
T8 = py3.table('c', 8); T10 = py3.table('c', 10)
F = {}
by = collections.Counter(len(T8.get(s, [])) for s in T10)
F['eight_movers_per_3c'] = {str(k): v for k, v in sorted(by.items())}          # how many 3-cycles have 0, 1, 2 eight-movers
# 3-cycles whose three corners keep their U/D sticker on U/D ("oriented")
ori = [cubie.make(*e) for e in py3.elements('c') if not any(e[1])]
F['oriented_3c'] = len(ori); F['oriented_3c_with_8'] = sum(1 for s in ori if T8.get(s))
# three corners no two of which share an edge
def adjacent(a, b): return sum(x != y for x, y in zip(cubie.CORNERS[a], cubie.CORNERS[b])) == 1
tri = []
for e in py3.elements('c'):
    pcs = [i for i in range(8) if e[0][i] != i]
    if not any(adjacent(a, b) for a in pcs for b in pcs if a < b): tri.append(cubie.make(*e))
F['triangle_3c'] = len(tri); F['triangle_with_8'] = sum(1 for s in tri if T8.get(s))
opt = collections.Counter()
T12 = None
F['triangle_opt_le10'] = dict(collections.Counter(str(min(len(a) for a in T10[s])) if T10.get(s) else '>10' for s in tri))
# from such a case, one move further: how often is there an 8-mover
pairs = hit = 0; per_state = collections.Counter()
for s in tri:
    k = 0
    for m in range(18):
        g = cube.compose(cube.compose(py3.MS[m], s), py3.MI[m]); pairs += 1
        if T8.get(g): hit += 1; k += 1
    per_state[k] += 1
none_next = [s for s in tri if not any(T8.get(cube.compose(cube.compose(py3.MS[m], s), py3.MI[m])) for m in range(18))]
F['no8_after_any_move'] = len(none_next); F['no8_after_any_move_all_3c'] = sum(1 for s in T10 if not T8.get(s) and not any(T8.get(cube.compose(cube.compose(py3.MS[m], s), py3.MI[m])) for m in range(18)))
F['no8_after_any_move_optimal'] = sorted({min(len(a) for a in T10[s]) if T10.get(s) else 99 for s in none_next})
F['triangle_next'] = {'pairs': pairs, 'with_8': hit, 'moves_with_8_per_state': {str(k): v for k, v in sorted(per_state.items())}}
# after any 8-mover case: nothing to add
# the algs quoted in the write-up, on the sticker model
ALGS = {'tronto_3tc': "U' B U' F U2 B2 D' R2 U D F' U' B", 'doug_3tc': "R L U2 R' F2 L2 B L' F L' F L' B'", 'dipietro_2c2c': "R2 U' L2 D B2 R2 D' L2 U F2",
        'triple_sexy': "R U R' U' R U R' U' R U R' U'", 'triple_sledge': "R' F R F' R' F R F' R' F R F'", 'rogo': "[U2, R' D R]", 'jay': "R' F' R B2 R' F R B2",
        'tronto_2tc': "[F L' D2 L F', U2]", 'torchlight_2tc': "[F' R D2 R' F, U2]", 'ben_9': "R2 D R' U2 R D' R' U2 R'", 'ben_10': "[D R': [F2, R D' R' D]]", 'sledge_comm': "[R' F R F', D2]",
        'niklas': "R U' L' U R' U' L U", 'if_2c2c_10': "L2 F2 B2 R2 U R2 F2 B2 L2 D", 'if_triple': "B' U' B U B' U' B U B' U' B U", 'six_3e': "R L' U2 R' L F2", 'eight_3e': "R2 B2 L2 D L2 B2 R2 U",
        'parity_10': "R' U F2 D' L D F2 U2 R U", 'doug_2tc_13': "L B2 R' B L B2 R B2 L' B D2 L' D2"}
F['algs'] = {}
for k, a in ALGS.items():
    mv = cube.cancel(replay.moves(a)); s = cube.do(cube.SOLVED, mv); cp, ct, ep, ef = cubie.cubie(s)
    nc = sum(1 for i in range(8) if cp[i] != i or ct[i]); ne = sum(1 for i in range(12) if ep[i] != i or ef[i])
    F['algs'][k] = {'alg': a, 'moves': len(mv), 'type': exlib.type_of(s) if not (nc and ne) else f'{nc} corners and {ne} edges', 'left': exlib.left_text(s),
                    'eight_movers': len(T8.get(s, [])) if nc == 3 and ne == 0 else None}
# 10-movers that are a setup move, an 8-mover and the setup undone: X A X' for a single move X and an 8-mover A, compared
# as reduced sequences (so `R L U R' D R U' R' D' L'` = L [R U R' D R U' R' D'] L' counts, although it is not written
# with the setup first).  And whether such a one is ever the only 10-mover that beats every 8- and 9-mover (20-move 3c
# skeletons of the sample; needs out/onepos_3c_n20.tsv from xone.py)
import xtables
eight = {a for v in T8.values() for a in v}
inv_move = lambda m: 3 * (m // 3) + 2 - m % 3
CONJ = {}
for a in eight:
    for x in range(18):
        q = py3.cancel([x] + list(a) + [inv_move(x)])
        if len(q) == 10: CONJ.setdefault(tuple(q), []).append((x, a))
assert all(py3.state(q) in T10 and q in T10[py3.state(q)] for q in list(CONJ)[:2000])
def inside_a_turn(sk, i, a):
    """Is the 10-mover a at spot i the same solution as one of its 8-movers put inside a turn of the skeleton (the
    turn done in two parts, one before the 8-mover and one after)?"""
    fin = py3.cancel(sk[:i] + list(a) + sk[i:]); n = len(sk); par = lambda p, q: sk[p] // 6 == sk[q] // 6
    for x, A in CONJ[tuple(a)]:
        for k in range(n):
            M = sk[k]
            for M1 in range(3 * (M // 3), 3 * (M // 3) + 3):
                M2 = py3.cancel([inv_move(M1), M])
                if M1 == M or len(M2) != 1: continue
                mid = [M1] + list(A) + M2
                forms = [sk[:k] + mid + sk[k + 1:]]                                  # the turn where it stands
                if k + 1 < n and par(k, k + 1): forms.append(sk[:k] + [sk[k + 1]] + mid + sk[k + 2:])     # after the parallel move that follows it
                if k > 0 and par(k, k - 1): forms.append(sk[:k - 1] + mid + [sk[k - 1]] + sk[k + 1:])     # before the parallel move in front of it
                if any(py3.cancel(f) == fin for f in forms): return True
    return False
def conj(a): return tuple(a) in CONJ
F['ten_movers_conjugates_written_setup_first'] = sum(1 for v in T10.values() for a in v if len(a) == 10 and a[0] // 3 == a[9] // 3 and (a[0] % 3 + a[9] % 3) == 2 and tuple(a[1:9]) in eight)
F['ten_movers'] = sum(1 for v in T10.values() for a in v if len(a) == 10); F['ten_movers_conjugates'] = sum(1 for v in T10.values() for a in v if conj(a))
P = xtables.onepos(20); R = xtables.sample_cols('3c', 20, ['skeleton', 'leftover(cp;ct;ep;ef)']); wins = some = only = 0; inside = inside_any = 0; gain = collections.Counter()
for idx, p in enumerate(P):
    m9, m10 = xtables.mn(p[1]), xtables.mn(p[2])
    if not (m9 is not None and m10 < m9): continue
    sk = py3.nums(R[idx][0]); c = cubie.make(*[[int(x) for x in part.split(',')] for part in R[idx][1].split(';')]); n = len(sk); g = cube.inverse(c); best = []
    for i in range(n, -1, -1):
        if i < n: g = cube.compose(cube.compose(py3.MS[sk[i]], g), py3.MI[sk[i]])
        best += [(i, a) for a in T10.get(g, ()) if len(a) == 10 and py3.clen(sk[:i] + list(a) + sk[i:]) - n == m10]
    wins += 1; some += any(conj(a) for i, a in best)
    if all(conj(a) for i, a in best):
        only += 1; inside += all(inside_a_turn(sk, i, a) for i, a in best); inside_any += any(inside_a_turn(sk, i, a) for i, a in best); gain[m9 - m10] += 1
F['ten_wins'] = wins; F['ten_wins_some_conjugate'] = some; F['ten_wins_only_conjugates'] = only
F['ten_wins_only_conjugates_all_inside_a_turn'] = inside; F['ten_wins_only_conjugates_some_inside_a_turn'] = inside_any; F['ten_wins_only_conjugates_gain'] = {str(k): v for k, v in sorted(gain.items())}; F['ten_sample'] = len(P)
# paulduc03's question, exactly: the 3-cycles whose shortest alg is 10 moves, and whether the case one or two moves
# further along a skeleton can have an 8-mover
T10opt = {s_: min(len(a) for a in v) for s_, v in T10.items() if v}
ten = [s_ for s_, k in T10opt.items() if k == 10]; cj = lambda s_, m: cube.compose(cube.compose(py3.MS[m], s_), py3.MI[m])
one = [sum(1 for m in range(18) if T8.get(cj(s_, m))) for s_ in ten]
two = [sum(1 for m in range(18) for m2 in range(18) if m2 // 3 != m // 3 and T8.get(cj(cj(s_, m), m2))) for s_ in ten]
F['ten_cases'] = len(ten); F['ten_cases_no8_after_one_move'] = sum(1 for k in one if k == 0); F['ten_cases_8_after_some_move'] = sum(1 for k in one if k)
F['ten_cases_moves_with_8'] = sorted(set(k for k in one if k)); F['ten_cases_8_after_some_two_moves'] = sum(1 for k in two if k)
F['ten_cases_two_moves_pairs'] = [sum(two), len(ten) * 18 * 15]
json.dump(F, open(O + 'facts.json', 'w'), indent=1)
for k, v in F.items(): print(k, v if k != 'algs' else '')
for k, v in F['algs'].items(): print('  ', k, v['moves'], v['type'], '|', v['left'], v['eight_movers'])
