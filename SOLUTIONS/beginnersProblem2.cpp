#include<iostream>
using namespace std;



int main() {
    int t;
    cin>>t;
    while(t--) {
        int n;
        cin>>n;
        int cnt = 0;
        for(int i = 0; i<n; i++) {
            int a;
            cin>>a;b
            if(!(a & 1) ) cnt++;
        }

        cout<<cnt<<endl;
    }

    return 0;
}
