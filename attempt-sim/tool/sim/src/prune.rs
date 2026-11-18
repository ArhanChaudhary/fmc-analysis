//! Optimal DR finishes without the 1.3 GB exact table.
//!
//! The research simulator looked the optimal finish of every DR state up in *Judging a DR*'s exact table.  That is
//! too big for a web page, so here the optimum is searched (IDA*) with a smaller exact table as the bound: the
//! distance of the corners and the U/D-layer edges alone, E slice ignored ("noE").  That table has one entry per
//! corner symmetry class (2,768 under the 16 symmetries that keep U/D) and edge permutation, 111.6 million entries at
//! four bits each (56 MB); it is built breadth first in a few seconds.  On random DR states it is about a third of a
//! move below the optimum on average, so the searches stay small.
//!
//! The bound only prunes branches that cannot reach solved within the budget, so the searches find exactly the
//! finishes, in exactly the order, that the exact table gave.

use crate::dr::{DrCanon, DrState, DrTables, NC, NE, NMOVES, NSYM, SOLVED};

/// Distances up to 13 are exact; 14 stands for "14 or more" (a lower bound is all the search needs, and the last
/// layer would take a third of the building time).
const MAX_EXACT: u8 = 13;
/// Marks an entry not reached yet while the table is built.
const UNSET: u8 = 15;
/// Layers are kept as lists of entries while they are smaller than this; bigger ones are found by scanning the table.
const LIST_LIMIT: usize = 4_000_000;

/// What a finish search hands each finish: its DR moves and the corner and edge coordinates after each prefix.
pub type FinishVisitor<'a> = dyn FnMut(&[u8], &[(usize, usize)]) + 'a;

/// The 16-symmetry classes of corner permutations.
pub struct CornerClasses {
    /// corner coordinate -> class
    pub class: Vec<u16>,
    /// corner coordinate -> a symmetry that takes it to its class representative
    pub to_rep: Vec<u8>,
    /// class -> representative (the smallest coordinate of the class)
    pub rep: Vec<usize>,
    /// class -> the symmetries other than the identity that fix the representative
    pub stabiliser: Vec<Vec<u8>>,
}

impl CornerClasses {
    pub fn new(dr: &DrTables) -> CornerClasses {
        let mut class = vec![u16::MAX; NC];
        let mut to_rep = vec![0u8; NC];
        let mut rep = Vec::new();
        for c in 0..NC {
            if class[c] != u16::MAX {
                continue; // scanning upward, c is the smallest of its class
            }
            let k = rep.len() as u16;
            rep.push(c);
            for sym in 0..NSYM {
                let d = dr.csym[sym][c] as usize;
                if class[d] == u16::MAX {
                    class[d] = k;
                    to_rep[d] = dr.sym_inv[sym] as u8;
                }
            }
        }
        let stabiliser = rep
            .iter()
            .map(|&c| (1..NSYM as u8).filter(|&s| dr.csym[s as usize][c] as usize == c).collect())
            .collect();
        CornerClasses { class, to_rep, rep, stabiliser }
    }
}

/// The corner + U/D-edge distance table, four bits per entry.
pub struct NoETable {
    classes: CornerClasses,
    nibbles: Vec<u8>,
}

impl NoETable {
    pub fn len_entries(&self) -> usize {
        self.classes.rep.len() * NE
    }

    #[inline]
    fn index(&self, dr: &DrTables, c: usize, e: usize) -> usize {
        let k = self.classes.class[c] as usize;
        let sym = self.classes.to_rep[c] as usize;
        k * NE + dr.esym[sym][e] as usize
    }

    #[inline]
    fn get(&self, i: usize) -> u8 {
        (self.nibbles[i >> 1] >> ((i & 1) * 4)) & 0xF
    }

    /// A lower bound for the optimal finish of a DR state.
    #[inline]
    pub fn bound(&self, dr: &DrTables, st: DrState) -> u8 {
        self.get(self.index(dr, st.0, st.1))
    }

    /// The table as bytes (to keep it between visits) and back.
    pub fn as_bytes(&self) -> &[u8] {
        &self.nibbles
    }
    pub fn from_bytes(dr: &DrTables, bytes: Vec<u8>) -> Result<NoETable, String> {
        let classes = CornerClasses::new(dr);
        let want = (classes.rep.len() * NE).div_ceil(2);
        if bytes.len() != want {
            return Err(format!("table has {} bytes, expected {}", bytes.len(), want));
        }
        let t = NoETable { classes, nibbles: bytes };
        if t.checksum() != NOE_CHECKSUM {
            return Err("table checksum does not match".into());
        }
        Ok(t)
    }

    /// FNV-1a over the bytes, to recognise a damaged copy.
    pub fn checksum(&self) -> u64 {
        self.nibbles.iter().fold(0xcbf2_9ce4_8422_2325u64, |h, &b| (h ^ b as u64).wrapping_mul(0x100_0000_01b3))
    }

    /// The optimal finish (in DR moves) of a state: IDA* with the table as the bound.
    pub fn optimal(&self, dr: &DrTables, st: DrState) -> u8 {
        let mut bound = self.bound(dr, st) as usize;
        loop {
            if self.solvable_within(dr, st, bound, DrCanon::START) {
                return bound as u8;
            }
            bound += 1;
        }
    }

    fn solvable_within(&self, dr: &DrTables, st: DrState, left: usize, canon: DrCanon) -> bool {
        if st == SOLVED {
            return true;
        }
        if left == 0 {
            return false;
        }
        (0..NMOVES).any(|m| {
            if !canon.allows(m) {
                return false;
            }
            let next = dr.apply(m, st);
            (self.bound(dr, next) as usize) < left && self.solvable_within(dr, next, left - 1, canon.after(m))
        })
    }

    /// Every canonical finish of `st` of at most `budget` moves, in the order of a depth-first search over the moves
    /// U U2 U' D D2 D' R2 L2 F2 B2: `found(moves, corner and edge coordinates after each prefix)`.  Stops after `cap`
    /// finishes and returns false in that case.
    pub fn for_each_finish(
        &self,
        dr: &DrTables,
        st: DrState,
        budget: usize,
        cap: u64,
        found: &mut FinishVisitor,
    ) -> bool {
        let mut search = FinishSearch {
            table: self,
            dr,
            budget,
            cap,
            count: 0,
            moves: Vec::with_capacity(24),
            path: vec![(st.0, st.1)],
            found,
        };
        search.go(st, DrCanon::START);
        search.count <= cap
    }
}

struct FinishSearch<'a, 'f> {
    table: &'a NoETable,
    dr: &'a DrTables,
    budget: usize,
    cap: u64,
    count: u64,
    moves: Vec<u8>,
    path: Vec<(usize, usize)>,
    found: &'f mut FinishVisitor<'f>,
}

impl FinishSearch<'_, '_> {
    fn go(&mut self, st: DrState, canon: DrCanon) {
        if self.count > self.cap {
            return;
        }
        if st == SOLVED {
            self.count += 1;
            if self.count <= self.cap {
                (self.found)(&self.moves, &self.path);
            }
            return;
        }
        let left = self.budget - self.moves.len();
        if left == 0 {
            return;
        }
        for m in 0..NMOVES {
            if !canon.allows(m) {
                continue;
            }
            let next = self.dr.apply(m, st);
            if self.table.bound(self.dr, next) as usize + 1 > left {
                continue;
            }
            self.moves.push(m as u8);
            self.path.push((next.0, next.1));
            self.go(next, canon.after(m));
            self.moves.pop();
            self.path.pop();
        }
    }
}

/// Builds the table breadth first, a slice at a time, so that a page can show progress.
///
/// Layer d+1 is found from layer d: while the layers are small, from a list of the entries of layer d; after that by
/// scanning the whole table for them, a range of corner classes per call of [`NoETableBuilder::step`].
pub struct NoETableBuilder {
    classes: CornerClasses,
    nibbles: Vec<u8>,
    /// entries at `depth` are known; `depth + 1` is being found
    depth: u8,
    /// the entries at `depth`, while there are few of them
    layer: Option<Vec<u32>>,
    next_layer: Vec<u32>,
    /// next corner class to scan at this depth
    next_class: usize,
    found_this_pass: usize,
    done: bool,
}

/// Rough share of the building time of each layer (finding depth d + 1 from depth d), measured natively.
const PASS_WEIGHT: [f64; 13] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002, 0.008, 0.03, 0.11, 0.28, 0.57];

impl NoETableBuilder {
    pub fn new(_dr: &DrTables) -> NoETableBuilder {
        let classes = CornerClasses::new(_dr);
        let n = classes.rep.len() * NE;
        let mut b = NoETableBuilder {
            nibbles: vec![0xFF; n.div_ceil(2)],
            classes,
            depth: 0,
            layer: Some(vec![0]),
            next_layer: Vec::new(),
            next_class: 0,
            found_this_pass: 0,
            done: false,
        };
        // the solved state (e = 0 is fixed by every symmetry of the solved corners)
        b.set(0, 0);
        b
    }

    #[inline]
    fn get(&self, i: usize) -> u8 {
        (self.nibbles[i >> 1] >> ((i & 1) * 4)) & 0xF
    }
    #[inline]
    fn set(&mut self, i: usize, v: u8) {
        let shift = (i & 1) * 4;
        let b = &mut self.nibbles[i >> 1];
        *b = (*b & !(0xF << shift)) | (v << shift);
    }

    /// Rough share of the work done.
    pub fn progress(&self) -> f64 {
        if self.done {
            return 1.0;
        }
        let total: f64 = PASS_WEIGHT.iter().sum();
        let done: f64 = PASS_WEIGHT[..self.depth as usize].iter().sum();
        let part = self.next_class as f64 / self.classes.rep.len() as f64;
        ((done + PASS_WEIGHT[self.depth as usize] * part) / total).min(0.999)
    }

    pub fn is_done(&self) -> bool {
        self.done
    }

    /// Mark the neighbours of entry `base + e` (corner class k) that are not reached yet as one move further.
    #[inline]
    fn expand(&mut self, dr: &DrTables, k: usize, e: usize, d: u8, keep: bool) {
        let rep = self.classes.rep[k];
        for m in 0..NMOVES {
            let c2 = dr.cmove[m][rep] as usize;
            let (k2, sym) = (self.classes.class[c2] as usize, self.classes.to_rep[c2] as usize);
            let e2 = dr.esym[sym][dr.emove[m][e] as usize] as usize;
            let i2 = k2 * NE + e2;
            if self.get(i2) != UNSET {
                continue;
            }
            self.set(i2, d + 1);
            self.found_this_pass += 1;
            if keep {
                self.next_layer.push(i2 as u32);
            }
            // the symmetric copies of the same state under the representative's stabiliser
            for si in 0..self.classes.stabiliser[k2].len() {
                let t = self.classes.stabiliser[k2][si] as usize;
                let i3 = k2 * NE + dr.esym[t][e2] as usize;
                if self.get(i3) == UNSET {
                    self.set(i3, d + 1);
                    self.found_this_pass += 1;
                    if keep {
                        self.next_layer.push(i3 as u32);
                    }
                }
            }
        }
    }

    /// Work for a while (a whole small layer, or up to `max_classes` corner classes of a big one); returns true when
    /// the table is complete.
    pub fn step(&mut self, dr: &DrTables, max_classes: usize) -> bool {
        if self.done {
            return true;
        }
        let d = self.depth;
        let nclass = self.classes.rep.len();
        if let Some(layer) = self.layer.take() {
            let keep = layer.len() * 4 < LIST_LIMIT;
            for &i in &layer {
                let i = i as usize;
                self.expand(dr, i / NE, i % NE, d, keep);
            }
            self.next_class = nclass;
            if keep {
                self.layer = Some(std::mem::take(&mut self.next_layer));
            }
        } else {
            let end = (self.next_class + max_classes).min(nclass);
            for k in self.next_class..end {
                let base = k * NE;
                for e in 0..NE {
                    if self.get(base + e) == d {
                        self.expand(dr, k, e, d, false);
                    }
                }
            }
            self.next_class = end;
        }
        if self.next_class < nclass {
            return false;
        }
        // the layer is complete
        #[cfg(feature = "profile")]
        eprintln!("depth {} found {}", d + 1, self.found_this_pass);
        let found = self.found_this_pass;
        self.found_this_pass = 0;
        self.next_class = 0;
        self.depth += 1;
        if found == 0 || self.depth >= MAX_EXACT {
            // whatever is not reached yet is MAX_EXACT + 1 or more
            for b in self.nibbles.iter_mut() {
                if *b & 0x0F == UNSET {
                    *b = (*b & 0xF0) | (MAX_EXACT + 1);
                }
                if *b >> 4 == UNSET {
                    *b = (*b & 0x0F) | ((MAX_EXACT + 1) << 4);
                }
            }
            self.done = true;
        }
        self.done
    }

    pub fn finish(self) -> NoETable {
        assert!(self.done, "the table is not complete");
        NoETable { classes: self.classes, nibbles: self.nibbles }
    }

    /// Build the whole table at once.
    pub fn build(dr: &DrTables) -> NoETable {
        let mut b = NoETableBuilder::new(dr);
        while !b.step(dr, usize::MAX) {}
        b.finish()
    }
}

/// Checksum of the complete table (the `table` command of the command-line program prints it).
pub const NOE_CHECKSUM: u64 = 0xb739_24ac_dc5f_da92;
