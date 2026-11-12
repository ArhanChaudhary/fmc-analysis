#!/usr/bin/env python3
"""Example scrambles for the statements of the write-up and the errata.  Each is taken from the sample files by a
search for the first skeleton with the property, given a scramble (exlib.scramble_for), solved again by the tool on
that scramble, and replayed on the sticker model.  Writes out/witness.json and the text blocks
report_build/wit_<name>.md that the write-up and the errata include.

  witness.py            make them
  witness.py --verify   read the blocks back and replay every scramble, skeleton and solution"""
import sys, json, re, os, glob, csv
import cube, cubie, exlib, py3, iv
O = iv.O; B = '/data/fmc/insertion-cost/research/src/report_build/'
def rows(typ, n, pre='sample'):
    with open(f'{O}{pre}_{typ}_n{n}.tsv') as f:
        hd = f.readline().rstrip('\n').split('\t')
        for l in f: yield dict(zip(hd, l.rstrip('\n').split('\t')))
def state_of(r):
    cp, ct, ep, ef = [[int(x) for x in part.split(',')] for part in r['leftover(cp;ct;ep;ef)'].split(';')]
    return cubie.make(cp, ct, ep, ef)
def scramble(r, sol=None):
    """A scramble for a sample line: needs one solution; take the line's own or search one with the tool."""
    sk = r['skeleton'].split(); c = state_of(r)
    if sol is None:
        # any solution: the tool on (inverse of leftover alg + skeleton) is not available without a scramble, so use
        # an alg for the leftover from the tables: two-phase on the state directly
        sol = None
    return sk, c
def any_solution(sk, c):
    """Some sequence that solves the scramble of (skeleton, leftover): skeleton followed by an alg for the leftover
    found by the tool's lists (3-cycles) or by two-phase through nissy on leftover^-1."""
    T = py3.table('c', 10)
    inv = cube.inverse(c)
    if inv in T: return sk + [py3.NAMES[m] for m in T[inv][0]]
    return None
def block_md(scr, sk, typ, parts):
    """parts: list of (label, sol or None, note)."""
    s = cube.do(cube.SOLVED, scr + sk)
    L = [f"Scramble: `{' '.join(scr)}`", '', f"Skeleton: `{' '.join(sk)}` ({len(sk)}), leaves {iv.LONG[typ]}: {exlib.left_text(s)}", '']
    for label, sol, note in parts:
        if sol is None: L += [f'**{label}**: {note}', '']
        else: L += [f"**{label}**: {sol['length']} in all{(', ' + note) if note else ''}.", '', '```'] + exlib.block(sk, sol) + ['```', '']
    return L
def make_from(typ, r, caps, mixed=False):
    sk = r['skeleton'].split(); c = state_of(r)
    sol = next((r[k] for k in ('L10_solution', 'L8_solution', 'L12_solution') if r.get(k, '-') not in ('-', None)), None)
    if sol is None:
        # no solution printed on this sample line: ask the tool for one through a temporary scramble made from a 3-cycle alg
        raise SystemExit('no solution on the sample line; pick a line with one (every 20th)')
    scr = exlib.scramble_for(sol.split())
    assert cube.do(cube.SOLVED, scr + sk) == c
    b = exlib.best(scr, sk, caps, mixed); assert b['type'] == typ
    return scr, sk, b
W = {}
def save(name, scr, sk, typ, parts, extra=None):
    L = block_md(scr, sk, typ, parts)
    open(f'{B}wit_{name}.md', 'w').write('\n'.join(L).rstrip('\n') + '\n')
    W[name] = dict({'scramble': ' '.join(scr), 'skeleton': ' '.join(sk), 'type': typ, 'n': len(sk)}, **(extra or {}))
def solve_line(typ, n, pick, pre='sample'):
    """First sample line (among those that carry a printed solution) for which pick(row) is true."""
    for r in rows(typ, n, pre):
        if r.get('L10_solution', r.get('L8_solution', '-')) == '-' and r.get('L8_solution', '-') == '-' and r.get('L12_solution', '-') == '-': continue
        if pick(r): return r
    raise SystemExit(f'no line for {typ} {n}')
def onepos_row(n, idx):
    with open(f'{O}onepos_3c_n{n}.tsv') as f:
        f.readline()
        for l in f:
            p = l.rstrip('\n').split('\t')
            if int(p[0]) == idx: return [[None if x == 'x' else int(x) for x in part.split(',')] for part in p[1:4]]
def main():
    val = lambda r, k: None if r[k] in ('inf', 'nc', 'na', '-') else int(r[k])
    # 1. every other move misses the only 8-3 (it sits before a pair of opposite-face moves)
    for r in rows('3c', 20):
        if r['L8_solution'] == '-' or val(r, 'L8_one') != 5: continue
        pp = onepos_row(20, int(r['idx']))[0]; best = [i for i, v in enumerate(pp) if v == 5]
        if len(best) != 1: continue
        par = best[0] % 2
        other = [v for i, v in enumerate(pp) if (i % 2 != par or i in (0, 20)) and v is not None]
        if best[0] in (0, 20) or (other and min(other) == 5): continue
        scr, sk, b = make_from('3c', r, '8')
        sol = b['sols'][8]['one']; assert sol['cost'] == 5 and sol['steps'][0][0] == best[0]
        spots = 'the odd spots' if par == 0 else 'the even spots'
        found = min(other)
        save('skip', scr, sk, '3c', [('The best 8-mover insertion', sol, f'the only 8-3 in the skeleton, after move {best[0]}')],
             {'spot': best[0], 'other_best': found, 'per_spot': pp})
        open(f'{B}wit_skip.md', 'a').write(f"\nCounting spots from 0 (before the first move), the 8-3 is at spot {best[0]}. Checking the {('odd', 'even')[par]} spots ({', '.join(str(i) for i in range(1 - par, 20, 2))}) and both ends finds nothing better than an 8-{8 - found}; the {('even', 'odd')[par]} spots would find it. The spot is {'before' if True else ''} the pair `{sk[best[0]]} {sk[best[0] + 1]}`.\n" if sk[best[0]][0] + sk[best[0] + 1][0] in ('UD', 'DU', 'RL', 'LR', 'FB', 'BF') else f"\nCounting spots from 0 (before the first move), the 8-3 is at spot {best[0]}. Checking the {('odd', 'even')[par]} spots ({', '.join(str(i) for i in range(1 - par, 20, 2))}) and both ends finds nothing better than an 8-{8 - found}; the {('even', 'odd')[par]} spots would find it. The spot is right after the pair `{sk[best[0] - 2]} {sk[best[0] - 1]}`.\n")
        break
    # 2. a 10-mover beats every 8- and 9-mover
    for r in rows('3c', 20):
        if r['L10_solution'] == '-': continue
        pp = onepos_row(20, int(r['idx'])); m8, m9, m10 = (min((v for v in x if v is not None), default=None) for x in pp)
        if m8 is None or m9 is None or not (m10 < m9 and m10 < m8 and m8 - m10 >= 1): continue
        scr, sk, b = make_from('3c', r, '8,10')
        s8, s10 = b['sols'][8]['one'], b['sols'][10]['one']
        if len(s10['steps'][0][1]) != 10: continue
        save('ten', scr, sk, '3c', [('Best with 8-movers', s8, ''), ('Best with algs up to 10', s10, 'a 10-mover; no 9-mover does better than the 8-movers here' if m9 >= m8 else 'a 10-mover')], {'m8': m8, 'm9': m9, 'm10': m10})
        break
    # 3. an insertion that cancels more than its own length
    for r in rows('3c', 20):
        if r['L8_solution'] == '-' or val(r, 'L8_one') is None or val(r, 'L8_one') >= 0: continue
        scr, sk, b = make_from('3c', r, '8'); s8 = b['sols'][8]['one']
        save('negative', scr, sk, '3c', [('The best 8-mover insertion', s8, f"{len(sk)} moves before, {s8['length']} after")], {'cost': s8['cost']})
        break
    else:
        # none among the lines that carry a solution: take any line and build a solution from the lists of 8-movers
        for r in rows('3c', 20):
            if val(r, 'L8_one') is None or val(r, 'L8_one') >= 0: continue
            sk = r['skeleton'].split(); c = state_of(r)
            T = py3.table('c', 8); skel = py3.nums(sk); pp = py3.per_position(T, skel, c, 8)
            i = min((v, i) for i, v in enumerate(pp) if v is not None)[1]
            g = cube.inverse(c)
            for j in range(len(skel) - 1, i - 1, -1): g = cube.compose(cube.compose(py3.MS[skel[j]], g), py3.MI[skel[j]])
            alg = min(T[g], key=lambda a: py3.clen(skel[:i] + list(a) + skel[i:]))
            sol = [py3.NAMES[m] for m in py3.cancel(skel[:i] + list(alg) + skel[i:])]
            scr = exlib.scramble_for(sol); assert cube.do(cube.SOLVED, scr + sk) == c
            b = exlib.best(scr, sk, '8'); s8 = b['sols'][8]['one']
            save('negative', scr, sk, '3c', [('The best 8-mover insertion', s8, f"{len(sk)} moves before, {s8['length']} after")], {'cost': s8['cost']})
            break
    # 4. typical skeletons of the three 4-corner types (cost = the rounded mean), 20 moves, 8-movers
    for typ in ('2c2c-twisted', '2c2c-pure', '3c1t'):
        want = round(iv.mean(iv.cell(typ, 20, 8, 'best')))
        r = solve_line(typ, 20, lambda r: val(r, 'L8_best') == want)
        scr, sk, b = make_from(typ, r, '8'); s8 = b['sols'][8]['two']
        save('typical_' + typ.replace('-', '_'), scr, sk, typ, [('Best with two 8-move comms', s8, '')], {'cost': s8['cost']})
    # 5. a 5c whose best pair of comms is nested
    r = solve_line('5c', 20, lambda r: r['L8_nested'] == '1' and val(r, 'L8_two') is not None and val(r, 'L8_two_flat') is not None and val(r, 'L8_two_flat') - val(r, 'L8_two') >= 2)
    scr, sk, b = make_from('5c', r, '8'); s8 = b['sols'][8]['two']; flat = b['sols'][8]['two-flat']
    save('nested', scr, sk, '5c', [('Best with two 8-move comms', s8, 'the second inside the first'), ('Best without nesting', flat, '')], {'two': s8['cost'], 'flat': flat['cost']})
    # 6. a 19-move 5c whose best is the usual +11 (30 in all)
    r = solve_line('5c', 19, lambda r: val(r, 'L8_best') == 11, pre='base')
    scr, sk, b = make_from('5c', r, '8'); s8 = b['sols'][8]['two']
    save('fivec19', scr, sk, '5c', [('Best with two 8-move comms', s8, '')], {'cost': s8['cost']})
    # 7. two of the server's skeletons, from the real-skeleton run (xreal.py): the 23-move 3c of N2057 and the 16-move 3C1T
    real = {r['id']: r for r in json.load(open(O + 'real_rows.json'))}
    r = real['N2057']; sk = r['reduced'].split(); scr = cube.parse(r['scramble'])
    save('n2057', scr, sk, '3c', [('Best with 8-movers', r['L8sol'], 'the 8-4 that was posted'), ('Best with one alg of up to 10 moves', r['L10sol'], 'a 10-mover that cancels all ten of its moves')],
         {'l8': r['L8sol']['length'], 'l10': r['L10sol']['length'], 'author': r['author_len']})
    # the 22 that 2014chri04 found by hand, read from the message itself and put on the cube
    sys.path.insert(0, B); import links
    m = re.search(r'got a 22!: ([URFDLB2\' ]+)', links.content('N2057')); hand = cube.parse(m.group(1).strip())
    assert cube.do(cube.SOLVED, scr + hand) == cube.SOLVED and cube.cancel(hand) == hand and len(hand) == 22
    add_text('n2057', f"The solution 2014chri04 then found by hand, by rewriting a stretch of the finished one: `{' '.join(hand)}` ({len(hand)} moves, solves the scramble).")
    W['n2057']['hand'] = len(hand)
    r = real['doc92']; sk = r['reduced'].split(); scr = cube.parse(r['scramble'])
    save('if92', scr, sk, '3c1t', [('A comm plus an alg, each of up to 12 moves', r['L12msol'], '')], {'l12m': r['L12msol']['length'], 'if': r['author_len']})
    # 8. a 5c where the best first comm is the wrong one to follow (xgreedy.py): the greedy line is rebuilt here move by move
    import xgreedy
    T8 = py3.table('c', 8); G = {r['idx']: r for r in csv.DictReader(open(O + 'greedy_5c_n20_L8.tsv'), delimiter='\t')}
    for r in rows('5c', 20):
        g = G.get(r['idx'])
        if r['L8_solution'] == '-' or g is None or int(g['g0']) - int(g['exact']) < 2 or int(g['g1']) != int(g['exact']) or int(g['firsts_at_best']) != 1: continue
        sk = r['skeleton'].split(); skel = py3.nums(sk); c = state_of(r); n = len(skel)
        ds = xgreedy.splits(T8, c); cur = list(ds); firsts = []
        for i in range(n, -1, -1):
            if i < n: cur = [cube.compose(cube.compose(py3.MS[skel[i]], a), py3.MI[skel[i]]) for a in cur]
            for k, a in enumerate(cur):
                for alg in T8[a]: firsts.append((py3.clen(skel[:i] + list(alg) + skel[i:]) - n, i, k, alg))
        m1 = min(f[0] for f in firsts); f = next(f for f in firsts if f[0] == m1)
        s1 = py3.cancel(skel[:f[1]] + list(f[3]) + skel[f[1]:]); c1 = cube.compose(c, ds[f[2]]); g2 = cube.inverse(c1); best2 = None
        for j in range(len(s1), -1, -1):
            if j < len(s1): g2 = cube.compose(cube.compose(py3.MS[s1[j]], g2), py3.MI[s1[j]])
            for alg in T8.get(g2, ()):
                v = py3.clen(s1[:j] + list(alg) + s1[j:])
                if best2 is None or v < best2[0]: best2 = (v, j, alg)
        fin = py3.cancel(s1[:best2[1]] + list(best2[2]) + s1[best2[1]:]); nm = lambda q: [py3.NAMES[m] for m in q]
        greedy = {'steps': [(f[1], nm(f[3]), n + 8 - len(s1)), (best2[1], nm(best2[2]), len(s1) + 8 - len(fin))], 'final': nm(fin), 'cost': len(fin) - n, 'length': len(fin), 'nested': False}
        assert greedy['cost'] == int(g['g0'])
        scr, sk, b = make_from('5c', r, '8'); best = b['sols'][8]['two']; assert best['cost'] == int(g['exact'])
        assert cube.do(cube.SOLVED, scr + greedy['final']) == cube.SOLVED
        save('greedy', scr, sk, '5c', [('The best first comm, then the best second', greedy, f"the first is the only 8-{8 - m1} in the skeleton"), ('The best pair', best, '')], {'g0': greedy['cost'], 'exact': best['cost'], 'm1': m1})
        break
    more(val)
    json.dump(W, open(O + 'witness.json', 'w'), indent=1)
    print('witnesses:', {k: (v['type'], v['n']) for k, v in W.items()})
# ---- helpers for the examples that are built from the Python lists (py3) instead of a printed sample solution
def cj(g, m): return cube.compose(cube.compose(py3.MS[m], g), py3.MI[m])
def cases_at(skel, c):
    """The state an insertion has to produce at every spot 0..n."""
    n = len(skel); g = cube.inverse(c); out = [None] * (n + 1)
    for i in range(n, -1, -1):
        if i < n: g = cj(g, skel[i])
        out[i] = g
    return out
def py_solution(sk, c, L=10):
    """A full solution of (skeleton, 3c leftover): the best insertion with algs of up to L moves, from the Python lists."""
    T = py3.table('c', 10 if L > 8 else 8); skel = py3.nums(sk); n = len(skel); G = cases_at(skel, c); best = None
    for i in range(n + 1):
        for a in T.get(G[i], ()):
            if len(a) > L: break
            v = py3.clen(skel[:i] + list(a) + skel[i:])
            if best is None or v < best[0]: best = (v, i, a)
    return None if best is None else [py3.NAMES[m] for m in py3.cancel(skel[:best[1]] + list(best[2]) + skel[best[1]:])]
def from_python(sk, c, caps, L=10):
    sol = py_solution(sk, c, L); scr = exlib.scramble_for(sol); assert cube.do(cube.SOLVED, scr + sk) == c
    return scr, exlib.best(scr, sk, caps)
def add_text(name, text): open(f'{B}wit_{name}.md', 'a').write('\n' + text.strip() + '\n')
def shortest_per_spot(skel, c):
    T = py3.table('c', 10); return [min((len(a) for a in T.get(g, ())), default=None) for g in cases_at(skel, c)]
def greedy_line(L, skel, c):
    """Insertion Finder's greedy 0 with every 3c alg of up to L moves: every first comm that ties for the fewest added
    moves is followed by its best second comm; the shortest result (the first found among equals)."""
    import xgreedy
    T = py3.table('c', 10 if L > 8 else 8); n = len(skel); ds = xgreedy.splits(T, c); cur = list(ds); firsts = []
    for i in range(n, -1, -1):
        if i < n: cur = [cj(a, skel[i]) for a in cur]
        for k, a in enumerate(cur):
            for alg in T[a]:
                if len(alg) > L: break
                firsts.append((py3.clen(skel[:i] + list(alg) + skel[i:]) - n, i, k, alg))
    m1 = min(f[0] for f in firsts); best = None
    for f in firsts:
        if f[0] != m1: continue
        s1 = py3.cancel(skel[:f[1]] + list(f[3]) + skel[f[1]:]); g2 = cube.inverse(cube.compose(c, ds[f[2]]))
        for j in range(len(s1), -1, -1):
            if j < len(s1): g2 = cj(g2, s1[j])
            for alg in T.get(g2, ()):
                if len(alg) > L: break
                v = py3.clen(s1[:j] + list(alg) + s1[j:])
                if best is None or v < best[0]: best = (v, f, s1, j, alg)
    if best is None: return None
    v, f, s1, j, alg = best; fin = py3.cancel(s1[:j] + list(alg) + s1[j:]); nm = lambda q: [py3.NAMES[m] for m in q]
    return {'steps': [(f[1], nm(f[3]), n + len(f[3]) - len(s1)), (j, nm(alg), len(s1) + len(alg) - len(fin))], 'final': nm(fin), 'cost': len(fin) - n, 'length': len(fin), 'nested': False, 'm1': m1, 'ties': sum(1 for x in firsts if x[0] == m1)}
def more(val):
    """The examples added with the review: no 8-mover anywhere (20 and 21 moves), every third spot, three spots on after a
    10-move case, a setup-type 10-mover that wins, greedy 0 made worse by more algs."""
    T8 = py3.table('c', 8); T10 = py3.table('c', 10); nm = lambda q: ' '.join(py3.NAMES[m] for m in q)
    # a. no 8-mover at any spot of a 20-move 3c skeleton
    r = next(r for r in rows('3c', 20) if r['L8_one'] == 'inf')
    sk = r['skeleton'].split(); c = state_of(r); scr, b = from_python(sk, c, '8,10'); assert b['type'] == '3c' and 8 not in b['sols'] or 'one' not in b['sols'].get(8, {})
    s10 = b['sols'][10]['one']; opt = shortest_per_spot(py3.nums(sk), c); assert all(k is None or k > 8 for k in opt)
    save('no8', scr, sk, '3c', [('With 8-movers', None, f'nothing. At none of the {len(sk) + 1} spots does the case have an 8-move alg.'), ('Best with algs of up to 10 moves', s10, f"a {len(s10['steps'][0][1])}-mover")], {'idx': int(r['idx']), 'l10': s10['length']})
    add_text('no8', 'Shortest alg for the case at each spot, from before the first move to after the last: ' + ', '.join('more than 10' if k is None else str(k) for k in opt) + '.')
    # b. 21 to 3c that does not give 29
    r = next(r for r in rows('3c', 21, 'base') if r['L8_one'] == 'inf' and val(r, 'L10_one') is not None and val(r, 'L10_one') >= 9)
    sk = r['skeleton'].split(); c = state_of(r); scr, b = from_python(sk, c, '8,10'); s10 = b['sols'][10]['one']; assert 'one' not in b['sols'].get(8, {}) and s10['length'] >= 30
    save('n21', scr, sk, '3c', [('With 8-movers', None, 'nothing: no spot has a case with an 8-move alg.'), ('Best with algs of up to 10 moves', s10, f"a {len(s10['steps'][0][1])}-mover")], {'idx': int(r['idx']), 'l10': s10['length']})
    # c. every third spot misses the only 8-3; every other spot from the start finds it
    for r in rows('3c', 20):
        if val(r, 'L8_one') != 5: continue
        pp = onepos_row(20, int(r['idx']))[0]; best = [i for i, v in enumerate(pp) if v == 5]
        if len(best) != 1 or best[0] in (0, 20) or best[0] % 2 or best[0] % 3 == 0: continue
        j = best[0]; third = [v for i, v in enumerate(pp) if (i % 3 == 0 or i == 20) and v is not None]
        if not third or min(third) < 7: continue                      # a clear miss: nothing better than an 8-1 on the way
        sk = r['skeleton'].split(); c = state_of(r); scr, b = from_python(sk, c, '8', 8); sol = b['sols'][8]['one']; assert sol['cost'] == 5 and sol['steps'][0][0] == j
        save('third', scr, sk, '3c', [('The best 8-mover insertion', sol, f'the only 8-3 in the skeleton, after move {j}')], {'spot': j, 'third_best': min(third), 'per_spot': pp})
        add_text('third', f"Counting spots from 0 (before the first move), the 8-3 is at spot {j}. Every other spot from the start (0, 2, 4, and so on) passes it. Every third spot from the start (0, 3, 6, and so on, and the end) does not, and finds nothing better than an 8-{8 - min(third)}. Of the three ways to take every third spot, only the one that starts at spot {j % 3} passes spot {j}.")
        break
    else: raise SystemExit('no witness for every third spot')
    # d. paulduc03's rule: three spots on after a case that needs a 10-mover
    P = {}
    with open(f'{O}onepos_3c_n20.tsv') as f:
        f.readline()
        for l in f:
            p = l.rstrip('\n').split('\t'); P[int(p[0])] = [[None if x == 'x' else int(x) for x in part.split(',')] for part in p[1:4]]
    for r in rows('3c', 20):
        if val(r, 'L8_one') is None or val(r, 'L8_one') > 5: continue
        c8, c9, c10 = P[int(r['idx'])]; b_ = min(v for v in c8 if v is not None); best = [i for i, v in enumerate(c8) if v == b_]
        if len(best) != 1 or best[0] % 2 or best[0] < 2 or best[0] >= 19: continue
        j = best[0]; ten = lambda i: c8[i] is None and c9[i] is None and c10[i] is not None
        if not ten(j - 2) or any(ten(i) for i in range(0, j - 2, 2)): continue      # the walk 0, 2, 4, ... reaches spot j - 2 and meets its first 10-move case there
        seen = {0, 20}; i = 0
        while i <= 20: seen.add(i); i += 3 if ten(i) else 2
        got = min(c8[i] for i in seen if c8[i] is not None)
        if j in seen or got < b_ + 2: continue
        sk = r['skeleton'].split(); c = state_of(r); scr, b = from_python(sk, c, '8', 8); sol = b['sols'][8]['one']; assert sol['cost'] == b_ and sol['steps'][0][0] == j
        G = cases_at(py3.nums(sk), c); a10 = T10[G[j - 2]][0]; assert len(a10) == 10 and not T8.get(G[j - 2])
        save('tenskip', scr, sk, '3c', [('The best 8-mover insertion', sol, f'the only 8-{8 - b_} in the skeleton, after move {j}')], {'spot': j, 'rule_best': got, 'best': b_, 'visited': sorted(seen)})
        add_text('tenskip', f"Counting spots from 0. Checking every other spot from the start, spot {j - 2} is the first whose case has no alg shorter than 10 moves (one of them: `{nm(a10)}`). Two spots on, at spot {j}, is the 8-{8 - b_}. Going three on instead lands on spot {j + 1}, and the walk (spots {', '.join(str(i) for i in sorted(seen))}) finds nothing better than an 8-{8 - got}.")
        break
    else: raise SystemExit('no witness for three spots on')
    # e. a 10-mover that is a setup move around an 8-mover and still beats every 8- and 9-mover
    eight = {a for v in T8.values() for a in v}; inv = lambda m: 3 * (m // 3) + 2 - m % 3; CONJ = {}
    for a in eight:
        for x in range(18):
            q = py3.cancel([x] + list(a) + [inv(x)])
            if len(q) == 10: CONJ.setdefault(tuple(q), []).append((x, a))
    done = False
    for r in rows('3c', 20):
        c8, c9, c10 = P[int(r['idx'])]; m8, m9, m10 = (min((v for v in x if v is not None), default=None) for x in (c8, c9, c10))
        if m8 is None or m9 is None or not m10 < m9: continue
        sk = r['skeleton'].split(); skel = py3.nums(sk); c = state_of(r); G = cases_at(skel, c)
        win = [(i, a) for i in range(21) for a in T10.get(G[i], ()) if len(a) == 10 and py3.clen(skel[:i] + list(a) + skel[i:]) - 20 == m10]
        if not all(a in CONJ for i, a in win): continue
        scr, b = from_python(sk, c, '8,10'); s8, s10 = b['sols'][8]['one'], b['sols'][10]['one']
        a = tuple(py3.nums(s10['steps'][0][1])); assert a in CONJ and s8['cost'] == m8 and s10['cost'] == m10
        fin = py3.nums(s10['final'])
        for x, A in CONJ[a]:
            for k in range(20):                                            # the 8-mover inside move k of the skeleton, the move done in two parts
                M = skel[k]
                for M1 in range(3 * (M // 3), 3 * (M // 3) + 3):
                    M2 = py3.cancel([inv(M1), M])
                    if M1 == M or len(M2) != 1: continue
                    if py3.cancel(skel[:k] + [M1] + list(A) + M2 + skel[k + 1:]) == fin and not done:
                        save('setup10', scr, sk, '3c', [('Best with 8-movers', s8, ''), ('Best with algs of up to 10 moves', s10, 'a setup move, an 8-mover and the setup undone')], {'m8': m8, 'm9': m9, 'm10': m10})
                        add_text('setup10', f"The 10-mover is the 8-mover `{nm(A)}` between `{py3.NAMES[x]}` and `{py3.NAMES[inv(x)]}`. The same solution is that 8-mover put inside move {k + 1} of the skeleton, the `{py3.NAMES[M]}` done in two parts: `{py3.NAMES[M1]}`, the comm, `{py3.NAMES[M2[0]]}`. No spot between two moves gives that with an 8-mover.")
                        done = True
        if done: break
    else: raise SystemExit('no witness for a setup-type 10-mover')
    # f. greedy 0: more algs, longer result
    G8 = {r['idx']: r for r in csv.DictReader(open(O + 'greedy_5c_n20_L8.tsv'), delimiter='\t')}; cand = []
    for g10 in csv.DictReader(open(O + 'greedy_5c_n20_L10.tsv'), delimiter='\t'):
        g8 = G8.get(g10['idx'])
        if g8 is None or 'inf' in (g8['g0'], g10['g0']) or int(g10['g0']) <= int(g8['g0']): continue
        r = next(r for r in rows('5c', 20) if r['idx'] == g10['idx']); sk = r['skeleton'].split(); skel = py3.nums(sk); c = state_of(r)
        a8 = greedy_line(8, skel, c); a10 = greedy_line(10, skel, c)
        assert a8['cost'] == int(g8['g0']) and a10['cost'] == int(g10['g0']), (a8['cost'], g8['g0'], a10['cost'], g10['g0'])
        assert a10['m1'] < a8['m1'] and len(a10['steps'][0][1]) > 8          # the longer list has a better first comm, and that is why
        cand.append((a8['ties'] + a10['ties'], int(r['idx']), sk, c, a8, a10))
    print('greedy 0 worse with more algs:', [(x[1], x[4]['cost'], x[5]['cost'], x[4]['ties'], x[5]['ties']) for x in cand])
    _, idx, sk, c, a8, a10 = min(cand, key=lambda x: (x[0], x[1]))
    scr = exlib.scramble_for(a8['final']); assert cube.do(cube.SOLVED, scr + sk) == c and cube.do(cube.SOLVED, scr + a10['final']) == cube.SOLVED and exlib.type_of(c) == '5c'
    f8, f10 = a8['steps'][0], a10['steps'][0]; d = a8['m1'] - a10['m1']
    tie = lambda a: '' if a['ties'] == 1 else f" ({a['ties']} first comms tie for the best; this is the one whose second comm is best)"
    save('greedy10', scr, sk, '5c', [('Best first comm, then the best second, 8-movers only', a8, f"the first comm is an 8-{f8[2]}{tie(a8)}"),
                                     ('The same rule with every 3c alg of up to 10 moves', a10, f"the first comm is now a {len(f10[1])}-{f10[2]}{tie(a10)}, {'one move' if d == 1 else f'{d} moves'} better than the 8-{f8[2]}, and the second comes out worse")],
         {'idx': idx, 'g8': a8['cost'], 'g10': a10['cost'], 'n_cases': len(cand)})

def verify():
    n = bad = 0
    for p in sorted(glob.glob(B + 'wit_*.md')):
        txt = open(p).read()
        scr = cube.parse(re.search(r'^Scramble: `([^`]+)`$', txt, flags=re.M).group(1))
        m = re.search(r'^Skeleton: `([^`]+)` \((\d+)\), leaves ([^:]+): (.+)$', txt, flags=re.M); sk = cube.parse(m.group(1))
        s = cube.do(cube.SOLVED, scr + sk); typ = exlib.type_of(s)
        if len(sk) != int(m.group(2)) or iv.LONG[typ] != m.group(3) or exlib.left_text(s) != m.group(4): bad += 1
        for total, blk in re.findall(r'^\*\*[^\n]*?(\d+) in all[^\n]*\n\n```\n(.*?)\n```', txt, flags=re.M | re.S):
            b, fin = exlib.check_block(blk.split('\n'), scr, sk); n += 1
            if b or fin != int(total): bad += 1
        for seq, k in re.findall(r'`([^`]+)` \((\d+) moves, solves the scramble\)', txt):          # a whole solution quoted in a sentence
            q = cube.parse(seq); n += 1
            if len(q) != int(k) or cube.cancel(q) != q or cube.do(cube.SOLVED, scr + q) != cube.SOLVED: bad += 1
    print(f'witness blocks: {len(glob.glob(B + "wit_*.md"))} files, {n} written solutions replayed on the sticker model; mismatches: {bad}')
    return bad
if __name__ == '__main__':
    if '--verify' not in sys.argv: main()
    sys.exit(1 if verify() else 0)
