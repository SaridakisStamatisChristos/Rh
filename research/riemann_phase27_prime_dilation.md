# Phase XXVII — Prime-dilation renormalization and the exact Euler-product operator-norm barrier

**Date:** 20 October 2026. **Status:** exact elementary arithmetic and Hilbert-space operator identities; sharp finite-prime operator norms; an asymptotic threshold at exponent 2, based on classical prime-distribution theorems. Executed deterministic tests and exact rational checks. **Not a proof of the Riemann Hypothesis; no novelty/priority claim.**

## 1. Arithmetic definitions

Write \(\mu(n)\) for the Möbius function and \(M(x)=\sum_{n\le x}\mu(n)\), with \(M(x)=0\) for \(x<1\). Let \(P\) be **any finite set of distinct primes**. Define the prime-excised Möbius sum

\[
M_P(x)=\sum_{\substack{n\le x\\ p\nmid n\,\forall p\in P}}\mu(n).
\]

For every integer \(p\ge2\), define dilation \((S_p f)(x)=f(x/p)\), extending each function by zero below 1. Decomposing squarefree integers as \(n=dm\), where \(d\) has its prime factors in \(P\) and \(m\) is coprime to every member of \(P\), gives the *exact* finite arithmetic identity

\[
\boxed{M=\prod_{p\in P}(I-S_p)M_P.}\tag{1}
\]

Each factor commutes. The inverse can be written as a **finite sum when evaluated at a fixed \(x\)**:

\[
\boxed{M_P(x)=\prod_{p\in P}(I-S_p)^{-1}M(x)
=\sum_{\substack{d\ge1\\\text{all prime factors of }d\text{ in }P}}
M(x/d).}\tag{2}
\]

Here \(d\) may contain **prime powers**; this is a sum over \(P\)-smooth integers, not only squarefree divisors. Only \(d\le x\) contribute. For \(P=\{2\}\), (1) reads \(M(x)=M_{\{2\}}(x)-M_{\{2\}}(x/2)\).

## 2. Weighted Hilbert space, including finite truncations

For \(\alpha>0\) define the norm

\[
\|f\|_\alpha^2=\alpha\int_1^\infty |f(x)|^2x^{-\alpha-1}\,dx
\]

on the Hilbert space \(\mathcal H_\alpha=L^2([1,\infty),\alpha x^{-\alpha-1}dx)\). With \(\|\cdot\|_{\alpha,X}\), truncate the integral to \([1,X]\). The norm is defined on all measurable functions, not just arithmetic step functions. A change of variables shows

\[
\boxed{\|S_pf\|_\alpha=p^{-\alpha/2}\|f\|_\alpha,\qquad
\|S_pf\|_{\alpha,X}\le p^{-\alpha/2}\|f\|_{\alpha,X}.}\tag{3}
\]

The full-space equality holds since the extension is zero below 1. As \(\|S_p\|<1\), \(I-S_p\) is invertible by a norm-convergent Neumann series on \(\mathcal H_\alpha\). On each truncated interval \([1,X]\), \(S_p\) is nilpotent (large dilations vanish), so invertibility is elementary as well.

For every finite prime set \(P\), the triangle and reverse-triangle inequalities and their counterparts for the inverse imply

\[
\boxed{\prod_{p\in P}(1-p^{-\alpha/2})\|M_P\|_{\alpha,X}
\le\|M\|_{\alpha,X}
\le\prod_{p\in P}(1+p^{-\alpha/2})\|M_P\|_{\alpha,X}.}\tag{4}
\]

This **finite-truncation statement needs no RH assumption** and holds for any \(X\ge1\) and \(\alpha>0\). The corresponding infinite-space inequalities hold whenever either side is finite; for fixed \(P\), membership of \(M\) and \(M_P\) in \(\mathcal H_\alpha\) is equivalent.

For an arithmetic step function with values \(f(k)\) on \([k,k+1)\), the truncated energy at integer \(X=N\) is exactly

\[
\|f\|_{\alpha,N}^2=\sum_{k=1}^{N-1}
\big(k^{-\alpha}-(k+1)^{-\alpha}\big)|f(k)|^2.
\]

**Important:** This excludes the endpoint term \(N^{-\alpha}M(N)^2\) present in the finite max-kernel quadratic form \(Q_\alpha(N)\). In the infinite limit, finiteness of \(\|M\|_\alpha\) is equivalent to the familiar RH weighted-energy criterion for every \(\alpha>1\), but the two *finite* expressions must not be conflated.

## 3. The constants in (4) are sharp as Hilbert-space operator norms

Define \(A_{P,\alpha}=\prod_{p\in P}(I-S_p)\) on \(\mathcal H_\alpha\). We prove the **exact operator norms**

\[
\boxed{\|A_{P,\alpha}\|=\prod_{p\in P}(1+p^{-\alpha/2}),\qquad
\|A_{P,\alpha}^{-1}\|=\prod_{p\in P}(1-p^{-\alpha/2})^{-1}.}\tag{5}
\]

### Proof of sharpness

Use the isometry \(Uf(u)=\sqrt\alpha\,e^{-\alpha u/2}f(e^u)\) from \(\mathcal H_\alpha\) onto \(L^2([0,\infty),du)\). It converts dilation to a scaled right shift:

\[
(US_pU^{-1}g)(u)=p^{-\alpha/2}g(u-\log p)\mathbf1_{u\ge\log p}.
\]

Let \(g_{R,t}(u)=R^{-1/2}e^{itu}\mathbf1_{[0,R]}(u)\). For each **fixed finite** prime set \(P\) and each real \(t\), away from the bounded-length endpoints of \([0,R]\), the finite linear combination of shifts \(A_{P,\alpha}g_{R,t}\) agrees with

\[
m_P(t)g_{R,t},\qquad m_P(t)=\prod_{p\in P}\big(1-p^{-\alpha/2-it}\big).
\]

Thus \(\|A_{P,\alpha}g_{R,t}-m_P(t)g_{R,t}\|_2\to0\) as \(R\to\infty\), giving \(\|A_{P,\alpha}\|\ge\sup_t|m_P(t)|\). The logarithms of distinct primes are rationally independent, by unique factorization. Kronecker's simultaneous approximation theorem therefore makes the phases \(t\log p\) approach \(\pi\) modulo \(2\pi\) simultaneously for every finite \(P\), giving

\[
\sup_{t\in\mathbb R}|m_P(t)|=\prod_{p\in P}(1+p^{-\alpha/2}).
\]

The opposite bound follows from \(\|I-S_p\|\le1+\|S_p\|\).

For the inverse, \(m_P(0)=\prod(1-p^{-\alpha/2})\). The same approximate-eigenvector construction with \(t=0\) gives
\(\|A_{P,\alpha}^{-1}\|\ge1/m_P(0)\), while Neumann series yield the reverse inequality. This completes (5).

**Scope:** These constants are optimal on the **full function Hilbert space**, not necessarily within the restricted family of actual Möbius summatory functions. Their optimality is an adversarial obstruction to a strategy using *only* abstract dilation operator norms.

## 4. Exact three-regime Euler-product barrier

Take \(P_y=\{p\le y:p\text{ prime}\}\) and denote \(A_y=A_{P_y,\alpha}\). The exact formula (5) gives:

- **\(\alpha>2\):** both products converge, and
  \[
  \boxed{\lim_{y\to\infty}\|A_y^{-1}\|=\zeta(\alpha/2),\quad
  \lim_{y\to\infty}\|A_y\|=\frac{\zeta(\alpha/2)}{\zeta(\alpha)}.}\tag{6}
  \]
  Furthermore \(A_y\) converges in operator norm to an invertible full-prime product, and applying this limit to the constant function \(f_0(x)=1\) gives \(M(x)\) pointwise and in \(\mathcal H_\alpha\).
- **\(\alpha=2\):** Mertens' third theorem and \(\prod_{p\le y}(1+p^{-1})=\prod_{p\le y}(1-p^{-2})\prod_{p\le y}(1-p^{-1})^{-1}\) imply
  \[
  \boxed{\|A_y^{-1}\|\sim e^\gamma\log y,\quad
  \|A_y\|\sim\frac6{\pi^2}e^\gamma\log y.}\tag{7}
  \]
- **\(0<\alpha<2\):** the prime number theorem and partial summation yield
  \[
  \boxed{\log\|A_y^{-1}\|\sim\log\|A_y\|
  \sim\frac{y^{1-\alpha/2}}{(1-\alpha/2)\log y}.}\tag{8}
  \]

These facts prove that one cannot obtain a **uniform-in-\(y\)** estimate in (4) for \(\alpha\le2\) by substituting only the best universal dilation-operator norms; those optimal constants diverge. This does **not** prove that the actual arithmetic \(M\) has divergent energy at these exponents; for example, classical Mertens estimates already establish its finite energy at \(\alpha=2\). Arithmetic cancellations are not represented by the universal operator-norm bound.

## 5. Independent computation

Reproducer: \`python3 experiments/riemann_phase27_prime_dilation.py\` (Python standard library only). Outputs \`experiments/riemann_phase27_energy.csv\` and \`experiments/riemann_phase27_operator_norms.csv\`.

Execution results:

- Independent trial-division Möbius check for integers 1–1,000: **PASS**.
- Seven distinct finite prime sets reconstructed every value of the true Mertens function through \(N=16,384\) by (1): **PASS**.
- Seven rational-energy inequalities at \(\alpha=2,N=256\), using Python \`Fraction\`: **PASS**.
- 28 finite real-exponent energy inequalities at \(N=16,384\) for \(\alpha\in\{1.25,1.5,2,3\}\): **PASS**.
- Exact finite Euler-product constants evaluated for \(y=10,100,1000,10000,100000\) and \(\alpha=1.5,2,2.5,3\); these are **computed products**, while their sharpness as operator norms is proved analytically.

Selected operator norms:

| Prime cutoff \(y\) | \(\alpha\) | \(\|A_y^{-1}\|\) | \(\|A_y\|\) |
|---:|---:|---:|---:|
| 1,000 | 1.5 | 196.308823 | 75.697685 |
| 100,000 | 1.5 | 32,700.634712 | 12,523.545025 |
| 1,000 | 2.0 | 12.350976 | 7.509446 |
| 100,000 | 2.0 | 20.511593 | 12.469563 |
| 100,000 | 2.5 | 4.525657 | 3.373611 |
| 100,000 | 3.0 | 2.611132 | 2.172220 |

As \(y\) grows, the behavior matches the three proved regimes. The finite numbers do not independently prove the asymptotic statements.

## 6. Research verdict / next falsification target

**PROVED:** exact finite-prime reconstruction; quantitative weighted-energy equivalence for each fixed finite \(P\); sharp universal operator constants; precise \(\alpha=2\) Euler-product threshold for abstract prime-by-prime norm arguments.

**NOT PROVED:** a uniform bound for the actual \(M\) energy for every \(1<\alpha<2\); a new zero-free half-plane; RH. No claim that the abstract dilation identities are new in the literature.

**Discriminating future target:** Find and verify a *Möbius-specific* cancellation bound for the prime-dilation cross terms that improves the optimal universal operator-norm estimate. If the argument only combines individual prime-dilation norms by the triangle inequality, (5)–(8) provide a precise barrier at the exponent \(2\). A useful test must exploit arithmetic correlations unavailable to general \(L^2\) functions.

## Sources / prior art

1. Classical Euler product \(1/\zeta(s)=\prod_p(1-p^{-s})\), \(\Re s>1\): https://mathworld.wolfram.com/MoebiusFunction.html
2. Mertens' third theorem (\(\prod_{p\le y}(1-1/p)^{-1}\sim e^\gamma\log y\)): https://mathworld.wolfram.com/MertensTheorem.html ; explicit bounds in *Ramanujan Journal* (2024): https://link.springer.com/article/10.1007/s11139-024-00893-8
3. Dilation/Hilbert-space prior art: Báez-Duarte (2005), *A general strong Nyman–Beurling Criterion for the Riemann Hypothesis*: https://arxiv.org/abs/math/0505453
4. Kronecker approximation theorem and prime-logarithm independence are classical; no priority is claimed for (5).

**Riemann Hypothesis remains unsolved.**