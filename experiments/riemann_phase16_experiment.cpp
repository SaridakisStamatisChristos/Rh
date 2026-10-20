// Phase XVI finite certificate and randomized-squarefree benchmark.
// Finite sign results and probabilistic model are NOT a proof of RH.
// g++ -O3 -std=c++17 -Wall -Wextra -Werror riemann_phase16_experiment.cpp -o phase16
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>
using i128 = __int128_t;
static uint64_t state=0x4c5b23084f8d5515ULL;
static uint64_t rng(){state^=state<<7;state^=state>>9;state^=state<<8;return state;}
int main(){
 const int LIM=10000000;
 const int R=4000;
 const int RN=50000;
 const int64_t SCALE=1000000000000LL;
 std::vector<int8_t> mu(LIM+1,1); std::vector<uint8_t> composite(LIM+1,0);mu[0]=0;
 for(int p=2;p<=LIM;++p){if(composite[p])continue;for(int j=p;j<=LIM;j+=p){mu[j]=-mu[j];if(j>p)composite[j]=1;}if(int64_t(p)*p<=LIM)for(int64_t j=int64_t(p)*p;j+=int64_t(p)*p)mu[j]=0;}
 for(int n=1;n<=2000;n++){
     int v=n;int8_t brute=1;
     for(int p=2;int64_t(p)*p<=v;p++){
       if(v%p)continue;
       v/=p;brute=-brute;
       if(v%p==0){brute=0;break;}
     }
     if(brute && v>1)brute=-brute;
     if(brute!=mu[n]) {std::cerr<<"Mobius mismatch n="<<n<<"\n";return 3;}
 }
 int64_t M=0; i128 prefixlower=0, maximumupper=-(i128(1)<<120);int maxwhere=0, bad=0;
 double act15=0,act1=0;int64_t S=0;
 std::vector<double> pref1(LIM+1,0);
 const int checks[]={100,1000,10000,100000,1000000,10000000};int ci=0;
 for(int n=1;n<=LIM;n++){
   int64_t a=(int64_t)mu[n]*M; i128 x=(i128)a*SCALE;
   i128 q=x/n; if(x<0&&x%n)q--; prefixlower+=q;
   i128 upper=prefixlower+n;
   if(n>=2){if(upper>maximumupper){maximumupper=upper;maxwhere=n;}if(upper>=0)bad++;}
   act1+=(double)a/n; act15+=(double)a/(n*std::sqrt((double)n));pref1[n]=act1;
   M+=mu[n];S+=int64_t(mu[n]!=0);
   if(ci<6&&n==checks[ci]){
      std::cout<<"N="<<n<<" M="<<M<<" C_1="<<std::setprecision(12)<<act1<<" C_1.5="<<act15<<" squarefree="<<S<<"\n"; ci++;
   }
 }
 std::cout<<"DYADIC_SHELLS_ALPHA1\n";
 for(int x=2,j=1;2*x<=LIM;x*=2,j++){
   std::cout<<"j="<<j<<" X="<<x<<" D1="<<std::setprecision(12)<<(pref1[2*x]-pref1[x])<<"\n";
 }
 int64_t firstPositiveX=-1; double inc=0;
 for(int x=2;2*x<=LIM;x++){
   double d=pref1[2*x]-pref1[x];
   if(d>1e-7){firstPositiveX=x;inc=d;break;}
 }
 std::cout<<"ALL-PREFIX_C1_SIGN="<<(bad==0?"PASS":"FAIL")<<" upper_scaled_max="<<(long long)maximumupper<<"/"<<SCALE<<" at_N="<<maxwhere<<" bad="<<bad<<"\n";
 std::cout<<"FIRST_POSITIVE_DYADIC_BLOCK="<<firstPositiveX<<" increment="<<std::setprecision(14)<<inc<<"\n";
 // Randomized null: independent Rademacher signs only at squarefree indices.
 // For X_n = xi_n * Mtilde(n-1)/n^alpha, E X_n = 0, Cov(X_n,X_m)=0 for n != m.
 // Exact null variance: sum b_n S(n-1) / n^(2alpha).
 std::vector<double> w(RN+1,0); double predicted=0;int sfprev=0;
 for(int n=1;n<=RN;n++){w[n]=1.0/(n*std::sqrt((double)n));if(mu[n])predicted+=double(sfprev)*w[n]*w[n];sfprev+=(mu[n]!=0);}
 double sm=0,ss=0;int positive=0;
 for(int r=0;r<R;r++){
   int m=0;double c=0;
   for(int n=1;n<=RN;n++){
     if(mu[n]){int xi=(rng()&1)?1:-1;c+=xi*m*w[n];m+=xi;}
   }
   sm+=c;ss+=c*c;if(c>0)positive++;
 }
 double mean=sm/R,variance=ss/R-mean*mean;
 std::cout<<"RANDOM_MODEL_N="<<RN<<" REPLICATES="<<R<<" SEED=0x4c5b23084f8d5515 C_mean="<<mean<<" C_var="<<variance<<" VAR_theory="<<predicted<<" positive_fraction="<<double(positive)/R<<"\n";
 return bad==0&&firstPositiveX==4?0:1;
}
