"""Write lean/ScrDiff/ScrDiff/Checks.lean from out/lean_claims.json:
each claim = a NISS DR: doing  inverse-side moves (as premoves), then the scramble, then the normal moves  on a solved
cube gives a DR state on the stated axis.  Checked on the sticker model copied from the eo-to-dr certificate."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
claims = json.load(open(os.path.join(HERE, '..', 'out', 'lean_claims.json')))
AXN = {'RL': 0, 'UD': 1, 'FB': 2}
out = ['import ScrDiff.Cube', '', 'namespace ScrDiff', 'open cube', '',
       '/-- axis of a face letter: 0 = R/L, 1 = U/D, 2 = F/B -/',
       'def axisOf (c : Char) : Nat := (AX c).1', '',
       '/-- DR on axis `a`: every sticker of an `a` colour is on an `a` face, and the four slice edges of axis `a`',
       '    (home coordinate 0 on `a`) keep their colours of the next axis on that axis\' faces.',
       '    This set has 8!·8!·4!/2 states and contains <U,D,R2,L2,F2,B2> (for a = U/D), so it is that group. -/',
       'def isDR (s : State) (a : Nat) : Bool :=',
       '  (List.range 54).all fun i =>',
       '    let h := s[i]!',
       '    let col := axisOf (FACE_OF[h]!)',
       '    let pl := axisOf (FACE_OF[i]!)',
       '    let b := (a + 1) % 3',
       '    (col != a || pl == a) && ((cube.ST[h]!).1[a]! != 0 || col != b || pl == b)', '',
       '-- sanity: solved is DR on every axis; DR moves keep it; a quarter turn of another axis breaks it',
       'theorem solved_dr : (isDR SOLVED 0 && isDR SOLVED 1 && isDR SOLVED 2) = true := by native_decide',
       'theorem dr_moves_ud : isDR (do_ SOLVED "U R2 F2 D\' L2 B2 U2 D") 1 = true := by native_decide',
       'theorem r_breaks_ud : isDR (do_ SOLVED "R") 1 = false := by native_decide',
       'theorem r_keeps_rl : isDR (do_ SOLVED "R U2 L\' F2") 0 = true := by native_decide', '']
for c in claims:
    if c.get('kind') == 'same':
        out.append(f"/-- {c['what']} -/")
        out.append(f"theorem {c['name']} : (do_ SOLVED \"{c['a']}\" == do_ SOLVED \"{c['b']}\") = true := by native_decide")
        out.append(f"theorem {c['name']}_not_solved : (do_ SOLVED \"{c['a']}\" == SOLVED) = false := by native_decide")
        out.append('')
        continue
    seq = ' '.join(x for x in (c['premoves'], c['scramble'], c['normal']) if x)
    out.append(f"/-- {c['what']} -/")
    out.append(f"theorem {c['name']} : isDR (do_ SOLVED \"{seq}\") {AXN[c['axis']]} = true := by native_decide")
    if c.get('not_before'):
        out.append(f"theorem {c['name']}_scramble_not_dr : isDR (do_ SOLVED \"{c['scramble']}\") {AXN[c['axis']]} = false := by native_decide")
    out.append('')
out.append('end ScrDiff')
open(os.path.join(HERE, '..', 'lean', 'ScrDiff', 'ScrDiff', 'Checks.lean'), 'w').write('\n'.join(out) + '\n')
print(len(claims), 'claims written')
