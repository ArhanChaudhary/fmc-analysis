#!/usr/bin/env python3
"""Replay a worked example as its author wrote it: put each algorithm at its mark, cancel after each step, and check
on the sticker model that the result solves the scramble.

  moves(txt)           a line of face turns, with commutator shorthand [A, B] and [A: B] written out; None if the line
                       has anything else (rotations, slices, wide moves, inverse-scramble brackets)
  author(example)      (ok, final sequence, [(algorithm length, moves cancelled) per step]) for an entry of
                       kb/reread/ins_examples.jsonl; ok is False when a mark or an algorithm cannot be read or the
                       result does not solve the scramble"""
import re
import cube
MOVE = re.compile(r"[UDRLFB][2']?")
def _norm(t): return t.replace('’', "'").replace('‘', "'").replace('`', "'").replace('′', "'")
def _split_top(s, seps):
    depth = 0
    for i, ch in enumerate(s):
        if ch == '[': depth += 1
        elif ch == ']': depth -= 1
        elif ch in seps and depth == 0: return s[:i], ch, s[i + 1:]
    return s, None, None
def moves(txt):
    """Face turns of a line; brackets are commutators [A, B] = A B A' B', conjugates [A: B] = A B A', or plain grouping."""
    t = _norm(txt).strip(); out = []; i = 0
    while i < len(t):
        ch = t[i]
        if ch.isspace(): i += 1; continue
        if ch == '[':
            depth = 0; j = i
            while j < len(t):
                if t[j] == '[': depth += 1
                elif t[j] == ']':
                    depth -= 1
                    if depth == 0: break
                j += 1
            if j >= len(t): return None
            a, sep, b = _split_top(t[i + 1:j], ',:')
            A = moves(a)
            if A is None: return None
            if sep is None: out += A
            else:
                B = moves(b)
                if B is None: return None
                out += A + B + cube.inv_seq(A) + (cube.inv_seq(B) if sep == ',' else [])
            i = j + 1; continue
        m = MOVE.match(t, i)
        if not m: return None
        nxt = t[m.end()] if m.end() < len(t) else ' '
        if not (nxt.isspace() or nxt == '['): return None            # things like Rw, R3, U2'
        out.append(m.group(0)); i = m.end()
    return out
def marks_of(r): return sorted({i['mark'] for i in r['insertions'] if i['mark'] not in ('', '[]')}, key=len, reverse=True)
def strip_marks(txt, marks):
    t = _norm(txt)
    for m in marks:
        for form in (f'[{m}]', f'({m})', m): t = t.replace(form, ' ')
    return re.sub(r"[^A-Za-z0-9'\[\],: ()]", ' ', t)              # any other mark-like character (emoji, @ # $ ...)
def skeleton_moves(r):
    """The skeleton of an example as plain face turns (marks taken out), or None."""
    return moves(strip_marks(r['skeleton'], marks_of(r)))
def author(r):
    marks = marks_of(r); cur = _norm(r['skeleton']); steps = []
    prev = moves(strip_marks(cur, marks))
    if prev is None or not r['insertions']: return False, None, []
    prev = cube.cancel(prev)
    for ins in r['insertions']:
        alg = _norm(ins['alg'] or ''); m = ins['mark']
        if 'placed_in' in ins: cur = _norm(ins['placed_in'])
        if m == '[]': return False, None, steps
        a = moves(strip_marks(alg, marks))
        if a is None or not a: return False, None, steps
        if m == '': cur = cur + ' ' + alg
        else:
            form = next((f for f in (f'[{m}]', f'({m})', m) if f in cur), None)
            if form is None: return False, None, steps
            cur = cur.replace(form, ' ' + alg + ' ', 1)
        now = moves(strip_marks(cur, marks))
        if now is None: return False, None, steps
        now = cube.cancel(now)
        steps.append((len(a), len(prev) + len(a) - len(now))); prev = now
    scr = moves(r['scramble'])
    ok = scr is not None and cube.do(cube.SOLVED, scr + prev) == cube.SOLVED
    return ok, prev, steps
if __name__ == '__main__':
    import json, collections
    assert moves("[R F2 R', B']") == cube.parse("R F2 R' B' R F2 R' B") and moves("[D R': [F2, R D' R' D]]") == cube.parse("D R' F2 R D' R' D F2 D' R D R' R D'")
    rows = [json.loads(l) for l in open('/data/fmc/kb/reread/ins_examples.jsonl')]; c = collections.Counter()
    for r in rows:
        if r['niss']: c['inverse-scramble parts'] += 1; continue
        if skeleton_moves(r) is None: c['skeleton not plain'] += 1; continue
        ok, fin, steps = author(r)
        if not r['insertions']: c['no insertion written'] += 1
        elif not ok: c['not replayable or does not solve'] += 1
        elif r['final_length'] is not None and len(fin) != r['final_length']: c['solves, length differs from the stated one'] += 1; print(' ', r['id'], len(fin), r['final_length'])
        else: c['replayed'] += 1
    print(dict(c))
