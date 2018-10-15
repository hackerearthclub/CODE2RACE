#include <iostream>
#include <vector>

using namespace std;

long long T,n,tmp,maxF = 0, res;
vector<long long> f,quest;

int main(){
    cin >> T;
    while(T--){
        cin >> tmp;
        maxF = max(maxF,tmp);
        quest.push_back(tmp);
    }
    //build Fibonacci array
    long long PreAns = 1, Ans = 1, fibo = PreAns + Ans;
    while(fibo <= maxF){
        if(fibo % 2 == 0) f.push_back(fibo);
        PreAns = Ans, Ans = fibo;
        fibo = PreAns + Ans;
    }
    //answer
    for(long long i = 0; i < quest.size(); i++){
        n = quest[i], res = 0;
        for(long long j = 0; f[j] <= n; j++) res += f[j];
        cout << res << endl;
    }
    return 0;
}
