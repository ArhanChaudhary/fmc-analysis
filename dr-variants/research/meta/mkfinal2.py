"""Markdown for the skeleton/variant meta doc at S+T <= 4 (from ../out/meta/final{2,3,4}_st4.json, and the S+T <= 3
JSON for the comparison).  usage: mkfinal2.py OUTDIR -> sec1.md sec2.md appA.md appB.md appC.md full.md"""
import sys, json, os
J = {m: json.load(open(f'../out/meta/final{m}_st4.json')) for m in (2, 3, 4)}
O = {m: json.load(open(f'../out/meta/final{m}.json')) for m in (2, 3, 4)}
GOAL = {2: 12, 3: 13, 4: 14}
ORDER = {2: ['4a2', '4b2'], 3: ['0c3', '2c3', '4c3'], 4: ['0c4', '2c4', '4c4']}
ALL = [(m, k) for m in (2, 3, 4) for k in ORDER[m]]
C = {k: J[m]['cases'][k] for m, k in ALL}
BNAME = {'none': 'Baseline (no DR Bounding)', 'simple': 'Simple', 'cca': 'Corner-case-aware', 'comp': 'Comprehensive'}
def one_in(s):
    v = 1 / s
    return f'1 in {v:.1f}' if v < 10 else f'1 in {v:,.0f}'
def pct(x, dec=0): return f'{100 * x:.{dec}f}%'
def num(x): return f'{x:,.0f}'
def who(c):
    s = f"{c['drs']:,} DRs, {c['wg']:,} within-goal"
    return s + (' (a small sample)' if c['wg'] < 100 else '')
def rng(vals, fmt='{:.0f}'):
    lo, hi = min(vals), max(vals)
    a, b = fmt.format(lo), fmt.format(hi)
    return a if a == b else f'{a}–{b}'
COLS = '| {first} | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish | Found within 5 finishes | Found within 10 finishes |\n|---|---|---|---|---|---|'
def row(name, b, bold=False):
    n = f'**{name}**' if bold else name
    return f"| {n} | {num(b['htr_med'])} | {one_in(b['share'])} | {pct(b['miss'], 1)} | {pct(b['found']['5'])} | {pct(b['found']['10'])} |"
def disp(x): return round(100 * x)

# ---------- section 1
cca_table = """| Corners | Bad slices | Edges | N, fr = 0 | N, fr = 1 |
|---|---|---|---|---|
| HH | 0 | any | +0 | +5 |
| HH | 1 | any | +3 | +5 |
| HH | 2 | any | +6 | +6 |
| RD, FD | 0 | DH | +0 | +3 |
| RD, FD | 0 | DD | +1 | +4 |
| RD, FD | 1 | any | +3 | +5 |
| RD, FD | 2 | any | +5 | +5 |
| RV, FV | 0 | VH | +0 | +1 |
| RV, FV | 0 | VV | +1 | +2 |
| RV, FV | 1 | any | +3 | +2 |
| RV, FV | 2 | any | +5 | +5 |
| DD | 0 | DV | +0 | +0 |
| DD | 0 | VV | +1 | +1 |
| DD | 0 | DD | +2 | +2 |
| DD | 1 | any | +3 | +3 |
| DD | 2 | any | +5 | +5 |"""
rank = sorted(ALL, key=lambda mk: -C[mk[1]]['wg'] / C[mk[1]]['drs'])
rk = ['| Rank | Corner case | DR type | Within-goal DRs | The meta finds a within-goal finish | DRs in the sample |', '|---|---|---|---|---|---|']
for i, (m, k) in enumerate(rank, 1):
    c = C[k]
    rk.append(f"| {i} | {k} | {m}qt | {pct(c['wg'] / c['drs'], 1)} | {pct(c['bounds']['cca']['found_all'], 1)} | {c['drs']:,} |")
byfind = sorted(ALL, key=lambda mk: -C[mk[1]]['bounds']['cca']['found_all'])
sec1 = f"""## 1. The meta

Take skeletons shortest first, stop each one at S+T ≤ 4 with at most 1 extra move before 2qt, and finish only the variants whose corner-case-aware bound fits the goal. On both normal and inverse:

1. **Sort the attempt's DRs by corner case**, best first: the table below ranks them.
2. **Within a DR, take the skeletons shortest first**, normal and inverse mixed. Skeletons with two more quarter turns than the DR count too, and sort in by length with the rest.
3. **For each skeleton, generate the variants with S+T ≤ 4**, at most 1 of those extra moves before 2qt. On a 2qt DR, only the skeletons with two more quarter turns have moves before 2qt.
4. **Discard a variant when S+T+N > M**, with N from the corner-case-aware bound below. Finish the rest, fewest extra moves first.

The **baseline** is the same search without DR Bounding: N = 0, so it finishes every variant with S+T ≤ M.

### Corner cases by within-goal share

{rank[0][1]}, {rank[1][1]} and {rank[2][1]} DRs have a within-goal finish most often; {rank[-2][1]} and {rank[-1][1]} least. Goals differ by DR type (12 / 13 / 14 moves). Ranked by what the meta finds instead, 4b2 drops behind 4c3 and 4c4.

{chr(10).join(rk)}

- **Within-goal DRs.** The share of the case's DRs that have a within-goal finish at all.
- **The meta finds a within-goal finish.** The share of the case's DRs where the meta's HTRs include one.

### Terms

- **Goal.** A leave-slice finish in DR moves of at most 12 / 13 / 14 moves for a 2qt / 3qt / 4qt DR. A **within-goal DR** is one that has such a finish.
- **Corner case.** The DR's HTR subset: 4a2, 4b2, 0c3, 2c3, 4c3, 0c4, 2c4 or 4c4. The last digit is the quarter turns to HTR.
- **Skeleton.** A corner solution, as in Advanced DR Bounding, fixed by its side (normal or inverse), its number of quarter turns and its NISS@1qt corner case. Its variants insert slices, corner swaps and edge permutations without changing that corner case.
- **Skeleton length.** Moves of the shortest variant to HTR, plus the corner case's own moves after HTR: 0 for HH, 1 for RD and FD, 2 for RV and FV, 3 for DD. M = goal − skeleton length.
- **S+T.** A variant's extra moves over the skeleton's shortest path to HTR. It includes extra moves before 2qt, the **pre-2qt moves**, made before the skeleton has 2 quarter turns left.
- **N.** The post-HTR penalty a bound gives the variant's NISS@1qt case. A variant can only finish within goal if S+T+N ≤ M.
- **HTR.** Counted once up to the U/D choice. A route stops at the first HTR it reaches.

### The corner-case-aware bound

N depends on the NISS@1qt corner case, the number of bad slices, the edges and fr-parity. It's the table from Rodney Kinney's [*Advanced DR Bounding*](https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0) (live version, read 19 Nov 2026). A slice is bad if it holds must-avoid edges or is missing must-have edges. The doc's "+2 per reflected slice" terms are left out.

{cca_table}"""

# ---------- section 2
ratios = [C[k]['bounds']['none']['htr_med'] / C[k]['bounds']['cca']['htr_med'] for _, k in ALL]
dmiss = [100 * (C[k]['bounds']['cca']['miss'] - C[k]['bounds']['none']['miss']) for _, k in ALL]
df10 = [disp(C[k]['bounds']['cca']['found']['10']) - disp(C[k]['bounds']['none']['found']['10']) for _, k in ALL]
o = lambda m, k: O[m]['cases'][k]['bounds']['cca']
htrx = [C[k]['bounds']['cca']['htr_med'] / o(m, k)['htr_med'] for m, k in ALL]
lead2 = (f"Against the baseline, the corner-case-aware bound finishes {rng(ratios)}× fewer HTRs per DR and misses a within-goal finish at most "
         f"{max(dmiss):.1f} points more often. It finds a within-goal finish in the first 10 HTRs {rng(df10)} points more often. "
         f"Next to an S+T ≤ 3 version of the meta, it misses about half as often or less, for up to {max(htrx):.1f}× the HTRs, and a finished HTR is within goal a little less often "
         f"(2c3: {one_in(C['2c3']['bounds']['cca']['share'])} instead of {one_in(o(3, '2c3')['share'])}). The bound only prunes after 2qt, so both searches explore the same routes to 2qt.")
s2 = ["## 2. Stats for the recommended meta", lead2, "How to read the columns:",
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
        s2.append(f"**{k}** · {who(c)} · {num(c['routes_meta'])} routes to 2qt per DR (median, both searches). "
                  f"The bound finishes {b0['htr_med'] / b1['htr_med']:.0f}× fewer HTRs with {miss}. It finds a within-goal finish in the first 10 for "
                  f"{pct(b1['found']['10'])} of within-goal DRs against {pct(b0['found']['10'])}.")
        s2.append(COLS.format(first='Search') + '\n' + row(BNAME['none'], b0) + '\n' + row(BNAME['cca'], b1, True))
M = {k: C[k]['miss'] for _, k in ALL}
mt = ['| Corner case | Missed, DR\'s own quarter turns only | Missed, with two more (the meta) | Needs S+T 5 | Needs a second pre-2qt move | Needs S+T 6 or more | Lost to the bound | Needs four more quarter turns |',
      '|---|---|---|---|---|---|---|---|']
for m, k in ALL:
    x = M[k]; w = C[k]['wg']
    mt.append(f"| {k} | {pct(x['own'], 1)} | {pct(x['meta'], 1)} | {pct(x['next'] / w, 1)} | {pct(x['pre2'] / w, 1)} | {pct(x['more'] / w, 1)} | {pct(x['bound'] / w, 1)} | {pct(x['beyond'] / w, 1)} |")
s2 += ['### Where the misses come from',
       f"Skeletons with two more quarter turns are part of the meta. Without them, 4b2 would miss {pct(M['4b2']['own'], 1)} of the time instead of {pct(M['4b2']['meta'], 1)}, "
       f"and 4c3 {pct(M['4c3']['own'], 1)} instead of {pct(M['4c3']['meta'], 1)}. What's left splits between S+T 5 and a second pre-2qt move. "
       f"Skeletons with four more quarter turns would save at most {max(M[k]['beyond'] for _, k in ALL)} DRs in any case.",
       "Each missed DR is filed under its cheapest within-goal HTR anywhere in the data: fewest S+T, then fewest pre-2qt moves. "
       "Cells are shares of within-goal DRs, and the five columns on the right add up to the meta's chance of missing, up to rounding.",
       '\n'.join(mt)]
sec2 = '\n\n'.join(s2)

# ---------- appendix A
g1 = [C[k]['bounds']['cca']['share'] / C[k]['bounds']['none']['share'] for _, k in ALL]
g2 = [C[k]['bounds']['comp']['share'] / C[k]['bounds']['cca']['share'] for _, k in ALL]
sd = [100 * (C[k]['bounds']['simple']['miss'] - C[k]['bounds']['none']['miss']) for _, k in ALL]
sA = ["## Appendix A. Varying the bound",
      f"Comprehensive adds only {rng(g2, '{:.1f}')}× on top of corner-case-aware, where corner-case-aware gains {rng(g1)}× over the baseline, so the meta keeps the middle path. "
      "Here S+T ≤ 4 with at most 1 pre-2qt move is fixed and the bound varies: none (the baseline), simple, corner-case-aware and comprehensive. "
      f"Simple misses up to {max(sd):.1f} points more often than the baseline, because one of its cells is too strict (appendix C)."]
for m in (2, 3, 4):
    sA.append(f'### {m}qt DRs (goal {GOAL[m]})')
    for k in ORDER[m]:
        Bb = C[k]['bounds']
        sA.append(f"**{k}** · {who(C[k])}. Corner-case-aware makes a finished HTR {Bb['cca']['share'] / Bb['none']['share']:.1f}× likelier to be within goal than the baseline does; "
                  f"comprehensive adds {Bb['comp']['share'] / Bb['cca']['share']:.1f}× on top.")
        sA.append(COLS.format(first='Bound') + '\n' + '\n'.join(row(BNAME[b], Bb[b], b == 'cca') for b in ['none', 'simple', 'cca', 'comp']))
appA = '\n\n'.join(sA)

# ---------- appendix B
G = {k: C[k]['grid'] for _, k in ALL}
moved5 = [k for _, k in ALL if G[k]['5,1']['miss'] < G[k]['4,1']['miss'] - 1e-9]
FAM = ['4b2', '2c3', '2c4']
r5 = [G[k]['5,1']['routes'] / G[k]['4,1']['routes'] for k in FAM]
h5 = [G[k]['5,1']['htr_med'] / G[k]['4,1']['htr_med'] for k in FAM]
r2 = [G[k]['4,2']['routes'] / G[k]['4,1']['routes'] for k in FAM]
sB = ["## Appendix B. Varying S+T and the pre-2qt moves",
      f"S+T ≤ 5 at 1 pre-2qt move cuts the misses further for the familiar cases (4b2 {pct(G['4b2']['4,1']['miss'], 1)} → {pct(G['4b2']['5,1']['miss'], 1)}, "
      f"2c3 {pct(G['2c3']['4,1']['miss'], 1)} → {pct(G['2c3']['5,1']['miss'], 1)}, 2c4 {pct(G['2c4']['4,1']['miss'], 1)} → {pct(G['2c4']['5,1']['miss'], 1)}) "
      f"for {rng(r5, '{:.1f}')}× the routes to 2qt and up to {max(h5):.1f}× the HTRs. A second pre-2qt move at S+T ≤ 4 does about as much, "
      f"but costs {rng(r2, '{:.1f}')}× the routes for those three. Allowing no pre-2qt move costs the most: 2c4 misses {pct(G['2c4']['4,0']['miss'], 1)} of the time instead of {pct(G['2c4']['4,1']['miss'], 1)}.",
      "Each table fixes the corner-case-aware bound and varies S+T (2 to 5) and the pre-2qt moves. The meta's row is in bold. "
      "At S+T ≤ 2, \"at most 2\" pre-2qt moves is the same as no limit and isn't shown."]
for m in (2, 3, 4):
    sB.append(f'### {m}qt DRs (goal {GOAL[m]})')
    for k in ORDER[m]:
        a, b = G[k]['4,1'], G[k]['5,1']
        if pct(a['miss'], 1) == pct(b['miss'], 1) and num(a['htr_med']) == num(b['htr_med']):
            tail = f"S+T ≤ 5 at 1 pre-2qt move changes nothing here: the chance of missing stays at {pct(a['miss'], 1)}."
        elif pct(a['miss'], 1) == pct(b['miss'], 1):
            tail = (f"S+T ≤ 5 at 1 pre-2qt move leaves the chance of missing at {pct(a['miss'], 1)} and finishes "
                    f"{num(b['htr_med'])} HTRs per DR instead of {num(a['htr_med'])}.")
        else:
            rt = (f"the same {num(a['routes'])} routes to 2qt" if num(a['routes']) == num(b['routes'])
                  else f"{num(b['routes'])} routes to 2qt instead of {num(a['routes'])}")
            tail = f"Going from S+T ≤ 4 to S+T ≤ 5 at 1 pre-2qt move takes the chance of missing from {pct(a['miss'], 1)} to {pct(b['miss'], 1)} for {rt}."
        sB.append(f"**{k}** · {who(C[k])}. " + tail)
        rows = ['| S+T at most | Pre-2qt moves at most | Routes to 2qt per DR (median) | HTRs to finish per DR (median) | Within goal | Chance of missing a within-goal finish |',
                '|---|---|---|---|---|---|']
        for kk in (2, 3, 4, 5):
            for aa in (0, 1, 2, 9):
                key = f'{kk},{aa}'
                if key not in G[k]: continue
                s = G[k][key]
                cells = [str(kk), 'no limit' if aa == 9 else str(aa), num(s['routes']), num(s['htr_med']), one_in(s['share']), pct(s['miss'], 1)]
                if (kk, aa) == (4, 1): cells = [f'**{v}**' for v in cells]
                rows.append('| ' + ' | '.join(cells) + ' |')
        sB.append('\n'.join(rows))
appB = '\n\n'.join(sB)

# ---------- appendix C
cost = ['| Bound | DRs | Within-goal HTRs the cell discards | Within-goal DRs it loses |', '|---|---|---|---|']
for b, name in [('simple', 'Simple'), ('cca', 'Corner-case-aware'), ('comp_raw', 'Comprehensive, as written')]:
    for m in (2, 3, 4):
        h = sum(C[k]['cells'][b]['htrs'] for k in ORDER[m]); dl = sum(C[k]['cells'][b]['drs_lost'] for k in ORDER[m])
        cost.append(f'| {name} | {m}qt | {h:,} | {dl} |')
appC = f"""## Appendix C. Data and method

Every number above comes from an exhaustive search of random DRs, with each HTR's finish taken from an exact table.

- **Sample.** 2,000 uniformly random DR states each with 2, 3 and 4 quarter turns to HTR. 40 of the 2qt states are 0c0 up to a turn of both layers and are dropped, leaving 1,960.
- **Search.** On both sides, every HTR in reach of every skeleton with the DR's quarter turns or two more, up to 6. In reach means S+T ≤ M. The S+T and pre-2qt limits of each table are applied on top.
- **Finish.** The shortest leave-slice finish in DR moves from that HTR, from an exact table. An HTR is within goal when its moves plus that finish fit the goal.
- **Order of finishing.** Shortest skeleton first, then fewest extra moves. Ties are taken in random order, and the found-within-N shares are expected values over that order.
- **Routes to 2qt.** Distinct move sequences, on either side, up to the point where the skeleton has 2 quarter turns left, that lead to at least one HTR the table's limits allow. They're counted before any bound, so they don't depend on it.
- **Bounds.** All three are from the live *Advanced DR Bounding*, without the reflection terms. Simple is +0 / +3 / +5 for 0 / 1 / 2 bad slices. Corner-case-aware is the table in section 1. Comprehensive is the doc's cs/fr rules with two readings. For DD corners with DV edges, "good cs-parity" takes the doc's per-case sheet value: good is F-D R-V with cs 0, or F-V R-D with cs 1. Its HH cell below is set to +0.

### Cells that are too strict

Each bound has one cell whose N is a move more than the case's shortest finish needs, checked against all 216 NISS@1qt cases. Each example below is a real 13-move leave-slice solution of a 3qt DR that the cell discards. Each was checked on a separate cube model.

| Bound | Cell | N in the doc | N the shortest finish needs |
|---|---|---|---|
| Simple | RV or FV corners, 1 bad slice, cs/fr 1/1 | +3 | +2 |
| Corner-case-aware | RD or FD corners, 1 bad slice, cs/fr 1/1 | +5 | +4 |
| Comprehensive | HH corners, 0 bad slices, cs/fr 0/0 | +1 | +0 |

- **Simple.** DR `R2 U F2 U' F2 L2 D F2 U' R2 D' L2` (2c3). On normal, `U F2 U L2 U L2 U L2 U` reaches HTR in 9 with FV corners, 1 bad slice and cs/fr 1/1, and `L2 U2 F2 R2` finishes in 4: 2 corner moves plus 2. The bound says 9 + 2 + 3 = 14. The doc itself flags this case as the 1% where the simple bound fails.
- **Corner-case-aware.** DR `U L2 U2 B2 D2 F2 L2 U' B2 D' R2 U2` (2c3). On normal, `R2 U' R2 B2 U' R2 B2 U'` reaches HTR in 8 with RD corners, 1 bad slice and cs/fr 1/1, and `B2 U2 L2 F2 D2` finishes in 5: 1 corner move plus 4. The bound says 8 + 1 + 5 = 14.
- **Comprehensive.** DR `D2 L2 F2 D' F2 R2 U2 R2 D' F2 U L2` (4c3). On inverse, `U2 R2 F2 U F2 U' F2 U L2 F2 U' B2 U'` solves the cube in 13: the HTR it reaches is already solved. The bound says 13 + 0 + 1 = 14. Every within-goal HTR this cell discards is a solution like this one, reached as an HTR with nothing left to do.

What each cell costs inside the meta (S+T ≤ 4, at most 1 pre-2qt move). The comprehensive rows are for the doc as written; the tables above use +0 for its cell, so they lose nothing.

{chr(10).join(cost)}

### Left out of the meta

- **Reflection penalties.** The doc's "+2 per reflected slice" terms aren't tracked here.
- **cs-parity.** Only the comprehensive bound needs it, and checking it during a solve is slow.
- **Pair count at the trigger.** The number of pairs at the quarter turn from 2qt to 1qt was looked at as a further sort for 2c3 DRs with RD corners. It's kept as a note, not part of the meta."""

out = sys.argv[1]
for name, txt in [('sec1', sec1), ('sec2', sec2), ('appA', appA), ('appB', appB), ('appC', appC)]:
    open(os.path.join(out, name + '.md'), 'w').write(txt.strip() + '\n')
full = '# The skeleton/variant meta\n\n19 Nov 2026\n\n' + '\n\n'.join([sec1, sec2, appA, appB, appC]) + '\n'
open(os.path.join(out, 'full.md'), 'w').write(full)
assert 'solvable' not in full.lower(), [l for l in full.split('\n') if 'solvable' in l.lower()][:3]
print('ok', len(full.encode()))
