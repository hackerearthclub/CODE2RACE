#include <iostream>
#include <math.h>
#include <stack>
using namespace std;

int a, type;

int OctToDec(int x){
    int i = 0, res = 0;
    while(x > 0){
        res += (x % 10) * pow(8,i);
        x /= 10;
        i++;
    }
    return res;
}

int DecToOct(int x){
    stack<int> s;
    int res = 0;
    do{
        s.push(x % 8);
        x /= 8;
    }while(x / 8 > 0);
    s.push(x % 8);
    //rebuild
    while(!s.empty()){
        res = res * 10 + s.top();
        s.pop();
    }
    return res;
}

int main()
{
    cout << "Choose type of conversion (input number only):\n"
            "1. Decimal to Octal (default)\n"
            "2. Octal to Decimal" << endl;
    cin >> type;
    cout << endl << "Please input number to convert: " << endl;
    cin >> a;
    if(type == 2) cout << OctToDec(a);
    else          cout << DecToOct(a);
    return 0;
}
