#include <fstream>
#include <iostream>
#include <string>

//reading from file ./input.txt

using namespace std;

string str;

int main(){
    freopen("input.txt","r",stdin);
    getline(cin,str);
    cout << "Line read:" << endl << str;
    return 0;
}
