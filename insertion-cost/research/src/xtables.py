#!/usr/bin/env python3
"""Tables of the insertion-cost report, written to report/data/*.md from the outputs in research/out/.
Nothing here is typed in: every cell is read from a result file (or from the Lean project's README for the
three-comm types).  Run histograms.py and xone.py first; the real-skeleton tables are written by xreal.py."""
import csv, json, re, collections, os, sys, math
import iv
from iv import O, TYPES, CORNER, EDGE, MAIN, SHOW, LONG, NS, ALLN, cell, head, mean, le, pct, fmt, num, f2, f1
D = '/data/fmc/insertion-cost/report/data/'
os.makedirs(D, exist_ok=True)
def write(name, lines):
    open(D + name + '.md', 'w').write('\n'.join(lines) + '\n'); print(name, len(lines), 'lines')
def n_(x): return f'{x:,}'

# ---------------------------------------------------------------- 1. how many 3-cycles each leftover needs
def shape_name(tp, kind='c'):
    """Plain words for a cycle type [(length, twist sum), ...]."""
    piece = 'corner' if kind == 'c' else 'edge'; tw = 'twisted' if kind == 'c' else 'flipped'
    c = collections.Counter((L, bool(t)) for L, t in tp); parts = []
    for (L, t), k in sorted(c.items(), key=lambda kv: (-kv[0][0], kv[0][1])):
        if L == 1: parts.append(f"{['', 'one', 'two', 'three', 'four', 'five'][k]} {piece}{'s' if k > 1 else ''} {tw} in place")
        else:
            what = 'swap' if L == 2 else f'{L}-cycle'
            parts.append((f"{['', 'a', 'two', 'three'][k]} " if k > 1 or not t else 'a ') .replace('a ', 'a ' if not t else f'a {tw} ') + (what + ('s' if k > 1 else '')) if not (k > 1 and t) else f"{['', 'a', 'two', 'three'][k]} {tw} {what}s")
    return ', '.join(parts)
def short_name(tp):
    """The server's shorthand for a corner cycle type, where it has one."""
    c = collections.Counter(L for L, t in tp); tw = sum(1 for L, t in tp if L == 1)
    cyc = sorted((L for L, t in tp if L > 1), reverse=True)
    s = ''.join({7: '7c', 5: '5c', 4: '4c', 3: '3c', 2: '2c'}[L] for L in cyc) + (f'{tw}t' if tw else '')
    return {'3c3c': 'mixed 3c3c', '4t': '4 twisted corners'}.get(s, s) if not (cyc == [3, 3] and tw) else '3c3c1t'
def three_types():
    """The 22 corner types that need exactly three 3-cycles, from the Lean project's README (theorem corner_fewest_up_to_three)."""
    txt = open('/data/fmc/insertion-cost/lean/Insertions/README.md').read()
    row = next(l for l in txt.split('\n') if l.startswith('| `corner_fewest_up_to_three`'))
    part = row.split('Exactly three are needed by 22 types:')[1]
    out = []
    for m in re.finditer(r'`\[((?:\(\d, \d\)(?:, )?)+)\]` ([\d,]+)', part):
        tp = tuple(tuple(map(int, x.split(', '))) for x in re.findall(r'\((\d, \d)\)', m.group(1)))
        out.append((tp, int(m.group(2).replace(',', ''))))
    assert len(out) == 22 and sum(v for _, v in out) == 8845836, (len(out), sum(v for _, v in out))
    return out
def tool_name(tp, kind):
    """The name used here for a cycle type of the Lean statement (which keeps the two twist directions apart)."""
    cyc = sorted(L for L, t in tp if L > 1); fixed = sum(1 for L, t in tp if L == 1); tw = any(t for L, t in tp if L > 1)
    if kind == 'corner':
        return {((3,), 0): '3c', ((5,), 0): '5c', ((3, 3), 0): '3c3c', ((3,), 1): '3c1t', ((2, 2), 0): '2c2c-twisted' if tw else '2c2c-pure', ((), 2): '2tc', ((), 3): '3tc'}[(tuple(cyc), fixed)]
    return {((3,), 0): '3e', ((5,), 0): '5e', ((3, 3), 0): '3e3e', ((3,), 1): '3e1f', ((2, 2), 0): '2e2e-flipped' if tw else '2e2e', ((), 2): '2f'}[(tuple(cyc), fixed)]
def lean_two(kind):
    """{name: (cycle types in the Lean statement, states)} for the products of two 3-cycles (corner_products_of_two,
    edge_products_of_two), from the Lean project's README."""
    txt = open('/data/fmc/insertion-cost/lean/Insertions/README.md').read()
    row = next(l for l in txt.split('\n') if l.startswith(f'| `{kind}_products_of_two`'))
    out = {}
    for m in re.finditer(r'`\[((?:\(\d, \d\)(?:, )?)+)\]` ([\d,]+)', row):
        tp = tuple(tuple(map(int, x.split(', '))) for x in re.findall(r'\((\d, \d)\)', m.group(1)))
        nm = tool_name(tp, kind); k, v = out.get(nm, (0, 0)); out[nm] = (k + 1, v + int(m.group(2).replace(',', '')))
    return out
def t_types():
    T = json.load(open(O + 'types.json'))
    L = ['| Leftover | What is left | States | 3-cycles needed | Types when the two twist directions are counted apart |', '|---|---|---:|---:|---:|']
    for kind, order in (('corner', CORNER), ('edge', EDGE)):
        lt = lean_two(kind); assert set(lt) == set(order), (kind, set(lt) ^ set(order))
        for t in order:
            d = T[kind]['types'][t]; assert lt[t][1] == d['states'], (t, lt[t], d)
            L.append(f"| {SHOW[t]} | {LONG[t]} | {n_(d['states'])} | {d['fewest_3_cycles']} | {lt[t][0]} |")
    write('types', L)
    g = collections.OrderedDict()
    for tp, v in three_types():
        g.setdefault(short_name(tp), [[], 0, 0]); g[short_name(tp)][1] += v; g[short_name(tp)][2] += 1
        if shape_name(tp) not in g[short_name(tp)][0]: g[short_name(tp)][0].append(shape_name(tp))
    L = ['| Leftover | What is left | States | Types when the two twist directions are counted apart |', '|---|---|---:|---:|']
    for nm, (shapes, v, k) in sorted(g.items(), key=lambda kv: -kv[1][1]):
        L.append(f"| {nm} | {'; or '.join(shapes)} | {n_(v)} | {k} |")
    assert sum(k for _, _, k in g.values()) == 22
    L.append(f"| **all {len(g)}** | | **{n_(sum(v for _, v, _ in g.values()))}** | **{sum(k for _, _, k in g.values())}** |")
    write('types_three', L)
    return T

# ---------------------------------------------------------------- 2. optimal algorithm length per type
def alg_summary():
    txt = open(O + 'algs_L12_summary.txt').read().split('\n'); a, b = {}, {}
    blk = 0
    for l in txt[1:]:
        if l.startswith('type\tlength'): blk = 1; continue
        if l.startswith('type\t') or not l.strip() or l.startswith('2c2e, '): continue
        p = l.split('\t')
        if blk == 0: a[p[0]] = (int(p[1]), int(p[2]), {k.strip(): int(v) for k, v in (x.split(':') for x in p[3].split(','))})
        else: b[p[0]] = {int(k): int(v) for k, v in (x.split(':') for x in p[1].split(','))} if len(p) > 1 and p[1].strip() else {}
    return a, b
def t_algs():
    a, b = alg_summary(); cols = [str(k) for k in range(6, 13)] + ['>12']
    L = ['| Leftover | States | ' + ' | '.join(f'{c} moves' if c != '>12' else 'more than 12' for c in cols) + ' |', '|---|---:|' + '---:|' * len(cols)]
    for t in TYPES + ['2c2e']:
        el, cl, d = a[t]
        L.append(f"| {SHOW.get(t, '2c2e')} | {n_(el)} | " + ' | '.join(n_(d[c]) if c in d else '' for c in cols) + ' |')
    write('alg_lengths', L)
    cols = list(range(6, 13))
    L = ['| Leftover | ' + ' | '.join(f'{c} moves' for c in cols) + ' | Up to 8 | Up to 10 | Up to 12 |', '|---|' + '---:|' * (len(cols) + 3)]
    for t in TYPES + ['2c2e']:
        d = b[t]; up = lambda k: n_(sum(v for x, v in d.items() if x <= k)) if any(x <= k for x in d) else '0'
        L.append(f"| {SHOW.get(t, '2c2e')} | " + ' | '.join(n_(d[c]) if c in d else '' for c in cols) + f' | {up(8)} | {up(10)} | {up(12)} |')
    write('alg_counts', L)
def t_classes():
    for t in ('3c', '3e'):
        rows = list(csv.DictReader(open(O + f'cases_{t}_L12.tsv'), delimiter='\t'))
        rows.sort(key=lambda r: (int(r['optimal_length']), -int(r['class_size']), int(r['class'])))
        lens = range(6 if t == '3e' else 8, 13)
        L = ['| Shortest alg, moves | A shortest alg | Pieces (from > to, + twist) | States in the class | ' + ' | '.join(f'{k}-move algs' for k in lens) + ' |', '|---:|---|---|---:|' + '---:|' * len(lens)]
        for r in rows:
            L.append(f"| {r['optimal_length']} | `{r['representative']}` | {r['pieces (from>to+twist)']} | {r['class_size']} | " + ' | '.join(r[f'n{k}'] if r[f'n{k}'] != '0' else '' for k in lens) + ' |')
        write(f'classes_{t}', L)

# ---------------------------------------------------------------- 3. the main cost tables
def cost_cols(typ): return list(range(2, 9)) if typ in ('3c', '3e') else list(range(4, 13))
def cost_rows(typ, L, model, ns, src='sample', first=None):
    out = []
    for n in ns:
        c = cell(typ, n, L, model, src)
        if not c: continue
        none = '0' if c['inf'] == 0 else fmt(c['inf'], c['n'])
        out.append('| ' + ((first + ' | ') if first else '') + f"{n} | {n_(c['n'])} | {f2(mean(c)) if c['n'] > c['inf'] else ''} | " + ' | '.join(pct(c, k) for k in cost_cols(typ)) + f' | {none} |')
    return out
def cost_head(typ, first=None):
    return [('| ' + first + ' ' if first else '') + '| Skeleton length | Skeletons | Mean moves added | ' + ' | '.join(f'Adds {k} or less' for k in cost_cols(typ)) + ' | Nothing fits |',
            ('|---' if first else '') + '|---:|---:|---:|' + '---:|' * (len(cost_cols(typ)) + 1)]
def caps_of(typ):
    """(cap, model, source) blocks shown for a type, in order."""
    if typ in ('3c', '3e'): return [(8, 'one', 'sample'), (10, 'one', 'sample'), (12, 'one', 'sample')]
    return [(8, 'best', 'sample'), (10, 'best', 'sample')]
def t_cost():
    for typ in TYPES:
        L = cost_head(typ, 'Cap')
        for cap, model, src in caps_of(typ): L += cost_rows(typ, cap, model, NS, src, first=str(cap))
        write(f'cost_{typ}', L)
        # appendix: every length, every model
        k = 'c' if typ in CORNER else 'e'
        blocks = [(8, 'one'), (10, 'one'), (12, 'one')] if typ in ('3c', '3e') else [(8, 'two'), (8, 'direct'), (8, 'best'), (10, 'two'), (10, 'direct'), (10, 'best'), (12, 'direct')]
        L = cost_head(typ, 'Cap and model')
        names = {'one': 'one comm', 'two': 'two comms', 'direct': 'one alg', 'best': 'best of the two'}
        for cap, model in blocks:
            c20 = cell(typ, 20, cap, model)
            if not c20 or c20['inf'] == c20['n']: continue
            L += cost_rows(typ, cap, model, ALLN, first=f'{cap}, {names[model]}')
        write(f'app_cost_{typ}', L)

# ---------------------------------------------------------------- 4. the cap, at skeleton length 20
def paired(typ):
    """Per skeleton of the n = 20 cell: best cost at cap 8, cap 10, cap 10 with `mixed`, cap 12 (None where not computed)."""
    def load(pre):
        p = f'{O}{pre}_{typ}_n20.tsv'
        if not os.path.exists(p): return {}
        with open(p) as f:
            head_ = f.readline().rstrip('\n').split('\t'); col = {h: i for i, h in enumerate(head_)}
            return {int(x[0]): {h: x[i] for h, i in col.items() if h.endswith(('_best', '_one', '_two', '_direct', '_mixed', '_two_flat', '_two_apart'))} for x in (l.rstrip('\n').split('\t') for l in f)}
    s, m, t = load('sample'), load('mixed'), load('two12'); out = []
    v = lambda d, k: None if d is None or d.get(k) in (None, 'nc', 'na', 'inf') else int(d[k])
    for idx in sorted(s):
        out.append({'8': v(s[idx], 'L8_best'), '10': v(s[idx], 'L10_best'), '10m': v(m.get(idx), 'L10_best'), '12': v(t.get(idx), 'L12_best') if typ not in ('3c', '3e') else v(s[idx], 'L12_best'),
                    '8inf': s[idx]['L8_best'] == 'inf'})
    return out
def t_caps():
    L = ['| Leftover | Cap 8: something fits on | Cap 8: mean added where something fits | Skeletons (cap 8) | Cap 10: mean added | Skeletons (cap 10) | Cap 10, a comm plus an alg: mean added | Skeletons (comm plus alg) | Cap 12: mean added | Skeletons (cap 12) |', '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    P = ['| Leftover | Skeletons | Cap 8: mean added where something fits | Nothing fits at cap 8 | Cap 10: mean added | Cap 10, a comm plus an alg: mean added | Cap 12: mean added |', '|---|---:|---:|---:|---:|---:|---:|']
    for typ in TYPES:
        h = head(typ); row = [SHOW[typ]]
        for cap, src in ((8, 'sample'), (10, 'sample'), (10, 'mixed'), (12, 'two12' if typ not in ('3c', '3e') else 'sample')):
            c = cell(typ, 20, cap, h, src) if not (src == 'mixed') else cell(typ, 20, cap, 'best', src)
            if cap == 8: row += ['every one' if c['inf'] == 0 else fmt(c['n'] - c['inf'], c['n'])]
            elif c: assert c['inf'] == 0, (typ, cap, src, 'a skeleton where nothing fits at this cap')
            row += [f2(mean(c)), n_(c['n'])] if c else ['not run', 'not run']
        L.append('| ' + ' | '.join(row) + ' |')
        pr = paired(typ); common = [r for r in pr if r['10'] is not None and r['10m'] is not None and r['12'] is not None]
        if common:
            ok8 = [r for r in common if r['8'] is not None]
            m = lambda k, rows=common: f2(sum(r[k] for r in rows) / len(rows))
            P.append(f"| {SHOW[typ]} | {len(common)} | {m('8', ok8)} | {len(common) - len(ok8)} | {m('10')} | {m('10m')} | {m('12')} |")
    write('caps', L); write('caps_paired', P)
    # one alg for the whole leftover, next to two 8-move comms on the skeletons where that alg fits
    T = {k: [f'| Leftover | Skeletons | Alg of {c} or less: fits somewhere | Alg of {c} or less: mean added | Two 8-move comms on the skeletons where an alg of {c} or less fits: mean added | Of those skeletons, two 8-move comms fit on |', '|---|---:|---:|---:|---:|---|'] for k, c in ((1, 10), (2, 12))}
    for typ in TYPES:
        if typ in ('3c', '3e'): continue
        rows = [r for r in sample_cols(typ, 20, ['L8_two', 'L10_direct', 'L12_direct']) if r[0] not in ('nc', 'na')]
        for k in (1, 2):
            cells = [SHOW[typ], n_(len(rows))]
            fit = [r for r in rows if r[k] not in ('inf', 'nc', 'na')]
            if not fit: cells += ['0', '', '', '']
            else:
                two = [int(r[0]) for r in fit if r[0] != 'inf']
                cells += [fmt(len(fit), len(rows)), f2(sum(int(r[k]) for r in fit) / len(fit)), f2(sum(two) / len(two)) if two else 'two 8-move comms never fit',
                          'all of them' if len(two) == len(fit) else f'{len(two):,}']
            T[k].append('| ' + ' | '.join(cells) + ' |')
    write('direct', T[1]); write('direct_12', T[2])
    # nesting, cap 8, the types that two comms solve
    L = ['| Leftover | Skeletons in the sample | Of them, all three ways have a solution | Nesting allowed: mean added | No nesting: mean added | The two not touching: mean added | Best needs nesting |', '|---|---:|---:|---:|---:|---:|---:|']
    for typ in TYPES:
        if typ in ('3c', '3e'): continue
        rows = []; tot = 0
        p = f'{O}sample_{typ}_n20.tsv'
        with open(p) as f:
            hd = f.readline().rstrip('\n').split('\t'); col = {h: i for i, h in enumerate(hd)}
            for l in f:
                x = l.rstrip('\n').split('\t')
                if x[col['L8_two']] in ('nc', 'na'): continue
                tot += 1
                if x[col['L8_two']] == 'inf' or x[col['L8_two_flat']] == 'inf' or x[col['L8_two_apart']] == 'inf': continue
                rows.append((int(x[col['L8_two']]), int(x[col['L8_two_flat']]), int(x[col['L8_two_apart']])))
        if not rows: continue
        nn = len(rows); nest = sum(1 for r in rows if r[1] > r[0])
        L.append(f"| {SHOW[typ]} | {n_(tot)} | {n_(nn)} | {f2(sum(r[0] for r in rows) / nn)} | {f2(sum(r[1] for r in rows) / nn)} | {f2(sum(r[2] for r in rows) / nn)} | {fmt(nest, nn)} |")
    write('nesting', L)

# ---------------------------------------------------------------- 5. one 3c comm: where, how much, which length
def onepos(n):
    """[(costs at cap 8, cap 9, cap 10)] per skeleton; each a list over the positions 0..n, None where nothing fits."""
    out = []
    with open(f'{O}onepos_3c_n{n}.tsv') as f:
        f.readline()
        for l in f:
            p = l.rstrip('\n').split('\t')
            out.append(tuple([None if x == 'x' else int(x) for x in part.split(',')] for part in p[1:4]))
    return out
def mn(v):
    w = [x for x in v if x is not None]; return min(w) if w else None
def sample_cols(typ, n, cols, pre='sample'):
    with open(f'{O}{pre}_{typ}_n{n}.tsv') as f:
        hd = f.readline().rstrip('\n').split('\t'); ix = [hd.index(c) for c in cols]
        return [[l.rstrip('\n').split('\t')[i] for i in ix] for l in f]
def third(i, n): return min(2, 3 * i // (n + 1))
def t_one():
    A = ['| Skeleton length | No 8-mover fits | 8-0 | 8-1 | 8-2 | 8-3 | 8-4 | 8-5 | 8-6 or more |', '|---:|' + '---:|' * 8]
    B = ['| Skeleton length | An 8-mover is as good as anything up to 10 | A 9-mover beats every 8-mover and no 10-mover beats it | A 10-mover beats every 8- and 9-mover | No alg of up to 10 moves fits | When a 10-mover beats every 8- and 9-mover: by one move only | An 11- or 12-mover beats everything up to 10 | Skeletons where an 8-mover fits | Mean added on those skeletons, cap 8 | Same skeletons, cap 9: mean added | Same skeletons, cap 10: mean added | Same skeletons, cap 12: mean added |', '|---:|' + '---:|' * 11]
    C = ['| Skeleton length | Cap 8: first third | Cap 8: middle third | Cap 8: last third | Cap 10: first third | Cap 10: middle third | Cap 10: last third |', '|---:|' + '---:|' * 6]
    S = ['| Skeleton length | Every other move finds the best | Every other move: mean loss, moves | All misses of every other move: next to two opposite-face moves | Every third move finds the best | Every third move: mean loss, moves |', '|---:|---:|---:|---:|---:|---:|']
    SG = ['| Skeleton length | Best is 8-3 or better: every other move finds it | Best is 8-3 or better: every third move finds it | Best is 8-3 or better and every other move missed it: walks | Of those, the best was 8-3 | Of those, the best was 8-4 | Of those, next to two opposite-face moves |', '|---:|---:|---:|---:|---:|---:|---:|']
    for n in NS:
        P = onepos(n); N = len(P)
        m8 = [mn(p[0]) for p in P]; m9 = [mn(p[1]) for p in P]; m10 = [mn(p[2]) for p in P]
        m12 = [None if x[0] == 'inf' else int(x[0]) for x in sample_cols('3c', n, ['L12_one'])]
        c = collections.Counter('none' if v is None else min(8 - v, 6) for v in m8)
        A.append(f"| {n} | {fmt(c['none'], N)} | " + ' | '.join(fmt(c[k], N) for k in range(0, 7)) + ' |')
        lt = lambda a, b: (b is not None) and (a is None or b < a)
        assert None not in m12, (n, 'a 3c skeleton where no alg of up to 12 moves fits anywhere')
        k0 = sum(1 for a in m10 if a is None)                                                # nothing up to 10 fits anywhere
        k8 = sum(1 for a, b in zip(m8, m10) if a is not None and a == b)                     # an 8-mover gives the best up to 10
        k10 = sum(lt(a, b) for a, b in zip(m9, m10))                                         # only a 10-mover does
        k9 = sum(1 for a, b, c in zip(m8, m9, m10) if lt(a, b) and b == c)                   # a 9-mover does, no 8-mover
        assert k8 + k9 + k10 + k0 == N, (n, k8, k9, k10, k0)
        fit = [i for i, a in enumerate(m8) if a is not None]
        av = lambda v: f2(sum(v[i] for i in fit) / len(fit))
        B.append(f"| {n} | {fmt(k8, N)} | {fmt(k9, N)} | {fmt(k10, N)} | {'0' if not k0 else fmt(k0, N)} | {fmt(sum(1 for a, b in zip(m9, m10) if a is not None and a - b == 1), k10)} | {fmt(sum(lt(a, b) for a, b in zip(m10, m12)), N)} | "
                 f"{len(fit):,} | {av(m8)} | {av(m9)} | {av(m10)} | {av(m12)} |")
        row = [str(n)]
        for k in (0, 2):
            w = [0.0, 0.0, 0.0]; tot = 0
            for p in P:
                b = mn(p[k])
                if b is None: continue
                pos = [i for i, v in enumerate(p[k]) if v == b]
                for i in pos: w[third(i, n)] += 1 / len(pos)
                tot += 1
            row += [num(100 * x / tot) for x in w]
        if (n + 1) % 3 == 0: C.append('| ' + ' | '.join(row) + ' |')
        SK = [x[0].split() for x in sample_cols('3c', n, ['skeleton'])]
        axis = lambda m: 'UDRLFB'.index(m[0]) // 2
        def skip(step):
            """Checking the spots i = par (mod step) and both ends, for every par.  Only skeletons with an 8-mover
            somewhere are counted; a set of spots with no 8-mover at all is scored as an 8-0 (+8)."""
            found = 0; loss = 0.0; good = goodfound = 0; missed = collections.Counter(); tot = 0; near = 0; nearall = 0
            for idx, p in enumerate(P):
                b = mn(p[0])
                if b is None: continue
                for par in range(step):
                    sub = mn([v for i, v in enumerate(p[0]) if i % step == par or i in (0, n)])
                    tot += 1; hit = sub == b; found += hit; loss += (sub - b) if sub is not None else (8 - b)
                    if b <= 5: good += 1; goodfound += hit
                    if not hit:
                        s_ = SK[idx]
                        nr = any((i >= 2 and axis(s_[i - 1]) == axis(s_[i - 2])) or (i <= n - 2 and axis(s_[i]) == axis(s_[i + 1])) for i, v in enumerate(p[0]) if v == b)
                        nearall += nr
                        if b <= 5: missed[8 - b] += 1; near += nr
            return found, loss, good, goodfound, missed, tot, near, nearall
        f2_, l2, g2, gf2, ms2, t2, nr2, na2 = skip(2); f3, l3, g3, gf3, ms3, t3, nr3, na3 = skip(3)
        S.append(f"| {n} | {fmt(f2_, t2)} | {f2(l2 / t2)} | {fmt(na2, t2 - f2_)} | {fmt(f3, t3)} | {f2(l3 / t3)} |")
        assert set(ms2) <= {3, 4}, (n, ms2)
        SG.append(f"| {n} | {fmt(gf2, g2)} | {fmt(gf3, g3)} | {sum(ms2.values())} | {ms2[3]} | {ms2[4]} | {nr2} |")
    write('one_cancel', A); write('one_longer', B); write('one_thirds', C); write('one_skip', S); write('one_skip_good', SG)
    # going three spots on, not two, after a spot whose case has a shortest alg of 10 moves (paulduc03's question)
    Q = ['| Skeleton length | Spots whose case needs a 10-mover | An 8-3 or better at the next spot | An 8-3 or better two spots on |', '|---:|---:|---:|---:|']
    QW = ['| Skeleton length | Walks on skeletons with a best of 8-3 or better | Every other move misses it: walks | Every other move misses it: share | Three spots on after a 10-move case misses it: walks | Three spots on after a 10-move case misses it: share |', '|---:|---:|---:|---:|---:|---:|']
    TS = {}
    for n in NS:
        P = onepos(n); ten = nxt = two = 0; good = plain = rule = 0
        for p in P:
            c8, c9, c10 = p
            for i in range(n - 1):                                        # spots that have two more spots after them
                if c8[i] is None and c9[i] is None and c10[i] is not None:
                    ten += 1
                    nxt += c8[i + 1] is not None and c8[i + 1] <= 5; two += c8[i + 2] is not None and c8[i + 2] <= 5
            b = mn(c8)
            if b is None or b > 5: continue
            for par in (0, 1):
                good += 1
                plain += mn([v for i, v in enumerate(c8) if i % 2 == par or i in (0, n)]) != b
                seen = {0, n}; i = par
                while i <= n:
                    seen.add(i); i += 3 if (c8[i] is None and c9[i] is None and c10[i] is not None) else 2
                rule += mn([c8[i] for i in sorted(seen)]) != b
        TS[n] = {'ten': ten, 'next': nxt, 'two': two, 'walks': good, 'plain_miss': plain, 'rule_miss': rule}
        Q.append(f'| {n} | {ten:,} | {fmt(nxt, ten)} | {fmt(two, ten)} |')
        QW.append(f'| {n} | {good:,} | {plain:,} | {fmt(plain, good)} | {rule:,} | {fmt(rule, good)} |')
    write('ten_skip', Q); write('ten_skip_walks', QW); json.dump(TS, open(O + 'ten_skip.json', 'w'), indent=1)
    # position by position, skeletons of 20 moves, cap 8
    P = onepos(20); n = 20; N = len(P)
    groups = [('before the first move', [0]), ('after move 1', [1]), ('after move 2', [2]), ('after moves 3 to 17 (each)', list(range(3, 18))), ('after move 18', [18]), ('after move 19', [19]), ('after the last move', [20])]
    L = ['| Position | An 8-mover fits there | Mean added when one fits | It is 8-3 or better | A best insertion of the skeleton is there |', '|---|---:|---:|---:|---:|']
    for name, pos in groups:
        fit = add = good = best = 0
        for p in P:
            b = mn(p[0])
            for i in pos:
                v = p[0][i]
                if v is not None: fit += 1; add += v; good += v <= 5
                if b is not None and v == b: best += 1
        k = N * len(pos)
        L.append(f'| {name} | {fmt(fit, k)} | {f2(add / fit)} | {fmt(good, k)} | {fmt(best, k)} |')
    write('one_positions', L)

# ---------------------------------------------------------------- 6. exchange rates between types
OTHERS = ['2tc', '3tc', '2c2c-pure', '2c2c-twisted', '3c1t', '5c']
def mean_at(typ, n, L):
    """Mean added moves (over the skeletons where something fits) at a whole length, from that length's own sample;
    at a length between two whole ones, the two neighbours mixed (only used to read off a crossing)."""
    lo = int(math.floor(n + 1e-9)); a = iv.cell_at(typ, lo, L)
    if abs(n - lo) < 1e-9: return mean(a) if a else None
    b = iv.cell_at(typ, lo + 1, L)
    if not a or not b: return None
    w = n - lo; return (1 - w) * mean(a) + w * mean(b)
def equal_mean(typ, L, n3):
    """The length at which a `typ` skeleton has the same expected total as a 3c skeleton of n3 moves."""
    want = n3 + mean_at('3c', n3, L); prev = None
    for k in range(100, 301):
        m = k / 10; v = mean_at(typ, m, L)
        if v is None: continue
        if prev and prev[1] <= want <= m + v: return prev[0] + (want - prev[1]) / (m + v - prev[1]) * (m - prev[0])
        prev = (m, m + v)
    return None
def t_exchange():
    for L in (8, 10):
        rows = ['| Target | 3c skeleton of | Chance of the target | ' + ' | '.join(f'{SHOW[t]} shorter by' for t in OTHERS) + ' |', '|---:|---:|---:|' + '---:|' * len(OTHERS)]
        for T in (22, 24, 26, 28, 30, 32):
            for n in range(T - 8, T - 2):
                if n < 12 or n > 30: continue
                p = iv.chance('3c', n, L, T)
                if p is None or p < 0.02 or p > 0.98: continue
                cells = []
                for t in OTHERS:
                    m = iv.equal_length(t, L, T, p)
                    cells.append(f1(n - m) if m is not None else '')
                rows.append(f'| {T} or less | {n} | {num(100 * p)} | ' + ' | '.join(cells) + ' |')
        write(f'exchange_cap{L}', rows)
    rows = ['| 3c skeleton of | Its expected total where an 8-mover fits | ' + ' | '.join(f'{SHOW[t]} shorter by' for t in OTHERS) + ' |', '|---:|---:|' + '---:|' * len(OTHERS)]
    for n in (16, 18, 20, 22, 24, 26, 28):
        cells = []
        for t in OTHERS:
            m = equal_mean(t, 8, n); cells.append(f1(n - m) if m is not None else '')
        rows.append(f"| {n} | {f1(n + mean_at('3c', n, 8))} | " + ' | '.join(cells) + ' |')
    write('exchange_mean', rows)
    # the chance of a total, by type and length: cap 8
    for T in (24, 26, 28, 30):
        rows = ['| Skeleton length | ' + ' | '.join(SHOW[t] for t in ['3c'] + OTHERS) + ' |', '|---:|' + '---:|' * (1 + len(OTHERS))]
        for n in range(12, 27):
            if T - n > 13 or T - n < 1: continue
            cs = []
            for t in ['3c'] + OTHERS:
                p = iv.chance(t, n, 8, T); cs.append('' if p is None else ('0' if p == 0 else num(100 * p)))
            rows.append(f'| {n} | ' + ' | '.join(cs) + ' |')
        write(f'chance_{T}', rows)

# ---------------------------------------------------------------- 8. Insertion Finder's pages
def t_if():
    rows = list(csv.reader(open(O + 'if_compare.tsv'), delimiter='\t')); hd = rows[0]
    cases = {l.split('\t')[2]: l.rstrip('\n').split('\t') for l in open(O + 'if_cases.tsv')}
    L = ['| Insertion Finder page | Skeleton | Insertion Finder, moves | This search, cap 8, moves | Cap 10, moves | Cap 12, moves |', '|---|---|---:|---:|---:|---:|']
    H = ['| Insertion Finder page | Cap 8: what was inserted | Cap 10: what was inserted | Cap 12: what was inserted |', '|---|---|---|---|']
    N = ['| Insertion Finder page | Skeleton | Insertion Finder, moves | Why it is not compared |', '|---|---|---:|---|']
    for r in rows[1:]:
        d = dict(zip(hd, r)); url = cases[d['page']][6]
        if d['L8 best'] == '-':
            why = 'a parity leftover (two corners and two edges)' if d['our type'] == '2c2e' else 'corners and edges both left'
            N.append(f"| [{d['IF says']}]({url}) | {d['skeleton length']} moves | {d['IF length']} | {why} |"); continue
        def best(Lc):
            b = d[f'L{Lc} best']; which = [m for m in ('direct', 'two', 'mixed') if d[f'L{Lc} {m}'].rstrip('n') == b]
            name = {'direct': 'one alg', 'two': 'two comms', 'mixed': 'a comm plus an alg'}[which[0]]
            return b, name
        L.append(f"| [{d['IF says']}]({url}) | {d['skeleton length']} moves | {d['IF length']} | {best(8)[0]} | {best(10)[0]} | {best(12)[0]} |")
        H.append(f"| {d['IF says']} | {best(8)[1]} | {best(10)[1]} | {best(12)[1]} |")
    write('if_pages', L); write('if_pages_how', H); write('if_pages_not', N)

# ---------------------------------------------------------------- the estimates people gave, next to the computed means
EST = [  # leftover, the tutorial's table, what was posted (who, figure)
    ('3c', '5/6', 'Baiqiang 5-6; Aneurin 6; Eli Rogers ~ +6'),
    ('2tc', '8', 'Phuwish ~8.0'),
    ('3tc', '9', 'Phuwish mid to high 8'),
    ('2c2c-pure', '9/10', 'cpaul 9 (pure); tave_789 asked whether a 2c2c is close to 9.5, Phuwish: yeah; Baiqiang 6-8 for a good 2c2c and 8-9 for a bad one, without saying which kind is which'),
    ('2c2c-twisted', 'not a row of the table', 'cpaul 9.5 (with a twist); tave_789 and Phuwish as above; Baiqiang as above'),
    ('3c1t', '10', 'cpaul 10; tave_789 asked whether a 3c1t is close to 9.5, Phuwish: yeah; Baiqiang 8-9'),
    ('5c', '10/11', 'Phuwish ~high 10; Aneurin 10-11'),
]
def t_estimates():
    """Each computed cell carries the number of skeletons behind it."""
    L = ['| Leftover | The tutorial\'s table | Posted on the server | Random, 16 moves, cap 8: mean added | Random, 20 moves, cap 8: mean added | Random, 20 moves, cap 10: mean added | Random, 20 moves, cap 12: mean added |', '|---|---:|---|---:|---:|---:|---:|']
    K = ['| Leftover | 16 moves, cap 8: skeletons | 16 moves, cap 8: something fits on | 20 moves, cap 8: skeletons | 20 moves, cap 10: skeletons | 20 moves, cap 12: skeletons |', '|---|---:|---:|---:|---:|---:|']
    def c_(typ, n, cap, src='sample'): return cell(typ, n, cap, head(typ), src)
    def m(c): return f2(mean(c)) if c else 'not run'
    def k(c): return n_(c['n']) if c else 'not run'
    def fits(c):
        assert c['inf'] == 0 or c['inf'] > c['n'] * 0.005, c
        return fmt(c['n'] - c['inf'], c['n']) if c['inf'] else 'every one'
    for typ, tr, posted in EST:
        cs = [c_(typ, 16, 8), c_(typ, 20, 8), c_(typ, 20, 10), c_(typ, 20, 12, 'sample' if typ == '3c' else 'two12')]
        assert all(c['inf'] <= c['n'] * 0.005 for c in cs[1:] if c), typ     # only the 16-move cell ever showed a share
        L.append(f"| {SHOW[typ]} | {tr} | {posted} | " + ' | '.join(m(c) for c in cs) + ' |')
        K.append(f"| {SHOW[typ]} | {k(cs[0])} | {fits(cs[0])} | " + ' | '.join(k(c) for c in cs[1:]) + ' |')
    write('estimates', L); write('estimates_n', K)
THRESH = [  # who, what was said, type, length, target
    ('the tutorial', '3c in 23: "you will probably get it" (sub-30)', '3c', 23, 29),
    ('the tutorial', '3c in 25: "you will need some luck" (sub-30)', '3c', 25, 29),
    ('sequesteredcuber', 'sub-22 for a 3c skeleton (sub-30)', '3c', 21, 29),
    ('sequesteredcuber', 'sub-20 for every other skeleton (sub-30): a 5c', '5c', 19, 29),
    ('sequesteredcuber', 'sub-20 for every other skeleton (sub-30): a 3c1t', '3c1t', 19, 29),
    ('sequesteredcuber', 'sub-20 for every other skeleton (sub-30): a pure 2c2c', '2c2c-pure', 19, 29),
    ('Gezza Cubing', '3c in 22 (sub-30)', '3c', 22, 29),
    ('Gezza Cubing, oliynykmax', '3c in 24 (sub-30)', '3c', 24, 29),
    ('Gezza Cubing', '5c in 16 (sub-30)', '5c', 16, 29),
    ('Gezza Cubing, oliynykmax', '5c in 18 (sub-30)', '5c', 18, 29),
    ('oliynykmax', '3c1t in 18 (sub-30)', '3c1t', 18, 29),
    ('trangium', '3c in 28 (sub-35)', '3c', 28, 34),
    ('trangium', '5c in 22 (sub-35)', '5c', 22, 34),
    ('trangium', '3c1t in 22 (sub-35)', '3c1t', 22, 34),
]
def t_thresholds():
    L = ['| Who | Skeleton and goal | Chance of the goal | Expected total where something fits |', '|---|---|---:|---:|']
    for who, said, typ, n, T in THRESH:
        L.append(f"| {who} | {said} | {num(100 * iv.chance(typ, n, 8, T))} | {f1(n + mean_at(typ, n, 8))} |")
    write('thresholds', L)
# ---------------------------------------------------------------- the tutorial's table, line by line
TRONTO = [('Corner 3-cycle', '5/6', '3c'), ('Edge 3-cycle', '7', '3e'), ('2 Twisted Corners (2 comms)', '8', '2tc'), ('3 Twisted Corners (2 comms)', '9', '3tc'),
          ('4 Corners (double swap)', '9/10', '2c2c-pure'), ('the twisted double swap (not a row of the table)', '', '2c2c-twisted'),
          ('4 Corners (3 + 1 twisted)', '10', '3c1t'), ('Corner 5-cycle', '10/11', '5c'), ('2 Corners and 2 Edges (double 2-cycle)', '10', None)]
def t_tronto():
    real = json.load(open(O + 'real_rows.json')) if os.path.exists(O + 'real_rows.json') else []
    L = ['| Row of the tutorial\'s table | Tutorial | Random skeletons of 16 moves, cap 8: mean added (skeletons) | Random, 20 moves, cap 8 | Random, 20 moves, cap 10 | Random, 20 moves, cap 12 | Posted skeletons, cap 8: mean added (skeletons, their mean length) |', '|---|---:|---:|---:|---:|---:|---:|']
    for name, val, typ in TRONTO:
        if typ is None:
            L.append(f'| {name} | {val} | not sampled | not sampled | not sampled | not sampled | not sampled |'); continue
        h = head(typ)
        def m(n, cap, src='sample'):
            c = cell(typ, n, cap, h, src)
            if not c: return 'not run'
            return f2(mean(c)) + (f" ({n_(c['n'])}; fits on {fmt(c['n'] - c['inf'], c['n'])})" if c['inf'] > c['n'] * 0.005 else f" ({n_(c['n'])})")
        rs = [r for r in real if r['type'] == typ and not r['dup_of']]; ok = [r for r in rs if r['L8'] is not None]
        posted = (f"{sum(r['L8'] for r in ok) / len(ok):.2f} ({len(ok)}" + (f' of {len(rs)} where something fits' if len(ok) != len(rs) else '') + f", {sum(r['n'] for r in ok) / len(ok):.1f} moves)") if ok else 'none posted'
        L.append(f"| {name} | {val} | {m(16, 8)} | {m(20, 8)} | {m(20, 10)} | {m(20, 12, 'sample' if typ in ('3c', '3e') else 'two12')} | {posted} |")
    write('tronto', L)

if __name__ == '__main__':
    t_types(); t_algs(); t_classes(); t_cost(); t_caps(); t_one(); t_exchange(); t_if(); t_estimates(); t_thresholds(); t_tronto()
