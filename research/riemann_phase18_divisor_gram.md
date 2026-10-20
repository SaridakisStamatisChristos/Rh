# Phase XVIII — Divisor Gram identity, null-model gap, and the transfer obstruction

**20 October 2026. Status:** exact algebraic results + rigorous elementary mean computation + executed finite experiment. All primary identities are classical or straightforward deductions from Möbius inversion; **no novelty claim**. Nothing here proves RH or an improved zero-free region.

## 1. Divisor Gram identity

For \(1\le d,e\le N\), define the symmetric matrix
\[
G_N(d,e)=\left\lfloor\frac{N}{[d,e]}\right\rfloor
\]
where \([d,e]=\operatorname{lcm}(d,e)\).
For any real \(a=(a_1,\ldots,a_N)\), set
\[
z_n=\sum_{d\mid n}a_d.
\]
Then the exact identity
\[
\boxed{a^\top G_Na=\sum_{n\le N}z_n^2}
\tag{1}
\]
follows by expanding the square and counting common multiples. In matrix form, \(G_N=V_N^\top V_N\), \(V_N(n,d)=\mathbf 1_{d\mid n}\). The lower-triangular \(V_N\) has diagonal entries 1, hence \(G_N\) is actually positive definite.

For \(a_d=\mu(d)\), Möbius inversion gives \(z=(1,0,\ldots,0)\) and therefore
\[
\boxed{\mu^\top G_N\mu=1}\qquad(N\ge1).
\tag{2}
\]
This is exact for every cutoff. Its value is neither an estimate on \(M(x)\) nor an RH proof.

## 2. Independent-sign null model

Let \(b_1=1\), and for every squarefree \(d\ge2\), let \(b_d=\epsilon_d\), where the \(\epsilon_d\) are independent Rademacher random variables; set \(b_d=0\) if \(d\) is not squarefree. Then
\[
\begin{aligned}
\mathbb E[b^\top G_Nb]
&=\sum_{d\le N}\mu(d)^2\lfloor N/d\rfloor\\
&=\sum_{n\le N}2^{\omega(n)}\\
&=\frac6{\pi^2}N\log N+O(N).
\end{aligned}
\tag{3}
\]
The cross-terms vanish by independence and centering (also for the deterministic \(b_1\)). The final asymptotic follows from
\(Q(x)=\sum_{d\le x}\mu(d)^2=(6/\pi^2)x+O(\sqrt x)\)
and partial summation:
\(\sum_{d\le N}\mu(d)^2/d=(6/\pi^2)\log N+O(1)\).
Replacing \(\lfloor N/d\rfloor\) by \(N/d\) causes an \(O(N)\) error.

The actual Möbius energy is exactly 1; the independent-sign expectation grows at order \(N\log N\). This quantifies *divisor* cancellation, but does not quantify the *ordinary summatory* cancellation needed for RH.

## 3. Exact inverse transformation and the missing inequality

Since \(z_n=\sum_{d\mid n}a_d\), Möbius inversion gives
\[
a_n=\sum_{d\mid n}\mu(n/d)z_d.
\]
Thus the ordinary prefix of \(a\) is
\[
\boxed{
A(k):=\sum_{n\le k}a_n
=\sum_{d\le k}z_d\,M\!\left(\left\lfloor\frac kd\right\rfloor\right).
}
\tag{4}
\]
For \(\alpha>0\), the positive maximum-kernel energy is
\[
\begin{aligned}
Q_\alpha(N;a)
&=\sum_{m,n\le N}\frac{a_ma_n}{\max(m,n)^\alpha}\\
&=\sum_{k<N}\Bigl(k^{-\alpha}-(k+1)^{-\alpha}\Bigr)A(k)^2
 +N^{-\alpha}A(N)^2.
\end{aligned}
\tag{5}
\]
Substituting (4) expresses \(Q_\alpha(N;a)\) as a positive quadratic form in the \(z_d\):
\[
Q_\alpha(N;a)
=\sum_{k<N} w_{\alpha,k}
\left(\sum_{d\le k}z_dM(\lfloor k/d\rfloor)\right)^2+
N^{-\alpha}\left(\sum_{d\le N}z_dM(\lfloor N/d\rfloor)\right)^2.
\tag{6}
\]
For \(a=\mu\), \(z=e_1\), and (6) reduces to the original positive energy \(Q_\alpha(N;\mu)\).

**Obstruction:** Knowing only \(\sum z_d^2=1\) does not bound (6). A uniform comparison
\[
Q_\alpha(N;a)\le C_\alpha \sum_{n\le N}\big(\sum_{d\mid n}a_d\big)^2
\tag{7}
\]
for every real vector \(a\) and all \(N\), **for every \(\alpha>1\)**, would *imply RH*, by applying it to \(a=\mu\). It is a much stronger, unproved operator inequality, and no claim is made here that it holds. In particular, divisor cancellation alone cannot be inserted as a free bound for the prefix energy. A bound only on \(Q_\alpha(N;\mu)\) for every \(\alpha>1\) is already the familiar RH-equivalent Mertens energy criterion.

The formal operator in (6) is precisely the sieve-to-prefix transfer that requires new control.

## 4. Independent recurrence from the divisor identity

Summing \(\sum_{d\mid n}\mu(d)=\mathbf 1_{n=1}\) over \(n\le N\), and regrouping terms,
\[
\boxed{\sum_{k=1}^N M(\lfloor N/k\rfloor)=1.}
\tag{8}
\]
For \(N>1\), this gives the exact recurrence
\(M(N)=1-\sum_{k=2}^N M(\lfloor N/k\rfloor)\).
It is standard and does not imply a useful square-root bound by taking absolute values.

## 5. Executed checks

Run \`python3 experiments/riemann_phase18_divisor_gram.py\`.

Exact integer and rational checks at \(N=16,32,64,128\):
- Direct \(N^2\) lcm-kernel Gram sum equals the divisor-square form and equals 1 at \(a=\mu\).
- Möbius inversion reconstructs arbitrary test vectors.
- Formula (4) reconstructs every prefix.
- Exact Fraction arithmetic verifies (5) against (6) at \(\alpha=1,2,3\).
- Recurrence (8) is checked for every \(1\le k\le N\).

Independent random signs on squarefree support: 200 deterministic-seed trials at each \(N\).

| N | Actual divisor energy | Exact null expectation | Sample null mean (200) |
|---:|---:|---:|---:|
| 256 | 1 | 1065 | 1068.5 |
| 1,024 | 1 | 5125 | 5189.1 |
| 4,096 | 1 | 23953 | 23780.1 |

Random sample averages are *not* the proof of (3): the exact expectation is a finite deterministic divisor sum.

## 6. Research verdict

**PROVED/CLASSICAL:** (1)–(6) and (8); the null expectation and asymptotic (3). **HYPOTHETICAL:** the uniform transfer bound (7). **OPEN:** any new nontrivial bound on \(Q_\alpha(N;\mu)\) for fixed \(1<\alpha<2\), or on the positive dyadic budget, and hence RH.

The natural next discriminating experiment is to study whether the transfer operator in (6) has an exploitable arithmetic restriction on its first column (or correlations between columns) that is not equivalent to RH by assumption. Avoid promoting an equivalent reformulation to a proof.

## Prior art

- Fundamental Möbius inversion: Hildebrand, *Analytic Number Theory* lecture notes, University of Athens mirror: https://eclass-b.uoa.gr/modules/document/file.php/MATH717/04.%20%CE%92%CE%BF%CE%B7%CE%B8%CE%AE%CE%BC%CE%B1%CF%84%CE%B1/Analytic-number-theory-Hildebrand.pdf
- Standard \(\sum_{n\le x}2^{\omega(n)}\) asymptotics: https://math.stackexchange.com/questions/1739355/asymptotic-estimate-for-the-sum-sum-n-leq-x-2-omegan
- Chavez, *Correlations of the Möbius and Liouville functions with their partial sums* (2026): https://doi.org/10.1142/S1793042126500934

No claim of priority or novelty is made for this material.
