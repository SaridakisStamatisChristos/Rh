# Phase XXVIII — Möbius prime-dilation covariance has both signs

**Date:** 20 October 2026. **Research status:** complete elementary analytic proof with independently executed exact-rational finite certificates and a rigorously bounded infinite tail. The counterexamples refute proposed sign-monotonicity mechanisms; they do **not** establish RH, a new zero-free region, or originality.

## 1. Definitions and the exact one-prime energy identity

Let \(\mu(n)\) be the Möbius function, \(M(x)=\sum_{n\le x}\mu(n)\), and for a prime \(p\) define
\[
F_p(x)=\sum_{\substack{n\le x\\p\nmid n}}\mu(n),\qquad F_p(x)=0\quad(x<1).
\]
Multiplicativity gives the exact pointwise identity
\[
\boxed{M(x)=F_p(x)-F_p(x/p).}
\tag{1}
\]

For \(\alpha>0\) and \(X>1\), put
\[
E_{\alpha,X}(f)=\alpha\int_1^X|f(x)|^2x^{-\alpha-1}\,dx,
\quad J_{p,\alpha}(X)=\alpha\int_1^X F_p(x)F_p(x/p)x^{-\alpha-1}\,dx.
\]
Write \(E_{\alpha,X}(S_pf)\) for the second dilation energy. Expanding (1) gives exactly
\[
\boxed{
E_{\alpha,X}(M)=E_{\alpha,X}(F_p)+E_{\alpha,X}(S_pF_p)-2J_{p,\alpha}(X).
}
\tag{2}
\]
A change of variables gives
\[
E_{\alpha,X}(S_pf)=p^{-\alpha} E_{\alpha,X/p}(f),
\]
where the norm is zero for \(X/p\le1\). This is **not** \(p^{-\alpha}E_{\alpha,X}(f)\) for a finite cutoff. Hence the precise difference is
\[
\boxed{
E_{\alpha,X}(M)-E_{\alpha,X}(F_p)
=p^{-\alpha}E_{\alpha,X/p}(F_p)-2J_{p,\alpha}(X).
}
\tag{3}
\]
In particular the sign of the correlation alone does not decide which energy is larger: the positive dilation-norm term matters.

On integer intervals, write \(w_{\alpha,n}=n^{-\alpha}-(n+1)^{-\alpha}\). Then
\[
\boxed{
J_{p,\alpha}(X)=\sum_{n=1}^{X-1}w_{\alpha,n}
F_p(n)F_p(\lfloor n/p\rfloor)
}
\tag{4}
\]
for integer \(X\ge2\), with \(F_p(0)=0\).

### An independent finite double-sum identity

Substituting the Möbius coefficients and integrating the two indicators gives
\[
\boxed{
J_{p,\alpha}(X)=
\sum_{\substack{m,n\ge1,\ p\nmid mn\\\max(m,pn)<X}}
\mu(m)\mu(n)
\big(\max(m,pn)^{-\alpha}-X^{-\alpha}\big).
}
\tag{5}
\]
The finite double sum is exact for all positive \(\alpha\). The two different expressions (4) and (5) were independently compared using rational arithmetic.

For \(\alpha>2\) the infinite limit exists absolutely and equals
\[
\boxed{
J_{p,\alpha}=\sum_{\substack{m,n\ge1\\p\nmid mn}}
\frac{\mu(m)\mu(n)}{\max(m,pn)^\alpha}.
}
\tag{6}
\]
Absolute convergence follows from counting pairs by their maximum, as the number of pairs of height \(r\) is \(O(r)\).

## 2. Rigorous infinite opposite-sign theorem

**Theorem:** For the *actual* arithmetic Möbius function and \(\alpha=3\),
\[
\boxed{J_{2,3}>0,\quad J_{3,3}<0,\quad J_{5,3}<0.}
\tag{7}
\]

**Proof:** Since \(|F_p(x)|\le x\) for \(x\ge1\), and \(|F_p(x/p)|\le x/p\) for \(x\ge p\),
\[
\begin{aligned}
|J_{p,\alpha}-J_{p,\alpha}(X)|
&\le \frac{\alpha}{p}\int_X^\infty x^{1-\alpha}\,dx\\
&=\boxed{\frac{\alpha}{p(\alpha-2)}X^{2-\alpha}}
\quad(\alpha>2,\ X\ge p).
\end{aligned}
\tag{8}
\]
At \(\alpha=3\) and \(X=1024\), the error is at most \(3/(1024p)\).

The accompanying *exact* Python Fraction certificate, using the independently cross-checked Möbius sieve, proves
\[
J_{2,3}(1024)>\frac9{100}>\frac3{2048},
\]
\[
J_{3,3}(1024)<-\frac1{600}<-\frac1{1024},
\]
\[
J_{5,3}(1024)<-\frac1{250}<-\frac3{5120}.
\]
(These comparisons are strict and use exact integer-rational arithmetic rather than rounded decimals.) Inserting the tail bound proves (7).

For human inspection, exact finite sums and conservative infinite intervals are:

| p | J_(p,3)(1024) approximate | Tail bound | Certified interval for infinite J_(p,3) |
|---:|---:|---:|---|
| 2 | +0.090402684273 | 0.001464843750 | (+0.0889378,+0.0918676) |
| 3 | -0.001979364261 | 0.000976562500 | (-0.0029560,-0.0010028) |
| 5 | -0.004483629290 | 0.000585937500 | (-0.0050696,-0.0038976) |

**Scope:** This is an infinite mathematical sign theorem at \(\alpha=3\), which is **outside** the unsettled \(1<\alpha<2\) strip. Its research role is to **falsify** universal positive or negative cross-prime sign lemmas, even for the true Möbius function. It gives no upper Mertens bound.

## 3. An exact finite energy sign reversal inside the critical strip

For \(\Delta_\alpha(X)=E_{\alpha,X}(M)-E_{\alpha,X}(F_3)\), direct rational evaluation at \(X=32\) yields
\[
\boxed{\Delta_1(32)=
-\frac{65627647919}{3208967842080}<0,}
\tag{9}
\]
\[
\boxed{\Delta_2(32)=
\frac{174590367216324991675973}
{2059494922300714363745280}>0.}
\tag{10}
\]
Since \(\alpha\mapsto\Delta_\alpha(32)\) is a finite sum of continuous functions, the intermediate-value theorem gives **some** \(\alpha_\ast\in(1,2)\) with \(\Delta_{\alpha_\ast}(32)=0\). We do **not** claim uniqueness. Thus prime excision cannot be globally ordered by a fixed energy inequality over all exponents in \([1,2]\), even at this one finite cutoff.

The use of \([1,32]\) is intentional: the finite energy sums run through **n=31**, unlike a max-kernel energy with an additional terminal square term. The certificate checks the exact denominators accordingly.

## 4. Two-prime terms reduce to rational-scale correlations

More generally let \(f\in\mathcal H_\alpha\) be real, and \(S_r f(x)=f(x/r)\) for any real \(r\ge1\). For integers \(1\le d\le e\) (and, in fact, real \(d,e\ge1\)),
\[
\boxed{
\langle S_df,S_ef\rangle_\alpha
=d^{-\alpha}\langle f,S_{e/d}f\rangle_\alpha.
}
\tag{11}
\]
This follows by changing \(x=du\). It exposes the off-diagonal terms in a two-prime inclusion–exclusion:
\[
(I-S_p)(I-S_q)f=f-S_pf-S_qf+S_{pq}f.
\]
All six cross terms can be reduced to (11); they are **not** orthogonal for a generic arithmetic \(f\).

For \(f(x)=\mathbf1_{x\ge1}\), (11) reduces to
\(\langle S_df,S_ef\rangle_\alpha=\max(d,e)^{-\alpha}\).
Expanding the infinite prime product on every finite interval then recovers the same maximum kernel \(Q_\alpha\) from Phases I–XXIII. This identifies the central circularity: an arbitrary estimate that "all cross-prime terms cancel favorably" would have to prove, rather than assume, the original RH-equivalent arithmetic cancellation.

## 5. Evidence and reproducibility

Run \`python3 experiments/riemann_phase28_prime_covariance.py\` using Python 3 standard library (no NumPy/SymPy dependencies).

- Independent integer-factorization cross-check of all Möbius values 1–1024: **1024/1024 PASS**.
- Three exact rational *infinite sign certificates*, with analytic tail bounds for p=2,3,5 at alpha=3: **PASS**.
- Exact finite sign reversal and the two displayed fractions at X=32: **PASS**.
- Exact one-prime reconstruction and energy polarization for p=2,3,5, each at alpha=1,2,3: **9/9 PASS**.
- Independent finite double-sum validation of (5) at X=16,32,64, p=2,3,5, alpha=1,2,3: **27/27 PASS**.

These computational checks supplement the complete proofs (1)–(11). No peer-review, formal proof-assistant, or CI run is claimed.

## 6. Verdict and future proof obligation

**PROVED:** Prime-step covariance energy identity; exact rational finite counterexample to exponent-independent monotonicity; opposite-signed *infinite* correlations for the true Möbius function at alpha=3; rational-scale pairwise-dilation identity.

**NOT PROVED:** A uniform upper bound on the positive Möbius energy \(Q_\alpha(N)\) at fixed \(1<\alpha<2\), a stronger zero-free half-plane, RH, or new methodological superiority. No novelty/priority claim is made: many such identities are classical Hilbert-space polarizations of multiplicative sieves.

**Discriminating next target:** investigate aggregate cross-prime correlations **with quantified cancellation and error rates** instead of imposing a false individual sign assumption. Any unconditional fixed-exponent estimate must go beyond the Euler-product operator norms from Phase XXVII, which are sharp for unrestricted Hilbert-space functions.

## Closest verified related literature

- Maier and Rassias, *Explicit estimates of sums related to the Nyman–Beurling criterion for the Riemann Hypothesis*, Journal of Functional Analysis 276 (2019), 3832–3857. https://www.sciencedirect.com/science/article/pii/S0022123618302544
- Ng, *The distribution of the summatory function of the Möbius function* (2003 preprint), https://arxiv.org/abs/math/0310381
- Classical Kronecker approximation theorem, Dirichlet-series Euler products and Möbius inversion as detailed in Phase XXVII. These are background and **do not** verify originality of the identities here.

**RH remains unsolved.**
