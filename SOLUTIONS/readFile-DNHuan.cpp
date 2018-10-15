#include <fstream>
#include <iostream>
#include <string>

using namespace std;

string str;

int main()
{
    freopen("D:/input.txt","r",stdin);
    getline(cin,str);
    cout << "Line read:" << endl << str;
    return 0;
}
