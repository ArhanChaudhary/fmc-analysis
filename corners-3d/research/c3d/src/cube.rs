//! The corners with DBL held fixed, turned by R, U and F only.
//!
//! Nothing here is typed in as a table.  A corner place is a vector (x, y, z) with x = +1 on R, y = +1 on U and
//! z = +1 on F.  A face turn is a rotation of space, and the place map and the twist it applies are worked out
//! from that rotation.
//!
//! A state is a pair (perm, ori) over the seven free places, in the order of [`PLACES`]:
//! `perm[p]` is the home place of the piece now at place `p`, and `ori[p]` its twist, 0 when the piece's U/D
//! sticker is on the U/D face, 1 when it sits one step clockwise from there (seen from outside the corner), 2
//! when one step counter-clockwise.

/// The number of states: 7! placements times 3^6 twists.
pub const N: usize = 5040 * 729;

/// The seven free places.  UFR is on all three faces that turn, the next three on two of them, the last three
/// on one.
pub const PLACES: [&str; 7] = ["UFR", "UFL", "UBR", "DFR", "UBL", "DFL", "DBR"];

/// (x, y, z) of each place of [`PLACES`]; DBL, the fixed corner, is (-1, -1, -1).
pub const XYZ: [[i8; 3]; 7] = [
    [1, 1, 1],
    [-1, 1, 1],
    [1, 1, -1],
    [1, -1, 1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, -1],
];

/// The nine turns, in the order R R2 R' U U2 U' F F2 F'.
pub const MOVES: [&str; 9] = ["R", "R2", "R'", "U", "U2", "U'", "F", "F2", "F'"];

/// The axis of a turn: 0 = R/L (x), 1 = U/D (y), 2 = F/B (z).
#[must_use]
pub const fn move_axis(m: usize) -> usize {
    m / 3
}

/// Whether turn `m` is a quarter turn.
#[must_use]
pub const fn is_quarter(m: usize) -> bool {
    m % 3 != 1
}

/// The turn that undoes turn `m`.
#[cfg(test)]
#[must_use]
pub const fn inverse_move(m: usize) -> usize {
    m - m % 3 + 2 - m % 3
}

/// The tetrad of a place: `true` for the places half turns can bring to DBL (UFL, UBR, DFR), `false` for
/// UFR, UBL, DFL, DBR.
#[must_use]
pub const fn tetrad(p: usize) -> bool {
    XYZ[p][0] * XYZ[p][1] * XYZ[p][2] < 0
}

/// What one corner shows.  The names say which of its three stickers are on a face of their own axis.
#[derive(Clone, Copy, PartialEq, Eq, Debug, Hash, PartialOrd, Ord)]
#[repr(u8)]
pub enum Kind {
    /// In its tetrad, all three stickers oriented.
    Good = 0,
    /// In its tetrad, twisted clockwise: no sticker oriented.
    TwistCw = 1,
    /// In its tetrad, twisted counter-clockwise: no sticker oriented.
    TwistCcw = 2,
    /// In the wrong tetrad, only the R/L sticker oriented.
    OutX = 3,
    /// In the wrong tetrad, only the U/D sticker oriented.
    OutY = 4,
    /// In the wrong tetrad, only the F/B sticker oriented.
    OutZ = 5,
}

/// A state of the seven free corners.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub struct State {
    pub perm: [u8; 7],
    pub ori: [u8; 7],
}

/// The place a quarter turn about `axis` sends (x, y, z) to, clockwise seen from the + side.
/// R: UFR -> UBR.  U: UFR -> UFL.  F: UFR -> DFR.
const fn rotate(axis: usize, v: [i8; 3]) -> [i8; 3] {
    match axis {
        0 => [v[0], v[2], -v[1]],
        1 => [-v[2], v[1], v[0]],
        _ => [v[1], -v[0], v[2]],
    }
}

/// The axis a sticker faces after a quarter turn about `axis`, if it faced `f` before.
const fn rotate_facing(axis: usize, f: usize) -> usize {
    if f == axis {
        f
    } else {
        3 - axis - f
    }
}

/// The faces around a place in clockwise order seen from outside, starting from the U/D face.
/// At UFR that is U, R, F.  A place of the other handedness has them in the order U/D, F/B, R/L.
const fn clockwise(p: usize) -> [usize; 3] {
    if tetrad(p) {
        [1, 2, 0]
    } else {
        [1, 0, 2]
    }
}

fn place_index(v: [i8; 3]) -> usize {
    XYZ.iter().position(|&w| w == v).expect("a free place")
}

/// The axis the U/D sticker of the piece at place `p` faces, given its twist.
#[must_use]
pub const fn ud_sticker_axis(p: usize, ori: u8) -> usize {
    clockwise(p)[ori as usize]
}

/// For each quarter turn (R, U, F) and each place: where the piece goes, and its new twist for each old one.
/// A place the turn leaves alone maps to itself.
struct Quarter {
    to: [usize; 7],
    twist: [[u8; 3]; 7],
}

fn quarter(axis: usize) -> Quarter {
    let mut to = [0; 7];
    let mut twist = [[0; 3]; 7];
    for p in 0..7 {
        if XYZ[p][axis] < 0 {
            to[p] = p;
            twist[p] = [0, 1, 2];
            continue;
        }
        let q = place_index(rotate(axis, XYZ[p]));
        to[p] = q;
        for o in 0..3u8 {
            let facing = rotate_facing(axis, ud_sticker_axis(p, o));
            let new = clockwise(q).iter().position(|&a| a == facing).expect("an axis");
            twist[p][o as usize] = u8::try_from(new).expect("0..3");
        }
    }
    Quarter { to, twist }
}

impl State {
    pub const SOLVED: Self = Self {
        perm: [0, 1, 2, 3, 4, 5, 6],
        ori: [0; 7],
    };

    /// One clockwise quarter turn about `axis`.
    fn quarter(&self, q: &Quarter) -> Self {
        let mut next = *self;
        for p in 0..7 {
            let d = q.to[p];
            next.perm[d] = self.perm[p];
            next.ori[d] = q.twist[p][self.ori[p] as usize];
        }
        next
    }

    /// What the corner at place `p` shows.
    #[must_use]
    pub fn kind(&self, p: usize) -> Kind {
        let home = self.perm[p] as usize;
        let o = self.ori[p];
        if tetrad(p) == tetrad(home) {
            return [Kind::Good, Kind::TwistCw, Kind::TwistCcw][o as usize];
        }
        // In the wrong tetrad two of the three stickers have changed places.  The U/D sticker faces `f`: if
        // that is U/D, the other two are swapped; otherwise it is swapped with the sticker of axis `f`, and
        // the third one is the oriented one.
        match ud_sticker_axis(p, o) {
            1 => Kind::OutY,
            0 => Kind::OutZ,
            _ => Kind::OutX,
        }
    }

    /// Whether the placement is an even permutation.  A quarter turn is a 4-cycle of places, so this flips with
    /// every quarter turn: HTR needs an even number of them from an even state and an odd number from an odd one.
    #[must_use]
    pub fn is_even(&self) -> bool {
        let inversions = (0..7)
            .flat_map(|i| (i + 1..7).map(move |j| (i, j)))
            .filter(|&(i, j)| self.perm[i] > self.perm[j]);
        inversions.count() % 2 == 0
    }

    /// The kinds at the seven places.
    #[must_use]
    pub fn kinds(&self) -> [Kind; 7] {
        std::array::from_fn(|p| self.kind(p))
    }

    /// Rank in 0..N: the placement in lexicographic order times 729, plus the twists of the first six places
    /// in base 3.
    #[must_use]
    pub fn index(&self) -> usize {
        let mut rank = 0;
        for i in 0..7 {
            let smaller = (i + 1..7).filter(|&j| self.perm[j] < self.perm[i]).count();
            rank = rank * (7 - i) + smaller;
        }
        let twist = self.ori[..6].iter().fold(0, |acc, &o| acc * 3 + o as usize);
        rank * 729 + twist
    }

    /// The state of rank `index`.
    #[must_use]
    pub fn from_index(index: usize) -> Self {
        let mut twist = index % 729;
        let mut rank = index / 729;
        let mut ori = [0u8; 7];
        let mut sum = 0;
        for i in (0..6).rev() {
            ori[i] = u8::try_from(twist % 3).expect("0..3");
            sum += twist % 3;
            twist /= 3;
        }
        ori[6] = u8::try_from((3 - sum % 3) % 3).expect("0..3");
        let mut digits = [0usize; 7];
        for i in (0..7).rev() {
            digits[i] = rank % (7 - i);
            rank /= 7 - i;
        }
        let mut left: Vec<u8> = (0..7).collect();
        let mut perm = [0u8; 7];
        for i in 0..7 {
            perm[i] = left.remove(digits[i]);
        }
        Self { perm, ori }
    }
}

/// The turn tables and everything built from them.
pub struct Cube {
    quarters: [Quarter; 3],
}

impl Default for Cube {
    fn default() -> Self {
        Self::new()
    }
}

impl Cube {
    #[must_use]
    pub fn new() -> Self {
        Self {
            quarters: [quarter(0), quarter(1), quarter(2)],
        }
    }

    /// The state after turn `m` (an index into [`MOVES`]).
    #[must_use]
    pub fn apply(&self, s: &State, m: usize) -> State {
        let q = &self.quarters[move_axis(m)];
        let mut t = *s;
        for _ in 0..=(m % 3) {
            t = t.quarter(q);
        }
        t
    }

    /// The state after a sequence of turns.
    #[must_use]
    pub fn apply_all(&self, s: &State, ms: &[usize]) -> State {
        ms.iter().fold(*s, |t, &m| self.apply(&t, m))
    }

    /// For each turn, the rank of the state it leads to from each state: `table[m][index]`.
    #[must_use]
    pub fn move_tables(&self) -> Vec<Vec<u32>> {
        (0..9)
            .map(|m| {
                (0..N)
                    .map(|i| {
                        u32::try_from(self.apply(&State::from_index(i), m).index()).expect("fits in u32")
                    })
                    .collect()
            })
            .collect()
    }
}

/// Reads a sequence such as `R U2 F'` into turn indices.  Only R, U and F turns exist here.
///
/// # Errors
/// Returns the first token that is not one of the nine turns.
pub fn parse(seq: &str) -> Result<Vec<usize>, String> {
    seq.split_whitespace()
        .map(|t| {
            let t = t.replace('\u{2019}', "'");
            MOVES.iter().position(|&m| m == t).ok_or(t)
        })
        .collect()
}

/// Writes turn indices as a sequence.
#[must_use]
pub fn show(ms: &[usize]) -> String {
    ms.iter().map(|&m| MOVES[m]).collect::<Vec<_>>().join(" ")
}

#[cfg(test)]
mod tests {
    use super::*;

    /// A second model that shares no code with the first: every piece carries its place and, for each of its
    /// three stickers (named by home axis), the direction it faces as a vector.
    #[derive(Clone)]
    struct Sticker {
        home: [i8; 3],
        at: [i8; 3],
        facing: [[i8; 3]; 3],
    }

    fn solved_stickers() -> Vec<Sticker> {
        XYZ.iter()
            .map(|&v| {
                let mut facing = [[0; 3]; 3];
                for a in 0..3 {
                    facing[a][a] = v[a];
                }
                Sticker {
                    home: v,
                    at: v,
                    facing,
                }
            })
            .collect()
    }

    fn turn_stickers(pieces: &mut [Sticker], axis: usize) {
        for piece in pieces.iter_mut().filter(|piece| piece.at[axis] > 0) {
            piece.at = rotate(axis, piece.at);
            for f in &mut piece.facing {
                *f = rotate(axis, *f);
            }
        }
    }

    /// Reads a state off the stickers: the twist is found by walking clockwise around the corner from the
    /// U/D face, with the cross product deciding what clockwise is.
    fn read_stickers(pieces: &[Sticker]) -> State {
        let mut s = State::SOLVED;
        for piece in pieces {
            let p = place_index(piece.at);
            s.perm[p] = u8::try_from(place_index(piece.home)).expect("0..7");
            let v = piece.at;
            // outward normals of the three faces at this place
            let n = [[v[0], 0, 0], [0, v[1], 0], [0, 0, v[2]]];
            let cross = |a: [i8; 3], b: [i8; 3]| {
                [
                    a[1] * b[2] - a[2] * b[1],
                    a[2] * b[0] - a[0] * b[2],
                    a[0] * b[1] - a[1] * b[0],
                ]
            };
            let dot = |a: [i8; 3], b: [i8; 3]| a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
            // seen from outside, b follows a clockwise when (a x b) points inward
            let other = if dot(cross(n[1], n[0]), v) < 0 {
                [0, 2]
            } else {
                [2, 0]
            };
            let order = [1, other[0], other[1]];
            let ud = piece.facing[1];
            let facing_axis = (0..3).find(|&a| ud[a] != 0).expect("faces some axis");
            s.ori[p] =
                u8::try_from(order.iter().position(|&a| a == facing_axis).expect("an axis")).expect("0..3");
        }
        s
    }

    #[test]
    fn index_round_trip() {
        for i in (0..N).step_by(997) {
            assert_eq!(State::from_index(i).index(), i);
        }
        assert_eq!(State::SOLVED.index(), 0);
    }

    #[test]
    fn agrees_with_the_sticker_model() {
        let cube = Cube::new();
        let mut seed = 0x9e37_79b9_7f4a_7c15_u64;
        for _ in 0..2000 {
            let mut pieces = solved_stickers();
            let mut s = State::SOLVED;
            for _ in 0..25 {
                seed ^= seed << 13;
                seed ^= seed >> 7;
                seed ^= seed << 17;
                let m = usize::try_from(seed % 9).expect("0..9");
                s = cube.apply(&s, m);
                for _ in 0..=(m % 3) {
                    turn_stickers(&mut pieces, move_axis(m));
                }
                assert_eq!(read_stickers(&pieces), s);
                // what each corner shows, read straight off the stickers
                for piece in &pieces {
                    let p = place_index(piece.at);
                    let oriented: Vec<bool> = (0..3).map(|a| piece.facing[a][a] != 0).collect();
                    let count = oriented.iter().filter(|&&b| b).count();
                    let same_tetrad = tetrad(p) == tetrad(place_index(piece.home));
                    match s.kind(p) {
                        Kind::Good => assert!(same_tetrad && count == 3),
                        Kind::TwistCw | Kind::TwistCcw => assert!(same_tetrad && count == 0),
                        Kind::OutX => assert!(!same_tetrad && oriented == [true, false, false]),
                        Kind::OutY => assert!(!same_tetrad && oriented == [false, true, false]),
                        Kind::OutZ => assert!(!same_tetrad && oriented == [false, false, true]),
                    }
                }
            }
        }
    }

    #[test]
    fn twists_sum_to_zero_and_turns_have_order_four() {
        let cube = Cube::new();
        for i in (0..N).step_by(1009) {
            let s = State::from_index(i);
            for m in [0, 3, 6] {
                let mut t = s;
                for _ in 0..4 {
                    t = cube.apply(&t, m);
                    assert_eq!(t.ori.iter().map(|&o| u32::from(o)).sum::<u32>() % 3, 0);
                }
                assert_eq!(t, s);
            }
            for m in 0..9 {
                assert_eq!(cube.apply(&cube.apply(&s, m), inverse_move(m)), s);
            }
        }
    }

    #[test]
    fn the_turns_are_the_usual_ones() {
        let cube = Cube::new();
        // R: UFR -> UBR -> DBR -> DFR.  U: UFR -> UFL -> UBL -> UBR.  F: UFR -> DFR -> DFL -> UFL.
        let name =
            |s: &State, home: usize| PLACES[s.perm.iter().position(|&h| h as usize == home).expect("there")];
        let r = cube.apply(&State::SOLVED, 0);
        assert_eq!(
            (name(&r, 0), name(&r, 2), name(&r, 6), name(&r, 3)),
            ("UBR", "DBR", "DFR", "UFR")
        );
        let u = cube.apply(&State::SOLVED, 3);
        assert_eq!(
            (name(&u, 0), name(&u, 1), name(&u, 4), name(&u, 2)),
            ("UFL", "UBL", "UBR", "UFR")
        );
        let f = cube.apply(&State::SOLVED, 6);
        assert_eq!(
            (name(&f, 0), name(&f, 3), name(&f, 5), name(&f, 1)),
            ("DFR", "DFL", "UFL", "UFR")
        );
        // U keeps every twist; R twists UFR clockwise on its way to UBR (the U sticker ends on B, and the
        // faces at UBR go U, B, R clockwise)
        assert_eq!(u.ori, [0; 7]);
        assert_eq!(r.ori[2], 1);
        // sexy move six times is the identity
        let sexy = parse("R U R' U'").expect("moves");
        let mut s = State::SOLVED;
        for _ in 0..6 {
            s = cube.apply_all(&s, &sexy);
        }
        assert_eq!(s, State::SOLVED);
    }
}
