#!/usr/bin/env python3
"""Re-check every witness in out/witnesses.txt from its scramble text alone: `drtools read` (state built from the
moves, optimal from the depth files) for all of them, nissy's optimal DR finish for the ones named on the command line."""
import re, subprocess, sys
W = '/data/fmc/judging-a-dr/research/out/witnesses.txt'
READ = ['/data/fmc/judging-a-dr/research/drtools/target/release/drtools', 'read', '/data/fmc/judging-a-dr/research/data/drbfs', '/data/fmc/judging-a-dr/research/data/ls_depth.u8']
lines = open(W).read().split('\n')
wit = []
for i, l in enumerate(lines):
    m = re.match(r'^\s*(.+?) :: ([UDRLFB2\' ]*)$', l)
    if m and i + 1 < len(lines) and lines[i + 1].strip().startswith('subset'):
        d = lines[i + 1]
        wit.append((m.group(1).strip(), m.group(2).strip(), re.search(r'subset (\S+ \S+)', d).group(1), int(re.search(r'optimal (\d+)', d).group(1)),
                    tuple(map(int, re.search(r'HTR (\d+) / (\d+)', d).groups())), int(re.search(r'leave slice (\d+)', d).group(1))))
for l in lines:
    m = re.match(r'^216 case (.+?) :: .*DR moves (\d+) :: state ([UDRLFB2\' ]+) :: finish', l)
    if m: wit.append(('216 ' + m.group(1), m.group(3).strip(), None, int(m.group(2)), None, None))
out = subprocess.run(READ, input='\n'.join(w[1] if w[1] else "U U'" for w in wit) + '\n', capture_output=True, text=True).stdout.strip().split('\n\n')
assert len(out) == len(wit), (len(out), len(wit))
bad = 0
for w, block in zip(wit, out):
    kv = dict(x.split(': ', 1) for x in block.split('\n') if ': ' in x)
    ok = int(kv['optimal']) == w[3] and (w[2] is None or kv['subset'] == w[2]) and (w[4] is None or tuple(map(int, kv['htr'].split())) == w[4]) and (w[5] is None or int(kv['leave_slice']) == w[5])
    ok = ok and len(w[1].split()) == w[3]          # the scramble is itself as short as the optimal
    if not ok: bad += 1; print('MISMATCH', w, kv['subset'], kv['optimal'], kv['htr'])
print(f'{len(wit)} witnesses re-read from their scrambles, {bad} mismatches')
for pat in sys.argv[1:]:
    for w in wit:
        if re.search(pat, w[0]) and w[1]:
            r = subprocess.run(['nissy', 'solve', 'drudfin', '-o', w[1]], capture_output=True, text=True, timeout=900).stdout.strip().split('\n')[-1]
            n = int(re.search(r'\((\d+)\)', r).group(1))
            print(f'nissy {"OK " if n == w[3] else "DIFF"} {w[0]}: nissy {n}, table {w[3]}')
