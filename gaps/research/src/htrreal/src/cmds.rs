//! The subcommands.

use crate::class::{HALF_MOVES, NCCOS, NEPAT};
use crate::core::{parse_moves, rank_perm, St, MOVE_NAME, NE, NMOVES};
use crate::model::{moves_str, Model, Rng, Sampler, R2};
use crate::routes::{analyse, finishes, ls_optimal, readings, Key};
use rayon::prelude::*;
use std::collections::HashMap;
use std::fs::{self, File};
use std::io::{self, BufRead, BufWriter, Write};
use std::path::Path;
use std::sync::Mutex;
use std::time::Instant;

// ------------------------------------------------------------------------------------------------ dist

pub fn dist(ex: &str, out: &str) -> io::Result<()> {
    let out = Path::new(out);
    fs::create_dir_all(out)?;
    let m = Model::new(Some(Path::new(ex)), None);
    let stab = m.cc.stabilisers(&m.core);
    let nsub = m.cls.sub48_name.len();
    let t0 = Instant::now();
    let hist = (0..m.cc.nclass)
        .into_par_iter()
        .fold(
            || vec![0u64; nsub * 19],
            |mut h, k| {
                let c = m.cc.crep[k];
                let w = (16 / stab[k].len()) as u64;
                let a = m.cls.ccos[c] as usize;
                for e in 0..NE {
                    let sub = m.cls.sub48[a][m.cls.epat[e] as usize] as usize;
                    let base = (k * NE + e) * 12;
                    for s12 in 0..12 {
                        h[sub * 19 + m.table[base + s12] as usize] += w;
                    }
                }
                h
            },
        )
        .reduce(|| vec![0u64; nsub * 19], |mut a, b| {
            a.iter_mut().zip(b).for_each(|(x, y)| *x += y);
            a
        });
    let mut f = BufWriter::new(File::create(out.join("dist48.tsv"))?);
    writeln!(f, "subset\tdepth\tstates")?;
    for s in 0..nsub {
        for d in 0..19 {
            if hist[s * 19 + d] > 0 {
                writeln!(f, "{}\t{}\t{}", m.cls.sub48_name[s], d, hist[s * 19 + d])?;
            }
        }
    }
    eprintln!("dist48: {} states in {:.1}s", hist.iter().sum::<u64>(), t0.elapsed().as_secs_f64());

    // HTR states: DR-optimal finish and half-turn-only finish
    let hc = &m.cls.hc;
    let he: Vec<usize> = (0..NE).filter(|&e| m.cls.epat[e] as usize == m.e0).collect();
    let cidx: HashMap<usize, usize> = hc.iter().enumerate().map(|(i, &c)| (c, i)).collect();
    let eidx: HashMap<usize, usize> = he.iter().enumerate().map(|(i, &e)| (e, i)).collect();
    let n = hc.len() * he.len() * 24;
    let idx = |c: usize, e: usize, s: usize| (cidx[&c] * he.len() + eidx[&e]) * 24 + s;
    let mut hd = vec![0xFFu8; n];
    let mut q = vec![(0usize, 0usize, 0usize)];
    hd[idx(0, 0, 0)] = 0;
    let mut h = 0;
    while h < q.len() {
        let st = q[h];
        h += 1;
        let d0 = hd[idx(st.0, st.1, st.2)];
        for &mv in &HALF_MOVES {
            let s2 = m.mv(mv, st);
            let i2 = idx(s2.0, s2.1, s2.2);
            if hd[i2] == 0xFF {
                hd[i2] = d0 + 1;
                q.push(s2);
            }
        }
    }
    let mut hist_dr = [0u64; 19];
    let mut hist_ht = [0u64; 19];
    let mut nst = 0u64;
    for &c in hc {
        for &e in &he {
            for s in 0..24 {
                if (m.core.cpar[c] ^ m.core.epar[e]) != m.core.spar[s] {
                    continue;
                }
                nst += 1;
                hist_dr[m.depth(c, e, s) as usize] += 1;
                hist_ht[hd[idx(c, e, s)] as usize] += 1;
            }
        }
    }
    let mut f = BufWriter::new(File::create(out.join("htr_states.tsv"))?);
    writeln!(f, "depth\tdr_optimal\thalf_turn_optimal")?;
    for d in 0..19 {
        if hist_dr[d] + hist_ht[d] > 0 {
            writeln!(f, "{}\t{}\t{}", d, hist_dr[d], hist_ht[d])?;
        }
    }
    eprintln!("HTR states: {} (reached by half-turn BFS: {})", nst, q.len());

    // DR -> HTR length per subset (every HTR coset holds the same number of states)
    let mut f = BufWriter::new(File::create(out.join("htr48.tsv"))?);
    writeln!(f, "subset\thtr_len\tcosets")?;
    let mut hh = vec![[0u64; 20]; nsub];
    for a in 0..NCCOS {
        for b in 0..NEPAT {
            hh[m.cls.sub48[a][b] as usize][m.cls.htr_dist[a][b] as usize] += 1;
        }
    }
    for s in 0..nsub {
        for d in 0..20 {
            if hh[s][d] > 0 {
                writeln!(f, "{}\t{}\t{}", m.cls.sub48_name[s], d, hh[s][d])?;
            }
        }
    }
    Ok(())
}

// ------------------------------------------------------------------------------------------------ routes

pub fn routes(ex: &str, ls: &str, n: usize, seed: u64, out: &str, subs: Option<&str>) -> io::Result<()> {
    let out = Path::new(out);
    fs::create_dir_all(out)?;
    let t0 = Instant::now();
    let m = Model::new(Some(Path::new(ex)), Some(Path::new(ls)));
    let sampler = Sampler::new(&m);
    eprintln!("tables loaded in {:.1}s", t0.elapsed().as_secs_f64());
    let nsub = m.cls.sub48_name.len();
    let wanted: Vec<usize> = match subs {
        None => (0..nsub).collect(),
        Some(list) => list
            .split(',')
            .map(|name| {
                let name = name.replace('_', " ");
                m.cls.sub48_name.iter().position(|s| *s == name).unwrap_or_else(|| fatal!("no subset {}", name))
            })
            .collect(),
    };
    // route keys are numbered across all subsets
    let interner: Mutex<(HashMap<Key, u32>, Vec<Key>)> = Mutex::new((HashMap::new(), Vec::new()));
    let cap: u64 = 3_000_000;
    let aliases: Mutex<HashMap<(u32, u32), u32>> = Mutex::new(HashMap::new());
    for &sub in &wanted {
        let ts = Instant::now();
        let name = m.cls.sub48_name[sub].replace(' ', "_");
        let res: Vec<(String, Vec<u64>, Vec<u64>)> = (0..sampler.count(sub, n))
            .into_par_iter()
            .map(|i| {
                let mut rng = Rng(seed ^ ((sub as u64) << 40) ^ (i as u64).wrapping_mul(0x9E37_79B9_7F4A_7C15));
                let x = sampler.draw_i(&m, sub, i, &mut rng);
                let agg = analyse(&m, x, 1, cap, true);
                let xv = m.mv(R2, x);
                let aggv = analyse(&m, xv, 1, cap, true);
                let (c, e) = (x.0, x.1);
                let (ci, ei) = (m.core.cinv[c] as usize, m.core.einv[e] as usize);
                let (lsd, lsn, lsqmin, lsqmax) = ls_optimal(&m, c, e, cap);
                let a = m.cls.ccos[c] as usize;
                let b = m.cls.epat[e] as usize;
                let line = format!(
                    "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
                    m.cls.sub48_name[sub], i, c, e, x.2, agg.d, agg.nopt, agg.nopt_canon, agg.n1, agg.capped as u8,
                    m.htr(c, e), m.htr(ci, ei), m.niss_htr(c, e), agg.best_lin_n, agg.best_lin_i, agg.best_any,
                    agg.best_any1, agg.mask_lin, agg.mask_any, agg.qmin, agg.qmax, agg.q1min, m.cls.cc_qt[a],
                    m.cls.qt_full[a][b], agg.ht_first_n, agg.ht_first_i, lsd, lsn, lsqmin, lsqmax,
                    crate::model::label_name(m.label(c, e)), crate::model::label_name(m.label(ci, ei)),
                    aggv.d, agg.routes.len(), aggv.routes.len(), aggv.capped as u8
                );
                let mut g = interner.lock().unwrap();
                // kept: H keys at <= optimal + 1; F keys (full-chain format) only at the optimal; for X*R2 only H keys
                let mut ids = |a: &crate::routes::StateAgg, var: bool| -> Vec<u64> {
                    let mut v: Vec<u64> = a
                        .routes
                        .iter()
                        .filter(|(k, &(len, _, _))| k.b[0] == b'H' || (!var && len == a.d))
                        .map(|(k, &(len, hl, hany))| {
                            let id = match g.0.get(k) {
                                Some(&id) => id,
                                None => {
                                    let id = g.1.len() as u32;
                                    g.0.insert(*k, id);
                                    g.1.push(*k);
                                    id
                                }
                            };
                            // id; shortest HTR among the readings of the shortest finishes of this route; shortest
                            // HTR over every finish within optimal + 1; finish length minus the optimum
                            (id as u64) << 11 | (hl as u64) << 6 | (hany as u64) << 1 | (len - a.d) as u64
                        })
                        .collect();
                    v.sort_unstable();
                    v
                };
                let r1 = ids(&agg, false);
                let r2 = ids(&aggv, true);
                // mirror aliases (normal-first / inverse-first reading of the same split): global id pairs
                let mut al: Vec<(u32, u32)> = Vec::new();
                for (x, y) in &agg.aliases {
                    if let (Some(&i), Some(&j)) = (g.0.get(x), g.0.get(y)) {
                        al.push((i, j));
                    }
                }
                drop(g);
                {
                    let mut ga = aliases.lock().unwrap();
                    for p in al {
                        *ga.entry(p).or_insert(0u32) += 1;
                    }
                }
                (line, r1, r2)
            })
            .collect();
        let mut f = BufWriter::new(File::create(out.join(format!("states_{}.tsv", name)))?);
        writeln!(
            f,
            "subset\tidx\tc\te\ts\td\tnopt\tnopt_canon\tn1\tcapped\thtrN\thtrI\thtrNiss\tbest_lin_n\tbest_lin_i\tbest_any\tbest_any1\tmask_lin\tmask_any\tqmin\tqmax\tq1min\tccqt\tqtfull\tht_first_n\tht_first_i\tlsd\tls_n\tls_qmin\tls_qmax\tlab_n\tlab_i\tdvar\tnroutes\tnroutes_var\tvar_capped"
        )?;
        let mut fb = BufWriter::new(File::create(out.join(format!("routes_{}.bin", name)))?);
        for (line, r1, r2) in &res {
            writeln!(f, "{}", line)?;
            for r in [r1, r2] {
                fb.write_all(&(r.len() as u64).to_le_bytes())?;
                for x in r {
                    fb.write_all(&x.to_le_bytes())?;
                }
            }
        }
        let nk = interner.lock().unwrap().1.len();
        eprintln!(
            "{:7} {} states in {:.1}s (route keys so far {})",
            m.cls.sub48_name[sub],
            n,
            ts.elapsed().as_secs_f64(),
            nk
        );
    }
    let mut fa = BufWriter::new(File::create(out.join("route_aliases.tsv"))?);
    writeln!(fa, "id_normal_first\tid_inverse_first\tstates")?;
    for ((i, j), c) in aliases.lock().unwrap().iter() {
        writeln!(fa, "{}\t{}\t{}", i, j, c)?;
    }
    let g = interner.lock().unwrap();
    let mut f = BufWriter::new(File::create(out.join("route_keys.tsv"))?);
    writeln!(f, "id\tkey")?;
    for (i, k) in g.1.iter().enumerate() {
        writeln!(f, "{}\t{}", i, k.to_string())?;
    }
    eprintln!("total {:.1}s", t0.elapsed().as_secs_f64());
    Ok(())
}

// ------------------------------------------------------------------------------------------------ helpers

/// A DR scramble (moves applied to the solved cube) or "#c,e,s" -> coordinates.
fn parse_state(m: &Model, s: &str) -> Option<(usize, usize, usize)> {
    let s = s.trim();
    if let Some(rest) = s.strip_prefix('#') {
        let v: Vec<usize> = rest.split(',').map(|x| x.trim().parse().unwrap()).collect();
        return Some((v[0], v[1], v[2]));
    }
    let mv = parse_moves(s.as_bytes(), 512)?;
    let g = mv.iter().fold(St::ID, |g, &x| g.apply_move(x));
    let _ = m;
    Some((rank_perm(&g.c), rank_perm(&g.e), rank_perm(&g.s)))
}

fn inv_str(ms: &[u8]) -> String {
    ms.iter()
        .rev()
        .map(|&x| MOVE_NAME[crate::core::MOVE_INV[x as usize]])
        .collect::<Vec<_>>()
        .join(" ")
}

pub fn trace(ex: &str, cap: usize) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), None);
    let stdin = io::stdin();
    let mut out = BufWriter::new(io::stdout().lock());
    for line in stdin.lock().lines() {
        let line = line?;
        if line.trim().is_empty() {
            continue;
        }
        let Some(x) = parse_state(&m, &line) else {
            writeln!(out, "{{\"error\":\"bad input\"}}")?;
            continue;
        };
        let d = m.depth(x.0, x.1, x.2);
        let mut fins: Vec<String> = Vec::new();
        let mut all: Vec<String> = Vec::new();
        let mut total = 0u64;
        let mut canon = 0u64;
        let mut rd = Vec::new();
        finishes(&m, x, d as usize, u64::MAX, &mut |moves, path| {
            total += 1;
            all.push(format!("\"{}\"", moves_str(moves)));
            canon += moves.windows(2).all(|w| {
                let (a, b) = (crate::model::FACE[w[0] as usize], crate::model::FACE[w[1] as usize]);
                !(a / 2 == b / 2 && a > b)
            }) as u64;
            if fins.len() < cap {
                readings(&m, moves, path, &mut rd);
                let rs: Vec<String> = rd
                    .iter()
                    .map(|r| {
                        format!(
                            "{{\"side\":\"{}\",\"k\":{},\"h\":\"{}\",\"f\":\"{}\",\"htr\":{}}}",
                            if r.inverse_first { "I" } else { "N" },
                            r.k,
                            r.h.to_string(),
                            r.f.to_string(),
                            r.htr_len
                        )
                    })
                    .collect();
                fins.push(format!("{{\"moves\":\"{}\",\"readings\":[{}]}}", moves_str(moves), rs.join(",")));
            }
        });
        writeln!(
            out,
            "{{\"input\":\"{}\",\"c\":{},\"e\":{},\"s\":{},\"d\":{},\"nopt\":{},\"nopt_canon\":{},\"all\":[{}],\"finishes\":[{}]}}",
            line.trim(),
            x.0,
            x.1,
            x.2,
            d,
            total,
            canon,
            all.join(","),
            fins.join(",")
        )?;
    }
    Ok(())
}

pub fn explain(ex: &str) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), None);
    let stdin = io::stdin();
    let mut out = BufWriter::new(io::stdout().lock());
    for line in stdin.lock().lines() {
        let line = line?;
        let parts: Vec<&str> = line.split('\t').collect();
        if parts.len() < 3 {
            continue;
        }
        let x = parse_state(&m, parts[0]).unwrap();
        let want = parts[1];
        let maxlen: usize = parts[2].trim().parse().unwrap();
        let d = m.depth(x.0, x.1, x.2) as usize;
        let mut found: Option<String> = None;
        let mut rd = Vec::new();
        for budget in d..=maxlen {
            finishes(&m, x, budget, 50_000_000, &mut |moves, path| {
                if found.is_some() || moves.len() != budget {
                    return;
                }
                readings(&m, moves, path, &mut rd);
                for r in &rd {
                    if r.h.to_string() == want || r.f.to_string() == want {
                        let n = moves.len();
                        let (normal, inverse) = if r.inverse_first {
                            (moves_str(&moves[..r.k]), inv_str(&moves[r.k..]))
                        } else {
                            (moves_str(&moves[..r.k]), inv_str(&moves[r.k..n]))
                        };
                        found = Some(format!(
                            "{{\"state\":\"{}\",\"scramble\":\"{}\",\"optimal\":{},\"route\":\"{}\",\"finish\":\"{}\",\"length\":{},\"first_side\":\"{}\",\"normal_moves\":\"{}\",\"inverse_moves\":\"{}\",\"htr_len\":{}}}",
                            parts[0], inv_str(moves), d, want, moves_str(moves), n,
                            if r.inverse_first { "inverse" } else { "normal" }, normal, inverse, r.htr_len
                        ));
                        return;
                    }
                }
            });
            if found.is_some() {
                break;
            }
        }
        writeln!(out, "{}", found.unwrap_or_else(|| format!("{{\"state\":\"{}\",\"route\":\"{}\",\"error\":\"not found\"}}", parts[0], want)))?;
        out.flush()?;
    }
    Ok(())
}

pub fn nisshtr(ex: &str) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), None);
    let stdin = io::stdin();
    let mut out = BufWriter::new(io::stdout().lock());
    for line in stdin.lock().lines() {
        let line = line?;
        if line.trim().is_empty() {
            continue;
        }
        let x = parse_state(&m, &line).unwrap();
        let (c, e) = (x.0, x.1);
        let (ci, ei) = (m.core.cinv[c] as usize, m.core.einv[e] as usize);
        writeln!(
            out,
            "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
            line.trim(),
            m.cls.sub48_name[m.sub48(c, e)],
            crate::model::label_name(m.label(c, e)),
            crate::model::label_name(m.label(ci, ei)),
            m.depth(x.0, x.1, x.2),
            m.htr(c, e),
            m.htr(ci, ei),
            m.niss_htr(c, e)
        )?;
    }
    let _ = NMOVES;
    Ok(())
}

// ------------------------------------------------------------------------------------------------ tie

/// One optimal finish per state, ties broken uniformly at random (how docs 171 / allcases and "nissy's first
/// optimal" read a state): for each sampled state, every optimal finish with commuting opposite-face moves in one
/// order (as nissy lists them) gets weight 1 / (their number); its linear (normal-side) F chain gets that weight.
/// Output per subset: chain, expected share under the random tie-break, share of states where some optimal has
/// it, share where every optimal has it.
pub fn tie(ex: &str, n: usize, seed: u64, out: &str) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), None);
    let sampler = Sampler::new(&m);
    let nsub = m.cls.sub48_name.len();
    let mut f = BufWriter::new(File::create(out)?);
    writeln!(f, "subset\tchain\texpected_share\tshare_some\tshare_all\tn_states")?;
    for sub in 0..nsub {
        let res: Vec<HashMap<String, (f64, bool)>> = (0..sampler.count(sub, n))
            .into_par_iter()
            .map(|i| {
                let mut rng = Rng(seed ^ ((sub as u64) << 40) ^ (i as u64).wrapping_mul(0xD1B5_4A32_D192_ED03));
                let x = sampler.draw_i(&m, sub, i, &mut rng);
                let d = m.depth(x.0, x.1, x.2) as usize;
                let mut chains: Vec<String> = Vec::new();
                let mut rd = Vec::new();
                finishes(&m, x, d, u64::MAX, &mut |moves, path| {
                    let canon = moves.windows(2).all(|w| {
                        let (a, b) = (crate::model::FACE[w[0] as usize], crate::model::FACE[w[1] as usize]);
                        !(a / 2 == b / 2 && a > b)
                    });
                    if !canon {
                        return;
                    }
                    readings(&m, moves, path, &mut rd);
                    let r = rd.iter().find(|r| !r.inverse_first && r.k == moves.len()).unwrap();
                    chains.push(r.f.to_string());
                });
                let t = chains.len() as f64;
                let mut h: HashMap<String, (f64, bool)> = HashMap::new();
                for c in &chains {
                    h.entry(c.clone()).or_insert((0.0, false)).0 += 1.0 / t;
                }
                for v in h.values_mut() {
                    v.1 = (v.0 - 1.0).abs() < 1e-9;
                }
                h
            })
            .collect();
        let mut agg: HashMap<String, (f64, usize, usize)> = HashMap::new();
        for h in &res {
            for (k, &(w, all)) in h {
                let e = agg.entry(k.clone()).or_insert((0.0, 0, 0));
                e.0 += w;
                e.1 += 1;
                e.2 += all as usize;
            }
        }
        let mut v: Vec<_> = agg.into_iter().collect();
        v.sort_by(|a, b| b.1 .0.partial_cmp(&a.1 .0).unwrap());
        for (k, (w, s, a)) in v {
            writeln!(f, "{}\t{}\t{:.5}\t{:.5}\t{:.5}\t{}", m.cls.sub48_name[sub], k, w / n as f64, s as f64 / n as f64, a as f64 / n as f64, n)?;
        }
        eprintln!("tie {} done", m.cls.sub48_name[sub]);
    }
    Ok(())
}

// ------------------------------------------------------------------------------------------------ bound (Q8, Q9)

/// Sections of a finish: s[0..=N] = number of half turns before the 1st qt, between qts, after the last qt.
fn sections(moves: &[u8]) -> Vec<u8> {
    let mut s = vec![0u8];
    for &mv in moves {
        if crate::model::is_qt(mv) {
            s.push(0);
        } else {
            *s.last_mut().unwrap() += 1;
        }
    }
    s
}

/// DR bounding read on finishes.  For a finish with sections s_0..s_N (N quarter turns), keeping a window of q
/// consecutive quarter turns (with the half turns around them) as the "q-quarter-turn finish" and calling the
/// moves outside it (a prefix done on normal, a suffix done on inverse) the reduction, the shortest reduction is
/// n - q - max over windows of (s_{t} + ... + s_{t+q}).  Per state and per (finish length - optimum, N): the
/// shortest reduction to 1q and to 2q over all finishes of that length with N quarter turns, and the finish's
/// sections that achieve the 1q minimum.  Same states as `routes` with the same n and seed.
pub fn bound(ex: &str, n: usize, seed: u64, out: &str) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), None);
    let sampler = Sampler::new(&m);
    let nsub = m.cls.sub48_name.len();
    let mut f = BufWriter::new(File::create(out)?);
    writeln!(f, "subset\tidx\tc\te\ts\td\thtrN\thtrI\tcells")?;
    for sub in 0..nsub {
        let t0 = Instant::now();
        let res: Vec<String> = (0..sampler.count(sub, n))
            .into_par_iter()
            .map(|i| {
                let mut rng = Rng(seed ^ ((sub as u64) << 40) ^ (i as u64).wrapping_mul(0x9E37_79B9_7F4A_7C15));
                let x = sampler.draw_i(&m, sub, i, &mut rng);
                let d = m.depth(x.0, x.1, x.2) as usize;
                // (delta, N) -> (min r1, min r2, sections of a finish achieving min r1)
                let mut cell: HashMap<(usize, usize), (u8, u8, Vec<u8>)> = HashMap::new();
                finishes(&m, x, d + 1, 3_000_000, &mut |moves, _| {
                    let s = sections(moves);
                    let nq = s.len() - 1;
                    let len = moves.len();
                    let win = |q: usize| -> u8 {
                        if nq < q {
                            return 99;
                        }
                        let best = (0..=nq - q).map(|t| s[t..=t + q].iter().map(|&x| x as usize).sum::<usize>()).max().unwrap();
                        (len - q - best) as u8
                    };
                    let (r1, r2) = (win(1), win(2));
                    let e = cell.entry((len - d, nq)).or_insert((99, 99, vec![]));
                    if r1 < e.0 {
                        e.0 = r1;
                        e.2 = s.clone();
                    }
                    e.1 = e.1.min(r2);
                });
                let (c, e) = (x.0, x.1);
                let (ci, ei) = (m.core.cinv[c] as usize, m.core.einv[e] as usize);
                let mut cells: Vec<String> = cell
                    .iter()
                    .map(|(&(dl, nq), (r1, r2, s))| {
                        format!("{}:{}:{}:{}:{}", dl, nq, r1, r2, s.iter().map(|v| v.to_string()).collect::<Vec<_>>().join(","))
                    })
                    .collect();
                cells.sort();
                format!(
                    "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
                    m.cls.sub48_name[sub], i, c, e, x.2, d, m.htr(c, e), m.htr(ci, ei), cells.join(";")
                )
            })
            .collect();
        for l in res {
            writeln!(f, "{}", l)?;
        }
        eprintln!("bound {} {:.1}s", m.cls.sub48_name[sub], t0.elapsed().as_secs_f64());
    }
    Ok(())
}

/// Count the reductions a solver writes: pairs (A on normal, B on inverse) of canonical sequences, each empty or
/// ending in a quarter turn, with |A| + |B| <= rmax, after which the state is one quarter turn from HTR (qt_full 1)
/// or two (qt_full 2).  Output per state and length r: number of such pairs and of distinct resulting states.
pub fn redcount(ex: &str, n: usize, seed: u64, rmax: usize, out: &str) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), None);
    let sampler = Sampler::new(&m);
    let nsub = m.cls.sub48_name.len();
    let mut f = BufWriter::new(File::create(out)?);
    writeln!(f, "subset\tidx\td\ttarget_q\tr\tpairs\tstates")?;
    // all canonical sequences up to rmax that are empty or end in a quarter turn, as move lists
    let mut seqs: Vec<Vec<u8>> = vec![vec![]];
    {
        let mut frontier: Vec<(Vec<u8>, u8, u8)> = vec![(vec![], 0xFF, 0xFF)];
        for _ in 0..rmax {
            let mut nxt = Vec::new();
            for (s, lf, la) in &frontier {
                for mv in 0..NMOVES {
                    if !crate::model::canonical_next(mv, *lf, *la) {
                        continue;
                    }
                    let mut t = s.clone();
                    t.push(mv as u8);
                    if crate::model::is_qt(mv as u8) {
                        seqs.push(t.clone());
                    }
                    nxt.push((t, crate::model::FACE[mv], crate::model::axis_run(mv, *lf, *la)));
                }
            }
            frontier = nxt;
        }
    }
    eprintln!("{} reduction halves", seqs.len());
    for sub in 0..nsub {
        let res: Vec<String> = (0..sampler.count(sub, n))
            .into_par_iter()
            .map(|i| {
                let mut rng = Rng(seed ^ ((sub as u64) << 40) ^ (i as u64).wrapping_mul(0x9E37_79B9_7F4A_7C15));
                let x = sampler.draw_i(&m, sub, i, &mut rng);
                let d = m.depth(x.0, x.1, x.2);
                let mut pairs = vec![[0u64; 3]; rmax + 1];
                let mut states: Vec<[std::collections::HashSet<(usize, usize, usize)>; 3]> =
                    (0..=rmax).map(|_| Default::default()).collect();
                for a in &seqs {
                    let mut y = x;
                    for &mv in a {
                        y = m.mv(mv as usize, y);
                    }
                    // inverse side state (X A)^-1, then B
                    let yi = St::unrank(y.0, y.1, y.2).inv();
                    let yi = (rank_perm(&yi.c), rank_perm(&yi.e), rank_perm(&yi.s));
                    for b in &seqs {
                        let r = a.len() + b.len();
                        if r > rmax {
                            continue;
                        }
                        let mut z = yi;
                        for &mv in b {
                            z = m.mv(mv as usize, z);
                        }
                        let q = m.cls.qt_full[m.cls.ccos[z.0] as usize][m.cls.epat[z.1] as usize] as usize;
                        if q == 1 || q == 2 {
                            pairs[r][q] += 1;
                            states[r][q].insert(z);
                        }
                    }
                }
                let mut lines = Vec::new();
                for q in 1..=2 {
                    for r in 0..=rmax {
                        lines.push(format!("{}\t{}\t{}\t{}\t{}\t{}\t{}", m.cls.sub48_name[sub], i, d, q, r, pairs[r][q], states[r][q].len()));
                    }
                }
                lines.join("\n")
            })
            .collect();
        for l in res {
            writeln!(f, "{}", l)?;
        }
        eprintln!("redcount {}", m.cls.sub48_name[sub]);
    }
    Ok(())
}

/// `tie` on leave-slice finishes (corners and U/D edges solved, E slice ignored), the finishes beef beans' sheets use
/// (T2882): every leave-slice-optimal finish with commuting moves in one order, weight 1 / their number, its linear
/// chain of labels at the start and after each quarter turn.
pub fn tie_ls(ex: &str, ls: &str, n: usize, seed: u64, out: &str) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), Some(Path::new(ls)));
    let sampler = Sampler::new(&m);
    let nsub = m.cls.sub48_name.len();
    let mut f = BufWriter::new(File::create(out)?);
    writeln!(f, "subset\tchain\texpected_share\tshare_some\tshare_all\tn_states")?;
    fn rec(m: &Model, c: usize, e: usize, r: usize, lf: u8, la: u8, moves: &mut Vec<u8>, out: &mut Vec<Vec<u8>>) {
        if c == 0 && e == 0 {
            out.push(moves.clone());
            return;
        }
        if r == 0 {
            return;
        }
        for mv in 0..NMOVES {
            if !crate::model::canonical_next(mv, lf, la) {
                continue;
            }
            let (c2, e2) = (m.core.cmove[mv][c] as usize, m.core.emove[mv][e] as usize);
            if m.lsdepth(c2, e2) as usize + 1 > r {
                continue;
            }
            moves.push(mv as u8);
            rec(m, c2, e2, r - 1, crate::model::FACE[mv], crate::model::axis_run(mv, lf, la), moves, out);
            moves.pop();
        }
    }
    for sub in 0..nsub {
        let res: Vec<HashMap<String, (f64, bool)>> = (0..sampler.count(sub, n))
            .into_par_iter()
            .map(|i| {
                let mut rng = Rng(seed ^ ((sub as u64) << 40) ^ (i as u64).wrapping_mul(0xD1B5_4A32_D192_ED03));
                let x = sampler.draw_i(&m, sub, i, &mut rng);
                let d = m.lsdepth(x.0, x.1) as usize;
                let mut fins = Vec::new();
                rec(&m, x.0, x.1, d, 0xFF, 0xFF, &mut Vec::new(), &mut fins);
                let mut chains = Vec::new();
                for mv in &fins {
                    let canon = mv.windows(2).all(|w| {
                        let (a, b) = (crate::model::FACE[w[0] as usize], crate::model::FACE[w[1] as usize]);
                        !(a / 2 == b / 2 && a > b)
                    });
                    if !canon {
                        continue;
                    }
                    let (mut c, mut e) = (x.0, x.1);
                    let mut labs = vec![crate::model::label_name(m.label(c, e))];
                    for &t in mv {
                        c = m.core.cmove[t as usize][c] as usize;
                        e = m.core.emove[t as usize][e] as usize;
                        if crate::model::is_qt(t) {
                            labs.push(crate::model::label_name(m.label(c, e)));
                        }
                    }
                    chains.push(format!("F:{}", labs.join(" > ")));
                }
                let t = chains.len() as f64;
                let mut h: HashMap<String, (f64, bool)> = HashMap::new();
                for c in &chains {
                    h.entry(c.clone()).or_insert((0.0, false)).0 += 1.0 / t;
                }
                for v in h.values_mut() {
                    v.1 = (v.0 - 1.0).abs() < 1e-9;
                }
                h
            })
            .collect();
        let mut agg: HashMap<String, (f64, usize, usize)> = HashMap::new();
        for h in &res {
            for (k, &(w, all)) in h {
                let e = agg.entry(k.clone()).or_insert((0.0, 0, 0));
                e.0 += w;
                e.1 += 1;
                e.2 += all as usize;
            }
        }
        let mut v: Vec<_> = agg.into_iter().collect();
        v.sort_by(|a, b| b.1 .0.partial_cmp(&a.1 .0).unwrap());
        for (k, (w, s, a)) in v {
            writeln!(f, "{}\t{}\t{:.5}\t{:.5}\t{:.5}\t{}", m.cls.sub48_name[sub], k, w / n as f64, s as f64 / n as f64, a as f64 / n as f64, n)?;
        }
    }
    Ok(())
}

/// A uniform random state of a subset with a given optimal (for witnesses of extreme cases): prints "#c,e,s".
pub fn find(ex: &str, sub: &str, depth: u8, seed: u64) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), None);
    let sampler = Sampler::new(&m);
    let name = sub.replace('_', " ");
    let s = m.cls.sub48_name.iter().position(|x| *x == name).unwrap_or_else(|| fatal!("no subset {}", name));
    let found = (0..64u64).into_par_iter().find_map_any(|t| {
        let mut rng = Rng(seed ^ (t << 50));
        for _ in 0..2_000_000_000u64 {
            let x = sampler.draw(&m, s, &mut rng);
            if m.depth(x.0, x.1, x.2) == depth {
                return Some(x);
            }
        }
        None
    });
    match found {
        Some(x) => println!("#{},{},{}", x.0, x.1, x.2),
        None => println!("none"),
    }
    Ok(())
}

/// leave-slice histogram per 48-subset, over every DR state (each E-slice placement counts 12 times the class weight / 12 = w per slice state)
pub fn lsdist(ls: &str) -> io::Result<()> {
    let m = Model::new(None, Some(Path::new(ls)));
    let stab = m.cc.stabilisers(&m.core);
    let nsub = m.cls.sub48_name.len();
    let mut h = vec![0u64; nsub * 19];
    for k in 0..m.cc.nclass {
        let c = m.cc.crep[k];
        let w = (16 / stab[k].len()) as u64;
        let a = m.cls.ccos[c] as usize;
        for e in 0..NE {
            let sub = m.cls.sub48[a][m.cls.epat[e] as usize] as usize;
            h[sub * 19 + m.ls[k * NE + e] as usize] += w * 12;
        }
    }
    for s in 0..nsub { for d in 0..19 { if h[s * 19 + d] > 0 { println!("{}\t{}\t{}", m.cls.sub48_name[s], d, h[s * 19 + d]); } } }
    Ok(())
}

// ------------------------------------------------------------------------------------------------ label (gaps fork)

/// stdin "c e s" -> subset48, optimal DR finish, optimal leave-slice, own label, inverse label, linear HTR normal /
/// inverse, shortest NISS HTR, optimum of X*R2.
pub fn label(ex: &str, ls: &str) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), Some(Path::new(ls)));
    let stdin = io::stdin();
    let lines: Vec<String> = stdin.lock().lines().collect::<Result<_, _>>()?;
    let res: Vec<String> = lines
        .par_iter()
        .map(|line| {
            let v: Vec<usize> = line.split_whitespace().take(3).map(|x| x.parse().unwrap()).collect();
            let (c, e, s) = (v[0], v[1], v[2]);
            let (ci, ei) = (m.core.cinv[c] as usize, m.core.einv[e] as usize);
            let xv = m.mv(R2, (c, e, s));
            format!(
                "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
                m.cls.sub48_name[m.sub48(c, e)], m.depth(c, e, s), m.lsdepth(c, e),
                crate::model::label_name(m.label(c, e)), crate::model::label_name(m.label(ci, ei)),
                m.htr(c, e), m.htr(ci, ei), m.niss_htr(c, e), m.depth(xv.0, xv.1, xv.2)
            )
        })
        .collect();
    let mut out = BufWriter::new(io::stdout().lock());
    writeln!(out, "subset\td\tlsd\tlab_n\tlab_i\thtrN\thtrI\thtrNiss\tdvar")?;
    for r in res {
        writeln!(out, "{}", r)?;
    }
    Ok(())
}
