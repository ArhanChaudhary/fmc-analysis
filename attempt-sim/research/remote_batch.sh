#!/bin/bash
# Run a list of experiments on another machine, one after the other, in the background there.
#   remote_batch.sh JOBS.txt      each line: NAME POLICYFILE(without .toml) SCRAMBLES FIRST COUNT [extra attemptsim args]
#                                 (extra args: --set cost.KEY=V, --set human.KEY=V, --log FILE --logn K)
#   remote_batch.sh --fetch       bring every finished result back to out/big/
# Machine: ATTEMPTSIM_HOST = fmc3 (24 slow x86 threads), fmc2 (8 x86 cores) or fmc4 (aarch64 laptop, 8 cores; the
# simulator is built there).  Results: out/big/NAME.tsv and NAME.summary.txt.  Progress: out/batch_TAG.log there.
# x86 machines get the static (musl) build of this folder's crate:
#   (cd attemptsim && cargo build --release --target x86_64-unknown-linux-musl)
# The exact DR-finish table (1.3 GB, judging-a-dr's lean_exact_table.u8) must already be on the machine at $EXACT.
# Nothing but code, scrambles and numeric tables is copied to the machines.  See /data/fmc/tmp/MACHINES.md.
set -euo pipefail
cd "$(dirname "$0")"
HOST=${ATTEMPTSIM_HOST:-fmc3}
B4=/data/fmc/tmp/bin
case "$HOST" in
  fmc3) DIR=${ATTEMPTSIM_DIR:-/var/tmp/fmc-$USER/attempt-sim}; EXACT=${ATTEMPTSIM_EXACT:-$DIR/data/lean_exact_table.u8}; NICE="nice -n 19";;
  fmc2) DIR=${ATTEMPTSIM_DIR:-/data/disk/attempt-sim/r2}; EXACT=${ATTEMPTSIM_EXACT:-/data/disk/fmc/judging-a-dr/research/data/lean_exact_table.u8}; NICE="nice -n 5";;
  fmc4) DIR=fmc-work/attempt-sim; EXACT=data/lean_exact_table.u8; NICE="nice -n 19";;
  *) DIR=${ATTEMPTSIM_DIR:?set ATTEMPTSIM_DIR}; EXACT=${ATTEMPTSIM_EXACT:?set ATTEMPTSIM_EXACT}; NICE="";;
esac
rexec() { if [ "$HOST" = fmc4 ]; then ssh fmc4 'bash -s' <<< "$1"; else ssh "$HOST" "$1"; fi; }   # fmc4's login shell is fish
if [ "$1" = "--fetch" ]; then
  mkdir -p out/big
  if [ "$HOST" = fmc4 ]; then
    T=$(mktemp -d); $B4/fmc4-get $DIR/out "$T"
    for f in "$T"/out/*.tsv "$T"/out/*.summary.txt "$T"/out/*.jsonl "$T"/out/batch_*.log; do [ -e "$f" ] && cp "$f" out/big/; done
    rm -rf "$T"
  else
    rsync -a --include='*.tsv' --include='*.summary.txt' --include='*.jsonl' --include='batch_*.log' --exclude='*' "$HOST:$DIR/out/" out/big/
  fi
  exit 0
fi
JOBS=$1; TAG=$(basename "$JOBS" .txt)
if [ "$HOST" = fmc4 ]; then
  T=$(mktemp -d); mkdir -p "$T/crate" "$T/run"
  cp -r attemptsim/Cargo.toml attemptsim/Cargo.lock attemptsim/src "$T/crate/"
  cp -r policies "$T/run/"; cp costs.toml "$T/run/costs-$TAG.toml"; cp "$JOBS" "$T/run/$TAG.jobs"
  mkdir -p "$T/run/data"; cp data/*.txt data/*.tsv "$T/run/data/"
  (cd "$T/run" && $B4/fmc4-put policies data costs-$TAG.toml $TAG.jobs $DIR)
  (cd "$T" && $B4/fmc4-put crate $DIR/build-$TAG)
  rm -rf "$T"
  rexec "cd ~/$DIR && mkdir -p bin out && export RUSTUP_HOME=~/fmc-work/rust/rustup CARGO_HOME=~/fmc-work/rust/cargo PATH=~/fmc-work/rust/cargo/bin:\$PATH && (cd build-$TAG/crate && nice -n 19 cargo build --release 2>&1 | tail -1) && cp build-$TAG/crate/target/release/attemptsim bin/attemptsim-$TAG"
  DIR="\$HOME/$DIR"
else
  BIN=attemptsim/target/x86_64-unknown-linux-musl/release/attemptsim
  ssh "$HOST" "mkdir -p $DIR/bin $DIR/out $DIR/policies $DIR/data"
  rsync -a "$BIN" "$HOST:$DIR/bin/attemptsim-$TAG"
  rsync -a policies/ "$HOST:$DIR/policies/"
  rsync -a costs.toml "$HOST:$DIR/costs-$TAG.toml"
  rsync -a data/ "$HOST:$DIR/data/" --exclude lean_exact_table.u8
  rsync -a "$JOBS" "$HOST:$DIR/$TAG.jobs"
fi
# one runner per tag, so that a batch that is still running is never rewritten under it (written here, copied over)
RUNNER=$(mktemp -d)/run_$TAG.sh
cat > $RUNNER <<X
#!/bin/bash
cd $DIR
export ATTEMPTSIM_DATA=$DIR/data
while read -r NAME POL SCR FIRST COUNT REST; do
  [ -z "\$NAME" ] && continue
  case "\$NAME" in \#*) continue;; esac
  echo "\$(date +%T) start \$NAME"
  $NICE bin/attemptsim-$TAG run --costs costs-$TAG.toml --policies policies/\$POL.toml --scrambles data/\$SCR --first \$FIRST --count \$COUNT --seed 1 --exact $EXACT --out out/\$NAME.tsv.part \$REST > out/\$NAME.summary.txt 2> out/\$NAME.err && mv out/\$NAME.tsv.part out/\$NAME.tsv
  cat out/\$NAME.err >> out/\$NAME.summary.txt
  echo "\$(date +%T) done \$NAME: \$(tail -1 out/\$NAME.err)"
done < $TAG.jobs
echo ALLDONE
X
chmod +x $RUNNER
if [ "$HOST" = fmc4 ]; then (cd $(dirname $RUNNER) && $B4/fmc4-put run_$TAG.sh fmc-work/attempt-sim); else rsync -a $RUNNER "$HOST:$DIR/"; fi
rm -rf $(dirname $RUNNER)
rexec "cd $DIR && setsid nohup ./run_$TAG.sh > out/batch_$TAG.log 2>&1 < /dev/null & echo started pid \$!"
