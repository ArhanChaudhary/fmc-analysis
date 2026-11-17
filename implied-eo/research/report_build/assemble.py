#!/usr/bin/env python3
"""Build report/WRITEUP.md from writeup.md and report/EXAMPLES.md (the full list): {{ table() }} and {= number =}
from env.py, [[T123]] to dated Discord links, the contents table from the headings."""
import re, sys, os
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B)
import env, links
ROOT = os.path.join(B, '..', '..', 'report')
DESC = {
 'The short version': 'The answer: the list, where it comes from, how often it happens.',
 'What was asked': 'The three questions.',
 'The theorems': 'When N (I) is an EO, when one EO implies another, the trick with its order, and why nothing else happens up to 5 moves.',
 'The list': '**The main result.** The dictionary between axes, the seven kinds, a test scramble for each.',
 'Implied EOs that are not the trick': 'The superflip on both sides: first at 6 moves, with an example.',
 'How often': 'Scrambles with an implied pair, by kind.',
 'The claims, checked': 'Every implication stated on the server, and the ones stated not to be.',
 'What this does not cover': 'Limits.',
 'Appendix: how it was computed, and what is proved in Lean': 'The model, the enumeration, the checks, the Lean theorems by name.',
}
def build(src, dst, contents):
    doc = open(os.path.join(B, src)).read()
    def one(m):
        v = eval(m.group(1), env.ENV); return v if isinstance(v, str) else str(v)
    doc = re.sub(r'\{\{\s*(.+?)\s*\}\}', lambda m: m.group(0) if m.group(1) == 'CONTENTS' else one(m), doc)
    doc = re.sub(r'\{=\s*(.+?)\s*=\}', one, doc)
    used = []
    doc = links.expand(doc, used)
    if contents:
        def anchor(h): return re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
        rows = ['| Section | What is in it |', '|---|---|']
        for h in re.findall(r'(?m)^## (.+)$', doc):
            k = re.sub(r'^\d+\. ', '', h); assert k in DESC, h
            rows.append(f'| [{h}](#{anchor(h)}) | {DESC[k]} |')
        doc = doc.replace('{{CONTENTS}}', '\n'.join(rows))
    assert '{{' not in doc and '[[' not in doc and '{=' not in doc, re.findall(r'\{\{[^}]*\}\}|\[\[[^\]]*\]\]', doc)[:5]
    open(os.path.join(ROOT, dst), 'w').write(doc)
    print(dst, len(doc.split('\n')), 'lines', len(doc), 'bytes; links:', len(used))
build('writeup.md', 'WRITEUP.md', True)
build('examples.md', 'EXAMPLES.md', False)
