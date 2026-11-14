#!/usr/bin/env python3
"""Per-policy statistics of a result file of `attemptsim run`, with standard errors and paired differences.

usage: analyze.py RESULT.tsv [--ref POLICY] [--out SUMMARY.tsv] [--dnf 30] [--top N] [--sort KEY]

Columns of the summary (one row per policy):
  n            attempts (scrambles)
  mean, se     mean length of the solved attempts, and its standard error
  sd           standard deviation of the solved attempts
  dnf          share of attempts with no solution written down inside the hour (%)
  sub20, le21, le22   share of all attempts with a result under 20 / at most 21 / at most 22 (%)
  score        mean with a DNF counted as `--dnf` moves (default 30)
  d_score, d_se   paired difference to the reference policy on the same scrambles (score), and its standard error
  d_le22, d_le22_se, d_sub20, d_sub20_se   paired differences of the shares, in points
  eos, rzp, sw, drs, fin, routes   EOs written, RZP states worked, switches, DRs written, DRs taken to a finish, routes tried
  best_dr      mean length of the shortest DR on the page (attempts with a DR)
  m_eo, m_dr, m_fin, m_write   minutes spent on EOs, on RZP/DR, on finishing (reading DRs, routes, finishes), on writing
  key_page     mean of (DR length + exact optimal finish) over the best DR on the page: what the page was worth (computer only)
"""
import sys, csv, math, collections

def load(path):
    by = collections.OrderedDict()
    with open(path) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            by.setdefault(r['policy'], {})[int(r['scr'])] = r
    return by

def stats(rows, dnf):
    n = len(rows)
    L = [int(r['len']) for r in rows]
    ok = [x for x in L if x > 0]
    k = len(ok)
    mean = sum(ok) / k if k else float('nan')
    sd = math.sqrt(sum((x - mean) ** 2 for x in ok) / (k - 1)) if k > 1 else 0.0
    f = lambda key: sum(float(r[key]) for r in rows) / n
    withdr = [float(r['best_dr']) for r in rows if r['best_dr'] != '0']
    orc = [float(r['oracle_page']) for r in rows if r['oracle_page'] != '0']
    return dict(n=n, mean=mean, se=sd / math.sqrt(k) if k else 0, sd=sd, dnf=100 * (n - k) / n,
                sub20=100 * sum(0 < x < 20 for x in L) / n, le21=100 * sum(0 < x <= 21 for x in L) / n, le22=100 * sum(0 < x <= 22 for x in L) / n,
                score=sum(x if x > 0 else dnf for x in L) / n,
                eos=f('eos'), rzp=f('n_rzp'), sw=f('n_switch'), drs=f('drs'), fin=f('drs_finished'), routes=f('n_htr'),
                best_dr=sum(withdr) / len(withdr) if withdr else float('nan'),
                m_eo=(f('ms_look') + f('ms_eo_scan') + f('ms_eo_write')) / 60000, m_dr=(f('ms_eo_eval') + f('ms_rzp') + f('ms_switch') + f('ms_dr_find')) / 60000,
                m_fin=(f('ms_dr_read') + f('ms_htr') + f('ms_tail')) / 60000, m_write=f('ms_write') / 60000,
                key_page=sum(orc) / len(orc) if orc else float('nan'))

def paired(a, b, dnf):
    """a, b: {scr: row}; differences a - b on the common scrambles"""
    ks = [k for k in a if k in b]
    n = len(ks)
    def diff(fn):
        d = [fn(a[k]) - fn(b[k]) for k in ks]
        m = sum(d) / n
        return m, math.sqrt(sum((x - m) ** 2 for x in d) / (n - 1) / n) if n > 1 else 0.0
    sc = lambda r: int(r['len']) if int(r['len']) > 0 else dnf
    return dict(zip(('d_score', 'd_se'), diff(sc)),
                **dict(zip(('d_le22', 'd_le22_se'), (100 * x for x in diff(lambda r: 1.0 if 0 < int(r['len']) <= 22 else 0.0)))),
                **dict(zip(('d_sub20', 'd_sub20_se'), (100 * x for x in diff(lambda r: 1.0 if 0 < int(r['len']) < 20 else 0.0)))),
                **dict(zip(('d_dnf', 'd_dnf_se'), (100 * x for x in diff(lambda r: 1.0 if int(r['len']) == 0 else 0.0)))))

def summarize(path, ref=None, dnf=30.0):
    by = load(path)
    if ref is None: ref = 'ref' if 'ref' in by else next(iter(by))
    out = []
    for name, rows in by.items():
        d = dict(policy=name, **stats(list(rows.values()), dnf), **paired(rows, by[ref], dnf))
        out.append(d)
    return out, ref

def main():
    a = sys.argv[1:]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    dnf = float(opt('--dnf', 30))
    rows, ref = summarize(a[0], opt('--ref'), dnf)
    if opt('--sort'): rows.sort(key=lambda r: r[opt('--sort')])
    cols = list(rows[0])
    if opt('--out'):
        with open(opt('--out'), 'w') as f:
            f.write('\t'.join(cols) + '\n')
            for r in rows: f.write('\t'.join(f'{r[c]:.4f}' if isinstance(r[c], float) else str(r[c]) for c in cols) + '\n')
    top = int(opt('--top', 10 ** 6))
    print(f'reference: {ref}; DNF counted as {dnf:g} in score')
    print(f"{'policy':<28}{'n':>6}{'mean':>8}{'se':>7}{'dnf%':>6}{'sub20':>7}{'le22':>7}{'score':>8}{'d_score':>9}{'d_se':>7}{'drs':>6}{'fin':>5}{'m_eo':>6}{'m_dr':>6}{'m_fin':>6}")
    for r in rows[:top]:
        print(f"{r['policy']:<28}{r['n']:>6}{r['mean']:>8.3f}{r['se']:>7.3f}{r['dnf']:>6.2f}{r['sub20']:>7.2f}{r['le22']:>7.1f}{r['score']:>8.3f}{r['d_score']:>+9.3f}{r['d_se']:>7.3f}{r['drs']:>6.1f}{r['fin']:>5.1f}{r['m_eo']:>6.1f}{r['m_dr']:>6.1f}{r['m_fin']:>6.1f}")

if __name__ == '__main__':
    main()
