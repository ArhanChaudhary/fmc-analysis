//! The one parallel pattern the aggregation passes need: a loop with dynamic scheduling in which every
//! worker thread owns some private state (a histogram, read buffers).
//!
//! OpenMP equivalent in the C sources:
//! `#pragma omp parallel { private state;  #pragma omp for schedule(dynamic, chunk) for (k = 0; k < n; k++) ... }`

use std::sync::atomic::{AtomicUsize, Ordering::Relaxed};

/// Run `body(&mut local, k)` for every `k` in `0..n` on all threads of the rayon pool.
///
/// Each thread creates its own `local` with `init`, then repeatedly claims the next `chunk` indices from
/// a shared counter.  Returns the `local` of every thread (one entry per thread, in thread order).
pub fn for_each_with_local<L, I, B>(n: usize, chunk: usize, init: I, body: B) -> Vec<L>
where
    L: Send,
    I: Fn() -> L + Sync,
    B: Fn(&mut L, usize) + Sync,
{
    let next = AtomicUsize::new(0);
    rayon::broadcast(|_| {
        let mut local = init();
        loop {
            let start = next.fetch_add(chunk, Relaxed);
            if start >= n {
                break;
            }
            for k in start..(start + chunk).min(n) {
                body(&mut local, k);
            }
        }
        local
    })
}

/// Add up the per-thread histograms returned by [`for_each_with_local`].
pub fn sum_histograms(parts: impl Iterator<Item = Vec<u64>>) -> Vec<u64> {
    parts
        .reduce(|mut total, part| {
            for (t, p) in total.iter_mut().zip(&part) {
                if *p != 0 {
                    *t += *p;
                }
            }
            total
        })
        .unwrap_or_default()
}
