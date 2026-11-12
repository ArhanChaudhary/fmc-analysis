#!/usr/bin/env python3
"""Real skeletons: Cyprian Kalbarczyk's "Blockbuilding example solves" (a Google Doc linked on the server, kb doc 178).
For each solve that writes a first skeleton ("Sk1:" or "Sk:") and a final solution ("S:"), check on the sticker model
that the solution solves the scramble, read off what the skeleton leaves, and write out/corpus_cyprian.tsv:
number, scramble, skeleton (plain moves), pieces left (corners, edges), the author's (alg length - cancelled) notes,
the author's final length."""
import re, sys, collections
import cube
sys.path.insert(0, '/data/fmc/is-dr-xs-worth-it/research/src'); import fe
F = '/data/fmc/kb/docs/gdoc/1oWbbzc375q4FRIuzA5U091yaiGxt0zkFObGPe5P24_I.md'
txt = open(F).read().replace('’', "'").replace('‘', "'").replace('\\', '')
blocks = re.split(r'\n\*\*(\d+)\. ', txt)[1:]
MOVE = r"[UDRLFB][2']?"
def moves(s): return re.findall(MOVE, s)
def left(s):
    c = sum(1 for p, pl in fe.CUBIES.items() if len(pl) == 3 and any(s[i] != i for i in pl))
    e = sum(1 for p, pl in fe.CUBIES.items() if len(pl) == 2 and any(s[i] != i for i in pl))
    return c, e
rows = []; stats = collections.Counter()
for num, body in zip(blocks[0::2], blocks[1::2]):
    head, _, rest = body.partition('**')
    scr = moves(head)
    # the first skeleton is the first "Sk1:", "Sk:" or "S:" line that carries an insertion mark; the solution is the last "S:" line without one
    MARK = r'[@#*^$%&!+]'
    cands = [m.group(2) for m in re.finditer(r'^(Sk1?|S):\s*(.+)$', rest, flags=re.M)]
    sks = [c for c in cands if re.search(MARK, c)]
    sols = [m.group(1) for m in re.finditer(r'^S:\s*(.+)$', rest, flags=re.M) if not re.search(MARK, m.group(1))]
    if not sks: stats['no skeleton with an insertion mark'] += 1; continue
    if not sols: stats['no final solution line'] += 1; continue
    line = sks[0]
    class _M:                                      # keep the old variable names below
        def __init__(self, t): self.t = t
        def group(self, i): return self.t
    m_s = _M(sols[-1])
    if re.search(r'[xyzMESw]', re.sub(r'\(.*?\)', '', line)) and not moves(line): stats['unreadable'] += 1; continue
    if re.search(r'[a-zMES]', re.sub(r"[^A-Za-z]", '', line).replace('U', '').replace('D', '').replace('R', '').replace('L', '').replace('F', '').replace('B', '')): stats['skeleton has rotations, slices or wide moves'] += 1; continue
    if '(' in line: stats['skeleton written with NISS'] += 1; continue
    sk = moves(line); sol = moves(m_s.group(1))
    if re.search(r'[xyzMESw]', m_s.group(1)): stats['solution has rotations, slices or wide moves'] += 1; continue
    x = cube.do(cube.SOLVED, scr)
    if cube.do(x, sol) != cube.SOLVED: stats['solution line does not solve the scramble as parsed'] += 1; continue
    c, e = left(cube.do(x, sk))
    notes = re.findall(r'\((\d+)-(\d+)\)', rest)
    final = re.search(r'^\s*(\d+)\s*$', rest, flags=re.M)
    rows.append((num, ' '.join(scr), ' '.join(sk), c, e, ' '.join(f'{a}-{b}' for a, b in notes), len(sol)))
    stats['ok'] += 1
with open('/data/fmc/insertion-cost/research/out/corpus_cyprian.tsv', 'w') as f:
    f.write('number\tscramble\tskeleton\tcorners_left\tedges_left\tnotes\tfinal_length\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')
print(dict(stats)); print('left (corners, edges):', sorted(collections.Counter((r[3], r[4]) for r in rows).items()))
print('skeleton lengths:', sorted(collections.Counter(len(r[2].split()) for r in rows).items()))
