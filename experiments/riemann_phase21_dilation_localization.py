#!/usr/bin/env python3
"""Phase XXI: exact dilation/upper-half identities and finite spectral diagnostics.
The inequalities are proved in the companion note. No RH proof.
"""
from fractions import Fraction
from math import floor

def mobius(n):
    mu=[0]+[1]*n
    marked=[False]*(n+1)
    for p in range(2,n+1):
        if marked[p]: continue
        for k in range(p,n+1,p):
            mu[k]=-mu[k]
            if k>p: marked[k]=True
        for k in range(p*p,n+1,p*p): mu[k]=0
    return mu

def gram_exact(n,alpha):
    mu=mobius(n); M=[0]*(n+1)
    for k in range(1,n+1): M[k]=M[k-1]+mu[k]
    T=[[M[k//d] if d<=k else 0 for d in range(1,n+1)] for k in range(1,n+1)]
    w=[Fraction(1,k**alpha)-Fraction(1,(k+1)**alpha) for k in range(1,n)]
    w+=[Fraction(1,n**alpha)]
    return [[sum((w[k]*T[k][d]*T[k][e] for k in range(n)),Fraction(0))
             for e in range(n)] for d in range(n)]

def exact_tests():
    groups=0
    for n in (8,12,24,36):
        for alpha in (1,2,3):
            H=gram_exact(n,alpha)
            for d in (2,3,4,5):
                k=n//d
                h=gram_exact(k,alpha)
                for i in range(1,k+1):
                    for j in range(1,k+1):
                        assert H[d*i-1][d*j-1]==h[i-1][j-1]/d**alpha
                groups+=1
            D=n//2+1; L=n-D+1
            for i in range(D,n+1):
                for j in range(D,n+1):
                    assert H[i-1][j-1]==Fraction(1,max(i,j)**alpha)
            rowmax=max(sum(H[i-1][j-1] for j in range(D,n+1))
                       for i in range(D,n+1))
            assert Fraction(L,n**alpha)<=rowmax<=Fraction(L,D**alpha)
            groups+=1
        print(f'EXACT N={n}: PASS')
    assert groups==60
    print(f'EXACT TEST GROUPS={groups} PASS')

def numerical_tests():
    try: import numpy as np
    except ImportError:
        print('NumPy unavailable: spectral diagnostics skipped')
        return
    for n in (64,128,256):
        mu=mobius(n); M=[0]*(n+1)
        for k in range(1,n+1): M[k]=M[k-1]+mu[k]
        T=np.array([[M[k//d] if d<=k else 0 for d in range(1,n+1)]
                    for k in range(1,n+1)],dtype=float)
        for alpha in (1.25,1.50,1.75):
            w=np.array([k**(-alpha)-(k+1)**(-alpha) for k in range(1,n)]
                       +[n**(-alpha)])
            H=(T.T*w)@T
            eta=(alpha-1)/2
            D=floor(n**(2-alpha+eta))+1
            tr=float(np.trace(H[D-1:,D-1:]))
            bound=2/(2-alpha)*n**(2-alpha)/(D-1)
            assert tr<=bound+1e-10
            full=float(np.linalg.eigvalsh(H)[-1])
            low=float(np.linalg.eigvalsh(H[:D-1,:D-1])[-1])
            assert -1e-10<=full-low<=tr+1e-9
            print(f'N={n} alpha={alpha:.2f} D={D} full={full:.8f} '
                  f'low={low:.8f} delta={full-low:.8f} '
                  f'tail_trace={tr:.8f} analytic_bound={bound:.8f}')
    print('ALL NUMERICAL TESTS PASS')

if __name__=='__main__':
    exact_tests()
    numerical_tests()
