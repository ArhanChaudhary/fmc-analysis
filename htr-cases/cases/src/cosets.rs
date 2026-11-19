//! The 29,400 HTR cosets of the DR group, and what acts on them: the ten DR moves, the 16 symmetries and the E slice.
//!
//! H = `<U2, D2, R2, L2, F2, B2>`.  Two DR states are the same HTR case when exactly the same move sequences take them
//! to HTR, which is when they differ by an element of H renaming the pieces: the class of a state g is the coset H·g.
//! A coset is a corner coset (420 of them) and an edge pattern (70: which U/D-layer places hold M-slice edges), numbered
//! `corner * 70 + edges` as in [`attempt_sim::htr`].
//!
//! * A symmetry S (a rotation or mirror that keeps the U/D axis) takes H·g to H·S g S⁻¹, and a solution's moves to
//!   their images.
//! * The E slice: renaming every piece by U D' takes H·g to H·(U D') g (U D' normalises H).  The bad pieces swap
//!   with the good ones; up to the rotation y it is the same as turning the E slice a quarter turn.

use attempt_sim::dr::{rank_perm, unrank_perm, DrTables, St, MOVE_FACE, MOVE_IS_QUARTER, NMOVES, NSYM};
use attempt_sim::htr::{Htr, NCCOS, NEPAT};

pub const NCOSETS: usize = NCCOS * NEPAT;

/// Tetrad of each corner place (1 = UFR UBL DFL DBR), as in `attempt_sim::htr`.
const TETRAD: [u8; 8] = [1, 0, 1, 0, 0, 1, 0, 1];

/// The moves U and D, the clockwise quarter turns (DR move numbers).
pub const CLOCKWISE: [u8; 2] = [0, 3];

pub struct Cosets {
    /// `mv[x][m]`: the coset after move m
    pub mv: Vec<[u16; NMOVES]>,
    /// fewest DR moves to HTR
    pub dist: Vec<u8>,
    /// `sym[x][s]`: the coset seen through symmetry s
    pub sym: Vec<[u16; NSYM]>,
    /// `move_sym[s][m]`: move m seen through symmetry s
    pub move_sym: [[u8; NMOVES]; NSYM],
    /// the coset with every piece renamed by U D' (the E slice)
    pub eslice: Vec<u16>,
    /// bad corners and bad edges as place masks (bit p: place p of `attempt_sim::dr`), relative to the centres
    pub corner_mask: Vec<u8>,
    pub edge_mask: Vec<u8>,
    /// the corner subset of each coset (index into `attempt_sim::htr::SUBSET_NAMES`: 4a3 and 4b3 apart)
    pub subset: Vec<u8>,
    /// fewest DR moves that put the corners alone in HTR, per corner coset
    pub corner_dist: Vec<u8>,
    /// the corner coset after each move
    pub corner_mv: Vec<[usize; NMOVES]>,
    /// the HTR coset
    pub solved: usize,
}

impl Cosets {
    pub fn new(dr: &DrTables, htr: &Htr) -> Cosets {
        let index = |c: usize, e: usize| htr.ccos[c] as usize * NEPAT + htr.epat[e] as usize;
        let rep: Vec<(usize, usize)> =
            (0..NCOSETS).map(|x| (htr.ccos_rep[x / NEPAT], htr.epat_rep[x % NEPAT])).collect();

        let mv = rep
            .iter()
            .map(|&(c, e)| std::array::from_fn(|m| index(dr.cmove[m][c] as usize, dr.emove[m][e] as usize) as u16))
            .collect();
        let dist = (0..NCOSETS).map(|x| htr.htr_dist[x / NEPAT][x % NEPAT]).collect();
        let sym = rep
            .iter()
            .map(|&(c, e)| std::array::from_fn(|s| index(dr.csym[s][c] as usize, dr.esym[s][e] as usize) as u16))
            .collect();

        // a move seen through a symmetry is the move whose state is the conjugate of its state
        let move_sym = std::array::from_fn(|s| {
            std::array::from_fn(|m| {
                let image = (
                    dr.csym[s][dr.cmove[m][0] as usize],
                    dr.esym[s][dr.emove[m][0] as usize],
                    dr.ssym[s][dr.smove[m][0] as usize],
                );
                let found = (0..NMOVES).find(|&n| (dr.cmove[n][0], dr.emove[n][0], dr.smove[n][0]) == image);
                found.expect("a symmetry takes moves to moves") as u8
            })
        });

        let ud = St::ID.apply_move(0).apply_move(5); // U D'
        let eslice = rep
            .iter()
            .map(|&(c, e)| {
                let renamed = ud.then(St::unrank(c, e, 0));
                index(rank_perm(&renamed.c), rank_perm(&renamed.e)) as u16
            })
            .collect();

        let corner_mask = rep
            .iter()
            .map(|&(c, _)| {
                let p = unrank_perm::<8>(c);
                (0..8).filter(|&k| TETRAD[k] != TETRAD[p[k] as usize]).fold(0u8, |m, k| m | 1 << k)
            })
            .collect();
        // a bad edge: an M-slice edge (UF UB DF DB, the even numbers) on an S-slice place, or the other way
        let edge_mask = rep
            .iter()
            .map(|&(_, e)| {
                let p = unrank_perm::<8>(e);
                (0..8).filter(|&k| k % 2 != p[k] as usize % 2).fold(0u8, |m, k| m | 1 << k)
            })
            .collect();
        let subset = (0..NCOSETS).map(|x| htr.cc_subset[x / NEPAT]).collect();

        let solved = index(0, 0);
        let corner_mv = htr.ccos_mv.clone();
        let mut corner_dist = vec![u8::MAX; NCCOS];
        corner_dist[solved / NEPAT] = 0;
        let mut queue = vec![solved / NEPAT];
        let mut head = 0;
        while head < queue.len() {
            let a = queue[head];
            head += 1;
            for &b in &corner_mv[a] {
                if corner_dist[b] == u8::MAX {
                    corner_dist[b] = corner_dist[a] + 1;
                    queue.push(b);
                }
            }
        }

        Cosets { mv, dist, sym, move_sym, eslice, corner_mask, edge_mask, subset, corner_dist, corner_mv, solved }
    }

    /// Bad corners and bad edges, relative to the centres.
    pub fn bad(&self, x: usize) -> (u32, u32) {
        (self.corner_mask[x].count_ones(), self.edge_mask[x].count_ones())
    }

    /// Is the coset seen in the frame with few bad pieces?  (Fewer than 4 bad corners, or 4 with at most 4 bad edges.)
    pub fn few_frame(&self, x: usize) -> bool {
        let (c, e) = self.bad(x);
        c < 4 || (c == 4 && e <= 4)
    }

    /// Every HTR of at most `max_len` DR moves from coset `x`, each once:
    ///
    /// * no two turns of one face in a row, and turns of opposite faces in the order U D, R L, F B;
    /// * nothing that is in HTR before its end;
    /// * no half turn in its last turn, or in its last two when they are on opposite faces (such a half turn could go
    ///   last, where it does nothing for HTR).
    ///
    /// So it ends in a quarter turn, or in U D with both quarter turns, and that quarter turn can go either way: only
    /// the clockwise one is listed.
    pub fn solutions(&self, x: usize, max_len: usize) -> Vec<Vec<u8>> {
        let mut out = Vec::new();
        if x != self.solved {
            self.search(x, max_len, &mut Vec::with_capacity(max_len), &mut out);
        }
        out
    }

    fn search(&self, x: usize, budget: usize, path: &mut Vec<u8>, out: &mut Vec<Vec<u8>>) {
        if x == self.solved {
            let last = last_block(path);
            if last.iter().all(|m| CLOCKWISE.contains(m)) {
                out.push(path.clone());
            }
            return;
        }
        if self.dist[x] as usize > budget {
            return;
        }
        for m in 0..NMOVES as u8 {
            if follows(path.last().copied(), m) {
                path.push(m);
                self.search(self.mv[x][m as usize] as usize, budget - 1, path, out);
                path.pop();
            }
        }
    }

    /// A shortest sequence of DR moves that puts the corners of coset `x` in HTR (edges ignored), the first in move
    /// order.
    pub fn corner_solution(&self, x: usize) -> Vec<u8> {
        let mut a = x / NEPAT;
        let mut path: Vec<u8> = Vec::new();
        while self.corner_dist[a] > 0 {
            let m = (0..NMOVES as u8)
                .find(|&m| {
                    follows(path.last().copied(), m)
                        && self.corner_dist[self.corner_mv[a][m as usize]] < self.corner_dist[a]
                })
                .expect("a move gets closer");
            a = self.corner_mv[a][m as usize];
            path.push(m);
        }
        path
    }

    /// The coset after a sequence of DR moves.
    pub fn after(&self, mut x: usize, moves: &[u8]) -> usize {
        for &m in moves {
            x = self.mv[x][m as usize] as usize;
        }
        x
    }
}

/// May DR move `m` follow `last`?  Never the same face twice, and opposite faces only in the order U D, R L, F B.
pub fn follows(last: Option<u8>, m: u8) -> bool {
    match last {
        None => true,
        Some(l) => {
            let (f, g) = (MOVE_FACE[l as usize], MOVE_FACE[m as usize]);
            f != g && !(f / 2 == g / 2 && g < f)
        }
    }
}

/// The turns that end a sequence and commute with each other: the last turn, with the one before when that one is on
/// the opposite face.
pub fn last_block(path: &[u8]) -> &[u8] {
    let n = path.len();
    if n >= 2 && MOVE_FACE[path[n - 1] as usize] / 2 == MOVE_FACE[path[n - 2] as usize] / 2 {
        &path[n - 2..]
    } else {
        &path[n.saturating_sub(1)..]
    }
}

/// Does the sequence end the way a listed HTR does: no half turn in its last block?
pub fn ends_in_quarter_turns(path: &[u8]) -> bool {
    !path.is_empty() && last_block(path).iter().all(|&m| MOVE_IS_QUARTER[m as usize])
}
