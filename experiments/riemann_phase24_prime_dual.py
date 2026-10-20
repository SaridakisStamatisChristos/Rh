#!/usr/bin/env python3
"""Phase XXIV: prime-coordinate inverse Gram identity, exact Schur complement,
and stable normalized spectrum. Pure Python exact arithmetic for core checks.
These are finite tests, NOT a proof of RH.
"""
from fractions import Fraction
from math import isqrt

def primes(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,isqrt(p)+1))]

def weights(n,alpha):
    return [Fraction(1,k**alpha)-Fraction(1,(k+1)**alpha)
            for k in range(1,n)]+[Fraction(1,n**alpha)]

def mobius(n):
    mu=[0]+[1]*n
    for p in primes(n):
        for k in range(p,n+1,p): mu[k]*=-1
        for k in range(p*p,n+1,p*p): mu[k]=0
    return mu

def exact_matrices(n,alpha):
    w=weights(n,alpha)
    B=[[int(d%k==0)-int(d%(k+1)==0) for k in range(1,n+1)] for d in range(1,n+1)]
    G=[[sum((Fraction(B[d][k]*B[e][k],1)/w[k] for k in range(n)),Fraction(0))
        for e in range(n)] for d in range(n)]
    mu=mobius(n)
    M=[0]
    for x in mu[1:]:M.append(M[-1]+x)
    T=[[M[k//d] if d<=k else 0 for d in range(1,n+1)]
       for k in range(1,n+1)]
    H=[[sum((w[k]*T[k][d]*T[k][e] for k in range(n)),Fraction(0))
        for e in range(n)] for d in range(n)]
    return w,B,H,G

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Fraction(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def prime_schur_bound(z,R,w):
    by={i:z[i-1] for i in R}
    bound=w[0]*by[1]**2+w[1]*by[2]**2+w[2]*(by[3]+by[2]-by[1])**2
    for p in R:
        if p>=5:
            d=1/w[p-2]+1/w[p-1]
            bound+=(by[p]-by[1])**2/d
    return bound

def exact_tests():
    cases=0
    for n in (3,5,8,12,18):
        for alpha in (1,2,3):
            w,B,H,G=exact_matrices(n,alpha)
            odd=[p for p in primes(n) if p>=3]
            c0=1/w[0]
            for p in odd:
                for q in odd:
                    want=c0+(1/w[p-2]+1/w[p-1] if p==q else 0)
                    assert G[p-1][q-1]==want,(n,alpha,p,q)
            R=[1,2]+odd
            gr=[[G[p-1][q-1] for q in R] for p in R]
            K=[]
            for p in R:
                row=[]
                for q in R:
                    v1=int(p==1);w1=int(q==1)
                    v2=int(p==2);w2=int(q==2)
                    v3=int(p==3);w3=int(q==3)
                    val=w[0]*v1*w1+w[1]*v2*w2+w[2]*(v2+v3-v1)*(w2+w3-w1)
                    for prime in odd:
                        if prime>=5:
                            d=1/w[prime-2]+1/w[prime-1]
                            val+=(int(p==prime)-v1)*(int(q==prime)-w1)/d
                    row.append(val)
                K.append(row)
            identity=[[int(i==j) for j in range(len(R))] for i in range(len(R))]
            assert matmul(gr,K)==identity
            assert matmul(K,gr)==identity
            z=[Fraction((7*d*d+13*d+3)%11-5) for d in range(1,n+1)]
            q=sum((z[i]*H[i][j]*z[j] for i in range(n) for j in range(n)),Fraction(0))
            assert q>=prime_schur_bound(z,R,w)
            cases+=1
        print(f'EXACT PASS N={n}')
    assert cases==15
    w,B,H,G=exact_matrices(18,2)
    assert G[8][14]==1/w[0]+1/w[1]+1/w[2]
    print('EXACT COMPOSITE COUNTEREXAMPLE PASS: Hinv[9,15] = c1+c2+c3')
    print('EXACT PASS: 15 test cases across five dimensions and three exponents')

def examples():
    for n in (31,127,509,1021):
        for alpha in (1.,1.5,2.):
            pp=[p for p in primes(n) if p>=3]
            def w(k):
                return k**(-alpha)-(k+1)**(-alpha) if k<n else n**(-alpha)
            nonunit=1+(1/w(1))*sum(1/(1/w(p-1)+1/w(p)) for p in pp)
            cutoff=100000
            partial=sum(m**(-alpha-1) for m in range(2,cutoff))
            tail=(cutoff-1)**(-alpha)/alpha
            upper=1+alpha/(1-2**(-alpha))*(partial+tail)
            assert nonunit<=upper+1e-10
            print(f'N={n} alpha={alpha:.2f} odd_primes={len(pp)} '
                  f'normalized_nonunit_eigenvalue={nonunit:.10f} '
                  f'conservative_upper={upper:.10f}')
    print('ALL CHECKS PASS; no fixed-alpha primal operator bound is claimed')

if __name__=='__main__':
    exact_tests()
    examples()
