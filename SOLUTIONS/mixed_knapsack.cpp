#include<iostream>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<bits/stdc++.h>

using namespace std;

bool byrat( pair<int,int> a, pair<int,int> b)
{
    float x=(float)a.first/a.second;
    float y=(float)b.first/b.second;
    return (x>y);
}

int main()
{
    int n1,w;
    cout<<"Enter Weight : ";
    cin>>w;

    cout<<"Enter number of items you have for 0-1 : ";
    cin>>n1;

    vector< pair<int,int> > oi;
    for(int i=0; i<n1; i++)
    {
        int temp1,temp2;
        cin>>temp1>>temp2;
        oi.push_back(make_pair(temp1,temp2));
    }

    int n2;
    cout<<"Enter number of items you have for fraction : ";
    cin>>n2;
    vector< pair<int,int> > fr;
    for(int i=0; i<n2; i++)
    {
        int temp1,temp2;
        cin>>temp1>>temp2;
        fr.push_back(make_pair(temp1,temp2));
    }

    sort(fr.begin(),fr.end(),byrat);
    int arr[w+1];
    arr[0]=0;
    for(int i=0; i<=w; i++)
    {
        arr[i]=0;
        int k=i;
        if(i!=0)
        {
            for(int j=0; j<=i; j++)
            {
                if(k<=fr[j].second)
                {
                    arr[i] += (fr[j].first*k)/fr[j].second;
                    break;
                }
                else
                {
                    arr[i] += fr[j].first;
                    k -= fr[j].second;
                }
            }
        }
        //cout<<arr[i]<<endl;
    }

    int dp[n1+1][w+1];

    for(int i=0; i<=n1; i++)
    {
        for(int j=0; j<=w; j++)
        {
            if(i==0 || j==0)
                dp[i][j]=0;
            else if(j<oi[i-1].second)
                dp[i][j]=dp[i-1][j];
            else
                dp[i][j]=max(dp[i-1][j] , dp[i-1][j-oi[i-1].second]+oi[i-1].first);
            //cout<<dp[i][j]<<" ";
        }
        //cout<<endl;
    }
    int ans=0;

    for(int i=0; i<=w; i++)
    {
        ans=max(ans,dp[n1][i]+arr[w-i]);
    }

    cout<<ans;
    return 0;
}
