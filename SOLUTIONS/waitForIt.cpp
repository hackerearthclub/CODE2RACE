#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;
const long long mod = 10e9 + 7;
int T;

int main()
{
    cin >> T;
    while(T--){
        long long res = 0, n, a, b;
        cin >> a >> b >> n;
        for(long long i = 1; i <= n; i++){
            for(long long j = 1; j <= n; j++){
                long long first  = pow(a,i) - pow(b,i),
                          second = pow(a,j) - pow(b,j);
                res = (res + __gcd( first , second )) % mod;
            }
        }
        cout << res << endl;
    }
    return 0;
}
