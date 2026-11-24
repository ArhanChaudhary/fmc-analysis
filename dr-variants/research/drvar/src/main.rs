//! Advanced DR Bounding: is a cheap zero-bad-slice variant at most one insertion from the best finish of its
//! skeleton?  See `search.rs` for the definitions and REPORT.md for the write-up.
//!
//!   drvar run N SEED OUT.tsv      N uniform random DR states, one line per qualifying variant
//!   drvar check N SEED            completeness checks (the path enumeration reproduces the exact optimum)
macro_rules! fatal {
    ($($arg:tt)*) => {{
        eprintln!($($arg)*);
        std::process::exit(1)
    }};
}

#[allow(dead_code)]
#[path = "../../../../judging-a-dr/research/drtools/src/class.rs"]
mod class;
#[allow(dead_code)]
#[path = "../../../../judging-a-dr/research/drtools/src/core.rs"]
mod core;
#[allow(dead_code)]
#[path = "../../../../judging-a-dr/research/drtools/src/quot.rs"]
mod quot;
#[allow(dead_code)]
#[path = "../../../../judging-a-dr/research/drtools/src/reduced.rs"]
mod reduced;
mod model;
mod split;
mod search;
mod crisp;
mod crisp3;
mod meta;
mod tuple;
mod stdcmp;
mod stdord;
mod annot;

use crate::core::{perm_parity, St};
use model::*;
use rayon::prelude::*;
use search::*;
use std::io::Write;

const CASES: &str = "/data/fmc/dr-variants/research/data/cases216.tsv";
const EXACT: &str = "/data/fmc/judging-a-dr/research/data/lean_exact_table.u8";
/// Largest S + T kept for a variant.
const STMAX: usize = 2;
/// Longest inserted block (half turns, before cancelling) that counts as one insertion.
const JMAX: u8 = 7;
/// Most quarter turns looked at.
const MMAX: usize = 6;
/// Deepest search for a skeleton's best finish, in moves over the DR's optimal finish.
const DEEPMAX: usize = 4;
/// Most qualifying variants tested per skeleton family.
const QCAP: usize = 2000;

pub struct Rng(pub u64);
impl Rng {
    fn next(&mut self) -> u64 {
        self.0 = self.0.wrapping_add(0x9E37_79B9_7F4A_7C15);
        let mut z = self.0;
        z = (z ^ (z >> 30)).wrapping_mul(0xBF58_476D_1CE4_E5B9);
        z = (z ^ (z >> 27)).wrapping_mul(0x94D0_49BB_1331_11EB);
        z ^ (z >> 31)
    }
    pub fn below(&mut self, n: u64) -> u64 { self.next() % n }
}

/// A uniformly random DR state.
pub fn random_dr(md: &Model, rng: &mut Rng) -> St {
    loop {
        let c = rng.below(40320) as usize;
        let e = rng.below(40320) as usize;
        let s = rng.below(24) as usize;
        let st = St::unrank(c, e, s);
        if perm_parity(&st.c) ^ perm_parity(&st.e) == perm_parity(&st.s) && md.hg.get(&st).is_none() {
            return st;
        }
    }
}

/// The DR moves that produce state x from solved (the inverse of an optimal finish).
pub fn scramble_of(md: &Model, x: &St) -> Vec<usize> {
    let mut s = *x;
    let mut sol = Vec::new();
    let mut lf = 6;
    while md.opt(&s) > 0 {
        let d = md.opt(&s);
        let mv = (0..10).find(|&mv| allowed(lf, mv) && md.opt(&s.apply_move(mv)) + 1 == d).expect("table descent");
        sol.push(mv);
        s = s.apply_move(mv);
        lf = FACE[mv];
    }
    sol.iter().rev().map(|&m| [2, 1, 0, 5, 4, 3, 6, 7, 8, 9][m]).collect()
}

struct Fam {
    m: usize,
    k: usize,
    lpre: u8,
}

fn find(p: &mut [usize], i: usize) -> usize {
    let mut r = i;
    while p[r] != r {
        r = p[r];
    }
    p[i] = r;
    r
}

fn analyse(md: &Model, hc: &HcIndex, jcl: &[[u8; 8]], x: &St, id: usize) -> Vec<String> {
    let timing = std::env::var_os("DRVAR_TIME").is_some();
    let opt = md.opt(x);
    let lp = skeleton_lengths(md, x, MMAX);
    let mmin = (1..=MMAX).find(|&m| lp[m].iter().any(|&l| l != 255)).unwrap();
    let lmin = (1..=MMAX).flat_map(|m| lp[m].iter().copied()).min().unwrap();
    // the skeletons a solver would look at: fewest quarter turns or one more, at most 3 moves over the shortest
    let fams: Vec<Fam> = (mmin..=(mmin + 1).min(MMAX))
        .flat_map(|m| (0..6).map(move |k| (m, k)))
        .filter(|&(m, k)| lp[m][k] != 255 && lp[m][k] <= lmin + 3)
        .map(|(m, k)| Fam { m, k, lpre: lp[m][k] })
        .collect();
    let fam_of = |m: u8, k: u8| fams.iter().position(|f| f.m == m as usize && f.k == k as usize);
    let qmax = fams.iter().map(|f| f.m).max().unwrap();
    let cap = fams.iter().map(|f| f.lpre as usize + STMAX).max().unwrap();
    // skeletons: the shortest corner paths of each family, grouped into classes of mutual variants
    let mut sks: Vec<Skeleton> = Vec::new();
    let mut sk_fam: Vec<usize> = Vec::new();
    for (fi, f) in fams.iter().enumerate() {
        for w in skeletons_of(md, x, f.m, f.k, f.lpre as usize) {
            sks.push(make_skeleton(md, hc, jcl, w, f.k as u8));
            sk_fam.push(fi);
        }
    }
    let mut par: Vec<usize> = (0..sks.len()).collect();
    for i in 0..sks.len() {
        for j in i + 1..sks.len() {
            if sk_fam[i] == sk_fam[j] && find(&mut par, i) != find(&mut par, j) && (is_variant(hc, &sks[i], &sks[j].w) || is_variant(hc, &sks[j], &sks[i].w)) {
                let (a, b) = (find(&mut par, i), find(&mut par, j));
                par[a] = b;
            }
        }
    }
    let mut cls_of_sk = vec![usize::MAX; sks.len()];
    let mut classes: Vec<Vec<usize>> = Vec::new();
    for i in 0..sks.len() {
        let r = find(&mut par, i);
        if cls_of_sk[r] == usize::MAX {
            cls_of_sk[r] = classes.len();
            classes.push(Vec::new());
        }
        let c = cls_of_sk[r];
        cls_of_sk[i] = c;
        classes[c].push(i);
    }
    let class_fam: Vec<usize> = classes.iter().map(|c| sk_fam[c[0]]).collect();
    let classes_of = |p: &PathRec| -> Vec<usize> {
        let Some(f) = fam_of(p.m, p.kind) else { return Vec::new() };
        (0..classes.len()).filter(|&c| class_fam[c] == f && classes[c].iter().any(|&s| is_variant(hc, &sks[s], &p.w))).collect()
    };
    // variants: every path of a considered family with S + T <= STMAX
    let c0 = |s: &St| crate::core::rank_perm(&s.c);
    let vars = paths(md, x, cap, qmax, |s, len, q| {
        // corner-only: some considered family must still be reachable within L_pre + STMAX
        let c = c0(s);
        let ok = fams.iter().any(|f| f.m >= q && {
            let r = md.rem[f.k][f.m - q][c];
            r != 255 && len + r as usize <= f.lpre as usize + STMAX
        });
        if ok { md.htrd(s) as usize } else { cap + 1 }
    }, |len, m, k, _| {
        fam_of(m, k).is_some_and(|f| len <= fams[f].lpre as usize + STMAX)
    });
    // zero bad slices; at most QCAP per family are tested (a fixed pseudo-random sample), counts are weighted
    let mut per_fam: Vec<Vec<&PathRec>> = vec![Vec::new(); fams.len()];
    for p in vars.iter().filter(|p| md.cases[p.case as usize].bad() == 0) {
        per_fam[fam_of(p.m, p.kind).unwrap()].push(p);
    }
    let mut weight = vec![1.0f64; fams.len()];
    let mut nqual_fam = vec![0usize; fams.len()];
    let mut qual: Vec<(&PathRec, Vec<usize>)> = Vec::new();
    for (f, list) in per_fam.iter_mut().enumerate() {
        nqual_fam[f] = list.len();
        if list.len() > QCAP {
            let mut r = Rng(0x5eed ^ (id as u64) << 8 ^ f as u64);
            for i in 0..QCAP {
                let j = i + (r.below((list.len() - i) as u64) as usize);
                list.swap(i, j);
            }
            weight[f] = list.len() as f64 / QCAP as f64;
            list.truncate(QCAP);
        }
        for p in list.iter() {
            let cs = classes_of(p);
            if !cs.is_empty() {
                qual.push((p, cs));
            }
        }
    }
    if timing {
        eprintln!("state {id}: {} skeletons in {} classes, {} paths, {} qualifying variants of a skeleton", sks.len(), classes.len(), vars.len(), qual.len());
    }
    let mut needed: Vec<usize> = qual.iter().flat_map(|(_, c)| c.iter().copied()).collect();
    needed.sort_unstable();
    needed.dedup();
    if needed.is_empty() {
        return Vec::new();
    }
    // every path of a considered family whose finish is <= bound, deepening until each needed skeleton class
    // has a variant there (or opt + DEEPMAX is reached), pruned with the exact optimal finish
    let t0 = std::time::Instant::now();
    let mut bound = opt as usize;
    let mut sols;
    let mut sol_cls: Vec<Vec<usize>>;
    loop {
        sols = paths(md, x, bound, qmax, |s, _, _| md.opt(s) as usize, |_, m, k, best| fam_of(m, k).is_some() && best as usize <= bound);
        sol_cls = sols.iter().map(&classes_of).collect();
        let found = needed.iter().all(|&c| sol_cls.iter().any(|v| v.contains(&c)));
        if found || bound >= opt as usize + DEEPMAX {
            break;
        }
        bound += 1;
    }
    let tb = t0.elapsed().as_secs_f64();
    let mut cbest = vec![255u8; classes.len()];
    for (p, cs) in sols.iter().zip(&sol_cls) {
        for &c in cs {
            cbest[c] = cbest[c].min(p.best);
        }
    }
    if timing {
        eprintln!("state {id}: opt {opt}, {} solutions up to {bound} in {tb:.2}s", sols.len());
    }
    let t1 = std::time::Instant::now();
    let scr = wname(&scramble_of(md, x));
    let sub = md.subset(x);
    let fin_of = |z: u32| wname(&md.hg.word_of(z).into_iter().rev().collect::<Vec<_>>());
    let mut lines = Vec::new();
    for (c, members) in classes.iter().enumerate() {
        let f = &fams[class_fam[c]];
        let nq = qual.iter().filter(|(_, cs)| cs.contains(&c)).count();
        let bestp = sols.iter().zip(&sol_cls).filter(|(p, cs)| cs.contains(&c) && p.best == cbest[c]).min_by_key(|(p, _)| p.w.len());
        lines.push(format!(
            "K\t{id}\t{sub}\t{opt}\t{mmin}\t{m}\t{k}\t{lpre}\t{c}\t{nm}\t{rep}\t{nq}\t{nqf}\t{w}\t{cb}\t{bp}\t{scr}",
            m = f.m,
            k = KIND_NAME[f.k],
            lpre = f.lpre,
            nm = members.len(),
            rep = wname(&sks[members[0]].w),
            nqf = nqual_fam[class_fam[c]],
            w = weight[class_fam[c]],
            cb = cbest[c],
            bp = bestp.map(|(p, _)| format!("{} | {}", wname(&p.w), fin_of(p.z))).unwrap_or_default(),
        ));
    }
    // counts per (class, S+T, rule penalty, status): variants, summed gap to the skeleton's best finish,
    // summed gap left after the best single insertion
    let mut cnt: std::collections::BTreeMap<(usize, usize, u8, &str), (usize, usize, usize)> = std::collections::BTreeMap::new();
    let mut shown: std::collections::HashMap<(usize, &str), usize> = std::collections::HashMap::new();
    let nshow: usize = std::env::var("DRVAR_EX").ok().and_then(|v| v.parse().ok()).unwrap_or(3);
    for (v, cs) in &qual {
        for &c in cs {
            let fam = &fams[class_fam[c]];
            let case = &md.cases[v.case as usize];
            let st = v.w.len() - fam.lpre as usize;
            let target = cbest[c];
            let tops: Vec<&PathRec> = sols.iter().zip(&sol_cls).filter(|(p, pc)| pc.contains(&c) && p.best == target).map(|(p, _)| p).collect();
            let tps: Vec<(St, usize)> = tops.iter().map(|p| (word(&p.w), p.w.len())).collect();
            let (status, hit, best1) = if target == 255 {
                ("unknown", None, 255u8)
            } else if v.best <= target {
                ("own", None, v.best)
            } else {
                let h = one_insertion(md, &v.w, &tps, false).filter(|(h, _)| h.jlen <= JMAX);
                if let Some((h, pi)) = h {
                    ("one", Some((h, tops[pi])), target)
                } else {
                    // how close does one insertion get?
                    let mut b1 = v.best;
                    for lvl in target + 1..v.best.min(target + 3) {
                        if lvl as usize > bound {
                            break;
                        }
                        let lp: Vec<(St, usize)> = sols.iter().zip(&sol_cls).filter(|(p, pc)| pc.contains(&c) && p.best == lvl).map(|(p, _)| (word(&p.w), p.w.len())).collect();
                        if one_insertion(md, &v.w, &lp, false).is_some_and(|(h, _)| h.jlen <= JMAX) {
                            b1 = lvl;
                            break;
                        }
                    }
                    // with U <-> D changes of the later quarter turns allowed as well
                    let gen = one_insertion(md, &v.w, &tps, true).is_some_and(|(h, _)| h.jlen <= JMAX);
                    (if gen { "one_ud" } else { "fail" }, None, b1)
                }
            };
            let e = cnt.entry((c, st, case.heur, status)).or_insert((0, 0, 0));
            e.0 += 1;
            if target != 255 {
                e.1 += v.best.saturating_sub(target) as usize;
                e.2 += best1.saturating_sub(target) as usize;
            }
            let n = shown.entry((c, status)).or_insert(0);
            if *n < nshow {
                *n += 1;
                let (hs, via) = match &hit {
                    Some((h, p)) => (format!("{}/{}/{}/{}", h.sec, h.pos, h.jlen, h.flips), format!("{} | {}", wname(&p.w), fin_of(p.z))),
                    None => ("-".to_string(), String::new()),
                };
                lines.push(format!(
                    "E\t{id}\t{sub}\t{opt}\t{mmin}\t{m}\t{k}\t{lpre}\t{c}\t{st}\t{cname}\t{heur}\t{best}\t{target}\t{status}\t{best1}\t{hs}\t{vw} | {fin}\t{via}\t{scr}",
                    m = v.m,
                    k = KIND_NAME[v.kind as usize],
                    lpre = fam.lpre,
                    cname = case.name(),
                    heur = case.heur,
                    best = v.best,
                    vw = wname(&v.w),
                    fin = fin_of(v.z),
                ));
            }
        }
    }
    for ((c, st, heur, status), (n, gap, gap1)) in cnt {
        let fam = &fams[class_fam[c]];
        lines.push(format!(
            "C\t{id}\t{sub}\t{opt}\t{mmin}\t{m}\t{k}\t{lpre}\t{c}\t{cb}\t{st}\t{heur}\t{status}\t{n}\t{gap}\t{gap1}\t{w}",
            m = fam.m,
            k = KIND_NAME[fam.k],
            lpre = fam.lpre,
            cb = cbest[c],
            w = weight[class_fam[c]],
        ));
    }
    if timing {
        eprintln!("state {id}: insertion tests {:.2}s", t1.elapsed().as_secs_f64());
    }
    lines
}


/// The best finish of the skeleton(s) that variant v belongs to, and every path that reaches it.
fn class_targets(md: &Model, hc: &HcIndex, jcl: &[[u8; 8]], x: &St, v: &[usize]) -> Option<(u8, Vec<Vec<usize>>)> {
    let z = md.hg.get(&x.mul(word(v)))?;
    let kind = md.cases[md.hcase[z as usize] as usize].kind;
    let m = v.iter().filter(|&&mv| is_qt(mv)).count();
    let lp = skeleton_lengths(md, x, MMAX);
    let sks: Vec<Skeleton> = skeletons_of(md, x, m, kind as usize, lp[m][kind as usize] as usize)
        .into_iter()
        .map(|w| make_skeleton(md, hc, jcl, w, kind))
        .filter(|s| is_variant(hc, s, v))
        .collect();
    if sks.is_empty() {
        return None;
    }
    let opt = md.opt(x) as usize;
    for bound in opt..=opt + 6 {
        let sols = paths(md, x, bound, m, |s, _, _| md.opt(s) as usize, |_, mm, k, best| mm as usize == m && k == kind && best as usize <= bound);
        let mine: Vec<&PathRec> = sols.iter().filter(|p| sks.iter().any(|s| is_variant(hc, s, &p.w))).collect();
        if let Some(b) = mine.iter().map(|p| p.best).min() {
            return Some((b, mine.iter().filter(|p| p.best == b).map(|p| p.w.clone()).collect()));
        }
    }
    None
}

/// Two insertions: the first is any J block of at most JMAX half turns put anywhere in a section (the section is
/// then rewritten as short as possible); the second is found by `one_insertion`.
fn two_insertions(md: &Model, v: &[usize], ps: &[(St, usize)], jlist: &[u32]) -> Option<(usize, usize, u8, Hit)> {
    let qpos: Vec<usize> = (0..v.len()).filter(|&i| is_qt(v[i])).collect();
    for a in 0..qpos.len() {
        let s0 = if a == 0 { 0 } else { qpos[a - 1] + 1 };
        let sec = &v[s0..qpos[a]];
        for i in 0..=sec.len() {
            let u = word(&sec[..i]);
            let w = word(&sec[i..]);
            for &ji in jlist {
                let t = u.mul(md.hg.st[ji as usize]).mul(w);
                let ti = md.hg.get(&t).unwrap();
                let mut v1 = v[..s0].to_vec();
                v1.extend(md.hg.word_of(ti));
                v1.extend_from_slice(&v[qpos[a]..]);
                let v1 = reduce(&v1);
                if v1.iter().filter(|&&mv| is_qt(mv)).count() != qpos.len() {
                    continue;
                }
                if let Some((h, _)) = one_insertion(md, &v1, ps, false).filter(|(h, _)| h.jlen <= JMAX) {
                    return Some((a, i, md.hg.d3[ji as usize], h));
                }
            }
        }
    }
    None
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        fatal!("usage: drvar run N SEED OUT.tsv | check N SEED");
    }
    if args[1] == "diag" {
        let md = Model::bare();
        md.diag(CASES, "/data/fmc/dr-variants/research/data/fm216.tsv");
        return;
    }
    let mut md = Model::new(CASES, EXACT);
    if args[1].starts_with("crisp") || args[1].starts_with("meta") || args[1] == "lsb" {
        md.leave_slice("/data/fmc/judging-a-dr/research/data/ls_depth.u8");
    }
    let md = md;
    // the half-turn minimum of every case against the sheet's penalty (HTR-breaking finishes allowed there)
    let mut le = 0;
    for c in &md.cases {
        if c.min_d3 >= LC[c.kind as usize] + c.pen {
            le += 1;
        }
        assert!(c.min_d3 >= LC[c.kind as usize] + c.heur, "Rodney's rule above the half-turn optimum: {}", c.name());
    }
    eprintln!("cases where the half-turn optimum >= corner moves + sheet penalty: {le} of 216; rule is a lower bound in all 216");
    let hc = HcIndex::new(&md);
    let jcl = jc_list(&md);
    match args[1].as_str() {
        "run" => {
            let n: usize = args[2].parse().unwrap();
            let seed: u64 = args[3].parse().unwrap();
            let mut rng = Rng(seed);
            let xs: Vec<St> = (0..n).map(|_| random_dr(&md, &mut rng)).collect();
            let done = std::sync::atomic::AtomicUsize::new(0);
            let res: Vec<Vec<String>> = xs
                .par_iter()
                .enumerate()
                .map(|(i, x)| {
                    let r = analyse(&md, &hc, &jcl, x, i);
                    let d = done.fetch_add(1, std::sync::atomic::Ordering::Relaxed) + 1;
                    if d % 50 == 0 {
                        eprintln!("{d} / {n}");
                    }
                    r
                })
                .collect();
            let mut f = std::io::BufWriter::new(std::fs::File::create(&args[4]).unwrap());
            writeln!(f, "# K: id subset opt mmin m kind lpre class n_skeleton_words skeleton n_qual_tested n_qual_family weight skeleton_best best_path scramble").unwrap();
            writeln!(f, "# C: id subset opt mmin m kind lpre class skeleton_best st heur status n sum_gap sum_gap_after_one_insertion weight").unwrap();
            writeln!(f, "# E: id subset opt mmin m kind lpre class st case heur best skeleton_best status best1 sec/pos/jlen/flips variant|finish via scramble").unwrap();
            for r in res {
                for l in r {
                    writeln!(f, "{l}").unwrap();
                }
            }
        }
        "path" => {
            // drvar path "SCRAMBLE" "PATH" : the HTR state after PATH, its case, and its half-turn finish
            let x = word(&crate::core::parse_moves(args[2].as_bytes(), 64).unwrap());
            let p = crate::core::parse_moves(args[3].as_bytes(), 64).unwrap();
            let z = x.mul(word(&p));
            match md.hg.get(&z) {
                None => println!("not in HTR"),
                Some(zi) => {
                    let c = &md.cases[md.hcase[zi as usize] as usize];
                    let fin: Vec<usize> = md.hg.word_of(zi).into_iter().rev().collect();
                    println!("{}  bad slices {}  rule bound +{}  finish {} ({})", c.name(), c.bad(), c.heur, md.hg.d3[zi as usize], wname(&fin));
                }
            }
        }
        "two" => {
            // drvar two RUN.tsv N : for up to N failing examples, the skeleton's best finish and whether two insertions reach it
            let n: usize = args[3].parse().unwrap();
            let jlist: Vec<u32> = (0..md.hg.st.len() as u32)
                .filter(|&i| md.hg.d3[i as usize] as u8 <= JMAX && md.jc[crate::core::rank_perm(&md.hg.st[i as usize].c)] && i != 0)
                .collect();
            eprintln!("{} insertion blocks of at most {JMAX} half turns", jlist.len());
            let txt = std::fs::read_to_string(&args[2]).unwrap();
            let mut seen = std::collections::HashSet::new();
            let ex: Vec<(String, String, String)> = txt
                .lines()
                .filter(|l| l.starts_with("E\t"))
                .map(|l| l.split('\t').map(String::from).collect::<Vec<_>>())
                .filter(|f| f[14] == "fail" && seen.insert((f[1].clone(), f[8].clone())))
                .take(n)
                .map(|f| (f[19].clone(), f[17].split(" | ").next().unwrap().to_string(), f[1].clone()))
                .collect();
            let res: Vec<String> = ex
                .par_iter()
                .map(|(scr, vw, id)| {
                    let x = word(&crate::core::parse_moves(scr.as_bytes(), 64).unwrap());
                    let v = crate::core::parse_moves(vw.as_bytes(), 64).unwrap();
                    let vb = v.len() + md.hg.d3[md.hg.get(&x.mul(word(&v))).unwrap() as usize] as usize;
                    match class_targets(&md, &hc, &jcl, &x, &v) {
                        None => format!("{id}\t{vw}\tno skeleton"),
                        Some((b, tops)) => {
                            let ps: Vec<(St, usize)> = tops.iter().map(|w| (word(w), w.len())).collect();
                            let one = one_insertion(&md, &v, &ps, false).filter(|(h, _)| h.jlen <= JMAX).is_some();
                            let two = if one { None } else { two_insertions(&md, &v, &ps, &jlist) };
                            format!(
                                "{id}\t{vw}\tvariant {vb}\tskeleton best {b} ({} paths)\tone {one}\ttwo {}\t{}",
                                tops.len(),
                                two.is_some(),
                                two.map(|(a, i, l, h)| format!("first: section {a} pos {i} block {l}; second: section {} pos {} block {}", h.sec, h.pos, h.jlen)).unwrap_or_default()
                            )
                        }
                    }
                })
                .collect();
            for r in res {
                println!("{r}");
            }
        }
        "crisp" => {
            // drvar crisp N SEED OUT.tsv [M...] : the 2qt hypothesis on N uniform random DRs (leave-slice)
            let n: usize = args[2].parse().unwrap();
            let mut rng = Rng(args[3].parse().unwrap());
            let mlist: Vec<usize> = if args.len() > 5 { args[5..].iter().map(|a| a.parse().unwrap()).collect() } else { vec![2, 3, 4, 5, 6] };
            let xs: Vec<St> = (0..n).map(|_| random_dr(&md, &mut rng)).collect();
            let done = std::sync::atomic::AtomicUsize::new(0);
            let res: Vec<Vec<String>> = xs
                .par_iter()
                .enumerate()
                .map(|(i, x)| {
                    let r = crisp::analyse(&md, &hc, &jcl, x, i, &mlist);
                    let d = done.fetch_add(1, std::sync::atomic::Ordering::Relaxed) + 1;
                    if d % 50 == 0 {
                        eprintln!("{d} / {n}");
                    }
                    r
                })
                .collect();
            let mut f = std::io::BufWriter::new(std::fs::File::create(&args[4]).unwrap());
            writeln!(f, "# P: id subset m kind lpre skeleton_best prefix_extra best_keeping_prefix part1 fewest_long part2 part1_if_prefix_qts_turned cheap_zero_bad_variant best_keeping_prefix_solution scramble weight").unwrap();
            writeln!(f, "# S: id subset m kind lpre skeleton_best n_prefixes n_tested n_qualifying n_part1 n_part2 skeleton skeleton_best_solution").unwrap();
            writeln!(f, "# O: id subset m kind lpre skeleton_best n_best_solutions fewest_extra_moves_before_2qt fewest_long_before_2qt long_before long_after (of the best solution with fewest long sections) that_solution skeleton best_in[no_long_before_and_<=1_after, no_extra_before, no_extra_before_and_<=1_long_after, <=2_extra_before_and_<=1_long_after, <=1_long_anywhere]").unwrap();
            writeln!(f, "# N: id m kind skeleton_best best_keeping_prefix keeps_best has_a_cheap_setup_in_the_skeleton weight   (routes with no extra moves that do not qualify)").unwrap();
            writeln!(f, "# V: id m kind family_paths_up_to_best+1 of_which_variants_of_a_shortest_skeleton").unwrap();
            for r in res {
                for l in r {
                    writeln!(f, "{l}").unwrap();
                }
            }
        }
        "metabase" => {
            // drvar metabase N SEED : optimal leave-slice length by quarter-turn count
            meta::base(&md, args[2].parse().unwrap(), args[3].parse().unwrap());
        }
        "metacount" => {
            // drvar metacount N SEED M QEXTRA : variants per side and length for N random M-qt DRs
            meta::count(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap(), args[5].parse().unwrap());
        }
        "metacases" => meta::cases(&md),
        "metawit" => meta::witnesses(&md),
        "metacheck" => meta::check(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap()),
        "metaniss" => meta::run_niss(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap(), &args[5]),
        "metahtrpairs" => meta::htr_pairs(&md),
        "metahtable" => meta::htable(&md),
        "metarule" => meta::run_rule(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap(), &args[5], &args[6]),
        "metacasemin" => meta::case_min(&md, args[2].parse().unwrap()),
        "metahcheck" => meta::hcheck(&md, args[2].parse().unwrap(), args[3].parse().unwrap()),
        "metastates" => meta::run_states(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap(), &args[5]),
        "metasplit" => split::run(&md, &args[2], &args[3]),
        "metatuple" => tuple::run(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap(), &args[5], &args[6], args.get(7).map_or(100, |a| a.parse().unwrap())),
        "metarest1" => tuple::rest_cmd(&md, &args[2], &args[3]),
        "metarest" => tuple::run_rest(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap(), &args[5], &args[6]),
        "metaskel" => tuple::skeletons_cmd(&md, &args[2], args.get(3).map(|a| a.parse().unwrap())),
        "metasec" => tuple::sections_cmd(),
        "metaread" => tuple::read_cmd(&md, &args[2], &args[3], args.get(4).is_some_and(|a| a == "inverse")),
        "metastd" => stdcmp::run(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap(), &args[5], &args[6]),
        "metastd1" => stdcmp::explain(&md, &args[2], &args[3]),
        "metaud" => stdord::udcheck(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap()),
        "metastdlist" => stdord::run(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap(), args[5].parse().unwrap(), &args[6]),
        "metaway" => stdcmp::way(&md),
        "metaannot" => annot::run(&md, &args[2..]),
        "metapairs" => annot::run_pairs(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap(), &args[5]),
        "metax2" => tuple::explain(&md, &args[2], &args[3], args.get(4).map(|a| a.parse().unwrap())),
        "metax" => meta::explain(&md, &args[2], args.get(3).map(|a| a.parse().unwrap())),
        "metarun" => {
            // drvar metarun N SEED M OUTPREFIX [niss] : the search-meta records for N random M-qt DRs
            meta::run(&md, args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap(), &args[5], args.len() > 6);
        }
        "lsb" => {
            // drvar lsb "SCRAMBLE" "PREFIX" : prefix length + optimal leave-slice finish after it (a floor for any
            // solution that keeps the prefix)
            let x = word(&crate::core::parse_moves(args[2].as_bytes(), 64).unwrap());
            let p = crate::core::parse_moves(args[3].as_bytes(), 64).unwrap();
            println!("{} + {} = {}", p.len(), md.lsopt(&x.mul(word(&p))), p.len() + md.lsopt(&x.mul(word(&p))) as usize);
        }
        "crisp3" => {
            // drvar crisp3 N SEED OUT.tsv : the 3qt version and the skeleton comparison (leave-slice, <= 4qt)
            let n: usize = args[2].parse().unwrap();
            let mut rng = Rng(args[3].parse().unwrap());
            let hb = crisp3::HBalls::new(&md, 6);
            let xs: Vec<St> = (0..n).map(|_| random_dr(&md, &mut rng)).collect();
            let done = std::sync::atomic::AtomicUsize::new(0);
            let res: Vec<Vec<String>> = xs
                .par_iter()
                .enumerate()
                .map(|(i, x)| {
                    let t = std::time::Instant::now();
                    let r = crisp3::analyse(&md, &hb, x, i);
                    let d = done.fetch_add(1, std::sync::atomic::Ordering::Relaxed) + 1;
                    if std::env::var_os("DRVAR_TIME").is_some() {
                        eprintln!("state {i}: {:.2}s", t.elapsed().as_secs_f64());
                    }
                    if d % 50 == 0 {
                        eprintln!("{d} / {n}");
                    }
                    r
                })
                .collect();
            let mut f = std::io::BufWriter::new(std::fs::File::create(&args[4]).unwrap());
            writeln!(f, "# B: id subset mmin optimal_leave_slice some_skeleton_good optimal_solution_in_a_good_skeleton optimal_only_beyond_4qt best_of_good_skeletons skeletons optimal_solution scramble").unwrap();
            writeln!(f, "# T: id subset kind lpre skeleton_best route_extra route_to_3qt best_keeping_route keeps_best keeps_best_if_qt_turned scramble").unwrap();
            for r in res {
                for l in r {
                    writeln!(f, "{l}").unwrap();
                }
            }
        }
        "crispgood" => {
            // drvar crispgood IN.tsv OUT.tsv : for each skeleton of each B line of a crisp3 run, is it good with
            // at most 0 / 1 / 2 extra moves per section before HTR?
            let lines: Vec<String> = std::fs::read_to_string(&args[2]).unwrap().lines().filter(|l| l.starts_with("B\t")).map(String::from).collect();
            let hb = crisp3::HBalls::new(&md, 6);
            let done = std::sync::atomic::AtomicUsize::new(0);
            let n = lines.len();
            let res: Vec<String> = lines
                .par_iter()
                .map(|l| {
                    let f: Vec<&str> = l.split('\t').collect();
                    let x = word(&crate::core::parse_moves(f[11].as_bytes(), 64).unwrap());
                    assert_eq!(md.lsopt(&x) as usize, f[4].parse::<usize>().unwrap(), "scramble does not reproduce the DR");
                    let mut out = Vec::new();
                    for d in f[9].split("; ") {
                        let t: Vec<&str> = d.split(' ').collect();
                        let m: usize = t[0].trim_end_matches("qt").parse().unwrap();
                        let kind = KIND_NAME.iter().position(|&k| k == t[1]).unwrap();
                        let lpre: usize = t[2][1..].parse().unwrap();
                        let (ms, g) = crisp3::goodness(&md, &hb, &x, m, kind, lpre);
                        assert_eq!(g[2], t.contains(&"good"), "slack-2 goodness differs from the crisp3 run");
                        let ms: Vec<String> = ms.iter().map(|v| v.to_string()).collect();
                        out.push(format!("{} {} {} {} {}", d, ms.join(","), g[0] as u8, g[1] as u8, g[2] as u8));
                    }
                    let k = done.fetch_add(1, std::sync::atomic::Ordering::Relaxed) + 1;
                    if k % 50 == 0 {
                        eprintln!("{k} / {n}");
                    }
                    format!("G\t{}\t{}", f[1], out.join("; "))
                })
                .collect();
            let mut fo = std::io::BufWriter::new(std::fs::File::create(&args[3]).unwrap());
            writeln!(fo, "# G: id; per skeleton: crisp3 description, section minimums, good with slack 0 / 1 / 2").unwrap();
            for l in res {
                writeln!(fo, "{l}").unwrap();
            }
        }
        "crispwit" => {
            // drvar crispwit "SCRAMBLE" M KIND : per slack 0/1/2, a zero-bad-slice variant of the skeleton (M, KIND)
            // with every section at most slack over its minimum, plus the skeleton's best leave-slice solution
            let x = word(&crate::core::parse_moves(args[2].as_bytes(), 64).unwrap());
            let m: usize = args[3].parse().unwrap();
            let kind = KIND_NAME.iter().position(|&k| k == args[4]).unwrap();
            let lp = skeleton_lengths(&md, &x, 6);
            let lpre = lp[m][kind] as usize;
            let hb = crisp3::HBalls::new(&md, 6);
            let (ms, g) = crisp3::goodness(&md, &hb, &x, m, kind, lpre);
            println!("skeleton {m}qt {} L{lpre} section minimums {ms:?} good(slack 0,1,2) {g:?}", KIND_NAME[kind]);
            for slack in 0..3 {
                let caps: Vec<usize> = ms.iter().map(|&l| l + slack).collect();
                match crisp3::cheap_witness(&md, &hb, &x, &caps, kind) {
                    None => println!("slack {slack}: none"),
                    Some(w) => {
                        let r = reduce(&w);
                        let z = x.mul(word(&r));
                        let zi = md.hg.get(&z).unwrap();
                        let cs = &md.cases[md.hcase[zi as usize] as usize];
                        let fin = crate::crisp::ls_finish(&md, zi);
                        println!("slack {slack}: {} | {}  ({} + {} = {}; case {} bad {})", wname(&r), wname(&fin), r.len(), fin.len(), r.len() + fin.len(), cs.name(), cs.bad());
                    }
                }
            }
            let lsx = md.lsopt(&x) as usize;
            for bound in lsx..=lsx + 6 {
                let sols = paths(&md, &x, bound, m, |s, _, _| md.lsopt(s) as usize, |_, mm, k, b| mm as usize == m && k as usize == kind && b as usize <= bound);
                if let Some(p) = sols.iter().min_by_key(|p| p.best) {
                    let cs = &md.cases[md.hcase[p.z as usize] as usize];
                    println!("best: {} | {}  ({} + {} = {}; case {} bad {})", wname(&p.w), wname(&crate::crisp::ls_finish(&md, p.z)), p.w.len(), p.best as usize - p.w.len(), p.best, cs.name(), cs.bad());
                    break;
                }
            }
        }
        "crisp3x" => {
            let x = word(&crate::core::parse_moves(args[2].as_bytes(), 64).unwrap());
            let hb = crisp3::HBalls::new(&md, 6);
            for l in crisp3::analyse(&md, &hb, &x, 0) {
                println!("{l}");
            }
        }
        "crispcases" => {
            // per NISS@1qt case: smallest leave-slice finish over its states, minus the kind's HTR corner moves
            let mut mn = vec![255u8; 216];
            let mut cnt_long = vec![0usize; 216];
            for (i, &c) in md.hcase.iter().enumerate() {
                let k = md.cases[c as usize].kind as usize;
                let e = md.fin[i].saturating_sub(LC[k]);
                mn[c as usize] = mn[c as usize].min(e);
                if e >= 3 {
                    cnt_long[c as usize] += 1;
                }
            }
            for (c, cs) in md.cases.iter().enumerate() {
                println!("{}\t{}\t{}\t{}\t{}\t{}", cs.name(), cs.bad(), cs.heur, cs.min_d3 - LC[cs.kind as usize], mn[c], cnt_long[c]);
            }
        }
        "crispx" => {
            let x = word(&crate::core::parse_moves(args[2].as_bytes(), 64).unwrap());
            println!("subset {}  optimal leave-slice {}", md.subset(&x), md.lsopt(&x));
            for l in crisp::analyse(&md, &hc, &jcl, &x, 0, &[2, 3, 4, 5, 6]) {
                println!("{l}");
            }
        }
        "explain" => {
            // drvar explain "SCRAMBLE" : the scramble's DR (DR moves only), its skeletons and qualifying variants
            let mv = crate::core::parse_moves(args[2].as_bytes(), 64).unwrap_or_else(|| fatal!("not DR moves"));
            let x = word(&mv);
            let lp = skeleton_lengths(&md, &x, MMAX);
            println!("subset {}  optimal finish {}", md.subset(&x), md.opt(&x));
            for (m, row) in lp.iter().enumerate() {
                for k in 0..6 {
                    if row[k] != 255 && m <= 4 {
                        println!("  skeleton family: {m} qt, {} corners, shortest corner path to HTR {} moves (+{} for the corner finish)", KIND_NAME[k], row[k], LC[k]);
                    }
                }
            }
            for l in analyse(&md, &hc, &jcl, &x, 0) {
                println!("  {l}");
            }
        }
        "check" => {
            // the path enumeration, unrestricted, must reproduce the exact optimal finish
            let n: usize = args[2].parse().unwrap();
            let mut rng = Rng(args[3].parse().unwrap());
            for i in 0..n {
                let x = random_dr(&md, &mut rng);
                let opt = md.opt(&x) as usize;
                let sols = paths(&md, &x, opt, 12, |s, _, _| md.opt(s) as usize, |_, _, _, b| b as usize <= opt);
                let best = sols.iter().map(|p| p.best as usize).min().unwrap();
                assert_eq!(best, opt, "state {i}");
                // and reduce() of a path followed by its inverse is empty
                let w = &sols[0].w;
                let mut ww = w.clone();
                ww.extend(w.iter().rev().map(|&m| [2, 1, 0, 5, 4, 3, 6, 7, 8, 9][m]));
                assert!(reduce(&ww).is_empty());
                if i % 10 == 0 {
                    eprintln!("{i}: opt {opt}, {} optimal paths", sols.iter().filter(|p| p.best as usize == opt).count());
                }
            }
            println!("check ok: {n} states");
            // positive controls: a path with a J block put into one of its sections must be found one insertion
            // away, and a skeleton with J blocks put in must be a variant of it
            let blocks: [&[usize]; 8] = [&[6, 7], &[8, 9], &[1, 4], &[6, 8, 6], &[8, 6, 8], &[6, 1, 6], &[6, 1, 6, 1, 6, 1], &[7, 8, 6]];
            let mut rng = Rng(99);
            let (mut tried, mut found, mut vt, mut vf) = (0, 0, 0, 0);
            for _ in 0..200 {
                let x = random_dr(&md, &mut rng);
                let opt = md.opt(&x) as usize;
                let sols = paths(&md, &x, opt + 1, 12, |s, _, _| md.opt(s) as usize, |_, _, _, b| b as usize <= opt + 1);
                let p = &sols[rng.below(sols.len() as u64) as usize];
                let qpos: Vec<usize> = (0..p.w.len()).filter(|&i| is_qt(p.w[i])).collect();
                let at = rng.below(qpos[qpos.len() - 1] as u64 + 1) as usize; // anywhere before the last quarter turn
                let blk = blocks[rng.below(8) as usize];
                let mut w2 = p.w[..at].to_vec();
                w2.extend_from_slice(blk);
                w2.extend_from_slice(&p.w[at..]);
                let w2 = reduce(&w2);
                if w2.iter().filter(|&&mv| is_qt(mv)).count() != qpos.len() || md.hg.get(&x.mul(word(&w2))).is_none() {
                    continue;
                }
                tried += 1;
                if one_insertion(&md, &p.w, &[(word(&w2), w2.len())], false).is_some() {
                    found += 1;
                }
                // variant control on corners: the path p as a "skeleton" (its corner sections), w2 a variant of it
                let sk = make_skeleton(&md, &hc, &jcl, p.w.clone(), 0);
                vt += 1;
                if is_variant(&hc, &sk, &w2) {
                    vf += 1;
                }
            }
            println!("one-insertion control: found {found} of {tried}; variant control: {vf} of {vt}");
            assert!(found == tried && vf == vt);
        }
        _ => fatal!("unknown command"),
    }
}
