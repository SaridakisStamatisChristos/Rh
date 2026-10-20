#!/usr/bin/env python3
"""Phase XXIII: exact inverse identities and numerical spectrum of H_(alpha,N).

Proofs appear in research/riemann_phase23_inverse_spectrum.md.
Uses only Python stdlib for rational checks; NumPy is optional for eigenvalues.
This is a research verification, NOT a proof of RH.
"""
from fractions import Fraction
from math import floor

def mobius(limit):
    mu=[0]+[1]*limit
    marked=bytearray(limit+1)
    for p in range(2,limit+1):
        if marked[p]: continue
        for j in range(p,limit+1,p):
            mu[j]=-mu[j]
            if j>p: marked[j]=1
        for j in range(p*p,limit+1,p*p):
            mu[j]=0
    return mu

def matrices(n):
    mu=mobius(n)
    M=[0]
    for v in mu[1:]: M.append(M[-1]+v)
    T=[[M[k//d] if d<=k else 0 for d in range(1,n+1)]
       for k in range(1,n+1)]
    B=[[int(d%k==0)-int(d%(k+1)==0) for k in range(1,n+1)]
       for d in range(1,n+1)]
    return T,B

def product(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]

def exact_checks():
    cases=0
    for n in (3,4,8,12,20):
        T,B=matrices(n)
        assert product(T,B)==[[int(i==j) for j in range(n)] for i in range(n)]
        assert product(B,T)==[[int(i==j) for j in range(n)] for i in range(n)]
        for alpha in (1,2,3):
            w=[Fraction(1,k**alpha)-Fraction(1,(k+1)**alpha)
               for k in range(1,n)]+[Fraction(1,n**alpha)]
            H=[[sum(w[k]*T[k][i]*T[k][j] for k in range(n))
                for j in range(n)] for i in range(n)]
            Hinv=[[sum(Fraction(B[i][k]*B[j][k],1)/w[k] for k in range(n))
                    for j in range(n)] for i in range(n)]
            assert product(H,Hinv)==[[int(i==j) for j in range(n)] for i in range(n)]
            count=[n//k+n//(k+1)-2*(n//(k*(k+1)))
                   for k in range(1,n+1)]
            assert sum(Hinv[i][i] for i in range(n))==sum(
                Fraction(count[k],1)/w[k] for k in range(n))
            for k in range(1,n+1):
                assert count[k-1]==sum(B[d][k-1]**2 for d in range(n))
            if n>=4:
                d=2*(n//2)
                k=d//2
                assert B[d-1][k-1]==1
            cases+=1
        print(f'EXACT PASS n={n}')
    print(f'EXACT INVERSE/TRACE CHECKS: {cases}/{cases} PASS')

def spectral():
    try:
        import numpy as np
    except ImportError:
        print('NumPy not installed; optional spectral diagnostics skipped')
        return
    print('N,alpha,lambda_min,lambda_max,condition,'
          'inverse_trace_normalized,asymptotic_constant')
    for n in (32,64,128,256):
        T,B=matrices(n)
        TT=np.asarray(T,dtype=float)
        for alpha in (1.25,1.5,2.0):
            w=np.array([k**(-alpha)-(k+1)**(-alpha)
                         for k in range(1,n)]+[n**(-alpha)])
            H=(TT.T*w)@TT
            eig=np.linalg.eigvalsh(H)
            assert eig[0]>0
            formula=sum((n//k+n//(k+1)-2*(n//(k*(k+1))))/w[k-1]
                        for k in range(1,n+1))
            tr_inverse=sum(1.0/eig)
            assert abs(formula/tr_inverse-1)<1e-6
            zeta=sum(1.0/(k**(alpha+2)) for k in range(1,200001))
            target=2*zeta/(alpha*(alpha+2))
            assert eig[0] >= n**(-alpha-1)/(4*2**(alpha+1)/alpha*(1+1/(alpha-1))) * 0.999
            print(f'{n},{alpha},{eig[0]:.12g},{eig[-1]:.12g},'
                  f'{eig[-1]/eig[0]:.12g},'
                  f'{formula/n**(alpha+2):.12g},{target:.12g}')
    print('SPECTRAL CHECKS PASSED (finite observations, not RH)')

if __name__=='__main__':
    exact_checks()
    spectral()
