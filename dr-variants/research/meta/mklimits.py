"""Writes "HTR search order and limits" (the order, the caps, NISS) from ../out/meta/tlimits.json (tlimits.py).
usage: mklimits.py OUT.md"""
import sys, json
from tcommon import ORDER, BYQT, path as tpath

Lm = json.load(open(tpath('tlimits.json')))
S = {k: dict(v['order'], drs=v['drs'], wg=v['wg'], cap=v['cap']) for k, v in Lm.items()}
ORDER = [k for k in ORDER if k in S]
MS = [m for m in (2, 3, 4) if any(k in S for k in BYQT[m])]
GOAL = {2: 12, 3: 13, 4: 14}
PAGE_LINK = 'WRITEUP.md'
KS = (2, 3, 4, 5, 6, 8, 10)
ROWS = [('len', 'By HTR length'), ('skel', 'One skeleton at a time')] + [(f'two{k}', f'Two passes, {k} per skeleton') for k in KS]

def pct(x, dec=1): return f'{100 * x:.{dec}f}%'
def num(x): return '—' if x is None else (f'{x:,.0f}' if abs(x - round(x)) < 1e-9 else f'{x:,.1f}')
def who(c): return f"{c['drs']:,} DRs, {c['wg']:,} within-goal" + (' (a small sample)' if c['wg'] < 100 else '')
def p50(c, o): return c[o]['p50']
def p95(c, o): return c[o]['p95']
def times(a, b): return f'{a / b:.1f}x'
def span(vs, f): return f(min(vs)) if f(min(vs)) == f(max(vs)) else f'{f(min(vs))} to {f(max(vs))}'

out = []
def w(s=''): out.append(s)

w('# HTR search order and limits')
w()
w('24 Nov 2026')
w()
w(f'Three choices in a search for DR finishes, measured on the DRs of the [skeleton/variant meta]({PAGE_LINK}): the order the HTRs are finished in (section 1), which HTRs are finished at all (section 2), and how much NISS to use (section 3).')
w()
w('The goal is 12/13/14 moves from DR to a leave-slice finish for 2qt/3qt/4qt DRs. The sample is the page\'s: 2,000 random DRs of each kind (1,960 for 2qt). '
  'P, S and T are the extra moves before 2qt, in the setup and in the trigger, counted on the HTR\'s own skeleton, and L is the skeleton\'s length, as on the page. '
  'Nothing here uses a lower bound for N, so the page\'s steps 4 and 5 are left out. Every HTR is at most G−1 moves away, as in the page\'s step 3: at G moves there is no move left for a finish.')
w()

w('## Short version')
w()
SHORT = len(out)
w()

# ------------------------------------------------------------------------------------------------------------ section 1
w('## 1. Order: by HTR length, or one skeleton at a time')
w()
w('Finishing the nearest HTR first should find a solution soonest. But that order mixes the skeletons, and by hand it is easier to go through one skeleton at a time. This section measures what that costs.')
w()
w('The HTRs are the same in every order: the ones with P ≤ 1 and P+S+T ≤ 5, on normal, on inverse and in the page\'s premove pass, whose premove counts as a move. The orders:')
w()
w('- **By HTR length.** All the DR\'s HTRs by moves to HTR, fewest first, with the skeletons and the two sides mixed.')
w('- **One skeleton at a time.** Skeletons shortest first, by L, with the two sides mixed. All of a skeleton\'s HTRs are finished before the next skeleton: '
  'those of its premove pass first, then the linear ones, the nearest first in each.')
w('- **Two passes, k per skeleton.** The same walk, but the first pass finishes at most k HTRs of each skeleton, premove pass and linear together. The second pass goes through the skeletons again, one at a time, for the rest. k runs from 2 to 10.')
w()
w('In every order, HTRs equally far are taken with the most pairs first, and skeletons of one length in random order. What is still tied is taken at random; the numbers are over 20 such orders. '
  'An HTR of the premove pass belongs to the skeleton whose last quarter turn is its premove.')
w()
w('How to read the columns:')
w()
w('- **Median place.** How many HTRs are finished up to the first one within goal, as a median over within-goal DRs.')
w('- **HTRs to finish for 95%.** How many HTRs have to be finished per DR before 95% of within-goal DRs have a within-goal finish. A dash means the HTRs kept don\'t reach 95% of them.')
w()
SUM = len(out)
w()
for m in MS:
    w(f'### {m}qt DRs (goal {GOAL[m]})')
    w()
    for k in BYQT[m]:
        c = S[k]
        lead = (f"**{k}** · {who(c)} · at most {c['cap']} moves to HTR · {num(c['htr_med'])} HTRs and {num(c['skel_med'])} skeletons per DR (median) · reach {pct(c['reach'])}. ")
        a, b = p50(c, 'len'), p50(c, 'skel')
        lead += f"One skeleton at a time puts the first solution at place {num(b)} instead of {num(a)}. "
        m50 = min(KS, key=lambda j: (p50(c, f'two{j}'), j))
        lead += f"Of the two-pass orders, {m50} per skeleton has the best median place ({num(p50(c, f'two{m50}'))})"
        if p95(c, 'len') is not None:
            m95 = min(KS, key=lambda j: (p95(c, f'two{j}') is None, p95(c, f'two{j}') or 0, j))
            lead += f", and {m95} per skeleton needs the fewest HTRs for 95% ({num(p95(c, f'two{m95}'))}, against {num(p95(c, 'len'))} by HTR length)."
        else:
            lead += '.'
        w(lead)
        w()
        w('| Order | Median place | HTRs to finish for 95% |')
        w('|---|---|---|')
        for key, name in ROWS:
            w(f"| {name} | {num(p50(c, key))} | {num(p95(c, key))} |")
        w()

# ------------------------------------------------------------------------------------------------------------ section 2
FIRSTK = Lm[ORDER[0]]['first']
PEN_ROWS = [('3', 'P ≤ 1, P+S+T ≤ 3'), ('4', 'P ≤ 1, P+S+T ≤ 4'), ('5', 'P ≤ 1, P+S+T ≤ 5'), ('6', 'P ≤ 1, P+S+T ≤ 6'), ('none', 'P ≤ 1')]
PEN_NAME = dict(PEN_ROWS)
def cap_rows(k):
    """The rows of a corner case's table: (kind, key, name, numbers).  kind: 'moves', 'extra', 'both'."""
    R = Lm[k]; g = R['goal']
    rows = [('moves', str(c), f'At most {c} moves', R['abs'][str(c)]) for c in range(g - 5, g)]
    rows += [('extra', kk, nm, R['grid'][f'{kk}_{g - 1}']) for kk, nm in PEN_ROWS]
    both = [(kk, c) for kk in ('4', '5', '6') for c in (g - 2,)]
    b = best(k, 'both')
    if b and b[0] not in both: both.append(b[0])
    rows += [('both', (kk, c), f'{PEN_NAME[kk]}, at most {c} moves', R['grid'][f'{kk}_{c}']) for kk, c in sorted(both, key=lambda x: (-x[1], PEN_ROWS.index((x[0], PEN_NAME[x[0]]))))]
    return rows
def best(k, kind):
    """The cap of this kind with the fewest HTRs per DR that still reaches 95% of within-goal DRs: (key, numbers), or None."""
    R = Lm[k]; g = R['goal']
    if kind == 'moves': cand = [(str(c), R['abs'][str(c)]) for c in range(g - 5, g)]
    elif kind == 'extra': cand = [(kk, R['grid'][f'{kk}_{g - 1}']) for kk, _ in PEN_ROWS]
    else: cand = [((kk, c), R['grid'][f'{kk}_{c}']) for kk, _ in PEN_ROWS for c in range(g - 5, g - 1)]
    cand = [x for x in cand if round(100 * x[1]['reach'], 1) >= 95.0]          # 95% as the tables print it
    return min(cand, key=lambda x: (x[1]['htr_med'], x[1]['n'])) if cand else None
def best_name(k, kind):
    b = best(k, kind)
    if b is None: return '—'
    if kind == 'moves': return f'{b[0]} moves'
    if kind == 'extra': return PEN_NAME[b[0]]
    return f'{PEN_NAME[b[0][0]]}, {b[0][1]} moves'

w('## 2. Which HTRs: the choice of cap')
w()
w('This section compares three kinds of cap. All of them leave out the HTRs G moves away.')
w()
w('- **A cap on the moves.** Every HTR at most c moves away, whatever its extra moves. This is the standard meta\'s cap.')
w('- **A cap on the extra moves.** Every HTR with P ≤ 1 and P+S+T ≤ k. The page uses k = 5.')
w('- **Both.** P ≤ 1 and P+S+T ≤ k, and at most c moves away, for c under G−1.')
w()
w('The HTRs come from normal, inverse and the premove pass, as in section 1. How to read the columns:')
w()
w('- **HTRs per DR.** The HTRs the cap keeps, as a median over all the corner case\'s DRs, within-goal or not. It is what gets finished on a DR where nothing fits the goal.')
w('- **Reach.** The share of within-goal DRs where at least one kept HTR has a finish within the goal.')
w(f'- **Median place.** As in section 1, with the order chosen there: one skeleton at a time, two passes, {FIRSTK} per skeleton in the first. A dash means fewer than half of the within-goal DRs are reached.')
w()
w('In each table the rows in bold are, for each kind of cap, the one with the fewest HTRs per DR that still reaches 95% of within-goal DRs. This table collects them.')
w()
w('| Corner case | Cap on the moves | Its HTRs per DR | Its reach | Cap on the extra moves | Its HTRs per DR | Its reach | Both | Their HTRs per DR | Their reach |')
w('|---|---|---|---|---|---|---|---|---|---|')
BEST = {k: {kind: best(k, kind) for kind in ('moves', 'extra', 'both')} for k in ORDER}
for k in ORDER:
    cells = []
    for kind in ('moves', 'extra', 'both'):
        b = BEST[k][kind]
        cells += [best_name(k, kind), num(b[1]['htr_med']) if b else '—', pct(b[1]['reach']) if b else '—']
    w(f'| {k} | ' + ' | '.join(cells) + ' |')
w()
w('A dash means no cap of that kind reaches 95%.')
w()
BIGS = [k for k in ORDER if Lm[k]['wg'] >= 100 and BEST[k]['moves'] and BEST[k]['extra']]
assert BIGS == [k for k in ORDER if Lm[k]['wg'] >= 100], 'written for corner cases where both single caps can reach 95%'
r_em = {k: BEST[k]['extra'][1]['htr_med'] / BEST[k]['moves'][1]['htr_med'] for k in BIGS}
fewer = [k for k in BIGS if r_em[k] < 0.995]; more = [k for k in BIGS if r_em[k] > 1.005]
def names(ks): return ', '.join(ks[:-1]) + (' and ' if len(ks) > 1 else '') + ks[-1]
S2A = (f"At 95% reach, the cap on the extra moves needs fewer HTRs than the cap on the moves in {len(fewer)} of the {len(BIGS)} corner cases with at least 100 within-goal DRs ({names(fewer)})"
       + (f", and more in {len(more)} ({names(more)})" if more else '') + f": {span(list(r_em.values()), lambda v: pct(v, 0))} as many.")
w(f"**Alone, neither cap wins everywhere.** {S2A}")
w()
BOTHS = [k for k in ORDER if Lm[k]['wg'] >= 100 and BEST[k]['both']]
r_b = {k: BEST[k]['both'][1]['htr_med'] / min(BEST[k]['moves'][1]['htr_med'], BEST[k]['extra'][1]['htr_med']) for k in BOTHS}
assert max(r_b.values()) < 1
rest = [k for k in BIGS if k not in BOTHS]
S2B = (f"In {len(BOTHS)} of those corner cases ({names(BOTHS)}) the cap on the moves can go under G−1 with the cap on the extra moves in place and still leave 95% reach. "
       f"The pair then keeps {span(list(r_b.values()), lambda v: pct(v, 0))} of the HTRs of the better single cap."
       + (f" On {names(rest)} it cannot: G−2 moves reaches under 95% whatever the extra moves." if rest else ''))
w(f"**Together they need the fewest HTRs.** {S2B}")
w()
dp = {}
for k in ORDER:
    v = [x[1]['p50'] for x in BEST[k].values() if x and x[1]['p50'] is not None]
    if len(v) > 1: dp[k] = (max(v) - min(v), min(v), max(v))
kd = max(dp, key=lambda k: dp[k][0])
w('**The cap moves the first solution little.** Between the bold rows of a corner case, the median place '
  + ('is the same.' if dp[kd][0] == 0 else f'differs by {dp[kd][0]} at most ({kd}: {dp[kd][1]} to {dp[kd][2]}).'))
w()
for m in MS:
    w(f'### {m}qt DRs (goal {GOAL[m]})')
    w()
    for k in BYQT[m]:
        R = Lm[k]
        bold = {(kind, BEST[k][kind][0]) for kind in BEST[k] if BEST[k][kind]}
        none = [nm_ for kind, nm_ in (('moves', 'the moves'), ('extra', 'the extra moves')) if not BEST[k][kind]]
        lead = f"**{k}** · {who(R)}. "
        parts = []
        if BEST[k]['moves']: parts.append(f"at most {best_name(k, 'moves')} ({num(BEST[k]['moves'][1]['htr_med'])} HTRs per DR)")
        if BEST[k]['extra']: parts.append(f"{best_name(k, 'extra')} ({num(BEST[k]['extra'][1]['htr_med'])})")
        if BEST[k]['both']:
            b = BEST[k]['both'][0]
            parts.append(f"{PEN_NAME[b[0]]} with at most {b[1]} moves ({num(BEST[k]['both'][1]['htr_med'])})")
        if parts:
            lead += 'The tightest caps with 95% reach: ' + '; '.join(parts[:-1]) + ('; and ' if len(parts) > 1 else '') + parts[-1] + '.'
            if not BEST[k]['both']: lead += f" With at most {R['goal'] - 2} moves no cap reaches 95%."
        else:
            lead += 'No cap reaches 95% of the within-goal DRs here, so no row is in bold.'
        w(lead)
        w()
        w('| Cap | HTRs per DR (median) | Reach | Median place |')
        w('|---|---|---|---|')
        for kind, key, name, e in cap_rows(k):
            cells = [name, num(e['htr_med']), pct(e['reach']), num(e['p50'])]
            if (kind, key) in bold: cells = [f'**{x}**' for x in cells]
            w('| ' + ' | '.join(cells) + ' |')
        w()

# ------------------------------------------------------------------------------------------------------------ section 3
w('## 3. NISS')
w()
w('The HTRs above come from normal, inverse and the page\'s premove pass. The standard meta has a NISS of its own: one NISS after a start of 1 to 3 moves '
  '(a quarter turn; a side half turn and a quarter turn; a U-layer move, a side half turn and a quarter turn). '
  f'This section counts what each adds, in the order of section 2: one skeleton at a time, two passes, {FIRSTK} per skeleton in the first.')
w()
w('Where a NISS HTR goes in that order:')
w()
w('- **Its skeleton** is the one its whole solution is on when written on one side: the path, the finish, then the start undone. After a start, P, S and T are read on the skeleton of what is left, as in the premove pass, and the start\'s moves count in the moves to HTR.')
w('- **After a single quarter turn**, the start is a premove: the HTR comes before the linear HTRs of its skeleton. The premove pass is this NISS on skeletons with 3 or more quarter turns, leaving out what the premove alone solves.')
w(f'- **After a longer start**, the HTR comes after all the linear HTRs of its skeleton, and never in the first pass: the first pass is for the {FIRSTK} nearest HTRs of the premove and the linear check.')
w()
NOPT = [('none', 'none'), ('premove', 'the premove pass'), ('n1', 'after 1 move'), ('n2', 'after up to 2 moves'), ('n3', 'after up to 3 moves')]
for cap, title, lead in (('abs', 'With the cap on the moves alone', 'This table has every HTR at most G−1 moves away, whatever its extra moves.'),
                         ('pen', 'With the page\'s cap on the extra moves', 'This table has the HTRs with P ≤ 1 and P+S+T ≤ 5 that are at most G−1 moves away.')):
    w(f'### {title}')
    w()
    w(lead)
    w()
    w('| Corner case | NISS | HTRs per DR (median) | Reach | Median place |')
    w('|---|---|---|---|---|')
    for k in ORDER:
        for key, nm_ in NOPT:
            e = Lm[k]['niss'][cap]['late'][key]
            w(f"| {k} | {nm_} | {num(e['htr_med'])} | {pct(e['reach'])} | {num(e['p50'])} |")
    w()
BIGN = [k for k in ORDER if Lm[k]['wg'] >= 100]
def nr(cap, a, b, key):
    """Option b against option a of the NISS tables, as ratios over the larger corner cases."""
    return [Lm[k]['niss'][cap]['late'][b][key] / Lm[k]['niss'][cap]['late'][a][key] for k in BIGN]
def nd(cap, a, b):
    """Largest change of the median place between two options, over all corner cases."""
    v = [abs(Lm[k]['niss'][cap]['late'][b]['p50'] - Lm[k]['niss'][cap]['late'][a]['p50']) for k in ORDER if Lm[k]['niss'][cap]['late'][a]['p50'] is not None and Lm[k]['niss'][cap]['late'][b]['p50'] is not None]
    return max(v)
w(f"**A NISS after 1 move is the premove pass without its conditions.** Under the page's cap it keeps {span(nr('pen', 'premove', 'n1', 'htr_med'), lambda v: f'{v:.2f}x')} the HTRs of the pass in the corner cases with at least 100 within-goal DRs, "
  f"and moves the median place by {nd('pen', 'premove', 'n1')} at most.")
w()
# the other way to place them: a longer start's HTRs fill the first pass of a skeleton with fewer than FIRSTK others
fill = {(k, cap): Lm[k]['niss'][cap]['n3']['p50'] - Lm[k]['niss'][cap]['late']['n3']['p50'] for k in ORDER for cap in ('abs', 'pen')
        if Lm[k]['niss'][cap]['n3']['p50'] is not None and Lm[k]['niss'][cap]['late']['n3']['p50'] is not None}
worst = max(fill, key=lambda x: fill[x])
dmed = max(nd('pen', 'premove', 'n3'), nd('abs', 'premove', 'n3'))
w(f"**A longer start adds HTRs and leaves the first solution where it is.** A NISS after up to 3 moves keeps {span(nr('pen', 'premove', 'n3', 'htr_med'), lambda v: f'{v:.1f}x')} the HTRs of the premove pass under the page's cap, "
  f"and {span(nr('abs', 'premove', 'n3', 'htr_med'), lambda v: f'{v:.1f}x')} under the cap on the moves alone. "
  + ('The median place is the same in every corner case' if dmed == 0 else f'The median place moves by {dmed} at most') + ', since those HTRs come in the second pass. '
  + (f"If they were let into the first pass of a skeleton with fewer than {FIRSTK} other HTRs, the first solution would come later: on {worst[0]} at place {num(Lm[worst[0]]['niss'][worst[1]]['n3']['p50'])} instead of {num(Lm[worst[0]]['niss'][worst[1]]['late']['n3']['p50'])}." if fill[worst] > 0 else
     f"Letting them into the first pass of a skeleton with fewer than {FIRSTK} other HTRs changes no median place."))
w()

# ------------------------------------------------------------------------------------------------------------ method
w('## How it was counted')
w()
w('- **HTRs.** On both sides of every DR, every HTR in reach on a skeleton with the DR\'s quarter turns or two more; the HTRs of the premove pass; and in section 3 the HTRs after each NISS start, with the whole path on the DR\'s quarter turns or two more. '
  'In reach means the moves to HTR plus the corner moves left after it fit the goal. An HTR is one path up to how its U and D layer turns are written, with the best finish among those. Only the HTRs at most G−1 moves away are used.')
w('- **The same HTRs as the page.** They are read from a list that also has, for each HTR, the skeleton of its whole solution. The list is checked against the page\'s records DR by DR: on normal and inverse it has the same HTRs, and its premove pass is the page\'s.')
w('- **Moves to HTR.** The length of the path, a premove or the start before a NISS included.')
w('- **Skeletons.** Two HTRs are on the same skeleton when they are on the same side and in the same corner case at every quarter turn. After a premove or another start, the corner cases are those of the whole solution written on the side of the path, which ends with the start undone. L is the skeleton\'s length.')
w('- **Ties.** HTRs equally far go most pairs first, the pairs counted right after the last insertion as on the page. Skeletons of one length, and HTRs still tied, are taken in random order; every place is taken over 20 such orders.')
w('- **Median place and HTRs for 95%.** The number of HTRs finished by which 50% and 95% of within-goal DRs have a within-goal finish, over the DRs and the random orders.')
w('- **Finish.** The shortest leave-slice finish in half turns from the HTR, from an exact table.')
w()

# the summary above the tables
BIG = [k for k in ORDER if S[k]['wg'] >= 100]
r50 = {k: p50(S[k], 'skel') / p50(S[k], 'len') for k in BIG}
ok95 = [k for k in BIG if p95(S[k], 'len') is not None and p95(S[k], 'skel') is not None]
r95 = {k: p95(S[k], 'skel') / p95(S[k], 'len') for k in ok95}
sm = []
sm.append(f"**One skeleton at a time costs a lot.** In the corner cases with at least 100 within-goal DRs, the first solution comes {span(list(r50.values()), lambda v: f'{v:.0f}x')} later (median place), "
          f"and 95% of within-goal DRs take {span(list(r95.values()), lambda v: f'{v:.0f}x')} as many HTRs.")
# two passes: how close each k comes to the order by HTR length
best50 = {j: [p50(S[k], f'two{j}') / p50(S[k], 'len') for k in BIG] for j in KS}
best95 = {j: [p95(S[k], f'two{j}') / p95(S[k], 'len') for k in ok95 if p95(S[k], f'two{j}') is not None] for j in KS}
sm.append('**Two passes get the median back, and part of the 95%.** What the first pass doesn\'t find is left to the second pass, which is one skeleton at a time again. So a larger first pass brings the 95% point in and pushes the median out. '
          'This table shows each first-pass size against the order by HTR length, over the same corner cases: how much later the first solution comes, and how many more HTRs it takes for 95%.')
w_tab = ['| First pass | Median place, against by HTR length | HTRs for 95%, against by HTR length |', '|---|---|---|']
for j in KS:
    w_tab.append(f"| {j} per skeleton | {span(best50[j], lambda v: f'{v:.1f}x')} | {span(best95[j], lambda v: f'{v:.1f}x')} |")
w_tab.append(f"| One skeleton at a time | {span(list(r50.values()), lambda v: f'{v:.1f}x')} | {span(list(r95.values()), lambda v: f'{v:.1f}x')} |")
out[SUM:SUM] = [sm[0], '', sm[1], ''] + w_tab
# the short version (SHORT comes before SUM, so this goes in second)
n3p = nr('pen', 'premove', 'n3', 'htr_med')
sv = [f"- **By hand, two passes cost little on the first solution and more on the tail.** Going through one skeleton at a time puts the first solution {span(list(r50.values()), lambda v: f'{v:.0f}x')} later than finishing by HTR length. "
      f"With a first pass of {FIRSTK} HTRs per skeleton it comes {span(best50[FIRSTK], lambda v: f'{v:.1f}x')} later, and getting to 95% of within-goal DRs takes {span(best95[FIRSTK], lambda v: f'{v:.1f}x')} as many HTRs (section 1).",
      f"- **Neither cap wins alone, and together they need the fewest HTRs.** At 95% reach, the cap on the extra moves needs fewer HTRs than the cap on the moves in {len(fewer)} of the {len(BIGS)} corner cases with at least 100 within-goal DRs"
      + (f", and more in {len(more)}" if more else '') + f". Where the cap on the moves can also go under G−1 ({names(BOTHS)}), the pair keeps {span(list(r_b.values()), lambda v: pct(v, 0))} of the HTRs of the better single cap (section 2).",
      f"- **More NISS adds HTRs, not earlier solutions.** A NISS after 1 move is the premove pass without its conditions. One after up to 3 moves keeps {span(n3p, lambda v: f'{v:.1f}x')} the HTRs under the page's cap, "
      + ('and the median place stays where it is' if dmed == 0 else f'and moves the median place by {dmed} at most') + ' (section 3).']
out[SHORT:SHORT] = sv
open(sys.argv[1], 'w').write('\n'.join(out) + '\n')
print('written', sys.argv[1], len(out), 'lines')
