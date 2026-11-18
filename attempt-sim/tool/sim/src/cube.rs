//! The whole cube: eight corners and twelve edges with their orientations (the centres stay put).
//!
//! Places are numbered as in the DR model ([`crate::dr`]), so that a state in the DR group reads off directly:
//!
//! ```text
//!   corners : 0 UFR  1 UFL  2 UBL  3 UBR  4 DFR  5 DFL  6 DBL  7 DBR
//!   edges   : 0 UF   1 UL   2 UB   3 UR   4 DF   5 DL   6 DB   7 DR   8 FR  9 FL  10 BL  11 BR
//! ```
//!
//! A state says which piece sits at each place (pieces are named by their home place) and how it is turned there:
//!
//! * corner twist: how many clockwise steps (seen from outside) from the place's U/D facelet to the facelet that
//!   holds the piece's U/D sticker;
//! * edge flip: 0 if the piece's reference sticker is on the place's reference facelet, else 1.  The reference facelet
//!   is the U/D one for an edge of the U or D layer and the F/B one for an E-slice edge, so the flips are the
//!   edge orientation (EO) on the F/B axis: only F and B quarter turns change them.
//!
//! The moves are not typed in: [`MoveTables::new`] works them out from the geometry (a face turn rotates the stickers of
//! one layer by a quarter turn about the face's axis).
//!
//! Moves are numbered `3 * face + (quarter turns - 1)` with the faces U D R L F B = 0..5, so `U U2 U' D D2 D' R …`.
//! Axes are 0 R/L, 1 U/D, 2 F/B.

use std::fmt;

/// Faces in move-number order.
pub const FACE_NAMES: [char; 6] = ['U', 'D', 'R', 'L', 'F', 'B'];
/// The axis of each face (0 R/L, 1 U/D, 2 F/B).
pub const FACE_AXIS: [usize; 6] = [1, 1, 0, 0, 2, 2];
pub const AXIS_NAMES: [&str; 3] = ["R/L", "U/D", "F/B"];

/// One of the 18 face turns.
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
pub struct Move(pub u8);

impl Move {
    pub const COUNT: usize = 18;

    pub fn new(face: usize, quarter_turns: usize) -> Move {
        debug_assert!(face < 6 && (1..=3).contains(&quarter_turns));
        Move((3 * face + quarter_turns - 1) as u8)
    }
    #[inline]
    pub fn index(self) -> usize {
        self.0 as usize
    }
    #[inline]
    pub fn face(self) -> usize {
        (self.0 / 3) as usize
    }
    #[inline]
    pub fn axis(self) -> usize {
        FACE_AXIS[self.face()]
    }
    /// 1 (clockwise), 2 (half turn) or 3 (counterclockwise).
    #[inline]
    pub fn quarter_turns(self) -> usize {
        (self.0 % 3 + 1) as usize
    }
    #[inline]
    pub fn is_half_turn(self) -> bool {
        self.0 % 3 == 1
    }
    #[inline]
    pub fn inverse(self) -> Move {
        Move(3 * (self.0 / 3) + 2 - self.0 % 3)
    }
    /// The same turn made the other way (a quarter turn becomes its inverse; a half turn stays).
    #[inline]
    pub fn the_other_way(self) -> Move {
        self.inverse()
    }
    /// The same amount of turning on another face.
    #[inline]
    pub fn on_face(self, face: usize) -> Move {
        Move(3 * face as u8 + self.0 % 3)
    }
    /// Is this a quarter turn of a face of `axis`?
    #[inline]
    pub fn is_quarter_turn_of(self, axis: usize) -> bool {
        !self.is_half_turn() && self.axis() == axis
    }
    pub fn all() -> impl Iterator<Item = Move> {
        (0..18u8).map(Move)
    }
}

impl serde::Serialize for Move {
    fn serialize<S: serde::Serializer>(&self, s: S) -> Result<S::Ok, S::Error> {
        s.serialize_str(&self.to_string())
    }
}

impl fmt::Display for Move {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let suffix = ["", "2", "'"][self.0 as usize % 3];
        write!(f, "{}{}", FACE_NAMES[self.face()], suffix)
    }
}

/// A move sequence written out: `R U2 F'`.
pub fn format_moves(moves: &[Move]) -> String {
    moves.iter().map(|m| m.to_string()).collect::<Vec<_>>().join(" ")
}

/// Read a sequence of face turns (`R U2 F'`, also `R2'`, `R'2` and the typographic apostrophe).
pub fn parse_moves(text: &str) -> Result<Vec<Move>, String> {
    let mut out = Vec::new();
    for token in text.split_whitespace() {
        let mut chars = token.chars();
        let face_char = chars.next().unwrap();
        let face = FACE_NAMES
            .iter()
            .position(|&c| c == face_char)
            .ok_or_else(|| format!("'{token}' is not a face turn (only U D R L F B turns are allowed)"))?;
        let (mut two, mut prime) = (false, false);
        for c in chars {
            match c {
                '2' if !two => two = true,
                '\'' | '\u{2019}' if !prime => prime = true,
                _ => return Err(format!("'{token}' is not a face turn")),
            }
        }
        out.push(Move::new(face, if two { 2 } else if prime { 3 } else { 1 }));
    }
    Ok(out)
}

/// The inverse sequence.
pub fn invert(moves: &[Move]) -> Vec<Move> {
    moves.iter().rev().map(|m| m.inverse()).collect()
}

/// Merge turns of one face (also across a turn of the opposite face) until nothing merges: the length a judge
/// counts (HTM).
pub fn cancel(moves: &[Move]) -> Vec<Move> {
    let mut out: Vec<Move> = Vec::with_capacity(moves.len());
    for &m in moves {
        let mut j = out.len();
        let mut merged = false;
        while j > 0 {
            let p = out[j - 1];
            if p.face() == m.face() {
                let total = (p.quarter_turns() + m.quarter_turns()) % 4;
                if total == 0 {
                    out.remove(j - 1);
                } else {
                    out[j - 1] = Move::new(m.face(), total);
                }
                merged = true;
                break;
            }
            if p.axis() != m.axis() {
                break;
            }
            j -= 1;
        }
        if !merged {
            out.push(m);
        }
    }
    out
}

/// The search's canonical order: never the same face twice in a row, and of two opposite faces in a row the lower
/// one (U before D, R before L, F before B) first.  `last` is `None` at the start of a sequence.
#[inline]
pub fn canonical_after(last: Option<Move>, m: Move) -> bool {
    match last {
        None => true,
        Some(l) => !(l.face() == m.face() || (l.axis() == m.axis() && l.face() > m.face())),
    }
}

/// A cube state.  `a.then(&b)` is "a, then b".
#[derive(Clone, Copy, PartialEq, Eq, Hash, Debug)]
pub struct Cube {
    /// corner piece at each place
    pub cp: [u8; 8],
    /// twist of the corner at each place (0..3)
    pub co: [u8; 8],
    /// edge piece at each place
    pub ep: [u8; 12],
    /// flip of the edge at each place (0..2): the EO on F/B
    pub eo: [u8; 12],
}

impl Cube {
    pub const SOLVED: Cube = Cube {
        cp: [0, 1, 2, 3, 4, 5, 6, 7],
        co: [0; 8],
        ep: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        eo: [0; 12],
    };

    /// "self, then b".
    pub fn then(&self, b: &Cube) -> Cube {
        let mut t = *self;
        for i in 0..8 {
            let q = b.cp[i] as usize;
            t.cp[i] = self.cp[q];
            t.co[i] = (self.co[q] + b.co[i]) % 3;
        }
        for i in 0..12 {
            let q = b.ep[i] as usize;
            t.ep[i] = self.ep[q];
            t.eo[i] = self.eo[q] ^ b.eo[i];
        }
        t
    }

    pub fn inverse(&self) -> Cube {
        let mut t = *self;
        for i in 0..8 {
            let p = self.cp[i] as usize;
            t.cp[p] = i as u8;
            t.co[p] = (3 - self.co[i]) % 3;
        }
        for i in 0..12 {
            let p = self.ep[i] as usize;
            t.ep[p] = i as u8;
            t.eo[p] = self.eo[i];
        }
        t
    }

    /// Bad edges on F/B as an 11-bit pattern (the twelfth flip follows from the others).
    #[inline]
    pub fn flip_pattern(&self) -> usize {
        (0..11).fold(0, |acc, i| acc | (self.eo[i] as usize) << i)
    }

    /// Number of bad edges on F/B.
    pub fn bad_edges(&self) -> u32 {
        self.eo.iter().map(|&f| f as u32).sum()
    }

    /// The corner twists as a number 0..2187 (base 3, the eighth twist follows from the others).
    #[inline]
    pub fn twist_coord(&self) -> usize {
        (0..7).rev().fold(0, |acc, i| acc * 3 + self.co[i] as usize)
    }

    /// If the state is in the DR group on U/D (corners twisted right for U/D, edges good on F/B, E-slice edges in the E
    /// slice), the three permutations of the DR model: corners, U/D-layer edges, E-slice edges.
    pub fn dr_perms(&self) -> Option<([u8; 8], [u8; 8], [u8; 4])> {
        if self.co != [0; 8] || self.eo != [0; 12] {
            return None;
        }
        let mut e = [0u8; 8];
        let mut s = [0u8; 4];
        for i in 0..8 {
            if self.ep[i] >= 8 {
                return None;
            }
            e[i] = self.ep[i];
        }
        for i in 0..4 {
            if self.ep[8 + i] < 8 {
                return None;
            }
            s[i] = self.ep[8 + i] - 8;
        }
        Some((self.cp, e, s))
    }
}

/// Where each place goes under a turn and how the piece is turned on the way.
#[derive(Clone, Copy, Debug)]
struct PieceMap {
    corner_to: [u8; 8],
    corner_twist: [u8; 8],
    edge_to: [u8; 12],
    edge_flip: [u8; 12],
}

/// The 18 face turns as piece maps.
pub struct MoveTables {
    maps: [PieceMap; 18],
}

type V3 = [i32; 3];

fn cross(a: V3, b: V3) -> V3 {
    [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
}
fn dot(a: V3, b: V3) -> i32 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}

/// Outward normal of each face, with x to the right (R), y up (U), z to the front (F).
const FACE_NORMAL: [V3; 6] = [[0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]];

/// The faces of each place: corners and edges, by the numbering at the top of this file.
const CORNER_FACES: [[usize; 3]; 8] = [[0, 4, 2], [0, 4, 3], [0, 5, 3], [0, 5, 2], [1, 4, 2], [1, 4, 3], [1, 5, 3], [1, 5, 2]];
const EDGE_FACES: [[usize; 2]; 12] = [
    [0, 4], [0, 3], [0, 5], [0, 2], [1, 4], [1, 3], [1, 5], [1, 2], [4, 2], [4, 3], [5, 3], [5, 2],
];

fn position(faces: &[usize]) -> V3 {
    let mut p = [0; 3];
    for &f in faces {
        for k in 0..3 {
            p[k] += FACE_NORMAL[f][k];
        }
    }
    p
}

/// A corner's facelet normals in clockwise order seen from outside, starting with the U/D one.
fn corner_facelets(place: usize) -> [V3; 3] {
    let faces = CORNER_FACES[place];
    let v = position(&faces);
    let ud = FACE_NORMAL[faces[0]];
    let (a, b) = (FACE_NORMAL[faces[1]], FACE_NORMAL[faces[2]]);
    // (u × next) · v < 0 when `next` follows u clockwise
    if dot(cross(ud, a), v) < 0 {
        [ud, a, b]
    } else {
        [ud, b, a]
    }
}

/// An edge's facelet normals: the reference facelet first (U/D in the U and D layers, F/B in the E slice).
fn edge_facelets(place: usize) -> [V3; 2] {
    let [a, b] = EDGE_FACES[place];
    [FACE_NORMAL[a], FACE_NORMAL[b]]
}

/// A quarter turn clockwise (seen from outside) about the outward normal n: v -> n (n·v) - n × v.
fn quarter_turn(n: V3, v: V3) -> V3 {
    let c = cross(n, v);
    let d = dot(n, v);
    [n[0] * d - c[0], n[1] * d - c[1], n[2] * d - c[2]]
}

impl MoveTables {
    pub fn new() -> MoveTables {
        let corner_pos: Vec<V3> = (0..8).map(|p| position(&CORNER_FACES[p])).collect();
        let edge_pos: Vec<V3> = (0..12).map(|p| position(&EDGE_FACES[p])).collect();
        let quarter: Vec<PieceMap> = (0..6)
            .map(|face| {
                let n = FACE_NORMAL[face];
                let turn = |v: V3| if dot(n, v) > 0 { quarter_turn(n, v) } else { v };
                let mut map = PieceMap { corner_to: [0; 8], corner_twist: [0; 8], edge_to: [0; 12], edge_flip: [0; 12] };
                for p in 0..8 {
                    let q = corner_pos.iter().position(|&x| x == turn(corner_pos[p])).unwrap();
                    // where the U/D facelet of place p lands, as a facelet of place q; a layer turn only moves the
                    // stickers of the layer (the others keep their normals)
                    let moved = if dot(n, corner_pos[p]) > 0 { quarter_turn(n, corner_facelets(p)[0]) } else { corner_facelets(p)[0] };
                    map.corner_to[p] = q as u8;
                    map.corner_twist[p] = corner_facelets(q).iter().position(|&f| f == moved).unwrap() as u8;
                }
                for p in 0..12 {
                    let q = edge_pos.iter().position(|&x| x == turn(edge_pos[p])).unwrap();
                    let moved = if dot(n, edge_pos[p]) > 0 { quarter_turn(n, edge_facelets(p)[0]) } else { edge_facelets(p)[0] };
                    map.edge_to[p] = q as u8;
                    map.edge_flip[p] = edge_facelets(q).iter().position(|&f| f == moved).unwrap() as u8;
                }
                map
            })
            .collect();
        // a move turned k quarter turns: the quarter turn composed k times
        let maps = std::array::from_fn(|m| {
            let (face, k) = (m / 3, m % 3 + 1);
            let q = &quarter[face];
            let mut map = PieceMap {
                corner_to: std::array::from_fn(|p| p as u8),
                corner_twist: [0; 8],
                edge_to: std::array::from_fn(|p| p as u8),
                edge_flip: [0; 12],
            };
            for _ in 0..k {
                for p in 0..8 {
                    let at = map.corner_to[p] as usize;
                    map.corner_twist[p] = (map.corner_twist[p] + q.corner_twist[at]) % 3;
                    map.corner_to[p] = q.corner_to[at];
                }
                for p in 0..12 {
                    let at = map.edge_to[p] as usize;
                    map.edge_flip[p] ^= q.edge_flip[at];
                    map.edge_to[p] = q.edge_to[at];
                }
            }
            map
        });
        MoveTables { maps }
    }

    /// The state after one more turn.
    #[inline]
    pub fn turn(&self, s: &Cube, m: Move) -> Cube {
        let map = &self.maps[m.index()];
        let mut t = *s;
        for i in 0..8 {
            let j = map.corner_to[i] as usize;
            t.cp[j] = s.cp[i];
            t.co[j] = (s.co[i] + map.corner_twist[i]) % 3;
        }
        for i in 0..12 {
            let j = map.edge_to[i] as usize;
            t.ep[j] = s.ep[i];
            t.eo[j] = s.eo[i] ^ map.edge_flip[i];
        }
        t
    }

    pub fn apply(&self, s: &Cube, moves: &[Move]) -> Cube {
        moves.iter().fold(*s, |a, &m| self.turn(&a, m))
    }

    /// The state of a move sequence applied to the solved cube.
    pub fn state(&self, moves: &[Move]) -> Cube {
        self.apply(&Cube::SOLVED, moves)
    }

    /// The single-move states.
    pub fn move_cube(&self, m: Move) -> Cube {
        self.turn(&Cube::SOLVED, m)
    }
}

impl Default for MoveTables {
    fn default() -> Self {
        Self::new()
    }
}

/// A *view*: the cube looked at after a whole-cube rotation, given by where each face goes.  The views used are the
/// ones that bring an EO axis to F/B (and a DR axis to U/D); a state is looked at in a view by making every turn of
/// its sequence on the face the rotation takes it to.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct View {
    /// `to_view[f]`: the face that face f becomes in the view
    to_view: [u8; 6],
    from_view: [u8; 6],
}

impl View {
    pub const fn new(to_view: [u8; 6]) -> View {
        let mut from_view = [0u8; 6];
        let mut f = 0;
        while f < 6 {
            from_view[to_view[f] as usize] = f as u8;
            f += 1;
        }
        View { to_view, from_view }
    }
    /// A turn of the cube, as the turn of the view.
    #[inline]
    pub fn to_view(&self, m: Move) -> Move {
        m.on_face(self.to_view[m.face()] as usize)
    }
    /// A turn of the view, as the turn of the cube.
    #[inline]
    pub fn from_view(&self, m: Move) -> Move {
        m.on_face(self.from_view[m.face()] as usize)
    }
    pub fn seq_to_view(&self, moves: &[Move]) -> Vec<Move> {
        moves.iter().map(|&m| self.to_view(m)).collect()
    }
    pub fn seq_from_view(&self, moves: &[Move]) -> Vec<Move> {
        moves.iter().map(|&m| self.from_view(m)).collect()
    }
}

// Face numbers for the view constants below.
const U: u8 = 0;
const D: u8 = 1;
const R: u8 = 2;
const L: u8 = 3;
const F: u8 = 4;
const B: u8 = 5;

/// The view that puts EO axis y on F/B, for y = R/L, U/D, F/B.  (These are the rotations the research simulator
/// picked; the search's canonical order depends on the face names in the view, so they are kept exactly.)
pub const EO_VIEW: [View; 3] = [
    View::new([U, D, F, B, L, R]), // R/L: y-like, R->F L->B F->L B->R
    View::new([B, F, R, L, U, D]), // U/D: U->B D->F F->U B->D
    View::new([U, D, R, L, F, B]), // F/B: as it is
];

/// `DR_VIEW[x][y]`: the view that puts DR axis x on U/D and EO axis y on F/B (x != y).
pub const DR_VIEW: [[View; 3]; 3] = [
    [
        View::new([U, D, R, L, F, B]), // unused (x = y)
        View::new([F, B, D, U, L, R]), // DR on R/L, EO on U/D
        View::new([R, L, D, U, F, B]), // DR on R/L, EO on F/B
    ],
    [
        View::new([U, D, F, B, L, R]), // DR on U/D, EO on R/L
        View::new([U, D, R, L, F, B]), // unused
        View::new([U, D, R, L, F, B]), // DR on U/D, EO on F/B
    ],
    [
        View::new([R, L, F, B, U, D]), // DR on F/B, EO on R/L
        View::new([B, F, R, L, U, D]), // DR on F/B, EO on U/D
        View::new([U, D, R, L, F, B]), // unused
    ],
];

#[cfg(test)]
mod tests {
    use super::*;

    fn seq(s: &str) -> Vec<Move> {
        parse_moves(s).unwrap()
    }

    #[test]
    fn every_move_has_the_right_order() {
        let t = MoveTables::new();
        for m in Move::all() {
            let order = if m.is_half_turn() { 2 } else { 4 };
            let mut c = Cube::SOLVED;
            for k in 1..=order {
                c = t.turn(&c, m);
                assert_eq!(c == Cube::SOLVED, k == order, "{m}");
            }
            assert_eq!(t.turn(&t.move_cube(m), m.inverse()), Cube::SOLVED);
        }
    }

    #[test]
    fn orientation_conventions() {
        let t = MoveTables::new();
        for m in Move::all() {
            let c = t.move_cube(m);
            // only F and B quarter turns flip edges, only R L F B quarter turns twist corners
            assert_eq!(c.eo.iter().any(|&f| f != 0), !m.is_half_turn() && m.axis() == 2, "{m}");
            assert_eq!(c.co.iter().any(|&x| x != 0), !m.is_half_turn() && m.axis() != 1, "{m}");
            assert_eq!(c.co.iter().map(|&x| x as u32).sum::<u32>() % 3, 0);
        }
        // U turns UFR to UFL (clockwise from above), D turns DFL to DFR
        assert_eq!(t.move_cube(seq("U")[0]).cp[1], 0);
        assert_eq!(t.move_cube(seq("D")[0]).cp[4], 5);
    }

    #[test]
    fn known_states() {
        let t = MoveTables::new();
        // (R U R' U') six times is solved
        let sexy = seq("R U R' U'");
        let mut c = Cube::SOLVED;
        for _ in 0..6 {
            c = t.apply(&c, &sexy);
        }
        assert_eq!(c, Cube::SOLVED);
        // a superflip: every edge flipped in place, corners solved
        let sf = t.state(&seq("U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2"));
        assert_eq!(sf.cp, Cube::SOLVED.cp);
        assert_eq!(sf.co, [0; 8]);
        assert_eq!(sf.ep, Cube::SOLVED.ep);
        assert_eq!(sf.eo, [1; 12]);
    }

    #[test]
    fn then_and_inverse_agree_with_turning() {
        let t = MoveTables::new();
        let a = seq("R U2 F' L D B2 R'");
        let b = seq("F2 U' L2 B D' R");
        let mut ab = a.clone();
        ab.extend(&b);
        assert_eq!(t.state(&a).then(&t.state(&b)), t.state(&ab));
        assert_eq!(t.state(&a).inverse(), t.state(&invert(&a)));
    }

    #[test]
    fn views_are_rotations() {
        // a view must turn a solved-looking relation into another: the commutator of two faces in the view has the same
        // order as in the cube, and opposite faces stay opposite
        for v in EO_VIEW.iter().chain(DR_VIEW.iter().flatten()) {
            for f in 0..6 {
                let g = v.to_view[f] as usize;
                assert_eq!(v.to_view[f ^ 1] as usize, g ^ 1);
                assert_eq!(v.from_view[g] as usize, f);
            }
        }
        // EO_VIEW[y] puts axis y on F/B; DR_VIEW[x][y] puts x on U/D and y on F/B
        for y in 0..3 {
            let face = (0..6).find(|&f| FACE_AXIS[f] == y).unwrap();
            assert_eq!(FACE_AXIS[EO_VIEW[y].to_view[face] as usize], 2);
            for x in (0..3).filter(|&x| x != y) {
                let fx = (0..6).find(|&f| FACE_AXIS[f] == x).unwrap();
                assert_eq!(FACE_AXIS[DR_VIEW[x][y].to_view[fx] as usize], 1);
                assert_eq!(FACE_AXIS[DR_VIEW[x][y].to_view[face] as usize], 2);
            }
        }
    }

    #[test]
    fn cancel_merges_across_the_opposite_face() {
        assert_eq!(format_moves(&cancel(&seq("R L R'"))), "L");
        assert_eq!(format_moves(&cancel(&seq("U D2 U2 D2 U"))), "");
        assert_eq!(format_moves(&cancel(&seq("F R R U"))), "F R2 U");
        assert_eq!(format_moves(&cancel(&seq("F R R2 R U"))), "F U");
    }

    #[test]
    fn parsing() {
        assert_eq!(format_moves(&seq("R U2 F' L2' D\u{2019}")), "R U2 F' L2 D'");
        assert!(parse_moves("R x2").is_err());
        assert!(parse_moves("Rw").is_err());
    }
}
