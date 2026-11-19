#!/usr/bin/env python3
"""Build report/WRITEUP.md, report/EXAMPLES.md and report/BUGS.md from writeup.md, examples.md and bugs.md:
{{ table() }} and {= number =} from env.py, [[T123]] to dated Discord links, the contents table from the headings.

usage: assemble.py"""
import os
import re
import sys

B = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, B)
import env  # noqa: E402
import links  # noqa: E402

ROOT = os.path.join(B, "..", "..", "..", "report")
DESC = {
    "The short version": "The answer: what is new, what is confirmed, what is corrected.",
    "What was asked": "The questions, and the ones the server left open.",
    "The model, and what carries over to a real cube": "DBL held, R U F turns. The distance tables in moves and in quarter turns, one side and with NISS.",
    "Reading a corner": "The six types, the rule for a quarter turn, and a floor you can prove by hand.",
    "Three reads fix everything: types, D-colour corners, parity": "**The main result.** Why types alone hit HTR 1 time in 6, what the other two reads add, and the test for HTR.",
    "Floors: proving a state needs at least X": "**Reference.** The ladder of floors with how tight each is, the count table, the 9 − k rule, quarter turns, NISS.",
    "Which turn gets closer": "Every rule graded by distance, and the best any rule could do with the same read. The flow chart.",
    "Quarter turns in 3D": "The subset number of the placement, what the twist costs, the out-corner maze, everything within 2 qt.",
    "DR corners, seen from outside DR": "Subset by subset: DR turns against all turns, with and without NISS. What going through CO costs.",
    "The mazes in one place": "Where each maze is, and why there isn't one big one.",
    "The claims, checked": "Everything said on the server that the search can check.",
    "What this does not cover": "Limits.",
    "Appendix: how it was computed, and what is proved in Lean": "The model, the searches, the Lean theorems by name.",
}


def build(src, dst, contents):
    doc = open(os.path.join(B, src)).read()

    def one(m):
        v = eval(m.group(1), env.ENV)
        return v if isinstance(v, str) else str(v)

    doc = re.sub(r"\{\{\s*(.+?)\s*\}\}", lambda m: m.group(0) if m.group(1) == "CONTENTS" else one(m), doc)
    doc = re.sub(r"\{=\s*(.+?)\s*=\}", one, doc)
    used = []
    doc = links.expand(doc, used)
    if contents:
        def anchor(h):
            return re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-")

        rows = ["| Section | What is in it |", "|---|---|"]
        for h in re.findall(r"(?m)^## (.+)$", doc):
            k = re.sub(r"^\d+\. ", "", h)
            assert k in DESC, h
            rows.append(f"| [{h}](#{anchor(h)}) | {DESC[k]} |")
        doc = doc.replace("{{CONTENTS}}", "\n".join(rows))
    left = re.findall(r"\{\{[^}]*\}\}|\[\[[^\]]*\]\]|\{=[^=]*=\}", doc)
    assert not left, left[:5]
    os.makedirs(ROOT, exist_ok=True)
    with open(os.path.join(ROOT, dst), "w") as fh:
        fh.write(doc)
    print(dst, len(doc.split("\n")), "lines", len(doc), "bytes; links:", len(used))


build("writeup.md", "WRITEUP.md", True)
build("examples.md", "EXAMPLES.md", False)
build("bugs.md", "BUGS.md", False)
