#!/usr/bin/env python3
"""Build report/WRITEUP.md from writeup.md (and report/BUGS.md from bugs.md with --bugs): tables from report/data
({{name}}), other parts of the text ({{NAME}} = name.md in this folder), computed numbers ({= expression =}, names in
xenv.py), links to Discord messages ([[T123]], [[D123]], [[N123]]), and the contents table from the headings."""
import re, sys, os
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B); sys.path.insert(0, os.path.dirname(B))
ROOT = '/data/fmc/htr-routes/'
import xenv, links
SRC = 'bugs.md' if '--bugs' in sys.argv else 'writeup.md'
doc = open(B + '/' + SRC).read()
def part(m):
    p = f'{B}/{m.group(1).lower()}.md'
    assert os.path.exists(p), m.group(1)
    return open(p).read().strip('\n')
for _ in range(4):                          # parts may include parts
    doc = re.sub(r'\{\{([A-Z][A-Z0-9_]*)\}\}', lambda m: m.group(0) if m.group(1) == 'CONTENTS' else part(m), doc)
def table(m):
    p = ROOT + 'report/data/' + m.group(1) + '.md'
    assert os.path.exists(p), m.group(1)
    return open(p).read().strip('\n')
doc = re.sub(r'\{\{([a-z0-9_\-]+)\}\}', table, doc)
pending = []
def one(m):
    try:
        v = eval(m.group(1), xenv.ENV)
    except Exception as e:                       # a data file that is not there yet
        pending.append((m.group(1), repr(e)[:80])); return '(pending)'
    return v if isinstance(v, str) else str(v)
doc = re.sub(r'\{=\s*(.+?)\s*=\}', one, doc)
assert '{=' not in doc
used = []
doc = links.expand(doc, used)
# contents
from desc import DESC          # one line per section, for the contents table
def anchor(h): return re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
rows = ['| Section | What is in it |', '|---|---|']
for h in (re.findall(r'(?m)^## (.+)$', doc) if SRC == 'writeup.md' else []):
    key = re.sub(r'^\d+\. ', '', h); assert key in DESC, h
    rows.append(f'| [{h}](#{anchor(h)}) | {DESC[key]} |')
doc = doc.replace('{{CONTENTS}}', '\n'.join(rows))
assert '{{' not in doc and '[[' not in doc, re.findall(r'\{\{[^}]*\}\}|\[\[[^\]]*\]\]', doc)[:5]
import routefmt; doc = routefmt.page(doc)   # routes as `4b2 2c3 (4b2 4a1 0c0)`
open(ROOT + 'report/' + ('BUGS.md' if SRC == 'bugs.md' else 'WRITEUP.md'), 'w').write(doc)
print(len(doc.split('\n')), 'lines', len(doc), 'bytes; links:', len(used))
if pending:
    print(len(pending), 'numbers pending:'); [print('  ', p) for p in pending[:12]]
    if '--final' in sys.argv: sys.exit(1)
