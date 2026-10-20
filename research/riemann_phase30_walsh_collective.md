# Phase XXX — Exact multi-prime Walsh expansion, uniformly bounded ensemble variance and deterministic RH obstruction

**20 October 2026 — evidence status:** Fully derived algebraic formulas; 56 independently executed exact rational Walsh/energy comparisons; six computer-assisted rigorous enclosures of complete infinite-energy interference integrals, with one independent sieve cross-check. This phase produces **no improved deterministic bound on the Möbius function, no new zero-free region and no RH proof**. The random multiplicative function model dates to Wintner (1944), and its classical square-root cancellation theory is substantially stronger than what we prove here. Novelty of the particular bookkeeping formulas is **not established**.

## 1. Mathematical setup

For \(\alpha>0\), let \(\mathcal H_\alpha=L^2([1,\infty),\alpha x^{-\alpha-1}dx)\), real-valued for simplicity; functions are extended by zero below 1. Put \(S_df(x)=f(x/d)\), and write
\[
\langle f,g\rangle_\alpha=\alpha\int_1^\infty f(x)g(x)x^{-\alpha-1}dx,
\quad\|S_df\|_\alpha=d^{-\alpha/2}\|f\|_\alpha.
\]
Take a finite set of primes \(P\), arbitrary \(f\in\mathcal H_\alpha\), and independent or deterministic signs \(\varepsilon_p\in\{-1,+1\}\). For \(U\subseteq P\), define \(d_U=\prod_{p\in U}p\), \(\varepsilon_U=\prod_{p\in U}\varepsilon_p\), and \(d_\varnothing=\varepsilon_\varnothing=1\). Let
\[
G_\varepsilon=\prod_{p\in P}(I-\varepsilon_p S_p)f,
\qquad \mathscr E_\alpha(\varepsilon)=\|G_\varepsilon\|_\alpha^2.
\]
No assumption on RH is used anywhere in the finite-prime algebra.

## 2. Exact full Walsh interaction identity (PROVED)

**Theorem.** The energy is a multilinear polynomial in the prime signs,
\[
\boxed{\mathscr E_\alpha(\varepsilon)=\sum_{U\subseteq P}c_U\varepsilon_U,}
\]
where
\[
\boxed{c_U=(-1)^{|U|}\left(\prod_{p\in P\setminus U}(1+p^{-\alpha})\right)
\sum_{A\subseteq U}\langle S_{d_A}f,S_{d_{U\setminus A}}f\rangle_\alpha.}
\tag{1}
\]
In particular, the constant term is
\[
\boxed{c_\varnothing=\|f\|_\alpha^2\prod_{p\in P}(1+p^{-\alpha}).}
\tag{2}
\]

**Proof.** Expand \(G_\varepsilon=\sum_{S\subseteq P}(-1)^{|S|}\varepsilon_S S_{d_S}f\) and then square the norm. The coefficient of \(\varepsilon_U\) collects ordered pairs \((S,T)\) with symmetric difference \(S\triangle T=U\). Such pairs have \(S=R\cup A,\ T=R\cup(U\setminus A)\) for \(R\subseteq P\setminus U,\ A\subseteq U\). Their sign is \((-1)^{|U|}\), and the inner product is \(d_R^{-\alpha}\langle S_{d_A}f,S_{d_{U\setminus A}}f\rangle_\alpha\), by common-dilation scaling. Summing over \(R\) produces \(\prod_{p\in P\setminus U}(1+p^{-\alpha})\), proving (1). For \(U=\varnothing\) the remaining inner product is \(\|f\|^2\). \(\square\)

For \(|P|=2\), (1) reduces to the signed-interference formula of Phase XXIX. The total multi-prime interaction is \(\sum_{U\ne\varnothing}c_U\varepsilon_U\); **it does not have a general favorable sign**.

## 3. Exact ensemble mean and variance (PROVED)

Assume the \(\varepsilon_p\) are independent symmetric Rademacher variables. Walsh characters are orthonormal: \(\mathbb E[\varepsilon_U\varepsilon_V]=\mathbf1_{U=V}\). Therefore
\[
\boxed{\mathbb E\,\mathscr E_\alpha=c_\varnothing,
\qquad \operatorname{Var}(\mathscr E_\alpha)=\sum_{\varnothing\ne U\subseteq P}c_U^2.}
\tag{3}
\]
By Cauchy–Schwarz, for every \(A\subseteq U\),
\[
|\langle S_{d_A}f,S_{d_{U\setminus A}}f\rangle_\alpha|
\le d_U^{-\alpha/2}\|f\|_\alpha^2.
\]
If \(f\ne0\), define
\[
q_p=\frac{2p^{-\alpha/2}}{1+p^{-\alpha}},\quad
r_p=q_p^2=\frac{4p^{-\alpha}}{(1+p^{-\alpha})^2},\quad R_P=\sum_{p\in P}r_p.
\]
Equation (1) yields
\[
\boxed{\frac{|c_U|}{c_\varnothing}\le\prod_{p\in U}q_p.}
\tag{4}
\]
Thus
\[
\boxed{\frac{\operatorname{Var}(\mathscr E_\alpha)}{(\mathbb E\mathscr E_\alpha)^2}
\le\prod_{p\in P}(1+r_p)-1
\le \exp(4\sum_{p\in P}p^{-\alpha})-1.}
\tag{5}
\]
For each fixed \(\alpha>1\), the right side is bounded **independently of the number of primes** by \(\exp(4(\zeta(\alpha)-1))-1\). For \(\alpha\le1\), this particular estimate diverges with the prime cutoff.

For the degree-\(\ge h\) part of the nonconstant Walsh expansion, the elementary symmetric-sum inequality gives the quantitative **high-order mean-square tail**
\[
\boxed{\frac{\mathbb E\left|\sum_{|U|\ge h}c_U\varepsilon_U\right|^2}{c_\varnothing^2}
\le \sum_{k\ge h}\frac{R_P^k}{k!}
\le e^{R_P}\frac{R_P^h}{h!}.}
\tag{6}
\]
The last inequality follows by writing \(k=h+j\), noting \(k!\ge h!j!\), and summing the exponential series. For fixed \(\alpha>1\), this is a **uniform factorial tail in Walsh degree**. Crucially, it is \(L^2\) over random signs and says **nothing about the one deterministic sign vector \(\varepsilon_p\equiv+1\)**.

## 4. Rademacher multiplicative model: almost-sure finite energy (CLASSICAL TYPE OF RESULT)

Let \((\varepsilon_p)_{p\text{ prime}}\) be independent signs and put
\[
f_\varepsilon(n)=\mu(n)\prod_{p\mid n}\varepsilon_p,
\quad \mathcal M_\varepsilon(x)=\sum_{n\le x}f_\varepsilon(n).
\]
For distinct positive integers \(m,n\), the random coefficients are orthogonal:
\[
\mathbb E[f_\varepsilon(m)f_\varepsilon(n)]=\mu(n)^2\mathbf1_{m=n}.
\]
Indeed, distinct squarefree integers have different prime supports; if either is not squarefree both sides vanish. Consequently, by Tonelli,
\[
\boxed{\mathbb E\left[\alpha\int_1^\infty
\frac{|\mathcal M_\varepsilon(x)|^2}{x^{\alpha+1}}dx\right]
=\sum_{n\ge1}\frac{\mu(n)^2}{n^\alpha}
=\frac{\zeta(\alpha)}{\zeta(2\alpha)}<\infty\quad(\alpha>1).}
\tag{7}
\]
Thus, with probability one, the random model has finite weighted energy for **every real \(\alpha>1\)**. To get the simultaneous statement, intersect the probability-one events at all rational \(\alpha>1\), then use the monotonicity of the positive integral weight when increasing \(\alpha\).

The choice \(\varepsilon_p\equiv+1\) for all primes produces **the actual Möbius function**, but is a measure-zero point in the infinite sign space. A uniform mean-square statement for random prime signs does not bound that deterministic exceptional point. The corresponding deterministic assertion for actual \(M(x)\), finite energy for every \(\alpha>1\), is **RH-equivalent** (Phases XVII and XIX). The stronger almost-sure square-root estimate for random multiplicative functions was already established by Wintner (1944), and has been greatly refined in subsequent work. Equation (7) is an elementary rederivation, **not a new theorem on random multiplicative functions**.

For finite \(P\), even the trivial fact that \(\varepsilon\equiv+1\) has probability \(2^{-|P|}\) shows that the uniform average can at best give \(\mathscr E_\alpha(+1)\le 2^{|P|}\mathbb E\mathscr E_\alpha\) without additional structure. This factor is useless as \(|P|\to\infty\).

## 5. Actual Möbius aggregates at alpha=3: rigorous infinite enclosures

For \(P\) a finite set of primes, let \(F_P(x)=\sum_{n\le x,(n,\prod_{p\in P}p)=1}\mu(n)\). At \(\alpha=3\), all energies converge absolutely by \(|F_P(x)|\le x\). Define
\[
\Delta_{3;P}=\mathcal E_3(M)
-\left(\prod_{p\in P}(1+p^{-3})\right)\mathcal E_3(F_P).
\tag{8}
\]
This is the deterministic sum of every nonconstant Walsh interaction in (1) for \(f=F_P\) and all \(\varepsilon_p=+1\).

**Computer-assisted exact certificate.** A locally executed Python 3 program sieved \(\mu(n)\) through \(K=65536\), independently checked the first 4096 coefficients by trial division, and computed **integer floor/ceiling bounds at scale \(10^{14}\)** for every finite weight \(k^{-3}-(k+1)^{-3}\), \(1\le k<K\). Because \(|M(x)|,|F_P(x)|\le x\), their omitted nonnegative energy tails lie between \(0\) and \(3/K\). With \(D_P=\prod_{p\in P}(1+p^{-3})\), if the integer finite intervals are \([m_-,m_+]\) and \([f_-,f_+]\), rigorous exact enclosures are
\[
\boxed{m_- -D_P(f_+ +3/K)\le\Delta_{3;P}
\le m_++3/K-D_Pf_-.}
\tag{9}
\]
Every endpoint here is an exact rational number; displayed decimals below are only for readability.

| Prime set \(P\) | Rigorous lower | Rigorous upper | Sign |
|---|---:|---:|---|
| \(\{2,3\}\) | −0.242411165461 | −0.242311981923 | Negative |
| \(\{2,5\}\) | −0.174392574489 | −0.174294886335 | Negative |
| \(\{3,5\}\) | +0.007424077291 | +0.007517706549 | Positive |
| \(\{2,3,5\}\) | −0.251384245051 | −0.251284634261 | Negative |
| \(\{2,3,5,7\}\) | −0.254368972554 | −0.254269204814 | Negative |
| \(\{2,3,5,7,11\}\) | −0.253746932201 | −0.253647123897 | Negative |

The negative/positive results are **complete infinite-integral sign theorems**, not extrapolations of finite plots. They reinforce Phase XXIX: even all-prime interactions combined can change sign depending on the finite prime set. Do not claim a universal negative inequality for arbitrary \(P\).

### Eventual negativity along initial prime sets at alpha>2

Let \(P_y=\{p\le y\}\), and let \(q_y\) be its next prime. Then \(F_{P_y}(x)=1\) for \(1\le x<q_y\) and \(|F_{P_y}(x)-1|\le x\) for \(x\ge q_y\). Therefore, for fixed \(\alpha>2\),
\[
\|F_{P_y}-1\|_\alpha^2\le \frac{\alpha}{\alpha-2}q_y^{2-\alpha}\to0.
\]
Also \(D_y=\prod_{p\le y}(1+p^{-\alpha})\to \zeta(\alpha)/\zeta(2\alpha)\). Hence
\[
\boxed{\lim_{y\to\infty}\Delta_{\alpha;P_y}
=\mathcal E_\alpha(M)-\frac{\zeta(\alpha)}{\zeta(2\alpha)}
=2C_\alpha(\infty).}
\tag{10}
\]
For \(\alpha>2\), Phase XII supplies the strictly negative sign of the right side, using its documented independently published Mertens estimate and finite certificate. Thus \(\Delta_{\alpha;P_y}<0\) for sufficiently large \(y\) at each fixed \(\alpha>2\). This is **deduced from the pre-existing Phase XII result, not a new zero-free region**, and it does not establish sign stability for arbitrary non-initial prime subsets.

## 6. Executed verification and open obligation

The reproducibility script \`experiments/riemann_phase30_walsh.py\` executed locally with no external dependencies:

- Exact \`fractions.Fraction\` Walsh-energy identities for \(P=\{2,3\}, \{2,3,5\}, \{2,3,5,7\}\), each with \(\alpha=2,3\) and **all** \(2^{|P|}\) sign assignments: **56/56 PASS**.
- Exact orthogonality/variance equality and exact variance upper bound verified in all six configurations, plus mean-square high-degree-tail comparisons.
- Independent trial-division vs sieve confirmation of \(\mu(1),\ldots,\mu(4096)\): **4096/4096 PASS**.
- Six rigorously signed total aggregate infinite enclosures for \(\alpha=3\): **6/6 PASS**; exact rational endpoints archived in \`experiments/riemann_phase30_aggregate_enclosures.csv\`.

**Proved:** Walsh coefficient identity, mean and variance formulas and uniform normalized variance for fixed \(\alpha>1\), factorial high-degree \(L^2\)-tail, random multiplicative energy expectation and a.s. finiteness, six infinite sign certificates, and eventual sign negativity along \(P_y\) when \(\alpha>2\) using Phase XII.

**Not proved:** any pointwise bound on the all-\(+1\) prime-sign vertex for \(1<\alpha<2\); any improved rate of cancellation of the actual Möbius function; a new zero-free half-plane; RH.

**Next phase:** Investigate whether the actual Möbius **deterministic** prime-sign vertex satisfies an additional signed spectral restriction not shared by arbitrary prime signs, and attempt explicit countermodels. Further random averaging, without a deterministic transfer theorem, cannot yield RH.

### References and prior art

- Wintner's 1944 random multiplicative Möbius model and later work, as summarized by Ofir Gorodetsky, Oxford Mathematical Institute: https://www.maths.ox.ac.uk/node/68544.
- *Almost Sure Large Fluctuations of Random Multiplicative Functions*, International Mathematics Research Notices (2023): https://academic.oup.com/imrn/article/2023/3/2095/6448070.
- Prior phases XXVII–XXIX in this repository.

**Research integrity:** classical probabilistic model; exact algebra; computer-certified elementary integer bounds. No claim of novelty or RH resolution.