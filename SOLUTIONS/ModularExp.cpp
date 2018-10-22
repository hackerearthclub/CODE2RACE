#include<bits/stdc++.h>
#define ull unsigned long long
#define ll long long
ll modularexp(ll a,ll b,ll m)
{
  if(b==0)
    return 1;
  if(b%2==0)
    return pow((a*a)%m,b/2,m);
  else
    return a*pow((a*a)%m,(b-1)/2,m)%m;
}
using namespace std;
int main()
{
    int a,b,m;
    cout<<"\nEnter a,b,and m to find (a^b)%m";
    cin>>a>>b>>m;
    cout<<"\nAnswer is "<<modularexp(a,b,m)
}
