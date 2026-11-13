#!/usr/bin/env python3
"""Write report/EXAMPLES.md: the tutorial's first example with this study's numbers, then 100 real scrambles with
their slice-EO skips and the DR-xs routes on them, answers folded away, and the tally.  `--verify` re-reads the page
and replays every route and solution on the sticker model."""
import csv, json, re, sys, random, subprocess, collections
import cube, fe, coords, export_cubie, xv
from check_examples import kinds as kinds_of
R = '/data/fmc/is-dr-xs-worth-it/'; O = R + 'research/out/'; PAGE = R + 'report/EXAMPLES.md'
SCR = [l.strip() for l in open('/data/fmc/judging-a-dr/research/out/hand/attempt_scrambles.txt') if l.strip() and not l.startswith('#')]
NPAGE = 100
KIND = ['E' if p[1] == 0 else 'M' if p[0] == 0 else 'S' for p in coords.EDGES]
G = {'F/B': {'E': 0, 'M': 0, 'S': 0}, 'U/D': {'E': 0, 'M': 1, 'S': 0}, 'R/L': {'E': 1, 'M': 0, 'S': 0}}
def skips(s):
    """Slice-EO skips of a state: (slice, axis, 'oriented' / 'misoriented')."""
    b = coords.flips(s); out = []
    piece = []
    for i in range(12):
        cols = {fe.cax(s, j) for j in coords.EF[i]}
        piece.append('E' if 1 not in cols else 'M' if 0 not in cols else 'S')
    for T in 'EMS':
        idx = [i for i in range(12) if piece[i] == T]
        for ax in ('U/D', 'R/L', 'F/B'):
            v = [b[i] ^ G[ax][KIND[i]] ^ G[ax][T] for i in idx]
            if sum(v) == 0: out.append((T, ax, 'oriented'))
            if sum(v) == 4: out.append((T, ax, 'misoriented'))
    return out
def load(name):
    d = collections.defaultdict(list)
    for r in csv.DictReader(open(O + name), delimiter='\t'): d[int(r['scramble'])].append(r)
    return d
def base():
    out = {}
    for l in open('/data/fmc/judging-a-dr/research/out/hand/attempt_run.csv'):
        if l.startswith('#'): continue
        v = l.strip().split(',')
        if v[0] == 'scramble': head = v; continue
        out[int(v[0])] = {k: int(x) for k, x in zip(head, v)}
    return out
def route(r): return f"`({r['moves']})`" if r['side'] == '1' else f"`{r['moves']}`"
def frm(r):
    fl = 'oriented' if r['flavour'] == '0' else 'misoriented'
    if r['start'] == '0': return f"skip: {r['slice']} slice on {r['axis'][0]}/{r['axis'][1]}, {fl}"
    if r['start'] == '1': return f"one-move slice EO: {r['slice']} slice on {r['axis'][0]}/{r['axis'][1]}, {fl}"
    return f"EO on {r['axis'][0]}/{r['axis'][1]}"
def pick(rows1, rows8, seed):
    rnd = random.Random(seed)
    def first(rows, n):
        rows = sorted(rows, key=lambda r: (int(r['length']), rnd.random()))
        return rows[:n]
    return first(rows1, 6), first(rows8, 2)
def classic(b, ln): return min(b[f'best{c}'] for c in (9, 10, 11, 12) if c <= ln)
def tutorial():
    S = "R' U' F U R F B' U2 F' L2 U B2 L' F' R2 D2 F' R2 F B' L2 U' R' U' F"
    E = '/data/fmc/judging-a-dr/research/data/lean_exact_table.u8'
    def fin(seq): return subprocess.run([R + 'research/xstools/target/release/xstools', 'finish', O + 'tables', O + 'kinds.tsv', E, ' '.join(seq)], capture_output=True, text=True).stdout.strip().split('\t')
    inv = cube.inv_seq(S); L = []
    a = fin(inv + cube.parse("R' D2 L U L")); b = fin(inv + cube.parse("R' D2 L U R"))
    assert a[0] == 'other' and b[0] == 'DR-1s'
    T = b[-1].split(); whole = xv_cancel(cube.inv_seq(cube.parse("R' D2 L U R") + T))
    assert cube.do(cube.do(cube.SOLVED, S), whole) == cube.SOLVED
    sk_n = skips(cube.do(cube.SOLVED, S)); sk_i = skips(cube.do(cube.SOLVED, inv))
    L += ['## The tutorial\'s first example, with the numbers', '',
          'tseitsei89\'s DR-Xs tutorial walks through FMCL S9W3A2. Here are its steps, with what the tables say at each one.', '',
          '```', f'{S} // scramble', '```', '',
          f"- **Slice-EO skips.** The tutorial lists two on normal and three on inverse. The count here: {len(sk_n)} on normal ({', '.join(f'{t} on {ax} {fl}' for t, ax, fl in sk_n)}) and {len(sk_i)} on inverse ({', '.join(f'{t} on {ax} {fl}' for t, ax, fl in sk_i)}).",
          f"- **`(R' D2 L U L)`**, the tutorial's \"DR-2s in 5 moves\": {a[1]}. Two flipped edges with the centers right is a DR-2s by the table in section 3 of the write-up.",
          f"- **`(L' R)`** on top, which cancels to `(R' D2 L U R)`, the tutorial's \"4a2-1s in 5\": {b[1]}. The tutorial says \"The shortest possible setups for edges are 5 moves\", which is the same count.",
          f"- **The finish.** The best finish of the form setup, slice, DR finish from that DR-1s is {b[2].split()[1]} moves, and its first move cancels with the last move of the route. Written out for the scramble:", '', '  ```', f"  {' '.join(whole)} // ({len(whole)})", '  ```', '',
          f"- The tutorial's own solution is 19 too. So on this DR-1s the method as taught finds the best there is of its form.", '']
    return L
def xv_cancel(seq):
    """Merge consecutive turns about one axis, face by face."""
    out = []
    AXF = {'U': 'UD', 'D': 'UD', 'R': 'RL', 'L': 'RL', 'F': 'FB', 'B': 'FB'}
    q = lambda m: 2 if m.endswith('2') else 3 if m.endswith("'") else 1
    name = lambda f, k: f + {1: '', 2: '2', 3: "'"}[k]
    i = 0; seq = list(seq)
    while i < len(seq):
        ax = AXF[seq[i][0]]; cnt = collections.OrderedDict()
        while out and AXF[out[-1][0]] == ax:
            m = out.pop(); cnt[m[0]] = cnt.get(m[0], 0) + q(m)
        while i < len(seq) and AXF[seq[i][0]] == ax:
            cnt[seq[i][0]] = cnt.get(seq[i][0], 0) + q(seq[i]); i += 1
        for f in ax:
            if cnt.get(f, 0) % 4: out.append(name(f, cnt[f] % 4))
    return out
def build():
    one, eight, B = load('attempts_1s.tsv'), load('attempts_8fe.tsv'), base()
    L = ['# Examples: is there a DR-xs worth finishing?', '',
         'Worked examples for the write-up *Is DR-xs worth it?*. First the tutorial\'s own example with the numbers. Then a hundred real scrambles: the slice-EO skips on each, the short DR-1s and DR-2s 8fe they lead to, and, folded away, how each one finishes and whether it beats the normal DRs on that scramble. Then the tally over all 500.', '']
    L += tutorial()
    L += ['## 100 scrambles: what a slice EO gives you', '',
          'The first hundred of the 500 random-state scrambles of the write-up\'s section 7. They\'re the same hundred as on the first study\'s examples page, with the same numbers, so you can put the normal DRs next to these.', '',
          '**What\'s listed.** Every route here starts from a slice-EO skip or a one-move slice EO and then keeps the EO of that axis (the tutorial\'s route), or, for a DR-2s 8fe, may also start from a normal EO of 4 moves or fewer. Each scramble shows at most six DR-1s of 8 moves or less and at most two DR-2s 8fe of 9 or less, the shortest first, drawn at random among equals. Nothing is picked by how it finishes.', '',
          '### How to read the tables', '',
          '- **Skips**: the slice-EO skips of the scramble, on normal and on inverse, as slice, axis, and whether the four edges are all oriented or all misoriented.',
          '- **Route**: the moves to the DR-xs. Brackets mean the whole route is on inverse. **Length**: its moves.',
          '- **Kind**: DR-1s or DR-2s 8fe. **Starts from**: the slice EO the route starts from (for an 8fe possibly a normal EO).',
          '- **Corner subset**: as in "4a2-1s". **Fewest turns to a real DR**: the fewest face turns from that state to a real DR (a DR-1s: 2 to 6, a DR-2s 8fe: 4).',
          '- **Finish** (answers): the best finish of the method\'s form, setup, slice(s), DR finish. For the 8fe the setup is searched up to 3 moves from either end.',
          '- **Solution** (answers): the whole solution for the scramble with all cancelling done; its length is the last column. A route on inverse is turned around for you.',
          '- **Normal DRs** (answers): the best solution through any normal DR of 10, 11 and 12 moves or less on that scramble, each finished optimally (first study).', '',
          '### The scrambles', '']
    stats = collections.Counter()
    for k in range(1, NPAGE + 1):
        s = cube.do(cube.SOLVED, SCR[k - 1]); b = B[k]
        r1, r8 = pick(one[k], eight[k], 1000 + k); rows = r1 + r8
        sk = [('normal',) + x for x in skips(s)] + [('inverse',) + x for x in skips(cube.inverse(s))]
        L += [f'#### Scramble {k}', '', '```', f'{SCR[k - 1]} // scramble', '```', '']
        L.append('Skips: ' + ('; '.join(f'{side}: {t} slice on {ax}, {fl}' for side, t, ax, fl in sk) if sk else 'none') + '.')
        L.append('')
        if not rows:
            L += [f"No DR-1s of 8 moves or less and no DR-2s 8fe of 9 or less here. The shortest normal DR is {b['shortest_dr']} moves; the best solution through a normal DR of 12 or less is {b['best']}.", '']
            stats['none'] += 1; continue
        L += ['Each row is one route to a DR-xs on this scramble, shortest first; the last column is how far that DR-xs is from a real DR.', '',
              '| # | Route | Length, moves | Kind | Starts from | Corner subset | Fewest turns to a real DR |', '|---:|---|---:|---|---|---|---:|']
        for j, r in enumerate(rows, 1):
            L.append(f"| {j} | {route(r)} | {r['length']} | {'DR-1s' if r['class'] == '1' else 'DR-2s 8fe'} | {frm(r)} | {r['subset']} | {r['turns_to_dr']} |")
        n1 = sum(1 for r in one[k]); n8 = len(eight[k])
        L += ['', f"Shown: {len(r1)} of the {n1} DR-1s of 8 or less and {len(r8)} of the {n8} DR-2s 8fe of 9 or less. Shortest normal DR: {b['shortest_dr']} moves.", '',
              '<details>', f'<summary>Answers for scramble {k}</summary>', '',
              'Each row is the route with the same number above: the best finish of the method\'s form from it, then the whole solution written out for the scramble.', '',
              '| # | Finish, moves | Solution | Solution length, moves |', '|---:|---:|---|---:|']
        for j, r in enumerate(rows, 1): L.append(f"| {j} | {r['finish']} | `{r['solution']}` | {r['total']} |")
        best = min(int(r['total']) for r in rows); c10, c11, c12 = classic(b, 10), classic(b, 11), classic(b, 12)
        cl = lambda v: 'none' if v == 99 else str(v)
        verdict = ('shorter than every normal DR of 12 or less gives' if best < c12 else 'as short as the best through a normal DR of 12 or less' if best == c12 else
                   'shorter than every normal DR of 11 or less gives' if best < c11 else 'as short as the best through a normal DR of 11 or less' if best == c11 else
                   'shorter than every normal DR of 10 or less gives' if best < c10 else 'as short as the best through a normal DR of 10 or less' if best == c10 else 'longer than the best through a normal DR of 10 or less')
        stats[verdict] += 1
        L += ['', f"Best of these: **{best}**, {verdict}. Normal DRs on this scramble: {cl(c10)} through one of 10 or less, {cl(c11)} through 11 or less, {cl(c12)} through 12 or less.", '', '</details>', '']
    L += ['### The tally', '', f'Of the hundred above: ' + '; '.join(f'{v} {"have none listed" if k == "none" else "where the best shown is " + k}' for k, v in stats.most_common()) + '.', '',
          'Over all 500 scrambles and every DR-xs of the kinds listed, not just the ones shown (write-up, section 7). How often one of them is as good as the best normal-DR solution of its scramble; each row is a kind of thing to finish, and the last column is the same share turned around:', '',
          open(R + 'report/data/real_yield.md').read().strip(), '', 'And what finishing them does to the result, over the scrambles with a normal DR of 10 or less; each row is a set of things you finish:', '', open(R + 'report/data/real_result.md').read().strip(), '',
          'Every finish is the best of its form, the answer key, not what you find in an hour.', '']
    open(PAGE, 'w').write('\n'.join(L))
    print('wrote', PAGE, len(L), 'lines;', dict(stats))
def verify():
    txt = open(PAGE).read(); blocks = re.split(r'^#### Scramble (\d+)$', txt, flags=re.M)[1:]
    n = bad = 0
    for k, body in zip(blocks[0::2], blocks[1::2]):
        scr = re.search(r'^```\n(.+?) // scramble\n```$', body, flags=re.M).group(1); assert scr == SCR[int(k) - 1]
        x = cube.do(cube.SOLVED, scr)
        routes = re.findall(r'^\| (\d+) \| `(\(?)([^`)]*)\)?` \| (\d+) \| (DR-1s|DR-2s 8fe) \|', body, flags=re.M)
        sols = dict(re.findall(r'^\| (\d+) \| \d+ \| `([^`]+)` \| \d+ \|', body, flags=re.M))
        lens = dict(re.findall(r'^\| (\d+) \| \d+ \| `[^`]+` \| (\d+) \|', body, flags=re.M))
        for j, par, mv, ln, kind in routes:
            side = cube.inverse(x) if par else x
            w = cube.do(side, mv); ks = kinds_of(w)
            ok = any(c != f and nf == (4 if kind == 'DR-1s' else 8) and sl == (1 if kind == 'DR-1s' else 2) for sl, nf, c, f in ks) and len(cube.parse(mv)) == int(ln)
            sol = cube.parse(sols[j]); ok2 = cube.do(x, sol) == cube.SOLVED and len(sol) == int(lens[j])
            n += 1; bad += not (ok and ok2)
    print(f're-read {len(blocks) // 2} scrambles from the page: {n} routes and solutions replayed, {bad} wrong')
if __name__ == '__main__':
    if '--verify' not in sys.argv: build()
    verify()
