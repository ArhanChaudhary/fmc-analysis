#!/usr/bin/env python3
"""Write the site's search index: every listed page cut into its sections (h1-h3 with an id), as plain text.

usage: scripts/search-index.py SITE_DIRECTORY STUDY_FOLDER...   (the studies to index: the listed ones, not UNLISTED)

Output: SITE_DIRECTORY/search-index.json, a list of {"u": url with #section, "p": page title, "k": kind of page,
"s": section heading, "t": section text}.  The search page (site/search.js) loads it on first use.  Only the
standard library, so the GitHub Pages build needs nothing more than pandoc and python3."""
import html.parser, json, os, re, sys

KIND = {'index.html': 'Write-up', 'examples.html': 'Examples', 'errata.html': 'Errata'}


class Sections(html.parser.HTMLParser):
    """Collect the text of <main>, cut at every heading that has an id."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_main = 0          # depth inside <main>
        self.skip = 0             # inside <script>, <style>, or KaTeX's hidden copies
        self.heading = None       # (id, [text]) while inside a heading
        self.title = ''
        self.in_title = False
        self.sections = [['', '', []]]   # [id, heading text, [text pieces]]

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'main':
            self.in_main += 1
            return
        if not self.in_main:
            return
        if tag in ('script', 'style') or 'katex-mathml' in (a.get('class') or ''):
            self.skip += 1
            return
        if tag in ('h1', 'h2', 'h3') and 'title' not in (a.get('class') or ''):
            self.heading = (a.get('id', ''), [])
        if tag in ('p', 'li', 'td', 'th', 'br', 'pre', 'tr', 'div', 'summary', 'blockquote'):
            self.sections[-1][2].append(' ')

    def handle_endtag(self, tag):
        if tag == 'main':
            self.in_main -= 1
            return
        if not self.in_main:
            return
        if tag in ('script', 'style') and self.skip:
            self.skip -= 1
            return
        if tag in ('h1', 'h2', 'h3') and self.heading is not None:
            hid, words = self.heading
            self.heading = None
            text = ' '.join(''.join(words).split())
            if hid:
                self.sections.append([hid, text, []])
            else:
                self.sections[-1][2].append(' ' + text + ' ')

    def handle_data(self, data):
        if not self.in_main or self.skip:
            return
        if self.heading is not None:
            self.heading[1].append(data)
        else:
            self.sections[-1][2].append(data)


class Title(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.on = False
        self.text = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'h1' and 'title' in (dict(attrs).get('class') or ''):
            self.on = True

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.on = False

    def handle_data(self, data):
        if self.on:
            self.text += data


def katex_free(s):
    # KaTeX renders math in the browser from \( ... \) spans; keep the TeX source readable for searching
    return s.replace('\\(', '').replace('\\)', '')


def index_page(site, rel, kind, entries):
    raw = open(os.path.join(site, rel), encoding='utf-8').read()
    t = Title()
    t.feed(raw)
    page = ' '.join(t.text.split())
    p = Sections()
    p.feed(raw)
    for hid, head, pieces in p.sections:
        text = ' '.join(katex_free(''.join(pieces)).split())
        if not text and not head:
            continue
        url = rel.replace('index.html', '') + ('#' + hid if hid else '')
        entries.append({'u': url, 'p': page, 'k': kind, 's': head or page, 't': text})


def main():
    site, studies = sys.argv[1], sys.argv[2:]
    entries = []
    for study in studies:
        for name, kind in KIND.items():
            if os.path.exists(os.path.join(site, study, name)):
                index_page(site, f'{study}/{name}', kind, entries)
    if os.path.exists(os.path.join(site, 'decision-cards.html')):
        index_page(site, 'decision-cards.html', 'Decision cards', entries)
    tables = os.path.join(site, 'tables')
    if os.path.isdir(tables):
        for name in sorted(os.listdir(tables)):
            if name.endswith('.html'):
                index_page(site, f'tables/{name}', 'Reference table', entries)
    json.dump(entries, open(os.path.join(site, 'search-index.json'), 'w', encoding='utf-8'), ensure_ascii=False,
              separators=(',', ':'))
    size = os.path.getsize(os.path.join(site, 'search-index.json'))
    print(f'search index: {len(entries)} sections from {len(studies)} studies and the tables, {size / 1e6:.1f} MB')


if __name__ == '__main__':
    main()
