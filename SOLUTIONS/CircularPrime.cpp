#include <iostream>
#include <cmath>
using namespace std;

//check if n is prime
bool isPrime(int N) {
    if (N <= 1)
        return false;

    for(int i = 2; i <= N/2; ++i) {
        if(N % i == 0)
            return false;
    }
    return true;
}

//check whether N is circular prime
bool checkCircularPrime(int N) {
    //count number of digits in N
    int count = 0;
    int temp = N;
    while (temp) {
        count++;
        temp /= 10;
    }

    //generate the next circular permutation of a number
    //by moving last digit to first position.
    int num = N;
    while (isPrime(num)) {
        int rem = num % 10;
        int div = num / 10;
        num = (pow(10, count - 1)) * rem + div;

        if (num == N)
            return true;
    }

    return false;
}

//Return the sum of circular primes that are below N
int sumOfCircularPrimes(int N) {
    int sum = 0;
    for (int i = 2; i < N; i++)
        if (checkCircularPrime(i))
            sum += i;
    return sum;
}

int main() {
    int N;
    cin >> N;
    cout << sumOfCircularPrimes(N);
    return 0;
}
