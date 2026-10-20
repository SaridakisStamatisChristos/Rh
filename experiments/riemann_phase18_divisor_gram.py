#!/usr/bin/env python3
"""Exact divisor-gram identities and reproducible random-sign comparator.

Research only. Does not prove the Riemann hypothesis.
"""
from fractions import Fraction
from math import gcd, log, pi
from random import Random


def mobius_sieve(n):
    mu = [1] * (n + 1)
    mu[0] = 0
    is_composite = [False] * (n + 1)
    for p in range(2, n + 1):
        if is_composite[p]:
            continue
        for k in range(p, n + 1, p):
            mu[k] = -mu[k]
            if k > p:
                is_composite[k] = True
        if p * p <= n:
            for k in range(p * p, n + 1, p * p):
                mu[k] = 0
    return mu


def divisor_transform(a):
    n = len(a) - 1
    z = [0] * (n + 1)
    for d in range(1, n + 1):
        if a[d]:
            for k in range(d, n + 1, d):
                z[k] += a[d]
    return z


def divisor_inverse(z, mu):
    n = len(z) - 1
    a = [0] * (n + 1)
    for d in range(1, n + 1):
        if z[d]:
            for k in range(d, n + 1, d):
                a[k] += z[d] * mu[k // d]
    return a


def gram_energy_direct(a):
    n = len(a) - 1
    result = 0
    for d in range(1, n + 1):
        for e in range(1, n + 1):
            l = d // gcd(d, e) * e
            result += a[d] * a[e] * (n // l)
    return result


def q_energy(a, alpha):
    n = len(a) - 1
    total = 0
    Q = Fraction(0)
    for k in range(1, n):
        total += a[k]
        Q += Fraction(total * total, k ** alpha) - Fraction(total * total, (k + 1) ** alpha)
    total += a[n]
    Q += Fraction(total * total, n ** alpha)
    return Q


def q_in_divisor_coordinates(z, mu, alpha):
    n = len(z) - 1
    M = [0] * (n + 1)
    for k in range(1, n + 1):
        M[k] = M[k-1] + mu[k]
    A = [0] * (n + 1)
    for k in range(1, n + 1):
        A[k] = sum(z[d] * M[k // d] for d in range(1, k + 1))
    Q = Fraction(0)
    for k in range(1, n):
        Q += A[k]*A[k]*(Fraction(1, k ** alpha)-Fraction(1,(k+1) ** alpha))
    Q += Fraction(A[n]*A[n], n**alpha)
    return Q, A


def independent_sign_experiment(n, seed=20261020, replications=200):
    mu = mobius_sieve(n)
    sf = [int(mu[d]!=0) for d in range(n+1)]
    theoretical = sum(sf[d] * (n//d) for d in range(1,n+1))
    random = Random(seed)
    values = []
    for _ in range(replications):
        b = [0] * (n+1)
        b[1] = 1
        for d in range(2,n+1):
            if sf[d]:
                b[d] = random.choice((-1,1))
        z = divisor_transform(b)
        values.append(sum(x*x for x in z[1:]))
    actual = sum(x*x for x in divisor_transform(mu)[1:])
    assert actual == 1
    return theoretical, sum(values)/len(values), min(values), max(values)


def main():
    for N in (16,32,64,128):
        mu = mobius_sieve(N)
        z = divisor_transform(mu)
        assert z[1] == 1 and all(x==0 for x in z[2:])
        assert gram_energy_direct(mu) == sum(x*x for x in z[1:]) == 1
        M = [0] * (N+1)
        for j in range(1,N+1):
            M[j] = M[j-1]+mu[j]
        for k in range(1,N+1):
            assert sum(M[k//d] for d in range(1,k+1)) == 1
            assert M[k] == 1 - sum(M[k//d] for d in range(2,k+1))
        rng = Random(20261020 + N)
        for trial in range(3):
            a = [0] + [rng.randint(-2,2) for _ in range(N)]
            z = divisor_transform(a)
            assert divisor_inverse(z,mu)==a
            assert gram_energy_direct(a)==sum(t*t for t in z[1:])
            for alpha in (1,2,3):
                Q=q_energy(a,alpha)
                Qz, A = q_in_divisor_coordinates(z,mu,alpha)
                assert Q==Qz
        print(f'N={N} divisorGram(mu)=1; exact inverse, recurrence, Q_alpha transfer: PASS')
    for N in (256,1024,4096):
        theory,avg,low,high=independent_sign_experiment(N)
        main_term=6/pi**2*N*log(N)
        print(f'N={N} true_energy=1 null_E_exact={theory} null_mean_200={avg:.1f} range=({low},{high}) main_term={main_term:.1f} relative_exact={theory/main_term:.4f}')
    print('ALL EXACT TESTS PASS (null model trials only illustrate the proven exact mean).')


if __name__ == '__main__':
    main()
