#!/usr/bin/env python3
"""Fully exact integer/rational certification of the Phase XVII model-sequence witness.

The surrogate b_n is not multiplicative and is NOT the arithmetic Mobius function.
The proof of its infinite-family behaviour is in the matching Markdown note.
"""
from fractions import Fraction

R = 10**30
H = R // 20_000
sqrt_R = 10**15
assert sqrt_R**2 == R
assert 2*H < R

# Since ln(10) < 7/3, ln(R) = 30 ln(10) < 70.
# Therefore H = R/20000 < R/(ln R)^2 for R=10^30,
# and x/(ln x)^2 is increasing for all x>=R.
assert 70**2 < 20_000

# For exponent alpha=3/2,  (R+2H)^(5/2) < (2R)^(5/2) < 6 R^(5/2).
# The exact tent-energy bound for the contribution of its nonzero block is
# D >= H^3/(12 R^(5/2)) - H/R^(3/2).
lower_pulse = Fraction(H**3, 12 * R**2 * sqrt_R) - Fraction(H, R * sqrt_R)
# The initial b_1=1,b_2=-1 makes contribution -1/2^(3/2)>-1.
lower_full = lower_pulse - 1
assert lower_full > 9

print("R =", R)
print("H =", H)
print("Proof that log(R)^2 < 20000: log(10) < 7/3 ==> log(R) < 70")
print("Exact rational lower bound on pulse contribution:", lower_pulse)
print("Exact rational lower bound on full C_(3/2):", lower_full)
print("Full correlation >9: PASS")
print("All arithmetic checks used Python big integers and fractions.")
