#!/bin/bash
# Regenerate every number of the eo-to-dr study.  About 50 minutes on 4 cores; peak memory about 3.5 GB (mkscr holds the 4-bit
# all_dr table and judging-a-dr's exact table; nissy's optimal solver), every heavy step capped with systemd-run.  Needs is-dr-xs-worth-it/research/out/tables/ and
# out/bfs/{all_dr,eo-fb_dr}.u8 (that study's run_bfs.sh makes them).
# The sample is deterministic (seeded); NISSY_SCRAMBLES=1 redraws the nissy scrambles used only in the uniformity check.
set -euo pipefail
source /data/fmc/env.sh
cd "$(dirname "$0")"
R=$PWD
B=$R/eodrtools/target/release/eodrtools
CAP="systemd-run --user --scope -q -p MemoryMax=5G"
mkdir -p out/big
step() { echo "== $1  ($(date +%H:%M:%S))"; }

step "build"
(cd eodrtools && cargo build --release 2>&1 | tail -1)
step "model self-test, sticker checks"
$B selftest
python3 src/sticker.py

step "50,000 uniformly random states written as scrambles (eodrtools mkscr, seed 2026)"
$CAP $B mkscr 50000 2026 > out/scrambles.txt
if [ "${NISSY_SCRAMBLES:-0}" = 1 ] || [ ! -s out/nissy_scrambles.txt ]; then
  step "50,000 nissy scrambles, only for the uniformity check (~10 min)"
  $CAP src/gen_scrambles.sh
fi
python3 src/check_scrambles.py mkscr=out/scrambles.txt nissy=out/nissy_scrambles.txt judging500=/data/fmc/judging-a-dr/research/out/hand/attempt_scrambles.txt
printf '%s\n' "U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2" > out/superflip.txt

step "EO-solved parts of the two DR tables"
$B extract /data/fmc/is-dr-xs-worth-it/research/out/bfs/eo-fb_dr.u8 out/big/eo-fb_dr_eo0.u8 > out/eo0_hist_eo-fb_dr.txt
$B extract /data/fmc/is-dr-xs-worth-it/research/out/bfs/all_dr.u8 out/big/all_dr_eo0.u8 > out/eo0_hist_all_dr.txt

step "checks: 4-bit packing; every table mapping against nissy (1000 positions each)"
$CAP $B check bits 1000000 9 | tee out/checks_bits.txt
$CAP python3 src/check_nissy.py 1000

step "B: EO tables (exact one axis, exact bad-edge layouts, 1,000,000 random states)"
$B eo axis > out/eo_axis.tsv
$CAP $B eo layouts > out/eo_layouts.tsv
$CAP $B eo sample 1000000 21 > out/eo_sample.tsv
python3 src/analyze_eo.py

step "C: EO -> DR (exact per coset, exact two axes, 10,000,000 sampled EO-solved states)"
$CAP $B eodr exact > out/eodr_exact.tsv
$CAP $B eodr twoaxis > out/eodr_twoaxis.tsv
$CAP $B eodr sample 10000000 31 > out/eodr_sample.tsv
python3 src/analyze_eodr.py

step "A: scramble -> EO -> DR on 50,000 scrambles (~30 min), the first study's 500, the superflip"
$CAP $B scr out/scrambles.txt 12 6 > out/big/scr50k.tsv 2> out/big/scr50k.log
$CAP $B scr /data/fmc/judging-a-dr/research/out/hand/attempt_scrambles.txt 12 6 > out/big/scr500.tsv 2> out/big/scr500.log
$CAP $B scr out/superflip.txt 11 6 > out/superflip_scr.tsv 2> /dev/null
python3 src/verify_scr.py out/big/scr50k.tsv out/scrambles.txt
python3 src/verify_scr.py out/big/scr500.tsv /data/fmc/judging-a-dr/research/out/hand/attempt_scrambles.txt
$CAP python3 src/check_counts.py out/big/scr50k.tsv 30
$CAP python3 src/check_niss_dr.py 40
python3 src/analyze_scr.py out/big/scr50k.tsv a50k
python3 src/analyze_scr.py out/big/scr500.tsv s500
python3 src/compare_prior.py

step "D: claims, witnesses, summary"
$CAP python3 src/optimal_check.py 3
$CAP python3 src/witness.py
python3 src/claims.py
python3 src/summary.py
step "done"
