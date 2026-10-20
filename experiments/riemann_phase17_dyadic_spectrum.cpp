// Phase XVII numeric diagnostic: dyadic Möbius-correlation spectrum.
// All results finite; this is not proof of universal sign or RH.
// Build: g++ -std=c++17 -O3 -Wall -Wextra -Werror riemann_phase17_dyadic_spectrum.cpp -o phase17_spectrum
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
using i128=__int128_t;
int main() {
    constexpr int LIMIT=1<<23;
    constexpr std::array<long double,5> A={1.0L,1.25L,1.5L,1.75L,2.0L};
    std::vector<int8_t> mu(LIMIT+1,1);
    std::vector<uint8_t> composite(LIMIT+1,0);
    mu[0]=0;
    for(int p=2;p<=LIMIT;++p){
       if(composite[p])continue;
       for(int64_t j=p;j<=LIMIT;j+=p) {mu[(size_t)j]=-mu[(size_t)j]; if(j>p)composite[(size_t)j]=1;}
       if(int64_t(p)*p<=LIMIT)for(int64_t j=int64_t(p)*p;j<=LIMIT;j+=int64_t(p)*p)mu[(size_t)j]=0;
    }
    int64_t M=0;std::array<long double,5> C={0,0,0,0,0};
    std::array<long double,5> prev={0,0,0,0,0};
    std::array<long double,5> posbudget={0,0,0,0,0};
    std::array<int,5> poscounts={0,0,0,0,0};
    int j=0;
    std::cout<<"j,N,D_alpha1,D_alpha1.25,D_alpha1.5,D_alpha1.75,D_alpha2\n";
    std::cout<<std::fixed<<std::setprecision(13);
    for(int n=1;n<=LIMIT;n++){
        int64_t a=int64_t(mu[n])*M;
        if(n>=2){
            long double inv=1.0L/n;
            long double invroot=1.0L/std::sqrt((long double)n);
            long double quarter=std::sqrt(invroot);
            std::array<long double,5> w={inv,inv*quarter,inv*invroot,inv*invroot*quarter,inv*inv};
            for(int k=0;k<5;k++)C[k]+=a*w[k];
        }
        M+=mu[n];
        if(n==(1<<j)){
           if(j>0){
             std::cout<<j<<','<<n;
             for(int k=0;k<5;k++){
                long double d=C[k]-prev[k];
                if(d>0){poscounts[k]++;posbudget[k]+=d;}
                std::cout<<','<<d;
             }
             std::cout<<'\n';
           }
           prev=C;j++;
        }
    }
    std::cout<<"FINAL_COUNTS_AND_POSITIVE_BUDGET";
    for(int k=0;k<5;k++)std::cout<<" alpha="<<(double)A[k]<<":count="<<poscounts[k]<<",budget="<<posbudget[k];
    std::cout<<'\n';
    // Dyadic block at X=4 is strictly positive for each alpha>0 by convexity.
    // At alpha=1 exact rational value is 1/105.
    return 0;
}
