#!/usr/bin/env python3
"""Read every worked example collected from the server and its docs (kb/reread/drxs_examples.jsonl), follow the
solution line by line, and compare each line's label (DR-2s, 4a2-1s, 8fe, ...) with what the state is by the rules
of this study.  Slices from the signature (the rule trangium gives in his dr-fe examples doc):
  corners on the colour's own faces:  slice pieces agree with centers: 0 flips -> DR, else 2 slices; disagree -> 3
  corners on other faces:             slice pieces agree: 4 flips -> 1 slice, else 3; disagree -> 2"""
import json, re, sys, collections
import cube, fe
def slices(c, f, flips, bit):
    n = sum(flips)
    if c == f: return (0 if n == 0 else 2) if bit else 3
    return (1 if n == 4 else 3) if bit else 2
def kinds(s):
    out = []
    for c in range(3):
        for f in range(3):
            g = fe.look(s, c, f)
            if g and len(set(g[1])) == 1: out.append((slices(c, f, g[0], g[1][0]), sum(g[0]), c, f))
    return sorted(out)
def main():
    ex = [json.loads(l) for l in open('/data/fmc/kb/reread/drxs_examples.jsonl')]
    agree = collections.Counter(); bad = []
    for e in ex:
        try: S = cube.parse(e['scramble'])
        except AssertionError: continue
        N, I = [], []
        for l in e['lines']:
            if l.get('role') in ('prose', 'command', 'solver-output', 'final', 'insertion', 'table-row') or l.get('plain') is False: break
            mv = l['moves'].strip().strip('.').strip()
            try: seq = cube.parse(mv) if mv else []
            except AssertionError: break
            (I if l['inverse'] else N).extend(seq)
            lab = l.get('label') or ''
            m = re.search(r'-\s?([123])s\b', lab) or re.search(r'DR-([123])s', lab, re.I)
            want8 = '8fe' in lab or '8 fe' in lab
            if not m and not want8: continue
            if re.search(r'rzp|htr|HTR|setup|->|to dr|optimal|opt', lab): continue          # labels about a later or earlier state
            s = cube.do(cube.do(cube.do(cube.SOLVED, cube.inv_seq(I)), S), N)
            ks = kinds(s)
            ok = bool(ks) and (m is None or any(k[0] == int(m.group(1)) for k in ks)) and (not want8 or any(k[1] == 8 for k in ks))
            agree[ok] += 1
            if not ok: bad.append((e['id'], e['author'], lab, ' '.join(N), '(' + ' '.join(I) + ')', ks))
    print('labelled states checked:', sum(agree.values()), '| agree:', agree[True], '| differ:', agree[False])
    for b in bad: print('  ', b)

if __name__ == '__main__': main()
