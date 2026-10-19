# Global weighted Möbius-correlation sign theorem at exponent 2

**Status:** conditional on the reliability of two prior rigorous results (a published unconditional explicit Mertens bound, and correct execution of the included finite exact-arithmetic certificate), the following is an unconditional mathematical theorem. **It is not a proof of the Riemann hypothesis. No novelty claim is made.**

## Result

Let `μ(n)` be the Möbius function, `M(N) = Σ_{n≤N} μ(n)`, and

`C_α(N) = Σ_{n≤N} μ(n)M(n−1)/n^α`.

For **every** integer `N≥2` and **every** real `α≥2`,

\[
\boxed{C_\alpha(N)<-\tfrac1{10}\,2^{2-\alpha}<0.}
\]

In the earlier parameterization `α=1+2ε`, this covers every `ε≥1/2`.

## External theorem used

We invoke the published, unconditional bound

\[
|M(x)| \le \frac{2.91890 x}{(\log x)^2}\qquad(x>1).
\]

Source: Daniel R. Johnston, Nicol Leong, Sebastian Tudzi, *New Bounds and Progress Towards a Conjecture on the Summatory Function of (-2)^{Ω(n)}*, Theorem A.1; the inequality is also quoted in Ethan S. Lee and Nicol Leong, *New explicit bounds for Mertens function and the reciprocal of the Riemann zeta function*, arXiv:2208.06141v5 (9 September 2026), Eq. (14). The source theorem is assumed, not re-proved by this certificate.

## Exact finite part

Set `K=2^25 = 33554432`, `a_n=μ(n) M(n−1)`, and `a_n^+=max(a_n,0)`.

The included C++ code uses a Möbius sieve and an exact integer ceiling of each rational summand multiplied by `10^12`. It verifies

\[
4\sum_{n=5}^{K}\frac{a_n^+}{n^2}
\le\frac{456992209700}{10^{12}}<\frac{23}{50}
\]

and

\[
C_2(K)\le-\frac{280391897955}{10^{12}}<-\frac7{25}.
\]

As `a_2=-1` and `a_3=a_4=0`, for **every** `2≤N≤K`,

\[
4C_2(N)=-1+4\sum_{n=5}^N\frac{a_n}{n^2}
\le-1+4\sum_{n=5}^K\frac{a_n^+}{n^2}
<-\frac{27}{50}.
\]

Therefore `C_2(N)<-27/200<-1/10` throughout the finite range.

## Infinite tail

For any `N>K`, using the published explicit bound at `x=n−1`,

\[
\begin{aligned}
C_2(N)-C_2(K)
&\le\sum_{n=K+1}^{N}\frac{|\mu(n)M(n-1)|}{n^2}\\
&\le 2.91890\sum_{m=K}^{\infty}\frac1{m(\log m)^2}\\
&\le2.91890\left(\frac1{K(\log K)^2}+\frac1{\log K}\right).
\end{aligned}
\]

`log(2)>2/3` (e.g. via `log(2)=2(1/3+1/(3⋅3^3)+...)`), so `log(K)>50/3`. A rational comparison, checked in the same C++ certificate, gives

\[
2.91890\left(\frac3{50}+\frac9{2500K}\right)
<\frac{22}{125}=0.176.
\]

Consequently

\[
C_2(N)<-\frac7{25}+\frac{22}{125}=-\frac{13}{125}<-\frac1{10}.
\]

Combining finite and infinite ranges gives `C_2(N)<-1/10` for every `N≥2`.

## Extension to every α≥2 (Abel summation)

Let `b_n=a_n/n²`, `S_k=Σ_{n≤k}b_n=C_2(k)`, `w_n=n^{-(α−2)}`. Then

\[
C_\alpha(N)=S_Nw_N+\sum_{k=2}^{N-1}S_k(w_k-w_{k+1}).
\]

All coefficients are nonnegative when `α≥2`. As every `S_k<-1/10`,

\[
C_\alpha(N)<-\frac1{10}\left(w_N+\sum_{k=2}^{N-1}(w_k-w_{k+1})\right)
=-\frac1{10}\,2^{-(\alpha-2)}.
\]

QED.

## Verification

```
g++ -std=c++17 -O3 -Wall -Wextra riemann_phase12_alpha2_certificate.cpp -o phase12
./phase12
```

Expected checks: finite all-prefix `PASS`; endpoint `C_2(K)<−7/25` `PASS`; infinite-tail rational comparison `<22/125` `PASS`.

**Important limitation:** This result covers only `α≥2` (`ε≥1/2`). Through the positive quadratic identity, these exponents do not yield any new zero-free half-plane beyond `Re(s)>1`. RH requires control approaching `α=1`. The observed sign theorem is therefore an intermediate statement, and its mathematical novelty has not been established.