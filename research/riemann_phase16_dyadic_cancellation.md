# Phase XVI — Dyadic cancellation, a refuted sign strategy, and a randomized null model

**Date:** 20 October 2026. **Status:** exact arithmetic identities and conditional reductions; a finite computer-assisted certificate. **Not a proof of RH.** Novelty not established.

## Definitions

Let \(\mu\) denote the Möbius function, \(M(x)=\sum_{n\le x}\mu(n)\), and \(a_n=\mu(n)M(n-1)\). For \(\alpha>0\) define

\[
C_\alpha(N)=\sum_{n\le N}\frac{a_n}{n^\alpha},\qquad
B_{\alpha,j}=\sum_{2^j<n\le 2^{j+1}}\frac{a_n}{n^\alpha}\quad(j\ge0).
\]

## A short, rigorous counterexample to a proposed method

For \(n=5,6,7,8\) the coefficients \(a_n\) are \(1,-2,1,0\). Hence

\[
B_{\alpha,2}=5^{-\alpha}-2\cdot6^{-\alpha}+7^{-\alpha}>0\qquad(\alpha>0).
\]

The inequality is strict convexity of \(f(x)=x^{-\alpha}\). In particular, \(B_{1,2}=1/105\). Thus a proof strategy requiring *all dyadic blocks to be nonpositive* is refuted for every positive exponent.

## Complete finite certificate over a continuum of exponents

The included C++ program uses a Möbius sieve independently checked against trial division for \(1\le n\le2000\), and exact scaled-integer **floor** bounds for every rational term \(a_n/n\), with scale \(10^{12}\). It verifies for every \(2\le N\le10^7\) that

\[
C_1(N)<-299/1000.
\]

The largest rational upper endpoint recorded was \(-299999999995/10^{12}\) at \(N=5\), and there were zero nonnegative rational upper endpoints. The C++ accumulated floating-point values are diagnostic only; the certificate's sign check is performed by integer arithmetic.

By Abel summation, for any \(\alpha\ge1\), put \(w_n=n^{1-\alpha}\). Then

\[
C_\alpha(N)=C_1(N)w_N+\sum_{k=2}^{N-1}C_1(k)(w_k-w_{k+1})
<-\frac{299}{1000}\,w_2=-\frac{299}{1000}2^{1-\alpha}
\]

for \(2\le N\le10^7\). This is a genuinely continuous-exponent *finite* consequence. It does not address \(N>10^7\).

## One-sided dyadic positive-budget criterion

For fixed \(\alpha>1\), define \(B_{\alpha,j}^{+}=\max(0,B_{\alpha,j})\).

**Proposition (conditional zero-free half-plane).** If
\[
\sum_{j=0}^\infty B_{\alpha,j}^{+}<\infty,
\]
then \(\zeta(s)\ne0\) throughout \(\Re s>\alpha/2\).

*Proof.* At \(N=2^J\), \(C_\alpha(N)=\sum_{j<J}B_{\alpha,j}\le\sum_j B_{\alpha,j}^+\). Since \(\alpha>1\), the diagonal sum \(\sum_n\mu(n)^2n^{-\alpha}\) is finite. Therefore the exact positive-energy identity
\[
Q_\alpha(2^J)=\sum_{k<2^J}(k^{-\alpha}-(k+1)^{-\alpha})M(k)^2+\frac{M(2^J)^2}{2^{J\alpha}}
=\sum_{n\le2^J}\frac{\mu(n)^2}{n^\alpha}+2C_\alpha(2^J)
\]
shows the nondecreasing partial energies are uniformly bounded. Hence \(\sum_{k\ge1}M(k)^2/k^{\alpha+1}<\infty\). For \(\sigma>\alpha/2\), Cauchy–Schwarz gives
\[
\sum_{k\ge1}\frac{|M(k)|}{k^{\sigma+1}}
\le\left(\sum_{k\ge1}\frac{M(k)^2}{k^{\alpha+1}}\right)^{1/2}
\left(\sum_{k\ge1}k^{\alpha-2\sigma-1}\right)^{1/2}<\infty.
\]
The Mellin representation of \(1/\zeta\) therefore extends holomorphically into \(\Re s>\alpha/2\), excluding poles and hence zeta zeros there. QED.

**Corollary (RH equivalence).** RH holds iff \(\sum_j B_{\alpha,j}^+<\infty\) **for every** \(\alpha>1\).

Sufficiency is the proposition as \(\alpha\downarrow1\). For necessity, under RH, \(M(x)=O_\eta(x^{1/2+\eta})\) for every \(\eta>0\). The exact Abel identity on \([X,2X]\) is
\[
2\sum_{X<n\le2X}\frac{a_n}{n^\alpha}
=\frac{M(2X)^2}{(2X)^\alpha}-\frac{M(X)^2}{X^\alpha}
+\alpha\int_X^{2X}\frac{M(t)^2}{t^{\alpha+1}}dt
-\sum_{X<n\le2X}\frac{\mu(n)^2}{n^\alpha}.
\]
For dyadic \(X\), selecting \(0<\eta<(\alpha-1)/2\) makes the absolute value of each dyadic block at most \(O_\alpha(X^{1+2\eta-\alpha})\), a geometrically summable sequence. This yields even \(\sum_j|B_{\alpha,j}|<\infty\). QED.

This is an *equivalent formulation* of the unsolved RH problem, not an unconditional proof of the missing positive-budget bound. It has not been established as novel.

## Randomized-squarefree null model

Let \(b_n=\mu(n)^2\) be the actual squarefree support, and let \(\varepsilon_n\) be independent fair signs. Define \(\xi_n=b_n\varepsilon_n\), \(\widetilde M(N)=\sum_{n\le N}\xi_n\), and
\[
\widetilde C_\alpha(N)=\sum_{n\le N}\frac{\xi_n\widetilde M(n-1)}{n^\alpha}.
\]

The summands are martingale differences, so \(\mathbb E\widetilde C_\alpha(N)=0\), and their cross-covariances vanish:
\[
\mathrm{Var}\bigl(\widetilde C_\alpha(N)\bigr)=
\sum_{n\le N}\frac{b_n S(n-1)}{n^{2\alpha}},
\qquad S(y)=\sum_{k\le y}b_k.
\]

Using \(S(x)=d x+O(\sqrt{x})\), with \(d=6/\pi^2\), yields
\[
\mathrm{Var}\bigl(\widetilde C_1(N)\bigr)=d^2\log N+O(1).
\]
For each fixed \(\alpha>1\), the variance is bounded and \(\widetilde C_\alpha(N)\) converges almost surely and in \(L^2\). As \(\alpha\downarrow1\), its limiting variance is \(d^2/(2(\alpha-1))+O(1)\).

The null model crosses below exponent 2, but **the actual Möbius function is not a sequence of independent random signs**. The probabilistic theorem cannot be imported as an arithmetic bound.

### Executed experiment

C++17, `-O3 -Wall -Wextra -Werror`, deterministic xorshift seed `0x4c5b23084f8d5515`:

- Independent arithmetic sieve check: n=1 through 2000 passed.
- Finite arithmetic sign certificate: \(N\le10^7\), zero violations.
- At \(N=10^7\): \(M(N)=1037\), numerical \(C_1(N)\approx-4.50299499784\), \(C_{3/2}(N)\approx-0.547422257531\).
- First positive dyadic block at exponent 1: \(X=4\), increment \(1/105\).
- Randomized model: 4,000 replications, \(N=50,000\), exponent \(3/2\): sample mean \(-0.00910615\), sample variance \(0.30219501\), mathematically predicted variance \(0.30020787\), sample positive fraction \(0.3635\).

The finite computation and null model are diagnostic; neither establishes RH or any arithmetic result for unbounded N.

## Audit verdict / next obligation

**REFUTED:** every dyadic correlation block is negative.

**CERTIFIED FINITE:** every \(C_\alpha(N)\) is negative for \(\alpha\ge1\), \(2\le N\le10^7\).

**PROVED CONDITIONAL:** summability of positive dyadic correlation budgets for fixed \(\alpha>1\) gives a zero-free half-plane \(\Re(s)>\alpha/2\); requiring this for every \(\alpha>1\) is equivalent to RH.

**PROVED FOR A RANDOM MODEL ONLY:** martingale cancellation works across \(1<\alpha<2\).

**OPEN:** establish any fixed-exponent budget for the actual Möbius function without assuming zero-free regions as strong as the desired conclusion.

Prior art: Gordon V. Chavez, *Correlations of the Möbius and Liouville functions with their partial sums*, https://doi.org/10.1142/S1793042126500934. Weak Mertens consequences: https://doi.org/10.1112/blms.13092. No originality or RH proof claim.