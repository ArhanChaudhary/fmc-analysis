#!/bin/bash
# Refresh the Lean certificate's data from the simulator and rebuild it on the second machine.
#   refresh.sh POLICYFILE NSCR [--no-build | --local]   (--local: build on this machine instead of fmc2)
# 1. exports the model and tables (`attemptsim export`, 12 scrambles for the completeness check, EO <= 4, DR <= 9);
# 2. runs every policy of POLICYFILE on the NSCR held-out scrambles 4000 ... 4000+NSCR-1 of
#    research/data/scrambles_uniform.txt with the full log of every attempt (research/out/lean_sample.jsonl) and
#    records the sha256 of the exact table it read;
# 3. runs gen.py (copies the data, writes the manifests, checks the copied Lean files);
# 4. copies the project to fmc2, builds it there with /usr/bin/time -v, and prints the axioms of every theorem.
# Needs: the static simulator build research/attemptsim/target/x86_64-unknown-linux-musl/release/attemptsim, the exact
# table at $EXACT (judging-a-dr's lean_exact_table.u8), python3, and the ssh alias fmc2 (Lean in /data/disk/elan).
# Only the data change normally: then Lake rebuilds Sample, SampleThm (and Manifest's importers if the tables changed).
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
RES=$(cd "$HERE/../../research" && pwd)
POL=$(realpath "$1"); NSCR=$2; BUILD=${3:-}
BIN=$RES/attemptsim/target/x86_64-unknown-linux-musl/release/attemptsim
EXACT=${EXACT:-/data/fmc/judging-a-dr/research/data/lean_exact_table.u8}
REMOTE=${REMOTE:-/data/disk/attempt-sim/lean/AttemptSim}
FIRST=4000
SCRATCH=${TMPDIR:-/tmp}/attemptsim-lean-$$
mkdir -p "$SCRATCH"
export ATTEMPTSIM_DATA=$RES/data RAYON_NUM_THREADS=${RAYON_NUM_THREADS:-4}

echo "== 1. export"
"$BIN" export --out "$RES/out/lean_export" --scrambles "$RES/data/scrambles_uniform.txt" --count 12 --eo 4 --cap 9
echo "== 2. sample: $(grep -c '^\[policy' "$POL") policies x $NSCR scrambles from $FIRST"
sha256sum "$EXACT" > "$RES/out/lean_export/exact_table.sha256"
# memory-capped: /data/fmc/tmp/bin/capped where there is no user systemd (the VM), systemd-run --user elsewhere
RUN=("$BIN" run --costs "$RES/costs.toml" --policies "$POL" --scrambles "$RES/data/scrambles_uniform.txt"
  --first $FIRST --count "$NSCR" --exact "$EXACT" --out "$SCRATCH/sample.tsv" --log "$RES/out/lean_sample.jsonl" --logn "$NSCR")
if [ -x /data/fmc/tmp/bin/capped ]; then /data/fmc/tmp/bin/capped 4G "$(printf '%q ' "${RUN[@]}")"
else systemd-run --user --scope -q -p MemoryMax=2800M "${RUN[@]}"; fi
echo "== 3. gen.py"
python3 "$HERE/gen.py" --eo 4 --cap 9
rm -rf "$SCRATCH"
[ "$BUILD" = "--no-build" ] && exit 0
if [ "$BUILD" = "--local" ]; then
  echo "== 4. build here"
  cd "$HERE" && lake build AttemptSim AttemptSim.Audit > build.log 2>&1; echo "lake exit $?" >> build.log
  grep -E 'error|lake exit' build.log; lake env lean AttemptSim/Audit.lean > audit.log 2>&1; python3 check_build.py
  exit 0
fi
echo "== 4. build on fmc2 ($REMOTE)"
ssh fmc2 "mkdir -p $REMOTE"
rsync -a --checksum --delete --exclude .lake "$HERE/" "fmc2:$REMOTE/"
ssh fmc2 "export PATH=/data/disk/elan/bin:\$PATH ELAN_HOME=/data/disk/elan; cd $REMOTE && \
  /usr/bin/time -v lake build AttemptSim AttemptSim.Audit > build.log 2>&1; echo \"lake exit \$?\" >> build.log; \
  grep -E 'Built (AttemptSim|DRBound)\.[A-Za-z]+ \(|error|lake exit|Elapsed|Maximum resident' build.log | grep -v 'c.o\|dynlib'; \
  lake env lean AttemptSim/Audit.lean > audit.log 2>&1; python3 check_build.py"
