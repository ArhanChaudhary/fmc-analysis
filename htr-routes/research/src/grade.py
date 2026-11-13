#!/usr/bin/env python3
"""Question 6: grade hand checklists.  Each step of a checklist is a set of route classes, written as a predicate on
the route to HTR of a reading (H key): its labels (subset + edges at the start and after each quarter turn up to
HTR), the switch position, whether the post-HTR part is half turns only, and the HTR length of the shortest such
reading.  A step "finds" the optimal on a state if some optimal finish has a reading in one of its classes; the
cumulative share after step k is the share of states where steps 1..k find it.  Same at optimal + 1.

What the keys cannot see (and so the grading cannot restrict on): how many half turns sit between two quarter turns
or before the first one; which side a reading starts on (except the 4a3/4b3 and 4a4/4b4 letters).  Steps that
depend on that are graded as the class they belong to (an upper bound) and marked "~".
Each checklist is graded with no HTR limit, with budget 2 (HTRs at most 2 over the shortest NISS HTR), with the HTR
limit each step's author stated (budget 2 where none is stated), and with budget 2 on the DRs whose optimal is 12 or
less.
Output: out/q6_grading.tsv; out/q6_daichi_vs_mine.tsv (Daichi's sheet against my first three routes, sheet_vs_mine)"""
import collections
import numpy as np
from common import *

K = None
_pc = {}
def P(rid):
    """parsed H key: (corner names, labels, switch index, post, n qts) or None for F keys"""
    r = _pc.get(rid)
    if r is None:
        k = K[rid]
        if k[0] != 'H': r = False
        else:
            kind, labs, sw, post = parse_key(k)
            r = ([l.split()[0] for l in labs], labs, sw, post, len(labs) - 1)
        _pc[rid] = r
    return r

_rt = {}
def routes(s):
    if s not in _rt:
        if len(_rt) > 3: _rt.clear()
        _rt[s] = Routes(s)
    return _rt[s]
_st = {}
def states(s):
    if s not in _st:
        if len(_st) > 3: _st.clear()
        _st[s] = load_states(s)
    return _st[s]

def first_step(s, steps, target, budgets):
    """per sampled state of s: the first step (0-based; len(steps) = none) that finds a finish at the target, a step
    counting a reading only when its HTR is at most budgets[i] over the DR's shortest NISS HTR (99: no limit).
    target 'opt': the optimal finishes and their shortest HTR (htr); 'p1': every finish <= opt + 1, shortest HTR over
    them (htr1).  budgets is one list or a dict of them (name -> list), answered with a dict."""
    rt = routes(s); niss = states(s)['htrNiss']
    m = (rt.delta == 0) if target == 'opt' else np.ones(len(rt.rid), bool)
    hh = (rt.htr if target == 'opt' else rt.htr1)[m]; stm = rt.state[m]
    over = hh - niss[stm]
    u, inv = np.unique(rt.rid[m] * 32 + hh, return_inverse=True)
    ok = np.zeros((len(u), len(steps)), bool)
    for k, x in enumerate(u):
        p = P(int(x >> 5))
        if not p: continue
        for si, st_ in enumerate(steps):
            ok[k, si] = st_[1](*p, int(x & 31))
    out = {}
    for name, bud in (budgets.items() if isinstance(budgets, dict) else [(None, budgets)]):
        first = np.full(rt.n, len(steps))
        for si in reversed(range(len(steps))):          # a smaller step overwrites a larger one
            first[stm[ok[inv, si] & (over <= bud[si])]] = si
        out[name] = first
    return out if isinstance(budgets, dict) else out[None]

def stated(steps):
    """each step's own HTR limit as its author stated it (third element of the step), else budget 2"""
    return [st_[2] if len(st_) > 2 else 2 for st_ in steps]

def grade_all(subs, steps):
    """cumulative shares (weighted by subset size) after each step: {(target, mode): array}, mode 'inf' (no HTR
    limit), 'b2' (budget 2), 'stated' (each step's own limit, budget 2 where none is stated), and ('opt', 'b2_le12'):
    budget 2 on the DRs whose optimal finish is 12 moves or less (Daichi's "sub13", D18343)"""
    S = len(steps)
    modes = {'inf': [99] * S, 'b2': [2] * S, 'stated': stated(steps)}
    acc = collections.defaultdict(lambda: np.zeros(S)); W = W12 = 0.0
    for s in subs:
        rt = routes(s); w = SIZE[s] / rt.n; le12 = states(s)['d'] <= 12
        for target in ('opt', 'p1'):
            fs = first_step(s, steps, target, modes)
            for mode, first in fs.items():
                for si in range(S):
                    acc[(target, mode)][si] += w * (first <= si).sum()
                    if target == 'opt' and mode == 'b2': acc[('opt', 'b2_le12')][si] += w * ((first <= si) & le12).sum()
        W += w * rt.n; W12 += w * le12.sum()
    return {k: v / (W12 if k[1] == 'b2_le12' else W) for k, v in acc.items()}

def grade(subs, steps, target, budget=99):
    """cumulative share (weighted by subset size) after each step, every step with the same HTR budget"""
    W = 0.0; hits = np.zeros(len(steps))
    for s in subs:
        rt = routes(s); w = SIZE[s] / rt.n
        first = first_step(s, steps, target, [budget] * len(steps))
        for si in range(len(steps)): hits[si] += w * (first <= si).sum()
        W += w * rt.n
    return hits / W

ht = lambda post: post == 'ht'
def lin(cn, chain): return lambda c, l, sw, post, nq, h: sw is None and c == chain and ht(post)

def checklists():
    L = []
    # Zagros D15884: 4b2 order.  The third element is the step's own HTR limit as Zagros stated it (99: none): step 2
    # "doing the HTR even if it's long", step 3 "if like <9 moves exists" (in the predicate); the rest budget 2
    z = [
        ('S1+S2 linear 2qt 4b2 > 4a1 > HTR (normal or inverse)', lambda c, l, sw, p, nq, h: sw is None and c == ['4b2', '4a1', '0c0'] and ht(p), 99),
        ('S3 linear 4qt HTR of <= 8 moves', lambda c, l, sw, p, nq, h: sw is None and nq == 4 and h <= 8 and ht(p), 99),
        ('S4 reduce to 4a1, switch (4b2 > 4a1 > (HTR))', lambda c, l, sw, p, nq, h: c == ['4b2', '4a1', '0c0'] and sw == 2 and ht(p)),
        ('S5 regress to 2c3 2e or 4e, switch (4b2 > 2c3 > (...))', lambda c, l, sw, p, nq, h: len(l) > 1 and l[1] in ('2c3 2e', '2c3 4e') and sw == 2 and ht(p)),
        ('S8 2+2: any 4qt route switching after the 2nd qt', lambda c, l, sw, p, nq, h: nq == 4 and sw == 3 and ht(p)),
    ]
    L.append(('Zagros 4b2 order (D15884)', ['4b2 0e', '4b2 2e', '4b2 4e'], z))
    L.append(('Zagros 4b2 order (D15884), 4b2 4e only', ['4b2 4e'], z))
    yura = [
        ('~S1 linear 2qt trigger with <= 2 setup moves (HTR <= 6)', lambda c, l, sw, p, nq, h: sw is None and c == ['4b2', '4a1', '0c0'] and h <= 6 and ht(p)),
        # "do you go to 2c3 2e or 4e or both" - "whatever is shortest" (D6414, D6415)
        ('S2 regress to 2c3 2e or 4e, then 2c3 linear or switch (4qt)', lambda c, l, sw, p, nq, h: nq == 4 and l[1] in ('2c3 2e', '2c3 4e') and ht(p)),
        ('S3 reduce to 4a1 and switch', lambda c, l, sw, p, nq, h: c == ['4b2', '4a1', '0c0'] and sw == 2 and ht(p)),
    ]
    L.append(('Yura 4b2 4e order (D6409-D6416)', ['4b2 4e'], yura))
    L.append(('rogo/Adri 4b2 4e order (D6422-D6424)', ['4b2 4e'], [yura[0], yura[2]]))
    lewis = [
        ('S1 linear 2qt 4a2 > 4a1 4e > HTR', lambda c, l, sw, p, nq, h: sw is None and c == ['4a2', '4a1', '0c0'] and ht(p)),
        ('S2 reduce to 4a1 4e, switch', lambda c, l, sw, p, nq, h: c == ['4a2', '4a1', '0c0'] and sw == 2 and ht(p)),
        ('S3 4qt linear through 4a2 4e again (qt, slice, qt)', lambda c, l, sw, p, nq, h: sw is None and nq == 4 and '4a2 4e' in l[1:] and ht(p)),
        ('S4 regress to 4b3 (2e/4e), switch, 4a3 > 4b2 > 4a1', lambda c, l, sw, p, nq, h: nq == 4 and c[1] == '4b3' and l[1] != '4b3 0e' and sw == 2 and ht(p)),
        ('S5 regress to 0c3, then 0c3 > 4a2 > 4a1 (linear or NISS)', lambda c, l, sw, p, nq, h: nq == 4 and c[1] == '0c3' and ht(p)),
    ]
    L.append(('Lewis 4a2 0e/2e list (T6743)', ['4a2 0e', '4a2 2e'], lewis))
    jay = [('~2c3 0e: one qt to 4b2 4e, switch, 4a1 > HTR (Jay T328 / rodney T331-T344, prefix not restricted)',
            lambda c, l, sw, p, nq, h: l[:2] == ['2c3 0e', '4b2 4e'] and nq == 3 and sw == 2 and ht(p))]
    L.append(('Jay/rodney 2c3 0e checks (T328-T344)', ['2c3 0e'], jay))
    # Daichi's cheat sheet (D18340): one predicate per corner subset and edge count, all graded as one step
    def daichi(sub, trigger=False):
        """trigger: the 4c3 row with its bracket, "always switch after 4b2 4e (except for the 4a3 0/4e 8 move trigger
        I think?)": also linear through 4b2 4e on the 4a3 side of 4c3 0e and 4e with an HTR of at most 8"""
        cnr, e = sub.split(); e = int(e[0])
        def f(c, l, sw, p, nq, h):
            if not ht(p): return False
            if cnr == '0c0':
                if e == 0: return True
                return nq == 2 or (2 <= e <= 6 and nq == 4 and '4b2 2e' in l)
            if cnr == '4a1':
                if e == 0: return nq == 3 or (nq == 5 and '2c3' in c and '4b2 2e' in l)
                if nq == 3 and not ('4a2' in c or '0c0 6e' in l or '0c0 8e' in l[:-1]): return True
                return e == 4 and nq == 1
            if cnr == '4a2':
                if e <= 2: return (c == ['4a2', '4a1', '0c0'] and sw == 2) or (nq == 4 and c[:3] == ['4a2', '4a1', '4b2'])
                return nq == 2
            if cnr == '4b2':
                return nq == 2 or (nq == 4 and c[1] == '2c3')
            if cnr == '2c3':
                if e in (0, 8):
                    return (l[1] == '4b2 4e' and sw == 2) or (nq == 5 and '0c0 4e' in l) or \
                           (nq == 5 and any(l[i] in ('2c3 2e', '2c3 4e') and l[i + 1] == '4b2 2e' for i in range(len(l) - 1)))
                return nq == 3
            if cnr == '4c3':
                return nq == 3 and (l[1] != '4b2 4e' or sw == 2 or
                                    (trigger and e in (0, 4) and c[0] == '4a3' and sw is None and h <= 8))
            if cnr == '2c4':
                if e == 8: return (sw == 2 and c[1] == '2c3') or (sw == 3 and l[2] == '4b2 2e')
                return (sw is None and nq == 4 and l[1] in ('2c3 2e', '2c3 4e')) or (sw == 2 and c[1] == '2c3') or (sw == 3 and l[2] == '4b2 2e')
            if cnr == '0c3':
                return l[1] == '4a2 4e' and sw == 2
            if cnr == '0c4':
                # "all: 4b2 switch (2e could be linear, except for 0c4 8e)": the 2e is the 4b2's, as in the 4c4 row
                # ("prioritize 2e over 4e") and in D18330 ("0c4 says just check 4b2 switches")
                return (sw == 3 and c[2] == '4b2') or (e != 8 and sw is None and len(l) > 2 and l[2] == '4b2 2e')
            if cnr == '4c4':
                return sw == 3 and c[2] == '4b2'
            if cnr == '2c5':
                return (sw == 3 and l[2] in ('2c3 2e', '2c3 4e')) or sw is None
            if cnr == '4b5':
                return (sw == 2 and l[1] in ('2c4 0e', '2c4 2e', '2c4 4e')) or sw is None
            return False
        return f
    for s in SUBS:
        L.append((f'Daichi cheat sheet (D18340): {s}', [s], [('the listed routes', daichi(s))]))
    for s in ('4c3 0e', '4c3 4e'):
        L.append((f'Daichi cheat sheet with the 4a3 8-move trigger (D18340): {s}', [s], [('the listed routes and the trigger', daichi(s, True))]))
    # (beef beans' bounding route is graded by its reduction length in bounding.py: as a route class alone it
    #  contains every finish that passes 4a1 4e, so it would score ~100% everywhere)
    # Fanti D10034: 4b2 4e split
    fan = [('2qt (4b2 > 4a1 > HTR, any switch)', lambda c, l, sw, p, nq, h: nq == 2 and ht(p)),
           ('4qt via 2c3', lambda c, l, sw, p, nq, h: nq == 4 and c[1] == '2c3' and ht(p)),
           ('4qt via 4a1 > 0c0', lambda c, l, sw, p, nq, h: nq == 4 and c[1:3] == ['4a1', '0c0'] and ht(p))]
    for i, st in enumerate(fan):
        L.append((f'Fanti 4b2 4e split (D10034), class alone: {st[0]}', ['4b2 4e'], [st]))
    L.append(('Fanti 4b2 4e split (D10034), cumulative', ['4b2 4e'], fan))
    return L

def sheet_vs_mine():
    """Daichi's sheet against my first three budget-2 route classes of each subset x edges (q2_checklist_budget.tsv,
    the checklist of section 4), on the same sampled states: on all DRs and on those with an optimal of 12 or less,
    the sheet's own population ("based on the sub13 DR route stats", D18343).  Both find the optimal with budget-2
    HTRs.  se_*: standard error of the paired difference (sheet minus mine) in share points, from the states only
    one of them finds.  Output: out/q6_daichi_vs_mine.tsv"""
    top3 = collections.defaultdict(list)
    for r in csv.DictReader(open(f'{OUT}/q2_checklist_budget.tsv'), delimiter='\t'):
        if r['level'] == 'C' and r['target'] == 'opt' and r['budget'] == '2' and int(r['step']) <= 3:
            top3[r['group']].append(r['class'])
    sheet = {name.split(': ')[1]: steps for name, subs, steps in checklists() if name.startswith('Daichi cheat sheet (D18340): ')}
    with open(f'{OUT}/q6_daichi_vs_mine.tsv', 'w') as f:
        f.write('subset\tn\tn_le12\tsheet\tmine3\tse_diff\tsheet_le12\tmine3_le12\tse_diff_le12\n')
        for s in SUBS:
            cl = set(top3[s])
            mine = [('my first three', lambda c, l, sw, p, nq, h: fmt(c, sw, p) in cl)]
            a = first_step(s, sheet[s], 'opt', [2]) == 0; b = first_step(s, mine, 'opt', [2]) == 0
            le12 = states(s)['d'] <= 12
            row = [s, len(a), int(le12.sum())]
            for sel in (np.ones(len(a), bool), le12):
                x, y, n_ = a[sel], b[sel], sel.sum()
                d = x.mean() - y.mean(); disc = (x != y).mean()
                row += [f'{x.mean():.6f}', f'{y.mean():.6f}', f'{np.sqrt(max(disc - d * d, 0) / n_):.6f}']
            f.write('\t'.join(str(v) for v in row) + '\n')
            print(s, row[1:], flush=True)

def main():
    global K
    K = keys()
    with open(f'{OUT}/q6_grading.tsv', 'w') as f:
        f.write('checklist\tsubsets\tstep\tstep_description\tcumulative_opt\tcumulative_p1\tcumulative_opt_htr_budget2\tcumulative_p1_htr_budget2'
                '\tcumulative_opt_stated\tcumulative_p1_stated\tcumulative_opt_htr_budget2_le12\n')
        for name, subs, steps in checklists():
            g = grade_all(subs, steps)
            for i, st_ in enumerate(steps):
                f.write(f'{name}\t{",".join(subs)}\t{i + 1}\t{st_[0]}\t' + '\t'.join(f"{g[k][i]:.6f}" for k in (
                    ('opt', 'inf'), ('p1', 'inf'), ('opt', 'b2'), ('p1', 'b2'), ('opt', 'stated'), ('p1', 'stated'), ('opt', 'b2_le12'))) + '\n')
            print(name, [round(x, 3) for x in g[('opt', 'b2')]], flush=True)
    sheet_vs_mine()

if __name__ == '__main__':
    main()
