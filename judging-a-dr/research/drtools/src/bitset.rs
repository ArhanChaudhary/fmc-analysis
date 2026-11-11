//! A fixed-size bitset that several threads may set bits in at the same time.
//!
//! This is the Rust counterpart of the C code's `uint64_t` arrays updated with `__atomic_fetch_or`.
//! Every word is an `AtomicU64`, so no `unsafe` is needed.  All accesses use relaxed ordering: the
//! BFS only ever *adds* bits during a parallel phase, and a bit that another thread sets concurrently
//! may be seen or missed without changing the result (see `bfs.rs`).

use std::fs::File;
use std::io::{self, Write};
use std::path::Path;
use std::sync::atomic::{AtomicU64, Ordering::Relaxed};

pub struct AtomicBitset {
    words: Vec<AtomicU64>,
}

/// A shared view of the bits of an [`AtomicBitset`]: the type through which bits are read and set.
///
/// It is a plain (pointer, length) pair and cheap to copy.  A hot loop takes the view into a local
/// variable once; the compiler can then keep the address in a register instead of fetching it from the
/// bitset again after every atomic update.
#[derive(Clone, Copy)]
pub struct Bits<'a> {
    words: &'a [AtomicU64],
}

impl Bits<'_> {
    #[inline]
    pub fn get(self, i: usize) -> bool {
        self.words[i >> 6].load(Relaxed) >> (i & 63) & 1 != 0
    }

    /// Set bit `i` (atomic "fetch or", safe to call from many threads).
    #[inline]
    pub fn set(self, i: usize) {
        self.words[i >> 6].fetch_or(1 << (i & 63), Relaxed);
    }

    /// The 12 bits `i .. i + 12` as a number (bit `i` is the lowest).
    #[inline]
    pub fn get12(self, i: usize) -> u64 {
        let mut w = self.words[i >> 6].load(Relaxed) >> (i & 63);
        if (i & 63) > 52 {
            // the 12 bits straddle two words
            w |= self.words[(i >> 6) + 1].load(Relaxed) << (64 - (i & 63));
        }
        w & 0xFFF
    }
}

impl AtomicBitset {
    /// A bitset of `nbits` zero bits (rounded up to whole 64-bit words).
    pub fn new(nbits: usize) -> AtomicBitset {
        AtomicBitset {
            words: (0..nbits.div_ceil(64)).map(|_| AtomicU64::new(0)).collect(),
        }
    }

    /// The view for reading and setting bits.
    pub fn bits(&self) -> Bits<'_> {
        Bits { words: &self.words }
    }

    /// Number of set bits among the whole words `first_word .. first_word + nwords`.
    pub fn count_ones(&self, first_word: usize, nwords: usize) -> u64 {
        self.words[first_word..first_word + nwords]
            .iter()
            .map(|w| w.load(Relaxed).count_ones() as u64)
            .sum()
    }

    /// Reset every bit.
    pub fn clear(&mut self) {
        for w in &mut self.words {
            *w.get_mut() = 0;
        }
    }

    /// Write the words to `path` in little-endian byte order (what the C code's `fwrite` of the word array
    /// produces on x86): bit `i` of the bitset is bit `i % 8` of byte `i / 8` of the file.
    pub fn write_to(&self, path: &Path) -> io::Result<()> {
        let mut file = File::create(path)?;
        let mut bytes = Vec::with_capacity(8 << 16);
        for chunk in self.words.chunks(1 << 16) {
            bytes.clear();
            for w in chunk {
                bytes.extend_from_slice(&w.load(Relaxed).to_le_bytes());
            }
            file.write_all(&bytes)?;
        }
        Ok(())
    }
}
