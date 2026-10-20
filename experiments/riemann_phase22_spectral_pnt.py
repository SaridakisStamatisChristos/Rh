#!/usr/bin/env python3
"""Phase XXII: reproducible PNT-scale spectral diagnostics, not an RH proof.

Verifies finite matrix trace formula and normalizes the exact trace and first
column by N**(2-alpha). The proved equivalences are in the companion note.
"""
from fractions import Fraction
import math
import numpy as np


def mobius_sieve(limit):
    mu = [1] * (limit + 1)
    mu[0] = 0
    marked = bytearray(limit + 1)
    for p in range(2, limit + 1):
        if marked[p]:
            continue
        for j in range(p, limit + 1, p):
            mu[j] = -mu[j]
            marked[j] = 1 if j > p else marked[j]
        for j in range(p * p, limit + 1, p * p):
            mu[j] = 0
    return mu


def trace_formula(n, alpha, M):
    Q = [0.0] * (n + 1)
    energy = 0.0
    for k in range(1, n + 1):
        if k > 1:
            energy += ((k - 1) ** (-alpha) - k ** (-alpha)) * M[k - 1] ** 2
        Q[k] = energy + k ** (-alpha) * M[k] ** 2
    trace = sum(d ** (-alpha) * Q[n // d] for d in range(1, n + 1))
    return trace, Q[n]


def trace_direct(n, alpha, M):
    k = np.arange(1, n + 1, dtype=np.int64)
    d = np.arange(1, n + 1, dtype=np.int64)
    T = np.where(d[None, :] <= k[:, None], np.asarray(M)[(k[:, None] // d[None, :])], 0).astype(float)
    w = np.empty(n)
    w[:-1] = k[:-1].astype(float) ** (-alpha) - (k[:-1] + 1).astype(float) ** (-alpha)
    w[-1] = n ** (-alpha)
    H = (T.T * w) @ T
    return float(np.trace(H)), float(np.linalg.eigvalsh(H)[-1])


def exact_check():
    for n in (4, 8, 16):
        mu = mobius_sieve(n)
        M = [0]
        for x in mu[1:]:
            M.append(M[-1] + x)
        for alpha in (1, 2, 3):
            def wt(k):
                return Fraction(1, k ** alpha) - Fraction(1, (k + 1) ** alpha) if k < n else Fraction(1, n ** alpha)
            lhs = sum((wt(k) * sum(M[k // d] ** 2 for d in range(1, k + 1)) for k in range(1, n + 1)), Fraction())
            q = []
            for m in range(1, n + 1):
                val = sum(((Fraction(1,k**alpha)-Fraction(1,(k+1)**alpha))*M[k]**2 for k in range(1,m)),Fraction())
                q.append(val + Fraction(M[m]**2,m**alpha))
            rhs = sum((Fraction(1, d**alpha) * q[n//d-1] for d in range(1,n+1)),Fraction())
            assert lhs == rhs, (n,alpha)
    print('EXACT FINITE TRACE IDENTITIES: 9/9 PASS')


def main():
    exact_check()
    checkpoints = [128, 512, 2048, 8192, 32768, 131072, 524288]
    limit = checkpoints[-1]
    mu = mobius_sieve(limit)
    M = [0] * (limit+1)
    for n in range(1,limit+1): M[n] = M[n-1] + mu[n]
    print('N,alpha,trace,Q_alpha,trace_over_Npow,Qalpha_over_Npow,largest_eig')
    for n in checkpoints:
        for alpha in (1.25,1.5,1.75):
            trace,q = trace_formula(n,alpha,M)
            direct_eig = ''
            if n<=512:
                tr,eig=trace_direct(n,alpha,M)
                assert abs(tr-trace)<1e-8, (n,alpha,tr,trace)
                assert 0<=eig<=tr+1e-8
                direct_eig=f'{eig:.9g}'
            scale=n**(2-alpha)
            print(f'{n},{alpha:.2f},{trace:.10f},{q:.10f},{trace/scale:.10f},{q/scale:.10f},{direct_eig}')
    print('ALL TESTS PASSED; SPECTRAL RATIOS ARE FINITE DIAGNOSTICS, NOT ASYMPTOTIC EVIDENCE')


if __name__=='__main__':main()
