#!/bin/bash
# Run one experiment on this machine (memory-capped), the same way remote_batch.sh does on the others.
#   run_local.sh NAME POLICYFILE(without .toml) SCRAMBLES FIRST COUNT [extra attemptsim args]
# Needs the static build (attemptsim/target/x86_64-unknown-linux-musl/release/attemptsim) and the exact table at
# $ATTEMPTSIM_EXACT (default: judging-a-dr's research/data/lean_exact_table.u8).  Output: out/big/NAME.tsv, NAME.summary.txt.
set -euo pipefail
cd "$(dirname "$0")"
NAME=$1; POL=$2; SCR=$3; FIRST=$4; COUNT=$5; shift 5
EXACT=${ATTEMPTSIM_EXACT:-/data/fmc/judging-a-dr/research/data/lean_exact_table.u8}
BIN=attemptsim/target/x86_64-unknown-linux-musl/release/attemptsim
mkdir -p out/big
RAYON_NUM_THREADS=${THREADS:-4} systemd-run --user --scope -q -p MemoryMax=2800M nice -n 10 \
  $BIN run --costs costs.toml --policies policies/$POL.toml --scrambles data/$SCR --first $FIRST --count $COUNT --seed 1 \
  --exact "$EXACT" --out out/big/$NAME.tsv.part "$@" > out/big/$NAME.summary.txt 2> out/big/$NAME.err
mv out/big/$NAME.tsv.part out/big/$NAME.tsv
cat out/big/$NAME.err >> out/big/$NAME.summary.txt
cat out/big/$NAME.summary.txt | tail -3
