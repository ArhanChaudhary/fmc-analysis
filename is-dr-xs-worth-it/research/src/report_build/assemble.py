#!/usr/bin/env python3
"""Build report/WRITEUP.md from writeup.md: tables from report/data ({{name}}), computed numbers ({= expression =},
names in xenv.py), links to Discord messages ([[T123]]), and the contents table from the headings."""
import re, sys, sqlite3, datetime, os
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B); sys.path.insert(0, os.path.dirname(B))
ROOT = '/data/fmc/is-dr-xs-worth-it/'
import xenv
sys.path.insert(0, '/data/fmc/judging-a-dr/research/src'); import pv
SRC = 'bugs.md' if '--bugs' in sys.argv else 'writeup.md'
doc = open(B + '/' + SRC).read()
for name in ('real', 'app_c'):
    p = f'{B}/{name}.md'
    if os.path.exists(p): doc = doc.replace('{{' + name.upper() + '}}', open(p).read().strip('\n'))
def table(m):
    p = ROOT + 'report/data/' + m.group(1) + '.md'
    assert os.path.exists(p), m.group(1)
    return open(p).read().strip('\n')
doc = doc.replace('{{APP_A}}', '{{app_a}}').replace('{{APP_B}}', '{{app_b}}')
doc = re.sub(r'\{\{([a-z0-9_]+)\}\}', table, doc)
pending = []
def one(m):
    try:
        v = eval(m.group(1), xenv.ENV)
    except Exception as e:                       # a data file that is not there yet
        pending.append((m.group(1), repr(e)[:60])); return '(pending)'
    return v if isinstance(v, str) else str(v)
doc = re.sub(r'\{=\s*(.+?)\s*=\}', one, doc)
assert '{=' not in doc
db = sqlite3.connect('/data/fmc/kb/kb.sqlite')
CH = {'fmc-theory': '1007841335434285126', 'fmc-discussion': '1007841273111117924'}
NAME = {'rodneykinney': 'Rodney', 'Jay (vibing)': 'Jay'}
used = []
def link(m):
    r = db.execute('select id,channel,ts,author from msg where sid=?', (m.group(1),)).fetchone(); assert r, m.group(1)
    y, mo, d = map(int, r[2][:10].split('-')); used.append(m.group(1))
    return f"[{d} {datetime.date(y, mo, d).strftime('%b %Y')}](https://discord.com/channels/1007840975726575667/{CH[r[1]]}/{r[0]})"
doc = re.sub(r'\[\[([TD]\d+)\]\]', link, doc)
# contents
DESC = {
 'The short version': 'What is new, what it confirms or corrects, and the verdict, one line each.',
 'What was asked': 'The questions and the standing disagreement, quoted.',
 'What a DR-xs is, and how many slices it needs': 'The 768 kinds and the rule for the number of slices.',
 'The move counts: DR-3s, DR-2s, DR-1s, DR': 'Every layout of flipped edges and what it takes to fix.',
 'The finish: DR-1s and DR-2s 8fe against a DR': 'Averages and odds by subset, which DR-1s are good, what a hand finish loses.',
 'Getting one': 'Slice-EO skip odds, how far a DR-1s is from a skip, and why getting to an 8fe is the same problem as getting to a DR.',
 'On 500 real scrambles': 'Every DR-1s and DR-2s 8fe against every normal DR on the same scrambles.',
 'The claims, checked': 'Each checkable statement from the server, with the verdict.',
 'What this does not cover': 'Limits.',
 'Appendix A: every DR-1s layout': 'The 70 layouts with a shortest fix and a scramble each.',
 'Appendix B: from an edge-orientation pattern to a kind of DR-xs': 'What each uniform EO pattern leads to, for each choice of faces.',
 'Appendix C: how it was computed, and what checks it': 'Method, cross-checks and the Lean certificate.',
 'Docs referred to': 'Links.',
}
def anchor(h): return re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
rows = ['| Section | What is in it |', '|---|---|']
for h in (re.findall(r'(?m)^## (.+)$', doc) if SRC == 'writeup.md' else []):
    key = re.sub(r'^\d+\. ', '', h); assert key in DESC, h
    rows.append(f'| [{h}](#{anchor(h)}) | {DESC[key]} |')
doc = doc.replace('{{CONTENTS}}', '\n'.join(rows))
assert '{{' not in doc and '[[' not in doc, re.findall(r'\{\{[^}]*\}\}|\[\[[^\]]*\]\]', doc)[:5]
open(ROOT + 'report/' + ('BUGS.md' if SRC == 'bugs.md' else 'WRITEUP.md'), 'w').write(doc)
print(len(doc.split('\n')), 'lines', len(doc), 'bytes; links:', len(used))
if pending:
    print(len(pending), 'numbers pending:'); [print('  ', p) for p in pending[:12]]
    if '--final' in sys.argv: sys.exit(1)
