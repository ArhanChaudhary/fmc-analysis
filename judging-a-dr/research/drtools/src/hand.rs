//! Statistics of the exact finish against what a solver can read off a DR by hand.
//!
//! * `drtools lsbfs <out.u8>` — optimal "leave slice" length of every DR state: the fewest DR moves that solve
//!   the corners and the eight U/D-layer edges, the E slice left as it falls.  One byte per reduced
//!   (corner class, U/D-edge coordinate), index `class * 40320 + e`.
//! * `drtools hcensus <bfsdir> <ls.u8> <outdir>` — one pass over all DR states, several joint histograms of
//!   hand-readable quantities with the exact optimal finish (see the `h*.csv` headers).
//! * `drtools ncensus <bfsdir> <outdir>` — one pass that looks at the ten neighbours of every state: the
//!   finish when the last DR move may be inverted, and how many first moves are optimal.
//!
//! Hand-readable quantities used here (all exact, all per state):
//!   subset            Mallard's 48 subsets
//!   coset             the HTR coset (which corners and edges are bad, and the corner case): 420 x 70
//!   hN, hI            shortest DR->HTR on the normal / inverse state
//!   L, Lp             optimal corner solution; the same among solutions whose number of side half turns has
//!                     the parity of the E-slice permutation (the only ones that can be completed for free)
//!   G                 "setup + HTR" bound for finishes with the minimum number of quarter turns:
//!                     max(hN + sI, hI + sN), s = fewest half turns before a quarter turn that lowers the
//!                     quarter-turn count (Levi's formula at 1qt, trangium's 2q bound at 2qt)
//!   pairs             corner/edge pairs in the U and D layers by the colours of the touching stickers:
//!                     true (same/same), pseudo (opposite/opposite), side semi (top opposite, side same),
//!                     top semi (top same, side opposite); and corner/E-slice-edge pairs
//!   ls                optimal leave-slice length

use crate::class::{corner_only_lengths, Classes, HALF_MOVES, NCCOS, NEPAT};
use crate::core::{unrank_perm, Core, MOVE_IS_QT, NC, NE, NMOVES, NS, NSYM};
use crate::par;
use crate::reduced::{CornerClasses, ExactData, RowDepths, SliceIndex, MAXD, ROW};
use rayon::prelude::*;
use std::collections::HashMap;
use std::fs::{self, File};
use std::io::{self, BufWriter, Write};
use std::path::Path;
use std::sync::atomic::{AtomicU8, Ordering::Relaxed};

const UNSET: u8 = 0xFF;
/// First side half turn (R2 L2 F2 B2 are moves 6..10).
const FIRST_SIDE: usize = 6;

// ---------------------------------------------------------------------------------------------------------
// leave-slice BFS

pub fn run_lsbfs(out: &Path) -> io::Result<i32> {
    let core = Core::new();
    let classes = CornerClasses::new(&core);
    let nclass = classes.nclass;
    let crep = &classes.crep;
    let stab = classes.stabilisers(&core);
    let mut mcl = vec![[0usize; NMOVES]; nclass];
    let mut msy = vec![[0usize; NMOVES]; nclass];
    for k in 0..nclass {
        for m in 0..NMOVES {
            let c2 = core.cmove[m][crep[k]] as usize;
            mcl[k][m] = classes.cclass[c2] as usize;
            msy[k][m] = classes.csymto[c2] as usize;
        }
    }
    let n = nclass * NE;
    let dep: Vec<AtomicU8> = (0..n).map(|_| AtomicU8::new(UNSET)).collect();
    dep[classes.cclass[0] as usize * NE].store(0, Relaxed);
    let mut total: u64 = 0;
    for depth in 0u8.. {
        // count the current depth: an entry stands for 16/|stab| corner-edge states, each with 12 E slices
        let cnt: u64 = (0..nclass)
            .into_par_iter()
            .map(|k| {
                let b = dep[k * NE..(k + 1) * NE]
                    .iter()
                    .filter(|x| x.load(Relaxed) == depth)
                    .count() as u64;
                b * (16 / stab[k].len() as u64) * 12
            })
            .sum();
        if cnt == 0 {
            break;
        }
        total += cnt;
        eprintln!(
            "leave-slice depth {:2}: {} states, total {}",
            depth, cnt, total
        );
        (0..nclass).into_par_iter().with_max_len(4).for_each(|k| {
            for e in 0..NE {
                if dep[k * NE + e].load(Relaxed) != depth {
                    continue;
                }
                for m in 0..NMOVES {
                    let (k2, sym) = (mcl[k][m], msy[k][m]);
                    let e2 = core.esym[sym][core.emove[m][e] as usize] as usize;
                    if dep[k2 * NE + e2].load(Relaxed) != UNSET {
                        continue;
                    }
                    // every image under the stabiliser of the representative (stab[k2][0] is the identity)
                    for &t in &stab[k2] {
                        dep[k2 * NE + core.esym[t as usize][e2] as usize].store(depth + 1, Relaxed);
                    }
                }
            }
        });
    }
    eprintln!("total {} (expected 19508428800)", total);
    let bytes: Vec<u8> = dep.iter().map(|x| x.load(Relaxed)).collect();
    fs::write(out, bytes)?;
    Ok(if total == 19_508_428_800 { 0 } else { 2 })
}

// ---------------------------------------------------------------------------------------------------------
// small tables

/// `lp[c * 2 + p]`: shortest corner solution of corner coordinate `c` with (number of side half turns) = p mod 2.
fn corner_lengths_by_side_parity(core: &Core) -> Vec<u8> {
    let mut len = vec![UNSET; NC * 2];
    let mut queue: Vec<usize> = Vec::with_capacity(NC * 2);
    len[0] = 0;
    queue.push(0);
    let mut head = 0;
    while head < queue.len() {
        let x = queue[head];
        head += 1;
        let (c, p) = (x / 2, x % 2);
        for m in 0..NMOVES {
            let y = core.cmove[m][c] as usize * 2 + (p ^ (m >= FIRST_SIDE) as usize);
            if len[y] == UNSET {
                len[y] = len[x] + 1;
                queue.push(y);
            }
        }
    }
    len
}

/// `s[a * 70 + b]`: fewest half turns before some quarter turn lowers the quarter-turn count of the coset.
fn setup_lengths(cls: &Classes) -> Vec<u8> {
    let n = NCCOS * NEPAT;
    let mut s = vec![0u8; n];
    let mut stamp = vec![u32::MAX; n];
    let mut queue: Vec<(usize, u8)> = Vec::new();
    for x in 0..n {
        let q = cls.qt_full[x / NEPAT][x % NEPAT];
        if q == 0 {
            continue;
        }
        queue.clear();
        queue.push((x, 0));
        stamp[x] = x as u32;
        let mut head = 0;
        let mut found = UNSET;
        while head < queue.len() {
            let (y, h) = queue[head];
            head += 1;
            let (a, b) = (y / NEPAT, y % NEPAT);
            if (0..NMOVES).any(|m| {
                MOVE_IS_QT[m] && cls.qt_full[cls.ccos_mv[a][m]][cls.epat_mv[b][m]] + 1 == q
            }) {
                found = h;
                break; // breadth-first: the first hit is the nearest
            }
            for &m in &HALF_MOVES {
                let z = cls.ccos_mv[a][m] * NEPAT + cls.epat_mv[b][m];
                if stamp[z] != x as u32 {
                    stamp[z] = x as u32;
                    queue.push((z, h + 1));
                }
            }
        }
        if found == UNSET {
            fatal!(
                "coset {} (qt {}) has no quarter turn that lowers the count",
                x,
                q
            );
        }
        s[x] = found;
    }
    s
}

/// Tetrad of a corner position / piece: 0 for UFR UBL DFL DBR, 1 for the others.
const TETRAD: [u8; 8] = [0, 1, 0, 1, 1, 0, 1, 0];
/// Side colours of a corner piece: [F/B colour, R/L colour], faces numbered F 0, L 1, B 2, R 3.
const CORNER_COL: [[u8; 2]; 8] = [
    [0, 3],
    [0, 1],
    [2, 1],
    [2, 3],
    [0, 3],
    [0, 1],
    [2, 1],
    [2, 3],
];
/// Side face of a U/D-layer edge position = side colour of the edge piece with that home.
const EDGE_FACE: [u8; 8] = [0, 1, 2, 3, 0, 1, 2, 3];
/// The 16 touching (corner position, edge position) pairs inside the U and the D layer.
const ADJ: [(usize, usize); 16] = [
    (0, 0),
    (0, 3),
    (1, 0),
    (1, 1),
    (2, 1),
    (2, 2),
    (3, 2),
    (3, 3),
    (4, 4),
    (4, 7),
    (5, 4),
    (5, 5),
    (6, 5),
    (6, 6),
    (7, 6),
    (7, 7),
];
/// E-slice position touching each corner position.
const E_ADJ: [usize; 8] = [0, 1, 2, 3, 0, 1, 2, 3];
/// [F/B colour, R/L colour] of an E-slice piece.
const SLICE_COL: [[u8; 2]; 4] = [[0, 3], [0, 1], [2, 1], [2, 3]];

/// (true, pseudo, side-semi, top-semi) pair counts of the U and D layers.
fn pair_counts(cp: &[u8; 8], ep: &[u8; 8]) -> [u8; 4] {
    let mut n = [0u8; 4];
    for &(p, q) in &ADJ {
        let (cpiece, epiece) = (cp[p] as usize, ep[q] as usize);
        let face = EDGE_FACE[q]; // the side face both stickers are on
        let good = TETRAD[cpiece] == TETRAD[p];
        // a corner in its own tetrad shows its F/B colour on F/B faces; out of it, on R/L faces
        let axis = (face & 1) as usize ^ (!good) as usize;
        let ccol = CORNER_COL[cpiece][axis];
        let ecol = EDGE_FACE[epiece];
        let top_same = (cpiece < 4) == (epiece < 4);
        let kind = if ccol == ecol {
            if top_same {
                0
            } else {
                2
            }
        } else if ccol == ecol ^ 2 {
            if top_same {
                3
            } else {
                1
            }
        } else {
            continue;
        };
        n[kind] += 1;
    }
    n
}

/// Number of corners that form a block with the E-slice edge next to them.
fn slice_pairs(cp: &[u8; 8], sp: &[u8; 4]) -> u8 {
    (0..8)
        .filter(|&p| {
            let cpiece = cp[p] as usize;
            TETRAD[cpiece] == TETRAD[p] && CORNER_COL[cpiece] == SLICE_COL[sp[E_ADJ[p]] as usize]
        })
        .count() as u8
}

/// Bit p set = the corner at position p is out of its tetrad ("bad").
fn bad_corner_mask(cp: &[u8; 8]) -> u8 {
    (0..8).fold(0, |m, p| {
        m | (((TETRAD[cp[p] as usize] != TETRAD[p]) as u8) << p)
    })
}

fn write_dense(
    path: &Path,
    header: &str,
    h: &[u64],
    radices: &[usize],
    mut row: impl FnMut(&[usize]) -> String,
) -> io::Result<()> {
    let mut out = BufWriter::new(File::create(path)?);
    writeln!(out, "{}", header)?;
    let mut digits = vec![0usize; radices.len()];
    for (i, &count) in h.iter().enumerate() {
        if count == 0 {
            continue;
        }
        let mut x = i;
        for j in (0..radices.len()).rev() {
            digits[j] = x % radices[j];
            x /= radices[j];
        }
        writeln!(out, "{},{}", row(&digits), count)?;
    }
    out.flush()
}

// ---------------------------------------------------------------------------------------------------------
// the feature census

const NH: usize = 14; // HTR lengths 0..=13
const NHP: usize = NH * (NH + 1) / 2; // (hmin, hmax) pairs
const NL: usize = 14; // corner lengths 0..=13
const NDL: usize = 7; // Lp - L, capped at 6
const NG: usize = 32;

pub fn run_hcensus(bfsdir: &Path, lsfile: &Path, outdir: &Path) -> io::Result<i32> {
    fs::create_dir_all(outdir)?;
    let core = Core::new();
    let cls = Classes::new(&core);
    let slice = SliceIndex::new(&core);
    let data = ExactData::open(bfsdir);
    let nsub = cls.sub48_name.len();
    let lsd = fs::read(lsfile)?;
    if lsd.len() != data.nclass * NE {
        fatal!(
            "{}: {} bytes, expected {}",
            lsfile.display(),
            lsd.len(),
            data.nclass * NE
        );
    }
    let clen = corner_only_lengths(&core);
    let lpar = corner_lengths_by_side_parity(&core);
    let setup = setup_lengths(&cls);
    let sperm: Vec<[u8; 4]> = (0..NS).map(unrank_perm::<4>).collect();

    let n1 = NCCOS * NEPAT * NH * MAXD; // coset, hI, depth
    let n2 = nsub * NHP * NL * NDL * 2 * MAXD; // sub, (hmin,hmax), L, dLp, par, depth
    let n3 = nsub * MAXD * MAXD; // sub, depth, ls
    let n4 = nsub * NH * NH * MAXD; // sub, hN, hI, ls
    let n6 = nsub * NL * NDL * 2 * MAXD; // sub, L, dLp, par, ls
    let n7 = nsub * NH * NG * MAXD; // sub, hmax, G, depth
    let n9 = nsub * 17 * 9 * MAXD; // sub, true pairs, slice pairs, depth
    struct Local {
        h1: Vec<u64>,
        h2: Vec<u64>,
        h3: Vec<u64>,
        h4: Vec<u64>,
        h6: Vec<u64>,
        h7: Vec<u64>,
        h9: Vec<u64>,
        pairs: HashMap<u64, u64>,
        row: RowDepths,
    }
    let parts = par::for_each_with_local(
        data.nclass,
        4,
        || Local {
            h1: vec![0; n1],
            h2: vec![0; n2],
            h3: vec![0; n3],
            h4: vec![0; n4],
            h6: vec![0; n6],
            h7: vec![0; n7],
            h9: vec![0; n9],
            pairs: HashMap::new(),
            row: RowDepths::new(),
        },
        |local, k| {
            let dep = local.row.load(&data, k);
            let c = data.crep[k];
            let ci = core.cinv[c] as usize;
            let w = (16 / data.nstab[k]) as u64;
            let (a, ai) = (cls.ccos[c] as usize, cls.ccos[ci] as usize);
            let l = clen[c] as usize;
            let cp: [u8; 8] = unrank_perm(c);
            for e in 0..NE {
                let ei = core.einv[e] as usize;
                let (b, bi) = (cls.epat[e] as usize, cls.epat[ei] as usize);
                let (hn, hi) = (cls.htr_dist[a][b] as usize, cls.htr_dist[ai][bi] as usize);
                let sub = cls.sub48[a][b] as usize;
                let par = (core.cpar[c] ^ core.epar[e]) as usize;
                let dl = ((lpar[c * 2 + par] as usize) - l).min(NDL - 1);
                let ls = lsd[k * NE + e] as usize;
                let g = if cls.qt_full[a][b] == 0 {
                    0
                } else {
                    (hn + setup[ai * NEPAT + bi] as usize).max(hi + setup[a * NEPAT + b] as usize)
                }
                .min(NG - 1);
                let ep: [u8; 8] = unrank_perm(e);
                let pc = pair_counts(&cp, &ep);
                let (hmin, hmax) = (hn.min(hi), hn.max(hi));
                let hp = hmax * (hmax + 1) / 2 + hmin;

                let mut cnt = [0u64; MAXD];
                for s12 in 0..12 {
                    let d = dep[e * 12 + s12] as usize;
                    if d >= MAXD {
                        fatal!("unvisited state class {} e {} s {}", k, e, s12);
                    }
                    cnt[d] += w;
                    let sp = &sperm[slice.from12[par][s12] as usize];
                    let ne = slice_pairs(&cp, sp) as usize;
                    local.h9[((sub * 17 + pc[0] as usize) * 9 + ne) * MAXD + d] += w;
                }
                let pkey = (sub as u64) << 32
                    | (pc[0] as u64) << 26
                    | (pc[1] as u64) << 20
                    | (pc[2] as u64) << 14
                    | (pc[3] as u64) << 8;
                for d in 0..MAXD {
                    let x = cnt[d];
                    if x == 0 {
                        continue;
                    }
                    local.h1[((a * NEPAT + b) * NH + hi) * MAXD + d] += x;
                    local.h2[((((sub * NHP + hp) * NL + l) * NDL + dl) * 2 + par) * MAXD + d] += x;
                    local.h3[(sub * MAXD + d) * MAXD + ls] += x;
                    local.h7[((sub * NH + hmax) * NG + g) * MAXD + d] += x;
                    *local.pairs.entry(pkey | d as u64).or_insert(0) += x;
                }
                let all = 12 * w;
                local.h4[((sub * NH + hn) * NH + hi) * MAXD + ls] += all;
                local.h6[(((sub * NL + l) * NDL + dl) * 2 + par) * MAXD + ls] += all;
            }
        },
    );
    let mut pairs: HashMap<u64, u64> = HashMap::new();
    let (mut h1, mut h2, mut h3, mut h4, mut h6, mut h7, mut h9) = (
        vec![0u64; n1],
        vec![0u64; n2],
        vec![0u64; n3],
        vec![0u64; n4],
        vec![0u64; n6],
        vec![0u64; n7],
        vec![0u64; n9],
    );
    for local in parts {
        for (t, p) in [
            (&mut h1, &local.h1),
            (&mut h2, &local.h2),
            (&mut h3, &local.h3),
            (&mut h4, &local.h4),
            (&mut h6, &local.h6),
            (&mut h7, &local.h7),
            (&mut h9, &local.h9),
        ] {
            for (x, y) in t.iter_mut().zip(p.iter()) {
                *x += *y;
            }
        }
        for (key, x) in local.pairs {
            *pairs.entry(key).or_insert(0) += x;
        }
    }
    let total: u64 = h3.iter().sum();
    eprintln!("states counted: {} (expected 19508428800)", total);

    // per coset: symmetry orbit, masks, lengths
    let name = |sub: usize| cls.sub48_name[sub].clone();
    let orbit: Vec<usize> = (0..NCCOS * NEPAT)
        .map(|x| {
            let (c, e) = (cls.ccos_rep[x / NEPAT], cls.epat_rep[x % NEPAT]);
            (0..NSYM)
                .map(|s| {
                    cls.ccos[core.csym[s][c] as usize] as usize * NEPAT
                        + cls.epat[core.esym[s][e] as usize] as usize
                })
                .min()
                .unwrap()
        })
        .collect();
    {
        let mut out = BufWriter::new(File::create(outdir.join("cosets.csv"))?);
        writeln!(
            out,
            "coset,orbit,subset,bad_corner_mask,bad_edge_mask,qt_corners,qt_min,hN,setup"
        )?;
        for x in 0..NCCOS * NEPAT {
            let (a, b) = (x / NEPAT, x % NEPAT);
            let cp: [u8; 8] = unrank_perm(cls.ccos_rep[a]);
            // an edge is bad when an M-slice edge (UF UB DF DB) sits in an S-slice position or the reverse
            let emask = cls.epat_mask[b] ^ 0b0101_0101;
            writeln!(
                out,
                "{},{},{},{},{},{},{},{},{}",
                x,
                orbit[x],
                name(cls.sub48[a][b] as usize),
                bad_corner_mask(&cp),
                emask,
                cls.cc_qt[a],
                cls.qt_full[a][b],
                cls.htr_dist[a][b],
                setup[x]
            )?;
        }
        out.flush()?;
    }
    write_dense(
        &outdir.join("h1_coset.csv"),
        "coset,hI,depth,count",
        &h1,
        &[NCCOS * NEPAT, NH, MAXD],
        |d| format!("{},{},{}", d[0], d[1], d[2]),
    )?;
    write_dense(
        &outdir.join("h2_lengths.csv"),
        "subset,hmin,hmax,L,dLp,parity,depth,count",
        &h2,
        &[nsub, NHP, NL, NDL, 2, MAXD],
        |d| {
            let hmax = (0..NH).rev().find(|&m| m * (m + 1) / 2 <= d[1]).unwrap();
            let hmin = d[1] - hmax * (hmax + 1) / 2;
            format!(
                "{},{},{},{},{},{},{}",
                name(d[0]),
                hmin,
                hmax,
                d[2],
                d[3],
                d[4],
                d[5]
            )
        },
    )?;
    write_dense(
        &outdir.join("h3_leaveslice.csv"),
        "subset,depth,ls,count",
        &h3,
        &[nsub, MAXD, MAXD],
        |d| format!("{},{},{}", name(d[0]), d[1], d[2]),
    )?;
    write_dense(
        &outdir.join("h4_htr_leaveslice.csv"),
        "subset,hN,hI,ls,count",
        &h4,
        &[nsub, NH, NH, MAXD],
        |d| format!("{},{},{},{}", name(d[0]), d[1], d[2], d[3]),
    )?;
    write_dense(
        &outdir.join("h6_corner_leaveslice.csv"),
        "subset,L,dLp,parity,ls,count",
        &h6,
        &[nsub, NL, NDL, 2, MAXD],
        |d| format!("{},{},{},{},{}", name(d[0]), d[1], d[2], d[3], d[4]),
    )?;
    write_dense(
        &outdir.join("h7_setup_bound.csv"),
        "subset,hmax,G,depth,count",
        &h7,
        &[nsub, NH, NG, MAXD],
        |d| format!("{},{},{},{}", name(d[0]), d[1], d[2], d[3]),
    )?;
    write_dense(
        &outdir.join("h9_true_slice_pairs.csv"),
        "subset,true_pairs,slice_pairs,depth,count",
        &h9,
        &[nsub, 17, 9, MAXD],
        |d| format!("{},{},{},{}", name(d[0]), d[1], d[2], d[3]),
    )?;
    {
        let mut out = BufWriter::new(File::create(outdir.join("h5_pairs.csv"))?);
        writeln!(
            out,
            "subset,true_pairs,pseudo_pairs,side_semi,top_semi,depth,count"
        )?;
        let mut keys: Vec<(&u64, &u64)> = pairs.iter().collect();
        keys.sort();
        for (&key, &count) in keys {
            writeln!(
                out,
                "{},{},{},{},{},{},{}",
                name((key >> 32) as usize),
                (key >> 26) & 63,
                (key >> 20) & 63,
                (key >> 14) & 63,
                (key >> 8) & 63,
                key & 255,
                count
            )?;
        }
        out.flush()?;
    }
    Ok(if total == 19_508_428_800 { 0 } else { 2 })
}

// ---------------------------------------------------------------------------------------------------------
// second feature census: corner cases on both sides, pairs on both sides, edge length, combined reads

/// Optimal length of solving the eight U/D-layer edges alone (corners and E slice ignored).
fn edge_only_lengths(core: &Core) -> Vec<u8> {
    let mut len = vec![UNSET; NE];
    let mut queue: Vec<usize> = Vec::with_capacity(NE);
    len[0] = 0;
    queue.push(0);
    let mut head = 0;
    while head < queue.len() {
        let e = queue[head];
        head += 1;
        for m in 0..NMOVES {
            let e2 = core.emove[m][e] as usize;
            if len[e2] == UNSET {
                len[e2] = len[e] + 1;
                queue.push(e2);
            }
        }
    }
    len
}

/// Corner cases: classes of the 420 corner cosets under the 16 symmetries and under turning both layers
/// (left multiplication by U D', which is how the server counts bad corners).
/// Returns (class representative of each coset, the sorted representatives, case number 0..ncc of each coset).
fn corner_case_tables(core: &Core, cls: &Classes) -> (Vec<usize>, Vec<usize>, Vec<usize>) {
    let corbit: Vec<usize> = (0..NCCOS)
        .map(|a| {
            let mut seen = vec![false; NCCOS];
            let mut stack = vec![a];
            seen[a] = true;
            while let Some(x) = stack.pop() {
                let images = (0..NSYM)
                    .map(|s| cls.ccos[core.csym[s][cls.ccos_rep[x]] as usize] as usize)
                    .chain(std::iter::once(cls.lmul_c[x]));
                for y in images {
                    if !seen[y] {
                        seen[y] = true;
                        stack.push(y);
                    }
                }
            }
            (0..NCCOS).find(|&y| seen[y]).unwrap()
        })
        .collect();
    let mut reps: Vec<usize> = corbit.clone();
    reps.sort();
    reps.dedup();
    let ccase: Vec<usize> = corbit
        .iter()
        .map(|o| reps.binary_search(o).unwrap())
        .collect();
    (corbit, reps, ccase)
}

pub fn run_hcensus2(bfsdir: &Path, outdir: &Path) -> io::Result<i32> {
    fs::create_dir_all(outdir)?;
    let core = Core::new();
    let cls = Classes::new(&core);
    let data = ExactData::open(bfsdir);
    let nsub = cls.sub48_name.len();
    let clen = corner_only_lengths(&core);
    let lpar = corner_lengths_by_side_parity(&core);
    let elen = edge_only_lengths(&core);

    let (corbit, reps, ccase) = corner_case_tables(&core, &cls);
    let ncc = reps.len();
    {
        let (mut lmin, mut lmax, mut size) = (vec![UNSET; ncc], vec![0u8; ncc], vec![0usize; ncc]);
        let mut hist = vec![[0usize; NL]; ncc];
        // an example with the fewest bad corners and, among those, the shortest corner solution
        let mut example = vec![(usize::MAX, 0usize); ncc];
        for c in 0..NC {
            let x = ccase[cls.ccos[c] as usize];
            lmin[x] = lmin[x].min(clen[c]);
            lmax[x] = lmax[x].max(clen[c]);
            size[x] += 1;
            hist[x][clen[c] as usize] += 1;
            let cp: [u8; 8] = unrank_perm(c);
            let key = bad_corner_mask(&cp).count_ones() as usize * 100 + clen[c] as usize;
            if key < example[x].0 {
                example[x] = (key, c);
            }
        }
        // a shortest move sequence from solved to a corner coordinate: walk down the distance table
        let scramble = |target: usize| -> String {
            let mut moves: Vec<&str> = Vec::new();
            let mut c = target;
            while clen[c] != 0 {
                // find the predecessor p and move m with cmove[m][p] == c and clen[p] == clen[c] - 1
                let (p, m) = (0..NMOVES)
                    .map(|m| (core.cmove[crate::core::MOVE_INV[m]][c] as usize, m))
                    .find(|&(p, _)| clen[p] + 1 == clen[c])
                    .unwrap();
                moves.push(crate::core::MOVE_NAME[m]);
                c = p;
            }
            moves.reverse();
            moves.join(" ")
        };
        let mut out = BufWriter::new(File::create(outdir.join("corner_cases.csv"))?);
        writeln!(out, "corner_case,corner_subset,bad_corner_mask,qt_corners,corner_states,L_min,L_max,L_mean,cosets,example_scramble,one_qt_reaches,qt_down_counts,qt_down_cases,qt_down_same_layer")?;
        for x in 0..ncc {
            let a = reps[x];
            let cp: [u8; 8] = unrank_perm(example[x].1);
            let mean = (0..NL).map(|l| l * hist[x][l]).sum::<usize>() as f64 / size[x] as f64;
            // corner subsets with one quarter turn less that a single U or D quarter turn can reach from this case
            let mut next: Vec<&str> = (0..NCCOS)
                .filter(|&y| corbit[y] == a)
                .flat_map(|y| (0..NMOVES).filter(|&m| MOVE_IS_QT[m]).map(move |m| (y, m)))
                .map(|(y, m)| cls.ccos_mv[y][m])
                .filter(|&z| cls.cc_qt[z] + 1 == cls.cc_qt[a])
                .map(|z| crate::class::SUBSET_NAME[cls.cc_subset[z] as usize])
                .collect();
            next.sort();
            next.dedup();
            // which of the four quarter turns lower the count: how many per coset, the cases they lead to,
            // and whether the turned layer is the one holding more bad corners ("more"), fewer ("fewer")
            // or the same number ("equal")
            let mut counts: Vec<usize> = Vec::new();
            let mut to: Vec<usize> = Vec::new();
            let mut layer: Vec<&str> = Vec::new();
            for y in (0..NCCOS).filter(|&y| corbit[y] == a) {
                let cp: [u8; 8] = unrank_perm(cls.ccos_rep[y]);
                let mask = bad_corner_mask(&cp);
                let (bu, bd) = ((mask & 0x0F).count_ones(), (mask >> 4).count_ones());
                let mut n = 0;
                for m in (0..NMOVES).filter(|&m| MOVE_IS_QT[m]) {
                    let z = cls.ccos_mv[y][m];
                    if cls.cc_qt[z] + 1 == cls.cc_qt[y] {
                        n += 1;
                        to.push(ccase[z]);
                        let (mine, other) = if m < 3 { (bu, bd) } else { (bd, bu) };
                        layer.push(if mine > other {
                            "more"
                        } else if mine < other {
                            "fewer"
                        } else {
                            "equal"
                        });
                    }
                }
                counts.push(n);
            }
            counts.sort();
            counts.dedup();
            to.sort();
            to.dedup();
            layer.sort();
            layer.dedup();
            writeln!(
                out,
                "{},{},{},{},{},{},{},{:.2},{},{},{},{},{},{}",
                x,
                crate::class::SUBSET_NAME[cls.cc_subset[a] as usize],
                bad_corner_mask(&cp),
                cls.cc_qt[a],
                size[x],
                lmin[x],
                lmax[x],
                mean,
                corbit.iter().filter(|&&o| o == a).count(),
                scramble(example[x].1),
                next.join(" "),
                counts
                    .iter()
                    .map(|n| n.to_string())
                    .collect::<Vec<_>>()
                    .join("/"),
                to.iter()
                    .map(|n| n.to_string())
                    .collect::<Vec<_>>()
                    .join("/"),
                layer.join("/")
            )?;
        }
        out.flush()?;
    }

    {
        // every corner permutation with its corner case (for working out how to tell look-alike cases apart)
        let mut out = BufWriter::new(File::create(outdir.join("corner_perm_cases.csv"))?);
        writeln!(out, "perm,corner_case")?;
        for c in 0..NC {
            let cp: [u8; 8] = unrank_perm(c);
            let text: String = cp.iter().map(|x| x.to_string()).collect();
            writeln!(out, "{},{}", text, ccase[cls.ccos[c] as usize])?;
        }
        out.flush()?;
    }
    const NTP: usize = 6; // true pairs capped at 5
    const NTB: usize = 9; // true pairs capped at 8
    const NLE: usize = 16;
    let n1 = nsub * ncc * ncc * MAXD; // sub, corner case normal, corner case inverse, depth
    let n2 = nsub * NHP * NL * 2 * NTP * MAXD; // sub, (hmin,hmax), L, parity misfit, true pairs, depth
    let n3 = nsub * NTB * NTB * MAXD; // sub, true pairs normal, inverse, depth
    let n4 = nsub * NL * NLE * MAXD; // sub, L, edge length, depth
    struct Local {
        k1: Vec<u64>,
        k2: Vec<u64>,
        k3: Vec<u64>,
        k4: Vec<u64>,
        row: RowDepths,
    }
    let parts = par::for_each_with_local(
        data.nclass,
        4,
        || Local {
            k1: vec![0; n1],
            k2: vec![0; n2],
            k3: vec![0; n3],
            k4: vec![0; n4],
            row: RowDepths::new(),
        },
        |local, k| {
            let dep = local.row.load(&data, k);
            let c = data.crep[k];
            let ci = core.cinv[c] as usize;
            let w = (16 / data.nstab[k]) as u64;
            let (a, ai) = (cls.ccos[c] as usize, cls.ccos[ci] as usize);
            let l = clen[c] as usize;
            let (cp, cpi): ([u8; 8], [u8; 8]) = (unrank_perm(c), unrank_perm(ci));
            for e in 0..NE {
                let ei = core.einv[e] as usize;
                let (b, bi) = (cls.epat[e] as usize, cls.epat[ei] as usize);
                let (hn, hi) = (cls.htr_dist[a][b] as usize, cls.htr_dist[ai][bi] as usize);
                let sub = cls.sub48[a][b] as usize;
                let par = (core.cpar[c] ^ core.epar[e]) as usize;
                let misfit = (lpar[c * 2 + par] as usize > l) as usize;
                let (ep, epi): ([u8; 8], [u8; 8]) = (unrank_perm(e), unrank_perm(ei));
                let (tp, tpi) = (
                    pair_counts(&cp, &ep)[0] as usize,
                    pair_counts(&cpi, &epi)[0] as usize,
                );
                let (hmin, hmax) = (hn.min(hi), hn.max(hi));
                let hp = hmax * (hmax + 1) / 2 + hmin;
                let le = (elen[e] as usize).min(NLE - 1);
                let i1 = ((sub * ncc + ccase[a]) * ncc + ccase[ai]) * MAXD;
                let i2 =
                    ((((sub * NHP + hp) * NL + l) * 2 + misfit) * NTP + tp.min(NTP - 1)) * MAXD;
                let i3 = ((sub * NTB + tp.min(NTB - 1)) * NTB + tpi.min(NTB - 1)) * MAXD;
                let i4 = ((sub * NL + l) * NLE + le) * MAXD;
                for s12 in 0..12 {
                    let d = dep[e * 12 + s12] as usize;
                    local.k1[i1 + d] += w;
                    local.k2[i2 + d] += w;
                    local.k3[i3 + d] += w;
                    local.k4[i4 + d] += w;
                }
            }
        },
    );
    let (mut k1, mut k2, mut k3, mut k4) = (
        vec![0u64; n1],
        vec![0u64; n2],
        vec![0u64; n3],
        vec![0u64; n4],
    );
    for local in parts {
        for (t, p) in [
            (&mut k1, &local.k1),
            (&mut k2, &local.k2),
            (&mut k3, &local.k3),
            (&mut k4, &local.k4),
        ] {
            for (x, y) in t.iter_mut().zip(p.iter()) {
                *x += *y;
            }
        }
    }
    let total: u64 = k4.iter().sum();
    eprintln!("states counted: {} (expected 19508428800)", total);
    let name = |sub: usize| cls.sub48_name[sub].clone();
    write_dense(
        &outdir.join("k1_corner_cases.csv"),
        "subset,corner_case_normal,corner_case_inverse,depth,count",
        &k1,
        &[nsub, ncc, ncc, MAXD],
        |d| format!("{},{},{},{}", name(d[0]), d[1], d[2], d[3]),
    )?;
    write_dense(
        &outdir.join("k2_combined.csv"),
        "subset,hmin,hmax,L,parity_misfit,true_pairs,depth,count",
        &k2,
        &[nsub, NHP, NL, 2, NTP, MAXD],
        |d| {
            let hmax = (0..NH).rev().find(|&m| m * (m + 1) / 2 <= d[1]).unwrap();
            let hmin = d[1] - hmax * (hmax + 1) / 2;
            format!(
                "{},{},{},{},{},{},{}",
                name(d[0]),
                hmin,
                hmax,
                d[2],
                d[3],
                d[4],
                d[5]
            )
        },
    )?;
    write_dense(
        &outdir.join("k3_pairs_both_sides.csv"),
        "subset,true_pairs_normal,true_pairs_inverse,depth,count",
        &k3,
        &[nsub, NTB, NTB, MAXD],
        |d| format!("{},{},{},{}", name(d[0]), d[1], d[2], d[3]),
    )?;
    write_dense(
        &outdir.join("k4_edge_length.csv"),
        "subset,L,edge_length,depth,count",
        &k4,
        &[nsub, NL, NLE, MAXD],
        |d| format!("{},{},{},{}", name(d[0]), d[1], d[2], d[3]),
    )?;
    Ok(if total == 19_508_428_800 { 0 } else { 2 })
}

// ---------------------------------------------------------------------------------------------------------
// third feature census: the quick reads together (corner case on both sides, true pairs, HTR on both sides)

pub fn run_hcensus3(bfsdir: &Path, outdir: &Path) -> io::Result<i32> {
    fs::create_dir_all(outdir)?;
    let core = Core::new();
    let cls = Classes::new(&core);
    let data = ExactData::open(bfsdir);
    let (_, _, ccase) = corner_case_tables(&core, &cls);
    // key = subset, corner case normal, corner case inverse, true pairs (capped at 5), hmin, hmax ; value = counts by depth
    struct Local {
        h: HashMap<u64, [u64; MAXD]>,
        row: RowDepths,
    }
    let parts = par::for_each_with_local(
        data.nclass,
        4,
        || Local { h: HashMap::new(), row: RowDepths::new() },
        |local, k| {
            let dep = local.row.load(&data, k);
            let c = data.crep[k];
            let ci = core.cinv[c] as usize;
            let w = (16 / data.nstab[k]) as u64;
            let (a, ai) = (cls.ccos[c] as usize, cls.ccos[ci] as usize);
            let cp: [u8; 8] = unrank_perm(c);
            // the corner case pair is symmetric in normal/inverse for the statistics: store it ordered
            let (c1, c2) = (ccase[a].min(ccase[ai]), ccase[a].max(ccase[ai]));
            for e in 0..NE {
                let ei = core.einv[e] as usize;
                let (b, bi) = (cls.epat[e] as usize, cls.epat[ei] as usize);
                let (hn, hi) = (cls.htr_dist[a][b] as usize, cls.htr_dist[ai][bi] as usize);
                let sub = cls.sub48[a][b] as usize;
                let ep: [u8; 8] = unrank_perm(e);
                let tp = (pair_counts(&cp, &ep)[0] as usize).min(5);
                let key = ((((((sub * 64 + c1) * 64 + c2) * 8 + tp) * 16 + hn.min(hi)) * 16) + hn.max(hi)) as u64;
                let entry = local.h.entry(key).or_insert([0; MAXD]);
                for s12 in 0..12 {
                    entry[dep[e * 12 + s12] as usize] += w;
                }
            }
        },
    );
    let mut h: HashMap<u64, [u64; MAXD]> = HashMap::new();
    for local in parts {
        for (key, v) in local.h {
            let entry = h.entry(key).or_insert([0; MAXD]);
            for d in 0..MAXD {
                entry[d] += v[d];
            }
        }
    }
    let mut keys: Vec<&u64> = h.keys().collect();
    keys.sort();
    let mut out = BufWriter::new(File::create(outdir.join("k5_quick_reads.csv"))?);
    writeln!(out, "subset,corner_case_a,corner_case_b,true_pairs,hmin,hmax,depth,count")?;
    let mut total = 0u64;
    for &key in keys {
        let v = h[&key];
        let (hmax, hmin, tp, c2, c1, sub) =
            (key % 16, key / 16 % 16, key / 256 % 8, key / 2048 % 64, key / 131072 % 64, key / 8388608);
        for d in 0..MAXD {
            if v[d] != 0 {
                total += v[d];
                writeln!(out, "{},{},{},{},{},{},{},{}", cls.sub48_name[sub as usize], c1, c2, tp, hmin, hmax, d, v[d])?;
            }
        }
    }
    out.flush()?;
    eprintln!("states counted: {} (expected 19508428800); classes: {}", total, h.len());
    Ok(if total == 19_508_428_800 { 0 } else { 2 })
}

// ---------------------------------------------------------------------------------------------------------
// neighbours: an invertible last move, and the number of optimal first moves

pub fn run_ncensus(bfsdir: &Path, outdir: &Path) -> io::Result<i32> {
    fs::create_dir_all(outdir)?;
    let core = Core::new();
    let cls = Classes::new(&core);
    let classes = CornerClasses::new(&core);
    let slice = SliceIndex::new(&core);
    let data = ExactData::open(bfsdir);
    let nsub = cls.sub48_name.len();
    let nclass = data.nclass;
    if nclass != classes.nclass || data.crep != classes.crep {
        fatal!("classes.bin does not match the corner classes of this build");
    }

    // the whole table in memory, one byte per reduced state (1.34 GB)
    let mut table = vec![UNSET; nclass * ROW];
    table
        .par_chunks_mut(ROW)
        .enumerate()
        .for_each_init(RowDepths::new, |row, (k, chunk)| {
            chunk.copy_from_slice(row.load(&data, k));
        });
    eprintln!("table loaded");

    let mut mcl = vec![[0usize; NMOVES]; nclass];
    let mut msy = vec![[0usize; NMOVES]; nclass];
    for k in 0..nclass {
        for m in 0..NMOVES {
            let c2 = core.cmove[m][classes.crep[k]] as usize;
            mcl[k][m] = classes.cclass[c2] as usize;
            msy[k][m] = classes.csymto[c2] as usize;
        }
    }
    let n8 = nsub * MAXD * MAXD; // sub, depth, depth after one given side half turn
    let n8b = nsub * MAXD * MAXD; // sub, depth, best depth after any of the four side half turns
    let n10 = nsub * MAXD * 11 * 11; // sub, depth, moves that go down, moves that stay level
    struct Local {
        h8: Vec<u64>,
        h8b: Vec<u64>,
        h10: Vec<u64>,
    }
    let parts = par::for_each_with_local(
        nclass,
        4,
        || Local {
            h8: vec![0; n8],
            h8b: vec![0; n8b],
            h10: vec![0; n10],
        },
        |local, k| {
            let c = classes.crep[k];
            let w = (16 / data.nstab[k]) as u64;
            let a = cls.ccos[c] as usize;
            let base = k * ROW;
            for e in 0..NE {
                let sub = cls.sub48[a][cls.epat[e] as usize] as usize;
                let par = (core.cpar[c] ^ core.epar[e]) as usize;
                // (target row, target edge coordinate, symmetry) of each move
                let mut tgt = [(0usize, 0usize); NMOVES];
                for m in 0..NMOVES {
                    let sym = msy[k][m];
                    tgt[m] = (
                        mcl[k][m] * ROW + core.esym[sym][core.emove[m][e] as usize] as usize * 12,
                        sym,
                    );
                }
                for s12 in 0..12 {
                    let d = table[base + e * 12 + s12] as usize;
                    let s = slice.from12[par][s12] as usize;
                    let (mut down, mut level, mut best) = (0usize, 0usize, MAXD);
                    for m in 0..NMOVES {
                        let (group, sym) = tgt[m];
                        let s2 = core.ssym[sym][core.smove[m][s] as usize] as usize;
                        let d2 = table[group + slice.to12[s2] as usize] as usize;
                        down += (d2 + 1 == d) as usize;
                        level += (d2 == d) as usize;
                        if m >= FIRST_SIDE {
                            local.h8[(sub * MAXD + d) * MAXD + d2] += w;
                            best = best.min(d2);
                        }
                    }
                    local.h8b[(sub * MAXD + d) * MAXD + best] += w;
                    local.h10[((sub * MAXD + d) * 11 + down) * 11 + level] += w;
                }
            }
        },
    );
    let (mut h8, mut h8b, mut h10) = (vec![0u64; n8], vec![0u64; n8b], vec![0u64; n10]);
    for local in parts {
        for (t, p) in [
            (&mut h8, &local.h8),
            (&mut h8b, &local.h8b),
            (&mut h10, &local.h10),
        ] {
            for (x, y) in t.iter_mut().zip(p.iter()) {
                *x += *y;
            }
        }
    }
    let total: u64 = h8b.iter().sum();
    eprintln!("states counted: {} (expected 19508428800)", total);
    let name = |sub: usize| cls.sub48_name[sub].clone();
    write_dense(
        &outdir.join("h8_last_move.csv"),
        "subset,depth,depth_after_side_half_turn,count",
        &h8,
        &[nsub, MAXD, MAXD],
        |d| format!("{},{},{}", name(d[0]), d[1], d[2]),
    )?;
    write_dense(
        &outdir.join("h8b_best_of_four.csv"),
        "subset,depth,best_depth_after_any_side_half_turn,count",
        &h8b,
        &[nsub, MAXD, MAXD],
        |d| format!("{},{},{}", name(d[0]), d[1], d[2]),
    )?;
    write_dense(
        &outdir.join("h10_first_moves.csv"),
        "subset,depth,moves_down,moves_level,count",
        &h10,
        &[nsub, MAXD, 11, 11],
        |d| format!("{},{},{},{}", name(d[0]), d[1], d[2], d[3]),
    )?;
    Ok(if total == 19_508_428_800 { 0 } else { 2 })
}

// ---------------------------------------------------------------------------------------------------------
// `drtools read <bfsdir> <ls.u8>`: everything a solver can read off one DR, plus the truth, for states on stdin

const CORNER_POS: [&str; 8] = ["UFR", "UFL", "UBL", "UBR", "DFR", "DFL", "DBL", "DBR"];
const EDGE_POS: [&str; 8] = ["UF", "UL", "UB", "UR", "DF", "DL", "DB", "DR"];

fn names(mask: usize, table: &[&str; 8]) -> String {
    let v: Vec<&str> = (0..8)
        .filter(|&p| mask >> p & 1 == 1)
        .map(|p| table[p])
        .collect();
    if v.is_empty() {
        "-".to_string()
    } else {
        v.join(",")
    }
}

pub fn run_read(bfsdir: &Path, lsfile: &Path) -> io::Result<i32> {
    use crate::core::{parse_moves, rank_perm, St, MOVE_NAME};
    use crate::reduced::{exact_depth, open_depth_files};
    use std::io::BufRead;
    let core = Core::new();
    let cls = Classes::new(&core);
    let classes = CornerClasses::new(&core);
    let slice = SliceIndex::new(&core);
    let depth_files = open_depth_files(bfsdir);
    let lsd = fs::read(lsfile)?;
    let clen = corner_only_lengths(&core);
    let lpar = corner_lengths_by_side_parity(&core);
    let setup = setup_lengths(&cls);
    let (_, _, ccase) = corner_case_tables(&core, &cls);

    // reduced coordinates of a state: (corner class, conjugated edge coordinate, conjugated slice coordinate)
    let reduce = |g: &St| -> (usize, usize, usize) {
        let c = rank_perm(&g.c);
        let sym = classes.csymto[c] as usize;
        (
            classes.cclass[c] as usize,
            core.esym[sym][rank_perm(&g.e)] as usize,
            core.ssym[sym][rank_perm(&g.s)] as usize,
        )
    };
    let depth = |g: &St| -> usize {
        let (k, e, s) = reduce(g);
        exact_depth(&depth_files, k * ROW + e * 12 + slice.to12[s] as usize).unwrap_or(99)
    };
    let seq = |moves: &[usize]| {
        moves
            .iter()
            .map(|&m| MOVE_NAME[m])
            .collect::<Vec<_>>()
            .join(" ")
    };

    let mut out = io::stdout().lock();
    for line in io::stdin().lock().lines() {
        let line = line?;
        let text = line.trim();
        if text.is_empty() {
            continue;
        }
        let g = if text.as_bytes()[0].is_ascii_digit() {
            let nums: Vec<u8> = text
                .split_whitespace()
                .filter_map(|t| t.parse().ok())
                .collect();
            if nums.len() != 20 {
                writeln!(out, "error: need 20 numbers\n")?;
                continue;
            }
            let mut g = St::ID;
            g.c.copy_from_slice(&nums[0..8]);
            g.e.copy_from_slice(&nums[8..16]);
            g.s.copy_from_slice(&nums[16..20]);
            g
        } else {
            match parse_moves(text.as_bytes(), 200) {
                Some(moves) => moves.iter().fold(St::ID, |g, &m| g.apply_move(m)),
                None => {
                    writeln!(out, "error: not a DR move sequence\n")?;
                    continue;
                }
            }
        };
        let gi = g.inv();
        let (c, e, s) = (rank_perm(&g.c), rank_perm(&g.e), rank_perm(&g.s));
        let (ci, ei) = (rank_perm(&gi.c), rank_perm(&gi.e));
        let par = core.spar[s] as usize;
        if (core.cpar[c] ^ core.epar[e]) as usize != par {
            writeln!(out, "error: not a reachable DR state\n")?;
            continue;
        }
        let (a, b) = (cls.ccos[c] as usize, cls.epat[e] as usize);
        let (ai, bi) = (cls.ccos[ci] as usize, cls.epat[ei] as usize);
        writeln!(out, "subset: {}", cls.sub48_name[cls.sub48[a][b] as usize])?;
        writeln!(out, "corner_case: {} {}", ccase[a], ccase[ai])?;
        writeln!(
            out,
            "bad_corners: {} | {}",
            names(bad_corner_mask(&g.c) as usize, &CORNER_POS),
            names(bad_corner_mask(&gi.c) as usize, &CORNER_POS)
        )?;
        writeln!(
            out,
            "bad_edges: {} | {}",
            names(cls.epat_mask[b] ^ 0b0101_0101, &EDGE_POS),
            names(cls.epat_mask[bi] ^ 0b0101_0101, &EDGE_POS)
        )?;
        // true pairs, by where they sit
        let mut pairs = Vec::new();
        for &(p, q) in &ADJ {
            let (cpiece, epiece) = (g.c[p] as usize, g.e[q] as usize);
            let good = TETRAD[cpiece] == TETRAD[p];
            let axis = (EDGE_FACE[q] & 1) as usize ^ (!good) as usize;
            if CORNER_COL[cpiece][axis] == EDGE_FACE[epiece] && (cpiece < 4) == (epiece < 4) {
                pairs.push(format!("{}+{}", CORNER_POS[p], EDGE_POS[q]));
            }
        }
        writeln!(out, "true_pairs: {} {}", pairs.len(), pairs.join(" "))?;
        writeln!(out, "slice_pairs: {}", slice_pairs(&g.c, &g.s))?;
        // shortest HTR on both sides
        let htr_path = |mut a: usize, mut b: usize| {
            let mut moves = Vec::new();
            while cls.htr_dist[a][b] != 0 {
                let m = (0..NMOVES)
                    .find(|&m| {
                        cls.htr_dist[cls.ccos_mv[a][m]][cls.epat_mv[b][m]] + 1 == cls.htr_dist[a][b]
                    })
                    .unwrap();
                moves.push(m);
                (a, b) = (cls.ccos_mv[a][m], cls.epat_mv[b][m]);
            }
            moves
        };
        writeln!(out, "htr: {} {}", cls.htr_dist[a][b], cls.htr_dist[ai][bi])?;
        writeln!(out, "htr_normal: {}", seq(&htr_path(a, b)))?;
        writeln!(out, "htr_inverse: {}", seq(&htr_path(ai, bi)))?;
        writeln!(
            out,
            "setup: {} {}",
            setup[a * NEPAT + b],
            setup[ai * NEPAT + bi]
        )?;
        writeln!(out, "qt: {} {}", cls.cc_qt[a], cls.qt_full[a][b])?;
        // corner solutions: optimal, and optimal for each parity of the number of side half turns
        writeln!(out, "e_parity: {}", par)?;
        writeln!(
            out,
            "corner_length: {} {} {}",
            clen[c],
            lpar[c * 2],
            lpar[c * 2 + 1]
        )?;
        for p0 in 0..2 {
            let (mut y, mut r) = (c, p0);
            let mut moves = Vec::new();
            while lpar[y * 2 + r] != 0 {
                let m = (0..NMOVES)
                    .find(|&m| {
                        let y2 = core.cmove[m][y] as usize;
                        lpar[y2 * 2 + (r ^ (m >= FIRST_SIDE) as usize)] + 1 == lpar[y * 2 + r]
                    })
                    .unwrap();
                moves.push(m);
                y = core.cmove[m][y] as usize;
                r ^= (m >= FIRST_SIDE) as usize;
            }
            writeln!(
                out,
                "corner_solution_{}: {}",
                if p0 == 0 { "even" } else { "odd" },
                seq(&moves)
            )?;
        }
        // the truth
        let d = depth(&g);
        let (k, e2, _) = reduce(&g);
        writeln!(out, "leave_slice: {}", lsd[k * NE + e2])?;
        writeln!(out, "optimal: {}", d)?;
        let after: Vec<String> = (FIRST_SIDE..NMOVES)
            .map(|m| format!("{}:{}", MOVE_NAME[m], depth(&g.apply_move(m))))
            .collect();
        writeln!(out, "after_side_half_turn: {}", after.join(" "))?;
        let first: Vec<&str> = (0..NMOVES)
            .filter(|&m| depth(&g.apply_move(m)) + 1 == d)
            .map(|m| MOVE_NAME[m])
            .collect();
        writeln!(out, "optimal_first_moves: {}", first.join(" "))?;
        let mut moves = Vec::new();
        let mut x = g;
        while depth(&x) != 0 {
            let dx = depth(&x);
            let m = (0..NMOVES)
                .find(|&m| depth(&x.apply_move(m)) + 1 == dx)
                .unwrap();
            moves.push(m);
            x = x.apply_move(m);
        }
        writeln!(out, "optimal_finish: {}", seq(&moves))?;
        writeln!(out)?;
        out.flush()?;
    }
    Ok(0)
}

// ---------------------------------------------------------------------------------------------------------
// `drtools witness <bfsdir> <ls.u8> <listing>`: one explicit DR state for every existence claim in the report

/// The two bad corners of a 2c state sit one above the other (after turning a layer that has 3 or 4 bad).
fn stacked_pair(mask: u8) -> bool {
    let (mut u, mut d) = (mask & 0x0F, mask >> 4);
    if u.count_ones() > 2 {
        u ^= 0x0F;
    }
    if d.count_ones() > 2 {
        d ^= 0x0F;
    }
    u.count_ones() == 1 && u == d
}

#[derive(Clone, Copy)]
struct Best {
    score: i64,
    at: (usize, usize, usize),
}
const NONE: Best = Best {
    score: i64::MIN,
    at: (0, 0, 0),
};
fn keep(slot: &mut Best, score: i64, at: (usize, usize, usize)) {
    // deterministic whatever the thread schedule: higher score, then the smaller state
    if score > slot.score || (score == slot.score && at < slot.at) {
        *slot = Best { score, at };
    }
}

pub fn run_witness(bfsdir: &Path, lsfile: &Path, listing: &Path) -> io::Result<i32> {
    use crate::core::{parse_moves, rank_perm, St, MOVE_INV, MOVE_NAME};
    use crate::quot::{Quot, E630};
    use crate::reduced::{exact_depth, open_depth_files};
    let core = Core::new();
    let cls = Classes::new(&core);
    let classes = CornerClasses::new(&core);
    let slice = SliceIndex::new(&core);
    let data = ExactData::open(bfsdir);
    let depth_files = open_depth_files(bfsdir);
    let lsd = fs::read(lsfile)?;
    let nsub = cls.sub48_name.len();
    let clen = corner_only_lengths(&core);
    let setup = setup_lengths(&cls);
    let (_, _, ccase) = corner_case_tables(&core, &cls);
    const FLOOR: [usize; 6] = [0, 1, 3, 5, 7, 9];

    // slots: per subset 0 longest, 1 shortest, 2 optimal == longer HTR, 3 optimal below the setup bound;
    // then the single ones
    const PER: usize = 4;
    const H13: usize = 0;
    const H13B: usize = 1;
    const LS18: usize = 2;
    const SHORT3: usize = 3;
    const ZRULE: usize = 4;
    const STACK5: usize = 5;
    const STACK4: usize = 6;
    const FLOORQ: usize = 7; // 7..12: corner qt 1..5
    const SLICE1: usize = 12;
    const SLICE2: usize = 13;
    const SLICEMAX: usize = 14;
    const NSINGLE: usize = 15;
    struct Local {
        per: Vec<Best>,
        single: Vec<Best>,
        cl: HashMap<u32, (u8, (usize, usize, usize), u8, (usize, usize, usize), u64)>,
        // per corner case and optimal length: a state (one with four bad edges if there is one), and how many
        cc: Vec<Best>,
        cc_hist: Vec<u64>,
        row: RowDepths,
    }
    let parts = par::for_each_with_local(
        data.nclass,
        4,
        || Local {
            per: vec![NONE; nsub * PER],
            single: vec![NONE; NSINGLE],
            cl: HashMap::new(),
            cc: vec![NONE; 64 * MAXD],
            cc_hist: vec![0; 64 * MAXD],
            row: RowDepths::new(),
        },
        |local, k| {
            let dep = local.row.load(&data, k);
            let c = data.crep[k];
            let ci = core.cinv[c] as usize;
            let w = (16 / data.nstab[k]) as u64;
            let (a, ai) = (cls.ccos[c] as usize, cls.ccos[ci] as usize);
            let (cp, cpi): ([u8; 8], [u8; 8]) = (unrank_perm(c), unrank_perm(ci));
            let both_stacked =
                stacked_pair(bad_corner_mask(&cp)) && stacked_pair(bad_corner_mask(&cpi));
            for e in 0..NE {
                let ei = core.einv[e] as usize;
                let (b, bi) = (cls.epat[e] as usize, cls.epat[ei] as usize);
                let (hn, hi) = (cls.htr_dist[a][b] as usize, cls.htr_dist[ai][bi] as usize);
                let sub = cls.sub48[a][b] as usize;
                let name = &cls.sub48_name[sub];
                let (sn, si) = (
                    setup[a * NEPAT + b] as usize,
                    setup[ai * NEPAT + bi] as usize,
                );
                let g = if cls.qt_full[a][b] == 0 {
                    0
                } else {
                    (hn + si).max(hi + sn)
                };
                let ls = lsd[k * NE + e];
                let q = cls.cc_qt[a] as usize;
                let key = (((sub * 64 + ccase[a]) * 64 + ccase[ai]) * 16 + hn) * 16 + hi;
                let mut seen = false;
                for s12 in 0..12 {
                    let d = dep[e * 12 + s12] as usize;
                    let at = (k, e, s12);
                    let di = d as i64;
                    keep(&mut local.per[sub * PER], di, at);
                    keep(
                        &mut local.cc[ccase[a] * MAXD + d],
                        name.ends_with("4e") as i64,
                        at,
                    );
                    local.cc_hist[ccase[a] * MAXD + d] += w;
                    keep(&mut local.per[sub * PER + 1], -di, at);
                    if d == hn.max(hi) {
                        keep(&mut local.per[sub * PER + 2], di, at);
                    }
                    if d < g {
                        keep(&mut local.per[sub * PER + 3], (g - d) as i64 * 100 - di, at);
                    }
                    if hn == 13 {
                        keep(&mut local.single[H13], -di, at);
                        if hi == 13 {
                            keep(&mut local.single[H13B], -di, at);
                        }
                    }
                    if ls == 18 {
                        keep(&mut local.single[LS18], -di, at);
                    }
                    let cost = d - ls as usize;
                    if cost == 1 {
                        keep(&mut local.single[SLICE1], -di, at);
                    }
                    if cost == 2 {
                        keep(&mut local.single[SLICE2], -di, at);
                    }
                    keep(&mut local.single[SLICEMAX], cost as i64 * 100 - di, at);
                    if cls.qt_full[a][b] == 1 && sn + 1 > hn && si + 1 > hi {
                        keep(&mut local.single[SHORT3], -di, at);
                    }
                    if name == "4c3 4e" && hn.min(hi) >= 9 {
                        keep(&mut local.single[ZRULE], -di, at);
                    }
                    if both_stacked && name.starts_with("2c5") {
                        keep(&mut local.single[STACK5], -di, at);
                    }
                    if both_stacked && name.starts_with("2c4") {
                        keep(&mut local.single[STACK4], -di, at);
                    }
                    if (1..=5).contains(&q) && hn == FLOOR[q] && hi == FLOOR[q] {
                        keep(&mut local.single[FLOORQ + q - 1], -di, at);
                    }
                    let entry = local
                        .cl
                        .entry(key as u32)
                        .or_insert((d as u8, at, d as u8, at, 0));
                    if (d as u8, at) < (entry.0, entry.1) {
                        (entry.0, entry.1) = (d as u8, at);
                    }
                    if (d as u8) > entry.2 || (d as u8 == entry.2 && at < entry.3) {
                        (entry.2, entry.3) = (d as u8, at);
                    }
                    if !seen {
                        entry.4 += 12 * w;
                        seen = true;
                    }
                }
            }
        },
    );
    let mut per = vec![NONE; nsub * PER];
    let mut cc = vec![NONE; 64 * MAXD];
    let mut cc_hist = vec![0u64; 64 * MAXD];
    let mut single = vec![NONE; NSINGLE];
    let mut cl: HashMap<u32, (u8, (usize, usize, usize), u8, (usize, usize, usize), u64)> =
        HashMap::new();
    for local in parts {
        for (t, x) in per
            .iter_mut()
            .zip(&local.per)
            .chain(single.iter_mut().zip(&local.single))
        {
            if x.score != i64::MIN {
                keep(t, x.score, x.at);
            }
        }
        for (t, x) in cc.iter_mut().zip(&local.cc) {
            if x.score != i64::MIN {
                keep(t, x.score, x.at);
            }
        }
        for (t, x) in cc_hist.iter_mut().zip(&local.cc_hist) {
            *t += *x;
        }
        for (key, v) in local.cl {
            let entry = cl.entry(key).or_insert(v);
            if (v.0, v.1) < (entry.0, entry.1) {
                (entry.0, entry.1) = (v.0, v.1);
            }
            if v.2 > entry.2 || (v.2 == entry.2 && v.3 < entry.3) {
                (entry.2, entry.3) = (v.2, v.3);
            }
        }
    }
    // class sizes were only summed per thread; recount is not needed for the choice below

    // ---- printing
    let reduce = |g: &St| -> (usize, usize, usize) {
        let c = rank_perm(&g.c);
        let sym = classes.csymto[c] as usize;
        (
            classes.cclass[c] as usize,
            core.esym[sym][rank_perm(&g.e)] as usize,
            core.ssym[sym][rank_perm(&g.s)] as usize,
        )
    };
    let depth = |g: &St| -> usize {
        let (k, e, s) = reduce(g);
        exact_depth(&depth_files, k * ROW + e * 12 + slice.to12[s] as usize).unwrap_or(99)
    };
    let seq = |moves: &[usize]| {
        moves
            .iter()
            .map(|&m| MOVE_NAME[m])
            .collect::<Vec<_>>()
            .join(" ")
    };
    let finish = |g: &St| -> Vec<usize> {
        let mut moves = Vec::new();
        let mut x = *g;
        while depth(&x) != 0 {
            let dx = depth(&x);
            let m = (0..NMOVES)
                .find(|&m| depth(&x.apply_move(m)) + 1 == dx)
                .unwrap();
            moves.push(m);
            x = x.apply_move(m);
        }
        moves
    };
    let state = |at: (usize, usize, usize)| -> St {
        let (k, e, s12) = at;
        let c = data.crep[k];
        let par = (core.cpar[c] ^ core.epar[e]) as usize;
        St::unrank(c, e, slice.from12[par][s12] as usize)
    };
    let htr_path = |mut a: usize, mut b: usize| {
        let mut moves = Vec::new();
        while cls.htr_dist[a][b] != 0 {
            let m = (0..NMOVES)
                .find(|&m| {
                    cls.htr_dist[cls.ccos_mv[a][m]][cls.epat_mv[b][m]] + 1 == cls.htr_dist[a][b]
                })
                .unwrap();
            moves.push(m);
            (a, b) = (cls.ccos_mv[a][m], cls.epat_mv[b][m]);
        }
        moves
    };
    // fewest half turns, then a quarter turn that lowers the quarter-turn count (breadth-first with parents)
    let setup_path = |a0: usize, b0: usize| -> Vec<usize> {
        let q = cls.qt_full[a0][b0];
        let start = a0 * NEPAT + b0;
        let mut parent: HashMap<usize, (usize, usize)> = HashMap::new();
        let mut queue = vec![start];
        let mut head = 0;
        loop {
            let y = queue[head];
            head += 1;
            let (a, b) = (y / NEPAT, y % NEPAT);
            if let Some(m) = (0..NMOVES).find(|&m| {
                MOVE_IS_QT[m] && cls.qt_full[cls.ccos_mv[a][m]][cls.epat_mv[b][m]] + 1 == q
            }) {
                let mut moves = vec![m];
                let mut z = y;
                while z != start {
                    let (p, pm) = parent[&z];
                    moves.push(pm);
                    z = p;
                }
                moves.reverse();
                return moves;
            }
            for &m in &HALF_MOVES {
                let z = cls.ccos_mv[a][m] * NEPAT + cls.epat_mv[b][m];
                if z != start && !parent.contains_key(&z) {
                    parent.insert(z, (y, m));
                    queue.push(z);
                }
            }
        }
    };
    let mut out = io::stdout().lock();
    let show = |out: &mut io::StdoutLock,
                label: &str,
                at: (usize, usize, usize)|
     -> io::Result<()> {
        let g = state(at);
        let gi = g.inv();
        let (c, e) = (rank_perm(&g.c), rank_perm(&g.e));
        let (ci, ei) = (rank_perm(&gi.c), rank_perm(&gi.e));
        let (a, b, ai, bi) = (
            cls.ccos[c] as usize,
            cls.epat[e] as usize,
            cls.ccos[ci] as usize,
            cls.epat[ei] as usize,
        );
        let fin = finish(&g);
        let scr: Vec<usize> = fin.iter().rev().map(|&m| MOVE_INV[m]).collect();
        let (hn, hi) = (cls.htr_dist[a][b] as usize, cls.htr_dist[ai][bi] as usize);
        let (sn, si) = (
            setup[a * NEPAT + b] as usize,
            setup[ai * NEPAT + bi] as usize,
        );
        let (k, e2, _) = reduce(&g);
        writeln!(out, "{} :: {}", label, seq(&scr))?;
        writeln!(
            out,
            "    subset {} | optimal {} ({}) | leave slice {} | HTR {} / {} | L {} | qt {} | setup {} / {} | setup+HTR bound {}",
            cls.sub48_name[cls.sub48[a][b] as usize],
            fin.len(),
            seq(&fin),
            lsd[k * NE + e2],
            hn,
            hi,
            clen[c],
            cls.qt_full[a][b],
            sn,
            si,
            if cls.qt_full[a][b] == 0 { 0 } else { (hn + si).max(hi + sn) }
        )?;
        writeln!(
            out,
            "    HTR normal: {} | HTR inverse: ({})",
            seq(&htr_path(a, b)),
            seq(&htr_path(ai, bi))
        )?;
        if cls.qt_full[a][b] != 0 {
            writeln!(
                out,
                "    shortest way to a qt that lowers the count, normal: {} | inverse: ({})",
                seq(&setup_path(a, b)),
                seq(&setup_path(ai, bi))
            )?;
        }
        Ok(())
    };
    for sub in 0..nsub {
        let name = &cls.sub48_name[sub];
        for (j, what) in [
            "longest",
            "shortest",
            "optimal equal to the longer HTR",
            "optimal below the setup+HTR bound",
        ]
        .iter()
        .enumerate()
        {
            let x = per[sub * PER + j];
            if x.score != i64::MIN {
                show(&mut out, &format!("{} {}", name, what), x.at)?;
            } else {
                writeln!(out, "{} {} :: none", name, what)?;
            }
        }
    }
    let labels = [
        "13 to HTR on normal",
        "13 to HTR on both sides",
        "leave slice 18",
        "4a1 4e whose shortest HTR needs three quarter turns on both sides",
        "4c3 4e with 9+ to HTR on both sides, shortest finish",
        "2c5 stacked on both sides, shortest finish",
        "2c4 stacked on both sides, shortest finish",
        "1qt corners with the shortest possible HTR on both sides",
        "2qt corners with the shortest possible HTR on both sides",
        "3qt corners with the shortest possible HTR on both sides",
        "4qt corners with the shortest possible HTR on both sides",
        "5qt corners with the shortest possible HTR on both sides",
        "slice costs one move, shortest finish",
        "slice costs two moves, shortest finish",
        "slice costs the most",
    ];
    for (j, label) in labels.iter().enumerate() {
        if single[j].score != i64::MIN {
            show(&mut out, label, single[j].at)?;
        } else {
            writeln!(out, "{} :: none", label)?;
        }
    }
    // a typical state of every corner case: one whose optimal is the median for that case
    for case in 0..64 {
        let hist = &cc_hist[case * MAXD..(case + 1) * MAXD];
        let total: u64 = hist.iter().sum();
        if total == 0 {
            continue;
        }
        let mut acc = 0;
        let median = (0..MAXD)
            .find(|&d| {
                acc += hist[d];
                acc * 2 >= total
            })
            .unwrap();
        show(
            &mut out,
            &format!("corner case {} typical", case),
            cc[case * MAXD + median].at,
        )?;
    }
    // same subset, same corner case on both sides, same HTR on both sides, optimal furthest apart
    let mut best: Vec<(u32, u8, u8)> = cl.iter().map(|(&key, v)| (key, v.0, v.2)).collect();
    best.sort_by_key(|&(key, lo, hi)| (std::cmp::Reverse(hi - lo), key));
    for &(key, lo, hi) in best
        .iter()
        .filter(|x| ((x.0 >> 20) as usize) < nsub)
        .take(1)
        .chain(
            best.iter()
                .filter(|x| cls.sub48_name[(x.0 >> 20) as usize] == "2c4 4e")
                .take(1),
        )
    {
        let v = cl[&key];
        writeln!(
            out,
            "same corner cases and HTR lengths, optimal {} against {}:",
            lo, hi
        )?;
        show(&mut out, "  the short one", v.1)?;
        show(&mut out, "  the long one", v.3)?;
    }

    // ---- the 216 NISS@1qt cases: classes whose best DR-move finish beats their best half-turn finish
    let e630 = E630::new(&core, &cls);
    let qf = Quot::new(&core, &cls, &e630, true);
    let class_of = |g: &St| -> usize {
        let (c, e) = (rank_perm(&g.c), rank_perm(&g.e));
        Quot::idx(
            qf.corners.ccls[c] as usize,
            e630.cls[e] as usize,
            (core.cpar[c] ^ core.epar[e]) as usize,
        )
    };
    let mut ht: HashMap<(usize, usize, usize), u8> = HashMap::new();
    let mut queue = vec![St::ID];
    ht.insert((0, 0, 0), 0);
    let mut head = 0;
    while head < queue.len() {
        let x = queue[head];
        head += 1;
        let dx = ht[&(rank_perm(&x.c), rank_perm(&x.e), rank_perm(&x.s))];
        for &m in &HALF_MOVES {
            let y = x.apply_move(m);
            let key = (rank_perm(&y.c), rank_perm(&y.e), rank_perm(&y.s));
            if !ht.contains_key(&key) {
                ht.insert(key, dx + 1);
                queue.push(y);
            }
        }
    }
    // per class: (best half-turn length, best DR length, a state with the best DR length)
    let mut by_class: HashMap<usize, (u8, usize, St)> = HashMap::new();
    for x in &queue {
        let dht = ht[&(rank_perm(&x.c), rank_perm(&x.e), rank_perm(&x.s))];
        let ddr = depth(x);
        let entry = by_class.entry(class_of(x)).or_insert((dht, ddr, *x));
        entry.0 = entry.0.min(dht);
        if ddr < entry.1 {
            (entry.1, entry.2) = (ddr, *x);
        }
    }
    writeln!(
        out,
        "HTR states {} in {} classes",
        queue.len(),
        by_class.len()
    )?;
    let text = fs::read_to_string(listing)?;
    for line in text.lines() {
        let Some((label, scramble)) = line.split_once("Example scramble:") else {
            continue;
        };
        let label = label.split("E-parity").next().unwrap().trim();
        let Some(moves) = parse_moves(scramble.trim().as_bytes(), 60) else {
            continue;
        };
        let g = moves.iter().fold(St::ID, |g, &m| g.apply_move(m));
        if let Some(&(dht, ddr, x)) = by_class.get(&class_of(&g)) {
            if (ddr as u8) < dht {
                let fin = finish(&x);
                let scr: Vec<usize> = fin.iter().rev().map(|&m| MOVE_INV[m]).collect();
                writeln!(
                    out,
                    "216 case {} :: half turns {} (listing: {}), DR moves {} :: state {} :: finish {}",
                    label, dht, scramble.trim(), ddr, seq(&scr), seq(&fin)
                )?;
            }
        }
    }
    Ok(0)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn solved_cube_has_all_pairs() {
        let id = [0u8, 1, 2, 3, 4, 5, 6, 7];
        assert_eq!(pair_counts(&id, &id), [16, 0, 0, 0]);
        assert_eq!(slice_pairs(&id, &[0, 1, 2, 3]), 8);
        assert_eq!(bad_corner_mask(&id), 0);
    }

    #[test]
    fn a_quarter_turn_keeps_the_pairs_of_its_layer() {
        // U moves the four U-layer pairs as blocks: all 16 layer pairs stay, the 4 slice blocks of U break
        let g = crate::core::St::ID.apply_move(0);
        assert_eq!(pair_counts(&g.c, &g.e), [16, 0, 0, 0]);
        assert_eq!(slice_pairs(&g.c, &g.s), 4);
        assert_eq!(bad_corner_mask(&g.c), 0b0000_1111);
    }

    #[test]
    fn rodneys_bar_example() {
        // B2 L2 B2 R2 "sets up a top/side semi-pair on each side of the UF edge" (Rodney, #fmc-theory):
        // with only the two corners next to UF looked at, one side semi-pair and one top semi-pair
        let g = [9usize, 7, 9, 6]
            .iter()
            .fold(crate::core::St::ID, |g, &m| g.apply_move(m));
        let mut kinds = Vec::new();
        for &(p, q) in ADJ.iter().filter(|&&(_, q)| q == 0) {
            let (cpiece, epiece) = (g.c[p] as usize, g.e[q] as usize);
            let good = TETRAD[cpiece] == TETRAD[p];
            let axis = (EDGE_FACE[q] & 1) as usize ^ (!good) as usize;
            let (ccol, ecol) = (CORNER_COL[cpiece][axis], EDGE_FACE[epiece]);
            kinds.push((ccol == ecol, ccol == ecol ^ 2, (cpiece < 4) == (epiece < 4)));
        }
        kinds.sort();
        // (side same, side opposite, top same)
        assert_eq!(kinds, vec![(false, true, true), (true, false, false)]);
    }

    #[test]
    fn setup_is_at_least_htr_minus_one_at_one_quarter_turn() {
        let core = Core::new();
        let cls = Classes::new(&core);
        let s = setup_lengths(&cls);
        for x in 0..NCCOS * NEPAT {
            let (a, b) = (x / NEPAT, x % NEPAT);
            if cls.qt_full[a][b] == 1 {
                assert!(s[x] + 1 >= cls.htr_dist[a][b], "coset {}", x);
            }
        }
    }

    #[test]
    fn parity_lengths_bracket_the_corner_length() {
        let core = Core::new();
        let (l, lp) = (
            corner_only_lengths(&core),
            corner_lengths_by_side_parity(&core),
        );
        for c in 0..NC {
            assert_eq!(l[c], lp[c * 2].min(lp[c * 2 + 1]));
        }
    }
}
