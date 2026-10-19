#include <cstdint>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>
int main(){
  constexpr int K=1<<25;
  std::vector<int8_t> mu(K+1,1);
  std::vector<uint8_t> composite(K+1,0);
  mu[0]=0;
  for(int p=2;p<=K;++p){
   if(composite[p]) continue;
   for(int j=p;j<=K;j+=p){mu[j]=-mu[j];if(j>p)composite[j]=1;}
   if((int64_t)p*p<=K)for(int64_t j=(int64_t)p*p;j<=K;j+=(int64_t)p*p)mu[j]=0;
  }
  int64_t M=0;
  long double C2=0, D2=0, q2=0;
  int checkpoints[]={100,1000,10000,100000,1000000,10000000,K};
  int cp=0;
  std::cout<<std::setprecision(16);
  for(int n=1;n<=K;++n){
    const int64_t a=int64_t(mu[n])*M;
    C2+=(long double)a/((long double)n*n);
    D2+=(long double)mu[n]*mu[n]/((long double)n*n);
    M+=mu[n];
    if(n==checkpoints[cp]) {
      q2=D2+2*C2;
      std::cout<<"N="<<n<<" M="<<M<<" C_1/2="<<C2<<" Q_1/2="<<q2<<" diagonal="<<D2<<"\n";
      ++cp;
    }
  }
}