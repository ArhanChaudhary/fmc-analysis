#!/usr/bin/env python3
"""The "300 more, at random" section of EXAMPLES.md.

For each of the 12 corner subsets: the first 25 random DR states of that subset from a fixed seed (each state is
200 random DR moves, which is long enough to be uniform: 30 moves is not, it leaves the short-finish states about
twice too likely; the pick never looks at the optimal), each given by a shortest scramble (the inverse of an optimal
finish), with its reads, what the exact tables say for the DRs that read the same, and its optimal.

Rewrites the region of EXAMPLES.md between the two markers, then re-reads every scramble printed there from its
text alone and checks the row against it (subset, pairs, corner cases, HTR lengths, optimal = scramble length,
and the quoted odds).  Prints the number of mismatches; it has to be 0.

usage: source /data/fmc/env.sh; python3 many_examples.py      (needs drtools built and the BFS tables)"""
import random, re, sys, importlib.machinery, importlib.util
R = '/data/fmc/judging-a-dr/research/'
sys.path.insert(0, R + 'src')
import pv
loader = importlib.machinery.SourceFileLoader('drread', R + 'tool/drread')
spec = importlib.util.spec_from_loader('drread', loader); dr = importlib.util.module_from_spec(spec); loader.exec_module(dr)

PAGE = '/data/fmc/judging-a-dr/report/EXAMPLES.md'
START, END = '<!-- many-examples:start -->', '<!-- many-examples:end -->'
SEED, PER, BATCH, WALK = 20261112, 25, 4000, 200
MOVES = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
INV = {"U": "U'", "U'": "U", "D": "D'", "D'": "D"}
# the two 2c4 cases with the same bad corners, told apart by the back face (write-up, corner case section)
TELL = {'8': '; back-face diagonals agree', '7': '; back-face diagonals differ'}
HEAD = ['| # | Scramble | Edges | True pairs | Corner case, normal / inverse | Shortest HTR, normal / inverse | DRs that read the same: in 10 / 11 / 12 | Optimal |',
        '|---:|---|---|---:|---|---|---|---:|']

def scramble(n=WALK):
    out = []; last = None
    while len(out) < n:
        m = random.choice(MOVES)
        if m[0] == last: continue
        out.append(m); last = m[0]
    return ' '.join(out)

def fields(kv):
    """What a row shows, from one block of drtools read."""
    cs, e = kv['subset'].split()
    ccn, cci = kv['corner_case'].split(); hn, hi = map(int, kv['htr'].split())
    return dict(cs=cs, e=int(e[0]), tp=int(kv['true_pairs'].split()[0]), ccn=ccn, cci=cci, hn=hn, hi=hi, opt=int(kv['optimal']), finish=kv['optimal_finish'])
def same_read(f):
    """All DRs with the same subset, pairs (five or more together), corner cases on the two sides and HTR lengths."""
    return pv.q(cs=f['cs'], e=f['e'], pairs=min(f['tp'], 5), both=({f['ccn']}, {f['cci']}), htr=(f['hn'], f['hi']))
def row(i, f, names):
    short = ' '.join(INV.get(m, m) for m in reversed(f['finish'].split()))
    h = same_read(f)
    assert sum(h) > 0 and h[f['opt']] > 0, f
    return f"| {i} | `{short}` | {f['e']}e | {f['tp']} | {names[f['ccn']]} / {names[f['cci']]} | {f['hn']} / {f['hi']} | {pv.tri(h)} | {f['opt']} |"

def build():
    names = dr.corner_names(); CC = pv.corner_cases()
    random.seed(SEED)
    picked = {cs: [] for cs in pv.CS_ORDER}; seen = set(); drawn = 0; hall = [0] * 19
    while any(len(v) < PER for v in picked.values()):
        batch = [scramble() for _ in range(BATCH)]; drawn += BATCH
        for kv in dr.read_states(batch):
            if 'subset' not in kv: continue
            f = fields(kv); hall[f['opt']] += 1
            if len(picked[f['cs']]) < PER and f['finish'] not in seen:
                seen.add(f['finish']); picked[f['cs']].append(f)
    ex = pv.q()
    print(f'drew {drawn} random DR states ({WALK} random moves each, seed {SEED}) to fill 12 subsets x {PER}')
    print(f'  all drawn states: average optimal {pv.avg(hall):.3f} (exact {pv.avg(ex):.3f}), in 11 or less {pv.share(hall, 11):.2f}% (exact {pv.share(ex, 11):.2f}%), '
          f'in 12 or less {pv.share(hall, 12):.2f}% (exact {pv.share(ex, 12):.2f}%), in 13 or less {pv.share(hall, 13):.2f}% (exact {pv.share(ex, 13):.2f}%)')
    out = [START, '', '## 300 more, at random', '',
           'Three hundred more DR states for fun, 25 for each of the 12 corner subsets, so you can hold your own reads against the table. '
           'They are the first 25 of each subset in a run of uniformly random DR states (200 random DR moves each, from a fixed seed). Nothing was picked for how it came out, and 0c0 or 0c3 get as many rows as 2c4 even though they come up far less often.',
           '',
           'Each state is given by a shortest scramble, the inverse of an optimal finish. So the scramble is exactly as long as the optimal and undoing it is the solution: the answer is visible on purpose. What is worth looking at is how the reads line up with it.',
           '',
           'The columns, the same in every table:', '',
           '- **Scramble**: do it on a solved cube and you are looking at the DR.',
           '- **Edges**: the number of bad edges, so with the heading it gives the subset (2c4 with 4e is 2c4 4e).',
           '- **True pairs**: counted as in the reads above.',
           '- **Corner case, normal / inverse**: the case names of the write-up\'s corner case appendix. The cases that show up are listed above each table with where their bad corners sit.',
           '- **Shortest HTR, normal / inverse**: the true shortest on each side.',
           '- **DRs that read the same**: the share finishing in 10 / 11 / 12 or less among all DR states with the same subset, the same number of pairs (five or more count as one), the same two corner cases and the same two HTR lengths. 0 means no such state gets there.',
           '- **Optimal**: the optimal finish in DR moves.', '']
    totals = {T: [0.0, 0.0, 0] for T in (10, 11, 12)}       # expected from subset, expected from the full read, happened
    for cs in pv.CS_ORDER:
        fs = picked[cs]; hcs = pv.q(cs=cs)
        out += [f'### {cs}', '']
        used = sorted({f['ccn'] for f in fs} | {f['cci'] for f in fs}, key=lambda k: int(names[k].split('-')[1]))
        out += ['| Corner case | Bad corners | L | A qt takes it straight to |', '|---|---|---|---|']
        for k in used:
            c = CC[k]; sub = f" ({c['sub']})" if c['sub'] != cs else ''
            out.append(f"| {names[k]}{sub} | {c['layout']}{TELL.get(k, '')} | {c['lmin']}–{c['lmax']} | {c['straight'] or 'nothing, needs a setup'} |")
        out += [''] + HEAD + [row(i + 1, f, names) for i, f in enumerate(fs)] + ['']
        got = {T: sum(f['opt'] <= T for f in fs) for T in pv.TARGETS}
        exp = {T: PER * pv.share(hcs, T) / 100 for T in pv.TARGETS}
        out += [f"How the 25 came out: {got[10]} in 10 or less, {got[11]} in 11 or less, {got[12]} in 12 or less, {got[13]} in 13 or less. "
                f"All of {cs} is {pv.quad(hcs)} (in 10 / 11 / 12 / 13), which for 25 DRs is about {exp[10]:.1f}, {exp[11]:.1f}, {exp[12]:.1f} and {exp[13]:.1f}.", '']
        for f in fs:
            hs = pv.q(cs=cs, e=f['e']); hr = same_read(f)
            for T in totals:
                totals[T][0] += pv.share(hs, T) / 100; totals[T][1] += pv.share(hr, T) / 100; totals[T][2] += f['opt'] <= T
    out += ['### All 300 against the odds', '',
            'Add up the odds quoted for each of the 300 DRs and you get the number of finishes the tables expect. Against what happened:', '',
            '| Finish | Expected from the subset alone | Expected from the full read (last-but-one column) | Happened |', '|---|---:|---:|---:|']
    for T in (10, 11, 12):
        a, b, c = totals[T]; out.append(f'| {T} or less | {a:.1f} | {b:.1f} | {c} |')
    out += ['', 'The reads don\'t change how many short finishes there are in a pile of DRs. They change which DRs you expect them in:', '']
    # how concentrated: of the DRs that finished in T, the share of the expected finishes the full read had put on them
    lines = []
    for T in (11, 12):
        hit = [(pv.share(same_read(f), T), pv.share(pv.q(cs=f['cs'], e=f['e']), T)) for cs in pv.CS_ORDER for f in picked[cs] if f['opt'] <= T]
        if hit: lines.append(f"The {len(hit)} DRs that finished in {T} or less had been given {pv.num(sum(x for x, _ in hit) / len(hit))} on average by the full read and {pv.num(sum(y for _, y in hit) / len(hit))} by their subset.")
    out += [' '.join(lines), '', END]
    page = open(PAGE).read()
    assert page.count(START) == 1 and page.count(END) == 1, 'markers missing in EXAMPLES.md'
    a = page.index(START); b = page.index(END) + len(END)
    open(PAGE, 'w').write(page[:a] + '\n'.join(out) + page[b:])
    print(f'wrote {sum(len(v) for v in picked.values())} rows to {PAGE}')

def verify():
    """Re-read every scramble printed in the section, from the page's text alone."""
    names = dr.corner_names()
    page = open(PAGE).read(); region = page[page.index(START):page.index(END)]
    rows = []; cs = None
    for line in region.split('\n'):
        m = re.match(r'^### (\S+)$', line)
        if m: cs = m.group(1)
        m = re.match(r'^\| (\d+) \| `([^`]+)` \| (\d)e \| (\d+) \| (\S+) / (\S+) \| (\d+) / (\d+) \| (.+?) \| (\d+) \|$', line)
        if m: rows.append((cs,) + m.groups())
    kvs = dr.read_states([r[2] for r in rows])
    assert len(kvs) == len(rows)
    bad = 0
    for r, kv in zip(rows, kvs):
        cs, i, scr, e, tp, cn, ci, hn, hi, odds, opt = r
        f = fields(kv)
        ok = (f['cs'] == cs and f['e'] == int(e) and f['tp'] == int(tp) and names[f['ccn']] == cn and names[f['cci']] == ci
              and f['hn'] == int(hn) and f['hi'] == int(hi) and f['opt'] == int(opt) == len(scr.split()) and pv.tri(same_read(f)) == odds)
        if not ok:
            bad += 1; print('MISMATCH', r, f)
    per = {}
    for r in rows: per[r[0]] = per.get(r[0], 0) + 1
    print(f're-read {len(rows)} scrambles from the page ({len(per)} subsets, {sorted(set(per.values()))} rows each): {bad} mismatches')
    return bad

if __name__ == '__main__':
    if '--verify-only' not in sys.argv: build()
    sys.exit(1 if verify() else 0)
