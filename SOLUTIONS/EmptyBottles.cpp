#include<bits/stdc++.h>
using namespace std;

int main() {

	int t,n;
	cin>>t;

	while(t--)
	{

		cin>>n;
		int sum=0;
		while(n--)
		{
			cin>>x;
			sum+=x;
		}
		cout<<sum/100;
	}

	return 0;

}