//! Exact insertion costs of one skeleton.
//!
//! Z·S = c (scramble, skeleton, leftover).  Inserting A at position i of S solves the scramble exactly when A's
//! product is g_i = Y c^-1 Y^-1 with Y = S[i..].  The result is cancel(S[..i] + A + S[i..]).
//!
//! `single`  one insertion of any sequence of length <= L whose product is g_i: the minimum over every position and
//!           every such sequence (models `one` and `direct`).
//! `two`     two insertions of 3-cycles, the second into the sequence the first one gives (model `two`).

use crate::algs::Table;
use crate::cubie::{Cubie, Model, SOLVED};
use crate::seq::{self, insert};
use crate::types;

#[derive(Clone, Copy, Debug)]
pub struct Ins {
    pub pos: usize,
    pub alg: u64,
}
#[derive(Clone, Debug)]
pub struct Sol {
    pub len: usize, // length of the final solution
    pub ins: Vec<Ins>,
    pub nested: bool,
}

/// What a sequence meets on one side of the place where it is inserted: the nearest run (axis, faces present), the
/// inverses of the moves of the nearest run and of the nearest two runs (as sets of moves), and the size of the larger
/// of those two runs.
#[derive(Clone, Copy)]
struct Side {
    ax: u8,
    mk: u8,
    inv1: u32,
    inv12: u32,
    u: isize,
}
#[inline]
fn side(p: &[u8], from_end: bool) -> Side {
    let n = p.len();
    let mut s = Side { ax: 3, mk: 0, inv1: 0, inv12: 0, u: 0 };
    if n == 0 {
        return s;
    }
    let at = |k: usize| if from_end { p[n - 1 - k] } else { p[k] };
    s.ax = at(0) / 6;
    let mut k = 0;
    let mut size = 0isize;
    while k < n && at(k) / 6 == s.ax {
        s.mk |= 1 << ((at(k) / 3) % 2);
        s.inv1 |= 1 << seq::inv_move(at(k));
        k += 1;
        size += 1;
    }
    s.inv12 = s.inv1;
    s.u = size;
    if k < n {
        let ax2 = at(k) / 6;
        let mut size2 = 0isize;
        while k < n && at(k) / 6 == ax2 {
            s.inv12 |= 1 << seq::inv_move(at(k));
            k += 1;
            size2 += 1;
        }
        s.u = size.max(size2);
    }
    s
}

/// The shortest cancel(pre + A + post) over the sequences A (length <= l) of element e; updates (best_len, best_alg)
/// when something shorter than best_len is found.
///
/// Exactness of the short cuts.  Write t for the number of moves of A that cancel outright against a move of `pre`
/// or `post` (not merges).  A sequence of at least 6 moves that is not swallowed whole gains 2t plus at most one merge
/// per move of the run where the cancelling stops on each side; with t <= 1 on each side that run is one of the two
/// nearest, so the gain is at most 2t + u(pre) + u(post).  To beat best_len a sequence of length len needs a gain of
/// G = pre + len + post - best_len + 1, hence t >= ceil((G - u(pre) - u(post)) / 2).  A sequence swallowed whole has
/// t >= 4.  A first cancel on a side needs a move of A's nearest run to be the inverse of a move of the nearest run
/// there; a second one needs two such moves within the nearest two runs.  Sequences that fail these tests are skipped;
/// every other one is evaluated in full.
#[inline]
pub fn best_at_cut(tab: &Table, e: u32, l: usize, pre: &[u8], post: &[u8], buf: &mut Vec<u8>, best_len: &mut usize, best_alg: &mut u64) -> bool {
    let (sl, sr) = (side(pre, true), side(post, false));
    let base = pre.len() + post.len();
    let mut improved = false;
    let mut a = [0u8; 12];
    for g in tab.groups_of(e) {
        if g.len as usize > l {
            break;
        }
        let li = g.fc == 9 || (g.fc / 3 == sl.ax && ((g.fc % 3 + 1) & sl.mk) != 0);
        let ri = g.lc == 9 || (g.lc / 3 == sr.ax && ((g.lc % 3 + 1) & sr.mk) != 0);
        if !li && !ri {
            // nothing cancels or merges: the result is pre + A + post as it stands
            if base + (g.len as usize) < *best_len {
                *best_len = base + g.len as usize;
                *best_alg = tab.algs[g.a0 as usize];
                improved = true;
            }
            continue;
        }
        let mut tneed = 0isize;
        if *best_len != usize::MAX && g.fc != 9 && g.len >= 6 {
            let need = (base + g.len as usize) as isize - *best_len as isize + 1;
            if need > 0 {
                tneed = (need - sl.u - sr.u + 1).div_euclid(2).clamp(0, 2);
            }
        }
        for ai in g.a0 as usize..g.a1 as usize {
            if tneed > 0 {
                let mk = &tab.masks[ai];
                let (cl1, cr1) = (mk[0] & sl.inv1 != 0, mk[2] & sr.inv1 != 0);
                let ok = if tneed == 1 {
                    cl1 || cr1
                } else {
                    (cl1 && cr1) || (cl1 && (mk[1] & sl.inv12).count_ones() >= 2) || (cr1 && (mk[3] & sr.inv12).count_ones() >= 2)
                };
                if !ok {
                    continue;
                }
            }
            let v = tab.algs[ai];
            let n = seq::unpack(v, &mut a);
            let ev = insert(buf, pre, &a[..n], post, false);
            if (ev.len as usize) < *best_len {
                *best_len = ev.len as usize;
                *best_alg = v;
                improved = true;
            }
        }
    }
    improved
}

/// One insertion that does the whole leftover.
pub fn single(tab: &Table, m: &Model, skel: &[u8], c: &Cubie, l: usize) -> Option<Sol> {
    let n = skel.len();
    let mut g = c.inverse();
    let (mut best_len, mut best_alg, mut best_pos) = (usize::MAX, 0u64, 0usize);
    let mut buf = Vec::with_capacity(n + 16);
    for p in (0..=n).rev() {
        if p < n {
            g = m.conj_move(&g, skel[p] as usize);
        }
        if let Some(e) = tab.find(g.key()) {
            if best_at_cut(tab, e, l, &skel[..p], &skel[p..], &mut buf, &mut best_len, &mut best_alg) {
                best_pos = p;
            }
        }
    }
    if best_len == usize::MAX {
        None
    } else {
        Some(Sol { len: best_len, ins: vec![Ins { pos: best_pos, alg: best_alg }], nested: false })
    }
}

#[derive(Clone, Copy)]
struct E1 {
    len: u16,   // length after this insertion alone
    low: u8,    // skel[..low] is unchanged at the front
    rend: u8,   // the insertion read skel[..rend] at most (n + 1: it ran off the end)
    lstart: i8, // the lowest index of skel it read (-1: it ran off the start)
    bpos: u8,   // skel[bpos..] is unchanged at the end
    pos: u8,
    d: u16,
    alg: u32,
}

pub struct TwoOut {
    pub two: Option<Sol>,   // the minimum; `nested` is set only when every solution of that length is nested
    pub flat: Option<Sol>,  // the minimum without nesting: the second insertion not strictly inside the stretch the first one changed
    pub apart: Option<Sol>, // the minimum over pairs that do not touch (see `two`)
}

/// Two insertions of 3-cycles (of corners when `corner`).
///
/// The first insertion (position i, 3-cycle a) must leave a 3-cycle; with a = Y d Y^-1 that means: d is a 3-cycle with
/// c·d a 3-cycle (`types::splits`).  It gives S1 = S[..low] + M + S[bpos..], where the two outer parts are unchanged
/// pieces of S.  The second insertion goes at any place j of S1:
///   * j <= low: the element needed there is Y_j (d·c)^-1 Y_j^-1, the same as in S.  If the cancelling of the second
///     sequence in S reads only moves before `low`, it does the same thing in S1 and the costs add: these pairs are
///     all covered by a table of the best insertion that reads only S[..t] (`apart`).  The others are tried one by one.
///   * j in the unchanged end: symmetric, element Y_j (c·d)^-1 Y_j^-1.
///   * j inside M: every sequence of the element needed there is tried.
/// So the minimum is exact.
pub fn two(tab: &Table, m: &Model, skel: &[u8], c: &Cubie, corner: bool, l: usize, check: bool, mixed: Option<&[Cubie]>) -> TwoOut {
    let n = skel.len();
    assert!(n <= 250);
    // `mixed` (the list of all 3-cycles of this kind of piece): one of the two insertions is a 3-cycle, the other any
    // element of one of the types; everything below is the same, only the list of first insertions is longer
    let ds = match mixed {
        None => types::splits(c, corner),
        Some(fam) => types::splits_mixed(c, corner, fam),
    };
    let nd = ds.len();
    let none = TwoOut { two: None, flat: None, apart: None };
    if nd == 0 {
        return none;
    }
    let find_d = |x: &Cubie| ds.iter().position(|d| d == x).expect("partner of a split is a split");
    let lp: Vec<usize> = ds.iter().map(|d| find_d(&d.then(c).inverse())).collect();
    let rp: Vec<usize> = ds.iter().map(|d| find_d(&c.then(d).inverse())).collect();
    let w = n + 1;
    let mut chain = vec![SOLVED; nd * w];
    let mut ids = vec![u32::MAX; nd * w];
    for k in 0..nd {
        chain[k * w + n] = ds[k];
        for p in (0..n).rev() {
            chain[k * w + p] = m.conj_move(&chain[k * w + p + 1], skel[p] as usize);
        }
        for p in 0..=n {
            ids[k * w + p] = tab.find(chain[k * w + p].key()).unwrap_or(u32::MAX);
        }
    }
    // every single insertion of every split at every position
    let mut ents: Vec<E1> = Vec::new();
    let mut rng = vec![(0u32, 0u32); nd * w];
    let mut buf = Vec::with_capacity(n + 32);
    let mut a = [0u8; 12];
    for k in 0..nd {
        for p in 0..=n {
            let start = ents.len() as u32;
            let e = ids[k * w + p];
            if e != u32::MAX {
                for g in tab.groups_of(e) {
                    if g.len as usize > l {
                        break;
                    }
                    for ai in g.a0..g.a1 {
                        let na = seq::unpack(tab.algs[ai as usize], &mut a);
                        let ev = insert(&mut buf, &skel[..p], &a[..na], &skel[p..], false);
                        ents.push(E1 {
                            len: ev.len,
                            low: ev.low as u8,
                            rend: (p + ev.r as usize).min(n + 1) as u8,
                            lstart: ev.lstart as i8,
                            bpos: (p + ev.b as usize) as u8,
                            pos: p as u8,
                            d: k as u16,
                            alg: ai,
                        });
                    }
                }
            }
            rng[k * w + p] = (start, ents.len() as u32);
        }
    }
    if ents.is_empty() {
        return none;
    }
    // bp[k][t]: the best insertion of split k that reads only skel[..t]
    const NO: u32 = u32::MAX;
    let mut bp = vec![(u16::MAX, NO); nd * w];
    for (idx, e) in ents.iter().enumerate() {
        if (e.rend as usize) <= n {
            let slot = &mut bp[e.d as usize * w + e.rend as usize];
            if e.len < slot.0 {
                *slot = (e.len, idx as u32);
            }
        }
    }
    for k in 0..nd {
        for t in 1..=n {
            if bp[k * w + t - 1].0 < bp[k * w + t].0 {
                bp[k * w + t] = bp[k * w + t - 1];
            }
        }
    }
    let mut by_rend: Vec<u32> = (0..ents.len() as u32).collect();
    let mut by_lstart: Vec<u32> = by_rend.clone();
    let mut maxrend = vec![0u8; nd * w];
    let mut minlstart = vec![i8::MAX; nd * w];
    for s in 0..nd * w {
        let (x, y) = (rng[s].0 as usize, rng[s].1 as usize);
        if x == y {
            continue;
        }
        by_rend[x..y].sort_unstable_by_key(|&i| std::cmp::Reverse(ents[i as usize].rend));
        by_lstart[x..y].sort_unstable_by_key(|&i| ents[i as usize].lstart);
        maxrend[s] = ents[by_rend[x] as usize].rend;
        minlstart[s] = ents[by_lstart[x] as usize].lstart;
    }

    let mut apart: Option<(usize, u32, u32)> = None;
    for (idx, f) in ents.iter().enumerate() {
        let (l2, e2) = bp[lp[f.d as usize] * w + f.low as usize];
        if e2 != NO {
            let total = f.len as usize + l2 as usize - n;
            if apart.map_or(true, |b| total < b.0) {
                apart = Some((total, idx as u32, e2));
            }
        }
    }
    let sol_apart = apart.map(|(total, f, e2)| {
        let (f, e2) = (ents[f as usize], ents[e2 as usize]);
        Sol { len: total, ins: vec![Ins { pos: f.pos as usize, alg: tab.algs[f.alg as usize] }, Ins { pos: e2.pos as usize, alg: tab.algs[e2.alg as usize] }], nested: false }
    });

    // the pairs that touch
    let mut best_len = apart.map_or(usize::MAX, |b| b.0); // not nested
    let mut best: Option<(Ins, Ins, bool)> = None;
    let mut nest_len = usize::MAX;
    let mut nest: Option<(Ins, Ins, bool)> = None;
    let mut s1: Vec<u8> = Vec::with_capacity(n + 16);
    let cinv_check = |s1: &[u8], j: usize, d: &Cubie, have: u32| {
        // the element needed at place j of s1, from scratch
        let q = m.state(&s1[j..]);
        let g = q.then(&c.then(d).inverse()).then(&q.inverse());
        assert_eq!(tab.find_le(g.key(), l).unwrap_or(u32::MAX), if have != u32::MAX && tab.elems[have as usize].opt as usize <= l { have } else { u32::MAX }, "needed element");
    };
    for f in ents.iter() {
        let (i, k) = (f.pos as usize, f.d as usize);
        let na = seq::unpack(tab.algs[f.alg as usize], &mut a);
        insert(&mut s1, &skel[..i], &a[..na], &skel[i..], true);
        let len1 = s1.len();
        debug_assert_eq!(len1, f.len as usize);
        let (low, bpos) = (f.low as usize, f.bpos as usize);
        let hi = len1 - (n - bpos);
        let mlen = hi - low;
        let (q, rq) = (lp[k], rp[k]);
        let first = Ins { pos: i, alg: tab.algs[f.alg as usize] };
        // second insertion before the changed part, reaching it
        for j in 0..low {
            let s = q * w + j;
            if maxrend[s] as usize <= low {
                continue;
            }
            for &ei in &by_rend[rng[s].0 as usize..rng[s].1 as usize] {
                let e = &ents[ei as usize];
                if e.rend as usize <= low {
                    break;
                }
                let nb = seq::unpack(tab.algs[e.alg as usize], &mut a);
                let ev = insert(&mut buf, &s1[..j], &a[..nb], &s1[j..], false);
                if (ev.len as usize) < best_len {
                    best_len = ev.len as usize;
                    best = Some((first, Ins { pos: j, alg: tab.algs[e.alg as usize] }, false));
                }
            }
            if check {
                cinv_check(&s1, j, &ds[k], ids[s]);
            }
        }
        // second insertion after the changed part, reaching it
        for jp in bpos + 1..=n {
            let s = rq * w + jp;
            if minlstart[s] as isize > bpos as isize {
                continue;
            }
            let j = jp + len1 - n;
            for &ei in &by_lstart[rng[s].0 as usize..rng[s].1 as usize] {
                let e = &ents[ei as usize];
                if e.lstart as isize > bpos as isize {
                    break;
                }
                let nb = seq::unpack(tab.algs[e.alg as usize], &mut a);
                let ev = insert(&mut buf, &s1[..j], &a[..nb], &s1[j..], false);
                if (ev.len as usize) < best_len {
                    best_len = ev.len as usize;
                    best = Some((first, Ins { pos: j, alg: tab.algs[e.alg as usize] }, false));
                }
            }
            if check {
                cinv_check(&s1, j, &ds[k], ids[s]);
            }
        }
        // second insertion at the edges of the changed part and inside it
        let mut g = chain[rq * w + bpos];
        for kk in (0..=mlen).rev() {
            let j = low + kk;
            let e = if kk == mlen && mlen > 0 {
                ids[rq * w + bpos]
            } else if kk == 0 {
                if check && mlen == 0 {
                    assert_eq!(ids[q * w + low], ids[rq * w + bpos]);
                }
                ids[q * w + low]
            } else {
                g = m.conj_move(&g, s1[j] as usize);
                tab.find(g.key()).unwrap_or(u32::MAX)
            };
            if check {
                cinv_check(&s1, j, &ds[k], e);
            }
            if e == u32::MAX {
                continue;
            }
            let mut alg2 = 0u64;
            if kk > 0 && kk < mlen {
                if best_at_cut(tab, e, l, &s1[..j], &s1[j..], &mut buf, &mut nest_len, &mut alg2) {
                    nest = Some((first, Ins { pos: j, alg: alg2 }, true));
                }
            } else if best_at_cut(tab, e, l, &s1[..j], &s1[j..], &mut buf, &mut best_len, &mut alg2) {
                best = Some((first, Ins { pos: j, alg: alg2 }, false));
            }
        }
    }
    let sol_flat = match best {
        Some((x, y, nested)) => Some(Sol { len: best_len, ins: vec![x, y], nested }),
        None => sol_apart.clone(),
    };
    let sol_two = match nest {
        Some((x, y, nested)) if nest_len < best_len => Some(Sol { len: nest_len, ins: vec![x, y], nested }),
        _ => sol_flat.clone(),
    };
    TwoOut { two: sol_two, flat: sol_flat, apart: sol_apart }
}

/// The same minimum by plain enumeration (for checking): every first insertion, then every place and every sequence.
pub fn two_naive(tab: &Table, m: &Model, skel: &[u8], c: &Cubie, corner: bool, l: usize, mixed: bool) -> Option<usize> {
    let n = skel.len();
    let want = if corner { types::T3C } else { types::T3E };
    let kind = |x: &Cubie| types::classify(x).filter(|&t| t != types::T2C2E && types::is_corner(t) == corner);
    let fam: Vec<Cubie> = if mixed {
        // every element of every type of this kind of piece
        (0..types::TYPES.len() - 1).filter(|&t| types::is_corner(t) == corner).flat_map(types::elements).collect()
    } else {
        types::elements(want)
    };
    let z = c.then(&m.state(skel).inverse());
    let mut best: Option<usize> = None;
    for d in fam.iter().filter(|d| {
        let (td, tcd) = (kind(d), kind(&c.then(d)));
        if mixed { td.is_some() && tcd.is_some() && (td == Some(want) || tcd == Some(want)) } else { tcd == Some(want) }
    }) {
        let c1 = c.then(d);
        for i in 0..=n {
            let y = m.state(&skel[i..]);
            let a1 = y.then(d).then(&y.inverse());
            for alg1 in tab.algs_of(a1.key(), l) {
                let whole: Vec<u8> = skel[..i].iter().copied().chain(seq::unpack_vec(alg1)).chain(skel[i..].iter().copied()).collect();
                let s1 = seq::cancel(&whole);
                assert_eq!(z.then(&m.state(&s1)), c1);
                for j in 0..=s1.len() {
                    let q = m.state(&s1[j..]);
                    let g = q.then(&c1.inverse()).then(&q.inverse());
                    for alg2 in tab.algs_of(g.key(), l) {
                        let whole: Vec<u8> = s1[..j].iter().copied().chain(seq::unpack_vec(alg2)).chain(s1[j..].iter().copied()).collect();
                        let fin = seq::cancel(&whole);
                        if best.map_or(true, |b| fin.len() < b) {
                            assert_eq!(z.then(&m.state(&fin)), SOLVED);
                            best = Some(fin.len());
                        }
                    }
                }
            }
        }
    }
    best
}

pub struct Step {
    pub pos: usize,
    pub alg: Vec<u8>,
    pub cancelled: usize,
    pub after: Vec<u8>,
}
/// Carry out the insertions of a solution one after the other.
pub fn replay(skel: &[u8], sol: &Sol) -> Vec<Step> {
    let mut cur = skel.to_vec();
    let mut out = Vec::new();
    for ins in &sol.ins {
        let alg = seq::unpack_vec(ins.alg);
        let whole: Vec<u8> = cur[..ins.pos].iter().chain(&alg).chain(&cur[ins.pos..]).copied().collect();
        let after = seq::cancel(&whole);
        out.push(Step { pos: ins.pos, alg: alg.clone(), cancelled: cur.len() + alg.len() - after.len(), after: after.clone() });
        cur = after;
    }
    out
}
