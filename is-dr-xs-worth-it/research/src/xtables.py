#!/usr/bin/env python3
"""Tables of the DR-xs report, written to report/data/*.md from the outputs in research/out/."""
import csv, json, collections, os, sys
import xv
from xv import fmt, num, pct, avg, share, CS_ORDER, O
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
    L = ['| Slices needed | Corners oriented on | Slice edges against the centers | Flipped edges | Kinds | Turns to a real DR |', '|---:|---|---|---|---:|---|']
    for (s, own, bit) in sorted(g):
        rows = g[(s, own, bit)]
        L.append(f"| {s} | {'the faces of their own colour' if own else 'two other faces'} | {'agree' if bit else 'disagree'} | {lst(int(r['flips']) for r in rows)} | {len(rows)} | {rng(int(r['turns_to_dr']) for r in rows)} |")
    L.append(f'| | | | | **{len(K)}** | |')
    write('kinds', L)

def t_fix():
    K = kinds(); L = ['| Slices needed | Kinds | ' + ' | '.join(f'{t} turns' for t in range(2, 11)) + ' | Average |', '|---:|---:|' + '---:|' * 10]
    for s in (1, 2, 3):
        rows = [int(r['turns_to_dr']) for r in K if int(r['slices']) == s]; c = collections.Counter(rows)
        L.append(f"| {s} | {len(rows)} | " + ' | '.join(str(c[t]) if c[t] else '' for t in range(2, 11)) + f' | {sum(rows) / len(rows):.2f} |')
    write('fix_turns', L)
    # DR-1s by where the four flipped edges sit, for corners on F/B (the fixing slice is R L)
    import fe
    pl = [p for p in fe.EDGES if p[2] != 0]
    def name(p): return ''.join(ch for ch, (a, sg) in (('U', (1, 1)), ('D', (1, -1)), ('F', (2, 1)), ('B', (2, -1)), ('R', (0, 1)), ('L', (0, -1))) if p[a] == sg)
    g = collections.defaultdict(list)
    for r in K:
        if r['slices'] != '1' or r['faces'] != 'FB': continue
        inside = sum(1 for p, b in zip(pl, r['flip_places']) if b == '1' and p[0] == 0)
        g[inside].append((int(r['turns_to_dr']), ' '.join(name(p) for p, b in zip(pl, r['flip_places']) if b == '1'), r['fix']))
    L = ['| Flipped edges already in the slice that fixes | Layouts | Turns to DR | Shortest example: flipped at | Fix |', '|---:|---:|---|---|---|']
    for k in (4, 3, 2, 1, 0):
        c = collections.Counter(t for t, _, _ in g[k]); ex = min(g[k])
        L.append(f"| {k} | {len(g[k])} | {', '.join(f'{t}: {n}' for t, n in sorted(c.items()))} | {ex[1]} | `{ex[2]}` |")
    write('dr1s_layouts', L)

def t_finish():
    TR1 = {'4a1': '14.8', '4b2': '14.9', '4a2': '15.6', '4c3': '15.7', '2c3': '15.2', '2c4': '15.5'}
    TR8 = {'4a1': '13.26', '4b2': '13.59', '2c3': '13.80', '4c3': '14.54', '2c4': '14.80'}
    have8 = os.path.exists(O + 'sample8fe.tsv') and os.path.getsize(O + 'sample8fe.tsv') > 100
    L = ['| Corner subset | Share of states | DR: average finish | DR-1s: average finish | DR-1s against DR | trangium\'s DR-1s (nissy optimal) | DR-2s 8fe: average finish | 8fe against DR | trangium\'s 8fe (nissy optimal) |', '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for cs in CS_ORDER + [None]:
        d, h = xv.dr(cs), xv.one_s(cs); e = xv.eight(cs) if have8 else None
        L.append(f"| {cs or '**all**'} | {100 * sum(d) / sum(xv.dr()):.1f}% | {avg(d):.2f} | {avg(h):.2f} | +{avg(h) - avg(d):.2f} | {TR1.get(cs, '')} | " +
                 (f"{avg(e):.2f} | +{avg(e) - avg(d):.2f}" if e and sum(e) else ' | ') + f" | {TR8.get(cs, '')} |")
    write('finish_subset', L)
    T = range(10, 19)
    L = ['| Finish in | ' + ' | '.join(f'{t} or less' for t in T) + ' | Average |', '|---|' + '---:|' * (len(T) + 1)]
    rows = [('a DR', xv.dr()), ('a DR-1s', xv.one_s()), ('a DR-1s that one slice turn fixes', xv.one_s(turns=(2,))), ('a DR-1s that needs 5 or 6 turns to DR', xv.one_s(turns=(5, 6)))]
    if have8: rows.insert(1, ('a DR-2s 8fe', xv.eight()))
    for nm, h in rows: L.append(f'| {nm} | ' + ' | '.join(pct(h, t) for t in T) + f' | {avg(h):.2f} |')
    write('finish_odds', L)
    # solution length: route length + finish
    N = range(18, 25)
    L = ['| You have | ' + ' | '.join(f'{n} or less' for n in N) + ' |', '|---|' + '---:|' * len(N)]
    def row(nm, h, length): L.append(f'| {nm} | ' + ' | '.join(pct(h, n - length) for n in N) + ' |')
    for ln in (9, 10, 11, 12): row(f'a DR in {ln}', xv.dr(), ln)
    for ln in (6, 7, 8, 9): row(f'a DR-1s in {ln}', xv.one_s(), ln)
    if have8:
        for ln in (7, 8, 9, 10): row(f'a DR-2s 8fe in {ln}', xv.eight(), ln)
    write('solution_odds', L)
    # split
    a = xv._rows('sample1s.tsv'); b = xv._rows('sample1s_labels.tsv')
    L = ['| Flipped edges by the slice they belong to | Share of DR-1s | Average finish | In 14 or less | In 15 or less |', '|---|---:|---:|---:|---:|']
    def srow(nm, p):
        h = [0] * 30
        for x, y in zip(a, b):
            if p(y): h[int(x['finish'])] += 1
        L.append(f'| {nm} | {100 * sum(h) / len(a):.1f}% | {avg(h):.2f} | {pct(h, 14)} | {pct(h, 15)} |')
    srow('4-0 on at least one side', lambda y: '4-0' in (y['split'], y['split_inverse']))
    srow('2-2 on both sides', lambda y: y['split'] == y['split_inverse'] == '2-2')
    srow('2-2 on one side, 3-1 on the other', lambda y: {y['split'], y['split_inverse']} == {'2-2', '3-1'})
    srow('3-1 on both sides', lambda y: y['split'] == y['split_inverse'] == '3-1')
    srow('any', lambda y: True)
    write('split', L)

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
    L = ['| Slice-EO skips on the scramble | On normal | On normal or inverse | All-oriented only, normal | All-oriented only, normal or inverse |', '|---|---:|---:|---:|---:|']
    hs = [block(k) for k in ('normal', 'both', 'normal oriented', 'both oriented')]
    L.append('| at least one | ' + ' | '.join(fmt(tot - h.get(0, 0), tot) for h in hs) + ' |')
    for k in (0, 1, 2, 3):
        L.append(f'| exactly {k} | ' + ' | '.join(fmt(h.get(k, 0), tot) for h in hs) + ' |')
    L.append('| 4 or more | ' + ' | '.join(fmt(sum(v for kk, v in h.items() if kk >= 4), tot) for h in hs) + ' |')
    L.append('| average number | ' + ' | '.join(f'{sum(k * v for k, v in h.items()) / tot:.2f}' for h in hs) + ' |')
    write('skip_odds', L)
    J = json.load(open(O + 'seo_hist.json'))
    def row(nm, key, cols=range(4, 12)):
        h = {int(k): v for k, v in J[key].items()}; tot = sum(h.values()); reach = tot - h.get(255, 0)
        mean = sum(d * c for d, c in h.items() if d != 255) / reach if reach else 0
        cum = lambda t: sum(c for d, c in h.items() if d <= t)
        return f'| {nm} | {fmt(reach, tot) if reach < tot else "always"} | ' + ' | '.join(fmt(cum(t), tot) if reach else '' for t in (5, 6, 7, 8, 9)) + f' | {mean:.2f} |' if reach else f'| {nm} | never | | | | | | |'
    head = ['| The skip | A route exists | In 5 or less | In 6 or less | In 7 or less | In 8 or less | In 9 or less | Average when there is one |', '|---|---:|---:|---:|---:|---:|---:|---:|']
    fam = [('another axis than the slice\'s own, all oriented', 'eo-fb', 'A oriented'), ('another axis, all misoriented', 'eo-fb', 'A misoriented'),
           ('the slice\'s own axis, all oriented', 'eo-ud', 'B oriented'), ('the slice\'s own axis, all misoriented', 'eo-ud', 'B misoriented')]
    for cls, title in (('1s', 'skip_to_1s'), ('2s8fe', 'skip_to_8fe'), ('dr', 'skip_to_dr')):
        L = list(head)
        for nm, rule, f in fam: L.append(row(nm, f'{rule}_{cls} | {f}'))
        write(title, L)
    L = list(head)
    for nm, rule, f in fam:
        L.append(row(nm + ', strict', f'{rule}_1s | {f}')); L.append(row(nm + ', quarter turns allowed when they miss the slice pieces', f's{rule}_1s | {f}')); L.append(row(nm + ', any turns', f'all_1s | {f}'))
    write('skip_to_1s_rules', L)


def t_appendix():
    W = json.load(open(O + 'witness.json'))
    rows = sorted(W['layouts'], key=lambda r: (r['turns'], r['flipped']))
    L = ['Corners oriented on F/B (so the slice turn that fixes is `R L`, and the places inside that slice are UF, UB, DF, DB). The other choice of faces is the same table with the cube turned. "Scramble" gives a DR-1s with that layout: it is a DR followed by the fix backwards.', '',
         '| Flipped edges at | Turns to DR | A shortest fix | Scramble |', '|---|---:|---|---|']
    for r in rows: L.append(f"| {r['flipped']} | {r['turns']} | `{r['fix']}` | `{r['scramble']}` |")
    four = [r for r in rows if min(r['turns'], r['other_direction']) == 4]
    L += ['', f"**With the last trigger move free to go either way.** If the move before was a quarter turn of U or D, turning it the other way moves the layout by a `U2` or `D2`. Taking the better of the two, the count is {', '.join(map(str, W['simon']))} layouts at 2 to 6 turns. The {len(four)} at 4:", '',
          '| Flipped edges at | Turns as it is | Turns with the last move the other way | Fix as it is |', '|---|---:|---:|---|']
    for r in four: L.append(f"| {r['flipped']} | {r['turns']} | {r['other_direction']} | `{r['fix']}` |")
    write('app_a', L)
    S13 = ['| Flipped edges at | Turns as it is | Turns with the last move the other way | Fix as it is |', '|---|---:|---:|---|'] + [f"| {r['flipped']} | {r['turns']} | {r['other_direction']} | `{r['fix']}` |" for r in four]
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
            parts.append(f'{nm}, {flips(cc)}' if len(by) == 1 else f'{nm} ({100 * sum(cc.values()) / n:.0f}%), {flips(cc)}')
        return '; '.join(parts)
    L = ['The frame: the corners\' colour is white/yellow (U/D), so the slice edges of the DR-xs are the E-slice edges; "M" and "S" are the edges belonging to the M and S slices. The orientation is for the axis in the first column, and the route keeps it (no quarter turns of that axis\'s faces). Each class of edges is all good or all bad. A percentage means it depends on where the pieces end up; without one it is guaranteed. Any other colour or axis is this table with the cube turned.', '',
         '| EO axis | Bad edges | Corners on U/D (their own faces) | Corners on R/L | Corners on F/B |', '|---|---|---|---|---|']
    for axis, an in (('FB', 'F/B (not the slice\'s own)'), ('UD', 'U/D (the slice\'s own)')):
        for pat in ('', 'E', 'M', 'S', 'EM', 'ES', 'MS', 'EMS'):
            bad = 'none' if not pat else 'all twelve' if pat == 'EMS' else ' and '.join(pat)
            L.append(f"| {an} | {bad} | " + ' | '.join(cell(patterns.outcomes(axis, pat, f), f == 'UD') for f in ('UD', 'RL', 'FB')) + ' |')
    write('app_b', L)

if __name__ == '__main__':
    todo = sys.argv[1:] or ['kinds', 'fix', 'finish', 'skip', 'app']
    for name in todo: {'kinds': t_kinds, 'fix': t_fix, 'finish': t_finish, 'skip': t_skip, 'app': t_appendix}[name]()
