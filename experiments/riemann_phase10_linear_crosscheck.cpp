// Independent linear-sieve, floating-point cross-check of finite P2.
// The integer-ceiling certificate is authoritative for the strict inequality.
#include <cstdint>
#include <iostream>
#include <iomanip>
#include <vector>
int main(){
  constexpr int K=1<<25;
  std::vector<int> lp(K+1,0), primes;
  std::vector<int8_t> mu(K+1,0);
  mu[1]=1;
  for(int n=2;n<=K;++n){
    if(lp[n]==0){lp[n]=n;primes.push_back(n);mu[n]=-1;}
    for(int p:primes){
      const int64_t j=int64_t(p)*n;
      if(j>K)break;
      lp[j]=p;
      if(p==lp[n]){mu[j]=0;break;}
      mu[j]=-mu[n];
    }
  }
  int64_t M=0;
  long double P=0;
  for(int n=1;n<=K;++n){
    const int64_t a=int64_t(mu[n])*M;
    if(a>0)P+=4.0L*a/((long double)n*n);
    M+=mu[n];
  }
  std::cout << std::setprecision(16)<<"K="<<K<<" M(K)="<<M<<" P2 approx="<<P<<"\n";
}