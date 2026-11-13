"""Shared loading code for the route analysis.

Inputs (written by `htrtools routes`, see README):
  out/big/run1/states_<subset>.tsv   one row per sampled state (25,000 per subset)
  out/big/run1/routes_<subset>.bin   per state: u32 count, count x u32 entries for X, then the same for X*R2;
                                     entry = route id << 6 | HTR length << 1 | (finish length - optimum)
  out/big/run1/route_keys.tsv        route id -> key ("H:..." route to HTR, "F:..." labels over the whole finish)
  out/checks/dist48.tsv              exact number of DR states per subset (to pool subsets by their true size)
"""
import os, csv, re, collections, sys
import numpy as np
sys.path.append('/data/fmc/judging-a-dr/research/src')
from pv import hu, exact          # every printed number: an exact half goes up (the first study's rule; xhtfirst.py reads pv too)
HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.normpath(os.path.join(HERE, '..'))
RUN = os.path.join(R, 'out', 'big', 'run1')
OUT = os.path.join(R, 'out')

SUBS = [l.split('\t')[0] for l in open(os.path.join(R, 'out/checks/dist48.tsv')).read().split('\n')[1:] if l]
SUBS = list(dict.fromkeys(SUBS))
SIZE = collections.Counter()
for r in csv.DictReader(open(os.path.join(R, 'out/checks/dist48.tsv')), delimiter='\t'):
    SIZE[r['subset']] += int(r['states'])
CORNER = lambda s: s.split()[0]
CGROUPS = list(dict.fromkeys(CORNER(s) for s in SUBS))

_keys = None
def keys():
    global _keys
    if _keys is None:
        _keys = []
        with open(os.path.join(RUN, 'route_keys.tsv')) as f:
            next(f)
            for l in f:
                i, k = l.rstrip('\n').split('\t')
                _keys.append(k)
    return _keys

def fname(sub): return sub.replace(' ', '_')

def load_states(sub):
    rows = list(csv.DictReader(open(os.path.join(RUN, f'states_{fname(sub)}.tsv')), delimiter='\t'))
    out = {}
    for k in rows[0]:
        v = [r[k] for r in rows]
        try:
            out[k] = np.array([int(x) for x in v], dtype=np.int64)
        except ValueError:
            out[k] = np.array(v)
    return out

class Routes:
    """CSR arrays: for state i, entries ptr[i]:ptr[i+1] of rid / htr / htr1 / delta (X), and vptr / vrid / vhtr / vhtr1 /
    vdelta (X*R2).  Entry (u64) = route id << 11 | htr << 6 | htr1 << 1 | delta, where
      delta  shortest finish following the route minus the optimum (0 or 1)
      htr    shortest HTR among the readings of the route's SHORTEST finishes (at delta = 0: over optimal finishes)
      htr1   shortest HTR among the route's readings of every finish of length <= optimum + 1
    So "works at the optimum with HTR budget b" = delta == 0 and htr <= niss + b; "works within +1 with budget b"
    = htr1 <= niss + b (a +1 finish may have a shorter HTR than the optimal ones)."""
    def __init__(self, sub):
        a = np.fromfile(os.path.join(RUN, f'routes_{fname(sub)}.bin'), dtype='<u8')
        i = 0; ptr = [0]; vptr = [0]; xs = []; vs = []
        n = len(a)
        while i < n:
            c = int(a[i]); xs.append(a[i + 1:i + 1 + c]); i += 1 + c; ptr.append(ptr[-1] + c)
            c = int(a[i]); vs.append(a[i + 1:i + 1 + c]); i += 1 + c; vptr.append(vptr[-1] + c)
        x = np.concatenate(xs).astype(np.int64); v = np.concatenate(vs).astype(np.int64)
        self.ptr = np.array(ptr); self.vptr = np.array(vptr)
        self.rid, self.htr, self.htr1, self.delta = x >> 11, (x >> 6) & 31, (x >> 1) & 31, x & 1
        self.vrid, self.vhtr, self.vhtr1, self.vdelta = v >> 11, (v >> 6) & 31, (v >> 1) & 31, v & 1
        self.n = len(ptr) - 1
        self.state = np.repeat(np.arange(self.n), np.diff(self.ptr))
        self.vstate = np.repeat(np.arange(self.n), np.diff(self.vptr))

# ---------------------------------------------------------------- mirror aliases and the tie-break order
_alias = None
def aliases():
    """route id -> its mirror (the reading of the same split started on the other side); and the set of ids seen as
    normal-first.  From out/big/run1/route_aliases.tsv."""
    global _alias
    if _alias is None:
        mirror = {}; nf = set()
        p = os.path.join(RUN, 'route_aliases.tsv')
        if os.path.exists(p):
            with open(p) as f:
                next(f)
                for l in f:
                    a, b, c = l.split('\t')
                    a, b = int(a), int(b)
                    mirror.setdefault(a, b); mirror.setdefault(b, a); nf.add(a)
        _alias = (mirror, nf)
    return _alias

def tie_rank(name, normal_first_names=frozenset()):
    """deterministic tie-break among classes covering the same states: fewer switches first (linear before NISS),
    then the normal-first member of a mirror pair (the reading a solver writes), then the name"""
    return (0 if '(' not in name else 1, 0 if (name in normal_first_names or '(' not in name) else 1, name)

# ---------------------------------------------------------------- route classes from keys
LAB = re.compile(r'(\d[abc]\d) (\d)e')
def parse_key(k):
    """'H:4b2 4e > 4a1 4e > (0c0 0e) | ht' -> (kind, [labels], switch index or None, post 'ht'/'qt'/None)"""
    kind, body = k.split(':', 1)
    post = None
    if kind == 'H':
        body, post = body.rsplit(' | ', 1)
    parts = body.split(' > ')
    sw = None
    labs = []
    for i, p in enumerate(parts):
        if p.startswith('('):
            sw = i; p = p[1:]
        labs.append(p.rstrip(')'))
    return kind, labs, sw, post

def fmt(labs, sw, post=None, kind=None):
    s = ' > '.join(('(' if sw is not None and i == sw else '') + l for i, l in enumerate(labs))
    if sw is not None: s += ')'
    if post: s += f' | {post}'
    return (kind + ':' if kind else '') + s

def level_of(k, level):
    """The route class of key k at a level:
       'H'  the H key: labels with edges at the start and after each quarter turn up to HTR, the switch, post-HTR in
            half turns (ht) or not (qt)
       'C'  the same without edge counts ("4b2 > 2c3 > (4b2 > 4a1 > 0c0) | ht")
       'Q'  quarter turns on each side only ("3 | ht" linear, "1+(2) | ht" NISS after the first qt)"""
    kind, labs, sw, post = parse_key(k)
    if level == 'H': return k[2:]
    if level == 'C':
        return fmt([l.split()[0] for l in labs], sw, post)
    if level == 'Q':
        q = len(labs) - 1
        if sw is None: return f'{q} | {post}'
        return f'{sw - 1}+({q - sw + 1}) | {post}'
    raise ValueError(level)
