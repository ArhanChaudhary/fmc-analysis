#!/usr/bin/env python3
"""Dated links to Discord messages from the short ids of the knowledge base (T = #fmc-theory, D = #fmc-discussion,
N = #non-dr-discussion).  The channel ids are the ones in the export itself (kb/data/messages.jsonl, field channel_id)."""
import sqlite3, datetime, re
CH = {'fmc-theory': '1007841335434285126', 'fmc-discussion': '1007841273111117924', 'non-dr-discussion': '1077216728683135046'}
_db = sqlite3.connect('/data/fmc/kb/kb.sqlite')
def row(sid):
    r = _db.execute('select id, channel, ts, author, content, extras from msg where sid=?', (sid,)).fetchone(); assert r, sid
    return r[:4] + ((r[4] or '') + ' ' + (r[5] or ''),)   # a forwarded message has its text in extras
def link(sid):
    mid, ch, ts, author, content = row(sid); y, mo, d = map(int, ts[:10].split('-'))
    return f"[{d} {datetime.date(y, mo, d).strftime('%b %Y')}](https://discord.com/channels/1007840975726575667/{CH[ch]}/{mid})"
def content(sid): return row(sid)[4]
def author(sid): return row(sid)[3]
def expand(doc, used=None):
    def one(m):
        if used is not None: used.append(m.group(1))
        return link(m.group(1))
    return re.sub(r'\[\[([TDN]\d+)\]\]', one, doc)
