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

## Phase XIV (20 October 2026)

An unconditional moving-exponent stability lemma was proved, assuming the cited Mertens bound and Phase XII finite certificate: if `delta_N >= 0` and `N^(delta_N) = o(log N)`, then `C_(2-delta_N)(N) -> C_2(infinity) < -1/10`. A particularly useful instance is `delta_N = c log(log N)/log N` for any fixed `0<c<1`. The proof and finite illustrative experiment are in `research/riemann_phase14_proof.md` and `experiments/riemann_phase14_loglog_corridor.cpp`. This is **not** a result for fixed `alpha<2` and does not improve known zero-free regions. Analytic proof not peer-reviewed; the numerical experiment is only illustrative.

## Phase XV (20 October 2026)

**Proof status: analytical derivation, not peer-reviewed; not a proof of RH.** By combining the unconditional Korobov–Vinogradov estimate `M(x) = O(x exp(-κ (log x)^(3/5)/(loglog x)^(1/5)))` (some κ>0) with the existing Phase XII global `C_2(N)<-1/10` certificate, the proof shows: for any nonnegative sequence `δ_N = o((log N)^(-2/5)(loglog N)^(-1/5))`, one has `C_(2-δ_N)(N) -> C_2(∞)<-1/10`, uniformly in exponent over `[2-δ_N,2]`. An accessible example is `δ_N=1/sqrt(log N)`. The proof is in `research/riemann_phase15_proof.md` and the C++ finite diagnostic is in `experiments/riemann_phase15_korobov_corridor.cpp`. A local C++17 compile-and-run passed, including a separate trial-division Möbius check through n=2000. This is a standard transfer of a known cancellation estimate, **not** a fixed exponent <2 and **not** an improvement of the known zeta zero-free region. Novelty not established.


## Phase XVI (20 October 2026)

**Adversarial finding:** A universal nonpositive dyadic correlation-block claim is **false**. For every real \(\alpha>0\), the block \(4<n\le8\) equals \(5^{-\alpha}-2\,6^{-\alpha}+7^{-\alpha}>0\); at \(\alpha=1\) this is \(1/105\).

**Finite rigor:** The C++17 scaled-integer bound independently checks all \(C_1(N)<-299/1000\) for \(2\le N\le10^7\), with a separate trial-division Möbius check through \(n=2000\). Abel summation **proves** that every \(C_\alpha(N)<-(299/1000)2^{1-\alpha}\) in this finite range for every real \(\alpha\ge1\). This is not an unbounded-N proof.

**Dyadic criterion:** For each fixed \(\alpha>1\), summability of the positive dyadic block contributions gives a zero-free half-plane \(\Re(s)>\alpha/2\). Requiring this condition for every \(\alpha>1\) is equivalent to RH. Thus the criterion reformulates the unsolved obligation without assuming falsely that each block is negative.

**Randomized null model:** On the actual squarefree support, independent Rademacher signs yield a martingale difference correlation, with zero expectation and exact variance \(\sum_{n\le N}\mu(n)^2 S(n-1)n^{-2\alpha}\). It converges in \(L^2\) and almost surely for \(\alpha>1\), but this does not transfer to the deterministic arithmetic Möbius signs. A fixed-seed experiment with 4,000 replications at \(N=50,000,\alpha=3/2\) showed sample variance \(0.30219501\), against theoretical \(0.30020787\).

Sources: \`research/riemann_phase16_dyadic_cancellation.md\`, \`experiments/riemann_phase16_experiment.cpp\`. The exact arithmetic certificate executed locally using \`g++ -std=c++17 -O3 -Wall -Wextra -Werror\`; no CI claim. **RH remains open.** Novelty has not been established.

## Phase XVII (20 October 2026)

**Proved analytically, but not peer-reviewed or claimed novel:**
- RH is equivalent to finiteness, for every alpha>1, of the cumulative positive dyadic-shell budget sum_j max(C_alpha(2^(j+1))-C_alpha(2^j),0). This remains an equivalent criterion, NOT a proof of RH.
- A hypothetical zero at beta>1/2 forces unbounded polynomially normalized positive budgets at every alpha in (1,2 beta), for exponents below 2 beta-alpha.
- An explicit NONMULTIPLICATIVE surrogate b_n in {-1,0,1} satisfies |sum_{n<=x} b_n| <= x/(log x)^2 for all x>1, but has arbitrarily large positive fixed-alpha correlation for any 1<alpha<2. For alpha=3/2, R=10^30 and H=R/20000, an exact rational lower bound makes correlation >9. This defeats a proof using ONLY the summatory envelope and coefficient range; it does not disprove any claim specifically about the multiplicative Mobius function.

**Locally executed:** A GCC C++17 -O3 -Wall -Wextra -Werror computation examined dyadic shell contributions through N=2^23 at alpha 1, 1.25, 1.5, 1.75 and 2. Exactly two shells, (4,8] and (16,32], were positive at all five sampled exponents; other tested shells were nonpositive. A Python fractions.Fraction certificate verified the explicit surrogate example (PASS). Both are finite demonstrations, not an all-N sign proof.

Files: research/riemann_phase17_structural_barrier.md, certificates/riemann_phase17_witness.py, experiments/riemann_phase17_dyadic_spectrum.cpp, and experiments/riemann_phase17_dyadic_spectrum.csv.

**Outstanding:** exploit arithmetic multiplicativity or another Mobius-specific principle to control the positive budget for fixed 1<alpha<2. RH remains open.
