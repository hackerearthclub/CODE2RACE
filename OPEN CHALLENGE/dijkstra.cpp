
// this is the solution for problem 743 on leetcode (network dealy problem)
// In this question we run the normal dijkstra first and then return the maximum of the shortest distances...
// Line 14 to line 32 is the main dijkstra part


int networkDelayTime(vector<vector<int>>& times, int n, int k) 
{
    vector< vector< pair<int,int> > > g(n+1);
    for(auto t : times) {
        g[t[0]].push_back({t[1], t[2]});
    }
    
    int res = INT_MIN;
    vector<int> d(n+1, INT_MAX);
    priority_queue< pair<int,int> , vector<pair<int,int>> , greater<pair<int,int>>  > pq;
    d[k] = 0;
    pq.push({0,k});
    while(!pq.empty())
    {
        pair<int,int> s = pq.top();
        pq.pop();
        int i = s.second;
        for(int j=0 ; j<g[i].size(); j++)
        {
            if(d[g[i][j].first] > d[i] + g[i][j].second)
            {
                d[g[i][j].first] = d[i] + g[i][j].second;
                pq.push({d[g[i][j].first], g[i][j].first});
            }
        }
    }
    for(int i=1;i<=n;i++)
        if(i!=k)
            res = max(res, d[i]);
    if(res == INT_MAX)
        return -1;
    return res;