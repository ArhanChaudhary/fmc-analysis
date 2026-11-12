#!/usr/bin/env python3
"""out/witness.json: one explicit DR state for every striking finding and every correction in SUMMARY.md.

Each entry: the finding, a scramble of DR moves that reaches the state (the inverse of one of its optimal
finishes), the subset, the optimal length, and a finish written out with the reading that shows the point
(which side first, the moves done on normal and on inverse, the route key).  Every entry is replayed here on the
independent sticker model (sticker.py): scramble + finish solves the cube, the length is what is claimed, and the
reading, re-simulated move by move with its own labels, gives the route key.  For "no optimal finish follows R"
witnesses, every optimal finish of the state (htrtools trace) is re-read on the sticker model and none follows R.

Input: out/witness_specs.json (written by summary.py: id, finding, subset, state "#c,e,s", route, max length,
kind 'follows' or 'none_optimal').  Output: out/witness.json"""
import json, os, subprocess, sys
from common import R, OUT
import sticker
from sticker import do, SOLVED, inv_seq
TOOL = os.environ.get('HTRTOOLS', f'{R}/htrtools/target/release/htrtools')
EXACT = '/data/fmc/judging-a-dr/research/data/lean_exact_table.u8'
CAP = ['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=5G']

def run(cmd, lines):
    p = subprocess.run(CAP + [TOOL, cmd, EXACT], input='\n'.join(lines) + '\n', capture_output=True, text=True, check=True)
    return [json.loads(l) for l in p.stdout.strip().split('\n')]

def nissy_htr(scr):
    env = dict(os.environ, NISSYDATA='/data/fmc/tools/nissy-data')
    p = subprocess.run(['/data/fmc/tools/nissy-2.0.8/nissy', 'solve', 'htr-drud', '-L', scr], capture_output=True, text=True, env=env)
    return p.stdout.strip().split('\n')[0]

def main():
    specs = json.load(open(f'{OUT}/witness_specs.json'))
    for s in specs:
        s.setdefault('route', ''); s.setdefault('maxlen', 0)
    ex = run('explain', [f"{s['state']}\t{s['route'] or 'none'}\t{s['maxlen']}" for s in specs])
    tr = run('trace', [s['state'] for s in specs])
    out = []; bad = 0
    for s, e, t in zip(specs, ex, tr):
        ent = dict(id=s['id'], finding=s['finding'], subset=s['subset'], kind=s['kind'], route=s['route'],
                   optimal=t['d'], n_optimal_finishes=t['nopt'])
        scr = ' '.join(inv_seq(t['all'][0])) if t['all'] else ''
        ent['scramble'] = scr
        ent['optimal_finish'] = t['all'][0] if t['all'] else ''
        X = do(SOLVED, scr)
        ok = do(X, ent['optimal_finish']) == SOLVED and len(ent['optimal_finish'].split()) == t['d']
        if s['kind'] in ('follows', 'none_optimal') and 'error' not in e:
            fin = e['finish'].split()
            k = len(e['normal_moves'].split()) if e['normal_moves'] else 0
            h, f, hl = sticker.reading(scr.split(), fin, k, e['first_side'] == 'inverse')
            ok &= do(X, e['finish']) == SOLVED
            ok &= s['route'] in (h, f)
            ent.update(finish=e['finish'], length=e['length'], first_side=e['first_side'], normal_moves=e['normal_moves'],
                       inverse_moves=e['inverse_moves'], htr_length=e['htr_len'])
            if s['kind'] == 'follows':
                ok &= e['length'] <= s['maxlen']
            else:
                ok &= e['length'] > t['d']
        elif s['kind'] in ('follows', 'none_optimal'):
            ent['finish'] = None
            ok &= s['kind'] != 'follows'
        if s['kind'] == 'optimal':
            ok &= t['d'] == s['value']
        if s['kind'] in ('min_htr', 'min_htr_at_most'):
            best = 99; bestf = None
            for fin in t['all'][:400]:
                mv = fin.split()
                for k in range(len(mv) + 1):
                    for invf in (False, True):
                        h, f, hl = sticker.reading(scr.split(), mv, k, invf)
                        if hl < best: best, bestf = hl, (fin, k, 'inverse' if invf else 'normal', h)
            ent['shortest_htr_in_any_reading_of_any_optimal'] = best
            ent['that_reading'] = dict(finish=bestf[0], split=bestf[1], first_side=bestf[2], route=bestf[3])
            ent['checked_optimal_finishes'] = min(len(t['all']), 400)
            ok &= (best >= s['value'] if s['kind'] == 'min_htr' else best <= s['value']) and len(t['all']) <= 400
        if s['kind'] == 'switch':
            rows = []
            for fin in t['all'][:400]:
                mv = fin.split(); n = len(mv)
                for k in range(n + 1):
                    for invf in (False, True):
                        h, f, hl = sticker.reading(scr.split(), mv, k, invf)
                        first = (n - k) if invf else k
                        rows.append((hl, '(' not in h, first, fin, k, 'inverse' if invf else 'normal', h))
            best = min(r[0] for r in rows)
            at = [r for r in rows if r[0] == best]
            ent['shortest_htr_in_any_reading_of_any_optimal'] = best
            ent['readings_with_it'] = [dict(finish=r[3], split=r[4], first_side=r[5], moves_before_switch=r[2], route=r[6]) for r in at[:4]]
            ok &= not any(r[1] for r in at) and min(r[2] for r in at) >= s['value'] and len(t['all']) <= 400
        if s['kind'] == 'variation':
            tv = run('trace', [scr + ' R2'])[0]
            ent['variation_scramble'] = scr + ' R2'
            ent['variation_optimal'] = tv['d']; ent['variation_finish'] = tv['all'][0]
            Xv = do(SOLVED, scr + ' R2')
            ok &= do(Xv, tv['all'][0]) == SOLVED and tv['d'] == t['d'] - 1
        if s['kind'] == 'htr_linear':
            line = nissy_htr(scr)
            sol = line.rsplit('(', 1)[0].strip() if line.endswith(')') else line
            n = int(line.rsplit('(', 1)[1].rstrip(')'))
            on_inv = sol.startswith('(')
            mv = sol.strip('()').split()
            st = do(SOLVED, ' '.join(inv_seq(scr)) if on_inv else scr)
            st = do(st, mv)
            ent['nissy_linear_htr'] = line
            ok &= sticker.in_htr(st) and n == s['value']
        if s['kind'] == 'none_optimal':
            hit = False
            for fin in t['all']:
                mv = fin.split()
                for k in range(len(mv) + 1):
                    for invf in (False, True):
                        h, f, _ = sticker.reading(scr.split(), mv, k, invf)
                        hit |= s['route'] in (h, f)
            ok &= not hit
            ent['checked_all_optimal_finishes'] = len(t['all'])
        ent['replayed_ok'] = bool(ok)
        bad += not ok
        out.append(ent)
    json.dump(out, open(f'{OUT}/witness.json', 'w'), indent=1)
    print(f'{len(out)} witnesses, {bad} failed replay')
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
