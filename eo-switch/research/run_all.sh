#!/bin/bash
# Regenerate every number of study 6 (when to switch on an EO).  About 6 minutes on 4 cores; every heavy step capped
# with systemd-run (peak about 1 GB, plus 3.5 GB for mkscr if the scrambles are redrawn).  Needs is-dr-xs-worth-it's
# out/tables/ and eo-to-dr's eodrtools binary (mkscr) and out/big/{eo-fb_dr,all_dr}_eo0.u8 (comparison, any-turn table).
set -euo pipefail
source /data/fmc/env.sh
cd "$(dirname "$0")"
B=$PWD/eoswtools/target/release/eoswtools
CAP="systemd-run --user --scope -q -p MemoryMax=4G"
PY=/data/fmc/venv/bin/python3
mkdir -p out/big
step() { echo "== $1  ($(date +%H:%M:%S))"; }
step "build"
(cd eoswtools && cargo build --release 2>&1 | tail -1)
step "1. exact EO-kept DR distance (BFS), compared with eo-to-dr; R/L-axis completions; nissy on 1000 cosets"
$CAP $B dist out/big/d.u8 > out/dist_hist.txt
$CAP $B twoaxis out/big/d.u8 out/big/p_rl.u32
$B checkpos out/big/d.u8 1000 606 > out/big/checkpos.tsv
$CAP $PY src/check_nissy.py
step "2. features + unit tests (+ Rodney's string code on every coset)"
$CAP $PY src/features.py full
step "3. RZP weights (exact), uniform scrambles, sampled attempts"
$CAP $B rzp out/big/d.u8 out/big/rzp_w.u64
if [ ! -s out/scrambles.txt ]; then
  $CAP /data/fmc/eo-to-dr/research/eodrtools/target/release/eodrtools mkscr 6000 6006 > out/scrambles.txt
fi
$CAP $B att out/big/d.u8 out/scrambles.txt 0 6000 out/big/att 40
step "tables: variants, reproduction, populations, grades, search, Q4, NISS predictors, claims, witnesses, summary"
$PY src/step1.py
$PY src/reproduce.py
$PY src/populations.py > /dev/null
$PY src/grade.py > /dev/null
$CAP $PY src/search.py
$PY src/q4.py > /dev/null
$CAP $PY src/niss_checks.py 20000
$PY src/claims.py > /dev/null
$PY src/witness.py
$PY src/summary.py
step "the two-ring model: turn rules on every case, side turns, half turns to two bars, ring swaps; tables; normal-side reading"
$CAP $PY src/rings.py
$CAP $PY src/xrings.py
$CAP $PY src/xtrace_rings.py 20000
step "done"
