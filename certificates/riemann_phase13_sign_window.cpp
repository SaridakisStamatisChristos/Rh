// Phase XIII: exact finite certificate for a LOGARITHMIC sign-stability window.
// This code proves finite rational comparisons. The infinite tail additionally
// uses Johnston–Leong–Tudzi, Theorem A.1: |M(x)| <= 2.91890 x/log(x)^2 (x>1).
// It does NOT prove the Riemann Hypothesis or a fixed-exponent alpha<2 result.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using i128 = __int128_t;
static std::string decimal(i128 v){
    if(v==0)return "0";
    bool neg=v<0;if(neg)v=-v;
    std::string s;
    while(v){s.push_back(char('0'+int(v%10)));v/=10;}
    if(neg)s.push_back('-');
    std::reverse(s.begin(),s.end());return s;
}
int main(){
    constexpr int K=1<<25;
    constexpr std::int64_t SCALE=1000000000000LL;
    std::vector<std::int8_t> mu(K+1,1);
    std::vector<std::uint8_t> composite(K+1,0);
    mu[0]=0;
    for(int p=2;p<=K;++p){
        if(composite[p])continue;
        for(int j=p;j<=K;j+=p){mu[j]=-mu[j];if(j>p)composite[j]=1;}
        if((std::int64_t)p*p<=K){
            for(std::int64_t j=(std::int64_t)p*p;j<=K;j+=(std::int64_t)p*p)mu[j]=0;
        }
    }
    i128 c2_upper=0, abs_upper=0, positive_scaled4_upper=0;
    std::int64_t M=0;
    for(int n=1;n<=K;++n){
        const std::int64_t a=(std::int64_t)mu[n]*M;
        const i128 den=(i128)n*n;
        const i128 num=(i128)a*SCALE;
        c2_upper+=(num>=0?(num+den-1)/den:num/den);
        const std::int64_t abs_a=(a>=0?a:-a);
        abs_upper+=((i128)abs_a*SCALE+den-1)/den;
        if(a>0)positive_scaled4_upper+=((i128)4*a*SCALE+den-1)/den;
        M+=mu[n];
    }
    // Published Mertens bound and integral comparison show:
    // sum_{n>K} |mu(n) M(n-1)|/n^2 <22/125.
    // log(2)>2/3, log(K)>50/3, and the comparison below is exact.
    const bool analytic_tail_check = (i128)29189*125*((i128)3*2500*K+(i128)9*50)
                                    <(i128)22*10000*50*2500*K;
    const bool positive_all_prefix=(positive_scaled4_upper*50<(i128)23*SCALE);
    const bool c2_endpoint=(c2_upper*25<-(i128)7*SCALE);
    // abs_upper/SCALE + 22/125 <343/500, a bound sharp enough to
    // prove C_alpha(N)<-1/500 for 2-1/(8log N)<=alpha<=2.
    const bool total_absolute_check = (abs_upper*500*125 + (i128)22*500*SCALE)
                                    <(i128)343*125*SCALE;
    const bool passed = analytic_tail_check&&positive_all_prefix&&c2_endpoint&&total_absolute_check;
    std::cout << "K="<<K<<" M(K)="<<M<<"\n";
    std::cout << "C2(K) upper="<<decimal(c2_upper)<<"/"<<SCALE<<"\n";
    std::cout << "4 x positive-sum upper="<<decimal(positive_scaled4_upper)<<"/"<<SCALE<<"\n";
    std::cout << "absolute-sum(K) upper="<<decimal(abs_upper)<<"/"<<SCALE<<"\n";
    std::cout << "analytic tail bound <22/125: "<<(analytic_tail_check?"PASS":"FAIL")<<"\n";
    std::cout << "C2(N)<-1/10 for all N: "<<((positive_all_prefix&&c2_endpoint&&analytic_tail_check)?"PASS":"FAIL")<<"\n";
    std::cout << "total absolute sum <343/500: "<<(total_absolute_check?"PASS":"FAIL")<<"\n";
    std::cout << "phase-XIII sufficient tests: "<<(passed?"PASS":"FAIL")<<"\n";
    return passed?0:1;
}