// Reproducible finite certificate for the Mobius correlation
// C(N) = sum_{n <= N} mu(n)*M(n-1)/n < 0 for every 2 <= N <= 10^7.
// This is a FINITE computation; it does NOT prove the Riemann hypothesis.
// Compile: g++ -std=c++17 -O3 mobius_correlation_certificate.cpp -o certify
// Run:     ./certify
#include <cstdint>
#include <iostream>
#include <vector>
using i128 = __int128_t;

int main() {
    constexpr int LIMIT = 10000000;
    constexpr int64_t SCALE = 1000000000000LL;
    std::vector<int8_t> mu(LIMIT + 1, 1);
    std::vector<uint8_t> composite(LIMIT + 1, 0);
    mu[0] = 0;

    // Independently implement Mobius sieve (not the linear-sieve implementation
    // used for the preliminary floating-point calculation).
    for (int p = 2; p <= LIMIT; ++p) {
        if (composite[p]) continue;
        for (int k = p; k <= LIMIT; k += p) {
            mu[k] = -mu[k];
            if (k > p) composite[k] = 1;
        }
        if (int64_t(p) * p <= LIMIT)
            for (int64_t k = int64_t(p) * p; k <= LIMIT; k += int64_t(p) * p)
                mu[k] = 0;
    }

    // Exact floor(a*SCALE/n) even for negative a. Each term a/n lies in
    // [floor(a*SCALE/n)/SCALE, (floor(a*SCALE/n)+1)/SCALE].
    i128 lower_scaled = 0;
    i128 maximum_upper_scaled = -(i128(1) << 120);
    int maximum_at = -1;
    int failures = 0;
    int64_t mertens = 0;
    for (int n = 1; n <= LIMIT; ++n) {
        int64_t a = int64_t(mu[n]) * mertens;
        i128 numerator = i128(a) * SCALE;
        i128 floor_q = numerator / n;
        if (numerator < 0 && numerator % n != 0) --floor_q;
        lower_scaled += floor_q;
        mertens += mu[n];
        if (n >= 2) {
            i128 upper_scaled = lower_scaled + n;
            if (upper_scaled > maximum_upper_scaled) {
                maximum_upper_scaled = upper_scaled;
                maximum_at = n;
            }
            if (upper_scaled >= 0) ++failures;
        }
    }
    // The maximal bound is greater than -SCALE and fits int64_t;
    // i128 was used throughout to avoid intermediate arithmetic overflow.
    int64_t result = static_cast<int64_t>(maximum_upper_scaled);
    std::cout << "N range: 2.." << LIMIT << '\n';
    std::cout << "Largest rational upper endpoint: " << result
              << " / " << SCALE << " (at N=" << maximum_at << ")\n";
    std::cout << "M(10000000)=" << mertens << '\n';
    std::cout << "All C(N)<0 in tested range: "
              << (failures == 0 ? "YES" : "NO") << '\n';
    return failures == 0 ? 0 : 1;
}