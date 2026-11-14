#!/bin/bash
# The sensitivity stage on this machine: every job of src/sensitivity_jobs.sh, one at a time, all cores, memory-capped
# (/data/fmc/tmp/bin/capped).  Output: out/big/s_*.tsv and .summary.txt.  usage: run_sens.sh
set -uo pipefail
cd "$(dirname "$0")"
EXACT=/data/fmc/judging-a-dr/research/data/lean_exact_table.u8
BIN=attemptsim/target/x86_64-unknown-linux-musl/release/attemptsim
bash src/sensitivity_jobs.sh | while read -r NAME POL SCR FIRST COUNT REST; do
  [ -f out/big/$NAME.tsv ] && continue
  echo "$(date +%T) start $NAME"
  /data/fmc/tmp/bin/capped 6G "RAYON_NUM_THREADS=8 nice -n 10 $BIN run --costs costs.toml --policies policies/$POL.toml --scrambles data/$SCR --first $FIRST --count $COUNT --seed 1 --exact $EXACT --out out/big/$NAME.tsv.part $REST > out/big/$NAME.summary.txt 2> out/big/$NAME.err" \
    && mv out/big/$NAME.tsv.part out/big/$NAME.tsv && echo "$(date +%T) done $NAME: $(tail -1 out/big/$NAME.err)" || echo "$(date +%T) FAILED $NAME"
done
echo ALLDONE
