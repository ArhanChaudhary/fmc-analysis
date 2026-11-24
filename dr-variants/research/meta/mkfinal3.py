"""Section 2 of the skeleton/variant meta doc with per-case S+T limits: 4b2 and 2c3 at S+T <= 5, the rest at
S+T <= 4 (all at most 1 pre-2qt move).  usage: mkfinal3.py OUT.md"""
import sys, json
KLIM = {'4b2': 5, '2c3': 5}
J = {(m, K): json.load(open(f'../out/meta/final{m}_st{K}.json')) for m in (2, 3, 4) for K in (4, 5) if not (m == 4 and K == 5)}
O = {m: json.load(open(f'../out/meta/final{m}.json')) for m in (2, 3, 4)}
GOAL = {2: 12, 3: 13, 4: 14}
ORDER = {2: ['4a2', '4b2'], 3: ['0c3', '2c3', '4c3'], 4: ['0c4', '2c4', '4c4']}
ALL = [(m, k) for m in (2, 3, 4) for k in ORDER[m]]
KOF = {k: KLIM.get(k, 4) for _, k in ALL}
C = {k: J[(m, KOF[k])]['cases'][k] for m, k in ALL}
def one_in(s):
    v = 1 / s
    return f'1 in {v:.1f}' if v < 10 else f'1 in {v:,.0f}'
def pct(x, dec=0): return f'{100 * x:.{dec}f}%'
def num(x): return f'{x:,.0f}'
def who(c):
    return f"{c['drs']:,} DRs, {c['wg']:,} within-goal" + (' (a small sample)' if c['wg'] < 100 else '')
def rng(vals, fmt='{:.0f}'):
    a, b = fmt.format(min(vals)), fmt.format(max(vals))
    return a if a == b else f'{a}–{b}'
disp = lambda x: round(100 * x)
COLS = '| Search | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |\n|---|---|---|---|---|---|'
def row(name, b, bold=False):
    n = f'**{name}**' if bold else name
    return f"| {n} | {num(b['htr_med'])} | {one_in(b['share'])} | {pct(b['miss'], 1)} | {pct(b['found']['5'])} | {pct(b['found']['10'])} |"
o = lambda m, k: O[m]['cases'][k]['bounds']['cca']
ratios = [C[k]['bounds']['none']['htr_med'] / C[k]['bounds']['cca']['htr_med'] for _, k in ALL]
dmiss = [100 * (C[k]['bounds']['cca']['miss'] - C[k]['bounds']['none']['miss']) for _, k in ALL]
df10 = [disp(C[k]['bounds']['cca']['found']['10']) - disp(C[k]['bounds']['none']['found']['10']) for _, k in ALL]
x5 = {k: C[k]['bounds']['cca']['htr_med'] / o(m, k)['htr_med'] for m, k in ALL}
rest = [x5[k] for _, k in ALL if KOF[k] == 4]
b4, c3 = C['4b2']['bounds']['cca'], C['2c3']['bounds']['cca']
lead = (f"Against the baseline, the corner-case-aware bound finishes {rng(ratios)}× fewer HTRs per DR and misses a within-goal finish at most "
        f"{max(dmiss):.1f} points more often. It finds a within-goal finish in the first 10 HTRs {rng(df10)} points more often. "
        "4b2 and 2c3 run to S+T ≤ 5; the other cases stop at S+T ≤ 4. "
        f"Next to an S+T ≤ 3 version of the meta, 4b2 misses {pct(b4['miss'], 1)} of the time instead of {pct(o(2, '4b2')['miss'], 1)} and 2c3 {pct(c3['miss'], 1)} instead of {pct(o(3, '2c3')['miss'], 1)}, "
        f"for {x5['4b2']:.1f}× and {x5['2c3']:.1f}× the HTRs. The other cases miss about half as often or less, for up to {max(rest):.1f}× the HTRs. "
        "The bound only prunes after 2qt, so both searches explore the same routes to 2qt.")
s2 = ["## 2. Stats for the recommended meta", lead, "How to read the columns:",
      "- **HTRs to finish per DR.** The variants the search finishes, as a median over all the case's DRs, within-goal or not.\n"
      "- **Within goal.** The share of those HTRs whose finish fits the goal.\n"
      "- **Chance of missing a within-goal finish.** The share of within-goal DRs where none of them does.\n"
      "- **Found within N finishes.** The share of within-goal DRs where one of the first N HTRs finished, in the meta's order, is within goal."]
for m in (2, 3, 4):
    s2.append(f'### {m}qt DRs (goal {GOAL[m]})')
    for k in ORDER[m]:
        c = C[k]; b0, b1 = c['bounds']['none'], c['bounds']['cca']
        dm = 100 * (b1['miss'] - b0['miss'])
        miss = 'no change in the chance of missing' if abs(dm) < 0.05 else f'a chance of missing {dm:.1f} points higher'
        s2.append(f"**{k}** · {who(c)} · S+T ≤ {KOF[k]} · {num(c['routes_meta'])} routes to 2qt per DR (median, both searches). "
                  f"The bound finishes {b0['htr_med'] / b1['htr_med']:.0f}× fewer HTRs with {miss}. It finds a within-goal finish in the first 10 for "
                  f"{pct(b1['found']['10'])} of within-goal DRs against {pct(b0['found']['10'])}.")
        s2.append(COLS + '\n' + row('Baseline (no DR Bounding)', b0) + '\n' + row('Corner-case-aware', b1, True))
M = {k: C[k]['miss'] for _, k in ALL}
mt = ["| Corner case | S+T limit | Missed, DR's own quarter turns only | Missed, with two more (the meta) | Needs 1 more S+T | Needs a second pre-2qt move | Needs 2 or more S+T beyond the limit | Lost to the bound | Needs four more quarter turns |",
      '|---|---|---|---|---|---|---|---|---|']
for m, k in ALL:
    x = M[k]; w = C[k]['wg']
    mt.append(f"| {k} | {KOF[k]} | {pct(x['own'], 1)} | {pct(x['meta'], 1)} | {pct(x['next'] / w, 1)} | {pct(x['pre2'] / w, 1)} | {pct(x['more'] / w, 1)} | {pct(x['bound'] / w, 1)} | {pct(x['beyond'] / w, 1)} |")
top = max(['next', 'pre2', 'more', 'bound', 'beyond'], key=lambda c: sum(M[k][c] for _, k in ALL))
assert top == 'pre2'
s2 += ['### Where the misses come from',
       f"Skeletons with two more quarter turns are part of the meta. Without them, 4b2 would miss {pct(M['4b2']['own'], 1)} of the time instead of {pct(M['4b2']['meta'], 1)}, "
       f"and 4c3 {pct(M['4c3']['own'], 1)} instead of {pct(M['4c3']['meta'], 1)}. What's left is mostly DRs that need a second pre-2qt move. "
       f"Skeletons with four more quarter turns would save at most {max(M[k]['beyond'] for _, k in ALL)} DRs in any case.",
       "Each missed DR the bound didn't lose is filed under its cheapest within-goal HTR anywhere in the data: fewest S+T, then fewest pre-2qt moves. "
       "Cells are shares of within-goal DRs, and the five columns on the right add up to the meta's chance of missing, up to rounding.",
       '\n'.join(mt)]
open(sys.argv[1], 'w').write('\n\n'.join(s2) + '\n')
print('ok')
