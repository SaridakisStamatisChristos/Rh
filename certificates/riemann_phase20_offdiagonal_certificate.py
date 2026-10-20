#!/usr/bin/env python3
"""Phase XX. Exact arithmetic certification of finite Möbius transfer identities.
Does not establish any uniform operator bound below exponent 2 or prove RH.
"""
from fractions import Fraction


def mobius(limit):
    mu = [0] + [1] * limit
    composite = [False] * (limit + 1)
    for p in range(2, limit + 1):
        if composite[p]:
            continue
        for j in range(p, limit + 1, p):
            mu[j] *= -1
            if j > p:
                composite[j] = True
        for j in range(p*p, limit + 1, p*p):
            mu[j] = 0
    return mu


def verify(n, alpha):
    mu = mobius(n)
    M = [0] * (n + 1)
    for k in range(1, n + 1):
        M[k] = M[k-1] + mu[k]
    T = [[M[k//d] if d <= k else 0 for d in range(1, n + 1)]
         for k in range(1, n + 1)]
    assert all(sum(row) == 1 for row in T)
    w = [Fraction(1, k**alpha) - Fraction(1, (k+1)**alpha)
         for k in range(1, n)]
    w += [Fraction(1, n**alpha)]
    assert sum(w) == 1

    H = [[sum(w[k] * T[k][d] * T[k][e] for k in range(n))
          for e in range(n)] for d in range(n)]
    trace = sum(H[d][d] for d in range(n))
    total = sum(sum(row) for row in H)
    off = total - trace
    assert total == 1
    assert off == 1 - trace
    assert trace > 1 if n >= 3 else trace == 1
    assert trace >= sum(Fraction(1, k**alpha) for k in range(1,n+1))/2

    for d in range(1,n+1):
        row_sum = sum(H[d-1])
        expected = sum((Fraction(mu[m], (d*m)**alpha)
                       for m in range(1, n//d+1)), Fraction(0))
        assert row_sum == expected, (n, alpha, d, row_sum, expected)

        diagonal = sum((Fraction(mu[m]*mu[t], (d*max(m,t))**alpha)
                        for m in range(1,n//d+1)
                        for t in range(1,n//d+1)), Fraction(0))
        assert H[d-1][d-1] == diagonal

    assert sum(H[0]) == sum(
        (Fraction(mu[m],m**alpha) for m in range(1,n+1)), Fraction(0))
    return {'N':n, 'alpha':alpha, 'trace':trace, 'offdiag':off,
            'row1':sum(H[0]), 'H12':H[0][1],
            'H13':H[0][2] if n>=3 else None,
            'H23':H[1][2] if n>=3 else None}


def main():
    for n in (3,5,8,16,32):
        for alpha in (1,2,3):
            r=verify(n,alpha)
            print(f'PASS N={n} alpha={alpha} tr={float(r["trace"]):.9f} '
                  f'offdiag={float(r["offdiag"]):.9f}')

    case3 = verify(3,1)
    assert case3['H12']==Fraction(-1,3)
    assert case3['H13']==Fraction(-1,3)
    assert case3['H23']==Fraction(1,3)
    assert case3['trace']==Fraction(5,3)
    assert case3['offdiag']==Fraction(-2,3)

    case5=verify(5,1)
    assert case5['row1']==Fraction(-1,30)
    print('EXACT COUNTEREXAMPLES PASS: H12=H13=-1/3 and H23=+1/3 at N=3,alpha=1; '
          'first row sum=-1/30 at N=5,alpha=1')
    print('ALL EXACT MATRIX TESTS PASS; NO CLAIM OF RH PROOF')


if __name__=='__main__':
    main()
