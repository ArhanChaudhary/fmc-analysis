#!/usr/bin/env python3
"""Tables of the DR-xs report, written to report/data/*.md from the outputs in research/out/."""
import csv, json, collections, os, sys
import xv
from xv import fmt, num, pct, avg, share, hu, CS_ORDER, O
D = '/data/fmc/is-dr-xs-worth-it/report/data/'
os.makedirs(D, exist_ok=True)
def write(name, lines):
    open(D + name + '.md', 'w').write('\n'.join(lines) + '\n'); print(name, len(lines), 'lines')
def kinds(): return list(csv.DictReader(open(O + 'kinds.tsv'), delimiter='\t'))
def rng(xs): xs = sorted(set(xs)); return str(xs[0]) if len(xs) == 1 else f'{xs[0]}–{xs[-1]}'
def lst(xs): xs = sorted(set(xs)); return ', '.join(map(str, xs[:-1])) + (' or ' if len(xs) > 1 else '') + str(xs[-1])

def t_kinds():
    K = kinds(); g = collections.defaultdict(list)
    for r in K: g[(int(r['slices']), r['faces'] == 'UD', r['slice_bit'] == '1')].append(r)
    L = ['| Slices needed | Corners oriented on | Slice edges against the centers | Possible numbers of flipped edges | Kinds of state | Turns to a real DR, fewest–most |', '|---:|---|---|---|---:|---|']
    for (s, own, bit) in sorted(g):
        rows = g[(s, own, bit)]
        L.append(f"| {s} | {'the faces of their own colour' if own else 'two other faces'} | {'agree' if bit else 'disagree'} | {lst(int(r['flips']) for r in rows)} | {len(rows)} | {rng(int(r['turns_to_dr']) for r in rows)} |")
    L.append(f'| all | | | | **{len(K)}** | |')
    write('kinds', L)

def t_fix():
    # transposed: one row per number of turns, one column per number of slices (a 12-column table otherwise)
    K = kinds(); by = {s: [int(r['turns_to_dr']) for r in K if int(r['slices']) == s] for s in (1, 2, 3)}
    c = {s: collections.Counter(v) for s, v in by.items()}
    L = ['| Turns to a real DR | Kinds of DR-1s state | Kinds of DR-2s state | Kinds of DR-3s state |', '|---:|---:|---:|---:|']
    for t in range(2, 11): L.append(f'| {t} | ' + ' | '.join(str(c[s][t]) for s in (1, 2, 3)) + ' |')
    L.append('| all | ' + ' | '.join(str(len(by[s])) for s in (1, 2, 3)) + ' |')
    L.append('| average turns | ' + ' | '.join(f'{hu(sum(by[s]) / len(by[s]), 2):.2f}' for s in (1, 2, 3)) + ' |')
    write('fix_turns', L)
    # the steps in between, one row per number of turns, one column per step; from scratch, then right after a trigger
    S = json.load(open(O + 'festeps.json'))
    steps = [('DR-3s to DR-2s', 'DR-3s -> DR-2s (or better)'), ('DR-2s to DR-1s', 'DR-2s -> DR-1s (or better)'), ('DR-1s to DR', 'DR-1s -> DR'), ('DR-2s to DR', 'DR-2s -> DR')]
    for which, title, first in (('scratch', 'steps_scratch', 'Turns, counted from scratch'), ('after_quarter_better', 'steps_trigger', 'Extra turns right after a trigger, at best')):
        hs = [{int(k): v for k, v in S[key][which].items()} for _, key in steps]
        L = [f'| {first} | ' + ' | '.join(nm for nm, _ in steps) + ' |', '|---:|' + '---:|' * len(steps)]
        for t in sorted(set().union(*hs)): L.append(f'| {t} | ' + ' | '.join(str(h.get(t, 0)) for h in hs) + ' |')
        if which == 'scratch': L.append('| all kinds | ' + ' | '.join(str(S[key]['kinds']) for _, key in steps) + ' |')
        write(title, L)
    # DR-1s by where the four flipped edges sit, for corners on F/B (the fixing slice is R L)
    import fe
    pl = [p for p in fe.EDGES if p[2] != 0]
    def name(p): return ''.join(ch for ch, (a, sg) in (('U', (1, 1)), ('D', (1, -1)), ('F', (2, 1)), ('B', (2, -1)), ('R', (0, 1)), ('L', (0, -1))) if p[a] == sg)
    g = collections.defaultdict(list)
    for r in K:
        if r['slices'] != '1' or r['faces'] != 'FB': continue
        inside = sum(1 for p, b in zip(pl, r['flip_places']) if b == '1' and p[0] == 0)
        g[inside].append((int(r['turns_to_dr']), ' '.join(name(p) for p, b in zip(pl, r['flip_places']) if b == '1'), r['fix']))
    T = range(2, 7)
    L = ['| Flipped edges already in the slice that fixes | Layouts | Layouts that take 2 turns | 3 turns | 4 turns | 5 turns | 6 turns |', '|---:|---:|' + '---:|' * len(T)]
    for k in (4, 3, 2, 1, 0):
        c = collections.Counter(t for t, _, _ in g[k])
        L.append(f"| {k} | {len(g[k])} | " + ' | '.join(str(c[t]) for t in T) + ' |')
    write('dr1s_layouts', L)
    L = ['| Flipped edges already in the slice that fixes | Shortest example: flipped edges at | Its fix |', '|---:|---|---|']
    for k in (4, 3, 2, 1, 0):
        ex = min(g[k]); L.append(f"| {k} | {ex[1]} | `{ex[2]}` |")
    write('dr1s_examples', L)

def t_finish():
    TR1 = {'4a1': '14.8', '4b2': '14.9', '4a2': '15.6', '4c3': '15.7', '2c3': '15.2', '2c4': '15.5'}
    TR8 = {'4a1': '13.26', '4b2': '13.59', '2c3': '13.80', '4c3': '14.54', '2c4': '14.80'}
    have8 = os.path.exists(O + 'sample8fe.tsv') and os.path.getsize(O + 'sample8fe.tsv') > 100
    # two tables, DR-1s and DR-2s 8fe, so neither is wider than seven columns
    L = ['| Corner subset | Share of states | DR: average finish, moves | DR-1s: average finish, moves | DR-1s minus DR, moves | trangium\'s DR-1s, nissy optimal average |', '|---|---:|---:|---:|---:|---:|']
    L8 = ['| Corner subset | DR-2s 8fe: average finish, moves | 8fe minus DR, moves | trangium\'s 8fe, nissy optimal average |', '|---|---:|---:|---:|']
    for cs in CS_ORDER + [None]:
        d, h = xv.dr(cs), xv.one_s(cs); e = xv.eight(cs) if have8 else None
        L.append(f"| {cs or '**all**'} | {num(100 * sum(d) / sum(xv.dr())) if cs else '100%'} | {hu(avg(d), 2):.2f} | {hu(avg(h), 2):.2f} | +{hu(avg(h) - avg(d), 2):.2f} | {TR1.get(cs, '')} |")
        L8.append(f"| {cs or '**all**'} | " + (f"{hu(avg(e), 2):.2f} | +{hu(avg(e) - avg(d), 2):.2f}" if e and sum(e) else ' | ') + f" | {TR8.get(cs, '')} |")
    write('finish_subset', L); write('finish_subset_8fe', L8)
    # transposed: one row per finish length, one column per kind of state (an 11-column table otherwise)
    T = range(10, 19)
    rows = [('DR', xv.dr()), ('DR-1s', xv.one_s()), ('DR-1s that one slice turn fixes', xv.one_s(turns=(2,))), ('DR-1s that needs 5 or 6 turns to DR', xv.one_s(turns=(5, 6)))]
    if have8: rows.insert(1, ('DR-2s 8fe', xv.eight()))
    def spct(h, t, sampled=False):
        v = pct(h, t); return f'0 of {sum(h):,}' if v == '0' and sampled else v
    L = ['| Finish in, moves | ' + ' | '.join(nm for nm, _ in rows) + ' |', '|---|' + '---:|' * len(rows)]
    for t in T: L.append(f'| {t} or less | ' + ' | '.join(spct(h, t, nm != 'DR') for nm, h in rows) + ' |')
    L.append('| average finish, moves | ' + ' | '.join(f'{hu(avg(h), 2):.2f}' for _, h in rows) + ' |')
    write('finish_odds', L)
    # solution length: route length + finish; split in two by solution length so each table stays narrow
    def row(L, nm, h, length, N): L.append(f'| {nm} | ' + ' | '.join(spct(h, n - length, 'DR in' not in nm or '1s' in nm or '8fe' in nm) for n in N) + ' |')
    for name, N in (('solution_odds', range(18, 22)), ('solution_odds_2', range(22, 25))):
        L = ['| You have | ' + ' | '.join(f'Solution in {n} or less' if n == N[0] else f'{n} or less' for n in N) + ' |', '|---|' + '---:|' * len(N)]
        for ln in (9, 10, 11, 12): row(L, f'a DR in {ln}', xv.dr(), ln, N)
        for ln in (6, 7, 8, 9): row(L, f'a DR-1s in {ln}', xv.one_s(), ln, N)
        if have8:
            for ln in (7, 8, 9, 10): row(L, f'a DR-2s 8fe in {ln}', xv.eight(), ln, N)
        write(name, L)
    # by the fewest turns to DR, taking the better of the two sides of the scramble
    a = xv._rows('sample1s.tsv'); b = xv._rows('sample1s_labels.tsv')
    L = ['| Fewest turns to a real DR, from the better side | Share of DR-1s | Average finish, moves | Average finish minus a DR\'s, moves | Finish in 14 or less | Finish in 15 or less |', '|---:|---:|---:|---:|---:|---:|']
    for k in (2, 3, 4, 5, 6):
        h = [0] * 30
        for x, y in zip(a, b):
            if min(int(y['turns_to_dr']), int(y['turns_to_dr_inverse'])) == k: h[int(x['finish'])] += 1
        L.append(f'| {k} | {num(100 * sum(h) / len(a))} | {hu(avg(h), 2):.2f} | +{hu(avg(h) - avg(xv.dr()), 2):.2f} | {pct(h, 14)} | {pct(h, 15)} |')
    write('better', L)

def t_skip():
    txt = open(O + 'seo_skip.txt').read()
    def block(key):
        seg = txt.split(f'number of slice-EO skips, {key}:')[1].split('number of')[0]
        h = {}
        for l in seg.strip().split('\n'):
            l = l.strip()
            if l[0].isdigit(): k, v = l.split(':'); h[int(k)] = int(v.split('=')[0])
        return h
    tot = 70963200
    L = ['| Slice-EO skips on the scramble | Any skip, on normal | Any skip, on normal or inverse | All-oriented skips only, on normal | All-oriented skips only, on normal or inverse |', '|---|---:|---:|---:|---:|']
    hs = [block(k) for k in ('normal', 'both', 'normal oriented', 'both oriented')]
    L.append('| at least one | ' + ' | '.join(fmt(tot - h.get(0, 0), tot) for h in hs) + ' |')
    for k in (0, 1, 2, 3):
        L.append(f'| exactly {k} | ' + ' | '.join(fmt(h.get(k, 0), tot) for h in hs) + ' |')
    L.append('| 4 or more | ' + ' | '.join(fmt(sum(v for kk, v in h.items() if kk >= 4), tot) for h in hs) + ' |')
    L.append('| average number | ' + ' | '.join(f'{hu(sum(k * v for k, v in h.items()) / tot, 2):.2f}' for h in hs) + ' |')
    write('skip_odds', L)
    J = json.load(open(O + 'seo_hist.json'))
    # each of these is two tables: whether there is a route and its average length, then how often it is short
    # (one table would be eight columns wide); skips that never lead there only appear in the first
    def rows(nm, key):
        h = {int(k): v for k, v in J[key].items()}; tot = sum(h.values()); reach = tot - h.get(255, 0)
        if not reach: return f'| {nm} | never | |', None
        mean = sum(d * c for d, c in h.items() if d != 255) / reach
        cum = lambda t: sum(c for d, c in h.items() if d <= t)
        return (f'| {nm} | {fmt(reach, tot) if reach < tot else "always"} | {hu(mean, 2):.2f} |',
                f'| {nm} | ' + ' | '.join(fmt(cum(t), tot) for t in (5, 6, 7, 8, 9)) + ' |')
    def heads(lab):
        return (['| ' + ' | '.join(lab) + ' | A route exists, share of such skips | Average moves, when there is one |', '|' + '---|' * len(lab) + '---:|---:|'],
                ['| ' + ' | '.join(lab) + ' | In 5 moves or less, share of all such skips | 6 or less | 7 or less | 8 or less | 9 or less |', '|' + '---|' * len(lab) + '---:|' * 5])
    fam = [('another axis than the slice\'s own, all oriented', 'eo-fb', 'A oriented'), ('another axis, all misoriented', 'eo-fb', 'A misoriented'),
           ('the slice\'s own axis, all oriented', 'eo-ud', 'B oriented'), ('the slice\'s own axis, all misoriented', 'eo-ud', 'B misoriented')]
    def two(title, items, lab):
        A, B = heads(lab)
        for nm, key in items:
            a, b = rows(nm, key); A.append(a)
            if b: B.append(b)
        write(title, A); write(title + '_dist', B)
    for cls, title in (('1s', 'skip_to_1s'), ('2s8fe', 'skip_to_8fe'), ('dr', 'skip_to_dr')):
        two(title, [(nm, f'{rule}_{cls} | {f}') for nm, rule, f in fam], ['The skip'])
    items = []
    for nm, rule, f in fam:
        for how, pre, r in (('strict', '', rule), ('quarter turns of the EO axis when they miss the slice pieces', 's', rule), ('any turns', '', 'all')):
            items.append((f'{nm} | {how}', f'{pre}{r}_1s | {f}'))
    two('skip_to_1s_rules', items, ['The skip', 'Moves allowed'])


def t_appendix():
    W = json.load(open(O + 'witness.json'))
    rows = sorted(W['layouts'], key=lambda r: (r['turns'], r['flipped']))
    L = ['Corners oriented on F/B (so the slice turn that fixes is `R L`, and the places inside that slice are UF, UB, DF, DB). The other choice of faces is the same table with the cube turned. "Scramble" gives a DR-1s with that layout: it is a DR followed by the fix backwards.', '',
         'Each row is one layout of the four flipped edges, sorted by how many face turns its shortest fix takes.', '',
         '| Flipped edges at | Fewest turns to a real DR | A shortest fix | Scramble |', '|---|---:|---|---|']
    for r in rows: L.append(f"| {r['flipped']} | {r['turns']} | `{r['fix']}` | `{r['scramble']}` |")
    four = [r for r in rows if min(r['turns'], r['other_direction']) == 4]
    H13 = ['Each row is one layout; the two middle columns are its fewest turns to a real DR as the layout stands and after turning the last trigger move the other way.', '',
           '| Flipped edges at | Turns to DR as it is | Turns to DR with the last move the other way | Fix as it is |', '|---|---:|---:|---|']
    L += ['', f"**With the last trigger move free to go either way.** If the move before was a quarter turn of U or D, turning it the other way moves the layout by a `U2` or `D2`. Taking the better of the two, the count is {', '.join(map(str, W['simon']))} layouts at 2 to 6 turns. The {len(four)} at 4:", ''] + H13
    for r in four: L.append(f"| {r['flipped']} | {r['turns']} | {r['other_direction']} | `{r['fix']}` |")
    write('app_a', L)
    S13 = H13 + [f"| {r['flipped']} | {r['turns']} | {r['other_direction']} | `{r['fix']}` |" for r in four]
    write('simon13', S13)
    import patterns
    def cell(c, own=False):
        if not c: return 'cannot happen'
        if set((k[0], k[1]) for k in c) == {(2, 8)}: return 'DR-2s, 8 flipped, centers right (6 turns to DR; not the 8fe case)' if own else 'DR-2s 8fe'
        if set((k[0], k[1]) for k in c) == {(2, 0)}: return 'DR-2s, 0 flipped (6 turns to DR)'
        n = sum(c.values()); by = collections.defaultdict(collections.Counter)
        for (s_, fl, sp), v in c.items(): by[s_][(fl, sp)] += v
        def flips(cc):
            fls = sorted({k[0] for k in cc}); sps = sorted({k[1] for k in cc})
            if len(fls) > 1: return f'{fls[0]} to {fls[-1]} flipped'
            if fls[0] in (0, 8): return f'{fls[0]} flipped'
            return f'{fls[0]} flipped, ' + (f'split {sps[0][0]}-{sps[0][1]}' if len(sps) == 1 else 'any split')
        parts = []
        for s_, cc in sorted(by.items()):
            nm = 'DR' if s_ == 0 else f'DR-{s_}s'
            parts.append(f'{nm}, {flips(cc)}' if len(by) == 1 else f'{nm} ({num(100 * sum(cc.values()) / n)}), {flips(cc)}')
        return '; '.join(parts)
    L = ['The frame: the corners\' colour is white/yellow (U/D), so the slice edges of the DR-xs are the E-slice edges; "M" and "S" are the edges belonging to the M and S slices. The orientation is for the axis in the first column, and the route keeps it (no quarter turns of that axis\'s faces). Each class of edges is all good or all bad. A percentage means it depends on where the pieces end up; without one it is guaranteed. Any other colour or axis is this table with the cube turned.']
    for axis, an in (('FB', 'F/B, not the slice\'s own'), ('UD', 'U/D, the slice\'s own')):
        L += ['', f'**EO axis {an}.** Each row is which edges are bad for that axis; each column is where the corners\' white or yellow faces end up, and the cell is the DR-xs you land on.', '',
              '| Bad edges | Corners on U/D (their own faces) | Corners on R/L | Corners on F/B |', '|---|---|---|---|']
        for pat in ('', 'E', 'M', 'S', 'EM', 'ES', 'MS', 'EMS'):
            bad = 'none' if not pat else 'all twelve' if pat == 'EMS' else ' and '.join(pat)
            L.append(f"| {bad} | " + ' | '.join(cell(patterns.outcomes(axis, pat, f), f == 'UD') for f in ('UD', 'RL', 'FB')) + ' |')
    write('app_b', L)

def t_eo8():
    """From a full EO: moves to the real DR and to the DR-2s 8fe on one axis (eo8_hist.py)."""
    J = json.load(open(O + 'eo8_hist.json')); n = J['positions']
    L = ['| Moves from a full EO | Positions that many moves from the real DR | Positions that many moves from the DR-2s 8fe |', '|---:|---:|---:|']
    for d, (a, b) in enumerate(zip(J['dr'], J['8fe'])): L.append(f'| {d} | {a:,} | {b:,} |')
    avg = lambda h: sum(d * c for d, c in enumerate(h)) / sum(h)
    L.append(f"| all {n:,} positions, average | {hu(avg(J['dr']), 2):.2f} | {hu(avg(J['8fe']), 2):.2f} |")
    write('eo_to_8fe', L)

if __name__ == '__main__':
    todo = sys.argv[1:] or ['kinds', 'fix', 'finish', 'skip', 'eo8', 'app']
    for name in todo: {'kinds': t_kinds, 'fix': t_fix, 'finish': t_finish, 'skip': t_skip, 'eo8': t_eo8, 'app': t_appendix}[name]()
