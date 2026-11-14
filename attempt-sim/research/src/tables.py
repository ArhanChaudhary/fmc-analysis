#!/usr/bin/env python3
"""Every table and number of the write-up, from the result files in out/big/ (nothing typed by hand).

Writes report/data/<name>.md (one markdown table each, with its lead sentence left to the write-up) and
report/data/values.json (single numbers used in the prose, read by report_build/assemble.py).
usage: tables.py            (run research/run_all.sh first, or fetch the results)"""
import os, sys, json, csv, math, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import simstats as S

R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
BIG = f'{R}/out/big'
OUT = os.path.normpath(f'{R}/../report/data')
os.makedirs(OUT, exist_ok=True)
V = {}                      # values for the prose
TRAIN = (0, 4000)           # scrambles the policies were chosen on
TEST = (4000, 8000)         # held-out scrambles

def f1(x): return S.fmt(x, 1)
def f2(x): return S.fmt(x, 2)
def pm(x, se, nd=2, sign=False): return f'{S.fmt(x, nd, sign)} ± {S.fmt(se, nd)}'

def table(name, header, rows):
    lines = ['| ' + ' | '.join(header) + ' |', '|' + '|'.join('---' for _ in header) + '|']
    lines += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    with open(f'{OUT}/{name}.md', 'w') as f: f.write('\n'.join(lines) + '\n')

def files(*names): return [f'{BIG}/{n}.tsv' for n in names if os.path.exists(f'{BIG}/{n}.tsv')]

# ------------------------------------------------------------------------------------------------ real results
def real_groups():
    """(label, list of results with 0 = DNF) for the WCA groups and Yura Riabov's log"""
    att = list(csv.DictReader(open(f'{R}/out/wca_top_attempts.tsv'), delimiter='\t'))
    t5 = [max(0, int(r['value'])) for r in att if int(r['solver']) <= 5]
    t10 = [max(0, int(r['value'])) for r in att]
    # Yura Riabov's tracking sheet "FMC Jan-May 2025" (138 attempts, no DNF): counts read off its Result column
    yura = sum(([k] * c for k, c in {18: 3, 19: 6, 20: 14, 21: 24, 22: 38, 23: 32, 24: 15, 25: 5, 26: 1}.items()), [])
    return [('Top 5 by mean, official, since 2024', t5), ('Top 10 by mean, official, since 2024', t10), ("Yura Riabov's log, 2025", yura)]

def dist_row(label, L):
    ok = [x for x in L if x > 0]; n = len(L)
    m = sum(ok) / len(ok); sd = math.sqrt(sum((x - m) ** 2 for x in ok) / (len(ok) - 1))
    pc = lambda f: 100 * sum(1 for x in L if f(x)) / n
    return [label, n, f2(m), f2(sd / math.sqrt(len(ok))), f2(sd), f1(pc(lambda x: x == 0)), f1(pc(lambda x: 0 < x < 20)),
            f1(pc(lambda x: 0 < x <= 22)), f1(pc(lambda x: x >= 24))]

DIST_HEAD = ['Who', 'Attempts', 'Mean, moves', '± SE, moves', 'SD, moves', 'DNF, %', 'Sub-20, %', '≤ 22, %', '24 or more, %']


# ------------------------------------------------------------------------------------------------ section 5
def calibration(train_files, off_files, policy='base'):
    """Section 5: the baseline against real results.  train_files: base on uniform scrambles; off_files: base on the
    official scrambles of the top-10 group (data/official_scrambles.txt, indexed as in out/wca_top_attempts.tsv)."""
    sim = S.load(train_files, *TRAIN, policies={policy})[policy]
    simL = [S.length(r) for r in sim.values()]
    off = S.load(off_files, policies={policy})[policy]
    att = list(csv.DictReader(open(f'{R}/out/wca_top_attempts.tsv'), delimiter='\t'))
    t5 = [r for r in att if int(r['solver']) <= 5 and int(r['scramble']) in off]
    # the simulator on exactly the scrambles of the top 5's attempts, once per attempt
    simoff = [S.length(off[int(r['scramble'])]) for r in t5]
    rows = [dist_row('Simulator, baseline policy, 4,000 random scrambles', simL),
            dist_row("Simulator, baseline policy, the top 5's official scrambles", simoff)]
    rows += [dist_row(lbl, L) for lbl, L in real_groups()]
    table('cal_dist', DIST_HEAD, rows)
    # histogram, % of attempts per result
    groups = [('Simulator', simL), ('Simulator, same scrambles as the top 5', simoff)] + [(l, L) for l, L in real_groups() if 'Top 10' not in l]
    keys = ['DNF', '≤ 18', '19', '20', '21', '22', '23', '24', '25', '26 or more']
    def bucket(x):
        if x == 0: return 'DNF'
        if x <= 18: return '≤ 18'
        if x >= 26: return '26 or more'
        return str(x)
    hrows = []
    for k in keys:
        hrows.append([k] + [f1(100 * sum(1 for x in L if bucket(x) == k) / len(L)) for _, L in groups])
    table('cal_hist', ['Result, moves'] + [f'{g}, % of attempts' for g, _ in groups], hrows)
    # same scramble, real against simulated: correlation and a fit of real on simulated (solved attempts)
    pairs = [(S.length(off[int(r['scramble'])]), int(r['value'])) for r in t5 if int(r['value']) > 0 and S.length(off[int(r['scramble'])]) > 0]
    n = len(pairs); mx = sum(p[0] for p in pairs) / n; my = sum(p[1] for p in pairs) / n
    sxx = sum((p[0] - mx) ** 2 for p in pairs); syy = sum((p[1] - my) ** 2 for p in pairs); sxy = sum((p[0] - mx) * (p[1] - my) for p in pairs)
    V['cal_pairs'] = n; V['cal_corr'] = f2(sxy / math.sqrt(sxx * syy)); V['cal_slope'] = f2(sxy / sxx)
    V['cal_corr_se'] = f2((1 - (sxy / math.sqrt(sxx * syy)) ** 2) / math.sqrt(n - 3))
    # by simulated result: the real mean on those scrambles
    by = collections.defaultdict(list)
    for s_, r_ in pairs: by[min(max(s_, 20), 24)].append(r_)
    lab = {20: '20 or less', 24: '24 or more'}
    table('cal_same', ['Simulated result on the scramble, moves', 'Real attempts', 'Real mean, moves', '± SE, moves'],
          [[lab.get(k, str(k)), len(v), f2(sum(v) / len(v)), f2(S.mse(v)[1])] for k, v in sorted(by.items())])
    d = S.summ(sim)
    V.update(cal_mean=f2(d['mean']), cal_mean_se=f2(d['se']), cal_sd=f2(d['sd']), cal_dnf=f1(d['dnf']), cal_sub20=f1(d['sub20']),
             cal_le22=f1(d['le22']), cal_ge24=f1(d['ge24']), cal_eos=f1(d['eos']), cal_drs=f1(d['drs']), cal_fin=f1(d['fin']),
             cal_rzp=f1(d['rzp']), cal_sw=f1(d['sw']), cal_routes=f1(d['routes']), cal_dr_len=f2(d['dr_len']), cal_opt_from_dr=f1(d['opt_from_dr']),
             cal_m_eo=f1(d['m_eo']), cal_m_dr=f1(d['m_dr']), cal_m_fin=f1(d['m_fin']), cal_m_write=f1(d['m_write']),
             cal_t_res_dr=f1(d['t_res_dr']), cal_t_res_sol=f1(d['t_res_sol']))
    return d

# ------------------------------------------------------------------------------------------------ generic
def stats_for(by, names, ref='base', dnf=S.DNF):
    """{name: (summ, paired vs ref)}"""
    out = {}
    for n in names:
        if n not in by: continue
        out[n] = (S.summ(by[n], dnf), S.paired(by[n], by[ref], dnf) if n != ref else None)
    return out

def diff_cell(p, key, nd=2):
    if p is None: return '0'
    return pm(p[key], p[key + '_se'], nd, sign=True)

def policy_table(name, by, rows, ref='base', first_col='Policy', extra=None):
    """rows: [(label, policy)].  Columns: mean, DNF %, <= 22 %, score difference to ref (DNF = 30), <= 22 difference."""
    st = stats_for(by, [p for _, p in rows] + [ref], ref)
    head = [first_col, 'Mean, moves', 'DNF, %', '≤ 22, %', 'Sub-20, %', f'Score − {"baseline" if ref == "base" else ref}, moves', f'≤ 22 − {"baseline" if ref == "base" else ref}, points']
    out = []
    for label, p in rows:
        if p not in st: continue
        d, pr = st[p]
        out.append([label, f2(d['mean']), f1(d['dnf']), f1(d['le22']), f1(d['sub20']), diff_cell(pr, 'd_score'), diff_cell(pr, 'd_le22', 1)])
    table(name, head, out)
    return st

# ------------------------------------------------------------------------------------------------ features
def feat(r):
    b = [int(x) for x in r['bad'].split('-')]
    return dict(bad_min=b[0], rich=sum(x <= 4 for x in b) >= 2, poor=(b[0] >= 6 and b[2] >= 10), eo_min=int(r['eo_min']), n_eo4=int(r['n_eo4']))

FEATURES = {
    'bad edges, best axis': (lambda f: f['bad_min'], [(lambda v: v <= 2, '0 or 2'), (lambda v: v == 4, '4'), (lambda v: v >= 6, '6 or more')]),
    'scramble type (bad edges)': (lambda f: ('rich' if f['rich'] else 'poor' if f['poor'] else 'middle'),
                                  [(lambda v: v == 'rich', 'rich: two axes with 4 or fewer'), (lambda v: v == 'middle', 'neither'), (lambda v: v == 'poor', 'poor: none with 4 or fewer, one with 10 or more')]),
    'shortest EO': (lambda f: f['eo_min'], [(lambda v: v <= 2, '2 or less'), (lambda v: v == 3, '3'), (lambda v: v == 4, '4'), (lambda v: v >= 5, '5 or more')]),
    'EOs of 4 moves or less': (lambda f: f['n_eo4'], [(lambda v: v <= 4, '0 to 4'), (lambda v: 5 <= v <= 14, '5 to 14'), (lambda v: 15 <= v <= 29, '15 to 29'), (lambda v: v >= 30, '30 or more')]),
}

def bucket_of(r, fname):
    fn, bs = FEATURES[fname]
    v = fn(feat(r))
    for test, lab in bs:
        if test(v): return lab
    return None

def per_bucket(by, policies, fname, ref='base', dnf=S.DNF):
    """{bucket: {policy: (n, mean score, paired d_score vs ref, se)}}"""
    out = collections.OrderedDict((lab, {}) for _, lab in FEATURES[fname][1])
    refrows = by[ref]
    for p in policies:
        if p not in by: continue
        groups = collections.defaultdict(list)
        for s, r in by[p].items():
            if s in refrows: groups[bucket_of(refrows[s], fname)].append(s)
        for lab, ss in groups.items():
            sc = [S.score(by[p][s], dnf) for s in ss]
            d = [S.score(by[p][s], dnf) - S.score(refrows[s], dnf) for s in ss]
            m, se = S.mse(d)
            out[lab][p] = (len(ss), sum(sc) / len(sc), m, se)
    return out

# ------------------------------------------------------------------------------------------------ section 6 / 10: E1 and E5
E1_TEO = (180, 300, 480, 720, 960)
E1_TDR = (900, 1200, 1500, 1800, 2100, 2400, 2700, 3000)

def e1_tables(by, ref='base'):
    st = stats_for(by, [f'e1_teo{te}_tdr{td}' for te in E1_TEO for td in E1_TDR if td > te] + [ref], ref)
    # compact: score - baseline by (EO stop, DR stop)
    cols = (1500, 1800, 2100, 2400, 2700)
    rows = []
    for te in E1_TEO:
        r = [f'{te // 60}']
        for td in cols:
            k = f'e1_teo{te}_tdr{td}'
            r.append(diff_cell(st[k][1], 'd_score') if k in st else '-')
        rows.append(r)
    table('e1_grid', ['EO writing stops, minute'] + [f'DR search stops at {td // 60}: score − baseline, moves' for td in cols], rows)
    # long form for the appendix
    rows = []
    for te in E1_TEO:
        for td in E1_TDR:
            k = f'e1_teo{te}_tdr{td}'
            if k not in st: continue
            d, p = st[k]
            rows.append([te // 60, td // 60, f2(d['mean']), f1(d['dnf']), f1(d['le22']), diff_cell(p, 'd_score'), f1(d['m_eo']), f1(d['m_fin'])])
    table('e1_long', ['EO writing stops, minute', 'DR search stops, minute', 'Mean, moves', 'DNF, %', '≤ 22, %', 'Score − baseline, moves', 'Minutes on EOs', 'Minutes finishing'], rows)
    best = min((k for k in st if k.startswith('e1_')), key=lambda k: st[k][0]['score'])
    return st, best

E5_KEYS = [('eo_cap', 'EOs written at most (no time limit on writing)', 'EOs'), ('eo_len', 'longest EO looked for', 'moves'),
           ('rzp_per_eo', 'RZP states worked per EO of 4 moves or less', 'states'), ('rzp_per_eo_long', 'RZP states worked per 5-move EO', 'states'),
           ('read_max', 'work an RZP state only if its read promises a DR of at most', 'moves'), ('rzp_depth', 'RZP moves at most', 'moves'),
           ('rzp_more', 'extra RZP states per EO on each pass back', 'states'), ('dr_per_line', 'DRs taken from one EO ending and axis', 'DRs'),
           ('switch_pen', 'a switch ranked this much worse than staying', 'moves'), ('dr_cap', 'longest DR written', 'moves'),
           ('t_dr', 'DR search stops', 'minute'), ('htr_per_dr', 'routes tried per DR', 'routes'),
           ('fin_min_p', 'skip a DR whose chance of beating the best so far is under', '%'), ('fin_max', 'DRs taken to a finish at most', 'DRs'),
           ('reserve', 'time kept for writing the solution', 'minutes')]

def e5_tables(by, ref='base'):
    base = {'eo_cap': 40, 'eo_len': 5, 'rzp_per_eo': 3, 'rzp_per_eo_long': 1, 'read_max': 11.5, 'rzp_depth': 3, 'rzp_more': 2, 'dr_per_line': 1,
            'switch_pen': 0.3, 'dr_cap': 11, 't_dr': 2100, 'htr_per_dr': 4, 'fin_min_p': 0.03, 'fin_max': 99, 'reserve': 300}
    out = {}
    for key, label, unit in E5_KEYS:
        names = sorted([n for n in by if n.startswith(f'e5_{key}_') and not any(n.startswith(f'e5_{k2}_') and len(k2) > len(key) for k2, _, _ in E5_KEYS)],
                       key=lambda n: float(n[len(f'e5_{key}_'):].replace('p', '.')))
        vals = [(float(n[len(f'e5_{key}_'):].replace('p', '.')), n) for n in names] + [(base[key], ref)]
        vals.sort(key=lambda x: x[0])
        st = stats_for(by, [n for _, n in vals] + [ref], ref)
        def show(v):
            if key in ('t_dr',): return f'{v / 60:g}'
            if key == 'reserve': return f'{v / 60:g}'
            if key == 'fin_min_p': return f'{100 * v:g}'
            if key == 'fin_max' and v >= 99: return 'no limit'
            if key == 'switch_pen' and v >= 99: return 'never switch'
            return f'{v:g}'
        rows = []
        for v, n in vals:
            if n not in st: continue
            d, p = st[n]
            rows.append([show(v) + (' (baseline)' if n == ref else ''), f2(d['mean']), f1(d['dnf']), f1(d['le22']), f1(d['sub20']), diff_cell(p, 'd_score')])
        table(f'e5_{key}', [f'{label[0].upper() + label[1:]}, {unit}', 'Mean, moves', 'DNF, %', '≤ 22, %', 'Sub-20, %', 'Score − baseline, moves'], rows)
        out[key] = st
    return out

# ------------------------------------------------------------------------------------------------ round 3: around the tuned plan
# The tuned plan ("ref") was chosen on round 2's training scrambles (0-3,399); every comparison below is on the held-out
# scrambles 4,000-7,999 (round 3: every experiment again, around ref).  Policy names there carry the prefix t (te1_...).
REF_PARAMS = dict(read_max=10, reserve=420, switch_pen=0)
def lab_ref(): return 'tuned plan'

def round3(prefix='r3_t', lo=4, hi=8):
    return S.load(files(*[f'{prefix}{i}' for i in range(lo, hi)]), *TEST)

def table_vs_ref(name, by, rows, first_col):
    """rows: [(label, policy)], compared with ref on the same scrambles"""
    st = stats_for(by, [p for _, p in rows] + ['ref'], 'ref')
    head = [first_col, 'Mean, moves', 'DNF, %', '≤ 22, %', 'Sub-20, %', 'Score − tuned plan, moves', '≤ 22 − tuned plan, points']
    out = []
    for label, p in rows:
        if p not in st: continue
        d, pr = st[p]
        out.append([label, f2(d['mean']), f1(d['dnf']), f1(d['le22']), f1(d['sub20']), diff_cell(pr, 'd_score', 3), diff_cell(pr, 'd_le22', 1)])
    table(name, head, out)
    return st

def r3_tables(by):
    st = stats_for(by, list(by), 'ref')
    # the tuned plan itself, and the baseline, on the held-out scrambles
    d = st['ref'][0]; b, pb = st['base']
    V.update(ref_mean=f2(d['mean']), ref_mean_se=f2(d['se']), ref_dnf=f1(d['dnf']), ref_le22=f1(d['le22']), ref_sub20=f1(d['sub20']),
             ref_score=f2(d['score']), base_mean=f2(b['mean']), base_dnf=f1(b['dnf']), base_le22=f1(b['le22']), base_score=f2(b['score']),
             base_minus_ref=pm(pb['d_score'], pb['d_score_se'], 2, True), ref_eos=f1(d['eos']), ref_rzp=f1(d['rzp']), ref_drs=f1(d['drs']),
             ref_fin=f1(d['fin']), ref_routes=f1(d['routes']), ref_m_eo=f1(d['m_eo']), ref_m_dr=f1(d['m_dr']), ref_m_fin=f1(d['m_fin']),
             ref_m_write=f1(d['m_write']), ref_t_res_dr=f1(d['t_res_dr']), ref_t_res_sol=f1(d['t_res_sol']), test_n=f"{d['n']:,}")
    # E1: the time split
    cols = (1200, 1500, 1800, 2100, 2400, 2700, 3000)
    rows = []
    for te in E1_TEO:
        r = [f'{te // 60}']
        for td in cols:
            k = f'te1_teo{te}_tdr{td}'
            r.append(diff_cell(st[k][1], 'd_score', 3) if k in st else '–')
        rows.append(r)
    table('r3_e1_grid', ['EO writing stops, minute'] + [f'DR search stops at minute {td // 60}' for td in cols], rows)
    e1 = {k: v for k, v in st.items() if k.startswith('te1_')}
    V['e1_n'] = len(e1)
    V['e1_within'] = sum(1 for k, v in e1.items() if abs(v[1]['d_score']) <= 0.02)
    V['e1_worst'] = f2(max(v[1]['d_score'] for v in e1.values()))
    # E2: order
    table_vs_ref('r3_e2', by, [
        ('the tuned plan (breadth first: all EOs, then DRs, then finishes)', 'ref'),
        ('depth first: each EO of 3 straight to DR, then each DR straight to a finish', 'te2_dfs_eo3'),
        ('depth first throughout', 'te2_dfs'),
        ('depth first, one route per DR', 'te2_dfs_r1'),
        ('EOs of 2 moves or less straight to DR', 'te2_eagereo2'),
        ('EOs of 4 moves or less straight to DR', 'te2_eagereo4'),
        ('a DR that promises 22 or better: one route at once', 'te2_eagerfin22p5_r1'),
        ('a DR that promises 23 or better: one route at once', 'te2_eagerfin23p5_r1'),
        ('every DR: all its routes at once', 'te2_eagerfin99_r99'),
        ('a backup: best DR finished by minute 10', 'te2_backup600'),
        ('a backup by minute 20', 'te2_backup1200'),
        ('a backup by minute 30', 'te2_backup1800'),
        ('a backup by minute 40', 'te2_backup2400')], 'Plan')
    # E3: adaptive
    table_vs_ref('r3_e3', by, [
        ('the tuned plan (fixed times)', 'ref'),
        ('rich in EOs (25+ found): DR search to minute 30', 'te3_rich25_tdr1800'),
        ('rich in EOs (25+ found): DR search to minute 45', 'te3_rich25_tdr2700'),
        ('poor in EOs (under 10 of 4 or less): 5-movers too, else 4 only', 'te3_poor10'),
        ('EOs of 4 or less only', 'te3_eo4only'),
        ('no DR of 9 by minute 25: DR search to minute 45', 'te3_late9_tdr2700'),
        ('stop the DR search once 2 DRs of 9 are written', 'te3_enough2_len9'),
        ('stop the DR search once 1 DR of 8 is written', 'te3_enough1_len8'),
        ('a 22 on the sheet: DR search to minute 45', 'te3_bk22_tdr2700'),
        ('a 23 on the sheet: DR search to minute 50', 'te3_bk23_tdr3000'),
        ('DR search to 25, or 40 without a DR of 9', 'te3_early1500_late9_2400')], 'Plan')
    # E4: safety, with the reserve curve
    rows = [(f'{rs // 60}{":30" if rs % 60 else ""} minutes kept for writing', f'te4_reserve{rs}') for rs in (150, 180, 210, 240, 270, 360)]
    rows.insert(6, ('7 minutes kept for writing (the tuned plan)', 'ref'))
    rows += [('10 minutes kept for writing', 'te4_reserve600')]
    rows += [('a DR that promises 22 or better: one route at once, bank a 22', 'te4_quick22p5_r1'),
             ('the same for 23 or better', 'te4_quick23p5_r1'),
             ('bank every result at once (then 3 minutes to rewrite)', 'te4_bankalways'),
             ('bank the first result', 'te4_bankfirst_rr180'),
             ('commit: DR search stops at minute 25, bank a 22', 'te4_commit1500')]
    table_vs_ref('r3_e4', by, rows, 'Plan')
    # E5: one decision at a time, around the tuned plan
    basev = {'eo_cap': 40, 'eo_len': 5, 'rzp_per_eo': 3, 'rzp_per_eo_long': 1, 'read_max': 10, 'rzp_depth': 3, 'rzp_more': 2, 'dr_per_line': 1,
             'switch_pen': 0, 'dr_cap': 11, 't_dr': 2100, 'htr_per_dr': 4, 'fin_min_p': 0.03, 'fin_max': 99, 'reserve': 420}
    for key, label, unit in E5_KEYS:
        names = [n for n in by if n.startswith(f'te5_{key}_') and not any(n.startswith(f'te5_{k2}_') and len(k2) > len(key) for k2, _, _ in E5_KEYS)]
        vals = sorted([(float(n[len(f'te5_{key}_'):].replace('p', '.')), n) for n in names if float(n[len(f'te5_{key}_'):].replace('p', '.')) != basev[key]] + [(basev[key], 'ref')])
        def show(v):
            if key in ('t_dr', 'reserve'): return f'{v / 60:g}'
            if key == 'fin_min_p': return f'{100 * v:g}'
            if key == 'fin_max' and v >= 99: return 'no limit'
            if key == 'switch_pen' and v >= 99: return 'never switch'
            return f'{v:g}'
        out = []
        for v, n in vals:
            if n not in st: continue
            d, p = st[n]
            out.append([show(v) + (' (tuned plan)' if n == 'ref' else ''), f2(d['mean']), f1(d['dnf']), f1(d['le22']), diff_cell(p, 'd_score', 3)])
        table(f'r3_e5_{key}', [f'{label[0].upper() + label[1:]}, {unit}', 'Mean, moves', 'DNF, %', '≤ 22, %', 'Score − tuned plan, moves'], out)
    # every plan's numbers by name, for the prose: d_<policy> (score - tuned plan, 3 decimals with SE), dd_<policy> (the same without
    # the SE), le22_<policy>, dle22_<policy>, mean_<policy>, dnf_<policy>
    for k, (d, p) in st.items():
        V[f'mean_{k}'] = f2(d['mean']); V[f'dnf_{k}'] = f1(d['dnf']); V[f'le22_{k}'] = f1(d['le22'])
        if p:
            V[f'd_{k}'] = pm(p['d_score'], p['d_score_se'], 3, True); V[f'dd_{k}'] = S.fmt(p['d_score'], 2, True)
            V[f'dle22_{k}'] = pm(p['d_le22'], p['d_le22_se'], 1, True)
    # appendix: every plan
    rows = []
    for k in sorted(st, key=lambda k: st[k][0]['score']):
        d, p = st[k]
        rows.append([f'`{k}`', f2(d['mean']), f1(d['dnf']), f1(d['le22']), f1(d['sub20']), diff_cell(p, 'd_score', 3) if p else '0'])
    table('r3_all', ['Plan (policy name)', 'Mean, moves', 'DNF, %', '≤ 22, %', 'Sub-20, %', 'Score − tuned plan, moves'], rows)
    return st

def round2_ingredients():
    """why the tuned plan: each of its three changes alone, against the baseline, round 2's held-out scrambles"""
    by = S.load(files('r2_te_a', 'r2_te_b', 'r2_te_c', 'r2_te_d'), *TEST,
                policies={'base', 'e5_read_max_10', 'e4_reserve420', 'e5_switch_pen_0', 'e5_switch_pen_99', 'e5_fin_max_1'})
    stx = stats_for(by, ['base', 'e5_read_max_10', 'e4_reserve420', 'e5_switch_pen_0', 'e5_switch_pen_99', 'e5_fin_max_1'], 'base')
    for k, (d, p) in stx.items():
        if p: V[f'r2d_{k}'] = pm(p['d_score'], p['d_score_se'], 2, True)
    V['r2_base_dnf'] = f1(stx['base'][0]['dnf']); V['r2_reserve_dnf'] = f1(stx['e4_reserve420'][0]['dnf'])
    st = policy_table('r2_ingredients', by, [('baseline', 'base'), ('only work an RZP whose read promises a DR of 10 or less (baseline 11.5)', 'e5_read_max_10'),
                                             ('keep 7 minutes for writing (baseline 5)', 'e4_reserve420'), ('switch as readily as staying (baseline: a switch ranked 0.3 worse)', 'e5_switch_pen_0'),
                                             ('never switch', 'e5_switch_pen_99'), ('finish only one DR', 'e5_fin_max_1')], 'base', 'Change to the baseline')
    return st

def budget_tables():
    rows = []
    for b in (1200, 1800, 2700, 3600, 4500, 5400, 7200):
        nm = f'r4_b{b}'
        p = f'{BIG}/{nm}.tsv' if os.path.exists(f'{BIG}/{nm}.tsv') else None
        sm = f'{BIG}/from_fmc3/{nm}.summary.txt'
        if p:
            by = S.load([p]); d = S.summ(by['ref']); db = S.summ(by['base']); pr = S.paired(by['ref'], by['base'])
            rows.append([f'{b // 60}', f2(d['mean']), f1(d['dnf']), f1(d['le22']), f1(d['sub20']), f2(db['mean']), f1(db['dnf']), diff_cell(pr, 'd_score')])
        elif os.path.exists(sm):
            L = {l.split()[0]: l for l in open(sm) if l.startswith(('base ', 'ref '))}
            def g(line, key):
                t = line.split(); return t[t.index(key) + 1].rstrip('%')
            rows.append([f'{b // 60}', g(L['ref'], 'mean'), g(L['ref'], 'dnf'), g(L['ref'], '<=22'), g(L['ref'], 'sub20'), g(L['base'], 'mean'), g(L['base'], 'dnf'), '–'])
    table('r4_budget', ['Length of the attempt, minutes', 'Tuned plan: mean, moves', 'Tuned plan: DNF, %', 'Tuned plan: ≤ 22, %', 'Tuned plan: sub-20, %', 'Baseline: mean, moves', 'Baseline: DNF, %', 'Tuned − baseline score, moves'], rows)

def solver_table():
    """section 10: the same plans for a faster or sharper solver (2,000 held-out scrambles each)"""
    rows = []
    for nm, lbl in [('r4_x2', 'every step twice as slow (same as 30 minutes)'), ('r4_x14', 'every step 1.4 times as slow'), ('r4_b3600', 'the costs of section 4'),
                    ('r4_x07', 'every step 0.7 times as long'), ('r4_x05', 'every step half as long (same as 2 hours)'),
                    ('r4_read05', 'reading error of an RZP state halved (0.5 moves)'), ('r4_drsee_hi', 'sees more of the DRs near an RZP state'),
                    ('r4_top', 'all three: half as long, sharper read, sees more DRs')]:
        if not os.path.exists(f'{BIG}/{nm}.tsv'): continue
        by = S.load([f'{BIG}/{nm}.tsv']); d = S.summ(by['ref']); db = S.summ(by['base'])
        rows.append([lbl, f2(d['mean']), f1(d['dnf']), f1(d['le22']), f1(d['sub20']), f2(db['mean'])])
        if nm == 'r4_top': V['top_mean'] = f2(d['mean']); V['top_sub20'] = f1(d['sub20']); V['top_le22'] = f1(d['le22'])
    table('r4_solver', ['Solver', 'Tuned plan: mean, moves', 'DNF, %', '≤ 22, %', 'Sub-20, %', 'Baseline: mean, moves'], rows)

SENS = [('look', 'look at the scramble (bad edges)'), ('eo_scan', 'scan for EOs'), ('eo_write', 'write an EO'), ('eo_eval', 'glance at an EO'),
        ('rzp', 'work an RZP state'), ('switch', 'switch'), ('dr_find', 'write a DR'), ('dr_read', 'read a DR'), ('htr', 'try an HTR route'),
        ('tail', 'write out a finish'), ('write', 'write the solution (and the reserve with it)'), ('noise', 'spread of step times')]
HUMAN = [('read', 'reading error of an RZP state', '0.5', '2'), ('route', 'a route gives its finish', '0.7', '1'), ('drsee', 'DRs seen', 'fewer', 'more'),
         ('eosee', 'EOs seen', 'fewer', 'more')]
CONCL = [('te1_teo300_tdr1500', 'EO writing to minute 5, DR search to 25'), ('te1_teo720_tdr2700', 'EO writing to minute 12, DR search to 45'),
         ('te1_teo960_tdr3000', 'EO writing to minute 16, DR search to 50'), ('te2_dfs', 'depth first throughout'),
         ('te2_eagerfin22p5_r1', 'quick route on a DR promising 22'), ('te2_backup1200', 'a backup by minute 20'),
         ('te3_rich25_tdr1800', 'rich in EOs: DR search to 30'), ('te3_poor10', '5-movers only when poor in EOs'), ('te3_bk22_tdr3000', 'a 22 on the sheet: DR search to 50'),
         ('te4_quick22p5_r1', 'quick route on a DR promising 22, bank a 22'), ('te4_commit1500', 'commit: DR search stops at 25'), ('te4_reserve600', '10 minutes kept for writing'),
         ('te5_rzp_per_eo_1', '1 RZP state per short EO'), ('te5_rzp_per_eo_8', '8 RZP states per short EO'),
         ('te5_read_max_9', 'read cut-off 9'), ('te5_read_max_11', 'read cut-off 11'), ('te5_htr_per_dr_2', '2 routes per DR'), ('te5_htr_per_dr_8', '8 routes per DR'),
         ('te5_fin_max_2', 'finish at most 2 DRs'), ('te5_eo_len_4', 'EOs of 4 or less only'), ('te5_switch_pen_99', 'never switch'),
         ('te5_eo_cap_20', 'write at most 20 EOs'), ('te5_t_dr_1200', 'DR search stops at 20'), ('te5_t_dr_2700', 'DR search stops at 45'), ('base', 'the baseline')]

def sensitivity():
    """section 11: each conclusion (a plan against the tuned plan) with every cost halved and doubled, 2,000 held-out scrambles"""
    runs = [('s_ref', 'costs as in section 4')]
    for k, lbl in SENS:
        runs += [(f's_{k}_h', f'{lbl}: half'), (f's_{k}_d', f'{lbl}: double')]
    for k, lbl, lo, hi in HUMAN:
        sfx = ('lo', 'hi') if k in ('route', 'drsee', 'eosee') else ('h', 'd')
        runs += [(f's_{k}_{sfx[0]}', f'{lbl}: {lo}'), (f's_{k}_{sfx[1]}', f'{lbl}: {hi}')]
    have = [(n, l) for n, l in runs if os.path.exists(f'{BIG}/{n}.tsv')]
    if len(have) < 2: return None
    res = {}
    for n, l in have:
        by = S.load([f'{BIG}/{n}.tsv'])
        res[n] = {p: S.paired(by[p], by['ref']) for p in by if p != 'ref'}
    rows = []
    for p, lbl in CONCL:
        if p not in res['s_ref']: continue
        d0 = res['s_ref'][p]['d_score']; se0 = res['s_ref'][p]['d_score_se']
        ds = [(res[n][p]['d_score'], res[n][p]['d_score_se'], l) for n, l in have if p in res[n]]   # the costs of section 4 included
        sig = lambda d, se: 'better' if d < -2 * se else 'worse' if d > 2 * se else 'level'
        cnt = {k: sum(1 for d, se, _ in ds if sig(d, se) == k) for k in ('better', 'level', 'worse')}
        major = 'better' if cnt['better'] > cnt['worse'] else 'worse' if cnt['worse'] > cnt['better'] else None
        other = {'better': 'worse', 'worse': 'better'}.get(major)
        opp = [l for d, se, l in ds if other and sig(d, se) == other]
        rows.append([lbl, pm(d0, se0, 2, True), f2(min(d for d, _, _ in ds)), f2(max(d for d, _, _ in ds)),
                     str(cnt['better']), str(cnt['level']), str(cnt['worse']), '; '.join(opp) if opp else 'none'])
    table('sens', ['Plan, against the tuned plan', 'Score difference, costs of section 4', 'Smallest difference over all runs', 'Largest difference',
                   'Runs where it is better', 'Runs where it is level', 'Runs where it is worse', 'Runs where it goes the other way'], rows)
    V['sens_runs'] = len(have) - 1
    # the tuned plan's own result under each moved cost: which costs move the result most (what to tune first)
    base_m = None; rows = []
    for n, l in have:
        by = S.load([f'{BIG}/{n}.tsv'], policies={'ref'}); d = S.summ(by['ref'])
        if n == 's_ref': base_m = d['score']
        rows.append((n, l, d['mean'], d['dnf'], d['le22'], d['score']))
    rows.sort(key=lambda r: -abs(r[5] - base_m))
    table('sens_ref', ['Cost or limit moved', 'Tuned plan: mean, moves', 'DNF, %', '≤ 22, %', 'Score change from section 4 costs, moves'],
          [[l, f2(m), f1(dn), f1(le), S.fmt(sc - base_m, 2, True)] for n, l, m, dn, le, sc in rows])
    return res

def main():
    by3 = round3()
    st = r3_tables(by3)
    round2_ingredients()
    budget_tables()
    solver_table()
    calibration(files('r3_t0', 'r3_t1', 'r3_t2', 'r3_t3'), files('r5_off'))
    t5 = [x for lbl, L in real_groups() if lbl.startswith('Top 5') for x in L]
    ok = [x for x in t5 if x > 0]
    V['real_t5_n'] = f'{len(t5):,}'; V['real_t5_mean'] = f2(sum(ok) / len(ok))
    V['cal_attempt_sigma'] = '0.15'; V['cal_form_sigma'] = '0'
    att = list(csv.DictReader(open(f'{R}/out/wca_top_attempts.tsv'), delimiter='\t'))
    V['n_off_scr'] = f"{len({r['scramble'] for r in att if int(r['solver']) <= 5}):,}"
    V['n_train'] = '3,400'                 # round 2's training scrambles (0 to 3,399), where the tuned plan was chosen
    V['n_test'] = f"{TEST[1] - TEST[0]:,}"
    sensitivity()
    per_type_plans()
    json.dump(V, open(f'{OUT}/values.json', 'w'), indent=1, ensure_ascii=False)
    print('tables and', len(V), 'values written to', OUT)


# ------------------------------------------------------------------------------------------------ section 8: a plan per scramble type
def light_load(names, keep_scr):
    """policy -> {scr: score} and scr -> feature row, from round-3 files, keeping only what this needs"""
    sc = collections.defaultdict(dict); fr = {}
    for p in files(*names):
        with open(p) as f:
            for r in csv.DictReader(f, delimiter='\t'):
                s = int(r['scr'])
                if not keep_scr(s): continue
                sc[r['policy']][s] = S.score(r)
                if s not in fr: fr[s] = {'bad': r['bad'], 'eo_min': r['eo_min'], 'n_eo4': r['n_eo4']}
    return sc, fr

def per_type_plans():
    """Choose, per scramble type, the plan with the best score on the training scrambles (0-3,999 of round 3), then score
    that choice on the held-out scrambles (4,000-7,999) against the tuned plan.  One row per feature: the plan chosen
    for each type, and the held-out gain of playing each type's plan."""
    tr, ftr = light_load([f'r3_t{i}' for i in range(4)], lambda s: TRAIN[0] <= s < TRAIN[1])
    te, fte = light_load([f'r3_t{i}' for i in range(4, 8)], lambda s: TEST[0] <= s < TEST[1])
    rows = []
    for fname in FEATURES:
        chosen = {}
        for _, lab in FEATURES[fname][1]:
            ss = [s for s in ftr if bucket_of(ftr[s], fname) == lab]
            if not ss: continue
            best = min(tr, key=lambda p: sum(tr[p][s] for s in ss) / len(ss))
            chosen[lab] = (best, sum(tr[best][s] - tr['ref'][s] for s in ss) / len(ss), len(ss))
        d = [te[chosen[bucket_of(fte[s], fname)][0]][s] - te['ref'][s] for s in fte if bucket_of(fte[s], fname) in chosen]
        m, se = S.mse(d)
        desc = '; '.join(f"{lab}: `{c[0]}` (training {S.fmt(c[1], 3, True)})" for lab, c in chosen.items())
        rows.append([fname, desc, pm(m, se, 3, True)])
        V[f'pertype_{fname.split()[0]}'] = pm(m, se, 3, True)
    table('pertype', ['Scramble feature', 'Plan chosen per type on the training scrambles (its gain there)', 'Held-out: score − tuned plan, moves'], rows)

if __name__ == '__main__':
    main()
