#include <bits/stdc++.h>
using namespace std;
#define M 1000000007
int n,m,root,BLOCK;
vector< vector<int> > g(400005);
int color[400005],temp[400005],h[400005];
vector<int> c;
vector< pair< pair<int,int> ,int> > qry;

void dfs(int u,int par)
{
    pair<int,int> p;
    p.first=c.size();
    c.push_back(color[u]);
    for(int i=0;i<g[u].size();i++)
    {
        if(g[u][i] != par)
        {
            dfs(g[u][i],u);
        }
    }
    p.second=c.size();
    c.push_back(color[u]);
    qry.push_back(make_pair(p,u));
}
bool cmp(const pair< pair<int,int>,int> &a,const pair< pair<int,int>,int> &b)
{
    int l1 = a.first.first/BLOCK;
    int l2 = b.first.first/BLOCK;
    if(l1 != l2)
        return (l1<l2);
    return l1%2 ? (a.first.second < b.first.second) : (a.first.second > b.first.second);
}
int main()
{
    scanf("%d",&n);
    BLOCK = static_cast<int>(sqrt(n));
    for(int i=2;i<=n;i++)
    {
        int u;
        scanf("%d",&u);
        u++;
        g[u].push_back(i);
        g[i].push_back(u);
    }
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&color[i]);
        temp[i]=color[i];
    }
    sort(temp,temp+n+1);
    for(int i=1;i<=n;i++)
        color[i]= lower_bound(temp,temp+n+1,color[i])-temp;
    dfs(1,0);
    sort(qry.begin(),qry.end(),cmp);
    int ml = 0,mr = -1;
    int cans=0;
    for(int i=0;i<qry.size();i++)
    {
        int l=qry[i].first.first,r=qry[i].first.second;
        while(mr < r)
        {
            mr++;
            h[c[mr]]++;
            if(h[c[mr]]==1)
                cans++;
        }
        while(ml > l)
        {
            ml--;
            h[c[ml]]++;
            if(h[c[ml]]==1)
                cans++;
        }
        while(mr > r)
        {
            h[c[mr]]--;
            if(h[c[mr]]==0)
                cans--;
            mr--;
        }
        while(ml < l)
        {            
            h[c[ml]]--;
            if(h[c[ml]]==0)
                cans--;
            ml++;
        }
        temp[qry[i].second]=cans;
    }
    long long res=1;
    for(int i=1;i<=n;i++)
    {
        res = (res%M*(long long)temp[i]%M)%M;
    }
    printf("%lld\n",res);
    return 0;
}
