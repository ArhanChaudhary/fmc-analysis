"""Writes the comparison of the standard meta's cap with the skeleton/variant meta's, on the same HTRs in the same
order: from ../out/meta/tord.json (tord.py: per cap the HTRs per DR, reach, found within K and the place of the first
solution; what each cap keeps that the other doesn't; the checks of the standard side), the page's own numbers
(../out/meta/tfinal{M}.json) and the solutions of ../out/meta/std{M}.tsv (drvar metastd) for the examples.
Every example is replayed on an independent sticker model, read by `drvar metaread` on both sides (and after its
premove where the pass applies), and its moves to HTR are recounted from the solution's own moves.
usage: mkstd.py OUT.md [reuse]   (reuse: the examples of the last run, ../out/meta/tord_examples.json)"""
import sys, json, subprocess
import numpy as np, pandas as pd
from tcommon import drs, ORDER, BYQT, path as tpath
from tstd import load, cls
from tex import solves, inv_txt, DRVAR, insertion_cut, pairs_after

O = json.load(open(tpath('tord.json')))
ORDER = [k for k in ORDER if k in O]           # (a test run may have some DR types only)
MS = [m for m in (2, 3, 4) if any(k in O for k in BYQT[m])]
J = {m: json.load(open(tpath(f'tfinal{m}.json'))) for m in MS}
assert all(v.get('rest_both', False) for v in O.values()), 'written for the premove pass on both sides'
GOAL = {2: 12, 3: 13, 4: 14}
M = {k: m for m in MS for k in BYQT[m]}
PAGE_LINK = 'WRITEUP.md'          # the page, next to this report
PEN = 'P ≤ 1, P+S+T ≤ 5'
def pct(x, dec=1): return f'{100 * x:.{dec}f}%'
def num(x): return f'{x:,.0f}' if abs(x - round(x)) < 1e-9 else f'{x:,.1f}'
def place(x): return '—' if x is None else num(x)
def one_in(e):
    if e['nok'] == 0: return 'none'
    v = e['n'] / e['nok']
    return f'1 in {v:.1f}' if v < 10 else f'1 in {v:,.0f}'
def per_dr(e, case): return num(round(e['n'] / O[case]['drs']))
def who(case): return f"{O[case]['drs']:,} DRs, {O[case]['wg']:,} within-goal" + (' (a small sample)' if O[case]['wg'] < 100 else '')
def cap_txt(case, c, short=False):
    g = O[case]['goal']
    return f'At most {c} moves' + ('' if short or c < g else ' (every HTR in reach)')
def row(e, dec=0):
    """The six numbers of a cap, as table cells."""
    return [num(e['htr_med']), pct(e['reach']), pct(e['within'][0], dec), pct(e['within'][1], dec), pct(e['within'][2], dec), place(e['med_pos'])]
COLS = 'HTRs per DR (median) | Reach | Within 5 | Within 10 | Within 20 | Place of the first solution (median)'

QT = {'U', "U'", 'D', "D'"}
def runs(sol):
    """Lengths of the half-turn stretches of a solution, first to last."""
    r = [0]
    for mv in sol.split():
        if mv in QT: r.append(0)
        else: r[-1] += 1
    return r
def view_moves(sol):
    """Moves to HTR of this very solution, from its own moves: on normal (N), on inverse (I), and with its last
    quarter turn on normal (RN) or on inverse (RI) made first as a premove, which counts as a move; None where the
    solution doesn't end with a quarter turn on that side."""
    r = runs(sol); n = len(sol.split())
    return dict(N=n - r[-1], I=n - r[0], RN=n - r[-2] if r[-1] == 0 and len(r) > 2 else None, RI=n - r[1] if r[0] == 0 and len(r) > 2 else None)

def metaread(scr, sol, inverse=False):
    o = subprocess.run([DRVAR, 'metaread', scr, sol] + (['inverse'] if inverse else []), capture_output=True, text=True).stdout.strip().split('\t')
    d = dict(zip(o[::2], o[1::2]))
    r = dict(L=int(d['L']), q=int(d['quarter turns']), P=int(d['P']), S=int(d['S']), T=int(d['T']), N=int(d['N']), pairs=int(d['pairs']))
    # the pairs right after the last insertion, counted again on the stickers
    cut = insertion_cut(sol, [int(v) for v in d['sections'].split(',')][:-1])
    assert pairs_after(scr, 'I' if inverse else 'N', cut) == r['pairs'], 'pairs: the tool and the stickers disagree'
    return r
def tup(r): return (f"(P, S, T, N) = ({r['P']}, {r['S']}, {r['T']}, {r['N']})" if r['q'] >= 3 else f"(S, T, N) = ({r['S']}, {r['T']}, {r['N']})")
def pass_read(scr, sol, inverse):
    """The premove pass on this side of a solution that ends there with a quarter turn: that turn first, then the DR of
    this side, is the left-over DR; the rest of the solution solves it and is read on its own.  L counts the premove."""
    mv = sol.split()
    assert mv[-1] in QT
    rscr = mv[-1] + ' ' + (inv_txt(scr) if inverse else scr); rsol = ' '.join(mv[:-1])
    assert solves(rscr, 'N', rsol)
    r = metaread(rscr, rsol); r['L'] += 1; r['turn'] = mv[-1]
    return r
def passes(r): return r['P'] <= 1 and r['P'] + r['S'] + r['T'] <= 5
def breaks(r):
    """What a reading has against P <= 1 and P+S+T <= 5."""
    pst = r['P'] + r['S'] + r['T']
    assert not passes(r)
    return ' and '.join(([f"P = {r['P']}"] if r['P'] > 1 else []) + ([f'P+S+T = {pst}'] if pst > 5 else []))

COL = {('N', False): 'cn', ('I', False): 'ci', ('N', True): 'rn', ('I', True): 'ri'}
VIEW = {'cn': 'N', 'ci': 'I', 'rn': 'RN', 'ri': 'RI'}
def where(view, reads):
    return {'N': 'on normal', 'I': 'on inverse'}.get(view) or f"with its last `{reads[view]['turn']}` on {'normal' if view == 'RN' else 'inverse'} as a premove"

def solution_of(c, sdr, scr, g):
    """The solution of a candidate record (tord.py) among its DR's solutions, checked on the solution itself: it
    solves the DR on the sticker model, reads as the record does on the record's side, and has its HTR where the
    record says.  Returns (solution, its readings by view, its moves to HTR by view) or None."""
    col = COL[(c['side'], c['pre'])]; view = VIEW[col]
    for r in sdr[sdr.len == c['total']].itertuples():
        k = cls(getattr(r, col))
        if k is None or (k['q'], k['L'], k['P'], k['S'], k['T'], k['total']) != (c['q'], c['L'], c['P'], c['S'], c['T'], c['total']): continue
        if cls(r.cn) is None or cls(r.ci) is None: continue          # (a solution the records have on one side only: not shown)
        sol = r.sol
        assert solves(scr, 'N', sol) and solves(scr, 'I', inv_txt(sol)) and len(sol.split()) == c['total'] <= g
        reads = {'N': metaread(scr, sol), 'I': metaread(scr, inv_txt(sol), True)}
        for v in ('N', 'I'): assert reads[v]['L'] + reads[v]['P'] + reads[v]['S'] + reads[v]['T'] + reads[v]['N'] == c['total']
        if cls(r.rn): reads['RN'] = pass_read(scr, sol, False)
        if cls(r.ri): reads['RI'] = pass_read(scr, inv_txt(sol), True)
        mv = view_moves(sol)
        own = reads.get(view)
        if own is None or (own['q'], own['L'], own['P'], own['S'], own['T']) != (c['q'], c['L'], c['P'], c['S'], c['T']) or mv[view] != c['moves']: continue
        assert all(mv[v] is not None for v in reads)
        return sol, reads, {v: mv[v] for v in reads}
    return None

def examples(m, case, d, s, info):
    """One within-goal solution only the standard cap reaches and one only the skeleton/variant cap reaches, at the
    matched cap, each on a DR where the other cap reaches nothing (tord.py's candidates)."""
    R = O[case]; g = R['goal']; cap = R['match']
    out = {}
    for kind in ('abs', 'pen'):
        for c in R[f'ex_{kind}']:
            scr = info.scramble[c['dr']]
            assert bool(d.sv_found[c['dr']]) == (kind == 'pen'), 'the solutions and the records disagree on what the skeleton/variant cap reaches'
            f = solution_of(c, s[s.dr == c['dr']], scr, g)
            if f is None: continue
            sol, reads, mv = f
            view = VIEW[COL[(c['side'], c['pre'])]]
            if kind == 'abs':
                # within the cap on the record's side, and no reading of it passes the skeleton/variant cap
                if mv[view] > cap or any(passes(x) for x in reads.values()): continue
            else:
                # the skeleton/variant cap passes it on the record's side, and it is over the standard cap everywhere
                if not passes(reads[view]) or any(v <= cap for v in mv.values()): continue
            out[kind] = dict(scramble=scr, sol=sol, len=c['total'], view=view, moves=mv, reads=reads, opt=int(info.ls[c['dr']]), cap=cap)
            break
    return out

def example_text(kind, e):
    reads, mv, view = e['reads'], e['moves'], e['view']
    if kind == 'abs':
        if tup(reads['N']) == tup(reads['I']) and reads['N']['L'] == reads['I']['L']:
            both = f"It reads {tup(reads['N'])} on {an(reads['N']['L'])} {reads['N']['L']}-move skeleton on both sides: {breaks(reads['N'])}"
        else:
            both = (f"It reads {tup(reads['N'])} on {an(reads['N']['L'])} {reads['N']['L']}-move skeleton on normal ({breaks(reads['N'])}) "
                    f"and {tup(reads['I'])} on {an(reads['I']['L'])} {reads['I']['L']}-move skeleton on inverse ({breaks(reads['I'])})")
        more = ''.join(f"; {where(v, reads)}, {tup(reads[v])} with L = {reads[v]['L']} ({breaks(reads[v])})" for v in ('RN', 'RI') if v in reads)
        return (f"`{e['scramble']}`: `{e['sol']}` solves it in {e['len']} moves, with HTR after {mv[view]} moves {where(view, reads)}. {both}{more}.")
    others = [f"{mv[v]} {where(v, reads)}" for v in ('N', 'I', 'RN', 'RI') if v in mv]
    return (f"`{e['scramble']}`: `{e['sol']}` solves it in {e['len']} moves and reads {tup(reads[view])} on {an(reads[view]['L'])} {reads[view]['L']}-move skeleton "
            f"{where(view, reads)}. Its HTR is " + ', '.join(others[:-1]) + (' and ' if len(others) > 1 else '') + others[-1] + f" moves away, and the cap is {e['cap']}.")
def an(n): return 'an' if n in (8, 11, 18) else 'a'

if __name__ == '__main__':
    dest = sys.argv[1]
    reuse = 'reuse' in sys.argv[2:]
    EX = json.load(open(tpath('tord_examples.json'))) if reuse else {}
    UNIV = EX.pop('_more_qt', None) if reuse else None
    if not reuse:
        UNIV = None
        for m in MS:
            d, s = load(m); info = drs(m)
            s['case'] = info.case.reindex(s.dr.values).values
            for case in BYQT[m]:
                EX[case] = examples(m, case, d, s, info)
                print(case, O[case]['match'], {k: (v['len'], v['view']) for k, v in EX[case].items()}, flush=True)
                # a within-goal DR the standard meta's own search reaches on normal or inverse and the records don't:
                # every solution it has there is on a skeleton with more than two quarter turns over the DR's
                g = GOAL[m]
                for dr in O[case]['own_search'][str(g)]['more_drs']:
                    sd = s[(s.dr == dr) & (s.lev0 <= g)]
                    assert len(sd) and (sd.q > m + 2).all(), ('a solution the records should have', case, dr)
                    if UNIV is None:
                        r = sd.sort_values(['len', 'sol']).iloc[0]
                        scr = info.scramble[dr]
                        assert solves(scr, 'N', r.sol) and len(r.sol.split()) == r.len <= g and sum(x in QT for x in r.sol.split()) == r.q
                        UNIV = dict(case=case, m=m, scramble=scr, sol=r.sol, len=int(r.len), q=int(r.q))
        json.dump(dict(EX, _more_qt=UNIV), open(tpath('tord_examples.json'), 'w'), indent=1, ensure_ascii=False)

    def A(case, c=None): return O[case]['abs'][str(O[case]['match'] if c is None else c)]
    def P(case, k='5'): return O[case]['pen'][k]
    C = {k: J[M[k]]['cases'][k] for k in ORDER}
    BIG = [k for k in ORDER if O[k]['wg'] >= 100]
    WG = sum(O[k]['wg'] for k in ORDER)
    out = []
    def w(s=''): out.append(s)

    # ---------------------------------------------------------------------------------------------------- intro
    w('# The standard meta against the skeleton/variant meta')
    w()
    w('24 Nov 2026')
    w()
    w(f'The [skeleton/variant meta]({PAGE_LINK}) finishes HTRs in the standard meta\'s order: fewest moves to HTR first, and the most pairs first among HTRs equally far. '
      'So the two metas differ only in which HTRs they finish at all. This report compares the two caps on the same HTRs, in that order:')
    w()
    w('- **The standard cap.** Finish every HTR at most c moves away, whatever its extra moves.')
    w('- **The skeleton/variant cap.** Finish every HTR with P ≤ 1 and P+S+T ≤ 5, however far it is. P, S and T are the extra moves before 2qt, in the setup and in the trigger, counted on the HTR\'s own skeleton as on the page.')
    w()
    w('Neither cap needs a lower bound for N, and nothing here uses one: the page\'s steps 4 and 5 are left out. An HTR is left out only when its moves plus the corner moves left after it are over the goal, under both caps. '
      'Both metas look in the same places: every skeleton on normal and on inverse, and the page\'s premove pass, where the premove counts as a move to HTR. '
      'The standard meta\'s usual NISS, in place of that pass, is in section 8.')
    w()
    w('The goal is 12/13/14 moves from DR to a leave-slice finish for 2qt/3qt/4qt DRs. The sample is the page\'s: 2,000 random DRs of each kind (1,960 for 2qt).')
    w()
    w('How to read the columns:')
    w()
    w('- **HTRs per DR.** The HTRs the cap keeps, as a median over all the corner case\'s DRs, within-goal or not. It is what gets finished on a DR where nothing fits the goal.')
    w('- **Reach.** The share of within-goal DRs where at least one kept HTR has a finish within the goal.')
    w('- **Within 5 / 10 / 20.** The share of within-goal DRs with a within-goal finish among the first 5 / 10 / 20 HTRs finished.')
    w('- **Place of the first solution.** How many HTRs are finished up to the first one within goal, as a median over within-goal DRs. A dash means fewer than half of them have one.')
    w()

    # ---------------------------------------------------------------------------------------------------- short version
    w('## Short version')
    w()
    SHORT = len(out)          # filled in below, once the sections have made their numbers
    w()

    # ---------------------------------------------------------------------------------------------------- section 1
    w('## 1. The two caps at similar numbers of HTRs')
    w()
    w('This table puts the skeleton/variant cap between the two standard caps with the nearest numbers of HTRs per DR. The corner cases are in the page\'s order, shortest skeleton first.')
    w()
    w(f'| Corner case | Cap | {COLS} |')
    w('|---|---|---|---|---|---|---|---|')
    for k in ORDER:
        R = O[k]
        lo, hi = R['below'], R['above']
        rows = []
        if lo is not None and lo != hi: rows.append((cap_txt(k, lo), A(k, lo), False))
        rows.append((f'**{PEN}**', P(k), True))
        if hi is not None: rows.append((cap_txt(k, hi), A(k, hi), False))
        for name, e, bold in rows:
            cells = row(e)
            if bold: cells = [f'**{x}**' for x in cells]
            w(f'| {k} | {name} | ' + ' | '.join(cells) + ' |')
    w()
    # found within K: the same under both caps
    near = [max(abs(a - b) for a, b in zip(A(k)['within'], P(k)['within'])) for k in ORDER]
    w(f"**How soon a solution is found is the same.** Both metas start with the same HTRs, so the cap only matters once it is reached. "
      f"At the standard cap closest in HTRs, found within 5, 10 and 20 are within {100 * max(near):.1f} points of the skeleton/variant cap's in every corner case.")
    w()
    # reach against HTRs: a standard cap that reaches at least as much with fewer HTRs, or the two neighbours
    dom = {}
    for k in ORDER:
        g = O[k]['goal']
        cs = [c for c in range(g - 5, g + 1) if A(k, c)['reach'] >= P(k)['reach'] - 1e-12 and A(k, c)['htr_med'] < P(k)['htr_med']]
        dom[k] = min(cs) if cs else None
    DOM = [k for k in ORDER if dom[k] is not None]; BET = [k for k in ORDER if dom[k] is None]
    def names(ks): return ', '.join(ks[:-1]) + (' and ' if len(ks) > 1 else '') + ks[-1]
    def span(vs, f): return f(vs[0]) if len(vs) == 1 or f(min(vs)) == f(max(vs)) else f'{f(min(vs))} to {f(max(vs))}'
    t = (f"**The caps trade reach for HTRs to finish.** In {len(DOM)} of the {len(ORDER)} corner cases ({names(DOM)}) a standard cap reaches at least as many within-goal DRs as the skeleton/variant cap with fewer HTRs per DR. ")
    if BET:
        assert all(O[k]['below'] is not None and O[k]['above'] is not None and O[k]['below'] != O[k]['above'] for k in BET)
        dlo = [P(k)['reach'] - A(k, O[k]['below'])['reach'] for k in BET]; rlo = [A(k, O[k]['below'])['htr_med'] / P(k)['htr_med'] for k in BET]
        dhi = [A(k, O[k]['above'])['reach'] - P(k)['reach'] for k in BET]; rhi = [A(k, O[k]['above'])['htr_med'] / P(k)['htr_med'] for k in BET]
        assert min(dlo) > 0 and min(dhi) > 0
        pts = lambda v: f'{100 * v:.1f}'
        t += (f"In the other {len(BET)} ({names(BET)}) it sits between two standard caps: the one below reaches {span(dlo, pts)} points less with {span(rlo, lambda v: pct(v, 0))} of the HTRs, "
              f"and the one above {span(dhi, pts)} points more with {span(rhi, lambda v: pct(v, 0))}.")
    w(t)
    w()

    # ---------------------------------------------------------------------------------------------------- section 2
    w('## 2. What each cap keeps that the other doesn\'t')
    w()
    w('This section takes the standard cap closest to the skeleton/variant cap in HTRs per DR, and splits the HTRs by which cap keeps them. '
      'Per DR is a mean over the corner case\'s DRs. Within goal is how often such an HTR has a finish within the goal.')
    w()
    w('| Corner case | Standard cap | Kept by both, per DR | Kept by both, within goal | Only the standard cap, per DR | Only the standard cap, within goal | Only the skeleton/variant cap, per DR | Only the skeleton/variant cap, within goal |')
    w('|---|---|---|---|---|---|---|---|')
    for k in ORDER:
        H = O[k]['htrs']
        w(f"| {k} | {O[k]['match']} moves | {per_dr(H['both'], k)} | {one_in(H['both'])} | {per_dr(H['abs_only'], k)} | {one_in(H['abs_only'])} | "
          + (f"{per_dr(H['pen_only'], k)} | {one_in(H['pen_only'])} |" if H['pen_only']['n'] else '0 | — |'))
    w()
    # the finish the goal leaves an HTR past the matched cap
    left = max(O[k]['goal'] - O[k]['match'] - 1 for k in ORDER if O[k]['htrs']['pen_only']['n'])
    LEFT = ('the goal leaves it no move for a finish, so it has to solve the DR as it stands' if left == 0 else
            f"the goal leaves it a finish of {left} move{'s' if left > 1 else ''} at most")
    T3 = {name: dict(n=sum(O[k]['htrs'][name]['n'] for k in ORDER), nok=sum(O[k]['htrs'][name]['nok'] for k in ORDER)) for name in ('both', 'abs_only', 'pen_only')}
    TW = {name: dict(n=sum(O[k]['htrs']['abs_only_why'][name]['n'] for k in ORDER), nok=sum(O[k]['htrs']['abs_only_why'][name]['nok'] for k in ORDER)) for name in ('P', 'P+S+T', 'both')}
    far = [O[k]['htrs']['pen_only']['n'] / P(k)['n'] for k in ORDER if O[k]['htrs']['pen_only']['n']]
    w(f"**Past the standard cap, the skeleton/variant cap keeps HTRs that are too far.** They are {span(far, lambda v: pct(v, 0))} of its HTRs where the standard cap is under the goal, "
      f"and one of them is within goal {one_in(T3['pen_only'])} times, against {one_in(T3['both'])} for an HTR both caps keep: {LEFT}.")
    w()
    worth = (T3['abs_only']['nok'] / T3['abs_only']['n']) / (T3['both']['nok'] / T3['both']['n'])
    assert 0.4 < worth < 0.7, 'written for dropped HTRs about half as often within goal as kept ones'
    w(f"**Within the standard cap, what the skeleton/variant cap drops is worth about half of what it keeps.** An HTR that only the standard cap keeps is within goal {one_in(T3['abs_only'])} times: "
      f"{one_in(TW['P'])} when it has P ≥ 2, {one_in(TW['P+S+T'])} when it has P+S+T ≥ 6, and {one_in(TW['both'])} with both.")
    w()
    w('The same split for within-goal DRs: reached by both caps, by one only, or by neither. The last columns say what the nearest within-goal HTR of a DR that only the standard cap reaches has against the skeleton/variant cap.')
    w()
    w('| Corner case | Standard cap | Within-goal DRs | Reached by both | Only the standard cap | Only the skeleton/variant cap | Neither | Only the standard cap: needs P ≥ 2 | Only the standard cap: needs P+S+T ≥ 6 | Only the standard cap: needs both |')
    w('|---|---|---|---|---|---|---|---|---|---|')
    tot = dict(both=0, abs_only=0, pen_only=0, neither=0, P=0, PST=0, bb=0)
    for k in ORDER:
        R = O[k]; x = R['cross'][str(R['match'])]; y = R['why_abs_only']
        assert sum(y.values()) == x['abs_only'] and sum(R['over_pen_only'].values()) == x['pen_only'] and sum(x.values()) == R['wg']
        w(f"| {k} | {R['match']} moves | {R['wg']:,} | {x['both']:,} | {x['abs_only']} | {x['pen_only']} | {x['neither']} | {y['P']} | {y['P+S+T']} | {y['both']} |")
        for kk in ('both', 'abs_only', 'pen_only', 'neither'): tot[kk] += x[kk]
        tot['P'] += y['P']; tot['PST'] += y['P+S+T']; tot['bb'] += y['both']
    w(f"| All | | {WG:,} | {tot['both']:,} | {tot['abs_only']} | {tot['pen_only']} | {tot['neither']} | {tot['P']} | {tot['PST']} | {tot['bb']} |")
    w()
    over = {}
    for k in ORDER:
        for v, n in O[k]['over_pen_only'].items(): over[int(v)] = over.get(int(v), 0) + n
    if tot['pen_only']:
        w(f"The {tot['pen_only']} DRs that only the skeleton/variant cap reaches have their nearest within-goal HTR "
          + ', '.join(f"{v} move{'s' if v > 1 else ''} past the standard cap ({n})" for v, n in sorted(over.items())) + '.')
        w()
    else:
        w('No within-goal DR is reached by the skeleton/variant cap only: whenever a within-goal HTR passes it past the standard cap, another one is within the cap. '
          'The DRs neither cap reaches have their within-goal solutions on skeletons with four more quarter turns than the DR, which the HTRs of this report leave out (see the end).')
        w()
    exs = [(k, kind, EX[k][kind]) for k in ORDER for kind in ('abs', 'pen') if kind in EX.get(k, {})]
    if exs:
        w('One example per corner case, where there is one. In each, the other cap reaches no within-goal HTR of the DR.')
        w()
        for kind, title in (('abs', 'Only the standard cap'), ('pen', 'Only the skeleton/variant cap')):
            rows = [(k, e) for k, kd, e in exs if kd == kind]
            if not rows: continue
            w(f'**{title}:**')
            w()
            for k, e in rows:
                w(f"- {k}, at most {e['cap']} moves. {example_text(kind, e)}")
            w()

    # ---------------------------------------------------------------------------------------------------- section 3
    w('## 3. The two caps together')
    w()
    w('The two caps cut different HTRs, so they can be used together: P ≤ 1, P+S+T ≤ 5, and at most c moves to HTR. This table takes c one move under the goal, where the standard cap alone still reaches everything it can.')
    w()
    w('| Corner case | Cap on the moves | Standard cap alone, HTRs per DR (median) | Standard cap alone, reach | Skeleton/variant cap alone, HTRs per DR (median) | Skeleton/variant cap alone, reach | Both, HTRs per DR (median) | Both, reach |')
    w('|---|---|---|---|---|---|---|---|')
    tog = {}
    for k in ORDER:
        R = O[k]; c = R['goal'] - 1; a, b, e = A(k, c), P(k), R['both'][str(c)]
        w(f"| {k} | {c} moves | {num(a['htr_med'])} | {pct(a['reach'])} | {num(b['htr_med'])} | {pct(b['reach'])} | {num(e['htr_med'])} | {pct(e['reach'])} |")
        tog[k] = dict(c=c, of_pen=e['htr_med'] / b['htr_med'], of_abs=e['htr_med'] / a['htr_med'], same=abs(e['reach'] - b['reach']) < 1e-12,
                      lost=R['cross'][str(c)]['abs_only'], full=abs(a['reach'] - A(k, R['goal'])['reach']) < 1e-12)
    w()
    assert all(v['same'] and v['full'] for v in tog.values()), 'written for a cap one move under the goal that costs neither cap any reach'
    lost1 = sum(v['lost'] for v in tog.values())
    w(f"**The cap on the moves costs the skeleton/variant cap nothing.** In every corner case it reaches the same within-goal DRs with {span([v['of_pen'] for v in tog.values()], lambda v: pct(v, 0))} of the HTRs. "
      f"**The skeleton/variant cap costs the standard cap a little.** On top of it, it keeps {span([v['of_abs'] for v in tog.values()], lambda v: pct(v, 0))} of the HTRs and gives up {lost1} of the sample's {WG:,} within-goal DRs, "
      'the ones that need P ≥ 2 or P+S+T ≥ 6 on both sides.')
    w()

    # ---------------------------------------------------------------------------------------------------- section 4
    w('## 4. Every cap, corner case by corner case')
    w()
    w('Each table has the standard cap at six values, the skeleton/variant cap with P+S+T ≤ 3 to 6 and with P ≤ 1 alone, and the two caps together. The page\'s cap is in bold. '
      'The largest standard cap is the goal itself, which keeps every HTR in reach.')
    w()
    for m in MS:
        w(f'### {m}qt DRs (goal {GOAL[m]})')
        w()
        for k in BYQT[m]:
            R = O[k]; g = R['goal']
            lo, hi = R['below'], R['above']
            nb = [f"at most {c} moves keeps {num(A(k, c)['htr_med'])} and reaches {pct(A(k, c)['reach'])}" for c in ([lo] if lo is not None and lo != hi else []) + ([hi] if hi is not None else [])]
            w(f"**{k}** · {who(k)}. {PEN} keeps {num(P(k)['htr_med'])} HTRs per DR and reaches {pct(P(k)['reach'])}; " + ', and '.join(nb) + '.')
            w()
            w(f'| Cap | {COLS} |')
            w('|---|---|---|---|---|---|---|')
            for c in range(g - 5, g + 1):
                w(f'| {cap_txt(k, c)} | ' + ' | '.join(row(A(k, c))) + ' |')
            for kk, nm in (('3', 'P ≤ 1, P+S+T ≤ 3'), ('4', 'P ≤ 1, P+S+T ≤ 4'), ('5', f'**{PEN}**'), ('6', 'P ≤ 1, P+S+T ≤ 6'), ('none', 'P ≤ 1')):
                cells = row(P(k, kk))
                if kk == '5': cells = [f'**{x}**' for x in cells]
                w(f'| {nm} | ' + ' | '.join(cells) + ' |')
            for c in range(g - 3, g):
                w(f'| {PEN}, at most {c} moves | ' + ' | '.join(row(R['both'][str(c)])) + ' |')
            w()

    # ---------------------------------------------------------------------------------------------------- section 5
    w('## 5. The premove pass under both caps')
    w()
    w('The premove pass is part of the skeleton/variant meta, and the tables above give it to the standard cap as well. This table shows each cap on normal and inverse alone, and with the pass. '
      'The standard cap is the one of section 2.')
    w()
    w('| Corner case | Standard cap | Standard cap, HTRs per DR, no pass | Standard cap, HTRs per DR, with the pass | Standard cap, reach, no pass | Standard cap, reach, with the pass | Skeleton/variant cap, HTRs per DR, no pass | Skeleton/variant cap, HTRs per DR, with the pass | Skeleton/variant cap, reach, no pass | Skeleton/variant cap, reach, with the pass |')
    w('|---|---|---|---|---|---|---|---|---|---|')
    for k in ORDER:
        R = O[k]; c = str(R['match']); a0, a1 = R['nopass']['abs'][c], R['abs'][c]; p0, p1 = R['nopass']['pen']['5'], R['pen']['5']
        w(f"| {k} | {c} moves | {num(a0['htr_med'])} | {num(a1['htr_med'])} | {pct(a0['reach'])} | {pct(a1['reach'])} | {num(p0['htr_med'])} | {num(p1['htr_med'])} | {pct(p0['reach'])} | {pct(p1['reach'])} |")
    w()
    ga = sum(O[k]['abs'][str(O[k]['match'])]['found'] - O[k]['nopass']['abs'][str(O[k]['match'])]['found'] for k in ORDER)
    gp = sum(O[k]['pen']['5']['found'] - O[k]['nopass']['pen']['5']['found'] for k in ORDER)
    w(f"Over the sample's {WG:,} within-goal DRs, the pass adds {ga} to the standard cap's reach and {gp} to the skeleton/variant cap's. "
      'Its HTRs come early in the order: with the last quarter turn made first, the trigger becomes part of the finish, so the HTR is that many moves nearer.')
    w()

    # ---------------------------------------------------------------------------------------------------- section 6
    w('## 6. The pairs in the order')
    w()
    w('This table shows the skeleton/variant cap with the order as it is, most pairs first among HTRs equally far, and with those HTRs taken in random order. The standard cap of section 2 gives the same numbers to within '
      f"{100 * max(max(abs(x - y) for x, y in zip(O[k]['nopairs']['abs']['within'], O[k]['nopairs']['pen']['within'])) for k in ORDER):.1f} points.")
    w()
    w('| Corner case | Within 5, most pairs first | Within 5, random | Within 10, most pairs first | Within 10, random | Within 20, most pairs first | Within 20, random | Place of the first solution, most pairs first | Place of the first solution, random |')
    w('|---|---|---|---|---|---|---|---|---|')
    for k in ORDER:
        a = P(k); b = O[k]['nopairs']['pen']
        w(f"| {k} | " + ' | '.join(f"{pct(a['within'][j], 0)} | {pct(b['within'][j], 0)}" for j in range(3)) + f" | {place(a['med_pos'])} | {place(b['med_pos'])} |")
    w()

    # ---------------------------------------------------------------------------------------------------- section 7
    w('## 7. For scale: the page\'s meta, with the bound')
    w()
    w(f'On the [page]({PAGE_LINK}) the skeleton/variant cap doesn\'t work alone: step 5 discards a variant when its extra moves plus the bound\'s N don\'t fit the goal, and step 4 leaves a variant to the side where it comes earlier. '
      'This table puts the page\'s meta, with the corner-case-aware bound, next to the two caps of this report. The order is the same in all three.')
    w()
    w('| Corner case | Standard cap | Standard cap, HTRs per DR | Skeleton/variant cap, HTRs per DR | Page\'s meta, HTRs per DR | Standard cap, reach | Skeleton/variant cap, reach | Page\'s meta, reach | Standard cap, within 10 | Skeleton/variant cap, within 10 | Page\'s meta, within 10 |')
    w('|---|---|---|---|---|---|---|---|---|---|---|')
    for k in ORDER:
        b = C[k]['bounds']['cca']; o = C[k]['orders']['cca_len']
        w(f"| {k} | {O[k]['match']} moves | {num(A(k)['htr_med'])} | {num(P(k)['htr_med'])} | {num(b['htr_med'])} | {pct(A(k)['reach'])} | {pct(P(k)['reach'])} | {pct(1 - b['miss'])} | "
          f"{pct(A(k)['within'][1], 0)} | {pct(P(k)['within'][1], 0)} | {pct(o[1], 0)} |")
    w()
    rb = [P(k)['htr_med'] / C[k]['bounds']['cca']['htr_med'] for k in BIG]
    w(f"The bound and step 4 take the skeleton/variant cap's HTRs per DR down by {min(rb):.0f}x to {max(rb):.0f}x in the corner cases with at least 100 within-goal DRs, "
      'and what they take out is mostly not within goal, so a solution also comes sooner.')
    w()

    # ---------------------------------------------------------------------------------------------------- section 8
    w('## 8. The standard cap with the standard meta\'s usual NISS')
    w()
    w('The tables above give both caps the same places to look, the premove pass included. The standard meta has a NISS of its own: one NISS after a start of 1 to 3 moves '
      '(a quarter turn; a side half turn and a quarter turn; a U-layer move, a side half turn and a quarter turn). '
      'This table shows the standard cap of section 2 with no NISS and with that NISS, by how long the start may be. '
      'It is counted on a list of the standard meta\'s own (see below), in the same order, so it also has the few HTRs on skeletons with four more quarter turns.')
    w()
    w(f'| Corner case | Standard cap | NISS | {COLS} |')
    w('|---|---|---|---|---|---|---|---|---|')
    niss = {}
    for k in ORDER:
        R = O[k]; c = min(R['match'], R['capmax'])
        for lev, nm in enumerate(('none', 'after 1 move', 'after up to 2 moves', 'after up to 3 moves')):
            w(f'| {k} | {c} moves | {nm} | ' + ' | '.join(row(R['own'][f'{c}_{lev}'])) + ' |')
        e1, e3 = R['own'][f'{c}_1'], R['own'][f'{c}_3']
        niss[k] = dict(c=c, d10=e3['within'][1] - e1['within'][1], ratio=e3['htr_med'] / e1['htr_med'],
                       pass10=abs(e1['within'][1] - A(k, c)['within'][1]), w1=e1['within'][1], w3=e3['within'][1])
    w()
    kb = max(BIG, key=lambda k: niss[k]['d10']); kw = min(BIG, key=lambda k: niss[k]['d10'])
    assert niss[kw]['d10'] > 0
    w(f"**A NISS after 1 move is the premove pass without its conditions** (3 or more quarter turns, a skeleton that ends in HH). It gives the numbers of the tables above: "
      f"found within 10 is within {100 * max(niss[k]['pass10'] for k in BIG):.0f} points of the standard cap's with the pass in every corner case with at least 100 within-goal DRs.")
    w()
    w(f"**A NISS after up to 3 moves finds a solution sooner.** At the same cap it keeps {min(v['ratio'] for v in niss.values()):.1f}x to {max(v['ratio'] for v in niss.values()):.1f}x the HTRs of a NISS after 1 move, "
      f"and found within 10 goes up by {100 * niss[kw]['d10']:.0f} points on {kw} and by {100 * niss[kb]['d10']:.0f} on {kb}, the two ends among those corner cases. "
      'This is a difference between the two metas that the caps don\'t account for: the skeleton/variant meta has no NISS but the premove pass.')
    w()

    # ---------------------------------------------------------------------------------------------------- method
    w('## How it was counted')
    w()
    nchk = sum({M[k]: O[k]['std_check'] for k in ORDER}.values())
    w('- **HTRs.** The page\'s records: on both sides of every DR, every HTR in reach on a skeleton with the DR\'s quarter turns or two more, and the HTRs of the premove pass. '
      'In reach means the moves to HTR plus the corner moves left after it fit the goal. An HTR is one path up to how its U and D layer turns are written, with the best finish among those.')
    w('- **Moves to HTR.** The length of the path, premove included. On its own skeleton that is L+P+S+T less the skeleton\'s moves after HTR.')
    w('- **Caps.** The standard cap is on the moves to HTR. The skeleton/variant cap is P ≤ 1 and P+S+T ≤ 5 on the HTR\'s own skeleton; in the premove pass, on the skeleton of what is left. No bound, no step 4.')
    w('- **Order.** By moves to HTR, fewest first, then most pairs, counted as on the page. Ties are taken in random order, and found within K and the place of the first solution are taken over 20 such orders.')
    w('- **Finish.** The shortest leave-slice finish in half turns from the HTR, from an exact table.')
    w()
    w('The standard cap doesn\'t need skeletons, so it was also counted on a list of its own: every HTR within the cap on normal, on inverse and with the NISS of section 8, with any number of quarter turns, the pairs counted at the HTR. '
      'This table compares the two counts on normal and inverse alone, at the standard cap closest to the skeleton/variant cap there.')
    w()
    w('| Corner case | Standard cap | HTRs per DR, records | HTRs per DR, own list | Reach, records | Reach, own list | Within 10, records | Within 10, own list | Place of the first solution, records | Place of the first solution, own list |')
    w('|---|---|---|---|---|---|---|---|---|---|')
    for k in ORDER:
        R = O[k]; c = min(R['nopass']['match'], R['capmax'])
        a = R['nopass']['abs'][str(c)]; b = R['own'][f'{c}_0']
        w(f"| {k} | {c} moves | {num(a['htr_med'])} | {num(b['htr_med'])} | {pct(a['reach'])} | {pct(b['reach'])} | {pct(a['within'][1], 0)} | {pct(b['within'][1], 0)} | {place(a['med_pos'])} | {place(b['med_pos'])} |")
    w()
    mq = dict(n=sum(O[k]['own_more_qt']['n'] for k in ORDER), more=sum(O[k]['own_more_qt']['more'] for k in ORDER))
    more_g = sum(O[k]['own_search'][str(O[k]['goal'])]['more'] for k in ORDER)
    # (the DRs neither cap reaches, section 2, are these: nothing of theirs is among the records)
    assert tot['neither'] == more_g and tot['pen_only'] == 0
    u = UNIV
    w(f"The own list has the HTRs on skeletons with four or more quarter turns over the DR's, which the records leave out: {pct(mq['more'] / mq['n'])} of its HTRs at those caps. "
      f"With no cap at all, on normal and inverse they hold the only within-goal solutions of {more_g} of the sample's {WG:,} within-goal DRs"
      + (f". For example, the {u['case']} DR `{u['scramble']}` is solved by `{u['sol']}` in {u['len']} moves, with {u['q']} quarter turns." if u else '.')
      + ' The two counts also differ in the pairs: the own list counts them at the HTR, the records right after the last insertion, which comes before the trigger when the trigger has no extra move. '
        'That is where found within 10 and the place of the first solution differ in the table.')
    w()
    w('Checks:')
    w()
    w(f"- The own list against a separate search for within-goal solutions: for every DR, cap and NISS depth, the best within-goal total is the same ({nchk:,} comparisons).")
    w('- The same search against the records: under P ≤ 1 and P+S+T ≤ 5 it finds a within-goal solution for the same DRs, with the same best length.')
    w('- On the own list the chances are worked out exactly for random ties; 40 random orders of the list itself give the same found within 5, 10 and 20 to within '
      f"{100 * max(max(abs(x - y) for x, y in zip(O[k]['sim']['within'], O[k]['own'][O[k]['own_match']]['within'])) for k in ORDER):.1f} points.")
    w('- Every example was replayed on an independent sticker model, read again on both sides and after its premove, and its moves to HTR recounted from its own moves.')

    # ---------------------------------------------------------------------------------------------------- short version, filled in
    k0 = '4b2'
    p0 = P(k0); R0 = O[k0]; g0 = R0['goal']
    b0 = C[k0]['bounds']['cca']
    lo0, hi0 = R0['below'], R0['above']
    assert lo0 is not None and hi0 is not None and lo0 != hi0 and k0 in BET
    sv = []
    sv.append(f"- **The cap doesn't change how soon a solution is found.** In the same order both metas start with the same HTRs. On {k0}, a within-goal finish is among the first 10 HTRs for "
              f"{pct(p0['within'][1], 0)} of within-goal DRs under the skeleton/variant cap and {pct(A(k0)['within'][1], 0)} under a cap of {R0['match']} moves, and the first one comes at place {place(p0['med_pos'])} under both. "
              f"No corner case differs by more than {100 * max(near):.1f} points (section 1).")
    assert place(p0['med_pos']) == place(A(k0)['med_pos'])
    sv.append(f"- **Alone, the skeleton/variant cap usually needs more HTRs for the same reach.** In {len(DOM)} of the {len(ORDER)} corner cases a standard cap reaches at least as many within-goal DRs with fewer HTRs per DR. "
              f"In the other {len(BET)} it sits between two standard caps: on {k0} it keeps {num(p0['htr_med'])} HTRs per DR and reaches {pct(p0['reach'])}, "
              f"a cap of {lo0} moves keeps {num(A(k0, lo0)['htr_med'])} and reaches {pct(A(k0, lo0)['reach'])}, and a cap of {hi0} moves {num(A(k0, hi0)['htr_med'])} and {pct(A(k0, hi0)['reach'])} (section 1).")
    sv.append(f"- **That is because it keeps HTRs that are too far.** Past a cap one move under the goal are {span(far, lambda v: pct(v, 0))} of its HTRs, and one of them is within goal {one_in(T3['pen_only'])} times, "
              f"against {one_in(T3['both'])} for an HTR both caps keep: {LEFT} (section 2).")
    sv.append(f"- **The two caps cut different HTRs and work together.** With a cap one move under the goal on top, the skeleton/variant cap reaches the same within-goal DRs in every corner case with "
              f"{span([v['of_pen'] for v in tog.values()], lambda v: pct(v, 0))} of the HTRs. On {k0} that is {num(R0['both'][str(g0 - 1)]['htr_med'])} HTRs per DR and {pct(R0['both'][str(g0 - 1)]['reach'])}, "
              f"against {num(A(k0, g0 - 1)['htr_med'])} and {pct(A(k0, g0 - 1)['reach'])} for the cap of {g0 - 1} moves alone. Over the sample, the two together give up {lost1} of {WG:,} within-goal DRs next to that cap alone (section 3).")
    sv.append(f"- **The premove pass is worth as much to the standard cap.** It adds {ga} within-goal DRs to the standard cap's reach and {gp} to the skeleton/variant cap's, out of {WG:,} (section 5).")
    sv.append(f"- **On the page, the bound does what a cap on the moves does here, and more.** With the corner-case-aware bound and step 4, the page's meta finishes {num(b0['htr_med'])} HTRs per DR on {k0}, "
              f"reaches {pct(1 - b0['miss'])} and finds a within-goal finish within 10 for {pct(C[k0]['orders']['cca_len'][1], 0)} (section 7).")
    sv.append(f"- **The standard meta's usual NISS goes further than the premove pass.** A NISS after 1 move gives what the pass gives. One after up to 3 moves keeps {min(v['ratio'] for v in niss.values()):.1f}x to {max(v['ratio'] for v in niss.values()):.1f}x the HTRs at the same cap, "
              f"and on {k0} finds a within-goal finish within 10 for {pct(niss[k0]['w3'], 0)} of within-goal DRs instead of {pct(niss[k0]['w1'], 0)}. The caps don't account for that difference (section 8).")
    out[SHORT:SHORT] = sv
    open(dest, 'w').write('\n'.join(out) + '\n')
    print('written', dest, len(out), 'lines')
