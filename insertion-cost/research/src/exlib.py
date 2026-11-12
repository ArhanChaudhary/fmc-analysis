#!/usr/bin/env python3
"""What the examples page and the witness scrambles share: a scramble for a skeleton and a leftover, the tool's
solutions for a scramble and skeleton, how a solution is written with marks, and how such a block is read back and
replayed on the sticker model.

  scramble_for(solution)      an FMC-style scramble (R' U' F ... R' U' F) whose inverse state is the given solution,
                              from nissy's two-phase solver
  best(scramble, skeleton)    parsed output of `instools best`: {L: {model: sol}}, sol = {cost, length, nested,
                              steps: [(position, algorithm, cancelled)], final}
  left_text(state)            what a skeleton leaves, in words: cycles of places and pieces twisted or flipped in place
  block(skeleton, sol)        the lines of a solution: skeleton with marks, `* = alg // (8-2/26)`, `Solution: ... (26)`
  check_block(lines, ...)     replays such lines; returns the number of things that do not fit"""
import re, subprocess, os
import cube, cubie
BIN = '/data/fmc/insertion-cost/research/instools/target/release/instools'
ENV = dict(os.environ, NISSYDATA='/data/fmc/tools/nissy-data')
NISSY = '/data/fmc/tools/nissy-2.0.8/nissy'
PAD = ["R'", "U'", 'F']
def _twophase(seq):
    out = subprocess.run([NISSY, 'twophase', ' '.join(seq)], capture_output=True, text=True, env=ENV, cwd='/data/fmc/tmp').stdout.strip().split('\n')[-1]
    return cube.parse(re.sub(r'\(\d+\)\s*$', '', out).strip())
def scramble_for(solution):
    """A scramble Z = R' U' F M R' U' F with Z + solution = solved.  M is the inverse of a two-phase solution of
    (R' U' F)^-1 solution^-1 (R' U' F)^-1; if that M would cancel into the R' U' F on either side, a move is put in
    front of it or behind it before solving, so that the scramble is written without cancelling moves."""
    w = cube.inv_seq(PAD) + cube.inv_seq(solution) + cube.inv_seq(PAD)
    A = [None, 'U', 'D', 'L', "U'", 'B', 'D2', "L'", 'U2', "D'"]; Z = [None, 'U', 'D', 'B', "U'", 'F', 'D2', "B'", 'U2', "D'"]
    for m1, m2 in sorted(((a, z) for a in A for z in Z), key=lambda p: A.index(p[0]) + Z.index(p[1])):
        t = _twophase(([m1] if m1 else []) + w + ([m2] if m2 else []))
        inner = (cube.inv_seq([m1]) if m1 else []) + cube.inv_seq(t) + (cube.inv_seq([m2]) if m2 else [])
        scr = PAD + inner + PAD
        if len(cube.cancel(scr)) == len(scr): break
    else: raise RuntimeError('no clean scramble')
    assert cube.do(cube.SOLVED, scr + list(solution)) == cube.SOLVED
    return scr
def best(scramble, skeleton, caps='8,10', mixed=False):
    out = subprocess.run([BIN, 'best', ' '.join(scramble), ' '.join(skeleton), '--L', caps] + (['--mixed'] if mixed else []), capture_output=True, text=True).stdout
    return parse_best(out)
def parse_best(out):
    res = {'type': None, 'sols': {}, 'best': {}, 'none': set(), 'parity': 'a parity leftover' in out}
    m = re.search(r'^leftover: ([^|]+) \| ([^|]*) \| (\S+)', out, flags=re.M)
    if m: res['type'] = m.group(1).strip(); res['pieces'] = m.group(2).strip(); res['left'] = m.group(3)
    m = re.search(r'^skeleton: (.*) \((\d+)\)', out, flags=re.M)
    if m: res['skeleton'] = m.group(1).split()
    for line in out.split('\n'):
        if line.startswith('SOL\t'):
            _, case, L, model, cost, length, nested, insd, final = line.split('\t')
            steps = []
            for part in insd.split('|'):
                pos, alg, canc = part.split(':'); steps.append((int(pos), alg.split(), int(canc)))
            res['sols'].setdefault(int(L), {})[model] = {'cost': int(cost), 'length': int(length), 'nested': nested == '1', 'steps': steps, 'final': final.split()}
        m = re.match(r'L=(\d+) best: cost (-?\d+), length (\d+) \((\w[\w-]*)\)', line)
        if m: res['best'][int(m.group(1))] = (m.group(4), int(m.group(2)), int(m.group(3)))
        m = re.match(r'L=(\d+) ([\w-]+): no solution within the bound', line)
        if m: res['none'].add((int(m.group(1)), m.group(2)))
    return res
# ---- what is left, in words
def cycles(perm):
    seen = set(); out = []
    for i in range(len(perm)):
        if i in seen or perm[i] == i: continue
        c = [i]; seen.add(i); j = perm[i]
        while j != i: c.append(j); seen.add(j); j = perm[j]
        out.append(c)
    return out
def left_text(s):
    """`A → B` : the piece now at A belongs at B.  Pieces that sit in place but turned are named with the turn."""
    cp, ct, ep, ef = cubie.cubie(s); parts = []
    for perm, tw, names, kind in ((cp, ct, cubie.CNAMES, 'c'), (ep, ef, cubie.ENAMES, 'e')):
        for c in cycles(perm):
            parts.append((' ↔ ' if len(c) == 2 else ' → ').join(names[i] for i in c) + ('' if len(c) == 2 else ' → ' + names[c[0]]))
        for i in range(len(perm)):
            if perm[i] == i and tw[i]:
                parts.append(names[i] + (' flipped' if kind == 'e' else ' twisted clockwise' if tw[i] == 1 else ' twisted counter-clockwise'))
    return ', '.join(parts)
def type_of(s):
    """The leftover type by the Python rule of leftover_types.py (cycle lengths with their twist sums)."""
    import leftover_types as lt
    cp, ct, ep, ef = cubie.cubie(s)
    c_un = any(cp[i] != i or ct[i] for i in range(8)); e_un = any(ep[i] != i or ef[i] for i in range(12))
    if c_un and e_un: return 'corners and edges'
    if not c_un and not e_un: return 'solved'
    # leftover_types works with "piece perm[i] sits at place i", which is what cubie gives
    return lt.name(lt.ctype((tuple(cp), tuple(ct)), 3), 'corner') if c_un else lt.name(lt.ctype((tuple(ep), tuple(ef)), 2), 'edge')
def axes_oriented(s):
    """On how many of the three axes (F/B, R/L, U/D) every edge of the state is oriented."""
    rots = list(cubie.rotations()); k = 0
    for rm in (tuple(range(54)), next(r for r, nm in rots if nm == 'y'), next(r for r, nm in rots if nm == 'x')):
        cp, ct, ep, ef = cubie.cubie(cubie.conj(s, rm)); k += not any(ef)
    return k
# ---- a solution written the usual way
MARKS = ['*', '^', '#']
def with_marks(seq, marks):
    """seq: list of moves; marks: {position: mark}."""
    out = []
    for i in range(len(seq) + 1):
        if i in marks: out.append(marks[i])
        if i < len(seq): out.append(seq[i])
    return ' '.join(out)
def block(skeleton, sol):
    """Lines for a solution.  Two insertions are written on one skeleton line when both sit in the original skeleton
    and the result is the same; otherwise the second mark is written in the skeleton as it stands after the first."""
    S = list(skeleton); steps = sol['steps']; lines = []
    p1, a1, c1 = steps[0]; S1 = cube.cancel(S[:p1] + a1 + S[p1:])
    if len(steps) == 1:
        lines.append(with_marks(S, {p1: '*'}))
        lines.append(f"* = {' '.join(a1)} // ({len(a1)}-{c1}/{len(S1)})")
        cur = S1
    else:
        p2, a2, c2 = steps[1]; S2 = cube.cancel(S1[:p2] + a2 + S1[p2:]); n = len(S)
        pre = 0
        while pre < min(len(S), len(S1)) and S[pre] == S1[pre] and pre < p1: pre += 1
        suf = 0
        while suf < min(len(S), len(S1)) and S[-1 - suf] == S1[-1 - suf] and suf < n - p1: suf += 1
        q2 = p2 if p2 < pre else (n - (len(S1) - p2)) if len(S1) - p2 < suf else None
        one_line = False
        if q2 is not None and q2 != p1:
            a, b = sorted([(p1, a1), (q2, a2)], key=lambda x: x[0])
            if cube.cancel(S[:a[0]] + a[1] + S[a[0]:b[0]] + b[1] + S[b[0]:]) == S2: one_line = True
        if one_line:
            lines.append(with_marks(S, {p1: '*', q2: '^'}))
            lines.append(f"* = {' '.join(a1)} // ({len(a1)}-{c1}/{len(S1)})")
            lines.append(f"^ = {' '.join(a2)} // ({len(a2)}-{c2}/{len(S2)})")
        else:
            lines.append(with_marks(S, {p1: '*'}))
            lines.append(f"* = {' '.join(a1)} // ({len(a1)}-{c1}/{len(S1)})")
            lines.append(with_marks(S1, {p2: '^'}))
            lines.append(f"^ = {' '.join(a2)} // ({len(a2)}-{c2}/{len(S2)})")
        cur = S2
    assert cur == sol['final'], (cur, sol['final'])
    lines.append(f"Solution: {' '.join(cur)} ({len(cur)})")
    return lines
def check_block(lines, scramble, skeleton):
    """Replay a block: every skeleton line must be the sequence as it stands, every `mark = alg // (a-b/len)` must
    cancel b and give len, and the Solution line must be the result, with its length, and solve the scramble.
    Returns (number of mismatches, final length)."""
    bad = 0; text = None; cur = cube.cancel(list(skeleton)); fin = None
    strip = lambda t: cube.parse(re.sub(r'[*^#]', ' ', t).replace(' ', '')) if re.sub(r'[*^# ]', '', t) else []
    for ln in lines:
        ln = ln.strip()
        m = re.match(r'^([*^#]) = (.+?) // \((\d+)-(\d+)/(\d+)\)$', ln)
        if m:
            mark, alg, a, b, tot = m.group(1), cube.parse(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
            if text is None or mark not in text: bad += 1; continue
            before = cube.cancel(strip(text)); text = text.replace(mark, ' ' + ' '.join(alg) + ' ', 1); after = cube.cancel(strip(text))
            if len(alg) != a or len(before) + len(alg) - len(after) != b or len(after) != tot or cube.cancel(alg) != alg: bad += 1
            cur = after
        elif ln.startswith('Solution: '):
            m = re.match(r'^Solution: (.+) \((\d+)\)$', ln); seq = cube.parse(m.group(1)); fin = len(seq)
            if seq != cur or len(seq) != int(m.group(2)) or cube.do(cube.SOLVED, list(scramble) + seq) != cube.SOLVED: bad += 1
        elif ln:
            if strip(ln) != cur: bad += 1                      # a skeleton line: the sequence as it stands, with marks
            text = ln
    if fin is None: bad += 1
    return bad, fin
