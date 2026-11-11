#!/usr/bin/env python3
"""Compare the Lean-proven table of optimal lengths with the depth files of the Rust BFS, entry by entry.

  lean_exact_table.u8   one byte per reduced state, index (class * 40320 + edge rank) * 12 + slice index,
                        written by an #eval of `DRBound.Exact.mkTable 18`
  drbfs/depth_NN.bits   one bit per reduced state and depth, same index, bit i = bit i%8 of byte i/8

Reads both in chunks (about 300 MB of memory)."""
import sys
import numpy as np

DATA = '/data/fmc/research/data'
N = 2768 * 40320 * 12
T = np.memmap(f'{DATA}/lean_exact_table.u8', dtype=np.uint8, mode='r')
assert T.size == N, (T.size, N)
files = [np.memmap(f'{DATA}/drbfs/depth_{d:02}.bits', dtype=np.uint8, mode='r') for d in range(19)]
assert all(f.size * 8 == N for f in files)

CH = 1 << 22                       # bytes of each bit file per chunk = 33.5 million entries
mismatch = uncovered = multiple = 0
hist = np.zeros(256, dtype=np.int64)
for off in range(0, N // 8, CH):
    n = min(CH, N // 8 - off)
    R = np.full(n * 8, 255, dtype=np.uint8)
    cnt = np.zeros(n * 8, dtype=np.uint8)
    for d, f in enumerate(files):
        b = np.unpackbits(np.asarray(f[off:off + n]), bitorder='little')
        R[b == 1] = d
        cnt += b
    t = np.asarray(T[off * 8:(off + n) * 8])
    mismatch += int((R != t).sum())
    uncovered += int((cnt == 0).sum())
    multiple += int((cnt > 1).sum())
    hist += np.bincount(t, minlength=256)
print(f'entries {N}')
print(f'Rust depth files: entries in no file {uncovered}, in more than one {multiple}')
print(f'Lean table vs Rust depth: {mismatch} mismatches')
print('entries by value (unweighted):', {d: int(c) for d, c in enumerate(hist) if c})
sys.exit(0 if mismatch == 0 and uncovered == 0 and multiple == 0 else 1)
