#!/usr/bin/env python3
"""Builds report/WRITEUP.md from writeup.md (next to this file):
  {{T:name}}   the table report/data/name.md
  {{V:key}}    a number from report/data/values.json (written by src/tables.py)
  [[D123]]     a dated link to that Discord message (links.py; kb ids never reach the page)
  {{S:file}}   the text of sec_file.md next to this file
Fails on a missing table or value, so no number in the write-up is typed by hand where a placeholder is used."""
import os, re, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import links
H = os.path.dirname(os.path.abspath(__file__))
REP = os.path.normpath(os.path.join(H, '..', '..', '..', 'report'))
src = open(os.path.join(H, 'writeup.md')).read()
vals = json.load(open(os.path.join(REP, 'data', 'values.json')))
missing = []
def tab(m):
    p = os.path.join(REP, 'data', m.group(1) + '.md')
    if not os.path.exists(p): missing.append('table ' + m.group(1)); return m.group(0)
    return open(p).read().rstrip('\n')
def val(m):
    k = m.group(1)
    if k not in vals: missing.append('value ' + k); return m.group(0)
    return str(vals[k])
out = re.sub(r'\{\{S:([A-Za-z0-9_]+)\}\}', lambda m: open(os.path.join(H, 'sec_' + m.group(1) + '.md')).read().rstrip('\n'), src)
out = re.sub(r'\{\{T:([A-Za-z0-9_]+)\}\}', tab, out)
out = re.sub(r'\{\{V:([A-Za-z0-9_.]+)\}\}', val, out)
if missing:
    print('missing:', ', '.join(sorted(set(missing)))); sys.exit(1)
out = links.expand(out)
left = re.findall(r'\[\[[^\]]*\]\]|\{\{[^}]*\}\}|\b(?:doc|docs) [0-9]+\b', out)
if left:
    print('left in the page:', left[:10]); sys.exit(1)
open(os.path.join(REP, 'WRITEUP.md'), 'w').write(out)
print('wrote', os.path.join(REP, 'WRITEUP.md'), len(out), 'bytes')
