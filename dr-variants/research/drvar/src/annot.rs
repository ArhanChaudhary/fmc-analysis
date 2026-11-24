//! `drvar metaannot`: everything the annotated example solves of the skeleton/variant meta print about one DR.
//!
//! One JSON object per line:
//!
//!   {"t":"dr", ...}     the DR: subset, quarter turns, goal, optimal leave-slice length
//!   {"t":"skel", ...}   one corner skeleton of a side (`tuple::skeletons_cmd`'s list): quarter turns, L, the skeleton
//!                       moves of each section, one way to write it
//!   {"t":"cls", ...}    one HTR of a side (a class of `Ctx::classes`, the unit the page counts), read against its own
//!                       skeleton by `tuple::read`: route (the skeleton), L, the extra moves of each section, the N of
//!                       the three bounds, the best path + finish, and its members written out
//!
//! Nothing here is a new reading: classes, (L; P, S, T), the bounds and the totals are the ones `tuple::one` writes
//! to the records the page is built from.  What is added is only what a worked example has to show:
//!
//!   * the members of a class as move sequences, with the NISS@1qt case of the HTR state each lands on (corner kind,
//!     F and R edges, which of the two slices is bad, cs, fr), its N under each bound and its finish;
//!   * one spelling of each approach to 2qt.  A class is a set of paths that differ in which of U and D is turned,
//!     so the paths of two HTRs after the same approach may be written with different turns before 2qt.  Every
//!     class after an approach is given by the members that start with one common spelling of it (the one with the
//!     fewest D turns that all of them have);
//!   * the skeleton the inverse reads each solution on (`mirror`): the route of the inverted solution on the other
//!     side.
use crate::core::{rank_perm, St, MOVE_INV};
use crate::meta::{bad_counts, goal_of, hpairs, pairs, qt_count, real_variants, Cls, Ctx, Uni};
use crate::model::*;
use crate::tuple::{load_rules, read, read_solution, Read, Sec};
use std::collections::{BTreeMap, HashMap, HashSet};
use std::fmt::Write as _;

fn corners(s: &St) -> St {
    St { c: s.c, e: St::ID.e, s: St::ID.s }
}

/// The corner cases at the quarter turns of the word `w` from `y`, folded the way `tuple::read` folds them.
fn route_of(sec: &Sec, y: &St, w: &[usize]) -> (usize, u64) {
    let mut s = corners(y);
    let (mut q, mut route) = (0usize, 1u64);
    for &mv in w {
        if is_qt(mv) {
            route = route * 631 + u64::from(sec.bcls[rank_perm(&s.c)]) + 1;
            q += 1;
        }
        s = s.apply_move(mv);
    }
    (q, route)
}

/// (P, S, T) of a reading (`Read::pst`).  A path with one quarter turn (a 1qt DR's own skeleton) has no state with
/// 2 quarter turns left: no approach, no setup, and the extra moves before its quarter turn are the trigger's T.
fn pst(r: &Read) -> (u8, u8, u8) {
    if r.q == 1 {
        (0, 0, r.e[0])
    } else {
        r.pst()
    }
}

/// Moves made up to the state with 2 quarter turns left (0 when the path has only 2).
fn cut2(w: &[u8]) -> usize {
    let q = w.iter().filter(|&&m| is_qt(m as usize)).count();
    if q <= 2 {
        return 0;
    }
    let mut seen = 0;
    for (i, &m) in w.iter().enumerate() {
        if is_qt(m as usize) {
            seen += 1;
            if q - seen == 2 {
                return i + 1;
            }
        }
    }
    unreachable!()
}

/// Which of the F and R slices is bad, by the doc's must-have / must-avoid table (`model::bad_by_rule`, split).
fn bad_flags(kind: u8, fe: u8, re: u8) -> (bool, bool) {
    let (h, d, v) = (0u8, 1u8, 2u8);
    match kind {
        0 => (fe != h, re != h),
        1 => (fe == v, re != d),
        2 => (fe != d, re == v),
        3 => (fe == d, re != v),
        4 => (fe != v, re == d),
        _ => (fe == h, re == h),
    }
}

struct Skel {
    l: usize,
    shape: Vec<usize>,
    ways: usize,
    /// the way to write it that keeps the most pairs: after the first quarter turn, then the second, ...
    form: Vec<usize>,
    /// true pairs in the U and D layers after each quarter turn of `form`
    pq: Vec<u8>,
}

struct Forms {
    first: Vec<Vec<usize>>,
    mid: Vec<Vec<usize>>,
    last: Vec<Vec<usize>>,
}

/// The shapes a skeleton section can have (`tuple::skeletons_cmd`): before the first quarter turn nothing, X2, U2 X2
/// or X2 U2 Y2; between quarter turns nothing, X2 or X2 U2 Y2; after the last nothing, X2, X2 U2 or X2 U2 Y2.
fn forms() -> Forms {
    let side = [6usize, 7, 8, 9];
    let mut xyz: Vec<Vec<usize>> = Vec::new();
    for &a in &side {
        for &b in &side {
            if FACE[a] / 2 != FACE[b] / 2 {
                xyz.push(vec![a, 1, b]);
            }
        }
    }
    let single: Vec<Vec<usize>> = side.iter().map(|&a| vec![a]).collect();
    let mut first: Vec<Vec<usize>> = vec![vec![]];
    first.extend(single.clone());
    first.extend(side.iter().map(|&a| vec![1, a]));
    first.extend(xyz.clone());
    let mut mid: Vec<Vec<usize>> = vec![vec![]];
    mid.extend(single.clone());
    mid.extend(xyz.clone());
    let mut last: Vec<Vec<usize>> = vec![vec![]];
    last.extend(single);
    last.extend(side.iter().map(|&a| vec![a, 1]));
    last.extend(xyz);
    Forms { first, mid, last }
}

struct Walk<'a> {
    md: &'a Model,
    sec: &'a Sec,
    f: &'a Forms,
    /// the state the skeletons are for (the walk itself only follows the corners)
    y: St,
    q: usize,
    goal: usize,
    /// quarter turns on the D layer too.  With 2 or more quarter turns to make, every route has a skeleton written
    /// with U turns only; a DR with one (4a1) can need its quarter turn on D (`D' L2 U2`), also as the first of 3
    both: bool,
    found: BTreeMap<(usize, u64), Skel>,
}
impl Walk<'_> {
    fn go(&mut self, s: St, w: &mut Vec<usize>, shape: &mut Vec<usize>, done: usize, route: u64) {
        let (md, sec, forms) = (self.md, self.sec, self.f);
        if done == self.q {
            for f in &forms.last {
                if w.len() + f.len() > self.goal {
                    continue;
                }
                let t = f.iter().fold(s, |t, &mv| t.apply_move(mv));
                if !sec.solved[rank_perm(&t.c)] {
                    continue;
                }
                let mut full = w.clone();
                full.extend(f);
                // a listed shape is a skeleton only if no section can be shortened
                let (l, ex) = read_solution(sec, &full);
                if ex.iter().any(|&e| e > 0) {
                    continue;
                }
                assert_eq!(l as usize, full.len());
                let mut sh = shape.clone();
                sh.push(f.len());
                let mut pq = Vec::new();
                let mut t = self.y;
                for &mv in &full {
                    t = t.apply_move(mv);
                    if is_qt(mv) {
                        pq.push(pairs(&t));
                    }
                }
                let e = self.found.entry((self.q, route)).or_insert(Skel { l: full.len(), shape: sh.clone(), ways: 0, form: full.clone(), pq: pq.clone() });
                assert_eq!(e.l, full.len(), "one route, one length");
                e.ways += 1;
                if pq > e.pq {
                    (e.shape, e.form, e.pq) = (sh, full.clone(), pq);
                }
            }
            return;
        }
        let list = if done == 0 { &forms.first } else { &forms.mid };
        for f in list {
            let t = f.iter().fold(s, |t, &mv| t.apply_move(mv));
            let c = rank_perm(&t.c);
            let left = self.q - done;
            let need = (0..6).map(|k| md.rem[k][left][c].saturating_add(LC[k])).min().unwrap() as usize;
            if w.len() + f.len() + need > self.goal {
                continue;
            }
            let r2 = route * 631 + u64::from(sec.bcls[c]) + 1;
            for qt in if self.both { &[0usize, 2, 3, 5][..] } else { &[0usize, 2][..] } {
                let qt = *qt;
                w.extend(f);
                w.push(qt);
                shape.push(f.len());
                self.go(t.apply_move(qt), w, shape, done + 1, r2);
                shape.pop();
                w.truncate(w.len() - f.len() - 1);
            }
        }
    }
}

fn skeletons(md: &Model, sec: &Sec, f: &Forms, y: &St, qs: &[usize], goal: usize) -> BTreeMap<(usize, u64), Skel> {
    let mut found = BTreeMap::new();
    let both = qs.contains(&1);
    for &q in qs {
        if !(1..=6).contains(&q) {
            continue;
        }
        let mut wk = Walk { md, sec, f, y: *y, q, goal, both, found };
        wk.go(corners(y), &mut Vec::new(), &mut Vec::new(), 0, 1);
        found = wk.found;
    }
    found
}

/// A turn of both layers together, U D' (the centres and the E slice left alone), `j` times.
fn turned(s: &St, j: usize) -> St {
    (0..j).fold(*s, |t, _| t.apply_move(0).apply_move(5))
}

/// What a turn of both layers does to the names of the side moves: names[j][s] = t with (U D')^j s = t (U D')^j on
/// the corners and the U/D-layer edges (U and D moves keep their names).
fn turn_names() -> [[usize; 10]; 4] {
    let mut names = [[0usize; 10]; 4];
    for (j, row) in names.iter_mut().enumerate() {
        let g = turned(&St::ID, j);
        for (s, slot) in row.iter_mut().enumerate() {
            if s < 6 {
                *slot = s;
                continue;
            }
            let lhs = g.apply_move(s);
            let hits: Vec<usize> = (6..10)
                .filter(|&t| {
                    let r = turned(&St::ID.apply_move(t), j);
                    r.c == lhs.c && r.e == lhs.e
                })
                .collect();
            assert_eq!(hits.len(), 1, "one name for a side move after a turn of both layers");
            *slot = hits[0];
        }
    }
    names
}

/// The path `w` from `y` the way a solver turns it.  A U turn and the same D turn differ by a turn of both layers,
/// which a leave-slice solution does not see, so each U/D move is written on the face that leaves fewer bad corners
/// (2 rather than 6, 0 rather than 8) and, with 4 bad corners, fewer bad edges (0 or 2 rather than 8 or 6); U when
/// that does not tell them apart (a half turn, or 4 bad corners and 4 bad edges).  The side moves that follow are
/// renamed to match, and commuting side moves are put in one order.  Returns the moves and how many turns of both
/// layers the state they reach is ahead of the one `w` reaches.
fn human(names: &[[usize; 10]; 4], y: &St, w: &[usize]) -> (Vec<usize>, usize) {
    let (mut s, mut sw, mut j) = (*y, *y, 0usize);
    let mut h: Vec<usize> = Vec::with_capacity(w.len());
    for &mv in w {
        sw = sw.apply_move(mv);
        if mv >= 6 {
            let t = names[(4 - j) % 4][mv];
            h.push(t);
            s = s.apply_move(t);
        } else {
            let (face, k) = (FACE[mv], AMT[mv]);
            let (u, d) = (move_of(0, k), move_of(1, k));
            let pick = match h.last().map(|&m| FACE[m]) {
                Some(0) => d,
                Some(1) => u,
                _ => {
                    if bad_counts(&s.apply_move(d)) < bad_counts(&s.apply_move(u)) {
                        d
                    } else {
                        u
                    }
                }
            };
            if FACE[pick] != face {
                j = if face == 0 { (j + 4 - k) % 4 } else { (j + k) % 4 };
            }
            h.push(pick);
            s = s.apply_move(pick);
        }
        let t = turned(&sw, j);
        assert!(s.c == t.c && s.e == t.e, "a respelling follows its path up to a turn of both layers");
    }
    for i in 0..h.len().saturating_sub(1) {
        let (a, b) = (FACE[h[i]], FACE[h[i + 1]]);
        if a >= 2 && a / 2 == b / 2 && a > b {
            h.swap(i, i + 1);
        }
    }
    (h, j)
}

/// The shortest leave-slice finish of the state `s`, where the U and D layers only have to be solved up to a turn
/// of both: (turns of both layers the solved state is off by, the HTR state the finish is read from, the moves).
/// None when `s` is no HTR state under any turn.
fn finish_up_to_turn(md: &Model, names: &[[usize; 10]; 4], s: &St) -> Option<(usize, u32, Vec<usize>)> {
    let (i, z) = (0..4).filter_map(|i| md.hg.get(&turned(s, i)).map(|z| (i, z))).min_by_key(|&(i, z)| (md.fin[z as usize], i))?;
    let f: Vec<usize> = crate::crisp::ls_finish(md, z).iter().map(|&mv| names[i][mv]).collect();
    let end = turned(&f.iter().fold(*s, |t, &mv| t.apply_move(mv)), i);
    assert!(end.c == St::ID.c && end.e == St::ID.e, "the renamed finish solves both layers up to the turn");
    Some((i, z, f))
}

/// Pairs right after the last insertion of the path `w` from `y`, read as `r`: (true pairs, HTR-equivalent pairs) in
/// the U and D layers of the state just before the quarter turn that closes the last section with extra moves, or
/// just before the last quarter turn when no section has any.  A quarter turn of a layer keeps both counts, and so
/// does writing a U turn as a D turn, so every spelling of a variant has the same count.
pub fn pairs_after_insertion(y: &St, w: &[usize], r: &Read) -> (u8, u8) {
    let q = r.q as usize;
    let last = (0..q).rev().find(|&j| r.e[j] > 0).unwrap_or(q - 1);
    let (mut s, mut qi) = (*y, 0usize);
    for &mv in w {
        if is_qt(mv) {
            if qi == last {
                return (pairs(&s), hpairs(&s));
            }
            qi += 1;
        }
        s = s.apply_move(mv);
    }
    unreachable!("a path has as many quarter turns as its reading")
}

fn wvec(a: &[u8; 16], n: u8) -> Vec<usize> {
    a[..n as usize].iter().map(|&m| m as usize).collect()
}
fn nums<T: std::fmt::Display>(v: &[T]) -> String {
    v.iter().map(T::to_string).collect::<Vec<_>>().join(",")
}

/// One side to list: the DR itself, or the DR left of it after a quarter turn made on the other side.
struct Pass<'a> {
    side: &'a str,
    /// line types of its skeletons and of its HTRs
    skel: &'a str,
    cls: &'a str,
    y: St,
    /// the other side's state, to name the skeleton the inverse reads each solution on (None after a premove)
    other: Option<St>,
    /// quarter turns of the skeletons to list
    qs: Vec<usize>,
    goal: usize,
    /// for the skeletons that end with their last quarter turn: the two states after that turn is made on the
    /// other side (either way), to name the skeleton that is left
    red: Option<[St; 2]>,
    /// after a premove: which way it was turned (0, 1)
    dir: Option<usize>,
    /// write the members of each class out
    members: bool,
}

/// Fewest half turns that solve the U and D layers of `s` against each other, up to a turn of both.
fn fin_turn(md: &Model, s: &St) -> Option<u8> {
    (0..4).filter_map(|i| md.hg.get(&turned(s, i))).map(|z| md.fin[z as usize]).min()
}

fn side_lines(cx: &Ctx, sec: &Sec, fm: &Forms, names: &[[usize; 10]; 4], out: &mut String, p: &Pass, pmax: u8, cap: u8) {
    let md = cx.md;
    let (side, y, goal) = (p.side, p.y, p.goal);
    let dirs = p.dir.map_or(String::new(), |d| format!(",\"dir\":{d}"));
    for ((q, route), sk) in &skeletons(md, sec, fm, &y, &p.qs, goal) {
        // a skeleton of 3 or more quarter turns that ends with the last one (HH corners): what is left of it
        // when that quarter turn is made on the other side, as the routes of the two DRs that leaves
        let mut left = String::new();
        if let Some(ry) = &p.red {
            if *q >= 3 && *sk.shape.last().unwrap() == 0 {
                let cut = sk.form.iter().enumerate().filter(|(_, &mv)| is_qt(mv)).nth(q - 2).unwrap().0 + 1;
                let r: Vec<String> = ry.iter().map(|t| format!("\"{:x}\"", route_of(sec, t, &sk.form[..cut]).1)).collect();
                // the skeleton without its last quarter turn, as a solver turns it after the premove (either way),
                // and which way that last quarter turn goes: 0 = the way `dir` 0 ends, 1 = the other
                let (&end, body) = sk.form.split_last().unwrap();
                assert!(is_qt(end), "a skeleton with HH corners ends with its last quarter turn");
                let f: Vec<String> = ry.iter().map(|t| format!("\"{}\"", wname(&human(names, t, body).0))).collect();
                write!(left, ",\"rroute\":[{}],\"rform\":[{}],\"rdir\":{}", r.join(","), f.join(","), usize::from(AMT[end] == 1)).unwrap();
            }
        }
        writeln!(
            out,
            "{{\"t\":\"{}\",\"side\":\"{side}\"{dirs},\"q\":{q},\"route\":\"{route:x}\",\"L\":{},\"shape\":[{}],\"ways\":{},\"pq\":[{}],\"form\":\"{}\"{left}}}",
            p.skel,
            sk.l,
            nums(&sk.shape),
            sk.ways,
            nums(&sk.pq),
            wname(&human(names, &y, &sk.form).0)
        )
        .unwrap();
    }
    let uni = Uni { goal, cap_any: 0, qmax: p.qs.iter().copied().max().unwrap().min(6) };
    let cl = cx.classes(&y, &uni);
    let mut keys: Vec<u64> = cl.keys().copied().collect();
    if p.dir.is_some() {
        // after a premove the DR also has paths with one quarter turn, which are no skeleton
        keys.retain(|k| p.qs.contains(&(cl[k].q as usize)));
    }
    keys.sort();
    // the reading of every class (its shortest member), and the classes whose members are gone through
    let reads: HashMap<u64, (Read, u64)> = keys
        .iter()
        .map(|k| {
            let c: &Cls = &cl[k];
            let w = wvec(&c.w, c.wl);
            let r = read(sec, &y, &w, &md.hg.st[c.z as usize]);
            (*k, (r, cx.im.key(&w[..r.a2 as usize], false)))
        })
        .collect();
    let want: HashSet<u64> = keys
        .iter()
        .copied()
        .filter(|k| {
            let (p, s, t) = pst(&reads[k].0);
            p <= pmax && p + s + t <= cap
        })
        .collect();
    let mut mem: HashMap<u64, Vec<(Vec<u8>, u32)>> = HashMap::new();
    real_variants(md, &y, &uni, &mut |w: &[usize], _q: usize, zi: u32| {
        let key = cx.im.key(w, true);
        if want.contains(&key) {
            mem.entry(key).or_default().push((w.iter().map(|&mv| mv as u8).collect(), zi));
        }
    });
    // one spelling per approach to 2qt: the prefixes every class after it has a member with
    let mut spell: HashMap<u64, HashMap<Vec<u8>, usize>> = HashMap::new();
    let mut group: HashMap<u64, usize> = HashMap::new();
    let own = |k: &u64| -> HashSet<Vec<u8>> {
        let (r, pre2) = &reads[k];
        mem[k]
            .iter()
            .filter(|(w, _)| {
                let a = cut2(w);
                a == r.a2 as usize && cx.im.key(&w[..a].iter().map(|&mv| mv as usize).collect::<Vec<_>>(), false) == *pre2
            })
            .map(|(w, _)| w[..r.a2 as usize].to_vec())
            .collect()
    };
    for k in &keys {
        if !want.contains(k) {
            continue;
        }
        let pre2 = reads[k].1;
        *group.entry(pre2).or_default() += 1;
        for p in own(k) {
            *spell.entry(pre2).or_default().entry(p).or_default() += 1;
        }
    }
    let rep: HashMap<u64, Vec<u8>> = spell
        .iter()
        .map(|(pre2, cnt)| {
            let best = cnt
                .iter()
                .min_by_key(|(p, &n)| (group[pre2] - n, p.iter().filter(|&&mv| (3..6).contains(&mv)).count(), (*p).clone()))
                .unwrap();
            (*pre2, best.0.clone())
        })
        .collect();
    for k in &keys {
        let c: &Cls = &cl[k];
        let (r, pre2) = &reads[k];
        let kind = md.cases[md.hcase[c.z as usize] as usize].kind as usize;
        let q = r.q as usize;
        let shape: Vec<u32> = (0..q).map(|i| (r.shape >> (3 * i)) & 7).collect();
        let nb: Vec<u8> = c.lbx.iter().map(|&b| b - c.wl - r.lc).collect();
        // the skeleton the inverse reads this HTR's solution on (its shortest member and that member's finish)
        let mirror = p.other.map_or(String::new(), |other| {
            let mut full = wvec(&c.w, c.wl);
            full.extend(crate::crisp::ls_finish(md, c.z));
            let inv: Vec<usize> = full.iter().rev().map(|&mv| MOVE_INV[mv]).collect();
            let (mq, mroute) = route_of(sec, &other, &inv);
            assert_eq!(mq, q);
            format!("{mroute:x}")
        });
        let (pr, hpr) = pairs_after_insertion(&y, &wvec(&c.w, c.wl), r);
        write!(
            out,
            "{{\"t\":\"{}\",\"side\":\"{side}\"{dirs},\"key\":\"{k:x}\",\"route\":\"{:x}\",\"mirror\":\"{mirror}\",\"q\":{q},\"kind\":\"{}\",\"L\":{},\"lc\":{},\"e\":[{}],\"shape\":[{}],\"a2\":{},\"wl\":{},\"total\":{},\"nb\":[{}],\"pairs\":{pr},\"hpairs\":{hpr},\"pre2\":\"{pre2:x}\"",
            p.cls,
            r.route,
            KIND_NAME[kind],
            r.l,
            r.lc,
            nums(&r.e[..q]),
            nums(&shape),
            r.a2,
            c.wl,
            c.total,
            nums(&nb)
        )
        .unwrap();
        if want.contains(k) {
            let rp = &rep[pre2];
            let mut list: Vec<&(Vec<u8>, u32)> = mem[k].iter().filter(|(w, _)| w.len() >= rp.len() && w[..rp.len()] == rp[..] && cut2(w) == rp.len()).collect();
            let common = !list.is_empty();
            let mine = own(k);
            if !common {
                // no member starts with the approach's common spelling: fall back to this class's own
                list = mem[k].iter().filter(|(w, _)| mine.contains(&w[..(r.a2 as usize).min(w.len())])).collect();
            }
            list.sort_by_key(|(w, zi)| (w.len(), md.fin[*zi as usize], w.clone()));
            // the moves to print: a member that reads like its class, written the way a solver turns it, with
            // its finish up to a turn of both layers.  Within goal: the member with the best total; otherwise
            // a shortest one.
            let cand: Vec<(u8, Vec<usize>)> = mem[k]
                .iter()
                .filter(|(w, _)| w.len() >= r.a2 as usize && mine.contains(&w[..r.a2 as usize]))
                .map(|(w, zi)| {
                    let wu: Vec<usize> = w.iter().map(|&mv| mv as usize).collect();
                    (w.len() as u8 + fin_turn(md, &md.hg.st[*zi as usize]).unwrap(), wu)
                })
                .collect();
            let within = cand.iter().map(|t| t.0).min().expect("a class has a member that reads like it") as usize <= goal;
            let ((_, _, htot, h), hw) = cand
                .into_iter()
                .filter(|(_, wu)| within || wu.len() == c.wl as usize)
                .map(|(tot, wu)| ((if within { tot } else { 0 }, wu.len(), tot, human(names, &y, &wu).0), wu))
                .min()
                .unwrap();
            let end = h.iter().fold(y, |t, &mv| t.apply_move(mv));
            let (hrot, hz, hfin) = finish_up_to_turn(md, names, &end).expect("a respelled path ends on HTR up to a turn of both layers");
            assert_eq!(h.len() + hfin.len(), htot as usize, "the printed finish is the member's best up to a turn");
            let hr = read(sec, &y, &hw, &md.hg.st[md.hg.get(&hw.iter().fold(y, |t, &mv| t.apply_move(mv))).unwrap() as usize]);
            let hcs = &md.cases[md.hcase[hz as usize] as usize];
            let (hbf, hbr) = bad_flags(hcs.kind, hcs.fe, hcs.re);
            // where the last insertion ends: the quarter turn that closes the last section with extra moves
            let hq = hr.q as usize;
            let lastsec = (0..hq).rev().find(|&j| hr.e[j] > 0).unwrap_or(hq - 1);
            let hcut = h.iter().enumerate().filter(|(_, &mv)| is_qt(mv)).nth(lastsec).unwrap().0;
            write!(
                out,
                ",\"h\":\"{}\",\"hfin\":\"{}\",\"htot\":{htot},\"hrot\":{hrot},\"hcut\":{hcut},\"ha2\":{},\"hL\":{},\"he\":[{}],\"hkind\":\"{}\",\"hfe\":\"{}\",\"hre\":\"{}\",\"hbf\":{hbf},\"hbr\":{hbr},\"hcsp\":{},\"hfr\":{},\"hn\":[{}]",
                wname(&h),
                wname(&hfin),
                hr.a2,
                hr.l,
                nums(&hr.e[..hq]),
                KIND_NAME[hcs.kind as usize],
                ET_NAME[hcs.fe as usize],
                ET_NAME[hcs.re as usize],
                hcs.cs,
                hcs.fr,
                nums(&cx.xpen[md.hcase[hz as usize] as usize])
            )
            .unwrap();
            if within {
                // the whole printed solution, read against its own skeleton: L, then the extra moves of every section
                let mut full = h.clone();
                full.extend(&hfin);
                let (l, ex) = read_solution(sec, &full);
                write!(out, ",\"hread\":[{l},{}]", nums(&ex)).unwrap();
            }
            write!(out, ",\"approach\":\"{}\",\"common\":{common}", wname(&rp.iter().map(|&mv| mv as usize).collect::<Vec<_>>())).unwrap();
            if p.members {
                out.push_str(",\"members\":[");
                for (i, (w, zi)) in list.iter().enumerate() {
                    let wu: Vec<usize> = w.iter().map(|&mv| mv as usize).collect();
                    let cs = &md.cases[md.hcase[*zi as usize] as usize];
                    let (bf, br) = bad_flags(cs.kind, cs.fe, cs.re);
                    assert_eq!(u8::from(bf) + u8::from(br), cs.bad());
                    let mr = read(sec, &y, &wu, &md.hg.st[*zi as usize]);
                    let mq = mr.q as usize;
                    write!(
                        out,
                        "{}{{\"w\":\"{}\",\"len\":{},\"fin\":{},\"finish\":\"{}\",\"q\":{mq},\"L\":{},\"e\":[{}],\"route\":\"{:x}\",\"kind\":\"{}\",\"fe\":\"{}\",\"re\":\"{}\",\"bf\":{bf},\"br\":{br},\"cs\":{},\"fr\":{},\"n\":[{}]}}",
                        if i > 0 { "," } else { "" },
                        wname(&wu),
                        w.len(),
                        md.fin[*zi as usize],
                        wname(&crate::crisp::ls_finish(md, *zi)),
                        mr.l,
                        nums(&mr.e[..mq]),
                        mr.route,
                        KIND_NAME[cs.kind as usize],
                        ET_NAME[cs.fe as usize],
                        ET_NAME[cs.re as usize],
                        cs.cs,
                        cs.fr,
                        nums(&cx.xpen[md.hcase[*zi as usize] as usize])
                    )
                    .unwrap();
                }
                out.push(']');
            }
        }
        out.push_str("}\n");
    }
}

/// The JSON lines of one DR.  `pmax`, `cap`: members are written out for the classes with P <= pmax and
/// P+S+T <= cap (the fixed part of the meta); the other classes get their line without members.
///
/// After the two sides come the lines of the premove route ("rdr", "rskel", "rcls"), for the skeletons of 3 or more
/// quarter turns that end with their last one (HH corners).  A solver does not go through such a skeleton as it
/// stands: the last quarter turn is made first on the other side, and what is left on this side is a DR with one
/// quarter turn fewer, one move closer to the goal.  That turn can go either way (the two differ by a U2 before
/// it), so the DR that is left is listed for both, `dir` 0 and 1, with the same paths; a reader takes the better
/// of the two for each path.
fn annotate(cx: &Ctx, sec: &Sec, fm: &Forms, scr: &str, x: &St, mwant: Option<usize>, gwant: Option<usize>, pmax: u8, cap: u8) -> String {
    let md = cx.md;
    let m = mwant.unwrap_or_else(|| qt_count(md, x));
    let goal = gwant.unwrap_or_else(|| goal_of(m));
    let names = turn_names();
    let mut out = String::new();
    writeln!(
        out,
        "{{\"t\":\"dr\",\"scramble\":\"{scr}\",\"subset\":\"{}\",\"qt\":{},\"m\":{m},\"goal\":{goal},\"lsopt\":{},\"lsopt_turn\":{},\"pmax\":{pmax},\"cap\":{cap}}}",
        md.subset(x),
        qt_count(md, x),
        md.lsopt(x),
        (0..4).map(|i| md.lsopt(&turned(x, i))).min().unwrap()
    )
    .unwrap();
    let sides = [("N", *x, x.inv()), ("I", x.inv(), *x)];
    // the quarter turn a solver makes first on the other side (U or D by `human`), and this side after it: the
    // premove p on the other side is p' at the end of this side's solution s = s' p', so y s' = p and what is left
    // to solve is p' y (dir 0), or p y when the turn goes the other way (dir 1)
    let left: Vec<(usize, [St; 2])> = sides
        .iter()
        .map(|(_, y, other)| {
            let pm = human(&names, other, &[0]).0[0];
            (pm, [word(&[MOVE_INV[pm]]).mul(*y), word(&[pm]).mul(*y)])
        })
        .collect();
    for (i, (side, y, other)) in sides.iter().enumerate() {
        let p = Pass { side, skel: "skel", cls: "cls", y: *y, other: Some(*other), qs: vec![m, m + 2], goal, red: Some(left[i].1), dir: None, members: true };
        side_lines(cx, sec, fm, &names, &mut out, &p, pmax, cap);
    }
    let qs: Vec<usize> = [m.wrapping_sub(1), m + 1].into_iter().filter(|q| (2..=6).contains(q)).collect();
    if !qs.is_empty() {
        for (i, (side, _, _)) in sides.iter().enumerate() {
            let (pm, ry) = left[i];
            for (d, y) in ry.iter().enumerate() {
                // dir 0: the premove is `pm` on the other side and this side's solution ends with its inverse
                let (pre, last) = if d == 0 { (pm, MOVE_INV[pm]) } else { (MOVE_INV[pm], pm) };
                writeln!(
                    out,
                    "{{\"t\":\"rdr\",\"side\":\"{side}\",\"dir\":{d},\"pre\":\"{}\",\"last\":\"{}\",\"qt\":{},\"goal\":{}}}",
                    wname(&[pre]),
                    wname(&[last]),
                    qt_count(md, y),
                    goal - 1
                )
                .unwrap();
                let p = Pass { side, skel: "rskel", cls: "rcls", y: *y, other: None, qs: qs.clone(), goal: goal - 1, red: None, dir: Some(d), members: false };
                side_lines(cx, sec, fm, &names, &mut out, &p, pmax, cap);
            }
        }
    }
    out
}

/// drvar metaannot RULES "SCRAMBLE" [M] [PMAX] [CAP] [GOAL]     one DR, to standard output
/// drvar metaannot RULES @LIST OUTDIR [PMAX] [CAP]              LIST: one `ID<tab>SCRAMBLE[<tab>M[<tab>GOAL]]` per line
///                                                              -> OUTDIR/ID.jsonl
/// SCRAMBLE in DR moves; M overrides the DR's quarter turns (a 0c0 DR read as a 2qt one, goal 12), GOAL the goal
/// that goes with them (10 + M; a 4a1 DR is given 12).  `-` for M or GOAL: no override.
pub fn run(md: &Model, args: &[String]) {
    let mut cx = Ctx::new(md);
    load_rules(&mut cx, &args[0]);
    let sec = Sec::new();
    let fm = forms();
    let state = |scr: &str| word(&crate::core::parse_moves(scr.as_bytes(), 64).unwrap_or_else(|| fatal!("not DR moves: {scr}")));
    let num = |i: usize, d: u8| args.get(i).map_or(d, |a| a.parse().unwrap_or_else(|_| fatal!("not a number: {a}")));
    if let Some(list) = args[1].strip_prefix('@') {
        let dir = &args[2];
        let (pmax, cap) = (num(3, 1), num(4, 5));
        let txt = std::fs::read_to_string(list).unwrap_or_else(|e| fatal!("{list}: {e}"));
        for line in txt.lines().filter(|l| !l.trim().is_empty()) {
            let f: Vec<&str> = line.split('\t').collect();
            let mwant = f.get(2).and_then(|v| v.trim().parse().ok());
            let gwant = f.get(3).and_then(|v| v.trim().parse().ok());
            let t0 = std::time::Instant::now();
            let s = annotate(&cx, &sec, &fm, f[1].trim(), &state(f[1].trim()), mwant, gwant, pmax, cap);
            let path = format!("{dir}/{}.jsonl", f[0].trim());
            std::fs::write(&path, s).unwrap_or_else(|e| fatal!("{path}: {e}"));
            eprintln!("{path}  {:.1}s", t0.elapsed().as_secs_f64());
        }
    } else {
        let mwant = args.get(2).and_then(|v| v.parse().ok());
        let gwant = args.get(5).and_then(|v| v.parse().ok());
        print!("{}", annotate(&cx, &sec, &fm, &args[1], &state(&args[1]), mwant, gwant, num(3, 1), num(4, 5)));
    }
}

/// drvar metapairs N SEED M OUT : for the HTRs of `metatuple N SEED M`, in the order of its records, 4 bytes each:
/// true pairs and HTR-equivalent pairs right after the last insertion (`pairs_after_insertion` on the class's
/// shortest member, the one the record's (L; P, S, T) is read on), then that member's length and the class's best
/// total, which a reader checks against the record to be sure the two files line up.
pub fn run_pairs(md: &Model, n: usize, seed: u64, mwant: usize, out: &str) {
    use rayon::prelude::*;
    use std::io::Write;
    let cx = Ctx::new(md);
    let sec = Sec::new();
    let mut rng = crate::Rng(seed);
    let mut xs = Vec::new();
    while xs.len() < n {
        let x = crate::random_dr(md, &mut rng);
        if qt_count(md, &x) == mwant {
            xs.push(x);
        }
    }
    let goal = goal_of(mwant);
    let qmax = (mwant + 2).min(6);
    let mut fb = std::io::BufWriter::new(std::fs::File::create(out).unwrap());
    let t0 = std::time::Instant::now();
    let mut tot = 0u64;
    for (b, chunk) in xs.chunks(64).enumerate() {
        let res: Vec<Vec<u8>> = chunk
            .par_iter()
            .map(|x| {
                let mut o = Vec::new();
                for y in [*x, x.inv()] {
                    let cl = cx.classes(&y, &Uni { goal, cap_any: 0, qmax });
                    let mut keys: Vec<&u64> = cl.keys().collect();
                    keys.sort();
                    for k in keys {
                        let c: &Cls = &cl[k];
                        let w = wvec(&c.w, c.wl);
                        let r = read(&sec, &y, &w, &md.hg.st[c.z as usize]);
                        let (p, h) = pairs_after_insertion(&y, &w, &r);
                        o.extend([p, h, c.wl, c.total]);
                    }
                }
                o
            })
            .collect();
        for o in res {
            tot += o.len() as u64 / 4;
            fb.write_all(&o).unwrap();
        }
        eprintln!("{} / {n}  {:.0}s", (b * 64 + chunk.len()).min(n), t0.elapsed().as_secs_f64());
    }
    println!("HTRs\t{tot}");
}
