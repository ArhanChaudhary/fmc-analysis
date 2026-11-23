"""The example scrambles of the "Advanced DR Bounding Examples" doc, with a DR-move scramble of each.

usage: scrambles.py DOC.txt > data/scrambles.jsonl      (DOC.txt: the doc exported as plain text)

A section heading of the doc is a line that is only a corner case (4b2, 4b3, 0c0, 2c3, 2c4); a scramble is a line of
moves that starts with R' U' F.  Every scramble leaves the cube in DR on U/D, and `drvar` reads a DR state as a
sequence of DR moves, so each scramble gets one: the inverse of a DR finish from nissy (`solve drudfin`)."""
import sys, re, json, subprocess, os

NISSY = '/data/fmc/tools/nissy-2.0.8/nissy'
ENV = dict(os.environ, NISSYDATA='/data/fmc/tools/nissy-data')
MOVE = re.compile(r"[URFDLB](2|')?")

def inv(seq):
    return ' '.join(t[0] + {'': "'", '2': '2', "'": ''}[t[1:]] for t in reversed(seq.split()))

def parse(path):
    section, n = None, {}
    for line in open(path, encoding='utf-8-sig'):
        line = line.strip().replace('’', "'").replace('‘', "'")
        if re.fullmatch(r'[0246][abc][0-5]', line):
            section = line
            continue
        body, _, note = line.partition('//')
        moves = body.split()
        if len(moves) >= 10 and moves[:3] == ["R'", "U'", 'F'] and all(MOVE.fullmatch(t) for t in moves):
            n[section] = n.get(section, 0) + 1
            yield dict(id=f'{section}-{n[section]:02d}', section=section, scramble=' '.join(moves), note=note.strip() or None)

for x in parse(sys.argv[1]):
    out = subprocess.run([NISSY, 'solve', 'drudfin', x['scramble']], capture_output=True, text=True, env=ENV, timeout=600).stdout
    sols = [l.rsplit(' (', 1)[0] for l in out.splitlines() if l.strip().endswith(')') and '(' in l]
    if not sols:
        x['error'] = 'not DR on U/D: ' + out.strip()[-200:]
    else:
        x['dr_scramble'] = inv(sols[0])
    print(json.dumps(x), flush=True)
