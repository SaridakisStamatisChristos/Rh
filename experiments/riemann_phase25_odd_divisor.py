#!/usr/bin/env python3
"""Phase XXV: odd-index inverse Gram factorization and sharp Schur interpolation.
Exact Fraction verification plus optional NumPy eigenvalue diagnostics.
These are finite crosschecks, not a proof of the Riemann hypothesis.
"""
from fractions import Fraction

def mobius(n):
    mu=[0]+[1]*n
    mark=[False]*(n+1)
    for p in range(2,n+1):
        if mark[p]: continue
        for j in range(p,n+1,p):
            mu[j]*=-1
            mark[j]=True if j>p else mark[j]
        for j in range(p*p,n+1,p*p): mu[j]=0
    return mu

def weights(n,a):
    return [Fraction(1,k**a)-Fraction(1,(k+1)**a) for k in range(1,n)]+[Fraction(1,n**a)]

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), Fraction(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def validate(n,alpha,mu):
    w=weights(n,alpha); c=[None]+[1/v for v in w]
    M=[0]
    for v in mu[1:]:M.append(M[-1]+v)
    T=[[M[k//d] if d<=k else 0 for d in range(1,n+1)] for k in range(1,n+1)]
    B=[[int(d%k==0)-int(d%(k+1)==0) for k in range(1,n+1)]
        for d in range(1,n+1)]
    H=[[sum((w[k]*T[k][d]*T[k][e] for k in range(n)),Fraction(0))
        for e in range(n)] for d in range(n)]
    inv=[[sum((c[k+1]*B[d][k]*B[e][k] for k in range(n)),Fraction(0))
          for e in range(n)] for d in range(n)]
    odds=list(range(1,n+1,2))
    gamma={1:c[1]}
    gamma.update({r:c[r-1]+c[r] for r in odds if r>1})
    for d in odds:
        for e in odds:
            want=sum((gamma[r] for r in odds if d%r==0 and e%r==0),Fraction(0))
            assert inv[d-1][e-1]==want, (n,alpha,d,e)
    L=[[int(d%r==0) for r in odds] for d in odds]
    Lm=[[mu[d//r] if d%r==0 else 0 for r in odds] for d in odds]
    ident=[[int(i==j) for j in range(len(odds))] for i in range(len(odds))]
    assert matmul(L,Lm)==ident and matmul(Lm,L)==ident
    oddinv=[[sum((Fraction(Lm[k][i]*Lm[k][j],1)/gamma[odds[k]]
                  for k in range(len(odds))),Fraction(0))
             for j in range(len(odds))] for i in range(len(odds))]
    oddmat=[[inv[d-1][e-1] for e in odds] for d in odds]
    assert matmul(oddmat,oddinv)==ident
    R=[2]+odds
    rows=[(w[0],{1:1}),(w[1],{2:1}),(w[2],{1:-1,2:1,3:1})]
    for r in odds:
        if r>=5:
            rows.append((1/gamma[r],{d:mu[r//d] for d in odds if r%d==0}))
    K=[[sum((coeff*vec.get(d,0)*vec.get(e,0) for coeff,vec in rows),Fraction(0))
        for e in R] for d in R]
    GR=[[inv[d-1][e-1] for e in R] for d in R]
    identity=[[int(i==j) for j in range(len(R))] for i in range(len(R))]
    assert matmul(GR,K)==identity and matmul(K,GR)==identity
    z=[Fraction(((13*d*d+7*d+2)%17)-8) for d in range(1,n+1)]
    q=sum((z[i]*H[i][j]*z[j] for i in range(n) for j in range(n)),Fraction(0))
    rhs=w[0]*z[0]**2+w[1]*z[1]**2+w[2]*(z[1]+z[2]-z[0])**2
    for r in odds:
        if r>=5:
            term=sum((mu[r//d]*z[d-1] for d in odds if r%d==0),Fraction(0))
            rhs+=term**2/gamma[r]
    assert q>=rhs,(n,alpha,q,rhs)
    qmu=H[0][0]
    bound=w[0]+w[2]+sum((Fraction(1,gamma[r]) for r in odds if r>=5 and mu[r]),Fraction(0))
    assert qmu>=bound
    return n,alpha,float(qmu),float(bound)

def numerical(alpha,n):
    try: import numpy as np
    except ImportError: return None
    w=np.array([k**(-alpha)-(k+1)**(-alpha) for k in range(1,n)]+[n**(-alpha)])
    c=1/w
    odds=list(range(1,n+1,2))
    gamma=np.array([c[0] if r==1 else c[r-2]+c[r-1] for r in odds])
    L=np.array([[int(d%r==0) for r in odds] for d in odds],dtype=float)
    A=(L*gamma[None,:]**.5)/gamma[:,None]**.5
    eig=np.linalg.eigvalsh(A@A.T)
    return n,alpha,len(odds),float(eig[0]),float(eig[-1])

def main():
    cases=[]
    for n in (3,5,8,12,15,21,32,40):
        mu=mobius(n)
        for alpha in (1,2,3):
            cases.append(validate(n,alpha,mu))
    assert len(cases)==24
    print("EXACT_ODD_DIVISOR_TESTS: PASS 24/24")
    for item in cases:
        if item[0] in (15,32) and item[1] in (1,2):
            print("CORRELATION_AND_SHARP_LOWER_BOUND",item)
    for alpha in (1.0,1.25,1.5,2.0):
        for n in (32,64,128,256):
            print("NORMALIZED_ODD_BLOCK_SPECTRUM",numerical(alpha,n))
    print("ALL CHECKS PASS. THESE RESULTS DO NOT PROVE RH.")

if __name__=="__main__":
    main()
