#!/usr/bin/env python3
"""The count table for the lookup page (tool/web/count.js) and the cases its test replays (tool/test/cases.json).

usage: tool_data.py"""
import json
import os

B = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(B, "..", "out")
TOOL = os.path.join(B, "..", "..", "tool")


def main():
    R = json.load(open(os.path.join(OUT, "numbers.json")))
    X = json.load(open(os.path.join(OUT, "extra.json")))
    E = json.load(open(os.path.join(OUT, "examples.json")))
    table = {}
    for r in R["count_table"]:
        key = str(r["twisted"] * 1000 + r["out"][0] * 100 + r["out"][1] * 10 + r["out"][2])
        table[f"{r['twisted']}|{','.join(str(x) for x in r['out'])}"] = dict(
            moves=r["floor_d"], niss=X["niss"]["count_floor"][key]["floor"], quarter=r["floor_q"])
    os.makedirs(os.path.join(TOOL, "web"), exist_ok=True)
    os.makedirs(os.path.join(TOOL, "test"), exist_ok=True)
    with open(os.path.join(TOOL, "web", "count.js"), "w") as fh:
        fh.write("// The count table of the write-up (section 6.3): twisted | out by axis, sorted -> floors.\n"
                 "// Written by research/src/tool_data.py from research/out/numbers.json and extra.json.\n"
                 "export const COUNT = " + json.dumps(table, indent=1) + ";\n")
    with open(os.path.join(TOOL, "test", "cases.json"), "w") as fh:
        json.dump(E["random"], fh, indent=1)
    print(len(table), "rows;", len(E["random"]), "test cases")


if __name__ == "__main__":
    main()
