"""Apply the S+T <= 5 meta (at most 1 pre-2qt move, every case) to the user's edited doc, add the pair-count appendix,
and fix the mechanical inconsistencies.  usage: mkfinal4.py IN.md OUT.md"""
import sys, json, re
K = 5
J = {m: json.load(open(f'../out/meta/final{m}_st{K}.json')) for m in (2, 3, 4)}
GOAL = {2: 12, 3: 13, 4: 14}
ORDER = {2: ['4a2', '4b2'], 3: ['0c3', '2c3', '4c3'], 4: ['0c4', '2c4', '4c4']}
ALL = [(m, k) for m in (2, 3, 4) for k in ORDER[m]]
C = {k: J[m]['cases'][k] for m, k in ALL}
SK = {'4b2': 3, '4a2': 5, '2c3': 5, '4c3': 7, '2c4': 7, '0c3': 9, '0c4': 9, '4c4': 9}
def one_in(s):
    v = 1 / s
    return f'1 in {v:.1f}' if v < 10 else f'1 in {v:,.0f}'
def pct(x, dec=0): return f'{100 * x:.{dec}f}%'
def num(x): return f'{x:,.0f}'
def who(c): return f"{c['drs']:,} DRs, {c['wg']:,} within-goal" + (' (a small sample)' if c['wg'] < 100 else '')
BN = {'none': 'Baseline (no DR Bounding)', 'simple': 'Simple', 'cca': 'Corner-case-aware', 'comp': 'Comprehensive'}
def cols(first): return f'| {first} | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |\n|---|---|---|---|---|---|'
def row(name, b, bold=False):
    n = f'**{name}**' if bold else name
    return f"| {n} | {num(b['htr_med'])} | {one_in(b['share'])} | {pct(b['miss'], 1)} | {pct(b['found']['5'])} | {pct(b['found']['10'])} |"

src = open(sys.argv[1]).read()
def between(s, a, b, new, start=0):
    i = s.index(a, start); j = s.index(b, i + len(a))
    return s[:i] + new + s[j:]
def rep(s, a, b):
    assert s.count(a) == 1, ('not unique', a[:70], s.count(a)); return s.replace(a, b)

# ---- corner case table
ct = ['| Corner case | Shortest skeleton length | Within-goal DRs | The meta misses a within-goal finish | DRs in the sample |', '|---|---|---|---|---|']
for k in ['4b2', '4a2', '2c3', '4c3', '2c4', '0c3', '0c4', '4c4']:
    c = C[k]; ct.append(f"| {k} | {SK[k]} | {pct(c['wg'] / c['drs'], 1)} | {pct(c['bounds']['cca']['miss'], 1)} | {c['drs']:,} |")
src = between(src, '| Corner case | Shortest skeleton length |', '\n\nAs we\'ll see below', '\n'.join(ct))

# ---- section 2 per-case blocks
s2 = []
for m in (2, 3, 4):
    s2.append(f'### {m}qt DRs (goal {GOAL[m]})')
    for k in ORDER[m]:
        c = C[k]; b0, b1 = c['bounds']['none'], c['bounds']['cca']
        dm = 100 * (b1['miss'] - b0['miss'])
        miss = 'no change in the chance of missing' if abs(dm) < 0.05 else f'a chance of missing {dm:.1f} points higher'
        s2.append(f"**{k}** · {who(c)} · {num(c['routes_meta'])} routes to 2qt per DR (median, both searches). "
                  f"The bound finishes {b0['htr_med'] / b1['htr_med']:.0f}× fewer HTRs with {miss}. It finds a within-goal finish in the first 10 for "
                  f"{pct(b1['found']['10'])} of within-goal DRs against {pct(b0['found']['10'])}.")
        s2.append(cols('Search') + '\n' + row(BN['none'], b0) + '\n' + row(BN['cca'], b1, True))
i2 = src.index('## 2. Stats for the recommended meta')
src = between(src, '### 2qt DRs (goal 12)', '### Where the misses come from', '\n\n'.join(s2) + '\n\n', i2)
ratios = [C[k]['bounds']['none']['htr_med'] / C[k]['bounds']['cca']['htr_med'] for _, k in ALL]
src = rep(src, 'reduces the number of HTRs to check by 10-20x**', f'reduces the number of HTRs to check by {min(ratios):.0f}-{max(ratios):.0f}x**')

# ---- misses
M = {k: C[k]['miss'] for _, k in ALL}
for k in M: assert max(['next', 'pre2', 'more', 'bound', 'beyond'], key=lambda c: M[k][c]) in ('pre2', 'beyond') or k in ('0c3', '4a2')
mt = ['| Corner case | Missed | Needs 1 more S+T | Needs a second pre-2qt move | Needs 2 or more S+T beyond the limit | Error in DR Bound | Needs four more quarter turns |', '|---|---|---|---|---|---|---|']
for m, k in ALL:
    x = M[k]; w = C[k]['wg']
    mt.append(f"| {k} | {pct(x['meta'], 1)} | {pct(x['next'] / w, 1)} | {pct(x['pre2'] / w, 1)} | {pct(x['more'] / w, 1)} | {pct(x['bound'] / w, 1)} | {pct(x['beyond'] / w, 1)} |")
src = between(src, '| Corner case |  Missed |', '\n\n## Appendix A', '\n'.join(mt))
src = re.sub(r'Without them, 4b2 would miss [0-9.]+% of the time instead of [0-9.]+%, and 4c3 [0-9.]+% instead of [0-9.]+%\.',
             f"Without them, 4b2 would miss {pct(M['4b2']['own'], 1)} of the time instead of {pct(M['4b2']['meta'], 1)}, and 4c3 {pct(M['4c3']['own'], 1)} instead of {pct(M['4c3']['meta'], 1)}.", src)
src = re.sub(r'save at most \d+ DRs in any case', f"save at most {max(M[k]['beyond'] for _, k in ALL)} DRs in any case", src)

# ---- appendix A
sA = []
for m in (2, 3, 4):
    sA.append(f'### {m}qt DRs (goal {GOAL[m]})')
    for k in ORDER[m]:
        B = C[k]['bounds']
        sA.append(f"**{k}** · {who(C[k])}. Corner-case-aware makes a finished HTR {B['cca']['share'] / B['none']['share']:.1f}× likelier to be within goal than the baseline does; "
                  f"comprehensive adds {B['comp']['share'] / B['cca']['share']:.1f}× on top.")
        sA.append(cols('Bound') + '\n' + '\n'.join(row(BN[b], B[b], b == 'cca') for b in ['none', 'simple', 'cca', 'comp']))
iA = src.index('## Appendix A.')
src = between(src, '### 2qt DRs (goal 12)', '## Appendix B.', '\n\n'.join(sA) + '\n\n', iA)

# ---- appendix B
sB = []
for m in (2, 3, 4):
    sB.append(f'### {m}qt DRs (goal {GOAL[m]})')
    for k in ORDER[m]:
        G = C[k]['grid']; a, b4, e = G['5,1'], G['4,1'], G['5,2']
        parts = []
        if pct(b4['miss'], 1) == pct(a['miss'], 1): parts.append(f"S+T ≤ 4 misses no more often ({pct(a['miss'], 1)})")
        else: parts.append(f"S+T ≤ 4 misses {pct(b4['miss'], 1)} of the time instead of {pct(a['miss'], 1)}")
        if pct(e['miss'], 1) == pct(a['miss'], 1): parts.append('a second pre-2qt move changes nothing')
        else: parts.append(f"a second pre-2qt move takes it to {pct(e['miss'], 1)}, for {num(e['htr_med'])} HTRs instead of {num(a['htr_med'])} and {num(e['routes'])} routes to 2qt instead of {num(a['routes'])}")
        sB.append(f"**{k}** · {who(C[k])}. " + parts[0][0].upper() + parts[0][1:] + '; ' + parts[1] + '.')
        rows = ['| S+T at most | Pre-2qt moves at most | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |', '|---|---|---|---|---|---|']
        for kk in (2, 3, 4, 5):
            for aa in (0, 1, 2, 9):
                key = f'{kk},{aa}'
                if key not in G: continue
                s = G[key]
                cl = [str(kk), 'no limit' if aa == 9 else str(aa), num(s['routes']), num(s['htr_med']), one_in(s['share']), pct(s['miss'], 1)]
                if (kk, aa) == (5, 1): cl = [f'**{v}**' for v in cl]
                rows.append('| ' + ' | '.join(cl) + ' |')
        sB.append('\n'.join(rows))
iB = src.index('## Appendix B.')
src = between(src, '### 2qt DRs (goal 12)', '## Appendix C.', '\n\n'.join(sB) + '\n\n', iB)
src = rep(src, 'The tables below show the stats with different S+T and pre-2qt limits, using the corner-case-aware bound.',
          "The tables below show the stats with different S+T and pre-2qt limits, using the corner-case-aware bound. The meta's row (S+T ≤ 5, at most 1 pre-2qt move) is in bold.")

# ---- appendix C (pairs) and D (data and method)
pairs = open(sys.argv[3]).read().strip()
src = rep(src, '## Appendix C. Data and method', pairs + '\n\n## Appendix D. Data and method')

# ---- mechanical fixes
for a, b in [
    ('use **S+T≤ 5**', None),
    ('**For each skeleton, generate the variants with S+T ≤ 4**, with at most 1 of those extra moves before 2qt. For 4b2 or 2c3 corners, use **S+T≤ 5**. ',
     '**For each skeleton, generate the variants with S+T ≤ 5**, with at most 1 of those extra moves before 2qt.'),
    ('In the **baseline** meta, you are checking all HTRs within 4 extra moves of the goal, the equivalent of N=0.',
     'In the **baseline** meta, you check every variant with S+T ≤ 5 and S+T+L ≤ G, the equivalent of N=0.'),
    (' - **S**: Additional moves used to set up the 2qt trigger', ' - **S**: Additional moves used to set up the 2qt trigger, counting any extra moves before reaching 2qt'),
    ('The meta is based the extra moves', 'The meta is based on the extra moves'),
    ('to not add too many exta moves', 'to not add too many extra moves'),
    ('doc \ndefine three estimates', 'doc \ndefines three estimates'),
    ('See the doc for details\n', 'See the doc for details.\n'),
    ('In reach means S+T ≤ M.', 'In reach means S+T+L ≤ G.'),
    ('the found-within-N shares', 'the found-within-K shares'),
    ("- **Pair count at the trigger.** The number of pairs at the quarter turn from 2qt to 1qt was looked at as a further sort for 2c3 DRs with RD corners. It's kept as a note, not part of the meta.",
     "- **Pair count at the trigger.** A possible further sort, looked at so far only for 2c3 DRs with RD or FD corners (appendix C)."),
]:
    if b is None: assert a in src; continue
    src = rep(src, a, b)
assert 'S+T ≤ 4 ·' not in src and 'S+T≤ 5' not in src
open(sys.argv[2], 'w').write(src)
print('ok', len(src.encode()))
