#!/bin/bash
# Run one experiment on the 24-thread machine and bring the result back.
#   remote.sh NAME POLICIES.toml SCRAMBLES FIRST COUNT [extra attemptsim arguments, e.g. --set cost.rzp=10]
# NAME.tsv lands in out/big/; the per-policy summary is printed and kept in out/big/NAME.summary.txt.
# (Machine alias and directory: see README "Machines"; nothing but code, scrambles and numeric tables goes there.)
set -euo pipefail
cd "$(dirname "$0")"
NAME=$1; POL=$2; SCR=$3; FIRST=$4; COUNT=$5; shift 5
HOST=${ATTEMPTSIM_HOST:-fmc3}
DIR=${ATTEMPTSIM_DIR:-/var/tmp/fmc-$USER/attempt-sim}
rsync -a "$POL" "$HOST:$DIR/policies/$NAME.toml"
rsync -a costs.toml "$HOST:$DIR/costs.toml"
ssh "$HOST" "cd $DIR && ATTEMPTSIM_DATA=$DIR/data nice -n 19 bin/attemptsim run --costs costs.toml --policies policies/$NAME.toml --scrambles data/$SCR --first $FIRST --count $COUNT --seed ${SEED:-1} --exact data/lean_exact_table.u8 --out out/$NAME.tsv $* > out/$NAME.summary.txt 2> out/$NAME.err; cat out/$NAME.err >> out/$NAME.summary.txt"
mkdir -p out/big
rsync -a "$HOST:$DIR/out/$NAME.tsv" "$HOST:$DIR/out/$NAME.summary.txt" out/big/
cat out/big/$NAME.summary.txt
