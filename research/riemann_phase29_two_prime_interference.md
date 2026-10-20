# Phase XXIX — Exact two-prime interference and rigorous aggregate-sign counterexamples

**Date:** 20 October 2026. **Status:** algebraic identities proved; four nontrivial signs of *infinite* weighted correlations proved using a finite integer-arithmetic certificate and explicit analytic tails; 27 further exact finite checks passed. **The Riemann hypothesis remains open. No originality claim.**

## 1. Notation and convergent range

Write \(\mu\) for the arithmetic Möbius function, \(M(x)=\sum_{n\le x}\mu(n)\). For distinct primes \(p,q\), set
\[
f(x)=F_{p,q}(x)=\sum_{n\le x,\,p\nmid n,\,q\nmid n}\mu(n),\qquad S_df(x)=f(x/d),
\]
with \(f(x)=0\) for \(0\le x<1\). Multiplicativity gives the *pointwise exact* identity
\[
\boxed{M=(I-S_p)(I-S_q)f=f-S_pf-S_qf+S_{pq}f.}\tag{1}
\]
For \(\alpha>2\) define
\[
\langle u,v\rangle_\alpha=\alpha\int_1^\infty u(x)v(x)x^{-\alpha-1}\,dx,
\quad E_\alpha(u)=\langle u,u\rangle_\alpha,
\quad B_{\alpha,d}(u)=\langle u,S_du\rangle_\alpha.
\]
All displayed infinite inner products are absolutely convergent because \(|M(x)|,|f(x)|\le x\). The dilation identity is \(\langle S_du,S_dv\rangle_\alpha=d^{-\alpha}\langle u,v\rangle_\alpha\).

Define the **mixed two-prime interference**
\[
\Gamma_{\alpha;p,q}(f)=\langle f,S_{pq}f\rangle_\alpha+\langle S_pf,S_qf\rangle_\alpha
\]
and the **net non-diagonal interaction**
\[
\Delta_{\alpha;p,q}
=E_\alpha(M)-(1+p^{-\alpha})(1+q^{-\alpha})E_\alpha(f).
\]

## 2. Exact two-prime energy and compatibility ('diamond') formulas

Expand (1) using bilinearity, symmetry, and dilation scaling:
\[
\boxed{\begin{aligned}
E_\alpha(M)={}&(1+p^{-\alpha})(1+q^{-\alpha})E_\alpha(f)\\
&-2(1+q^{-\alpha})B_{\alpha,p}(f)
-2(1+p^{-\alpha})B_{\alpha,q}(f)
+2\Gamma_{\alpha;p,q}(f).
\end{aligned}}\tag{2}
\]
In particular
\[
\boxed{\Delta_{\alpha;p,q}=-2(1+q^{-\alpha})B_{\alpha,p}(f)-2(1+p^{-\alpha})B_{\alpha,q}(f)+2\Gamma_{\alpha;p,q}(f).}\tag{3}
\]
The two possible orders of removing primes give an exact compatibility relation:
\[
\boxed{\begin{aligned}
B_{\alpha,p}((I-S_q)f)&=(1+q^{-\alpha})B_{\alpha,p}(f)-\Gamma_{\alpha;p,q}(f),\\
B_{\alpha,q}((I-S_p)f)&=(1+p^{-\alpha})B_{\alpha,q}(f)-\Gamma_{\alpha;p,q}(f).
\end{aligned}}\tag{4}
\]
These identities are algebraic and do **not** imply a favorable sign for either \(\Gamma\) or \(\Delta\).

**Finite cutoff warning.** When \(\langle\cdot,\cdot\rangle_{\alpha,X}\) integrates only to \(X\), \(\langle S_du,S_dv\rangle_{\alpha,X}=d^{-\alpha}\langle u,v\rangle_{\alpha,X/d}\), not generally \(d^{-\alpha}\langle u,v\rangle_{\alpha,X}\). The full identities (2)–(4) therefore require boundary correction at finite cutoffs; the certificate tests *the exact cutoff-corrected expansions*, not a false same-cutoff formula.

## 3. Rigorous sign certificates for the actual Möbius sequence

**Theorem (exact integer-rational certification at \(\alpha=3\)).** For the genuine Möbius function:
\[
\boxed{\Gamma_{3;2,3}(F_{2,3})>\frac3{100},\qquad
\Gamma_{3;2,7}(F_{2,7})<-\frac1{1000}.}\tag{5}
\]
Furthermore, the **entire combined non-diagonal interaction** has opposite signs for different prime pairs:
\[
\boxed{\Delta_{3;2,3}<-\frac6{25},\qquad
\Delta_{3;3,5}>\frac1{200}.}\tag{6}
\]
Thus a conjecture that the two-prime mixed term or the combined two-prime interference always has one beneficial sign is **false even for the arithmetic Möbius sequence**, safely within the absolutely convergent exponent range.

### Self-contained certification

Take \(K=4096\). Since the summatory functions are constant on \([k,k+1)\), for integer \(\alpha=3\)
\[
\Gamma_{3;p,q}(K)=\sum_{k=1}^{K-1}
\big(k^{-3}-(k+1)^{-3}\big)
\left[f(k)f(\lfloor k/pq\rfloor)+f(\lfloor k/p\rfloor)f(\lfloor k/q\rfloor)\right].\tag{7}
\]
Similarly, set \(A_{p,q}=(1+p^{-3})(1+q^{-3})\) and compute
\[
\Delta_{3;p,q}(K)=\sum_{k=1}^{K-1}
\big(k^{-3}-(k+1)^{-3}\big)
\left[M(k)^2-A_{p,q}f(k)^2\right].\tag{8}
\]
Every summand is rational. The attached Python script computes integer floors and ceilings of each rational term scaled by \(10^{15}\), yielding rigorous lower and upper bounds with rounding error below \((K-1)10^{-15}\). It constructs \(\mu(1),\ldots,\mu(K)\) using a sieve and **independently checks every value by trial division**.

For the tails, the trivial inequalities \(|f(x)|,|M(x)|\le x\) and \(|S_df(x)|\le x/d\) give
\[
\boxed{\left|\Gamma_{3;p,q}-\Gamma_{3;p,q}(K)\right|\le\frac6{pqK},\qquad
\left|\Delta_{3;p,q}-\Delta_{3;p,q}(K)\right|
\le \frac3K(1+A_{p,q}).}\tag{9}
\]
Adding these analytic tails to the integer-rational intervals proves (5)–(6). Selected full **infinite** enclosures (rounded outwards for display) are:

| \((p,q)\) | \(\Gamma_{3;p,q}\) interval | \(\Delta_{3;p,q}\) interval |
|---|---:|---:|
| (2,3) | [0.0325110067, 0.0329992881] | [−0.2439445729, −0.2407707447] |
| (2,7) | [−0.0020018910, −0.0017926275] | [−0.1744817912, −0.1713641936] |
| (3,5) | [0.0026292325, 0.0028245451] | [0.0059739023, 0.0089699962] |

The complete six-pair dataset is in `experiments/riemann_phase29_sign_enclosures.csv`. The precision of the printed decimals is not needed for the proofs: the script compares exact rational endpoints against \(3/100\), \(-1/1000\), \(-6/25\), and \(1/200\).

## 4. Why universal Hilbert-space norm control cannot fix the signs

For arbitrary \(f\in L^2([1,\infty),\alpha x^{-\alpha-1}dx)\), Cauchy–Schwarz yields
\[
\boxed{|\Gamma_{\alpha;p,q}(f)|\le 2(pq)^{-\alpha/2}E_\alpha(f).}\tag{10}
\]
This is an unsigned upper bound. The Mellin-frequency multiplier of \(\Gamma\) is proportional to
\(2(pq)^{-\alpha/2}\cos(t\log p)\cos(t\log q)\), which takes both signs. Therefore positivity cannot be imposed on generic states. The explicit Möbius certificates in Section 3 prove that arithmetic specialization does not restore a universal sign either.

## 5. Executed verification and interpretation

`python3 experiments/riemann_phase29_two_prime.py` was executed locally using Python standard library only and returned:

- independent Möbius trial-division check: **4096/4096 PASS**;
- exact finite-cutoff reconstruction, energy expansion and corrected diamond formulas: **27/27 PASS** (three prime pairs, three integer cutoffs, three exponents);
- four strict **infinite-integral** inequalities in (5)–(6): **4/4 PASS**;
- additional rational intervals for six prime pairs, with analytic tail bounds.

**What is proved:** the two-prime identities, rigorous mixed-sign and net-interaction counterexamples, and Cauchy bound. **What is not proved:** any bound on the aggregate of arbitrarily many prime dilations at fixed \(1<\alpha<2\), any improvement over the standard Mertens-function estimates, or RH. Finite cutoffs at \(\alpha\le2\) give no entitlement to infinite energy convergence. The Prime Number Theorem and RH have not been advanced by these identities.

**Prior art:** This is a finite Euler-factor expansion in a weighted Hilbert space; it is a natural algebraic relative of classical Möbius/Mellin identities and Nyman–Beurling approaches. Relevant examples include Maier–Rassias, *Estimates of sums related to the Nyman–Beurling criterion for the Riemann Hypothesis*, JNT 188 (2018), 96–120, DOI https://doi.org/10.1016/j.jnt.2017.12.012, and Báez-Duarte, *New versions of the Nyman-Beurling criterion for the Riemann hypothesis* (2002), DOI https://doi.org/10.1155/S0161171202013248. These do not establish novelty or priority of the particular identities here.

**Research next step:** Any favorable multi-prime estimate must accommodate both positive and negative signed two-prime interaction terms; a universal sign claim has been falsified. The needed bound must exploit arithmetic correlations that are not contained in abstract dilation norms.