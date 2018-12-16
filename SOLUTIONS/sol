#include<bits/stdc++.h>
using namespace std;
vector<int>v[1005];
queue<int>qu;
int girls[1005];
int bfs()
{
    int mi=10005;
    while(!qu.empty())
    {
        int t=qu.front();
        for(int i=0;i<v[t].size();i++)
        {
            if(girls[v[t][i]]==1)
            {
                mi=min(mi,v[t][i]);
            }
            qu.push(v[t][i]);
        }
        if(mi!=10005)
        {
            return mi;
        }
        qu.pop();
 
    }
    return 0;
 
}
 
//int girls[1005];
int main()
{
    int n;
    cin>>n;
   // vector<int>v[n];
    int x,y;
    for(int i=0;i<n-1;i++)
    {
        cin>>x>>y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    int q;
    cin>>q;
   // bool girls[n+5]={false};
    int k;
    while(q)
    {
        cin>>k;
        girls[k]=true;
        q--;
    }
 
    qu.push(1);
    cout<<bfs()<<endl;
   // stack<int>s;
 
}
