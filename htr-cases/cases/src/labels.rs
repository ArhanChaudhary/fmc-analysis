//! The properties solvers use to tell apart HTR cases whose bad pieces look the same: 4b2 parity, 2c3 direction, and
//! good or bad 2c4 and 4a3.  All are computed per corner coset from the solvers' own rules, and all turn out to be well
//! defined (the same on every route, or from every side the rule can be read from; `cargo test` checks it).
//!
//! * **4b2 parity** (*Hitchhiker's Guide to HTR*, "How to solve 4b2"): set the corners up for a 2-quarter-turn trigger
//!   (Q X2 Q, X a side face) with half turns, counting every U2 or D2 done while the bad corners split 3/1 between U
//!   and D.  An even count means the trigger then gives real HTR: no parity.  An odd count: parity.
//! * **2c3 direction** (same guide, "How to solve 2c3", and the server: "every half turn you do on a 2c3 changes the
//!   qt direction"): from the position shown, the quarter turn that brings it to 4b2 with no parity goes clockwise or
//!   anticlockwise (U and D each seen from its own face), every half turn done before it flipping the direction.
//! * **2c4 and 4a3, good or bad**: a sequence *progresses* when it brings the corners a quarter turn closer to HTR,
//!   half turns counting nothing: the number of the subset goes down (2c4 to a 3, 4a3 to a 2).  A 2c4 is good when,
//!   with its bad corners on UFR and UFL, U and B2 U both progress; on UBL and DFR, F2 U and R2 U; stacked on UFR and
//!   DFR, U2 R2 U and U2 F2 U.  A 4a3 is good when, with its bad corners as bars on U and D, U progresses; all on U,
//!   F2 U.  Otherwise bad, and a 4a3 with its corners on diagonals of U and D is neither.  (U or U' makes no
//!   difference: they are a free U2 apart.)  The bad corners are those of the frame with few of them, as subsets are
//!   named.

use crate::cosets::Cosets;
use attempt_sim::dr::{HALF_MOVES, MOVE_IS_QUARTER, NSYM};
use attempt_sim::htr::{NCCOS, NEPAT, SUBSET_NAMES};
use std::collections::{BTreeSet, VecDeque};

/// U, U', D, D' as DR moves, and whether each is clockwise seen from its own face.
const QUARTER_TURNS: [(usize, bool); 4] = [(0, true), (2, false), (3, true), (5, false)];
const SIDE_HALF_TURNS: [usize; 4] = [6, 7, 8, 9];
/// DR move numbers
const U: usize = 0;
const U2: usize = 1;
const R2: usize = 6;
const F2: usize = 8;
const B2: usize = 9;

/// A set of corner places as a mask (bit p: place p, in the order UFR UFL UBL UBR DFR DFL DBL DBR).
const fn places(list: &[usize]) -> u8 {
    let mut mask = 0;
    let mut i = 0;
    while i < list.len() {
        mask |= 1 << list[i];
        i += 1;
    }
    mask
}
const UFR: usize = 0;
const UFL: usize = 1;
const UBL: usize = 2;
const DFR: usize = 4;

/// Two bad corners next to each other on one layer: a bar.
fn bar(layer: u8) -> bool {
    [0b0011, 0b0110, 0b1100, 0b1001].contains(&layer)
}

/// A rule for good and bad: where the bad corners must be, and the sequences that must all progress from there.
struct Rule {
    at: fn(u8) -> bool,
    progress: &'static [&'static [usize]],
}

const RULES_2C4: [Rule; 3] = [
    Rule { at: |m| m == places(&[UFR, UFL]), progress: &[&[U], &[B2, U]] },
    Rule { at: |m| m == places(&[UBL, DFR]), progress: &[&[F2, U], &[R2, U]] },
    Rule { at: |m| m == places(&[UFR, DFR]), progress: &[&[U2, R2, U], &[U2, F2, U]] },
];
const RULES_4A3: [Rule; 2] = [
    Rule { at: |m| bar(m & 0x0F) && bar(m >> 4), progress: &[&[U]] },
    Rule { at: |m| m == 0x0F, progress: &[&[F2, U]] },
];

pub struct Labels {
    /// per corner coset: for 4b2, Some(true) if it has parity
    pub parity: Vec<Option<bool>>,
    /// per corner coset: for 2c3, Some(true) if its quarter turn goes clockwise
    pub clockwise: Vec<Option<bool>>,
    /// per corner coset: for 2c4 and 4a3, Some(true) if good (None for a 4a3 with its corners on diagonals)
    pub good: Vec<Option<bool>>,
    /// per corner coset: the fewest quarter turns that put the corners in HTR, half turns counting nothing (the
    /// number of the subset)
    pub quarter_turns: Vec<u8>,
}

/// The fewest quarter turns to put the corners in HTR, half turns free (a 0-1 breadth-first search; the DR moves
/// are their own inverses' set, so the distance from HTR is the distance to it).
fn quarter_turns(cs: &Cosets) -> Vec<u8> {
    let mut d = vec![u8::MAX; NCCOS];
    let start = cs.solved / NEPAT;
    d[start] = 0;
    let mut queue = VecDeque::from([start]);
    while let Some(a) = queue.pop_front() {
        for (m, &quarter) in MOVE_IS_QUARTER.iter().enumerate() {
            let (b, w) = (cs.corner_mv[a][m], quarter as u8);
            if d[a] + w < d[b] {
                d[b] = d[a] + w;
                if w == 0 {
                    queue.push_front(b);
                } else {
                    queue.push_back(b);
                }
            }
        }
    }
    d
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

        // 2c4 and 4a3: good or bad, read from every side that puts the bad corners where a rule wants them.  The bad
        // corners are those of the frame with few of them (a 2c4 with the E slice turned has 6, and is read from its
        // 2): turning the E slice keeps the number of the subset, and so whether a turn progresses.
        let qt = quarter_turns(cs);
        let few = |m: u8| if m.count_ones() > 4 { !m } else { m };
        let progresses = |b: usize, seq: &[usize]| qt[after(b, seq)] < qt[b];
        let good: Vec<Option<bool>> = (0..NCCOS)
            .map(|a| {
                let rules: &[Rule] = match name(a) {
                    "2c4" => &RULES_2C4,
                    "4a3" => &RULES_4A3,
                    _ => return None,
                };
                let mut seen = BTreeSet::new();
                for s in 0..NSYM {
                    let b = cs.sym[a * NEPAT][s] as usize / NEPAT;
                    for rule in rules.iter().filter(|r| (r.at)(few(corner_mask(b)))) {
                        seen.insert(rule.progress.iter().all(|seq| progresses(b, seq)));
                    }
                }
                match (seen.len(), name(a)) {
                    (1, _) => seen.first().copied(),
                    (0, "4a3") => None, // its corners on diagonals
                    _ => panic!("good or bad is not well defined for corner coset {a} ({}): {seen:?}", name(a)),
                }
            })
            .collect();

        Labels { parity, clockwise, good, quarter_turns: qt }
    }

    /// The label of a coset, if it is 4b2, 2c3, 2c4 or 4a3: "no parity", "parity", "clockwise", "anticlockwise",
    /// "good", "bad" (none for a 4a3 with its corners on diagonals).
    pub fn of(&self, coset: usize) -> Option<&'static str> {
        let a = coset / NEPAT;
        match (self.parity[a], self.clockwise[a], self.good[a]) {
            (Some(false), _, _) => Some("no parity"),
            (Some(true), _, _) => Some("parity"),
            (_, Some(true), _) => Some("clockwise"),
            (_, Some(false), _) => Some("anticlockwise"),
            (_, _, Some(true)) => Some("good"),
            (_, _, Some(false)) => Some("bad"),
            _ => None,
        }
    }
}
