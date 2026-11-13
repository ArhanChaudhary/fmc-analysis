#!/usr/bin/env python3
"""Real skeletons against the search: the server's worked examples and Kalbarczyk's example solves.

Reads out/real_meta.json (real_cases.py) and out/real_best.txt (real_run.py), checks every case on the sticker
model, and writes out/real.json (everything the report quotes) and the tables report/data/real_*.md.

  xreal.py --need     print the (type, length) cells of random skeletons that the comparison needs and that the main
                      runs do not have (odd lengths, lengths under 10 or over 30); run them with
                      `instools runs <type> <lengths> 20000 2026 --L 8,10 --prefix base`, then histograms.py
  xreal.py --corpus   write the files for `instools corpus` (real sequences, random leftovers) and run it
  xreal.py            the checks, out/real.json and the tables"""
import names
import json, re, sys, os, collections, subprocess, math, random
import cube, cubie, exlib, iv, check_solutions
from iv import O, SHOW, fmt, num, f2, f1
D = '/data/fmc/insertion-cost/report/data/'
def write(name, lines):
    open(D + name + '.md', 'w').write('\n'.join(lines) + '\n'); print(name, len(lines), 'lines')
META = json.load(open(O + 'real_meta.json')); CASES = META['cases']
def load():
    txt = open(O + 'real_best.txt').read(); blocks = re.split(r'^CASE\t(\d+)\n', txt, flags=re.M)[1:]
    out = {}
    for k, body in zip(blocks[0::2], blocks[1::2]): out[int(k)] = exlib.parse_best(body)
    return out
def cell(typ, n, L, model):
    return iv.cell(typ, n, L, model, 'sample') or iv.cell(typ, n, L, model, 'base')
def base_model(typ): return 'one' if typ in ('3c', '3e') else 'best'
def length_of(sol): return None if sol is None else sol['length']
def rows():
    """One row per case that the tool's models cover."""
    B = load(); skipped = {int(x) for x in open(O + 'real_best.skipped').read().split()}; out = []
    for k, c in enumerate(CASES, 1):
        b = B[k]; scr = cube.parse(c['scramble']); sk = cube.cancel(cube.parse(c['skeleton']))
        s = cube.do(cube.SOLVED, scr + sk)
        cp, ct, ep, ef = [[int(x) for x in part.split(',')] for part in b['left'].split(';')]
        assert cubie.make(cp, ct, ep, ef) == s and b['skeleton'] == sk, (c['id'], 'the tool and the sticker model disagree on what is left')
        typ = b['type']
        if typ == 'not one of the types' or b['parity']: continue
        assert exlib.type_of(s) == typ, (c['id'], exlib.type_of(s), typ)
        r = dict(c, case=k, type=typ, n=len(sk), reduced=' '.join(sk), mixed12=k not in skipped)
        for L in (8, 10, 12):
            S = b['sols'].get(L, {})
            one = S.get('one') or S.get('direct'); two = S.get('two'); mixed = S.get('mixed')
            plain = [x['length'] for x in (one, two) if x]
            r[f'L{L}'] = min(plain) - len(sk) if plain else None                                   # one / direct / two
            allm = plain + ([mixed['length']] if mixed else [])
            r[f'L{L}m'] = min(allm) - len(sk) if allm else None                                  # with a comm plus an alg as well
            r[f'L{L}one'] = one['length'] - len(sk) if one else None
            r[f'L{L}two'] = two['length'] - len(sk) if two else None
            pack = lambda sol, nm: None if sol is None else {'steps': sol['steps'], 'final': sol['final'], 'cost': sol['cost'], 'length': sol['length'], 'nested': sol['nested'], 'model': nm}
            cands = [(x['length'], k, nm, x) for k, (x, nm) in enumerate(((one, 'one' if typ in ('3c', '3e') else 'direct'), (two, 'two'))) if x]
            best_plain = min(cands)[2:] if cands else None                      # shortest; one insertion before two on a tie
            r[f'L{L}model'] = best_plain[0] if best_plain else None
            r[f'L{L}sol'] = pack(best_plain[1], best_plain[0]) if best_plain else None
            r[f'L{L}msol'] = pack(mixed, 'mixed') if mixed and (not plain or mixed['length'] < min(plain)) else None      # only when it beats the others
        # Anything allowed at a cap is allowed at the next one.  The plain models are exact, so they must come out
        # monotone.  The comm-plus-alg search at cap 12 did not finish for some edge leftovers: there the value is the
        # best of what did finish (cap 12 plain, cap 10 with a comm plus an alg), and the solution shown is that one.
        for a, b in (('L8', 'L10'), ('L10', 'L12')):
            assert r[a] is None or (r[b] is not None and r[b] <= r[a]), (c['id'], a, r[a], b, r[b])
        if r['mixed12']:
            assert r['L10m'] is None or r['L12m'] <= r['L10m'], (c['id'], 'cap 12 with a comm plus an alg above cap 10')
        for a, b in (('L8m', 'L10m'), ('L10m', 'L12m')):
            if r[a] is not None and (r[b] is None or r[a] < r[b]):
                assert b == 'L12m' and not r['mixed12'], (c['id'], a, r[a], b, r[b])
                r[b] = r[a]; r[b[:-1] + 'msol'] = r[a[:-1] + 'msol'] if (r[b[:-1]] is None or r[a] < r[b[:-1]]) else None
        for a, b in (('L8m', 'L10m'), ('L10m', 'L12m'), ('L8', 'L8m'), ('L10', 'L10m'), ('L12', 'L12m')):
            assert r[a] is None or (r[b] is not None and r[b] <= r[a]), (c['id'], a, r[a], b, r[b])
        if c['final'] is not None or c['replay_len'] is not None:
            r['author_len'] = c['replay_len'] if c['replayed'] else c['final']
            r['author_added'] = r['author_len'] - len(sk)
        out.append(r)
    return out
def need():
    R = rows(); want = collections.defaultdict(set)
    for r in R:
        if not (r['n'] % 2 == 0 and 10 <= r['n'] <= 30): want[r['type']].add(r['n'])
    for t, ns in sorted(want.items()): print(t, ','.join(map(str, sorted(ns))))
def rand_mean(typ, n, L):
    c = cell(typ, n, L, base_model(typ))
    return (iv.mean(c), c['inf'] / c['n'], c) if c else (None, None, None)
GROUP = collections.OrderedDict([('3c', ['3c']), ('2tc and 3tc', ['2tc', '3tc']), ('2c2c (pure or twisted)', ['2c2c-pure', '2c2c-twisted']), ('3c1t', ['3c1t']), ('5c', ['5c']), ('3c3c', ['3c3c']),
                                 ('3e', ['3e']), ('2e2e, 2fe, 3e1f, 5e, 3e3e', ['2e2e', '2e2e-flipped', '2f', '3e1f', '5e', '3e3e'])])
def main():
    n_sol = check_solutions.check_best(O + 'real_best.txt')
    R = rows(); U = [r for r in R if not r['dup_of']]              # one row per skeleton
    J = {'examples': META['examples_in_file'], 'excluded': META['excluded'], 'cases_run': len(CASES), 'covered': len(R), 'skeletons': len(U),
         'server': sum(1 for r in R if r['origin'] == 'server'), 'kalbarczyk': sum(1 for r in R if r['origin'] == 'kalbarczyk'),
         'inverse': sum(1 for r in R if r['inverse']), 'replayed': sum(1 for r in R if r['origin'] == 'server' and r['replayed']),
         'with_final': sum(1 for r in R if 'author_len' in r), 'no_mixed12': sum(1 for r in R if not r['mixed12']), 'by_type': collections.Counter(r['type'] for r in U)}
    B = load(); J['parity'] = sum(1 for k in B if B[k]['parity']); J['other'] = sum(1 for k in B if B[k]['type'] == 'not one of the types')
    # ---- what was usable
    ex = META['excluded']
    L = ['| Worked examples | How many |', '|---|---:|', f"| Worked examples in the reading notes | {META['examples_in_file']} |"]
    for key in ('written with inverse-scramble parts', 'skeleton has rotations, slice or wide moves', 'scramble not in face turns', 'corners and edges both left', 'parity (2 corners and 2 edges)', 'more than 6 pieces of one kind left', 'scramble and skeleton do not fit'):
        if ex.get(key): L.append(f'| left out: {key} | {ex[key]} |')
    srv = [r for r in R if r['origin'] == 'server']
    L.append(f"| left out: three or more comms needed (not one of the types) | {ex['kept'] - len(srv)} |")
    L.append(f'| **used, from the server** | **{len(srv)}** |')
    L.append(f"| used, from Kalbarczyk's example solves (of 46 read) | {J['kalbarczyk']} |")
    L.append(f'| **used in all** | **{len(R)}** |'); L.append(f"| distinct skeletons among them | {len(U)} |")
    L.append(f"| of the server's: the author's own solution replays to the stated length | {J['replayed']} |")
    write('real_counts', L)
    # ---- real against random, like for like (one / direct / two; no comm plus alg)
    L = ['| Leftover | Real skeletons | Their mean length, moves | Cap 8: something fits on | Cap 8: real, mean added | Cap 8: random of the same lengths, mean added | Cap 10: real, mean added | Cap 10: random, mean added | Cap 12: real, mean added |', '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    comp = {}
    for g, types in GROUP.items():
        rs = [r for r in U if r['type'] in types]
        if not rs: continue
        cells = []; comp[g] = {'n': len(rs)}
        for Lc in (8, 10):
            real, rand, miss = [], [], 0
            for r in rs:
                m, _, c = rand_mean(r['type'], r['n'], Lc)
                if r[f'L{Lc}'] is None: miss += 1; continue
                if m is None or m != m: continue
                real.append(r[f'L{Lc}']); rand.append(m)
            if real:
                d = [a - b for a, b in zip(real, rand)]; md = sum(d) / len(d)
                sd = (sum((x - md) ** 2 for x in d) / max(len(d) - 1, 1)) ** 0.5
                comp[g][str(Lc)] = {'real': sum(real) / len(real), 'rand': sum(rand) / len(rand), 'k': len(real), 'diff': md, 'se': sd / len(d) ** 0.5, 'none': miss}
                assert Lc == 8 or len(real) == len(rs), (g, Lc, 'a real skeleton without a solution at this cap')
                cells += ([f'{len(real)} of {len(rs)}'] if Lc == 8 else []) + [f2(sum(real) / len(real)), f2(sum(rand) / len(rand))]
            else: cells += ([''] if Lc == 8 else []) + ['', '']
        r12 = [r['L12'] for r in rs if r['L12'] is not None]
        comp[g]['12'] = sum(r12) / len(r12) if r12 else None
        assert len(r12) == len(rs)
        L.append(f"| {g} | {len(rs)} | {f1(sum(r['n'] for r in rs) / len(rs))} | {cells[0]} | {cells[1]} | {cells[2]} | {cells[3]} | {cells[4]} | {f2(sum(r12) / len(r12)) if r12 else ''} |")
    write('real_cost', L); J['comp'] = comp
    # ---- the same per cap with a comm plus an alg allowed (what Insertion Finder also does)
    L = ['| Leftover | Real skeletons | Cap 8: something fits on | Cap 8: mean added | Cap 10: mean added | Cap 12: mean added | Cap 12 comm-plus-alg search not finished for |', '|---|---:|---:|---:|---:|---:|---:|']
    J['mixed'] = {}
    for g, types in GROUP.items():
        rs = [r for r in U if r['type'] in types]
        if not rs: continue
        v8 = [r['L8m'] for r in rs if r['L8m'] is not None]; v10 = [r['L10m'] for r in rs]; v12 = [r['L12m'] for r in rs]
        assert None not in v10 and None not in v12
        m10, m12 = sum(v10) / len(v10), sum(v12) / len(v12); assert m12 <= m10 + 1e-9, (g, m10, m12)
        if len(v8) == len(rs): assert m10 <= sum(v8) / len(v8) + 1e-9
        J['mixed'][g] = {'k8': len(v8), '8': sum(v8) / len(v8) if v8 else None, '10': m10, '12': m12}
        L.append(f"| {g} | {len(rs)} | {len(v8)} of {len(rs)} | {f2(sum(v8) / len(v8)) if v8 else ''} | {f2(m10)} | {f2(m12)} | {sum(1 for r in rs if not r['mixed12'])} |")
    write('real_mixed', L)
    # ---- the author against the best
    def author_table(sel, name):
        A = [r for r in R if 'author_added' in r and sel(r)]
        L = ['| Compared with the best at | Solutions | Author shorter | Same length | Author 1 move longer | Author 2 longer | Author 3 or more longer | Author, mean added | Best, mean added |', '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
        res = {}
        for Lc, key, label in ((8, 'L8', 'cap 8: one comm or two (edges: algs of 6 to 8)'), (10, 'L10', 'cap 10: one comm, two comms or one alg'), (12, 'L12', 'cap 12: one comm, two comms or one alg'),
                               (10, 'L10m', 'cap 10, a comm plus an alg also allowed'), (12, 'L12m', 'cap 12, a comm plus an alg also allowed')):
            v = [(r['author_added'], r[key]) for r in A if r[key] is not None]
            if not v: continue
            c = collections.Counter(max(-1, min(3, a - b)) for a, b in v); k = len(v)
            L.append(f"| {label} | {k} | {c[-1]} | {c[0]} | {c[1]} | {c[2]} | {c[3]} | {f2(sum(a for a, b in v) / k)} | {f2(sum(b for a, b in v) / k)} |")
            res[key] = {'k': k, 'shorter': c[-1], 'same': c[0], 'plus1': c[1], 'plus2': c[2], 'plus3': c[3], 'author': sum(a for a, b in v) / k, 'best': sum(b for a, b in v) / k}
        write(name, L); return res, A
    J['author_hand'], AH = author_table(lambda r: r['source'] == 'hand', 'real_author_hand')
    J['author_if'], AI = author_table(lambda r: r['source'] == 'IF', 'real_author_if')
    J['author_hand_3c'], _ = author_table(lambda r: r['source'] == 'hand' and r['type'] == '3c', 'real_author_hand_3c')
    TWO_CORNER = ('2tc', '3tc', '2c2c-pure', '2c2c-twisted', '3c1t', '5c', '3c3c')
    J['author_hand_two'], AT = author_table(lambda r: r['source'] == 'hand' and r['type'] in TWO_CORNER, 'real_author_hand_two')
    A3 = [r for r in R if 'author_added' in r and r['source'] == 'hand' and r['type'] == '3c']
    J['author_dups'] = {'3c': sum(1 for r in A3 if r['dup_of']), 'two': sum(1 for r in AT if r['dup_of']), 'all': sum(1 for r in AH if r['dup_of'])}
    J['if_wording_only'] = sum(1 for r in AI if r['wording_only'])
    # solutions shorter than the best at cap 12: listed, with what the author did
    short = [r for r in R if 'author_added' in r and r['L12m'] is not None and r['author_added'] < r['L12m']]
    J['shorter12'] = [{'id': r['id'], 'type': r['type'], 'n': r['n'], 'author': r['author_len'], 'best12': r['n'] + r['L12m'], 'source': r['source'], 'replayed': r['replayed'], 'steps': r['steps'], 'notes': r['notes']} for r in short]
    WHY = {'N4763a': 'two slice insertions (`E2 ... E2`) on top of the 3e algs', 'N5493': "a slice pair (`M' ... M`) on top of the comm", 'N6810': "a slice pair (`S ... S'`) on top of the comm",
           'N6662': 'a stretch of the finished solution rewritten shorter', 'K27': 'a stretch of the finished solution rewritten shorter (the `[] =` line of the solve)', 'K97': 'a stretch of the finished solution rewritten shorter (the `[] =` line of the solve)',
           'D4876': 'two moves of the skeleton made wide, which changes the skeleton'}
    L = ['| Example | By | Leftover | Skeleton, moves | Author\'s solution, moves | Best at cap 12 with a comm plus an alg, moves | What the author did besides inserting |', '|---|---|---|---:|---:|---:|---|']
    for x in J['shorter12']:
        r = next(r for r in R if r['id'] == x['id'])
        who = 'Kalbarczyk, solve ' + x['id'][1:] if x['id'].startswith('K') else f"{names.shown(r['author'])}, [[{x['id'].rstrip('ab')}]]"
        L.append(f"| {who} | {'hand' if x['source'] == 'hand' else 'Insertion Finder'} | {SHOW[x['type']]} | {x['n']} | {x['author']} | {x['best12']} | {WHY[x['id']]} |")
    write('real_shorter', L)
    # ---- the (8-2) notes: what the authors' insertions cancel
    steps = []
    for r in R:
        if r['source'] != 'hand': continue
        st = r['steps'] if r['replayed'] and r['steps'] else r['notes']
        for a, b in st: steps.append((a, b, r['type'], 'replayed' if r['replayed'] and r['steps'] else 'as written'))
    e8 = [s for s in steps if s[0] == 8]; c8 = collections.Counter(min(s[1], 6) for s in e8)
    groups = [(label, [s for s in e8 if sel(s)]) for label, sel in (('All of them', lambda s: True), ('On a 3c skeleton', lambda s: s[2] == '3c'), ('On a skeleton that needs two', lambda s: s[2] not in ('3c', '3e')))]
    groups = [(label, v) for label, v in groups if v]
    L = ['| What the 8-move insertion cancels | ' + ' | '.join(f'{g}: insertions | {g}: share' for g, _ in groups) + ' |', '|---|' + '---:|---:|' * len(groups)]
    L.append('| all of them | ' + ' | '.join(f'{len(v)} | ' for _, v in groups) + ' |')
    cs = [collections.Counter(min(s[1], 6) for s in v) for _, v in groups]
    for k in range(7):
        L.append(f"| {'8-6 or more' if k == 6 else f'8-{k}'} | " + ' | '.join(f'{c[k]} | {fmt(c[k], len(v))}' if c[k] else '0 | ' for c, (_, v) in zip(cs, groups)) + ' |')
    write('real_notes', L)
    J['notes'] = {'steps': len(steps), 'eight': len(e8), 'by_len': dict(collections.Counter(s[0] for s in steps)), 'eight_mean_cancel': sum(s[1] for s in e8) / max(len(e8), 1),
                  'eight_ge3': sum(1 for s in e8 if s[1] >= 3), 'replayed_steps': sum(1 for s in steps if s[3] == 'replayed')}
    # ---- by where the skeleton comes from, 3c and 5c, cap 8
    L = ['| Skeletons | 3c: how many | 3c: real minus random, moves | 3c: ± one standard error | 5c: how many | 5c: real minus random, moves | 5c: ± one standard error |', '|---|---:|---:|---:|---:|---:|---:|']
    subsets = collections.OrderedDict([('all', lambda r: True), ('from the server, an insertion written out', lambda r: r['origin'] == 'server' and r['n_ins'] > 0),
                                       ('from the server, no insertion written (a skeleton posted as it is)', lambda r: r['origin'] == 'server' and r['n_ins'] == 0),
                                       ("Kalbarczyk's example solves", lambda r: r['origin'] == 'kalbarczyk'),
                                       ('the last two together', lambda r: r['origin'] == 'kalbarczyk' or r['n_ins'] == 0)])
    J['subsets'] = {}
    for name, sel in subsets.items():
        cells = []; J['subsets'][name] = {}
        for typ in ('3c', '5c'):
            rs = [r for r in U if r['type'] == typ and sel(r) and r['L8'] is not None]
            d = [r['L8'] - rand_mean(typ, r['n'], 8)[0] for r in rs]
            if d:
                md = sum(d) / len(d); se = (sum((x - md) ** 2 for x in d) / max(len(d) - 1, 1) / len(d)) ** 0.5
                cells += [str(len(d)), f'{md:+.2f}', f'{se:.2f}']; J['subsets'][name][typ] = {'k': len(d), 'diff': md, 'se': se}
            else: cells += ['0', '', '']
        L.append(f'| {name} | ' + ' | '.join(cells) + ' |')
    write('real_subsets', L)
    # ---- the real move sequences with a random leftover on them (xreal.py --corpus)
    import csv as _csv
    C = {}; T = {Lc: [f'| Leftover put on the real move sequences | Skeletons made (a real sequence with a random leftover) | Cap {Lc}: real sequences, mean added | Cap {Lc}: the mean is over | Cap {Lc}: random sequences of the same lengths, mean added |', '|---|---:|---:|---|---:|'] for Lc in (8, 10)}
    for typ in ('3c', '5c'):
        p = f'{O}corpus_real_{typ}.tsv'
        if not os.path.exists(p): continue
        lines = list(_csv.DictReader(open(p), delimiter='\t')); C[typ] = {'lines': len(lines), 'sequences': len({r['skeleton'] for r in lines})}
        for Lc in (8, 10):
            real, rnd = [], []; nc = inf = 0
            for r in lines:
                v = r[f'L{Lc}_best']
                if v in ('nc', 'inf'): nc += v == 'nc'; inf += v == 'inf'; continue
                real.append(int(v)); rnd.append(rand_mean(typ, len(r['skeleton'].split()), Lc)[0])
            C[typ][str(Lc)] = {'k': len(real), 'real': sum(real) / len(real), 'rand': sum(rnd) / len(rnd), 'not_run': nc, 'nothing_fits': inf}
            assert not (nc and inf)
            over = f'the {len(real):,} where something fits' if inf else f'the first {len(real):,} (only those were run)' if nc else 'all of them'
            T[Lc].append(f"| a random {typ} | {len(lines):,} | {sum(real) / len(real):.2f} | {over} | {sum(rnd) / len(rnd):.2f} |")
    write('real_corpus', T[8]); write('real_corpus_10', T[10])
    # ---- where the best 3c insertion sits: real skeletons with their own leftover, real sequences with a random 3c,
    #      and random sequences of the same lengths (thirds of the skeleton by position / length)
    import py3
    T8 = py3.table('c', 8)
    def thirds(items):
        """items: (move numbers, leftover state).  Returns [first, middle, last] weights and the number counted."""
        w = [0.0, 0.0, 0.0]; k = 0; ends = 0.0
        for sk, c in items:
            pp = py3.per_position(T8, sk, c, 8); v = [x for x in pp if x is not None]
            if not v: continue
            pos = [i for i, x in enumerate(pp) if x == min(v)]; n = len(sk); k += 1
            for i in pos: w[min(2, 3 * i // (n + 1))] += 1 / len(pos)            # the cut of section 8.1 (xtables.third)
        return w, k
    item = lambda r: (py3.nums(r['reduced']), cube.do(cube.SOLVED, cube.parse(r['scramble']) + cube.parse(r['reduced'])))
    real3 = [r for r in U if r['type'] == '3c']; real_items = [item(r) for r in real3]
    w_real, k_real = thirds(real_items)
    doug = lambda r: names.shown(r['author']).startswith(('DougCube', 'Doug L'))
    w_doug, k_doug = thirds([item(r) for r in real3 if doug(r)]); w_rest, k_rest = thirds([item(r) for r in real3 if not doug(r)])
    assert k_doug + k_rest == k_real
    J['doug'] = {'examples': sum(1 for r in R if doug(r)), 'skeletons_3c': k_doug, 'thirds': w_doug, 'rest_3c': k_rest, 'rest_thirds': w_rest}
    lines = list(_csv.DictReader(open(f'{O}corpus_real_3c.tsv'), delimiter='\t'))[:6000]
    mk = lambda r: cubie.make(*[[int(x) for x in part.split(',')] for part in r['leftover(cp;ct;ep;ef)'].split(';')])
    w_corp, k_corp = thirds([(py3.nums(r['skeleton']), mk(r)) for r in lines])
    rnd = random.Random(2026); els = list(T8) + [s for s in py3.table('c', 10) if s not in T8]
    def rseq(n):
        out = []
        while len(out) < n:
            m = rnd.randrange(18)
            if out and (m // 3 == out[-1] // 3 or (m // 6 == out[-1] // 6 and m // 3 < out[-1] // 3)): continue
            out.append(m)
        return out
    w_rand, k_rand = thirds([(rseq(len(r['skeleton'].split())), rnd.choice(els)) for r in lines])
    L = ['| 3c, the best 8-mover insertion is in the | First third | Middle third | Last third | Skeletons tried | Of them with an 8-mover somewhere |', '|---|---:|---:|---:|---:|---:|']
    L.append(f"| real skeletons with their own 3c (counts) | {w_real[0]:.1f} | {w_real[1]:.1f} | {w_real[2]:.1f} | {len(real_items)} | {k_real} |")
    for name, w, k, tried in (('real skeletons with their own 3c', w_real, k_real, len(real_items)), ("of them, DougCube's", w_doug, k_doug, k_doug), ('of them, everybody else\'s', w_rest, k_rest, k_rest),
                              ('the real move sequences with a random 3c', w_corp, k_corp, len(lines)), ('random sequences of the same lengths with a random 3c', w_rand, k_rand, len(lines))):
        L.append(f"| {name} | {num(100 * w[0] / k)} | {num(100 * w[1] / k)} | {num(100 * w[2] / k)} | {tried:,} | {k:,} |")
    write('real_spots', L)
    J['spots'] = {'real': w_real, 'k_real': k_real, 'corpus': [x / k_corp for x in w_corp], 'random': [x / k_rand for x in w_rand]}
    # ---- A6: on how many of the three axes are the edges of a 3e leftover oriented?  All 1,760 edge 3-cycles, by
    #      whether they have a short alg, next to the real 3e skeletons (the leftover as it stands after the skeleton)
    T8e = py3.table('e', 8); rots = {nm: R_ for R_, nm in cubie.rotations()}
    AXROT = [tuple(range(54)), next(R_ for R_, nm in cubie.rotations() if nm == 'y'), next(R_ for R_, nm in cubie.rotations() if nm == 'x')]   # F/B, R/L, U/D
    def axes_oriented(st):
        k = 0
        for Rm in AXROT:
            cp_, ct_, ep_, ef_ = cubie.cubie(cubie.conj(st, Rm)); k += not any(ef_)
        return k
    assert axes_oriented(cube.SOLVED) == 3 and axes_oriented(cube.do(cube.SOLVED, 'F')) == 2 and axes_oriented(cube.do(cube.SOLVED, 'F R')) == 1 and axes_oriented(cube.do(cube.SOLVED, 'F R U')) == 0
    allc = collections.Counter(); six = collections.Counter(); le8 = collections.Counter()
    for e in py3.elements('e'):
        st = cubie.make(*e); k = axes_oriented(st); allc[k] += 1
        algs = T8e.get(st, [])
        six[k] += any(len(a) == 6 for a in algs); le8[k] += bool(algs)
    r3e = [(axes_oriented(cube.do(cube.SOLVED, cube.parse(r['scramble']) + cube.parse(r['reduced']))), r) for r in U if r['type'] == '3e']
    realc = collections.Counter(k for k, r in r3e); real10 = collections.defaultdict(list)
    for k, r in r3e: real10[k].append(r['L10'])
    rand10 = collections.defaultdict(list)                         # random 20-move 3e skeletons of the sample, by the same count
    with open(f'{O}sample_3e_n20.tsv') as f:
        hd = f.readline().rstrip('\n').split('\t'); ia, ib = hd.index('leftover(cp;ct;ep;ef)'), hd.index('L10_one')
        for l in f:
            p = l.rstrip('\n').split('\t'); st = cubie.make(*[[int(x) for x in part.split(',')] for part in p[ia].split(';')])
            rand10[axes_oriented(st)].append(int(p[ib]))
    nr = sum(len(v) for v in rand10.values())
    L = ['| Axes on which the three edges are oriented | Edge 3-cycles | With a 6-move alg | With an alg of 8 moves or fewer | Share with an alg of 8 moves or fewer |', '|---:|---:|---:|---:|---:|']
    K = ['| Axes on which the three edges are oriented | Real 3e skeletons | Their mean added, cap 10 | Random 20-move 3e skeletons | Their mean added, cap 10 |', '|---:|---:|---:|---:|---:|']
    for k in (3, 2, 1, 0):
        L.append(f"| {k} | {allc[k]:,} | {six[k]} | {le8[k]} | {fmt(le8[k], allc[k]) if allc[k] else ''} |")
        K.append(f"| {k} | {realc[k]} | {f2(sum(real10[k]) / len(real10[k])) if real10[k] else ''} | {len(rand10[k]):,} | {f2(sum(rand10[k]) / len(rand10[k]))} |")
    allreal = [x for v in real10.values() for x in v]; allrand = [x for v in rand10.values() for x in v]
    L.append(f"| **all** | **{sum(allc.values()):,}** | **{sum(six.values())}** | **{sum(le8.values())}** | {fmt(sum(le8.values()), sum(allc.values()))} |")
    K.append(f"| **all** | **{sum(realc.values())}** | **{f2(sum(allreal) / len(allreal))}** | **{nr:,}** | **{f2(sum(allrand) / len(allrand))}** |")
    write('real_eo', L); write('real_eo_skeletons', K)
    J['eo'] = {'all': {str(k): allc[k] for k in range(4)}, 'six': {str(k): six[k] for k in range(4)}, 'le8': {str(k): le8[k] for k in range(4)}, 'real': {str(k): realc[k] for k in range(4)},
               'real10': {str(k): (sum(v) / len(v) if v else None) for k, v in real10.items()}, 'rand10': {str(k): sum(v) / len(v) for k, v in rand10.items()}, 'rand_n': {str(k): len(v) for k, v in rand10.items()}}
    json.dump(C, open(O + 'real_corpus.json', 'w'), indent=1)
    json.dump(J, open(O + 'real.json', 'w'), indent=1, default=str)
    json.dump(R, open(O + 'real_rows.json', 'w'))
    print('real.json written:', len(R), 'cases,', len(U), 'skeletons; by type', dict(J['by_type']))
    print('shorter than the best at cap 12:', [(x['id'], x['type'], x['author'], x['best12']) for x in J['shorter12']])
def corpus():
    """The real move sequences with random leftovers: every distinct real skeleton of 10 to 30 moves, repeated (in
    rounds, so that any first k lines hold every sequence equally often), each line with its own random leftover."""
    R = rows(); seqs = sorted({r['reduced'] for r in R if 10 <= r['n'] <= 30})
    for typ, rep in (('3c', 100), ('5c', 50)):
        p = f'{O}corpus_real_{typ}.txt'
        open(p, 'w').write('\n'.join(s for _ in range(rep) for s in seqs) + '\n')
        subprocess.run([exlib.BIN, 'corpus', p, typ, '777', '--L', '8,10', '--two', '10:2000', '--sol-every', '50', '--out', f'{O}corpus_real_{typ}.tsv'], check=True)
        print(typ, len(seqs), 'real sequences x', rep)
if __name__ == '__main__':
    if '--need' in sys.argv: need()
    elif '--corpus' in sys.argv: corpus()
    else: main()
