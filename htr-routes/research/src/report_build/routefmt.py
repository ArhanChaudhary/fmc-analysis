"""Route notation on the pages.

The data and the sources write a route as `4b2 > 2c3 > (4b2 > 4a1 > 0c0)`. The pages print it with spaces only,
`4b2 2c3 (4b2 4a1 0c0)`: one name per state, the bracket where the NISS switch is. A route with edge counts at every
step, `2c3 2e > 4b2 2e > 4a1 4e > 0c0`, keeps a separator between states (a name and its edge count are already two
words) and prints as `2c3 2e → 4b2 2e → 4a1 4e → 0c0`.

Code spans and fenced code blocks are rewritten when the whole span is a route. In plain text a run of states joined
by ` > ` (states may also be HTR or `(...)`) is rewritten too, except inside double quotes (quoted messages) and in
blockquotes, so what members wrote stays as they wrote it."""
import re

_STATE = r'\(?\d[a-c]\d(?: \de)?\)?'
_ROUTE = re.compile(rf'^{_STATE}(?: > {_STATE})+(?: \\?\| (?:qt|ht))?$')
_EDGE = re.compile(r'\d[a-c]\d \de')


def route(s):
    """One route in page notation; anything that is not a route is returned unchanged."""
    if not _ROUTE.match(s.strip()):
        return s
    return s.replace(' > ', ' → ' if _EDGE.search(s) else ' ')


def _line(line):
    # a whole code-block line may hold a route followed by a // comment
    head, sep, tail = line.partition('  //')
    return route(head.rstrip()) + head[len(head.rstrip()):] + sep + tail if _ROUTE.match(head.strip()) else line


_PSTATE = r'\(*(?:\d[a-c]\d(?: \de)?|HTR|\.\.\.)\)*'
_PLAIN = re.compile(rf'{_PSTATE}(?: > {_PSTATE})+')


def _plain(segment):
    return _PLAIN.sub(lambda m: m.group(0).replace(' > ', ' → ' if _EDGE.search(m.group(0)) else ' '), segment)


def _prose(line):
    if line.startswith('>'):
        return line
    # split off code spans and double-quoted stretches; rewrite only the rest
    parts = re.split(r'(`[^`\n]+`|"[^"\n]*"|“[^”\n]*”)', line)
    return ''.join(p if i % 2 else _plain(p) for i, p in enumerate(parts))


def page(text):
    out, fenced = [], False
    for line in text.split('\n'):
        if line.startswith('```'):
            fenced = not fenced
            out.append(line)
        elif fenced:
            out.append(_line(line))
        else:
            line = _prose(line)
            out.append(re.sub(r'`([^`\n]+)`', lambda m: '`' + route(m.group(1)) + '`', line))
    return '\n'.join(out)
