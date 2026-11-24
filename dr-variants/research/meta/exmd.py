"""Markdown blocks for the worked examples (every printed solution is replayed on the sticker model in exview)."""
from exview import *
INVMOVE = lambda s: ' '.join((m[:-1] if m.endswith("'") else (m if m.endswith('2') else m + "'")) for m in reversed(s.split()))
def block(scr, depth=3):
    r = view(scr, quiet=True); t = r['t']; g = r['goal']
    hum = t[(t.extra <= depth) & (t.e2 <= 1)]
    hb = hum[hum.rlive & hum.plive].sort_values(['pairs_htr', 'len'], ascending=[False, True]).reset_index(drop=True)
    # the baseline: pair floor, shortest HTR first, most pairs among equals; then the same order with both floors
    base = hum[hum.plive].sort_values(['len', 'pairs_htr'], ascending=[True, False]).reset_index(drop=True)
    same = hum[hum.rlive & hum.plive].sort_values(['len', 'pairs_htr'], ascending=[True, False]).reset_index(drop=True)
    fb = (base.index[base.ok][0] + 1) if base.ok.any() else None
    fs = (same.index[same.ok][0] + 1) if same.ok.any() else None
    ff = (hb.index[hb.ok][0] + 1) if hb.ok.any() else None
    w = t[t.ok].sort_values(['extra', 'len'])
    def sol(x):
        seq = (x.path + ' | ' + x.finish).strip()
        where = 'normal' if x.side == 'N' else 'inverse'
        tail = f" (as a normal solution: `{INVMOVE((x.path + ' ' + x.finish).strip())}`)" if x.side == 'I' else ''
        return f"on {where}, `{seq}` ({x.total}): {x.q}qt {x.kind} skeleton of {x.L}, S+T = {x.extra} ({x.e2} before 2qt), {x.bad} bad slice{'' if x.bad == 1 else 's'}, rule +{x.rule_N}, {x.pairs_htr} pairs at HTR; at 2qt {x.pairs_2qt} pair{'' if x.pairs_2qt == 1 else 's'} and {x.htrpairs_2qt} HTR-equivalent pairs, {x.htrpairs_2qt_inv} on the inverse{tail}"
    return dict(r=r, hum=hum, hb=hb, fb=fb, fs=fs, ff=ff, nbase=len(base), w=w, sol=sol, info=r['info'], gen=len(hum), rl=int(hum.rlive.sum()), both=len(hb), within=int(hum.ok.sum()),
                all=len(t), all_rule=r['n_rule'], all_both=r['n_both'], all_within=r['n_within'], first_base_all=r['first_base'], niss=r['niss'])
