#!/usr/bin/env python3
"""Collect every DR state on the published pages that comes with a stated length, and write them as Lean data
(lean/DRBound/DRBound/PageData.lean) for DRBound.PageChecks to prove.  Reads the built pages, not the sources, so what
gets checked is what readers see.

  pageOptima   (where, scramble, stated optimal DR finish)
  pageHTR      (where, scramble, stated shortest HTR on normal, on inverse)
  pageSolves   (where, scramble, printed finish, its stated length)
  pageInHTR    (where, scramble, printed HTR): scramble + HTR lands in HTR
  pageLevels   (where, scramble, [HTR, L, L with parity, L+S+T, NISS@DR, + H-perm parity] on normal and on inverse)

Usage: python3 research/src/gen_page_checks.py   (from the study directory or anywhere)"""
import re, sys
S = '/data/fmc/judging-a-dr/'
W = open(S + 'report/WRITEUP.md').read().split('\n')
DRMOVE = re.compile(r"^(?:[UD]['2]?|[RLFB]2)$")
def dr(seq):
    t = seq.split()
    assert t and all(DRMOVE.match(x) for x in t), seq
    return ' '.join(t)
def line_of(text):
    hits = [i + 1 for i, l in enumerate(W) if text in l]
    assert hits, text
    return hits[0]

optima, htr, solves, inhtr, levels = [], [], [], [], []

# ---- tables: find the header, then map columns
def tables():
    i = 0
    while i < len(W):
        if W[i].startswith('|') and i + 1 < len(W) and re.match(r'^\|[-:| ]+\|$', W[i + 1]):
            head = [c.strip() for c in W[i].strip('|').split('|')]
            rows = []; j = i + 2
            while j < len(W) and W[j].startswith('|'):
                rows.append((j + 1, [c.strip() for c in W[j].strip('|').split('|')])); j += 1
            yield i + 1, head, rows; i = j
        else:
            i += 1
def tick(c):
    m = re.fullmatch(r'`([^`]*)`', c); return m.group(1) if m else None
def sec(n):
    h = next(W[k] for k in range(n - 1, -1, -1) if W[k].startswith('## ') or W[k].startswith('### '))
    return 'WRITEUP.md, ' + h.lstrip('#').strip()
for n, head, rows in tables():
    if head[:3] == ['Bad corners', 'A typical DR', 'Its optimal, moves'] or head[:3] == ['Case', 'A typical DR', 'Its optimal, moves']:
        for ln, r in rows:
            optima.append((f'{sec(ln)}: typical DR of {r[0]}', dr(tick(r[1])), int(r[2])))
    elif head[:3] == ['Subset', 'A longest one', 'Its optimal, moves']:
        for ln, r in rows:
            optima.append((f'{sec(ln)}: longest {r[0]}', dr(tick(r[1])), int(r[2])))
            optima.append((f'{sec(ln)}: {r[0]} finishing in its longer HTR', dr(tick(r[3])), int(r[6])))
            htr.append((f'{sec(ln)}: {r[0]} finishing in its longer HTR', dr(tick(r[3])), int(r[4]), int(r[5])))
            assert int(r[6]) == max(int(r[4]), int(r[5])), r
    elif head == ['Corner qt', 'Shortest HTR', 'A state with exactly that on both sides']:
        for ln, r in rows:
            htr.append((f'{sec(ln)}: shortest HTR at {r[0]}qt', dr(tick(r[2])), int(r[1]), int(r[1])))
    elif head[:5] == ['Subset', 'Scramble', 'Setup + HTR bound', 'Optimal finish', 'Its length']:
        for ln, r in rows:
            s, f = dr(tick(r[1])), dr(tick(r[3]))
            assert len(f.split()) == int(r[4]) and sum(1 for x in f.split() if not x.endswith('2')) == int(r[5]), r
            optima.append((f'{sec(ln)}: setup + HTR beaten in {r[0]}', s, int(r[4])))
            solves.append((f'{sec(ln)}: setup + HTR beaten in {r[0]}', s, f, int(r[4])))

# ---- the code-block examples, by hand (each with the line it is on)
def ex(text): return line_of(text)
for scr, n in [("U2 L2 D' F2 U' R2 U F2 D L2 U2", 11), ("U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2", 13),
               ("U B2 U' F2 U B2 D2 L2 U' R2 U R2 U' L2 U2", 15),
               ("D' U2 F2 U2", 4), ("U R2 D U'", 4), ("B2 F2 D' U L2 R2 D U'", 8),
               ("D2 B2 U' R2 D R2 B2 R2 F2 U2 R2 D F2 U R2 U'", 16),
               ("U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2", 13), ("U R2 L2 F2 U' B2 D2 F2 D L2 U B2 R2 U' F2 U", 13)]:
    optima.append((f'{sec(ex(scr))}', dr(scr), n))
optima.append((f"{sec(ex(chr(39).join(['D', ' L2 D R2 B2 F2 U2 B2 R2 U L2 U', '       // optimal 12'])))}", "D' L2 D R2 B2 F2 U2 B2 R2 U L2 U'", 12))
optima.append((f"{sec(ex(chr(39).join(['D', ' L2 D R2 B2 F2 U2 B2 R2 U L2 U', ' L2    // the same DR'])))}", "D' L2 D R2 B2 F2 U2 B2 R2 U L2 U' L2", 11))
# 4c3 4e that is 9 to HTR on both sides and finishes in 9
s = "U' L2 D' B2 U' B2 U L2 D"; ln = ex(s)
optima.append((f'{sec(ln)}', s, 9)); htr.append((f'{sec(ln)}', s, 9, 9))
solves.append((f'{sec(ln + 1)}', s, "D' L2 U' B2 U B2 D L2 U", 9))
# Levi section: 4a1 4e whose shortest HTR is 3qt on both sides
s = "U L2 R2 U R2 B2 U L2"; ln = ex(s)
htr.append((f'{sec(ln)}', s, 7, 7)); optima.append((f'{sec(ln)}', s, 8))
inhtr.append((f'{sec(ln + 1)}', s, "U L2 F2 L2 U B2 U"))
inhtr.append((f'{sec(ln + 2)}', s, "R2 F2 U2 R2 F2 U2 L2 D"))
solves.append((f'{sec(ln + 3)}', s, "L2 U' B2 R2 U' R2 L2 U'", 8))
# section 10: the two cases that get shorter with quarter turns
for a, b in [("L2 B2 D B2 L2 R2 F2 U'", "U F2 R2 L2 B2 D' B2 L2"), ("B2 L2 D L2 B2 F2 R2 U'", "U R2 F2 B2 L2 D' L2 B2")]:
    solves.append((f'{sec(ex(b))}', a, b, 8))
# section 4 (the data): qt counts of the finish, with a printed finish for each; section 13: a DR-breaking example's DR-move optimum
for a, b, n in [("D F2 R2 F2 D", "D' F2 R2 F2 D'", 5), ("D F2 U' B2 F2 D'", "D F2 B2 U F2 D'", 6), ("U L2 R2 U L2 R2 U'", "U R2 L2 U' R2 L2 U'", 7)]:
    solves.append((f'{sec(ex(a + " "))}', a, b, n))
s = "B2 L2 R2 F2 R2 U2 L2 R2 U2 R2 U2"; optima.append((f'{sec(ex(s))}', s, 11))
# the seven levels on the docs' examples: HTR, L, L with parity, L+S+T, NISS@DR, + H-perm parity (normal, inverse)
levels.append((f"{sec(ex('    HTR length          9 / 7'))}, Rodney's first random scramble",
               "U D L2 D' B2 U R2 F2 B2 D2 L2 D' R2 L2 D2 B2", [(9, 7), (5, 5), (7, 7), (10, 9), (10, 11), (11, 12)]))
levels.append((f"{sec(ex('    HTR 11 / 10,  L 11 / 11'))}, Rodney's 4a4 example",
               "U R2 L2 F2 U' B2 D2 F2 D L2 U B2 R2 U' F2 U", [(11, 10), (11, 11), None, (13, 11), (13, 12), None]))
# section 6.5: corner length and the parity read
levels.append((f"{sec(ex('U B2 U' + chr(39) + ' F2 U B2 D2 L2'))}, 2c4 4e odd E-slice",
               "U B2 U' F2 U B2 D2 L2 U' R2 U R2 U' L2 U2", [None, (12, 12), (13, 13), None, None, None]))

# section 5 (errata B4): the two 2c4 4e with the same reads, 7 to HTR and corner length 7 on both sides
for a in ("D F2 U' F2 D B2 D'", "D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'"):
    levels.append((f'{sec(ex(a + " "))}, the pair behind Zagros\'s first hunch', a, [(7, 7), (7, 7), None, None, None, None]))
optima.append((f"{sec(ex('D F2 U' + chr(39) + ' F2 D B2 D' + chr(39) + ' '))}", "D F2 U' F2 D B2 D'", 7))
optima.append((f"{sec(ex('D' + chr(39) + ' R2 B2 U' + chr(39) + ' F2 D B2 U B2 F2 U' + chr(39) + ' F2 U' + chr(39) + ' L2 D' + chr(39) + ' U' + chr(39) + ' '))}", "D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'", 16))

def lean_str(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
def opt(x): return 'none' if x is None else f'some ({x[0]}, {x[1]})'
out = ['/-', '  DRBound.PageData — every DR state on the published pages of judging-a-dr that comes with a stated length,',
       '  generated by research/src/gen_page_checks.py from report/WRITEUP.md.  Proved in DRBound.PageChecks.', '-/', '',
       'namespace DRBound.Page', '',
       '/-- (where, scramble, stated optimal DR finish). -/',
       'def pageOptima : List (String × String × Nat) := [']
out += [f'  ({lean_str(w)}, {lean_str(s)}, {n}),' for w, s, n in optima]; out[-1] = out[-1].rstrip(',') + ']'
out += ['', '/-- (where, scramble, stated shortest HTR on normal, on inverse). -/', 'def pageHTR : List (String × String × Nat × Nat) := [']
out += [f'  ({lean_str(w)}, {lean_str(s)}, {a}, {b}),' for w, s, a, b in htr]; out[-1] = out[-1].rstrip(',') + ']'
out += ['', '/-- (where, scramble, printed finish, its stated length). -/', 'def pageSolves : List (String × String × String × Nat) := [']
out += [f'  ({lean_str(w)}, {lean_str(s)}, {lean_str(f)}, {n}),' for w, s, f, n in solves]; out[-1] = out[-1].rstrip(',') + ']'
out += ['', '/-- (where, scramble, printed HTR): scramble then HTR is an HTR state. -/', 'def pageInHTR : List (String × String × String) := [']
out += [f'  ({lean_str(w)}, {lean_str(s)}, {lean_str(f)}),' for w, s, f in inhtr]; out[-1] = out[-1].rstrip(',') + ']'
out += ['', '/-- (where, scramble, stated levels on (normal, inverse): HTR, L, L with parity, L+S+T, NISS@DR, NISS@DR + H-perm parity;',
        '`none` where the page states nothing). -/', 'def pageLevels : List (String × String × List (Option (Nat × Nat))) := [']
out += [f'  ({lean_str(w)}, {lean_str(s)}, [{", ".join(opt(x) for x in L)}]),' for w, s, L in levels]; out[-1] = out[-1].rstrip(',') + ']'
out += ['', 'end DRBound.Page', '']
open(S + 'lean/DRBound/DRBound/PageData.lean', 'w').write('\n'.join(out))
print(f'optima {len(optima)}, HTR {len(htr)}, finishes {len(solves)}, in-HTR {len(inhtr)}, levels {len(levels)}', file=sys.stderr)
