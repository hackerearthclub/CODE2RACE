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
  int t,i,j,k=0;
  cin>>t;
  int n[t],phi[t],b[t],l[t][100]={0},pi[t][100]={0};
  for(i=0;i<t;i++)
  {
    cin>>n[i]>>phi[i];
    k=0;
    while (n[i]%2 == 0) 
    { 
        pi[i][k]=2; 
        l[i][k]++; 
        n[i]= n[i]/2; 
    } 
    if(l[i][k]>0)
      k++;
    for (j=3;j<=sqrt(n[i]);j=j+2) 
    { 
        while (n[i]%j==0) 
        { 
            pi[i][k]=j; 
            l[i][k]++; 
            n[i]= n[i]/j; 
        } 
        if(l[i][k]>0)
          k++;
    }  
    if (n[i]>2) 
    { 
      pi[i][k]=n[i];
      l[i][k]++;
    } 
    if(l[i][k]>0)
         k++;
    b[i]=k;
  }
  for(i=0;i<t;i++)
  {
    cout<<b[i]<<endl;
    for(j=0;j<b[i];j++)
    {
      cout<<pi[i][j]<<" "<<l[i][j]<<endl;
    }
  }
  return 0;
}
