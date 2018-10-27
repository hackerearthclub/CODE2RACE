
// Solution to XORAGN question of codechef
#include<bits/stdc++.h>
#include<vector>
#include<iostream>
using namespace std;
int main(){
long long int test, n;
long int temp,k=0;
cin>>test;
vector<long long int > ans(test);
for (int i=0;i<test;i++){
	  cin>>n;
	  vector<long long int> arr(n);
	   temp=0;
	 for(int j=0;j<n;j++){
	 	cin>>arr[j];
	 	temp=temp^arr[j]; 
	 }
	 ans[k]=(temp<<1);
     k++;
}
for(int i=0;i<k;i++){
	cout<<ans[i]<<endl;
}
}
