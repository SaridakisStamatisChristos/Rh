# Phase XXII — Spectral Prime Number Theorem and the power-saving barrier

**Research date: 20 October 2026. Status:** exact consequences of standard Möbius summatory estimates and earlier Gram identities. **No proof of RH; no priority/novelty claim.** All asymptotic constants may depend on fixed parameters. Finite code checks are not substitutes for proofs.

## Definitions and the exact trace identity

Write \(\mu(n)\) for the Möbius function, \(M(x)=\sum_{n\le x}\mu(n)\), and for \(\alpha>0\),
\[
Q_\alpha(n)=\sum_{k=1}^{n-1}\big(k^{-\alpha}-(k+1)^{-\alpha}\big)M(k)^2+n^{-\alpha}M(n)^2\ge0.
\]
Define \(T_N(k,d)=\mathbf 1_{d\le k}M(\lfloor k/d\rfloor)\) and \(H_{\alpha,N}=T_N^*W_{\alpha,N}T_N\), where the positive diagonal weights \(W_{\alpha,N}\) are the differences \(k^{-\alpha}-(k+1)^{-\alpha}\) except for the terminal \(N^{-\alpha}\). Phase XIX's exact identity, recalled here, states
\[
\boxed{\operatorname{tr}H_{\alpha,N}=\sum_{d=1}^N d^{-\alpha}Q_\alpha(\lfloor N/d\rfloor).}\tag{T}
\]
The first diagonal element is \((H_{\alpha,N})_{11}=Q_\alpha(N)\) and \(H_{\alpha,N}\) is positive semidefinite. Therefore
\[
\frac{M(N)^2}{N^\alpha}\le Q_\alpha(N)\le\|H_{\alpha,N}\|\le\operatorname{tr}H_{\alpha,N}.
\tag{B}
\]

## Theorem 1: a spectral criterion for the Prime Number Theorem

For any **one fixed** \(0<\alpha<2\),
\[
\boxed{M(N)=o(N)\ \Longleftrightarrow\ \|H_{\alpha,N}\|=o(N^{2-\alpha}).}\tag{1}
\]
Thus the PNT is equivalent to this spectral decay at any one (or equivalently every) fixed exponent in \((0,2)\).

**Proof, PNT to spectral decay.** Let \(p=2-\alpha>0\). Assume \(M(k)=o(k)\). Since for \(k<N\),
\[
0<k^{-\alpha}-(k+1)^{-\alpha}\le\alpha k^{-\alpha-1},
\]
fixing \(\varepsilon>0\) and using \(|M(k)|\le\varepsilon k\) for all sufficiently large \(k\) gives
\[
Q_\alpha(n)=O_{\varepsilon,\alpha}(1)+O_\alpha(\varepsilon^2 n^p)=o(n^p).
\]
The trivial estimate \(|M(k)|\le k\) also gives \(Q_\alpha(n)\le C_\alpha n^p\) for *all* \(n\ge1\). Divide (T) by \(N^p\) to obtain the exact expression
\[
\frac{\operatorname{tr}H_{\alpha,N}}{N^p}
=\sum_{d\le N}\frac1{d^2}\frac{Q_\alpha(\lfloor N/d\rfloor)}{\lfloor N/d\rfloor^p}\left(\frac{d\lfloor N/d\rfloor}{N}\right)^p.
\]
For each fixed \(d\), the summand tends to zero as \(N\to\infty\), and all summands are dominated by \(C_\alpha/d^2\). Dominated convergence for series yields \(\operatorname{tr}H_{\alpha,N}=o(N^p)\); hence \(\|H\|=o(N^p)\).

**Proof, spectral decay to PNT.** If \(\|H_{\alpha,N}\|=o(N^p)\), inequality (B) gives \(M(N)^2\le N^\alpha o(N^p)=o(N^2)\). Thus \(M(N)=o(N)\). QED.

**Remark:** \(M(N)=o(N)\iff\mathrm{PNT}\) is a classical equivalence; the theorem is an algebraic recasting, not a new proof of the PNT.

## Theorem 2: exactly what a spectral power saving would imply

Fix \(1<\alpha<2\) and \(0<\eta<2-\alpha\). Set
\[
\theta=1-\eta/2>1/2,\qquad \beta=2-\alpha-\eta=2\theta-\alpha>0.
\]
Then
\[
\boxed{\|H_{\alpha,N}\|=O_{\alpha,\eta}(N^\beta)
\quad\Longleftrightarrow\quad M(N)=O_{\alpha,\eta}(N^\theta).}\tag{2}
\]

**Proof, operator bound to summatory bound.** By (B),
\(|M(N)|^2\le N^\alpha O(N^\beta)=O(N^{2\theta})\).

**Proof, summatory bound to operator bound.** Suppose \(|M(k)|\le Bk^\theta\) for all \(k\ge1\). With \(\beta=2\theta-\alpha>0\),
\[
\begin{aligned}
Q_\alpha(m)
&\le B^2\left(\alpha\sum_{k<m}k^{\beta-1}+m^\beta\right)\\
&\le B^2\left[1+\alpha\left(1+\beta^{-1}\right)\right]m^\beta.
\end{aligned}
\]
Insert this in (T). Since \(\alpha+\beta=2\theta>1\),
\[
\begin{aligned}
\|H_{\alpha,N}\|
&\le\operatorname{tr}H_{\alpha,N}\\
&\le B^2\left[1+\alpha(1+\beta^{-1})\right]
N^\beta\sum_{d\le N}d^{-\alpha-\beta}\\
&\le B^2\left[1+\alpha(1+\beta^{-1})\right]\zeta(2\theta)N^\beta.
\end{aligned}
\]
This proves the converse and provides an explicit operator constant. QED.

**Crucial logical limitation.** Establishing the spectral power saving in (2) for any fixed \(1<\alpha<2\), \(\eta>0\) would give a fixed power saving \(M(N)=O(N^{1-\eta/2})\). The classical Mellin representation then yields a zero-free half-plane \(\Re s>1-\eta/2\). Such a uniform fixed-power estimate is **not** obtained in Phase XXII. No implication in this section justifies assuming (2)'s hypotheses.

## Theorem 3: quantitative unconditional spectral saving from Korobov–Vinogradov

For any fixed \(0<\alpha<2\), there exist positive constants \(C_\alpha,c_\alpha,N_\alpha\) such that for \(N\ge N_\alpha\),
\[
\boxed{
\|H_{\alpha,N}\|\le\operatorname{tr}H_{\alpha,N}
\le C_\alpha N^{2-\alpha}\exp\!\left[-c_\alpha\frac{(\log N)^{3/5}}{(\log\log N)^{1/5}}\right].
}\tag{3}
\]
This is an unconditional **subpower saving**, not a fixed power saving. It reflects the classical Korobov–Vinogradov zero-free region, rather than improving it.

**Proof.** Define \(F(t)=t^{3/5}/(\log t)^{1/5}\) for large \(t\). The known unconditional bound supplies \(A,b>0\) with
\[
|M(x)|\le Ax\exp(-bF(\log x))
\]
for all sufficiently large \(x\). Put \(p=2-\alpha>0\). For large \(m\), split the quadratic energy defining \(Q_\alpha(m)\) into indices \(k\le\sqrt m\) and \(\sqrt m<k\le m\). For the former, the trivial bound \(|M(k)|\le k\) gives \(O_\alpha(m^{p/2})\). For the latter, \(F(\log k)\ge c_0 F(\log m)\) for some fixed \(c_0>0\) and large \(m\). The Korobov–Vinogradov bound gives
\[
Q_\alpha(m)\le C_\alpha m^p\exp(-b'F(\log m))
\]
for some \(b'>0\). Indeed \(m^{p/2}=o(m^p e^{-b'F(\log m)})\), since \(F(\log m)=o(\log m)\).

Now split the trace identity (T) at \(d=\sqrt N\). When \(d\le\sqrt N\), the quotient \(\lfloor N/d\rfloor\ge N^{1/3}\) for sufficiently large \(N\), and the improved bound for \(Q\) yields
\[
\sum_{d\le\sqrt N}d^{-\alpha}Q_\alpha(\lfloor N/d\rfloor)
\le C_\alpha N^p e^{-b''F(\log N)}\sum_{d\ge1}d^{-2}.
\]
When \(d>\sqrt N\), use the trivial bound \(Q_\alpha(m)\le C_\alpha m^p\) and \(\sum_{d>\sqrt N}d^{-2}=O(N^{-1/2})\), obtaining \(O_\alpha(N^{p-1/2})\). Because \(F(\log N)=o(\log N)\), this polynomially smaller term is absorbed by the displayed subpower saving. Adjusting the constants proves (3). QED.

## Falsification and independent finite checks

The reproducibility script \`experiments/riemann_phase22_spectral_pnt.py\` (and the CSV) verifies Phase XIX's exact trace identity with Python \`fractions.Fraction\` at nine \((N,\alpha)\) pairs \(N\in\{4,8,16\}\), \(\alpha\in\{1,2,3\}\). It compares trace formula (T) with the direct Gram trace, and checks the finite largest eigenvalue inequality for \(N=128,512\). The Möbius sieve runs through \(N=524288\); full matrices are not built at large \(N\).

Selected observed normalized traces are:

| \(N\) | \(\alpha=1.25\) | \(\alpha=1.50\) | \(\alpha=1.75\) |
|---:|---:|---:|---:|
| 128 | 0.1002407924 | 0.2251171924 | 0.5678272706 |
| 512 | 0.0401668088 | 0.1183006953 | 0.4085562380 |
| 8192 | 0.0057905127 | 0.0307283327 | 0.2060746201 |
| 524288 | 0.0002779525 | 0.0038826206 | 0.0729426567 |

Entries represent \(\operatorname{tr}H_{\alpha,N}/N^{2-\alpha}\), **not the operator norm itself**, although the latter is bounded above by the trace. Decline of these finite values is not a proof of convergence or RH; the theorem's limiting conclusion comes from the PNT.

## Evidence/novelty ledger

- **PROVED from standard prior results:** Theorem 1 (PNT equivalence); Theorem 2 (power-saving equivalence); Theorem 3 (subpower spectral estimate from classical Korobov–Vinogradov Mertens bound).
- **EXECUTED:** Nine exact Fraction trace comparisons, finite eigenvalue comparisons and deterministic sieve through \(2^{19}\).
- **UNPROVED:** Fixed spectral power saving at any \(1<\alpha<2\), stronger-than-classical zero-free region, RH.
- **PRIOR ART:** PNT–Mertens equivalence and the Korobov–Vinogradov bound are classical; related spectral/functional-analytic zero-free criteria exist. Nothing in this document asserts originality.

**Sources:**

1. Classical PNT–Mertens equivalence: https://citeseerx.ist.psu.edu/document?doi=14f880aae0fcf4c34cb226c631ce4389182305e0&repid=rep1&type=pdf (Theorem 1.4.3).
2. Nicol Leong, *On Some Effective Results Involving Zeros of the Riemann Zeta Function*, Cambridge Core: https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/on-some-effective-results-involving-zeros-of-the-riemann-zeta-function/8D885EAF542CEA62250CDF37719DC7B0 (quotes the Mertens/Korobov–Vinogradov exponential estimate).
3. Ghosh, Kremnizer, Noor and Santos, *Zero-free half-planes of the ζ-function via spaces of analytic functions*, Advances in Mathematics 455 (2024), DOI https://doi.org/10.1016/j.aim.2024.109872 (related operator/functional analysis prior art).