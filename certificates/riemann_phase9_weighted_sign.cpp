// Phase IX: finite EXACT-ARITHMETIC ingredient for unconditional sign theorem.
// Rigorous result after applying the tail inequality in the accompanying argument:
// for every real eps >= 5/8 and every integer N >= 2,
//    sum_{n<=N} mu(n)*M(n-1)/n^(1+2*eps) < 0.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra riemann_phase9_weighted_sign.cpp -o phase9
// Run: ./phase9
#include <cstdint>
#include <iostream>
#include <vector>

int main() {
    constexpr int K = 1 << 20;
    constexpr int64_t SCALE = 1'000'000'000;
    std::vector<int8_t> mu(K + 1, 1);
    std::vector<uint8_t> composite(K + 1, 0);
    mu[0] = 0;
    for (int p = 2; p <= K; ++p) {
        if (composite[p]) continue;
        for (int k = p; k <= K; k += p) {
            mu[k] = -mu[k];
            if (k > p) composite[k] = 1;
        }
        if ((int64_t)p * p <= K) {
            for (int64_t k = (int64_t)p * p; k <= K; k += (int64_t)p * p)
                mu[k] = 0;
        }
    }
    int64_t M = 0;
    int64_t positive_sum_ceiling = 0;
    for (int n = 1; n <= K; ++n) {
        const int64_t a = (int64_t)mu[n] * M;
        if (a > 0) {
            const int64_t denominator = (int64_t)n * n;
            const int64_t numerator = 4 * a * SCALE;
            // An exact rational upper bound on 4*a/n^2, no floating point.
            positive_sum_ceiling += (numerator + denominator - 1) / denominator;
        }
        M += mu[n];
    }
    std::cout << "K=" << K << " M(K)=" << M << '\n';
    std::cout << "P2(K) <= " << positive_sum_ceiling << "/" << SCALE << '\n';
    const bool ok = (50 * positive_sum_ceiling < 23 * SCALE);
    std::cout << "Verified P2(K) < 23/50: " << (ok ? "YES" : "NO") << '\n';
    return ok ? 0 : 1;
}