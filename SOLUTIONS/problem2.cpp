/*
Author: Divya Gupta 
Problem 4
C++ Implementation
*/
#include<bits/stdc++.h> 
using namespace std;  
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int n,count=0;
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
            if(a[i]%2==0)
            count++;
        }
        cout<<count<<endl;
    }
} 