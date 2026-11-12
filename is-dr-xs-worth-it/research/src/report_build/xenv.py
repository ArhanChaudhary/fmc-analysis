#!/usr/bin/env python3
"""Names available inside {= ... =} in the write-up source.  Every number in the text comes through here."""
import sys, json, csv, collections, os
sys.path.insert(0, '/data/fmc/is-dr-xs-worth-it/research/src')
import xv
from xv import pct, avg, fmt, num, share, O
J = json.load(open(O + 'seo_hist.json')); SDIST = json.load(open(O + 'seo_dist.json')); STEPS = json.load(open(O + 'festeps.json'))
KINDS = list(csv.DictReader(open(O + 'kinds.tsv'), delimiter='\t'))
def f2(x): return f'{x:.2f}'
def f1(x): return f'{x:.1f}'
# ---- finishes
def P1(t, **kw): return pct(xv.one_s(**kw), t)
def PD(t, cs=None): return pct(xv.dr(cs), t)
def P8(t, cs=None): return pct(xv.eight(cs), t)
def A1(cs=None, turns=None, col='finish'): return f2(avg(xv.one_s(cs, turns, col)))
def AD(cs=None): return f2(avg(xv.dr(cs)))
def A8(cs=None): return f2(avg(xv.eight(cs)))
def D1(cs=None, turns=None): return f2(avg(xv.one_s(cs, turns)) - avg(xv.dr(cs)))
def D8(cs=None): return f2(avg(xv.eight(cs)) - avg(xv.dr(cs)))
def N1(): return f'{sum(xv.one_s()):,}'
def N8(): return f'{sum(xv.eight()):,}'
def SHARE1(turns): return num(100 * sum(xv.one_s(turns=turns)) / sum(xv.one_s()))
def SETUP_LE(k):
    r = xv._rows('sample1s.tsv'); return num(100 * sum(int(x['setup']) <= k for x in r) / len(r))
def OWN4_SAME():
    r = xv._rows('sample1s.tsv'); return num(100 * sum(x['finish_setup4'] == x['finish'] for x in r) / len(r))
def EIGHT_GAIN(what):
    """DR-2s 8fe: 'share' of states where a setup before the slices beats doing both slices at once, 'avg' moves saved over all states."""
    r = xv._rows('sample8fe.tsv'); g = [int(x['direct']) - int(x['finish']) for x in r]
    return num(100 * sum(v > 0 for v in g) / len(g)) if what == 'share' else f2(sum(g) / len(g))
def A8D(): r = xv._rows('sample8fe.tsv'); return f2(sum(int(x['direct']) for x in r) / len(r))
# ---- kinds and steps
def NK(slices=None, **kw): return str(sum(1 for r in KINDS if (slices is None or int(r['slices']) == slices) and all(r[k] == str(v) for k, v in kw.items())))
def FIX(slices, t): return str(sum(1 for r in KINDS if int(r['slices']) == slices and int(r['turns_to_dr']) == t))
def FIXAVG(slices):
    v = [int(r['turns_to_dr']) for r in KINDS if int(r['slices']) == slices]; return f2(sum(v) / len(v))
def FIXSHARE(slices, ts):
    v = [int(r['turns_to_dr']) for r in KINDS if int(r['slices']) == slices]; return num(100 * sum(t in ts for t in v) / len(v))
def STEP(name, which, t=None):
    h = {int(k): v for k, v in STEPS[name][which].items()}
    if t == 'avg': return f2(sum(k * v for k, v in h.items()) / sum(h.values()))
    if t is not None: return str(h.get(t, 0))
    return f'{list(h)[0]} (all)' if len(h) == 1 else ', '.join(f'{k} ({v} kinds)' for k, v in sorted(h.items()))
# ---- slice EO
def _skip(key):
    txt = open(O + 'seo_skip.txt').read().split(f'number of slice-EO skips, {key}:')[1].split('number of')[0]
    return {int(l.split(':')[0]): int(l.split(':')[1].split('=')[0]) for l in txt.strip().split('\n') if l.strip()[0].isdigit()}
def SKIP(key, k='some'):
    h = _skip(key); tot = sum(h.values())
    if k == 'some': return num(100 * (tot - h[0]) / tot, 1)
    if k == 'avg': return f2(sum(a * b for a, b in h.items()) / tot)
    return num(100 * h.get(k, 0) / tot)
def SKIP4(key): h = _skip(key); return f'{100 * (sum(h.values()) - h[0]) / sum(h.values()):.4f}%'
def SD(name, k): h = SDIST[name]; v = 100 * h.get(str(k), 0) / 7920; return '0' if v == 0 else f'{v:.1f}%'
def _h(key): return {int(k): v for k, v in J[key].items()}
def SH(key, t): h = _h(key); return num(100 * sum(c for d, c in h.items() if d <= t) / sum(h.values()))
def SHR(key): h = _h(key); return num(100 * (1 - h.get(255, 0) / sum(h.values())), 1)
def SHM(key): h = _h(key); r = {d: c for d, c in h.items() if d != 255}; return f2(sum(d * c for d, c in r.items()) / sum(r.values()))
# ---- random scrambles: nearest
def _near(what, sides):
    return {int(r['turns']): int(r['states']) for r in csv.DictReader(open(O + 'nearest.tsv'), delimiter='\t') if r['what'] == what and r['sides'] == sides}
def NEAR(what, t, sides='both'): h = _near(what, sides); return num(100 * sum(c for d, c in h.items() if d <= t) / sum(h.values()))
def NEARAVG(what, sides='both'): h = _near(what, sides); return f2(sum(d * c for d, c in h.items()) / sum(h.values()))
def NEARN(): return f"{sum(_near('dr', 'both').values()):,}"
def FIX70(t): return str(sum(1 for r in KINDS if r['slices'] == '1' and int(r['turns_to_dr']) == t) // 2)
def _split(kind):
    a = xv._rows('sample1s.tsv'); b = xv._rows('sample1s_labels.tsv')
    p = {'4-0': lambda y: '4-0' in (y['split'], y['split_inverse']), '2-2': lambda y: y['split'] == y['split_inverse'] == '2-2', '3-1': lambda y: y['split'] == y['split_inverse'] == '3-1'}[kind]
    return [int(x['finish']) for x, y in zip(a, b) if p(y)]
def SPLIT(kind): v = _split(kind); return f2(sum(v) / len(v))
def SPLITSHARE(kind): return num(100 * len(_split(kind)) / len(xv._rows('sample1s.tsv')))
WIT = json.load(open(O + 'witness.json'))
def SIMON(): return ', '.join(map(str, WIT['simon']))
def W6(): return WIT['six']['scramble']
def W12():
    w = WIT['twelve_bad']
    return (f"`{w['scramble']}` has all twelve edges bad on F/B and green or blue on the U and D face of every corner; it has {w['flipped']} flipped edges, "
            f"needs {w['slices']} slices, and a shortest fix to DR is `{w['fix']}` ({w['turns']} turns).")
REAL = json.load(open(O + 'real.json')) if os.path.exists(O + 'real.json') else {}
def RL(key, sub=None, f='{:.2f}'):
    v = REAL[key] if sub is None else REAL[key][sub]
    return f.format(v) if isinstance(v, (int, float)) else str(v)
def POL(i, what='result'):
    v = REAL['policies'][i][what]; return f'{v:.2f}' if what == 'result' else f'{v:,.0f}'
def POLD(i, j): return f"{round(REAL['policies'][i]['result'], 2) - round(REAL['policies'][j]['result'], 2):.2f}"
def POLN(i, j): return f"{REAL['policies'][i]['n'] - REAL['policies'][j]['n']:,.0f}"
def TH(name, k=0): return REAL['there'][name][k]
def YLD(key): return num(100 * REAL['yield'][key])
def YIN(key): return f"{1 / REAL['yield'][key]:,.0f}"
def YX(a, b): return f"{REAL['yield'][a] / REAL['yield'][b]:.1f}"
def EIGHT3(what):
    r = xv._rows('sample8fe.tsv'); g = [int(x['finish_setup3']) - int(x['finish']) for x in r]
    return num(100 * sum(v == 0 for v in g) / len(g)) if what == 'same' else f2(sum(g) / len(g))
def _eo():
    return list(csv.DictReader(open(O + 'eo_run.tsv'), delimiter='\t'))
def EO(col, f='avg'):
    v = [int(r[col]) for r in _eo()]
    return f'{sum(v) / len(v):,.1f}' if f == 'avg' else num(100 * sum(x > 0 for x in v) / len(v))
def EOP(key, i, what='result'):
    v = REAL[key]['policies'][i][what]; return f'{v:.2f}' if what == 'result' else f'{v:,.0f}'
def EOD(key, i, j): return f"{round(REAL[key]['policies'][i]['result'], 2) - round(REAL[key]['policies'][j]['result'], 2):.2f}"
def EOV(k, f='{:,.0f}'): return f.format(REAL['eo'][k])
def YX2(a, b): return f"{REAL['yield'][a] / REAL['yield'][b]:.2f}"
def _better(k):
    a = xv._rows('sample1s.tsv'); b = xv._rows('sample1s_labels.tsv')
    return [int(x['finish']) for x, y in zip(a, b) if min(int(y['turns_to_dr']), int(y['turns_to_dr_inverse'])) == k]
def BETTER(k, what='avg'):
    v = _better(k); n = len(xv._rows('sample1s.tsv'))
    if what == 'share': return num(100 * len(v) / n)
    if what == 'avg': return f2(sum(v) / len(v))
    if what == 'diff': return f2(sum(v) / len(v) - avg(xv.dr()))
    return num(100 * sum(x <= what for x in v) / len(v))
def OTHER4(what='avg'):
    """DR-1s whose four flipped edges all sit in the slice that does not fix (4 turns: F B R L)."""
    a = xv._rows('sample1s.tsv'); b = xv._rows('sample1s_labels.tsv')
    v = [int(x['finish']) for x, y in zip(a, b) if y['turns_to_dr'] == '4' and y['split_inverse'] == '4-0']
    return f2(sum(v) / len(v)) if what == 'avg' else f2(sum(v) / len(v) - avg(xv.dr()))
def EXCH():
    """The DR-1s against the DR at equal odds: for finishes of 13 to 16, how many moves earlier a DR has the same chance (odds interpolated on a log scale)."""
    import math
    d, h = xv.dr(), xv.one_s(); out = []
    cd = lambda t: sum(d[:t + 1]) / sum(d)
    for t in (13, 14, 15, 16):
        p = sum(h[:t + 1]) / sum(h)
        x = next(u for u in range(1, 19) if cd(u) >= p)
        frac = (math.log(p) - math.log(cd(x - 1))) / (math.log(cd(x)) - math.log(cd(x - 1)))
        out.append(t - (x - 1 + frac))
    return f1(sum(out) / len(out))
def SE1(): return f'{xv.se(xv.one_s()):.3f}'
def SE8(): return f'{xv.se(xv.eight()):.2f}'
def A8C(): r = xv._rows('sample8fe.tsv'); return f2(sum(int(x['finish_setup3']) for x in r) / len(r))
def REAL_HEADLINE(): return open(os.path.dirname(os.path.abspath(__file__)) + '/real_headline.md').read().strip() if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + '/real_headline.md') else '(pending)'
def REAL_VERDICT(): return open(os.path.dirname(os.path.abspath(__file__)) + '/real_verdict.md').read().strip() if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + '/real_verdict.md') else '(pending)'
EO8 = json.load(open(O + 'eo8_hist.json'))
def E8AVG(): h = EO8['8fe']; return f2(sum(d * c for d, c in enumerate(h)) / sum(h))
def E8CHK(): a, b = EO8['renaming_full_eo'], EO8['renaming_any_moves']; assert a[0] == a[1] and b[0] == b[1]; return f'{a[1] + b[1]:,}'
def E8START(start=None, maxlen=9):
    """8fe candidates on the 500 scrambles by where they start: '0' slice-EO skip, '1' one-move slice EO, '4' EO of 4 or less."""
    return f"{sum(1 for r in xv._rows('attempts_8fe.tsv') if int(r['length']) <= maxlen and (start is None or r['start'] == start)):,}"
ENV = {k: v for k, v in globals().items() if not k.startswith('_')}
