# Phase XIV — A logarithmic–logarithmic sign-stability corridor

**Date:** 20 October 2026  
**Status:** complete analytic argument, reliant on a published unconditional Mertens bound and Phase XII's finite certificate. Not independently peer-reviewed, not claimed novel, **not a proof of RH**.

## Definitions

Let \(\mu\) be the Möbius function, \(M(x)=\sum_{n\le x}\mu(n)\), and
\[
a_n=\mu(n)M(n-1),\qquad C_\alpha(N)=\sum_{n\le N}\frac{a_n}{n^\alpha}.
\]

## Theorem (general moving-exponent stability)

Let \(\delta_N\ge0\) be any sequence satisfying
\[
N^{\delta_N}=o(\log N)\quad(N\to\infty).
\]
Then
\[
\lim_{N\to\infty}C_{2-\delta_N}(N)
=\sum_{n=2}^{\infty}\frac{\mu(n)M(n-1)}{n^2}
=:C_2(\infty)<-\frac{1}{10}.
\]
In particular, for each fixed \(0<c<1\), taking
\[
\delta_N=c\frac{\log\log N}{\log N}
\]
gives \(C_{2-\delta_N}(N)<0\) for all sufficiently large integers \(N\). The cutoff \(N_0(c)\) is not made explicit by this proof.

## Published input and finite certificate

Johnston–Leong–Tudzi's explicit, unconditional Mertens bound (also quoted in Nicol Leong's 2025 thesis abstract) is
\[
|M(x)|\le A\frac{x}{(\log x)^2}\quad(x>1),\qquad A=2.9189.
\]
It implies absolute convergence of \(\sum |a_n|/n^2\). The previous Phase XII proof, combining an exact finite certificate with the same estimate, gives \(C_2(N)<-1/10\) uniformly, and at the infinite limit in fact \(C_2(\infty)\le-13/125<-1/10\). These are **inputs**, not rederived from the following estimate.

For \(n\ge4\), \(\log(n-1)\ge\frac12\log n\), hence
\[
\frac{|a_n|}{n^2}\le\frac{B}{n(\log n)^2},\qquad B=4A=11.6756.
\]

## Proof of moving-exponent stability

Write \(L=\log N\) and \(\delta=\delta_N\). The hypothesis says \(e^{\delta L}=o(L)\), implying \(0\le\delta\le(\log L)/L\) eventually. Thus \(\delta\to0\) and \(\delta<1/2\) for large \(N\).

Since \(e^u-1\le ue^u\) for \(u\ge0\),
\[
\begin{aligned}
|C_{2-\delta}(N)-C_2(N)|
&\le\sum_{n=2}^N\frac{|a_n|}{n^2}(n^\delta-1)\\
&\le O(\delta)+B\delta\sum_{n=4}^N\frac{n^{\delta-1}}{\log n}.
\end{aligned}
\]
Here \(O(\delta)\) covers the finite terms \(n=2,3\), with constants independent of \(N\).

For \(0\le\delta<1\), \(x^{\delta-1}/\log x\) decreases for \(x>1\). Therefore,
\[
\sum_{n=4}^N\frac{n^{\delta-1}}{\log n}
\le \frac{4^{\delta-1}}{\log4}
+\int_{\log4}^{L}\frac{e^{\delta t}}t\,dt.
\]
For \(N\ge16\), split the integral at \(L/2\), to obtain
\[
\delta\int_{\log4}^{L}\frac{e^{\delta t}}t\,dt
\le\delta e^{\delta L/2}\log\left(\frac{L}{2\log4}\right)
+\frac2L e^{\delta L}.
\]
(The inequality extends continuously through \(\delta=0\).)

Because \(e^{\delta L}=o(L)\) and \(\delta\le(\log L)/L\),
\[
\delta e^{\delta L/2}\log L
=o\!\left(\frac{(\log L)^2}{\sqrt L}\right)\longrightarrow0,
\qquad \frac{e^{\delta L}}{L}\longrightarrow0.
\]
Hence
\[
C_{2-\delta_N}(N)-C_2(N)\longrightarrow0.
\]
Absolute convergence gives \(C_2(N)\to C_2(\infty)\), and the Phase XII bound establishes its negative sign. This completes the proof.

## Rate for a fixed corridor coefficient

For \(\delta_N=c\log\log N/\log N\) with \(0<c<1\), the same bound gives
\[
C_{2-\delta_N}(N)=C_2(\infty)
+O_c\!\left((\log N)^{c-1}+\frac{(\log\log N)^2}{(\log N)^{1-c/2}}\right).
\]
The absolute tail of \(C_2\) is \(O(1/\log N)\), absorbed by this expression.

## Numerical diagnostics (not proof)

A separate C++ Möbius sieve computes the moving exponent at selected checkpoints for \(c=1/2\):

| N | delta | C2(N) | C_(2-delta)(N) |
|---:|---:|---:|---:|
| 100 | 0.165811 | -0.277800475 | -0.327819514 |
| 1,000 | 0.139890 | -0.280128551 | -0.324058803 |
| 10,000 | 0.120535 | -0.280371920 | -0.317873442 |
| 100,000 | 0.106119 | -0.280399213 | -0.312988818 |
| 1,000,000 | 0.095031 | -0.280401802 | -0.309269495 |
| 2,000,000 | 0.092178 | -0.280401955 | -0.308324094 |

The numerical table is only illustrative. The theorem follows from the analytic argument, independently of the listed data.

## Why this does not prove RH

For any **fixed** \(\alpha<2\), \(\delta=2-\alpha>0\) gives \(N^\delta/\log N\to\infty\), violating the hypothesis. Our result covers only moving exponents tending to \(2\), not a fixed interval beneath \(2\), and supplies no zero-free half-plane to the left of \(\Re(s)=1\). The major outstanding proof obligation is a genuinely new signed estimate at fixed \(1<\alpha<2\).

## Sources

1. Nicol Leong (2025), *On some effective results involving zeros of the Riemann zeta function* (thesis abstract). https://doi.org/10.1017/S0004972725000188.
2. Johnston, Leong & Tudzi, *New Bounds and Progress Towards a Conjecture on the Summatory Function of (-2)^Ω(n)*. https://doi.org/10.1080/10586458.2025.2483942.
3. Gordon V. Chavez (2026), *Correlations of the Möbius and Liouville functions with their partial sums*. https://doi.org/10.1142/S1793042126500934. Closely related prior art; no novelty claim is made.