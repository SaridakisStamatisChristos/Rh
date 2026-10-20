# Phase XXVIII — Cross-prime energy signs: exact Möbius counterexamples and Mellin localization

**Date:** 20 October 2026. **Evidence:** elementary exact formulas plus a reproducible rigorous integer-arithmetic certificate and infinite-tail bound, verified locally. **RH remains unsolved; no priority/novelty claim.**

## 1. Arithmetic setup and exact energy identity

Let \(\mu\) be the true arithmetic Möbius function, and for a prime \(p\) put
\[
b_p(n)=\mu(n)\mathbf1_{p\nmid n},\quad
F_p(x)=\sum_{n\le x}b_p(n),\quad
S_pf(x)=f(x/p)
\]
where \(f(y)=0\) for \(y<1\). By multiplicativity, \(M=F_p-S_pF_p\) at every real \(x\ge1\).

For any \(\alpha>2\), define
\[
E_\alpha(f)=\alpha\int_1^\infty f(x)^2x^{-\alpha-1}dx,\qquad
B_{\alpha,p}=\alpha\int_1^\infty F_p(x)F_p(x/p)x^{-\alpha-1}dx.
\]
All integrals converge absolutely from \(|F_p(x)|\le x\). The dilation isometry gives \(E_\alpha(S_pf)=p^{-\alpha}E_\alpha(f)\). Expanding the square yields the exact identity
\[
\boxed{E_\alpha(M)=(1+p^{-\alpha})E_\alpha(F_p)-2B_{\alpha,p}.}
\tag{1}
\]
The cross term need not be positive. The sign determines whether prime removal decreases or increases the reconstructed energy relative to the sum of the squared components.

For a finite cutoff \(X\ge1\), put
\[
E_{\alpha,X}(f)=\alpha\int_1^Xf(x)^2x^{-\alpha-1}dx,\quad
B_{\alpha,p}(X)=\alpha\int_1^XF_p(x)F_p(x/p)x^{-\alpha-1}dx.
\]
The identity holds with \(E_{\alpha,X/p}\) in the dilated term:
\[
\boxed{E_{\alpha,X}(M)=E_{\alpha,X}(F_p)+
p^{-\alpha}E_{\alpha,X/p}(F_p)-2B_{\alpha,p}(X).}
\tag{2}
\]
Define the energy as zero when the upper integration limit is less than 1. **Do not substitute \(E_{\alpha,X}(F_p)\) for the \(X/p\) cutoff.**

For integer \(K\ge2\), the correlation is an exact finite rational sum when \(\alpha\) is a positive integer:
\[
\boxed{
B_{\alpha,p}(K)=
\sum_{k=1}^{K-1}
\big(k^{-\alpha}-(k+1)^{-\alpha}\big)
F_p(k)F_p(\lfloor k/p\rfloor).
}
\tag{3}
\]
Equivalently, upon expanding \(F_p\),
\[
\boxed{
B_{\alpha,p}(K)=
\sum_{m\le K}\sum_{n\le K/p}
b_p(m)b_p(n)
\left(\max(m,pn)^{-\alpha}-K^{-\alpha}\right).
}
\tag{4}
\]
Both identities were cross-checked in exact \`fractions.Fraction\` arithmetic.

## 2. New falsification certificate: opposite signs at the same exponent

**Explicit theorem (computer-assisted exact finite certificate plus elementary infinite-tail estimate).**
For actual \(\mu\), at \(\alpha=3\),
\[
\boxed{
B_{3,2}>\frac2{25},\qquad
B_{3,3}<-\frac1{1000},\qquad
B_{3,5}<-\frac3{1000}.
}
\tag{5}
\]
These are statements about the full **infinite integrals**. They refute any universal claim that the prime-removal cross correlations are nonnegative at all primes.

### How to reproduce and independently audit the proof

The companion script \`experiments/riemann_phase28_cross_prime.py\` constructs \(\mu(n)\) via a prime sieve and independently verifies every \(n\le1024\) by trial division. It uses only exact integer arithmetic to enclose every summand of (3) at \(K=1024\), exponent 3, by floor/ceiling rounding after multiplication by \(10^{16}\). The summed rounding interval has width at most \(1023\cdot 10^{-16}\).

For any \(x\ge1\), \(|F_p(x)|\le x\) and \(|F_p(x/p)|\le x/p\). Consequently,
\[
\boxed{
|B_{3,p}-B_{3,p}(K)|\le
3\int_K^\infty\frac{x^2/p}{x^4}dx
=\frac3{pK}.
}
\tag{6}
\]
The certificate's resulting *rigorous rational enclosures*, displayed approximately, are:

| \(p\) | Full lower bound | Full upper bound |
|---:|---:|---:|
| 2 | +0.088937840523 | +0.091867528024 |
| 3 | −0.002955926762 | −0.001002801761 |
| 5 | −0.005069566790 | −0.003897691789 |

In particular these intervals prove (5), with no hypothesis on zeta zeros. The decimals are displays of exact rational enclosures, not floating-point proof.

The sign difference is **arithmetically genuine**: \(F_2,F_3,F_5\) are the partial sums of \(\mu(n)\) with one prime's multiples excised, not arbitrary surrogate sequences.

### A finite counterexample inside the RH-relevant exponent region

The same exact rounding procedure, without any assertion about an infinite tail, finds for \(K=512\), exponent \(\alpha=1\):
\[
\boxed{B_{1,2}(512)>1,\qquad B_{1,107}(512)<-1/1000.}
\tag{7}
\]
(The displayed finite value for the second correlation is approximately \(-0.004212577651\).)
This **falsifies universal nonnegativity at finite cutoffs even at \(\alpha=1\)**. Because a simple absolute-value tail bound is not summable there, it gives no global sign statement at that exponent and no new implication for RH.

## 3. Mellin–Plancherel representation: why the sign is not universal

Fix \(\alpha>2\), write \(\sigma=\alpha/2>1\), and let
\[
F_p(s)=\sum_{\substack{n\ge1\\p\nmid n}}\frac{\mu(n)}{n^s}
=\frac{1}{\zeta(s)(1-p^{-s})}
\qquad(\Re s>1).
\]
For \(f=F_p(\cdot)\) as a summatory function, Mellin integration by parts gives
\[
\int_1^\infty f(x)x^{-s-1}dx=\frac{F_p(s)}s.
\]
Changing variables \(u=\log x\) and applying Fourier/Plancherel gives
\[
\boxed{
B_{\alpha,p}
=
\frac{\alpha p^{-\sigma}}{2\pi}
\int_{-\infty}^{\infty}
\cos(t\log p)
\frac{|F_p(\sigma+it)|^2}{|\sigma+it|^2}\,dt.
}
\tag{8}
\]
The Dirichlet series is absolutely convergent at \(\sigma>1\), and the displayed integral is absolutely convergent. **The cosine changes sign.** Without additional control of the arithmetic spectral distribution, no positivity follows from the nonnegative modulus-square factor.

More generally, for finite prime sets \(P\) and \(\alpha>2\),
\[
E_\alpha(M)=\frac{\alpha}{2\pi}
\int_{\mathbb R}\frac{|F_P(\sigma+it)|^2}{|\sigma+it|^2}
\prod_{p\in P}|1-p^{-\sigma-it}|^2\,dt,
\]
where \(F_P(s)=\zeta(s)^{-1}\prod_{p\in P}(1-p^{-s})^{-1}\). This exact spectral expression exposes frequency-dependent phase interactions, but algebraically collapses to the known formula for \(1/\zeta\). It is not new cancellation.

## 4. Evidentiary boundary and the next genuine challenge

**Proved:** equations (1)–(4), (6), (8), and the signed infinite certificates (5), contingent only on correct execution of the fully supplied deterministic integer certificate (independently executable). The finite \(\alpha=1\) examples (7) are also exact.

**Refuted:** a universal nonnegative cross-prime correlation assertion, even when evaluated on actual Möbius coefficients. An approach requiring \(B_{\alpha,p}\ge0\) for all primes is therefore invalid.

**Not proved:** uniform bounds for \(1<\alpha<2\), an improved zeta zero-free region, RH, or originality. The full Mellin representation above is safely justified for \(\alpha>2\); using it at \(1<\alpha<2\) would require precisely the still-unproved weighted-energy convergence. Do not extend (8) across the critical boundary without additional independent proof.

The remaining target is a **signed multi-prime estimate** that bounds the *combined* correlations, accounting for individually negative terms, without circular use of RH-equivalent energy bounds.

### Sources and prior-art context

- Gordon V. Chavez, *Correlations of the Möbius and Liouville functions with their partial sums* (International Journal of Number Theory, May 2026): https://doi.org/10.1142/S1793042126500934. Related but not identical weighting/correlation.
- Mellin Parseval–Plancherel theorem: e.g. London Mathematical Society Newsletter 474 (2018), https://www.lms.ac.uk/sites/lms.ac.uk/files/Publications/newsletter/201801.pdf.
- Earlier phases in this repository, especially XXVII (prime-dilation decomposition).

**Research integrity:** Computer-certified exact rational inequality, with analytic tail, is stronger than a finite floating-point observation, but does not amount to novelty, a general cross-prime sign theorem, or an RH solution.
