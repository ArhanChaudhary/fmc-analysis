//! Every HTR case of a DR, up to symmetry and the E slice: which pieces are bad, how far it is from HTR, and every
//! HTR of 8 moves or less.
//!
//! A DR on U/D is solved to HTR with the DR moves U, D, R2, L2, F2, B2.  What decides the HTRs of a DR state is its
//! coset of the half-turn group H = `<U2, D2, R2, L2, F2, B2>` ([`cosets`]): 29,400 of them.  Taking rotations and
//! mirrors that keep the U/D axis as the same case, and also the E slice (2c3 2e and 6c3 6e: the same pieces are bad
//! in the frame with few bad pieces), leaves 1,272 cases ([`classes`]).  Turning the E slice keeps the number of
//! moves to HTR, except for HTR itself, which a turned E slice puts 2 moves away.  Several cases have the same bad
//! pieces; [`labels`] has the two properties the guides tell such cases apart by (4b2 parity, 2c3 direction), and every
//! case has a corner test.  [`find`] reads a solver's own DR.
//!
//! Reading order: `cosets.rs`, `classes.rs`, `labels.rs`, `find.rs`, then [`Index`].

pub mod classes;
pub mod cosets;
pub mod find;
pub mod labels;

use attempt_sim::cube::{format_moves, parse_moves, Move, MoveTables};
use attempt_sim::dr::{DrTables, MOVE_FACE, MOVE_NAMES};
use attempt_sim::htr::{Htr, SUBSET_NAMES};
use classes::Class;
use cosets::{Cosets, NCOSETS};
use labels::Labels;
use serde::Serialize;

/// HTRs are listed up to a length the page sets (this by default), but never more than [`ABOVE_SHORTEST`] moves over
/// the case's shortest; for a case with none that short, at the shortest length.
pub const MAX_LEN: usize = 8;
/// How many moves over the shortest HTR the listed ones go at most (past it, a short case has millions).
pub const ABOVE_SHORTEST: usize = 4;

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
}

/// A case as the page and the text file show it.  Everything is for the coset drawn, except `turned`.
#[derive(Serialize, Debug)]
pub struct CaseInfo {
    /// 1, 2, ... in the order of the index
    pub number: usize,
    pub subset: &'static str,
    /// bad edges in the frame with few bad pieces
    pub edges: u8,
    /// fewest moves to HTR
    pub moves: u8,
    /// 4b2 parity or 2c3 direction
    pub label: Option<&'static str>,
    /// the highlighted pieces: the bad ones, relative to the centres
    pub bad_corners: Vec<&'static str>,
    pub bad_edges: Vec<&'static str>,
    /// numbers of the cases whose bad pieces look the same
    pub lookalikes: Vec<usize>,
    /// numbers of the cases a U2 away that it meets after its first quarter turn ([`classes::u2_mates`])
    pub u2_mates: Vec<usize>,
    /// a shortest sequence that puts the corners alone in HTR (it leaves the lookalikes' corners in fake HTR)
    pub corner_test: String,
    /// a shortest sequence that makes the case from a solved cube
    pub generator: String,
    /// how many HTRs are listed by default (see [`Index::longest`] with MAX_LEN)
    pub solutions: usize,
    /// the same case with the E slice turned: every other piece bad
    pub turned: Turned,
}

#[derive(Serialize, Debug)]
pub struct Turned {
    pub corners: u32,
    pub edges: u32,
    pub moves: u8,
    pub label: Option<&'static str>,
    pub corner_test: String,
    pub generator: String,
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
    pub solutions: Vec<String>,
}

fn dr_text(moves: &[u8]) -> String {
    moves.iter().map(|&m| MOVE_NAMES[m as usize]).collect::<Vec<_>>().join(" ")
}

/// The inverse of a DR-move sequence, with turns of opposite faces put back in the order U D, R L, F B.
fn inverse(moves: &[u8]) -> Vec<u8> {
    let mut out: Vec<u8> = moves.iter().rev().map(|&m| [2, 1, 0, 5, 4, 3, 6, 7, 8, 9][m as usize]).collect();
    for i in 1..out.len() {
        let (f, g) = (MOVE_FACE[out[i - 1] as usize], MOVE_FACE[out[i] as usize]);
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
        let cases = classes::classes(&cosets);
        let mut case_of = vec![0u16; NCOSETS];
        for (i, c) in cases.iter().enumerate() {
            for &x in &c.members {
                case_of[x] = i as u16;
            }
        }
        let u2_mates = classes::u2_mates(&cosets, &cases);
        Index { htr, cube: MoveTables::new(), cosets, labels, cases, case_of, u2_mates }
    }

    pub fn case_of(&self, coset: usize) -> usize {
        self.case_of[coset] as usize
    }

    /// How long the listed HTRs of a coset go: up to `max_len` moves but at most [`ABOVE_SHORTEST`] over its
    /// shortest, and the shortest if there are none that short.
    /// (HTR with the E slice turned, case 1, is HTR up to the E slice: only its shortest, the E slice itself.)
    pub fn longest(&self, coset: usize, max_len: usize) -> usize {
        let dist = self.cosets.dist[coset] as usize;
        if coset == self.cosets.turned_solved {
            dist
        } else {
            dist.max(max_len.min(dist + ABOVE_SHORTEST))
        }
    }

    /// Every HTR of a coset in the listed form (see [`Cosets::solutions`]), as DR moves, as long as
    /// [`Index::longest`] says.
    pub fn all_solutions(&self, coset: usize, max_len: usize) -> Vec<Vec<u8>> {
        self.cosets.solutions(coset, self.longest(coset, max_len))
    }

    /// The listed HTRs: [`Index::all_solutions`] with one of each set that is the same up to the E slice
    /// ([`cosets::modulo_e`]), the shortest (then the first in move order), shortest first.
    pub fn solutions(&self, coset: usize, max_len: usize) -> Vec<Vec<u8>> {
        let all = self.all_solutions(coset, max_len);
        let mut seen = std::collections::HashSet::new();
        let mut kept: Vec<Vec<u8>> = Vec::new();
        let mut by_length: Vec<&Vec<u8>> = all.iter().collect();
        by_length.sort_by_key(|s| s.len()); // stable: move order within a length
        for s in by_length {
            if seen.insert(cosets::modulo_e(s)) {
                kept.push(s.clone());
            }
        }
        kept
    }

    pub fn solution_texts(&self, coset: usize, max_len: usize) -> Vec<String> {
        self.solutions(coset, max_len).iter().map(|s| dr_text(s)).collect()
    }

    /// A shortest sequence that makes the coset from a solved cube: the inverse of its first shortest HTR.
    pub fn generator(&self, coset: usize) -> Vec<u8> {
        if coset == self.cosets.solved {
            return Vec::new();
        }
        let shortest = self.cosets.solutions(coset, self.cosets.dist[coset] as usize);
        inverse(&shortest[0])
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
            label: self.labels.of(x),
            bad_corners: (0..8)
                .filter(|&p| self.cosets.corner_mask[x] >> p & 1 == 1)
                .map(|p| CORNER_PLACES[p])
                .collect(),
            bad_edges: (0..8).filter(|&p| self.cosets.edge_mask[x] >> p & 1 == 1).map(|p| EDGE_PLACES[p]).collect(),
            lookalikes: c.lookalikes.iter().map(|&j| j + 1).collect(),
            u2_mates: self.u2_mates[i].iter().map(|&j| j + 1).collect(),
            corner_test: dr_text(&self.cosets.corner_solution(x)),
            generator: dr_text(&self.generator(x)),
            solutions: self.solutions(x, MAX_LEN).len(),
            turned: Turned {
                corners: 8 - corners,
                edges: 8 - edges,
                moves: self.cosets.dist[t],
                label: self.labels.of(t),
                corner_test: dr_text(&self.cosets.corner_solution(t)),
                generator: dr_text(&self.generator(t)),
            },
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
    pub fn find_attempt(&self, text: &str, max_len: usize) -> Result<FoundInfo, String> {
        let (scramble, moves) = find::split_attempt(text);
        if scramble.is_empty() {
            return Err("enter a scramble and your moves to DR, or a setup".into());
        }
        self.find(&scramble, &moves, max_len)
    }

    /// Read a solver's DR from a scramble and the moves so far (NISS moves in brackets), with its HTRs of up to
    /// `max_len` moves.
    pub fn find(&self, scramble: &str, solution: &str, max_len: usize) -> Result<FoundInfo, String> {
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
        Ok(FoundInfo {
            axis: AXIS_NAMES[found.axis],
            number: i + 1,
            turned,
            subset: SUBSET_NAMES[c.subset as usize],
            edges: c.edges,
            moves: self.cosets.dist[x],
            label: self.labels.of(x),
            corners: names(self.cosets.corner_mask[x], &CORNER_PLACES),
            edge_pieces: names(self.cosets.edge_mask[x], &EDGE_PLACES),
            highlighted_are_bad: few,
            bad: self.cosets.bad(x),
            corner_test: in_frame(&self.cosets.corner_solution(x)),
            solutions: self.solutions(x, max_len).iter().map(|s| in_frame(s)).collect(),
        })
    }
}

impl Default for Index {
    fn default() -> Self {
        Self::new()
    }
}
