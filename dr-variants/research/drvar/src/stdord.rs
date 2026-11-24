//! The standard meta as a list of HTRs to finish: every HTR within a cap on the moves to HTR, whether or not its
//! finish fits the goal, so that the two metas can be compared at the same number of HTRs and by the order they
//! take them in.  (`stdcmp` only has the HTRs with a within-goal finish, which is enough for reach.)
//!
//! One HTR is a class of paths, as on the skeleton/variant side (`Ctx::classes`): the D-free image of the path, with
//! the direction of its last quarter turn folded, and the best path + finish over the members.  A path counts when
//! its moves plus the corner moves left at the HTR fit the goal, as there, and stops at the first HTR it comes to.
//!
//! The ways to an HTR are those of `stdcmp`: on normal, on inverse, and with one NISS after a start of one to three
//! moves (a quarter turn; a side half turn and a quarter turn; a U-layer move, a side half turn and a quarter
//! turn).  A start and the path after it are one class however their U-layer moves are spelled (U or D), and the
//! direction of the start's quarter turn is folded as well: the two left-over states are a U2 apart, the same paths
//! reach HTR from both, and the HTR counts once with the better of the two finishes (as for the premove pass).  Every
//! spelling is run, so the best finish is the best over all of them.  The starts on the U layer alone give the same
//! HTRs up to a few near the goal (`STDORD_CHECK=1` checks it), but not always the best finish: with one quarter
//! turn in the path, the HTR state that is a half turn of the D layer away is only reached from a start on the D
//! layer, and it can have a shorter finish or fewer corner moves left.
use crate::core::{rank_perm, St};
use crate::meta::{goal_of, htr_like, pairs, qt_count, Ctx};
use crate::model::*;
use crate::tuple::{read_any, Sec};
use std::collections::HashMap;

/// One HTR of the standard meta.
#[derive(Clone, Copy)]
pub struct Rec {
    pub dr: u32,
    /// 0 normal, 1 inverse, 2 a start on normal and the rest on inverse, 3 a start on inverse and the rest on normal
    pub view: u8,
    /// moves before the NISS (0 = none)
    pub lev: u8,
    /// which start (0 = none)
    pub sid: u8,
    /// moves to HTR, the start included (the shortest member's)
    pub moves: u8,
    /// best moves + finish over the members
    pub total: u8,
    /// corner/edge pairs in the U and D layers at the HTR
    pub pairs: u8,
    /// quarter turns, the start's included
    pub q: u8,
    /// corner moves left at the HTR
    pub lc: u8,
    /// the path read on its own skeleton (`tuple::read_any`; after a start, the skeleton of what is left): L, the
    /// start's moves counted as a premove is; P, S, T; the pairs right after the last insertion; the corner cases at
    /// the quarter turns.  Of the shortest members, the one with the shortest skeleton.
    pub l: u8,
    pub p: u8,
    pub s: u8,
    pub t: u8,
    pub ipairs: u8,
    pub route: u64,
    /// the linear skeleton this HTR belongs to: the whole solution (the path, a finish, the start undone) read on
    /// the side the path is on, its length and its corner cases.  On normal and inverse these are `l` and `route`.
    pub ll: u8,
    pub lroute: u64,
    /// which spelling of the start the corner cases were read after (not written): the corner cases at the quarter
    /// turns depend on it, so every HTR takes them from the first spelling it has, in one fixed order
    pub aord: u32,
}
impl Rec {
    pub fn bytes(&self) -> [u8; 40] {
        let mut b = [0u8; 40];
        b[..4].copy_from_slice(&self.dr.to_le_bytes());
        b[4..18].copy_from_slice(&[self.view, self.lev, self.sid, self.moves, self.total, self.pairs, self.q, self.lc, self.l, self.p, self.s, self.t, self.ipairs, self.ll]);
        b[24..32].copy_from_slice(&self.route.to_le_bytes());
        b[32..].copy_from_slice(&self.lroute.to_le_bytes());
        b
    }
}

/// Every path from `y` of at most `maxlen` moves that ends with a quarter turn on an HTR state, comes through no
/// HTR before, and has moves + corner moves left within `glen`: f(path, HTR state index).
fn arrivals<F: FnMut(&[usize], u32)>(md: &Model, y: &St, glen: usize, maxlen: usize, f: &mut F) {
    fn dfs<F: FnMut(&[usize], u32)>(md: &Model, s: St, w: &mut Vec<usize>, lf: usize, glen: usize, maxlen: usize, f: &mut F) {
        if let Some(&last) = w.last() {
            if is_qt(last) {
                if let Some(zi) = md.hg.get(&s) {
                    let kind = md.cases[md.hcase[zi as usize] as usize].kind as usize;
                    if w.len() + LC[kind] as usize <= glen {
                        f(w, zi);
                    }
                }
                if htr_like(md, &s) {
                    return;
                }
            }
        }
        if w.len() >= maxlen {
            return;
        }
        for mv in 0..10 {
            if !allowed(lf, mv) {
                continue;
            }
            let s2 = s.apply_move(mv);
            if w.len() + 1 + md.htrd(&s2) as usize > maxlen {
                continue;
            }
            w.push(mv);
            dfs(md, s2, w, FACE[mv], glen, maxlen, f);
            w.pop();
        }
    }
    let mut w = Vec::with_capacity(16);
    dfs(md, *y, &mut w, 6, glen, maxlen, f);
}

/// Every start, on the U or the D layer, with its number of moves: a quarter turn (1); a side half turn and a
/// quarter turn (2); a move of the U or D layer, a side half turn and a quarter turn (3).
fn starts() -> Vec<(u8, Vec<usize>)> {
    const Q: [usize; 4] = [0, 2, 3, 5];
    let mut v: Vec<(u8, Vec<usize>)> = Q.iter().map(|&q| (1, vec![q])).collect();
    for h in 6..10 {
        v.extend(Q.iter().map(|&q| (2, vec![h, q])));
    }
    for a in 0..6 {
        for h in 6..10 {
            v.extend(Q.iter().map(|&q| (3, vec![a, h, q])));
        }
    }
    v
}

/// (way, class of the start, class of the path).
type Key = (u8, u64, u64);

/// For each of the 96 corner states of HTR (by corner rank), a half-turn word that solves its corners.
pub fn corner_fix() -> HashMap<usize, Vec<usize>> {
    let mut map: HashMap<usize, Vec<usize>> = HashMap::new();
    let mut list: Vec<(St, Vec<usize>)> = vec![(St::ID, vec![])];
    map.insert(rank_perm(&St::ID.c), vec![]);
    let mut i = 0;
    while i < list.len() {
        let (s, w) = list[i].clone();
        for &h in &HALF {
            let t = s.apply_move(h);
            if let std::collections::hash_map::Entry::Vacant(e) = map.entry(rank_perm(&t.c)) {
                // the word that makes the state, read backwards, undoes it (half turns are their own inverses)
                let mut made = w.clone();
                made.push(h);
                e.insert(made.iter().rev().copied().collect());
                list.push((t, made));
            }
        }
        i += 1;
    }
    assert_eq!(map.len(), 96);
    map
}

/// The class of a start `a` and of the path `w` made after it on the other side: the D-free image of each, with the
/// direction of its last quarter turn folded.  A start with D for U leaves the other side as it is up to a turn of
/// both layers together made first (U' D), so the same path, with its last quarter turn on the other layer, comes to
/// the HTR from both, and the path's class is its own image whatever the spelling of the start.
fn niss_key(cx: &Ctx, a: &[usize], w: &[usize]) -> (u64, u64) {
    (cx.im.key(a, true), cx.im.key(w, true))
}

/// The HTRs of one DR by class.  With `ulayer`, only the starts on the U layer (for the check).
fn collect(cx: &Ctx, sec: &Sec, fix: &HashMap<usize, Vec<usize>>, x: &St, capmax: usize, ulayer: bool) -> HashMap<Key, Rec> {
    let md = cx.md;
    let strict = std::env::var("STDORD_CHECK").is_ok();
    let mut bad: HashMap<Key, String> = HashMap::new();
    let goal = goal_of(qt_count(md, x));
    let xi = x.inv();
    let st: Vec<(u8, Vec<usize>)> = starts().into_iter().filter(|(_, a)| !ulayer || a.iter().all(|&m| m < 3 || m >= 6)).collect();
    let mut map: HashMap<Key, Rec> = HashMap::new();
    for view in 0u8..4 {
        let base = if view == 0 || view == 2 { *x } else { xi };
        let list: Vec<(u8, Vec<usize>)> = if view < 2 { vec![(0, vec![])] } else { st.clone() };
        for (lev, a) in list {
            let y = if view < 2 { base } else { base.mul(word(&a)).inv() };
            let al = a.len();
            let qa = a.iter().filter(|&&m| is_qt(m)).count();
            arrivals(md, &y, goal - al, capmax - al, &mut |w: &[usize], zi: u32| {
                let moves = (al + w.len()) as u8;
                let total = moves + md.fin[zi as usize];
                let kind = md.cases[md.hcase[zi as usize] as usize].kind as usize;
                let rd = read_any(sec, &y, w);
                // the linear skeleton: on normal and inverse the path's own; after a start, that of the whole solution
                // on the side of the path, which ends with the start undone (any finish that solves the corners will
                // do: the reading only looks at corners)
                let (ll, lroute) = if view < 2 {
                    (rd.l, rd.route)
                } else {
                    let end = w.iter().fold(y, |s, &m| s.apply_move(m));
                    let mut full: Vec<usize> = w.to_vec();
                    full.extend(&fix[&rank_perm(&end.c)]);
                    full.extend(a.iter().rev().map(|&m| [2, 1, 0, 5, 4, 3, 6, 7, 8, 9][m]));
                    let cut = full.iter().rposition(|&m| is_qt(m)).unwrap() + 1;
                    let lin = read_any(sec, &base.inv(), &full[..cut]);
                    assert!(usize::from(lin.q) == usize::from(rd.q) + qa, "the whole solution has the path's quarter turns and the start's");
                    (lin.l, lin.route)
                };
                let r = Rec {
                    dr: 0,
                    view,
                    lev,
                    sid: 0,
                    moves,
                    total,
                    pairs: pairs(&md.hg.st[zi as usize]),
                    q: (qa + w.iter().filter(|&&m| is_qt(m)).count()) as u8,
                    lc: LC[kind],
                    l: al as u8 + rd.l,
                    p: rd.p,
                    s: rd.s,
                    t: rd.t,
                    ipairs: rd.ipairs,
                    route: rd.route,
                    ll,
                    lroute,
                    aord: a.iter().fold(1u32, |k, &m| k * 16 + m as u32),
                };
                assert!(rd.lc == LC[kind] && usize::from(rd.q) + qa == usize::from(r.q), "the reading and the HTR case disagree on the corner moves left");
                let (ka, kb) = if view < 2 { (0, cx.im.key(w, true)) } else { niss_key(cx, &a, w) };
                if std::env::var("STDORD_DBG").is_ok_and(|v| v == format!("{view},{ka},{kb}")) {
                    eprintln!("member ulayer={ulayer} start {} path {} moves {moves} total {total} lc {}", wname(&a), wname(w), LC[kind]);
                }
                let e = map.entry((view, ka, kb)).or_insert(r);
                if r.moves < e.moves {
                    (e.moves, e.pairs, e.q, e.lc) = (r.moves, r.pairs, r.q, r.lc);
                    (e.l, e.p, e.s, e.t, e.ipairs, e.route, e.aord) = (r.l, r.p, r.s, r.t, r.ipairs, r.route, r.aord);
                    (e.ll, e.lroute) = (r.ll, r.lroute);
                    if strict {
                        bad.remove(&(view, ka, kb));
                    }
                } else if r.moves == e.moves {
                    // the shortest members of a class are one path with its U-layer moves on either layer (a longer
                    // member writes a U2 as U D): the same extra moves and pairs, a skeleton that can only differ by
                    // the corner moves left, and after one spelling of the start the same corner cases
                    if strict && ((e.p, e.s, e.t, e.ipairs, e.q, e.lroute) != (r.p, r.s, r.t, r.ipairs, r.q, r.lroute) || (e.aord == r.aord && e.route != r.route)) {
                        bad.insert((view, ka, kb), format!("view {view} start {} path {}: pst {},{},{} / {},{},{} ipairs {} {} q {} {} routes {} {} linear routes {} {} lengths {} {}", wname(&a), wname(w), e.p, e.s, e.t, r.p, r.s, r.t, e.ipairs, r.ipairs, e.q, r.q, e.route, r.route, e.lroute, r.lroute, e.ll, r.ll));
                    }
                    e.l = e.l.min(r.l);
                    e.ll = e.ll.min(r.ll);
                    if r.aord < e.aord {
                        (e.route, e.aord) = (r.route, r.aord);
                    }
                }
                e.total = e.total.min(r.total);
            });
        }
    }
    assert!(bad.is_empty(), "two shortest spellings of one path read differently: {}", bad.values().next().unwrap());
    map
}

/// The HTRs of one DR, in a fixed order, the starts numbered from 1 in the order of their classes.
pub fn list(cx: &Ctx, sec: &Sec, fix: &HashMap<usize, Vec<usize>>, x: &St, dr: u32, capmax: usize) -> Vec<Rec> {
    let map = collect(cx, sec, fix, x, capmax, false);
    if std::env::var("STDORD_CHECK").is_ok() {
        // the starts on the U layer alone: the same HTRs with the same moves, a best finish that is never shorter, and
        // a few HTRs missing near the goal (the corner moves left can be fewer after a start on the D layer)
        let u = collect(cx, sec, fix, x, capmax, true);
        for (k, r) in &u {
            let f = map.get(k).unwrap_or_else(|| panic!("DR {dr}: an HTR of the U-layer starts is not in the list"));
            assert!(
                (f.moves, f.pairs, f.q) == (r.moves, r.pairs, r.q) && f.total <= r.total,
                "DR {dr}: an HTR differs with the U-layer starts: key {},{},{} view {} lev {} moves {} {} total {} {} pairs {} {} q {} {} lc {} {}",
                k.0, k.1, k.2, f.view, f.lev, f.moves, r.moves, f.total, r.total, f.pairs, r.pairs, f.q, r.q, f.lc, r.lc
            );
        }
        let goal = goal_of(qt_count(cx.md, x)) as u8;
        for (k, r) in &map {
            assert!(u.contains_key(k) || r.moves + 3 >= goal, "DR {dr}: an HTR far from the goal is missing with the U-layer starts");
        }
        assert!((map.len() - u.len()) * 20 <= map.len(), "DR {dr}: {} HTRs, and {} from the U-layer starts", map.len(), u.len());
    }
    let mut v: Vec<(Key, Rec)> = map.into_iter().collect();
    v.sort_unstable_by_key(|(k, _)| *k);
    let mut ids: Vec<u64> = v.iter().filter(|(k, _)| k.0 >= 2).map(|(k, _)| k.1).collect();
    ids.sort_unstable();
    ids.dedup();
    v.into_iter().map(|(k, r)| Rec { dr, sid: if k.0 < 2 { 0 } else { ids.binary_search(&k.1).unwrap() as u8 + 1 }, ..r }).collect()
}

fn sample(md: &Model, n: usize, seed: u64, mwant: usize) -> Vec<St> {
    let mut rng = crate::Rng(seed);
    let mut xs = Vec::new();
    while xs.len() < n {
        let x = crate::random_dr(md, &mut rng);
        if qt_count(md, &x) == mwant {
            xs.push(x);
        }
    }
    xs
}

/// drvar metastdlist N SEED M CAPMAX OUT : the DRs of `metatuple N SEED M`; every HTR of the standard meta within
/// CAPMAX moves, 40 bytes each (`Rec::bytes`).  OUT "-" only prints the counts by cap and moves before the NISS.
/// STDORD_CAPS="4a2=12,0c3=13" sets another cap for the DRs of a corner case.
pub fn run(md: &Model, n: usize, seed: u64, mwant: usize, capmax: usize, out: &str) {
    use rayon::prelude::*;
    use std::io::Write;
    let cx = Ctx::new(md);
    let sec = Sec::new();
    let fix = corner_fix();
    let xs = sample(md, n, seed, mwant);
    // STDORD_CAPS="4a2=12,0c3=13": another cap for the DRs of a corner case
    let over: Vec<(String, usize)> = std::env::var("STDORD_CAPS")
        .map(|v| v.split(',').filter(|t| !t.is_empty()).map(|t| { let (a, b) = t.split_once('=').unwrap(); (a.to_string(), b.parse().unwrap()) }).collect())
        .unwrap_or_default();
    let cap_of = |x: &St| over.iter().find(|(c, _)| md.subset(x).starts_with(c.as_str())).map_or(capmax, |o| o.1);
    let mut f = if out == "-" { None } else { Some(std::io::BufWriter::new(std::fs::File::create(out).unwrap())) };
    let t0 = std::time::Instant::now();
    let mut tot = 0u64;
    for (b, chunk) in xs.chunks(64).enumerate() {
        let res: Vec<Vec<Rec>> = chunk.par_iter().enumerate().map(|(i, x)| list(&cx, &sec, &fix, x, (b * 64 + i) as u32, cap_of(x))).collect();
        for (i, v) in res.iter().enumerate() {
            tot += v.len() as u64;
            match f.as_mut() {
                Some(f) => {
                    for r in v {
                        f.write_all(&r.bytes()).unwrap();
                    }
                }
                None => {
                    // HTRs within each cap with a NISS after at most 0, 1, 2, 3 moves, and the within-goal ones
                    let goal = goal_of(mwant) as u8;
                    let mut line = format!("{}\t{}", b * 64 + i, md.subset(&chunk[i]));
                    for lev in 0..4u8 {
                        let c: Vec<String> = (7..=capmax as u8)
                            .map(|cap| {
                                let k = v.iter().filter(|r| r.lev <= lev && r.moves <= cap);
                                format!("{}/{}", k.clone().count(), k.filter(|r| r.total <= goal).count())
                            })
                            .collect();
                        line += &format!("\t{}", c.join(","));
                    }
                    println!("{line}");
                }
            }
        }
        eprintln!("{} / {n}  {:.0}s  {tot} HTRs", (b * 64 + chunk.len()).min(n), t0.elapsed().as_secs_f64());
    }
}

/// drvar metaud N SEED M : a check of the class totals.  A leave-slice finish only has to bring the U and D layers
/// right relative to each other, so an HTR state and the one a half turn of both layers away (U2 D2) have the same
/// true finish.  The finish table keeps the centres fixed; a class makes up for it by taking the best total over
/// every spelling of its path (U or D for each U-layer move, either way for the last quarter turn).  With three or
/// more quarter turns, or a U2, the spellings end on all four states that are a half turn of a layer apart; with two
/// quarter turns on three of the four.  This counts, by quarter turns, the classes whose total would be smaller with
/// the fourth, and how many of those would come within the goal.
pub fn udcheck(md: &Model, n: usize, seed: u64, mwant: usize) {
    use crate::meta::{real_variants, Uni};
    let cx = Ctx::new(md);
    let goal = goal_of(mwant);
    let qmax = (mwant + 2).min(6);
    let mut tab = [[0u64; 4]; 8];      // by q: classes, smaller with the fourth state, of those newly within goal, DRs' best
    let mut drs = [0u64; 2];
    for (i, x) in sample(md, n, seed, mwant).iter().enumerate() {
        let (mut b1, mut b2) = (255u8, 255u8);
        for y in [*x, x.inv()] {
            let mut map: HashMap<u64, (u8, u8, u8)> = HashMap::new();
            real_variants(md, &y, &Uni { goal, cap_any: 0, qmax }, &mut |w: &[usize], q: usize, zi: u32| {
                let z = md.hg.st[zi as usize];
                let z2 = md.hg.get(&z.apply_move(1).apply_move(4)).unwrap();
                let len = w.len() as u8;
                let (t1, t2) = (len + md.fin[zi as usize], len + md.fin[zi as usize].min(md.fin[z2 as usize]));
                let e = map.entry(cx.im.key(w, true)).or_insert((q as u8, 255, 255));
                e.1 = e.1.min(t1);
                e.2 = e.2.min(t2);
            });
            for (q, t1, t2) in map.values() {
                let r = &mut tab[*q as usize];
                r[0] += 1;
                r[1] += u64::from(t2 < t1);
                r[2] += u64::from(*t2 as usize <= goal && *t1 as usize > goal);
                b1 = b1.min(*t1);
                b2 = b2.min(*t2);
            }
        }
        drs[0] += u64::from(b2 < b1);
        drs[1] += u64::from(b2 as usize <= goal && b1 as usize > goal);
        if b2 < b1 {
            println!("DR {i} {}: best {b1} with the spellings, {b2} with the fourth state", md.subset(x));
        }
    }
    for (q, r) in tab.iter().enumerate().filter(|(_, r)| r[0] > 0) {
        println!("{q} quarter turns: {} classes, {} with a smaller total, {} of those newly within goal", r[0], r[1], r[2]);
    }
    println!("DRs whose best total is smaller: {}, newly within goal: {}", drs[0], drs[1]);
}
