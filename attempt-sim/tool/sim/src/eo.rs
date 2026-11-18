//! Every EO of a scramble up to a length, on the three axes: on the normal side, on the inverse side, and with turns
//! on both sides (NISS).
//!
//! An EO is a pair (N, I), N on the normal side and I on the inverse side, with `I^-1 S N` EO-solved on its axis:
//!
//! * normal: I empty, EO reached for the first time at N's last turn;
//! * inverse: N empty, the same on the inverse scramble;
//! * NISS: both non-empty; I ends in a quarter turn of the axis and is not an EO by itself, and EO is reached for the
//!   first time at N's last turn (each side ends in a quarter turn of the axis).
//!
//! The last turn of each side is a quarter turn of the axis and can be made either way, so EOs come in groups of two
//! (four with NISS) *endings*.  A solver finds the group; its endings are the starting points for the DR.

use crate::cube::{canonical_after, invert, Cube, Move, EO_VIEW};
use crate::rng::hash_bytes;
use crate::tables::Tables;
use std::collections::HashMap;

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum EoKind {
    Normal,
    Inverse,
    Niss,
}

impl EoKind {
    pub fn name(self) -> &'static str {
        match self {
            EoKind::Normal => "normal",
            EoKind::Inverse => "inverse",
            EoKind::Niss => "NISS",
        }
    }
}

/// One ending of an EO: moves on the normal side and on the inverse side.
#[derive(Clone, Debug)]
pub struct Ending {
    pub normal: Vec<Move>,
    pub inverse: Vec<Move>,
}

#[derive(Clone, Debug)]
pub struct Eo {
    pub axis: usize,
    pub kind: EoKind,
    pub len: usize,
    /// a name for the random draws about this EO
    pub key: u64,
    pub endings: Vec<Ending>,
}

/// A sequence written the way FMC solvers do: `N (I)`.
pub fn niss_text(normal: &[Move], inverse: &[Move]) -> String {
    let n = crate::cube::format_moves(normal);
    let i = crate::cube::format_moves(inverse);
    match (normal.is_empty(), inverse.is_empty()) {
        (true, true) => "(nothing)".into(),
        (false, true) => n,
        (true, false) => format!("({i})"),
        (false, false) => format!("{n} ({i})"),
    }
}

impl Eo {
    /// The EO with the last turns made clockwise, e.g. `F (R' U F)`, for naming the group.
    pub fn text(&self) -> String {
        let e = &self.endings[0];
        let cw = |q: &[Move]| -> Vec<Move> {
            let mut v = q.to_vec();
            if let Some(l) = v.last_mut() {
                *l = Move::new(l.face(), 1);
            }
            v
        };
        niss_text(&cw(&e.normal), &cw(&e.inverse))
    }
}

/// The canonical move sequences from `flips` to EO on F/B within `left` turns.
fn to_eo(t: &Tables, flips: usize, left: usize, last: Option<Move>, path: &mut Vec<Move>, found: &mut dyn FnMut(&[Move])) {
    if flips == 0 {
        found(path);
        return;
    }
    if t.eo_dist[flips] as usize > left {
        return;
    }
    for m in Move::all() {
        if !canonical_after(last, m) {
            continue;
        }
        path.push(m);
        to_eo(t, t.flip_move[flips][m.index()] as usize, left - 1, Some(m), path, found);
        path.pop();
    }
}

/// Every canonical sequence of exactly `k` turns, with P = the state of its inverse.
fn sequences(t: &Tables, k: usize, last: Option<Move>, seq: &mut Vec<Move>, p: &Cube, found: &mut dyn FnMut(&[Move], &Cube)) {
    if seq.len() == k {
        found(seq, p);
        return;
    }
    for m in Move::all() {
        if !canonical_after(last, m) {
            continue;
        }
        let q = t.moves.move_cube(m.inverse()).then(p);
        seq.push(m);
        sequences(t, k, Some(m), seq, &q, found);
        seq.pop();
    }
}

/// A half turn among a side's last turns about the EO axis commutes to the end and keeps EO: that is a shorter EO
/// followed by an RZP move, not an EO of its own.
fn ends_in_a_half_turn(q: &[Move]) -> bool {
    let Some(last) = q.last() else { return false };
    q.iter().rev().take_while(|m| m.axis() == last.axis()).any(|m| m.is_half_turn())
}

/// Every EO of at most `max_len` turns of the scramble, on every axis (with `niss`, also those with turns on both
/// sides), grouped by endings, sorted by length, kind, axis and key.
pub fn enumerate(t: &Tables, scramble: &[Move], max_len: usize, niss: bool) -> Vec<Eo> {
    let mut groups: Vec<Eo> = Vec::new();
    let mut index: HashMap<u64, usize> = HashMap::new();
    for axis in 0..3 {
        let view = &EO_VIEW[axis];
        let sv = t.moves.state(&view.seq_to_view(scramble));
        let sv_inv = sv.inverse();
        let mut add = |kind: EoKind, normal: Vec<Move>, inverse: Vec<Move>| {
            if ends_in_a_half_turn(&normal) || ends_in_a_half_turn(&inverse) {
                return;
            }
            // the group: both sides with their last turn made clockwise
            let clockwise = |q: &[Move]| -> Vec<u8> {
                let mut v: Vec<u8> = q.iter().map(|m| m.0).collect();
                if let Some(l) = v.last_mut() {
                    *l = 3 * (*l / 3);
                }
                v
            };
            let mut k = vec![axis as u8, 0xFE];
            k.extend(clockwise(&normal));
            k.push(0xFF);
            k.extend(clockwise(&inverse));
            let key = hash_bytes(0xE0, &k);
            let len = normal.len() + inverse.len();
            let gi = *index.entry(key).or_insert_with(|| {
                groups.push(Eo { axis, kind, len, key, endings: Vec::new() });
                groups.len() - 1
            });
            groups[gi].endings.push(Ending { normal, inverse });
        };
        let mut found: Vec<Vec<Move>> = Vec::new();
        to_eo(t, sv.flip_pattern(), max_len, None, &mut Vec::new(), &mut |p| found.push(p.to_vec()));
        for p in &found {
            add(EoKind::Normal, view.seq_from_view(p), Vec::new());
        }
        found.clear();
        to_eo(t, sv_inv.flip_pattern(), max_len, None, &mut Vec::new(), &mut |p| found.push(p.to_vec()));
        for p in &found {
            // an EO that is already solved is the same EO on both sides: keep the normal one
            if !p.is_empty() {
                add(EoKind::Inverse, Vec::new(), view.seq_from_view(p));
            }
        }
        if niss {
            let mut both: Vec<(Vec<Move>, Vec<Move>)> = Vec::new();
            for k in 1..max_len {
                sequences(t, k, None, &mut Vec::new(), &Cube::SOLVED, &mut |iseq, p| {
                    if !iseq.last().unwrap().is_quarter_turn_of(2) {
                        return;
                    }
                    let flips = p.then(&sv).flip_pattern();
                    if flips == 0 || k + t.eo_dist[flips] as usize > max_len {
                        return;
                    }
                    to_eo(t, flips, max_len - k, None, &mut Vec::new(), &mut |nseq| both.push((nseq.to_vec(), iseq.to_vec())));
                });
            }
            for (n, i) in &both {
                add(EoKind::Niss, view.seq_from_view(n), view.seq_from_view(i));
            }
        }
    }
    for g in groups.iter_mut() {
        g.endings.sort_by(|a, b| (&a.normal, &a.inverse).cmp(&(&b.normal, &b.inverse)));
    }
    groups.sort_by_key(|g| (g.len, g.kind as u8, g.axis, g.key));
    groups
}

/// The state `I^-1 S N` reached with N on the normal side and I on the inverse side, in a view: every turn made on the
/// face the view takes it to.
pub fn view_state(t: &Tables, view: &crate::cube::View, scramble: &[Move], normal: &[Move], inverse: &[Move]) -> Cube {
    let mut seq = view.seq_to_view(&invert(inverse));
    seq.extend(view.seq_to_view(scramble));
    seq.extend(view.seq_to_view(normal));
    t.moves.state(&seq)
}
