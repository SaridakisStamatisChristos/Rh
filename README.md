# RH — Möbius correlation research archive

**Status (20 October 2026): exploratory number-theory investigation, NOT a proof of the Riemann Hypothesis.** The hypothesis remains open. Nothing in this repository should be cited as an unconditional proof of RH, zero simplicity, or novelty without independent mathematical review.

## Main definitions

For the Möbius function `μ(n)`, let `M(N)=Σ_{n≤N} μ(n)`, and define

```text
a_n = μ(n) M(n−1)
C_α(N) = Σ_{n≤N} a_n / n^α
Q_α(N) = Σ_{m,n≤N} μ(m)μ(n) / max(m,n)^α
```

The exact arithmetic identity for `α>0` is

```text
Q_α(N) = Σ_{k<N} (k^(−α) − (k+1)^(−α)) M(k)^2 + M(N)^2 / N^α
       = Σ_{n≤N} μ(n)^2/n^α + 2 C_α(N).
```

This yields research targets involving upper bounds for `C_α(N)`. In particular, a uniform bound for every `α>1` arbitrarily close to 1 would imply RH. **No such unconditional bound has been proved here.**

## Contents

- `research/PHASES_01_09.md` — reconstructed chronology for early phases, including proofs, numerical observations, conjectures, and limitations.
- `research/riemann_phase10_proof.md` through `riemann_phase15_proof.md` — phase-specific notes, original research drafts retained for audit.
- `research/riemann_phase14_proof.md` — logarithmic moving-exponent sign-stability theorem.
- `research/riemann_phase15_proof.md` — Korobov–Vinogradov moving-exponent corridor and the fixed-exponent obstruction.
- `research/riemann_phase16_dyadic_cancellation.md` — dyadic counterexample, finite exponent-uniform proof, one-sided budget criterion, and randomized null model.
- `research/riemann_phase17_structural_barrier.md` — dyadic positive-budget criterion and explicit countermodel showing why generic Mertens bounds cannot force fixed-exponent negativity.
- `research/riemann_phase18_divisor_gram.md` — exact divisor Gram identity, random-sign null expectation and the precise sieve-to-prefix transfer obstruction.
- `research/riemann_phase19_operator_trace.md` — exact trace of the sieve-to-prefix operator and an explicit all-coefficient bound at exponent 2.
- `research/riemann_phase20_offdiagonal.md` — exact row sums, logarithmically growing negative aggregate off-diagonal contributions, and the critical-exponent spectral obstruction.
- `research/riemann_phase21_dilation_localization.md` — exact arithmetic-dilation symmetry, finite-coordinate no-go theorem, and unconditional high-divisor spectral compression.
- `research/riemann_phase22_spectral_pnt.md` — a spectral reformulation of the Prime Number Theorem, exact spectral power-saving equivalences, and an unconditional Korobov–Vinogradov subpower bound.
- `research/riemann_phase23_inverse_spectrum.md` — exact Möbius-free inverse, determinant, inverse trace asymptotic, unconditional smallest-eigenvalue estimate, and RH-equivalent condition-number criterion.
- `research/riemann_phase24_prime_dual.md` — exact odd-prime inverse Gram rank-one structure, uniformly normalized prime-sector eigenvalues, and an explicit Schur-complement energy lower bound.
- `research/riemann_phase25_odd_divisor.md` — weighted-GCD factorization on all odd inverse-Gram coordinates, dimension-uniform diagonal conditioning for fixed alpha>1, and sharp odd-composite Schur lower bound.
- `research/riemann_phase26_parity_residual.md` — independent Phase XXV odd-GCD audit, sharp parity-pair decomposition, and an RH-equivalent nonnegative residual with finite diagnostics; `experiments/riemann_phase26_parity_residual.py` contains the reproducible exact tests.
- `research/riemann_phase27_prime_dilation.md` — finite prime-excision reconstruction, sharp prime-dilation Hilbert-operator norms, and the Euler-product obstruction at exponent 2.
- `experiments/riemann_phase27_prime_dilation.py` — executed exact finite reconstructions and weighted norm tests; accompanying CSV diagnostics are in `experiments/riemann_phase27_energy.csv` and `experiments/riemann_phase27_operator_norms.csv`.
- `research/riemann_phase28_prime_covariance.md` — exactly certified infinite Möbius prime-step covariances of opposite signs, a finite energy sign reversal inside (1,2), and an exact signed all-prime telescoping energy identity.
- `experiments/riemann_phase28_prime_covariance.py` — pure-Python exact rational covariance, analytic-tail, Möbius reconstruction, and independent double-sum checks.
- `research/riemann_phase28_cross_prime_signs.md` — exact cross-prime energy identity, rigorous infinite counterexamples to universal positive correlation, and a Mellin-frequency explanation.
- `research/riemann_phase29_two_prime_interference.md` — exact two-prime energy/diamond identities and certified opposite signs for full mixed and aggregate interference at exponent 3.
- `experiments/riemann_phase29_two_prime.py` — independent 4,096-point Möbius check, rational 27-case finite identity audit and four exact-infinite-integral sign tests; associated [six-pair enclosures](experiments/riemann_phase29_sign_enclosures.csv).
- `experiments/riemann_phase28_cross_prime.py` — independently verified 1,024-term Möbius sieve, 36 rational bilinear checks, integer-rounded sign certificates and elementary infinite-tail bounds.
- `research/riemann_phase30_walsh_collective.md` — exact all-orders Walsh expansion of prime interference, bounded random-sign variance and factorial interaction tail, random multiplicative energy expectation, and deterministic RH obstruction.
- `experiments/riemann_phase30_walsh.py` — 56 exact Walsh-energy comparisons, independent Möbius coefficient verification and rigorous six-prime-set aggregate sign certification; `experiments/riemann_phase30_aggregate_enclosures.csv` stores exact rational endpoints.
- `certificates/` — finite integer-arithmetic C++ checks (original programs). These verify computations, not RH. The Phase XVII Python witness certificate checks an explicit nonmultiplicative countermodel.
- `experiments/` — additional C++ and Python cross-checks, including Phase XIV–XV moving-exponent experiments, the Phase XVI randomized-null audit, the Phase XVII dyadic spectrum Phase XVIII exact Gram checks, Phase XIX spectral diagnostics, Phase XXI compressed-matrix tests, and Phase XXII normalized-trace diagnostics.
- `research/STATUS_AND_AUDIT.md` — verification scope, hypotheses, source dependencies and next work.

## Reproduction

```bash
g++ -std=c++17 -O3 -Wall -Wextra certificates/riemann_phase12_alpha2_certificate.cpp -o /tmp/rh_phase12
/tmp/rh_phase12

g++ -std=c++17 -O3 -Wall -Wextra certificates/riemann_phase13_sign_window.cpp -o /tmp/rh_phase13
/tmp/rh_phase13

python -m pip install mpmath
python experiments/riemann_spectral_budget_audit.py
```

The larger C++ tests may require hundreds of megabytes of memory. Python spectral calculations are numerical diagnostics only.

## Literature and attribution

- Johnston, Leong and Tudzi, *New Bounds and Progress Towards a Conjecture on the Summatory Function of (−2)^Ω(n)*, https://doi.org/10.1080/10586458.2025.2483942 (explicit Mertens bounds).
- Gordon V. Chavez, *Correlations of the Möbius and Liouville functions with their partial sums*, https://doi.org/10.1142/S1793042126500934 (prior correlation research).
- Clay Mathematics Institute, Riemann Hypothesis: https://www.claymath.org/millennium/riemann-hypothesis/

## Research integrity

The notes originate from a sequence of AI-assisted mathematical explorations. Some derivations remain provisional; published estimates must be checked in their original sources, and numerical outputs do not replace independent proof review. Any apparent novelty requires a literature audit.

No software or content license is granted by this repository unless one is added explicitly.
