//! Small text helpers that reproduce the C library calls the original tools used on their input
//! (`fgets`, `isspace`, `strtol`, `strstr`), so that odd input is treated exactly the same way.

use std::io::{self, BufRead};

/// C `isspace` in the "C" locale.
pub fn is_c_space(b: u8) -> bool {
    matches!(b, b' ' | b'\t' | b'\n' | 0x0B | 0x0C | b'\r')
}

/// Read the next line like C `fgets(buf, limit, f)` followed by C string handling:
/// at most `limit - 1` bytes, stopping after a newline (a longer line comes back in several pieces),
/// and cut at the first NUL byte.  Returns `false` at end of input.
pub fn read_line_like_fgets(
    input: &mut impl BufRead,
    limit: usize,
    line: &mut Vec<u8>,
) -> io::Result<bool> {
    line.clear();
    while line.len() < limit - 1 {
        let buf = input.fill_buf()?;
        if buf.is_empty() {
            break;
        }
        let window = &buf[..buf.len().min(limit - 1 - line.len())];
        let take = window
            .iter()
            .position(|&b| b == b'\n')
            .map_or(window.len(), |i| i + 1);
        line.extend_from_slice(&window[..take]);
        input.consume(take);
        if line.last() == Some(&b'\n') {
            break;
        }
    }
    if line.is_empty() {
        return Ok(false);
    }
    if let Some(nul) = line.iter().position(|&b| b == 0) {
        line.truncate(nul);
    }
    Ok(true)
}

/// C `strtol(txt, &end, 10)`: skips white space, takes an optional sign and decimal digits.
/// Returns the value (clamped to the `long` range like `strtol`) and the number of bytes consumed,
/// or `None` if there is no number.
pub fn strtol(txt: &[u8]) -> Option<(i64, usize)> {
    let mut i = txt
        .iter()
        .position(|&b| !is_c_space(b))
        .unwrap_or(txt.len());
    let negative = txt.get(i) == Some(&b'-');
    if negative || txt.get(i) == Some(&b'+') {
        i += 1;
    }
    let first_digit = i;
    let mut value: Option<i64> = Some(0); // None once out of range
    while let Some(digit) = txt.get(i).filter(|b| b.is_ascii_digit()) {
        let d = (digit - b'0') as i64;
        value = value.and_then(|v| v.checked_mul(10)).and_then(|v| {
            if negative {
                v.checked_sub(d)
            } else {
                v.checked_add(d)
            }
        });
        i += 1;
    }
    if i == first_digit {
        return None;
    }
    Some((
        value.unwrap_or(if negative { i64::MIN } else { i64::MAX }),
        i,
    ))
}

/// C `strstr`: position of the first occurrence of `needle` in `haystack`.
pub fn find(haystack: &[u8], needle: &[u8]) -> Option<usize> {
    haystack.windows(needle.len()).position(|w| w == needle)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn strtol_like_c() {
        assert_eq!(strtol(b"  42 7"), Some((42, 4)));
        assert_eq!(strtol(b"-3x"), Some((-3, 2)));
        assert_eq!(strtol(b" x"), None);
        assert_eq!(strtol(b"99999999999999999999"), Some((i64::MAX, 20)));
        assert_eq!(strtol(b"-9223372036854775808"), Some((i64::MIN, 20)));
    }

    #[test]
    fn fgets_splits_long_lines() {
        let mut input = io::Cursor::new(b"abcdef\nxy\n\nlast".to_vec());
        let mut line = Vec::new();
        let mut pieces = Vec::new();
        while read_line_like_fgets(&mut input, 5, &mut line).unwrap() {
            pieces.push(line.clone());
        }
        assert_eq!(pieces, [&b"abcd"[..], b"ef\n", b"xy\n", b"\n", b"last"]);
    }
}
