"""The three bounds of the live Advanced DR Bounding doc (fetched 19 Nov 2026): Simple, Corner-Case-Aware and
Comprehensive, as an N for each of the 216 NISS@1qt cases -> ../out/meta/rules3.tsv (columns simple, cca, comp, in the
order of cases.tsv), each checked against the shortest leave-slice finish of every case.  The "+2 per reflected
slice" terms are left out: reflection is not part of the 216 cases."""
import sys
import pandas as pd, numpy as np
c = pd.read_csv('../out/meta/cases.tsv', sep='\t'); c.columns = list(c.columns[:-1]) + ['hs']
def split(kind, F, R):
    must, other = (R, F) if kind[0] == 'R' else (F, R)
    return must, other
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
        if bad == 0: return 1 if (cs, fr) == (0, 0) else 5
        if bad == 1: return 3 if (cs, fr) == (1, 0) else 5
        return 6
    if kind == 'D-D':
        if bad == 0:
            s = ''.join(sorted(F + R))
            if s == 'VV': return 1
            if s == 'DD': return 2
            # The doc reads "good cs-parity" for D-V edges off the direction of the X2 U2 Y2 finish, which the 216
            # case labels don't carry; the sheet's own column gives the per-case value: good is F-D R-V with cs 0 or
            # F-V R-D with cs 1, whatever fr.
            good = (F, cs) in (('D', 0), ('V', 1))
            return 0 if good else 4
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
        print(f'    NOT A FLOOR: {r.case:24s} bad {r.bad}  N {r[name]}  shortest finish minus corner moves {r.case_min}  (sheet rule {r.rule})')
d = c[c.comp != c.rule]
print(f'comprehensive (doc text) differs from the sheet column in {len(d)} cases:')
print(d[['case', 'bad', 'rule', 'comp', 'case_min']].to_string())
c[['simple', 'cca', 'comp']].to_csv('../out/meta/rules3.tsv', sep='\t', index=False, header=False)
# the comprehensive bound with its one cell that isn't a floor (H-H, 0 bad slices, cs/fr = 0/0: +1) set to the
# case's own minimum, +0
fix = (c.kind == 'H-H') & (c.bad == 0) & (c.cs == 0) & (c.fr == 0)
assert fix.sum() == 1 and (c.case_min[fix] == 0).all()
c['comp_fixed'] = np.where(fix, 0, c.comp)
assert (c.case_min >= c.comp_fixed).all()
c[['comp_fixed']].to_csv('../out/meta/rules3fix.tsv', sep='\t', index=False, header=False)
