//! The cases: cosets up to the 16 symmetries and the E slice, the bad pieces each one is drawn with, and which
//! cases look the same.

use crate::cosets::{Cosets, NCOSETS};
use attempt_sim::dr::NSYM;
use std::collections::HashMap;

/// Bad corners and bad edges as place masks.
pub type Layout = (u8, u8);

pub struct Class {
    /// the coset drawn and solved: the highlighted pieces are its bad pieces, relative to the centres
    pub coset: usize,
    /// the corner subset (index into `SUBSET_NAMES`) and the bad edges, in the frame with few bad pieces
    pub subset: u8,
    pub edges: u8,
    /// fewest moves to HTR
    pub moves: u8,
    /// every coset of the case: its symmetric copies and theirs with the E slice turned
    pub members: Vec<usize>,
    /// the other cases whose bad pieces look the same (indices into the sorted list)
    pub lookalikes: Vec<usize>,
}

/// How many bad pieces a front-right-top view of the cube hides (DBL, DL, DB), then more bad corners on U: lower is
/// a better picture.
fn view_score((corners, edges): Layout) -> (u8, std::cmp::Reverse<u32>, Layout) {
    let hidden = (corners >> 6 & 1) + (edges >> 5 & 1) + (edges >> 6 & 1);
    (hidden, std::cmp::Reverse((corners & 0x0F).count_ones()), (corners, edges))
}

/// Every case, sorted by subset (in the order of `SUBSET_NAMES`), bad edges, moves to HTR, then how it is drawn.
pub fn classes(cs: &Cosets) -> Vec<Class> {
    // a case is a coset with everything it is joined to by a symmetry or the E slice
    let mut class_of = vec![usize::MAX; NCOSETS];
    let mut members: Vec<Vec<usize>> = Vec::new();
    for x in 0..NCOSETS {
        if class_of[x] != usize::MAX {
            continue;
        }
        let id = members.len();
        class_of[x] = id;
        let mut stack = vec![x];
        let mut list = Vec::new();
        while let Some(y) = stack.pop() {
            list.push(y);
            for z in (0..NSYM).map(|s| cs.sym[y][s] as usize).chain([cs.eslice[y] as usize]) {
                if class_of[z] == usize::MAX {
                    class_of[z] = id;
                    stack.push(z);
                }
            }
        }
        list.sort_unstable();
        members.push(list);
    }

    // Cases look the same when they share a set of layouts (the symmetries and the E slice move a layout around, and
    // turn it into its complement).  Each such set is drawn one way, with the few-frame layout of best view_score.
    let layout = |x: usize| -> Layout { (cs.corner_mask[x], cs.edge_mask[x]) };
    let key = |m: &[usize]| m.iter().map(|&x| layout(x)).min().expect("a case has cosets");
    let mut drawn: HashMap<Layout, Layout> = HashMap::new();
    for m in &members {
        for &x in m.iter().filter(|&&x| cs.few_frame(x)) {
            let best = drawn.entry(key(m)).or_insert(layout(x));
            if view_score(layout(x)) < view_score(*best) {
                *best = layout(x);
            }
        }
    }

    let mut out: Vec<Class> = members
        .into_iter()
        .map(|m| {
            let want = drawn[&key(&m)];
            let mut coset = *m.iter().find(|&&x| layout(x) == want).expect("a case has the layout it is drawn with");
            if coset == cs.solved {
                // HTR itself looks like HTR with the E slice turned; the second is the case
                coset = cs.eslice[coset] as usize;
            }
            let (c, e) = cs.bad(coset);
            let edges = if c < 4 || (c == 4 && e <= 4) { e } else { 8 - e };
            Class {
                coset,
                subset: cs.subset[coset],
                edges: edges as u8,
                moves: cs.dist[coset],
                members: m,
                lookalikes: Vec::new(),
            }
        })
        .collect();
    out.sort_by_key(|c| (c.subset, c.edges, c.moves, layout(c.coset), c.coset));

    let keys: Vec<Layout> = out.iter().map(|c| key(&c.members)).collect();
    for i in 0..out.len() {
        out[i].lookalikes = (0..out.len()).filter(|&j| j != i && keys[j] == keys[i]).collect();
    }
    out
}

/// Cases that meet after their first quarter turn: B is A after U2 (or D2: the symmetries swap U and D), and on both
/// a shortest HTR starts with a quarter turn of that layer.  A with that turn one way and B with it the other way
/// reach the same coset (U2 then U' is U), so after it they are one case.  For each case, the others joined to it this
/// way, directly or through others (indices into `cases`).
pub fn u2_mates(cs: &Cosets, cases: &[Class]) -> Vec<Vec<usize>> {
    let mut case_of = vec![0usize; NCOSETS];
    for (i, c) in cases.iter().enumerate() {
        for &x in &c.members {
            case_of[x] = i;
        }
    }
    // does a shortest HTR from x start with one of these two quarter turns?
    let starts_with = |x: usize, turns: [usize; 2]| {
        cs.dist[x] > 0 && turns.iter().any(|&q| cs.dist[cs.mv[x][q] as usize] + 1 == cs.dist[x])
    };
    let mut parent: Vec<usize> = (0..cases.len()).collect();
    fn root(parent: &mut [usize], mut i: usize) -> usize {
        while parent[i] != i {
            parent[i] = parent[parent[i]];
            i = parent[i];
        }
        i
    }
    // (U, U') with U2, and (D, D') with D2, as DR moves
    for (turns, half) in [([0, 2], 1), ([3, 5], 4)] {
        for x in 0..NCOSETS {
            let y = cs.mv[x][half] as usize;
            if starts_with(x, turns) && starts_with(y, turns) {
                let (a, b) = (root(&mut parent, case_of[x]), root(&mut parent, case_of[y]));
                parent[a.max(b)] = a.min(b);
            }
        }
    }
    let roots: Vec<usize> = (0..cases.len()).map(|i| root(&mut parent, i)).collect();
    (0..cases.len()).map(|i| (0..cases.len()).filter(|&j| j != i && roots[j] == roots[i]).collect()).collect()
}
