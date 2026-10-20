#!/usr/bin/env python3
"""Phase XIX: exact trace identity and finite spectral diagnostics.

Research diagnostic only. Not a proof of RH.
Global alpha>=2 estimate depends on the published Mertens bound and Phase XII.
"""
from fractions import Fraction
from math import pi

def mobius(n):
    mu=[1]*(n+1); mu[0]=0
    comp=[False]*(n+1)
    for p in range(2,n+1):
        if comp[p]: continue
        for k in range(p,n+1,p):
            mu[k]=-mu[k]
            if k>p: comp[k]=True
        if p*p<=n:
            for k in range(p*p,n+1,p*p): mu[k]=0
    return mu

def exact_trace(n,alpha):
    mu=mobius(n)
    M=[0]*(n+1)
    for k in range(1,n+1): M[k]=M[k-1]+mu[k]
    weights=[Fraction(1,k**alpha)-Fraction(1,(k+1)**alpha) for k in range(1,n)]
    weights.append(Fraction(1,n**alpha))
    direct=sum(weights[k-1]*sum(M[k//d]**2 for d in range(1,k+1))
               for k in range(1,n+1))
    q=[Fraction(0)]*(n+1)
    for size in range(1,n+1):
        q[size]=sum((Fraction(1,k**alpha)-Fraction(1,(k+1)**alpha))*M[k]**2
                    for k in range(1,size))
        q[size]+=Fraction(M[size]**2,size**alpha)
    formula=sum(Fraction(1,d**alpha)*q[n//d] for d in range(1,n+1))
    assert direct==formula, (n,alpha,direct,formula)
    return float(direct)

def spectral_diagnostics(n,alpha):
    try: import numpy as np
    except ImportError: return None
    mu=mobius(n)
    M=[0]*(n+1)
    for k in range(1,n+1): M[k]=M[k-1]+mu[k]
    T=np.zeros((n,n),dtype=float)
    for k in range(1,n+1):
        for d in range(1,k+1): T[k-1,d-1]=M[k//d]
    w=np.array([k**(-alpha)-(k+1)**(-alpha) for k in range(1,n)]
               +[n**(-alpha)],dtype=float)
    H=(T.T*w)@T
    return float(np.trace(H)),float(np.linalg.eigvalsh(H)[-1])

def main():
    for n in (4,8,12,24):
        for alpha in (1,2,3):
            v=exact_trace(n,alpha)
            print(f'EXACT PASS N={n} alpha={alpha} trace={v:.12f}')
    upper=2.5-pi*pi/30
    print(f'ALPHA_2_UNIVERSAL_UPPER={upper:.12f}')
    for n in (32,64,128,256):
        for alpha in (1.25,1.5,2.):
            result=spectral_diagnostics(n,alpha)
            if result is None:
                print('numpy unavailable; spectra skipped'); return
            tr,lam=result
            if alpha==2.: assert tr<upper
            print(f'N={n} alpha={alpha:.2f} trace={tr:.9f} lambda_max={lam:.9f}')
    print('PASS: exact identity, finite spectra (not RH)')

if __name__=='__main__': main()
