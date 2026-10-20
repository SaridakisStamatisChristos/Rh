#!/usr/bin/env python3
"""Phase XXIX: two-prime interference and exact sign certificates.

Uses only Python standard library. Arithmetic certificates at alpha=3 include
an explicit infinite-tail bound; finite alpha<=2 tests are only algebraic.
No new zero-free region or RH proof is claimed.
"""
from fractions import Fraction
from math import isqrt

K = 4096
SCALE = 10**15
PAIRS = ((2, 3), (2, 5), (2, 7), (3, 5), (3, 7), (5, 7))


def trial_mu(n):
    v, sign = n, 1
    for p in range(2, isqrt(v) + 1):
        if v % p:
            continue
        v //= p
        sign = -sign
        if v % p == 0:
            return 0
        while v % p == 0:
            v //= p
    return -sign if v > 1 else sign


def sieve_mu(n):
    a = [1] * (n + 1)
    a[0] = 0
    composite = bytearray(n + 1)
    for p in range(2, n + 1):
        if composite[p]:
            continue
        for j in range(p, n + 1, p):
            a[j] = -a[j]
            if j > p:
                composite[j] = 1
        for j in range(p * p, n + 1, p * p):
            a[j] = 0
    return a


def prefix(mu, primes):
    n = len(mu) - 1
    f = [0] * (n + 1)
    v = 0
    for k in range(1, n + 1):
        if all(k % p for p in primes):
            v += mu[k]
        f[k] = v
    return f


def inner(f, d, e, x, alpha):
    """Exact weighted inner product, integrated from 1 to x, for integer alpha."""
    return sum((Fraction(f[k//d] * f[k//e], k**alpha)
                - Fraction(f[k//d] * f[k//e], (k+1)**alpha)
                for k in range(1, x)), Fraction(0))


def energy(f, x, alpha):
    return inner(f, 1, 1, x, alpha)


def signed_interval(terms, scale=SCALE):
    """Rigorous rational enclosure of a sum of (integer numerator, denominator)."""
    low = high = 0
    for numerator, denominator in terms:
        scaled = numerator * scale
        low += scaled // denominator
        high += -(-scaled // denominator)
    return Fraction(low, scale), Fraction(high, scale)


def gamma_partial_interval(f, p, q, x=K):
    pq = p*q
    def terms():
        for k in range(1, x):
            numerator = ((k+1)**3-k**3) * (
                f[k] * f[k//pq] + f[k//p] * f[k//q])
            yield numerator, k**3 * (k+1)**3
    return signed_interval(terms())


def delta_partial_interval(f, M, p, q, x=K):
    pq3 = p**3*q**3
    factor = (p**3+1) * (q**3+1)
    def terms():
        for k in range(1, x):
            numerator = ((k+1)**3-k**3)*(pq3 * M[k]**2-factor*f[k]**2)
            yield numerator, pq3*k**3*(k+1)**3
    return signed_interval(terms())


def cross_prime_checks(mu):
    M=prefix(mu,())
    # Independent Möbius generation for every coefficient used in certificates.
    for n in range(1,K+1):
        assert mu[n] == trial_mu(n), f'mu mismatch n={n}'
    print(f'INDEPENDENT MOBIUS CHECK: {K}/{K} PASS')

    # Every identity is checked with exact fractions and the correct
    # boundary correction at a finite cutoff.
    cases=0
    for p,q in ((2,3),(2,7),(3,5)):
        f=prefix(mu,(p,q))
        fp=[f[k]-f[k//p] for k in range(K+1)]
        fq=[f[k]-f[k//q] for k in range(K+1)]
        for x in (32,64,96):
            for alpha in (1,2,3):
                assert all(M[k] == f[k]-f[k//p]-f[k//q]+f[k//(p*q)]
                           for k in range(1,x+1))
                gamma=inner(f,1,p*q,x,alpha)+inner(f,p,q,x,alpha)
                # Finite cutoff versions require scale-corrected inner products.
                lhs=inner(fp,1,q,x,alpha)
                # The finite-cutoff correction is the shifted-pair term
                # inner(f,p,p*q,x), not a naive same-cutoff scalar factor.
                assert lhs == (inner(f,1,q,x,alpha)-gamma+
                               inner(f,p,p*q,x,alpha)), (p,q,x,alpha)
                # The analogous p-side identity.
                assert inner(fq,1,p,x,alpha) == (inner(f,1,p,x,alpha)-gamma+
                                                inner(f,q,p*q,x,alpha))
                # Four-term expansion from the exact integrated Gram matrix.
                A=[(1,1),(p,-1),(q,-1),(p*q,1)]
                reconstructed=sum((sa*sb*inner(f,da,db,x,alpha)
                    for da,sa in A for db,sb in A),Fraction(0))
                assert reconstructed == energy(M,x,alpha)
                cases+=1
    print(f'EXACT FINITE TWO-PRIME/DIAMOND CHECKS: {cases}/{cases} PASS')

    for p,q in PAIRS:
        f=prefix(mu,(p,q))
        glow,ghigh=gamma_partial_interval(f,p,q)
        # Each of the two products satisfies |S_d f(x)S_e f(x)|<= x^2/(de).
        # Therefore at alpha=3 the infinite mixed-covariance tail <= 6/(pq*K).
        gtail=Fraction(6,p*q*K)
        glo,ghi=glow-gtail,ghigh+gtail
        dlow,dhigh=delta_partial_interval(f,M,p,q)
        # |M(x)|<=x, |f(x)|<=x, so the aggregate tail bound is
        # 3/K * (1 + (1+p^-3)(1+q^-3)).
        A=Fraction((p**3+1)*(q**3+1),p**3*q**3)
        dtail=Fraction(3,K)*(1+A)
        dlo,dhi=dlow-dtail,dhigh+dtail
        print(f'PAIR p={p} q={q}  GAMMA_3 full in [{float(glo):+.10f}, {float(ghi):+.10f}]'
              f'  DELTA_3 full in [{float(dlo):+.10f}, {float(dhi):+.10f}]')
        if (p,q)==(2,3):
            assert glo > Fraction(3,100), (glo,ghi)
            assert dhi < -Fraction(6,25), (dlo,dhi)
        if (p,q)==(2,7):
            assert ghi < -Fraction(1,1000), (glo,ghi)
        if (p,q)==(3,5):
            assert dlo > Fraction(1,200), (dlo,dhi)
    print('FULL INFINITE INEQUALITY SIGNS: 4/4 PASS')


def main():
    cross_prime_checks(sieve_mu(K))
    print('ALL PHASE XXIX CHECKS PASS — no RH proof or new zero-free region')

if __name__=='__main__': main()
