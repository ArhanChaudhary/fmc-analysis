# Scramble difficulty: how to rerun

The write-up is `../report/WRITEUP.md` (the first draft was `REPORT.md`). The study was built in `/data/scramble-difficulty`
on the machine the site's studies are built on; the paths below and in the scripts are relative to that folder, where
`big/`, `ext/` and `venv/` (not in the repository) also live. Heavy steps ran on the second VM (`fmc2`, under `/data/disk/scramble-difficulty`), the
rest here. Python: `src/*.py` other than `analysis.py` run on the system `python3` (pure Python);
`analysis.py` needs `venv/` (numpy, scipy, scikit-learn: `python3 -m venv venv && venv/bin/pip install numpy scipy scikit-learn`).

## Inputs

| What | Where it came from |
|---|---|
| tnoodle-lib source | `git clone https://github.com/thewca/tnoodle-lib` into `ext/tnoodle-lib` (commit d01a947, 2026-10-05) |
| JDK 17 | Adoptium tarball into `ext/jdk-17.0.21+9` |
| official scrambles | WCA results export v2.0.2 of 2026-11-13 (`https://www.worldcubeassociation.org/export/results/v2/tsv`): table `scrambles`, event `333fm` → `big/fm_scrambles.tsv`; `competitions` (id, year, month, day) → `big/comp_dates.tsv` |
| uniform population | `/data/fmc/gaps/research/big/pop_raw.tsv`, `pop_label.tsv`, `pop_raw_scrambles.txt` (10,000 uniform states, every EO-first DR of at most 11 moves, labelled with the exact optimal finish) |
| optimal lengths | DougCube's sheet, kb copy `/data/fmc/kb/docs/gsheet/183AYpjKz4fZZAy5Hx5lxEthD2f356ReZG-uHPm_HWcY/FMC.csv` |
| lore | `out/lore.md` (quotes from the kb, collected for this study) |

## Steps

```bash
# 1. TNoodle scrambles: the generator is tnoodle-lib's min2phase + a driver that only records the solver's split
J=ext/jdk-17.0.21+9/bin
$J/javac -d build -sourcepath ext/tnoodle-lib/min2phase/src/main/java:src/java src/java/cs/min2phase/GenFMC.java
$J/java -cp build cs.min2phase.GenFMC 12000 2 0 big/gen12k.tsv     # stopped after 5,771 (2 threads, ~200 ms each)
#   big/gen.tsv = the complete rows; big/in_gen.tsv = "g<k>\t<scramble>"
python3 src/real_scr.py             # big/real_unique.tsv (8,108 padded official scrambles), per-year text stats
python3 src/check_gen.py big/gen.tsv  # generator rows: state reproduced, text split vs min2phase's own split
python3 src/tnoodle_check.py        # out/tnoodle_tables.txt, out/tnoodle_examples.txt
python3 src/randmove_baseline.py    # out/randmove_baseline.txt

# 2. the DR lists (EO <= 5 with NISS, then DR; total <= 10) for the official and generated scrambles
#    src/enum_drs.py is gaps' population.py with the DR cap at 10 and a scramble list as input.
#    It ran in two parts: here with cap 11 (rows of length <= 10 kept: big/*_raw_10a.tsv) and on fmc2 with cap 10
#    for the rest (big/*_raw_10b.tsv); fmc2's src/label.sh merges them and labels every DR state:
#      htrtools label lean_exact_table.u8 ls_depth.u8 < ces > big/<pop>_label_10.tsv   (gaps' htrtools fork)
source /data/fmc/env.sh
python3 src/enum_drs.py big/in_real.tsv big/real_raw.tsv 4      # (as one run; see above for how it was split)
python3 src/enum_drs.py big/in_gen.tsv big/gen_raw.tsv 4

# 3. targets and features
python3 src/targets.py /data/fmc/gaps/research/big/pop_raw.tsv /data/fmc/gaps/research/big/pop_label.tsv u out/tgt_uni.tsv out/tgt_uni_axis.tsv 10
python3 src/targets.py big/real_raw_10.tsv big/real_label_10.tsv '' out/tgt_real.tsv out/tgt_real_axis.tsv 10
python3 src/targets.py big/gen_raw_10.tsv big/gen_label_10.tsv '' out/tgt_gen.tsv out/tgt_gen_axis.tsv 10
awk '{print "u"NR-1"\t"$0}' /data/fmc/gaps/research/big/pop_raw_scrambles.txt > big/in_uni.tsv
python3 src/coords.py                                   # coordinate tables + self-test (out/coords.pkl)
python3 src/features.py big/in_uni.tsv out/feat_uni.tsv x 2
python3 src/features.py big/in_real.tsv out/feat_real.tsv tnoodle 2
python3 src/features.py big/in_gen.tsv out/feat_gen.tsv tnoodle 2
for p in uni real gen; do python3 src/features2.py big/in_$p.tsv out/feat2_$p.tsv; done
python3 src/sheet_join.py                               # out/opt_real.tsv, EO cross-check

# 4. statistics (all tables of the report): out/analysis.txt, out/results.json
venv/bin/python src/analysis.py

# 5. witnesses and Lean
python3 src/witnesses.py                                # out/witnesses.txt, out/lean_claims.json
python3 src/gen_lean.py && (cd lean/ScrDiff && lake build)
```

`src/cube.py` (cubie model + facelets, self-test: `python3 src/cube.py`) and `src/coords.py` are this study's own
cube code; `src/textfeat.py` reads the split off a scramble's text.

## Added for the public version (`public/WRITEUP.md`, `public/README.md`)

```bash
# which EO axis each DR comes from (section 6.1 and 6.4 of the public page)
for p in real gen uni; do python3 src/enum_eoaxis.py big/in_$p.tsv out/eoaxis_$p.tsv 2; done
# features proposed on the server: shared bad edges, Levi Gibson's seven counts, DRM-style pairs, corner QT
python3 src/features3.py selftest
for p in uni real gen; do python3 src/features3.py big/in_$p.tsv out/feat3_$p.tsv; done
# corner cases of every scramble's DRs
python3 src/drqt.py /data/fmc/gaps/research/big/pop_raw.tsv /data/fmc/gaps/research/big/pop_label.tsv u out/drqt_uni.tsv
python3 src/drqt.py big/real_raw_10.tsv big/real_label_10.tsv '' out/drqt_real.tsv
python3 src/drqt.py big/gen_raw_10.tsv big/gen_label_10.tsv '' out/drqt_gen.tsv
venv/bin/python src/claims_extra.py      # out/claims_extra.txt: corner QT, per-axis features, EO axes, claim details
venv/bin/python src/layer_rule.py        # out/layer_rule.txt: flipped layer edges as an axis rule
venv/bin/python src/layer_scr.py         # out/layer_scr.txt: the same at scramble level
# is the official middle the first solution min2phase finds?
J=ext/jdk-17.0.21+9/bin
$J/javac -d build -sourcepath ext/tnoodle-lib/min2phase/src/main/java:src/java src/java/cs/min2phase/FirstSol.java
$J/java -cp build cs.min2phase.FirstSol < big/states_real.tsv > big/first_real.tsv    # states_real.tsv: id, facelets of each official middle
python3 src/first_check.py               # out/first_check.txt
python3 src/witnesses.py && python3 src/gen_lean.py && (cd lean/ScrDiff && lake build)   # 30 theorems
# the page: quotation check against the knowledge base, and a render with the site's pandoc settings
python3 src/check_quotes.py public/WRITEUP.md
```
