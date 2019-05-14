#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		int a[n];
		for(int i=0;i<n;i++)
			cin>>a[i];
		for(int i=0;i<n;i++){
			if(a[i]%2==0){
				cout<<a[i]<<endl;
				break;
			}
		}
	}
	return 0;
}