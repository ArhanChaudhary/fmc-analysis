//! HTRs with every face turn: the ones that leave DR on the way (R, L, F, B quarter turns) as well as the DR-move ones.
//!
//! The search runs on the whole cube, pruned by four exact distances of projections of it:
//!
//! * the corners up to renaming by H (the HTR group): their twists (2187) and their corner coset (420), 918,540 in all,
//!   each with the fewest face turns that put the corners in HTR;
//! * the edges' flips on F/B (2048) with the places of one slice's four edges (495), for each of the three slices: the
//!   fewest face turns that make every edge good and bring those four into their slice.
//!
//! In HTR every one of them is 0, and a face turn changes each by at most 1, so their largest is a lower bound on the
//! moves left.  Back in DR, the bound is exact: the fewest face turns from each DR coset to HTR, computed once
//! ([`AllMoves::dr_distances`], kept in `all_dist.bin`).  Near HTR the search knows the moves left exactly: every coset of H within [`AllMoves::radius`] face
//! turns of HTR is listed with its distance (a breadth-first search from HTR), so in the last moves a state that is not
//! close enough is dropped at once.

use attempt_sim::cube::{canonical_after, Cube, Move, MoveTables};
use attempt_sim::dr::{rank_perm, unrank_perm};
use attempt_sim::htr::{Htr, NCCOS, NEPAT};
use std::collections::HashSet;

const NTWIST: usize = 2187;
const NFLIP: usize = 2048;
const NPOS: usize = 495;
/// the pieces of each slice: M (UF UB DF DB), S (UL UR DL DR), E (FR FL BL BR)
const SLICES: [[u8; 4]; 3] = [[0, 2, 4, 6], [1, 3, 5, 7], [8, 9, 10, 11]];

/// The 495 sets of 4 places of 12, in order; and the rank of each (as a 12-bit mask).
fn four_sets() -> (Vec<u16>, Vec<u16>) {
    let sets: Vec<u16> = (0u16..1 << 12).filter(|m| m.count_ones() == 4).collect();
    let mut rank = vec![u16::MAX; 1 << 12];
    for (i, &m) in sets.iter().enumerate() {
        rank[m as usize] = i as u16;
    }
    (sets, rank)
}

/// A node of the search: the projections, and the whole cube for the exact checks.
#[derive(Clone, Copy)]
struct Node {
    corners: u32,
    flip: u16,
    pos: [u16; 3],
}

pub struct AllMoves {
    pub cube: MoveTables,
    twist_mv: Vec<[u16; 18]>,
    ccos_mv: Vec<[u16; 18]>,
    flip_mv: Vec<[u16; 18]>,
    pos_mv: Vec<[u16; 18]>,
    corner_dist: Vec<u8>,
    edge_dist: [Vec<u8>; 3],
    /// the edge permutations of H (6912)
    h_edges: HashSet<[u8; 12]>,
    /// the corner coset of every corner permutation (`Htr::ccos`)
    ccos: Vec<u16>,
    home: [u16; 3],
    solved: Node,
    /// HTR with the E slice turned (U D'), as a projection
    turned: Node,
    pos_rank: Vec<u16>,
    /// the cosets within `radius` face turns of HTR ([`AllMoves::key`]), sorted, and their distances
    near: Vec<u64>,
    near_dist: Vec<u8>,
    pub radius: usize,
    /// the fewest face turns from each DR coset to HTR, when known (else empty)
    dr_dist: Vec<u8>,
    /// the edge pattern of every DR edge permutation (`Htr::epat`)
    epat: Vec<u8>,
}

impl AllMoves {
    pub fn new(htr: &Htr, radius: usize) -> AllMoves {
        let cube = MoveTables::new();
        let (sets, pos_rank) = four_sets();
        let turn = |c: &Cube, m: usize| cube.turn(c, Move(m as u8));

        // the twists: a cube with those twists, turned
        let twist_cube = |t: usize| {
            let mut c = Cube::SOLVED;
            let mut t = t;
            let mut sum = 0;
            for i in 0..7 {
                c.co[i] = (t % 3) as u8;
                sum += c.co[i];
                t /= 3;
            }
            c.co[7] = (3 - sum % 3) % 3;
            c
        };
        let twist_mv: Vec<[u16; 18]> =
            (0..NTWIST).map(|t| std::array::from_fn(|m| turn(&twist_cube(t), m).twist_coord() as u16)).collect();
        // the corner cosets: a representative, turned
        let ccos_mv: Vec<[u16; 18]> = (0..NCCOS)
            .map(|a| {
                let mut c = Cube::SOLVED;
                c.cp = attempt_sim::dr::unrank_perm::<8>(htr.ccos_rep[a]);
                std::array::from_fn(|m| htr.ccos[rank_perm(&turn(&c, m).cp)])
            })
            .collect();
        let flip_cube = |f: usize| {
            let mut c = Cube::SOLVED;
            for i in 0..11 {
                c.eo[i] = (f >> i & 1) as u8;
            }
            c.eo[11] = (f.count_ones() % 2) as u8;
            c
        };
        let flip_mv: Vec<[u16; 18]> =
            (0..NFLIP).map(|f| std::array::from_fn(|m| turn(&flip_cube(f), m).flip_pattern() as u16)).collect();
        // the places of four edges: put four marked pieces there, turn, read where they went
        let pos_mv: Vec<[u16; 18]> = sets
            .iter()
            .map(|&mask| {
                let mut c = Cube::SOLVED;
                for p in 0..12 {
                    c.ep[p] = if mask >> p & 1 == 1 { 0 } else { 1 };
                }
                std::array::from_fn(|m| {
                    let t = turn(&c, m);
                    pos_rank[(0..12).filter(|&p| t.ep[p] == 0).fold(0usize, |a, p| a | 1 << p)]
                })
            })
            .collect();

        let solved_ccos = htr.ccos[rank_perm(&Cube::SOLVED.cp)] as usize;
        let corner_dist = bfs(NTWIST * NCCOS, solved_ccos, |x, m| {
            let (t, a) = (x / NCCOS, x % NCCOS);
            twist_mv[t][m] as usize * NCCOS + ccos_mv[a][m] as usize
        });
        let set_of = |pieces: &[u8; 4]| pos_rank[pieces.iter().fold(0usize, |a, &p| a | 1 << p)];
        let home: [u16; 3] = std::array::from_fn(|k| set_of(&SLICES[k]));
        let edge_dist = std::array::from_fn(|k| {
            bfs(NFLIP * NPOS, home[k] as usize, |x, m| {
                let (f, p) = (x / NPOS, x % NPOS);
                flip_mv[f][m] as usize * NPOS + pos_mv[p][m] as usize
            })
        });

        // the edges of H: every arrangement half turns reach
        let mut h_edges = HashSet::from([Cube::SOLVED.ep]);
        let mut frontier = vec![Cube::SOLVED];
        while let Some(c) = frontier.pop() {
            for face in 0..6 {
                let d = cube.turn(&c, Move::new(face, 2));
                if h_edges.insert(d.ep) {
                    frontier.push(d);
                }
            }
        }
        assert_eq!(h_edges.len(), 6912);

        let mut all = AllMoves {
            cube,
            twist_mv,
            ccos_mv,
            flip_mv,
            pos_mv,
            corner_dist,
            edge_dist,
            h_edges,
            ccos: htr.ccos.clone(),
            home,
            solved: Node { corners: 0, flip: 0, pos: [0; 3] },
            turned: Node { corners: 0, flip: 0, pos: [0; 3] },
            pos_rank,
            near: Vec::new(),
            near_dist: Vec::new(),
            radius,
            dr_dist: Vec::new(),
            epat: htr.epat.clone(),
        };
        all.solved = all.node(&Cube::SOLVED);
        all.turned = all.node(&all.cube.state(&[Move::new(0, 1), Move::new(1, 3)]));

        // the cosets near HTR, by breadth-first search from it
        let mut near: Vec<(u64, u8)> = vec![(all.key(&Cube::SOLVED, &all.solved), 0)];
        let mut seen: HashSet<u64> = HashSet::from([near[0].0]);
        let mut frontier = vec![Cube::SOLVED];
        for r in 1..=radius as u8 {
            let mut next = Vec::new();
            for c in &frontier {
                for m in Move::all() {
                    let d = all.cube.turn(c, m);
                    let k = all.key(&d, &all.node(&d));
                    if seen.insert(k) {
                        near.push((k, r));
                        next.push(d);
                    }
                }
            }
            frontier = next;
        }
        near.sort_unstable();
        (all.near, all.near_dist) = near.into_iter().unzip();
        all
    }

    /// The coset of H a cube is in (renaming its pieces by H leaves it): the corners' coordinate, the flips, the places
    /// of the M and S edges, and the parity of the three slices' pieces read in place order (all three together: H
    /// keeps it).
    fn key(&self, c: &Cube, n: &Node) -> u64 {
        let mut parity = 0u64;
        for slice in SLICES {
            let mut order = [0u8; 4];
            let mut k = 0;
            for &piece in &c.ep {
                if slice.contains(&piece) {
                    order[k] = piece;
                    k += 1;
                }
            }
            for i in 0..4 {
                for j in i + 1..4 {
                    parity ^= (order[i] > order[j]) as u64;
                }
            }
        }
        n.corners as u64 | (n.flip as u64) << 20 | (n.pos[0] as u64) << 31 | (n.pos[1] as u64) << 40 | parity << 49
    }

    /// The face turns from a coset to HTR, if within the radius.
    fn near_distance(&self, c: &Cube, n: &Node) -> Option<u8> {
        self.near.binary_search(&self.key(c, n)).ok().map(|i| self.near_dist[i])
    }

    fn node(&self, c: &Cube) -> Node {
        let set =
            |k: usize| self.pos_rank[(0..12).filter(|&p| SLICES[k].contains(&c.ep[p])).fold(0usize, |a, p| a | 1 << p)];
        Node {
            corners: (c.twist_coord() * NCCOS + self.ccos[rank_perm(&c.cp)] as usize) as u32,
            flip: c.flip_pattern() as u16,
            pos: [set(0), set(1), set(2)],
        }
    }

    fn after(&self, n: &Node, m: Move) -> Node {
        let m = m.index();
        let (t, a) = (n.corners as usize / NCCOS, n.corners as usize % NCCOS);
        Node {
            corners: (self.twist_mv[t][m] as usize * NCCOS + self.ccos_mv[a][m] as usize) as u32,
            flip: self.flip_mv[n.flip as usize][m],
            pos: std::array::from_fn(|k| self.pos_mv[n.pos[k] as usize][m]),
        }
    }

    /// Use the fewest face turns from each DR coset to HTR ([`AllMoves::dr_distances`]) as the bound in DR.
    pub fn with_dr_distances(mut self, dr_dist: Vec<u8>) -> AllMoves {
        self.dr_dist = dr_dist;
        self
    }

    /// A lower bound on the face turns left to HTR (exact in DR, once the DR distances are known).
    fn bound(&self, c: &Cube, n: &Node) -> u8 {
        let in_dr = n.corners as usize / NCCOS == 0 && n.flip == 0 && n.pos[2] == self.home[2];
        if in_dr && !self.dr_dist.is_empty() {
            return self.dr_dist[self.dr_coset(c, n)];
        }
        let e = |k: usize| self.edge_dist[k][n.flip as usize * NPOS + n.pos[k] as usize];
        self.corner_dist[n.corners as usize].max(e(0)).max(e(1)).max(e(2))
    }

    /// The DR coset (`Cosets` numbering) of a cube in DR.
    fn dr_coset(&self, c: &Cube, n: &Node) -> usize {
        n.corners as usize % NCCOS * NEPAT + self.epat[rank_perm(&c.ep[..8])] as usize
    }

    /// A cube in a DR coset (`Cosets` numbering): its corner coset's and edge pattern's representatives, with two
    /// E-slice edges swapped if that is what makes it a cube one can hold (DR leaves their order free).
    pub fn dr_cube(htr: &Htr, coset: usize) -> Cube {
        let mut c = Cube::SOLVED;
        c.cp = unrank_perm::<8>(htr.ccos_rep[coset / NEPAT]);
        c.ep[..8].copy_from_slice(&unrank_perm::<8>(htr.epat_rep[coset % NEPAT]));
        let odd = |p: &[u8]| {
            (0..p.len()).flat_map(|i| (i + 1..p.len()).map(move |j| (i, j))).filter(|&(i, j)| p[i] > p[j]).count() % 2
        };
        if odd(&c.cp) != odd(&c.ep) {
            c.ep.swap(8, 9);
        }
        c
    }

    /// The fewest face turns from every DR coset to HTR, each no more than with DR moves (`dr_dist`): what
    /// `all_dist.bin` keeps.  (About 15 seconds.)
    pub fn dr_distances(&self, htr: &Htr, dr_dist: &[u8]) -> Vec<u8> {
        (0..dr_dist.len())
            .map(|x| {
                let c = AllMoves::dr_cube(htr, x);
                if self.in_htr(&c) {
                    0
                } else {
                    self.distance(&c, dr_dist[x] as usize).expect("no further than with DR moves") as u8
                }
            })
            .collect()
    }

    /// Is the whole cube in H (HTR)?
    pub fn in_htr(&self, c: &Cube) -> bool {
        let n = self.node(c);
        n.corners == self.solved.corners && c.eo == [0; 12] && self.h_edges.contains(&c.ep)
    }

    /// In HTR with the E slice turned a quarter (U D' from HTR)?
    pub fn in_turned_htr(&self, c: &Cube) -> bool {
        self.in_htr(&self.cube.apply(c, &[Move::new(1, 1), Move::new(0, 3)]))
    }

    fn could_be(&self, n: &Node, target: &Node) -> bool {
        n.corners == target.corners && n.flip == 0 && n.pos == target.pos
    }

    /// Every sequence of at most `max_len` face turns that takes `start` to HTR: canonical (no face twice in a row,
    /// of opposite faces the lower first), in HTR at its end and not before, nor in HTR with the E slice turned before
    /// its end, and with only quarter turns, all clockwise, in its last block (the last turn, or the last two if they
    /// are on one axis).  `start` must not be in HTR.
    pub fn solutions(&self, start: &Cube, max_len: usize) -> Vec<Vec<Move>> {
        let mut out = Vec::new();
        let mut path = Vec::with_capacity(max_len);
        self.search(start, &self.node(start), max_len, &mut path, &mut out);
        out
    }

    fn search(&self, c: &Cube, n: &Node, budget: usize, path: &mut Vec<Move>, out: &mut Vec<Vec<Move>>) {
        if !path.is_empty() {
            if self.could_be(n, &self.solved) && c.eo == [0; 12] && self.h_edges.contains(&c.ep) {
                let k = path.len();
                let block = if k >= 2 && path[k - 2].axis() == path[k - 1].axis() { 2 } else { 1 };
                if path[k - block..].iter().all(|m| m.quarter_turns() == 1) {
                    out.push(path.clone());
                }
                return;
            }
            if self.could_be(n, &self.turned) && self.in_turned_htr(c) {
                return;
            }
        }
        if !self.close_enough(c, n, budget) {
            return;
        }
        for m in Move::all() {
            if canonical_after(path.last().copied(), m) {
                path.push(m);
                self.search(&self.cube.turn(c, m), &self.after(n, m), budget - 1, path, out);
                path.pop();
            }
        }
    }

    /// Could HTR be `budget` face turns away or less?
    fn close_enough(&self, c: &Cube, n: &Node, budget: usize) -> bool {
        if self.bound(c, n) as usize > budget {
            return false;
        }
        budget > self.radius || self.near_distance(c, n).is_some_and(|d| d as usize <= budget)
    }

    /// The fewest face turns from `start` to HTR, if at most `max_len`.
    pub fn distance(&self, start: &Cube, max_len: usize) -> Option<usize> {
        let n = self.node(start);
        if let Some(d) = self.near_distance(start, &n) {
            return (d as usize <= max_len).then_some(d as usize);
        }
        (self.radius + 1..=max_len).find(|&len| self.exists(start, &n, len, None))
    }

    fn exists(&self, c: &Cube, n: &Node, budget: usize, last: Option<Move>) -> bool {
        if !self.close_enough(c, n, budget) {
            return false;
        }
        if budget <= self.radius {
            return true; // close enough is exact here
        }
        Move::all()
            .filter(|&m| canonical_after(last, m))
            .any(|m| self.exists(&self.cube.turn(c, m), &self.after(n, m), budget - 1, Some(m)))
    }
}

/// Breadth-first distances from `start` over the 18 face turns (`next(x, m)`), as bytes.
fn bfs(size: usize, start: usize, next: impl Fn(usize, usize) -> usize) -> Vec<u8> {
    let mut d = vec![u8::MAX; size];
    d[start] = 0;
    let mut frontier = vec![start];
    let mut depth = 0;
    while !frontier.is_empty() {
        depth += 1;
        let mut nextf = Vec::new();
        for &x in &frontier {
            for m in 0..18 {
                let y = next(x, m);
                if d[y] == u8::MAX {
                    d[y] = depth;
                    nextf.push(y);
                }
            }
        }
        frontier = nextf;
    }
    d
}

/// The form of a sequence up to the E slice: with the E slice ignored, a D turn is the U turn the same way with the cube
/// turned a quarter with it, so each D turn is written as a U turn and the faces after it are moved round (R to F, F to
/// L, L to B, B to R); then turns of one face are merged and opposite faces put in order.  Two HTRs with the same
/// form are listed once.  (As `cosets::modulo_e`, for every face turn.)
pub fn modulo_e(path: &[Move]) -> Vec<(u8, u8)> {
    // the face a side face becomes after one D quarter turn (U and D unused)
    const NEXT: [u8; 6] = [0, 1, 4, 5, 3, 2];
    let mut turned = 0u8;
    let mut out: Vec<(u8, u8)> = Vec::with_capacity(path.len());
    for &m in path {
        let (face, quarters) = (m.face() as u8, m.quarter_turns() as u8);
        let face = match face {
            0 => 0,
            1 => {
                turned = (turned + quarters) % 4;
                0
            }
            _ => (0..turned).fold(face, |f, _| NEXT[f as usize]),
        };
        // merge with the last turn of the same face, looking past a turn of the opposite face
        let mut j = out.len();
        let mut merged = false;
        while j > 0 {
            let (f, q) = out[j - 1];
            if f == face {
                let total = (q + quarters) % 4;
                if total == 0 {
                    out.remove(j - 1);
                } else {
                    out[j - 1].1 = total;
                }
                merged = true;
                break;
            }
            if face == 0 || f / 2 != face / 2 {
                break;
            }
            j -= 1;
        }
        if !merged {
            out.push((face, quarters));
        }
    }
    for i in 1..out.len() {
        let (f, g) = (out[i - 1].0, out[i].0);
        if f != 0 && f / 2 == g / 2 && g < f {
            out.swap(i - 1, i);
        }
    }
    out
}
