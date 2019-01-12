#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,k,a;
        cin>>n>>k;
        while(n--)
        {
            cin>>a;
            if(k>=a)
            {
                k=k-a;
                cout<<"1";
            }
            
            else
            {
                cout<<"0";
            }
            
        }
        cout<<endl;
    }
}