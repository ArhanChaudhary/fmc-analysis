#!/usr/bin/env python3
"""report/EXAMPLES.md: 150 uniformly random scrambles with their shortest DRs and their best DRs through short EOs,
then about 50 EO-solved states by case, every answer folded away.  Every move sequence printed is replayed on the
sticker model (sticker.py, built on is-dr-xs-worth-it's cube.py) before the page is written; the page states how many
and fails on any mismatch.

Inputs (made by the commands in the README):
  out/scrambles.txt, out/big/scr50k.tsv            the first 150 scrambles and their rows of `eodrtools scr`
  out/big/ex_inv150.tsv                            `eodrtools scr out/big/ex_inv150.txt 9 6` (the same scrambles inverted)
  out/big/ex_eolist.tsv                            `eodrtools eolist 4 <scrambles 151-450>`
usage: xexamples.py"""
import csv, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sticker, cube
from canon import simplify

OUT = os.path.normpath(os.path.join(HERE, '..', 'out')) + '/'
PAGE = os.path.normpath(os.path.join(HERE, '..', '..', 'report', 'EXAMPLES.md'))
AX = {'RL': 0, 'UD': 1, 'FB': 2}
NAME = {'RL': 'R/L', 'UD': 'U/D', 'FB': 'F/B'}
csv.field_size_limit(10**8)
NSCR = 150

REPLAYED = [0]
MISMATCH = []


def toks(t):
    return [] if t.strip() in ('-', '') else t.split()


def quarter_of(m, y):
    return sticker.FACE_AXIS[m[0]] == y and not m.endswith('2')


def check(ok, what):
    REPLAYED[0] += 1
    if not ok:
        MISMATCH.append(what)


def dr_check(scr, normal, inverse, axis, length, what):
    n, i = toks(normal), toks(inverse)
    s = sticker.replay(scr, ' '.join(n), ' '.join(i))
    check(sticker.is_dr(s, AX[axis]) and len(n) + len(i) == length, what)


def route_check(scr, eo, dr, y, x, total, side, what):
    """EO on axis y (on the given side), then turns without quarter turns of y to DR on x, on the same side."""
    e, d = toks(eo), toks(dr)
    if side == 'normal':
        se, sd = sticker.replay(scr, ' '.join(e)), sticker.replay(scr, ' '.join(e + d))
    else:
        se, sd = sticker.replay(scr, '', ' '.join(e)), sticker.replay(scr, '', ' '.join(e + d))
    check(sticker.is_eo(se, AX[y]) and not any(quarter_of(m, AX[y]) for m in d) and sticker.is_dr(sd, AX[x])
          and len(e) + len(d) == total, what)


def case_of(s, x):
    """xcye of the state for DR on axis x: corners whose x-colour sticker is not on an x face, and the edges out of
    place for DR (slice pieces outside the middle layer of x, and as many others inside it)."""
    X = AX[x]
    bad_c = 0
    for p, ids in sticker._by_pos.items():
        if len(ids) == 3:
            k = [i for i in ids if sticker.col_axis(s, i) == X]
            bad_c += sticker.PLACE_AXIS[k[0]] != X
    out = 0
    for p, ids in sticker.EDGES:
        if p[X] != 0 and all(sticker.col_axis(s, i) != X for i in ids):
            out += 1
    return f'{bad_c}c{2 * out}e'


def code(m):
    return f'`{m}`' if m.strip() and m.strip() != '-' else '(nothing)'


def niss(n, i):
    n, i = n if n != '-' else '', i if i != '-' else ''
    return f"`{(n + ' ' if n else '') + ('(' + i + ')' if i else '')}`".replace(' `', '`')


def parse_route(t):
    if t == '-':
        return None
    head, rest = t.split(':', 1)
    axes, moves = rest.split(':', 1)
    y, x = axes.split('>')
    eo, dr = moves.split('|')
    return int(head), y, x, eo.strip(), dr.strip()


def inv_text(seq):
    return ' '.join(cube.inv_seq(seq.split())) if seq.strip() else ''


# --------------------------------------------------------------------------------------------- part 1
scr_all = [l.strip() for l in open(OUT + 'scrambles.txt') if l.strip()]
rows = {}
for r in csv.DictReader(open(OUT + 'big/scr50k.tsv'), delimiter='\t'):
    if int(r['i']) <= NSCR:
        rows[int(r['i'])] = r
    elif int(r['i']) > NSCR + 5:
        break
inv = {int(r['i']): r for r in csv.DictReader(open(OUT + 'big/ex_inv150.tsv'), delimiter='\t')}
assert len(rows) == NSCR and len(inv) == NSCR
inv_lines = [l.strip() for l in open(OUT + 'big/ex_inv150.txt') if l.strip()]

def neo_sum(r, kinds, L):
    return sum(int(r[f'neo_{k}_{y}_{l}']) for k in kinds for y in AX for l in range(L + 1))

def best_upto(r, kinds, k):
    return min(int(r[f'best_{kd}_{y}_{l}']) for kd in kinds for y in AX for l in range(k + 1))

part1 = []
stats = {'six': [], 'niss': [], 'r4': [], 'r5': []}
for i in range(1, NSCR + 1):
    s0 = scr_all[i - 1]
    r, q = rows[i], inv[i]
    assert inv_lines[i - 1] == inv_text(s0)
    s = simplify(s0)                                   # printed form: adjacent same-face turns merged
    check(sticker.replay(s) == sticker.replay(s0), (i, 'printed scramble'))
    dn = {a: int(r[f'd_n_{a}']) for a in AX}
    di = {a: int(r[f'd_i_{a}']) for a in AX}
    # the inverse run's normal side is this scramble's inverse side
    assert all(int(q[f'd_n_{a}']) == di[a] for a in AX), i
    lin, linv = min(dn.values()), min(di.values())
    six, dniss = min(lin, linv), int(r['dniss'])
    bad = [int(r[f'bad_{a}']) for a in AX]
    s0 = sticker.replay(s)
    for a in AX:
        check(sticker.bad_edges(s0, AX[a]) == int(r[f'bad_{a}']), (i, 'bad edges', a))
    lines = [f'### Scramble {i}', '', f'`{s}`', '',
             f"Bad edges on R/L, U/D, F/B: {bad[0]}, {bad[1]}, {bad[2]}. EOs of at most 4 turns (all three axes): "
             f"{neo_sum(r, 'n', 4)} normal, {neo_sum(r, 'i', 4)} inverse, {neo_sum(r, 'x', 4)} NISS with turns on both sides; "
             f"of at most 5: {neo_sum(r, 'n', 5)}, {neo_sum(r, 'i', 5)}, {neo_sum(r, 'x', 5)}.", '',
             '<details><summary>Shortest DRs and the best DRs through short EOs</summary>', '']
    opt = r['opt_solution']
    dr_check(s, opt, '', r['opt_axis'], lin, (i, 'opt normal'))
    iopt = q['opt_solution']
    dr_check(s, '', iopt, q['opt_axis'], linv, (i, 'opt inverse'))
    dr_check(s, r['niss_normal'], r['niss_inverse'], r['niss_axis'], dniss, (i, 'niss'))
    per_axis = ', '.join(f'{NAME[a]} {dn[a]}' for a in AX)
    per_axis_i = ', '.join(f'{NAME[a]} {di[a]}' for a in AX)
    lines += [f'- Shortest DR on the normal side: {lin} (per axis: {per_axis}), for example {code(opt)} (DR on {NAME[r["opt_axis"]]}).',
              f'- On the inverse: {linv} (per axis: {per_axis_i}), for example `({iopt})` (DR on {NAME[q["opt_axis"]]}).',
              f'- Best of the six: {six}. With NISS: {dniss}, for example {niss(r["niss_normal"], r["niss_inverse"])} (DR on {NAME[r["niss_axis"]]}).']
    for k, col in ((4, 'route4'), (5, 'route5')):
        rn, ri = parse_route(r[col]), parse_route(q[col])
        txt = []
        if rn:
            t, y, x, eo, dr = rn
            route_check(s, eo, dr, y, x, t, 'normal', (i, col, 'normal'))
            assert t == best_upto(r, 'n', k)
            txt.append(f'through a normal EO: {t}, EO `{eo}` on {NAME[y]}, then `{dr}` to DR on {NAME[x]}')
        else:
            txt.append('no normal EO')
        if ri:
            t, y, x, eo, dr = ri
            route_check(s, eo, dr, y, x, t, 'inverse', (i, col, 'inverse'))
            assert t == best_upto(r, 'i', k)
            txt.append(f'through an inverse EO: {t}, `({eo})` on {NAME[y]}, then `({dr})` to DR on {NAME[x]}')
        else:
            txt.append('no inverse EO')
        bx = best_upto(r, 'nix', k)
        txt.append(f'with NISS EOs too: {bx}' if bx < 99 else 'no EO at all')
        lines.append(f'- EOs of at most {k} turns, best DR: ' + '; '.join(txt) + '.')
    lines += ['', '</details>', '']
    part1.append('\n'.join(lines))
    stats['six'].append(six); stats['niss'].append(dniss)

# --------------------------------------------------------------------------------------------- part 2
el = list(csv.DictReader(open(OUT + 'big/ex_eolist.tsv'), delimiter='\t'))
by_eo = {}
for r in el:
    by_eo.setdefault((r['scramble'], r['eo_axis'], r['eo']), []).append(r)
order = ['6c6e', '5c6e', '6c4e', '4c6e', '5c4e', '7c6e', '4c4e', '7c4e', '6c8e', '5c8e', '4c8e', '3c6e', '7c8e', '6c2e', '8c6e', '3c4e', '2c4e', '4c2e', '3c2e', '8c8e']
want = {c: 3 for c in order}
chosen = {c: [] for c in order}
seen_scr = set()
def kind(r, other):
    """What shortens this one: the other axis, the inverse, the switch (or nothing)."""
    p = int(r['plain'])
    return (int(other['plain']) < p, int(r['inverse']) < p, int(r['switched']) < p)
pairs = []
for key, rr in by_eo.items():
    if len(rr) == 2:
        pairs += [(rr[0], rr[1]), (rr[1], rr[0])]
for distinct in (True, False):            # first one of each kind per case, then fill up
    for a, b in pairs:
        c = a['case']
        if c not in chosen or len(chosen[c]) >= want[c] or a['scramble'] in seen_scr:
            continue
        if distinct and any(kind(x[0], x[1]) == kind(a, b) for x in chosen[c]):
            continue
        chosen[c].append((a, b)); seen_scr.add(a['scramble'])
part2 = []
n2 = 0
for c in order:
    if not chosen[c]:
        continue
    part2.append(f'### {c}\n')
    for j, (a, b) in enumerate(chosen[c], 1):
        n2 += 1
        s0, y, eo = a['scramble'], a['eo_axis'], a['eo']
        s = simplify(s0)
        check(sticker.replay(s) == sticker.replay(s0), ('printed scramble', s0))
        x, x2 = a['dr_axis'], b['dr_axis']
        se = sticker.replay(s, eo)
        check(sticker.is_eo(se, AX[y]), ('eo', s, eo))
        check(case_of(se, x) == a['case'] and case_of(se, x2) == b['case'], ('case', s, eo))
        tab = ['| After the EO | Turns to DR | One way |', '|---|---:|---|']
        for r in (a, b):
            X = r['dr_axis']
            route_check(s, eo, r['plain_dr'], y, X, len(toks(eo)) + int(r['plain']), 'normal', ('plain', s, eo, X))
            route_check(s, r['switched_eo'], r['switched_dr'], y, X, len(toks(r['switched_eo'])) + int(r['switched']), 'normal', ('switched', s, eo, X))
            # the inverse: EO on the normal side, DR turns (keeping the EO) on the inverse side
            d = toks(r['inverse_dr'])
            st = sticker.replay(s, eo, r['inverse_dr'])
            check(sticker.is_dr(st, AX[X]) and not any(quarter_of(m, AX[y]) for m in d) and len(d) == int(r['inverse']), ('inverse', s, eo, X))
            dr_check(s, eo + ' ' + r['any_dr'], '', X, len(toks(eo)) + int(r['any']), ('any', s, eo, X))
            tab.append(f"| DR on {NAME[X]} ({r['case']}), EO kept | {r['plain']} | `{r['plain_dr']}` |")
            tab.append(f"| DR on {NAME[X]} on the inverse ({r['inverse_case']} there), EO kept | {r['inverse']} | `({r['inverse_dr']})` |")
            tab.append(f"| DR on {NAME[X]}, last EO turn the other way (`{r['switched_eo']}`) | {r['switched']} | `{r['switched_dr']}` |")
            if int(r['any']) < int(r['plain']):
                tab.append(f"| DR on {NAME[X]}, any turns (breaking the EO) | {r['any']} | `{r['any_dr']}` |")
        part2.append('\n'.join([
            f'**{c}, example {j}.** Scramble `{s}`, EO `{eo}` on {NAME[y]} ({len(toks(eo))} turns). '
            f'After it, the case is {a["case"]} for DR on {NAME[x]} and {b["case"]} for DR on {NAME[x2]}.', '',
            '<details><summary>Turns to DR each way</summary>', '',
            *tab, '', '</details>', '']))

# --------------------------------------------------------------------------------------------- page
import json
A1 = json.load(open(OUT + 'a50k_stats.json'))['a1']
six = np.array(stats['six']); dn_ = np.array(stats['niss'])
head = f"""# Worked examples: EO to DR, and scramble to DR

Examples to play along with the write-up ([WRITEUP.md](WRITEUP.md)). Try a scramble, then open the answers.

**Part 1** is {NSCR} uniformly random scrambles, the first {NSCR} of the study's 50,000 (made by the study itself, not by nissy's `scramble`; see the write-up, appendix B). For each one: the bad edges on each axis, how many EOs of at most 4 and at most 5 turns it has, and, folded away, its shortest DR (normal, inverse, best of six, NISS) and the best DR through an EO of at most 4 and of at most 5 turns. **Part 2** is {n2} EO-solved states by case: a scramble and an EO, then how far DR is on each of the two DR axes, on the inverse, and with the EO's last turn the other way.

How to read it. Turns are face turns (HTM). *Normal* means turns after the scramble, *inverse* turns after the inverse scramble, written in brackets as usual for NISS: `R U (F D)` is `R U` on the normal side and `F D` on the inverse. A *route through an EO* is the EO, then turns that keep it (no quarter turns of the EO's axis) to DR on one of the two other axes, on the same side. "EOs of at most 4 turns" counts every move sequence that solves EO for the first time at its last turn, both directions of the last turn counted, as nissy's `-a` lists them (nissy's default listing shows about half of these). A *NISS EO* has turns on both sides. A case like 4c4e names the bad corners and the edges out of place for that DR axis (slice edges outside the slice, and as many other edges inside it), as in Cale's "DR setup stats" sheet.

Every answer is exact: a shortest DR is the fewest turns there are (from exact distance tables), and a "best DR through an EO" is the best over every EO of that length or shorter. "For example" gives one of the shortest; there are usually several.

**Replay check.** Every move sequence on this page was replayed on the sticker model before the page was written: {{REPLAYED}} checks (each EO is an EO on its axis, each DR is a DR on its axis with the stated number of turns, DR turns after an EO keep it, each case and bad-edge count is read off the stickers), {{MISMATCHES}} mismatches.

In these {NSCR}: best of six {six.mean():.2f} on average, NISS {dn_.mean():.2f} (the 50,000 give {A1['best of 6 (3 axes x normal/inverse, linear)']['mean']:.2f} and {A1['NISS (moves on both sides), best of 3 axes']['mean']:.2f}).

## Part 1. {NSCR} scrambles

"""
page = head + '\n'.join(part1) + f'\n## Part 2. EO to DR, {n2} states by case\n\nEach is a scramble from the study\'s sample and one of its EOs of at most 4 turns. The cases are in order of how often they come up after an EO (most common first). The summary line under each gives the case on each DR axis; the table gives the turns to DR each way, all with the EO kept unless the row says otherwise.\n\n' + '\n'.join(part2)
page = page.replace('{REPLAYED}', f'{REPLAYED[0]:,}').replace('{MISMATCHES}', str(len(MISMATCH)))
open(PAGE, 'w').write(page)
print(f'{PAGE}: {NSCR} scrambles, {n2} EO-solved states; {REPLAYED[0]:,} sticker-model checks, {len(MISMATCH)} mismatches')
if MISMATCH:
    print(MISMATCH[:10]); sys.exit(1)
