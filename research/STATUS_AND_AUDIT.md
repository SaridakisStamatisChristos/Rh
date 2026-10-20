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

## Phase XVIII (20 October 2026)

**Exact, classical divisor-cancellation mechanism:** For G_N(d,e)=floor(N/lcm(d,e)), the divisor incidence factorization is a^T G_N a=sum_{n<=N}(sum_{d|n}a_d)^2. In particular for actual Mobius coefficients mu, the value is exactly 1 for every N. This is not an estimate of the Mertens function.

**Independent random-sign null:** On the same squarefree support, independent Rademacher signs have expected divisor Gram energy sum_{d<=N}mu(d)^2 floor(N/d)=sum_{n<=N}2^{omega(n)}=(6/pi^2)N log N+O(N). This is standard and shows extreme divisor-orthogonality, not ordinary prefix cancellation.

**Proof obstruction:** Mobius inversion sends z_n=sum_{d|n}a_d to a_n=sum_{d|n}mu(n/d)z_d and ordinary prefixes A(k)=sum_{d<=k}z_d M(floor(k/d)). Plugging the latter into the positive max-kernel energy shows that a uniform sieve-to-prefix operator estimate for every alpha>1 would imply RH by applying it to z=e_1; that operator estimate is NOT proved and the exact Gram identity alone does not give it. The familiar Mertens RH-equivalent energy bound remains open.

**Executed:** In Python 3, independent exact lcm Gram expansion, inversion, recurrence and Fraction-valued max-kernel energy comparisons all passed for N=16,32,64,128. A fixed-seed 200-trial comparator at N=256,1024,4096 produced exact null expectations 1065, 5125 and 23953, while actual Mobius energy equals 1. The source files are research/riemann_phase18_divisor_gram.md and experiments/riemann_phase18_divisor_gram.py. Neither the algebra nor the null-model asymptotic is claimed novel.

**RH remains open.** Phase XIX should test a genuinely nontrivial arithmetic bound on the sieve-to-prefix transfer, rather than treating exact divisor cancellation as a free norm bound.

## Phase XIX (20 October 2026)

**Proved (exact finite-dimensional algebra):** Let z_n=sum_{d|n}a_d and T_N(k,d)=1_{d<=k}M(floor(k/d)). The weighted prefix energy has Gram matrix H_(alpha,N)=T_N^*diag(w_(alpha,k))T_N, with diagonal H_dd=d^(-alpha) Q_alpha(floor(N/d);mu). Therefore tr(H_(alpha,N))=sum_{d<=N}d^(-alpha)Q_alpha(floor(N/d);mu).

**Proved conditional only on prior certified/published mathematical inputs (not on RH):** Phase XII's C_alpha(m)<0 for all m>=2 and alpha>=2, together with S_alpha(infinity)=zeta(alpha)/zeta(2alpha), gives tr(H)<=zeta(alpha)^2/zeta(2alpha)<=5/2. Thus for arbitrary real/complex a, Q_alpha(N;a)<=5/2 sum_{n<=N}|sum_{d|n}a_d|^2 for alpha>=2. At alpha=2, Phase XII's quantitative C_2(m)<-1/10 strengthens the uniform bound to (5/2-pi^2/30) ~= 2.17101318663, also valid at m=1 by direct check.

**The RH-equivalent barrier remains:** bounded tr(H_(alpha,N)) uniformly in N for every fixed alpha>1 would imply RH; RH implies the bound. The present alpha>=2 estimate is insufficient. Numerical largest eigenvalues or traces at finite sizes cannot prove any uniform estimate for 1<alpha<2.

**Executed in local Python:** exact fractions prove both trace formulas agree at all 12 (N,alpha) pairs N=4,8,12,24; alpha=1,2,3. NumPy spectral diagnostics at N=32,64,128,256 and alpha=1.25,1.5,2.0 passed, with e.g. N=256: alpha=1.25 trace=4.086603028, lambda_max=1.257977208; alpha=2 trace=1.571451294, lambda_max=0.971571343. No formal verification, no novelty assertion.

Archived: research/riemann_phase19_operator_trace.md and experiments/riemann_phase19_operator_trace.py. The explicit Mertens input was verified against Johnston–Leong–Tudzi, Theorem A.1, https://doi.org/10.1080/10586458.2025.2483942. The algebra is related to established Hilbert spaces of Dirichlet series; novelty not established. RH remains open.

## Phase XX (20 October 2026)

**Classical/elementary exact identities (PROVED):** For the sieve-to-prefix Gram matrix H_(alpha,N), sum_e H_(alpha,N)(d,e)=d^(-alpha) sum_{m<=N/d}mu(m)/m^alpha, and the sum of *all* H entries is 1. From entries T(k,d)=1 for k/2<d<=k, tr(H)>= (1/2)sum_{k<=N} k^(-alpha). Thus the signed aggregate of all off-diagonal entries is exactly 1-tr(H), which is <= 1-(1/2) harmonic(N) at alpha=1 and tends to -infinity. For N>=3 this aggregate is strictly negative. No RH input is needed.

**Sign counterexamples (exact):** at N=3, alpha=1, H12=H13=-1/3 while H23=+1/3. At N=5, alpha=1, sum_e H(1,e)=-1/30. Therefore neither entrywise positivity nor positive row sums may be used for Schur-type bounds.

**Critical endpoint obstruction (PROVED using Hardy 1914):** The existence of a critical-line zero of zeta, together with the classical Mellin representation of 1/zeta and weighted Cauchy-Schwarz, implies limsup_N ||H_(1,N)|| / log N > 0. More quantitatively, if rho=1/2+i gamma is simple, limsup_N ||H_(1,N)|| / log N >= |rho*zeta'(rho)|^(-2); if rho is multiple, the limsup is infinite. Hence any all-N uniform alpha=1 operator-bound strategy is FALSE. This does not prohibit bounds at fixed alpha>1 and does not prove RH.

**Executed:** Python 3 exact Fraction Gram and row-sum certificate for 15 (N,alpha) pairs N=3,5,8,16,32; alpha=1,2,3, PASS. Optional float spectral checks at N=32,64,128,256,512 support only finite observations. The exact formulas and Hardy argument are analytical proofs; the finite certificate is not a formal proof assistant.

Files: research/riemann_phase20_offdiagonal.md and certificates/riemann_phase20_offdiagonal_certificate.py. Relevant source for existence of critical zeros: Hardy 1914; 2015 Journal of Number Theory centenary paper https://www.sciencedirect.com/science/article/pii/S0022314X14003515. Operator prior art: Brevig et al., multiplicative Hilbert matrix, DOI 10.1016/j.aim.2016.07.019, different kernel. Novelty unverified. **RH remains open.**

## Phase XXI (20 October 2026)

**Exact arithmetic-dilation identity (PROVED):** The divisor-coordinate embedding U_d supported on multiples of d satisfies U_d* H_(alpha,N) U_d = d^(-alpha) H_(alpha,floor(N/d)) for every alpha>0.

**Persistent RH obstruction (PROVED):** For any fixed D>=1 and any fixed alpha>1, uniform-in-N boundedness of the compression P_{d>=D} H_(alpha,N) P_{d>=D} is equivalent to uniform boundedness of Q_alpha(N;mu), by the basis e_D and the exact trace formula. Requiring these equivalent conditions for all alpha>1 is RH-equivalent. Deleting any fixed finite set of initial divisor coordinates cannot close the proof gap.

**High-divisor spectral localization (PROVED unconditionally from |mu(n)|<=1):** For fixed 1<alpha<2 and 2<=D<=N, ||P_{d>=D}H_(alpha,N)P_{d>=D}|| <= [2/(2-alpha)] N^(2-alpha)/(D-1). For any eta in (0,alpha-1), choosing D=floor(N^(2-alpha+eta))+1 gives upper bound [2/(2-alpha)]N^(-eta). Positive-semidefinite Gram factorization yields 0<=lambda_max(H_N)-lambda_max(H_N[1:D-1,1:D-1])<=the same bound. This is an explicit dimension reduction but DOES NOT bound the difficult growing leading block.

**Upper-half exact block (PROVED):** For d,e>floor(N/2), H_(alpha,N)(d,e)=max(d,e)^(-alpha). With L=ceil(N/2), its operator norm is between L/N^alpha and L/(floor(N/2)+1)^alpha, hence Theta_alpha(N^(1-alpha)) for fixed alpha>1.

**Executed locally:** 60 rational-arithmetic test groups (N=8,12,24,36; alpha=1,2,3; dilations 2,3,4,5 plus upper-half checks), and 9 finite NumPy spectral comparisons (N=64,128,256; alpha=1.25,1.5,1.75); all PASS. No CI or formal proof-assistant claims. The locally executed script is substantially equivalent to the archived reproduction script.

Files: research/riemann_phase21_dilation_localization.md; experiments/riemann_phase21_dilation_localization.py. Prior art includes Nikolski, Hardy Spaces, Ch.6 (2019), DOI 10.1017/9781316882108.008. Uniqueness/novelty not established. **RH remains open.**

## Phase XXII (20 October 2026)

**Proved, but not claimed novel:** For any single fixed alpha in (0,2), M(N)=o(N) (equivalently PNT) if and only if ||H_(alpha,N)||=o(N^(2-alpha)). Forward: Q_alpha(m)=o(m^(2-alpha)) from M=o(N); dominated convergence in the exact divisor-coordinate trace with d^(-2) domination; reverse: H_11=Q_alpha(N)>=M(N)^2/N^alpha.

**Power-saving equivalence (PROVED but an equivalent reformulation, not a new zero-free region):** For 1<alpha<2, 0<eta<2-alpha, beta=2-alpha-eta>0 and theta=1-eta/2>1/2, one has ||H_(alpha,N)||=O(N^beta) iff M(N)=O(N^theta). If |M(k)|<=B k^theta, then Q_alpha(m)<=B^2[1+alpha(1+1/beta)]m^beta and the operator norm is bounded by B^2[1+alpha(1+1/beta)] zeta(2theta) N^beta. Conversely use the first diagonal and positive endpoint square. Any new fixed spectral power saving would produce a corresponding fixed zero-free half-plane Re(s)>theta; NONE is proved here.

**Unconditional effective-rate class (PROVED using existing external theorem):** For fixed 0<alpha<2, classical Korobov–Vinogradov/Mertens cancellation |M(x)|<=A x exp(-b (log x)^(3/5)/(loglog x)^(1/5)) implies ||H_(alpha,N)|| <= C_alpha N^(2-alpha) exp(-c_alpha (log N)^(3/5)/(loglog N)^(1/5)) for large N and unspecified positive constants. This is a classical subpower saving in new coordinates, not a better zero-free region.

**Executed locally:** exact rational trace identities PASS in 9/9 cases (N=4,8,16; alpha=1,2,3). Direct Gram spectra and trace formula agree for N=128,512 and alpha=1.25,1.5,1.75. Deterministic Mobius sieve through N=524288 and normalized trace table show finite decreases; this does NOT prove asymptotic decay or RH. Reproduction source: experiments/riemann_phase22_spectral_pnt.py; results: experiments/riemann_phase22_results.csv; proof: research/riemann_phase22_spectral_pnt.md.

**Prior art sources:** Standard M=o(x) iff PNT; Nicol Leong's 2025/26 Cambridge paper on effective Mertens bounds and K–V; Ghosh et al., Advances in Mathematics 2024, related zero-free half-plane functional-analytic characterizations. Proof novelty NOT established. The Clay Mathematics Institute lists RH as unsolved as of October 2026.

## Phase XXIII (20 October 2026)

**Exact linear algebra (PROVED):** The inverse of T_N(k,d)=1_{d<=k}M(floor(k/d)) is B_N(d,k)=1_{k|d}-1_{k+1|d}; therefore H_(alpha,N)^(-1)=B_N W^(-1) B_N^*, and det(H)=N^(-alpha)*product_{k<N}[k^(-alpha)-(k+1)^(-alpha)], independent of Mobius values. For v, the inverse quadratic form is sum_k w_k^(-1) |sum_{km<=N} v_{km} - sum_{(k+1)m<=N} v_{(k+1)m}|^2.

**Exact inverse trace and new asymptotic deduction (PROVED, no RH):** tr H^(-1) = sum_{k=1}^N [floor(N/k)+floor(N/(k+1))-2floor(N/[k(k+1)])]/w_(alpha,k) = [2*zeta(alpha+2)/(alpha*(alpha+2))]*N^(alpha+2)+O_alpha(N^(alpha+1)) for every fixed alpha>0. Derivation uses the power-sum asymptotic, a divisor-counting interchange, and the fact that the cross-lcm term comes only from k<=sqrt(N).

**Sharp smallest-eigenvalue order (PROVED, alpha>1):** (N/3)^(alpha+1)/alpha <= ||H^(-1)|| <= [4*2^(alpha+1)*zeta(alpha)/alpha] N^(alpha+1) for N>=4. Thus lambda_min(H)=Theta_alpha(N^(-alpha-1)), unconditionally. This rate of ill-conditioning exists even if RH is true.

**RH-equivalent condition-number reformulation (NOT AN RH PROOF):** Since kappa_2(H)=lambda_max(H)*||H^(-1)||, RH is equivalent to requiring for every fixed alpha>1 that kappa_2(H)=O_alpha(N^(alpha+1)). At alpha>=2 this condition-number growth is already unconditional by the earlier Phase XII/XIX result lambda_max(H)<=5/2, coupled with lambda_max(H)>=1-2^(-alpha). For 1<alpha<2, uniform control on the largest eigenvalue is still open.

**Independently executed in the available Python environment:** Exact Fraction tests passed for N=3,4,8,12,20; alpha=1,2,3 (15 exact pairs), confirming T*B=B*T=I, H*H^(-1)=I and inverse trace formula. NumPy eigenvalue/trace comparisons passed for N=32,64,128,256 and alpha=1.25,1.5,2 (12 finite cases). For N=256, alpha=1.5, lambda_min=3.65454737e-7, lambda_max=1.10182218, inverse trace divided by N^(alpha+2)=0.429840369 vs asymptotic 0.429231949. Finite computations are not proof of RH.

Files: research/riemann_phase23_inverse_spectrum.md; experiments/riemann_phase23_inverse_spectrum.py. Research priority: investigate largest eigenvalue at fixed 1<alpha<2; exact determinants and small eigenvalues alone cannot resolve RH. Closest prior art: Roesler 1986 RH eigenvalue paper and Ilmonen–Kaarnioja 2018 lattice-incidence eigenvalue paper. No novelty claim; **RH remains open**.

## Phase XXIV (20 October 2026)

**Exact finite arithmetic algebra (PROVED, novelty not established):** The inverse Gram matrix has B(d,k)=1_{k|d}-1_{k+1|d}. For any distinct odd primes p,q<=N, (H_(alpha,N)^(-1))_(pq)=1/w_(alpha,1). The odd-prime block is diag(d_p)+c1*11^T, with d_p=1/w_(alpha,p-1)+1/w_(alpha,p) and c1=1/w_(alpha,1).

**Uniform diagonal preconditioning (PROVED for each fixed alpha>0):** D^(-1/2) G_prime D^(-1/2)=I+c1*s*s^T with s_p=d_p^(-1/2). It has one eigenvalue 1+c1*sum_p 1/d_p; the others equal 1. Using d_p >= (p-1)^(alpha+1)/alpha gives an N-independent upper bound 1+alpha*(zeta(alpha+1)-1)/(1-2^(-alpha)). This controls a prime-indexed restricted block of the INVERSE, not the full primal norm.

**Prime-coordinate interpolation inequality (PROVED):** For z_n=sum_{d|n}a_d and every N>=3, alpha>0, the primal energy z*H z is at least w1*|z1|^2+w2*|z2|^2+w3*|z2+z3-z1|^2+sum_{odd primes p>=5,p<=N}|zp-z1|^2/(1/w_(p-1)+1/w_p). This follows by exact inversion of the principal inverse block on indices {1,2}+odd primes and the positive-definite Schur complement. For a=mu this supplies only a finite, explicit LOWER bound on Q_alpha(N;mu), not the upper bound equivalent to RH.

**Failure of naive composite extension (PROVED):** At N>=15 the inverse entry (9,15) equals c1+c2+c3>c1, so the rank-one formula is special to odd primes.

**Executed locally:** Python 3 fractions.Fraction checks passed at N=3,5,8,12,18 and alpha=1,2,3: 15 cases covering prime-pair inverse entries, exact inverse of the restricted inverse block, Schur interpolation inequality; composite (9,15) check PASS. The rank-one spectral formula was checked numerically at N=31,127,509,1021 and alpha=1,1.5,2 (12 combinations). Archived: research/riemann_phase24_prime_dual.md; experiments/riemann_phase24_prime_dual.py. No peer review or claim of novel mathematics; **RH remains open**.

## Phase XXV (20 October 2026)

**Exact odd-index inverse Gram factorization (PROVED, no novelty claim):** For odd d,e<=N and c_k=1/w_(alpha,k), define gamma_1=c_1, gamma_r=c_(r-1)+c_r for odd r>=3. Then (H_(alpha,N)^(-1))_(de)=sum_{r|gcd(d,e), r odd}gamma_r. Equivalently G_odd=L diag(gamma)L^T for the odd-divisor incidence matrix L; det(G_odd)=prod_odd gamma. This extends the odd-prime rank-one structure of Phase XXIV to all odd composites. Closely related to the classical weighted-GCD matrix literature, including Ovall (2004), DOI 10.13001/1081-3810.1121.

**Uniform diagonal preconditioning (PROVED for each fixed alpha>1, all N):** Let D=diag(gamma_r), s=(alpha+1)/2>1 and gamma_r asymptotically bounded between positive alpha-dependent multiples of r^(alpha+1). Both A=D^(-1/2)L D^(1/2) and A^(-1) are dominated on ell^2 by the absolutely convergent odd-dilation sum sum_{m odd} m^(-s)=(1-2^(-s))zeta(s). Hence the normalized odd inverse Gram D^(-1/2)G_odd D^(-1/2) has N-uniformly bounded max AND min eigenvalues. At alpha=1 this specific proof does not yield boundedness. None of these statements bounds the full primal H required by RH.

**Sharp Schur-interpolation lower bound (PROVED):** Retaining z_2 and all odd divisor-transform coordinates, the primal weighted energy is >= w1|z1|^2 + w2|z2|^2 + w3|z2+z3-z1|^2 + sum_{odd r>=5} |sum_{d|r}mu(r/d)z_d|^2/(c_(r-1)+c_r). The formula is exact for the optimized energy with unobserved even z coordinates. For arithmetic Mobius input z=e1 it gives Q_alpha(N;mu)>=w1+w3+sum_{odd r>=5}mu(r)^2/(c_(r-1)+c_r), strictly stronger than the Phase XXIV prime-only lower bound starting at the composite 15. It is a LOWER bound and does not imply RH.

**Executed locally:** Python Fraction exact tests passed at all 24 pairs of N=3,5,8,12,15,21,32,40 with alpha=1,2,3, verifying the weighted-GCD block entries, odd-Mobius inverse, inverse restricted augmented Gram, arbitrary-z inequality and Mobius specialization. NumPy diagonal-normalized spectral diagnostics ran for N=32,64,128,256; alpha=1,1.25,1.5,2 (16 observations). At N=256, alpha=1.5: min=0.53950804, max=1.97141481; alpha=2: min=0.63880756, max=1.62550780. Computations are finite tests, not independent proof of uniform bounds.

Source: research/riemann_phase25_odd_divisor.md; verification: experiments/riemann_phase25_odd_divisor.py. No full operator bound at fixed 1<alpha<2, no new zero-free region, and **RH remains open**.

## Phase XXVI (20 October 2026) — parity-residual audit and reconciliation

**Repository reconciliation:** Phase XXV's independently archived weighted-GCD note and its 24 exact tests are preserved unchanged. An overlapping new odd-GCD audit was therefore consolidated under Phase XXVI instead of creating two conflicting Phase XXV notes. The odd-gcd factorization itself was already documented in research/riemann_phase25_odd_divisor.md and is not claimed as a new mathematical result in this phase.

**Complete algebraic identity (PROVED for every complex coefficient vector, N>=3, alpha>0):** Let A_k=sum_{n<=k}a_n, w_k=k^(-alpha)-(k+1)^(-alpha) for k<N, w_N=N^(-alpha), c_k=1/w_k, and Q=sum_k w_k |A_k|^2. Then Q=L+R where L=w1|A1|^2+w2|A2|^2+w3|A3|^2+sum_{odd t>=5,t<=N}|a_t|^2/(c_(t-1)+c_t), and R=sum_{odd t>=5,t<=N}|w_(t-1) A_(t-1)+w_t A_t|^2/(w_(t-1)+w_t)+1_{N even} w_N |A_N|^2 >=0. This follows by completing the square on disjoint adjacent prefix pairs (4,5), (6,7), ... . It is precisely the sharp Schur complement for the inverse Gram block indexed by {2} union odd indices (a result also reached in Phase XXV). No multiplicativity is needed; it is ordinary weighted least squares.

**RH-equivalent residual reformulation (NOT A PROOF):** For a=mu, A=M, the local term L=w1+w3+sum_{odd t>=5}mu(t)^2/(c_(t-1)+c_t) is uniformly bounded in N for every fixed alpha>0. Thus RH iff for every fixed alpha>1 the nonnegative residual R_alpha(N;mu) is uniformly bounded in N. This is another restatement of the known quadratic-energy criterion, not an independently established new cancellation estimate.

**Longer finite experiment:** An independent pure-Python linear Möbius sieve evaluated N=1024,8192,65536,524288, at alpha=1.25,1.5,2; at N=524288: alpha=1.25 Q=1.232970991663, prime-only lower=0.689705728847, odd+2 lower=0.693232510826, residual=0.539738480836; alpha=1.50 Q=1.077940603923, lower=0.740239877429, residual=0.337700726494; alpha=2 Q=0.959013501984, lower=0.811756174174, residual=0.147257327810. Finite values do not prove convergence or RH.

**Independent exact checks executed:** 36 N/alpha combinations, N=3,4,5,8,9,10,11,16,20,21,24,31; alpha=1,2,3, plus 108 seeded exact rational vectors. Verified inverse matrix, weighted odd GCD entries, Möbius inversion of the odd incidence matrix, enhanced odd+2 Schur complement, full parity decomposition and nonnegative residual. All PASS; source is experiments/riemann_phase26_parity_residual.py. No CI, peer review or formal verification claim.

**Scientific interpretation:** The uniformly normalized inverse odd block from Phase XXV is valid, but the direct parity-matching identity proves the lower estimate does not supply the upper bound needed for RH. The residual still contains weighted averages of consecutive Mertens values and remains uncontrolled for fixed 1<alpha<2. **RH remains open.**

## Phase XXVII (20 October 2026) — prime-dilation and sharp norm barrier

**Exact arithmetic (PROVED):** For a finite prime set P, define M_P(x)=sum_{n<=x,(n,prod(P))=1}mu(n) and S_p f(x)=f(x/p), zero below 1. Then M=prod_{p in P}(I-S_p) M_P and M_P=prod_{p in P}(I-S_p)^(-1) M, where the latter sum is finite at every fixed x and ranges over P-smooth integers including prime powers.

**Weighted energy (PROVED):** In H_alpha=L2([1,infinity),alpha*x^(-alpha-1)dx), ||S_p||=p^(-alpha/2), so for finite P and any finite cutoff X, [prod(1-p^(-alpha/2))] ||M_P||_(alpha,X) <= ||M||_(alpha,X) <= [prod(1+p^(-alpha/2))] ||M_P||_(alpha,X). The finite energy is the weighted sum over k<X without the endpoint correction in finite Q_alpha(X). Membership of M and M_P in H_alpha is equivalent for every fixed finite P, but not known for all alpha>1.

**Sharpness (PROVED in the full function Hilbert space, NOT merely the arithmetic subclass):** For A_P=prod(I-S_p), exact operator norms are ||A_P||=prod(1+p^(-alpha/2)) and ||A_P^(-1)||=prod(1-p^(-alpha/2))^(-1). An isometry to weighted right shifts on L2(0,infinity), approximate oscillatory eigenvectors and Kronecker approximation of log primes yield equality. This defeats any attempt to obtain a uniform estimate in the number of primes using ONLY abstract prime-dilation operator norms.

**Euler-product threshold (CLASSICAL DEDUCTION):** For P_y={p<=y}, at alpha>2 the exact norm limits are zeta(alpha/2)/zeta(alpha) (forward) and zeta(alpha/2) (inverse). At alpha=2, by Mertens' third theorem, these grow like (6/pi^2)*exp(gamma)*log(y) and exp(gamma)*log(y), respectively. At 0<alpha<2, both logarithms are asymptotic to y^(1-alpha/2)/((1-alpha/2)*log(y)) using the prime number theorem. This is a sharp failure of UNIFORM UNIVERSAL NORM bounds, not evidence of divergence for the arithmetic Mertens function.

**Actually executed:** Standard-library Python 3 code checked mu by an independent trial division for 1000 integers; exactly reconstructed the Mertens function through N=16384 for 7 finite prime sets; passed 7 Fraction-exact energy inequalities at N=256,alpha=2; and passed 28 real-exponent finite-energy inequalities at N=16384,alpha=1.25,1.5,2,3. Computed exact finite Euler products for y=10,100,1000,10000,100000 and alpha=1.5,2,2.5,3. For y=100000, inverse product =32700.634712 at alpha=1.5, =20.511593 at alpha=2 and =2.611132 at alpha=3.

**Files on main:** research/riemann_phase27_prime_dilation.md; experiments/riemann_phase27_prime_dilation.py; experiments/riemann_phase27_energy.csv; experiments/riemann_phase27_operator_norms.csv.

**Integrity:** The underlying number-theoretic facts and operator-shift ideas are standard; novelty unchecked. The prime-dilation barrier does not imply RH, disprove RH, or establish a new zero-free region. The specific next missing fact is arithmetic cross-prime correlation/cancellation stronger than the universal operator-norm triangle inequality. **RH remains open.**

## Phase XXVIII (20 October 2026) — signed prime-step covariance falsification

**Exact identities (PROVED, elementary):** For prime p let F_p(x)=sum_{n<=x, p does not divide n}mu(n); M(x)=F_p(x)-F_p(x/p). In the weighted energy E_(alpha,X)(f)=alpha integral_1^X f(x)^2 x^(-alpha-1)dx, the reconstruction gives E(M)-E(F_p)=p^(-alpha) E_(alpha,X/p)(F_p)-2 J_(p,alpha)(X), with J=alpha integral_1^X F_p(x)F_p(x/p)x^(-alpha-1)dx. There is an independent finite double-sum expression using max(m,pn)^(-alpha)-X^(-alpha).

**Opposite infinite signs (PROVED for the real arithmetic Möbius function, alpha=3):** J_(2,3)>0, J_(3,3)<0, J_(5,3)<0. The integral tail beyond X is absolutely <= alpha/[p(alpha-2)]X^(2-alpha), by |F_p(x)|<=x. At X=1024, exact Fraction finite sums prove J_(2,3)(X)>9/100, J_(3,3)(X)<-1/600, J_(5,3)(X)<-1/250; their respective tail allowances 3/(2X), 1/X, 3/(5X) cannot change the signs. Rigorously outward-rounded enclosing intervals for the INFINITE correlations: p=2 (0.0889378, 0.0918676); p=3 (-0.0029560, -0.0010028); p=5 (-0.0050696, -0.0038976). This explicitly REJECTS both universal-positive and universal-negative sign assumptions about prime-step cross terms. It is at alpha=3, *not* a new fixed-strip cancellation bound.

**Critical-interval finite energy sign reversal (PROVED by exact rational arithmetic):** At cutoff X=32, Delta_alpha=E_(alpha,X)(M)-E_(alpha,X)(F_3) has Delta_1=-65627647919/3208967842080<0 and Delta_2=174590367216324991675973/2059494922300714363745280>0. Continuity gives some alpha_* in (1,2) with Delta_(alpha_*)=0, with no uniqueness asserted. This rejects an exponent-independent monotonicity claim at a fixed finite cutoff, not an asymptotic sign theorem.

**Pairwise rational dilation identity (PROVED):** For f in the weighted Hilbert space and 1<=d<=e, <S_d f,S_e f>_alpha=d^(-alpha)<f,S_(e/d) f>_alpha. Thus adding two primes gives nonorthogonal cross terms depending on rational scale ratios. For f=1_[x>=1] it reduces to the original max-kernel Gram form, so a favorable aggregate cross-term theorem cannot be assumed without reproducing the RH-equivalent cancellation challenge.

**Executed, separately validated:** Python 3 standard-library script with Möbius independently checked at all 1024 integers; 3 exact Fraction infinite sign certificates plus analytic tail; 2 exact energy-difference rationals; 9 one-prime reconstruction/energy polarization cases; 27 independent finite double-sum comparisons; plus 9 exact telescoping checks over every prime up to X=16,32,64 and exponents 1,2,3. All PASS locally. Files: research/riemann_phase28_prime_covariance.md and experiments/riemann_phase28_prime_covariance.py. Mathematical novelty and priority not established; outside critical-strip infinite sign results do not improve any zeta zero-free region. **RH remains unsolved.**

**Phase XXVIII exact aggregate addendum (proved):** If p_1<...<p_r are all primes <=X, P_j={p_1,...,p_j}, and F_j=M_(P_j), then E_(alpha,X)(M)=1-X^(-alpha)+sum_{j=1}^r[p_j^(-alpha)E_(alpha,X/p_j)(F_j)-2J_(p_j,alpha)(F_j;X)] for every alpha>0. The final sieve-excised function is 1 throughout [1,X), and the result telescopes exact one-prime energy polarizations. This is another identity for the existing RH-equivalent weighted energy, not a new uniform bound.
