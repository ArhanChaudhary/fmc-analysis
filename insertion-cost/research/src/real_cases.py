#!/usr/bin/env python3
"""Real skeletons for `instools best`: the server's worked examples (kb/reread/ins_examples.jsonl) that have a plain
skeleton, and the 46 skeletons of out/corpus_cyprian.tsv (Cyprian Kalbarczyk's blockbuilding example solves).

Plain means: not written with inverse-scramble parts, and once the insertion marks are taken out the skeleton line is
face turns only (commutator shorthand is written out; no rotations, slice or wide moves); the scramble is face turns
only too.  Nothing in the examples file was checked on a cube when it was made, so every case is put on the sticker
model here: an example counts only if scramble + skeleton leaves corners only or edges only, at most 6 pieces.  When
it does not but scramble + inverse of the skeleton does, the skeleton was written on the inverse scramble and its
inverse is used (the insertions of one are the inverses of the insertions of the other, with the same lengths).

Writes out/real_cases.tsv (scramble, skeleton, id) for real_run.py and out/real_meta.json with, per case: who, when, by
hand or Insertion Finder, the author's final length, and the author's own solution replayed (replay.py)."""
import json, re, collections, csv
import cube, cubie, replay
OUT = '/data/fmc/insertion-cost/research/out/'
EX = '/data/fmc/kb/reread/ins_examples.jsonl'
WORDING_ONLY = {'N5952', 'N4338', 'N1071', 'D4736', 'D4737', 'D4876'}      # marked Insertion Finder on the wording of the message only
def left(scr, sk):
    cp, ct, ep, ef = cubie.cubie(cube.do(cube.SOLVED, scr + sk))
    c = sum(1 for i in range(8) if cp[i] != i or ct[i]); e = sum(1 for i in range(12) if ep[i] != i or ef[i])
    return c, e
def insertable(c, e): return (c == 0 and 0 < e <= 6) or (e == 0 and 0 < c <= 6)
def notes(r):
    """(algorithm length, moves cancelled) pairs as the author wrote them, e.g. (8-2/24)."""
    out = []
    for ins in r['insertions']:
        m = re.search(r'(?<![\d.])(\d{1,2})\s*-\s*(\d{1,2})(?![\d.])', (ins.get('comment') or '').split('//')[-1] if '(' not in (ins.get('comment') or '') else re.sub(r'^[^(]*\(', '', ins.get('comment') or ''))
        if m and 1 <= int(m.group(1)) <= 20: out.append((int(m.group(1)), int(m.group(2))))
    return out
rows = [json.loads(l) for l in open(EX)]
cases = []; why = collections.Counter(); seen = {}
for r in rows:
    if r['niss']: why['written with inverse-scramble parts'] += 1; continue
    scr = replay.moves(r['scramble'] or ''); sk = replay.skeleton_moves(r)
    if not scr: why['scramble not in face turns'] += 1; continue
    if not sk: why['skeleton has rotations, slice or wide moves'] += 1; continue
    inv = False; c, e = left(scr, sk)
    if not insertable(c, e):
        c2, e2 = left(scr, cube.inv_seq(sk))
        if insertable(c2, e2): inv = True; sk = cube.inv_seq(sk); c, e = c2, e2
    if not insertable(c, e):
        why['parity (2 corners and 2 edges)' if (c, e) == (2, 2) else 'corners and edges both left' if c and e and c + e <= 12 else 'more than 6 pieces of one kind left' if c + e <= 12 else 'scramble and skeleton do not fit'] += 1
        continue
    ok, fin, steps = replay.author(r) if not inv else (False, None, [])
    key = (' '.join(scr), ' '.join(cube.cancel(sk)))
    cases.append({'id': r['id'], 'author': r['author'], 'date': r['date'], 'source': r['source'], 'wording_only': r['id'] in WORDING_ONLY, 'if_setting': r['if_setting'],
                  'scramble': ' '.join(scr), 'skeleton': ' '.join(sk), 'said': r['leftover'], 'final': r['final_length'], 'inverse': inv,
                  'notes': notes(r), 'n_ins': len(r['insertions']), 'origin': 'server', 'dup_of': seen.get(key),
                  'replayed': bool(ok), 'replay_len': len(fin) if ok else None, 'steps': steps if ok else []})
    seen.setdefault(key, r['id']); why['kept'] += 1
for r in csv.DictReader(open(OUT + 'corpus_cyprian.tsv'), delimiter='\t'):
    nt = [tuple(map(int, x.split('-'))) for x in r['notes'].split()] if r['notes'] else []
    scr = cube.parse(r['scramble']); sk = cube.parse(r['skeleton']); c, e = left(scr, sk)
    if not insertable(c, e): why['Kalbarczyk: ' + ('parity (2 corners and 2 edges)' if (c, e) == (2, 2) else 'corners and edges both left')] += 1; continue
    key = (r['scramble'], ' '.join(cube.cancel(sk)))
    cases.append({'id': 'K' + r['number'], 'author': 'Cyprian Kalbarczyk', 'date': '', 'source': 'hand', 'wording_only': False, 'if_setting': '',
                  'scramble': r['scramble'], 'skeleton': r['skeleton'], 'said': f"{r['corners_left']}c {r['edges_left']}e", 'final': int(r['final_length']), 'inverse': False,
                  'notes': nt, 'n_ins': len(nt), 'origin': 'kalbarczyk', 'dup_of': seen.get(key), 'replayed': True, 'replay_len': int(r['final_length']), 'steps': []})
    seen.setdefault(key, 'K' + r['number']); why['Kalbarczyk: kept'] += 1
with open(OUT + 'real_cases.tsv', 'w') as f:
    for c in cases: f.write(f"{c['scramble']}\t{c['skeleton']}\t{c['id']}\n")
json.dump({'cases': cases, 'excluded': dict(why), 'examples_in_file': len(rows)}, open(OUT + 'real_meta.json', 'w'), indent=0, ensure_ascii=False)
print(len(rows), 'examples;', dict(why)); print(len(cases), 'cases written;', sum(1 for c in cases if c['dup_of']), 'repeat an earlier scramble and skeleton;', sum(1 for c in cases if c['inverse']), 'on the inverse scramble')
