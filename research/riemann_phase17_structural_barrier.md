# Phase XVII — Dyadic positive budget and the limits of generic Mertens cancellation

**20 October 2026 — Research status:** two elementary deductions with full arguments, one finite diagnostic, and an exact arithmetic countermodel. **Not a solution to RH; no novelty claim.** See Gordon V. Chavez, *Correlations of the Möbius and Liouville functions with their partial sums* (2026), DOI https://doi.org/10.1142/S1793042126500934 for substantially related prior research.

## 1. Definitions and exact energy identity

Let `mu` denote the actual Möbius function, `M(x) = sum_{n<=x} mu(n)`, `a_n = mu(n) M(n-1)`, and, for alpha > 0,

\[
 C_\alpha(N)=\sum_{n\le N}\frac{a_n}{n^\alpha},\quad
 Q_\alpha(N)=\sum_{m,n\le N}\frac{\mu(m)\mu(n)}{\max(m,n)^\alpha}.
\]

Set

\[
 E_\alpha(N)=\sum_{k=1}^{N-1}(k^{-\alpha}-(k+1)^{-\alpha})M(k)^2,\qquad
 B_\alpha(N)=\frac{M(N)^2}{N^\alpha},\qquad
 S_\alpha(N)=\sum_{n\le N}\frac{\mu(n)^2}{n^\alpha}.
\]

Exact summation by parts gives

\[
 Q_\alpha(N)=E_\alpha(N)+B_\alpha(N)=S_\alpha(N)+2C_\alpha(N).
\]

Here `E_alpha` is nonnegative and nondecreasing, while `B_alpha >= 0`. For alpha > 1,

\[
S_\alpha(\infty)=\frac{\zeta(\alpha)}{\zeta(2\alpha)}<\infty.
\]

## 2. Dyadic positive-budget criterion

For j >= 0 define the signed shell increment

\[
D_{\alpha,j}=C_\alpha(2^{j+1})-C_\alpha(2^j)
=\sum_{2^j<n\le2^{j+1}}\frac{\mu(n)M(n-1)}{n^\alpha},
\]

and the cumulative positive budget

\[
P_\alpha(J)=\sum_{j=0}^{J-1}\max(D_{\alpha,j},0).
\]

**Proposition (exactly equivalent reformulation).**

\[
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
 \text{for every }\alpha>1,\ \sum_{j\ge0}D_{\alpha,j}^{+}<\infty.}
\]

This is an equivalent condition and does not resolve RH.

### Sufficiency

Since `C_alpha(1)=0`, telescoping and dropping negative block contributions give

\[
 C_\alpha(2^J)\le P_\alpha(J).
\]

Therefore

\[
\boxed{0\le E_\alpha(2^J)\le
\frac{\zeta(\alpha)}{\zeta(2\alpha)}+2P_\alpha(J).}
\tag{1}
\]

If the positive budget is finite, monotonicity of `E_alpha` gives

\[
\sum_{k\ge1}\frac{M(k)^2}{k^{\alpha+1}}<\infty,
\]

because the positive coefficient `k^{-alpha}-(k+1)^{-alpha}` is comparable to `k^{-alpha-1}`. Suppose this holds for every alpha > 1. Given sigma > 1/2, choose `1 < alpha < 2 sigma`. Cauchy–Schwarz gives

\[
\sum_{k\ge1}\frac{|M(k)|}{k^{\sigma+1}}
\le\left(\sum_{k\ge1}\frac{M(k)^2}{k^{\alpha+1}}\right)^{1/2}
\left(\sum_{k\ge1}k^{\alpha-2\sigma-1}\right)^{1/2}<\infty.
\]

The resulting locally normally convergent Mellin representation of `1/zeta(s)` precludes zeta zeros in `Re(s)>1/2`. Functional-equation symmetry yields RH.

### Necessity

RH implies the classical estimate `M(x)=O_eta(x^(1/2+eta))` for every eta > 0. Fix alpha > 1 and choose `0<eta<(alpha-1)/2`. Then `E_alpha(infinity)<infinity` and

\[
\sum_{j\ge0}B_\alpha(2^{j+1})<\infty.
\]

The exact shell decomposition is

\[
2D_{\alpha,j}=\big(E_\alpha(2^{j+1})-E_\alpha(2^j)\big)
+\big(B_\alpha(2^{j+1})-B_\alpha(2^j)\big)
-\big(S_\alpha(2^{j+1})-S_\alpha(2^j)\big).
\]

Since `S_alpha` increases and `B_alpha >= 0`,

\[
2D_{\alpha,j}^{+}\le
E_\alpha(2^{j+1})-E_\alpha(2^j)+B_\alpha(2^{j+1}).
\]

The right-hand side is summable in `j`. This proves necessity.

### Quantitative zero-detection consequence

Suppose a zeta zero has real part `beta>1/2`. For every `1<alpha<2 beta` and every `0<=kappa<2 beta-alpha`,

\[
\boxed{\limsup_{J\to\infty}2^{-\kappa J}P_\alpha(J)=+\infty.}
\]

Otherwise (1) implies `E_alpha(X)=O(X^kappa)` by choosing the next dyadic endpoint. Weighted dyadic Cauchy–Schwarz then extends `1/zeta(s)` holomorphically for `Re(s)>(alpha+kappa)/2`, contradicting the hypothesized zero. This is a conditional consequence, not evidence that such a zero exists.

## 3. Explicit countermodel to generic-Mertens-bound sign arguments

**Countermodel theorem.** For every fixed `1<alpha<2`, there exist finitely supported sequences `b_n in {-1,0,1}` with

\[
|B(x)|=\left|\sum_{n\le x}b_n\right|\le\frac{x}{(\log x)^2}\quad(x>1),
\]

and some `N` for which the correlation

\[
C_\alpha^{(b)}(N)=\sum_{n\le N}\frac{b_nB(n-1)}{n^\alpha}
\]

is arbitrarily large and positive.

**Construction:** Take `b_1=1, b_2=-1`, and `b_n=0` for `3<=n<=R`. Let `H=floor(R/(log R)^2)`. Set `b_n=1` for `R<n<=R+H`, `b_n=-1` for `R+H<n<=R+2H`, and `b_n=0` thereafter. The summatory function starts at 0, increases to H, then returns to 0. For `x>=R` we have `|B(x)|<=H<=R/(log R)^2<=x/(log x)^2` because `x/(log x)^2` increases when `x>e^2`. On `(1,2)`, `B(x)=1` and the same bound holds because the global minimum of `x/(log x)^2`, for `x>1`, is `e^2/4>1`. Outside these regions B=0.

For the nonzero excursion, define `D_alpha(R,H)` as its correlation contribution. The sum of squared intermediate heights equals `(2H^3+H)/3`, giving

\[
\boxed{D_\alpha(R,H)\ge
\frac{\alpha(2H^3+H)}{6(R+2H)^{\alpha+1}}-\frac{H}{R^\alpha}.}
\tag{2}
\]

With `H~R/(log R)^2` and `1<alpha<2`, the first term grows on the scale `R^(2-alpha)/(log R)^6 -> infinity` while the second is `O(R^(1-alpha)/(log R)^2) -> 0`. Including the fixed initial contribution `-1/2^alpha` still leaves the total correlation tending to +infinity.

**Completely explicit instance at alpha=3/2:** Choose `R=10^30`, `H=R/20000=5*10^25`. Since `log(10)<7/3`, `log R<70`, hence `H<R/(log R)^2`. Also `R+2H<2R` and `2^(5/2)<6`. From (2),

\[
D_{3/2}(R,H) > \frac{H^3}{12R^{5/2}}-\frac{H}{R^{3/2}}
=\frac{125}{12}-\frac{1}{20000\cdot10^{15}}.
\]

Therefore

\[
\boxed{C_{3/2}^{(b)}(R+2H)>9.}
\]

The attached Python script verifies every rational comparison using exact integers and fractions; no enumeration of 10^30 integers is needed.

**Scope of countermodel:** These surrogate sequences are **not multiplicative** and are **not** the Möbius function. The result does **not** refute Möbius sign conjectures or RH. It establishes that upper bounds on the magnitude of summatory functions—even the strong `x/log^2(x)` envelope—plus coefficient range `{-1,0,1}` cannot alone imply a fixed-alpha sign theorem for `1<alpha<2`. A successful proof must use more structure than the generic envelope.

## 4. Finite numerical diagnostic on the actual Möbius function

C++17 sieve with `-O3 -Wall -Wextra -Werror` computed dyadic block correlations through `N=2^23=8,388,608` at alpha `1`, `1.25`, `1.5`, `1.75`, `2`.

At **each** sampled exponent there were **two positive dyadic shells**: `X=4` (the exact strict-convexity example) and `X=16`. Every other tested shell from `X=1` through `X=2^22` was nonpositive at these five exponents. This is descriptive finite numerical evidence, **not a sign certificate for all real alpha or all N**.

The sums of positive shell contributions through this cutoff were approximately:

| alpha | Positive budget P_alpha(23) |
|---:|---:|
| 1.00 | 0.1043230658463 |
| 1.25 | 0.0494177568351 |
| 1.50 | 0.0251508845072 |
| 1.75 | 0.0139264287025 |
| 2.00 | 0.0083828393637 |

The companion C++ program and output CSV reproduce these values. Finite budgets can grow beyond the cutoff, so they do not prove summability or RH.

## 5. Conclusion / next proof obligation

- **Proved:** a dyadic-positive-budget RH equivalence (reformulation); a quantitative conditional zero-detection criterion; and an explicit countermodel establishing the insufficiency of generic Mertens bounds for fixed-exponent signs.
- **Executed:** exact rational surrogate witness and finite Möbius dyadic spectrum.
- **Not proved:** bounded positive dyadic budget for the real Möbius function at any fixed `1<alpha<2`; therefore no new zero-free half-plane and no RH proof.
- **Next mathematical target:** exploit multiplicativity or a new arithmetic cancellation principle that rules out long squarefree Möbius-correlated excursions of the kind the surrogate sequence can manufacture.

This file is an original AI-assisted research note, not peer-reviewed and not claimed novel. Prior art: Chavez 2026, https://doi.org/10.1142/S1793042126500934.