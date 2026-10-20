// Phase XV — moving-exponent Mobius correlation experiment.
// Numerical diagnostic only. Does NOT prove RH, a fixed-alpha theorem,
// or universal negativity. See research/riemann_phase15_proof.md.
// Build: g++ -std=c++17 -O3 -Wall -Wextra riemann_phase15_korobov_corridor.cpp -o phase15
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>

static int8_t brute_mu(int n) {
    int v=n; int8_t sign=1;
    for (int p=2; int64_t(p)*p<=v; ++p) {
        if (v%p) continue;
        v/=p; sign=-sign;
        if(v%p==0) return 0;
        while (v%p==0) v/=p;
    }
    if (v>1) sign=-sign;
    return sign;
}
int main() {
    constexpr int LIMIT=2000000;
    std::vector<int8_t> mu(LIMIT+1,1);
    std::vector<uint8_t> composite(LIMIT+1,0);
    mu[0]=0;
    for(int p=2;p<=LIMIT;++p) {
        if (composite[p]) continue;
        for(int j=p;j<=LIMIT;j+=p) {
            mu[j]=-mu[j];
            if(j>p) composite[j]=1;
        }
        if(int64_t(p)*p<=LIMIT)
            for(int64_t j=int64_t(p)*p;j<=LIMIT;j+=int64_t(p)*p) mu[j]=0;
    }
    for(int n=1;n<=2000;++n){
        if(mu[n]!=brute_mu(n)) {
            std::cerr<<"Mobius sieve mismatch at "<<n<<'\n';
            return 1;
        }
    }
    std::vector<int> a(LIMIT+1,0);
    int64_t M=0;
    long double c2=0;
    const std::vector<int> checkpoints={100,1000,10000,100000,1000000,2000000};
    size_t k=0;
    std::cout<<"N,delta,alpha,C2,Cmoving,difference,M(N)\n";
    std::cout<<std::fixed<<std::setprecision(12);
    for(int n=1;n<=LIMIT;++n){
        a[n]=int(int64_t(mu[n])*M);
        if(n>=2) c2+=((long double)a[n])/((long double)n*n);
        M+=mu[n];
        if(k<checkpoints.size()&&n==checkpoints[k]) {
            const long double L=std::log((long double)n);
            const long double delta=1/std::sqrt(L);
            const long double alpha=2-delta;
            long double cmoving=0;
            for(int j=2;j<=n;++j)cmoving+=(long double)a[j]/std::pow((long double)j,alpha);
            std::cout<<n<<','<<delta<<','<<alpha<<','<<c2<<','<<cmoving<<','
                     <<(cmoving-c2)<<','<<M<<'\n';
            ++k;
        }
    }
    if(k!=checkpoints.size())return 2;
    return 0;
}
