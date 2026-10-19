# Riemann Hypothesis investigation — Phase XI

Status: verified unconditional boundary-convergence theorem and a numerical cross-check; **not a proof of RH**. Date: 2026-10-20.

Let μ be the Möbius function, M(x)=sum_{n<=x} μ(n), and

C_α(N)=sum_{n<=N} μ(n)M(n-1)/n^α,   Q_α(N)=sum_{m,n<=N} μ(m)μ(n)/max(m,n)^α.

**Theorem (boundary absolute convergence).** For every integer r>=0,

  sum_{n>=2} |μ(n)M(n-1)| (log n)^r /n^2 < infinity.

Consequently C_α(infinity) exists absolutely at α=2; all right-sided derivatives of C_α(infinity) at α=2 are finite. This says nothing about analytic continuation to α<2.

**Proof.** The classical Korobov–Vinogradov zero-free region gives for every A>0 an unconditional bound M(x)=O_A(x/(log x)^A). Therefore |μ(n)M(n-1)| (log n)^r/n^2 <= const/[n(log n)^(A-r)], summable when A>r+1. End.

**Exact energy identity.** For every α>0 and finite N,

  Q_α(N)=sum_{k=1}^{N-1} (k^-α-(k+1)^-α) M(k)^2 + M(N)^2/N^α
         =sum_{n<=N} μ(n)^2/n^α +2 C_α(N).

At α=2, M(N)=o(N), so the boundary term vanishes. Moreover the energy series converges because M(x)=O_A(x/log^A x) with A>1/2, and k^-2-(k+1)^-2=O(k^-3). Hence

  2 C_2(infinity) = sum_{k>=1}(k^-2-(k+1)^-2)M(k)^2 - ζ(2)/ζ(4).

**Poisson/Dirichlet identity.** For finite N, with D_N(s)=sum_{n<=N} μ(n)n^-s,

  Q_2(N)=(1/π) int_{-infty}^infty |D_N(1+it)|^2/(1+t^2) dt.

Classical Mertens bounds give local-uniform convergence of D_N(1+it) to 1/ζ(1+it) (with 1/ζ(1)=0), and the tail quadratic identity above gives L² convergence with the Poisson weight. Thus

  2 C_2(infinity)= (1/π) int_{-infty}^infty dt/[(1+t^2)|ζ(1+it)|²] - ζ(2)/ζ(4).

A *sufficient* analytic inequality to make this boundary-limit correlation negative is

  (1/π) int |1/ζ(1+it)|²/(1+t²) dt < ζ(2)/ζ(4).

No rigorous proof of this particular strict inequality is claimed. Even if proved, it would be a result at α=2, **not** a proof of RH: RH requires substantially stronger information corresponding to α approaching 1 from above.

**Numerical checks, not bounds on the infinite tail.** Running the accompanying C++ sieve at N=33,554,432 produced

  M(N)=-1042,
  C_2(N)≈-0.2804020912566827,
  Q_2(N)≈0.9590135540040768,
  sum_{n<=N} μ(n)^2/n²≈1.519817736517442.

These computations cannot certify the sign of the limit C_2(infinity), despite absolute convergence, without an explicit sufficiently strong numerical tail bound.

**Literature:** See Walfisz's classical unconditional Mertens estimate, discussed at https://mathoverflow.net/questions/293738/best-estimate-of-the-mertens-function-without-assuming-the-riemann-hypothesis ; and Gordon Chavez's existing Mobius correlation research, https://arxiv.org/abs/2409.02106 . The Clay Mathematics Institute classifies RH as unsolved: https://www.claymath.org/millennium/riemann-hypothesis/ .