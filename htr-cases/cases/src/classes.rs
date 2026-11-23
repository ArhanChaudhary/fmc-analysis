//! The cases: cosets up to the 16 symmetries and the E slice (the classes), the bad pieces each one is drawn with,
//! which cases look the same, and the list: every coset with its class's picture ([`entries`]).

use crate::cosets::{Cosets, NCOSETS};
use attempt_sim::dr::NSYM;
use std::collections::{BTreeMap, HashMap};

/// Bad corners and bad edges as place masks.
pub type Layout = (u8, u8);

pub struct Class {
    /// the coset drawn and solved: the highlighted pieces are its bad pieces, relative to the centres
    pub coset: usize,
    /// the corner subset (index into `SUBSET_NAMES`) and the bad edges, in the frame with few bad pieces
    pub subset: u8,
    pub edges: u8,
    /// the optimal: fewest face turns to HTR, DR-breaking HTRs included
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

/// Every case, sorted by subset (in the order of `SUBSET_NAMES`), bad edges, optimal (`dist`: the fewest face turns to
/// HTR of each coset), then how it is drawn.
pub fn classes(cs: &Cosets, dist: &[u8]) -> Vec<Class> {
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
                moves: dist[coset],
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

/// A case as listed: one coset with its class's picture.  A class whose picture a symmetry maps onto itself while
/// moving the coset (its mirror image looks the same, say), or a 4-corner 4-edge class whose E-slice twin looks the
/// same, is listed once for each coset with that picture: they look alike and take different HTRs.
pub struct Entry {
    pub coset: usize,
    /// its class (index into the classes)
    pub class: usize,
    pub subset: u8,
    pub edges: u8,
    /// the optimal: fewest face turns to HTR, DR-breaking HTRs included
    pub moves: u8,
    /// the other entries whose bad pieces look the same, its siblings included (indices into the entries)
    pub lookalikes: Vec<usize>,
    /// the other entries of its class (the same picture), and what each is of this one: "in a mirror", "turned", "with
    /// the E slice turned"
    pub siblings: Vec<(usize, &'static str)>,
}

/// The list: every coset with its class's picture (HTR itself aside), sorted by subset, bad edges, optimal, picture,
/// class, coset.  Seen from some side, every DR state is one of them, and every coset that looks like a listed picture
/// is listed (`cargo test` checks both).
pub fn entries(cs: &Cosets, classes: &[Class], dist: &[u8]) -> Vec<Entry> {
    let layout = |x: usize| -> Layout { (cs.corner_mask[x], cs.edge_mask[x]) };
    let mut list: Vec<(usize, usize)> = Vec::new();
    for (k, c) in classes.iter().enumerate() {
        let picture = layout(c.coset);
        for &y in c.members.iter().filter(|&&y| y != cs.solved && layout(y) == picture) {
            list.push((y, k));
        }
    }
    list.sort_by_key(|&(y, k)| (cs.subset[y], classes[k].edges, dist[y], layout(y), k, y));
    let mut by_picture: BTreeMap<Layout, Vec<usize>> = BTreeMap::new();
    for (i, &(y, _)) in list.iter().enumerate() {
        by_picture.entry(layout(y)).or_default().push(i);
    }
    // how another coset of the class is this one seen: turned (a rotation), in a mirror, or with the E slice turned
    let relation = |x: usize, y: usize| -> &'static str {
        let by = |from: usize, syms: std::ops::Range<usize>| syms.into_iter().any(|s| cs.sym[from][s] as usize == y);
        if by(x, 0..8) {
            "turned"
        } else if by(x, 8..NSYM) {
            "in a mirror"
        } else {
            "with the E slice turned"
        }
    };
    list.iter()
        .enumerate()
        .map(|(i, &(y, k))| Entry {
            coset: y,
            class: k,
            subset: cs.subset[y],
            edges: classes[k].edges,
            moves: dist[y],
            lookalikes: by_picture[&layout(y)].iter().copied().filter(|&j| j != i).collect(),
            siblings: by_picture[&layout(y)]
                .iter()
                .copied()
                .filter(|&j| j != i && list[j].1 == k)
                .map(|j| (j, relation(y, list[j].0)))
                .collect(),
        })
        .collect()
}

/// Cases that meet after their first quarter turn: B is A after U2 (or D2: the symmetries swap U and D), seen from
/// some side, and on both a shortest HTR starts with a quarter turn of that layer.  A with that turn one way and B with
/// it the other way reach the same coset (U2 then U' is U), so after it they are one case.  For each entry, the others
/// joined to it this way directly, and those joined directly or through others: its group (indices into `entries`).
pub fn u2_mates(cs: &Cosets, entries: &[Entry], dist: &[u8]) -> (Vec<Vec<usize>>, Vec<Vec<usize>>) {
    let index: HashMap<usize, usize> = entries.iter().enumerate().map(|(i, e)| (e.coset, i)).collect();
    // does a shortest HTR from x start with one of these two quarter turns?
    let starts_with =
        |x: usize, turns: [usize; 2]| dist[x] > 0 && turns.iter().any(|&q| dist[cs.mv[x][q] as usize] + 1 == dist[x]);
    let mut parent: Vec<usize> = (0..entries.len()).collect();
    let mut direct: Vec<Vec<usize>> = vec![Vec::new(); entries.len()];
    fn root(parent: &mut [usize], mut i: usize) -> usize {
        while parent[i] != i {
            parent[i] = parent[parent[i]];
            i = parent[i];
        }
        i
    }
    // (U, U') with U2, and (D, D') with D2, as DR moves
    for (turns, half) in [([0, 2], 1), ([3, 5], 4)] {
        for (i, e) in entries.iter().enumerate() {
            let y = cs.mv[e.coset][half] as usize;
            if !(starts_with(e.coset, turns) && starts_with(y, turns)) {
                continue;
            }
            for s in 0..NSYM {
                if let Some(&j) = index.get(&(cs.sym[y][s] as usize)) {
                    let (a, b) = (root(&mut parent, i), root(&mut parent, j));
                    parent[a.max(b)] = a.min(b);
                    for (p, q) in [(i, j), (j, i)] {
                        if p != q && !direct[p].contains(&q) {
                            direct[p].push(q);
                        }
                    }
                }
            }
        }
    }
    let roots: Vec<usize> = (0..entries.len()).map(|i| root(&mut parent, i)).collect();
    for d in direct.iter_mut() {
        d.sort_unstable();
    }
    let groups = (0..entries.len()).map(|i| (0..entries.len()).filter(|&j| j != i && roots[j] == roots[i]).collect());
    (direct, groups.collect())
}
