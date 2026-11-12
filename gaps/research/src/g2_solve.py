#!/usr/bin/env python3
"""Gap 2: the true optimum (any of the 18 face turns) of DR states, against the DR-group optimum.

Input TSV: tag, id, c, e, s, d (DR-group optimum, judging-a-dr's exact table) [, more columns kept].
For each state: htrtools `trace` gives an optimal DR finish F (U/D axis); the scramble X = F^-1 reaches the state from
solved.  nissy 2.0.8 `solve optimal -M d-1 -n 1` (exact IDA* with its 3 GB nxopt31 table, one session for all
states) finds the shortest solution of at most d - 1 moves if there is one; if none, the true optimum is d (F is a
solution of d moves).  So true optimum = len(nissy's solution) or d.
Output TSV: input columns + scramble, true_opt, shorter solution (or "-").
usage: g2_solve.py <in.tsv> <out.tsv> [threads]   (run where nissy's tables fit; source /data/fmc/env.sh)"""
import sys, subprocess, json, re, time
HT = '/data/fmc/htr-routes/research/htrtools/target/release/htrtools'
EX = '/data/fmc/judging-a-dr/research/data/lean_exact_table.u8'
INV = {'': "'", "'": '', '2': '2'}

def invert(seq):
    return ' '.join(m[0] + INV[m[1:]] for m in reversed(seq.split()))

def main():
    inp, outp = sys.argv[1], sys.argv[2]; T = sys.argv[3] if len(sys.argv) > 3 else '8'
    rows = [l.rstrip('\n').split('\t') for l in open(inp) if l.strip() and not l.startswith('#')]
    tr = subprocess.run([HT, 'trace', EX, '1'], input=''.join(f'#{r[2]},{r[3]},{r[4]}\n' for r in rows),
                        capture_output=True, text=True, check=True).stdout.strip().split('\n')
    scr = []
    for r, t in zip(rows, tr):
        j = json.loads(t)
        assert j['d'] == int(r[5]), (r, j['d'])
        scr.append(invert(j['all'][0]) if j['d'] > 0 else '')
    cmds = []
    for r, s in zip(rows, scr):
        d = int(r[5])
        if d >= 1:
            cmds.append(f'solve optimal -M {d - 1} -n 1 -t {T} {s}')
        cmds.append('invert R')
    cmds.append('quit')
    t0 = time.time()
    out = subprocess.run(['nissy'], input='\n'.join(cmds) + '\n', capture_output=True, text=True).stdout
    body = out                                  # the welcome lines go to stderr
    chunks = body.replace('nissy-# ', '\n').split("\nR'\n")
    res = []
    for ch in chunks[:len(rows)]:
        m = re.search(r"^([URFDLB][2']?(?: [URFDLB][2']?)*) \((\d+)\)$", ch.strip(), re.M)
        res.append((m.group(1), int(m.group(2))) if m else None)
    assert len(res) == len(rows), (len(res), len(rows))
    with open(outp, 'w') as f:
        for r, s, x in zip(rows, scr, res):
            d = int(r[5])
            if x: assert x[1] < d
            f.write('\t'.join(r + [s, str(x[1] if x else d), x[0] if x else '-']) + '\n')
    print(f'{len(rows)} states, nissy {time.time() - t0:.0f}s, shorter than DR optimum: {sum(x is not None for x in res)}', flush=True)

if __name__ == '__main__':
    main()
