#include <iostream>
using namespace std;

long long  sumOfEvenFibonacci(long long  N) {
    long long  fibo2 = 2; //first even fibo number
    long long  fibo1 = 8; //second even fibo number
    long long  sum = fibo1 + fibo2; //note that 10 <= N <= 4e-16 so sum starts from 10
    long long  fiboN;
    //calculate the next even fibo number from the previous 2 even fibo numbers
    while (true) {
        fiboN = 4*fibo1+fibo2;
        if (fiboN >= N) {
            return sum;
        }
        sum += fiboN;
        fibo2 = fibo1;
        fibo1 = fiboN;
    }
}

int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        long long N; //use long long because N<=4e16
        cin >> N;
        cout << sumOfEvenFibonacci(N) << std::endl;
    }
    return 0;
}
