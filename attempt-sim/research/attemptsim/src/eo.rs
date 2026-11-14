//! Every EO of a scramble up to a length, on the three axes: on the normal side, on the inverse side, and with
//! turns on both sides (NISS).
//!
//! An EO is a pair (N, I): N on the normal side, I on the inverse side, with `I^-1 S N` EO-solved on the axis.
//!   normal   I empty; EO reached for the first time at N's last turn
//!   inverse  N empty; the same on the inverse scramble
//!   NISS     both non-empty; I ends in a quarter turn of the axis and is not an EO by itself, and EO is reached for
//!            the first time at N's last turn (eo-to-dr's definition: each side ends in a quarter turn of the axis)
//! The last turn of each side is a quarter turn of the axis and can be made either way, so EOs come in groups of two
//! (four with NISS) *endings*.  A solver finds the group; the endings are its starting points for the DR.

use crate::ctx::*;
use crate::cubie::{Cubie, SOLVED};
use crate::rngx::hseq;
use std::collections::HashMap;

#[derive(Clone, Debug)]
pub struct EoRoot {
    pub n: Vec<u8>,
    pub i: Vec<u8>,
}
#[derive(Clone, Debug)]
pub struct EoGroup {
    pub axis: u8,
    /// 0 normal, 1 inverse, 2 NISS
    pub kind: u8,
    pub len: u8,
    pub key: u64,
    pub roots: Vec<EoRoot>,
}

fn lin_dfs(c: &Ctx, e: usize, left: usize, last: u8, path: &mut Vec<u8>, f: &mut dyn FnMut(&[u8])) {
    if e == 0 {
        f(path);
        return;
    }
    if c.eodist[e] as usize > left {
        return;
    }
    for mv in 0..18u8 {
        if !canon_ok(last, mv) {
            continue;
        }
        path.push(mv);
        lin_dfs(c, c.eo_mv[e][mv as usize] as usize, left - 1, mv, path, f);
        path.pop();
    }
}

/// All canonical sequences of exactly k turns (view labels) with P = their inverse as a state.
fn premoves(c: &Ctx, k: usize, last: u8, seq: &mut Vec<u8>, p: &Cubie, f: &mut dyn FnMut(&[u8], &Cubie)) {
    if seq.len() == k {
        f(seq, p);
        return;
    }
    for mv in 0..18u8 {
        if !canon_ok(last, mv) {
            continue;
        }
        let q = c.mvc[inv_move(mv) as usize].then(p);
        seq.push(mv);
        premoves(c, k, mv, seq, &q, f);
        seq.pop();
    }
}

/// Every EO of at most `maxlen` turns on every axis (`niss`: also those with turns on both sides), grouped by
/// endings, sorted by (length, kind, axis, key).
pub fn enumerate(c: &Ctx, s: &Cubie, maxlen: usize, niss: bool) -> Vec<EoGroup> {
    let mut groups: Vec<EoGroup> = Vec::new();
    let mut index: HashMap<u64, usize> = HashMap::new();
    for y in 0..3usize {
        let r = c.rot_eo[y];
        let sv = c.m.conj(s, r);
        let svi = sv.inverse();
        let own = |seq: &[u8]| -> Vec<u8> { seq.iter().map(|&mv| c.umove[r][mv as usize]).collect() };
        let mut add = |kind: u8, n: Vec<u8>, i: Vec<u8>| {
            // a half turn among a side's last turns about the EO axis commutes to the end and keeps EO: that is a
            // shorter EO followed by a half turn (an RZP move), not an EO of its own
            let redundant = |q: &[u8]| {
                let ax = q.last().map(|&m| m / 6);
                q.iter().rev().take_while(|&&m| Some(m / 6) == ax).any(|&m| m % 3 == 1)
            };
            if redundant(&n) || redundant(&i) {
                return;
            }
            // the group: both sequences with their last turn made clockwise
            let norm = |q: &[u8]| -> Vec<u8> {
                let mut v = q.to_vec();
                if let Some(l) = v.last_mut() {
                    *l = 3 * (*l / 3);
                }
                v
            };
            let mut k = vec![y as u8, 0xFE];
            k.extend(norm(&n));
            k.push(0xFF);
            k.extend(norm(&i));
            let key = hseq(0xE0, &k);
            let len = (n.len() + i.len()) as u8;
            let gi = *index.entry(key).or_insert_with(|| {
                groups.push(EoGroup { axis: y as u8, kind, len, key, roots: Vec::new() });
                groups.len() - 1
            });
            groups[gi].roots.push(EoRoot { n, i });
        };
        // normal and inverse, linear
        let mut found: Vec<Vec<u8>> = Vec::new();
        lin_dfs(c, Ctx::eo_of(&sv), maxlen, NONE, &mut Vec::new(), &mut |p| found.push(p.to_vec()));
        for p in &found {
            add(0, own(p), Vec::new());
        }
        found.clear();
        lin_dfs(c, Ctx::eo_of(&svi), maxlen, NONE, &mut Vec::new(), &mut |p| found.push(p.to_vec()));
        for p in &found {
            // an EO that is already solved (length 0) is the same EO on both sides: keep the normal one
            if !p.is_empty() {
                add(1, Vec::new(), own(p));
            }
        }
        if niss {
            let mut both: Vec<(Vec<u8>, Vec<u8>)> = Vec::new();
            for k in 1..maxlen {
                premoves(c, k, NONE, &mut Vec::new(), &SOLVED, &mut |iseq, p| {
                    if !axis_quarter(*iseq.last().unwrap(), 2) {
                        return;
                    }
                    let st = p.then(&sv);
                    let e = Ctx::eo_of(&st);
                    if e == 0 || k + c.eodist[e] as usize > maxlen {
                        return;
                    }
                    lin_dfs(c, e, maxlen - k, NONE, &mut Vec::new(), &mut |nseq| both.push((nseq.to_vec(), iseq.to_vec())));
                });
            }
            for (n, i) in &both {
                add(2, own(n), own(i));
            }
        }
    }
    for g in groups.iter_mut() {
        g.roots.sort_by(|a, b| (&a.n, &a.i).cmp(&(&b.n, &b.i)));
    }
    groups.sort_by_key(|g| (g.len, g.kind, g.axis, g.key));
    groups
}
