//! Deterministic "random" numbers from hashes, so that the same object (an EO, an RZP state, an HTR, a step)
//! gets the same draw under every policy: paired comparisons on common random numbers.

#[inline]
pub fn mix(mut z: u64) -> u64 {
    z = z.wrapping_add(0x9E3779B97F4A7C15);
    z = (z ^ (z >> 30)).wrapping_mul(0xBF58476D1CE4E5B9);
    z = (z ^ (z >> 27)).wrapping_mul(0x94D049BB133111EB);
    z ^ (z >> 31)
}
#[inline]
pub fn h2(a: u64, b: u64) -> u64 {
    mix(a ^ mix(b).rotate_left(23))
}
pub fn hseq(seed: u64, xs: &[u8]) -> u64 {
    let mut h = mix(seed ^ 0x5851F42D4C957F2D);
    for &x in xs {
        h = h2(h, x as u64 + 1);
    }
    h2(h, xs.len() as u64)
}
/// Uniform in [0, 1).
#[inline]
pub fn unif(h: u64) -> f64 {
    (h >> 11) as f64 / (1u64 << 53) as f64
}
/// Standard normal (Box-Muller on two uniforms derived from h).
pub fn normal(h: u64) -> f64 {
    let u1 = unif(mix(h ^ 0xA5A5A5A5)).max(1e-300);
    let u2 = unif(mix(h ^ 0x5A5A5A5A5A));
    (-2.0 * u1.ln()).sqrt() * (2.0 * std::f64::consts::PI * u2).cos()
}
