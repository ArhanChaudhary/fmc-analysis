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
use crate::meta::{goal_of, qt_count, real_variants, Cls, Ctx, Uni};
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
    form: Vec<usize>,
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
    q: usize,
    goal: usize,
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
                let e = self.found.entry((self.q, route)).or_insert(Skel { l: full.len(), shape: sh, ways: 0, form: full.clone() });
                assert_eq!(e.l, full.len(), "one route, one length");
                e.ways += 1;
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
            for qt in [0usize, 2] {
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

fn skeletons(md: &Model, sec: &Sec, f: &Forms, y: &St, m: usize, goal: usize) -> BTreeMap<(usize, u64), Skel> {
    let mut found = BTreeMap::new();
    for q in [m, m + 2] {
        if q > 6 {
            continue;
        }
        let mut wk = Walk { md, sec, f, q, goal, found };
        wk.go(corners(y), &mut Vec::new(), &mut Vec::new(), 0, 1);
        found = wk.found;
    }
    found
}

fn wvec(a: &[u8; 16], n: u8) -> Vec<usize> {
    a[..n as usize].iter().map(|&m| m as usize).collect()
}
fn nums<T: std::fmt::Display>(v: &[T]) -> String {
    v.iter().map(T::to_string).collect::<Vec<_>>().join(",")
}

/// The JSON lines of one DR.  `pmax`, `cap`: members are written out for the classes with P <= pmax and
/// P+S+T <= cap (the fixed part of the meta); the other classes get their line without members.
fn annotate(cx: &Ctx, sec: &Sec, fm: &Forms, scr: &str, x: &St, mwant: Option<usize>, pmax: u8, cap: u8) -> String {
    let md = cx.md;
    let m = mwant.unwrap_or_else(|| qt_count(md, x));
    let goal = goal_of(m);
    let qmax = (m + 2).min(6);
    let mut out = String::new();
    writeln!(
        out,
        "{{\"t\":\"dr\",\"scramble\":\"{scr}\",\"subset\":\"{}\",\"qt\":{},\"m\":{m},\"goal\":{goal},\"lsopt\":{},\"pmax\":{pmax},\"cap\":{cap}}}",
        md.subset(x),
        qt_count(md, x),
        md.lsopt(x)
    )
    .unwrap();
    for (side, y, other) in [("N", *x, x.inv()), ("I", x.inv(), *x)] {
        for ((q, route), sk) in &skeletons(md, sec, fm, &y, m, goal) {
            writeln!(
                out,
                "{{\"t\":\"skel\",\"side\":\"{side}\",\"q\":{q},\"route\":\"{route:x}\",\"L\":{},\"shape\":[{}],\"ways\":{},\"form\":\"{}\"}}",
                sk.l,
                nums(&sk.shape),
                sk.ways,
                wname(&sk.form)
            )
            .unwrap();
        }
        let uni = Uni { goal, cap_any: 0, qmax };
        let cl = cx.classes(&y, &uni);
        let mut keys: Vec<u64> = cl.keys().copied().collect();
        keys.sort();
        // the reading of every class (its shortest member), and the classes whose members are written out
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
                let (p, s, t) = reads[k].0.pst();
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
            let mut full = wvec(&c.w, c.wl);
            full.extend(crate::crisp::ls_finish(md, c.z));
            let inv: Vec<usize> = full.iter().rev().map(|&mv| MOVE_INV[mv]).collect();
            let (mq, mroute) = route_of(sec, &other, &inv);
            assert_eq!(mq, q);
            write!(
                out,
                "{{\"t\":\"cls\",\"side\":\"{side}\",\"key\":\"{k:x}\",\"route\":\"{:x}\",\"mirror\":\"{mroute:x}\",\"q\":{q},\"kind\":\"{}\",\"L\":{},\"lc\":{},\"e\":[{}],\"shape\":[{}],\"a2\":{},\"wl\":{},\"total\":{},\"nb\":[{}],\"pre2\":\"{pre2:x}\"",
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
                if !common {
                    // no member starts with the approach's common spelling: fall back to this class's own
                    let mine = own(k);
                    list = mem[k].iter().filter(|(w, _)| mine.contains(&w[..(r.a2 as usize).min(w.len())])).collect();
                }
                list.sort_by_key(|(w, zi)| (w.len(), md.fin[*zi as usize], w.clone()));
                write!(out, ",\"approach\":\"{}\",\"common\":{common},\"members\":[", wname(&rp.iter().map(|&mv| mv as usize).collect::<Vec<_>>())).unwrap();
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
            out.push_str("}\n");
        }
    }
    out
}

/// drvar metaannot RULES "SCRAMBLE" [M] [PMAX] [CAP]      one DR, to standard output
/// drvar metaannot RULES @LIST OUTDIR [PMAX] [CAP]        LIST: one `ID<tab>SCRAMBLE[<tab>M]` per line -> OUTDIR/ID.jsonl
/// SCRAMBLE in DR moves; M overrides the DR's quarter turns (a 0c0 DR read as a 2qt one, goal 12).
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
            let t0 = std::time::Instant::now();
            let s = annotate(&cx, &sec, &fm, f[1].trim(), &state(f[1].trim()), mwant, pmax, cap);
            let path = format!("{dir}/{}.jsonl", f[0].trim());
            std::fs::write(&path, s).unwrap_or_else(|e| fatal!("{path}: {e}"));
            eprintln!("{path}  {:.1}s", t0.elapsed().as_secs_f64());
        }
    } else {
        let mwant = args.get(2).and_then(|v| v.parse().ok());
        print!("{}", annotate(&cx, &sec, &fm, &args[1], &state(&args[1]), mwant, num(3, 1), num(4, 5)));
    }
}
