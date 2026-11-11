//! HTR cosets of the DR group and the community's "HTR subset" labels, all computed from scratch.
//! (Port of `drclass.h`.)
//!
//! H = `<U2, D2, R2, L2, F2, B2>` (the HTR group).  A right coset H·g is "the state g up to renaming
//! pieces by an HTR element", i.e. exactly the information that survives when you only look at which
//! pieces are bad.  H\G = 420 corner cosets x 70 edge patterns.
//!
//! Definitions used for labels (source: wen's sheet "HTR better smh (v2)", KB doc 87; Jay/Jack Love T144-T172):
//!
//! * bad corner = a corner sitting in a position of the other tetrad (tetrads = orbits of corner
//!   positions under half turns)
//! * bad edge = an M-slice edge (UF UB DF DB) sitting in an S-slice position (UL UR DL DR) or vice versa
//!
//! The community counts bad pieces up to turning both outer layers by a quarter ("0 or 8 bad corners",
//! "4C2E = 4C6E", T165): renaming all pieces by the state U D' turns n bad corners into 8-n and n bad
//! edges into 8-n.  Mallard (cubelib, steps/htr/subsets.rs) builds its 48 subsets as: closure of H·g and
//! H·(U D)·g under half turns on the right and inversion, i.e. double cosets of Hhat = `<H, U D>` merged
//! with their inverses.  We reproduce exactly that:
//!
//! * `NcQ` label = N bad corners in the frame where N <= 4 (and, if N = 4, bad edges <= 4),
//!   Q = minimum number of quarter turns that bring the corners into H-corners or (U D')·H-corners
//!   ("qt_corners")
//! * `4a` / `4b` = the four bad corners can / cannot be placed on a single face using half turns only
//!   (only for Q <= 2 and Q = 5; for Q = 3, 4 a state and its inverse have different letters, and
//!   Mallard writes 4c3 / 4c4)

use crate::core::{rank_perm, unrank_perm, Core, St, MOVE_IS_QT, NC, NE, NMOVES};

/// Number of HTR corner cosets.
pub const NCCOS: usize = 420;
/// Number of edge patterns (which U/D-layer positions hold M-slice edges): C(8,4).
pub const NEPAT: usize = 70;
/// The half turns U2 D2 R2 L2 F2 B2 as move numbers.
pub const HALF_MOVES: [usize; 6] = [1, 4, 6, 7, 8, 9];

/// Number of corner subsets (labels of the 420 corner cosets).
pub const NSUBSET: usize = 14;
pub const SUBSET_NAME: [&str; NSUBSET] = [
    "0c0", "4a1", "4a2", "4b2", "0c3", "2c3", "4a3", "4b3", "0c4", "2c4", "4a4", "4b4", "2c5",
    "4b5",
];

/// "Not reached yet" marker in the distance tables.
const UNSET: u8 = 0xFF;

/// Index into [`SUBSET_NAME`] for (bad corners in {0, 2, 4}, quarter-turn count, 4a/4b shape), if such a subset exists.
fn subset_index(nbadclass: u8, qt: u8, shape: u8) -> Option<u8> {
    let table: &[(u8, u8)] = match (nbadclass, shape) {
        (0, _) => &[(0, 0), (3, 4), (4, 8)],
        (2, _) => &[(3, 5), (4, 9), (5, 12)],
        (_, 0) => &[(1, 1), (2, 2), (3, 6), (4, 10)],
        _ => &[(2, 3), (3, 7), (4, 11), (5, 13)],
    };
    table
        .iter()
        .find(|&&(q, _)| q == qt)
        .map(|&(_, index)| index)
}

/// All tables of `drclass.h`.
// Not every table is read by the current subcommands; they are all kept, as in the C header.
#[allow(dead_code)]
pub struct Classes {
    /// corner coordinate -> corner coset 0..419
    pub ccos: Vec<u16>,
    /// U/D-edge coordinate -> edge pattern 0..69
    pub epat: Vec<u8>,
    /// a representative corner coordinate of each coset (the smallest one)
    pub ccos_rep: Vec<usize>,
    pub epat_rep: Vec<usize>,
    /// bit k set = position k holds an M-slice edge
    pub epat_mask: Vec<usize>,
    /// action of the ten moves on corner cosets / edge patterns
    pub ccos_mv: Vec<[usize; NMOVES]>,
    pub epat_mv: Vec<[usize; NMOVES]>,
    /// `htr_dist[a][b]`: optimal DR->HTR length (DR moves) of corner coset a, edge pattern b
    pub htr_dist: Vec<[u8; NEPAT]>,
    /// "qt_corners": min quarter turns to bring the corners to HTR up to the U D' rotation
    pub cc_qt: Vec<u8>,
    /// min quarter turns of any DR sequence reaching H exactly (corners and edges)
    pub qt_full: Vec<[u8; NEPAT]>,
    /// left multiplication by U D' (renaming pieces by a quarter rotation of both layers)
    pub lmul_c: Vec<usize>,
    pub lmul_e: Vec<usize>,
    /// Mallard subset id 0..47 of each HTR coset
    pub sub48: Vec<[u8; NEPAT]>,
    /// name ("4a1 2e", ...) and label parts of each of the 48 subsets; `sub48_name.len()` is the C `NSUB48`
    pub sub48_name: Vec<String>,
    pub sub48_nc: Vec<u8>,
    pub sub48_ne: Vec<u8>,
    pub sub48_qt: Vec<u8>,
    pub sub48_letter: Vec<char>,
    /// number of bad corners (0, 2, 4, 6, 8)
    pub cc_nbad: Vec<u8>,
    /// for 4 bad corners: 0 = 4a, 1 = 4b ; otherwise 0
    pub cc_shape: Vec<u8>,
    /// index into [`SUBSET_NAME`]
    pub cc_subset: Vec<u8>,
    /// number of bad edges (0, 2, 4, 6, 8)
    pub ep_nbad: Vec<u8>,
    /// the 96 corner permutations of H
    pub hc: Vec<usize>,
}

impl Classes {
    /// Build everything (the C `drclass_init`).
    pub fn new(core: &Core) -> Classes {
        // --- the HTR corner group: all corner permutations reachable with half turns
        let mut hc: Vec<usize> = vec![0];
        {
            let mut seen = vec![false; NC];
            seen[0] = true;
            let mut head = 0;
            while head < hc.len() {
                let c = hc[head];
                head += 1;
                for &m in &HALF_MOVES {
                    let d = core.cmove[m][c] as usize;
                    if !seen[d] {
                        seen[d] = true;
                        hc.push(d);
                    }
                }
            }
            if hc.len() != 96 {
                fatal!("HTR corner group has {} elements, expected 96", hc.len());
            }
        }

        // --- right cosets H·c : relabel the pieces of c by every h in H
        let mut ccos = vec![0xFFFFu16; NC];
        let mut ccos_rep: Vec<usize> = Vec::with_capacity(NCCOS);
        {
            let hp: Vec<[u8; 8]> = hc.iter().map(|&h| unrank_perm::<8>(h)).collect();
            for c in 0..NC {
                if ccos[c] != 0xFFFF {
                    continue;
                }
                let p = unrank_perm::<8>(c);
                let n = ccos_rep.len();
                if n >= NCCOS {
                    fatal!("more than 420 corner cosets");
                }
                ccos_rep.push(c);
                for h in &hp {
                    let r: [u8; 8] = std::array::from_fn(|k| h[p[k] as usize]);
                    ccos[rank_perm(&r)] = n as u16;
                }
            }
            if ccos_rep.len() != NCCOS {
                fatal!("found {} corner cosets, expected 420", ccos_rep.len());
            }
        }

        // --- edge patterns: which positions hold M-slice pieces (pieces 0,2,4,6)
        let mut epat = vec![0u8; NE];
        let mut epat_rep: Vec<usize> = Vec::with_capacity(NEPAT);
        let mut epat_mask: Vec<usize> = Vec::with_capacity(NEPAT);
        {
            let mut idx: [Option<usize>; 256] = [None; 256];
            for e in 0..NE {
                let p = unrank_perm::<8>(e);
                let mut mask = 0usize;
                for k in 0..8 {
                    if p[k] & 1 == 0 {
                        mask |= 1 << k;
                    }
                }
                let i = *idx[mask].get_or_insert_with(|| {
                    epat_rep.push(e);
                    epat_mask.push(mask);
                    epat_rep.len() - 1
                });
                if i >= NEPAT {
                    fatal!("more than 70 edge patterns");
                }
                epat[e] = i as u8;
            }
            if epat_rep.len() != NEPAT {
                fatal!("found {} edge patterns, expected 70", epat_rep.len());
            }
        }
        // a bad edge = an M-slice piece in an S-slice (odd) position; equally many S pieces are then misplaced
        let ep_nbad: Vec<u8> = epat_mask
            .iter()
            .map(|&mask| 2 * (mask & 0b1010_1010).count_ones() as u8)
            .collect();

        let ccos_mv: Vec<[usize; NMOVES]> = (0..NCCOS)
            .map(|i| std::array::from_fn(|m| ccos[core.cmove[m][ccos_rep[i]] as usize] as usize))
            .collect();
        let epat_mv: Vec<[usize; NMOVES]> = (0..NEPAT)
            .map(|i| std::array::from_fn(|m| epat[core.emove[m][epat_rep[i]] as usize] as usize))
            .collect();
        // well-definedness check of the coset action (every element, every move)
        for c in 0..NC {
            for m in 0..NMOVES {
                if ccos[core.cmove[m][c] as usize] as usize != ccos_mv[ccos[c] as usize][m] {
                    fatal!("corner coset action not well defined");
                }
                if epat[core.emove[m][c] as usize] as usize != epat_mv[epat[c] as usize][m] {
                    fatal!("edge pattern action not well defined");
                }
            }
        }
        let (c0, e0) = (ccos[0] as usize, epat[0] as usize); // the coset of the solved cube

        // --- DR->HTR distance (BFS over 420 x 70 from the coset of the identity)
        let mut htr_dist = vec![[UNSET; NEPAT]; NCCOS];
        {
            let mut queue: Vec<(usize, usize)> = Vec::with_capacity(NCCOS * NEPAT);
            htr_dist[c0][e0] = 0;
            queue.push((c0, e0));
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
            if queue.len() != NCCOS * NEPAT {
                fatal!("HTR coset graph not connected ({})", queue.len());
            }
        }

        // --- left multiplication by X = U D' on cosets (X normalises H, so H·g -> H·X·g is well defined)
        let x = St::ID.apply_move(0).apply_move(5);
        let lmul_c: Vec<usize> = (0..NCCOS)
            .map(|i| ccos[rank_perm(&x.mul(St::unrank(ccos_rep[i], 0, 0)).c)] as usize)
            .collect();
        let lmul_e: Vec<usize> = (0..NEPAT)
            .map(|i| epat[rank_perm(&x.mul(St::unrank(0, epat_rep[i], 0)).e)] as usize)
            .collect();
        for c in (0..NC).step_by(11) {
            let r = x.mul(St::unrank(c, c, 0));
            if ccos[rank_perm(&r.c)] as usize != lmul_c[ccos[c] as usize]
                || epat[rank_perm(&r.e)] as usize != lmul_e[epat[c] as usize]
            {
                fatal!("U D' does not normalise H");
            }
        }

        // --- "qt_corners": half turns cost 0, quarter turns cost 1, targets = H-corners and (U D')·H-corners
        let mut cc_qt = vec![UNSET; NCCOS];
        cc_qt[c0] = 0;
        cc_qt[lmul_c[c0]] = 0;
        for d in 0..12u8 {
            // spread cost d along half turns until nothing changes, then step once with quarter turns
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
                    for m in (0..NMOVES).filter(|&m| MOVE_IS_QT[m]) {
                        let j = ccos_mv[i][m];
                        if cc_qt[j] == UNSET {
                            cc_qt[j] = d + 1;
                        }
                    }
                }
            }
        }

        // --- qt_full: min quarter turns to reach H exactly, over all 29,400 cosets
        let mut qt_full = vec![[UNSET; NEPAT]; NCCOS];
        qt_full[c0][e0] = 0;
        for d in 0..16u8 {
            let mut changed = true;
            while changed {
                changed = false;
                for a in 0..NCCOS {
                    for b in 0..NEPAT {
                        if qt_full[a][b] == d {
                            for &m in &HALF_MOVES {
                                let (a2, b2) = (ccos_mv[a][m], epat_mv[b][m]);
                                if qt_full[a2][b2] > d {
                                    qt_full[a2][b2] = d;
                                    changed = true;
                                }
                            }
                        }
                    }
                }
            }
            for a in 0..NCCOS {
                for b in 0..NEPAT {
                    if qt_full[a][b] == d {
                        for m in (0..NMOVES).filter(|&m| MOVE_IS_QT[m]) {
                            let (a2, b2) = (ccos_mv[a][m], epat_mv[b][m]);
                            if qt_full[a2][b2] == UNSET {
                                qt_full[a2][b2] = d + 1;
                            }
                        }
                    }
                }
            }
        }

        // --- bad corners, 4a/4b, labels
        let mut cc_nbad = vec![0u8; NCCOS];
        let mut cc_shape = vec![0u8; NCCOS];
        let mut cc_subset = vec![0u8; NCCOS];
        {
            // tetrad of each position; tetrad 1 = UFR UBL DFL DBR
            const T1: [u8; 8] = [1, 0, 1, 0, 0, 1, 0, 1];
            // U D F B R L as corner-position masks
            const FACE: [usize; 6] = [0x0F, 0xF0, 0x33, 0xCC, 0x99, 0x66];
            let half: [St; 6] = std::array::from_fn(|k| St::ID.apply_move(HALF_MOVES[k]));
            for i in 0..NCCOS {
                let p = unrank_perm::<8>(ccos_rep[i]);
                let mut mask = 0usize;
                let mut n = 0u8;
                for k in 0..8 {
                    if T1[k] != T1[p[k] as usize] {
                        mask |= 1 << k;
                        n += 1;
                    }
                }
                cc_nbad[i] = n;
                if n == 4 {
                    // move the set of bad positions around with half turns; 4a if it can become a face
                    let mut seen = [false; 256];
                    let mut queue = vec![mask];
                    seen[mask] = true;
                    let mut on_a_face = false;
                    let mut head = 0;
                    while head < queue.len() {
                        let mk = queue[head];
                        head += 1;
                        if FACE.contains(&mk) {
                            on_a_face = true;
                        }
                        for g in &half {
                            // the piece now at `pos` came from g.c[pos]
                            let mut mk2 = 0usize;
                            for pos in 0..8 {
                                if mk >> g.c[pos] & 1 != 0 {
                                    mk2 |= 1 << pos;
                                }
                            }
                            if !seen[mk2] {
                                seen[mk2] = true;
                                queue.push(mk2);
                            }
                        }
                    }
                    cc_shape[i] = if on_a_face { 0 } else { 1 };
                }
                let nb = match n {
                    8 => 0,
                    6 => 2,
                    _ => n,
                };
                match subset_index(nb, cc_qt[i], cc_shape[i]) {
                    Some(si) => cc_subset[i] = si,
                    None => fatal!(
                        "unexpected corner class: nbad {} qt {} shape {}",
                        n,
                        cc_qt[i],
                        cc_shape[i]
                    ),
                }
            }
        }

        // --- the 48 subsets: components of the 29,400 cosets under  half turns on the right, U D' on the left, inversion
        let mut sub48 = vec![[0u8; NEPAT]; NCCOS];
        let (mut sub48_name, mut sub48_nc, mut sub48_ne, mut sub48_qt, mut sub48_letter) =
            (Vec::new(), Vec::new(), Vec::new(), Vec::new(), Vec::new());
        {
            // union-find over the cosets, numbered a * NEPAT + b
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
                    let inv_a = ccos[core.cinv[ccos_rep[a]] as usize] as usize;
                    let inv_b = epat[core.einv[epat_rep[b]] as usize] as usize;
                    union(&mut parent, x, inv_a * NEPAT + inv_b);
                }
            }
            // The label of a coset in the frame with few bad pieces: (bad corners, bad edges).
            let frame = |a: usize, b: usize| -> (u8, u8) {
                let (nc, ne) = (cc_nbad[a], ep_nbad[b]);
                if nc > 4 || (nc == 4 && ne > 4) {
                    (8 - nc, 8 - ne)
                } else {
                    (nc, ne)
                }
            };
            // number the components in order of first appearance; the first coset met names the subset
            let mut id: Vec<Option<u8>> = vec![None; NCCOS * NEPAT];
            for a in 0..NCCOS {
                for b in 0..NEPAT {
                    let r = find(&mut parent, a * NEPAT + b);
                    if id[r].is_none() {
                        id[r] = Some(sub48_name.len() as u8);
                        let (nc, ne) = frame(a, b);
                        let q = cc_qt[a];
                        let mut letter = 'c';
                        if nc == 4 && (q <= 2 || q == 5) {
                            letter = if cc_shape[a] != 0 { 'b' } else { 'a' };
                        }
                        sub48_nc.push(nc);
                        sub48_ne.push(ne);
                        sub48_qt.push(q);
                        sub48_letter.push(letter);
                        sub48_name.push(format!("{}{}{} {}e", nc, letter, q, ne));
                        if sub48_name.len() > 64 {
                            fatal!("too many subsets");
                        }
                    }
                    sub48[a][b] = id[r].unwrap();
                }
            }
            // every coset of a component must carry the same label
            for a in 0..NCCOS {
                for b in 0..NEPAT {
                    let (nc, ne) = frame(a, b);
                    let k = sub48[a][b] as usize;
                    if sub48_nc[k] != nc || sub48_ne[k] != ne || sub48_qt[k] != cc_qt[a] {
                        fatal!(
                            "subset label not constant on component {} (coset {},{}: {}c{} {}e)",
                            sub48_name[k],
                            a,
                            b,
                            nc,
                            cc_qt[a],
                            ne
                        );
                    }
                }
            }
        }

        Classes {
            ccos,
            epat,
            ccos_rep,
            epat_rep,
            epat_mask,
            ccos_mv,
            epat_mv,
            htr_dist,
            cc_qt,
            qt_full,
            lmul_c,
            lmul_e,
            sub48,
            sub48_name,
            sub48_nc,
            sub48_ne,
            sub48_qt,
            sub48_letter,
            cc_nbad,
            cc_shape,
            cc_subset,
            ep_nbad,
            hc,
        }
    }
}

/// Optimal corner-solution length in DR moves of every corner permutation (corners only, 40320 states):
/// a plain breadth-first search from the solved corners.
pub fn corner_only_lengths(core: &Core) -> Vec<u8> {
    let mut len = vec![UNSET; NC];
    let mut queue: Vec<usize> = Vec::with_capacity(NC);
    len[0] = 0;
    queue.push(0);
    let mut head = 0;
    while head < queue.len() {
        let c = queue[head];
        head += 1;
        for m in 0..NMOVES {
            let c2 = core.cmove[m][c] as usize;
            if len[c2] == UNSET {
                len[c2] = len[c] + 1;
                queue.push(c2);
            }
        }
    }
    len
}
