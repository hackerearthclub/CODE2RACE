#include<bits/stdc++.h>
using namespace std;
#define ll long long int
ll t,m,lenval;
vector<ll>posible,cc,pst;
set<ll>st;
string s;
ll fg;
ll suf[1000006],pre[1000006],vis[1005],pos[1005];
void dfs(ll rem)
{
    vis[rem]=1;
    cc.push_back(rem);
    for(auto ch:pst)
    {
        ll nw=rem*lenval+ch;
        nw%=m;
        if(pos[nw]==1)
        fg=1;
        if(!vis[nw])
        dfs(nw);
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll i,j,k;
    cin>>t;
    while(t--)
    {
        cin>>s>>m;
        s=" "+s;
        memset(vis,0,sizeof vis);
        memset(pos,0,sizeof pos);
        posible.clear();
        lenval=1;
        for(i=1;i<s.size();i++)
        {
            if(i>1)
            {
                lenval=lenval*10;
                lenval%=m;
            }
            pre[i]=pre[i-1]*10LL+(s[i]-'0');
            pre[i]%=m;
        }
        lenval%=m;
        suf[s.size()]=0;
        ll pw=1;
        pos[0]=vis[0]=1;
        for(i=s.size()-1;i>=1;i--)
        {
            suf[i]=(s[i]-'0')*pw+suf[i+1];
            suf[i]%=m;
            pw=(pw*10LL)%m;
        }
        pw=1;
        st.clear();
        pst.clear();
        ll ans=0;
        for(i=s.size()-1;i>=1;i--)
        {
            ll cmod=pre[i-1]*pw+suf[i+1];
            pw*=10LL;
            pw%=m;
            cmod%=m;
            posible.push_back(cmod);
            st.insert(cmod);
        }
        for(auto it:st)
        {
            pst.push_back(it);
        }
        for(i=0;i<posible.size();i++)
        {
            j=posible[i];
            if(vis[j]==0)
            {
                fg=0;
                cc.clear();
                dfs(j);
                if(fg==1)
                {
                    for(auto ch:cc)
                    {
                        pos[ch]=1;
                    }
                }
            }
        }
        for(i=0;i<posible.size();i++)
        {
            ans+=pos[posible[i]];
        }
        cout<<ans<<"\n";
    }
    return 0;
}
