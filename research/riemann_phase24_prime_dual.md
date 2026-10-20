# Phase XXIV — Prime-indexed dual Gram blocks and an exact interpolation inequality

**Date:** 20 October 2026. **Status:** Exact finite-dimensional algebraic theorems, 15 independently executed rational-arithmetic cases, separate floating-point diagnostics. **No RH proof, new zero-free region, or novelty claim.**

## 1. Operators, inverse, and exceptional prime supports

As in Phases XIX–XXIII, let \(\mu\) be the Möbius function, \(M(x)=\sum_{n\le x}\mu(n)\), and for each \(\alpha>0\), \(N\ge3\) define
\[
w_{\alpha,k}=\begin{cases}k^{-\alpha}-(k+1)^{-\alpha},&k<N,\\N^{-\alpha},&k=N,\end{cases}
\quad c_k=w_{\alpha,k}^{-1}>0.
\]
The sieve-to-prefix Gram matrix \(H_{\alpha,N}=T_N^*W_{\alpha,N}T_N\) is positive definite. The previously proved exact inverse identity is
\[
H_{\alpha,N}^{-1}=B_NW_{\alpha,N}^{-1}B_N^*,\qquad
B_N(d,k)=\mathbf1_{k\mid d}-\mathbf1_{k+1\mid d}.
\tag{1}
\]
Let \(\mathcal P_N=\{p:3\le p\le N,\ p\text{ an odd prime}\}\).

For an odd prime \(p\), since its only divisors are \(1,p\), row \(p\) of \(B_N\) is supported at \(k=1,p-1,p\) with values \(+1,-1,+1\), respectively. For *distinct* odd primes \(p,q\), these supports intersect only at \(k=1\). There are no consecutive odd primes; possible equalities \(p=q-1\) or \(p-1=q\) are excluded.

Thus, setting \(d_p=c_{p-1}+c_p\), the prime-indexed principal submatrix of the **inverse Gram matrix** obeys
\[
\boxed{
G_{\alpha,N}:=(H_{\alpha,N}^{-1})_{\mathcal P_N,\mathcal P_N}
=\operatorname{diag}(d_p)_{p\in\mathcal P_N}
+c_1\mathbf1\mathbf1^*.}
\tag{2}
\]
In particular, for \(p\ne q\) odd primes the off-diagonal entry is *exactly* \(c_1=1/(1-2^{-\alpha})\), independently of \(N\) once both primes are present.

### Composite counterexample

The same conclusion fails for general odd numbers: at \(N\ge15\),
\[
\boxed{(H_{\alpha,N}^{-1})_{9,15}=c_1+c_2+c_3>c_1.}
\]
Rows 9 and 15 overlap at \(k=1,2,3\) with matching signs. Hence prime support, not mere oddness, is essential to this rank-one structure.

## 2. The normalized prime block is uniformly well conditioned

Let \(D=\operatorname{diag}(d_p)\), \(s_p=d_p^{-1/2}\). The diagonally normalized inverse-prime block is
\[
\boxed{D^{-1/2}G_{\alpha,N}D^{-1/2}=I+c_1ss^*.}
\tag{3}
\]
It has exactly one potentially non-unit eigenvalue,
\[
\boxed{\Lambda_{\alpha,N}=1+c_1\sum_{p\in\mathcal P_N}d_p^{-1},}
\tag{4}
\]
and all remaining eigenvalues are precisely \(1\). The statement includes \(|\mathcal P_N|=1\), when there are no remaining eigenvalues.

Since \(w_{\alpha,p-1}\le\alpha(p-1)^{-\alpha-1}\) by the mean-value theorem,
\[
d_p=c_{p-1}+c_p\ge c_{p-1}\ge (p-1)^{\alpha+1}/\alpha,
\qquad
\sum_{p\in\mathcal P_N}d_p^{-1}
\le\alpha\sum_{m=2}^\infty m^{-\alpha-1}
=\alpha[\zeta(\alpha+1)-1].
\]
Therefore, for *every fixed* \(\alpha>0\) and *every* \(N\ge3\),
\[
\boxed{1\le\Lambda_{\alpha,N}
\le 1+\frac{\alpha[\zeta(\alpha+1)-1]}{1-2^{-\alpha}}.}
\tag{5}
\]
The diagonal preconditioning constants are independent of matrix size, even at \(\alpha=1\). For any vector \(v\) supported on odd-prime coordinates,
\[
\boxed{
\sum_pd_p|v_p|^2
\le v^*H_{\alpha,N}^{-1}v
\le \left(1+\frac{\alpha[\zeta(\alpha+1)-1]}{1-2^{-\alpha}}\right)
\sum_pd_p|v_p|^2.}
\tag{6}
\]
This bounds a **restricted inverse-operator subspace only**, not \(\|H_{\alpha,N}\|\) itself; it does not resolve RH.

## 3. Exact Schur complement and a prime-coordinate energy lower bound

The exceptional prime 2 has inverse row \(B_N(2,2)=1\) and all other entries zero. The prime 3 additionally satisfies \(B_N(3,2)=-1\). Include the finite index set
\[
R_N=\{1,2\}\cup\mathcal P_N=\{1,2,3,5,7,\ldots\}\cap[1,N].
\]
For \(v\) supported on \(R_N\), (1) gives the **exact** dual form
\[
\begin{split}
v^*H_{\alpha,N}^{-1}v
={}&c_1\big|v_1+\sum_{p\in\mathcal P_N}v_p\big|^2
+c_2|v_2-v_3|^2+c_3|v_3|^2\\
&+\sum_{\substack{p\in\mathcal P_N\\p\ge5}}
(c_{p-1}+c_p)|v_p|^2.
\end{split}
\tag{7}
\]
This is a diagonal quadratic form after the triangular change of variables
\[
u=v_1+\sum_{p\in\mathcal P_N}v_p,\quad
t=v_2-v_3,\quad r=v_3,\quad r_p=v_p\ (p\ge5).
\]
Its positive-definite inverse, on the restricted coordinate space \(R_N\), consequently satisfies for \(z_R=(z_d)_{d\in R_N}\),
\[
\boxed{
z_R^*[(H_{\alpha,N}^{-1})_{R_N,R_N}]^{-1}z_R
=w_{\alpha,1}|z_1|^2+
w_{\alpha,2}|z_2|^2+
w_{\alpha,3}|z_2+z_3-z_1|^2+
\sum_{\substack{p\in\mathcal P_N\\p\ge5}}
\frac{|z_p-z_1|^2}{c_{p-1}+c_p}.}
\tag{8}
\]

**Unconditional interpolation lower bound:** For any vector \(a\in\mathbb C^N\), let \(z_n=\sum_{d\mid n}a_d\). By the Schur-complement/minimum-energy principle for positive definite matrices,
\[
\boxed{\mathcal Q_{\alpha,N}(a)=z^*H_{\alpha,N}z\ \ge\ \text{right-hand side of (8)}.}
\tag{9}
\]
It is valid for all \(N\ge3\), all \(\alpha>0\) and all real or complex coefficients. It is exact as the **best possible lower bound depending solely on the specified \(z_R\)**, because equality is attained after optimizing the unconstrained coordinates \(z_{R^c}\).

In particular, for \(a_n=\mu(n)\), the divisor transform is \(z_1=1,z_n=0\) for \(n>1\), so
\[
\boxed{
Q_\alpha(N;\mu)\ge w_{\alpha,1}+w_{\alpha,3}
+\sum_{\substack{p\le N\\p\ge5\text{ prime}}}
\frac{w_{\alpha,p-1}w_{\alpha,p}}{w_{\alpha,p-1}+w_{\alpha,p}}.}
\tag{10}
\]
The right side is a **positive lower bound**, with a convergent prime correction of order \(p^{-\alpha-1}\) for fixed \(\alpha>0\). It is not the upper bound needed to prove RH. At \(N=3\) it is an equality; for larger \(N\) it is generally strict.

### Why this does NOT settle RH

The RH-equivalent target is an *upper* bound on the primal energy \(Q_\alpha(N;\mu)=e_1^*H_{\alpha,N}e_1\) or \(\|H_{\alpha,N}\|\) at every fixed \(\alpha>1\). Equations (5)–(10) only bound a diagonally preconditioned submatrix of **\(H^{-1}\)** or produce lower bounds on **\(H\)**. There is no legitimate implication from the restricted inverse block being well conditioned to uniform boundedness of the full primal operator. The first divisor coordinate and composite-coordinate interactions remain uncontrolled in the required direction.

## 4. Independent execution

Script: \`experiments/riemann_phase24_prime_dual.py\`.

- Python 3 \`fractions.Fraction\` verified all odd-prime-pair entries, the \(\{1,2\}\cup\)odd-prime restricted inverse and explicit Schur complement, and \(z^*Hz\ge\) (8), at \((N,\alpha)\in\{3,5,8,12,18\}\times\{1,2,3\}\): **15/15 exact cases PASS**.
- Independently verified the composite counterexample \((9,15)\): **PASS**.
- Printed diagonal-normalized nonunit eigenvalue \(\Lambda_{\alpha,N}\) from its exact rank-one formula at \(N=31,127,509,1021\) and \(\alpha=1,1.5,2\) (12 numerical reports, with a conservative rigorous integral-test upper bound for the finite-zeta-series approximation).

Examples:

| \(N\) | \(\alpha\) | \(\Lambda_{\alpha,N}\) |
|---:|---:|---:|
| 31 | 1.00 | 1.1970917729 |
| 1021 | 1.00 | 1.2021252686 |
| 31 | 1.50 | 1.1107896137 |
| 1021 | 1.50 | 1.1114344758 |
| 31 | 2.00 | 1.0647617513 |
| 1021 | 2.00 | 1.0648484298 |

The displayed decimals are not interval-certified, while the underlying structural identities have elementary exact proofs.

## 5. Related literature, integrity and next research question

Incidence-algebra and Hilbert-space RH reformulations are extensively studied; see:
- Bhaskar Bagchi, *On Nyman, Beurling and Báez-Duarte's Hilbert space reformulation of the Riemann hypothesis* (2006), https://arxiv.org/abs/math/0607733.
- Luis Báez-Duarte, *Arithmetical Aspects of Beurling's Real Variable Reformulation of the Riemann Hypothesis* (2000), https://arxiv.org/abs/math/0011254.
- Brevig et al., *The multiplicative Hilbert matrix*, Adv. Math. 302 (2016), https://doi.org/10.1016/j.aim.2016.07.019.

These works are related background, not proof of exact priority for (2)–(10). **Novelty has not been established.**

**Next falsifiable target:** Identify another family of divisor-coordinate supports whose overlaps admit similarly explicit, uniformly normalized inverse Gram bounds, *and then determine whether those can supply upper rather than lower control on the primal first-column energy*. Avoid inferring RH from restricted inverse coercivity.

**Verdict: Structural exact results; no RH proof, no new zero-free half-plane.**
