//! instools: all insertion algorithms up to a length bound, and exact insertion costs of skeletons.
//! See ../SPEC.md.  Subcommands: selftest, count, algs, best, sample, corpus, bf1, bf2.

mod algs;
mod cubie;
mod ins;
mod seq;
mod types;

use algs::Table;
use cubie::{Cubie, Model, SOLVED};
use ins::Sol;
use rayon::prelude::*;
use std::collections::{HashMap, HashSet};
use std::io::Write;
use types::{classify, TYPES};

fn opt_val(args: &[String], name: &str) -> Option<String> {
    args.iter().position(|a| a == name).and_then(|i| args.get(i + 1).cloned())
}
fn bounds(args: &[String]) -> Vec<usize> {
    opt_val(args, "--L").unwrap_or_else(|| "8,10".to_string()).split(',').map(|x| x.parse().unwrap()).collect()
}

fn cmd_count(m: &Model) {
    println!("type\texpected\tby construction\tdistinct\tamong all products of two 3-cycles\tamong all corner states");
    // independent: all products of two 3-cycles (and the 3-cycles themselves)
    let mut prod: Vec<HashSet<u128>> = vec![HashSet::new(); TYPES.len()];
    for t3 in [types::T3C, types::T3E] {
        let c3 = types::elements(t3);
        for a in &c3 {
            prod[classify(a).unwrap()].insert(a.key());
            for b in &c3 {
                let p = a.then(b);
                if let Some(t) = classify(&p) {
                    prod[t].insert(p.key());
                }
            }
        }
    }
    // independent: every corner state (8! permutations, 3^7 twists)
    let mut sweep = vec![0u64; TYPES.len()];
    let mut perm = [0u8, 1, 2, 3, 4, 5, 6, 7];
    loop {
        for v in 0..2187u32 {
            let mut c = SOLVED;
            c.cp = perm;
            let (mut w, mut sum) = (v, 0u32);
            for i in 0..7 {
                c.ct[i] = (w % 3) as u8;
                sum += w % 3;
                w /= 3;
            }
            c.ct[7] = ((3 - sum % 3) % 3) as u8;
            if let Some(t) = classify(&c) {
                sweep[t] += 1;
            }
        }
        // next permutation
        let mut i = 7;
        while i > 0 && perm[i - 1] > perm[i] {
            i -= 1;
        }
        if i == 0 {
            break;
        }
        let mut j = 7;
        while perm[j] < perm[i - 1] {
            j -= 1;
        }
        perm.swap(i - 1, j);
        perm[i..].reverse();
    }
    let mut ok = true;
    for t in 0..TYPES.len() {
        let el = algs::elements_all(t);
        let distinct: HashSet<u128> = el.iter().map(|c| c.key()).collect();
        let all_typed = el.iter().all(|c| classify(c) == Some(t));
        let p = if t == types::T2C2E { "-".to_string() } else { prod[t].len().to_string() };
        let s = if types::is_corner(t) { sweep[t].to_string() } else { "-".to_string() };
        println!("{}\t{}\t{}\t{}\t{}\t{}", TYPES[t], types::EXPECTED[t], el.len(), distinct.len(), p, s);
        ok &= el.len() == types::EXPECTED[t] && distinct.len() == el.len() && all_typed;
        ok &= t == types::T2C2E || prod[t].len() == el.len();
        ok &= !types::is_corner(t) || sweep[t] as usize == el.len();
    }
    let _ = m;
    println!("2c2c (pure + twisted) = {}, 2e2e (unflipped + flipped) = {}", types::EXPECTED[3] + types::EXPECTED[4], types::EXPECTED[10] + types::EXPECTED[11]);
    println!("{}", if ok { "type sizes: all agree" } else { "type sizes: MISMATCH" });
    assert!(ok);
}

/// `twistmin L`: for every length up to L, how many corner-only reduced sequences there are, how many of them leave
/// a corner twisted in its place, and what those do (by leftover type; `other` is a type no two 3-cycles make).
fn cmd_twistmin(m: &Model, args: &[String]) {
    let lmax: usize = args[0].parse().unwrap();
    let h = (lmax + 1) / 2;
    let levels: Vec<algs::Level> = (0..=h).map(|k| algs::build_level(m, k)).collect();
    println!("length\tcorner-only reduced sequences (not the identity)\twith a corner twisted in place\tdistinct states of those\tby type");
    for l in 2..=lmax {
        let (ka, kb) = ((l + 1) / 2, l / 2);
        let (pairs, hits, keys) = algs::join_twisted(&levels[ka], &levels[kb]);
        let mut by: std::collections::BTreeMap<String, usize> = std::collections::BTreeMap::new();
        for &c in &keys {
            let g = Cubie::from_key((c as u128) << 64 | cubie::SOLVED.ekey() as u128);
            let name = match classify(&g) {
                Some(t) => TYPES[t].to_string(),
                None => "other".to_string(),
            };
            *by.entry(name).or_insert(0) += 1;
        }
        let parts: Vec<String> = by.iter().map(|(k, v)| format!("{k}: {v}")).collect();
        println!("{l}\t{pairs}\t{hits}\t{}\t{}", keys.len(), parts.join(", "));
    }
}

fn cmd_algs(m: &Model, args: &[String]) {
    let lmax: usize = args[0].parse().unwrap();
    let check = opt_val(args, "--check").unwrap_or_else(|| "simple".to_string());
    let out = cubie::out_dir();
    let t0 = std::time::Instant::now();
    let lists = algs::build_by_join(m, lmax, true);
    eprintln!("join done in {:.1}s", t0.elapsed().as_secs_f64());
    // every sequence found: reduced, and its product is the element
    lists.par_iter().enumerate().for_each(|(t, v)| {
        for &(k, a) in v {
            let s = seq::unpack_vec(a);
            assert!(seq::is_reduced(&s) && s.len() <= lmax);
            assert_eq!(m.state(&s).key(), k);
            assert_eq!(classify(&Cubie::from_key(k)), Some(t));
        }
    });
    algs::write_file(&format!("{out}/algs_L{lmax}.bin"), lmax, &lists);
    let tab = Table::from_lists(lmax, &lists, lmax);
    eprintln!("table: {} elements with sequences, {} sequences", tab.elems.len(), tab.algs.len());
    let search = if check != "none" || lmax >= 10 { Some(algs::Search::new(m, lmax)) } else { None };
    let simple = ["3c", "3e", "2c2c-pure", "2c2c-twisted", "2tc", "3tc", "2e2e", "2e2e-flipped", "2f"];
    let mut summary = String::new();
    summary.push_str(&format!("type\telements\tclasses\toptimal length: number of elements{}\n", ""));
    let mut totals = String::from("type\tlength: number of distinct sequences over all elements\n");
    for t in 0..TYPES.len() - 1 {
        let el = algs::elements_all(t);
        let rows = algs::classes(m, &tab, &el, lmax, true);
        assert_eq!(rows.iter().map(|r| r.size).sum::<usize>(), el.len());
        // the counts of every element agree with its class (follows from the transport check; here: totals)
        let mut f = std::io::BufWriter::new(std::fs::File::create(format!("{out}/cases_{}_L{lmax}.tsv", TYPES[t])).unwrap());
        writeln!(f, "class\trepresentative\tpieces (from>to+twist)\tclass_size\toptimal_length\t{}", (1..=lmax).map(|l| format!("n{l}")).collect::<Vec<_>>().join("\t")).unwrap();
        let mut dist: Vec<usize> = vec![0; lmax + 2];
        let mut tot = vec![0u64; lmax + 1];
        for (i, r) in rows.iter().enumerate() {
            let opt = r.shortest.map(seq::plen);
            dist[opt.unwrap_or(lmax + 1)] += r.size;
            for l in 0..=lmax {
                tot[l] += r.counts[l] * r.size as u64;
            }
            writeln!(
                f,
                "{}\t{}\t{}\t{}\t{}\t{}",
                i + 1,
                r.shortest.map_or("-".to_string(), |a| seq::text(&seq::unpack_vec(a))),
                types::describe(&r.rep, &m.cnames, &m.enames),
                r.size,
                opt.map_or(format!(">{lmax}"), |o| o.to_string()),
                (1..=lmax).map(|l| r.counts[l].to_string()).collect::<Vec<_>>().join("\t")
            )
            .unwrap();
        }
        let in_table: u64 = lists[t].len() as u64;
        assert_eq!(tot.iter().sum::<u64>(), in_table, "class totals against the table");
        let d: Vec<String> = (1..=lmax + 1).filter(|&l| dist[l] > 0).map(|l| if l > lmax { format!(">{lmax}: {}", dist[l]) } else { format!("{l}: {}", dist[l]) }).collect();
        summary.push_str(&format!("{}\t{}\t{}\t{}\n", TYPES[t], el.len(), rows.len(), d.join(", ")));
        let tt: Vec<String> = (1..=lmax).filter(|&l| tot[l] > 0).map(|l| format!("{l}: {}", tot[l])).collect();
        totals.push_str(&format!("{}\t{}\n", TYPES[t], tt.join(", ")));
        // independent search, class by class
        let do_check = check == "all" || (check == "simple" && simple.contains(&TYPES[t]));
        if do_check {
            let s = search.as_ref().unwrap();
            let t1 = std::time::Instant::now();
            rows.par_iter().for_each(|r| {
                let mut have = tab.algs_of(r.rep.key(), lmax);
                have.sort_unstable();
                assert!(s.algs_of(m, &r.rep) == have, "search and join disagree");
            });
            eprintln!("  {}: {} classes, the search for each representative agrees with the join ({:.1}s)", TYPES[t], rows.len(), t1.elapsed().as_secs_f64());
        } else {
            eprintln!("  {}: {} classes (lists of all elements are images of the representative's)", TYPES[t], rows.len());
        }
    }
    // the parity family, by the search
    if let Some(s) = search.as_ref() {
        let t = types::T2C2E;
        let el = algs::elements_all(t);
        let reps: Vec<u128> = el.par_iter().map(|g| algs::class_rep(m, g)).collect();
        let mut size: HashMap<u128, usize> = HashMap::new();
        for &r in &reps {
            *size.entry(r).or_insert(0) += 1;
        }
        let mut keys: Vec<u128> = size.keys().copied().collect();
        keys.sort_unstable();
        let t1 = std::time::Instant::now();
        let found: Vec<Vec<u64>> = keys.par_iter().map(|&k| s.algs_of(m, &Cubie::from_key(k))).collect();
        eprintln!("  2c2e: {} classes searched ({:.1}s)", keys.len(), t1.elapsed().as_secs_f64());
        let mut f = std::io::BufWriter::new(std::fs::File::create(format!("{out}/cases_2c2e_L{lmax}.tsv")).unwrap());
        writeln!(f, "class\trepresentative\tpieces (from>to+twist)\tclass_size\toptimal_length\t{}", (1..=lmax).map(|l| format!("n{l}")).collect::<Vec<_>>().join("\t")).unwrap();
        let mut dist: Vec<usize> = vec![0; lmax + 2];
        let mut tot = vec![0u64; lmax + 1];
        let mut seen: HashSet<u64> = HashSet::new();
        let mut cyc: HashMap<usize, HashSet<u64>> = HashMap::new();
        let mut optseq: HashMap<usize, u64> = HashMap::new();
        let mut shorter: HashMap<usize, bool> = HashMap::new();
        for (i, (&k, list)) in keys.iter().zip(&found).enumerate() {
            let rep = Cubie::from_key(k);
            for &a in list {
                assert_eq!(m.state(&seq::unpack_vec(a)), rep);
            }
            let opt = list.first().map(|&a| seq::plen(a));
            dist[opt.unwrap_or(lmax + 1)] += size[&k];
            let mut counts = vec![0u64; lmax + 1];
            for &a in list {
                counts[seq::plen(a)] += 1;
            }
            for l in 0..=lmax {
                tot[l] += counts[l] * size[&k] as u64;
            }
            if let Some(o) = opt {
                *optseq.entry(o).or_insert(0) += counts[o] * size[&k] as u64;
                for &a in list.iter().filter(|&&a| seq::plen(a) == o) {
                    if !seen.contains(&a) {
                        let (c, sh) = algs::cyclic_class(m, a, &mut seen);
                        *shorter.entry(o).or_insert(false) |= sh;
                        cyc.entry(o).or_default().insert(c);
                    }
                }
            }
            writeln!(
                f,
                "{}\t{}\t{}\t{}\t{}\t{}",
                i + 1,
                list.first().map_or("-".to_string(), |&a| seq::text(&seq::unpack_vec(a))),
                types::describe(&rep, &m.cnames, &m.enames),
                size[&k],
                opt.map_or(format!(">{lmax}"), |o| o.to_string()),
                (1..=lmax).map(|l| counts[l].to_string()).collect::<Vec<_>>().join("\t")
            )
            .unwrap();
        }
        let d: Vec<String> = (1..=lmax + 1).filter(|&l| dist[l] > 0).map(|l| if l > lmax { format!(">{lmax}: {}", dist[l]) } else { format!("{l}: {}", dist[l]) }).collect();
        summary.push_str(&format!("{}\t{}\t{}\t{}\n", TYPES[t], el.len(), keys.len(), d.join(", ")));
        let tt: Vec<String> = (1..=lmax).filter(|&l| tot[l] > 0).map(|l| format!("{l}: {}", tot[l])).collect();
        totals.push_str(&format!("{}\t{}\n", TYPES[t], tt.join(", ")));
        let mut os: Vec<_> = optseq.into_iter().collect();
        os.sort();
        for (o, cnt) in os {
            let reps: Vec<String> = { let mut v: Vec<u64> = cyc[&o].iter().copied().collect(); v.sort(); v.iter().take(12).map(|&a| seq::text(&seq::unpack_vec(a))).collect() };
            summary.push_str(&format!(
                "2c2e, elements of optimal length {o}: {cnt} distinct sequences of that length in all; {} classes up to rotation, reflection, inversion and cyclic shift{}; class representatives: {}\n",
                cyc[&o].len(),
                if shorter.get(&o).copied().unwrap_or(false) { " (some cyclic shift of some of them cancels to a shorter sequence; such shifts are not followed)" } else { " (no cyclic shift of any of them cancels)" },
                reps.join(" | ")
            ));
        }
    }
    let txt = format!("L = {lmax}\n{summary}\n{totals}");
    std::fs::write(format!("{out}/algs_L{lmax}_summary.txt"), &txt).unwrap();
    print!("{txt}");
    eprintln!("algs {lmax}: {:.1}s in all", t0.elapsed().as_secs_f64());
}

struct Res {
    direct: Option<Sol>,
    two: Option<Option<Sol>>,   // None: not applicable or not computed
    flat: Option<Option<Sol>>,
    apart: Option<Option<Sol>>,
    mixed: Option<Option<Sol>>,
    two_applies: bool,
}
fn two_applies(ty: usize) -> bool {
    ty != types::T3C && ty != types::T3E && ty != types::T2C2E
}
fn evaluate(tab: &Table, m: &Model, skel: &[u8], c: &Cubie, ty: usize, l: usize, do_two: bool, check: bool, mixed_fam: Option<&[Cubie]>) -> Res {
    let direct = ins::single(tab, m, skel, c, l);
    let (mut two, mut flat, mut apart, mut mixed) = (None, None, None, None);
    if two_applies(ty) && do_two {
        let o = ins::two(tab, m, skel, c, types::is_corner(ty), l, check, None);
        two = Some(o.two);
        flat = Some(o.flat);
        apart = Some(o.apart);
    }
    if ty != types::T2C2E {
        if let Some(fam) = mixed_fam {
            mixed = Some(ins::two(tab, m, skel, c, types::is_corner(ty), l, false, Some(fam)).two);
        }
    }
    Res { direct, two, flat, apart, mixed, two_applies: two_applies(ty) }
}
/// (model name, solution) with the shortest result among the models computed.
fn best_of(r: &Res) -> Option<(&'static str, &Sol)> {
    let mut b: Option<(&'static str, &Sol)> = None;
    if let Some(s) = &r.direct {
        b = Some(("direct", s));
    }
    if let Some(Some(s)) = &r.two {
        if b.map_or(true, |x| s.len < x.1.len) {
            b = Some(("two", s));
        }
    }
    if let Some(Some(s)) = &r.mixed {
        if b.map_or(true, |x| s.len < x.1.len) {
            b = Some(("mixed", s));
        }
    }
    b
}

fn show_sol(out: &mut String, case: usize, l: usize, model: &str, skel: &[u8], sol: &Option<Sol>) {
    let n = skel.len();
    match sol {
        None => out.push_str(&format!("L={l} {model}: no solution within the bound\n")),
        Some(s) => {
            let steps = ins::replay(skel, s);
            let fin = &steps.last().unwrap().after;
            assert_eq!(fin.len(), s.len);
            out.push_str(&format!("L={l} {model}: cost {}, length {}{}\n", s.len as i64 - n as i64, s.len, if s.nested { " (nested)" } else { "" }));
            for (k, st) in steps.iter().enumerate() {
                out.push_str(&format!("   {}. at {}: insert {} ({}), {} cancel -> {} ({})\n", k + 1, st.pos, seq::text(&st.alg), st.alg.len(), st.cancelled, seq::text(&st.after), st.after.len()));
            }
            let insd: Vec<String> = steps.iter().map(|st| format!("{}:{}:{}", st.pos, seq::text(&st.alg), st.cancelled)).collect();
            out.push_str(&format!("SOL\t{case}\t{l}\t{model}\t{}\t{}\t{}\t{}\t{}\n", s.len as i64 - n as i64, s.len, s.nested as u8, insd.join("|"), seq::text(fin)));
        }
    }
}

fn cmd_best(m: &Model, args: &[String]) {
    let ls = bounds(args);
    let tab = Table::load(*ls.iter().max().unwrap());
    let do_mixed = args.iter().any(|a| a == "--mixed");
    let fams = [types::elements(types::T3C), types::elements(types::T3E)];
    let mut cases: Vec<(String, String)> = Vec::new();
    if let Some(f) = opt_val(args, "--file") {
        for line in std::fs::read_to_string(&f).unwrap().lines() {
            if let Some((a, b)) = line.split_once('\t') {
                cases.push((a.to_string(), b.split('\t').next().unwrap().to_string()));
            }
        }
    } else {
        cases.push((args[0].clone(), args[1].clone()));
    }
    for (k, (scr, sk)) in cases.iter().enumerate() {
        let mut out = String::new();
        out.push_str(&format!("CASE\t{}\nscramble: {}\n", k + 1, scr));
        let (z, s) = match (seq::parse(scr), seq::parse(sk)) {
            (Ok(z), Ok(s)) => (z, s),
            _ => {
                println!("{out}cannot parse (only face turns are accepted)\n");
                continue;
            }
        };
        let skel = seq::cancel(&s);
        let n = skel.len();
        out.push_str(&format!("skeleton: {} ({}){}\n", seq::text(&skel), n, if skel != s { " [written reduced]" } else { "" }));
        let c = m.state(&z).then(&m.state(&skel));
        let ty = classify(&c);
        out.push_str(&format!("leftover: {} | {} | {}\n", ty.map_or("not one of the types", |t| TYPES[t]), types::describe(&c, &m.cnames, &m.enames), c.to_text()));
        if ty == Some(types::T2C2E) {
            out.push_str("a parity leftover: the insertion models here do not cover it\n");
        } else if let Some(ty) = ty {
            for &l in &ls {
                let fam = if do_mixed { Some(&fams[if types::is_corner(ty) { 0 } else { 1 }][..]) } else { None };
                let r = evaluate(&tab, m, &skel, &c, ty, l, true, false, fam);
                if ty == types::T3C || ty == types::T3E {
                    show_sol(&mut out, k + 1, l, "one", &skel, &r.direct);
                }
                show_sol(&mut out, k + 1, l, "direct", &skel, &r.direct);
                if let Some(t) = &r.two {
                    show_sol(&mut out, k + 1, l, "two", &skel, t);
                    show_sol(&mut out, k + 1, l, "two-flat", &skel, r.flat.as_ref().unwrap());
                    show_sol(&mut out, k + 1, l, "two-apart", &skel, r.apart.as_ref().unwrap());
                }
                if let Some(t) = &r.mixed {
                    show_sol(&mut out, k + 1, l, "mixed", &skel, t);
                }
                match best_of(&r) {
                    Some((model, s)) => out.push_str(&format!("L={l} best: cost {}, length {} ({model})\n", s.len as i64 - n as i64, s.len)),
                    None => out.push_str(&format!("L={l} best: no solution within the bound\n")),
                }
            }
        }
        println!("{out}");
    }
}

fn cost_text(n: usize, s: &Option<Sol>) -> String {
    s.as_ref().map_or("inf".to_string(), |s| (s.len as i64 - n as i64).to_string())
}

/// One output line for a skeleton and a leftover.
fn sample_line(tab: &Table, m: &Model, idx: usize, skel: &[u8], c: &Cubie, ty: usize, ls: &[usize], two_limit: &HashMap<usize, usize>, with_sol: bool, mixed_fam: Option<&[Cubie]>, mixed_limit: &HashMap<usize, usize>) -> String {
    let n = skel.len();
    let mut f = vec![idx.to_string(), seq::text(skel), c.to_text()];
    for &l in ls {
        let do_two = two_limit.get(&l).map_or(true, |&k| idx < k);
        let do_mixed = mixed_limit.get(&l).map_or(false, |&k| idx < k);
        let r = evaluate(tab, m, skel, c, ty, l, do_two, false, if do_mixed { mixed_fam } else { None });
        let mixed = r.mixed.as_ref().map_or("nc".to_string(), |s| cost_text(n, s));
        let one = if ty == types::T3C || ty == types::T3E { cost_text(n, &r.direct) } else { "na".to_string() };
        let two = if !r.two_applies { "na".to_string() } else { r.two.as_ref().map_or("nc".to_string(), |s| cost_text(n, s)) };
        let flat = if !r.two_applies { "na".to_string() } else { r.flat.as_ref().map_or("nc".to_string(), |s| cost_text(n, s)) };
        let apart = if !r.two_applies { "na".to_string() } else { r.apart.as_ref().map_or("nc".to_string(), |s| cost_text(n, s)) };
        let complete = !r.two_applies || r.two.is_some();
        let b = best_of(&r);
        let best = if !complete { "nc".to_string() } else { b.map_or("inf".to_string(), |(_, s)| (s.len as i64 - n as i64).to_string()) };
        f.extend([one, cost_text(n, &r.direct), two, flat, apart, mixed, best]);
        match b {
            Some((model, s)) if complete => {
                let steps = ins::replay(skel, s);
                f.push(model.to_string());
                f.push(steps.iter().map(|st| st.pos.to_string()).collect::<Vec<_>>().join(","));
                f.push(steps.iter().map(|st| st.alg.len().to_string()).collect::<Vec<_>>().join(","));
                f.push(steps.iter().map(|st| st.cancelled.to_string()).collect::<Vec<_>>().join(","));
                f.push((s.nested as u8).to_string());
                f.push(if with_sol { seq::text(&steps.last().unwrap().after) } else { "-".to_string() });
            }
            _ => f.extend(std::iter::repeat("-".to_string()).take(6)),
        }
    }
    f.join("\t")
}

fn header(ls: &[usize]) -> String {
    let mut f = vec!["idx".to_string(), "skeleton".to_string(), "leftover(cp;ct;ep;ef)".to_string()];
    for &l in ls {
        for c in ["one", "direct", "two", "two_flat", "two_apart", "mixed", "best", "best_model", "positions", "alg_lengths", "cancelled", "nested", "solution"] {
            f.push(format!("L{l}_{c}"));
        }
    }
    f.join("\t")
}

fn parse_two_limit(args: &[String], name: &str) -> HashMap<usize, usize> {
    let mut h = HashMap::new();
    if let Some(v) = opt_val(args, name) {
        for part in v.split(',') {
            let (a, b) = part.split_once(':').unwrap();
            h.insert(a.parse().unwrap(), b.parse().unwrap());
        }
    }
    h
}

fn run_lines(m: &Model, args: &[String], ty: usize, seed: u64, skeletons: Option<Vec<Vec<u8>>>, n: usize, count: usize) {
    let ls = bounds(args);
    let tab = Table::load(*ls.iter().max().unwrap());
    let two_limit = parse_two_limit(args, "--two");
    let mixed_limit = parse_two_limit(args, "--mixed");
    let every: usize = opt_val(args, "--sol-every").map_or(20, |x| x.parse().unwrap());
    run_cell(m, &tab, &ls, &two_limit, &mixed_limit, every, opt_val(args, "--out"), ty, seed, skeletons, n, count);
}

#[allow(clippy::too_many_arguments)]
fn run_cell(m: &Model, tab: &Table, ls: &[usize], two_limit: &HashMap<usize, usize>, mixed_limit: &HashMap<usize, usize>, every: usize, path: Option<String>, ty: usize, seed: u64, skeletons: Option<Vec<Vec<u8>>>, n: usize, count: usize) {
    let mixed_fam = types::elements(if types::is_corner(ty) { types::T3C } else { types::T3E });
    let el = algs::elements_all(ty);
    let t0 = std::time::Instant::now();
    let mut w: Box<dyn Write> = match &path {
        Some(p) => Box::new(std::io::BufWriter::new(std::fs::File::create(p).unwrap())),
        None => Box::new(std::io::BufWriter::new(std::io::stdout())),
    };
    writeln!(w, "{}", header(ls)).unwrap();
    let mut done = 0;
    while done < count {
        let hi = (done + 1000).min(count);
        let lines: Vec<String> = (done..hi)
            .into_par_iter()
            .map(|idx| {
                let mut rng = seq::Rng(seed.wrapping_mul(0x9E3779B97F4A7C15) ^ (idx as u64 + 1).wrapping_mul(0xD1B54A32D192ED03));
                rng.next();
                let skel = match &skeletons {
                    Some(v) => v[idx].clone(),
                    None => rng.skeleton(n),
                };
                let c = el[rng.below(el.len())];
                sample_line(tab, m, idx, &skel, &c, ty, ls, two_limit, every > 0 && idx % every == 0, Some(&mixed_fam[..]), mixed_limit)
            })
            .collect();
        for l in lines {
            writeln!(w, "{l}").unwrap();
        }
        done = hi;
    }
    w.flush().unwrap();
    eprintln!("{} n={} count={} two-limits {:?}: {:.1}s", TYPES[ty], n, count, two_limit, t0.elapsed().as_secs_f64());
}

/// The sampling runs of the study: for each n and each type, out/sample_<type>_n<n>.tsv, with the table loaded once.
/// The model `two` is computed for the first k skeletons only, k depending on the type and the bound (see `plan`).
fn plan(ty: usize, count: usize) -> HashMap<usize, usize> {
    let (k8, k10) = match TYPES[ty] {
        "2tc" | "2f" | "2e2e" | "2e2e-flipped" => (5000, 200),
        "2c2c-pure" | "2c2c-twisted" | "3tc" | "3c1t" | "5e" | "3e1f" => (20000, 500),
        _ => (20000, 2000),
    };
    HashMap::from([(8, k8.min(count)), (10, k10.min(count)), (12, 0)])
}
fn cmd_runs(m: &Model, args: &[String]) {
    let tys: Vec<usize> = if args[0] == "all" { (0..TYPES.len() - 1).collect() } else { args[0].split(',').map(|t| types::type_id(t).expect("type")).collect() };
    let ns: Vec<usize> = args[1].split(',').map(|x| x.parse().unwrap()).collect();
    let (count, seed): (usize, u64) = (args[2].parse().unwrap(), args[3].parse().unwrap());
    let ls: Vec<usize> = opt_val(args, "--L").unwrap_or_else(|| "8,10,12".to_string()).split(',').map(|x| x.parse().unwrap()).collect();
    let tab = Table::load(*ls.iter().max().unwrap());
    let prefix = opt_val(args, "--prefix").unwrap_or_else(|| "sample".to_string());
    let given = parse_two_limit(args, "--two");
    let mixed_limit = parse_two_limit(args, "--mixed");
    for &n in &ns {
        for &ty in &tys {
            let lim = if given.is_empty() { plan(ty, count) } else { given.clone() };
            let path = format!("{}/{}_{}_n{}.tsv", cubie::out_dir(), prefix, TYPES[ty], n);
            run_cell(m, &tab, &ls, &lim, &mixed_limit, 20, Some(path), ty, seed + 1000 * ty as u64 + n as u64, None, n, count);
        }
    }
}

/// Check of `single`: random 3c leftovers on random skeletons of length n, against an enumeration of the sequences by
/// another method (depth-first over whole sequences, pruned with a breadth-first ball of radius 4 kept in a standard
/// hash map of states) and the plain `cancel` on whole sequences.
fn cmd_bf1(m: &Model, args: &[String]) {
    let (count, seed): (usize, u64) = (args[0].parse().unwrap(), args[1].parse().unwrap());
    let n: usize = opt_val(args, "--n").map_or(6, |x| x.parse().unwrap());
    let l: usize = opt_val(args, "--L").map_or(8, |x| x.parse().unwrap());
    let tname = opt_val(args, "--type").unwrap_or_else(|| "3c".to_string());
    let ty = types::type_id(&tname).unwrap();
    let tab = Table::load(l);
    // ball: distance from solved, up to 4
    let mut ball: HashMap<Cubie, u8> = HashMap::new();
    ball.insert(SOLVED, 0);
    let mut frontier = vec![SOLVED];
    for d in 1..=4u8 {
        let mut next = Vec::new();
        for s in &frontier {
            for mv in 0..18 {
                let t = m.turn(s, mv);
                if !ball.contains_key(&t) {
                    ball.insert(t, d);
                    next.push(t);
                }
            }
        }
        frontier = next;
    }
    fn dfs(m: &Model, ball: &HashMap<Cubie, u8>, g: &Cubie, s: &Cubie, w: &mut Vec<u8>, len: usize, out: &mut Vec<Vec<u8>>) {
        let left = len - w.len();
        if left == 0 {
            if s == g {
                out.push(w.clone());
            }
            return;
        }
        if left <= 4 {
            // the rest must be s^-1 · g, which has to be within `left` of solved
            match ball.get(&s.inverse().then(g)) {
                Some(&d) if d as usize <= left => {}
                _ => return,
            }
        }
        for mv in 0..18u8 {
            if let Some(&last) = w.last() {
                if !seq::follows(last, mv) {
                    continue;
                }
            }
            w.push(mv);
            dfs(m, ball, g, &m.turn(s, mv as usize), w, len, out);
            w.pop();
        }
    }
    let el = algs::elements_all(ty);
    let mut rng = seq::Rng(seed);
    let (mut agree, mut nalg, mut solved) = (0, 0usize, 0);
    let mut hist: HashMap<String, usize> = HashMap::new();
    for _ in 0..count {
        let skel = rng.skeleton(n);
        let c = el[rng.below(el.len())];
        let z = c.then(&m.state(&skel).inverse());
        let mut best: Option<usize> = None;
        for i in 0..=n {
            let y = m.state(&skel[i..]);
            let g = y.then(&c.inverse()).then(&y.inverse());
            let mut found: Vec<Vec<u8>> = Vec::new();
            for len in 1..=l {
                dfs(m, &ball, &g, &SOLVED, &mut Vec::new(), len, &mut found);
            }
            // the same set as the table's
            let mut a: Vec<u64> = found.iter().map(|s| seq::pack(s)).collect();
            a.sort_unstable();
            let mut b = tab.algs_of(g.key(), l);
            b.sort_unstable();
            assert!(a == b, "the two enumerations of the sequences of an element disagree");
            nalg += a.len();
            for alg in &found {
                let whole: Vec<u8> = skel[..i].iter().chain(alg).chain(&skel[i..]).copied().collect();
                let fin = seq::cancel(&whole);
                assert_eq!(z.then(&m.state(&fin)), SOLVED);
                if best.map_or(true, |b| fin.len() < b) {
                    best = Some(fin.len());
                }
            }
        }
        let fast = ins::single(&tab, m, &skel, &c, l).map(|s| s.len);
        assert_eq!(fast, best, "single insertion: skeleton {} leftover {}", seq::text(&skel), c.to_text());
        agree += 1;
        if best.is_some() {
            solved += 1;
        }
        *hist.entry(best.map_or("none".to_string(), |b| (b as i64 - n as i64).to_string())).or_insert(0) += 1;
    }
    let mut h: Vec<_> = hist.into_iter().collect();
    h.sort();
    println!("bf1: type {tname}, n = {n}, L = {l}: {agree} of {count} pairs agree (one insertion, table against direct enumeration); {solved} have a solution; {nalg} sequences compared; costs {h:?}");
}

/// Check of `two` against the plain enumeration.
fn cmd_bf2(m: &Model, args: &[String]) {
    let ty = types::type_id(&args[0]).unwrap();
    let (n, count, seed, l): (usize, usize, u64, usize) = (args[1].parse().unwrap(), args[2].parse().unwrap(), args[3].parse().unwrap(), args[4].parse().unwrap());
    let tab = Table::load(l);
    let el = algs::elements_all(ty);
    let t0 = std::time::Instant::now();
    let mixed = args.iter().any(|a| a == "--mixed");
    let fam3 = types::elements(if types::is_corner(ty) { types::T3C } else { types::T3E });
    let res: Vec<(Option<usize>, Option<usize>, Option<usize>, bool)> = (0..count)
        .into_par_iter()
        .map(|idx| {
            let mut rng = seq::Rng(seed.wrapping_mul(0x9E3779B97F4A7C15) ^ (idx as u64 + 1).wrapping_mul(0xD1B54A32D192ED03));
            rng.next();
            let skel = rng.skeleton(n);
            let c = el[rng.below(el.len())];
            let fast = ins::two(&tab, m, &skel, &c, types::is_corner(ty), l, true, if mixed { Some(&fam3[..]) } else { None });
            let slow = ins::two_naive(&tab, m, &skel, &c, types::is_corner(ty), l, mixed);
            // the splits found by the short cut are all of them
            let fam = types::elements(if types::is_corner(ty) { types::T3C } else { types::T3E });
            let want = if types::is_corner(ty) { types::T3C } else { types::T3E };
            let all = fam.iter().filter(|d| classify(&c.then(d)) == Some(want)).count();
            assert_eq!(all, types::splits(&c, types::is_corner(ty)).len());
            if let Some(s) = &fast.two {
                let steps = ins::replay(&skel, s);
                assert_eq!(steps.last().unwrap().after.len(), s.len);
                let z = c.then(&m.state(&skel).inverse());
                assert_eq!(z.then(&m.state(&steps.last().unwrap().after)), SOLVED);
            }
            let nested = fast.two.as_ref().map_or(false, |s| s.nested);
            let (fl, tw) = (fast.flat.as_ref().map(|s| s.len), fast.two.as_ref().map(|s| s.len));
            assert!(fl.is_none() || (tw.is_some() && fl >= tw));
            assert_eq!(nested, fl != tw);
            (fast.two.map(|s| s.len), slow, fast.apart.map(|s| s.len), nested)
        })
        .collect();
    let mut bad = 0;
    let (mut solved, mut apart_worse, mut nested) = (0, 0, 0);
    for (f, s, a, ne) in &res {
        if f != s {
            bad += 1;
        }
        if f.is_some() {
            solved += 1;
        }
        if a != f {
            apart_worse += 1;
        }
        if *ne {
            nested += 1;
        }
    }
    println!(
        "bf2: type {}{}, n = {n}, L = {l}: {} of {count} agree (two insertions, fast against plain enumeration); {solved} have a solution; two-apart is worse in {apart_worse}; nesting is needed for the best in {nested}  ({:.1}s)",
        args[0],
        if mixed { " (mixed model)" } else { "" },
        count - bad,
        t0.elapsed().as_secs_f64()
    );
    assert_eq!(bad, 0);
}

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    if args.is_empty() {
        eprintln!("usage: instools selftest | count | algs <L> [--check none|simple|all] | best <scramble> <skeleton> [--L 8,10] | best --file <tsv> | sample <type> <n> <count> <seed> [--L 8,10] [--two 10:2000] [--sol-every 20] [--out file] | corpus <file> <type> <seed> | runs <types|all> <n,n,..> <count> <seed> [--L 8,10,12] [--two 8:k,10:k,12:k] [--mixed 10:k] [--prefix sample] | bf1 <count> <seed> | bf2 <type> <n> <count> <seed> <L>");
        return;
    }
    let m = Model::load();
    let rest = &args[1..];
    match args[0].as_str() {
        "selftest" => cubie::selftest(&m),
        "count" => cmd_count(&m),
        "algs" => cmd_algs(&m, rest),
        "twistmin" => cmd_twistmin(&m, rest),
        "best" => cmd_best(&m, rest),
        "sample" => {
            let ty = types::type_id(&rest[0]).expect("type");
            run_lines(&m, rest, ty, rest[3].parse().unwrap(), None, rest[1].parse().unwrap(), rest[2].parse().unwrap());
        }
        "corpus" => {
            let ty = types::type_id(&rest[1]).expect("type");
            let sk: Vec<Vec<u8>> = std::fs::read_to_string(&rest[0]).unwrap().lines().filter(|l| !l.trim().is_empty()).map(|l| seq::cancel(&seq::parse(l).expect("skeleton"))).collect();
            let count = sk.len();
            run_lines(&m, rest, ty, rest[2].parse().unwrap(), Some(sk), 0, count);
        }
        "runs" => cmd_runs(&m, rest),
        "list" => {
            // all sequences of length <= L of the element given as cp;ct;ep;ef
            let v: Vec<Vec<u8>> = rest[0].split(';').map(|p| p.split(',').map(|x| x.parse().unwrap()).collect()).collect();
            let mut c = SOLVED;
            c.cp.copy_from_slice(&v[0]);
            c.ct.copy_from_slice(&v[1]);
            c.ep.copy_from_slice(&v[2]);
            c.ef.copy_from_slice(&v[3]);
            let l: usize = rest[1].parse().unwrap();
            let tab = Table::load(l);
            for a in tab.algs_of(c.key(), l) {
                println!("{}", seq::text(&seq::unpack_vec(a)));
            }
        }
        "bf1" => cmd_bf1(&m, rest),
        "bf2" => cmd_bf2(&m, rest),
        _ => eprintln!("unknown subcommand"),
    }
}
