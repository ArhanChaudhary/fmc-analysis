"""Names available inside {= ... =} and {{table}} in the v2 write-up sources.  Every number on the page comes through
here, from out/results.json (results.py), out/witness2.json (witness2.py) and out/checks_trace2.tsv (trace2.py)."""
import json, os, sys, csv
HERE = os.path.dirname(os.path.abspath(__file__)); V2 = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(V2, '..', 'src'))
from halfup import hu
R = json.load(open(os.path.join(V2, 'out', 'results.json')))
W = json.load(open(os.path.join(V2, 'out', 'witness2.json')))
LEAN = os.path.exists(os.path.join(V2, 'out', 'lean_ok'))
CK = '' if not LEAN else ' ✓'
def D(name): return R['drm'][name]
def pc(x, d=None):
    if x is None: return '-'
    v = float(x) * 100
    if v == 0: return '0%'
    if d is None: d = 1 if v >= 1 else 2
    s = f'{hu(x, d, 100):.{d}f}%'
    return '100%' if float(x) == 1.0 else s
def pc0(x): return f'{round(100 * x):d}%'
def pts(x): return f'{hu(x, 1, 100):.1f} points'
def p0(x): return f'{hu(x, 0, 100):.0f}%'
def n(x): return f'{int(round(float(x))):,}'
def f2(x): return f'{hu(x, 2):.2f}'
def f3(x): return f'{hu(x, 3):.3f}'
def f1(x): return f'{hu(x, 1):.1f}'
VERD = {'switch': '**switch**', 'time': 'if you have time', 'skip': 'skip'}
def grp(drm, label):
    for g in D(drm)['groups']:
        if g['label'] == label: return g
    raise KeyError(label)
def gshare(drm, label): return pc(grp(drm, label)['share'])
def grate(drm, label): return pc(grp(drm, label)['rate'])
def miss(p): return f"{pc(p['miss_le4'])} / {pc(p['miss_d5'])} / {pc(p['miss_d6'])}"
# ------------------------------------------------------------------ tables
def t_card(drm, tiers=('switch', 'time', 'skip')):
    X = D(drm)
    rows = [f'| What you read ({drm}) | Verdict | Share of {drm} | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |', '|---|---|---|---|---|---|---|']
    for g in X['groups']:
        if g['verdict'] not in tiers: continue
        rows.append(f"| {g['label']} | {VERD[g['verdict']]} | {pc(g['share'])} | {pc(g['rate'])} | {pc(g['le4'] / X['n_le4']) if X['n_le4'] else '-'} | {pc(g['d5'] / X['n_d5']) if X['n_d5'] else '-'} | {pc(g['d6'] / X['n_d6'])} |")
    return '\n'.join(rows)
sys.path.insert(0, V2)
try:
    import cards as _C; SRC = {(f'{c}c{e}e', k): v for ((c, e), k), v in _C.SRC.items()}
except Exception:
    SRC = {}
def _prow(name, who, p):
    return f"| {name} | {who} | {pc(p['switch'])} | {pc(p['miss_le4'])} | {pc(p['miss_d5'])} | {pc(p['miss_d6'])} | {f3(p['loss'])} |"
def t_cmp(drm, keys=None, time=True):
    X = D(drm)
    rows = ['| Policy | From | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |', '|---|---|---|---|---|---|---|']
    for k, b in X['base'].items():
        if keys is None or k in keys: rows.append(_prow(b['name'], b['who'].replace('DRM Subsets Meta', '*DRM Subsets Meta*') + (', ' + SRC[(drm, k)] if (drm, k) in SRC else ''), b))
    rows.append(_prow('**the card**', 'this page', X['card']))
    if time and abs(X['card_time']['switch'] - X['card']['switch']) > 1e-9: rows.append(_prow('the card with its *if you have time* groups', 'this page', X['card_time']))
    return '\n'.join(rows)
def t_main4():
    M = R['main4']['uniform']
    rows = ['| Policy (4c4e, 4c2e, 3c2e and 7c8e together) | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |', '|---|---|---|---|---|---|']
    for key, name in (('pairs', 'pairs only (the *DRM Subsets Meta* table)'), ('best_old', 'the best list on the server for each DRM (Fanti\'s pairs + ARM for 4c4e, caycala\'s chart for 7c8e, 1.5+ pairs for 4c2e, wen\'s rule for 3c2e)'), ('card', '**the cards**'), ('card_time', 'the cards with their *if you have time* groups')):
        p = M[key]; rows.append(f"| {name} | {pc(p['switch'])} | {pc(p['miss_le4'])} | {pc(p['miss_d5'])} | {pc(p['miss_d6'])} | {f3(p['loss'])} |")
    return '\n'.join(rows)
def t_k(drm):
    X = D(drm)
    def v(g, K, key):
        r = g[key] if key else g
        ratio = r['ratio']
        return ('**switch**' if (ratio is None or ratio > 1) else 'skip')
    rows = [f'| What you read ({drm}) | 4-move RZP: DR in 7 or less | Verdict at 4 | 5-move RZP: DR in 6 or less | Verdict at 5 | 6-move RZP: DR in 5 or less | Verdict at 6 |', '|---|---|---|---|---|---|---|']
    for g in X['groups']:
        rows.append(f"| {g['label']} | {pc(g['K7']['rate'])} | {v(g, 7, 'K7')} | {pc(g['rate'])} | {v(g, 6, None)} | {pc(g['K5']['rate'])} | {v(g, 5, 'K5')} |")
    return '\n'.join(rows)
def t_count():
    X = D('4c4e'); rows = ['| Half turns to two bars | Share of 4c4e | Sub-7 rate | Of its 4-or-less | Of its 5-movers | Of its 6-movers |', '|---|---|---|---|---|---|']
    for g in R['twobars']['by_count']:
        rows.append(f"| {g['count']} | {pc(g['share'])} | {pc(g['rate'])} | {pc(g['le4'] / X['n_le4'])} | {pc(g['d5'] / X['n_d5'])} | {pc(g['d6'] / X['n_d6'])} |")
    return '\n'.join(rows)
def t_count_groups():
    rows = ['| What you read (4c4e) | Card says | 2 or fewer: share of the group | 2 or fewer: sub-7 rate | 3: share of the group | 3: sub-7 rate | 4 or 5: share of the group |', '|---|---|---|---|---|---|---|']
    for g in R['twobars']['groups']:
        tot = sum(g[k]['n'] for k in ('le2', 'eq3', 'ge4') if g[k])
        def sh(k): return pc(g[k]['n'] / tot) if g[k] else '0%'
        def rt(k): return pc(g[k]['rate']) if g[k] else '-'
        rows.append(f"| {g['label']} | {VERD[g['verdict']]} | {sh('le2')} | {rt('le2')} | {sh('eq3')} | {rt('eq3')} | {sh('ge4')} |")
    return '\n'.join(rows)
def t_count_pairs():
    rows = ['| Pairs (4c4e) | Cases | With 2 half turns or fewer | With 3 | With 4 or 5 | Sub-7 cases | Of them at 2 or fewer | Of them at 3 |', '|---|---|---|---|---|---|---|---|']
    for g in R['twobars']['by_pairs']:
        rows.append(f"| {g['pairs']} | {n(g['n'])} | {pc(g['le2'] / g['n'])} | {pc(g['eq3'] / g['n'])} | {pc(g['ge4'] / g['n'])} | {n(g['good'])} | {pc(g['good_le2'] / g['good'])} | {pc(g['good_eq3'] / g['good'])} |")
    return '\n'.join(rows)
def t_tried():
    base = R['tried44_pairs']
    rows = ['| Read added to the pair count (4c4e) | Cost per case, best rule on pairs + this read | Switched | Missed: 5-movers | Missed: 6-movers |', '|---|---|---|---|---|',
            f"| (pairs alone) | {f3(base['loss'])} | {pc(base['switch'])} | {pc(base['miss_d5'])} | {pc(base['miss_d6'])} |"]
    for t in sorted(R['tried44'], key=lambda t: t['with_pairs']['loss']):
        p = t['with_pairs']; rows.append(f"| {t['label']} | {f3(p['loss'])} | {pc(p['switch'])} | {pc(p['miss_d5'])} | {pc(p['miss_d6'])} |")
    return '\n'.join(rows)
CEIL = (('pairs', 'pairs'), ('pairs+arm', 'pairs and ARM'), ('pairs+case', 'pairs and corner case'), ('pairs+side', 'pairs and side pairs'), ('pairs+arm+case+side', 'pairs, ARM, corner case and side pairs'),
        ('quick', 'every quick read together'))
def t_ceil(drm):
    X = D(drm); rows = [f'| Reads the rule may use ({drm}) | Cells | Switched | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers | Cost per case |', '|---|---|---|---|---|---|---|']
    for k, name in CEIL:
        if 'case' in k and drm[0] != '4': continue
        p = X['ceil'][k]; rows.append(f"| {name} | {n(p['cells'])} | {pc(p['switch'])} | {pc(p['miss_le4'])} | {pc(p['miss_d5'])} | {pc(p['miss_d6'])} | {f3(p['loss'])} |")
    p = X['card']; rows.append(f"| **the card** | {len(X['groups'])} groups | {pc(p['switch'])} | {pc(p['miss_le4'])} | {pc(p['miss_d5'])} | {pc(p['miss_d6'])} | {f3(p['loss'])} |")
    p = X['exact']; rows.append(f"| the exact DR length | {n(X['n'])} | {pc(p['switch'])} | 0% | 0% | 0% | 0 |")
    return '\n'.join(rows)
def t_sens():
    X = D('4c4e'); rows = ['| A declined 6-mover costs | Each move shorter multiplies by | Pairs only | Pairs + corner case | Pairs + ARM | The card | The card, wider |', '|---|---|---|---|---|---|---|']
    for k, v in X['sens'].items():
        a, b = k.split(',')
        rows.append(f"| {a} wasted switches | {b} | {f3(v['pairs'])} | {f3(v['pairs+case'])} | {f3(v['pairs+arm'])} | {f3(v['card'])} | {f3(v['card_time'])} |")
    return '\n'.join(rows)
def t_real():
    rows = ['| DRM | Real 5-move attempts | Switched: exact | Switched: real attempts | Missed 5-movers: exact | Missed 5-movers: real | Missed 6-movers: exact | Missed 6-movers: real |', '|---|---|---|---|---|---|---|---|']
    for drm in ('4c4e', '4c2e', '3c2e', '7c8e'):
        X = D(drm); a = X['card']; b = X['real']['card']
        rows.append(f"| {drm} | {n(X['real']['attempts'])} | {pc(a['switch'])} | {pc(b['switch'])} | {pc(a['miss_d5'])} | {pc(b['miss_d5'])} | {pc(a['miss_d6'])} | {pc(b['miss_d6'])} |")
    return '\n'.join(rows)
ALL = ('4c4e', '4c2e', '3c2e', '7c8e', '8c8e', '2c2e', '4c6e', '3c4e', '3c6e', '5c4e', '5c6e', '6c6e')
def t_all_card():
    rows = ['| DRM | Sub-7 rate | Card switches | Sub-7 rate of what it switches | Missed: 4 or less | Missed: 5-movers | Missed: 6-movers |', '|---|---|---|---|---|---|---|']
    for drm in ALL:
        X = D(drm); p = X['card']
        rows.append(f"| {drm} | {pc(X['sub7'])} | {pc(p['switch'])} | {pc(p['precision'])} | {pc(p['miss_le4']) if X['n_le4'] else '-'} | {pc(p['miss_d5'])} | {pc(p['miss_d6'])} |")
    return '\n'.join(rows)
def t_all_cost():
    rows = ['| DRM | Pairs policy | Its cost per case | Best list on the server | Its cost per case | The card\'s cost per case |', '|---|---|---|---|---|---|']
    for drm in ALL:
        X = D(drm); b0 = list(X['base'].values())[0]; bo = X['base'][X['best_old']]
        rows.append(f"| {drm} | {b0['name']} | {f3(b0['loss'])} | {bo['name'] if X['best_old'] != list(X['base'])[0] else 'the same'} | {f3(bo['loss'])} | {f3(X['card']['loss'])} |")
    return '\n'.join(rows)
TRACE, SWITCH = 5, 20
def t_time():
    rows = ['| DRM | Card switches | Sub-7 rate of what it switches | Seconds per short DR found (5 s a trace, 20 s a switch) |', '|---|---|---|---|']
    for drm in ALL:
        p = D(drm)['card']; found = p['switch'] * p['precision']
        rows.append(f"| {drm} | {pc(p['switch'])} | {pc(p['precision'])} | {n((TRACE + p['switch'] * SWITCH) / found)} |")
    return '\n'.join(rows)
def t_second():
    rows = ['| DRM | Pairs alone | Pairs + ARM | Pairs + corner case | Pairs + side pairs | Pairs + fake pairs |', '|---|---|---|---|---|---|']
    for drm in ALL:
        c = D(drm)['ceil']
        vals = {k: c[k]['loss'] for k in ('pairs+arm', 'pairs+case', 'pairs+side', 'pairs+fake')}
        best = min(vals, key=vals.get)
        def cell(k): return ('**' + f3(vals[k]) + '**') if k == best and vals[k] < c['pairs']['loss'] - 1e-9 else f3(vals[k])
        rows.append(f"| {drm} | {f3(c['pairs']['loss'])} | {cell('pairs+arm')} | {cell('pairs+case') if drm[0] == '4' else '-'} | {cell('pairs+side')} | {cell('pairs+fake')} |")
    return '\n'.join(rows)
def t_trace():
    agg = {}
    for r in csv.DictReader(open(os.path.join(V2, 'out', 'checks_trace2.tsv')), delimiter='\t'):
        a = agg.setdefault(r['read'], [0, 0]); a[0] += int(r['cubes']); a[1] += int(r['holds'])
    NAME = {'pairs': 'pairs', 'edges_paired': 'edges with a pair (two edges or a bar)', 'fake': 'fake pairs', 'side': 'side pairs', 'carm': 'corner ARM', 'earm': 'edge ARM', 'cc': 'corner case (4 bad corners)',
            'hole_cfg': 'where the two holes are (2 holes)', 'ud_split': 'corners per layer', 'edges_same_layer': 'bad edges in one layer', 'split_pairs': 'split pairs', 'cols_bad': 'corners in columns'}
    rows = ['| Read | Random cubes checked | Read on normal = the inverse\'s value |', '|---|---|---|']
    for k in ('pairs', 'edges_paired', 'fake', 'side', 'carm', 'earm', 'cc', 'cols_bad', 'hole_cfg', 'ud_split', 'edges_same_layer', 'split_pairs'):
        rows.append(f'| {NAME[k]} | {n(agg[k][0])} | {n(agg[k][1])} |')
    return '\n'.join(rows)
def wit(key, comment_setup, comment_dr=None):
    w = W[key]
    return f"```\n{w['setup']}   // setup: {comment_setup}\n{w['dr']}   // {comment_dr or ('DR in ' + str(w['d']))}\n```"
ENV = dict(globals())
# ------------------------------------------------------------------ shortcuts for the text
def B(drm, key): return D(drm)['base'][key]
NX = json.load(open(os.path.join(V2, 'out', 'nextrows.json')))
X44 = D('4c4e'); M4 = R['main4']['uniform']; M4R = R['main4']['real']; TB = R['twobars']; EX = R['extra']; AF = EX['armfree']; ALLU = R['all']['uniform']
def held(drm, label, key):
    g = grp(drm, label); return pc(g[key] / D(drm)['n_' + key])
LOW = ('4c6e', '3c4e', '3c6e', '5c4e', '5c6e', '6c6e')
def lowshare(key):
    """Share of the 12 DRMs' k-movers that sit in the six low DRMs."""
    tot = sum(D(x)['n_' + key] for x in ALL); low = sum(D(x)['n_' + key] for x in LOW)
    return pc(low / tot)
def timeratio(drm, other='4c4e'):
    def sec(x):
        p = D(x)['card']; return (TRACE + p['switch'] * SWITCH) / (p['switch'] * p['precision'])
    return f1(sec(drm) / sec(other))
def frac(pair): return f"{n(pair[0])} of the {n(pair[1])}"
def extra_looks():
    r = EX['reads44']; return f2(r['bar_lt2fake'] + r['one_pair'] + r['one_pair_arm2x'] + r['one_pair_arm21_4b'] + r['stacked_2x'] + r['zero_nofake'])
def bar_rate():
    a = AF['bar_on']; b = AF['bar_off']
    return pc((a['good'] + b['good']) / (a['n'] + b['n']))
def t_budget():
    """The slower reads spent where they pay most: share of cases that get them -> best possible cost."""
    out = ['| Slower reads on | Corner case and side pairs | Those two, the columns, the corner layers and the edges out of the slice |', '|---|---|---|',
           f"| no case (pair trace and ARM only) | {f3(AF['budget_cc_side']['fast_only'])} | {f3(AF['budget_all']['fast_only'])} |"]
    for a, b in zip(AF['budget_cc_side']['steps'], AF['budget_all']['steps']):
        out.append(f"| the best {pc0(a['mark'])} of cases | {f3(a['loss'])} | {f3(b['loss'])} |")
    out.append(f"| every case | {f3(AF['budget_cc_side']['everywhere'])} | {f3(AF['budget_all']['everywhere'])} |")
    return '\n'.join(out)
def t_variants():
    """The 4c4e card and the versions of it with fewer reads."""
    rows = [('the card', X44['card']), ('the card, stacked 4a only at ARM 21', AF['card_arm21_only']), ('the card, bar read with ARM instead of the edges out of the slice', AF['bar_by_arm']),
            ('the card, every 2-pair case switched', AF['no_bar_split']), ('pairs + ARM (Fanti\'s list)', B('4c4e', 'pairs+arm')), ('2+ pairs', B('4c4e', 'pairs'))]
    out = ['| Policy (4c4e) | Switched | Missed 4-or-less | Missed 5-movers | Missed 6-movers | Cost per case |', '|---|---|---|---|---|---|']
    for nm, p_ in rows: out.append(f"| {nm} | {pc(p_['switch'])} | {pc(p_['miss_le4'])} | {pc(p_['miss_d5'])} | {pc(p_['miss_d6'])} | {f3(p_['loss'])} |")
    return '\n'.join(out)
def nmain(): return sum(D(x)['n'] for x in ('4c4e', '4c2e', '3c2e', '7c8e'))
def t_k_short(drm):
    return t_k(drm)
ENV = dict(globals())
LEANTEXT = open(os.path.join(HERE, 'leantext.md')).read().strip() if os.path.exists(os.path.join(HERE, 'leantext.md')) else '**Lean.** (pending)'
ENV = dict(globals())
