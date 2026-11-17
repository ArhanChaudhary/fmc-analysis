#!/usr/bin/env python3
"""Every implication stated on the server, checked: two EOs hold on the same scrambles exactly when their two
cases agree (census.to_fb), and each pair is also tried on 300 scrambles built to have the first EO.
-> out/claims.json"""
import os, json, random, re
from eomodel import *
import census as E
HERE = os.path.dirname(os.path.abspath(__file__))
def parse_eo(txt):
    m = re.match(r'^\s*([^()]*?)\s*(?:\(([^()]*)\))?\s*([^()]*?)\s*$', txt)
    normal = (m.group(1) + ' ' + m.group(3)).split(); inverse = (m.group(2) or '').split()
    axes = {AX[s[-1][0]][0] for s in (normal, inverse) if s}
    assert len(axes) == 1 and all(not s[-1].endswith('2') for s in (normal, inverse) if s), txt
    return axes.pop(), normal, inverse
def key(txt):
    a, n, i = parse_eo(txt)
    return E.to_fb(a, E.case_of(i, a), E.case_of(n, a))
def holds(scr, txt):
    a, n, i = parse_eo(txt)
    return eo_solved(compose(compose(apply(inv_seq(i)), apply(scr)), apply(n)), a)
rng = random.Random(3)
KEEP = {ax: [m for m in MOVE_NAMES if AX[m[0]][0] != ax or m.endswith('2')] for ax in range(3)}
def scramble_with(txt):
    a, n, i = parse_eo(txt)
    return i + [rng.choice(KEEP[a]) for _ in range(20)] + inv_seq(n)
CLAIMS = [
 ('T3441', 'Jay (vibing), for Cale', ['F B (F B)', 'R L (R L)', 'U D (U D)']),
 ('T3441', 'Jay (vibing)', ['F B (F)', 'U D (B U D)', 'R L (B R L)']),
 ('T3450', 'Jay (vibing)', ['(D) R B U D', 'R F (U F B)']),
 ('T3458', 'Jay (vibing)', ['F (F R F B)', '(F L) B R L']),
 ('T3459', 'Jay (vibing)', ['F (B2 R F B)', '(B2 L) B R L']),
 ('T3459', 'Jay (vibing)', ['F (R F B)', '(L) B R L']),
 ('T3459', 'Jay (vibing)', ['B U D', 'F (U D F B)']),
 ('T3463', 'Jay (vibing)', ['F B (F R B)', "(D R' U) U D"]),
 ('T3587', 'Jay (vibing)', ['R (D L R)', '(U) L U D']),
 ('T3639', 'Cale', ['F (R L F B)', 'B R L']),
 ('T3662', 'trig0n', ['R F B', 'L (F B L R)']),
 ('T3662', 'trig0n', ['R L F B', '(F B L R)']),
 ('T3661', 'trig0n', ['U D', 'F B (U D F B)', 'R L (U D R L)']),
 ('T3653', 'trig0n', ['F (R U2 F B)', 'B U D (R U D)']),
 ('D4424', 'Jay (vibing)', ['(U) F2 L D U', 'F2 R (D R L)']),
 ('D15042', 'FakeMMAP', ["F B (U F2 U' F B)", 'U D (U F2 D)']),
 ('D13106', 'Jay (vibing)', ['F L F B', 'F R (F B R L)']),
 ('D17329', 'Zagros', ['(R F) U F B', 'D (R B U D)']),
 ('D17328', 'bpaul', ['(R F) B U F', "(R F) L' U' L F B", "(R B R L) L' U' R"]),
 ('D11878', 'tseitsei89', ['B F R L', '(R L F B)']),
 ('D11881', 'Yura Riabov', ['F (R F B)', 'B R L (L)']),
]
NOT = [
 ('T5344', 'Shota', ['F B (F R2 B)', 'U D (U R2 D)']),
 ('T5344', 'Shota', ['F B (F R2 B)', 'R L (R F2 L)']),
 ('T6837', 'Jay (vibing)', ['B (F U2 B)', '(D) D R2 U']),
]
out = []
for kind, lst in (('same', CLAIMS), ('different', NOT)):
    for mid, who, eos in lst:
        same = all(key(e) == key(eos[0]) for e in eos[1:])
        lens = [len(parse_eo(e)[1]) + len(parse_eo(e)[2]) for e in eos]
        # on scrambles that have the first EO: do the others hold?
        tries = [scramble_with(eos[0]) for _ in range(300)]
        assert all(holds(s, eos[0]) for s in tries)
        rate = [sum(holds(s, e) for s in tries) for e in eos[1:]]
        wit = None
        if not same:
            wit = next(' '.join(s) for s in tries if not all(holds(s, e) for e in eos[1:]))
        ok = (same and all(r == 300 for r in rate)) if kind == 'same' else (not same)
        out.append({'id': mid, 'who': who, 'eos': eos, 'lens': lens, 'stated': kind, 'same': same, 'rate': rate, 'witness': wit, 'ok': ok})
        print('OK ' if ok else 'BAD', mid, who, eos, lens, 'same' if same else 'different', rate, wit or '')
json.dump(out, open(os.path.join(HERE, 'out', 'claims.json'), 'w'), indent=1)
