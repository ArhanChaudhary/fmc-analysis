//! Deterministic "random" numbers from hashes: the same object (an EO, an RZP state, a route, a step) gets the same
//! draw whatever the plan, so two plans on one scramble differ only by what they do.  The functions come from the
//! `libm` crate so that the native program and the web page give the same attempt to the last bit.

#[inline]
pub fn mix(mut z: u64) -> u64 {
    z = z.wrapping_add(0x9E37_79B9_7F4A_7C15);
    z = (z ^ (z >> 30)).wrapping_mul(0xBF58_476D_1CE4_E5B9);
    z = (z ^ (z >> 27)).wrapping_mul(0x94D0_49BB_1331_11EB);
    z ^ (z >> 31)
}

/// Hash of a pair.
#[inline]
pub fn h2(a: u64, b: u64) -> u64 {
    mix(a ^ mix(b).rotate_left(23))
}

/// Hash of a byte sequence.
pub fn hash_bytes(seed: u64, xs: &[u8]) -> u64 {
    let mut h = mix(seed ^ 0x5851_F42D_4C95_7F2D);
    for &x in xs {
        h = h2(h, x as u64 + 1);
    }
    h2(h, xs.len() as u64)
}

/// Uniform in [0, 1).
#[inline]
pub fn uniform(h: u64) -> f64 {
    (h >> 11) as f64 / (1u64 << 53) as f64
}

/// Standard normal (Box-Muller on two uniforms derived from h).
pub fn normal(h: u64) -> f64 {
    let u1 = uniform(mix(h ^ 0xA5A5_A5A5)).max(1e-300);
    let u2 = uniform(mix(h ^ 0x5A_5A5A_5A5A));
    libm::sqrt(-2.0 * libm::log(u1)) * libm::cos(2.0 * std::f64::consts::PI * u2)
}

/// A log-normal factor with mean 1 and spread `sigma`, from a standard normal z.
#[inline]
pub fn lognormal(sigma: f64, z: f64) -> f64 {
    libm::exp(sigma * z - sigma * sigma / 2.0)
}
