#!/usr/bin/env python3
"""Build cards/decision-cards.md from cards/src/cards.md.

In the template:
  {= study: expression =}   a number of a study, evaluated in that study's own report environment
                            (STUDY/research/src/report_build/xenv.py, the names its write-up uses), so a card prints
                            exactly what the study prints
  {= expression =}          a number of this page, evaluated here (names below: the cards' own data in cards/data)
  {{name}}                  a table made here (TABLES below)
  {{sec study N}}           a link to section N of a study's write-up, by its heading
  [[T123]]                  a dated link to a Discord message (as in the studies)
Routes print in the site's notation (htr-routes/research/src/report_build/routefmt.py).

usage: build.py   (needs the studies' result files and the knowledge base, like the studies' own assemble.py)"""
import csv, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = '/data/fmc'
sys.path.insert(0, f'{ROOT}/judging-a-dr/research/src')
from pv import hu                                           # every printed number: an exact half goes up
sys.path.insert(0, f'{ROOT}/htr-routes/research/src/report_build')
import routefmt
sys.path.insert(0, f'{ROOT}/eo-switch/research/src/report_build')
import links

DATA = os.path.join(HERE, '..', 'data')
def tsv(path): return list(csv.DictReader(open(path), delimiter='\t'))
def pc(x, d=1): return f'{hu(float(x) * 100, d):.{d}f}%'
def f2(x): return f'{hu(float(x), 2):.2f}'
def n(x): return f'{int(x):,}'

STOP = tsv(f'{DATA}/eo_stop.tsv')
MID = tsv(f'{DATA}/niss_mid.tsv')
BUD = tsv(f'{ROOT}/htr-routes/research/out/q2_checklist_budget.tsv')
CASES = tsv(f'{ROOT}/eo-to-dr/research/out/c6_by_case.tsv')
SUBSETS = ['0c0', '4a1', '4a2', '4b2', '0c3', '2c3', '4c3', '0c4', '2c4', '4c4', '2c5', '4b5']   # htr-routes' order of corner subsets

def STOPV(scope, group, col):
    for r in STOP:
        if r['scope'] == scope and r['best_le4'] == group: return r[col]
    raise KeyError((scope, group))
def BUDV(sub, budget, step, col='cumulative'):
    for r in BUD:
        if r['group'] == sub and r['level'] == 'C' and r['target'] == 'opt' and r['budget'] == budget and r['step'] == str(step): return r[col]
    raise KeyError((sub, budget, step))
def ALONE(sub, budget, cls):
    """the share of the subset's DRs where this one route finds the optimal at that HTR budget (any step of the checklist)"""
    for r in BUD:
        if r['group'] == sub and r['level'] == 'C' and r['target'] == 'opt' and r['budget'] == budget and r['class'] == cls: return r['alone']
    raise KeyError((sub, budget, cls))
def route(cls): return routefmt.route(cls.split(' | ')[0])

# ------------------------------------------------------------------ tables made here
def t_stop(scope):
    rows = ['| Best DR through your EOs of 4 or less | Share of scrambles | 5-move EOs give a shorter DR | Average shortening from the 5-movers, moves | Then 6-move EOs give a shorter DR still |',
            '|---|---:|---:|---:|---:|']
    for g, label in [('8 or less', '8 or less'), ('9', '9'), ('10', '10'), ('11', '11'), ('12 or more', '12 or more'), ('no EO of 4 or less', 'no EO of 4 or less')]:
        gain = STOPV(scope, g, 'five_gain')
        rows.append(f'| {label} | {pc(STOPV(scope, g, "share"))} | {pc(STOPV(scope, g, "five_better"))} | '
                    f'{"–" if gain == "nan" else f2(gain)} | {pc(STOPV(scope, g, "six_better"))} |')
    return '\n'.join(rows)

Q1 = {(r['group'], r['class']): r for r in tsv(f'{ROOT}/htr-routes/research/out/q1_routes.tsv') if r['level'] == 'C' and ' ' not in r['group']}
def t_variants():
    rows = ['| Subset | First route | Shortest HTRs only | Up to 1 longer | Up to 2 longer | Any HTR length | Three routes, shortest HTRs only | Two routes, up to 2 longer |',
            '|---|---|---:|---:|---:|---:|---:|---:|']
    for s in SUBSETS:
        first = BUDV(s, '2', 1, 'class')
        rows.append(f'| {s} | `{route(first)}` | {pc(ALONE(s, "0", first))} | {pc(ALONE(s, "1", first))} | {pc(ALONE(s, "2", first))} | '
                    f'{pc(Q1[(s, first)]["share_opt"])} | {pc(BUDV(s, "0", 3))} | {pc(BUDV(s, "2", 2))} |')
    for s in SUBSETS:   # the card's rule: one route to 2 longer beats three routes at shortest HTRs, on every subset
        assert float(ALONE(s, '2', BUDV(s, '2', 1, 'class'))) > float(BUDV(s, '0', 3)), s
    return '\n'.join(rows)

def t_mid():
    rows = ['| Subset | Where you are, on normal | Quarter turns so far | Keep going on normal finds the optimal | Switch now finds the optimal | Either | Better |',
            '|---|---|---:|---:|---:|---:|---|']
    for s in SUBSETS:
        for r in [r for r in MID if r['subset'] == s]:
            a, b = float(r['continue_linear']), float(r['switch_now'])
            better = 'switch' if b - a >= 0.05 else 'keep going' if a - b >= 0.05 else 'about even'
            rows.append(f'| {s} | `{routefmt.route(r["so_far"])}` | {r["qt_done"]} | {pc(a)} | {pc(b)} | {pc(r["either"])} | {better} |')
    return '\n'.join(rows)

CASE_ROWS = ['3c2e', '2c2e', '4c2e', '4c4e', '7c8e', '8c8e', '3c4e', '5c4e', '4c6e', '5c6e', '6c6e', '6c4e', '7c6e', '7c4e', '6c8e', '3c6e']
def t_cases():
    rows = ['| DRM on the DR axis you look at | Share of all EO-solved states | DR in 5 or fewer more moves, every option (share of the row) | DR in 6 or fewer more, every option (share of the row) | DR in 7 or fewer more, every option (share of the row) | DR in 6 or fewer more, that one DR axis, normal only (share of the row) |',
            '|---|---:|---:|---:|---:|---:|']
    for c in CASE_ROWS:
        rows.append(f"| {c} | {{= eo-to-dr: C6('{c}', 'share') =}} | {{= eo-to-dr: C6('{c}', 'all_eo_kept_p_le5') =}} | "
                    f"{{= eo-to-dr: C6('{c}', 'all_eo_kept_p_le6') =}} | {{= eo-to-dr: C6('{c}', 'all_eo_kept_p_le7') =}} | "
                    f"{{= eo-to-dr: C6('{c}', 'plain_p_le6') =}} |")
    return '\n'.join(rows)

def t_mid_rule():
    """the bold rule of the NISS card, from the table: per subset the best point to switch (ahead by 5 points or more),
    or keep going / even"""
    sw, keep, even = [], [], []
    for s in SUBSETS:
        rs = [r for r in MID if r['subset'] == s]
        good = [r for r in rs if float(r['switch_now']) - float(r['continue_linear']) >= 0.05]
        if good:
            best = max(good, key=lambda r: float(r['either']))
            sw.append((s, best['so_far'].split(' > ')[-1], int(best['qt_done'])))
        elif all(float(r['continue_linear']) - float(r['switch_now']) >= 0.05 for r in rs):
            keep.append(s)
        else:
            even.append(s)
    at = {}
    for s, where, q in sw: at.setdefault(where, []).append(s)
    lines = ['- **Switch** ' + '; '.join(f"on {', '.join(v)} at {k}" for k, v in at.items()) + '.']
    if keep: lines.append(f"- **Keep going on normal** on {', '.join(keep)}.")
    if even: lines.append(f"- **About even** on {', '.join(even)}: both work about as often, so check both.")
    return '\n'.join(lines)

def include(path): return open(f'{ROOT}/{path}').read().strip('\n')

SW44 = {r['key']: r for r in tsv(f'{DATA}/switch44.tsv')}
SWR = {r['key']: r for r in tsv(f'{DATA}/switch44_rules.tsv')}
def S44(key, col): return SW44[key][col]
def SR(key, col): return SWR[key][col]

def t_sw44_groups():
    rows = ['| What you NISS trace on the switched case | Share of all non-JZP 4c4e cases | DR in 6 or less after the switch (share of the row) | DR in 5 or less after the switch (share of the row) | Share of all non-JZP 4c4e cases with a DR in 5 or less |',
            '|---|---:|---:|---:|---:|']
    for k in ('p2_le2', 'p2_3', 'p2_45', 'p1_arm21', 'p1_other', 'p0'):
        r = SW44[k]
        rows.append(f"| {r['group']} | {pc(r['share_of_nonjzp'])} | {pc(r['p_le6'])} | {pc(r['p_le5'])} | {pc(r['of_nonjzp_le5'])} |")
    return '\n'.join(rows)

def t_sw44_rules():
    rows = ['| Switch when | Share of all non-JZP 4c4e cases switched | DR in 6 or less, among the switched | Share of all non-JZP 4c4e cases with a DR in 6 or less that get switched | Share of all non-JZP 4c4e cases with a DR in 5 or less that get switched |',
            '|---|---:|---:|---:|---:|']
    for k in ('current', 'first', 'first_arm21'):
        r = SWR[k]
        rows.append(f"| {r['rule']} | {pc(r['share_switched'])} | {pc(r['p_le6'])} | {pc(r['caught_le6'])} | {pc(r['caught_le5'])} |")
    return '\n'.join(rows)

def t_eoswitch_cards():
    t = include('eo-switch/report/data/rule_cards.md')
    old = '| DRM | Verdict | What the switched case shows | Share of the DRM | Sub-7 rate |'
    assert t.startswith(old)
    return t.replace(old, '| DRM | Verdict | What you NISS trace on the switched case | Share of all cases of this DRM | DR in 6 or less after the switch (share of the row) |', 1)

TABLES = {'eoswitch_cards': t_eoswitch_cards, 'sw44_groups': t_sw44_groups, 'sw44_rules': t_sw44_rules, 'stop_all': lambda: t_stop('normal, inverse and NISS'), 'stop_normal': lambda: t_stop('normal'),
          'variants': t_variants, 'mid': t_mid, 'mid_rule': t_mid_rule, 'cases': t_cases}

# ------------------------------------------------------------------ section links
TITLES = {}
def anchor(head):
    """GitHub's (and pandoc gfm's) heading id"""
    h = head.strip().lower()
    h = re.sub(r'[^\w\- ]', '', h)
    return h.replace(' ', '-')
def sec(study, num):
    w = open(f'{ROOT}/{study}/report/WRITEUP.md').read()
    if study not in TITLES:
        TITLES[study] = re.search(r'^# (.+)$', w, re.M).group(1)
    m = re.search(rf'^#+ ({re.escape(num)}\.? .+)$', w, re.M)
    assert m, (study, num)
    return f'[section {num}]({study}/#{anchor(m.group(1))})'

# ------------------------------------------------------------------ evaluation
def study_eval(study, exprs):
    code = ("import sys, json; sys.path.insert(0, '.'); sys.path.insert(0, '..'); import xenv\n"
            "ex = json.loads(sys.stdin.read()); print(json.dumps([str(eval(e, xenv.ENV)) for e in ex]))")
    p = subprocess.run([sys.executable, '-c', code], cwd=f'{ROOT}/{study}/research/src/report_build', input=json.dumps(exprs),
                       capture_output=True, text=True)
    if p.returncode: sys.exit(f'{study}: {p.stderr[-2000:]}')
    return json.loads(p.stdout.strip().split('\n')[-1])

def main():
    doc = open(os.path.join(HERE, 'cards.md')).read()
    doc = re.sub(r'\{\{([a-z_0-9]+)\}\}', lambda m: TABLES[m.group(1)](), doc)
    doc = re.sub(r'\{\{sec ([a-z\-]+) ([\d.]+)\}\}', lambda m: sec(m.group(1), m.group(2)), doc)
    pat = re.compile(r'\{=\s*(?:([a-z][a-z\-]+):\s*)?(.+?)\s*=\}')
    want = {}
    for m in pat.finditer(doc):
        if m.group(1): want.setdefault(m.group(1), []).append(m.group(2))
    got = {s: dict(zip(ex, study_eval(s, ex))) for s, ex in want.items()}
    env = dict(globals())
    def one(m):
        if m.group(1): return got[m.group(1)][m.group(2)]
        v = eval(m.group(2), env)
        return v if isinstance(v, str) else str(v)
    doc = pat.sub(one, doc)
    assert '{=' not in doc and '{{' not in doc
    doc = links.expand(doc)
    doc = routefmt.page(doc)
    out = os.path.join(HERE, '..', 'decision-cards.md')
    open(out, 'w').write(doc)
    print('wrote', os.path.normpath(out), len(doc.split('\n')), 'lines')

if __name__ == '__main__':
    main()
