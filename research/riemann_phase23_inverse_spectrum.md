# Phase XXIII — Exact inverse and RH-equivalent condition-number growth

**Date:** 20 October 2026  
**Status:** Complete elementary proofs of an exact inverse, determinant, inverse-trace asymptotic, and sharp polynomial order of the smallest eigenvalue for fixed \(\alpha>1\). The condition-number criterion is *equivalent to RH*, **not** a proof of RH. All mathematical novelty remains unassessed. Finite exact and numerical checks completed.

## 1. Basic definitions and factorization

For the Möbius function \(\mu\), let \(M(x)=\sum_{n\le x}\mu(n)\).
Fix \(\alpha>0\) and integer \(N\ge1\). Define
\[
T_N(k,d)=\mathbf 1_{d\le k}M(\lfloor k/d\rfloor),\qquad
w_{\alpha,k}=\begin{cases}
k^{-\alpha}-(k+1)^{-\alpha},&1\le k<N,\\
N^{-\alpha},&k=N.
\end{cases}
\]
The symmetric positive-definite matrix
\[
H_{\alpha,N}=T_N^\ast W_{\alpha,N}T_N,\qquad
W_{\alpha,N}=\operatorname{diag}(w_{\alpha,k})
\]
represents the maximum-kernel weighted prefix energy of the inverse divisor transform (Phase XIX).

Set \(P_N(k,n)=\mathbf1_{n\le k}\), and \(V_N(n,d)=\mathbf1_{d\mid n}\). The divisor transform \(z=V_Na\), and ordinary prefix sums \(A=P_Na\), imply \(T_N=P_NV_N^{-1}\). The Möbius function enters in \(V_N^{-1}\), but its inverse \(V_NP_N^{-1}\) is *elementary*.

## 2. Exact inverse, determinant, and dual quadratic form

Since \(P_N^{-1}\) is the first-difference matrix, we have
\[
\boxed{(T_N^{-1})(d,k)=\mathbf1_{k\mid d}-\mathbf1_{k+1\mid d}.}
\tag{1}
\]
In particular \(\det T_N=1\). Let \(B_N=T_N^{-1}\). Then
\[
\boxed{H_{\alpha,N}^{-1}=B_NW_{\alpha,N}^{-1}B_N^\ast,\qquad
\det H_{\alpha,N}=\prod_{k=1}^N w_{\alpha,k}.}
\tag{2}
\]
Hence
\[
\boxed{\det H_{\alpha,N}=N^{-\alpha}\prod_{k<N}
(k^{-\alpha}-(k+1)^{-\alpha}).}
\tag{3}
\]
The determinant is *independent of the Möbius values*. It cannot on its own provide an RH test for this particular matrix.

For a vector \(v=(v_d)_{1\le d\le N}\) (real or complex) define
\[
S_k(v)=\sum_{m:km\le N}v_{km},\qquad S_{N+1}(v)=0.
\]
Then
\[
(B_N^\ast v)_k=S_k(v)-S_{k+1}(v),
\]
and
\[
\boxed{v^\ast H_{\alpha,N}^{-1}v
=\sum_{k=1}^Nw_{\alpha,k}^{-1}|S_k(v)-S_{k+1}(v)|^2.}
\tag{4}
\]
This dual form is explicitly Möbius-free, though its best lower frame constant is difficult.

## 3. Exact inverse trace and sharp asymptotic

From the divisor indicators and \(\gcd(k,k+1)=1\),
\[
\sum_{d\le N}(\mathbf1_{k\mid d}-\mathbf1_{k+1\mid d})^2
=\lfloor N/k\rfloor+\lfloor N/(k+1)\rfloor
-2\lfloor N/(k(k+1))\rfloor.
\]
Consequently
\[
\boxed{\operatorname{tr}H_{\alpha,N}^{-1}
=\sum_{k=1}^N \frac{\lfloor N/k\rfloor+\lfloor N/(k+1)\rfloor
-2\lfloor N/[k(k+1)]\rfloor}{w_{\alpha,k}}.}
\tag{5}
\]

**Theorem (proved, no RH input).** For each fixed \(\alpha>0\),
\[
\boxed{\operatorname{tr}H_{\alpha,N}^{-1}
=\frac{2\zeta(\alpha+2)}{\alpha(\alpha+2)}N^{\alpha+2}
+O_\alpha(N^{\alpha+1}).}
\tag{6}
\]

### Proof

For \(1\le k<N\), the mean value theorem / Taylor expansion gives
\[
w_{\alpha,k}^{-1}=\alpha^{-1}k^{\alpha+1}+O_\alpha(k^\alpha).
\]
For \(p>0\), the power-sum formula and switching \(\lfloor N/k\rfloor\) with its divisor-counting interpretation yield
\[
\begin{aligned}
\sum_{k\le N}k^{p}\lfloor N/k\rfloor
&=\sum_{m\le N}\sum_{k\le N/m} k^p\\
&=\frac{\zeta(p+1)}{p+1}N^{p+1}
+O_p(N^p)
\end{aligned}
\]
provided \(p>1\) (so that the summed power-sum errors converge); here \(p=\alpha+1>1\). The same main term follows with \(\lfloor N/(k+1)\rfloor\), by shifting \(k\) and observing that \((k-1)^{\alpha+1}=k^{\alpha+1}+O_\alpha(k^\alpha)\). The error term from \(O(k^\alpha)\lfloor N/k\rfloor\) is \(O_\alpha(N^{\alpha+1})\) since \(\alpha>0\).

For the common-multiple subtraction, only \(k(k+1)\le N\) contribute:
\[
\sum_{k<N}w_{\alpha,k}^{-1}
\left\lfloor\frac{N}{k(k+1)}\right\rfloor
\ll_\alpha N\sum_{k\le\sqrt N}k^{\alpha-1}
=O_\alpha(N^{1+\alpha/2})
=O_\alpha(N^{\alpha+1}).
\]
The terminal \(k=N\) term is exactly \(N^\alpha\), negligible in (6). The two leading sums therefore contribute the main term in (6). \(\square\)

## 4. Sharp order of the smallest eigenvalue

**Theorem (proved):** For every fixed \(\alpha>1\),
\[
\boxed{\|H_{\alpha,N}^{-1}\|=\Theta_\alpha(N^{\alpha+1}),\qquad
\lambda_{\min}(H_{\alpha,N})=\Theta_\alpha(N^{-\alpha-1}).}
\tag{7}
\]

### Upper bound on inverse norm

For \(1\le k<N\), the mean value theorem gives
\[
w_{\alpha,k}^{-1}
\le\frac{(k+1)^{\alpha+1}}{\alpha}
\le\frac{2^{\alpha+1}}{\alpha}k^{\alpha+1}.
\]
The same weaker estimate holds at \(k=N\) since \(w_{\alpha,N}^{-1}=N^\alpha\).
By (4) and \(|x-y|^2\le2|x|^2+2|y|^2\),
\[
v^\ast H_{\alpha,N}^{-1}v
\le\frac{4\cdot2^{\alpha+1}}{\alpha}
\sum_{k\le N}k^{\alpha+1}|S_k(v)|^2.
\]
By Cauchy–Schwarz,
\[
|S_k(v)|^2
\le\frac Nk\sum_{m\le N/k}|v_{km}|^2.
\]
Thus
\[
\begin{aligned}
\sum_{k\le N}k^{\alpha+1}|S_k(v)|^2
&\le N\sum_{d\le N}|v_d|^2\sum_{k\mid d}k^\alpha\\
&=N\sum_{d\le N}|v_d|^2d^\alpha\sum_{\ell\mid d}\ell^{-\alpha}\\
&\le \zeta(\alpha)N^{\alpha+1}\|v\|_2^2.
\end{aligned}
\]
The final inequality is valid precisely as stated for every fixed \(\alpha>1\). Therefore
\[
\boxed{\|H_{\alpha,N}^{-1}\|
\le\frac{4\cdot2^{\alpha+1}\zeta(\alpha)}{\alpha}N^{\alpha+1}.}
\tag{8}
\]

### Lower bound on inverse norm

For \(N\ge4\), put \(d=2\lfloor N/2\rfloor\), \(k=d/2=\lfloor N/2\rfloor\ge2\). Then \(k\mid d\) while \(k+1\nmid d=2k\). Hence \(B_N(d,k)=1\). Since \(w_{\alpha,k}\le\alpha k^{-\alpha-1}\), the diagonal satisfies
\[
\boxed{\|H_{\alpha,N}^{-1}\|
\ge (H_{\alpha,N}^{-1})_{dd}
\ge w_{\alpha,k}^{-1}
\ge\frac{(N/3)^{\alpha+1}}{\alpha}.}
\tag{9}
\]
Inverting (8)–(9) proves the theorem.

## 5. Condition number and the RH-equivalent obstruction

Let \(\kappa_2(H)=\lambda_{\max}(H)/\lambda_{\min}(H)\). The bounds (8)–(9) give, for fixed \(\alpha>1\),
\[
\boxed{\kappa_2(H_{\alpha,N})
\asymp_\alpha N^{\alpha+1}\|H_{\alpha,N}\|.}
\tag{10}
\]

Phases XIX and XXI established (through the first diagonal and exact trace) that, for every \(\alpha>1\), \(\sup_N\|H_{\alpha,N}\|<\infty\) is equivalent to a bounded positive Mertens energy at that \(\alpha\). Demanding this for *every* \(\alpha>1\) is equivalent to RH.

Thus:
\[
\boxed{\mathrm{RH}\iff
\forall\alpha>1,\quad
\kappa_2(H_{\alpha,N})=O_\alpha(N^{\alpha+1}).}
\tag{11}
\]
This is an **equivalent criterion**, not a proof of the required estimate.

For all \(\alpha\ge2\), the prior Phase XII / XIX bound \(\|H_{\alpha,N}\|\le5/2\) yields the **unconditional**
\[
\boxed{\kappa_2(H_{\alpha,N})=\Theta_\alpha(N^{\alpha+1}),\quad\alpha\ge2.}
\]
The lower bound uses \(\|H_{\alpha,N}\|\ge (H_{\alpha,N})_{11}=Q_\alpha(N;\mu)\ge 1-2^{-\alpha}\) for \(N\ge2\).

The sharp elementary singularity of the smallest eigenvalue is *not* the RH obstacle. The unresolved question remains a bounded largest eigenvalue for every fixed \(1<\alpha<2\).

## 6. Independent computational verification

Companion script: \`experiments/riemann_phase23_inverse_spectrum.py\`.

- Independent exact \`fractions.Fraction\` computation verified \(T_NB_N=B_NT_N=I\), \(H_{\alpha,N}H_{\alpha,N}^{-1}=I\), the inverse trace formula, and all column-support counts for \(N=3,4,8,12,20\), \(\alpha=1,2,3\): 15 exact cases PASS.
- Finite NumPy eigenspectra were independently computed at \(N=32,64,128,256\) and \(\alpha=1.25,1.5,2.0\). All 12 inverse-trace/eigenvalue checks passed.

Examples:

| \(N\) | \(\alpha\) | \(\lambda_{\min}\) | \(\lambda_{\max}\) | inverse trace divided by \(N^{\alpha+2}\) |
|---:|---:|---:|---:|---:|
| 64 | 1.25 | 2.9238451e-5 | 1.2515103 | 0.573180587 |
| 128 | 1.25 | 5.8398174e-6 | 1.2561634 | 0.571838853 |
| 256 | 1.25 | 1.1884981e-6 | 1.2579772 | 0.571514133 |
| 256 | 1.50 | 3.6545474e-7 | 1.1018222 | 0.429840369 |
| 256 | 2.00 | 3.1306244e-8 | 0.9715713 | 0.270897200 |

The corresponding theoretical inverse-trace coefficients \(2\zeta(\alpha+2)/[\alpha(\alpha+2)]\) are approximately 0.570659439, 0.429231949 and 0.270580808 at \(\alpha=1.25,1.5,2\).

Finite numerical stabilization of the largest eigenvalue does not imply an all-\(N\) bound.

## 7. Prior art and integrity

This is an elementary incidence-algebra computation. Matrix spectral approaches to RH have longstanding prior art:
- Friedrich Roesler, *Riemann's hypothesis as an eigenvalue problem*, Linear Algebra and its Applications 81 (1986), 153–198, https://doi.org/10.1016/0024-3795(86)90255-7 (a different matrix).
- Pauliina Ilmonen and Vesa Kaarnioja, *Generalized eigenvalue problems for meet and join matrices on semilattices*, Linear Algebra and its Applications 536 (2018), 250–273, https://doi.org/10.1016/j.laa.2017.09.023.
- Werner Ehm, *On certain Gram matrices and their associated series* (2024), https://arxiv.org/abs/2405.06349.

No originality or superiority claims are made without a broader comparison. **The Riemann Hypothesis remains open.**
