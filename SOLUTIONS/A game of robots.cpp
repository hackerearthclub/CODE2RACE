#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#define ll long long int

using namespace std;
int main(void) {
    int t;
    cin >> t;
    
    while (t--) {
        string str;
        cin >> str;
        int l = str.length(), flag = 1;//cout << l;
        int a[l] = {0};
        
        for (int i = 0; i < l; i++) {
            if (str[i] != '.') {
                int temp = str[i]-'0';
                for (int j = i; j <= i+temp && j < l; j++) a[j]++;
                for (int j = i-1; j >= i-temp && j >= 0; j--) a[j]++;
                
            }
        }
        
        for (int i = 0; i < l; i++) {//cout<< a[i] << " ";
            if (a[i] > 1) {
                flag = 0;
                break;
            }
        }
            
        if (flag) cout << "safe\n";
        else cout << "unsafe\n";
    }
}
