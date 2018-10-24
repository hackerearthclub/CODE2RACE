
#include<iostream>
#include<bits/stdc++.h>
#define mod 1000000007
typedef unsigned long long int ll;
using namespace std;

int main()
{
    int m;
    cin>>m;
    ll p=1,q=0;
    while(m--)
    {
        int n;
        cin>>n;
        ll a[n],i,result=1;
        for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(i=0;i<n;i++)
    {
        p=(p*a[i])%mod;
    }
    for(i=0;i<n;i++)
    {
        q=__gcd(q,a[i]);
    }
    
    
    i=0;
    
    while(i!=q)
    {
       result=(result*p)%mod;
       i++;
    }
    cout<<result<<endl;
    
    }
    return 0;
}
