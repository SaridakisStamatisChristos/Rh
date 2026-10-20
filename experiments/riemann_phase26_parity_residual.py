#!/usr/bin/env python3
"""Phase XXVI: exact odd-index GCD factorization and sharp parity interpolation.

Pure-stdlib exact rational tests check factorization, inverse, and equality cases.
Float diagnostics on the real Mobius sequence are finite observations only.
No proof of the Riemann hypothesis is claimed.
"""
from fractions import Fraction
from math import gcd, isqrt
from random import Random


def mobius(N):
    mu=[0]+[1]*N
    marked=[False]*(N+1)
    for p in range(2,N+1):
        if marked[p]: continue
        for k in range(p,N+1,p):
            mu[k]=-mu[k]
            if k>p: marked[k]=True
        for k in range(p*p,N+1,p*p):mu[k]=0
    return mu


def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Fraction())
             for j in range(len(B[0]))] for i in range(len(A))]


def weights(N,alpha):
    return [None]+[Fraction(1,k**alpha)-Fraction(1,(k+1)**alpha)
                    for k in range(1,N)] +[Fraction(1,N**alpha)]


def forms(N,alpha):
    mu=mobius(N)
    M=[0]
    for v in mu[1:]:M.append(M[-1]+v)
    w=weights(N,alpha)
    c=[None]+[1/x for x in w[1:]]
    T=[[M[k//d] if d<=k else 0 for d in range(1,N+1)]
       for k in range(1,N+1)]
    B=[[int(d%k==0)-int(d%(k+1)==0) for k in range(1,N+1)]
       for d in range(1,N+1)]
    G=[[sum((c[k+1]*B[d-1][k]*B[e-1][k]
              for k in range(N)),Fraction())
       for e in range(1,N+1)] for d in range(1,N+1)]
    H=[[sum((w[k+1]*T[k][d]*T[k][e]
              for k in range(N)),Fraction())
       for e in range(N)] for d in range(N)]
    odds=list(range(1,N+1,2))
    b={1:c[1]}
    b.update({d:c[d-1]+c[d] for d in odds if d>=3})
    return mu,w,c,T,B,G,H,odds,b


def certificate(N,alpha,trial_count=3):
    mu,w,c,T,B,G,H,odds,b=forms(N,alpha)
    o=len(odds)
    eye=lambda n:[[int(i==j) for j in range(n)] for i in range(n)]
    assert matmul(T,B)==eye(N) and matmul(B,T)==eye(N)
    # All-odd inverse block is a weighted GCD matrix; exact unimodular factorization.
    oddblock=[[G[d-1][e-1] for e in odds] for d in odds]
    E=[[int(t<=d and d%t==0) for t in odds] for d in odds]
    Einv=[[mu[d//t] if d%t==0 else 0 for t in odds] for d in odds]
    assert matmul(E,Einv)==eye(o) and matmul(Einv,E)==eye(o)
    odd_gcd=[[sum((b[t] for t in odds if gcd(d,e)%t==0),Fraction())
              for e in odds] for d in odds]
    assert oddblock==odd_gcd
    oddinv=[[sum((Fraction(Einv[k][i]*Einv[k][j],1)/b[odds[k]]
                   for k in range(o)),Fraction())
              for j in range(o)] for i in range(o)]
    assert matmul(oddblock,oddinv)==eye(o)
    det_prod=Fraction(1)
    for d in odds:det_prod*=b[d]
    # Schur block includes coordinate 2 plus all odd coordinates.
    R=[1,2]+[d for d in odds if d>=3]
    idx={d:i for i,d in enumerate(R)}
    G_R=[[G[d-1][e-1] for e in R] for d in R]
    def linear_vectors():
        out=[(w[1],{1:1}),(w[2],{2:1}),(w[3],{1:-1,2:1,3:1})]
        for n in odds:
            if n>=5:
                out.append((1/b[n],{d:mu[n//d] for d in odds if n%d==0}))
        return out
    vectors=linear_vectors()
    K=[[sum((weight*coeff.get(d,0)*coeff.get(e,0)
             for weight,coeff in vectors),Fraction()) for e in R] for d in R]
    assert matmul(G_R,K)==eye(len(R)) and matmul(K,G_R)==eye(len(R))
    for trial in range(trial_count):
        rng=Random(20261020+N*17+alpha*31+trial)
        a=[0]+[rng.randint(-3,3) for _ in range(N)]
        z=[0]*(N+1)
        for d in range(1,N+1):
            for k in range(d,N+1,d):z[k]+=a[d]
        A=[0]
        for value in a[1:]:A.append(A[-1]+value)
        Q=sum((w[k]*A[k]**2 for k in range(1,N+1)),Fraction())
        schur=sum((z[d]*K[i][j]*z[e] for i,d in enumerate(R)
                   for j,e in enumerate(R)),Fraction())
        local=w[1]*A[1]**2+w[2]*A[2]**2+w[3]*A[3]**2
        local+=sum((Fraction(a[t]**2,1)/b[t] for t in odds if t>=5),Fraction())
        assert local==schur
        residual=sum(((w[t-1]*A[t-1]+w[t]*A[t])**2/(w[t-1]+w[t])
                      for t in odds if t>=5),Fraction())
        if N%2==0:residual+=w[N]*A[N]**2
        assert Q==local+residual
        assert Q>=local
    print(f'PASS N={N} alpha={alpha} odd_dim={o}, R_dim={len(R)} ')


def exact_tests():
    count=0
    for N in (3,4,5,8,9,10,11,16,20,21,24,31):
        for alpha in (1,2,3):
            certificate(N,alpha)
            count+=1
    print(f'PASS: {count} exact cases and {3*count} exact polynomial vectors; '
          'T*B, GCD, inverse, 2+odd Schur, and residual decomposition')


def mobius_linear(N):
    mu=[0]*(N+1);mu[1]=1
    low=[0]*(N+1);ps=[]
    for n in range(2,N+1):
        if low[n]==0:
            low[n]=n;ps.append(n);mu[n]=-1
        for p in ps:
            k=n*p
            if k>N or p>low[n]:break
            low[k]=p
            if n%p==0:
                mu[k]=0;break
            mu[k]=-mu[n]
    return mu,ps


def numeric_diagnostics(Nlimit=524288):
    mu,primes=mobius_linear(Nlimit)
    M=[0]*(Nlimit+1)
    for n in range(1,Nlimit+1):M[n]=M[n-1]+mu[n]
    print('N,alpha,Q_mu,prime_lower,extended_lower,residual,fraction_residual')
    for N in (1024,8192,65536,524288):
        for alpha in (1.25,1.5,2.):
            def w(k):
                return k**(-alpha)-(k+1)**(-alpha) if k<N else N**(-alpha)
            Q=sum(w(k)*M[k]*M[k] for k in range(1,N+1))
            base=w(1)+w(3)   # for mu: M(1)=1, M(2)=0, M(3)=-1
            extended=base
            for k in range(5,N+1,2):
                if mu[k]:
                    wa,wb=w(k-1),w(k)
                    extended+=wa*wb/(wa+wb)
            prime=base
            for p in primes:
                if p>N:break
                if p>=5:
                    wa,wb=w(p-1),w(p)
                    prime+=wa*wb/(wa+wb)
            assert -1e-8<=prime<=extended+1e-8, (N,alpha,prime,extended)
            assert -1e-8<=extended<=Q+1e-8
            print(f'{N},{alpha:.2f},{Q:.12f},{prime:.12f},{extended:.12f},'
                  f'{Q-extended:.12f},{(Q-extended)/Q:.7f}')
    print('FINITE MOBIUS DIAGNOSTICS PASS (not evidence of RH)')

if __name__=='__main__':
    exact_tests()
    numeric_diagnostics()
