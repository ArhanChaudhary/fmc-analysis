#!/usr/bin/env python3
"""Every quotation of the write-up against its source, word for word.

Double quotes are kept for quotations only (terms, tab and column names are in italics), so every "quoted string"
of report/WRITEUP.md must be found in one of the sources the page cites, as stored in the knowledge base: Rodney
Kinney's Advanced DR Bounding and DRM Subsets docs (table chunk of kb.sqlite) or one of the Discord messages the
page links (table msg, looked up by the message id in the link).  Differences in quote characters, backslashes and
line breaks are ignored.  Also fails on an internal knowledge-base id (T123, D123, N123, doc 12) left on the page.
Needs the knowledge base, which is not in the repository.  usage: check_quotes.py [file]"""
import re, sqlite3, sys
PAGE = sys.argv[1] if len(sys.argv) > 1 else '/data/fmc/dr-variants/report/WRITEUP.md'
DOCS = (411, 275)       # Advanced DR Bounding [Beta] (Rodney Kinney's own copy), DRM Subsets
kb = sqlite3.connect('/data/fmc/kb/kb.sqlite')
def norm(t):
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('\\', ''), ('`', ''), ('*', '')): t = t.replace(a, b)
    return re.sub(r'\s+', ' ', t).strip().lower()
text = open(PAGE).read()
sources = [norm(' '.join(t for (t,) in kb.execute('select text from chunk where docid=? order by idx', (d,)))) for d in DOCS]
ids = sorted(set(re.findall(r'discord\.com/channels/\d+/\d+/(\d+)', text)))
for i in ids:
    row = kb.execute('select content from msg where id=?', (i,)).fetchone()
    assert row, f'linked message {i} is not in the knowledge base'
    sources.append(norm(row[0]))
prose = re.sub(r'`[^`\n]*`', ' ', text)                      # move sequences and code are not quotations
quotes = re.findall(r'"([^"\n]+)"', prose)
bad = [q for q in quotes if not any(norm(q).rstrip('.,') in s for s in sources)]
for q in bad: print('NOT FOUND:', q)
leaked = re.findall(r'\b[TDN]\d{3,5}\b|\bdoc \d+\b', prose)
for x in leaked: print('INTERNAL ID:', x)
print(f'{len(quotes)} quotations, {len(ids)} linked messages, {len(bad)} not found, {len(leaked)} internal ids')
sys.exit(1 if bad or leaked else 0)
