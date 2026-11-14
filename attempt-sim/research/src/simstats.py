#!/usr/bin/env python3
"""Shared statistics over result files of `attemptsim run` (one row per policy x scramble).

load(paths, lo, hi)      {policy: {scr: row}} over several files (scrambles lo <= scr < hi), later files win
summ(rows, dnf)          per-policy statistics with standard errors
paired(a, b, dnf)        differences a - b on the scrambles both have, with standard errors (common random numbers:
                         the same scramble gets the same draws under every policy, so differences are much sharper
                         than the two means' own errors)
A DNF is counted as `dnf` moves (30 unless said otherwise) in `score`; `mean` is over the solved attempts only."""
import csv, math, collections

DNF = 30.0

def load(paths, lo=0, hi=10 ** 9, policies=None):
    if isinstance(paths, str): paths = [paths]
    by = collections.OrderedDict()
    for p in paths:
        with open(p) as f:
            for r in csv.DictReader(f, delimiter='\t'):
                s = int(r['scr'])
                if lo <= s < hi and (policies is None or r['policy'] in policies):
                    by.setdefault(r['policy'], {})[s] = r
    return by

def length(r): return int(r['len'])
def score(r, dnf=DNF): return int(r['len']) if int(r['len']) > 0 else dnf

def mse(xs):
    n = len(xs)
    if n == 0: return float('nan'), float('nan')
    m = sum(xs) / n
    return m, (math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1) / n) if n > 1 else 0.0)

def share(rows, f):
    """share (in %) of rows with f(row), and its standard error (binomial)"""
    n = len(rows); k = sum(1 for r in rows if f(r)); p = k / n
    return 100 * p, 100 * math.sqrt(p * (1 - p) / n)

def summ(rows, dnf=DNF):
    rows = list(rows.values()) if isinstance(rows, dict) else list(rows)
    L = [length(r) for r in rows]; ok = [x for x in L if x > 0]
    m, se = mse(ok)
    sd = math.sqrt(sum((x - m) ** 2 for x in ok) / (len(ok) - 1)) if len(ok) > 1 else 0.0
    sc, sc_se = mse([score(r, dnf) for r in rows])
    d = dict(n=len(rows), mean=m, se=se, sd=sd, score=sc, score_se=sc_se)
    for key, f in (('dnf', lambda r: length(r) == 0), ('sub20', lambda r: 0 < length(r) < 20), ('le20', lambda r: 0 < length(r) <= 20),
                   ('le21', lambda r: 0 < length(r) <= 21), ('le22', lambda r: 0 < length(r) <= 22), ('le23', lambda r: 0 < length(r) <= 23),
                   ('ge24', lambda r: length(r) >= 24)):
        d[key], d[key + '_se'] = share(rows, f)
    avg = lambda k: sum(float(r[k]) for r in rows) / len(rows)
    d.update(eos=avg('eos'), drs=avg('drs'), fin=avg('drs_finished'), rzp=avg('n_rzp'), sw=avg('n_switch'), routes=avg('n_htr'),
             m_eo=(avg('ms_look') + avg('ms_eo_scan') + avg('ms_eo_write')) / 60000,
             m_dr=(avg('ms_eo_eval') + avg('ms_rzp') + avg('ms_switch') + avg('ms_dr_find')) / 60000,
             m_fin=(avg('ms_dr_read') + avg('ms_htr') + avg('ms_tail')) / 60000, m_write=avg('ms_write') / 60000)
    ok_rows = [r for r in rows if length(r) > 0]
    if ok_rows and 'res_dr_ms' in ok_rows[0]:
        d['t_res_dr'] = sum(int(r['res_dr_ms']) for r in ok_rows) / len(ok_rows) / 60000
        d['t_res_sol'] = sum(int(r['res_sol_ms']) for r in ok_rows) / len(ok_rows) / 60000
        d['dr_len'] = sum(int(r['res_dr_len']) for r in ok_rows) / len(ok_rows)
        d['opt_from_dr'] = 100 * sum(int(r['res_fin']) == int(r['res_exact']) for r in ok_rows) / len(ok_rows)
    hist = collections.Counter(L)
    d['hist'] = hist
    return d

def paired(a, b, dnf=DNF):
    """a, b: {scr: row}; mean differences a - b on the common scrambles, with standard errors"""
    ks = [k for k in a if k in b]
    def diff(fn):
        return mse([fn(a[k]) - fn(b[k]) for k in ks])
    ind = lambda f: (lambda r: 1.0 if f(int(r['len'])) else 0.0)
    out = dict(n_pair=len(ks))
    out['d_score'], out['d_score_se'] = diff(lambda r: score(r, dnf))
    for key, f in (('d_le22', lambda x: 0 < x <= 22), ('d_le21', lambda x: 0 < x <= 21), ('d_sub20', lambda x: 0 < x < 20), ('d_dnf', lambda x: x == 0)):
        m, se = diff(ind(f)); out[key], out[key + '_se'] = 100 * m, 100 * se
    both = [k for k in ks if int(a[k]['len']) > 0 and int(b[k]['len']) > 0]
    m, se = mse([int(a[k]['len']) - int(b[k]['len']) for k in both])
    out['d_mean_both'], out['d_mean_both_se'] = m, se
    return out

def fmt(x, nd=2, sign=False):
    if x is None or (isinstance(x, float) and math.isnan(x)): return '-'
    s = f'{x:+.{nd}f}' if sign else f'{x:.{nd}f}'
    return s.replace('-', '−') if s.startswith('-') else s
