#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#define ll long long
#define t(test) for(;test!=0;test--)
#define ltx(n) for(int xo=0;xo<=n-1;xo++)
#define lt(a,b) for(;a<=b;a++)
#define pb(list,temp) list.push_back(temp)
#define MAX 1000000007
#define MAXXIUS 1000003
using namespace std;
 int main(){
    ll int test,m,n,l,temp,total,hour;
    cin>>test;
    for (int i = 0; i < test; ++i) {
        vector <ll int> speed,acceleration;
        cin>>n>>m>>l;
        for (int j = 0; j < n; ++j) {
            cin>>temp;
            speed.push_back(temp);
            cin>>temp;
            acceleration.push_back(temp);
        }
        total = 0;
        for (hour = 0; total < m; ++hour) {
            total=0;
            for (int j = 0; j < speed.size(); ++j) {
                temp =  speed[j] + (hour*acceleration[j]);
                if(temp>l){
                    total = total + temp;
                }
            }
        }
        cout<<hour-1<<"\n";
    }
    return 0;
}

 // test case: 1 3 400 120 20 20 50 70 20 90 