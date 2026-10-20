#!/usr/bin/env python3
"""Phase XXX: exact Walsh expansion, ensemble variance, and certified aggregate signs.
Proofs in matching Phase XXX note. All finite checks are deterministic.
"""
from fractions import Fraction
from itertools import product
from math import gcd

SCALE = 10**14
K = 65536


def sieve_mu(n):
    mu = [1] * (n+1); mu[0] = 0
    marked = bytearray(n+1)
    for p in range(2,n+1):
        if marked[p]: continue
        for j in range(p,n+1,p):
            mu[j] = -mu[j]
            if j > p: marked[j] = 1
        for j in range(p*p,n+1,p*p): mu[j] = 0
    return mu


def trial_mu(n):
    v=n; sign=1; p=2
    while p*p<=v:
        if v%p==0:
            v//=p; sign=-sign
            if v%p==0:return 0
        p+=1
    return -sign if v>1 else sign


def subset_product(P, bits):
    v=1
    for i,p in enumerate(P):
        if (bits>>i)&1: v*=p
    return v


def inner_scaled(b,da,db,alpha):
    # For f(x)=sum b_n 1_{x>=n}: <S_da f, S_db f>_alpha.
    return sum((Fraction(x*y,max(da*m,db*n)**alpha)
                for m,x in b.items() for n,y in b.items()),Fraction(0))


def walsh_coefficients(P,b,alpha):
    r=len(P); ds=[subset_product(P,s) for s in range(1<<r)]
    coefficients=[]
    for u in range(1<<r):
        outside=Fraction(1)
        for i,p in enumerate(P):
            if not (u>>i)&1: outside*=1+Fraction(1,p**alpha)
        subtotal=Fraction(0)
        a=u
        while True:
            subtotal+=inner_scaled(b,ds[a],ds[u^a],alpha)
            if a==0:break
            a=(a-1)&u
        coefficients.append(((-1)**u.bit_count())*outside*subtotal)
    return coefficients


def direct_energy(P,b,alpha,signs):
    r=len(P); coeffs={}
    for s in range(1<<r):
        eps=1
        for i in range(r):
            if (s>>i)&1: eps*=signs[i]
        mult=((-1)**s.bit_count())*eps
        d=subset_product(P,s)
        for n,bn in b.items():
            coeffs[d*n]=coeffs.get(d*n,0)+mult*bn
    # Q=sum_{n} (a_n^2+2a_n A_{n-1})/n^alpha exact.
    pref=0; E=Fraction(0)
    for n,v in sorted(coeffs.items()):
        if v: E+=Fraction(v*v+2*v*pref,n**alpha)
        pref+=v
    return E


def check_walsh():
    mu=sieve_mu(64); checks=0
    for P in ((2,3),(2,3,5),(2,3,5,7)):
        L=8
        b={n:mu[n] for n in range(1,L+1)
           if mu[n] and all(n%p for p in P)}
        for alpha in (2,3):
            cs=walsh_coefficients(P,b,alpha)
            energies=[]
            for signs in product((-1,1), repeat=len(P)):
                measured=direct_energy(P,b,alpha,signs)
                predicted=sum((cs[s] * product_value(signs,s)
                               for s in range(1<<len(P))), Fraction(0))
                assert measured==predicted,(P,alpha,signs,measured,predicted)
                energies.append(measured)
                checks+=1
            mean=sum(energies,Fraction(0))/len(energies)
            var=sum(((e-mean)**2 for e in energies),Fraction(0))/len(energies)
            assert mean==cs[0]
            assert var==sum((c*c for c in cs[1:]),Fraction(0))
            rvals=[Fraction(4*p**alpha,(p**alpha+1)**2) for p in P]
            variance_cap=cs[0]**2*(product_fraction(1+x for x in rvals)-1)
            assert var<=variance_cap
            for degree in range(len(P)+1):
                sumsq=sum((cs[u]**2 for u in range(1<<len(P))
                           if u.bit_count()>=degree),Fraction(0))
                R=sum(rvals,Fraction(0))
                rough=cs[0]**2*sum((R**k/factorial(k)
                                   for k in range(degree,degree+19)),Fraction(0))
                assert sumsq<=rough, (P,alpha,degree)
            print('EXACT_WALSH_PASS',P,'alpha=',alpha,'states=',len(energies),
                  'mean=',float(mean),'variance=',float(var),
                  'bound=',float(variance_cap))
    print('EXACT_ALL_WALSH_ENERGY_CASES_PASS:', checks)
    assert checks==2*(4+8+16)


def product_value(signs,subset):
    out=1
    for i in range(len(signs)):
        if (subset>>i)&1:out*=signs[i]
    return out


def product_fraction(values):
    x=Fraction(1)
    for v in values:x*=v
    return x


def factorial(n):
    v=1
    for k in range(2,n+1):v*=k
    return v


def energy_interval_cubed(F,K):
    lo=hi=0
    for k in range(1,K):
        v=F[k]**2
        numerator = v*(3*k*k+3*k+1)*SCALE
        denominator = (k*(k+1))**3
        lo += numerator//denominator
        hi += (numerator+denominator-1)//denominator
    return Fraction(lo,SCALE),Fraction(hi,SCALE)


def check_aggregate():
    mu=sieve_mu(K)
    assert all(mu[n]==trial_mu(n) for n in range(1,4097))
    M=[0]*(K+1)
    for n in range(1,K+1): M[n]=M[n-1]+mu[n]
    mlo,mhi=energy_interval_cubed(M,K)
    print('AGGREGATE: independent trial division 4096/4096 PASS')
    print('prime_set,alpha,lower,upper,sign')
    rows=[]
    for P in ((2,3),(2,5),(3,5),(2,3,5),(2,3,5,7),(2,3,5,7,11)):
        F=[0]*(K+1)
        for n in range(1,K+1):
            F[n]=F[n-1]+(mu[n] if all(n%p for p in P) else 0)
        flo,fhi=energy_interval_cubed(F,K)
        D=product_fraction(Fraction(1)+Fraction(1,p**3) for p in P)
        # Infinite nonnegative energy tails bounded by 3/K each.
        low=mlo-D*(fhi+Fraction(3,K))
        high=mhi+Fraction(3,K)-D*flo
        sign='negative' if high<0 else 'positive' if low>0 else 'undetermined'
        rows.append((P,low,high,sign))
        print(';'.join(map(str,P)),3,f'{float(low):+.12f}',f'{float(high):+.12f}',sign,sep=',')
    assert any(row[3]=='positive' for row in rows)
    assert any(row[3]=='negative' for row in rows)
    print('AGGREGATE INFINITE-SIGN ENCLOSURES PASS')
    return rows


def main():
    check_walsh()
    check_aggregate()
    print('ALL TESTS PASS: RANDOM ENSEMBLE != DETERMINISTIC RH PROOF')

if __name__ == '__main__':main()
