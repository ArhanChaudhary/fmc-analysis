#!/usr/bin/env python3
"""Write report/EXAMPLES.md: a few of the server's own worked examples redone with the tool, then 200 play-along
examples (10 leftover types x 20 random skeletons of 16 to 22 moves, fixed seed) with the answers folded away, and
the tally.  Then the page is read back and every scramble, skeleton, insertion and solution on it is replayed on the
sticker model (`--verify` does only that).

  xexamples.py --cases     draw the skeletons, make the scrambles, run the tool: out/examples_cases.json (slow part:
                           one two-phase solve per example)
  xexamples.py             write the page from out/examples_cases.json and out/real.json, then verify
  xexamples.py --verify    verify only"""
import json, re, sys, subprocess, collections, os
from concurrent.futures import ThreadPoolExecutor
import cube, cubie, exlib, iv
R = '/data/fmc/insertion-cost/'; O = R + 'research/out/'; PAGE = R + 'report/EXAMPLES.md'
TYPES = ['3c', '5c', '2c2c-pure', '2c2c-twisted', '3c1t', '2tc', '3tc', '3e', '2e2e', '5e']
LENGTHS = [16, 17, 18, 19, 20, 21, 22]; PER = 20; SEED = 20261111
TITLE = {'3c': '3c', '5c': '5c', '2c2c-pure': 'Pure 2c2c', '2c2c-twisted': 'Twisted 2c2c', '3c1t': '3c1t', '2tc': '2tc', '3tc': '3tc', '3e': '3e', '2e2e': '2e2e', '5e': '5e'}

def draw(typ):
    """PER skeletons of type typ: three per length 16..22 from the sampler (seed fixed), taken length by length."""
    rows = []
    for n in LENGTHS:
        out = subprocess.run([exlib.BIN, 'sample', typ, str(n), '3', str(SEED + n), '--L', '8,10', '--sol-every', '1'], capture_output=True, text=True).stdout.strip().split('\n')
        hd = out[0].split('\t')
        for l in out[1:]: rows.append(dict(zip(hd, l.split('\t'))))
    # order: 16, 17, ..., 22, 16, 17, ...
    by = collections.defaultdict(list)
    for r in rows: by[len(r['skeleton'].split())].append(r)
    order = [by[n][k] for k in range(3) for n in LENGTHS]
    return order[:PER]
def make(job):
    typ, k, r = job
    sk = r['skeleton'].split()
    sol = r['L10_solution'] if r['L10_solution'] != '-' else r['L8_solution']
    assert sol != '-', (typ, k, 'no solution at cap 10')
    scr = exlib.scramble_for(sol.split())
    cp, ct, ep, ef = [[int(x) for x in part.split(',')] for part in r['leftover(cp;ct;ep;ef)'].split(';')]
    assert cube.do(cube.SOLVED, scr + sk) == cubie.make(cp, ct, ep, ef)
    b = exlib.best(scr, sk, '8,10')
    assert b['type'] == typ and b['skeleton'] == sk
    ans = {}
    for L in (8, 10):
        if L not in b['best']: ans[L] = None; continue
        model = b['best'][L][0]
        if typ in ('3c', '3e'): model = 'one'
        ans[L] = dict(b['sols'][L][model], model=model)
    return {'type': typ, 'k': k, 'scramble': scr, 'skeleton': sk, 'answers': {str(L): a for L, a in ans.items()}}
def cases():
    jobs = [(t, k + 1, r) for t in TYPES for k, r in enumerate(draw(t))]
    with ThreadPoolExecutor(3) as ex: out = list(ex.map(make, jobs))
    json.dump(out, open(O + 'examples_cases.json', 'w'))
    print('drew', len(out), 'examples:', dict(collections.Counter(c['type'] for c in out)))

SERVER = [   # (id in the examples file, title, text with [[links]])
    ('doc14§2.5.3a', 'A 5c from the tutorial',
     "The example of section 2.5.3 of Sebastiano Tronto's tutorial (\"Classic PDR\"). The tutorial takes it from Alexandre Campos's collection of PDR solves: \"Alexandre has collected some PDR solves in a document … Let’s look at the first one as an example\". 17 moves to five corners, then two comms."),
    ('N1440', 'A 5c where the comms are right and the alg list is not exhausted',
     "jperm ([[N1422]]): \"theres a 19 to 5c that i found but could not find any good insertions\". The skeleton is 21 moves. tseitsei89 found two comms for it by hand ([[N1440]]: \"8 move comm and 3 moves cancel\", \"8 move comm and 2 cancel.\") and then checked ([[N1441]]): \"IF says those are optimal insertions.\""),
    ('N2057', 'A 3c where the 8-4 is the best 8-mover and a 10-mover cancels all ten',
     "2014chri04 ([[N2057]]), 23 to 3C: \"& = [D R D', L'] cancels 4, IF verifies that this is optimal\". With time left, 2014chri04 then found by hand that a stretch of the finished solution could be replaced by something shorter, for a 22, and asked how to find such things in general."),
    ('doc92', 'The 3C1T that Insertion Finder was given twice',
     "alkamaass's 16-move skeleton ([[D3795]]), which is alkamaass's 18-move skeleton after an 8-move comm that cancels 10 (write-up, section 9.5). Insertion Finder with every alg set on and greedy 6 gives 25 ([[D3796]])."),
    ('N5938', 'A 3e with a 10-9',
     "DougCube ([[N5938]]), 18 moves to three edges. The solve starts with \"EO on LR-axis\", and a later step is commented \"but breaks EO\": the three edges that are left are oriented on {AXES}. Then: \"insert 3e comm (10-9/19)\". jisu101 ([[N5939]]): \"10-9 is also crazy ngl\"."),
]
def server_section():
    sys.path.insert(0, R + 'research/src/report_build'); import links, replay
    rows = {r['id']: r for r in json.load(open(O + 'real_rows.json'))}
    ex = {}
    for l in open('/data/fmc/kb/reread/ins_examples.jsonl'):
        e = json.loads(l); ex[e['id']] = e
    open(R + 'research/src/report_build/examples_server.src.md', 'w').write('\n\n'.join(t for _, _, t in SERVER) + '\n')
    L = ['## From the tutorial and the server', '',
         'Five worked examples, the first from the tutorial and four from the server, each with what was inserted at the time and then the best there is on the same skeleton: with 8 moves or less per insertion, with up to 10, and with up to 12. *A comm plus an alg* is two insertions of which only one has to be a 3-cycle; the other may be any alg of that length that leaves a 3c or solves what the comm left (write-up, section 3). It is shown when it beats everything else at that length.', '']
    for eid, title, text in SERVER:
        r = rows[eid]; e = ex[eid]; sk = r['reduced'].split(); scr = cube.parse(r['scramble']); typ = r['type']
        s = cube.do(cube.SOLVED, scr + sk)
        if '{AXES}' in text:
            k = exlib.axes_oriented(s); text = text.replace('{AXES}', ['none of the three axes', 'one of the three axes', 'two of the three axes', 'all three axes'][k])
        L += [f'### {title}', '', links.expand(text), '', f"Scramble: `{' '.join(scr)}`", '', f"Skeleton: `{' '.join(sk)}` ({len(sk)}), leaves {iv.LONG[typ]}: {exlib.left_text(s)}", '']
        ok, fin, steps = replay.author(e); assert ok and len(fin) == r['author_len'], eid
        who = 'By Insertion Finder' if r['source'] == 'IF' else 'By hand'
        did = ' and '.join(f"`{' '.join(cube.cancel(replay.moves(replay.strip_marks(i['alg'], replay.marks_of(e)))))}` ({a}-{b})" for i, (a, b) in zip(e['insertions'], steps))
        L += [f'**{who}**: {did}. {len(fin)} moves.', '', '```', f"Solution: {' '.join(fin)} ({len(fin)})", '```', '']
        shown = None
        for cap, label in ((8, '8 moves or less per insertion'), (10, 'Up to 10 moves per insertion'), (12, 'Up to 12 moves per insertion')):
            plain = r.get(f'L{cap}sol'); mixed = r.get(f'L{cap}msol')
            if plain is None: L += [f'**{label}**: nothing fits anywhere in this skeleton.', '']
            elif shown is not None and plain['length'] >= shown: L += [f'**{label}**: nothing better with one comm, two comms or one alg.', '']
            else:
                L += [f"**{label}** ({MODEL_WORDS[plain['model']]}): {plain['length']} in all.", '', '```'] + exlib.block(sk, plain) + ['```', '']; shown = plain['length']
            if mixed is not None and (shown is None or mixed['length'] < shown):
                L += [f"**{label}, a comm plus an alg**: {mixed['length']} in all.", '', '```'] + exlib.block(sk, mixed) + ['```', '']; shown = mixed['length']
        note = SERVER_NOTE.get(eid, '')
        if eid == 'N5938':                         # what was searched on this one, and what it found
            assert r['L12'] == r['L10'] == r['author_added'] and r['L10m'] == r['L10'] and not r['mixed12'] and r['L8'] is not None and r['L8'] > r['L10'] + 3
        if eid == 'doc14§2.5.3a': assert r['mixed12'] and r['L12m'] == r['L8'] == r['author_added']
        L += [note, ''] if note else []
    return L
SERVER_NOTE = {
    'N2057': 'The 8-4 is the best 8-mover. One 10-move comm at another spot cancels all ten of its moves. The last line is the length 2014chri04 reached by hand: a comm plus an alg wrapped around a stretch of the skeleton is the same thing as replacing that stretch, because the two algs and the moves between them cancel into something shorter.',
    'N1440': 'So the two comms found by hand are the best pair of 8-movers, as Insertion Finder said. Everything shorter needs a longer alg.',
    'doc92': 'Insertion Finder\'s result is the comm-plus-alg line at 10 moves. With every alg of up to 12 moves there is one move less.',
    'N5938': 'The 10-9 is the best single alg of up to 12 moves, and a comm plus an alg of up to 10 moves each does no better. A comm plus an alg of up to 12 moves each was not searched to the end on this skeleton. With algs of 8 moves or fewer the best is far behind.',
    'doc14§2.5.3a': 'The two comms in the tutorial are the best pair of 8-movers, and nothing up to 12 moves beats them, a comm plus an alg included.',
}
MODEL_WORDS = {'one': 'one comm', 'two': 'two comms', 'direct': 'one alg for the whole leftover', 'mixed': 'a comm plus an alg', 'two-flat': 'two comms, no nesting', 'two-apart': 'two comms that do not touch'}
def answer_lines(sk, a8, a10):
    L = []
    if a8 is None:
        L += ['**8 moves or less per insertion**: nothing fits anywhere in this skeleton.', '']
    else:
        L += [f"**8 moves or less per insertion** ({MODEL_WORDS[a8['model']]}): +{a8['cost']}, {a8['length']} in all.", '', '```'] + exlib.block(sk, a8) + ['```', '']
    if a10 is None:
        L += ['**Up to 10 moves per insertion**: nothing fits either.', '']
    elif a8 is not None and a10['cost'] >= a8['cost']:
        L += [f"**Up to 10 moves per insertion**: nothing better, {a8['length']} stays the best.", '']
    else:
        L += [f"**Up to 10 moves per insertion** ({MODEL_WORDS[a10['model']]}): +{a10['cost']}, {a10['length']} in all.", '', '```'] + exlib.block(sk, a10) + ['```', '']
    return L
def build():
    C = json.load(open(O + 'examples_cases.json'))
    real = '\n'.join(server_section())
    L = ['# Examples: what does this skeleton cost?', '',
         'Worked examples for the write-up *Insertion cost by skeleton type*. First, five worked examples (one from the tutorial, four from the server) redone with the search: what the author inserted, and the best there is with 8-movers, with algs up to 10 moves and up to 12. Then 200 skeletons to play along with, 20 for each of ten kinds of leftover: put the scramble and the skeleton on a cube, look for the insertions, then unfold the answer. Then the tally.', '',
         'The script that writes this page replays everything on it on a sticker-level cube: every scramble, skeleton, insertion and solution.', '']
    L += [real, ''] if real else []
    L += ['## 200 skeletons to play along with', '',
          'For each kind of leftover, 20 skeletons of 16 to 22 moves. They are random move sequences, not solves: each move is drawn at random (no two in a row on one face), and the leftover is drawn at random among all leftovers of that kind. So there are no blocks to spot, only the insertion to find, and none of them is picked by how it comes out. The scramble is made to fit: the skeleton solves it up to that leftover.', '',
          '### How to read them', '',
          '- **Left**: what the skeleton leaves. `A → B` means the piece now at A belongs at B; `A ↔ B` is a swap. A piece that sits in its place but turned is listed as twisted (clockwise or counter-clockwise, looking at the corner) or flipped.',
          '- **The answer** has two parts. *8 moves or less per insertion* is the best there is with pure 8-move comms (and, for edges, the 6- and 7-movers). *Up to 10 moves per insertion* also allows every 9- and 10-move alg, including one alg that does the whole leftover where such an alg exists. Each is the true minimum over every position and every alg of that length, with two insertions allowed to sit inside each other.',
          '- **Marks.** `*` is the first insertion and `^` the second. When the second one goes into moves that the first one changed, the skeleton is written out again as it stands after the first, with `^` in it.',
          '- `// (8-3/22)` is the usual note: an 8-move alg, 3 moves cancel, 22 moves so far.',
          '- When the answer says "nothing better" for 10 moves, the 8-move answer is still the best one.', '']
    tally = collections.defaultdict(list)
    for typ in TYPES:
        mine = [c for c in C if c['type'] == typ]
        L += [f"### {TITLE[typ]}: skeletons {mine[0]['k']}–{mine[-1]['k']}", '', f'{iv.LONG[typ][0].upper() + iv.LONG[typ][1:]}.', '']
        for c in mine:
            sk, scr = c['skeleton'], c['scramble']; a8, a10 = c['answers']['8'], c['answers']['10']
            s = cube.do(cube.SOLVED, scr + sk)
            L += [f"#### {TITLE[typ]}, skeleton {c['k']}", '', f"Scramble: `{' '.join(scr)}`", '', f"Skeleton: `{' '.join(sk)}` ({len(sk)})", '', f'Left: {exlib.left_text(s)}', '',
                  '<details>', f"<summary>Answer for {TITLE[typ].lower() if typ not in ('3c', '5c', '3e', '5e') else TITLE[typ]}, skeleton {c['k']}</summary>", '']
            L += answer_lines(sk, a8, a10)
            L += ['</details>', '']
            tally[typ].append((len(sk), a8['cost'] if a8 else None, a10['cost'] if a10 else None))
    L += ['## The tally', '', 'Over the 20 skeletons of each kind above, next to the same numbers from the big samples of the write-up (20,000 random skeletons of 20 moves at 8 moves per insertion, 5,000 for 2tc and 2e2e; fewer at 10, see the write-up). One row per leftover; the counts are of the 20 skeletons.', '',
          '| Leftover | On this page: mean added, 8 moves or less | On this page: nothing fits at 8 | On this page: mean added, up to 10 | On this page: up to 10 beats 8 or less | Write-up, 20-move skeletons: mean added, 8 or less | Write-up: mean added, up to 10 |', '|---|---:|---:|---:|---:|---:|---:|']
    for typ in TYPES:
        t = tally[typ]; v8 = [x[1] for x in t if x[1] is not None]; v10 = [x[2] for x in t if x[2] is not None]
        better = sum(1 for x in t if x[2] is not None and (x[1] is None or x[2] < x[1]))
        c8, c10 = iv.cell(typ, 20, 8, iv.head(typ)), iv.cell(typ, 20, 10, iv.head(typ))
        L.append(f"| {iv.SHOW[typ]} | {sum(v8) / len(v8):.2f} | {len(t) - len(v8)} of {len(t)} | {sum(v10) / len(v10):.2f} | {better} of {len(t)} | {iv.mean(c8):.2f} | {iv.mean(c10):.2f} |")
    L += ['', 'Twenty skeletons are a handful: the page is for practice, the write-up has the odds. Every answer is the best there is for its cap, the answer key, not what you find in the time you have.', '']
    open(PAGE, 'w').write('\n'.join(L))
    print('wrote', PAGE, len(L), 'lines')
def verify():
    txt = open(PAGE).read(); bad = 0; n_ex = n_blocks = n_server = 0
    # the play-along examples
    parts = re.split(r'^#### (.+), skeleton (\d+)$', txt.split('## 200 skeletons to play along with')[1].split('## The tally')[0], flags=re.M)[1:]
    names = {v: k for k, v in TITLE.items()}
    for title, k, body in zip(parts[0::3], parts[1::3], parts[2::3]):
        typ = names[title]; n_ex += 1
        scr = cube.parse(re.search(r'^Scramble: `([^`]+)`$', body, flags=re.M).group(1))
        m = re.search(r'^Skeleton: `([^`]+)` \((\d+)\)$', body, flags=re.M); sk = cube.parse(m.group(1))
        left = re.search(r'^Left: (.+)$', body, flags=re.M).group(1)
        s = cube.do(cube.SOLVED, scr + sk)
        if len(sk) != int(m.group(2)) or cube.cancel(sk) != sk or exlib.type_of(s) != typ or exlib.left_text(s) != left: bad += 1
        heads = re.findall(r'^\*\*(8 moves or less|Up to 10 moves) per insertion\*\*([^\n]*)$', body, flags=re.M)
        blocks = re.findall(r'^\*\*[^\n]*\+(-?\d+), (\d+) in all\.\n\n```\n(.*?)\n```', body, flags=re.M | re.S)
        for cost, total, blk in blocks:
            b, fin = exlib.check_block(blk.split('\n'), scr, sk); n_blocks += 1
            if b or fin != int(total) or fin - len(sk) != int(cost): bad += 1
    # the server's examples
    assert '## From the tutorial and the server' in txt
    if '## From the tutorial and the server' in txt:
        sec = txt.split('## From the tutorial and the server')[1].split('## 200 skeletons to play along with')[0]
        for body in re.split(r'^### ', sec, flags=re.M)[1:]:
            scr = cube.parse(re.search(r'^Scramble: `([^`]+)`$', body, flags=re.M).group(1))
            m = re.search(r'^Skeleton: `([^`]+)` \((\d+)\), leaves .+$', body, flags=re.M); sk = cube.parse(m.group(1)); n_server += 1
            if len(sk) != int(m.group(2)): bad += 1
            for total, blk in re.findall(r'^\*\*[^\n]*?(\d+) in all[^\n]*\n\n```\n(.*?)\n```', body, flags=re.M | re.S):
                b, fin = exlib.check_block(blk.split('\n'), scr, sk); n_blocks += 1
                if b or fin != int(total): bad += 1
            for total, seq, ln in re.findall(r'^\*\*By (?:hand|Insertion Finder)\*\*[^\n]*?(\d+) moves\.\n\n```\nSolution: (.+) \((\d+)\)\n```', body, flags=re.M):
                seq = cube.parse(seq); n_blocks += 1
                if len(seq) != int(ln) or int(total) != int(ln) or cube.do(cube.SOLVED, scr + seq) != cube.SOLVED: bad += 1
            s = cube.do(cube.SOLVED, scr + sk)
            if m.group(0).split('leaves ')[-1] != f'{iv.LONG[exlib.type_of(s)]}: {exlib.left_text(s)}': bad += 1
    print(f're-read the page: {n_server} examples from the tutorial and the server and {n_ex} play-along skeletons; {n_blocks} written solutions replayed on the sticker model (skeleton lines, insertions, cancellations, lengths, and that scramble + solution is solved); mismatches: {bad}')
    return bad
if __name__ == '__main__':
    if '--cases' in sys.argv: cases(); sys.exit()
    if '--verify' not in sys.argv: build()
    sys.exit(1 if verify() else 0)
