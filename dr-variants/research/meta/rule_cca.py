"""The corner-case-aware bound of Advanced DR Bounding as the user gave it on 19 Nov 2026 (the live doc's table):
N for each of the 216 NISS@1qt cases -> ../out/meta/rule_cca.tsv (one line per case, in the order of cases.tsv),
checked against the shortest leave-slice finish of each case.  Reflection is not part of the 216 cases, so the
"+2 per reflected slice" terms are left out: the bound used here is the table's value for an unreflected slice."""
import pandas as pd, numpy as np
c = pd.read_csv('../out/meta/cases.tsv', sep='\t'); c.columns = list(c.columns[:-1]) + ['hs']
def n_new(kind, F, R, fr, bad):
    if kind == 'H-H':
        return [5 if fr else 0, 5 if fr else 3, 6][bad]
    if kind in ('R-D', 'F-D', 'R-V', 'F-V'):
        must, other = (R, F) if kind[0] == 'R' else (F, R)
        cor = kind[2]                                   # D or V: the must-have slice type
        if bad == 0:
            assert must == cor and other in ('H', cor), (kind, F, R)
            base = 0 if other == 'H' else 1
            return base + ((3 if cor == 'D' else 1) if fr else 0)
        if bad == 1:
            return (5 if fr else 3) if cor == 'D' else (2 if fr else 3)
        return 5
    # D-D corners
    if bad == 0:
        s = ''.join(sorted(F + R))
        return {'DV': 0, 'VV': 1, 'DD': 2}[s]
    return [None, 3, 5][bad]
c['n_cca'] = [n_new(k, f, r, fr, b) for k, f, r, fr, b in zip(c.kind, c.F, c.R, c.fr, c.bad)]
c['case_min'] = [next(i for i, v in enumerate(map(int, h.split())) if v) for h in c.hs]   # shortest finish minus corner moves
c['slack'] = c.case_min - c.n_cca
bad = c[c.slack < 0]
print(f'216 cases: the bound is a floor in {int((c.slack >= 0).sum())}; exact in {int((c.slack == 0).sum())}, 1 under in {int((c.slack == 1).sum())}, 2+ under in {int((c.slack >= 2).sum())}')
print('against the earlier rule (sheet Heuristic): lower in', int((c.n_cca < c.rule).sum()), 'cases, equal in', int((c.n_cca == c.rule).sum()), ', higher in', int((c.n_cca > c.rule).sum()))
if len(bad): print('NOT A FLOOR:\n', bad[['case', 'kind', 'F', 'R', 'cs', 'fr', 'bad', 'rule', 'n_cca', 'case_min']].to_string())
c[['n_cca']].to_csv('../out/meta/rule_cca.tsv', sep='\t', index=False, header=False)
