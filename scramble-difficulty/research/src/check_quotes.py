"""Quotation check for the public page.  usage: check_quotes.py WRITEUP.md
Every text in straight double quotes on the page must occur verbatim in a Discord message linked in the same
paragraph, list item or table row (line breaks of a message are written " / " on the page).  Prints, per quote,
the message it was found in and whether it is the whole message; for partial quotes, the rest of the message, so a
dropped hedge or condition shows.  Also: links whose message is not in the knowledge base, internal ids, local paths,
and every person named next to a link with the display name and username the knowledge base has for that message."""
import re, sys, sqlite3
page = open(sys.argv[1]).read()
db = sqlite3.connect('/data/fmc/kb/kb.sqlite')
LINK = re.compile(r'\[([^\]]+)\]\(https://discord\.com/channels/(\d+)/(\d+)/(\d+)\)')
def norm(s): return re.sub(r'\s+', ' ', s.replace('\n', ' / ')).strip()
def msg(mid):
    r = db.execute('select content, author, username, ts, channel from msg where id=?', (mid,)).fetchone()
    return r
blocks = re.split(r'\n\s*\n', page)
units = []
for b in blocks:
    if b.lstrip().startswith('|'):
        units += [l for l in b.split('\n')]            # one table row = one unit
    elif re.search(r'^\s*[-*] ', b, re.M):
        cur = []
        for l in b.split('\n'):
            if re.match(r'^\s*[-*] ', l) and cur: units.append('\n'.join(cur)); cur = []
            cur.append(l)
        if cur: units.append('\n'.join(cur))
    else:
        units.append(b)
WHITELIST = {'findable'}   # inside the unattributed question of section 2
bad = 0; nq = 0; partial = 0; nfull = 0; missing_links = set(); people = {}
for u in units:
    links = LINK.findall(u)
    msgs = {}
    for text, g, c, m in links:
        r = msg(m)
        if r is None: missing_links.add(m); continue
        msgs[m] = r
        people.setdefault((r[1], r[2]), set())
    plain = re.sub(r'`[^`]*`', lambda mo: mo.group(0), u)
    utext = norm(re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', u)).replace('\\|', '|')
    full = {m for m, r in msgs.items() if norm(r[0]) in utext}
    nfull += len(full)
    quotes = re.findall(r'"([^"\n]{3,})"', re.sub(r'\]\([^)]*\)', ']', u))
    for q in quotes:
        if q in WHITELIST: continue
        nq += 1
        qn = norm(q).replace('\\|', '|')
        hit = None
        for m, r in msgs.items():
            cn = norm(r[0])
            # markdown on the page may escape * and _ ; compare with and without backslashes
            if qn in cn or qn.replace('\\', '') in cn: hit = (m, r, cn); break
        if not hit:
            bad += 1; print(f'NOT FOUND: "{q[:140]}"  (links in unit: {len(msgs)})')
            continue
        m, r, cn = hit
        whole = (qn == cn) or (qn.replace('\\', '') == cn) or (m in full)
        if not whole:
            partial += 1
            rest = cn.replace(qn if qn in cn else qn.replace('\\', ''), ' [...QUOTED...] ')
            print(f'PARTIAL ({r[1]} | {r[2]}, {r[3][:10]}): "{q[:80]}..."\n    rest of message: {rest[:600]}')
print(f'\nmessages quoted in full (whole text present in their paragraph or row): {nfull}')
print(f'quotes checked: {nq}; not found: {bad}; partial quotes: {partial}; links to messages not in the kb: {sorted(missing_links)}')
print('authors of linked messages (display name | username):')
for (a, un) in sorted(people): print('   ', a, '|', un)
for pat, lab in ((r'\b[TDN]\d{2,5}\b', 'internal message id'), (r'\bdocs? \d+\b', 'internal doc id'), (r'/data/|/home/|/tmp/', 'local path'), (r'\bsrc/|\bout/|\bbig/', 'study file path')):
    found = sorted(set(re.findall(pat, page)))
    print(f'{lab}: {found[:20]}')
