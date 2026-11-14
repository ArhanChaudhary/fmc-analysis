#!/usr/bin/env python3
"""Writes the policy files of every experiment (research/policies/*.toml).

Each file starts with the baseline [policy.base] and adds the variants of one experiment as [policy.NAME] sections
with `base = "base"` (or `base = "ref"`, a tuned reference given with --best).  The parameters are those of
attemptsim/src/conf.rs `Policy`; times are seconds on the clock of a one-hour attempt (they scale with the budget).
usage: make_policies.py [--best KEY=VALUE ...]   (the --best overrides define [policy.ref]; files get the prefix t_)"""
import os, sys
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
BASE = dict(eo_len=5, eo_niss='true', eo_cap=40, t_eo=480, rzp_per_eo=3, rzp_short=4, rzp_per_eo_long=1, read_max=11.5,
            rzp_depth=3, switch_pen=0.3, dr_cap=11, t_dr=2100, htr_per_dr=4, fin_min_p=0.03, reserve=300)

def sec(name, kv, base=None):
    lines = [f'[policy.{name}]']
    if base: lines.append(f'base = "{base}"')
    lines += [f'{k} = {v}' for k, v in kv.items()]
    return '\n'.join(lines) + '\n'

ALL = []

def write(fname, variants, ref=None, header=''):
    """variants: list of (name, dict).  ref: dict of overrides defining [policy.ref] (the tuned reference).
    Every variant also goes into all.toml as EXP_NAME (EXP = e1 ... e5), so that one run covers every experiment."""
    ALL.extend((fname.split('_')[0] if not fname.startswith('t_') else 't' + fname.split('_')[1], n, kv) for n, kv in variants)
    out = [f'# {header}\n' if header else '', sec('base', BASE)]
    b = 'base'
    if ref:
        out.append(sec('ref', ref, 'base')); b = 'ref'
    names = set()
    for name, kv in variants:
        assert name not in names and name not in ('base', 'ref'), name
        names.add(name)
        out.append(sec(name, kv, b))
    with open(f'{R}/policies/{fname}.toml', 'w') as f: f.write('\n'.join(out))
    return len(variants) + 1 + (1 if ref else 0)

def tag(x): return str(x).replace('.', 'p')

def main():
    ref = {}
    if '--best' in sys.argv:
        for a in sys.argv[sys.argv.index('--best') + 1:]:
            k, v = a.split('='); ref[k] = v
    pre = 't_' if ref else ''
    r = ref or None
    n = 0
    # E1: minute the EO writing stops x minute the DR search stops (finishing gets the rest)
    v = [(f'teo{te}_tdr{td}', dict(t_eo=te, eo_cap=999, t_dr=td)) for te in (180, 300, 480, 720, 960)
         for td in (900, 1200, 1500, 1800, 2100, 2400, 2700, 3000) if td > te]
    n += write(pre + 'e1_split', v, r, 'E1: time per phase. t_eo = stop writing EOs, t_dr = stop looking for DRs.')
    # E2: breadth first against depth first and mixtures, early backups
    v = [(f'eagereo{k}', dict(eager_eo=k)) for k in (2, 3, 4, 5)]
    v += [(f'eagerfin{tag(th)}_r{rt}', dict(eager_finish=th, eager_routes=rt)) for th in (20.5, 21.5, 22.5, 23.5, 99) for rt in (1, 2, 99)]
    v += [('dfs', dict(eager_eo=9, eager_finish=99, eager_routes=99)),
          ('dfs_r1', dict(eager_eo=9, eager_finish=99, eager_routes=1)),
          ('dfs_eo3', dict(eager_eo=3, eager_finish=99, eager_routes=99)),
          ('dfs_eo3_fin22p5', dict(eager_eo=3, eager_finish=22.5, eager_routes=99))]
    v += [(f'backup{bt}', dict(backup_time=bt)) for bt in (600, 900, 1200, 1500, 1800, 2100, 2400)]
    n += write(pre + 'e2_order', v, r, 'E2: breadth first, depth first, early backups.')
    # E3: budgets that react to what the attempt shows
    v = [(f'rich{rn}_tdr{td}', dict(rich_n=rn, t_dr_rich=td)) for rn in (15, 25, 35, 50) for td in (1500, 1800, 2400, 2700)]
    v += [(f'poor{pn}', dict(eo_len=4, eo_len_poor=5, poor_n=pn)) for pn in (6, 10, 15, 25, 40)] + [('eo4only', dict(eo_len=4))]
    v += [(f'late{ll}_tdr{td}', dict(late_len=ll, t_dr_late=td)) for ll in (8, 9, 10) for td in (2400, 2700, 3000)]
    v += [(f'enough{k}_len{ll}', dict(dr_enough=k, dr_enough_len=ll)) for k in (1, 2, 3, 5) for ll in (8, 9, 10)]
    v += [(f'bk{bl}_tdr{td}', dict(backup_len=bl, t_dr_backup=td, bank_at=bl)) for bl in (21, 22, 23) for td in (2700, 3000, 3150)]
    v += [(f'early{td}_late{ll}_{tl}', dict(t_dr=td, late_len=ll, t_dr_late=tl)) for td in (1500, 1800) for ll in (9, 10) for tl in (2400, 2700)]
    n += write(pre + 'e3_adaptive', v, r, 'E3: budgets that depend on what the attempt shows.')
    # E4: safety
    v = [(f'reserve{rs}', dict(reserve=rs)) for rs in (150, 180, 210, 240, 270, 360, 420, 600)]
    v += [(f'stop{k}', dict(stop_at=k)) for k in (20, 21, 22, 23)]
    v += [(f'bankfirst_rr{rr}', dict(bank_first='true', reserve_rewrite=rr)) for rr in (150, 180, 240, 300)]
    v += [(f'bankat{k}_rr{rr}', dict(bank_at=k, reserve_rewrite=rr)) for k in (21, 22, 23, 24) for rr in (180, 300)]
    v += [('bankalways', dict(bank_always='true', reserve_rewrite=180))]
    v += [(f'quick{tag(th)}_r{rt}', dict(eager_finish=th, eager_routes=rt, bank_at=22, reserve_rewrite=180)) for th in (21.5, 22.5, 23.5) for rt in (1, 2)]
    v += [(f'safe_bk{bt}_q22p5', dict(backup_time=bt, bank_at=22, eager_finish=22.5, eager_routes=1, reserve_rewrite=180)) for bt in (900, 1200, 1500, 1800)]
    v += [(f'commit{td}', dict(t_dr=td, bank_at=22, reserve_rewrite=180)) for td in (1200, 1500, 1800)]
    n += write(pre + 'e4_safety', v, r, 'E4: safety. Written backups, the reserve for writing, quick checks of good DRs, committing early.')
    # E5: one decision at a time
    v = []
    def sweep(key, vals, extra=None):
        for x in vals:
            kv = {key: x}; kv.update(extra or {})
            v.append((f'{key}_{tag(x)}', kv))
    sweep('eo_cap', (10, 20, 30, 60, 80, 120), dict(t_eo=9999))
    sweep('eo_len', (3, 4))
    sweep('rzp_per_eo', (0, 1, 2, 4, 6, 8))
    sweep('rzp_per_eo_long', (0, 2, 3))
    sweep('read_max', (8, 8.5, 9, 9.5, 10, 10.5, 11, 12, 13))
    sweep('rzp_depth', (1, 2))
    sweep('rzp_more', (0, 1, 4))
    sweep('dr_per_line', (2, 3))
    sweep('switch_pen', (0, 0.6, 1, 2, 99))
    sweep('dr_cap', (10, 12))
    sweep('t_dr', (900, 1200, 1500, 1800, 2400, 2700, 3000))
    sweep('htr_per_dr', (1, 2, 3, 6, 8))
    sweep('fin_min_p', (0, 0.01, 0.06, 0.1, 0.2))
    sweep('fin_max', (1, 2, 3, 4, 5, 6))
    sweep('reserve', (180, 240, 360))
    v.append(('read_on_find_false', dict(read_on_find='false')))
    v.append(('eo_niss_false', dict(eo_niss='false')))
    n += write(pre + 'e5_curves', v, r, 'E5: one budgeting decision at a time.')
    out = ['# Every experiment in one file: base, then each variant as EXP_NAME.\n', sec('base', BASE)]
    b = 'base'
    if r:
        out.append(sec('ref', r, 'base')); b = 'ref'
    out += [sec(f'{e}_{nm}', kv, b) for e, nm, kv in ALL]
    with open(f'{R}/policies/{pre}all.toml', 'w') as f: f.write('\n'.join(out))
    print('policies written:', n, '; all.toml:', len(ALL) + 1)

if __name__ == '__main__':
    main()
