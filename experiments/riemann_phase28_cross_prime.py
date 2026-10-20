#!/usr/bin/env python3
"""Phase XXVIII: exact cross-prime energy sign certificate.

Infinite sign statements at alpha=3 use the elementary bound |M_P(x)|<=x.
The alpha=1 examples are finite only. No claim of RH proof or originality.
"""
from fractions import Fraction

SCALE = 10**16
K = 1024


def trial_mu(n):
    v, sign, p = n, 1, 2
    while p*p <= v:
        if v % p == 0:
            v //= p
            sign = -sign
            if v % p == 0:
                return 0
            while v % p == 0:
                v //= p
        p += 1
    if v > 1:
        sign = -sign
    return sign


def sieve_mu(n):
    mu = [1]*(n+1)
    mu[0] = 0
    marked = bytearray(n+1)
    for p in range(2, n+1):
        if marked[p]:
            continue
        for j in range(p, n+1, p):
            mu[j] = -mu[j]
            if j > p:
                marked[j] = 1
        for j in range(p*p, n+1, p*p):
            mu[j] = 0
    return mu


def exclude_prime(n, p, mu):
    b = mu[:n+1].copy()
    for k in range(p, n+1, p):
        b[k] = 0
    f = [0]*(n+1)
    for k in range(1, n+1):
        f[k] = f[k-1] + b[k]
    return b, f


def interval_bounds(f, p, alpha, cutoff):
    lower = upper = 0
    for k in range(1, cutoff):
        val = f[k]*f[k//p]
        left, right = k**alpha, (k+1)**alpha
        num, den = val*(right-left)*SCALE, left*right
        lower += num // den
        upper += (num+den-1) // den
    return Fraction(lower, SCALE), Fraction(upper, SCALE)


def step_exact(f, p, alpha, cutoff):
    return sum((Fraction(f[k]*f[k//p], k**alpha)
                - Fraction(f[k]*f[k//p], (k+1)**alpha)
                for k in range(1, cutoff)), Fraction(0))


def bilinear_exact(b, p, alpha, cutoff):
    result = Fraction(0)
    for m in range(1, cutoff+1):
        if not b[m]:
            continue
        for n in range(1, cutoff//p+1):
            if b[n]:
                result += b[m]*b[n]*(
                    Fraction(1, max(m,p*n)**alpha)
                    - Fraction(1,cutoff**alpha))
    return result


def test_bilinear():
    mu = sieve_mu(128)
    cases = 0
    for N in (16,32,64):
        for p in (2,3,5,7):
            b, f = exclude_prime(N,p,mu)
            for alpha in (1,2,3):
                lhs = step_exact(f,p,alpha,N)
                rhs = bilinear_exact(b,p,alpha,N)
                assert lhs == rhs, (N,p,alpha,lhs,rhs)
                cases += 1
    assert cases == 36
    print('EXACT BILINEAR IDENTITY: 36/36 PASS')


def test_global():
    mu = sieve_mu(K)
    assert all(mu[k] == trial_mu(k) for k in range(1,K+1))
    print('MOBIUS INDEPENDENT TRIAL-DIVISION CHECK: 1024/1024 PASS')
    for p in (2,3,5):
        _, f = exclude_prime(K,p,mu)
        low, high = interval_bounds(f,p,3,K)
        assert low <= step_exact(f,p,3,K) <= high
        # |F_p(x) F_p(x/p)|<=x^2/p => tail <= 3/(p*K)
        tail = Fraction(3,p*K)
        full_low, full_high = low-tail, high+tail
        print(f'p={p} alpha=3 full rational enclosure: '
              f'{full_low} < B_3,p < {full_high}')
        print(f'  display: [{float(full_low):+.12f},{float(full_high):+.12f}]')
        if p == 2:
            assert full_low > Fraction(2,25)
        elif p == 3:
            assert full_high < -Fraction(1,1000)
        else:
            assert full_high < -Fraction(3,1000)
    print('FULL INFINITE alpha=3 OPPOSITE SIGNS: PASS')


def test_finite_critical():
    mu = sieve_mu(512)
    for p in (2,107):
        _, f = exclude_prime(512,p,mu)
        low, high = interval_bounds(f,p,1,512)
        print(f'FINITE X=512 alpha=1 p={p}: '
              f'{float(low):+.12f} to {float(high):+.12f}')
        if p == 2:
            assert low > 1
        else:
            assert high < -Fraction(1,1000)
    print('FINITE alpha=1 CROSS-PRIME SIGNS: PASS')


def main():
    test_bilinear()
    test_global()
    test_finite_critical()
    print('PASS. No improved zero-free region or RH proof established.')


if __name__ == '__main__':
    main()
