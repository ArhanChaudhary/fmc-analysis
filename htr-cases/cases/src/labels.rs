//! Two properties the guides use to tell apart HTR cases whose bad pieces look the same: 4b2 parity and 2c3
//! direction.  Both are computed per corner coset from the guides' own rules, and both turn out to be well defined (the
//! same on every route; `cargo test` checks it).
//!
//! * **4b2 parity** (*Hitchhiker's Guide to HTR*, "How to solve 4b2"): set the corners up for a 2-quarter-turn trigger
//!   (Q X2 Q, X a side face) with half turns, counting every U2 or D2 done while the bad corners split 3/1 between U
//!   and D.  An even count means the trigger then gives real HTR: no parity.  An odd count: parity.
//! * **2c3 direction** (same guide, "How to solve 2c3", and the server: "every half turn you do on a 2c3 changes the
//!   qt direction"): from the position shown, the quarter turn that brings it to 4b2 with no parity goes clockwise or
//!   anticlockwise (U and D each seen from its own face), every half turn done before it flipping the direction.

use crate::cosets::Cosets;
use attempt_sim::dr::HALF_MOVES;
use attempt_sim::htr::{NCCOS, NEPAT, SUBSET_NAMES};

/// U, U', D, D' as DR moves, and whether each is clockwise seen from its own face.
const QUARTER_TURNS: [(usize, bool); 4] = [(0, true), (2, false), (3, true), (5, false)];
const SIDE_HALF_TURNS: [usize; 4] = [6, 7, 8, 9];

pub struct Labels {
    /// per corner coset: for 4b2, Some(true) if it has parity
    pub parity: Vec<Option<bool>>,
    /// per corner coset: for 2c3, Some(true) if its quarter turn goes clockwise
    pub clockwise: Vec<Option<bool>>,
}

/// The values a property takes over every half-turn route from corner coset `a`: `flips(b, m)` says whether half
/// turn m done at b flips the count, `seen_at(b)` which values a state b reached with an even count shows (as a
/// bit mask of 0 / 1 values, each xor-ed with the count).
fn over_half_turn_routes(
    cs: &Cosets,
    a: usize,
    flips: impl Fn(usize, usize) -> bool,
    seen_at: impl Fn(usize) -> [bool; 2],
) -> [bool; 2] {
    let mut seen = vec![[false; 2]; NCCOS];
    seen[a][0] = true;
    let mut queue = vec![(a, 0usize)];
    let mut head = 0;
    let mut values = [false; 2];
    while head < queue.len() {
        let (b, count) = queue[head];
        head += 1;
        for (v, &shown) in seen_at(b).iter().enumerate() {
            if shown {
                values[v ^ count] = true;
            }
        }
        for &m in &HALF_MOVES {
            let next = (cs.corner_mv[b][m], count ^ flips(b, m) as usize);
            if !seen[next.0][next.1] {
                seen[next.0][next.1] = true;
                queue.push(next);
            }
        }
    }
    values
}

impl Labels {
    pub fn new(cs: &Cosets) -> Labels {
        let corner_solved = cs.solved / NEPAT;
        let corner_mask = |a: usize| cs.corner_mask[a * NEPAT];
        let name = |a: usize| SUBSET_NAMES[cs.subset[a * NEPAT] as usize];
        let after = |a: usize, moves: &[usize]| moves.iter().fold(a, |b, &m| cs.corner_mv[b][m]);

        // 4b2 parity
        let split_3_1 = |a: usize| {
            let (u, d) = ((corner_mask(a) & 0x0F).count_ones(), (corner_mask(a) & 0xF0).count_ones());
            u + d == 4 && (u == 1 || u == 3)
        };
        let trigger_solves = |a: usize| {
            QUARTER_TURNS.iter().any(|&(q1, _)| {
                SIDE_HALF_TURNS
                    .iter()
                    .any(|&x| QUARTER_TURNS.iter().any(|&(q2, _)| after(a, &[q1, x, q2]) == corner_solved))
            })
        };
        let parity: Vec<Option<bool>> = (0..NCCOS)
            .map(|a| {
                if name(a) != "4b2" {
                    return None;
                }
                let values = over_half_turn_routes(
                    cs,
                    a,
                    |b, m| (m == 1 || m == 4) && split_3_1(b),
                    |b| [trigger_solves(b), false],
                );
                match values {
                    [true, false] => Some(false),
                    [false, true] => Some(true),
                    _ => panic!("4b2 parity is not well defined for corner coset {a}"),
                }
            })
            .collect();

        // 2c3 direction: every half turn flips it
        let clockwise: Vec<Option<bool>> = (0..NCCOS)
            .map(|a| {
                if name(a) != "2c3" {
                    return None;
                }
                let progress = |b: usize| {
                    let mut shown = [false; 2];
                    for &(q, cw) in &QUARTER_TURNS {
                        if parity[cs.corner_mv[b][q]] == Some(false) {
                            shown[cw as usize] = true;
                        }
                    }
                    shown
                };
                match over_half_turn_routes(cs, a, |_, _| true, progress) {
                    [false, true] => Some(true),
                    [true, false] => Some(false),
                    _ => panic!("2c3 direction is not well defined for corner coset {a}"),
                }
            })
            .collect();

        Labels { parity, clockwise }
    }

    /// The label of a coset, if it is 4b2 or 2c3: "no parity", "parity", "clockwise", "anticlockwise".
    pub fn of(&self, coset: usize) -> Option<&'static str> {
        let a = coset / NEPAT;
        match (self.parity[a], self.clockwise[a]) {
            (Some(false), _) => Some("no parity"),
            (Some(true), _) => Some("parity"),
            (_, Some(true)) => Some("clockwise"),
            (_, Some(false)) => Some("anticlockwise"),
            _ => None,
        }
    }
}
