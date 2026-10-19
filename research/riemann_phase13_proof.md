# Phase XIII: A logarithmic sign-stability window for the Möbius correlation

**Research note (20 October 2026). Not peer reviewed. Not a proof of RH.**

Let `mu(n)` be the Möbius function, `M(N)=sum_{n<=N} mu(n)`, and

\[
 C_\alpha(N)=\sum_{n=1}^N\frac{\mu(n)M(n-1)}{n^\alpha}.
\]

## Theorem

For every integer `N>=2` and every real `alpha` with

\[
 2-\frac{1}{8\log N}\le\alpha\le 2,
\]

we have

\[
 \boxed{C_\alpha(N)<-\frac1{500}<0.}
\]

For `alpha>=2`, the earlier Abel-summation argument also gives `C_alpha(N)<0`, but does not preserve the uniform `1/500` margin as alpha tends to infinity.

## Input from Phase XII (explicitly audited)

Set `K=2^25` and `a_n=mu(n)M(n-1)`. The provided C++ file computes, by exact rational upward rounding, the finite inequalities

\[
4\sum_{n=5}^K \frac{\max(a_n,0)}{n^2}<\frac{23}{50},
\qquad C_2(K)<-\frac7{25},
\]

and

\[
\sum_{n=2}^K\frac{|a_n|}{n^2}<\frac{508906458926}{10^{12}}.
\]

Johnston–Leong–Tudzi, *New Bounds and Progress Towards a Conjecture on the Summatory Function of (-2)^{Omega(n)}*, Theorem A.1, show

\[
 |M(x)|\le \frac{2.91890 x}{(\log x)^2}, \quad x>1.
\]

Source: https://www.tandfonline.com/doi/full/10.1080/10586458.2025.2483942

By direct comparison with the decreasing positive function `1/[x (log x)^2]` and `log 2>2/3`, the infinite tail satisfies

\[
 \sum_{n>K}\frac{|a_n|}{n^2}
 \le 2.9189\left(\frac1{K(\log K)^2}+\frac1{\log K}\right)
 <\frac{22}{125}.
\]

The finite positive-part inequality implies `C_2(N)<-27/200` for `2<=N<=K`; the endpoint and tail inequality imply `C_2(N)<-13/125<-1/10` for `N>K`. Consequently

\[
 \boxed{C_2(N)<-\frac1{10}\quad (N\ge2).}
\]

Furthermore, combining the finite absolute bound and the infinite tail yields the exact rational comparison

\[
 B:=\sum_{n=2}^\infty\frac{|a_n|}{n^2}
 <\frac{508906458926}{10^{12}}+\frac{22}{125}
 <\frac{343}{500}.
\]

## Proof of the new theorem

For `2-1/(8 log N)<=alpha<=2`, set `delta=2-alpha`, so `0<=delta<=1/(8 log N)`. For every `2<=n<=N`,

\[
1\le n^\delta\le N^\delta\le e^{1/8}<\frac87.
\]

The strict exponential bound follows from `e^x < 1/(1-x)` for `0<x<1`; the case `delta=0` is immediate. Therefore

\[
\begin{aligned}
 C_\alpha(N)
 &=C_2(N)+\sum_{n=2}^N\frac{a_n}{n^2}(n^\delta-1)\\
 &\le C_2(N)+\left(e^{1/8}-1\right)\sum_{n=2}^N\frac{|a_n|}{n^2}\\
 &<-\frac1{10}+\frac17\cdot\frac{343}{500}
 =-\frac1{500}.
\end{aligned}
\]

This proves the statement.

## Exact limitations

The window has width `1/(8 log N)` and therefore shrinks to zero as `N -> infinity`. This **does not establish the sign inequality for any fixed alpha<2** at arbitrarily large `N`. In particular it does not furnish a fixed zero-free half-plane beyond `Re(s)>1`, and is not material progress toward a proof of RH without a further mechanism handling a non-shrinking exponent gap.

The major open question remains whether a signed-cancellation bound is available for any fixed `1<alpha<2`, much less for exponents approaching `1`. A global sign bound at any such fixed alpha would itself have major consequences for zeros of the zeta function.

Earlier prior art: Gordon V. Chavez, *Correlations of the Möbius and Liouville functions with their partial sums*, International Journal of Number Theory (2026), DOI 10.1142/S1793042126500934. https://doi.org/10.1142/S1793042126500934