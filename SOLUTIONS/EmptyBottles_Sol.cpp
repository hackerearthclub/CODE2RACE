#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    // Get number of testcases
    int T;
    cin >> T;

    // Loop for each testcase
    while (T--) {

        // Get number of bottles and height of water
        int N;
        cin >> N;
        vector<int> bottles;
        while (N--) {
            int tmp;
            cin >> tmp;
            bottles.push_back(tmp);
        }
        // Sort bottles by height of water in ascending order
        sort(bottles.begin(), bottles.end());

        // Point fullIndex to the last not-full bottle  
        size_t fullIndex = bottles.size() - 1;
        if (bottles[fullIndex] == 100) {
            while (bottles[fullIndex] == 100) {
                fullIndex--;
            }
        }

        // Point fillIndex to first bottle
        // Fill water from fillIndex to fullIndex until both indexes are equal
        size_t fillIndex = 0;
        while (fillIndex != fullIndex) {
            if (100 - bottles[fullIndex] <= bottles[fillIndex]) {
                bottles[fullIndex] = 100;
                bottles[fillIndex] -= (100 - bottles[fullIndex]);
                fullIndex--;
            }
            else {
                bottles[fullIndex] += bottles[fillIndex];
                bottles[fillIndex] = 0;
            }
            if (bottles[fillIndex] == 0) fillIndex++;
        }

        // Print the result
        cout << bottles.size() - fullIndex - 1;
    }

    return 0;

}