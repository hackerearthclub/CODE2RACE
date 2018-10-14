#include <iostream>

using namespace std;

long int n,T;

long int fact(long int a){
    long int ft = a, res = 0;
    for(long i = 2; i < a; i++) ft *= i;
    while(ft > 0){
        res += ft % 10;
        ft /= 10;
    }
    return res;
}

int main()
{
    cin >> T;
    while(T--){
        cin >> n;
        cout<<fact(n);
    }
    return 0;
}
