# Phase XIX — Trace of the sieve-to-prefix operator

**Date:** 20 October 2026  
**Status:** exact trace identity; unconditional \(\alpha\ge2\) operator inequality, **assuming the independently checkable finite Phase XII certificate and the published explicit Mertens bound used there**; independent finite rational and numerical checks. **No RH proof. No novelty claim.**

## 1. Operators and kernels

Let \(\mu(n)\) be the Möbius function, \(M(x)=\sum_{n\le x}\mu(n)\). For \(a=(a_n)_{1\le n\le N}\in\mathbb C^N\), define its divisor transform
\[
z_n=\sum_{d\mid n}a_d,\qquad a_n=\sum_{d\mid n}\mu(n/d)z_d.
\]
Then
\[
A(k):=\sum_{n\le k}a_n=\sum_{d\le k}z_d M(\lfloor k/d\rfloor).
\]
Define the lower-triangular matrix
\[
T_N(k,d)={\bf1}_{d\le k}M(\lfloor k/d\rfloor)
\]
and positive weights \(w_{\alpha,k}=k^{-\alpha}-(k+1)^{-\alpha}\) for \(k<N\), and \(w_{\alpha,N}=N^{-\alpha}\), for \(\alpha>0\). The positive form
\[
\mathcal Q_{\alpha,N}(a)
=\sum_{k=1}^N w_{\alpha,k}|A(k)|^2
=\sum_{m,n\le N}\frac{a_m\bar a_n}{\max(m,n)^\alpha}
=z^*H_{\alpha,N}z
\]
uses
\[
H_{\alpha,N}=T_N^*\operatorname{diag}(w_{\alpha,k})T_N\succeq0.
\]
Here the conjugated maximum-kernel expression is valid for complex \(a\).

## 2. Exact diagonal and trace (proven)

For the \(d\)-th divisor-coordinate basis vector \(z=e_d\), inverse Möbius transformation gives \(a_{dm}=\mu(m)\) for \(dm\le N\), and \(a_n=0\) otherwise. Rescale both indices by \(d\) in the maximum-kernel form to obtain
\[
\boxed{(H_{\alpha,N})_{dd}=d^{-\alpha}Q_\alpha(\lfloor N/d\rfloor;\mu).}
\]
Therefore
\[
\boxed{\operatorname{tr}H_{\alpha,N}
=\sum_{d=1}^N d^{-\alpha}Q_\alpha(\lfloor N/d\rfloor;\mu).}
\tag{1}
\]
All equalities hold exactly for finite \(N\), independently of RH.

## 3. Explicit \(\alpha\ge2\) operator bound (proven from Phase XII input)

Let \(S_\alpha(m)=\sum_{n\le m}\mu(n)^2/n^\alpha\) and
\(C_\alpha(m)=\sum_{n\le m}\mu(n)M(n-1)/n^\alpha\). The existing exact identity is
\[
Q_\alpha(m;\mu)=S_\alpha(m)+2C_\alpha(m).
\]
Phase XII established \(C_\alpha(m)<0\) for all integers \(m\ge2\), all \(\alpha\ge2\), by a finite integer-arithmetic certificate plus Johnston–Leong–Tudzi's published bound \(|M(x)|\le2.91890x/(\log x)^2\) for \(x>1\).
For \(m=1\), \(C_\alpha(1)=0\). Thus, for every \(m\ge1,\alpha\ge2\),
\[
0\le Q_\alpha(m;\mu)\le S_\alpha(m)\le \frac{\zeta(\alpha)}{\zeta(2\alpha)}.
\]
Using (1),
\[
\operatorname{tr}H_{\alpha,N}
\le\frac{\zeta(\alpha)^2}{\zeta(2\alpha)}
=\prod_p\frac{1+p^{-\alpha}}{1-p^{-\alpha}}
\le\frac{\zeta(2)^2}{\zeta(4)}=\frac52.
\]
The Euler product decreases with increasing \(\alpha>1\). For every positive semidefinite matrix,
\(\lambda_{\max}(H)\le\operatorname{tr}H\). Therefore the **operator inequality for arbitrary coefficient vectors**
\[
\boxed{
\sum_{m,n\le N}\frac{a_m\bar a_n}{\max(m,n)^\alpha}
\le\frac52\sum_{n\le N}\left|\sum_{d\mid n}a_d\right|^2
\quad (\alpha\ge2)
}
\tag{2}
\]
holds uniformly in \(N\).

### Sharper explicit result at \(\alpha=2\)

Phase XII gives \(C_2(m)<-1/10\) for every \(m\ge2\). Therefore
\[
Q_2(m;\mu)<\frac{\zeta(2)}{\zeta(4)}-\frac15
=\frac{15}{\pi^2}-\frac15\qquad (m\ge2).
\]
At \(m=1\), \(Q_2(1;\mu)=1<15/\pi^2-1/5\), so the same uniform bound holds for *all* \(m\ge1\). Applying (1) gives
\[
\boxed{\mathcal Q_{2,N}(a)\le
\left(\frac52-\frac{\pi^2}{30}\right)
\sum_{n\le N}|z_n|^2,\quad
\frac52-\frac{\pi^2}{30}\approx2.17101318663.}
\tag{3}
\]
This result is unconditional under the published external theorem and the exact finite certificate that are documented in Phase XII; it is not an independent proof of that earlier sign theorem.

## 4. Trace finiteness and RH — no shortcut

For every fixed \(\alpha>1\), since all terms in (1) are nonnegative and the \(d=1\) summand equals \(Q_\alpha(N;\mu)\), boundedness of the trace uniformly in \(N\) **implies** bounded \(Q_\alpha(N;\mu)\). Conversely, if \(\sup_m Q_\alpha(m;\mu)<\infty\), then (1) implies \(\sup_N\operatorname{tr}H_{\alpha,N}\le\zeta(\alpha)\sup_m Q_\alpha(m;\mu)\). Consequently
\[
\boxed{\forall\alpha>1\;\sup_N\operatorname{tr}H_{\alpha,N}<\infty
\quad\Longleftrightarrow\quad \mathrm{RH}.}
\tag{4}
\]
This is a **reformulation**, not proof of RH.

A bound on \(\operatorname{tr}H\) is stronger than a bound on \(\lambda_{\max}(H)\) for a general matrix; a trace that grows with dimension does *not* prove divergence of the operator norm. The numerical values below demonstrate finite behavior only.

## 5. Executed verification

The companion Python 3 script performs **exact Fraction** comparisons of both sides of (1) at \(N=4,8,12,24\) and \(\alpha=1,2,3\). All twelve exact checks passed. Optional NumPy double-precision spectral diagnostic, separately checked against the trace formula:

| N | alpha | trace(H) | largest eigenvalue(H) |
|---:|---:|---:|---:|
| 32 | 1.25 | 3.186085940 | 1.471161650 |
| 32 | 1.50 | 2.324807874 | 1.165322746 |
| 32 | 2.00 | 1.537357058 | 0.980936255 |
| 64 | 1.25 | 3.508873047 | 1.251510290 |
| 64 | 1.50 | 2.447311414 | 1.094939416 |
| 64 | 2.00 | 1.555083072 | 0.970449773 |
| 128 | 1.25 | 3.814626034 | 1.256163361 |
| 128 | 1.50 | 2.546910293 | 1.100090038 |
| 128 | 2.00 | 1.565717351 | 0.971387898 |
| 256 | 1.25 | 4.086603028 | 1.257977208 |
| 256 | 1.50 | 2.621893775 | 1.101822179 |
| 256 | 2.00 | 1.571451294 | 0.971571343 |

These are diagnostics, *not* bounds in \(N\) or proofs about \(1<\alpha<2\).

## 6. Scope, dependencies, and next experiment

- **Proved algebraically:** exact transfer matrix, positive energy, trace identity and trace-vs-operator inequality.
- **Proved with external/finite inputs:** explicit \(\alpha\ge2\) operator bound (2) and \(\alpha=2\) sharpened constant (3).
- **Not proved:** any uniformly bounded trace or operator norm at fixed \(1<\alpha<2\), and RH.
- **Next discriminating work:** test *structured arithmetic subspaces* or find an operator decomposition whose residual can be bounded independently of the RH-equivalent first column. Do **not** infer uniform boundedness from finite eigenvalues or transfer the \(\alpha\ge2\) estimate into the strip without a separate argument.

Sources: [DLMF Möbius inversion](https://dlmf.nist.gov/27.5), Johnston–Leong–Tudzi [explicit Mertens bound, Theorem A.1](https://doi.org/10.1080/10586458.2025.2483942), [Brevig et al., multiplicative Hilbert matrix](https://doi.org/10.1016/j.aim.2016.07.019), [Hedenmalm/Lindqvist/Seip and Dirichlet-series Hilbert spaces](https://doi.org/10.1016/j.jmaa.2019.03.026). These are relevant prior art, not claims of priority.

**Research status: RH remains open.**
