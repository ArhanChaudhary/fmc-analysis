//! Reorienting the whole cube, and how a solver's DR relates to the case listed for it.
//!
//! A *rotation* reorients the whole cube without moving any face (x, y, z and their combinations: 24 of them, named
//! here by the shortest sequence of x, y and z rotations, as `y x2`); a *mirror* swaps left and right.  A DR is listed
//! as it is drawn, or else it is a listed case rotated, mirrored or with the E slice turned a quarter: [`relate`] finds
//! the plainest of these that makes it exactly the listed case, on the whole-cube model (the turns of the solver's
//! own sequence, renamed).

use attempt_sim::cube::{Move, MoveTables};
use attempt_sim::dr::rank_perm;
use attempt_sim::htr::{Htr, NEPAT};

/// A reorientation of the whole cube: where each face goes (U D R L F B = 0..5), and whether it is a mirror image.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub struct Orientation {
    to: [u8; 6],
    mirror: bool,
}

impl Orientation {
    pub const NONE: Orientation = Orientation { to: [0, 1, 2, 3, 4, 5], mirror: false };
    /// x: the whole cube as R turns (F to U, U to B); y: as U turns (F to L); z: as F turns (U to R)
    pub const X: Orientation = Orientation { to: [5, 4, 2, 3, 0, 1], mirror: false };
    pub const Y: Orientation = Orientation { to: [0, 1, 4, 5, 3, 2], mirror: false };
    pub const Z: Orientation = Orientation { to: [2, 3, 1, 0, 4, 5], mirror: false };
    /// left and right swapped
    pub const MIRROR: Orientation = Orientation { to: [0, 1, 3, 2, 4, 5], mirror: true };

    /// This reorientation, then `other`.
    pub fn then(self, other: Orientation) -> Orientation {
        Orientation { to: std::array::from_fn(|f| other.to[self.to[f] as usize]), mirror: self.mirror != other.mirror }
    }

    /// A turn as named after this reorientation (a mirror turns it the other way).
    pub fn turn(self, m: Move) -> Move {
        let q = m.quarter_turns();
        Move::new(self.to[m.face()] as usize, if self.mirror { 4 - q } else { q })
    }
}

/// The 24 rotations, each with its shortest name in x, y and z ("" for none; y before x before z), shortest first.
pub fn rotations() -> Vec<(String, Orientation)> {
    let mut tokens: Vec<(String, Orientation)> = Vec::new();
    for (name, r) in [("y", Orientation::Y), ("x", Orientation::X), ("z", Orientation::Z)] {
        let (r2, r3) = (r.then(r), r.then(r).then(r));
        tokens.extend([(name.to_string(), r), (format!("{name}'"), r3), (format!("{name}2"), r2)]);
    }
    let mut out: Vec<(String, Orientation)> = vec![(String::new(), Orientation::NONE)];
    let add = |name: String, o: Orientation, out: &mut Vec<(String, Orientation)>| {
        if !out.iter().any(|(_, p)| *p == o) {
            out.push((name, o));
        }
    };
    for (n, o) in &tokens {
        add(n.clone(), *o, &mut out);
    }
    for (n1, o1) in &tokens {
        for (n2, o2) in &tokens {
            add(format!("{n1} {n2}"), o1.then(*o2), &mut out);
        }
    }
    assert_eq!(out.len(), 24);
    out
}

/// How a DR is the case listed for it: rotate it, then mirror it, then turn the E slice a quarter (E, the way D
/// turns), and it is that case exactly as drawn.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Relation {
    /// the rotation, in x, y and z ("" for none)
    pub rotation: String,
    pub mirror: bool,
    pub slice: bool,
}

impl Relation {
    /// Is it the listed case as it is?
    pub fn identical(&self) -> bool {
        self.rotation.is_empty() && !self.mirror && !self.slice
    }

    /// The steps, in order: "rotate y x2", "mirror it (left and right swapped)", "turn the E slice a quarter (E)".
    pub fn steps(&self) -> Vec<String> {
        let mut out = Vec::new();
        if !self.rotation.is_empty() {
            out.push(format!("rotate {}", self.rotation));
        }
        if self.mirror {
            out.push("mirror it (left and right swapped)".to_string());
        }
        if self.slice {
            out.push("turn the E slice a quarter (E)".to_string());
        }
        out
    }
}

/// The coset (`Cosets` numbering) of a cube in DR on U/D, if it is one.
pub fn coset_of(htr: &Htr, cube: &MoveTables, moves: &[Move]) -> Option<usize> {
    let (c, e, _) = cube.state(moves).dr_perms()?;
    Some(htr.ccos[rank_perm(&c)] as usize * NEPAT + htr.epat[rank_perm(&e)] as usize)
}

/// The plainest way the cube `moves` make (from solved, in the solver's own frame) is the listed coset `target`: no
/// E slice before the E slice, no mirror before a mirror, then the shortest rotation.  The E slice turned is E: U D',
/// then the whole cube rotated y' (so the centres stay put).
pub fn relate(
    htr: &Htr,
    cube: &MoveTables,
    rotations: &[(String, Orientation)],
    moves: &[Move],
    target: usize,
) -> Option<Relation> {
    let y3 = Orientation::Y.then(Orientation::Y).then(Orientation::Y);
    for slice in [false, true] {
        for mirror in [false, true] {
            for (name, r) in rotations {
                let o = if mirror { r.then(Orientation::MIRROR) } else { *r };
                let mut seq: Vec<Move> = moves.iter().map(|&m| o.turn(m)).collect();
                if slice {
                    seq.extend([Move::new(0, 1), Move::new(1, 3)]);
                    seq = seq.iter().map(|&m| y3.turn(m)).collect();
                }
                if coset_of(htr, cube, &seq) == Some(target) {
                    return Some(Relation { rotation: name.clone(), mirror, slice });
                }
            }
        }
    }
    None
}
