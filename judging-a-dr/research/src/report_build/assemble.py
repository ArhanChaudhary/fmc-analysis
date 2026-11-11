import re, sqlite3, datetime
R='/data/fmc/judging-a-dr/report/'
old=open('/data/fmc/judging-a-dr/research/src/report_build/WRITEUP_first_version.md').read()
assert old.startswith('# DR Bounding at any qt'), 'WRITEUP.md is not the old version; restore it before assembling'
def section(start, end):
    a=old.index(start); b=old.index(end, a+1)
    return old[a:b]
def body(start, end):
    t=section(start,end); return t[t.index('\n')+1:].strip('\n')
def strip_rule(t): return re.sub(r'\n---\s*$', '', t.strip('\n')).strip('\n')

levels = strip_rule(body('## What to look at: seven levels', '## How good is it'))
howgood = strip_rule(body('## How good is it', '## Examples'))
examples = strip_rule(body('## Examples', '## What you can use in an actual solve'))
c216 = strip_rule(body('## The 216 NISS@1qt cases, three ways', '## The proof, if you don'))
proof = strip_rule(body('## The proof, if you don', '## How it was computed and checked'))
how = strip_rule(body('## How it was computed and checked', "## What this doesn't do"))
appA = strip_rule(body('## Appendix A: all 48 subsets', '## Appendix B'))
appB = strip_rule(body('## Appendix B', '## Appendix C'))
appC = strip_rule(body('## Appendix C', '## Docs and sheets referred to'))
docs = old[old.index('## Docs and sheets referred to'):].strip('\n')
docs = docs[docs.index('\n')+1:].strip('\n')
zero_row = re.search(r"\| 0c0 \| 0e/2e/4e are short\..*\|", old).group(0)

# Appendix A: add the longest optimal of each subset
MAXD = dict(x.rsplit(' ',1) for x in '''0c0 0e 13|0c0 2e 15|0c0 4e 16|0c0 6e 16|0c0 8e 18|4a1 0e 16|4a1 2e 16|4a1 4e 17|4a2 0e 17|4a2 2e 17|4a2 4e 16|4b2 0e 16|4b2 2e 16|4b2 4e 16|0c3 0e 17|0c3 2e 17|0c3 4e 18|0c3 6e 17|0c3 8e 17|2c3 0e 16|2c3 2e 15|2c3 4e 16|2c3 6e 16|2c3 8e 16|4c3 0e 16|4c3 2e 16|4c3 4e 16|0c4 0e 16|0c4 2e 16|0c4 4e 16|0c4 6e 16|0c4 8e 16|2c4 0e 16|2c4 2e 17|2c4 4e 16|2c4 6e 17|2c4 8e 17|4c4 0e 17|4c4 2e 17|4c4 4e 17|2c5 0e 18|2c5 2e 17|2c5 4e 18|2c5 6e 17|2c5 8e 17|4b5 0e 17|4b5 2e 16|4b5 4e 17'''.split('|'))
outA=[]; seen=0
for line in appA.split('\n'):
    cells=line.split(' | ')
    if line.startswith('| Subset |'):
        cells.insert(4,'Longest'); line=' | '.join(cells)
    elif line.startswith('|---'):
        line=line.replace('|---|---:|---:|---:|','|---|---:|---:|---:|---:|',1)
    elif line.startswith('| ') and cells[0][2:] in MAXD:
        cells.insert(4, MAXD[cells[0][2:]]); line=' | '.join(cells); seen+=1
    outA.append(line)
assert seen==48, seen
appA='\n'.join(outA)

front=open('/data/fmc/judging-a-dr/research/src/report_build/new_front.md').read().rstrip('\n')
tail=open('/data/fmc/judging-a-dr/research/src/report_build/new_tail.md').read()
def data(name): return open(R+'data/'+name).read().strip('\n')
doc = (front + '\n\n### The seven levels\n\n' + levels + '\n\n' + howgood + '\n\n### Examples\n\n' + examples + '\n\n'
       + tail.replace('{{C216}}', c216).replace('{{PROOF}}', proof).replace('{{HOW}}', how)
              .replace('{{APPA}}', appA).replace('{{APPB}}', appB).replace('{{APPC}}', appC)
              .replace('{{PAIRS}}', data('odds_by_true_pairs.md')).replace('{{CORNERS}}', data('corner_cases.md'))
              .replace('{{SQUARES}}', data('htr_square_tables.md')).replace('{{WITNESSES}}', data('witnesses_by_subset.md')).replace('{{DOCS}}', docs))

# links
db=sqlite3.connect('/data/fmc/kb/kb.sqlite')
CH={'fmc-theory':'1007841335434285126','fmc-discussion':'1007841273111117924'}
NAME={'rodneykinney':'Rodney','Jay (vibing)':'Jay','beef beans':'Levi','Tomas Rokicki (radeye)':'Tomas Rokicki','Louis | 2012SART01':'Louis'}
def meta(sid):
    r=db.execute('select id,channel,ts,author from msg where sid=?',(sid,)).fetchone()
    assert r, sid
    y,m,d=map(int,r[2][:10].split('-'))
    who='Oskar' if r[3].startswith('Oskar') else NAME.get(r[3],r[3])
    return who, f"{d} {datetime.date(y,m,d).strftime('%b %Y')}", f"https://discord.com/channels/1007840975726575667/{CH[r[1]]}/{r[0]}"
used=[]
def full(m):
    who,date,url=meta(m.group(1)); used.append(m.group(1)); return f'[{who}, {date}]({url})'
def custom(m):
    used.append(m.group(1)); return '('+meta(m.group(1))[2]+')'
doc=re.sub(r'\[\[([TD]\d+)\]\]', full, doc)
doc=re.sub(r'\(@([TD]\d+)\)', custom, doc)
assert '[[' not in doc and '(@' not in doc and '{{' not in doc

# ---- "Start here" and the table of contents, built from the headings so they cannot drift
DESC = {
 'Introduction': 'The question, and what came out, in seven bullets.',
 'What people asked for': "The gap in the solvers' own words, and the sixteen questions from the server that are answered here.",
 'The data': 'What was computed, and what "optimal" and "in 12" mean.',
 'How much can a read tell you?': "The ceiling: every read against the exact finish. Zagros's two hunches.",
 'The reads, cheapest first': 'What each read is worth, with the tables:',
 'Bounds people use, graded': "Levi's formula, trangium's 2q bound at any qt, HTR length, the parity bound. Which never fail, how often the others do.",
 'Leave slice, the slice, and width': 'What the slice costs, and how many first moves are optimal.',
 'What a computer can prove from the DR': 'Table lookups that prove "no 12" for most 4–5qt DRs, and why no hand read gets there.',
 "What I'd do per subset": '**The one to read.** For each of the 12 corner subsets: how it finishes, what to read, when to drop it, what not to conclude.',
 'The 216 NISS@1qt cases, three ways': "FakeMMAP's and Rodney's tables checked with half turns, with DR moves and with any move.",
 "The proof, if you don't speak Lean": 'What is proven, how, and what you have to trust.',
 'How it was computed and checked': 'The programs, and what agreed with what.',
 "What this doesn't do": 'Limits, and questions left open.',
 'Appendix A: all 48 subsets': 'Share, average, shortest and longest optimal, odds for 12 and 13.',
 'Appendix B: odds by corner length and E-slice parity': 'For the big high-qt subsets.',
 'Appendix C: the 216 NISS@1qt cases': 'Every case with its optimal for half turns, DR moves and any move.',
 'Appendix D: odds by true pairs, all 48 subsets': 'Odds for 12 and 13 by number of pairs.',
 'Appendix E: the 46 corner cases': 'Layout, example scramble, corner solution lengths, odds, and the both-sides tables.',
 'Appendix F: HTR length on both sides, all 48 subsets': 'The square tables.',
 'Appendix G: a scramble for every subset': 'A longest state, and one that finishes in exactly its longer HTR, for each of the 48 subsets.',
 'Docs and sheets referred to': 'Links.',
}
def anchor(h):
    return re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
def words(t):
    t = re.sub(r'\]\(https?://[^)]*\)', ']', t)
    return len(re.findall(r"[A-Za-z0-9%'’.–-]+", t))
parts = re.split(r'(?m)^(?=## )', doc)
head, secs = parts[0], parts[1:]
# the per-subset guide is the section most readers want: it goes first, and everything is renumbered
guide = [x for x in secs if re.match(r"## \d+\. What I'd do per subset", x)]
assert len(guide) == 1
secs.remove(guide[0])
secs.insert([i for i, x in enumerate(secs) if x.startswith('## Introduction')][0] + 1, guide[0])
remap = {}
for x in secs:
    m = re.match(r'## (\d+)\. ', x)
    if m: remap[m.group(1)] = str(len(remap) + 1)
def renumber(t):
    t = re.sub(r'(?m)^## (\d+)\. ', lambda m: f'## {remap[m.group(1)]}. ', t)
    t = re.sub(r'(?m)^### (\d+)\.(\d+) ', lambda m: f'### {remap[m.group(1)]}.{m.group(2)} ', t)
    t = re.sub(r'§(\d+)', lambda m: '§' + remap.get(m.group(1), m.group(1)), t)
    t = re.sub(r'\b([Ss]ections) (\d+)( (?:to|and) )(\d+)', lambda m: f'{m.group(1)} {remap.get(m.group(2), m.group(2))}{m.group(3)}{remap.get(m.group(4), m.group(4))}', t)
    t = re.sub(r'\b([Ss]ection) (\d+)\b', lambda m: f'{m.group(1)} {remap.get(m.group(2), m.group(2))}', t)
    return re.sub(r'\(#(\d+)-', lambda m: '(#' + remap.get(m.group(1), m.group(1)) + '-', t)
secs = [renumber(x) for x in secs]
rows = ['| Section | What is in it | Size |', '|---|---|---|']
for sec in secs:
    title = sec.split('\n', 1)[0][3:].strip()
    key = re.sub(r'^\d+\. ', '', title)
    assert key in DESC, title
    n = words(sec)
    size = 'tables' if title.startswith('Appendix') else 'links' if title.startswith('Docs') else f'{max(50, round(n / 50) * 50):,} words'
    desc = DESC[key]
    if key == 'The reads, cheapest first':
        subs = re.findall(r'(?m)^### (\d+\.\d+ .*)$', sec)
        desc += ' ' + ', '.join(f'[{x}](#{anchor(x)})' for x in subs) + '.'
    rows.append(f'| [{title}](#{anchor(title)}) | {desc} | {size} |')
main = sum(words(s) for s in secs if re.match(r'## (Introduction|[1-8]\. )', s))
start = renumber(open('/data/fmc/judging-a-dr/research/src/report_build/start_here.md').read())
note = f'\nSections 1 to 8 are the main text, about {round(main / 500) * 500:,} words with their tables. The rest is reference.\n\n---\n\n'
assert head.rstrip().endswith('---')
doc = head + start + '\n'.join(rows) + '\n' + note + ''.join(secs)
open(R+'WRITEUP.md','w').write(doc+'\n')
print(len(doc.split('\n')),'lines',len(doc),'bytes; links filled:',len(used))
