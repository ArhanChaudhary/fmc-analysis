"""All eight corners with the 18 face turns, for the few claims that use D, L or B turns (the study itself holds
DBL fixed).  A piece is its home place (x, y, z); a state maps each piece to (where it is, where its three
stickers face).  Built from rotations, like cube.rs."""
import itertools

PLACES = [(x, y, z) for x in (1, -1) for y in (1, -1) for z in (1, -1)]
FACE = {"R": (0, 1), "L": (0, -1), "U": (1, 1), "D": (1, -1), "F": (2, 1), "B": (2, -1)}


def rot(axis, v, sign):
    """A quarter turn of the face on the `sign` side of `axis`, clockwise seen from outside that face."""
    x, y, z = v
    if axis == 0:
        w = (x, z, -y)
    elif axis == 1:
        w = (-z, y, x)
    else:
        w = (y, -x, z)
    if sign < 0:               # clockwise seen from the other side is the opposite rotation
        for _ in range(2):
            x, y, z = w
            w = (x, z, -y) if axis == 0 else (-z, y, x) if axis == 1 else (y, -x, z)
    return w


def solved():
    return {p: (p, ((p[0], 0, 0), (0, p[1], 0), (0, 0, p[2]))) for p in PLACES}


def turn(state, name):
    axis, sign = FACE[name[0]]
    times = {"": 1, "2": 2, "'": 3}[name[1:].replace("’", "'")]
    for _ in range(times):
        new = {}
        for piece, (at, facing) in state.items():
            if at[axis] == sign:
                new[piece] = (rot(axis, at, sign), tuple(rot(axis, f, sign) for f in facing))
            else:
                new[piece] = (at, facing)
        state = new
    return state


def apply(seq, state=None):
    state = state or solved()
    for name in seq.split():
        state = turn(state, name)
    return state


def placement(state):
    return tuple(state[p][0] for p in PLACES)


def key(state):
    return tuple(state[p] for p in PLACES)


def dr_corner_search():
    """Fewest U, D, R2, L2, F2, B2 turns to solve the corners, for all 40,320 placements; and to the half-turn
    group.  Returns (distance to solved, distance to HTR), dicts keyed by placement."""
    names = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
    # each turn as a map on places
    maps = []
    for n in names:
        s = turn(solved(), n)
        maps.append({p: s[p][0] for p in PLACES})

    def step(pl, m):
        return tuple(m[a] for a in pl)

    def bfs(sources):
        dist = {s: 0 for s in sources}
        frontier = list(sources)
        while frontier:
            nxt = []
            for pl in frontier:
                for m in maps:
                    q = step(pl, m)
                    if q not in dist:
                        dist[q] = dist[pl] + 1
                        nxt.append(q)
            frontier = nxt
        return dist

    start = placement(solved())
    half = {start}
    stack = [start]
    while stack:
        pl = stack.pop()
        for i in (1, 4, 6, 7, 8, 9):
            q = step(pl, maps[i])
            if q not in half:
                half.add(q)
                stack.append(q)
    return bfs([start]), bfs(sorted(half)), half


if __name__ == "__main__":
    a, b = apply("R"), apply("D2 L2 U' L2 D2")
    print("R and [D2 L2 : U'] place the corners alike:", placement(a) == placement(b))
    ds, dh, half = dr_corner_search()
    print(len(ds), "placements; half-turn group", len(half))
    print("longest corner solution in DR turns:", max(ds.values()), " longest to HTR:", max(dh.values()))
    del itertools
