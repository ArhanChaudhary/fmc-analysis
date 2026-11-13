//! Independent recount of cap-8 best insertions on the insertion-cost sample files.
//! Own sticker model, own cancelling, own alg list (meet in the middle over all words of <= 4 turns),
//! brute force over every spot and alg; two comms with nesting allowed. No pruning.
use std::collections::{HashMap, HashSet};
use std::io::{BufRead, Write};

type V = [i32; 3];
type St = [u8; 54];

struct Model {
    stick: Vec<(V, V)>,    // place index -> (cubie position, outward normal)
    moves: Vec<[u8; 54]>,  // move m: sticker at place i goes to place moves[m][i]
    corner_pl: Vec<usize>, // sticker places on corner cubies
    edge_pl: Vec<usize>,
    cf: Vec<[usize; 3]>,   // corner place k (sorted by coords): facelets, U/D first, then clockwise from outside
    ef: Vec<[usize; 2]>,   // edge place k: primary (U/D, else F/B) facelet first
}

fn cross(a: V, b: V) -> V { [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]] }
fn dot(a: V, b: V) -> i32 { a[0]*b[0]+a[1]*b[1]+a[2]*b[2] }
/// rotate v by -90 degrees about unit axis u (clockwise seen from the tip of u)
fn rot_cw(u: V, v: V) -> V { let c = cross(u, v); let d = dot(u, v); [-c[0]+u[0]*d, -c[1]+u[1]*d, -c[2]+u[2]*d] }
/// rotate v by -120 degrees about corner diagonal p (entries +-1): (-v - p x v + p (p.v)) / 2
fn rot_cw3(p: V, v: V) -> V { let c = cross(p, v); let d = dot(p, v); [(-v[0]-c[0]+p[0]*d)/2, (-v[1]-c[1]+p[1]*d)/2, (-v[2]-c[2]+p[2]*d)/2] }

// faces: 0 U(+y) 1 D(-y) 2 R(+x) 3 L(-x) 4 F(+z) 5 B(-z); move m = 3*face + (q-1)
const FAX: [(usize, i32); 6] = [(1, 1), (1, -1), (0, 1), (0, -1), (2, 1), (2, -1)];
const NAMES: [&str; 18] = ["U","U2","U'","D","D2","D'","R","R2","R'","L","L2","L'","F","F2","F'","B","B2","B'"];

impl Model {
    fn new() -> Model {
        let mut stick = vec![];
        for x in -1..=1 { for y in -1..=1 { for z in -1..=1 {
            let p = [x, y, z];
            for a in 0..3 { if p[a] != 0 { let mut n = [0; 3]; n[a] = p[a]; stick.push((p, n)); } }
        }}}
        assert_eq!(stick.len(), 54); // centres included
        let idx = |s: &Vec<(V, V)>, p: V, n: V| s.iter().position(|&(q, m)| q == p && m == n).unwrap();
        let mut moves = vec![];
        for f in 0..6 {
            let (a, sg) = FAX[f]; let mut u = [0; 3]; u[a] = sg;
            for q in 1..=3 {
                let mut m = [0u8; 54];
                for i in 0..54 {
                    let (mut p, mut n) = stick[i];
                    if p[a] == sg { for _ in 0..q { p = rot_cw(u, p); n = rot_cw(u, n); } }
                    m[i] = idx(&stick, p, n) as u8;
                }
                moves.push(m);
            }
        }
        let nz = |p: V| p.iter().filter(|&&c| c != 0).count();
        let mut cubies: Vec<V> = stick.iter().map(|s| s.0).collect(); cubies.sort(); cubies.dedup();
        let corners: Vec<V> = cubies.iter().cloned().filter(|&p| nz(p) == 3).collect();
        let edges: Vec<V> = cubies.iter().cloned().filter(|&p| nz(p) == 2).collect();
        let mut cf = vec![]; for &p in &corners {
            let ud = [0, p[1], 0]; let a = rot_cw3(p, ud); let b = rot_cw3(p, a);
            cf.push([idx(&stick, p, ud), idx(&stick, p, a), idx(&stick, p, b)]);
        }
        let mut ef = vec![]; for &p in &edges {
            let pri = if p[1] != 0 { [0, p[1], 0] } else { [0, 0, p[2]] };
            let oth = [p[0] - pri[0], p[1] - pri[1], p[2] - pri[2]];
            ef.push([idx(&stick, p, pri), idx(&stick, p, oth)]);
        }
        let corner_pl = (0..54).filter(|&i| nz(stick[i].0) == 3).collect();
        let edge_pl = (0..54).filter(|&i| nz(stick[i].0) == 2).collect();
        Model { stick, moves, corner_pl, edge_pl, cf, ef }
    }
    fn apply(&self, s: &St, m: u8) -> St { let mv = &self.moves[m as usize]; let mut t = [0u8; 54]; for i in 0..54 { t[mv[i] as usize] = s[i]; } t }
    fn run(&self, s: &St, w: &[u8]) -> St { let mut s = *s; for &m in w { s = self.apply(&s, m); } s }
}
fn solved() -> St { let mut s = [0u8; 54]; for i in 0..54 { s[i] = i as u8; } s }
/// state of g then h
fn mul(g: &St, h: &St) -> St { let mut t = [0u8; 54]; for i in 0..54 { t[i] = g[h[i] as usize]; } t }
fn inverse(g: &St) -> St { let mut t = [0u8; 54]; for i in 0..54 { t[g[i] as usize] = i as u8; } t }
fn invw(w: &[u8]) -> Vec<u8> { w.iter().rev().map(|&m| 3 * (m / 3) + (2 - m % 3)).collect() }

/// normal form: one syllable per run of turns about one axis, quarter turns of each face mod 4
fn normal(w: &[u8]) -> Vec<u8> {
    let mut st: Vec<(u8, u8, u8)> = Vec::with_capacity(w.len());
    for &m in w {
        let f = m / 3; let a = f / 2; let q = m % 3 + 1; let first = f % 2 == 0;
        if let Some(top) = st.last_mut() {
            if top.0 == a {
                if first { top.1 = (top.1 + q) % 4 } else { top.2 = (top.2 + q) % 4 }
                if top.1 == 0 && top.2 == 0 { st.pop(); }
                continue;
            }
        }
        st.push((a, if first { q } else { 0 }, if first { 0 } else { q }));
    }
    let mut out = vec![];
    for (a, p, q) in st { if p != 0 { out.push(6 * a + p - 1); } if q != 0 { out.push(6 * a + 3 + q - 1); } }
    out
}
fn nlen(w: &[u8]) -> usize { normal(w).len() }
fn parse(t: &str) -> Vec<u8> { t.split_whitespace().map(|x| NAMES.iter().position(|&n| n == x).unwrap_or_else(|| panic!("{}", x)) as u8).collect() }

fn all_words(k: usize) -> Vec<Vec<u8>> { let mut v = vec![vec![]]; for _ in 0..k { let mut n = vec![]; for w in &v { for m in 0..18u8 { let mut x: Vec<u8> = w.clone(); x.push(m); n.push(x); } } v = n; } v }

/// all normal forms of <= 8 turns leaving the places `fixed` home, not the identity
fn join(md: &Model, fixed: &[usize]) -> Vec<Vec<u8>> {
    let mut halves = vec![]; for k in 0..=4 { halves.extend(all_words(k)); }
    let sol = solved();
    let states: Vec<St> = halves.iter().map(|w| md.run(&sol, w)).collect();
    let key = |s: &St| -> Vec<u8> { fixed.iter().map(|&i| s[i]).collect() };
    let mut left: HashMap<Vec<u8>, Vec<usize>> = HashMap::new();
    for (i, s) in states.iter().enumerate() { left.entry(key(&inverse(s))).or_default().push(i); }
    let mut seen = HashSet::new(); let mut out = vec![];
    for (j, s) in states.iter().enumerate() {
        if let Some(v) = left.get(&key(s)) { for &i in v {
            let mut w = halves[i].clone(); w.extend(&halves[j]); let w = normal(&w);
            if seen.insert(w.clone()) {
                let t = md.run(&sol, &w);
                assert!(fixed.iter().all(|&k| t[k] as usize == k));
                if t != sol { out.push(w); }
            }
        }}
    }
    out
}

/// corner perm (piece home index per place) and edge perm
fn cperm(md: &Model, s: &St) -> Vec<usize> { md.cf.iter().map(|f| { let h = s[f[0]] as usize; md.cf.iter().position(|g| g.contains(&h)).unwrap() }).collect() }
fn eperm(md: &Model, s: &St) -> Vec<usize> { md.ef.iter().map(|f| { let h = s[f[0]] as usize; md.ef.iter().position(|g| g.contains(&h)).unwrap() }).collect() }
fn is_3cycle_perm(p: &[usize]) -> bool { let mv: Vec<usize> = (0..p.len()).filter(|&i| p[i] != i).collect(); mv.len() == 3 && p[p[p[mv[0]]]] == mv[0] }
fn edges_home(md: &Model, s: &St) -> bool { md.edge_pl.iter().all(|&i| s[i] as usize == i) }
fn corners_home(md: &Model, s: &St) -> bool { md.corner_pl.iter().all(|&i| s[i] as usize == i) }

fn leftover(md: &Model, txt: &str) -> St {
    let parts: Vec<Vec<usize>> = txt.split(';').map(|x| x.split(',').map(|y| y.parse().unwrap()).collect()).collect();
    let (cp, ct, ep, ef) = (&parts[0], &parts[1], &parts[2], &parts[3]);
    let mut s = solved();
    for i in 0..8 { for k in 0..3 { s[md.cf[i][(k + ct[i]) % 3]] = md.cf[cp[i]][k] as u8; } }
    for i in 0..12 { for k in 0..2 { s[md.ef[i][(k + ef[i]) % 2]] = md.ef[ep[i]][k] as u8; } }
    s
}

struct Tab { algs: Vec<Vec<u8>>, by: HashMap<St, Vec<usize>> }
fn tab(md: &Model, algs: Vec<Vec<u8>>) -> Tab { let mut by: HashMap<St, Vec<usize>> = HashMap::new(); let s0 = solved(); for (i, a) in algs.iter().enumerate() { by.entry(md.run(&s0, a)).or_default().push(i); } Tab { algs, by } }

/// what an alg inserted at spot j must do, for every spot: Q_j L^-1 Q_j^-1 (L = state after skeleton, Q_j = moves after spot j)
fn needs(md: &Model, l: &St, s: &[u8]) -> Vec<St> {
    let li = inverse(l); let s0 = solved(); let n = s.len();
    let mut out = vec![s0; n + 1]; let mut q = s0; // state of Q_j
    for j in (0..=n).rev() {
        if j < n { q = mul(&md.run(&s0, &s[j..j + 1]), &q); }
        out[j] = mul(&mul(&q, &li), &inverse(&q));
    }
    out
}
fn ins(s: &[u8], j: usize, a: &[u8]) -> Vec<u8> { let mut w = s[..j].to_vec(); w.extend(a); w.extend(&s[j..]); normal(&w) }

/// every way of writing s with each opposite-face pair in either order (s has no cancelling)
fn variants(s: &[u8]) -> Vec<Vec<u8>> {
    let pairs: Vec<usize> = (0..s.len().saturating_sub(1)).filter(|&i| s[i] / 6 == s[i + 1] / 6).collect();
    (0..1usize << pairs.len()).map(|mask| { let mut w = s.to_vec(); for (b, &i) in pairs.iter().enumerate() { if mask >> b & 1 == 1 { w.swap(i, i + 1); } } w }).collect()
}
fn best_one_any(md: &Model, t: &Tab, l: &St, s: &[u8], any: bool) -> Option<usize> {
    if !any { return best_one(md, t, l, s); }
    variants(s).iter().filter_map(|v| best_one(md, t, l, v)).min()
}
fn best_one(md: &Model, t: &Tab, l: &St, s: &[u8]) -> Option<usize> {
    let mut best: Option<usize> = None;
    for (j, nd) in needs(md, l, s).iter().enumerate() {
        if let Some(v) = t.by.get(nd) { for &k in v { let x = ins(s, j, &t.algs[k]).len(); best = Some(best.map_or(x, |b| b.min(x))); } }
    }
    best
}
/// for a report: the best single insertion over every rewriting, written out (variant, spot, alg, result)
fn show_one(md: &Model, t: &Tab, l: &St, s: &[u8], any: bool) -> Option<(Vec<u8>, usize, Vec<u8>, Vec<u8>)> {
    let mut best: Option<(Vec<u8>, usize, Vec<u8>, Vec<u8>)> = None;
    for v in (if any { variants(s) } else { vec![s.to_vec()] }) {
        for (j, nd) in needs(md, l, &v).iter().enumerate() {
            if let Some(ks) = t.by.get(nd) { for &k in ks {
                let r = ins(&v, j, &t.algs[k]);
                if best.as_ref().map_or(true, |b| r.len() < b.3.len()) { best = Some((v.clone(), j, t.algs[k].clone(), r)); }
            }}
        }
    }
    best
}
fn text(w: &[u8]) -> String { w.iter().map(|&m| NAMES[m as usize]).collect::<Vec<_>>().join(" ") }
fn best_two(md: &Model, t: &Tab, l: &St, s0w: &[u8], corners: bool, any: bool) -> Option<usize> {
    let s0 = solved(); let mut best: Option<usize> = None;
    for s in (if any { variants(s0w) } else { vec![s0w.to_vec()] }) { let s = &s[..];
    let astates: Vec<St> = t.algs.iter().map(|a| md.run(&s0, a)).collect();
    for (i, nd) in needs(md, l, s).iter().enumerate() {
        for (k, a) in t.algs.iter().enumerate() {
            let x = mul(&inverse(&astates[k]), nd); // still needed right after the first comm
            // a pure 3-cycle: exactly three cubies of the kind off, cycling (three pieces twisted in place, or a 3-cycle next to twisted pieces, have no alg in the list)
            let ok = if corners { edges_home(md, &x) && md.cf.iter().filter(|f| f.iter().any(|&i| x[i] as usize != i)).count() == 3 && is_3cycle_perm(&cperm(md, &x)) }
                     else { corners_home(md, &x) && md.ef.iter().filter(|f| f.iter().any(|&i| x[i] as usize != i)).count() == 3 && is_3cycle_perm(&eperm(md, &x)) };
            if !ok { continue; }
            let s1 = ins(s, i, a);
            // leftover after s1: L s^-1 s1
            let l1 = md.run(&md.run(l, &invw(s)), &s1);
            if let Some(b) = best_one_any(md, t, &l1, &s1, any) { best = Some(best.map_or(b, |c| c.min(b))); }
        }
    }
    }
    best
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let md = Model::new();
    // self-checks of the model
    let s0 = solved();
    let ord = |w: &str| { let w = parse(w); let mut s = md.run(&s0, &w); let mut k = 1; while s != s0 { s = md.run(&s, &w); k += 1; } k };
    assert_eq!(ord("R U R' U'"), 6); assert_eq!(ord("R U"), 105); assert_eq!(ord("R U2 D' B D'"), 1260);
    let (w1, w2) = (parse("R U F2 D' L"), parse("B' D2 R U' F L2"));
    let mut w12 = w1.clone(); w12.extend(&w2);
    assert_eq!(mul(&md.run(&s0, &w1), &md.run(&s0, &w2)), md.run(&s0, &w12));
    assert_eq!(normal(&parse("F' B F D F' U F D' F' U' U2 B' L D")), parse("B D F' U F D' F' U B' L D"));
    let mut tw = vec![]; for _ in 0..4 { tw.extend(parse("U")); } assert!(normal(&tw).is_empty());

    let calgs = join(&md, &md.edge_pl.clone());
    let ealgs = join(&md, &md.corner_pl.clone());
    let ct = tab(&md, calgs); let et = tab(&md, ealgs);
    eprintln!("corner algs {} states {} lengths {:?}", ct.algs.len(), ct.by.len(), { let mut h = [0; 9]; for a in &ct.algs { h[a.len()] += 1; } h });
    let mut e3_seq = [0usize; 9]; let mut e3_el = [0usize; 9];
    for (st, v) in &et.by { if is_3cycle_perm(&eperm(&md, st)) { let mn = v.iter().map(|&k| et.algs[k].len()).min().unwrap(); e3_el[mn] += 1; for &k in v { e3_seq[et.algs[k].len()] += 1; } } }
    eprintln!("edge algs {} states {}; 3e sequences by length {:?}; 3e elements by shortest {:?}", et.algs.len(), et.by.len(), e3_seq, e3_el);
    if args.len() < 3 { return; }
    let (kind, path) = (&args[1], &args[2]); // kind: one-c, one-e, two-c, two-e
    let threads: usize = args.get(3).map(|x| x.parse().unwrap()).unwrap_or(4);
    let any = args.get(4).map_or(false, |x| x == "any");
    let limit: usize = args.get(5).map_or(usize::MAX, |x| x.parse().unwrap());
    let f = std::io::BufReader::new(std::fs::File::open(path).unwrap());
    let mut lines: Vec<String> = f.lines().map(|l| l.unwrap()).collect();
    let header = lines.remove(0); lines.truncate(limit); let cols: Vec<&str> = header.split('\t').collect();
    let cb = cols.iter().position(|&c| c == "L8_best").unwrap();
    let csol = cols.iter().position(|&c| c == "L8_solution");
    let chunk = (lines.len() + threads - 1) / threads;
    let results: Vec<String> = std::thread::scope(|sc| {
        let hs: Vec<_> = lines.chunks(chunk).map(|ch| { let (md, ct, et) = (&md, &ct, &et); sc.spawn(move || {
            let mut out = vec![];
            for ln in ch {
                let c: Vec<&str> = ln.split('\t').collect();
                let s = parse(c[1]); let l = leftover(md, c[2]); let n = s.len();
                // replay the study's printed solution, if any: L s^-1 F = solved
                let solok = match csol { Some(k) if c[k] != "-" && c[k] != "" => { if md.run(&md.run(&l, &invw(&s)), &parse(c[k])) == solved() { "ok" } else { "BAD" } }, _ => "-" };
                let v = match kind.as_str() { "one-c" => best_one_any(md, ct, &l, &s, any), "one-e" => best_one_any(md, et, &l, &s, any), "two-c" => best_two(md, ct, &l, &s, true, any), _ => best_two(md, et, &l, &s, false, any) };
                let vs = v.map_or("inf".to_string(), |x| (x as i64 - n as i64).to_string());
                if std::env::var("SHOW").is_ok() && kind.starts_with("one") {
                    let tb = if kind == "one-c" { ct } else { et };
                    if let Some((v, j, a, r)) = show_one(md, tb, &l, &s, any) {
                        assert!(md.run(&md.run(&l, &invw(&s)), &r) == solved());
                        out.push(format!("{}\t{}\t{}\t{}\twritten as: {} | spot {} | alg {} | result ({}): {}", c[0], vs, c[cb], solok, text(&v), j, text(&a), r.len(), text(&r)));
                        continue;
                    }
                }
                out.push(format!("{}\t{}\t{}\t{}", c[0], vs, c[cb], solok));
            }
            out
        })}).collect();
        hs.into_iter().flat_map(|h| h.join().unwrap()).collect()
    });
    let mut o = std::io::stdout().lock(); writeln!(o, "idx\tmine\tstudy_L8_best\tsolution_replay").unwrap();
    for r in results { writeln!(o, "{}", r).unwrap(); }
}
