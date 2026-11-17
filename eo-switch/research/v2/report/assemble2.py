#!/usr/bin/env python3
"""Build report/WRITEUP.md from writeup.md (and report/BUGS.md from bugs.md with --bugs): {{t_name(args)}} tables and
{= expression =} numbers from env2.py, [[T123]] links to Discord messages, and the contents table from the headings."""
import re, sys, os
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B)
sys.path.insert(0, os.path.join(B, '..', '..', 'src', 'report_build'))
import env2, links
from desc2 import DESC
ROOT = '/data/fmc/eo-switch/'
SRC = 'bugs.md' if '--bugs' in sys.argv else 'writeup.md'
doc = open(os.path.join(B, SRC)).read()
def one(m):
    v = eval(m.group(1), env2.ENV)
    return v if isinstance(v, str) else str(v)
doc = re.sub(r'\{\{\s*(.+?)\s*\}\}', lambda m: m.group(0) if m.group(1) == 'CONTENTS' else one(m), doc)
doc = re.sub(r'\{=\s*(.+?)\s*=\}', one, doc)
used = []
doc = links.expand(doc, used)
def anchor(h): return re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
rows = ['| Section | What is in it |', '|---|---|']
for h in (re.findall(r'(?m)^## (.+)$', doc) if SRC == 'writeup.md' else []):
    key = re.sub(r'^\d+\. ', '', h); assert key in DESC, h
    rows.append(f'| [{h}](#{anchor(h)}) | {DESC[key]} |')
doc = doc.replace('{{CONTENTS}}', '\n'.join(rows))
assert '{{' not in doc and '[[' not in doc and '{=' not in doc, re.findall(r'\{\{[^}]*\}\}|\[\[[^\]]*\]\]', doc)[:5]
open(ROOT + 'report/' + ('BUGS.md' if SRC == 'bugs.md' else 'WRITEUP.md'), 'w').write(doc)
print(len(doc.split('\n')), 'lines', len(doc), 'bytes; links:', len(used))
