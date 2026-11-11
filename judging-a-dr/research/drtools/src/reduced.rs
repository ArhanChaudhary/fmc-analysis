//! The symmetry-reduced index of DR states and the exact-distance data that `drtools bfs` leaves on disk.
//!
//! Reduced index of a state: `(class, e, s12)` with
//!
//! * `class` = symmetry class of the corner permutation under the 16 symmetries (2768 classes; the
//!   representative is the smallest coordinate of the class),
//! * `e` = U/D-edge coordinate (0..40320),
//! * `s12` = rank of the E-slice permutation among the 12 that have the parity forced by corners and edges.
//!
//! Bit number `class * ROW + e * 12 + s12` of the file `depth_XX.bits` is set iff that reduced state has
//! optimal length XX.  A state whose corner permutation is not a class representative is first conjugated
//! by the symmetry that brings its corners to the representative.  If a representative has a non-trivial
//! stabiliser, every `(e, s)` image under the stabiliser is marked, so that
//! "number of states at depth d" = sum over set bits of 16/|stabiliser|.
//!
//! Files in a BFS directory:
//!
//! * `depth_00.bits` … `depth_18.bits`: bitsets as arrays of little-endian 64-bit words (bit i of the file
//!   is bit `i % 8` of byte `i / 8`), `nclass * ROWB` bytes each
//! * `classes.bin`: `nclass` (i32), the representative corner coordinate of each class (i32 each), the
//!   stabiliser size of each class (one byte each); all little-endian
//! * `counts.txt`: one line `depth states reduced_states` per depth and a final `total` line

use crate::core::{Core, NC, NE, NS, NSYM};
use std::fs::File;
use std::io::Read;
use std::os::unix::fs::FileExt;
use std::path::Path;

/// Bits per corner class: 40320 U/D-edge permutations x 12 E-slice permutations.
pub const ROW: usize = NE * 12;
/// Bytes per corner class in a depth file.
pub const ROWB: usize = ROW / 8;
/// Number of depths (0..=18).
pub const MAXD: usize = 19;

// A class row starts on a 64-bit word boundary, so rows can be handled as whole words / whole bytes.
const _: () = assert!(ROW % 64 == 0 && ROWB == 60480);

/// The 16-symmetry classes of corner permutations.
pub struct CornerClasses {
    pub nclass: usize,
    /// corner coordinate -> class
    pub cclass: Vec<u16>,
    /// corner coordinate -> a symmetry S with `csym[S][c]` = representative of the class of c
    pub csymto: Vec<u8>,
    /// class -> representative corner coordinate (the smallest of the class)
    pub crep: Vec<usize>,
}

impl CornerClasses {
    pub fn new(core: &Core) -> CornerClasses {
        let mut cclass = vec![0xFFFFu16; NC];
        let mut csymto = vec![0u8; NC];
        let mut crep = Vec::new();
        for c in 0..NC {
            if cclass[c] != 0xFFFF {
                continue; // c is the smallest of its orbit because we scan upward
            }
            let k = crep.len() as u16;
            crep.push(c);
            for sym in 0..NSYM {
                let d = core.csym[sym][c] as usize;
                if cclass[d] == 0xFFFF {
                    cclass[d] = k;
                    csymto[d] = core.sym_inv[sym] as u8;
                }
            }
        }
        CornerClasses {
            nclass: crep.len(),
            cclass,
            csymto,
            crep,
        }
    }

    /// For each class the symmetries that fix its representative (the identity, symmetry 0, comes first).
    pub fn stabilisers(&self, core: &Core) -> Vec<Vec<u8>> {
        self.crep
            .iter()
            .map(|&c| {
                (0..NSYM as u8)
                    .filter(|&sym| core.csym[sym as usize][c] as usize == c)
                    .collect()
            })
            .collect()
    }
}

/// Numbering of the E-slice permutations inside their parity class.
pub struct SliceIndex {
    /// E-slice coordinate (0..24) -> rank among the 12 permutations of the same parity
    pub to12: [u8; NS],
    /// `from12[parity][s12]` -> E-slice coordinate
    pub from12: [[u8; 12]; 2],
}

impl SliceIndex {
    pub fn new(core: &Core) -> SliceIndex {
        let mut index = SliceIndex {
            to12: [0; NS],
            from12: [[0; 12]; 2],
        };
        let mut n = [0usize; 2];
        for s in 0..NS {
            let par = core.spar[s] as usize;
            index.to12[s] = n[par] as u8;
            index.from12[par][n[par]] = s as u8;
            n[par] += 1;
        }
        index
    }
}

fn depth_file_name(depth: usize) -> String {
    format!("depth_{:02}.bits", depth)
}

/// Open `depth_00.bits` … `depth_18.bits` of a BFS directory for reading.
pub fn open_depth_files(dir: &Path) -> Vec<File> {
    (0..MAXD)
        .map(|d| {
            let path = dir.join(depth_file_name(d));
            File::open(&path).unwrap_or_else(|_| fatal!("missing {}", path.display()))
        })
        .collect()
}

/// The exact optimal length of every DR state, as left on disk by `drtools bfs` (or the C `drbfs`).
pub struct ExactData {
    pub nclass: usize,
    /// class -> representative corner coordinate
    pub crep: Vec<usize>,
    /// class -> size of the stabiliser of the representative
    pub nstab: Vec<u8>,
    depth_files: Vec<File>,
}

impl ExactData {
    /// Read `classes.bin` and open the depth files.
    pub fn open(dir: &Path) -> ExactData {
        let path = dir.join("classes.bin");
        let mut bytes = Vec::new();
        if File::open(&path)
            .and_then(|mut f| f.read_to_end(&mut bytes))
            .is_err()
            || bytes.len() < 4
        {
            fatal!("no classes.bin in {}", dir.display());
        }
        let nclass = i32::from_le_bytes([bytes[0], bytes[1], bytes[2], bytes[3]]) as usize;
        if bytes.len() < 4 + 5 * nclass {
            fatal!("short classes.bin in {}", dir.display());
        }
        let crep = bytes[4..4 + 4 * nclass]
            .chunks_exact(4)
            .map(|b| i32::from_le_bytes([b[0], b[1], b[2], b[3]]) as usize)
            .collect();
        let nstab = bytes[4 + 4 * nclass..4 + 5 * nclass].to_vec();
        ExactData {
            nclass,
            crep,
            nstab,
            depth_files: open_depth_files(dir),
        }
    }
}

/// Scratch space for the depths of one class row.
pub struct RowDepths {
    buf: Vec<u8>,
    dep: Vec<u8>,
}

impl RowDepths {
    pub fn new() -> RowDepths {
        RowDepths {
            buf: vec![0; ROWB],
            dep: vec![0xFF; ROW],
        }
    }

    /// Read the row of class `k` from every depth file (one positioned read of 60,480 bytes per depth) and
    /// return `dep` with `dep[e * 12 + s12]` = optimal length of that reduced state (0xFF if in no file).
    pub fn load(&mut self, data: &ExactData, k: usize) -> &[u8] {
        self.dep.fill(0xFF);
        for (d, file) in data.depth_files.iter().enumerate() {
            if file
                .read_exact_at(&mut self.buf, (k * ROWB) as u64)
                .is_err()
            {
                fatal!("short read");
            }
            // every set bit of this depth's row gets depth d; 64 bits at a time (most words are zero)
            for (w, word) in self.buf.chunks_exact(8).enumerate() {
                let mut x = u64::from_le_bytes(word.try_into().unwrap());
                while x != 0 {
                    let t = x.trailing_zeros() as usize;
                    x &= x - 1;
                    self.dep[w * 64 + t] = d as u8;
                }
            }
        }
        &self.dep
    }
}

/// Exact optimal length of one state, looked up bit by bit in the depth files (None if the state is in no file).
pub fn exact_depth(depth_files: &[File], bit: usize) -> Option<usize> {
    for (d, file) in depth_files.iter().enumerate() {
        let mut byte = [0u8];
        if file.read_exact_at(&mut byte, (bit >> 3) as u64).is_err() {
            return None;
        }
        if byte[0] >> (bit & 7) & 1 != 0 {
            return Some(d);
        }
    }
    None
}
