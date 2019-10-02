#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define M 1000000007LL
#define sz(a) (ll)a.size()
#define rep(i,a,b) for(ll i=(ll)a;i<(ll)b;i++)
#define sep(i,a,b) for(ll i=(ll)a;i>=(ll)b;i--)
#define mll map<ll,ll>
#define vl vector<ll>
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define all(a) a.begin(),a.end()
#define F first
#define S second
#define pii pair<ll,ll>
#define mod 1000000007
#define MAXN 200002

/*static vector < ll >*base_arr;
bool compar (ll a, ll b)
{
  return ((*base_arr)[a] < (*base_arr)[b]);
}*/

/*ll gcd(ll a, ll b)
 {
    // Everything divides 0
    if (a == 0 || b == 0)
        return 0;

    // Base case
    if (a == b)
        return a;

    // a is greater
    if (a > b)
        return gcd(a-b, b);
    return gcd(a, b-a);
 }*/

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  ll t,n,u,l,ans;
  cin>>t;
  while(t--)
  {
    cin>>n;
    u=(n*n*(n+1)*(n+1))/4;
    l=(n*(n+1)*(2*n+1))/6;
    ans=abs(u-l);
    cout<<ans<<"\n";
  }
  return 0;
}