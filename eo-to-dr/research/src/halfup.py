"""Rounding for every number printed on a page: an exact half goes up (away from zero).

Formatting a float rounds its binary digits, so an exact half goes either way (8.055 -> 8.05, 8.685 -> 8.69,
6.25 -> 6.2, 12.5 -> 12).  hu() rounds the decimal a reader would compute instead.  Same rule and code as
judging-a-dr/research/src/pv.py (kept here so that this study does not import the other one)."""
import decimal, fractions, numbers

def exact(x):
    """x as a Fraction: a whole number, a Fraction or a Decimal as it is; a float (or a number read from a result
    file) as its shortest repr, which is the decimal a reader would compute (40275 / 5000 is 8.055)."""
    if isinstance(x, numbers.Integral): return fractions.Fraction(int(x))          # int() for numpy's whole numbers
    if isinstance(x, (fractions.Fraction, decimal.Decimal)): return fractions.Fraction(x)
    return fractions.Fraction(repr(float(x)))

def hu(x, digits=0, scale=1):
    """x * scale rounded to `digits` decimals, an exact half going up, as a Decimal that takes the format of the float
    it replaces: f'{hu(x, 2):.2f}', f'{hu(share, 1, 100):.1f}%'.  nan and inf come back as they are."""
    if not isinstance(x, (numbers.Integral, fractions.Fraction, decimal.Decimal)):
        x = float(x)
        if x != x or x in (float('inf'), float('-inf')): return x
    v = exact(x) * scale * 10 ** digits
    n = (2 * abs(v.numerator) + v.denominator) // (2 * v.denominator)
    return decimal.Decimal(n).scaleb(-digits).copy_sign(-1 if v < 0 else 1)
