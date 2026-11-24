"""The three bounds of Advanced DR Bounding as the doc states them on 23 Nov 2026 (Simple, Corner-Case-Aware,
Comprehensive), as an N for each of the 216 NISS@1qt cases, plus each case's own shortest leave-slice finish minus
its corner moves (the best any case-level bound can do) -> ../out/meta/rules_1123.tsv (columns simple, cca, comp,
case minimum; one line per case in the order of cases.tsv).  The "+2 per reflected slice" terms are left out:
reflection is not part of the 216 cases.  Against the 19 Nov text the only change is the comprehensive cell for H-H
corners, 0 bad slices, cs/fr = 0/0: +0 now (+1 then, which was not a floor)."""
import pandas as pd, numpy as np
c = pd.read_csv('../out/meta/cases.tsv', sep='\t'); c.columns = list(c.columns[:-1]) + ['hs']
def split(kind, F, R):
    return (R, F) if kind[0] == 'R' else (F, R)
def simple(kind, F, R, cs, fr, bad):
    return [0, 3, 5][bad]
def cca(kind, F, R, cs, fr, bad):
    if kind == 'H-H':
        return [5 if fr else 0, 5 if fr else 3, 6][bad]
    if kind == 'D-D':
        return {'DV': 0, 'VV': 1, 'DD': 2}[''.join(sorted(F + R))] if bad == 0 else [None, 3, 5][bad]
    must, other = split(kind, F, R); cor = kind[2]
    if bad == 0:
        assert must == cor and other in ('H', cor)
        return (0 if other == 'H' else 1) + ((3 if cor == 'D' else 1) if fr else 0)
    if bad == 1:
        return (5 if fr else 3) if cor == 'D' else (2 if fr else 3)
    return 5
def comp(kind, F, R, cs, fr, bad):
    if kind == 'H-H':
        if bad == 0: return 0 if (cs, fr) == (0, 0) else 5
        if bad == 1: return 3 if (cs, fr) == (1, 0) else 5
        return 6
    if kind == 'D-D':
        if bad == 0:
            s = ''.join(sorted(F + R))
            if s == 'VV': return 1
            if s == 'DD': return 2
            # "good cs-parity" for D-V edges: F-D R-V with cs 0 or F-V R-D with cs 1 (the sheet's own column)
            return 0 if (F, cs) in (('D', 0), ('V', 1)) else 4
        return [None, 3, 5][bad]
    must, other = split(kind, F, R); cor = kind[2]
    if cor == 'D':
        if bad == 0:
            if other == 'H': return (0 if cs == 0 else 3) + ((3 - cs) if fr else 0)
            return 1 if (cs, fr) == (1, 0) else 4
        if bad == 1: return 3 if (cs, fr) == (1, 0) else (5 if (cs, fr) == (0, 1) else 4)
        return 5
    if bad == 0:
        if other == 'H': return (0 if cs == 0 else 4) + (1 if fr else 0)
        return (1 if cs == 1 else 3) + (1 if fr == cs else 0)
    if bad == 1: return 2 if (cs, fr) == (1, 1) else 3
    return 5
c['case_min'] = [next(i for i, v in enumerate(map(int, h.split())) if v) for h in c.hs]
for name, f in [('simple', simple), ('cca', cca), ('comp', comp)]:
    c[name] = [f(k, F, R, cs, fr, b) for k, F, R, cs, fr, b in zip(c.kind, c.F, c.R, c.cs, c.fr, c.bad)]
    sl = c.case_min - c[name]
    print(f'{name:7s} floor in {int((sl >= 0).sum())} of 216; exact in {int((sl == 0).sum())}; mean slack {sl[sl >= 0].mean():.2f}')
    for _, r in c[sl < 0].iterrows():
        print(f'    NOT A FLOOR: {r.case:24s} bad {r.bad}  N {r[name]}  shortest finish minus corner moves {r.case_min}')
old = pd.read_csv('../out/meta/rules4col.tsv', sep='\t', header=None)
assert (old[0] == c.simple).all() and (old[1] == c.cca).all() and (old[3] == c.comp).all()
c[['simple', 'cca', 'comp', 'case_min']].to_csv('../out/meta/rules_1123.tsv', sep='\t', index=False, header=False)
