#include <iostream>
#include <cmath>
using namespace std;

int sumNthPowerOfDigit(int N) {
    int finalSum = 0;

    // (N+1)*pow(9,N) is the upper limit of the brute-force search
    for (int number = 2; number < (N+1)*pow(9,N); number++) {
        int sumOfPowers = 0;

        //go through each digit, calculate digit^N, and add to sumOfPowers
        int tempNumber = number;
        while (tempNumber > 0) {
            int digit = tempNumber % 10;
            tempNumber /= 10;
            sumOfPowers += pow(digit,N);
        }

        if (sumOfPowers == number) {
            finalSum += number;
        }
    }
    return finalSum;
}

int main() {
    int N;
    cin >> N;
    cout << sumNthPowerOfDigit(N);
    return 0;
}
