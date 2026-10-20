# Phase XXX — Collective prime interference via Walsh–Fourier analysis

**20 October 2026. Evidence:** exact finite/infinite identities, six rigorous infinite-integral sign certificates, 16 exact Walsh-vector comparisons, and four finite-ensemble diagnostics, all independently executed with standard-library Python. **Riemann Hypothesis remains unsolved; originality not established.**

## 1. Finite-prime Möbius reconstruction

Let \(P=\{p_1,\ldots,p_r\}\) be a finite set of distinct primes, let \(Q=\prod_{p\in P}p\), and put
\[
 f_P(x)=\sum_{n\le x,(n,Q)=1}\mu(n),\qquad (S_df)(x)=f(x/d),
\]
with functions zero below \(x=1\). For each subset \(A\subseteq P\), let \(d_A=\prod_{p\in A}p\) (\(d_\varnothing=1\)). By multiplicativity,
\[
 \boxed{M(x)=\sum_{A\subseteq P}(-1)^{|A|}S_{d_A}f_P(x).}\tag{1}
\]
For \(\alpha>2\), every weighted squared energy and covariance below converges absolutely from \(|f_P(x)|,|M(x)|\le x\). Use
\[
\langle g,h\rangle_\alpha=\alpha\int_1^\infty g(x)h(x)x^{-\alpha-1}\,dx,\qquad \mathcal E_\alpha(g)=\langle g,g\rangle_\alpha.
\]
Define the full multi-prime *diagonal baseline*
\[
 D_{\alpha,P}=\sum_{A\subseteq P}\mathcal E_\alpha(S_{d_A}f_P)
 =\prod_{p\in P}(1+p^{-\alpha})\mathcal E_\alpha(f_P),
\]
and the aggregate interference
\[
\boxed{\Delta_{\alpha,P}=\mathcal E_\alpha(M)-D_{\alpha,P}.}\tag{2}
\]
This is the natural generalization of Phase XXIX's two-prime interference, and sums **all** non-diagonal terms including higher-order interactions. Its sign is not prescribed by positivity of energy.

## 2. Exact Walsh–Fourier expansion for all interactions

Introduce independent prime signs \(\varepsilon=(\varepsilon_p)_{p\in P}\in\{\pm1\}^r\). Set
\[
 \varepsilon_A=\prod_{p\in A}\varepsilon_p,\qquad
 g_\varepsilon=\sum_{A\subseteq P}\varepsilon_A S_{d_A}f_P.
\]
The actual Möbius sequence is precisely the special vertex \(\varepsilon_p=-1\) for all \(p\in P\), while other vertices correspond to flipping the multiplicative signs on those selected primes, leaving the other Möbius prime values unchanged.

For each subset \(H\subseteq P\), write \(A\triangle H\) for symmetric difference and define the **real Walsh coefficient**
\[
\boxed{C_H=\sum_{A\subseteq P}\langle S_{d_A}f_P,S_{d_{A\triangle H}}f_P\rangle_\alpha.}\tag{3}
\]
Expanding the energy and applying Walsh orthogonality gives **three exact identities**:
\[
\boxed{\mathcal E_\alpha(g_\varepsilon)=\sum_{H\subseteq P}C_H\varepsilon_H,}\tag{4}
\]
\[
\boxed{\mathbb E_\varepsilon\mathcal E_\alpha(g_\varepsilon)=C_\varnothing=D_{\alpha,P},\qquad
\operatorname{Var}_\varepsilon\mathcal E_\alpha(g_\varepsilon)
 =\sum_{H\ne\varnothing}C_H^2,}\tag{5}
\]
and
\[
\boxed{\Delta_{\alpha,P}=\sum_{H\ne\varnothing}(-1)^{|H|}C_H.}\tag{6}
\]
No information is omitted: every pairwise and higher-order prime interaction appears in exactly one Walsh coefficient. The variance identity is a Parseval theorem for the Boolean cube, not a new Möbius bound.

**Finite-cutoff warning.** For \(\mathcal E_{\alpha,K}(f)=\alpha\int_1^K f(x)^2x^{-\alpha-1}dx\), equations (3)–(6) hold with the *same cutoff applied to every inner product*. The diagonal term becomes
\[
 C_\varnothing^{(K)}=\sum_{A\subseteq P}d_A^{-\alpha}\mathcal E_{\alpha,K/d_A}(f_P),
\]
which is **not** generally \(\prod_p(1+p^{-\alpha})\mathcal E_{\alpha,K}(f_P)\). The companion experiment uses the correctly cutoff-adjusted formula.

## 3. Six rigorous, infinite-integral counterexamples at alpha=3

**Theorem (computer-assisted with an explicit elementary infinite tail).** For the actual arithmetic Möbius function at exponent \(\alpha=3\), aggregate multi-prime interference has **both signs**, already for three, four and five primes:
\[
\begin{array}{lll}
\Delta_{3,\{2,3,5\}}<-1/4,& \Delta_{3,\{5,11,17\}}>1/100,\\
\Delta_{3,\{2,3,5,7\}}<-1/4,&\Delta_{3,\{5,11,13,23\}}>1/100,\\
\Delta_{3,\{2,3,5,7,31\}}<-1/4,&\Delta_{3,\{5,11,13,19,29\}}>1/100.
\end{array}\tag{7}
\]
These are sign conclusions for the **complete infinite integrals**, not merely a finite numerical scan. The prime sets were selected after an exploratory search, so these results are *existence counterexamples*, not statistical evidence about a typical prime set.

### Fully reproducible certificate

Put \(K=16,384\), \(L=10^{16}\). For integer exponent 3, the finite energy is exactly
\[
 \mathcal E_{3,K}(F)=\sum_{k=1}^{K-1}\big(k^{-3}-(k+1)^{-3}\big)F(k)^2.
\]
The script evaluates each rational term using integer floors and ceilings after scaling by \(L\), producing a rigorous rational interval with width at most \((K-1)/L\) per energy. It independently checks every sieve-produced \(\mu(n)\), \(n\le K\), using trial division. Since \(|F(x)|\le x\), for both \(F=M\) and \(F=f_P\),
\[
 0\le \mathcal E_3(F)-\mathcal E_{3,K}(F)\le 3/K.
\]
Thus, with \(A_P=\prod_{p\in P}(1+p^{-3})\),
\[
\boxed{|\Delta_{3,P}-[\mathcal E_{3,K}(M)-A_P\mathcal E_{3,K}(f_P)]|
\le 3(1+A_P)/K.}\tag{8}
\]
The enclosures below are rounded **outwards for display** from exact rational endpoints; the script uses rational comparisons rather than decimal claims:

| Prime set P | Lower bound for full Delta | Upper bound for full Delta | Certified inequality |
|---|---:|---:|---|
| (2,3,5) | -0.251728832118 | -0.250931957114 | < -1/4 |
| (5,11,17) | +0.010640632291 | +0.011376336390 | > +1/100 |
| (2,3,5,7) | -0.254713993336 | -0.253915862752 | < -1/4 |
| (5,11,13,23) | +0.010828957352 | +0.011564784782 | > +1/100 |
| (2,3,5,7,31) | -0.254102973624 | -0.253304828542 | < -1/4 |
| (5,11,13,19,29) | +0.010968422872 | +0.011704288964 | > +1/100 |

Since all intervals lie strictly on their stated sides, the conclusions in (7) follow from finite computations **plus proved global tail bounds**. No RH assumption is used. Exact rational endpoint strings are reproduced by `experiments/riemann_phase30_walsh.py`.

## 4. The random multiplicative benchmark does not prove deterministic RH

At a finite integer cutoff \(N\), if signs are randomized on **all primes** up to \(N\), independent Walsh character orthogonality gives
\[
\boxed{\mathbb E_\varepsilon Q_\alpha(N;g_\varepsilon)=
\sum_{n\le N}\frac{\mu(n)^2}{n^\alpha}.}\tag{9}
\]
This bounded expectation, for any fixed \(\alpha>1\), is the familiar random-multiplicative surrogate for the RH-equivalent first-column energy. However, the deterministic all-minus prime assignment is only one point of a sign cube of cardinality \(2^{\pi(N)}\). An average over that cube cannot by itself bound the energy at that one vertex. For finite prime sets, (7) proves the Möbius assignment may sit either above or below its randomized baseline. Neither ordinary Markov bounds nor unsigned second-moment bounds transfer automatically to the deterministic Möbius sequence.

The full variance identity (5) **does** quantify collective interference across all Walsh orders, but it neither forces the sign of the all-minus evaluation nor gives a new zero-free half-plane. A necessary future ingredient would be a deterministic arithmetic estimate for the particular alternating Walsh sum (6), better than an arbitrary-vertex bound.

### Executed cross-checks

The standard-library Python script `experiments/riemann_phase30_walsh.py` was run locally:
- **16,384/16,384** independently recomputed Möbius values matched.
- **Six** infinite-integral signs passed *exact* Fraction inequalities using equation (8).
- For \(P=(2,3,5),(3,5,7)\), \(N=32\), exact rational Gram-matrix and Walsh transform expansions matched all **16 of 16** sign assignments; exact ensemble means and variances agreed with equations (5).
- Four \(N=4096\) finite-ensemble computations matched the correctly cutoff-adjusted mean. For \(P=(5,11,17)\) and \(P=(5,11,13,23)\), the all-minus assignment had the largest energy among the 8 and 16 tested sign assignments, respectively. These are finite observations, not global results.

## 5. Literature and integrity

The Walsh transform and Rademacher random multiplicative functions are classical. Wintner-type random models and comparisons with Möbius are described in *Better than Squareroot Cancellation in Number Theory* (ICM 2026 invited lectures), https://doi.org/10.1137/25M1826366. Arithmetic sieve/RH reformulations with primes excluded have substantial prior art: E. Alkan, *Variations on criteria of Pólya and Turán for the Riemann hypothesis*, J. Number Theory 225 (2021), https://doi.org/10.1016/j.jnt.2021.01.004. This note does **not** claim that its algebraic Walsh decomposition is novel.

**Verdict:** rigorous refutation of universal beneficial sign for *entire* multi-prime interference (up to five primes), and an exact exhaustive accounting of all interactions by Walsh coefficients. **No new bound for fixed \(1<\alpha<2\), no new zero-free region, and no RH proof.**