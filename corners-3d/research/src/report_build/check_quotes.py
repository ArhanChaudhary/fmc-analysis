#!/usr/bin/env python3
"""Every quotation in the write-up, the errata and the examples text against its source.

A unit is a paragraph, a list item or a table row of the source text.  Each "quoted string" in a unit must be found,
word for word, in one of the messages the unit cites ([[N123]]: table msg of kb.sqlite, column content) or, failing
that, in one of the documents of the study (the sheets and docs named in the write-up, as stored in the knowledge
base: table chunk of kb.sqlite).  Differences in quote characters, ligatures and line breaks are ignored; a quotation
may have … in it for a cut.
A quotation repeated further down without its link is looked up among all messages the text cites.
Double quotes are kept for quotations only (terms and column names are in italics), so anything not found is an error.
Prints every quotation that is not found.  usage: check_quotes.py [files]"""
import re, sys, os, glob
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B)
import links
import sqlite3
# the documents the study quotes: Hyper-Parity (rodneykinney), HTR better smh and its v2 (wen and exhaustingg), the
# CO maze gist (rodneykinney), the H48 solver's doc (Sebastiano Tronto)
DOCIDS = (499, 57, 87, 76, 250)
_kb = sqlite3.connect('/data/fmc/kb/kb.sqlite')
def norm(t):
    t = t.replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('ﬀ', 'ff').replace('ﬃ', 'ffi').replace('/quotesingle.ts1', "'")
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('\\', '').replace('`', '').replace('*', '')
    return re.sub(r'\s+', ' ', t).strip().lower()
DOCTEXT = norm(' '.join(t.replace('""', '"') for (t,) in _kb.execute(f'select text from chunk where docid in {DOCIDS} order by docid, idx')))
DOCTEXT = DOCTEXT + ' ' + DOCTEXT.replace('- ', '')          # words hyphenated at a line break in the PDF text
def units(txt):
    out = []; cur = []
    for line in txt.split('\n'):
        if line.startswith('|') or line.lstrip().startswith(('- ', '* ')) or not line.strip():
            if cur: out.append('\n'.join(cur)); cur = []
            if line.strip(): out.append(line)
        else: cur.append(line)
    if cur: out.append('\n'.join(cur))
    return out
def check(path, everywhere):
    txt = re.sub(r'\{=.*?=\}', '', open(path).read()); bad = n = near = far = docs = 0
    for u in units(txt):
        ids = re.findall(r'\[\[([TDN]\d+)\]\]', u)
        quotes = re.findall(r'"([^"\n]{2,})"', u)
        if not quotes: continue
        src = [norm(links.content(i)) for i in ids]
        for q in quotes:
            pieces = [norm(x) for x in re.split(r'…|\.\.\. ', q) if x.strip()]
            n += 1
            if any(all(p in s for p in pieces) for s in src): near += 1
            elif all(p in DOCTEXT for p in pieces): docs += 1
            elif any(all(p in s for p in pieces) for s in everywhere): far += 1
            else: bad += 1; print(f'  NOT FOUND in {os.path.basename(path)}: "{q}"   (cited here: {", ".join(ids) or "no message"})')
    return n, near, docs, far, bad
if __name__ == '__main__':
    files = sys.argv[1:] or [B + '/writeup.md', B + '/bugs.md', B + '/examples.md']
    files = [f for f in files if os.path.exists(f)]
    cited = sorted({i for f in files for i in re.findall(r'\[\[([TDN]\d+)\]\]', open(f).read())})
    everywhere = [norm(links.content(i)) for i in cited]
    tot = [0, 0, 0, 0, 0]
    for f in files:
        r = check(f, everywhere)
        tot = [a + b for a, b in zip(tot, r)]
        print(f'{os.path.basename(f)}: {r[0]} quotations; {r[1]} in a message cited next to them, {r[2]} in a document, '
              f'{r[3]} in a message cited elsewhere, {r[4]} not found')
    print('total not found:', tot[4])
    sys.exit(1 if tot[4] else 0)
