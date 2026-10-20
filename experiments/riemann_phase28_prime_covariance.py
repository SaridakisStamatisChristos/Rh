#!/usr/bin/env python3
"""Phase XXVIII: exactly certified opposite-sign prime-step covariances.

Uses only the Python standard library. No numerical observation is promoted to
an all-N claim, and no improvement on the Riemann Hypothesis is claimed.

Run: python3 riemann_phase28_prime_covariance.py
"""
from fractions import Fraction
from math import isqrt


def mobius_sieve(n):
    mu = [1] * (n + 1)
    mu[0] = 0
    prime_marked = bytearray(n + 1)
    for p in range(2, n + 1):
        if prime_marked[p]:
            continue
        for j in range(p, n + 1, p):
            mu[j] = -mu[j]
            if j > p:
                prime_marked[j] = 1
        for j in range(p*p, n + 1, p*p):
            mu[j] = 0
    return mu


def reference_mu(n):
    rem, sign = n, 1
    for p in range(2, isqrt(rem) + 1):
        if rem % p:
            continue
        rem //= p
        sign = -sign
        if rem % p == 0:
            return 0
        while rem % p == 0:
            rem //= p
    return -sign if rem > 1 else sign


def excised_prefix(mu, prime, X):
    f = [0] * (X + 1)
    for n in range(1, X + 1):
        f[n] = f[n - 1] + (mu[n] if n % prime else 0)
    return f


def correlation_exact(mu, p, alpha, X):
    # alpha integral on [1,X] of f(x)f(x/p) / x^(alpha+1):
    # f is a step function on [n,n+1).
    f = excised_prefix(mu, p, X)
    return sum((Fraction(1, n**alpha)-Fraction(1, (n+1)**alpha)) *
               f[n]*f[n//p] for n in range(p, X)), f


def energy_exact(f, alpha, X):
    return sum((Fraction(1, n**alpha)-Fraction(1, (n+1)**alpha)) *
               f[n]**2 for n in range(1, X))


def main():
    X = 1024
    mu = mobius_sieve(X)
    for n in range(1, X + 1):
        assert mu[n] == reference_mu(n), ('sieve error', n)
    print('INDEPENDENT MU CROSSCHECK: 1024/1024 PASS')

    # For alpha=3, |f(x)| <= x and |f(x/p)| <= x/p (x>=p), hence
    # |J_{p,3}(infinity)-J_{p,3}(X)| <= 3/(pX).
    witnesses = [(2, 'positive', Fraction(9, 100)),
                 (3, 'negative', Fraction(1, 600)),
                 (5, 'negative', Fraction(1, 250))]
    for p, sign, margin in witnesses:
        j, f = correlation_exact(mu, p, 3, X)
        tail = Fraction(3, p*X)
        if sign == 'positive':
            assert j > margin and margin > tail
            assert j - tail > 0
        else:
            assert j < -margin and margin > tail
            assert j + tail < 0
        assert j == sum((Fraction(1, n**3)-Fraction(1, (n+1)**3))*
                        f[n]*f[n//p] for n in range(1,X))
        print(f'INFINITE J_(p={p},alpha=3): {sign.upper()} PROVED; '
              f'finite={float(j):+.12f} tail <= {float(tail):.12f} '
              f'certified interval [{float(j-tail):+.12f},{float(j+tail):+.12f}]')

    Xs = 32
    M=[0]
    for n in range(1,Xs + 1):
        M.append(M[-1] + mu[n])
    M3=excised_prefix(mu,3,Xs)
    d1=energy_exact(M,1,Xs)-energy_exact(M3,1,Xs)
    d2=energy_exact(M,2,Xs)-energy_exact(M3,2,Xs)
    assert d1 == Fraction(-65627647919,3208967842080)
    assert d2 == Fraction(174590367216324991675973,2059494922300714363745280)
    assert d1 < 0 < d2
    print(f'EXACT EXPONENT SIGN REVERSAL for p=3, X=32: '
          f'Delta_1={d1}; Delta_2={d2}; '
          'continuity forces some alpha_star in (1,2).')

    for p in (2,3,5):
        f=excised_prefix(mu,p,X)
        sf=[f[n//p] for n in range(X+1)]
        g=[f[n]-sf[n] for n in range(X+1)]
        Mfull=[0]
        for n in range(1,X+1):
            Mfull.append(Mfull[-1]+mu[n])
        assert g == Mfull
        for alpha in (1,2,3):
            e0=energy_exact(f,alpha,X)
            es=energy_exact(sf,alpha,X)
            j=sum((Fraction(1,n**alpha)-Fraction(1,(n+1)**alpha))*f[n]*sf[n]
                  for n in range(1,X))
            er=energy_exact(g,alpha,X)
            assert er==e0+es-2*j
        print(f'EXACT PRIME-STEP ENERGY IDENTITY: p={p}, alpha=1,2,3 PASS')

    # Independently obtain the finite correlation from a double sum of
    # prime-free Mobius coefficients, guarding cutoff and divisibility.
    crosschecks=0
    for cutoff in (16,32,64):
        for p in (2,3,5):
            ms=[m for m in range(1,cutoff) if m%p and mu[m]]
            ns=[n for n in range(1,(cutoff-1)//p+1) if n%p and mu[n]]
            for alpha in (1,2,3):
                j,_=correlation_exact(mu,p,alpha,cutoff)
                alt=sum((mu[m]*mu[n]*(Fraction(1,max(m,p*n)**alpha)
                         -Fraction(1,cutoff**alpha))
                         for m in ms for n in ns),Fraction(0))
                assert j==alt,(cutoff,p,alpha,j,alt)
                crosschecks+=1
    print(f'INDEPENDENT DOUBLE-SUM CROSSCHECKS: {crosschecks}/{crosschecks} PASS')
    print('ALL EXACT TESTS PASS. NO RH PROOF OR NEW ZERO-FREE REGION.')


if __name__ == '__main__':
    main()
