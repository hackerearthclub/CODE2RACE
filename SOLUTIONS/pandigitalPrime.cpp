#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

bool isPrime(long long x){
    if(x < 2) return false;
    for(long long i = 2; i <= sqrt(x); i++){
        if(x % i == 0) return false;
    }
    return true;
}

bool isPandigital(long long x){
    vector<int> num(11);
    int it = 0;
    while(x > 0){
        num[it] = x % 10;
        x /= 10;
        it++;
    }
    num.resize(it);
    sort(num.begin(),num.end());
    for(int i = 0; i < it - 1; i++){
        if(num[i] == num[i+1]) return false; //check unique digits
        if(num[i] > it) return false;        //check valid number, each digit must not be greater than it's number length
    }
    if(num[it-1] > it) return false;
    return true;
}

int main()
{
    int T;
    cin >> T;
    while(T--){
        long long n, i;
        bool found = false;
        cin >> n;
        for(i = n; i > 1; i--){
            if(isPrime(i) && isPandigital(i)){
                found = true;
                break;
            }
        }
        if(found) cout << i << endl;
        else      cout << "-1" << endl;
    }
    return 0;
}
