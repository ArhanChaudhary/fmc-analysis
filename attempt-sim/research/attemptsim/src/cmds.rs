//! Subcommands: selftest, run (the experiment runner), exhaust (the answer key), cmpgaps (cross-check with cubelib's
//! lists from the gaps study).

use crate::conf::{load_costs, load_policies, parse_overrides, Policy};
use crate::ctx::*;
use crate::cubie::SOLVED;
use crate::line::all_drs;
use crate::solver::{Attempt, Outcome, World, KIND_NAME};
use rayon::prelude::*;
use std::collections::{HashMap, HashSet};
use std::io::Write;

pub struct Args {
    pub pos: Vec<String>,
    pub opt: HashMap<String, String>,
    pub sets: Vec<String>,
}
pub fn args(a: &[String]) -> Args {
    let mut r = Args { pos: Vec::new(), opt: HashMap::new(), sets: Vec::new() };
    let mut k = 0;
    while k < a.len() {
        if a[k] == "--set" {
            r.sets.push(a[k + 1].clone());
            k += 2;
        } else if let Some(name) = a[k].strip_prefix("--") {
            if k + 1 < a.len() && !a[k + 1].starts_with("--") {
                r.opt.insert(name.to_string(), a[k + 1].clone());
                k += 2;
            } else {
                r.opt.insert(name.to_string(), "1".to_string());
                k += 1;
            }
        } else {
            r.pos.push(a[k].clone());
            k += 1;
        }
    }
    r
}
impl Args {
    pub fn get(&self, k: &str) -> Option<&str> {
        self.opt.get(k).map(|s| s.as_str())
    }
    pub fn need(&self, k: &str) -> &str {
        self.get(k).unwrap_or_else(|| fatal!("missing --{}", k))
    }
    pub fn num(&self, k: &str, d: usize) -> usize {
        self.get(k).map_or(d, |v| v.parse().unwrap_or_else(|_| fatal!("--{}: not a number", k)))
    }
}

pub fn read_scrambles(path: &str, first: usize, count: usize) -> Vec<(u64, Vec<u8>)> {
    let txt = std::fs::read_to_string(path).unwrap_or_else(|e| fatal!("cannot read {}: {}", path, e));
    txt.lines()
        .filter(|l| !l.trim().is_empty() && !l.starts_with('#'))
        .enumerate()
        .skip(first)
        .take(count)
        .map(|(k, l)| {
            // "id<TAB>scramble" or just the scramble
            let body = l.rsplit('\t').next().unwrap();
            (k as u64, parse(body))
        })
        .collect()
}

pub fn selftest() {
    let c = Ctx::new(None);
    // EO-kept distance histogram: Cale's table (also proved in the EO-switch study's Lean project)
    let mut h = [0u64; 16];
    for &d in &c.drdist {
        h[d as usize] += 1;
    }
    let want = [1u64, 2, 17, 134, 1065, 8190, 54694, 267576, 560568, 187204, 3114];
    assert_eq!(&h[..11], &want, "EO-kept DR distance histogram");
    println!("drdist histogram ok: {:?}", &h[..11]);
    let mut he = [0u64; 9];
    for &d in &c.eodist {
        he[d as usize] += 1;
    }
    println!("eodist histogram: {:?} (mean {:.3})", &he[..8], c.eodist.iter().map(|&d| d as f64).sum::<f64>() / 2048.0);
    println!("all DR states: mean optimal finish {:.4}; P(<=10) {:.4} P(<=11) {:.4} P(<=12) {:.4}", c.all_mean, c.all_cdf[10], c.all_cdf[11], c.all_cdf[12]);
    // the DR moves of the view agree with judging-a-dr's model, and cancel() does not change what a sequence does
    let mut rng = 12345u64;
    let mut next = |n: usize| {
        rng = crate::rngx::mix(rng);
        (rng % n as u64) as usize
    };
    for _ in 0..2000 {
        let seq: Vec<usize> = (0..12).map(|_| next(10)).collect();
        let view: Vec<u8> = seq.iter().map(|&m| DRMOVE[m]).collect();
        let st = c.apply(&SOLVED, &view);
        let got = c.dr_coords(&st).expect("DR state");
        let mut want = (0usize, 0usize, 0usize);
        for &m in &seq {
            want = c.dm.mv(m, want);
        }
        assert_eq!(got, want, "DR coordinates");
        assert_eq!(c.dr_coords(&st.inverse()).unwrap(), c.dr_inv(got), "inverse");
        let any: Vec<u8> = (0..25).map(|_| next(18) as u8).collect();
        assert_eq!(c.apply(&SOLVED, &any), c.apply(&SOLVED, &cancel(&any)), "cancel");
        let cc = cancel(&any);
        for w in cc.windows(2) {
            assert!(w[0] / 3 != w[1] / 3, "cancel left two turns of one face");
        }
        // N, I convention: I^-1 S N solved <=> S N I^-1 solved
        let s = c.apply(&SOLVED, &any);
        let n: Vec<u8> = (0..5).map(|_| next(18) as u8).collect();
        let i: Vec<u8> = (0..5).map(|_| next(18) as u8).collect();
        let x = c.state_ni(&s, &n, &i);
        let mut lin = n.clone();
        lin.extend(invert(&i));
        let y = c.apply(&s, &lin);
        // x = I^-1 S N and y = S N I^-1 are conjugate: x solved iff y solved; check via x * I^-1 == I^-1 * y
        let pre = c.apply(&SOLVED, &invert(&i));
        assert_eq!(c.apply(&x, &invert(&i)), pre.then(&y), "NISS convention");
    }
    println!("selftest ok");
}

fn summary(name: &str, v: &[&Outcome]) -> String {
    let n = v.len() as f64;
    let solved: Vec<f64> = v.iter().filter(|o| o.len > 0).map(|o| o.len as f64).collect();
    let k = solved.len() as f64;
    let mean = solved.iter().sum::<f64>() / k.max(1.0);
    let var = solved.iter().map(|x| (x - mean) * (x - mean)).sum::<f64>() / (k - 1.0).max(1.0);
    let share = |f: &dyn Fn(&Outcome) -> bool| v.iter().filter(|o| f(o)).count() as f64 / n;
    let avg = |f: &dyn Fn(&Outcome) -> f64| v.iter().map(|o| f(o)).sum::<f64>() / n;
    format!(
        "{:<28} n {:>5}  mean {:.3} +- {:.3}  dnf {:.2}%  sub20 {:.1}%  <=22 {:.1}%  | eos {:.1} drs {:.1} fin {:.1} bestDR {:.2} | min eo {:.1} dr {:.1} fin {:.1} write {:.1} | t_end {:.0}s",
        name, v.len(), mean, (var / k.max(1.0)).sqrt(), 100.0 * share(&|o| o.len == 0),
        100.0 * share(&|o| o.len > 0 && o.len < 20), 100.0 * share(&|o| o.len > 0 && o.len <= 22),
        avg(&|o| o.eos_found as f64), avg(&|o| o.drs_found as f64), avg(&|o| o.drs_finished as f64),
        v.iter().filter(|o| o.best_dr > 0).map(|o| o.best_dr as f64).sum::<f64>() / v.iter().filter(|o| o.best_dr > 0).count().max(1) as f64,
        avg(&|o| (o.time[0] + o.time[1] + o.time[2]) as f64) / 60000.0,
        avg(&|o| (o.time[3] + o.time[4] + o.time[5] + o.time[6]) as f64) / 60000.0,
        avg(&|o| (o.time[7] + o.time[8] + o.time[9]) as f64) / 60000.0,
        avg(&|o| o.time[10] as f64) / 60000.0,
        avg(&|o| o.t_end as f64) / 1000.0,
    )
}

/// attemptsim run --costs F --policies F --scrambles F [--first A] [--count N] [--seed S] --out OUT.tsv
///                --exact TABLE [--log FILE --logn K] [--set cost.KEY=V | human.KEY=V]...
pub fn run(a: &Args) {
    let (costs, human) = load_costs(a.need("costs"), &parse_overrides(&a.sets));
    let pols: Vec<Policy> = load_policies(a.need("policies"));
    let scr = read_scrambles(a.need("scrambles"), a.num("first", 0), a.num("count", 1000));
    let seed = a.num("seed", 1) as u64;
    let c = Ctx::new(Some(a.need("exact")));
    let lists = crate::finish::load_checklists(&c);
    let max_eo = pols.iter().map(|p| p.eo_len.max(p.eo_len_poor)).max().unwrap().clamp(1, 7);
    let logn = a.num("logn", 0);
    let t0 = std::time::Instant::now();
    // per scramble: (bad edges of the three axes smallest first, shortest EO, EOs of <= 4 all kinds, linear only)
    let res: Vec<(String, Vec<Outcome>)> = scr
        .par_iter()
        .map(|(id, moves)| {
            let w = World::new(&c, &lists, *id, seed, moves, max_eo);
            let mut b = w.bad;
            b.sort();
            let feat = format!("{}-{}-{}\t{}\t{}\t{}", b[0], b[1], b[2], w.eo_min, w.n_eo4, w.n_eo4_lin);
            // this attempt's form: fixed per scramble, the same under every policy
            let hum = human.on_form(crate::rngx::normal(crate::rngx::h2(w.seed, 0xF0F0)));
            (feat, pols.iter().map(|p| Attempt::new(&w, &costs, &hum, p, (*id as usize) < a.num("first", 0) + logn).run()).collect())
        })
        .collect();
    let feats: Vec<&String> = res.iter().map(|r| &r.0).collect();
    let res: Vec<&Vec<Outcome>> = res.iter().map(|r| &r.1).collect();
    let secs = t0.elapsed().as_secs_f64();
    let mut out = std::io::BufWriter::new(std::fs::File::create(a.need("out")).unwrap_or_else(|e| fatal!("{}", e)));
    write!(out, "policy\tscr\tbad\teo_min\tn_eo4\tn_eo4_lin\tlen\tt_end_ms\tbest_found\teos\tdrs\tdrs_finished\tbest_dr\tfirst_sol_ms\tfirst_sol_len\tres_dr_len\tres_subset\tres_exact\tres_fin\tres_dr_ms\tres_sol_ms\tlast_eo_ms\tlast_dr_ms\toracle_page\tbanks").unwrap();
    for k in KIND_NAME {
        write!(out, "\tn_{}", k).unwrap();
    }
    for k in KIND_NAME {
        write!(out, "\tms_{}", k).unwrap();
    }
    writeln!(out, "\treplay_fail\tsolution").unwrap();
    let mut fails = 0u32;
    for (pi, p) in pols.iter().enumerate() {
        for (si, (id, _)) in scr.iter().enumerate() {
            let o = &res[si][pi];
            fails += o.replay_fail;
            write!(
                out, "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
                p.name, id, feats[si], o.len, o.t_end, o.best_found, o.eos_found, o.drs_found, o.drs_finished, o.best_dr, o.first_sol_t, o.first_sol_len,
                o.res_dr_len, if o.len > 0 { c.dm.cls.sub48_name[o.res_sub as usize].as_str() } else { "-" }, o.res_exact, o.res_fin,
                o.res_dr_t, o.res_sol_t, o.last_eo_t, o.last_dr_t, o.oracle_page, o.banks.len()
            )
            .unwrap();
            for k in 0..11 {
                write!(out, "\t{}", o.count[k]).unwrap();
            }
            for k in 0..11 {
                write!(out, "\t{}", o.time[k]).unwrap();
            }
            writeln!(out, "\t{}\t{}", o.replay_fail, text(&o.moves)).unwrap();
        }
    }
    drop(out);
    if let Some(lp) = a.get("log") {
        let mut lf = std::io::BufWriter::new(std::fs::File::create(lp).unwrap());
        for (pi, p) in pols.iter().enumerate() {
            for (si, (id, moves)) in scr.iter().enumerate() {
                let o = &res[si][pi];
                if o.log.is_empty() {
                    continue;
                }
                let steps: Vec<String> = o.log.iter().map(|(k, ms)| format!("[{},{}]", k, ms)).collect();
                let sols: Vec<String> = o.sols.iter().map(|(t, l, m)| format!("[{},{},\"{}\"]", t, l, text(m))).collect();
                let banks: Vec<String> = o.banks.iter().map(|(t, l)| format!("[{},{}]", t, l)).collect();
                writeln!(
                    lf, "{{\"policy\":\"{}\",\"scr\":{},\"scramble\":\"{}\",\"seed\":{},\"budget_ms\":{},\"len\":{},\"solution\":\"{}\",\"t_end_ms\":{},\"steps\":[{}],\"sols\":[{}],\"banks\":[{}]}}",
                    p.name, id, text(moves), seed, (costs.budget * 1000.0).round() as u64, o.len, text(&o.moves), o.t_end, steps.join(","), sols.join(","), banks.join(",")
                )
                .unwrap();
            }
        }
    }
    for (pi, p) in pols.iter().enumerate() {
        let v: Vec<&Outcome> = res.iter().map(|r| &r[pi]).collect();
        println!("{}", summary(&p.name, &v));
    }
    eprintln!("{} scrambles x {} policies in {:.1} s; replay failures: {}", scr.len(), pols.len(), secs, fails);
    if fails > 0 {
        std::process::exit(1);
    }
}

/// The trailing run of one side's moves about the axis of its last move, quarter turns made clockwise
/// (the gaps study's way of writing a DR once: judging-a-dr many_examples.canon).
fn canon_side(q: &[u8]) -> Vec<u8> {
    let mut v = q.to_vec();
    let Some(&l) = v.last() else { return v };
    let ax = FACE_AXIS[(l / 3) as usize];
    let mut k = v.len();
    while k > 0 && FACE_AXIS[(v[k - 1] / 3) as usize] == ax {
        k -= 1;
        if v[k] % 3 != 1 {
            v[k] = 3 * (v[k] / 3);
        }
    }
    v
}

pub struct KeyDr {
    pub x: usize,
    pub len: usize,
    pub eo_len: usize,
    pub n: Vec<u8>,
    pub i: Vec<u8>,
    pub st: (usize, usize, usize),
}

/// Every EO-first DR of a scramble: EO of at most `eo_max` (normal, inverse or NISS), then EO-keeping turns on one
/// side, at most `cap` turns in all.  One entry per sequence pair.
pub fn key_drs(c: &Ctx, w: &World, eo_max: usize, cap: usize) -> Vec<KeyDr> {
    let mut out = Vec::new();
    for g in &w.eos {
        if g.len as usize > eo_max || g.len as usize > cap {
            continue;
        }
        let y = g.axis as usize;
        for root in &g.roots {
            let x0 = c.state_ni(&w.s, &root.n, &root.i);
            for x in 0..3 {
                if x == y {
                    continue;
                }
                let rot = c.rot_pair[x][y];
                let v = c.m.conj(&x0, rot);
                let lastv = |q: &[u8]| q.last().map_or(NONE, |&mv| c.vmove[rot][mv as usize]);
                all_drs(c, &v, [lastv(&root.n), lastv(&root.i)], cap - g.len as usize, &mut |side, path| {
                    let ownp: Vec<u8> = path.iter().map(|&mv| c.umove[rot][mv as usize]).collect();
                    let (mut n, mut i) = (root.n.clone(), root.i.clone());
                    if side == 0 {
                        n.extend(&ownp);
                    } else {
                        i.extend(&ownp);
                    }
                    let st = c.dr_coords(&c.m.conj(&c.state_ni(&w.s, &n, &i), rot)).expect("DR");
                    out.push(KeyDr { x, len: n.len() + i.len(), eo_len: g.len as usize, n, i, st });
                });
            }
        }
    }
    out
}

/// attemptsim exhaust --scrambles F [--first A] [--count N] --exact TABLE [--eo 5] [--cap 11] --out OUT.tsv
/// The answer key (computer only): every EO-first DR, each finished optimally (exact table).
pub fn exhaust(a: &Args) {
    let scr = read_scrambles(a.need("scrambles"), a.num("first", 0), a.num("count", 1000));
    let (eo_max, cap) = (a.num("eo", 5), a.num("cap", 11));
    let c = Ctx::new(Some(a.need("exact")));
    let lists: Vec<Vec<crate::finish::Step>> = Vec::new();
    let rows: Vec<String> = scr
        .par_iter()
        .map(|(id, moves)| {
            let w = World::new(&c, &lists, *id, 0, moves, eo_max);
            let drs = key_drs(&c, &w, eo_max, cap);
            // one entry per (axis, state): the shortest way to it
            // (a DR and its twin, the last turn made the other way, are two states; the state is named up to the
            // symmetries of its axis, so that the EO it came through does not matter)
            let mut best: HashMap<(usize, (usize, usize, usize)), (usize, usize)> = HashMap::new();
            for d in &drs {
                let e = best.entry((d.x, c.dr_canon(d.st))).or_insert((d.len, d.eo_len));
                if d.len < e.0 {
                    *e = (d.len, d.eo_len);
                }
            }
            let mut nlen = [0u32; 16];
            let mut tot = [99u32; 16]; // best total with DRs of at most L, L = index
            let mut tot4 = [99u32; 16]; // the same through EOs of at most 4
            let mut bestdr = 99usize;
            for (&(_, st), &(len, eol)) in &best {
                nlen[len] += 1;
                bestdr = bestdr.min(len);
                let t = len as u32 + c.dm.depth(st.0, st.1, st.2) as u32;
                for l in len..16 {
                    tot[l] = tot[l].min(t);
                    if eol <= 4 {
                        tot4[l] = tot4[l].min(t);
                    }
                }
            }
            let s = |v: &[u32]| v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join("\t");
            format!("{}\t{}\t{}\t{}\t{}\t{}\t{}", id, w.eos.iter().filter(|g| g.len <= 4).count(), w.eos.len(), bestdr, s(&nlen[4..=cap]), s(&tot[8..=cap]), s(&tot4[8..=cap]))
        })
        .collect();
    let mut out = std::io::BufWriter::new(std::fs::File::create(a.need("out")).unwrap());
    let cols = |p: &str, lo: usize| (lo..=cap).map(|l| format!("{}{}", p, l)).collect::<Vec<_>>().join("\t");
    writeln!(out, "scr\teo_groups_le4\teo_groups\tbest_dr\t{}\t{}\t{}", cols("drs_len", 4), cols("best_total_dr_le", 8), cols("best_total_eo4_dr_le", 8)).unwrap();
    for r in rows {
        writeln!(out, "{}", r).unwrap();
    }
}

/// attemptsim cmpgaps --scrambles F --pop POP_RAW.tsv [--count N]
/// The DRs of `key_drs` (EO <= 5 with NISS, total <= 11) against cubelib-cli's lists in the gaps study, as sets of
/// (axis, DR state) per scramble, each DR written the gaps way (trailing quarter turns clockwise).
pub fn cmpgaps(a: &Args) {
    let n = a.num("count", 200);
    let scr = read_scrambles(a.need("scrambles"), 0, n);
    let c = Ctx::new(None);
    let lists: Vec<Vec<crate::finish::Step>> = Vec::new();
    let mut theirs: Vec<HashMap<(usize, (usize, usize, usize)), usize>> = vec![HashMap::new(); n];
    let txt = std::fs::File::open(a.need("pop")).unwrap_or_else(|e| fatal!("{}", e));
    use std::io::BufRead;
    for line in std::io::BufReader::new(txt).lines() {
        let line = line.unwrap();
        if line.starts_with('#') || line.starts_with("scr\t") {
            continue;
        }
        let p: Vec<&str> = line.split('\t').collect();
        let k: usize = p[0].parse().unwrap();
        if k >= n {
            continue;
        }
        let x = match p[1] {
            "R/L" => 0,
            "U/D" => 1,
            _ => 2,
        };
        let st = (p[9].parse().unwrap(), p[10].parse().unwrap(), p[11].parse().unwrap());
        let len: usize = p[3].parse().unwrap();
        let e = theirs[k].entry((x, c.dr_canon(st))).or_insert(len);
        *e = (*e).min(len);
    }
    let res: Vec<(usize, usize, usize, usize, usize)> = scr
        .par_iter()
        .map(|(id, moves)| {
            let w = World::new(&c, &lists, *id, 0, moves, 5);
            let mut mine: HashMap<(usize, (usize, usize, usize)), usize> = HashMap::new();
            for d in key_drs(&c, &w, 5, 11) {
                let (n2, i2) = (canon_side(&d.n), canon_side(&d.i));
                // any rotation that puts the DR axis on U/D will do: the name is taken up to symmetry
                let y = (0..3).find(|&y| y != d.x).unwrap();
                let st = c.dr_coords(&c.m.conj(&c.state_ni(&w.s, &n2, &i2), c.rot_pair[d.x][y])).expect("canonical DR");
                let e = mine.entry((d.x, c.dr_canon(st))).or_insert(d.len);
                *e = (*e).min(d.len);
            }
            let t = &theirs[*id as usize];
            let a: HashSet<_> = t.keys().collect();
            let b: HashSet<_> = mine.keys().collect();
            if std::env::var("CMP_DUMP").map_or(false, |v| v.parse::<u64>().ok() == Some(*id)) {
                for d in key_drs(&c, &w, 5, 11) {
                    let (n2, i2) = (canon_side(&d.n), canon_side(&d.i));
                    let y = (0..3).find(|&y| y != d.x).unwrap();
                    let st = c.dr_coords(&c.m.conj(&c.state_ni(&w.s, &n2, &i2), c.rot_pair[d.x][y])).unwrap();
                    if !t.contains_key(&(d.x, c.dr_canon(st))) {
                        println!("ONLY-MINE axis {} len {} eo {}: {} ({})", AXIS_NAME[d.x], d.len, d.eo_len, text(&d.n), text(&d.i));
                    }
                }
                for k in a.difference(&b) {
                    println!("ONLY-CUBELIB axis {} state {:?} len {}", AXIS_NAME[k.0], k.1, t[*k]);
                }
            }
            let only_t = a.difference(&b).count();
            let only_m = b.difference(&a).count();
            let lendiff = a.intersection(&b).filter(|k| t[**k] != mine[**k]).count();
            (a.len(), b.len(), only_t, only_m, lendiff)
        })
        .collect();
    let s = res.iter().fold((0, 0, 0, 0, 0), |x, y| (x.0 + y.0, x.1 + y.1, x.2 + y.2, x.3 + y.3, x.4 + y.4));
    println!("{} scrambles: cubelib (gaps) {} DRs, attemptsim {} DRs; only in cubelib {}, only in attemptsim {}, same DR with another length {}", n, s.0, s.1, s.2, s.3, s.4);
    for (k, r) in res.iter().enumerate() {
        if r.2 + r.3 + r.4 > 0 {
            println!("  scramble {}: cubelib {} mine {} only-cubelib {} only-mine {} lendiff {}", k, r.0, r.1, r.2, r.3, r.4);
        }
    }
    if s.2 + s.3 + s.4 > 0 {
        std::process::exit(1);
    }
}

/// attemptsim routecurve --exact TABLE [--count N] [--seed S]
/// The checklists as the simulator uses them, against htr-routes' own numbers: on uniform states of each of the 48
/// subsets, the share where one of the first k routes finds the optimal finish (and one within +1, +2).
pub fn routecurve(a: &Args) {
    let c = Ctx::new(Some(a.need("exact")));
    let lists = crate::finish::load_checklists(&c);
    let n = a.num("count", 300);
    let sampler = crate::model::Sampler::new(&c.dm);
    let nsub = c.dm.cls.sub48_name.len();
    println!("subset\tn\tk\tclass\tcum_opt\tcum_p1\tcum_p2\thtr_routes_cum_opt\tmean_ms_per_state");
    let txt = std::fs::read_to_string(format!("{}/checklist.tsv", data_dir())).unwrap();
    let theirs: Vec<Vec<&str>> = txt.lines().skip(1).map(|l| l.split('\t').collect()).collect();
    for sub in 0..nsub {
        let t0 = std::time::Instant::now();
        let res: Vec<Vec<u8>> = (0..n)
            .into_par_iter()
            .map(|i| {
                let mut rng = crate::model::Rng(a.num("seed", 1) as u64 ^ ((sub as u64) << 40) ^ (i as u64).wrapping_mul(0x9E37_79B9_7F4A_7C15));
                let x = sampler.draw(&c.dm, sub, &mut rng);
                let rt = crate::finish::route_table(&c, x);
                // best excess over the optimum after the first k routes (9 = nothing found)
                let mut best = 9u8;
                lists[sub]
                    .iter()
                    .map(|st| {
                        if let Some((len, _)) = rt.best.get(&st.key) {
                            best = best.min(len - rt.d);
                        }
                        best
                    })
                    .collect()
            })
            .collect();
        let ms = t0.elapsed().as_secs_f64() * 1000.0 / n as f64 * rayon::current_num_threads() as f64;
        for k in 0..lists[sub].len() {
            let sh = |lim: u8| res.iter().filter(|r| r[k] <= lim).count() as f64 / n as f64;
            let th = theirs.iter().find(|r| r[0] == c.dm.cls.sub48_name[sub] && r[1].parse::<usize>().unwrap() == k + 1).map_or("", |r| r[4]);
            println!("{}\t{}\t{}\t{}\t{:.4}\t{:.4}\t{:.4}\t{}\t{:.1}", c.dm.cls.sub48_name[sub], n, k + 1, lists[sub][k].name, sh(0), sh(1), sh(2), th, ms);
        }
    }
}

/// attemptsim export --out DIR [--scrambles F --count N --eo K --cap L]
/// What the Lean project checks, as plain text:
///   model.txt       the 18 face turns as the simulator applies them (corner places, twists added, edge places, flips
///                   added), the rotations of the six views with their move relabelling, the DR-move table
///   eodist.txt      2,048 values; eo_mv.txt, co_mv.txt, sl_mv.txt: coordinate move tables (one row per coordinate)
///   drdist.u8       1,082,565 bytes, index co * 495 + sl
///   htrdist.txt     420 rows x 70: fewest DR moves to HTR per (corner coset, edge pattern); cosets.txt: the coset
///                   and pattern of every corner / edge permutation rank is NOT exported (40,320 values each) but
///                   their representatives are
///   cands_eo.tsv    with --scrambles: every EO candidate (scramble, axis, kind, normal moves, inverse moves)
///   cands_dr.tsv    with --scrambles: every EO-first DR of at most L moves (scramble, axis, length, N, I)
pub fn export(a: &Args) {
    let c = Ctx::new(None);
    let dir = a.need("out");
    std::fs::create_dir_all(dir).unwrap();
    let w = |name: &str, s: String| std::fs::write(format!("{}/{}", dir, name), s).unwrap();
    let j = |v: &[u8]| v.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(" ");
    let mut m = String::new();
    m.push_str("# faces U D R L F B = 0..5; move = 3 * face + (quarter turns - 1); axes 0 R/L, 1 U/D, 2 F/B\n");
    m.push_str("# a move carries the piece at place i to place d[i]; corner twist += ca[i] (mod 3), edge flip ^= ea[i]\n");
    m.push_str("moves  (18 rows: cd[8] | ca[8] | ed[12] | ea[12])\n");
    for mp in &c.m.moves {
        m.push_str(&format!("{} | {} | {} | {}\n", j(&mp.cd), j(&mp.ca), j(&mp.ed), j(&mp.ea)));
    }
    m.push_str("views  (EO axis y, DR axis x, rotation index, own move of each view move 0..17)\n");
    for y in 0..3 {
        m.push_str(&format!("eo {} - {} | {}\n", y, c.rot_eo[y], j(&c.umove[c.rot_eo[y]])));
    }
    for x in 0..3 {
        for y in 0..3 {
            if x != y {
                m.push_str(&format!("dr {} {} {} | {}\n", y, x, c.rot_pair[x][y], j(&c.umove[c.rot_pair[x][y]])));
            }
        }
    }
    m.push_str("rotations  (24 rows: cd[8] | ca[8] | ed[12] | ea[12] | where axes 0 1 2 go | where faces 0..5 go)\n");
    for r in 0..24 {
        let mp = &c.m.rots[r];
        m.push_str(&format!("{} | {} | {} | {} | {} | {}\n", j(&mp.cd), j(&mp.ca), j(&mp.ed), j(&mp.ea), j(&c.m.rot_axes[r]), j(&c.m.rot_faces[r])));
    }
    m.push_str("drmap  (judging-a-dr corner position -> place; U/D-layer edge position -> place; E-slice position -> place)\n");
    m.push_str(&format!("{}\n{}\n{}\n", j(&c.m.dr_c), j(&c.m.dr_e), j(&c.m.dr_s)));
    m.push_str(&format!("drmoves  (view move of U U2 U' D D2 D' R2 L2 F2 B2)\n{}\n", j(&DRMOVE)));
    m.push_str(&format!("eokeep  (the 14 view moves that keep F/B EO)\n{}\n", j(&EOKEEP)));
    m.push_str(&format!("solved_sl {}\n", c.solved_sl));
    w("model.txt", m);
    w("eodist.txt", c.eodist.iter().map(|x| x.to_string()).collect::<Vec<_>>().join("\n") + "\n");
    let tab = |t: &Vec<[u16; 18]>| t.iter().map(|r| r.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(" ")).collect::<Vec<_>>().join("\n") + "\n";
    w("eo_mv.txt", tab(&c.eo_mv));
    w("co_mv.txt", tab(&c.co_mv));
    w("sl_mv.txt", tab(&c.sl_mv));
    std::fs::write(format!("{}/drdist.u8", dir), &c.drdist).unwrap();
    w("htrdist.txt", c.dm.cls.htr_dist.iter().map(|r| j(r)).collect::<Vec<_>>().join("\n") + "\n");
    w("cosets.txt", format!("corner coset representatives (rank of the corner permutation)\n{}\nedge pattern masks (bit k = U/D-layer position k holds an M-slice edge)\n{}\n",
        c.dm.cls.ccos_rep.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(" "), c.dm.cls.epat_mask.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(" ")));
    if let Some(sp) = a.get("scrambles") {
        let (eo_max, cap) = (a.num("eo", 4), a.num("cap", 9));
        let scr = read_scrambles(sp, a.num("first", 0), a.num("count", 10));
        let lists: Vec<Vec<crate::finish::Step>> = Vec::new();
        let mut fe = String::from("scr\taxis\tkind\tlen\tnormal\tinverse\n");
        let mut fd = String::from("scr\tdr_axis\tlen\tnormal\tinverse\n");
        let mut fs = String::from("scr\tscramble\n");
        for (id, moves) in &scr {
            let wd = World::new(&c, &lists, *id, 0, moves, eo_max);
            fs.push_str(&format!("{}\t{}\n", id, text(moves)));
            for g in &wd.eos {
                for r in &g.roots {
                    fe.push_str(&format!("{}\t{}\t{}\t{}\t{}\t{}\n", id, g.axis, g.kind, g.len, text(&r.n), text(&r.i)));
                }
            }
            for d in key_drs(&c, &wd, eo_max, cap) {
                fd.push_str(&format!("{}\t{}\t{}\t{}\t{}\n", id, d.x, d.len, text(&d.n), text(&d.i)));
            }
        }
        w("cands_scrambles.tsv", fs);
        w("cands_eo.tsv", fe);
        w("cands_dr.tsv", fd);
    }
    println!("exported to {}", dir);
}
