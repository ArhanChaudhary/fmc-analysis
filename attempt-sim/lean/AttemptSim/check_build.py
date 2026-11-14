#!/usr/bin/env python3
"""After `lake build AttemptSim AttemptSim.Audit` and `lake env lean AttemptSim/Audit.lean > audit.log`, in the project
folder: (1) the data files on disk are the ones the manifests describe (sha256 against data/MANIFEST.txt; Lake does not
track `include_str` files, the modules are rebuilt through the manifests' hashes, so this closes the loop); (2) the
axioms of every theorem: Lean's three standard axioms and one `native_decide` axiom per checked run, no `sorryAx`;
(3) no `sorry` in the sources.  Exit 1 on any failure.  Python 3, standard library only."""
import hashlib, os, re, sys

ok = True
rows = [l.split('\t') for l in open('data/MANIFEST.txt').read().split('\n')[1:] if l.strip() and '\t' in l]
n = 0
for r in rows:
    if len(r) == 5 and os.path.exists(os.path.join('data', r[0])):
        h = hashlib.sha256(open(os.path.join('data', r[0]), 'rb').read()).hexdigest()
        n += 1
        if h != r[3]:
            print(f'DATA MISMATCH {r[0]}: {h} on disk, {r[3]} in MANIFEST.txt'); ok = False
print(f'data files checked against MANIFEST.txt: {n}')

audit = open('audit.log').read()
thms = re.findall(r"'(\S+)' (depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", audit, re.S)
kinds = {}
for name, _, ax in thms:
    for a in [x.strip() for x in ax.replace('\n', ' ').split(',') if x.strip()]:
        k = '<native_decide>' if '_native' in a else a
        kinds.setdefault(k, set()).add(name)
print(f'theorems audited: {len(thms)}')
for k, v in sorted(kinds.items()):
    print(f'  {k}: {len(v)} theorems')
bad = set(kinds) - {'propext', 'Classical.choice', 'Quot.sound', '<native_decide>'}
if bad or 'sorryAx' in audit or len(thms) == 0:
    print('UNEXPECTED AXIOMS:', bad or 'sorryAx'); ok = False

hits = []
for d in ('AttemptSim', 'DRBound'):
    for f in sorted(os.listdir(d)):
        if f.endswith('.lean'):
            for i, l in enumerate(open(os.path.join(d, f)), 1):
                if re.search(r'\bsorry\b', l): hits.append(f'{d}/{f}:{i}: {l.strip()}')
print('sorry in sources:', 'none' if not hits else '\n  ' + '\n  '.join(hits))
ok = ok and not hits
print('CHECK', 'OK' if ok else 'FAILED')
sys.exit(0 if ok else 1)
