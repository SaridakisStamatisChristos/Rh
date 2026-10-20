# Phase XXV — Weighted-GCD structure of the odd inverse-Gram block

**Date:** 20 October 2026. **Evidence state:** elementary factorization and Schur inequalities proved; 24 independent exact rational test cases and 16 finite spectral diagnostics executed locally. **No RH proof, no newly established zero-free region, no originality/priority claim.** Research extends Phase XXIV from odd primes to all odd integers including composites.

## 1. Definitions

Use the notation of Phases XIX–XXIV. For a cutoff \(N\ge3\) and \(\alpha>0\), let
\[
w_{\alpha,k}=k^{-\alpha}-(k+1)^{-\alpha}\ (k<N),\qquad
w_{\alpha,N}=N^{-\alpha},\qquad c_k=w_{\alpha,k}^{-1}.
\]
The original transfer matrix \(T_N(k,d)=\mathbf1_{d\le k}M(\lfloor k/d\rfloor)\) has Möbius-free inverse
\[
B_N(d,k)=(T_N^{-1})(d,k)=\mathbf1_{k\mid d}-\mathbf1_{k+1\mid d}.
\]
Its positive-definite primal energy Gram matrix \(H_{\alpha,N}=T_N^*W_{\alpha,N}T_N\) satisfies
\[
H_{\alpha,N}^{-1}=B_N\operatorname{diag}(c_k)B_N^*.
\]

For odd \(r\le N\), put
\[
\gamma_1=c_1,\qquad \gamma_r=c_{r-1}+c_r\quad(r\ge3,\ r\text{ odd}).
\]
Let \(\mathcal O_N=\{1,3,5,\dots\}\cap[1,N]\) and \(L(d,r)=\mathbf1_{r\mid d}\) on these odd indices.

## 2. Exact weighted-gcd factorization (PROVED)

For odd \(d\), row \(d\) of \(B_N\) has:
- a \(+1\) at \(k=1\);
- for each odd divisor \(r\mid d\), \(r\ge3\), a \(+1\) at \(k=r\) and a \(-1\) at \(k=r-1\);
- zeros elsewhere.

The support pairs \((r-1,r)\), \(r\ge3\) odd, are mutually disjoint. Two rows corresponding to odd \(d,e\) therefore overlap at the divisor \(r=1\), and at each odd common divisor \(r\ge3\), contributing \(\gamma_r=c_{r-1}+c_r\). Hence
\[
\boxed{
G_{\mathrm{odd}}(d,e):=(H_{\alpha,N}^{-1})_{d,e}
=\sum_{\substack{r\mid\gcd(d,e)\\ r\ \mathrm{odd}}}\gamma_r,
\qquad
G_{\mathrm{odd}}=L\operatorname{diag}(\gamma_r)L^*.}
\tag{1}
\]
The incidence matrix \(L\) is lower triangular with diagonal 1, so \(G_{\mathrm{odd}}\) is positive definite and
\[
\boxed{\det G_{\mathrm{odd}}=\prod_{r\in\mathcal O_N}\gamma_r.}
\tag{2}
\]

Since \(L^{-1}(d,r)=\mathbf1_{r\mid d}\mu(d/r)\) for odd indices, the block inverse is
\[
\boxed{
G_{\mathrm{odd}}^{-1}
=L^{-*}\operatorname{diag}(\gamma_r^{-1})L^{-1}.
}
\tag{3}
\]
The odd-prime rank-one-plus-diagonal formula of Phase XXIV is the restriction of (1) to \(d,e\) odd primes.

### Related prior art

Weighted gcd kernels and incidence factorizations are classical. Jeffrey S. Ovall, *An analysis of GCD and LCM matrices via the LDL^T-factorization*, Electronic Journal of Linear Algebra 11 (2004), DOI https://doi.org/10.13001/1081-3810.1121. No claim that (1)–(3) are previously unknown.

## 3. Uniform diagonal normalization for every fixed alpha>1 (PROVED)

Set \(s=(\alpha+1)/2>1\). Define the positive diagonal \(D=\operatorname{diag}(\gamma_r)_{r\in\mathcal O_N}\). For \(r\ge3\) odd, the mean-value theorem implies
\[
\frac{(r-1)^{\alpha+1}}{\alpha}
\le c_{r-1}\le\frac{r^{\alpha+1}}{\alpha}.
\]
For \(r<N\), \(c_r\le(r+1)^{\alpha+1}/\alpha\); for terminal \(r=N\), \(c_N=N^\alpha\le r^{\alpha+1}/3\) because \(r\ge3\). Consequently, with
\[
k_\alpha=\min\left\{
\frac{(2/3)^{\alpha+1}}{\alpha},\ \frac1{1-2^{-\alpha}}
\right\},\qquad
K_\alpha=\max\left\{
\frac{1+(4/3)^{\alpha+1}}{\alpha}+\frac13,\
\frac1{1-2^{-\alpha}}
\right\},
\]
we have, for all odd \(r\le N\),
\[
\boxed{k_\alpha r^{\alpha+1}\le\gamma_r\le K_\alpha r^{\alpha+1}.}
\tag{4}
\]

Put \(A=D^{-1/2}LD^{1/2}\). Each entry satisfies
\[
|A(d,r)|=\mathbf1_{r\mid d}\sqrt{\gamma_r/\gamma_d}
\le \sqrt{K_\alpha/k_\alpha}\,
\mathbf1_{r\mid d}(r/d)^s.
\]
Writing \(d=mr\), the right side is dominated by a weighted sum of integer dilation operators \(S_mx(d)=\mathbf1_{m\mid d}x(d/m)\), each of \(\ell^2\)-operator norm at most 1. Therefore
\[
\|A\|\le C_\alpha\sum_{\substack{m\ge1\\m\text{ odd}}}m^{-s},
\quad C_\alpha=\sqrt{K_\alpha/k_\alpha}.
\]
The same bound holds for \(A^{-1}=D^{-1/2}L^{-1}D^{1/2}\), because \(|\mu(m)|\le1\). Since \(s>1\),
\[
Z_s^{\mathrm{odd}}=\sum_{m\text{ odd}}m^{-s}
=(1-2^{-s})\zeta(s)<\infty.
\]
Set \(\mathcal K_\alpha=C_\alpha Z_s^{\mathrm{odd}}\). Because
\(D^{-1/2}G_{\mathrm{odd}}D^{-1/2}=AA^*\),
\[
\boxed{\mathcal K_\alpha^{-2}I
\preceq D^{-1/2}G_{\mathrm{odd}}D^{-1/2}
\preceq \mathcal K_\alpha^2I,\quad\alpha>1.}
\tag{5}
\]
This is **uniform in N** and involves all odd composites, but applies only to a diagonally preconditioned principal block of **H^{-1}**. It does **not** imply boundedness of the full primal operator H, and does **not** imply RH. At \(\alpha=1\), this proof's convergent dilation majorant is unavailable; it does not prove divergence there.

## 4. Exact odd-composite Schur interpolation inequality (PROVED)

Retain divisor-transform indices
\[
R_N=\{2\}\cup\mathcal O_N,\quad N\ge3.
\]
For a vector \(v\) supported there, define
\(S_r=\sum_{r\mid d,\ d\text{ odd}}v_d\) for odd \(r\), and \(v_2=t+S_3\). From the rows of B,
\[
\begin{aligned}
v^*[(H^{-1})_{R_N,R_N}]v
={}&c_1|S_1|^2
+c_2|t|^2+c_3|S_3|^2\\
&+\sum_{\substack{5\le r\le N\\r\text{ odd}}}
(c_{r-1}+c_r)|S_r|^2.
\end{aligned}
\tag{6}
\]
Here the change of variables \(v\mapsto(t,S_1,S_3,S_5,\ldots)\) is invertible by odd Möbius inversion.

For an arbitrary coefficient vector \(a\in\mathbb C^N\), let \(z_n=\sum_{d\mid n}a_d\). Applying duality to (6) and the positive-definite Schur-complement/minimum-energy principle gives
\[
\boxed{
\begin{aligned}
\mathcal Q_{\alpha,N}(a)\ge{}&
w_{\alpha,1}|z_1|^2+w_{\alpha,2}|z_2|^2\\
&+w_{\alpha,3}|z_2+z_3-z_1|^2\\
&+\sum_{\substack{5\le r\le N\\r\text{ odd}}}
\frac{\left|\sum_{d\mid r}\mu(r/d)z_d\right|^2}
{c_{r-1}+c_r}.
\end{aligned}}
\tag{7}
\]
The divisors of odd \(r\) in this sum are automatically odd. Equality in (7) is achievable by optimizing the unobserved even coordinates \(z_4,z_6,\ldots\), so this is the **sharp** bound based only on the retained coordinates \(R_N\). This claim is checked by an exact symbolic inverse identity in the experiment.

### Specialization to actual Möbius coefficients

For \(a_n=\mu(n)\), Möbius inversion gives \(z_1=1,\ z_d=0\ (d>1)\). Hence
\[
\boxed{
Q_\alpha(N;\mu)\ge
w_{\alpha,1}+w_{\alpha,3}
+\sum_{\substack{5\le r\le N\\r\text{ odd}}}
\frac{\mu(r)^2}{c_{r-1}+c_r}.
}
\tag{8}
\]
This **strictly improves** the Phase XXIV odd-prime lower bound once \(N\ge15\), because \(15\) is odd, squarefree and composite; its additional summand is positive. Since \(c_{r-1}+c_r\asymp_\alpha r^{\alpha+1}\), the new lower-bound series converges as \(N\to\infty\) for every \(\alpha>0\).

Crucial limitation: (8) is a **lower**, not an upper, bound. The RH-equivalent challenge is to control \(Q_\alpha(N;\mu)\) **from above** at every fixed \(\alpha>1\). No such new upper bound follows from (5) or (8).

## 5. Independent verification

The companion script \`experiments/riemann_phase25_odd_divisor.py\` was executed locally with Python 3 (stdlib Fraction and NumPy eigenvalue diagnostics). Every exact check passed for \(N=3,5,8,12,15,21,32,40\) and \(\alpha=1,2,3\) — **24/24 test cases** — including:
- (1), (3), incidence inversion and the full exact restricted matrix inverse of (7);
- energy inequality for independently chosen nontrivial divisor coordinates;
- specialization (8).

Numerical diagonal-preconditioned odd-block eigenvalues were checked at \(N=32,64,128,256\) for \(\alpha=1,1.25,1.5,2\), **16 diagnostics**. Examples:

| N | alpha | min eigenvalue | max eigenvalue |
|---:|---:|---:|---:|
| 32 | 1.0 | 0.52867635 | 2.01348540 |
| 256 | 1.0 | 0.42137089 | 2.62211286 |
| 32 | 1.5 | 0.62026174 | 1.67891181 |
| 256 | 1.5 | 0.53950804 | 1.97141481 |
| 32 | 2.0 | 0.69702011 | 1.47252284 |
| 256 | 2.0 | 0.63880756 | 1.62550780 |

Actual weighted Möbius energy vs lower bound from (8):

| N | alpha | actual Q | bound |
|---:|---:|---:|---:|
| 15 | 1 | 1.1621045621 | 0.6250726707 |
| 15 | 2 | 0.9445379174 | 0.8112087831 |
| 32 | 1 | 1.7382457320 | 0.6291593819 |
| 32 | 2 | 0.9688727644 | 0.8115455866 |

Finite spectral observations do not establish or refute global spectral asymptotics at alpha=1.

## 6. Verdict and next proof obligation

**Proved:** exact entire odd-block weighted-gcd factorization, determinant and Möbius inverse; dimension-independent two-sided bounds on its **diagonally normalized inverse block** for each fixed alpha>1; a sharp odd-composite Schur interpolation **lower bound** on arbitrary primal energies.

**Not proved:** any improved uniform **upper** bound on the full sieve-to-prefix operator at fixed \(1<\alpha<2\); any new zero-free half-plane; RH.

**Next research decision:** investigate whether a decomposition containing *both odd and even composite interactions* admits a transfer estimate in the needed upper direction. An additional uniformly conditioned principal inverse block, without control of its coupling to the complement, does not suffice. Prior art in GCD incidence matrices makes originality doubtful until assessed with expert literature review.
