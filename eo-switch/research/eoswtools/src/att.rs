//! Population 3: sampled real attempts.  For each scramble (uniform random states written by eo-to-dr's
//! `eodrtools mkscr`), on each side (normal, and the inverse scramble), each EO axis y and each DR axis x != y:
//! every EO E (canonical, first reach of EO on y) and every RZP R after it (canonical EO-keeping turns, canonical
//! also against E's last turn) with |E| + |R| = 4, 5 or 6 whose end state T reaches its DRM for the first time on
//! the path (the EO's end state included).  The switch: the solver goes to the other side, where the state is
//! W = T^-1 (same EO axis, same DR axis; DRM of T with the two twist directions exchanged).
//! Per total length L and per coset, counts of: switched states W, normal states T, and W with
//!   alt: EO's last turn(s) free (the F/B quarter turns ending E inverted, each subset), min distance;
//!   two: min over the two DR axes of W (EO kept);
//!   all: both.
//! Thresholds k = 5, 6, 7 for alt/two/all.  Output: <prefix>_counts.u32 (arrays below), <prefix>_examples.tsv.

use crate::common::*;
use crate::cubie::Cubie;
use crate::dist::{load_d, EOK};
use rayon::prelude::*;
use std::io::Write;

const NARR: usize = 2 + 3 * 3; // n_sw, n_norm, alt5..7, two5..7, all5..7
const NL: usize = 3; // L = 4, 5, 6
const NB: usize = 20; // scramble batches for cluster-robust errors

struct Acc {
    a: Vec<u32>,         // [L][arr][ix]
    per_drm: Vec<u64>,   // [L][class 45][d 0..15]: switched-state distance histogram
    bt: Vec<u64>,        // [batch 20][L][class 405 = (twist1 * 9 + twist2) * 5 + E out][d 0..15], switched states
    ex: Vec<String>,
}
impl Acc {
    fn new() -> Acc {
        Acc { a: vec![0; NL * NARR * N0], per_drm: vec![0; NL * 45 * 16], bt: vec![0; NB * NL * 405 * 16], ex: Vec::new() }
    }
}

fn ix_of(c: &Ctx, s: &Cubie) -> usize {
    let (co, eo, sl) = c.coords(s);
    debug_assert_eq!(eo, 0);
    co * NSL + sl
}

pub fn cmd(a: &[String]) {
    let c = Ctx::new();
    let d = load_d(&a[0]);
    let scr: Vec<String> = std::fs::read_to_string(&a[1]).unwrap().lines().map(|s| s.to_string()).collect();
    let (first, count): (usize, usize) = (a[2].parse().unwrap(), a[3].parse().unwrap());
    let prefix = &a[4];
    let nex: usize = a.get(5).map_or(200, |s| s.parse().unwrap());
    let drm = DrmOf::new(&c);
    let cls = |ix: usize| -> usize { drm.corners[ix / NSL] as usize * 5 + drm.edges[ix % NSL] as usize / 2 };
    // q[x][y]: the rotation from the view (x -> U/D, y -> F/B) to the view (other x -> U/D, y -> F/B)
    let mut q = [[usize::MAX; 3]; 3];
    let mut rng = Rng::new(5, 5);
    let probes: Vec<Cubie> = (0..4).map(|_| random_cube(&mut rng, false)).collect();
    for y in 0..3 {
        for x in 0..3 {
            if x == y {
                continue;
            }
            let x2 = 3 - x - y;
            q[x][y] = (0..24)
                .find(|&r| probes.iter().all(|p| c.view(&c.view(p, c.rot_pair[x][y]), r) == c.view(p, c.rot_pair[x2][y])))
                .unwrap();
        }
    }
    let end = (first + count).min(scr.len());
    let nth = rayon::current_num_threads();
    let acc = (0..nth)
        .into_par_iter()
        .map(|th| {
          let mut acc = Acc::new();
          for si in (first..end).filter(|si| si % nth == th) {
            let s = c.m.apply(&crate::cubie::SOLVED, &parse(&scr[si]));
            let sides = [s, s.inverse()];
            for side in 0..2 {
                for y in 0..3 {
                    for x in 0..3 {
                        if x == y {
                            continue;
                        }
                        let r = c.rot_pair[x][y];
                        let v0 = c.view(&sides[side], r);
                        let mut eos: Vec<Vec<usize>> = Vec::new();
                        eo_dfs(&c, &v0, 6, NONE, &mut Vec::new(), &mut eos);
                        for e in &eos {
                            let t0 = c.m.apply(&v0, e);
                            let last = *e.last().unwrap_or(&NONE);
                            let mut rz = Vec::new();
                            rzp_dfs(&c, &d, &t0, 6 - e.len(), last, 0u64, &mut rz, &mut |rr: &[usize], t: &Cubie| {
                                let l = e.len() + rr.len();
                                if l < 4 {
                                    return;
                                }
                                let li = l - 4;
                                let w = t.inverse();
                                let ixw = ix_of(&c, &w);
                                let ixt = ix_of(&c, t);
                                let dw = d[ixw];
                                // alternatives: trailing F/B quarter turns of E inverted
                                let mut tq = Vec::new();
                                for k in (0..e.len()).rev() {
                                    if y_quarter_view(e[k]) {
                                        tq.push(k);
                                    } else {
                                        break;
                                    }
                                }
                                let mut dalt = dw;
                                let mut dall;
                                let w2 = c.view(&w, q[x][y]);
                                let dtwo = dw.min(d[ix_of(&c, &w2)]);
                                dall = dtwo;
                                for mask in 1..(1u32 << tq.len()) {
                                    let mut e2 = e.clone();
                                    for (bi, &k) in tq.iter().enumerate() {
                                        if mask >> bi & 1 == 1 {
                                            e2[k] = inv_move(e2[k]);
                                        }
                                    }
                                    let ta = c.m.apply(&c.m.apply(&v0, &e2), rr);
                                    let wa = ta.inverse();
                                    let da = d[ix_of(&c, &wa)];
                                    dalt = dalt.min(da);
                                    dall = dall.min(da).min(d[ix_of(&c, &c.view(&wa, q[x][y]))]);
                                }
                                let base = li * NARR * N0;
                                acc.a[base + ixw] += 1;
                                acc.a[base + N0 + ixt] += 1;
                                for (ki, k) in [5u8, 6, 7].iter().enumerate() {
                                    if dalt <= *k {
                                        acc.a[base + (2 + ki) * N0 + ixw] += 1;
                                    }
                                    if dtwo <= *k {
                                        acc.a[base + (5 + ki) * N0 + ixw] += 1;
                                    }
                                    if dall <= *k {
                                        acc.a[base + (8 + ki) * N0 + ixw] += 1;
                                    }
                                }
                                acc.per_drm[(li * 45 + cls(ixw)) * 16 + dw as usize] += 1;
                                let batch = (si - first) * NB / (end - first);
                                acc.bt[((batch * NL + li) * 405 + cls405(ixw)) * 16 + dw as usize] += 1;
                                if si < first + nex && acc.ex.len() < 1_000_000 {
                                    let real = |seq: &[usize]| text(&seq.iter().map(|&mv| c.m.unview(r, mv)).collect::<Vec<_>>());
                                    acc.ex.push(format!(
                                        "{si}\t{side}\t{}\t{}\t{}\t{}\t{l}\t{}c{}e\t{ixt}\t{ixw}\t{dw}\t{dalt}\t{dtwo}\t{dall}",
                                        AXIS_NAME[y], AXIS_NAME[x], real(e), real(rr),
                                        drm.corners[ixt / NSL], drm.edges[ixt % NSL]
                                    ));
                                }
                            });
                        }
                    }
                }
            }
          }
          acc
        })
        .reduce(Acc::new, |mut x, y| {
            for (p, q) in x.a.iter_mut().zip(&y.a) {
                *p += q;
            }
            for (p, q) in x.per_drm.iter_mut().zip(&y.per_drm) {
                *p += q;
            }
            for (p, q) in x.bt.iter_mut().zip(&y.bt) {
                *p += q;
            }
            x.ex.extend(y.ex);
            x
        });
    let mut buf = Vec::with_capacity(acc.a.len() * 4);
    for v in &acc.a {
        buf.extend_from_slice(&v.to_le_bytes());
    }
    std::fs::write(format!("{prefix}_counts.u32"), &buf).unwrap();
    let mut f = std::fs::File::create(format!("{prefix}_examples.tsv")).unwrap();
    writeln!(f, "scr\tside\teo_axis\tdr_axis\teo\trzp\tlength\tdrm_normal\tix_normal\tix_switched\td_switched\td_eo_last_free\td_two_axes\td_both").unwrap();
    let mut ex = acc.ex;
    ex.sort_by_key(|l| l.split('\t').next().unwrap().parse::<usize>().unwrap());
    for l in ex {
        writeln!(f, "{l}").unwrap();
    }
    let mut g = std::fs::File::create(format!("{prefix}_drm.tsv")).unwrap();
    writeln!(g, "length\tcorners\tedges\t{}", (0..16).map(|k| format!("d{k}")).collect::<Vec<_>>().join("\t")).unwrap();
    for li in 0..NL {
        for k in 0..45 {
            let row = &acc.per_drm[(li * 45 + k) * 16..(li * 45 + k + 1) * 16];
            if row.iter().sum::<u64>() > 0 {
                writeln!(g, "{}\t{}\t{}\t{}", li + 4, k / 5, 2 * (k % 5), row.iter().map(|v| v.to_string()).collect::<Vec<_>>().join("\t")).unwrap();
            }
        }
    }
    let mut bb = Vec::with_capacity(acc.bt.len() * 8);
    for v in &acc.bt {
        bb.extend_from_slice(&v.to_le_bytes());
    }
    std::fs::write(format!("{prefix}_batches.u64"), &bb).unwrap();
    let tot: u64 = acc.a[..].chunks(N0).step_by(1).enumerate().filter(|(i, _)| i % NARR == 0).map(|(_, ch)| ch.iter().map(|&v| v as u64).sum::<u64>()).sum();
    eprintln!("scrambles {first}..{}: {tot} attempts (L = 4..6)", first + count);
}

#[inline]
fn y_quarter_view(mv: usize) -> bool {
    y_quarter(mv, 2)
}

/// EOs on F/B (of the view): canonical, first reach, at most `left` turns.
fn eo_dfs(c: &Ctx, v: &Cubie, left: usize, last: usize, path: &mut Vec<usize>, out: &mut Vec<Vec<usize>>) {
    let e = Ctx::eo(v);
    if e == 0 {
        out.push(path.clone());
        return;
    }
    if c.eodist[e] as usize > left {
        return;
    }
    for mv in 0..18 {
        if canon_ok(last, mv) {
            path.push(mv);
            eo_dfs(c, &c.m.turn(v, mv), left - 1, mv, path, out);
            path.pop();
        }
    }
}

/// RZPs: canonical EO-keeping turns; f is called on every state whose DRM is reached for the first time on the path.
#[allow(clippy::too_many_arguments)]
fn rzp_dfs(c: &Ctx, d: &[u8], t: &Cubie, left: usize, last: usize, seen: u64, path: &mut Vec<usize>, f: &mut dyn FnMut(&[usize], &Cubie)) {
    let (co, _, sl) = c.coords(t);
    let _ = d;
    let drm = drm_class(c, co, sl);
    let mut seen = seen;
    if seen >> drm & 1 == 0 {
        if drm != 0 {
            f(path, t);
        }
        seen |= 1 << drm;
    }
    if left == 0 {
        return;
    }
    for &mv in &EOK {
        if canon_ok(last, mv) {
            path.push(mv);
            rzp_dfs(c, d, &c.m.turn(t, mv), left - 1, mv, seen, path, f);
            path.pop();
        }
    }
}

fn drm_class(c: &Ctx, co: usize, sl: usize) -> usize {
    let _ = c;
    let mut v = co;
    let mut s = 0;
    let mut n = 0;
    for _ in 0..7 {
        let t = v % 3;
        v /= 3;
        s += t;
        if t != 0 {
            n += 1;
        }
    }
    if s % 3 != 0 {
        n += 1;
    }
    n * 5 + edges_out(sl)
}

/// Number of E-slice pieces outside the E slice for slice coordinate sl (bad edges / 2).
fn edges_out(sl: usize) -> usize {
    use std::sync::OnceLock;
    static T: OnceLock<Vec<u8>> = OnceLock::new();
    let t = T.get_or_init(|| {
        let c = Ctx::new();
        let drm = DrmOf::new(&c);
        drm.edges.iter().map(|&e| e / 2).collect()
    });
    t[sl] as usize
}

/// Class of a coset: (number of corners with twist 1) * 9 + (twist 2)) * 5 + E pieces out of the slice.
fn cls405(ix: usize) -> usize {
    let mut v = ix / NSL;
    let (mut n1, mut n2, mut s) = (0, 0, 0);
    for _ in 0..7 {
        let t = v % 3;
        v /= 3;
        s += t;
        if t == 1 { n1 += 1 } else if t == 2 { n2 += 1 }
    }
    match (3 - s % 3) % 3 { 1 => n1 += 1, 2 => n2 += 1, _ => {} }
    (n1 * 9 + n2) * 5 + edges_out(ix % NSL)
}
