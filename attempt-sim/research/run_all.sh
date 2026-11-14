#!/bin/bash
# Every run and table of the attempt-sim study, in order.  Runs here (memory-capped) by default; set REMOTE=fmc2 or
# REMOTE=fmc3 to send the heavy stages to that machine with remote_batch.sh (then rerun with FETCH=1 when the batches
# are done, to fetch and build the tables).  About 2.5 core-hours per 1,000,000 attempts; the whole study is about
# 3.2 million attempts (roughly 4 hours on 8 cores).
#
#   stage 0  build, self-test, real results from the WCA export (needs out/big/wca/WCA_export.tsv.zip)
#   stage 1  calibration: the baseline at several paces, forms and step-time spreads (cal*.toml)
#   stage 2  every policy of every experiment on the 4,000 training scrambles (all.toml)
#   stage 3  the recommended and representative policies on the 4,000 held-out scrambles and the official scrambles
#   stage 4  the length of the attempt: 20 to 120 minutes
#   stage 5  sensitivity: every time cost halved and doubled, and the human limits moved
#   stage 6  tables, write-up, Lean sample
set -euo pipefail
source /data/fmc/env.sh
cd "$(dirname "$0")"
STAGES=${STAGES:-0 1 2 3 4 5 6}
U=scrambles_uniform.txt
run() {  # NAME POLICY SCRAMBLES FIRST COUNT [args]
  if [ -n "${REMOTE:-}" ]; then echo "$*" >> jobs/run_all_$STAGE.txt; else ./run_local.sh "$@"; fi
}
flush() { if [ -n "${REMOTE:-}" ] && [ -s jobs/run_all_$STAGE.txt ]; then ATTEMPTSIM_HOST=$REMOTE ./remote_batch.sh jobs/run_all_$STAGE.txt; fi; }
for STAGE in $STAGES; do
  rm -f jobs/run_all_$STAGE.txt
  case $STAGE in
  0)
    (cd attemptsim && cargo build --release --target x86_64-unknown-linux-musl 2>&1 | tail -1)
    attemptsim/target/x86_64-unknown-linux-musl/release/attemptsim selftest
    [ -s out/big/wca/fm_attempts.tsv ] || python3 src/wca_extract.py
    python3 src/wca_top.py 10 2024 40
    python3 src/make_policies.py ;;
  1)
    run c1_f00 cal1 $U 0 4000
    for s in 0.25 0.35 0.5; do run c0_s${s#0.} cal $U 0 4000 --set cost.attempt_sigma=$s; done
    for f in 0.3 0.5; do run c1_f0${f#0.} cal1 $U 0 4000 --set human.form_sigma=$f; done
    run c0_n40 cal $U 0 4000 --set cost.noise_sigma=0.4
    flush ;;
  2)
    run r2_tr_a all $U 0 1700
    run r2_tr_d all $U 1700 1700
    run r2_tr_c all $U 3400 600
    flush ;;
  3)
    run r3_te final $U 4000 4000
    run r3_off final official_scrambles.txt 0 912
    flush ;;
  4)
    for b in 1200 1800 2700 3600 4500 5400 7200; do run r4_b$b final $U 4000 2000 --set cost.budget=$b; done
    for x in 0.5 0.7 1.4; do run r4_x${x/./} final $U 4000 2000 --set cost.scale_all=$x; done
    run r4_read05 final $U 4000 2000 --set human.read_sd=0.5
    flush ;;
  5)
    bash src/sensitivity_jobs.sh | while read -r line; do run $line; done
    flush ;;
  6)
    if [ -n "${REMOTE:-}" ]; then ATTEMPTSIM_HOST=$REMOTE ./remote_batch.sh --fetch; fi
    python3 src/tables.py
    python3 src/report_build/assemble.py
    python3 src/report_build/check_quotes.py ;;
  esac
done
