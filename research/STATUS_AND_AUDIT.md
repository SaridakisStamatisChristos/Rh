# Research status and verification ledger

Date: 20 October 2026. **Status: preliminary research archive. NOT an RH proof.**

## Scope

The repository contains calculations and draft mathematical arguments from a thirteen-phase exploration of Möbius-sum correlations. The results are deliberately separated into: exact algebraic identities, conditional RH-equivalent criteria, published external estimates, finite computations, and open arithmetic hypotheses.

### Basic exact identity

For \(\alpha>0\),
\[
Q_\alpha(N)=\sum_{k<N}(k^{-\alpha}-(k+1)^{-\alpha})M(k)^2+M(N)^2/N^\alpha
=\sum_{n\le N}\mu(n)^2/n^\alpha+2C_\alpha(N).
\]
It follows that \(Q_\alpha(N)\ge0\). Statements needing bounded \(Q_\alpha(N)\) near \(\alpha=1\) are conditional and not proved here.

### Computational verification in current archival pass

The following original C++ programs were freshly compiled with GCC C++17, \`-O3 -Wall -Wextra\`, and returned passing internal checks:

| File | Check | Scope |
| --- | --- | --- |
| \`certificates/riemann_phase9_weighted_sign.cpp\` | PASS | Finite positive majorant through \(2^{20}\) |
| \`certificates/riemann_phase10_weighted_sign_certificate.cpp\` | PASS | Finite bound through \(2^{25}\), rational tail parameters |
| \`certificates/riemann_phase12_alpha2_certificate.cpp\` | PASS | Finite \(C_2\) and positive sums through \(2^{25}\); arithmetic comparison for the published-bound tail |
| \`certificates/riemann_phase13_sign_window.cpp\` | PASS | Finite \(C_2\), absolute sums through \(2^{25}\), rational sign-window parameters |

Other included experiments were preserved but not all independently rerun in the archival pass. Binary outputs are omitted; build from source.

### External analytical input

The proof notes for Phases XII–XIII use a published bound
\[
|M(x)|\le2.91890x/(\log x)^2\quad(x>1).
\]
See Johnston–Leong–Tudzi, *Experimental Mathematics*, DOI https://doi.org/10.1080/10586458.2025.2483942. The repository does **not** independently prove this external theorem; readers should verify its hypotheses and constant against the publication.

### Computational-vs-mathematical separation

- Exact integer ceiling/floor checks are a finite certificate of rational sums under their implementation assumptions.
- A finite sign test at \(10^7\) or even \(10^8\) **does not** imply an all-\(N\) statement.
- Numerical zeta zeros and derivatives calculated with \`mpmath\` are diagnostic and not interval-certified.
- The range \(\alpha\ge2\) does not yield a new zero-free strip for \(\zeta(s)\).
- The Phase XIII window \(\alpha\ge2-1/(8\log N)\) shrinks with \(N\), and does not establish a fixed range \(1<\alpha<2\).
- All novel-looking statements require independent mathematical review and a prior-art search before publication.

### Highest-value open tasks

1. Obtain a fixed-\(\alpha<2\) **signed** correlation bound, not a positive-only bound.
2. Independently inspect each analytic tail derivation and the relation to known zero-free regions.
3. Independently certify critical computations if they are used in a formal proof (including exact input data and platform assumptions).
4. Compare with prior work on Möbius–Mertens correlations, weak Mertens conjectures and zeta-zero multiplicity.

### Sources

- Clay Mathematics Institute, *Riemann Hypothesis*: https://www.claymath.org/millennium/riemann-hypothesis/
- Gordon V. Chavez, *Correlations of the Möbius and Liouville functions with their partial sums*, https://doi.org/10.1142/S1793042126500934.
- Johnston, Leong, Tudzi, *New Bounds and Progress Towards a Conjecture on the Summatory Function of (−2)^Ω(n)*, https://doi.org/10.1080/10586458.2025.2483942.

### License status

This public repository has no software license yet. Public visibility alone does not grant permission to reuse the code; licensing remains a deliberate future decision.
