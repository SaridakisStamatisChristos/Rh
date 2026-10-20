# Phase XXVI — Parity-pair energy decomposition and the RH residual barrier

**Date:** 20 October 2026.  **Evidence:** elementary exact proofs, 36 rational-arithmetic matrix checks with 108 exact vectors, and finite sieve diagnostics through \(2^{19}=524288\). **Status:** complementary verification of the existing Phase XXV algebra plus a new explicit two-point residual decomposition; no novelty claim, no new zero-free region, **RH remains open**.

## 1. Definitions

Let \(\mu\) be the classical Möbius function and \(M(x)=\sum_{n\le x}\mu(n)\). Fix \(N\ge3\), \(\alpha>0\). From Phases XIX–XXV:

\[
T_N(k,d)={\bf1}_{d\le k}M(\lfloor k/d\rfloor),\qquad
w_k=\begin{cases}k^{-\alpha}-(k+1)^{-\alpha},&k<N,\\N^{-\alpha},&k=N,\end{cases}
\]
\[
H=T_N^*\operatorname{diag}(w_k)T_N,\qquad
H^{-1}=B\operatorname{diag}(c_k)B^*,\quad
c_k=w_k^{-1},\quad B(d,k)={\bf1}_{k\mid d}-{\bf1}_{k+1\mid d}.
\]

The *primal* form is \(\mathcal Q_{\alpha,N}(a)=\sum_{k\le N}w_k|A(k)|^2\), where \(A(k)=\sum_{n\le k}a_n\), and the divisor transform is \(z_n=\sum_{d\mid n}a_d\). Then \(\mathcal Q=z^*Hz\). The inverse and all matrices in this note use the **actual** arithmetic Möbius function only to define \(T_N\) and invert the divisor transform. No RH assumption is made.

## 2. Independent audit of Phase XXV's weighted-GCD factorization

Let \(\mathcal O_N=\{1,3,5,\ldots\}\cap[1,N]\). Define

\[
b_1=c_1,\qquad b_t=c_{t-1}+c_t\quad (3\le t\le N,\ t\text{ odd}).
\]

**Theorem 25.1.** For any odd \(d,e\le N\),

\[
\boxed{(H^{-1})_{d,e}=\sum_{\substack{t\mid\gcd(d,e)\\t\text{ odd}}}b_t
=c_1+\sum_{\substack{t\mid\gcd(d,e)\\t\ge3}}(c_{t-1}+c_t).}
\tag{1}
\]

Writing \(E(d,t)={\bf1}_{t\mid d}\) for odd \(d,t\), the full odd-coordinate principal block therefore factors exactly:

\[
\boxed{G_{\mathcal O}=E\operatorname{diag}(b_t)E^*,\quad
G_{\mathcal O}^{-1}=E^{-*}\operatorname{diag}(b_t^{-1})E^{-1},\quad
\det G_{\mathcal O}=\prod_{t\in\mathcal O_N}b_t.}
\tag{2}
\]

Here \(E^{-1}(d,t)={\bf1}_{t\mid d}\mu(d/t)\), since the odd integers form a divisor-closed set.

*Proof.* For odd \(d\), the only nonzero terms \(B(d,k)\) are \(B(d,1)=1\), \(B(d,t)=1\) for odd divisors \(t\ge3\) of \(d\), and \(B(d,t-1)=-1\) for those same odd divisors. In particular, the \(t-1\) columns are even and the \(t\) columns are odd, and the sets do not overlap. When taking the weighted inner product of rows \(d,e\), a common odd divisor \(t\ge3\) contributes \(c_{t-1}+c_t\), while \(t=1\) contributes \(c_1\). This proves (1). Equation (2) follows by divisor-incidence factorization and Möbius inversion. \(\square\)

**Correct interpretation:** The rank-one inverse-prime block in Phase XXIV is a corollary, because distinct odd primes share no divisor greater than 1. A rank-one formula does **not** hold for all odd composite pairs. For example, \(\gcd(9,15)=3\) yields \((H^{-1})_{9,15}=c_1+c_2+c_3\). The weighted-GCD form is standard incidence-algebra machinery; no novelty is claimed.

## 3. A sharp Schur-complement bound from the odd indices plus coordinate 2

The already archived Phase XXV odd-only block misses the important divisor coordinate \(z_2\). In particular, its lower bound can be *weaker* than the earlier prime-plus-2 bound, so **it would be incorrect to claim automatic improvement merely from including all odd indices**.

Define \(\mathcal R_N=\{2\}\cup\mathcal O_N\), let \(G_{\mathcal R}\) be the principal block of \(H^{-1}\), and let \(z_{\mathcal R}\) be the corresponding divisor data. Define, for odd \(t\ge5\),

\[
a_t=\sum_{d\mid t}\mu(t/d)z_d,
\]

which equals the original coefficient \(a_t\) by Möbius inversion. The \(\mathcal R_N\)-restricted inverse form is exactly

\[
\begin{aligned}
v^*G_{\mathcal R}v={}&c_1\left|\sum_{d\in\mathcal O_N}v_d\right|^2
+c_2\left|v_2-\sum_{3\mid d,\ d\in\mathcal O_N}v_d\right|^2\\
&+c_3\left|\sum_{3\mid d,\ d\in\mathcal O_N}v_d\right|^2
+\sum_{\substack{5\le t\le N\\t\text{ odd}}}
(c_{t-1}+c_t)\left|\sum_{t\mid d,\ d\in\mathcal O_N}v_d\right|^2.
\end{aligned}
\tag{3}
\]

This triangular change of coordinates can be inverted without estimation. Its inverse quadratic form is

\[
\boxed{
\begin{aligned}
z_{\mathcal R}^*G_{\mathcal R}^{-1}z_{\mathcal R}
={}&w_1|z_1|^2+w_2|z_2|^2
+w_3|z_2+z_3-z_1|^2\\
&+\sum_{\substack{5\le t\le N\\t\text{ odd}}}
\frac{|a_t|^2}{c_{t-1}+c_t}.
\end{aligned}}
\tag{4}
\]

The standard Schur complement / minimum-energy principle for positive definite matrices implies the sharp interpolation inequality

\[
\boxed{\mathcal Q_{\alpha,N}(a)\ge z_{\mathcal R}^*G_{\mathcal R}^{-1}z_{\mathcal R}.}
\tag{5}
\]

The adjective *sharp* means the bound is the exact minimum of \(z^*Hz\) over **unconstrained** omitted divisor coordinates when the \(\mathcal R\)-coordinates are fixed. It is not a sharp estimate on the **arithmetic Möbius sequence**, whose omitted coordinates are not free.

## 4. De-mystification: exact parity matching, not new Möbius cancellation

Write \(A_k=A(k)\), \(a_k=A_k-A_{k-1}\). For every odd \(t\ge5\), complete the square:

\[
\boxed{
 w_{t-1}|A_{t-1}|^2+w_t|A_t|^2
 =\frac{|a_t|^2}{c_{t-1}+c_t}
 +\frac{|w_{t-1}A_{t-1}+w_tA_t|^2}{w_{t-1}+w_t}.}
\tag{6}
\]

The index pairs \((4,5),(6,7),(8,9),\ldots\) are disjoint. Consequently, for all \(N\ge3\),

\[
\boxed{\mathcal Q_{\alpha,N}(a)=\mathcal L_{\alpha,N}(a)+\mathcal R_{\alpha,N}(a),}\tag{7}
\]

where

\[
\begin{aligned}
\mathcal L_{\alpha,N}(a)
={}&w_1|A_1|^2+w_2|A_2|^2+w_3|A_3|^2\\
&+\sum_{\substack{5\le t\le N\\t\text{ odd}}}
\frac{|a_t|^2}{c_{t-1}+c_t}
\end{aligned}
\tag{8}
\]

and the **nonnegative residual** is

\[
\boxed{\mathcal R_{\alpha,N}(a)
=\sum_{\substack{5\le t\le N\\t\text{ odd}}}
\frac{|w_{t-1}A_{t-1}+w_tA_t|^2}{w_{t-1}+w_t}
+\mathbf1_{2\mid N}\,w_N|A_N|^2.}
\tag{9}
\]

The first three prefixes \(A_1=z_1\), \(A_2=z_2\), \(A_3=z_2+z_3-z_1\), and (8) coincides exactly with (4). Hence the elaborate-looking Schur complement (5) has a simple two-point energy decomposition. Crucially, this needs **no multiplicativity, no Möbius signs, and no prime distribution theorem**; it holds for arbitrary complex sequences \(a\). It does not create a new cancellation estimate.

## 5. Exact implication for the actual Möbius function and the RH gap

For \(a_n=\mu(n)\), \(A_k=M(k)\). For \(N\ge3\), \(A_1=1,A_2=0,A_3=-1\), so

\[
\boxed{\mathcal L_{\alpha,N}(\mu)=w_1+w_3+
\sum_{\substack{5\le t\le N\\t\text{ odd}}}
\mu(t)^2\frac{w_{t-1}w_t}{w_{t-1}+w_t}.}
\tag{10}
\]

This improves the Phase XXIV prime-plus-2 lower bound by adding the nonnegative contributions of odd squarefree composites. For every fixed \(\alpha>0\), \(\sup_N\mathcal L_{\alpha,N}(\mu)<\infty\): away from a possible terminal odd index, \(w_t\ll_\alpha t^{-\alpha-1}\), while the exceptional terminal weight is at most \(N^{-\alpha}\). In fact \(\mathcal L_{\alpha,N}(\mu)\) converges to a finite limit as \(N\to\infty\).

It follows from (7), with the classical RH-equivalent positive-energy criterion from Phases I–XIX, that

\[
\boxed{\mathrm{RH}\iff
\text{for every fixed }\alpha>1,\quad
\sup_{N\ge3}\mathcal R_{\alpha,N}(\mu)<\infty.}
\tag{11}
\]

This is **only a reformulation**: the residual contains weighted squared averages of consecutive Mertens values. No uniform bound on it for fixed \(1<\alpha<2\) has been established. Restricting attention to the prime/odd inverse blocks gives only *lower* bounds for the primal energy.

## 6. Executed tests and numerical diagnostics

Reproducer: \`python3 experiments/riemann_phase26_parity_residual.py\` (Python standard library only).

- **36 exact matrix cases:** \(N\in\{3,4,5,8,9,10,11,16,20,21,24,31\}\), \(\alpha\in\{1,2,3\}\).
- **108 additional exact rational vectors:** verified the full energy, the exact Schur lower bound, the parity-local term, and residual identity.
- Verified \(T_NB_N=B_NT_N=I\), the full odd-index weighted-GCD factorization, its inverse via odd Möbius inversion, and the enhanced \(\{2\}\cup\mathcal O_N\) inverse-block Schur complement. All tests **PASS**.
- A separate linear Möbius sieve computed finite \(\mu,M\) data through \(N=524288\) and evaluated the true energy, the earlier prime lower bound, the new bound, and the residual.

| N | α | Q(μ) | Earlier prime lower | New odd+2 lower | Residual | Residual / Q |
|---:|---:|---:|---:|---:|---:|---:|
| 524288 | 1.25 | 1.232970991663 | 0.689705728847 | 0.693232510826 | 0.539738480836 | 43.775% |
| 524288 | 1.50 | 1.077940603923 | 0.738390715992 | 0.740239877429 | 0.337700726494 | 31.328% |
| 524288 | 2.00 | 0.959013501984 | 0.811239265586 | 0.811756174174 | 0.147257327810 | 15.355% |

These finite observations do not establish an all-\(N\) bound for the residual, any improvement to a zeta zero-free region, or RH.

## 7. Prior art and research next step

Weighted-GCD/meet-matrix incidence factorizations are a longstanding subject, not an original general approach; see:

- *On the positive definiteness and eigenvalues of meet and join matrices*, Discrete Mathematics (2014), DOI https://doi.org/10.1016/j.disc.2014.02.018.
- Haukkanen, Wang and Sillanpää, *On Smith's determinant*, Linear Algebra and its Applications 258 (1997), https://doi.org/10.1016/S0024-3795(96)00192-9.
- Phases XXIV–XXV: \`research/riemann_phase24_prime_dual.md\` and \`research/riemann_phase25_odd_divisor.md\`, which already prove the prime and odd-index inverse-Gram identities. Phase XXVI adds an independent parity-residual audit and longer finite Möbius diagnostics.

**Proof audit verdict:** all new algebraic identities here are elementary and independently testable, but the final matching identity shows that the apparent arithmetic complexity is a consequence of index parity, not a new restriction on Möbius correlations. The next viable research task must produce a *new upper bound* for the residual in (9), not another lower frame bound or finite spectral stabilization. Novelty unverified. **RH unsolved.**
