# A certified weighted Möbius-correlation sign theorem

**Status:** A rigorously reduced theorem with a finite exact-arithmetic certificate and elementary analytic tail. **Not a proof of the Riemann hypothesis.** The broader Möbius–Mertens anticorrelation conjecture is discussed in G. Chavez, *Multiplicative function anticorrelation and upper bounds on 1/zeta'(rho)*, arXiv:2409.02106 (2024). Novelty of this particular bound has not been established.

## Statement

For the Möbius function `mu` and `M(x)=sum_{n<=x} mu(n)`, every integer `N>=2` and every real `epsilon>=7/12` satisfy

\[
\sum_{n\le N}\frac{\mu(n)M(n-1)}{n^{1+2\varepsilon}}
<-\frac{11}{400\,2^{1+2\varepsilon}}<0.
\]

## Proof

Let `alpha = 1+2 epsilon >= 13/6`, `a_n = mu(n)M(n-1)`, and `a_n^+ = max(a_n,0)`. Directly, `a_1=0, a_2=-1, a_3=a_4=0`; hence

\[
2^\alpha C_\epsilon(N) = -1 + \sum_{5\le n\le N}a_n (2/n)^\alpha
\le -1+\sum_{5\le n\le N}a_n^+(2/n)^{13/6}.
\]

Take `K=2^25`. A deterministic Möbius sieve with *upward-rounded integer arithmetic* establishes

\[
P_2(K):=4\sum_{n=5}^{K}\frac{a_n^+}{n^2}
\le\frac{456992209700}{10^{12}}<\frac{23}{50}.
\]

Because `(2/5)^(1/6)<7/8`, the contribution from `5<=n<=K` is less than `(7/8)(23/50)=161/400`.

For `S(x)=sum_{n<=x} mu(n)^2`, the square-divisor identity gives

\[
S(x)=d x+E(x),\qquad d=6/\pi^2<61/100,\qquad |E(x)|\le3\sqrt x.
\]

To verify the error bound, put `h=floor(sqrt(x))>=sqrt(x)/2`, write `S(x)=sum_{r<=h} mu(r) floor(x/r^2)`, and compare with `x sum_{r>=1} mu(r)/r^2`; the floor errors total at most `h`, and the omitted tail is at most `x/h`. Thus `|E(x)|<=sqrt(x)+2sqrt(x)`.

Let `R_s(K)=sum_{n>K} mu(n)^2/n^s`, `s>1`. Partial summation and `|E(x)|<=3sqrt(x)` imply

\[
R_s(K) \le \frac{dK^{1-s}}{s-1}+
3\left(\frac{s}{s-1/2}+1\right)K^{1/2-s}.
\]

Since `a_n^+ <= mu(n)^2 S(n-1) <= mu(n)^2(d n+3sqrt(n))`, the tail at exponent `13/6` is at most

\[
T:=2^{13/6}\{d R_{7/6}(K)+3R_{5/3}(K)\}.
\]

Use the rational inequalities

- `2^(13/6)<9/2`;
- `K^(-1/6)=2^(-25/6)<9/160`;
- `K^(-2/3)=2^(-50/3)<1/98304`;
- `K^(-7/6)=2^(-175/6)<9/(10*2^29)`.

Substitution, with `d<61/100`, gives the purely rational upper bound

\[
T < \frac{26564248299609}{46976204800000}<\frac{57}{100}.
\]

Combining the finite prefix and infinite tail,

\[
2^\alpha C_\epsilon(N) < -1+\frac{161}{400}+\frac{57}{100}=-\frac{11}{400}.
\]

When `N<=K`, the finite prefix estimate alone suffices. QED.

## How to verify the arithmetic

```bash
g++ -std=c++17 -O3 -Wall -Wextra riemann_phase10_weighted_sign_certificate.cpp -o phase10
./phase10
```

Expected summary: `P2(K)<23/50: YES`, `tail<57/100: YES`, and `normalized negativity margin >=11/400: YES`.

An independent **floating-point only** linear-sieve cross-check gave `P2(K)≈0.4569870376577961`, agreeing with the rigorous rational upper bound. The integer-arithmetic certificate, not the floating-point check, justifies the strict inequality.

## Limitation / explicit stopping point

The result applies only to `epsilon>=7/12>1/2`, which gives no nontrivial zero-free improvement for zeta. The squarefree-density majorant has a sharp barrier at the exponent `alpha=2`:

\[
\sum_{n\le X}\frac{\mu(n)^2 S(n-1)}{n^2}
=\frac{36}{\pi^4}\log X+O(1).
\]

This diverges, so that specific positive-only majorant cannot establish the sought inequality at `epsilon=1/2` or below. Signed cancellation or stronger, explicit estimates must be used. It does not imply the *actual* correlation becomes positive, nor rule out different positive-part bounds.