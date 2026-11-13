#!/usr/bin/env python3
"""Replay the published examples page (report/EXAMPLES.md) with the independent tool vhtr.

For each of the 200 DRs: the labels on both sides, the three shortest HTR lengths, the optimum and the number of
optimal finishes; each checklist row's yes / no (HTR within 2, any HTR); each printed reading (it solves the
scramble in the optimal length, has the stated class and HTR length, and the "as read on normal" line is the same
finish); each printed reduction (kind of the reduced state, the rest solves it with the stated quarter turns, the
total is the optimum, and the reduction is the shortest of its kind over the optimal finishes).
Usage: check_examples_page.py [EXAMPLES.md]   (needs the vhtr binary: VHTR=/path/to/vhtr)"""
import re, sys, os, subprocess
PAGE = sys.argv[1] if len(sys.argv) > 1 else '/data/fmc/htr-routes/report/EXAMPLES.md'
VHTR = os.environ.get('VHTR', '/data/fmc/tmp/vhtr_target2/release/vhtr')
INV = {"U": "U'", "U'": "U", "D": "D'", "D'": "D"}
def inv(seq): return ' '.join(INV.get(m, m) for m in reversed(seq.split()))
def norm(route): return route.replace(' | ht', '').replace(' > ', ' ')
def split_niss(txt):
    """'A B (C D)' -> ('A B', 'C D')"""
    m = re.fullmatch(r'\s*([^()]*?)\s*(?:\(([^()]*)\))?\s*', txt)
    return m.group(1).strip(), (m.group(2) or '').strip()

text = open(PAGE).read()
blocks = re.split(r'(?m)^(?=\*\*[0-9a-c]+ \de, example \d+\.\*\*)', text)[1:]
jobs, ex = [], []
for b in blocks:
    h = re.match(r'\*\*([0-9a-c]+ \de), example (\d+)\.\*\* `([^`]+)`', b)
    cell, num, scr = h.group(1), int(h.group(2)), h.group(3)
    r = re.search(r'Read as (\S+ \de) on normal, (\S+ \de) on inverse\. Shortest HTR: (\d+) on normal, (\d+) on inverse, (\d+) with NISS', b)
    o = re.search(r'Optimal: (\d+) moves \((\d+) optimal finish', b)
    e = dict(cell=cell, num=num, scr=scr, read=r.groups(), opt=(int(o.group(1)), int(o.group(2))), rows=[], cls=[], red=[], none=[])
    for m in re.finditer(r'(?m)^\| (\d+) \| `([^`]+)` \| [\d.]+% \| (yes|no) \| (yes|no) \|', b):
        e['rows'].append((int(m.group(1)), m.group(2), m.group(3), m.group(4)))
    for m in re.finditer(r'(?m)^- Class (\d+): (normal first|inverse first|linear on normal|linear on the inverse): `([^`]+)`(?:, then on (?:inverse|normal) `([^`]+)`)?\. HTR after (\d+) moves \(([^)]*)\); the whole finish, as read on normal: `([^`]+)`\.', b):
        e['cls'].append(m.groups())
    for m in re.finditer(r'(?m)^- Shortest reduction to (\d)q \(([^)]*)\) on an optimal path: (\d+) moves?(?:, `([^`]*)`| \(the DR is already there\)); the reduced state is then solved by `([^`]*)` \((\d+) moves, (\d+) quarter turns?\)\.', b):
        e['red'].append(m.groups())
    for m in re.finditer(r'(?m)^- No optimal finish has a stretch with exactly (\d) quarter turns', b):
        e['none'].append(int(m.group(1)))
    nlines = len(re.findall(r'(?m)^- (Class|Shortest reduction|No optimal finish)', b))
    assert nlines == len(e['cls']) + len(e['red']) + len(e['none']), (cell, num, 'unparsed line')
    ex.append(e)
    jobs.append(('S', scr))
    for c in e['cls']:
        k, how, first, second, htr, note, whole = c
        if how == 'normal first':
            a, bb = first, second.strip('()'); f = (a + ' ' + inv(bb)).strip(); kk, invf = len(a.split()), 0
        elif how == 'inverse first':
            bb, a = first.strip('()'), second; f = (a + ' ' + inv(bb)).strip(); kk, invf = len(a.split()), 1
        elif how == 'linear on normal':
            f = first; kk, invf = len(f.split()), 0
        else:
            f = inv(first.strip('()')); kk, invf = 0, 1
        c_f = f
        jobs.append(('R', scr, f, str(kk), str(invf)))
        e.setdefault('fin', []).append(c_f)
    for rd in e['red']:
        p, u = split_niss(rd[3] or '')
        jobs.append(('D', scr, p, u, rd[4]))
print(len(ex), 'examples,', len(jobs), 'jobs', file=sys.stderr)
res = subprocess.run([VHTR, 'page'], input='\n'.join('\t'.join(j) for j in jobs) + '\n', capture_output=True, text=True, check=True).stdout.split('\n')
it = iter(res)
bad, checks = [], 0
def chk(cond, *what):
    global checks
    checks += 1
    if not cond: bad.append(what)
for e in ex:
    tag = f"{e['cell']} ex {e['num']}"
    s = next(it).split('\t')
    lab_n, lab_i, ln, li, niss, d, nopt, red1, red2 = s[1], s[2], int(s[3]), int(s[4]), int(s[5]), int(s[6]), int(s[7]), int(s[8]), int(s[9])
    routes = dict((norm(x.rsplit('=', 1)[0]), int(x.rsplit('=', 1)[1])) for x in s[10].split(';')) if s[10] else {}
    sub = lambda l: re.sub(r'^4[ab]([34])', r'4c\1', l)
    chk(sub(lab_n) == e['cell'] or lab_n == e['cell'], tag, 'cell', lab_n)
    chk((lab_n, lab_i, str(ln), str(li), str(niss)) == e['read'], tag, 'read-as line', (lab_n, lab_i, ln, li, niss), e['read'])
    chk((d, nopt) == e['opt'], tag, 'optimum / count', (d, nopt), e['opt'])
    for k, cls, y2, yany in e['rows']:
        mine_any = cls in routes
        mine_2 = mine_any and routes[cls] <= niss + 2
        chk(('yes' if mine_2 else 'no') == y2, tag, 'row', k, cls, 'within 2', y2, routes.get(cls))
        chk(('yes' if mine_any else 'no') == yany, tag, 'row', k, cls, 'any', yany, routes.get(cls))
    rowcls = {k: (cls, y2, yany) for k, cls, y2, yany in e['rows']}
    chk(len(e['cls']) == sum(1 for r in e['rows'] if r[3] == 'yes'), tag, 'a reading printed for every class that finds an optimal')
    for c, f in zip(e['cls'], e.get('fin', [])):
        k, how, first, second, htr, note, whole = c
        r = next(it).split('\t')
        route, rh, solved, flen, dd = norm(r[1]), int(r[2]), r[3], int(r[4]), int(r[5])
        cls, y2, yany = rowcls[int(k)]
        chk(solved == '1' and flen == dd, tag, 'class', k, 'finish solves in the optimum', solved, flen, dd)
        chk(route == cls, tag, 'class', k, 'reading has class', route, cls)
        chk(rh == int(htr), tag, 'class', k, 'HTR length', rh, htr)
        chk(f == whole, tag, 'class', k, 'as read on normal', f, whole)
        want = 'within the budget' if rh <= niss + 2 else f'{rh - niss} over the shortest NISS HTR'
        chk(note == want, tag, 'class', k, 'budget note', note, want)
        chk((y2 == 'yes') == (rh <= niss + 2), tag, 'class', k, 'printed reading is within budget iff the row says yes', y2, rh, niss)
        chk(routes.get(cls) is not None and (rh == routes[cls] or y2 == 'no' or rh <= niss + 2), tag, 'class', k, 'min HTR', rh, routes.get(cls))
    for rd in e['red']:
        q, kind, rlen, redtxt, rest, restlen, restq = rd
        r = next(it).split('\t')
        lab, qdist, solves, nq, total, dd, ends = r[1], int(r[2]), r[3], int(r[4]), int(r[5]), int(r[6]), r[7]
        p, u = split_niss(redtxt or '')
        chk(len(p.split()) + len(u.split()) == int(rlen), tag, 'reduction', q, 'length', rlen)
        chk(qdist == int(q), tag, 'reduction', q, 'reduced state is', qdist, 'quarter turns from HTR')
        chk(kind.replace(' here', '') == lab, tag, 'reduction', q, 'kind', kind, lab)
        chk(solves == '1' and nq == int(restq) == int(q) and len(rest.split()) == int(restlen), tag, 'reduction', q, 'rest', solves, nq, restq)
        chk(total == dd, tag, 'reduction', q, 'total is the optimum', total, dd)
        chk(ends == '1', tag, 'reduction', q, 'each side empty or ending in a quarter turn')
        chk(int(rlen) == (red1 if q == '1' else red2), tag, 'reduction', q, 'is the shortest over the optimal finishes', rlen, red1, red2)
    for q in e['none']:
        chk((red1 if q == 1 else red2) < 0 or (red1 if q == 1 else red2) > 10**9, tag, 'no stretch with', q, 'qt', red1, red2)
    chk(len(e['red']) + len(e['none']) == 2, tag, 'two bounding lines', len(e['red']), len(e['none']))
print(f'{len(ex)} examples, {checks} checks, {len(bad)} mismatches')
for b in bad[:40]: print('  ', b)
