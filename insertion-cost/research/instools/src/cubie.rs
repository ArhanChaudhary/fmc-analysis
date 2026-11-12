//! A whole cube as corner and edge pieces with twists and flips (centers fixed).  All move and rotation data are read
//! from `out/tables/cubie.txt`, which `src/export_tables.py` computes from the sticker model `src/cube.py`.
//!
//!   cp[i], ct[i]   corner piece at place i (named by its home place) and its twist
//!   ep[i], ef[i]   edge piece at place i and its flip
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
    pub moves: Vec<Map>,          // 18 face turns: 3 * face + (quarter turns - 1), faces U D R L F B
    pub rots: Vec<Map>,           // 24 rotations
    pub rot_faces: Vec<[u8; 6]>,  // where each face (U D R L F B) goes under the rotation
    pub move_state: Vec<Cubie>,   // the state after each single turn
    pub cnames: Vec<String>,
    pub enames: Vec<String>,
    pub tests: Vec<String>,
    pub cancel_tests: Vec<String>,
}

pub const SOLVED: Cubie = Cubie { cp: [0, 1, 2, 3, 4, 5, 6, 7], ct: [0; 8], ep: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ef: [0; 12] };

fn parse_map(nums: &[u8]) -> Map {
    let mut m = Map { cd: [0; 8], ca: [0; 8], ed: [0; 12], ea: [0; 12] };
    m.cd.copy_from_slice(&nums[0..8]);
    m.ca.copy_from_slice(&nums[8..16]);
    m.ed.copy_from_slice(&nums[16..28]);
    m.ea.copy_from_slice(&nums[28..40]);
    m
}

pub fn out_dir() -> String {
    std::env::var("INSTOOLS_OUT").unwrap_or_else(|_| concat!(env!("CARGO_MANIFEST_DIR"), "/../out").to_string())
}

impl Model {
    pub fn load() -> Model {
        let path = format!("{}/tables/cubie.txt", out_dir());
        let txt = fs::read_to_string(&path).unwrap_or_else(|_| panic!("cannot read {path}: run src/export_tables.py"));
        let mut section = "";
        let (mut moves, mut rots, mut rot_faces, mut tests, mut cancel_tests, mut names) = (Vec::new(), Vec::new(), Vec::new(), Vec::new(), Vec::new(), Vec::new());
        for line in txt.lines() {
            if ["moves", "rotations", "names", "tests", "cancel"].contains(&line) {
                section = line;
                continue;
            }
            match section {
                "tests" => tests.push(line.to_string()),
                "cancel" => cancel_tests.push(line.to_string()),
                "names" => names.push(line.split_whitespace().map(|s| s.to_string()).collect::<Vec<_>>()),
                _ => {
                    let nums: Vec<u8> = line.split_whitespace().map(|x| x.parse().unwrap()).collect();
                    if section == "moves" {
                        moves.push(parse_map(&nums));
                    } else {
                        rots.push(parse_map(&nums));
                        rot_faces.push([nums[40], nums[41], nums[42], nums[43], nums[44], nums[45]]);
                    }
                }
            }
        }
        assert!(moves.len() == 18 && rots.len() == 24 && names.len() == 2);
        let mut m = Model { moves, rots, rot_faces, move_state: Vec::new(), cnames: names[0].clone(), enames: names[1].clone(), tests, cancel_tests };
        m.move_state = (0..18).map(|mv| m.turn(&SOLVED, mv)).collect();
        m
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

    pub fn apply(&self, s: &Cubie, seq: &[u8]) -> Cubie {
        seq.iter().fold(*s, |a, &m| self.turn(&a, m as usize))
    }

    pub fn state(&self, seq: &[u8]) -> Cubie {
        self.apply(&SOLVED, seq)
    }

    /// m · g · m^-1 for a face turn m (do m, then g, then undo m).
    #[inline]
    pub fn conj_move(&self, g: &Cubie, m: usize) -> Cubie {
        let t = self.move_state[m].then(g);
        self.turn(&t, 3 * (m / 3) + 2 - m % 3)
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
}

impl Cubie {
    /// "self, then b".
    #[inline]
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

    #[inline]
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

    /// Corners packed in 40 bits.
    #[inline]
    pub fn ckey(&self) -> u64 {
        let mut k = 0u64;
        for i in 0..8 {
            k |= ((self.cp[i] | (self.ct[i] << 3)) as u64) << (5 * i);
        }
        k
    }
    /// Edges packed in 60 bits.
    #[inline]
    pub fn ekey(&self) -> u64 {
        let mut k = 0u64;
        for i in 0..12 {
            k |= ((self.ep[i] | (self.ef[i] << 4)) as u64) << (5 * i);
        }
        k
    }
    #[inline]
    pub fn key(&self) -> u128 {
        (self.ckey() as u128) << 64 | self.ekey() as u128
    }
    pub fn from_key(k: u128) -> Cubie {
        let (c, e) = ((k >> 64) as u64, k as u64);
        let mut s = SOLVED;
        for i in 0..8 {
            let v = ((c >> (5 * i)) & 31) as u8;
            s.cp[i] = v & 7;
            s.ct[i] = v >> 3;
        }
        for i in 0..12 {
            let v = ((e >> (5 * i)) & 31) as u8;
            s.ep[i] = v & 15;
            s.ef[i] = v >> 4;
        }
        s
    }
    pub fn corners_solved(&self) -> bool {
        self.cp == SOLVED.cp && self.ct == [0; 8]
    }
    pub fn edges_solved(&self) -> bool {
        self.ep == SOLVED.ep && self.ef == [0; 12]
    }
    pub fn to_text(&self) -> String {
        let j = |v: &[u8]| v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(",");
        format!("{};{};{};{}", j(&self.cp), j(&self.ct), j(&self.ep), j(&self.ef))
    }
}

#[inline]
pub fn hash128(k: u128) -> u64 {
    let (a, b) = ((k >> 64) as u64, k as u64);
    let mut x = (a ^ b.rotate_left(29)).wrapping_mul(0x9E3779B97F4A7C15);
    x ^= x >> 32;
    x = (x ^ b).wrapping_mul(0xBF58476D1CE4E5B9);
    x ^ (x >> 29)
}

/// Check the model against the vectors written by export_tables.py.
pub fn selftest(m: &Model) {
    use crate::seq;
    let mut n = 0;
    for line in &m.tests {
        let parts: Vec<Vec<u8>> = line.split('|').map(|p| p.split_whitespace().map(|x| x.parse().unwrap()).collect()).collect();
        let s = m.state(&parts[0]);
        let as_vec = |c: &Cubie| -> Vec<u8> { c.cp.iter().chain(&c.ct).chain(&c.ep).chain(&c.ef).copied().collect() };
        assert_eq!(as_vec(&s), parts[1], "state");
        let r = parts[2][0] as usize;
        assert_eq!(as_vec(&m.conj(&s, r)), parts[3], "rotation");
        assert_eq!(as_vec(&s.inverse()), parts[4], "inverse");
        assert_eq!(s.then(&s.inverse()), SOLVED);
        assert_eq!(Cubie::from_key(s.key()), s);
        let cut = parts[0].len() / 2;
        let (a, b) = parts[0].split_at(cut);
        assert_eq!(m.state(a).then(&m.state(b)), s, "then");
        assert_eq!(m.state(&seq::invert(&parts[0])), s.inverse(), "inverse sequence");
        // a sequence relabelled by a rotation gives the rotated state; so does the mirrored sequence for mirrors
        for r in 0..24 {
            assert_eq!(m.state(&seq::relabel(m, &parts[0], r, false)), m.conj(&s, r), "relabel");
        }
        for mv in 0..18 {
            assert_eq!(m.conj_move(&s, mv), m.state(&[mv as u8]).then(&s).then(&m.state(&[mv as u8]).inverse()));
        }
        n += 1;
    }
    println!("cubie model: {n} test vectors from cube.py ok (states, rotations, inverses, composition, relabelling)");
    let mut k = 0;
    let mut rng = seq::Rng(5);
    for line in &m.cancel_tests {
        let parts: Vec<Vec<u8>> = line.split('|').map(|p| p.split_whitespace().map(|x| x.parse().unwrap()).collect()).collect();
        let c = seq::cancel(&parts[0]);
        assert_eq!(c, parts[1], "cancel");
        assert!(seq::is_reduced(&c));
        // the incremental stack gives the same word, and so does inserting in the middle
        let mut st = Vec::new();
        for &mv in &parts[0] {
            seq::push(&mut st, mv);
        }
        assert_eq!(st, c, "stack");
        if c.len() >= 2 {
            let i = rng.below(c.len() + 1);
            let a = seq::cancel(&parts[0][..parts[0].len().min(9)]);
            let whole: Vec<u8> = c[..i].iter().chain(&a).chain(&c[i..]).copied().collect();
            let want = seq::cancel(&whole);
            let mut buf = Vec::new();
            let ev = seq::insert(&mut buf, &c[..i], &a, &c[i..], true);
            assert_eq!(buf, want, "insert");
            assert_eq!(ev.len as usize, want.len());
            assert_eq!(&buf[..ev.low as usize], &c[..ev.low as usize]);
            let tail = c.len() - (i + ev.b as usize);
            assert_eq!(&buf[buf.len() - tail..], &c[c.len() - tail..]);
        }
        k += 1;
    }
    println!("cancel: {k} test vectors from cube.py ok (cancel, incremental stack, insertion)");
}
