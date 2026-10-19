// Phase XIV: illustrative numeric audit of a moving-exponent Möbius correlation.
// This program does NOT prove RH or an all-N sign theorem.
// The asymptotic corridor theorem is proved analytically in research/riemann_phase14_proof.md.
// Build: g++ -std=c++17 -O3 -Wall -Wextra riemann_phase14_loglog_corridor.cpp -o phase14
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>

int main() {
    constexpr int LIMIT = 2000000;
    std::vector<int8_t> mu(LIMIT + 1, 1);
    std::vector<uint8_t> composite(LIMIT + 1, 0);
    mu[0] = 0;
    for (int p = 2; p <= LIMIT; ++p) {
        if (composite[p]) continue;
        for (int k = p; k <= LIMIT; k += p) {
            mu[k] = -mu[k];
            if (k > p) composite[k] = 1;
        }
        if (int64_t(p)*p <= LIMIT) {
            for (int64_t k = int64_t(p)*p; k <= LIMIT; k += int64_t(p)*p) {
                mu[k] = 0;
            }
        }
    }
    const std::vector<int> checkpoints = {100, 1000, 10000, 100000, 1000000, 2000000};
    std::vector<int32_t> a(LIMIT + 1, 0);
    int64_t M = 0;
    double c2 = 0;
    size_t idx = 0;
    std::cout << std::fixed << std::setprecision(9);
    std::cout << "N,delta(N),C_2(N),C_{2-delta(N)}(N),difference,M(N)\n";
    for (int n = 1; n <= LIMIT; ++n) {
        a[n] = int32_t(int64_t(mu[n]) * M);
        c2 += double(a[n]) / (double(n) * n);
        M += mu[n];
        if (idx < checkpoints.size() && n == checkpoints[idx]) {
            double L = std::log(double(n));
            double delta = 0.5 * std::log(L) / L;
            double cmoving = 0;
            for (int j = 2; j <= n; ++j) {
                cmoving += double(a[j]) / std::pow(double(j), 2.0 - delta);
            }
            std::cout << n << ',' << delta << ',' << c2 << ',' << cmoving << ','
                      << (cmoving - c2) << ',' << M << '\n';
            ++idx;
        }
    }
    if (idx != checkpoints.size()) return 2;
    return 0;
}
