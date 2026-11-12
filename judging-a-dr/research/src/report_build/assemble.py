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
howgood = howgood[:howgood.index('### Throwing DRs away')].rstrip('\n')     # the by-target version is throwing.md
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

front=open('/data/fmc/judging-a-dr/research/src/report_build/new_front.md').read().rstrip('\n')
front=front.replace('{{CORNER_SECTION}}', open('/data/fmc/judging-a-dr/research/src/report_build/corner_section.md').read().rstrip('\n'))
tail=open('/data/fmc/judging-a-dr/research/src/report_build/new_tail.md').read()
def data(name): return open(R+'data/'+name).read().strip('\n')
B='/data/fmc/judging-a-dr/research/src/report_build/'
doc = (front + '\n\n### The seven levels\n\n' + levels + '\n\n' + howgood + '\n\n' + open(B+'throwing.md').read().rstrip('\n') + '\n\n### Examples\n\n' + examples + '\n\n'
       + tail.replace('{{C216}}', c216).replace('{{PROOF}}', proof).replace('{{HOW}}', how)
              .replace('{{APPA}}', data('appendix_a.md')).replace('{{APPB}}', data('appendix_b.md')).replace('{{APPC}}', appC).replace('{{GUIDE}}', open(B+'guide.md').read().rstrip('\n'))
              .replace('{{PAIRS}}', data('odds_by_true_pairs.md')).replace('{{CORNERS}}', data('corner_cases.md'))
              .replace('{{SQUARES}}', data('htr_square_tables.md')).replace('{{WITNESSES}}', data('witnesses_by_subset.md')).replace('{{DOCS}}', docs))

for name, f in (('PIV_BASE', 'pivots_base.md'), ('PIV_RANK', 'pivots_rank.md'), ('PIV_DROP', 'pivots_drop.md'), ('PIV_DEAD', 'pivots_dead.md'), ('PIV_RULES', 'pivots_rules.md'),
                ('PIV_PAIR_RULES', 'pivots_pair_rules.md'), ('PIV_BOUNDS', 'pivots_bounds.md'), ('PIV_LASTMOVE', 'pivots_lastmove.md'), ('PIV_FULL', 'pivots_full.md'),
                ('PIV_LADDER_SUBSETS', 'pivots_ladder_subsets.md'), ('PIV_LADDER', 'pivots_ladder.md'), ('PIV_COMPARE', 'pivots_compare.md'),
                ('PIV_HTR', 'pivots_htr.md'), ('MAIN_PAIRS', 'main_pairs.md'), ('MAIN_SQUARES', 'main_squares.md'), ('MAIN_ZAGROS', 'main_zagros.md')):
    assert doc.count('{{' + name + '}}') == 1, name
    doc = doc.replace('{{' + name + '}}', data(f))
# numbers written as {= expression =} in the sources are computed from the census
import sys
sys.path.insert(0, B); sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
import fillenv, pv
doc = pv.fill(doc, fillenv.ENV)
assert '{=' not in doc

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

# ---- "How to read it" and the table of contents, built from the headings so they cannot drift
DESC = {
 'The short version': 'What is new, then what it confirms or corrects, one line each.',
 'What people asked for': "How this started, the gap in the solvers' own words, the sixteen questions from the server that are answered here, and which finish matters.",
 'The data': 'What was computed, and what "optimal" and "in 11" mean.',
 'How much can a read tell you?': "Every read against the exact finish, for each finish you might need from 9 to 13: ranking, throwing away, plain rules with their price, what is proven. Zagros's two hunches.",
 'The reads, cheapest first': 'What each read is worth, with the tables:',
 'Bounds people use, graded': "Levi's formula, trangium's 2q bound at any qt, HTR length, the parity bound. Which never fail, how often the others do.",
 'Leave slice, the slice, and width': 'What the slice costs, and how many first moves are optimal.',
 'What a computer can prove from the DR': 'Table lookups that prove "no 12" for most 4–5qt DRs and "no 11" for nearly all, and why no hand read gets there.',
 "What I'd do per subset": '**The reference to keep open.** For each of the 12 corner subsets: how often it finishes in 10, 11 and 12, what to read, when to drop it for the finish you need, what not to conclude.',
 'The 216 NISS@1qt cases, three ways': "FakeMMAP's and Rodney's tables checked with half turns, with DR moves and with any move.",
 "The proof, if you don't speak Lean": 'What is proven, how, and what you have to trust.',
 'How it was computed and checked': 'The programs, and what agreed with what.',
 "What this doesn't do": 'Limits, and questions left open.',
 'Appendix A: all 48 subsets': 'Share, average, fastest and longest optimal, odds for 9 to 13, and what is proven per subset.',
 'Appendix B: odds by corner length and E-slice parity': 'For the big high-qt subsets.',
 'Appendix C: the 216 NISS@1qt cases': 'Every case with its optimal for half turns, DR moves and any move.',
 'Appendix D: odds by true pairs, all 48 subsets': 'Odds for 10, 11, 12 and 13 by number of pairs.',
 'Appendix E: the 46 corner cases': 'Layout, example scramble, corner solution lengths, odds for 10 to 13, and the both-sides tables.',
 'Appendix F: HTR length on both sides, all 48 subsets': 'Odds for 10 to 13 for every pair of HTR lengths.',
 'Appendix H: every read at every target': 'Ranking and pruning power of each read, for a finish in 9, 10, 11, 12 or 13.',
 'Appendix G: a scramble for every subset': 'A longest state, and one that finishes in exactly its longer HTR, for each of the 48 subsets.',
 'Docs and sheets referred to': 'Links.',
}
def anchor(h):
    return re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
parts = re.split(r'(?m)^(?=## )', doc)
head, secs = parts[0], parts[1:]
# the per-subset guide is the section most readers want: it goes first, and everything is renumbered
guide = [x for x in secs if re.match(r"## \d+\. What I'd do per subset", x)]
assert len(guide) == 1
secs.remove(guide[0])
secs.insert([i for i, x in enumerate(secs) if x.startswith('## 0. The short version')][0] + 1, guide[0])
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
rows = ['| Section | What is in it |', '|---|---|']
for sec in secs:
    title = sec.split('\n', 1)[0][3:].strip()
    key = re.sub(r'^\d+\. ', '', title)
    assert key in DESC, title
    desc = DESC[key]
    if key == 'The reads, cheapest first':
        subs = re.findall(r'(?m)^### (\d+\.\d+ .*)$', sec)
        desc += ' ' + ', '.join(f'[{x}](#{anchor(x)})' for x in subs) + '.'
    rows.append(f'| [{title}](#{anchor(title)}) | {desc} |')
start = renumber(open('/data/fmc/judging-a-dr/research/src/report_build/start_here.md').read())
assert not head.rstrip().endswith('---')
doc = renumber(head).rstrip('\n') + '\n\n' + start.strip('\n') + '\n\n---\n\n' + '\n'.join(rows) + '\n\n---\n\n' + ''.join(secs)
open(R+'WRITEUP.md','w').write(doc+'\n')
print(len(doc.split('\n')),'lines',len(doc),'bytes; links filled:',len(used))
