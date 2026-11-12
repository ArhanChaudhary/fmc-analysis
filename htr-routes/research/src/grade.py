#!/usr/bin/env python3
"""Question 6: grade hand checklists.  Each step of a checklist is a set of route classes, written as a predicate on
the route to HTR of a reading (H key): its labels (subset + edges at the start and after each quarter turn up to
HTR), the switch position, whether the post-HTR part is half turns only, and the HTR length of the shortest such
reading.  A step "finds" the optimal on a state if some optimal finish has a reading in one of its classes; the
cumulative share after step k is the share of states where steps 1..k find it.  Same at optimal + 1.

What the keys cannot see (and so the grading cannot restrict on): how many half turns sit between two quarter turns
or before the first one; which side a reading starts on (except the 4a3/4b3 and 4a4/4b4 letters).  Steps that
depend on that are graded as the class they belong to (an upper bound) and marked "~".
Output: out/q6_grading.tsv"""
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

def grade(subs, steps, target, budget=99):
    """cumulative share (weighted by subset size) after each step"""
    W = 0.0
    hits = np.zeros(len(steps))
    for s in subs:
        rt = routes(s)
        w = SIZE[s] / rt.n
        # optimum: optimal finishes, their shortest HTR (htr); +1: every finish <= opt + 1, shortest HTR over them (htr1)
        m = (rt.delta == 0) if target == 'opt' else np.ones(len(rt.rid), bool)
        hh = rt.htr if target == 'opt' else rt.htr1
        if budget < 99:
            niss = load_states(s)['htrNiss']
            m &= hh <= niss[rt.state] + budget
        pair = rt.rid[m] * 32 + hh[m]
        u, inv = np.unique(pair, return_inverse=True)
        stepof = np.full(len(u), len(steps))
        for k, x in enumerate(u):
            p = P(int(x >> 5))
            if not p: continue
            cn, labs, sw, post, nq = p
            for si, (_, pred) in enumerate(steps):
                if pred(cn, labs, sw, post, nq, int(x & 31)):
                    stepof[k] = si; break
        first = np.full(rt.n, len(steps))
        np.minimum.at(first, rt.state[m], stepof[inv])
        for si in range(len(steps)):
            hits[si] += w * (first <= si).sum()
        W += w * rt.n
    return hits / W

ht = lambda post: post == 'ht'
def lin(cn, chain): return lambda c, l, sw, post, nq, h: sw is None and c == chain and ht(post)

def checklists():
    L = []
    # Zagros D15884: 4b2 order
    z = [
        ('S1+S2 linear 2qt 4b2 > 4a1 > HTR (normal or inverse)', lambda c, l, sw, p, nq, h: sw is None and c == ['4b2', '4a1', '0c0'] and ht(p)),
        ('S3 linear 4qt HTR of <= 8 moves', lambda c, l, sw, p, nq, h: sw is None and nq == 4 and h <= 8 and ht(p)),
        ('S4 reduce to 4a1, switch (4b2 > 4a1 > (HTR))', lambda c, l, sw, p, nq, h: c == ['4b2', '4a1', '0c0'] and sw == 2 and ht(p)),
        ('S5 regress to 2c3, switch (4b2 > 2c3 > (...))', lambda c, l, sw, p, nq, h: len(c) > 1 and c[1] == '2c3' and sw == 2 and ht(p)),
        ('S8 2+2: any 4qt route switching after the 2nd qt', lambda c, l, sw, p, nq, h: nq == 4 and sw == 3 and ht(p)),
    ]
    L.append(('Zagros 4b2 order (D15884)', ['4b2 0e', '4b2 2e', '4b2 4e'], z))
    L.append(('Zagros 4b2 order (D15884), 4b2 4e only', ['4b2 4e'], z))
    yura = [
        ('~S1 linear 2qt trigger with <= 2 setup moves (HTR <= 6)', lambda c, l, sw, p, nq, h: sw is None and c == ['4b2', '4a1', '0c0'] and h <= 6 and ht(p)),
        ('S2 regress to 2c3 (2e or 4e), then 2c3 linear or switch (4qt)', lambda c, l, sw, p, nq, h: nq == 4 and c[1] == '2c3' and ht(p)),
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
    def daichi(sub):
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
                return nq == 3 and (l[1] != '4b2 4e' or sw == 2)
            if cnr == '2c4':
                if e == 8: return (sw == 2 and c[1] == '2c3') or (sw == 3 and l[2] == '4b2 2e')
                return (sw is None and nq == 4 and l[1] in ('2c3 2e', '2c3 4e')) or (sw == 2 and c[1] == '2c3') or (sw == 3 and l[2] == '4b2 2e')
            if cnr == '0c3':
                return l[1] == '4a2 4e' and sw == 2
            if cnr == '0c4':
                return (sw == 3 and c[2] == '4b2') or (e == 2 and sw is None)
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

def main():
    global K
    K = keys()
    with open(f'{OUT}/q6_grading.tsv', 'w') as f:
        f.write('checklist\tsubsets\tstep\tstep_description\tcumulative_opt\tcumulative_p1\tcumulative_opt_htr_budget2\tcumulative_p1_htr_budget2\n')
        for name, subs, steps in checklists():
            a = grade(subs, steps, 'opt'); b = grade(subs, steps, 'p1')
            a2 = grade(subs, steps, 'opt', 2); b2 = grade(subs, steps, 'p1', 2)
            for i, (desc, _) in enumerate(steps):
                f.write(f'{name}\t{",".join(subs)}\t{i + 1}\t{desc}\t{a[i]:.4f}\t{b[i]:.4f}\t{a2[i]:.4f}\t{b2[i]:.4f}\n')
            print(name, [round(x, 3) for x in a], flush=True)

if __name__ == '__main__':
    main()
