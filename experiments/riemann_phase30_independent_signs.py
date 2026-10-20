#!/usr/bin/env python3
"""Independent Phase XXX supplement: six exact infinite-sign certificates.
Uses only Python stdlib; all computations rational plus a proved 3/K tail.
"""
from fractions import Fraction
from math import isqrt, prod

K = 16384
SCALE = 10**16
CASES = (
    ((2, 3, 5), '<', Fraction(-1, 4)),
    ((5, 11, 17), '>', Fraction(1, 100)),
    ((2, 3, 5, 7), '<', Fraction(-1, 4)),
    ((5, 11, 13, 23), '>', Fraction(1, 100)),
    ((2, 3, 5, 7, 31), '<', Fraction(-1, 4)),
    ((5, 11, 13, 19, 29), '>', Fraction(1, 100)),
)

def sieve_mu(N):
    mu = [1] * (N + 1)
    mu[0] = 0
    crossed = bytearray(N + 1)
    for p in range(2, N + 1):
        if crossed[p]:
            continue
        for n in range(p, N + 1, p):
            mu[n] = -mu[n]
            if n > p:
                crossed[n] = 1
        for n in range(p * p, N + 1, p * p):
            mu[n] = 0
    return mu

def trial_mu(n):
    sign = 1
    for p in range(2, isqrt(n) + 1):
        if n % p:
            continue
        n //= p
        sign = -sign
        if n % p == 0:
            return 0
    if n > 1:
        sign = -sign
    return sign

def prefix(mu, P):
    f = [0] * len(mu)
    for n in range(1, len(mu)):
        f[n] = f[n - 1] + (mu[n] if all(n % p for p in P) else 0)
    return f

def finite_energy_bounds(f):
    lo = hi = 0
    for k in range(1, K):
        a = ((k + 1) ** 3 - k ** 3) * f[k] ** 2 * SCALE
        b = k ** 3 * (k + 1) ** 3
        lo += a // b
        hi += -(-a // b)
    return Fraction(lo, SCALE), Fraction(hi, SCALE)

def main():
    mu = sieve_mu(K)
    assert all(mu[n] == trial_mu(n) for n in range(1, K + 1))
    print(f'Independent Möbius coefficients: {K}/{K} passed')
    mlow, mhigh = finite_energy_bounds(prefix(mu, ()))
    for P, sign, bound in CASES:
        fl, fh = finite_energy_bounds(prefix(mu, P))
        A = prod(Fraction(p ** 3 + 1, p ** 3) for p in P)
        # |M(x)|,|F_P(x)| <= x, giving tails <= 3/K each.
        tail = Fraction(3, K) * (1 + A)
        low, high = mlow - A * fh - tail, mhigh - A * fl + tail
        assert (high < bound if sign == '<' else low > bound), (P, low, high)
        print(P, f'[{float(low):+.12f}, {float(high):+.12f}]',
              sign, bound, 'CERTIFIED')
    print('All six infinite-interference sign certificates passed; no RH claim')

if __name__ == '__main__':
    main()
