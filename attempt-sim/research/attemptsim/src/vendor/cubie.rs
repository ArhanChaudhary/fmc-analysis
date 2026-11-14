//! A whole cube as corner and edge pieces with twists and flips (centers fixed), with the place numbering and the
//! orientation conventions of `research/src/coords.py`.  All move and rotation data are read from
//! `out/tables/cubie.txt`, which export_cubie.py computes from the sticker model.
//!
//!   cp[i], ct[i]   corner piece at place i (named by its home place) and its twist: the place's facelet, counted
//!                  clockwise from the U/D facelet, that holds the piece's U/D sticker
//!   ep[i], ef[i]   edge piece at place i and its flip (1 = its reference sticker is not on the reference facelet)
//!
//! Sequences compose left to right: `a.then(&b)` is "do a, then b".

use std::fs;

#[derive(Clone, Copy, PartialEq, Eq, Debug, Hash)]
pub struct Cubie {
    pub cp: [u8; 8],
    pub ct: [u8; 8],
    pub ep: [u8; 12],
    pub ef: [u8; 12],
}

#[derive(Clone, Copy)]
pub struct Map {
    pub cd: [u8; 8],
    pub ca: [u8; 8],
    pub ed: [u8; 12],
    pub ea: [u8; 12],
}

pub struct Model {
    pub moves: Vec<Map>,     // 18 face turns: 3 * face + (quarter turns - 1), faces U D R L F B
    pub rots: Vec<Map>,      // 24 rotations
    pub rot_axes: Vec<[u8; 3]>, // where each axis (0 R/L, 1 U/D, 2 F/B) goes under the rotation
    pub rot_faces: Vec<[u8; 6]>, // where each face (U D R L F B) goes under the rotation
    pub dr_c: [u8; 8],       // judging-a-dr corner position -> place here
    pub dr_e: [u8; 8],       // judging-a-dr U/D-layer edge position -> place here
    pub dr_s: [u8; 4],       // judging-a-dr E-slice position -> place here
    pub e_piece: [bool; 12], // the edge whose home is this place is an E-slice piece
    pub slot_kind: [u8; 12], // kind of each edge place: 0 E-slice, 1 M-slice, 2 S-slice
    pub comb: Vec<u16>,      // 12-bit mask with four bits set -> rank among the 495 (lexicographic by places)
    pub tests: Vec<String>,
}

pub const SOLVED: Cubie = Cubie {
    cp: [0, 1, 2, 3, 4, 5, 6, 7],
    ct: [0; 8],
    ep: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    ef: [0; 12],
};

// Two states with no symmetry between them, to recognise the inverse of a rotation: after U, and after R.
const SOLVED_PROBE: Cubie = Cubie { cp: [1, 0, 2, 3, 4, 5, 6, 7], ct: [1, 2, 0, 0, 0, 0, 0, 0], ep: [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ef: [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] };
const SOLVED_PROBE2: Cubie = Cubie { cp: [0, 1, 2, 3, 4, 5, 7, 6], ct: [0, 0, 0, 0, 0, 0, 2, 1], ep: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10], ef: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] };

fn parse_map(nums: &[u8]) -> Map {
    let mut m = Map { cd: [0; 8], ca: [0; 8], ed: [0; 12], ea: [0; 12] };
    m.cd.copy_from_slice(&nums[0..8]);
    m.ca.copy_from_slice(&nums[8..16]);
    m.ed.copy_from_slice(&nums[16..28]);
    m.ea.copy_from_slice(&nums[28..40]);
    m
}

impl Model {
    pub fn load(dir: &str) -> Model {
        let txt = fs::read_to_string(format!("{dir}/cubie.txt")).expect("cubie.txt");
        let mut section = "";
        let (mut moves, mut rots, mut rot_axes, mut drmap, mut tests) = (Vec::new(), Vec::new(), Vec::new(), Vec::new(), Vec::new());
        let mut slot_kind = [0u8; 12];
        let mut rot_faces = Vec::new();
        for line in txt.lines() {
            if ["moves", "rotations", "drmap", "slotkind", "tests"].contains(&line) {
                section = line;
                continue;
            }
            if section == "tests" {
                tests.push(line.to_string());
                continue;
            }
            let nums: Vec<u8> = line.split_whitespace().map(|x| x.parse().unwrap()).collect();
            match section {
                "moves" => moves.push(parse_map(&nums)),
                "rotations" => {
                    rots.push(parse_map(&nums));
                    rot_axes.push([nums[40], nums[41], nums[42]]);
                    rot_faces.push([nums[43], nums[44], nums[45], nums[46], nums[47], nums[48]]);
                }
                "drmap" => drmap.push(nums),
                "slotkind" => slot_kind.copy_from_slice(&nums),
                _ => {}
            }
        }
        assert!(moves.len() == 18 && rots.len() == 24 && drmap.len() == 3);
        let mut dr_c = [0u8; 8];
        dr_c.copy_from_slice(&drmap[0]);
        let mut dr_e = [0u8; 8];
        dr_e.copy_from_slice(&drmap[1]);
        let mut dr_s = [0u8; 4];
        dr_s.copy_from_slice(&drmap[2]);
        let mut e_piece = [false; 12];
        for &p in &dr_s {
            e_piece[p as usize] = true;
        }
        // rank of 4-subsets of 0..12 in lexicographic order (itertools.combinations)
        let mut comb = vec![0xFFFFu16; 1 << 12];
        let mut r = 0u16;
        for a in 0..12 {
            for b in a + 1..12 {
                for c in b + 1..12 {
                    for d in c + 1..12 {
                        comb[(1 << a) | (1 << b) | (1 << c) | (1 << d)] = r;
                        r += 1;
                    }
                }
            }
        }
        Model { moves, rots, rot_axes, rot_faces, dr_c, dr_e, dr_s, e_piece, slot_kind, comb, tests }
    }

    /// The state after one more face turn.
    #[inline]
    pub fn turn(&self, s: &Cubie, m: usize) -> Cubie {
        let mp = &self.moves[m];
        let mut t = *s;
        for i in 0..8 {
            let j = mp.cd[i] as usize;
            t.cp[j] = s.cp[i];
            t.ct[j] = (s.ct[i] + mp.ca[i]) % 3;
        }
        for i in 0..12 {
            let j = mp.ed[i] as usize;
            t.ep[j] = s.ep[i];
            t.ef[j] = s.ef[i] ^ mp.ea[i];
        }
        t
    }

    pub fn apply(&self, s: &Cubie, seq: &[usize]) -> Cubie {
        seq.iter().fold(*s, |a, &m| self.turn(&a, m))
    }

    /// The state seen after turning the whole cube by rotation r (pieces, places and colours all carried along).
    pub fn conj(&self, s: &Cubie, r: usize) -> Cubie {
        let mp = &self.rots[r];
        let mut t = *s;
        for i in 0..8 {
            let j = mp.cd[i] as usize;
            t.cp[j] = mp.cd[s.cp[i] as usize];
            t.ct[j] = (s.ct[i] + mp.ca[i] + 3 - mp.ca[s.cp[i] as usize]) % 3;
        }
        for i in 0..12 {
            let j = mp.ed[i] as usize;
            t.ep[j] = mp.ed[s.ep[i] as usize];
            t.ef[j] = s.ef[i] ^ mp.ea[i] ^ mp.ea[s.ep[i] as usize];
        }
        t
    }

    /// Undo `conj`: the state whose view after rotation r is `v`.
    pub fn conj_back(&self, v: &Cubie, r: usize) -> Cubie {
        let rinv = (0..24).find(|&q| self.conj(&self.conj(&SOLVED_PROBE, r), q) == SOLVED_PROBE && self.conj(&self.conj(&SOLVED_PROBE2, r), q) == SOLVED_PROBE2).unwrap();
        self.conj(v, rinv)
    }

    /// (co, eo, sl) as in coords.py.
    #[inline]
    pub fn coords(&self, s: &Cubie) -> (usize, usize, usize) {
        let mut co = 0usize;
        for i in (0..7).rev() {
            co = co * 3 + s.ct[i] as usize;
        }
        let mut eo = 0usize;
        let mut mask = 0usize;
        for i in 0..12 {
            if i < 11 {
                eo |= (s.ef[i] as usize) << i;
            }
            if self.e_piece[s.ep[i] as usize] {
                mask |= 1 << i;
            }
        }
        (co, eo, self.comb[mask] as usize)
    }

    /// For a state in the DR group on U/D: the three permutations in judging-a-dr's numbering
    /// (which piece sits at each position), or None if the state is not such a DR.
    pub fn dr_perms(&self, s: &Cubie) -> Option<([u8; 8], [u8; 8], [u8; 4])> {
        if s.ct != [0; 8] || s.ef != [0; 12] {
            return None;
        }
        let inv = |map: &[u8], x: u8| -> Option<u8> { map.iter().position(|&p| p == x).map(|k| k as u8) };
        let (mut c, mut e, mut sl) = ([0u8; 8], [0u8; 8], [0u8; 4]);
        for k in 0..8 {
            c[k] = inv(&self.dr_c, s.cp[self.dr_c[k] as usize])?;
            e[k] = inv(&self.dr_e, s.ep[self.dr_e[k] as usize])?;
        }
        for k in 0..4 {
            sl[k] = inv(&self.dr_s, s.ep[self.dr_s[k] as usize])?;
        }
        Some((c, e, sl))
    }

    /// Corner permutation in judging-a-dr's numbering of a state whose corners are oriented for U/D (edges ignored).
    pub fn dr_perms_corners(&self, s: &Cubie) -> ([u8; 8], (), ()) {
        assert!(s.ct == [0; 8]);
        let mut c = [0u8; 8];
        for k in 0..8 {
            c[k] = self.dr_c.iter().position(|&p| p == s.cp[self.dr_c[k] as usize]).unwrap() as u8;
        }
        (c, (), ())
    }

    /// A turn written in the view after rotation r, as the turn of the cube before the rotation.
    pub fn unview(&self, r: usize, mv: usize) -> usize {
        let face = self.rot_faces[r].iter().position(|&f| f as usize == mv / 3).unwrap();
        3 * face + mv % 3
    }

    /// A rotation carrying axis `from` to axis `to` (0 R/L, 1 U/D, 2 F/B); with `also`, a second axis pair as well.
    pub fn rot_for(&self, from: usize, to: usize, also: Option<(usize, usize)>) -> usize {
        (0..24)
            .find(|&r| self.rot_axes[r][from] as usize == to && also.map_or(true, |(a, b)| self.rot_axes[r][a] as usize == b))
            .unwrap()
    }
}

impl Cubie {
    /// "self, then b".
    pub fn then(&self, b: &Cubie) -> Cubie {
        let mut t = *self;
        for i in 0..8 {
            let q = b.cp[i] as usize;
            t.cp[i] = self.cp[q];
            t.ct[i] = (self.ct[q] + b.ct[i]) % 3;
        }
        for i in 0..12 {
            let q = b.ep[i] as usize;
            t.ep[i] = self.ep[q];
            t.ef[i] = self.ef[q] ^ b.ef[i];
        }
        t
    }

    pub fn inverse(&self) -> Cubie {
        let mut t = *self;
        for i in 0..8 {
            let p = self.cp[i] as usize;
            t.cp[p] = i as u8;
            t.ct[p] = (3 - self.ct[i]) % 3;
        }
        for i in 0..12 {
            let p = self.ep[i] as usize;
            t.ep[p] = i as u8;
            t.ef[p] = self.ef[i];
        }
        t
    }
}

/// Check the model against the vectors written by export_cubie.py.
pub fn selftest(dir: &str) {
    let m = Model::load(dir);
    let mut n = 0;
    for line in &m.tests {
        let parts: Vec<Vec<usize>> = line.split('|').map(|p| p.split_whitespace().map(|x| x.parse().unwrap()).collect()).collect();
        let s = m.apply(&SOLVED, &parts[0]);
        let as_vec = |c: &Cubie| -> Vec<usize> { c.cp.iter().chain(&c.ct).chain(&c.ep).chain(&c.ef).map(|&x| x as usize).collect() };
        assert_eq!(as_vec(&s), parts[1], "state");
        let (co, eo, sl) = m.coords(&s);
        assert_eq!(vec![co, eo, sl], parts[2], "coords");
        assert_eq!(as_vec(&m.conj(&s, parts[3][0])), parts[4], "rotation");
        assert_eq!(as_vec(&s.inverse()), parts[5], "inverse");
        assert_eq!(s.then(&s.inverse()), SOLVED);
        // then() agrees with applying moves
        let (a, b) = parts[0].split_at(10);
        assert_eq!(m.apply(&SOLVED, a).then(&m.apply(&SOLVED, b)), s);
        // turning the cube before a rotation = turning the viewed cube by the viewed turn
        let r = parts[3][0];
        for mv in 0..18 {
            assert_eq!(m.conj(&m.turn(&s, m.unview(r, mv)), r), m.turn(&m.conj(&s, r), mv), "view of a turn");
        }
        n += 1;
    }
    println!("cubie model: {n} test vectors ok");
}
