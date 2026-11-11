//! "What you can see" quotients of the DR group and their exact best-case finish tables.
//! (Port of `drquot.h`.)
//!
//! Principle (formalised in Lean, FMC/Quotient.lean): let K be a subgroup of the DR group G and T(Kg)
//! the distance, in the graph of right cosets K\G with the 10 DR moves, from Kg to K.  Then
//!
//! ```text
//!      T(Kg) = min { optimal finish of k·g : k in K }      (so every state g needs at least T(Kg) moves),
//! ```
//!
//! and the same holds for the inverse state:  `optimal(g) >= T(K g^-1)`.
//! A right coset Kg is "g up to renaming pieces by an element of K", i.e. a set of visible features
//! of the position.
//!
//! Two subgroups are tabulated:
//!
//! * **KF** (order 3072) = HTR states whose corners are solved up to whole-cube half rotations and U2,
//!   whose M-slice edges have both U-coloured edges in the same layer, likewise the S-slice edges, and
//!   whose E-slice permutation is even.  Restricted to HTR states and half-turn moves, K\H is exactly
//!   the 216-case table of FakeMMAP (T12059-T12076) behind Rodney Kinney's "Advanced DR Bounding".
//!   Features of a DR state modulo KF:
//!     - corners  : the corner permutation up to renaming by {id, x2, y2, z2} x {id, U2}   (5040 classes)
//!     - edges    : which U/D-layer positions hold M-slice edges (70), and the U/D-colour pattern of the
//!                  M-slice edges up to swapping the two colours, same for the S-slice edges (3 x 3)
//!                                                                                          (630 classes)
//!     - E parity : parity of the E-slice permutation                                       (2)
//! * **K0** (order 1536) = the same without U2 (corners solved up to whole-cube half rotations only):
//!   10080 x 630 x 2 classes.

use crate::class::Classes;
use crate::core::{e_parity_flip, rank_perm, unrank_perm, Core, St, MOVE_IS_QT, NC, NE, NMOVES};

/// Number of edge classes of KF / K0.
pub const NE630: usize = 630;

/// The 630 edge classes: bad-edge positions + U/D-colour patterns of the M and S edges up to colour swap.
// Not every table is read by the current subcommands; they are all kept, as in the C header.
#[allow(dead_code)]
pub struct E630 {
    /// U/D-edge coordinate -> class 0..629
    pub cls: Vec<u16>,
    /// a representative edge coordinate of each class (the smallest one)
    pub rep: Vec<usize>,
    /// action of the ten moves on the classes
    pub mv: Vec<[u16; NMOVES]>,
    /// class -> edge pattern 0..69 of [`Classes::epat`]
    pub epat: Vec<u8>,
}

impl E630 {
    /// The C `e630_init`.
    pub fn new(core: &Core, classes: &Classes) -> E630 {
        let mut cls = vec![0u16; NE];
        let mut rep: Vec<usize> = Vec::with_capacity(NE630);
        let mut epat: Vec<u8> = Vec::with_capacity(NE630);
        let mut idx: Vec<Option<u16>> = vec![None; 1 << 16];
        for e in 0..NE {
            let p = unrank_perm::<8>(e);
            // mask: positions holding M-slice edges.  lay: for every position the home layer of its piece
            // (0 = U, white; 1 = D, yellow), normalised so that the first M edge and the first S edge read 0.
            let (mut mask, mut lay) = (0usize, 0usize);
            let (mut flip_m, mut flip_s): (Option<usize>, Option<usize>) = (None, None);
            for k in 0..8 {
                let is_s = p[k] & 1 != 0;
                let mut layer = (p[k] >> 2) as usize;
                if !is_s {
                    mask |= 1 << k;
                    layer ^= *flip_m.get_or_insert(layer);
                } else {
                    layer ^= *flip_s.get_or_insert(layer);
                }
                lay |= layer << k;
            }
            let key = mask << 8 | lay;
            if idx[key].is_none() {
                if rep.len() >= NE630 {
                    fatal!("more than 630 edge classes");
                }
                idx[key] = Some(rep.len() as u16);
                rep.push(e);
                epat.push(classes.epat[e]);
            }
            cls[e] = idx[key].unwrap();
        }
        if rep.len() != NE630 {
            fatal!("edge classes: {}, expected 630", rep.len());
        }
        let mv: Vec<[u16; NMOVES]> = (0..NE630)
            .map(|i| std::array::from_fn(|m| cls[core.emove[m][rep[i]] as usize]))
            .collect();
        for e in 0..NE {
            for m in 0..NMOVES {
                if cls[core.emove[m][e] as usize] != mv[cls[e] as usize][m] {
                    fatal!("edge class action not well defined");
                }
            }
        }
        E630 { cls, rep, mv, epat }
    }
}

/// The corner part of KF / K0: corner permutations up to renaming by {id, y2, x2, z2} (x {id, U2}).
// Not every table is read by the current subcommands; they are all kept, as in the C header.
#[allow(dead_code)]
pub struct CornerQuot {
    /// number of corner classes (5040 for KF, 10080 for K0)
    pub ncc: usize,
    /// corner coordinate -> class
    pub ccls: Vec<u16>,
    /// a representative corner coordinate of each class (the smallest one)
    pub rep: Vec<usize>,
    /// action of the ten moves on the classes
    pub mv: Vec<[u16; NMOVES]>,
    /// class -> HTR corner coset
    pub cc_ccos: Vec<u16>,
}

impl CornerQuot {
    /// `with_u2 = true` -> KF ; `false` -> K0.  (First half of the C `quot_init`.)
    pub fn new(core: &Core, classes: &Classes, with_u2: bool) -> CornerQuot {
        // the renaming group on corners: V = {id, U2D2, R2L2, F2B2} (x <U2>)
        let y2 = St::ID.apply_move(1).apply_move(4);
        let x2 = St::ID.apply_move(6).apply_move(7);
        let z2 = St::ID.apply_move(8).apply_move(9);
        let u2 = St::ID.apply_move(1);
        let mut el: Vec<St> = Vec::new();
        for v in [St::ID, y2, x2, z2] {
            el.push(v);
            if with_u2 {
                el.push(v.mul(u2));
            }
        }
        let mut ccls = vec![0xFFFFu16; NC];
        let mut rep: Vec<usize> = Vec::new();
        for c in 0..NC {
            if ccls[c] != 0xFFFF {
                continue;
            }
            let p = unrank_perm::<8>(c);
            let n = rep.len() as u16;
            rep.push(c);
            for g in &el {
                let r: [u8; 8] = std::array::from_fn(|k| g.c[p[k] as usize]);
                let d = rank_perm(&r);
                if ccls[d] != 0xFFFF && ccls[d] != n {
                    fatal!("renaming set is not a group");
                }
                ccls[d] = n;
            }
        }
        let ncc = rep.len();
        if ncc != NC / el.len() {
            fatal!("corner classes {}, expected {}", ncc, NC / el.len());
        }
        let cc_ccos: Vec<u16> = rep.iter().map(|&r| classes.ccos[r]).collect();
        let mv: Vec<[u16; NMOVES]> = rep
            .iter()
            .map(|&r| std::array::from_fn(|m| ccls[core.cmove[m][r] as usize]))
            .collect();
        for c in 0..NC {
            if classes.ccos[c] != cc_ccos[ccls[c] as usize] {
                fatal!("class does not refine HTR coset");
            }
            for m in 0..NMOVES {
                if ccls[core.cmove[m][c] as usize] != mv[ccls[c] as usize][m] {
                    fatal!("corner class action not well defined");
                }
            }
        }
        CornerQuot {
            ncc,
            ccls,
            rep,
            mv,
            cc_ccos,
        }
    }
}

/// A quotient KF or K0 with its distance tables, indexed by [`Quot::idx`].
pub struct Quot {
    pub corners: CornerQuot,
    /// `[ncc * 630 * 2]` distance to the solved class with all 10 DR moves
    pub t: Vec<u8>,
    /// same graph, half-turn moves only (0xFF if unreachable): the HTR-only table
    pub th: Vec<u8>,
}

impl Quot {
    /// Table index of (corner class, edge class, E-slice parity).
    #[inline]
    pub fn idx(cc: usize, ee: usize, par: usize) -> usize {
        (cc * NE630 + ee) * 2 + par
    }

    /// Number of classes (table length).
    pub fn len(&self) -> usize {
        self.corners.ncc * NE630 * 2
    }

    /// `with_u2 = true` -> KF ; `false` -> K0.  (The C `quot_init`.)
    pub fn new(core: &Core, classes: &Classes, e630: &E630, with_u2: bool) -> Quot {
        let corners = CornerQuot::new(core, classes, with_u2);
        let n = corners.ncc * NE630 * 2;
        let bfs = |half_turns_only: bool| -> (Vec<u8>, usize) {
            let mut t = vec![0xFFu8; n];
            let mut queue: Vec<u32> = Vec::with_capacity(n);
            let s0 = Quot::idx(corners.ccls[0] as usize, e630.cls[0] as usize, 0);
            t[s0] = 0;
            queue.push(s0 as u32);
            let mut head = 0;
            while head < queue.len() {
                let s = queue[head] as usize;
                head += 1;
                let (par, ee, cc) = (s & 1, (s >> 1) % NE630, (s >> 1) / NE630);
                for m in 0..NMOVES {
                    if half_turns_only && MOVE_IS_QT[m] {
                        continue;
                    }
                    let j = Quot::idx(
                        corners.mv[cc][m] as usize,
                        e630.mv[ee][m] as usize,
                        par ^ e_parity_flip(m),
                    );
                    if t[j] == 0xFF {
                        t[j] = t[s] + 1;
                        queue.push(j as u32);
                    }
                }
            }
            (t, queue.len())
        };
        let (t, reached) = bfs(false);
        if reached != n {
            fatal!("quotient graph not connected: {} of {}", reached, n);
        }
        let (th, _) = bfs(true);
        Quot { corners, t, th }
    }
}
