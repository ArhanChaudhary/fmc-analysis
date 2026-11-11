#!/usr/bin/env python3
"""Writes DRXs/PyMoves.lean: the 18 face-turn permutations exactly as research/src/cube.py builds them.

The Lean project builds its own permutations from geometry (DRXs/Cube.lean) and does not need this file to do so;
PyMoves.lean is only the other side of the theorem `moves_agree_with_python` (DRXs/Theorems.lean), which says the
two constructions give the same 18 lists of 54 numbers.

Run from this directory:   /data/fmc/venv/bin/python gen_moves.py      (any Python 3; cube.py needs no packages)"""
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', '..', 'research', 'src'))
import cube

NAMES = [f + s for f in 'UDRLFB' for s in ('', '2', "'")]
lines = ['/-',
         '  DRXs.PyMoves — GENERATED, do not edit.  Made by `gen_moves.py` in the project directory, which imports',
         '  research/src/cube.py and prints `cube.MOVES[name]` for the 18 face turns:',
         '      /data/fmc/venv/bin/python gen_moves.py',
         '  Used only by the theorem `moves_agree_with_python`; nothing else in the project reads these numbers.',
         '-/',
         '',
         'namespace DRXs',
         '',
         '/-- `[(name, cube.MOVES[name]) for name in NAMES]` as printed by Python. -/',
         'def PY_MOVES : List (String × Array Nat) := [']
for k, name in enumerate(NAMES):
    m = cube.MOVES[name]
    assert sorted(m) == list(range(54))
    lines.append(f'  ("{name}", #[{", ".join(map(str, m))}])' + (',' if k < len(NAMES) - 1 else ''))
lines += [']', '', 'end DRXs', '']
out = os.path.join(here, 'DRXs', 'PyMoves.lean')
open(out, 'w').write('\n'.join(lines))
print('wrote', out)
