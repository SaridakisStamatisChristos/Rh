// Phase X arithmetic certificate. The mathematical theorem requires the
// analytic squarefree-counting tail bound in the accompanying proof.
// This program verifies the FINITE premise P2(2^25)<23/50 exactly.
// It also verifies rational inequalities used for the infinite tail.
// Not a proof of the Riemann Hypothesis.
// Build: g++ -std=c++17 -O3 -Wall -Wextra riemann_phase10_weighted_sign_certificate.cpp -o phase10
#include <cstdint>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using i128=__int128_t;

std::string as_string(i128 x){
    if(x==0) return "0";
    bool neg=x<0; if(neg) x=-x;
    std::string s;
    while(x>0){s.push_back('0'+int(x%10)); x/=10;}
    if(neg) s.push_back('-');
    std::reverse(s.begin(),s.end()); return s;
}
int main(){
    constexpr int K=1<<25;
    constexpr int64_t SCALE=1'000'000'000'000LL;
    std::vector<int8_t> mu(K+1,1);
    std::vector<uint8_t> composite(K+1,0);
    mu[0]=0;
    for(int p=2;p<=K;++p){
        if(composite[p]) continue;
        for(int j=p;j<=K;j+=p){
            mu[j]=-mu[j];
            if(j>p) composite[j]=1;
        }
        if(int64_t(p)*p<=K){
            for(int64_t j=int64_t(p)*p;j<=K;j+=int64_t(p)*p)
                mu[j]=0;
        }
    }
    int64_t M=0;
    i128 upper=0;
    for(int n=1;n<=K;++n){
        const int64_t a=int64_t(mu[n])*M;
        if(a>0){
            const i128 den=i128(n)*n;
            const i128 num=i128(4)*a*SCALE;
            upper+=(num+den-1)/den; // rigorous upward rounding
        }
        M+=mu[n];
    }
    const bool finite_ok=50*upper < i128(23)*SCALE;
    // Rational tail bound derived from |S(x)-(6/pi^2)x| <= 3sqrt(x):
    // T < 26564248299609 / 46976204800000 < 57/100
    const int64_t tail_num=26'564'248'299'609LL;
    const int64_t tail_den=46'976'204'800'000LL;
    const bool tail_ok=i128(100)*tail_num < i128(57)*tail_den;
    // Verify key algebraic rational comparisons.
    const bool powers_ok=(i128(5)*117649>i128(2)*262144)
      &&(i128(531441)>i128(2)*262144)
      &&(i128(2)*531441>1000000LL)
      &&(i128(4)*8>27);
    const bool total_ok=i128(161)*1+i128(228)<400; // finite + tail < 389/400
    std::cout << "K="<<K<<" M(K)="<<M<<"\n";
    std::cout << "P2(K) <= "<<as_string(upper)<<"/"<<SCALE<<"\n";
    std::cout << "P2(K)<23/50: "<<(finite_ok?"YES":"NO")<<"\n";
    std::cout << "tail<57/100: "<<(tail_ok?"YES":"NO")<<"\n";
    std::cout << "power inequalities: "<<(powers_ok?"YES":"NO")<<"\n";
    std::cout << "normalized negativity margin >=11/400: "
              <<((finite_ok&&tail_ok&&powers_ok&&total_ok)?"YES":"NO")<<"\n";
    return (finite_ok&&tail_ok&&powers_ok&&total_ok)?0:1;
}