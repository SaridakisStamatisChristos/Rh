#!/usr/bin/env python3
"""Phase XXVII: independently test finite-prime Mobius reconstruction and
weighted Hilbert-energy inequalities. No claim of an RH proof.

Run: python3 experiments/riemann_phase27_prime_dilation.py
Writes two deterministic CSV diagnostics next to the script.
"""
import csv
from fractions import Fraction
from math import prod, isclose, log
from pathlib import Path


def mobius_sieve(n):
    mu = [1] * (n + 1)
    mu[0] = 0
    composite = bytearray(n + 1)
    for p in range(2, n + 1):
        if composite[p]:
            continue
        for j in range(p, n + 1, p):
            mu[j] = -mu[j]
            if j > p:
                composite[j] = 1
        for j in range(p * p, n + 1, p * p):
            mu[j] = 0
    return mu


def independent_mu(n):
    s = 1
    v = n
    for p in range(2, int(n**0.5) + 2):
        if v % p:
            continue
        v //= p
        s = -s
        if v % p == 0:
            return 0
        while v % p == 0:
            v //= p
    if v > 1:
        s = -s
    return s


def primes(n):
    q = bytearray(b'\x01') * (n + 1)
    q[:2] = b'\x00\x00'
    for p in range(2, int(n**0.5) + 1):
        if q[p]:
            for k in range(p*p, n+1, p):
                q[k] = 0
    return [p for p in range(2, n + 1) if q[p]]


def energy(f, alpha, exact=False):
    n = len(f)-1
    if exact:
        return sum((Fraction(f[k]**2, k**alpha)-Fraction(f[k]**2, (k+1)**alpha)
                    for k in range(1,n)), Fraction(0))
    return sum((f[k]**2 * (k**(-alpha) - (k+1)**(-alpha)) for k in range(1,n)))


def removed_primes(mu, cutoff, P):
    result = [0] * (cutoff+1)
    for k in range(1,cutoff+1):
        result[k] = result[k-1] + (mu[k] if all(k%p for p in P) else 0)
    return result


def reconstruct(mp, P):
    current = mp[:]
    for p in P:
        prev = current
        current = [prev[k]-prev[k//p] for k in range(len(prev))]
    return current


def main():
    cutoff=16384
    mu=mobius_sieve(cutoff)
    for k in range(1,1001):
        assert mu[k]==independent_mu(k), ('wrong mu sieve', k)
    M=[0]*(cutoff+1)
    for k in range(1,cutoff+1):
        M[k]=M[k-1]+mu[k]
    sets=((),(2,),(2,3),(2,3,5),(2,3,5,7),
          (2,3,5,7,11),(2,3,5,7,11,13))
    alphas=(1.25,1.5,2.0,3.0)
    out=Path(__file__).resolve().parent
    with (out/'riemann_phase27_energy.csv').open('w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(('N','primes_removed','alpha','energy_M','energy_MP',
                         'norm_ratio_M_over_MP','lower_constant','upper_constant'))
        for P in sets:
            mp=removed_primes(mu,cutoff,P)
            assert reconstruct(mp,P)==M, ('reconstruction failed',P)
            # Separate *rational* check at N=256 and alpha=2.
            m256=M[:257]
            mp256=mp[:257]
            e=energy(m256,2,exact=True)
            ep=energy(mp256,2,exact=True)
            lo=prod((Fraction(p-1,p) for p in P), start=Fraction(1))
            hi=prod((Fraction(p+1,p) for p in P), start=Fraction(1))
            assert lo**2*ep<=e<=hi**2*ep,('exact energy failed',P)
            for alpha in alphas:
                E=energy(M,alpha)
                Ep=energy(mp,alpha)
                lo=prod(1-p**(-alpha/2) for p in P)
                hi=prod(1+p**(-alpha/2) for p in P)
                assert lo**2*Ep <= E+1e-10 and E <= hi**2*Ep+1e-10
                writer.writerow((cutoff,' '.join(map(str,P)),alpha,f'{E:.12f}',
                                 f'{Ep:.12f}',f'{(E/Ep)**0.5:.12f}',
                                 f'{lo:.12f}',f'{hi:.12f}'))
    with (out/'riemann_phase27_operator_norms.csv').open('w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(('prime_cutoff_y','alpha','num_primes',
                         'exact_inverse_operator_norm','exact_forward_operator_norm'))
        for y in (10,100,1000,10000,100000):
            ps=primes(y)
            for alpha in (1.5,2.0,2.5,3.0):
                inv=prod(1/(1-p**(-alpha/2)) for p in ps)
                fwd=prod(1+p**(-alpha/2) for p in ps)
                writer.writerow((y,alpha,len(ps),f'{inv:.12f}',f'{fwd:.12f}'))
    print('PASS 1000 Möbius trial-division comparisons')
    print('PASS 7 exact finite-prime reconstructions at N=16384')
    print('PASS 7 exact rational finite-norm inequalities at N=256, alpha=2')
    print('PASS 28 finite real-exponent energy inequalities at N=16384')
    print('WROTE riemann_phase27_energy.csv and riemann_phase27_operator_norms.csv')


if __name__=='__main__':
    main()
