#!/usr/bin/env python3
"""Run the checks again and record what they print.

  checks.py            the data: the tool's self-tests, the brute-force comparisons, every printed solution replayed
                       (out/checks.txt; about ten minutes, most of it replaying the sample files in Python)
  checks.py --report   the reports: the witness blocks, the examples page and the quotations (out/checks_report.txt)
Both add their counts to out/checks.json, which the write-up quotes."""
import subprocess, json, glob, re, sys, os
O = '/data/fmc/insertion-cost/research/out/'; S = '/data/fmc/insertion-cost/research/src/'
BIN = '/data/fmc/insertion-cost/research/instools/target/release/instools'; PY = '/data/fmc/venv/bin/python'
log = []
def run(cmd, cwd=S):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    out = (r.stdout + r.stderr).strip(); log.append('$ ' + ' '.join(c.replace(O, 'out/').replace(BIN, 'instools').replace(PY, 'python') for c in cmd) + '\n' + out + '\n')
    assert r.returncode == 0, (cmd, out[-2000:])
    return out
REPORT = '--report' in sys.argv
J = json.load(open(O + 'checks.json')) if os.path.exists(O + 'checks.json') else {}
if not REPORT:
    run([BIN, 'selftest']); run([BIN, 'count'])
    run([BIN, 'bf1', '200', '1']); run([BIN, 'bf1', '200', '2', '--type', '3e'])
    for t in ('2tc', '3tc', '2c2c-pure', '2c2c-twisted', '3c1t', '5c', '3c3c', '2f', '2e2e', '2e2e-flipped', '5e', '3e1f', '3e3e'):
        run([BIN, 'bf2', t, '12', '300', '7', '8'])
    out = run([PY, 'check_solutions.py', 'sample'] + sorted(glob.glob(O + 'sample_*_n*.tsv')))
    J['sample_solutions'] = f"{int(re.search(r'total solutions replayed: (\d+)', out).group(1)):,}"
    log[-1] = '\n'.join(log[-1].split('\n')[:1] + ['...'] + log[-1].strip().split('\n')[-3:]) + '\n'
    out = run([PY, 'check_solutions.py', 'best', O + 'real_best.txt', O + 'if_best.txt'])
    J['real_solutions'] = f"{sum(int(x) for x in re.findall(r'real_best.txt: (\d+) printed solutions', out)):,}"
    J['if_solutions'] = f"{sum(int(x) for x in re.findall(r'if_best.txt: (\d+) printed solutions', out)):,}"
    n = sum(sum(1 for _ in open(p)) - 1 for p in glob.glob(O + 'onepos_3c_n*.tsv')); J['onepos'] = f'{n:,}'
    J['greedy_full'] = f"{sum(1 for _ in open(O + 'greedy_5c_n20_L8_full.tsv')) - 1:,}"
    open(O + 'checks.txt', 'w').write('\n'.join(log))
else:
    out = run([PY, 'witness.py', '--verify']); J['witness'] = out.strip().split('\n')[-1]
    out = run([PY, 'xexamples.py', '--verify']); J['examples'] = out.strip().split('\n')[-1]
    out = run([PY, 'report_build/check_quotes.py']); J['quotes'] = out.strip().split('\n')[-1]
    open(O + 'checks_report.txt', 'w').write('\n'.join(log))
json.dump(J, open(O + 'checks.json', 'w'), indent=1)
print(json.dumps(J, indent=1))
