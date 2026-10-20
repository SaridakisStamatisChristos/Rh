# Phase XX — Exact off-diagonal cancellation and the critical-exponent spectral obstruction

**Date:** 20 October 2026. **Status:** complete elementary finite matrix identities; critical-line spectral lower bound derived from the classical Hardy theorem and the standard Mellin formula. These arguments are not claimed novel and **do not prove RH**.

## 1. Definitions

For the Möbius function \(\mu(n)\), put \(M(x)=\sum_{n\le x}\mu(n)\). For integer \(N\ge1\), define the \(N\times N\) matrix
\[
T_N(k,d)=\begin{cases}M(\lfloor k/d\rfloor),&d\le k,\\0,&d>k,\end{cases}
\]
and weights \(w_{\alpha,k}=k^{-\alpha}-(k+1)^{-\alpha}\) for \(1\le k<N\), and \(w_{\alpha,N}=N^{-\alpha}\), where \(\alpha>0\). Let
\[
H_{\alpha,N}=T_N^\ast\operatorname{diag}(w_{\alpha,1},\dots,w_{\alpha,N})T_N.
\]
This is the positive-semidefinite sieve-to-prefix energy Gram matrix. Phase XIX derived
\((H_{\alpha,N})_{dd}=d^{-\alpha}Q_\alpha(\lfloor N/d\rfloor;\mu)\).

## 2. Exact row sum and total signed sum

Classical Möbius inversion gives for **every** integer \(k\ge1\)
\[
\sum_{d\le k}M(\lfloor k/d\rfloor)=\sum_{m\le k}\mu(m)\lfloor k/m\rfloor=1.
\]
Thus \(T_N\mathbf1=\mathbf1\). It follows that
\[
\begin{aligned}
\sum_{e=1}^NH_{\alpha,N}(d,e)
&=\langle T_Ne_d,T_N\mathbf1\rangle_w\\
&=\sum_{k=d}^Nw_{\alpha,k}M(\lfloor k/d\rfloor)\\
&=\sum_{m\le N/d}\mu(m)\sum_{k=dm}^Nw_{\alpha,k}\\
&=\boxed{d^{-\alpha}\sum_{m\le N/d}\frac{\mu(m)}{m^\alpha}}.
\end{aligned}
\tag{1}
\]
The last equality uses \(\sum_{k=r}^Nw_{\alpha,k}=r^{-\alpha}\).
Summing all matrix entries,
\[
\boxed{\mathbf1^\ast H_{\alpha,N}\mathbf1=1.}
\tag{2}
\]
This identity holds for every \(N,\alpha>0\). **Interpretation:** The coordinate vector \(z=\mathbf1\) corresponds under inverse Möbius transformation to \(a_n=\sum_{d\mid n}\mu(n/d)=\mathbf1_{n=1}\). Therefore the total-sum identity represents the energy of a point mass at 1. It is a classical cancellation identity, not independent evidence of RH.

## 3. Quantitative off-diagonal cancellation

For \(d>k/2\), \(T_N(k,d)=M(1)=1\). Thus each row obeys
\[
\sum_{d\le k}|T_N(k,d)|^2\ge k-\lfloor k/2\rfloor\ge k/2.
\]
Consequently,
\[
\begin{aligned}
\operatorname{tr}H_{\alpha,N}
&=\sum_{k=1}^Nw_{\alpha,k}\sum_{d\le k}|T_N(k,d)|^2\\
&\ge\tfrac12\sum_{k=1}^N k\,w_{\alpha,k}\\
&=\boxed{\tfrac12\sum_{k=1}^Nk^{-\alpha}}.
\end{aligned}
\tag{3}
\]
The last step is exact summation by parts. In addition, every row of \(T_N\) contains integers summing to 1, hence its sum of squares is at least 1, so \(\operatorname{tr}H_{\alpha,N}\ge1\), strictly if \(N\ge3\).

Combining (2) with the trace,
\[
\boxed{\sum_{d\ne e}H_{\alpha,N}(d,e)
=1-\operatorname{tr}H_{\alpha,N}
\le 1-\frac12\sum_{k=1}^Nk^{-\alpha}.}
\tag{4}
\]
For \(\alpha=1\) this tends to \(-\infty\) at least as fast as \(-\tfrac12\log N\); for \(0<\alpha<1\), at least as fast as \(-N^{1-\alpha}/(2(1-\alpha))\) up to constants. **This is algebraic and unconditional.** It is a *signed aggregate*; neither entrywise positivity nor a bound on the spectral norm follows.

### Exact entrywise counterexamples

At \(N=3\), \(\alpha=1\), with \(M(1)=1,M(2)=0,M(3)=-1\),
\[
T_3=\begin{pmatrix}1&0&0\\0&1&0\\-1&1&1\end{pmatrix},
\quad w=(1/2,1/6,1/3).
\]
Thus \(H_{12}=H_{13}=-1/3\), while \(H_{23}=+1/3\); the trace is \(5/3\) and the summed off-diagonal entries are \(-2/3\). At \(N=5\), \(\alpha=1\), the first row sum is
\[
1-\tfrac12-\tfrac13-\tfrac15=-\tfrac1{30}.
\]
Hence entries and even row sums can change sign. Entrywise positivity, diagonal-dominance arguments, and naive Schur tests must not be assumed.

## 4. Strong obstruction at the endpoint alpha=1

**Theorem (from classical zeros on the critical line).** For the actual Möbius coefficients,
\[
\boxed{\sup_N\|H_{1,N}\|_{\ell^2\to\ell^2}=+\infty,}
\tag{5}
\]
and in fact
\[
\boxed{\limsup_{N\to\infty}\frac{\|H_{1,N}\|}{\log N}>0.}
\tag{6}
\]
Hardy proved that \(\zeta\) has infinitely many zeros on \(\Re s=1/2\). Fix any such \(\rho=1/2+i\gamma\) of multiplicity \(m\ge1\).

Let \(E(X)=\int_1^XM(x)^2x^{-2}\,dx\) and \(A(T)=E(e^T)\). The first diagonal entry obeys
\[
\|H_{1,N}\|\ge H_{1,N}(1,1)=Q_1(N;\mu)
=E(N)+\frac{M(N)^2}{N}\ge E(N).
\tag{7}
\]
Write \(L=\limsup_{T\to\infty}A(T)/T\). If \(L=\infty\), (6) follows. Assume \(L<\infty\).

Put \(f(u)=e^{-u/2}M(e^u)\). Then \(A(T)=\int_0^T|f(u)|^2du\le (L+\eta)T\) for sufficiently large \(T\) (every fixed \(\eta>0\)). Consequently the Laplace transform
\[
F_\gamma(\varepsilon)=\int_0^\infty f(u)e^{-(\varepsilon+i\gamma)u}du
\]
converges absolutely and holomorphically for \(\Re\varepsilon>0\), by weighted Cauchy–Schwarz. For real \(\varepsilon>1/2\), the classical Mellin identity gives
\[
F_\gamma(\varepsilon)=\frac1{(\rho+\varepsilon)\zeta(\rho+\varepsilon)}.
\tag{8}
\]
Analytic/meromorphic identity continuation gives the same equality for small positive \(\varepsilon\) (and forces the absence of poles in \(\Re\varepsilon>0\) under the finite-\(L\) hypothesis).

Weighted Cauchy–Schwarz gives
\[
\varepsilon^2|F_\gamma(\varepsilon)|^2
\le \varepsilon\int_0^\infty|f(u)|^2e^{-\varepsilon u}du
=\varepsilon^2\int_0^\infty A(u)e^{-\varepsilon u}du
\le L+\eta+o(1).
\tag{9}
\]
If \(m\ge2\), the left side tends to infinity, contradiction; hence \(L=\infty\). If \(m=1\), (8) and the simple-zero expansion imply
\[
\lim_{\varepsilon\downarrow0}\varepsilon F_\gamma(\varepsilon)
=\frac1{\rho\zeta'(\rho)},
\]
so
\[
\boxed{
\limsup_{N\to\infty}\frac{\|H_{1,N}\|}{\log N}
\ge\frac1{|\rho\zeta'(\rho)|^2}>0.
}
\tag{10}
\]
This latter bound holds whenever \(\rho\) is simple. In the multiple-zero case the limsup in (10), interpreted without its finite right-side constant, is actually infinite.

Thus an operator norm bound uniform in \(N\) is *impossible* at \(\alpha=1\), although the total matrix sum is exactly 1 and the total off-diagonal sum is negative. This endpoint result does not prohibit a bound for each fixed \(\alpha>1\); proving the latter for all \(\alpha>1\) would imply RH.

### Why this is not an RH proof

The use of a critical-line zero is unconditional: such zeros exist by Hardy's theorem, not by assuming RH. The argument gives an endpoint **obstruction** to a particular stronger operator hypothesis and a quantified lower bound; it supplies no new zero-free region. The statement is expected to be related to classical weak-Mertens/reciprocal-zeta pole lower bounds. Do not claim novelty without a prior-art audit.

## 5. Verification

The companion Python 3 script \`certificates/riemann_phase20_offdiagonal_certificate.py\` uses exact \`fractions.Fraction\` arithmetic to verify (1), (2), (4), the diagonal identity from Phase XIX, and the matrix products for \((N,\alpha)\in\{3,5,8,16,32\}\times\{1,2,3\}\). All fifteen cases PASS. It checks \(H_{12}=H_{13}=-1/3,\ H_{23}=1/3\) for \(N=3,\alpha=1\), and row-sum \(-1/30\) for \(N=5,\alpha=1\). The proof for all \(N\) is the algebra above, not these finite checks.

An optional floating-point spectral experiment separately evaluated \(N=32,64,128,256,512\) at \(\alpha=1\): the observed largest eigenvalues were approximately \(2.355,\ 2.152,\ 2.154,\ 2.140,\ 2.193\). Such finite measurements do not exhibit or refute the asymptotic divergence (6).

## Sources and related prior art

- G. H. Hardy, *Sur les zéros de la fonction ζ(s) de Riemann*, Comptes Rendus 158 (1914), 1012–1014: infinitude of critical-line zeros. Secondary confirmation: https://www.sciencedirect.com/science/article/pii/S0022314X14003515
- Classical Dirichlet-series identity \(1/\zeta(s)=s\int_1^\infty M(x)x^{-s-1}dx\), initially \(\Re s>1\).
- Brevig, Perfekt, Seip, Siskakis and Vukotić, *The multiplicative Hilbert matrix*, Advances in Mathematics 302 (2016), 410–432, https://doi.org/10.1016/j.aim.2016.07.019 — related operator-theoretic prior art, **not** identical to the matrix here.

**Evidence classification:** exact algebra (PROVED); critical-zero endpoint lower bound (PROVED using classical Hardy theorem and Mellin identity); finite rational checks (EXECUTED); new fixed-\(\alpha>1\) norm bound (NOT PROVED); RH (UNSOLVED).
