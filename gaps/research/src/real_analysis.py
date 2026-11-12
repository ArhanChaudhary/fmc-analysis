#!/usr/bin/env python3
"""Gap 1 (b): the htr-routes headline outputs on the real DR population, through the htr-routes code itself.

htr-routes' src/common.py, checklist_cost.py and grade.py are imported from their own folder (read only) and pointed
at a run directory; only the weighting is new: every function that pooled states by `SIZE[s] / n` (uniform states,
pooled by exact subset size) here takes one weight per state, and every share gets a standard error clustered by
scramble (DRs of one scramble are not independent).  Selection (greedy class order) is taken as fixed for the SE.

Runs:
  uniform   htr-routes out/big/run1 (25,000 uniform states per subset x edges), bound4 on its first 4,000;
            weight SIZE[s] / n, each state its own cluster.  Must reproduce htr-routes' published tables exactly.
  real      big/real/run (htrtools gaps fork, GAPS_STATES = big/real/list.txt), bound4 on the same states;
            weights from big/real/meta.tsv for the populations dr11, scr11, dr10, scr10, cluster = scramble.

Outputs (out/):
  b_checklist.tsv    per group (corner subset, subset x edges) and population: the greedy budget-2 checklist (level C,
                     target optimal): class 1-3, cumulative share after 1/2/3 and +1 after 3, with SE; and the uniform
                     checklist's three classes evaluated on the population ("uniform classes")
  b_grades.tsv       the hand checklists of htr-routes Q6 (Zagros, Yura, rogo/Adri, Lewis, Jay, Fanti, Daichi), budget 2
                     and no limit, optimal and +1, cumulative per step, with SE
  b_bounding.tsv     Q8 as stated: share where a reduction of <= R moves (R = 0..7) to 1q / 2q followed by the optimal
                     finish of the reduced state gives an optimal (and +1), per corner subset / subset x edges / all
  b_q3.tsv           Q3 per group: linear vs NISS shortest HTR, optimal through a shortest HTR, HTR means
usage: real_analysis.py [part ...]   parts: checklist grades bounding q3 (default all)"""
import sys, os, csv, collections, importlib
import numpy as np
HR = '/data/fmc/htr-routes/research'
sys.path.insert(0, f'{HR}/src')
import common
G = '/data/fmc/gaps/research'
OUTD = f'{G}/out'
TMP = f'{G}/big/real/tmp'
os.makedirs(TMP, exist_ok=True)
common.OUT = TMP            # anything the imported modules write goes here, never into htr-routes
RUNS = {'uniform': (f'{HR}/out/big/run1', f'{HR}/out/big/bound4.tsv'),
        'real': (f'{G}/big/real/run', f'{G}/big/real/bound4.tsv')}
POPS = {'uniform': ['uniform'], 'real': ['dr11', 'scr11', 'dr10', 'scr10']}
SUBS, SIZE, CORNER, CGROUPS = common.SUBS, common.SIZE, common.CORNER, common.CGROUPS

def set_run(run):
    common.RUN = RUNS[run][0]; common._keys = None; common._alias = None
    import checklist_cost, grade
    importlib.reload(checklist_cost); importlib.reload(grade)
    checklist_cost.load_aliases()
    grade.K = common.keys(); grade._pc.clear(); grade._rt.clear()
    return checklist_cost, grade

_meta = None
def meta():
    """(subset, i) -> row of big/real/meta.tsv, as per-subset arrays"""
    global _meta
    if _meta is None:
        cols = collections.defaultdict(lambda: collections.defaultdict(list))
        for r in csv.DictReader(open(f'{G}/big/real/meta.tsv'), delimiter='\t'):
            c = cols[r['subset']]
            for k in ('scr', 'len', 'w_dr11', 'w_scr11', 'w_dr10', 'w_scr10'): c[k].append(float(r[k]))
        _meta = {s: {k: np.array(v) for k, v in c.items()} for s, c in cols.items()}
    return _meta

def weights(run, pop, s, n, idx=None):
    """per-state weight and cluster id of the n states of subset s (idx: their state indices, default 0..n-1)"""
    idx = np.arange(n) if idx is None else np.asarray(idx)
    if run == 'uniform':
        return np.full(len(idx), SIZE[s] / n), SUBS.index(s) * 10 ** 7 + idx
    m = meta()[s]
    return m['w_' + pop][idx], m['scr'][idx].astype(np.int64)

def wstat(x, w, cl):
    """weighted mean and its standard error, clusters cl (linearised ratio estimator, K/(K-1) correction)"""
    x = np.asarray(x, float); w = np.asarray(w, float)
    keep = w > 0
    x, w, cl = x[keep], w[keep], np.asarray(cl)[keep]
    W = w.sum()
    if W <= 0 or len(x) == 0: return float('nan'), float('nan'), 0
    p = (w * x).sum() / W
    _, inv = np.unique(cl, return_inverse=True)
    t = np.bincount(inv, weights=w * (x - p))
    K = len(t)
    se = np.sqrt((t ** 2).sum() * K / max(K - 1, 1)) / W
    return p, se, K

def groups_of():
    return [(s, [s]) for s in SUBS] + [(g, [s for s in SUBS if CORNER(s) == g]) for g in CGROUPS]

# ------------------------------------------------------------------ checklist (Q2, budget 2, level C)
def checklist(f, run, cc, uni_classes):
    """writes rows for every population of the run; returns {group: [class names]} chosen (first population)"""
    chosen = {}
    mem = {s: cc.member(s) for s in SUBS}          # (n, {(lv, tg, b): (state idx, class idx)})
    for pop in POPS[run]:
        for g, subs in groups_of():
            S, C, S1, C1, W, CL = [], [], [], [], [], []; off = 0
            for s in subs:
                n, out = mem[s]
                w, cl = weights(run, pop, s, n)
                a, b = out[('C', 'opt', 2)]; S.append(a + off); C.append(b)
                a, b = out[('C', 'p1', 2)]; S1.append(a + off); C1.append(b)
                W.append(w); CL.append(cl); off += n
            si, ci, si1, ci1 = map(np.concatenate, (S, C, S1, C1)); w = np.concatenate(W); cl = np.concatenate(CL)
            if w.sum() <= 0: continue
            res = cc.greedy(si, ci, w, 'C', steps=3)
            cls_idx = [r[0] for r in res]
            names = [cc.names['C'][c] for c in cls_idx]
            if pop == POPS[run][0]: chosen[g] = names
            def cover(classes):
                vals = []
                for k in range(1, 4):
                    cv = np.zeros(off, bool); cv[si[np.isin(ci, classes[:k])]] = True; vals.append(cv)
                cv = np.zeros(off, bool); cv[si1[np.isin(ci1, classes[:3])]] = True; vals.append(cv)
                return [wstat(v, w, cl) for v in vals]
            st = cover(cls_idx)
            line = [g, run, pop, 'own'] + names + [''] * (3 - len(names))
            f.write('\t'.join(line + [f'{p:.4f}\t{se:.4f}' for p, se, _ in st] + [str(st[0][2])]) + '\n')
            if uni_classes is not None and g in uni_classes:
                ids = [cc.ids['C'].get(nm, -2) for nm in uni_classes[g]]
                st = cover(ids)
                line = [g, run, pop, 'uniform classes'] + uni_classes[g] + [''] * (3 - len(uni_classes[g]))
                f.write('\t'.join(line + [f'{p:.4f}\t{se:.4f}' for p, se, _ in st] + [str(st[0][2])]) + '\n')
        f.flush()
        print('checklist', run, pop, flush=True)
    return chosen

# ------------------------------------------------------------------ hand checklists (Q6)
def grades(f, run, gr):
    L = gr.checklists()
    for pop in POPS[run]:
        for name, subs, steps in L:
            for target in ('opt', 'p1'):
                for budget in (2, 99):
                    firsts, W, CL = [], [], []
                    for s in subs:
                        rt = gr.routes(s)
                        m = (rt.delta == 0) if target == 'opt' else np.ones(len(rt.rid), bool)
                        hh = rt.htr if target == 'opt' else rt.htr1
                        if budget < 99:
                            niss = common.load_states(s)['htrNiss']
                            m &= hh <= niss[rt.state] + budget
                        pair = rt.rid[m] * 32 + hh[m]
                        u, inv = np.unique(pair, return_inverse=True)
                        stepof = np.full(len(u), len(steps))
                        for k, x in enumerate(u):
                            p = gr.P(int(x >> 5))
                            if not p: continue
                            cn, labs, sw, post, nq = p
                            for si_, (_, pred) in enumerate(steps):
                                if pred(cn, labs, sw, post, nq, int(x & 31)):
                                    stepof[k] = si_; break
                        first = np.full(rt.n, len(steps))
                        np.minimum.at(first, rt.state[m], stepof[inv])
                        w, cl = weights(run, pop, s, rt.n)
                        firsts.append(first); W.append(w); CL.append(cl)
                    first = np.concatenate(firsts); w = np.concatenate(W); cl = np.concatenate(CL)
                    for k, (desc, _) in enumerate(steps):
                        p, se, K = wstat(first <= k, w, cl)
                        f.write(f'{name}\t{",".join(subs)}\t{run}\t{pop}\t{target}\t{"inf" if budget == 99 else budget}\t{k + 1}\t{desc}\t{p:.4f}\t{se:.4f}\t{K}\n')
        f.flush()
        print('grades', run, pop, flush=True)

# ------------------------------------------------------------------ bounding (Q8 as stated)
def bounding(f, run):
    path = RUNS[run][1]
    rows = collections.defaultdict(list)
    for r in csv.DictReader(open(path), delimiter='\t'):
        t = {x.split(':')[0]: (int(x.split(':')[1]), int(x.split(':')[2])) for x in r['targets'].split(';')}
        rows[r['subset']].append((int(r['idx']), t['opt'], t['p1']))
    for pop in POPS[run]:
        for g, subs in groups_of() + [('all', SUBS)]:
            W, CL, OPT, P1 = [], [], [], []
            for s in subs:
                idx = np.array([x[0] for x in rows[s]])
                w, cl = weights(run, pop, s, len(idx), idx)
                W.append(w); CL.append(cl)
                OPT.append(np.array([x[1] for x in rows[s]])); P1.append(np.array([x[2] for x in rows[s]]))
            w = np.concatenate(W); cl = np.concatenate(CL); o = np.concatenate(OPT); p1 = np.concatenate(P1)
            for q in (1, 2):
                for R in range(0, 8):
                    a = wstat(o[:, q - 1] <= R, w, cl); b = wstat(p1[:, q - 1] <= R, w, cl)
                    f.write(f'{g}\t{run}\t{pop}\t{q}\t{R}\t{a[0]:.4f}\t{a[1]:.4f}\t{b[0]:.4f}\t{b[1]:.4f}\t{a[2]}\n')
        f.flush()
        print('bounding', run, pop, flush=True)

# ------------------------------------------------------------------ Q3
Q3COLS = [
    ('mean_opt', lambda t: t['d']),
    ('mean_htr_normal', lambda t: t['htrN']),
    ('mean_htr_linear_best_side', lambda t: np.minimum(t['htrN'], t['htrI'])),
    ('mean_htr_niss', lambda t: t['htrNiss']),
    ('niss_eq_linear', lambda t: np.minimum(t['htrN'], t['htrI']) == t['htrNiss']),
    ('niss_shorter_by_1', lambda t: np.minimum(t['htrN'], t['htrI']) - t['htrNiss'] == 1),
    ('niss_shorter_by_2plus', lambda t: np.minimum(t['htrN'], t['htrI']) - t['htrNiss'] >= 2),
    ('opt_uses_shortest_niss', lambda t: t['best_any'] == t['htrNiss']),
    ('no_opt_through_shortest_niss', lambda t: t['best_any'] != t['htrNiss']),
    ('opt_htr_plus1', lambda t: t['best_any'] - t['htrNiss'] == 1),
    ('opt_htr_plus2', lambda t: t['best_any'] - t['htrNiss'] == 2),
    ('opt_htr_plus3more', lambda t: t['best_any'] - t['htrNiss'] >= 3),
    ('every_opt_htr_ge9', lambda t: t['best_any'] >= 9),
    ('mean_post_htr_longest_in_an_optimal', lambda t: t['d'] - t['best_any']),
    ('mean_opt_minus_leave_slice', lambda t: t['d'] - t['lsd']),
    ('xr2_one_shorter', lambda t: t['dvar'] < t['d']),
]
def q3(f, run):
    ST = {s: common.load_states(s) for s in SUBS}
    for pop in POPS[run]:
        for g, subs in groups_of() + [('all', SUBS)]:
            W, CL = [], []
            for s in subs:
                w, cl = weights(run, pop, s, len(ST[s]['d'])); W.append(w); CL.append(cl)
            w = np.concatenate(W); cl = np.concatenate(CL)
            for name, fn in Q3COLS:
                x = np.concatenate([fn(ST[s]) for s in subs]).astype(float)
                p, se, K = wstat(x, w, cl)
                f.write(f'{g}\t{run}\t{pop}\t{name}\t{p:.4f}\t{se:.4f}\t{K}\n')
        f.flush()
        print('q3', run, pop, flush=True)

def main():
    parts = sys.argv[1:] or ['checklist', 'grades', 'bounding', 'q3']
    runs = [r for r in ('uniform', 'real') if os.path.exists(RUNS[r][0])]
    if 'checklist' in parts:
        with open(f'{OUTD}/b_checklist.tsv', 'w') as f:
            f.write('group\trun\tpop\tclasses\tclass1\tclass2\tclass3\tafter1\tse1\tafter2\tse2\tafter3\tse3\tp1_after3\tse_p1\tclusters\n')
            uni = None
            for run in runs:
                cc, gr = set_run(run)
                ch = checklist(f, run, cc, uni if run != 'uniform' else None)
                if run == 'uniform': uni = ch
    if 'grades' in parts:
        with open(f'{OUTD}/b_grades.tsv', 'w') as f:
            f.write('checklist\tsubsets\trun\tpop\ttarget\tbudget\tstep\tdescription\tcumulative\tse\tclusters\n')
            for run in runs:
                cc, gr = set_run(run); grades(f, run, gr)
    if 'bounding' in parts:
        with open(f'{OUTD}/b_bounding.tsv', 'w') as f:
            f.write('group\trun\tpop\tq\tR\tfound_opt\tse_opt\tfound_p1\tse_p1\tclusters\n')
            for run in runs:
                if os.path.exists(RUNS[run][1]):
                    set_run(run); bounding(f, run)
    if 'q3' in parts:
        with open(f'{OUTD}/b_q3.tsv', 'w') as f:
            f.write('group\trun\tpop\tmetric\tvalue\tse\tclusters\n')
            for run in runs:
                set_run(run); q3(f, run)

if __name__ == '__main__':
    main()
