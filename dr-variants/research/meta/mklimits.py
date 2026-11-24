"""Writes "HTR search order and limits" (breadth vs depth, length restrictions, NISS strategy) from
../out/meta/tlimits.json (tlimits.py).  The report's notation: E = P+S+T, the extra moves added to the corner skeleton
to reach HTR; H = the moves at which HTR is reached (the moves made before a NISS counted, a skeleton's moves after its
last quarter turn not).
usage: mklimits.py OUT.md"""
import sys, json
from tcommon import ORDER, BYQT, path as tpath

Lm = json.load(open(tpath('tlimits.json')))
ORDER = [k for k in ORDER if k in Lm]
MS = [m for m in (2, 3, 4) if any(k in Lm for k in BYQT[m])]
GOAL = {2: 12, 3: 13, 4: 14}
DOC = 'https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0/edit?usp=sharing'
KS = (2, 3, 4, 5, 6, 8, 10)
FIRSTK = Lm[ORDER[0]]['first']
ROWS = [('len', 'Breadth first'), ('skel', 'Depth first')] + [(f'two{k}', f'Two pass, {k} per skeleton') for k in KS]
HK = ['3', '4', '5', '6']          # caps on H shown (the row with no cap on H is H+L <= G-1)
BIG = [k for k in ORDER if Lm[k]['wg'] >= 100]

def pct(x, dec=1): return f'{100 * x:.{dec}f}%'
def num(x): return '—' if x is None else (f'{x:,.0f}' if abs(x - round(x)) < 1e-9 else f'{x:,.1f}')
def who(c): return f"{c['drs']:,} DRs, {c['wg']:,} within-goal" + (' (a small sample)' if c['wg'] < 100 else '')
def span(vs, f): return f(min(vs)) if f(min(vs)) == f(max(vs)) else f'{f(min(vs))} to {f(max(vs))}'
def names(ks): return ', '.join(ks[:-1]) + (' and ' if len(ks) > 1 else '') + ks[-1]
def byqt(ks):
    """Corner cases by quarter turns, then by name, as a list with a comma before the last 'and'."""
    ks = sorted(ks, key=lambda k: (k[2], k))
    return ks[0] if len(ks) == 1 else (' and '.join(ks) if len(ks) == 2 else ', '.join(ks[:-1]) + ', and ' + ks[-1])
def p50(k, o): return Lm[k]['order'][o]['p50']
def p95(k, o): return Lm[k]['order'][o]['p95']
def G(k, h, c): return Lm[k]['grid'][f'{h}_{c}']            # H <= h ('none': no cap on H) and H+L <= c
def reaches(e): return round(100 * e['reach'], 1) >= 95.0     # 95% as the tables print it

out = []
def w(s=''): out.append(s)

# ---------------------------------------------------------------------------------------------------------------- intro
w('# HTR search order and limits')
w()
w('24 Nov 2026')
w()
w('This is an analysis of different metas for prioritizing HTRs when searching for a DR finish.')
w('The key decisions that the meta needs to make are:')
w(' - **Breadth vs depth**: how many HTRs to check on a skeleton before moving to another skeleton')
w(' - **Length restriction**: limits on the HTRs to check')
w(' - **NISS strategy**: when to use NISS')
w()
w('The analysis uses a sample of 2,000 random DRs each for 2qt, 3qt and 4qt (1,960 for 2qt), split by corner case. The success criterion is')
w('finding a 12/13/14 move finish for a 0-2qt/3qt/4qt DR.')
w()
w('The analysis uses the following definitions:')
w(' - **G** goal total move count to leave-slice: 12, 13, or 14')
w(' - **L** length of the corner skeleton')
w(' - **E** extra moves that must be added to the corner skeleton to reach HTR')
w(' - **H** total moves to reach HTR')
w()
w(f'See [Advanced DR Bounding]({DOC}) for definition of a corner skeleton, its length, and extra moves. In that doc\'s notation, E=P+S+T')
w()
w('## Conclusions')
w()
CONC = len(out)
w()

# ---------------------------------------------------------------------------------------------------------------- section 1
w('## 1. Breadth vs Depth')
w()
w('Finishing the shortest HTR first should find a solution soonest. But that order mixes the skeletons, and by hand it is easier to go through one skeleton at a time.')
w('This section measures what that costs by comparing three strategies:')
w()
w('- **Breadth first** Strict ordering by H, mixing together all skeletons on both sides. The a-priori optimal ordering')
w('- **Depth first** Order skeletons by L, then check all of a skeleton\'s HTRs before moving to the next: its NISS after a single qt first, then linear, shortest first in each')
w('- **Two pass** Order skeletons by L, then check up to k HTRs per skeleton (NISS and linear combined). Finish with a depth-first second pass through the skeletons')
w()
w('The HTRs checked are the same in all three: E ≤ 5 and H ≤ G−1, with at most 1 extra move before 2qt, on normal, on inverse and with a NISS after a single qt. '
  'HTRs with the same H are taken most pairs first, and skeletons of one length in random order.')
w()
w('For all DRs that have a within-goal solution, we compute')
w()
w('- **Median place.** How many HTRs must be checked to find the first within-goal finish, as a median over those DRs')
w('- **HTRs to finish for 95%.** How many HTRs have to be finished to have a 95% chance of finding a within-goal finish. A dash means the HTRs checked don\'t reach 95% of those DRs')
w()
ok95 = [k for k in BIG if p95(k, 'len') is not None]
r50 = {j: [p50(k, f'two{j}') / p50(k, 'len') for k in BIG] for j in KS}
r95 = {j: [p95(k, f'two{j}') / p95(k, 'len') for k in ok95 if p95(k, f'two{j}') is not None] for j in KS}
d50 = [p50(k, 'skel') / p50(k, 'len') for k in BIG]; d95 = [p95(k, 'skel') / p95(k, 'len') for k in ok95 if p95(k, 'skel') is not None]
S1 = (f"a two-pass strategy with {FIRSTK} HTRs per skeleton puts the median place at {span(r50[FIRSTK], lambda v: f'{v:.1f}x')} that of breadth first and takes {span(r95[FIRSTK], lambda v: f'{v:.1f}x')} as many HTRs for 95%. "
      f"Depth first puts the median place at {span(d50, lambda v: f'{v:.0f}x')} and takes {span(d95, lambda v: f'{v:.0f}x')} as many HTRs for 95%")
w(f"Across the corner cases with at least 100 within-goal DRs, {S1}. A smaller first pass helps the median and a larger one the 95% point, so {FIRSTK} is the trade-off.")
w()
for m in MS:
    w(f'### {m}qt DRs (goal {GOAL[m]})')
    w()
    for k in BYQT[m]:
        c = Lm[k]; x = c['order']
        lead = (f"**{k}** · {who(c)} · E ≤ 5, H ≤ {c['cap']} · {num(x['htr_med'])} HTRs and {num(x['skel_med'])} skeletons per DR (median) · reach {pct(x['reach'])}. "
                f"Depth first puts the first solution at place {num(p50(k, 'skel'))} instead of {num(p50(k, 'len'))}. ")
        m50 = min(KS, key=lambda j: (p50(k, f'two{j}'), j))
        lead += f"Of the two-pass orders, {m50} per skeleton has the best median place ({num(p50(k, f'two{m50}'))})"
        if p95(k, 'len') is not None:
            m95 = min(KS, key=lambda j: (p95(k, f'two{j}') is None, p95(k, f'two{j}') or 0, j))
            lead += f", and {m95} per skeleton needs the fewest HTRs for 95% ({num(p95(k, f'two{m95}'))}, against {num(p95(k, 'len'))} breadth first)."
        else:
            lead += '.'
        w(lead)
        w()
        if not reaches(x):
            # the DRs out of reach have their within-goal solutions on skeletons with four more quarter turns
            lost = c['wg'] - round(x['reach'] * c['wg'])
            w(f"The analysis only extends skeletons to 2 extra qt, and {lost} of the {c['wg']} within-goal DRs "
              + ('needs' if lost == 1 else 'need') + f" more, so the success rate stops at {pct(x['reach'])} and 95% is never reached.")
            w()
        w('| Order | Median place | HTRs to finish for 95% |')
        w('|---|---|---|')
        for key, name in ROWS:
            w(f"| {name} | {num(p50(k, key))} | {num(p95(k, key))} |")
        w()

# ---------------------------------------------------------------------------------------------------------------- section 2
def best(k, kind):
    """The restriction of this kind with the fewest HTRs per DR that still reaches 95% of within-goal DRs, or None."""
    g = Lm[k]['goal']
    if kind == 'hl': cand = [(c, G(k, 'none', c)) for c in range(g - 5, g)]
    elif kind == 'h': cand = [(h, G(k, h, g - 1)) for h in HK]
    else: cand = [((h, c), G(k, h, c)) for h in HK for c in range(g - 5, g - 1)]
    cand = [x for x in cand if reaches(x[1])]
    return min(cand, key=lambda x: (x[1]['htr_med'], x[1]['n'])) if cand else None
def cap_rows(k):
    """The rows of a corner case's table: (kind, key, name, numbers); kind: 'hl' (H+L), 'h' (H alone), 'both'."""
    g = Lm[k]['goal']
    rows = [('hl', c, f'H ≤ {c}', G(k, 'none', c)) for c in range(g - 5, g)]
    rows += [('h', h, f'E ≤ {h}', G(k, h, g - 1)) for h in HK]
    both = [(h, g - 2) for h in ('4', '5', '6')]
    b = best(k, 'both')
    if b and b[0] not in both: both.append(b[0])
    rows += [('both', (h, c), f'E ≤ {h}, H ≤ {c}', G(k, h, c)) for h, c in sorted(both, key=lambda x: (-x[1], x[0]))]
    return rows
def best_name(k, kind):
    b = best(k, kind)
    return f'H ≤ {b[0]}' if kind == 'hl' else (f'E ≤ {b[0]}' if kind == 'h' else f'E ≤ {b[0][0]} with H ≤ {b[0][1]}')
BEST = {k: {kind: best(k, kind) for kind in ('hl', 'h', 'both')} for k in ORDER}

w('## 2. Length Restrictions')
w()
anyr = [Lm[k]['anyp']['htr_med'] / G(k, 'none', Lm[k]['goal'] - 1)['htr_med'] - 1 for k in BIG]
anyd = [Lm[k]['anyp']['reach'] - G(k, 'none', Lm[k]['goal'] - 1)['reach'] for k in BIG]
w('An HTR too close to the goal has a very small chance of hitting the goal. We enforce these limits always:')
w(' - **H < G** Must reach HTR with at least one move to spare')
w(f" - **≤ 1 extra move before 2qt** Allowing more adds {span(anyr, lambda v: pct(v, 0))} to the HTR count for {span(anyd, lambda v: f'{100 * v:.1f}')} points of reach, "
  'and is usually unnecessary because we are checking both directions')
w()
w(f'We use the k={FIRSTK}, two-pass strategy from section 1 and consider three kinds of restrictions')
w()
w('- **H** Cap on the total moves to reach HTR')
w('- **E** Cap on the extra moves to reach HTR')
w('- **Combined** Cap both separately')
w()
w('For each corner case, the tables below show')
w()
w('- **HTRs per DR.** The median number of HTRs that satisfy the restriction. As before, ratios are most important')
w('- **Reach.** The fraction of within-goal DRs that still have a within-goal HTR under the restriction')
w('- **Median place.** How many HTRs must be checked to find the first within-goal finish. A dash means fewer than half of the within-goal DRs are reached')
w()
w('The rows in bold are, for each kind of restriction, the one with the fewest HTRs per DR that still has 95% reach.')
w()
# the recommended pair: H <= 5, H+L <= G-2
REC = {k: G(k, '5', Lm[k]['goal'] - 2) for k in ORDER}
H5 = {k: G(k, '5', Lm[k]['goal'] - 1) for k in ORDER}
cut = [REC[k]['htr_med'] / H5[k]['htr_med'] for k in BIG]
okr = [k for k in ORDER if reaches(REC[k])]; low = [k for k in ORDER if not reaches(REC[k])]
dmed = [abs(REC[k]['p50'] - H5[k]['p50']) for k in ORDER if REC[k]['p50'] is not None and H5[k]['p50'] is not None]
never = [k for k in low if not reaches(G(k, 'none', Lm[k]['goal'] - 1))]
S2 = (f"Next to E ≤ 5 alone, it keeps {span(cut, lambda v: pct(v, 0))} of the HTRs in the corner cases with at least 100 within-goal DRs and moves the median place by {max(dmed)} at most. "
      f"Reach stays at 95% or more in {len(okr)} of the {len(ORDER)} corner cases ({names(okr)}).")
if low:
    S2 += (' It falls to ' + names([f"{pct(REC[k]['reach'])} on {k}" for k in low]) + '. '
           + 'There H ≤ G−1 keeps 95%' + (f" (except on {names(never)}, which never reaches it)" if never else '') + ', and so does more NISS (section 3).')
w('Across corner cases, a combined restriction gives the best tradeoff: E ≤ 5, H ≤ G−2.')
w(S2)
w()
for m in MS:
    w(f'### {m}qt DRs (goal {GOAL[m]})')
    w()
    for k in BYQT[m]:
        R = Lm[k]
        bold = {(kind, BEST[k][kind][0]) for kind in BEST[k] if BEST[k][kind]}
        lead = f"**{k}** · {who(R)}. "
        parts = [f"{best_name(k, kind)} ({num(BEST[k][kind][1]['htr_med'])}" + (' HTRs per DR)' if i == 0 else ')') for i, kind in enumerate(kd for kd in ('hl', 'h', 'both') if BEST[k][kd])]
        if parts:
            lead += 'The tightest restrictions with 95% reach: ' + '; '.join(parts[:-1]) + ('; and ' if len(parts) > 1 else '') + parts[-1] + '.'
            if not BEST[k]['both']: lead += f" With H ≤ {R['goal'] - 2} nothing reaches 95%."
        else:
            lead += 'No restriction reaches 95% of the within-goal DRs here, so no row is in bold.'
        w(lead)
        w()
        w('| Restriction | HTRs per DR (median) | Reach | Median place |')
        w('|---|---|---|---|')
        for kind, key, name, e in cap_rows(k):
            cells = [name, num(e['htr_med']), pct(e['reach']), num(e['p50'])]
            if (kind, key) in bold: cells = [f'**{x}**' for x in cells]
            w('| ' + ' | '.join(cells) + ' |')
        w()

# ---------------------------------------------------------------------------------------------------------------- section 3
NOPT = [('none', 'None'), ('n1', 'After 1 move'), ('n2', 'After 1-2 moves'), ('n3', 'After 1-3 moves')]
def N(k, o): return Lm[k]['niss'][o]
w('## 3. NISS Strategy')
w()
w('The search strategy used above always uses linear search on both normal and inverse, and also checks NISS for skeletons that begin or end with a qt.')
w('This section shows the effect of different NISS strategies:')
w()
w('- **None** No NISS on any skeleton')
w('- **After 1 move** NISS only after a single qt (as in Sections 1 and 2)')
w('- **After 1-2 moves** Also NISS after `X2 U`')
w('- **After 1-3 moves** Also NISS after `U X2 U`')
w()
w(f'The table uses the restrictions of section 2, E ≤ 5 and H ≤ G−2, and the two-pass order with {FIRSTK} per skeleton. '
  'A NISS after a single qt is checked before the linear HTRs of its skeleton. A NISS after more moves is checked after all of them, in the second pass.')
w()
low1 = [k for k in ORDER if not reaches(N(k, 'n1'))]          # a NISS after 1 move leaves them under 95%
never = [k for k in low1 if not reaches(N(k, 'n2'))]          # ... and so does a NISS after 1-2 moves
assert all(reaches(N(k, 'none')) is False for k in BIG), 'written for corner cases that need a NISS to reach 95%'
w('A NISS after 1 move is important. ' + ('For most corner cases, it\'s enough to get the reach above 95%.' if low1 else 'In every corner case it\'s enough to get the reach above 95%.'))
if low1:
    w(f"The exceptions are {byqt(low1)}, which require 1-2 moves"
      + (' (' + ' and '.join(f"{k} then reaches {pct(N(k, 'n2')['reach'])}, its ceiling" for k in never) + ').' if never else '.'))
w()
w('| Corner case | NISS | HTRs per DR (median) | Reach | Median place |')
w('|---|---|---|---|---|')
for k in ORDER:
    for key, nm_ in NOPT:
        e = N(k, key)
        w(f"| {k} | {nm_} | {num(e['htr_med'])} | {pct(e['reach'])} | {num(e['p50'])} |")

# ---------------------------------------------------------------------------------------------------------------- conclusions
conc = [f'- **Narrow first pass, then depth first** Check up to {FIRSTK} HTRs on each skeleton before moving to the next one',
        '- **Use both a relative and an absolute cap on HTR length** Restrict to E ≤ 5 and H ≤ G−2',
        '- **NISS after a single QT is enough' + (f' for all but {byqt(low1)}**' if low1 else '**')]
out[CONC:CONC] = conc
open(sys.argv[1], 'w').write('\n'.join(out) + '\n')
print('written', sys.argv[1], len(out), 'lines')
