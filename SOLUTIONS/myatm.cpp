#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    while(T--){
        int n,k,p;
        cin >> n >> k;
        while(n--){
            cin >> p;
            if(k >= p){
                k -= p;
                cout << "1";
            }
            else
                cout << "0";
        }
        cout << endl;
    }
    return 0;
}
