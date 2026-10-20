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
- `certificates/` — finite integer-arithmetic C++ checks (original programs). These verify computations, not RH. The Phase XVII Python witness certificate checks an explicit nonmultiplicative countermodel.
- `experiments/` — additional C++ and Python cross-checks, including Phase XIV–XV moving-exponent experiments, the Phase XVI randomized-null audit, the Phase XVII dyadic spectrum Phase XVIII exact Gram checks, and Phase XIX spectral diagnostics.
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
