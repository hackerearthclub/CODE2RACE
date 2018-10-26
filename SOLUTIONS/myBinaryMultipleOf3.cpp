#include <iostream>
#include <math.h>
#include <cstring>

using namespace std;

int main() {
    
    int qtd, count = 0, len, exponent;
    cin >> qtd;

    for(int i = 0; i < qtd; i++) {
        char binary[100];
        cin >> binary;
        
        len = strlen(binary);
        for (int i = len; i >= 0; i--) {
            if(binary[i-1] == '1') {
                exponent = len - i;
                count += pow(2, exponent);
            }
        }
        
        if (count % 3 == 0){
            cout << "1" << endl;
        } else {
            cout << "0" << endl;
        }
        
        count = 0;
    }
    
 return 0;
}
