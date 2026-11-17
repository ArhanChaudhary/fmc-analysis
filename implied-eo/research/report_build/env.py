#!/usr/bin/env python3
"""Numbers, tables and checked example scrambles for the write-up and the full list (assemble.py)."""
import os, sys, json, re, random, zlib
B = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(B, '..')
sys.path.insert(0, R); sys.path.insert(0, '/data/fmc/eo-switch/research/src/report_build')
from eomodel import *
import census as E
S = json.load(open(os.path.join(R, 'out', 'study.json')))
C = json.load(open(os.path.join(R, 'out', 'claims.json')))
BY = json.load(open(os.path.join(R, 'out', 'beyond.json')))
SETS = S['sets']; FREQ = S['freq']; NS = S['n_sample']
RS = json.load(open(os.path.join(R, 'out', 'scrambles.json')))
for _s, _scr in zip(SETS, RS['sets']): _s['scramble'] = _scr

def parse_eo(txt):
    m = re.match(r'^\s*([^()]*?)\s*(?:\(([^()]*)\))?\s*([^()]*?)\s*$', txt)
    normal = (m.group(1) + ' ' + m.group(3)).split(); inverse = (m.group(2) or '').split()
    axes = {AX[s[-1][0]][0] for s in (normal, inverse) if s}
    assert len(axes) == 1, txt
    return axes.pop(), normal, inverse
def key(a, n, i): return E.to_fb(a, E.case_of(i, a), E.case_of(n, a))
def holds(scr, a, n, i): return eo_solved(compose(compose(apply(inv_seq(i)), apply(scr)), apply(n)), a)
def cancel(seq):
    out = []
    for m in seq:
        if out and out[-1][0] == m[0]:
            t = ({'': 1, '2': 2, "'": 3}[out[-1][1:]] + {'': 1, '2': 2, "'": 3}[m[1:]]) % 4
            out.pop()
            if t: out.append(m[0] + {1: '', 2: '2', 3: "'"}[t])
        else: out.append(m)
    return out
KEEP = {ax: [m for m in MOVE_NAMES if AX[m[0]][0] != ax or m.endswith('2')] for ax in range(3)}
def scramble(eos, pick=0):
    """an ordinary random-move scramble (out/scrambles.json) on which every EO of the list holds, checked again here"""
    eos = [e if isinstance(e, tuple) else parse_eo(e) for e in eos]
    k = key(*eos[0]); assert all(key(*e) == k for e in eos), eos
    hit = [st['scramble'] for st in SETS if tuple(st['key']) == k]
    if not hit:
        hit = [v[pick] for t, v in RS['extra'].items() if key(*parse_eo(t)) == k]
    scr = hit[0]
    assert all(holds(scr.split(), *e) for e in eos)
    return scr
def n(x): return f'{x:,}'
def pc(k, d=1): return f'{100 * FREQ[k][0]:.{d}f}%'
def pm(k, d=2): return f'{100 * FREQ[k][0]:.{d}f}% ± {100 * FREQ[k][1]:.{d}f}'

KINDS = [   # (type, the EOs of the example, first seen)
 ('T1', ['F B (F B)', 'R L (R L)', 'U D (U D)'], 'Cale, posted by Jay ([[T3441]])'),
 ('T2', ['F B (F)', 'R L (B R L)', 'U D (B U D)'], 'Jay ([[T3441]])'),
 ('P1', ['R F B', 'L (F B R L)'], 'Jay ([[T3459]]), trig0n ([[T3662]])'),
 ('P2', ['R F B (F)', 'L (B R L)'], 'Jay ([[T3459]])'),
 ('P3', ['R L F B', '(F B R L)'], 'trig0n ([[T3662]])'),
 ('P4', ['F B (F U B)', "R L (R U' L)"], 'Jay ([[T3463]])'),
 ('P5', ['U R F B (F)', 'U L (B R L)'], 'Jay ([[T3450]], [[T3458]])'),
]
CNT = S['counts']
def lens(e): a, nn, i = parse_eo(e); return len(nn) + len(i)
def t_kinds():
    rows = ['| Kind | One EO | The others | Moves | Sets of scrambles | First seen |', '|---|---|---|---|---|---|']
    for k, (t, eos, who) in enumerate(KINDS, 1):
        scramble(eos)
        show = [e.replace('U R F B', 'X R F B').replace('U L (', 'X L (') for e in eos] if t == 'P5' else eos
        rows.append(f"| {k} | {show[0]} | {', '.join(show[1:])} | {', '.join(str(lens(e)) for e in eos)} | {CNT[t]} | {who} |")
    return '\n'.join(rows)
def t_kind_scrambles():
    return '\n'.join(f"{k}. `{scramble(eos)}` has {' and '.join(eos)}." for k, (t, eos, who) in enumerate(KINDS, 1))
def t_freq():
    rows = ['| Kind | Example | Sets | Scrambles with one |', '|---|---|---|---|']
    for k, (t, eos, who) in enumerate(KINDS, 1):
        rows.append(f"| {k} | {eos[0]} | {CNT[t]} | {pm(t)} |")
    rows.append(f"| 1, 4 or 5 | both EOs of 4 moves or less | {CNT['T1'] + CNT['P2'] + CNT['P3']} | {pm('le4')} |")
    rows.append(f"| any | any of the above | {sum(CNT.values())} | {pm('any')} |")
    return '\n'.join(rows)
def t_claims():
    rows = ['| Said | By | Moves | Check |', '|---|---|---|---|']
    for c in C:
        arrow = ' ⟺ ' if c['stated'] == 'same' else ' with '
        assert c['ok']
        verdict = 'same scrambles' if c['same'] else f"not related: `{witness(c['eos'])}` has the first and not the second"
        who = {'Jay (vibing), for Cale': 'Cale, posted by Jay', 'Jay (vibing)': 'Jay'}.get(c['who'], c['who'])
        rows.append(f"| {arrow.join(c['eos'])} | {who}, [[{c['id']}]] | {', '.join(map(str, c['lens']))} | {verdict} |")
    return '\n'.join(rows)
def witness(eos):
    """a random scramble with the first EO and without the second"""
    for scr in RS['extra'][eos[0]]:
        if holds(scr.split(), *parse_eo(eos[0])) and not holds(scr.split(), *parse_eo(eos[1])): return scr
    raise ValueError(eos)
REAL = [  # scrambles posted on the server with the EOs people found on them
 ('D8033', 'Evan', "R' U' F D2 L' B2 L' F B U' F R' U B2 D B2 R2 D' R' L2 D2 R' U' F", ['F B (F B)', 'R L (R L)', 'U D (U D)'], 1),
 ('D19123', 'count quackula', "R' U' F D' U B2 U' F2 R2 F2 R B' F L B2 D' L2 B R' F' U F' R' U' F", ['F B (F B)', 'R L (R L)', 'U D (U D)'], 1),
 ('T3639', 'Cale', "R' U' F U2 R' F2 L U2 F2 L F2 R' F2 R2 U L2 B' F D L' B' R' B' R' U' F", ['B R L', 'F (R L F B)'], 3),
 ('T3584', 'jaye', "R' U' F R2 F2 D2 U F2 D U F D' U' B2 L D B' D U2 L R U2 R' U' F", ['R (D L R)', '(U) L U D'], 4),
 ('D11878', 'tseitsei89', "R' U' F R2 F2 U' R2 F2 L2 U B2 D' R2 F2 L2 F' R2 U L D2 U' R2 B D R' U' F", ['B F R L', '(R L F B)'], 5),
 ('D4423', 'sebastianotronto', "R' U' F R2 D' B2 U B2 D' L2 U2 F2 U' R' U' L R2 F2 D B' U2 R' F' R' U' F", ['(U) F2 L D U', 'F2 R (D R L)'], 7),
]
def t_real():
    out = []
    for mid, who, scr, eos, kind in REAL:
        pe = [parse_eo(e) for e in eos]
        assert all(holds(scr.split(), *e) for e in pe) and all(key(*e) == key(*pe[0]) for e in pe), (mid, [holds(scr.split(), *e) for e in pe])
        out.append(f"- `{scr}` ({who}, [[{mid}]]) has {' and '.join(eos)}: kind {kind}.")
    return '\n'.join(out)
# the order example
assert eo_solved(apply(parse("F U F'")), 0) and not any(eo_solved(apply(parse("L' R' B' F' F U F' F B R L")), ax) for ax in range(3))
assert eo_solved(apply(parse("B' F' L' R' F U F' R L F B")), 2)
SIX = BY['six']; SEVEN = BY['seven']
six_scr = scramble([parse_eo(SIX['X']), parse_eo(SIX['Y'])]); seven_scr = scramble([parse_eo(SEVEN['X']), parse_eo(SEVEN['Y'])])
fb_scr = scramble(['F (B)'])
assert key(*parse_eo(SIX['X'])) == key(*parse_eo(SIX['Y'])) and key(*parse_eo(SEVEN['X'])) == key(*parse_eo(SEVEN['Y']))

# the dictionary F/B side <-> R/L side: every row checked (the R/L case is the F/B case with the 8 edges off the
# E slice toggled), and the rows together are every side with both lengths at most 4 and at most 6 in all
T8 = FULL ^ SLICE[1]
XA = [f + s for f in 'UDRL' for s in ('', '2', "'")]; XB = [f + s for f in 'UDFB' for s in ('', '2', "'")]
DICT = [  # (F/B side, R/L side, moves, note, list of X or None)
 ('(nothing)', 'F B R L', '0 and 4', '', None),
 ('F', 'B R L', '1 and 3', '', None), ('B', 'F R L', '1 and 3', '', None),
 ('X F', 'X B R L', '2 and 4', 'X any U, D, R or L move', XA), ('X B', 'X F R L', '2 and 4', 'X any U, D, R or L move', XA),
 ('F B', 'R L', '2 and 2', '', None),
 ('U F B', 'U R L', '3 and 3', '', None), ('D F B', 'D R L', '3 and 3', '', None),
 ('F U B', "R U' L", '3 and 3', '', None), ("F U' B", 'L U R', '3 and 3', '', None),
 ('F D B', "L D' R", '3 and 3', '', None), ("F D' B", 'R D L', '3 and 3', '', None),
 ('B U F', "L U' R", '3 and 3', '', None), ("B U' F", 'R U L', '3 and 3', '', None),
 ('B D F', "R D' L", '3 and 3', '', None), ("B D' F", 'L D R', '3 and 3', '', None),
 ('R F B', 'L', '3 and 1', '', None), ('L F B', 'R', '3 and 1', '', None),
 ('X R F B', 'X L', '4 and 2', 'X any U, D, F or B move', XB), ('X L F B', 'X R', '4 and 2', 'X any U, D, F or B move', XB),
 ('R L F B', '(nothing)', '4 and 0', '', None),
]
_seen = set()
for fb, rl, mv_, note, xs in DICT:
    for x in (xs or ['']):
        a = [] if fb == '(nothing)' else fb.replace('X', x).split(); b = [] if rl == '(nothing)' else rl.replace('X', x).split()
        wa = E.case_of(a, 2); wb = E.case_of(b, 0)
        assert wa ^ T8 == wb, (fb, rl, x)
        assert (E.DIST[2][wa], E.DIST[0][wb]) == (len(a), len(b)), (fb, rl, x)
        _seen.add(wa)
assert _seen == {w for w in E.DIST[2] if E.DIST[2][w] + E.DIST[0][w ^ T8] <= 6 and max(E.DIST[2][w], E.DIST[0][w ^ T8]) <= 4}
def t_dict():
    rows = ['| A side on F/B | The same side on R/L | Moves | X |', '|---|---|---|---|']
    for fb, rl, mv_, note, xs in DICT: rows.append(f"| {fb} | {rl} | {mv_} | {note.replace('X any', 'any') or 'no X'} |")
    return '\n'.join(rows)

ROWS = [  # kind, rows used, F/B EO, R/L EO
 (1, 'F B twice', 'F B (F B)', 'R L (R L)'), (2, 'F B and F', 'F B (F)', 'R L (B R L)'),
 (3, 'R F B and nothing', 'R F B', 'L (F B R L)'), (4, 'R F B and F', 'R F B (F)', 'L (B R L)'),
 (5, 'R L F B and nothing', 'R L F B', '(F B R L)'), (6, 'F B and F U B', 'F B (F U B)', "R L (R U' L)"),
 (7, 'X R F B and F', 'X R F B (F)', 'X L (B R L)'),
]
def t_kind_rows():
    rows = ['| Kind | Rows used | F/B EO | R/L EO |', '|---|---|---|---|']
    for k, used, fb, rl in ROWS:
        for x in (XB if 'X' in fb else ['']):
            a = parse_eo(fb.replace('X', x)); b = parse_eo(rl.replace('X', x))
            assert a[0] == 2 and b[0] == 0 and key(*a) == key(*b), (fb, rl, x)
        rows.append(f'| {k} | {used} | {fb} | {rl} |')
    return '\n'.join(rows)
assert key(*parse_eo('F B (F R B)')) == key(*parse_eo("U D (D R' U)"))
def full_list():
    names = {'T1': 'Kind 1: F B (F B)', 'T2': 'Kind 2: F B (F)', 'P1': 'Kind 3: R F B', 'P2': 'Kind 4: R F B (F)',
             'P3': 'Kind 5: R L F B', 'P4': 'Kind 6: F B (F U B)', 'P5': 'Kind 7: X R F B (F)'}
    out = []
    for t in ('T1', 'T2', 'P1', 'P2', 'P3', 'P4', 'P5'):
        ss = sorted((s for s in SETS if s['type'] == t), key=lambda s: [x.rsplit(' on ', 1)[0] for x in s['text']])
        out.append(f"## {names[t]}\n\n{len(ss)} {'set' if len(ss) == 1 else 'sets'}.\n")
        out.append('| The EOs of the set | A scramble that has them |'); out.append('|---|---|')
        for s in ss:
            eos = [x.rsplit(' on ', 1)[0] for x in s['text']]
            pe = [parse_eo(e) for e in eos]
            assert [AXIS_NAME[p[0]] for p in pe] == [x.rsplit(' on ', 1)[1] for x in s['text']]
            scr = s['scramble'].split()
            assert all(holds(scr, *p) for p in pe) and len(scr) == 25
            out.append(f"| {' ⟺ '.join(eos)} | `{s['scramble']}` |")
        out.append('')
    return '\n'.join(out)

# --- sub-6 EOs implied by a longer EO (out/longer.json) ---------------------------------------------------------
LG = json.load(open(os.path.join(R, 'out', 'longer.json')))
PT = LG['pointed']; PROBE = LG['probe']
pt_scr = scramble([PT['Y'], PT['X']])
assert len(PROBE) == 230
def pcount(yl, pl): return sum(1 for r in PROBE if r['ylen'] - 2 == yl and r['pattern_len'] == pl)
assert [pcount(*k) for k in ((0, 4), (1, 3), (2, 2), (2, 4), (3, 1), (3, 3), (3, 4), (3, 5))] == [1, 2, 1, 24, 2, 10, 28, 162]
MAINKEYS = {tuple(st['key']): st['type'] for st in SETS}
KN = {'T1': 1, 'T2': 2, 'P1': 3, 'P2': 4, 'P3': 5, 'P4': 6, 'P5': 7}
def t_probe():
    rows = ['| After F B, the other side shows | That case alone takes | The EO on R/L | Its moves | The F/B one has | How many | In section 4 |', '|---|---|---|---|---|---|---|']
    spec = [((3, 1), 'the F case or the B case', 'R L (B R L), R L (F R L)'), ((2, 2), 'the F B case', 'R L (R L)'),
            ((1, 3), 'the R F B case or the L F B case', 'R L (L), R L (R)'), ((3, 3), 'F U B, U F B and the like', "R L (R U' L), R L (U R L), …"),
            ((0, 4), 'the R L F B case: the E slice good, the other eight bad', 'R L'), ((2, 4), 'an X R F B or X L F B case', 'R L (X L), R L (X R)'),
            ((3, 4), 'one of 28 other 4-move cases', 'R L (a 3-move case)'), ((3, 5), 'one of 162 5-move cases', 'R L (a 3-move case)')]
    for (yl, pl), what, eo_ in spec:
        rs = [r for r in PROBE if r['ylen'] - 2 == yl and r['pattern_len'] == pl]
        inm = [r for r in rs if tuple(r['key']) in MAINKEYS]
        kinds = sorted({KN[MAINKEYS[tuple(r['key'])]] for r in inm})
        assert all(tuple(r['key']) in MAINKEYS for r in rs if r['xlen'] <= 5)
        kt = ('kind ' if len(kinds) == 1 else 'kinds ') + ' and '.join(map(str, kinds))
        note = kt if len(inm) == len(rs) else (f'{len(inm)} of them, through U/D ({kt})' if inm else 'no')
        rows.append(f"| {what} | {pl} {'move' if pl == 1 else 'moves'} | {eo_} | {2 + yl} | {2 + pl} | {len(rs)} | {note} |")
    return '\n'.join(rows)
def probe_list():
    rows = ['| Bad edges on the other side after F B | How many | Solving that takes | So the F/B EO has | The EO on R/L | Its moves | In the kinds above | A scramble that has it |', '|---|---|---|---|---|---|---|---|']
    for r in sorted(PROBE, key=lambda r: (r['xlen'] <= 5, r['ylen'], r['pattern_len'], r['nbad'], r['pattern_names'])):
        scr = scramble([r['Y'], r['X']])
        k = MAINKEYS.get(tuple(r['key']))
        where = 'no' if not k else (f'kind {KN[k]}' if r['xlen'] <= 5 else f'kind {KN[k]}, with its U/D EO')
        rows.append(f"| {r['pattern_names']} | {r['nbad']} | {r['pattern_len']} | {r['xlen']} | {r['Y']} | {r['ylen']} | {where} | `{scr}` |")
    return '\n'.join(rows)
SH = LG['shape']; assert SH['rule_holds'] and SH['n'] == 32 and SH['three_move'] == 16
BP = LG['by_probe']
EXS = LG['ex_slice']; EXU = LG['ex_super']; EXF = LG['ex_xf']
exs_scr = scramble([EXS['Y'], EXS['X']]); exu_scr = scramble([EXU['Y'], EXU['X']]); exf_scr = scramble([EXF['Y'], EXF['X']])
LF = LG['freq']
assert PT['good'] == 'UB FR BR BL' and EXS['pattern'] == 'UR DR FL BL'
assert all(BP[k][q] % 2 == 0 for k in BP for q in ('1', '2', '3'))
NPRES = 52848; NCLASS = 52144
assert sum(CNT.values()) == 691 and len(SETS) == 691
THREE = sum(1 for s in SETS if len(s['pres']) == 3)
ENV = dict(globals())
