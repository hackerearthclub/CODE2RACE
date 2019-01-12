#include <iostream>

using namespace std;

int main() {

    // Number of testcases
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        // Get number of people and money in ATM
        int N,K;
        cin >> N >> K;

        // For each withdrawal, check if ATM has enough money or not.
        // If yes, print "1" and subtract that money from ATM.
        // Else, print "0".
        for (int i = 0; i < N; i++) {
            int amount;
            cin >> amount;
            if (K >= amount) {
                K -= amount;
                printf("1");
            }
            else {
                printf("0");
            }
        }
        printf("\n");

    }

    return 0;

}