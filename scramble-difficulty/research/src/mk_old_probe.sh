#!/bin/bash
# The min2phase of tnoodle before its 2019 update (commit 7f6fe84^ of tnoodle-lib's history), with the same change as
# GenProbe.java: the clock is replaced by a count of phase-1 solutions tried.  usage: mk_old_probe.sh TNOODLE_LIB OUT
set -euo pipefail
T=$1; O=$2; mkdir -p $O/cs/min2phase
for f in CoordCube CubieCube Search Tools Util; do git -C $T show 7f6fe84^:min2phase/src/main/java/cs/min2phase/$f.java > $O/cs/min2phase/$f.java; done
python3 - "$O/cs/min2phase/Search.java" <<'PY'
import sys
p = sys.argv[1]; s = open(p).read()
a = "\t\tif (System.currentTimeMillis() >= (solution == null ? timeOut : timeMin)) {\n\t\t\treturn 0;\n\t\t}"
b = "\t\tif (budget >= 0) {\n\t\t\tif (solution != null && calls >= budget) {\n\t\t\t\treturn 0;\n\t\t\t}\n\t\t\tcalls++;\n\t\t} else if (System.currentTimeMillis() >= (solution == null ? timeOut : timeMin)) {\n\t\t\treturn 0;\n\t\t}"
assert s.count(a) == 1; s = s.replace(a, b)
a = "\t\t\t\treturn System.currentTimeMillis() >= timeMin ? 0 : 1;"
assert s.count(a) == 1; s = s.replace(a, "\t\t\t\treturn (budget < 0 && System.currentTimeMillis() >= timeMin) ? 0 : 1;")
a = "\tprivate long timeOut;"
assert s.count(a) == 1; s = s.replace(a, "\tpublic long budget = -1, calls = 0;   // budget >= 0: stop after this many phase-1 solutions instead of by the clock\n\tprivate long timeOut;")
a = "\t\tthis.timeOut = System.currentTimeMillis() + timeOut;"
assert s.count(a) == 1; s = s.replace(a, "\t\tthis.calls = 0;\n" + a)
open(p, 'w').write(s)
PY
