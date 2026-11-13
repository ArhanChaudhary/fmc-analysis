#!/usr/bin/env python3
"""The generated tables once more, every mean and share left at six decimals: research/out/data6/*.md.

The pages take a difference of two table cells (a gap between two means, a step from one cap to the next) from
these, not from the printed cells, so that it is rounded once.  Same code as the printed tables (xtables.py,
xgreedy_sum.py, xdr.py --table) with only the formatters swapped; xenv.X checks every cell it reads here against the
printed one.  Run after those three and before report_build/assemble.py."""
import sys, os, io, json, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iv
D6 = iv.O + 'data6/'
def build(D6=D6):
    os.makedirs(D6, exist_ok=True)
    six = lambda x: 'nan' if x != x else f'{x:.6f}'
    iv.f2 = six; iv.f1 = six
    iv.fmt = lambda good, n: '' if n == 0 else '0' if good == 0 else f'{100 * good / n:.6f}%'
    iv.num = lambda x, digits=1: '0' if x == 0 else f'{float(x):.6f}%'
    ten = open(iv.O + 'ten_skip.json').read()           # xtables.t_one rewrites this file; put it back as it was
    with contextlib.redirect_stdout(io.StringIO()):
        import xtables, xgreedy_sum, xdr
        xtables.D = D6; xgreedy_sum.D = D6
        xtables.t_cost(); xtables.t_caps(); xtables.t_one(); xtables.t_exchange(); xtables.t_estimates(); xtables.t_thresholds(); xtables.t_tronto()
        xgreedy_sum.main()
        xdr.table(json.load(open(iv.O + 'dr17.json')), D6)
    open(iv.O + 'ten_skip.json', 'w').write(ten)
    return D6
if __name__ == '__main__':
    print(len(os.listdir(build())), 'tables in', D6)
