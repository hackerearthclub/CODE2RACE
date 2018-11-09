
#include<bits/stdc++.h>
using namespace std;

long long solve (long long K, long long N) {
    // write code here



    vector < long long > vec (N+1);
    //vector <long long > vecK (K+1);
    //iota ( begin(vecK), end(vecK), 0);

    vec[0] = 1;
    long long sum = 1;

    for ( long long i = 1 ; i < K+1; i ++){
        vec[i] = sum ;
        sum += sum ;
        sum = sum % 1000000007;
    }

    sum -= vec[0];
    //cout << sum << endl;
    for ( long long i = K+1; i <= N; i ++){
        for ( int j = i-1 ; j >= i-K; j--)
            vec[i] += vec[j] ;
        vec[i] %= 1000000007;

    }

    for ( int i = 0 ; i <= N ; i ++ )
        cout << vec[i] << " ";

    return vec[N];
}

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int t_i=0; t_i<T; t_i++)
    {
        long long N;
        cin >> N;
        long long K;
        cin >> K;

        long long out_;
        out_ = solve(K, N);
        cout << out_;
        cout << "\n";
    }
}
