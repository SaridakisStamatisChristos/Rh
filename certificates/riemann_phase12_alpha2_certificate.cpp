// Exact finite verification for weighted Mobius anticorrelation at alpha=2.
// The global theorem additionally invokes the unconditional published bound
// |M(x)| <= 2.91890*x/log(x)^2 (x>1), which is NOT proved in this file.
#include <cstdint>
#include <iostream>
#include <vector>
#include <algorithm>
using i128=__int128_t;
std::string s128(i128 v){ if(!v)return "0"; bool neg=v<0; if(neg)v=-v; std::string s;for(;v;v/=10)s.push_back('0'+int(v%10));if(neg)s.push_back('-'); std::reverse(s.begin(),s.end());return s; }
int main(){
 constexpr int K=1<<25;
 constexpr int64_t SCALE=1000000000000LL;
 std::vector<int8_t> mu(K+1,1);
 std::vector<uint8_t> composite(K+1,0);
 mu[0]=0;
 for(int p=2;p<=K;++p){
   if(composite[p])continue;
   for(int j=p;j<=K;j+=p){mu[j]=-mu[j];if(j>p)composite[j]=1;}
   if(int64_t(p)*p<=K)for(int64_t j=int64_t(p)*p;j<=K;j+=int64_t(p)*p)mu[j]=0;
 }
 int64_t M=0;
 i128 c2_upper=0, p2_upper=0;
 for(int n=1;n<=K;++n){
   int64_t a=int64_t(mu[n])*M;
   i128 den=i128(n)*n;
   i128 num=i128(a)*SCALE;
   // C++ rounds negative division toward zero, which is exactly CEIL for negative fractions.
   c2_upper+=(num>=0?(num+den-1)/den:num/den);
   if(a>0) p2_upper+=(i128(4)*a*SCALE+den-1)/den;
   M+=mu[n];
 }
 bool prefix_ok=(p2_upper*50 < i128(23)*SCALE);
 bool endpoint_ok=(c2_upper*25 < -i128(7)*SCALE);
 // With K=2^25, log 2 >2/3 proves log K >50/3.
 // Published Mertens bound implies absolute tail 
 // <= 29189/10000 * (3/50 + 9/(2500*K)) < 22/125.
 const bool rational_tail_ok = i128(29189)*125*(i128(3)*2500*K + i128(9)*50)
                         < i128(22)*10000*50*2500*K;
 std::cout<<"K="<<K<<" M(K)="<<M<<"\n";
 std::cout<<"Upper(C2(K)) = "<<s128(c2_upper)<<"/"<<SCALE<<"\n";
 std::cout<<"Upper(P2(K)) = "<<s128(p2_upper)<<"/"<<SCALE<<"\n";
 std::cout<<"Finite all-prefix test="<<(prefix_ok?"PASS":"FAIL")<<"\n";
 std::cout<<"Endpoint C2(K)<-7/25="<<(endpoint_ok?"PASS":"FAIL")<<"\n";
 std::cout<<"Published-bound tail <22/125 rational arithmetic="<<(rational_tail_ok?"PASS":"FAIL")<<"\n";
 return prefix_ok&&endpoint_ok&&rational_tail_ok?0:1;
}