#!/usr/bin/env python3
"""Gap 2 examples: every optimal solution (any face turns) of a few DR states where a non-DR finish beats the DR
optimum, listed by nissy and replayed on is-dr-xs-worth-it's sticker model (research/src/cube.py).

  g2_examples.py pick N            -> big/g2/examples_in.tsv: N states from big/g2/uni1000.out with true < DR optimum,
                                      spread over subsets and gains (deterministic)
  g2_examples.py list              (on the machine with nissy's tables) -> big/g2/examples_nissy.txt:
                                      `solve optimal -o -a -n 10000` for each: every optimal solution
  g2_examples.py replay            -> out/g2_examples.json: per state the scramble (a DR-move sequence reaching it),
                                      DR optimum, true optimum, every listed solution with: replays to solved on
                                      cube.py, leaves the DR group (a quarter turn of R/L/F/B), its moves; and one
                                      DR-optimal finish replayed too"""
import sys, json, re, subprocess, collections
G = '/data/fmc/gaps/research'
sys.path.insert(0, '/data/fmc/is-dr-xs-worth-it/research/src')

def pick(n):
    rows = [l.rstrip('\n').split('\t') for l in open(f'{G}/big/g2/uni1000.out')]
    sh = [r for r in rows if int(r[9]) < int(r[5])]
    by = collections.defaultdict(list)
    for r in sh: by[r[0].split()[0]].append(r)
    out = []
    # biggest gain first, then one per corner subset
    out.append(max(sh, key=lambda r: (int(r[5]) - int(r[9]), -int(r[9]))))
    for g in sorted(by):
        if len(out) >= n: break
        r = by[g][0]
        if r not in out: out.append(r)
    with open(f'{G}/big/g2/examples_in.tsv', 'w') as f:
        for r in out[:n]: f.write('\t'.join(r) + '\n')
    print(len(out[:n]))

def lst():
    rows = [l.rstrip('\n').split('\t') for l in open(f'{G}/big/g2/examples_in.tsv')]
    cmds = []
    for r in rows: cmds += [f'solve optimal -o -a -n 10000 -t 8 {r[8]}', 'invert R']
    out = subprocess.run(['nissy'], input='\n'.join(cmds + ['quit']) + '\n', capture_output=True, text=True).stdout
    open(f'{G}/big/g2/examples_nissy.txt', 'w').write(out)

def replay():
    import cube
    rows = [l.rstrip('\n').split('\t') for l in open(f'{G}/big/g2/examples_in.tsv')]
    chunks = open(f'{G}/big/g2/examples_nissy.txt').read().replace('nissy-# ', '\n').split("\nR'\n")
    HT = '/data/fmc/gaps/research/src/htrreal/target/release/htrtools'
    tr = subprocess.run(['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=4G', HT, 'trace',
                         '/data/fmc/judging-a-dr/research/data/lean_exact_table.u8', '1'],
                        input=''.join(f'#{r[2]},{r[3]},{r[4]}\n' for r in rows), capture_output=True, text=True).stdout.strip().split('\n')
    res = []; bad = 0
    for r, ch, t in zip(rows, chunks, tr):
        sols = re.findall(r"^([URFDLB][2']?(?: [URFDLB][2']?)*) \((\d+)\)$", ch, re.M)
        start = cube.do(cube.SOLVED, r[8])
        drfin = json.loads(t)['all'][0]
        ok_dr = cube.do(start, drfin) == cube.SOLVED and len(drfin.split()) == int(r[5])
        S = []
        for s, L in sols:
            mv = s.split()
            ok = cube.do(start, s) == cube.SOLVED and len(mv) == int(L) == int(r[9])
            nondr = any(m[0] in 'RLFB' and not m.endswith('2') for m in mv)
            bad += (not ok) or (not nondr)
            S.append({'moves': s, 'length': int(L), 'replayed_ok': ok, 'breaks_dr': nondr})
        bad += (not ok_dr) or not sols
        res.append({'subset': r[0], 'scramble_reaching_state': r[8], 'dr_optimum': int(r[5]), 'leave_slice_optimum': int(r[6]),
                    'true_optimum': int(r[9]), 'dr_optimal_finish': drfin, 'dr_finish_replayed_ok': ok_dr,
                    'n_optimal_solutions': len(S), 'solutions': S})
    json.dump({'failures': bad, 'examples': res}, open(f'{G}/out/g2_examples.json', 'w'), indent=1)
    print('examples', len(res), 'solutions', sum(len(x['solutions']) for x in res), 'failures', bad)

if __name__ == '__main__':
    {'pick': lambda: pick(int(sys.argv[2])), 'list': lst, 'replay': replay}[sys.argv[1]]()
