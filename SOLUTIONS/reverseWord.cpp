#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

vector<string> a;
string tmp,t;
stringstream ss;

int main()
{
    getline(cin,t);
    ss << t;
    while(!ss.eof()){
        ss >> tmp;
        a.push_back(tmp);
    }
    for(long i = a.size()-1; i > 0; i--) cout << a[i] << " ";
    cout << a[0] << endl;
    return 0;
}
