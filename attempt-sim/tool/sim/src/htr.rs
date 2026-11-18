//! HTR cosets of the DR group and the community's HTR subset labels (`4b2 4e`), computed from scratch.
//!
//! H = `<U2, D2, R2, L2, F2, B2>` is the HTR group.  A right coset H·g is the state g up to renaming pieces by an HTR
//! element: exactly what survives when you only look at which pieces are bad.  There are 420 corner cosets × 70 edge
//! patterns.
//!
//! * A *bad corner* sits in a position of the other tetrad (the tetrads are the orbits of corner positions under half
//!   turns); a *bad edge* is an M-slice edge (UF UB DF DB) in an S-slice position (UL UR DL DR) or the other way.
//! * Bad pieces are counted in the frame with few of them ("4c2e = 4c6e"): renaming every piece by U D' turns n bad
//!   corners into 8 - n and n bad edges into 8 - n.
//! * `NcQ`: N bad corners in that frame, Q = fewest quarter turns that bring the corners into H (or into (U D')·H);
//!   `4a` / `4b`: the four bad corners can / cannot be put on one face with half turns (only for Q <= 2 and Q = 5).
//! * The 48 subsets are Mallard's (cubelib): the cosets merged under half turns on the right, U D' on the left and
//!   inversion.

use crate::dr::{rank_perm, unrank_perm, DrTables, St, HALF_MOVES, MOVE_IS_QUARTER, NC, NE, NMOVES};

pub const NCCOS: usize = 420;
pub const NEPAT: usize = 70;

/// The corner subsets, in the order the route keys number them.
pub const SUBSET_NAMES: [&str; 14] =
    ["0c0", "4a1", "4a2", "4b2", "0c3", "2c3", "4a3", "4b3", "0c4", "2c4", "4a4", "4b4", "2c5", "4b5"];

const UNSET: u8 = 0xFF;

/// Index into [`SUBSET_NAMES`] for (bad corners 0/2/4, quarter-turn count, 4a = 0 / 4b = 1).
fn subset_index(bad: u8, qt: u8, shape: u8) -> Option<u8> {
    let table: &[(u8, u8)] = match (bad, shape) {
        (0, _) => &[(0, 0), (3, 4), (4, 8)],
        (2, _) => &[(3, 5), (4, 9), (5, 12)],
        (_, 0) => &[(1, 1), (2, 2), (3, 6), (4, 10)],
        _ => &[(2, 3), (3, 7), (4, 11), (5, 13)],
    };
    table.iter().find(|&&(q, _)| q == qt).map(|&(_, i)| i)
}

pub struct Htr {
    /// corner coordinate -> corner coset; edge coordinate -> edge pattern
    pub ccos: Vec<u16>,
    pub epat: Vec<u8>,
    pub ccos_rep: Vec<usize>,
    pub epat_rep: Vec<usize>,
    pub ccos_mv: Vec<[usize; NMOVES]>,
    pub epat_mv: Vec<[usize; NMOVES]>,
    /// `htr_dist[a][b]`: fewest DR moves to HTR
    pub htr_dist: Vec<[u8; NEPAT]>,
    /// the corner subset of each corner coset (index into [`SUBSET_NAMES`]) and the bad edges of each pattern
    pub cc_subset: Vec<u8>,
    pub cc_bad: Vec<u8>,
    pub ep_bad: Vec<u8>,
    /// Mallard's subset (0..48) of each coset, and its name (`4a1 2e`)
    pub sub48: Vec<[u8; NEPAT]>,
    pub sub48_names: Vec<String>,
    /// route label of each coset: corner subset * 5 + bad edges / 2, in the frame with few bad pieces
    label: Vec<[u8; NEPAT]>,
    c0: usize,
    e0: usize,
    /// corner-only and edge-only lower bounds for [`Htr::niss_htr`]
    corner_bound: Vec<u8>,
    edge_bound: Vec<u8>,
}

impl Htr {
    pub fn new(dr: &DrTables) -> Htr {
        // the HTR corner group: corner permutations reachable with half turns (96)
        let mut hc: Vec<usize> = vec![0];
        let mut seen = vec![false; NC];
        seen[0] = true;
        let mut head = 0;
        while head < hc.len() {
            let c = hc[head];
            head += 1;
            for &m in &HALF_MOVES {
                let d = dr.cmove[m][c] as usize;
                if !seen[d] {
                    seen[d] = true;
                    hc.push(d);
                }
            }
        }
        assert_eq!(hc.len(), 96);

        // right cosets H·c: relabel the pieces of c by every h in H
        let mut ccos = vec![u16::MAX; NC];
        let mut ccos_rep = Vec::with_capacity(NCCOS);
        let hp: Vec<[u8; 8]> = hc.iter().map(|&h| unrank_perm::<8>(h)).collect();
        for c in 0..NC {
            if ccos[c] != u16::MAX {
                continue;
            }
            let p = unrank_perm::<8>(c);
            let n = ccos_rep.len() as u16;
            ccos_rep.push(c);
            for h in &hp {
                let r: [u8; 8] = std::array::from_fn(|k| h[p[k] as usize]);
                ccos[rank_perm(&r)] = n;
            }
        }
        assert_eq!(ccos_rep.len(), NCCOS);

        // edge patterns: which positions hold M-slice pieces (pieces 0, 2, 4, 6)
        let mut epat = vec![0u8; NE];
        let mut epat_rep = Vec::with_capacity(NEPAT);
        let mut epat_mask: Vec<usize> = Vec::with_capacity(NEPAT);
        let mut index_of_mask: [Option<u8>; 256] = [None; 256];
        for e in 0..NE {
            let p = unrank_perm::<8>(e);
            let mask = (0..8).filter(|&k| p[k].is_multiple_of(2)).fold(0usize, |m, k| m | 1 << k);
            epat[e] = *index_of_mask[mask].get_or_insert_with(|| {
                epat_rep.push(e);
                epat_mask.push(mask);
                (epat_rep.len() - 1) as u8
            });
        }
        assert_eq!(epat_rep.len(), NEPAT);
        // a bad edge: an M-slice piece in an S-slice (odd) position; as many S pieces are then misplaced
        let ep_bad: Vec<u8> = epat_mask.iter().map(|&mask| 2 * (mask & 0b1010_1010).count_ones() as u8).collect();

        let ccos_mv: Vec<[usize; NMOVES]> =
            (0..NCCOS).map(|i| std::array::from_fn(|m| ccos[dr.cmove[m][ccos_rep[i]] as usize] as usize)).collect();
        let epat_mv: Vec<[usize; NMOVES]> =
            (0..NEPAT).map(|i| std::array::from_fn(|m| epat[dr.emove[m][epat_rep[i]] as usize] as usize)).collect();
        let (c0, e0) = (ccos[0] as usize, epat[0] as usize);

        // DR -> HTR distance: breadth-first over the 420 x 70 cosets
        let mut htr_dist = vec![[UNSET; NEPAT]; NCCOS];
        htr_dist[c0][e0] = 0;
        let mut queue = vec![(c0, e0)];
        let mut head = 0;
        while head < queue.len() {
            let (a, b) = queue[head];
            head += 1;
            for m in 0..NMOVES {
                let (a2, b2) = (ccos_mv[a][m], epat_mv[b][m]);
                if htr_dist[a2][b2] == UNSET {
                    htr_dist[a2][b2] = htr_dist[a][b] + 1;
                    queue.push((a2, b2));
                }
            }
        }
        assert_eq!(queue.len(), NCCOS * NEPAT);

        // renaming by U D' (it normalises H, so it acts on cosets from the left)
        let x = St::ID.apply_move(0).apply_move(5);
        let lmul_c: Vec<usize> = (0..NCCOS).map(|i| ccos[rank_perm(&x.then(St::unrank(ccos_rep[i], 0, 0)).c)] as usize).collect();
        let lmul_e: Vec<usize> = (0..NEPAT).map(|i| epat[rank_perm(&x.then(St::unrank(0, epat_rep[i], 0)).e)] as usize).collect();

        // quarter turns of the corners to HTR: half turns cost 0, quarter turns 1, targets H and (U D')·H
        let mut cc_qt = vec![UNSET; NCCOS];
        cc_qt[c0] = 0;
        cc_qt[lmul_c[c0]] = 0;
        for d in 0..12u8 {
            let mut changed = true;
            while changed {
                changed = false;
                for i in 0..NCCOS {
                    if cc_qt[i] == d {
                        for &m in &HALF_MOVES {
                            let j = ccos_mv[i][m];
                            if cc_qt[j] > d {
                                cc_qt[j] = d;
                                changed = true;
                            }
                        }
                    }
                }
            }
            for i in 0..NCCOS {
                if cc_qt[i] == d {
                    for m in (0..NMOVES).filter(|&m| MOVE_IS_QUARTER[m]) {
                        let j = ccos_mv[i][m];
                        if cc_qt[j] == UNSET {
                            cc_qt[j] = d + 1;
                        }
                    }
                }
            }
        }

        // bad corners, 4a / 4b, the corner subset
        let mut cc_bad = vec![0u8; NCCOS];
        let mut cc_shape = vec![0u8; NCCOS];
        let mut cc_subset = vec![0u8; NCCOS];
        // tetrad of each position (tetrad 1 = UFR UBL DFL DBR) and the faces as position masks (U D F B R L)
        const TETRAD: [u8; 8] = [1, 0, 1, 0, 0, 1, 0, 1];
        const FACE_MASKS: [usize; 6] = [0x0F, 0xF0, 0x33, 0xCC, 0x99, 0x66];
        let half: [St; 6] = std::array::from_fn(|k| St::ID.apply_move(HALF_MOVES[k]));
        for i in 0..NCCOS {
            let p = unrank_perm::<8>(ccos_rep[i]);
            let mask = (0..8).filter(|&k| TETRAD[k] != TETRAD[p[k] as usize]).fold(0usize, |m, k| m | 1 << k);
            let n = mask.count_ones() as u8;
            cc_bad[i] = n;
            if n == 4 {
                // move the set of bad positions around with half turns: 4a if it can become a face
                let mut seen = [false; 256];
                let mut queue = vec![mask];
                seen[mask] = true;
                let mut head = 0;
                while head < queue.len() {
                    let mk = queue[head];
                    head += 1;
                    for g in &half {
                        let mk2 = (0..8).filter(|&pos| mk >> g.c[pos] & 1 != 0).fold(0usize, |m, pos| m | 1 << pos);
                        if !seen[mk2] {
                            seen[mk2] = true;
                            queue.push(mk2);
                        }
                    }
                }
                cc_shape[i] = if queue.iter().any(|mk| FACE_MASKS.contains(mk)) { 0 } else { 1 };
            }
            let bad = match n {
                8 => 0,
                6 => 2,
                _ => n,
            };
            cc_subset[i] = subset_index(bad, cc_qt[i], cc_shape[i]).expect("every corner coset has a subset");
        }

        // the 48 subsets: components of the cosets under half turns on the right, U D' on the left and inversion
        let mut parent: Vec<usize> = (0..NCCOS * NEPAT).collect();
        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }
        fn union(parent: &mut [usize], x: usize, y: usize) {
            let (a, b) = (find(parent, x), find(parent, y));
            if a != b {
                parent[a] = b;
            }
        }
        for a in 0..NCCOS {
            for b in 0..NEPAT {
                let x = a * NEPAT + b;
                for &m in &HALF_MOVES {
                    union(&mut parent, x, ccos_mv[a][m] * NEPAT + epat_mv[b][m]);
                }
                union(&mut parent, x, lmul_c[a] * NEPAT + lmul_e[b]);
                let inv_a = ccos[dr.cinv[ccos_rep[a]] as usize] as usize;
                let inv_b = epat[dr.einv[epat_rep[b]] as usize] as usize;
                union(&mut parent, x, inv_a * NEPAT + inv_b);
            }
        }
        // (bad corners, bad edges) in the frame with few bad pieces
        let frame = |a: usize, b: usize| -> (u8, u8) {
            let (nc, ne) = (cc_bad[a], ep_bad[b]);
            if nc > 4 || (nc == 4 && ne > 4) {
                (8 - nc, 8 - ne)
            } else {
                (nc, ne)
            }
        };
        let mut sub48 = vec![[0u8; NEPAT]; NCCOS];
        let mut sub48_names: Vec<String> = Vec::new();
        let mut id: Vec<Option<u8>> = vec![None; NCCOS * NEPAT];
        for a in 0..NCCOS {
            for b in 0..NEPAT {
                let r = find(&mut parent, a * NEPAT + b);
                let k = *id[r].get_or_insert_with(|| {
                    let (nc, ne) = frame(a, b);
                    let q = cc_qt[a];
                    let letter = if nc == 4 && (q <= 2 || q == 5) { if cc_shape[a] != 0 { 'b' } else { 'a' } } else { 'c' };
                    sub48_names.push(format!("{nc}{letter}{q} {ne}e"));
                    (sub48_names.len() - 1) as u8
                });
                sub48[a][b] = k;
            }
        }
        assert_eq!(sub48_names.len(), 48);

        let label: Vec<[u8; NEPAT]> = (0..NCCOS)
            .map(|a| std::array::from_fn(|b| cc_subset[a] * 5 + frame(a, b).1 / 2))
            .collect();

        let mut htr = Htr {
            ccos, epat, ccos_rep, epat_rep, ccos_mv, epat_mv, htr_dist, cc_subset, cc_bad, ep_bad, sub48, sub48_names,
            label, c0, e0, corner_bound: Vec::new(), edge_bound: Vec::new(),
        };
        htr.build_niss_bounds(dr);
        htr
    }

    /// The route label of a state: corner subset * 5 + bad edges / 2.
    #[inline]
    pub fn label(&self, c: usize, e: usize) -> u8 {
        self.label[self.ccos[c] as usize][self.epat[e] as usize]
    }
    /// Is the state in HTR?
    #[inline]
    pub fn in_htr(&self, c: usize, e: usize) -> bool {
        self.ccos[c] as usize == self.c0 && self.epat[e] as usize == self.e0
    }
    /// Fewest DR moves to HTR, on this side only.
    #[inline]
    pub fn htr_moves(&self, c: usize, e: usize) -> u8 {
        self.htr_dist[self.ccos[c] as usize][self.epat[e] as usize]
    }
    /// Mallard's subset of a DR state.
    #[inline]
    pub fn subset(&self, c: usize, e: usize) -> usize {
        self.sub48[self.ccos[c] as usize][self.epat[e] as usize] as usize
    }
    pub fn subset_index(&self, name: &str) -> Option<usize> {
        self.sub48_names.iter().position(|n| n == name)
    }

    /// Lower bounds for `niss_htr`: the same quantity for corners alone and for edges alone, computed by relaxation
    /// over the 40320 corner (edge) permutations: `N(g) = min over A of |A| + htr(inverse of g·A)`.
    fn build_niss_bounds(&mut self, dr: &DrTables) {
        let bfs = |n: usize, mv: &dyn Fn(usize, usize) -> usize, start: usize| -> Vec<u8> {
            let mut d = vec![UNSET; n];
            d[start] = 0;
            let mut queue = vec![start];
            let mut head = 0;
            while head < queue.len() {
                let x = queue[head];
                head += 1;
                for m in 0..NMOVES {
                    let y = mv(x, m);
                    if d[y] == UNSET {
                        d[y] = d[x] + 1;
                        queue.push(y);
                    }
                }
            }
            d
        };
        let corner_htr = bfs(NCCOS, &|a, m| self.ccos_mv[a][m], self.c0);
        let edge_htr = bfs(NEPAT, &|b, m| self.epat_mv[b][m], self.e0);
        let relax = |n: usize, init: &dyn Fn(usize) -> u8, mv: &dyn Fn(usize, usize) -> usize| -> Vec<u8> {
            let mut v: Vec<u8> = (0..n).map(init).collect();
            loop {
                let mut changed = false;
                for x in 0..n {
                    for m in 0..NMOVES {
                        let y = mv(x, m);
                        if v[y] + 1 < v[x] {
                            v[x] = v[y] + 1;
                            changed = true;
                        }
                    }
                }
                if !changed {
                    return v;
                }
            }
        };
        self.corner_bound =
            relax(NC, &|c| corner_htr[self.ccos[dr.cinv[c] as usize] as usize], &|c, m| dr.cmove[m][c] as usize);
        self.edge_bound =
            relax(NE, &|e| edge_htr[self.epat[dr.einv[e] as usize] as usize], &|e, m| dr.emove[m][e] as usize);
    }

    /// Shortest NISS HTR: min |A| + |B| over A on normal and B on inverse with (X·A)^-1·B in H (IDA*, with the
    /// corner-only and edge-only versions of the same quantity as the bound).
    pub fn niss_htr(&self, dr: &DrTables, c: usize, e: usize) -> u8 {
        let upper = self.htr_moves(c, e).min(self.htr_moves(dr.cinv[c] as usize, dr.einv[e] as usize));
        let lower = self.corner_bound[c].max(self.edge_bound[e]);
        (lower..upper).find(|&t| self.niss_dfs(dr, c, e, 0, t, crate::dr::DrCanon::START)).unwrap_or(upper)
    }

    fn niss_dfs(&self, dr: &DrTables, c: usize, e: usize, g: u8, t: u8, canon: crate::dr::DrCanon) -> bool {
        if g + self.corner_bound[c].max(self.edge_bound[e]) > t {
            return false;
        }
        if g + self.htr_moves(dr.cinv[c] as usize, dr.einv[e] as usize) <= t {
            return true;
        }
        (0..NMOVES).any(|m| {
            canon.allows(m)
                && self.niss_dfs(dr, dr.cmove[m][c] as usize, dr.emove[m][e] as usize, g + 1, t, canon.after(m))
        })
    }
}
