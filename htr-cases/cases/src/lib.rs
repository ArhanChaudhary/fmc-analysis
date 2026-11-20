//! Every HTR case of a DR, up to symmetry and the E slice: which pieces are bad, how far it is from HTR, and its HTRs,
//! the ones that break DR on the way included.
//!
//! A DR on U/D goes to HTR with the DR moves U, D, R2, L2, F2, B2, or with any face turns, leaving DR on the way.  What
//! decides the HTRs of a DR state is its coset of the half-turn group H = `<U2, D2, R2, L2, F2, B2>` ([`cosets`]):
//! 29,400 of them.  Taking rotations and mirrors that keep the U/D axis as the same case, and also the E slice (2c3 2e
//! and 6c3 6e: the same pieces are bad in the frame with few bad pieces), leaves 1,272 cases ([`classes`]).  A case's
//! optimal counts every face turn ([`allmoves`]): for 155 cases a DR-breaking HTR is shorter than any with DR moves.
//! With DR moves only, turning the E slice keeps the number of moves to HTR (but for HTR itself, which a turned E slice
//! puts 2 moves away); with every face turn, it changes it by one for 25 more cases.  Several cases have the same bad
//! pieces; [`labels`] has the properties solvers tell such cases apart by, and every case has a corner test.  [`find`]
//! reads a solver's own DR.
//!
//! Reading order: `cosets.rs`, `classes.rs`, `labels.rs`, `allmoves.rs`, `find.rs`, then [`Index`].

pub mod allmoves;
pub mod classes;
pub mod cosets;
pub mod find;
pub mod labels;

use allmoves::AllMoves;
use attempt_sim::cube::{format_moves, parse_moves, Move, MoveTables};
use attempt_sim::dr::{DrTables, MOVE_NAMES};
use attempt_sim::htr::{Htr, SUBSET_NAMES};
use classes::Class;
use cosets::{Cosets, NCOSETS};
use labels::Labels;
use serde::Serialize;
use std::sync::OnceLock;

/// The fewest face turns from each DR coset to HTR, DR-breaking HTRs included ([`AllMoves::dr_distances`]; `htr-cases
/// all-dist FILE` writes it, and the checks compute it again and compare).
const ALL_DIST: &[u8] = include_bytes!("all_dist.bin");
/// How far from HTR the search knows the moves left exactly ([`AllMoves::radius`]).
pub const RADIUS: usize = 5;

/// The page lists a case's HTRs up to a number of moves over its optimal that a slider sets: 0 to [`MOST_ABOVE`],
/// this by default ...
pub const DEFAULT_ABOVE: usize = 2;
pub const MOST_ABOVE: usize = 4;
/// ... but never past this many moves (a case whose optimal is longer lists its optimal ones).  With DR-breaking HTRs a
/// 7-optimal case has about 100,000 of 11 moves before the dedupe, a second's search; some cases take ten at 12.
pub const LONGEST: usize = 11;

pub const CORNER_PLACES: [&str; 8] = ["UFR", "UFL", "UBL", "UBR", "DFR", "DFL", "DBL", "DBR"];
pub const EDGE_PLACES: [&str; 8] = ["UF", "UL", "UB", "UR", "DF", "DL", "DB", "DR"];
pub const AXIS_NAMES: [&str; 3] = ["R/L", "U/D", "F/B"];

pub struct Index {
    htr: Htr,
    cube: MoveTables,
    pub cosets: Cosets,
    pub labels: Labels,
    pub cases: Vec<Class>,
    /// the case (index into `cases`) of each coset
    case_of: Vec<u16>,
    /// the cases each case meets after its first quarter turn ([`classes::u2_mates`])
    u2_mates: Vec<Vec<usize>>,
    /// the fewest face turns from each coset to HTR, DR-breaking HTRs included
    pub dist: Vec<u8>,
    /// the search with every face turn, built when first needed
    all: OnceLock<AllMoves>,
}

/// A case as the page and the text file show it.  Everything is for the coset drawn, except `turned`.
#[derive(Serialize, Debug)]
pub struct CaseInfo {
    /// 1, 2, ... in the order of the index
    pub number: usize,
    pub subset: &'static str,
    /// bad edges in the frame with few bad pieces
    pub edges: u8,
    /// the optimal: fewest face turns to HTR, DR-breaking HTRs included
    pub moves: u8,
    /// with DR moves only
    pub dr_moves: u8,
    /// 4b2 parity, 2c3 direction, 2c4 or 4a3 good or bad
    pub label: Option<&'static str>,
    /// the highlighted pieces: the bad ones, relative to the centres
    pub bad_corners: Vec<&'static str>,
    pub bad_edges: Vec<&'static str>,
    /// numbers of the cases whose bad pieces look the same
    pub lookalikes: Vec<usize>,
    /// numbers of the cases a U2 away that it meets after its first quarter turn ([`classes::u2_mates`])
    pub u2_mates: Vec<usize>,
    /// a shortest sequence of DR moves that puts the corners alone in HTR (it leaves the lookalikes' corners in fake
    /// HTR)
    pub corner_test: String,
    /// the same case with the E slice turned: every other piece bad
    pub turned: Turned,
}

#[derive(Serialize, Debug)]
pub struct Turned {
    pub corners: u32,
    pub edges: u32,
    pub moves: u8,
    pub label: Option<&'static str>,
}

/// A solver's own DR, read by [`Index::find`].  Moves and pieces are in the solver's own frame.
#[derive(Serialize, Debug)]
pub struct FoundInfo {
    pub axis: &'static str,
    /// the case's number in the index
    pub number: usize,
    /// is it the case with the E slice turned (the slice between the DR faces): its bad pieces the index's good ones?
    pub turned: bool,
    pub subset: &'static str,
    pub edges: u8,
    pub moves: u8,
    pub label: Option<&'static str>,
    /// the pieces to highlight: the bad ones if there are few, else the good ones
    pub corners: Vec<String>,
    pub edge_pieces: Vec<String>,
    pub highlighted_are_bad: bool,
    /// bad pieces, relative to the centres
    pub bad: (u32, u32),
    pub corner_test: String,
    /// how long the HTRs listed go ([`Index::longest`])
    pub longest: usize,
    pub solutions: Vec<String>,
}

pub fn dr_text(moves: &[u8]) -> String {
    moves.iter().map(|&m| MOVE_NAMES[m as usize]).collect::<Vec<_>>().join(" ")
}

/// The inverse of a sequence, with turns of opposite faces put back in the order U D, R L, F B.
fn inverse(moves: &[Move]) -> Vec<Move> {
    let mut out: Vec<Move> = moves.iter().rev().map(|m| m.inverse()).collect();
    for i in 1..out.len() {
        let (f, g) = (out[i - 1].face(), out[i].face());
        if f / 2 == g / 2 && g < f {
            out.swap(i - 1, i);
        }
    }
    out
}

impl Index {
    pub fn new() -> Index {
        let dr = DrTables::new();
        let htr = Htr::new(&dr);
        let cosets = Cosets::new(&dr, &htr);
        let labels = Labels::new(&cosets);
        let dist = ALL_DIST.to_vec();
        assert_eq!(dist.len(), NCOSETS);
        let cases = classes::classes(&cosets, &dist);
        let mut case_of = vec![0u16; NCOSETS];
        for (i, c) in cases.iter().enumerate() {
            for &x in &c.members {
                case_of[x] = i as u16;
            }
        }
        let u2_mates = classes::u2_mates(&cosets, &cases, &dist);
        Index { htr, cube: MoveTables::new(), cosets, labels, cases, case_of, u2_mates, dist, all: OnceLock::new() }
    }

    /// The search with every face turn (its tables take a moment: built the first time they are needed).
    pub fn allmoves(&self) -> &AllMoves {
        self.all.get_or_init(|| AllMoves::new(&self.htr, RADIUS).with_dr_distances(self.dist.clone()))
    }

    /// The fewest face turns from every coset to HTR, computed again (what `all_dist.bin` keeps; about 15 seconds).
    pub fn fresh_distances(&self) -> Vec<u8> {
        AllMoves::new(&self.htr, 6).dr_distances(&self.htr, &self.cosets.dist)
    }

    /// A cube in a coset (see [`AllMoves::dr_cube`]).
    pub fn cube_of(&self, coset: usize) -> attempt_sim::cube::Cube {
        AllMoves::dr_cube(&self.htr, coset)
    }

    pub fn case_of(&self, coset: usize) -> usize {
        self.case_of[coset] as usize
    }

    /// How long the page lists a coset's HTRs with the slider at `above`: up to that many moves over its optimal
    /// (at most [`MOST_ABOVE`]), but not past [`LONGEST`] unless the optimal is.  (HTR with the E slice turned, case
    /// 1: only its optimal, the E slice itself; see [`Index::all_solutions`].)
    pub fn longest(&self, coset: usize, above: usize) -> usize {
        let dist = self.dist[coset] as usize;
        if coset == self.cosets.turned_solved {
            return dist;
        }
        dist.max((dist + above.min(MOST_ABOVE)).min(LONGEST))
    }

    /// Every HTR of a coset in the listed form ([`AllMoves::solutions`]): those of up to `longest` face turns, or if
    /// there are none, the shortest ones.
    /// (HTR with the E slice turned, case 1, is HTR up to the E slice: only its shortest, the E slice itself.)
    pub fn all_solutions(&self, coset: usize, longest: usize) -> Vec<Vec<Move>> {
        if coset == self.cosets.solved {
            return Vec::new();
        }
        if coset == self.cosets.turned_solved {
            return vec![vec![Move::new(0, 1), Move::new(1, 1)]];
        }
        let longest = longest.max(self.dist[coset] as usize);
        self.allmoves().solutions(&self.cube_of(coset), longest)
    }

    /// The listed HTRs: [`Index::all_solutions`] with one of each set that is the same up to the E slice
    /// ([`allmoves::modulo_e`]), the shortest (then the first in move order), shortest first.
    pub fn solutions(&self, coset: usize, longest: usize) -> Vec<Vec<Move>> {
        let all = self.all_solutions(coset, longest);
        let mut seen = std::collections::HashSet::new();
        let mut by_length: Vec<&Vec<Move>> = all.iter().collect();
        by_length.sort_by_key(|s| s.len()); // stable: move order within a length
        by_length.into_iter().filter(|s| seen.insert(allmoves::modulo_e(s))).cloned().collect()
    }

    pub fn solution_texts(&self, coset: usize, longest: usize) -> Vec<String> {
        self.solutions(coset, longest).iter().map(|s| format_moves(s)).collect()
    }

    /// The HTRs with DR moves only ([`Cosets::solutions`]), as DR moves, to `longest` or the DR-move shortest.
    pub fn dr_solutions(&self, coset: usize, longest: usize) -> Vec<Vec<u8>> {
        let dist = self.cosets.dist[coset] as usize;
        let longest = if coset == self.cosets.turned_solved { dist } else { longest.max(dist) };
        self.cosets.solutions(coset, longest)
    }

    /// A shortest sequence that makes the coset from a solved cube: the inverse of its first shortest HTR (DR-breaking
    /// for some cases).
    pub fn generator(&self, coset: usize) -> Vec<Move> {
        match self.all_solutions(coset, self.dist[coset] as usize).first() {
            Some(shortest) => inverse(shortest),
            None => Vec::new(),
        }
    }

    pub fn generator_text(&self, coset: usize) -> String {
        format_moves(&self.generator(coset))
    }

    pub fn info(&self, i: usize) -> CaseInfo {
        let c = &self.cases[i];
        let x = c.coset;
        let t = self.cosets.eslice[x] as usize;
        let (corners, edges) = self.cosets.bad(x);
        CaseInfo {
            number: i + 1,
            subset: SUBSET_NAMES[c.subset as usize],
            edges: c.edges,
            moves: c.moves,
            dr_moves: self.cosets.dist[x],
            label: self.labels.of(x),
            bad_corners: (0..8)
                .filter(|&p| self.cosets.corner_mask[x] >> p & 1 == 1)
                .map(|p| CORNER_PLACES[p])
                .collect(),
            bad_edges: (0..8).filter(|&p| self.cosets.edge_mask[x] >> p & 1 == 1).map(|p| EDGE_PLACES[p]).collect(),
            lookalikes: c.lookalikes.iter().map(|&j| j + 1).collect(),
            u2_mates: self.u2_mates[i].iter().map(|&j| j + 1).collect(),
            corner_test: dr_text(&self.cosets.corner_solution(x)),
            turned: Turned { corners: 8 - corners, edges: 8 - edges, moves: self.dist[t], label: self.labels.of(t) },
        }
    }

    /// The coset a case is drawn with, or with the E slice turned.
    pub fn coset(&self, i: usize, turned: bool) -> usize {
        let x = self.cases[i].coset;
        if turned {
            self.cosets.eslice[x] as usize
        } else {
            x
        }
    }

    /// Read a solver's DR from one text: a scramble and the moves to DR after it, or a setup
    /// ([`find::split_attempt`]).
    pub fn find_attempt(&self, text: &str, above: usize) -> Result<FoundInfo, String> {
        let (scramble, moves) = find::split_attempt(text);
        if scramble.is_empty() {
            return Err("enter a scramble and your moves to DR, or a setup".into());
        }
        self.find(&scramble, &moves, above)
    }

    /// Read a solver's DR from a scramble and the moves so far (NISS moves in brackets), with its HTRs of up to
    /// `above` moves over its optimal ([`Index::longest`]).
    pub fn find(&self, scramble: &str, solution: &str, above: usize) -> Result<FoundInfo, String> {
        let scramble: Vec<Move> = parse_moves(scramble.split("//").next().unwrap_or(""))?;
        let (normal, inverse) = find::parse_solution(solution)?;
        let found = find::find(&self.htr, &self.cube, &find::state_moves(&scramble, &normal, &inverse))?;
        let x = found.coset;
        if x == self.cosets.solved {
            return Err("that is already HTR".into());
        }
        let i = self.case_of(x);
        let c = &self.cases[i];
        let turned = !(0..attempt_sim::dr::NSYM).any(|s| self.cosets.sym[c.coset][s] as usize == x);
        let few = self.cosets.few_frame(x);
        let flip = if few { 0 } else { 0xFF };
        let names = |mask: u8, places: &[&str; 8]| -> Vec<String> {
            (0..8).filter(|&p| (mask ^ flip) >> p & 1 == 1).map(|p| found.place_name(places[p])).collect()
        };
        let in_frame = |moves: &[u8]| format_moves(&moves.iter().map(|&m| found.turn(m)).collect::<Vec<_>>());
        let in_frame_all =
            |moves: &[Move]| format_moves(&moves.iter().map(|&m| found.turn_move(m)).collect::<Vec<_>>());
        Ok(FoundInfo {
            axis: AXIS_NAMES[found.axis],
            number: i + 1,
            turned,
            subset: SUBSET_NAMES[c.subset as usize],
            edges: c.edges,
            moves: self.dist[x],
            label: self.labels.of(x),
            corners: names(self.cosets.corner_mask[x], &CORNER_PLACES),
            edge_pieces: names(self.cosets.edge_mask[x], &EDGE_PLACES),
            highlighted_are_bad: few,
            bad: self.cosets.bad(x),
            corner_test: in_frame(&self.cosets.corner_solution(x)),
            longest: self.longest(x, above),
            solutions: self.solutions(x, self.longest(x, above)).iter().map(|s| in_frame_all(s)).collect(),
        })
    }
}

impl Default for Index {
    fn default() -> Self {
        Self::new()
    }
}
