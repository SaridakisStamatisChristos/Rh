# Investigation chronology, Phases I–IX

**Editorial reconstruction of this conversation, not a verbatim transcript.** Date: 19–20 October 2026. This is mathematical research in progress; **RH was not proved**. The displayed equivalent conditions are not independent theorems resolving the core problem.

## I. Initial Möbius reduction

Set \(M(x)=\sum_{n\le x}\mu(n)\). For \(\Re s>1\),

\[
1/\zeta(s)=\sum_{n\ge1}\mu(n)n^{-s}
=s\int_1^\infty M(x)x^{-s-1}\,dx.
\]

The classical Littlewood criterion is
\[
\mathrm{RH}\iff M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
\]
The forward and reverse implications require the standard analytic continuation and the functional equation; neither supplies the missing bound.

## II. Quadratic-energy formulation

For \(\alpha>0\) define
\[
Q_\alpha(N)=\sum_{m,n\le N}\frac{\mu(m)\mu(n)}{\max(m,n)^\alpha}.
\]
The exact identities
\[
Q_\alpha(N)
=\sum_{k<N}\big(k^{-\alpha}-(k+1)^{-\alpha}\big)M(k)^2+\frac{M(N)^2}{N^\alpha}
=\sum_{n\le N}\frac{\mu(n)^2}{n^\alpha}
+2\sum_{n\le N}\frac{\mu(n)M(n-1)}{n^\alpha}
\]
show positivity and expose signed Möbius correlation. Uniform boundedness of \(Q_{1+2\varepsilon}(N)\) for every \(\varepsilon>0\) is equivalent to RH. This is a reformulation, not a proof.

## III. Mean-square and quantitative zero-free criteria

The relation \(S(X)=\sum_{n\le X}M(n)^2\) gives another equivalent condition:
\(S(X)=O_\delta(X^{2+\delta})\) for every \(\delta>0\).
A growth bound \(Q_{1+2\varepsilon}(N)=O(N^\kappa)\) implies a zero-free half-plane
\(\Re s>1/2+\varepsilon+\kappa/2\).
No new unconditional exponent gain was obtained.

A proposed signed-correlation conjecture is
\[
C_\varepsilon(N)=\sum_{n\le N}\frac{\mu(n)M(n-1)}{n^{1+2\varepsilon}}\le0.
\]
Its sufficiency for RH does **not** establish its truth.

## IV. Large-exponent sign bound and logarithmic scaling

A direct estimate gave an elementary sign theorem in the easy range \(\varepsilon\ge1\); later certified improvements supersede it.
With \(\varepsilon_N=1/(2\log N)\), the scale-dependent energy \(Q_{1+1/\log N}(N)=N^{o(1)}\) is equivalent to RH.
No such bound was proved.

## V. Fixed-exponent correlation

Define
\[
C(N)=\sum_{n\le N}\frac{\mu(n)M(n-1)}n.
\]
If \(C(N)\le0\) for all \(N\ge2\), the energy identity yields
\[
|M(N)|\le\sqrt{N(1+\log N)},
\]
so RH follows. More flexibly, one-sided bounds \(C(N)=O_\delta(N^\delta)\) for all \(\delta>0\) are equivalent to RH. Numeric experiments do not establish either claim for arbitrary \(N\).

The unweighted correlation \(\sum_{n\le N}\mu(n)M(n-1)=\frac12(M(N)^2-\sum_{n\le N}\mu(n)^2)\) can be positive; the stronger partial-sum sign approach is invalid.

## VI. Forced excursions and energy growth

Define the energy
\[
E(X)=\int_1^X\frac{M(x)^2}{x^2}\,dx.
\]
If a zero exists with real part \(\beta>1/2\), the correlation must have arbitrarily large positive excursions at powers below \(2\beta-1\). A Laplace-transform argument also relates growth of \(E(X)\) to contributions \(1/|\rho\zeta'(\rho)|^2\) from simple critical-line zeros. These are conditional zero-detection statements, not zero exclusions.

## VII. Weak Mertens, dyadic minima and zero simplicity

Hypothetical uniform negativity of \(C(N)\) yields the weak-Mertens-type bound
\[
E(X)\le(6/\pi^2)\log X+O(1),
\]
which would imply RH and simplicity of all nontrivial zeros. A dyadic-minimum formulation controls \(\min_{X\le N\le2X}C(N)\) (one-sided, subpower upper bounds), giving an equivalent RH criterion. None of these assumptions was proved.

## VIII. Multiple-zero obstruction

For a hypothetical zero \(\rho=1/2+i\gamma\) of multiplicity \(m\ge2\), Laplace-transform estimates produce conditional energy growth on order at least \((\log X)^{2m-1}\) along a sequence. This would force large positive correlation intervals. Therefore an upper bound \(C(N)=o((\log N)^3)\) from above would imply RH and simplicity. The sufficient hypothesis remains open.

## IX. Positive-part majorant and finite certificate

For \(a_n=\mu(n)M(n-1)\), the weighted-sign proof split the positive terms from \(a_2=-1\), using a finite integer-arithmetic calculation through \(K=2^{20}\) plus the simple tail \(|a_n|\le n-1\).

This yielded sign negativity for \(\alpha=1+2\varepsilon\ge9/4\) (\(\varepsilon\ge5/8\)), assuming the certificate and explicit inequality checks. See \`certificates/riemann_phase9_weighted_sign.cpp\`.

The method deliberately throws away negative correlations, so it cannot itself reach the RH-critical \(\alpha\downarrow1\).

## X–XIII

Full phase-specific Markdown files and finite certificates are included separately. The strongest archived sign bound uses the published explicit Mertens estimate to cover all \(\alpha\ge2\), and a shrinking window of exponents just below 2 at each finite \(N\).

## Source provenance and caveats

- This chronology is reconstructed from AI-assisted conversation responses. It is **not** a peer-reviewed manuscript.
- Some numerical figures in the discussion were obtained by floating point and should not be treated as rigorous certifications.
- Finite exact-arithmetic programs certify only their stated finite inequalities; global theorems additionally depend on analytic estimates.
- Related Möbius–Mertens correlations were studied by Gordon V. Chavez (2024 preprint; 2026 journal publication): https://doi.org/10.1142/S1793042126500934.
- Research question: can signed cancellations, rather than absolute-value majorants, yield a fixed exponent \(1<\alpha<2\), or the full critical regime \(\alpha\downarrow1\)?
