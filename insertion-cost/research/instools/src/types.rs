//! Leftover types: the cycle structure of a corner-only or edge-only element, with the twist / flip sum of each cycle.

use crate::cubie::{Cubie, SOLVED};

pub const TYPES: [&str; 16] = [
    "3c", "2tc", "3tc", "2c2c-pure", "2c2c-twisted", "3c1t", "5c", "3c3c", // corner types
    "3e", "2f", "2e2e", "2e2e-flipped", "5e", "3e1f", "3e3e", // edge types
    "2c2e", // parity: one corner swap and one edge swap, each with zero net twist / flip
];
pub const EXPECTED: [usize; 16] = [1008, 56, 112, 1890, 3780, 10080, 108864, 90720, 1760, 66, 5940, 5940, 304128, 15840, 591360, 11088];
pub const T3C: usize = 0;
pub const T3E: usize = 8;
pub const T2C2E: usize = 15;
pub fn type_id(name: &str) -> Option<usize> {
    TYPES.iter().position(|&t| t == name)
}
pub fn is_corner(t: usize) -> bool {
    t < 8
}

/// Cycles of a permutation with orientation: the list of (length, orientation sum mod m) of every cycle that is not
/// a fixed untwisted piece, sorted in decreasing order.
fn signature(p: &[u8], o: &[u8], m: u8, out: &mut [(u8, u8); 12]) -> usize {
    let n = p.len();
    let mut seen = [false; 12];
    let mut k = 0;
    for i in 0..n {
        if seen[i] {
            continue;
        }
        let (mut j, mut len, mut tw) = (i, 0u8, 0u8);
        while !seen[j] {
            seen[j] = true;
            tw += o[j];
            j = p[j] as usize;
            len += 1;
        }
        if len > 1 || tw % m != 0 {
            out[k] = (len, tw % m);
            k += 1;
        }
    }
    out[..k].sort_unstable_by(|a, b| b.cmp(a));
    k
}

fn corner_type(sig: &[(u8, u8)]) -> Option<usize> {
    match sig {
        [(3, 0)] => Some(0),
        [(1, 2), (1, 1)] => Some(1),
        [(1, 1), (1, 1), (1, 1)] | [(1, 2), (1, 2), (1, 2)] => Some(2),
        [(2, 0), (2, 0)] => Some(3),
        [(2, 2), (2, 1)] => Some(4),
        [(3, 1), (1, 2)] | [(3, 2), (1, 1)] => Some(5),
        [(5, 0)] => Some(6),
        [(3, 0), (3, 0)] => Some(7),
        _ => None,
    }
}
fn edge_type(sig: &[(u8, u8)]) -> Option<usize> {
    match sig {
        [(3, 0)] => Some(8),
        [(1, 1), (1, 1)] => Some(9),
        [(2, 0), (2, 0)] => Some(10),
        [(2, 1), (2, 1)] => Some(11),
        [(5, 0)] => Some(12),
        [(3, 1), (1, 1)] => Some(13),
        [(3, 0), (3, 0)] => Some(14),
        _ => None,
    }
}

/// The type of an element, if it is one of the types above.
pub fn classify(c: &Cubie) -> Option<usize> {
    let mut sc = [(0u8, 0u8); 12];
    let mut se = [(0u8, 0u8); 12];
    let nc = signature(&c.cp, &c.ct, 3, &mut sc);
    let ne = signature(&c.ep, &c.ef, 2, &mut se);
    if ne == 0 {
        corner_type(&sc[..nc])
    } else if nc == 0 {
        edge_type(&se[..ne])
    } else if sc[..nc] == [(2, 0)] && se[..ne] == [(2, 0)] {
        Some(T2C2E)
    } else {
        None
    }
}

/// Permutations of n points with the given cycle structure, as p[i] = the piece at place i.
fn perms(n: usize, structure: &[usize]) -> Vec<Vec<u8>> {
    fn put(p: &mut [u8], cyc: &[usize]) {
        for k in 0..cyc.len() {
            p[cyc[(k + 1) % cyc.len()]] = cyc[k] as u8;
        }
    }
    let id: Vec<u8> = (0..n as u8).collect();
    let mut out = Vec::new();
    match structure {
        [] => out.push(id),
        [2] => {
            for a in 0..n {
                for b in a + 1..n {
                    let mut p = id.clone();
                    put(&mut p, &[a, b]);
                    out.push(p);
                }
            }
        }
        [3] => {
            for a in 0..n {
                for b in a + 1..n {
                    for c in b + 1..n {
                        for cyc in [[a, b, c], [a, c, b]] {
                            let mut p = id.clone();
                            put(&mut p, &cyc);
                            out.push(p);
                        }
                    }
                }
            }
        }
        [2, 2] => {
            for a in 0..n {
                for b in a + 1..n {
                    for c in b + 1..n {
                        for d in c + 1..n {
                            for (x, y) in [([a, b], [c, d]), ([a, c], [b, d]), ([a, d], [b, c])] {
                                let mut p = id.clone();
                                put(&mut p, &x);
                                put(&mut p, &y);
                                out.push(p);
                            }
                        }
                    }
                }
            }
        }
        [5] => {
            let mut pts = [0usize; 5];
            fn rec(n: usize, start: usize, k: usize, pts: &mut [usize; 5], id: &Vec<u8>, out: &mut Vec<Vec<u8>>) {
                if k == 5 {
                    // all cyclic orders with pts[0] first: permutations of the other four
                    let rest = [pts[1], pts[2], pts[3], pts[4]];
                    let mut idx = [0usize, 1, 2, 3];
                    loop {
                        let cyc = [pts[0], rest[idx[0]], rest[idx[1]], rest[idx[2]], rest[idx[3]]];
                        let mut p = id.clone();
                        for t in 0..5 {
                            p[cyc[(t + 1) % 5]] = cyc[t] as u8;
                        }
                        out.push(p);
                        // next permutation of idx
                        let mut i = 3;
                        while i > 0 && idx[i - 1] > idx[i] {
                            i -= 1;
                        }
                        if i == 0 {
                            break;
                        }
                        let mut j = 3;
                        while idx[j] < idx[i - 1] {
                            j -= 1;
                        }
                        idx.swap(i - 1, j);
                        idx[i..].reverse();
                    }
                    return;
                }
                for a in start..n {
                    pts[k] = a;
                    rec(n, a + 1, k + 1, pts, id, out);
                }
            }
            rec(n, 0, 0, &mut pts, &id, &mut out);
        }
        [3, 3] => {
            for a in 0..n {
                for b in a + 1..n {
                    for c in b + 1..n {
                        for d in a + 1..n {
                            for e in d + 1..n {
                                for f in e + 1..n {
                                    if [d, e, f].iter().any(|x| [a, b, c].contains(x)) {
                                        continue;
                                    }
                                    for x in [[a, b, c], [a, c, b]] {
                                        for y in [[d, e, f], [d, f, e]] {
                                            let mut p = id.clone();
                                            put(&mut p, &x);
                                            put(&mut p, &y);
                                            out.push(p);
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        _ => panic!("structure"),
    }
    out
}

/// Every element of a type, by construction: all permutations with the cycle structure, all orientations on the moved
/// pieces and on `extra` further pieces, kept when `classify` agrees.  (The count is checked against EXPECTED.)
pub fn elements(t: usize) -> Vec<Cubie> {
    let (structure, extra): (&[usize], usize) = match TYPES[t] {
        "3c" | "3e" => (&[3], 0),
        "2tc" | "2f" => (&[], 2),
        "3tc" => (&[], 3),
        "2c2c-pure" | "2c2c-twisted" | "2e2e" | "2e2e-flipped" => (&[2, 2], 0),
        "3c1t" | "3e1f" => (&[3], 1),
        "5c" | "5e" => (&[5], 0),
        "3c3c" | "3e3e" => (&[3, 3], 0),
        _ => panic!("type"),
    };
    let corner = is_corner(t);
    let (n, m) = if corner { (8usize, 3u8) } else { (12usize, 2u8) };
    let mut out = Vec::new();
    for p in perms(n, structure) {
        let moved: Vec<usize> = (0..n).filter(|&i| p[i] as usize != i).collect();
        let fixed: Vec<usize> = (0..n).filter(|&i| p[i] as usize == i).collect();
        // choose `extra` fixed pieces (as an increasing list)
        let mut choice: Vec<usize> = (0..extra).collect();
        loop {
            let pts: Vec<usize> = moved.iter().copied().chain(choice.iter().map(|&k| fixed[k])).collect();
            let total = (m as usize).pow(pts.len() as u32);
            for v in 0..total {
                let mut o = [0u8; 12];
                let mut w = v;
                let mut ok = true;
                for (k, &pt) in pts.iter().enumerate() {
                    o[pt] = (w % m as usize) as u8;
                    w /= m as usize;
                    if k >= moved.len() && o[pt] == 0 {
                        ok = false; // an extra piece must be twisted, or the same element comes up twice
                    }
                }
                if !ok {
                    continue;
                }
                let mut c = SOLVED;
                if corner {
                    c.cp.copy_from_slice(&p);
                    c.ct.copy_from_slice(&o[..8]);
                    if c.ct.iter().map(|&x| x as u32).sum::<u32>() % 3 != 0 {
                        continue;
                    }
                } else {
                    c.ep.copy_from_slice(&p);
                    c.ef.copy_from_slice(&o[..12]);
                    if c.ef.iter().map(|&x| x as u32).sum::<u32>() % 2 != 0 {
                        continue;
                    }
                }
                if classify(&c) == Some(t) {
                    out.push(c);
                }
            }
            // next choice
            let mut i = extra;
            loop {
                if i == 0 {
                    break;
                }
                i -= 1;
                if choice[i] < fixed.len() - (extra - i) {
                    choice[i] += 1;
                    for j in i + 1..extra {
                        choice[j] = choice[j - 1] + 1;
                    }
                    i = usize::MAX;
                    break;
                }
            }
            if i != usize::MAX {
                break;
            }
        }
    }
    out
}

/// Elements of the parity family 2c2e.
pub fn elements_2c2e() -> Vec<Cubie> {
    let mut out = Vec::new();
    for cp in perms(8, &[2]) {
        let mv: Vec<usize> = (0..8).filter(|&i| cp[i] as usize != i).collect();
        for tw in 0..3u8 {
            for ep in perms(12, &[2]) {
                let me: Vec<usize> = (0..12).filter(|&i| ep[i] as usize != i).collect();
                for fl in 0..2u8 {
                    let mut c = SOLVED;
                    c.cp.copy_from_slice(&cp);
                    c.ep.copy_from_slice(&ep);
                    c.ct[mv[0]] = tw;
                    c.ct[mv[1]] = (3 - tw) % 3;
                    c.ef[me[0]] = fl;
                    c.ef[me[1]] = fl;
                    assert_eq!(classify(&c), Some(T2C2E));
                    out.push(c);
                }
            }
        }
    }
    out
}

/// All 3-cycles d (of corners when `corner`, else of edges) with c·d again a 3-cycle: the first insertions that
/// leave a single 3-cycle.  (A 3-cycle that moves two pieces c leaves alone cannot work, so only those are built that
/// move at most one such piece.)
pub fn splits(c: &Cubie, corner: bool) -> Vec<Cubie> {
    let (n, m, want) = if corner { (8usize, 3u8, T3C) } else { (12usize, 2u8, T3E) };
    let touched = |i: usize| if corner { c.cp[i] as usize != i || c.ct[i] != 0 } else { c.ep[i] as usize != i || c.ef[i] != 0 };
    let mut out = Vec::new();
    for a in 0..n {
        for b in a + 1..n {
            for x in b + 1..n {
                let outside = [a, b, x].iter().filter(|&&i| !touched(i)).count();
                if outside > 1 {
                    continue;
                }
                for cyc in [[a, b, x], [a, x, b]] {
                    for o1 in 0..m {
                        for o2 in 0..m {
                            let o3 = (2 * m - o1 - o2) % m;
                            let mut d = SOLVED;
                            for k in 0..3 {
                                let (from, to) = (cyc[k], cyc[(k + 1) % 3]);
                                let o = [o1, o2, o3][k];
                                if corner {
                                    d.cp[to] = from as u8;
                                    d.ct[to] = o;
                                } else {
                                    d.ep[to] = from as u8;
                                    d.ef[to] = o;
                                }
                            }
                            if classify(&c.then(&d)) == Some(want) {
                                out.push(d);
                            }
                        }
                    }
                }
            }
        }
    }
    out
}

/// First insertions for the mixed model: every d with c·d of one of the types (of the same kind of piece), where
/// d or c·d is a 3-cycle.  `fam` is the list of all 3-cycles of that kind.
pub fn splits_mixed(c: &Cubie, corner: bool, fam: &[Cubie]) -> Vec<Cubie> {
    let want = if corner { T3C } else { T3E };
    let kind = |x: &Cubie| classify(x).filter(|&t| t != T2C2E && is_corner(t) == corner);
    let ci = c.inverse();
    let mut out: Vec<Cubie> = Vec::new();
    for x in fam {
        debug_assert_eq!(classify(x), Some(want));
        if kind(&c.then(x)).is_some() {
            out.push(*x); // d = x is the 3-cycle
        }
        let d = ci.then(x); // c·d = x is the 3-cycle
        if kind(&d).is_some() && kind(&d) != Some(want) {
            out.push(d);
        }
    }
    out
}

/// A readable description: which piece goes where ("UFR>UBL+1": the piece from UFR ends at UBL, twisted by 1).
pub fn describe(c: &Cubie, cn: &[String], en: &[String]) -> String {
    let mut parts = Vec::new();
    for i in 0..8 {
        if c.cp[i] as usize != i || c.ct[i] != 0 {
            parts.push(format!("{}>{}{}", cn[c.cp[i] as usize], cn[i], if c.ct[i] != 0 { format!("+{}", c.ct[i]) } else { String::new() }));
        }
    }
    for i in 0..12 {
        if c.ep[i] as usize != i || c.ef[i] != 0 {
            parts.push(format!("{}>{}{}", en[c.ep[i] as usize], en[i], if c.ef[i] != 0 { "+1" } else { "" }));
        }
    }
    parts.join(" ")
}
