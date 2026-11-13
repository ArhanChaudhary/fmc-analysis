#!/usr/bin/env python3
"""Writes HTFirst/Data.lean: what the Lean library HTFirst checks of the reference table "Half turns before the first
quarter turn" (tables/half-turns-before-first-qt.md).

  examples   the worked DRs of the page, from research/out/ht_first_witness.json (the file the page prints them from):
             scramble, optimal, subset x edges, every optimal finish with its printed counts, the corners' setup count
             and the quarter turns that lower the corners at once, on normal and on inverse.
  recount    the first N sampled DRs of one or more subset x edges (default: 200 of 2c4 2e), each as a scramble, with
             the study's numbers for that state: optimal, number of optimal finishes, fewest and most quarter turns
             among them, fewest half turns before the first quarter turn read from the first move and from the last
             (research/out/big/run1/states_<subset>.tsv: d, nopt, qmin, qmax, ht_first_n, ht_first_i, qtfull) and the
             same two counts over the optimal finishes with no extra quarter turn (research/out/big/htfirst/htfirst.tsv:
             hasmin, e0n, e0i).

A sampled state is stored by the study as three ranks (c, e, s).  Its scramble here is the inverse of one optimal
finish, found with research/src/check_ht_first.py's own move tables and the exact table; the scramble is replayed with
those move tables and must give back (c, e, s).  The finishes of an example are written in the order Lean lists them
(by move number, U U2 U' D D2 D' R2 L2 F2 B2), which need not be the page's order.

usage (from anywhere, env.sh sourced):  python3 gen_htfirst.py [N] [subset ...]      e.g.  gen_htfirst.py 200 2c4_2e"""
import os, sys, csv, json
HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.normpath(os.path.join(HERE, '..', '..', 'research'))
sys.path.insert(0, os.path.join(R, 'src'))
import check_ht_first as C          # move tables, depth() on the exact table, finishes(), lead(), trail()

N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
SUBS = sys.argv[2:] or ['2c4_2e']
NAMES = C.NAMES
IDX = {n: i for i, n in enumerate(NAMES)}
INV = {'U': "U'", "U'": 'U', 'D': "D'", "D'": 'D'}

def inv_seq(names): return [INV.get(m, m) for m in reversed(names)]
def replay(names):
    c = e = s = 0
    for m in names:
        k = IDX[m]; c, e, s = C.CML[k][c], C.EML[k][e], C.SML[k][s]
    return c, e, s
def q(s): return '"' + s + '"'

# ---------------------------------------------------------------- examples
wit = json.load(open(os.path.join(R, 'out', 'ht_first_witness.json')))
ex = []
for w in wit:
    scr = w['scramble'].split()
    c, e, s = (int(x) for x in w['state'].lstrip('#').split(','))
    assert replay(scr) == (c, e, s), w['id']
    fins = sorted(w['optimal_finishes'], key=lambda f: [IDX[m] for m in f['finish'].split()])
    assert len(fins) == w['n_optimal_finishes']
    fl = ', '.join(f"({q(f['finish'])}, {f['half_turns_before_first_qt_normal']}, {f['half_turns_before_first_qt_inverse']}, {f['quarter_turns']})"
                   for f in fins)
    row = w['sample'].split(' #')[0]
    ex.append(f"  {{ id := {q(w['id'])}, row := {q(row)}, scr := {q(w['scramble'])}, opt := {w['optimal']},\n"
              f"    fin := [{fl}],\n"
              f"    setupN := {w['corner_setup_sticker']['normal']}, setupI := {w['corner_setup_sticker']['inverse']}, "
              f"lowN := {len(w['qt_that_lowers_now']['normal'])}, lowI := {len(w['qt_that_lowers_now']['inverse'])}, "
              f"qtf := {w['fewest_quarter_turns_of_any_finish']}, "
              f"noExtra := {'true' if w['an_optimal_has_no_extra_quarter_turn'] else 'false'} }}")

# ---------------------------------------------------------------- recount
hf = {}
want = {s.replace('_', ' ') for s in SUBS}
with open(os.path.join(R, 'out', 'big', 'htfirst', 'htfirst.tsv')) as f:
    for r in csv.DictReader(f, delimiter='\t'):
        if r['subset'] in want and int(r['idx']) < N: hf[(r['subset'], int(r['idx']))] = r
rc = []
for sub in SUBS:
    name = sub.replace('_', ' ')
    rows = list(csv.DictReader(open(os.path.join(R, 'out', 'big', 'run1', f'states_{sub}.tsv')), delimiter='\t'))[:N]
    for r in rows:
        c, e, s = int(r['c']), int(r['e']), int(r['s']); d = C.depth(c, e, s)
        assert d == int(r['d'])
        fs = C.finishes(c, e, s, d)
        scr = inv_seq([NAMES[m] for m in fs[0]])
        assert replay(scr) == (c, e, s) and len(scr) == d
        h = hf[(name, int(r['idx']))]
        assert (int(h['c']), int(h['e']), int(h['s'])) == (c, e, s) and int(h['qtf']) == int(r['qtfull'])
        # the two files give the same count wherever an optimal finish has a quarter turn (the first writes the
        # optimal where none has one, the second 99; Lean follows the second)
        if h['noqt0'] == '0': assert (int(r['ht_first_n']), int(r['ht_first_i'])) == (int(h['a0n']), int(h['a0i']))
        vals = [int(r['d']), int(r['nopt']), int(r['qmin']), int(r['qmax']), int(h['a0n']), int(h['a0i']),
                int(r['qtfull']), int(h['hasmin']), int(h['e0n']), int(h['e0i'])]
        rc.append(f"  ({q(name + ' #' + r['idx'])}, {q(' '.join(scr))}, [{', '.join(str(v) for v in vals)}])")

out = f"""/-
  HTFirst.Data — GENERATED by `gen_htfirst.py`, do not edit.  Proved in `HTFirst.Examples`.

  `examples`: the worked DRs of tables/half-turns-before-first-qt.md (research/out/ht_first_witness.json).
  `recount`: the first {N} sampled DRs of {', '.join(sorted(want))} with the study's numbers for each state:
  [optimal, optimal finishes, fewest quarter turns among them, most, fewest half turns before the first quarter turn
  read from the first move, read from the last move, fewest quarter turns of any finish, 1 if some optimal finish has
  no extra quarter turn, and the two half-turn counts over those finishes (99 = none)].
-/

namespace HTFirst

/-- A worked DR of the page.  `fin`: (finish, half turns before its first quarter turn, half turns after its last,
quarter turns), every optimal finish, ordered by move number.  `setupN` / `setupI`: the half turns the corners need
before a quarter turn lowers them, on normal / on inverse.  `lowN` / `lowI`: how many of U U' D D' lower the corners
at once.  `qtf`: the fewest quarter turns of any finish.  `noExtra`: some optimal finish has exactly that many. -/
structure Ex where
  id : String
  row : String
  scr : String
  opt : Nat
  fin : List (String × Nat × Nat × Nat)
  setupN : Nat
  setupI : Nat
  lowN : Nat
  lowI : Nat
  qtf : Nat
  noExtra : Bool

def examples : List Ex := [
{(',' + chr(10)).join(ex)}]

/-- (sample, scramble, the study's numbers). -/
def recount : List (String × String × List Nat) := [
{(',' + chr(10)).join(rc)}]

end HTFirst
"""
open(os.path.join(HERE, 'HTFirst', 'Data.lean'), 'w').write(out)
print('wrote HTFirst/Data.lean:', len(ex), 'examples,', len(rc), 'recounted states')
