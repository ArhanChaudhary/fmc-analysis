//! Every table the simulated solver uses, built once.
//!
//! Most of the search happens in a *view*: the cube turned so that the EO axis is F/B and the DR axis is U/D.  On that
//! orientation:
//!
//! * `eo_dist[pattern]`: fewest turns to EO on F/B from a pattern of bad edges (2,048 patterns, any turn);
//! * `dr_dist[twists * 495 + slice]`: fewest EO-keeping turns (U D R L F2 B2) to DR on U/D, from the corner twists and
//!   the places of the four E-slice edges, EO solved (1,082,565 states);
//! * the DR group with its HTR subsets ([`crate::dr`], [`crate::htr`]) and the bound for optimal finishes
//!   ([`crate::prune`]);
//! * what the solver knows about a subset: the distribution of the optimal finish over all DR states of the subset
//!   (*Which HTR routes to try from a DR*), and the route checklist of each subset.

use crate::cube::{Cube, Move, MoveTables};
use crate::dr::DrTables;
use crate::htr::Htr;
use crate::prune::{NoETable, NoETableBuilder};
use crate::routes::parse_route;

pub const N_TWIST: usize = 2187;
pub const N_FLIP: usize = 2048;
pub const N_SLICE: usize = 495;

/// The 14 turns that keep EO on F/B.
pub const EO_KEEPING: [Move; 14] = [
    Move(0), Move(1), Move(2), Move(3), Move(4), Move(5), Move(6), Move(7), Move(8), Move(9), Move(10), Move(11),
    Move(13), Move(16),
];

/// The optimal finish distribution of every DR state, per subset (from *Which HTR routes to try from a DR*).
const DIST48: &str = include_str!("../data/dist48.tsv");
/// The route checklist of each subset, in order (same study: level C, optimum, HTR budget 2).
const CHECKLIST: &str = include_str!("../data/checklist.tsv");

/// One line of a subset's checklist.
pub struct ChecklistRoute {
    pub route: Vec<u8>,
    pub name: String,
    /// share of the subset's DRs on which this route is the first of the list to find the optimum
    pub marginal: f64,
}

pub struct Tables {
    pub moves: MoveTables,
    pub twist_move: Vec<[u16; 18]>,
    pub flip_move: Vec<[u16; 18]>,
    pub slice_move: Vec<[u16; 18]>,
    pub eo_dist: Vec<u8>,
    pub dr_dist: Vec<u8>,
    /// bad corners of a twist coordinate, edges out of the E slice (x2) of a slice coordinate
    pub drm_corners: Vec<u8>,
    pub drm_edges: Vec<u8>,
    slice_rank: Vec<u16>,
    pub dr: DrTables,
    pub htr: Htr,
    /// the bound for optimal DR finishes, once built (see [`Tables::prune_builder`])
    pub noe: Option<NoETable>,
    /// per subset: share of its DR states with an optimal finish of at most k moves (k = 0..=20), and the mean
    pub subset_cdf: Vec<[f64; 21]>,
    pub subset_mean: Vec<f64>,
    pub all_cdf: [f64; 21],
    pub all_mean: f64,
    pub checklists: Vec<Vec<ChecklistRoute>>,
}

impl Tables {
    /// Everything except the finish bound (fast: well under a second).
    pub fn new() -> Tables {
        let moves = MoveTables::new();
        // rank of every 4-element subset of the 12 edge places, lexicographic
        let mut slice_rank = vec![u16::MAX; 1 << 12];
        let mut masks = Vec::with_capacity(N_SLICE);
        for mask in 0..(1usize << 12) {
            if mask.count_ones() == 4 {
                slice_rank[mask] = masks.len() as u16;
                masks.push(mask);
            }
        }
        let dr = DrTables::new();
        let htr = Htr::new(&dr);
        let mut t = Tables {
            moves,
            twist_move: Vec::new(),
            flip_move: Vec::new(),
            slice_move: Vec::new(),
            eo_dist: Vec::new(),
            dr_dist: Vec::new(),
            drm_corners: Vec::new(),
            drm_edges: Vec::new(),
            slice_rank,
            dr,
            htr,
            noe: None,
            subset_cdf: Vec::new(),
            subset_mean: Vec::new(),
            all_cdf: [0.0; 21],
            all_mean: 0.0,
            checklists: Vec::new(),
        };
        t.build_coordinate_tables(&masks);
        t.build_distances();
        t.load_subset_data();
        t
    }

    /// The finish bound is the one slow table: build it with this, a slice at a time ([`NoETableBuilder::step`]).
    pub fn prune_builder(&self) -> NoETableBuilder {
        NoETableBuilder::new(&self.dr)
    }

    /// Build the finish bound in one go.
    pub fn build_prune(&mut self) {
        self.noe = Some(NoETableBuilder::build(&self.dr));
    }

    pub fn noe(&self) -> &NoETable {
        self.noe.as_ref().expect("the finish table has not been built")
    }

    /// The (twists, flips, E-slice places) coordinates of a state.
    #[inline]
    pub fn coords(&self, c: &Cube) -> (usize, usize, usize) {
        let mask = (0..12).filter(|&i| c.ep[i] >= 8).fold(0usize, |m, i| m | 1 << i);
        (c.twist_coord(), c.flip_pattern(), self.slice_rank[mask] as usize)
    }

    fn build_coordinate_tables(&mut self, masks: &[usize]) {
        let mv = &self.moves;
        self.twist_move = (0..N_TWIST)
            .map(|tw| {
                let mut c = Cube::SOLVED;
                let mut v = tw;
                for i in 0..7 {
                    c.co[i] = (v % 3) as u8;
                    v /= 3;
                }
                c.co[7] = ((3 - c.co[..7].iter().map(|&x| x as usize).sum::<usize>() % 3) % 3) as u8;
                std::array::from_fn(|m| mv.turn(&c, Move(m as u8)).twist_coord() as u16)
            })
            .collect();
        self.flip_move = (0..N_FLIP)
            .map(|fl| {
                let mut c = Cube::SOLVED;
                for i in 0..11 {
                    c.eo[i] = ((fl >> i) & 1) as u8;
                }
                c.eo[11] = c.eo[..11].iter().fold(0, |p, &x| p ^ x);
                std::array::from_fn(|m| mv.turn(&c, Move(m as u8)).flip_pattern() as u16)
            })
            .collect();
        self.slice_move = masks
            .iter()
            .map(|&mask| {
                // E-slice pieces (8..11) at the places of the mask, the others elsewhere
                let mut c = Cube::SOLVED;
                let (mut e_piece, mut other) = (8u8, 0u8);
                for i in 0..12 {
                    if mask >> i & 1 == 1 {
                        c.ep[i] = e_piece;
                        e_piece += 1;
                    } else {
                        c.ep[i] = other;
                        other += 1;
                    }
                }
                std::array::from_fn(|m| self.coords(&mv.turn(&c, Move(m as u8))).2 as u16)
            })
            .collect();
        self.drm_corners = (0..N_TWIST)
            .map(|tw| {
                let mut v = tw;
                let (mut sum, mut bad) = (0, 0u8);
                for _ in 0..7 {
                    bad += (v % 3 != 0) as u8;
                    sum += v % 3;
                    v /= 3;
                }
                bad + (sum % 3 != 0) as u8
            })
            .collect();
        const E_SLICE_PLACES: usize = 0xF00;
        self.drm_edges = masks.iter().map(|&m| 2 * (4 - (m & E_SLICE_PLACES).count_ones() as u8)).collect();
    }

    fn build_distances(&mut self) {
        // EO distance, any turn
        let mut eo_dist = vec![u8::MAX; N_FLIP];
        eo_dist[0] = 0;
        let mut frontier = vec![0usize];
        let mut d = 0;
        while !frontier.is_empty() {
            let mut next = Vec::new();
            for &e in &frontier {
                for m in 0..18 {
                    let f = self.flip_move[e][m] as usize;
                    if eo_dist[f] == u8::MAX {
                        eo_dist[f] = d + 1;
                        next.push(f);
                    }
                }
            }
            frontier = next;
            d += 1;
        }
        self.eo_dist = eo_dist;

        // EO-kept distance to DR
        let solved_slice = self.coords(&Cube::SOLVED).2;
        let mut dr_dist = vec![u8::MAX; N_TWIST * N_SLICE];
        dr_dist[solved_slice] = 0;
        let mut frontier = vec![(0usize, solved_slice)];
        let mut d = 0;
        while !frontier.is_empty() {
            let mut next = Vec::new();
            for &(tw, sl) in &frontier {
                for m in EO_KEEPING {
                    let (tw2, sl2) = (self.twist_move[tw][m.index()] as usize, self.slice_move[sl][m.index()] as usize);
                    if dr_dist[tw2 * N_SLICE + sl2] == u8::MAX {
                        dr_dist[tw2 * N_SLICE + sl2] = d + 1;
                        next.push((tw2, sl2));
                    }
                }
            }
            frontier = next;
            d += 1;
        }
        self.dr_dist = dr_dist;
    }

    fn load_subset_data(&mut self) {
        let nsub = self.htr.sub48_names.len();
        let mut count = vec![[0f64; 21]; nsub];
        for line in DIST48.lines().skip(1) {
            let p: Vec<&str> = line.split('\t').collect();
            let k = self.htr.subset_index(p[0]).expect("dist48.tsv names a known subset");
            count[k][p[1].parse::<usize>().unwrap()] += p[2].parse::<f64>().unwrap();
        }
        let mut all = [0f64; 21];
        self.subset_cdf = vec![[0.0; 21]; nsub];
        self.subset_mean = vec![0.0; nsub];
        for k in 0..nsub {
            let total: f64 = count[k].iter().sum();
            assert!(total > 0.0, "dist48.tsv covers every subset");
            let mut acc = 0.0;
            for d in 0..21 {
                acc += count[k][d];
                self.subset_cdf[k][d] = acc / total;
                self.subset_mean[k] += d as f64 * count[k][d] / total;
                all[d] += count[k][d];
            }
        }
        let total: f64 = all.iter().sum();
        assert_eq!(total, 19_508_428_800.0, "dist48.tsv covers every DR state");
        let mut acc = 0.0;
        for d in 0..21 {
            acc += all[d];
            self.all_cdf[d] = acc / total;
            self.all_mean += d as f64 * all[d] / total;
        }

        self.checklists = (0..nsub).map(|_| Vec::new()).collect();
        for line in CHECKLIST.lines().skip(1) {
            let p: Vec<&str> = line.split('\t').collect();
            let g = self.htr.subset_index(p[0]).expect("checklist.tsv names a known subset");
            self.checklists[g].push(ChecklistRoute {
                route: parse_route(p[2]).expect("checklist.tsv routes parse"),
                name: p[2].to_string(),
                marginal: p[3].parse().unwrap(),
            });
        }
        assert!(self.checklists.iter().all(|l| !l.is_empty()), "every subset has a checklist");
    }

    /// The DRM of an EO-solved view state ("4c4e": bad corners, edges out of the E slice).
    pub fn drm_name(&self, twist: usize, slice: usize) -> String {
        format!("{}c{}e", self.drm_corners[twist], self.drm_edges[slice])
    }
}

impl Default for Tables {
    fn default() -> Self {
        Self::new()
    }
}
