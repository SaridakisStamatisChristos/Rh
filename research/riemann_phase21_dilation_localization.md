# Phase XXI — Arithmetic dilation, persistent obstructions and spectral localization

**20 October 2026 — research note.** The finite-dimensional identities and inequalities below have elementary proofs and were subjected to rational-arithmetic checks. They **do not prove the Riemann hypothesis (RH)**. The analytic novelty of the formulation has not been established; related themes in dilation systems and Dirichlet-series operators are classical.

## 1. Definitions

Write \(\mu(n)\) for the Möbius function and \(M(x)=\sum_{n\le x}\mu(n)\). For any coefficient vector \(a\in\mathbb C^N\), its divisor transform is \(z_n=\sum_{d\mid n}a_d\), so that \(a_n=\sum_{d\mid n}\mu(n/d)z_d\). Its ordinary prefix is
\[
A(k)=\sum_{d\le k}M(\lfloor k/d\rfloor)z_d.
\]
For \(\alpha>0\), let \(T_N(k,d)=\mathbf1_{d\le k}M(\lfloor k/d\rfloor)\) and weights \(w_{\alpha,k}=k^{-\alpha}-(k+1)^{-\alpha}\) for \(k<N\), \(w_{\alpha,N}=N^{-\alpha}\). Define
\[
H_{\alpha,N}=T_N^*\mathrm{diag}(w_{\alpha,k})T_N,
\qquad
z^*H_{\alpha,N}z=\sum_{m,n\le N}\frac{a_m\overline{a_n}}{\max(m,n)^\alpha}.
\]
This matrix is positive definite, because \(T_N\) is lower triangular with diagonal entries 1 and every weight is positive. Its trace formula from Phase XIX is
\[
\operatorname{tr}H_{\alpha,N}=\sum_{d\le N}d^{-\alpha}Q_\alpha(\lfloor N/d\rfloor;\mu),
\quad Q_\alpha(K;\mu)=\sum_{m,n\le K}\frac{\mu(m)\mu(n)}{\max(m,n)^\alpha}\ge0.
\]

## 2. Exact arithmetic-dilation covariance (PROVED)

For any integer \(d\ge1\), put \(K=\lfloor N/d\rfloor\). Let \(U_d:\mathbb C^K\to\mathbb C^N\) embed coordinates by \((U_d z)_{dm}=z_m\) and set all other coordinates to zero. Then
\[
\boxed{U_d^*H_{\alpha,N}U_d=d^{-\alpha}H_{\alpha,K}.}\tag{1}
\]
**Proof.** The inverse divisor transform of \(U_dz\) is supported on multiples of \(d\), with \(a'_{dm}=a_m\). Indeed
\[
a'_{dm}=\sum_{r\mid dm}\mu(dm/r)(U_dz)_r
=\sum_{r'\mid m}\mu(m/r')z_{r'}=a_m,
\]
and it vanishes at integers not divisible by \(d\). Every pair of nonzero indices in the maximum-kernel energy is \((dm,dn)\), extracting \(d^{-\alpha}\). Equality of quadratic forms for every \(z\) proves (1).

In particular, every principal block restricted to multiples of \(d\) is a rescaled copy of the full smaller Gram matrix, not merely a set of similarly behaved diagonal entries.

## 3. Fixed-coordinate removal is RH-equivalent (PROVED)

Fix \(D\ge1\) and \(\alpha>1\). For each \(N\ge D\), denote by \(P_{D,N}\) the projection onto \(\{D,D+1,\dots,N\}\). Then
\[
\boxed{\sup_{N\ge D}\|P_{D,N}H_{\alpha,N}P_{D,N}\|<\infty
\quad\Longleftrightarrow\quad
\sup_m Q_\alpha(m;\mu)<\infty.}\tag{2}
\]
**Proof, \(\Rightarrow\).** Test the compression on \(e_D\). By (1),
\[
\langle e_D,H_{\alpha,N}e_D\rangle=D^{-\alpha}Q_\alpha(\lfloor N/D\rfloor;\mu).
\]
Taking \(N=Dm\) shows boundedness of \(Q_\alpha(m;\mu)\) uniformly in \(m\).

**Proof, \(\Leftarrow\).** If \(Q_\alpha(m;\mu)\le B_\alpha\) for every \(m\), the positive-semidefinite trace formula yields
\[
\|P_{D,N}H_{\alpha,N}P_{D,N}\|\le\mathrm{tr}H_{\alpha,N}
\le B_\alpha\sum_{d=1}^Nd^{-\alpha}\le B_\alpha\zeta(\alpha).
\]
The condition \(\sup_m Q_\alpha(m;\mu)<\infty\) for **every** \(\alpha>1\) is equivalent to RH by the classical Littlewood criterion and the energy identity. Thus (2), demanded for every \(\alpha>1\), is RH-equivalent for **any fixed finite coordinate cutoff**. Removing finitely many coordinates never removes the logical obstruction.

## 4. High-divisor spectral tail (unconditional, PROVED)

For \(1<\alpha<2\), the elementary coefficient bound \(|\mu(n)|\le1\) gives
\[
\begin{aligned}
0\le Q_\alpha(m;\mu)
&\le\sum_{u,v\le m}\max(u,v)^{-\alpha}
=\sum_{r\le m}\frac{2r-1}{r^\alpha}\\
&\le2\sum_{r\le m}r^{1-\alpha}
\le\frac{2}{2-\alpha}m^{2-\alpha}.
\end{aligned}
\tag{3}
\]
The last inequality follows by comparison of the decreasing function \(x^{1-\alpha}\) with its integral. Set \(P=P_{D,N}\), where \(2\le D\le N\). Trace positivity and (3) yield
\[
\begin{aligned}
\|P H_{\alpha,N}P\|
&\le\mathrm{tr}(P H_{\alpha,N}P)
=\sum_{d=D}^Nd^{-\alpha}Q_\alpha(\lfloor N/d\rfloor;\mu)\\
&\le\frac{2}{2-\alpha}N^{2-\alpha}\sum_{d=D}^\infty d^{-2}
\le\boxed{\frac{2}{2-\alpha}\frac{N^{2-\alpha}}{D-1}.}
\end{aligned}
\tag{4}
\]
This is an **unconditional bound for the actual finite matrices**, requiring no RH or zero-free-region inputs. It uses only \(|\mu|\le1\) and thus is not yet an arithmetic breakthrough.

Choose \(0<\eta<\alpha-1\) and a growing cutoff
\[
D_N=\lfloor N^{2-\alpha+\eta}\rfloor+1.
\]
For all sufficiently large \(N\) this satisfies \(D_N\le N\), and (4) implies
\[
\boxed{\|P_{D_N,N}H_{\alpha,N}P_{D_N,N}\|
\le\frac{2}{2-\alpha}N^{-\eta}.}\tag{5}
\]
Therefore all large-divisor directions above \(N^{2-\alpha+\eta}\) contribute vanishing *operator norm*. This is a quantitative spectral-localization result at **every fixed** \(1<\alpha<2\); it does **not** control the remaining low-coordinate block, and so does not give RH.

## 5. Approximate leading eigenvalue from a smaller principal matrix

Let \(L\) project onto the first \(D-1\) coordinates, \(P=I-L\). For any positive-semidefinite \(H\), the Gram factorization \(H=B^*B\) gives
\[
\|H\|\le\|LHL\|+\|PHP\|,
\qquad\|LHL\|\le\|H\|.
\]
To see the upper bound, write \(B=[B_L\ B_P]\) and use
\(\|B\|^2\le \|B_L\|^2+\|B_P\|^2\). Thus from (4)
\[
\boxed{
0\le\|H_{\alpha,N}\|-\|L H_{\alpha,N}L\|
\le\frac{2}{2-\alpha}\frac{N^{2-\alpha}}{D-1}.}
\tag{6}
\]
With the cutoff in (5), the largest eigenvalue of the full \(N\times N\) matrix is determined within additive error \(O_\alpha(N^{-\eta})\) by its \((D_N-1)\times(D_N-1)\) leading principal block. This is a valid *dimension-reduction/certification statement*, not an eigenvalue-uniformity proof: the small block still grows with \(N\) and contains RH-equivalent information.

## 6. Exact upper-half block, with matching norm scale (PROVED)

Put \(D=\lfloor N/2\rfloor+1\), \(L_0=N-D+1=\lceil N/2\rceil\). For \(d,e\ge D\), the inverse divisor transform has no nonzero multiples except \(d\) and \(e\) themselves: hence
\[
\boxed{H_{\alpha,N}(d,e)=\max(d,e)^{-\alpha}.}\tag{7}
\]
All entries in this block are positive. The constant-vector Rayleigh quotient and maximum absolute row sum give the matching bounds
\[
\boxed{\frac{L_0}{N^\alpha}\le
\|P_{D,N}H_{\alpha,N}P_{D,N}\|
\le\frac{L_0}{D^\alpha}.}\tag{8}
\]
Thus for fixed \(\alpha>1\), the upper-half block norm is \(\Theta_\alpha(N^{1-\alpha})\to0\). At \(\alpha=1\) it remains \(\Theta(1)\), even though Phase XX proved the *full* matrix norm grows at least logarithmically along a subsequence. The obstruction is concentrated elsewhere.

## 7. Verified finite tests

The accompanying Python script runs:
- **60 exact rational groups** over \(N\in\{8,12,24,36\}\), \(\alpha\in\{1,2,3\}\) and integer dilations \(d\in\{2,3,4,5\}\), plus the exact upper-half identities and inequalities.
- **9 numerical matrix tests** at \(N=64,128,256\) and \(\alpha=1.25,1.5,1.75\). The measured full-largest eigenvalue exceeds that of the leading compressed block by substantially less than the analytic tail trace.

Selected finite checks:

| N | alpha | D | lambda_max(full) | lambda_max(low) | measured difference | upper bound from (4) |
|---:|---:|---:|---:|---:|---:|---:|
| 64 | 1.25 | 39 | 1.25151029 | 1.24641017 | 0.00510012 | 1.58788891 |
| 128 | 1.50 | 39 | 1.10009004 | 1.09984446 | 0.00024558 | 1.19091668 |
| 256 | 1.25 | 129 | 1.25797721 | 1.25795674 | 0.00002047 | 1.33333333 |
| 256 | 1.50 | 65 | 1.10182218 | 1.10176914 | 0.00005304 | 1.00000000 |
| 256 | 1.75 | 33 | 1.01831145 | 1.01827028 | 0.00004117 | 1.00000000 |

The exact arithmetic supports the finite identities; **the proofs for arbitrary N are the algebra above**, not extrapolation from measurements.

## 8. Prior art, limitations and next test

Classical work connects dilation systems and RH (Nyman–Beurling and later Hilbert-space developments). Relevant context:
- Nikolaï Nikolski, *Hardy Spaces*, Ch. 6, *The Riemann Hypothesis, Dilations, and H² in the Hilbert Multi-disk* (2019), DOI: https://doi.org/10.1017/9781316882108.008.
- *Zero-Free Regions of the Riemann Zeta Function and Approximation in Weighted Dirichlet Spaces* (2025), https://link.springer.com/article/10.1007/s11785-025-01661-2.
- *The multiplicative Hilbert matrix*, Advances in Mathematics 302 (2016), DOI: https://doi.org/10.1016/j.aim.2016.07.019.

No claim is made that the present elementary scaling/compression observations are novel. The essential target remains a bound on the leading \(N^{2-\alpha+\eta}\)-dimensional block for every fixed \(\alpha>1\), without importing the bound on \(Q_\alpha(N;\mu)\) that is itself RH-equivalent.

**Evidence ledger:** equations (1)–(8) PROVED by elementary reasoning; finite checks EXECUTED; any fixed-alpha improvement of zeta zero-free regions NOT ACHIEVED; RH UNSOLVED.