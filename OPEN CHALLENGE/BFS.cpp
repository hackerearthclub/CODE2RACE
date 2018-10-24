#include<bits/stdc++.h>
using namespace  std;
 int color[100];
int main(){
 int v,e;
 cout<<"Enter the number of vertices and edges"<<endl;
 cin>>v>>e;
 bool visited[v]={false},flag=true;

 vector<int> adjList[v];
 for(int i=0;i<e;i++)
 {int a,b;
   cin>>a>>b;
   adjList[a-1].push_back(b-1);
   adjList[b-1].push_back(a-1);

 }
 queue<int> q;
 visited[0]=true;
 q.push(0);
 color[0]=-1;
 while(!q.empty()&&flag)
 {
   int u=q.front();
   q.pop();
  for(int i=0;i<adjList[u].size();i++)
  {
    if(visited[adjList[u][i]]==false)
    { q.push(adjList[u][i]);
      visited[adjList[u][i]]=true;
      if(color[u]==-1)
      color[adjList[u][i]]=1;
      else
      color[adjList[u][i]]=-1;
    }
    else if(color[u]==color[adjList[u][i]])
      {flag=false;
        break;
      }


  }

}
if(flag)
for(int i=0;i<v;i++)
{ if(color[i]==-1)
    cout<<i+1<<" -> "<<"W"<<endl;
  else
    cout<<i+1<<" -> "<<"B"<<endl;
}
else
cout<<"Not Possible"<<endl;
}
