#include <bits/stdc++.h>
using namespace std;
#define FOR(i,n) for (int i = 0; i < (int)(n); ++i)
#define mod 1000000007
#define bigger(a,b) (a>b?a:b)
#define smaller(a,b) (a<b?a:b)
#define mem(A,g) memset(A,g,sizeof(A))
#define gc getchar_unlocked
#define positive(a) (bigger(a,-a))
#define INF std::numeric_limits<int>::max();
bool visited[1005];
vector<int>graph[1005];
void init()
{
	for(int i=0;i<1005;i++)
	{
		visited[i] = false;
	}
}
int query,cnt = 0;
void dfs(int check, int depth)
{
	visited[check] = true;
	for(int i=0;i<graph[check].size();i++)
	{
		if(!visited[graph[check][i]])
		{
			if(graph[check][i]==query)
			{
			    cnt = depth+1;
				return;
			}
			dfs(graph[check][i],depth+1);
		}
	}
}
bool compare(const pair<int,int>&x, const pair<int,int>&y)
{
	if(x.first!=y.first)
	{
		return x.first<y.first;
	}
	else
	{
		return x.second<y.second;
	}
}
int main() {
ios_base::sync_with_stdio(false); cin.tie(0);
int n;
cin>>n;
int u,v;
for(int i=0;i<n-1;i++)
{
	cin>>u>>v;
	graph[u].push_back(v);
	graph[v].push_back(u);
}
int q;

cin>>q;
vector<pair<int,int>>answer;
for(int i=0;i<q;i++)
{
	cnt = 0;
	cin>>query;
	init();
	dfs(1,0);
// 	cout<<cnt<<"\n";
	answer.push_back({cnt,query});
}
sort(answer.begin(),answer.end(),compare);
cout<<answer[0].second<<"\n";
return 0;
}