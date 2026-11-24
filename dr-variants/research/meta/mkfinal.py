"""Markdown for the skeleton/variant meta doc from ../out/meta/final{2,3,4}.json.
usage: mkfinal.py PART M...   PART = sec2 | appA | appB"""
import sys, json

GOAL = {2: 12, 3: 13, 4: 14}
ORDER = {2: ['4a2', '4b2'], 3: ['0c3', '2c3', '4c3'], 4: ['0c4', '2c4', '4c4']}
BNAME = {'none': 'Baseline (no DR Bounding)', 'simple': 'Simple', 'cca': 'Corner-case-aware', 'comp': 'Comprehensive'}

def one_in(share):
    v = 1 / share
    return f'1 in {v:.1f}' if v < 10 else f'1 in {v:,.0f}'
def pct(x, dec=0):
    return f'{100 * x:.{dec}f}%'
def num(x):
    return f'{x:,.0f}'
def who(c):
    s = f"{c['drs']:,} DRs, {c['solvable']:,} solvable"
    if c['solvable'] < 100: s += ' (a small sample)'
    return s

COLS = '| {first} | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |\n|---|---|---|---|---|---|'
def row(name, b, bold=False):
    n = f'**{name}**' if bold else name
    return f"| {n} | {num(b['htr_med'])} | {one_in(b['share'])} | {pct(b['miss'], 1)} | {pct(b['found']['5'])} | {pct(b['found']['10'])} |"

def sec2(m, J):
    out = [f'### {m}qt DRs (goal {GOAL[m]})']
    for k in ORDER[m]:
        c = J['cases'][k]; b0, b1 = c['bounds']['none'], c['bounds']['cca']
        ratio = b0['htr_med'] / b1['htr_med']
        dmiss = 100 * (b1['miss'] - b0['miss'])
        miss = 'no change in the chance of missing' if abs(dmiss) < 0.05 else f'a chance of missing {dmiss:.1f} points higher'
        out.append(f"**{k}** · {who(c)} · {num(c['routes_meta'])} routes to 2qt per DR (median, both searches). "
                   f"The bound finishes {ratio:.0f}× fewer HTRs with {miss}. It finds a within-goal finish in the first 10 for "
                   f"{pct(b1['found']['10'])} of solvable DRs against {pct(b0['found']['10'])}.")
        out.append(COLS.format(first='Search') + '\n' + row(BNAME['none'], b0) + '\n' + row(BNAME['cca'], b1, True))
    return '\n\n'.join(out)

def appA(m, J):
    out = [f'### {m}qt DRs (goal {GOAL[m]})']
    for k in ORDER[m]:
        c = J['cases'][k]; B = c['bounds']
        g1 = B['cca']['share'] / B['none']['share']; g2 = B['comp']['share'] / B['cca']['share']
        out.append(f"**{k}** · {who(c)}. Corner-case-aware makes a finished HTR {g1:.1f}× likelier to be within goal than the baseline does; "
                   f"comprehensive adds {g2:.1f}× on top.")
        out.append(COLS.format(first='Bound') + '\n' + '\n'.join(row(BNAME[b], B[b], b == 'cca') for b in ['none', 'simple', 'cca', 'comp']))
    return '\n\n'.join(out)

def appB(m, J):
    out = [f'### {m}qt DRs (goal {GOAL[m]})']
    for k in ORDER[m]:
        c = J['cases'][k]; G = c['grid']
        a, b = G['3,1'], G['4,1']
        out.append(f"**{k}** · {who(c)}. Going from S+T ≤ 3 to S+T ≤ 4 at 1 pre-2qt move takes the chance of missing from "
                   f"{pct(a['miss'], 1)} to {pct(b['miss'], 1)} for {num(b['routes'])} routes to 2qt instead of {num(a['routes'])}.")
        rows = ['| S+T at most | Pre-2qt moves at most | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |',
                '|---|---|---|---|---|---|']
        for kk in (2, 3, 4):
            for aa in (0, 1, 2, 9):
                key = f'{kk},{aa}'
                if key not in G: continue
                if aa == kk: continue          # same as no limit: the pre-2qt moves can't exceed S+T
                s = G[key]; lim = 'no limit' if aa == 9 else str(aa)
                cells = [str(kk), lim, num(s['routes']), num(s['htr_med']), one_in(s['share']), pct(s['miss'], 1)]
                if (kk, aa) == (3, 1): cells = [f'**{v}**' for v in cells]
                rows.append('| ' + ' | '.join(cells) + ' |')
        out.append('\n'.join(rows))
    return '\n\n'.join(out)

part = sys.argv[1]
print('\n\n'.join({'sec2': sec2, 'appA': appA, 'appB': appB}[part](int(m), json.load(open(f'../out/meta/final{m}.json'))) for m in sys.argv[2:]))
