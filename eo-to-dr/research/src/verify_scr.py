#!/usr/bin/env python3
"""Replay on the sticker model every solution `eodrtools scr` wrote, and check the bad-edge counts.

For each row: the NISS DR (normal and inverse moves) is a DR on its axis and has `dniss` turns; the optimal DR on the
normal side is a DR with min(d_n_*) turns, and its first `e` turns are an EO on the named axis with no quarter turn
of that axis after them (`estar` = e); each best route through an EO of at most 4, 5, 6 turns is an EO, then turns
without quarter turns of the EO axis, ending in a DR on the named axis, with the stated total; bad_* are the bad
edges of the scramble on each axis.

usage: verify_scr.py <scr.tsv> <scrambles file> [every]     (every: check one row in this many, default 1)"""
import csv, sys
import sticker, cube

AX = {'RL': 0, 'UD': 1, 'FB': 2}
csv.field_size_limit(10**7)

def toks(t):
    return [] if t in ('-', '') else t.split()

def quarter_of(m, y):
    return sticker.FACE_AXIS[m[0]] == y and not m.endswith('2')

def check_row(r, scr):
    d_n = min(int(r[f'd_n_{a}']) for a in AX)
    # NISS DR
    n, i = toks(r['niss_normal']), toks(r['niss_inverse'])
    s = sticker.replay(scr, ' '.join(n), ' '.join(i))
    assert sticker.is_dr(s, AX[r['niss_axis']]), ('niss', r['i'])
    assert len(n) + len(i) == int(r['dniss']), ('niss length', r['i'])
    # optimal DR and the EO it starts with
    opt = toks(r['opt_solution'])
    assert len(opt) == d_n and sticker.is_dr(sticker.replay(scr, ' '.join(opt)), AX[r['opt_axis']]), ('opt', r['i'])
    y, e = r['estar_eo_axis'].split(':')
    y, e = AX[y], int(e)
    assert e == int(r['estar'])
    if e > 0 and not quarter_of(opt[e - 1], y):
        # F2 B written in canonical order: the quarter turn comes after the half turn it commutes with
        assert quarter_of(opt[e], y) and opt[e][0] in {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U', 'F': 'B', 'B': 'F'}[opt[e - 1][0]]
        opt = opt[:e - 1] + [opt[e], opt[e - 1]] + opt[e + 1:]
        assert sticker.is_dr(sticker.replay(scr, ' '.join(opt)), AX[r['opt_axis']])
    assert sticker.is_eo(sticker.replay(scr, ' '.join(opt[:e])), y), ('estar eo', r['i'])
    assert not any(quarter_of(m, y) for m in opt[e:]), ('estar rest', r['i'])
    # routes through an EO of at most 4, 5, 6 turns
    for k, col in ((4, 'route4'), (5, 'route5'), (6, 'route6')):
        if r[col] == '-':
            continue
        head, rest = r[col].split(':', 1)
        axes, moves = rest.split(':', 1)
        ya, xa = axes.split('>')
        eo, dr = moves.split('|')
        eo, dr = toks(eo.strip()), toks(dr.strip())
        assert len(eo) <= k and len(eo) + len(dr) == int(head), (col, r['i'])
        assert sticker.is_eo(sticker.replay(scr, ' '.join(eo)), AX[ya]), (col, 'eo', r['i'])
        assert not any(quarter_of(m, AX[ya]) for m in dr), (col, 'dr breaks eo', r['i'])
        assert sticker.is_dr(sticker.replay(scr, ' '.join(eo + dr)), AX[xa]), (col, 'dr', r['i'])
        bests = [int(r[f'best_n_{a}_{k}']) for a in AX]
        assert int(head) == min(bests), (col, 'not the best', r['i'], head, bests)
    s0 = sticker.replay(scr)
    for a, y in AX.items():
        assert sticker.bad_edges(s0, y) == int(r[f'bad_{a}']), ('bad', a, r['i'])

if __name__ == '__main__':
    rows = csv.DictReader(open(sys.argv[1]), delimiter='\t')
    scr = [l.strip() for l in open(sys.argv[2]) if l.strip() and not l.startswith('#')]
    every = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    n = 0
    for r in rows:
        k = int(r['i'])
        if (k - 1) % every:
            continue
        check_row(r, scr[k - 1])
        n += 1
    print(f'{sys.argv[1]}: {n} rows replayed on the sticker model, all solutions check')
