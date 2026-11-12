#!/usr/bin/env python3
"""How a member of the server is named in the pages.

The export gives each message a display name and a username.  The display name is what the pages print, without a
trailing status (results, a WCA id, a mood), except where the display name is not a name at all: a status line, or a
line about somebody else.  Those are printed by username.  Two of them are tributes to each other, so going by the
display name would attribute each one's messages to the other."""
import re
BY_USERNAME = {                                   # display name in the export -> what is printed (the username)
    'Brandon is my goat 🐐': 'tave_789',
    'TAVE IS DEFINITELY MY GOAT 🐐': 'bvcuber13',
    'EG-1 grind? (34/40) PR 1.92/2.65': 'jisu101',          # username `jisu101.` in the export
}
SAME_PERSON = {'Yura Riabov': 'Yurii Riabov (Yura)'}        # the author of the Hitchhiker's Guide, as the guide spells the name
def shown(display):
    """The printed name for a display name of the export (or of the reading notes, which add a remark after it)."""
    if display in BY_USERNAME: return BY_USERNAME[display]
    name = re.split(r' \| | \(| // ', display)[0].strip()
    name = re.sub(r' \d{4}[A-Z]{4}\d{2}$', '', name)                   # a WCA id after the name
    return SAME_PERSON.get(name, name)
if __name__ == '__main__':
    import sqlite3
    db = sqlite3.connect('/data/fmc/kb/kb.sqlite')
    for d, u in db.execute('select distinct author, username from msg'):
        if shown(d) != d and d in BY_USERNAME: print(repr(d), '->', shown(d), '(username', u + ')')
