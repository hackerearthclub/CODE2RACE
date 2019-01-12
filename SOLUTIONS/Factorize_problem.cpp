//code for Factorize Problem

#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

int main()
{
    int T;
    cin >> T;
    while(T--){
        int n, phi, k = 0;
        cin >> n >> phi;
        int lim = n / 2;
        vector<int> fact(n);
        for(int i = 2; i <= lim; i++){
            if(n % i == 0) k++;
            while(n % i == 0){
                fact[i]++;
                n /= i;
            }
        }
        cout << k << endl;
        for(int i = 2; i <= lim; i++)
            if(fact[i] != 0) cout << i << " " << fact[i] << endl;
    }
    return 0;
}
