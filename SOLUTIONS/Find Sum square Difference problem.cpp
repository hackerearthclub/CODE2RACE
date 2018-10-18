#include <bits/stdc++.h>
using namespace std;


int main()
{
    #ifndef ONLINE_JUDGE
    // for getting input from input.txt
    freopen("input.txt", "r", stdin);
    // for writing output to output.txt
    freopen("output.txt", "w", stdout);
  #endif
  int t,i;
  cin>>t;
  int a[t],s[t];
  for(i=0;i<t;i++) 
    cin>>a[i];
  for(i=0;i<t;i++) 
  {
   s[i]=(((a[i]*(a[i]+1))/2)*((a[i]*(a[i]+1))/2))-((a[i]*(a[i]+1)*(2*a[i]+1))/6);
   if(s[i]<0)
    s[i]=(-1)*s[i];
   cout<<s[i]<<endl;
  }
  return 0;
}
